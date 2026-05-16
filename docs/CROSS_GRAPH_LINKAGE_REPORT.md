# Cross-graph mechanism linkage report

A survey across all 233 REVIEWED records and their 1,252 graph nodes
to find mechanism nodes defined independently in multiple causal
graphs. Each entry below is a label that appears in **≥3 distinct
graphs** under a mechanism-bearing node type (`BIOLOGICAL_PROCESS`,
`GENE_OR_PROTEIN`, `CHEMICAL`, `CELLULAR_LOCALIZATION`,
`ENVIRONMENTAL_FACTOR`, `ORGANELLE`, `MOLECULAR_FUNCTION`,
`EXPERIMENTAL_FACTOR`).

This report has three purposes:

1. **Confirm what's already grounded consistently** — these are the
   robust shared nodes that downstream KG integrations can rely on.
2. **Surface inconsistent groundings or types** for normalisation.
3. **Propose candidate shared groundings** for recurring mechanism
   nodes that are currently ungrounded.

## Already grounded consistently (no action needed)

These 11 labels are used in ≥3 graphs and carry the **same**
grounding everywhere they appear:

| Label | Node type | Grounding | # graphs |
|---|---|---|---:|
| molecular oxygen | `CHEMICAL` | `CHEBI:15379` | 16 |
| carbon dioxide | `CHEMICAL` | `CHEBI:16526` | 16 |
| proton | `CHEMICAL` | `CHEBI:15378` | 8 |
| reactive oxygen species | `CHEMICAL` | `CHEBI:26523` | 5 |
| molecular hydrogen | `CHEMICAL` | `CHEBI:18276` | 5 |
| aerobic respiration | `BIOLOGICAL_PROCESS` | `GO:0009060` | 4 |
| sodium ion | `CHEMICAL` | `CHEBI:29101` | 3 |
| potassium ion | `CHEMICAL` | `CHEBI:29103` | 3 |
| carbon monoxide | `CHEMICAL` | `CHEBI:17245` | 3 |
| acetate | `CHEMICAL` | `CHEBI:30089` | 3 |
| ATP (post-normalisation) | `CHEMICAL` | `CHEBI:30616` | 22 |

## Normalised in this PR

These had small inconsistencies; the PR brings them to a single
canonical form.

### ATP grounding

**Before**: 20 graphs grounded `ATP` to `CHEBI:30616`; 2 graphs
(`metabolism/fermentation`, `metabolism/oxidative_phosphorylation`)
grounded it to `CHEBI:15422`, which is the ATP(4−) anion specifically.

**After**: All 22 occurrences grounded to `CHEBI:30616` (ATP).

### `peptidoglycan cell wall` GO grounding

**Before**: 4 graphs name a `peptidoglycan cell wall` node typed
`CELLULAR_LOCALIZATION`; only 1 carried `grounding: GO:0009274`,
the other 3 (`morphology/cell_shape`, `morphology/gram_stain`,
`morphology/sphere_shaped`) were ungrounded.

**After**: All 4 carry `grounding: GO:0009274`.

### `peptidoglycan cell wall` legacy `ORGANELLE` type

**Before**: `morphology/pleomorphic_shaped.yaml` had a
`weak_cell_wall` node grounded to `GO:0009274` but typed `ORGANELLE`,
contradicting the established convention (PR #26 / #44) that the
peptidoglycan cell wall is `CELLULAR_LOCALIZATION`.

**After**: Retyped to `CELLULAR_LOCALIZATION`. This was the only
remaining legacy case.

### `catabolism` GO grounding

**Before**: 5 graphs name a `catabolism` node typed
`BIOLOGICAL_PROCESS`; only 1 carried `grounding: GO:0009056`,
the other 4 (`physiology/chemoheterotrophic`,
`physiology/chemoorganoheterotrophic`, `physiology/heterotrophic`,
`physiology/organotrophic`) were ungrounded.

**After**: All 5 carry `grounding: GO:0009056`.

## Surfaced for future work (not fixed in this PR)

### `terminal electron acceptor` — node-type disagreement

5 graphs use this label, but with two different `node_type`s:

- 2 graphs (e.g. `environment/aerobic`) type it as
  `MOLECULAR_FUNCTION` with descriptions framing it as a role
  ("Functional role played by oxygen in aerobic respiration").
- 3 graphs (`metabolism/respiration`, `physiology/chemoorganotrophic`,
  `physiology/chemotrophic`) type it as `CHEMICAL` with descriptions
  framing it as the substance ("Oxidized acceptor receiving
  electrons").

These are semantically distinct concepts that happen to share a
label. The clean fix is to either (a) split the role and substance
in the 3 CHEMICAL-typed graphs into two nodes, or (b) standardise on
`MOLECULAR_FUNCTION` and update node descriptions to match. Deferred
because the fix requires non-trivial description rewrites and
possibly edge restructuring; tracked here so a future PR can
revisit.

### Candidate shared groundings for currently-ungrounded recurring nodes

These nodes recur in ≥4 graphs but carry no grounding. Each is a
candidate for a shared CURIE; this report does not change them —
the proposals are starter suggestions for a future grounding-pass
PR (and may need refinement against the most-specific GO/CHEBI/PRO
term).

| Label | # graphs | Type | Proposed grounding |
|---|---:|---|---|
| proton motive force | 16 | `BIOLOGICAL_PROCESS` | `GO:0015988` (proton motive force-driven ATP synthesis) or `GO:1902600` (proton transmembrane transport) — neither is exact; "proton motive force" itself is more an *entity* than a process. May warrant a TraitMech-local term. |
| biomass | 16 | `BIOLOGICAL_PROCESS` | Abstract — leave ungrounded or move to a TraitMech-local concept. |
| cytoplasmic pH homeostasis | 11 | `BIOLOGICAL_PROCESS` | `GO:0030641` (regulation of cellular pH) — close fit. |
| compatible solutes | 7 | `CHEMICAL` | `CHEBI:88061` (osmolyte) — group, not exact. |
| inorganic electron donor | 7 | `CHEMICAL` | No clean CHEBI term; leave ungrounded. |
| membrane fluidity | 6 | `BIOLOGICAL_PROCESS` | Not a GO process per se; this is really a *quality* (PATO?). |
| precursor metabolites | 6 | `CHEMICAL` | Abstract — leave ungrounded. |
| organic compound | 6 | `CHEMICAL` | `CHEBI:50860` (organic molecular entity). |
| light | 6 | `ENVIRONMENTAL_FACTOR` | No standard CURIE in active use. |
| osmotic stress | 5 | `BIOLOGICAL_PROCESS` | `GO:0006970` (response to osmotic stress). |
| MreB | 4 | `GENE_OR_PROTEIN` | UniProt per organism (e.g., `UniProtKB:P0A9X4` for E. coli MreB) — but the node is typically generic across taxa. |
| peptidoglycan synthesis | 4 | `BIOLOGICAL_PROCESS` | `GO:0009252` (peptidoglycan biosynthetic process). |
| rod-complex peptidoglycan synthesis | 4 | `BIOLOGICAL_PROCESS` | More specific than GO:0009252; no clean CURIE. |
| septal peptidoglycan synthesis | 4 | `BIOLOGICAL_PROCESS` | `GO:0043093` (FtsZ-dependent cytokinesis) — partial fit. |
| ferrous iron | 4 | `CHEMICAL` | `CHEBI:29033` (iron(2+)). |
| reducing power | 4 | `CHEMICAL` | Abstract — leave ungrounded. |
| Na+/H+ antiporter | 3 | `GENE_OR_PROTEIN` | `GO:0015385` (sodium:proton antiporter activity) — a molecular function term, not exactly a protein. |
| FtsZ | 3 | `GENE_OR_PROTEIN` | UniProt per organism (e.g., `UniProtKB:P0A9A6` for E. coli FtsZ). |
| DivIVA | 3 | `GENE_OR_PROTEIN` | UniProt per organism (e.g., `UniProtKB:O32093` for Bacillus subtilis DivIVA). |
| RubisCO | 3 | `GENE_OR_PROTEIN` | UniProt per organism, multiple chains/subunits. |
| photosynthetic reaction center | 3 | `GENE_OR_PROTEIN` | `GO:0009523` (photosystem II) / `GO:0009522` (photosystem I) — but this is a complex, not a single gene. |
| chemotaxis signaling | 3 | `BIOLOGICAL_PROCESS` | `GO:0006935` (chemotaxis). |

## Survey method

```python
# For each TraitRecord YAML under data/traits/, walk causal_graphs.
# Collect every node with its (cat, file, graph_id, node_id, label,
# node_type, grounding). Group by lowercase label; only include
# labels in mechanism-bearing node types (BIOLOGICAL_PROCESS,
# GENE_OR_PROTEIN, CHEMICAL, CELLULAR_LOCALIZATION,
# ENVIRONMENTAL_FACTOR, ORGANELLE, MOLECULAR_FUNCTION,
# EXPERIMENTAL_FACTOR). Report labels appearing in ≥3 distinct
# (file, graph_id) pairs.
```

This script is intentionally not committed; rerunning the survey
in the future can be a one-off ad-hoc check rather than a CI
artefact.

## Coverage

- Total node instances surveyed: **1,252**
- Total causal graphs: **233**
- Recurring labels (≥3 graphs): **54**
- Recurring labels with consistent grounding: **11**
- Recurring labels needing normalisation (this PR): **4**
- Recurring labels with grounding candidates noted but not changed: **22**

## Why this matters

Each independently-defined node weakens cross-graph integration: a
downstream consumer querying for "all traits whose mechanism
involves the proton motive force" sees 16 graphs, each with its
own `proton_motive_force` node, each with its own description.
Canonicalising the recurring mechanism nodes (by grounding) lets
downstream tools see one shared concept across all 16 graphs.

The fixes in this PR move 4 such concepts (ATP, peptidoglycan
cell wall × 2 normalisations, catabolism) to a single canonical
form. The 22 proposals above are starter suggestions for the
**next** grounding pass.
