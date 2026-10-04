# Heterokaryon Incompatibility: METPO Proposal v483

## Context

Lift `traitmech:000606 heterokaryon incompatibility`, a PROPOSED PHYSIOLOGY
class, to a provisional upstream slot. The trait concerns postfusion nonself
recognition restricting viable vegetative heterokaryons, not a locus or an
individual interaction measurement. Three directly retrieved primary abstracts
support the phenotype and distinguish it from broader vegetative barriers.

Whole-repository novelty searches included ignored and hidden files, labels,
spelling variants, slugs, citations, xrefs, graphs, discussions, research,
proposals, generated artifacts and history. Existing negative-autotropism
mentions are boundary exclusions, not unresolved exact trait nodes. The
hyphal-anastomosis discussion already allows subsequent incompatibility;
it does not assert a missing exact parent or synonym. No older trait needs
mutation for this addition. A structured search of the pinned 12,617-triple
METPO graph found no exact class. All-state upstream issue searches for
heterokaryon and vegetative incompatibility were empty on 2026-10-04.

A fresh 399-record seed was reconciled with the 1,000-record live corpus
before addition: 344 present and 55 absent. Both frozen 2026-06-12 tables
classify the remaining 55 as 38 supporting-field rows and 17 duplicates.
Their absence is not an uncurated primary-trait queue.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

No predicate, sequence feature or workflow-enum lift is needed.

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`, in
the pinned ontology's `https://w3id.org/metpo/` namespace. Hyphal fusion may
precede incompatibility but is not a broader class of the response. This
is not motility, sexual incompatibility or generic programmed cell death.

Do not require complete colony death or failure of every nonself pairing.
Barrage formation and prefusion avoidance alone do not establish the trait.
The 2006 vic4 counterexample makes unqualified vegetative incompatibility
unsafe as an exact synonym. No synonyms, external xrefs or SSSOM equivalences
are asserted without resolving their scope and authority.

## Evidence and Limitations

- `DOI:10.1099/mic.0.032284-0` (`PMID:19696111`): definition authority;
  nonself recognition during fusion, restricted growth and localized death.
  Direct Europe PMC and publisher abstracts were read. Transcript associations
  are not causal edges, and tested caspase/AIF homologues were not required.
- `DOI:10.1016/s1087-1845(03)00086-0` (`PMID:14516765`): pairing and
  transformant microscopy evidence, with compatible controls. TUNEL does not
  by itself establish a conserved apoptosis mechanism; older hyphae also die.
- `DOI:10.3852/mycologia.98.1.43` (`PMID:16800303`): distinguishes
  heterokaryon incompatibility from barrage formation using forced pairings
  in Cryphonectria parasitica. A DOI alias is not a second replication.

All snippets are contiguous spans from directly retrieved Europe PMC
abstracts. Full texts, figures and supplements were not retrieved or
inspected: attempted publisher, Europe PMC and PMC full-text access did
not yield the required experimental details. Do not describe abstract
access as full-text review. Original strain provenance, current taxonomy,
protein accessions and native perturbation details remain CURATION_TODOs.
No canonical examples or protein-resolved causal graph are asserted.

## ID Space and Subset

Reserve `METPO:1056000` in `1056000-1056099`, following v482's block.
Ignored-and-hidden whole-repository collision searches were empty before
writing. The block does not overlap CommunityMech v1 or its extensions.
Subset: `metpo_traitmech_2026_10`. The local ID stays `traitmech:000606`
pending upstream acceptance and release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Evidence, boundaries and migration |

No property or SSSOM artifact is required. The 11-column upstream class
template retains its three trailing empty directive cells. The upstream
contract is pinned to Knowledge-Graph-Hub/kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406`.

## Verification

```bash
just verify-proposal metpo_traitmech_v483
just robot-validate-proposal metpo_traitmech_v483
just audit-proposal-coverage
just qc
```

Inspect emitted OWL for the released phenotype parent and quality ancestry,
not just a successful ELK exit. A legacy OBO METPO stub is not that parent.
Check record/template label, definition and parent parity.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following TraitMech
review. A reserved placeholder does not imply upstream acceptance.

## Round-Trip Plan

After upstream acceptance and release, update the pinned ontology and replace
the local identifier with the accepted METPO CURIE. Preserve the old local
CURIE in an explicit migration artifact and append-only history, regenerate
dependent artifacts, and avoid creating a second primary record.

## Change Log

- v483, 2026-10-04: propose heterokaryon incompatibility with three primary
  abstract snippets and explicit phenotype, terminology and access limits.
