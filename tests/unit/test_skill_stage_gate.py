import unittest
from tests.test_helpers import REPO_ROOT


SKILL_PATH = REPO_ROOT / "skills/lpa-stage-gate-architecture/SKILL.md"


class StageGateSkillTests(unittest.TestCase):
    def setUp(self):
        self.text = SKILL_PATH.read_text()

    def test_learning_readiness_gates_stage_2_not_stage_1(self):
        # Must say Stage 2 near "Learning Readiness", must NOT say "gates Stage 1"
        self.assertIn("Learning Readiness", self.text)
        self.assertIn("gates Stage 2", self.text)
        self.assertNotIn("gates Stage 1", self.text)

    def test_all_five_stage_names_are_present(self):
        self.assertIn("Narrative Hypothesis + Eval Design", self.text)
        self.assertIn("Low-Signal Deployment", self.text)
        self.assertIn("Narrative Lock", self.text)
        self.assertIn("Distribution Test", self.text)
        self.assertIn("Lightning Strike", self.text)

    def test_deployment_threshold_5_to_10_percent(self):
        self.assertTrue("5–10%" in self.text or "5-10%" in self.text)

    def test_deployment_threshold_30_to_50_percent(self):
        self.assertTrue("30–50%" in self.text or "30-50%" in self.text)

    def test_endless_discovery_loop_threshold_30_percent(self):
        self.assertIn("30%", self.text)

    def test_endless_discovery_loop_threshold_15_percent(self):
        self.assertIn("15%", self.text)

    def test_zero_proactive_commercial_communication_rule(self):
        self.assertIn("ZERO proactive commercial communication", self.text)

    def test_stakeholder_impatience_anti_pattern_named(self):
        self.assertIn("Stakeholder Impatience", self.text)

    def test_scope_creep_anti_pattern_named(self):
        self.assertIn("Scope Creep", self.text)

    def test_gate_1_criteria_present(self):
        self.assertIn("Gate 1", self.text)
        self.assertIn("Discovery Readiness", self.text)

    def test_gate_2_criteria_present(self):
        self.assertIn("Gate 2", self.text)
        self.assertIn("Hypothesis Validation", self.text)

    def test_xyz_hypothesis_format_described(self):
        self.assertIn("XYZ", self.text)
        self.assertIn("At least X% of Y will do Z", self.text)

    def test_narrative_containment_plan_in_stage_2(self):
        self.assertIn("Narrative Containment Plan", self.text)


if __name__ == "__main__":
    unittest.main()
