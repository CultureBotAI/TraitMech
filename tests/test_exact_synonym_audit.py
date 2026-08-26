from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_exact_synonyms.py"
SPEC = importlib.util.spec_from_file_location("audit_exact_synonyms_test", SCRIPT)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def test_label_match_accepts_only_canonical_or_declared_exact() -> None:
    term = audit.Term("GO:1", "canonical label", ("exact alias",), "definition")

    assert audit.label_match("Canonical  Label", term) == "CANONICAL_LABEL"
    assert audit.label_match("EXACT ALIAS", term) == "EXACT_SYNONYM"
    assert audit.label_match("related alias", term) == "NO_EXACT_LABEL_MATCH"


def test_streaming_obo_parser_keeps_scope_and_tolerates_escaped_xref(tmp_path: Path) -> None:
    source = tmp_path / "test.obo"
    source.write_text(
        r"""format-version: 1.2
data-version: releases/2026-01-02

[Term]
id: GO:0000001
name: canonical label
def: "A useful definition." [TEST:1]
synonym: "exact alias" EXACT []
synonym: "related alias" RELATED []
xref: https://example.org/a\,b
""",
        encoding="utf-8",
    )

    snapshot = audit.parse_obo("GO", source)

    assert snapshot.version == "releases/2026-01-02"
    assert snapshot.terms["GO:0000001"] == audit.Term(
        "GO:0000001", "canonical label", ("exact alias",), "A useful definition."
    )


def test_collision_report_ignores_related_synonyms() -> None:
    records = [
        (
            audit.ROOT / "data/traits/a.yaml",
            {
                "identifier": "TEST:1",
                "label": "shared",
                "synonyms": [
                    {"synonym_text": "not shared", "synonym_type": "RELATED_SYNONYM"}
                ],
            },
        ),
        (
            audit.ROOT / "data/traits/b.yaml",
            {
                "identifier": "TEST:2",
                "label": "other",
                "synonyms": [
                    {"synonym_text": "Shared", "synonym_type": "EXACT_SYNONYM"},
                    {"synonym_text": "not shared", "synonym_type": "RELATED_SYNONYM"},
                ],
            },
        ),
    ]

    rows = audit.collision_rows(records)

    assert [row["normalized_text"] for row in rows] == ["shared"]


def test_collisions_only_cli_needs_no_snapshots(tmp_path, monkeypatch) -> None:
    traits = tmp_path / "traits"
    traits.mkdir()
    (traits / "one.yaml").write_text(
        "identifier: traitmech:1\n"
        "label: shared\n"
        "synonyms: []\n"
    )
    (traits / "two.yaml").write_text(
        "identifier: traitmech:2\n"
        "label: distinct\n"
        "synonyms:\n"
        "- synonym_text: Shared\n"
        "  synonym_type: EXACT_SYNONYM\n"
    )
    output = tmp_path / "collisions.tsv"
    monkeypatch.setattr(audit, "ROOT", tmp_path)
    monkeypatch.setattr(audit, "TRAITS_DIR", traits)

    assert audit.main(["--collisions-only", "--collision-out", str(output)]) == 0

    rows = list(csv.DictReader(output.open(), delimiter="\t"))
    assert len(rows) == 1
    assert rows[0]["normalized_text"] == "shared"
    assert rows[0]["owner_count"] == "2"
