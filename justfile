# TraitMech - microbial trait knowledge base seeded from METPO

set dotenv-load := true

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
    /opt/homebrew/bin/python3.13 scripts/build_embedding_index.py

# Render per-trait HTML pages + category indexes + landing into pages/.
gen-pages *args:
    /opt/homebrew/bin/python3.13 scripts/render_trait_pages.py {{args}}

# ============== Deep Research ==============

research_dir := "research"
templates_dir := "templates"

# Deep research on a trait using a specified provider.
# Examples:
#   just research-trait falcon physiology autotrophic
#   just research-trait falcon environment aerobic --dry-run
research-trait provider category slug *args="":
    uv run --extra dev python scripts/research_trait.py \
      --provider {{provider}} \
      --category {{category}} \
      --slug {{slug}} \
      --template {{templates_dir}}/trait_causal_graph_research.md \
      --research-dir {{research_dir}} \
      {{args}}

# List available deep-research-client providers.
research-providers:
    uv run --extra dev deep-research-client providers

# Show detailed availability and parameters for one provider.
research-provider provider:
    uv run --extra dev deep-research-client providers --provider {{provider}}

# Composite: refresh METPO → seed → build embeddings → render pages.
gen-site: seed-apply build-embeddings gen-pages

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

# Composite QC: strict closed-schema validation + schema-quality probes +
# writers audit + proposal citation bar. Mirrors the qc target in
# MediaIngredientMech / CultureMech.
qc: validate-strict audit-schema audit-writers audit-proposals
