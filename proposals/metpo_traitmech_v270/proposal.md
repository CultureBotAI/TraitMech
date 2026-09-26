# METPO ROBOT Template Proposal - PD-T4-8 System (v270, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v269 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for PD-T4-8 system, the
genome-level possession trait for a DefenseFinder-modeled anti-phage locus from
Vassallo et al.'s *E. coli* pangenome screen. DefenseFinder models PD-T4-8 with
one required HMM profile, `PD-T4-8__PD-T4-8`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for PD-T4-8 system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1034700` is reserved for this one-row class cohort. The v269 cohort
used `METPO:1034600`, so v270 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope PD-T4-8 system record,
`pd_t4_8_system` slug, `PD-T4-8__PD-T4-8`, `traitmech:000393`,
`metpo_traitmech_v270`, or `METPO:1034700`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1034700` | PD-T4-8 system | `METPO:1016300` phage defense system |

PD-T4-8 system captures genome-level possession of a single-profile DefenseFinder
phage-defense locus experimentally linked to T2, T4, T6, SECphi18, and SECphi27
protection when expressed in *E. coli*. It excludes the individual PD-T4-8 gene
or protein, the DefenseFinder `PD-T4-8__PD-T4-8` profile, the source key
`PD-T4-8`, DUF4263 or Shedu-system domain context outside a complete PD-T4-8
locus, protection against T2, T4, T6, SECphi18, or SECphi27 outside a complete
PD-T4-8 locus, RefSeq example loci without experimental validation, sibling
PD-T4 systems, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual proteins, source database rows
naming the DefenseFinder model, HMM profiles, RefSeq example loci, DUF4263 or
Shedu-system domain context, and specific phage-protection phenotypes are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact external xrefs and related DefenseFinder profile labels.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000393` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000393` as traceability during the migration.

## Change Log

- v270, 2026-09: lifts `traitmech:000393 PD-T4-8 system` into the
  `METPO:1034700` block.
