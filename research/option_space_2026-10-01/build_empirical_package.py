"""Builds the empirical package (code, tables, public inputs, registration, README, manifest) from the tracked files of this repository.
Usage: python3 build_empirical_package.py OUT_DIR   (from anywhere; writes OUT_DIR/ and OUT_DIR.zip)
Licensed data are never in the repository, and two derived firm-level panels from licensed prices are left out on purpose (see the README).
Only tracked files are copied (git ls-files), so scratch files cannot slip in."""
import csv, datetime, hashlib, os, re, shutil, subprocess, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
R = "research/option_space_2026-10-01/"
out = os.path.abspath(sys.argv[1]); shutil.rmtree(out, ignore_errors=True); os.makedirs(out)
tracked = subprocess.run(["git", "-C", ROOT, "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
# the thirteen inputs outside research/ that the rebuild reads (found by logging every file the rebuild opened)
INPUTS = """data/asean_context/asean_worldbank_context_2000_2025.csv
data/global_ecommerce/global_platform_definition_map.csv
data/global_ecommerce/global_platform_growth_divergence.csv
data/global_ecommerce/global_platform_matched_annual.csv
data/global_ecommerce/global_platform_summary.csv
data/indonesia_fy2023/fy2023_indonesia_main_rebuilt.csv
data/longitudinal/annual_extension_panel_preliminary.csv
data/measurement/results/tokopedia_fy2022_2023_revenue_incentive_reconciliation.csv
outputs/hypothesis_tests_2026-09-10/bps_national_levels.csv
outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_levels.csv
outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_candidate_transitions.csv
outputs/hypothesis_tests_2026-09-10/indonesia_longitudinal_transition_summary.csv
outputs/payment_ledger_2026-09-11/bps_payment_growth_comparison_2023_2024.csv""".split()
LEFT_OUT = {R + "tables/event_study_panel.csv", R + "tables/event_study_surprise_panel.csv",
            R + "tables/src/drive_discover_test_report.json",      # a scratch report of another tool, unrelated to the analysis
            R + "v_definition_map.py"}                           # reads a local filing corpus by absolute path; not rebuilt and not used in the thesis text
keep = []
for f in tracked:
    if f in INPUTS or f in ("papers/thesis_2026-10/figures/make_figures.py", "papers/thesis_2026-10/figures/make_fig3_1.py") \
       or re.fullmatch(r"papers/thesis_2026-10/figures/(fig[0-9_a-z]+\.png|fonts/[^/]+)", f):
        keep.append(f); continue
    if not f.startswith(R) or f in LEFT_OUT: continue
    rel = f[len(R):]
    if re.fullmatch(r"[A-Za-z0-9_]+\.py", rel) or rel in ("rebuild_all.sh", "PREREGISTRATION.md", "LICENSED_DATA.md") \
       or rel.startswith("publishable_track/") or rel.startswith("tables/"):
        if rel in ("build_empirical_package.py", "advisor_package.py"): continue
        keep.append(f)
missing = [i for i in INPUTS if i not in tracked]
assert not missing, missing
for f in keep:
    d = os.path.join(out, f); os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy2(os.path.join(ROOT, f), d)
# patches to the copies: author's machine paths in run lines; the event-study step is skipped when its panels are absent
n_patched = 0
for dp, _, fs in os.walk(os.path.join(out, R)):
    for fn in fs:
        if fn.endswith(".py"):
            p = os.path.join(dp, fn); s = open(p, encoding="utf-8").read()
            s2 = re.sub(r"PYTHONPATH=/home/phyrexian/\.local/lib/python3\.13/site-packages ", "", s)
            if s2 != s: open(p, "w", encoding="utf-8").write(s2); n_patched += 1
rb = os.path.join(out, R, "rebuild_all.sh"); s = open(rb).read()
line = [l for l in s.splitlines() if l.startswith("step event_study_panel_check.py")][0]
s = s.replace(line, 'if [ -f tables/event_study_panel.csv ]; then ' + line.split("#")[0].strip() + '; else echo "== skipped event_study_panel_check.py (licensed-price panels are not in this package)"; fi')
open(rb, "w").write(s)
# README and manifest
readme = open(os.path.join(HERE, "empirical_package_README.md"), encoding="utf-8").read()
today = datetime.date.today().isoformat()
summary = os.environ.get("LEDGER_SUMMARY", "all ledger rows PASS")
open(os.path.join(out, "README.md"), "w", encoding="utf-8").write(readme.replace("{DATE}", today).replace("{LEDGER_SUMMARY}", summary))
rows = []
for dp, _, fs in os.walk(out):
    for fn in sorted(fs):
        p = os.path.join(dp, fn); rel = os.path.relpath(p, out)
        if rel == "MANIFEST.csv": continue
        rows.append((rel, os.path.getsize(p), hashlib.sha256(open(p, "rb").read()).hexdigest()))
rows.sort()
with open(os.path.join(out, "MANIFEST.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["path", "bytes", "sha256"]); w.writerows(rows)
with zipfile.ZipFile(out + ".zip", "w", zipfile.ZIP_DEFLATED) as z:
    base = os.path.basename(out)
    for dp, _, fs in os.walk(out):
        for fn in sorted(fs):
            p = os.path.join(dp, fn); z.write(p, os.path.join(base, os.path.relpath(p, out)))
print(f"{len(rows)} files, {sum(r[1] for r in rows)/1e6:.1f} MB, {n_patched} scripts with the run line cleaned; zip {os.path.getsize(out + '.zip')/1e6:.1f} MB")
