---
name: curate-yaml-record
description: Review and curate one TraitMech trait YAML record for concept identity, definition, hierarchy, scope, evidence, causal mechanisms, completeness, and resolvable gaps. Use when asked to audit, improve, complete, correct, or add evidence to a named trait; do not use for bulk METPO ingestion, paid research without approval, excluded records, or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Curate one TraitMech YAML record

Produce a scientifically defensible `TraitRecord` and an explicit account of
what is supported, corrected, unresolved, and genuinely unknown. Search results
and deep-research reports are leads; inspect the cited source before using it.

## The Contract

<!-- canonical:begin the-contract -->
Produce a defensible record and an explicit account of four things: what is
**supported**, what was **corrected**, what is **still unresolved**, and what is
**genuinely unknown**. The last two are different — a gap you searched for and
could not close is a finding; a gap you did not look at is not.

**One target.** Resolve exactly one record before touching anything. If a label
matches several, or a request names a family rather than a member, stop and
disambiguate. Silently substituting a similar record is the error that no later
check catches, because everything downstream is then correct about the wrong
thing.

**Audit preserves scientific inputs. Curation authorises edits to the named
record only.** A review or audit request changes no scientific record, status,
or curation history. It does save a new timestamped structured review through
`docs/record-reviews.md` and the native rubric in `docs/record-review-profile.md`.
A curate, improve, complete, correct or add-evidence request authorises local edits to that record and the smallest
maintained path its provenance requires — not to neighbours, not to whatever
else looked wrong on the way.

**Search results are leads. Only an inspected source supports a claim.** A
search hit, a deep-research report, a rendered page, and a generated artifact are
each somewhere to look, and none is evidence. Evidence is text you read in the
source, attached to the narrowest assertion it actually supports.
<!-- canonical:end the-contract -->

## Boundaries

<!-- canonical:begin boundaries -->
- **A generated artifact is never the fix.** Pages, merged products, exports and
  derived indexes are outputs. Correct the input or rule that owns the value and
  regenerate; patching the output makes it look right once and diverge on the
  next build.
- **No outbound action without explicit authorisation for that action.** Do not
  launch paid research, contact an author, or create or edit a GitHub issue, PR
  or comment because curation seemed to call for it. Authorisation to curate a
  record is not authorisation to spend or to speak.
- **Absence is not evidence of falsity, and coverage is not a goal.** Never
  infer that an unstated optional property is false. Never fill an optional
  slot to make the record look more complete. An empty field the source does
  not address is correct.
- **Search before declaring anything absent — and search past `.gitignore`.**
  Before treating a record, evidence source, decision row or overlay as missing,
  search for its identifier, label and slug with an ignore-independent tool
  (`rg --no-ignore --hidden`, `grep -r`, or `find`). Ordinary search skips
  ignored files, so an ordinary miss is a search over a subset, not a result.
- **Preserve unrelated work.** Use a branch, and a separate worktree when the
  checkout is dirty or occupied by something else.
<!-- canonical:end boundaries -->

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

## Evidence Standard

<!-- canonical:begin evidence-standard -->
- Each claim is its own object. A definition, an example, a relation and a
  mechanism edge are separate assertions; attach a source to the narrowest one
  it supports, never to the record as a whole.
- Resolve every DOI, PMID and CURIE, and read enough of the source to establish
  support for the *exact* claim and scope. A matching string from the wrong
  paper, or an unrelated sentence from the right one, is not support.
- A snippet is short verbatim text from the source. Interpretation belongs in a
  notes field, never inside the quotation.
- **The kind of source is part of the citation.** A database assertion, a
  primary experiment, a review, a prediction and a search snippet are different
  strengths of support. Cite each as what it is; never present a database row
  or a review as if it were the primary study.
- Association and prediction do not establish mechanism or causality. Do not
  let a co-occurrence or a computed score become a mechanism edge.
- **A near-miss is not a match.** Never ground to a CURIE or canonical label
  because it looks plausible, and never use a broader or related term as an
  exact identity. Unresolved stays unresolved, recorded as such, until a source
  resolves it.
- **Evidence about one thing supports a claim about that thing.** Do not
  generalise one organism, strain, protein instance, construct or experiment
  into a family-wide, universal or "optimal" claim. Scope inflation is the most
  common way a true observation becomes a false record.
- Keep conflicts. When sources disagree, record both and the disagreement; do
  not resolve it by omission.
- A bounded search that found nothing is a result. Report it as "not found,
  searched X" rather than leaving the field silently empty.
<!-- canonical:end evidence-standard -->

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

## Writing Back

<!-- canonical:begin writing-back -->
**Write only through the path that preserves formatting and records history.**
Never hand-edit a curated YAML with a text editor or a generic dump: canonical
key order, quoting and derived metadata are what make the corpus diffable, and a
dump destroys them in one save.

Repositories in this fleet do this in three different, equally correct ways, and
which one applies is a property of the corpus:

- **Direct guarded write** — a narrowly scoped mutator loads the record, asserts
  its identity, changes only the reviewed nodes, appends a curation event, and
  writes through the repository's validated writer.
- **Registered editor** — no generic writer exists on purpose; in-place changes
  use text-preserving operations through an editor that is registered and
  behaviourally tested, and the writer audit rejects anything else.
- **Regenerate from inputs** — the record is a build product. The fix goes into
  the decision row, term request, overlay or source inventory that owns the
  value, and the record is regenerated; the YAML is never edited directly.

The section below says which one this repository uses and names the exact
functions or files. Do not guess from a sibling.

Inspect the diff before committing. Whole-file presentation churn — reordered
keys, requoted strings, a hundred lines changed to alter one value — means the
write path was bypassed; abandon and repair rather than commit it.
<!-- canonical:end writing-back -->

## History And Attribution

<!-- canonical:begin history-and-attribution -->
- Use `curator="claude"` when no curator identity was supplied. **Never
  attribute an agent's judgement to the user.** The history entry is a record
  of who decided, and it will be read when the decision is questioned.
- Mark LLM assistance where the schema records it.
- **Do not append a history event when nothing substantive changed.** A
  no-op event is noise that makes real events harder to find.
- The history entry describes the actual diff. If the corpus derives status or
  history from inputs, never set them directly — change the input.
- A REVIEWED status means a human reviewed it. Do not invent one, and do not
  promote to it on the strength of an agent pass.
<!-- canonical:end history-and-attribution -->

## Workflow

For an audit-only request, use
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[the native profile](../../../docs/record-review-profile.md). Capture exact
targets and inspected input hashes before judging with
`scripts/record_review.py inspect`. Apply steps 1-4 as assessments/proposed
actions, skip step 5, and run only applicable read-only checks from step 6.
Validate and save a `kind: record` observation using
`uv run python scripts/record_review.py validate <review.yaml>` and
`uv run python scripts/record_review.py save --content <review.yaml>`.
Link the saved YAML and derived Markdown. Record unavailable required checks
as partial/blocked; do not append either history event or promote status.
`DO_NOT_WORK.md` remains authoritative and its listed records stay untouched.

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
