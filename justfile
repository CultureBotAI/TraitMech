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
# This is the implementation used by `validate-all` and CI.
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

# Every biolink: CURIE we ground to must name a real slot in the pinned model
# (#342). `encodes` grounded to biolink:encodes with source=biolink and a note
# claiming an exact label match; the model has no such slot. The signal was
# already in reports/biolink_coverage.tsv as the only applied biolink: CURIE with
# both backing columns empty -- and nothing read it, which is the actual defect:
# a report nobody consults is not a check.
#
# Does NOT require the LABEL to match a slot name: most labels are synonyms
# (generates, yields and seven others all ground to biolink:produces). Checks
# the CORPUS as well as the mapping table, because a curator can type a
# predicate_id straight into a record and the CURIE in the record is what a
# reader believes.
#
# A coinage stays legitimate when nothing upstream fits -- but MINT it, as #342
# did for `encodes` (METPO:2007813). Setting source=local does not exempt
# anything; the escape is ALLOWED_UNBACKED in the script, keyed to the CURIE, so
# adding one is a reviewed change rather than a cell edit.
audit-biolink-curies:
    uv run python scripts/audit_biolink_curies.py

# Cross-cohort Scope-A coverage: every traitmech:NNNNNN id in the corpus is
# lifted by SOME proposal cohort (#319). Per-cohort verification cannot assert
# this -- v5 lifts the synthetic traits, v1/v3/v7 lift other things -- and
# demanding it of every cohort failed three of them permanently over work they
# never took on, which is how a check gets ignored.
#
# In qc because it is offline and instant, and because the obligation it tracks
# (an unlifted id has no METPO home and cannot be cross-referenced from
# kg-microbe) accrues silently otherwise: mint traitmech:000121 and nothing
# would notice.
audit-proposal-coverage:
    uv run python scripts/verify_metpo_proposal.py --coverage

# Predicate domain/range audit: `validate-strict` sees predicate_id as a bare
# string, so a CURIE whose ontological domain/range no causal node type can
# satisfy is a false type entailment that passes every other gate. Flags edges
# whose predicate is subPropertyOf METPO:2000001 — microbe domain — on a
# non-organism subject (#301, 366 edges), and enables/RO:0002327 pointed at a
# TRAIT object when its range is 'biological process or activity' (#302, 164).
# Emits reports/predicate_domain_audit.tsv.
#
# THE ORIGINAL TWO CLASSES ARE BURNED DOWN. This shipped as a ratchet over 530
# findings (#314); those decisions landed — #302/#303 via the v8 predicates
# (#320, #323) and #301 via v9 (#326, #328, #329), with the last edge re-grounded
# to RO:0001001 in #327 — so MICROBE_DOMAIN_ON_NONORGANISM is 0 and stays 0.
#
# `--fail-on new` is back, but NOT to excuse those. #315 widened the enables
# check from its original TRAIT-only test to the full biolink range, which
# surfaced 33 edges pointing at proteins, states, qualities, capacities,
# chemicals and locations — a class nothing could see before. They need per-edge
# biological judgement, so they are baselined and tracked for burn-down; the
# ratchet machinery was kept in the script for exactly this case.
#
# The distinction that matters: MICROBE_DOMAIN_ON_NONORGANISM has ZERO rows in
# the baseline, so any regression there is `new` and still fails. A baseline is
# for a class that has never been clean, never for one that has.
#
# Do NOT add rows to the baseline to make a regression pass.
audit-predicate-domains *args:
    uv run python scripts/audit_predicate_domains.py --fail-on new {{args}}

# TraitMech curation-priority queue with a recommended action per record (#448).
# Ported from DisMech's MONDO prioritiser: weighted, YAML-tunable scoring whose
# every component is inspectable, resolving to an ACTION rather than a rank.
#
# One DisMech rule is deliberately inverted. It lumps subtype series into their
# parent; TraitMech does not, because live sibling/parent overlap is measured by
# the command and emitted in its output and dashboard (#481). LUMP_INTO_PARENT
# fires only above the configured measured-overlap threshold.
trait-priority *args:
    uv run python scripts/trait_priority.py {{args}}

# Write the static dashboard to app/dashboard/priority.{html,json}. NOT pages/:
# that tree must byte-match render_trait_pages.py and audit-derived-reports
# enforces it, so a second generator writing there reads as staleness.
gen-priority-dashboard *args:
    uv run python scripts/trait_priority.py --dashboard --top 80 {{args}}

# Check canonical_examples taxon ids against NCBITaxon (#445).
#
# NOT in `qc`, following validate-products: the default resolver needs the 13 GB
# OAK NCBITaxon build. The canonical-example-taxonomy workflow instead uses one
# batched authoritative NCBI request (`--ncbi-api`). Without either resolver the
# id-shape checks still run and resolution is reported as SKIPPED rather than
# passing quietly. ERROR on a malformed/missing/unresolvable id; WARN on label
# drift, since NCBI relabels nodes for its own reasons and a curator-chosen
# display label is not wrong just because upstream added a strain synonym.
audit-canonical-examples *args:
    uv run python scripts/audit_canonical_examples.py {{args}}

# Check that every `discussions[].attaches_to` anchor resolves (#409).
# `attaches_to` is free-form so the schema cannot check it, which made the
# anchors decorative: rename a node in a migration and the discussion silently
# points at nothing. ERROR on an anchor into a section this record has that
# lacks the id; WARN (not ERROR) on a section this audit does not know, because
# the slot is free-form by design and a Mech may anchor somewhere unseen.
audit-discussion-anchors *args:
    uv run python scripts/audit_discussion_anchors.py {{args}}

# Fail when app/discussions/data.js no longer matches the authoritative
# discussions in data/traits (#409). The generator itself is shared from claw,
# but ordinary QC does not have a claw checkout; this credential-free semantic
# projection catches stale rows, counts, links, and facets without rewriting the
# tracked artifact it judges.
audit-discussions-data *args:
    uv run python scripts/audit_discussions_data.py {{args}}

# Flag open PRs that received NO CI at all (#345). PR #344 produced zero
# pull_request workflow runs -- not failures, not skips -- while `gh pr checks`
# said "no checks reported" and mergeStateStatus said CLEAN. Two of the
# workflows that failed to fire carry no `paths:` filter at all, so the usual
# filter explanations do not apply and the mechanism is still unidentified.
#
# This therefore detects the SILENCE rather than any one cause of it, and stays
# meaningful however the runs go missing. Runs triggered by workflow_dispatch do
# NOT count: dispatching by hand is what you do AFTER noticing, so counting it
# would make the check green on exactly the PRs it exists to find.
#
# Needs network and gh auth, so it is NOT in `qc`; it runs from
# pr-checks-present.yaml on pushes to main, where triggering demonstrably works.
audit-pr-checks *args:
    uv run python scripts/audit_pr_checks_present.py {{args}}

# Fail a PR that changes trait records and records no provenance (#325).
#
# history/README.md describes a per-session record as the thing that captures
# WHICH MODEL, USING WHICH TOOL, changed what, why, and under which issue. The
# per-file `curation_history:` block has no slot for any of those, and because it
# hangs off an edit it cannot record a session that changed NOTHING -- an AUDIT
# that checked a trait and correctly found nothing wrong is invisible without a
# record here.
#
# Presence was advisory until #325. Of the 134 commits that modified trait
# records, 2 added a history record; meanwhile 275 records grew an issue number
# hand-typed into a `changes` string, which is the same provenance in a form
# nothing can query.
#
# ONE record per CHANGE, not one per changed file -- that granularity fix is what
# makes this reasonable to block on. Needs a base ref to diff against, so it is
# NOT in `qc`; it runs from curation-history.yaml on pull_request.
audit-history-records *args:
    uv run python scripts/audit_history_records.py {{args}}

# The stronger companion to audit-pr-checks: not "did ANY check fire" but "did
# every check that SHOULD have fired, fire" (#348).
#
# audit-pr-checks can only see TOTAL silence. claude-code-review.yml runs on
# pull_request with no `paths:` filter and records a run even when its `if:`
# gates skip the job, so nearly every PR here has at least one qualifying event
# -- meaning qc, pytest and validate-strict could all be mute and it would still
# pass. This checks each PR-triggered workflow by name instead.
#
# The required set is DERIVED from .github/workflows (every workflow with a
# pull_request trigger), not declared, for the reason #252 gave when it rejected
# a hand-maintained list: a declaration drifts the moment someone adds a
# workflow. Path filters are evaluated against the PR's own changed files, so a
# legitimately filtered-out workflow is not reported.
#
# Needs network and gh auth, so it is NOT in `qc`; same vantage point as
# audit-pr-checks -- pushes to main, where triggering demonstrably works.
audit-required-workflows *args:
    uv run python scripts/audit_required_workflows.py {{args}}

# Structural audit of evidence snippets: EvidenceItem.snippet is specified as a
# VERBATIM quote and docs/CURATION_PLAYBOOK.md sharpens that to contiguous, no
# ellipsis, no paraphrase, diversified across edges — and until #247 nothing
# checked any of it. Flags elliptical, unsupportive, reused and missing
# snippets, plus snippets echoing this trait's own research report.
#
# Same ratchet as audit-graphs: conf/evidence_snippet_baseline.tsv freezes
# today's backlog and only NEW findings fail, so it lands green while #183's
# backfill (thousands of new snippets) cannot make it worse. Regenerate the
# baseline with `--write-baseline` after an intended burn-down, then tighten to
# `just audit-snippets --fail-on any`.
audit-snippets *args:
    uv run python scripts/audit_evidence_snippets.py {{args}}

# Fail when a directory the `qc` chain reads is missing from qc.yaml's paths
# filter. Fourth instance of that bug (#184, #200, #250, #252) — every earlier
# one was caught by review rather than CI. Derives the read-set from the chain
# itself (justfile -> scripts -> REPO_ROOT constants) rather than from a
# declaration, since a declaration is one more thing to forget the same way.
audit-qc-paths:
    uv run python scripts/audit_qc_paths_coverage.py

# Fail if the justfile names a scripts//tests/ Python file that is not tracked
# in git. A recipe only fails when invoked, so a reference to an uncommitted
# script is invisible to every other gate and surfaces at a colleague's
# terminal on a clean checkout. Twice caused by `git add justfile` sweeping up
# someone else's working-tree edits.
audit-justfile-paths *args:
    uv run python scripts/audit_justfile_paths.py {{args}}

# Report graph-level protein, canonical-taxon, semantic-grounding, and
# taxon-paired UniProt-example coverage. Existing coverage gaps remain a
# reported backlog during rollout, but malformed/contradictory examples fail.
# Use `--fail-on gaps` for the completed corpus: it fails on errors too, and
# records listed in DO_NOT_WORK.md report PROTECTED instead of GAP so the
# gate stays reachable. Offline and deterministic.
audit-graph-protein-taxa *args:
    uv run python scripts/audit_graph_protein_taxa.py --fail-on errors {{args}}

# Resolve every UniProtKB protein example against the UniProt REST API and
# verify primary accession, review status, taxon, and entry/sequence versions.
# Also fails if a generic GENE_OR_PROTEIN `grounding` contains UniProtKB.
# Emits reports/uniprot_grounding_audit.tsv.
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

# Repair the fermentation grounding in chemoorganoheterotrophic.yaml (#391). Default dry-run.
reground-fermentation-curie *args:
    uv run python scripts/reground_fermentation_curie.py {{args}}

# Add canonical examples for flagellar arrangement, intracellular inclusion, and
# motility (#444). Default dry-run.
add-morphology-motility-exemplars *args:
    uv run python scripts/add_morphology_motility_exemplars.py {{args}}

# Backfill per-record curation events the protein-taxon tranche omitted (#517). Default dry-run.
backfill-protein-taxon-events *args:
    uv run python scripts/backfill_protein_taxon_events.py {{args}}

# Restore the five canonical-example citations the tranche replaced under an
# "upgrade" label (#519). Default dry-run.
restore-substituted-citations *args:
    uv run python scripts/restore_substituted_citations.py {{args}}

# Install the manifest-locked METPO source. The former sibling-copy recipe could
# silently roll the source back because ../assays remains on 2025-11-25 (#515).
refresh-metpo *args:
    uv run python scripts/refresh_metpo_source.py --apply {{args}}

# Migrate source-owned fields changed by the locked METPO 2026-06-12 release.
# Dry-run by default; stable filenames/ids and evidence snippets are preserved.
migrate-metpo-2026-06-12 *args:
    uv run python scripts/migrate_metpo_2026_06_12.py {{args}}

# Finalize review dispositions for active additions and non-target drift (#534).
# Dry-run by default; --apply updates only the release-delta inventory.
finalize-metpo-2026-06-12-review *args:
    uv run python scripts/finalize_metpo_2026_06_12_review.py {{args}}

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

# Replay the fixed #409 knowledge-gap curation. Validated dry-run by default;
# pass --apply to write the ten in-scope trait records.
curate-knowledge-gaps *args:
    uv run python scripts/curate_knowledge_gaps.py {{args}}

# ============== Curation history (append-only provenance) ==============
# Records which model, using which tool, changed what, why, and under which
# issue. ONE record per change under history/ -- per target for hand curation,
# per migration for a bulk edit (#325) -- never edited after write. Required:
# a PR that changes data/traits and adds no record fails CI. See
# history/README.md. Schema + scaffolder live in claw.

# Scaffold a history record. Prints the path as its last stdout line.
#   just new-history --kind record --slug cellulolysis \
#     --target-root data/traits/metabolism --event EDIT --outcome changed \
#     --summary "..." --details "..." --model <model-id>
# Always use the local scaffolder. The previous claw-preferred branch bypassed
# this repository's bare issue/PR number normalization whenever claw happened to
# be installed (#423), making identical commands produce different link values.
# "$@" not {{args}} — see `set positional-arguments` at the top of this file.
new-history *args:
    uv run python scripts/new_history_record.py "$@"

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
      uv run python scripts/validate_history_links.py "$target"
      find "$target" -name '*.yaml' -print0 \
        | xargs -0 uv run linkml-validate \
            --schema src/traitmech/schema/history.yaml --target-class HistoryRecord
    else
      uv run python scripts/validate_history_links.py "$target"
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

# Rank providers for TraitMech causal-mechanism or definition-grounding work.
deep-research-providers focus="causal_mechanism" *args="":
    uv run --extra dev python scripts/deep_research_provider.py \
      --config conf/deep_research_provider.yaml --focus {{focus}} {{args}}

# Show one provider's focus-specific fit, capabilities, and availability.
deep-research-provider provider focus="causal_mechanism" *args="":
    uv run --extra dev python scripts/deep_research_provider.py \
      --config conf/deep_research_provider.yaml --provider {{provider}} \
      --focus {{focus}} {{args}}

# Composite: refresh METPO → seed → build embeddings → render pages.
gen-site: seed-apply build-embeddings gen-pages

# NOTE: the shared LinkML module (mech_shared.yaml) is vendored byte-identical
# across the Mech repos (package-namespaced path per repo). Its self-generated
# sha256 pin (verify-/refresh-schema-pin) was retired — same self-referential
# flaw as the id-label pin. It is now covered by the manifest-driven drift check:
# scripts/check_vendored_sync.sh verifies the package-specific schema against
# CultureBotAI/culturebotai-claw@<scripts/.vendored_canon_ref>, and claw audits
# the complete five-Mech fleet before an authority release.

# Run tests with coverage
test:
    uv run pytest tests/ -v

test-cov:
    uv run pytest tests/ --cov=traitmech --cov-report=term-missing

# Lint + format
format:
    uv run ruff format src/ scripts/ tests/

# Runs inside `qc`, so a new violation fails CI rather than accumulating.
# It was NOT in qc until #312, and had been failing on main with nobody
# noticing — which meant it gave no signal at all, and telling whether a branch
# added anything required diffing failing-file lists against main by hand.
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
# Fail when a curated node grounding was never written into the trait records.
# audit-derived-reports checks the residual (nodes with NO mapping) is current;
# it cannot see a mapping that exists and was never applied (#460).
audit-unapplied-groundings:
    uv run python scripts/audit_unapplied_groundings.py

# Exact labels are not necessarily unique. Keep the exact-only ambiguity table
# current without requiring the large external ontology snapshots used by the
# full grounding review.
audit-exact-synonym-collisions:
    #!/usr/bin/env bash
    set -euo pipefail
    tmp="$(mktemp)"
    trap 'rm -f "$tmp"' EXIT
    uv run python scripts/audit_exact_synonyms.py \
      --collisions-only --collision-out "$tmp"
    if ! diff -q reports/exact_synonym_collisions.tsv "$tmp" >/dev/null; then
      echo "STALE reports/exact_synonym_collisions.tsv" >&2
      diff -u reports/exact_synonym_collisions.tsv "$tmp" || true
      echo "Regenerate it with:" >&2
      echo "  uv run python scripts/audit_exact_synonyms.py --collisions-only" >&2
      exit 1
    fi
    echo "  OK    reports/exact_synonym_collisions.tsv"

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
    cgc=causal_graph_connectivity.tsv
    # --connectivity-out is NOT optional here. Omitting it would let this
    # check write the connectivity report to its default path in the working
    # tree -- a staleness check that mutates the file it is judging, which is
    # the failure this recipe's header warns about.
    uv run python scripts/audit_causal_graphs.py --out "$tmp/$cga" \
      --connectivity-out "$tmp/$cgc" \
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

    # --- causal_graph_connectivity.tsv, compared against git (#359) ----------
    # Written by the same generator invocation above, so it needs no second
    # run. It carries no ratchet of its own: it is a MEASUREMENT of component
    # structure, and the whole point of #359 is that a number which cannot be
    # gamed by retyping is worth having even when nothing gates on it. Staleness
    # still matters -- an out-of-date copy would misreport whether a PR actually
    # connected anything, which is the one question it exists to answer.
    if [ ! -s "$tmp/$cgc" ]; then
      echo "ERROR: audit_causal_graphs.py produced no connectivity report. Its output:" >&2
      cat "$tmp/gen.log" >&2
      exit 1
    fi
    if ! git show "HEAD:reports/$cgc" > "$tmp/committed_$cgc" 2>/dev/null; then
      echo "  MISSING reports/$cgc is not in git at HEAD" >&2
      stale_cga=1
      fail=1
    elif diff -q "$tmp/committed_$cgc" "$tmp/$cgc" >/dev/null; then
      echo "  OK    reports/$cgc (vs git)"
    else
      echo "  STALE reports/$cgc — the COMMITTED copy is not what audit-graphs produces:" >&2
      { diff -u "$tmp/committed_$cgc" "$tmp/$cgc" | sed -n '1,20p' >&2; } || true
      stale_cga=1
      fail=1
    fi

    # --- graph_protein_taxon_coverage.tsv, compared against git -------------
    # audit-graph-protein-taxa runs earlier in qc and rewrites its working-tree
    # report, so compare the fresh temp output with HEAD just like graph audit.
    gpt=graph_protein_taxon_coverage.tsv
    uv run python scripts/audit_graph_protein_taxa.py --out "$tmp/$gpt" \
      --fail-on none > "$tmp/gen.log" 2>&1
    if [ ! -s "$tmp/$gpt" ]; then
      echo "ERROR: audit_graph_protein_taxa.py produced no report. Its output:" >&2
      cat "$tmp/gen.log" >&2
      exit 1
    fi
    if ! git show "HEAD:reports/$gpt" > "$tmp/committed_$gpt" 2>/dev/null; then
      echo "  MISSING reports/$gpt is not in git at HEAD" >&2
      stale_gpt=1
      fail=1
    elif diff -q "$tmp/committed_$gpt" "$tmp/$gpt" >/dev/null; then
      echo "  OK    reports/$gpt (vs git)"
    else
      echo "  STALE reports/$gpt — the COMMITTED copy is not current:" >&2
      { diff -u "$tmp/committed_$gpt" "$tmp/$gpt" | sed -n '1,20p' >&2; } || true
      stale_gpt=1
      fail=1
    fi

    # --- predicate_domain_audit.tsv, compared against git (#301) -------------
    # Same shape as causal_graph_audit.tsv above: this generator's exit code is
    # its RATCHET VERDICT (--fail-on new), owned by `audit-predicate-domains`
    # earlier in this qc run, not a generation error. So judge only whether the
    # committed copy is stale against git and ignore the status.
    pda=predicate_domain_audit.tsv
    uv run python scripts/audit_predicate_domains.py --out "$tmp/$pda" \
      > "$tmp/gen.log" 2>&1 || true
    if [ ! -s "$tmp/$pda" ]; then
      echo "ERROR: audit_predicate_domains.py produced no report. Its output:" >&2
      cat "$tmp/gen.log" >&2
      exit 1
    fi
    if ! git show "HEAD:reports/$pda" > "$tmp/committed_$pda" 2>/dev/null; then
      echo "  MISSING reports/$pda is not in git at HEAD" >&2
      stale_pda=1
      fail=1
    elif diff -q "$tmp/committed_$pda" "$tmp/$pda" >/dev/null; then
      echo "  OK    reports/$pda (vs git)"
    else
      echo "  STALE reports/$pda — the COMMITTED copy is not what audit-predicate-domains produces:" >&2
      { diff -u "$tmp/committed_$pda" "$tmp/$pda" | sed -n '1,20p' >&2; } || true
      echo "  --- audit-predicate-domains output for this run ---" >&2
      sed -n '1,15p' "$tmp/gen.log" >&2 || true
      stale_pda=1
      fail=1
    fi

    # --- biolink_coverage.tsv, compared against git (#342) -------------------
    # Not gated until #342, and it had drifted: regenerating it there moved 549
    # lines that had nothing to do with the change (produces METPO:2000202 ->
    # METPO:2007800, defines residual -> applied). It is the report that recorded
    # biolink:encodes as unbacked for however long, which is the whole reason
    # audit-biolink-curies had to be written -- a stale report nobody reads is
    # even less of a check than a current one.
    bcv=biolink_coverage.tsv
    uv run python scripts/check_biolink_coverage.py --out "$tmp/$bcv"       > "$tmp/gen.log" 2>&1 || true
    if [ ! -s "$tmp/$bcv" ]; then
      echo "ERROR: check_biolink_coverage.py produced no report. Its output:" >&2
      cat "$tmp/gen.log" >&2
      exit 1
    fi
    if ! git show "HEAD:reports/$bcv" > "$tmp/committed_$bcv" 2>/dev/null; then
      echo "  MISSING reports/$bcv is not in git at HEAD" >&2
      stale_bcv=1
      fail=1
    elif diff -q "$tmp/committed_$bcv" "$tmp/$bcv" >/dev/null; then
      echo "  OK    reports/$bcv (vs git)"
    else
      echo "  STALE reports/$bcv — the COMMITTED copy is not what check-biolink-coverage produces:" >&2
      { diff -u "$tmp/committed_$bcv" "$tmp/$bcv" | sed -n '1,20p' >&2; } || true
      stale_bcv=1
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
    # This used to reject any research block outright, because the renderer
    # reads research/traits/ and research/ was GITIGNORED: a committed
    # research-bearing page could not be reproduced by CI's fresh render, so it
    # would wedge this gate permanently — `just gen-pages` fixes it locally and
    # CI re-breaks it on every push. #230 listed the ways out: stop committing
    # such pages, exclude the block from the comparison, or track the research
    # inputs. #240/#241 took the third — 353 reports are now tracked — which is
    # what let #233 render the block at all.
    #
    # So the collision is gone, and what remains is its precondition. If
    # research/ were ever gitignored again, the two sides would diverge exactly
    # as before, and the failure would surface as an unexplained 353-file STALE
    # rather than as a cause. Guard the premise instead of the symptom.
    #
    # Two ways the premise breaks, with different remedies, so they are reported
    # separately. Testing only "is the directory tracked" would miss the second
    # and reachable one: a curator generates a report, renders, and commits
    # pages/ without committing the report. Locally both sides see it and qc
    # passes; in CI the fresh render has no block and pages/ does (#257).
    if grep -rlq 'class="research-md"' "$pages_tmp" pages/traits 2>/dev/null; then
      # Only the files research_report() can actually select. A sidecar is
      # excluded by the renderer, so an untracked one changes nothing about the
      # render, and claiming otherwise would make the message false (#258).
      untracked_research="$(git ls-files --others --exclude-standard research/traits 2>/dev/null \
        | grep -- '-deep-research-' | grep -Ev '[-.]citations\.md$' | head -3 || true)"
      if [ -z "$(git ls-files research/traits | head -1)" ]; then
        echo "  ERROR a research block is rendered, but research/traits is not" >&2
        echo "        tracked — CI renders no block and pages/ can never match" >&2
        echo "        (#230, #233). Track research/ or drop the block." >&2
        stale_pages=1
        fail=1
      elif [ -n "$untracked_research" ]; then
        echo "  ERROR research reports the renderer can select are not committed," >&2
        echo "        so CI may not reproduce this render (#257):" >&2
        echo "$untracked_research" | sed 's/^/          /' >&2
        echo "  git add research/" >&2
        stale_pages=1
        fail=1
      fi
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
      if [ "${stale_gpt:-0}" -eq 1 ]; then
        echo '  just audit-graph-protein-taxa' >&2
      fi
      if [ "${stale_bcv:-0}" -eq 1 ]; then
        echo '  # biolink_coverage.tsv is regenerated by `just check-biolink-coverage`' >&2
        echo '  just check-biolink-coverage' >&2
      fi
      if [ "${stale_pda:-0}" -eq 1 ]; then
        echo '  # predicate_domain_audit.tsv is regenerated by `just audit-predicate-domains`' >&2
        echo '  # (already run if you got here via `just qc`), then committed.' >&2
        echo '  just audit-predicate-domains' >&2
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
      [ "${stale_gpt:-0}" -eq 1 ] && paths="reports/"
      [ "${stale_pda:-0}" -eq 1 ] && paths="reports/"
      [ "${stale_bcv:-0}" -eq 1 ] && paths="reports/"
      [ "${regen_pages:-0}" -eq 1 ] && paths="$paths pages/"
      # Only when something is actually stageable — an asset-only failure has
      # no paths, and a bare `git add` is not a command anyone can run.
      [ -n "$paths" ] && echo "  git add$(printf ' %s' $paths)" >&2
      exit 1
    fi
    echo "=== derived reports: all current ==="

# Integrity gate for the tracked sweep artifacts: every manifest `ok` row's
# report is on disk AND above a 1 KiB floor (existence is not non-emptiness), no
# report in the resume namespace lacks an `ok` row (the disk-to-manifest
# direction, which a missing-artifact check cannot see), and no artifact carries
# a malformed CURIE (#244). Deliberately
# credential-free and network-free (see run_trait_graph_audit.py --verify), so it
# runs on a fresh clone and in CI — the two places where a lost artifact is
# actually noticed. Plain `uv run`, no `--extra dev`: --verify makes no calls and
# so does not need deep-research-client.
audit-research-artifacts:
    uv run python scripts/run_trait_graph_audit.py --verify

# Composite QC: strict closed-schema validation + schema-quality probes +
# writers audit + proposal citation bar. Mirrors the qc target in
# MediaIngredientMech / CultureMech.
qc: lint pr-sanity validate-strict audit-schema audit-writers audit-proposals audit-proposal-coverage audit-biolink-curies audit-graphs audit-graph-protein-taxa audit-predicate-domains audit-discussion-anchors audit-discussions-data audit-snippets audit-justfile-paths audit-qc-paths audit-exact-synonym-collisions audit-derived-reports audit-unapplied-groundings audit-research-artifacts

# --- id↔label correspondence gate (vendored byte-identical across the Mech repos) ---

# Verify (id,label) pairs in TraitMech's ontology grounding tables correspond to
# the ontology (CHEBI/GO/ENVO/PATO/RO via OAK). Exits non-zero on any mismatch.
# BLOCKING gate in CI (Phase 2); curator-accepted residuals pass via the
# `exceptions:` allow-list in conf/id_label_targets.yaml.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# Rebuild the exact-synonym review from versioned ontology snapshots.  This is
# intentionally not in qc: the official GO/ChEBI/ENVO/PATO/RO/METPO downloads
# are large external inputs, pinned by SHA-256 in the generated manifest rather
# than committed to this repository.  Pass --oak-dir through args for the
# independent OAK sqlite cross-check.
report-exact-synonyms snapshot_dir *args:
    uv run python scripts/audit_exact_synonyms.py --snapshot-dir {{snapshot_dir}} {{args}}

# Download or verify the exact ontology bytes locked by the review manifest.
# Existing mismatched files fail closed and are never overwritten.
fetch-exact-synonym-snapshots snapshot_dir *args:
    uv run python scripts/fetch_exact_synonym_snapshots.py \
      --out-dir {{snapshot_dir}} {{args}}

# Dry-run the approved TraitRecord xrefs/exact synonyms; append --apply to write.
apply-trait-exact-matches snapshot_dir *args:
    uv run python scripts/apply_trait_exact_matches.py --snapshot-dir {{snapshot_dir}} {{args}}

# Baseline (non-failing): do the CURIEs SUGGESTED in the deep-research reports
# mean what those reports say they mean? Writes a ranked backlog to
# reports/research_grounding_backlog.tsv and every occurrence to
# reports/research_grounding_drift.tsv (#243).
#
# Deliberately NOT in `qc`. The reports are provider output that nobody will
# hand-edit 353 of, so failing a build on their contents would gate work on data
# no one intends to correct in place; and the extraction from prose tables is
# heuristic, so some findings are judgement calls. The BLOCKING gate stays where
# the curated data is — `validate-products` over mappings/*.tsv, which is where
# these suggestions land if a curator accepts one.
# Named report-*, not audit-*: every audit-* recipe here is a `qc` member, so
# that prefix reads as a gate this deliberately isn't — the sibling non-gating
# baseline is report-label-drift.
#
# NOT wired into audit-derived-reports, unlike the other tracked reports under
# reports/. Regenerating needs OAK semsql databases, which means network on a
# cold cache, and audit-derived-reports must stay runnable offline. The cost is
# real and is the failure that recipe's own comment describes — a derived
# artifact drifting unwatched — so the report stamps its own vintage and counts
# into reports/research_grounding_backlog.tsv rather than relying on memory.
report-research-groundings *args:
    uv run python scripts/audit_research_groundings.py {{args}}

# Baseline (non-failing): id↔label drift report across the grounding tables to
# reports/label_drift.tsv. Used by CI to publish a triage artifact.
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv

# NOTE: the id↔label validator + its shared tests are vendored byte-identical
# across the Mech repos. The old self-generated sha256 pin (verify-/refresh-
# validator-pin) was retired — it only compared a copy to a hash from the SAME
# repo, so all four could pass while diverged. Drift is now caught by the
# manifest-driven check: the `vendored-sync` CI job runs
# scripts/check_vendored_sync.sh, which verifies these files against
# CultureBotAI/culturebotai-claw@<scripts/.vendored_canon_ref>. To propagate a
# change: PR into claw, merge, then roll the reviewed claw pin across all Mechs.

# Discussions / knowledge-gap browser (shared kg_microbe_discussions in claw).
# Writes app/discussions/{index.html,data.js} from every record's discussions.
gen-discussions-data: (_require-claw "kg_microbe_discussions")
    PYTHONPATH={{claw_src}} uv run python \
      -m kg_microbe_discussions --config conf/discussions_config.yaml --output app/discussions
