# METPO ROBOT Template Proposal - AbiR System (v194, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v193 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiR system, the
genome-level possession trait for the multicomponent abortive-infection
determinant encoded by two separated regions of the pKR223 plasmid in
Lactococcus lactis subsp. lactis KR2. Twomey et al. named AbiR, showed that
its phenotype was encoded by two genetic loci separated by the LlaKR2I
restriction-modification genes, and classified it as a multicomponent,
heat-sensitive, early-functioning Abi system that impedes phage DNA
replication. DefenseFinder models AbiR with `AbiR__AbiRa`, `AbiR__AbiRb`, and
`AbiR__AbiRc` profiles.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiR |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1027100` is reserved for this one-row class cohort. The v193 cohort used
`METPO:1027000`, so v194 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files under
`data/traits`, `history`, `proposals`, `scripts`, the pinned local METPO
snapshot, and the pinned DefenseFinder registries used for candidate discovery.
AbiR occurred only in the pinned DefenseFinder article, rules, and HMM
registries; no exact same-scope record, `abir_system` slug, `traitmech:000317`,
`metpo_traitmech_v194`, or `METPO:1027100` was present before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1027100` | AbiR system | `METPO:1016800` abortive infection system |

AbiR system captures genome-level possession of the multicomponent AbiR
determinant originally described on pKR223 and represented by DefenseFinder's
three required AbiR HMM profiles. It excludes individual `abiR`-region genes;
AbiR proteins; pKR223 as a plasmid; the intervening LlaKR2I
restriction-modification system; individual DefenseFinder HMM profiles; source
database rows naming one AbiR locus; individual lactococcal phage host-range
outcomes; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiR, pKR223, LlaKR2I, the DefenseFinder
HMMs, and downstream phage-restriction or phage-DNA-replication outcomes are
shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  related shifted label, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000317` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000317` as traceability during the migration.

## Change Log

- v194, 2026-09: lifts `traitmech:000317 AbiR system` into the
  `METPO:1027100` block.
