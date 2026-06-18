# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-06-15.

## 1. Embedding coverage — DONE (98.3%); residual is legitimately absent

`just build-embeddings` now matches **469/477 TraitRecords (98.3%)**:
349 `direct_metpo` + 120 `parent_proxy`. The parent-proxy tier (added to
`scripts/build_embedding_index.py`) walks `parent_traits` transitively to the
nearest ancestor CURIE present in the deepwalk and borrows its embedding, so
the 120 synthetic `traitmech:` traits now get a UMAP point near their semantic
parent (clearly tagged `parent_proxy`).

The remaining **8 `no_match`** are abstract value-carrier properties
(`METPO:2000058`–`2000063`, `2000071`, `2000103` — `has value`, `has observed
spot value`, `capable of`, …); they have no meaningful node embedding and are
left absent by design. Re-deriving real embeddings for the newly-minted METPO
classes would need a fresh kg-microbe deepwalk run (post-2026-04-25). No
further action unless a newer deepwalk lands.

## 2. id↔label validator — ADOPTED + ENFORCING (Phase 2) — DONE

TraitMech joined the Mech group — the byte-identical pin is now a **4-repo
invariant** (CultureMech / MIM / CommunityMech / TraitMech). Vendored
byte-identical (sha256 matches all three siblings):
`scripts/validate_id_label_correspondence.py` + the two shared tests +
`scripts/.validate_id_label_correspondence.sha256` pin.
`conf/id_label_targets.yaml` targets the two ontology grounding tables
(`mappings/node_grounding.tsv`, `mappings/predicate_grounding.tsv`) with
CHEBI/GO/ENVO/PATO/RO adapters; METPO/traitmech/biolink/rdfs/UniProtKB are
ignored prefixes. Recipes: `validate-products`, `report-label-drift`,
`verify-validator-pin`, `refresh-validator-pin`. CI workflow
`label-correspondence.yaml`: pin guard + `validate-products` both **blocking**.

The 15 pre-existing MISMATCHES found at adoption were all wrong CURIEs in
`mappings/node_grounding.tsv` (e.g. `PATO:0000383` is "female", not "decreased
temperature"); corrected to the right CURIEs (verified vs OAK) and the trait-YAML
`grounding:` values re-migrated. One curator-accepted residual stays green via
`exceptions:` (`PATO:0001717` "light intensity" — OAK canonical is the awkward
"radiation emitting intensity quality"). Gate now reports 113 OK_CANONICAL +
2 OK_SYNONYM + 1 OK_EXCEPTION, 0 errors.

## 3. Trait promotion PROPOSED -> REVIEWED — DONE

All categories are promoted: the corpus is **427 REVIEWED + 50 DEPRECATED,
0 PROPOSED**. The 50 DEPRECATED are observation-value carriers, deliberately
out of scope (see `docs/DEPRECATED_REPLACEMENT_PROPOSAL.md`). No promotion work
remains.

## 4. METPO upstream round-trip (BLOCKED on upstream) + residual floor

- Causal-graph grounding now stands at **predicates 85% (1094/1284)** and
  **nodes 62% (1024/1643)**. The remaining residual is non-ontological
  graph-narrative phrases (adaptation states, composite descriptors) and vague
  verbs — these are NOT ontology concepts and should stay as free-text node/edge
  labels, not be force-matched or proposed. This is the quality floor.
- Genuinely-novel recurring concepts have been proposed: electron-transfer
  predicates ([v6](proposals/metpo_traitmech_v6/)) and 2 causal-mechanism
  classes ([v7](proposals/metpo_traitmech_v7/): salt-in strategy, reductive
  genome evolution).
- Upstream submission [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
  now requests real METPO IDs for cohorts **v1–v7 (145 classes + 13 predicates)**,
  with concrete suggested mintable ranges from the 2026-06-12 release
  (classes `1007094–1007238`, predicates `2000735–2000747`). **Blocked on the
  METPO maintainers minting.** When minted, run the documented round-trip (swap
  placeholder `1007xxx`/`2007xxx` for real CURIEs in `data/raw/metpo.owl` +
  groundings, re-seed).

## Adopt DisMech knowledge-gaps + datasets + QC dashboard (claw#7)

Coordinated cross-Mech adoption of DisMech's domain-general features. Full plan,
locked decisions, and DisMech schema references live in culturebotai-claw#7 (the
shared, pinned LinkML module is authored once and vendored across all four Mechs).
This repo's slice:
- Knowledge gaps — add a `discussions` slot (broad `Discussion` supertype; `kind`
  incl. KNOWLEDGE_GAP / OPEN_QUESTION / CONTROVERSY / CURATION_TODO) to
  `TraitRecord`, imported from the shared module; bind `attaches_to` anchors to
  `causal_graphs#…` (pairs naturally with the existing evidence-backed causal
  edges). Wire a `knowledge-gap-scan` recipe over the existing Edison harness.
- Datasets — add the canonical shared `Dataset` slot (TraitMech models none today).
- QC dashboard — adopt the generalized dashboard from Phase 3 (TraitMech currently
  has only TSV/MD reports, no rendered dashboard).
