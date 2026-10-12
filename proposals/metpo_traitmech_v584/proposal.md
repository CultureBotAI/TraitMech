# Diversifying Bet Hedging (v584)

## Context And Scope

This cohort proposes an ontology home for `traitmech:000708`,
`data/traits/physiology/diversifying_bet_hedging.yaml`. It denotes a
lineage-level physiological disposition, not an individual observation,
sequence feature, gene, or mixed-species community property. The model-assisted
record remains `PROPOSED`, pending human scientific sign-off.

| Scope | Records | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: accepted local trait | 1 | `METPO:1000059` phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

No exact synonym, canonical taxon, molecular graph, negative companion, xref or
SSSOM equivalence is asserted. Only the diversification sense is proposed.

## Evidence And Boundaries

[Levy, Ziv and Siegal 2012](https://doi.org/10.1371/journal.pbio.1001325)
(PMID:22589700, PMC3348152), especially Box 1, supplies the operational
definition framework and its important distinction from demonstrated adaptive
origin. [Beaumont et al. 2009](https://doi.org/10.1038/nature08504)
(PMID:19890329) supplies experimental bacterial evolution evidence;
[Tang et al. 2024](https://doi.org/10.1038/s41467-024-46297-6)
(PMID:38453919) supplies a separate microalgal context with growth/survival
trade-offs. The three short snippets were checked against directly retrieved
scientific abstracts, not search-result summaries or editorial digests.

The definition concerns reversible diversification before the relevant
environmental shift, with condition-dependent performance trade-offs. It does
not classify all heterogeneity or phenotypic switching as bet hedging, require
only two states or a purely stochastic mechanism, or assert evolutionary
optimization in every cited experiment. Fitness-proxy measurements are not a
substitute for measuring long-term geometric mean fitness against a stated
comparison strategy. Figures, supplements and raw data were not independently
assessed; molecular mechanisms and natural canonical exemplars remain deferred.

Source-qualified MED, Crossref and visible publisher notice links were checked.
Commentary, reviews and an earlier preprint are not counted as additional
experiments. No correction or retraction was exposed by those bounded checks;
they do not establish universal notice absence.

## Hierarchy Decisions

Use `METPO:1000059` phenotype, an active class under `METPO:1000188` quality
in both pinned and current released RDF. Its actual IRI uses
`https://w3id.org/metpo/`, not a legacy OBO stub. A more specific parent for the
lineage-level disposition remains an upstream curator decision.

Dormancy and persister formation can contribute to risk spreading, but neither
necessarily establishes the cross-condition strategy, so existing records
are not reparented. Carbon-source memory, cue-triggered environmental
anticipation and generalist/specialist niche breadth are not exact equivalents;
particular observations can overlap. No organism-level disjointness is inferred.

## Novelty And Reservation

The 2026-10-12 allocation check covered main
`e9709d15a82f5d6715e74fd7fdc3665e4fc4c278`, all 22 registered TraitMech
worktrees, 583 proposal cohorts and 4,094 narrative reservation intervals,
plus 530 proposal files in 127 registered CommunityMech worktrees. Whole-root
lexical/citation searches included ignored and hidden files: records, research,
history, proposals, raw ontology and generated products. They did not unpack
archives, follow symlink directories or claim unregistered/private work.

Earlier mentions in research reports are leads, not an existing exact primary
record. Memory and anticipation discussions explicitly distinguish this concept;
the conidiation citation's generic heterogeneity wording is not an equivalent.
No accepted record has an exact unresolved graph node or synonym requiring a
same-branch repair. The protected spore-germination record is unchanged.

A fresh 399-record seed projection was reconciled by exact ID with the
1,102-record live baseline: 344 IDs overlap and 55 absent IDs remain leads,
not automatically acceptable additions. The frozen 1,546-row release-delta
and 153-row active-review tables were rechecked as historical decisions.
No exact active or deprecated candidate was found in pinned/current released
METPO RDF or current templates. The imports-only editable root was not used
alone to establish absence; no pinned ontology refresh is included.

Fresh paginated changed-file lists and immutable relevant blobs covered
TraitMech PRs #1782, #1476, #973 and draft #924 (all 692 files, seven pages);
CommunityMech draft #935; and METPO PRs #644, #643, #641, #640, #638 and #629.
Complete pending ontology/template blobs and all 644 METPO issue/PR bodies
plus 654 comments were checked. No competing candidate or reservation was
found; open sets and heads were stable through acquisition.

Current upstream heads were freshly checked, then existing immutable source
snapshots verified by Git blob SHA and SHA-256 before reuse:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `80049bcc9195480a58633236169b62f86c23489a`.
- KG-Microbe: `bac582f4e131a7ba96b585996ae1fa759403f0b6` (`master`).

Recheck main, registered roots and pending heads immediately before publication.
These bounded checks do not eliminate concurrent-allocation races or establish
global microbial-trait discovery exhaustion.

## ID Space And Subset

- Local ID: `traitmech:000708`.
- Cohort: `metpo_traitmech_v584`.
- Reserve the full `METPO:1066100`-`METPO:1066199` block.
- Populate only `METPO:1066100`, an unreleased proposal placeholder.
- Subset: `metpo_traitmech_2026_10`, following adjacent monthly-tag convention.
- No historical block is reused; this block is separate from CommunityMech v1
  `1007100`-`1007220` and all inspected later reservations.

## Files And Verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two canonical headers, one class row, 11 columns |
| `proposal.md` | Evidence, scope, reservation and round-trip rationale |

Property and SSSOM files are inapplicable. The guarded writer is
`scripts/add_diversifying_bet_hedging_trait.py`; it validates before writing
and refuses parent, target or proposal drift. Headers match the checked
upstream class template; citation fields do not assert equivalence.

```bash
just verify-proposal metpo_traitmech_v584
just robot-validate-proposal metpo_traitmech_v584
just qc
just validate-history
just validate-products
```

The saved structured review and PR report actual outcomes and limitations.
Inspect RDF identity/hierarchy as well as ROBOT exits. Only required trailing
TSV header cells receive the documented, exact-path `-blank-at-eol` whitespace
exception after template-width verification. No frozen baseline is weakened.

## Upstream Path And Round Trip

After review, submit the template and rationale to `berkeleybop/metpo` or the
KG-Microbe proposal pipeline. Curator `codex`, the LLM-assisted curation event
and append-only repository history preserve authorship. Upstream maintainers
choose the final identifier and hierarchy.

After an explicitly reviewed ontology update includes the accepted term,
re-seed that release and migrate this identifier and dependent references,
preserving `traitmech:000708` as a traceable identifier alias and retaining
history. Do not emit the placeholder as a released METPO identity or silently
replace the pinned ontology.

## Change Log

- v584, 2026-10-12: propose one qualified diversification phenotype with three
  primary citations, directly checked snippets and explicit evidence limits.
