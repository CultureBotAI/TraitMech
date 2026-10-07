# Autophagic Glycogen Degradation: METPO Proposal v523

## Context

Add `traitmech:000647 autophagic glycogen degradation`, a PROPOSED
PHYSIOLOGY class, on base `b2a07ae9c54be1428a4d5f34fd8f56c12244795f`.
The explicit endpoint is autophagic breakdown of intracellular glycogen,
not glycogen granule possession, growth on glycogen, extracellular
amylolysis, a reporter, or a sequence-feature inventory.

Ignored-and-hidden whole-repository searches covered labels, likely slugs,
glycophagy, multiline glycogen/autophagy wording, all four DOI/PMID bundles,
PMC accessions, GO:0061723 and prospective IDs. No exact record, prior local
proposal or allocation was found. A fresh 399-record seed shares 344 IDs
with the 1,041-record corpus. Its 55 absent terms comprise 38 supporting-
field terms and 17 reviewed duplicates. All 38 formerly unselected classes
are now live. Structured scans covered all 1,546 release-delta rows, 153
active-review rows and the 12,617-triple pinned METPO graph, with no
candidate/block hit. This establishes candidate novelty, not discovery
exhaustion.

All-state GitHub searches returned no indexed TraitMech glycogen item,
METPO glycophagy item or METPO:1060000 reservation. The broader upstream
glycogen search found [METPO #269](https://github.com/berkeleybop/metpo/issues/269),
which was read in full: it concerns cellular inclusions, not autophagic
degradation, and has no comments or matching allocation. The known #1758
landing comment was read separately; it records this research lead without
allocating an ID. Index silence is not treated as proof against that comment.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Cargo identity narrows the existing degradative autophagy phenotype. This is
an intracellular recycling phenotype, not a parametric organism-to-external-
substrate use relation. Existing autophagy children describe different cargo.
No universal receptor, enzyme, trigger, selectivity or macroautophagic route
is imposed. The parent definition remains unchanged.

The source terminology is not uniform. The Cells paper introduces glycophagy
as selective but concludes that its K. phaffii observations are nonselective.
The iScience paper uses glycophagy for vacuolar preservation during
sporulation. Those broader or differently qualified usages are not flattened
into exact synonyms. The label here explicitly retains the degradative
endpoint supported by the fungal Sga1 paper and the K. phaffii studies.
Broader delivery/storage and selective subtype relationships remain open;
this record does not claim to exhaust all glycophagy biology.

[GO:0061723](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061723)
was directly resolved as nonobsolete biological-process glycophagy, with
selective degradation and macroautophagy qualifiers. It is neither an exact
phenotype mapping nor an authority for imposing those qualifiers on every
microbial observation. No exact xref, synonym or SSSOM alignment is asserted.

## Evidence and Limits

| DOI | PMID | Role |
| --- | --- | --- |
| 10.4161/auto.6.4.11736 | 20383057 | Definition: autophagy/Sga1-associated vacuolar glycogen breakdown |
| 10.3390/cells13060467 | 38534311 | Nitrogen-starved K. phaffii reporter evidence; PMC10969688 |
| 10.3390/ijms252111772 | 39519320 | Follow-up Gsy1/CBM20 reporter study; PMC11546884 |
| 10.1016/j.isci.2024.109810 | 38832010 | Storage boundary and conditional Atg45 mechanism; PMC11145338 |

The first three snippets are exact scientific-abstract spans from directly
retrieved DOI-matched Europe PMC metadata. The fourth is an exact Results
sec2.7 span from the iScience full-text XML, not its scientific Summary,
graphical abstract, highlights or teaser. The two K. phaffii studies are
distinct publications from the same research group, not independent-lab
replication. The Atg45 storage observation is boundary evidence, not a
positive completed-degradation exemplar.

Keep reporter proteolysis, polymer hydrolysis, localization and total glycogen
content distinct. K. phaffii conclusions use matched binding/nonbinding and
cytosolic controls, not Atg11 independence alone. Extraction bias and early
autophagy-independent dot disappearance remain explicit. Human domains used
as reporters and exogenous assay enzymes do not establish corresponding
native microbial mechanisms or exemplars. Actual panels, supplements and
independent strain provenance remain uninspected. No canonical examples or
protein-level graph is added. Two OPEN discussions retain these limits.

## Relationship to v522

The TSV copies corrected `METPO:1059100` autophagy context from v522
unchanged. It is dependency context, not another allocation. The writer
guards the full parent semantic preimage and v522 template hash, rejects
target/proposal drift, validates before production writes and defaults to a
nonmutating dry run. It never writes the parent or older template. Tests use
controlled temporary preimages and distinct fixture hashes while retaining
production-guard checks. Historical cohorts remain unchanged.

## ID Space and Files

Reserve `METPO:1060000` in fresh block 1060000-1060099, following v522.
Local identifier: `traitmech:000647`; subset: `metpo_traitmech_2026_10`.
Current upstream contract/templates were retrieved at
`1408e7099d039026d7611c240938d8e177753406`. Canonical class/property headers
have 11/13 columns. CommunityMech v1's three reference files and TraitMech
v1 were read end-to-end. Local, CommunityMech and pinned upstream checks
found no candidate/block collision. METPO IRIs use w3id, not legacy OBO stubs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

Production dry run, direct LinkML/strict validation, history links and schema,
`just validate-history`, `just validate-products`, `just qc`, and Ruff passed.
Focused writer tests: 43 passed. Full pytest: 2,769 passed in 591.87 seconds
with two dependency deprecation warnings. README, priority and QC-dashboard
artifact tests: 45 passed. Existing audit findings remain baselined; no new
blocking findings were introduced.

The maintained snippet resolver returned three VERIFIED and one
NOT_IN_ABSTRACT. The latter is the manually confirmed contiguous Results
sec2.7 full-text span, not a failed or verified abstract match. The offline
canonical-example audit passed for 727 examples in 542 records; live NCBI
resolution was skipped because no example was added or changed.

Proposal verification and ROBOT/ELK passed with no unsatisfiable classes.
RDF parsing counted 25 class-template, 12,638 merged and 12,642 reasoned
triples; the w3id child, unchanged corrected parent, phenotype and quality
hierarchy were inspected. All 527 historical TSVs and historical narratives
remain byte-identical. Both canonical class headers have 11 columns.
The ordinary staged whitespace check flags only the directive header's
three required trailing empty cells; after inspecting that exact line,
scoped checks pass with only blank-at-EOL exempted for that TSV.

The artifact audit confirms all 1,041 prior YAML files and the protected
record are byte-identical. Of prior trait pages, 1,040 change only in their
footer; autophagy also gains the new child link. Its priority child count
changes from eight to nine. Discussion data has 586 discussions across
513 records. Published dashboards and all rendered pages were regenerated;
shared discussion templates remain unchanged. Embeddings were not regenerated:
both configured source paths are absent, and displayed coverage stays 45.8%.

Playwright checks passed at 1,440 and 390 pixels with no horizontal overflow
or page errors. Six screenshots were visually inspected. Local identity,
four snippets, two OPEN discussions, parent navigation and the dashboard
coverage image render correctly. These checks do not replace inspection of
the scientific figures explicitly left unread above.

## Upstream and Round Trip

Submit the child with unchanged corrected parent context and scope notes to
upstream METPO after review. Issue #269 is related structural work, not an
existing proposal for this trait. No new upstream issue has been opened.
After acceptance, refresh the ontology and migrate local identity and parent
references to accepted IDs while preserving local provenance and history;
regenerate products without duplicating the record. Upstream minting does
not resolve the independent scientific discussions.

## Change Log

- v523, 2026-10-06: propose autophagic glycogen degradation with explicit
  delivery/storage, selectivity, reporter and source-access boundaries.
