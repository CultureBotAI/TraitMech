# TraitMech trait graph provenance

Graph maps retain their KG-Microbe DeepWalk features and domain matching policies. The fleet's common BGE text map is a separate view. This work follows #917.

Run `python scripts/build_embedding_index.py --src /path/to/source.tsv.gz --kgm-aliases /path/to/metpo_alias_mappings.tsv --method pacmap`. For the retained graph layout add `--method sfdp --umap-out data/embeddings/trait_graph.json`. `--method umap` is an explicit alternative.

The slim source, match TSV, selected projection and nearest-neighbor JSON are staged together. Their destinations (`--out-deepwalk`, `--out-match`, `--umap-out`, `--out-neighbors`) must be distinct siblings, so the projection's `.metadata.json` can validate the complete generation. Default names are `deepwalk_traits.tsv.gz`, `metpo_to_kgm_node.tsv`, `trait_umap.json`, and `trait_nearest_neighbors.json` under `data/embeddings`.

The source scan retains only direct/parent CURIEs and record/alias label candidates. Every trait has a projected or omitted ledger entry. Parent-proxy source IDs, mean weights, exact normalized reducer matrix and cosine nearest-neighbor matrix are recorded separately. Generating the alternate projection from identical inputs preserves the shared artifact bytes; both receipts must validate afterward.

New generation reads the selected TSV or TSV.gz stream directly and hashes the exact bytes while parsing. Old basename/size/mtime pickle caches are ignored, including when `force_reload` is false. The scan is streaming and retains only required node vectors; the full source file is still read once per generation. Do not infer source identity by hashing a different file beside old coordinates.

Schema-v2 receipts bind the full corpus, matching/omission ledger, ordered reducer matrix, actual algorithm/normalization/settings and installed backend versions to checksums of every output. PaCMAP records fitted pair counts. The sfdp backend, where available, records the symmetric union-kNN construction, DOT checksum, Graphviz version and command arguments. Failed generation leaves previous outputs unchanged; publication rolls back ordinary write failures. A process kill can leave a `.graph-recovery-*` directory for recovery and is not claimed to be an atomic website deployment.

Validate a completed generation with:

```python
from pathlib import Path
from traitmech.graph_embedding_receipts import load_receipt

receipt = load_receipt(Path("path/to/projection.metadata.json"))
```

This verifies all sibling artifacts declared by the receipt. It is not a tool for attaching newly guessed provenance to legacy arrays. Full published artifacts must be regenerated from reviewed current inputs before the graph correction is considered complete.

Before publication, run `just audit-embedding-publication`. The maintained page renderer
and the `just qc` derived-pages audit run the same preflight before changing site
output. Both specialty maps must bind the exact complete current YAML path/hash
ledger, including ignored YAML, and their map, match table, slim vectors and
neighbor outputs must form consistent generations. Parent ordering and other
graph-relevant fields are covered even when common semantic text is unchanged.

This check reads current YAML and committed artifacts only; it never opens the
original large embedding source or runs a model/reducer. Missing, legacy-only,
stale or inconsistent receipts block current publication and preserve prior
pages. After YAML curation, refresh both specialty generations from the selected
source before rendering; do not attach current hashes to old coordinates. The
standalone historical receipt reader may still label old arrays as unverified,
but the maintained current-site writer does not bypass this gate.

## Refreshing the complete local site

Finish YAML curation and any `just seed-apply` first. Then refresh and validate
the enabled common text bundle from those complete current records, following
[the semantic-map guide](TEXT_MAP_INPUTS.md) and the
[locked runtime instructions](../conf/embedding-runtime/README.md).
`gen-site` does not seed YAML or run semantic model inference: the current
common bundle remains an explicit prerequisite checked by the renderer.

Select the exact reviewed DeepWalk source and alias TSV, then run:

```bash
just gen-site "/path/to/selected-source.tsv.gz" "/path/to/metpo_alias_mappings.tsv"
```

This runs PaCMAP into `trait_umap.json`, then sfdp into `trait_graph.json`,
using the same literal source and alias paths for both, before the maintained
renderer checks all current bundles and writes pages. Either producer failing
stops the composite before rendering. `just build-embeddings SOURCE ALIASES`
runs only the paired graph refresh. Both commands require explicit paths;
the former zero-argument, PaCMAP-only composite is retired (#929).

The direct builder defaults to the selected 2026-06-26 v3 filename, preferring
`KG_MICROBE_EMBEDDINGS`, then the local embeddings directory, then CommunityMech
(or `COMMUNITYMECH_ROOT`). The paired recipes require an explicit source to
keep both invocations on one reviewed release. Both source and aliases must
remain unchanged while the pair runs; the final gate rejects a mixed generation.
Graph refresh scans the source once per layout and needs the numerical runtime
and Graphviz sfdp. It is a deliberate local operation, never a CI/QC dependency.
