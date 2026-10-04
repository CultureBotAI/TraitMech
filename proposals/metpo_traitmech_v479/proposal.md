# pH Tropism: METPO Proposal v479

## Context

Add `traitmech:000602 pH tropism`, a PROPOSED PHYSIOLOGY class for
external-pH-directed polarized growth. Before this addition the live corpus
contained 996 records. A freshly generated temporary seed contains 399 IDs:
344 already live and 55 absent. Joining the frozen active-review and release
inventories identifies those absences as 38 supporting-field terms and 17
duplicates, not an automatic addition queue.

Whole-repository novelty searches included ignored and hidden files, likely
labels/slugs, alternative phrasings, primary citations, research, proposals
and history. The broad search finds chemotropism's existing pH experiment
and unrelated pH homeostasis/growth-limit material, but no exact record.
Structured inspection of the 12,617-triple pinned ontology found no exact
pH-tropism term. Upstream all-state issue searches found no matching proposal;
open TraitMech PRs do not add this candidate. No same-scope synonym or exact
ungrounded causal node needs migration.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This is a qualitative directional-growth phenotype, not a pH-tolerance bin,
chemical-use pair, sequence feature, kinase or molecular pathway. Its cue
distinguishes it from the broader chemotropism record. Sharing one paper with
that parent does not make the definitions equivalent.

## Hierarchy And Boundaries

The local parent is `traitmech:000597 chemotropism`; external pH is the
chemical-gradient cue that narrows the parent. Its v474 proposal reserves
`METPO:1055100`, which is not released. The standalone v479 proposal instead
uses released `METPO:1000059 phenotype`, under `METPO:1000188 quality`.
The phenotype genus matches that parent. No pending-parent stub is created;
reconcile the narrower hierarchy after v474 acceptance. Use w3id METPO IRIs,
not the legacy OBO-prefix namespace.

The class is polarity-neutral without requiring both directions in one
organism or treating an engineered reversal as a natural exemplar. Keep
locomotory pH taxis, pH optimum, tolerance and growth rate distinct. No
acidotropism synonym, external equivalent, canonical strain or molecular
graph is asserted without verification. Two OPEN discussions retain source
limitations, identity questions and the incomplete spatial-sensing mechanism.
No older trait YAML, including protected spore_germination, is changed.

## Evidence And Access

- [Fernandes et al. (2023)](https://doi.org/10.1128/mbio.00285-23),
  PMID:36861989 / PMC10128062, directly read definition authority.
  Results, Methods and Discussion were inspected in raw Europe PMC JATS;
  Figure 1B and Table S1 were inspected visually from the repository's
  supplementary-files package. The record distinguishes germ-tube
  direction, mutant reversal, invasion and uniform-pH-shift assays.
- [Yamamoto et al. (2024)](https://doi.org/10.1371/journal.pbio.3002726),
  PMID:39078817 / PMC11288418, an independent pH-interface experiment.
  Raw JATS was inspected, together with publisher Figure 3 and the strain
  table. The record retains the single-experiment limitation, growth
  inhibition, summary/Results discrepancy and engineered backgrounds.

Both snippets exact-match contiguous full-text spans, including punctuation,
and are fewer than 25 words each. They are not copied from search summaries.
The source-specific qualifications and collection-label discrepancy are in
the record rather than silently reconciled. Full PDFs were not available
from ASM; its repository JATS and figure/supplement package were accessible.
Movies and remaining supplements were not inspected. No baseline exceptions
or citation-gate changes are part of this proposal.

## ID Space And Files

Reserve `METPO:1055600` in the fresh 1055600-1055699 block following v478,
disjoint from the CommunityMech reference cohort. Ignored-and-hidden
collision searches found no reservation of this block, v479 or local
`traitmech:000602` before writing. The local identity remains temporary;
the reserved METPO CURIE is not a released identifier.
Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

Properties and SSSOM files are omitted because no new relation or verified
external equivalence is asserted. The two 11-column headers follow the live
upstream contract, including its trailing empty directive cells.

## Verification

The writer defaults to dry run, validates before either output and refuses
record or proposal drift. Tests cover definition/source qualifications,
record/proposal parity, replay, dry run, independent drift refusal and
closed-schema rejection without partial writes.

Corpus QC, LinkML/strict validation, history/product checks, proposal coverage,
ROBOT/ELK, canonical-example shape checks, grounding/Biolink audits and lint
pass. All 52 focused trait/README/priority/QC artifact tests pass. Structured
emitted-OWL inspection confirms the released w3id parent chain and absence of
a pending chemotropism stub. The abstract-only snippet resolver returns
NOT_IN_ABSTRACT for both full-text quotes; direct raw-JATS matching verifies
the spans separately. Record the full-suite result and exact reviewed heads
in the PR.

Maintained recipes regenerated pages, discussions and priority/QC dashboards.
The reviewed shared generator matches its pinned archive; the regenerated
coverage chart is byte-identical. Exactly 995 older non-parent trait pages
have footer-only changes, while chemotropism also gains its new child link.
Playwright checks at 1440px and 390px pass, and screenshots were inspected.
The exact primary and fallback embedding inputs are absent, so embeddings
were not regenerated. Plain staged whitespace checking flags only the three
upstream-required empty TSV header cells; all other paths pass and structured
TSV parsing confirms exact upstream header parity.

## Upstream And Round Trip

Submit the validated TSV through berkeleybop/metpo or the KG-Microbe proposal
pipeline after review. On upstream acceptance, refresh the pinned ontology,
seed to a temporary tree, migrate the local identity while preserving its
traceability, and reconcile parent references and proposal status in a
reviewed change. No upstream issue substitutes for these artifacts. Human
signoff is required before promoting the record from PROPOSED.

## Change Log

- v479, 2026-10-04: add pH-directed polarized growth with two directly read
  primary sources, inspected directional figures, explicit source limitations
  and deferred strain/mechanism enrichment.
