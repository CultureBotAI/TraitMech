#!/usr/bin/env python3
"""#301 migration, part 1 of 2: the mechanical families.

Moves 185 of the 366 causal-graph edges that carry a microbe-domain METPO
predicate (transitively ``subPropertyOf METPO:2000001``, whose ``rdfs:domain``
is METPO:1000525) onto predicates a causal-graph node can actually satisfy.
Only the families whose target was already decided or is upstream:

  A  any subject -> TRAIT object      62  -> METPO:2007700  confers      (v8)
  B  activity subject `produces` X   103  -> RO:0002234     has output   (RO)
  D  TRAIT uses carbon/energy source  20  -> METPO:2007806/7            (v9)

Every edge here keeps its direction: this pass only relabels and re-grounds,
which is what makes it reviewable in one PR. The remaining 181 edges (enzyme,
transport and the rest of `produces`) need the other 11 v9 terms and follow
separately, per #301's warning that one 366-edge sweep would be unreviewable.

Family B takes an RO term rather than a new METPO one on purpose: biolink gives
`has output` ``domain: biological process or activity``, which BIOLOGICAL_PROCESS,
PATHWAY and MOLECULAR_FUNCTION subjects satisfy, so minting a METPO competitor
would be redundant. Subjects RO cannot cover (proteins, traits, chemicals) are
NOT touched here — they belong to METPO:2007800 in part 2.

Edits raw lines rather than round-tripping through write_validated_trait, which
is not byte-identical on hand-edited YAML (#322) and would bury the real changes
in reflow churn. Reuses the block splitter and curation-event writer from the
v8 migration so the two passes cannot drift apart.

Usage:
    python scripts/migrate_microbe_domain_edges.py            # dry-run
    python scripts/migrate_microbe_domain_edges.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_predicate_domains import METPO_OWL, microbe_domain_predicates  # noqa: E402
from migrate_enables_trait_edges import _blocks  # noqa: E402

TRAITS_DIR = REPO_ROOT / "data/traits"

PRODUCES = "METPO:2000202"
CARBON_SRC = "METPO:2000006"
ENERGY_SRC = "METPO:2000010"

CONFERS = ("confers", "METPO:2007700")
HAS_OUTPUT = ("has output", "RO:0002234")
HAS_CARBON = ("has carbon source", "METPO:2007806")
HAS_ENERGY = ("has energy source", "METPO:2007807")

# Subject types that satisfy biolink's 'biological process or activity' domain.
ACTIVITY = {"BIOLOGICAL_PROCESS", "PATHWAY", "MOLECULAR_FUNCTION"}


def target_for(pid: str, subject_type: str | None, object_type: str | None,
               microbe_domain: set[str]) -> tuple[str, str] | None:
    """The (label, curie) this edge migrates to, or None to leave it alone."""
    if pid not in microbe_domain:
        return None
    if object_type == "TRAIT":
        return CONFERS
    if pid == PRODUCES and subject_type in ACTIVITY:
        return HAS_OUTPUT
    if pid == CARBON_SRC:
        return HAS_CARBON
    if pid == ENERGY_SRC:
        return HAS_ENERGY
    return None  # part 2's families


def targets_in(doc: dict, microbe_domain: set[str]) -> dict[tuple[str, str, str], tuple[str, str]]:
    """Map (subject, object, predicate_id) -> (new_label, new_curie).

    Keyed on the TRIPLE, not the endpoint pair. Two real cases in this corpus
    make the pair alone unsafe, and both would have caused a silent mis-edit:

    - `ecology/biosafety_level_1.yaml` has `low_pathogen_hazard --produces-->
      bsl1_trait` (a target) AND `low_pathogen_hazard --qualifies for-->
      bsl1_trait` (UNGROUNDED, not a target) on the same endpoints. Keying by
      pair would have rewritten the ungrounded edge too.
    - `physiology/chemoheterotrophic.yaml` has both `uses energy source` and
      `uses carbon source` between the same two nodes; they take DIFFERENT
      targets, so one key cannot carry both.
    """
    out: dict[tuple[str, str, str], tuple[str, str]] = {}
    for graph in (doc.get("causal_graphs") or []):
        ntype = {n.get("node_id"): n.get("node_type") for n in (graph.get("nodes") or [])}
        for e in (graph.get("edges") or []):
            t = target_for(e.get("predicate_id"), ntype.get(e.get("subject")),
                           ntype.get(e.get("object")), microbe_domain)
            if t:
                out[(e.get("subject"), e.get("object"), e.get("predicate_id"))] = t
    return out


def migrate_text(text: str, targets: dict[tuple[str, str, str], tuple[str, str]]) -> tuple[str, int]:
    """Rewrite only the `predicate:` and `predicate_id:` lines. No reversals."""
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write files (default: dry-run)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    ap.add_argument("--owl", type=Path, default=METPO_OWL)
    ap.add_argument("--timestamp", default="2026-08-06T01:00:00Z")
    args = ap.parse_args()

    microbe_domain = microbe_domain_predicates(args.owl)
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
        targets = targets_in(doc, microbe_domain)
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

    total = sum(tally.values())
    print(f"{'APPLIED' if args.apply else 'DRY-RUN'}: {total} edge(s) in "
          f"{files_changed} file(s)", file=sys.stderr)
    for label in (CONFERS[0], HAS_OUTPUT[0], HAS_CARBON[0], HAS_ENERGY[0]):
        print(f"    {label:<20} {tally.get(label, 0):>4}", file=sys.stderr)
    return 0


def _event(text: str, counts: dict[str, int], timestamp: str) -> str:
    """Append this migration's CurationEvent at the end of curation_history.

    Insertion mirrors the v8 migration's writer: find the next top-level key
    rather than appending at EOF, because 5 records carry a `discussions:` block
    after their history.
    """
    moved = ", ".join(f"{n} to {label}" for label, n in counts.items() if n)
    changes = (
        f"Re-grounded {sum(counts.values())} causal edge(s) off microbe-domain METPO "
        f"predicates ({moved}), issue 301. The previous predicates are transitively "
        f"rdfs:subPropertyOf METPO:2000001, whose rdfs:domain is METPO:1000525 (microbe), "
        f"so a causal-graph subject entailed that the subject IS a microbe; "
        f"CausalNodeTypeEnum has no organism member, so no such edge could ever satisfy "
        f"the domain. Edge directions are unchanged - this pass only relabels and "
        f"re-grounds. RO:0002234 (has output) is used where the subject is an activity, "
        f"since biolink gives it the domain 'biological process or activity'; the METPO "
        f"replacements are proposed in proposals/metpo_traitmech_v8 and v9 and are "
        f"placeholder ids until METPO mints them."
    )
    ev = {"timestamp": timestamp, "curator": "claude",
          "action": "MIGRATE_MICROBE_DOMAIN_EDGES", "changes": changes,
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


if __name__ == "__main__":
    sys.exit(main())
