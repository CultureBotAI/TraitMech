# METPO Proposal v454: Druantia IV and Family Scope

## Context

This cohort adds `traitmech:000577 Druantia type IV system` and corrects the
definition of `traitmech:000234 Druantia system` (#1635). The new class is
organism-level possession of a recurring DruE/F/L locus architecture, without
the type-II DruM/G components. It is not a protein, HMM hit, detector row or
experimentally demonstrated resistance phenotype.

A fresh METPO seed produced 399 records, 344 exact IDs already present and
55 absent. Exact-ID absence was only a lead. Whole-repository searches,
including ignored and hidden files, found no exact IV record or METPO term.
Existing mentions were the broader family discussion and III-scope exclusions.
The existing Druantia III child (`traitmech:000560`) has a different architecture.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 2 | phage defense system, corrected Druantia family | 1 new IV child |
| B: predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

## Hierarchy Decisions

| Proposed ID | Stable local ID | Label | Parent |
|---|---|---|---|
| METPO:1053100 | traitmech:000234 | Druantia system | METPO:1016300 |
| METPO:1053101 | traitmech:000577 | Druantia type IV system | METPO:1053100 |

Payne et al. (DOI:10.1093/nar/gkab883), Results and Figure 2C, define the
DruE/F/L architecture and its distinction from type-II DruM/F/G/E. Their
functional experiments test Zorya III, Hachiman II and Lamassu II, not
Druantia IV. No canonical taxon or type-IV mechanism is inferred from those
experiments. No exact external mappings or organism-level disjointness are
proposed.

The immutable DefenseFinder model at
`afb0e5a8b466be53586b13266f5d38d98c3ac268` has three mandatory slots and
minimum counts of three. DruE and DruF have exchangeable profiles; DruL
does not. PADLOC at `9e380165633a8d6aef93b5a164cea0f3359bd33f` requires
DruE4/F4/L4, with secondary DruK. Neither rule prohibits DruM/G. Thus raw
calls alone do not establish the literature's absence-qualified architecture;
complete locus review is required. Missing hits and incomplete assemblies do
not establish biological absence or functional defense.

Wu et al. (DOI:10.64898/2026.05.12.724681, preprint v1) suggest a conserved
DruE-family DNA-processing mechanism from type-III results. The corrected
family definition does not turn that suggestion into a universal requirement.
The overgeneralized parent graph is removed; characterized type-III evidence
remains on the existing child. Native type-IV activity and DruL/DruK function
remain open questions.

## Relationship to v111

This is Path C of the proposal-update policy. `METPO:1053100` replaces the
unminted v111 placeholder `METPO:1018800` for the same stable local family.
Do not submit both rows as separate biological classes. The historical v111
TSV is unchanged; its narrative records this replacement. Neither placeholder
is asserted to be a minted upstream ID.

The already-merged v437 Druantia III TSV still references the historical
family placeholder. During upstream consolidation, redirect that parent from
`METPO:1018800` to `METPO:1053100`; retain the v437 child ID and definition.
The live III TraitRecord already points to the stable local family ID, so
no unrelated child YAML or historical TSV rewrite is needed.

## ID Space and Subset

The live highest cohort was v453, reserving METPO:1053000. v454 reserves
the fresh METPO:1053100-1053199 block and uses subset
`metpo_traitmech_2026_10`, replacing v111's September subset. Collision
searches included ignored and hidden files. This block does not overlap
CommunityMech v1's 1007100-1007220 range.

## Files

| Artifact | Rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 2 classes plus 2 headers |
| proposal.md | This narrative |

No property template or SSSOM is emitted because there are no new predicates
or verified equivalent external classes. The class template follows the
canonical kg-microbe `master` contract, including the empty ROBOT header cells.

## Verification

The writer passes 22 focused tests for scientific boundaries, proposal
identity, preimage refusal, dry-run behavior, replay and preservation.
Template verification passes with zero failures; both 11-column headers
match the canonical upstream template. ROBOT template, merge and ELK
reasoning pass with no UNSAT (23,347 merged lines, 23,353 reasoned).
Cross-cohort coverage includes all 577 local IDs. Both changed records pass
LinkML validation. All three new snippets exactly match primary full text
or pinned raw models; the abstract-only check is inconclusive for the paper's
Results quote. Final full-corpus results are recorded on the reviewed PR.

## Upstream Path

After review, consolidate both rows into
[berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535),
with the v111 replacement and v437 parent-redirection instructions above.
Unminted METPO placeholders must not be used as production trait identifiers.

## Round-Trip Plan

After real IDs are minted, update the METPO mirror, re-seed only the relevant
records, migrate their identifiers and parent links, and preserve stable local
IDs for traceability. Retain historical proposals without reusing their blocks.

## Change Log

- v454, 2026-10-03: add Druantia IV possession and correct the family-wide
  mechanism overclaim; preserve v111 and v437 TSVs.
