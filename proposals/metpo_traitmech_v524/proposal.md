# Unconventional Protein Secretion: METPO Proposal v524

## Context

Add `traitmech:000648 unconventional protein secretion`, a PROPOSED
PHYSIOLOGY class, on base `73d5530fa4864f4db6f9d35d38066241b73b050a`.
This is a microbial trafficking phenotype, not a sequence feature,
an extracellular-protein prediction, or a claim about a host cell.

Ignored-and-hidden whole-repository searches covered candidate terminology,
likely slugs, leaderless secretion, secretory autophagy, Golgi bypass,
the DOI/PMID bundles and prospective IDs. No exact record or prior local
proposal was found. Existing Acb1 research concerns membrane fluidity;
PmaA in chemotropism concerns a growth/pH perturbation. Neither is an
unresolved exact secretion-trait node requiring reassignment.

A fresh seed has 399 records, of which 344 IDs occur in the pre-addition
1,042-record corpus. The 55 absent seed terms comprise 38 supporting-field
terms and 17 reviewed duplicates. All 38 formerly unselected classes are
now live. Structured scans covered all 1,546 release-delta rows, 153
active-review rows and the 12,617-triple pinned ontology. No candidate or
new-block hit was found. The secretion and secretion-system ontology
neighbors are deprecated, not exact active parents. These searches establish
candidate novelty, not discovery exhaustion.

All-state GitHub API searches found no indexed exact unconventional-secretion
item or METPO:1060100 reservation in TraitMech or upstream METPO. Historical
upstream [#57](https://github.com/berkeleybop/metpo/issues/57) and
[#67](https://github.com/berkeleybop/metpo/issues/67), including #57's comments,
concern broad label/system modeling, not this trait. The known
[PR #1759 landing receipt](https://github.com/CultureBotAI/TraitMech/pull/1759#issuecomment-6022652364)
records the research lead without an allocation; index silence does not
erase that prior mention.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The definition includes plasma-membrane delivery and extracellular release.
Its differentia is departure from the conventional ER-Golgi-plasma-membrane itinerary, not
one obligatory cargo, trigger or membrane intermediate. It is not an exact
synonym of leaderless secretion, Golgi bypass or secretory autophagy.

The 2022 Aspergillus study explicitly includes membrane cargo within
unconventional protein secretion, whereas the 2016 yeast study describes
an ER-bypassing soluble-cargo route. Both source usages are retained.
Consequently ER entry, COPII participation and signal peptides are not
universally excluded. The 2014 and 2025 CUPS studies prevent imposing
canonical autophagosomes or absence of all Golgi-derived membranes.

Degradative autophagy (`traitmech:000638`) is not a broader parent.
Exocytosis (`traitmech:000637`) classifies fusion-pore discharge rather than
the trafficking itinerary. Their possible overlap is not disjointness.
No existing record is reparented. No exact xrefs, synonyms, SSSOM mappings,
canonical examples or causal graph are asserted; two OPEN discussions
retain the remaining scientific and mapping work.

## Evidence and Limits

| DOI | PMID | Role |
| --- | --- | --- |
| 10.3389/fcell.2022.852028 | 35465316 | Definition scope and membrane delivery; PMC9021693 |
| 10.7554/eLife.16299 | 27115345 | Intact soluble-cargo export assay; PMC4868542 |
| 10.1083/jcb.201407119 | 25512390 | Autophagosome boundary; PMC4274258 |
| 10.1083/jcb.202312120 | 40015244 | Modified-Golgi boundary; PMC11867701 |

All four DOI identities and snippets were checked directly against Europe
PMC full-text XML. Three quotes are scientific-abstract spans, not the
precis, teaser or eLife digest. The Acb1 quote is from Results s2-1, not
the abstract. The maintained resolver's verdict is recorded separately below.

Keep plasma-membrane localization separate from soluble release and
cell-wall/periplasmic recovery separate from detection in culture medium.
The latter requires leakage controls. A missing predicted signal peptide,
ATG dependence or CUPS formation alone does not establish this phenotype.
Qualified experimental observations are not natural canonical exemplars.
Actual panels and supplements remain visually uninspected. The three CUPS
papers share investigators; the Aspergillus work supports another route,
not independent replication of CUPS. Route-specific mechanisms are deferred.

## ID Space and Files

Reserve fresh block 1060100-1060199, using `METPO:1060100`, after v523's
1060000 block. Local ID: `traitmech:000648`.
Subset: `metpo_traitmech_2026_10`. Previous cohorts remain unchanged.

Current upstream contract and template blobs were verified at
`1408e7099d039026d7611c240938d8e177753406`; class/property headers have
11/13 columns. CommunityMech v1 and TraitMech v1 were inspected as worked
examples. Local, CommunityMech and pinned upstream checks found no
candidate/block collision. The writer guards the parent identity/scope
projection, rejects existing target/template drift, prevalidates before
production writes and defaults to dry run. It never writes the parent.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

Focused writer tests: 21 passed, including the #1760 correction preimage.
Production dry run and guarded apply passed. All four snippets matched
contiguous source XML with markup removed and whitespace normalized. The
maintained resolver reports three VERIFIED and one NOT_IN_ABSTRACT; the
latter is the explicitly labeled 2016 Results span, checked in full text.

Direct LinkML, strict corpus validation, `just qc`, history/product validation,
Ruff, proposal coverage and ROBOT ELK validation passed. The complete Python
test-suite result is recorded on the PR when it finishes; it is required
before merge. The emitted RDF has 15 class-template, 12,628 merged and 12,632
reasoned triples, with the expected w3id METPO parent and quality hierarchy.

The corpus contains 1,043 unique records. All 1,042 previous YAMLs, including
the protected record, remain byte-identical. The 1,041 pre-existing non-parent
pages change only in their corpus footers; phenotype gains one child. Existing
priority rows change only phenotype's child count, 143 to 144. All 528
historical templates and narratives remain unchanged. The reviewed shared
generator source is pinned to `6d0a6fbbaeec47f42c6f999233b460e3f56bae89`.

Playwright checks at 1440 and 390 px pass identity, four snippets, two OPEN
discussions, parent navigation, dashboard counts/image, and absence of page
errors or overflow; screenshots were visually inspected. Configured embedding
sources are absent, so embedding artifacts were not rebuilt. The ordinary
staged whitespace check flags only the ROBOT directive header's three required
empty trailing cells; canonical 11-column widths and scoped checks pass.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. The
historical issues above are not an existing proposal for this class; no new
upstream issue has been opened. After acceptance, refresh the ontology and
migrate the local identifier and references to the accepted METPO ID while
preserving local provenance and append-only history. Regenerate products
without duplicating the record. Ontology acceptance does not close the
independent scientific discussions.

## Change Log

- v524, 2026-10-06: propose unconventional protein secretion with explicit
  soluble-export, membrane-delivery, pathway and assay boundaries.
- Review correction #1760: state the conventional itinerary through plasma-membrane
  delivery explicitly, retaining the source's inclusion of post-Golgi alternatives.
