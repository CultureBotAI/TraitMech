# TraitMech Curation Playbook

Conventions for curating a `TraitRecord` YAML up to
`mapping_status: REVIEWED` with a DOI-backed `causal_graphs` block.
Extracted from the experience of curating 233 records across PRs
#24–#46.

This is a **practical guide**, not the formal schema — see
`src/traitmech/schema/traitmech.yaml` for what is structurally valid.
This playbook describes what reviewers (human and Copilot) will flag
beyond raw schema validity.

## What gets a causal graph

Add a `causal_graphs:` block **only when the trait has source-backed
mechanism structure**. Three healthy use cases:

1. **Concrete phenotype with literature mechanism** — e.g.,
   `halophilic`, `aerobic`, `thermophilic`. Build a 5–7 node graph
   with environmental factor → mechanism → trait edges.
2. **Umbrella class with a regulatory or developmental program** —
   e.g., `sporulation`, `metabolism`, `gc_content`. Build a graph
   that names the program and optionally includes `is a` edges to
   grounded child phenotypes.
3. **Quantitative bin** — e.g., `nacl_optimum_high`,
   `temperature_range_mid2`. Build a compact 3–4 node graph linking
   the numeric range (from the METPO synonym) to a representative
   mechanism, with a single `is a` edge back to the umbrella.

**Skip causal graphs when:**

- The record is `term_kind: OBJECT_PROPERTY` or
  `DATATYPE_PROPERTY` (relation carrier) → typically `DEPRECATED`.
- The record is an administrative/regulatory classification with no
  biological mechanism (e.g., `biosafety_level_1` deserves a thin
  hazard-classification graph but is not a phenotype mechanism).

## File-level structure

Order fields in this sequence (matches what merged PRs use):

```yaml
identifier: METPO:XXXXXXX
label: ...
definition: ...
definition_source: DOI:...
trait_category: ...
term_kind: CLASS
mapping_status: REVIEWED      # promote from SEEDED when curating
parent_traits:
- METPO:XXXXXXX
synonyms: [...]               # if any
created_by: ...               # if seeded with one
evidence:
- reference: DOI:...
  snippet: <verbatim phrase>
  notes: <what the snippet supports>
causal_graphs:
- graph_id: ...
  title: ...
  description: ...
  nodes: [...]
  edges: [...]
curation_history:
- timestamp: ...
  curator: seed_from_metpo
  action: SEEDED_FROM_METPO
  ...
- timestamp: <today>
  curator: claude            # or codex or human name
  action: CURATED_CAUSAL_GRAPH
  changes: <one-sentence summary of what was added>
  llm_assisted: true
```

## Definitions

- **Always set `definition_source`** to a DOI/PMID that supports the
  definition.
- **Bin records** without an upstream definition: derive one from the
  synonym threshold, e.g. synonym `NaO_>8` →
  *"NaCl optimum phenotype with best-growth NaCl concentration above
  approximately 8% (w/v)..."*.
- **Inherited grammar bugs**: fix subject-verb agreement and similar
  issues from the upstream seed (e.g., `"that pose"` → `"that poses"`).
  Copilot flags these consistently.
- **Match the synonym's numeric semantics**: if synonym says
  `pHd_5_9`, the definition says "5–9 pH units", not "above ~5"
  (Copilot flagged this on PR #32).

## Top-level `evidence:` block

Two to three entries are ideal. Each is a DOI/PMID, a **verbatim**
snippet, and a `notes:` line explaining what it supports.

- One entry should support the **definition**.
- One entry should support the **mechanism** appearing in the causal
  graph.
- For trait records of well-known biology, **add a representative
  organism example** as a third entry (PMID-backed), following
  `halophilic.yaml` / `aerobic.yaml`. This is high-value and
  Copilot does not require it, but it makes the record genuinely
  useful downstream.

## Causal graph mechanics

### `graph_id`, `title`, `description`

- `graph_id`: short, lowercase, underscore-separated, distinct across
  the repo. Pattern: `<trait_slug>_<mechanism_keyword>`.
- `title`: 5–7 words, human-readable.
- `description`: 1–2 sentences. **Must match what the graph actually
  models** — Copilot will flag if the description mentions a
  node/edge that isn't there. Recurring pitfall.

### Nodes

Required: `node_id` (unique within the graph), `label`,
`node_type`. Optional: `grounding` (CURIE), `description`.

**Pick the right `node_type`:**

| If the node represents… | Use |
|---|---|
| The trait itself | `TRAIT` with `grounding: METPO:...` |
| Another grounded trait (`is a` child, sibling) | `TRAIT` with `grounding: METPO:...` |
| Ambient temperature/pH/NaCl/light/nutrient level | `ENVIRONMENTAL_FACTOR` |
| A biological process (e.g., osmotic balance, cytokinesis) | `BIOLOGICAL_PROCESS` |
| A named enzyme / protein / pathway component | `GENE_OR_PROTEIN` |
| A small-molecule (with optional `CHEBI:` grounding) | `CHEMICAL` |
| A cell-envelope structure, membrane, sacculus | `CELLULAR_LOCALIZATION` |
| A non-membrane organelle (e.g., endospore) | `ORGANELLE` |
| Laboratory practice / containment / experimental design | `EXPERIMENTAL_FACTOR` |
| A molecular role (e.g., "terminal electron acceptor") | `MOLECULAR_FUNCTION` |

**Established convention: the bacterial cell wall is
`CELLULAR_LOCALIZATION`** with `node_id: peptidoglycan_cell_wall`
(and ideally `grounding: GO:0009274`). Do **not** use `ORGANELLE`
for the cell wall — see PR #26 / #44 precedent.

**TRAIT labels** should match the canonical METPO label of the
trait being grounded — no stray `" phenotype"` suffix beyond what
METPO has (Copilot flagged this on PR #25).

**Every defined node must be referenced by at least one edge.**
Orphan nodes get dropped by the page renderer and Copilot flags
them. If a node feels orphan-y, either wire it in or remove it.

### Edges

Required: `subject`, `predicate`, `object`. Always include `evidence`
on causal edges — every edge needs at least one DOI/PMID-backed
support.

**Predicate vocabulary** (reuse for cross-trait consistency):

| Predicate | Use for |
|---|---|
| `selects for` | environment → trait (selection pressure) |
| `causes` / `triggers` / `produces` / `drives` | environment/factor → response |
| `enables` / `supports` / `contributes to` | mechanism → trait |
| `requires` | strict dependency |
| `maintains` / `mitigates` / `limits` | adaptive responses |
| `protects against` | defensive mechanisms |
| `has mechanistic process` | trait → defining process |
| `acts as` | role assignment |
| `manifests as` | mechanism → trait endpoint |
| `is a` | bin → umbrella, child → parent class |
| `defines` | axis variable → quantitative phenotype |

**Verb form: always third-person singular.** `enables`, not
`enable`. `delivers`, not `deliver`. `confers`, not `confer`.
`specializes`, not `specialize`. **No snake_case predicates** —
use spaces (`combines with`, not `combines_with`).

### Evidence on edges

- **Always include a `reference:`** (DOI/PMID/CHEBI/GO/METPO).
- **The `snippet:` should be a verbatim, contiguous quote** from
  the cited source (no ellipsis, no paraphrase). Copilot flags
  ellipses and paraphrased fragments.
- **Snippets must support the specific edge claim.** If three edges
  all cite the same review with the same one-word snippet, Copilot
  will flag low diversity. Each edge needs a distinct verbatim
  phrase that actually supports *that* edge's assertion. See PRs
  #28, #29, #32, #44 for examples.
- **The `notes:` line** explains *how* the snippet supports the
  claim — not a paraphrase of the snippet, but the reasoning
  linking quote to edge.

## Curation history

Append a `CurationEvent` for each significant change. Use these
canonical action names:

- `SEEDED_FROM_METPO` (the auto-import event; never write this
  yourself)
- `CURATED_WITH_LITERATURE` (added definition/evidence from sources)
- `CURATED_WITH_ORGANISM_EXAMPLE` (added a PMID organism example)
- `CURATED_CAUSAL_GRAPH` (added or revised the causal graph)
- `DEPRECATED_PROPERTY_RECORD` (marked a relation carrier as
  superseded)

Set `llm_assisted: true` when an LLM helped generate the content.

## Bin records (umbrella + child pattern)

Quantitative-bin records (`*_optimum_*`, `*_range_*`, `*_delta_*`)
share a recipe used across PRs #26, #31–#33:

1. The umbrella (`*_optimum`, `*_range`, `*_delta`) gets a full
   mechanism graph (5–7 nodes).
2. Each bin gets a compact graph (3–4 nodes) with:
   - The bin itself as a `TRAIT` node grounded to its METPO ID.
   - The umbrella as a `TRAIT` node grounded to the umbrella's
     METPO ID.
   - One mechanism node specific to the bin's range.
   - One `is a` edge from bin → umbrella.
3. Bin definitions are derived from the synonym threshold and cite
   one of the references used in the umbrella.

## Cross-axis / numerical-limits umbrellas

`*_phenotype_with_numerical_limits` records and their three-axis
parents (`optimum_phenotype_with_numerical_limits` etc.) get a
thin graph: an `ENVIRONMENTAL_FACTOR` axis node plus three
axis-specific `TRAIT` children (e.g., `nacl_optimum`, `ph_optimum`,
`temperature_optimum`) connected by `is a` edges and a single
`defines` edge from the axis to the umbrella.

## Common Copilot review items

The reviewer (`Copilot`) reliably catches:

1. **Bare-verb predicates** — `enable` instead of `enables`,
   `confer` instead of `confers`.
2. **Verbatim-quote violations** — snippets with ellipsis or
   paraphrase.
3. **Orphan nodes** — defined but never used in an edge.
4. **Low snippet diversity** — same short snippet across many edges
   of a single graph (a single repeated word like "virulence
   factors" or "type III secretion").
5. **Description / graph mismatch** — graph description claims a
   mechanism the graph doesn't actually model.
6. **Inappropriate node types** — `BIOLOGICAL_PROCESS` for things
   that are not processes (e.g., lab equipment, classifications).
7. **Cell-wall node convention** — `ORGANELLE` instead of
   `CELLULAR_LOCALIZATION` for the peptidoglycan wall.
8. **TRAIT label drift** — adding `" phenotype"` to a TRAIT node
   label when the METPO trait it grounds to doesn't carry that
   suffix.
9. **Subject-verb agreement** in inherited METPO definitions
   ("that pose" → "that poses").
10. **Numeric definitions** not matching the synonym threshold
    (e.g., "above ~5" when the synonym says `pHd_5_9`).

## Workflow

```bash
just install
just gen-schema                       # if schema changes
git checkout -b add-<theme>-causal-graphs
# ... edit records ...
just validate data/traits/<cat>/<file>.yaml      # spot-check
just validate-all                                # before commit
git add -p && git commit
git push -u origin <branch>
gh pr create --title "..." --body "..."
gh api repos/CultureBotAI/TraitMech/pulls/<N>/requested_reviewers \
  -X POST --input - <<<'{"reviewers":["Copilot"]}'
# wait for Copilot review, address, resolve threads, merge --delete-branch
```

**Branch hygiene**: always `git checkout main && git pull` before
creating a new feature branch. Otherwise the new branch will carry
prior PR commits and the diff scope leaks (this happened on PR #27,
and was a recurring issue in the early environment PRs).

## Verification

Before opening a PR:

- [ ] `just validate <file>` passes on every modified YAML.
- [ ] `just validate-all` is clean (catches schema regressions).
- [ ] Definitions match synonym thresholds for bin records.
- [ ] Every causal edge has at least one DOI/PMID-backed evidence.
- [ ] Evidence snippets are verbatim and diversified across edges.
- [ ] `mapping_status` set to `REVIEWED`.
- [ ] `curation_history` event appended with today's date.

## Reference: example records to study

- **Concrete phenotype**: `data/traits/environment/halophilic.yaml`,
  `data/traits/environment/aerobic.yaml`,
  `data/traits/morphology/sporulation.yaml`.
- **Umbrella with children**: `data/traits/physiology/trophic_type.yaml`,
  `data/traits/environment/oxygen_preference.yaml`.
- **Cross-axis numerical-limits umbrella**:
  `data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.
- **Quantitative bin**: `data/traits/environment/nacl_optimum_high.yaml`,
  `data/traits/morphology/cell_length_large.yaml`.
- **Negation/loss-of-function phenotype**:
  `data/traits/morphology/non_motile.yaml`,
  `data/traits/morphology/non_spore_forming.yaml`.
- **Classification axis (non-mechanistic)**:
  `data/traits/ecology/biosafety_level.yaml`.

When in doubt, mirror the closest example above and adapt the
mechanism, references, and bin thresholds.
