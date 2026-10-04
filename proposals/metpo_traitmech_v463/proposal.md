# METPO Proposal v463: Chemokinesis

## Context

Lift `traitmech:000586 chemokinesis`, following the bacterial swimming-speed
usage of Garren et al. (DOI:10.1038/ismej.2013.210), Son et al.
(DOI:10.1073/pnas.1602307113), and Gao et al.
(DOI:10.1038/s41396-021-01024-7). The fourth evidence source,
DOI:10.7717/peerj.17126, supplies experimental-strain provenance only.

Temporary seeding emitted 399 identifiers: 344 present and 55 absent from
the pre-change 980-record corpus. Both frozen release-review tables were
checked against live records. Whole-repository searches included ignored
and hidden files, chemokinesis/orthokinesis/klinokinesis alternatives,
chemical-induced speed phrases, citations, and the proposed identifiers.
The substantive prior hit was a chemotaxis research boundary note, not an
exact record, METPO class or unresolved YAML graph node. That note remains
correct. The upstream METPO issue search returned no chemokinesis result.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | motile | 1 |
| B: predicates | 0 | None proposed | 0 |
| C: schema enums | 0 | Outside this addition | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1054000 | traitmech:000586 | chemokinesis | METPO:1000702 |

The parent denotes energy-dependent locomotion. Chemokinesis here denotes
chemical-dependent swimming-speed modulation, without requiring directional
bias. It may coexist with chemotaxis, but neither equivalence nor
disjointness nor a parent-child relation between them is asserted.
PHYSIOLOGY follows the neighboring behavioral motility records. The
definition does not require increasing speed, a particular chemical or one
universal receptor. Broader turning-frequency usage remains an explicit
terminology TODO; it is not silently added as an exact synonym.

## Evidence And Mapping Boundaries

- Four primary DOI evidence items carry short contiguous snippets.
  Garren's definition passage (page 1005), Son's Figure S5 and caption,
  and Gao's hypothesis passage (page 3677) were visually inspected in
  author-hosted published PDFs. Son's full article and embedded SI were
  inspected. No supplementary gene-level result from Gao or independent
  reanalysis of Garren's supplementary assays is claimed.
- The uniform-serine experiment distinguishes a speed response from
  gradient-following. Its conditions are retained in evidence notes.
- Local adversarial review #1653 identified YM4 as a laboratory mutant
  with defective lateral flagellation, independently supported by the
  strain-provenance paper's abstract (PMID:38515459). The observation is
  retained as qualified evidence, not a natural canonical example. No
  taxon identifier or universal species assertion is emitted.
- Son's functional-block removals are computational, not gene deletions.
  Gao explicitly presents the proposed Na+-NQR explanation as a hypothesis
  needing experimental tests. No causal protein graph is inferred from
  these results or borrowed from the existing chemotaxis graph.
- Two open discussions retain terminology and molecular-grounding gaps.
  Canonical examples are deferred pending verification of a natural
  exemplar. No equivalent xrefs or SSSOM mappings are asserted.

Source checks: 2026-10-04. The add-trait skill now explicitly distinguishes
model ablations and transcript associations from causal perturbations.

## ID Space And Subset

Reserve `METPO:1054000-1054099`, using only `1054000`, after v462's
`1053900` block. Ignored-and-hidden searches found no collision before
writing. The block is disjoint from the inspected CommunityMech v1 class
and property identifiers. Subset: `metpo_traitmech_2026_10`.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Properties and SSSOM | Omitted: no predicate or equivalent mapping |

The refreshed upstream class template has 11 columns, including three
trailing empty cells in the ROBOT directive row.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v463`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v463` and
`scripts/verify_metpo_proposal.py --coverage`. Actual validation results and
rendered-page checks are recorded in the PR.

## Upstream Path

Submit the verified TSV to berkeleybop/metpo after TraitMech review.
The reserved placeholder is not an accepted or released METPO identifier.

## Round-Trip Plan

After upstream acceptance, refresh METPO, seed a temporary tree and migrate
to the released identifier while retaining `traitmech:000586` in provenance.
Regenerate affected artifacts; do not publish the placeholder as released.

## Change Log

- v463, 2026-10-04: add source-qualified chemokinesis and address review #1653.
