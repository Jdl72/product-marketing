#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


FIELD_ORDER = [
    "record_id",
    "primary_pains",
    "secondary_pains",
    "desired_outcomes",
    "current_alternatives",
    "objections",
    "contract_or_legal_objections",
    "buying_triggers",
    "evaluation_criteria",
    "trust_requirements",
    "competitors_mentioned",
    "language_to_use",
    "language_to_avoid",
    "notable_quotes",
    "term_normalization_notes",
    "summary_of_signal",
    "evidence_strength",
    "confidence",
    "missing_context",
    "open_questions",
]


def parse_metadata(lines):
    metadata = {}
    in_metadata = False
    for line in lines:
        stripped = line.strip()
        if stripped == "## Raw source metadata":
            in_metadata = True
            continue
        if in_metadata and stripped.startswith("## "):
            break
        if in_metadata and stripped.startswith("- `") and "`: " in stripped:
            key_part, value = stripped[2:].split("`: ", 1)
            key = key_part.strip("`")
            metadata[key] = value.strip().strip("`")
    return metadata


def extract_parsed_conversation_record(text):
    start_marker = "## Parsed conversation record"
    end_marker = "## Review notes"
    start = text.find(start_marker)
    if start == -1:
        return text
    start += len(start_marker)
    end = text.find(end_marker, start)
    if end == -1:
        end = len(text)
    return text[start:end]


def parse_sections(text):
    text = extract_parsed_conversation_record(text)
    parts = re.split(r"^### `([^`]+)`\s*$", text, flags=re.M)
    sections = {}
    for index in range(1, len(parts), 2):
        key = parts[index]
        body = parts[index + 1].strip()
        sections[key] = body
    return sections


def parse_field_value(body):
    lines = [line.rstrip() for line in body.splitlines() if line.strip()]
    if not lines:
        return []
    bullet_lines = [line for line in lines if line.lstrip().startswith("- ")]
    if bullet_lines and len(bullet_lines) == len(lines):
        return [line.lstrip()[2:].strip() for line in bullet_lines]
    if len(lines) == 1:
        return lines[0].strip("`")
    return "\n".join(lines)


def parse_record(path):
    text = Path(path).read_text()
    lines = text.splitlines()
    metadata = parse_metadata(lines)
    sections = parse_sections(text)
    record = {
        "source_file": str(Path(path)),
        "title": lines[0].lstrip("# ").strip() if lines else Path(path).name,
        "metadata": metadata,
    }
    for field in FIELD_ORDER:
        if field in sections:
            record[field] = parse_field_value(sections[field])
    return record


def render_markdown_pack(records, objective, segment, persona_scope, time_window):
    lines = [
        "# Conversation Synthesis Input Pack",
        "",
        "## Scope",
        "",
        f"- `objective`: `{objective}`",
        f"- `segment`: `{segment}`",
        f"- `persona_scope`: `{persona_scope}`",
        f"- `time_window`: `{time_window}`",
        f"- `record_count`: `{len(records)}`",
        "",
        "## Included records",
        "",
    ]

    for record in records:
        record_id = record.get("record_id", "unknown-record-id")
        lines.append(f"- `{record_id}`")
        lines.append(f"  Source: [{Path(record['source_file']).name}]({record['source_file']})")

    for record in records:
        record_id = record.get("record_id", "unknown-record-id")
        meta = record.get("metadata", {})
        lines.extend(
            [
                "",
                f"## Record: `{record_id}`",
                "",
                f"- `account_or_company`: `{meta.get('account_or_company', 'unknown')}`",
                f"- `segment`: `{meta.get('segment', 'unknown')}`",
                f"- `persona_or_role`: `{meta.get('persona_or_role', 'unknown')}`",
                f"- `conversation_context`: `{meta.get('conversation_context', 'unknown')}`",
            ]
        )
        if meta.get("stakeholder_map"):
            lines.append(f"- `stakeholder_map`: `{meta['stakeholder_map']}`")

        for field in FIELD_ORDER:
            value = record.get(field)
            if not value:
                continue
            lines.extend(["", f"### `{field}`", ""])
            if isinstance(value, list):
                for item in value:
                    lines.append(f"- {item}")
            else:
                lines.append(str(value))

    lines.extend(
        [
            "",
            "## Suggested synthesis workflow",
            "",
            "1. Compare recurring pains, outcomes, objections, and trust requirements across records.",
            "2. Separate strongly supported patterns from emerging patterns.",
            "3. Preserve stakeholder differences and contradictions.",
            "4. Reuse the attributed, cited quote bank rather than inventing new wording.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_parser():
    parser = argparse.ArgumentParser(
        description="Assemble parsed conversation records into a synthesis-ready input pack."
    )
    parser.add_argument("records", nargs="+", help="Paths to parsed conversation markdown files")
    parser.add_argument("--objective", default="prepare grounded conversation synthesis")
    parser.add_argument("--segment", default="unspecified")
    parser.add_argument("--persona-scope", default="unspecified")
    parser.add_argument("--time-window", default="unspecified")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format",
    )
    parser.add_argument("--output", help="Optional output file path")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    records = [parse_record(path) for path in args.records]
    if args.format == "json":
        payload = {
            "objective": args.objective,
            "segment": args.segment,
            "persona_scope": args.persona_scope,
            "time_window": args.time_window,
            "record_count": len(records),
            "records": records,
        }
        text = json.dumps(payload, indent=2)
    else:
        text = render_markdown_pack(
            records,
            args.objective,
            args.segment,
            args.persona_scope,
            args.time_window,
        )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
