# Energy Taxis: METPO proposal v467

## Context

TraitMech mints `traitmech:000590 energy taxis` as a PROPOSED organismal
disposition. It captures energy-linked sensing that regulates locomotion,
not merely metabolic power for movement or possession of a receptor.
Two primary DOI studies support this phenotype; a culture-collection URL
independently supports the canonical strain's environmental provenance.

The fresh temporary seed has 399 identifiers, 344 present and 55 absent in
the pre-change 984-record corpus. Structured review of both frozen release
tables and the live OWL found no exact energy-taxis class. Whole-repository
novelty searches included ignored and hidden files, lexical variants,
metabolism-dependent-taxis phrases, both DOI/PMID pairs, the ATCC URL and
new identifier reservations. Only the chemotaxis research report and its
rendered copy identify this as a separate trait; no exact graph node or
synonym needs reconciliation. The upstream METPO issue search returned
no energy-taxis result.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new identity. No predicate or enum requires lifting.

## Hierarchy Decisions

The active parent `METPO:1000702 motile` denotes independently powered
locomotion. Energy taxis adds electron-transport-linked sensing; power
supply alone is insufficient. No closer active METPO parent was found.
The local chemotaxis definition imposes flagellar motor switching and is
not used to impose that apparatus universally.

Aerotaxis and phototaxis are stimulus-defined and can use other sensing
mechanisms, so neither entire class is reparented here. Metabolism-dependent
chemotaxis can involve intracellular-intermediate sensing instead of the
electron-transport-based mechanism, and is not an exact synonym. No
external equivalent xref or SSSOM mapping is asserted without authority
resolution and organismal-disposition scope comparison.

## Evidence

- Alexandre et al., DOI:10.1128/jb.182.21.6042-6048.2000, PMID:11029423:
  publisher Methods, Results and Discussion inspected; abstract snippet
  exact-matched at Europe PMC. The reference Sp7 and cytN mutant are kept
  distinct. The study supports electron-transport-linked responses but
  does not decide the sensed redox-state versus ion-motive-force parameter.
- Greer-Phillips et al., DOI:10.1128/jb.186.19.6595-6604.2004,
  PMID:15375141: abstract supplies the explicit energy-taxis definition and
  transducer-mutant evidence. Full text was not fully inspected; no complete
  molecular pathway or universal host-specificity claim is inferred.
- https://www.atcc.org/products/29145: ATCC identifies the type strain,
  environmental origin and Sp. 7 custody. This provenance-only URL is kept
  in the qualified canonical example note, not counted as trait evidence.
  Review issue #1660 removed the flattened collection-field snippet.
  NCBI resolves `NCBITaxon:192` to `Azospirillum brasilense` at species rank;
  the exemplar is explicitly Sp7-qualified, not an exact strain accession.

The record remains PROPOSED pending human curation. Unverified protein
accessions, sensed-signal identity and external mappings remain open
discussions rather than graph assertions.

## ID Space And Subset

Reserve `METPO:1054400` in block 1054400-1054499, following v466's block
1054300-1054399. Ignored-and-hidden searches found no collision. The live
CommunityMech v1 cohort has 96 classes through 1008013 and 19 properties
through 2008002, disjoint from this block. Subset:
`metpo_traitmech_2026_10`. The proposed ID is not an accepted identity;
the record continues to use `traitmech:000590`.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

LinkML, strict record validation, the cohort verifier and cross-cohort
coverage pass. Full `just qc`, history and product validation pass, as do
the initial writer, namespace and artifact/priority tests. Initial head CI
passed all 1,925 tests; review-fix validation is recorded separately in the PR.
Europe PMC verifies both retained abstract snippets. Live NCBI resolution reports no errors and
24 pre-existing label-drift warnings elsewhere in the corpus.

Adversarial review found shared validator defect #1658: the legacy METPO
prefix created a detached parent stub despite ELK success. The helper and
skill commands now use `https://w3id.org/metpo/`. Regenerated v467 OWL passes
ROBOT/ELK; structured RDF inspection confirms the proposed class points to
the labeled `motile` parent and its real hierarchy, without a legacy stub.
An existing properties-only v2 cohort also passes with the corrected helper.
This does not revalidate every historical proposal's generated OWL.
Review issue #1661 removes 45 tracked legacy-prefix OWL outputs while
retaining local copies under the existing ignore rule, with a regression
guard against tracking new generated outputs.

The canonical 11-column class template retains its three trailing empty
ROBOT directive cells. Desktop (1440px) and mobile (390px) browser checks
initially confirmed the qualified example, correct local-identifier
provenance, 985-record QC counts and no overflow or page errors. All 984
existing trait-page deltas are footer counts/coverage, plus the expected
new child link on `motile`. Both configured embedding source paths are
absent; embedding artifacts were not regenerated.

Post-review desktop and mobile checks verify two primary evidence items and
the ATCC URL only in the example note. Both snippets reverify at Europe PMC,
and all 17 focused writer/namespace/artifact-policy tests pass. Complete
review-fix validation results are attached to the updated PR.

## Upstream Path

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. Do not export the placeholder as an accepted METPO ID.

## Round-Trip Plan

After upstream acceptance, refresh the pinned ontology and seed a temporary
tree. Migrate to the actual accepted CURIE, preserve the local identifier
in traceability metadata, and reconcile references and proposal status in
a separately reviewed change.

## Change Log

- v467, 2026-10-04: one evidence-backed energy-taxis class, curated by codex.
