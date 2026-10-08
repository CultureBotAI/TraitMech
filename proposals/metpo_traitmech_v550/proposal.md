# METPO proposal v550: necridium formation

## Context and scope

Lift `traitmech:000674`, a reusable cyanobacterial separation-cell morphology,
as `METPO:1062700`. The local fallback remains `PROPOSED` pending human review.

| Scope | New terms | Parent |
| --- | ---: | --- |
| A: local trait class | 1 | phenotype, METPO:1000059 |
| B: causal predicates | 0 | no graph proposed |
| C: schema enums | 0 | not applicable |

## Hierarchy and scientific boundaries

Use active phenotype below quality (`METPO:1000188`). Hormogonium formation
(`traitmech:000651`) denotes the dispersal filament, not its separation cell.
The 2005 Introduction describes alternative fragmentation routes; neither
trait is made a subclass or exact synonym of the other. Filament-shaped
morphology denotes elongated cell shape, not this multicellular stage.
No existing exact causal node, synonym or parent-gap discussion needs repair.
The class does not require a fixed shape, spacing, cold trigger, adhesion
function, fitness benefit or conserved apoptosis machinery. Generic cell
death and arbitrary trichome breakage are insufficient. Historical
separation-disc terminology remains an open question, not an exact synonym.

Three independent primary papers support the record, each with a short
verbatim evidence snippet:

- [Hernandez-Marine and Roldan 2005](https://doi.org/10.1127/1864-1318/2005/0117-0239):
  definition authority. Published article pages 239-247 were visually read
  in the university thesis reproduction, including the scientific abstract,
  Methods, Results, Discussion and actual Figures 1-4. Cell degeneration and
  fragmentation are observed; an adhesive role for the resulting polysaccharide
  pads is proposed, not a universal causal requirement. The DOI identity was
  checked against Crossref; DOI landing-page access failed, so the thesis
  reproduction is the directly inspected text.
- [Nurnberg et al. 2014](https://doi.org/10.1111/mmi.12506): scientific abstract
  retrieved from DOI-matched Europe PMC PMID:24383541; publisher Results and
  Methods read. Actual Figures 5-6 were inspected in the institutionally
  archived accepted manuscript, with final publisher captions cross-checked.
  The 24-second 5-CFDA observation is not evidence about every molecule or
  permanent exclusion. Supplements were not inspected.
- [Arctic Microcoleus study, 2015](https://doi.org/10.3389/fmicb.2015.00278):
  publisher Methods, Results, caption and actual Figure 2 panels A-I inspected.
  Membrane permeability and CTC reduction distinguish dead necridic cells
  from injured cells and nitrogen-starved but active bleached cells. The cold
  condition is source-specific. Supplements were not inspected.

Canonical example: the naturally isolated study strain Mastigocladus laminosus
SAG 4.84, `NCBITaxon:447715`, qualified to its necridium-forming stage.
Live NCBI efetch confirms the name and **rank strain**; the directly read
[SAG collection record](https://sagdb.uni-goettingen.de/detailedList.php?str_number=4.84)
confirms natural Icelandic thermal-spring origin in 1967. These identity and
provenance checks are not counted as additional phenotype studies. No example
is inferred from mixed biofilms or an unverified Microcoleus strain identity.

No causal graph is proposed. Observed cellular transitions do not establish
protein causality; the 2014 SepJ sequence/localization work cannot substitute
for a necridium-formation perturbation experiment. This is a documented
knowledge gap, not a claim that mechanisms are biologically absent. No new
predicates, xrefs or SSSOM equivalences are asserted.

## ID space and novelty

Reserve the entire **METPO:1062700-1062799** block; only 1062700 is used.
Local ID: **traitmech:000674**. This follows v549/1062600-1062699.
Subset: `metpo_traitmech_2026_10`.

At allocation, main was `a4aec23443bc14ca04fe2fbe5746c7cfb3ef3370`.
Ignored-and-hidden searches covered 19 roots: all 17 then-existing TraitMech
worktrees, the whole CommunityMech checkout, and a complete immutable snapshot
of changed curation artifacts from every open PR, including drafts. Queries
included necridi-/necriti- variants, sacrificial-cell/separation-disc labels,
primary citations, the local ID, cohort and every identifier in the full block.
There were no matching prior traits or proposals. Numeric dependency/cache
hits did not reserve the block. RDF inspection of the 12,617-triple pinned
METPO ontology found no exact term. Hormogonium, heterocyst and akinete context
was checked for semantic duplication. CommunityMech v1 class/property files
and their extensions were read; their reserved ranges do not overlap.

Complete paginated open-head snapshot at allocation:

| PR | Head | Relevant curation reservation |
| --- | --- | --- |
| #1802 | `b2566d960ef630f73ea966015dd583994d826d0a` | existing Shedu trait; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

Publication recheck retained the same main SHA and searched all 20 current
roots, including this new worktree, ignored files and hidden files. The #1802
head changed to `a74d9278b3ce5971d773a4e81616373f795f2816`; its complete
eight-file inventory still contains only the existing Shedu record and its
history as curation artifacts. The other four heads are unchanged. No new
reservation or semantic duplicate was found outside this branch's artifacts.

## Files and verification

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 2 headers + 1 new class |
| proposal.md | this narrative |
| properties / SSSOM | omitted; no new predicates or mappings |

Pinned upstream kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406` has class header blob
`b590cf303dc2fbdd57bed021668641cd0c32396d` (11 columns) and property header
blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (13 columns). The class
headers match exactly, including three empty trailing directive cells.

Proposal verification and ROBOT template/merge/ELK validation passed:

```bash
just verify-proposal metpo_traitmech_v550
just robot-validate-proposal metpo_traitmech_v550
just qc
```

Inspect emitted RDF for the child and phenotype parent under
`https://w3id.org/metpo/`, the parent's label and its quality ancestry.
Keep maintained snippet-resolver results distinct from direct text/figure
inspection. Run live canonical-taxonomy audit, focused writer tests, full
pytest, committed-history checks and generated-page browser inspection.

RDF inspection passed: 15 class-template triples, 12,628 merged triples and
12,632 reasoned triples, with the correct phenotype/quality hierarchy and no
legacy METPO IRI stub. Live taxonomy resolved all 751 examples with zero
errors and 24 existing label warnings. Snippet resolution returned one
`VERIFIED` (2014 abstract), one `NOT_IN_ABSTRACT` (2015 caption), and one
`UNRESOLVED` (2005); the latter two were directly verified at their recorded
source locations without altering the resolver verdicts or baseline.
Desktop/mobile browser checks passed at widths 1440 and 390, including the
three quotes, qualified example, open discussions, history and hierarchy
navigation. Existing embeddings were preserved because both configured
source paths are absent. Full committed-tree QC and pytest remain merge gates.

## Upstream and round trip

Submit this template and narrative to berkeleybop/metpo or the kg-microbe
proposal pipeline after TraitMech review. No separate upstream issue or
released METPO term is claimed. After acceptance, refresh the ontology,
re-seed and migrate the record to the accepted identifier while preserving
the local identifier as traceability metadata and both history trails.
Keep unresolved terminology and mechanism questions open.

## Change log

- v550, 2026-10-08: cyanobacterial necridium formation with bounded primary evidence.
