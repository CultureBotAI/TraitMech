# Pseudohyphal Growth: METPO Proposal v529

## Context and Novelty

Add `traitmech:000653 pseudohyphal growth`, a PROPOSED MORPHOLOGY class
on base `37eae65865b9e7a05181443a294a70aa68f49e3f`. The trait describes
growth as attached elongated budding-cell chains with constricted junctions,
not a gene, assay label or generic filament.

Whole-repository searches included ignored and hidden files, terminology,
likely slugs, source identifiers and the proposed identifier block. No exact
record, synonym, unresolved causal node or prior proposal was found. Broad
numeric searches had incidental certificate-serial matches, not trait hits.
CommunityMech proposals and all-state TraitMech/upstream METPO GitHub searches
also found no exact candidate or `METPO:1060600` reservation. Search-index
absence is not proof that no historical discussion ever occurred.

The fresh seed contains 399 records, 344 shared with the pre-addition
1,047-record corpus. The 55 absent identifiers comprise 38 supporting fields
and 17 reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. None provides an
exact candidate or identifier collision. This does not establish trait exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The phenotype is a microscopic growth form, not a macroscopic colony shape.
`traitmech:000074 mycelial growth` is explicitly bacterial. The local
`METPO:1000674 filament shaped` definition broadly mentions hypha-like
structures, but its hierarchy is individual cell shape (`METPO:1000666`).
That record does not encode attached budding-cell chains and their constricted
junctions. Neither record is edited or treated as an exact duplicate.
Colony morphology (`METPO:1007062`) concerns macroscopic colonies; obsolete
cell arrangement (`METPO:1000046`) is not an active parent. Use phenotype
pending a more specific growth-form parent review.

Pseudohyphae and uninterrupted true hyphae are not interchangeable. Different
morphologies can coexist in one culture or occur at different times; no
organism-level disjointness is implied. Branching, a particular ploidy, serum,
nitrogen starvation, agar invasion, numerical morphology cutoffs and virulence
are not universal requirements. No exact synonym, xref or SSSOM mapping is asserted.

## Evidence and Example

| DOI | Evidence Role |
| --- | --- |
| [10.1590/S1517-83822013005000056](https://doi.org/10.1590/S1517-83822013005000056) | Definition, microscopy and canonical example; PMID:24516422, PMC3910194 |
| [10.1016/0092-8674(92)90079-r](https://doi.org/10.1016/0092-8674(92)90079-r) | Independent S. cerevisiae pseudohyphal-growth observation; PMID:1547504 |

For Staniszewska et al. (2013), the scientific abstract, Methods, Table 1,
Results subsection Pseudohyphae, Discussion and actual Figure 4 were read.
The short stored quote comes from Results. Publication was in 2013; PMC
release in 2014 is not a second study. Figure 4A,C supports constricted
pseudohyphal junctions alongside true hyphae in the six-hour population.
The Discussion also points to Figure 4A when describing one-hour aggregation;
that pointer does not override the concordant six-hour pseudohyphae Results
and Figure 4A caption used for the canonical example.

The canonical example is `NCBITaxon:5476 Candida albicans`, specifically
clinical bloodstream isolate 82 cultured for six hours in undiluted human
serum at 37 C. Its clinical origin is explicit in Methods and Table 1,
separately from engineered mutants. This is an in-vitro morphology claim,
not evidence of pseudohyphae in the patient's bloodstream. NCBI esearch/efetch
verified the species identifier, name and rank. Later hyphal predominance is
not misrepresented as absence of the earlier mixed population.

The 1992 scientific abstract was retrieved directly through Europe PMC.
Its full text, figures and strain provenance were not verified, so no
Saccharomyces canonical-example row or accession-resolved graph was added.
Its ploidy and induction constraints are source-specific. Two OPEN discussions
retain hierarchy/mapping and organism-scoped mechanism questions. Graph
deferral does not claim that morphogenesis mechanisms are unknown.

## Allocation and Contract

Reserve fresh block 1060600-1060699, using `METPO:1060600`, after v528's
1060500 block. Local identifier: `traitmech:000653`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

The current upstream contract was rechecked at
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Canonical class/property template blobs match the reviewed local copies:
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
This class-only cohort uses the 11-column header, including the three required
empty trailing directive cells. No property or mapping rows are needed.

The writer defaults to dry run, guards the parent projection and existing
target/template, prevalidates before writing and records LLM-assisted
provenance. Repository history is append-only.

## Verification

The writer dry run, direct LinkML/strict validation, history/products,
`just qc`, Ruff, 20 writer tests and 53 artifact-focused tests passed.
The full suite passed: 2,890 tests with two dependency deprecation warnings.
Proposal verification/coverage and ROBOT/ELK passed. Parsed RDF contains
15 class-template, 12,628 merged and 12,632 reasoned triples, with real w3id
phenotype/quality ancestry and no legacy METPO stubs. Headers match the
pinned upstream template, including required trailing empty directive cells.

Both snippets exact-match retrieved source text: 14 and 19 words. The
maintained online verifier returned NOT_IN_ABSTRACT for the 2013 Results
quote and VERIFIED for the 1992 scientific-abstract quote. No manual check
was relabeled as a resolver result and no frozen snippet baseline changed.
The NCBI-backed audit resolved all 730 examples with zero errors and 24
pre-existing label-drift warnings, none on this new example.

The corpus has 1,048 records and 598 discussions. All 1,047 prior YAMLs,
533 historical proposal templates, prior narratives and discussion templates
remain unchanged. Of the old trait pages, 1,046 change only in their footer;
phenotype gains its new child and changes from 148 to 149 children. That
child count is the only existing priority-row delta. All 139 source blobs of
reviewed claw commit `6d0a6fbbaeec47f42c6f999233b460e3f56bae89` were reverified.
Neither configured embedding input exists, so embedding regeneration is not claimed.

Desktop/mobile checks at 1440/390 px passed identity, provenance, two quotes,
the qualified example, two OPEN discussions, hierarchy navigation, dashboard
count and image loading, without overflow or page errors. All six screenshots
were visually inspected. Committed-history, staged whitespace, exact-head
review, remote-byte verification and CI/merge outcomes will be recorded on
the PR rather than preclaimed here.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed. After acceptance, refresh the ontology, migrate the
local identifier and references to the accepted METPO identifier, preserve
local-ID traceability and append-only history, and regenerate without adding
a duplicate record. Open scientific discussions need their own evidence review.

## Change Log

- v529, 2026-10-06: propose pseudohyphal growth with two primary references
  and a condition-qualified clinical-isolate example.
