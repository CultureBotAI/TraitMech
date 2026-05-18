# Proposal: predicate + class composition for chemical-use relations

> **History note.** An earlier revision of this document proposed
> *precomposing* substrate-specific TraitRecords like
> `traitmech:UCS_GLUCOSE` ("uses glucose as carbon source") to replace
> the DEPRECATED METPO relation carriers (`METPO:2000006` etc.).
> That direction was wrong: it is not the METPO modelling pattern.
> The correct pattern is **predicate + class composition** —
> reusing the METPO OBJECT_PROPERTY as the predicate and pointing it
> at a CHEBI (or other) class at the assertion site. This document
> now describes that approach.
>
> See `git log -- docs/DEPRECATED_REPLACEMENT_PROPOSAL.md` for the
> precomposition draft (now superseded). PR #52 (which added 7
> precomposed records) was reverted.

## The pattern

METPO carries a set of OBJECT_PROPERTY records for chemical-use
relations:

| METPO ID | Relation | Companion class |
|---|---|---|
| METPO:2000006 | uses as carbon source | a `CHEBI:` class (organic / carbon-bearing chemical) |
| METPO:2000008 | uses as electron acceptor | a `CHEBI:` class (oxidised species) |
| METPO:2000009 | uses as electron donor | a `CHEBI:` class (reduced species) |
| METPO:2000007 | uses as energy source | a `CHEBI:` class or environmental factor |
| METPO:2000010 | uses as nitrogen source | a `CHEBI:` class (N-bearing chemical) |
| METPO:2000020 | uses as sulfur source | a `CHEBI:` class (S-bearing chemical) |
| METPO:2000003 | builds acid from | a `CHEBI:` class (substrate) |
| (and many more — see `data/traits/metabolism/`) |

The intended assertion at use-site (in downstream KG, in causal
graph edges, etc.) is:

```
<organism>  METPO:2000006  CHEBI:17234     # X uses glucose as carbon source
<organism>  METPO:2000009  CHEBI:18276     # X uses H2 as electron donor
<organism>  METPO:2000008  CHEBI:17632     # X uses nitrate as electron acceptor
```

TraitMech provides the predicate vocabulary (the METPO relations as
`OBJECT_PROPERTY` records with definitions, evidence, and proper
domain/range) and curated trait/phenotype classes. Downstream
consumers — KG-Microbe, observation databases, organism profiles —
compose the predicate with the CHEBI substrate at the level where
each organism's observation is recorded. **No precomposed
substrate-specific TraitRecords are needed in this corpus.**

## Implications for the DEPRECATED records

The 94 metabolism `OBJECT_PROPERTY` records previously marked
`DEPRECATED` were the **wrong** thing to deprecate. They are
precisely the composition primitives that the predicate+class model
needs. They should be:

- Restored to `mapping_status: REVIEWED`.
- Given a clean definition, definition_source, and at least one
  literature-evidence entry that supports the relation as a
  microbial-physiology descriptor.
- Have their `domain:` and `range_:` slots set explicitly so RDF
  consumers know the predicate connects an organism class to a
  chemical class.

A `UNDEPRECATED_AS_COMPOSITION_PRIMITIVE` curation_history event
records the restoration on each record.

3 of these (METPO:2000006 / 2000008 / 2000009 — the three directly
touched in the original precomposition push) are un-deprecated in
the same PR as this doc revision. The remaining 91 are deferred to
a follow-up survey PR.

## Implications for downstream graphs

Causal graphs inside TraitRecords already use the predicate+class
pattern when needed: edges carry a `predicate:` string and point at
nodes that are typically grounded chemicals or processes. For
example, the existing `aerobic.yaml` causal graph has:

```yaml
edges:
- subject: aerobic_trait
  predicate: requires
  object: molecular_oxygen          # CHEMICAL node grounded to CHEBI:15379
```

Asserting "uses glucose as carbon source" at the edge level in
*another* trait's graph would look like:

```yaml
- subject: <some trait>
  predicate: uses as carbon source  # METPO:2000006
  object: glucose                   # CHEMICAL node grounded to CHEBI:17234
```

This is already supported by the current schema — no schema change
is needed beyond what's already there.

## Implications for the `replaces:` schema field

The `replaces:` slot added in PR #51 (slot_uri `dcterms:replaces`)
remains in the schema. Its primary motivating use case
(precomposition records replacing DEPRECATED predicates) no longer
applies, but the slot is still useful for genuine record
replacements (e.g. when a TraitMech curator splits one record into
two, or when METPO renumbers a class). The slot stays — it just
won't be widely used until those occasions arise.

## Implications for the upstream METPO issue

`CultureBotAI/assay-metadata#2` was opened to request METPO IDs for
the 7 precomposed records. That request is now moot. The issue is
updated to explain the pivot to predicate+class composition.

## What this PR does

1. **Reverts PR #52** — deletes the 7 precomposed substrate-specific
   records (`uses_glucose_as_carbon_source.yaml`, etc.) that were
   the wrong direction.
2. **Un-deprecates 3 METPO relation predicates** (METPO:2000006,
   METPO:2000008, METPO:2000009) — switches `mapping_status` from
   `DEPRECATED` back to `REVIEWED`, adds DOI-backed definition and
   evidence, sets `domain:` and `range_:` to make the predicate's
   intended composition explicit.
3. **Rewrites this proposal doc** to describe the predicate+class
   composition pattern.
4. **Updates the curation playbook** with a section on the pattern.
5. **Updates the upstream METPO issue** to explain the pivot.

## Out of scope for this PR

- **The 91 remaining DEPRECATED metabolism predicates** (`assimilates`,
  `degrades`, `disproportionates`, `exports`, `ferments`, `hydrolyzes`,
  `imports`, `oxidizes`, `produces`, `reduces`, `sequesters`,
  `shows_activity_of`, `transports`, etc., plus their `does_not_*`
  negation variants, plus the various `has_*_observation` records).
  These are tracked in task #33 — a survey PR will pick the canonical
  predicates and un-deprecate them in batch, leaving any genuinely
  non-canonical ones (e.g. metpo-internal observation carriers) as
  DEPRECATED.

- **The 20 observation and 7 quantitative_property DEPRECATED
  records**. These are structurally different (observation/value
  carriers, not predicates), and the predicate+class pivot does
  not directly affect them. They remain DEPRECATED pending a
  separate observation-modelling decision. **Update 2026-05-17:
  the observation-modelling decision is now resolved — see
  "Observation-value records stay deprecated" below.**

## Observation-value records stay deprecated

After the predicate+class composition pivot landed (#54, #55, #56),
50 records remain `DEPRECATED`:

| Group | Count | Where |
|---|---|---|
| `has_*_observation` / `has_phenotype` / `has_quality` predicates | 23 | `data/traits/metabolism/` |
| Observation classes (pH observation, temperature observation, etc.) | 20 | `data/traits/observation/` |
| Value-carrying datatype properties (`has_value`, etc.) | 7 | `data/traits/quantitative_property/` |

These three groups together would compose into the
BacDive-style assertion shape:

```
<organism>  has_temperature_observation  <obs-instance>
<obs-instance>  has_value  37.0
<obs-instance>  has_unit   UO:0000027   # degree Celsius
```

**They stay deprecated and out of scope for TraitMech.** The reasoning:

1. **Observations belong in the downstream consumer, not the
   trait knowledge base.** TraitMech's job is to curate the trait
   vocabulary (METPO classes + predicates) and the *mechanism*
   behind each trait (causal graphs, evidence). Per-organism
   numeric observations — what temperature *this strain*
   actually grew at — are KG-Microbe's job, and earlier
   BacDive-derived observations there already use a different
   shape (a per-strain table, not OWL instance assertions).
   Recreating BacDive's observation schema inside TraitMech would
   duplicate that effort with a less-mature implementation.

2. **The METPO observation classes are wrappers around
   numeric values; they have no curatable mechanism.** Unlike
   `aerobic` or `halophilic` (which have rich mechanism graphs),
   `optimum_pH_observation` carries no mechanism — it's a measurement
   slot. Promoting these to REVIEWED would force us to add
   placeholder causal_graphs that wouldn't carry real information.

3. **`has_value` and the other datatype properties in
   `quantitative_property/` are part of the observation shape,
   not standalone phenotypes.** If we ever do model
   per-organism observations directly, we'd want to align with
   STATO / OBI / QUDT rather than maintaining a parallel METPO
   numeric vocabulary.

4. **The predicate+class pivot covers the trait-level need.**
   Every chemical-use or activity assertion that previously
   would have used `has_X_observation` can now be expressed as
   `<organism> <METPO predicate> <CHEBI/METPO class>` —
   evidence sits in the predicate record (or downstream
   per-strain table), not as a separate observation instance.

A `DEPRECATION_CONFIRMED_AS_OUT_OF_SCOPE` curation_history entry
has been added to all 50 records pointing at this section, so the
decision is findable from each record individually rather than
only from this doc.

**If a future use case requires per-strain observation modelling
inside TraitMech**, reopen this section: the cleanest path
would be to introduce a `traitmech:Observation` class in the
schema (separate from `TraitRecord`) rather than re-promoting the
METPO 1001xxx and 2000xxx observation/has-observation records,
which were modelled before STATO/OBI alignment was a goal.

## Why the pivot now

The precomposition approach treats each (substrate, relation) pair
as a new ontology class. This:

1. Multiplies record count combinatorially (5 substrates × 3
   relations = 15 classes; the full matrix is ~thousands).
2. Doesn't reflect how METPO is actually modelled upstream — METPO
   keeps the predicate and class spaces separate.
3. Creates a permanent fork between TraitMech and METPO whenever
   substrates outside the precomposed batch are needed.

The predicate+class approach:

1. Records O(predicates) + O(chemicals), not O(predicates × chemicals).
2. Matches METPO modelling.
3. Lets organism observations refer directly to the same MM/CHEBI
   classes used elsewhere in the OBO world.
4. Surfaces the per-organism evidence at the *observation* level
   (where it belongs) rather than the *class* level (where it
   doesn't).
