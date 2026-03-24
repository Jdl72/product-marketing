import unittest
from tests.test_helpers import REPO_ROOT


SKILL_PATH = REPO_ROOT / "skills/lpa-weekly-discovery-log/SKILL.md"


class WeeklyDiscoveryLogSkillTests(unittest.TestCase):
    def setUp(self):
        self.text = SKILL_PATH.read_text()

    def test_section_3_insight_pattern_tracker_is_present(self):
        self.assertIn("SECTION 3", self.text)
        self.assertIn("INSIGHT PATTERN TRACKER", self.text)

    def test_section_4_positioning_pivot_log_is_present(self):
        self.assertIn("SECTION 4", self.text)
        self.assertIn("POSITIONING PIVOT LOG", self.text)

    def test_section_5_how_to_use_is_present(self):
        self.assertIn("SECTION 5", self.text)
        self.assertIn("HOW TO USE THIS LOG", self.text)

    def test_pattern_id_schema_is_present(self):
        self.assertIn("Pattern ID", self.text)
        self.assertIn("PAT-", self.text)

    def test_validation_rate_threshold_60_percent(self):
        self.assertIn("60%", self.text)

    def test_validation_rate_threshold_40_percent(self):
        self.assertIn("40%", self.text)

    def test_evidence_strength_strong_defined(self):
        self.assertIn("Strong", self.text)

    def test_evidence_strength_moderate_defined(self):
        self.assertIn("Moderate", self.text)

    def test_evidence_strength_weak_defined(self):
        self.assertIn("Weak", self.text)

    def test_escalation_rule_below_40_percent(self):
        self.assertIn("40%", self.text)
        self.assertIn("escalat", self.text)

    def test_pivot_log_has_previous_position_field(self):
        self.assertIn("Previous Position", self.text)

    def test_pivot_log_has_new_position_field(self):
        self.assertIn("New Position", self.text)

    def test_14_column_log_includes_confidence_shift(self):
        self.assertIn("Confidence Shift", self.text)

    def test_14_column_log_includes_strategic_implication(self):
        self.assertIn("Strategic Implication", self.text)

    def test_competitive_intelligence_log_in_handoff(self):
        self.assertIn("Competitive Intelligence Log", self.text)


if __name__ == "__main__":
    unittest.main()
