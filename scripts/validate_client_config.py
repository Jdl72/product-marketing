#!/usr/bin/env python3
import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

PLACEHOLDER_LABELS = {
    "Alternative",
    "Buying triggers used in coding",
    "Category",
    "Canonical Name",
    "Client Name",
    "Core GTM Motion",
    "Definition",
    "Description",
    "Excluded conversation types",
    "In-scope evidence types",
    "Included conversation types",
    "Known Constraints",
    "Known Competitors",
    "Name",
    "Notes",
    "Objection categories used in coding",
    "Outcome signals used in coding",
    "Primary Buyer Persona",
    "Primary Buyer Types",
    "Primary Product Lines",
    "Primary Strategic Questions This Quarter",
    "Primary User Persona",
    "Primary User Types",
    "Proof categories used in coding",
    "Segment ID",
    "Segment-mapping rules",
    "Source Systems Available",
    "Stage ID",
    "Stage-mapping rules",
    "Success signal",
    "Type",
    "Variants / aliases",
}

FILE_RULES = {
    "client-profile.md": {
        "title": "# Client Profile",
        "required_sections": [],
        "content_markers": ["`Client Name`:", "`Category`:", "`Source Systems Available`:"],
        "fallback": "Continue with generic workflow behavior and mark client framing as unresolved.",
    },
    "segment-taxonomy.md": {
        "title": "# Segment Taxonomy",
        "required_sections": ["## Segments"],
        "content_markers": ["`Name`:", "`Description`:"],
        "fallback": "Mark segment as `unresolved` and preserve generic schema behavior without inventing client labels.",
    },
    "funnel-stages.md": {
        "title": "# Funnel Stages",
        "required_sections": ["## Stage Definitions"],
        "content_markers": ["`Name`:", "`Definition`:"],
        "fallback": "Mark stage as `unresolved` and avoid guessing client stage labels.",
    },
    "competitor-map.md": {
        "title": "# Competitor Map",
        "required_sections": ["## Named Competitors", "## Status Quo Alternatives"],
        "content_markers": ["`Category`:", "`Type`:"],
        "fallback": "Preserve raw competitor mentions and skip canonical normalization.",
    },
    "coding-rules.md": {
        "title": "# Coding Rules",
        "required_sections": ["## Client Extensions", "## Rules"],
        "content_markers": ["`Stage-mapping rules`:", "`Segment-mapping rules`:"],
        "fallback": "Use generic schema fields only and keep unresolved mappings explicit.",
    },
    "strategic-questions.md": {
        "title": "# Strategic Questions",
        "required_sections": [],
        "content_markers": ["- "],
        "fallback": "Proceed only from the explicit PMM objective and do not invent executive questions.",
    },
    "metrics-scorecard.md": {
        "title": "# Metrics Scorecard",
        "required_sections": [],
        "content_markers": ["- `"],
        "fallback": "Use generic evidence and workflow review instead of fabricated client metrics.",
    },
}

REQUIRED_FILES = tuple(FILE_RULES.keys())


def detect_workspace_kind(root: Path) -> str:
    parts = root.resolve().parts
    if "examples" in parts and "client-workspace" in parts:
        return "template"
    return "client"


def _readable_path(path: Path) -> str:
    path = path.resolve()
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _count_placeholder_lines(text: str) -> int:
    lines = text.splitlines()
    count = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not (stripped.startswith("- `") and stripped.endswith(":")):
            continue
        label = stripped[3:-2]
        if label not in PLACEHOLDER_LABELS:
            continue
        current_indent = len(line) - len(line.lstrip())
        has_nested_content = False
        for later in lines[index + 1 :]:
            later_stripped = later.strip()
            if not later_stripped:
                continue
            later_indent = len(later) - len(later.lstrip())
            if later_indent <= current_indent:
                break
            if later_stripped.startswith("- "):
                has_nested_content = True
                break
        if not has_nested_content:
            count += 1
    return count


def _has_real_marker_content(text: str, markers: list[str]) -> bool:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        for marker in markers:
            if marker in stripped:
                after = stripped.split(marker, 1)[1].strip()
                if after:
                    return True
                current_indent = len(line) - len(line.lstrip())
                for later in lines[index + 1 :]:
                    later_stripped = later.strip()
                    if not later_stripped:
                        continue
                    later_indent = len(later) - len(later.lstrip())
                    if later_indent <= current_indent:
                        break
                    if later_stripped.startswith("- "):
                        return True
    return False


def analyze_config_file(path: Path, *, workspace_kind: str) -> dict:
    rule = FILE_RULES[path.name]
    text = path.read_text(encoding="utf-8")

    missing_sections = []
    if rule["title"] not in text:
        missing_sections.append(rule["title"])
    for section in rule["required_sections"]:
        if section not in text:
            missing_sections.append(section)

    placeholder_count = _count_placeholder_lines(text)
    has_real_content = _has_real_marker_content(text, rule["content_markers"])

    if missing_sections:
        status = "FAIL"
        reason = f"Missing required sections: {', '.join(missing_sections)}"
    elif workspace_kind == "template":
        status = "PASS"
        reason = "Template scaffold has the required sections and may keep placeholders."
    elif has_real_content and placeholder_count == 0:
        status = "PASS"
        reason = "Client config is populated enough for live use."
    elif has_real_content:
        status = "CONDITIONAL"
        reason = "Client config is partly populated but still retains template-style placeholders."
    else:
        status = "FAIL"
        reason = "Client config does not contain enough real content for live use."

    return {
        "file": path.name,
        "path": _readable_path(path),
        "status": status,
        "reason": reason,
        "placeholder_count": placeholder_count,
        "fallback": rule["fallback"],
    }


def analyze_workspace(root: Path) -> dict:
    root = root.resolve()
    config_dir = root / "config"
    workspace_kind = detect_workspace_kind(root)

    missing_files = [name for name in REQUIRED_FILES if not (config_dir / name).is_file()]
    file_reports = []
    for name in REQUIRED_FILES:
        path = config_dir / name
        if path.is_file():
            file_reports.append(analyze_config_file(path, workspace_kind=workspace_kind))

    statuses = [report["status"] for report in file_reports]
    if missing_files or "FAIL" in statuses:
        overall = "FAIL"
    elif "CONDITIONAL" in statuses:
        overall = "CONDITIONAL"
    else:
        overall = "PASS"

    if overall == "PASS" and workspace_kind == "template":
        summary = "The template config pack is structurally valid and ready to be copied into a real client workspace."
    elif overall == "PASS":
        summary = "The client config pack is structurally valid and populated enough for live workflow use."
    elif overall == "CONDITIONAL":
        summary = "The config pack is usable but still contains unresolved template-level gaps."
    else:
        summary = "The config pack is missing required structure or enough populated content for safe client-specific use."

    return {
        "workspace_name": root.name,
        "workspace_path": _readable_path(root),
        "workspace_kind": workspace_kind,
        "overall_result": overall,
        "missing_files": missing_files,
        "summary": summary,
        "files": file_reports,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Client Config Validation Report",
        "",
        "## Workspace",
        "",
        f"- `workspace_name`: `{report['workspace_name']}`",
        f"- `workspace_path`: `{report['workspace_path']}`",
        f"- `workspace_kind`: `{report['workspace_kind']}`",
        f"- `overall_result`: `{report['overall_result']}`",
        "",
        "## Summary",
        "",
        report["summary"],
        "",
        "## Missing files",
        "",
        f"- {report['missing_files'] or 'none'}",
        "",
        "## File reports",
        "",
    ]

    for item in report["files"]:
        lines.extend(
            [
                f"### `{item['file']}`",
                "",
                f"- `status`: `{item['status']}`",
                f"- `path`: `{item['path']}`",
                f"- `reason`: {item['reason']}",
                f"- `placeholder_count`: `{item['placeholder_count']}`",
                f"- `fallback_behavior`: {item['fallback']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Review notes",
            "",
            "- strongest config file:",
            "- weakest config file:",
            "- blocking config gap:",
            "- next recommended improvement:",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Validate client config files and surface allowed fallback behavior."
    )
    parser.add_argument("workspace", help="Path to the client workspace root")
    parser.add_argument("--output", help="Optional markdown output path")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    report = analyze_workspace(Path(args.workspace))
    text = render_markdown(report)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
    else:
        print(text)
    if report["overall_result"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
