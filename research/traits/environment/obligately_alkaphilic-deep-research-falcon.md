---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:45:02.833976'
end_time: '2026-06-17T23:56:08.350874'
duration_seconds: 665.52
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately alkaphilic
  trait_identifier: METPO:1003004
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_alkaphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism requires alkaline conditions
    (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
  parent_traits: METPO:1003000
  synonyms: obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
  evidence_summary: 'DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9
    and above (Supports the obligate alkaliphile definition.)'
  causal_graph_summary: 'obligately_alkaphilic_sodium_cycle_homeostasis: 7 nodes,
    6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately alkaphilic
- **METPO identifier:** METPO:1003004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism requires alkaline conditions (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9 and above (Supports the obligate alkaliphile definition.)
- **Existing causal graph summary:** obligately_alkaphilic_sodium_cycle_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_alkaphilic.yaml`.

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
- **Trait label:** obligately alkaphilic
- **METPO identifier:** METPO:1003004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism requires alkaline conditions (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9 and above (Supports the obligate alkaliphile definition.)
- **Existing causal graph summary:** obligately_alkaphilic_sodium_cycle_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_alkaphilic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **obligately alkaphilic** (METPO:1003004)

### Executive scope summary
**Obligately alkaphilic (obligate alkaliphile)** denotes a microbial pH-growth preference in which growth requires alkaline conditions and does not occur (or is negligible) under near-neutral or acidic pH. Recent primary literature demonstrates that authors operationalize “obligate alkaliphile” using **experimentally measured growth pH ranges** and explicitly contrast this with “alkalitolerant” organisms that can still grow closer to neutral pH. For example, an alkaliphilic aceticlastic methanogen enriched from a soda lake (“strain Mx”) is described as an **“obligate alkaliphile”** with growth in the pH range **7.7–10.2** (optimum 9.3–9.5), while a related mud-volcano strain is described as **alkalitolerant** with growth **7.5–10.0** (optimum 9.0). (khomyakova2023phenotypicandgenomic pages 1-2)

**Boundary warning:** the “obligate alkaliphile” minimum pH reported (7.7) is **below** the template’s heuristic “typically pH above 8.5”; therefore, curations should preserve the **assay context** (medium/buffer system, salinity, incubation regime, measured final pH) and may require species-specific interpretation rather than applying a rigid pH threshold. (khomyakova2023phenotypicandgenomic pages 2-3, khomyakova2023phenotypicandgenomic pages 1-2)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Phenotype represented by METPO:1003004
The trait is best treated as an **assay-observed growth phenotype**: the organism’s ability to reproduce under alkaline pH and **failure to grow** at neutral/acidic pH under the tested conditions. In practice, papers report:
- pH range for growth and pH optimum (khomyakova2023phenotypicandgenomic pages 1-2)
- buffer systems used to define pH range and warnings that **final pH can deviate** from initial pH, particularly at extremes (khomyakova2023phenotypicandgenomic pages 2-3)

### 1.2 Distinguishing nearby traits
- **Obligately alkaliphilic**: requires alkaline conditions; no meaningful growth at neutral pH.
- **Alkalitolerant / facultative alkaliphile**: can grow in alkaline conditions but retains growth nearer neutral pH.

A primary example of this distinction is explicitly given for two related aceticlastic methanogens: alkalitolerant strain M04Ac (pH 7.5–10.0) versus obligate alkaliphile strain Mx (pH 7.7–10.2). (khomyakova2023phenotypicandgenomic pages 1-2)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Ion homeostasis and the “sodium cycle” at high pH
A 2024 multi-omics study in *Natranaerobius thermophilus* emphasizes monovalent cation/proton antiporters as **essential for growth** of halophilic/alkaliphilic bacteria under stress conditions by regulating **H+ influx** and **Na+ efflux**, and reports **upregulation** of three NhaC Na+/H+ antiporters under different salinities. (xing2024thepolyextremophilenatranaerobius pages 19-21)

The same study links K+ uptake and membrane potential to pH homeostasis via the **TrkAH** system: “responsible for the uptake of K+ … and maintaining pH homeostasis” and “involved in the adjustment of membrane potential.” (xing2024thepolyextremophilenatranaerobius pages 19-21)

### 2.2 Cell envelope and proton capture at alkaline pH
A 2023 review of methanotroph pH ecophysiology summarizes a widely cited mechanism: at high pH, alkaliphilic microbes develop **secondary cell wall polymers (SCWPs)** such as **S-layer protein** to enhance net negative surface charge, increasing attraction to external protons. (yao2023howmethanotrophsrespond pages 5-7)

The same review includes a schematic summarizing this concept (Figure 2), which can be used as a high-level mechanistic model while treating organism-specific instantiation as curation-dependent. (yao2023howmethanotrophsrespond media 29407bd1)

### 2.3 Membrane lipid remodeling under alkaline pH
The 2023 review reports an alkaliphilic methanotroph example in which cells increased phosphatidylglycerol (PG), phosphatidylcholine (PC), and cardiolipin (CL), and decreased phosphatidylethanolamine (PE), phosphatidylserine (PS), and phosphatidic acid (PA) “in response to high pH.” (yao2023howmethanotrophsrespond pages 5-7)

### 2.4 Metabolic constraints unique to alkaline conditions: acetate chemistry
A 2023 primary paper on alkaliphilic aceticlastic methanogens highlights a specific alkaline constraint: “High pH favors the dissociation of acetic acid to its anion (CH3COO−), preventing transmembrane diffusion,” making acetate uptake dependent on a transporter and rendering aceticlastic methanogenesis “energetically less favorable” under alkaline conditions. (khomyakova2023phenotypicandgenomic pages 1-2)

### 2.5 Compatible solutes and osmoprotection linked to haloalkaliphily
In 2023, Khomyakova et al. report that genomes of the alkaliphilic aceticlastic methanogens encoded (halo)alkaline adaptation mechanisms including **ectoine biosynthesis**, described as “the first evidence for the formation of this osmoprotectant in archaea.” (khomyakova2023phenotypicandgenomic pages 1-2)

### 2.6 Quantitative data reported in 2024
Xing et al. report quantitative intracellular ion and proteome statistics under haloalkaline growth conditions, including:
- intracellular K+ increasing with salinity to **~440.2 mM at 4.3 M Na+** (and 227.2 mM at 2.5 M Na+) (xing2024thepolyextremophilenatranaerobius pages 19-21)
- majority of identified proteins acidic (**69.8%**) and calculated proteome pI statistics (median/average pI values reported) (xing2024thepolyextremophilenatranaerobius pages 19-21)
These provide curation-ready numeric attributes for nodes such as “intracellular K+ concentration” and “acidic proteome bias,” with clear uncertainty about generality beyond the studied organism.

---

## 3) Current applications and real-world implementations

### 3.1 Environmental microbiology / ecosystem functioning in alkaline systems
The trait is directly relevant to organismal persistence in natural hyperalkaline habitats (e.g., soda lakes, serpentinization-associated environments), where high pH constrains energy generation and transport. Experimental cultivation protocols for alkaliphilic methanogens explicitly use sodium carbonate/bicarbonate buffers at alkaline pH and manipulate Na+ concentrations, reflecting how field ecology and laboratory assay design co-determine the phenotype. (khomyakova2023phenotypicandgenomic pages 2-3)

### 3.2 Bioprocessing relevance (operational)
Although detailed industrial case studies were not extracted in the present evidence set, the mechanisms captured here (cation/proton antiporters; compatible solutes; membrane/cell-envelope remodeling) are precisely the modules commonly targeted when engineering or selecting strains for high-pH processes (e.g., alkaline waste or alkaline bioreactors). This statement should be treated as **contextual**, not a direct claim of deployment for the specific taxa referenced.

---

## 4) Expert opinions and authoritative synthesis

### 4.1 Authoritative review perspective (2023)
Yao et al. summarize a mechanistic view in which alkaliphiles must overcome **proton limitation** at high pH, including cell-surface strategies (S-layer/SCWPs) to attract protons and membrane/respiratory-chain coupling mechanisms (including “incompletely elucidated mechanisms for sequestered proton transfer”). (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media 29407bd1)

### 4.2 Primary-study perspective (2024)
Xing et al. explicitly characterize monovalent cation/proton antiporters (CPA/Mrp and Nha families) as “essential for the growth of various halophilic and alkaliphilic bacteria under stress conditions,” and frame Na+/H+ antiporters as central to reducing cytoplasmic Na+ and maintaining homeostasis. (xing2024thepolyextremophilenatranaerobius pages 19-21)

---

## 5) Candidate nodes for TraitMech causal graph (grouped by type)

### 5.1 Environmental / experimental factor nodes
- External pH (alkaline pH)
- Na-carbonate brine / sodium carbonate–bicarbonate buffer (alkaline medium design) (khomyakova2023phenotypicandgenomic pages 2-3)
- Salinity / total Na+ concentration (0–2 M tested in one study’s salinity profile; optimal 0.2–0.3 M total Na+ for obligate alkaliphile strain Mx) (khomyakova2023phenotypicandgenomic pages 2-3, khomyakova2023phenotypicandgenomic pages 1-2)

### 5.2 Phenotype/assay nodes
- Growth pH range
- “Obligate alkaliphile” vs “alkalitolerant” category label (khomyakova2023phenotypicandgenomic pages 1-2)

### 5.3 Genes/proteins/complexes (mechanistic) 
- Na+/H+ antiporters: **NhaC family**; broader **Nha families** and **CPA/Mrp-type** antiporters (xing2024thepolyextremophilenatranaerobius pages 19-21)
- **TrkAH** potassium uptake system (TrkH + TrkA) (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Na+/solute symporters (SSS family; e.g., Na+/proline; Na+/dicarboxylate SdcS) (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Cell surface: **S-layer proteins** / secondary cell wall polymers (SCWPs) (yao2023howmethanotrophsrespond pages 5-7)

### 5.4 Chemicals/metabolites/ions (with suggested groundings)
- Proton: CHEBI:15378 (yao2023howmethanotrophsrespond pages 5-7)
- Sodium ion: CHEBI:29101 (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Potassium ion: CHEBI:29103 (reported as intracellular K+; grounding suggested) (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Acetate: CHEBI:30089 (khomyakova2023phenotypicandgenomic pages 1-2)
- Ectoine: CHEBI:53515 (khomyakova2023phenotypicandgenomic pages 1-2)
- Glycine betaine: CHEBI:17750 (suggested) (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Proline: CHEBI:17203 (suggested) (xing2024thepolyextremophilenatranaerobius pages 19-21)
- Phospholipids: PG CHEBI:17517; PC CHEBI:64482; CL CHEBI:28494; PE CHEBI:16038; PS CHEBI:18303; PA CHEBI:16337 (yao2023howmethanotrophsrespond pages 5-7)

---

## 6) Evidence-backed candidate causal edges (curation table)
The following table is formatted for direct curation review and includes verbatim snippets, DOIs, and uncertainty notes.

| Subject (node) | Predicate | Object (node) | Proposed grounding (subject/object CURIEs when available or label-only) | Evidence snippet (verbatim) | Source (DOI, year, URL) | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| Na+/H+ antiporter NhaC | decreases | intracellular Na+ concentration | subject: label-only (NhaC family); object: CHEBI:29101 sodium(1+) | “The Na+/H+ antiporters effectively decrease the intracellular Na+ concentration and may play an important role in the salt acclimation of N. thermophilus.” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong mechanistic statement; taxon-specific to *Natranaerobius thermophilus* but broadly relevant to haloalkaliphily. |
| high salinity / alkaline stress | upregulates | NhaC Na+/H+ antiporters | subject: label-only high salinity/alkaline stress; object: label-only (NhaC family) | “Monovalent cation/proton antiporters play a key role in regulating the influx of H+ and the efflux of Na+, which are essential for the growth of various halophilic and alkaliphilic bacteria under stress conditions… In N. thermophilus, three Na+/H+ antiporters NhaC were found to be upregulated at different salinities.” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Good support for stress-responsive antiporter expression; direct growth causality is inferred from same passage. |
| monovalent cation/proton antiporters (CPA/Mrp and Nha families) | are essential for | growth of halophilic and alkaliphilic bacteria under stress conditions | subject: label-only; object: METPO:1003004 obligately alkaphilic / label-only “growth under saline/alkaline stress” | “Monovalent cation/proton antiporters play a key role in regulating the influx of H+ and the efflux of Na+, which are essential for the growth of various halophilic and alkaliphilic bacteria under stress conditions.” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Broad statement supports antiporter module as candidate core mechanism; not restricted to obligate alkaliphiles. |
| TrkAH transport system | contributes to | pH homeostasis | subject: label-only (TrkAH K+ uptake system); object: GO:0006885 regulation of pH? / label-only “pH homeostasis” | “The TrkAH transport system is responsible for the uptake of K+ in response to osmotic shock and maintaining pH homeostasis.” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong direct support for K+ uptake node to pH-homeostasis edge. |
| TrkAH transport system | contributes to | membrane potential adjustment | subject: label-only (TrkAH K+ uptake system); object: GO:0006811 ion transport / label-only “membrane potential adjustment” | “Additionally, this system is involved in the adjustment of membrane potential.” (xing2024thepolyextremophilenatranaerobius pages 19-21) | 10.1128/AEM.00145-24, 2024, https://doi.org/10.1128/AEM.00145-24 | Strong but taxon-contextual. Useful for sodium-cycle/homeostasis subgraph. |
| secondary cell wall polymers / S-layer protein | increase | net negative charges on cellular surfaces | subject: label-only SCWPs/S-layer; object: label-only net negative surface charge | “the second cell wall polymers (SCWPs), such as S-layer protein, are developed by alkaliphilic microbes. These components enhance net negative charges on cellular surfaces” (yao2023howmethanotrophsrespond pages 5-7) | 10.3389/fmicb.2022.1034164, 2023, https://doi.org/10.3389/fmicb.2022.1034164 | Review source; strong conceptual support, but not exclusive to obligate alkaliphiles. |
| net negative surface charge | increases attraction to | external protons | subject: label-only net negative surface charge; object: CHEBI:15378 hydron | “These components enhance net negative charges on cellular surfaces that increase attraction to external protons” (yao2023howmethanotrophsrespond pages 5-7) | 10.3389/fmicb.2022.1034164, 2023, https://doi.org/10.3389/fmicb.2022.1034164 | Supports proton-capture mechanism at high pH; review-based and should be curated with note. |
| high external pH | increases abundance of | phosphatidylglycerol / phosphatidylcholine / cardiolipin | subject: label-only high external pH; object: CHEBI:17517 phosphatidylglycerol / CHEBI:64482 phosphatidylcholine / CHEBI:28494 cardiolipin | “It increased the relative abundance of phosphatidylglycerol (PG), phosphatidylcholine (PC), and cardiolipin (CL) in response to high pH” (yao2023howmethanotrophsrespond pages 5-7) | 10.3389/fmicb.2022.1034164, 2023, https://doi.org/10.3389/fmicb.2022.1034164 | Good edge for membrane remodeling under alkaline conditions; organism-specific example in review. |
| high external pH | decreases abundance of | phosphatidylethanolamine / phosphatidylserine / phosphatidic acid | subject: label-only high external pH; object: CHEBI:16038 phosphatidylethanolamine / CHEBI:18303 phosphatidylserine / CHEBI:16337 phosphatidic acid | “and decreased the relative abundance of phosphatidylethanolamine (PE), phosphatidylserine (PS), and phosphatidic acid (PA)” (yao2023howmethanotrophsrespond pages 5-7) | 10.3389/fmicb.2022.1034164, 2023, https://doi.org/10.3389/fmicb.2022.1034164 | Complements prior membrane-remodeling edge; likely species-specific and adaptive rather than universal. |
| adapted a subunit of thermoalkaliphilic F1Fo-ATP synthase | enables | ATP synthesis at high pH but not at neutral pH values | subject: label-only adapted ATP synthase a subunit; object: label-only ATP synthesis at high pH | “A specific adaptation in the a subunit of thermoalkaliphilic F1Fo-ATP synthase enables ATP synthesis at high pH but not at neutral pH values.” (jong2023membraneproteomeof pages 9-10) | 10.1074/jbc.M611709200, 2007, cited in 10.3389/fmicb.2023.1228266 (2023), https://doi.org/10.3389/fmicb.2023.1228266 | Evidence is indirect via cited reference in bibliography context, not full primary text excerpt; useful but should be marked secondary/needs direct paper check before hard curation. |
| alkaline conditions (>pH 9.0) | cause | dissociation of acetic acid to acetate anion | subject: label-only alkaline conditions; object: CHEBI:30089 acetate | “High pH favors the dissociation of acetic acid to its anion (CH3COO−), preventing transmembrane diffusion” (khomyakova2023phenotypicandgenomic pages 1-2) | 10.3389/fmicb.2023.1233691, 2023, https://doi.org/10.3389/fmicb.2023.1233691 | Strong direct mechanistic chemistry constraint relevant to alkaliphilic aceticlastic methanogens. |
| acetate anion at high pH | prevents | transmembrane diffusion of acetate | subject: CHEBI:30089 acetate; object: label-only transmembrane diffusion of acetate | “High pH favors the dissociation of acetic acid to its anion (CH3COO−), preventing transmembrane diffusion” (khomyakova2023phenotypicandgenomic pages 1-2) | 10.3389/fmicb.2023.1233691, 2023, https://doi.org/10.3389/fmicb.2023.1233691 | Strong direct support. |
| alkaline conditions | make dependent on | acetate transporter for acetate uptake | subject: label-only alkaline conditions; object: label-only acetate transporter-dependent uptake | “Thus, under alkaline conditions, the transport of acetate into the cell depends on the acetate transporter, and aceticlastic methanogenesis is likely to be energetically less favorable” (khomyakova2023phenotypicandgenomic pages 1-2) | 10.3389/fmicb.2023.1233691, 2023, https://doi.org/10.3389/fmicb.2023.1233691 | Strong mechanistic edge; transporter identity not specified in excerpt. |
| ectoine biosynthesis | provides | osmoprotectant function in alkaliphilic methanogens | subject: label-only ectoine biosynthesis; object: CHEBI:53515 ectoine / label-only osmoprotection | “different mechanisms of (halo)alkaline adaptations, including ectoine biosynthesis, which is the first evidence for the formation of this osmoprotectant in archaea.” (khomyakova2023phenotypicandgenomic pages 1-2) | 10.3389/fmicb.2023.1233691, 2023, https://doi.org/10.3389/fmicb.2023.1233691 | Strong support for compatible-solute node; taxon-specific to newly described methanogens. |
| growth in pH range 7.7–10.2 with optimum 9.3–9.5 | defines | obligate alkaliphile phenotype | subject: label-only experimental growth range; object: METPO:1003004 obligately alkaphilic | “the soda lake strain Mx was an obligate alkaliphile growing in the pH range 7.7–10.2 (optimum 9.3–9.5)” (khomyakova2023phenotypicandgenomic pages 1-2) | 10.3389/fmicb.2023.1233691, 2023, https://doi.org/10.3389/fmicb.2023.1233691 | Important boundary case: minimum pH 7.7 is slightly below 8.5 heuristic in trait definition, but authors explicitly classify it as obligate alkaliphile. |
| growth in pH range 7.5–10.0 with optimum 9.0 | defines | alkalitolerant phenotype | subject: label-only experimental growth range; object: label-only alkalitolerant | “The mud volcano strain M04Ac was alkalitolerant, with the pH range for growth from 7.5 to 10.0 (optimum at 9.0)” (khomyakova2023phenotypicandgenomic pages 1-2) | 10.3389/fmicb.2023.1233691, 2023, https://doi.org/10.3389/fmicb.2023.1233691 | Useful contrast edge for scope delimitation; supports distinction from obligate alkaliphily. |


*Table: This table compiles evidence-backed candidate subject–predicate–object edges for curating the obligately alkaliphilic trait. It focuses on mechanistic nodes and explicit phenotype-defining observations from the allowed context IDs.*

---

## 7) Visual evidence (figures/tables useful for curation)
- **Figure 2** (schematic) in Yao et al. summarizes pH homeostasis mechanisms for alkaliphilic methanotrophs, including a depiction of S-layer development for proton attraction and respiratory-chain/ATP synthase coupling hypotheses. (yao2023howmethanotrophsrespond media 29407bd1)
- **Table entries** in Yao et al. provide pH optima and ranges for alkaliphilic methanotroph taxa such as *Methylomicrobium buryatense* and *Methylomicrobium kenyense*. (yao2023howmethanotrophsrespond media 29407bd1)

---

## 8) Warnings and “do not curate yet” items
1. **ATP synthase adaptation edge needs primary-text confirmation.** Evidence for “a specific adaptation in the a subunit … enables ATP synthesis at high pH but not at neutral pH values” appears here as a cited statement within another paper’s reference list context rather than extracted from the original JBC article text. Before curating as a strong mechanistic edge, retrieve and quote the primary JBC source directly. (jong2023membraneproteomeof pages 9-10)
2. **Review-derived generalizations (S-layer, lipid remodeling) are high-level and may be taxon-specific.** The S-layer/SCWP and lipid composition changes are presented in a review; each should be curated either as (i) general hypothesis edges with uncertainty or (ii) taxa-scoped edges with primary evidence for the target organism. (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media 29407bd1)
3. **Trait boundary conditions must preserve assay context.** The obligate alkaliphile example includes minimum growth pH 7.7, below the template’s “typically pH above 8.5.” Curations should therefore avoid enforcing an absolute numeric threshold without recording the specific experimental growth assay and medium composition. (khomyakova2023phenotypicandgenomic pages 2-3, khomyakova2023phenotypicandgenomic pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. **Xing Q, et al.** (May 2024). *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology** 90(5). DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 19-21)

2. **Khomyakova MA, et al.** (Published 11 Oct 2023). *Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus Methanocrinis gen.nov. within the family Methanotrichaceae.* **Frontiers in Microbiology** 14:1233691. DOI: **10.3389/fmicb.2023.1233691**. URL: https://doi.org/10.3389/fmicb.2023.1233691 (khomyakova2023phenotypicandgenomic pages 1-2, khomyakova2023phenotypicandgenomic pages 2-3)

3. **Yao X, Wang J, Hu B.** (Jan 2023). *How methanotrophs respond to pH: A review of ecophysiology.* **Frontiers in Microbiology** 13. DOI: **10.3389/fmicb.2022.1034164**. URL: https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media 29407bd1)

4. **de Jong SI, et al.** (Jul 2023). *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1.* **Frontiers in Microbiology** 14:1228266. DOI: **10.3389/fmicb.2023.1228266**. URL: https://doi.org/10.3389/fmicb.2023.1228266 (jong2023membraneproteomeof pages 8-9, jong2023membraneproteomeof pages 9-10)

---

## Suggested next-step retrieval targets (for strengthening curatable edges)
- Primary paper for ATP synthase a-subunit adaptation (J. Biol. Chem. 2007; DOI **10.1074/jbc.M611709200**) to obtain a direct quote and the specific residue/mutation and phenotype context before curating. (jong2023membraneproteomeof pages 9-10)
- Primary evidence papers (not review) for SCWP/S-layer proton attraction and lipid remodeling in a model obligate alkaliphile relevant to METPO:1003004.


References

1. (khomyakova2023phenotypicandgenomic pages 1-2): Maria A. Khomyakova, Alexander Y. Merkel, Alexander I. Slobodkin, and Dimitry Y. Sorokin. Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus methanocrinis gen.nov. within the family methanotrichaceae. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1233691, doi:10.3389/fmicb.2023.1233691. This article has 13 citations and is from a peer-reviewed journal.

2. (khomyakova2023phenotypicandgenomic pages 2-3): Maria A. Khomyakova, Alexander Y. Merkel, Alexander I. Slobodkin, and Dimitry Y. Sorokin. Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus methanocrinis gen.nov. within the family methanotrichaceae. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1233691, doi:10.3389/fmicb.2023.1233691. This article has 13 citations and is from a peer-reviewed journal.

3. (xing2024thepolyextremophilenatranaerobius pages 19-21): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

4. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

5. (yao2023howmethanotrophsrespond media 29407bd1): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

6. (jong2023membraneproteomeof pages 9-10): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.

7. (jong2023membraneproteomeof pages 8-9): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.