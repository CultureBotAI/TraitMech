# TraitMech adapter review, 2026-11-07

Tracked as [TraitMech #2079](https://github.com/CultureBotAI/TraitMech/issues/2079).

The independent read-only implementation review found that `verify_export`
checked native assertion identities, physical hashes and counters but did not
reconcile the manifest's declared source repository and commit with each native
envelope. Changing `manifest.source_commit` left the assertion stream unchanged
and passed the verifier. This can mislabel the pinned source even though the
downstream EdgeMech census performs its own source check.

The in-scope repair must bind every assertion to the declared source repository,
commit and selected record inventory, validate the export contract and schema
version, and enforce the adapter's unassessed/zero-approval invariants. Complete
native scope must reconcile with the declared selected corpus. Mutation tests
must reject mismatched manifests without changing the assertion bytes.

The reviewer found no additional blocking scientific-scope issue: canonical
examples remained unassessed, and native content came from immutable Git blobs.
After repair, the actual publisher must rerun one real canary and inspect its
persisted files before another complete native export.

The publication-protocol follow-up identified a missing output-parent directory
flush, recorded as [#2080](https://github.com/CultureBotAI/TraitMech/issues/2080).
The repair flushes newly created directory entries, the staged directory, the
payload link before the manifest link, and the final output and parent before
success. A regression test checks this ordering.

The shared-runtime check also omitted the actual governance implementation of
the imported YAML loader. [#2081](https://github.com/CultureBotAI/TraitMech/issues/2081)
records this boundary gap. The checker now verifies that implementation's import
origin and includes its source directory in the immutable-checkout check.

Validation completed for these repairs: 27 focused adapter tests, lint, PR sanity,
and the live shared-runtime pin check passed. The repository's complete
`just --no-dotenv qc` run passed, including strict validation of 1,130 records and
freshness checks for the existing reports and pages. The publication-only
follow-ups were then checked by the focused tests and lint; curated records and
their scientific projections did not change.

The final live canary used `data/traits/environment/hyperthermophilic.yaml`,
example 0, at source commit `0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a`.
It published one unassessed assertion, 17,740 bytes, zero scientific reviews and
zero approved KG occurrences. Its persisted JSONL SHA256 is
`50f47ea7bde2f81cc9c222c706f0bcf98414d841c1f08f3ab5f9af7c4459fd36`;
the manifest SHA256 is
`9e1abe71ca1c09bc8f0fbdca60eec2060c0b4fb6f832df3ca7ef863a7421cb4b`.
Both were independently rehashed after the publisher returned. Runtime outputs
are retained under `workspace/edge-curation-20261107/trait-canary-v3/`.

The complete native export subsequently scanned all 1,130 records at the same
source commit and persisted 784 assertions (13,106,061 bytes), all unassessed.
It created zero scientific reviews and approved zero KG occurrences. The final
JSONL SHA256 is
`4328328381dcc3c44f9b9b49a34edd275d28b5ee43971d4c6f4a36bddee01175`;
the final manifest SHA256 is
`7a1e5b5d9ff30e3b1db947c7facea76f43d967b48594ea72c7777e8fba1e545a`.
The same publisher and environment ran both final jobs; both final files were
independently rehashed and the JSONL line count was checked after publication.
The full artifact is under `workspace/edge-curation-20261107/trait-full-v3/`.
