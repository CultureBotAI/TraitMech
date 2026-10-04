# Hyphal Anastomosis: METPO Proposal v482

## Context

Lift `traitmech:000605 hyphal anastomosis`, a PROPOSED PHYSIOLOGY class,
to a provisional upstream slot. Completed vegetative fusion establishes
cytoplasmic continuity; approach alone is not this phenotype. Three primary
DOI-backed sources have exact abstract snippets.

Before this addition, a fresh seed produced 399 records against 999 live
records: 344 already present and 55 absent. Structured joins to both frozen
2026-06-12 review tables classify those 55 as 38 supporting-field rows and
17 duplicates, not an uncurated trait queue.

Whole-repository searches included ignored and hidden files, exact labels,
slugs, citations, fusion synonyms, graphs, discussions, research, proposals,
generated artifacts and history. Existing autotropism boundary notes and
Biolink anatomical anastomosis relations do not denote an exact trait record.
A structured search of the pinned 12,617-triple METPO graph found no exact
class. All-state upstream issue searches for anastomosis and hyphal fusion
were empty on 2026-10-04. Open TraitMech PRs did not overlap this addition.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This reusable organismal phenotype is not a sequence feature, gene, assay
column or an individual fusion event. No predicate or schema-enum lift is needed.

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`, with
the pinned ontology's `https://w3id.org/metpo/` namespace. Whole-cell motility,
directional attraction and a particular signaling mechanism are not required.
The existing positive-autotropism record describes approach, not fusion.
Its boundary note contains no unresolved exact causal node, synonym or
missing-parent assertion requiring repair.

`Vegetative hyphal fusion` is a source-named exact synonym. Unqualified
anastomosis, self-fusion, mating and recombination are not exact equivalents.
Genetic identity and enduring postfusion compatibility are not prerequisites.
No external xrefs or SSSOM mappings are asserted without issuer-resolved
organismal equivalence.

## Evidence and Limitations

- `DOI:10.1128/aem.65.12.5571-5575.1999` (`PMID:10584019`): direct
  fusion/flow evidence. Publisher methods/results/discussion and actual
  Figures 1 and 3 were inspected. Figure 2 was not visually inspected.
- `DOI:10.1128/ec.00191-12` (`PMID:23042130`): names the exact synonym
  and provides native soft perturbation/rescue evidence. Actual Figure 3 was
  inspected. Static connectivity, non-clean delta-so238 and unsuccessful
  delta-so75 complementation are explicitly qualified; supplements remain unread.
- `DOI:10.1111/j.1469-8137.2008.02726.x` (`PMID:19140939`): supports
  nonself fusion. Relevant methods/results/discussion were read; figures and
  supplementary movies were not visually inspected. An apparent Table 1
  column-footnote mismatch is recorded without reusing those column rates.

Every snippet was exact-matched to its directly retrieved Europe PMC abstract.
Genetic marker transfer is not evidence of nuclear recombination. Native
protein accessions, modern strain identities and canonical provenance remain
CURATION_TODOs; no causal graph is asserted.

## ID Space and Subset

Reserve `METPO:1055900` in `1055900-1055999`, following v481's
`1055800-1055899` block. The ignored-and-hidden whole-repository collision
search was empty before writing. This does not overlap CommunityMech v1.
Subset: `metpo_traitmech_2026_10`. The local ID remains `traitmech:000605`
pending upstream acceptance.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Evidence, boundaries and migration |

No property or SSSOM file is needed. The 11-column upstream template includes
three trailing empty directive cells. Its headers were checked against
Knowledge-Graph-Hub/kg-microbe at `1408e7099d039026d7611c240938d8e177753406`.

## Verification

```bash
just verify-proposal metpo_traitmech_v482
just robot-validate-proposal metpo_traitmech_v482
just audit-proposal-coverage
just qc
```

Inspect the emitted OWL for the proposed class, its released phenotype
parent and quality ancestry. A legacy OBO METPO stub is not that parent.
Verify label, definition, exact synonym and parent parity with the record.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following TraitMech
review. A reserved placeholder does not imply upstream acceptance.

## Round-Trip Plan

After upstream acceptance and release, update the pinned ontology and replace
the local identifier with the accepted METPO CURIE. Preserve the old local
CURIE in an explicit migration artifact and append-only history, then regenerate
dependent pages, discussions and reports. Do not create a second primary record.

## Change Log

- v482, 2026-10-04: propose hyphal anastomosis with direct fusion evidence,
  a source-named synonym and explicit nonself, provenance and mechanism boundaries.
