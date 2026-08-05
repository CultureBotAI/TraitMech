---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:18:00.409754'
end_time: '2026-08-04T11:26:42.916037'
duration_seconds: 522.51
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: lithoheterotrophic
  trait_identifier: METPO:1000648
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: lithoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from the oxidation
    of inorganic compounds while using organic compounds as the primary carbon source
    for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: lithoheterotroph
  evidence_summary: 'DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic
    strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth
    with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize
    inorganic atoms or molecules (Review supports inorganic compound oxidation as
    lithotrophic energy metabolism.)'
  causal_graph_summary: 'lithoheterotrophic_inorganic_energy_organic_carbon: 18 nodes,
    17 edges'
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
- **Trait label:** lithoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000648
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of inorganic compounds while using organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.)
- **Existing causal graph summary:** lithoheterotrophic_inorganic_energy_organic_carbon: 18 nodes, 17 edges

## Research Objective

Research the microbial trait **lithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoheterotrophic.yaml`.

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
- **Trait label:** lithoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000648
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of inorganic compounds while using organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.)
- **Existing causal graph summary:** lithoheterotrophic_inorganic_energy_organic_carbon: 18 nodes, 17 edges

## Research Objective

Research the microbial trait **lithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoheterotrophic.yaml`.

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


# Curation-focused research report: lithoheterotrophic

**Trait:** `lithoheterotrophic`  
**Identifier:** **“METPO:1000648”**  
**Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** `METPO:1000631`

## 1. Scope summary and current understanding

Lithoheterotrophy is a trophic strategy in which oxidation of a reduced inorganic electron donor supplies respiratory energy, while preformed organic compounds provide the principal carbon incorporated into biomass. The defining evidence therefore requires two experimentally separable fluxes: **(i)** inorganic-donor oxidation linked to energy conservation and **(ii)** organic-carbon uptake and assimilation. It does not require one universal donor, acceptor, or pathway.

The clearest model is *Arcobacter peruensis*: sulfide oxidation is coupled to nitrate reduction, whereas acetate is assimilated and CO₂ fixation is negligible. The isolate grew best with sulfide, nitrate, and acetate; isotope experiments verified acetate assimilation and complete nitrate reduction to N₂. Its reported yield was 3.1 mol assimilated C per mol H₂S oxidized, and sulfide plus acetate supported approximately twice the growth observed under CO₂-fixing conditions. The organism’s acetate system had an apparent *K*m of 5.4 μM. These observations directly separate energy source from biomass-carbon source. (callbeck2019arcobacterperuensissp. pages 9-12)

A 2023 marine study broadened this model to trace-gas metabolism: H₂ oxidation by uptake [NiFe]-hydrogenases can supply enough energy for growth of otherwise heterotrophic bacteria, including *Sphingopyxis alaskensis*. The estimated H₂-derived cell-specific power was 5.4 × 10⁻¹³ W. Hydrogenase genes occurred across eight bacterial phyla and were expressed in ocean metatranscriptomes. (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 1-2)

### Boundaries

- **Versus chemolithoautotrophy:** both obtain energy from inorganic donors, but lithoautotrophs obtain biomass carbon primarily from CO₂/HCO₃⁻. Growth on H₂ plus CO₂ alone, for example, is not evidence for this trait. (zeng2021microorganismsfromdeepsea pages 9-11, zeng2021microorganismsfromdeepsea pages 12-13)
- **Versus chemoorganoheterotrophy:** if an organic compound supplies both electrons/energy and biomass carbon, the phenotype is organoheterotrophic unless an inorganic donor makes a demonstrated energetic contribution.
- **Versus mixotrophy:** “mixotrophy” is broader and inconsistently applied. It can include simultaneous organic-carbon assimilation and CO₂ fixation, or co-oxidation of organic and inorganic energy sources. Curate `METPO:1000648` only where organic carbon is the primary biomass source and inorganic oxidation contributes energy.
- **Maintenance versus growth:** CO oxidation is common, but the 2023 marine analysis concluded that CO generally supported survival during organic-carbon starvation, whereas H₂ produced enough power to support growth. CO oxidation alone should therefore not automatically imply lithoheterotrophic growth. (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 2-3)
- **Genotype versus phenotype:** `coxL`, hydrogenase, `sqr`, or `sox` genes indicate potential, not the complete trait. Expression, donor consumption, acceptor reduction, growth/yield, and organic-carbon assimilation provide stronger evidence.
- **Facultative status:** an organism can be lithoheterotrophic only under particular conditions and organoheterotrophic or lithoautotrophic under others. The graph should represent the assayed condition rather than impose an obligate lifestyle.

## 2. Candidate graph nodes

### Trait and process nodes

- lithoheterotrophic — **“METPO:1000648”**
- inorganic electron-donor oxidation
- organic-carbon assimilation
- aerobic respiration — `GO:0009060`
- nitrate respiration — `GO:0042126`
- denitrification — `GO:0019333`
- hydrogen oxidation
- carbon-monoxide oxidation
- sulfide oxidation
- thiosulfate oxidation
- acetate assimilation
- respiratory electron-transfer chain
- proton-motive-force generation
- ATP synthesis coupled to electron transport — `GO:0042773`
- cellular growth — `GO:0016049`

### Chemicals and environmental inputs

Conservative ChEBI candidates include:

- molecular hydrogen — `CHEBI:18276`
- carbon monoxide — `CHEBI:17245`
- carbon dioxide — `CHEBI:16526`
- dioxygen — `CHEBI:15379`
- nitrate — `CHEBI:17632`
- nitrite — `CHEBI:16301`
- hydrogen sulfide — `CHEBI:16136`
- thiosulfate — `CHEBI:26977`
- elemental sulfur — label-only pending choice of the intended sulfur allotrope/species
- iron(II) — `CHEBI:29033`
- acetate — `CHEBI:30089`
- glucose — `CHEBI:17234`
- dinitrogen — `CHEBI:17997`
- organic carbon / dissolved organic matter — label-only because these are material classes rather than single chemicals
- low-organic-carbon marine water, oxygen-minimum-zone water, sulfidic coastal water, wastewater biofilm, and hydrothermal-vent habitat — use ENVO terms only after checking the current ENVO release.

### Genes, proteins, enzymes, and complexes

- group 1 uptake [NiFe]-hydrogenase
- group 2a [NiFe]-hydrogenase
- hydrogenase large and small subunits — taxon-specific gene names should be retained where reported
- aerobic carbon-monoxide dehydrogenase, CoxMSL; `coxL` encodes its molybdenum-binding catalytic large subunit
- sulfide:quinone oxidoreductase — `sqr`, including `sqrA`/`sqrF` variants
- flavocytochrome-c sulfide dehydrogenase — `fccAB`
- Sox thiosulfate-oxidation system — `soxAXBYZ`; `soxCD` where complete oxidation is demonstrated
- respiratory nitrate reductase — `narG` complex
- periplasmic nitrate reductase — `napAB`
- cytochrome-cd₁ nitrite reductase — `nirS`
- nitric-oxide reductase — `norBC`
- nitrous-oxide reductase — `nosZ`, only when present and experimentally relevant
- terminal oxidases — CoxA/aa₃-type, CcoN/cbb₃-type, CydA/bd-type, and CyoA/bo₃-type candidates
- acetate permease — label-only unless the source gives a validated locus
- acetyl-CoA synthetase — `EC:6.2.1.1`
- NADH dehydrogenase/respiratory Complex I — `GO:0045271`
- succinate dehydrogenase/Complex II — `GO:0045273`
- ATP synthase — `GO:0045259`
- quinone pool, periplasm, cytoplasmic membrane, and cytoplasm as localization nodes

Exact UniProt, KEGG, Rhea, and MetaCyc accessions should be assigned only after selecting a strain and reaction direction. A gene symbol should not be treated as a universal protein identifier.

## 3. Recommended causal architecture

The graph should have a modular rather than donor-specific core:

> inorganic donor availability → donor-specific oxidoreductase activity → respiratory electron transfer → terminal-acceptor reduction → proton motive force/ATP production → energetic support of growth; in parallel, organic-carbon availability → transport → assimilation into biomass → lithoheterotrophic phenotype.

The strongest modules for initial curation are summarized below.

| Module | Causal chain | Strongest taxon/system | Evidence strength | Key DOI |
|---|---|---|---|---|
| H2 oxidation-driven lithoheterotrophy | H2 oxidation via uptake [NiFe]-hydrogenase → aerobic respiratory chain/O2 reduction → energy supports growth while organic carbon is used for biosynthesis | Marine bacteria; culture-validated in *Sphingopyxis alaskensis* and supported by ocean metagenomes/metatranscriptomes (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 1-2, lappan2023molecularhydrogenin pages 2-3, lappan2023molecularhydrogenin pages 17-18) | **Strong, experimentally validated** for trait-relevant module; multi-approach 2023 evidence | 10.1038/s41564-023-01322-0 |
| Sulfide oxidation + acetate assimilation + denitrification | Sulfide oxidation → nitrate reduction to N2 → acetate uptake/assimilation as main biomass carbon source; no substantial CO2 fixation | *Arcobacter peruensis* from sulfidic coastal waters (callbeck2019arcobacterperuensissp. pages 9-12) | **Strong, experimentally validated** by physiology, isotope labeling, and genome analysis | 10.1128/AEM.01344-19 |
| Sulfur oxidation module in wastewater Thiothrix | Reduced sulfur compounds/H2S oxidation via SQR, FccAB, Sox systems; nitrate or O2 can serve as electron acceptor; coupled to growth in organic-rich wastewater contexts | *Thiothrix* morphotype in wastewater systems and pangenome review (gureeva2024wastewatertreatmentwith pages 7-9, gureeva2024wastewatertreatmentwith pages 9-12, gureeva2024wastewatertreatmentwith pages 6-7, gureeva2024wastewatertreatmentwith pages 15-16) | **Moderate**: strong for sulfur-oxidation gene content and real-world implementation, but often genomic/review-level rather than direct trait-isolating experiments | 10.3390/ijms25169093 |
| CO oxidation caveat | CO oxidation via CoxL/CODH can provide energy, but in marine datasets mainly supports persistence/survival more than growth; lithoheterotrophic assignment can be context-dependent | Marine bacterioplankton and sponge-associated symbionts (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 2-3) | **Moderate to weak for core trait curation**: ecologically important but growth-support evidence is less direct than for H2 or sulfide systems | 10.1038/s41564-023-01322-0 |
| Fe(II)-based engineered lithoheterotrophy caveat | Fe(II) oxidation engineered to support lithoheterotrophic growth with glucose/organic carbon; demonstrates mechanism but in synthetic host/background | Engineered strain reported in existing evidence, not a native environmental lithoheterotroph system | **Weak for direct TraitMech core curation**: useful as mechanistic support, but taxon-engineered and assay-specific | 10.1038/s41598-021-81412-3 |


*Table: This table prioritizes mechanistic modules for TraitMech curation of lithoheterotrophy, distinguishing strong experimentally validated systems from genomic or assay-specific evidence. It is useful for deciding which causal chains are ready for conservative curation and which should remain flagged as caveats.*

## 4. Candidate evidence-backed causal edges

| # | Subject — predicate — object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | molecular hydrogen — **is oxidized by** — uptake [NiFe]-hydrogenase | DOI [10.1038/s41564-023-01322-0](https://doi.org/10.1038/s41564-023-01322-0), published 6 February 2023: marine bacteria consume H₂, with group 1 and group 2 uptake hydrogenases prevalent and expressed. (lappan2023molecularhydrogenin pages 1-2) | **Strong**, but hydrogenase group and organism should be recorded per assay/genome. |
| 2 | group 2a [NiFe]-hydrogenase activity — **enables** — aerobic H₂ consumption in *Sphingopyxis alaskensis* | Same DOI: the culture aerobically consumed H₂ through a group 2a [NiFe]-hydrogenase. (lappan2023molecularhydrogenin pages 6-7) | **Strong; taxon-specific.** Avoid generalizing group 2a dependence to all lithoheterotrophs. |
| 3 | H₂ oxidation — **supplies energy sufficient for** — bacterial growth | Same DOI: calculated power of 5.4 × 10⁻¹³ W per cell exceeded typical requirements of copiotrophic marine isolates. (lappan2023molecularhydrogenin pages 6-7) | **Strong for the tested marine systems.** “Sufficient for” is preferable to asserting all growth energy came from H₂. |
| 4 | dioxygen — **serves as terminal electron acceptor for** — aerobic H₂ oxidation | Same DOI: uptake hydrogenases were linked to aerobic respiratory-chain components, and axenic cultures consumed H₂ aerobically. (lappan2023molecularhydrogenin pages 1-2, lappan2023molecularhydrogenin pages 2-3) | **Strong/moderate.** Gene colocalization alone is weaker than culture physiology. |
| 5 | low primary production / increasing water depth — **increases ecological importance of** — H₂ oxidation capacity | Same DOI: hydrogen-oxidation capacity increased with depth and decreased with oxygen concentration. (lappan2023molecularhydrogenin pages 1-2) | **Context association, not universal causation.** Curate as environmental modulation only if the schema permits association edges. |
| 6 | dissolved sulfide — **is oxidized while coupled to** — nitrate reduction | DOI [10.1128/AEM.01344-19](https://doi.org/10.1128/AEM.01344-19), December 2019: *A. peruensis* coupled sulfide oxidation to complete denitrification. (callbeck2019arcobacterperuensissp. pages 9-12) | **Strong; taxon-specific.** |
| 7 | nitrate — **is reduced to** — dinitrogen | Same DOI: isotope and physiological experiments verified complete reduction of nitrate to N₂. (callbeck2019arcobacterperuensissp. pages 9-12) | **Strong.** Intermediate edges through nitrite/NO/N₂O require source-level confirmation before addition. |
| 8 | acetate — **is transported by** — high-affinity acetate permease | Same DOI: acetate uptake showed an apparent *K*m of 5.4 μM, and transporter genes were identified. (callbeck2019arcobacterperuensissp. pages 9-12) | **Strong for uptake phenotype; moderate for assigning a particular gene.** |
| 9 | acetate — **is activated by** — acetyl-CoA synthetase | Same DOI identified acetyl-CoA synthetase in the acetate-assimilation mechanism. (callbeck2019arcobacterperuensissp. pages 9-12) | **Moderate/strong; taxon-specific.** Curate the reaction only after verifying substrates/products in the full methods/genome annotation. |
| 10 | acetate assimilation — **provides biomass carbon for** — lithoheterotrophic growth | Same DOI: isotope labeling verified acetate assimilation, while substantial CO₂ fixation was absent. (callbeck2019arcobacterperuensissp. pages 9-12) | **Strong and trait-defining.** |
| 11 | sulfide oxidation plus acetate assimilation — **increases** — growth relative to CO₂ fixation alone | Same DOI: combined sulfide and acetate produced approximately twofold faster growth; yield was 3.1 mol C mol⁻¹ H₂S oxidized. (callbeck2019arcobacterperuensissp. pages 9-12) | **Strong but assay-specific.** Store values with units and conditions rather than as universal parameters. |
| 12 | absence of a complete autotrophic CO₂-fixation pathway — **supports classification as** — lithoheterotrophic rather than lithoautotrophic | Same DOI: genome and isotope experiments showed no meaningful autotrophic CO₂ fixation. (callbeck2019arcobacterperuensissp. pages 9-12) | **Supporting classification edge, not a biochemical cause.** Represent as evidence/constraint if allowed. |
| 13 | `sqrA`/`sqrF` — **encode catalysts of** — hydrogen-sulfide oxidation | DOI [10.3390/ijms25169093](https://doi.org/10.3390/ijms25169093), August 2024: the *Thiothrix* pangenome contains SQR systems for H₂S oxidation. (gureeva2024wastewatertreatmentwith pages 7-9) | **Moderate:** authoritative synthesis/pangenome evidence; validate expression and knockout effects before asserting necessity. |
| 14 | `fccAB` — **encode** — flavocytochrome-c sulfide dehydrogenase | Same DOI documents `fccAB` in *Thiothrix* sulfur metabolism. (gureeva2024wastewatertreatmentwith pages 7-9) | **Moderate, genomic.** Potential redundancy with SQR makes “required for” inappropriate. |
| 15 | `soxAXBYZ` — **enables** — thiosulfate oxidation | Same DOI documents the Sox system in the *Thiothrix* pangenome. (gureeva2024wastewatertreatmentwith pages 7-9) | **Moderate.** Species-level presence and pathway completeness must be checked. |
| 16 | `soxCD` — **promotes** — complete oxidation of stored/intermediate sulfur | In *A. peruensis*, `soxCD` was present and the organism lacked intracellular sulfur storage characteristic of some co-occurring sulfur oxidizers. (callbeck2019arcobacterperuensissp. pages 9-12) | **Moderate; taxon-specific inference.** Do not convert correlation into universal necessity. |
| 17 | reduced sulfur oxidation — **donates electrons to** — nitrate or oxygen respiration in *Thiothrix* systems | The 2024 review documents sulfur removal in reactors using nitrate or oxygen as acceptors. (gureeva2024wastewatertreatmentwith pages 7-9) | **Moderate and implementation-specific.** Split nitrate and oxygen modules in YAML. |
| 18 | `narG` or `napAB` — **catalyzes** — dissimilatory nitrate reduction | The *Thiothrix* pangenome contains respiratory nitrate-reductase systems, with species-dependent distributions. (gureeva2024wastewatertreatmentwith pages 15-16) | **Moderate, genomic.** Do not assert both systems occur in every species. |
| 19 | `nirS` — **catalyzes** — nitrite reduction in denitrification | `nirS` occurs among *Thiothrix* nitrogen-metabolism genes. (gureeva2024wastewatertreatmentwith pages 15-16) | **Moderate; genomic.** |
| 20 | `norBC` — **catalyzes** — nitric-oxide reduction in denitrification | `norBC` is reported in the *Thiothrix* pangenome. (gureeva2024wastewatertreatmentwith pages 15-16) | **Moderate; genomic.** Complete denitrification cannot be inferred without the remaining modules and phenotype. |
| 21 | lactate or acetate availability — **supports carbon assimilation during** — sulfur-oxidizing denitrifying growth | The 2024 review describes mixotrophic denitrification by *Thiothrix* with reduced sulfur plus lactate or acetate. (gureeva2024wastewatertreatmentwith pages 15-16) | **Moderate; species and assay dependent.** |
| 22 | intracellular sulfur oxidation — **supplies energy for** — phosphate uptake/removal | *Thiothrix caldifontis* can oxidize intracellular sulfur as an additional energy source in low-organic, reduced-sulfur-rich EBPR conditions. (gureeva2024wastewatertreatmentwith pages 9-12) | **Moderate; application-specific**, not necessary to the general trait. |
| 23 | CO — **is oxidized by** — CoxL-containing carbon-monoxide dehydrogenase | The 2023 marine study found CoxL widespread; approximately 25% of surface-water bacterial cells encoded CO dehydrogenases. (lappan2023molecularhydrogenin pages 2-3) | **Strong for genomic prevalence and CO oxidation potential; weak for growth causality.** |
| 24 | CO oxidation — **supports** — persistence during organic-carbon starvation | Same DOI concluded that CO mainly supports survival rather than growth. (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 2-3) | **Do not use as a core positive edge to growth.** It is an important negative boundary case. |
| 25 | respiratory electron transfer — **generates** — proton motive force | *Caldithrix abyssi* encodes hydrogenases, Complex I/II, Nap nitrate reductase, and a respiratory chain consistent with energy conservation. (kublanov2017genomicanalysisof pages 11-12) | **Mechanistically plausible but partly inferred.** This organism/source does not independently establish the complete target phenotype in the cited excerpt. |
| 26 | sulfide oxidation by facultative heterotrophic denitrifiers — **increases** — organic-carbon assimilation and denitrification | DOI [10.1038/s41467-025-56588-1](https://doi.org/10.1038/s41467-025-56588-1), January 2025: sulfide increased labeled organic-carbon assimilation by 64.1% in *Azoarcus* and 8.0% in *Pseudomonas*. (shao2025versatilenitraterespiringheterotrophs pages 1-2) | **Strong but post-priority-window (2025), taxon-specific.** Useful as confirmatory update rather than the sole support for a 2023–2024 report. |
| 27 | sulfur-oxidizing heterotrophic denitrification — **reduces** — N₂O emissions | Same 2025 study reported accelerated denitrification and substantially lower N₂O emissions in organic-rich and organic-limited incubations. (shao2025versatilenitraterespiringheterotrophs pages 1-2) | **Promising application edge**, but retain assay context and seek exact effect sizes before quantitative curation. |

## 5. Recent developments and real-world implementations

### 2023: trace H₂ as a growth-supporting energy source

The major recent conceptual advance is that lithoheterotrophy need not depend on high-energy geochemical settings. H₂ at environmentally relevant marine concentrations can support bacterial growth, and hydrogenase capacity is distributed across eight phyla. Surface waters were reported to be 2–5-fold supersaturated in H₂ relative to the atmosphere. In contrast, CO was 20–200-fold supersaturated and CoxL was widespread, but its main measured role was persistence rather than growth. This donor-specific distinction is important for causal curation. (lappan2023molecularhydrogenin pages 1-2, lappan2023molecularhydrogenin pages 2-3)

### 2024: pangenome-guided wastewater interpretation

The 2024 *Thiothrix* synthesis connects sulfur-oxidation genes to full-scale and engineered wastewater communities. These organisms occur in UASB reactors, fluidized-bed systems, and biodrainage filters, where reduced-sulfur oxidation can contribute to sulfide removal, denitrification, and phosphorus removal. *Thiothrix lacustris* accounted for 38% of 16S rRNA sequences in one H₂S-treatment filter. The same review reports functional fractions of 1.51% for phosphorus removal, 9.41% for nitrification–denitrification, and 4.29% for aerobic carbon removal in a surveyed context; these percentages should be stored with their original system definition, not generalized across treatment plants. (gureeva2024wastewatertreatmentwith pages 7-9)

A practical limitation is that excessive *Thiothrix*-morphotype proliferation can cause sludge bulking or membrane clogging, whereas controlled filamentous growth can improve granular-sludge structure and treatment performance. The application is therefore management of a context-dependent guild, not simply maximizing the trait. (gureeva2024wastewatertreatmentwith pages 6-7)

### Environmental implementations

- **Coastal oxygen-minimum zones:** sulfide oxidation coupled to denitrification and organic-carbon assimilation detoxifies sulfide and contributes to fixed-nitrogen loss. *Arcobacter* constituted 3–25% of cells at one Peruvian nearshore station; the chemocline exceeded 10⁶ cells ml⁻¹, with denitrification up to 6.5 ± 0.4 μM N day⁻¹ and dark carbon fixation of 2.8 ± 0.2 μM C day⁻¹. The isolate data showed, however, that *A. peruensis* itself assimilated acetate rather than substantially fixing CO₂. (callbeck2019arcobacterperuensissp. pages 9-12)
- **Low-productivity marine waters:** H₂ oxidation supplements limited organic-energy supply and becomes more prevalent with depth and lower oxygen availability. (lappan2023molecularhydrogenin pages 1-2)
- **Wastewater and sulfide control:** sulfur-oxidizing lithoheterotrophs can couple sulfide removal to oxygen or nitrate respiration and may contribute to denitrification and EBPR. (gureeva2024wastewatertreatmentwith pages 7-9, gureeva2024wastewatertreatmentwith pages 9-12, gureeva2024wastewatertreatmentwith pages 15-16)
- **Climate-relevant denitrification:** 2025 evidence suggests facultative sulfur-oxidizing heterotrophic denitrifiers can lower N₂O accumulation while maintaining denitrification under fluctuating organic-carbon availability. (shao2025versatilenitraterespiringheterotrophs pages 1-2)

## 6. Expert interpretation for TraitMech

The literature supports a **composite physiological trait**, not a single pathway. The invariant causal logic is energetic partitioning: inorganic oxidation contributes reducing power/ATP, while organic compounds dominate biomass carbon. Accordingly, a robust graph should contain interchangeable donor modules (H₂, sulfide/thiosulfate, potentially Fe(II) or CO), interchangeable acceptor modules (O₂, nitrate and its denitrification products), and an organic assimilation module.

The most defensible initial graph is a union of two experimentally strong systems:

1. **H₂ → uptake hydrogenase → aerobic respiratory chain → energy supporting growth**, with organic substrates supplying biomass carbon; and
2. **sulfide → sulfur-oxidation machinery → denitrification**, paired with **acetate uptake → acetyl-CoA → biomass**.

The *Thiothrix* pangenome then adds useful gene-level candidates, but gene presence should not be represented as sufficient for phenotype. CoxL/CO and engineered Fe(II) systems are better retained as optional, uncertain modules until growth and carbon-source partitioning are directly demonstrated.

## 7. Warnings: claims not yet ready for TraitMech curation

1. **Do not curate `coxL → lithoheterotrophic growth` as a universal edge.** CoxL is widespread, yet CO mainly supported survival in the strongest recent marine study. (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 2-3)
2. **Do not infer phenotype from a hydrogenase, `sqr`, `fccAB`, or `sox` gene alone.** Catalytic direction, maturation machinery, expression, electron acceptor, and physiological flux must be established.
3. **Do not treat “mixotrophic” as an exact synonym.** Some mixotrophs fix substantial CO₂ or oxidize organic substrates for energy, which falls outside the supplied definition.
4. **Do not make `narG`, `napAB`, `nirS`, `norBC`, and `nosZ` universally required.** Aerobic lithoheterotrophs do not require denitrification, and denitrifying taxa vary in pathway completeness. (gureeva2024wastewatertreatmentwith pages 15-16)
5. **Do not generalize taxon-specific kinetics or yields.** The 5.4 μM acetate *K*m, 3.1 mol C mol⁻¹ H₂S yield, and twofold growth effect belong to *A. peruensis* under particular conditions. (callbeck2019arcobacterperuensissp. pages 9-12)
6. **Do not curate predicted aerobic or sulfur respiration where experiments were negative.** In *C. abyssi*, some genome-predicted respiratory capacities were not physiologically confirmed. (kublanov2017genomicanalysisof pages 11-12)
7. **Engineered Fe(II) evidence is mechanistically useful but not proof of a natural general trait.** DOI [10.1038/s41598-021-81412-3](https://doi.org/10.1038/s41598-021-81412-3) should be tagged `engineered`, `assay-specific`, and `taxon-specific`; its exact gene-to-Fe(II)-oxidation chain should be extracted from the full article before adding gene-level edges.
8. **Avoid an unqualified “inorganic compound” node in executable reaction edges.** Instantiate the donor and its oxidation product whenever the source provides them.
9. **Environmental co-occurrence is not causation.** Depth, oxygen, sulfide, and organic-carbon correlations should be represented as contextual associations unless manipulated experimentally.
10. **The 2025 F-SOHD study is strong but outside the requested 2023–2024 priority window.** Use it as a recent confirmatory extension and preserve its enrichment/microcosm context. (shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2)

## 8. DOI-first bibliography

1. Lappan R. et al. “Molecular hydrogen in seawater supports growth of diverse marine bacteria.” *Nature Microbiology* 8, 581–595. **Published 6 February 2023.** DOI: [10.1038/s41564-023-01322-0](https://doi.org/10.1038/s41564-023-01322-0). (lappan2023molecularhydrogenin pages 6-7, lappan2023molecularhydrogenin pages 1-2)
2. Gureeva M.V. et al. “Wastewater Treatment with Bacterial Representatives of the Thiothrix Morphotype.” *International Journal of Molecular Sciences* 25, 9093. **Published August 2024.** DOI: [10.3390/ijms25169093](https://doi.org/10.3390/ijms25169093). (gureeva2024wastewatertreatmentwith pages 7-9, gureeva2024wastewatertreatmentwith pages 15-16)
3. Callbeck C.M. et al. “*Arcobacter peruensis* sp. nov., a Chemolithoheterotroph Isolated from Sulfide- and Organic-Rich Coastal Waters off Peru.” *Applied and Environmental Microbiology* 85. **Published December 2019.** DOI: [10.1128/AEM.01344-19](https://doi.org/10.1128/AEM.01344-19). (callbeck2019arcobacterperuensissp. pages 9-12)
4. Burgsdorf I. et al. “Lineage-specific energy and carbon metabolism of sponge symbionts and contributions to the host carbon pool.” *ISME Journal* 16, 1163–1175. **Published online December 2021; issue 2022.** DOI: [10.1038/s41396-021-01165-9](https://doi.org/10.1038/s41396-021-01165-9). This study identifies CO oxidation as a widespread potential energy source in sponge lithoheterotrophs while warning that genomic potential requires physiological validation.
5. Zeng X., Alain K., Shao Z. “Microorganisms from deep-sea hydrothermal vents.” *Marine Life Science & Technology* 3, 204–230. **Published January 2021.** DOI: [10.1007/s42995-020-00086-4](https://doi.org/10.1007/s42995-020-00086-4). (zeng2021microorganismsfromdeepsea pages 9-11, zeng2021microorganismsfromdeepsea pages 12-13)
6. Kublanov I.V. et al. “Genomic Analysis of *Caldithrix abyssi*.” *Frontiers in Microbiology* 8:195. **Published February 2017.** DOI: [10.3389/fmicb.2017.00195](https://doi.org/10.3389/fmicb.2017.00195). (kublanov2017genomicanalysisof pages 11-12)
7. Hooper A.B., DiSpirito A.A. “Chemolithotrophy.” In *Encyclopedia of Biological Chemistry*, pp. 486–492. **Published 2013.** DOI: [10.1016/B978-0-12-378630-2.00219-X](https://doi.org/10.1016/B978-0-12-378630-2.00219-X).
8. Shao B. et al. “Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle.” *Nature Communications* 16. **Published January 2025.** DOI: [10.1038/s41467-025-56588-1](https://doi.org/10.1038/s41467-025-56588-1). (shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2)
9. Existing engineered Fe(II) study. *Scientific Reports*. **Published 2021.** DOI: [10.1038/s41598-021-81412-3](https://doi.org/10.1038/s41598-021-81412-3). Treat as engineered, assay-specific evidence pending full-text verification of each molecular edge.

References

1. (callbeck2019arcobacterperuensissp. pages 9-12): Cameron M. Callbeck, Chris Pelzer, Gaute Lavik, Timothy G. Ferdelman, Jon S. Graf, Bram Vekeman, Harald Schunck, Sten Littmann, Bernhard M. Fuchs, Philipp F. Hach, Tim Kalvelage, Ruth A. Schmitz, and Marcel M. M. Kuypers. <i>arcobacter peruensis</i> sp. nov., a chemolithoheterotroph isolated from sulfide- and organic-rich coastal waters off peru. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01344-19, doi:10.1128/aem.01344-19. This article has 61 citations and is from a peer-reviewed journal.

2. (lappan2023molecularhydrogenin pages 6-7): Rachael Lappan, Guy Shelley, Zahra F. Islam, Pok Man Leung, Scott Lockwood, Philipp A. Nauer, Thanavit Jirapanjawat, Gaofeng Ni, Ya-Jou Chen, Adam J. Kessler, Timothy J. Williams, Ricardo Cavicchioli, Federico Baltar, Perran L. M. Cook, Sergio E. Morales, and Chris Greening. Molecular hydrogen in seawater supports growth of diverse marine bacteria. Nature Microbiology, 8:581-595, Feb 2023. URL: https://doi.org/10.1038/s41564-023-01322-0, doi:10.1038/s41564-023-01322-0. This article has 82 citations and is from a highest quality peer-reviewed journal.

3. (lappan2023molecularhydrogenin pages 1-2): Rachael Lappan, Guy Shelley, Zahra F. Islam, Pok Man Leung, Scott Lockwood, Philipp A. Nauer, Thanavit Jirapanjawat, Gaofeng Ni, Ya-Jou Chen, Adam J. Kessler, Timothy J. Williams, Ricardo Cavicchioli, Federico Baltar, Perran L. M. Cook, Sergio E. Morales, and Chris Greening. Molecular hydrogen in seawater supports growth of diverse marine bacteria. Nature Microbiology, 8:581-595, Feb 2023. URL: https://doi.org/10.1038/s41564-023-01322-0, doi:10.1038/s41564-023-01322-0. This article has 82 citations and is from a highest quality peer-reviewed journal.

4. (zeng2021microorganismsfromdeepsea pages 9-11): Xiang Zeng, Karine Alain, and Zongze Shao. Microorganisms from deep-sea hydrothermal vents. Marine Life Science & Technology, 3:204-230, Jan 2021. URL: https://doi.org/10.1007/s42995-020-00086-4, doi:10.1007/s42995-020-00086-4. This article has 120 citations and is from a peer-reviewed journal.

5. (zeng2021microorganismsfromdeepsea pages 12-13): Xiang Zeng, Karine Alain, and Zongze Shao. Microorganisms from deep-sea hydrothermal vents. Marine Life Science & Technology, 3:204-230, Jan 2021. URL: https://doi.org/10.1007/s42995-020-00086-4, doi:10.1007/s42995-020-00086-4. This article has 120 citations and is from a peer-reviewed journal.

6. (lappan2023molecularhydrogenin pages 2-3): Rachael Lappan, Guy Shelley, Zahra F. Islam, Pok Man Leung, Scott Lockwood, Philipp A. Nauer, Thanavit Jirapanjawat, Gaofeng Ni, Ya-Jou Chen, Adam J. Kessler, Timothy J. Williams, Ricardo Cavicchioli, Federico Baltar, Perran L. M. Cook, Sergio E. Morales, and Chris Greening. Molecular hydrogen in seawater supports growth of diverse marine bacteria. Nature Microbiology, 8:581-595, Feb 2023. URL: https://doi.org/10.1038/s41564-023-01322-0, doi:10.1038/s41564-023-01322-0. This article has 82 citations and is from a highest quality peer-reviewed journal.

7. (lappan2023molecularhydrogenin pages 17-18): Rachael Lappan, Guy Shelley, Zahra F. Islam, Pok Man Leung, Scott Lockwood, Philipp A. Nauer, Thanavit Jirapanjawat, Gaofeng Ni, Ya-Jou Chen, Adam J. Kessler, Timothy J. Williams, Ricardo Cavicchioli, Federico Baltar, Perran L. M. Cook, Sergio E. Morales, and Chris Greening. Molecular hydrogen in seawater supports growth of diverse marine bacteria. Nature Microbiology, 8:581-595, Feb 2023. URL: https://doi.org/10.1038/s41564-023-01322-0, doi:10.1038/s41564-023-01322-0. This article has 82 citations and is from a highest quality peer-reviewed journal.

8. (gureeva2024wastewatertreatmentwith pages 7-9): Maria V. Gureeva, Maria S. Muntyan, Nikolai V. Ravin, and Margarita Yu. Grabovich. Wastewater treatment with bacterial representatives of the thiothrix morphotype. International Journal of Molecular Sciences, 25:9093, Aug 2024. URL: https://doi.org/10.3390/ijms25169093, doi:10.3390/ijms25169093. This article has 14 citations.

9. (gureeva2024wastewatertreatmentwith pages 9-12): Maria V. Gureeva, Maria S. Muntyan, Nikolai V. Ravin, and Margarita Yu. Grabovich. Wastewater treatment with bacterial representatives of the thiothrix morphotype. International Journal of Molecular Sciences, 25:9093, Aug 2024. URL: https://doi.org/10.3390/ijms25169093, doi:10.3390/ijms25169093. This article has 14 citations.

10. (gureeva2024wastewatertreatmentwith pages 6-7): Maria V. Gureeva, Maria S. Muntyan, Nikolai V. Ravin, and Margarita Yu. Grabovich. Wastewater treatment with bacterial representatives of the thiothrix morphotype. International Journal of Molecular Sciences, 25:9093, Aug 2024. URL: https://doi.org/10.3390/ijms25169093, doi:10.3390/ijms25169093. This article has 14 citations.

11. (gureeva2024wastewatertreatmentwith pages 15-16): Maria V. Gureeva, Maria S. Muntyan, Nikolai V. Ravin, and Margarita Yu. Grabovich. Wastewater treatment with bacterial representatives of the thiothrix morphotype. International Journal of Molecular Sciences, 25:9093, Aug 2024. URL: https://doi.org/10.3390/ijms25169093, doi:10.3390/ijms25169093. This article has 14 citations.

12. (kublanov2017genomicanalysisof pages 11-12): Ilya V. Kublanov, Olga M. Sigalova, Sergey N. Gavrilov, Alexander V. Lebedinsky, Christian Rinke, Olga Kovaleva, Nikolai A. Chernyh, Natalia Ivanova, Chris Daum, T.B.K. Reddy, Hans-Peter Klenk, Stefan Spring, Markus Göker, Oleg N. Reva, Margarita L. Miroshnichenko, Nikos C. Kyrpides, Tanja Woyke, Mikhail S. Gelfand, and Elizaveta A. Bonch-Osmolovskaya. Genomic analysis of caldithrix abyssi, the thermophilic anaerobic bacterium of the novel bacterial phylum calditrichaeota. Frontiers in Microbiology, Feb 2017. URL: https://doi.org/10.3389/fmicb.2017.00195, doi:10.3389/fmicb.2017.00195. This article has 54 citations and is from a peer-reviewed journal.

13. (shao2025versatilenitraterespiringheterotrophs pages 1-2): Bo Shao, Yuan-Guo Xie, Long Zhang, Yang Ruan, Bin Liang, Ruochen Zhang, Xijun Xu, Wei Wang, Zhengda Lin, Xuanyuan Pei, Xueting Wang, Lei Zhao, Xu Zhou, Xiaohui Wu, Defeng Xing, Aijie Wang, Duu-Jong Lee, Nanqi Ren, Donald E. Canfield, Brian P. Hedlund, Zheng-Shuang Hua, and Chuan Chen. Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56588-1, doi:10.1038/s41467-025-56588-1. This article has 33 citations and is from a highest quality peer-reviewed journal.

14. (shao2025versatilenitraterespiringheterotrophs pages 4-4): Bo Shao, Yuan-Guo Xie, Long Zhang, Yang Ruan, Bin Liang, Ruochen Zhang, Xijun Xu, Wei Wang, Zhengda Lin, Xuanyuan Pei, Xueting Wang, Lei Zhao, Xu Zhou, Xiaohui Wu, Defeng Xing, Aijie Wang, Duu-Jong Lee, Nanqi Ren, Donald E. Canfield, Brian P. Hedlund, Zheng-Shuang Hua, and Chuan Chen. Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56588-1, doi:10.1038/s41467-025-56588-1. This article has 33 citations and is from a highest quality peer-reviewed journal.