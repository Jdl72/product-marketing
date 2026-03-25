import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


SKILL_PATH = REPO_ROOT / "skills/lpa-customer-interview/SKILL.md"


class TestSkillCustomerInterview(unittest.TestCase):
    def setUp(self):
        self.text = SKILL_PATH.read_text()

    # Section codes
    def test_section_code_2a_present(self):
        self.assertIn("§2A", self.text)

    def test_section_code_2b_present(self):
        self.assertIn("§2B", self.text)

    def test_section_code_2c_present(self):
        self.assertIn("§2C", self.text)

    def test_section_code_2d_present(self):
        self.assertIn("§2D", self.text)

    def test_section_code_2e_present(self):
        self.assertIn("§2E", self.text)

    def test_section_code_2f_present(self):
        self.assertIn("§2F", self.text)

    def test_section_code_2g_present(self):
        self.assertIn("§2G", self.text)

    def test_section_code_2h_present(self):
        self.assertIn("§2H", self.text)

    # Interview phases
    def test_phase_prepare_present(self):
        self.assertIn("Prepare", self.text)

    def test_phase_open_present(self):
        self.assertIn("Open", self.text)

    def test_phase_core_questions_present(self):
        self.assertIn("Core Questions", self.text)

    def test_phase_probe_deeper_present(self):
        self.assertIn("Probe Deeper", self.text)

    def test_phase_close_present(self):
        self.assertIn("Close", self.text)

    def test_phase_synthesize_present(self):
        self.assertIn("Synthesize", self.text)

    # Core principles
    def test_principle_two_person_team_present(self):
        self.assertIn("Two-person team", self.text)

    def test_principle_80_20_rule_present(self):
        self.assertIn("80/20", self.text)

    def test_principle_past_over_future_present(self):
        self.assertIn("Past over future", self.text)

    def test_principle_behavior_over_opinion_present(self):
        self.assertIn("Behavior over opinion", self.text)

    # §2F required fields
    def test_memorable_quote_field_present(self):
        self.assertIn("Memorable Quote", self.text)

    def test_cumulative_evidence_rating_present(self):
        self.assertIn("Cumulative Evidence Rating", self.text)

    def test_follow_up_actions_present(self):
        self.assertIn("Follow-Up Actions", self.text)

    # §2H required fields
    def test_hypothesis_scorecard_present(self):
        self.assertIn("Hypothesis Scorecard", self.text)

    # Evidence Calibration Rubric — 4 levels
    def test_evidence_level_validated_present(self):
        self.assertIn("Validated", self.text)

    def test_evidence_level_partially_validated_present(self):
        self.assertIn("Partially Validated", self.text)

    def test_evidence_level_inconclusive_present(self):
        self.assertIn("Inconclusive", self.text)

    def test_evidence_level_falsified_present(self):
        self.assertIn("Falsified", self.text)

    # Common mistakes — 7 named
    def test_common_mistake_pitching_present(self):
        self.assertIn("Pitching during the interview", self.text)

    def test_common_mistake_leading_questions_present(self):
        self.assertIn("Leading questions", self.text)

    def test_common_mistake_vague_generalizations_present(self):
        self.assertIn("Accepting vague generalizations", self.text)

    def test_common_mistake_wrong_people_present(self):
        self.assertIn("Interviewing the wrong people", self.text)

    def test_common_mistake_recording_without_synthesizing_present(self):
        self.assertIn("Recording without synthesizing", self.text)

    def test_common_mistake_over_interviewing_present(self):
        self.assertIn("Over-interviewing", self.text)

    def test_common_mistake_one_anecdote_present(self):
        self.assertIn("Treating one anecdote as validation", self.text)

    # CRM 90-day rule
    def test_crm_90_day_rule_present(self):
        self.assertIn("90 days", self.text)

    # Downstream handoffs
    def test_handoff_elevator_pitch_present(self):
        self.assertIn("Elevator Pitch", self.text)

    def test_handoff_battle_cards_present(self):
        self.assertIn("Battle Cards", self.text)

    def test_handoff_bar_test_present(self):
        self.assertIn("Bar Test", self.text)

    def test_handoff_impact_protocol_present(self):
        self.assertIn("Impact Protocol", self.text)


if __name__ == "__main__":
    unittest.main()
