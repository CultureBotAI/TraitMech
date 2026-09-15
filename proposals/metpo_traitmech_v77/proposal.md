# METPO ROBOT Template Proposal - Tetrathionate Respiration (v77, 2026-09)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
> alongside the v1-v76 cohorts, requesting a real METPO ID for this Scope-A
> `traitmech:` fallback.

## Context

The pinned METPO snapshot has no active exact class for the anaerobic
respiration in which microorganisms use tetrathionate as the terminal electron
acceptor and reduce it to thiosulfate for energy conservation. This cohort
lifts the local fallback record for tetrathionate respiration. The local
TraitMech record is parented to `METPO:1000802` anaerobic respiration; the
proposal keeps that parent because this is a same-axis specialization by
non-oxygen electron acceptor.

This cohort lifts one local class:

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A - synthetic trait class lift | 1 | `traitmech:000200` was minted locally because METPO has no exact tetrathionate respiration class |
| B - causal-graph predicate lift | 0 | no predicates are proposed |
| C - schema enum lift | 0 | no schema vocabulary is proposed |

## ID Block

`METPO:1015400` is reserved for this one-row class cohort. The v76 cohort used
`METPO:1015300`, so v77 starts at the next hundred block to keep cohorts
visually separated and leave room for upstream minting.

Collision search included ignored and hidden files across the whole repository.
No prior proposal reserved `metpo_traitmech_v77`, no live record used
`traitmech:000200`, and no prior proposal reserved `METPO:1015400`. The pinned
METPO snapshot has no exact tetrathionate respiration class.

Subset tag: `metpo_traitmech_2026_09`.

## Proposed Class

| ID | label | parent |
|---|---|---|
| `METPO:1015400` | tetrathionate respiration | `METPO:1000802` Anaerobic respiration |

Tetrathionate respiration is the tetrathionate terminal-electron-acceptor
branch of anaerobic respiration. It captures organism-level respiratory use of
tetrathionate and excludes narrower terms for TtrA/TtrB/TtrC, tetrathionate
reductase activity, or genes in the `ttrRSBCA` locus.

## External Mappings

No exact external mapping is proposed. Candidate EC, Rhea, and protein-family
terms for tetrathionate reductase describe enzyme activities, reactions, or
protein families rather than the organism-level anaerobic respiration
phenotype.

## Artifacts

- `metpo_proposal_classes_robot.tsv` - 12-column ROBOT class template with no
  exact synonyms, one related enzyme-name label, and no exact external xrefs.

## Upstream Path

1. Append `metpo_proposal_classes_robot.tsv` to berkeleybop/metpo#535.
2. On mint, replace local `traitmech:000200` with the assigned `METPO:` CURIE.
3. Preserve `traitmech:000200` as traceability during the migration.

## Change Log

- v77, 2026-09: lifts `traitmech:000200 tetrathionate respiration` into the
  `METPO:1015400` block.
