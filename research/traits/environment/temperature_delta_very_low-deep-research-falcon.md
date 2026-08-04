---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:38:36.654781'
end_time: '2026-08-04T03:47:13.166075'
duration_seconds: 516.51
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta very low
  trait_identifier: METPO:1000483
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth of approximately 1\u20135 \xB0C, characteristic of stenothermal physiology."
  parent_traits: METPO:1000303
  synonyms: Td_1_5
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports very narrow thermal-tolerance breadths
    as the stenothermal phenotype with limited membrane-remodeling flexibility.)'
  causal_graph_summary: 'temperature_delta_very_low_stenothermal: 9 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000483
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 1–5 °C, characteristic of stenothermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_1_5
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very narrow thermal-tolerance breadths as the stenothermal phenotype with limited membrane-remodeling flexibility.)
- **Existing causal graph summary:** temperature_delta_very_low_stenothermal: 9 nodes, 6 edges

## Research Objective

Research the microbial trait **temperature delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_very_low.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000483
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 1–5 °C, characteristic of stenothermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_1_5
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very narrow thermal-tolerance breadths as the stenothermal phenotype with limited membrane-remodeling flexibility.)
- **Existing causal graph summary:** temperature_delta_very_low_stenothermal: 9 nodes, 6 edges

## Research Objective

Research the microbial trait **temperature delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_very_low.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


# Curation report: temperature delta very low

## 1. Scope summary

**Target:** `METPO:1000483` — **temperature delta very low** (`Td_1_5`), an environmental class under `METPO:1000303`.

The trait should represent an **assay-observed growth-temperature breadth of approximately 1–5 °C**: the difference between the lowest and highest temperatures supporting a defined amount of microbial growth under otherwise fixed conditions. It is therefore a phenotype of **very narrow thermal tolerance (stenothermy)**, not a temperature preference or optimum. Thermal tolerance itself is commonly defined as “the temperature range within which a species can grow.” (he2023highspeciationrate pages 1-2)

A defensible measurement should estimate the width of a thermal-performance curve using sufficiently dense temperature intervals. Herren and Baym emphasize that niche breadth can be expressed through the width or area of that curve and that no single metric is appropriate for every population. (herren2022decreasedthermalniche pages 8-9)

### Boundaries and exclusions

Do **not** equate `METPO:1000483` with:

- **Psychrophily or thermophily:** these classify the location of the optimum or limits, not breadth. Psychrophiles can be broad or narrow thermal generalists.
- **Growth at one temperature:** occurrence at a single temperature does not establish a 1–5 °C interval.
- **Cold survival, persistence, or metabolic activity:** viability without population growth is a different endpoint.
- **A narrow realized environmental distribution:** environmental detection can reflect dispersal, nutrients, pH, pressure, competition, or sampling resolution rather than intrinsic growth limits.
- **Acute heat/cold tolerance:** short-term survival thresholds are not equivalent to sustained growth boundaries.

Assay annotations should include strain, medium, atmosphere, pH, salinity, pressure, inoculum, temperature spacing, incubation duration, growth threshold, and biological replication. Incubation time is especially important: *Exiguobacterium chiriqhucha* RW2 required 10 days to score growth at 4 °C, whereas most other temperatures were scored after two days. (white2019thecompletegenome pages 9-10)

No retrieved study directly demonstrated that a particular gene or lipid perturbation creates the exact **1–5 °C** breadth specified by `METPO:1000483`. Consequently, the strongest available graph is a mechanistic scaffold around determinants of thermal breadth, with explicit uncertainty on the final links to the target trait.

## 2. Current understanding and recent developments

The most mature mechanism concerns **membrane homeoviscous adaptation**. Cooling increases lipid ordering, reduces membrane fluidity and permeability, slows diffusion, and impairs embedded proteins. Cells counter this by changing lipid composition—especially increasing cis-unsaturated, short-chain, or selected branched fatty acids—to lower the gel–liquid-crystalline transition temperature and preserve a functional membrane. (collins2019psychrophiliclifestylesmechanisms pages 5-8, siliakus2017adaptationsofarchaeal pages 3-5)

However, these mechanisms normally support thermal accommodation and thus plausibly **broaden**, rather than define, tolerance. The hypothesis relevant to stenothermy is that restricted remodeling capacity causes membrane function to fail after only a small temperature shift. That final inference is biologically coherent but has not been directly tested against a 1–5 °C microbial growth breadth in the retrieved evidence.

Recent work strengthens the ecological and trade-off context rather than identifying a universal stenothermy gene. A 2023 hot-spring survey spanning 54.8–80 °C classified 26,070 OTUs as temperature-sensitive—detected at one sampled temperature—and 524 as temperature-resistant—detected at five or more temperatures. Temperature-sensitive taxa were much less abundant, while community niche breadth narrowed with increasing temperature. These are community-distribution data, not intrinsic 1–5 °C growth assays. (he2023highspeciationrate pages 4-8, he2023highspeciationrate pages 1-2)

A 2024 synthesis emphasizes that microbial growth, adaptability, and survival compete for finite physiological and proteome resources. This supports trade-off models for specialization but does not identify a causal module specific to very-low thermal delta. (zhu2024shapingofmicrobial pages 1-2)

A 2023 genome/proteome/metabolome study of the snow-blight fungus *Phacidium infestans* found antifreeze proteins, trehalose-synthesis enzymes, desaturases, very-long-chain fatty-acid elongation proteins, and stress-response proteins during investigation of freezing-temperature adaptation. The fungus can grow as low as −5 °C, and metabolites differed between −3 and 22 °C. These results identify candidates, but the work did not perturb them or establish narrow thermal breadth. (zerouki2023wholegenomesequenceand pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and assay nodes

- `METPO:1000483` — temperature delta very low.
- Growth-supporting temperature breadth — label-only assay-derived quantity.
- Lower growth-temperature limit — label-only.
- Upper growth-temperature limit — label-only.
- Thermal-performance curve width/area — label-only.
- Stenothermal physiology — label-only; use as a descriptive synonym unless a verified ontology mapping is available.
- Temperature fluctuation periodicity — label-only experimental factor.
- Historical/selective temperature — label-only experimental factor.

### Environmental and experimental factors

- Environmental temperature — candidate `ENVO:01000207` only after ontology verification in the curation environment; otherwise label-only.
- Low-temperature exposure — label-only.
- High-temperature exposure — label-only.
- Constant-temperature habitat — label-only.
- Periodic temperature fluctuation — label-only.
- Random temperature fluctuation — label-only.
- Chloramphenicol exposure — `CHEBI:17698`.
- Freeze–thaw cycling, ice formation, osmotic stress, oxidative stress, hydrostatic pressure, nutrient availability, pH, and salinity — important covariates; add only when measured.

### Cellular structures, properties, and processes

- Cytoplasmic membrane — `GO:0005886`.
- Membrane lipid bilayer — label-only unless a verified ontology term is selected.
- Membrane fluidity — label-only physical property.
- Membrane permeability — label-only physical property.
- Gel-to-liquid-crystalline phase-transition temperature — label-only.
- Homeoviscous adaptation — label-only; no identifier is asserted here.
- Membrane transport, protein folding, translation, cell division, and stress response — candidate biological processes, but use verified GO terms during implementation.

### Lipids and metabolites

- Unsaturated fatty acids — lipid-class node; select a verified CHEBI class during implementation.
- cis-monounsaturated fatty acids.
- Short-chain fatty acids.
- Branched-chain fatty acids, separated into iso- and anteiso forms.
- Cyclopropane fatty acids.
- Cardiolipin, glycolipids, carotenoids, archaeal diether lipids, and tetraether lipids.
- Trehalose — `CHEBI:27082`.
- Glycine betaine — `CHEBI:17750`.
- Choline — `CHEBI:15354`.
- Reactive oxygen species — class-level label unless a specific species is assayed.

### Genes, proteins, enzymes, and systems

These should generally remain **family-level or label-only** until taxon-specific accessions are verified:

- Fatty-acid desaturase.
- Fatty-acid cis/trans isomerase.
- β-ketoacyl-ACP synthases KAS-II and KAS-III.
- Cold-shock proteins/Csp family.
- DnaK/Hsp70 chaperone system.
- Opu and ProU compatible-solute uptake systems.
- Trehalose-biosynthesis enzymes.
- Antifreeze proteins.
- Membrane transporters.
- Archaeal tetraether-lipid biosynthesis/remodeling machinery.

### Taxa useful as evidence contexts

- *Escherichia coli* — `NCBITaxon:562`; strain-level identifiers should be added when verified.
- *Exiguobacterium chiriqhucha* RW2 — retain as a strain label pending NCBI Taxonomy verification.
- *Phacidium infestans* DSM 5139 — retain as a strain label pending verification.
- *Psychromonas ingrahamii*, *Colwellia psychrerythraea*, *Clostridium psychrophilum*, and *Sphingobacterium antarcticus* — useful membrane-adaptation exemplars, but not established instances of `METPO:1000483`.

## 4. Candidate causal edges

| # | Subject — predicate — object | Evidence and supporting snippet | Interpretation and curation status |
|---|---|---|---|
| 1 | low-temperature exposure — **decreases** — membrane fluidity | Collins and Margesin: “Low temperatures adversely affect…[the envelope] by leading to reduced membrane fluidity, permeability and diffusion rates.” DOI: [10.1007/s00253-019-09659-5](https://doi.org/10.1007/s00253-019-09659-5), online 7 February 2019. (collins2019psychrophiliclifestylesmechanisms pages 5-8) | **Core, strong mechanistic edge.** General microbial membrane biophysics; not specific to a stenothermal strain. |
| 2 | decreased membrane fluidity — **impairs** — membrane-protein mobility/function | Same review reports reduced “mobility and function of embedded proteins” under cooling; Siliakus et al. note that many membrane proteins function only in the liquid-crystalline phase. DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x), accepted 29 April 2017. (collins2019psychrophiliclifestylesmechanisms pages 5-8, siliakus2017adaptationsofarchaeal pages 3-5) | **Core mechanistic edge.** Supports a route from cooling to loss of cellular function. |
| 3 | decreased membrane fluidity — **decreases** — nutrient diffusion/transport | Cooling reduces diffusion; some psychrophiles upregulate transport proteins “to counteract the reduced diffusion rates and transport inherent to low temperatures.” (collins2019psychrophiliclifestylesmechanisms pages 5-8) | **Core or contextual edge.** Direction is supported, but consequences for growth breadth need direct testing. |
| 4 | fatty-acid desaturase activity — **increases** — membrane unsaturated-fatty-acid content | Desaturases actively introduce double bonds; cold-adapted organisms show overrepresentation/upregulation of fatty-acid-desaturation genes. (collins2019psychrophiliclifestylesmechanisms pages 5-8, siliakus2017adaptationsofarchaeal pages 3-5) | **Core pathway edge**, but gene/protein grounding must be taxon-specific. |
| 5 | increased cis-unsaturated-fatty-acid content — **decreases** — membrane phase-transition temperature | Unsaturated fatty acids disrupt packing and lower the liquid-to-gel transition temperature. (collins2019psychrophiliclifestylesmechanisms pages 5-8) | **Core, strong physicochemical edge.** |
| 6 | decreased membrane phase-transition temperature — **maintains** — liquid-crystalline membrane at low temperature | The lipid changes maintain “functional fluid bilayers even at low temperatures”; below transition, lipids become ordered and many proteins lose function. (collins2019psychrophiliclifestylesmechanisms pages 5-8, siliakus2017adaptationsofarchaeal pages 3-5) | **Core mechanistic edge.** |
| 7 | homeoviscous lipid remodeling — **maintains** — membrane functionality under temperature change | Homeoviscous adaptation is the active modification of lipid composition to maintain fluidity and membrane function at different temperatures. DOI: [10.1016/j.jmb.2016.08.013](https://doi.org/10.1016/j.jmb.2016.08.013), December 2016; DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x), 2017. (siliakus2017adaptationsofarchaeal pages 1-3, ernst2016homeoviscousadaptationand pages 1-2) | **Core process edge.** |
| 8 | increased short-chain/anteiso-branched fatty acids — **increases** — membrane fluidity at low temperature | Short chains and anteiso branching disturb acyl-chain packing; however, short-chain synthesis requires growing cells and branched-fatty-acid responses are species- and situation-specific. (siliakus2017adaptationsofarchaeal pages 5-7, siliakus2017adaptationsofarchaeal pages 3-5) | **Uncertain/contextual.** Do not encode as universal. |
| 9 | limited homeoviscous-remodeling capacity — **narrows** — growth-supporting temperature breadth | Inference from the preceding membrane mechanism: failure to preserve membrane function should move growth boundaries inward. Reviews distinguish long-term evolutionary range from short-term reversible regulation. (siliakus2017adaptationsofarchaeal pages 1-3, siliakus2017adaptationsofarchaeal pages 3-5) | **Key target edge, but inferred.** Curate only with an `uncertain` or hypothesis qualifier until knockout/remodeling studies measure the complete growth curve. |
| 10 | very narrow growth-supporting temperature breadth — **realizes** — `METPO:1000483` | Supplied trait definition specifies approximately 1–5 °C. Literature recommends performance-curve width/area and defines tolerance as the range supporting growth. (herren2022decreasedthermalniche pages 8-9, he2023highspeciationrate pages 1-2) | **Trait-definition edge**, not a biological causal mechanism. |
| 11 | increasing chloramphenicol resistance — **narrows** — thermal niche breadth | In 24 evolved *E. coli* lineages, resistance had disproportionately negative effects at 32 and 42 °C versus historical 37 °C; the temperature-by-resistance effect was significant, `F(1,974)=13.8`, `p<0.001`. Only 2 evolved cultures exceeded ancestral growth at 42 °C, compared with 41 at 37 °C and 13 at 32 °C. DOI: [10.1038/s41396-022-01235-6](https://doi.org/10.1038/s41396-022-01235-6), published online 14 April 2022. (herren2022decreasedthermalniche pages 3-4) | **Direct but taxon-, drug-, and assay-specific contextual edge.** It demonstrates niche compression, not necessarily a final 1–5 °C breadth. |
| 12 | chloramphenicol resistance — **decreases** — competitive fitness at 42 °C | Sensitive populations reached threefold the population size of the most resistant populations at 42 °C, versus 1.3-fold at 32 or 37 °C; 12/24 lineages had significantly stronger resistance costs at 42 than 37 °C. (herren2022decreasedthermalniche pages 4-5) | **Direct contextual edge.** Useful as an experimentally established route to narrowing. |
| 13 | random alternation between 15 and 43 °C — **favors evolution of** — thermal specialists | Twenty-four *E. coli* populations evolved under alternating 15/43 °C; specialists were favored in the random regime. DOI: [10.3389/fmicb.2021.724982](https://doi.org/10.3389/fmicb.2021.724982), published 22 October 2021. (lambros2021emergingadaptivestrategies pages 1-2) | **Direct experimental-evolution edge**, but regime-specific and not evidence for 1–5 °C breadth. |
| 14 | periodic alternation between 15 and 43 °C — **favors evolution of** — thermal generalists | The same experiment found generalists favored in periodic regimes. (lambros2021emergingadaptivestrategies pages 1-2) | **Direct contextual edge.** Supports environmental predictability as a determinant of breadth. |
| 15 | increasing hot-spring temperature — **filters toward** — narrower realized community niche breadth | Across 54.8–80 °C, Levins’ niche breadth narrowed with temperature; temperature-sensitive OTUs occurred at one temperature and resistant OTUs at ≥5. DOI: [10.1038/s41396-023-01447-4](https://doi.org/10.1038/s41396-023-01447-4), published online 7 June 2023. (he2023highspeciationrate pages 4-8, he2023highspeciationrate pages 1-2) | **Ecological association only.** Do not use as an organism-level causal edge to `METPO:1000483`. |
| 16 | *csp*/*dnaK*, osmolyte systems, and lipid-remodeling capacity — **are associated with** — broad thermal growth | *E. chiriqhucha* RW2 grew from 4–50 °C and encoded predicted cold/heat-shock cascades, choline/betaine systems, and lipid saturation/unsaturation machinery. DOI: [10.3389/fmicb.2018.03189](https://doi.org/10.3389/fmicb.2018.03189), published 8 January 2019. (white2019thecompletegenome pages 1-2) | **Genomic co-occurrence, not causation.** Potential negative evidence for stenothermy; do not encode with a causal predicate. |
| 17 | antifreeze proteins/trehalose enzymes/desaturases — **are associated with** — freezing-temperature adaptation | These candidates were found in *P. infestans*, with laboratory growth reported down to −5 °C and differing metabolites at −3 versus 22 °C. DOI: [10.1007/s00438-023-02073-7](https://doi.org/10.1007/s00438-023-02073-7), published online 10 October 2023. (zerouki2023wholegenomesequenceand pages 1-2) | **Multi-omics association.** Do not curate as causal without perturbation evidence. |

The evidence-readiness summary below separates core mechanisms from contextual or premature assertions.

| Proposed mechanism / edge family | Evidence status | Representative taxon and assay | Curation recommendation |
|---|---|---|---|
| Low temperature exposure → reduced membrane fluidity / permeability and impaired diffusion | Direct causal | Cold-adapted microorganisms; review of membrane biophysics and cell-envelope effects under low temperature, emphasizing reduced fluidity, permeability, diffusion, and membrane-protein mobility (collins2019psychrophiliclifestylesmechanisms pages 5-8, siliakus2017adaptationsofarchaeal pages 3-5) | Core edge |
| Increased fatty-acid unsaturation / desaturase activity → lower bilayer phase-transition temperature and maintenance of functional fluid membranes at low temperature (homeoviscous adaptation) | Direct causal | Psychrophilic/cold-adapted microbes; comparative membrane adaptation literature describing increased unsaturated fatty acids and desaturase-linked remodeling that lowers gel-to-liquid transition temperature (collins2019psychrophiliclifestylesmechanisms pages 5-8, siliakus2017adaptationsofarchaeal pages 3-5, ernst2016homeoviscousadaptationand pages 1-2) | Core edge |
| Homeoviscous adaptation capacity → membrane functionality across changing temperatures | Experimentally supported association | Broad prokaryotic/eukaryotic membrane adaptation reviews; mechanism inferred from repeated temperature-dependent lipid remodeling and maintenance of membrane properties, but not tied to a single stenothermal assay (siliakus2017adaptationsofarchaeal pages 1-3, ernst2016homeoviscousadaptationand pages 1-2) | Contextual edge |
| Chloramphenicol resistance evolution → narrower thermal niche breadth / disproportionate growth loss at novel temperatures | Direct causal | *Escherichia coli* experimental evolution; growth and competition at 32, 37, 42 °C after serial passage to increasing chloramphenicol, with stronger costs at 42 °C and reduced growth away from historical 37 °C (herren2022decreasedthermalniche pages 3-4, herren2022decreasedthermalniche pages 4-5) | Contextual edge |
| Random/fluctuating temperature regime → specialist evolution; periodic fluctuation → generalist evolution | Direct causal | *Escherichia coli* laboratory evolution under alternating 15 and 43 °C; specialists favored in random regime, generalists in periodic regimes (lambros2021emergingadaptivestrategies pages 1-2) | Contextual edge |
| High environmental temperature in hot springs → temperature filtering / narrower realized thermal niche breadth of T-sensitive taxa | Ecological association | Hot-spring communities across 54.8–80 °C; OTU distributions and Levins’ niche breadth showing narrower niche breadth with temperature, but no direct cellular mechanism for an individual trait instance (he2023highspeciationrate pages 4-8, he2023highspeciationrate pages 1-2) | Do not curate yet |
| Presence of cold/heat shock genes (*csp*, *dnaK*) and osmolyte systems (e.g., choline/betaine uptake/biosynthesis) → broad thermal growth range | Genomic co-occurrence | *Exiguobacterium chiriqhucha* RW2 genome plus physiological profiling across 4–50 °C; genes are predicted alongside broad range but not causally perturbed (white2019thecompletegenome pages 1-2, white2019thecompletegenome pages 9-10) | Do not curate yet |
| Antifreeze proteins / trehalose synthesis enzymes / desaturases / stress proteins → growth or persistence at freezing temperatures | Genomic co-occurrence | *Phacidium infestans* grown/assayed at −3 °C and 22 °C with genome/proteome/metabolome integration; adaptive candidates identified without direct functional knockout evidence (zerouki2023wholegenomesequenceand pages 1-2, zerouki2023wholegenomesequenceand pages 6-7) | Do not curate yet |


*Table: This table summarizes which proposed mechanism families for very-low temperature breadth are most ready for TraitMech curation. It distinguishes direct causal evidence from broader associations and genomic co-occurrence so curators can prioritize core versus contextual edges.*

## 5. Recommended initial graph architecture

A conservative first revision of the existing nine-node/six-edge graph should center on the following chain:

1. **Low-temperature deviation** → decreases → **membrane fluidity**.
2. **Decreased membrane fluidity** → impairs → **membrane-protein function and transport**.
3. **Impaired membrane function/transport** → decreases → **growth rate**.
4. **Fatty-acid desaturase activity** → increases → **cis-unsaturated fatty acids**.
5. **cis-unsaturated fatty acids** → decrease → **membrane phase-transition temperature**.
6. **Lower phase-transition temperature** → maintains → **functional liquid-crystalline membrane**.
7. **Homeoviscous-remodeling capacity** → counteracts → **temperature-induced membrane dysfunction**.
8. **Restricted remodeling capacity** → potentially narrows → **growth-supporting temperature breadth** `[uncertain]`.
9. **Growth-supporting breadth of 1–5 °C** → instantiates → `METPO:1000483`.

The chloramphenicol-resistance and temperature-regime edges should be represented as **separate contextual branches**, not merged into a universal membrane mechanism. Hot-spring OTU distributions and cold-adaptation multi-omics belong in evidence notes or a candidate queue rather than the core causal graph.

## 6. Applications and real-world relevance

A reliable narrow-breadth annotation has several applications:

- **Climate and ecosystem vulnerability:** stenothermal microbes should be disproportionately affected by small shifts or increased variability, but this must be inferred from measured growth curves rather than occurrence records. The 2023 hot-spring study illustrates strong temperature filtering and specialist/generalist turnover. (he2023highspeciationrate pages 4-8, he2023highspeciationrate pages 1-2)
- **Antimicrobial-resistance ecology:** the *E. coli* experiment shows that resistance costs can be invisible at the historical temperature yet become large at novel temperatures, affecting predictions of resistance persistence across hosts and environments. (herren2022decreasedthermalniche pages 1-2, herren2022decreasedthermalniche pages 3-4)
- **Bioprocess control and contamination:** a genuinely stenothermal production or spoilage organism may be controlled by small temperature shifts, whereas broad-range organisms such as RW2 cannot. RW2’s measured 4–50 °C range is an instructive eurythermal counterexample. (white2019thecompletegenome pages 1-2)
- **Cold biotechnology:** cold-adapted organisms supply enzymes, cryoprotectants, PUFAs, pigments, and membrane components. Cold-adapted microalgae and fungi are investigated as alternative PUFA sources; *Crypthecodinium cohnii* is used commercially to produce DHA for infant formula. (collins2019psychrophiliclifestylesmechanisms pages 5-8, collins2019psychrophiliclifestylesmechanisms pages 8-10)
- **Plant-pathogen management:** *P. infestans* grows under snow and near/subzero temperatures, motivating work on cold-active fungal metabolism and control of snow blight. This is cold adaptation, not evidence of stenothermal breadth. (zerouki2023wholegenomesequenceand pages 1-2)

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not curate “more unsaturated fatty acids → very-low temperature delta” as a direct universal edge.** Unsaturation preserves function in cold and may broaden tolerance. A direct narrowing effect requires comparative or perturbational growth-curve evidence.
2. **Do not infer limited membrane-remodeling flexibility from a static lipid profile.** Temperature-dependent lipidomics or gene perturbation is required.
3. **Do not use psychrophile, thermophile, or growth optimum as a proxy for breadth.** Several psychrophiles have broad ranges, and broad-range RW2 originated from a nearly constant 4–10 °C habitat. (white2019thecompletegenome pages 1-2)
4. **Do not treat OTU occurrence at one sampled temperature as a 1–5 °C intrinsic growth interval.** The 2023 hot-spring “T-sensitive” category is sampling- and community-dependent. (he2023highspeciationrate pages 4-8)
5. **Do not assign causality to *csp*, *dnaK*, Opu/ProU, antifreeze, trehalose, or desaturase candidates from genome/proteome presence alone.** The cited studies did not perform knockout/rescue experiments tied to thermal breadth. (white2019thecompletegenome pages 1-2, zerouki2023wholegenomesequenceand pages 1-2)
6. **Do not conflate enzyme-temperature optimum with organismal growth range.** The *P. infestans* GH11 xylanase optimum was 45 °C and retained activity at 55 °C despite fungal adaptation to freezing conditions, illustrating that individual-enzyme optima do not delimit whole-organism breadth. (zerouki2023wholegenomesequenceand pages 6-7)
7. **Control incubation time and temperature resolution.** A nominal 1–5 °C breadth cannot be resolved using 5–10 °C temperature steps, and slow cold growth may be falsely scored as no growth.
8. **Treat carotenoids and long-chain PUFAs cautiously.** Their roles can include antioxidant, photoprotective, cryoprotective, or membrane-stabilizing functions; LC-PUFAs may respond to oxidative stress rather than temperature itself. (collins2019psychrophiliclifestylesmechanisms pages 5-8, collins2019psychrophiliclifestylesmechanisms pages 8-10)
9. **Keep bacterial and archaeal lipid mechanisms separate where appropriate.** Archaeal diether/tetraether remodeling is chemically distinct from bacterial fatty-acid remodeling. (siliakus2017adaptationsofarchaeal pages 1-3, siliakus2017adaptationsofarchaeal pages 5-7)

## 8. DOI-first bibliography

1. **He Q. et al.** “High speciation rate of niche specialists in hot springs.” *The ISME Journal* 17, 1303–1314. Published online **7 June 2023**. DOI: [10.1038/s41396-023-01447-4](https://doi.org/10.1038/s41396-023-01447-4). (he2023highspeciationrate pages 1-2)
2. **Zerouki C. et al.** “Whole-genome sequence and mass spectrometry study of the snow blight fungus *Phacidium infestans* … growing at freezing temperatures.” *Molecular Genetics and Genomics* 298, 1449–1466. Published online **10 October 2023**. DOI: [10.1007/s00438-023-02073-7](https://doi.org/10.1007/s00438-023-02073-7). (zerouki2023wholegenomesequenceand pages 1-2)
3. **Zhu M., Dai X.** “Shaping of microbial phenotypes by trade-offs.” *Nature Communications* 15, 4238. Accepted **6 May 2024**. DOI: [10.1038/s41467-024-48591-9](https://doi.org/10.1038/s41467-024-48591-9). (zhu2024shapingofmicrobial pages 1-2)
4. **Herren C.M., Baym M.** “Decreased thermal niche breadth as a trade-off of antibiotic resistance.” *The ISME Journal* 16, 1843–1852. Published online **14 April 2022**. DOI: [10.1038/s41396-022-01235-6](https://doi.org/10.1038/s41396-022-01235-6). (herren2022decreasedthermalniche pages 1-2, herren2022decreasedthermalniche pages 4-5)
5. **Lambros M. et al.** “Emerging Adaptive Strategies Under Temperature Fluctuations in a Laboratory Evolution Experiment of *Escherichia coli*.” *Frontiers in Microbiology* 12:724982. Published **22 October 2021**. DOI: [10.3389/fmicb.2021.724982](https://doi.org/10.3389/fmicb.2021.724982). (lambros2021emergingadaptivestrategies pages 1-2)
6. **Collins T., Margesin R.** “Psychrophilic lifestyles: mechanisms of adaptation and biotechnological tools.” *Applied Microbiology and Biotechnology* 103, 2857–2871. First online **7 February 2019**. DOI: [10.1007/s00253-019-09659-5](https://doi.org/10.1007/s00253-019-09659-5). (collins2019psychrophiliclifestylesmechanisms pages 1-5)
7. **White R.A. III et al.** “The Complete Genome and Physiological Analysis of the Eurythermal Firmicute *Exiguobacterium chiriqhucha* Strain RW2…” *Frontiers in Microbiology* 9:3189. Published **8 January 2019**. DOI: [10.3389/fmicb.2018.03189](https://doi.org/10.3389/fmicb.2018.03189). (white2019thecompletegenome pages 1-2)
8. **Siliakus M.F., van der Oost J., Kengen S.W.M.** “Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure.” *Extremophiles* 21, 651–670. Accepted **29 April 2017**. DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x). (siliakus2017adaptationsofarchaeal pages 1-3)
9. **Ernst R., Ejsing C.S., Antonny B.** “Homeoviscous Adaptation and the Regulation of Membrane Lipids.” *Journal of Molecular Biology* 428, 4776–4791. Published **December 2016**. DOI: [10.1016/j.jmb.2016.08.013](https://doi.org/10.1016/j.jmb.2016.08.013). (ernst2016homeoviscousadaptationand pages 1-2)
10. **Anesi A. et al.** “Comparative Analysis of Membrane Lipids in Psychrophilic and Mesophilic Freshwater Dinoflagellates.” *Frontiers in Plant Science* 7:524. Published **20 April 2016**. DOI: [10.3389/fpls.2016.00524](https://doi.org/10.3389/fpls.2016.00524). The lipid groups correlated with inferred temperature tolerance, but some non-thylakoid lipids tracked phylogeny instead, underscoring confounding. (anesi2016comparativeanalysisof pages 1-2)

## Curation conclusion

The strongest curation-ready subgraph is **temperature → membrane physical state → membrane-dependent function**, with **lipid desaturation/homeoviscous adaptation** as a counteracting module. The final edge from limited remodeling to `METPO:1000483` should remain explicitly **uncertain** because no retrieved perturbation study measured an resulting 1–5 °C growth interval. Chloramphenicol resistance provides unusually strong experimental evidence that thermal breadth can be compressed, but it is a contextual *E. coli* mechanism rather than a universal cause of stenothermy.

References

1. (he2023highspeciationrate pages 1-2): Qing He, Shang Wang, Kai Feng, Sean T Michaletz, Weiguo Hou, Wenhui Zhang, Fangru Li, Yidi Zhang, Danrui Wang, Xi Peng, Xingsheng Yang, and Ye Deng. High speciation rate of niche specialists in hot springs. The ISME Journal, 17:1303-1314, Jun 2023. URL: https://doi.org/10.1038/s41396-023-01447-4, doi:10.1038/s41396-023-01447-4. This article has 71 citations.

2. (herren2022decreasedthermalniche pages 8-9): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

3. (white2019thecompletegenome pages 9-10): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

4. (collins2019psychrophiliclifestylesmechanisms pages 5-8): Tony Collins and Rosa Margesin. Psychrophilic lifestyles: mechanisms of adaptation and biotechnological tools. Applied Microbiology and Biotechnology, 103:2857-2871, Feb 2019. URL: https://doi.org/10.1007/s00253-019-09659-5, doi:10.1007/s00253-019-09659-5. This article has 294 citations and is from a domain leading peer-reviewed journal.

5. (siliakus2017adaptationsofarchaeal pages 3-5): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

6. (he2023highspeciationrate pages 4-8): Qing He, Shang Wang, Kai Feng, Sean T Michaletz, Weiguo Hou, Wenhui Zhang, Fangru Li, Yidi Zhang, Danrui Wang, Xi Peng, Xingsheng Yang, and Ye Deng. High speciation rate of niche specialists in hot springs. The ISME Journal, 17:1303-1314, Jun 2023. URL: https://doi.org/10.1038/s41396-023-01447-4, doi:10.1038/s41396-023-01447-4. This article has 71 citations.

7. (zhu2024shapingofmicrobial pages 1-2): Manlu Zhu and Xiongfeng Dai. Shaping of microbial phenotypes by trade-offs. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48591-9, doi:10.1038/s41467-024-48591-9. This article has 121 citations and is from a highest quality peer-reviewed journal.

8. (zerouki2023wholegenomesequenceand pages 1-2): C. Zerouki, K. Chakraborty, S. Kuittinen, A. Pappinen, and O. Turunen. Whole-genome sequence and mass spectrometry study of the snow blight fungus phacidium infestans (karsten) dsm 5139 growing at freezing temperatures. Molecular Genetics and Genomics, 298:1449-1466, Oct 2023. URL: https://doi.org/10.1007/s00438-023-02073-7, doi:10.1007/s00438-023-02073-7. This article has 10 citations and is from a peer-reviewed journal.

9. (siliakus2017adaptationsofarchaeal pages 1-3): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

10. (ernst2016homeoviscousadaptationand pages 1-2): Robert Ernst, Christer S. Ejsing, and Bruno Antonny. Homeoviscous adaptation and the regulation of membrane lipids. Journal of molecular biology, 428 24 Pt A:4776-4791, Dec 2016. URL: https://doi.org/10.1016/j.jmb.2016.08.013, doi:10.1016/j.jmb.2016.08.013. This article has 614 citations and is from a domain leading peer-reviewed journal.

11. (siliakus2017adaptationsofarchaeal pages 5-7): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

12. (herren2022decreasedthermalniche pages 3-4): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

13. (herren2022decreasedthermalniche pages 4-5): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

14. (lambros2021emergingadaptivestrategies pages 1-2): Maryl Lambros, Ximo Pechuan-Jorge, Daniel Biro, Kenny Ye, and Aviv Bergman. Emerging adaptive strategies under temperature fluctuations in a laboratory evolution experiment of escherichia coli. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.724982, doi:10.3389/fmicb.2021.724982. This article has 34 citations and is from a peer-reviewed journal.

15. (white2019thecompletegenome pages 1-2): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

16. (zerouki2023wholegenomesequenceand pages 6-7): C. Zerouki, K. Chakraborty, S. Kuittinen, A. Pappinen, and O. Turunen. Whole-genome sequence and mass spectrometry study of the snow blight fungus phacidium infestans (karsten) dsm 5139 growing at freezing temperatures. Molecular Genetics and Genomics, 298:1449-1466, Oct 2023. URL: https://doi.org/10.1007/s00438-023-02073-7, doi:10.1007/s00438-023-02073-7. This article has 10 citations and is from a peer-reviewed journal.

17. (herren2022decreasedthermalniche pages 1-2): Cristina M Herren and Michael Baym. Decreased thermal niche breadth as a trade-off of antibiotic resistance. The ISME Journal, 16:1843-1852, Apr 2022. URL: https://doi.org/10.1038/s41396-022-01235-6, doi:10.1038/s41396-022-01235-6. This article has 46 citations.

18. (collins2019psychrophiliclifestylesmechanisms pages 8-10): Tony Collins and Rosa Margesin. Psychrophilic lifestyles: mechanisms of adaptation and biotechnological tools. Applied Microbiology and Biotechnology, 103:2857-2871, Feb 2019. URL: https://doi.org/10.1007/s00253-019-09659-5, doi:10.1007/s00253-019-09659-5. This article has 294 citations and is from a domain leading peer-reviewed journal.

19. (collins2019psychrophiliclifestylesmechanisms pages 1-5): Tony Collins and Rosa Margesin. Psychrophilic lifestyles: mechanisms of adaptation and biotechnological tools. Applied Microbiology and Biotechnology, 103:2857-2871, Feb 2019. URL: https://doi.org/10.1007/s00253-019-09659-5, doi:10.1007/s00253-019-09659-5. This article has 294 citations and is from a domain leading peer-reviewed journal.

20. (anesi2016comparativeanalysisof pages 1-2): Andrea Anesi, Ulrike Obertegger, Gert Hansen, Assaf Sukenik, Giovanna Flaim, and Graziano Guella. Comparative analysis of membrane lipids in psychrophilic and mesophilic freshwater dinoflagellates. Frontiers in Plant Science, Apr 2016. URL: https://doi.org/10.3389/fpls.2016.00524, doi:10.3389/fpls.2016.00524. This article has 32 citations.