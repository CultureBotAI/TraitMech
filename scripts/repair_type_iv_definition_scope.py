#!/usr/bin/env python3
"""Broaden the Type IV restriction definition to DNA modifications."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "type_iv_modification_dependent_restriction_system.yaml"
)

OLD_DEFINITION = (
    "A phage defense system in which an organism possesses a Type IV "
    "modification-dependent restriction locus, including DefenseFinder "
    "RM_Type_IV loci, whose restriction-enzyme activity cleaves foreign "
    "DNA bearing modified bases rather than the unmodified targets of "
    "canonical Type I-III restriction-modification systems."
)
NEW_DEFINITION = (
    "A phage defense system in which an organism possesses a Type IV "
    "modification-dependent restriction locus, including DefenseFinder "
    "RM_Type_IV loci, whose restriction-enzyme activity cleaves foreign "
    "DNA carrying recognized base or backbone modifications rather than "
    "the unmodified targets of canonical Type I-III "
    "restriction-modification systems."
)


def load_record(path: Path) -> dict[str, Any]:
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(record, dict):
        raise AssertionError(f"{path} did not contain a TraitRecord mapping")
    return record


def update_record(record: dict[str, Any]) -> None:
    assert record["identifier"] == "traitmech:000496"
    assert record["label"] == "type IV modification-dependent restriction system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["definition"] == OLD_DEFINITION
    assert (
        record["causal_graphs"][0]["nodes"][1]["description"]
        == "Incoming bacteriophage or other foreign DNA bearing modified bases "
        "or phosphorothioated backbone positions."
    )

    record["definition"] = NEW_DEFINITION
    record_curation_event(
        record,
        curator="codex",
        action="REVISED_DEFINITION",
        changes=(
            "Broadened the Type IV modification-dependent restriction system "
            "definition from modified bases to recognized base or backbone "
            "DNA modifications after PR #1488 local review found the original "
            "definition excluded phosphorothioated backbone targets; fixes #1489."
        ),
        llm_assisted=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = load_record(TARGET)
    update_record(record)

    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"updated {TARGET.relative_to(REPO_ROOT)}")
    else:
        with tempfile.TemporaryDirectory() as tmp:
            write_validated_trait(record, Path(tmp) / TARGET.name)
        print(f"would update {TARGET.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
