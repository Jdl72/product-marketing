import unittest
from tests.test_helpers import REPO_ROOT


SKILL_PATH = REPO_ROOT / "skills/lpa-risk-and-assumption-register/SKILL.md"


class RiskRegisterSkillTests(unittest.TestCase):
    def setUp(self):
        self.content = SKILL_PATH.read_text()

    def test_fmea_formula_is_present(self):
        # Accept either "SEV × OCC × DET" or "RPN = SEV"
        has_formula = ("SEV × OCC × DET" in self.content) or ("RPN = SEV" in self.content)
        self.assertTrue(has_formula, "FMEA formula not found in SKILL.md")

    def test_all_four_priority_thresholds_are_present(self):
        for threshold in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
            self.assertIn(threshold, self.content)

    def test_priority_threshold_rpn_values_are_present(self):
        self.assertIn("200", self.content)
        self.assertIn("100", self.content)
        self.assertIn("40", self.content)

    def test_validation_status_field_is_present(self):
        self.assertIn("Validation Status", self.content)

    def test_all_seven_validation_status_values_are_listed(self):
        for status in ["Open", "Testing", "Validated", "Falsified", "Mitigated", "Accepted", "Escalated"]:
            self.assertIn(status, self.content)

    def test_post_mitigation_fields_are_present(self):
        self.assertIn("Post-Mitigation SEV", self.content)
        self.assertIn("Post-Mitigation OCC", self.content)
        self.assertIn("Post-Mitigation RPN", self.content)

    def test_register_summary_section_exists(self):
        has_summary = ("Register Summary" in self.content) or ("REGISTER SUMMARY" in self.content)
        self.assertTrue(has_summary, "Register Summary section not found in SKILL.md")

    def test_evidence_required_is_separate_from_test_method(self):
        self.assertIn("Evidence Required", self.content)
        self.assertIn("Test Method", self.content)
        # Confirm they appear as distinct entries, not combined into one field
        evidence_pos = self.content.index("Evidence Required")
        test_method_pos = self.content.index("Test Method")
        self.assertNotEqual(evidence_pos, test_method_pos)

    def test_owner_and_due_date_fields_are_present(self):
        self.assertIn("Owner", self.content)
        self.assertIn("Due Date", self.content)

    def test_date_added_field_is_present(self):
        self.assertIn("Date Added", self.content)

    def test_summary_health_metrics_are_present(self):
        self.assertIn("Avg RPN", self.content)
        self.assertIn("Max RPN", self.content)

    def test_post_mitigation_rescoring_instruction_is_present(self):
        self.assertIn("Post-Mitigation Re-Scoring", self.content)


if __name__ == "__main__":
    unittest.main()
