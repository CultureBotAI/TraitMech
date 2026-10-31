# TraitMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `traitmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/TraitMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: traitmech-infra-0001
    summary: Replace workstation-absolute paths in .claude/skills/traitmech-evolve-workflow/SKILL.md:213 so pr-sanity and qc pass on clean checkouts
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/1962
    disposition: Resolved in PR #1961 (minimal blocker for Stage 1 bootstrap PR CI); upstream coordinator template should also emit configurable CLAW_SRC/CLAW_PYTHON and repository-relative paths.
  - task_id: traitmech-infra-0002
    summary: Document or support section-level attaches_to anchors on Discussion entries when target sections (e.g. causal_graphs) are not yet populated
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/1988
    disposition: Resolved in Cycle 1 Stage 6 (PR #1989, issue #1988); scripts/audit_discussion_anchors.py now supports bare section-level attaches_to anchors (e.g. causal_graphs, ontology_mapping, ecological_interactions) when the target section is empty on the record and rejects them with MALFORMED_ANCHOR once populated, covered by unit tests in tests/test_audit_discussion_anchors.py.
  - task_id: traitmech-infra-0003
    summary: Add an offline structural consistency check for reports/uniprot_grounding_audit.tsv in audit-derived-reports so new protein_examples cannot land without refreshing the tracked report
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/1988
    disposition: Resolved in Cycle 1 Stage 6 (PR #1989, issue #1988); added offline check_inventory / --check-inventory mode to scripts/audit_uniprot_grounding.py, wired it into audit-derived-reports in justfile against git show HEAD:reports/uniprot_grounding_audit.tsv, and added unit tests in tests/test_audit_uniprot_grounding.py.
  - task_id: traitmech-infra-0004
    summary: Add an optional definition_source evidence-coverage warning to scripts/audit_evidence_snippets.py when a record's definition_source is already quoted in-repo on causal_graphs or parent/sibling records but omitted from record-level evidence
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/1981
    disposition: Resolved in Cycle 1 Stage 6 (PR #1989, issue #1981, grouped with #1988); added UNQUOTED_DEFINITION_SOURCE warning to scripts/audit_evidence_snippets.py and unit tests in tests/test_audit_evidence_snippets.py to flag any PMID:/DOI: definition_source omitted from record-level evidence[].reference when a verbatim quote already exists in-corpus.
  - task_id: traitmech-infra-0005
    summary: Fix parent-record CURIE lookup (doc.get("identifier")) and snippet-presence check in scripts/audit_evidence_snippets.py so UNQUOTED_DEFINITION_SOURCE detects unquoted or snippet-less definition_source entries when an in-corpus verbatim quote exists
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/2002
    disposition: Resolved in Cycle 3 Stage 6 (issue #2002, follow-up to #1981); updated scripts/audit_evidence_snippets.py to index and query refs_by_record_id/refs_by_parent_id by doc.get("identifier") (alongside id and path.stem), propagate child quotes to parents, and distinguish snippet-less record-level evidence[] entries from absent references on UNQUOTED_DEFINITION_SOURCE, covered by unit tests in tests/test_audit_evidence_snippets.py.
  - task_id: traitmech-infra-0006
    summary: Skip term_kind OBJECT_PROPERTY records with non-empty predicate-stem snippets in scripts/audit_evidence_snippets.py UNQUOTED_DEFINITION_SOURCE so 1-word predicate stems are not flagged as missing when sibling OBJECT_PROPERTY records have >=12-char stems
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/2002
    disposition: "Resolved in Cycle 4 Stage 6 (issue #2002, follow-up to #1981); updated scripts/audit_evidence_snippets.py so OBJECT_PROPERTY records do not propagate predicate-stem snippets into refs_by_record_id/refs_by_parent_id and accept any non-empty, non-elliptical predicate-stem snippet on definition_source, covered by unit tests in tests/test_audit_evidence_snippets.py."
  - task_id: traitmech-infra-0007
    summary: Extend UNQUOTED_DEFINITION_SOURCE in scripts/audit_evidence_snippets.py to check corpus-wide >=16-char non-elliptical quotes when definition_source is cited in evidence[].reference without a snippet
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/2002
    disposition: "Resolved in Cycle 5 Stage 6 (issue #2002, follow-up to #1981); updated scripts/audit_evidence_snippets.py to track corpus_quoted_refs_16 (>=16-char non-elliptical quotes on non-OBJECT_PROPERTY records) and flag UNQUOTED_DEFINITION_SOURCE when a CLASS record cites definition_source in evidence[].reference without a snippet and a >=16-char quote exists in-corpus, covered by unit tests in tests/test_audit_evidence_snippets.py."
  - task_id: traitmech-infra-0008
    summary: Extend UNQUOTED_DEFINITION_SOURCE in scripts/audit_evidence_snippets.py to resolve DOI-to-PMID reference aliases from data/raw/defense_finder/wiki/List_system_article.md
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/2002
    disposition: "Resolved in Cycle 6 Stage 6 (issue #2002, follow-up to #1981); updated scripts/audit_evidence_snippets.py to resolve DOI<->PMID reference aliases from data/raw/defense_finder/wiki/List_system_article.md (when present) and in-record List_system_article.md evidence snippets when checking UNQUOTED_DEFINITION_SOURCE, covered by unit tests in tests/test_audit_evidence_snippets.py."
  - task_id: traitmech-infra-0009
    summary: Extend _record_wiki_doi_aliases in scripts/audit_evidence_snippets.py to recognize PMC/EuropePMC PPR primary references and pair definition_source DOIs with primary quoted PMID/PMC/EuropePMC references when List_system_article.md, canonical_examples[].reference, or synonyms[].source confirms the same publication
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/2002
    disposition: "Resolved in Cycle 7 Stage 6 (issue #2002, follow-up to #1981); updated _record_wiki_doi_aliases() and added _record_repeats_def_source() in scripts/audit_evidence_snippets.py to recognize PMC (https://pmc.ncbi.nlm.nih.gov/articles/PMC.../, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC...) and EuropePMC PPR (https://europepmc.org/article/PPR/...) primary references alongside PMID: and pair a record's definition_source DOI with its single quoted primary PMID/PMC/EuropePMC reference when the record cites List_system_article.md or repeats definition_source in canonical_examples[].reference or synonyms[].source, covered by unit tests in tests/test_audit_evidence_snippets.py."
  - task_id: traitmech-infra-0010
    summary: Extend has_corpus_16_quote and _record_repeats_def_source in scripts/audit_evidence_snippets.py so UNQUOTED_DEFINITION_SOURCE also checks corpus_quoted_refs_16 when a CLASS record repeats definition_source in canonical_examples[].reference, synonyms[].source, or causal_graphs[].edges[].evidence[].reference
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/2002
    disposition: "Resolved in Cycle 8 Stage 6 (issue #2002, follow-up to #1981); extended _record_repeats_def_source() in scripts/audit_evidence_snippets.py to inspect causal_graphs[].edges[].evidence[].reference alongside canonical_examples[].reference and synonyms[].source, and updated has_corpus_16_quote to trigger for non-OBJECT_PROPERTY records whenever (def_source_in_ev or _record_repeats_def_source(doc, def_source)) and def_source in corpus_quoted_refs_16, covered by unit tests in tests/test_audit_evidence_snippets.py."
  - task_id: traitmech-infra-0011
    summary: Add HTTP 5xx/429 retry with backoff to fetch() in scripts/audit_uniprot_grounding.py so transient rest.uniprot.org 500 responses do not cause false API_ERROR failures during full-corpus refreshes
    status: open
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/1988
```
<!-- mech-infra-tasks:end -->

## Tasks

### `traitmech-infra-0001` — Replace workstation-absolute paths in `.claude/skills/traitmech-evolve-workflow/SKILL.md:213`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 1 (`add_records`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/1962
- **Implementation PR**: https://github.com/CultureBotAI/TraitMech/pull/1961
- **Status**: `resolved`
- **Observation**: The coordinator-installed `.claude/skills/traitmech-evolve-workflow/SKILL.md` embedded workstation-absolute paths on line 213, failing `scripts/pr_sanity.py` (`ABSOLUTE_REPO_PATH` and `SIBLING_ABSOLUTE_PATH`) and `just qc`.
- **Disposition**: Replaced with configurable `CLAW_SRC` / `CLAW_PYTHON` defaults (`../culturebotai-claw/src` and `../culturebotai-claw/.venv/bin/python`) and repository-relative paths (`workflow/mech-workflow.yaml`, `workflow/parent/mech-cycle.yaml`, `workflow/parent/workflow.yaml`) in PR #1961.

### `traitmech-infra-0002` — Document or support section-level `attaches_to` anchors on `Discussion` entries when target sections are not yet populated
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 2 (`causal_graphs`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/1988
- **Implementation PR**: https://github.com/CultureBotAI/TraitMech/pull/1989
- **Status**: `resolved`
- **Observation**: `src/traitmech/schema/traitmech.yaml` defines `Discussion.attaches_to` as free-form strings, while `scripts/audit_discussion_anchors.py` enforces `<section>#<id>` where `<id>` resolves to an existing element inside `<section>`. When recording a `KNOWLEDGE_GAP` or `CURATION_TODO` explaining why an entire section (`causal_graphs`) is absent due to source-limited single-snippet evidence, `attaches_to: ["causal_graphs"]` fails with `MALFORMED_ANCHOR`.
- **Desired outcome**: In Stage 6, either document the `<section>#<id>` syntax constraint directly on `Discussion.attaches_to` in `src/traitmech/schema/traitmech.yaml` (so curators omit `attaches_to` for whole-record/missing-section gaps) or allow a section-level token when `causal_graphs` is empty.
- **Evidence paths**: `src/traitmech/schema/traitmech.yaml`, `scripts/audit_discussion_anchors.py`, `tests/test_audit_discussion_anchors.py`, `scripts/curate_stage2_causal_graphs.py`
- **Priority**: Low
- **Dependencies**: None
- **Disposition**: Resolved in Stage 6 (PR #1989, issue #1988) by adding `EMPTY_SECTION_ANCHORS` support in `scripts/audit_discussion_anchors.py`: bare section-level anchors such as `causal_graphs`, `ontology_mapping`, and `ecological_interactions` are accepted when the target section is empty on the record and rejected with `MALFORMED_ANCHOR` once the section is populated, verified by `tests/test_audit_discussion_anchors.py`.

### `traitmech-infra-0003` — Add an offline structural consistency check for `reports/uniprot_grounding_audit.tsv` in `audit-derived-reports`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 3 (`protein_examples`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/1988
- **Implementation PR**: https://github.com/CultureBotAI/TraitMech/pull/1989
- **Status**: `resolved`
- **Observation**: `scripts/audit_uniprot_grounding.py` queries the live UniProt REST API, so `reports/uniprot_grounding_audit.tsv` is excluded from `audit-derived-reports` (which must remain offline). As a result, when Stage 2 added 6 new `protein_examples`, `reports/uniprot_grounding_audit.tsv` was not flagged as missing those 6 rows, and 110 `ENTRY_VERSION_MISMATCH` findings had accumulated in the tracked TSV. Stage 3 refreshed all 110 `entry_version` values and regenerated `reports/uniprot_grounding_audit.tsv` (163 uses, 0 findings).
- **Desired outcome**: In Stage 6, add an offline `--check-inventory` mode to `scripts/audit_uniprot_grounding.py` (or a lightweight check in `audit-derived-reports`) verifying that the set of `(file, graph_id, node_id, accession, declared_entry_version, declared_sequence_version)` tuples in `reports/uniprot_grounding_audit.tsv` matches the working-tree `data/traits/` YAML files without making network calls.
- **Evidence paths**: `scripts/audit_uniprot_grounding.py`, `tests/test_audit_uniprot_grounding.py`, `reports/uniprot_grounding_audit.tsv`, `justfile`, `scripts/curate_stage3_protein_examples.py`
- **Priority**: Medium
- **Dependencies**: None
- **Disposition**: Resolved in Stage 6 (PR #1989, issue #1988) by adding `declared_inventory_row`, `check_inventory`, and `--check-inventory` to `scripts/audit_uniprot_grounding.py`, wiring the check into `audit-derived-reports` in `justfile` against `git show HEAD:reports/uniprot_grounding_audit.tsv`, and adding unit tests in `tests/test_audit_uniprot_grounding.py`.

### `traitmech-infra-0004` — Add an optional `definition_source` evidence-coverage warning to `scripts/audit_evidence_snippets.py` when a record's `definition_source` is already quoted in-repo
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 4 (`record_review`) / Stage 5 (`resolve_review_findings`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/1981
- **Implementation PR**: https://github.com/CultureBotAI/TraitMech/pull/1989
- **Status**: `resolved`
- **Observation**: During Stage 4 frozen-inventory review of all 1,129 eligible records, 4 records (`data/traits/morphology/cyanophycin_granule.yaml`, `data/traits/environment/cadmium_tolerant.yaml`, `data/traits/environment/cobalt_tolerant.yaml`, and `data/traits/environment/zinc_tolerant.yaml`) were found to declare a primary `definition_source` (`DOI:10.1128/AEM.01298-18` or `PMID:12829273`) that already has a verified verbatim quote in-repo (on the record's own `causal_graphs` edges or on parent/sibling records `metal_tolerant.yaml`/`mercury_tolerant.yaml`) while omitting that reference from record-level `evidence`. All 4 records were remediated in Stage 5 via `scripts/curate_stage5_review_findings.py` (`#1981`).
- **Desired outcome**: In Stage 6, add an advisory check in `scripts/audit_evidence_snippets.py` flagging records whose `definition_source` is absent from `evidence[].reference` whenever `definition_source` already has a verified verbatim snippet in the repository (either on `causal_graphs` edges or on sibling/parent records).
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `scripts/curate_stage5_review_findings.py`, `reviews/structured/20261022T033000Z-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/structured/20261022T052500Z-stage5-remediated-records-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml`
- **Priority**: Low
- **Dependencies**: None (Stage 5 remediation of `F-DEF-SRC-CYANOPHYCIN-001`..`004` completed)
- **Disposition**: Resolved in Stage 6 (PR #1989, issue #1981, grouped with #1988) by adding `UNQUOTED_DEFINITION_SOURCE` (`WARN`) to `scripts/audit_evidence_snippets.py` and unit tests in `tests/test_audit_evidence_snippets.py`.

### `traitmech-infra-0005` — Fix parent-record CURIE lookup (`doc.get("identifier")`) and snippet-presence check in `scripts/audit_evidence_snippets.py` for `UNQUOTED_DEFINITION_SOURCE`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 3, Stage 4 (`record_review`) / Stage 5 (`resolve_review_findings`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/2002 (follow-up to https://github.com/CultureBotAI/TraitMech/issues/1981)
- **Status**: `resolved`
- **Observation**: In `scripts/audit_evidence_snippets.py` (lines 223 and 257), `rec_id = _norm(str(doc.get("id") or path.stem))` indexes `refs_by_record_id` by `doc.get("id")` (falling back to `path.stem`), whereas `TraitRecord` YAML files store their primary CURIE (`METPO:...` or `traitmech:...`) in `doc.get("identifier")` and list parent CURIEs in `parent_traits`. Furthermore, `UNQUOTED_DEFINITION_SOURCE` reported `"is absent from record-level evidence[].reference"` even when `definition_source` appeared in `evidence[].reference` without a non-elliptical verbatim `snippet` while an in-corpus verbatim quote already existed (as seen across 16 of the 17 records remediated in Cycle 3 Stage 5 under `#2002`).
- **Desired outcome**: In Cycle 3 Stage 6, update `scripts/audit_evidence_snippets.py` to index `refs_by_record_id` by `_norm(str(doc.get("identifier") or doc.get("id") or path.stem))` (plus `id` and `path.stem`), propagate child quotes to parents (`refs_by_parent_id.get(rec_id)`), and distinguish snippet-less/elliptical record-level `evidence[]` entries from absent references on `UNQUOTED_DEFINITION_SOURCE`, with unit tests in `tests/test_audit_evidence_snippets.py`.
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `scripts/curate_stage5_review_findings.py`, `reviews/structured/20261023T235000Z-cycle3-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/structured/20261024T025000Z-cycle3-stage5-remediated-records-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/evidence.yaml`
- **Priority**: Medium
- **Dependencies**: None (Cycle 3 Stage 5 remediation of `F-C3S4-DEF-SRC-001`..`017` completed)
- **Disposition**: Resolved in Cycle 3 Stage 6 (issue #2002, follow-up to #1981) by updating `scripts/audit_evidence_snippets.py` to index and query `refs_by_record_id` / `refs_by_parent_id` by `doc.get("identifier")` (alongside `id` and `path.stem`), propagate child quotes to parent records, and distinguish snippet-less/elliptical record-level `evidence[]` entries from absent references on `UNQUOTED_DEFINITION_SOURCE`, verified by unit tests in `tests/test_audit_evidence_snippets.py`.

### `traitmech-infra-0006` — Skip `term_kind: OBJECT_PROPERTY` records with non-empty predicate-stem snippets in `scripts/audit_evidence_snippets.py` `UNQUOTED_DEFINITION_SOURCE`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 4, Stage 4 (`record_review`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/2002 (follow-up to https://github.com/CultureBotAI/TraitMech/issues/1981)
- **Status**: `resolved`
- **Observation**: After Cycle 3 Stage 6 enabled sibling/parent quote propagation via `doc.get("identifier")` (`traitmech-infra-0005`), running `audit_file(p, check_definition_sources=True)` across the full corpus surfaces 26 `term_kind: OBJECT_PROPERTY` records in `data/traits/metabolism/` (`builds_base_from.yaml`, `compartmentalizes.yaml`, `degrades.yaml`, etc., all children of `METPO:2000001` sharing `definition_source: DOI:10.1099/ijsem.0.004332`) because 2 sibling `OBJECT_PROPERTY` records (`produces_acid_from.yaml` with `"acid production"` and `disproportionates.yaml` with `"disproportionation"`) have predicate-stem snippets `>= 12` characters (`_MIN_LEN = 12`), whereas the other 26 `OBJECT_PROPERTY` records carry valid 1-word predicate-stem snippets (`"alkaline"`, `"compartment"`, `"degradation"`, `"oxidation"`, `"reduction"`, `"transport"`, `"growth"`, `"respiration"`, `< 12` characters) that `_has_verbatim_snippet` treats as absent (`len(s) >= _MIN_LEN`).
- **Desired outcome**: In Cycle 4 Stage 6, update `scripts/audit_evidence_snippets.py` so `UNQUOTED_DEFINITION_SOURCE` treats any non-empty, non-elliptical `snippet` on a `term_kind: OBJECT_PROPERTY` record as satisfying `definition_source` snippet coverage (and does not propagate `<12`-char or predicate-stem `OBJECT_PROPERTY` snippets as full-sentence quotes), with unit tests in `tests/test_audit_evidence_snippets.py`.
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `reviews/structured/20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/evidence.yaml`
- **Priority**: Medium
- **Dependencies**: None
- **Disposition**: Resolved in Cycle 4 Stage 6 (issue #2002, follow-up to #1981) by updating `scripts/audit_evidence_snippets.py` so `term_kind: OBJECT_PROPERTY` records do not propagate predicate-stem snippets into `refs_by_record_id` / `refs_by_parent_id` and accept any non-empty, non-elliptical predicate-stem snippet (`min_snip_chars = 1`) as satisfying `definition_source` coverage, verified by unit tests in `tests/test_audit_evidence_snippets.py` and full-corpus `audit(check_definition_sources=True)` (`0` `UNQUOTED_DEFINITION_SOURCE` findings across all 28 `OBJECT_PROPERTY` records).

### `traitmech-infra-0007` — Extend `UNQUOTED_DEFINITION_SOURCE` in `scripts/audit_evidence_snippets.py` to check corpus-wide `>=16`-char non-elliptical quotes when `definition_source` is cited in `evidence[].reference` without a snippet
- **Origin**: `mech-goal-sequence-20261019`, Cycle 5, Stage 4 (`record_review`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/2002 (follow-up to https://github.com/CultureBotAI/TraitMech/issues/1981)
- **Status**: `resolved`
- **Observation**: In `scripts/audit_evidence_snippets.py` (`_collect_in_repo_quoted_refs`), `UNQUOTED_DEFINITION_SOURCE` only inspects quotes on the same record, its immediate 1-hop `parent_traits` (`refs_by_record_id`), its immediate children (`refs_by_parent_id`), or direct siblings sharing an immediate `parent_traits` entry. During Cycle 5 Stage 4 frozen-inventory review, 5 `CLASS` records (`data/traits/genomics/genome_streamlining.yaml`, `data/traits/metabolism/biopolymer_degradation.yaml`, `data/traits/metabolism/denitrification.yaml`, `data/traits/metabolism/sulfur_oxidation.yaml`, and `data/traits/physiology/catalase_activity.yaml`) were found to declare a primary `definition_source` and cite that exact reference in record-level `evidence[0]` without a `snippet`, while a verified non-elliptical verbatim quote (`>=16` chars) from the exact same `definition_source` already exists on a 2-hop ancestor (`nitrogen_respiration.yaml` / `anaerobic_respiration.yaml`) or on a cross-cohort `TraitRecord` (`oligotrophic.yaml`, `saprotrophy.yaml`, `lithotrophic.yaml`, `oxidative_stress_response.yaml`).
- **Desired outcome**: In Cycle 5 Stage 6, extend `scripts/audit_evidence_snippets.py` so that when a `CLASS` record already cites `definition_source` in `evidence[].reference` (`def_source_in_ev == True`) without a non-elliptical verbatim `snippet`, `UNQUOTED_DEFINITION_SOURCE` also checks corpus-wide verified non-elliptical quotes (`>= 16` chars, excluding predicate-stem `OBJECT_PROPERTY` snippets) for that reference, with unit tests in `tests/test_audit_evidence_snippets.py`.
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `reviews/structured/20261025T200500Z-cycle5-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/evidence.yaml`
- **Priority**: Medium
- **Dependencies**: None
- **Disposition**: Resolved in Cycle 5 Stage 6 (issue #2002, follow-up to #1981) by updating `scripts/audit_evidence_snippets.py` to track `corpus_quoted_refs_16` (`>= 16`-char non-elliptical quotes on non-`OBJECT_PROPERTY` records) and trigger `UNQUOTED_DEFINITION_SOURCE` when a `CLASS` record cites `definition_source` in `evidence[].reference` without a snippet while a `>= 16`-char quote exists in-corpus, verified by unit tests in `tests/test_audit_evidence_snippets.py` and full-corpus `audit(check_definition_sources=True)` (`0` `UNQUOTED_DEFINITION_SOURCE` findings across all 1,130 records).

### `traitmech-infra-0008` — Extend `UNQUOTED_DEFINITION_SOURCE` in `scripts/audit_evidence_snippets.py` to resolve DOI↔PMID reference aliases from `data/raw/defense_finder/wiki/List_system_article.md`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 6, Stage 4 (`review_records`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/2002 (follow-up to https://github.com/CultureBotAI/TraitMech/issues/1981)
- **Status**: `resolved`
- **Observation**: In `scripts/audit_evidence_snippets.py`, `UNQUOTED_DEFINITION_SOURCE` checks whether `definition_source` appears in `evidence[].reference` using exact string equality after `_norm()` (`ev_ref == def_source`). During Cycle 6 Stage 4 frozen-inventory review, 13 `CLASS` records in `data/traits/genomics/` (`fs_giy_yig_system.yaml`, `fs_hepn_tm_system.yaml`, `fs_hp_system.yaml`, `fs_hp_sdh_sah_system.yaml`, `fs_hsdr_like_system.yaml`, `fs_sma_system.yaml`, `mazef_system.yaml`, `mok_hok_sok_system.yaml`, `pfiat_system.yaml`, `prrc_system.yaml`, `rloc_system.yaml`, `rnlab_system.yaml`, and `tagi_system.yaml`) were found to declare `definition_source: DOI:...` while citing only the corresponding `PMID:...` alias in `evidence[0].reference` (with a verified verbatim `snippet` and `explanation`), even though `data/raw/defense_finder/wiki/List_system_article.md` maps both the `DOI:` and `PMID:` for the same publication (`MISSING_DEFINITION_SOURCE_EVIDENCE` in `scripts/record_review.py inspect`).
- **Desired outcome**: In Cycle 6 Stage 6, extend `scripts/audit_evidence_snippets.py` so `UNQUOTED_DEFINITION_SOURCE` optionally loads `DOI:`↔`PMID:` equivalence pairs from `data/raw/defense_finder/wiki/List_system_article.md` (when present) and flags records whose `definition_source` is absent from `evidence[].reference` while its mapped `PMID:`/`DOI:` alias is already quoted in `evidence[].reference` on the same record or in-corpus, with unit tests in `tests/test_audit_evidence_snippets.py`.
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `data/raw/defense_finder/wiki/List_system_article.md`, `reviews/structured/20261026T053500Z-cycle6-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/evidence.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/evidence.yaml`
- **Priority**: Medium
- **Dependencies**: None
- **Disposition**: Resolved in Cycle 6 Stage 6 (issue #2002, follow-up to #1981) by adding `_load_defense_finder_ref_aliases()`, `_record_wiki_doi_aliases()`, and `has_alias_quote` in `scripts/audit_evidence_snippets.py` to resolve `DOI:`↔`PMID:` reference aliases from `data/raw/defense_finder/wiki/List_system_article.md` (when present) and from in-record `List_system_article.md` table-row snippets paired with a single quoted `PMID:`, verified by unit tests in `tests/test_audit_evidence_snippets.py` and full-corpus `audit(check_definition_sources=True)` (`0` `UNQUOTED_DEFINITION_SOURCE` findings across all 1,130 records).

### `traitmech-infra-0009` — Extend `_record_wiki_doi_aliases` in `scripts/audit_evidence_snippets.py` to recognize `PMC`/`EuropePMC PPR` primary references and pair `definition_source: DOI:...` with primary quoted `PMID:`/`PMC`/`EuropePMC` references
- **Origin**: `mech-goal-sequence-20261019`, Cycle 7, Stage 4 (`review_records`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/2002 (follow-up to https://github.com/CultureBotAI/TraitMech/issues/1981)
- **Status**: `resolved`
- **Observation**: In `scripts/audit_evidence_snippets.py`, `_record_wiki_doi_aliases()` currently requires `DOI:...` to appear inside the markdown table snippet of an `evidence[]` entry citing `List_system_article.md` and only extracts `PMID:...` references from `record_refs`. During Cycle 7 Stage 4 frozen-inventory review, all 15 remaining DefenseFinder `CLASS` records in `data/traits/genomics/` (`abia_system.yaml`, `abib_system.yaml`, `abic_system.yaml`, `abid_system.yaml`, `abii_system.yaml`, `abir_system.yaml`, `abiu_system.yaml`, `lit_system.yaml`, `card_nlr_endonuclease_system.yaml`, `card_nlr_gasdermin_system.yaml`, `card_nlr_phospho_system.yaml`, `card_nlr_subtilase_system.yaml`, `card_nlr_system.yaml`, `nlr_like_bnacht_system.yaml`, and `pd_t2_1_system.yaml`) whose `definition_source: DOI:...` was absent from `evidence[].reference` (`MISSING_DEFINITION_SOURCE_EVIDENCE` in `scripts/record_review.py inspect`) were found to already carry a verified non-elliptical verbatim quote from that exact `definition_source` publication in `evidence[0]`, cited under its `PMID:`, `https://europepmc.org/article/PPR/PPR668921`, or `https://pmc.ncbi.nlm.nih.gov/articles/PMC.../` alias (with `List_system_article.md` cited in `evidence[]` and/or `definition_source` repeated in `canonical_examples[].reference` or `synonyms[].source`).
- **Desired outcome**: In Cycle 7 Stage 6, extend `_record_wiki_doi_aliases()` in `scripts/audit_evidence_snippets.py` so `UNQUOTED_DEFINITION_SOURCE` also recognizes quoted `PMC` (`https://pmc.ncbi.nlm.nih.gov/articles/PMC.../`) and `EuropePMC PPR` (`https://europepmc.org/article/PPR/...`) primary references in `record_refs` (alongside `PMID:...`) and pairs a record's `definition_source: DOI:...` with its single quoted primary `PMID:`/`PMC`/`EuropePMC` reference when the record also cites `List_system_article.md` or repeats `definition_source` in `canonical_examples[].reference` or `synonyms[].source`, with unit tests in `tests/test_audit_evidence_snippets.py`.
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `reviews/structured/20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/evidence.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/evidence.yaml`
- **Priority**: Medium
- **Dependencies**: None
- **Disposition**: Resolved in Cycle 7 Stage 6 (issue #2002, follow-up to #1981) by adding `_PRIMARY_REF_PREFIXES` and `_record_repeats_def_source()` and extending `_record_wiki_doi_aliases()` in `scripts/audit_evidence_snippets.py` to recognize `PMC` (`https://pmc.ncbi.nlm.nih.gov/articles/PMC.../`, `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC...`) and `EuropePMC PPR` (`https://europepmc.org/article/PPR/...`) primary references alongside `PMID:` and pair a record's `definition_source: DOI:...` with its single quoted primary `PMID:`/`PMC`/`EuropePMC` reference when the record cites `List_system_article.md` or repeats `definition_source` in `canonical_examples[].reference` or `synonyms[].source`, verified by unit tests in `tests/test_audit_evidence_snippets.py` and full-corpus `audit(check_definition_sources=True)` (`0` `UNQUOTED_DEFINITION_SOURCE` findings across all 1,130 records).

### `traitmech-infra-0010` — Extend `has_corpus_16_quote` and `_record_repeats_def_source` in `scripts/audit_evidence_snippets.py` so `UNQUOTED_DEFINITION_SOURCE` also checks `corpus_quoted_refs_16` when a `CLASS` record repeats `definition_source` in `canonical_examples[].reference`, `synonyms[].source`, or `causal_graphs[].edges[].evidence[].reference`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 8, Stage 4 (`review_records`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/2002 (follow-up to https://github.com/CultureBotAI/TraitMech/issues/1981)
- **Status**: `resolved`
- **Observation**: In `scripts/audit_evidence_snippets.py`, `has_corpus_16_quote` (lines 418–422) currently checks `not is_object_property and def_source_in_ev and def_source in corpus_quoted_refs_16`, requiring `def_source_in_ev == True` (`definition_source` already listed in `evidence[].reference`), while `_record_repeats_def_source(doc, def_source)` (lines 166–182) only inspects `canonical_examples[].reference` and `synonyms[].source` (not `causal_graphs[].edges[].evidence[].reference`). During Cycle 8 Stage 4 frozen-inventory review of the `ecology` and `metabolism` cohorts, 12 `ecology` `CLASS` records (`biofilm_formation.yaml`, `commensalism.yaml`, `endosymbiosis.yaml`, `gut_associated.yaml`, `host_associated.yaml`, `mutualism.yaml`, `nitrogen_fixing_symbiosis.yaml`, `opportunistic_pathogen.yaml`, `parasitism.yaml`, `predatory_bacterium.yaml`, `rhizosphere_association.yaml`, and `symbiosis.yaml`) were found to cite `definition_source` in `evidence[0].reference` without a `snippet` (`MISSING_SNIPPET` in `conf/evidence_snippet_baseline.tsv`) while open Europe PMC abstracts provide verified verbatim definitional quotes, and 14 FAPROTAX `metabolism` `CLASS` records (`traitmech:000121`..`traitmech:000134`) were found to repeat `definition_source` in `synonyms[0].source` while omitting it from `evidence[].reference` (`def_source_in_ev == False`). If any of a record's repeated `definition_source` references (in `canonical_examples[].reference`, `synonyms[].source`, or `causal_graphs[].edges[].evidence[].reference`) acquires a `>= 16`-char quote anywhere in `corpus_quoted_refs_16` across a non-sibling cohort while `def_source_in_ev` is `False`, `has_corpus_16_quote` currently fails to flag `UNQUOTED_DEFINITION_SOURCE`.
- **Desired outcome**: In Cycle 8 Stage 6, extend `_record_repeats_def_source(doc, def_source)` in `scripts/audit_evidence_snippets.py` to also check `causal_graphs[].edges[].evidence[].reference` and update `has_corpus_16_quote` to trigger for non-`OBJECT_PROPERTY` records whenever `(def_source_in_ev or _record_repeats_def_source(doc, def_source)) and def_source in corpus_quoted_refs_16`, with unit tests in `tests/test_audit_evidence_snippets.py`.
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `reviews/structured/20261031T091500Z-cycle8-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/evidence.yaml`
- **Priority**: Medium
- **Dependencies**: None
- **Disposition**: Resolved in Cycle 8 Stage 6 (issue #2002, follow-up to #1981) by extending `_record_repeats_def_source()` in `scripts/audit_evidence_snippets.py` to inspect `causal_graphs[].edges[].evidence[].reference` alongside `canonical_examples[].reference` and `synonyms[].source`, and updating `has_corpus_16_quote` to trigger for non-`OBJECT_PROPERTY` records whenever `(def_source_in_ev or _record_repeats_def_source(doc, def_source)) and def_source in corpus_quoted_refs_16`, verified by unit tests in `tests/test_audit_evidence_snippets.py` and full-corpus `audit(check_definition_sources=True)` (`0` `UNQUOTED_DEFINITION_SOURCE` findings across all 1,130 records).

### `traitmech-infra-0011` — Add HTTP 5xx/429 retry with backoff to `fetch()` in `scripts/audit_uniprot_grounding.py`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 9, Stage 3 (`protein_examples`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/1988
- **Status**: `open`
- **Observation**: In `scripts/audit_uniprot_grounding.py`, `fetch(accession)` (lines 147–162) executes a single `urllib.request.urlopen` call against `https://rest.uniprot.org/uniprotkb/{accession}.json` and immediately returns `{"_error": f"HTTP {exc.code}"}` on any `urllib.error.HTTPError` other than `404` or `410`. During the Cycle 9 Stage 3 live refresh of `reports/uniprot_grounding_audit.tsv` across 166 unique accessions (201 uses), `rest.uniprot.org` returned transient `HTTP 500` errors on 3 accessions (`P0DW05`, `A0A099LW44`, and `Q9Z4S6`), causing `audit_uses()` to emit false `API_ERROR` findings even though each accession succeeded immediately on retry.
- **Desired outcome**: In Cycle 9 Stage 6, update `fetch(accession)` in `scripts/audit_uniprot_grounding.py` to retry transient `HTTPError` (`500`, `502`, `503`, `504`, `429`) and `URLError` exceptions with configurable bounded retries and backoff before recording `_error`, with unit tests in `tests/test_audit_uniprot_grounding.py`.
- **Evidence paths**: `scripts/audit_uniprot_grounding.py`, `tests/test_audit_uniprot_grounding.py`, `reports/uniprot_grounding_audit.tsv`
- **Priority**: Medium
- **Dependencies**: None

