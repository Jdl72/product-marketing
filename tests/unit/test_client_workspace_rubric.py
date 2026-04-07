import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
RUBRIC_PATH = REPO_ROOT / "evals" / "client-workspace-rubric.md"
SCHEMA_PATH = REPO_ROOT / "schemas" / "client-workspace-evaluation.md"


class ClientWorkspaceRubricTests(unittest.TestCase):
    def setUp(self):
        self.rubric_text = RUBRIC_PATH.read_text(encoding="utf-8")
        self.schema_text = SCHEMA_PATH.read_text(encoding="utf-8")

    def test_rubric_file_exists(self):
        self.assertTrue(RUBRIC_PATH.exists())

    def test_schema_file_exists(self):
        self.assertTrue(SCHEMA_PATH.exists())

    def test_rubric_has_pass_fail_rule(self):
        self.assertIn("## Pass / fail rule", self.rubric_text)

    def test_rubric_has_five_dimensions(self):
        dimensions = re.findall(r"^### \d+\.", self.rubric_text, re.MULTILINE)
        self.assertGreaterEqual(len(dimensions), 5)

    def test_schema_lists_required_dimensions(self):
        self.assertIn("contract_completeness", self.schema_text)
        self.assertIn("config_pack_readiness", self.schema_text)
        self.assertIn("evidence_readiness", self.schema_text)
        self.assertIn("decision_layer_readiness", self.schema_text)
        self.assertIn("workspace_maturity", self.schema_text)


if __name__ == "__main__":
    unittest.main()
