---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T12:03:46.994571'
end_time: '2026-08-04T12:11:30.312862'
duration_seconds: 463.32
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: trophic type
  trait_identifier: METPO:1000631
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: trophic_type
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that is describing how an organism obtains carbon, energy,
    and electron donors for growth and metabolism.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.nutrition type.type, nutritional type, pathways
  evidence_summary: 'DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy
    source, and electron donor (Microbial physiology review frames trophic type as
    the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106:
    molecular mechanisms of adaptation (Comparative genomics supports the classification
    of bacteria by trophic strategy from genome-encoded pathways.)'
  causal_graph_summary: 'trophic_type_classification_axes: 14 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** trophic type
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000631
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is describing how an organism obtains carbon, energy, and electron donors for growth and metabolism.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.nutrition type.type, nutritional type, pathways
- **Existing evidence:** DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy source, and electron donor (Microbial physiology review frames trophic type as the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106: molecular mechanisms of adaptation (Comparative genomics supports the classification of bacteria by trophic strategy from genome-encoded pathways.)
- **Existing causal graph summary:** trophic_type_classification_axes: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **trophic type** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/trophic_type.yaml`.

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
- **Trait label:** trophic type
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000631
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is describing how an organism obtains carbon, energy, and electron donors for growth and metabolism.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.nutrition type.type, nutritional type, pathways
- **Existing evidence:** DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy source, and electron donor (Microbial physiology review frames trophic type as the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106: molecular mechanisms of adaptation (Comparative genomics supports the classification of bacteria by trophic strategy from genome-encoded pathways.)
- **Existing causal graph summary:** trophic_type_classification_axes: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **trophic type** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/trophic_type.yaml`.

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


# Curation report: microbial trophic type

**Target trait:** `METPO:1000631` — **trophic type**  
**Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** `METPO:1000059`

## 1. Scope summary

Trophic type is a **composite physiological classification** describing how an organism obtains (i) energy, (ii) electrons/reducing power, and (iii) carbon for growth. The conventional axes are:

- **Energy:** light → *phototroph*; chemical reactions → *chemotroph*.
- **Electron donor:** inorganic donor → *lithotroph*; organic donor → *organotroph*.
- **Carbon:** inorganic carbon, principally CO₂/DIC → *autotroph*; preformed organic carbon → *heterotroph*.

These axes combine into labels such as *photolithoautotroph*, *photoorganoheterotroph*, *chemolithoautotroph*, and *chemoorganoheterotroph*. For example, nitrifiers are classically chemolithoautotrophic, while purple sulfur bacteria can be anoxygenic photolithoautotrophs using light, H₂S, and CO₂. Purple nonsulfur bacteria often exhibit photoorganoheterotrophy and considerable trophic flexibility. (weissbrodt2023basicmicrobiologyand pages 19-22)

**Recommended interpretation for TraitMech:** the phenotype should represent an organism’s **demonstrated or condition-qualified trophic mode**, not merely the presence of one pathway marker. The causal graph should therefore connect environmental resources through uptake and energy-conservation modules to carbon assimilation and growth.

### Boundaries and nearby traits

1. **Respiration type is related but distinct.** O₂, nitrate, sulfate, and other terminal acceptors determine respiratory mode and energetic feasibility, but they do not replace the three primary trophic naming axes. They should enter the graph as environmental/chemical determinants of a condition-specific trophic phenotype. Redox zones create niches for different trophic guilds. (weissbrodt2023basicmicrobiologyand pages 19-22)
2. **Substrate utilization is narrower.** Growth on acetate or H₂ is evidence for a trophic component, but a complete classification also requires carbon-source and energy-source interpretation.
3. **Carbon fixation is not sufficient evidence of obligate autotrophy.** Organisms may express carbon-fixation pathways while also assimilating organics; *Leptothrix ochracea* and marine Arcobacteraceae illustrate this mixotrophic boundary. (tothero2024leptothrixochraceagenomes pages 1-2, li2024arcobacteraceaeareubiquitous pages 1-2)
4. **Mixotrophy is not one uniform mechanism.** It can mean simultaneous or condition-dependent combination of autotrophic and heterotrophic nutrition. In protists, constitutive mixotrophs possess photosystems, whereas non-constitutive mixotrophs acquire photosynthetic capacity from prey through kleptoplasty. (schenone2024mixotrophicprotistsand pages 2-3)
5. **Genetic potential is not the same as phenotype.** MAG pathway completeness, transcription, isotope incorporation, and growth assays provide progressively different evidence. Even transcript abundance is normally a proxy for potential activity rather than direct flux. (li2024insitucommunity pages 1-2)
6. **Ecological “trophic level” or food-web position is out of scope.** `METPO:1000631` concerns nutritional physiology, not predator–prey rank.

## 2. Candidate causal-graph nodes

Identifiers below are limited to stable CURIEs that can be assigned confidently. Candidate labels without a CURIE should remain label-only until ontology validation.

### A. Trait and trophic-state nodes

- `METPO:1000631` — trophic type
- phototrophy; chemotrophy
- lithotrophy; organotrophy
- autotrophy; heterotrophy; mixotrophy
- photolithoautotrophy; photoorganoheterotrophy
- chemolithoautotrophy; chemoorganoheterotrophy
- photoferrotrophy; photohydrogenotrophy; photoelectrotrophy
- condition-dependent trophic switching

### B. Environmental and experimental nodes

- light availability
- oxic, hypoxic, anoxic, and dark conditions
- organic-carbon availability
- electron-donor availability
- hypersaline sediment; deep groundwater; marine water column; wetland iron mat
- growth medium with H₂/CO₂/O₂, formate, succinate, fructose, Fe(II), sulfide, thiosulfate, or butyrate
- RB-TnSeq/barcoded transposon fitness assay
- stable-isotope carbon incorporation
- metagenomics, metatranscriptomics, and metabolic modeling

Deep aquifers exemplify environmental control: nine wells reached depths up to 1.5 km and contained hypoxic-to-anoxic water; measured chemosynthetic productivity was **0.55 ± 0.06 to 0.82 ± 0.07 μg C L⁻¹ d⁻¹**, and **60% of recovered MAGs** encoded autotrophic pathways, principally CBB and Wood–Ljungdahl modules. (atencio2024metabolicadaptationsunderpin pages 1-2)

### C. Pathways and biological processes

- Calvin–Benson–Bassham cycle (CBB); **GO:0015977** carbon fixation
- Wood–Ljungdahl/reductive acetyl-CoA pathway
- reverse tricarboxylic-acid cycle
- non-Calvin carbon-fixation pathways
- photosynthesis; **GO:0015979** photosynthesis
- aerobic respiration; **GO:0009060** aerobic respiration
- electron-transport chain and proton-motive-force generation
- hydrogen oxidation; formate oxidation; Fe(II) oxidation
- sulfide/thiosulfate oxidation; Sox pathway
- denitrification and nitrate respiration
- organic-acid and sugar uptake/catabolism
- phagotrophy, relevant mainly to microbial eukaryotes
- proton-pump-rhodopsin phototrophy

In Great Salt Lake sediments, communities changed from aerobic/heterotrophic at the surface to anaerobic/autotrophic at depth. Dark CO₂ fixation was detected, and the Wood–Ljungdahl pathway was predicted to be the principal mode of autotrophy among 36 OTUs, including hydrogenotrophic acetogens. The authors interpret this as selection for the lowest-energy-demanding known CO₂-fixation pathway under combined anoxia and hypersalinity. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)

### D. Genes, proteins, enzymes, and complexes

- RuBisCO: `rbcL`, `rbcS`, and Form II `cbbM`
- soluble NAD⁺-reducing [NiFe]-hydrogenase; membrane-bound [NiFe]-hydrogenase
- hydrogenase maturation proteins: `hyp` genes
- soluble and membrane-bound formate dehydrogenases
- molybdenum-cofactor biosynthesis proteins
- Fe(II)-oxidation candidates `cyc2` and `mtoA`
- Sox proteins `soxABXYZ` and `soxCD`
- lactate permease `lctP`; lactate dehydrogenase `ykgEFG`
- acetate permease `actP`; acetate kinase `ackA`
- nitrate reductase and terminal respiratory complexes
- denitrification markers including `nosZ`
- sulfur-cycle markers `aprAB` and `dsrAB`
- proton-pump rhodopsin
- organic-carbon transporters, including sugar and organic-acid transport systems

In *C. necator*, soluble hydrogenase transfers electrons to NAD⁺ to produce NADH, whereas membrane-bound dehydrogenases reduce quinone and feed the electron-transport chain that generates proton motive force. Hydrogenase maturation depends on `hyp` proteins that install the Ni–Fe–(CN)₂–CO cofactor. (jahn2024theenergymetabolism pages 1-2)

### E. Chemicals and resource nodes

- carbon dioxide — **CHEBI:16526**
- dioxygen — **CHEBI:15379**
- nitrate — **CHEBI:17632**
- nitrite — **CHEBI:16301**
- ammonium — **CHEBI:28938**
- formate — **CHEBI:15740**
- Fe(II) — **CHEBI:29033**
- H₂, sulfide/H₂S, elemental sulfur, thiosulfate, sulfate
- dissolved inorganic carbon
- organic carbon, acetate, lactate, sugars, fructose, succinate, butyrate
- NAD⁺/NADH, quinone/quinol, ATP
- poised electrode/extracellular electrons

For H₂, sulfide, thiosulfate, and pathway-specific metabolites, identifier assignment should be checked against the precise protonation/speciation intended by the experimental source before YAML insertion.

### F. Taxon/context nodes

- *Cupriavidus necator* H16 — model chemolithoautotroph/generalist
- *Leptothrix ochracea* — uncultivated, putative mixotrophic Fe(II) oxidizer
- Arcobacteraceae clade C and candidate genera UBA6211/CAIJNA01
- *Rhodomicrobium vannielii* and *R. udaipurense*
- *Sulfuritalea* in a hypoxic reservoir
- *Candidatus Bipolaricaulia* hydrogenotrophic acetogens

NCBI Taxonomy CURIEs should be added only after checking the exact accepted strain or candidate-taxon record; names alone are safer than an unverified numeric identifier.

## 3. Candidate evidence-backed causal edges

The following compact table identifies the highest-priority relationships.

| subject | predicate | object | evidence strength | taxon/context | DOI |
|---|---|---|---|---|---|
| light | supplies energy to | phototrophic growth | strong | general microbial trophic classification (weissbrodt2023basicmicrobiologyand pages 19-22) | 10.2166/9781789062304_0009 |
| inorganic carbon (CO2) | is fixed via | Calvin-Benson-Bassham cycle during autotrophy | strong | general; also *Cupriavidus necator* and deep aquifer MAGs (weissbrodt2023basicmicrobiologyand pages 19-22, jahn2024theenergymetabolism pages 1-2, atencio2024metabolicadaptationsunderpin pages 1-2) | 10.2166/9781789062304_0009; 10.1128/aem.00748-24; 10.1038/s41598-024-68868-9 |
| H2 oxidation | supplies electrons/reducing power for | CO2 fixation and energy metabolism | strong | *Cupriavidus necator* H16 lithoautotrophy (jahn2024theenergymetabolism pages 1-2) | 10.1128/aem.00748-24 |
| soluble hydrogenase and membrane-bound hydrogenase | enable | lithoautotrophic growth on H2/CO2 | strong | *Cupriavidus necator* H16 RB-TnSeq fitness assay (jahn2024theenergymetabolism pages 1-2) | 10.1128/aem.00748-24 |
| soluble formate dehydrogenase | dominates | formate oxidation | strong | *Cupriavidus necator* H16 on formic acid (jahn2024theenergymetabolism pages 1-2) | 10.1128/aem.00748-24 |
| Fe(II) oxidation genes *cyc2*/*mtoA* | support | iron-based lithotrophy | moderate-uncertain | *Leptothrix ochracea* genomes/metatranscriptomes; potential, not isolate proof (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 13-15) | 10.1128/aem.00599-24 |
| organic substrates | support | organoheterotrophic growth | strong | general classification; sugars/organic acids in *C. necator* and *L. ochracea* (weissbrodt2023basicmicrobiologyand pages 19-22, jahn2024theenergymetabolism pages 1-2, tothero2024leptothrixochraceagenomes pages 13-15) | 10.2166/9781789062304_0009; 10.1128/aem.00748-24; 10.1128/aem.00599-24 |
| inorganic carbon fixation plus organic substrate utilization | support | mixotrophic growth | strong | *Leptothrix ochracea*; marine Arcobacteraceae (tothero2024leptothrixochraceagenomes pages 1-2, li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 10-12) | 10.1128/aem.00599-24; 10.1128/msystems.00513-24 |
| sulfide oxidation | donates electrons to | nitrate reduction / autotrophic denitrification | strong | hypoxic sulfate-abundant reservoir water column (yang2024metagenomicsandstable pages 1-2) | 10.1021/acs.est.4c00248 |
| Wood-Ljungdahl pathway | enables | dark autotrophy in anoxic hypersaline sediment | strong | Great Salt Lake sediments (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | 10.1093/femsec/fiae105 |
| proton-pump rhodopsin expression | is positively associated with | non-Calvin carbon fixation potential | moderate-uncertain | marine plankton metatranscriptomes; correlation only (li2024insitucommunity pages 1-2) | 10.1128/spectrum.02177-23 |


*Table: This compact table prioritizes high-confidence causal edges for curating the microbial trophic type graph. It highlights mechanistic links among energy source, carbon source, electron donors, and flexible trophic strategies, while flagging correlation-only or genome-inferred claims as uncertain.*

The expanded curation table below gives source language and restrictions. “Strong” means direct growth, fitness, isotope, or convergent multi-omics evidence in the stated context—not universal validity across microbes.

| # | Subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---:|---|---|---|
| 1 | **light — supplies energy for → phototrophy** | Weissbrodt et al. 2023: microbes obtain energy from “chemicals (chemotrophs) or light photons (phototrophs).” (weissbrodt2023basicmicrobiologyand pages 19-22) | Strong definitional edge; general classification. |
| 2 | **inorganic electron donor — supports → lithotrophy** | The same source distinguishes “organic (organotrophs) or inorganic (lithotrophs) e-donors.” (weissbrodt2023basicmicrobiologyand pages 19-22) | Strong definitional edge. Add particular donor-specific children rather than treating all inorganic chemicals as interchangeable. |
| 3 | **CO₂ fixation — supports classification as → autotrophy** | Chemolithoautotrophs “respire inorganic donors with O₂ and fix CO₂”; nitrifiers fix CO₂ while oxidizing NH₄⁺ or NO₂⁻. (weissbrodt2023basicmicrobiologyand pages 19-22) | Strong, but require growth/flux or sufficiently complete pathway evidence; RuBisCO alone is not enough. |
| 4 | **organic carbon assimilation — supports classification as → heterotrophy** | Chemoorganoheterotrophs use organic donors; *C. necator* grows on “organic acids and sugars.” (weissbrodt2023basicmicrobiologyand pages 19-22, jahn2024theenergymetabolism pages 1-2) | Strong if organics supply biomass carbon. Do not infer from transporters alone. |
| 5 | **H₂ oxidation — generates ATP and reducing equivalents for → CBB CO₂ fixation** | *C. necator* “generates ATP and reduction equivalents from the oxidation of molecular hydrogen (H₂ → 2e⁻ + 2H⁺)” to fuel the CBB cycle. (jahn2024theenergymetabolism pages 1-2) | Strong, mechanistic, taxon-specific. H₂ is electron/energy source; CO₂ is carbon source; O₂ is the respiratory acceptor in the tested gas regime. |
| 6 | **soluble hydrogenase — contributes to → H₂-dependent lithoautotrophic growth** | RB-TnSeq fitness analysis found that “both soluble and membrane-bound enzymes were utilized for lithoautotrophic growth.” (jahn2024theenergymetabolism pages 1-2) | Strong direct gene-fitness evidence in *C. necator* H16. |
| 7 | **membrane-bound hydrogenase — contributes to → H₂-dependent lithoautotrophic growth** | Same knockout result as edge 6. (jahn2024theenergymetabolism pages 1-2) | Strong; retain as a separate edge because the enzymes feed different electron carriers. |
| 8 | **soluble formate dehydrogenase — catalyzes/dominates → formate oxidation** | “Soluble formate dehydrogenase (FDH) was the dominant enzyme for formate oxidation, not membrane-bound FDH.” (jahn2024theenergymetabolism pages 1-2) | Strong RB-TnSeq evidence in *C. necator*. “Dominates” is condition- and taxon-specific. |
| 9 | **molybdenum-cofactor biosynthesis — enables → growth on formate** | “Some, but not all, molybdenum cofactor biosynthesis genes were essential for growth on formate and nitrate respiration.” (jahn2024theenergymetabolism pages 1-2) | Strong but gene-specific. Curate individual genes only after consulting the paper’s fitness table. |
| 10 | **terminal respiratory-complex identity — conditionally affects → fitness under a trophic regime** | Of six terminal respiratory complexes, “only some are utilized, and utilization depends on the energy source.” (jahn2024theenergymetabolism pages 1-2) | Strong but too nonspecific for individual complex edges without extracting condition-by-complex results. |
| 11 | **background expression of hydrogenase machinery — imposes protein cost on → heterotrophic growth** | Deleting hydrogenase-related genes boosted heterotrophic growth through relief of “associated protein cost.” (jahn2024theenergymetabolism pages 1-2) | Strong and useful regulatory/resource-allocation edge; specific to *C. necator* conditions. |
| 12 | **`rbcL/cbbM` plus complete CBB cycle — enables → CO₂ fixation potential in *L. ochracea*** | Genomes encoded Form II RuBisCO and complete CBB genes; experimental assimilation supplied only “a small fraction of total carbon demand.” (tothero2024leptothrixochraceagenomes pages 13-15) | Moderate. Supports partial autotrophic carbon input, not obligate autotrophy. |
| 13 | **`cyc2`/`mtoA` — supports potential for → Fe(II) oxidation** | Nine high-quality genomes contained iron-oxidase genes, and metatranscriptomes showed high iron-oxidation expression. (tothero2024leptothrixochraceagenomes pages 1-2) | **Uncertain/moderate:** uncultivated organism; annotation and expression do not prove that Fe(II) oxidation alone supports growth. |
| 14 | **Fe(II) plus organic carbon availability — supports → mixotrophic growth of *L. ochracea*** | Environmental enrichments required organic-containing water and Fe(II); transcriptomes co-expressed iron oxidation, aerobic respiration, organic utilization, and RuBisCO. (tothero2024leptothrixochraceagenomes pages 1-2) | Strong convergent environmental evidence, but taxon-specific and not a pure-culture demonstration. |
| 15 | **lactate uptake/catabolism (`lctP`, `ykgEFG`) — enables potential for → organotrophic carbon/energy use** | Genomes encoded lactate permease, lactate dehydrogenase, and a lactate-responsive regulator. (tothero2024leptothrixochraceagenomes pages 13-15) | Moderate genomic evidence; curate as “enables potential,” not demonstrated causation. |
| 16 | **acetate uptake/catabolism (`actP`, `ackA`) — enables potential for → organotrophic carbon/energy use** | Genomes encoded acetate permease and acetate kinase. (tothero2024leptothrixochraceagenomes pages 13-15) | Moderate genomic evidence with the same restriction as edge 15. |
| 17 | **sulfur oxidation plus denitrification plus organic-matter metabolism — supports → mixotrophy in Arcobacteraceae CAIJNA01** | In situ metatranscriptomes indicated carbon fixation coupled to sulfur oxidation and denitrification while organic matter was also metabolized. (li2024arcobacteraceaeareubiquitous pages 1-2) | Strong expression-based ecological evidence; still not direct substrate-flux proof. |
| 18 | **thiosulfate oxidation — contributes to → DIC fixation in marine Arcobacteraceae** | Across 187 Tara sites, thiosulfate-oxidation genes were transcribed at **98%** of sites and DIC-fixation genes at **80%**. (li2024arcobacteraceaeareubiquitous pages 10-12) | Moderate association at global scale. Do not encode site co-occurrence as direct enzyme-level causality. |
| 19 | **heterotrophic pathways — contribute more than autotrophic pathways to → Arcobacteraceae activity** | Fermentation/methane-oxidation transcription occurred at >98% of sites; heterotrophic activity exceeded autotrophic activity (**P < 0.001**). (li2024arcobacteraceaeareubiquitous pages 10-12) | Quantitative but dependent on transcript-based activity definitions. Useful as an annotation, not a universal trophic ranking. |
| 20 | **sulfide oxidation — provides electrons for → autotrophic nitrate reduction/denitrification** | The reservoir study states that ΣS²⁻ was the “primary electron donor preferentially oxidized by denitrification”; sulfide-oxidation and denitrification potentials correlated at **P < 0.05**. (yang2024metagenomicsandstable pages 1-2) | Strong convergent isotope, chemistry, and metagenomic evidence in hypoxic water; do not generalize to all denitrifiers. |
| 21 | **sulfate reduction — produces sulfide that enhances → denitrification** | Sulfide produced by sulfate reduction enhanced denitrification; `nosZ` and `aprAB/dsrAB` were abundant, and the nitrate isotope-fractionation ratio was **0.60**, lower than expected for heterotrophic denitrification. (yang2024metagenomicsandstable pages 1-2) | Strong ecosystem-level coupling; cross-population causation is possible, so do not force both processes into one organism. |
| 22 | **anoxic hypersaline conditions — select for → Wood–Ljungdahl-based autotrophy** | Dark CO₂ fixation was detected and the Wood–Ljungdahl pathway was the predicted principal autotrophic mode in saturated-NaCl sediment. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | Moderate-to-strong community evidence. “Select for” is an interpretation; encode environmental association separately if TraitMech predicates demand direct causality. |
| 23 | **proton-pump rhodopsin activity — may provide energy for → non-Calvin carbon fixation** | NCF potential was positively correlated with proton-pump-rhodopsin expression in four bacterial orders, “suggesting that NCF might be energetically supported by PPR.” (li2024insitucommunity pages 1-2) | **Uncertain:** correlation in metatranscriptomes, not perturbation evidence. Curate only with an uncertainty qualifier. |
| 24 | **phagotrophy — may complement → Calvin carbon fixation** | CCF potential showed positive or negative lineage-dependent correlations with phagotrophy-gene expression. (li2024insitucommunity pages 1-2) | **Uncertain and lineage-specific.** Direction is not consistent; unsuitable as one universal causal edge. |
| 25 | **combined photosynthesis and phagotrophy — constitutes → protistan mixotrophy** | Mixotrophs obtain energy/nutrients through both autotrophy and heterotrophy and regulate the two modes according to resource availability. (schenone2024mixotrophicprotistsand pages 2-3) | Strong class definition for microbial eukaryotes; keep separate from bacterial osmo-mixotrophy. |
| 26 | **nutrient limitation — favors grazing-mediated nutrient acquisition by → mixotrophs** | Under nutrient-poor conditions, mixotrophs can graze nutrient-rich prey when photosynthesis alone does not meet nutrient requirements. (schenone2024mixotrophicprotistsand pages 2-3) | Moderate ecological mechanism, primarily protistan. |
| 27 | **trophic growth condition plus nitrogen source — determines → PHA yield in *Rhodomicrobium*** | Maximum PHA was **44.08 mg L⁻¹ (43.61% dry weight)** during photoheterotrophy on butyrate with N₂; minimum was **0.04 mg L⁻¹ (0.16%)** during photoelectrotrophy. (conners2024thephototrophicpurple pages 1-2) | Strong application-level experimental evidence; PHA production is an output of trophic state, not part of its definition. |
| 28 | **photohydrogenotrophy with NH₄Cl — increases → electron yield** | Electron yield reached **58.89%**, versus **0.27–1.39%** under photoheterotrophy. (conners2024thephototrophicpurple pages 1-2) | Strong, species- and assay-specific process metric. |

## 4. Recent developments and current applications

### Multi-omics resolves trophic flexibility

The major 2024 advance is movement beyond single marker genes. The *L. ochracea* study combined nine MAGs, metabolic modeling, environmental enrichment, and transcriptomics to support concurrent Fe(II)/sulfur oxidation, organic-substrate use, and CBB fixation. This is substantially stronger than assigning trophic type from `rbcL` or `cyc2` alone, although the lack of a pure culture still limits causal claims. (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 13-15)

Likewise, global Arcobacteraceae analysis mapped metatranscriptomes from **187 Tara Oceans sites to 82 genomes**. Sulfur oxidation, DIC fixation, and heterotrophic modules were active across broad depths and regions, providing strong evidence that mixotrophy is geographically widespread rather than an exceptional laboratory state. (li2024arcobacteraceaeareubiquitous pages 10-12)

Whole-community transcriptomics in the South China Sea recovered **4.4 million unigenes**, detected expression from all five recognized non-Calvin fixation pathways, and linked non-Calvin fixation potential to proton-pump-rhodopsin expression. The authors nevertheless describe this relationship as a suggestion, appropriately distinguishing energetic hypothesis from demonstrated flux. (li2024insitucommunity pages 1-2)

### Carbon sequestration and subsurface ecology

Chemosynthetic productivity in ancient deep groundwater and Wood–Ljungdahl-dominated primary production in hypersaline sediment show that trophic type is central to identifying dark carbon sinks. The aquifer result—60% of MAGs with autotrophic pathways and measurable carbon incorporation—also demonstrates why pathway inventory should be paired with process-rate measurements. (atencio2024metabolicadaptationsunderpin pages 1-2, shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)

### Wastewater and nitrate remediation

Sulfide- and thiosulfate-driven autotrophic denitrification can remove nitrate without requiring large organic-carbon additions. In the Aha Reservoir, isotope fractionation, sulfur/nitrogen chemistry, and metagenomic potential jointly implicated sulfide as the preferred electron donor and *Sulfuritalea* as an important participant. This mechanism is directly relevant to low-carbon denitrification designs, but it can also connect sulfate reducers and sulfur oxidizers across a community rather than within one genome. (yang2024metagenomicsandstable pages 1-2)

### Carbon-to-products and metabolic engineering

*C. necator* is a model chassis for conversion of H₂/CO₂/O₂ or formate into biomass and polyhydroxybutyrate. Genome-wide fitness mapping identified the hydrogenases, soluble FDH, cofactor genes, and condition-specific respiratory complexes actually required under different feed regimes. It also revealed that unnecessary expression of trophic machinery imposes a protein cost, suggesting genome-streamlining targets. The organism’s genome is approximately **6.6 Mb/~6,600 genes**, and the study provides an interactive fitness resource at https://m-jahn.shinyapps.io/ShinyLib/. (jahn2024theenergymetabolism pages 1-2)

Phototrophic *Rhodomicrobium* strains produced PHA under photoheterotrophic, photohydrogenotrophic, photoferrotrophic, and photoelectrotrophic regimes. Their large condition-dependent differences in titre and electron yield demonstrate a real-world reason to represent trophic type as an experimental condition rather than a fixed species label. (conners2024thephototrophicpurple pages 1-2)

## 5. Expert synthesis for TraitMech design

A useful causal graph should have three converging branches:

1. **Energy acquisition:** light/rhodopsin/photosystem or chemical oxidation → electron transport/proton motive force → ATP.
2. **Reducing-power acquisition:** organic or inorganic donor → donor-specific oxidoreductase → NAD(P)H/reduced ferredoxin/quinol.
3. **Carbon acquisition:** inorganic carbon → CBB/Wood–Ljungdahl/rTCA fixation, or organic substrate → transporter/catabolic/assimilation pathway.

These branches should converge on **growth under a specified trophic regime**, which then supports the `METPO:1000631` annotation. Electron acceptor, oxygen status, salinity, light, and nutrient availability belong upstream as conditional factors. This structure prevents a frequent category error: treating “has RuBisCO,” “oxidizes sulfide,” or “grows aerobically” as a complete trophic classification.

For evidence ranking, a practical order is:

**controlled growth with carbon/electron balance or isotope flux > gene knockout/fitness under defined medium > convergent metatranscriptomics plus geochemistry > transcript expression alone > complete genomic pathway > single marker gene.** Recent mixoplankton experts similarly recommend integration of physiology, comparative genomics, single-cell methods, stable-isotope probing, proteomics, and metabolomics. They caution that isotope assays are complicated in non-constitutive mixotrophs because ingestion of photosynthetic prey can confound labels. (millette2024recommendationsforadvancing pages 11-12)

## 6. Warnings: claims not yet suitable for unqualified curation

- **Do not infer trophic type from one marker gene.** RuBisCO, `cyc2`, `mtoA`, Sox, or rhodopsin indicates potential, not necessarily growth-supporting flux.
- **Do not curate the PPR→non-Calvin-fixation edge as established causality.** It is a positive expression correlation and explicitly framed as “might be energetically supported.” (li2024insitucommunity pages 1-2)
- **Do not assert that *L. ochracea* is an obligate or fully demonstrated Fe(II)-based autotroph.** Current evidence supports mixotrophic potential and environmental activity, but the organism remains uncultivated and CO₂ supplied only a small fraction of carbon demand. (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 13-15)
- **Do not generalize *C. necator* isoenzyme dependencies.** Soluble FDH dominance, use of both hydrogenases, and respiratory-complex requirements are strain- and medium-specific RB-TnSeq results. (jahn2024theenergymetabolism pages 1-2)
- **Do not collapse sulfur cycling and denitrification into one cell without genome-resolved support.** Reservoir-level sulfate reduction can produce sulfide for a different sulfur-oxidizing denitrifier. (yang2024metagenomicsandstable pages 1-2)
- **Do not equate transcript abundance with metabolic rate.** Arcobacteraceae and plankton studies measure expressed potential, although broad replication and complementary geochemistry strengthen interpretation. (li2024arcobacteraceaeareubiquitous pages 10-12, li2024insitucommunity pages 1-2)
- **Do not encode “mixotrophy” without a mechanism qualifier.** Bacterial organic-substrate/inorganic-carbon mixotrophy, protistan phagomixotrophy, and kleptoplastidic mixotrophy are biologically different. (millette2024recommendationsforadvancing pages 11-12, schenone2024mixotrophicprotistsand pages 2-3)
- **Do not use terminal electron acceptor as the sole trophic label.** Aerobic, nitrate-respiring, sulfate-reducing, and fermentative modes should be modeled as respiratory or environmental context.
- **Do not assign unverified CURIEs.** In particular, distinguish chemical species by protonation state and verify NCBITaxon, EC, Rhea, KEGG, and MetaCyc records before committing them to YAML.

## 7. DOI-first bibliography

1. Weissbrodt DG, Laureni M, van Loosdrecht MCM, Comeau Y. **Basic microbiology and metabolism.** *Biological Wastewater Treatment*. Published May 2023. DOI: [10.2166/9781789062304_0009](https://doi.org/10.2166/9781789062304_0009). (weissbrodt2023basicmicrobiologyand pages 19-22)
2. Jahn M et al. **The energy metabolism of *Cupriavidus necator* in different trophic conditions.** *Applied and Environmental Microbiology* 90(10). Published September 25, 2024; issue October 2024. DOI: [10.1128/aem.00748-24](https://doi.org/10.1128/aem.00748-24). (jahn2024theenergymetabolism pages 1-2)
3. Tothero GK et al. ***Leptothrix ochracea* genomes reveal potential for mixotrophic growth on Fe(II) and organic carbon.** *Applied and Environmental Microbiology* 90(9). Published September 2024. DOI: [10.1128/aem.00599-24](https://doi.org/10.1128/aem.00599-24). (tothero2024leptothrixochraceagenomes pages 1-2)
4. Li J et al. **Arcobacteraceae are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans.** *mSystems* 9(7). Published July 2024. DOI: [10.1128/msystems.00513-24](https://doi.org/10.1128/msystems.00513-24). (li2024arcobacteraceaeareubiquitous pages 1-2, li2024arcobacteraceaeareubiquitous pages 10-12)
5. Atencio B et al. **Metabolic adaptations underpin high productivity rates in relict subsurface water.** *Scientific Reports* 14:18126. Published August 2024. DOI: [10.1038/s41598-024-68868-9](https://doi.org/10.1038/s41598-024-68868-9). (atencio2024metabolicadaptationsunderpin pages 1-2)
6. Shoemaker A et al. **Wood–Ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at Great Salt Lake, Utah.** *FEMS Microbiology Ecology* 100, fiae105. Advance publication July 25, 2024. DOI: [10.1093/femsec/fiae105](https://doi.org/10.1093/femsec/fiae105). (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
7. Yang M et al. **Metagenomics and stable isotopes uncover the augmented sulfide-driven autotrophic denitrification in a seasonally hypoxic, sulfate-abundant reservoir.** *Environmental Science & Technology* 58:14225–14236. Published July 31, 2024. DOI: [10.1021/acs.est.4c00248](https://doi.org/10.1021/acs.est.4c00248). (yang2024metagenomicsandstable pages 1-2)
8. Li H et al. **In situ community transcriptomics illuminates CO₂-fixation potentials and supporting roles of phagotrophy and proton pump in plankton in a subtropical marginal sea.** *Microbiology Spectrum* 12(3). Published February 6, 2024; issue March 2024. DOI: [10.1128/spectrum.02177-23](https://doi.org/10.1128/spectrum.02177-23). (li2024insitucommunity pages 1-2)
9. Conners EM et al. **The phototrophic purple non-sulfur bacteria *Rhodomicrobium* spp. are novel chassis for bioplastic production.** *Microbial Biotechnology* 17:e14552. Accepted July 31, 2024; published August 2024. DOI: [10.1111/1751-7915.14552](https://doi.org/10.1111/1751-7915.14552). (conners2024thephototrophicpurple pages 1-2)
10. Schenone L et al. **Mixotrophic protists and ecological stoichiometry: connecting homeostasis and nutrient limitation from organisms to communities.** *Frontiers in Ecology and Evolution* 12. Published November 2024. DOI: [10.3389/fevo.2024.1505037](https://doi.org/10.3389/fevo.2024.1505037). (schenone2024mixotrophicprotistsand pages 2-3)
11. Millette NC et al. **Recommendations for advancing mixoplankton research through empirical-model integration.** *Frontiers in Marine Science* 11. Published June 2024. DOI: [10.3389/fmars.2024.1392673](https://doi.org/10.3389/fmars.2024.1392673). (millette2024recommendationsforadvancing pages 11-12)

References

1. (weissbrodt2023basicmicrobiologyand pages 19-22): David G. Weissbrodt, Michele Laureni, Mark C.M. van Loosdrecht, and Yves Comeau. Basic microbiology and metabolism. Biological Wastewater Treatment, pages 9-74, May 2023. URL: https://doi.org/10.2166/9781789062304\_0009, doi:10.2166/9781789062304\_0009. This article has 21 citations.

2. (tothero2024leptothrixochraceagenomes pages 1-2): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 24 citations and is from a peer-reviewed journal.

3. (li2024arcobacteraceaeareubiquitous pages 1-2): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 39 citations and is from a peer-reviewed journal.

4. (schenone2024mixotrophicprotistsand pages 2-3): Luca Schenone, Zoe S. Aarons, Minerva García-Martínez, Anika Happe, and Andrea Redoglio. Mixotrophic protists and ecological stoichiometry: connecting homeostasis and nutrient limitation from organisms to communities. Frontiers in Ecology and Evolution, Nov 2024. URL: https://doi.org/10.3389/fevo.2024.1505037, doi:10.3389/fevo.2024.1505037. This article has 22 citations and is from a peer-reviewed journal.

5. (li2024insitucommunity pages 1-2): Hongfei Li, Jianwei Chen, Liying Yu, Guangyi Fan, Tangcheng Li, Ling Li, Huatao Yuan, Jingtian Wang, Cong Wang, Denghui Li, and Senjie Lin. <i>in situ</i> community transcriptomics illuminates co <sub>2</sub> -fixation potentials and supporting roles of phagotrophy and proton pump in plankton in a subtropical marginal sea. Mar 2024. URL: https://doi.org/10.1128/spectrum.02177-23, doi:10.1128/spectrum.02177-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (atencio2024metabolicadaptationsunderpin pages 1-2): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

7. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 15 citations and is from a peer-reviewed journal.

8. (jahn2024theenergymetabolism pages 1-2): Michael Jahn, Nick Crang, Arvid H. Gynnå, Deria Kabova, Stefan Frielingsdorf, Oliver Lenz, Emmanuelle Charpentier, and Elton P. Hudson. The energy metabolism of <i>cupriavidus necator</i> in different trophic conditions. Oct 2024. URL: https://doi.org/10.1128/aem.00748-24, doi:10.1128/aem.00748-24. This article has 41 citations and is from a peer-reviewed journal.

9. (tothero2024leptothrixochraceagenomes pages 13-15): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 24 citations and is from a peer-reviewed journal.

10. (li2024arcobacteraceaeareubiquitous pages 10-12): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 39 citations and is from a peer-reviewed journal.

11. (yang2024metagenomicsandstable pages 1-2): Mengdi Yang, Qianli Luo, Zhongya Fan, Fantang Zeng, Lu Huang, Shiyuan Ding, Gaoyang Cui, Dongli Li, Gangjian Wei, Cong-Qiang Liu, and Xiao-Dong Li. Metagenomics and stable isotopes uncover the augmented sulfide-driven autotrophic denitrification in a seasonally hypoxic, sulfate-abundant reservoir. Environmental science & technology, 58:14225-14236, Jul 2024. URL: https://doi.org/10.1021/acs.est.4c00248, doi:10.1021/acs.est.4c00248. This article has 23 citations and is from a domain leading peer-reviewed journal.

12. (conners2024thephototrophicpurple pages 1-2): Eric M. Conners, Karthikeyan Rengasamy, Tahina Ranaivoarisoa, and Arpita Bose. The phototrophic purple non‐sulfur bacteria rhodomicrobium spp. are novel chassis for bioplastic production. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14552, doi:10.1111/1751-7915.14552. This article has 14 citations and is from a peer-reviewed journal.

13. (millette2024recommendationsforadvancing pages 11-12): Nicole C. Millette, Suzana G. Leles, Matthew D. Johnson, Ashley E. Maloney, Emily F. Brownlee, Natalie R. Cohen, Solange Duhamel, Nicole J. Poulton, Sarah D. Princiotta, Karen Stamieszkin, Susanne Wilken, and Holly V. Moeller. Recommendations for advancing mixoplankton research through empirical-model integration. Frontiers in Marine Science, Jun 2024. URL: https://doi.org/10.3389/fmars.2024.1392673, doi:10.3389/fmars.2024.1392673. This article has 12 citations.