---
description: Deep-research the ungrounded causal-graph predicates/nodes; ground to METPO first (else RO/OBO), and where no good term exists, draft a METPO proposal.
argument-hint: "[predicates|nodes] [min-freq N | category C | label \"...\"]  (default: both, min-freq 2)"
---

# Ground-or-propose residual causal-graph terms (METPO-first)

Goal: shrink the ungrounded residual left after the matchers, by **deep-researching
each recurring residual term** and either (a) grounding it to an existing ontology
term — **METPO first**, then RO/OBO — or (b) drafting a **METPO proposal** when no good
existing term exists. Maximize METPO coverage; mint only when nothing fits.

`$ARGUMENTS` selects scope (default: both predicates and nodes, only labels with
edge/node count ≥ 2; skip the freq-1 long tail). Examples:
`/ground-or-propose-metpo predicates min-freq 3` · `/ground-or-propose-metpo nodes category metabolism`.

## Inputs (read these)
- **Residual to work:**
  - Predicates: `reports/predicate_grounding_residual.tsv` (cols: `predicate_label`, `edge_count`, `example_files`).
  - Nodes: `reports/node_grounding_residual.tsv` (cols: `node_label`, `node_type`, `node_count`, `example_files`).
  Filter to the requested scope + min-freq; rank by frequency (highest first).
- **Context/evidence per term:** the trait's Edison report at
  `research/traits/<category>/<slug>-deep-research-falcon.md` (the `example_files` point you to the trait),
  and the trait YAML `data/traits/<category>/<slug>.yaml` (how the term is actually used in the graph).
- **METPO term inventory (search FIRST):**
  - In-repo: every `data/traits/**/*.yaml` with `term_kind: OBJECT_PROPERTY` (predicates) or `term_kind: CLASS` (nodes) and an `identifier: METPO:…` — match on `label` + `synonyms`.
  - Full ontology: `data/raw/metpo.owl` (local) and the latest release `https://w3id.org/metpo/metpo.owl` (BioPortal-equivalent) for terms not yet seeded into the corpus.
- **Where groundings/proposals go:** `mappings/predicate_grounding.tsv`, `mappings/node_grounding.tsv`; new proposal cohort under `proposals/`.
- **Conventions:** the `metpo-proposal` and `manage-identifiers` skills (METPO-first policy, ID reservation, ROBOT-template format, citation-vs-mapping rule).

## Procedure

### 1. Build the worklist
Load the residual for the requested scope, apply min-freq/category/label filters, and
**deduplicate by meaning** (e.g. `c-di-GMP`, `cyclic di-GMP`, `c_di_gmp` are one concept).
Drop terms that are clearly graph-narrative artifacts, not reusable concepts
(`maximal growth rate`, `baseline mesophile adaptation`, vague verbs like `engages`,
`realizes`, `positions`) — record these as `skipped: non-ontological`.

### 2. Deep-research each concept — **use the `cc deep-research` command**
For each concept (batch related ones into one question), invoke the Claude Code
**`deep-research`** skill (`/deep-research`) with a tightly-scoped question, e.g.:

> Deep-research the microbial-trait concept **"<term>"** (used as a causal-graph
> <predicate|node of type T>; context: <one line from the trait/Edison report>).
> 1. Does the **METPO** ontology (https://w3id.org/metpo/metpo.owl, BioPortal "METPO")
>    contain a class/relation for this concept? Give the exact `METPO:` CURIE + label,
>    and whether it is an exact, broad, narrow, or close match.
> 2. If METPO has none, is there a standard term in **RO** (relations), **biolink**
>    (predicates), or **CHEBI/GO/ENVO/PATO** (nodes)? Give the CURIE + match strength.
> 3. If neither has a good match, state that explicitly and propose a one-line
>    Aristotelian definition + the most likely METPO parent class for a new term.
> Prefer authoritative ontology sources; cite OLS/BioPortal/OBO. Be decisive about
> match strength; flag if the concept is too vague/idiosyncratic to be an ontology term.

Treat the existing Edison report as supporting evidence, but the **`deep-research`
command is the ontology-lookup authority** here.

### 3. Decide per concept (in this priority order)
1. **Strong METPO match** (exact/close, same concept) → record a grounding to the `METPO:` CURIE. *Maximize this — it is the whole point.*
2. **No METPO, but strong RO/OBO match** (RO/biolink for predicates; CHEBI/GO/ENVO/PATO for nodes) → record a grounding to that CURIE (better to reuse a real term than mint).
3. **No good existing term anywhere**, but the concept is **generic + recurring + reusable** → **METPO proposal** (new term).
4. **Vague / idiosyncratic / one-off** → leave residual; do not force a match or mint a term.

Verify every chosen CURIE actually resolves to that label (catch typos / obsolete terms)
— for OAK-resolvable prefixes, the `label-correspondence` gate will re-check, but don't
rely on it for METPO.

### 4. Apply
- **Groundings** → append rows to the mapping TSVs (keep column structure incl. the skos
  `predicate_id` strength column):
  - `mappings/predicate_grounding.tsv`: `label, target_curie, target_label, predicate_id(skos:*Match), source, confidence, notes`
  - `mappings/node_grounding.tsv`: `label, node_type, target_curie, target_label, predicate_id(skos:*Match), source, confidence, notes`
  Then run `just` grounders to write them into the YAMLs:
  `uv run python scripts/ground_causal_predicates.py --apply` and
  `uv run python scripts/ground_causal_nodes.py --apply`.
- **Proposals** → follow the `metpo-proposal` skill: a fresh cohort
  `proposals/metpo_traitmech_v8/` (next after v7), ROBOT-template rows for the new
  classes/predicates with Aristotelian definitions, parents, `definition_source` =
  `TraitMech:data/traits/<…>` (citations only — equivalents go to `xrefs`/SSSOM, per
  issue #83), placeholder IDs in the reserved range **above v7** (classes `1007722+`,
  predicates `2007604+`), verified collision-free against the latest release. Then ground
  the motivating edges/nodes to the proposed placeholder CURIEs (the documented round-trip
  swaps them for real IDs once METPO mints). `just verify-proposal` + `just robot-validate-proposal`.

### 5. Verify + report
Run the gates and fix anything they flag:
`just validate-strict` (0 errors) · `uv run python scripts/audit_causal_graphs.py` (0 orphans/dangling) ·
`just validate-products` (id↔label gate clean) · `just gen-pages`.
Report: new coverage (predicate_id %, node grounding %), # grounded-to-METPO vs
grounded-to-RO/OBO vs proposed vs skipped-non-ontological, and the new proposal cohort summary.

## Guardrails
- **METPO-maximizing, not METPO-forcing:** never ground a term to a METPO CURIE whose
  meaning doesn't actually match just to raise METPO %. A wrong grounding is worse than a residual.
- **Quality over coverage:** the freq-1 idiosyncratic tail is expected to stay residual; that's correct.
- **Conservative proposals:** propose only genuinely reusable concepts (recurring across
  traits or a clear mechanistic primitive); one-offs are not ontology terms.
- Work in batches, commit per scope, keep the diff reviewable.
