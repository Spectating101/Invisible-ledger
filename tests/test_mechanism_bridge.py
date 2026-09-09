import importlib.util
import math
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "mechanism_bridge", ROOT / "scripts/analysis/build_mechanism_bridge.py"
)
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)


class MechanismBridgeTests(unittest.TestCase):
    def setUp(self):
        self.cases, self.d = mod.build_cases()
        self.by_id = {r["case_id"]: r for r in self.cases}

    def test_four_cases_and_unique_ids(self):
        self.assertEqual(len(self.cases), 4)
        self.assertEqual(len(self.by_id), 4)

    def test_blibli_2022_2023_identity_and_shares(self):
        self.assertEqual(self.d["blibli_2022_2023_revenue_increase"], 664)
        self.assertEqual(self.d["blibli_2022_2023_promotion_reduction"], 262)
        self.assertEqual(self.d["blibli_2022_2023_net_revenue_increase"], 926)
        self.assertTrue(math.isclose(
            self.d["blibli_2022_2023_revenue_share"], 664 / 926, rel_tol=0, abs_tol=1e-12
        ))
        self.assertTrue(math.isclose(
            self.d["blibli_2022_2023_promotion_share"], 262 / 926, rel_tol=0, abs_tol=1e-12
        ))
        self.assertTrue(math.isclose(
            self.d["blibli_2022_2023_revenue_share"] + self.d["blibli_2022_2023_promotion_share"],
            1.0, rel_tol=0, abs_tol=1e-12
        ))

    def test_tokopedia_is_opposite_sign_and_matches_reconciliation(self):
        r = self.by_id["tokopedia_2022_2023_incentive_reconciliation"]
        self.assertLess(r["activity_growth_pct"], 0)
        self.assertGreater(r["recognized_revenue_growth_pct"], 0)
        self.assertAlmostEqual(r["activity_growth_pct"], -8.9000004488, places=7)
        self.assertAlmostEqual(r["recognized_revenue_growth_pct"], 53.1955864159, places=7)
        self.assertIn("60.56%", r["mechanism_evidence"])
        self.assertEqual(r["mechanism_status"], "arithmetic_reconciliation")

    def test_blibli_2024_2025_is_margin_mix_sign_reversal(self):
        r = self.by_id["blibli_3p_2024_2025_margin_mix"]
        self.assertLess(r["activity_growth_pct"], 0)
        self.assertGreater(r["recognized_revenue_growth_pct"], 0)
        self.assertGreater(r["other_metric_growth_pct"], 0)
        self.assertAlmostEqual(r["activity_growth_pct"], -1.8871057001, places=7)
        self.assertAlmostEqual(r["recognized_revenue_growth_pct"], 12.0664739884, places=7)
        self.assertAlmostEqual(r["other_metric_growth_pct"], 13.9255702281, places=7)
        self.assertGreater(r["monetization_change_pp"], 0)
        self.assertEqual(r["mechanism_status"], "issuer_documented_business_mix_and_efficiency")

    def test_unresolved_case_stays_unresolved(self):
        r = self.by_id["blibli_3p_2020_2021_unresolved"]
        self.assertEqual(r["mechanism_status"], "unresolved")
        self.assertIn("sufficient to explain", r["mechanism_evidence"])
        self.assertLess(r["recognized_revenue_growth_pct"], 0)
        self.assertGreater(r["activity_growth_pct"], 0)

    def test_generated_markdown_contains_bounded_interpretation(self):
        text = mod.build_markdown(self.cases, self.d)
        self.assertIn("economically non-equivalent state variables", text)
        self.assertIn("unresolved mechanism", text)
        self.assertIn("not a causal", text)
        self.assertNotIn("missing GDP estimate", text)

    def test_deterministic_generation(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            cases1, d1 = mod.build_cases()
            mod.write_csv(out / "a.csv", cases1)
            (out / "a.md").write_text(mod.build_markdown(cases1, d1), encoding="utf-8")
            first_csv = (out / "a.csv").read_bytes()
            first_md = (out / "a.md").read_bytes()
            cases2, d2 = mod.build_cases()
            mod.write_csv(out / "a.csv", cases2)
            (out / "a.md").write_text(mod.build_markdown(cases2, d2), encoding="utf-8")
            self.assertEqual(first_csv, (out / "a.csv").read_bytes())
            self.assertEqual(first_md, (out / "a.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
