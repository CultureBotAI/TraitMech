---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:20:18.923554'
end_time: '2026-06-18T00:34:10.963069'
duration_seconds: 832.04
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum
  trait_identifier: METPO:1000331
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH phenotype with numerical limits that represents the external pH
    conditions at which an organism exhibits the most efficient growth and reproduction.
  parent_traits: METPO:1000531, METPO:1000536
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports the external pH at which cytoplasmic pH is best maintained as the operational
    definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force
    (pH-homeostasis review supports the balanced proton motive force at the optimal
    external pH as the mechanism enabling maximal growth.)'
  causal_graph_summary: 'ph_optimum_balanced_homeostasis: 6 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum
- **METPO identifier:** METPO:1000331
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that represents the external pH conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000531, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic pH is best maintained as the operational definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the balanced proton motive force at the optimal external pH as the mechanism enabling maximal growth.)
- **Existing causal graph summary:** ph_optimum_balanced_homeostasis: 6 nodes, 4 edges

## Research Objective

Research the microbial trait **pH optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum.yaml`.

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
- **Trait label:** pH optimum
- **METPO identifier:** METPO:1000331
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that represents the external pH conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000531, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic pH is best maintained as the operational definition of pH optimum.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the balanced proton motive force at the optimal external pH as the mechanism enabling maximal growth.)
- **Existing causal graph summary:** ph_optimum_balanced_homeostasis: 6 nodes, 4 edges

## Research Objective

Research the microbial trait **pH optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum.yaml`.

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


# Microbial Trait Causal Graph Curation Report: pH optimum (METPO:1000331)

## 0) Scope summary (trait meaning, boundaries)

**Trait definition (curation-ready interpretation).** *pH optimum* is an organism-level growth phenotype: the **external pH condition(s) at which an organism’s growth rate (or reproductive output/biomass accumulation) is maximal under a specified medium, temperature, and atmosphere**. This aligns with the mechanistic view that microbes generally maintain cytoplasmic pH near neutral, so the “optimum” external pH is the condition where **pH homeostasis and energy transduction (PMF) are balanced at lowest cost and highest efficiency**. Because “the magnitude of the pH gradient is largely determined by the external pH” when cytoplasmic pH is maintained near neutral, external pH directly reshapes PMF partitioning and the energetic burden of homeostasis. (poolman2023physicochemicalhomeostasisin pages 1-2)

**Distinguish from nearby traits.**
1. **pH tolerance range**: the external pH interval over which growth is possible (or survival/viability is maintained), not necessarily maximal. Example: isolated acidophilic sulfate reducers are reported with **pH ranges** (e.g., 2.9–6.5; 3.6–6.5; 3.8–7.0) as empirical growth ranges. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
2. **Ecological pH preference (realized niche)**: the pH where a taxon reaches **maximal relative abundance in nature**, integrating intrinsic growth optimum plus biotic/abiotic constraints. Ramoneda et al. explicitly define pH preference as the realized niche: “**pH preference is the pH at which an organism achieves maximal relative abundances in nature**,” noting it can differ from the in vitro growth optimum. (ramoneda2023buildingagenomebased pages 1-2)
3. **Cytoplasmic pH homeostasis**: a physiological capacity/constraint (mechanism) that contributes causally to pH optimum but is not the trait itself. Poolman notes “the internal pH of many cell types is kept within the range of 7.0 to 7.5,” and buffering/transport systems maintain it. (poolman2023physicochemicalhomeostasisin pages 1-2)
4. **Acid/alkali resistance**: typically survival/fitness after acute exposure (stress phenotype), which can differ from the pH that maximizes exponential growth.

**Boundary cases (curation warnings).**
- Enzyme “pH optimum” (max activity) is **not** organismal pH optimum; keep separate unless explicitly linked to growth-rate maxima. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13)
- Environmental detection ranges (metagenomic presence across pH) are not growth optima unless validated physiologically. (yao2023howmethanotrophsrespond pages 2-4)

## 1) Key concepts and definitions (current understanding)

### 1.1 Proton motive force (PMF) as the central energetic concept
Poolman (2023) summarizes that PMF drives ATP synthesis and transport and is composed of membrane potential and a pH gradient: “**The proton motive force is composed of the membrane potential … and the pH gradient (ΔpH)**,” and because cytoplasmic pH is near neutral, “**the magnitude of the pH gradient is largely determined by the external pH**.” (poolman2023physicochemicalhomeostasisin pages 1-2)

This implies a mechanistic hypothesis for pH optimum used in TraitMech: the optimal external pH is the condition where **PMF magnitude and partitioning (Δψ vs ΔpH) best support ATP generation, transport, and enzyme function** with minimal homeostatic expenditure. (poolman2023physicochemicalhomeostasisin pages 1-2)

### 1.2 pH homeostasis modules: buffering, antiporters, ATPases, metabolism
Poolman emphasizes buffering and the small absolute proton number in bacterial cytoplasm: for ~1 fL cytoplasm, “**the number of free protons at pH 7.2 is only about 10**,” so buffering (e.g., phosphates) is essential. (poolman2023physicochemicalhomeostasisin pages 1-2)

Key regulators include ion/proton antiporters and proton-pumping systems: “**Key regulators of bacterial pH homeostasis are Na+/H+ and K+/H+ antiporters, the proton pumping enzymes … and metabolite decarboxylation pathways**.” (poolman2023physicochemicalhomeostasisin pages 1-2)

Decarboxylation pathways are explicitly connected to pH and PMF: decarboxylation “**requires a proton, and thus the internal pH is increased**” and “**directly … contribute[s] to pH homeostasis**.” (poolman2023physicochemicalhomeostasisin pages 2-4)

### 1.3 Acidophile and alkaliphile strategies (envelope, membrane potential, transport)
Valdez‑Nuñez et al. (2024) synthesize general acidophile strategies: acidophiles often keep internal pH ~6 even at external pH <3, using “**proton exclusion, exchange, pumping and consumption, and cytoplasmic buffering**.” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

Structural mechanisms to reduce proton permeability include hopanoids and specific proteins: “**hopanoid lipids … or membrane proteins such as Omp40 … and PspA … are structural adaptations used for proton exclusion**.” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

Electrostatic repulsion via cation uptake is highlighted: acidophiles can pump K+ and Na+ in “**to reduce the influx of protons by electrostatic repulsion**.” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

Yao et al. (2023) provide a consolidated schematic for methanotrophs and describe lipid saturation reducing proton permeability, and S-layer/negative surface charge enhancing proton attraction in alkaliphiles. (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media e5c40e89)

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 2023: Physicochemical homeostasis framework (bacteria)
Poolman (FEMS Microbiology Reviews; advance access **19 Jun 2023**) provides an updated synthesis connecting **energy status, PMF, internal pH, buffering, transport, and decarboxylation** as a coupled homeostatic network. Key quantitative points for curation include: ΔpH contribution depends on external pH; only ~10 free protons at pH 7.2 in ~1 fL cytoplasm; F0F1 ATP synthase uses “**three to five protons**” per ATP. (poolman2023physicochemicalhomeostasisin pages 1-2)

### 2.2 2023: Genome-based prediction of bacterial pH preferences (realized niche)
Ramoneda et al. (Science Advances; **28 Apr 2023**) analyzed **five datasets spanning soil/freshwater pH gradients (pH 3–10) totaling 1470 samples** and inferred pH preferences from abundance maxima. (ramoneda2023buildingagenomebased pages 1-2)

They explicitly define pH preference as realized niche and note that cultivated taxa often lack experimentally determined pH optima/tolerances. (ramoneda2023buildingagenomebased pages 1-2)

Mechanistically relevant genomic associations include Na+/H+ antiporters and Kdp transporters being enriched in taxa with higher vs lower pH preferences, respectively (correlative evidence). (ramoneda2023buildingagenomebased pages 3-5)

### 2.3 2024: Acidophilic sulfate-reducing bacteria (aSRB) and applications
Valdez‑Nuñez et al. (Environmental Microbiology Reports; **Oct 2024**) review aSRB diversity and emphasizes mechanistic parallels with broader acidophile homeostasis and envelope adaptation. It also compiles isolate pH ranges in Table 1 (e.g., 2.9–6.5; 3.6–6.5; 3.8–7.0). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 2.4 2024: Applied stress physiology perspective (LAB/food systems)
Sionek et al. (Fermentation; **Jun 2024**) synthesizes lactic acid bacteria survival and notes determinants such as “**F1F0-ATPase activity under markedly acidic conditions**, membrane composition and functionality, … intracellular buffering, and enzyme stability,” situating pH optimum/tolerance as multifactorial and relevant for food fermentation and probiotic viability. (sionek2024theimpactof pages 14-15)

## 3) Current applications and real-world implementations

1. **Cultivation strategy and inoculant selection.** Genome-based prediction of pH preference can “aid in the selection of microbial inoculants” and “help design effective cultivation strategies” by estimating where taxa reach peak abundance along pH gradients. (yao2023howmethanotrophsrespond pages 5-7)
2. **Bioremediation / AMD treatment.** aSRB are discussed for treating acid mine drainage (AMD; pH often <3) and for recovery of metal sulfides/nanoparticles; homeostasis under low pH is a prerequisite for function. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
3. **Food fermentation and probiotic robustness.** LAB viability is sensitive to combined stressors; adjusting “optimal physicochemical conditions” including pH supports survival and product quality. (sionek2024theimpactof pages 14-15)
4. **Extremophile biotechnology.** Acidophilic fungi and alkaliphilic fungi produce enzymes stable/active at extreme pH for industrial processes; organismal pH optimum informs strain selection and process pH setpoints. (ianutsevich2023theroleof pages 1-2, fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13)

## 4) Candidate causal graph entities (nodes) grouped by type

### 4.1 Core phenotype / assay nodes
- **pH optimum (external)** (METPO:1000331) — *target trait*
- label-only: **growth rate**, **doubling time**, **biomass accumulation** (assay readouts)
- label-only: **culture medium buffering capacity**, **temperature**, **ionic strength**, **salinity** (experimental modifiers)

### 4.2 Physicochemical / process nodes
- **proton motive force** (GO:0045333) (poolman2023physicochemicalhomeostasisin pages 1-2)
- label-only: **ΔpH (pH gradient)**; label-only: **Δψ (membrane potential)** (poolman2023physicochemicalhomeostasisin pages 1-2)
- label-only: **cytoplasmic pH homeostasis**; label-only: **cytoplasmic buffering capacity** (poolman2023physicochemicalhomeostasisin pages 1-2)
- label-only: **proton exclusion**; label-only: **proton influx/efflux** (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 4.3 Complexes / pathways
- **F0F1 ATP synthase / ATPase** (GO:0045263) (poolman2023physicochemicalhomeostasisin pages 1-2)
- label-only: **respiratory complexes I/III/IV** (proton pumps) (yao2023howmethanotrophsrespond media e5c40e89)
- label-only: **amino-acid decarboxylation pathways** (pH homeostasis and PMF generation) (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 1-2)
- **urease** (EC:3.5.1.5) and **urea transport** (GO:0015204) (ramoneda2023buildingagenomebased pages 3-5)

### 4.4 Transporters and ion homeostasis
- **Na+/H+ antiporter activity** (GO:0015385) (poolman2023physicochemicalhomeostasisin pages 1-2)
- label-only: **K+/H+ antiporter activity** (poolman2023physicochemicalhomeostasisin pages 1-2)
- **potassium ion transmembrane transporter activity** (GO:0015079) (yao2023howmethanotrophsrespond pages 5-7)
- label-only: **Kdp system (KdpACD)** (ramoneda2023buildingagenomebased pages 3-5)
- label-only: **symporters/antiporters** for proton extrusion (yao2023howmethanotrophsrespond media e5c40e89)

### 4.5 Envelope/membrane structure nodes
- **membrane** (GO:0016020)
- **saturated fatty acid** (CHEBI) (yao2023howmethanotrophsrespond pages 5-7)
- label-only: **S-layer protein / SCWPs** (yao2023howmethanotrophsrespond pages 5-7)
- label-only: **hopanoid lipids**, **Omp40**, **PspA** (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 4.6 Fungal-specific regulatory/homeostasis nodes (optional cross-domain extensions)
- label-only: **V-ATPase**; label-only: **Pma1 proton pump** (ianutsevich2023theroleof pages 1-2)
- label-only: **Pal/Rim pathway**; label-only: **PacC/Rim101 transcription factor** (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)

## 5) Evidence-backed candidate causal edges (curation table)

The following table is directly designed for `data/traits/environment/ph_optimum.yaml` curation.

| Edge (subject—predicate—object) | Node grounding suggestions (CURIEs where possible) | Evidence snippet (verbatim quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|
| external pH gradient (ΔpH) — contributes to — proton motive force (PMF) | GO:0045333 proton motive force; label-only: external pH gradient/ΔpH | “The proton motive force is composed of the membrane potential … and the pH gradient (ΔpH, typically inside alkaline relative to the outside).” / “Since cells maintain their cytoplasmic pH around neutral, the magnitude of the pH gradient is largely determined by the external pH.” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong general edge for bacteria; directly links external pH to PMF component. |
| proton motive force (PMF) — drives — ATP synthesis by F0F1-ATP synthase | GO:0045333 proton motive force; GO:0006754 ATP biosynthetic process; GO:0045263 proton-transporting ATP synthase complex | “Protons participate in numerous reactions and serve as a source of electrochemical energy (proton motive force, PMF …) to drive the synthesis of ATP” / “the F0F1-ATP synthase uses three to five protons to synthesize one molecule of ATP.” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong mechanistic edge; central to why balanced PMF supports growth optimum. |
| Na+/H+ antiporter activity — acidifies — cytoplasm when internal pH is too high | GO:0015385 sodium:proton antiporter activity | “Proton-sensing ion/H+ antiporters acidify the cytoplasm by exporting K+ or Na+ in exchange for protons when the internal pH gets too high” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong general edge; antiporters are key pH-homeostasis nodes. |
| K+/H+ antiporter activity — acidifies — cytoplasm when internal pH is too high | label-only: K+/H+ antiporter activity | “Proton-sensing ion/H+ antiporters acidify the cytoplasm by exporting K+ or Na+ in exchange for protons when the internal pH gets too high” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong but grounding for K+/H+ antiporter may remain label-only unless a stable ontology term is selected. |
| F0F1-ATPase upregulation/activation — prevents — internal pH from becoming too low | GO:0045263 proton-transporting ATP synthase complex | “Upregulation and or activation of the components of proton-pumping respiratory chains … the F0F1-ATPase (fermentative bacteria), or decarboxylation pathways … prevent the internal pH from becoming too low” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong for fermentative bacteria; directionality is homeostatic support, not direct determination of optimum alone. |
| metabolite decarboxylation pathways — contribute to — pH homeostasis | GO:0016831 carboxy-lyase activity; label-only: amino-acid decarboxylation pathway | “the chemistry of the decarboxylation reaction requires a proton, and thus the internal pH is increased” / “the enzymes have a built-in self-regulatory mechanism to deal with lower pH values and thus directly … contribute to pH homeostasis” (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong; useful causal edge between proton-consuming metabolism and homeostasis. |
| decarboxylation pathways — generate — proton motive force | GO:0045333 proton motive force; label-only: decarboxylation pathway | “the free energy change from decarboxylation reactions can be stored in the form of a proton motive force” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong mechanistic edge; supports existing graph summary around balanced homeostasis. |
| cytoplasmic buffering capacity — stabilizes — internal pH | GO:0005737 cytoplasm; label-only: cytoplasmic buffering capacity; CHEBI: phosphate | “The buffering capacity of the cytoplasm is important in absorbing pH fluctuations.” / “there would not be sufficient buffering capacity (e.g. inorganic and organic phosphates)” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023. DOI:10.1093/femsre/fuad033. 2023-06-19. https://doi.org/10.1093/femsre/fuad033 | Strong general edge; buffering is a core non-gene homeostatic determinant. |
| saturated membrane fatty acids — reduce — proton permeability of cytoplasmic membrane | GO:0016020 membrane; CHEBI: saturated fatty acid | “The membrane of acidophilic verrucomicrobial methanotrophs was almost made up of saturated fatty acids … verrucomicrobial methanotrophs required a saturated membrane to minimize proton permeability in an extremely acidic environment” (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023. DOI:10.3389/fmicb.2022.1034164. 2023-01-12. https://doi.org/10.3389/fmicb.2022.1034164 | Good mechanistic edge, but taxon-specific to acidophilic methanotrophs unless generalized cautiously. |
| K+ uptake transporter activity — generates — internal positive membrane potential | GO:0015079 potassium ion transmembrane transporter activity; GO:0016020 membrane | “The internal positive transmembrane electrical potential helps to maintain a cytoplasmic pH that is only mildly acidic.” / “the blue oval refers to the potassium uptake transporter that helps generate an internal positive membrane potential.” (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media e5c40e89) | Yao et al. 2023. DOI:10.3389/fmicb.2022.1034164. 2023-01-12. https://doi.org/10.3389/fmicb.2022.1034164 | Strong within figure/text synthesis; especially relevant to acidophiles. |
| internal positive membrane potential — reduces — proton influx | label-only: positive membrane potential; GO:1902600 proton transmembrane transport | “Acidophiles, including aSRB, can pump cations such as K+ and Na+ into the cytoplasm to reduce the influx of protons by electrostatic repulsion” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Valdez-Nuñez et al. 2024. DOI:10.1111/1758-2229.70019. 2024-10. https://doi.org/10.1111/1758-2229.70019 | Strong for acidophiles/aSRB; may be curated as acidophile-specific unless broader support added. |
| S-layer glycoprotein / SCWP — increases attraction to — external protons | GO:0009277 bacterial-type cell wall; label-only: S-layer glycoprotein; label-only: secondary cell wall polymers | “the second cell wall polymers (SCWPs), such as S-layer protein, are developed by alkaliphilic microbes. These components enhance net negative charges on cellular surfaces that increase attraction to external protons” (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023. DOI:10.3389/fmicb.2022.1034164. 2023-01-12. https://doi.org/10.3389/fmicb.2022.1034164 | Good mechanistic edge for alkaliphiles; taxon-specific and should be marked conditional on alkaline adaptation. |
| phospholipid remodeling (↑PG/PC/CL; ↓PE/PS/PA) — adapts — membrane proton-flux regulation at high pH | CHEBI: phosphatidylglycerol; CHEBI: phosphatidylcholine; CHEBI: cardiolipin; CHEBI: phosphatidylethanolamine; CHEBI: phosphatidylserine; CHEBI: phosphatidic acid | “methanotrophs also adapted the composition of the cell membrane to regulate the proton flux. For instance, Methylomicrobium alcaliphilum 20Z modified its phospholipid composition based on salinity and pH values” (yao2023howmethanotrophsrespond pages 5-7) | Yao et al. 2023. DOI:10.3389/fmicb.2022.1034164. 2023-01-12. https://doi.org/10.3389/fmicb.2022.1034164 | Useful but species-specific; edge may be too detailed for a generic trait graph without broader corroboration. |
| hopanoid lipids / Omp40 / PspA — decrease — proton permeability | CHEBI: hopanoid; UniProt: label-only Omp40; UniProt: PspA family label-only | “The presence of hopanoid lipids in the cytoplasmic membrane … or membrane proteins such as Omp40 … and PspA … are structural adaptations used for proton exclusion in acidophilic bacteria.” (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Valdez-Nuñez et al. 2024. DOI:10.1111/1758-2229.70019. 2024-10. https://doi.org/10.1111/1758-2229.70019 | Good acidophile-focused edge; probably uncertain for broad microbial curation absent wider evidence. |
| vacuolar-type ATPase and Pma1 proton pump — regulate — intracellular pH in fungi | GO:0015991 ATP hydrolysis coupled proton transport; GO:0008553 hydrogen-exporting ATPase activity; UniProt: Pma1 label-only | “In fungi, the intracellular pH regulation system includes vacuolar-type ATPases (V-ATPase) and a P-type proton pump Pma1, acting with many other transporters” (ianutsevich2023theroleof pages 1-2) | Ianutsevich et al. 2023. DOI:10.3390/microorganisms11071733. 2023-07-01. https://doi.org/10.3390/microorganisms11071733 | Strong fungal homeostasis edge; relevant if TraitMech graph is domain-general across bacteria/fungi. |
| osmolytes and membrane lipids — participate in — adaptation to acidophilic growth optimum | CHEBI: trehalose; CHEBI: polyol; CHEBI: phosphatidic acid; CHEBI: phosphatidylethanolamine; CHEBI: phosphatidylcholine; CHEBI: sterol | “P. gigantea had a narrow optimum of growth at pH 4.0 … accompanied by a decrease in the number of osmolytes and significant changes in the composition of membrane lipids.” / “the data obtained indicate the participation of osmolytes and membrane lipids in the adaptation of acidophilic fungi.” (ianutsevich2023theroleof pages 1-2) | Ianutsevich et al. 2023. DOI:10.3390/microorganisms11071733. 2023-07-01. https://doi.org/10.3390/microorganisms11071733 | Good phenotype-linked edge; fungal and somewhat assay-specific. |
| F1F0-ATPase activity under acidic conditions — supports — active pH homeostasis / acid tolerance | GO:0045263 proton-transporting ATP synthase complex | “active pH homeostasis systems (e.g., F1F0-ATPase activity under markedly acidic conditions), membrane composition and functionality, specific transporters and proton pumps that maintain proton motive force, intracellular buffering, and enzyme stability.” (sionek2024theimpactof pages 14-15) | Sionek et al. 2024. DOI:10.3390/fermentation10060298. 2024-06. https://doi.org/10.3390/fermentation10060298 | Review-level corroboration rather than new primary evidence; useful support for generality across LAB/food microbes. |
| membrane composition/functionality — contributes to — external pH optimum / survival across pH | GO:0016020 membrane | “major determinants of microbial external pH optimum and acid tolerance: active pH homeostasis systems … membrane composition and functionality, specific transporters and proton pumps that maintain proton motive force, intracellular buffering, and enzyme stability” (sionek2024theimpactof pages 14-15) | Sionek et al. 2024. DOI:10.3390/fermentation10060298. 2024-06. https://doi.org/10.3390/fermentation10060298 | Good summary support, but this is secondary synthesis rather than direct mechanistic demonstration. |
| Na+/H+ antiporter gene families (e.g., PhaGF, MnhG, MrpF, YufB) — are overrepresented in — taxa with higher pH preference | label-only: PhaGF; label-only: MnhG; label-only: MrpF; label-only: YufB; GO:0015385 sodium:proton antiporter activity | “Na+/H+ antiporters [PhaGF, MnhG, MrpF, and YufB; (33)] … were overrepresented in taxa with preferences for higher pH.” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023. DOI:10.1126/sciadv.adf8998. 2023-04-28. https://doi.org/10.1126/sciadv.adf8998 | Association edge from comparative genomics, not direct causation; should be flagged inferred/correlative. |
| Kdp K+ membrane transporter genes (KdpACD) — are overrepresented in — taxa with low pH preference | GO:0006813 potassium ion transport; label-only: KdpA/KdpC/KdpD | “genes for a wide range of cation and anion efflux pumps such as the Kdp K+ membrane transporters (KdpACD) … were overrepresented in taxa with low pH preference in all habitats.” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023. DOI:10.1126/sciadv.adf8998. 2023-04-28. https://doi.org/10.1126/sciadv.adf8998 | Correlative genome-trait association; useful candidate node/edge but not sufficient alone for causal curation. |
| urease / urea transport system — counteracts — acidity via ammonia production | EC:3.5.1.5 urease; GO:0015204 urea transmembrane transporter activity | “cells will produce basic compounds, such as ammonia released from urea to counter acidity. We found genes assigned to urea membrane transporters … as well as a gene for urease … that hydrolyzes urea into ammonia” (ramoneda2023buildingagenomebased pages 3-5) | Ramoneda et al. 2023. DOI:10.1126/sciadv.adf8998. 2023-04-28. https://doi.org/10.1126/sciadv.adf8998 | Correlative genomic support plus established mechanism; still not directly a universal determinant of pH optimum. |
| Pal/Rim signaling pathway — activates — PacC pH-responsive transcription factor | GO:0007165 signal transduction; label-only: Pal/Rim pathway; label-only: PacC/Rim101 | “the Pal/Rim signal transduction pathway controls pH-responsive transcription via proteolytic activation of the zinc-finger factor PacC” (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7) | Fernández-López et al. 2023. DOI:10.3390/jof9060652. 2023-06. https://doi.org/10.3390/jof9060652 | Mechanistically strong for fungal pH response, but indirect for external pH optimum; curate only if including regulatory response nodes. |
| PacC active form — activates/represses — alkaline-expressed vs acid-expressed genes | label-only: PacC27; GO:0045893 positive regulation of transcription, DNA-templated; GO:0045892 negative regulation of transcription, DNA-templated | “PacC27 represses acid-expressed genes and activates alkaline-expressed genes.” (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7) | Fernández-López et al. 2023. DOI:10.3390/jof9060652. 2023-06. https://doi.org/10.3390/jof9060652 | Likely relevant to fungal alkaline preference, but connection to growth optimum remains indirect and should be marked uncertain. |


*Table: This table compiles evidence-backed candidate causal edges for curating a TraitMech graph of microbial external pH optimum. It emphasizes directly supported homeostasis mechanisms and flags correlative or taxon-specific claims that may require cautious curation.*

## 6) Visual evidence (mechanism schematic)

Yao et al. provide a schematic summarizing **acidophilic vs alkaliphilic** homeostasis modules (saturated membranes; K+ uptake for positive potential; symporters/antiporters; respiratory proton pumps + F0F1-ATPase; alkaliphile S-layer and lipid remodeling; potential sequestered proton transfer). (yao2023howmethanotrophsrespond media e5c40e89)

## 7) Relevant statistics and data points from recent studies

- **PMF / buffering quantitative context (bacteria):** In ~1 fL cytoplasm, “**the number of free protons at pH 7.2 is only about 10**,” highlighting reliance on buffering and regulated transport; ATP synthase uses “**three to five protons**” per ATP. (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Environmental pH preference inference dataset size:** 5 datasets, **1470 total samples**, spanning **pH 3–10**, and 250,275 ASVs. (ramoneda2023buildingagenomebased pages 1-2)
- **Coverage of preference inference:** pH preferences could be estimated for only **0.5–4.9% of ASVs per dataset** under conservative criteria. (ramoneda2023buildingagenomebased pages 1-2)
- **Genome-based model performance/limits:** The pH preference model’s reported error includes **MAE ~0.63 pH units**, and is reliable mainly between ~pH 4 and 9 (limitations stated in the study). (ramoneda2023buildingagenomebased pages 6-7)
- **Acidophilic sulfate reducers pH ranges (examples):** isolate pH ranges include **2.9–6.5**, **3.6–6.5**, **3.8–7.0**, etc. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

## 8) Expert synthesis and analysis (authoritative perspective)

**Mechanistic integration (TraitMech-friendly).** The most robust, cross-taxon mechanistic spine for pH optimum is:

**external pH → ΔpH component of PMF → energy available for transport/ATP → ability/cost to maintain cytoplasmic pH near neutral → growth rate maximum**.

Poolman’s synthesis supports this by explicitly tying external pH to ΔpH, PMF, ATP synthesis, and the homeostasis modules that prevent cytoplasmic pH from becoming too low (antiporters, respiratory chains, F0F1-ATPase, decarboxylation, buffering). (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4)

**Taxon-specific adaptations as modular add-ons.** Acidophile-specific structural features (hopanoids, Omp40, PspA, positive membrane potential via cation uptake) and alkaliphile strategies (S-layer-based proton attraction, lipid remodeling, potential sequestered proton transfer) are well supported in specific contexts but may require curation as conditional subgraphs (e.g., for acidophiles/alkaliphiles) rather than universal edges. (yao2023howmethanotrophsrespond pages 5-7, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, yao2023howmethanotrophsrespond media e5c40e89)

**Genomic association vs causality.** Ramoneda et al. provide valuable candidate nodes (e.g., Na+/H+ antiporters, Kdp) associated with pH preference across environments, but these are **correlative** (presence/absence enriched among taxa with certain inferred preferences). Curate these as **inferred/uncertain edges** unless validated by perturbation/physiology. (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-2)

## 9) Warnings (claims not yet ready for strong curation)

1. **Do not equate pH preference (realized niche) with in vitro pH optimum.** Ramoneda et al. explicitly frame pH preference as realized niche influenced by other constraints. (ramoneda2023buildingagenomebased pages 1-2)
2. **Correlative gene enrichments are not causal mechanisms by themselves.** Antiporter/Kdp/urease enrichments should be labeled *inferred* until tested with gene knockouts/physiological assays. (ramoneda2023buildingagenomebased pages 3-5)
3. **Species-specific membrane lipid shifts (e.g., particular phospholipid ratios) may be overfit.** Use as conditional nodes/edges or as examples rather than universal traits. (yao2023howmethanotrophsrespond pages 5-7)
4. **Fungal signaling pathways (Pal/Rim→PacC) regulate pH response but may not directly determine growth pH optimum** without organism-level growth evidence across pH gradients. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)

## 10) DOI-first bibliography (with URLs and publication dates where available)

1. Poolman B. *Physicochemical homeostasis in bacteria.* **FEMS Microbiology Reviews**. Advance access publication date: **19 Jun 2023**. DOI: **10.1093/femsre/fuad033**. https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2)
2. Ramoneda J, Stallard-Olivera E, Hoffert M, et al. *Building a genome-based understanding of bacterial pH preferences.* **Science Advances**. **28 Apr 2023**. DOI: **10.1126/sciadv.adf8998**. https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-2)
3. Yao X, Wang J, Hu B. *How methanotrophs respond to pH: A review of ecophysiology.* **Frontiers in Microbiology**. **Jan 2023**. DOI: **10.3389/fmicb.2022.1034164**. https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)
4. Valdez‑Nuñez LF, Kappler A, Ayala‑Muñoz D, et al. *Acidophilic sulphate‑reducing bacteria: Diversity, ecophysiology, and applications.* **Environmental Microbiology Reports**. **Oct 2024**. DOI: **10.1111/1758-2229.70019**. https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
5. Ianutsevich EA, Danilova OA, Grum‑Grzhimaylo OA, Tereshina VM. *The Role of Osmolytes and Membrane Lipids in the Adaptation of Acidophilic Fungi.* **Microorganisms**. Published: **1 Jul 2023**. DOI: **10.3390/microorganisms11071733**. https://doi.org/10.3390/microorganisms11071733 (ianutsevich2023theroleof pages 1-2)
6. Sionek B, Szydłowska A, Trząskowska M, Kołożyn‑Krajewska D. *The Impact of Physicochemical Conditions on Lactic Acid Bacteria Survival in Food Products.* **Fermentation**. **Jun 2024**. DOI: **10.3390/fermentation10060298**. https://doi.org/10.3390/fermentation10060298 (sionek2024theimpactof pages 14-15)
7. Fernández‑López MG, Batista‑García RA, Aréchiga‑Carvajal ET. *Alkaliphilic/Alkali‑Tolerant Fungi: Molecular, Biochemical, and Biotechnological Aspects.* **Journal of Fungi**. **Jun 2023**. DOI: **10.3390/jof9060652**. https://doi.org/10.3390/jof9060652 (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7)

References

1. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

3. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

4. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 12-13): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

5. (yao2023howmethanotrophsrespond pages 2-4): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

6. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

7. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

8. (yao2023howmethanotrophsrespond media e5c40e89): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

9. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

10. (sionek2024theimpactof pages 14-15): Barbara Sionek, Aleksandra Szydłowska, Monika Trząskowska, and Danuta Kołożyn-Krajewska. The impact of physicochemical conditions on lactic acid bacteria survival in food products. Fermentation, 10:298, Jun 2024. URL: https://doi.org/10.3390/fermentation10060298, doi:10.3390/fermentation10060298. This article has 125 citations.

11. (ianutsevich2023theroleof pages 1-2): Elena A. Ianutsevich, Olga A. Danilova, Olga A. Grum-Grzhimaylo, and Vera M. Tereshina. The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi. Microorganisms, 11:1733, Jul 2023. URL: https://doi.org/10.3390/microorganisms11071733, doi:10.3390/microorganisms11071733. This article has 22 citations.

12. (fernandezlopez2023alkaliphilicalkalitolerantfungimolecular pages 4-7): Maikel Gilberto Fernández-López, Ramón Alberto Batista-García, and Elva Teresa Aréchiga-Carvajal. Alkaliphilic/alkali-tolerant fungi: molecular, biochemical, and biotechnological aspects. Journal of Fungi, 9:652, Jun 2023. URL: https://doi.org/10.3390/jof9060652, doi:10.3390/jof9060652. This article has 35 citations.

13. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.