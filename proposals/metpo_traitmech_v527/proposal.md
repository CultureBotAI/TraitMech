# Hormogonium Formation: METPO Proposal v527

## Context

Add `traitmech:000651 hormogonium formation`, a PROPOSED MORPHOLOGY
class on base `8459cfcb63c44af78f04e7d6e7709187fa1bc9e6`. It denotes a
cyanobacterial developmental phenotype, not a gene, protein or material entity.

Ignored-and-hidden whole-repository searches covered terminology, source
DOI/PMID bundles, prospective identifiers and proposal names. The only
hormogonium mentions were an explicit exclusion from the heterocyst concept
in its research report and rendered copy. No exact record or unresolved
same-scope node was found. Those exclusion statements remain correct.

The fresh seed contains 399 records, 344 shared with the pre-addition
1,045-record corpus. The 55 absent seed identifiers comprise 38 supporting
fields and 17 reviewed duplicates; all 38 formerly unselected classes are
now live. Structured review covered 1,546 release-delta rows, 153 active-review
rows and the 12,617-triple ontology. No exact candidate or reserved-block
collision was found. This is a novelty check, not an exhaustion claim.

All-state GitHub searches in TraitMech and upstream METPO returned no indexed
candidate or identifier reservation. Local CommunityMech proposals were also
searched including ignored and hidden files. Search-index absence is not proof
that a discussion never occurred.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The endpoint is differentiation of short, initially heterocyst-free filaments
distinct from mature vegetative trichomes. Random breakage alone does not
establish this developmental stage. Motile `METPO:1000702` is not a necessary
parent: the 1979 study explicitly includes immotile hormogonia, and the 2019
sigF deletion separates morphological differentiation from locomotion. The
1989 abstract's motile description is specific to the studied Nostoc cultures.
Smaller cell size, gas vacuoles, permanent heterocyst absence, plant symbiosis
and nitrogen fixation are not universal defining requirements.

Filament shaped `METPO:1000674` concerns cell shape, and filamentous colony
`METPO:1007066` concerns colony outline. Neither captures this developmental
filament stage. Heterocyst `traitmech:000073` and akinete `traitmech:000185`
describe other differentiated cell types; these phenotypes can occur in one
life cycle, so organism-level disjointness is not asserted. Keep the phenotype
parent pending human hierarchy review. No exact xref, synonym or SSSOM mapping
is asserted. No existing record requires reparenting or node repair.

## Evidence and Limits

| DOI | Role |
| --- | --- |
| 10.1099/00221287-111-1-1 | Developmental stages and immotile forms |
| 10.1128/aem.55.1.125-131.1989 | Induced Nostoc morphology; PMID:16347816, PMC184065 |
| 10.1128/mSphere.00231-19 | Definition and genetic separation of development/motility; PMID:31043519, PMC6495340 |

The 1979 snippet was directly read in the publisher PDF's extracted text,
Genera of Section IV, printed page 35; surrounding pages 34-36 distinguish
development from fragmentation and describe later heterocyst formation.
Screenshots were unavailable and the direct download returned HTTP 403;
no visual figure or numerical table verification is claimed.

The 1989 scientific abstract was directly read on PubMed and through the
Europe PMC core API. Full text and panels were not read. The 2019 scientific
ABSTRACT, first Results subsection, and first two Methods subsections were
directly read in Europe PMC XML. Its snippet is a Results conclusion, not
the separately labeled precis/IMPORTANCE text. Actual figures, movies and
strain-table supplements were not inspected. Search-result text is not used
as verified snippet evidence.

No causal graph or canonical example is asserted. Two OPEN discussions retain
scope/mapping and strain/protein grounding tasks. Genetic dependence is known;
accession-resolved edges and taxon anchors require further inspection, not an
inference from homologous genes or transcript changes alone. Observed transient
stages remain valid evidence without an unqualified canonical taxon row.

## ID Space and Files

Reserve fresh block 1060400-1060499, using `METPO:1060400`, after v526's
1060300 block. Local ID: `traitmech:000651`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

The upstream contract remains pinned to
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
The skill and canonical 11/13-column template blobs were rehash-verified
against that unchanged current commit. The writer guards the reviewed parent
projection and existing target/template content, prevalidates, and defaults
to dry run. The new record's curation event identifies codex as its curator.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

Writer dry run, direct LinkML/strict validation, history/products, 20 writer
tests and 45 artifact-focused tests passed. Proposal verification/coverage and
ROBOT ELK passed. Parsed RDF contains 15 class-template, 12,628 merged and
12,632 reasoned triples, with real w3id phenotype/quality ancestry and no
legacy METPO stubs. Both template headers and the row have 11 columns.

The online snippet resolver returned 1989 VERIFIED, 2019 NOT_IN_ABSTRACT,
and 1979 UNRESOLVED. The 2019 quote exact-matches the directly read Results;
the 1979 quote was checked against directly retrieved publisher PDF text.
An independent exact quoted-DOI API query also returned zero hits for 1979;
that does not invalidate the publisher record or establish a universal absence
from indexing. No manual source check is relabeled as a resolver success.

The corpus has 1,046 records and 594 discussions. All 1,045 prior YAML files,
531 historical proposal templates/narratives and discussion templates remain
unchanged. Of the old trait pages, 1,044 change only in their footer;
phenotype gains the child and changes from 146 to 147 children. That child
count is also the only existing priority-row change. The shared generator
matches all 139 source blobs of reviewed claw commit
`6d0a6fbbaeec47f42c6f999233b460e3f56bae89`. Both configured embedding inputs
are absent, so embedding regeneration is not claimed.

Desktop/mobile browser checks at 1440/390 px passed identity, provenance,
three quotes, source limits, parent navigation, dashboard counts and image
loading with no overflow or page errors; screenshots were visually inspected.
No canonical or protein examples were changed. `just qc`, Ruff and the full
2,850-test suite passed; the suite reported two dependency deprecation warnings.
The ordinary staged whitespace check flags only the three required trailing
empty ROBOT directive cells. Both exact-path scoped checks passed without
weakening global Git settings. The committed-history gate, exact-head review,
remote-byte verification and actual CI/merge outcomes will be recorded on the
PR, not preclaimed here.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed. After acceptance, refresh the ontology, migrate
the local identifier and references to the accepted METPO ID, preserve the
local identifier's traceability and append-only history, and regenerate
products without creating a duplicate. Scientific discussions remain open
until their own evidence and grounding tasks are resolved.

## Change Log

- v527, 2026-10-06: propose hormogonium formation with developmental-stage,
  motility and sequence-inference boundaries.
