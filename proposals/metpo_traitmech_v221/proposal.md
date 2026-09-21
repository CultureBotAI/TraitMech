# METPO ROBOT Template Proposal - AbiA System (v221, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v220 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for AbiA system, the
genome-level possession trait for a lactococcal `abiA` abortive-infection
locus. Dinsmore and Klaenhammer showed that `abiA`, formerly `hsp`, encodes
an abortive phage infection mechanism inhibiting phage DNA replication, that
AbiA-containing plasmids protect Lactococcus lactis against c2, p2, sk1, and
phi31, and that `abiA` gene dosage or expression changes phage-resistance
levels. DefenseFinder models AbiA with an `AbiA_large` subrule and an
`AbiA_small` subrule.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for AbiA |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1029800` is reserved for this one-row class cohort. The v220 cohort used
`METPO:1029700`, so v221 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
whole repository outside `.git`, `.venv`, and scratch `reports/robot`, plus the
pinned DefenseFinder registries used for candidate discovery. AbiA occurred
only in neighboring phage-defense records as a same-source comparator, not as
an AbiA record or proposal; no exact same-scope record, `abia_system` slug,
`AbiA system` label, `AbiA_large` or `AbiA_small` model row,
`traitmech:000344`, `metpo_traitmech_v221`, or `METPO:1029800` was present
before this cohort.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1029800` | AbiA system | `METPO:1016800` abortive infection system |

AbiA system captures genome-level possession of an AbiA-family locus whose
copy number or expression modulates Lactococcus lactis phage resistance and
that DefenseFinder represents with AbiA_large or AbiA_small model subrules.
It excludes individual `abiA`, `hsp`, `AbiA_large`, or `AbiA_small` genes;
AbiA proteins; AbiA leucine-repeat variants; individual DefenseFinder HMM
profiles; pTR2030-derived plasmid constructs; phage escape mutants; source
database rows naming one AbiA model; and other abortive-infection systems.

## External Mappings

No exact external mapping is proposed. AbiA genes, AbiA proteins,
DefenseFinder subrules and HMMs, pTR2030-derived plasmids, lactococcal
phage-resistance assay outcomes, and downstream phage-DNA-replication
inhibition are shifted from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with
  related shifted labels, no exact synonyms, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000344` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000344` as traceability during the migration.

## Change Log

- v221, 2026-09: lifts `traitmech:000344 AbiA system` into the
  `METPO:1029800` block.
