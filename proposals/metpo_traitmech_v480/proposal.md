# Negative Autotropism: METPO Proposal v480

## Context

Add `traitmech:000603 negative autotropism`, a PROPOSED PHYSIOLOGY class
for directional growth away from conspecific neighbors. The pre-addition
corpus has 997 records. A fresh temporary METPO seed contains 399 IDs,
344 live and 55 absent; the frozen review inventories classify those
absences as 38 supporting-field terms and 17 duplicates, not new traits.

Whole-repository novelty searches included ignored and hidden files,
labels, slugs, alternate self-avoidance/repulsion descriptions, citations,
research, proposals, history and causal nodes. Germ-tube orientation matches
in aerotropism concern an oxygen cue, not the same phenotype. Structured
inspection of the 12,617-triple pinned ontology found no exact term.
All-state upstream issue search found no matching proposal. No same-scope
synonym, unresolved node or parent-gap discussion requires migration.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This is a reusable directional-growth phenotype, not a sequence feature,
organism-specific observation, chemical-use pair or molecular pathway.
The qualified negative label excludes attraction; it is not an assay-negative
wrapper around an existing autotropism record.

## Hierarchy And Boundaries

Both the record and proposal use released `METPO:1000059 phenotype`, under
`METPO:1000188 quality`. Use the pinned ontology's w3id namespace, not the
legacy OBO-prefix stub. A chemical or oxygen-dependent mechanism is not
established merely by naming the response, so neither chemotropism nor
aerotropism is asserted as a parent.

The definition covers initial germ-tube orientation and later hyphal
redirection without requiring both stages in one organism. Same-species
neighbors may belong to one mycelium or separate spores; this does not imply
genetic identity or vegetative incompatibility. Whole-cell locomotion,
passive bending, branching, growth inhibition and cytoplasm retreat alone
do not establish the defined orientation. Positive autotropism and hyphal
fusion are not exact synonyms. The 2025 source uses the label more broadly
for head-on arrest/retreat; those observations are explicitly excluded as
standalone evidence for this directional-growth class.

No external equivalent, canonical strain or protein mechanism is asserted
without verification. Two OPEN discussions retain scope and enrichment
questions. No existing trait, including protected spore_germination, changes.

## Evidence And Access

- [Montiel-Rubies et al. (2025)](https://doi.org/10.3390/biomimetics10050287),
  PMID:40422117 / PMC12109565, supplies the directly read directional-growth
  definition authority. The Methods, Sections 3.2/3.4.1 and source tables
  were read in Europe PMC JATS. Figure 5 and Table 2 were visually inspected
  in the [authors' PDF](https://bionanoinfo.com/wp-content/uploads/2025/07/Montiel-Rubies-et-al-2025.pdf).
  The paper retrospectively analyzes earlier experiments, not an independent
  replication of each cited dataset. Notes distinguish directional growth
  from head-on retreat, alternative directional-memory explanations, and
  qualitative mode-specific descriptions from quantitative replication.
- [Robinson, Park and Graham (1968)](https://doi.org/10.1093/jxb/19.1.125)
  supplies a distinct spore-pair experiment. Its original abstract was
  retrieved directly from the publisher's
  [article endpoint](https://oup.silverchair-cdn.com/article-minimal/447341),
  not copied from a search index. Three species show negative responses;
  Botrytis cinerea is neutral on agar and positive on Cellophane and is not
  treated as a negative exemplar. The record distinguishes emergence
  orientation from timing, cis-ness and later tip bending. Full text,
  strain provenance, figures and sample sizes remain unverified.

The 14-word and 20-word snippets exactly match contiguous spans in freshly
retrieved source text. The 2025 supplementary movies were not inspected.
Unretrieved historical citations are research leads, not counted evidence.
No snippet-baseline exceptions or relaxed two-citation gate are proposed.

## ID Space And Files

Reserve `METPO:1055700` in the fresh 1055700-1055799 block following v479,
disjoint from CommunityMech v1. Ignored-and-hidden collision searches found
no reservation of that block, v480 or `traitmech:000603` before writing.
The proposed METPO identifier is not a released identity; the local record
retains its temporary TraitMech CURIE. Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

No properties or SSSOM file is needed because there is no new relation or
verified external mapping. Headers follow the upstream 11-column contract,
including its three trailing empty directive cells.

## Verification

The guarded writer defaults to dry run, validates before either output,
and refuses record/proposal drift. Tests cover scope, evidence limitations,
record/proposal parity, replay, dry run, independent drift refusal and
closed-schema rejection without partial writes. Record the executed corpus,
history, proposal/ROBOT, snippet, rendered-page and test results in the PR;
an unexecuted command is not a passing check.

Single-record LinkML/strict validation and proposal verification pass with
zero failures. ROBOT template/merge/ELK passes; structured emitted-OWL
inspection confirms the released w3id phenotype-to-quality parent chain and
no legacy METPO stubs. Both header rows exactly match the retrieved upstream
template. The abstract-only resolver reports NOT_IN_ABSTRACT for the 2025
full-text quote and UNRESOLVED for the 1968 citation; independent direct-source
matching verifies both spans without relabeling those machine outcomes.

Local adversarial review filed #1684 for an unsupported engineered qualifier
on ro-1. The record now leaves its origin unresolved, with a second curation
event and append-only correction history. The add-trait skill and guidance
test also explicitly distinguish mutation from strain origin. All 52 focused
trait/README/priority/QC tests pass; all 16 post-correction trait/skill/QC
checks pass. Maintained recipes regenerated pages, discussions and both
dashboards. Playwright checks and screenshot inspection at 1440px/390px
confirm local identifier provenance, evidence and correction rendering.
The 996 non-parent older pages have only corpus-count footer changes;
phenotype also gains its new child. Both exact configured embedding inputs
are absent, so embedding artifacts were not regenerated. Raw whitespace
checking flags only the required three empty TSV directive cells; all other
paths pass. Full-suite, final QC and exact-head review results belong in the PR.

## Upstream And Round Trip

Submit the validated TSV through berkeleybop/metpo or the KG-Microbe proposal
pipeline after review. On acceptance, refresh the pinned ontology, seed to
a temporary tree and migrate the local identifier while preserving its
traceability. Reconcile parent references and proposal status in a reviewed
change. Human signoff is required before promotion from PROPOSED.

## Change Log

- v480, 2026-10-04: add negative autotropism with two directly read sources,
  exact snippets, stage-specific scope and explicit provenance limits.
