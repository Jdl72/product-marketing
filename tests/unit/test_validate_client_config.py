import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


validator = load_module(
    "validate_client_config_unit",
    "scripts/validate_client_config.py",
)


class ClientConfigValidationUnitTests(unittest.TestCase):
    def test_detect_workspace_kind_distinguishes_template_and_client(self):
        template_root = REPO_ROOT / "examples" / "client-workspace" / "generic-example"
        client_root = REPO_ROOT / "clients" / "xnurta"
        self.assertEqual(validator.detect_workspace_kind(template_root), "template")
        self.assertEqual(validator.detect_workspace_kind(client_root), "client")

    def test_placeholder_counter_ignores_real_ids_and_nested_content(self):
        text = "\n".join(
            [
                "- `Segment ID`:",
                "- `S1`:",
                "  - `Name`: Real segment",
                "- `Stage-mapping rules`:",
                "  - If pricing is present -> F3",
            ]
        )
        self.assertEqual(validator._count_placeholder_lines(text), 1)

    def test_template_workspace_passes_with_expected_placeholder_counts(self):
        report = validator.analyze_workspace(REPO_ROOT / "examples" / "client-workspace" / "generic-example")
        self.assertEqual(report["overall_result"], "PASS")
        by_name = {item["file"]: item for item in report["files"]}
        self.assertEqual(by_name["client-profile.md"]["placeholder_count"], 9)
        self.assertEqual(by_name["segment-taxonomy.md"]["placeholder_count"], 5)
        self.assertEqual(by_name["funnel-stages.md"]["placeholder_count"], 5)
        self.assertEqual(by_name["competitor-map.md"]["placeholder_count"], 5)
        self.assertEqual(by_name["coding-rules.md"]["placeholder_count"], 6)

    def test_populated_client_workspace_passes(self):
        report = validator.analyze_workspace(REPO_ROOT / "clients" / "xnurta")
        self.assertEqual(report["overall_result"], "PASS")
        self.assertTrue(all(item["status"] == "PASS" for item in report["files"]))

    def test_missing_required_sections_fail_file_validation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "segment-taxonomy.md"
            path.write_text("# Segment Taxonomy\n", encoding="utf-8")
            report = validator.analyze_config_file(path, workspace_kind="client")
        self.assertEqual(report["status"], "FAIL")
        self.assertIn("## Segments", report["reason"])

    def test_main_returns_nonzero_for_failing_workspace(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "broken-client"
            config_dir = workspace / "config"
            config_dir.mkdir(parents=True)
            (config_dir / "client-profile.md").write_text("# Client Profile\n", encoding="utf-8")
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                exit_code = validator.main([str(workspace)])
        self.assertEqual(exit_code, 1)
        self.assertIn("`overall_result`: `FAIL`", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
