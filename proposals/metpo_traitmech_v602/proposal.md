# Fungal Nematode Egg Parasitism

## Proposed Class

`METPO:1067900`: **fungal nematode egg parasitism**. An animal-pathogenic
phenotype in which a fungus infects nematode eggs by penetrating their eggshells
and colonizing their interiors.

Local identifier: `traitmech:000726`, category `ECOLOGY`, status `PROPOSED`.
The fungal bearer, not the nematode, carries this trait. The direct parent is
animal pathogen `METPO:1004002`, below pathogenic to host `METPO:1004000`,
phenotype `METPO:1000059` and quality `METPO:1000188`. The pinned parent's
organism-like definition is clarified as a phenotype in current upstream
METPO. The local parent and pinned ontology remain unchanged. Infection of a
nematode developmental stage does not imply mammalian pathogenicity.

Eggshell penetration and internal colonization distinguish this established
infection strategy from surface attachment, egg-hatching inhibition, killing,
trapping and generic feeding. Xie calls the fungus nematophagous; this source
umbrella is retained, but the operational infection definition does not measure
feeding. Fungal nematophagy `traitmech:000719` requires consumption and also
includes dead prey; it is related, not an asserted parent. Local parasitism
`traitmech:000043` inherits persistent symbiosis, which is not required here.
These classes are not declared disjoint at organism level. Neither obligacy,
exclusive host stage nor universal host range is asserted. Bare egg parasitism
does not specify a fungal actor and is not an exact synonym.

## Evidence And Limits

- **Definition authority:** [Xu et al. 2021](https://doi.org/10.3389/fmicb.2021.617710),
  `PMID:33897634`, `PMCID:PMC8058359`. Own JZD02 infection experiment,
  Methods, actual Figure 1 A-C and Supplementary Table 1 support infection of
  Meloidogyne incognita eggs. The supplement defines infection by penetration
  through an individual egg; the main Methods' sample wording is less precise.
  The printed 30-hour mean is 38%, but replicates 38%, 33% and 33% average
  approximately 34.7%. No quantitative rates or infection threshold are curated.
  The 6-hour control and 42-hour infected transcriptomes differ in time and
  contain mixed stages; expression is not causal protein evidence.
- **Second primary experiment:** [Xie et al. 2016](https://doi.org/10.3389/fmicb.2016.01084),
  `PMID:27486440`, `PMCID:PMC4949223`. Own 36-1 infection experiment and
  actual Figure 5 A-C were inspected, including the infected eggs in panel B.
  Eggs were the only supplied nourishment in the 24-hour comparison, but
  microscopy is not a direct nutrient-flux measurement. RNA-seq replicates
  were pooled. Conserved appressorium-associated genes also occur in fungi
  lacking that structure; homology and expression do not establish the trait
  or a required effector.

Only Xu and the local record annotate the proposal definition. Xie supports
the trait with a second primary experiment, not an extra bibliographic
definition annotation. The nine-word Xu scientific-abstract excerpt directly
matches JATS and the native verifier returns `VERIFIED`. The six-word Xie
Figure 5 caption directly matches JATS; `NOT_IN_ABSTRACT` is retained, not
converted into an abstract match. Record-specific CLI outcomes, source URLs,
byte hashes and access limitations are in the
[verification sidecar](../../research/traits/ecology/fungal_nematode_egg_parasitism-source-verification.json).

Selected Abstract/Methods/Results/Discussion passages, Xu Figure 1 A-C, Xie
Figure 5 A-C and the complete rendered Xu Supplementary Table 1 were inspected.
The supplement came from Europe PMC's supplementaryFiles ZIP. A derived CDN
path returned 404; the direct PMC download returned CAPTCHA HTML, not DOCX.
Other ZIP members and complete experimental raw data were not audited.
Hao 2025 and Lopez-Llorca 2002 remain contextual research leads, not counted
positive evidence. The former has unresolved setup/stage inconsistencies; the
latter was inspected only at abstract level. Exact DOI metadata and bounded
notice searches were checked, not comprehensive correction/retraction clearance.

No canonical taxa, proteins, chemicals, causal graph, exact synonyms or
equivalent xrefs are asserted. Strain names in evidence notes do not establish
canonical taxonomy or strain provenance. No field efficacy or safety follows.

## Novelty And Reservations

Accepted at `2026-10-14T11:46:22Z` on clean main
`75cfd0e0bfbfda8110aaf71a22a14b889951c205`. Searches included ignored and hidden
files in 190 known locations and 143 retained heads, with 23,435 TraitMech and
5,815 CommunityMech unique regular-file blobs. Positive regex controls and
whole-tree comparison passed. All 548 unique matched path/text variants
(8,035 occurrences) were classified. Specific genus/citation matches concerned
acid-environment biomineralization and chromium removal, not egg infection.
Broader cached matches concerned fungal attraction or bacterial egg-hatching
inhibition. Existing maintained records describe feeding, trap morphology,
lethality, paralysis, attraction, repellence or hatching, not this exact
infection strategy. No exact same-scope synonym, graph node or TODO was found
in the inspected maintained matches.

Pinned release: 12,617 triples; current release: 12,649; current editor's
byte-verified ROBOT conversion: 31. None imports other ontologies. Six current
template owners were also screened; the small editor is not a substitute for
release inspection. Historical `METPO:1000227` obsolete parasitism is broader,
deprecated, under ObsoleteClass with reason `OMO:0001000`, without replacement
or consider annotations in the inspected releases. [METPO issue 521](https://github.com/berkeleybop/metpo/issues/521)
disputes mechanically assigned reasons, not permission to revive identifiers.
This historical ID is neither reused nor placed in exact xrefs. Fried-egg
colony is unrelated.

Remote screening covered 11 open/draft PRs, 783 nonremoved changed blobs and
587 selected upstream owners. Included PRs: TraitMech #1782, #1476, #973 and
draft #924; CommunityMech draft #935; METPO #644, #643, #641, #640, #638 and
#629. Exact heads, bodies and states were checked at acceptance and retained
in the sidecar. Upstream heads: CommunityMech
`8df89370be840a4b58a9d8a7407c66c7471a5085`, METPO
`1efc8c73009200b9cb74d125df6a0ea5dc36cb93`, KG-Microbe
`9d84fdf903788423ea0c36104d7fc64e01be52be`.

Reserve `traitmech:000726`, cohort `metpo_traitmech_v602` and the full
`1067900-1067999` block; only `METPO:1067900` is proposed. The two exact numeric
hits were `size = 1067941` in pymongo wheel lockfile metadata in METPO #643/#644,
not identifiers. All 956 overlapping ranges refer to the broad
`1000000-1999999` editor envelope or its documentation. Structured full-content
inspection covered 45,499 owner contexts and 2,565 unique contents, including
wrapped proposal ranges. No conflicting narrower reservation was identified.

These are bounded checks, not atomic allocation or literature exhaustion.
Unavailable ignored/untracked history, symlink targets, submodules and arbitrary
archives cannot be reconstructed by the historical checks. Remote screening
covers changed blobs and selected owners, not every unchanged file. Recheck
live reservations before publication.

## Round Trip

The canonical 11-column class template preserves empty directive cells, uses
`metpo_traitmech_2026_10` and carries the local identifier in `traits_addressed`.
No SSSOM file is needed without equivalent mappings. Run
`just verify-proposal metpo_traitmech_v602` and
`just robot-validate-proposal metpo_traitmech_v602`, then inspect the emitted
definition annotations and real `https://w3id.org/metpo/` parent hierarchy.
After upstream acceptance and release, verify exact identity in a separate
reviewed local-to-METPO migration. This proposal is not a released or
human-reviewed ontology term.

Three OPEN discussions retain hierarchy, historical identity and evidence
limits. Existing add-trait guidance covers these cases; this addition does not
justify a skill edit. All preexisting records, including protected spore
germination, remain outside the change.
