# METPO ROBOT Template Proposal — TraitMech Node-Class Lift (v3, 2026-07)

## Context

The TraitMech v1 cohort lifted the *causal-graph scaffolding* (graph,
node, edge classes + the `CausalNodeTypeEnum` value set). The v2
cohort lifted *causal-graph predicates* (the property axis). This
v3 cohort is the third leg of the same triangulation: **lifting
microbe-trait-specific node-class abstractions** that the
node-grounding pipeline (#66) cannot reach because no clean upstream
home (CHEBI, GO, ENVO, PRO, etc.) exists.

The node-grounding pipeline applies a curated
`(label, node_type) → CURIE` mapping
(`mappings/node_grounding.tsv`) across
`data/traits/**/causal_graphs[].nodes[]`. As of this proposal,
**622 of 1252 causal-graph nodes are grounded** (50%) using 39
CHEBI / GO / ENVO / PATO mappings from #66 plus the 7 additions in
this cohort (6 METPO + 1 GO).

The remaining **630 nodes across 503 distinct (label, type) keys**
are residual. Within that residual, the largest, most semantically
coherent clusters are abstractions that **don't fit existing
ontologies cleanly** — they are bioenergetic states, class-of-X
abstractions, and microbe-physiology qualities. This cohort
proposes **6 new METPO classes** (`METPO:1007500`–`METPO:1007505`)
that together cover **58 nodes** (9% of the residual at v2-merge
time).

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| A (synthetic trait classes) | `data/traits/**/*.yaml` records whose `identifier:` starts with `traitmech:` | 0 | not applicable — none in corpus |
| B (causal-graph predicates) | already lifted in v2 | 0 | already covered |
| C (controlled vocabularies) | already lifted in v1 (`CausalNodeTypeEnum`) | 0 | already covered |
| **D (node-class abstractions, NEW)** | top clusters in `reports/node_grounding_residual.tsv` | **6 classes / 58 nodes** | included |

Total class rows in v3: **6**. No property rows.

> *Note: "Scope D" is a TraitMech naming convention for node-class
> proposals — the upstream `metpo-proposal` skill currently
> documents only A/B/C. The same ROBOT-template column conventions
> apply.*

## Node-class proposals

All 6 sit directly under `METPO:1000000` (root) because no closer
existing METPO parent applies. Upstream maintainers can relocate
them under a richer parent (e.g. *bioenergetic state*,
*microbial material entity*) if METPO grows one.

| ID | Label | Nodes | Cluster |
|---|---|---:|---|
| `METPO:1007500` | proton motive force | 16 | bioenergetic state — electrochemical proton gradient |
| `METPO:1007501` | microbial biomass | 16 | material entity — carbon-assimilation sink |
| `METPO:1007502` | inorganic electron donor | 7 | class-of-chemicals — lithotrophic substrates |
| `METPO:1007503` | reducing power | 4 | metabolic capacity — reduced-cofactor pool |
| `METPO:1007504` | terminal electron acceptor | 5 | role-of-chemical — end of ETC (covers both CHEMICAL and MOLECULAR_FUNCTION node-type uses) |
| `METPO:1007505` | membrane fluidity | 6 | membrane quality — modulated by temperature / lipid composition |

### Why not CHEBI / GO / PATO / ENVO?

| Proposed | Considered | Why rejected |
|---|---|---|
| `proton motive force` | GO:0015988 (proton motive force generation) | corpus uses the *thing* (the gradient), not the *process of generating* it |
| `microbial biomass` | CHEBI:33232 (biological role), GO:0044464 (cell part) | neither captures the aggregate-cellular-mass-as-sink sense |
| `inorganic electron donor` | CHEBI:50858 (organic donor) | CHEBI has individual species (H₂, NH₄⁺, Fe²⁺ etc.) but no class for "inorganic electron donor in lithotrophy" |
| `reducing power` | individual cofactor CHEBIs (NADH CHEBI:16908, etc.) | corpus uses the *capacity / pool*, not specific species |
| `terminal electron acceptor` | individual CHEBIs (O₂, NO₃⁻, SO₄²⁻) | role-of class is missing upstream; corpus mixes CHEMICAL + MOLECULAR_FUNCTION node-typings of the same concept |
| `membrane fluidity` | PATO:0001985 (viscosity) | viscosity is closely related but is a generic physical quality; membrane-specific lipid-mobility sense has no exact upstream term |

### Node-typing notes

Three of these are *mis-typed* in the corpus (a separate cleanup):
- `proton motive force` and `membrane fluidity` appear under
  `node_type: BIOLOGICAL_PROCESS` but are semantically a
  bioenergetic state and a membrane quality respectively.
- `microbial biomass` and `reducing power` are typed as
  `BIOLOGICAL_PROCESS` / `CHEMICAL` but are aggregate matter and
  capacity respectively.

Lifting them to METPO with proper classification gives downstream
re-typing migrations a target. The mapping TSV in this PR grounds
them via the corpus's current (mis-)typing so the corpus-side fix
can land separately.

## Hierarchy decisions

All 6 are siblings under `METPO:1000000`. They are **not** mutually
disjoint — `reducing power` is a kind of `inorganic electron donor`
when realized as H₂, and `terminal electron acceptor` overlaps
with `microbial biomass` in fermentative dispoportionation. The
intentional flatness defers these refinements to a future cohort
once METPO grows a richer mid-level taxonomy.

## ID space and subset

| Range | Use |
|---|---|
| `METPO:1007500`–`METPO:1007505` | v3 class block (allocated; first 6 IDs of the `1007500+` placeholder range) |

Subset tag: **`metpo_traitmech_2026_07`** (forward-dated relative to
the May 2026 v1 + v2 cohorts; per the `metpo-proposal` skill, each
new cohort directory gets a new subset tag).

Collision check: `grep "METPO_1007[45][0-9][0-9]" data/raw/metpo.owl`
→ 0 hits.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `proposal.md` | this file | Reviewer narrative |
| `metpo_proposal_classes_robot.tsv` | 8 (2 header + 6 class) | Submittable ROBOT-template artifact |

No `metpo_proposal_properties_robot.tsv` — no predicates in v3.

## Verification

```
$ just verify-proposal metpo_traitmech_v3
  classes TSV: 8 rows
  scope-A: no traitmech:NNNNNN ids in corpus (nothing to cover)
  scope-C: CausalNodeTypeEnum not lifted in this cohort (skip)
  failures: 0
  status:   PASS

$ just robot-validate-proposal metpo_traitmech_v3
  merged.owl lines:    8425
  reasoned.owl lines:  8431
  delta:               +6
  status:              PASS (no UNSAT, ELK exited 0)
```

## Corpus impact

After applying `mappings/node_grounding.tsv` (with this cohort's
10 new mappings: 6 METPO + 1 GO + 3 alias rows for terminal-acceptor
CHEMICAL/MF dual-typing and the GO carotenoid biosynthesis):

|  | Before v3 | After v3 |
|---|---:|---:|
| Nodes grounded | 564 | 622 |
| Nodes residual | 688 | 630 |
| Distinct (label, type) residuals | 511 | 503 |
| Mappings TSV size | 39 rows | 49 rows |

The remaining 630-node residual is dominated by:
- protein-family / gene-product labels (`MreB`, `FtsZ`, `RuBisCO`,
  `DivIVA`, `Na+/H+ antiporter`, etc.) — should ground to PRO or
  UniProt, not METPO.
- ENVIRONMENTAL_FACTOR pH / NaCl variants
  (`acidic external pH`, `near-neutral external pH`, etc.) — could
  be a future ENVO/PATO mapping cohort.
- Long tail of low-frequency curator paraphrases (≤2 nodes each).

## Upstream path

Per the established TraitMech convention for v1 + v2, this cohort
is **not filed upstream in this PR**. The cohort lives in this
repo for review and to enable corpus-side grounding to reference
the proposed CURIEs ahead of upstream adoption.

When ready to file upstream:

1. Confirm v1 + v2 cohorts are also being filed (this cohort's
   proposed classes are parented at `METPO:1000000` and don't
   depend on v1/v2 IRIs, but reviewers will want the full
   TraitMech lift in context).
2. Open an issue at <https://github.com/berkeleybop/metpo> with
   `metpo_proposal_classes_robot.tsv` attached.
3. After upstream mints real `METPO:1007500`-range IDs (or a
   different block), refresh `data/raw/metpo.owl`, update
   `mappings/node_grounding.tsv` with the upstream CURIEs, and
   re-run `just ground-nodes --apply`.

## Round-trip plan

The grounding script (`scripts/ground_causal_nodes.py`) never
overwrites existing `grounding:` values, so a post-upstream CURIE
swap requires either:

1. A one-off migration script that clears `grounding:` on nodes
   bearing v3 placeholder METPO CURIEs, OR
2. A direct text substitution across `data/traits/**/*.yaml`
   (safe because the placeholder CURIEs `METPO:1007500`–
   `METPO:1007505` don't appear elsewhere in the corpus).

After re-grounding, re-run `just validate-strict` (CI-enforced via
`.github/workflows/validate-strict.yaml`).

## Change log

- **v3 (2026-07)** — 6 new METPO classes covering 58 of 630
  residual causal-graph nodes; subset `metpo_traitmech_2026_07`.
  First "Scope D" cohort (node-class lift).
