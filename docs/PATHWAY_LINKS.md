# Pathway context on causal nodes

`causal_graphs[].nodes[].related_records` uses `PathwayContextLink`, a local
specialization of claw's shared `CrossCorpusLink`. It requires `corpus`,
`identifier`, `relation`, `basis`, and a full 40-character `source_version`.

The supported corpus is `PathwayMech`; `PATHWAY_CONTEXT` means the linked
organism-scoped pathway illustrates the node's route, biochemical component,
or precursor context. It does not assert exact equivalence, a trait phenotype
in the linked organism, or identical physiology in every organism. Existing
`grounding` and exact-equivalence `xrefs` retain their own meanings.

Each basis names the linked organism and explains the correspondence and its
limits. Composite nodes can link several records, stating which component
each record covers. The record page renders the context alongside its graph,
including basis and source version.

`conf/pathwaymech_index.json` is a byte-preserved copy of the PathwayMech
published index at the commit in `conf/pathwaymech_pin.yaml`. The pin records
its repository path and SHA-256. `just check-pathway-links` verifies those
bytes, target membership, exact source version, allowed relation, nonblank
basis, and duplicate links. This offline check runs in `just qc`. Refresh the
index from a reviewed PathwayMech commit and review all affected links before
updating the pin; do not point the pin at a moving branch.

The initial reviewed additions are in `conf/pathway_context_links.yaml`.
`just apply-pathway-context-links` previews them; `--apply` writes through
`write_validated_trait` and appends per-record curation history. The writer
checks target and node identity, refuses protected records, prevalidates every
proposed record, preserves existing examples by appending, and makes no change
on an exact replay. Repository-level history and regenerated derived artifacts
are still required.

The initial manifest links 16 nodes in 11 traits to 14 pathway records
(18 node-record links). It excludes peptidoglycan morphology leads: cytoplasmic
precursor synthesis does not by itself describe septal, polar, or lateral wall
remodeling. It also excludes the urease/urea-amidolyase, assimilatory/
dissimilatory sulfate, and formaldehyde assimilation/oxidation look-alikes.

The catalase addition appends the reviewed P06115 Ctt1 reference protein to
the monofunctional heme-catalase node. UniProt verifies identity, strain taxon,
versions and InterPro family; PMID:24563848 supplies primary catalytic-function
evidence. The role and evidence notes distinguish the paper's YPH250 and BY4741
experimental backgrounds from the S288c reference accession and retain the
nutrient-rich-medium limitation. It does not extend the bacterial PerR/OxyR
regulatory branches to yeast. Retrieval metadata and the exact checked excerpt
are in `research/pathway_context_sources.json`.
