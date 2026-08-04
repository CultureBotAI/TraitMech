# TraitMech - microbial trait knowledge base seeded from METPO

set dotenv-load := true

# Binds recipe arguments to "$@" in shebang recipes so multi-word arguments keep
# their quoting. Needed by `new-history`, whose --summary/--details are prose;
# plain `{{args}}` interpolation splits them on whitespace. No existing recipe
# uses $1/$@, so enabling this changes nothing else.
set positional-arguments := true

# Shared tooling lives in the culturebotai-claw checkout. Override CLAW_SRC when
# claw is not the default sibling directory — CI checks it out elsewhere.
claw_src := env_var_or_default("CLAW_SRC", "../culturebotai-claw/src")
claw_root := parent_directory(claw_src)

# Fail loudly when a shared claw module is missing, rather than running on and
# producing an empty or wrong result. A skip-when-missing variant of this check is
# exactly what let the vendored-sync job pass while verifying nothing (#182).
_require-claw module:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -d "{{claw_src}}/{{module}}" ]; then
      echo "error: shared module '{{module}}' not found under '{{claw_src}}'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi

default:
    @just --list --unsorted

# Install package + dev tools
install:
    uv sync --extra dev

# Generate Python dataclasses from LinkML schema
gen-schema:
    uv run gen-pydantic src/traitmech/schema/traitmech.yaml > src/traitmech/schema/traitmech_dataclasses.py

# Validate a single trait YAML against the schema
validate file:
    uv run linkml-validate -s src/traitmech/schema/traitmech.yaml \
      --target-class TraitRecord {{file}}

# Validate every YAML under data/traits/. Delegates to validate-strict
# (closed-mode, rejects unknown fields, exits non-zero on any ERROR).
# Previous open-mode implementation ran linkml-validate per file via
# xargs and silently passed unknown fields — see G02 in
# reports/gap_fix_backlog.md.
validate-all *args:
    @just validate-strict {{args}}

# Strict in-process validation in *closed* mode (rejects unknown fields).
# Emits reports/instance_validation_failures.tsv and exits 1 on any ERROR.
# This is what `validate-all` should become once trusted in CI.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Cheap repo-wide checks that run on EVERY PR, including ones that touch only
# docs/ or a new workflow file and so match no other workflow's paths: filter
# (#200). Workflow YAML validity, the "at least one unfiltered workflow"
# invariant, merge-conflict markers, and relative Markdown links. ~0.5s.
pr-sanity *args:
    uv run python scripts/pr_sanity.py {{args}}

# Programmatic schema-quality probes (orphan enums, missing identifiers,
# untyped string slots, etc.). Output to stdout — pipe to a report.
audit-schema:
    uv run python scripts/audit_schema.py

# Audit every YAML-writing Python module for safeguards
# (curation_history append, --dry-run, validates-before-write, wired-into-just).
audit-writers *args:
    uv run python scripts/audit_writers.py {{args}}

# Enforce the citation bar on PROPOSED candidate traits: each must carry
# >= 2 distinct literature citations (across definition_source + evidence).
# Emits reports/proposal_citation_audit.tsv; exits 1 on any short record.
audit-proposals *args:
    uv run python scripts/audit_proposals.py {{args}}

# Structural-integrity audit of causal graphs: dangling edges (subject/object
# not a declared node), orphan nodes (declared but unreferenced), graphs with
# no TRAIT node, and nodes unreachable from the TRAIT node (an island rather
# than one mechanism). Emits reports/causal_graph_audit.tsv.
# Ratchets against conf/causal_graph_audit_baseline.tsv: the 1314 pre-existing
# UNREACHABLE_FROM_TRAIT findings are frozen and never fail, but any NEW finding
# exits 1 — so the corpus cannot get more fragmented than it is today.
# Regenerate the baseline with `--write-baseline` (only when the change is
# intended). Burn it down, then tighten to `just audit-graphs --fail-on any`.
audit-graphs *args:
    uv run python scripts/audit_causal_graphs.py {{args}}

# Fail if the justfile names a scripts//tests/ Python file that is not tracked
# in git. A recipe only fails when invoked, so a reference to an uncommitted
# script is invisible to every other gate and surfaces at a colleague's
# terminal on a clean checkout. Twice caused by `git add justfile` sweeping up
# someone else's working-tree edits.
audit-justfile-paths *args:
    uv run python scripts/audit_justfile_paths.py {{args}}

# Resolve every UniProtKB grounding on GENE_OR_PROTEIN causal nodes against
# the UniProt REST API; classify reviewed / unreviewed / deleted and flag
# accessions reused across trait files. Emits
# reports/uniprot_grounding_audit.tsv; exits 1 on any deleted accession.
# Network-dependent, so it is not part of `just qc`.
# See docs/GROUNDING_POLICY.md.
audit-uniprot *args:
    uv run python scripts/audit_uniprot_grounding.py {{args}}

# Retract UniProtKB groundings whose accessions UniProt has DELETED, demoting
# those nodes to label-only. MERGED accessions are reported, not retracted --
# they carry a live replacement a curator should apply. Dry-run by default.
# See docs/GROUNDING_POLICY.md.
retract-dead-groundings *args:
    uv run python scripts/retract_dead_uniprot_groundings.py {{args}}

# Verify a METPO ROBOT-template proposal cohort under proposals/.
# Runs column-count, header, parent integrity, subset tag, and scope-A/C
# coverage checks. See .claude/skills/metpo-proposal/SKILL.md.
# Example: just verify-proposal metpo_traitmech_v1
verify-proposal cohort *args:
    uv run python scripts/verify_metpo_proposal.py proposals/{{cohort}} {{args}}

# Validate a METPO proposal cohort by compiling its ROBOT-template TSVs,
# merging with data/raw/metpo.owl, and reasoning with ELK. Requires the
# robot binary — picks up $ROBOT, $ROBOT_BIN, or ../kg-microbe/data/raw/robot.
# Example: just robot-validate-proposal metpo_traitmech_v1
robot-validate-proposal cohort *args:
    uv run python scripts/robot_validate_proposal.py proposals/{{cohort}} {{args}}

# Apply mappings/predicate_grounding.tsv to populate empty
# causal_graphs[].edges[].predicate_id across data/traits/.
# Dry-run by default; re-run with --apply to write.
ground-predicates *args:
    uv run python scripts/ground_causal_predicates.py {{args}}

# Apply mappings/node_grounding.tsv to populate empty
# causal_graphs[].nodes[].grounding across data/traits/.
# Keyed on (label, node_type) since the same label can resolve to
# different CURIEs depending on node type (e.g. "terminal electron
# acceptor" as CHEMICAL vs MOLECULAR_FUNCTION).
# Dry-run by default; re-run with --apply to write.
ground-nodes *args:
    uv run python scripts/ground_causal_nodes.py {{args}}

# Cross-check applied mappings + residual labels against the Biolink model.
# Emits reports/biolink_coverage.tsv. Uses data/raw/biolink-model.yaml.
check-biolink-coverage *args:
    uv run python scripts/check_biolink_coverage.py {{args}}

# Seed data/traits/ from data/raw/metpo.owl. Default dry-run.
seed-from-metpo *args:
    uv run python3 scripts/seed_from_metpo.py {{args}}

# Apply the seed (writes YAMLs)
seed-apply:
    uv run python3 scripts/seed_from_metpo.py --apply

# Rename predicate labels across data/traits/ from a TSV mapping. Default dry-run.
rename-predicates *args:
    uv run python scripts/rename_predicate_labels.py {{args}}

# Apply the rename (writes YAMLs)
rename-predicates-apply *args:
    uv run python scripts/rename_predicate_labels.py --apply {{args}}

# Retype causal-graph nodes from a TSV mapping. Default dry-run.
retype-causal-nodes *args:
    uv run python scripts/retype_causal_nodes.py {{args}}

# Apply the retype (writes YAMLs)
retype-causal-nodes-apply *args:
    uv run python scripts/retype_causal_nodes.py --apply {{args}}

# Refresh raw METPO copy from the local KG-Hub assays clone
refresh-metpo:
    cp ../assays/assay-metadata/metpo.owl data/raw/metpo.owl
    @echo "Refreshed data/raw/metpo.owl"

# Build slim deepwalk subset + METPO ↔ kg-microbe-node match table from the
# local kg-microbe deepwalk artifact. Reads
# ../kg-microbe-projects/taxa_media/DeepWalkSkipGramEnsmallen_*.tsv.gz
# (latest available) and ../kg-microbe/mappings/canonical/metpo_alias_mappings.tsv.
build-embeddings:
    uv run python scripts/build_embedding_index.py

# Render per-trait HTML pages + category indexes + landing into pages/.
gen-pages *args:
    uv run python scripts/render_trait_pages.py {{args}}

# QC coverage dashboard (shared kg_microbe_qc generator in culturebotai-claw).
# Reads conf/qc_config.yaml; writes dashboard/index.html + coverage.png.
gen-qc-dashboard: (_require-claw "kg_microbe_qc")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_qc --config conf/qc_config.yaml --output dashboard

# Knowledge-gap scan (Europe PMC, free) via shared kg_microbe_kgscan in claw.
# Dry-run by default → reports/knowledge_gap_scan.{json,md}. Pass `--apply` (and
# e.g. --limit/--min-score) to seed Discussion(kind=KNOWLEDGE_GAP) into records.
knowledge-gap-scan *args: (_require-claw "kg_microbe_kgscan")
    PYTHONPATH={{claw_src}} uv run python -m kg_microbe_kgscan \
      --config conf/kgscan_config.yaml {{args}}

# ============== Curation history (append-only provenance) ==============
# Records which model, using which tool, changed what, why, and under which
# issue. One file per session per target under history/; never edited after
# write. See history/README.md. Schema + scaffolder live in claw.

# Scaffold a history record. Prints the path as its last stdout line.
#   just new-history --kind record --slug cellulolysis \
#     --target-root data/traits/metabolism --event EDIT --outcome changed \
#     --summary "..." --details "..." --model <model-id>
new-history *args: (_require-claw "kg_microbe_history")
    #!/usr/bin/env bash
    set -euo pipefail
    # "$@" not {{args}} — see `set positional-arguments` at the top of this file.
    # `uv run python`, not `python3`: bare python3 is whatever the machine puts
    # first on PATH (miniforge here, not the project venv), which is the same
    # undeclared-interpreter problem the Homebrew paths had.
    PYTHONPATH="{{claw_src}}" uv run python -m kg_microbe_history new "$@"

# Validate one history record, or a directory of them. Uses the VENDORED schema,
# so this works with no claw checkout — same as CI.
validate-history target="history":
    #!/usr/bin/env bash
    set -euo pipefail
    target="{{target}}"
    if [ -z "$target" ]; then
      echo "validate-history: empty target. Pass a record path or a directory." >&2
      exit 2
    fi
    if [ ! -e "$target" ]; then
      echo "validate-history: '$target' does not exist." >&2
      exit 2
    fi
    if [ -d "$target" ]; then
      if [ -z "$(find "$target" -name '*.yaml' -print -quit)" ]; then
        echo "No history records under '$target'."
        exit 0
      fi
      find "$target" -name '*.yaml' -print0 \
        | xargs -0 uv run linkml-validate \
            --schema src/traitmech/schema/history.yaml --target-class HistoryRecord
    else
      uv run linkml-validate \
        --schema src/traitmech/schema/history.yaml --target-class HistoryRecord "$target"
    fi

# ============== Deep Research ==============

research_dir := "research"
templates_dir := "templates"

# Deep research on a trait.
# Provider defaults to `edison` in scripts/research_trait.py (an alias for
# deep-research-client's `falcon`, the Edison research agent). Override by
# passing --provider through as a trailing arg.
#   just research-trait physiology autotrophic                    # Edison
#   just research-trait environment aerobic --dry-run
#   just research-trait environment aerobic --provider openai
research-trait category slug *args="":
    uv run --extra dev python scripts/research_trait.py \
      --category {{category}} \
      --slug {{slug}} \
      --template {{templates_dir}}/trait_causal_graph_research.md \
      --research-dir {{research_dir}} \
      {{args}}

# Edison Scientific deep research (PaperQA3) for one trait record, driven through
# the edison-client SDK rather than deep-research-client. Unlike `research-trait`
# this exposes Edison's job selection and captures full provenance sidecars
# (-response.json, -citations.md, -agent-state.json, -files.json, -meta.yaml).
# target = category/slug, a bare slug (must be unique), or a YAML path.
#   just research-trait-edison physiology/autotrophic --dry-run
#   just research-trait-edison autotrophic --job literature-high
research-trait-edison target *args="":
    uv run --extra dev python scripts/research_trait_edison.py \
      --target {{target}} \
      --template {{templates_dir}}/trait_causal_graph_research.md \
      --out-dir {{research_dir}}/traits \
      {{args}}

# Same, over a JSON list of targets ("category/slug" strings or objects).
#   just research-trait-edison-batch queue.json --limit 5 --dry-run
research-trait-edison-batch batch *args="":
    uv run --extra dev python scripts/research_trait_edison.py \
      --batch {{batch}} \
      --template {{templates_dir}}/trait_causal_graph_research.md \
      --out-dir {{research_dir}}/traits \
      {{args}}

# Retroactively backfill Edison provenance sidecars for past runs (no re-billing).
enrich-edison-response *args="":
    uv run --extra dev python scripts/enrich_edison_response.py {{args}}

# Batch Edison sweep over every REVIEWED CLASS trait that has a causal graph.
# Resumable (skips traits whose report exists), fail-soft, paced, and appends to
# reports/trait_graph_audit_manifest.tsv.
#
# THIS RECIPE EXISTS FOR THE CREDENTIALS, not for convenience. scripts/
# research_trait.py has no load_dotenv, so a run launched outside `just` sees no
# EDISON_API_KEY and every call in the sweep fails instantly — the script says so
# in its own comment. `set dotenv-load := true` at the top of this file is what
# injects the per-repo .env, so the sweep must be launched through here.
#
# PAID: one deep-research call per trait, ~7.5 min each at --workers 1. Canary
# with --limit 1 and check the artifact is on disk and non-empty before any
# fan-out; the exit code alone will not tell you.
#   just trait-graph-sweep --dry-run
#   just trait-graph-sweep --limit 1
#   just trait-graph-sweep --workers 4
trait-graph-sweep *args="":
    uv run --extra dev python scripts/run_trait_graph_audit.py {{args}}

# List available deep-research-client providers.
research-providers:
    uv run --extra dev deep-research-client providers

# Show detailed availability and parameters for one provider.
research-provider provider:
    uv run --extra dev deep-research-client providers --provider {{provider}}

# Composite: refresh METPO → seed → build embeddings → render pages.
gen-site: seed-apply build-embeddings gen-pages

# NOTE: the shared LinkML module (mech_shared.yaml) is vendored byte-identical
# across the Mech repos (package-namespaced path per repo). Its self-generated
# sha256 pin (verify-/refresh-schema-pin) was retired — same self-referential
# flaw as the id-label pin. It is now covered by the shared-reference drift check
# (scripts/check_vendored_sync.sh diffs src/*/schema/mech_shared.yaml against the
# hub's copy at CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>) plus the
# hub's nightly vendored-fleet-audit.yml.

# Run tests with coverage
test:
    uv run pytest tests/ -v

test-cov:
    uv run pytest tests/ --cov=traitmech --cov-report=term-missing

# Lint + format
format:
    uv run ruff format src/ scripts/ tests/

lint:
    uv run ruff check src/ scripts/ tests/

check: lint test

# Fail when a tracked derived report no longer matches what its generator
# produces (#214). These two TSVs are the *work queue* for the grounding backlog
# — section 9 of NEXT_TASKS ranks labels by residual count off them — so a stale
# copy silently sends work at labels that are already grounded. That is not
# hypothetical: `cellobiose` sat in the committed node report for weeks after
# #185 grounded it to CHEBI:17057, and the report only disagreed by that one row,
# which is exactly the size of error nobody notices.
#
# Generates into a temp dir and never touches reports/ — the old habit of
# running the script just to read the numbers, and thereby dirtying a tracked
# file, is the other half of #214.
#
# Compares against the WORKING TREE rather than `git show HEAD:`. In CI the two
# are the same thing, so the invariant enforced there is exactly "the committed
# copy is current". Locally, comparing the working tree means regenerating
# clears the failure immediately, instead of only after you commit — the HEAD
# variant tells you to fix something and then keeps failing when you have.
#
# reports/causal_graph_audit.tsv is checked too, but AGAINST GIT rather than the
# working tree, and the difference is forced (#223). `audit-graphs` rewrites that
# file earlier in this same `qc` run, so by the time this recipe executes the
# working-tree copy is guaranteed fresh and comparing it would always pass while
# a stale committed copy sailed through. Confirmed by appending a bogus row and
# running what qc runs: audit-graphs overwrote it, exited 0, said nothing.
#
# The two comparison bases are not a style choice — they follow from whether
# anything else in the run mutates the file.
audit-derived-reports:
    #!/usr/bin/env bash
    set -euo pipefail
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' EXIT
    # Generator output is captured rather than discarded: swallowing it would
    # leave a bare non-zero exit with nothing to act on. Note that non-zero here
    # has two quite different causes — the script can die outright (no TSV, so
    # staleness is genuinely unknowable), or it can exit 1 having written a
    # perfectly good TSV because some trait YAML was invalid and skipped
    # (`files_skipped_invalid`). The captured log distinguishes them; the
    # message must not assert one of them.
    generate() {
      if ! uv run python "$1" --out "$2" > "$tmp/gen.log" 2>&1; then
        echo "ERROR: $1 exited non-zero — staleness not checked. Its output:" >&2
        cat "$tmp/gen.log" >&2
        exit 1
      fi
    }
    generate scripts/ground_causal_predicates.py "$tmp/predicate_grounding_residual.tsv"
    generate scripts/ground_causal_nodes.py "$tmp/node_grounding_residual.tsv"
    fail=0
    for f in predicate_grounding_residual.tsv node_grounding_residual.tsv; do
      if [ ! -f "reports/$f" ]; then
        echo "  MISSING reports/$f — the generator produced it, the repo has no copy" >&2
        # Same remediation as STALE — regenerate and commit — so this branch has
        # to raise the same flag, or the one failure mode with NO committed file
        # is the one that prints no instructions.
        stale_grounding=1
        fail=1
        continue
      fi
      if diff -q "reports/$f" "$tmp/$f" >/dev/null; then
        echo "  OK    reports/$f"
      else
        echo "  STALE reports/$f — not what the generator produces:" >&2
        # `|| true` is load-bearing: diff exits 1 on a difference, pipefail
        # propagates that through the pipeline, and `set -e` would abort the
        # recipe HERE — skipping `fail=1`, skipping the second report, and
        # making the remediation block below unreachable in exactly the case
        # it exists for.
        { diff -u "reports/$f" "$tmp/$f" | sed -n '1,20p' >&2; } || true
        stale_grounding=1
        fail=1
      fi
    done
    # --- causal_graph_audit.tsv, compared against git (#223) -----------------
    # This generator's exit code is its RATCHET VERDICT (--fail-on new), not a
    # generation error, and `audit-graphs` already owns that verdict earlier in
    # this same qc run. Judging staleness on it would conflate "the corpus got
    # more fragmented" with "the committed report is out of date". So the status
    # is deliberately ignored and only missing output is fatal.
    cga=causal_graph_audit.tsv
    uv run python scripts/audit_causal_graphs.py --out "$tmp/$cga" \
      > "$tmp/gen.log" 2>&1 || true
    if [ ! -s "$tmp/$cga" ]; then
      echo "ERROR: audit_causal_graphs.py produced no report. Its output:" >&2
      cat "$tmp/gen.log" >&2
      exit 1
    fi
    if ! git show "HEAD:reports/$cga" > "$tmp/committed_$cga" 2>/dev/null; then
      echo "  MISSING reports/$cga is not in git at HEAD" >&2
      # Same reason as the grounding MISSING branch: same remediation, so the
      # same flag, or the case with nothing committed prints no instructions.
      stale_cga=1
      fail=1
    elif diff -q "$tmp/committed_$cga" "$tmp/$cga" >/dev/null; then
      echo "  OK    reports/$cga (vs git)"
    else
      echo "  STALE reports/$cga — the COMMITTED copy is not what audit-graphs produces:" >&2
      { diff -u "$tmp/committed_$cga" "$tmp/$cga" | sed -n '1,20p' >&2; } || true
      # Print the generator's own output here too, not only on missing output.
      # audit() silently `continue`s past a trait YAML that fails safe_load
      # (audit_causal_graphs.py:106-108) — no counter, no row — so an
      # unparseable file drops its findings from the fresh copy and this reads
      # as a stale COMMITTED report when the committed report was fine. Same
      # care the generate() helper above takes: the message must not assert a
      # cause the evidence does not establish.
      echo "  --- audit-graphs output for this run ---" >&2
      sed -n '1,15p' "$tmp/gen.log" >&2 || true
      stale_cga=1
      fail=1
    fi

    # --- pages/, compared against the working tree (#230) --------------------
    # Only checkable at all since #228 made the renderer deterministic; before
    # that a fresh build differed from every committed page on the timestamp
    # alone. Rendered into the temp dir via --out, never into pages/ — this
    # generator wipes and recreates its output root, so pointing it at pages/
    # to verify pages/ would destroy what is being compared.
    #
    # Working tree, not `git show HEAD:` — nothing else in a qc run rewrites
    # pages/, which is the property that forced the other basis for
    # causal_graph_audit.tsv.
    pages_tmp="$tmp/pages"
    if ! uv run python scripts/render_trait_pages.py --out "$pages_tmp" \
         > "$tmp/gen.log" 2>&1; then
      echo "ERROR: render_trait_pages.py failed — pages staleness not checked:" >&2
      cat "$tmp/gen.log" >&2
      exit 1
    fi
    if [ ! -d pages ]; then
      echo "  MISSING pages/ — the renderer produced output, the repo has none" >&2
      stale_pages=1
      # Regenerating IS part of the fix here — gen-pages recreates the directory
      # — so unlike the orphan case this branch should say so.
      regen_pages=1
      # But not the WHOLE fix: the hand-vendored assets went with the directory
      # and gen-pages never emits them, so `git add pages/` alone would stage
      # their deletion. The per-asset loop below only runs when pages/ exists,
      # so name them here. The restore line prints above the git add, which is
      # the ordering that makes this safe to follow top to bottom.
      lost_assets=" pages/d3.v7.min.js pages/theme-toggle.js"
      fail=1
      pages_diff=""
    else
    # The renderer reads research/traits/ (render_trait_pages.py) to embed a
    # research block, and research/ is GITIGNORED — it exists on a curator's
    # machine and never in CI. A committed research-bearing page is therefore
    # unreproducible by a fresh render and would wedge this gate permanently:
    # `just gen-pages` fixes it locally and CI re-breaks it on every push.
    # Nothing is affected today (no page under pages/traits/ carries one), so
    # this names the collision rather than silently producing a confusing
    # STALE. If the research block is ever wanted in committed pages, the fix
    # is to exclude it from the comparison, not to weaken the gate.
    # Checks the RENDERED side as well as the committed one, and names whichever
    # fired. The collision arises on a curator's machine, where research/ exists
    # and the fresh render grows a block the committed page lacks — so testing
    # only the committed side would miss the very direction this guards, and
    # reporting "pages/ carries" in that case would name the wrong side.
    research_side=""
    grep -rlq 'class="research-md"' "$pages_tmp" 2>/dev/null \
      && research_side="the fresh render"
    if grep -rlq 'class="research-md"' pages/traits 2>/dev/null; then
      [ -n "$research_side" ] && research_side="$research_side and pages/" \
        || research_side="pages/"
    fi
    if [ -n "$research_side" ]; then
      echo "  ERROR $research_side carries a research block, rendered from" >&2
      echo "        gitignored research/ and cannot be reproduced in CI (#230)." >&2
      stale_pages=1
      fail=1
    fi
    # Excusing these two from the diff is not the same as tolerating their
    # absence: the renderer never emits them, so nothing else would notice if
    # they were deleted, and umap.html/graph.html break without d3. Require
    # them explicitly rather than only exempting them.
    for asset in d3.v7.min.js theme-toggle.js; do
      if [ ! -f "pages/$asset" ]; then
        echo "  MISSING pages/$asset — hand-vendored, never regenerated" >&2
        # NOT stale_pages: that flag's remediation is `just gen-pages` then
        # `git add pages/`, and neither restores this — gen-pages does not emit
        # it, and `git add` would stage the deletion and make the loss
        # permanent. Restoring from git is the only fix.
        lost_assets="${lost_assets:-} pages/$asset"
        fail=1
      fi
    done
    # Only those two are excused by NAME. Dropping the whole `Only in pages`
    # direction would also hide an orphan — a page for a trait that was deleted
    # or renamed, which `just gen-pages` does not sweep because it does not pass
    # --clean by default.
    # diff exits 0 (same), 1 (differences) or >1 (error). `|| true` alone folded
    # an ERROR into an empty result, which then read as OK — the same fail-open
    # both sibling blocks treat as fatal. Capture the status instead.
    set +e
    pages_raw="$(diff -rq "$pages_tmp" pages)"
    diff_rc=$?
    set -e
    if [ "$diff_rc" -gt 1 ]; then
      echo "  ERROR diff failed on pages/ (exit $diff_rc) — staleness not checked" >&2
      exit 1
    fi
    if [ -z "$pages_raw" ]; then
      pages_diff=""
    else
      pages_diff="$(printf '%s\n' "$pages_raw" \
        | grep -vE '^Only in pages: (d3\.v7\.min\.js|theme-toggle\.js)$' || true)"
    fi
    fi
    if [ -n "$pages_diff" ]; then
      echo "  STALE pages/ — not what render_trait_pages.py produces:" >&2
      printf '%s\n' "$pages_diff" | sed -n '1,15p' >&2
      n=$(printf '%s\n' "$pages_diff" | wc -l | tr -d ' ')
      echo "  ($n path(s) differ)" >&2
      # An "Only in pages" line is an ORPHAN — a page whose trait YAML was
      # deleted or renamed. `just gen-pages` cannot clear it (it overwrites and
      # never deletes, since --clean is not the default), so recommending it
      # would loop: regenerate, `git add` stages nothing, next run fails
      # identically. `--clean` is worse, not better: it rmtree's pages/, and the
      # `git add pages/` printed below would then stage the deletion of both
      # hand-vendored assets. Name the orphans and say `git rm`.
      orphans="$(printf '%s\n' "$pages_diff" | sed -nE 's|^Only in (pages[^:]*): (.*)$|\1/\2|p' || true)"
      # Only recommend regenerating if something other than an orphan differs.
      #
      # `grep -v`, NOT `grep -qv`: -q exits on the first matching line, and with
      # pipefail the resulting SIGPIPE on printf became the pipeline's status,
      # short-circuiting the `&&` so regen_pages stayed unset. The flagship case
      # is exactly where it bites — a template edit makes all 505 pages differ,
      # ~66 KB of diff text against a 64 KB pipe capacity, so printf blocks
      # while grep is already exiting. The curator then saw STALE with no
      # remediation at all, because orphans and lost_assets are empty too.
      # Reading the whole stream removes the race rather than widening it.
      non_orphan="$(printf '%s\n' "$pages_diff" | grep -v '^Only in pages' || true)"
      [ -n "$non_orphan" ] && regen_pages=1
      stale_pages=1
      fail=1
    elif [ "${stale_pages:-0}" -eq 0 ] && [ -z "${lost_assets:-}" ]; then
      # Every way this block can fail has to be represented here, or "OK pages/"
      # prints underneath the line that just said otherwise. Both conditions are
      # load-bearing: stale_pages covers the absent-pages/ and research-block
      # branches, lost_assets covers a deleted vendored asset — which
      # deliberately does NOT set stale_pages, because its remediation is a
      # restore rather than a regenerate.
      echo "  OK    pages/"
    fi

    if [ "$fail" -ne 0 ]; then
      echo "" >&2
      echo "derived reports are stale (#214, #223). Regenerate and commit them:" >&2
      # Guarded so a cga-only failure does not send the curator to run two
      # grounding scripts that have nothing to do with what failed.
      if [ "${stale_grounding:-0}" -eq 1 ]; then
        echo "  uv run python scripts/ground_causal_predicates.py" >&2
        echo "  uv run python scripts/ground_causal_nodes.py" >&2
      fi
      if [ "${stale_cga:-0}" -eq 1 ]; then
        # Names the command rather than asserting the run: under `just qc`,
        # audit-graphs has already refreshed the working-tree copy and this is a
        # no-op, but standalone `just audit-derived-reports` refreshed nothing
        # and a bare `git add reports/` would stage nothing and fail identically
        # next time.
        #
        # Single-quoted on purpose: backticks inside a double-quoted echo are
        # command substitution, and this string names a command.
        echo '  # causal_graph_audit.tsv is regenerated by `just audit-graphs`' >&2
        echo '  # (already run if you got here via `just qc`), then committed.' >&2
        echo '  just audit-graphs' >&2
      fi
      # Only when regenerating can actually fix it — an orphan-only failure is
      # cleared by git rm, and gen-pages would loop.
      if [ "${regen_pages:-0}" -eq 1 ]; then
        echo '  just gen-pages' >&2
      fi
      if [ -n "${orphans:-}" ]; then
        echo "  git rm$(printf ' %s' $orphans)" >&2
      fi
      if [ -n "${lost_assets:-}" ]; then
        echo "  git checkout --${lost_assets}" >&2
      fi
      # Name the directory that actually changed. A pages-only failure told the
      # curator to `git add reports/`, which stages nothing and fails the same
      # way next run.
      paths=""
      [ "${stale_grounding:-0}" -eq 1 ] && paths="reports/"
      [ "${stale_cga:-0}" -eq 1 ] && paths="reports/"
      [ "${regen_pages:-0}" -eq 1 ] && paths="$paths pages/"
      # Only when something is actually stageable — an asset-only failure has
      # no paths, and a bare `git add` is not a command anyone can run.
      [ -n "$paths" ] && echo "  git add$(printf ' %s' $paths)" >&2
      exit 1
    fi
    echo "=== derived reports: all current ==="

# Integrity gate for the tracked sweep artifacts: every manifest `ok` row's
# report is on disk, and no artifact carries a malformed CURIE. Deliberately
# credential-free and network-free (see run_trait_graph_audit.py --verify), so it
# runs on a fresh clone and in CI — the two places where a lost artifact is
# actually noticed. Plain `uv run`, no `--extra dev`: --verify makes no calls and
# so does not need deep-research-client.
audit-research-artifacts:
    uv run python scripts/run_trait_graph_audit.py --verify

# Composite QC: strict closed-schema validation + schema-quality probes +
# writers audit + proposal citation bar. Mirrors the qc target in
# MediaIngredientMech / CultureMech.
qc: pr-sanity validate-strict audit-schema audit-writers audit-proposals audit-graphs audit-justfile-paths audit-derived-reports audit-research-artifacts

# --- id↔label correspondence gate (vendored byte-identical across the Mech repos) ---

# Verify (id,label) pairs in TraitMech's ontology grounding tables correspond to
# the ontology (CHEBI/GO/ENVO/PATO/RO via OAK). Exits non-zero on any mismatch.
# BLOCKING gate in CI (Phase 2); curator-accepted residuals pass via the
# `exceptions:` allow-list in conf/id_label_targets.yaml.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# Baseline (non-failing): id↔label drift report across the grounding tables to
# reports/label_drift.tsv. Used by CI to publish a triage artifact.
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv

# NOTE: the id↔label validator + its shared tests are vendored byte-identical
# across the Mech repos. The old self-generated sha256 pin (verify-/refresh-
# validator-pin) was retired — it only compared a copy to a hash from the SAME
# repo, so all four could pass while diverged. Drift is now caught by the
# shared-reference check: the `vendored-sync` CI job runs
# scripts/check_vendored_sync.sh, which diffs these files against
# CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>. To propagate a change:
# PR into that hub → merge → bump .vendored_canon_ref here.

# Discussions / knowledge-gap browser (shared kg_microbe_discussions in claw).
# Writes app/discussions/{index.html,data.js} from every record's discussions.
gen-discussions-data: (_require-claw "kg_microbe_discussions")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_discussions --config conf/discussions_config.yaml --output app/discussions
