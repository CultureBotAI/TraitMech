---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:50:47.687375'
end_time: '2026-06-18T05:11:04.420004'
duration_seconds: 1216.73
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Electron transfer
  trait_identifier: METPO:1000805
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: electron_transfer
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which electrons are transferred from an electron donor
    to an electron acceptor.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review
    supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93:
    c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer
    mechanisms.)'
  causal_graph_summary: 'electron_transfer_redox_carriers: 9 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Electron transfer
- **METPO identifier:** METPO:1000805
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred from an electron donor to an electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93: c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer mechanisms.)
- **Existing causal graph summary:** electron_transfer_redox_carriers: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **Electron transfer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/electron_transfer.yaml`.

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
- **Trait label:** Electron transfer
- **METPO identifier:** METPO:1000805
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred from an electron donor to an electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bbabio.2008.09.008: electron transfer process (Review supports electron donor-to-acceptor flow in membrane respiratory chains.) | DOI:10.1038/nrmicro.2016.93: c-type cytochromes and microbial nanowires (Review supports extracellular electron-transfer mechanisms.)
- **Existing causal graph summary:** electron_transfer_redox_carriers: 9 nodes, 7 edges

## Research Objective

Research the microbial trait **Electron transfer** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/electron_transfer.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Electron transfer (METPO:1000805)

### Scope summary (TraitMech curation)
The METPO trait **Electron transfer** (METPO:1000805) can be operationalized as a **microbial physiological capacity** to route electrons from an **electron donor** through redox carriers to an **electron acceptor**, encompassing (i) **intracellular respiratory electron transport chains (ETC)** that couple electron flow to ion translocation and energy conservation, and (ii) **extracellular electron transfer (EET)** where cells exchange electrons with **redox-active materials outside the cell**, including minerals and electrodes. A recent peer-reviewed definition states: “Extracellular electron transfer (EET) is a process by which bacterial cells can exchange electrons with a redox-active material located outside of the cell” (Ford & TerAvest, Jan 2024) (ford2024theelectrontransport pages 1-2). 

**Boundary cases / nearby traits**:
- **Intracellular vs extracellular**: Intracellular respiration routes electrons from donors (e.g., NADH, succinate) to internal membrane carriers and terminal oxidases/reductases, whereas EET explicitly involves external acceptors such as Fe(III)/Mn(IV) oxides or electrodes via outer-surface conduits (trani2023structureofthe pages 1-2, ford2024theelectrontransport pages 1-2).
- **Direct vs mediated EET**: Reviews distinguish **direct electron transfer (DET)** to electrodes via outer-membrane c-type cytochromes and **mediated EET** via soluble shuttles (e.g., pyocyanin) (Hazzan et al., Nov 2023) (hazzan2023strategiesforenhancing pages 2-3).
- **Interspecies electron transfer**: Community-level DIET/MIET is within scope as electron transfer between syntrophic partners; e.g., in sulfate-dependent anaerobic oxidation of methane, “electrons are transferred to the partner SRBs by various mechanisms, such as MIET and DIET” (Zhuang et al., May 2024) (zhuang2024electrontransferin pages 10-11).
- **Electrode-driven “reverse” electron transfer**: Bidirectional operation of EET pathways (electron uptake from cathodes) is in scope because it is still donor→acceptor electron flow, but it is **assay-dependent** (poised electrodes, microaerobic constraints) and should be curated with context (ford2024theelectrontransport pages 1-2, ford2024theelectrontransport pages 2-5).

### Key concepts and current understanding (mechanistic overview)
#### 1) Intracellular respiratory electron transfer
A current (2024) synthesis of complex I emphasizes that bacterial **NDH-1/Complex I** “oxidizes NADH using ubiquinone,” coupling the redox reaction to “transmembrane translocation of four protons to generate a proton motive force (pmf)” (Grivennikova et al., Dec 2024) (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2). Downstream, electron transfer commonly proceeds from a quinone pool to **cytochrome bc1** and then to cytochrome c and terminal oxidases; in *Pseudomonas aeruginosa*, Trani et al. describe electrons flowing “into the quinone pool… then to the bc1 complex… and onward via cytochrome c to terminal oxidases… that reduce O2 to H2O” (Sep 2023) (trani2023structureofthe pages 1-2).

A key “nearby trait” is **energy conservation**: electron transfer in the ETC is tightly linked to ion translocation and ATP synthesis (pmf generation), while EET may or may not conserve energy depending on context (e.g., electrode poised potentials, mediator availability) (trani2023structureofthe pages 1-2, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2).

#### 2) Extracellular electron transfer (EET) and bidirectionality
In *Shewanella oneidensis* MR-1, the **Mtr pathway** acts as an outer-membrane-spanning conduit enabling respiration to insoluble acceptors (Fe(III), Mn(IV)) and electrodes, and it can be **reversible** for cathode electron uptake (ford2024theelectrontransport pages 1-2). In the electrosynthesis context, electrons taken up from a cathode are routed through Mtr components and periplasmic carriers to the inner membrane and quinone pool; a key energetic constraint is that “generating NADH via electron uptake from a cathode is energetically unfavorable,” requiring ion-coupled NADH dehydrogenases operating in reverse and maintenance of the pmf (ford2024theelectrontransport pages 2-5).

A schematic of this bidirectional EET architecture (MtrCAB → periplasmic carriers → CymA/quinone pool) is shown in Ford & TerAvest (Figure 1) (ford2024theelectrontransport media 74995b43).

#### 3) Long-range extracellular conduction: cytochrome nanowires
A major 2023 advance is the discovery/extension of **extracellular cytochrome nanowires (ECNs)** across diverse prokaryotes. Baquero et al. (Cell, Jun 2023) describe ECNs as multiheme filaments with “closely stacked heme arrangements for efficient electron transfer,” supporting long-range EET concepts (baquero2023extracellularcytochromenanowires pages 10-11). For some archaeal ECNs, functional claims are partly inferred (“it is very likely… function in long-distance electron transfer”), and should be curated as **uncertain** unless supported by direct conductivity/functional assays in the target taxon (baquero2023extracellularcytochromenanowires pages 10-11).

### Recent developments (prioritizing 2023–2024)
1. **High-resolution structural organization of respiratory supercomplexes**: Trani et al. (PNAS, Sep 2023) resolve a **bc1–cbb3 supercomplex** in *P. aeruginosa* that “transfer[s] electrons directly to [terminal oxidases] via bound cytochrome c4 and c5,” strengthening evidence that electron transfer can be organized as physical supercomplexes (trani2023structureofthe pages 1-2).
2. **EET bidirectionality enabling microbial electrosynthesis**: Ford & TerAvest (Applied and Environmental Microbiology, Jan 2024) show electron uptake can be partitioned between **NADH generation** and **oxygen reduction** to sustain pmf in microaerobic BES; importantly, high dissolved oxygen can lead to ROS formation at a strong reductant cathode and cell death, emphasizing design constraints (ford2024theelectrontransport pages 1-2, ford2024theelectrontransport pages 2-5).
3. **Broad distribution of cytochrome nanowires**: Baquero et al. (Cell, Jun 2023) provide structural comparative evidence that cytochrome-nanowire-like architectures may be widespread, motivating ontology nodes for “extracellular cytochrome nanowire” distinct from type-IV-pilus-based nanowires (baquero2023extracellularcytochromenanowires pages 10-11).
4. **Respiratory chain branching and inhibitor tolerance**: Uribe-Ramírez et al. (J Bioenerg Biomembr, Nov 2024) show condition-dependent use of terminal oxidases and cyanide tolerance via bd oxidase dominance, illustrating environmental modulation of intracellular electron transfer routes (uriberamirez2024modificationsofthe pages 11-12).

### Current applications / real-world implementations
1. **Bioelectrochemical systems (BES)**: EET is exploited in microbial fuel cells and related technologies where current output/charge transfer serves as an assay and functional output (hazzan2023strategiesforenhancing pages 2-3, mouhib2023engineeringextracellularelectron pages 17-20). Electrochemical methods commonly used to quantify electron transfer include cyclic voltammetry and electrochemical impedance spectroscopy (hazzan2023strategiesforenhancing pages 2-3).
2. **Microbial electrosynthesis (MES)**: Cathode-driven electron uptake can power intracellular reductions (e.g., acetoin → 2,3-butanediol) via reverse electron transfer to NADH in *S. oneidensis* engineered to express butanediol dehydrogenase, providing a concrete implementation and assay (product formation) (ford2024theelectrontransport pages 1-2).
3. **Biogeochemical cycling and syntrophy**: In anoxic sediments, sulfate-dependent AOM involves electron transfer from ANME archaea to sulfate-reducing bacteria via DIET/MIET mechanisms, linking this trait to methane consumption and sulfur cycling (zhuang2024electrontransferin pages 10-11).

### Quantitative/statistical data points from recent studies
- In an AD-MET context, exposure of *Geobacter* biofilm anodes to methanogens decreased electrochemical performance: e.g., **maximum current density decreased by ~37%** with *Methanobacterium formicicum*, and **total transferred charge decreased by ~40%** with *Methanothrix soehngenii* (Ngoumelah et al., NPJ Biofilms Microbiomes, Mar 2024; DOI:10.1038/s41522-024-00490-z; URL: https://doi.org/10.1038/s41522-024-00490-z). *Note:* full-text evidence for these numeric values was not ingested into the evidence set above; they should be re-verified before curation into TraitMech.

### Candidate nodes (curation-ready)
The following table lists candidate entities for `data/traits/metabolism/electron_transfer.yaml`, grouped by type and grounded to stable identifiers where possible.

| Node type | Node label | Suggested ontology grounding | Notes | Example taxa |
|---|---|---|---|---|
| Process/Pathway | electron transfer | GO:0006118 | broad donor-to-acceptor redox flow trait; includes ETC and EET (mouhib2023engineeringextracellularelectron pages 17-20, ford2024theelectrontransport pages 1-2) | broad bacterial and archaeal trait |
| Process/Pathway | respiratory electron transport chain | GO:0022900 | intracellular membrane ETC generating pmf (uriberamirez2024modificationsofthe pages 11-12, trani2023structureofthe pages 1-2) | *Pseudomonas aeruginosa*, *Bacillus licheniformis* |
| Process/Pathway | extracellular electron transfer (EET) |  | cell exchanges electrons with external redox-active material (mouhib2023engineeringextracellularelectron pages 17-20, ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1, *Geobacter sulfurreducens* |
| Process/Pathway | direct extracellular electron transfer |  | cytochrome/nanowire-dependent contact route (mouhib2023engineeringextracellularelectron pages 20-23, hazzan2023strategiesforenhancing pages 2-3) | *Shewanella oneidensis* MR-1, *Geobacter sulfurreducens* |
| Process/Pathway | mediated extracellular electron transfer |  | soluble redox shuttles transfer electrons externally (mouhib2023engineeringextracellularelectron pages 20-23, hazzan2023strategiesforenhancing pages 2-3) | *Shewanella oneidensis* MR-1, *Pseudomonas aeruginosa* |
| Process/Pathway | direct interspecies electron transfer (DIET) |  | electron flow between partner microbes without diffusible metabolites (zhuang2024electrontransferin pages 10-11) | ANME/SRB consortia, *Geobacter* partnerships |
| Process/Pathway | mediated interspecies electron transfer (MIET) |  | interspecies exchange via diffusible mediators/intermediates (zhuang2024electrontransferin pages 10-11) | ANME/SRB consortia |
| Process/Pathway | long-distance electron transport (LDET) |  | multicellular filament-associated electrogenic transport (zhuang2024electrontransferin pages 10-11) | cable bacteria |
| Process/Pathway | reverse electron transport for NADH generation |  | inward EET drives reverse NDH to make NADH (ford2024theelectrontransport pages 1-2, ford2024theelectrontransport pages 2-5) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | Complex I / NDH-1 / NADH:quinone oxidoreductase | EC:7.1.1.2 | oxidizes NADH and reduces quinone; pumps protons (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | broad bacteria |
| Protein/Complex | NADH dehydrogenase (reverse-operating NDH) | EC:7.1.1.2 | uses pmf to reduce NAD+ during electron uptake (ford2024theelectrontransport pages 1-2, ford2024theelectrontransport pages 2-5) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | succinate dehydrogenase / Complex II | EC:7.1.1.2? | feeds electrons from succinate to quinone pool; no proton pumping emphasized (uriberamirez2024modificationsofthe pages 11-12, giordano2024nitricoxideand pages 8-13) | *Bacillus licheniformis*, broad bacteria |
| Protein/Complex | quinol:cytochrome c reductase / cytochrome bc1 complex | EC:7.1.1.8 | routes quinol electrons to cytochrome c via Q cycle (trani2023structureofthe pages 1-2, walters2024spectroscopicinvestigationsof pages 21-25) | *Pseudomonas aeruginosa*, broad bacteria |
| Protein/Complex | cytochrome c oxidase aa3-type | EC:7.1.1.9 | terminal oxidase reducing O2 in aerobic ETC (uriberamirez2024modificationsofthe pages 11-12, giordano2024nitricoxideand pages 8-13) | *Bacillus licheniformis*, *Pseudomonas aeruginosa* |
| Protein/Complex | cytochrome c oxidase cbb3-type | EC:7.1.1.9 | terminal oxidase in bc1-cbb3 supercomplex (trani2023structureofthe pages 1-2) | *Pseudomonas aeruginosa* |
| Protein/Complex | cytochrome bd quinol oxidase | EC:7.1.1.7 | quinol-oxidizing terminal oxidase; cyanide-resistant branch (uriberamirez2024modificationsofthe pages 11-12, giordano2024nitricoxideand pages 8-13) | *Bacillus licheniformis* |
| Protein/Complex | MtrCAB complex |  | outer-membrane EET conduit linking periplasm to exterior (mouhib2023engineeringextracellularelectron pages 20-23, ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | CymA |  | inner-membrane quinol oxidizing hub feeding EET routes (mouhib2023engineeringextracellularelectron pages 20-23, mouhib2023engineeringextracellularelectron pages 74-77) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | FccA |  | periplasmic carrier between CymA and outer-membrane conduits (ford2024theelectrontransport pages 2-5, mouhib2023engineeringextracellularelectron pages 20-23) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | CctA / small tetraheme cytochrome |  | periplasmic electron carrier in Mtr-linked pathways (ford2024theelectrontransport pages 2-5, mouhib2023engineeringextracellularelectron pages 74-77) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | OmcA |  | outer-surface multiheme cytochrome transferring electrons to external acceptors (mouhib2023engineeringextracellularelectron pages 20-23, mouhib2023engineeringextracellularelectron pages 74-77) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | MtrC |  | outer-surface decaheme cytochrome for extracellular reduction/electrode exchange (mouhib2023engineeringextracellularelectron pages 20-23, mouhib2023engineeringextracellularelectron pages 74-77) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | MtrA |  | periplasm-spanning decaheme component within MtrCAB conduit (mouhib2023engineeringextracellularelectron pages 20-23) | *Shewanella oneidensis* MR-1 |
| Protein/Complex | PioABC complex |  | Fe(II)-oxidation-associated porin-cytochrome pathway homologous to MtrAB (hou2024biologicalandchemical pages 1-2) | phototrophic Fe(II)-oxidizers; compared with *Shewanella* |
| Protein/Complex | PioA |  | periplasmic decaheme c-type cytochrome needed for Fe(II) oxidation (hou2024biologicalandchemical pages 1-2) | Fe(II)-oxidizing bacteria |
| Protein/Complex | PioB |  | outer-membrane porin-like partner in Pio pathway (hou2024biologicalandchemical pages 1-2) | Fe(II)-oxidizing bacteria |
| Protein/Complex | PioC |  | periplasmic Fe-S protein in Pio pathway (hou2024biologicalandchemical pages 1-2) | Fe(II)-oxidizing bacteria |
| Protein/Complex | conductive pili / nanowires |  | long-range extracellular conduction appendages (mouhib2023engineeringextracellularelectron pages 20-23, mouhib2023engineeringextracellularelectron pages 72-74) | *Geobacter sulfurreducens*, some *Shewanella* |
| Protein/Complex | extracellular cytochrome nanowires (ECNs) |  | stacked multiheme filaments enabling long-distance ET (baquero2023extracellularcytochromenanowires pages 10-11) | *Geobacter* spp., archaeal ECN-formers |
| Protein/Complex | OmcS/OmcZ-like filamentous cytochromes |  | cytochrome filaments implicated in conductive biofilms (baquero2023extracellularcytochromenanowires pages 10-11) | *Geobacter sulfurreducens* |
| Small molecule/electron carrier | quinone pool | GO:0052887 | membrane electron hub linking donors to terminal branches (giordano2024nitricoxideand pages 8-13, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | broad bacteria |
| Small molecule/electron carrier | ubiquinone / ubiquinol | CHEBI:16389 | aerobic ETC quinone carrier feeding bc1/oxidases (trani2023structureofthe pages 1-2, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | *Pseudomonas aeruginosa* |
| Small molecule/electron carrier | menaquinone / menaquinol | CHEBI:18009 | quinone carrier linked to CymA and anaerobic branches (mouhib2023engineeringextracellularelectron pages 20-23, ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1, *Bacillus licheniformis* |
| Small molecule/electron carrier | semiquinone | CHEBI:24646 | one-electron quinone intermediate in Q cycle (donald2023decipheringtheenergetics pages 35-40, walters2024spectroscopicinvestigationsof pages 21-25) | broad bacteria |
| Small molecule/electron carrier | flavins / riboflavin / FMN | CHEBI:30527 / CHEBI:17621 / CHEBI:58210 | soluble or bound mediators for mediated EET (mouhib2023engineeringextracellularelectron pages 20-23, mouhib2023engineeringextracellularelectron pages 72-74) | *Shewanella oneidensis* MR-1, Gram-positive EET systems |
| Small molecule/electron carrier | c-type cytochrome hemes | GO:0020038 | multiheme cofactors enabling stepwise electron hopping (mouhib2023engineeringextracellularelectron pages 20-23, baquero2023extracellularcytochromenanowires pages 10-11) | *Shewanella*, *Geobacter*, broad bacteria |
| Small molecule/electron carrier | cytochrome c | CHEBI:36124 | periplasmic/extrinsic carrier between bc1 and oxidases (trani2023structureofthe pages 1-2, walters2024spectroscopicinvestigationsof pages 21-25) | *Pseudomonas aeruginosa* |
| Small molecule/electron carrier | NADH | CHEBI:16908 | intracellular electron donor to complex I; product of reverse ET in electrosynthesis (ford2024theelectrontransport pages 1-2, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | broad bacteria |
| Small molecule/electron carrier | NAD+ | CHEBI:57540 | reduced to NADH by reverse-operating NDH during inward EET (ford2024theelectrontransport pages 2-5) | *Shewanella oneidensis* MR-1 |
| Small molecule/electron carrier | proton motive force | GO:0015988 | energetic driver coupling ET to ATP synthesis/reverse NDH (ford2024theelectrontransport pages 2-5, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | broad bacteria |
| Electron donor | NADH | CHEBI:16908 | canonical intracellular ETC electron donor (giordano2024nitricoxideand pages 8-13, grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | broad bacteria |
| Electron donor | succinate | CHEBI:15741 | donates electrons via succinate dehydrogenase (uriberamirez2024modificationsofthe pages 11-12, giordano2024nitricoxideand pages 8-13) | broad bacteria |
| Electron donor | lactate | CHEBI:24996 | donor supporting Shewanella extracellular reduction pathways (mouhib2023engineeringextracellularelectron pages 20-23) | *Shewanella oneidensis* MR-1 |
| Electron donor | formate | CHEBI:15740 | donor for extracellular reduction/electrode-linked pathways (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 |
| Electron donor | H2 | CHEBI:18276 | donor in some Shewanella iodate-reduction pathway tests (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 |
| Electron donor | Fe(II) | CHEBI:29033 | electron donor in nitrate-reducing Fe(II) oxidation (hou2024biologicalandchemical pages 1-2) | *Shewanella oneidensis* MR-1 context, FeOB |
| Electron donor | methane | CHEBI:16183 | donor oxidized by ANME in sulfate-dependent AOM (zhuang2024electrontransferin pages 10-11) | ANME archaea |
| Electron donor | ethane | CHEBI:16183? | donor in sulfate-coupled alkane oxidation consortia (zhuang2024electrontransferin pages 10-11) | alkane-oxidizing archaea/SRB consortia |
| Electron donor | butane | CHEBI:37808 | donor in sulfate-coupled alkane oxidation consortia (zhuang2024electrontransferin pages 10-11) | alkane-oxidizing archaea/SRB consortia |
| Electron donor | sulfide | CHEBI:16199 | donor entering sulfur-oxidizing respiratory chains (donald2023decipheringtheenergetics pages 35-40) | sulfur oxidizers |
| Electron donor | cathode-derived electrons | ENVO:01001416 | external abiotic donor in microbial electrosynthesis/BES (ford2024theelectrontransport pages 1-2) | electrotrophs, *Shewanella oneidensis* MR-1 |
| Electron acceptor | oxygen | CHEBI:15379 | terminal acceptor for oxidases in aerobic ETC (giordano2024nitricoxideand pages 8-13, trani2023structureofthe pages 1-2) | broad bacteria |
| Electron acceptor | nitrate | CHEBI:17632 | respiratory acceptor in quinone-linked nitrate branches and EET assays (hou2024biologicalandchemical pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | *Bacillus licheniformis*, *Shewanella* |
| Electron acceptor | nitrite | CHEBI:16301 | reduction intermediate; can abiotically oxidize Fe(II) (hou2024biologicalandchemical pages 1-2) | nitrate-reducing systems |
| Electron acceptor | fumarate | CHEBI:18012 | soluble terminal acceptor linked to CymA/FccA branches (mouhib2023engineeringextracellularelectron pages 20-23) | *Shewanella oneidensis* MR-1 |
| Electron acceptor | Fe(III) oxide | CHEBI:25523 | classic insoluble extracellular acceptor in metal reduction (mouhib2023engineeringextracellularelectron pages 20-23, ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1, *Geobacter sulfurreducens* |
| Electron acceptor | Mn(IV) oxide | CHEBI:26284 | extracellular mineral acceptor for Mtr-linked respiration (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 |
| Electron acceptor | sulfate | CHEBI:16189 | terminal acceptor used by SRB receiving interspecies electrons (zhuang2024electrontransferin pages 10-11) | SRB in ANME/SRB consortia |
| Electron acceptor | electrode / anode | ENVO:01001416 | extracellular solid acceptor used in BES/MFC assays (mouhib2023engineeringextracellularelectron pages 17-20, hazzan2023strategiesforenhancing pages 2-3) | exoelectrogens |
| Electron acceptor | iodate | CHEBI:83429 | extracellular acceptor reduced via dmsEFABGH-linked pathway (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 |
| Electron acceptor | uranium(VI) | CHEBI:33287 | extracellular reducible metal target in EET examples (mouhib2023engineeringextracellularelectron pages 72-74) | *Geobacter sulfurreducens* |
| Electron acceptor | hexavalent chromium | CHEBI:18408 | extracellular reducible contaminant in EET examples (mouhib2023engineeringextracellularelectron pages 72-74) | electroactive bacteria |
| Environmental/assay factor | microaerobic condition | ENVO:01001406 | trace O2 can support pmf during inward EET (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 BES |
| Environmental/assay factor | high dissolved oxygen | ENVO:09200014 | excess O2 can cause ROS and inhibit electrosynthesis (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 BES |
| Environmental/assay factor | cathode poised at -0.5 V vs Ag/AgCl |  | assay condition driving inward electron uptake (ford2024theelectrontransport pages 1-2) | *Shewanella oneidensis* MR-1 BES |
| Environmental/assay factor | microbial fuel cell / bioelectrochemical system | ENVO:03501257 | current-producing assay platform for EET capacity (mouhib2023engineeringextracellularelectron pages 17-20, hazzan2023strategiesforenhancing pages 2-3) | broad exoelectrogens |
| Environmental/assay factor | chronoamperometry / current production |  | operational readout of electrode electron transfer (mouhib2023engineeringextracellularelectron pages 44-48, hazzan2023strategiesforenhancing pages 2-3) | BES studies |
| Environmental/assay factor | cyclic voltammetry |  | electrochemical assay for redox activity and mediator behavior (hazzan2023strategiesforenhancing pages 2-3) | BES studies |
| Environmental/assay factor | electrochemical impedance spectroscopy |  | assay for biofilm charge transfer resistance/capacitance (hazzan2023strategiesforenhancing pages 2-3) | BES studies |
| Environmental/assay factor | ferrozine Fe assay |  | assay for Fe redox change linked to ET (mouhib2023engineeringextracellularelectron pages 17-20, mouhib2023engineeringextracellularelectron pages 72-74) | metal-reduction studies |
| Environmental/assay factor | acetoin-to-2,3-butanediol conversion |  | proxy assay for cathode-driven intracellular NADH generation (ford2024theelectrontransport pages 1-2) | engineered *Shewanella oneidensis* MR-1 |


*Table: This table lists candidate nodes for a TraitMech causal graph of microbial electron transfer, grouped by biological entity type and annotated with suggested ontology grounding. It is designed to support curation of intracellular respiratory electron transport and extracellular electron transfer mechanisms, including taxon-specific components where warranted.*

### Candidate causal edges (evidence-backed triples)
The following edges are proposed for a TraitMech causal graph. Edges include intracellular ETC, EET, and interspecies electron transfer, with assay- and taxon-specific notes.

| Edge (S–P–O) | Evidence snippet | Reference (DOI + URL + publication month/year) | Context/notes |
|---|---|---|---|
| NADH dehydrogenase/Complex I → reduces → ubiquinone | “Complex I… oxidizes NADH using ubiquinone” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | 10.3390/ijms252413421 · https://doi.org/10.3390/ijms252413421 · Dec 2024 | Broad bacterial respiratory ETC; strong, general intracellular ET edge. |
| Complex I → translocates → protons across membrane | “coupling this redox reaction to vectorial transmembrane translocation of four protons to generate a proton motive force” (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2) | 10.3390/ijms252413421 · https://doi.org/10.3390/ijms252413421 · Dec 2024 | Broad bacterial respiratory ETC; supports ET→PMF coupling. |
| ubiquinol → donates electrons to → cytochrome bc1 complex | “UQH2:cyt c oxidoreductase, Complex III” and electrons flow “from donors… into the quinone pool… then to the bc1 complex” (trani2023structureofthe pages 1-2) | 10.1073/pnas.2307093120 · https://doi.org/10.1073/pnas.2307093120 · Sep 2023 | Canonical intracellular ETC edge; broad but source is *Pseudomonas aeruginosa*. |
| cytochrome bc1 complex → transfers electrons to → cytochrome c | “then to the bc1 complex… and onward via cytochrome c” (trani2023structureofthe pages 1-2) | 10.1073/pnas.2307093120 · https://doi.org/10.1073/pnas.2307093120 · Sep 2023 | Strong respiratory edge; intracellular, membrane/periplasm interface. |
| cytochrome c → transfers electrons to → terminal oxidase | “and onward via cytochrome c to terminal oxidases (Complex IV) that reduce O2 to H2O” (trani2023structureofthe pages 1-2) | 10.1073/pnas.2307093120 · https://doi.org/10.1073/pnas.2307093120 · Sep 2023 | Broad ETC architecture; source specifically resolves bc1–cbb3 supercomplex. |
| terminal oxidase → reduces → oxygen | “terminal oxidases (Complex IV) that reduce O2 to H2O” (trani2023structureofthe pages 1-2) | 10.1073/pnas.2307093120 · https://doi.org/10.1073/pnas.2307093120 · Sep 2023 | Strong, broad aerobic respiration edge. |
| succinate dehydrogenase → feeds electrons into → quinone pool | “Succinate dehydrogenase (SDH/fumarate reductase) appears associated with a quinone-linked nitrate reductase… implying electron transfer from succinate to the quinone pool” (uriberamirez2024modificationsofthe pages 11-12) | 10.1007/s10863-024-10041-y · https://doi.org/10.1007/s10863-024-10041-y · Nov 2024 | Supported in *Bacillus licheniformis*; taxon-specific respiratory configuration. |
| quinol oxidase bd → functions as → cyanide-resistant terminal oxidase branch | “Cyanide strongly inhibits aa3… but has limited effect when bd predominates, indicating bd is cyanide-resistant” (uriberamirez2024modificationsofthe pages 11-12) | 10.1007/s10863-024-10041-y · https://doi.org/10.1007/s10863-024-10041-y · Nov 2024 | Taxon- and condition-specific (*B. licheniformis* growth conditions). |
| MtrCAB pathway → enables respiration using → extracellular Fe(III)/Mn(IV) or electrodes | “the Mtr pathway is an outer-membrane-spanning electron conduit that enables respiration to insoluble acceptors (Fe(III), Mn(IV)) or electrodes” (ford2024theelectrontransport pages 1-2) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Strong EET edge; *Shewanella oneidensis* MR-1 specific but archetypal. |
| cathode-derived electrons → enter cell via → MtrCAB pathway | “Electrons taken into the cell from a cathode… [involve] the reversible Mtr pathway/MtrCAB complex” (ford2024theelectrontransport pages 1-2) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Assay-specific to poised cathode BES; inward EET/electrosynthesis. |
| MtrCAB pathway → passes electrons to → periplasmic carriers FccA/CctA | “electrons… are transferred via Mtr to reduce respiratory quinones” and “passed through periplasmic electron carriers (FccA and CctA)” (ford2024theelectrontransport pages 1-2, ford2024theelectrontransport pages 2-5) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | *Shewanella* pathway topology; strong but taxon-specific. |
| FccA/CctA → transfer electrons to → CymA | “passed through periplasmic electron carriers (PEC) like FccA and CctA, to the inner membrane cytochrome CymA” (ford2024theelectrontransport media 74995b43, ford2024theelectrontransport pages 2-5) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Supported by figure/text in *S. oneidensis* MR-1. |
| CymA → oxidizes → reduced quinones/quinol pool | “inner membrane cytochrome CymA that oxidizes reduced quinones and acts as an electron hub” (ford2024theelectrontransport pages 1-2) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Core *Shewanella* EET hub; taxon-specific but well-established. |
| reverse-operating NADH dehydrogenases → reduce → NAD+ to NADH | “reverse operation of ion-coupled NADH dehydrogenases generates NADH” (ford2024theelectrontransport pages 1-2) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Inward EET/electrosynthesis context; assay-specific to cathode-driven system. |
| proton motive force → drives → reverse NADH dehydrogenase activity | “PMF drives unfavorable reductions” and dissipation of PMF “halts electrosynthetic NADH-dependent reactions” (ford2024theelectrontransport pages 2-5) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Strong mechanistic edge for cathodic electrosynthesis; *Shewanella* BES. |
| trace oxygen/microaerobic oxidase activity → supports → proton motive force | “oxidases use trace dissolved oxygen in a microaerobic bioelectrical chemical system… supporting the membrane proton gradient” (ford2024theelectrontransport pages 1-2) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Assay-specific; beneficial only at low O2 in this BES design. |
| high dissolved oxygen → inhibits → electrosynthetic electron transfer/product formation | “this process is inhibited by high levels of dissolved oxygen… O2 molecules react with the strong reductant (cathode) to form reactive oxygen species, resulting in cell death” (ford2024theelectrontransport pages 1-2) | 10.1128/aem.01387-23 · https://doi.org/10.1128/aem.01387-23 · Jan 2024 | Negative environmental edge; specific to cathodic BES conditions. |
| extracellular cytochrome nanowires → enable → long-distance electron transfer | “it is very likely that the two archaeal ECNs function in long-distance electron transfer” (baquero2023extracellularcytochromenanowires pages 10-11) | 10.1016/j.cell.2023.05.012 · https://doi.org/10.1016/j.cell.2023.05.012 · Jun 2023 | Comparative/phylogenetic evidence; partly inferred for archaeal ECNs, mark uncertain. |
| closely stacked hemes in ECNs → promote → efficient electron transfer | “closely stacked heme arrangements for efficient electron transfer” (baquero2023extracellularcytochromenanowires pages 10-11) | 10.1016/j.cell.2023.05.012 · https://doi.org/10.1016/j.cell.2023.05.012 · Jun 2023 | Structural mechanism; strong for filament architecture, conductivity directness may vary by taxon. |
| type IV pilus/T2SS-associated machinery → exports → cytochrome filaments | pilin may be “functioning as a pump to aid the export of cytochrome filaments through a Type 2 Secretion System (T2SS)” (baquero2023extracellularcytochromenanowires pages 10-11) | 10.1016/j.cell.2023.05.012 · https://doi.org/10.1016/j.cell.2023.05.012 · Jun 2023 | Mechanistic inference from genomic/structural context; uncertain. |
| MtrABC gene cluster → is linked to → nitrate-reducing Fe(II) oxidation | “The MtrABC gene cluster was linked to this process” (hou2024biologicalandchemical pages 1-2) | 10.3390/microorganisms12122454 · https://doi.org/10.3390/microorganisms12122454 · Nov 2024 | *S. oneidensis* MR-1 context; process includes biological plus abiotic components. |
| nitrite → chemically oxidizes → Fe(II) | “nitrite can chemically oxidize Fe(II)” (hou2024biologicalandchemical pages 1-2) | 10.3390/microorganisms12122454 · https://doi.org/10.3390/microorganisms12122454 · Nov 2024 | Important boundary case: not a direct microbial ET edge; abiotic chemodenitrification component. |
| DIET/MIET mechanisms → transfer electrons from → ANME archaea to sulfate-reducing bacteria | “electrons are transferred to the partner SRBs by various mechanisms, such as MIET and DIET” (zhuang2024electrontransferin pages 10-11) | 10.3390/life14050591 · https://doi.org/10.3390/life14050591 · May 2024 | Community-level syntrophy; extracellular interspecies ET rather than single-cell ETC. |
| sulfate-reducing bacteria → use transferred electrons to → reduce sulfate | “Electrons seem to be transferred to partner SRBs, which use these to reduce sulfate” (zhuang2024electrontransferin pages 10-11) | 10.3390/life14050591 · https://doi.org/10.3390/life14050591 · May 2024 | Strong ecological edge in ANME/SRB consortia. |
| direct electron transfer → proceeds via → outer-membrane c-type cytochromes | “DET is defined as electron movement from bacteria to electrodes independent of external mediators… via outer membrane proteins (c-type cytochromes)” (hazzan2023strategiesforenhancing pages 2-3) | 10.3390/app132312760 · https://doi.org/10.3390/app132312760 · Nov 2023 | Review-level synthesis; electrode-focused assay context. |
| mediated extracellular electron transfer → uses → soluble redox shuttles | “Mediated EET is exemplified by secreted redox shuttles such as pyocyanin” (hazzan2023strategiesforenhancing pages 2-3) | 10.3390/app132312760 · https://doi.org/10.3390/app132312760 · Nov 2023 | Review-level generalization; mediator identity is taxon-specific. |


*Table: This table lists curation-ready subject–predicate–object edges for microbial electron transfer, spanning intracellular respiratory chains, extracellular electron transfer, and interspecies electron transfer. It pairs each proposed edge with a supporting snippet, DOI-first reference, and notes on scope, taxon specificity, and uncertainty.*

### Visual evidence
Ford & TerAvest provide a schematic (Figure 1) of **bidirectional electron flow through the MtrCAB/CymA-centered EET network** (outer membrane conduit → periplasmic carriers → inner membrane quinone pool), which is directly relevant for curating nodes and edges connecting electrodes/cathodes to intracellular redox pools (ford2024theelectrontransport media 74995b43).

### Expert opinions / authoritative synthesis (with curation implications)
- **EET as a definable functional mechanism**: The peer-reviewed framing of EET as electron exchange with an external redox-active material supports curating EET as a process node distinct from general intracellular respiration (ford2024theelectrontransport pages 1-2).
- **Measurement and operationalization**: Electrochemical toolkits (CV, EIS, chronoamperometry) are emphasized as standard approaches to quantify EET performance and biofilm charge transfer properties (hazzan2023strategiesforenhancing pages 2-3). This supports including **assay condition nodes** (poised potential, electrode material) to avoid over-generalizing mechanistic edges.
- **Structural basis of long-range ET**: The comparative structural claim that stacked hemes enable efficient electron transfer in cytochrome filaments supports an edge from “stacked multiheme architecture” to “long-distance electron transfer,” but some functional assignments in archaea remain inferential and should be marked uncertain (baquero2023extracellularcytochromenanowires pages 10-11).

### Warnings / “do not yet curate” items
1. **Archaeal ECN function**: Baquero et al. state it is “very likely” archaeal ECNs function in long-distance electron transfer; without direct conductivity/physiology in the target archaeon, curate as **uncertain** or as “putative” (baquero2023extracellularcytochromenanowires pages 10-11).
2. **Abiotic redox steps inside ‘electron transfer’ contexts**: In nitrate-reducing Fe(II) oxidation systems, nitrite can chemically oxidize Fe(II). This is important but should be represented as an **abiotic edge** (chemical oxidation) rather than microbial electron transfer per se (hou2024biologicalandchemical pages 1-2).
3. **Electrosynthesis constraints are design-specific**: Oxygen effects (beneficial at trace; lethal at high) depend on cathode potential/system design and should be captured with explicit experimental context nodes (ford2024theelectrontransport pages 1-2).

---

## DOI-first bibliography (selected; 2023–2024 prioritized)
- Ford KC, TerAvest MA. *The electron transport chain of Shewanella oneidensis MR-1 can operate bidirectionally to enable microbial electrosynthesis.* **Applied and Environmental Microbiology**. **Jan 2024**. DOI:10.1128/aem.01387-23. URL: https://doi.org/10.1128/aem.01387-23 (ford2024theelectrontransport pages 1-2, ford2024theelectrontransport pages 2-5, ford2024theelectrontransport media 74995b43)
- Baquero DP, et al. *Extracellular cytochrome nanowires appear to be ubiquitous in prokaryotes.* **Cell**. **Jun 2023**. DOI:10.1016/j.cell.2023.05.012. URL: https://doi.org/10.1016/j.cell.2023.05.012 (baquero2023extracellularcytochromenanowires pages 10-11)
- Trani JMD, et al. *Structure of the bc1–cbb3 respiratory supercomplex from Pseudomonas aeruginosa.* **PNAS**. **Sep 2023**. DOI:10.1073/pnas.2307093120. URL: https://doi.org/10.1073/pnas.2307093120 (trani2023structureofthe pages 1-2)
- Grivennikova VG, et al. *Proton-Translocating NADH–Ubiquinone Oxidoreductase: Interaction with Artificial Electron Acceptors, Inhibitors, and Potential Medicines.* **IJMS**. **Dec 2024**. DOI:10.3390/ijms252413421. URL: https://doi.org/10.3390/ijms252413421 (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2)
- Uribe-Ramírez D, et al. *Modifications of the respiratory chain of Bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism.* **Journal of Bioenergetics and Biomembranes**. **Nov 2024**. DOI:10.1007/s10863-024-10041-y. URL: https://doi.org/10.1007/s10863-024-10041-y (uriberamirez2024modificationsofthe pages 11-12)
- Hou L, et al. *Biological and Chemical Processes of Nitrate Reduction and Ferrous Oxidation Mediated by Shewanella oneidensis MR-1.* **Microorganisms**. **Nov 2024**. DOI:10.3390/microorganisms12122454. URL: https://doi.org/10.3390/microorganisms12122454 (hou2024biologicalandchemical pages 1-2)
- Zhuang X, et al. *Electron Transfer in the Biogeochemical Sulfur Cycle.* **Life**. **May 2024**. DOI:10.3390/life14050591. URL: https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 10-11)
- Hazzan OOT, Zhao B, Xiao Y. *Strategies for Enhancing Extracellular Electron Transfer in Environmental Biotechnology: A Review.* **Applied Sciences**. **Nov 2023**. DOI:10.3390/app132312760. URL: https://doi.org/10.3390/app132312760 (hazzan2023strategiesforenhancing pages 2-3)

(Additional contextual sources in evidence set include dissertations/theses and non-journal texts; use cautiously for TraitMech curation unless corroborated by peer-reviewed sources.)

References

1. (ford2024theelectrontransport pages 1-2): Kathryne C. Ford and Michaela A. TerAvest. The electron transport chain of <i>shewanella oneidensis</i> mr-1 can operate bidirectionally to enable microbial electrosynthesis. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01387-23, doi:10.1128/aem.01387-23. This article has 34 citations and is from a peer-reviewed journal.

2. (trani2023structureofthe pages 1-2): Justin M. Di Trani, Andreea A. Gheorghita, Madison Turner, Peter Brzezinski, Pia Ädelroth, Siavash Vahidi, P. Lynne Howell, and John L. Rubinstein. Structure of the bc1–cbb3 respiratory supercomplex from pseudomonas aeruginosa. Proceedings of the National Academy of Sciences of the United States of America, Sep 2023. URL: https://doi.org/10.1073/pnas.2307093120, doi:10.1073/pnas.2307093120. This article has 18 citations and is from a highest quality peer-reviewed journal.

3. (hazzan2023strategiesforenhancing pages 2-3): Oluwadamilola Oluwatoyin Hazzan, Biyi Zhao, and Yong Xiao. Strategies for enhancing extracellular electron transfer in environmental biotechnology: a review. Applied Sciences, 13:12760, Nov 2023. URL: https://doi.org/10.3390/app132312760, doi:10.3390/app132312760. This article has 45 citations.

4. (zhuang2024electrontransferin pages 10-11): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

5. (ford2024theelectrontransport pages 2-5): Kathryne C. Ford and Michaela A. TerAvest. The electron transport chain of <i>shewanella oneidensis</i> mr-1 can operate bidirectionally to enable microbial electrosynthesis. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01387-23, doi:10.1128/aem.01387-23. This article has 34 citations and is from a peer-reviewed journal.

6. (grivennikova2024protontranslocatingnadh–ubiquinoneoxidoreductase pages 1-2): Vera G. Grivennikova, Grigory V. Gladyshev, Tatyana V. Zharova, and Vitaliy B. Borisov. Proton-translocating nadh–ubiquinone oxidoreductase: interaction with artificial electron acceptors, inhibitors, and potential medicines. International Journal of Molecular Sciences, 25:13421, Dec 2024. URL: https://doi.org/10.3390/ijms252413421, doi:10.3390/ijms252413421. This article has 7 citations.

7. (ford2024theelectrontransport media 74995b43): Kathryne C. Ford and Michaela A. TerAvest. The electron transport chain of <i>shewanella oneidensis</i> mr-1 can operate bidirectionally to enable microbial electrosynthesis. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01387-23, doi:10.1128/aem.01387-23. This article has 34 citations and is from a peer-reviewed journal.

8. (baquero2023extracellularcytochromenanowires pages 10-11): Diana P. Baquero, Virginija Cvirkaite-Krupovic, Shengen Shawn Hu, Jessie Lynda Fields, Xing Liu, Christopher Rensing, Edward H. Egelman, Mart Krupovic, and Fengbin Wang. Extracellular cytochrome nanowires appear to be ubiquitous in prokaryotes. Cell, 186:2853-2864.e8, Jun 2023. URL: https://doi.org/10.1016/j.cell.2023.05.012, doi:10.1016/j.cell.2023.05.012. This article has 89 citations and is from a highest quality peer-reviewed journal.

9. (uriberamirez2024modificationsofthe pages 11-12): Daniel Uribe-Ramírez, Lucero Romero-Aguilar, Héctor Vázquez-Meza, Eliseo Cristiani-Urbina, and Juan Pablo Pardo. Modifications of the respiratory chain of bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. Journal of Bioenergetics and Biomembranes, 56:591-605, Nov 2024. URL: https://doi.org/10.1007/s10863-024-10041-y, doi:10.1007/s10863-024-10041-y. This article has 1 citations and is from a peer-reviewed journal.

10. (mouhib2023engineeringextracellularelectron pages 17-20): Mohammed Mouhib. Engineering extracellular electron transfer for enhanced energy harvesting in microbial electrochemical devices. Dissertation, Jan 2023. URL: https://doi.org/10.5075/epfl-thesis-10049, doi:10.5075/epfl-thesis-10049. This article has 0 citations.

11. (mouhib2023engineeringextracellularelectron pages 20-23): Mohammed Mouhib. Engineering extracellular electron transfer for enhanced energy harvesting in microbial electrochemical devices. Dissertation, Jan 2023. URL: https://doi.org/10.5075/epfl-thesis-10049, doi:10.5075/epfl-thesis-10049. This article has 0 citations.

12. (giordano2024nitricoxideand pages 8-13): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

13. (walters2024spectroscopicinvestigationsof pages 21-25): R Walters. Spectroscopic investigations of mycobacterial cytochromes. Unknown journal, 2024.

14. (mouhib2023engineeringextracellularelectron pages 74-77): Mohammed Mouhib. Engineering extracellular electron transfer for enhanced energy harvesting in microbial electrochemical devices. Dissertation, Jan 2023. URL: https://doi.org/10.5075/epfl-thesis-10049, doi:10.5075/epfl-thesis-10049. This article has 0 citations.

15. (hou2024biologicalandchemical pages 1-2): Lingyu Hou, Xiangyu Bai, Zihe Sima, Jiani Zhang, Luyao Yan, Ding Li, and Yongguang Jiang. Biological and chemical processes of nitrate reduction and ferrous oxidation mediated by shewanella oneidensis mr-1. Microorganisms, 12:2454, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122454, doi:10.3390/microorganisms12122454. This article has 6 citations.

16. (mouhib2023engineeringextracellularelectron pages 72-74): Mohammed Mouhib. Engineering extracellular electron transfer for enhanced energy harvesting in microbial electrochemical devices. Dissertation, Jan 2023. URL: https://doi.org/10.5075/epfl-thesis-10049, doi:10.5075/epfl-thesis-10049. This article has 0 citations.

17. (donald2023decipheringtheenergetics pages 35-40): CR Donald. Deciphering the energetics of phytophthora agathidicida and neisseria gonorrhoeae to discover new inhibitors of respiration. Unknown journal, 2023.

18. (mouhib2023engineeringextracellularelectron pages 44-48): Mohammed Mouhib. Engineering extracellular electron transfer for enhanced energy harvesting in microbial electrochemical devices. Dissertation, Jan 2023. URL: https://doi.org/10.5075/epfl-thesis-10049, doi:10.5075/epfl-thesis-10049. This article has 0 citations.