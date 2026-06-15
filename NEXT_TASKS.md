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

## 2. id↔label validator — ADOPTED (Phase 1, report-only)

TraitMech joined the Mech trio. Vendored byte-identical (sha256 matches
CommunityMech/CultureMech): `scripts/validate_id_label_correspondence.py` + the
two shared tests + `scripts/.validate_id_label_correspondence.sha256` pin.
`conf/id_label_targets.yaml` targets the two ontology grounding tables
(`mappings/node_grounding.tsv`, `mappings/predicate_grounding.tsv`) with
CHEBI/GO/ENVO/PATO/RO adapters; METPO/traitmech/biolink/rdfs/UniProtKB are
ignored prefixes. Recipes: `validate-products`, `report-label-drift`,
`verify-validator-pin`, `refresh-validator-pin`. CI workflow
`label-correspondence.yaml`: pin guard blocking; drift report non-blocking.

**Phase 2 prerequisite — triage 15 pre-existing id↔label MISMATCHES** (caught
on first run; all in `mappings/node_grounding.tsv`, mostly wrong CURIEs that
need the correct id + a re-grounding migration that *overwrites* the wrong
`grounding:` values already written into trait YAMLs — `ground_causal_nodes.py`
only fills empty slots):

- `PATO:0000383` (is "female") labeled "decreased temperature" — wrong id
- `PATO:0001428` (is "medium acidity") labeled "acidic pH"
- `PATO:0001429` (is "acidic") labeled "alkaline pH"
- `PATO:0001432` (is "decayed") labeled "neutral pH"
- `PATO:0001637` labeled "extremely high temperature"; `PATO:0001717` "light intensity"
- `ENVO:01001057` (is "environment associated with a plant part…") labeled "anaerobic environment" (x2)
- `ENVO:01000687` (is "coast") labeled "saline environment"
- `CHEBI:65015` (is "paromamine(3+)") labeled "osmolyte"
- `CHEBI:33542` thiosulfate(2-)→canonical "trioxidosulfanidosulfate(1-)" (likely a real synonym; may move to exceptions)
- `CHEBI:17499` electron donor→"hydrogen donor"; `GO:0046358` wood-ljungdahl label; `GO:0030641` obsolete; `GO:0006572` "L-tyrosine catabolic process" (synonym → exceptions)

After fixing the wrong CURIEs (+ re-grounding) and moving true residuals to
`exceptions:`, flip CI to the blocking `validate-products` gate (Phase 2),
mirroring CommunityMech.

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
