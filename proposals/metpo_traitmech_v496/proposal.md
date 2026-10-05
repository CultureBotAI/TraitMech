# Isogamy: METPO Proposal v496

## Context

Lift `traitmech:000619 isogamy`, a PROPOSED PHYSIOLOGY class. Searches of
the whole repository, including ignored and hidden files, found no exact
record, prior proposal, source-citation overlap or allocation collision before
writing. The available CommunityMech proposal tree was also searched.

The pinned 12,617-triple METPO graph contains no matching gamete or sexual
reproduction literal. A fresh 399-record seed compared with the 1,013-record
pre-addition corpus has 344 present and 55 absent IDs. Both frozen
release-review tables classify all 55 as 38 supporting-field rows and 17
duplicates, with no unclassified ID. These dispositions were checked against
the live corpus; the seed output is not itself a missing-work queue.

The all-state upstream isogamy issue search returned no results on 2026-10-05.
Paginated file inventories of open PRs #1477, #1476, #973 and #924 contain
no competing trait or proposal allocation. None of this proves that trait
discovery is exhausted.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

This is a reproductive phenotype defined by similar size of fusing gametes,
not equality of arbitrary cells, complete gamete symmetry, one mating type,
or a genomic feature. It is distinct from fungal self-fertility and
compatibility-locus systems. No exact numerical boundary with slight
anisogamy, universal behavioural identity, or disjointness is asserted.

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`,
in both record and template. A narrower reproductive-phenotype hierarchy
remains a curator TODO. PHYSIOLOGY is a filesystem category, not an OWL
parent. Keep PROPOSED status pending human curator signoff.

## Evidence and Limitations

- `DOI:10.1038/s42003-022-04275-y`, `PMID:36473948`, `PMC9726906`:
  the Introduction Sec1 definition sentence was checked against raw XML
  and publisher HTML. Main text and captions were read; actual Figure 4
  and Supplementary Table 2 were visually inspected. The source establishes
  terminology and structural asymmetry, not a mechanism maintaining size
  similarity. Reference-strain mutations are retained in the record.
- `DOI:10.1111/evo.13427`, `PMID:29345308`: the scientific-abstract
  clause was checked against raw Europe PMC metadata. It supports
  experimental use of an isogamous microalga, not an independent test of
  the definition criterion. Full-text access and strain provenance remain
  unresolved; the author-manuscript endpoint returned HTTP 403.

The record distinguishes vegetative-versus-gamete comparisons from
plus-versus-minus gamete comparisons. It defers natural canonical examples
and causal graphs. No protein accessions, xrefs, synonyms or SSSOM mappings
are asserted. Actual uninspected figures and source-data material remain
explicit limitations. A successful abstract match must not be represented
as inspection of a full paper or its figures.

## ID Space and Subset

Reserve `METPO:1057300` in `1057300-1057399`, after v495's block.
Subset: `metpo_traitmech_2026_10`. This is outside CommunityMech v1's
`1007100-1007220` range. The placeholder is not a released METPO ID;
retain `traitmech:000619` until upstream acceptance and release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or mapping template is needed. The 11-column class header follows
Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three empty trailing
directive cells. The expected local contract is absent, so its pinned
upstream version was read. CommunityMech v1 is the worked reference.
Legacy OBO-prefix examples do not override the pinned ontology's w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v496
just robot-validate-proposal metpo_traitmech_v496
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect actual
`https://w3id.org/metpo/` IRIs and the labeled phenotype/quality ancestry;
ELK success alone does not rule out a detached parent stub.

Local proposal verification passed with zero failures and complete coverage
of 619 local IDs. ROBOT/ELK passed without UNSAT; merged/reasoned outputs
contain 23,322/23,326 lines. Structured inspection confirmed the proposed
w3id class is below the labeled phenotype parent and its quality ancestor,
with no legacy OBO-prefix METPO stub. The maintained snippet resolver
returned NOT_IN_ABSTRACT for the 2022 Introduction quote and VERIFIED for
the 2018 scientific-abstract clause; both separately matched raw sources.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` after local review.

## Round-Trip Plan

After upstream acceptance and release, refresh the pinned ontology and migrate
to the accepted METPO CURIE. Preserve the local identifier in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and avoid creating a second primary record for the same trait.

## Change Log

- v496, 2026-10-05: propose isogamy with two DOI-backed sources, exact
  evidence snippets, size-based scope and qualified strain provenance.
