---
name: curate-yaml-record
description: Review and curate one TraitMech trait YAML record for concept identity, definition, hierarchy, scope, evidence, causal mechanisms, completeness, and resolvable gaps. Use when asked to audit, improve, complete, correct, or add evidence to a named trait; do not use for bulk METPO ingestion, paid research without approval, excluded records, or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one TraitMech YAML record

Produce a scientifically defensible `TraitRecord` and an explicit account of
what is supported, corrected, unresolved, and genuinely unknown. Search results
and deep-research reports are leads; inspect the cited source before using it.

## Boundaries

- Resolve one target under `data/traits/`. Stop and disambiguate if a label
  matches several trait concepts or positive/negative variants.
- Check `DO_NOT_WORK.md` before doing anything. Do not edit a listed record
  unless the user first removes its exclusion.
- Review/audit requests are read-only. Curate, improve, complete, correct, or
  add-evidence requests authorize local edits to the named record and its
  required append-only history/generated artifacts.
- Do not launch a paid provider, expand a batch, contact anyone, or mutate a
  GitHub issue/PR/comment without explicit authorization.
- Preserve unrelated work and use a branch/worktree for multi-file changes.
- Never fill an optional slot merely to improve coverage or infer false from
  absence.

## Read before judging the record

Read the complete target plus:

- `CLAUDE.md`, `docs/CURATION_PLAYBOOK.md`, and
  `docs/GROUNDING_POLICY.md`;
- the relevant `TraitRecord`, evidence, example, relation, causal-graph,
  discussion, and history classes in `src/traitmech/schema/traitmech.yaml`;
- `history/README.md`;
- [references/review-checklist.md](references/review-checklist.md).

Inspect parent/child and positive/negative partner records, existing research,
and source-native ontology/database entries. Existing YAML and rendered pages
are not independent evidence.

## Workflow

### 1. Establish the baseline

Read the full YAML. Record identifier, label, definition/source, synonyms,
parents, xrefs, category, kind/domain/range, examples, mapping status, evidence,
causal graphs, discussions, datasets, and curation history. Run:

```bash
just validate <record-path>
just validate-strict <record-path>
```

Run relevant graph, ontology-product, and snippet checks while iterating. A
green LinkML result proves shape, not that a biological claim is true.

### 2. Verify trait identity and hierarchy first

Confirm the record denotes a microbial trait rather than a taxon, protein,
cellular structure, assay, or one experimental observation. Check identifier,
label, synonym scope, term kind, category, domain/range, parents, replacements,
and xrefs. A related or correlated trait is not necessarily a parent or exact
mapping. Never guess a CURIE or canonical label.

### 3. Review every scientific claim

Verify that definition sources, top-level evidence, canonical examples,
relations, causal nodes/edges, datasets, and discussions support the exact
trait, taxon/context, direction, and wording. Prefer primary evidence for
mechanistic and exemplar claims; cite a database assertion as such.

Every causal edge needs DOI/PMID-backed evidence. Do not upgrade correlation,
prediction, co-occurrence, class membership, or a protein instance into causal
mechanism or universal taxonomic scope. Snippets are short exact source text;
interpretation belongs in notes.

### 4. Assess completeness and resolve supported gaps

Apply the checklist and use bounded searches for consequential gaps. Prioritize:

1. wrong trait identity, polarity, category, or hierarchy;
2. unsupported/overbroad definitions and mappings;
3. unsupported canonical examples or taxonomic scope;
4. missing or overclaimed causal-edge evidence;
5. concrete discussions whose source or identifier checks can be resolved.

Do not manufacture a mechanism for a classification or measurement trait.
Record an explicit nonmechanistic scope decision when the schema and evidence
support it. Add a discussion only for a specific unresolved conflict or task.

### 5. Write through the guarded path

Use a narrowly scoped mutator that asserts the target ID/path, calls
`traitmech.curate.curation_event.record_curation_event` with
`llm_assisted=True`, and writes with
`traitmech.validation.write_validated.write_validated_trait`. Use
`curator="claude"` when no curator identity was supplied and never attribute an
agent's judgement to the user.

Create a repository-level append-only history record with `just new-history`.
Do not append either history event when content is unchanged.

`mapping_status: REVIEWED` represents human curator sign-off on label,
definition, and parents. An agent draft remains `PROPOSED` unless a human
curator explicitly signs off; never demote an already reviewed record merely
because the current task found an additional gap.

### 6. Verify and report

```bash
just validate-strict <record-path>
just validate-history
just validate-products
just audit-writers
just qc
git diff --check
git diff -- <record-path> history src scripts reports pages
```

Run `just verify-snippets` when source access is available and evidence changed.
Re-read the result; verify every edge and citation, the status decision, and
both history records against the actual diff.

Report corrections/additions and sources, retained claims checked, unresolved
gaps and bounded searches, whether human REVIEWED sign-off exists, history
artifact, and all validation results.
