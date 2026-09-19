# METPO ROBOT Template Proposal - Dsr System (v157, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v156 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Dsr system, the
genome-level possession trait for defense-associated sirtuin antiphage loci. Gao
et al. named `dsr` as defense-associated sirtuin among experimentally tested
candidate defense systems and identified SIR2-domain proteins among additional
antiphage defense systems. Garb et al. then showed that DSR proteins deplete
NAD+ during infection and that DSR2 can respond directly to a Bacillus subtilis
phage tail tube protein. DefenseFinder models Dsr as Dsr_I and Dsr_II subtype
models.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000280` was minted locally because METPO has no active exact Dsr-system phage-defense class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1023400` is reserved for this one-row class cohort. The v156 cohort used
`METPO:1023300`, so v157 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v157`, no live phage-defense record
used `traitmech:000280`, and no prior proposal reserved `METPO:1023400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1023400` | Dsr system | `METPO:1016300` phage defense system |

Dsr system captures genome-level possession of a defense-associated sirtuin
locus whose SIR2-domain effector can deplete NAD+ during bacteriophage defense
and that DefenseFinder represents as a Dsr subtype. It excludes individual `dsr` genes;
Dsr proteins; generic sirtuins or SIR2 domains; Thoeris Sir2 domains;
prokaryotic Argonaute-associated Sir2 proteins; metabolic dissimilatory sulfite
reductase DsrAB systems; Dsr_I or Dsr_II HMM profiles; predicted source-database
rows naming one Dsr component; and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Defense-associated sirtuin genes, Dsr
proteins, SIR2-domain molecular functions, DefenseFinder HMM profiles, and
dissimilatory sulfite reductase DsrAB components are shifted from this
organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with one
  exact Dsr synonym, one related gene/protein-family label, and no exact
  external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000280` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000280` as traceability during the migration.

## Change Log

- v157, 2026-09: lifts `traitmech:000280 Dsr system` into the
  `METPO:1023400` block.
