---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:38:50.753432'
end_time: '2026-06-18T08:59:29.640432'
duration_seconds: 1238.89
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mycelial growth
  trait_identifier: traitmech:000074
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: mycelial_growth
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait in which a bacterium grows as branching, filamentous
    hyphae that form a mycelium, often with subsequent differentiation into aerial
    hyphae and spores, as in Streptomyces.
  parent_traits: METPO:1000059
  synonyms: mycelium-forming, hyphal growth
  evidence_summary: "DOI:10.1038/nrmicro1968:  (Fl\xE4rdh & Buttner describe Streptomyces\
    \ growth as a branching hyphal mycelium with subsequent morphological differentiation.)\
    \ | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth\
    \ as a bacterial solution to multicellularity.)"
  causal_graph_summary: 'mycelial_branching_hyphal_growth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mycelial growth
- **METPO identifier:** traitmech:000074
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a bacterium grows as branching, filamentous hyphae that form a mycelium, often with subsequent differentiation into aerial hyphae and spores, as in Streptomyces.
- **Parent traits:** METPO:1000059
- **Synonyms:** mycelium-forming, hyphal growth
- **Existing evidence:** DOI:10.1038/nrmicro1968:  (Flärdh & Buttner describe Streptomyces growth as a branching hyphal mycelium with subsequent morphological differentiation.) | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth as a bacterial solution to multicellularity.)
- **Existing causal graph summary:** mycelial_branching_hyphal_growth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mycelial growth** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/mycelial_growth.yaml`.

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
- **Trait label:** mycelial growth
- **METPO identifier:** traitmech:000074
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a bacterium grows as branching, filamentous hyphae that form a mycelium, often with subsequent differentiation into aerial hyphae and spores, as in Streptomyces.
- **Parent traits:** METPO:1000059
- **Synonyms:** mycelium-forming, hyphal growth
- **Existing evidence:** DOI:10.1038/nrmicro1968:  (Flärdh & Buttner describe Streptomyces growth as a branching hyphal mycelium with subsequent morphological differentiation.) | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth as a bacterial solution to multicellularity.)
- **Existing causal graph summary:** mycelial_branching_hyphal_growth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mycelial growth** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/mycelial_growth.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **Mycelial growth** (traitmech:000074)

## 1) Scope summary (trait meaning, boundaries)
**Mycelial growth** in bacteria (canonical in *Streptomyces* and related filamentous Actinobacteria) is a **morphology trait** defined by growth as **branching, filamentous hyphae** that collectively form a **multicellular mycelium**. Vegetative hyphae extend by **polar tip growth** and branch to generate a dense substrate network; development can proceed to **aerial hyphae** and then **sporulation** (chains of spores) (schlimpert2023thebestof pages 8-10, schlimpert2023thebestof pages 1-2, bhowmick2023osmoticstressresponses pages 1-2).

Key boundaries and near-trait distinctions:
- The trait is **not** merely “elongated cells” or transient filamentation due to division inhibition; rather it is a **developmental/multicellular growth mode** with **apical extension and branching** (bhowmick2023osmoticstressresponses pages 1-2, schlimpert2023thebestof pages 1-2).
- **Vegetative septation/cross-walls** can be infrequent and are **not required for viability**; e.g., deletion of **ftsZ** prevents cross-walls/sporulation septa but can still allow vegetative and aerial growth (reviewed in 2023) (schlimpert2023thebestof pages 8-10).
- **Pellet formation** in liquid culture (often used in industry) is a context-dependent aggregate phenotype and should be represented as an assay/context node rather than conflated with the core trait definition.

## 2) Key concepts and current mechanistic understanding (2023–2024 emphasis)
### 2.1 Polar tip growth and branching: the DivIVA-centered polarisome
A defining mechanism is **polar cell-wall growth at hyphal tips**, directed by **DivIVA** clusters (“polarisomes”). A 2023 authoritative review of *Streptomyces* model systems states that the **“DivIVA-polarisome drives the growth of both the branching vegetative hyphae and the non-branching aerial hyphae”** (schlimpert2023thebestof pages 8-10, schlimpert2023thebestof pages 1-2). Polarisome dynamics contribute to branching: **“Splitting of the polarisomes at growing tips gives rise to daughter polarisomes”** that coordinate new branch emergence (bhowmick2023osmoticstressresponses pages 1-2).

A key *recently emphasized control layer* is **post-translational regulation of DivIVA** under envelope stress. In a 2023 review focused on osmotic stress and c-di-AMP biology in *Streptomyces*, **AfsK** is described as phosphorylating DivIVA in response to cell-wall stressors (e.g., bacitracin/vancomycin), and **high DivIVA phosphorylation promotes polarisome disassembly and “hyperbranching”**; **SppA** counteracts by dephosphorylating DivIVA (bhowmick2023osmoticstressresponses pages 1-2).

### 2.2 Cell envelope biogenesis and morphogenesis: glycopolymers and peptidoglycan
A major 2024 advance is direct evidence that **cell-wall glycopolymer attachment to peptidoglycan** is required for proper hyphal shape and sporulation septation. In *S. venezuelae*, **CglA** (an LCP-LytR_C domain protein) is identified as a glycopolymer ligase that **“catalyzes attachment of wall teichoic acids (WTAs) to peptidoglycan”** (bhowmick2024cellshapeand pages 1-2). CglA localizes to **“hyphal tips and branching points”** (bhowmick2024cellshapeand pages 8-10) and loss of CglA causes enlarged/swollen hyphae and **failure of FtsZ ring formation/positioning** leading to misplaced septa and misshaped spores (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 5-8).

Visual support: the paper’s figures show **CglA localization at tips/branches** and **disruption of FtsZ “Z-ladders”** in the *cglA* mutant (bhowmick2024cellshapeand media 2038f321, bhowmick2024cellshapeand media faa1a359).

### 2.3 Sporulation septation in a mycelium: FtsZ Z-ladders and their regulation
During sporulation, aerial hyphae undergo synchronous septation. The sporulation-specific division mode involves **many regularly spaced division sites**, described in a 2024 synthesis as transforming division from one site to **“up to ~200 regularly spaced division sites”** along aerial hyphae, with **FtsZ** as the principal Z-ring scaffold (falguera2024stressresponsesaffectinga pages 16-22). In *Streptomyces*, this appears as a **“Z-ring ladder”** (falguera2024stressresponsesaffectinga pages 16-22).

A 2023 experimental study directly links **FtsZ phosphorylation state** to Z-ladder formation and spore morphology: phosphomimetic FtsZ alleles fail to show visible Z-ladders, and **septal spacing is increased**, producing **“significantly longer” spores** than wild type (yague2023ftszphosphorylationpleiotropically pages 8-10, yague2023ftszphosphorylationpleiotropically pages 10-13). This is highly curation-relevant but should be stored as allele/construct- and taxon-specific evidence.

### 2.4 Environmental control and second messengers: osmotic stress and c-di-AMP
Osmotic stress is a soil-relevant cue affecting mycelial patterning. A 2023 review reports that an **osmotic upshift arrests tip growth for ~2–3 h**, followed by resumption via **multiple lateral branches**, yielding a hyperbranching mycelium (bhowmick2023osmoticstressresponses pages 2-3). High salinity can suppress development: *S. venezuelae* **fails to raise aerial hyphae under high NaCl**, can still sporulate at **0.25 M NaCl**, but sporulation is essentially blocked at **0.5 M NaCl** (bhowmick2023osmoticstressresponses pages 2-3).

The same 2023 review emphasizes **c-di-AMP** as an osmotic homeostasis signal: c-di-AMP is **important for survival at high salinity** (bhowmick2023osmoticstressresponses pages 7-8). Perturbing c-di-AMP turnover impacts development: deletion of the c-di-AMP phosphodiesterase **ataC** (elevated c-di-AMP) causes severe aerial hyphae/sporulation defects (bhowmick2023osmoticstressresponses pages 6-7). A 2024 primary study connects cell-wall glycopolymer decoration with c-di-AMP physiology by reporting that **cglA deletion restores growth of a disA mutant under high salt**, implying functional coupling between wall decoration and osmotic signaling (bhowmick2024cellshapeand pages 1-2).

### 2.5 Emerging mechanisms (2024): membrane microdomains organizing tip growth under hyperosmotic stress
A 2024 Research Square preprint proposes that a **stomatin-like SPFH protein StlP** organizes a **tip membrane microdomain of increased fluidity** that confines apical synthesis and supports polar growth under hyperosmotic stress (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 7-9). The preprint reports that **loss of StlP** causes delocalized DivIVA foci and nascent peptidoglycan incorporation at multiple sites, and **“dramatically increased proximal branching (>60% of hyphae branch within 5 µm of the tip)”** (claessen2024thestomatinlikeprotein pages 5-7). The same work reports quantitative wall-thickness changes (apical thickness decreasing from ~35.5 nm to ~6.4 nm) (claessen2024thestomatinlikeprotein pages 5-7). These findings are mechanistically compelling but should be curated as **provisional** until peer-reviewed.

### 2.6 Cross-talk and oxidative cues: ROS/H2O2 as branch-inducing signals (preprint)
A 2023 preprint reports that the redox-active compound pyrogallol induces hyphal branching, and that the effect is suppressed by catalase, supporting an **H2O2-mediated mechanism** (kato2023redoxactivecompoundgenerated pages 1-7). The same preprint indicates that **H2O2 exposure alone** can induce branching (kato2023redoxactivecompoundgenerated pages 1-7). This is potentially important for ENVO “oxidative exposure” edges but is currently preprint- and assay-specific.

## 3) Candidate nodes grouped by type (ontology grounding where possible)
The following inventory is designed to map directly into a TraitMech YAML (nodes + grounded IDs where unambiguous). Many proteins are left as **gene labels** to avoid inventing UniProt accessions.

| Node type | Label | Suggested grounding | Notes/scope |
|---|---|---|---|
| Phenotype/process | mycelial growth | METPO:traitmech:000074 | Target morphology trait: branching filamentous hyphae forming vegetative mycelium, often followed by aerial hyphae and spores in streptomycetes (schlimpert2023thebestof pages 8-10, schlimpert2023thebestof pages 1-2) |
| Phenotype/process | polar tip growth | GO:0030997 | Apical cell-wall extension at hyphal tips; central defining process of Streptomyces vegetative and aerial hyphae growth (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Phenotype/process | branching | GO:0000904 | Emergence of new lateral growth sites behind/near the tip; often coordinated by polarisome splitting and stress responses (bhowmick2023osmoticstressresponses pages 1-2) |
| Phenotype/process | aerial hyphae formation | GO:0019827 | Developmental transition from substrate/vegetative mycelium to reproductive aerial filaments; requires hydrophobic sheath/surfactant systems (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2) |
| Phenotype/process | sporulation septation (Z-ladders) | label only | Streptomyces-specific ladder-like arrays of FtsZ rings in aerial hyphae that mark synchronous sporulation septa; no obvious single GO term for "Z-ladder" itself (bhowmick2024cellshapeand pages 1-2, falguera2024stressresponsesaffectinga pages 16-22) |
| Phenotype/process | programmed cell death | GO:0012501 | Developmentally regulated hyphal cell death contributes to multicellular development; eCIS implicated in S. coelicolor (schlimpert2023thebestof pages 8-10, falguera2024stressresponsesaffectinga pages 16-22) |
| Phenotype/process | membrane microdomain / increased membrane fluidity | GO:0019860 | Tip-associated membrane organization state proposed to spatially coordinate apical synthesis; grounding approximate because the actinobacterial RIF-like tip microdomain is not a dedicated ontology term (claessen2024thestomatinlikeprotein pages 7-9, claessen2024thestomatinlikeprotein pages 1-5) |
| Genes/proteins/complexes | DivIVA | gene label only | Core polarity determinant and polarisome component directing apical growth; stress-responsive phosphorylation target (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2) |
| Genes/proteins/complexes | polarisome | label only | Tip-localized multiprotein assembly centered on DivIVA; includes Scy/FilP and recruits growth machinery (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2) |
| Genes/proteins/complexes | Scy | gene label only | Coiled-coil apical growth protein/polarisome component involved in branching and tip organization (bhowmick2023osmoticstressresponses pages 1-2, claessen2024thestomatinlikeprotein pages 17-20) |
| Genes/proteins/complexes | FilP | gene label only | Intermediate filament-like/coiled-coil apical protein associated with polarisome and hyphal tip organization (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Genes/proteins/complexes | SepIVA | gene label only | DivIVA-like coiled-coil protein that accumulates at growing tips in S. venezuelae; associated with polar growth, dispensable in tested conditions (sen2024adispensablesepiva pages 1-2) |
| Genes/proteins/complexes | AfsK | gene label only | Ser/Thr kinase that phosphorylates DivIVA in response to cell-envelope stress, promoting hyperbranching (bhowmick2023osmoticstressresponses pages 1-2) |
| Genes/proteins/complexes | SppA | gene label only | Protein phosphatase that dephosphorylates DivIVA and regulates apical growth/polarity (claessen2024thestomatinlikeprotein pages 17-20, bhowmick2023osmoticstressresponses pages 1-2) |
| Genes/proteins/complexes | StlP | gene label only | Stomatin-like SPFH-domain protein organizing a tip-associated membrane microdomain under hyperosmotic stress; preprint evidence (claessen2024thestomatinlikeprotein pages 7-9, claessen2024thestomatinlikeprotein pages 1-5) |
| Genes/proteins/complexes | CglA | gene label only | LCP-family wall glycopolymer ligase required for normal hyphal diameter, FtsZ placement, and septation; localizes to tips/branches (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 8-10) |
| Genes/proteins/complexes | FtsZ | gene label only | Tubulin-like division scaffold; forms sporulation Z-ladders in aerial hyphae and occasional vegetative cross-walls (yague2023ftszphosphorylationpleiotropically pages 13-15, falguera2024stressresponsesaffectinga pages 16-22) |
| Genes/proteins/complexes | SepF | gene label only | FtsZ-interacting division protein required for late division steps in streptomycetes (yague2023ftszphosphorylationpleiotropically pages 16-17, yague2023ftszphosphorylationpleiotropically pages 13-15) |
| Genes/proteins/complexes | ZapA | gene label only | FtsZ polymerization modulator relevant to ring assembly dynamics (yague2023ftszphosphorylationpleiotropically pages 16-17) |
| Genes/proteins/complexes | DisA | gene label only | Diadenylate cyclase producing c-di-AMP; required for ionic/osmotic stress tolerance and linked to development (bhowmick2024cellshapeand pages 1-2, bhowmick2023osmoticstressresponses pages 6-7) |
| Genes/proteins/complexes | AtaC | gene label only | c-di-AMP phosphodiesterase; deletion elevates c-di-AMP and causes severe aerial hypha/sporulation defects (bhowmick2023osmoticstressresponses pages 6-7) |
| Genes/proteins/complexes | CslA | gene label only | Tip-localized cellulose-like glycan synthase associated with polar growth and StlP-organized complexes (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 5-7) |
| Genes/proteins/complexes | GlxA | gene label only | Accessory factor in CslA/GlxA glycan system linked to tip growth and morphogenesis (claessen2024thestomatinlikeprotein pages 1-5) |
| Genes/proteins/complexes | CslZ | gene label only | Cellulose/glycan-associated component interacting with StlP in tip-growth complex (claessen2024thestomatinlikeprotein pages 7-9) |
| Genes/proteins/complexes | LpmP | gene label only | Glycan/cell-wall-associated component interacting with StlP and apical synthesis machinery (claessen2024thestomatinlikeprotein pages 7-9, claessen2024thestomatinlikeprotein pages 5-7) |
| Genes/proteins/complexes | SapB | gene label only | Secreted surfactant peptide promoting emergence of aerial hyphae across the air-water interface (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2) |
| Genes/proteins/complexes | chaplins | gene family label only | Hydrophobic surface proteins that coat aerial hyphae; often polymerize as amyloid-like fibrils (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2) |
| Genes/proteins/complexes | rodlins | gene family label only | Hydrophobic sheath proteins associated with aerial structures and developmental robustness under stress (bhowmick2023osmoticstressresponses pages 1-2, bhowmick2023osmoticstressresponses pages 2-3) |
| Genes/proteins/complexes | eCIS | label only | Extracellular contractile injection system implicated in developmentally regulated cell death and morphology (schlimpert2023thebestof pages 8-10, falguera2024stressresponsesaffectinga pages 16-22) |
| Small molecules/chemicals | peptidoglycan | CHEBI:17334 | Main bacterial cell-wall polymer inserted at tips and septa during hyphal growth and sporulation (bhowmick2024cellshapeand pages 1-2, claessen2024thestomatinlikeprotein pages 1-5) |
| Small molecules/chemicals | wall teichoic acids / cell-wall glycopolymers | CHEBI:76983 | CglA-linked glycopolymers attached to peptidoglycan; important for shape and FtsZ positioning in S. venezuelae (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 8-10) |
| Small molecules/chemicals | c-di-AMP | CHEBI:206357 | Second messenger controlling osmotic homeostasis, growth, and development in Streptomyces (bhowmick2023osmoticstressresponses pages 7-8, bhowmick2023osmoticstressresponses pages 6-7) |
| Small molecules/chemicals | c-di-GMP | CHEBI:19029 | Second messenger regulating developmental regulators such as BldD and WhiG/RsiG in streptomycetes (schlimpert2023thebestof pages 8-10) |
| Small molecules/chemicals | hydrogen peroxide | CHEBI:16240 | ROS signal that induces hyphal branching in some Streptomyces assays (preprint) (kato2023redoxactivecompoundgenerated pages 15-20, kato2023redoxactivecompoundgenerated pages 1-7) |
| Small molecules/chemicals | reactive oxygen species | CHEBI:26523 | Broad signaling/stress category implicated in branch induction by redox-active compounds (kato2023redoxactivecompoundgenerated pages 15-20, kato2023redoxactivecompoundgenerated pages 1-7) |
| Small molecules/chemicals | catalase | EC:1.11.1.6 | Enzyme used experimentally to suppress pyrogallol/H2O2-mediated branching, supporting H2O2 causality (preprint) (kato2023redoxactivecompoundgenerated pages 1-7) |
| Small molecules/chemicals | proline | CHEBI:17203 | Compatible solute accumulated/imported during osmotic stress adaptation (bhowmick2023osmoticstressresponses pages 1-2, bhowmick2023osmoticstressresponses pages 7-8) |
| Small molecules/chemicals | ectoine | CHEBI:51899 | Compatible solute used in osmoprotection by Streptomyces (bhowmick2023osmoticstressresponses pages 1-2, bhowmick2023osmoticstressresponses pages 7-8) |
| Small molecules/chemicals | trehalose | CHEBI:18128 | Compatible solute/osmoprotectant associated with osmotic stress adaptation (bhowmick2023osmoticstressresponses pages 1-2, bhowmick2023osmoticstressresponses pages 7-8) |
| Small molecules/chemicals | potassium ion | CHEBI:29103 | First emergency osmotic-response solute accumulated after hyperosmotic shock (bhowmick2023osmoticstressresponses pages 7-8) |
| Small molecules/chemicals | sodium chloride | CHEBI:26710 | Standard osmotic-upshift stressor that arrests growth transiently and can block aerial development at high concentration (bhowmick2023osmoticstressresponses pages 2-3) |
| Small molecules/chemicals | sucrose | CHEBI:17992 | Osmotic-upshift stressor used experimentally to induce branching/growth arrest responses (bhowmick2023osmoticstressresponses pages 2-3) |
| Small molecules/chemicals | pyrogallol | CHEBI:17593 | Redox-active branching inducer that acts through H2O2/ROS in coculture-derived assays; preprint evidence (kato2023redoxactivecompoundgenerated pages 1-7) |
| Pathways/modules | apical cell-wall synthesis machinery | GO:0009252 | Functional module of peptidoglycan synthases/hydrolases concentrated at tips by the polarisome (bhowmick2023osmoticstressresponses pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Pathways/modules | peptidoglycan biosynthetic process | GO:0009252 | Cell-wall assembly process central to polar extension and septation (bhowmick2024cellshapeand pages 1-2, claessen2024thestomatinlikeprotein pages 1-5) |
| Pathways/modules | wall glycopolymer attachment to peptidoglycan | label only | CglA/LCP-mediated ligation activity; ontology grounding not obvious at process level (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 8-10) |
| Pathways/modules | cellulose-like glycan synthesis at hyphal tips | label only | CslA/GlxA/CslZ/LpmP-associated tip module implicated in polar growth protection, especially under stress (claessen2024thestomatinlikeprotein pages 7-9, claessen2024thestomatinlikeprotein pages 1-5) |
| Pathways/modules | c-di-AMP signaling | label only | DisA/AtaC-centered second messenger pathway for ionic/osmotic homeostasis and development (bhowmick2023osmoticstressresponses pages 7-8, bhowmick2023osmoticstressresponses pages 6-7) |
| Pathways/modules | c-di-GMP signaling | label only | Developmental signaling controlling BldD/WhiG-RsiG and transitions between developmental states (schlimpert2023thebestof pages 8-10) |
| Pathways/modules | osmoadaptation / compatible-solute response | GO:0006970 | Includes K+ uptake and compatible solutes such as proline, ectoine, trehalose during osmotic upshift (bhowmick2023osmoticstressresponses pages 1-2, bhowmick2023osmoticstressresponses pages 7-8) |
| Pathways/modules | oxidative stress / ROS signaling | GO:0006979 | Candidate signaling/stress module for H2O2-induced branch formation; mechanistic link to polarisome remains unresolved (kato2023redoxactivecompoundgenerated pages 15-20, kato2023redoxactivecompoundgenerated pages 1-7) |
| Environmental/exposure factor | osmotic upshift (NaCl/sucrose) | label only | Experimental increase in medium osmolarity causing temporary growth arrest then hyperbranching (bhowmick2023osmoticstressresponses pages 2-3) |
| Environmental/exposure factor | hyperosmotic stress | ENVO:01001617 | Soil-relevant stress context; important for c-di-AMP biology and StlP microdomain phenotype (bhowmick2023osmoticstressresponses pages 7-8, claessen2024thestomatinlikeprotein pages 1-5) |
| Environmental/exposure factor | high salt / salinity stress | ENVO:01001813 | Strong inhibitor of aerial hypha formation and sporulation at sufficiently high NaCl (bhowmick2023osmoticstressresponses pages 2-3) |
| Environmental/exposure factor | nutrient depletion | label only | Developmental cue linked to alternative foraging/exploratory growth and classic sporulation transitions; not always a direct trigger of mycelium formation itself (falguera2024stressresponsesaffectinga pages 22-26) |
| Environmental/exposure factor | cell-wall stress (bacitracin/vancomycin) | label only | Envelope stress context that increases DivIVA phosphorylation via AfsK and promotes hyperbranching (kato2023redoxactivecompoundgenerated pages 15-20, bhowmick2023osmoticstressresponses pages 1-2) |
| Environmental/exposure factor | oxidative cue / H2O2 exposure | label only | Exogenous or coculture-generated ROS branch-inducing condition in specific Streptomyces assays (preprint) (kato2023redoxactivecompoundgenerated pages 15-20, kato2023redoxactivecompoundgenerated pages 1-7) |
| Environmental/exposure factor | soil habitat | ENVO:00001998 | Natural environment where filamentous network growth and osmotic fluctuations are ecologically relevant (bhowmick2023osmoticstressresponses pages 1-2, kato2023redoxactivecompoundgenerated pages 1-7) |
| Assays/experimental context | fluorescence microscopy of DivIVA/FtsZ/CglA/YPet fusions | label only | Core localization assay for polarisome, Z-ladders, and CglA growth-zone localization (bhowmick2024cellshapeand pages 5-8, bhowmick2024cellshapeand media 2038f321) |
| Assays/experimental context | osmotic-shift assay (NaCl or sucrose addition) | label only | Time-resolved morphology assay demonstrating 2–3 h arrest and lateral hyperbranching after upshift (bhowmick2023osmoticstressresponses pages 2-3) |
| Assays/experimental context | high-salt developmental assay | label only | Plate-based developmental readout for aerial hyphae/sporulation inhibition and c-di-AMP phenotypes (bhowmick2023osmoticstressresponses pages 6-7, bhowmick2023osmoticstressresponses pages 2-3) |
| Assays/experimental context | pyrogallol/H2O2 branching assay | label only | Chemical perturbation assay showing ROS-dependent branch induction; catalase suppression used for causality (preprint) (kato2023redoxactivecompoundgenerated pages 1-7) |
| Assays/experimental context | microdroplet GC-MS methyl bromide gas-reporting assay | label only | Quantifies growth of filamentous S. venezuelae in droplets; useful because optical readouts are hindered by mycelial morphology (song2023methylhalidetransferasebased pages 4-7, song2023methylhalidetransferasebased pages 1-2) |
| Assays/experimental context | cryo-EM/TEM cell-wall thickness analysis | label only | Used to quantify wall thinning and structural defects in StlP and CglA-related studies (claessen2024thestomatinlikeprotein pages 5-7, bhowmick2024cellshapeand pages 5-8) |


*Table: This table inventories candidate nodes for a TraitMech causal graph of bacterial mycelial growth, grouped by biological entity type and annotated with suggested ontology grounding. It is useful for curating a structured YAML graph with prioritized mechanistic entities and clear scope notes.*

## 4) Evidence-backed candidate causal edges (triples) for curation
The table below is curated for direct translation into edges with explicit uncertainty notes.

| Edge (subject–predicate–object triple) | Edge type | Taxon/context | Evidence snippet (short quote) | Reference (DOI + URL + year) | Curation notes/uncertainty |
|---|---|---|---|---|---|
| DivIVA polarisome → directs → apical hyphal growth | gene/protein | *Streptomyces* vegetative and aerial hyphae | “the DivIVA-polarisome drives the growth of both the branching vegetative hyphae and the non-branching aerial hyphae” (schlimpert2023thebestof pages 8-10, schlimpert2023thebestof pages 1-2) | 10.1128/JB.00153-23; https://doi.org/10.1128/jb.00153-23; 2023 | Strong review-level statement; broadly accepted for streptomycetes. |
| Polarisome splitting → causes → daughter polarisomes/new branch emergence | process | *Streptomyces* tip growth/branching | “Splitting of the polarisomes at growing tips gives rise to daughter polarisomes” coordinating branches (bhowmick2023osmoticstressresponses pages 1-2) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | Strong review synthesis; mechanistic but not a single perturbation experiment in these excerpts. |
| AfsK-mediated DivIVA phosphorylation → promotes → hyperbranching | gene/protein | Cell-wall stress response in *Streptomyces* | “AfsK phosphorylates DivIVA in response to… bacitracin, vancomycin… high DivIVA phosphorylation causes… multiple new polarisomes, producing a hyperbranching phenotype” (bhowmick2023osmoticstressresponses pages 1-2) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | Good mechanistic review statement; curate as stress-responsive branch-control edge. |
| SppA dephosphorylation of DivIVA → regulates → apical growth | gene/protein | *Streptomyces* polarity control | “SppA dephosphorylates DivIVA” and “regulates apical growth” (bhowmick2023osmoticstressresponses pages 1-2, claessen2024thestomatinlikeprotein pages 17-20) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023; 10.21203/rs.3.rs-3811693/v1; https://doi.org/10.21203/rs.3.rs-3811693/v1; 2024 | Supported by review plus preprint mention; direct edge is reasonable but one source is preprint. |
| StlP-organized membrane microdomain → enables → polar growth under hyperosmotic stress | gene/protein | Filamentous actinobacteria; hyperosmotic stress | “StlP… establishes a membrane microdomain of increased fluidity. This StlP-dependent microdomain is required to coordinate membrane and cell-wall growth at the tip” (claessen2024thestomatinlikeprotein pages 1-5) | 10.21203/rs.3.rs-3811693/v1; https://doi.org/10.21203/rs.3.rs-3811693/v1; 2024 | Preprint; promising but should be flagged until peer-reviewed final version. |
| Loss of StlP → increases → proximal branching | gene/protein | *Streptomyces coelicolor* / filamentous actinobacteria | “Consequences of StlP loss include dramatically increased proximal branching (>60% of hyphae branch within 5 µm of the tip)” (claessen2024thestomatinlikeprotein pages 5-7) | 10.21203/rs.3.rs-3811693/v1; https://doi.org/10.21203/rs.3.rs-3811693/v1; 2024 | Quantitative and specific, but from preprint. |
| Loss of StlP → causes → wall thinning and aberrant cell-wall synthesis | gene/protein | *Streptomyces coelicolor* / filamentous actinobacteria | “loss of StlP causes… aberrant cell-wall synthesis, wall thinning” with apical thickness “~35.5 nm → 6.4 nm” (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 5-7) | 10.21203/rs.3.rs-3811693/v1; https://doi.org/10.21203/rs.3.rs-3811693/v1; 2024 | Strong phenotype, but preprint. |
| CglA ligase → mediates → wall teichoic acid/glycopolymer attachment to peptidoglycan | gene/protein | *Streptomyces venezuelae* cell wall biogenesis | “CglA is identified as an LCP-LytR_C domain glycopolymer ligase… [that] catalyzes attachment of wall teichoic acids (WTAs) to peptidoglycan” (bhowmick2024cellshapeand pages 1-2) | 10.1128/mbio.01492-24; https://doi.org/10.1128/mbio.01492-24; 2024 | Strong direct primary evidence. |
| CglA localization → occurs at → hyphal tips and branching points | gene/protein | *Streptomyces venezuelae* vegetative growth zones | “YPet-CglA localizes to regions of active cell-wall incorporation — hyphal tips and branching points” (bhowmick2024cellshapeand pages 8-10, bhowmick2024cellshapeand media 2038f321) | 10.1128/mbio.01492-24; https://doi.org/10.1128/mbio.01492-24; 2024 | Strong localization edge; image evidence available. |
| Reduced CglA/glycopolymers → disrupts → FtsZ-ring positioning and septa placement | gene/protein | *Streptomyces venezuelae* sporogenic hyphae | “Loss of CglA… causes… failures in FtsZ-ring formation and positioning, and consequently misplaced division septa” (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 8-10) | 10.1128/mbio.01492-24; https://doi.org/10.1128/mbio.01492-24; 2024 | Strong causal mutant phenotype; good curation candidate. |
| c-di-AMP → supports → survival at high salinity/osmotic stress | chemical | *Streptomyces* osmotic stress physiology | “c-di-AMP is important for survival at high salinity” (bhowmick2023osmoticstressresponses pages 7-8) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | General signaling edge; could be modeled via DisA/AtaC if granularity desired. |
| ataC deletion / elevated c-di-AMP → causes → severe sporulation and aerial-hypha defects | gene/protein | *Streptomyces venezuelae* c-di-AMP dysregulation | “deletion of the c-di-AMP phosphodiesterase ataC raises c-di-AMP, compromises growth, and causes severe sporulation and aerial-hyphae defects” (bhowmick2023osmoticstressresponses pages 6-7) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | Strong but specific to c-di-AMP homeostasis perturbation. |
| Osmotic upshift (NaCl/sucrose) → causes → temporary growth arrest followed by hyperbranching | environment | *Streptomyces* osmotic upshift assays | “osmotic upshift… arrests Streptomyces hyphal growth for ~2–3 hours, after which cells resume by forming multiple new lateral branches producing a hyperbranching mycelium” (bhowmick2023osmoticstressresponses pages 2-3) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | Strong assay-defined environmental edge. |
| High salt (NaCl) → blocks → aerial hyphae formation and sporulation | environment | *Streptomyces venezuelae* salt stress | “S. venezuelae fails to raise aerial hyphae under high NaCl… spore formation is essentially blocked at 0.5 M NaCl” (bhowmick2023osmoticstressresponses pages 2-3) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | Strong environmental inhibition edge; salt concentration should be retained in notes if curated. |
| SapB/chaplins/rodlins → promote → aerial hyphae emergence | gene/protein | *Streptomyces* aerial development | “Aerial development involves production of chaplin/rodlin hydrophobic sheaths and the surfactant SapB to overcome surface tension” (bhowmick2023osmoticstressresponses pages 1-2) | 10.1093/femsml/uqad020; https://doi.org/10.1093/femsml/uqad020; 2023 | Strong developmental mechanism; can split into separate nodes if needed. |
| FtsZ Z-ladders → drive → sporulation septation/spore-chain formation | gene/protein | Sporogenic aerial hyphae of *Streptomyces* | “FtsZ… forming ladder-like arrays of multiple FtsZ-rings along the filament; constriction of these rings and subsequent separation yields regularly shaped spores” (bhowmick2024cellshapeand pages 1-2, falguera2024stressresponsesaffectinga pages 16-22) | 10.1128/mbio.01492-24; https://doi.org/10.1128/mbio.01492-24; 2024; 10.1007/s10482-022-01778-w; https://doi.org/10.1007/s10482-022-01778-w; 2023 | Strong and central curation edge. |
| FtsZ phosphorylation state → alters → Z-ladder formation and spore length | gene/protein | *Streptomyces coelicolor* phosphomimetic FtsZ alleles | “Phosphomimetic FtsZ alleles… lack visible FtsZ-eGFP sporulation ladders” and “spacing between the septa… was larger… correlating with ‘significantly longer’ spores” (yague2023ftszphosphorylationpleiotropically pages 8-10, yague2023ftszphosphorylationpleiotropically pages 10-13) | 10.1007/s10482-022-01778-w; https://doi.org/10.1007/s10482-022-01778-w; 2023 | Strong but allele/assay-specific; best marked taxon- and construct-specific. |
| H2O2 / ROS → induces → hyphal branching | chemical | *Streptomyces variegatus* and some other *Streptomyces* spp. | “H2O2 was tested and similar activity which induced hyphal branching was observed” (kato2023redoxactivecompoundgenerated pages 1-7, kato2023redoxactivecompoundgenerated pages 15-20) | 10.1101/2023.01.12.523877; https://doi.org/10.1101/2023.01.12.523877; 2023 | Preprint and species-specific; promising but should be marked uncertain. |
| Catalase → suppresses → pyrogallol-induced branching | chemical | *Streptomyces* branching assay with pyrogallol | “the pyrogallol activity was diminished by adding catalase, which broke down H2O2” (kato2023redoxactivecompoundgenerated pages 1-7) | 10.1101/2023.01.12.523877; https://doi.org/10.1101/2023.01.12.523877; 2023 | Good perturbation evidence, but preprint and chemical-assay-specific. |
| eCIS → contributes to → programmed cell death affecting developmental switch | process | *Streptomyces coelicolor* development in liquid media | “eCISs appear to participate in the complex developmental process… mutants display reduced levels of cell death and altered morphology… modulate the developmental switch that leads to aerial hyphae formation and sporulation” (schlimpert2023thebestof pages 8-10, falguera2024stressresponsesaffectinga pages 16-22) | 10.1038/s41467-023-37087-7; https://doi.org/10.1038/s41467-023-37087-7; 2023 | Relevant to developmental mycelium remodeling, but more indirect than core polarity/cell-wall edges. |


*Table: This table compiles curation-ready candidate causal edges for bacterial mycelial growth in Streptomyces and related filamentous actinobacteria, with short supporting snippets, DOI-first references, and uncertainty notes for preprints or assay-specific findings.*

## 5) Current applications and real-world implementations
### 5.1 Industrial/biotech context: morphology-development coupling and metabolite production
A 2023 review emphasizes that *Streptomyces* are foundational models because of their **unusual fungal-like development** and prolific specialized metabolite production, providing the conceptual basis for linking mycelial growth modes to antibiotic production programs and their regulation (schlimpert2023thebestof pages 1-2, schlimpert2023thebestof pages 8-10). Mechanistically, the developmental switch to aerial growth/sporulation is integrated with regulatory complexity (sigma factors, TCSs, kinases) that coordinates multicellular growth with metabolism (schlimpert2023thebestof pages 1-2).

### 5.2 Measurement/engineering: microdroplet systems and non-optical growth quantification
A 2023 peer-reviewed Applied and Environmental Microbiology study demonstrates a practical solution to measuring filamentous growth where optical density is unreliable due to scattering/pellets. An MHT gas-reporting system in *S. venezuelae* provided a **“100- to 1,000-fold increase”** in signal-to-noise vs optical reporters, with reliable detection down to **10^6 CFU/mL** (song2023methylhalidetransferasebased pages 1-2). This provides an implementable assay node for TraitMech graphs (quantification context rather than mechanism).

## 6) Recent statistics and quantitative data (from 2023–2024 studies)
- **Osmotic-upshift dynamics:** hyphal growth arrest for **~2–3 hours** after osmotic upshift (NaCl/sucrose), then resumption via multiple new branches (“hyperbranching”) (bhowmick2023osmoticstressresponses pages 2-3).
- **Salt thresholds for development:** *S. venezuelae* sporulates at **0.25 M NaCl**, but sporulation is essentially blocked at **0.5 M NaCl**; aerial hyphae formation can fail under high NaCl (bhowmick2023osmoticstressresponses pages 2-3).
- **Sporulation division architecture:** sporulation division involves up to **~200 regularly spaced division sites** (falguera2024stressresponsesaffectinga pages 16-22).
- **CglA mutant impact on viability:** *cglA* mutant viable spore yield reported as **~13% of wild type** (bhowmick2024cellshapeand pages 5-8).
- **Microdroplet assay performance:** estimated doubling time **~50 min** for labeled and wild-type *S. venezuelae*; mature vegetative mycelium fragments **~0.9–1.8 µm diameter** and **up to 150 µm length**; CFU conversion **~2×10^8 CFU/mL per OD unit**; lowest reliable detection **~10^6 CFU/mL** within **~4 h**; density–signal correlation r² up to **0.9975** (song2023methylhalidetransferasebased pages 4-7, song2023methylhalidetransferasebased pages 1-2).
- **StlP preprint quantitative morphology:** proximal branching **>60% of hyphae within 5 µm of tip**; wall thickness reductions and other nanometer-scale measurements (preprint) (claessen2024thestomatinlikeprotein pages 5-7).

## 7) Expert opinions and authoritative synthesis (interpretation)
- **Core consensus:** Mycelial growth in *Streptomyces* is fundamentally a **polarity-driven cell-wall growth program** (DivIVA-centered polarisome) coupled to **developmental differentiation** into aerial hyphae and spore chains (schlimpert2023thebestof pages 8-10, schlimpert2023thebestof pages 1-2).
- **Regulatory architecture:** Environmental stress inputs (osmotic stress, envelope stress) are integrated into polarity and development via second messengers (c-di-AMP), kinase/phosphatase control (AfsK/SppA), and developmental regulators (bld/whi systems; c-di-GMP mediated controls noted in review) (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2).
- **Current frontier (2024):** Cell-envelope “non-PG” components (glycopolymers/WTAs) and membrane organization (microdomains) are increasingly implicated as **direct determinants** of where growth and septation occur, moving beyond a PG-only perspective (bhowmick2024cellshapeand pages 1-2, claessen2024thestomatinlikeprotein pages 1-5).

## 8) Curation warnings (do not curate without flags)
1. **Preprints:** StlP microdomain mechanisms (Research Square) and ROS/H2O2 branching induction (bioRxiv) should be flagged as **uncertain / pending peer review** (claessen2024thestomatinlikeprotein pages 1-5, kato2023redoxactivecompoundgenerated pages 1-7).
2. **Assay-specific edges:** Osmotic upshift timing (2–3 h arrest), salt thresholds (0.25–0.5 M NaCl), and catalase suppression are strong but should carry **explicit condition nodes** (bhowmick2023osmoticstressresponses pages 2-3, kato2023redoxactivecompoundgenerated pages 1-7).
3. **Allele/construct specificity:** FtsZ phosphomimetic effects on Z-ladder visibility and spore length depend on engineered alleles and imaging context; curate with strong taxon+allele qualifiers (yague2023ftszphosphorylationpleiotropically pages 10-13, yague2023ftszphosphorylationpleiotropically pages 8-10).
4. **Ontology gaps:** “Z-ladder” and actinobacterial tip “RIF-like” membrane microdomains lack clean single-term grounding; represent as label-only nodes with mapping notes (artifact-01).

## 9) DOI-first bibliography (URLs + publication dates)
- Schlimpert S, Elliot MA. *The Best of Both Worlds—Streptomyces coelicolor and Streptomyces venezuelae as Model Species for Studying Antibiotic Production and Bacterial Multicellular Development.* **Journal of Bacteriology**. **2023-07**. DOI: **10.1128/jb.00153-23**. https://doi.org/10.1128/jb.00153-23 (schlimpert2023thebestof pages 1-2, schlimpert2023thebestof pages 8-10)
- Bhowmick S, Shenouda ML, Tschowri N. *Osmotic stress responses and the biology of the second messenger c-di-AMP in Streptomyces.* **microLife**. **2023-04**. DOI: **10.1093/femsml/uqad020**. https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 1-2, bhowmick2023osmoticstressresponses pages 2-3, bhowmick2023osmoticstressresponses pages 7-8)
- Bhowmick S et al. *Cell shape and division septa positioning in filamentous Streptomyces require a functional cell wall glycopolymer ligase CglA.* **mBio**. **2024-10**. DOI: **10.1128/mbio.01492-24**. https://doi.org/10.1128/mbio.01492-24 (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 5-8, bhowmick2024cellshapeand media 2038f321)
- Sen BC et al. *A dispensable SepIVA orthologue in Streptomyces venezuelae is associated with polar growth and not cell division.* **BMC Microbiology**. **2024-11**. DOI: **10.1186/s12866-024-03625-6**. https://doi.org/10.1186/s12866-024-03625-6 (sen2024adispensablesepiva pages 1-2)
- Yagüe P et al. *FtsZ phosphorylation pleiotropically affects Z-ladder formation, antibiotic production, and morphogenesis in Streptomyces coelicolor.* **Antonie van Leeuwenhoek**. **2023-11**. DOI: **10.1007/s10482-022-01778-w**. https://doi.org/10.1007/s10482-022-01778-w (yague2023ftszphosphorylationpleiotropically pages 8-10, yague2023ftszphosphorylationpleiotropically pages 10-13)
- Vladimirov M et al. *A contractile injection system is required for developmentally regulated cell death in Streptomyces coelicolor.* **Nature Communications**. **2023-03**. DOI: **10.1038/s41467-023-37087-7**. https://doi.org/10.1038/s41467-023-37087-7 (falguera2024stressresponsesaffectinga pages 16-22)
- Song X et al. *Methyl halide transferase-based gas reporters for quantification of filamentous bacteria in microdroplet emulsions.* **Applied and Environmental Microbiology**. **2023-09**. DOI: **10.1128/aem.00764-23**. https://doi.org/10.1128/aem.00764-23 (song2023methylhalidetransferasebased pages 1-2, song2023methylhalidetransferasebased pages 4-7)
- Claessen D et al. *The stomatin-like protein StlP organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress.* **Research Square (preprint)**. **2024-01**. DOI: **10.21203/rs.3.rs-3811693/v1**. https://doi.org/10.21203/rs.3.rs-3811693/v1 (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 5-7)
- Kato M, Asamizu S, Onaka H. *Redox-active compound generated by bacterial crosstalk induces hypha branching in Streptomyces species.* **bioRxiv (preprint)**. **2023-01**. DOI: **10.1101/2023.01.12.523877**. https://doi.org/10.1101/2023.01.12.523877 (kato2023redoxactivecompoundgenerated pages 1-7)

---

## Appendix: Key visual evidence
- **CglA localization and Z-ladder disruption** in *S. venezuelae* (WT vs *cglA* mutant): (bhowmick2024cellshapeand media 2038f321, bhowmick2024cellshapeand media faa1a359, bhowmick2024cellshapeand media 603f43a1).

References

1. (schlimpert2023thebestof pages 8-10): Susan Schlimpert and Marie A. Elliot. The best of both worlds—streptomyces coelicolor and streptomyces venezuelae as model species for studying antibiotic production and bacterial multicellular development. Journal of Bacteriology, Jul 2023. URL: https://doi.org/10.1128/jb.00153-23, doi:10.1128/jb.00153-23. This article has 53 citations and is from a peer-reviewed journal.

2. (schlimpert2023thebestof pages 1-2): Susan Schlimpert and Marie A. Elliot. The best of both worlds—streptomyces coelicolor and streptomyces venezuelae as model species for studying antibiotic production and bacterial multicellular development. Journal of Bacteriology, Jul 2023. URL: https://doi.org/10.1128/jb.00153-23, doi:10.1128/jb.00153-23. This article has 53 citations and is from a peer-reviewed journal.

3. (bhowmick2023osmoticstressresponses pages 1-2): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

4. (bhowmick2024cellshapeand pages 1-2): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (bhowmick2024cellshapeand pages 8-10): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (bhowmick2024cellshapeand pages 5-8): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

7. (bhowmick2024cellshapeand media 2038f321): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (bhowmick2024cellshapeand media faa1a359): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (falguera2024stressresponsesaffectinga pages 16-22): JVT Falguera. Stress responses affecting the sporulation and specialized metabolism programs of streptomycetes. Unknown journal, 2024.

10. (yague2023ftszphosphorylationpleiotropically pages 8-10): Paula Yagüe, Joost Willemse, Xiansha Xiao, Le Zhang, Angel Manteca, and Gilles P. van Wezel. Ftsz phosphorylation pleiotropically affects z-ladder formation, antibiotic production, and morphogenesis in streptomyces coelicolor. Antonie Van Leeuwenhoek, 116:1-19, Nov 2023. URL: https://doi.org/10.1007/s10482-022-01778-w, doi:10.1007/s10482-022-01778-w. This article has 10 citations.

11. (yague2023ftszphosphorylationpleiotropically pages 10-13): Paula Yagüe, Joost Willemse, Xiansha Xiao, Le Zhang, Angel Manteca, and Gilles P. van Wezel. Ftsz phosphorylation pleiotropically affects z-ladder formation, antibiotic production, and morphogenesis in streptomyces coelicolor. Antonie Van Leeuwenhoek, 116:1-19, Nov 2023. URL: https://doi.org/10.1007/s10482-022-01778-w, doi:10.1007/s10482-022-01778-w. This article has 10 citations.

12. (bhowmick2023osmoticstressresponses pages 2-3): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

13. (bhowmick2023osmoticstressresponses pages 7-8): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

14. (bhowmick2023osmoticstressresponses pages 6-7): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

15. (claessen2024thestomatinlikeprotein pages 1-5): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

16. (claessen2024thestomatinlikeprotein pages 7-9): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

17. (claessen2024thestomatinlikeprotein pages 5-7): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

18. (kato2023redoxactivecompoundgenerated pages 1-7): Manami Kato, Shumpei Asamizu, and Hiroyasu Onaka. Redox-active compound generated by bacterial crosstalk induces hypha branching in streptomyces species. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.12.523877, doi:10.1101/2023.01.12.523877. This article has 0 citations.

19. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

20. (claessen2024thestomatinlikeprotein pages 17-20): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

21. (yague2023ftszphosphorylationpleiotropically pages 13-15): Paula Yagüe, Joost Willemse, Xiansha Xiao, Le Zhang, Angel Manteca, and Gilles P. van Wezel. Ftsz phosphorylation pleiotropically affects z-ladder formation, antibiotic production, and morphogenesis in streptomyces coelicolor. Antonie Van Leeuwenhoek, 116:1-19, Nov 2023. URL: https://doi.org/10.1007/s10482-022-01778-w, doi:10.1007/s10482-022-01778-w. This article has 10 citations.

22. (yague2023ftszphosphorylationpleiotropically pages 16-17): Paula Yagüe, Joost Willemse, Xiansha Xiao, Le Zhang, Angel Manteca, and Gilles P. van Wezel. Ftsz phosphorylation pleiotropically affects z-ladder formation, antibiotic production, and morphogenesis in streptomyces coelicolor. Antonie Van Leeuwenhoek, 116:1-19, Nov 2023. URL: https://doi.org/10.1007/s10482-022-01778-w, doi:10.1007/s10482-022-01778-w. This article has 10 citations.

23. (kato2023redoxactivecompoundgenerated pages 15-20): Manami Kato, Shumpei Asamizu, and Hiroyasu Onaka. Redox-active compound generated by bacterial crosstalk induces hypha branching in streptomyces species. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.12.523877, doi:10.1101/2023.01.12.523877. This article has 0 citations.

24. (falguera2024stressresponsesaffectinga pages 22-26): JVT Falguera. Stress responses affecting the sporulation and specialized metabolism programs of streptomycetes. Unknown journal, 2024.

25. (song2023methylhalidetransferasebased pages 4-7): Xinhao Song, Sarah J. Kong, Seokju Seo, Ramya Ganiga Prabhakar, and Yousif Shamoo. Methyl halide transferase-based gas reporters for quantification of filamentous bacteria in microdroplet emulsions. Applied and Environmental Microbiology, Sep 2023. URL: https://doi.org/10.1128/aem.00764-23, doi:10.1128/aem.00764-23. This article has 0 citations and is from a peer-reviewed journal.

26. (song2023methylhalidetransferasebased pages 1-2): Xinhao Song, Sarah J. Kong, Seokju Seo, Ramya Ganiga Prabhakar, and Yousif Shamoo. Methyl halide transferase-based gas reporters for quantification of filamentous bacteria in microdroplet emulsions. Applied and Environmental Microbiology, Sep 2023. URL: https://doi.org/10.1128/aem.00764-23, doi:10.1128/aem.00764-23. This article has 0 citations and is from a peer-reviewed journal.

27. (bhowmick2024cellshapeand media 603f43a1): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.