#!/usr/bin/env python3
"""One-time migration: move `enables`->TRAIT edges onto the v8 predicates.

Rewrites the 164 causal-graph edges that carry ``predicate_id: RO:0002327``
with a ``TRAIT`` object (#302) onto the three predicates proposed in
``proposals/metpo_traitmech_v8``:

  confers                METPO:2007700   direction unchanged
  has electron donor     METPO:2007701   direction REVERSED
  has electron acceptor  METPO:2007702   direction REVERSED

`enables` is the wrong relation for a TRAIT object: biolink gives it the range
'biological process or activity' and a trait is a disposition, so each edge
entails ``trait ⊑ BiologicalProcessOrActivity``. The electron edges additionally
lost their donor/acceptor role when PR #300 collapsed both onto `enables`
(#303); those are reversed back to ``<trait> --has electron donor|acceptor-->
<chemical>``, the direction METPO:2000008/2000009 expressed before their
inherited microbe domain made them unusable in causal graphs (#301).

WHY SURGICAL TEXT EDITS RATHER THAN load->write_validated_trait: round-tripping
a hand-edited trait YAML through the helper is NOT byte-identical (#322) — it
re-wraps long strings and drops hand-written quoting. Over 128 files that buries
164 real changes in reflow churn, which is the unreviewable outcome #301 warns
about. So the parsed document is used only to DECIDE, and the edit is applied to
the raw lines: exactly the `subject:`/`object:`/`predicate:`/`predicate_id:`
lines that change, nothing else.

Classification is the same rule the v8 proposal published: a CHEMICAL subject
whose label or edge description names an electron donor/acceptor role goes to
the role-bearing pair; everything else goes to `confers`. A MOLECULAR_FUNCTION
node such as oxygen_preference's "O2 as terminal electron acceptor" denotes the
USE of O2 rather than O2 itself, so it is deliberately NOT treated as a chemical
species and grounds to `confers`.

Usage:
    python scripts/migrate_enables_trait_edges.py            # dry-run
    python scripts/migrate_enables_trait_edges.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data/traits"

ENABLES = "RO:0002327"
CONFERS = ("confers", "METPO:2007700")
DONOR = ("has electron donor", "METPO:2007701")
ACCEPTOR = ("has electron acceptor", "METPO:2007702")

ACCEPTOR_RE = re.compile(r"electron acceptor|terminal electron", re.I)
DONOR_RE = re.compile(r"electron donor|donors? for|reducing equivalent", re.I)


def classify(subject_type: str | None, subject_label: str, description: str) -> tuple[str, str]:
    """Return the (label, curie) this edge migrates to."""
    if subject_type == "CHEMICAL":
        blob = f"{subject_label} {description}"
        if ACCEPTOR_RE.search(blob):
            return ACCEPTOR
        if DONOR_RE.search(blob):
            return DONOR
    return CONFERS


def targets_in(doc: dict) -> dict[tuple[str, str], tuple[str, str]]:
    """Map (subject_id, object_id) -> (new_label, new_curie) for this document.

    Keyed by the node-id pair because that is what identifies the edge in the
    raw text. Two edges in one file sharing BOTH endpoints would collide; the
    corpus has none (asserted by the caller's count check).
    """
    out: dict[tuple[str, str], tuple[str, str]] = {}
    for graph in (doc.get("causal_graphs") or []):
        nodes = graph.get("nodes") or []
        ntype = {n.get("node_id"): n.get("node_type") for n in nodes}
        nlabel = {n.get("node_id"): (n.get("label") or "") for n in nodes}
        for e in (graph.get("edges") or []):
            if e.get("predicate_id") != ENABLES:
                continue
            subj, obj = e.get("subject"), e.get("object")
            if ntype.get(obj) != "TRAIT":
                continue
            out[(subj, obj)] = classify(
                ntype.get(subj), nlabel.get(subj, ""), e.get("description") or "")
    return out


def _blocks(lines: list[str]) -> list[tuple[int, int]]:
    """(start, end) line spans of every `- subject:` edge block."""
    starts = [i for i, ln in enumerate(lines)
              if re.match(r"^\s*-\s+subject:\s+\S", ln)]
    spans = []
    for n, s in enumerate(starts):
        indent = len(lines[s]) - len(lines[s].lstrip())
        end = len(lines)
        for j in range(s + 1, len(lines)):
            ln = lines[j]
            if not ln.strip():
                continue
            cur = len(ln) - len(ln.lstrip())
            # Next sibling list item, or a dedent out of this list.
            if (cur == indent and ln.lstrip().startswith("- ")) or cur < indent:
                end = j
                break
        spans.append((s, end))
    return spans


def migrate_text(text: str, targets: dict[tuple[str, str], tuple[str, str]]) -> tuple[str, int]:
    """Apply the edge rewrites to raw YAML text. Returns (new_text, n_changed)."""
    lines = text.splitlines(keepends=True)
    changed = 0
    for start, end in _blocks(lines):
        block = lines[start:end]
        idx = {}
        subj = obj = None
        for k, ln in enumerate(block):
            m = re.match(r"^(\s*-?\s*)(subject|object|predicate|predicate_id):\s+(.*?)(\s*)$", ln)
            if not m:
                continue
            key, val = m.group(2), m.group(3)
            # Only the FIRST occurrence at block level; nested evidence blocks
            # do not carry these keys, but be defensive rather than clever.
            if key not in idx:
                idx[key] = (k, m.group(1), val, m.group(4))
            if key == "subject":
                subj = val
            elif key == "object":
                obj = val
        if subj is None or obj is None:
            continue
        new = targets.get((subj, obj))
        if new is None:
            continue
        new_label, new_curie = new
        reverse = new_curie in (DONOR[1], ACCEPTOR[1])

        for key, value in (("predicate", new_label), ("predicate_id", new_curie)):
            if key not in idx:
                continue
            k, prefix, _old, trail = idx[key]
            block[k] = f"{prefix}{key}: {value}{trail}"
        if reverse:
            for key, value in (("subject", obj), ("object", subj)):
                k, prefix, _old, trail = idx[key]
                block[k] = f"{prefix}{key}: {value}{trail}"
        lines[start:end] = block
        changed += 1
    return "".join(lines), changed


def _event_yaml(counts: dict[str, int], timestamp: str) -> str:
    """One CurationEvent, emitted in the corpus's existing style."""
    moved = ", ".join(f"{n} to {label}" for label, n in counts.items() if n)
    reversed_n = counts.get(DONOR[0], 0) + counts.get(ACCEPTOR[0], 0)
    changes = (
        f"Migrated {sum(counts.values())} causal edge(s) off enables/RO:0002327 "
        f"with a TRAIT object ({moved}), issue 302. RO:0002327 has range "
        f"'biological process or activity', which a trait (a disposition) cannot "
        f"satisfy, so the previous form entailed trait is-a BiologicalProcessOrActivity. "
        f"The replacements are proposed in proposals/metpo_traitmech_v8 and are "
        f"placeholder ids until METPO mints them."
    )
    if reversed_n:
        changes += (
            f" {reversed_n} electron edge(s) were also reversed back to "
            f"trait -> chemical, restoring the donor/acceptor role that PR 300 "
            f"collapsed onto enables (issue 303); the organism-subject problem that "
            f"forced that collapse does not arise here because these predicates take "
            f"a causal-node domain rather than METPO:2000001's microbe domain "
            f"(issue 301)."
        )
    event = {
        "timestamp": timestamp,
        "curator": "claude",
        "action": "MIGRATE_ENABLES_TRAIT_EDGES",
        "changes": changes,
        "llm_assisted": True,
    }
    return yaml.safe_dump([event], sort_keys=False, allow_unicode=True, width=88)


def append_curation_event(text: str, counts: dict[str, int], timestamp: str) -> str:
    """Insert a CurationEvent at the END of the curation_history block.

    Appending at end-of-file would be wrong for the 5 records that carry a
    `discussions:` block after their history, so find the next top-level key
    instead and insert above it.
    """
    lines = text.splitlines(keepends=True)
    start = next((i for i, ln in enumerate(lines)
                  if re.match(r"^curation_history:\s*$", ln)), None)
    if start is None:
        return text
    end = len(lines)
    for j in range(start + 1, len(lines)):
        # A top-level key ends the block; list items and nested lines are indented.
        if re.match(r"^[A-Za-z_][\w]*:", lines[j]):
            end = j
            break
    block = _event_yaml(counts, timestamp)
    if lines and not lines[end - 1].endswith("\n"):
        lines[end - 1] += "\n"
    lines.insert(end, block)
    return "".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write the files (default: dry-run)")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    ap.add_argument("--timestamp", default="2026-08-06T00:00:00Z",
                    help="CurationEvent timestamp (fixed, so a re-run is reproducible)")
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
            new_text = append_curation_event(new_text, counts, args.timestamp)
            files_changed += 1
            if args.apply:
                path.write_text(new_text)

    total = sum(tally.values())
    print(f"{'APPLIED' if args.apply else 'DRY-RUN'}: "
          f"{total} edge(s) in {files_changed} file(s)", file=sys.stderr)
    for label in (CONFERS[0], DONOR[0], ACCEPTOR[0]):
        print(f"    {label:<24} {tally.get(label, 0):>4}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
