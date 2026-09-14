import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "certified_review", ROOT / "scripts/analysis/build_empirical_review_certified.py"
)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)


class CertifiedReviewTests(unittest.TestCase):
    def setUp(self):
        self.base = mod.load_base()
        self.samples, self.census_issues, self.exclusions, _ = self.base.build_sample_sensitivity()
        self.checks, self.d = mod.certified_bps_checks(self.base)
        self.by_id = {r["check_id"]: r for r in self.checks}
        self.census = mod.build_certified_census(self.base)
        self.counts = mod.certified_headline_counts(self.census)

    def test_later_official_growth_resolves_series_choice(self):
        self.assertEqual(self.by_id["BPS-06"]["status"], "RESOLVED_FOR_CROSS_YEAR_SERIES")
        self.assertAlmostEqual(self.d["business_growth_selected_pct"], 15.3067924281, places=5)
        self.assertAlmostEqual(self.d["business_growth_alternative_pct"], 11.8422681075, places=5)
        self.assertAlmostEqual(self.d["business_growth_later_official_pct"], 15.30, places=2)
        self.assertLess(abs(self.d["business_growth_selected_pct"] - 15.30), 0.02)
        self.assertGreater(abs(self.d["business_growth_alternative_pct"] - 15.30), 1.0)

    def test_source_conflict_is_preserved_not_erased(self):
        evidence = self.by_id["BPS-06"]["evidence"]
        self.assertIn("3,934,981", evidence)
        self.assertIn("3,816,750", evidence)
        self.assertIn("preserve", self.by_id["BPS-06"]["consequence"].lower())

    def test_marketplace_growth_stays_conditional(self):
        self.assertEqual(self.by_id["BPS-02"]["status"], "CONDITIONAL_SOURCE_CONCORDANCE")

    def test_tokopedia_fy2021_is_corrected_in_certified_census(self):
        rows = [r for r in self.census if r.get("platform", "").startswith("Tokopedia") and r.get("period") == "FY2021"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["certified_admission_status"], "exclude_period_mismatch")
        self.assertEqual(rows[0]["certified_ratio_eligible"], "False")
        self.assertEqual(rows[0]["admission_status"], "candidate_core")  # historical field preserved

    def test_certified_headline_counts(self):
        self.assertEqual(self.counts["direct_candidate_periods_after_hard_exclusion"], 13)
        self.assertEqual(self.counts["direct_candidate_positive_denominator_periods"], 12)
        self.assertEqual(self.counts["retained_indonesia_extension_periods"], 8)
        self.assertEqual(self.counts["conditional_country_periods"], 6)
        self.assertEqual(self.counts["retained_tokopedia_direct_segment_periods"], 2)

    def test_certified_review_stays_empirical(self):
        text = mod.build_certified_review(
            self.base, self.samples, self.census_issues, self.exclusions, self.checks, self.d, self.counts
        )
        self.assertIn("empirical review package only", text)
        self.assertIn("Certified headline-count correction", text)
        self.assertIn("cross-year business-count resolution", text)
        self.assertIn("Decisions requested from the advisor", text)
        self.assertNotIn("rewrite the thesis now", text.lower())


if __name__ == "__main__":
    unittest.main()
