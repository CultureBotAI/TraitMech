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
