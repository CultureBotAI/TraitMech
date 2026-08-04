---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:26:53.426143'
end_time: '2026-08-04T11:33:49.982765'
duration_seconds: 416.56
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mixotrophic
  trait_identifier: METPO:1000652
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: mixotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism can use both organic and inorganic
    carbon sources for growth.
  parent_traits: METPO:1000631
  synonyms: mixotroph
  evidence_summary: 'DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic
    bacteria (Review supports bacterial mixotrophy as combined metabolic modes in
    marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which
    an organism can obtain its energy and carbon (Perspective supports mixotrophy
    as combined energy and carbon acquisition modes.)'
  causal_graph_summary: 'mixotrophic_dual_carbon_energy_use: 14 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000652
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism can use both organic and inorganic carbon sources for growth.
- **Parent traits:** METPO:1000631
- **Synonyms:** mixotroph
- **Existing evidence:** DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic bacteria (Review supports bacterial mixotrophy as combined metabolic modes in marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which an organism can obtain its energy and carbon (Perspective supports mixotrophy as combined energy and carbon acquisition modes.)
- **Existing causal graph summary:** mixotrophic_dual_carbon_energy_use: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **mixotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/mixotrophic.yaml`.

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
- **Trait label:** mixotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000652
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism can use both organic and inorganic carbon sources for growth.
- **Parent traits:** METPO:1000631
- **Synonyms:** mixotroph
- **Existing evidence:** DOI:10.1128/AEM.01559-06: Evidence for the ubiquity of mixotrophic bacteria (Review supports bacterial mixotrophy as combined metabolic modes in marine systems.) | DOI:10.1073/pnas.1305998110: combination of modes by which an organism can obtain its energy and carbon (Perspective supports mixotrophy as combined energy and carbon acquisition modes.)
- **Existing causal graph summary:** mixotrophic_dual_carbon_energy_use: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **mixotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/mixotrophic.yaml`.

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


# Curation report: microbial trait **mixotrophic**

## 1. Scope summary

**Trait record:** `METPO:1000652` (quote verbatim)  
**Category:** PHYSIOLOGY · **Term kind:** CLASS · **Status:** REVIEWED  
**Parent:** `METPO:1000631`  
**Definition supplied:** “A trophic type in which an organism can use both organic and inorganic carbon sources for growth.”

For TraitMech, the safest interpretation is a **physiological capacity for growth-supporting acquisition of carbon through both (i) inorganic-carbon fixation and (ii) assimilation or catabolism of organic carbon**. The two modes may operate simultaneously or be flexibly balanced across conditions. Mixotrophy is therefore not one conserved pathway: it is a higher-level phenotype realized by multiple carbon-fixation, energy-generation, transport, and organic-carbon catabolic modules.

Recent studies reinforce this functional definition. Marine Arcobacteraceae combine reverse-TCA carbon fixation driven by reduced sulfur oxidation and nitrate reduction with organic-matter metabolism, while groundwater Burkholderiales balance Calvin-cycle fixation with uptake of environmental organic carbon. Marine picocyanobacteria combine photosynthetic inorganic-carbon fixation with glucose, amino-acid, and peptide uptake (li2024arcobacteraceaeareubiquitous pages 1-2, munozmarin2020mixotrophyinmarine pages 5-7, taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 1-2).

### Boundary cases

1. **Not strict autotrophy:** possession or expression of a complete autotrophic fixation pathway without demonstrated organic-carbon use is insufficient.
2. **Not strict heterotrophy:** organic-carbon growth plus only incidental bicarbonate incorporation does not establish mixotrophy.
3. **Exclude ordinary anaplerosis unless stronger evidence exists.** Heterotrophic carboxylation commonly contributes about 1–8% of microbial biomass carbon and extends organic substrates by C1 units; it is mechanistically distinct from a growth-supporting autotrophic module (braun2021reviewsandsyntheses pages 1-2).
4. **Organic-nutrient uptake is not necessarily organic-carbon nutrition.** In Marine Group I Thaumarchaeota, organic substrates were used principally to satisfy nitrogen demand. Organic carbon contributed approximately 4–7% of population biomass carbon, and <1% of newly synthesized biomass carbon from tested glucose, pyruvate, and oxaloacetate; classification as predominantly chemolithoautotrophic remained more appropriate (parada2023constrainingthecomposition pages 1-6, parada2023constrainingthecomposition pages 17-19).
5. **Community-level coexistence is not organism-level mixotrophy.** Bulk CO₂ fixation and organic-substrate consumption can arise from separate autotrophic and heterotrophic populations. Single-cell isotope evidence, isolate growth, or genome-resolved expression in the same lineage is preferable.
6. **Potential is not phenotype.** Co-occurrence of fixation and transporter genes in a genome is weaker than growth, flux, isotope-incorporation, proteomic, or lineage-resolved transcriptomic evidence.
7. **Trophic flexibility versus simultaneous mixotrophy:** facultative switching between autotrophic and heterotrophic growth may fit the supplied broad definition, but edges claiming simultaneous operation require direct evidence.

## 2. Current understanding and recent developments

### 2.1 Marine Arcobacteraceae—strong 2024 graph seed

Li et al. identified two candidate mixotrophic genera, UBA6211 and CAIJNA01, with reverse-TCA carbon fixation potential. CAIJNA01-like organisms expressed a mechanism coupling sulfur oxidation and denitrification to carbon fixation while also metabolizing organic matter. Candidate electron donors include sulfide, thiosulfate, and hydrogen; nitrate reduction proceeds through denitrification or DNRA. The result is taxon-specific but unusually complete evidence linking energy metabolism, electron acceptors, carbon fixation, and heterotrophy in the same lineage (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10).

Across 187 ocean sites, DIC-fixation genes were transcribed at 80% of sites; thiosulfate- and sulfide-utilization signatures occurred at 98% and 72%, respectively. Heterotrophic activity was slightly higher than autotrophic activity (`P < 0.001`). The authors also reported organic pathways including fermentation and oxidation of fatty acids, methane, methanol, formate, and pyruvate, although individual modules should not all be generalized to every Arcobacteraceae genome (li2024arcobacteraceaeareubiquitous pages 10-12).

### 2.2 Dark-ocean sulfur–carbon coupling—2023

In Labrador Sea Water from approximately 2,000 m depth, adding 1 µM thiosulfate enhanced inorganic-carbon fixation. Co-addition of thiosulfate, 10 µM glucose, and 10 µM acetate stimulated copiotrophic Gammaproteobacteria. Sox-system sulfur oxidation was associated with CO₂ fixation, while heterotrophic organisms induced glycogen and phospholipid storage functions. This is strong evidence for environmental control of coupled autotrophic and heterotrophic metabolism, but much of the result is community-level and should not automatically become a single-organism trait edge (srivastava2023interplaybetweenautotrophic pages 1-2).

### 2.3 Quantitative groundwater mixotrophy

Stable-isotope cluster analysis showed that mixotrophs—including relatives of *Hydrogenophaga*, *Polaromonas*, and *Dechloromonas*—dominated thiosulfate-stimulated groundwater microcosms. CO₂-derived carbon replaced 43% of microbial carbon stores after 21 days and 80% after 70 days. Mixotrophs represented more than half of the community, outnumbered strict autotrophs approximately 5:1, and some clusters had generation times ≤2 days versus up to 8 days for heterotrophs. The inferred advantage is the capacity to balance CBB-cycle fixation against uptake of carbohydrates, amino acids, nucleotides, C1 compounds, and hydrocarbons under oligotrophic conditions (taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 6-7, taubert2022bolsteringfitnessvia pages 7-8).

### 2.4 Picocyanobacterial mixotrophy

*Prochlorococcus* and *Synechococcus* use organic compounds while retaining photosynthetic carbon fixation. The high-affinity, ATP-dependent glucose transporter **GlcH** is reported across *Prochlorococcus* clades and is expressed in response to glucose. Imported glucose can feed the pentose-phosphate and Entner–Doudoroff pathways. Genes for amino-acid, peptide, and sugar uptake were found across 67 strains. Uptake of three glucose molecules was estimated to cost one ATP, compared with 18 ATP for their biosynthesis, supporting an energy-saving explanation for mixotrophy in oligotrophic waters (munozmarin2020mixotrophyinmarine pages 5-7, munozmarin2020mixotrophyinmarine pages 1-2).

## 3. Candidate causal-graph nodes

Ontology mappings below are deliberately conservative. **Label-only** means that an exact stable identifier should be resolved during ontology review rather than guessed.

### Trait and processes

- **mixotrophic** — `METPO:1000652`
- inorganic-carbon fixation — `GO:0015977`
- organic-carbon compound utilization — label-only candidate
- photosynthesis — `GO:0015979`
- sulfur-compound oxidation — label-only candidate
- denitrification — `GO:0019333`
- dissimilatory nitrate reduction to ammonium (DNRA) — label-only candidate
- carbohydrate transport/catabolism — label-only candidate
- fermentation — `GO:0006113`
- glycogen biosynthesis — `GO:0005978`
- phospholipid biosynthesis — `GO:0008654`

### Carbon-fixation pathways and modules

- Calvin–Benson–Bassham cycle — label-only candidate; verify a current pathway CURIE
- reverse/reductive tricarboxylic-acid cycle — label-only candidate
- Wood–Ljungdahl pathway / reductive acetyl-CoA pathway — label-only candidate
- carbon-concentrating mechanism — label-only candidate
- anaplerotic carboxylation — label-only **exclusion/boundary node**

### Genes, proteins, enzymes, and complexes

- **glcH**, high-affinity glucose transporter — gene/protein label; use strain-specific UniProt IDs only after taxon and sequence are fixed
- Sox sulfur-oxidation system — complex/module label
- CO dehydrogenase/acetyl-CoA synthase complex — label-only; enzyme components require organism-specific grounding
- RuBisCO — label-only candidate; use EC/UniProt grounding only for a specified form and organism
- ATP citrate lyase or alternative rTCA enzymes — candidate only; not directly established for every lineage in the retrieved evidence
- organic-carbon transporters — generic node; refine to glucose, amino-acid, oligopeptide, or C1-compound transporter

### Chemicals and nutrients

High-confidence chemical candidates include:

- carbon dioxide — `CHEBI:16526`
- hydrogencarbonate/bicarbonate — `CHEBI:17544`
- glucose — `CHEBI:17234`
- acetate — `CHEBI:30089`
- pyruvate — `CHEBI:15361`
- molecular hydrogen — `CHEBI:18276`
- nitrate — `CHEBI:17632`
- ammonium — `CHEBI:28938`
- thiosulfate — `CHEBI:26977`
- hydrogen sulfide — `CHEBI:16136`
- oxygen — `CHEBI:15379`
- organic matter / dissolved organic matter — label-only environmental material
- amino acids, peptides, urea, ATP, DMSP, fatty acids, methane, methanol, formate, ethanol, lactate, CO — retain as labels until exact protonation/state-specific CHEBI grounding is reviewed

### Environmental and experimental factors

- oligotrophic water — ENVO grounding to be reviewed
- bathypelagic marine water (~2,000 m) — ENVO grounding to be reviewed
- groundwater — `ENVO:01001004`
- deep-sea in-situ incubation — assay/environment node
- light availability — experimental/environmental factor
- reduced-sulfur availability — experimental/environmental factor
- nitrate availability — experimental/environmental factor
- dissolved-organic-carbon availability — experimental/environmental factor
- oxygenated versus anoxic condition — environmental states; exact ENVO/PATO grounding to be reviewed
- ^13CO₂ stable-isotope probing — assay node
- metagenomics, metatranscriptomics, and metaproteomics — assay nodes

### Taxa

- Arcobacteraceae — use the current NCBITaxon identifier after taxonomy-version verification
- *Candidatus* UBA6211 and CAIJNA01 — provisional taxon labels
- *Prochlorococcus* — `NCBITaxon:1218`
- *Synechococcus* — genus label requiring lineage-specific resolution because the name spans distinct taxonomic usages
- *Hydrogenophaga*, *Polaromonas*, *Dechloromonas*, *Methyloversatilis*, *Rhodoferax*, *Paucibacter*, and *Rubrivivax* — genus labels; verify NCBITaxon IDs during implementation
- acetogens including *Blautia producta*, *Clostridium scatologenes*, and *Thermoanaerobacter kivui* — species labels requiring current-taxonomy verification

## 4. Candidate evidence-backed edges

The following compact table identifies the strongest graph backbone.

| subject | predicate | object | scope/uncertainty | primary DOI |
|---|---|---|---|---|
| mixotrophic trait | enables growth by using | both inorganic carbon fixation and organic carbon assimilation | Broad trait definition; applies to growth-supporting dual carbon use, not merely trace co-assimilation (li2024arcobacteraceaeareubiquitous pages 1-2, taubert2022bolsteringfitnessvia pages 1-2) | 10.1073/pnas.1305998110 |
| reduced sulfur compound oxidation | provides energy for | inorganic carbon fixation in marine mixotrophs | Strong in marine Arcobacteraceae and bathypelagic sulfur-oxidizers; donor examples include thiosulfate and sulfide (li2024arcobacteraceaeareubiquitous pages 1-2, srivastava2023interplaybetweenautotrophic pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10) | 10.1128/msystems.00513-24 |
| denitrification / DNRA | couples to | sulfur-driven carbon fixation | Strong but taxon-specific to marine Arcobacteraceae lineages and related sulfur oxidizers (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10) | 10.1128/msystems.00513-24 |
| reverse TCA pathway | mediates | inorganic carbon fixation in marine Arcobacteraceae mixotrophs | Strong for Candidatus UBA6211 and CAIJNA01; not universal across all mixotrophs (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10) | 10.1128/msystems.00513-24 |
| organic matter metabolism | co-occurs with | sulfur oxidation-coupled carbon fixation | Strong for CAIJNA01-like marine mixotrophs; supports simultaneous autotrophic and heterotrophic metabolism (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10) | 10.1128/msystems.00513-24 |
| glcH glucose transporter | enables uptake of | glucose for mixotrophic metabolism in marine picocyanobacteria | Strong for Prochlorococcus/Synechococcus; phototroph-specific, not general bacterial mechanism (munozmarin2020mixotrophyinmarine pages 5-7) | 10.1038/s41396-020-0603-9 |
| Calvin-Benson-Bassham cycle | supports | groundwater mixotrophy with simultaneous CO2 fixation and organic carbon uptake | Strong in oligotrophic groundwater microcosms; taxa include Hydrogenophaga/Polaromonas/Dechloromonas relatives (taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 6-7, taubert2022bolsteringfitnessvia pages 1-2) | 10.1038/s41396-021-01163-x |
| reduced sulfur compounds (e.g., thiosulfate) | stimulate | mixotrophic growth and CO2 incorporation in groundwater communities | Strong in experimental microcosms; assay-specific environmental driver (taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 1-2) | 10.1038/s41396-021-01163-x |
| Wood-Ljungdahl pathway | mediates | anaerobic non-photosynthetic mixotrophic CO2/CO fixation during growth on carbohydrates | Strong for acetogens; anaerobic and taxon-specific rather than universal (maru2018fixationofco2 pages 1-5) | 10.1093/femsle/fny039 |
| glycolysis / carbohydrate catabolism | supplies ATP and reducing power for | Wood-Ljungdahl pathway carbon fixation | Strong in acetogen mixotrophy; mechanistic energy-coupling edge (maru2018fixationofco2 pages 1-5) | 10.1093/femsle/fny039 |
| heterotrophic anaplerotic CO2 fixation | should not be equated with | mixotrophic trait | Important negative/boundary edge; usually co-substrate carboxylation contributing minor biomass fractions rather than growth-supporting autotrophy (braun2021reviewsandsyntheses pages 1-2, braun2021reviewsandsyntheses pages 4-5) | 10.5194/bg-18-3689-2021 |
| organic nitrogen uptake by marine Thaumarchaeota | should not be interpreted as | strong evidence of mixotrophic organic carbon growth | Important negative/boundary edge; organic substrates mainly satisfy N demand, with low organic C contribution (parada2023constrainingthecomposition pages 1-6, parada2023constrainingthecomposition pages 17-19) | 10.1111/1462-2920.16299 |


*Table: This table summarizes the strongest curation-ready causal edges for microbial mixotrophy, emphasizing growth-supporting dual carbon use and the best-supported mechanistic modules. It also includes explicit boundary edges to prevent miscuration of anaplerotic CO2 fixation or primarily organic-nitrogen uptake as true mixotrophy.*

A more explicit curation representation follows. Predicates are proposed relation labels, not asserted ontology relations.

| # | Subject — predicate — object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | `METPO:1000652` — **has carbon-source input** — inorganic carbon | Moore 2013; Li 2024 | “combination of modes by which an organism can obtain its energy and carbon”; Arcobacteraceae conduct DIC fixation | Trait-defining backbone; use with edge 2, not alone (li2024arcobacteraceaeareubiquitous pages 1-2). |
| 2 | `METPO:1000652` — **has carbon-source input** — organic carbon | Li 2024; Taubert 2022 | CAIJNA01 “conducts carbon fixation … and metaboliz[es] organic matter”; groundwater organisms balance CO₂ fixation and organic uptake | Trait-defining backbone (li2024arcobacteraceaeareubiquitous pages 1-2, taubert2022bolsteringfitnessvia pages 1-2). |
| 3 | reduced sulfur oxidation — **provides energy for** — inorganic-carbon fixation | Li 2024 | Carbon fixation was coupled to sulfur oxidation; sulfide, thiosulfate, and hydrogen oxidation genes were identified | Strong for Arcobacteraceae; taxon-specific (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10). |
| 4 | nitrate — **serves as electron acceptor in** — sulfur-driven carbon fixation | Li 2024 | Sulfur oxidation was coupled with denitrification or DNRA | Strong lineage-specific mechanism; avoid universal trait edge (li2024arcobacteraceaeareubiquitous pages 10-12, li2024arcobacteraceaeareubiquitous pages 1-2). |
| 5 | reverse TCA cycle — **mediates** — inorganic-carbon fixation | Li 2024 | UBA6211 and CAIJNA01 “harbor genes putatively involved in the reverse tricarboxylic acid pathway” | Genomic plus transcriptomic support; “putatively” warrants qualified confidence (li2024arcobacteraceaeareubiquitous pages 1-2). |
| 6 | organic-matter metabolism — **co-occurs with** — rTCA carbon fixation | Li 2024 | CAIJNA01 was described as fixing carbon while metabolizing organic matter | Strong mixotrophy edge in a genome-resolved lineage, although uncultivated (li2024arcobacteraceaeareubiquitous pages 1-2). |
| 7 | thiosulfate availability — **increases** — inorganic-carbon fixation | Srivastava 2023 | “Amendment … with thiosulfate … enhanced prokaryotic inorganic carbon fixation” | Direct perturbation evidence; community- and assay-specific (srivastava2023interplaybetweenautotrophic pages 1-2). |
| 8 | thiosulfate + glucose + acetate — **stimulates** — copiotrophic Gammaproteobacteria | Srivastava 2023 | Co-amendment stimulated *Vibrio*/*Pseudoalteromonas*-related Gammaproteobacteria | Do not equate stimulation with organism-level mixotrophy without lineage-resolved dual uptake (srivastava2023interplaybetweenautotrophic pages 1-2). |
| 9 | sulfur oxidation/CO₂ fixation — **is associated with** — glycogen and phospholipid biosynthesis | Srivastava 2023 | Energy from chemoautotrophy and heterotrophy was used for storage-molecule biosynthesis | Community metabolic-interplay edge; uncertain as a direct intracellular edge (srivastava2023interplaybetweenautotrophic pages 1-2). |
| 10 | CBB cycle — **mediates** — groundwater CO₂ fixation | Taubert 2022 | Mixotrophs fixed CO₂ via the CBB cycle while assimilating organic carbon | Strong, isotope/proteomic evidence (taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 6-7). |
| 11 | organic-carbon uptake — **complements** — CBB-cycle fixation | Taubert 2022 | Organisms used different strategies to balance fixation and uptake | Strong phenotype-level relation; substrate-specific edges require corresponding transporter evidence (taubert2022bolsteringfitnessvia pages 1-2). |
| 12 | oligotrophic conditions — **select for/increase fitness of** — mixotrophic strategy | Taubert 2022 | Flexibility may provide fitness under nutrient-limited conditions | Mechanistically plausible and experimentally supported, but “select for” remains partly interpretive (taubert2022bolsteringfitnessvia pages 1-2, taubert2022bolsteringfitnessvia pages 7-8). |
| 13 | `glcH` — **enables transport of** — glucose | Muñoz-Marín 2020 | `glcH` encodes an ATP-dependent, high-affinity glucose transporter expressed upon glucose availability | Strong for marine picocyanobacteria; species/strain-specific sequence grounding required (munozmarin2020mixotrophyinmarine pages 5-7). |
| 14 | imported glucose — **feeds** — pentose-phosphate and Entner–Doudoroff pathways | Muñoz-Marín 2020 | Two reported glucose-assimilation routes were pentose-phosphate and Entner–Doudoroff pathways | Strong review-supported mechanistic edge; phototroph-specific (munozmarin2020mixotrophyinmarine pages 5-7). |
| 15 | organic-compound uptake — **reduces energetic cost relative to** — de novo biosynthesis | Muñoz-Marín 2020 | Three glucose molecules cost about 1 ATP to import versus 18 ATP to synthesize | Useful explanatory edge; quantitative estimate is system-specific (munozmarin2020mixotrophyinmarine pages 5-7). |
| 16 | glycolysis of carbohydrate — **supplies ATP/reductant to** — Wood–Ljungdahl fixation | Maru 2018 | Glycolysis generates excess ATP that powers CO₂ fixation through WLP | Strong in anaerobic acetogens, not a universal mixotrophic mechanism (maru2018fixationofco2 pages 1-5). |
| 17 | Wood–Ljungdahl pathway — **fixes** — CO₂ or CO into acetyl-CoA-derived carbon | Maru 2018 | Methyl and carbonyl branches unite through CO dehydrogenase/acetyl-CoA synthase | Mechanistically strong, anaerobic and taxon-specific (maru2018fixationofco2 pages 1-5). |
| 18 | H₂ or reduced organic feedstock — **provides reducing equivalents for** — Wood–Ljungdahl fixation | Maru 2018 | Electrons were supplied by H₂, syngas, or reduced feedstocks such as glycerol | Strong under the reported fermentation conditions; separate substrate-specific edges (maru2018fixationofco2 pages 1-5). |
| 19 | heterotrophic anaplerotic CO₂ fixation — **is insufficient evidence for** — `METPO:1000652` | Braun 2021 | Anaplerosis is a co-substrate mechanism adding C1 units rather than primary autotrophic fixation | Recommended negative curation rule (braun2021reviewsandsyntheses pages 1-2). |
| 20 | organic-nitrogen uptake — **is insufficient evidence for** — organic-carbon-supported growth | Parada 2023 | Thaumarchaeota used organic substrates mainly to meet nitrogen demand | Recommended negative curation rule (parada2023constrainingthecomposition pages 1-6, parada2023constrainingthecomposition pages 17-19). |

## 5. Recommended initial TraitMech graph architecture

A single universal linear chain would overgeneralize. The YAML should use a **shared phenotype core plus alternative mechanistic branches**:

1. **Core phenotype**
   - inorganic carbon → carbon-fixation module → biomass carbon
   - organic carbon → transporter/catabolic module → biomass carbon and/or energy
   - both branches → `METPO:1000652`

2. **Chemolithotrophic Arcobacteraceae branch**
   - sulfide/thiosulfate/H₂ → oxidation → reducing power/proton motive force
   - nitrate → denitrification or DNRA
   - energy/reductant → rTCA fixation
   - organic matter → uptake/catabolism
   - rTCA fixation + organic-matter metabolism → mixotrophic growth

3. **Photo-mixotrophic picocyanobacteria branch**
   - light → photosynthesis → energy/reductant
   - inorganic carbon → photosynthetic fixation
   - glucose → GlcH → PPP/Entner–Doudoroff metabolism
   - dual assimilation → mixotrophic growth

4. **Groundwater CBB branch**
   - thiosulfate + oxygen → chemolithotrophic energy generation
   - CO₂ → CBB cycle → biomass
   - environmental organic compounds → transport/catabolism
   - balanced fluxes → rapid growth under oligotrophy

5. **Anaerobic acetogen branch**
   - carbohydrate → glycolysis → ATP/reductant
   - CO₂/CO → Wood–Ljungdahl pathway
   - pathway coupling → enhanced carbon yield

This architecture preserves the 14-node/13-edge existing summary as a possible core while avoiding the false implication that every mixotroph uses sulfur oxidation, nitrate reduction, rTCA, CBB, photosynthesis, or WLP.

## 6. Applications and real-world relevance

- **Ocean carbon-cycle modeling:** globally distributed Arcobacteraceae expressed carbon-, sulfur-, and nitrogen-cycling functions across ocean regions and depths, implying that models dividing microbes strictly into autotrophs and heterotrophs can misassign carbon flux (li2024arcobacteraceaeareubiquitous pages 10-12, li2024arcobacteraceaeareubiquitous pages 1-2).
- **Groundwater and subsurface carbon cycling:** mixotrophs can dominate dark primary production and rapidly recycle newly fixed carbon. The observed 43% and 80% replacement of microbial carbon over 21 and 70 days illustrates substantial ecosystem impact (taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 1-2).
- **Wastewater denitrification:** recent 2023–2024 engineering studies apply sulfur-, pyrite-, hydrogen-, or iron-supported mixotrophic denitrification to nitrate removal. These are important implementation domains, but reactor-level performance should not be curated as a universal cellular mechanism without organism-resolved evidence.
- **CO₂ capture and biomanufacturing:** photo-mixotrophic microalgae and cyanobacteria combine inorganic-carbon capture with organic-feed utilization to increase biomass or product yields. Anaerobic acetogen mixotrophy can improve carbon retention by coupling carbohydrate conversion to CO₂/CO reassimilation; the tested WLP consumes approximately one ATP and four reducing equivalents and can approach very high carbon yield under selected conditions (maru2018fixationofco2 pages 1-5).
- **Ecological forecasting:** substrate availability, light, oxygen, sulfur compounds, and nitrate can shift the balance between autotrophic and heterotrophic fluxes. Trait models should therefore treat mixotrophy as condition-dependent rather than constitutively active.

## 7. Expert interpretation

The strongest current view is that mixotrophy is a **continuum of carbon-allocation strategies**, not a binary metabolic state. Groundwater taxa differ in how much carbon they derive from CO₂ versus organic compounds, and Arcobacteraceae show slightly greater heterotrophic than autotrophic activity despite expressing both systems (li2024arcobacteraceaeareubiquitous pages 10-12, taubert2022bolsteringfitnessvia pages 6-7).

Authoritative studies also emphasize measurement design. Bulk isotope incorporation cannot determine whether every cell is mixotrophic or whether separate subpopulations specialize. Parada et al. showed that an apparent population-level inorganic/organic split may conceal uptake by only a minority of cells, while Braun et al. showed that routine anaplerotic CO₂ fixation can mimic dual-carbon use (parada2023constrainingthecomposition pages 1-6, braun2021reviewsandsyntheses pages 1-2). Accordingly, high-confidence curation should prioritize isolate growth, single-cell dual-isotope measurements, quantitative SIP, or genome-resolved multi-omics that localize both branches to one organism.

## 8. Warnings—claims not yet ready for TraitMech

1. **Do not curate every Arcobacteraceae pathway as universal.** rTCA fixation is concentrated in particular clade-C candidate genera; methane oxidation, arsenate reduction, perchlorate reduction, and other expanded functions are unevenly distributed (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 7-10).
2. **Do not make “thiosulfate + DOM → mixotrophy” an organism-level edge from the bathypelagic experiment alone.** The response can reflect interspecies metabolic coupling (srivastava2023interplaybetweenautotrophic pages 1-2).
3. **Do not classify Thaumarchaeota as mixotrophic solely from urea or amino-acid uptake.** The recent single-cell study supports primarily organic-nitrogen acquisition, with limited organic-carbon assimilation (parada2023constrainingthecomposition pages 1-6, parada2023constrainingthecomposition pages 17-19).
4. **Do not use presence of `glcH` as a universal biomarker.** It supports glucose uptake in marine picocyanobacteria but is neither necessary nor sufficient for all forms of mixotrophy (munozmarin2020mixotrophyinmarine pages 5-7).
5. **Do not equate trace ^13CO₂ incorporation with autotrophy.** Require a complete fixation module and evidence that inorganic carbon materially supports growth; heterotrophic anaplerosis alone is insufficient (braun2021reviewsandsyntheses pages 1-2).
6. **Do not infer simultaneous operation from alternative growth tests.** Record facultative dual capacity separately when autotrophic and heterotrophic modes were tested only in separate treatments.
7. **Do not assign strain-specific UniProt, EC, Rhea, KEGG, or MetaCyc identifiers without sequence/reaction verification.** Several pathways have isoenzymatic alternatives and taxon-dependent implementations.
8. **Avoid hard quantitative thresholds for mixotrophy.** The literature provides no accepted minimum percentage of biomass carbon that must derive from each source; the biological role and completeness of the fixation machinery are more informative than a single cutoff.

## 9. DOI-first bibliography

1. **Li J. et al.** “Arcobacteraceae are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans.” *mSystems* 9(7), **July 2024**. DOI: [10.1128/msystems.00513-24](https://doi.org/10.1128/msystems.00513-24) (li2024arcobacteraceaeareubiquitous pages 10-12, li2024arcobacteraceaeareubiquitous pages 1-2).
2. **Parada A.E. et al.** “Constraining the composition and quantity of organic matter used by abundant marine Thaumarchaeota.” *Environmental Microbiology* 25, 689–704, **2023**; online metadata retrieved December 2023. DOI: [10.1111/1462-2920.16299](https://doi.org/10.1111/1462-2920.16299) (parada2023constrainingthecomposition pages 1-6, parada2023constrainingthecomposition pages 17-19).
3. **Srivastava A. et al.** “Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses.” *Microbiome* 11, **November 2023**. DOI: [10.1186/s40168-023-01688-7](https://doi.org/10.1186/s40168-023-01688-7) (srivastava2023interplaybetweenautotrophic pages 1-2).
4. **Taubert M. et al.** “Bolstering fitness via CO₂ fixation and organic carbon uptake: mixotrophs in modern groundwater.” *ISME Journal* 16, 1153–1162, **2022**; online publication December 2021. DOI: [10.1038/s41396-021-01163-x](https://doi.org/10.1038/s41396-021-01163-x) (taubert2022bolsteringfitnessvia pages 5-6, taubert2022bolsteringfitnessvia pages 1-2).
5. **Braun A. et al.** “Reviews and syntheses: Heterotrophic fixation of inorganic carbon—significant but invisible flux in environmental carbon cycling.” *Biogeosciences* 18, 3689–3700, **June 2021**. DOI: [10.5194/bg-18-3689-2021](https://doi.org/10.5194/bg-18-3689-2021) (braun2021reviewsandsyntheses pages 1-2, braun2021reviewsandsyntheses pages 4-5).
6. **Muñoz-Marín M.C. et al.** “Mixotrophy in marine picocyanobacteria: use of organic compounds by Prochlorococcus and Synechococcus.” *ISME Journal* 14, 1065–1073, **February 2020**. DOI: [10.1038/s41396-020-0603-9](https://doi.org/10.1038/s41396-020-0603-9) (munozmarin2020mixotrophyinmarine pages 5-7, munozmarin2020mixotrophyinmarine pages 1-2).
7. **Maru B.T. et al.** “Fixation of CO₂ and CO on a diverse range of carbohydrates using anaerobic, non-photosynthetic mixotrophy.” *FEMS Microbiology Letters* 365, **April 2018**. DOI: [10.1093/femsle/fny039](https://doi.org/10.1093/femsle/fny039) (maru2018fixationofco2 pages 1-5).
8. **Moore L.R.** “More mixotrophy in the marine microbial mix.” *Proceedings of the National Academy of Sciences* 110, 8323–8324, **May 2013**. DOI: [10.1073/pnas.1305998110](https://doi.org/10.1073/pnas.1305998110).

References

1. (li2024arcobacteraceaeareubiquitous pages 1-2): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 39 citations and is from a peer-reviewed journal.

2. (munozmarin2020mixotrophyinmarine pages 5-7): M. C. Muñoz-Marín, G. Gómez-Baena, A. López‐Lozano, J. A. Moreno-Cabezuelo, Jesús Díez, and J. García-Fernández. Mixotrophy in marine picocyanobacteria: use of organic compounds by prochlorococcus and synechococcus. The ISME Journal, 14:1065-1073, Feb 2020. URL: https://doi.org/10.1038/s41396-020-0603-9, doi:10.1038/s41396-020-0603-9. This article has 116 citations.

3. (taubert2022bolsteringfitnessvia pages 5-6): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 69 citations.

4. (taubert2022bolsteringfitnessvia pages 1-2): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 69 citations.

5. (braun2021reviewsandsyntheses pages 1-2): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.

6. (parada2023constrainingthecomposition pages 1-6): Alma E. Parada, Xavier Mayali, Peter K. Weber, Jessica Wollard, Alyson E. Santoro, Jed A. Fuhrman, Jennifer Pett‐Ridge, and Anne E. Dekas. Constraining the composition and quantity of organic matter used by abundant marine thaumarchaeota. Dec 2023. URL: https://doi.org/10.1111/1462-2920.16299, doi:10.1111/1462-2920.16299. This article has 19 citations and is from a domain leading peer-reviewed journal.

7. (parada2023constrainingthecomposition pages 17-19): Alma E. Parada, Xavier Mayali, Peter K. Weber, Jessica Wollard, Alyson E. Santoro, Jed A. Fuhrman, Jennifer Pett‐Ridge, and Anne E. Dekas. Constraining the composition and quantity of organic matter used by abundant marine thaumarchaeota. Dec 2023. URL: https://doi.org/10.1111/1462-2920.16299, doi:10.1111/1462-2920.16299. This article has 19 citations and is from a domain leading peer-reviewed journal.

8. (li2024arcobacteraceaeareubiquitous pages 7-10): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 39 citations and is from a peer-reviewed journal.

9. (li2024arcobacteraceaeareubiquitous pages 10-12): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 39 citations and is from a peer-reviewed journal.

10. (srivastava2023interplaybetweenautotrophic pages 1-2): Abhishek Srivastava, Daniele De Corte, Juan A. L. Garcia, Brandon K. Swan, Ramunas Stepanauskas, Gerhard J. Herndl, and Eva Sintes. Interplay between autotrophic and heterotrophic prokaryotic metabolism in the bathypelagic realm revealed by metatranscriptomic analyses. Microbiome, Nov 2023. URL: https://doi.org/10.1186/s40168-023-01688-7, doi:10.1186/s40168-023-01688-7. This article has 10 citations and is from a highest quality peer-reviewed journal.

11. (taubert2022bolsteringfitnessvia pages 6-7): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 69 citations.

12. (taubert2022bolsteringfitnessvia pages 7-8): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 69 citations.

13. (munozmarin2020mixotrophyinmarine pages 1-2): M. C. Muñoz-Marín, G. Gómez-Baena, A. López‐Lozano, J. A. Moreno-Cabezuelo, Jesús Díez, and J. García-Fernández. Mixotrophy in marine picocyanobacteria: use of organic compounds by prochlorococcus and synechococcus. The ISME Journal, 14:1065-1073, Feb 2020. URL: https://doi.org/10.1038/s41396-020-0603-9, doi:10.1038/s41396-020-0603-9. This article has 116 citations.

14. (maru2018fixationofco2 pages 1-5): Biniam T Maru, Pradeep C Munasinghe, Hadar Gilary, Shawn W Jones, and Bryan P Tracy. Fixation of co2 and co on a diverse range of carbohydrates using anaerobic, non-photosynthetic mixotrophy. FEMS Microbiology Letters, 365:&NA;, Apr 2018. URL: https://doi.org/10.1093/femsle/fny039, doi:10.1093/femsle/fny039. This article has 74 citations and is from a peer-reviewed journal.

15. (braun2021reviewsandsyntheses pages 4-5): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.