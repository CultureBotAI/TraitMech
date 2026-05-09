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

# Validate every YAML under data/traits/
validate-all:
    @find data/traits -name '*.yaml' | xargs -I{} just validate {}

# Seed data/traits/ from data/raw/metpo.owl. Default dry-run.
seed-from-metpo *args:
    uv run python3 scripts/seed_from_metpo.py {{args}}

# Apply the seed (writes YAMLs)
seed-apply:
    uv run python3 scripts/seed_from_metpo.py --apply

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
