# METPO Proposal v447: Short Lamassu System

## Scope

One Scope-A class lifts `traitmech:000570`, the organism-level possession
trait for the short-LmuB structural family. Scope B and C have zero rows.
`METPO:1052400` is reserved in the next unused hundred block, after v446's
`METPO:1052300`. The subset is `metpo_traitmech_2026_10`; the parent is
`METPO:1018600`, reserved for Lamassu system in v109.

## Evidence and Boundaries

[Haudiquet et al.](https://doi.org/10.1073/pnas.2519643122) distinguish
short and long families by LmuB phylogeny and coiled-coil architecture.
The short family's approximate 600-residue average is not a threshold.
Their Vc-Cap4 example has a 653-residue LmuB, independently confirmed in
[PDB 9NY5 entity 3](https://data.rcsb.org/rest/v1/core/polymer_entity/9NY5/3).
The deposition separates the V. cholerae source organism from the E. coli
expression host. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=666&mode=Info)
resolves taxon 666 to V. cholerae. Neither the source identity nor the
heterologous assay establishes species-wide native phage resistance.

This class is neither a single protein nor an effector-specific profile
call. It is also not equivalent to type I: short-family architectures
include both LmuC-containing and LmuC-loss forms. No universal LmuC,
effector chemistry, zinc-hook count, or complex stoichiometry is imposed.
The existing Lamassu parent already describes the particular Vc-Cap4
mechanism; duplicating that graph here would not establish a family-wide
mechanism. No exact external mapping or SSSOM artifact is proposed.

## Existing Child

The local HNH record (`traitmech:000568`, v445 `METPO:1052200`) already
requires short-form LmuB in its definition, so its direct parent is refined
to the new family. Its definition, evidence and exemplar are unchanged.
The v445 template's broader Lamassu parent remains a true superclass and
is retained as a historical proposal; neither its ID nor its row is
rewritten. On upstream minting, add the more specific subclass relation:

`METPO:1052200 SubClassOf METPO:1052400`

This uses the established missing-parent proposal pattern (for example,
v286). Do not move SMEK, whose long-profile exception is unresolved, or
other table-defined effector records without their own scope review.

## Novelty Review

Searches covered ignored and hidden files throughout the repository,
including METPO, proposals, research, history and generated artifacts.
Existing mentions of short Lamassu were narrower HNH evidence or prose,
not an exact family record. The fresh METPO seed comparison had 55
identifier-only leads: 17 previously classified duplicates and 38
supporting-field properties, not uncurated primary traits. No exact METPO
term or local/proposed identifier collision was found.

Lamassu-Hypothetical is deferred: an uncharacterized registry annotation
does not establish the effector-domain-loss biology described for clade O.
The long family and component-number subtypes remain discovery leads,
not evidence that the broader trait frontier is exhausted.

## Validation and Upstream Path

The guarded writer generates the record, the HNH refinement, the parent
discussion append and the 11-column two-header ROBOT template. Tests cover
dry runs, idempotence, scope preservation and refusal of input/output drift.
Validate the record, proposal, history, taxonomy, snippets and generated
products, run ROBOT/ELK and the full QC/test suite before merge.

Submit with [the existing METPO tracker](https://github.com/berkeleybop/metpo/issues/535).
After human ontology review and minting, replace the local fallback with
the assigned ID, retain its provenance, and translate the HNH parent
relation above using the assigned IDs. Bot review does not change
`mapping_status: PROPOSED`.

## Change Log

- v447, 2026-10-03: propose the short-LmuB family and document the HNH
  subclass refinement without changing historical proposal identifiers.
