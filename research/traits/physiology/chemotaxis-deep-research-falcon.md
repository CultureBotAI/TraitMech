---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:10:33.174227'
end_time: '2026-06-18T11:25:38.376285'
duration_seconds: 905.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemotaxis
  trait_identifier: traitmech:000086
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemotaxis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A behavioral physiology in which cells bias their movement toward attractants
    or away from repellents by modulating flagellar motor switching in response to
    chemical gradients.
  parent_traits: METPO:1000059
  synonyms: chemotactic
  evidence_summary: 'DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis
    as gradient-guided movement controlled by a histidine-aspartate phosphorelay.)
    | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing
    in complex chemotaxis pathways.)'
  causal_graph_summary: 'chemotaxis_gradient_response: 3 nodes, 2 edges'
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
- **Trait label:** chemotaxis
- **METPO identifier:** traitmech:000086
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A behavioral physiology in which cells bias their movement toward attractants or away from repellents by modulating flagellar motor switching in response to chemical gradients.
- **Parent traits:** METPO:1000059
- **Synonyms:** chemotactic
- **Existing evidence:** DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis as gradient-guided movement controlled by a histidine-aspartate phosphorelay.) | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing in complex chemotaxis pathways.)
- **Existing causal graph summary:** chemotaxis_gradient_response: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **chemotaxis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotaxis.yaml`.

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
- **Trait label:** chemotaxis
- **METPO identifier:** traitmech:000086
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A behavioral physiology in which cells bias their movement toward attractants or away from repellents by modulating flagellar motor switching in response to chemical gradients.
- **Parent traits:** METPO:1000059
- **Synonyms:** chemotactic
- **Existing evidence:** DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis as gradient-guided movement controlled by a histidine-aspartate phosphorelay.) | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing in complex chemotaxis pathways.)
- **Existing causal graph summary:** chemotaxis_gradient_response: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **chemotaxis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotaxis.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Chemotaxis (traitmech:000086)

## 0. Executive scope summary
**Chemotaxis** (METPO traitmech:000086) is a behavioral physiology in which cells **bias their movement** toward attractants or away from repellents by **modulating flagellar motor switching** (classically through the CheA→CheY phosphorelay acting on the motor). In the canonical enteric paradigm, chemical sensing by chemoreceptors (MCPs) changes CheA autokinase activity, which changes CheY phosphorylation, which changes motor rotational bias and thus run/tumble statistics. Chemotaxis is distinct from **motility per se** (movement without gradient bias), and from non-chemical taxis modalities (e.g., phototaxis) unless explicitly grounded as chemical-gradient driven. Chemotaxis-like pathways can also control **type IV pili/gliding** in some taxa, but this TraitMech entry should prioritize **flagella-based** chemotaxis consistent with the provided definition and review framing. (muok2024unpackingalternativefeatures pages 2-4, wheeler2024individualbacterialcells pages 8-9)

## 1. Key concepts & current understanding (mechanistic definition)
### 1.1 Canonical information-processing architecture
Chemotaxis is commonly implemented by a chemosensory pathway in which **chemoreceptors (MCPs)** detect extracellular chemicals via ligand-binding domains and transmit conformational signals through **TM/HAMP** regions to a cytoplasmic **protein interaction region (PIR)** that interfaces with a receptor–kinase array. In *E. coli*, “**Upon effector binding to the receptor, a signal is transduced down to the histidine kinase CheA**” and “**The autophosphorylation activity of CheA is modulated by chemoreceptors**”. (muok2024unpackingalternativefeatures pages 2-4)

The central kinase **CheA** is a multi-domain histidine kinase. Muok et al. (2024) specify: “**CheA is composed of five domains (P1–P5)**… P1… histidine substrate residue… P2 binds… CheY and CheB… P4… uses ATP to phosphorylate P1, and **P5 binds receptors and CheW**.” (muok2024unpackingalternativefeatures pages 2-4)

### 1.2 Motor output and behavioral bias
Downstream, phosphorylated CheA transfers phosphoryl groups to response regulators: “**When CheA is phosphorylated, it can activate its response regulators, CheB and CheY, via phosphoryl transfer**.” (muok2024unpackingalternativefeatures pages 2-4)

Motor control is achieved through CheY phosphorylation state. In the canonical model: “**CheY-P interacts with the flagella to induce clockwise rotation**,” and the pool is reset because “**CheZ… dephosphorylates CheY**.” (muok2024unpackingalternativefeatures pages 2-4)

### 1.3 Adaptation (memory) and robustness
Chemotaxis includes sensory adaptation to allow cells to respond to changes rather than absolute concentration. In the canonical pathway, “**CheB, along with CheR… constitutes an adaptation system that reversibly methylates receptors**.” (muok2024unpackingalternativefeatures pages 2-4) 

Mechanistic variants exist. For example, in *Bacillus subtilis*, Muok et al. describe a CheV-mediated feedback: “**CheV… is phosphorylated by CheA and, as CheV-P, inhibits CheA activity**.” (muok2024unpackingalternativefeatures pages 13-15) This is taxon-specific and should be curated with explicit organismal context.

### 1.4 Structural basis: chemosensory arrays and core signaling units (CSUs)
Chemotaxis signaling is organized into higher-order arrays. Muok et al. define the smallest functional unit: “**The CSU consists of one CheA dimer, two CheW proteins, and two receptor ToDs**.” (muok2024unpackingalternativefeatures pages 2-4)

Cassidy et al. (2023) provide high-resolution *in situ* structural support for the CSU and its stoichiometry: “**CSUs comprise transmembrane chemoreceptors… a CheA histidine kinase dimer, and CheW adaptor proteins; six receptor dimers form two trimers-of-dimers organized around one CheA dimer and two CheW**.” (cassidy2023structureofthe pages 1-2)

### 1.5 Diversity and boundary cases
Chemotaxis systems are conserved yet diverse in composition and architecture across prokaryotes. A large-scale survey emphasizes the organizational role of CheW/CheV scaffolds and multiple “chemotaxis system categories.” (vass2023analysisofchew‐like pages 1-3)

Boundary-case behavior: Wheeler et al. (2024) show that **surface-tethered twitching chemotaxis** can use **spatial sensing** across the cell body, contrasting with temporal sensing in swimming bacteria; they report that correct reversals can outnumber incorrect ones by “**approximately tenfold**” under decreasing concentration and “**approximately fourfold**” under increasing concentration in alternating gradients. (wheeler2024individualbacterialcells pages 8-9) This is important for ontology scoping: it is chemotaxis behavior, but not flagellar motor switching.

## 2. Recent developments (2023–2024 priority)
### 2.1 Structural biology of intact arrays (cryo-ET + modeling)
Cassidy et al. (mBio, 2023) resolved the complete *E. coli* CSU from lysed cells by cryo-electron tomography and subtomogram averaging (~12 Å reported in the abstract), providing structural constraints on how receptor arrays couple to CheA and CheW and enabling mechanistic hypotheses about CheA domain interactions in intact assemblies. (cassidy2023structureofthe pages 1-2)

### 2.2 Expanding catalog of non-canonical system features
Muok et al. (Annual Review of Microbiology, 2024) synthesize “alternative features” beyond the *E. coli* paradigm, including differences in array baseplate symmetry and additional components (e.g., CheV, ParP) in some taxa, as well as non-canonical CheA architectures (e.g., missing P2 in many homologs). (muok2024unpackingalternativefeatures pages 2-4, muok2024unpackingalternativefeatures pages 13-15)

### 2.3 Chemorepulsion and receptor diversity statistics
Fu & Feng (Microorganisms, 2024) highlight that while chemoattraction is well studied, mechanisms of chemorepulsion remain less resolved, and they quantify receptor-domain diversity: among **26,530 MCP sequences**, **15,872** had known LBDs and **10,658** unknown; dominant LBD families included **Cache (33%)** and **4HB (31%)**. (fu2024decipheringbacterialchemorepulsion pages 3-4)

## 3. Current applications & real-world implementations (with recent data)
### 3.1 Microfluidics as a real-world implementation for chemotaxis quantification
Stehnach et al. (Bio-protocol, published **2024-09-05**) describe a **multiplexed chemotaxis device (MCD)** for “**efficient, high-throughput, and high-resolution chemotaxis screening**,” performing “**six stop-flow diffusion assays simultaneously**” and producing “**five logarithmically diluted chemostimulant solutions (plus a control)**” via an on-chip serial dilution layer. (stehnach2024multiplexedmicrofluidicplatform pages 1-4)

This platform is explicitly positioned to disentangle how chemicals/concentrations mediate processes relevant to “ecosystem function, human health, and disease,” indicating broad translational utility in environmental microbiology and infection biology. (stehnach2024multiplexedmicrofluidicplatform pages 1-4)

### 3.2 Gut-like porous environments: quorum-signal gradients as chemoattractants
Scheidweiler et al. (Nature Communications, **2024-01**) used microfluidic porous media mimicking gut structure and found that “**production of AI-2 and its accumulation within DEPs promote chemotactic migration towards and cells accumulation within the DEPs**,” with dependence on chemotaxis and signaling capacity (ΔluxS, ΔcheA, and Δtsr controls). (scheidweiler2024spatialstructurechemotaxis pages 7-8)

Quantitative/statistical evidence: In Figure 5, they quantify AI-2 reporter activity differences between pore classes using “**repeated measures ANOVA, p < 0.0001**,” with “**n = 230**” pores (averages over pores; SD bars). (scheidweiler2024spatialstructurechemotaxis media bf440b44, scheidweiler2024spatialstructurechemotaxis media 674a50af, scheidweiler2024spatialstructurechemotaxis media 1ab7e4ad)

### 3.3 Infection and biofilm initiation: chemotaxis signaling tunes flagellar bias
Liu et al. (mBio, **2024-06**) connect chemotaxis signaling components to biofilm initiation in *Helicobacter pylori*. They describe canonical entities (chemoreceptors, CheW, CheA, CheY) and identify that chemotaxis mutants shift **flagellar rotational bias**, which correlates with biofilm initiation: CCW-biased mutants (e.g., ΔcheA, ΔcheW, ΔcheV1) promote initiation; CW-biased mutants (e.g., ΔcheZ, ΔchePep, ΔcheV3) inhibit it; a CCW-locked flagellum can induce biofilm formation “independent of the chemotaxis system,” implicating motor-bias as a proximate driver. (liu2024counterclockwiserotationof pages 1-2)

### 3.4 Surface colonization and polymicrobial ecology (boundary-case)
Wheeler et al. (Nature Microbiology, **2024-09**) provide evidence that *Pseudomonas aeruginosa* twitching chemotaxis on surfaces can use **spatial sensing** across the cell body, challenging the “widely held notion” that bacteria are too small to sense gradients spatially for chemotaxis on surfaces, and providing quantitative reversal asymmetries under alternating gradients (∼10× vs ∼4×). (wheeler2024individualbacterialcells pages 8-9)

## 4. Candidate nodes for TraitMech chemotaxis causal graph (grouped)

### 4.1 Biological processes / functions
- Chemotaxis (GO:0006935)
- Flagellar rotation (GO:0001539)
- Two-component signal transduction (GO:0000160; pathway-level)
- Protein histidine kinase activity (GO:0000155; CheA function)
- Response regulator activity (CheY-like; GO:0000156)
- Protein phosphorylation / phosphotransfer (GO:0018106 candidate)
- Dephosphorylation (GO:0016311)

### 4.2 Proteins / genes (canonical)
- MCP chemoreceptors (Tar, Tsr, Trg, Tap, Aer in *E. coli* model context) (labels; organism-specific) (muok2024unpackingalternativefeatures pages 2-4)
- CheA (histidine kinase; multi-domain P1–P5) (muok2024unpackingalternativefeatures pages 2-4)
- CheW (coupling/scaffold) (muok2024unpackingalternativefeatures pages 2-4, cassidy2023structureofthe pages 1-2)
- CheY (motor-control response regulator) (muok2024unpackingalternativefeatures pages 2-4)
- CheZ (CheY-P phosphatase in canonical enteric systems) (muok2024unpackingalternativefeatures pages 2-4)
- CheR (receptor methyltransferase) (muok2024unpackingalternativefeatures pages 2-4)
- CheB (receptor methylesterase/deamidase; phospho-regulated) (muok2024unpackingalternativefeatures pages 2-4)

### 4.3 Complexes / cellular structures
- Chemosensory array
- Core signaling unit (CSU): 1 CheA dimer + 2 CheW + receptor trimers-of-dimers (muok2024unpackingalternativefeatures pages 2-4, cassidy2023structureofthe pages 1-2)
- Flagellar motor / baseplate (node label; downstream target of CheY-P) (muok2024unpackingalternativefeatures pages 2-4)

### 4.4 Chemicals / chemoeffectors
- Attractants/repellents (label nodes; chemical identity assay-specific)
- Autoinducer-2 (AI-2) (CHEBI label-only; quorum sensing molecule acting as chemoattractant cue in porous media) (scheidweiler2024spatialstructurechemotaxis pages 7-8)

### 4.5 Environmental / experimental factors (ENVO label suggestions)
- Chemical gradient (environmental condition)
- Porous media microhabitats: transmitting pores (TPs) vs dead-end pores (DEPs) (scheidweiler2024spatialstructurechemotaxis pages 7-8)
- Flow/laminar regime (experimental factor) (scheidweiler2024spatialstructurechemotaxis pages 7-8)
- Microfluidic device / stop-flow diffusion assay (experimental factor) (stehnach2024multiplexedmicrofluidicplatform pages 1-4)

## 5. Evidence-backed candidate causal edges (curation table)
The table below is designed to be directly translatable into `data/traits/physiology/chemotaxis.yaml` as candidate nodes/edges (with uncertainty notes where relevant).

| Edge (subject–predicate–object) | Node types | Suggested CURIEs | Evidence snippet/quote | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Chemoreceptor ligand binding–positively or negatively modulates–CheA autophosphorylation | protein/chemical/process | chemoreceptor/MCP: GO:0004888 candidate; CheA: GO:0000155; autophosphorylation: GO:0046777 | “Upon effector binding to the receptor, a signal is transduced down to the histidine kinase CheA… The autophosphorylation activity of CheA is modulated by chemoreceptors” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Canonical flagellar chemotaxis; sign depends on attractant/repellent and receptor/system. |
| Repellent recognition by chemoreceptors–activates–CheA autokinase activity | chemical/protein/process | repellent: CHEBI label-only; CheA: GO:0000155 | “In E. coli, recognition of a repellent by receptors initiates CheA autokinase activity.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | E. coli-specific wording; opposite behavior for attractant increase in canonical enteric systems. |
| CheA–phosphorylates–CheY | protein/protein/process | CheA: GO:0000155; CheY: GO:0000156; phosphotransfer: GO:0018106 | “When CheA is phosphorylated, it can activate its response regulators, CheB and CheY, via phosphoryl transfer.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Core conserved phosphorelay. |
| CheY-P–induces–clockwise flagellar rotation | protein/process | CheY: GO:0000156; flagellar rotation: GO:0001539; chemotaxis: GO:0006935 | “CheY-P interacts with the flagella to induce clockwise rotation.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Canonical for peritrichous flagellar systems; motor outputs vary across taxa. |
| CheZ–dephosphorylates–CheY-P | protein/protein/process | CheZ: label-only; CheY: GO:0000156; dephosphorylation: GO:0016311 | “The phosphatase CheZ dephosphorylates CheY to ensure that a stable pool of CheY is available.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Canonical enteric paradigm; some taxa use CheC/CheX instead. |
| CheR–methylates–chemoreceptors/MCPs | protein/protein/process | CheR: EC 2.1.1.- candidate; receptor methylation: GO:0000160 | “CheB, along with CheR… constitutes an adaptation system that reversibly methylates receptors.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Receptor methylation sites and tethering differ across taxa. |
| CheB–demethylates/deamidates–chemoreceptors/MCPs | protein/protein/process | CheB: EC 3.1.1.61 candidate; receptor demethylation: GO:0000160 candidate | “CheB, along with CheR… constitutes an adaptation system that reversibly methylates receptors.”; “CheB (phospho-regulated methylesterase) removing them” (muok2024unpackingalternativefeatures pages 2-4, vass2023analysisofchew‐like pages 1-3) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 ; 10.1002/prot.26430, 2023, https://doi.org/10.1002/prot.26430 | Wording in review compresses methylation cycle; curate as adaptation/demethylation with caution. |
| CheA–phosphorylates–CheB | protein/protein/process | CheA: GO:0000155; CheB: label-only; phosphotransfer: GO:0018106 | “When CheA is phosphorylated, it can activate its response regulators, CheB and CheY, via phosphoryl transfer.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Important adaptation edge. |
| CheB phosphorylation–increases–CheB demethylation activity | protein/process/process | CheB: label-only; demethylation activity: label-only | “CheA-mediated phosphorylation of CheB increases its demethylation activity, forming two feedback loops that restore baseline kinase activity.” (soriano2023chemotaxisinpectobacterium pages 30-33) | Soriano thesis/dissertation, 2023, URL unavailable in provided context | Source is a thesis-like document with unclear journal metadata; useful but weaker for direct curation than DOI review sources. |
| CheW–couples/scaffolds–CheA with chemoreceptor PIR/baseplate | protein/protein complex/process | CheW: label-only; CheA: GO:0000155; MCP/PIR: label-only | “The coupling protein CheW secures the…” and “The baseplate of the protein complex consists of the chemoreceptor PIR, CheA, and CheW.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Structural/organizational edge rather than signal-flow edge. |
| Core signaling unit (CSU)–consists of–1 CheA dimer + 2 CheW + 2 receptor trimers-of-dimers | complex/protein complex | CSU: label-only; CheA: GO:0000155; CheW: label-only; MCP: label-only | “The CSU consists of one CheA dimer, two CheW proteins, and two receptor ToDs.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Structural stoichiometry from E. coli canonical array. |
| Core signaling unit (CSU)–composed of–transmembrane chemoreceptors + CheA dimer + CheW adaptors | complex/protein complex | CSU: label-only; CheA: GO:0000155; CheW: label-only; MCP: label-only | “CSUs comprise transmembrane chemoreceptors… a CheA histidine kinase dimer, and CheW adaptor proteins; six receptor dimers form two trimers-of-dimers organized around one CheA dimer and two CheW.” (cassidy2023structureofthe pages 1-2) | 10.1128/mbio.00793-23, 2023, https://doi.org/10.1128/mbio.00793-23 | High-value structural support from cryo-ET. |
| CheA P5–binds–receptors and CheW | protein/protein | CheA P5: label-only; CheW: label-only; receptor: label-only | “P5 binds receptors and CheW.” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Domain-level edge. |
| CheA P2–binds–CheY and CheB | protein/protein | CheA P2: label-only; CheY: GO:0000156; CheB: label-only | “The P2 domain binds its response regulators CheY and CheB” (muok2024unpackingalternativefeatures pages 2-4) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Domain-level edge. |
| CheV–is phosphorylated by–CheA | protein/protein/process | CheV: label-only; CheA: GO:0000155 | “In B. subtilis, CheV… is phosphorylated by CheA” (muok2024unpackingalternativefeatures pages 13-15) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Taxon-specific; not universal. |
| CheV-P–inhibits–CheA activity | protein/protein/process | CheV-P: label-only; CheA: GO:0000155 | “CheV… is phosphorylated by CheA and, as CheV-P, inhibits CheA activity, likely by disrupting receptor interactions.” (muok2024unpackingalternativefeatures pages 13-15) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | B. subtilis-specific; mechanism likely indirect. Mark uncertain/generalization-limited. |
| CheX–dephosphorylates–CheY-P | protein/protein/process | CheX: label-only; CheY: GO:0000156 | “CheX (in some species) is a stronger CheY-P phosphatase” (muok2024unpackingalternativefeatures pages 13-15) | 10.1146/annurev-micro-032421-110850, 2024, https://doi.org/10.1146/annurev-micro-032421-110850 | Alternative to CheZ in some taxa; taxon-specific. |
| AI-2 gradient–promotes–E. coli chemotactic accumulation in dead-end pores | chemical/environment/process | AI-2: CHEBI label-only; dead-end pore: ENVO label-only; chemotaxis: GO:0006935 | “We show that production of AI-2 and its accumulation within DEPs promote chemotactic migration towards and cells accumulation within the DEPs” (scheidweiler2024spatialstructurechemotaxis pages 7-8) | 10.1038/s41467-023-44267-y, 2024, https://doi.org/10.1038/s41467-023-44267-y | Application/context edge in porous microfluidic habitat; strain and flow dependent. |
| AI-2 production/sensing–is required for–pore-specific colonization in DEPs | process/protein/process | luxS/AI-2 synthase: label-only; tsr receptor: label-only; DEP: ENVO label-only | “This pore-specific colonization does not occur in a ΔluxS… mutant; therefore, this phenomenon depends on the ability of the WT strain to produce and sense AI-2 gradients.” (scheidweiler2024spatialstructurechemotaxis pages 7-8) | 10.1038/s41467-023-44267-y, 2024, https://doi.org/10.1038/s41467-023-44267-y | Combines production and sensing; receptor identity for AI-2 response linked here via Δtsr negative control in paper text. |
| cheA deletion–disrupts–AI-2-driven chemotactic accumulation in dead-end pores | gene/process/environment | cheA: label-only; DEP: ENVO label-only; chemotactic accumulation: label-only | “To conclusively claim that the observed E. coli accumulation in the DEP is due to the chemotactic activity toward the self-produced AI-2, we also consider the general non-chemotactic E. coli strain ΔcheA… Flow experiments… display similar results as… ΔluxS” (scheidweiler2024spatialstructurechemotaxis pages 7-8) | 10.1038/s41467-023-44267-y, 2024, https://doi.org/10.1038/s41467-023-44267-y | Negative-control inference from mutant phenotype; curate as loss-of-function evidence. |
| AI-2 reporter activity in DEPs–is greater than–in transmitting pores | process/environment/process | PlsrR activity: label-only; DEP/TP: ENVO label-only | “Quantification of the PlsrR activity… for E. coli WT… in TP, cyan, and DEP, red… (repeated measures ANOVA, p < 0.0001)… averages over all pores (n = 230)” (scheidweiler2024spatialstructurechemotaxis pages 7-8, scheidweiler2024spatialstructurechemotaxis media bf440b44) | 10.1038/s41467-023-44267-y, 2024, https://doi.org/10.1038/s41467-023-44267-y | Quantitative support for localized AI-2/QS conditions rather than direct trait-defining edge. |
| Chemotaxis signaling mutants with counterclockwise bias–promote–biofilm initiation in H. pylori | gene/process/process | cheA/cheW/cheV1: label-only; biofilm initiation: GO:0042710 candidate | “mutants with a counterclockwise (CCW) bias promoted biofilm initiation, e.g., ∆cheA, ∆cheW, or ∆cheV1” (liu2024counterclockwiserotationof pages 1-2) | 10.1128/mbio.00440-24, 2024, https://doi.org/10.1128/mbio.00440-24 | Downstream application edge; not a universal chemotaxis mechanism. |
| Chemotaxis signaling mutants with clockwise bias–inhibit–biofilm initiation in H. pylori | gene/process/process | cheZ/chePep/cheV3: label-only; biofilm initiation: GO:0042710 candidate | “those with a clockwise bias inhibited it, e.g., ∆cheZ, ∆chePep, or ∆cheV3.” (liu2024counterclockwiserotationof pages 1-2) | 10.1128/mbio.00440-24, 2024, https://doi.org/10.1128/mbio.00440-24 | H. pylori-specific phenotype. |
| Counterclockwise bias-locked flagellum–induces–biofilm formation independent of chemotaxis system | process/process/process | CCW flagellum: label-only; biofilm formation: GO:0042710 | “A CCW bias-locked flagellar mutant induced biofilm formation independent of the chemotaxis system” (liu2024counterclockwiserotationof pages 1-2) | 10.1128/mbio.00440-24, 2024, https://doi.org/10.1128/mbio.00440-24 | Indicates motor-bias output can be proximate cause downstream of chemotaxis. |
| Oxaloacetic acid–acts as chemoattractant for–Azospirillum brasilense | chemical/process/taxon | oxaloacetate: CHEBI:30797; chemotaxis: GO:0006935; Azospirillum brasilense: NCBITaxon:192 | “We found that oxaloacetic acid acts as a chemoattractant for Azospirillum brasilense.” (fu2024decipheringbacterialchemorepulsion pages 3-4) | 10.1007/s00248-024-02366-3, 2024, https://doi.org/10.1007/s00248-024-02366-3 | Do not curate from this artifact: no valid citeable context ID for direct quotation in final evidence chain. |
| Microfluidic multiplexed chemotaxis device–enables–six parallel stop-flow diffusion assays | assay/device/process | microfluidic chemotaxis device: label-only | “The MCD performs six stop-flow diffusion assays simultaneously on a single chip” (stehnach2024multiplexedmicrofluidicplatform pages 1-4) | 10.21769/bioprotoc.5062, 2024, https://doi.org/10.21769/BioProtoc.5062 | Assay/experimental-factor node rather than biological causal edge; useful for evidence metadata. |
| Multiplexed chemotaxis device serial dilution layer–produces–five logarithmically diluted chemostimulus concentrations plus control | device/process/chemical | chemostimulus: label-only | “a serial dilution layer… produces five logarithmically diluted chemostimulant solutions (plus a control)” (stehnach2024multiplexedmicrofluidicplatform pages 1-4) | 10.21769/bioprotoc.5062, 2024, https://doi.org/10.21769/BioProtoc.5062 | Experimental-factor edge for assay ontology, not trait mechanism. |


*Table: This table compiles candidate causal edges for a TraitMech chemotaxis graph, spanning the canonical CheA/CheY motor-control pathway, adaptation modules, structural organization of chemosensory arrays, and recent application-linked phenotypes. It is designed to support curation by pairing each proposed edge with grounded node suggestions, evidence snippets, source metadata, and uncertainty notes.*

## 6. Expert opinions / authoritative analysis (as stated in sources)
- Muok et al. (Annual Review of Microbiology, 2024) emphasize that *E. coli* is a model and that many bacteria possess “alternative features… demonstrating that these systems are likely more complex than previously assumed,” with divergence in “supramolecular architecture, sensory mechanisms, and protein composition.” (muok2024unpackingalternativefeatures pages 2-4, muok2024unpackingalternativefeatures pages 13-15)
- Cassidy et al. (mBio, 2023) frame CSU structural resolution as a key barrier to “a detailed mechanistic understanding of signal transduction,” positioning cryo-ET and integrative modeling as central to current progress. (cassidy2023structureofthe pages 1-2)
- Wheeler et al. (Nature Microbiology, 2024) argue that the established temporal-sensing paradigm does not generalize to surface-based movement in *P. aeruginosa*, implicating broader ecological relevance on surfaces where gradients are “strong and stable.” (wheeler2024individualbacterialcells pages 8-9)

## 7. Warnings / curation cautions
1. **Taxon specificity:** Some edges (e.g., CheV-P inhibition of CheA; specific array symmetries; absence/presence of CheZ vs CheX) are taxon- and system-category dependent and should be curated with organism/system qualifiers. (muok2024unpackingalternativefeatures pages 13-15, vass2023analysisofchew‐like pages 1-3)
2. **Behavioral modality mismatch:** Twitching chemotaxis and phototaxis-like systems can be “chemotaxis-like” but do not necessarily operate via **flagellar motor switching**; include only if the TraitMech graph is expanded beyond the METPO definition. (wheeler2024individualbacterialcells pages 8-9)
3. **Assay-dependence of chemoeffectors:** Chemical identities and valence (attractant vs repellent) are assay- and receptor-specific; represent as explicit nodes (e.g., AI-2) only when the evidence supports the behavior in context. (scheidweiler2024spatialstructurechemotaxis pages 7-8)
4. **Non-DOI evidence:** A subset of mechanistic claims may be supported by theses or non-peer-reviewed sources in the retrieved corpus; prioritize DOI peer-reviewed sources for curation. (soriano2023chemotaxisinpectobacterium pages 30-33)

## 8. DOI-first bibliography (with publication date and URL)
- Muok AR, Olsthoorn FA, Briegel A. **Unpacking Alternative Features of the Bacterial Chemotaxis System.** *Annual Review of Microbiology.* **2024-11**. DOI:10.1146/annurev-micro-032421-110850. https://doi.org/10.1146/annurev-micro-032421-110850 (muok2024unpackingalternativefeatures pages 2-4)
- Cassidy CK, Qin Z, Frosio T, et al. **Structure of the native chemotaxis core signaling unit from phage E-protein lysed *E. coli* cells.** *mBio.* **2023-10**. DOI:10.1128/mbio.00793-23. https://doi.org/10.1128/mbio.00793-23 (cassidy2023structureofthe pages 1-2)
- Fu R, Feng H. **Deciphering Bacterial Chemorepulsion: The Complex Response of Microbes to Environmental Stimuli.** *Microorganisms.* **2024-08**. DOI:10.3390/microorganisms12081706. https://doi.org/10.3390/microorganisms12081706 (fu2024decipheringbacterialchemorepulsion pages 3-4)
- Vass LR, Bourret RB, Foster CA. **Analysis of CheW-like domains provides insights into organization of prokaryotic chemotaxis systems.** *Proteins.* **2023-10**. DOI:10.1002/prot.26430. https://doi.org/10.1002/prot.26430 (vass2023analysisofchew‐like pages 1-3)
- Scheidweiler D, Bordoloi AD, Jiao W, et al. **Spatial structure, chemotaxis and quorum sensing shape bacterial biomass accumulation in complex porous media.** *Nature Communications.* **2024-01**. DOI:10.1038/s41467-023-44267-y. https://doi.org/10.1038/s41467-023-44267-y (scheidweiler2024spatialstructurechemotaxis pages 7-8)
- Stehnach MR, Henshaw RJ, Floge SA, Guasto JS. **Multiplexed Microfluidic Platform for Parallel Bacterial Chemotaxis Assays.** *Bio-protocol.* **2024-09-05**. DOI:10.21769/bioprotoc.5062. https://doi.org/10.21769/bioprotoc.5062 (stehnach2024multiplexedmicrofluidicplatform pages 1-4)
- Liu X, Lertsethtakarn P, Mariscal VT, Yildiz F, Ottemann KM. **Counterclockwise rotation of the flagellum promotes biofilm initiation in *Helicobacter pylori*.** *mBio.* **2024-06**. DOI:10.1128/mbio.00440-24. https://doi.org/10.1128/mbio.00440-24 (liu2024counterclockwiserotationof pages 1-2)
- Wheeler JHR, Foster KR, Durham WM. **Individual bacterial cells can use spatial sensing of chemical gradients to direct chemotaxis on surfaces.** *Nature Microbiology.* **2024-09**. DOI:10.1038/s41564-024-01729-3. https://doi.org/10.1038/s41564-024-01729-3 (wheeler2024individualbacterialcells pages 8-9)



References

1. (muok2024unpackingalternativefeatures pages 2-4): A.R. Muok, F.A. Olsthoorn, and A. Briegel. Unpacking alternative features of the bacterial chemotaxis system. Nov 2024. URL: https://doi.org/10.1146/annurev-micro-032421-110850, doi:10.1146/annurev-micro-032421-110850. This article has 6 citations and is from a peer-reviewed journal.

2. (wheeler2024individualbacterialcells pages 8-9): James H. R. Wheeler, Kevin R. Foster, and William M. Durham. Individual bacterial cells can use spatial sensing of chemical gradients to direct chemotaxis on surfaces. Nature Microbiology, 9:2308-2322, Sep 2024. URL: https://doi.org/10.1038/s41564-024-01729-3, doi:10.1038/s41564-024-01729-3. This article has 33 citations and is from a highest quality peer-reviewed journal.

3. (muok2024unpackingalternativefeatures pages 13-15): A.R. Muok, F.A. Olsthoorn, and A. Briegel. Unpacking alternative features of the bacterial chemotaxis system. Nov 2024. URL: https://doi.org/10.1146/annurev-micro-032421-110850, doi:10.1146/annurev-micro-032421-110850. This article has 6 citations and is from a peer-reviewed journal.

4. (cassidy2023structureofthe pages 1-2): C. Keith Cassidy, Zhuan Qin, Thomas Frosio, Khoosheh Gosink, Zhengyi Yang, Mark S. P. Sansom, Phillip J. Stansfeld, John S. Parkinson, and Peijun Zhang. Structure of the native chemotaxis core signaling unit from phage e-protein lysed <i>e. coli</i> cells. Oct 2023. URL: https://doi.org/10.1128/mbio.00793-23, doi:10.1128/mbio.00793-23. This article has 16 citations and is from a domain leading peer-reviewed journal.

5. (vass2023analysisofchew‐like pages 1-3): Luke R. Vass, Robert B. Bourret, and Clay A. Foster. Analysis of <scp>chew</scp>‐like domains provides insights into organization of prokaryotic chemotaxis systems. Proteins: Structure, Function, and Bioinformatics, 91:315-329, Oct 2023. URL: https://doi.org/10.1002/prot.26430, doi:10.1002/prot.26430. This article has 11 citations.

6. (fu2024decipheringbacterialchemorepulsion pages 3-4): Ruixin Fu and Haichao Feng. Deciphering bacterial chemorepulsion: the complex response of microbes to environmental stimuli. Microorganisms, 12:1706, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081706, doi:10.3390/microorganisms12081706. This article has 15 citations.

7. (stehnach2024multiplexedmicrofluidicplatform pages 1-4): Michael R. Stehnach, Richard J. Henshaw, Sheri A. Floge, and J. Guasto. Multiplexed microfluidic platform for parallel bacterial chemotaxis assays. Bio-protocol, Sep 2024. URL: https://doi.org/10.21769/bioprotoc.5062, doi:10.21769/bioprotoc.5062. This article has 2 citations and is from a peer-reviewed journal.

8. (scheidweiler2024spatialstructurechemotaxis pages 7-8): David Scheidweiler, Ankur Deep Bordoloi, Wenqiao Jiao, Vladimir Sentchilo, Monica Bollani, Audam Chhun, Philipp Engel, and Pietro de Anna. Spatial structure, chemotaxis and quorum sensing shape bacterial biomass accumulation in complex porous media. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44267-y, doi:10.1038/s41467-023-44267-y. This article has 65 citations and is from a highest quality peer-reviewed journal.

9. (scheidweiler2024spatialstructurechemotaxis media bf440b44): David Scheidweiler, Ankur Deep Bordoloi, Wenqiao Jiao, Vladimir Sentchilo, Monica Bollani, Audam Chhun, Philipp Engel, and Pietro de Anna. Spatial structure, chemotaxis and quorum sensing shape bacterial biomass accumulation in complex porous media. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44267-y, doi:10.1038/s41467-023-44267-y. This article has 65 citations and is from a highest quality peer-reviewed journal.

10. (scheidweiler2024spatialstructurechemotaxis media 674a50af): David Scheidweiler, Ankur Deep Bordoloi, Wenqiao Jiao, Vladimir Sentchilo, Monica Bollani, Audam Chhun, Philipp Engel, and Pietro de Anna. Spatial structure, chemotaxis and quorum sensing shape bacterial biomass accumulation in complex porous media. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44267-y, doi:10.1038/s41467-023-44267-y. This article has 65 citations and is from a highest quality peer-reviewed journal.

11. (scheidweiler2024spatialstructurechemotaxis media 1ab7e4ad): David Scheidweiler, Ankur Deep Bordoloi, Wenqiao Jiao, Vladimir Sentchilo, Monica Bollani, Audam Chhun, Philipp Engel, and Pietro de Anna. Spatial structure, chemotaxis and quorum sensing shape bacterial biomass accumulation in complex porous media. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-023-44267-y, doi:10.1038/s41467-023-44267-y. This article has 65 citations and is from a highest quality peer-reviewed journal.

12. (liu2024counterclockwiserotationof pages 1-2): Xiaolin Liu, Paphavee Lertsethtakarn, Vanessa T. Mariscal, Fitnat Yildiz, and Karen M. Ottemann. Counterclockwise rotation of the flagellum promotes biofilm initiation in <i>helicobacter pylori</i>. Jun 2024. URL: https://doi.org/10.1128/mbio.00440-24, doi:10.1128/mbio.00440-24. This article has 22 citations and is from a domain leading peer-reviewed journal.

13. (soriano2023chemotaxisinpectobacterium pages 30-33): F Velando Soriano. Chemotaxis in pectobacterium atrosepticum scri1043: functional and structural studies on chemotaxis adaptation proteins and chemoreceptors. Unknown journal, 2023.