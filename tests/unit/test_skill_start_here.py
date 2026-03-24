import unittest
from tests.test_helpers import REPO_ROOT


SKILL_PATH = REPO_ROOT / "skills/lpa-start-here/SKILL.md"


class StartHereSkillTests(unittest.TestCase):
    def setUp(self):
        self.content = SKILL_PATH.read_text()

    def test_tier_definitions_are_present(self):
        self.assertIn("Tier 1", self.content)
        self.assertIn("Tier 2", self.content)
        self.assertIn("Tier 3", self.content)

    def test_tier_timelines_are_present(self):
        self.assertIn("6–10 weeks", self.content)
        self.assertIn("2–3 weeks", self.content)
        self.assertIn("2–3 hours", self.content)

    def test_tier1_stage_names_are_present(self):
        self.assertIn("Narrative Hypothesis", self.content)
        self.assertIn("Low-Signal Deploy", self.content)
        self.assertIn("Narrative Lock", self.content)
        self.assertIn("Distribution Test", self.content)
        self.assertIn("Lightning Strike GA", self.content)

    def test_slack_template_fields_are_present(self):
        self.assertIn("What:", self.content)
        self.assertIn("Why:", self.content)
        self.assertIn("Who it affects:", self.content)
        self.assertIn("How to use it:", self.content)
        self.assertIn("Known limitations:", self.content)

    def test_escalation_tiebreaker_question_is_present(self):
        self.assertIn("If we get the positioning wrong on this release", self.content)
        self.assertIn("does it cost us a deal", self.content)

    def test_q1_to_q4_output_mapping_table_exists(self):
        self.assertIn("Q1–Q4 Outputs-To Mapping", self.content)
        self.assertIn("Feeds", self.content)
        self.assertIn("Where it lands", self.content)
        self.assertIn("Launch Triage Matrix", self.content)
        self.assertIn("Stage Gate Architecture", self.content)

    def test_q_to_artifact_mappings_are_present(self):
        self.assertIn("Risk & Assumption Register", self.content)
        self.assertIn("Customer Interview", self.content)
        self.assertIn("Positioning Canvas", self.content)
        self.assertIn("PR-FAQ Template", self.content)

    def test_tier3_approval_protocol_silence_equals_approval(self):
        self.assertIn("PMM silence = approval", self.content)

    def test_tier3_slack_template_has_pmm_owner_field(self):
        self.assertIn("Tag [PMM owner]", self.content)


if __name__ == "__main__":
    unittest.main()
