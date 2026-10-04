# Phototropism: METPO Proposal v475

## Context

TraitMech adds `traitmech:000598 phototropism` as a PROPOSED PHYSIOLOGY
class for light-directed growth, distinct from phototaxis, photokinesis
and phototrophic energy acquisition.

A fresh temporary METPO seed emitted 399 identifiers, 344 present and 55
absent from the pre-change 992-record corpus. Structured comparison with
both frozen release-review tables identified the 55 as 38 supporting-field
terms and 17 reviewed duplicates; all 38 former no-demand classes are now
represented. These absences are not a work queue. The pinned OWL contains
light-related energy-source terms but no exact phototropism class.

Whole-repository novelty searches included ignored and hidden files, labels,
slugs, likely synonyms, source identifiers, research, history and proposals.
The only prior phototropic hits were photosynthesis-literature titles in two
research reports, not directional-growth records. No existing node, synonym
or parent-gap discussion needs changing. An all-state upstream METPO issue
search found no phototropism proposal; open TraitMech PRs did not overlap.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses the local identity. No gene, domain, source column, chemical
use pair, predicate or workflow enum is promoted into a trait.

## Hierarchy And Boundaries

The pinned OWL resolves phenotype to the real `https://w3id.org/metpo/1000059`
class under `METPO:1000188 quality`. Growth orientation does not imply
locomotion, so the parent is not motile. The definition includes both growth
directions without requiring both in every organism or condition.

No unverified synonyms, external xrefs or SSSOM mapping are asserted.
Two OPEN discussions retain mapping and native-mechanism questions. Human
curator signoff is required before promotion from PROPOSED.

## Evidence And Access

- Idnurm et al., DOI:10.1073/pnas.0600633103, PMID:16537433, PMC1450208:
  primary phenotype/definition source. Its abstract supports both directions;
  Figure 1A supports the white-light positive case, not a far-UV experiment.
- Sanz et al., DOI:10.1073/pnas.0900879106, PMID:19380729, PMC2678449:
  supporting positive response and bounded genetic/interaction evidence.
- Shakya and Idnurm, DOI:10.1128/EC.00203-13, PMID:24243797, PMC3910969:
  independent strain provenance, not a separate phototropism experiment.

The first two abstracts were retrieved directly from Europe PMC and exact
snippets matched. Their full PDFs were inspected from institutional copies:
[Idnurm 2006](https://gredos.usal.es/handle/10366/159035) and
[Sanz 2009](https://gredos.usal.es/handle/10366/158987). Figures 1A (2006),
2B and 4 (2009) were visually checked. Sanz supplementary material was not
accessible or inspected. Raw [PMC3910969 HTML](https://pmc.ncbi.nlm.nih.gov/articles/PMC3910969/)
supports the provenance quote. XML endpoints returned HTTP 500; PDF/HTML
checks are not misreported as successful XML retrievals.

Canonical `NCBITaxon:763407` resolves directly at NCBI to
`Phycomyces blakesleeanus NRRL 1555(-)`, rank strain, parent 4837.
The example is limited to the natural NRRL1555 background's sporangiophore
response, excluding mutants and backcrossed A56. No protein accession or
universal mechanism is inferred from heterologous assays. No causal graph
is added to bypass the unresolved mechanistic grounding.

## ID Space And Files

Reserve `METPO:1055200` in the fresh 1055200-1055299 block after v474's
1055100-1055199 block, disjoint from CommunityMech v1. Ignored-and-hidden
collision searches found only an unrelated embedding similarity decimal.
The live identity is `traitmech:000598`; the proposed METPO placeholder
is not presented as a released identifier. Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

Property and SSSOM files are omitted. The 11-column class header follows
the live upstream template, including required trailing directive cells.
The local wrapper's correct w3id prefix supersedes the legacy OBO prefix
still illustrated in the upstream skill.

## Verification

Seven focused writer tests pass: growth/polarity boundaries, qualified
evidence and natural strain, template parity, dry-run/replay, independent
record/proposal drift refusal, and schema rejection without partial writes.
Full QC passes with no new blocking findings and two existing ENIGMA
source-license warnings. Strict validation covers 993 records; history
validation covers 1,030 records. Product, proposal, Biolink and graph-artifact
checks pass. ROBOT/ELK reasoning adds four lines without unsatisfiable
classes; structured RDF inspection confirms the real phenotype parent and
quality ancestor, with no legacy OBO-prefix METPO stubs.

The snippet resolver reports two VERIFIED abstracts and one
NOT_IN_ABSTRACT provenance quote. The latter was exact-matched separately
against raw PMC HTML, not relabeled as abstract verification. The canonical
audit resolves all 707 examples across 522 records: zero errors and 24
pre-existing label warnings, none on the new strain.

The full suite passes all 1,988 tests with two dependency deprecation
warnings; all 45 artifact tests also pass. Desktop 1440px and mobile 390px browser and
screenshot checks pass for the new trait and QC dashboard, including three
evidence entries, the canonical example, local identifier link, loaded
coverage image, and no document overflow or page errors. Among 992 older
trait pages, 991 have only count-footer changes; phenotype additionally
gains the new child and its child count increases from 114 to 115. No older
source YAML changed. Both configured embedding sources are absent, so
embeddings were not regenerated.

The proposal's required three trailing header tabs preserve exact upstream
11-column parity; data rows pass ordinary whitespace checks.

## Upstream And Round Trip

After review, submit the TSV to berkeleybop/metpo or the KG-Microbe proposal
pipeline. After upstream acceptance, refresh the ontology, seed a temporary
tree, migrate to the accepted CURIE, preserve the local identity in
traceability metadata, and reconcile references and proposal status in a
reviewed change. No separate upstream issue was opened in this branch.

## Change Log

- v475, 2026-10-04: add one light-directed growth class with a verified
  natural strain exemplar and explicit limits on mechanism evidence.
  Clarify in the add-trait skill that an unqualified growth tropism must
  consider both response directions rather than generalize a positive case.
