---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:33:22.141245'
end_time: '2026-06-18T04:57:34.252062'
duration_seconds: 1452.11
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory iron reduction
  trait_identifier: traitmech:000031
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_iron_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism conserves energy
    for growth by coupling the oxidation of organic matter or hydrogen to the reduction
    of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella,
    often via extracellular electron transfer.
  parent_traits: traitmech:000039
  synonyms: ferric iron respiration, dissimilatory Fe(III) reduction
  evidence_summary: 'DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter
    coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical
    reactions in aquatic sediments, soils, and groundwater (Lovley review establishes
    dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration
    coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson
    & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and
    Mn(IV) as terminal electron acceptors competitive with nitrate.)'
  causal_graph_summary: 'dir_ferric_iron_respiration: 3 nodes, 2 edges'
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
- **Trait label:** dissimilatory iron reduction
- **METPO identifier:** traitmech:000031
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella, often via extracellular electron transfer.
- **Parent traits:** traitmech:000039
- **Synonyms:** ferric iron respiration, dissimilatory Fe(III) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and Mn(IV) as terminal electron acceptors competitive with nitrate.)
- **Existing causal graph summary:** dir_ferric_iron_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory iron reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_iron_reduction.yaml`.

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
- **Trait label:** dissimilatory iron reduction
- **METPO identifier:** traitmech:000031
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella, often via extracellular electron transfer.
- **Parent traits:** traitmech:000039
- **Synonyms:** ferric iron respiration, dissimilatory Fe(III) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and Mn(IV) as terminal electron acceptors competitive with nitrate.)
- **Existing causal graph summary:** dir_ferric_iron_respiration: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **dissimilatory iron reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_iron_reduction.yaml`.

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


# Microbial Trait Causal Graph Curation Report

## Target trait
- **Trait label:** dissimilatory iron reduction (DIR)
- **METPO identifier:** traitmech:000031
- **Trait category:** METABOLISM
- **Term kind:** CLASS

## 1) Scope summary (trait meaning and boundaries)

### Core definition (current understanding)
DIR is best treated as an **energy-conserving anaerobic respiratory metabolism** in which microorganisms **use Fe(III) as a terminal electron acceptor** and couple it to oxidation of organic substrates (and in some settings H2), producing extracellular Fe(II). Lovley’s foundational review emphasized that microorganisms were discovered that can “obtain energy for growth by completely oxidizing organic compounds to CO2 with Fe(III)… as the sole acceptor,” and that “the oxidation of organic matter coupled to the reduction of Fe(III)… is the direct result of the enzymatic activity of specialized microorganisms.” (lovley1991dissimilatoryfe(iii)and pages 2-3, lovley1991dissimilatoryfe(iii)and pages 6-7)

A modern environmental framing is consistent: in anoxic settings, “dissimilatory Fe(III)-reducing bacteria utilize Fe(III) as an electron acceptor during their energy metabolism.” (shi2024responseoffe(iii)reducing pages 1-2)

### Boundary cases (what DIR is not)
1. **Assimilatory Fe(III) reduction (iron uptake) vs DIR:** Lovley distinguished dissimilatory reduction from assimilatory reduction in that dissimilatory reduction yields “appreciable extracellular Fe(II)… whereas assimilatory reduction incorporates metal into cellular components.” (lovley1991dissimilatoryfe(iii)and pages 2-3)
2. **Non-enzymatic/abiotic Fe(III) reduction vs DIR:** Historically, much Fe(III) reduction in sediments was attributed to “nonenzymatic processes,” but Lovley argues respiratory DIR is enzymatic and linked to energy conservation and CO2 production (lovley1991dissimilatoryfe(iii)and pages 1-2, lovley1991dissimilatoryfe(iii)and pages 10-10).
3. **Fermentative Fe(III) reduction vs DIR:** Fermenters can reduce Fe(III) as an electron sink without it being the main energy-conserving terminal electron accepting process; Lovley explicitly separates “Fermentative Fe(III)… Reducers” from specialized Fe(III)-respiring organisms that completely oxidize substrates to CO2 (lovley1991dissimilatoryfe(iii)and pages 1-2).

### Assay/phenotype interpretation for curation
DIR is often observed experimentally as:
- **Growth or electron flux linked to Fe(III) reduction** (Fe(II) accumulation) under anoxic conditions (lovley1991dissimilatoryfe(iii)and pages 6-7, schwarz2024lackofphysiological pages 1-2).
- **Extracellular electron transfer (EET)** machinery engagement when Fe(III) is insoluble (Fe(III) oxides), requiring electron export beyond the cell envelope (schwarz2024lackofphysiological pages 1-2, portela2024widespreadextracellularelectron pages 1-2).

## 2) Key mechanistic entities (candidate nodes)

### A. Pathways / modules (label-only if not grounded)
- Dissimilatory Fe(III) respiration / anaerobic respiration using Fe(III) (lovley1991dissimilatoryfe(iii)and pages 2-3, shi2024responseoffe(iii)reducing pages 1-2)
- Extracellular electron transfer (EET) (portela2024widespreadextracellularelectron pages 1-2, fessler2023conjugativeplasmidsinhibit pages 1-2)
- Direct interspecies electron transfer (DIET) (portela2024widespreadextracellularelectron pages 1-2)
- “Nanowire-charging pathway” (periplasm → outer-surface nanowire) (portela2024widespreadextracellularelectron pages 7-9)

### B. Genes / proteins / complexes
**Geobacter (model DIR/EET system)**
- **PilA** (type IV pilin; e-pili) (schwarz2024lackofphysiological pages 1-2)
- **OmcS** (cytochrome nanowire) (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9)
- **PpcA/B/C/D/E** (periplasmic cytochromes injecting electrons into OmcS) (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9)
- **OmcE, OmcZ** (filament-forming cytochromes discussed as not required for Fe(III) oxide reduction in one physiological reassessment) (schwarz2024lackofphysiological pages 1-2)
- **OmcB (porin–cytochrome complex)** (essential conduit component in the physiological reassessment context) (schwarz2024lackofphysiological pages 4-8)

**Shewanella (facultative anaerobe with broad metal reduction)**
- **MtrCAB complex:** MtrA (periplasmic decaheme), MtrB (outer membrane porin), MtrC (cell-surface decaheme cytochrome) (norman2023acysteinepair pages 1-2)
- **OmcA** (outer membrane cytochrome, functionally linked to extracellular Fe oxide reduction) (norman2023acysteinepair pages 1-2)
- **MtrC CX8C motif / redox-active disulfide** controlling FMN interaction and ROS risk at oxic/anoxic transitions (norman2023acysteinepair pages 1-2)

### C. Chemicals / electron donors / acceptors / mediators
- **Electron donors:** organic matter/organic compounds (Lovley review), H2 (sediment coupling claims) (lovley1991dissimilatoryfe(iii)and pages 2-3, lovley1991dissimilatoryfe(iii)and pages 6-7)
- **Terminal electron acceptor:** Fe(III) (trait-defining) (shi2024responseoffe(iii)reducing pages 1-2)
- **Insoluble acceptors:** Fe(III) oxide minerals (e.g., “soil-abundant Fe(III) oxide”) (portela2024widespreadextracellularelectron pages 1-2)
- **Soluble Fe(III) complexes:** Fe(III)-citrate, Fe(III)-EDTA (shi2024responseoffe(iii)reducing pages 1-2)
- **Flavins:** FMN and secreted flavins (nanomolar) as shuttles/cofactors in Shewanella EET/Fe reduction (norman2023acysteinepair pages 1-2)
- **Soluble iron as mediator/shuttle:** Fe3+/Fe2+ cycling as redox shuttle (electrode-associated inward EET context) (abuyen2023solubleironenhances pages 6-8)

### D. Environmental / experimental factors
- **Anoxic / oxygen-limited conditions** induce/enable EET-based respiration; oxygen exposure creates ROS risk (norman2023acysteinepair pages 1-2)
- **Fe(III) phase/speciation:** dissolved Fe(III)-OM complexes vs solid minerals; influences kinetics and community composition (shi2024responseoffe(iii)reducing pages 1-2)
- **Conjugative plasmid carriage** (pKJK5, RP4, pB10) impacting EET phenotype (fessler2023conjugativeplasmidsinhibit pages 1-2)

## 3) Recent developments (prioritize 2023–2024)

### 3.1 Geobacter: defined periplasm-to-nanowire electron injection pathway (2024)
Portela et al. (Nature Communications, published 2024; received Aug 2023, accepted Feb 2024) explicitly identify a minimal “nanowire-charging” mechanism: “Geobacter sulfurreducens periplasmic cytochromes PpcABCDE inject electrons directly into OmcS nanowires by binding transiently,” with “the least-abundant cytochrome (PpcC) showing the highest efficiency.” (portela2024widespreadextracellularelectron pages 1-2)

They frame a kinetic/biophysical constraint and motivate the mechanism by a striking rate mismatch: microbes can “wire electrons rapidly (>10^6 s−1)” despite “slow (<10^5 s−1) electron diffusion among periplasmic cytochromes.” (portela2024widespreadextracellularelectron pages 1-2)

Quantitative electrochemical/statistical parameters reported include:
- “OmcS heme reduction potentials… with a midpoint 82 mV-higher than reported previously” (portela2024widespreadextracellularelectron pages 1-2)
- “physiological OmcS nanowires have a midpoint potential of −130 mV” (portela2024widespreadextracellularelectron pages 7-9)

### 3.2 Reassessment of Geobacter long-range conduits (2024)
Schwarz et al. (mBio, published 2 Apr 2024) argue that Fe(III) oxide reduction is a key functional assay for long-range EET and conclude: “The results are consistent with the concept that 3 nm diameter electrically conductive pili (e-pili) are required for G. sulfurreducens long-range extracellular electron transfer.” (schwarz2024lackofphysiological pages 1-2)

They provide quantitative and phenotype-linked statements relevant for edges:
- “OmcS filaments accounted for… only ca. 10% of the filaments emanating from wild-type… cells” (schwarz2024lackofphysiological pages 8-11)
- In cytochrome-filament-deletion backgrounds, “Fe(III) oxide reduction was inhibited when the pilin gene… was modified to yield poorly conductive 3 nm diameter filaments.” (schwarz2024lackofphysiological pages 1-2)

### 3.3 Shewanella: oxygen/ROS management integrated with EET (2023)
Norman et al. (mBio; published 16 Jan 2023) show an EET safety/regulation mechanism during oxic transitions. They state:
- Under anoxic conditions, S. oneidensis uses Mtr for EET: “the Mtr complex… consists of… MtrA… MtrB… and… MtrC on the surface of the cell” (norman2023acysteinepair pages 1-2)
- “deletion of both MtrC and the analogous OmcA prevents the reduction of extracellular iron oxides” (norman2023acysteinepair pages 1-2)
- Iron oxide reduction depends on mediators: “iron reduction… is also dependent on the secretion of nanomolar concentrations of flavins” (norman2023acysteinepair pages 1-2)
- Control node: “FMN reduction… is controlled by the redox-active disulfide on the cytochrome surface. In the presence of oxygen, the disulfide forms, lowering the affinity for FMN and decreasing the rate of peroxide formation.” (norman2023acysteinepair pages 1-2)

### 3.4 Soluble iron as an electron-transfer mediator in bioelectrochemical contexts (2023)
Abuyen & El-Naggar (ChemElectroChem; published Jan 2023) provide quantitative perturbation evidence in inward EET (electrode-to-cell) that is mechanistically adjacent to DIR/EET:
- “MtrC and OmcA… primary cell surface conduits” for soluble-iron-mediated inward EET (abuyen2023solubleironenhances pages 6-8)
- Knockouts reduce current: ΔmtrC and ΔomcA currents “37% and 42% lower” than wild-type; ΔmtrC/omcA “about 73% less”; ΔOMC “about 96% lower” (abuyen2023solubleironenhances pages 6-8)
- Mechanism: “freely diffusing ions acting as redox shuttles, where Fe3+/Fe2+ is continuously oxidized/reduced by the cells/electrodes” (abuyen2023solubleironenhances pages 6-8)

### 3.5 Environmental Fe(III) form controls kinetics and community outcomes (2024)
Shi et al. (Biogeochemistry; published online 15 Oct 2024) report lake sediment microcosms amended with ferrihydrite vs dissolved Fe(III) complexes:
- “sediments amended with Fe(III)-citrate and Fe(III)-EDTA exhibited faster Fe(III) reduction rates… compared to those amended with ferrihydrite.” (shi2024responseoffe(iii)reducing pages 1-2)
- “the reduction rates of dissolved Fe(III)-OM complexes are significantly higher than those observed for solid Fe(III) minerals” (shi2024responseoffe(iii)reducing pages 1-2)
- Phenotypic boundary: “the flagella and pili of Geobacter metallireducens are not expressed when cultured with Fe(III)-citrate” (shi2024responseoffe(iii)reducing pages 1-2)

### 3.6 Horizontal gene transfer elements can suppress EET phenotypes (2023)
Fessler et al. (Frontiers in Microbiology; published 17 Mar 2023) report that conjugative plasmids alter the DIR/EET phenotype in Geobacter:
- “electrically conductive nanowires that link internal electron flow from metabolism to solid electron acceptors” (fessler2023conjugativeplasmidsinhibit pages 1-2)
- plasmid carriage causes “reduces insoluble iron oxides at much slower rates” (fessler2023conjugativeplasmidsinhibit pages 1-2)
- transcriptomics: “presence of pKJK5 reduces transcription of… including pilA and omcE” (fessler2023conjugativeplasmidsinhibit pages 1-2)

## 4) Current applications / real-world implementations

DIR and associated EET underpin:
- **Biogeochemical Fe cycling in sediments/soils/groundwater** (Lovley review; modern sediment microcosms) (lovley1991dissimilatoryfe(iii)and pages 1-2, shi2024responseoffe(iii)reducing pages 1-2)
- **Microbial electrochemical systems (electrodes as acceptors/donors)**: Geobacter’s electron exchange with “iron oxides and electrodes” and relevance to “microbial electrochemical systems” is highlighted (fessler2023conjugativeplasmidsinhibit pages 1-2); electrode-linked inward EET is explored for electrosynthesis-relevant contexts (abuyen2023solubleironenhances pages 6-8).
- **Bioremediation potential**: Portela et al. emphasize EET relevance for “bioenergy, bioremediation, and bioelectronics” (portela2024widespreadextracellularelectron pages 1-2).

## 5) Expert opinions / analysis (authoritative sources)

- Lovley (1991) provides a canonical framework emphasizing DIR as enzymatic respiration and correcting earlier assumptions of abiotic dominance (lovley1991dissimilatoryfe(iii)and pages 1-2, lovley1991dissimilatoryfe(iii)and pages 10-10).
- Schwarz et al. (2024) provide an explicit methodological opinion that “conductance… is not rigorous evidence” and that “Fe(III) oxide reduction is best evaluated” for long-range EET; they argue cytochrome filaments lack rigorous physiological evidence as primary long-range conduits, emphasizing PilA e-pili (schwarz2024lackofphysiological pages 1-2).
- Portela et al. (2024) contribute a mechanistic reconciliation for fast electron flux through a crowded periplasm via direct periplasm–nanowire interactions (portela2024widespreadextracellularelectron pages 1-2).

## 6) Candidate causal graph edges (curation table)

| Edge (Subject —predicate→ Object) | Evidence | Reference | Notes/curation flags |
|---|---|---|---|
| dissimilatory iron reduction —is_a→ energy-conserving anaerobic respiration | “organisms capable of obtaining energy by completely oxidizing organic compounds to CO2 with Fe(III) or Mn(IV) as the sole acceptor have been described” | Lovley 1991. DOI: 10.1128/mr.55.2.259-287.1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991 | Core trait-defining edge; broad review evidence. (lovley1991dissimilatoryfe(iii)and pages 2-3) |
| dissimilatory iron reduction —has_terminal_electron_acceptor→ Fe(III) | “dissimilatory Fe(III)-reducing bacteria utilize Fe(III) as an electron acceptor during their energy metabolism” | Shi et al. 2024. DOI: 10.1007/s10533-024-01186-4. URL: https://doi.org/10.1007/s10533-024-01186-4 | Good modern definition; environmental microbiology context. (shi2024responseoffe(iii)reducing pages 1-2) |
| oxidation of organic matter —coupled_to→ Fe(III) reduction | “the oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is the direct result of the enzymatic activity of specialized microorganisms” | Lovley 1991. DOI: 10.1128/mr.55.2.259-287.1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991 | Broad mechanistic statement; suitable for scope edge. (lovley1991dissimilatoryfe(iii)and pages 6-7) |
| H2 oxidation —can_be_coupled_to→ Fe(III) reduction | “the use of Fe(III) or Mn(IV) as an external electron acceptor in metabolism” and “abundant evidence that H2 oxidation can be coupled to Fe(III)/Mn(IV) reduction in sediments” | Lovley 1991. DOI: 10.1128/mr.55.2.259-287.1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991 | Donor edge; broad but older review evidence. (lovley1991dissimilatoryfe(iii)and pages 2-3) |
| PpcABCDE periplasmic cytochromes —directly_inject_electrons_into→ OmcS nanowires | “Geobacter sulfurreducens periplasmic cytochromes PpcABCDE inject electrons directly into OmcS nanowires by binding transiently” | Portela et al. 2024. DOI: 10.1038/s41467-024-46192-0. URL: https://doi.org/10.1038/s41467-024-46192-0 | Strong primary evidence; Geobacter-specific. (portela2024widespreadextracellularelectron pages 1-2) |
| PpcC —has_higher_electron_transfer_efficiency_to→ OmcS nanowires | “the least-abundant cytochrome (PpcC) showing the highest efficiency” | Portela et al. 2024. DOI: 10.1038/s41467-024-46192-0. URL: https://doi.org/10.1038/s41467-024-46192-0 | Specific paralog edge; taxon-specific. (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 4-7) |
| PpcA-E:OmcS interaction —occurs_by→ transient binding via complementary-charged residues | “periplasmic cytochromes bind transiently to nanowires via complementary-charged residues” | Portela et al. 2024. DOI: 10.1038/s41467-024-46192-0. URL: https://doi.org/10.1038/s41467-024-46192-0 | Mechanistic interaction edge; Geobacter-specific. (portela2024widespreadextracellularelectron pages 7-9) |
| OmcS nanowires —required_for→ EET to soil-abundant Fe(III) oxide | “G. sulfurreducens requires nanowires of cytochrome OmcS11 to eliminate respiratory electrons via EET to soil-abundant Fe(III) oxide” | Portela et al. 2024. DOI: 10.1038/s41467-024-46192-0. URL: https://doi.org/10.1038/s41467-024-46192-0 | Use with caution: phrased in intro/background, but from primary paper. (portela2024widespreadextracellularelectron pages 1-2) |
| PilA-based e-pili —required_for→ long-range extracellular electron transfer / Fe(III) oxide reduction | “The results are consistent with the concept that 3 nm diameter electrically conductive pili (e-pili) are required for G. sulfurreducens long-range extracellular electron transfer.” | Schwarz et al. 2024. DOI: 10.1128/mbio.00690-24. URL: https://doi.org/10.1128/mbio.00690-24 | Strong physiological evidence; Geobacter-specific. (schwarz2024lackofphysiological pages 1-2) |
| poorly conductive PilA filaments —inhibit→ Fe(III) oxide reduction | “Fe(III) oxide reduction was inhibited when the pilin gene in cytochrome-deficient mutants was modified to yield poorly conductive 3 nm diameter filaments.” | Schwarz et al. 2024. DOI: 10.1128/mbio.00690-24. URL: https://doi.org/10.1128/mbio.00690-24 | Useful negative perturbation edge. (schwarz2024lackofphysiological pages 1-2) |
| MtrCAB complex —mediates→ extracellular electron transfer across the outer membrane | “The central mechanism for electron transfer across the membrane involves the Mtr complex, a porin-cytochrome complex that consists of periplasmic decaheme MtrA, a large transmembrane pore MtrB, and the decaheme cytochrome MtrC on the surface of the cell” | Norman et al. 2023. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 | Strong primary evidence; Shewanella-specific. (norman2023acysteinepair pages 1-2) |
| MtrC/OmcA deletion —prevents→ reduction of extracellular iron oxides | “deletion of both MtrC and the analogous OmcA prevents the reduction of extracellular iron oxides” | Norman et al. 2023. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 | Perturbation evidence; Shewanella-specific. (norman2023acysteinepair pages 1-2) |
| flavin secretion —supports→ iron oxide reduction | “iron reduction by S. oneidensis is also dependent on the secretion of nanomolar concentrations of flavins” | Norman et al. 2023. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 | Strong mediator edge; Shewanella-specific. (norman2023acysteinepair pages 1-2) |
| reduced FMN —reduces→ ferrihydrite and lepidocrocite | “Reduction of certain iron oxides, such as ferrihydrite and lepidocrocite, by reduced flavin has been shown to occur at favorable rates” | Norman et al. 2023. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 | Mineral-specific; not all Fe(III) oxides. (norman2023acysteinepair pages 1-2) |
| MtrC CX8C disulfide —controls→ FMN reduction / FMN binding | “FMN reduction in S. oneidensis MR-1 is controlled by the redox-active disulfide on the cytochrome surface” | Norman et al. 2023. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 | Strong regulatory edge; Shewanella-specific. (norman2023acysteinepair pages 1-2) |
| oxygen exposure —promotes→ MtrC disulfide formation and lowers FMN affinity | “In the presence of oxygen, the disulfide forms, lowering the affinity for FMN and decreasing the rate of peroxide formation.” | Norman et al. 2023. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 | Environmental regulation edge; Shewanella-specific. (norman2023acysteinepair pages 1-2) |
| soluble Fe(II)/Fe(III) cycling —functions_as→ redox shuttle for EET | “the enhancement is due to freely diffusing ions acting as redox shuttles, where Fe3+/Fe2+ is continuously oxidized/reduced by the cells/electrodes” | Abuyen & El-Naggar 2023. DOI: 10.1002/celc.202200965. URL: https://doi.org/10.1002/celc.202200965 | Inward EET/electrode assay; not direct DIR to minerals. Mark assay-specific. (abuyen2023solubleironenhances pages 6-8) |
| MtrC and OmcA —act_as→ primary cell-surface conduits for Fe-mediated inward EET | “MtrC and OmcA are the primary cell surface conduits through which electrons are passed from the dissolved Fe into the cells” | Abuyen & El-Naggar 2023. DOI: 10.1002/celc.202200965. URL: https://doi.org/10.1002/celc.202200965 | Shewanella inward EET; assay-specific to cathodic uptake. (abuyen2023solubleironenhances pages 6-8) |
| dissolved Fe(III)-OM complexes —have_higher_reduction_rates_than→ solid Fe(III) minerals | “the reduction rates of dissolved Fe(III)-OM complexes are significantly higher than those observed for solid Fe(III) minerals” | Shi et al. 2024. DOI: 10.1007/s10533-024-01186-4. URL: https://doi.org/10.1007/s10533-024-01186-4 | Environmental factor edge; broad and curation-relevant. (shi2024responseoffe(iii)reducing pages 1-2) |
| Fe(III)-citrate / Fe(III)-EDTA amendment —causes→ faster Fe(III) reduction than ferrihydrite | “sediments amended with Fe(III)-citrate and Fe(III)-EDTA exhibited faster Fe(III) reduction rates” | Shi et al. 2024. DOI: 10.1007/s10533-024-01186-4. URL: https://doi.org/10.1007/s10533-024-01186-4 | Microcosm/sediment assay; environmental factor. (shi2024responseoffe(iii)reducing pages 1-2) |
| Fe(III)-citrate —associated_with_absence_of→ flagella and pili expression in Geobacter metallireducens | “the flagella and pili of Geobacter metallireducens are not expressed when cultured with Fe(III)-citrate” | Shi et al. 2024. DOI: 10.1007/s10533-024-01186-4. URL: https://doi.org/10.1007/s10533-024-01186-4 | Important boundary case; species-specific and indirect to DIR phenotype. (shi2024responseoffe(iii)reducing pages 1-2) |
| conjugative plasmids —slow→ insoluble iron oxide reduction | “G. sulfurreducens reduces insoluble iron oxides at much slower rates” | Fessler et al. 2023. DOI: 10.3389/fmicb.2023.1150091. URL: https://doi.org/10.3389/fmicb.2023.1150091 | Perturbation edge; Geobacter-specific. (fessler2023conjugativeplasmidsinhibit pages 1-2) |
| conjugative plasmid pKJK5 —reduces_transcription_of→ pilA and omcE | “presence of pKJK5 reduces transcription of several genes that have been shown to be implicated in extracellular electron transfer in G. sulfurreducens, including pilA and omcE” | Fessler et al. 2023. DOI: 10.3389/fmicb.2023.1150091. URL: https://doi.org/10.3389/fmicb.2023.1150091 | Transcriptomic perturbation; Geobacter-specific. (fessler2023conjugativeplasmidsinhibit pages 1-2) |
| nanowires —link→ internal electron flow to solid electron acceptors | “electrically conductive nanowires that link internal electron flow from metabolism to solid electron acceptors in the extracellular environment” | Fessler et al. 2023. DOI: 10.3389/fmicb.2023.1150091. URL: https://doi.org/10.3389/fmicb.2023.1150091 | Broad EET architecture edge; Geobacter-specific. (fessler2023conjugativeplasmidsinhibit pages 1-2) |


*Table: This table summarizes curation-ready causal edges for dissimilatory iron reduction, spanning trait definition, core Geobacter and Shewanella EET components, environmental controls, and perturbation evidence. It is designed to support TraitMech graph assembly with verbatim evidence, DOI-first references, and internal context-ID traceability.*

## 7) Visual evidence (figures)

- Portela et al. 2024 Fig. 1 and Fig. 8 panels illustrate OmcS nanowires and the proposed “nanowire-charging pathway” schematic connecting periplasmic cytochromes (PpcA-E) to OmcS nanowires (portela2024widespreadextracellularelectron media 70985d91, portela2024widespreadextracellularelectron media 36384d35).

## 8) Ontology grounding suggestions (CURIEs where feasible)

**Trait**
- METPO: traitmech:000031 (provided)

**Environment**
- ENVO terms (suggested for curator lookup; not asserted here due to missing direct mapping in evidence): anoxic sediment, suboxic sediment, groundwater.

**Chemicals**
- Fe(III), Fe(II): CHEBI identifiers exist (curator to select appropriate species/charge state); complexes: Fe(III)-citrate, Fe(III)-EDTA (label-level acceptable).
- Flavin mononucleotide (FMN): CHEBI term exists (curator lookup); riboflavin/flavins similarly.

**Processes**
- GO: “respiratory electron transport chain,” “anaerobic respiration,” “iron ion reduction,” “extracellular electron transfer” (GO term availability varies; curator validation needed).

**Proteins/complexes**
- Shewanella MtrCAB (MtrA/MtrB/MtrC) and OmcA: UniProt/GO MF grounding possible but organism/strain-specific IDs needed.
- Geobacter PpcA-E, OmcS, PilA, OmcE/OmcZ, OmcB: organism-specific UniProt IDs recommended during curation.

## 9) Warnings / curation caveats

1. **Species- and assay-specificity:** Many mechanistic edges (MtrCAB, flavin secretion, PilA/e-pili, PpcA-E→OmcS) are grounded in specific model organisms (Geobacter sulfurreducens, Shewanella oneidensis MR-1). Represent them as taxon-scoped nodes/edges when appropriate (norman2023acysteinepair pages 1-2, schwarz2024lackofphysiological pages 1-2, portela2024widespreadextracellularelectron pages 1-2).
2. **Inward EET vs DIR:** Soluble-iron-mediated cathodic electron uptake (Abuyen & El-Naggar 2023) is mechanistically relevant to EET but is not itself DIR to Fe(III) minerals; mark as assay-specific if curated (abuyen2023solubleironenhances pages 6-8).
3. **Nanowire identity controversy:** The long-range conduit debate (cytochrome filaments vs e-pili) is active. Schwarz et al. provide physiological evidence supporting e-pili requirement and argue against cytochrome filaments as primary conduits, while Portela et al. focus on OmcS nanowires and their charging pathway. Curate both as competing/mechanistically distinct pathways with appropriate evidence strength tags and species/condition qualifiers (schwarz2024lackofphysiological pages 1-2, portela2024widespreadextracellularelectron pages 1-2).
4. **Background statements vs direct functional tests:** Some claims (e.g., “requires OmcS nanowires…”) appear in introductory framing in Portela et al.; treat as moderate unless supported by direct experimental sections in the same paper or additional primary sources (portela2024widespreadextracellularelectron pages 1-2).

## 10) DOI-first bibliography (with dates/URLs where available)

1. Lovley DR. *Dissimilatory Fe(III) and Mn(IV) reduction.* **Microbiological Reviews**. 1991-06. DOI: 10.1128/mr.55.2.259-287.1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991 (lovley1991dissimilatoryfe(iii)and pages 1-2)
2. Norman MP, Edwards MJ, White GF, et al. *A Cysteine Pair Controls Flavin Reduction by Extracellular Cytochromes during Anoxic/Oxic Environmental Transitions.* **mBio**. 2023-01-16. DOI: 10.1128/mbio.02589-22. URL: https://doi.org/10.1128/mbio.02589-22 (norman2023acysteinepair pages 1-2)
3. Abuyen K, El‑Naggar MY. *Soluble Iron Enhances Extracellular Electron Uptake by Shewanella oneidensis MR‑1.* **ChemElectroChem**. 2023-01. DOI: 10.1002/celc.202200965. URL: https://doi.org/10.1002/celc.202200965 (abuyen2023solubleironenhances pages 6-8)
4. Fessler M, Madsen JS, Zhang Y. *Conjugative plasmids inhibit extracellular electron transfer in Geobacter sulfurreducens.* **Frontiers in Microbiology**. 2023-03-17. DOI: 10.3389/fmicb.2023.1150091. URL: https://doi.org/10.3389/fmicb.2023.1150091 (fessler2023conjugativeplasmidsinhibit pages 1-2)
5. Portela PC, Shipps CC, Shen C, et al. *Widespread extracellular electron transfer pathways for charging microbial cytochrome OmcS nanowires via periplasmic cytochromes PpcABCDE.* **Nature Communications**. Accepted 2024-02-19. DOI: 10.1038/s41467-024-46192-0. URL: https://doi.org/10.1038/s41467-024-46192-0 (portela2024widespreadextracellularelectron pages 1-2)
6. Schwarz IA, Alsaqri B, Lekbach Y, et al. *Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer.* **mBio**. Published 2024-04-02. DOI: 10.1128/mbio.00690-24. URL: https://doi.org/10.1128/mbio.00690-24 (schwarz2024lackofphysiological pages 1-2)
7. Shi T, Peng C, Lu L, et al. *Response of Fe(III)-reducing kinetics, microbial community structure and Fe(III)-related functional genes to Fe(III)-organic matter complexes and ferrihydrite in lake sediment.* **Biogeochemistry**. Published online 2024-10-15. DOI: 10.1007/s10533-024-01186-4. URL: https://doi.org/10.1007/s10533-024-01186-4 (shi2024responseoffe(iii)reducing pages 1-2)

---

## Appendix: quantitative/statistical highlights suitable for node/edge attributes
- Electron wiring rate contrast: “wire electrons rapidly (>10^6 s−1)” vs “slow (<10^5 s−1) electron diffusion” (Portela 2024) (portela2024widespreadextracellularelectron pages 1-2)
- OmcS electrochemistry: “midpoint 82 mV-higher” and “midpoint potential of −130 mV” (Portela 2024) (portela2024widespreadextracellularelectron pages 1-2, portela2024widespreadextracellularelectron pages 7-9)
- OmcS filament prevalence: “only ca. 10% of the filaments” (Schwarz 2024) (schwarz2024lackofphysiological pages 8-11)
- Knockout effects on inward EET current: 37%, 42%, 73%, 96% decreases (Abuyen 2023) (abuyen2023solubleironenhances pages 6-8)



References

1. (lovley1991dissimilatoryfe(iii)and pages 2-3): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2590 citations.

2. (lovley1991dissimilatoryfe(iii)and pages 6-7): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2590 citations.

3. (shi2024responseoffe(iii)reducing pages 1-2): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 11 citations and is from a peer-reviewed journal.

4. (lovley1991dissimilatoryfe(iii)and pages 1-2): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2590 citations.

5. (lovley1991dissimilatoryfe(iii)and pages 10-10): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2590 citations.

6. (schwarz2024lackofphysiological pages 1-2): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 14 citations and is from a domain leading peer-reviewed journal.

7. (portela2024widespreadextracellularelectron pages 1-2): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.

8. (fessler2023conjugativeplasmidsinhibit pages 1-2): Mathias Fessler, Jonas Stenløkke Madsen, and Yifeng Zhang. Conjugative plasmids inhibit extracellular electron transfer in geobacter sulfurreducens. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1150091, doi:10.3389/fmicb.2023.1150091. This article has 8 citations and is from a peer-reviewed journal.

9. (portela2024widespreadextracellularelectron pages 7-9): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.

10. (schwarz2024lackofphysiological pages 4-8): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 14 citations and is from a domain leading peer-reviewed journal.

11. (norman2023acysteinepair pages 1-2): Michael P. Norman, Marcus J. Edwards, Gaye F. White, Joshua A. J. Burton, Julea N. Butt, David J. Richardson, Ricardo O. Louro, Catarina M. Paquete, and Thomas A. Clarke. A cysteine pair controls flavin reduction by extracellular cytochromes during anoxic/oxic environmental transitions. Feb 2023. URL: https://doi.org/10.1128/mbio.02589-22, doi:10.1128/mbio.02589-22. This article has 15 citations and is from a domain leading peer-reviewed journal.

12. (abuyen2023solubleironenhances pages 6-8): Karla Abuyen and Mohamed Y. El‐Naggar. Soluble iron enhances extracellular electron uptake by shewanella oneidensis mr-1. ChemElectroChem, Jan 2023. URL: https://doi.org/10.1002/celc.202200965, doi:10.1002/celc.202200965. This article has 24 citations and is from a peer-reviewed journal.

13. (schwarz2024lackofphysiological pages 8-11): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 14 citations and is from a domain leading peer-reviewed journal.

14. (portela2024widespreadextracellularelectron pages 4-7): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.

15. (portela2024widespreadextracellularelectron media 70985d91): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.

16. (portela2024widespreadextracellularelectron media 36384d35): Pilar C. Portela, Catharine C. Shipps, Cong Shen, Vishok Srikanth, Carlos A. Salgueiro, and Nikhil S. Malvankar. Widespread extracellular electron transfer pathways for charging microbial cytochrome omcs nanowires via periplasmic cytochromes ppcabcde. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46192-0, doi:10.1038/s41467-024-46192-0. This article has 88 citations and is from a highest quality peer-reviewed journal.