# Pipeline / writer audit

Source: `scripts/audit_writers.py` → `reports/pipeline_writers_audit.tsv`.

The auditor's writer-detection heuristic surfaces every Python module that calls `yaml.safe_dump` / `yaml.dump`, or `.write_text(` near a `.yaml` literal. That cast is intentionally wide — it includes false positives (the auditor itself, the HTML renderer, the embedding builder), which the table below resolves manually.

## Raw audit

| path | writes_yaml | curation_history | safeguard | validates_first | wired_into_just |
|---|---|---|---|---|---|
| `scripts/audit_writers.py` | yes | yes | yes | yes | yes |
| `scripts/build_embedding_index.py` | yes | no | no | no | yes |
| `scripts/render_trait_pages.py` | yes | no | yes | no | yes |
| `scripts/seed_from_metpo.py` | yes | yes | yes | no | yes |

## Per-writer reading

### `scripts/seed_from_metpo.py` — the only real trait-YAML writer

This is the entry point for new trait records. It uses the safer **opt-in** convention (`--apply` defaults off; bare invocation is dry-run) and appends `CurationEvent` entries when it writes — both correct. It does **not** validate output against the schema before writing.

**Gap (P1):** add an in-process strict validation pass before each write, using the same `linkml.validator.Validator(closed=True)` configured in `scripts/validate_strict.py`. If a record fails, log + skip rather than abort the whole run, so one bad record doesn't poison a 357-file seed. Effort: M (refactor the writer loop to construct a per-process Validator and call it before `path.write_text`). This is the highest-leverage fix on the pipeline axis because the seeder is the *only* path producing new trait records.

### `scripts/audit_writers.py` — false positive

The auditor reads `yaml.safe_dump` as a string in its own regex source; the heuristic matches itself. The row's "all yes" is meaningless. **Action: none** — could be silenced by short-circuiting `if path == __file__` in `audit_writers.py`, but the marginal cost is a one-line "this is the auditor itself" footnote in the report. Not worth tuning the regex.

### `scripts/render_trait_pages.py` — false positive (writes HTML)

`.write_text()` writes HTML pages; the only YAML touched is read-side. The auditor row's `has_write_safeguard=yes` is incidental — the script does accept `--dry-run`-like args for its own purposes. **Action: none.**

### `scripts/build_embedding_index.py` — false positive (writes JSON)

Line 344 emits the embedding payload via `path.write_text(json.dumps(...))`. The only `.yaml` token in the file is on line 142 (`rglob("*.yaml")` — reading trait files). The auditor's regex flagged the proximity. **Action: none.**

## CI / `just` wiring

All four modules are referenced in `justfile`, so the audit's `wired_into_just=yes` column is correct. What's *missing* on the wiring axis is a **CI gate** running `just validate-strict` on PRs. Today nothing blocks a merge that would re-introduce schema-breaking records. See backlog `G01`.

## Summary against the skill's four-question rubric

| question | answer |
|---|---|
| Does the only real trait-YAML writer append curation history? | Yes (`seed_from_metpo.py`) |
| Does it have a write safeguard? | Yes — `--apply` opt-in (default dry-run) |
| Does it validate before writing? | **No** — gap P1, backlog G03 |
| Is it wired into a `just` target? | Yes (`just seed-from-metpo`, `just seed-apply`) |

## Reproduce

```bash
just audit-writers                                                  # TSV to reports/
uv run python scripts/audit_writers.py --out /tmp/x.tsv && cat /tmp/x.tsv
```
