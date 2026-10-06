# Endocytosis: METPO Proposal v512

## Context

Add `traitmech:000636 endocytosis`, a PROPOSED PHYSIOLOGY class for a
microbial cell's membrane-bound uptake phenotype. This is neither a
sequence feature nor induction of uptake by a host cell. Base:
`731dfb55bcfcd20220383fb5923ad06d20ee57e9`.

Ignored-and-hidden searches across TraitMech and CommunityMech proposals
covered endocytosis/endocytic/endocytotic, the source identifiers, local
ID, cohort and prospective METPO block. Existing uptake-trait contrasts,
pinocytosis's parent gap, source-attributed myzocytosis terminology and
raw Biolink process terminology are not an exact primary record. No
exact record or ID reservation was found. All-state GitHub issue/PR
searches in TraitMech and METPO returned no endocytosis result.

A fresh 399-record seed shares 344 identifiers with the 1,030-record
pre-addition corpus. Its 55 absent IDs reconcile to 38 supporting-field
terms and 17 reviewed duplicates. The complete 1,546-row release delta
and 153-row active review were parsed; all 38 formerly unselected
classes are live. All 12,617 pinned METPO triples were searched for
endocytosis variants and the prospective block, without a match.
This is a local novelty audit, not evidence of literature exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The defining boundary is internalization into membrane-bound compartments
through plasma-membrane remodeling. Surface adsorption, membrane-transporter
entry, passive diffusion, open invaginations, autophagy and intracellular
trafficking alone do not establish this phenotype. No fixed size, rate,
clathrin/actin dependence, nutrition or degradation is required. No synonyms,
process-level equivalence, molecular accessions or causal graph are asserted.

Existing pinocytosis `traitmech:000635` and phagocytosis `traitmech:000627`
definitions entail this broader scope. Both receive the new direct parent.
Pinocytosis's temporary parent gap is resolved with its historical rationale
preserved; its separate taxonomy and mechanism discussions remain OPEN.
Phagocytosis's scope discussion remains OPEN for process-mapping review;
only its broader-parent sentence changes. Both definitions, evidence,
examples and previous history remain unchanged. Macropinocytosis
`traitmech:000634` remains below pinocytosis, gaining a transitive ancestor.
These are definition-based hierarchy inferences, not new child experiments.

Myzocytosis `traitmech:000631` and trogocytosis `traitmech:000633` retain
their current parents. Their aspiration/partial-cell-uptake definitions
do not universally specify the enclosure required by this operational
endocytosis definition. The myzocytosis record cites the 2023 Discussion
of `DOI:10.3390/microorganisms11081945`, which uses endocytosis as an
umbrella for the studied Colpodella feeding mode. That attributed usage
is retained explicitly, not silently contradicted or generalized into
universal subtyping. These decisions do not assert exclusion or
organismal disjointness. Nutritional phagotrophy is not an equivalent.

**Additional upstream axioms on adoption:**

- `METPO:1058800 SubClassOf METPO:1058900` (pinocytosis, v511).
- `METPO:1058000 SubClassOf METPO:1058900` (phagocytosis, v503).

The historical phenotype superclass axioms remain true. Preserve those
cohorts and do not re-emit their IDs in the new reservation template.
Following v447/v449/v511, these refinements are explicit upstream curation
requests, not axioms emitted by the v512-only ROBOT template.

## Evidence and Limits

- `DOI:10.1083/jcb.128.5.779`, `PMID:7533169`, `PMC2120394`:
  Vida and Emr (1995), definition authority. A 19-word scientific Abstract
  span was checked directly. Introduction, Methods, Results and Discussion
  were read in Europe PMC full-text OCR:
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2120394/fullTextXML.
  FM 4-64 reports membrane transport. Early BHY10.5 reporter experiments
  must not be attributed to later SEY6210 controls. Endosome identity is
  qualified; late transport and initial uptake are distinct readouts.
  The PDF/figures were unavailable and were not visually audited.
- `DOI:10.1128/mcb.14.11.7245-7255.1994`, `PMID:7935439`, `PMC359259`:
  Schandel and Jenness (1994), independent experimental study. A 12-word
  scientific Abstract span was checked in NCBI PubMed XML and Europe PMC
  metadata, which agree on this canonical DOI. Fractionation and protease
  protection support receptor internalization, distinct from signaling
  and degradation. Full text and figures were unavailable: Europe PMC's
  full-text endpoint returned HTTP 500; the indexed PDF mirror returned
  404. No unread strain identity or assay detail is inferred.
  https://pubmed.ncbi.nlm.nih.gov/7935439/

Both studies concern laboratory Saccharomyces cerevisiae, not independent
taxon replication. Canonical examples are deliberately unset pending
strain-provenance review; a reporter background is not a wild isolate.
Neither marker kinetics nor an abstract establishes a universal molecular
mechanism. The record retains an OPEN exemplar/mechanism gap and a separate
OPEN scope/mapping discussion. The two-citation gate is not relaxed.

## ID Space and Files

Reserve `METPO:1058900` in the free 1058900-1058999 block, following
v511's 1058800 block. Local identifier: `traitmech:000636`; subset:
`metpo_traitmech_2026_10`. CommunityMech proposals do not overlap.
The Knowledge-Graph-Hub/kg-microbe contract and headers were read at
`1408e7099d039026d7611c240938d8e177753406`. Use its 11-column class
template and the pinned ontology's w3id namespace, not the legacy purl
example. Its 13-column property template does not affect this class-only
cohort. Definition provenance cites the local codex minting record and
both experimental DOIs; header rows retain all 11 cells.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded dry run and 40 focused tests passed before application.
Tests cover biological scope, source limitations, child preservation,
controlled historical preimages, dry-run immutability, exact replay,
all-record prevalidation and drift refusal. All three changed records
receive curation events and separate append-only repository histories.
Broader gates and exact-head CI outcomes will be recorded in the PR
receipt; no unrun check is claimed passed here.

- Direct LinkML and strict checks pass for all three records; strict
  corpus validation reports zero errors across 1,031 records. Both
  snippets return `VERIFIED`, similarity 1.00, and were separately
  confirmed as scientific-abstract spans.
- Proposal verification and ROBOT/ELK pass with no UNSAT. Parsed RDF
  contains 15 triples in classes.owl, 12,628 in merged.owl and 12,632 in
  reasoned.owl. The w3id class points to labeled phenotype and its quality
  ancestor; no legacy purl METPO stub is emitted. All 636 local IDs have
  proposal coverage; all 516 PROPOSED records meet the citation gate.
- Maintained generators produce 1,031 trait pages, 564 discussions across
  502 records, and a 1,031-record QC dashboard with no failing slots.
  All 139 reviewed claw source files match their archive. Shared browser
  and dashboard navigation/accessibility templates are unchanged.
- Semantic comparison preserves both children's definitions, evidence,
  examples, other discussions and prior history. All 1,027 non-coupled
  existing trait pages change only in footers. The phenotype priority row
  changes from 142 to 141 direct children; endocytosis has two. Historical
  v503/v511 proposals and protected spore-germination YAML are unchanged.
- Chromium checks at 1440 and 390 pixels pass identity/provenance, quotes,
  child discussion states, hierarchy round trips, dashboard counts and
  image loading, without overflow or page errors. Screenshots were
  inspected. Both configured embedding source paths are absent, so
  embedding artifacts were not regenerated.
- The complete local pipeline exits zero: `just qc`, history/product
  validation, Ruff and all 2,420 tests pass (837.79 seconds; two dependency
  deprecation warnings). Existing graph and snippet findings remain fully
  baselined, with no new or blocking findings. Exact-head CI results are
  recorded separately in the PR.
- Ordinary staged whitespace checking flags only the ROBOT directive
  row's three required trailing tabs. All rows have 11 cells; normal
  checks elsewhere and the documented exact-TSV exception pass.

## Upstream and Round Trip

Submit the cohort and both child axioms for METPO review after TraitMech
signoff. After acceptance, refresh the pinned ontology, migrate the local
identifier and references to the accepted ID, preserve the local minting
provenance and append-only history, and regenerate without introducing a
duplicate primary record. PROPOSED status awaits human curator signoff;
the named scope and exemplar/mechanism discussions remain OPEN.

## Change Log

- v512, 2026-10-06: propose endocytosis with two DOI-backed snippets and
  refine pinocytosis/phagocytosis parents while retaining evidence limits.
