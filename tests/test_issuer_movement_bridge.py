import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/analysis/build_issuer_movement_bridge.py"
spec = importlib.util.spec_from_file_location("issuer_bridge", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class IssuerMovementBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.series, cls.exclusions = mod.load_series()
        cls.transitions = mod.build_transitions(cls.series)

    def test_expected_series_and_transition_counts(self):
        self.assertEqual(len(self.series), 18)
        self.assertEqual(len(self.transitions), 13)
        self.assertEqual(len(self.exclusions), 2)

    def test_tokopedia_fy2021_is_hard_excluded(self):
        years = [r["year"] for r in self.series if r["platform"] == "Tokopedia"]
        self.assertEqual(years, [2022, 2023])
        excluded = [r for r in self.exclusions if r["platform"].startswith("Tokopedia")]
        self.assertEqual(len(excluded), 1)
        self.assertIn("post-acquisition", excluded[0]["reason"])

    def test_bukalapak_2024_period_mismatch_is_excluded(self):
        years = [r["year"] for r in self.series if r["platform"] == "Bukalapak"]
        self.assertEqual(years, [2020, 2021, 2022, 2023])
        self.assertTrue(any(r["platform"] == "Bukalapak" and r["period"] == "FY2024" for r in self.exclusions))

    def test_blibli_2020_unit_conversion(self):
        r = next(r for r in self.series if r["platform"] == "Blibli/GDN" and r["year"] == 2020)
        self.assertAlmostEqual(r["transaction_value"], 13708.846, places=6)
        self.assertAlmostEqual(r["revenue_value"], 169.633, places=6)
        self.assertEqual(r["currency_unit"], "IDR billion")

    def test_direct_and_conditional_stay_separate(self):
        direct = [r for r in self.transitions if r["evidence_class"] == "direct_candidate"]
        conditional = [r for r in self.transitions if r["evidence_class"] == "conditional_country_reconstruction"]
        self.assertEqual(len(direct), 9)
        self.assertEqual(len(conditional), 4)

    def test_direct_sign_reversals_are_exactly_three(self):
        direct = [r for r in self.transitions if r["evidence_class"] == "direct_candidate"]
        reversals = [
            (r["platform"], r["from_year"], r["to_year"], r["movement_pattern"])
            for r in direct
            if r["movement_pattern"] in {"activity_up_revenue_down", "activity_down_revenue_up"}
        ]
        self.assertEqual(
            reversals,
            [
                ("Blibli/GDN", 2020, 2021, "activity_up_revenue_down"),
                ("Blibli/GDN", 2024, 2025, "activity_down_revenue_up"),
                ("Tokopedia", 2022, 2023, "activity_down_revenue_up"),
            ],
        )

    def test_key_growth_rates(self):
        by_key = {(r["platform"], r["from_year"], r["to_year"]): r for r in self.transitions}
        toko = by_key[("Tokopedia", 2022, 2023)]
        self.assertAlmostEqual(toko["activity_growth_pct"], -8.8999, places=3)
        self.assertAlmostEqual(toko["revenue_growth_pct"], 53.1960, places=3)
        blibli = by_key[("Blibli/GDN", 2024, 2025)]
        self.assertAlmostEqual(blibli["activity_growth_pct"], -1.8871, places=3)
        self.assertAlmostEqual(blibli["revenue_growth_pct"], 12.0665, places=3)

    def test_direct_median_absolute_growth_gap(self):
        direct = [r for r in self.transitions if r["evidence_class"] == "direct_candidate"]
        self.assertAlmostEqual(
            mod.median(r["abs_growth_gap_pp"] for r in direct),
            42.9402,
            places=3,
        )

    def test_output_is_reproducible(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            mod.write_csv(out / "annual_series.csv", self.series)
            mod.write_csv(out / "adjacent_growth_transitions.csv", self.transitions)
            mod.write_csv(out / "exclusions.csv", self.exclusions)
            summary1 = mod.build_summary(self.transitions, self.exclusions)
            summary2 = mod.build_summary(self.transitions, self.exclusions)
            self.assertEqual(summary1, summary2)
            self.assertIn("9 adjacent annual transitions", summary1)
            self.assertIn("3** transitions", summary1)


if __name__ == "__main__":
    unittest.main()
