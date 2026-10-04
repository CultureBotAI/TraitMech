# Thigmotropism: METPO Proposal v471

## Context

TraitMech mints `traitmech:000594 thigmotropism` as a PROPOSED PHYSIOLOGY
class for contact-directed reorientation of polarized growth. Four primary
fungal studies support the trait independently of a locomotor apparatus.

A fresh seed contained 399 identifiers, 344 present and 55 absent in the
pre-change 988-record corpus. Both frozen METPO release-review tables and
the active-review narrative were checked against live records. Structured
OWL search found no exact thigmotropism or growth-tropism class. Whole-repo
novelty and collision searches included ignored and hidden files, label
variants, citations, local identifiers and the complete placeholder block.
No pre-existing exact record, node, synonym or discussion required repair.
The existing mycelial-growth record is explicitly bacterial; filament shape
does not establish a contact response. The upstream METPO issue search
returned no thigmotropism entry.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the new identity. No predicate or schema enum is lifted.

## Hierarchy Decisions

Use the verified `phenotype` parent. Directional extension of a growing
hyphal tip is not whole-cell locomotion, so `motile` would add an unsupported
entailment. The trait also differs from simple filament shape, stiffness-
gradient migration, passive bending, generic adhesion and contact-induced
differentiation. No narrower exact parent was identified in the pinned OWL.
No exact synonym or external equivalent is asserted without a scope and
authority check. The evidence does not establish a universal mechanosensor
or make in vitro contact responses proof of host invasion.

## Evidence

- Sherwood et al., DOI:10.1080/02681219280000621, PMID:1287165:
  pore-entry observations support the authors' contact-guidance
  interpretation, including growth away from the nutrient agar.
- Watts et al., DOI:10.1099/00221287-144-3-689, PMID:9534238:
  low-concentration inhibitor effects separate reorientation from extension
  rate, but do not uniquely identify the molecular contact sensor.
- Brand et al., DOI:10.1016/j.cub.2006.12.043, PMID:17275302,
  PMCID:PMC1885950: channel-component perturbations support a calcium-related
  contribution. Full text distinguishes the contact response from cathodal
  emergence; calcineurin dependence must not be transferred between them.
  Localized channel activation and influx remain a proposed explanation.
- Thomson et al., DOI:10.1111/cmi.12369, PMID:25262778,
  PMCID:PMC4371639: full text, Fig. 6 and supplementary Table S1 were
  inspected. Mechanical constraint distinguishes tip reorientation from
  subapical bending. The strain table lists engineered backgrounds and
  reporters, not a demonstrated natural-strain exemplar. Main-text and
  supplement force units disagree, so no force magnitude is curated.

All four evidence items have contiguous abstract snippets. The first two
sources were abstract-only checks; the Brand supplement and Thomson movies
were not inspected. No canonical taxon ID, protein accession or causal graph
is inferred. Two OPEN discussions retain growth/contact boundaries and
natural-strain/accession-level mechanism gaps. Model approval does not
promote the record from PROPOSED without human curation.

## ID Space And Subset

Reserve `METPO:1054800` in block 1054800-1054899, following v470's
1054700-1054799 block. Ignored-and-hidden collision searches found the block
unoccupied; CommunityMech v1 ranges are disjoint. Subset:
`metpo_traitmech_2026_10`. The live record uses `traitmech:000594`, not the
proposed upstream placeholder.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

Direct LinkML/strict validation, cohort and coverage verification, ROBOT/ELK,
full QC/history/products, artifact freshness and desktop/mobile checks passed.
All four snippets report VERIFIED in the live resolver and are exact raw
abstract substrings. Full pytest passed 1,958 tests with two dependency
warnings in 926.24s; seven writer tests and 45 artifact/priority tests also
passed. History validates 1,025 records. Both merged and reasoned RDF retain
the labeled phenotype-to-quality hierarchy, with no legacy namespace stub.
The canonical upstream class header matches exactly: 11 columns and three
trailing empty ROBOT directive cells.

Desktop 1440px/mobile 390px checks found no page errors or document overflow;
screenshots were visually inspected. All 988 existing pages were checked:
987 footer-only changes plus the phenotype child link. Both exact configured
embedding source paths were absent, so embedding artifacts were not rebuilt.

The add-trait skill gains a narrow growth-tropism boundary rule: do not
inherit motility solely from neighboring taxis records, and distinguish
directional growth from passive bending or contact-induced differentiation.

## Upstream Path

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. Do not export the placeholder as an accepted METPO ID.

## Round-Trip Plan

After upstream acceptance, refresh the ontology and seed a temporary tree.
Migrate to the accepted CURIE, preserve the local identifier in traceability
metadata, and reconcile references and proposal status in a reviewed change.

## Change Log

- v471, 2026-10-04: one evidence-backed thigmotropism class, curated by codex.
