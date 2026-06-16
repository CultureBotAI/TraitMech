# METPO ROBOT Template Proposal — TraitMech Causal-Mechanism Lift (v7, 2026-06)

> **Upstream submission:** consolidated in [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) (2026-06-14) — requesting real METPO IDs for this cohort.

## Context

After the predicate-grounding (v2/v4/v6) and node-grounding passes, TraitMech's
causal graphs reach **85% predicate / 62% node** grounding. The remaining node
residual is dominated by graph-internal narrative phrases that are **not**
ontology concepts (e.g. "warm-mesophile adaptation", "maximal growth rate",
"precursor metabolites"). A small number, however, are **genuine, recurring,
microbe-specific mechanism concepts with no upstream home** in METPO, CHEBI,
GO, ENVO, or PATO. This cohort lifts those.

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| A (synthetic trait classes) | `traitmech:` records | 0 | covered by [v5](../metpo_traitmech_v5/) |
| B (causal predicates) | predicate residual | 0 | electron-transfer set covered by [v6](../metpo_traitmech_v6/); the rest are vague verbs, not predicates |
| **mechanism classes** | recurring no-home causal-graph node concepts | **2** | included |

Only **2** classes are proposed — deliberately selective. The bulk of the node
residual is composed of trait-graph narrative nodes (adaptation states, composite
descriptive phrases) that should stay as free-text node labels, not become METPO
classes. Two further residual concepts were instead **grounded to existing
ontology terms** in this PR rather than proposed (`hydrostatic pressure` →
`PATO:0001025` pressure; `chemotaxis signaling` → `GO:0006935` chemotaxis).

## Class proposals

| ID | Label | Edges | Why new |
|---|---|---:|---|
| `METPO:1007720` | salt-in strategy | 5 | The "salt-in" halophilic osmoadaptation (molar cytoplasmic K⁺/Cl⁻ accumulation), distinct from the compatible-solute "salt-out" strategy. No METPO/GO term; recurs across extremely_halophilic / halophilic / nacl_optimum_high. |
| `METPO:1007721` | reductive genome evolution | 3 | Progressive genome-size reduction by gene loss under host association / low effective population size. No GO process term; recurs across genome_size / genome_streamlining / endosymbiosis. |

### Hierarchy decision

Both are parented under `METPO:1000059` (*phenotype*) — the generic parent the
TraitMech synthetic-trait corpus already uses — as a **fallback**. These are
mechanism/process concepts; maintainers may prefer to slot `salt-in strategy`
under an osmoadaptation / stress-response process parent and `reductive genome
evolution` under a genome-evolution process parent. Flagged for review (see the
`observations` column).

## ID space and subset

Reserved against the **latest METPO release (`2026-06-12`, w3id/BioPortal)**:
1-series used to `1007093`, 2-series to `2000734`. This cohort takes
`METPO:1007720`–`METPO:1007721` — the next contiguous block above the v5 class
block (`…1007719`), collision-free upstream. Subset tag:
`metpo_traitmech_2026_10` (next after v6's `2026_09`).

## Files

| File | Rows |
|---|---|
| `metpo_proposal_classes_robot.tsv` | 2 class rows (+ 2 header rows) |
| `proposal.md` | this narrative |

## Verification

- `just verify-proposal metpo_traitmech_v7` — column counts 11/11.
- `just robot-validate-proposal metpo_traitmech_v7` — **PASS** (ELK no UNSAT, +6 lines).
- `just validate-strict` — 477 trait files, 0 errors after grounding the 13
  motivating edges (5 salt-in + 3 reductive-genome to the new classes; 4
  hydrostatic-pressure + chemotaxis to existing PATO/GO).

## Upstream path

Submitted via [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535).
The `1007720`–`1007721` numbers are placeholders; METPO maintainers mint the real IDs.

## Round-trip plan

After upstream mints real IDs: update `data/raw/metpo.owl`, re-seed, and swap the
`grounding:` values in `mappings/node_grounding.tsv` + affected `data/traits/**`
nodes from the placeholder CURIEs to the minted ones.

## Change log

- v7, 2026-06: propose 2 causal-mechanism classes (`METPO:1007720`–`1007721`);
  ground 8 edges to them; ground 7 further residual edges to existing PATO/GO.
  IDs reserved against METPO release `2026-06-12`.
