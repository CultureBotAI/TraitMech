---
name: schema-gap-analysis
description: Find gaps between TraitMech's LinkML schema, its METPO-seeded trait YAMLs, and the seeder/causal-graph scripts that write them. Uses linkml-validate as ground truth and reports along three axes (schema / instances / process). Copy-paste runnable.
category: quality
requires_database: false
requires_internet: false
version: 2.1.0
---

# Schema gap analysis (TraitMech)

The conceptual framework — why three axes, error-class heuristics, common anti-patterns — lives once at the cross-Mech version in claw:
https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md

This file is the TraitMech-specific operational version. Every command below runs as-is.

## Setup

TraitMech uses `uv`-managed `.venv/`:

```bash
.venv/bin/linkml-validate --help   # smoke test

# If you hit `AttributeError: Format has no attribute 'JSON'`, pin runtime:
.venv/bin/python -m pip install "linkml-runtime>=1.9,<1.10"
```

## Procedure

TraitMech has no top-level collection file; every trait is its own YAML under `data/traits/<category>/<slug>.yaml`.

### 1. Validate one sample

```bash
SAMPLE=$(ls data/traits/environment/*.yaml | head -1)
.venv/bin/linkml-validate \
  -s src/traitmech/schema/traitmech.yaml \
  -C TraitRecord "$SAMPLE"
```

### 2. Validate the trait corpus

```bash
find data/traits -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/traitmech/schema/traitmech.yaml \
      -C TraitRecord \
      2>&1 | tee /tmp/tm_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/tm_validate.out
```

### 3. Histogram the errors

```bash
grep -oE "Additional properties are not allowed \('[^']+'" /tmp/tm_validate.out \
  | sort | uniq -c | sort -rn

grep -oE "'[^']+' is a required property" /tmp/tm_validate.out \
  | sort | uniq -c | sort -rn

grep -oE "does not match '[^']+'" /tmp/tm_validate.out \
  | sort | uniq -c | sort -rn

grep -oE "is not a '[^']+'" /tmp/tm_validate.out \
  | sort | uniq -c | sort -rn
```

### 4. Cross-check generator drift (Axis 3)

TraitMech's only YAML writer is `scripts/seed_from_metpo.py` (initial seed from METPO OWL). `scripts/trait_causal_graph.py` is a **renderer helper** that reads `record["causal_graphs"]` and shapes it for the page template — it does not write to the YAMLs, so drift there can't introduce schema gaps. All other edits to `data/traits/*.yaml` are made directly by hand or by ad-hoc scripts; those are what the greps below sweep for.

```bash
# Naive datetimes
grep -rnE 'datetime\.now\(\)\.isoformat\b' \
  src/ scripts/ --include='*.py' | grep -v "timezone"

# yaml.dump that drops collection metadata (TraitMech key: traits)
grep -rnE 'yaml\.dump\(\s*\{\s*["\047]traits["\047]\s*:' \
  src/ scripts/ --include='*.py'

# Direct writes that skip the seeder
grep -rnE 'open\([^)]*data/traits/[^)]*["\047][wa][bt]?["\047]' \
  scripts/ src/ --include='*.py'
```

### 5. Re-validate after fixes

```bash
find data/traits -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/traitmech/schema/traitmech.yaml \
      -C TraitRecord \
      2>&1 | grep -c "^\[ERROR\]"
# target: 0
```

## TraitMech-specific state (as of 2026-05-17 pass)

| Surface | Records | Errors |
|---|---:|---:|
| `data/traits/<cat>/*.yaml` | 357 | 0 (clean) |

TraitMech's corpus passes cleanly. Re-run this skill after:
- Re-seeding from a new METPO release (`just seed-from-metpo`).
- Hand-editing `causal_graphs:` blocks into `data/traits/*.yaml` (the renderer reads them but does not write or validate them).
- Schema changes (any edit to `src/traitmech/schema/traitmech.yaml`).

## Pointers

- Schema: `src/traitmech/schema/traitmech.yaml`
- Seeder (the only writer; initial trait creation from METPO): `scripts/seed_from_metpo.py`
- Causal-graph template helper (reads `causal_graphs:`; doesn't write YAML): `scripts/trait_causal_graph.py`
- Page renderer (consumes validated YAML, doesn't write it): `scripts/render_trait_pages.py`
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md)
