# Native evidence inventory, 2026-11-07

This advances [TraitMech #2083](https://github.com/CultureBotAI/TraitMech/issues/2083)
by making the current observation and review surface inspectable. It does not
change the native assertion exporter or grant scientific approval. The remaining
observation extraction and exact-scope review work stays open in that issue.

The inventory reads immutable Git blobs at
`0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a`, including both the native trait schema
and the canonical review schema. The full report hashes 1,245 inputs: 1,130 trait
records, 113 structured review documents, and two schemas. It retains every
example's original fields and qualifiers, and each review's declared source,
targets, selectors and scientific-review flag. Those declarations are inventoried;
their historical freshness and scientific validity are not adjudicated here.

| Pinned surface | Count |
| --- | ---: |
| Trait records | 1,130 |
| Records with canonical examples | 579 |
| Canonical examples | 784 |
| Examples with both a note and a reference | 784 |
| Causal graphs | 769 |
| Records carrying `observation_count` | 0 |
| Records carrying dataset references | 0 |
| Structured review documents | 113 |
| Review documents by kind | 82 record, 18 batch, 13 repository |
| Review target entries across documents | 12,645 maintained targets |
| Exact `canonical_examples[index]` selectors | 0 |

Target entries can recur across reviews; 12,645 is not a count of independent
observations or experiments. Of the 113 review documents, 105 declare scientific
review and eight do not. The inventory does not turn those declarations into
assertion-level approvals. Its one nonempty selector addresses graph scope notes
and an edge description in `data/traits/ecology/predatory_bacterium.yaml`, not an
individual canonical example.

At this pin, `CanonicalExample` has four fields: `taxon_id`, `taxon_label`, `note`
and `reference`. Assay identifiers, strain identifiers, conditions, measurements,
units, polarity and review bindings have no dedicated example fields. Notes can
contain biologically meaningful qualifications, and these remain intact; the
inventory does not claim that the cited literature lacks experimental evidence.
The schema describes `observation_count` as an aggregate ranking signal, not a
collection of independently identified experiments. Dataset references or quoted
assay narratives need explicit extraction and review before a future observation
adapter can make stronger claims.

The local discovery pass includes ignored files under `data/` and `reviews/`.
It found no additional paths outside the source commit in this worktree. This is
a bounded filesystem finding, not a claim about all repositories or external
datasets. Local file contents never replace the pinned evidence.

The real canary inspected `data/traits/ecology/periplasmic_bacterial_predation.yaml`
through the same helper, environment and output directory as the full inventory.
It retained the full HD100 note and its wild-type, prey and assay qualifications.
Both reports were written exclusively, flushed, read back and independently
rehashed before their counts were reported:

| Retained local report | SHA256 |
| --- | --- |
| `workspace/edge-curation-20261107/evidence-inventory-canary.json` | `df4abc7057903293867ca136902b1de6864834a9bc9e92a1e1aedc02b6c9c6b9` |
| `workspace/edge-curation-20261107/evidence-inventory-full.json` | `8e299b691dd681eca725e45a7365adc377e82436df20605860b458c22c001dbe` |

With this repository's `src` and the pinned CLAW checkout's `src` on `PYTHONPATH`,
the retained launcher is:

```sh
.venv/bin/python scripts/adhoc/inventory_edge_evidence_20261107.py \
  --root . --source-commit 0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a \
  --all --output workspace/edge-curation-20261107/evidence-inventory-full.json --write
```

Omit `--write` for the plan. For a new canary, replace `--all` with `--record`
and the record path above, and choose a new output filename. Existing outputs are
refused. The shared contract checkout remains
`1b5391d083ba85ac94e5279c3cba25ac4fde243c`.

Validation passed: 34 focused adapter/inventory tests, Ruff, diff checks and the
complete `just --no-dotenv qc` gate. The independent read-only code review found
no blocking finding. Zero scientific reviews and zero inherited approvals were
created. The existing 784-row native export remains byte-identical; its manifest
SHA256 is `7a1e5b5d9ff30e3b1db947c7facea76f43d967b48594ea72c7777e8fba1e545a`.
