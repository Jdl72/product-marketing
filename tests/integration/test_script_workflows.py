import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


builder = load_module(
    "build_conversation_synthesis_input_integration",
    "scripts/build_conversation_synthesis_input.py",
)
fetcher = load_module(
    "fetch_fireflies_transcripts_integration",
    "scripts/fetch_fireflies_transcripts.py",
)
validator = load_module(
    "validate_conversation_synthesis_integration",
    "scripts/validate_conversation_synthesis.py",
)


class FakeClient:
    def list_transcripts(self, limit=10):
        return [{"id": "list-1", "title": f"Demo {limit}"}]

    def get_transcript(self, transcript_id):
        return {"id": transcript_id, "title": "Detailed Demo"}


class ScriptWorkflowIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.ejam = REPO_ROOT / "examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md"
        self.schleich = REPO_ROOT / "examples/conversations/parsed-fireflies-schleich-copenhagen-dsp.md"
        self.synthesis_example = REPO_ROOT / "examples/conversations/conversation-synthesis-example.md"

    def test_builder_creates_markdown_pack_from_real_examples(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "pack.md"
            exit_code = builder.main(
                [
                    str(self.ejam),
                    str(self.schleich),
                    "--objective",
                    "test synthesis",
                    "--segment",
                    "test segment",
                    "--persona-scope",
                    "test persona",
                    "--time-window",
                    "test window",
                    "--output",
                    str(output),
                ]
            )
            self.assertEqual(exit_code, 0)
            text = output.read_text()
            self.assertIn("convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9", text)
            self.assertIn("convrec-fireflies-01KMDFR8SB2ZEPT3452AFH85F9", text)
            self.assertIn("## Suggested synthesis workflow", text)

    def test_fetch_script_writes_json_with_fake_client(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "transcript.json"
            exit_code = fetcher.main(
                ["--transcript-id", "tx-123", "--output", str(output)],
                client_factory=FakeClient,
            )
            self.assertEqual(exit_code, 0)
            payload = json.loads(output.read_text())
            self.assertEqual(payload["id"], "tx-123")

    def test_fetch_script_prints_list_output_with_fake_client(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = fetcher.main(["--limit", "5"], client_factory=FakeClient)
        self.assertEqual(exit_code, 0)
        self.assertIn('"id": "list-1"', buffer.getvalue())

    def test_validator_main_passes_for_real_synthesis_example(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = validator.main([str(self.synthesis_example)])
        self.assertEqual(exit_code, 0)
        self.assertIn("PASS:", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
