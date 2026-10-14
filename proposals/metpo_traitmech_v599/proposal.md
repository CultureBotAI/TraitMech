# Nematode Egg-Hatching Inhibitory Activity

## Context And Scope

One Scope-A physiological CLASS, `traitmech:000723`, proposed as
`METPO:1067600`: **nematode egg-hatching inhibitory activity**. A physiological
capability of a microorganism to reduce nematode egg hatching over a defined
observation interval relative to comparable unexposed controls.
The record remains `PROPOSED`, without human sign-off.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: microbial hatch inhibition | 1 | METPO:1000059 phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This is the microorganism's capability, not its own development, the
nematode's susceptibility, a source column, chemical role or sequence feature.
Hatch reduction does not establish egg death, irreversible arrest or later
recovery. Juvenile killing or paralysis, fewer root egg masses, population
suppression, trapping and attraction alone do not establish this endpoint.
Feeding, infection, a particular active molecule and a secretion mechanism
are not required. No universal host/stage range or numerical cutoff is imposed.

## Evidence

- **Definition authority:** [Meyer et al. 2004](https://doi.org/10.1163/156854104323072883).
  A 22-word Results excerpt directly reports fungal-filtrate hatch reduction.
  All ten pages of the USDA-hosted publication PDF were inspected, including
  the quoted page, Table 1 and Figure 1. The record preserves control-based
  denominators, host-specific assay concentrations and the distinction between
  culture age and exposure interval. The PDF text extractor loses a ligature;
  the quote follows the actual typeset passage. USDA and Crossref establish
  article identity despite the native `UNRESOLVED` result.
- **Second primary hatch experiment:** [Saharan et al. 2023](https://doi.org/10.1038/s41598-023-33669-z),
  PMID:37088805. A 13-word Results excerpt matches original publisher HTML.
  It reports this study's experiment, not its background description of Meyer.
  Methods and actual Figure 3 were inspected. Timing and strain-provenance
  discrepancies remain explicit; neither egg death nor the juvenile recovery
  endpoint is transferred to hatching. Native result: `NOT_IN_ABSTRACT`.

Only Meyer and the local record annotate the proposal definition.
Saharan supplies additional primary support; its citation is not copied
automatically into the definition annotation. Direct source matches are
not native `VERIFIED` results. An inconclusive abstract check is not proof
of fabrication, and a source match is not independent replication of the assay.

The [verification sidecar](../../research/traits/physiology/nematode_egg_hatching_inhibitory_activity-source-verification.json)
retains source URLs, SHA-256 hashes, exact locators, native outcomes,
notice-check scope and access limits. Earlier research receipts retain their
historical unfinished states; the later assessments explicitly supersede them.
Meyer has no Crossmark data available; Saharan's current Crossmark and index
checks do not establish comprehensive correction/retraction clearance.

Two OPEN discussions preserve scope/hierarchy and source/mechanism gaps.
No canonical taxon, exact synonym, xref, protein example or causal graph is
asserted. No field efficacy, environmental safety, common active molecule
or complete raw-data/statistical reanalysis is claimed.

## Hierarchy Decisions

Use active `METPO:1000059` phenotype below `METPO:1000188` quality.
The existing lethal, paralyzing, trapping, attracting and fungal-nematophagy
traits have different endpoints and are not necessary parents or equivalents.
The same microorganism may have several of these capabilities; no
organism-level disjointness is proposed.

Pinned `animal pathogen` mentions infection. Current upstream places it below
an infectious-disease/disorder phenotype. Neither meaning is required for
cell-free hatch inhibition, so it is not used as parent.

The ontology screen inspected literal annotations in three explicit
pinned/current OWL inputs and all cells in six selected TSV owners, including
deprecated and draft terms. The only lexical lead was `METPO:1007069`,
fried-egg-shaped colony, with related annotations and a stub row. That
morphological analogy is not an exact active or historical counterpart.
The editor input has 31 triples and no imports after ROBOT conversion;
it is metadata, not a substitute for the separately inspected release OWL.
Initial XML-parser and unsupported-format attempts failed and are not
counted as successful checks. The pinned ontology is unchanged.
Ovicidal labels and nematicide chemical-name mappings are not exact xrefs.

## Novelty And Reservation

Acceptance: `2026-10-14T03:09:57Z`; base
`4200c75a930654cfec7e635edcbcec896efef919`.
The current-copy search included ignored and hidden files across 182 known
locations, 178 available. Retained tracked-history screening covered 139
heads. All 76 matched paths were adjudicated. Existing reduced-hatch passages
are exclusions or literature context, not an exact trait, synonym, ungrounded
node or same-scope parent-gap TODO requiring coupled repair.

PGPT sequence categories remain prediction leads. Cached TYQ1 literature
contains a hatch endpoint, but its CommunityMech consortium record is not
an exact microbial trait class. Bibliographic nematicide mentions and the
`novicida` lexical match do not establish a duplicate. No other curated
record needs modification for this addition.

Reservation checks covered the local ID, cohort, full hundred block and
overlapping declared numerical intervals. They found zero exact-number,
local-ID or cohort matches. All 665 overlapping interval occurrences denote
the broad `1000000-1999999` METPO editor envelope or documentation of it,
not narrower competing reservations.

Remote checks covered 11 open/draft PRs, 783 nonremoved changed blobs and
587 selected upstream owner blobs. Exact heads, titles and bodies were
rechecked before acceptance:

- TraitMech #1782, #1476, #973 and draft #924.
- CommunityMech draft #935; main `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- METPO #644, #643, #641, #640, #638 and #629;
  main `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- KG-Microbe main `3db7393ad591a7876f3c981dd70cc68ce9d37add`.

All selected owner contents remained identical across the refreshed semantic
and reservation screens. Recheck before publication; these observations are
not an atomic reservation service. Unavailable historical ignored/untracked
files, symlink targets, submodules and arbitrary local archives were not
reconstructed. Pending PR checks cover changed blobs, not every unchanged
file. This is bounded novelty review, not literature exhaustion.

## ID Space And Files

Reserve local `traitmech:000723`, cohort `metpo_traitmech_v599` and the whole
`METPO:1067600`-`METPO:1067699` block. Only `METPO:1067600` is populated;
it is not a released identifier. Subset: `metpo_traitmech_2026_10`.
The block does not overlap inspected CommunityMech allocations or extensions.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM template | 0; omitted |

Preserve the canonical 11-column header and required empty ROBOT cells.
Definition citations are not mappings. Proposal and parent IRIs must expand
to `https://w3id.org/metpo/`, matching the pinned ontology.

## Verification And Upstream Path

Before publication, require guarded-writer tests, LinkML/strict and native
snippet checks, history, regenerated products, proposal coverage, ROBOT/ELK
with RDF inspection, full QC and a saved adversarial record review. These
are requirements, not a claim that unfinished checks passed.

After curator sign-off, submit the template to METPO or KG-Microbe. Adoption
requires a separately reviewed pinned-release refresh and identifier
migration, preserving the temporary ID, provenance and incoming references.
Automated checks do not promote the record to human `REVIEWED`.

## Change Log

- 2026-10-14, v599: one microbial hatch-inhibitory capability, two directly
  inspected primary-source excerpts and two OPEN discussions.
