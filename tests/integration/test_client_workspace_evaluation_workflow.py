import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


evaluator = load_module(
    "evaluate_client_workspace_integration",
    "scripts/evaluate_client_workspace.py",
)


class ClientWorkspaceEvaluationIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.generic_workspace = REPO_ROOT / "examples" / "client-workspace" / "generic-example"
        self.xnurta_workspace = REPO_ROOT / "clients" / "xnurta"
        self.example_output = REPO_ROOT / "examples" / "client-workspace" / "client-workspace-evaluation-example.md"

    def test_main_writes_generic_example_evaluation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "generic-eval.md"
            exit_code = evaluator.main([str(self.generic_workspace), "--output", str(output)])
            self.assertEqual(exit_code, 0)
            text = output.read_text(encoding="utf-8")
            self.assertIn("`workspace_kind`: `template`", text)
            self.assertIn("`overall_result`: `PASS`", text)

    def test_main_writes_xnurta_evaluation_with_source_inventory_signal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "xnurta-eval.md"
            exit_code = evaluator.main([str(self.xnurta_workspace), "--output", str(output)])
            self.assertEqual(exit_code, 0)
            text = output.read_text(encoding="utf-8")
            self.assertIn("`workspace_kind`: `client`", text)
            self.assertIn("has_source_inventory=True", text)

    def test_checked_in_example_matches_current_generic_workspace(self):
        facts = evaluator.collect_workspace_facts(self.generic_workspace)
        evaluation = evaluator.evaluate_workspace(facts)
        rendered = evaluator.render_markdown(evaluation).strip()
        checked_in = self.example_output.read_text(encoding="utf-8").strip()
        self.assertEqual(rendered, checked_in)


if __name__ == "__main__":
    unittest.main()
