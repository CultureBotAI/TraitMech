# METPO ROBOT Template Proposal - SPARTA System (v117, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v116 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the SPARTA system, the
genome-level possession trait for short prokaryotic Argonaute TIR-APAZ loci.
Koopal et al. named SPARTA around paired short pAgo and TIR-APAZ proteins whose
guide RNA-mediated target DNA binding induces oligomerization and TIR-domain
NAD(P)ase activity in plasmid-challenged cells. Kottur et al. resolved the
guide-RNA/target-ssDNA-bound SPARTA oligomer and supported the structural basis
of active assembly.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000240` was minted locally because METPO has no active exact SPARTA-system class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1019400` is reserved for this one-row class cohort. The v116 cohort used
`METPO:1019300`, so v117 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v117`, no live record used
`traitmech:000240`, and no prior proposal reserved `METPO:1019400`.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1019400` | SPARTA system | `METPO:1000188` quality |

SPARTA system captures genome-level possession of a short prokaryotic Argonaute
TIR-APAZ locus encoding short pAgo and TIR-APAZ components that assemble into a
guide-RNA/target-DNA-activated NAD(P)ase complex. It excludes individual `pago`
or `tir-apaz` genes; standalone pAgo, TIR-APAZ, SIR2-APAZ, DNase-APAZ, and
nuclease-APAZ proteins; guide RNAs; target-DNA binding, NAD(P)ase activity, and
abortive-infection outputs as process-level activities; high-copy
plasmid-challenge measurements; the limited phage-protection phenotype observed
for some SPARTA loci; DefenseFinder/PADLOC rows naming one predicted locus;
SIR2-APAZ/SPARSA, Hailong, Mokosh, Eleos, Olokun, Hna, Menshen, and other
short-pAgo families; other plasmid-defense systems; plasmid carriage; and
dedicated phage-defense-system families such as BREX, CBASS, DISARM, AVAST,
Gabija, RADAR, PARIS, Wadjet, Zorya, and CRISPR-Cas.

## External Mappings

No exact external mapping is proposed. Short prokaryotic Argonaute proteins,
TIR-APAZ effectors, guide RNAs, active SPARTA complexes, APAZ-associated SIR2 or
nuclease protein families, DefenseFinder/PADLOC locus calls, and
plasmid-challenge outcomes are shifted from this organism-level GENOMICS
possession trait.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 11-column ROBOT class template with one
  exact SPARTA long-form synonym and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000240` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000240` as traceability during the migration.

## Change Log

- v117, 2026-09: lifts `traitmech:000240 SPARTA system` into the
  `METPO:1019400` block.
