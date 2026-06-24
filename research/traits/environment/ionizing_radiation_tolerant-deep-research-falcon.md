---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:33:39.322842'
end_time: '2026-06-17T22:45:28.758778'
duration_seconds: 709.44
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ionizing radiation tolerant
  trait_identifier: traitmech:000008
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ionizing_radiation_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental tolerance in which an organism survives high doses
    of ionizing radiation (e.g. gamma rays), typically via efficient repair of DNA
    double-strand breaks and protection of the proteome from oxidative damage.
  parent_traits: traitmech:000007
  synonyms: gamma radiation resistant
  evidence_summary: "DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates\
    \ a significantly higher radiation resistance with D10 values exceeding 12 kGy\
    \ for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus\
    \ radiodurans tolerates gamma (ionizing) radiation D10 doses exceeding 12 kGy.)\
    \ | DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between\
    \ intracellular Mn/Fe concentration ratios and bacterial resistance to radiation\
    \ (Mechanism support \u2014 manganese-mediated oxidative-damage protection underlies\
    \ survival of lethal ionizing-radiation doses.)"
  causal_graph_summary: 'ionizing_radiation_tolerance_dsb_repair: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ionizing radiation tolerant
- **METPO identifier:** traitmech:000008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ionizing radiation (e.g. gamma rays), typically via efficient repair of DNA double-strand breaks and protection of the proteome from oxidative damage.
- **Parent traits:** traitmech:000007
- **Synonyms:** gamma radiation resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates gamma (ionizing) radiation D10 doses exceeding 12 kGy.) | DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Mechanism support — manganese-mediated oxidative-damage protection underlies survival of lethal ionizing-radiation doses.)
- **Existing causal graph summary:** ionizing_radiation_tolerance_dsb_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **ionizing radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ionizing_radiation_tolerant.yaml`.

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
- **Trait label:** ionizing radiation tolerant
- **METPO identifier:** traitmech:000008
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives high doses of ionizing radiation (e.g. gamma rays), typically via efficient repair of DNA double-strand breaks and protection of the proteome from oxidative damage.
- **Parent traits:** traitmech:000007
- **Synonyms:** gamma radiation resistant
- **Existing evidence:** DOI:10.3390/genes14091803: Deinococcus radiodurans R1 demonstrates a significantly higher radiation resistance with D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation (Organism example: Deinococcus radiodurans tolerates gamma (ionizing) radiation D10 doses exceeding 12 kGy.) | DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Mechanism support — manganese-mediated oxidative-damage protection underlies survival of lethal ionizing-radiation doses.)
- **Existing causal graph summary:** ionizing_radiation_tolerance_dsb_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **ionizing radiation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ionizing_radiation_tolerant.yaml`.

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


# Research Report: Microbial Trait “Ionizing radiation tolerant” (METPO: traitmech:000008)

## 1) Scope summary (phenotype, assays, boundary cases)
**Trait definition (curation scope):** *Ionizing-radiation tolerance* is the capacity of a microorganism to remain viable after exposure to high doses of ionizing radiation (commonly γ-radiation in laboratory assays), typically by repairing extensive DNA damage (notably double-strand breaks) and limiting oxidative damage to proteins (“proteome protection”). Ionizing radiation is described as producing **single- and double-strand breaks, abasic sites, and complex clustered lesions**; clustered/bistranded lesions are particularly repair-resistant and contribute strongly to lethality. (Lourenço et al., 2023-01, DOI:10.1007/978-3-031-18810-7_9, https://doi.org/10.1007/978-3-031-18810-7_9) (lourenco2023environmentalradiobiology pages 11-13)

**Operational measurements:** In microbial radiobiology, tolerance is typically quantified by survival curves and summary measures such as **D10** (dose causing 90% reduction of viable cells) and **LD50** (dose causing 50% lethality). These metrics are explicitly used in reactor-cooling-pool isolate studies and are sensitive to experimental context (irradiation matrix, nutrient availability, metabolic state). (Petit et al., 2023-07, DOI:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871) (petit2023firstisolationand pages 8-9)

**Boundary cases / nearby traits:**
- **UV resistance** (non-ionizing) shares DNA repair pathways (e.g., NER) but does *not* imply ionizing-radiation tolerance unless survival after ionizing exposure is demonstrated. (Subramani & Srinivasan, 2023-09, DOI:10.3390/genes14091803, https://doi.org/10.3390/genes14091803) (subramani2023involvementofnucleotide pages 1-2)
- **Oxidative-stress tolerance** and **desiccation tolerance** are often correlated with ionizing-radiation tolerance (shared ROS/protein oxidation challenges), but should be curated as distinct traits unless ionizing-radiation survival is directly measured. (Pal et al., 2024-06, DOI:10.1371/journal.pone.0304810, https://doi.org/10.1371/journal.pone.0304810) (pal2024unravelingradiationresistance pages 2-4)

**Key curation caution:** The same organism can show markedly different apparent tolerance depending on **dose rate**, **culture medium**, and whether cells are metabolically active versus resting. (Gregory et al., 2024-01, DOI:10.1093/femsre/fuae001, https://doi.org/10.1093/femsre/fuae001; Petit et al., 2023-07, DOI:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871) (gregory2024radioactivewastemicrobiology pages 13-14, petit2023firstisolationand pages 8-9)

## 2) Current understanding (key mechanistic concepts)
### 2.1 DNA damage sensing and DDR derepression in *Deinococcus*
A central, well-supported regulatory mechanism in *Deinococcus radiodurans* is a **protease-based derepression system**:
- **PprI/IrrE** is a metalloprotease that, upon DNA damage, **cleaves the transcriptional repressor DdrO**, thereby inducing expression of DNA damage response (DDR) genes. (Lu et al., 2024-02, DOI:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9) (lu2024thedeinococcusprotease pages 1-2)
- **Upstream signal:** Lu et al. (2024) provide direct structural/biochemical evidence that **single-stranded DNA (ssDNA) serves as the damage-sensing signal** by physically binding PprI and enhancing PprI–DdrO interaction and DdrO cleavage in a length-dependent manner. (Lu et al., 2024-02, DOI:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9) (lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5, lu2024thedeinococcusprotease pages 1-2)
- **Downstream transcriptional activation:** When the system is functional, canonical DDR genes such as **recA** and **uvrD** show **~5–10-fold induction** after γ-radiation, whereas induction is strongly blunted in defective mutants. (Lu et al., 2024-02, DOI:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9) (lu2024thedeinococcusprotease pages 7-8)

### 2.2 Proteome protection and metal homeostasis (Mn/Fe axis)
Proteome protection is repeatedly emphasized as a determinant of survival after ionizing radiation.
- A foundational model links **high intracellular Mn relative to Fe** to radioresistance by protecting proteins from oxidative damage. (Krisko & Radman, 2013-07, DOI:10.1101/cshperspect.a012765, https://doi.org/10.1101/cshperspect.a012765) (supported contextually via repository-focused review) (gregory2024radioactivewastemicrobiology pages 13-14)
- **Recent mechanistic extension (2024):** A γ-radiation-induced sRNA (**DrsS**) in *D. radiodurans* supports radiotolerance via oxidative-stress defenses and metal homeostasis. Deletion of **drsS** depletes intracellular **Mn2+ (~70%)** and **Fe2+ (~40%)** and increases **protein carbonylation**, while complementation reverses these phenotypes. (Rai & Dutta, 2024-05, DOI:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23) (rai2024anovelionizing pages 1-3)

### 2.3 DNA repair pathways beyond *Deinococcus*-specific regulators
A wide range of bacteria rely on combinations of conserved DNA repair systems:
- In *Deinococcus irradiatisoli* 17bor-2 (genome sequenced and annotated), the genome shows key NER components (**UvrABC excinuclease genes**) and **Rec-dependent pathway genes**, supporting roles for **nucleotide excision repair** and recombinational repair in radiation-associated stress survival (noting the paper focuses on UV, but uses Deinococcus radiation tolerance benchmarks). (Subramani & Srinivasan, 2023-09, DOI:10.3390/genes14091803, https://doi.org/10.3390/genes14091803) (subramani2023involvementofnucleotide pages 1-2)

## 3) Recent developments (prioritize 2023–2024)
### 3.1 2024: ssDNA-dependent activation of PprI/IrrE (Nature Communications)
Lu et al. (2024) provide a direct answer to a long-standing question: **what activates PprI?** Their results support a causal chain: radiation damage → ssDNA accumulation → ssDNA binding to PprI → enhanced cleavage of DdrO → DDR gene induction (recA/uvrD). (Lu et al., 2024-02, DOI:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9) (lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5, lu2024thedeinococcusprotease pages 1-2)

### 3.2 2024: sRNA DrsS couples ROS detoxification with Mn/Fe balancing (AEM)
Rai & Dutta (2024) expand the mechanism set from protein-centered systems to **RNA regulation**, showing DrsS induction under γ-radiation and oxidative/genotoxic stresses, with impacts on Mn/Fe levels, protein oxidation, and catalase-mediated ROS detoxification. (Rai & Dutta, 2024-05, DOI:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23) (rai2024anovelionizing pages 1-3)

### 3.3 2024: Radiowaste context—quantitative “limits to life” and relevance of dose rate (FEMS Microbiology Reviews)
Gregory et al. (2024) synthesize radiation survival data under conditions relevant to engineered barrier systems in geological disposal facilities. They emphasize that survival depends on both total dose and dose rate, with a threshold region below which damage is repairable and above which viability collapses. (Gregory et al., 2024-01, DOI:10.1093/femsre/fuae001, https://doi.org/10.1093/femsre/fuae001) (gregory2024radioactivewastemicrobiology pages 13-14)

## 4) Current applications and real-world implementations
### 4.1 Nuclear facility microbiology and radionuclide bioremediation
**Cooling pool isolates from an operating reactor**: Petit et al. (2023) isolated bacteria from a reactor core cooling pool and demonstrated both **radiotolerance** and **uranium removal** capabilities:
- Most isolates survived **200 Gy**; some endured **1 kGy**, with **four strains retaining >10% survival** at 1 kGy. (Petit et al., 2023-07, DOI:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871) (petit2023firstisolationand pages 1-2)
- Uranium uptake: **seven strains removed almost all uranium from a 5 µM solution**, and **four strains were efficient at 50 µM**, supporting practical radionuclide decontamination potential. (Petit et al., 2023-07, DOI:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871) (petit2023firstisolationand pages 1-2)

**Visual survival data (assay dependence):** Petit et al. report survival across strains at 200 Gy, 500 Gy, and 1 kGy in heat-map format for (i) resting cells (NaCl) and (ii) metabolically active cells (LB), illustrating strong medium/state effects. (Petit et al., 2023-07, DOI:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871) (petit2023firstisolationand media 698b6292, petit2023firstisolationand media 8e4e84a6)

### 4.2 Environmental and repository safety modeling
In geological disposal facility (GDF) or engineered barrier system (EBS) contexts, microbial survival under changing radiation, temperature, pH, and salinity is treated as a safety-relevant variable. Gregory et al. (2024) provide an integrative framework for predicting when/where conditions limit microbial activity and survival. (Gregory et al., 2024-01, DOI:10.1093/femsre/fuae001, https://doi.org/10.1093/femsre/fuae001) (gregory2024radioactivewastemicrobiology pages 13-14)

## 5) Relevant statistics and quantitative data (recent studies)
### 5.1 Survival/tolerance benchmarks (kGy/Gy scale)
- **Deinococcus spp. tolerance**: environmental radiobiology synthesis reports *D. radiodurans* acute resistance up to **~15 kGy** and chronic tolerance **>60 Gy/h** (and notes some Deinococci above this). (Lourenço et al., 2023-01, DOI:10.1007/978-3-031-18810-7_9, https://doi.org/10.1007/978-3-031-18810-7_9) (lourenco2023environmentalradiobiology pages 11-13)
- **Repository/radiowaste review statistics:** Gregory et al. (2024) compile broad microbial D10 values and survival thresholds, including D10 for bacteria in different matrices (e.g., dried vs buffer) and survival to accumulated doses approaching **~20 kGy** in some laboratory isolates related to *Deinococcus*/*Kineococcus*. (Gregory et al., 2024-01, DOI:10.1093/femsre/fuae001, https://doi.org/10.1093/femsre/fuae001) (gregory2024radioactivewastemicrobiology pages 13-14)

### 5.2 Assay dependence (medium/metabolic state) and D10/LD50 examples
Petit et al. (2023) explicitly note that irradiation medium and metabolic state influence survival, and provide example LD50 and D10 values that vary by medium (e.g., D10 in the ~0.18–0.21 kGy range in some contexts, and higher values in others), supporting the need to represent assay context in curation. (Petit et al., 2023-07, DOI:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871) (petit2023firstisolationand pages 8-9)

### 5.3 Quantitative molecular phenotypes (metal levels, transcription induction)
- **Metal homeostasis:** drsS deletion causes **~70% lower Mn2+** and **~40% lower Fe2+**, with increased protein carbonylation. (Rai & Dutta, 2024-05, DOI:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23) (rai2024anovelionizing pages 1-3)
- **DDR induction:** functional PprI–DdrO system yields **~5–10-fold induction** of recA/uvrD/ddrO after γ-radiation, versus <2-fold induction in defective mutants. (Lu et al., 2024-02, DOI:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9) (lu2024thedeinococcusprotease pages 7-8)

## 6) Candidate nodes for TraitMech causal graph (grouped)
The table below provides a curation-ready node inventory with node type and suggested ontology grounding.

| Node label | Node type (gene/protein/pathway/metabolite/process/environment/assay) | Suggested ontology grounding (CURIE) | Taxon scope (broad vs Deinococcus-specific) | Evidence support (which cited papers in our context) |
|---|---|---|---|---|
| ionizing radiation | environment | ENVO:01001024 | broad | Causes DNA strand breaks and clustered lesions; foundational trait-defining stressor (lourenco2023environmentalradiobiology pages 11-13, gregory2024radioactivewastemicrobiology pages 13-14) |
| gamma radiation | environment | label-only | broad | Primary assay/exposure type in most cited microbial radiotolerance studies (gregory2024radioactivewastemicrobiology pages 13-14, petit2023firstisolationand pages 1-2, petit2023firstisolationand pages 8-9) |
| dose rate | assay | label-only | broad | Survival depends on both total dose and dose rate in repository/radiowaste contexts (gregory2024radioactivewastemicrobiology pages 13-14) |
| D10 | assay | label-only | broad | Standard assay metric for 90% killing; explicitly discussed for isolates and reviews (petit2023firstisolationand pages 8-9, gregory2024radioactivewastemicrobiology pages 13-14) |
| LD50 | assay | label-only | broad | Used as survival benchmark in reactor cooling-pool isolate study (petit2023firstisolationand pages 8-9) |
| single-stranded DNA (ssDNA) | metabolite/process-related molecular entity | CHEBI:33696 | broad | Direct activating ligand/signal for PprI in Deinococcus DNA damage sensing (lu2024thedeinococcusprotease pages 1-2, lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5) |
| DNA double-strand break | process | GO:0006302 | broad | Core ionizing-radiation lesion type emphasized in radiobiology overview (lourenco2023environmentalradiobiology pages 11-13) |
| clustered DNA lesion | process | label-only | broad | Repair-resistant complex damage caused by ionizing radiation, especially high-LET exposure (lourenco2023environmentalradiobiology pages 11-13) |
| DNA repair | process | GO:0006281 | broad | Central umbrella mechanism for radiation tolerance across taxa (lourenco2023environmentalradiobiology pages 11-13, pal2024unravelingradiationresistance pages 2-4) |
| DNA double-strand break repair | pathway/process | GO:0006302 | broad | Trait definition emphasizes efficient DSB repair after ionizing radiation (lourenco2023environmentalradiobiology pages 11-13, pal2024unravelingradiationresistance pages 2-4) |
| nucleotide excision repair (NER) | pathway/process | GO:0006289 | broad | Identified in Deinococcus genomes as major UV/radiation-associated repair pathway (subramani2023involvementofnucleotide pages 1-2, pal2024unravelingradiationresistance pages 2-4) |
| recombination repair | pathway/process | GO:0000725 | broad | Rec-dependent pathways highlighted in radiation resistance (subramani2023involvementofnucleotide pages 1-2, pal2024unravelingradiationresistance pages 2-4) |
| ESDSA (extended synthesis-dependent strand annealing) | pathway/process | label-only | Deinococcus-enriched | Generates extensive ssDNA during recovery; part of Deinococcus repair context (lu2024thedeinococcusprotease pages 7-8) |
| recA | gene/protein | GO:0003677 | broad | DDR gene induced downstream of PprI-DdrO system; Rec-dependent repair highlighted (lu2024thedeinococcusprotease pages 7-8, subramani2023involvementofnucleotide pages 1-2) |
| uvrD | gene/protein | label-only | broad | DDR gene induced after radiation in functional PprI-DdrO system (lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5) |
| UvrABC excinuclease | protein complex/pathway component | GO:0016449 | broad | Key NER machinery identified in Deinococcus irradiatisoli genome (subramani2023involvementofnucleotide pages 1-2) |
| DdrO | protein | label-only | Deinococcus-specific | Essential Deinococcus transcriptional repressor cleaved by PprI after DNA damage (lu2024thedeinococcusprotease pages 1-2, lu2024thedeinococcusprotease pages 7-8) |
| PprI/IrrE | protein | label-only | Deinococcus-specific | Metalloprotease/sensor central to DDR derepression in Deinococcus (lu2024thedeinococcusprotease pages 1-2, lu2024thedeinococcusprotease pages 8-9) |
| RDRM promoter motif | assay/regulatory element | label-only | Deinococcus-specific | Promoter motif bound by DdrO upstream of DDR genes (lu2024thedeinococcusprotease pages 1-2) |
| reactive oxygen species (ROS) | metabolite/process | CHEBI:26523 | broad | Detoxification is a key arm of radioresistance and oxidative-stress survival (rai2024anovelionizing pages 1-3, pal2024unravelingradiationresistance pages 2-4) |
| catalase / KatA | gene/protein | EC:1.11.1.6 | broad | DrsS promotes catalase-mediated ROS detoxification via katA transcript interaction (rai2024anovelionizing pages 1-3) |
| superoxide dismutase / SodA | gene/protein | EC:1.15.1.1 | broad | drsS is potentially co-transcribed with sodA in D. radiodurans (rai2024anovelionizing pages 1-3) |
| DrsS sRNA | gene/regulatory RNA | label-only | Deinococcus-specific | Radiation-induced sRNA affecting Mn/Fe balance, KatA, and oxidative-stress resistance (rai2024anovelionizing pages 1-3) |
| protein carbonylation | process | GO:0006481 | broad | Marker of proteome oxidation increased in drsS deletion mutant (rai2024anovelionizing pages 1-3) |
| Mn2+ | metabolite/ion | CHEBI:29035 | broad | Supports proteome protection and activates PprI in vitro; homeostasis altered by drsS deletion (lu2024thedeinococcusprotease pages 8-9, rai2024anovelionizing pages 1-3) |
| Fe2+ | metabolite/ion | CHEBI:29033 | broad | Intracellular levels shift with drsS deletion; low relative Fe linked to radioresistance models (rai2024anovelionizing pages 1-3, pal2024unravelingradiationresistance pages 2-4) |
| Mn/Fe ratio | assay/metabolic state | label-only | broad | Strongly associated with radiation resistance/proteome protection in foundational model (pal2024unravelingradiationresistance pages 2-4, gregory2024radioactivewastemicrobiology pages 13-14) |
| manganese transporters | protein/system | label-only | broad | MntABCD/NRAMP-type transport discussed as contributors to Mn homeostasis in resistance strategies (pal2024unravelingradiationresistance pages 2-4) |
| antioxidant manganese complexes | metabolite complex | label-only | broad | Non-enzymatic Mn-containing metabolites implicated in ROS quenching and proteome shielding (pal2024unravelingradiationresistance pages 2-4, lu2024thedeinococcusprotease pages 8-9) |
| carotenoids | metabolite | CHEBI:23044 | broad | Chemical protectants/oxidant scavengers associated with radiation resistance (lourenco2023environmentalradiobiology pages 11-13, pal2024unravelingradiationresistance pages 2-4) |
| ectoine | metabolite | CHEBI:53552 | broad | Extremolyte cited as a protectant stabilizing proteins/membranes under stress (lourenco2023environmentalradiobiology pages 11-13) |
| nucleoid condensation/remodeling | process | GO:0009295 | broad | Listed among radiation-tolerance contributors in Deinococcus review context (subramani2023involvementofnucleotide pages 1-2) |
| stationary or metabolically inactive state | assay/physiological state | label-only | broad | Survival differs between inactive/resting and metabolically active cells under irradiation (petit2023firstisolationand pages 8-9) |
| metabolically active state | assay/physiological state | label-only | broad | Growth in nutritive medium can alter immediate repair/ROS-scavenging responses (petit2023firstisolationand pages 8-9) |
| growth medium | assay | label-only | broad | Medium composition changes apparent radiotolerance measurements (petit2023firstisolationand pages 8-9) |
| LB medium | assay | label-only | broad | Used as metabolically active irradiation condition in cooling-pool isolate assays (petit2023firstisolationand pages 8-9, petit2023firstisolationand media 698b6292) |
| NaCl medium | assay | label-only | broad | Used for resting-cell irradiation condition in cooling-pool isolate assays (petit2023firstisolationand pages 8-9, petit2023firstisolationand media 698b6292) |
| PBS | assay | CHEBI:62996 | broad | Used in irradiation preparation and survival contexts in HBRA isolate work/reviewed comparisons (pal2024unravelingradiationresistance pages 2-4, gregory2024radioactivewastemicrobiology pages 13-14) |
| uranium(VI) / uranyl | metabolite/ion | CHEBI:37336 | broad | Target contaminant removed by radiotolerant isolates from reactor cooling pool (petit2023firstisolationand pages 1-2, petit2023firstisolationand pages 8-9) |
| uranium uptake / biosorption | process | GO:0015706 | broad | Measured functional outcome supporting application in radionuclide cleanup (petit2023firstisolationand pages 1-2, petit2023firstisolationand pages 8-9) |
| bioremediation of radionuclides | process/application | GO:0030250 | broad | Real-world application highlighted for radiation-tolerant microbes and isolates (petit2023firstisolationand pages 1-2, lourenco2023environmentalradiobiology pages 11-13, pal2024unravelingradiationresistance pages 2-4) |


*Table: This table lists candidate entities for a TraitMech causal graph of microbial ionizing-radiation tolerance, spanning environmental exposures, assay variables, damage types, repair systems, regulatory proteins, metabolites, and application nodes. It is useful for selecting grounded graph nodes while distinguishing broad mechanisms from Deinococcus-specific components.*

## 7) Evidence-backed candidate causal edges (triples)
The table below lists candidate edges with supporting quotes/snippets, DOI-first references, and curation notes (including uncertainty flags).

| Subject node (suggested CURIE/ID) | Predicate | Object node (CURIE/ID) | Evidence (paper + year + DOI + URL) | Supporting snippet | Notes for curation |
|---|---|---|---|---|---|
| PprI/IrrE (label only; Deinococcus protease) | directly_binds | single-stranded DNA (ssDNA) (GO:0003697 candidate for ssDNA binding function) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 1-2, lu2024thedeinococcusprotease pages 7-8) | “ssDNA physically interacts with PprI protease” and “single-stranded DNA could serve as the signal for DNA damage sensing” | Strong, direct biochemical/structural evidence in Deinococcus; taxon-specific regulator but high-value causal edge. |
| PprI/IrrE (label only) | proteolytically_cleaves | DdrO repressor (label only) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 1-2) | “specific cleavage of DdrO by PprI induces the expression of DDR proteins following DNA damage” | Strong, direct mechanism in Deinococcus DDR pathway. |
| DdrO repressor (label only) | represses | RDRM-containing DDR gene promoters (label only) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 1-2) | “DdrO is a transcriptional repressor that binds to the radiation/desiccation response motif (RDRM)-containing promoters upstream of DDR genes” | Strong for Deinococcus; promoter motif can be node or annotation depending graph granularity. |
| ssDNA (label only) | increases_interaction_between | PprI/IrrE and DdrO (label only complex/process) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 4-5) | “ssDNA increases PprI–DdrO interaction (FRET RFU ratio)” | Strong, in vitro/in vivo support; model-system-specific but mechanistically precise. |
| ssDNA (label only) | enhances | PprI-mediated DdrO cleavage (label only process) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 4-5, lu2024thedeinococcusprotease pages 1-2) | “enhances the PprI-DdrO interactions as well as the DdrO cleavage in a length-dependent manner” | Strong; useful as process-level edge if cleavage event represented explicitly. |
| DdrO cleavage (label only process) | induces_expression_of | recA (gene; KEGG/UniProt taxon-specific pending) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 7-8) | “recA, uvrD, and ddrO show 5–10-fold induction when the system is functional” | Strong but should be modeled as PprI/DdrO-dependent in Deinococcus after γ-radiation. |
| DdrO cleavage (label only process) | induces_expression_of | uvrD (gene; KEGG/UniProt taxon-specific pending) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5) | “recA, uvrD, and ddrO show 5–10-fold induction” | Strong for Deinococcus DNA repair response. |
| DdrO cleavage (label only process) | induces_expression_of | ddrO (gene; label only) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 7-8) | “recA, uvrD, and ddrO show 5–10-fold induction” | Strong; autoregulatory recovery logic plausible but curate carefully as transcriptional response downstream of derepression. |
| Mn2+ (CHEBI:29035) | activates | PprI protease activity (label only) | Lu et al. 2024, Nature Communications, doi:10.1038/s41467-024-46208-9, https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 8-9) | “low concentrations of Zn or Mn (20 µM) can activate DG-PprI in vitro” | Moderate-strong; biochemical assay evidence, may be assay-specific and concentration-dependent. |
| DrsS sRNA (label only) | directly_interacts_with | katA transcript (gene/transcript; label only) | Rai & Dutta 2024, Applied and Environmental Microbiology, doi:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3) | “In vitro binding assays indicate that DsrS directly interacts with the coding region of the katA transcript” | Strong direct interaction in D. radiodurans; spelling DrsS/DsrS varies in excerpt, verify exact gene symbol at curation. |
| DrsS sRNA (label only) | stabilizes_or_protects | katA transcript (label only) | Rai & Dutta 2024, Applied and Environmental Microbiology, doi:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3) | “thus possibly protecting it from cellular endonucleases in vivo” | Moderate; mechanistic inference from binding assays, mark uncertain if requiring direct in vivo stability assay. |
| DrsS sRNA (label only) | promotes | catalase-mediated ROS detoxification (GO:0098869 candidate process) | Rai & Dutta 2024, Applied and Environmental Microbiology, doi:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3) | “DrsS appeared to activate catalase under oxidative stress and detoxify intracellular ROS” | Strong phenotype-level evidence in D. radiodurans, though direct molecular route is via katA transcript interaction. |
| drsS deletion (label only perturbation) | decreases_intracellular | Mn2+ (CHEBI:29035) | Rai & Dutta 2024, Applied and Environmental Microbiology, doi:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3) | “Deletion of the drsS gene resulted in the depletion of intracellular concentration of both Mn2+ and Fe2+ by ~70% and 40%” | Strong perturbation evidence; could be represented inversely as DrsS maintains Mn2+ homeostasis. |
| drsS deletion (label only perturbation) | decreases_intracellular | Fe2+ (CHEBI:29033) | Rai & Dutta 2024, Applied and Environmental Microbiology, doi:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3) | “depletion of intracellular concentration of both Mn2+ and Fe2+ by ~70% and 40%” | Strong perturbation evidence in D. radiodurans. |
| drsS deletion (label only perturbation) | increases | protein carbonylation (GO:carbonylation label only) | Rai & Dutta 2024, Applied and Environmental Microbiology, doi:10.1128/aem.01538-23, https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3) | “with a concomitant increase in carbonylation of intracellular protein” | Strong; useful proteome-damage node linked to radiation tolerance mechanism. |
| high intracellular Mn/Fe ratio (label only) | positively_correlates_with | ionizing radiation tolerance (METPO:traitmech:000008) | Krisko & Radman 2013, Cold Spring Harbor Perspectives in Biology, doi:10.1101/cshperspect.a012765, https://doi.org/10.1101/cshperspect.a012765; summarized in Gregory et al. 2024, FEMS Microbiology Reviews, doi:10.1093/femsre/fuae001, https://doi.org/10.1093/femsre/fuae001 (gregory2024radioactivewastemicrobiology pages 13-14) | “A strong correlation has … more Mn2+ and about three times less Fe2+ … the antioxidant protection of the cellular proteome.” | Foundational rather than 2024-primary; strong review-supported claim, but correlation is not universal causation. |
| ionizing radiation (ENVO/label only) | causes | DNA double-strand breaks and clustered lesions (GO:0006302 candidate for DSB repair context) | Lourenço et al. 2023, Environmental Radiobiology, doi:10.1007/978-3-031-18810-7_9, https://doi.org/10.1007/978-3-031-18810-7_9 (lourenco2023environmentalradiobiology pages 11-13) | “ionizing radiation produces single- and double-strand DNA breaks, abasic sites and complex clustered lesions” | Strong general radiobiology edge; broad across taxa and foundational for trait scope. |
| growth medium / metabolic state (label only assay factor) | modulates | survival after gamma irradiation (label only phenotype) | Petit et al. 2023, Microorganisms, doi:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871 (petit2023firstisolationand pages 8-9) | “irradiation medium (LB vs NaCl) and active versus inactive metabolism influence survival” | Strong assay-context edge; should be marked experimental-factor rather than core mechanism. |
| radiation-tolerant cooling-pool isolates (label only microbial group) | remove_from_solution | U(VI) / uranyl (CHEBI:37336 candidate for uranyl ion) | Petit et al. 2023, Microorganisms, doi:10.3390/microorganisms11081871, https://doi.org/10.3390/microorganisms11081871 (petit2023firstisolationand pages 1-2, petit2023firstisolationand pages 8-9) | “Seven strains were able to remove almost all the uranium from a 5 µM solution” | Strong application edge for bioremediation, but not a core causal determinant of IR tolerance; keep separate from mechanism graph unless modeling downstream utility. |


*Table: This table lists candidate causal edges for curating microbial ionizing radiation tolerance, emphasizing experimentally supported mechanisms in Deinococcus and assay/application context from recent reactor and repository studies. It is useful as a starting set of subject-predicate-object triples with direct evidence, short snippets, and curation cautions.*

## 8) Expert interpretation and analysis (authoritative-source synthesis)
**Two-arm mechanistic picture supported across 2023–2024 literature:**
1) **DNA damage processing and repair control**: ionizing radiation generates DSBs/clustered lesions, requiring effective DDR regulation and repair capacity. The 2024 PprI/ssDNA work provides strong support that *Deinococcus* uses a dedicated SOS-independent derepression module (PprI→DdrO cleavage) triggered by ssDNA, with measurable induction of repair genes such as recA and uvrD. (lourenco2023environmentalradiobiology pages 11-13, lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5, lu2024thedeinococcusprotease pages 1-2)
2) **Oxidative proteome defense and metal homeostasis**: recent sRNA evidence (DrsS) reinforces the concept that maintaining Mn/Fe balance and antioxidant enzyme activity protects proteins from oxidative carbonylation, supporting survival under radiation-induced ROS stress. (rai2024anovelionizing pages 1-3)

**Curation implication:** The trait is best modeled as a *composite phenotype* emergent from **(i) lesion burden + repair capacity** and **(ii) oxidative/proteome protection**, with strong assay-context modifiers (medium, metabolic state, dose rate). (gregory2024radioactivewastemicrobiology pages 13-14, petit2023firstisolationand pages 8-9)

## 9) Warnings / claims not yet ready to curate (or curate as “uncertain”)
1) **“Mn/Fe ratio causes radioresistance”**: while widely cited as strongly correlated and mechanistically plausible, the causal generalization across diverse taxa is not fully established in the provided recent evidence set; curate as correlation/association unless direct perturbation evidence in non-*Deinococcus* taxa is added. (gregory2024radioactivewastemicrobiology pages 13-14)
2) **DrsS “stabilizes katA transcript”**: the binding interaction is directly supported, but stabilization/protection from endonucleases is phrased as “possibly”; mark this edge as **uncertain** unless additional in vivo transcript half-life evidence is curated. (rai2024anovelionizing pages 1-3)
3) **Repository survival limits**: compiled D10 values and “limits to life” in Gregory et al. (2024) are heterogeneous across organisms/matrices/dose rates; curate carefully with explicit context nodes (matrix, dose rate). (gregory2024radioactivewastemicrobiology pages 13-14)

---

# DOI-first bibliography (with dates and URLs)
- **Lu H. et al.** (2024-02). *The Deinococcus protease PprI senses DNA damage by directly interacting with single-stranded DNA.* **Nature Communications**. DOI: **10.1038/s41467-024-46208-9**. https://doi.org/10.1038/s41467-024-46208-9 (lu2024thedeinococcusprotease pages 7-8, lu2024thedeinococcusprotease pages 4-5, lu2024thedeinococcusprotease pages 1-2, lu2024thedeinococcusprotease pages 8-9, lu2024thedeinococcusprotease pages 9-10)
- **Rai S.N., Dutta T.** (2024-05). *A novel ionizing radiation-induced small RNA, DrsS, promotes the detoxification of reactive oxygen species in Deinococcus radiodurans.* **Applied and Environmental Microbiology**. DOI: **10.1128/aem.01538-23**. https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3)
- **Gregory S.P. et al.** (2024-01). *Radioactive waste microbiology: predicting microbial survival and activity in changing extreme environments.* **FEMS Microbiology Reviews**. DOI: **10.1093/femsre/fuae001**. https://doi.org/10.1093/femsre/fuae001 (gregory2024radioactivewastemicrobiology pages 13-14)
- **Pal S. et al.** (2024-06). *Unraveling radiation resistance strategies in two bacterial strains from the high background radiation area of Chavara-Neendakara: a comprehensive whole genome analysis.* **PLOS ONE**. DOI: **10.1371/journal.pone.0304810**. https://doi.org/10.1371/journal.pone.0304810 (pal2024unravelingradiationresistance pages 2-4, pal2024unravelingradiationresistance pages 44-45)
- **Petit P. et al.** (2023-07). *First Isolation and Characterization of Bacteria from the Core’s Cooling Pool of an Operating Nuclear Reactor.* **Microorganisms**. DOI: **10.3390/microorganisms11081871**. https://doi.org/10.3390/microorganisms11081871 (petit2023firstisolationand pages 1-2, petit2023firstisolationand pages 8-9, petit2023firstisolationand media 698b6292, petit2023firstisolationand media 8e4e84a6)
- **Subramani G., Srinivasan S.** (2023-09). *Involvement of Nucleotide Excision Repair and Rec-Dependent Pathway Genes for UV Radiation Resistance in Deinococcus irradiatisoli 17bor-2.* **Genes**. DOI: **10.3390/genes14091803**. https://doi.org/10.3390/genes14091803 (subramani2023involvementofnucleotide pages 1-2)
- **Lourenço J. et al.** (2023-01). *Environmental Radiobiology.* In: Radiobiology Textbook. DOI: **10.1007/978-3-031-18810-7_9**. https://doi.org/10.1007/978-3-031-18810-7_9 (lourenco2023environmentalradiobiology pages 11-13)
- **Krisko A., Radman M.** (2013-07). *Biology of extreme radiation resistance: the way of Deinococcus radiodurans.* **Cold Spring Harbor Perspectives in Biology**. DOI: **10.1101/cshperspect.a012765**. https://doi.org/10.1101/cshperspect.a012765 (foundational, referenced for Mn/Fe correlation context) (gregory2024radioactivewastemicrobiology pages 13-14)


References

1. (lourenco2023environmentalradiobiology pages 11-13): Joana Lourenço, Carmel Mothersill, Carmen Arena, Deborah Oughton, Margot Vanheukelom, Ruth Pereira, Sónia Mendo, and Veronica De Micco. Environmental radiobiology. Radiobiology Textbook, pages 469-501, Jan 2023. URL: https://doi.org/10.1007/978-3-031-18810-7\_9, doi:10.1007/978-3-031-18810-7\_9. This article has 16 citations.

2. (petit2023firstisolationand pages 8-9): Pauline Petit, Karim Hayoun, Béatrice Alpha-Bazin, Jean Armengaud, and Corinne Rivasseau. First isolation and characterization of bacteria from the core’s cooling pool of an operating nuclear reactor. Microorganisms, 11:1871, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081871, doi:10.3390/microorganisms11081871. This article has 6 citations.

3. (subramani2023involvementofnucleotide pages 1-2): Gayathri Subramani and Sathiyaraj Srinivasan. Involvement of nucleotide excision repair and rec-dependent pathway genes for uv radiation resistance in deinococcus irradiatisoli 17bor-2. Genes, 14:1803, Sep 2023. URL: https://doi.org/10.3390/genes14091803, doi:10.3390/genes14091803. This article has 6 citations.

4. (pal2024unravelingradiationresistance pages 2-4): Sowptika Pal, Ramani Yuvaraj, Hari Krishnan, Balasubramanian Venkatraman, Jayanthi Abraham, and Anilkumar Gopinathan. Unraveling radiation resistance strategies in two bacterial strains from the high background radiation area of chavara-neendakara: a comprehensive whole genome analysis. PLOS ONE, 19:e0304810, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0304810, doi:10.1371/journal.pone.0304810. This article has 8 citations and is from a peer-reviewed journal.

5. (gregory2024radioactivewastemicrobiology pages 13-14): Simon P Gregory, Jessica R M Mackie, and Megan J Barnett. Radioactive waste microbiology: predicting microbial survival and activity in changing extreme environments. FEMS Microbiology Reviews, Jan 2024. URL: https://doi.org/10.1093/femsre/fuae001, doi:10.1093/femsre/fuae001. This article has 14 citations and is from a domain leading peer-reviewed journal.

6. (lu2024thedeinococcusprotease pages 1-2): Huizhi Lu, Zijing Chen, Teng Xie, Shitong Zhong, Shasha Suo, Shuang Song, Liangyan Wang, Hong Xu, Bing Tian, Ye Zhao, Ruhong Zhou, and Yuejin Hua. The deinococcus protease ppri senses dna damage by directly interacting with single-stranded dna. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46208-9, doi:10.1038/s41467-024-46208-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

7. (lu2024thedeinococcusprotease pages 7-8): Huizhi Lu, Zijing Chen, Teng Xie, Shitong Zhong, Shasha Suo, Shuang Song, Liangyan Wang, Hong Xu, Bing Tian, Ye Zhao, Ruhong Zhou, and Yuejin Hua. The deinococcus protease ppri senses dna damage by directly interacting with single-stranded dna. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46208-9, doi:10.1038/s41467-024-46208-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (lu2024thedeinococcusprotease pages 4-5): Huizhi Lu, Zijing Chen, Teng Xie, Shitong Zhong, Shasha Suo, Shuang Song, Liangyan Wang, Hong Xu, Bing Tian, Ye Zhao, Ruhong Zhou, and Yuejin Hua. The deinococcus protease ppri senses dna damage by directly interacting with single-stranded dna. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46208-9, doi:10.1038/s41467-024-46208-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

9. (rai2024anovelionizing pages 1-3): Shiv Narayan Rai and Tanmay Dutta. A novel ionizing radiation-induced small rna, drss, promotes the detoxification of reactive oxygen species in <i>deinococcus radiodurans</i>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.01538-23, doi:10.1128/aem.01538-23. This article has 9 citations and is from a peer-reviewed journal.

10. (petit2023firstisolationand pages 1-2): Pauline Petit, Karim Hayoun, Béatrice Alpha-Bazin, Jean Armengaud, and Corinne Rivasseau. First isolation and characterization of bacteria from the core’s cooling pool of an operating nuclear reactor. Microorganisms, 11:1871, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081871, doi:10.3390/microorganisms11081871. This article has 6 citations.

11. (petit2023firstisolationand media 698b6292): Pauline Petit, Karim Hayoun, Béatrice Alpha-Bazin, Jean Armengaud, and Corinne Rivasseau. First isolation and characterization of bacteria from the core’s cooling pool of an operating nuclear reactor. Microorganisms, 11:1871, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081871, doi:10.3390/microorganisms11081871. This article has 6 citations.

12. (petit2023firstisolationand media 8e4e84a6): Pauline Petit, Karim Hayoun, Béatrice Alpha-Bazin, Jean Armengaud, and Corinne Rivasseau. First isolation and characterization of bacteria from the core’s cooling pool of an operating nuclear reactor. Microorganisms, 11:1871, Jul 2023. URL: https://doi.org/10.3390/microorganisms11081871, doi:10.3390/microorganisms11081871. This article has 6 citations.

13. (lu2024thedeinococcusprotease pages 8-9): Huizhi Lu, Zijing Chen, Teng Xie, Shitong Zhong, Shasha Suo, Shuang Song, Liangyan Wang, Hong Xu, Bing Tian, Ye Zhao, Ruhong Zhou, and Yuejin Hua. The deinococcus protease ppri senses dna damage by directly interacting with single-stranded dna. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46208-9, doi:10.1038/s41467-024-46208-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

14. (lu2024thedeinococcusprotease pages 9-10): Huizhi Lu, Zijing Chen, Teng Xie, Shitong Zhong, Shasha Suo, Shuang Song, Liangyan Wang, Hong Xu, Bing Tian, Ye Zhao, Ruhong Zhou, and Yuejin Hua. The deinococcus protease ppri senses dna damage by directly interacting with single-stranded dna. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46208-9, doi:10.1038/s41467-024-46208-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

15. (pal2024unravelingradiationresistance pages 44-45): Sowptika Pal, Ramani Yuvaraj, Hari Krishnan, Balasubramanian Venkatraman, Jayanthi Abraham, and Anilkumar Gopinathan. Unraveling radiation resistance strategies in two bacterial strains from the high background radiation area of chavara-neendakara: a comprehensive whole genome analysis. PLOS ONE, 19:e0304810, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0304810, doi:10.1371/journal.pone.0304810. This article has 8 citations and is from a peer-reviewed journal.