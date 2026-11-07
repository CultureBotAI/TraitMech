# Native assertions for EdgeMech

The optional `traitmech.edge_curation` module exports exact `canonical_examples`
from a caller-pinned TraitMech Git commit. It reads Git blobs, so a later working
copy edit cannot alter a pinned export. Each assertion retains its full owning
record, example position, native reference, evidence, conditions and qualifiers.
The native schema and prefix map are hashed independently.

These examples describe reference taxa. They do not constitute strain-specific
assay observations, and their record's `mapping_status: REVIEWED` does not approve
an organism assertion. The adapter marks every example `unassessed`. It retains
taxon-agnostic causal graphs as source context without projecting their edges
onto organisms. The export grants zero KG occurrence approvals and zero new
scientific reviews. A future reviewed-assay adapter needs explicit statement
scope, exact source/evidence bindings and native review proof before promotion.

Use the shared CLAW source commit named by `CLAW_COMMIT` in the module. The
dedicated CI job checks that exact commit and import origin. To use a local
checkout, set `PYTHONPATH` to this repository's `src` and that CLAW checkout's
`src`, then run `scripts/adhoc/check_edge_contract_pin_20261107.py --claw-root PATH`.

Plan one example before writing it:

```sh
python -m traitmech.edge_curation --root . --source-commit COMMIT \
  --record data/traits/environment/hyperthermophilic.yaml --example-index 0 \
  --output workspace/edge-curation/canary
```

Repeat the same command with `--write`, then call `verify_export(output)` and
inspect the nonempty `assertions.jsonl`, `manifest.json`, row count and status
counters. Only after the real canary succeeds, replace the record selection with
`--all` and choose a new output directory for the full native export. Both paths
use the same publisher and validation. Existing destinations are refused.

The publisher streams canonical JSONL and verifies persisted identities, hashes
and counters before atomically publishing the manifest. Consumers must require
the manifest. An interrupted run may leave an unpublished directory; it never
overwrites an earlier export. Generated exports belong under ignored `workspace/`.
The manifest states whether all native example records were selected; that is
native-source coverage, not KG-Microbe scientific approval or edge coverage.

The [native evidence inventory](EDGE_EVIDENCE_INVENTORY_20261107.md) records the
pinned observation and review surfaces, preserved qualifiers and remaining
requirements for an exact organism/strain observation adapter. It advances
[issue #2083](https://github.com/CultureBotAI/TraitMech/issues/2083) without changing
the current unassessed export.
