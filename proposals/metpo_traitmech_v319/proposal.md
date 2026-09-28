# METPO ROBOT Template Proposal - Endophytic (v319, 2026-09)

## Scope

The pinned METPO snapshot has no active exact class for the endophytic
plant-host residence trait. Hardoim et al. frame endophytism as internal plant
residence by diverse bacterial, archaeal, fungal, and protistic communities,
while Kandel et al. define bacterial endophytes as microbes living inside the
plant for most of their life cycle without a detrimental effect on the host.

| Proposal scope | Count | Rationale |
|---|---:|---|
| A - synthetic trait class lift | 1 | local fallback for endophytic |
| B - causal predicate lift | 0 | no new ungrounded causal predicates |
| C - schema enum lift | 0 | no schema enum is in scope |

## Identifier Block

`METPO:1039600` is reserved for this one-row class cohort. The v318 cohort used
`METPO:1039500`; no previously merged proposal or vendored METPO class uses the
1039600 block.

## Duplicate Review

The pre-mint duplicate search covered ignored and hidden files in the live
curation corpus. It found no exact endophyte, endophytic, or endophytism
TraitMech, METPO, history, or prior proposal record, no `10.1128/MMBR.00050-14`
or `10.3390/microorganisms5040077` citation, no `traitmech:000442`, no
`METPO:1039600`, and no `metpo_traitmech_v319` proposal record.

## Proposed Classes

| METPO placeholder | Label | Parent |
|---|---|---|
| `METPO:1039600` | endophytic | `METPO:1007648` host-associated |

Endophytic captures internal residence in living plant tissues without apparent
host disease. It excludes the broader host-associated trait, rhizosphere
association, epiphytic plant-surface residence, plant pathogenicity,
saprotrophy, and nitrogen-fixing symbiosis or growth-promotion phenotypes that
may be observed in only some endophytic isolates.

## Hierarchy and Synonyms

`traitmech:000442` is a direct local child of `traitmech:000049`
host-associated, whose upstream placeholder is `METPO:1007648`. The endophytic
trait is narrower than general host association because it requires residence
inside living plant tissues and is distinct from rhizosphere association at the
root surface, epiphytic residence on plant surfaces, plant pathogen residence
with apparent disease, saprotrophic growth on dead organic matter, and the
specialized subset of endophytic nitrogen-fixing symbioses.

`endophyte` is exact because Kandel et al. define an endophyte by internal
plant residence without detrimental host impact. `endophytism` is related
because Hardoim et al. use the noun for the endophytic lifestyle rather than an
ordinary adjective label.

## Verification

- The new TraitRecord validates against the closed TraitMech LinkML schema.
- The METPO proposal verifies with `scripts/verify_metpo_proposal.py
  proposals/metpo_traitmech_v319`.
- The ROBOT template validates with `scripts/robot_validate_proposal.py
  proposals/metpo_traitmech_v319`.
- `scripts/audit_proposals.py` sees the new record as proposed, cited, and
  backed by stable DOI references.

## Upstream Round-Trip

1. Submit this ROBOT template to METPO maintainers.
2. On mint, replace local `traitmech:000442` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000442` as traceability during the migration.

## Changelog

- v319, 2026-09: lifts `traitmech:000442 endophytic` into the
  `METPO:1039600` placeholder block.
