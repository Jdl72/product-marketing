#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path


PATTERN_SECTIONS = {
    "top_recurring_pains": "support_line",
    "strongly_supported_patterns": "support_line",
    "emerging_patterns": "support_line",
    "contradictory_signals": "inline_record",
}

RECORD_ID_RE = re.compile(r"convrec-[A-Za-z0-9-]+")


def extract_sections(text):
    parts = re.split(r"^### `([^`]+)`\s*$", text, flags=re.M)
    sections = {}
    for index in range(1, len(parts), 2):
        sections[parts[index]] = parts[index + 1]
    return sections


def split_bullets(section_text):
    entries = []
    current = []
    for line in section_text.splitlines():
        if line.startswith("- "):
            if current:
                entries.append(current)
            current = [line]
        elif current:
            current.append(line)
    if current:
        entries.append(current)
    return entries


def validate_support_line(section_name, entry_lines, errors):
    bullet = entry_lines[0][2:].strip()
    support_lines = [line.strip() for line in entry_lines[1:] if line.strip()]
    support_text = " ".join(support_lines)
    if "Support:" not in support_text:
        errors.append(f"{section_name}: missing Support line for bullet '{bullet}'")
        return
    if not RECORD_ID_RE.search(support_text):
        errors.append(f"{section_name}: missing record id citation for bullet '{bullet}'")


def validate_inline_record(section_name, entry_lines, errors):
    bullet = entry_lines[0][2:].strip()
    combined = " ".join(line.strip() for line in entry_lines if line.strip())
    if not RECORD_ID_RE.search(combined):
        errors.append(f"{section_name}: missing record id citation for bullet '{bullet}'")


def main():
    parser = argparse.ArgumentParser(
        description="Validate that conversation synthesis pattern sections cite supporting record ids."
    )
    parser.add_argument("path", help="Path to conversation synthesis markdown file")
    args = parser.parse_args()

    text = Path(args.path).read_text()
    sections = extract_sections(text)
    errors = []

    for section_name, mode in PATTERN_SECTIONS.items():
        section_text = sections.get(section_name)
        if not section_text:
            errors.append(f"missing required section '{section_name}'")
            continue
        entries = split_bullets(section_text)
        if not entries:
            errors.append(f"{section_name}: no bullet entries found")
            continue
        for entry in entries:
            if mode == "support_line":
                validate_support_line(section_name, entry, errors)
            else:
                validate_inline_record(section_name, entry, errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        sys.exit(1)

    print("PASS: all required synthesis pattern sections include record-level citations")


if __name__ == "__main__":
    main()
