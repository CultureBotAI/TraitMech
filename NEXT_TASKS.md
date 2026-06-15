# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-06-14.

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

## 2. Vendor the id↔label validator (decide: join the Mech trio?)

CultureMech / MIM / CommunityMech share a byte-identical
`scripts/validate_id_label_correspondence.py` + pin guard that gates
ontology `(id, label)` pairs. **TraitMech has no copy.** Its trait pages carry
METPO/CHEBI/etc. `(id, label)` pairs that would benefit from the same QC.

- Decide whether TraitMech joins the trio. If yes: copy the validator
  byte-for-byte, add a `conf/id_label_targets.yaml` for TraitMech's surfaces
  (trait YAML term blocks + rendered pages), add `verify-validator-pin` +
  `refresh-validator-pin` recipes and a CI guard. Coordinate with
  culturebotai-claw#6 (pin should ideally also cover tests/conf).

## 3. Trait promotion PROPOSED -> REVIEWED — DONE

All categories are promoted: the corpus is **427 REVIEWED + 50 DEPRECATED,
0 PROPOSED**. The 50 DEPRECATED are observation-value carriers, deliberately
out of scope (see `docs/DEPRECATED_REPLACEMENT_PROPOSAL.md`). No promotion work
remains.

## 4. Grounding tail + METPO upstream round-trip (deferred)

- Causal-graph grounding stands at **predicates 84% (1082/1284)** and
  **nodes 61% (1011/1643)**. The remaining residual is non-ontological
  descriptive phrases / one-off LLM verbs; raising it needs fuzzy matching or
  new term proposals (diminishing returns, higher risk).
- Upstream submission [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
  requests real METPO IDs for cohorts v1-v6 (143 classes + 13 predicates).
  When minted, run the documented round-trip (swap placeholder
  `1007xxx`/`2007xxx` for real CURIEs, re-seed).
