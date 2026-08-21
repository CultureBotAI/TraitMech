"""Keep the root README's artifact catalog complete as the repo grows."""

from __future__ import annotations

import re
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"


def readme_targets() -> set[str]:
    text = README.read_text(encoding="utf-8")
    return {
        target.split("#", 1)[0]
        for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", text)
    }


def test_readme_links_every_artifact_collection() -> None:
    expected = {
        ".claude/commands/",
        ".claude/skills/",
        "app/",
        "conf/",
        "dashboard/",
        "data/embeddings/",
        "data/raw/",
        "data/traits/",
        "docs/",
        "history/README.md",
        "mappings/",
        "pages/",
        "prompts/",
        "proposals/README.md",
        "reports/",
        "research/traits/",
        "src/traitmech/schema/",
        "templates/trait_causal_graph_research.md",
    }

    missing = expected - readme_targets()
    assert not missing, f"README artifact collections missing links: {sorted(missing)}"


def test_readme_links_every_committed_report() -> None:
    result = subprocess.run(
        ["git", "ls-files", "reports"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    reports = {
        path
        for path in result.stdout.splitlines()
        if path != "reports/.gitkeep" and not path.startswith("reports/robot/")
    }

    missing = reports - readme_targets()
    assert not missing, f"README report catalog missing links: {sorted(missing)}"


def test_readme_corpus_table_matches_the_trait_artifacts() -> None:
    actual: Counter[tuple[str, str]] = Counter()
    for path in (ROOT / "data" / "traits").glob("*/*.yaml"):
        text = path.read_text(encoding="utf-8")
        status_match = re.search(r"^mapping_status: (\w+)$", text, re.MULTILINE)
        assert status_match, f"{path.relative_to(ROOT)} has no mapping_status"

        category = path.parent.name.upper()
        actual[(category, status_match.group(1))] += 1
        actual[(category, "causal_graphs")] += int("\ncausal_graphs:" in text)
        actual[(category, "total")] += 1

    rows = re.findall(
        r"^\| ([A-Z_]+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$",
        README.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    documented = {
        (category, key): value
        for category, reviewed, deprecated, graphs, total in rows
        for key, value in (
            ("REVIEWED", int(reviewed)),
            ("DEPRECATED", int(deprecated)),
            ("causal_graphs", int(graphs)),
            ("total", int(total)),
        )
    }

    assert {category for category, _ in documented} == {
        category for category, _ in actual
    }
    for key, value in documented.items():
        assert value == actual[key], f"README has {key}={value}, corpus has {actual[key]}"

    total_match = re.search(
        r"^\| \*\*TOTAL\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* "
        r"\| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \|$",
        README.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    assert total_match, "README corpus table has no TOTAL row"
    assert tuple(map(int, total_match.groups())) == (
        sum(value for (category, key), value in actual.items() if key == "REVIEWED"),
        sum(value for (category, key), value in actual.items() if key == "DEPRECATED"),
        sum(value for (category, key), value in actual.items() if key == "causal_graphs"),
        sum(value for (category, key), value in actual.items() if key == "total"),
    )
