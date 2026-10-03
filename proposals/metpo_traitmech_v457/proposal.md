# METPO Proposal v457: Thermotaxis

## Context

This cohort lifts `traitmech:000580 thermotaxis`, a motile phenotype defined
by temperature-guided active movement. It is not a growth-temperature class,
passive thermophoresis, or a chemical-gradient response. Primary sources are
Paulick et al. (DOI:10.7554/eLife.26607) and Paster and Ryu
(DOI:10.1073/pnas.0709903105); the Tar response is additionally supported by
DOI:10.1074/jbc.271.30.17932 and DOI:10.1128/jb.179.21.6573-6580.1997.

Fresh temporary seeding emitted 399 METPO identifiers: 344 present and 55
absent from the 974-record pre-change corpus. Both frozen release-review
tables were inspected. Whole-repository searches included ignored and hidden
files, OWL, history, research, proposals and generated pages. Thermotaxis was
mentioned in the chemotaxis research report as a distinct trait, not represented
by an exact record. No exact METPO class or prior thermotaxis proposal was found.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | Existing graph relations suffice | 0 |
| C: schema enums | 0 | Not biological trait proposals | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053400 | traitmech:000580 | thermotaxis | METPO:1000702 |

The reviewed `motile` parent denotes independent energy-dependent movement.
Thermotaxis adds temperature-guided bias, so this is more specific than the
generic phenotype parent. The PHYSIOLOGY category follows the behavioral
scope of chemotaxis, not the filesystem category of the motility apparatus.
Chemotaxis is not the parent: a shared signaling pathway does not make the
temperature stimulus a chemical gradient. No existing parent or sibling is edited.

## Evidence And Mapping Boundaries

- The eLife API identifies version 2 as the Version of Record dated August 31,
  2017. The [version-specific PDF](https://cdn.elifesciences.org/articles/26607/elife-26607-v2.pdf)
  and primary PMC5578741 XML were inspected, including figure supplements.
- AW405 with a GFP marker supplies the K-12 behavioral example. The VS223
  FRET reporter and MG1655 growth experiment are distinct assays, not interchangeable
  examples. Response inversion depends on assay and chemical-adaptation context;
  there is no universal preferred-temperature threshold in this definition.
- The graph describes the Tar-mediated arm, not the complete Tar/Tsr network.
  It preserves deamidation, methylation and response-sign distinctions, with
  intermediate phosphorelay steps compressed rather than bypassed.
- UniProt P07017 resolves to reviewed K-12 Tar, entry version 208, sequence
  version 2, checked October 3, 2026. It is an instance example, not a trait xref.
  InterPro IPR003122 is a ligand-binding domain rather than a full Tar receptor.
- QuickGO resolves GO:0043052 to the thermotaxis biological process. It grounds
  the graph's process node, not an equivalent organismal-disposition xref.
  No exact cross-ontology equivalence or SSSOM mapping is asserted.
- An open discussion records the assay-context disagreement and the limits of
  extrapolation beyond the experimentally supported E. coli mechanism.

## ID Space And Subset

Reserve `METPO:1053400-1053499`, using only `1053400`, after v456's
`1053300` block. Ignored-and-hidden collision searches found no previous local
ID, cohort or block allocation. Numeric substrings in vendored plotting sample
data are not identifier allocations. The block does not intersect CommunityMech
v1 `1007100-1007220`. Subset: `metpo_traitmech_2026_10`.
These are proposal placeholders, not released METPO identities.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The 11-column header follows the live kg-microbe master class template;
the three trailing empty ROBOT header cells are required.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v457`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v457` and
`scripts/verify_metpo_proposal.py --coverage`. The PR records actual validation,
source matching, authority checks and rendered-page inspection results.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review. This local
proposal is not evidence of upstream acceptance or a minted METPO identifier.

## Round-Trip Plan

After acceptance, refresh the METPO snapshot, seed into a temporary tree and
migrate the record to the released identifier. Preserve `traitmech:000580` in
provenance, update the graph trait node and regenerate affected artifacts.
Never emit this placeholder as a released METPO ID before that migration.

## Change Log

- v457, 2026-10-03: add thermotaxis with context-bounded evidence, a direct
  behavioral example and a Tar-mediated causal graph.
