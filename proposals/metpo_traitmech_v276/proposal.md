# METPO ROBOT Template Proposal - Old Exonuclease System (v276, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v275 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for Old exonuclease system,
the genome-level possession trait for a one-protein phage-defense locus modeled
by DefenseFinder under the `Old_exonuclease` key. The original P2 Old nuclease
study links the bacteriophage P2 Old protein to interference with phage lambda,
and the pinned DefenseFinder wiki maps Old_exonuclease to P2 Old and to broader
Rousset et al. Old plus Tin validation. DefenseFinder models Old_exonuclease in
the pinned rule and HMM tables with one required profile,
`Old_exonuclease__Old_exonuclease`.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for Old exonuclease system |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1035300` is reserved for this one-row class cohort. The v275 cohort used
`METPO:1035200`, so v276 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

The pre-curation collision search included ignored and hidden files across the
curation corpus. It found no exact same-scope Old exonuclease system record,
`old_exonuclease_system` slug, P2 Old source protein accession,
`traitmech:000399`, `metpo_traitmech_v276`, or `METPO:1035300`; the Rousset
final DOI was already used by distinct prophage-hotspot phage-defense-system
records.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035300` | Old exonuclease system | `METPO:1016300` phage defense system |

Old exonuclease system captures genome-level possession of a locus represented
by DefenseFinder as a single required Old_exonuclease profile and
experimentally linked to lambda interference through the bacteriophage P2 Old
protein. It excludes individual Old proteins, the DefenseFinder
`Old_exonuclease__Old_exonuclease` HMM profile, the P2 Tin accessory protein,
RecBCD inhibition, lambda interference outside a complete Old_exonuclease
locus, unvalidated RefSeq examples, and other phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Old proteins, the P2 Tin
accessory protein, DefenseFinder HMM profiles, source database rows naming one
Rousset et al. system model, and candidate RefSeq genomic examples are shifted
from this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, no exact external xrefs, and two related source-key or
  HMM-profile synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000399` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000399` as traceability during the migration.

## Change Log

- v276, 2026-09: lifts `traitmech:000399 Old exonuclease system` into the
  `METPO:1035300` block.
