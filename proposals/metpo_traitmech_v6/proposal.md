# METPO ROBOT Template Proposal — TraitMech Predicate Lift (v6, 2026-06)

> **Upstream submission:** consolidated in [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) (2026-06-14) — requesting real METPO IDs for this cohort.

## Context

[TraitMech](https://github.com/CultureBotAI/TraitMech) records carry
`causal_graphs:` with typed `nodes:` and evidence-backed `edges:`. Each
edge carries a free-text `predicate:` label and an optional `predicate_id:`
CURIE grounding (LinkML class `CausalEdge`).

The [v2 cohort](../metpo_traitmech_v2/) proposed the first 8 causal-graph
predicates (`METPO:2007400`–`METPO:2007407`), including the electron-flux
relations `feeds electrons into` (2007402) and `transfers electrons to`
(2007403). Subsequent predicate-grounding passes
(`scripts/ground_causal_predicates.py`) raised coverage to **1071 / 1284
edges (83%)** before this cohort.

The residual that remained was dominated by a **microbe-specific
electron-transfer / bioenergetics cluster** — relations with no RO, biolink,
or existing-METPO home. This v6 cohort closes the genuinely novel members of
that cluster by proposing **4 new METPO predicates**, and grounds the rest
either to the new predicates or to existing v2 predicates where they are
semantic equivalents.

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| A (synthetic trait classes) | `data/traits/**` `traitmech:` records | 0 | already covered by [v5](../metpo_traitmech_v5/) (120/120) |
| B (causal-graph predicates) | electron-transfer/bioenergetics residual in `reports/predicate_grounding_residual.tsv` | **4 predicates / 8 edges** | included |
| C (controlled vocabularies) | `CausalNodeTypeEnum` | 0 | already covered by [v1](../metpo_traitmech_v1/) (13/13) |

Total property rows in v6: **4**. No class rows — the domain class
(`METPO:1007401` *trait causal node*) was minted in v1.

> The Scope-A "failure" reported by `just verify-proposal` is expected for a
> predicate-only cohort (v2 and v4 report it identically); Scope A is fully
> covered by v5.

## Predicate proposals

Each row uses domain = range = `METPO:1007401` (the v1-minted *trait causal
node* superclass), mirroring v2. Reviewers should merge v1, v2, and v6
together at adoption time so domain/range references resolve.

| ID | Label | Edges | Rationale |
|---|---|---:|---|
| `METPO:2007600` | transfers electrons via | 2 | Mediated electron transfer through a diffusible carrier (interspecies H₂/formate in syntrophy). Distinct from the direct donor→acceptor sense of `transfers electrons to` (2007403) — the object is the carrier, not the terminal acceptor. |
| `METPO:2007601` | imposes gradient of | 4 | Establishment of a transmembrane electrochemical gradient of an ion (e.g. an acidic environment imposing a proton gradient). No RO/biolink relation expresses "establishes a gradient of"; central to chemiosmotic and acid-stress phenotypes. Consolidates the corpus labels `imposes gradient of` (1) and `increases gradient of` (3). |
| `METPO:2007602` | couples electron flow to | 1 | Chemiosmotic coupling: an electron-transport process thermodynamically driving an energy-conserving process (ETC → proton-motive force). Textbook, reusable across respiration / photosynthesis. |
| `METPO:2007603` | serves as electron donor and acceptor | 1 | Disproportionation: one species simultaneously oxidized and reduced within a process. Not expressible by the single-direction redox predicates 2007403 / 2007405. |

### Residual grounded to existing v2 predicates (no new ID)

Three further residual labels are semantic equivalents of v2 predicates and
were grounded there rather than proposed anew (see
`mappings/predicate_grounding.tsv`):

| Corpus label | Grounded to |
|---|---|
| `donates electrons to` | `METPO:2007403` transfers electrons to |
| `provides electrons to` | `METPO:2007403` transfers electrons to |
| `provides electrons for` | `METPO:2007402` feeds electrons into |

### Deliberately left residual

One-off (single-edge), idiosyncratic, or direction-ambiguous labels are
**not** proposed — proposing them would be speculative: `conserves energy
by`, `reoxidized by`, `reduced with electron donor`, `provides electron
donor`, `provides electron acceptor`, `donates phosphoryl group to`,
`transfers electrons from`, `mediates transfer between`, `uses electron flow
from`.

## ID space and subset

Reserved against the **latest METPO release (`2026-06-12`)**, which uses
1-series IDs up to `1007093` and 2-series up to `2000734`; the entire
`2007xxx` predicate range is unused upstream. This cohort takes
`METPO:2007600`–`METPO:2007603` — above the v4 block (`2007500`) and far clear
of upstream's active 2-series frontier. Subset tag: `metpo_traitmech_2026_09`
(next free suffix after v4's `2026_08`). No collision with CommunityMech v1
(`1007100`–`1007220` / `2007100`–`2007113`).

## Files

| File | Rows |
|---|---|
| `metpo_proposal_properties_robot.tsv` | 4 property rows (+ 2 header rows) |
| `proposal.md` | this narrative |

No classes TSV and no SSSOM mappings file: these predicates have **no**
cross-ontology equivalent (that is why they are proposed), so there is
nothing to record as a `skos:*Match`.

## Verification

- `just verify-proposal metpo_traitmech_v6` — column counts 12/12, header
  directives, subset tag all pass (Scope-A check N/A, as for v2/v4).
- `just robot-validate-proposal metpo_traitmech_v6` — **PASS**: props.owl
  compiles, merges with `metpo.owl`, ELK reasons with no UNSAT (reasoned −
  merged = +6 lines; no unintended inferred equivalences).
- `just validate-strict` — 477 trait files, 0 errors after grounding the 11
  motivating edges.

## Upstream path

Submit `metpo_proposal_properties_robot.tsv` to
[berkeleybop/metpo](https://github.com/berkeleybop/metpo) (issue or PR with
the TSV attached) alongside the v1–v5 cohorts. The `2007600`–`2007603`
numbers are TraitMech placeholders; METPO maintainers mint the real IDs.

## Round-trip plan

After upstream mints real METPO IDs for these predicates: update
`data/raw/metpo.owl`, re-seed, and swap the `predicate_id` groundings in
`mappings/predicate_grounding.tsv` (and the affected `data/traits/**` edges)
from the placeholder `METPO:2007600`–`2007603` to the minted CURIEs.

## Change log

- v6, 2026-06: propose 4 electron-transfer/bioenergetics predicates
  (`METPO:2007600`–`2007603`); ground 8 edges to them and 3 to existing v2
  predicates. IDs reserved against METPO release `2026-06-12`.
