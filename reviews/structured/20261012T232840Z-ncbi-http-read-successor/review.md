# Successor review of NCBI HTTP error and success read-failure retries

- Review: 20261012T232840Z-ncbi-http-read-successor
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-12T23:14:37Z
- Finished UTC: 2026-10-12T23:28:40Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Both confirmed read-failure paths are repaired at this checkpoint: #1899 for HTTP-error diagnostics and #1901 for successful responses. All 38 focused and 4,315 repository tests pass, including eleven new cases previously shown failing across their respective pre-fix implementations. No remaining actionable finding in the expanded code delta. Earlier saved observations remain unchanged; new external approval is still required.

## Scope And Provenance

Two maintained code/test targets covering both HTTP-error-body diagnostics and successful-response protocol failures, with their retry and CLI contracts.

Selection: Exact code delta and regression surface for issues #1899 and #1901; both prior target IDs retained, no sampling.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 3d2d48ab25b979903dd686be4578868ce3ac3186.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ncbi-error-diagnostic | scripts/audit_canonical_examples.py | maintained | NCBI taxonomy HTTP read-failure handling |
| ncbi-error-diagnostic-tests | tests/test_audit_canonical_examples.py | maintained | Canonical-example audit regressions |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_audit_canonical_examples.py --junitxml=/tmp/traitmech-ncbi-success-body-checks-20261012/focused.xml | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| just qc | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| just validate-history | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| just validate-products | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --ncbi-api | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 74e279995781d8faab0ed687201e8c79afc3c95a | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| git diff --check | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-ncbi-success-body-checks-20261012/pytest.xml | passed | True | ncbi-error-diagnostic, ncbi-error-diagnostic-tests | Completed with exit 0; actual command defines its scope. |

## Scientific And Domain Assessments

### Error and successful response failures remain failures

representation: supported. Targets: ncbi-error-diagnostic, ncbi-error-diagnostic-tests.

The helper retains bounded unavailable-body diagnostics, while successful Content-Length and chunked truncation now enter the adapter retry loop. Incomplete bytes are never accepted as labels, and resources close through existing contexts.

### Retry budget, partial results and CLI behavior

consistency: supported. Targets: ncbi-error-diagnostic, ncbi-error-diagnostic-tests.

Three failed requests retain identical bodies/timeouts and [1, 2] backoff. Complete later responses recover; exhaustion reaches RuntimeError and CLI exit 2 without skipped/clean output. Existing partial-success tests still pass, and pending-ID accounting is unchanged.

### Fresh expanded-scope regression and integration validation

completeness: supported. Targets: ncbi-error-diagnostic, ncbi-error-diagnostic-tests.

38 focused and 4,315 full tests pass. QC, history, products, Ruff, committed-diff history and whitespace checks pass. Live NCBI resolves all 761 examples with zero errors and 24 existing warnings; this successful request is not a truncation test.

### Address the supported external finding without inflating it

provenance: supported. Targets: ncbi-error-diagnostic, ncbi-error-diagnostic-tests.

The previously excluded successful-response gap was reproduced, filed as #1901 and repaired on the same PR. All 16 captured inputs match committed checkpoint bytes. Prior review/history are retained. The example-versus-unique-ID distinction is explicit, and no production-likelihood or incident-root-cause claim is inferred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| focused-0 | /tmp/traitmech-ncbi-success-body-checks-20261012/focused-00.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-0 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-00.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-1 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-01.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-2 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-02.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-3 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-03.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-4 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-04.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-5 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-05.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| verify-6 | /tmp/traitmech-ncbi-success-body-checks-20261012/verify-06.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| tests-0 | /tmp/traitmech-ncbi-success-body-checks-20261012/tests-00.log | supports | Fresh successful command output for the expanded checkpoint; not scientific evidence. |
| red-error | /tmp/traitmech-ncbi-truncated-body-five-red-20261012.xml | context_only | Historical initial run: five added HTTP-error-body cases failed before the #1899 helper repair. Their current counterparts are included in the 38 fresh focused passes. |
| red-success | /tmp/traitmech-ncbi-success-body-six-red-20261012.xml | context_only | Six added successful-response cases failed against the implementation at 686ab457 before the adapter edit. Both real Content-Length and chunked HTTP 200 truncation escaped as IncompleteRead; these were code failures, not collection errors. |
| code | scripts/audit_canonical_examples.py; _fetch_ncbi_taxonomy, _ncbi_http_error_detail, _ncbi_api_adapter and main | supports | Re-read both read contexts and the full retry/error propagation. HTTPException is caught in the error diagnostic and adapter; response contexts close, labels update only after a complete parsed return, and pending IDs/backoff are unchanged. No BaseException catch or false-clean fallback. |
| tests | tests/test_audit_canonical_examples.py; All 38 audit cases, especially eleven added cases across the two repairs | supports | Five error-body regressions plus six Content-Length/chunked successful-response cases exercise retries, unchanged request bodies/timeouts, backoff, closure, valid-response recovery and CLI exit 2. Existing partial-response, unavailable-ID and no-resolve behavior remains tested. |
| external | https://github.com/CultureBotAI/TraitMech/pull/1900#pullrequestreview-5496918637 | partial | Changes-requested review correctly identified the explicitly excluded successful-response gap. Its production-likelihood assertion is not established, and 761 example rows are not 761 unique requested IDs. Current source-based count is 340 unique IDs. The supported code finding is addressed as #1901. |
| history | history/infrastructure/ncbi-truncated-success-body/2026-10-12T231337Z-codex-e0885a.yaml | supports | Append-only repair event links #1901, PR #1900 and exact external review. Reports the six red cases, 38 focused passes and unresolved production cause without overwriting earlier history. |
| prior | reviews/structured/20261012T225918Z-ncbi-truncated-error-body/review.yaml | context_only | Earlier self-review explicitly excluded successful-response protocol failures. This successor retains both affected code/test targets and reassesses the expanded scope, while preserving the prior bundle unchanged. |
| python | https://docs.python.org/3.13/library/http.client.html#http.client.IncompleteRead; HTTPException and IncompleteRead hierarchy | supports | Previously directly read Python 3.13 exception documentation; the current real HTTPResponse regressions confirm the relevant runtime inheritance and read failures. |

## Limits And Additional Notes

- Author self-review. The earlier external review requested changes on 686ab457; it is not approval of this new checkpoint. Exact-head approval, CI/merge-group gates, landed integrity and independent before/after-deletion recovery remain subsequent requirements.
- Synthetic in-memory HTTP responses establish the failure modes, not their production frequency or a cause for incident #1898.
- No scientific claim, trait identity, source literature or canonical taxon provenance was reassessed or modified.
- Tests exercise Python 3.13 behavior and representative protocol-read failures; this is not an exhaustive transport or security audit.
- Product validation retains 123 SKIPPED_NO_ADAPTER pairs, 361 canonical labels, two synonyms and one accepted exception. The skipped pairs were not resolved; existing QC baselines remain.
- Zero remaining findings is restricted to this repaired code delta and does not itself close GitHub issues or erase historical review findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T232840Z-ncbi-http-read-successor
kind: repository
repository: CultureBotAI/TraitMech
title: Successor review of NCBI HTTP error and success read-failure retries
started_at: '2026-10-12T23:14:37Z'
finished_at: '2026-10-12T23:28:40Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author adversarial reassessment after external changes-requested
    feedback; not independent review or human scientific sign-off.
skill: User-requested code review following docs/record-reviews.md and docs/record-review-profile.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: 'Both confirmed read-failure paths are repaired at this checkpoint: #1899
  for HTTP-error diagnostics and #1901 for successful responses. All 38 focused and
  4,315 repository tests pass, including eleven new cases previously shown failing
  across their respective pre-fix implementations. No remaining actionable finding
  in the expanded code delta. Earlier saved observations remain unchanged; new external
  approval is still required.'
source:
  git_revision: 3d2d48ab25b979903dd686be4578868ce3ac3186
  state: working_tree
  inputs:
  - path: .github/workflows/canonical-example-taxonomy.yaml
    sha256: 408d06225ee3dff3cdcc42e58cbb1afe77d25c569bcae6260041d32c57d3b967
    role: context
  - path: .github/workflows/pytest.yaml
    sha256: a0db00511a8e875e60347e14efe880b2bc8e37c180f66d9db3de727809557c34
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/infrastructure/ncbi-truncated-error-body/2026-10-12T224549Z-codex-a8b685.yaml
    sha256: 6bf60af18acbae0fea20077072cca0bffe070451238cb7f8c474369827c6b879
    role: context
  - path: history/infrastructure/ncbi-truncated-success-body/2026-10-12T231337Z-codex-e0885a.yaml
    sha256: 5fe111e48ac48bbbbe9da6c54ed8c724fd99a3238515c97bc0406ca03d2d4003
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: reviews/structured/20261012T215358Z-stress-memory-diagnostic-successor/review.yaml
    sha256: a15c07c938e8cc4b6cdcdd4e276721cbdb2465653967465cc43ca96d231886e8
    role: context
  - path: reviews/structured/20261012T225918Z-ncbi-truncated-error-body/review.yaml
    sha256: 6558d7a792d08b1d0b45689a79a07ba6cf4d117b637833b2d0c36910e0c6e2cb
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/audit_canonical_examples.py
    sha256: 3b334e4ec3a5ee2b1c8af589354d400a8ae7c3fbc0d66f574b74345546147701
    role: target
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: tests/test_audit_canonical_examples.py
    sha256: d703003e9ef34510c8bffeff477c0748008b5251011bafd0277bfcd259763a03
    role: target
targets:
- target_id: ncbi-error-diagnostic
  path: scripts/audit_canonical_examples.py
  label: NCBI taxonomy HTTP read-failure handling
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/audit_canonical_examples.py
    role: maintained diagnostic reader, retry adapter and audit CLI
- target_id: ncbi-error-diagnostic-tests
  path: tests/test_audit_canonical_examples.py
  label: Canonical-example audit regressions
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: tests/test_audit_canonical_examples.py
    role: maintained regression tests
scope:
  description: Two maintained code/test targets covering both HTTP-error-body diagnostics
    and successful-response protocol failures, with their retry and CLI contracts.
  selection: 'Exact code delta and regression surface for issues #1899 and #1901;
    both prior target IDs retained, no sampling.'
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exclusions:
  - target: Trait records including protected spore_germination, ontology proposals
      and generated pages
    reason: Unchanged; no scientific review or curation performed.
  - target: Production network incident cause and comparative truncation probability
    reason: No matching production payload, traffic study or cause evidence was obtained.
checks:
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_audit_canonical_examples.py --junitxml=/tmp/traitmech-ncbi-success-body-checks-20261012/focused.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_audit_canonical_examples.py --junitxml=/tmp/traitmech-ncbi-success-body-checks-20261012/focused.xml
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-0
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-0
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-1
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-2
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-3
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --ncbi-api
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --ncbi-api
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-4
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 74e279995781d8faab0ed687201e8c79afc3c95a
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 74e279995781d8faab0ed687201e8c79afc3c95a
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-5
  summary: Completed with exit 0; actual command defines its scope.
- check_id: verify-6
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - verify-6
  summary: Completed with exit 0; actual command defines its scope.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-ncbi-success-body-checks-20261012/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-ncbi-success-body-checks-20261012/pytest.xml
  status: passed
  required: true
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - tests-0
  summary: Completed with exit 0; actual command defines its scope.
evidence:
- evidence_id: focused-0
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/focused-00.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 0b6b2b4b067c9070f6473acaaa7ab8599c81e106737e59c6b944eafa25f1bb1f
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-0
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-00.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 770b6756ab838a35e87ca4ac3ef091a23ebdcb587a5b4c7a3d97d8faaf3c6d2b
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-1
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-01.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: c0bf40de7f0dea446e447920af8b4c329f2aae83465d1dde1c75fde0a7ee1f95
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-2
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-02.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 060fcb191c9b0fceb7dd8ebf172d1055f794292211401b30fa4e7f4ffa819141
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-3
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-03.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-4
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-04.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 4df5d97525f09ebd44359235ea2a4dd5e964e193cdde3d5c84d062b21abd4e6a
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-5
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-05.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 7da4014eba1190880afa2d04adfaccefab522e1ca9db97bb6e0c5ed90c91afd1
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: verify-6
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/verify-06.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: tests-0
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-checks-20261012/tests-00.log
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  snapshot_sha256: 89fb0c5cc5bff7cc17371b3564a1806a2a286c6732402a4c24bf49dafbe86a83
  summary: Fresh successful command output for the expanded checkpoint; not scientific
    evidence.
- evidence_id: red-error
  kind: validation
  reference: /tmp/traitmech-ncbi-truncated-body-five-red-20261012.xml
  accessed_at: '2026-10-12T23:28:40Z'
  support: context_only
  snapshot_sha256: 6e75acc6b26f27b46d85f87a87847b3d725f559234d9c6dde5a412f7a11e5b5b
  summary: 'Historical initial run: five added HTTP-error-body cases failed before
    the #1899 helper repair. Their current counterparts are included in the 38 fresh
    focused passes.'
- evidence_id: red-success
  kind: validation
  reference: /tmp/traitmech-ncbi-success-body-six-red-20261012.xml
  accessed_at: '2026-10-12T23:28:40Z'
  support: context_only
  snapshot_sha256: 408808dac0fe2be4a653b02e54c12828d767ceeb6e66d3dd94c5b536859b621b
  summary: Six added successful-response cases failed against the implementation at
    686ab457 before the adapter edit. Both real Content-Length and chunked HTTP 200
    truncation escaped as IncompleteRead; these were code failures, not collection
    errors.
- evidence_id: code
  kind: record_content
  reference: scripts/audit_canonical_examples.py
  locator: _fetch_ncbi_taxonomy, _ncbi_http_error_detail, _ncbi_api_adapter and main
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  summary: Re-read both read contexts and the full retry/error propagation. HTTPException
    is caught in the error diagnostic and adapter; response contexts close, labels
    update only after a complete parsed return, and pending IDs/backoff are unchanged.
    No BaseException catch or false-clean fallback.
- evidence_id: tests
  kind: record_content
  reference: tests/test_audit_canonical_examples.py
  locator: All 38 audit cases, especially eleven added cases across the two repairs
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  summary: Five error-body regressions plus six Content-Length/chunked successful-response
    cases exercise retries, unchanged request bodies/timeouts, backoff, closure, valid-response
    recovery and CLI exit 2. Existing partial-response, unavailable-ID and no-resolve
    behavior remains tested.
- evidence_id: external
  kind: prior_review
  reference: https://github.com/CultureBotAI/TraitMech/pull/1900#pullrequestreview-5496918637
  accessed_at: '2026-10-12T23:28:40Z'
  support: partial
  summary: 'Changes-requested review correctly identified the explicitly excluded
    successful-response gap. Its production-likelihood assertion is not established,
    and 761 example rows are not 761 unique requested IDs. Current source-based count
    is 340 unique IDs. The supported code finding is addressed as #1901.'
- evidence_id: history
  kind: record_content
  reference: history/infrastructure/ncbi-truncated-success-body/2026-10-12T231337Z-codex-e0885a.yaml
  accessed_at: '2026-10-12T23:28:40Z'
  support: supports
  summary: 'Append-only repair event links #1901, PR #1900 and exact external review.
    Reports the six red cases, 38 focused passes and unresolved production cause without
    overwriting earlier history.'
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261012T225918Z-ncbi-truncated-error-body/review.yaml
  accessed_at: '2026-10-12T23:28:40Z'
  support: context_only
  summary: Earlier self-review explicitly excluded successful-response protocol failures.
    This successor retains both affected code/test targets and reassesses the expanded
    scope, while preserving the prior bundle unchanged.
- evidence_id: python
  kind: authority
  reference: https://docs.python.org/3.13/library/http.client.html#http.client.IncompleteRead
  locator: HTTPException and IncompleteRead hierarchy
  accessed_at: '2026-10-12T22:50:53Z'
  support: supports
  summary: Previously directly read Python 3.13 exception documentation; the current
    real HTTPResponse regressions confirm the relevant runtime inheritance and read
    failures.
assessments:
- assessment_id: both-read-paths
  area: representation
  topic: Error and successful response failures remain failures
  outcome: supported
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  evidence_ids:
  - code
  - tests
  - red-error
  - red-success
  - focused-0
  - python
  summary: The helper retains bounded unavailable-body diagnostics, while successful
    Content-Length and chunked truncation now enter the adapter retry loop. Incomplete
    bytes are never accepted as labels, and resources close through existing contexts.
- assessment_id: contracts
  area: consistency
  topic: Retry budget, partial results and CLI behavior
  outcome: supported
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  evidence_ids:
  - code
  - tests
  - focused-0
  summary: Three failed requests retain identical bodies/timeouts and [1, 2] backoff.
    Complete later responses recover; exhaustion reaches RuntimeError and CLI exit
    2 without skipped/clean output. Existing partial-success tests still pass, and
    pending-ID accounting is unchanged.
- assessment_id: gates
  area: completeness
  topic: Fresh expanded-scope regression and integration validation
  outcome: supported
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  evidence_ids:
  - focused-0
  - tests-0
  - verify-0
  - verify-1
  - verify-2
  - verify-3
  - verify-4
  - verify-5
  - verify-6
  summary: 38 focused and 4,315 full tests pass. QC, history, products, Ruff, committed-diff
    history and whitespace checks pass. Live NCBI resolves all 761 examples with zero
    errors and 24 existing warnings; this successful request is not a truncation test.
- assessment_id: review-remediation
  area: provenance
  topic: Address the supported external finding without inflating it
  outcome: supported
  target_ids:
  - ncbi-error-diagnostic
  - ncbi-error-diagnostic-tests
  evidence_ids:
  - external
  - history
  - prior
  - red-success
  summary: 'The previously excluded successful-response gap was reproduced, filed
    as #1901 and repaired on the same PR. All 16 captured inputs match committed checkpoint
    bytes. Prior review/history are retained. The example-versus-unique-ID distinction
    is explicit, and no production-likelihood or incident-root-cause claim is inferred.'
findings: []
actions: []
limitations:
- Author self-review. The earlier external review requested changes on 686ab457; it
  is not approval of this new checkpoint. Exact-head approval, CI/merge-group gates,
  landed integrity and independent before/after-deletion recovery remain subsequent
  requirements.
- 'Synthetic in-memory HTTP responses establish the failure modes, not their production
  frequency or a cause for incident #1898.'
- No scientific claim, trait identity, source literature or canonical taxon provenance
  was reassessed or modified.
- Tests exercise Python 3.13 behavior and representative protocol-read failures; this
  is not an exhaustive transport or security audit.
- Product validation retains 123 SKIPPED_NO_ADAPTER pairs, 361 canonical labels, two
  synonyms and one accepted exception. The skipped pairs were not resolved; existing
  QC baselines remain.
- Zero remaining findings is restricted to this repaired code delta and does not itself
  close GitHub issues or erase historical review findings.
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261012T225918Z-ncbi-truncated-error-body
  relationship: 'Reassesses both prior code/test targets and expands the previously
    excluded successful-response path after external finding #1901; preserves the
    predecessor unchanged.'
links:
- https://github.com/CultureBotAI/TraitMech/issues/1899
- https://github.com/CultureBotAI/TraitMech/issues/1901
- https://github.com/CultureBotAI/TraitMech/pull/1900
- https://github.com/CultureBotAI/TraitMech/pull/1900#pullrequestreview-5496918637
```
