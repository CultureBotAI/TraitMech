# Schema gap audit — `src/traitmech/schema/traitmech.yaml`

Source of findings: `scripts/audit_schema.py` probes plus narrative interpretation. Schema header at the time of audit: 7 classes, 6 enums, 432 lines.

## Headline

The schema is in good shape. None of the probes surfaced anything that breaks instance validation today (the 357-file strict pass came back clean — see `instance_validation_summary.md`). The findings below are about *consistency* and *future-proofing*, not active bugs.

## Findings

### S1 — Classes lacking an `identifier: true` slot — *expected*

| class | line | attrs | reading |
|---|---|---|---|
| `TraitSynonym` | 219 | 3 | sub-object inlined under `TraitRecord.synonyms` — no need for a global ID |
| `EvidenceItem` | 231 | 3 | sub-object inlined under `evidence:` on `TraitRecord` and `CausalEdge` — pure value |
| `CausalEdge` | 302 | 6 | sub-object inlined under `CausalGraph.edges` — addressed by `(subject, predicate, object)` |
| `CurationEvent` | 331 | 5 | inlined log entry — addressed by `(timestamp, curator)` |

**Action:** none. All four are by-design sub-objects, never referenced by ID from outside their owning record. The probe surfaces them because it can't distinguish "owns no ID" from "shouldn't own an ID"; treat the list as a sanity check that no *root* class is missing an identifier — `TraitRecord` and `CausalGraph` both have one (`id`, `graph_id`). **No change.**

### S2 — Slots with `range: string` that look enum-shaped — *clean*

Probe returned 0 hits. The schema is already disciplined about using enums (`TraitCategoryEnum`, `TermKindEnum`, `PriorityEnum`, `MappingStatusEnum`, `CausalNodeTypeEnum`, `SynonymTypeEnum`) for every controlled-vocabulary slot it has. **No change.**

### S3 — Term/ontology slot naming divergence — *intentional*

Probe surfaced four slots with `_id`/`term`-like suffixes:

- `graph_id` (CausalGraph) — *local* identifier within the trait record
- `node_id` (CausalNode) — *local* identifier within the graph
- `predicate_id` (CausalEdge) — *ontology CURIE* grounding the predicate
- `term_kind` (TraitRecord) — enum slot (`Class` vs `DatatypeProperty`), not an identifier — **probe false positive** (matched the `term` fragment).

**Action:** none. `graph_id` / `node_id` denote local graph-scope IDs; `predicate_id` denotes an external grounding — these *should* differ. **No change.**

### S4 — `required:` inconsistency: `evidence` — *defensible, document it*

The probe flagged one divergence:

- `TraitRecord.evidence` (line 188) — *optional*
- `CausalEdge.evidence` (line 324) — **required**

This is intentional: a `TraitRecord`'s evidence is a curator-added bonus on top of METPO provenance, while every causal edge must carry literature support to be assertable. The asymmetry encodes a real editorial policy.

**Action:** lift the rationale into the schema descriptions for both `evidence:` slots, so a future reader doesn't "harmonize" them by adding `required: true` to `TraitRecord.evidence`. One-line description tweak; effort S.

### S5 — Orphan enums — *clean*

Every declared enum is referenced as a `range:` somewhere. **No change.**

### S6 — Undefined range references — *clean*

Every `range:` resolves to a class, enum, or built-in type defined in this schema. **No change.**

### S7 — Enum value casing audit — *clean*

No enum mixes UPPER/lower/MixedCase values. **No change.**

## Schema-level recommendations (none urgent)

1. **S4** — add a short rationale to both `evidence:` descriptions explaining why one is required and one isn't. Cost ~2 lines.
2. **General hygiene** — when adding any new descriptor class with a stable cross-reference, give it an `identifier: true` slot. The current four IDless classes are all sub-objects; the *policy* worth writing down is "sub-objects can be IDless, root descriptor classes must not."

Neither requires regenerating `traitmech_dataclasses.py` since descriptions only affect documentation.

## Reproduce

```bash
uv run python scripts/audit_schema.py        # all probes, stdout
just audit-schema                            # same, via just
```
