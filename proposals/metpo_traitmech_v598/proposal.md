# Reversible Nematode-Paralyzing Activity

## Context And Scope

One Scope-A physiological CLASS, `traitmech:000722`, proposed as
`METPO:1067500`: **reversible nematode-paralyzing activity**. A physiological
capability of a microorganism to induce a loss of active nematode movement
that reverses after exposure to the microorganism or its products ends.
The record remains `PROPOSED`, without human sign-off.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: reversible paralyzing capability | 1 | METPO:1000059 phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

The microbial actor has the capability; the nematode loses and recovers
movement. This is not microbial nonmotility, nematode susceptibility, an
assay, a chemical role or a sequence-feature annotation. Recovery after
removal is required. Immobility, reduced speed, trapping, attraction,
killing, reduced egg hatch or population suppression alone is insufficient.
Infection, feeding, a neural target and a particular active molecule are
not required. Neither a universal recovery time nor universal host/stage
susceptibility is implied.

## Evidence

- **Definition authority:** [Kilama et al. 2007](https://journals.flvc.org/nematropica/article/view/64427).
  The 19-word English Abstract excerpt explicitly links microbial filtrates
  to reversible paralysis. Publisher HTML, PDF text and the typeset passage
  were inspected directly. Recovery is reported in Results/Table 2;
  Figure 1 depicts initial immobilization. The record preserves failed or
  confounded bioassays and strain, dose and timing discrepancies.
- **Separate primary recovery support:** [Cayrol, Djian and Pijarowski 1989](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/pleins_textes_5/pt5/nemato/27861.pdf).
  The 22-word Results excerpt reports recovery after water transfer; it is
  not a standalone producer-identity excerpt. The surrounding experiment
  identifies fungal filtrate and the tested larvae. Actual Figure 3 and
  the typeset passage were inspected. The PDF text layer misreads `all`
  as `dl`; the stored quote follows the printed page. The record retains
  Summary/Results exposure-boundary differences without inventing a
  universal cutoff or demonstrating a neural mechanism.

Only Kilama and the local record annotate the proposal definition.
Cayrol supplies a second primary recovery study, not an automatically
copied definition citation. Both references are stable URLs. The maintained
DOI/PMID verifier skips URL references and emits no rows for them: manual
matching is not a native `VERIFIED` result. No DOI or PMID was invented to
obtain a resolver result. Search-result excerpts were not used as evidence.

The [verification sidecar](../../research/traits/physiology/reversible_nematode_paralyzing_activity-source-verification.json)
records source hashes, sections, direct checks, native outcomes, notice-check
scope and access limitations. Historical research receipts remain unchanged;
later assessments explicitly supersede their unfinished checks.

Two OPEN discussions preserve hierarchy and source/mechanism gaps. No
canonical taxon, exact synonym, xref, microbial protein example or causal
graph is asserted. Taxonomic authority and strain provenance are not yet
resolved for exemplar purposes. No full raw-data or statistical reanalysis,
field efficacy or environmental safety is claimed. URL availability and
bounded notice searches do not constitute comprehensive source clearance.

## Hierarchy Decisions

Use `METPO:1000059` phenotype below `METPO:1000188` quality. Existing
lethal-nematicidal activity, fungal nematophagy, trap formation and attraction
have different endpoints and are not necessary parents or equivalents.
A producer or product can cause reversible paralysis in one condition and
death in another; no organism-level disjointness is proposed.

The documented screen covered literal annotations in three specified
pinned/current OWL inputs and all cells in six selected current TSV owners,
including deprecated/draft terms. No exact active or deprecated counterpart
was identified in that scope. The editor file is metadata, not an inspected
import closure. The pinned ontology is unchanged. Nematostatic terminology
and nematicide chemical mappings are not silently adopted as equivalents.

## Novelty And Reservation

Acceptance: `2026-10-14T01:02:02Z`; base
`f44af60a9d88dcc604543301a8669e1e2bff428d`.
The current-copy search included ignored and hidden files across 179 known
locations, 176 available. Retained tracked-history screening covered 139
heads. All 88 matched paths were adjudicated; existing paralysis passages
are exclusions or qualified comparators, not an exact trait, synonym,
ungrounded exact node or parent-gap TODO requiring coupled repair.
PGPT sequence categories and cached literature are leads, not validated
organismal traits. No other curated record needs editing for this addition.

Reservation screening included the local ID, cohort and full hundred block,
with overlapping numerical intervals checked separately. An initial Git
PCRE2 control rejected Unicode escape syntax; after correction to literal
dash characters, the historical phase completed with positive controls.
The failed phase is not counted as a successful check.

Remote screening completed at `2026-10-14T00:59:23.960608+00:00`:
11 open/draft PRs, 783 nonremoved changed blobs and 587 selected upstream
owner blobs. All inspected owner blobs remain byte-identical to the earlier
semantic screen, including after KG-Microbe main advanced:

- TraitMech #1782, #1476, #973 and draft #924.
- CommunityMech draft #935; main `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- METPO #644, #643, #641, #640, #638 and #629;
  main `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- KG-Microbe main `fe3b8d6145483518968a313ea66f2736bd6c283e`.

The 256 exact-number matches are decimals: 253 occurrences of a measurement
in copies of a CommunityMech supplement and three embedding coordinates
in draft #924. All 572 overlapping intervals denote the broad
`1000000-1999999` METPO editor envelope or its documentation, not narrower
reservations. No conflicting reservation remained in the inspected scope.
Recheck before publication; this is not an atomic allocation service.

Unavailable historical ignored/untracked files, symlink targets, submodules
and arbitrary local archives were not reconstructed. Pending PR screening
covers changed blobs, not every unchanged file. This is bounded novelty
review, not a claim that the phrase was never mentioned or that discovery
is exhausted.

## ID Space And Files

Reserve local `traitmech:000722`, cohort `metpo_traitmech_v598` and the whole
`METPO:1067500`-`METPO:1067599` block. Only `METPO:1067500` is populated;
it is not released. Subset: `metpo_traitmech_2026_10`. The block does not
overlap the inspected CommunityMech v1 allocations or extensions.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM template | 0; omitted |

Keep the canonical 11-column header and required empty ROBOT cells.
Definition citations are not mappings. METPO IRIs must expand to
`https://w3id.org/metpo/`.

## Verification And Upstream Path

Before publication, require guarded-writer tests, LinkML/strict and native
snippet checks, history, generated products, proposal coverage, ROBOT/ELK
with RDF inspection, full QC and a saved adversarial record review. These
are requirements, not a claim that unfinished checks passed.

After curator sign-off, submit the template to METPO or KG-Microbe. Adoption
requires a separately reviewed pinned-release refresh and identifier
migration, preserving the temporary local ID, provenance and incoming
references. Automated checks do not promote the record to human `REVIEWED`.

## Change Log

- 2026-10-14, v598: one microbial reversible paralyzing capability, two
  directly inspected primary-source excerpts and two OPEN discussions.
