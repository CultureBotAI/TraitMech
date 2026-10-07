# Palmelloid Formation: METPO Proposal v530

## Context and Novelty

Add `traitmech:000654 palmelloid formation`, a PROPOSED MORPHOLOGY class
on base `a44a738c2f196310845b894653339747e8359030`. This is an organismal
growth-form phenotype, not an algal taxon, gene, profile or assay column.

Whole-repository searches included ignored and hidden files, terminology,
likely slugs, source identifiers and reservation blocks. No exact record,
synonym, unresolved causal node or prior proposal was found. An initial broad
numeric search matched an unrelated NumPy test value, not a trait.
CommunityMech proposal searches and all-state TraitMech/upstream METPO GitHub
searches found no candidate or `METPO:1060700` reservation. Search-index
absence does not prove that no historical discussion ever occurred.

Fresh seeding produced 399 records, 344 shared with the pre-addition
1,048-record corpus. The 55 absent identifiers are 38 supporting fields and
17 reviewed duplicates; all 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows,
the 12,617-triple ontology and pinned upstream templates. No exact candidate
or block collision was found. This does not establish trait exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The unqualified term covers nonmotile algal groups formed by mother-wall
retention or adhesion through extracellular gelatinous material. Herron et
al. explicitly documents both senses; the 2022/2023 sources emphasize the
enclosed-cell sense. Preserve those attributions, not an unsupported claim
that all authors use one operational definition. This corrects the initial
narrow draft identified in [issue #1767](https://github.com/CultureBotAI/TraitMech/issues/1767).
The term is not an exact synonym for every microbial aggregate or normal
transient pre-release sporangium. This growth form is not individual cell
shape (`METPO:1000666`) or
macroscopic colony morphology (`METPO:1007062`). Obsolete cell arrangement
`METPO:1000046` and aggregate `METPO:1000011` are not active parents.

Biofilm formation `traitmech:000053` requires surface-attached, matrix-enclosed
communities. Rosette cell arrangement `traitmech:000652` requires inward-facing
cell poles. Neither feature is required for palmelloids.
Capsule and bacterial tetrad/sarcina records also differ in scope. Keep
phenotype as parent pending a broader multicellular morphology review.
Existing records are unchanged. No exact synonym, xref, SSSOM equivalence,
new predicate or organism-level disjointness is asserted.

## Evidence and Example

| DOI | Evidence Role |
| --- | --- |
| [10.1038/s41598-019-39558-8](https://doi.org/10.1038/s41598-019-39558-8) | Both documented senses and the extracellular-material form; PMID:30787483, PMC6382799 |
| [10.3390/ijms24098374](https://doi.org/10.3390/ijms24098374) | Enclosed-cell interpretation and high-light microscopy; PMID:37176080, PMC10179368 |
| [10.3389/fpls.2022.911035](https://doi.org/10.3389/fpls.2022.911035) | Independent morphology and canonical example; PMID:36119589, PMC9470844 |

Three short snippets exact-match retrieved full text, not search results.
The 2019 Discussion explicitly includes retention and extracellular adhesion
and describes palmelloids as nonmotile. Its selected evolved isolates are
not promoted to natural canonical examples. Only that source's terminology
passages are used here; no figure or supplementary-material inspection is
claimed for it. The 17-word added quote supports the extracellular-material
sense, while the other sources retain the enclosed-cell evidence.
The 2023 quote is from Discussion 3.3; Results 2.5, Methods 4.1-4.2 and
actual Figure 10 were inspected. Its percentage uses an area ratio, not
an individual-cell count. Proteomic associations do not establish a causal
protein mechanism or universal necessity for high-light tolerance.

The 2022 quote is from the Introduction. Its scientific abstract, growth
Methods, morphology Results and actual Figure 1 were inspected. The
canonical example is `NCBITaxon:1653778 Chlamydomonas priscui`, the Lake
Bonney isolate at 8 C in salt-supplemented BBM. It has a mixed population,
not an invariant morphology. NCBI efetch directly confirms the species
identifier, rank and current label, with source spelling `C. priscuii` as
a synonym. Neither aflagellate internal cells nor environmental stress is
required universally. The enclosure wording does not assert lipid-membrane
chemistry or a shared cytokinesis defect.

CC-4414 remains qualified evidence, not a canonical example. The
[resource-center entry](https://www.chlamycollection.org/product/cc-4414-wild-type-mt-dn2/)
and 2023 study describe a field isolate, but the directly read
[Flowers et al. primary Results](https://academic.oup.com/plcell/article/27/9/2353/6206349)
raise possible cross-contamination while noting a distinct chromosome-16
segment. This does not prove contamination of the 2023 stock or engineering.
These provenance sources are not counted as independent palmelloid evidence.

Three OPEN discussions retain hierarchy, mechanism and provenance questions.
A causal graph is deferred pending organism-specific perturbation and
accession review; a cell-release mechanism cannot simply be transferred to
extracellular adhesion. Gene possession alone is not phenotype evidence. No fixed
cell-count, stress, flagellar, persistence-duration or photoprotection
requirement is imposed across algae.

## Allocation and Contract

Reserve fresh block 1060700-1060799, using `METPO:1060700`, after v529's
1060600 block. Local identifier: `traitmech:000654`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

The current upstream contract was rechecked at
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
Canonical class/property template blobs match the inspected copies:
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`.
This class-only cohort uses the 11-column header with three required
empty trailing directive cells. No properties or mapping file is needed.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| proposal.md | Reviewer narrative |

The writer defaults to dry run, guards the parent projection and existing
target/template, prevalidates before writing and records LLM-assisted
provenance. Its explicit initial-draft migration accepts only the reviewed
preimage, preserves the first event and appends the scope correction.
Repository history is append-only; the original CREATE record is not rewritten.

## Verification

Corrected-state validation passed: direct LinkML and strict validation,
writer dry run, 24 writer tests, proposal verification and ROBOT/ELK,
`just validate-history`, `just validate-products`, `just qc`, Ruff,
53 artifact-focused tests and the full suite (2,914 passed, two warnings).
The initial broad run was deliberately stopped after the scope defect was
found; only the complete corrected-state run is claimed here.

The online canonical-example audit resolved 731 examples across 546 records
with zero errors and 24 existing label-drift warnings; none concerns the new
example. The maintained snippet resolver reports three `NOT_IN_ABSTRACT`
rows. Each snippet separately exact-matches the retrieved full text (22, 14
and 17 words); this does not change those resolver outcomes.

Parsed class, merged and reasoned OWL contain 15, 12,628 and 12,632 triples.
The parent uses the real w3id METPO namespace and expected quality hierarchy;
no legacy-namespace parent stub is present. ROBOT's physical line counts
(23,322 merged and 23,326 reasoned) are not triple counts.

Artifact comparison confirms all 1,048 existing YAMLs and 534 historical
templates are unchanged. Existing trait pages change only in footer counts,
except phenotype's new child; its priority child count changes 149 to 150.
Historical narratives, shared discussion templates and the protected record
are unchanged. The citation audit counts three sources. All six desktop/mobile
screenshots were inspected, and browser assertions passed at 1440 and 390
pixels without page errors or horizontal overflow.

The add-trait skill validator passed. Neither configured embedding source
path exists, so embedding artifacts were not regenerated. Existing QC
baselines and source-license warnings were not changed or hidden.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new
upstream issue is claimed. After acceptance, refresh the ontology, migrate
the local identifier and references to the accepted METPO identifier,
preserve local-ID traceability and append-only history, and regenerate
without creating a duplicate record. Scientific discussions remain open
until their specific evidence questions are resolved.

## Change Log

- v530, 2026-10-07: propose palmelloid formation with three primary references,
  a qualified Antarctic example and explicit provenance limitations; correct
  the initial enclosed-cell-only scope under issue #1767 before commit.
