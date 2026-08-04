---
description: Deep-research the ungrounded causal-graph predicates/nodes; ground to METPO first (else RO/OBO), and where no good term exists, draft a METPO proposal. METPO-maximizing, not METPO-forcing.
argument-hint: "[predicates|nodes] [min-freq N | category C | label \"...\"]  (default: both, min-freq 2)"
---

# Ground-or-propose residual causal-graph terms (METPO-first)

Goal: shrink the ungrounded residual left after the matchers. For **each recurring
residual term**, either (a) ground it to an existing ontology term — **METPO first**,
then RO/OBO — or (b) draft a **METPO proposal** when nothing fits. Maximize METPO
coverage; mint only when no good existing term exists anywhere.

`$ARGUMENTS` selects scope (default: both predicates and nodes, only labels with
edge/node count ≥ 2; skip the freq-1 long tail). Examples:
`/ground-or-propose-metpo predicates min-freq 3` · `/ground-or-propose-metpo nodes category metabolism`.

## Scale (what the residual looks like — re-check before you start)
The residual is large and skewed: a small head of high-frequency terms carries most
of the coverage. Re-read the live counts each run; as of the last pass:
- Predicates: ~190 labels at freq ≥ 2 (top: `supports`, `positively regulates`,
  `induces`, `required for`, `drives`, `maintains`, `mediates`, `converts`).
  `positively regulates`/`negatively regulates` were grounded in #235;
  `causally upstream of` is deliberately withheld — see the skip rule below.
- Nodes: ~215 labels at freq ≥ 2, dominated by `BIOLOGICAL_PROCESS` and
  `GENE_OR_PROTEIN`, then `CHEMICAL`, `ENVIRONMENTAL_FACTOR`, `QUALITY`.

**Do not deep-research all ~400 one at a time.** Most of the head is bulk-groundable
without research (see steps 2–3). Reserve `/deep-research` for the genuinely ambiguous
remainder. Work the head first — it buys the most coverage per unit effort.

## Inputs (read these)
- **Residual to work:**
  - Predicates: `reports/predicate_grounding_residual.tsv` (cols: `predicate_label`,
    `edge_count`, `status`, `blocked_by`, `example_files`).
  - Nodes: `reports/node_grounding_residual.tsv` (cols: `node_label`, `node_type`, `node_count`, `example_files`).
  Filter to the requested scope + min-freq; rank by frequency (highest first).
  **Skip every row whose `status` is `blocked_by_node_type`.** Those are not
  ungrounded for lack of a CURIE — `blocked_by` names it. The CURIE is withheld
  because the edges' node types fall outside the relation's declared domain and
  range, so re-mapping the label re-introduces the error rather than fixing it.
- **Context/evidence per term:** the trait's Edison report at
  `research/traits/<category>/<slug>-deep-research-falcon.md` (the `example_files` point you to the trait),
  and the trait YAML `data/traits/<category>/<slug>.yaml` (how the term is actually used in the graph).
- **METPO term inventory (search FIRST):**
  - In-repo: every `data/traits/**/*.yaml` with `term_kind: OBJECT_PROPERTY` (predicates) or `term_kind: CLASS` (nodes) and an `identifier: METPO:…` — match on `label` + `synonyms`.
  - Full ontology: `data/raw/metpo.owl` (local) and the latest release `https://w3id.org/metpo/metpo.owl` (BioPortal-equivalent) for terms not yet seeded into the corpus.
- **Where groundings/proposals go:** `mappings/predicate_grounding.tsv`, `mappings/node_grounding.tsv`; new proposal cohort under `proposals/` (latest is `metpo_traitmech_v7/`).
- **Conventions:** the `metpo-proposal` and `manage-identifiers` skills (METPO-first policy, ID reservation, ROBOT-template format, citation-vs-mapping rule).

## Procedure

### 1. Build + cluster the worklist
Load the residual for the requested scope, apply min-freq/category/label filters, and
**deduplicate by meaning, casing, and format** — `atp`/`ATP`, `c-di-GMP`/`cyclic
di-GMP`/`c_di_gmp`, `na+/h+ antiporter activity`/`na+/h+ antiporters` are each one
concept; ground once and let it apply to all surface forms. Cluster near-synonyms so
one decision (and at most one research query) covers the whole cluster.

Drop terms that are graph-narrative artifacts, not reusable concepts (`maximal growth
rate`, `baseline mesophile adaptation`, vague verbs like `engages`, `realizes`,
`positions`) — record as `skipped: non-ontological`.

### 2. Tier-0 bulk grounding — no research needed (do this first)
A large share of the head is mechanical. Ground these directly; **do not** spend a
`/deep-research` call on them:

- **Generic causal/regulatory predicates → RO** (the relation closure). Map the obvious
  ones straight to RO and record `skos:exactMatch`/`closeMatch` with `source: RO`.
  **Write `subject_types`/`object_types` for each one rather than leaving
  `*`/`*`, and read the relation's own domain and range to decide what they
  are** — they differ across this list, so there is no blanket rule:
  the regulation and causal relations (`RO:0002211/2/3`, `RO:0002418`,
  `RO:0002629/30`) are defined over **occurrents**; `enables` (RO:0002327) is
  *"c enables p iff c is capable of p"*, so material entity → process;
  `produces` (RO:0003000) is defined *"where a and b are material entities"*;
  `part of`/`has part` (BFO) are deliberately domain-neutral.
  `causally upstream of` is absent from this list precisely because its label
  matched exactly and its edges did not (#235, #236):
  `positively regulates`→`RO:0002213`, `negatively regulates`→`RO:0002212`,
  `regulates`→`RO:0002211`, `causally upstream of or within`→`RO:0002418`,
  `directly positively regulates`→`RO:0002629`,
  `directly negatively regulates`→`RO:0002630`, `enables`→`RO:0002327`, `part of`→`BFO:0000050`,
  `has part`→`BFO:0000051`, `produces`→`RO:0003000`, `is converted to`/`converts`→ check
  `RO:0002233`/`RO:0002234` (has input/output) vs a SO/ChEBI transformation relation.
  For softer verbs (`supports`, `drives`, `maintains`, `mediates`, `induces`, `required
  for`, `protects against`), pick the closest RO relation and mark `skos:closeMatch` /
  `skos:broadMatch` — these are real RO relations, prefer reuse over minting. Only escalate
  to research/proposal if no RO relation is even close.
- **Nodes route by `node_type`** to a target ontology branch — search *that branch first*:
  | node_type | search first | then |
  |---|---|---|
  | CHEMICAL | CHEBI | GO (metabolite roles) |
  | GENE_OR_PROTEIN | PR, GO (gene-product), enzyme (EC) | UniProt-backed |
  | MOLECULAR_FUNCTION | GO:MF | RO/METPO |
  | BIOLOGICAL_PROCESS / PATHWAY | GO:BP | METPO, MetaCyc xref |
  | CELLULAR_LOCALIZATION / ORGANELLE | GO:CC | — |
  | ENVIRONMENTAL_FACTOR | ENVO | PATO, CHEBI |
  | QUALITY / STATE / CAPACITY | PATO | METPO |
  | TRAIT | **METPO** | OMP, MICRO |
  Concrete chemicals/proteins/processes (ATP, acetyl-CoA, trehalose, carbonic anhydrase,
  proton motive force) live in CHEBI/GO, **not** METPO — grounding them to CHEBI/GO is
  correct and expected. METPO is the phenotype/trait/capability layer; don't force concrete
  molecules into it.

After Tier-0, what remains for step 3 is the ambiguous middle: trait-/capability-level
concepts and fuzzy predicates where the right term (or whether one exists) is unclear.

### 3. Deep-research the ambiguous remainder — **use the `deep-research` command**
For each *cluster* that survives Tier-0 (batch related terms into one question), invoke
the Claude Code **`deep-research`** skill (`/deep-research`) with a tightly-scoped query.
Pass the `node_type`/predicate role and the routing hint so the search starts in the
right branch:

> Deep-research the microbial-trait concept **"<term>"** (used as a causal-graph
> <predicate | node of type T>; context: <one line from the trait/Edison report>).
> 1. Does the **METPO** ontology (https://w3id.org/metpo/metpo.owl, BioPortal "METPO")
>    contain a class/relation for this concept? Give the exact `METPO:` CURIE + label,
>    and whether it is an exact, broad, narrow, or close match.
> 2. If METPO has none, is there a standard term in the expected branch for this type
>    (<RO/biolink for predicates; CHEBI/GO/ENVO/PATO/PR for nodes per the routing table>)?
>    Give the CURIE + match strength.
> 3. If neither has a good match, state that explicitly and propose a one-line
>    Aristotelian definition + the most likely METPO parent class for a new term.
> Prefer authoritative ontology sources; cite OLS/BioPortal/OBO. Be decisive about
> match strength; flag if the concept is too vague/idiosyncratic to be an ontology term.

Treat the existing Edison report as supporting evidence, but the **`deep-research`
command is the ontology-lookup authority** here.

### 4. Decide per concept (priority order)
1. **Strong METPO match** (exact/close, same concept) → ground to the `METPO:` CURIE. *Maximize this — it is the whole point.*
2. **No METPO, strong RO/OBO match** (RO/biolink predicates; CHEBI/GO/ENVO/PATO/PR nodes) → ground to that CURIE. Reuse a real term before minting.
3. **No good existing term anywhere**, but the concept is **generic + recurring + reusable** → **METPO proposal** (new term).
4. **Vague / idiosyncratic / one-off** → leave residual; do not force a match or mint a term.

Verify every chosen CURIE actually resolves to that label (catch typos / obsolete terms)
— for OAK-resolvable prefixes the `label-correspondence` gate re-checks, but don't rely
on it for METPO.

### 5. Apply
- **Groundings** → append rows to the mapping TSVs (keep column order; the 4th col is the
  skos strength `predicate_id`):
  - `mappings/predicate_grounding.tsv`: `label, target_curie, target_label, predicate_id(skos:*Match), source, confidence, notes`
  - `mappings/node_grounding.tsv`: `label, node_type, target_curie, target_label, predicate_id(skos:*Match), source, confidence, notes`
  Then run the grounders to write them into the YAMLs:
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

### 6. Verify + report
Run the gates and fix anything they flag:
`just validate-strict` (0 errors) · `uv run python scripts/audit_causal_graphs.py` (0 orphans/dangling) ·
`just validate-products` (id↔label gate clean) · `just gen-pages`.

Report, against the **prior** coverage (predicates were ~62%, nodes ~33% after the last pass):
- new predicate_id % and node grounding %, and the delta;
- counts: grounded-to-METPO vs grounded-to-RO/OBO vs proposed vs skipped-non-ontological;
- the Tier-0 bulk share vs the deep-researched share (so the effort/coverage split is visible);
- the new proposal cohort summary.

## Guardrails
- **METPO-maximizing, not METPO-forcing:** never ground a term to a METPO CURIE whose
  meaning doesn't actually match just to raise METPO %. A wrong grounding is worse than a residual.
- **Right layer:** concrete molecules/proteins/processes belong in CHEBI/GO/PR, not METPO.
  Push trait/capability/phenotype concepts toward METPO; push concrete entities toward OBO.
- **Quality over coverage:** the freq-1 idiosyncratic tail is expected to stay residual; that's correct.
- **Conservative proposals:** propose only genuinely reusable concepts (recurring across
  traits or a clear mechanistic primitive); one-offs are not ontology terms.
- **Don't over-research:** Tier-0 the mechanical head; spend `/deep-research` only on the
  ambiguous middle. Batch clusters into one query. Work in batches, commit per scope, keep the diff reviewable.
