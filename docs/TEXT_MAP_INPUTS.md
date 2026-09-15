# Common semantic text map inputs

Includes all canonical trait YAML records. Stable record identifiers link to
the exact existing category/stem page. Text includes label, definition, semantic
category, synonyms, resolved parent labels and named canonical taxa. Citation,
history, mapping status, ontology identifiers and curation discussions are
excluded; graph structure and graph-source vectors remain a separate view.
Parent labels come from the full corpus, so canary selection cannot alter text.

Export with `just text-map-inputs --output data/text_map/inputs.jsonl`. Without `--output`, the command validates a preview. `--record` (repeatable repository-relative YAML path) and `--limit` explicitly select canary subsets; ordinary exports cover every eligible record.

Each JSONL row has exactly `identifier`, `label`, `category`, `page`, `source_path`, `text`, `text_sha256`, and `adapter_version`. The text digest is SHA-256 over the exact UTF-8 text. Input order and text are deterministic; duplicate IDs and unreadable records fail. This adapter makes no model call. Common model/projection generation and publication require the fleet pipeline and full-input checks.

Changing provenance-only fields leaves semantic text unchanged. Editing a selected semantic field changes its digest. This text view supplements the existing graph view; it does not alter graph aggregation or its scientific interpretation.

The `page` field is relative to the directory containing the published map
folder: from `text-map/index.html`, the shared renderer uses `../` plus `page`.
This repository publishes the bundle at `pages/text-map/`, so record links omit
the deployment wrapper `pages/` and resolve to its sibling record directories.

## Generate and publish the common map

The governed runtime is installed at `scripts/embedding_pipeline.py`.
`conf/text_map.yaml` enables the immutable bundle selected by
`data/text_map/current.json`. `just gen-pages` validates the pinned BGE profile,
512-token window, actual PaCMAP and fresh complete adapter input before staging
`pages/text-map/` and its navigation link. A stale or invalid enabled bundle
fails before the existing site is replaced.

Follow the [locked runtime instructions](../conf/embedding-runtime/README.md)
for local generation and refresh. After semantic curation, export complete
inputs and reuse the matching verified vector cache to encode changed text,
then project the new bundle and run `just gen-pages`. Keep the same recorded
model/runtime profile to reuse its cache. Normal CI and page rendering do not
run inference. Graph maps retain their own source/corpus receipts and must be
regenerated through their maintained builders when those inputs change.
