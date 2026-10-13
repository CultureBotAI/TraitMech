# Nematode-Attracting Activity

## Context And Scope

One Scope-A physiological CLASS, `traitmech:000721`, proposed as
`METPO:1067400`: **nematode-attracting activity**. A physiological capability
of a microorganism to elicit directed movement of nematodes toward itself or
substances it produces. The record remains `PROPOSED`, without human sign-off.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: attracting capability | 1 | METPO:1000059 phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This is the microbial actor's capability, not microbial chemotaxis, a
nematode's sensory trait, an assay, or a chemical role. Passive retention or
co-occurrence alone is insufficient. Trapping, paralysis, killing, feeding,
infection, field recruitment, fitness benefit and predatory intent are not
required or inferred. No universal strain, nematode-species or stage coverage
is asserted. The evidence uses volatile-mediated assays but does not establish
that all microbial attraction must use one chemical or sensing mechanism.

## Evidence

- **Definition authority:** [Hsueh et al. 2017](https://doi.org/10.7554/eLife.20023),
  PMID:28098555. The 14-word scientific-abstract excerpt links the fungal
  producer to attracted nematodes; native `VERIFIED` and direct XML match.
  Figure 1B/D supplies behavior, not the structural capture image 1E.
  Responses vary by host and stage; azide retains arrivals, not fungal killing.
- **Separate primary support:** [Choi et al. 2016, online 2015](https://doi.org/10.1038/ismej.2015.134),
  PMID:26241504. The 16-word Discussion result links bacteria grown on
  specified media to nematode attraction. Native `NOT_IN_ABSTRACT`; exact
  publisher HTML match. Lid-mounted bacterial plugs are compared with
  bacteria-free medium; citrate medium also contains glucose. YSM0385 is
  the reported L. paracasei strain; Y091 is only Lactobacillus sp.

Only Hsueh and the local record annotate the proposal definition. Choi is
independent supporting evidence, not an automatically copied definition citation.
Both studies have directly read source passages; search-result text is not
used as a quote. The [source-verification sidecar](../../research/traits/physiology/nematode_attracting_activity-source-verification.json)
retains source hashes, sections, native outcomes, notice-check scope and access limits.

Two OPEN discussions preserve hierarchy and source/mechanism gaps. Hsueh's
headspace workbook has a medium-control signal conflicting with its
five-compound exclusivity caption. The published review exchange does not
establish evolutionary adaptation or exact pheromone mimicry. Choi's host
odr-10 allele differs between Methods/captions and Results; a shared supplement
link exposes a colony-count image, not a separately verified S2 calibration.
No complete raw-statistical audit, Choi typeset-PDF inspection, canonical taxon,
microbial protein example or common causal graph is claimed.

## Hierarchy Decisions

Use `METPO:1000059` phenotype below `METPO:1000188` quality. Trapping,
nematophagy and lethal nematicidal activity have different endpoints; they
are not necessary parents or exact equivalents. A microorganism may have
several of these capabilities, so no organism-level disjointness follows.

Inspection covered all literal annotations in three explicit pinned/current
OWL files and all cells in six selected upstream TSV owners, including
deprecated and draft terms. No exact active or deprecated counterpart was
identified in that bounded screen. The editor OWL is a metadata skeleton,
not an independently inspected import closure. The pinned ontology is unchanged.
No xrefs, exact synonyms, SSSOM alignments or sequence-feature claims are added.

## Novelty And Reservation

Acceptance: `2026-10-13T23:01:02Z`; base
`33d043127f3cd214fc6608745172c95b1fdaf00f`.
Ignored and hidden files were included across 176 known locations. Retained
tracked-history screening covered 139 heads using native positive-controlled
Git searches, with shared regular-file blobs searched once. The novelty
continuation matched all 24 completed earlier native full-tree results;
the interrupted original phase is not reported as a completed scan.

No same-scope maintained record, proposal or unresolved exact node was found.
Existing trapping/killing records distinguish attraction. Exact paper DOIs
do occur in CommunityMech's ignored literature cache; those bibliography
mentions are not a competing trait. TYQ1 attraction concerns bacterial
partners, not this endpoint. These are bounded semantic decisions, not claims
that attraction was never mentioned.

Remote screening completed at `2026-10-13T23:00:03.775174+00:00`: 11 open/draft
PRs, 783 nonremoved changed blobs and 587 selected upstream owner blobs.
All inspected remote blobs were unchanged from the prior novelty assessment:

- TraitMech #1782, #1476, #973 and draft #924.
- CommunityMech draft #935; main `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- METPO #644, #643, #641, #640, #638 and #629;
  main `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- KG-Microbe main `32a99f2407f5c0ac3273a432432d8f2936b3b685`.

The 128 exact-number hits are decimal values: 127 occurrences in copies of
a cached CommunityMech supplement and one embedding coordinate in draft
#924. All 481 interval overlaps denote the broad `1000000-1999999` editor
envelope or its documentation, not narrower reservations. No conflicting
reservation remained in the inspected scope. Recheck before publication;
this is not an atomic allocation service.

Unavailable historical ignored/untracked files, symlink targets, submodules
and arbitrary local archives were not reconstructed. Pending PR screening
covers changed blobs, not every unchanged file. Discovery is not exhausted.

## ID Space And Files

Reserve local `traitmech:000721`, cohort `metpo_traitmech_v597` and the whole
`METPO:1067400`-`METPO:1067499` block. Only `METPO:1067400` is populated;
it is not released. Subset: `metpo_traitmech_2026_10`. The block does not
overlap the inspected CommunityMech v1 allocations or their extensions.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM template | 0; omitted |

Keep 11 columns and the required empty ROBOT header cells. Definition
citations are not mappings. METPO IRIs expand to `https://w3id.org/metpo/`.

## Verification And Upstream Path

Before publication, require guarded-writer tests, schema/strict and native
snippet checks, history, generated products, proposal coverage, ROBOT/ELK
with RDF inspection, full QC and a saved adversarial record review. These
are requirements, not a claim that unfinished checks passed.

After curator sign-off, submit the template to METPO or KG-Microbe. Adoption
requires a separately reviewed pinned-release refresh and identifier migration,
preserving the local ID, provenance and incoming references. Automated
validation cannot promote the record to human `REVIEWED` status.

## Change Log

- 2026-10-13, v597: one microbial attracting capability, two primary-source
  excerpts, explicit source/assay limitations and two OPEN discussions.
