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
  the fallback `traitmech:NNNNNN` allocation workflow.
- `.claude/skills/metpo-proposal/SKILL.md` before minting a `traitmech:`
  fallback, so the temporary local ID gets a same-PR upstream proposal.
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
- at least two distinct DOI/PMID/stable-URL citations for a new
  `mapping_status: PROPOSED` local term

Reject organism-level observations, one-off database columns, source-specific
field names, predicted profile rows, precomposed chemical-use pairs, genes,
proteins, pathways without a trait, broad placeholders, and traits already
represented by an existing exact record. Treat lexical variants or METPO family
variants as duplicates when they only add a context suffix, assay polarity, or
capability wrapper to a trait already represented at the exact same scope. For
rejected near misses, record the reason in the response or an attached
`discussions` item on the exact existing record so the same target is not
repeatedly triaged as missing.

Diagnostic and commercial enzyme-panel labels also need interpretation before
acceptance. Treat kit well names, chromogenic-substrate names, and ambiguous
panel rows as evidence leads, not trait labels; reject a row when its only
stable biology collapses to an existing activity record, and keep the kit string
out of `EXACT_SYNONYM` unless papers use it as a true trait name.

Sequence-feature-like candidates need an explicit interpretation pass before
they are accepted. Do not add a literal locus, gene, operon, protein domain,
regulatory site, mobile-element sequence, or source-database feature row as a
TraitRecord. Add a GENOMICS record only when the record denotes a reusable
organism-, strain-, or genome-level property, such as possession of a mobile
element class or a sequence-composition phenotype; keep unresolved source labels
out of `EXACT_SYNONYM` and record borderline mapping questions as
`CURATION_TODO` discussions.

## Prove it is new

Before writing anything, search exact identifiers, labels, synonyms, likely
slugs, key citations, and xrefs across the whole repository, including ignored
and hidden files:

```bash
rg --no-ignore --hidden -n \
  "<METPO CURIE>|<traitmech CURIE>|<slug>|<label>|<synonym>|<DOI>|<PMID>|<stable URL>" \
  .
```

Search `data/raw/metpo.owl`, `data/traits`, `parent_traits`, `xrefs`,
`synonyms`, `causal_graphs`, `discussions`, `research/`, `proposals/`,
generated pages, and `history/`. If a prior mention is only a rejection or a
METPO proposal, read it before continuing. Never search broad prefixes such as
`DOI:10`, `PMID:`, `https://`, or `METPO:` to prove absence.

When you report "no existing record" or "no prior proposal", explicitly say the
search included ignored and hidden files.

If a seeded METPO label looks absent only because it adds a suffix such as
`activity`, `capability`, `positive`, or `flagellation`, inspect the parent and
same-family sibling records before copying the skeleton. Skip the candidate if
the existing local record already carries the exact phenotype, and explain that
semantic duplicate explicitly.

Do not treat a temporary seeder output directory as a missing-work queue. It is
a reusable METPO projection that can contain records already live under
`data/traits`, and it goes stale as soon as another add-trait PR lands. For each
candidate, copy by exact identifier, then prove absence against the live tree
and `history/` with the ignored-and-hidden search above.

## Identity

TraitMech is METPO-first:

1. Search `data/raw/metpo.owl` for an exact class or property for the target.
2. If METPO already has the term, use the METPO CURIE as `identifier`.
3. If the term is in METPO but missing under `data/traits`, run the seeder
   against a temporary output root and copy only the target YAML into the real
   tree:

   ```bash
   set -euo pipefail
   tmp="$(mktemp -d /tmp/traitmech-seed.XXXXXX)"
   .venv/bin/python scripts/seed_from_metpo.py --out "$tmp" --apply
   target="$(rg --no-ignore --hidden --glob '*.yaml' -l '^identifier: <METPO CURIE>$' "$tmp" || :)"
   test -n "$target"
   relative="${target#"$tmp"/}"
   destination="data/traits/$relative"
   test ! -e "$destination"
   mkdir -p "$(dirname "$destination")"
   cp "$target" "$destination"
   ```

   Never run the whole-tree `seed-apply` recipe for a one-record add; the seeder has no
   target filter and emits a broad METPO skeleton tree. Preserve the
   seeder-chosen category and generated file name, including any slug collision
   suffix, and do not infer novelty from a target file merely existing under a
   temporary seed root.
4. If METPO has no exact term and the trait is in scope, mint the next
   zero-padded `traitmech:NNNNNN` through `manage-identifiers`.
5. Add or extend a METPO ROBOT-template proposal for every minted
   `traitmech:` ID. The same PR that adds the local record must reserve the
   upstream `METPO:` placeholder, document the round-trip path, and verify the
   proposal. If a separate upstream METPO issue already exists, reference it,
   but do not substitute an issue link for a proposal artifact.

Use `parent_traits` only for true broader trait classes. Put true equivalent
external terms in `xrefs`; do not use `xrefs` for broader, narrower, merely
related, or source-column mappings. If a candidate METPO, GO, CHEBI, ENVO, OBI,
RO, MICRO, PATO, NCBITaxon, InterPro, Pfam, NCBIfam, ComplexPortal, or UniProtKB
accession has not been resolved at its issuing authority, leave it out and add
a `CURATION_TODO` discussion describing what must be checked.

`xrefs` are emitted as `oboInOwl:hasDbXref`, so they cannot carry
`skos:*Match` strength. Leave close, narrow, broad, medium-confidence, or
otherwise scope-qualified mappings out of the TraitRecord xrefs; put them in
METPO proposal SSSOM or an explicit discussion instead.

For cell-level enzyme-activity TraitRecords, same-label GO catalytic-activity
classes usually denote the molecular function rather than an equivalent
organismal phenotype. If a GO term is exact for a causal node but shifted for
the record's `xrefs`, leave it out of `xrefs` and record the decision in a
`CURATION_TODO` discussion or proposal notes.

When a local parent is the genus in the new definition, do not borrow endpoints,
substrates, products, or pathway branches from that parent unless the new
trait's own scope and evidence support them. A child term can be narrower than
its parent on one axis and deliberately silent on another.

## Evidence bundle

Make the first record small but independently reviewable:

- `definition`: one sentence that states the trait, not the source column that
  suggested it
- `definition_source`: a METPO source for seeded records or a DOI, PMID, or
  stable URL for curator-minted records
- `trait_category`: the enum matching the filesystem category
- `term_kind`: `CLASS`, `OBJECT_PROPERTY`, or `DATATYPE_PROPERTY`
- `mapping_status`: leave generated METPO skeletons as `SEEDED`; use
  `PROPOSED` for first-pass model-drafted `traitmech:` records; set `REVIEWED`
  only after human curator signoff
- `synonyms`: exact, broad, narrow, or related labels only when the declared
  scope is defensible
- `evidence`: DOI/PMID/stable-URL-backed literature that supports the
  definition or major curation claims
- `canonical_examples`: organisms with direct source support for the trait,
  not taxa inferred from a pathway or protein paper
- `discussions`: `CURATION_TODO`, `KNOWLEDGE_GAP`, or controversy notes for
  unresolved but reviewable gaps

Every added record needs at least one DOI, PMID, or stable URL in
`definition_source` or `evidence`; a bare uncited seed skeleton is not enough.

Do not put paraphrases in `snippet`. `snippet` is a verbatim, contiguous span
from the cited source; put interpretation in `notes`.

For new records, prefer a `snippet` on every DOI/PMID/stable-URL evidence item
that supports a definition, canonical example, graph edge, or curation
decision. If the source exposes no concise contiguous passage for that claim,
leave `snippet` absent and make `notes` say exactly what the citation supports;
never synthesize a quote to make the record look complete.

Use source-system group keys, database column names, and other identifier-like
strings as `RELATED_SYNONYM` provenance labels by default, especially when they
contain underscores. Promote one to `EXACT_SYNONYM` only when it is a true
lexical name for the same trait.

Apply that scope test to METPO proposal synonyms too. For enzyme-activity
phenotypes, a bare enzyme name usually names the molecule rather than the
organismal phenotype; keep it out of TraitRecord `EXACT_SYNONYM` and proposal
`exact_synonyms` unless a source uses that bare string as a phenotype label, and
store useful shifted labels as `RELATED_SYNONYM` or `related_synonyms` instead.

An evidence snippet must carry the specific definition claim it is attached to.
Do not use article titles, section headings, keyword fragments, or generic noun
phrases that name the topic but do not support the asserted substrate, endpoint,
energy-conservation role, taxon scope, or direction.

A `SEEDED` METPO record still needs DOI, PMID, or stable-URL evidence when prior
review artifacts marked the term as lacking corpus demand or primary support.
Use METPO or its source axiom for `definition_source`, and add literature
evidence that justifies the TraitMech record.

Keeping first-pass local records at `PROPOSED` leaves them in the
`scripts/audit_proposals.py` two-citation gate until a human curator promotes them to
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
  DOI/PMID/stable-URL-backed `evidence`
- `predicate_id` only when an exact relation CURIE has been curated
- no orphan nodes: every declared node must be referenced by at least one edge
- no disconnected mechanistic branches: every node in a `MECHANISTIC` graph
  must connect back to the `TRAIT` node

Generic states, capacities, and intermediates may stay ungrounded. Do not add a
node or edge just to make the graph look complete.

Positive or negative assay-result children of a reviewed activity parent often
need only their definition, evidence, and a direct canonical example. Do not add
a child graph when the reviewed parent already captures the molecular mechanism
and the child merely records assay polarity.

## Write the record

For a METPO-owned record, generate a temporary seed tree and copy only the
target YAML into `data/traits` so unrelated emitted METPO skeletons stay
disposable. For a curator-minted record, create
`data/traits/<category>/<slug>.yaml` from a small Python dictionary and write it
through `write_validated_trait`.

For every curator-minted `traitmech:` record, add the companion METPO proposal
under `proposals/metpo_traitmech_v<N>/` in the same branch. Use the
`metpo-proposal` skill, reserve the proposed `METPO:` identifier, keep shifted
or enzyme-name-only labels in `related_synonyms` instead of `exact_synonyms`,
and omit SSSOM mappings when there is no exact external equivalence to assert.

Every manual edit to a new or seeded record must:

- load the existing YAML with `yaml.safe_load`
- append a `record_curation_event(..., llm_assisted=True)`
- write with `write_validated_trait`
- leave unrelated generated fields and source-owned seeded fields alone

Do not hand-serialize YAML or loosen the `write_validated_trait` round-trip
test if formatting drifts.

For every added record, create repository-level history:

```bash
.venv/bin/python scripts/new_history_record.py \
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

Update every record-count mention in the root `README.md` whenever the new
`data/traits` record changes a category or total count. This includes the corpus
statistics table and any prose or layout comments that quote the total number of
curated records; derive the numbers live instead of incrementing one visible
counter by hand.

## Validate

Validate the new record directly with the maintained LinkML wrapper before
broader gates:

```bash
.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml \
  --target-class TraitRecord data/traits/<category>/<slug>.yaml
```

Then run the checks whose scope LinkML does not cover:

```bash
.venv/bin/python scripts/validate_strict.py data/traits/<category>/<slug>.yaml
.venv/bin/python scripts/validate_history_links.py history/records/<slug>
.venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml \
  --target-class HistoryRecord history/records/<slug>/<record>.yaml
.venv/bin/python scripts/audit_schema.py
.venv/bin/python scripts/audit_writers.py
.venv/bin/python scripts/audit_proposals.py
.venv/bin/python scripts/verify_metpo_proposal.py proposals/<cohort>
.venv/bin/python scripts/verify_metpo_proposal.py --coverage
.venv/bin/python scripts/audit_causal_graphs.py
.venv/bin/python scripts/ground_causal_predicates.py
.venv/bin/python scripts/ground_causal_nodes.py
.venv/bin/python scripts/audit_biolink_curies.py
.venv/bin/python scripts/audit_predicate_domains.py --fail-on new
.venv/bin/python scripts/audit_graph_protein_taxa.py --fail-on gaps
.venv/bin/python scripts/audit_canonical_examples.py --no-resolve
.venv/bin/python scripts/check_biolink_coverage.py
.venv/bin/python scripts/audit_evidence_snippets.py
.venv/bin/python scripts/audit_exact_synonyms.py --collisions-only
.venv/bin/python scripts/audit_unapplied_groundings.py
.venv/bin/python scripts/audit_discussion_anchors.py
.venv/bin/python scripts/audit_discussions_data.py
.venv/bin/python scripts/pr_sanity.py
.venv/bin/python scripts/audit_justfile_paths.py
.venv/bin/python scripts/audit_qc_paths_coverage.py
.venv/bin/python scripts/run_trait_graph_audit.py --verify
.venv/bin/python scripts/check_sources.py
.venv/bin/python scripts/render_trait_pages.py
.venv/bin/python scripts/trait_priority.py --dashboard --top 80
git diff --check
.venv/bin/ruff check src scripts tests
.venv/bin/python -m pytest tests/test_readme_artifacts.py tests/test_trait_priority.py -v --tb=short
.venv/bin/python -m pytest -q
```

Also run `.venv/bin/python scripts/verify_snippets.py --record data/traits/<category>/<slug>.yaml`
after adding a `snippet`. A `VERIFIED` row is decisive for an abstract quote;
for `NOT_IN_ABSTRACT`, `UNRESOLVED`, or URL-backed evidence, open the source
directly and confirm the recorded text is still a contiguous, verbatim source
span. When adding or editing `canonical_examples`, run
`.venv/bin/python scripts/audit_canonical_examples.py --ncbi-api` so local
validation resolves `NCBITaxon:` identifiers like the `canonical-example-taxonomy`
PR workflow. Run `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
when adding or editing CHEBI formula-bearing chemicals, and run
`.venv/bin/python scripts/audit_uniprot_grounding.py` after adding or editing
`protein_examples`. Run `.venv/bin/python scripts/build_embedding_index.py`
before `scripts/render_trait_pages.py` only
when the sibling DeepWalk artifacts named by
`scripts/build_embedding_index.py` are present; otherwise report that embedding
artifacts were not regenerated.

When `scripts/ground_causal_predicates.py` or `scripts/ground_causal_nodes.py`
proposes exact CURIEs you accept, rerun that script with `--apply` before
repeating downstream audits.

If any `discussions:` block changes, regenerate the browser data with the
shared claw module:

```bash
PYTHONPATH=<culturebotai-claw>/src .venv/bin/python -m kg_microbe_discussions \
  --config conf/discussions_config.yaml --output app/discussions
```

Regenerated priority artifacts can legitimately change existing parent rows
when the new record changes child counts, series families, or overlap scores.
Inspect those deltas before changing tests; do not preserve a stale assertion
that `--unresearched-only` is equivalent to only `BUILD_CAUSAL_GRAPH`, because
`CURATE_ROOT_WITH_SUBTYPES` is also a valid unresearched mechanism action.

## Review and merge

After local validation passes, finish the record through the same reviewed PR
loop used for other hand-curated trait changes:

1. Commit only the new record, its history, supporting writer script if any,
   generated artifacts, and directly related documentation or tests.
   After committing, run the committed-diff curation-history gate against the
   PR base:

   ```bash
   git fetch origin main
   .venv/bin/python scripts/audit_history_records.py --base origin/main
   ```

   This audit reads `base...HEAD`, not the working tree, so run it after the
   history record is committed.
2. Push a trait-scoped branch and open a pull request with the new identifier,
   label, sources, generated artifacts, and validation commands in the body.
3. Request Copilot review, dispatch both manual adversarial workflows, and
   perform a local adversarial review of the PR diff:
   `.github/workflows/claude-code-review.yml` and
   `.github/workflows/pr-shepherd.yml`, using the PR number as input.
   The local review must try to falsify the trait identity, duplicate search,
   parent choice, xrefs, evidence snippets, canonical examples, any METPO
   proposal, and regenerated artifacts before the PR merges.
4. Inspect every local finding, external review, PR comment, and workflow
   outcome. For each actionable curation defect, file a GitHub issue, fix the
   defect on the same branch, and rerun the relevant local validation before
   pushing.
   Quota and rate-limit failures are not reviews: fetch the failed workflow logs
   or PR review/comment that reported quota exhaustion, confirm no agent read
   the diff, log the affected PR plus each failed workflow run or failed review
   request on the standing quota issue, and file GitHub issues only for actual
   curation defects.
5. Watch PR checks until every required check is green. Treat a failing gate as
   a blocker, not as advisory output.
6. Merge the PR only after CI and reviews are clean. Use the native merge-queue
   path in `docs/MERGE_QUEUE.md`: enqueue without `--delete-branch`, wait until
   `gh pr view <n> --json state,mergedAt,mergeCommit` reports `MERGED`, then
   delete the remote feature branch, fetch with pruning, and verify no local or
   remote branch for that trait remains.

## Report

End with:

- new identifier, label, category, and file path
- strongest identity source and strongest mechanism source
- every DOI, PMID, URL, CURIE, source accession, and taxon id added
- curation-history event and repository history record
- generated pages or derived reports that changed
- validation commands that passed
- PR review outcome, issue numbers filed for review findings, merge result, and
  branch cleanup
- any `CURATION_TODO`, METPO proposal, or upstream METPO issue left open
- whether duplicate and absence searches included ignored and hidden files
