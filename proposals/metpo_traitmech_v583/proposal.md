# Cue-Triggered Environmental Anticipation (v583)

## Context And Scope

This cohort proposes an ontology home for `traitmech:000707` at
`data/traits/physiology/cue_triggered_environmental_anticipation.yaml`.
It is a conditional organismal phenotype, not a regulatory sequence feature,
pathway, individual observation or precomposed chemical-use assertion.
The record remains `PROPOSED`; model-assisted review is not human sign-off.

| Scope | Records | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: accepted local trait | 1 | `METPO:1000059` phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

No negative companion, source-specific cue pair, universal molecular mechanism,
canonical example, exact synonym, xref or SSSOM equivalence is proposed.

## Evidence And Boundaries

The definition is supported by [Mitchell et al. 2009](https://doi.org/10.1038/nature08112)
(PMID:19536156). [Eoh et al. 2017](https://doi.org/10.1038/nmicrobiol.2017.84)
(PMID:28530656, PMC5540153) supplies a distinct primary metabolic context.
The YAML retains short scientific-abstract snippets, source locators and
explicit evidence limits. Both snippets match the directly retrieved publisher
abstracts and source-qualified MED records. Notice checks covered MED,
Crossref and visible publisher links, not every possible notice repository.

The cue-triggered qualifier distinguishes this proposed scope from broader
uses of anticipation. Existing carbon-source memory, stress response,
nutrient adaptation and diauxic growth are not exact equivalents. Overlap in
particular assays is not asserted to be disjointness. The two OPEN discussions
retain the hierarchy, terminology, provenance and mechanism questions.

The separate [Tagkopoulos 2008 lead](https://doi.org/10.1126/science.1154456)
is not counted toward the evidence gate: its main PMC text was accessible but
the indexed corrected supplement could not be directly inspected. Neither
secondary commentary nor another publication of the same study is counted as
independent experimental support.

## Hierarchy Decisions

Use `METPO:1000059` phenotype. The pinned and current released RDF subjects
are active classes under `METPO:1000188` quality. Use the actual
`https://w3id.org/metpo/` namespace, not a legacy OBO stub.

`METPO:1000731` nutrient adaptation is a trophic-type class with local
source-attributed chronic copiotroph/oligotroph framing; that is not the scope
of this temporal-response class. Stress response is not a mandatory parent
because the proposed definition is not restricted to stress. A more specific
upstream parent remains a curator decision, not an inferred exact mapping.

## Novelty And Reservation

Allocation was checked on 2026-10-12 against main
`4a84d33e1dc4369e3c2c84fe0d4d87b537097388`, all 22 registered TraitMech
worktrees, 582 proposal cohorts and 4,092 narrative reservation intervals.
It also covered 530 proposal files in 127 registered CommunityMech worktrees.
Lexical and citation searches included ignored and hidden files, raw ontology,
records, history, research, proposals and generated products. Searches did not
unpack archives, follow symlink directories or claim unregistered/private work.

The fresh 399-record seed projection was compared by exact ID against the
1,101-record live baseline; 55 absent IDs remain leads, not automatic additions.
The frozen 1,546-row release-delta and 153-row active-review tables were treated
as historical decisions. No exact active or deprecated candidate was found
in the pinned/current released RDF or current templates. The imports-only
editable ontology root was not used alone to establish absence.

Fresh fully paginated file lists covered TraitMech PRs #1782, #1476, #973 and
draft #924; CommunityMech draft #935; and METPO PRs #644, #643, #641, #640,
#638 and #629. Relevant immutable blobs and complete pending ontology/template
blobs were inspected. Heads and open sets were stable through acquisition.
All 644 METPO issue/PR bodies and 654 comments were searched; #340's use of
"pre-anticipate" concerns mapping design, not this biological trait.

Current upstream snapshots were verified by Git blob and SHA-256 hashes:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `80049bcc9195480a58633236169b62f86c23489a`.
- KG-Microbe: `bac582f4e131a7ba96b585996ae1fa759403f0b6`; its changed default
  branch was refreshed with 106 mapping/proposal/guidance files from an
  untruncated tree, not silently reused from an older snapshot.

No conflicting reservation was found in this scope. Recheck current main,
registered roots and pending heads immediately before publication. These
bounded checks cannot eliminate concurrent-allocation races and do not establish
global trait-discovery exhaustion. No pinned ontology refresh is included.

## ID Space And Subset

- Local ID: `traitmech:000707`.
- Cohort: `metpo_traitmech_v583`.
- Reserve the entire `METPO:1066000`-`METPO:1066099` block.
- Populate only `METPO:1066000`; it is an unreleased proposal placeholder.
- Subset: `metpo_traitmech_2026_10`, following adjacent monthly-tag convention.
- The block is separate from CommunityMech v1 `1007100`-`1007220` and all
  inspected later reservations; no historical block is reused.

## Files And Verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two canonical headers, one class row, 11 columns |
| `proposal.md` | Scope, evidence, reservation and round-trip rationale |

Property and SSSOM files are inapplicable. The maintained writer is
`scripts/add_environmental_anticipation_trait.py`; it validates before writing
and refuses parent, target or proposal drift. TSV headers match the freshly
checked upstream class template. Citation fields do not assert equivalence.

```bash
just verify-proposal metpo_traitmech_v583
just robot-validate-proposal metpo_traitmech_v583
just qc
just validate-history
just validate-products
```

The saved structured review and PR report actual outcomes, source limits and
generated-artifact checks. Inspect parsed RDF identity/hierarchy in addition
to ROBOT exits. Normal whitespace checks flag required trailing TSV header
tabs; after width verification, only that exact template uses the documented
`-blank-at-eol` exception. No frozen baseline or global check is weakened.

## Upstream Path And Round Trip

After review, submit the TSV and rationale to `berkeleybop/metpo` or the
KG-Microbe proposal pipeline. Curator `codex`, the LLM-assisted curation event
and append-only repository history preserve authorship. Upstream maintainers
choose the final identifier and hierarchy.

After an explicitly reviewed ontology update includes the accepted term,
re-seed that release and migrate the identifier and dependent references,
preserving `traitmech:000707` as a traceable identifier alias and retaining
history. Do not emit the placeholder as a released METPO identity or replace
the pinned ontology automatically.

## Change Log

- v583, 2026-10-12: propose one qualified anticipation phenotype with two
  directly checked primary-source snippets and explicit evidence limits.
