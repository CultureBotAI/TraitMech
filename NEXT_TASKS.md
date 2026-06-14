# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-06-14.

## 1. Improve embedding coverage — 128/477 traits unmatched (26.8%)

`just build-embeddings` matched 349/477 TraitRecords to ≥1 kg-microbe node
(73.2%); **128 are `no_match`** (see `data/embeddings/metpo_to_kgm_node.tsv`,
`method == no_match`). These have no embedding → no UMAP point / nearest
neighbors.

- Improve the alias path: extend `../kg-microbe/mappings/canonical/metpo_alias_mappings.tsv`
  (label → METPO CURIE) and/or the label-match fallback so more METPO classes
  resolve to a kg-microbe node.
- Re-run `just build-embeddings` then `just gen-pages`; coverage prints at the end.
- Some no_match are legitimately absent from the embedding (newly minted METPO
  classes the 2026-04-25 deepwalk run never ingested) — track those separately
  rather than forcing a match.

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

## 3. Continue trait promotion PROPOSED → REVIEWED

The metabolism / morphology / environment / ecology batches (+ citrate/fumarate
groundings) have been promoted and merged. Continue with the remaining trait
categories (e.g. physiology, upper-level/ontology classes), each as a
`promote-reviewed-<category>` batch with causal graphs.
