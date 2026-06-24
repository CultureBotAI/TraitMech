---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:08:39.134031'
end_time: '2026-06-18T01:28:41.093561'
duration_seconds: 1201.96
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: radiotolerant
  trait_identifier: traitmech:000007
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: radiotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental tolerance in which an organism survives doses of ionizing
    and/or ultraviolet radiation that are lethal to most microorganisms, typically
    via efficient DNA repair and oxidative-damage protection.
  parent_traits: METPO:1000059
  synonyms: radioresistant
  evidence_summary: 'DOI:10.1101/cshperspect.a012765: A strong correlation has been
    shown between intracellular Mn/Fe concentration ratios and bacterial resistance
    to radiation (Review of extreme radiation resistance supports manganese-antioxidant
    protection of the proteome as a core radiotolerance mechanism in Deinococcus radiodurans,
    "a champion of extreme radiation resistance".) | DOI:10.3390/genes14091803: Deinococcus
    radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example
    of such an organism, showcasing an impressive resistance to a wide array of stressors,
    including ionizing radiation, desiccation, UV radiation, and oxidizing agents
    (Organism example: Deinococcus radiodurans tolerates ionizing radiation, UV radiation,
    and desiccation.)'
  causal_graph_summary: 'radiotolerance_repair_antioxidant: 4 nodes, 3 edges'
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
- **Trait label:** radiotolerant
- **METPO identifier:** traitmech:000007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives doses of ionizing and/or ultraviolet radiation that are lethal to most microorganisms, typically via efficient DNA repair and oxidative-damage protection.
- **Parent traits:** METPO:1000059
- **Synonyms:** radioresistant
- **Existing evidence:** DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Review of extreme radiation resistance supports manganese-antioxidant protection of the proteome as a core radiotolerance mechanism in Deinococcus radiodurans, "a champion of extreme radiation resistance".) | DOI:10.3390/genes14091803: Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example of such an organism, showcasing an impressive resistance to a wide array of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents (Organism example: Deinococcus radiodurans tolerates ionizing radiation, UV radiation, and desiccation.)
- **Existing causal graph summary:** radiotolerance_repair_antioxidant: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **radiotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/radiotolerant.yaml`.

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
- **Trait label:** radiotolerant
- **METPO identifier:** traitmech:000007
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives doses of ionizing and/or ultraviolet radiation that are lethal to most microorganisms, typically via efficient DNA repair and oxidative-damage protection.
- **Parent traits:** METPO:1000059
- **Synonyms:** radioresistant
- **Existing evidence:** DOI:10.1101/cshperspect.a012765: A strong correlation has been shown between intracellular Mn/Fe concentration ratios and bacterial resistance to radiation (Review of extreme radiation resistance supports manganese-antioxidant protection of the proteome as a core radiotolerance mechanism in Deinococcus radiodurans, "a champion of extreme radiation resistance".) | DOI:10.3390/genes14091803: Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example of such an organism, showcasing an impressive resistance to a wide array of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents (Organism example: Deinococcus radiodurans tolerates ionizing radiation, UV radiation, and desiccation.)
- **Existing causal graph summary:** radiotolerance_repair_antioxidant: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **radiotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/radiotolerant.yaml`.

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


## Microbial radiotolerance (TraitMech: radiotolerant; traitmech:000007) — curation-focused research report

### 1) Scope summary (trait definition, boundaries, and current understanding)

**Trait meaning (phenotype):** Microbial *radiotolerance* (syn. radioresistance) is an environmental tolerance phenotype describing the capacity to survive (and sometimes maintain growth) after exposure to ionizing radiation (IR; e.g., γ-rays, X-rays) and/or ultraviolet radiation (often UV‑C in lab assays). Quantification commonly uses **D10**, the acute dose at which **10%** of cells remain viable (colony-forming) (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4). 

**Operational thresholds / boundary cases:** A recent machine-learning framework (TolRad) formalizes a practical boundary for bacterial classification: **radiosensitive** if **D10 < 200 Gy** and **radiation-tolerant** if **D10 > 200 Gy**; the D10 distribution and this cutoff are shown in Figure 1 of Sweet et al. 2024 (sweet2024tolradamodel media e020062b). This is an assay-conditioned definition: TolRad’s curated training set limited D10s to acute γ/X-ray exposures performed at room temperature in liquid media or PBS, reflecting how strongly exposure conditions influence measured tolerance (sweet2024tolradamodel pages 2-4). 

**Distinguishing from nearby traits:** Radiotolerance overlaps mechanistically with oxidative-stress tolerance (because IR generates ROS) and often correlates with desiccation tolerance, but it is distinct as a phenotype: radiotolerance is *defined by survival/growth under radiation exposure* rather than survival under drying or oxidants alone (lourenco2023environmentalradiobiology pages 11-13). 

**What it is not:** Radiotolerance is not synonymous with spore formation or generic stress tolerance. In fact, radiotolerance can vary widely among non-spore-formers; across bacteria, D10 can range from ~60–70 Gy in sensitive species to >10,000 Gy in extremophiles (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4). 

### 2) Recent developments (prioritizing 2023–2024)

#### 2.1 Trait quantification and prediction from genomes (2024)
Sweet et al. (Microbiology Spectrum, 2024) developed **TolRad**, a Pfam-frequency-based classifier for predicting IR tolerance using curated D10 data across 61 bacterial species, and explicitly used the **D10 < 200 Gy** radiosensitive threshold (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4). The paper also reiterates the field consensus that the **intracellular Mn/Fe ratio** is a leading predictor of IR tolerance and notes it is assay-dependent (growth medium affects Mn/Fe) (sweet2024tolradamodel pages 2-4). 

#### 2.2 Regulatory RNAs as radiotolerance modulators (2024)
Rai & Dutta (Applied and Environmental Microbiology, 2024) identified a **γ‑radiation-induced small RNA (sRNA), DrsS**, in *Deinococcus radiodurans* and demonstrated that deleting drsS:
- impairs growth under γ‑radiation,
- depletes intracellular **Mn2+ (~70%)** and **Fe2+ (~40%)**,
- increases **protein carbonylation** (oxidative protein damage), and
- increases sensitivity to oxidative stress; complementation restores metals and reduces carbonylation (rai2024anovelionizing pages 1-3).
Mechanistically, DrsS **directly interacts with the katA transcript** and rescues oxidative-stress resistance via **catalase-mediated ROS detoxification** (rai2024anovelionizing pages 1-3).

#### 2.3 Double-strand break (DSB) repair pathway choice as a control point (2024)
Sharma et al. (Applied and Environmental Microbiology, 2024) provided experimental evidence that **DprA**, a protein classically associated with natural transformation, **coordinates DSB repair pathway choice** in heavily irradiated *D. radiodurans*, balancing **RecA-independent SSA** and **RecA-dependent ESDSA/HR**, with measurable effects on survival under γ-radiation, UV, and mitomycin C (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14). 

#### 2.4 Radiation-resistant bacteria beyond *Deinococcus* with actionable gene differences (2024)
Pal et al. (PLOS ONE, 2024) characterized two mid-range radiotolerant Firmicutes from a high background radiation area and reported **D10 values of 2.32 kGy vs 1.42 kGy** for *Metabacillus halosaccharovorans* (VITHBRA001) vs *Bacillus paralicheniformis* (VITHBRA024), respectively (pal2024unravelingradiationresistance pages 1-2). They proposed that the higher D10 strain’s presence of **uvsE**, **frnE**, **ppk1**, **ppx**, and **carotenoid biosynthesis genes** (absent in the lower D10 strain) could explain improved resistance (pal2024unravelingradiationresistance pages 1-2). 

### 3) Current applications and real-world implementations

**Bioremediation and radioactive environments:** Environmental radiobiology literature emphasizes that microorganisms contribute to **radionuclide mobility and decontamination** via reduction, uptake/accumulation, biosorption, and biomineralization, supporting interest in radiotolerant taxa for contaminated sites (lourenco2023environmentalradiobiology pages 11-13). 

**Metagenomics / community risk assessment:** TolRad exemplifies practical deployment: predicting radiosensitive taxa from reference proteomes and MAGs to support (i) mechanistic prioritization of sensitive species and (ii) identification of potential biomarkers of IR exposure in microbiomes (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4). 

**Biotechnology for stress-hardening:** Experimental evolution can increase bacterial IR resistance (e.g., *E. coli* selection increased the dose to kill 99% from ~750 Gy to ~3000 Gy), motivating engineering approaches where radiotolerant modules (repair + antioxidant/metal homeostasis) can be introduced or tuned (lourenco2023environmentalradiobiology pages 11-13).

### 4) Expert opinions and analysis (authoritative synthesis)

**Consensus model (two coupled pillars):** Across sources, radiotolerance is best explained by the **coupling of (i) exceptional DNA repair capacity** (particularly DSB repair and UV lesion repair) and **(ii) oxidative damage management/proteome protection**. Environmental radiobiology notes that many DNA repair proteins exist in both tolerant and sensitive microbes, implying that **repair efficiency/regulation and integration with antioxidant strategies** are decisive (lourenco2023environmentalradiobiology pages 11-13). 

**Metal-centered oxidative protection as a unifying axis:** Sweet et al. (2024) summarize the Mn/Fe model: iron promotes ROS spread (Fenton chemistry) while manganese acts antioxidatively; thus Mn/Fe ratio links intracellular chemistry to radiation outcomes (sweet2024tolradamodel pages 2-4). Rai & Dutta (2024) add mechanistic depth by connecting an sRNA regulator to metal homeostasis, protein oxidation, and catalase-mediated ROS detoxification (rai2024anovelionizing pages 1-3). 

**Repair pathway choice matters (not only presence):** Sharma et al. (2024) highlight that radiotolerance can depend on *how* repair pathways are deployed temporally and competitively—DprA modulates the balance between early SSA and later ESDSA/HR, with survival consequences (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14).

### 5) Statistics and quantitative data (recent studies)

- **Trait range:** Species can succumb to acute IR doses as low as **~60 Gy**, while extremophiles can survive **>10,000 Gy** (sweet2024tolradamodel pages 1-2). 
- **Benchmark D10s:** *Deinococcus radiodurans* D10 reported as **12,000 Gy** vs *Shewanella oneidensis* D10 **~70 Gy** (sweet2024tolradamodel pages 2-4). 
- **Operational cutoff used in 2024 TolRad:** radiosensitive **D10 < 200 Gy**; tolerant **D10 > 200 Gy**; D10 distribution shown in **Figure 1** (sweet2024tolradamodel media e020062b). 
- **Mid-range radiotolerant Firmicutes (2024):** D10 = **2.32 kGy** (VITHBRA001, *Metabacillus halosaccharovorans*) vs **1.42 kGy** (VITHBRA024, *Bacillus paralicheniformis*) (pal2024unravelingradiationresistance pages 1-2). 
- **Dose-rate tolerance (2023):** *D. radiodurans* described as resistant to **acute IR up to 15 kGy** and **chronic radiation ~60 Gy/h**, with Deinococci vegetative cells tolerating >100 Gy/h in some contexts (lourenco2023environmentalradiobiology pages 11-13). 
- **Metal homeostasis effect size (2024):** deleting drsS depleted intracellular Mn2+ by **~70%** and Fe2+ by **~40%**, with increased protein carbonylation; complementation reversed these changes (rai2024anovelionizing pages 1-3). 

---

## Curation-ready content for `data/traits/environment/radiotolerant.yaml`

### A) Candidate nodes grouped by type (with grounding suggestions)

| Node label | Node type | Suggested ontology grounding | Notes |
|---|---|---|---|
| ionizing radiation | environmental factor | ENVO:01001024 | Core exposure defining the trait; acute gamma/X-ray exposure commonly used in D10 assays for bacterial radiotolerance (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4, lourenco2023environmentalradiobiology pages 11-13) |
| ultraviolet radiation (UV-C) | environmental factor | ENVO:01001680 | Important boundary-case exposure for “radioresistant” phenotypes; causes thymine dimers/photoproducts and selects for NER/UvdE/UvsE systems (subramani2023involvementofnucleotide pages 1-2, subramani2023involvementofnucleotide pages 5-7) |
| reactive oxygen species (ROS) | chemical | CHEBI:26523 | Indirect products of radiolysis and major damage mediators; detoxification is a central radiotolerance mechanism (tan2025radiationresistantbacteriapotential pages 5-8, rai2024anovelionizing pages 13-14, rai2024anovelionizing pages 1-3) |
| DNA double-strand break repair | process | GO:0006302 | Central process for surviving ionizing radiation; includes ESDSA, SSA, HR, and other end-joining-related activities in some taxa (pal2024unravelingradiationresistance pages 32-34, sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| homologous recombination | process | GO:0000724 | RecA-centered repair route contributing to genome reassembly after irradiation; especially prominent in Deinococcus (tan2025radiationresistantbacteriapotential pages 5-8, pal2024unravelingradiationresistance pages 32-34) |
| RecA | gene/protein | GO:0003697 | DNA recombinase; essential for RecA-dependent repair and strongly associated with radiation survival in Deinococcus and broader bacteria (tan2025radiationresistantbacteriapotential pages 5-8, subramani2023involvementofnucleotide pages 7-9) |
| RecFOR complex | protein | unresolved | RecA-loading/mediator system on ssDNA; implicated in pathway choice and resistance, especially in Deinococcus DSB repair models (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| extended synthesis-dependent strand annealing (ESDSA) | pathway | unresolved | Deinococcus-associated genome reassembly pathway after heavy irradiation; RecA-dependent and important for extensive DSB repair (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| single-strand annealing (SSA) | pathway | GO:0010792 | RecA-independent DSB repair route in Deinococcus; supported by DdrB/DdrA and modulated relative to ESDSA by DprA (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| DprA | gene/protein | unresolved | Natural transformation protein with repair-pathway coordination role in heavily irradiated D. radiodurans; affects SSA vs ESDSA balance and survival after gamma/UV/MMC (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| DdrA | gene/protein | unresolved | Deinococcus-specific DNA damage response protein; protects DNA ends from nuclease degradation and supports SSA-like repair context (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| DdrB | gene/protein | unresolved | Deinococcus-specific ssDNA annealing protein; central to SSA and short-homology annealing linked to ESDSA intermediates (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| nucleotide excision repair (NER) | process | GO:0006289 | Key pathway for UV-induced helix-distorting lesions and also implicated in broader radiation damage responses (subramani2023involvementofnucleotide pages 1-2, subramani2023involvementofnucleotide pages 5-7) |
| UvrABC excinuclease | protein | unresolved | Canonical bacterial NER machinery detecting/incising UV-damaged DNA; genomic evidence in Deinococcus irradiatisoli and other radiotolerant bacteria (subramani2023involvementofnucleotide pages 1-2, subramani2023involvementofnucleotide pages 7-9, subramani2023involvementofnucleotide pages 5-7) |
| UV damage endonuclease (UvsE/UVDE/UvdE) | gene/protein | unresolved | Alternative UV lesion repair endonuclease; reported as UvdE/UVDE-like in Deinococcus and as uvsE in mid-range radiotolerant Firmicutes (pal2024unravelingradiationresistance pages 1-2, subramani2023involvementofnucleotide pages 5-7) |
| catalase KatA | gene/protein | GO:0004096 | ROS-detoxifying enzyme; in D. radiodurans, DrsS interacts with katA transcript and promotes catalase-mediated oxidative stress resistance (rai2024anovelionizing pages 13-14, rai2024anovelionizing pages 1-3) |
| Mn2+ | chemical | CHEBI:29035 | Protective manganese pool associated with radiotolerance and proteome shielding against oxidative damage (rai2024anovelionizing pages 13-14, rai2024anovelionizing pages 1-3, sweet2024tolradamodel pages 2-4) |
| Fe2+ | chemical | CHEBI:29033 | Iron pool relevant to oxidative damage via Fenton chemistry; lower relative Fe or higher Mn/Fe ratio correlates with tolerance (rai2024anovelionizing pages 13-14, sweet2024tolradamodel pages 2-4) |
| Mn/Fe ratio | assay metric | unresolved | Best-understood predictor of bacterial IR tolerance in comparative studies; higher values correlate with survival (sweet2024tolradamodel pages 2-4) |
| protein carbonylation | process | GO:0006481 | Readout of oxidative protein damage; reduced when DrsS maintains Mn/Fe homeostasis in D. radiodurans (rai2024anovelionizing pages 13-14, rai2024anovelionizing pages 1-3) |
| carotenoids | chemical | CHEBI:23044 | Non-enzymatic antioxidants/pigments contributing to ROS scavenging and UV/oxidative protection in radiotolerant bacteria (abbaszadeh2024theecologyand pages 24-28, tan2025radiationresistantbacteriapotential pages 5-8, pal2024unravelingradiationresistance pages 1-2) |
| deinoxanthin | chemical | unresolved | Deinococcus carotenoid specifically highlighted as a powerful ROS scavenger supporting radiation resistance (tan2025radiationresistantbacteriapotential pages 5-8, abbaszadeh2024theecologyand pages 24-28) |
| ppk1 | gene/protein | unresolved | Polyphosphate kinase; in HBRA strain comparison, presence is associated with better radiation resistance, likely via non-enzymatic protective metabolite production (pal2024unravelingradiationresistance pages 1-2) |
| ppx | gene/protein | unresolved | Exopolyphosphatase; co-mentioned with ppk1 as part of non-enzymatic metabolite production linked to higher resistance in VITHBRA001 (pal2024unravelingradiationresistance pages 1-2) |
| frnE | gene/protein | unresolved | Protein-protection gene; present in the more radiation-resistant HBRA strain and proposed to contribute to D10 difference (pal2024unravelingradiationresistance pages 1-2) |
| PprA | gene/protein | unresolved | Deinococcus DNA repair protein associated with DSB repair; discussed in pathway-interaction context with DprA (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) |
| PprI / IrrE | gene/protein | unresolved | Global regulator/protease-like response factor in Deinococcus DNA damage response networks; linked in comparative/genomic review context to radiation resistance regulation (pal2024unravelingradiationresistance pages 32-34) |
| DdrO | gene/protein | unresolved | Deinococcus transcriptional repressor in the IrrE/DdrO DNA damage response module; part of radiation-responsive regulatory network (pal2024unravelingradiationresistance pages 32-34) |
| D10 (dose for 10% survival) | assay metric | unresolved | Standard quantitative phenotype metric for radiotolerance; examples range from ~70 Gy in S. oneidensis to ~12,000 Gy in D. radiodurans; TolRad uses 200 Gy cutoff for tolerant vs sensitive (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4) |
| Deinococcus radiodurans | environmental factor | NCBITaxon:1299 | Exemplar extreme radiotolerant bacterium; model for Mn/Fe homeostasis, ESDSA/SSA, DrsS, PprA and Ddr pathways (rai2024anovelionizing pages 13-14, rai2024anovelionizing pages 1-3, sharma2024naturaltransformationspecificdpra pages 10-12) |
| Deinococcus irradiatisoli | environmental factor | NCBITaxon:unresolved | Deinococcus species with genomic evidence for UvrABC, RecA/RecQ and UvdE-mediated UV resistance mechanisms (subramani2023involvementofnucleotide pages 1-2, subramani2023involvementofnucleotide pages 5-7) |
| Bacillus paralicheniformis | environmental factor | NCBITaxon:2745623 | Mid-range radiotolerant HBRA isolate used in comparative genomics; lower D10 than paired Metabacillus strain and lacks several candidate protection genes (pal2024unravelingradiationresistance pages 1-2) |
| Metabacillus halosaccharovorans | environmental factor | NCBITaxon:2033715 | Mid-range radiotolerant HBRA isolate with higher D10 and unique genes (uvsE, frnE, ppk1, ppx, carotenoid biosynthesis) proposed to explain stronger resistance (pal2024unravelingradiationresistance pages 1-2) |
| Escherichia coli | environmental factor | NCBITaxon:562 | Reference comparatively radiosensitive bacterium; experimental evolution and comparative context help define boundary of trait (lourenco2023environmentalradiobiology pages 11-13, pal2024unravelingradiationresistance pages 1-2) |
| Shewanella oneidensis | environmental factor | NCBITaxon:70863 | Strongly radiosensitive comparator with D10 ~70 Gy in trait-definition literature; used in Mn/Fe comparisons (sweet2024tolradamodel pages 2-4) |


*Table: This table lists candidate entities for a radiotolerant TraitMech graph, grouped across exposures, pathways, genes/proteins, chemicals, and assay metrics. It emphasizes conservative ontology grounding and notes each node’s likely mechanistic role and taxon scope based on the cited evidence.*

### B) Candidate evidence-backed causal edges (triples)

| Subject | Predicate | Object | Evidence snippet (quote) | Source (DOI + URL + year) | Notes/uncertainty | Suggested node grounding (CURIEs if available) |
|---|---|---|---|---|---|---|
| ionizing radiation | causes | reactive oxygen species (ROS) | "Another aftermath of irradiation is the production of reactive oxygen species (ROS)" (pal2024unravelingradiationresistance pages 1-2) | DOI:10.1371/journal.pone.0304810 · https://doi.org/10.1371/journal.pone.0304810 · 2024 | General mechanism across microbes; supports environmental-factor-to-damage edge. | ionizing radiation: ENVO:01001024; ROS: CHEBI:26523 |
| DrsS | maintains | intracellular Mn2+/Fe2+ homeostasis | "Deletion of the drsS gene resulted in the depletion of intracellular concentration of both Mn2+ and Fe2+ by ~70% and 40%, respectively" (rai2024anovelionizing pages 1-3) | DOI:10.1128/aem.01538-23 · https://doi.org/10.1128/aem.01538-23 · 2024 | Strong, taxon-specific to *D. radiodurans*; homeostasis inferred from loss and complementation. | DrsS: unresolved; Mn2+: CHEBI:29035; Fe2+: CHEBI:29033 |
| DrsS | reduces | protein carbonylation | "Complementation of drsS gene in ΔdrsS cells helped revert its intracellular Mn2+ and Fe2+ concentration and alleviated carbonylation of intracellular proteins" (rai2024anovelionizing pages 1-3) | DOI:10.1128/aem.01538-23 · https://doi.org/10.1128/aem.01538-23 · 2024 | Strong for *D. radiodurans*; likely mediated by metal homeostasis and antioxidant defense. | DrsS: unresolved; protein carbonylation: GO:0006481 |
| DrsS | interacts with/stabilizes transcript of | katA catalase | "In vitro binding assays indicated that DsrS directly interacts with the coding region of the katA transcript" (rai2024anovelionizing pages 1-3) | DOI:10.1128/aem.01538-23 · https://doi.org/10.1128/aem.01538-23 · 2024 | Direct molecular evidence; mechanism described as likely transcript protection from endonucleases. | DrsS: unresolved; KatA/catalase: GO:0004096 |
| DrsS | promotes | catalase-mediated ROS detoxification | "Extrachromosomally expressed drsS in ΔdrsS cells retrieved its oxidative stress resistance properties by catalase-mediated detoxification of reactive oxygen species (ROS)" (rai2024anovelionizing pages 1-3) | DOI:10.1128/aem.01538-23 · https://doi.org/10.1128/aem.01538-23 · 2024 | Strong, taxon-specific; bridges regulator to antioxidant phenotype. | DrsS: unresolved; ROS: CHEBI:26523; catalase activity: GO:0004096 |
| high intracellular Mn/Fe ratio | positively correlates with | ionizing-radiation tolerance | "The best-understood predictor of IR tolerance in bacteria is the intracellular ratio of manganese to iron (Mn/Fe)" and "the intracellular ratio of Mn/Fe is correlated with IR tolerance" (sweet2024tolradamodel pages 2-4) | DOI:10.1128/spectrum.03838-23 · https://doi.org/10.1128/spectrum.03838-23 · 2024 | Correlative rather than direct intervention; still high-value trait-level edge. | Mn/Fe ratio: unresolved; IR tolerance: unresolved |
| Fe2+ | promotes | ROS spread via Fenton chemistry | "Iron furthers the spread of ROS through Fenton chemistry" (sweet2024tolradamodel pages 2-4) | DOI:10.1128/spectrum.03838-23 · https://doi.org/10.1128/spectrum.03838-23 · 2024 | Mechanistic explanation supporting Mn/Fe ratio association with tolerance. | Fe2+: CHEBI:29033; ROS: CHEBI:26523 |
| Mn2+ | acts as antioxidant against | ROS | "whereas manganese is an antioxidant, acting as a sponge of ROS" (sweet2024tolradamodel pages 2-4) | DOI:10.1128/spectrum.03838-23 · https://doi.org/10.1128/spectrum.03838-23 · 2024 | General bacterial mechanism; supports metal-based protection node. | Mn2+: CHEBI:29035; ROS: CHEBI:26523 |
| DprA | coordinates pathway choice between | SSA and ESDSA/HR | "DprA is instrumental in selecting DNA double-strand break repair pathways" and it is "crucial in the selection between SSA and ESDSA pathways" (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) | DOI:10.1128/aem.01948-23 · https://doi.org/10.1128/aem.01948-23 · 2024 | Strong, specific to heavily irradiated *D. radiodurans*; pathway-choice regulator rather than core repair enzyme. | DprA: unresolved; SSA: GO:0010792; ESDSA: unresolved |
| loss of DprA | increases sensitivity to | gamma radiation / UV / MMC | "ΔdprA mutants show increased susceptibility to gamma radiation, UV and MMC" (sharma2024naturaltransformationspecificdpra pages 10-12) | DOI:10.1128/aem.01948-23 · https://doi.org/10.1128/aem.01948-23 · 2024 | Strong phenotype evidence; supports DprA contribution to radiotolerance. | DprA: unresolved; UV radiation: ENVO:01001680 |
| DdrB | promotes | SSA / short-homology annealing | "DdrB and DdrA are central to SSA (DdrB aids annealing; DdrA limits nuclease degradation)" (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) | DOI:10.1128/aem.01948-23 · https://doi.org/10.1128/aem.01948-23 · 2024 | Taxon-specific to *Deinococcus* damage-response system. | DdrB: unresolved; SSA: GO:0010792 |
| DdrA | limits nuclease degradation of | damaged DNA ends | "DdrB and DdrA are central to SSA (DdrB aids annealing; DdrA limits nuclease degradation)" (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14) | DOI:10.1128/aem.01948-23 · https://doi.org/10.1128/aem.01948-23 · 2024 | Supports protective DNA-end stabilization during early post-irradiation repair. | DdrA: unresolved; DNA double-strand break repair: GO:0006302 |
| RecA | mediates | homologous recombination / ESDSA-associated repair | "HR is central for double-strand break repair, with RecA abundant (~11,000 molecules/cell) and RecA expression increasing eightfold after 15 kGy" (tan2025radiationresistantbacteriapotential pages 4-5, tan2025radiationresistantbacteriapotential pages 5-8) | DOI:10.3390/su17177864 · https://doi.org/10.3390/su17177864 · 2025 | Review source, but quantitative and mechanistically explicit; useful for general edge. | RecA: GO:0003697; homologous recombination: GO:0000724 |
| RecA | contributes to | survival after radiation and UV | "recA mutations increase susceptibility to ionizing radiation and UV" (subramani2023involvementofnucleotide pages 7-9) | DOI:10.3390/genes14091803 · https://doi.org/10.3390/genes14091803 · 2023 | Strong but framed from prior literature summarized in review/genome paper. | RecA: GO:0003697 |
| UvrABC excinuclease / NER | repairs | UV-induced helix-distorting lesions | "UvrA is described as the initial damage sensor in nucleotide excision repair (NER), recruiting UvrB and, with UvrC, performing a dual-incision to remove damaged DNA" (subramani2023involvementofnucleotide pages 7-9) | DOI:10.3390/genes14091803 · https://doi.org/10.3390/genes14091803 · 2023 | Strong mechanistic edge for UV-resistance module. | NER: GO:0006289; UvrABC: unresolved |
| UvrABC excinuclease / NER | enables | UV radiation resistance | "The genome analysis of strain 17bor-2 revealed evidence of excinuclease UvrABC genes, which are key enzymes in the nucleotide excision repair (NER) mechanism" for "UV radiation resistance" (subramani2023involvementofnucleotide pages 1-2) | DOI:10.3390/genes14091803 · https://doi.org/10.3390/genes14091803 · 2023 | Genomic-plus-review evidence; less direct than knockout study but curation-worthy. | UvrABC: unresolved; UV resistance: unresolved |
| UvdE/UVDE/UvsE | repairs | UV damage | "The strain encodes a UV damage repair endonuclease called UvdE" and "UvdE likely contributes to strong UV resistance" (subramani2023involvementofnucleotide pages 5-7) | DOI:10.3390/genes14091803 · https://doi.org/10.3390/genes14091803 · 2023 | Strong for UV-specific branch; naming varies across taxa (UvdE/UVDE/UvsE). | UvdE/UvsE: unresolved |
| presence of uvsE, frnE, ppk1, ppx, carotenoid biosynthesis genes | contributes to | higher D10 / better radiation resistance | "the genes such as uvsE (NER), frnE (protein protection), ppk1 and ppx (non-enzymatic metabolite production) and those for carotenoid biosynthesis, are endogenous to VITHBRA001, but absent in VITHBRA024, which could explain the former’s better radiation resistance" (pal2024unravelingradiationresistance pages 1-2) | DOI:10.1371/journal.pone.0304810 · https://doi.org/10.1371/journal.pone.0304810 · 2024 | Comparative genomic inference tied to measured D10 difference (2.32 vs 1.42 kGy); curate as uncertain/composite edge. | uvsE/frnE/ppk1/ppx: unresolved; carotenoids: CHEBI:23044; D10: unresolved |
| carotenoids / deinoxanthin | scavenge | ROS | "The carotenoid deinoxanthin scavenges ROS quantitatively (removed up to 69.7% H2O2 and quenched singlet oxygen up to 99%)" (tan2025radiationresistantbacteriapotential pages 5-8) | DOI:10.3390/su17177864 · https://doi.org/10.3390/su17177864 · 2025 | Quantitative review evidence; supports non-enzymatic antioxidant branch. | carotenoids: CHEBI:23044; deinoxanthin: unresolved; ROS: CHEBI:26523 |
| carotenoids | protect against | UV/oxidative stress and radiation damage | "Carotenoid pigment deinoxanthin acts as an ROS scavenger; knockout of carotenoid biosynthesis increases UV/oxidative sensitivity" (abbaszadeh2024theecologyanda pages 24-28, abbaszadeh2024theecologyand pages 24-28) | DOI unavailable in context excerpt (Abbaszadeh 2024 thesis/source excerpt) · URL unavailable in context excerpt · 2024 | Useful mechanistic support, but bibliographic metadata incomplete in provided context; mark uncertain for direct curation until source finalized. | carotenoids: CHEBI:23044 |
| D10 phenotype | distinguishes | radiosensitive vs radiotolerant bacteria | "radiosensitive (D10 < 200 Gy) and radiation-tolerant (D10 > 200 Gy) bacteria" (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4, sweet2024tolradamodel media e020062b) | DOI:10.1128/spectrum.03838-23 · https://doi.org/10.1128/spectrum.03838-23 · 2024 | Assay-definition edge for trait scope, not mechanism per se; useful metadata for curation thresholds. | D10: unresolved |


*Table: This table compiles evidence-backed candidate causal edges for microbial radiotolerance, spanning radiation-induced ROS damage, metal homeostasis, DNA repair pathway choice, and antioxidant protection. It is useful as a curation-ready starting point for selecting TraitMech triples and flagging which claims are direct versus correlative or taxon-specific.*

---

## Warnings / curation cautions (claims not yet ready for strong curation)

1. **Correlation vs causation (Mn/Fe):** The Mn/Fe ratio is repeatedly described as a leading predictor, but much of the evidence is **correlative** across taxa and sensitive to growth conditions; curate as *association* unless a specific intervention study is available in the evidence set (sweet2024tolradamodel pages 2-4).
2. **Comparative gene presence → D10 differences:** Pal et al. infer that presence/absence of uvsE/frnE/ppk1/ppx/carotenoid genes “could explain” D10 differences; this is plausible but remains **comparative and multi-factorial** without direct knockouts in those strains (pal2024unravelingradiationresistance pages 1-2). Mark such edges as *uncertain* or *hypothesized*.
3. **Secondary sources lacking full bibliographic metadata:** The Deinococcaceae ecology/evolution excerpt provides useful mechanistic statements (Mn-proteome protection, carotenoid knockout sensitivity), but the tool state does not provide complete publication metadata; avoid hard-curating these as primary evidence until source identity/DOI is confirmed (abbaszadeh2024theecologyand pages 24-28, abbaszadeh2024theecologyanda pages 24-28).

---

## DOI-first bibliography (with dates and URLs where available)

1. **Sweet P, Burroughs MR, Jang S, Contreras LM.** TolRad, a model for predicting radiation tolerance using Pfam annotations, identifies novel radiosensitive bacterial species from reference genomes and MAGs. *Microbiology Spectrum.* Published **2024-09-05**. DOI: **10.1128/spectrum.03838-23**. URL: https://doi.org/10.1128/spectrum.03838-23 (sweet2024tolradamodel pages 1-2, sweet2024tolradamodel pages 2-4, sweet2024tolradamodel media e020062b)
2. **Rai SN, Dutta T.** A novel ionizing radiation-induced small RNA, DrsS, promotes the detoxification of reactive oxygen species in *Deinococcus radiodurans*. *Applied and Environmental Microbiology.* Published **2024-04-08**. DOI: **10.1128/aem.01538-23**. URL: https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3)
3. **Sharma DK, Soni I, Misra HS, Rajpurohit YS.** Natural transformation-specific DprA coordinate DNA double-strand break repair pathways in heavily irradiated *D. radiodurans*. *Applied and Environmental Microbiology.* Published **2024-02**. DOI: **10.1128/aem.01948-23**. URL: https://doi.org/10.1128/aem.01948-23 (sharma2024naturaltransformationspecificdpra pages 10-12, sharma2024naturaltransformationspecificdpra pages 12-14)
4. **Pal S, Yuvaraj R, Krishnan H, Venkatraman B, Abraham J, Gopinathan A.** Unraveling radiation resistance strategies in two bacterial strains from the high background radiation area of Chavara-Neendakara: A comprehensive whole genome analysis. *PLOS ONE.* Published **2024-06-10**. DOI: **10.1371/journal.pone.0304810**. URL: https://doi.org/10.1371/journal.pone.0304810 (pal2024unravelingradiationresistance pages 1-2)
5. **Subramani G, Srinivasan S.** Involvement of Nucleotide Excision Repair and Rec-Dependent Pathway Genes for UV Radiation Resistance in *Deinococcus irradiatisoli* 17bor-2. *Genes.* Published **2023-09-15**. DOI: **10.3390/genes14091803**. URL: https://doi.org/10.3390/genes14091803 (subramani2023involvementofnucleotide pages 1-2, subramani2023involvementofnucleotide pages 7-9, subramani2023involvementofnucleotide pages 5-7)
6. **Lourenço J, Mothersill C, Arena C, et al.** Environmental Radiobiology. In: *Radiobiology Textbook.* Published **2023**. DOI: **10.1007/978-3-031-18810-7_9**. URL: https://doi.org/10.1007/978-3-031-18810-7_9 (lourenco2023environmentalradiobiology pages 11-13)

### Image citation
- Figure showing D10 distribution and D10<200 Gy cutoff from Sweet et al. 2024 (sweet2024tolradamodel media e020062b).


References

1. (sweet2024tolradamodel pages 1-2): Philip Sweet, Matthew R. Burroughs, Sungyeon Jang, and Lydia M. Contreras. Tolrad, a model for predicting radiation tolerance using pfam annotations, identifies novel radiosensitive bacterial species from reference genomes and mags. Oct 2024. URL: https://doi.org/10.1128/spectrum.03838-23, doi:10.1128/spectrum.03838-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (sweet2024tolradamodel pages 2-4): Philip Sweet, Matthew R. Burroughs, Sungyeon Jang, and Lydia M. Contreras. Tolrad, a model for predicting radiation tolerance using pfam annotations, identifies novel radiosensitive bacterial species from reference genomes and mags. Oct 2024. URL: https://doi.org/10.1128/spectrum.03838-23, doi:10.1128/spectrum.03838-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (sweet2024tolradamodel media e020062b): Philip Sweet, Matthew R. Burroughs, Sungyeon Jang, and Lydia M. Contreras. Tolrad, a model for predicting radiation tolerance using pfam annotations, identifies novel radiosensitive bacterial species from reference genomes and mags. Oct 2024. URL: https://doi.org/10.1128/spectrum.03838-23, doi:10.1128/spectrum.03838-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (lourenco2023environmentalradiobiology pages 11-13): Joana Lourenço, Carmel Mothersill, Carmen Arena, Deborah Oughton, Margot Vanheukelom, Ruth Pereira, Sónia Mendo, and Veronica De Micco. Environmental radiobiology. Radiobiology Textbook, pages 469-501, Jan 2023. URL: https://doi.org/10.1007/978-3-031-18810-7\_9, doi:10.1007/978-3-031-18810-7\_9. This article has 16 citations.

5. (rai2024anovelionizing pages 1-3): Shiv Narayan Rai and Tanmay Dutta. A novel ionizing radiation-induced small rna, drss, promotes the detoxification of reactive oxygen species in <i>deinococcus radiodurans</i>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.01538-23, doi:10.1128/aem.01538-23. This article has 9 citations and is from a peer-reviewed journal.

6. (sharma2024naturaltransformationspecificdpra pages 10-12): Dhirendra Kumar Sharma, Ishu Soni, Hari S. Misra, and Yogendra Singh Rajpurohit. Natural transformation-specific dpra coordinate dna double-strand break repair pathways in heavily irradiated <i>d. radiodurans</i>. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01948-23, doi:10.1128/aem.01948-23. This article has 6 citations and is from a peer-reviewed journal.

7. (sharma2024naturaltransformationspecificdpra pages 12-14): Dhirendra Kumar Sharma, Ishu Soni, Hari S. Misra, and Yogendra Singh Rajpurohit. Natural transformation-specific dpra coordinate dna double-strand break repair pathways in heavily irradiated <i>d. radiodurans</i>. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01948-23, doi:10.1128/aem.01948-23. This article has 6 citations and is from a peer-reviewed journal.

8. (pal2024unravelingradiationresistance pages 1-2): Sowptika Pal, Ramani Yuvaraj, Hari Krishnan, Balasubramanian Venkatraman, Jayanthi Abraham, and Anilkumar Gopinathan. Unraveling radiation resistance strategies in two bacterial strains from the high background radiation area of chavara-neendakara: a comprehensive whole genome analysis. PLOS ONE, 19:e0304810, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0304810, doi:10.1371/journal.pone.0304810. This article has 8 citations and is from a peer-reviewed journal.

9. (subramani2023involvementofnucleotide pages 1-2): Gayathri Subramani and Sathiyaraj Srinivasan. Involvement of nucleotide excision repair and rec-dependent pathway genes for uv radiation resistance in deinococcus irradiatisoli 17bor-2. Genes, 14:1803, Sep 2023. URL: https://doi.org/10.3390/genes14091803, doi:10.3390/genes14091803. This article has 6 citations.

10. (subramani2023involvementofnucleotide pages 5-7): Gayathri Subramani and Sathiyaraj Srinivasan. Involvement of nucleotide excision repair and rec-dependent pathway genes for uv radiation resistance in deinococcus irradiatisoli 17bor-2. Genes, 14:1803, Sep 2023. URL: https://doi.org/10.3390/genes14091803, doi:10.3390/genes14091803. This article has 6 citations.

11. (tan2025radiationresistantbacteriapotential pages 5-8): Zheng Tan, Delin Yin, Jiangchuan Min, Yushuai Liu, Daoyang Zhang, Jiahong He, Yanke Bi, and Kena Qin. Radiation-resistant bacteria: potential player in sustainable wastewater treatment. Sustainability, 17:7864, Sep 2025. URL: https://doi.org/10.3390/su17177864, doi:10.3390/su17177864. This article has 3 citations.

12. (rai2024anovelionizing pages 13-14): Shiv Narayan Rai and Tanmay Dutta. A novel ionizing radiation-induced small rna, drss, promotes the detoxification of reactive oxygen species in <i>deinococcus radiodurans</i>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.01538-23, doi:10.1128/aem.01538-23. This article has 9 citations and is from a peer-reviewed journal.

13. (pal2024unravelingradiationresistance pages 32-34): Sowptika Pal, Ramani Yuvaraj, Hari Krishnan, Balasubramanian Venkatraman, Jayanthi Abraham, and Anilkumar Gopinathan. Unraveling radiation resistance strategies in two bacterial strains from the high background radiation area of chavara-neendakara: a comprehensive whole genome analysis. PLOS ONE, 19:e0304810, Jun 2024. URL: https://doi.org/10.1371/journal.pone.0304810, doi:10.1371/journal.pone.0304810. This article has 8 citations and is from a peer-reviewed journal.

14. (subramani2023involvementofnucleotide pages 7-9): Gayathri Subramani and Sathiyaraj Srinivasan. Involvement of nucleotide excision repair and rec-dependent pathway genes for uv radiation resistance in deinococcus irradiatisoli 17bor-2. Genes, 14:1803, Sep 2023. URL: https://doi.org/10.3390/genes14091803, doi:10.3390/genes14091803. This article has 6 citations.

15. (abbaszadeh2024theecologyand pages 24-28): J Abbaszadeh. The ecology and evolutionary history of the deinococcaceae family. Unknown journal, 2024.

16. (tan2025radiationresistantbacteriapotential pages 4-5): Zheng Tan, Delin Yin, Jiangchuan Min, Yushuai Liu, Daoyang Zhang, Jiahong He, Yanke Bi, and Kena Qin. Radiation-resistant bacteria: potential player in sustainable wastewater treatment. Sustainability, 17:7864, Sep 2025. URL: https://doi.org/10.3390/su17177864, doi:10.3390/su17177864. This article has 3 citations.

17. (abbaszadeh2024theecologyanda pages 24-28): J Abbaszadeh. The ecology and evolutionary history of the deinococcaceae family. Unknown journal, 2024.