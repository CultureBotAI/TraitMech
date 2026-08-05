---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:47:17.234454'
end_time: '2026-08-04T03:55:42.916910'
duration_seconds: 505.68
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum low
  trait_identifier: METPO:1000442
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 10 and 22 \xB0C, characteristic of psychrophilic or psychrotolerant\
    \ physiology."
  parent_traits: METPO:1000304
  synonyms: Psychrophile, Psychrotolerant, TO_10_to_22
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Psychrophile review supports low-but-not-freezing
    optima as the psychrophile / psychrotolerant category.)'
  causal_graph_summary: 'temperature_optimum_low_psychrotolerant_setpoint: 14 nodes,
    10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000442
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 10 and 22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, Psychrotolerant, TO_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports low-but-not-freezing optima as the psychrophile / psychrotolerant category.)
- **Existing causal graph summary:** temperature_optimum_low_psychrotolerant_setpoint: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_low.yaml`.

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
- **Trait label:** temperature optimum low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000442
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 10 and 22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Psychrophile, Psychrotolerant, TO_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports low-but-not-freezing optima as the psychrophile / psychrotolerant category.)
- **Existing causal graph summary:** temperature_optimum_low_psychrotolerant_setpoint: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_low.yaml`.

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


# Curation report: microbial “temperature optimum low”

## 1. Scope and curation interpretation

**Trait:** `METPO:1000442`  
**Label:** temperature optimum low  
**Parent:** `METPO:1000304`  
**Operational definition:** an experimentally measured optimum-growth temperature of approximately **10–22 °C**.

This trait should represent the **temperature at which growth rate or biomass production is maximal under a specified assay**, rather than mere survival, metabolic activity, or detectable growth at low temperature. Classical terminology overlaps only imperfectly: psychrophiles are commonly defined as having an optimum near or below 15 °C and a maximum near 20 °C, whereas psychrotrophs/psychrotolerants can grow near refrigeration temperature but generally have optima above 20 °C. Accordingly, “psychrophile” and “psychrotolerant” should be annotations or supporting classifications, not exact logical synonyms of `METPO:1000442`. (ramon2023ageneraloverview pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 2-3)

### Inclusion criteria

Curate the trait when a temperature-series growth assay places the optimum within approximately 10–22 °C. Suitable endpoints include maximum specific growth rate, shortest doubling time, colony expansion, or maximum biomass yield, provided the endpoint and medium are recorded.

### Boundary cases

- **Growth at 4 °C alone:** insufficient; many psychrotrophs grow at 4 °C but have optima above 22 °C.
- **Survival or metabolic activity below 0 °C:** not equivalent to a low optimum. For example, survival at −10 °C or activity at −20 °C does not establish where growth is optimal. (purwar2024adaptationsofpsychrophilic pages 3-4)
- **Cold-shock tolerance:** an acute response to a temperature downshift, not necessarily an evolved low-temperature optimum.
- **Enzyme temperature optimum:** a property of an isolated catalyst, not automatically the organismal growth optimum.
- **Maximum growth temperature:** should be recorded separately. *Methanogenium frigidum*, for example, has a reported optimum of 15 °C, maximum of 18 °C, and minimum of −2 °C; this is a clear organism-level example within the target class. (moyer2017psychrophilesandpsychrotrophs pages 3-5)
- **Freezing resistance:** antifreeze proteins and extracellular polymers may support survival near ice but do not by themselves establish a 10–22 °C optimum.

The most defensible graph endpoint is therefore:

> **coordinated maintenance of membrane transport, transcription, translation, protein folding, redox balance, and catalytic flux at low ambient temperature → increased growth performance at 10–22 °C → `METPO:1000442`.**

## 2. Current mechanistic understanding

Low-temperature growth is a systems phenotype rather than the product of a single “psychrophile gene.” Cooling rigidifies membranes, stabilizes inhibitory RNA/DNA secondary structures, slows enzyme reactions and macromolecular assembly, increases protein-folding demands, and can elevate oxidative stress. Cold-adapted microorganisms compensate through homeoviscous membrane remodeling, RNA chaperones and helicases, altered translation machinery, molecular chaperones, compatible solutes, antioxidant systems, extracellular cryoprotectants, and enzymes with high low-temperature catalytic efficiency. Recent reviews emphasize that these responses are coordinated and temperature-dependent rather than universal or identical across taxa. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 6-7)

A particularly useful 2023 result is the tiered response of *Pseudomonas fragi* D12. Following 30→15 °C cooling, genes associated with fatty-acid degradation, polysaccharides, pili, compatible solutes, and catalase increased. Following 15→4 °C cooling, unsaturated-fatty-acid synthesis genes, cold-shock proteins, helicases, and transcription-related genes predominated. Thus, moderate cooling and severe cold shock should not be collapsed into one graph state. (bao2023miningofkey pages 9-11)

## 3. Candidate nodes

### Trait and environmental nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| temperature optimum low | phenotype | `METPO:1000442` | Terminal trait node; quote CURIE verbatim. |
| low ambient temperature | environmental factor | Label-only unless the project has an approved ENVO temperature-quality term | Attach measured temperature and assay duration as edge qualifiers. |
| temperature downshift | experimental factor/process | Label-only | Distinguish 30→15 °C from 15→4 °C or acute cold shock. |
| microbial growth | biological process | `GO:0016049` | Prefer growth-rate or biomass endpoint where available. |
| cold acclimation | biological process | Label-only candidate | Do not equate with stable low optimum. |

### Cellular structures and physical-state nodes

| Candidate node | Type | Suggested grounding | Role |
|---|---|---|---|
| plasma membrane | cellular component | `GO:0005886` | Principal temperature-sensitive transport and energy-transduction interface. |
| membrane fluidity | cellular property | Label-only candidate | Mechanistic intermediate; avoid forcing an uncertain ontology ID. |
| ribosome | cellular component | `GO:0005840` | Translation machinery affected by cooling. |
| extracellular polymeric substance matrix | extracellular structure/material | Label-only candidate | Cryoprotection, adhesion, and local-environment stabilization. |
| biofilm | multicellular structure/process | `GO:0042710` for biofilm formation | Evidence is often indirect and taxon-specific. |

### Chemicals and metabolites

| Candidate node | Suggested grounding | Mechanistic interpretation |
|---|---|---|
| unsaturated fatty acid | `CHEBI:27208` | Increases lipid disorder and helps preserve membrane fluidity. |
| trehalose | `CHEBI:27082` | Compatible solute/cryoprotectant; transport and accumulation may stabilize cells. |
| glycine betaine | `CHEBI:17750` | Compatible solute supporting osmotic and cold protection. |
| ectoine | `CHEBI:42899` | Compatible solute implicated in bacterial cold protection. |
| reactive oxygen species | `CHEBI:26523` | Damaging redox intermediates whose burden may increase during cold stress. |
| oxygen | `CHEBI:15379` | Substrate for desaturation and source context for oxidative stress; relevance depends on taxon and pathway. |

*P. fragi* D12 literature additionally mentions glycine, mannitol, and sorbitol as candidate compatible solutes, but their specific contributions were not functionally separated and should remain lower-confidence nodes. (bao2023miningofkey pages 1-2)

### Genes, proteins, activities, and complexes

| Candidate node | Type/grounding | Evidence status |
|---|---|---|
| fatty-acid desaturase | `GO:0016717` may be used only when the annotated enzyme satisfies this activity | Strong general mechanism; individual genes require strain-specific annotation. |
| cold-shock protein CspA family | RNA chaperone; gene/protein family | Review and heterologous-expression support, but paralogs are not interchangeable. |
| RNA helicase | `GO:0003724` | Transcriptomic association in *P. fragi* D12; specific helicase should be identified before gene-level curation. |
| translation | `GO:0006412` | Downstream process restored during cold acclimation. |
| protein folding | `GO:0006457` | Chaperone-mediated maintenance process. |
| GroEL | chaperonin; preferably ground to a taxon-specific UniProt record | Direct heterologous-expression evidence from *Rhodococcus* RCBS9 study. |
| DPS | DNA-binding protein from starved cells; taxon-specific record needed | Direct heterologous-expression evidence, but exact source accession should be recovered from supplementary data. |
| USP-2 | universal stress protein; taxon-specific record needed | Direct heterologous-expression evidence. |
| small heat-shock protein | protein family; exact accession needed | Tested in the RCBS9 study, but growth response differed by construct/time. |
| catalase activity | `GO:0004096` | Antioxidant mechanism; *P. fragi* evidence is expression-associated. |
| superoxide dismutase activity | `GO:0004784` | General cold-stress antioxidant mechanism; not directly perturbed in the focal study. |
| antifreeze/ice-binding protein | `GO:0050825` for ice binding where applicable | Important near freezing, but peripheral to an optimum of 10–22 °C. |
| type 1 fimbria component D12GL002241 | strain-local gene label | Upregulated at 15 and 4 °C; causal role remains speculative. |
| PapD, D12GL002240 | strain-local gene label | Pilus-assembly chaperone; association only. |
| FimD/PapC, D12GL002239 | strain-local gene label | Outer-membrane usher; association only. |

### Pathways and modules

1. **Homeoviscous adaptation:** lipid desaturation, shorter acyl chains, and branched-chain fatty acids → membrane fluidity → transport and energy metabolism.
2. **RNA/translation maintenance:** cold-shock proteins and RNA helicases → reduced inhibitory RNA structure → translation recovery.
3. **Proteostasis:** GroEL and other chaperones → protein folding → low-temperature growth.
4. **Compatible-solute module:** synthesis/import of trehalose, betaine, or ectoine → macromolecular and membrane stabilization.
5. **Redox-protection module:** catalase/SOD → decreased ROS burden → lower cellular damage.
6. **Extracellular protection:** pili/adhesion → EPS or biofilm accumulation → local cryoprotection.
7. **Cold-active catalysis:** increased protein flexibility → high catalytic efficiency at low temperature, commonly with reduced thermostability. (moyer2017psychrophilesandpsychrotrophs pages 2-3, kuddus2024cold‐activemicrobialenzymes pages 2-4)

## 4. Candidate causal edges

The following compact artifact grades the principal edges by evidence type.

| subject | predicate | object | evidence strength | taxon/assay | DOI |
|---|---|---|---|---|---|
| low temperature decrease (30→15 °C; 15→4 °C) | upregulates / selects for | fatty-acid degradation at 30→15 °C, then unsaturated fatty-acid synthesis at 15→4 °C | omics association; moderate | *Pseudomonas fragi* D12 transcriptome after 2 h at 30, 15, 4 °C; authors infer stage-specific membrane adaptation (bao2023miningofkey pages 9-11) | 10.3389/fmicb.2023.1215837 |
| unsaturated fatty acids / lipid desaturation | increases | membrane fluidity | review synthesis plus organismal association; moderate | Foundational psychrophile/psychrotroph physiology; multiple taxa, not a single perturbation test (moyer2017psychrophilesandpsychrotrophs pages 3-5, moyer2017psychrophilesandpsychrotrophs pages 2-3) | 10.1016/b978-0-12-809633-8.02282-2 |
| low temperature (15→4 °C) | upregulates | cold shock proteins, helicases, and transcription molecules | omics association; moderate | *Pseudomonas fragi* D12 transcriptome; low-temperature shift (bao2023miningofkey pages 9-11) | 10.3389/fmicb.2023.1215837 |
| cold shock proteins / RNA helicases | supports restoration of | transcription and translation under low temperature | inferred mechanistic edge from omics plus expert review; moderate/uncertain | *P. fragi* D12 authors state bacteria must restore normal transcription/translation; broad bacterial cold-shock literature cited in study (bao2023miningofkey pages 11-13, grigorov2023dynamictranscriptionallandscape pages 15-16) | 10.3389/fmicb.2023.1215837 |
| compatible solutes (trehalose, betaine, mannitol, sorbitol, glycine) | stabilizes intracellular environment and promotes | low-temperature growth/adaptation | omics/physiology association; moderate | *P. fragi* D12, 30→15 °C response; no direct knockout in this study (bao2023miningofkey pages 1-2, bao2023miningofkey pages 9-11) | 10.3389/fmicb.2023.1215837 |
| catalase / superoxide dismutase | lowers | reactive oxygen species burden under cold stress | review-backed association; moderate | Reported as antioxidant enzymes used by cold-tolerant microbes; in *P. fragi* D12 catalase-associated genes rise at 30→15 °C (bao2023miningofkey pages 1-2, bao2023miningofkey pages 9-11) | 10.3389/fmicb.2023.1215837 |
| extracellular polymers / biofilm-associated pili | provides | cryoprotection and extracellular-environment stability | omics association; moderate/uncertain | *P. fragi* D12: pilus genes upregulated; authors speculate enhanced adhesion/EPS lowers freezing point and stabilizes environment (bao2023miningofkey pages 11-13, bao2023miningofkey pages 9-11) | 10.3389/fmicb.2023.1215837 |
| GroEL overexpression | improves | *E. coli* growth at 10 °C | functional heterologous-expression test; strong | Recombinant *E. coli* BL21 expressing RCBS9 genes; OD600 of control stayed ~1.0–1.1, recombinant strains peaked ~1.4 at 4 h at 10 °C (li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| DPS overexpression | improves | *E. coli* growth at 10 °C | functional heterologous-expression test; strong | Recombinant *E. coli* BL21 at 10 °C, same assay as above (li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| USP-2 overexpression | improves | *E. coli* growth at 10 °C | functional heterologous-expression test; strong | Recombinant *E. coli* BL21 at 10 °C, same assay as above (li2024mechanismsunderlyingthe pages 12-13) | 10.3389/fmicb.2024.1465627 |
| cold-active enzyme structural flexibility | increases | catalytic activity at low temperature | expert review/general mechanism; moderate | 2024 review of cold-active microbial enzymes; broad industrial enzyme literature, not a single microbial perturbation assay (kuddus2024cold‐activemicrobialenzymes pages 2-4) | 10.1111/1751-7915.14467 |


*Table: This table summarizes the strongest curation-ready candidate edges for METPO:1000442, separating broad omics associations from direct functional tests. It is useful as a compact starting point for TraitMech YAML curation while highlighting which claims still need stronger causal validation.*

A more curation-specific rendering follows. “Strong” denotes a direct functional test; “moderate” denotes consistent physiological or multi-omics evidence; “uncertain” denotes author inference, review-level synthesis, or missing perturbation evidence.

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| low temperature | increases | membrane lipid desaturation/unsaturated fatty acids | Moyer et al.: decreasing culture temperature increases (poly)unsaturated lipids; desaturation is described as the primary adaptive response. DOI: [10.1016/B978-0-12-809633-8.02282-2](https://doi.org/10.1016/B978-0-12-809633-8.02282-2), January 2017. (moyer2017psychrophilesandpsychrotrophs pages 3-5) | **Moderate, broad physiology.** Direction is well supported, but not every taxon uses the same lipid response. |
| unsaturated fatty acids | increase/maintain | membrane fluidity | The same synthesis reports higher 16:1 and 18:1 proportions in psychrophiles and links cooling-induced unsaturation to membrane-fluidity maintenance. (moyer2017psychrophilesandpsychrotrophs pages 3-5) | **Moderate.** Suitable as a central mechanistic edge; retain taxon and oxygen dependence. |
| membrane fluidity | enables | nutrient/material transport and low-temperature growth | Membrane homeophasic adaptation is described as enabling nutrient transport at low temperature, with the membrane considered a principal thermal-damage site. (moyer2017psychrophilesandpsychrotrophs pages 2-3) | **Moderate.** The final edge to `METPO:1000442` remains phenotype-level inference unless optimum shifts are measured. |
| 30→15 °C downshift | upregulates | fatty-acid degradation, polysaccharide, compatible-solute, pilus, and catalase genes | “When the temperature decreased from 30°C to 15°C…the up-regulated genes were associated with fatty acid degradation, polysaccharides, pilin, compatible solutes, and catalase.” DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837), July 2023. (bao2023miningofkey pages 9-11) | **Moderate association; *P. fragi* D12-specific.** Assay used 2 h at each temperature. |
| 15→4 °C downshift | upregulates | unsaturated-fatty-acid synthesis genes | “Crucial genes involved in unsaturated fatty acid synthesis were up-regulated.” (bao2023miningofkey pages 9-11) | **Moderate association.** Do not curate as proof that these genes set the organism’s optimum. |
| 15→4 °C downshift | upregulates | cold-shock proteins, helicases, and transcription-related genes | “The majority of genes associated with cold shock proteins, helicases, and transcription molecules were up-regulated.” (bao2023miningofkey pages 9-11) | **Moderate association.** Specific gene identities should be recovered before gene-level YAML entries. |
| cold-shock protein/RNA chaperone activity | promotes | low-temperature transcription and translation | Cold-shock proteins function as RNA chaperones; heterologous *cspA* expression has been reported to enhance low-temperature growth. DOI: [10.52679/tabcj.2023.0006](https://doi.org/10.52679/tabcj.2023.0006), June 2023. (gupta2023psychrophilesasa pages 9-10) | **Moderate-to-strong but secondary-source evidence.** Retrieve the original *cspA* experiment before asserting a universal edge. |
| GroEL overexpression | increases | growth at 10 °C | Recombinant *E. coli* BL21-GroEL reached approximately OD600 1.4 at 4 h, whereas control BL21-pET28a remained approximately 1.0–1.1 at 10 °C. DOI: [10.3389/fmicb.2024.1465627](https://doi.org/10.3389/fmicb.2024.1465627), November 2024. (li2024mechanismsunderlyingthe pages 12-13) | **Strong functional evidence**, but heterologous and short-term. Curate as “promotes growth at 10 °C,” not “causes a low optimum.” |
| DPS overexpression | increases | growth at 10 °C | BL21-DPS likewise reached approximately OD600 1.4 at 4 h under the 10 °C assay. (li2024mechanismsunderlyingthe pages 12-13) | **Strong, heterologous and taxon-specific.** Exact RCBS9 accession is needed. |
| USP-2 overexpression | increases | growth at 10 °C | BL21-USP-2 reached approximately OD600 1.4 at 4 h at 10 °C. (li2024mechanismsunderlyingthe pages 12-13) | **Strong, heterologous and taxon-specific.** |
| compatible-solute accumulation | stabilizes | intracellular environment under cooling | *P. fragi* D12 increased compatible-solute-associated expression during 30→15 °C cooling; reported candidates include glycine, betaine, trehalose, mannitol, and sorbitol. (bao2023miningofkey pages 1-2, bao2023miningofkey pages 9-11) | **Moderate association.** Prefer separate edges only after metabolite measurements or transporter/synthesis perturbations. |
| catalase/SOD activity | decreases | cold-associated ROS burden | The study associates catalase induction with intracellular stability, while catalase and SOD are described as defenses against cold-associated oxidative damage. (bao2023miningofkey pages 1-2, bao2023miningofkey pages 9-11) | **Moderate/uncertain.** Catalase expression was measured; ROS reduction was not established by a gene knockout in this experiment. |
| D12GL002241/PapD/FimD-PapC induction | increases | adhesion/pilus assembly | All three genes were significantly upregulated at 15 and 4 °C; the authors infer enhanced adhesion and extracellular-polymer production. (bao2023miningofkey pages 9-11) | **Uncertain.** Curate induction edges, but not pilus→cold optimum or pilus→EPS causality yet. |
| extracellular polymeric substances | provide | cryoprotection/local-environment stabilization | EPS are described as lowering the surrounding freezing point and protecting extracellular enzymes. (bao2023miningofkey pages 1-2) | **Moderate review/physiological support.** More relevant near freezing than at 10–22 °C. |
| antifreeze/ice-binding protein | inhibits | ice-crystal growth or recrystallization | IBPs bind ice surfaces, while antifreeze proteins can depress freezing point by more than 2 °C. (purwar2024adaptationsofpsychrophilic pages 6-7, moyer2017psychrophilesandpsychrotrophs pages 2-3) | **Mechanistically supported but peripheral.** Do not connect directly to the target optimum without organismal growth evidence. |
| cold-active enzyme flexibility | increases | low-temperature catalytic efficiency | The 2024 review describes high catalytic efficiency and flexibility at low temperature, frequently accompanied by low thermal stability. DOI: [10.1111/1751-7915.14467](https://doi.org/10.1111/1751-7915.14467), April 2024. (kuddus2024cold‐activemicrobialenzymes pages 2-4) | **Moderate general mechanism.** Enzyme activity is not equivalent to organismal optimum. |
| coordinated cold-adaptation modules | promote | growth between approximately 10 and 22 °C | Systems-level synthesis across membrane, translation, proteostasis, solute, and redox responses. (ramon2023ageneraloverview pages 1-2) | **Inferred integrative edge.** Appropriate as a high-level graph summary, not a directly measured molecular interaction. |

## 5. Quantitative evidence and recent developments

### *Pseudomonas fragi* D12, 2023

Whole-genome and transcriptome analysis identified **124 potential cold-adaptation genes**, including **19 strain-unique candidates**. The genome contained **46 genes associated with membrane fluidity**—four assigned to unsaturated-fatty-acid synthesis and 42 to fatty-acid degradation—and 233 genes broadly assigned to stress responses. These are annotation counts, not 124 independently validated causes. (bao2023miningofkey pages 6-7)

RNA-seq used a greater-than-twofold-change and q≤0.05 threshold after 2 h at 30, 15, or 4 °C. Relative to 30 °C, the 15 °C condition yielded 750 upregulated and 542 downregulated genes. Comparing 4 with 15 °C yielded 1,003 upregulated and 1,088 downregulated genes. The large, temperature-specific response supports a modular graph rather than a single linear pathway. (bao2023miningofkey pages 9-11)

### *Rhodococcus* sp. RCBS9, 2024

The clearest recent functional result is the expression of six RCBS9 candidate proteins in *E. coli* BL21. At 10 °C, the empty-vector control remained near OD600 1.0–1.1, whereas DPS-, GroEL-, and USP-2-expressing cultures peaked near OD600 1.4 at 4 h. This establishes that several individual proteins can improve short-term growth performance at 10 °C in a heterologous host. It does **not** show that they shift the optimum into the 10–22 °C interval. (li2024mechanismsunderlyingthe pages 12-13)

RCBS9 also upregulated the sensor/regulator DesK, global transcription factors, HSPs, USPs, transporters, and fatty-acid catabolism under cold stress. Those results imply a strain-specific strategy that differs from the canonical assumption that cold-shock proteins always dominate. (li2024mechanismsunderlyingthe pages 12-13)

### *Pseudomonas sivasensis* W-6, 2023

W-6 was cultivated at 15 °C for genome preparation and was interpreted as showing psychrophilic rather than psychrotrophic characteristics. Its proposed mechanisms include unsaturated-fatty-acid remodeling, two-component systems, antisense transcription, and the ribosomal protein gene *rpsU*. Because the cited work is predominantly genome-based, these should be candidate nodes rather than asserted causal edges. DOI: [10.1038/s41598-023-41323-x](https://doi.org/10.1038/s41598-023-41323-x), accepted 24 August 2023. (xiong2023wholegenomeanalysis pages 9-10)

### Expert assessment

Recent authoritative reviews converge on a **multifactorial model**: no isolated marker reliably predicts a low organismal optimum across bacteria, archaea, fungi, and microalgae. The strongest broadly reusable core is membrane homeoviscous adaptation plus maintenance of RNA, translation, protein folding, and catalytic activity. EPS, antifreeze proteins, pigments, and biofilms are important in particular habitats but should generally be modeled as optional branches. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)

## 6. Applications and real-world relevance

Cold-adapted microorganisms and enzymes are being investigated or used in:

- **Refrigerated dairy processing:** cold-active β-galactosidase can hydrolyze lactose without warming milk. One summarized enzyme digested more than 80% of raw-milk lactose at 20 °C and pH 6.5. (kuddus2024cold‐activemicrobialenzymes pages 2-4)
- **Food processing and detergents:** cold-active amylases, proteases, lipases, cellulases, and pectinases enable reactions at lower process temperatures.
- **Cold-region bioremediation and wastewater treatment:** low-temperature catalytic activity can sustain contaminant degradation where mesophilic processes are slow.
- **Textiles, leather, biopulping, and biotransformation:** lower-temperature enzymes can reduce heating requirements and protect temperature-sensitive products.
- **Molecular biology:** cold-adapted ligases, polymerases, and other enzymes offer altered temperature windows and easier thermal inactivation.

The 2024 review describes applications across food, detergent, textile, wastewater, biopulping, bioremediation, and molecular biology, but anticipated energy savings should not be recorded as a biological causal edge unless a process-level life-cycle or energy comparison is available. (kuddus2024cold‐activemicrobialenzymes pages 14-15, kuddus2024cold‐activemicrobialenzymes pages 2-4)

A commonly repeated estimate is that cold habitats constitute approximately **85% of Earth’s biosphere/surface environments**. This is useful context for ecological and biotechnological importance, but it is a broad review estimate rather than a trait-prevalence statistic. (kuddus2024cold‐activemicrobialenzymes pages 2-4)

## 7. Recommended initial TraitMech subgraph

The following compact structure is defensible for an initial YAML revision:

1. **low ambient temperature** → `induces` → **membrane lipid remodeling**
2. **membrane lipid remodeling** → `increases_or_maintains` → **membrane fluidity**
3. **membrane fluidity** → `supports` → **membrane transport and energy metabolism**
4. **low ambient temperature** → `induces` → **cold-shock proteins/RNA helicases**
5. **cold-shock proteins/RNA helicases** → `supports` → **transcription and translation at low temperature**
6. **low ambient temperature** → `induces` → **molecular chaperones**
7. **molecular chaperones** → `supports` → **protein folding at low temperature**
8. **compatible-solute accumulation** → `stabilizes` → **intracellular macromolecules and membranes**
9. **catalase/SOD activity** → `decreases` → **ROS burden**
10. **cold-active enzyme flexibility** → `increases` → **low-temperature catalytic flux**
11. **combined transport, translation, proteostasis, redox, and catalytic maintenance** → `promotes` → **growth performance at 10–22 °C**
12. **growth optimum measured at 10–22 °C** → `has_trait` → **`METPO:1000442`**

Edges 1–10 describe mechanisms supporting low-temperature growth. Edge 12 is the actual phenotype assignment and should require direct growth-temperature data.

## 8. Warnings: claims not ready for TraitMech

1. **Do not curate “psychrotroph → `METPO:1000442`.”** Psychrotrophs commonly have optima above the target interval despite growing at 4 °C.
2. **Do not infer an organismal optimum from one low-temperature growth point.** A temperature-response curve is required.
3. **Do not equate cold-shock induction with constitutive psychrophily.** Acute acclimation and evolutionary adaptation are different processes.
4. **Do not treat every upregulated gene as causal.** Most 2023 *P. fragi* edges are transcriptomic associations.
5. **Do not curate the D12 pilus genes as causing EPS production or a low optimum.** The authors explicitly frame this route as speculation and future work. (bao2023miningofkey pages 11-13, bao2023miningofkey pages 9-11)
6. **Do not generalize RCBS9 heterologous-expression effects to all taxa.** These experiments show improved *E. coli* growth at 10 °C, not a shifted temperature optimum. (li2024mechanismsunderlyingthe pages 12-13)
7. **Do not collapse all compatible solutes into one node.** Trehalose, glycine betaine, ectoine, mannitol, and sorbitol have distinct biosynthesis, transport, and regulatory systems.
8. **Do not make antifreeze proteins obligatory.** They are most relevant in ice-containing environments and may be absent from organisms whose optimum is 15–22 °C.
9. **Do not infer enzyme flexibility from taxonomic identity.** Cold-active enzymes vary, and some combine cold activity with appreciable thermal stability. (kuddus2024cold‐activemicrobialenzymes pages 2-4)
10. **Do not assign gene-family CURIEs without sequence verification.** Desaturases, CSPs, helicases, USPs, and small HSPs contain functionally heterogeneous members.

## 9. DOI-first bibliography

1. **Li Q. et al.** “Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain *Rhodococcus* sp. RCBS9.” *Frontiers in Microbiology* 15. **November 2024.** DOI: [10.3389/fmicb.2024.1465627](https://doi.org/10.3389/fmicb.2024.1465627). Functional heterologous-expression evidence. (li2024mechanismsunderlyingthe pages 12-13)
2. **Kuddus M. et al.** “Cold-active microbial enzymes and their biotechnological applications.” *Microbial Biotechnology* 17. **April 2024.** DOI: [10.1111/1751-7915.14467](https://doi.org/10.1111/1751-7915.14467). (kuddus2024cold‐activemicrobialenzymes pages 2-4)
3. **Purwar S., Srivastava S.** “Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.” *Applied Microbiology: Theory & Technology*, 168–188. **October 2024.** DOI: [10.37256/amtt.5220244537](https://doi.org/10.37256/amtt.5220244537). (purwar2024adaptationsofpsychrophilic pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7)
4. **Bao C. et al.** “Mining of key genes for cold adaptation from *Pseudomonas fragi* D12 and analysis of its cold-adaptation mechanism.” *Frontiers in Microbiology* 14. **July 2023.** DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837). (bao2023miningofkey pages 9-11)
5. **Ramón A. et al.** “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology* 54:2259–2287. **July 2023.** DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4). (ramon2023ageneraloverview pages 1-2)
6. **Xiong L. et al.** “Whole genome analysis and cold adaptation strategies of *Pseudomonas sivasensis* W-6 isolated from the Napahai plateau wetland.” *Scientific Reports* 13:14190. **August 2023.** DOI: [10.1038/s41598-023-41323-x](https://doi.org/10.1038/s41598-023-41323-x). (xiong2023wholegenomeanalysis pages 9-10)
7. **Gupta V. et al.** “Psychrophiles as a novel and promising source of cold-adapted industrial enzymes.” *Applied Biology & Chemistry Journal*, 54–68. **June 2023.** DOI: [10.52679/tabcj.2023.0006](https://doi.org/10.52679/tabcj.2023.0006). (gupta2023psychrophilesasa pages 9-10)
8. **Moyer C.L., Collins R.E., Morita R.Y.** “Psychrophiles and Psychrotrophs.” *Reference Module in Life Sciences*. **January 2017.** DOI: [10.1016/B978-0-12-809633-8.02282-2](https://doi.org/10.1016/B978-0-12-809633-8.02282-2). Foundational definitions and physiology. (moyer2017psychrophilesandpsychrotrophs pages 2-3, moyer2017psychrophilesandpsychrotrophs pages 3-5)

Overall, the strongest curation strategy is to retain `METPO:1000442` as an assay-defined organismal endpoint and connect it to a modular, evidence-graded mechanism. Membrane homeoviscous adaptation is the most broadly supported core, while the 2024 RCBS9 GroEL, DPS, and USP-2 experiments provide unusually direct—although heterologous—evidence for individual protein contributions to growth at 10 °C.

References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

2. (moyer2017psychrophilesandpsychrotrophs pages 2-3): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.

3. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

4. (moyer2017psychrophilesandpsychrotrophs pages 3-5): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.

5. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

6. (bao2023miningofkey pages 9-11): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

7. (bao2023miningofkey pages 1-2): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

8. (kuddus2024cold‐activemicrobialenzymes pages 2-4): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 63 citations and is from a peer-reviewed journal.

9. (bao2023miningofkey pages 11-13): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

10. (grigorov2023dynamictranscriptionallandscape pages 15-16): Artem S. Grigorov, Yulia V. Skvortsova, Oksana S. Bychenko, Leonid V. Aseev, Ludmila S. Koledinskaya, Irina V. Boni, and Tatyana L. Azhikina. Dynamic transcriptional landscape of mycobacterium smegmatis under cold stress. International Journal of Molecular Sciences, 24:12706, Aug 2023. URL: https://doi.org/10.3390/ijms241612706, doi:10.3390/ijms241612706. This article has 7 citations.

11. (li2024mechanismsunderlyingthe pages 12-13): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 9 citations and is from a peer-reviewed journal.

12. (gupta2023psychrophilesasa pages 9-10): Varsha Gupta, Pranav Bhaskar, Jeancolar Thoudam, Shiwali Bisht, Anita Sharma, and Rashmi Tripathi. Psychrophiles as a novel and promising source of cold-adapted industrial enzymes. The Applied Biology &amp; Chemistry Journal, pages 54-68, Jun 2023. URL: https://doi.org/10.52679/tabcj.2023.0006, doi:10.52679/tabcj.2023.0006. This article has 10 citations.

13. (bao2023miningofkey pages 6-7): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

14. (xiong2023wholegenomeanalysis pages 9-10): Lingling Xiong, Yanmei Li, Hang Yu, Yunlin Wei, Haiyan Li, and Xiuling Ji. Whole genome analysis and cold adaptation strategies of pseudomonas sivasensis w-6 isolated from the napahai plateau wetland. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41323-x, doi:10.1038/s41598-023-41323-x. This article has 13 citations and is from a peer-reviewed journal.

15. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

16. (kuddus2024cold‐activemicrobialenzymes pages 14-15): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 63 citations and is from a peer-reviewed journal.