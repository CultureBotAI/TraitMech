# Viscotaxis: METPO Proposal v470

## Context

TraitMech mints `traitmech:000593 viscotaxis` as a PROPOSED PHYSIOLOGY
class. The phenotype is net migration of an actively moving organism in
response to a spatial gradient in surrounding fluid viscosity, not merely
faster or slower swimming in a uniform medium.

A fresh seed contained 399 identifiers, 344 present and 55 absent in the
pre-change 987-record corpus. Both frozen METPO release-review tables and
the active-review narrative were checked against live records. Structured
OWL search found no viscosity or viscotaxis term. Whole-repository novelty
and collision searches included ignored and hidden files, labels, variants,
citations, local IDs and the complete reserved block. Two broader-phrase
hits were the same research mention and rendered copy about VidA/VidB and
viscosity-dependent swimming velocity, not an exact migration trait. No
record, node, synonym or discussion needs same-scope reconciliation.
Extended viscophobic/viscophilic and viscous-gradient searches only matched
the existing gyrotaxis gravity-viscous torque balance, a distinct phenotype.
The upstream METPO issue search returned no viscotaxis result.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new identity. No predicate or schema enum is lifted.
This is a reusable migration phenotype, not a chemical-use pair.

## Hierarchy Decisions

The verified `motile` parent denotes independently powered locomotion.
Viscotaxis adds a fluid-viscosity spatial cue, without requiring a universal
preferred direction, viscosity, receptor or locomotor apparatus. It is
distinct from osmotic-gradient migration and flow-directed rheotaxis.
Substrate stiffness and matrix loss-modulus migration are not silently
included in this fluid-viscosity definition. Coupled chemical, osmotic,
light or flow cues require source-specific controls.

No exact synonym or external equivalent is asserted without an authority
and organismal-scope check. Hydrodynamic turning of an active swimmer is
compatible with this trait; passive advection or uniform-viscosity speed
changes alone are not sufficient evidence of gradient-directed migration.

## Evidence

- Petrino and Doetsch, DOI:10.1099/00221287-109-1-113, PMID:731206:
  the primary abstract names positive viscosity-gradient migration in the
  historically designated Leptospira interrogans (biflexa) strain B16.
  Modern species/strain identity and pathogenicity are not inferred.
- Coppola and Kantsler, DOI:10.1038/s41598-020-79887-7, PMID:33432106,
  PMCID:PMC7801662: conditional accumulation of Chlamydomonas reinhardtii
  in lower-viscosity regions, with uniform profiles under other conditions.
  Full text, Fig. 5 and supplementary Figs. S1-S3 were inspected. Wild-type
  and short-flagella observations are kept separate; pump stoppage and
  optical filtering address flow and phototactic confounding. A confined
  sharp interface does not directly validate an unconfined slow-gradient
  model. No strain accession is inferred.
- Liebchen et al., DOI:10.1103/physrevlett.120.208002, PMID:29864289:
  theoretical shape-dependent asymmetry of viscous forces in slowly varying
  fields, not a new biological migration assay, verified receptor, or
  experimentally established function of microbial shape changes.

All three evidence items have exact Europe PMC abstract snippets. Only the
Coppola full text and supplement were inspected; no full-text access is
claimed for the other two studies. Two OPEN discussions preserve scope,
canonical strain/taxon provenance, external mapping and molecular mechanism
gaps. No canonical example, protein accession or causal graph is invented.
Human curator signoff remains necessary to promote the record from PROPOSED.

## ID Space And Subset

Reserve `METPO:1054700` in block 1054700-1054799, following v469's
1054600-1054699 block. Ignored-and-hidden reservation searches and structured
OWL subject checks found no collision; CommunityMech v1 ranges are disjoint.
Subset: `metpo_traitmech_2026_10`. The live record uses `traitmech:000593`,
not the proposed upstream placeholder.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

Direct LinkML/strict validation, proposal and coverage checks, ROBOT/ELK,
full QC/history/products, artifact freshness and desktop/mobile page checks
passed. All three snippets report VERIFIED in the live resolver. The full
suite passed 1,951 tests with two dependency warnings; seven writer tests
and 45 artifact/priority tests also passed. Both merged and reasoned RDF
retain the real labeled `motile` parent and its existing broader hierarchy.
Desktop 1440px and mobile 390px checks found no browser errors or document
overflow; screenshots were visually inspected. Both exact configured
embedding source paths were absent, so embedding artifacts were not rebuilt.
The canonical upstream class header was freshly retrieved: 11 columns and
three trailing empty ROBOT directive cells. METPO IRIs must use the pinned
ontology's `https://w3id.org/metpo/` namespace rather than legacy stubs.

The current add-trait guidance already distinguishes spatial migration from
uniform-stimulus motility and model predictions; no further skill change is
needed for this evidence bundle.

## Upstream Path

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. Do not export the placeholder as an accepted METPO ID.

## Round-Trip Plan

After upstream acceptance, refresh the pinned ontology and seed a temporary
tree. Migrate to the accepted CURIE, preserve the local identifier in
traceability metadata, and reconcile references and proposal status in a
separately reviewed change.

## Change Log

- v470, 2026-10-04: one evidence-backed viscotaxis class, curated by codex.
