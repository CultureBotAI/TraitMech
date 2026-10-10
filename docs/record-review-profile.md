# TraitMech Record Review Profile

Use the [shared contract](record-reviews.md) for new structured observations.
`conf/record_review.yaml` declares the active review routes and native rubrics.
CLAW owns the byte-identical schema, saver, common guide and contract test;
TraitMech owns this profile and the native portions of its skills. Historical
research, reports, scientific records and curation history are not migrated.

## Native routes

- `add-trait`: persist the local adversarial scientific review before merging
  a new trait. Use `kind: record` for one trait, `batch` for an explicitly
  scoped coupled change, or `category` for an actual boundary assessment.
  Capture inputs before judgement, identify author self-review honestly, and
  save a new linked observation after fixes change reviewed inputs. The final
  assessment covers the content being merged; PR comments and green CI do not
  substitute for the bundle or confer human scientific sign-off.
- `review-yaml-record`: `kind: record`, one complete `TraitRecord` assessed
  against the curate checklist, grounding policy and curation playbook.
- `review-yaml-category`: `kind: category`, explicit membership, selection,
  population, actual reviewed IDs, exclusions and lump/split/retain/defer
  decisions. Preserve polarity, trait class, domain/range, taxon/context and
  legitimate measurement variants; a shared label does not prove equivalence.
- Audit-only `curate-yaml-record`: the same record observation and local
  scientific rubric, with proposed actions only. Skip the mutation/history
  steps and persist a YAML/Markdown bundle through the shared saver.
- `research-causal-graphs`: a provider run or batch sweep produces research
  drafts. After inspecting cited sources and the actual record, save the
  final graph review as `record` or explicitly scoped `batch`. Retain exact
  node/edge locators, evidence, taxon/context, polarity, mechanism versus
  correlation, missing steps and limitations. Provider output is not primary
  evidence and a completed provider call is not a completed scientific review.
- `audit-schema-gaps` and its `schema-gap-analysis` alias: deterministic
  instance/schema/writer reports remain diagnostics. Save any final bounded
  record/repository assessment through the shared saver, retaining
  `scientific_review: false` unless a separate source-based scientific review
  was actually performed. A successful schema check proves shape only.

Issue triage, prioritization and source acquisition remain separate workflows.
`deep-research-trait` captures provider provenance and curation leads; use the
record or causal-graph review route for a final judgement of those leads.

## Commands and input ownership

Run in TraitMech's environment (`just install` installs project/dev dependencies):

```bash
uv run python scripts/record_review.py inspect --targets /tmp/targets.yaml --input src/traitmech/schema/traitmech.yaml
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
just fetch-record-review-bases
just fetch-record-review-bases --apply
just check-record-reviews
just test-record-reviews
just validate <record-path>
just validate-strict <record-path>
just audit-graphs
```

Use session-unique temporary paths. Capture the entire target, schema and any
inspected source snapshot, ontology release, proposal, mapping or research
input with `inspect --input` before judgement. Keep exact source locations and
bounded ignored-file-inclusive searches for absence findings. Record the
actual commands, exit codes and scope; unavailable required checks produce
partial/blocked observations. Full-corpus graph audits cannot be reported as
focused validation of only a selected record.

`scripts/run_trait_graph_audit.py` delegates acquisition to
`scripts/research_trait.py`; its manifest `ok` and resume predicate describe
research artifacts, not adjudicated findings. Retain those native provenance
and resume contracts. Verify the record and cited literature before authoring
the final structured document; never mechanically convert provider prose into
a passing scientific verdict. This adoption adds no provider calls or batch
expansion and changes no paid-workflow trigger.

Curated record corrections belong to the guarded writer for the maintained
`data/traits/` file. If a defect originates in `scripts/seed_from_metpo.py`, a
source mapping, proposal, or another maintained transform, identify that owner
and its regeneration/acceptance checks instead. Pages and audit reports are
derived products, never the owner of a scientific fix.

## Retained gates

Read `DO_NOT_WORK.md` first and preserve every excluded record untouched.
Include applicable exclusions in review scope; a review does not remove a
curation prohibition. No review bundle appends `curation_history` or repository
history, modifies generated Pages, or promotes `mapping_status: REVIEWED`.
Human sign-off, `record_curation_event`, `write_validated_trait`, strict closed
schema validation, edge evidence, grounding and product checks retain their
existing roles. Authorized later curation still runs the native `just qc` and
other applicable gates.

PR and merge-group `pytest.yaml` executes the common contract test alongside
the existing suite. It supplies `RECORD_REVIEW_BASE` from the trusted PR base
SHA, merge-group base SHA or push-before SHA and checks out full history, so
committed rewrites/deletions of earlier bundles fail the append-only check.
Only explicit manual workflow runs fall back to HEAD (also the local default).
`reviews/structured/<timestamp>-<slug>/review.yaml` and
derived `review.md` are Git-visible immutable observations. Existing research
and ignored report policies remain unchanged.

## Review bases after squash merges

Full main history does not include pre-squash feature commits. Use a full-history
checkout as CI does: recovering a base in a shallow clone can require downloading
unrelated missing ancestry and exceed the command's five-minute Git timeout.
Before checking reviews in a fresh clone, run `just fetch-record-review-bases` to inspect the
plan, then `just fetch-record-review-bases --apply` to recover missing exact
source commits from the matching GitHub repository. The command validates all
bundle pairs and repository identities before fetching; it retains source
commits under local `refs/record-review-bases/<sha>` so Git garbage collection
does not discard them. These are local provenance refs, not feature branches.
No review, working file, remote branch or tag is changed. An unavailable source
commit fails explicitly; do not rewrite the review or skip its provenance check.

CI explicitly runs this preparation before pytest. The native check/test recipes
remain read-only, and the trusted `RECORD_REVIEW_BASE` append-only gate is
unchanged. Direct shared-helper callers and fleet ingestion must prepare their
own object stores too; this native command does not change CLAW ingestion.
A fetched base still establishes only a base for `working_tree` attestations,
not proof that their recorded input bytes were committed. For `git_commit`
reviews the shared validator still checks historical regular-file blob hashes.

After a squash merge, verify review preparation and validation in an independent
single-branch main clone before branch cleanup. Use `--no-local` for a local
clone: a linked worktree or copied object store can conceal missing commits
(#1843). Repeat with a new independent clone after deleting the remote feature
branch; reusing the prepared clone would conceal remote availability failures.
GitHub must still
serve each exact source commit; the command cannot reconstruct a lost object.
