import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


builder = load_module(
    "build_conversation_synthesis_input",
    "scripts/build_conversation_synthesis_input.py",
)


class BuildConversationSynthesisInputUnitTests(unittest.TestCase):
    def setUp(self):
        self.record_path = REPO_ROOT / "examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md"

    def test_parse_metadata_extracts_expected_fields(self):
        lines = self.record_path.read_text().splitlines()
        metadata = builder.parse_metadata(lines)
        self.assertEqual(metadata["source_id"], "01KM6GSRBZNXNSKQW5BQNDG2M9")
        self.assertEqual(metadata["account_or_company"], "Ejam")
        self.assertIn("managed service scope", metadata["conversation_context"])

    def test_extract_parsed_conversation_record_excludes_review_notes(self):
        text = self.record_path.read_text()
        extracted = builder.extract_parsed_conversation_record(text)
        self.assertIn("### `record_id`", extracted)
        self.assertNotIn("## Review notes", extracted)
        self.assertNotIn("## Output quality verdict", extracted)

    def test_parse_field_value_handles_bullets_and_scalar_values(self):
        bullets = builder.parse_field_value("- one\n- two\n")
        scalar = builder.parse_field_value("`high`\n")
        self.assertEqual(bullets, ["one", "two"])
        self.assertEqual(scalar, "high")

    def test_parse_record_loads_expected_fields(self):
        record = builder.parse_record(self.record_path)
        self.assertEqual(record["record_id"], "convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9")
        self.assertEqual(record["metadata"]["account_or_company"], "Ejam")
        self.assertIn("Predictable and explainable pricing", record["evaluation_criteria"])
        self.assertTrue(any("Sam Sutcu" in quote for quote in record["notable_quotes"]))

    def test_render_markdown_pack_includes_record_ids_and_workflow(self):
        record = builder.parse_record(self.record_path)
        text = builder.render_markdown_pack(
            [record],
            "test objective",
            "test segment",
            "test persona",
            "test window",
        )
        self.assertIn("convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9", text)
        self.assertIn("## Suggested synthesis workflow", text)
        self.assertIn("Reuse the attributed, cited quote bank", text)

    def test_main_writes_json_output(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "pack.json"
            exit_code = builder.main(
                [
                    str(self.record_path),
                    "--format",
                    "json",
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.exists())
            text = output_path.read_text()
            self.assertIn('"record_count": 1', text)
            self.assertIn('"record_id": "convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9"', text)


if __name__ == "__main__":
    unittest.main()
