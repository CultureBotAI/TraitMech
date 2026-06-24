---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:29:58.314334'
end_time: '2026-06-18T00:38:14.565547'
duration_seconds: 496.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum mid2
  trait_identifier: METPO:1000457
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH between approximately
    7 and 8, corresponding to neutrophilic or moderately alkaliphilic physiology.
  parent_traits: METPO:1000331
  synonyms: Alkali Tolerant, Alkaliphile, Neutrophile, pHO_7_to_8
  evidence_summary: "DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review\
    \ supports the 7\u20138 external-pH range as the common neutrophile / moderately\
    \ alkaline-tolerant optimum.)"
  causal_graph_summary: 'ph_optimum_mid2_alkaline_tolerant_setpoint: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum mid2
- **METPO identifier:** METPO:1000457
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 7 and 8, corresponding to neutrophilic or moderately alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Neutrophile, pHO_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the 7–8 external-pH range as the common neutrophile / moderately alkaline-tolerant optimum.)
- **Existing causal graph summary:** ph_optimum_mid2_alkaline_tolerant_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid2.yaml`.

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
- **Trait label:** pH optimum mid2
- **METPO identifier:** METPO:1000457
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH between approximately 7 and 8, corresponding to neutrophilic or moderately alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Neutrophile, pHO_7_to_8
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the 7–8 external-pH range as the common neutrophile / moderately alkaline-tolerant optimum.)
- **Existing causal graph summary:** ph_optimum_mid2_alkaline_tolerant_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pH optimum mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_mid2.yaml`.

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


## Microbial Trait Causal Graph Curation Report: pH optimum mid2 (METPO:1000457)

### Scope summary (TraitMech curation)
**Trait label:** pH optimum mid2 (METPO:1000457)  
**Definition (given):** best-growth external pH approximately **7–8**, corresponding to neutrophilic or moderately alkaliphilic physiology.

**Operational meaning for curation.** The trait should be treated as a **growth optimum** (e.g., maximal specific growth rate, biomass accumulation rate, or reproducible maximum OD increase) in a controlled assay across a pH gradient, not merely a tolerance range. In many bacteria, **cytoplasmic pH is maintained near neutral (~7.0–7.5)**, meaning that for organisms with optimum external pH 7–8, the ΔpH component of proton motive force (PMF) is typically modest and the energetic/transport requirements shift toward maintaining membrane potential and ion balances. (poolman2023physicochemicalhomeostasisin pages 1-2)

**Boundary cases (distinguish from nearby traits).**
- **Acidophilic optimum**: growth optimum substantially below 7; extreme acidophiles often have optimum pH <3 (out of scope here).
- **Strict neutrophile**: may be narrower around ~6.5–7.5.
- **Moderate alkaliphile**: optimal pH can extend above 8; overlap exists at 7.5–8.0.
- **Hyperalkaliphile**: optimum often >10 (clearly outside mid2).

### Key concepts and current understanding (mechanistic framing)
1. **Intracellular pH homeostasis as a growth constraint.** Because the absolute number of free protons in a bacterial cytoplasm is extremely small (Poolman notes ~**10 free protons at pH 7.2** for a ~**1 fL** cytoplasmic volume), buffering and regulated transport are essential to prevent disruptive pHi excursions that would impair enzyme function and membrane stability. (poolman2023physicochemicalhomeostasisin pages 1-2)
2. **PMF coupling and external pH.** PMF is composed of membrane potential (Δψ) and ΔpH; because bacteria maintain cytoplasmic pH around neutral, **external pH largely determines ΔpH** and thus the relative contributions of Δψ vs ΔpH to PMF. (poolman2023physicochemicalhomeostasisin pages 1-2)
3. **Transport-centric pH control near neutral pH.** Key regulators include **Na+/H+ and K+/H+ antiporters** and energy-linked proton cycling via respiration and/or F0F1-ATPase. Antiporters can acidify cytoplasm by importing protons when pHi rises (a relevant control mode when external pH is neutral-to-mildly alkaline). (poolman2023physicochemicalhomeostasisin pages 1-2)

### Recent developments (prioritizing 2023–2024)
#### 1) Quantitative constraints and mechanistic synthesis (2023)
Poolman (FEMS Microbiology Reviews, 2023) synthesizes quantitative constraints on pHi control (pHi 7.0–7.5; ~10 free protons at pH 7.2 in ~1 fL), emphasizes buffering capacity (e.g., phosphate pools), and highlights core regulators (Na+/H+ and K+/H+ antiporters; respiratory proton pumps; F0F1-ATPase; decarboxylation pathways). (poolman2023physicochemicalhomeostasisin pages 1-2)

#### 2) Genome-based associations with pH preference (2023)
Ramoneda et al. (Science Advances, 2023) infer bacterial pH preferences across large environmental gradients and identify gene families associated with pH preference. For **higher pH preference**, they report overrepresentation of **Na+/H+ antiporters** (PhaGF, MnhG, MrpF, YufB) and certain anion transporters; for lower pH preference, Kdp K+ transporters are overrepresented. This evidence is **associational**, useful for candidate-node nomination but not sufficient alone to assert causality in TraitMech without additional mechanistic support. (ramoneda2023buildingagenomebased pages 3-5)

#### 3) Systems-level modeling tying PMF and antiporters to extracellular pH range (2024)
Terradot et al. (PRX Life, 2024) provide a quantitative model + single-cell measurements linking **PMF magnitude** to the **extracellular pH range** over which near-neutral pHi can be maintained. Their model predicts **antiporter “regimes”** by external pH: **NhaB-like antiporter** dominates roughly **pHe 5–9** (which contains the 7–8 optimum window), while **NhaA-like antiporter** dominates **pHe ~9–12**, with **NhaA activity increasing above ~pHe 6.5**. This supports treating antiporter identity/stoichiometry and PMF as central mechanistic determinants for growth across neutral–mildly alkaline conditions. (terradot2024escherichiacolimaintains pages 8-9)

#### 4) Alkaliphile membrane-proteome evidence for supportive modules (2023)
de Jong et al. (Frontiers in Microbiology, 2023) show that the thermoalkaliphile *Caldalkalibacillus thermarum* TA2.A1 grows from **pH 7.5 to 11** and discuss membrane/proteome components important for alkaliphile physiology, including F1Fo-ATP synthase (also “thought to regulate cytoplasmic pH”) and transporters for compatible solutes **ectoine** and **glycine betaine**, which “may assist in maintaining a near neutral internal pH when the external pH is highly alkaline.” This provides candidate edges for moderate-to-strong alkaliphily; for pH optimum mid2 these are best treated as **boundary-case / uncertain** unless validated in neutrophiles. (jong2023membraneproteomeof pages 1-2)

### Current applications and real-world implementations (how this trait is used)
1. **Microbial ecology / prediction of community structure by pH.** Environmental pH is a major structuring factor for microbial communities; genome-based inference of pH preference is being developed for applications such as cultivation strategy and inoculant selection (e.g., predicting which genomes encode machinery associated with higher vs lower pH preference). (ramoneda2023buildingagenomebased pages 3-5)
2. **Strain selection for neutral-to-mildly alkaline bioprocesses.** In fermentation/biomanufacturing and environmental biotechnology, organisms with robust pHi homeostasis around external pH ~7–8 can be preferred due to enzyme stability and compatibility with many industrial media; mechanistic tuning points include antiporters and energy metabolism that sustain PMF under process conditions (oxygen availability, ionic strength). (poolman2023physicochemicalhomeostasisin pages 1-2, terradot2024escherichiacolimaintains pages 1-2)

### Expert opinions / analysis (authoritative synthesis)
- **Poolman 2023** frames bacterial physicochemical homeostasis as tightly coupled to energy status; pH control depends on buffering, PMF management, and transporter networks with distinct pH sensitivities, emphasizing that multiple systems are typically deployed rather than a single universal gene. (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Terradot et al. 2024** argue for a “shift of perspective” in bacterial electrophysiology, in which proton-ion antiporters are key to generating/maintaining membrane potential and PMF needed for pHi homeostasis across external pH. (terradot2024escherichiacolimaintains pages 8-9, terradot2024escherichiacolimaintains pages 4-5)

### Relevant quantitative statistics and data points (recent sources)
- **Internal pH range:** many cells maintain pHi **7.0–7.5**. (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Free proton count constraint:** at **pH 7.2**, ~**10 free protons** in ~**1 fL** cytoplasm (illustrates why buffering and controlled transport are essential). (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Antiporter regime predictions (E. coli model):** NhaB-like antiporter optimal use **pHe ~5–9**; NhaA-like **pHe ~9–12**; NhaA activity increases when pHe > **~6.5**. (terradot2024escherichiacolimaintains pages 8-9)
- **Energy coupling:** F0F1-ATP synthase uses **~3–5 protons per ATP** (species-dependent), linking PMF and growth energetics. (poolman2023physicochemicalhomeostasisin pages 1-2)

### Visual evidence (mechanistic schematic)
Poolman 2023 provides a schematic (Figure 2) linking **decarboxylation-driven PMF generation** and **PMF utilization by antiporters and ATP synthase**—a useful conceptual backbone for the causal graph. (poolman2023physicochemicalhomeostasisin media 9ecadea6)

---

## Candidate causal-graph nodes (grouped by type)

### Phenotypes / processes
- **pH optimum mid2** (METPO:1000457) — external pH optimum 7–8 (given)
- **Intracellular pH homeostasis / cytoplasmic pH regulation** (label; candidate GO term: GO:0006885 “regulation of pH” is broad—use label if unsure)
- **Proton motive force (PMF)** (label)
- **Membrane potential (Δψ)** (label)
- **ΔpH (pHi − pHo)** (label)

### Transporters / complexes (genes/proteins)
- **Na+/H+ antiporters** (GO:0015385 sodium:proton antiporter activity) including:
  - **NhaA-like** antiporter (label) (terradot2024escherichiacolimaintains pages 8-9)
  - **NhaB-like** antiporter (label) (terradot2024escherichiacolimaintains pages 8-9)
  - **PhaGF, MnhG, MrpF, YufB** (gene-family labels as in Ramoneda; treat as candidate markers) (ramoneda2023buildingagenomebased pages 3-5)
- **K+/H+ antiporters** (GO:0015386 potassium:proton antiporter activity) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **ClcA-like antiporter** (chloride/proton antiporter; label) (terradot2024escherichiacolimaintains pages 8-9)
- **Mrp-type cation/proton antiporter complex** (multi-subunit antiporter; label; often linked to alkaliphile/halophile stress) (jong2023membraneproteomeof pages 1-2)
  - **MrpA subunit histidine-switch** (mechanistic subnode; label) (jong2023membraneproteomeof pages 1-2)

### Energy metabolism modules
- **Proton-pumping respiratory chain components** (GO:0006119 oxidative phosphorylation; GO:0015992 proton transport) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **F0F1-ATP synthase / ATPase** (GO:0046933 proton-transporting ATP synthase complex) (poolman2023physicochemicalhomeostasisin pages 1-2, jong2023membraneproteomeof pages 1-2)
- **Metabolite decarboxylation pathways** (label; contributes to PMF) (poolman2023physicochemicalhomeostasisin pages 1-2)

### Chemicals / buffering and osmolytes
- **Inorganic/organic phosphates** (CHEBI:26078 phosphate; label “organic phosphate pool”) (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Proton (H+)** (CHEBI:15378) and **sodium (Na+)** (CHEBI:29101), **potassium (K+)** (CHEBI:29103)
- **Ectoine** (CHEBI:17634) and **glycine betaine** (CHEBI:17750) (candidate supportive osmolytes; uncertain for mid2 optimum) (jong2023membraneproteomeof pages 1-2)

### Environmental / assay factors
- **External pH (pHo)** (ENVO term unclear; use label)
- **Oxygen availability / respiratory vs fermentative regime** (label; affects PMF and proton export) (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)
- **Ionic composition (Na+/K+ availability), ionic strength, buffer system** (labels; experimental determinants) (terradot2024escherichiacolimaintains pages 2-3, poolman2023physicochemicalhomeostasisin pages 1-2)

---

## Candidate evidence-backed causal edges (curation table)
The following table is intended to be directly mined into `data/traits/environment/ph_optimum_mid2.yaml` as candidate edges, with uncertainty flags as noted.

| Edge (Subject—predicate—Object) | Node type(s) | Ontology grounding suggestions | Evidence (short quote/snippet) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Cytoplasmic buffering capacity — stabilizes — intracellular pH (pHi) | process, chemical, phenotype | GO:0006885?; CHEBI:26078 phosphate; label: intracellular pH homeostasis | “The buffering capacity of the cytoplasm is important in absorbing pH fluctuations… the number of free protons at pH 7.2 is only about 10… if there would not be sufficient buffering capacity” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | Broad bacterial mechanism; strong support for pHi stability, indirect support for best growth near external pH 7–8 where near-neutral pHi is maintained (poolman2023physicochemicalhomeostasisin pages 1-2) |
| External pH — determines magnitude of — ΔpH contribution to PMF | environment, process | ENVO:environmental material (label only); GO:0006754 ATP biosynthetic process; label: proton motive force | “Since cells maintain their cytoplasmic pH around neutral, the magnitude of the pH gradient is largely determined by the external pH” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | Core scope edge for trait definition; implies pH optimum is assay/environment dependent; not a gene-specific mechanism (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Na+/H+ antiporters — acidify cytoplasm when pHi is too high — intracellular pH homeostasis | protein/transporter, process | GO:0015385 sodium:proton antiporter activity; CHEBI:29101 sodium(1+); CHEBI:15378 hydrogen ion; label: NhaA/NhaB/Mrp/Pha/Mnh family | “Proton-sensing ion/H+ antiporters acidify the cytoplasm by exporting K+ or Na+ in exchange for protons when the internal pH gets too high” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | General mechanism spanning neutrophiles and alkalitolerant taxa; highly relevant to pH optimum mid2 because external pH 7–8 can push pHi upward unless compensated (poolman2023physicochemicalhomeostasisin pages 1-2) |
| K+/H+ antiporters — regulate — internal pH | protein/transporter, process | GO:0015386 potassium:proton antiporter activity; CHEBI:29103 potassium(1+); CHEBI:15378 hydrogen ion | “Key regulators of bacterial pH homeostasis are Na+/H+ and K+/H+ antiporters” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | Mechanistically credible but less specific than Na+/H+ systems for pH 7–8; curate as general regulator node/edge (poolman2023physicochemicalhomeostasisin pages 1-2) |
| Proton-pumping respiratory chain components — prevent — internal pH from becoming too low | pathway/protein complex, process | GO:0015992 proton transport; GO:0006119 oxidative phosphorylation; label: respiratory proton-pumping ETC | “Upregulation and or activation of the components of proton-pumping respiratory chains… prevent the internal pH from becoming too low” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | Broad statement across respiratory bacteria; directionality reflects low-pHi correction, so relevance to mid2 optimum is homeostatic balancing rather than alkaline adaptation alone (poolman2023physicochemicalhomeostasisin pages 1-2) |
| F0F1-ATPase — contributes to — intracellular pH regulation | protein complex, process | GO:0046933 proton-transporting ATP synthase complex; EC:7.1.2.2 | “the F1Fo ATP synthase… harness[es] both a proton or sodium gradient alongside membrane potential to regenerate ATP… it is also thought to regulate cytoplasmic pH” | 10.3389/fmicb.2023.1228266, 2023, https://doi.org/10.3389/fmicb.2023.1228266 | de Jong provides direct statement for pH regulation role; alkaliphile-focused, but mechanism broadly relevant. Distinguish from Poolman statement on fermentative bacteria using F0F1-ATPase in pH homeostasis (jong2023membraneproteomeof pages 1-2, poolman2023physicochemicalhomeostasisin pages 1-2) |
| Metabolite decarboxylation pathways — generate — proton motive force (PMF) | pathway, process | GO:0016831 carboxy-lyase activity; label: amino-acid/metabolite decarboxylation pathway; label: PMF | “the free energy change from decarboxylation reactions can be stored in the form of a proton motive force” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | Strong mechanistic edge; general, not specific to one taxon. Useful for graph if representing auxiliary pH-homeostasis modules (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin media 9ecadea6) |
| Proton motive force (PMF) — powers — F0F1-ATP synthase ATP synthesis | process, protein complex | GO:0046933 proton-transporting ATP synthase complex; GO:0006754 ATP biosynthetic process | “the proton motive force… subsequently can be used by F0F1-ATP synthase to make ATP” | 10.1093/femsre/fuad033, 2023, https://doi.org/10.1093/femsre/fuad033 | Strong bioenergetic edge; trait relevance is indirect but important because energetic feasibility constrains growth optimum (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin media 9ecadea6) |
| PMF magnitude — determines robustness/range of — pHi homeostasis across external pH values | process, phenotype, environment | label: proton motive force; label: intracellular pH homeostasis; label: external pH range | “the absolute magnitude of PMF sets the extracellular pH range over which cells can maintain near-neutral pHi” | 10.1103/PRXLife.2.043015, 2024, https://doi.org/10.1103/PRXLife.2.043015 | Central causal edge for trait optimum; based on E. coli model + experiments, so broadly informative but still somewhat model-system dependent (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) |
| NhaB-like antiporter — minimizes homeostatic cost / functions optimally — at external pH ~5–9 | gene/protein/transporter, environment | label: NhaB; GO:0015385 sodium:proton antiporter activity | “cells should use… the NhaB-like antiporter between 5 and 9” | 10.1103/PRXLife.2.043015, 2024, https://doi.org/10.1103/PRXLife.2.043015 | Particularly relevant to pH optimum mid2 because 7–8 lies inside the predicted NhaB-dominant window; model-driven, E. coli-centric, so mark moderate confidence for broad curation (terradot2024escherichiacolimaintains pages 8-9) |
| NhaA activity — increases above — external pH 6.5 | gene/protein/transporter, environment | label: NhaA; GO:0015385 sodium:proton antiporter activity | “NhaA… [is] important at acidic pH and NhaA in alkaline pH… with its activity increasing once pHe goes above 6.5” | 10.1103/PRXLife.2.043015, 2024, https://doi.org/10.1103/PRXLife.2.043015 | Useful threshold edge spanning the 7–8 window; still from E. coli-based analysis, so likely not universal quantitative cutoff across taxa (terradot2024escherichiacolimaintains pages 8-9) |
| Proton-ion antiporters — generate/maintain — membrane potential (Δψ) and PMF | transporter, process | label: proton-ion antiporter; label: membrane potential; label: proton motive force | “we predict that proton antiporters generate the cell’s out-of-equilibrium membrane potential… the PMF… powers these antiporters, is necessary to maintain ΔpH and ψ” | 10.1103/PRXLife.2.043015, 2024, https://doi.org/10.1103/PRXLife.2.043015 | Strong systems-level edge; shifts emphasis from simple proton pumping to antiporter stoichiometry. Good mechanistic graph backbone for pH optimum (terradot2024escherichiacolimaintains pages 8-9, terradot2024escherichiacolimaintains pages 4-5) |
| Na+/H+ antiporter families (PhaGF/MnhG/MrpF/YufB) — are associated with — preference for higher external pH | gene family, phenotype/environment | label: PhaGF; label: MnhG; label: MrpF; label: YufB; GO:0015385 sodium:proton antiporter activity | “Na+/H+ antiporters [PhaGF, MnhG, MrpF, and YufB]… were overrepresented in taxa with preferences for higher pH” | 10.1126/sciadv.adf8998, 2023, https://doi.org/10.1126/sciadv.adf8998 | Association study, not direct causation; valuable candidate-edge evidence for curation but should be marked inferred/population-genomic (ramoneda2023buildingagenomebased pages 3-5) |
| ATPases, cation/anion transporters, acidic/alkaline phosphatases — are associated with — bacterial pH preference | pathway/gene-function class, phenotype | GO:0015992 proton transport; GO transporter terms; GO phosphatase terms | “56 gene types… encoded for proteins known for their involvement in pH tolerance such as ATPases, anion and cation transporters and antiporters, and alkaline and acidic phosphatases” | 10.1126/sciadv.adf8998, 2023, https://doi.org/10.1126/sciadv.adf8998 | High-level association only; too broad for direct TraitMech edge unless decomposed into specific functions (ramoneda2023buildingagenomebased pages 3-5) |
| Mrp-type cation/proton antiporter — is essential for growth under — halophilic/alkaliphilic stress conditions | protein complex, phenotype/environment | label: Mrp antiporter complex; GO:0015385 sodium:proton antiporter activity | “Mrp-type antiporters are essential for growth of a variety of halophilic and alkaliphilic bacteria under stress conditions” | 10.1038/s41467-022-33640-y, 2022, https://doi.org/10.1038/s41467-022-33640-y | Strong structural/mechanistic support, but evidence is about stress growth in halo/alkaliphiles, not specifically optimum 7–8. Curate with taxon/context note (jong2023membraneproteomeof pages 1-2) |
| Histidine-switch mechanism in MrpA — drives — proton transfer coupled to Na+ translocation | protein subunit/mechanism, process | label: MrpA; CHEBI:15378 hydrogen ion; CHEBI:29101 sodium(1+) | “switching the position of a histidine residue between three hydrated pathways in the MrpA subunit is critical for proton transfer that drives gated transmembrane sodium translocation” | 10.1038/s41467-022-33640-y, 2022, https://doi.org/10.1038/s41467-022-33640-y | Detailed mechanistic sub-edge for Mrp node; useful only if graph supports subunit-level mechanism. Not specific to mid2 optimum (jong2023membraneproteomeof pages 1-2) |
| Ectoine transporter / glycine betaine transporter — may assist in maintaining — near-neutral internal pH at alkaline external pH | transporter, chemical, process | CHEBI:17634 ectoine; CHEBI:17750 glycine betaine; GO:0015188? compatible solute transmembrane transporter activity (label if uncertain) | “transporters for ectoine and glycine betaine… may assist in maintaining a near neutral internal pH when the external pH is highly alkaline” | 10.3389/fmicb.2023.1228266, 2023, https://doi.org/10.3389/fmicb.2023.1228266 | Explicitly tentative (“may assist”); alkaliphile-specific and indirect. Keep as uncertain candidate, not core edge for pH optimum mid2 (jong2023membraneproteomeof pages 1-2) |
| Inverted pH gradient / proton scarcity at high external pH — selects for — proton leakage prevention by membrane adaptation | environment, process, cellular component | label: inverted pH gradient; GO:0015886? ion transmembrane transport; GO:0016020 membrane | “With alkaliphiles, the defining environmental pressure is a lack of environmental proton availability… the membrane is theoretically very sensitive to leakage, so it must prevent the loss of protons” | 10.3389/fmicb.2023.1228266, 2023, https://doi.org/10.3389/fmicb.2023.1228266 | Relevant mainly to stronger alkaliphily than mid2; useful boundary-case mechanism but should be flagged as extrapolative for pH 7–8 optimum (jong2023membraneproteomeof pages 1-2) |


*Table: This table lists curation-ready causal edges for the microbial trait pH optimum mid2, linking transporters, buffering, PMF, and related modules to growth at external pH ~7–8. It prioritizes evidence-backed mechanisms from recent and authoritative sources, while flagging inferred or taxon-specific claims.*

---

## Warnings / claims not yet ready for strong curation
1. **Genome–trait associations are not causation.** Ramoneda et al. provide strong evidence that certain transporter gene families correlate with higher pH preference across environments, but this should be curated as **inferred/associational** unless supported by mechanistic knockout/physiology data in relevant taxa. (ramoneda2023buildingagenomebased pages 3-5)
2. **Alkaliphile-specific mechanisms may not generalize to pH 7–8 optima.** Mechanisms like “inverted pH gradient” and compatible-solute support for near-neutral pHi are most directly evidenced for strong alkaliphiles; use as boundary-case nodes/edges and mark uncertain for mid2. (jong2023membraneproteomeof pages 1-2)
3. **Model-system quantitative thresholds.** Terradot et al.’s pHe regime boundaries (e.g., NhaA increasing above pHe ~6.5) are grounded in *E. coli* modeling/measurements and may not be universal constants across taxa. Curate as *E. coli*-supported quantitative guidance. (terradot2024escherichiacolimaintains pages 8-9)

---

## DOI-first bibliography (with URLs and publication dates when available)
1. **Poolman B.** *Physicochemical homeostasis in bacteria.* **FEMS Microbiology Reviews**. Advance access publication date **19 Jun 2023**. DOI: **10.1093/femsre/fuad033**. URL: https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2)
2. **Ramoneda J, et al.** *Building a genome-based understanding of bacterial pH preferences.* **Science Advances**. **28 Apr 2023**. DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5)
3. **Terradot G, et al.** *Escherichia coli maintains pH via the membrane potential.* **PRX Life**. **Nov 2024**. DOI: **10.1103/PRXLife.2.043015**. URL: https://doi.org/10.1103/prxlife.2.043015 (terradot2024escherichiacolimaintains pages 8-9)
4. **de Jong SI, et al.** *Membrane proteome of the thermoalkaliphile Caldalkalibacillus thermarum TA2.A1.* **Frontiers in Microbiology**. Published **28 Jul 2023**. DOI: **10.3389/fmicb.2023.1228266**. URL: https://doi.org/10.3389/fmicb.2023.1228266 (jong2023membraneproteomeof pages 1-2)
5. **Lee Y, et al.** *Ion transfer mechanisms in Mrp-type antiporters from high resolution cryoEM and molecular dynamics simulations.* **Nature Communications**. **Jan 2022**. DOI: **10.1038/s41467-022-33640-y**. URL: https://doi.org/10.1038/s41467-022-33640-y (jong2023membraneproteomeof pages 1-2)


References

1. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

3. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

4. (jong2023membraneproteomeof pages 1-2): Samuel I. de Jong, Dimitry Y. Sorokin, Mark C. M. van Loosdrecht, Martin Pabst, and Duncan G. G. McMillan. Membrane proteome of the thermoalkaliphile caldalkalibacillus thermarum ta2.a1. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1228266, doi:10.3389/fmicb.2023.1228266. This article has 5 citations and is from a peer-reviewed journal.

5. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

6. (terradot2024escherichiacolimaintains pages 4-5): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

7. (poolman2023physicochemicalhomeostasisin media 9ecadea6): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

8. (terradot2024escherichiacolimaintains pages 2-3): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.