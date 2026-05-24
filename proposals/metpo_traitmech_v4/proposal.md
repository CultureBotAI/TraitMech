# METPO ROBOT Template Proposal — TraitMech Predicate Lift (v4, 2026-08)

## Context

Follow-on to the v2 predicate cohort (`metpo_traitmech_v2`, 8
predicates). The v2 cohort closed out the largest semantically
coherent clusters of the predicate residual; this v4 cohort picks
up the next-most-prevalent single residual label
(`defines`, 14 edges).

`defines` is an operationally-definitional predicate used uniformly
across the delta / range / optimum phenotype graphs: an
environmental measurement axis (or condition) **defines** the
phenotype variable it parameterizes (e.g. *"external pH axis
defines pH phenotype with numerical limits"*).

## Scope

| Scope | # rows | Lift status |
|---|---:|---|
| A (synthetic trait classes) | 0 | not applicable |
| B (causal-graph predicates) | **1 predicate / 14 edges** | included |
| C (controlled vocabularies) | 0 | already covered in v1 |
| D (node-class abstractions) | 0 | covered in v3 |

Total property rows in v4: **1**.

## Predicate proposal

| ID | Label | Edges grounded | Domain | Range |
|---|---|---:|---|---|
| `METPO:2007500` | defines | 14 | `METPO:1007401` | `METPO:1007401` |

### Why not an existing predicate?

| Considered | Why rejected |
|---|---|
| `biolink:has_phenotype` | Wrong direction (phenotype is the object here, not the holder). |
| `biolink:related_to` | Too weak — `defines` is an operationally-definitional claim, not a generic association. |
| `RO:0000087` (has role) | Mismatched semantics — the axis isn't a role of the phenotype. |
| `METPO:2007401` (selects for) | Evolutionary selection, not operational definition. |
| `rdfs:subClassOf` / `is a` | The axis is not a subclass of the phenotype; it's the input dimension. |

The 14 uses cluster tightly: every one is an `<axis> defines
<phenotype with numerical limits>` pattern from the delta / range
/ optimum trait graphs.

## ID space and subset

| Range | Use |
|---|---|
| `METPO:2007500` | v4 predicate block (first ID of the `2007500+` fresh block; v2 used `2007400–2007407`) |

Subset tag: **`metpo_traitmech_2026_08`** (forward-dated relative
to v2's `2026_06` and v3's `2026_07`).

Collision check: `grep "METPO_2007500" data/raw/metpo.owl` → 0
hits.

## Files

| File | Rows | Purpose |
|---|---:|---|
| `proposal.md` | this file | Reviewer narrative |
| `metpo_proposal_properties_robot.tsv` | 3 (2 header + 1 predicate) | Submittable ROBOT-template artifact |

No `metpo_proposal_classes_robot.tsv` — no new classes in v4.

## Verification

```
$ just verify-proposal metpo_traitmech_v4
  failures: 0
  status:   PASS

$ just robot-validate-proposal metpo_traitmech_v4
  merged.owl lines:    8328
  reasoned.owl lines:  8334
  delta:               +6
  status:              PASS (no UNSAT, ELK exited 0)
```

## Corpus impact

After applying `mappings/predicate_grounding.tsv` (with the
`defines → METPO:2007500` addition):

|  | Before v4 | After v4 |
|---|---:|---:|
| Edges grounded | 688 | 702 |
| Edges residual | 331 | 317 |
| Distinct residual labels | 177 | 176 |
| Mappings TSV | 38 rows | 39 rows |

## Upstream path

Per the established TraitMech convention (v1, v2, v3), this cohort
is **not filed upstream in this PR**. When ready, file at
<https://github.com/berkeleybop/metpo> alongside the v1/v2/v3
cohorts.

## Change log

- **v4 (2026-08)** — 1 new METPO predicate (`defines`) covering 14
  of 331 residual causal-edge predicates; subset
  `metpo_traitmech_2026_08`.
