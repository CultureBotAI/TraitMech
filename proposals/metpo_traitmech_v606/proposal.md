# Stalk Contraction

## Scope And Hierarchy

Propose **stalk contraction**, `METPO:1068300`, for `traitmech:000730`
(`PHYSIOLOGY`, `CLASS`, `PROPOSED`).

Definition: A physiological phenotype in which a microbial cell actively reduces
the end-to-end extension of its stalk.

Scope A contains one new trait, used by this one new record, and one repeated
parent declaration. Scopes B and C contain no predicates or schema-enum lifts.
This is an observable microbial phenotype, not a structure record, sequence
feature, protein, one-off assay row or a universal molecular mechanism.

The direct parent is **cell body or cytoplasmic projection contraction**,
`traitmech:000729`, proposed as `METPO:1068200` in v605. This is a
definition-based subclass inference. The source-named Vorticella stalk contains
an intracytoplasmic contracting thread within a sheath; the whole composite
stalk sheath is not asserted to be cytoplasm. The parent allows reduced
projection extension, not only reduced contour length. Active denotes a
cellular contraction response, not demonstrated ATP-driven motor action.

The parent is not in the pinned ontology. The two-row template therefore copies
its existing v605 declaration without changing any cell or allocating another
parent ID, and emits `METPO:1068300 rdfs:subClassOf METPO:1068200`. That parent
remains below phenotype `METPO:1000059`, then quality `METPO:1000188`.
Historical v605, its child axioms and the ontology pin are unchanged.

The same branch replaces only the parent's stalk-contraction future-lead
sentence with the new child link, through a preimage-guarded writer. Its
definition, evidence, hierarchy, other discussion prose and prior history are
preserved. Independent scope and mechanism questions stay OPEN. Historical
v605 prose and source receipts still describe their original curation scope;
they are not claims that this later child is absent today.

Reduced end-to-end extension need not shorten the stalk contour. Coiling is
observed, not required universally. Static stalk morphology, reduced growth,
passive bending, detachment and isometric force alone are insufficient.
Stalk-induced body displacement is not cell-body contraction `traitmech:000728`
and differs from rapid axopodial contraction `traitmech:000682`. No locomotion,
universal rate, force, calcium threshold, energy source or organism-level
disjointness is asserted. No synonyms, xrefs, SSSOM mappings, canonical taxa,
proteins or causal graphs are added.

## Evidence And Limits

1. [Kamiguri et al. 2012, Part I](https://doi.org/10.2142/biophysics.8.1),
   `PMID:27857602`, `PMCID:PMC5070450`: definition authority and direct
   high-speed imaging. Printed page 3, Results and Discussion first paragraph,
   describes a straight stalk bending and coiling; the same paragraph explicitly
   distinguishes unchanged contour length from reduced extension. The 19-word
   excerpt was checked against extracted text and the actual typeset passage.
   All nine main-paper pages, Figures 1-10 and Tables 1-2 were inspected.
   Eight source-named Vorticella sp. cells from activated sludge were observed at
   6000 frames/s after dish-hit stimulation, attached to glass rods. Models are
   not molecular proof; raw videos were not reanalyzed. Junko Kamiguri is the
   PDF's first author despite its Hashimoto et al. running header. The
   [J-STAGE PDF](https://www.jstage.jst.go.jp/article/biophysics/8/0/8_0_1/_pdf/-char/en)
   is retained by hash. Its acquisition helper failed after saving the file;
   the missing original request time and headers are not reconstructed.
2. [Ryu et al. 2012](https://doi.org/10.1016/j.bpj.2012.07.038),
   `PMID:23009835`, `PMCID:PMC3433611`: independent experimental support.
   Printed page 862, Figure 2A caption, sentence beginning "The stalk
   contraction", reports increasing stall with viscosity/flow. The 14-word
   excerpt, actual panels and all eight main-paper pages were inspected in the
   [Lang Lab primary-paper mirror](https://lab.prd.vanderbilt.edu/lang-lab/wp-content/uploads/sites/195/2023/01/MaximalForceCharacteristicsoftheCa2D-PoweredActuatorofVorticellaconvallaria2012.pdf).
   Source-named Vorticella convallaria contracted in microfluidic channels.
   Four to five contractions per cell per condition are repeated measurements,
   not independent cells; Figure 3 uses six cells and Figure 4C fifteen in a
   separate analysis. Isometric force is extrapolated through a hydrodynamic
   model, not directly measured at zero shortening. Geometry/projection
   assumptions and uninspected supplements remain limits. Extracted micrometre
   symbols sometimes appear as mm; no such numeric extraction is quoted.

Both native snippet outcomes are `NOT_IN_ABSTRACT`, retained separately from
direct full-text matches. Only the first paper and local curation record
annotate the new definition. The copied parent row retains its existing
Katoh citation, `DOI:10.1242/jeb.189.1.163`, without making it an additional
new child citation.

[Amos 1971](https://www.nature.com/articles/229127a0),
`DOI:10.1038/229127a0`, supplies anatomical background only. Its directly read
publisher Abstract second sentence locates the spasmoneme inside cytoplasm and
a sheath. The 17-word excerpt is in discussion evidence with `NO_EVIDENCE`
and an explicit context-only explanation, not counted trait support or a
definition annotation. Native `UNRESOLVED` is retained; issuing DOI/title/author
metadata was checked, but this is not a VERIFIED verdict or proof of absent
indexing. The complete historical paper and its experiments were not inspected.

Part II, `DOI:10.2142/biophysics.8.11`, was read as related research, not counted
as another independent experiment supporting this record. Source-named
organisms remain qualified observations pending culture/taxonomy verification.
Protein-resolved mechanisms are deferred, not claimed absent. Bounded
MED/Crossref notice-field and publisher checks do not establish comprehensive
correction/retraction clearance. The
[source verification receipt](../../research/traits/physiology/stalk_contraction-source-verification.json)
retains source locators, hashes, access limits and actual native outcomes.

## Identity And Reservation

Accepted at `2026-10-15T03:51:31Z` on main
`f815ad06c3f6b1d1c3f37e18dc37c8579267d880`. Reserve `traitmech:000730`,
`metpo_traitmech_v606`, and all **1068300-1068399**; only `METPO:1068300`
is populated. Repeated `METPO:1068200` remains owned by v605's prior block.
Subset: `metpo_traitmech_2026_10`.

The fresh search included ignored and hidden files in 153 registered or known
locations, 152 retained heads, 25,115 TraitMech and 6,855 CommunityMech regular
blobs, with positive regex controls. Its catalogue was stable and rechecked at
acceptance. The earlier broader 200-location scan remains dated evidence,
not a claim that every unregistered copy was freshly reread. All 1,523 refreshed
biological matched lines were already in that prior inventory; canonical
identity and proposal assessments remain applicable. Nine unique
contraction-related research/cache contexts were inspected separately: prior
source leads, distinct endpoint boundaries and the parent's follow-up, not
another exact trait. The Amos citation was included in the refresh.

Remote checks covered 13 open/draft PRs: TraitMech #1938, #1937, #1936, #973
and draft #924; CommunityMech #2011 and draft #935; METPO #644, #643, #641,
#640, #638 and #629. All 806 nonremoved changed-file blobs and 587 selected
upstream owners were screened. All 25 matched owners retained identical bytes
and contexts to the previously assessed set. Main, PR heads/descriptions/draft
states and selected upstream heads were rechecked at acceptance.

The numeric `1068386.556` is a supplement data value in CommunityMech cache
copies, and `-2.1068373` is an embedding component in draft #924, not a term
reservation. Full-content range inspection, including wrapped ranges and gzip
decoding, covered 30,818 owner contexts and 2,596 unique contents. Its only
overlapping intervals were the general `1000000-1999999` editor envelope.

RDF assessment of pinned/current METPO and the editor found only the historical
`METPO:1000288`, **obsolete stalk**, for the stalk lexical match. It is
deprecated, under ObsoleteClass, with OMO:0001000 as its recorded reason and no
replacement/consider annotation observed. This morphology term is not an active
exact contraction class, is not revived, and is not an exact xref. The reason
code alone does not invalidate the biology. The editor is an import stub, not a
complete imported closure; the released ontology was checked separately.

Checks are bounded, not an atomic reservation or exhaustive literature search.
Lost untracked/ignored history, symlink targets, arbitrary archives and unchanged
PR files were not reconstructed. Refresh reservations before publication.

## Verification And Upstream Path

The template preserves canonical 11-column headers checked against the captured
KG-Microbe template at `1acb8b61fcae24fafc0640b1bf6e5be669f315f9`.
Run the maintained verifier and ROBOT/ELK wrapper, then parse emitted RDF for
the actual `https://w3id.org/metpo/` IRIs, the child axiom, the copied parent
label/definition/phenotype parent and definition-source annotations. These
instructions do not assert that unrun gates passed.

After review, submit the child and its existing parent dependency to METPO.
These placeholders are not released IDs. On upstream acceptance and release,
separately review scope, update the pin, re-seed and migrate the local identifier
while preserving its old spelling for traceability. No upstream PR or human
scientific sign-off is implied here.
