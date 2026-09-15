import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "data/quality_control/issuer_admission_policy_candidate_2026-09-15.json"
CURRENT_STATUS_PATH = ROOT / "docs/CURRENT_STATUS.md"
HUMAN_POLICY_PATH = ROOT / "docs/ISSUER_ADMISSION_POLICY_CANDIDATE_2026-09-15.md"


class IssuerAdmissionPolicyCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
        cls.domains = {row["id"]: row for row in cls.policy["domains"]}
        cls.current_status = CURRENT_STATUS_PATH.read_text(encoding="utf-8")
        cls.human_policy = HUMAN_POLICY_PATH.read_text(encoding="utf-8")

    def test_candidate_does_not_claim_advisor_approval(self):
        self.assertEqual(
            self.policy["status"],
            "RESEARCHER_CANDIDATE_ADVISOR_RATIFICATION_REQUIRED",
        )
        self.assertFalse(self.policy["advisor_approved"])
        self.assertFalse(self.policy["changes_current_status"])
        self.assertIn("No expanded sample is represented here as advisor-approved", self.current_status)
        self.assertIn("ADVISOR_RATIFICATION_REQUIRED", self.human_policy)

    def test_indonesia_remains_the_proposed_main_geography(self):
        self.assertEqual(self.policy["proposed_main_geography"], "Indonesia")
        self.assertIn("The proposed main geography is Indonesia", self.current_status)

    def test_direct_longitudinal_inventory_preserves_scope_labels(self):
        direct = self.domains["B_DIRECT_ISSUER_LONGITUDINAL"]
        self.assertEqual(direct["periods"], 13)
        self.assertEqual(direct["positive_base_transitions"], 9)
        self.assertFalse(direct["pool_levels_as_indonesia_panel"])

        series = {row["name"]: row for row in direct["series"]}
        self.assertEqual(series["Tokopedia e-commerce"]["periods"], 2)
        self.assertEqual(series["Blibli 3P"]["periods"], 7)
        self.assertEqual(series["Bukalapak Group"]["periods"], 4)
        self.assertIn("not a literal geographic country line", series["Tokopedia e-commerce"]["scope_label"])
        self.assertIn("OTA/travel", series["Blibli 3P"]["scope_label"])
        self.assertIn("overseas operations", series["Bukalapak Group"]["scope_label"])

    def test_conditional_and_external_evidence_do_not_enter_direct_core(self):
        conditional = self.domains["C_CONDITIONAL_COUNTRY_RECONSTRUCTION"]
        external = self.domains["D_EXTERNAL_CORROBORATION"]
        self.assertEqual(conditional["admission"], "CONDITIONAL_ONLY_NOT_DIRECT_CORE")
        self.assertFalse(conditional["pool_with_domain_b"])
        self.assertFalse(external["validate_indonesia_allocation"])
        self.assertFalse(external["pool_with_indonesia_n"])

    def test_revenue_basis_is_within_series_not_synthetic_cross_platform_harmonization(self):
        rule = self.policy["revenue_basis_rule"]
        self.assertFalse(rule["force_common_cross_platform_revenue_definition"])
        self.assertEqual(rule["primary_comparison"], "within_series")
        self.assertEqual(rule["cross_platform_levels"], "descriptive_scope_labelled_only")
        self.assertEqual(
            rule["cross_platform_growth_summaries"],
            "diagnostic_not_common_level_panel_estimate",
        )

    def test_hard_exclusions_and_diagnostics_match_current_certification(self):
        exclusions = {(row["series"], row["period"]) for row in self.policy["hard_exclusions"]}
        self.assertEqual(exclusions, {("Tokopedia", "FY2021"), ("Bukalapak", "FY2024")})

        direct = self.policy["diagnostics"]["domain_b"]
        self.assertEqual(direct["transitions"], 9)
        self.assertEqual(direct["revenue_growth_faster"], 6)
        self.assertEqual(direct["transaction_growth_faster"], 3)
        self.assertEqual(direct["opposite_sign_transitions"], 3)
        self.assertAlmostEqual(direct["median_absolute_growth_divergence_pp"], 42.94, places=2)

        all_tier = self.policy["diagnostics"]["all_tier_inventory"]
        self.assertEqual(all_tier["levels"], 17)
        self.assertEqual(all_tier["transitions"], 12)
        self.assertAlmostEqual(all_tier["median_absolute_growth_divergence_pp"], 42.02, places=2)

    def test_ratification_question_preserves_inference_boundary(self):
        question = self.policy["advisor_ratification_question"]
        self.assertIn("scope-labelled direct issuer longitudinal evidence set", question)
        self.assertIn("not treating the 13 periods as one Indonesia country panel", question)
        self.assertIn("update docs/CURRENT_STATUS.md", self.policy["effect_if_ratified"][0])


if __name__ == "__main__":
    unittest.main()
