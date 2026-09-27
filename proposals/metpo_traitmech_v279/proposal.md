# METPO proposal: Rst_Hydrolase-3Tm system

## Scope

This Scope A cohort lifts one TraitMech-local synthetic class into METPO.
Scope B and Scope C counts are zero for this cohort: it proposes no causal
predicates and no schema enum values.

Rst_Hydrolase-3Tm system was minted as `traitmech:000402` on 2026-09-27
because METPO has no exact organism-level possession trait for the
DefenseFinder `Rst_Hydrolase-3Tm`/`Rst_Hydrolase-Tm` model. It has been used in
one TraitMech record since minting.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1035600` | Rst_Hydrolase-3Tm system | `METPO:1016300` phage defense system |

Rst_Hydrolase-3Tm system captures genome-level possession of a two-protein
hydrolase/transmembrane locus represented by DefenseFinder as a two-profile
`Rst_Hydrolase-Tm` model requiring `Rst_Hydrolase-Tm__Hydrolase` and
`Rst_Hydrolase-Tm__Hydrolase-Tm` and experimentally linked to T7 protection
when expressed in *Escherichia coli*. It excludes individual Hydrolase or
Hydrolase-Tm proteins, DefenseFinder HMM profiles, the source keys
`Rst_Hydrolase-3Tm` and `Rst_Hydrolase-Tm`, unvalidated RefSeq examples, and
other Rst or phage-defense systems.

## External Mappings

No exact external mapping is proposed. Individual Hydrolase or Hydrolase-Tm
proteins, DefenseFinder HMM profiles, source database rows naming one Rousset
et al. system model, and candidate RefSeq genomic examples are shifted from
this organism-level GENOMICS possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with a
  primary Rousset et al. citation, no exact synonyms, no exact external xrefs,
  and five related source-key, HMM-profile, or component synonyms.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000402` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000402` as traceability during the migration.

## Change Log

- v279, 2026-09: lifts `traitmech:000402 Rst_Hydrolase-3Tm system` into the
  `METPO:1035600` block.
