import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class ClientWorkspaceEvaluationEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.script = REPO_ROOT / "scripts" / "evaluate_client_workspace.py"
        self.generic_workspace = REPO_ROOT / "examples" / "client-workspace" / "generic-example"

    def test_workspace_eval_script_runs_via_subprocess(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "workspace-eval.md"
            result = subprocess.run(
                ["python3", str(self.script), str(self.generic_workspace), "--output", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            text = output.read_text(encoding="utf-8")
            self.assertIn("# Client Workspace Evaluation", text)
            self.assertIn("`workspace_name`: `generic-example`", text)
            self.assertIn("`overall_result`: `PASS`", text)


if __name__ == "__main__":
    unittest.main()
