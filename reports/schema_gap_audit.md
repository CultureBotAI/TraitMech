# Schema gap audit

Source: `scripts/audit_schema.py`, run through:

```bash
just audit-schema
```

The command derives class, enum, slot, and line information from the current
schema. Its output is authoritative for the live inventory; this interpretation
records only durable decisions.

## Decisions

### Identifier-less classes

The audit lists concrete classes without an `identifier: true` attribute.
Inline value objects such as synonyms, evidence items, examples, edges, and
curation events are intentionally addressed through their owning record rather
than given global identifiers. Investigate only if a new independently
referenceable/root class appears in the live list.

### String ranges and controlled values

Slots whose names imply a status, category, kind, or other controlled value
should normally use an enum or typed range. Review any live hit; do not turn a
string into an enum mechanically when the value is genuinely open vocabulary.

### Identifier-like slot names

The current naming differences encode different scopes: graph and node IDs are
local, predicate IDs are ontology CURIEs, taxon IDs are external references,
and `term_kind` is a classifier rather than an identifier. Uniform suffixes
would erase useful distinctions.

### Requiredness

`TraitRecord.evidence` is optional because seeded records inherit METPO
provenance. `CausalEdge.evidence` is required because curator-asserted mechanism
claims must carry direct support. That rationale is recorded in both schema
descriptions. Other requiredness differences should be evaluated on their
semantics, not normalized by name alone.

### Imported ranges

Range resolution includes recursively imported local LinkML schemas. In
particular, `Discussion` and `Dataset` resolve through `mech_shared`; they are
not undefined types. Prefix imports such as `linkml:types` are handled as
built-ins. Any remaining undefined-range hit is actionable.

### Enums

Unused enums and mixed casing are review signals. Run the command after schema
changes and remove dead declarations or document intentional casing rather than
silencing the probe.

## Verification after a schema change

```bash
just audit-schema
just validate-all
just qc
```

Generated dataclasses are ignored and regenerable; they are not part of this
report or the committed schema contract.
