import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


evaluator = load_module(
    "evaluate_client_workspace",
    "scripts/evaluate_client_workspace.py",
)


GENERIC_WORKSPACE = REPO_ROOT / "examples" / "client-workspace" / "generic-example"
XNURTA_WORKSPACE = REPO_ROOT / "clients" / "xnurta"


class EvaluateClientWorkspaceUnitTests(unittest.TestCase):
    def test_detect_workspace_kind_for_template(self):
        self.assertEqual(evaluator.detect_workspace_kind(GENERIC_WORKSPACE), "template")

    def test_detect_workspace_kind_for_client(self):
        self.assertEqual(evaluator.detect_workspace_kind(XNURTA_WORKSPACE), "client")

    def test_detect_workspace_kind_uses_explicit_marker_before_path_shape(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "clients" / "acme-examples" / "client-workspace-v2"
            root.mkdir(parents=True)
            (root / ".workspace-kind").write_text("client\n", encoding="utf-8")
            self.assertEqual(evaluator.detect_workspace_kind(root), "client")

    def test_collect_workspace_facts_for_generic_example(self):
        facts = evaluator.collect_workspace_facts(GENERIC_WORKSPACE)
        self.assertEqual(facts["missing_dirs"], [])
        self.assertEqual(facts["missing_config_files"], [])
        self.assertEqual(facts["missing_decision_files"], [])
        self.assertTrue(facts["has_evidence_readme"])
        self.assertFalse(facts["has_source_inventory"])

    def test_collect_workspace_facts_for_xnurta_finds_source_inventory(self):
        facts = evaluator.collect_workspace_facts(XNURTA_WORKSPACE)
        self.assertTrue(facts["has_source_inventory"])

    def test_substantive_files_ignore_non_markdown_noise(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            directory = Path(tmpdir)
            (directory / "brief.md").write_text("# Brief\n", encoding="utf-8")
            (directory / ".DS_Store").write_text("noise\n", encoding="utf-8")
            (directory / ".gitkeep").write_text("", encoding="utf-8")
            (directory / "brief.json").write_text("{}", encoding="utf-8")
            self.assertEqual(evaluator._list_substantive_files(directory), ["brief.md"])

    def test_client_workspace_with_source_inventory_passes_evidence_readiness_without_readme(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "client-a"
            for dirname in evaluator.REQUIRED_DIRS:
                (root / dirname).mkdir(parents=True, exist_ok=True)
            (root / ".workspace-kind").write_text("client\n", encoding="utf-8")
            for name in evaluator.REQUIRED_CONFIG_FILES:
                (root / "config" / name).write_text("content\n", encoding="utf-8")
            for name in evaluator.REQUIRED_DECISION_FILES:
                (root / "decisions" / name).write_text("content\n", encoding="utf-8")
            (root / "evidence" / "source-inventory.md").write_text("inventory\n", encoding="utf-8")

            evaluation = evaluator.evaluate_workspace(evaluator.collect_workspace_facts(root))

        evidence_dimension = next(
            dimension
            for dimension in evaluation["dimensions"]
            if dimension["dimension_id"] == "evidence_readiness"
        )
        self.assertEqual(evidence_dimension["status"], "PASS")

    def test_evaluate_workspace_flags_missing_contract_elements(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "broken-workspace"
            (root / "config").mkdir(parents=True)
            (root / ".workspace-kind").write_text("client\n", encoding="utf-8")
            facts = evaluator.collect_workspace_facts(root)
            evaluation = evaluator.evaluate_workspace(facts)

        self.assertEqual(evaluation["overall_result"], "FAIL")
        contract = next(
            dimension
            for dimension in evaluation["dimensions"]
            if dimension["dimension_id"] == "contract_completeness"
        )
        self.assertEqual(contract["status"], "FAIL")

    def test_render_markdown_includes_overall_result_and_dimensions(self):
        facts = evaluator.collect_workspace_facts(GENERIC_WORKSPACE)
        evaluation = evaluator.evaluate_workspace(facts)
        text = evaluator.render_markdown(evaluation)

        self.assertIn("# Client Workspace Evaluation", text)
        self.assertIn("`overall_result`", text)
        self.assertIn("`contract_completeness`", text)
        self.assertIn("`workspace_maturity`", text)

    def test_collect_workspace_facts_requires_explicit_workspace_kind_signal(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "workspace"
            root.mkdir(parents=True)
            with self.assertRaises(ValueError):
                evaluator.collect_workspace_facts(root)


if __name__ == "__main__":
    unittest.main()
