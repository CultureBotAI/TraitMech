#!/usr/bin/env python3
"""#301 migration, part 2 of 2: the families needing v9 terms.

Part 1 (#328) moved the 185 edges whose target was already decided or upstream,
taking MICROBE_DOMAIN_ON_NONORGANISM from 366 to 181. This moves 180 of the
remaining 181 onto the causal-graph counterparts proposed in
``proposals/metpo_traitmech_v9``, each a 1:1 mirror of its source predicate that
changes only the domain:

  produces           METPO:2000202 -> METPO:2007800   84
  reduces            METPO:2000017 -> METPO:2007802   30
  oxidizes           METPO:2000016 -> METPO:2007803   21
  exports            METPO:2000209 -> METPO:2007804   14
  imports            METPO:2000208 -> METPO:2007805   12
  hydrolyzes         METPO:2000013 -> METPO:2007808    6
  degrades           METPO:2000007 -> METPO:2007809    6
  accumulates        METPO:2000210 -> METPO:2007810    3
  disproportionates  METPO:2000200 -> METPO:2007811    2
  does not produce   METPO:2000222 -> METPO:2007801    1
  transports         METPO:2000207 -> METPO:2007812    1

All directions are unchanged; this is a relabel-and-reground pass like part 1.

ONE EDGE IS DELIBERATELY LEFT BEHIND, so the baseline lands at 1 rather than 0.
``metabolism/cellulolysis.yaml`` carries ``cellulose --METPO:2000013--> cellobiose``
under the label ``is hydrolyzed to``: the same CURIE as ``hydrolyzes`` but the
inverse reading, substrate to product rather than agent to substrate. Migrating
it onto METPO:2007808 would assert that cellulose hydrolyses cellobiose, so it
waits on the direction decision in #327. Selection is therefore by the edge's
``predicate`` LABEL, not by its CURIE alone.

Edits raw lines rather than round-tripping through write_validated_trait, which
is not byte-identical on hand-edited YAML (#322). Targets are keyed on
(subject, object, predicate_id) because the endpoint pair alone is not unique in
this corpus — see migrate_microbe_domain_edges.targets_in for the two cases.

Usage:
    python scripts/migrate_remaining_microbe_domain_edges.py            # dry-run
    python scripts/migrate_remaining_microbe_domain_edges.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from migrate_enables_trait_edges import _blocks  # noqa: E402

TRAITS_DIR = REPO_ROOT / "data/traits"

# (source CURIE, source label) -> (new label, new CURIE). Keyed on the LABEL too
# because METPO:2000013 is reached from two labels with opposite directions.
MAP: dict[tuple[str, str], tuple[str, str]] = {
    ("METPO:2000202", "produces"): ("produces", "METPO:2007800"),
    ("METPO:2000222", "does not produce"): ("does not produce", "METPO:2007801"),
    ("METPO:2000017", "reduces"): ("reduces", "METPO:2007802"),
    ("METPO:2000016", "oxidizes"): ("oxidizes", "METPO:2007803"),
    ("METPO:2000209", "exports"): ("exports", "METPO:2007804"),
    ("METPO:2000208", "imports"): ("imports", "METPO:2007805"),
    ("METPO:2000013", "hydrolyzes"): ("hydrolyzes", "METPO:2007808"),
    ("METPO:2000007", "degrades"): ("degrades", "METPO:2007809"),
    ("METPO:2000210", "accumulates"): ("accumulates", "METPO:2007810"),
    ("METPO:2000200", "disproportionates"): ("disproportionates", "METPO:2007811"),
    ("METPO:2000207", "transports"): ("transports", "METPO:2007812"),
}

# Present in the corpus on a mapped CURIE, but deliberately NOT migrated (#327).
EXCLUDED = {("METPO:2000013", "is hydrolyzed to")}


def targets_in(doc: dict) -> dict[tuple[str, str, str], tuple[str, str]]:
    out: dict[tuple[str, str, str], tuple[str, str]] = {}
    for graph in (doc.get("causal_graphs") or []):
        for e in (graph.get("edges") or []):
            key = (e.get("predicate_id"), e.get("predicate"))
            if key in EXCLUDED:
                continue
            new = MAP.get(key)
            if new:
                out[(e.get("subject"), e.get("object"), e.get("predicate_id"))] = new
    return out


def migrate_text(text: str, targets: dict[tuple[str, str, str], tuple[str, str]]) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    changed = 0
    for start, end in _blocks(lines):
        block = lines[start:end]
        idx: dict[str, tuple[int, str, str]] = {}
        subj = obj = pid = None
        for k, ln in enumerate(block):
            m = re.match(r"^(\s*-?\s*)(subject|object|predicate|predicate_id):\s+(.*?)(\s*)$", ln)
            if not m:
                continue
            key = m.group(2)
            if key not in idx:
                idx[key] = (k, m.group(1), m.group(4))
            if key == "subject":
                subj = m.group(3)
            elif key == "object":
                obj = m.group(3)
            elif key == "predicate_id":
                pid = m.group(3)
        if subj is None or obj is None:
            continue
        new = targets.get((subj, obj, pid))
        if new is None:
            continue
        label, curie = new
        for key, value in (("predicate", label), ("predicate_id", curie)):
            if key not in idx:
                continue
            k, prefix, trail = idx[key]
            block[k] = f"{prefix}{key}: {value}{trail}"
        lines[start:end] = block
        changed += 1
    return "".join(lines), changed


def _event(text: str, counts: dict[str, int], timestamp: str) -> str:
    moved = ", ".join(f"{n} to {label}" for label, n in sorted(counts.items()))
    changes = (
        f"Re-grounded {sum(counts.values())} causal edge(s) off microbe-domain METPO "
        f"predicates onto their causal-graph counterparts ({moved}), issue 301 part 2. "
        f"The previous predicates are transitively rdfs:subPropertyOf METPO:2000001, "
        f"whose rdfs:domain is METPO:1000525 (microbe), so a causal-graph subject "
        f"entailed that the subject IS a microbe; CausalNodeTypeEnum has no organism "
        f"member, so no such edge could ever satisfy the domain. Each replacement is a "
        f"1:1 mirror of its source predicate that changes only the domain, so the claim "
        f"each edge makes is unchanged and directions are unchanged. The replacements "
        f"are proposed in proposals/metpo_traitmech_v9 and are placeholder ids until "
        f"METPO mints them."
    )
    ev = {"timestamp": timestamp, "curator": "claude",
          "action": "MIGRATE_MICROBE_DOMAIN_EDGES_PART2", "changes": changes,
          "llm_assisted": True}
    block = yaml.safe_dump([ev], sort_keys=False, allow_unicode=True, width=88)
    lines = text.splitlines(keepends=True)
    start = next((i for i, ln in enumerate(lines)
                  if re.match(r"^curation_history:\s*$", ln)), None)
    if start is None:
        return text
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^[A-Za-z_][\w]*:", lines[j]):
            end = j
            break
    if lines and not lines[end - 1].endswith("\n"):
        lines[end - 1] += "\n"
    lines.insert(end, block)
    return "".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write files (default: dry-run)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    ap.add_argument("--timestamp", default="2026-08-06T02:00:00Z")
    args = ap.parse_args()

    tally: dict[str, int] = {}
    files_changed = 0
    for path in sorted(args.traits_dir.rglob("*.yaml")):
        text = path.read_text()
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        targets = targets_in(doc)
        if not targets:
            continue
        new_text, changed = migrate_text(text, targets)
        if changed != len(targets):
            print(f"ERROR: {path}: matched {changed} of {len(targets)} target edge(s) "
                  f"in text — refusing to write a partial migration", file=sys.stderr)
            return 1
        counts: dict[str, int] = {}
        for label, _curie in targets.values():
            tally[label] = tally.get(label, 0) + 1
            counts[label] = counts.get(label, 0) + 1
        if new_text != text:
            files_changed += 1
            if args.apply:
                path.write_text(_event(new_text, counts, args.timestamp))

    print(f"{'APPLIED' if args.apply else 'DRY-RUN'}: {sum(tally.values())} edge(s) in "
          f"{files_changed} file(s)", file=sys.stderr)
    for label, n in sorted(tally.items(), key=lambda x: -x[1]):
        print(f"    {label:<20} {n:>4}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
