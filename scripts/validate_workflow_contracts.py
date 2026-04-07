#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = (
    "## Purpose",
    "## Output artifact",
    "## Required inputs",
    "## Optional inputs",
    "## Input readiness checks",
    "## Workflow notes",
    "## Human review gate",
    "## Failure and fallback behavior",
    "## Downstream consumers",
    "## Done when",
)

SCHEMA_LINK_RE = re.compile(r"\[([^\]]+\.md)\]\(([^)]+schemas/[^)]+\.md)\)")


def validate_contract(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{path.name}: missing section '{section}'")

    match = SCHEMA_LINK_RE.search(text)
    if not match:
        errors.append(f"{path.name}: missing schema link in output artifact section")
    else:
        label = match.group(1)
        if label.startswith("conversation-"):
            pass

    if "fail if" not in text.lower():
        errors.append(f"{path.name}: missing explicit fail-if guidance")

    return errors


def validate_directory(directory: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(directory.glob("*-workflow-contract.md")):
        errors.extend(validate_contract(path))
    return errors


def build_parser():
    parser = argparse.ArgumentParser(
        description="Validate schema-backed workflow contract markdown files."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="docs/contracts",
        help="Contract file or directory to validate (default: docs/contracts)",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    target = Path(args.path)

    if target.is_dir():
        errors = validate_directory(target)
    else:
        errors = validate_contract(target)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: workflow contracts include the required sections and schema links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
