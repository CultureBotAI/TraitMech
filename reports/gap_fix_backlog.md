# Gap fix backlog

Ranked by impact × (1/effort). Lead item is always **G01: enable the CI gate** — without it, every other fix can regress on the next merge.

The corpus is currently clean under closed-mode validation (0 ERROR rows across 357 files), so this backlog is about *keeping it clean* and tightening the producer, not repairing existing drift.

## Tier 1 — Land first (enables everything else)

### G01 — Add CI gate running `just validate-strict`
- **Category:** pipeline
- **Effort:** S
- **Why now:** Today nothing blocks a PR that introduces unknown fields or breaks the schema. The audit harness only helps if it runs on every merge candidate. This is the single fix that prevents regression of items G02–G05.
- **Where:** `.github/workflows/validate-strict.yaml`. Trigger on PRs that touch `src/traitmech/schema/**`, `data/traits/**`, or `scripts/seed_from_metpo.py`.
- **Acceptance:** A test PR that adds an unknown field to one trait YAML fails the workflow with a non-zero exit and the offending row in the TSV.

## Tier 2 — Producer-side hardening (blocks future drift)

### G02 — Promote `validate-strict` to be the default, deprecate the open-mode target
- **Category:** pipeline
- **Effort:** S
- **Blocked by:** G01
- **Why:** `just validate-all` currently runs the CLI per-file in open mode and discards exit codes; it is misleading by default. After CI uses `validate-strict`, the open-mode target should either delegate to strict or be removed.
- **Where:** `justfile` (`validate-all:` body), `README.md` validation section.
- **Acceptance:** `just validate-all` either invokes the same closed-mode harness as `just validate-strict`, or is removed in favor of the strict target with a brief README note explaining the change.

### G03 — Validate before write in `scripts/seed_from_metpo.py`
- **Category:** pipeline
- **Effort:** M
- **Blocked by:** G01
- **Why:** The seeder is the *only* producer of new trait YAMLs. It currently writes without validating; the round-trip "seed → strict-validate" is two commands instead of one. Catching errors at seed time means a broken seeder never produces a committed bad record, even on a developer's branch.
- **Where:** `scripts/seed_from_metpo.py` — construct a per-process `Validator(schema=..., validation_plugins=[JsonschemaValidationPlugin(closed=True)])`, call it on each instance before `path.write_text`, log + skip failures, summarize at end.
- **Acceptance:** Seeding with a deliberately broken template (e.g. an unknown attribute) emits a per-record warning and that record is not written. Exit code stays 0 if `--apply` succeeds for any record; non-zero if all fail.
- **Anti-pattern guard:** do not abort the whole run on a single failure — the seed touches hundreds of records.

## Tier 3 — Cleanup (no functional impact, prevents misinterpretation)

### G04 — Document the `required:` asymmetry on `evidence`
- **Category:** schema
- **Effort:** S
- **Why:** `TraitRecord.evidence` is optional; `CausalEdge.evidence` is required. This is intentional (causal claims must carry support; trait records inherit METPO provenance), but a future "harmonization" PR is easy to imagine. Burying the rationale into both `description:` fields makes the policy survive turnover.
- **Where:** `src/traitmech/schema/traitmech.yaml` lines 188–194 (TraitRecord) and 324–329 (CausalEdge).
- **Acceptance:** Both `evidence:` descriptions explicitly state why one is required and the other isn't. No code regen needed since only descriptions change.

### G05 — Suppress auditor self-match in `scripts/audit_writers.py`
- **Category:** pipeline
- **Effort:** S
- **Why:** The auditor's own regex source contains `yaml.safe_dump`, so it matches itself and appears in the writers TSV. It's not a bug — just a cosmetic line of noise that an outside reader will flag every time.
- **Where:** `scripts/audit_writers.py` — `if path.resolve() == Path(__file__).resolve(): return None` near the top of `audit()`.
- **Acceptance:** Re-running `just audit-writers` produces 3 rows instead of 4.

## Items deliberately NOT in the backlog

- **Bulk field-rename migration scripts.** The instance-axis is clean; no field needs to be renamed across the corpus. If a future strict run surfaces `unexpected_field` rows, add a migration script then — not preemptively.
- **Adding identifiers to the four IDless sub-object classes** (`TraitSynonym`, `EvidenceItem`, `CausalEdge`, `CurationEvent`). They are inlined sub-objects, never cross-referenced; adding IDs would be ceremony for no benefit. See `schema_gap_audit.md::S1`.
- **Tightening the suspect-string-slot probe.** Probe surfaced zero hits — schema already uses enums everywhere it should.
- **Pattern broadening for CURIE prefixes.** No CURIE pattern is failing today; broadening preemptively only weakens validation.
