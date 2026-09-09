import importlib.util
import math
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "empirical_review", ROOT / "scripts/analysis/build_empirical_review_package.py"
)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)


class EmpiricalReviewPackageTests(unittest.TestCase):
    def setUp(self):
        self.samples, self.census_issues, self.exclusions, self.transitions = mod.build_sample_sensitivity()
        self.by_rule = {r["rule"]: r for r in self.samples}
        self.bps, self.d = mod.build_bps_certification()
        self.bps_by_id = {r["check_id"]: r for r in self.bps}

    def test_sample_rules_are_explicit_and_separate(self):
        self.assertEqual(len(self.samples), 5)
        self.assertEqual(self.by_rule["R0_strict_explicit_country_direct"]["adjacent_transitions"], 0)
        self.assertEqual(self.by_rule["R1_indonesia_aligned_segment_only"]["adjacent_transitions"], 1)
        self.assertEqual(self.by_rule["R2_exclude_overseas_group_keep_segment_candidates"]["adjacent_transitions"], 6)
        self.assertEqual(self.by_rule["R3_all_direct_candidate_series"]["adjacent_transitions"], 9)
        self.assertEqual(self.by_rule["R4_conditional_indonesia_country_reconstructions"]["adjacent_transitions"], 4)

    def test_direct_sensitivity_counts(self):
        r2 = self.by_rule["R2_exclude_overseas_group_keep_segment_candidates"]
        self.assertEqual(r2["opposite_sign_transitions"], 3)
        self.assertAlmostEqual(float(r2["median_abs_growth_gap_pp"]), 52.5178802962, places=5)
        r3 = self.by_rule["R3_all_direct_candidate_series"]
        self.assertEqual(r3["opposite_sign_transitions"], 3)
        self.assertEqual(r3["revenue_growth_outpaces"], 6)
        self.assertEqual(r3["activity_growth_outpaces"], 3)
        self.assertAlmostEqual(float(r3["median_abs_growth_gap_pp"]), 42.9401737278, places=5)

    def test_conditional_cases_not_mixed_with_direct(self):
        r = self.by_rule["R4_conditional_indonesia_country_reconstructions"]
        self.assertEqual(r["adjacent_transitions"], 4)
        self.assertEqual(r["opposite_sign_transitions"], 0)
        self.assertIn("sensitivity", r["interpretation_note"].lower())

    def test_tokopedia_fy2021_stale_census_admission_detected(self):
        self.assertEqual(len(self.census_issues), 1)
        issue = self.census_issues[0]
        self.assertEqual(issue["issue_id"], "STALE-TOKOPEDIA-FY2021")
        self.assertEqual(issue["certified_treatment"], "EXCLUDE")

    def test_hard_exclusions_include_tokopedia_and_bukalapak(self):
        keys = {(r["platform"], r["period"]) for r in self.exclusions}
        self.assertIn(("Tokopedia e-commerce segment", "FY2021"), keys)
        self.assertIn(("Bukalapak", "FY2024"), keys)

    def test_bps_internal_checks(self):
        self.assertEqual(len(self.bps), 7)
        self.assertEqual(self.bps_by_id["BPS-01"]["status"], "PASS_INTERNAL")
        self.assertEqual(self.bps_by_id["BPS-05"]["status"], "PASS_INTERNAL")
        self.assertEqual(self.bps_by_id["BPS-06"]["status"], "BLOCKED_SOURCE_CONFLICT")
        self.assertEqual(self.bps_by_id["BPS-07"]["status"], "PASS_WITH_SOURCE_RESIDUAL")
        self.assertEqual(self.d["province24_total_diff"], 1)

    def test_bps_conditional_growth_calculation(self):
        self.assertAlmostEqual(self.d["total_growth_pct"], 17.0843082934, places=5)
        self.assertAlmostEqual(self.d["marketplace24_derived_value"], 203.522047, places=5)
        self.assertAlmostEqual(self.d["marketplace_growth_pct"], 1.4164605342, places=5)
        self.assertEqual(self.bps_by_id["BPS-02"]["status"], "CONDITIONAL_SOURCE_CONCORDANCE")

    def test_province_common_coverage(self):
        self.assertEqual(self.d["common_provinces"], 38)
        self.assertEqual(self.d["complete_common_provinces"], 36)

    def test_advisor_outputs_do_not_claim_approval(self):
        review = mod.build_kong_review(self.samples, self.census_issues, self.exclusions, self.bps, self.d)
        sheet = mod.build_decision_sheet(self.samples, self.bps)
        self.assertIn("not a manuscript rewrite", review)
        self.assertIn("No manuscript rewrite", sheet)
        self.assertIn("Do not advertise one final N", review)
        self.assertNotIn("advisor-approved final sample", review.lower())

    def test_deterministic_generation(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            mod.write_csv(out / "samples.csv", self.samples)
            first = (out / "samples.csv").read_bytes()
            samples2, _, _, _ = mod.build_sample_sensitivity()
            mod.write_csv(out / "samples.csv", samples2)
            self.assertEqual(first, (out / "samples.csv").read_bytes())


if __name__ == "__main__":
    unittest.main()
