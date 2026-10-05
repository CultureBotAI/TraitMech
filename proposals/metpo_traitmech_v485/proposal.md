# Heterokaryosis: METPO Proposal v485

## Context

Lift `traitmech:000608 heterokaryosis`, a PROPOSED GENOMICS class. This
denotes a reusable nuclear-state phenotype, not a literal sequence feature.
Whole-repository searches included ignored and hidden files, spelling
variants, citations, synonyms, graph nodes, discussions, research, proposals,
pages and history. No exact record was found. Existing ploidy, hyphal
anastomosis, heterokaryon incompatibility and parasexuality records concern
distinct properties or processes. Their contextual mentions do not create
an unresolved exact node or synonym requiring mutation.

The pinned 12,617-triple METPO graph contains no matching term. A fresh
399-record seed reconciled against the 1,002-record pre-addition corpus
has 344 present and 55 absent IDs. Both frozen release-review tables classify
those 55 as 38 supporting-field rows and 17 duplicates, not missing primary
traits. An all-state upstream issue search for heterokary returned no result
on 2026-10-04.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`, in
the pinned ontology's `https://w3id.org/metpo/` namespace. GENOMICS is a
filesystem category, not a new ontology parent. Nuclear identity differs
from genome-copy number and multinucleation. Neither cell fusion,
incompatibility nor parasexual reproduction is an is-a parent.

The fungal definition does not require exactly two nuclei, diploidy, fixed
nuclear ratios or universal fertility. A heterokaryon is a structure, so
the bare noun is not asserted as an exact phenotype synonym. Broader uses
of the terminology and external identifiers require separate interpretation;
no xrefs, SSSOM mappings or exact synonyms are asserted.

## Evidence and Limitations

- `DOI:10.1098/rspb.2022.0971` (`PMID:35946150`) supplies the definition.
  Full-text XML was read, but actual figures and supplements remain
  uninspected. Gene-expression correlations are not causal protein evidence.
- `DOI:10.1098/rspb.2014.0084` (`PMID:24850920`) supports a qualified natural
  P581 example. Component stock IDs are not heterokaryon IDs. NCBI directly
  resolves taxon 40127 to active Neurospora tetrasperma. The record retains
  primary provenance and tissue qualifiers; figures and supplements remain
  uninspected.
- `DOI:10.1016/j.fgb.2018.01.005` (`PMID:29331685`) provides independent
  experimental support. Figures 5-6 were inspected; other figures and
  supplements were not. Engineered fluorescent histones can exchange, so
  color alone does not establish nuclear fusion or genotype.

All three snippets exact-match directly retrieved Europe PMC abstracts with
single-hit DOI/PMID metadata. Two CURATION_TODOs retain scope, mechanism,
source-access and readout limits. No protein-resolved causal graph is
asserted, and NONMECHANISTIC is not used to bypass missing grounding.

## ID Space and Subset

Reserve `METPO:1056200` in `1056200-1056299`, after v484's block.
Ignored-and-hidden searches across this repository and CommunityMech
proposals found no collision before writing. Subset:
`metpo_traitmech_2026_10`. Keep local `traitmech:000608` pending release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class template
follows the upstream headers with three trailing empty directive cells.
The upstream contract is pinned to Knowledge-Graph-Hub/kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406`.

## Verification

```bash
just verify-proposal metpo_traitmech_v485
just robot-validate-proposal metpo_traitmech_v485
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect emitted
OWL for the released w3id phenotype parent and quality ancestor; an ELK
pass against a legacy OBO parent stub is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following local
review. The reserved placeholder does not imply upstream acceptance.

## Round-Trip Plan

After acceptance and release, update the pinned ontology and migrate to
the accepted METPO CURIE. Preserve the local identifier in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and avoid creating a duplicate primary record.

## Change Log

- v485, 2026-10-04: propose heterokaryosis with three primary snippets and
  a qualified natural-strain example.
