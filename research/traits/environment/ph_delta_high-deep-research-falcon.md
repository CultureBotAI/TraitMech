---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:01:31.339119'
end_time: '2026-06-18T00:16:13.794841'
duration_seconds: 882.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta high
  trait_identifier: METPO:1000478
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 5\u20139 pH units, characteristic of euryphilic pH-tolerance physiology."
  parent_traits: METPO:1000232
  synonyms: pHd_5_9
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports very broad pH-homeostasis as a hallmark of generalist pH-tolerance physiology.)
    | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports
    robust proton extrusion and import machinery as the basis of very broad pH-tolerance.)'
  causal_graph_summary: 'ph_delta_high_euryphilic_breadth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta high
- **METPO identifier:** METPO:1000478
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 5–9 pH units, characteristic of euryphilic pH-tolerance physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_5_9
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very broad pH-homeostasis as a hallmark of generalist pH-tolerance physiology.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust proton extrusion and import machinery as the basis of very broad pH-tolerance.)
- **Existing causal graph summary:** ph_delta_high_euryphilic_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_high.yaml`.

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
- **Trait label:** pH delta high
- **METPO identifier:** METPO:1000478
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 5–9 pH units, characteristic of euryphilic pH-tolerance physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_5_9
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very broad pH-homeostasis as a hallmark of generalist pH-tolerance physiology.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports robust proton extrusion and import machinery as the basis of very broad pH-tolerance.)
- **Existing causal graph summary:** ph_delta_high_euryphilic_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_high.yaml`.

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


## Microbial Trait Causal Graph Report: **pH delta high** (METPO:1000478)

### Scope summary (TraitMech curation focus)
**Trait label:** pH delta high (syn. *pHd_5_9*) is best interpreted as an **assay-observed, growth-supporting external pH breadth** spanning roughly **pH 5–9**, corresponding closely to the classic neutralophile growth range of **~pHout 5.5–9.0**. (krulwich2011molecularaspectsof pages 1-3)

This trait is **not** a synonym for (i) acidophily (typical growth at pH 1–3) or (ii) alkaliphily (pH 10–13), which are specialist strategies often involving constitutive, energetically costly adaptations. (krulwich2011molecularaspectsof pages 3-5)

A key boundary case is **survival without growth** at more extreme pH values (e.g., transient gastric passage). The canonical operational distinction is: **survival** is assessed by the ability to **resume growth after return to a permissive pH**, whereas the pH-breadth trait concerns **growth across the pH gradient itself**. (krulwich2011molecularaspectsof pages 1-3)

Mechanistically, pH-delta-high aligns with the capacity for **cytoplasmic pH homeostasis**: neutralophiles can grow across a broad pHout range while keeping **pHin much narrower (~7.5–7.7)**. (krulwich2011molecularaspectsof pages 1-3)

### Key concepts and definitions (current understanding)
1. **Cytoplasmic pH homeostasis:** Many cells maintain an internal pH near neutrality (often **7.0–7.5**). (poolman2023physicochemicalhomeostasisin pages 1-2)
2. **Neutralophile growth range:** Neutralophiles can grow at **external pH ~5.5–9.0** while holding **pHin ~7.5–7.7**; at the acidic end pHin is maintained more alkaline than pHout, and at alkaline pHout the cytoplasm becomes more acidic than outside. (krulwich2011molecularaspectsof pages 1-3)
3. **Proton motive force (PMF) and its components:** PMF reflects a combination of **Δψ (membrane potential)** and **ΔpH**; their relative contributions shift across external pH conditions. Poolman summarizes that the **PMF of neutralophiles is kept relatively constant in the pH range ~5–8**, suggesting system-level robustness that supports broad growth. (poolman2023physicochemicalhomeostasisin pages 1-2)
4. **Why buffering matters at cellular scale:** In a ~1 fL bacterial cytoplasm, there are extremely few free protons at neutral pH (e.g., at pH ~7.2, on the order of **~10 free protons**), so buffering species (e.g., phosphates) are crucial to blunt pH swings. (poolman2023physicochemicalhomeostasisin pages 1-2)

### Recent developments and latest research (prioritize 2023–2024)

#### 1) 2023—Physicochemical homeostasis synthesis (Poolman 2023)
Poolman’s 2023 review provides an updated, integrative description of bacterial physicochemical homeostasis and explicitly names pH-homeostasis “key regulators”: **Na+/H+ and K+/H+ antiporters**, **proton-pumping enzymes** (respiratory components) and **F0F1-ATPase** (highlighted in lactic acid bacteria), plus **metabolite decarboxylation pathways**. (poolman2023physicochemicalhomeostasisin pages 1-2)

It also states the internal pH setpoint and system-level energetic robustness: internal pH **7.0–7.5** and relatively constant PMF for neutralophiles over **pH ~5–8**. (poolman2023physicochemicalhomeostasisin pages 1-2)

A mechanistic summary figure was extracted (Figure 2), suitable as a high-level evidence anchor for curating “mechanism classes” in TraitMech. (poolman2023physicochemicalhomeostasisin media cb4ea770)

#### 2) 2023—Genome-based prediction of pH preference (Ramoneda et al. 2023)
Ramoneda et al. compiled **5 datasets** spanning soil and freshwater pH gradients (**1470 total samples; pH 3–10**) and inferred pH preferences for taxa, then associated **gene presence/absence** with inferred pH preference and trained ML models. (ramoneda2023buildingagenomebased pages 1-2)

Key quantitative results (useful statistics):
- Dataset scale: **250,275 ASVs** initially; **4,568 ASVs** in genomic analysis spanning **38 bacterial phyla**. (ramoneda2023buildingagenomebased pages 1-2)
- Community structuring by pH: Mantel correlations **ρ = 0.37–0.78** across datasets. (ramoneda2023buildingagenomebased pages 1-2)
- Consistent gene associations: **332 gene types** significantly associated in ≥2 datasets; **56 gene types** in ≥3 datasets; no single gene was significant in all datasets. (ramoneda2023buildingagenomebased pages 3-5)
- ML performance: average **R² ≈ 0.80** across datasets; training **MAE = 0.43**, validation **MAE = 0.63**; independent validation **R² = 0.55**; an external UK soil validation gave **R² = 0.21, MAE = 0.93**. (ramoneda2023buildingagenomebased pages 6-7)
- The predictive window was effectively limited to **~pH 4–9** due to data gaps, which notably overlaps the “pH delta high” concept window. (ramoneda2023buildingagenomebased pages 6-7)

Mechanistically, the authors relate gene associations to four main acid-stress strategies: **proton-consuming reactions (decarboxylases)**, **production of basic compounds (urease → ammonia)**, **active proton efflux and ion transport (Kdp K+ transporters; Na+/H+ antiporters such as Mrp/Mnh-related families)**, and **membrane permeability/protein maturation/folding-related functions**. (ramoneda2023buildingagenomebased pages 3-5)

Interpretation caution: this study predicts **realized niche pH** (distribution-derived), not necessarily in vitro growth optima; absence of a gene can be as informative as presence, and associations may be habitat-specific. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5)

#### 3) 2024—Applications-driven acid stress review (Atasoy et al. 2024)
Atasoy et al. (2024) frames low-pH microbial physiology as enabling applied “planetary health” outcomes, with explicit mentions of acid tolerance response components (e.g., **proton-translocating F1FO-ATPase**, **membrane fatty-acid modifications**, **amino-acid decarboxylase systems**, and **stress-protein production**). (atasoy2024exploitationofmicrobial pages 3-4)

### Current applications and real-world implementations
Atasoy et al. provides numerous application domains tied to low-pH physiology and tolerance engineering:
- **Food preservation and fermentation**: acidic fermentation improves safety/shelf life/texture/flavor across dairy, meats, vegetables; organic acids and their **pKa** are emphasized in antimicrobial efficacy. (atasoy2024exploitationofmicrobial pages 2-3, atasoy2024exploitationofmicrobial pages 4-5)
- **Bioprocessing & circular economy**: microbial production of organic acids (e.g., lactic, succinic, itaconic) as platform chemicals; development of **acid-tolerant strains** as cell factories; process strategies such as adaptive evolution are discussed. (atasoy2024exploitationofmicrobial pages 2-3, atasoy2024exploitationofmicrobial pages 3-4)
- **Decontamination technologies**: plasma-activated water (PAW) that is rapidly acidified (≈pH 3) for food and surface decontamination; microbial responses resemble acid-pH responses. (atasoy2024exploitationofmicrobial pages 2-3, atasoy2024exploitationofmicrobial pages 3-4)
- **Environmental bioremediation**: mentions include acid mine drainage bioremediation using acidophilic microbes (not directly “pH delta high,” but relevant to pH-stress engineering and selection). (atasoy2024exploitationofmicrobial pages 26-27)

### Expert opinions and analysis (authoritative sources)
- **System-level view (Poolman 2023):** pH tolerance breadth is framed as an emergent property of linked homeostasis systems—antiporters, proton pumps/ATPases, decarboxylation pathways, and buffering—operating to keep internal pH near neutral and PMF usable across external pH variation. (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Mechanistic grounding (Krulwich et al. 2011):** pH homeostasis relies on modulating PMF components, deploying primary proton pumps and secondary cation/proton antiporters, and recruiting proton-consuming metabolic routes (e.g., amino-acid decarboxylation). The review also stresses that extremophiles may constitutively express these systems at energetic cost. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 5-6)
- **Comparative-genomics perspective (Ramoneda 2023):** taxonomy/phylogeny are poor predictors of pH preference; instead, gene content provides predictive signal, highlighting practical value for cultivation strategy design and inoculant selection—while cautioning that predictions reflect realized niches and are constrained by available data ranges. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)

### Relevant statistics and data points for curation
- Neutralophile external growth range: **~pHout 5.5–9.0** with **pHin ~7.5–7.7**. (krulwich2011molecularaspectsof pages 1-3)
- Internal pH typical setpoint in many cell types: **7.0–7.5**. (poolman2023physicochemicalhomeostasisin pages 1-2)
- Neutralophile PMF stability window summarized as **~pH 5–8**. (poolman2023physicochemicalhomeostasisin pages 1-2)
- Bacterial cytoplasm scale: ~**1 fL**; at pH ~7.2 about **~10 free protons** (underscoring the necessity of buffering). (poolman2023physicochemicalhomeostasisin pages 1-2)
- Ramoneda et al. 2023 scale and performance: **1470 samples**, **pH 3–10**, Mantel **ρ = 0.37–0.78**, model **R² ≈ 0.80**, MAE **0.43–0.63**, etc. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)

---

## Candidate nodes for TraitMech causal graph (grouped)

### Phenotype / trait nodes
- **METPO:1000478 pH delta high** (growth-supporting external pH breadth ~5–9; label-only assay concept)
- Growth across external pH gradient (label-only)
- Cytoplasmic pH homeostasis (GO:0051453 regulation of intracellular pH; candidate) (krulwich2011molecularaspectsof pages 1-3)

### Environmental / experimental factor nodes
- External pH (ENVO concept for pH; label-only) (beilen2013compartmentspecificphmonitoring pages 3-4)
- Acid stress (label-only)
- Alkaline stress (label-only)

### Biological process / system nodes
- Proton motive force (PMF), ΔpH, Δψ (label-only) (poolman2023physicochemicalhomeostasisin pages 1-2)
- Cytoplasmic buffering capacity (label-only) (poolman2023physicochemicalhomeostasisin pages 1-2)
- Membrane lipid and porin remodeling (GO:0005886 plasma membrane; label-only) (krulwich2011molecularaspectsof pages 6-8)

### Proteins/complexes/transporters (mechanism nodes)
- **Na+/H+ antiporters** (GO:0015385 sodium:proton antiporter activity; includes NhaA) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **K+/H+ antiporters** (label-only; K+:proton antiport activity) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Respiratory proton-pumping enzymes** (GO:1902600 proton transmembrane transport; label-only) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **F0F1-ATPase / ATP synthase** (GO:0046933; EC:7.1.2.2) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Glutamate decarboxylase system (Gad)** (GO:0004351; EC:4.1.1.15) (krulwich2011molecularaspectsof pages 6-8)
- **Kdp K+ transporters (KdpACD)** (GO:0008556 potassium-transporting ATPase activity; candidate) (ramoneda2023buildingagenomebased pages 3-5)
- **Urease / ammonia production machinery** (GO:0009039; EC:3.5.1.5) (ramoneda2023buildingagenomebased pages 3-5)
- Alkaliphile-associated wall factors: teichuronic acids; S-layer protein SlpA (label-only; uncertain generality) (krulwich2011molecularaspectsof pages 6-8)

### Chemicals/metabolites
- H+ (CHEBI:15378) and Na+ (CHEBI:29103) / K+ (CHEBI:29103 for K+ label-only) (poolman2023physicochemicalhomeostasisin pages 1-2)
- Phosphate buffer species (CHEBI:26078 phosphate) (poolman2023physicochemicalhomeostasisin pages 1-2)
- L-glutamate (CHEBI:29987) and GABA (CHEBI:16865) (krulwich2011molecularaspectsof pages 6-8)
- Ammonia (CHEBI:16134) (ramoneda2023buildingagenomebased pages 3-5)

### Assays / measurement nodes
- OD600 growth monitoring across external pH (label-only assay node) (beilen2013compartmentspecificphmonitoring pages 3-4)
- pHluorin/IpHluorin intracellular pH measurement (label-only) (beilen2013compartmentspecificphmonitoring pages 3-4)
- Survival-without-growth (resuscitation) assay (label-only) (krulwich2011molecularaspectsof pages 1-3)

---

## Candidate causal edges (evidence-backed)
The following artifact is designed for direct curation into a YAML causal graph as subject–predicate–object triples with evidence and grounding suggestions.

| Subject node | Predicate (causal) | Object node | Mechanism summary | Evidence snippet | Source (DOI, authors, year, URL) | Confidence | Suggested ontology grounding |
|---|---|---|---|---|---|---|---|
| Na+/H+ antiporters | contributes_to | pH delta high | Na+/H+ antiport is a core regulator of cytoplasmic pH across changing external pH and is broadly implicated in neutralophile homeostasis. | "Key regulators of bacterial pH homeostasis are Na /H and K /H antiporters" (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | GO:0015385 sodium:proton antiporter activity; CHEBI:29103 sodium(1+); CHEBI:15378 hydrogen ion |
| K+/H+ antiporters | contributes_to | pH delta high | K+/H+ antiport complements Na+/H+ exchange in maintaining cytoplasmic pH over a broad external pH span. | "Key regulators of bacterial pH homeostasis are Na /H and K /H antiporters" (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | label-only K+/H+ antiporter; CHEBI:29103 potassium(1+); CHEBI:15378 hydrogen ion |
| respiratory proton-pumping enzymes | helps_maintain | cytoplasmic pH homeostasis | Electron-transport proton pumps are named as major homeostasis regulators that counteract pH stress by controlling proton flux. | "Key regulators of bacterial pH homeostasis are... the proton pumping enzymes (electron transport components in respiratory bacteria" (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | GO:0015992 proton transport; GO:1902600 proton transmembrane transport |
| F0F1-ATPase | contributes_to | pH delta high | F0F1-ATPase participates in pH homeostasis, including proton extrusion or uptake depending on physiology and pH regime. | "Key regulators of bacterial pH homeostasis are... F 0 F 1 -ATPase in lactic acid bacteria" (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | GO:0046933 proton-transporting ATP synthase activity, rotational mechanism; EC:7.1.2.2 |
| metabolite decarboxylation pathways | contributes_to | pH delta high | Proton-consuming decarboxylation pathways support acid resistance and broad pH tolerance by reducing intracellular acidification and coupling to energetics. | "Key regulators... are... metabolite decarboxylation pathways" (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | GO:0016831 carboxy-lyase activity; MetaCyc: glutamate decarboxylation pathway (label-only if unresolved) |
| glutamate decarboxylase system (Gad) | consumes | protons | The Gad acid-response system is a dedicated proton-consuming mechanism supporting low-pH survival and likely one component of broader pH breadth where present. | "glutamate decarboxylation-based acid response in E. coli is a dedicated acid-protection pathway" (krulwich2011molecularaspectsof pages 6-8) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | medium | GO:0004351 glutamate decarboxylase activity; EC:4.1.1.15; CHEBI:29987 L-glutamate; CHEBI:16865 GABA |
| cytoplasmic buffering capacity | stabilizes | cytoplasmic pH homeostasis | High buffering capacity limits pH swings in the tiny bacterial cytoplasm, enabling broader environmental pH tolerance. | "the internal pH of many cell types is kept within the range of 7.0 to 7.5" and buffers absorb fluctuations (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | label-only cytoplasmic buffering capacity; CHEBI:26078 phosphate |
| near-neutral cytoplasmic pH | enables | growth across external pH 5.5-9.0 | Neutralophiles maintain a narrow internal pH while growing over a broader external range, which operationally matches the pH delta high phenotype. | "neutralophilic bacteria... grow at external pH values ~5.5–9.0 while maintaining cytoplasmic pH ~7.5–7.7" (krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | high | GO:0051453 regulation of intracellular pH |
| constant proton motive force (PMF) | supports | pH delta high | A relatively constant PMF across external pH changes is a systems-level hallmark of broad pH tolerance in neutralophiles. | "the proton motive force of neutralophilic bacteria is kept relatively constant in the pH range from 5 to 8" (poolman2023physicochemicalhomeostasisin pages 1-2) | 10.1093/femsre/fuad033; Poolman, 2023; https://doi.org/10.1093/femsre/fuad033 | high | GO:0015985 energy coupled proton transmembrane transport, against electrochemical gradient |
| membrane lipid/porin composition changes | reduces | inward proton leakage | Structural changes in membrane and porin composition lower proton leak during acid stress, helping maintain intracellular pH. | "Membrane lipid and porin composition changes minimize inward proton leakage during acid stress" (krulwich2011molecularaspectsof pages 6-8) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | high | GO:0005886 plasma membrane; GO:0016020 membrane |
| acidic secondary cell-wall polymers (teichuronic acids) | retains_local | protons near cell surface | In alkaliphiles, acidic wall polymers help capture protons near the surface; relevance to pH 5–9 breadth is plausible but extrapolative outside alkaline specialists. | "Alkaliphiles use acidic secondary cell-wall polymers (e.g., teichuronic acids... ) that bind protons near the surface" (krulwich2011molecularaspectsof pages 6-8) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | uncertain | label-only teichuronic acids |
| S-layer protein SlpA | facilitates | adaptation to high external pH | SlpA supports adaptation to alkaline shifts by aiding proton capture/retention at the surface; direct support is strongest for alkaliphiles rather than general euryphily. | "loss of SlpA impairs adaptation from pH 7.5 to 11" (krulwich2011molecularaspectsof pages 6-8) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | uncertain | label-only SlpA; GO:0009274 peptidoglycan-based cell wall |
| urease / ammonia-producing pathways | associated_with | lower-pH preference adaptation | Genomic association analysis links urease-related ammonia production with low-pH adaptation, likely by neutralizing acidity. | "production of basic compounds... ureide_permeases and urease UreE_C producing ammonia" (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998; Ramoneda et al., 2023; https://doi.org/10.1126/sciadv.adf8998 | medium | GO:0009039 urease activity; EC:3.5.1.5; CHEBI:16134 ammonia |
| Kdp K+ transporters (KdpACD) | associated_with | low-pH preference adaptation | Kdp transporters were enriched in taxa preferring lower pH, implicating K+ uptake in acid-side pH adaptation. | "Kdp K+ transporters KdpACD enriched in low-pH taxa" (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998; Ramoneda et al., 2023; https://doi.org/10.1126/sciadv.adf8998 | medium | GO:0008556 potassium-transporting ATPase activity; KEGG:KdpA/KdpB/KdpC/KdpD |
| Na+/H+ antiporter families (PhaGF, MnhG, MrpF, YufB) | associated_with | higher-pH preference adaptation | Comparative genomics linked several antiporter families to taxa preferring higher pH, supporting their relevance at the alkaline side of broad pH breadth. | "Na+/H+ antiporters PhaGF, MnhG, MrpF, YufB... associated with higher-pH taxa" (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998; Ramoneda et al., 2023; https://doi.org/10.1126/sciadv.adf8998 | medium | GO:0015385 sodium:proton antiporter activity; KEGG:Mrp/Mnh family (label-only where specific IDs unresolved) |
| amino-acid decarboxylases | associated_with | low-pH preference adaptation | Comparative genomics recovered amino-acid decarboxylases among genes consistently associated with lower-pH preference. | "proton-consuming reactions (e.g., decarboxylases AAL_decarboxy" (ramoneda2023buildingagenomebased pages 3-5) | 10.1126/sciadv.adf8998; Ramoneda et al., 2023; https://doi.org/10.1126/sciadv.adf8998 | medium | GO:0016831 carboxy-lyase activity |
| acid tolerance response | includes | F1FO-ATPase-mediated pH homeostasis | Applied review literature identifies ATPase-driven pH homeostasis as part of acid tolerance programs used in food/biotech settings. | "physiological acid tolerance response includes pH homeostasis via proton-translocating F1FO-ATPase" (atasoy2024exploitationofmicrobial pages 3-4) | 10.1093/femsre/fuad062; Atasoy et al., 2024; https://doi.org/10.1093/femsre/fuad062 | medium | GO:0046933 proton-transporting ATP synthase activity, rotational mechanism |
| acid tolerance response | includes | membrane fatty-acid modifications | Acid stress responses include membrane remodeling, which likely contributes to broad pH tolerance in strains exposed to fluctuating acidity. | "acid tolerance response includes... membrane fatty-acid modifications" (atasoy2024exploitationofmicrobial pages 3-4) | 10.1093/femsre/fuad062; Atasoy et al., 2024; https://doi.org/10.1093/femsre/fuad062 | medium | GO:0006633 fatty acid biosynthetic process; GO:0016042 lipid catabolic process |
| acid tolerance response | includes | stress-protein production | Stress proteins are part of acid tolerance programs, but direct curation to broad pH breadth should be cautious without trait-specific experiments. | "acid tolerance response includes... stress-protein production" (atasoy2024exploitationofmicrobial pages 3-4) | 10.1093/femsre/fuad062; Atasoy et al., 2024; https://doi.org/10.1093/femsre/fuad062 | uncertain | label-only stress proteins |
| external pH gradient growth assay | measures | observed growth pH breadth | Broad pH phenotype is operationally determined by growth across external pH conditions, typically via OD-based assays. | "pH tolerance or breadth is assessed experimentally by monitoring growth (OD600) and external pH over time" (beilen2013compartmentspecificphmonitoring pages 3-4) | 10.3389/fmicb.2013.00157; van Beilen & Brul, 2013; https://doi.org/10.3389/fmicb.2013.00157 | high | ENVO:00001998 pH; label-only external pH gradient growth assay |
| return to permissive pH assay | distinguishes | survival beyond growth range from true growth breadth | Resumption of growth after return to neutral pH distinguishes survival at extreme pH from actual growth-supporting breadth. | "survival without growth is assessed by resumption of growth upon return... to permissive pH" (krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | high | label-only survival/resuscitation assay |
| pHluorin/IpHluorin intracellular pH measurement | measures | cytoplasmic pH homeostasis | Fluorescent pH reporters enable direct assay of intracellular pH, which is useful for validating mechanisms underlying broad pH growth range. | "reliable internal pH (pHi) readings... over an operational measurement range of pH 5 to 8.5" (beilen2013compartmentspecificphmonitoring pages 3-4) | 10.3389/fmicb.2013.00157; van Beilen & Brul, 2013; https://doi.org/10.3389/fmicb.2013.00157 | high | label-only pHluorin/IpHluorin assay |
| broad growth-supporting external pH range (~5.5-9.0) | operationalizes | pH delta high | The trait is best grounded as an assay-observed growth breadth matching neutralophile growth range rather than specialist acidophile/alkaliphile behavior. | "neutralophilic bacteria... grow at external pH values ~5.5–9.0" (krulwich2011molecularaspectsof pages 1-3) | 10.1038/nrmicro2549; Krulwich, Sachs, Padan, 2011; https://doi.org/10.1038/nrmicro2549 | high | METPO:1000478 pH delta high; ENVO:00001998 pH |


*Table: This table compiles evidence-backed candidate causal edges for curating the microbial trait pH delta high, focusing on mechanisms, assay definitions, and ontology grounding. It prioritizes statements directly supported by the available review and comparative-genomics sources, while flagging taxon-specific or extrapolative claims as uncertain.*

### Visual evidence anchor
Poolman (2023) Figure 2 provides a compact, review-level synthesis of pH homeostasis “key regulators” (antiporters, proton pumps/ATPase, decarboxylation pathways), useful for curating a high-level mechanism scaffold. (poolman2023physicochemicalhomeostasisin media cb4ea770)

---

## Warnings / items to defer from curation
1. **Alkaliphile-specialist cell-wall/S-layer edges** (e.g., teichuronic acids, SlpA) are well-supported for extreme alkaliphiles, but their role as *general* determinants of pH-delta-high across pH 5–9 is **inferred** and should be curated as **uncertain** unless corroborated in euryphilic/neutralophile contexts. (krulwich2011molecularaspectsof pages 6-8)
2. **Gene–pH associations from environmental distributions** (Ramoneda 2023) may not directly translate to growth breadth (pH delta) because the study predicts **realized niche pH** and is limited by pH-range sampling; treat these as **hypothesis-generating** nodes/edges pending lab validation. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5)
3. **Generic stress-protein production** as a causal determinant of pH breadth is plausible but nonspecific; curation should require direct mechanistic linkage to pH-range growth in a defined assay. (atasoy2024exploitationofmicrobial pages 3-4)

---

## DOI-first bibliography (with dates and URLs)
1. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews* (June 2023). DOI: **10.1093/femsre/fuad033**. URL: https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2)
2. Ramoneda J, Stallard-Olivera E, Hoffert M, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* (April 2023). DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 6-7)
3. Atasoy M, Álvarez Ordóñez A, Cenian A, et al. **Exploitation of microbial activities at low pH to enhance planetary health.** *FEMS Microbiology Reviews* (November 2024). DOI: **10.1093/femsre/fuad062**. URL: https://doi.org/10.1093/femsre/fuad062 (atasoy2024exploitationofmicrobial pages 3-4)
4. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology* (May 2011). DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3)
5. van Beilen JWA, Brul S. **Compartment-specific pH monitoring in Bacillus subtilis using fluorescent sensor proteins: a tool to analyze the antibacterial effect of weak organic acids.** *Frontiers in Microbiology* (June 2013). DOI: **10.3389/fmicb.2013.00157**. URL: https://doi.org/10.3389/fmicb.2013.00157 (beilen2013compartmentspecificphmonitoring pages 3-4)


References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (poolman2023physicochemicalhomeostasisin media cb4ea770): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

5. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

6. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

7. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

8. (atasoy2024exploitationofmicrobial pages 3-4): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

9. (atasoy2024exploitationofmicrobial pages 2-3): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

10. (atasoy2024exploitationofmicrobial pages 4-5): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

11. (atasoy2024exploitationofmicrobial pages 26-27): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

12. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

13. (beilen2013compartmentspecificphmonitoring pages 3-4): Johan W. A. van Beilen and Stanley Brul. Compartment-specific ph monitoring in bacillus subtilis using fluorescent sensor proteins: a tool to analyze the antibacterial effect of weak organic acids. Frontiers in Microbiology, Jun 2013. URL: https://doi.org/10.3389/fmicb.2013.00157, doi:10.3389/fmicb.2013.00157. This article has 65 citations and is from a peer-reviewed journal.

14. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.