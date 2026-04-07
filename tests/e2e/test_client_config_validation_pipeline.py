import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class ClientConfigValidationPipelineEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.script = REPO_ROOT / "scripts" / "validate_client_config.py"

    def test_validator_runs_via_subprocess_for_template_workspace(self):
        workspace = REPO_ROOT / "examples" / "client-workspace" / "generic-example"
        result = subprocess.run(
            ["python3", str(self.script), str(workspace)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("`workspace_kind`: `template`", result.stdout)
        self.assertIn("`overall_result`: `PASS`", result.stdout)

    def test_validator_runs_via_subprocess_for_reference_client_workspace(self):
        workspace = REPO_ROOT / "clients" / "xnurta"
        result = subprocess.run(
            ["python3", str(self.script), str(workspace)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("`workspace_kind`: `client`", result.stdout)
        self.assertIn("`overall_result`: `PASS`", result.stdout)

    def test_validator_returns_nonzero_for_broken_workspace(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "broken-client"
            (workspace / "config").mkdir(parents=True)
            result = subprocess.run(
                ["python3", str(self.script), str(workspace)],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("`overall_result`: `FAIL`", result.stdout)


if __name__ == "__main__":
    unittest.main()
