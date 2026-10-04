# Positive Autotropism: METPO Proposal v481

## Context

Lift `traitmech:000604 positive autotropism`, a PROPOSED PHYSIOLOGY class,
to a provisional upstream slot. The definition concerns directional growth
toward same-species neighbors, not completed fusion or a specific signal.
Its two DOI-backed evidence entries include verbatim snippets.

Before this addition, a fresh seed generated 399 records against 998 live
records: 344 already present and 55 absent. Structured joins to both frozen
2026-06-12 review tables classified those 55 as 38 supporting-field rows and
17 duplicates. The frozen dispositions are not a missing-work queue.

Whole-repository searches included ignored and hidden files, labels, likely
slugs, citations, synonyms, graphs, discussions, research, proposals, generated
artifacts and history. Autotropism hits concerned the negative sibling and
its boundary notes; Biolink anastomosis relations do not define this phenotype.
A structured search of the pinned 12,617-triple METPO graph found no exact
autotropism, hyphal-homing, self-attraction or anastomosis term. Upstream
all-state issue search for autotropism found no prior issue on 2026-10-04.
Open TraitMech PRs did not overlap this addition.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This reusable directional phenotype is neither a sequence feature nor a
source-specific field. The negative sibling asserts the opposite direction,
not an equivalent trait under another label. No redundant polarity wrapper
around an existing same-scope parent is being added.

## Hierarchy Decisions

Use the released `METPO:1000059 phenotype`, whose parent is
`METPO:1000188 quality`. The pinned ontology uses `https://w3id.org/metpo/`.
Growth orientation does not require whole-cell motility. The evidence does
not establish a universal chemical cue, so `chemotropism` is not asserted
as a parent. Negative autotropism is a sibling, not a parent.

Emergence and extension are separate qualifying readouts. Anastomosis,
adhesion, mating, contact alone and passive alignment are not exact synonyms.
Neither genetic identity nor successful fusion is required by the definition.
The negative sibling's existing boundary note remains accurate and does not
contain an unresolved exact node, synonym or missing-parent assertion to repair.
No external xrefs, synonyms or SSSOM equivalences are proposed.

## Evidence and Limitations

- `DOI:10.1093/jxb/19.1.125`: directly retrieved publisher abstract supplies
  the positive-autotropism terminology and spore-orientation readout. Full
  paper and strain provenance remain unread; substrate conditions are retained.
- `DOI:10.1039/d3lc00859b` (`PMID:38416560`, `PMC10964749`): directly read
  primary full text and inspected Figure 5 support directional extension
  before fusion. This phenotype interpretation does not claim that the paper
  uses the autotropism label. Its representative trace is not a replicate count.

Both stored snippets were exact-matched against directly retrieved source
text. Supplement access attempts failed; no movie inspection is claimed.
Natural canonical strains and protein-resolved mechanisms remain explicit
CURATION_TODOs. No causal graph is asserted.

## ID Space and Subset

Reserve `METPO:1055800` in the fresh `1055800-1055899` block, following v480's
`1055700-1055799` block. An ignored-and-hidden whole-repository collision search
was empty before writing the new artifacts. This block does not overlap
CommunityMech v1. Subset: `metpo_traitmech_2026_10`.
The local identifier stays `traitmech:000604` pending upstream acceptance.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Evidence, boundaries and migration |

No property or SSSOM artifact is needed. The class template preserves the
upstream 11-column headers, including three trailing empty directive cells.

## Verification

Run the maintained gates and inspect the emitted hierarchy, not just ELK's exit:

```bash
just verify-proposal metpo_traitmech_v481
just robot-validate-proposal metpo_traitmech_v481
just audit-proposal-coverage
just qc
```

Confirm that the proposed class's parent is the labeled released phenotype
at its w3id IRI, with quality ancestry and no legacy OBO METPO stub. The TSV
definition and parent must match the TraitRecord. Required trailing empty
header cells are not disposable whitespace.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following TraitMech
review. The placeholder reservation is not an upstream acceptance claim.

## Round-Trip Plan

When METPO accepts and releases the term, update the pinned ontology, use the
accepted METPO identifier in this record and preserve the old local CURIE in
an explicit migration artifact and append-only history. Regenerate dependent
pages, discussions and reports; do not create a second primary record.

## Change Log

- v481, 2026-10-04: propose positive autotropism with separate emergence and
  extension evidence and explicit fusion, provenance and mechanism boundaries.
