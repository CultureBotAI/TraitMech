# METPO ROBOT Template Proposal - MqsRAC System (v245, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v244 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for MqsRAC system, the
genome-level possession trait for an MqsR/MqsA/MqsC
toxin-antitoxin-chaperone phage-defense locus. Fernandez-Garcia et al. support
MqsR/MqsA/MqsC from *Escherichia coli* C496_10 as a tripartite
toxin-antitoxin-chaperone phage-exclusion system whose expression from its
natural promoter inhibits T2 phage through persister-cell formation and in
concert with restriction/modification systems. DefenseFinder maps the `MqsRAC`
key to the Vassallo et al. *E. coli* pangenome phage-defense screen while
pinning custom `MqsRAC__mqsC` and `MqsRAC__mqsR` profiles for this system.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for MqsRAC |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1032200` is reserved for this one-row class cohort. The v244 cohort used
`METPO:1032100`, so v245 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository, excluding only `.git`. It found no exact same-scope MqsRAC
system record, `mqsrac_system` slug, `MqsRAC__mqsC` or `MqsRAC__mqsR` profile
row, `traitmech:000368`, `metpo_traitmech_v245`, or `METPO:1032200`. The
Fernandez-Garcia et al. DOI appears only in an unrelated viable-but-nonculturable
state deep-research bibliography.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1032200` | MqsRAC system | `METPO:1016300` phage defense system |

MqsRAC system captures genome-level possession of an MqsR/MqsA/MqsC
toxin-antitoxin-chaperone locus represented by DefenseFinder as a two-profile
model requiring `MqsRAC__mqsC` and `MqsRAC__mqsR`. It excludes the individual
MqsR, MqsA, and MqsC components, the `MqsRAC__mqsC` and `MqsRAC__mqsR` HMM
profiles, MqsR RNase activity outside a complete antiphage locus,
MqsRAC-dependent persister formation, restriction/modification-assisted T2
inhibition, source database rows naming one MqsRAC model, and other
phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual MqsR/MqsA/MqsC components,
MqsR RNase activity, downstream persistence or restriction/modification
activities, and DefenseFinder profile rows are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, four related shifted labels, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000368` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000368` as traceability during the migration.

## Change Log

- v245, 2026-09: lifts `traitmech:000368 MqsRAC system` into the
  `METPO:1032200` block.
