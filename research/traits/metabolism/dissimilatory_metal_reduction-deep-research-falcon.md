---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:40:13.295569'
end_time: '2026-06-18T04:57:51.370074'
duration_seconds: 1058.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory metal reduction
  trait_identifier: traitmech:000039
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_metal_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism conserves energy
    for growth by coupling the oxidation of organic matter or hydrogen to the reduction
    of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
  parent_traits: METPO:1000802
  synonyms: dissimilatory metal-ion reduction
  evidence_summary: 'DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter
    coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical
    reactions in aquatic sediments, soils, and groundwater (Lovley review establishes
    dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic
    respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson
    & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as
    terminal electron acceptors in anaerobic respiration.)'
  causal_graph_summary: 'metal_reduction_anaerobic_respiration: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory metal reduction
- **METPO identifier:** traitmech:000039
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
- **Parent traits:** METPO:1000802
- **Synonyms:** dissimilatory metal-ion reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as terminal electron acceptors in anaerobic respiration.)
- **Existing causal graph summary:** metal_reduction_anaerobic_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory metal reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_metal_reduction.yaml`.

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
- **Trait label:** dissimilatory metal reduction
- **METPO identifier:** traitmech:000039
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of a metal (e.g. Fe(III), Mn(IV)) as a terminal electron acceptor.
- **Parent traits:** METPO:1000802
- **Synonyms:** dissimilatory metal-ion reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory metal (Fe(III)/Mn(IV)) reduction as energy-conserving anaerobic respiration; parent of the metal-specific reduction sub-variants.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports metals as terminal electron acceptors in anaerobic respiration.)
- **Existing causal graph summary:** metal_reduction_anaerobic_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory metal reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_metal_reduction.yaml`.

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


## Research Report: Dissimilatory Metal Reduction (TraitMech/METPO: traitmech:000039)

### 1) Key concepts and definitions (current understanding)

**Trait definition and scope.** Dissimilatory metal reduction (DMR) is an anaerobic respiratory metabolism in which microorganisms conserve energy for growth by coupling oxidation of electron donors (organic matter or H2) to reduction of oxidized metals—classically Fe(III) and Mn(IV)—as terminal electron acceptors (traitmech:000039). In subsurface contexts, oxidized, insoluble metals can be “an abundant electron acceptor that microbes could potentially utilize as a respiratory substrate,” and successful DMR requires moving electrons to extracellular (often insoluble) acceptors via extracellular electron transfer (EET). (hsu2024isolationandgenomic pages 1-2)

**Operational/assay definition (what is being measured).** DMR is frequently detected by: (i) accumulation of reduced metal (e.g., Fe(II) from Fe(III)), (ii) donor consumption/mineralization, and/or (iii) current generation when electrodes substitute for minerals. For example, a newly isolated Fe(III)-reducing bacterium (MK1) was enriched under “anaerobic, acetate-oxidizing, and Fe(III) citrate-reducing conditions,” showing how soluble Fe(III)-chelate assays can operationalize the trait even when the ecological target includes insoluble oxides. (hsu2024isolationandgenomic pages 1-2)

**Distinguishing boundaries.**
- **Versus assimilatory metal reduction:** Assimilatory processes reduce metals for biosynthesis (nutrient acquisition) and are not primarily energy-conserving terminal electron-acceptor respiration. The evidence base assembled here operationalizes DMR as *respiratory* electron disposal to terminal acceptors and emphasizes required EET machinery, which is not a defining feature of assimilatory uptake. (hsu2024isolationandgenomic pages 1-2, jiang2019advancesinfe(iii) pages 3-4)
- **Versus fermentation:** Fermentation does not rely on external terminal electron acceptors; DMR is defined by electron flow to external metal acceptors and energy conservation through anaerobic respiration. (jiang2019advancesinfe(iii) pages 3-4)
- **Versus abiotic metal reduction:** Field and lab settings include abiotic redox reactions, but DMR is tied to microbial electron transport chains and EET components (cytochromes/conduits/shuttles) whose perturbation changes metal reduction/electrical output. (soares2025toolsforenhancing pages 5-8, hou2025cooccurrenceofdirect pages 1-2)

**Environmental context and thermodynamic positioning.** In groundwater, Fe(III) reduction is positioned in the canonical redox ladder (O2 > NO3− > Mn(IV) > Fe(III) > SO42− > CO2), and Fe(III) in anaerobic subsurface environments is largely insoluble/crystalline with very low solubility at neutral pH (~10−9 M), motivating mechanisms for accessing solid-phase acceptors. (jiang2019advancesinfe(iii) pages 1-3, jiang2019advancesinfe(iii) pages 3-4)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 Direct nanowire-charging pathway (2024 Nature Communications)
A major 2024 mechanistic advance is evidence for a **direct periplasm-to-nanowire electron injection** route in *Geobacter sulfurreducens*, resolving spatial/kinetic barriers across a relatively large periplasm.

- **Core finding:** “All major periplasmic triheme cytochromes PpcABCDE (PpcA-E) transiently bind to hexaheme OmcS nanowires to transfer electrons,” establishing a defined nanowire-charging pathway. (portela2024widespreadextracellularelectron pages 2-3)
- **Structural basis:** OmcS nanowires contain stacked hemes, and “closely stacked hemes can promote rapid and insulated electron conduction over distances of several micrometers.” (portela2024widespreadextracellularelectron pages 2-3)
- **Quantitative electrochemical update:** Intact OmcS nanowires have an apparent midpoint potential Eapp = −130 ± 13 mV and a 360 mV redox-active window (−0.31 to 0.05 V), aligning better with periplasmic cytochromes (≈ −117 to −143 mV) than prior non-native OmcS values and thereby removing a proposed thermodynamic barrier. (portela2024widespreadextracellularelectron pages 2-3)
- **Trait-relevant implication:** *Geobacter* “requires nanowires of cytochrome OmcS to eliminate respiratory electrons via EET to soil-abundant Fe(III) oxide.” (portela2024widespreadextracellularelectron pages 2-3)

A schematic consistent with this pathway (including PpcA–E→OmcS and other EET components) is shown in a figure panel retrieved from the same paper. (portela2024widespreadextracellularelectron media 6c43b966)

#### 2.2 Expansion of taxonomic breadth and Gram-positive Fe(III) reducers (2024 AEM)
Hsu et al. (2024) report isolation and genomics of a novel Gram-positive Fe(III) reducer (“*Metallumcola ferriviriculae*” MK1) enriched under “anaerobic, acetate-oxidizing, and Fe(III) citrate-reducing conditions.” (hsu2024isolationandgenomic pages 1-2)

The study also situates DMR in deep subsurface brines that are “anoxic, and reduced (−200 to −500 mV)” and rich in metal oxides, linking environmental redox conditions to trait expression. (hsu2024isolationandgenomic pages 1-2)

#### 2.3 Assay dependence and electrode-specific conduits (2024 Nat Commun)
In addition to OmcS nanowires, *Geobacter* uses multiple outer-membrane porin–cytochrome conduits; notably, “ExtABCD are essential in bacterial growth only on electrodes,” highlighting **assay context (electrode vs mineral) as a boundary case** for the trait graph. (portela2024widespreadextracellularelectron pages 2-3)

### 3) Current applications and real-world implementations

#### 3.1 Bioelectrochemical systems (microbial fuel cells and related technologies)
Microbial fuel cells (MFCs) operationalize DMR/EET principles by using anodes as terminal electron acceptors. In SRB-focused MFC work, “Microbial fuel cells (MFCs) have been used as a promising technology for electrical energy generation,” converting “chemical energy of organic compounds into electricity.” (hou2025cooccurrenceofdirect pages 1-2)

Reported SRB-driven MFC power densities span “0.013 W/m2 to 0.68 W/m2,” providing an order-of-magnitude benchmark for real systems. (hou2025cooccurrenceofdirect pages 1-2)

Recent BES engineering strategies (electrode/nanomaterial/mediator approaches) report substantially higher power densities in some configurations (reviewed literature), e.g., maximum power density 5.07 W/m2 in one modified-anode system and current densities such as 673 mA/m2 under optimized potential in *Shewanella* systems. (soares2025toolsforenhancing pages 12-13)

#### 3.2 Groundwater/sediment remediation and metal mobility
A recurring application is stimulating Fe(III) reduction to drive contaminant transformations and immobilization/mobilization dynamics. Jiang et al. (2019) review Fe(III) bioreduction “application prospect for groundwater remediation” and emphasize that Fe(III) is commonly insoluble in anaerobic subsurface settings, requiring EET strategies (direct contact, ligands, shuttles) to access it. (jiang2019advancesinfe(iii) pages 1-3, jiang2019advancesinfe(iii) pages 3-4)

#### 3.3 Corrosion and infrastructure interactions (EET with solids)
Electroactive respiration principles extend to microbial interactions with elemental iron and electrodes; Hou et al. discuss SRB implications including corrosion and altered mobility of toxic metals, and note that some SRB can harvest extracellular electrons from solid substrates. (hou2025cooccurrenceofdirect pages 1-2)

### 4) Expert opinions and analysis from authoritative sources (interpreting the evidence)

**Consensus mechanistic framing:** Authoritative recent syntheses emphasize that DMR of insoluble Fe(III)/Mn(IV) depends on EET that can be **direct** (outer-surface multiheme cytochromes; porin–cytochrome conduits; nanowires/filaments) or **indirect** (secreted or added redox mediators). For *Shewanella*, review evidence summarizes porin–cytochrome complexes as core: “mtrB…required for Fe(III) and Mn(IV) reduction,” with mtrA and mtrC essential for reducing iron and manganese minerals. (soares2025toolsforenhancing pages 5-8)

**Electron-shuttling as a functional extension of DMR:** In *Shewanella*, electron shuttling allows reduction of physically sequestered Fe(III) oxides; the identity of a produced shuttle “was determined to be flavins,” and “adding flavins…enhances the reduction rate” of electrodes or Fe(III) oxides, supporting a causal edge from flavin production to increased apparent DMR rate in diffusion-limited settings. (soares2025toolsforenhancing pages 5-8)

**Assay-/substrate-specific pathways (warning for curation):** The electrode-essential role of ExtABCD “only on electrodes” indicates that some conduits are specialized for electrode respiration rather than generalized mineral reduction. TraitMech curation should mark these as assay-contextual rather than universal DMR components. (portela2024widespreadextracellularelectron pages 2-3)

### 5) Relevant statistics and data from recent studies

**Electrochemical and kinetic constraints (2024):**
- OmcS nanowire midpoint potential: Eapp = −130 ± 13 mV; redox window 360 mV (−0.31 to 0.05 V). (portela2024widespreadextracellularelectron pages 2-3)
- Periplasmic compartment size constraints cited: periplasm >40 nm; direct electron transfer limited to ~1.5 nm; cellular EET >10^6 s−1 vs periplasmic diffusion <10^5 s−1; OmcS nanowires ~200 monomers; would require >2000 periplasmic monomers to match rates under simple diffusion assumptions. (portela2024widespreadextracellularelectron pages 2-3)

**Environmental statistics relevant to DMR niches (2024):**
- Deep subsurface brines: conductivity 102–174 mS/cm (2–3× seawater), flow ~1.1–3.4 mL/s; redox potential −200 to −500 mV; site depth 713 m. (hsu2024isolationandgenomic pages 1-2)

**BES performance statistics (recent syntheses):**
- SRB MFC power density range: 0.013–0.68 W/m2. (hou2025cooccurrenceofdirect pages 1-2)
- Single-cell EET measurement (planktonic *Shewanella*): 0.05–2.8 fA/cell. (soares2025toolsforenhancing pages 5-8)
- Examples of enhanced MFC/BES performance (reviewed): maximum power density 5.07 W/m2; Mo-doped carbon nanofibers power density 1287.38 mW/m2; optimized *Shewanella* DET current density 673 mA/m2. (soares2025toolsforenhancing pages 12-13)

---

## Curation-Focused Outputs for TraitMech Graph

### Scope summary (for YAML header)
Dissimilatory metal reduction (traitmech:000039) should be curated as an **anaerobic, energy-conserving respiratory phenotype** where electrons from donor oxidation are exported via EET machinery to terminal metal acceptors (Fe(III), Mn(IV)), including insoluble oxides and (in assays) soluble chelates, and sometimes to electrodes as a proxy acceptor. (hsu2024isolationandgenomic pages 1-2, jiang2019advancesinfe(iii) pages 1-3, jiang2019advancesinfe(iii) pages 3-4)

### Candidate nodes (grouped)

**Pathways / modules (label nodes unless curated in an external pathway DB):**
- Extracellular electron transfer (EET) (GO label suggestion: extracellular electron transfer; no GO CURIE supplied in sources)
- Direct electron transfer (DET) vs indirect/mediated EET (MET)
- Anaerobic respiration using Fe(III)/Mn(IV) as terminal electron acceptors

**Genes / proteins / complexes (taxon-specific grounding suggested as label-only in this pass):**
- *Shewanella* porin–cytochrome conduit: MtrCAB (mtrB β-barrel; mtrA decaheme; mtrC surface decaheme), plus OmcA/MtrF mentioned in review context (label-only). (soares2025toolsforenhancing pages 5-8)
- *Geobacter* periplasmic cytochromes: PpcA, PpcB, PpcC, PpcD, PpcE (PpcABCDE). (portela2024widespreadextracellularelectron pages 2-3)
- *Geobacter* nanowires: OmcS (and OmcZ referenced as electrode growth/electricity). (portela2024widespreadextracellularelectron pages 2-3)
- *Geobacter* outer-membrane conduits: ExtABCD (electrode-specific essentiality). (portela2024widespreadextracellularelectron pages 2-3)
- Pili/filaments involved in electrode attachment/EET (label-only; demonstrated in SRB). (hou2025cooccurrenceofdirect pages 1-2)

**Chemicals / electron donors / acceptors:**
- Electron donors: acetate (CHEBI:30089), lactate (label-only in these excerpts), hydrogen (CHEBI:18276). (hsu2024isolationandgenomic pages 1-2, hou2025cooccurrenceofdirect pages 1-2)
- Electron acceptors: Fe(III) (CHEBI:63046), Mn(IV) (CHEBI:18291); Fe(III) oxide (label-only), Fe(III)-citrate (label-only). (soares2025toolsforenhancing pages 5-8, hsu2024isolationandgenomic pages 1-2)
- Electron shuttles: flavins (CHEBI:17621; includes FMN and riboflavin as described). (soares2025toolsforenhancing pages 5-8)

**Environmental / experimental factors:**
- Anoxia; reduced redox potentials (e.g., −200 to −500 mV in subsurface brines). (hsu2024isolationandgenomic pages 1-2)
- Substrate physical state: insoluble/crystalline Fe(III) minerals vs soluble Fe(III) chelates; electrodes as solid acceptors. (portela2024widespreadextracellularelectron pages 2-3, jiang2019advancesinfe(iii) pages 3-4)

**Applications:**
- Microbial fuel cells (MFCs); wastewater treatment; electrode-based enrichments. (hou2025cooccurrenceofdirect pages 1-2)
- Groundwater remediation via stimulating Fe(III) bioreduction. (jiang2019advancesinfe(iii) pages 1-3)

### Evidence-backed causal edges (table)
The following artifact provides candidate subject–predicate–object triples, each with a verbatim snippet, DOI-first reference, and uncertainty notes.

| Edge (S–P–O) | Edge type | Grounding suggestions | Supporting snippet (verbatim quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| acetate oxidation — coupled to — Fe(III) citrate reduction | process / assay | CHEBI:30089 acetate; CHEBI:63046 ferric cation; label-only: Fe(III) citrate reduction | “a novel Gram-positive bacterium was enriched under **anaerobic, acetate-oxidizing, and Fe(III) citrate-reducing conditions**.” (hsu2024isolationandgenomic pages 1-2) | Hsu et al., 2024. DOI:10.1128/aem.00044-24. https://doi.org/10.1128/aem.00044-24 | Strong assay evidence for coupling in enrichment; soluble Fe(III)-citrate is an assay proxy and may not capture insoluble-mineral reduction breadth. |
| organic compounds oxidation — donates electrons to — Fe(III) reduction | process | label-only: organic compounds oxidation; CHEBI:63046 ferric cation; CHEBI:29033 ferrous cation | “**FeRB transfers the electrons to Fe(III), Fe(III) is reduced to Fe(II), and organic compounds are mineralized**” (jiang2019advancesinfe(iii) pages 3-4) | Jiang et al., 2019. DOI:10.1007/s11783-019-1173-9. https://doi.org/10.1007/s11783-019-1173-9 | General FeRB statement; supports core respiratory coupling but not a single named donor. |
| hydrogen — serves as electron donor for — sulfate-reducing bacteria extracellular/electroactive respiration | process | CHEBI:18276 hydrogen; label-only: sulfate-reducing bacteria | “**SRB can utilize organic compounds and gases (e.g., hydrogen) as electron donors**” (hou2025cooccurrenceofdirect pages 1-2) | Hou et al., 2025. DOI:10.1128/spectrum.01226-24. https://doi.org/10.1128/spectrum.01226-24 | Indirectly relevant to metal reduction trait because same donor logic applies to anaerobic respiration/EET; taxon is SRB, not canonical FeRB. Mark as broader anaerobic-respiration evidence. |
| MtrB — required for — Fe(III) and Mn(IV) reduction | molecular | label-only: mtrB; CHEBI:63046 ferric cation; CHEBI:18291 manganese(4+) | “**mtrB, which encodes an outer membrane β-barrel protein required for Fe (III) and Mn (IV) reduction**.” (soares2025toolsforenhancing pages 5-8) | Soares et al., 2025. DOI:10.3390/fermentation11070381. https://doi.org/10.3390/fermentation11070381 | Strong review summary of genetic evidence in *Shewanella*; appropriate for a taxon-specific edge. |
| MtrA/MtrC — essential for reducing — iron and manganese minerals | molecular | label-only: MtrA; label-only: MtrC; label-only: iron minerals; label-only: manganese minerals | “The same genetic locus contains **mtrA**, encoding a decaheme c-type cytochrome, and **mtrC** … These proteins are **essential for reducing iron and manganese minerals**.” (soares2025toolsforenhancing pages 5-8) | Soares et al., 2025. DOI:10.3390/fermentation11070381. https://doi.org/10.3390/fermentation11070381 | Good support for MtrCAB-mediated EET to metal oxides; taxon-specific to *Shewanella*. |
| MtrCAB complex — creates pathway transferring electrons to — extracellular acceptor | molecular / process | label-only: MtrCAB complex; GO:0009055 electron transfer activity; label-only: extracellular acceptor | “S. oneidensis utilizes … **the outer membrane complex MtrCAB** (15) to create a **pathway that transfers electrons to an extracellular acceptor**.” (hsu2024isolationandgenomic pages 1-2) | Hsu et al., 2024. DOI:10.1128/aem.00044-24. https://doi.org/10.1128/aem.00044-24 | Supports generalized EET conduit role; source is background text in primary paper. |
| PpcA-E — transiently bind to — OmcS nanowires | molecular | label-only: PpcA; label-only: PpcB; label-only: PpcC; label-only: PpcD; label-only: PpcE; label-only: OmcS nanowire | “**all major periplasmic triheme cytochromes PpcABCDE (PpcA-E) transiently bind to hexaheme OmcS nanowires to transfer electrons**” (portela2024widespreadextracellularelectron pages 2-3) | Portela et al., 2024. DOI:10.1038/s41467-024-46192-0. https://doi.org/10.1038/s41467-024-46192-0 | Strong recent primary evidence; highly suitable for curation. |
| PpcA-E — transfer electrons to — OmcS nanowires | molecular / process | label-only: PpcABCDE; label-only: OmcS nanowires; GO:0009055 electron transfer activity | “all major periplasmic triheme cytochromes PpcABCDE (PpcA-E) transiently bind to hexaheme OmcS nanowires **to transfer electrons**” (portela2024widespreadextracellularelectron pages 2-3) | Portela et al., 2024. DOI:10.1038/s41467-024-46192-0. https://doi.org/10.1038/s41467-024-46192-0 | Mechanistically stronger than generic periplasmic relay models because direct transfer was experimentally shown. |
| ExtABCD — essential for growth on — electrodes | assay / molecular | label-only: ExtABCD complex; ENVO:01000635 electrode | “among which **ExtABCD are essential in bacterial growth only on electrodes**” (portela2024widespreadextracellularelectron pages 2-3) | Portela et al., 2024. DOI:10.1038/s41467-024-46192-0. https://doi.org/10.1038/s41467-024-46192-0 | Strong but assay-specific; should not be overgeneralized to Fe(III)/Mn(IV) minerals. |
| flavins — facilitate electron transfer to — distant Fe(III) substrates | molecular / process | CHEBI:17621 flavin; CHEBI:63046 ferric cation | “**the redox-active small molecules facilitate electron transfer to substrates distant from the cell surface** … The identity of one electron shuttle produced by Shewanella was determined to be **flavins**.” (soares2025toolsforenhancing pages 5-8) | Soares et al., 2025. DOI:10.3390/fermentation11070381. https://doi.org/10.3390/fermentation11070381 | Strong review support for mediated EET; especially relevant where metal oxides are spatially inaccessible. |
| flavins — enhance reduction rate of — electrodes or Fe(III) oxides | molecular / assay | CHEBI:17621 flavin; ENVO:01000635 electrode; label-only: Fe(III) oxides | “**Adding flavins to cells, reducing electrodes or Fe (III) oxides, enhances the reduction rate**.” (soares2025toolsforenhancing pages 5-8) | Soares et al., 2025. DOI:10.3390/fermentation11070381. https://doi.org/10.3390/fermentation11070381 | Strong evidence for mediated EET; applies to assay and environmental mineral contexts. |
| pili-like filaments — facilitate extracellular electron transfer to — electrode | molecular / assay | label-only: pili; GO:0022900 electron transport chain; ENVO:01000635 electrode | “DvH utilized **filaments that resemble pili** to attach to electrodes and **facilitate extracellular electron transfer from cell to cell and to the electrode**.” (hou2025cooccurrenceofdirect pages 1-2) | Hou et al., 2025. DOI:10.1128/spectrum.01226-24. https://doi.org/10.1128/spectrum.01226-24 | Useful support for pili-mediated direct EET; taxon-specific and electrode-assay specific. |
| deletion of major pilus gene — decreases — extracellular electron transfer / current production | molecular / assay | label-only: major pilus-producing gene; label-only: current production | “The mutant with a deletion of the major pilus-producing gene **yielded less voltage and far less attachment** … **suggesting the importance of pili in extracellular electron transfer**.” (hou2025cooccurrenceofdirect pages 1-2) | Hou et al., 2025. DOI:10.1128/spectrum.01226-24. https://doi.org/10.1128/spectrum.01226-24 | Strong perturbational evidence, but in SRB/electrode context rather than direct Fe/Mn mineral reduction. |
| OmcS nanowires — required to eliminate respiratory electrons via EET to — Fe(III) oxide | molecular / process | label-only: OmcS nanowires; label-only: Fe(III) oxide | “G. sulfurreducens **requires nanowires of cytochrome OmcS to eliminate respiratory electrons via EET to soil-abundant Fe(III) oxide**” (portela2024widespreadextracellularelectron pages 2-3) | Portela et al., 2024. DOI:10.1038/s41467-024-46192-0. https://doi.org/10.1038/s41467-024-46192-0 | Strong recent primary evidence; central edge for insoluble Fe(III) oxide reduction. |
| closely stacked hemes in nanowires — promote — rapid long-range electron conduction | molecular | label-only: stacked hemes; label-only: cytochrome nanowire; GO:0009055 electron transfer activity | “Such **closely stacked hemes can promote rapid and insulated electron conduction over distances of several micrometers**” (portela2024widespreadextracellularelectron pages 2-3) | Portela et al., 2024. DOI:10.1038/s41467-024-46192-0. https://doi.org/10.1038/s41467-024-46192-0 | Supports mechanistic basis of nanowire conductivity; molecular-structure edge. |
| anoxic, reduced subsurface brines — provide environment for — metal-reducing organisms | environment | ENVO:00002007 sediment groundwater/brine (approx.); label-only: anoxic reduced brine | “the downward boreholes … have actively flowing brine waters … **anoxic, and reduced (−200 to −500 mV)**” (hsu2024isolationandgenomic pages 1-2) | Hsu et al., 2024. DOI:10.1128/aem.00044-24. https://doi.org/10.1128/aem.00044-24 | Strong environmental context; useful for trait ecological preference. |
| oxidized, insoluble metals — can serve as respiratory substrate for — extracellular electron transfer-capable microbes | environment / process | label-only: oxidized insoluble metals; label-only: respiratory substrate | “**oxidized, insoluble metals are an abundant electron acceptor that microbes could potentially utilize as a respiratory substrate**.” (hsu2024isolationandgenomic pages 1-2) | Hsu et al., 2024. DOI:10.1128/aem.00044-24. https://doi.org/10.1128/aem.00044-24 | Strong trait-defining statement for metal reduction as respiration. |
| Fe(III) reduction — occurs under — anaerobic subsurface conditions with insoluble/crystalline Fe(III) | environment | CHEBI:63046 ferric cation; ENVO:00002006 subsurface environment | “**Fe(III) has a solubility of approximately 10–9 M at neutral pH and is generally present as insoluble or crystalline forms under anaerobic subsurface environments**” (jiang2019advancesinfe(iii) pages 3-4) | Jiang et al., 2019. DOI:10.1007/s11783-019-1173-9. https://doi.org/10.1007/s11783-019-1173-9 | Good environmental/chemical constraint; especially relevant to insoluble-mineral assays. |
| microbial fuel cells — use microbes to convert chemical energy of organics into — electricity | application | label-only: microbial fuel cell; label-only: electricity generation | “**Microbial fuel cells (MFCs) have been used as a promising technology for electrical energy generation, which uses microbes to transfer the chemical energy of organic compounds into electricity**” (hou2025cooccurrenceofdirect pages 1-2) | Hou et al., 2025. DOI:10.1128/spectrum.01226-24. https://doi.org/10.1128/spectrum.01226-24 | Application edge; broader than metal reduction but directly leverages EET mechanisms shared with metal reducers. |
| sulfate-reducing bacteria cultured in MFCs — achieve removal of — sulfate and organic compounds with electricity production | application | label-only: sulfate-reducing bacteria; label-only: sulfate-containing wastewater; label-only: electricity production | “**By culturing SRB in MFCs, previous studies have achieved the removal of sulfate and organic compounds with electricity production**” (hou2025cooccurrenceofdirect pages 1-2) | Hou et al., 2025. DOI:10.1128/spectrum.01226-24. https://doi.org/10.1128/spectrum.01226-24 | Application evidence for wastewater treatment; not specific to Fe/Mn reduction but relevant to electroactive respiration implementations. |
| dissimilatory metal reducers — can reduce soluble toxic metals to less soluble forms enabling — bioremediation | application | label-only: dissimilatory metal reducers; CHEBI:22908 uranium; CHEBI:30514 chromium | “**Soluble toxic metal species like UVI or CrVI can be reduced by DMRs, forming species with reduced solubility which precipitate**” (nash2025thestructureand pages 20-25) | Nash, 2025. DOI not available in current context. URL not available in current context. | Useful remediation edge, but source metadata are incomplete in current context and statement is in a review/summary; curate with caution or replace with primary source later. |


*Table: This table lists curation-ready subject–predicate–object edges for dissimilatory metal reduction, supported only by evidence already present in context. It highlights mechanistic, environmental, assay, and application relationships that can seed a TraitMech causal graph while flagging taxon-specific or assay-specific uncertainties.*

### Figure evidence (visual)
A schematic of the *Geobacter* EET pathway including periplasmic cytochromes (PpcA–E) and OmcS nanowires, plus a docking model of PpcA binding OmcS, is available from Portela et al. (2024). (portela2024widespreadextracellularelectron media 6c43b966)

---

## Warnings / curation cautions (do not over-curate)

1. **Electrode-specific genes are not necessarily mineral-reduction genes.** ExtABCD being “essential…only on electrodes” should be represented as an assay-contextual edge (electrode respiration) rather than universal Fe(III)/Mn(IV) oxide reduction. (portela2024widespreadextracellularelectron pages 2-3)
2. **Taxon specificity.** MtrCAB-based edges are strongly supported for *Shewanella* but should not be generalized to Gram-positive reducers or all FeRB. (soares2025toolsforenhancing pages 5-8, hsu2024isolationandgenomic pages 1-2)
3. **Soluble Fe(III) chelates are proxies.** Fe(III)-citrate reduction assays (used for MK1 enrichment) support DMR capacity but may not imply competence on insoluble minerals without additional evidence. (hsu2024isolationandgenomic pages 1-2)
4. **Some application statements require stronger primary sourcing.** A remediation precipitating-U/Cr statement was identified in a review-like source with incomplete bibliographic metadata in the available context; it should be replaced or corroborated with a DOI-resolved primary/authoritative review before curation. (nash2025thestructureand pages 20-25)

---

## DOI-first bibliography (with dates/URLs where available)

1. **Portela PC, Shipps CC, Shen C, et al.** Widespread extracellular electron transfer pathways for charging microbial cytochrome OmcS nanowires via periplasmic cytochromes PpcABCDE. *Nature Communications*. **2024-03**. DOI: **10.1038/s41467-024-46192-0**. https://doi.org/10.1038/s41467-024-46192-0 (portela2024widespreadextracellularelectron pages 2-3)
2. **Hsu D, Flynn JR, Schuler CJ, et al.** Isolation and genomic analysis of “*Metallumcola ferriviriculae*” MK1, a Gram-positive, Fe(III)-reducing bacterium from the Soudan Underground Mine, an iron-rich Martian analog site. *Applied and Environmental Microbiology*. Published **2024-07-15** (accepted 2024-06-18). DOI: **10.1128/aem.00044-24**. https://doi.org/10.1128/aem.00044-24 (hsu2024isolationandgenomic pages 1-2)
3. **Hou L, Cortez R, Hagerman M, Hu Z, Majumder EL-W.** Co-occurrence of direct and indirect extracellular electron transfer mechanisms during electroactive respiration in a dissimilatory sulfate reducing bacterium. *Microbiology Spectrum*. Published **2024-12-05** (issue Jan 2025). DOI: **10.1128/spectrum.01226-24**. https://doi.org/10.1128/spectrum.01226-24 (hou2025cooccurrenceofdirect pages 1-2)
4. **Soares KAA, Silva JAS, Wang X, Bueno AV, Lobo FLL.** Tools for Enhancing Extracellular Electron Transfer in Bioelectrochemical Systems: A Review. *Fermentation*. **2025-06**. DOI: **10.3390/fermentation11070381**. https://doi.org/10.3390/fermentation11070381 (soares2025toolsforenhancing pages 5-8, soares2025toolsforenhancing pages 12-13, soares2025toolsforenhancing pages 2-4)
5. **Jiang Y, Xi B, Li R, et al.** Advances in Fe(III) bioreduction and its application prospect for groundwater remediation: A review. *Frontiers of Environmental Science & Engineering*. **2019-11**. DOI: **10.1007/s11783-019-1173-9**. https://doi.org/10.1007/s11783-019-1173-9 (jiang2019advancesinfe(iii) pages 1-3, jiang2019advancesinfe(iii) pages 3-4)

(Additional sources were present in context but were not essential for the core curated edges.)


References

1. (hsu2024isolationandgenomic pages 1-2): David Hsu, Jack R. Flynn, Christopher J. Schuler, Cara M. Santelli, Brandy M. Toner, Daniel R. Bond, and Jeffrey A. Gralnick. Isolation and genomic analysis of “ <i>metallumcola ferriviriculae”</i> mk1, a gram-positive, fe(iii)-reducing bacterium from the soudan underground mine, an iron-rich martian analog site. Applied and Environmental Microbiology, Aug 2024. URL: https://doi.org/10.1128/aem.00044-24, doi:10.1128/aem.00044-24. This article has 9 citations and is from a peer-reviewed journal.

2. (jiang2019advancesinfe(iii) pages 3-4): Yu Jiang, Beidou Xi, Rui Li, Mingxiao Li, Zheng Xu, Yuning Yang, and Shaobo Gao. Advances in fe(iii) bioreduction and its application prospect for groundwater remediation: a review. Frontiers of Environmental Science & Engineering, 13:1-11, Nov 2019. URL: https://doi.org/10.1007/s11783-019-1173-9, doi:10.1007/s11783-019-1173-9. This article has 42 citations and is from a peer-reviewed journal.

3. (soares2025toolsforenhancing pages 5-8): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 16 citations.

4. (hou2025cooccurrenceofdirect pages 1-2): Liyuan Hou, Rebecca Cortez, Michael Hagerman, Zhiqiang Hu, and Erica L.-W. Majumder. Co-occurrence of direct and indirect extracellular electron transfer mechanisms during electroactive respiration in a dissimilatory sulfate reducing bacterium. Jan 2025. URL: https://doi.org/10.1128/spectrum.01226-24, doi:10.1128/spectrum.01226-24. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (jiang2019advancesinfe(iii) pages 1-3): Yu Jiang, Beidou Xi, Rui Li, Mingxiao Li, Zheng Xu, Yuning Yang, and Shaobo Gao. Advances in fe(iii) bioreduction and its application prospect for groundwater remediation: a review. Frontiers of Environmental Science & Engineering, 13:1-11, Nov 2019. URL: https://doi.org/10.1007/s11783-019-1173-9, doi:10.1007/s11783-019-1173-9. This article has 42 citations and is from a peer-reviewed journal.

6. (portela2024widespreadextracellularelectron pages 2-3): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.

7. (portela2024widespreadextracellularelectron media 6c43b966): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.

8. (soares2025toolsforenhancing pages 12-13): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 16 citations.

9. (nash2025thestructureand pages 20-25): BW Nash. The structure and function of extracellular redox enzymes. Unknown journal, 2025.

10. (soares2025toolsforenhancing pages 2-4): Kaline Araújo Soares, Jhoni Anderson Schembek Silva, Xin Wang, André Valente Bueno, and Fernanda Leite Lobo. Tools for enhancing extracellular electron transfer in bioelectrochemical systems: a review. Fermentation, 11:381, Jun 2025. URL: https://doi.org/10.3390/fermentation11070381, doi:10.3390/fermentation11070381. This article has 16 citations.