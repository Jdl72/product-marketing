import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class SourcePackWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.job_spec = REPO_ROOT / "jobs/gather-customer-conversations.md"
        self.job_text = self.job_spec.read_text()

        self.schema = REPO_ROOT / "schemas/conversation-source-pack.md"
        self.schema_text = self.schema.read_text()

        self.example = REPO_ROOT / "examples/conversations/source-pack-example.md"

    # --- File existence ---

    def test_source_pack_example_exists(self):
        self.assertTrue(
            self.example.exists(),
            "examples/conversations/source-pack-example.md must exist",
        )

    # --- Schema fields ---

    def test_schema_has_readiness_status_field(self):
        self.assertIn(
            "review_status",
            self.schema_text,
            "conversation-source-pack schema must include review_status pack-level field",
        )

    def test_schema_has_completeness_field(self):
        self.assertIn(
            "completeness",
            self.schema_text,
            "schema must include completeness field (full/partial/fragment)",
        )

    def test_schema_has_language_quality_field(self):
        self.assertIn(
            "language_quality",
            self.schema_text,
            "schema must include language_quality field",
        )

    # --- Job spec: duplicate flagging ---

    def test_job_spec_mentions_duplicate_flagging(self):
        text_lower = self.job_text.lower()
        self.assertIn(
            "duplicate",
            text_lower,
            "gather-customer-conversations.md must explicitly describe how to flag duplicate sources",
        )

    def test_job_spec_has_explicit_duplicate_exclusion_rule(self):
        self.assertIn(
            "exclude",
            self.job_text.lower(),
            "job spec must instruct the user to exclude confirmed duplicate sources",
        )

    # --- Job spec: partial and low-quality source flagging ---

    def test_job_spec_mentions_partial_source_flag(self):
        text_lower = self.job_text.lower()
        self.assertIn(
            "partial",
            text_lower,
            "job spec must explicitly describe how to flag partial sources",
        )

    def test_job_spec_mentions_low_quality_flag(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "low-quality" in text_lower or "low quality" in text_lower,
            "job spec must explicitly describe how to flag low-quality sources",
        )

    # --- Job spec: review gate criteria ---

    def test_job_spec_has_explicit_review_gate(self):
        self.assertIn(
            "Human review gate",
            self.job_text,
            "job spec must have a Human review gate section",
        )

    def test_job_spec_review_gate_covers_source_quality(self):
        self.assertIn(
            "quality",
            self.job_text.lower(),
            "review gate must cover source quality",
        )

    def test_job_spec_review_gate_covers_segment_fit(self):
        self.assertIn(
            "segment",
            self.job_text.lower(),
            "review gate must cover segment fit",
        )

    def test_job_spec_review_gate_covers_coverage_adequacy(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "coverage" in text_lower or "adequacy" in text_lower or "enough sources" in text_lower,
            "review gate must address coverage adequacy",
        )

    def test_job_spec_has_readiness_status_section(self):
        self.assertIn(
            "Readiness status",
            self.job_text,
            "job spec must define readiness status values for each source",
        )

    def test_job_spec_defines_ready_for_parsing_status(self):
        self.assertIn(
            "ready for parsing",
            self.job_text,
            "job spec must define 'ready for parsing' as a source status",
        )

    def test_job_spec_defines_needs_review_status(self):
        self.assertIn(
            "needs review",
            self.job_text,
            "job spec must define 'needs review' as a source status",
        )

    def test_job_spec_eval_mentions_readiness_status(self):
        self.assertIn(
            "readiness_status",
            self.job_text,
            "evals section must reference readiness_status",
        )

    # --- Example: content checks ---

    def test_example_has_review_status_ready_for_parsing(self):
        example_text = self.example.read_text()
        self.assertIn(
            "ready for parsing",
            example_text,
            "source-pack-example.md must have a pack-level review_status of 'ready for parsing'",
        )

    def test_example_has_at_least_one_partial_source(self):
        example_text = self.example.read_text()
        self.assertIn(
            "partial",
            example_text.lower(),
            "source-pack-example.md must include at least one source marked as partial",
        )

    def test_example_has_at_least_one_low_quality_source(self):
        example_text = self.example.read_text()
        self.assertIn(
            "language_quality`: `low",
            example_text,
            "source-pack-example.md must include at least one source with language_quality: low",
        )

    def test_example_has_at_least_one_excluded_duplicate(self):
        example_text = self.example.read_text()
        self.assertIn(
            "exclude",
            example_text.lower(),
            "source-pack-example.md must include at least one source marked for exclusion (e.g., duplicate)",
        )

    def test_example_has_known_gaps_entry(self):
        example_text = self.example.read_text()
        self.assertIn(
            "known_gaps",
            example_text,
            "source-pack-example.md must have a known_gaps entry",
        )

    def test_example_has_at_least_one_source_ready_for_parsing(self):
        example_text = self.example.read_text()
        self.assertIn(
            "readiness_status`: `ready for parsing",
            example_text,
            "source-pack-example.md must include at least one source with readiness_status: ready for parsing",
        )

    def test_example_sources_can_feed_parsing_job(self):
        """
        Confirm the example includes source metadata fields needed by the parsing job:
        source_id, source_type, date, and segment.
        """
        example_text = self.example.read_text()
        for field in ["source_id", "source_type", "date", "segment"]:
            self.assertIn(
                field,
                example_text,
                f"source-pack-example.md must include '{field}' metadata on sources so they can feed the parsing job",
            )


if __name__ == "__main__":
    unittest.main()
