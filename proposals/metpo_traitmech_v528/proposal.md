# Rosette Cell Arrangement: METPO Proposal v528

## Context

Add `traitmech:000652 rosette cell arrangement`, a PROPOSED MORPHOLOGY
class on base `4adb4e95f861520d5030f076d6f36f2b811ca788`. This is an
organismal morphology, not a gene, protein, individual cell shape or assay.

Ignored-and-hidden whole-repository searches covered terminology, likely slugs,
DOI/PMID bundles, identifiers and the proposed block. The star-shaped research
report explicitly distinguishes rosettes from one star-shaped cell. The
bacterial citation also supports the existing monotrichous example, not an
exact rosette trait. No same-scope record, synonym or unresolved causal node
was found. These existing records need no edit.

The fresh seed has 399 records, 344 shared with the pre-addition 1,046-record
corpus. Its 55 absent identifiers comprise 38 supporting fields and 17 reviewed
duplicates; all 38 formerly unselected classes are now live. Structured review
covered 1,546 release-delta rows, 153 active-review rows and the 12,617-triple
ontology. No exact candidate or proposed-block collision was found. These
results do not establish exhaustion of microbial traits.

All-state TraitMech and upstream METPO GitHub searches returned no indexed
rosette proposal or exact identifier reservation. CommunityMech proposals were
also searched including ignored and hidden files. Search-index absence is not
proof that no prior discussion ever occurred.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The defining feature is organized inward cell polarity around a central region
of a multicellular cluster. It does not require a particular formation route,
perfect sphere, one attachment point, fixed cell count or bacterial adhesin.
Irregular aggregation alone does not establish it.

Cell shape `METPO:1000666` concerns an individual cell; colony morphology
`METPO:1007062` and colony shape `METPO:1007063` concern macroscopic colonies
on solid medium. Obsolete cell arrangement `METPO:1000046` is not an active
parent. Star shaped `METPO:1000685`, staphylococcus arrangement
`traitmech:000118`, holdfast `traitmech:000184` and biofilm formation
`traitmech:000053` have distinct scopes. Co-occurrence does not imply
organism-level disjointness. Use phenotype pending human hierarchy review;
no exact xref, synonym or SSSOM mapping is asserted.

## Evidence and Limits

| DOI | Evidence role |
| --- | --- |
| [10.7554/eLife.41482](https://doi.org/10.7554/eLife.41482) | Definition, polarity/clumping comparison and S. rosetta example; PMID:30556809, PMC6322860 |
| [10.1128/jb.00064-19](https://doi.org/10.1128/jb.00064-19) | Bacterial rosettes and geometry boundaries; PMID:31010900, PMC6707911 |

Both short snippets are directly read Results passages. The 2018 full-text XML,
first Results subsection, relevant culture/scoring Methods and actual Figure 1
were inspected. The 2019 publisher HTML Results, relevant Discussion and
growth/sampling/microscopy Methods plus actual Figure 4 were inspected.
Supplemental Figure S2's text was accessible, but its image was not verified.
Search-result text is not treated as a verified snippet or panel inspection.

The example is NCBITaxon:946362 Salpingoeca rosetta, qualified to wild-type
SrEpac and induced rosettes rather than every life stage. NCBI efetch resolved
the species identifier and label. Primary strain provenance was read directly
in the PMC author manuscript of
[Levin and King (2013)](https://doi.org/10.1016/j.cub.2013.08.061),
Experimental Procedures and Figure 1 caption. That provenance-only reference
stays in the example note and does not inflate the two-citation evidence gate.

The source-specific exclusion of aggregation in S. rosetta must not override
the bacterial adhesion example. No universal homologous mechanism is asserted.
Two OPEN discussions retain hierarchy/mapping and organism-scoped mechanism
tasks. No causal graph or protein accession is added; sequence possession alone
does not establish the observed arrangement.

## ID Space and Files

Reserve fresh block 1060500-1060599, using `METPO:1060500`, after v527's
1060400 block. Local identifier: `traitmech:000652`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

The upstream contract remains pinned to
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Canonical class/property template blobs were rechecked against that current
pin; layouts have 11 and 13 columns respectively. This class-only cohort uses
the canonical 11-column header, including three empty trailing directive cells.
Properties and SSSOM mappings are omitted.

The writer defaults to dry run, guards the reviewed parent projection and any
existing target/template, prevalidates before writing, and records LLM-assisted
curation provenance. Repository history is append-only.

## Verification

Writer dry run, direct LinkML/strict validation, history/products, `just qc`,
Ruff, 20 writer tests and 53 artifact-focused tests passed. The complete suite
passed: 2,870 tests with two dependency deprecation warnings.

Proposal verification/coverage and ROBOT ELK passed. Parsed RDF contains
15 class-template, 12,628 merged and 12,632 reasoned triples, with real w3id
phenotype/quality ancestry and no legacy METPO stubs. Template headers match
the pinned upstream bytes, including their required empty cells.

Both online snippet-verifier rows returned NOT_IN_ABSTRACT. The 2018 quote
exact-matches the directly read XML Results, and the 2019 quote was directly
checked in publisher HTML Results. These manual checks are not relabeled as
resolver VERIFIED outcomes. No new snippet-audit finding or baseline exception
was introduced. The NCBI-backed canonical-example audit resolved all 729
examples with zero errors and 24 label-drift warnings on pre-existing records;
none concerns the new example.

The corpus has 1,047 records and 596 discussions. All 1,046 prior YAML files,
532 historical proposal templates, prior proposal narratives and discussion
templates remain unchanged. Of the old trait pages, 1,045 change only in their
footer; phenotype gains the child and changes from 147 to 148 children. That
child count is the only existing priority-row change. All 139 source blobs of
reviewed claw commit `6d0a6fbbaeec47f42c6f999233b460e3f56bae89` were reverified.
Both configured embedding inputs are absent, so no embedding regeneration is
claimed.

Desktop/mobile browser checks at 1440/390 px passed identity, provenance,
two quotes, the qualified example, source limits, hierarchy navigation,
dashboard counts and image loading, without overflow or page errors.
All six screenshots were visually inspected. The ordinary staged whitespace
check flags only the three required trailing empty ROBOT directive cells;
both exact-path scoped checks passed without weakening global Git settings.
The committed-history gate,
exact-head review, remote-byte verification and CI/merge outcomes will be
recorded on the PR, not preclaimed here.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new upstream
issue is claimed. After acceptance, refresh the ontology, migrate the local
identifier and references to the accepted METPO identifier, preserve local-ID
traceability and append-only history, and regenerate without creating a second
record. Scientific discussions remain open until their own evidence and
grounding tasks are resolved.

## Change Log

- v528, 2026-10-06: propose rosette cell arrangement with two primary sources
  and a provenance-qualified canonical example.
