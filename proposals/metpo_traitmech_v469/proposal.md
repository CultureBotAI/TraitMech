# Osmotaxis: METPO Proposal v469

## Context

TraitMech mints `traitmech:000592 osmotaxis` as a PROPOSED organismal
motility phenotype. It captures active net migration in a spatial osmotic
gradient, not osmotic stress tolerance or a speed change alone.

A fresh temporary seed contains 399 identifiers, 344 present and 55 absent
in the pre-change 986-record corpus. Both frozen release-review tables were
examined alongside live records. Structured OWL search found no exact term.
Whole-repository novelty searches included ignored and hidden files,
osmotaxis/osmotactic variants, osmotic migration/movement phrases, citation
DOIs/PMIDs and identifier reservations. The only broader-phrase match was
osmotic water movement in a salinity research report, not organismal
migration. No exact record, node, synonym or discussion needs reconciliation.
The upstream METPO issue search returned no osmotaxis result.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new identity. No predicate or schema enum is lifted.
This is a reusable gradient-response phenotype, not a chemical-use pair.

## Hierarchy Decisions

The active `METPO:1000702 motile` parent denotes independently powered
locomotion. The child adds net migration responding to external osmotic
conditions. Chemotaxis can coexist with osmotaxis; the existing local
chemotaxis definition imposes bacterial flagellar motor switching and is
not used to impose that apparatus on all microbial examples.

Neither preference for high or low osmolarity, a universal optimum, nor a
particular receptor is required. Osmokinesis can contribute to accumulation
but is not an exact synonym or alone a spatial migration assay. Passive
transport, water efflux, differential growth and tolerance are insufficient.
No equivalent external xref, synonym or SSSOM mapping is asserted without
authority resolution and an organismal-scope comparison.

## Evidence

- Leslie et al., DOI:10.1016/s0014-4894(03)00031-6, PMID:12706748:
  Leishmania mexicana promastigote migration requiring an osmotic gradient
  under the tested conditions. The authors' reinterpretation does not
  abolish solute-specific chemotaxis in other conditions or organisms.
- Barros et al., DOI:10.1016/j.exppara.2005.10.005, PMID:16313904:
  Leishmania amazonensis promastigotes respond to both chemical and osmotic
  stimuli. The proposed receptor and vector-development models are not
  asserted as established universal mechanisms.
- Rosko et al., DOI:10.1073/pnas.1620945114, PMID:28874571:
  Escherichia coli temporal-shock motor/population measurements and a
  discussed connection from speed changes to accumulation. This is not
  presented as direct spatial migration measured by those assays.

All three snippets were read from authoritative Europe PMC abstracts;
full texts and supplements were not systematically inspected. The historical
Adler 1988 publisher excerpt was a discovery lead, not an additional evidence
item or a claim of full-text access. Two OPEN discussions defer external
equivalents, natural strain/life-stage provenance, taxon identity and
protein-resolved mechanisms. No canonical taxon or graph is inferred.
Human curator signoff is still needed to promote the record from PROPOSED.

## ID Space And Subset

Reserve `METPO:1054600` in block 1054600-1054699, following v468's
1054500-1054599 block. Ignored-and-hidden collision searches and OWL
subject inspection found no collision. The CommunityMech v1 ranges are
disjoint. Subset: `metpo_traitmech_2026_10`. The record uses
`traitmech:000592`, not its proposed upstream placeholder.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

LinkML, strict validation, cohort verification, ROBOT/ELK, full QC,
history/product validation, and rendered-page checks passed. The full test
suite passed 1,944 tests with two dependency warnings; 45 artifact/priority
tests and 25 focused writer/verifier tests also passed. Live snippet
verification reports 3/3 VERIFIED after fixing the parenthesized-DOI query
defect tracked in #1663. Desktop and 390px browser checks found no errors or
horizontal overflow, and rendered evidence/provenance was visually inspected.
The canonical class template has 11 columns and three trailing empty ROBOT
directive cells. Emitted RDF uses `https://w3id.org/metpo/1054600` below the
real labeled `motile` parent, with its existing broader hierarchy intact.
No legacy METPO namespace stub is asserted. ROBOT outputs remain ignored.

The add-trait skill gains a general evidence rule distinguishing spatial
migration from uniform-stimulus motility measurements, without demanding
a receptor-based sensing mechanism for every taxis phenotype. It also gains
guidance for diagnosing apparent unindexed references without concealing
query failures by changing citations. Both exact configured embedding
source paths were absent, so embedding artifacts were not regenerated.

## Upstream Path

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. Do not export the placeholder as an accepted METPO ID.

## Round-Trip Plan

After upstream acceptance, refresh the pinned ontology and seed a temporary
tree. Migrate to the accepted CURIE, preserve the local identifier in
traceability metadata, and reconcile references and proposal status in a
separately reviewed change.

## Change Log

- v469, 2026-10-04: one evidence-backed osmotaxis class, curated by codex.
