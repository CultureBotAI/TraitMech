# Canonical Example (metpo_traitmech_v1)

*Reference for the **metpo-proposal** skill — see [`../SKILL.md`](../SKILL.md) for the overview, scopes, ID-space conventions, and workflow.*

---

## Canonical example

`proposals/metpo_traitmech_v1/` — the first TraitMech cohort, lifting the
trait-causal-graph scaffold. Read it end-to-end before writing a new cohort;
every convention in this skill is instantiated there.

**v1 contents (14 class rows, 0 predicate rows):**

| ID block | Coverage |
|---|---|
| `METPO:1007400`–`1007402` | Top-level domain classes (`trait causal graph`, `trait causal node`, `trait causal edge`) lifting LinkML classes `CausalGraph`, `CausalNode`, `CausalEdge`. |
| `METPO:1007410` | Enum-parent (`trait causal node type`) under `trait causal node`. |
| `METPO:1007411`–`1007420` | All 10 `CausalNodeTypeEnum` permissible values as leaves (TRAIT, PATHWAY, ENVIRONMENTAL_FACTOR, EXPERIMENTAL_FACTOR, GENE_OR_PROTEIN, CHEMICAL, ORGANELLE, CELLULAR_LOCALIZATION, MOLECULAR_FUNCTION, BIOLOGICAL_PROCESS). |

Subset tag: `metpo_traitmech_2026_05`. Verified clean by
`just verify-proposal metpo_traitmech_v1` (column counts, header
directives, parent integrity, subset tag, Scope-A and Scope-C coverage all
pass).

**What v1 deliberately omits:**

- **Scope A** is empty — the corpus has zero `traitmech:NNNNNN` IDs at the
  time of drafting. As curators begin minting fallback IDs, add them via
  **Path B (extend in place)** with a contiguous block at `1007430+`.
- **Scope B** is empty — but **not because the corpus is well-grounded**.
  An audit at v1 time found `0/1019` causal edges have a `predicate_id`;
  the `predicate` field carries 218 distinct free-text labels. Most top
  labels (`enables`, `causes`, `contributes to`, …) have RO homes already,
  and a few (`produces`, `uses as carbon source`, `oxidizes`) already exist
  in METPO. Drafting a Scope-B cohort today would propose ~200 predicates
  alongside ones that should be RO-grounded — wrong direction.
  **The correct prerequisite is a data-side predicate-grounding migration**
  (populate `predicate_id` from RO/METPO where matches exist). Only the
  residual that has no upstream home (`manifests as`, `selects for`,
  `feeds electrons into`, `uses electron donor`, …) becomes a Scope-B
  candidate. Add those via Path B (extend v1) at `2007400+` after grounding
  completes.

The structural template — Aristotelian definitions, OBO xrefs without
equivalence claims, contiguous ID blocks per logical group, single subset
tag, flat hierarchy under the enum-parent — is exactly what subsequent
cohorts should follow. A cross-Mech reference for a heavier proposal (9
enums + 14 predicates) is
`CommunityMech`: `proposals/metpo_communitymech_v1/`.
