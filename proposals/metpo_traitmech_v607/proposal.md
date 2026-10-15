# Eukaryotic Flagellar Autotomy

## Scope And Hierarchy

Propose **eukaryotic flagellar autotomy**, `METPO:1068400`, for
`traitmech:000731` (`PHYSIOLOGY`, `CLASS`, `PROPOSED`).

Definition: A physiological phenotype in which a microbial eukaryote sheds its
cilia or flagella by regulated severing of their axonemes near the base.

Scope A contains one new class for one new record. Scopes B and C contain no
predicates or schema-enum lifts. The direct parent, phenotype `METPO:1000059`,
is a definition-based inference, not a molecular mechanism. It remains below
quality `METPO:1000188`. No motility parent is required.

Possession, arrangement, assembly failure and nonmotility are not this shedding
endpoint. Resorption, retained-organelle disassembly, passive breakage, distal
vesicle release and premitotic basal-body release alone do not establish it.
Bacterial flagellar ejection/resorption involves a different apparatus and is
outside this qualified class. Palmelloid formation `traitmech:000654` does not
require flagellar loss. No exact synonyms, xrefs, SSSOM mappings, canonical taxa,
proteins, causal graphs, organism-level disjointness or universal stimulus
threshold are added. This is not a sequence feature or an inference from a
domain, motif or gene name.

## Evidence And Limits

1. [Parker and Quarmby 2003](https://doi.org/10.1186/1471-2121-4-11),
   `PMID:12930563`, `PMCID:PMC194436`, supplies the definition authority.
   Background distinguishes regulated basal axonemal severing from resorption.
   The 10-word evidence snippet matches the MED scientific abstract Results,
   second sentence, with native `VERIFIED`. Its spelling "degrees C" is the
   MED rendering, not the PDF degree glyph. All twelve main PDF pages and eight
   figures were inspected. The response concerns source-named Chlamydomonas
   fla10 in calcium-containing medium, not WTB214 at the same temperature.
   Released flagella per 100 cells, with the initial count subtracted, and
   flagellar lengths are separate endpoints. Low calcium is not calcium-free;
   buffer exchange is a confound. No universal IFT or calcium dependence follows.
2. [Hilton et al. 2016](https://doi.org/10.1534/g3.116.034264),
   `PMID:27520959`, `PMCID:PMC5068960.1`, supplies a second experimental paper,
   not independent-laboratory replication. The 15-word contiguous snippet was
   checked in JATS and on printed page 3416, Results and Discussion, ADF2 and
   ADF4 remain unassigned, first paragraph, with Figure 4A. Native
   `NOT_IN_ABSTRACT` is retained. The experiment compares 21 and 33 degrees C
   after six hours. The endpoint is a control-normalized decrease in
   biflagellate cells per 100 cells, not a direct count of released flagella or
   proof that every responding cell loses both. Figure 4A has three independent
   experiments with SD. All ten main pages, four figures and three tables were
   inspected; supplements remain unread. Phototaxis screening alone is not the
   shedding endpoint.

[Dymek and Smith 2012](https://doi.org/10.1242/jcs.096941),
`PMID:22467860`, `PMCID:PMC3516377`, is separate discussion evidence supporting
a bounded mechanism limitation, not another definition citation. Its 10-word
snippet was directly checked in the Discussion subsection on katanin and
flagellar excision; native `NOT_IN_ABSTRACT` is retained. Main HTML and all six
figures were inspected, not the supplements or a full PDF. Figure 5A assays
cellular shedding; Figure 2 assays purified protein. Transcript knockdown is
not verified protein depletion, the reference A54-e18 has listed mutations,
and tested mutants are not nulls. The result does not establish dispensability
of every katanin function. No universal FA1, FA2, TRP15 or IFT mechanism follows.

Only the 2003 DOI and local record annotate the proposed definition. Study
strain names remain qualified observations pending culture/taxonomy checks.
The [source verification receipt](../../research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json)
records locators, hashes, actual native outcomes and access limits. Nine
substantive 2016 assets matched supplied digests; the supplementary index did
not. A challenge page or failed DOI request is not a successful check. Bounded
MED/Crossref and accessible publisher/PubMed notice checks do not establish
comprehensive correction/retraction clearance. No raw-data reanalysis, paid
research or human sign-off is implied.

## Identity And Reservation

Accepted at `2026-10-15T07:50:51Z` on main
`982e7239752041073343fad00e24fbd9474e4776`. Reserve `traitmech:000731`,
`metpo_traitmech_v607` and the whole block **1068400-1068499**. Only
`METPO:1068400` is populated. Subset: `metpo_traitmech_2026_10`.

The searches included ignored and hidden current files in 202 known locations,
291 retained heads, 85,118 unique TraitMech and 9,178 CommunityMech regular
blobs, with positive regex controls. Nine unavailable locations remain limits.
The original 154 biological context windows and all 64 supplementary
biology/identifier/range windows were assessed. Final drift checks covered two
changed CommunityMech locations without editing their files; relevant matches
were lexical or numeric false positives, not exact traits or allocations.

The remote snapshot covered 13 open/draft PRs: TraitMech #1938, #1937, #1936,
#973 and draft #924; CommunityMech #2013 and draft #935; METPO #644, #643,
#641, #640, #638 and #629. All 840 nonremoved changed-file blobs and 587
selected upstream owners were screened. Original biological matches retained
identical bytes and contexts. The 07:49:31 UTC preallocation guard confirmed
unchanged main, PR heads/descriptions/draft states and selected upstream heads.

The 08:09:24 UTC prepublication guard found only CommunityMech #2013 changed,
to `a1c66812a65bf25bd694d0b8c07bc49303c47da1`, with updated review-remediation
prose. All 88 nonremoved files on that revision and its title/body were
rechecked, with no biological/exact-token hits, overlapping reservation ranges
or binary limits. The other pinned inputs remained unchanged in that guard.

Full-content range inspection included wrapped ranges and gzip decoding across
184,357 owner contexts and 2,662 unique contents. All 26 overlapping contents
concerned the general `1000000-1999999` editor envelope, not a competing narrow
reservation. No exact candidate identifier/cohort token was found in that
bounded check. These are context counts, not counts of unique traits.

Pinned/current METPO releases and editor/template context were checked
separately. Historical METPO:0000089 and METPO:000090 are deprecated with
OMO:0001000; METPO:1000381 uses IAO:0000226. Their replacement METPO:1000704
denotes locomotory flagellar possession, not shedding. Deprecated ciliated
METPO:0000093 and METPO:000094 use OMO:0001000; METPO:1000385 uses
IAO:0000226. No replacement/consider annotation was observed for those three
or deprecated flagellum METPO:1000123 (OMO:0001000). These are not exact xrefs
and are not revived. [METPO issue #521](https://github.com/berkeleybop/metpo/issues/521)
tracks reason-code interpretation. Current upstream describes a
bacterial/archaeal focus, so adoption needs maintainer review. The pin is
unchanged; the editor import stub is not treated as the full release.

Checks are bounded, not an atomic reservation or exhaustive literature search.
Lost ignored/untracked history, symlink targets, arbitrary archives and
unchanged PR files were not reconstructed. Refresh remote reservations if
publication is delayed or another relevant revision changes.

## Verification And Upstream Path

The class table preserves the canonical 11-column headers checked against the
KG-Microbe template at `1acb8b61fcae24fafc0640b1bf6e5be669f315f9`.
Run the maintained verifier and ROBOT/ELK wrapper; inspect emitted RDF for the
actual `https://w3id.org/metpo/` child/parent IRIs, phenotype hierarchy and
definition annotations. This instruction does not assert unrun gates passed.

After review, submit the class upstream. The reserved ID is not released.
On acceptance and release, separately review scope, update the pin, re-seed
and migrate the local identifier while retaining its prior spelling for
traceability. No upstream PR or human scientific approval is implied here.
