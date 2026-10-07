# Ballistospore Discharge: METPO Proposal v537

## Context and Novelty

Add `traitmech:000661 ballistospore discharge`, a PROPOSED PHYSIOLOGY
class on base `36b8d109beb6026b231ebf21662e382777a2843f`. This is a
reusable fungal discharge phenotype, not a spore structure, gene, assay
column or organism-level observation.

Whole-repository searches included ignored and hidden files, exact candidate
labels, ballistospore/ballistoconidium/ballistospory variants, Buller's drop,
surface-tension catapult, spore discharge/ejection, source DOIs and proposed
identifiers. No prior exact record, synonym, causal node or proposal was found.
Structured inspection of the 12,617-triple pinned METPO ontology likewise
found no exact label or annotation. CommunityMech proposals were searched
with ignored and hidden files included; no target or reserved-block collision
was found. Two all-state GitHub searches, for ballistospore and ballistospory,
across TraitMech and berkeleybop/metpo returned zero indexed results and
`incomplete_results: false`. Indexed absence is not exhaustive historical proof.

Fresh seeding produced 399 records, of which 344 IDs were in the pre-addition
1,055-record live corpus. The remaining 55 are 38 supporting fields and 17
reviewed duplicates, according to structured review of the 153-row active
review and 1,546-row release-delta tables. All 38 formerly unselected classes
are now live. Seed absence was not treated as proof of novelty. Additional
credible trait leads remain; no global discovery exhaustion is claimed.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The definition identifies forcible discharge by coalescence of Buller's drop
with fluid on the spore surface. It does not generalize to every form of
forcible fungal spore ejection. Pressure-driven ascospore/sporangium ejection,
passive shedding and subsequent transport by wind are different phenomena.

`METPO:1000870 sporulation` and `METPO:1000871 spore forming` concern
endospores in the live records. `traitmech:000657 fungal conidiation` concerns
production of asexual propagules. Ballistospores can be sexual or asexual,
and the 2014 study reports formation without release in a mutant. Neither
production trait is an exact record or an appropriate required parent.
`METPO:1000701 motility` emphasizes independent locomotion, so a closer
dispersal parent remains an explicit review question rather than an assumed
hierarchy. The phenotype parent is an active class beneath `METPO:1000188
quality` in the pinned ontology and live corpus.

No universal discharge speed, range, lens-shaped drop, macroscopic fruiting
body or asexual mode is imposed. Cell names such as ballistospore and
ballistoconidium are not exact phenotype synonyms. No xrefs or SSSOM mappings
are asserted without authority-level equivalence review. Two OPEN discussions
preserve the hierarchy/mapping and mechanism/readout questions.

## Evidence and Example

| Reference | Directly Inspected Evidence |
| --- | --- |
| [10.1371/journal.pone.0004163](https://doi.org/10.1371/journal.pone.0004163) | Stolze-Rybczynski et al. (2009), PMID:19129912, PMC2612744; scientific abstract, Introduction, Results and Discussion, Table 1, Methods and figure captions from publisher HTML and Europe PMC XML |
| [10.1371/journal.pone.0105147](https://doi.org/10.1371/journal.pone.0105147) | Ianiri et al. (2014), PMID:25148260, PMC4141788; scientific abstract, Introduction, strain table, mirror-assay Methods, initial mutant-screen Results and Discussion from directly retrieved XML |
| [10.1242/jeb.029975](https://doi.org/10.1242/jeb.029975) | Noblin, Yang and Dumais (2009), PMID:19684219; scientific abstract directly retrieved from Europe PMC, not full text or figures |

The first paper is the strongest directly inspected identity source. The
independent mechanical study is the strongest mechanism lead, but its full
text was not audited. The three snippets are contiguous verbatim spans of
17, 10 and 16 words. Manual exact comparisons to the retrieved text passed.
The maintained snippet resolver returned **1 VERIFIED, 2 NOT_IN_ABSTRACT**:
the first and second quotations are from their papers' Introductions,
not abstracts. Manual full-text matches do not replace those resolver verdicts.

The 2014 quotation is terminology, not new experimental proof comparing sexual
and asexual forms. The study's initial screen distinguishes 17 formation-defect
mutants from GI277, which retained abundant spores without release. Negative
mirror transfer is a composite readout; the PHS1 formation phenotype does not
identify a universal discharge motor. Actual figures and supplements were not
inspected. The Discussion's stated mutant percentage is not repeated here;
the record uses the directly reported counts, without a prevalence claim.

The canonical example is `NCBITaxon:5005 Sporobolomyces salmonicolor`,
qualified to NPM01. NCBI taxonomy efetch confirms the species ID, rank and
label. Primary Methods identify isolation from a contaminated manufacturing
facility, with the culture supplied by T. Ward according to Acknowledgments.
That passage is direct provenance, not an inference from a wild-type label.
The paper reports spore formation on PDA within 24 h and measured initial
launch speeds from six spores. The reported 1.42 +/- 0.12 m/s is a mean with
s.e.m.; the 0.54 +/- 0.04 mm range is calculated, not directly measured.
Do not transfer these conditions or values to every strain. Publisher figure
retrieval failed; captions, but not actual images, videos or supplements,
were inspected. No numerical physical optimum or dispersal engineering claim
is made.

The physical mechanism has evidence. Graph omission does not mean it is
unknown: full mechanical text/supplements still need inspection, and the
current MECHANISTIC audit demands a protein node and protein example even
for physical coalescence. Do not fabricate a protein motor or call this
physical mechanism NONMECHANISTIC to satisfy that gate. The unread 2017
[asymmetric-coalescence paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5550963/)
is retained only as a research lead after a PMC challenge and two failed
XML requests; it is not counted evidence or a definition authority.

## ID Space and Subset

Reserve `METPO:1061400` in the fresh block `1061400-1061499`; v536 reserved
`1061300-1061399`. The live maximum local ID before this addition was
`traitmech:000660`; v536 was the latest cohort. Ignored-and-hidden searches
found no prior use of the new local ID, cohort or METPO block. This is separate
from CommunityMech v1's `1007100-1007220` and `2007100-2007113` ranges.
Subset: `metpo_traitmech_2026_10`. The local record remains identified by
`traitmech:000661` until upstream acceptance, not by the reserved placeholder.

Pinned kg-microbe default branch `master` resolves to
`1408e7099d039026d7611c240938d8e177753406`. The exact class and property
template headers were retrieved and decoded: 11 and 13 columns, respectively.
Class blob: `b590cf303dc2fbdd57bed021668641cd0c32396d`.
Property blob: `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
This cohort uses the exact 11-column class header, including three trailing
empty directive cells. It adds no property rows. METPO IRIs must use
`https://w3id.org/metpo/`, not legacy purl stubs.

## Files

| Artifact | Rows |
| --- | ---: |
| `metpo_proposal_classes_robot.tsv` | 1 class plus two headers |
| `metpo_proposal_properties_robot.tsv` | Not emitted; no predicates |
| `metpo_proposal_mappings.sssom.tsv` | Not emitted; no asserted equivalences |

The guarded writer, `scripts/add_ballistospore_discharge_trait.py`, defaults
to dry-run and prevalidates through `write_validated_trait`. It checks the
eight-field phenotype parent projection, accepts only the exact initial or
corrected target preimage, refuses template drift, deep-copies its record and
supports idempotent replay. It does not
edit any existing TraitRecord. The per-record event is LLM-assisted. The
append-only CREATE history record is
`history/records/ballistospore_discharge/2026-10-07T084444Z-codex-95a938.yaml`;
its actor is explicitly Codex, model gpt-5, tool codex.

## Verification

Writer dry-run and 20 focused tests passed before application. All three
manual snippet matches and the maintained resolver run completed with the
qualified verdicts above. LinkML and closed-schema corpus validation,
`just qc`, `just validate-history`, `just validate-products`, proposal
verification, ROBOT/ELK and repository-wide Ruff passed. The 45 focused
README, priority and QC-dashboard tests passed. Before the review correction,
full pytest passed 3,062 tests with two warnings. The corrected writer passes
23 focused tests; post-correction QC, full PR CI and merge-queue results will
be recorded on the pull request.

The online canonical-example audit resolved all 738 examples across 553
records, with zero errors and 24 existing label warnings. The new species ID
and label also matched a direct NCBI taxonomy response. History validation
found 1,142 valid records after the correction and zero invalid records. The snippet baseline was
not expanded; the audit found zero new findings. Existing audit warnings
were retained rather than presented as newly resolved.

Structured artifact comparison confirms all 1,055 existing trait YAMLs and
541 historical proposal TSVs are byte-identical. Of the existing trait pages,
1,054 differ only in footer counts; phenotype additionally gains its child
link. The only changed pre-existing priority row is phenotype's child count,
156 to 157. The published corpus has 1,056 records and 718 unchanged graphs.
Discussion templates and protected spore germination are unchanged.

ROBOT output was inspected with an RDF parser: classes, merged and reasoned
graphs contain 15, 12,628 and 12,632 triples, respectively. The label,
definition, source annotation and phenotype-to-quality hierarchy are intact;
ELK found no unsatisfiable class and no legacy METPO purl stubs were introduced.
The shared dashboard generator used the reviewed `6d0a6fb` source snapshot,
with all 139 source blobs rechecked. The coverage PNG regenerated byte-for-byte
unchanged; HTML counts updated. Neither configured embedding input was present,
so no embeddings were regenerated.

Playwright passed at 1440x900 and 390x900: identity, three evidence spans,
qualified example, history attribution/link, parent/child navigation, browse
filter and dashboard image/counts. Screenshots were visually inspected with
no overflow or browser errors. Ordinary staged whitespace checking flags only
the required three trailing tabs in the ROBOT directive row. Both header
widths were checked, and the documented exception was scoped to that exact
TSV; all other staged files pass the ordinary check.

## Adversarial Review Correction

PR #1780 review filed #1781 because the initial Results snippet began with
"is achieved" and lacked its subject. It was exact but not self-contained.
The replacement is a complete 17-word Introduction sentence describing
Buller's drop snapping onto the adjacent spore surface at fusion, matched
directly to the primary XML. Its section locator and a new per-record
`CORRECTED_EVIDENCE_SNIPPET` event preserve the change without rewriting the
original minting event. Three added tests cover history preservation, exact
initial-preimage migration/replay and refusal of unreviewed initial drift.
The existing add-trait skill already prohibits this kind of shortened quote;
no additional skill wording was needed.

Repository history `2026-10-07T091232Z-codex-0bfe38.yaml` records the edit.
Its accidental 21-word count is corrected to 17 by append-only AUDIT record
`2026-10-07T091248Z-codex-168a56.yaml`; the actual quote was unchanged.
Both records identify Codex explicitly and link #1781 and #1780. No definition,
taxon, measurement, parent, proposal-template or other evidence claim changed.

## Upstream Path

After TraitMech review, submit the TSV to berkeleybop/metpo or the kg-microbe
proposal pipeline with this narrative and reserved block. No upstream issue
is substituted for this same-PR proposal. Maintainers must review organismal
disposition versus biological-process scope and the appropriate dispersal
parent before accepting the term.

## Round-Trip Plan

After an upstream release actually mints the accepted term, update the pinned
ontology, seed into a temporary tree and review the exact accepted definition
and hierarchy. Migrate the local identifier only after checking the approved
mapping, preserve `traitmech:000661` as provenance rather than a lexical exact
synonym, reconcile downstream references and append curation history. Then
regenerate pages, reports and proposal coverage and rerun all gates. An
unreleased placeholder must not replace the live local ID prematurely.

## Change Log

- 2026-10-07: v537 proposes ballistospore discharge with three cited snippets,
  an NPM01-qualified yeast example and explicit experimental/readout limits.
- 2026-10-07: #1781 replaces the subjectless snippet with a complete source
  sentence and retains append-only correction provenance.
