# Kleptoplasty: METPO Proposal v505

## Context

Add `traitmech:000629 kleptoplasty`, a PROPOSED PHYSIOLOGY class for selective
retention of algal prey plastids after other prey components are discarded or
digested. Retaining a whole living algal endosymbiont is not sufficient.
Photosynthetic function, plastid replication and a fixed retention interval
are deliberately not required.

Novelty and allocation searches included ignored and hidden files throughout
TraitMech and CommunityMech proposals. The only exact-label leads were in the
trophic_type research report and its rendered page, not curated records.
Structured review of all 12,617 pinned METPO triples found no exact term.
All-state TraitMech/METPO PR searches found no competing term; open PR heads
were checked against their previously inspected complete file inventories.
The base is merged main `b5ef803b7f9290f8be151ab30e99776ae4a269e0`.

A fresh 399-record seed shares 344 identifiers with the pre-addition
1,023-record corpus. The 55 absent IDs reconcile to 38 supporting-field terms
and 17 reviewed duplicates. The complete 1,546-row release delta and 153-row
active review were checked; all 38 formerly unselected classes are now live.
This is not evidence that literature-based discovery is exhausted.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Use phenotype pending a closer organelle-acquisition hierarchy. Phagocytosis
`traitmech:000627` describes uptake; phagotrophy `traitmech:000628` requires
nutrition. Local phototrophic and mixotrophic definitions impose energy/carbon
use that generic plastid retention does not. The trophic_type Falcon report
attributes a narrower acquired-photosynthesis interpretation to Schenone 2024;
preserve that research attribution without turning it into a universal
definition. This is a physiological trait, not a literal organelle or sequence
feature. No existing trait, exact synonym, xref, SSSOM mapping, protein
accession or causal graph is changed or added.

## Evidence and Example

Four distinct publications have directly read supporting passages:

- `DOI:10.1038/s41598-018-28455-1`: Introduction definition, not experimental
  replication. Scientific Abstract and Introduction read for terminology.
- `DOI:10.1073/pnas.2220100120`: scientific Abstract and main text, actual
  Figures 1 and 3; qualified Rapaza NIES-4477 example. Supplements not visually
  audited; no claims unique to uninspected panels are imported.
- `DOI:10.1038/s41467-026-70516-x`: scientific Abstract, relevant main-text
  sections, actual Figures 3-5 and Supplementary Figure 4; host-protein
  functional evidence, not merely sequence prediction. Protein groundings and
  a complete import mechanism remain deferred.
- `DOI:10.1111/1462-2920.14433`: directly retrieved scientific abstract only,
  supporting photosynthesis-independent terminology under the assayed
  conditions. No full-text, figure or canonical-taxon claim is made.

NCBI independently resolves `NCBITaxon:1112050 Rapaza viridis`. Natural
provenance is supported by the original 2012 Methods, not inferred from later
engineered experiments. The NIES-4477 collection's ATCC alias conflicts with
the primary papers; the record retains the discrepancy instead of silently
merging host and prey identifiers. Provenance-only URLs do not count as
independent trait evidence. All four evidence items have concise verbatim
snippets; resolver results are recorded separately from manual source checks.

## ID Space and Files

Reserve `METPO:1058200` in the fresh 1058200-1058299 hundred block, following
v504's 1058100 block. No collision was found in the full ignored-and-hidden
search or the pinned ontology. The subset is `metpo_traitmech_2026_10`.
The local identifier occurs in one new record. Scopes B/C are intentionally
empty; no mapping file is needed because no equivalence is asserted.

The canonical kg-microbe contract at
`ea1c5f15e6c4dba6c72165367162b354e215f018`, class/property templates,
CommunityMech v1 and TraitMech v504 were inspected. Use current w3id METPO
IRIs, not the legacy prefix in example commands. Citation columns contain
publications and local provenance, not ontology mappings.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer passed dry run and 11 focused tests covering apply/replay,
parent preservation and fail-closed drift refusal. Direct LinkML and strict
record validation passed. The maintained snippet resolver returned three
VERIFIED scientific-abstract spans and one NOT_IN_ABSTRACT Introduction span;
all four exact contiguous passages were independently matched to directly
retrieved source sections. The full-text result is not relabeled VERIFIED.

The live NCBI audit resolved all 721 examples across 536 records with zero
errors and 24 existing warnings, none for the new example. An initial audit
invocation supplied an unsupported output argument and exited before auditing;
the corrected supported invocation passed. Proposal verification, cross-cohort
coverage and ROBOT ELK reasoning passed, with no unsatisfiable class. Direct
RDF inspection confirms the new definition and labeled phenotype-to-quality
hierarchy under w3id IRIs, with no legacy METPO stub. The merged graph contains
12,628 triples in 23,322 physical lines; the reasoned graph contains 12,632
triples in 23,326 lines. The inspection initially expected an untyped literal;
using ROBOT's actual xsd:string datatype confirmed the unchanged definition.

Maintained generators refreshed the discussion browser, QC dashboard, priority
dashboard and trait pages. Playwright checks passed at 1440- and 390-pixel
widths: local identifier provenance, four citations and quotes, one qualified
example, reciprocal parent navigation, 1,024-record dashboard and loaded
coverage image, without document-level horizontal overflow or JavaScript
errors. Screenshots were inspected. The pre-existing floating theme button
can overlap mobile text; no shared presentation fix is claimed.

All 1,023 existing trait pages were compared structurally: 1,022 have only
footer changes; the phenotype parent's new child link/count is the sole
substantive existing trait-page change. Both exact configured DeepWalk inputs
are absent, so embeddings were not regenerated. No existing trait YAML or
repository history record changed. No audit baseline was expanded. All 509
PROPOSED records satisfy the citation gate; all 629 local IDs have proposals.

`just qc`, `just validate-history` and `just validate-products` passed.
Full pytest passed: **2,295 tests**, two dependency deprecation warnings, in
609.98 seconds. Exact-head adversarial review, fresh CI and native-queue merge
remain separate required steps, not claims established by local validation.

The ordinary staged whitespace check flags only the ROBOT header's required
three trailing empty cells. Structured parsing confirms three 11-column rows.
The staged check passes with that exact TSV excluded, and the exact-path check
passes with `core.whitespace=-blank-at-eol`; no global setting is changed.

## Upstream and Round Trip

Submit this cohort for METPO review. After accepted identifiers enter a
release, refresh the ontology, migrate the local ID and references to the
accepted METPO ID, preserve local provenance and append-only history, and
regenerate products without duplicate primary records. Keep the local record
PROPOSED until human signoff.

## Change Log

- v505, 2026-10-05: propose kleptoplasty with four DOI-backed evidence snippets,
  one qualified natural example and explicit functional/identity limits.
