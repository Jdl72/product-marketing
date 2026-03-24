import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class DiscoveryPipelineEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.builder_script = REPO_ROOT / "scripts/build_conversation_synthesis_input.py"
        self.validator_script = REPO_ROOT / "scripts/validate_conversation_synthesis.py"
        self.ejam = REPO_ROOT / "examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md"
        self.schleich = REPO_ROOT / "examples/conversations/parsed-fireflies-schleich-copenhagen-dsp.md"
        self.synthesis_example = REPO_ROOT / "examples/conversations/conversation-synthesis-example.md"

    def test_records_to_pack_and_validation_flow(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generated = Path(tmpdir) / "generated-pack.md"
            build_result = subprocess.run(
                [
                    "python3",
                    str(self.builder_script),
                    str(self.ejam),
                    str(self.schleich),
                    "--objective",
                    "e2e synthesis",
                    "--segment",
                    "e2e segment",
                    "--persona-scope",
                    "e2e persona",
                    "--time-window",
                    "2026-03-20 to 2026-03-23",
                    "--output",
                    str(generated),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(build_result.returncode, 0, build_result.stderr)
            generated_text = generated.read_text()
            self.assertIn("convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9", generated_text)
            self.assertIn("Sam Sutcu [sentence 231, 14:15-14:24]", generated_text)

            validate_result = subprocess.run(
                ["python3", str(self.validator_script), str(self.synthesis_example)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(validate_result.returncode, 0, validate_result.stderr)
            self.assertIn("PASS:", validate_result.stdout)


if __name__ == "__main__":
    unittest.main()
