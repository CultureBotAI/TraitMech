# Karyoklepty: METPO Proposal v506

## Context

Add `traitmech:000630 karyoklepty`, a PROPOSED PHYSIOLOGY class for selective
retention and use of prey nuclei. This is an organismal phenotype, not a
literal nucleus, nucleomorph, sequence feature or gene-transfer event.

Novelty and allocation searches included ignored and hidden files throughout
TraitMech and CommunityMech proposals. No exact record, prior proposal or
same-scope unresolved mention was found. Structured review of all 12,617
pinned METPO triples found no exact term. All-state TraitMech/METPO PR
searches found no competing term; open PR heads remain unchanged from their
previously inspected file inventories. Base main is
`0d008f73a1bd10952e1ab4abf75837814dfcfda6`.

A fresh 399-record seed shares 344 IDs with the pre-addition 1,024-record
corpus. Its 55 absent IDs reconcile to 38 supporting-field terms and 17
reviewed duplicates. The full 1,546-row release delta and 153-row active
review were checked against live identifiers and repository history;
all 38 formerly unselected classes are now live. Literature discovery is
not exhausted by this reconciliation.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Use phenotype pending a closer organelle-acquisition hierarchy. Kleptoplasty
`traitmech:000629` concerns plastids, phagocytosis `traitmech:000627` concerns
uptake, and phagotrophy `traitmech:000628` concerns nutrition. Endosymbiosis
`traitmech:000045` describes an intracellular organism rather than selective
retention of its nucleus. None supplies an exact equivalent or a demonstrated
universal parent for this class. Whole living prey and DNA detection alone
are insufficient. Nuclear division, fusion, fixed retention intervals,
host-genome integration and photosynthesis are not definition requirements.
No existing YAML, synonym, xref or causal graph is changed.

## Evidence and Example

- `DOI:10.1038/nature05496`, `PMID:17251979`: directly retrieved scientific
  abstract supports the named strategy and functional prey-nucleus use.
  Main text, figures and supplements were not accessed.
- `DOI:10.1186/s12864-015-2052-9`, `PMID:26475598`, `PMC4609049`:
  scientific Abstract and Background read; the stored naming snippet is
  from Background, not an abstract. No claim of audited experimental
  detail or independent terminology replication is made.
- `DOI:10.3389/fmicb.2017.00423`, `PMID:28377747`, `PMC5359308`:
  main text and actual Figures 2-5 and 9 inspected; supplements not audited.
  The Results snippet and strain-qualified example retain the distinction
  between microscopy, physiological correlation and modeled inheritance.

NCBI independently resolves `NCBITaxon:704171 Mesodinium rubrum`, including
the synonym Myrionecta rubra. The canonical note identifies MBL-DK2009 and
the primary Methods provenance URL. Provenance is not an extra independent
publication. Three concise snippets have directly retrieved source sections;
maintained resolver verdicts are recorded separately from manual checks.

## ID Space and Files

Reserve `METPO:1058300` in the fresh 1058300-1058399 block, after v505's
1058200 block. Ignored-and-hidden searches found no collision, including
CommunityMech proposals; this is outside its v1 block. Use subset
`metpo_traitmech_2026_10`. The local ID occurs in one new record.

The canonical kg-microbe contract at
`ea1c5f15e6c4dba6c72165367162b354e215f018`, class/property templates,
CommunityMech v1 and TraitMech v505 informed this cohort. Use w3id METPO
IRIs, not the legacy prefix in example commands. Definition provenance
contains literature and the local minting record, not ontology mappings.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted; no equivalence asserted |

## Verification

The guarded writer passed dry run and 11 focused tests covering apply/replay,
parent preservation and fail-closed drift refusal. Direct LinkML and strict
record validation passed. The maintained snippet resolver returned one
VERIFIED scientific-abstract span and two NOT_IN_ABSTRACT full-text spans.
All three exact contiguous passages were independently matched to directly
retrieved sections; full-text checks are not relabeled VERIFIED.

The live NCBI audit resolved all 722 examples across 537 records with zero
errors and 24 existing warnings, none for the new example. Proposal
verification, cross-cohort coverage and ROBOT ELK reasoning passed with no
unsatisfiable class. Direct RDF inspection confirms the definition and
labeled phenotype-to-quality hierarchy under w3id IRIs, with no legacy METPO
stub. The merged graph contains 12,628 triples in 23,322 physical lines; the
reasoned graph contains 12,632 triples in 23,326 lines.

Maintained generators refreshed the discussion browser, QC dashboard,
priority dashboard and trait pages. Playwright checks passed at 1440- and
390-pixel widths: local identifier provenance, three citations and quotes,
one qualified example, two discussions, reciprocal parent navigation,
1,025-record dashboard and loaded coverage image, without document-level
horizontal overflow or JavaScript errors. Screenshots were inspected. The
pre-existing floating theme button can overlap mobile text; no shared
presentation fix is claimed.

All 1,024 existing trait pages were compared structurally: 1,023 have only
footer changes; the phenotype parent's new child link/count is the sole
substantive existing trait-page change. Both exact configured DeepWalk
inputs are absent, so embeddings were not regenerated. No existing trait
YAML or repository history record changed. No audit baseline was expanded.
All 510 PROPOSED records satisfy the citation gate; all 630 local IDs have
proposals. `just qc`, `just validate-history` and `just validate-products`
passed. Full pytest passed: **2,306 tests**, two dependency deprecation
warnings, in 630.73 seconds. Exact-head adversarial review, fresh CI and
native-queue merge remain separate steps, not local-validation claims.

The ordinary whitespace check on the new ROBOT template flags only its
header's required three trailing empty cells. Structured parsing confirms
three 11-column rows. The staged check passes with that exact TSV excluded,
and its exact-path check passes with `core.whitespace=-blank-at-eol`.
No required cells are trimmed or global setting changed.

## Upstream and Round Trip

Submit this cohort for METPO review. After accepted identifiers enter a
release, refresh the ontology, migrate the local ID and references to the
accepted METPO ID, preserve local provenance and append-only history, and
regenerate products without duplicate primary records. Keep the record
PROPOSED until human signoff.

## Change Log

- v506, 2026-10-05: propose karyoklepty with three DOI-backed snippets,
  one qualified natural example and explicit mechanism limits.
