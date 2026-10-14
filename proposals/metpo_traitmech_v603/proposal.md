# Fungal Nematode Endoparasitism

## Context And Scope

Propose `METPO:1068000`, **fungal nematode endoparasitism**, for local
`traitmech:000727` (`ECOLOGY`, `CLASS`, `PROPOSED`). TraitMech uses the local
fallback only after evidence and active/historical METPO identity checks.

Definition: An animal-pathogenic phenotype in which a fungus uses spores
attached to or ingested by a vermiform nematode to initiate infection and then
grows inside the host.

| Scope | Classes | Properties | Parent |
|---|---:|---:|---|
| A: one synthetic trait lift | 1 | 0 | METPO:1004002 animal pathogen |
| B: predicates | 0 | 0 | Not needed |
| C: schema enums | 0 | 0 | Not needed |

This separate single-trait cohort follows the current add-trait convention;
it neither redefines nor supersedes any merged cohort. No equivalent external
mapping was accepted, so no SSSOM file is emitted.

## Hierarchy Decisions

The fungus, not its nematode host, bears this trait. Animal pathogen
`METPO:1004002` is active below pathogenic to host `METPO:1004000`, phenotype
`METPO:1000059` and quality `METPO:1000188`. Current upstream clarifies the
pinned parent's organism-like definition as a phenotype; this addition does
not rewrite that parent or change the ontology pin.

This is the established **spore-infection strategy**, not all fungal growth
anatomically inside a nematode. The host-contacting or ingested spore initiates
infection. Germination into an external hyphal trap does not satisfy that
route. Attachment, ingestion, killing, internal occupancy without this route,
and sequence annotations alone are insufficient.

Vermiform stages distinguish the selected strategy from eggshell penetration
in fungal nematode egg parasitism `traitmech:000726`. Fungal nematophagy
`traitmech:000719` requires feeding and includes dead prey; fungal nematode
trap formation `traitmech:000718` concerns hyphal differentiation. Neither is
asserted as a parent. Local parasitism `traitmech:000043` inherits persistent
symbiosis, which this phenotype does not require. No organism-level
disjointness, exclusive host stage, universal host range, mammalian
pathogenicity or obligacy follows. Generic endoparasitism is not an exact synonym.

## Evidence And Limits

1. [Lebrigand et al. 2016](https://doi.org/10.1371/journal.pgen.1006017),
   `PMID:27153332`, `PMCID:PMC4859500`: definition authority. The 20-word
   scientific-abstract excerpt directly matches JATS; native `VERIFIED`.
   Author Summary and Discussion distinguish this strategy from traps and
   egg infection. Actual Figures 8/9 show recombinant fungal growth in
   C. elegans. Both S1 Text pages were read and visually inspected: the
   laboratory line underwent about 15 years of passage, and the source
   isolate and ARSEF 6962 share provenance. "Obligate" is the authors'
   species description, not a universal requirement or inability to grow on
   their artificial medium. Gene predictions and expression are not causal
   effectors or universal trait mechanisms.
2. [Sun et al. 2024](https://doi.org/10.3390/jof10010068), `PMID:38248977`,
   `PMCID:PMC10820206`: internal-growth evidence. The 16-word Results 3.2
   excerpt directly matches JATS; native `NOT_IN_ABSTRACT` remains unchanged.
   Methods 2.5 and actual Figure 2c,d concern engineered HR-eGFP1 on
   Bursaphelenchus xylophilus. Methods 2.6 counts attached spores **or**
   colonization: no reported percentage is curated as an internal-infection
   rate. Figure 3 and the complete two-page S1-S3 supplement were inspected.
   The tentative main-text ingestion-route suggestion is not silently
   strengthened by a supplement caption. Morphological similarity to wild
   type does not establish unchanged virulence; plant endpoints are omitted.
3. [Glockling and Shimazu 1997](https://doi.org/10.1017/S0953756296002092):
   distinct primary abstract supporting spore-ingestion infection in
   Harposporium cycloides. The 13-word excerpt directly matches the publisher
   scientific Abstract. Crossref and Europe PMC `AGR:IND20619532` verify
   identity. Native `UNRESOLVED` means no abstract was returned, not that
   the article is unindexed. Full Methods, figures and host/strain provenance
   were not accessed; no dose, route universality or canonical taxon is asserted.

Only Lebrigand and the local record annotate the proposal definition. Sun and
Glockling provide supporting evidence, not extra definition-source annotations.
Actual record-specific CLI results, retrieval URLs, hashes, sections and
inspected assets are retained in the
[source-verification sidecar](../../research/traits/ecology/fungal_nematode_endoparasitism-source-verification.json).
Direct source matching never converts `NOT_IN_ABSTRACT` or `UNRESOLVED` into
an abstract verification. Jansson 1993 and other retrieved literature leads
are not counted support. Full raw data and all genomic tables were not audited.
Bounded notice queries and retrieved metadata are not comprehensive
correction/retraction clearance; the direct MDPI page returned HTTP 403.

No canonical taxa, proteins, causal graph, exact synonyms or equivalent xrefs
are asserted. Microscopy is not a nutrient-flux assay; no quantitative
threshold, field efficacy or safety claim is made. Three OPEN discussions
retain hierarchy, historical identity and evidence/provenance gaps.

## Identity And Reservations

Author acceptance: `2026-10-14T15:19:28Z`, clean main
`b41e4ed2266eaef45db087014dd707bd1f3f273d`. Ignored/hidden files were included
in 192 known locations; retained-history checks covered 143 heads, 23,435
TraitMech and 5,815 CommunityMech unique regular-file blobs. All 26 matched
path/text variants (1,656 occurrences) were assessed. Existing bacterial
predation mentions are not this fungal trait; other hits concern spore
resistance, infection control, unrelated plant pathogens, an endozoic ciliate
clade or a nematode parasitizing a plant. Supplemental Meria coniospora,
Haptocillium and spore-initiated/mediated-infection alias checks found no
same-scope record in the inspected owners. No exact same-scope synonym,
ungrounded graph node or parent-gap discussion requiring migration was identified.

Pinned/current METPO releases have 12,617/12,649 triples; the byte-verified
editor conversion has 31. None imports another ontology. Six template owners
were separately checked; the editor alone is not absence evidence. Historical
`METPO:1000227` obsolete parasitism is broader, deprecated, under
ObsoleteClass with `OMO:0001000`, with no replacement or consider annotation
in either release. [METPO issue 521](https://github.com/berkeleybop/metpo/issues/521)
disputes mechanically assigned reasons. This does not justify reviving that
identifier, declaring the biology invalid or treating it as an exact xref.

Remote screening covered 11 open/draft PRs, 783 nonremoved changed blobs and
587 selected upstream owners: TraitMech #1782, #1476, #973, draft #924;
CommunityMech draft #935; METPO #644, #643, #641, #640, #638 and #629.
Fresh heads, bodies and states were checked at acceptance. Three pending
matches were generated-page spore/tracer context in #924; 103 values in a
structured KG-Microbe JSON match were Endozoicomonas/Parendozoicomonas
bacterial taxonomy/references, not fungal endoparasitism.

Reserve local ID `traitmech:000727`, cohort `metpo_traitmech_v603` and the full
METPO block **1068000-1068099**; only `METPO:1068000` is proposed. The numeric
hit `chemspider:1068002` maps to CHEBI:171826 in structured SSSOM, not METPO.
All 1,057 interval overlaps denote the broad `1000000-1999999` editor envelope
or its documentation. Full-content inspection covered 47,921 owner contexts
and 2,567 unique contents, including wrapped proposal ranges. No conflicting
narrower reservation was identified. CommunityMech's 1007100-1007220 block
does not overlap. The template subset is `metpo_traitmech_2026_10`.

These are bounded checks, not atomic allocation or literature exhaustion.
Unavailable ignored/untracked history, symlink targets, submodules and arbitrary
archives were not reconstructed; remote scope is changed blobs and selected
owners, not every unchanged file. Recheck live reservations before publication.

## Files And Verification

| File | Content |
|---|---|
| metpo_proposal_classes_robot.tsv | One class, canonical 11-column two-row header |
| proposal.md | Scope, evidence, reservations and migration plan |
| Source-verification sidecar linked above | Source and search provenance |

Required commands: `just verify-proposal metpo_traitmech_v603` and
`just robot-validate-proposal metpo_traitmech_v603`. Inspect actual emitted
RDF to confirm `https://w3id.org/metpo/` IRIs, the real animal-pathogen parent
chain and definition annotations. Native gate results are saved with the
structured review; this narrative does not claim an unrun check passed.

## Upstream And Round Trip

After local sign-off, the ROBOT template can be submitted to berkeleybop/metpo.
The proposed identifier is not yet a released term and no KG assertion should
treat it as minted upstream. On upstream acceptance and release, a separately
reviewed migration must recheck exact identity, update the ontology snapshot,
re-seed and replace the local identifier while preserving the old identifier
as a traceability synonym. No upstream PR is implied by this local proposal.

## Change Log

- 2026-10-14: v603 introduces one fungal spore-infection phenotype; prior
  records, proposals and protected spore germination remain unchanged.
