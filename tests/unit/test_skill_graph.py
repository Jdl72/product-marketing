"""Structural tests for the skill dependency graph.

Every `SKILL.md` declares its dependencies in prose: an `## Inputs` section
naming what must exist first, and a `## Handoff` section naming what consumes
its output. Together those sections form a dependency graph. Nothing checked
that graph, so four kinds of drift accumulated undetected:

  * `CLAUDE.md` naming skills that do not exist in `skills/`
  * a skill listing an input produced by a later workbook tab
  * a skill referenced by other skills but absent from `lpa-workflow-map`
  * artifact names that no skill and no declared external source produces

These tests parse the graph and fail on all four.

Parsing convention: inside an `## Inputs` or `## Handoff` bullet, the FIRST
backticked token is the artifact name. Everything after it is annotation --
`- \\`Certification Rubric\\` (status must be \\`Certified\\`)` depends on
`Certification Rubric`, not on `Certified`.
"""

import re
import unittest

from tests.test_helpers import REPO_ROOT


SKILLS_DIR = REPO_ROOT / "skills"
WORKFLOW_MAP = SKILLS_DIR / "lpa-workflow-map/SKILL.md"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"


# Artifacts that legitimately have no producing skill in `skills/`.
# Adding to this list is how you declare a new external dependency -- it should
# be a deliberate act, not a way to silence a typo.
EXTERNAL_ARTIFACTS = {
    # Produced by the discovery workflow in `jobs/`, not by a workbook skill.
    "Conversation Synthesis",
    "Positioning Brief",
    # Shared ledger with a schema (`schemas/content-calendar.md`) but no skill;
    # Release Article and Monthly Innovation Roundup both write to it.
    "Content Calendar",
    # Sub-artifacts produced inside `lpa-customer-interview` (sections 2F/2H),
    # referenced by name because Weekly Discovery Log consumes those specific
    # sections rather than the whole interview.
    "Interview Snapshot",
    "Cross-Interview Pattern Synthesis",
    # A stage name inside Stage Gate Architecture, not a standalone artifact.
    "Narrative Lock",
    # Explicitly marked "if later added" in the skills that name them.
    "Narrative Skeletons",
    "Quarterly Innovation Moment",
}

# Backward edges: a skill listing an input produced by a later-numbered tab.
# Each entry is (consumer tab, consumer artifact, upstream tab, input artifact).
#
# These are unresolved contradictions between the declared dependency and the
# workflow map's own ordering, not approved exceptions. The test fails if a NEW
# one appears AND if one of these is fixed without being delisted, so the list
# cannot quietly grow or quietly rot.
KNOWN_BACKWARD_EDGES = {
    # Bar Test says it needs Segment Playbooks, and Segment Playbooks agrees
    # (its Handoff feeds Bar Test) -- but the map runs Bar Test first.
    ("4.1", "Bar Test", "4.2", "Segment Playbooks"),
    # ROI Calculator and Impact Protocol each list the other as an input.
    ("4.4", "ROI Calculator", "5.2", "Impact Protocol"),
}


def normalize(artifact):
    """Map a human-readable artifact name to its skill directory suffix.

    "Risk & Assumption Register" -> "risk-and-assumption-register"
    """
    name = artifact.lower().replace("&", "and")
    name = re.sub(r"[^a-z0-9\s-]", "", name)
    return re.sub(r"[\s-]+", "-", name).strip("-")


def section_bullets(content, heading):
    """Return the first backticked token of each bullet under `## <heading>`."""
    pattern = rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    artifacts = []
    for line in match.group(1).splitlines():
        if not line.lstrip().startswith("- "):
            continue
        token = re.search(r"`([^`]+)`", line)
        if token:
            artifacts.append(token.group(1).strip())
    return artifacts


def load_skills():
    skills = {}
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        content = skill_md.read_text()
        skills[skill_md.parent.name] = {
            "content": content,
            "inputs": section_bullets(content, "Inputs"),
            "handoff": section_bullets(content, "Handoff"),
        }
    return skills


def load_tabs():
    """Parse `lpa-workflow-map` into {artifact: tab number} plus cross-cutting."""
    content = WORKFLOW_MAP.read_text()
    numbered = {}
    for tab, name in re.findall(r"- `(\d+\.\d+)\s+([^`]+)`", content):
        numbered[name.strip()] = tab

    cross_cutting = set()
    match = re.search(
        r"^## Cross-cutting artifacts\s*$(.*?)(?=^## |\Z)",
        content,
        re.MULTILINE | re.DOTALL,
    )
    if match:
        for line in match.group(1).splitlines():
            if line.lstrip().startswith("- "):
                token = re.search(r"`([^`]+)`", line)
                if token:
                    cross_cutting.add(token.group(1).strip())
    return numbered, cross_cutting


SKILLS = load_skills()
NUMBERED_TABS, CROSS_CUTTING = load_tabs()

# artifact name -> skill directory, for every artifact a skill produces
ARTIFACT_TO_SKILL = {}
for artifact in list(NUMBERED_TABS) + list(CROSS_CUTTING):
    directory = f"lpa-{normalize(artifact)}"
    if directory in SKILLS:
        ARTIFACT_TO_SKILL[artifact] = directory


def tab_sort_key(tab):
    phase, sequence = tab.split(".")
    return (int(phase), int(sequence))


class SkillDirectoryTests(unittest.TestCase):
    def test_every_skill_directory_has_a_skill_file(self):
        for directory in sorted(p.name for p in SKILLS_DIR.iterdir() if p.is_dir()):
            self.assertIn(
                directory,
                SKILLS,
                f"skills/{directory}/ has no SKILL.md",
            )

    def test_every_skill_has_frontmatter_name_matching_its_directory(self):
        for directory, skill in SKILLS.items():
            match = re.search(r"^name:\s*(\S+)\s*$", skill["content"], re.MULTILINE)
            self.assertIsNotNone(match, f"{directory}/SKILL.md has no `name:` frontmatter")
            self.assertEqual(
                match.group(1),
                directory,
                f"{directory}/SKILL.md declares name `{match.group(1)}`",
            )


class WorkflowMapCoverageTests(unittest.TestCase):
    def test_every_mapped_artifact_resolves_to_a_real_skill(self):
        for artifact in list(NUMBERED_TABS) + list(CROSS_CUTTING):
            directory = f"lpa-{normalize(artifact)}"
            self.assertIn(
                directory,
                SKILLS,
                f"workflow map lists `{artifact}` but skills/{directory}/ does not exist",
            )

    def test_every_skill_appears_in_the_workflow_map(self):
        # lpa-workflow-map is the map itself, so it is not a member of the map.
        mapped = set(ARTIFACT_TO_SKILL.values()) | {"lpa-workflow-map"}
        for directory in sorted(SKILLS):
            self.assertIn(
                directory,
                mapped,
                f"{directory} exists but is missing from lpa-workflow-map "
                "(add it to a phase, or to Cross-cutting artifacts)",
            )

    def test_tab_numbers_are_unique(self):
        seen = {}
        for artifact, tab in NUMBERED_TABS.items():
            self.assertNotIn(tab, seen, f"tab {tab} used by both {seen.get(tab)} and {artifact}")
            seen[tab] = artifact


class ArtifactClosureTests(unittest.TestCase):
    """Every artifact named anywhere is produced by a skill or declared external."""

    def _assert_known(self, artifact, directory, section):
        known = artifact in ARTIFACT_TO_SKILL or artifact in EXTERNAL_ARTIFACTS
        self.assertTrue(
            known,
            f"{directory} lists `{artifact}` under ## {section}, but no skill "
            "produces it and it is not in EXTERNAL_ARTIFACTS",
        )

    def test_every_input_artifact_is_produced_or_external(self):
        for directory, skill in SKILLS.items():
            for artifact in skill["inputs"]:
                self._assert_known(artifact, directory, "Inputs")

    def test_every_handoff_target_is_a_real_artifact(self):
        for directory, skill in SKILLS.items():
            for artifact in skill["handoff"]:
                self._assert_known(artifact, directory, "Handoff")

    def test_no_skill_lists_itself_as_its_own_input(self):
        for directory, skill in SKILLS.items():
            for artifact in skill["inputs"]:
                self.assertNotEqual(
                    ARTIFACT_TO_SKILL.get(artifact),
                    directory,
                    f"{directory} lists its own output `{artifact}` as an input",
                )


class PhaseOrderTests(unittest.TestCase):
    """A skill may not depend on a tab that the workflow map runs later."""

    def _backward_edges(self):
        edges = set()
        for artifact, tab in NUMBERED_TABS.items():
            directory = ARTIFACT_TO_SKILL.get(artifact)
            if not directory:
                continue
            for dependency in SKILLS[directory]["inputs"]:
                upstream = NUMBERED_TABS.get(dependency)
                if not upstream:
                    continue  # cross-cutting or external: no ordering constraint
                if tab_sort_key(upstream) > tab_sort_key(tab):
                    edges.add((tab, artifact, upstream, dependency))
        return edges

    def test_no_new_backward_edges(self):
        for edge in sorted(self._backward_edges() - KNOWN_BACKWARD_EDGES):
            tab, artifact, upstream, dependency = edge
            self.fail(
                f"{artifact} (tab {tab}) lists `{dependency}` (tab {upstream}) as an "
                "input, but the workflow map runs it later. Fix the dependency, "
                "renumber the tabs, or add it to KNOWN_BACKWARD_EDGES with a reason."
            )

    def test_known_backward_edges_are_still_present(self):
        for edge in sorted(KNOWN_BACKWARD_EDGES - self._backward_edges()):
            self.fail(
                f"{edge} is listed in KNOWN_BACKWARD_EDGES but no longer exists. "
                "Remove it from the list."
            )


class ClaudeMdIndexTests(unittest.TestCase):
    """The index Claude reads first must name real skills, and all of them."""

    def setUp(self):
        self.content = CLAUDE_MD.read_text()
        self.referenced = set(re.findall(r"`(lpa-[a-z0-9-]+)`", self.content))

    def test_every_referenced_skill_exists(self):
        for name in sorted(self.referenced):
            self.assertIn(
                name,
                SKILLS,
                f"CLAUDE.md references `{name}`, which does not exist in skills/",
            )

    def test_every_skill_is_referenced(self):
        for directory in sorted(SKILLS):
            self.assertIn(
                directory,
                self.referenced,
                f"{directory} exists but CLAUDE.md never mentions it",
            )

    def test_referenced_job_specs_exist(self):
        for path in sorted(set(re.findall(r"`(jobs/[a-z0-9-]+\.md)`", self.content))):
            self.assertTrue(
                (REPO_ROOT / path).is_file(),
                f"CLAUDE.md references `{path}`, which does not exist",
            )


if __name__ == "__main__":
    unittest.main()
