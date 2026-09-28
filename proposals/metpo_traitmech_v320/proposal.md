# METPO ROBOT Template Proposal - Epiphytic (v320, 2026-09)

## Scope

The pinned METPO snapshot has no active exact class for the epiphytic
plant-surface residence trait. Lindow and Brandl define the aerial plant habitat
colonized by microbes as the phyllosphere and its inhabitants as epiphytes,
while Fones et al. define epiphytic microbes as microbes living for some or all
of their life cycle on plant leaf surfaces.

| Proposal scope | Count | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for epiphytic |
| B - causal predicate lift | 0 | no new ungrounded causal predicates |
| C - schema enum lift | 0 | no schema enum is in scope |

## Identifier Block

`METPO:1039700` is reserved for this one-row class cohort. The v319 cohort used
`METPO:1039600`; no previously merged proposal or vendored METPO class uses the
1039700 block.

## Duplicate Review

The pre-mint duplicate search covered ignored and hidden files in the live
curation corpus. It found contextual endophyte/epiphyte follow-up and boundary
mentions in research and proposal artifacts, but no exact epiphyte, epiphytic,
or epiphytism TraitMech, METPO, history, or prior proposal record, no
`10.1128/AEM.69.4.1875-1883.2003` or `10.1186/s12915-024-01967-1` citation,
no `traitmech:000443`, no `METPO:1039700`, and no `metpo_traitmech_v320`
proposal record.

## Proposed Classes

| METPO placeholder | Label | Parent |
|---|---|---|
| `METPO:1039700` | epiphytic | `METPO:1007648` host-associated |

Epiphytic captures microbial residence on living aerial plant surfaces. It
excludes the broader host-associated trait, internal endophytic residence,
root-surface rhizosphere association, plant pathogenicity with apparent disease,
saprotrophic residence on dead organic matter, and phyllosphere use that also
includes above-ground internal plant compartments.

## Hierarchy and Synonyms

`traitmech:000443` is a direct local child of `traitmech:000049`
host-associated, whose upstream placeholder is `METPO:1007648`. The epiphytic
trait is narrower than general host association because it requires residence
on living aerial plant surfaces and is distinct from endophytic residence
inside living plant tissues, rhizosphere association at the root surface, plant
pathogen residence with apparent disease, and saprotrophic growth on dead
organic matter.

`epiphyte` is exact because Fones et al. define epiphytic microbes by
leaf-surface residence. `phyllosphere association` is related rather than exact
because recent phyllosphere usage can include the phyllo-endosphere as well as
the surface phylloplane.

## Verification

- The new TraitRecord validates against the closed TraitMech LinkML schema.
- The METPO proposal verifies with `scripts/verify_metpo_proposal.py
  proposals/metpo_traitmech_v320`.
- The ROBOT template validates with `scripts/robot_validate_proposal.py
  proposals/metpo_traitmech_v320`.
- `scripts/audit_proposals.py` sees the new record as proposed, cited, and
  backed by stable DOI references.

## Upstream Round-Trip

1. Submit this ROBOT template to METPO maintainers.
2. On mint, replace local `traitmech:000443` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000443` as traceability during the migration.

## Changelog

- v320, 2026-09: lifts `traitmech:000443 epiphytic` into the
  `METPO:1039700` placeholder block.
