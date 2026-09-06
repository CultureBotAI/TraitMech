---
name: add-trait
description: Add a named microbial ecophysiological trait as a TraitRecord YAML with METPO-first identity, source-backed definition, optional canonical examples and causal graphs, curation history, repository history, generated pages, and validation. Use when the target trait is already named.
---

# Add a TraitRecord

This skill turns one named, in-scope microbial trait into a validated
TraitMech record.

Use `trait-priority` when choosing among existing curation targets. Use
`deep-research-trait` or `research-causal-graphs` when an existing record needs
paid literature research before its causal graph can be curated. Use
`manage-identifiers` for every ID lookup or fallback minting decision.

## Read first

- `CLAUDE.md` for mutation, derived-artifact, history, and validation rules.
- `docs/CURATION_PLAYBOOK.md` for trait boundaries, examples, evidence snippets,
  and causal-graph patterns.
- `docs/GROUNDING_POLICY.md` before adding or editing `GENE_OR_PROTEIN` causal
  nodes or `protein_examples`.
- `history/README.md` for repository-level curation history.
- `.claude/skills/manage-identifiers/SKILL.md` for METPO-first identifiers and
  the fallback `traitmech:NNNNNN` workflow.
- `src/traitmech/schema/traitmech.yaml` for allowed `TraitRecord` fields.
- `DO_NOT_WORK.md` to avoid touching a protected existing record while checking
  parent or sibling context.
- The closest existing `data/traits/<category>/*.yaml` record, to copy local
  shape but not facts.

## Accept or reject

Add the record only if the target is a reusable microbial
ecophysiological trait or METPO relation:

- phenotype, capability, growth condition, environmental preference, cellular
  morphology, genome-level quality, ecological role, or assayable physiological
  disposition
- quantitative parent or bin when METPO defines the full meaning or the record
  can be proposed upstream as a stable ontology term
- `term_kind: CLASS`, `OBJECT_PROPERTY`, or `DATATYPE_PROPERTY` matching the
  exact METPO term semantics
- at least one citable definition source for a curator-minted term
- at least two distinct DOI/PMID-backed citations for a new
  `mapping_status: PROPOSED` local term

Reject organism-level observations, one-off database columns, source-specific
field names, predicted profile rows, precomposed chemical-use pairs, genes,
proteins, pathways without a trait, broad placeholders, and traits already
represented by an existing exact record. For rejected near misses, record the
reason in the response or an attached `discussions` item on the exact existing
record so the same target is not repeatedly triaged as missing.

## Prove it is new

Before writing anything, search exact identifiers, labels, synonyms, likely
slugs, key citations, and xrefs across the whole repository, including ignored
and hidden files:

```bash
rg --no-ignore --hidden -n \
  "<METPO CURIE>|<traitmech CURIE>|<slug>|<label>|<synonym>|<DOI>|<PMID>" \
  .
```

Search `data/raw/metpo.owl`, `data/traits`, `parent_traits`, `xrefs`,
`synonyms`, `causal_graphs`, `discussions`, `research/`, `proposals/`,
generated pages, and `history/`. If a prior mention is only a rejection or a
METPO proposal, read it before continuing. Never search broad prefixes such as
`DOI:10`, `PMID:`, or `METPO:` to prove absence.

When you report "no existing record" or "no prior proposal", explicitly say the
search included ignored and hidden files.

## Identity

TraitMech is METPO-first:

1. Search `data/raw/metpo.owl` for an exact class or property for the target.
2. If METPO already has the term, use the METPO CURIE as `identifier`.
3. If the term is in METPO but missing under `data/traits`, run the seeder
   against a temporary output root and copy only the target YAML into the real
   tree:

   ```bash
   set -euo pipefail
   tmp="$(mktemp -d)"
   trap 'rm -rf "$tmp"' EXIT
   uv run python scripts/seed_from_metpo.py --out "$tmp" --apply
   target="$(rg --glob '*.yaml' -l '^identifier: <METPO CURIE>$' "$tmp" || :)"
   test -n "$target"
   relative="${target#"$tmp"/}"
   destination="data/traits/$relative"
   test ! -e "$destination"
   mkdir -p "$(dirname "$destination")"
   cp "$target" "$destination"
   ```

   Never run bare `just seed-apply` for a one-record add; the seeder has no
   target filter and can emit every missing METPO term. Preserve the
   seeder-chosen category and generated file name, including any slug collision
   suffix, and do not overwrite an existing real record.
4. If METPO has no exact term and the trait is in scope, mint the next
   zero-padded `traitmech:NNNNNN` through `manage-identifiers`.
5. File or reference a METPO upstream issue for every minted `traitmech:` ID.

Use `parent_traits` only for true broader trait classes. Put true equivalent
external terms in `xrefs`; do not use `xrefs` for broader, narrower, merely
related, or source-column mappings. If a candidate METPO, GO, CHEBI, ENVO, OBI,
RO, MICRO, PATO, NCBITaxon, InterPro, Pfam, NCBIfam, ComplexPortal, or UniProtKB
accession has not been resolved at its issuing authority, leave it out and add
a `CURATION_TODO` discussion describing what must be checked.

## Evidence bundle

Make the first record small but independently reviewable:

- `definition`: one sentence that states the trait, not the source column that
  suggested it
- `definition_source`: a METPO source for seeded records or a DOI/PMID for
  curator-minted records
- `trait_category`: the enum matching the filesystem category
- `term_kind`: `CLASS`, `OBJECT_PROPERTY`, or `DATATYPE_PROPERTY`
- `mapping_status`: leave generated METPO skeletons as `SEEDED`; use
  `PROPOSED` for first-pass model-drafted `traitmech:` records; set `REVIEWED`
  only after human curator signoff
- `synonyms`: exact, broad, narrow, or related labels only when the declared
  scope is defensible
- `evidence`: DOI/PMID-backed literature that supports the definition or major
  curation claims
- `canonical_examples`: organisms with direct source support for the trait,
  not taxa inferred from a pathway or protein paper
- `discussions`: `CURATION_TODO`, `KNOWLEDGE_GAP`, or controversy notes for
  unresolved but reviewable gaps

Do not put paraphrases in `snippet`. `snippet` is a verbatim, contiguous span
from the cited source; put interpretation in `notes`.

Keeping first-pass local records at `PROPOSED` leaves them in the
`just audit-proposals` two-citation gate until a human curator promotes them to
`REVIEWED`.

## Causal graphs

Add `causal_graphs` only when the trait has source-backed mechanism structure.
Do not add graphs for `OBJECT_PROPERTY` or `DATATYPE_PROPERTY` relation
records, chemical-use relation carriers, or traits whose biology is completely
covered by a more specific child.

A first graph should be readable and source-bounded:

- 5 to 7 nodes for a concrete phenotype with a known mechanism
- 3 to 4 nodes for a quantitative bin or classification-axis record
- one `TRAIT` node grounded to this record's `identifier`
- `scope_status` and, for nonmechanistic contexts, `scope_notes`
- `node_id` values that mean the same thing everywhere they are reused in the
  corpus
- stable local `graph_id` values
- taxon-agnostic node groundings when exact ontology or database CURIEs exist
- `protein_examples` only for reviewed UniProt primary accessions paired with
  taxon metadata and direct evidence
- directed `edges` with `subject`, `predicate`, `object`, `description`, and
  DOI/PMID-backed `evidence`
- `predicate_id` only when an exact relation CURIE has been curated
- no orphan nodes: every declared node must be referenced by at least one edge
- no disconnected mechanistic branches: every node in a `MECHANISTIC` graph
  must connect back to the `TRAIT` node

Generic states, capacities, and intermediates may stay ungrounded. Do not add a
node or edge just to make the graph look complete.

## Write the record

For a METPO-owned record, generate a temporary seed tree and copy only the
target YAML into `data/traits` so unrelated emitted METPO skeletons stay
disposable. For a curator-minted record, create
`data/traits/<category>/<slug>.yaml` from a small Python dictionary and write it
through `write_validated_trait`.

Every manual edit to a new or seeded record must:

- load the existing YAML with `yaml.safe_load`
- append a `record_curation_event(..., llm_assisted=True)`
- write with `write_validated_trait`
- leave unrelated generated fields and source-owned seeded fields alone

Do not hand-serialize YAML or loosen the `write_validated_trait` round-trip
test if formatting drifts.

For every added record, create repository-level history:

```bash
just new-history \
  --kind record \
  --slug <slug> \
  --target-root data/traits/<category> \
  --event CREATE \
  --outcome changed \
  --sections identity,evidence,canonical_examples,causal_graphs \
  --summary "<short summary>" \
  --details "<what was added and which sources justify it>" \
  --actor-name <actor> \
  --model <model> \
  --agent-tool <agent-tool>
```

## Validate

Validate the new record directly with the maintained LinkML wrapper before
broader gates:

```bash
just validate data/traits/<category>/<slug>.yaml
```

Then run the checks whose scope LinkML does not cover:

```bash
just validate-strict data/traits/<category>/<slug>.yaml
just validate-history history/records/<slug>
just audit-proposals
just audit-graphs
just ground-predicates
just ground-nodes
just audit-predicate-domains
just audit-graph-protein-taxa
just check-biolink-coverage
just gen-pages
just gen-priority-dashboard
git diff --check
just qc
```

Also run `just verify-snippets --record data/traits/<category>/<slug>.yaml`
after adding a `snippet`. Run `just validate-products` when adding or editing
CHEBI formula-bearing chemicals, and run `just audit-uniprot` after adding or
editing `protein_examples`. Run `just build-embeddings` before `just gen-pages`
only when the sibling DeepWalk artifacts named by
`scripts/build_embedding_index.py` are present; otherwise report that embedding
artifacts were not regenerated.

When `just ground-predicates` or `just ground-nodes` proposes exact CURIEs you
accept, rerun that recipe with `--apply` before repeating downstream audits.

## Report

End with:

- new identifier, label, category, and file path
- strongest identity source and strongest mechanism source
- every DOI, PMID, CURIE, source accession, and taxon id added
- curation-history event and repository history record
- generated pages or derived reports that changed
- validation commands that passed
- any `CURATION_TODO` or upstream METPO issue left open
- whether duplicate and absence searches included ignored and hidden files
