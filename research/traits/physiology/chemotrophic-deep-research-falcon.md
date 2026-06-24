---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:13:47.603197'
end_time: '2026-06-18T11:44:07.670069'
duration_seconds: 1820.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemotrophic
  trait_identifier: METPO:1000641
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from chemical oxidation
    of either inorganic or organic compounds.
  parent_traits: METPO:1000631
  synonyms: TT_chemotroph, chemotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia
    chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008:
    free energy of a redox reaction (Review supports chemical redox reactions as energy
    sources for respiratory energy conservation.)'
  causal_graph_summary: 'chemotrophic_chemical_redox_energy: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemotrophic
- **METPO identifier:** METPO:1000641
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_chemotroph, chemotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports chemical redox reactions as energy sources for respiratory energy conservation.)
- **Existing causal graph summary:** chemotrophic_chemical_redox_energy: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **chemotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotrophic.yaml`.

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
- **Trait label:** chemotrophic
- **METPO identifier:** METPO:1000641
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_chemotroph, chemotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports chemical redox reactions as energy sources for respiratory energy conservation.)
- **Existing causal graph summary:** chemotrophic_chemical_redox_energy: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **chemotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **chemotrophic** (METPO:1000641)

### 0. Trait record
- **Trait label:** chemotrophic  
- **METPO ID:** METPO:1000641  
- **Definition (given):** “A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.”  
- **Trait category:** PHYSIOLOGY  

---

## 1. Scope summary (TraitMech curation focus)

**Chemotrophic** is best treated as an *energy-source phenotype axis*: organisms are chemotrophic when they derive energy from **chemical reactions** (in practice, chemical **redox** reactions), in contrast to phototrophs, which derive energy from sunlight. (yousavich2024effectsoftransient pages 21-25)

Mechanistically, the trait is expressed through the ability to couple **electron donor (ED)** oxidation to **terminal electron acceptor (TEA)** reduction and conserve the released free energy, typically by **electron transport chain (ETC)**-driven generation of a **proton gradient/proton motive force (pmf)** that drives **ATP synthesis**. (yousavich2024effectsoftransient pages 21-25, simon2008theorganisationof pages 1-3)

**Boundary cases / nearby traits:**
- **Chemoautotrophy vs chemoheterotrophy:** autotrophy/heterotrophy describes *carbon source* (CO2 vs organic carbon), while chemotrophy/phototrophy describes *energy source*; these combine into “four general metabolic genres.” (yousavich2024effectsoftransient pages 21-25)
- **Respiration vs fermentation:** respiration uses an ETC and TEA; “fermentation … does not involve an electron transport chain (and thus does not need a TEA).” (yousavich2024effectsoftransient pages 21-25)
- **Chemolithotrophy vs chemoorganotrophy:** distinguished by inorganic vs organic electron donors; examples of inorganic EDs (NH4+, Fe2+, H2S) are explicitly given for chemoautotrophs. (yousavich2024effectsoftransient pages 25-30)

---

## 2. Key concepts & definitions (current understanding)

### 2.1 Redox framing (ED/TEA)
Catabolic pathways are organized by ED and TEA: “The specific pathways of catabolism differ depending on the electron donor (ED) and terminal electron acceptor (TEA).” (yousavich2024effectsoftransient pages 21-25)

### 2.2 Canonical chemotrophic energy conservation mechanism
A concise mechanistic chain supported by text:
- Electrons are stored in carriers (example NADPH): “electrons are first stored in a transfer molecule such as … (NADPH).” (yousavich2024effectsoftransient pages 21-25)
- Carriers feed the ETC: “This molecule then transfers the electrons … to the first molecule of the electron transport chain.” (yousavich2024effectsoftransient pages 21-25)
- ETC redox steps pump protons: “the cell utilizes the energy gained from these redox reaction to pump H+ … across a membrane.” (yousavich2024effectsoftransient pages 21-25)
- Proton gradient makes ATP: “this proton gradient is then used to generate … ATP.” (yousavich2024effectsoftransient pages 21-25)

### 2.3 Foundational bioenergetics (respiratory chemotrophy)
Simon et al. (2008) formalize the general principle for respiratory energy conservation: “the free energy of a redox reaction catalysed by a membrane-bound electron transport chain is transduced via the generation of an electrochemical ion (usually proton) gradient across a coupling membrane that drives ATP synthesis.” (simon2008theorganisationof pages 1-3)

The same review notes alternative mechanisms to build pmf (proton pumping, quinone/quinol cycling, redox loops). (simon2008theorganisationof pages 1-3)

---

## 3. Recent developments & research highlights (prioritizing 2023–2024)

### 3.1 Multi-donor chemolithoautotrophy quantified at hydrothermal vents (2024)
Laufer-Meiser et al. (ISME J, 2024-01; https://doi.org/10.1093/ismejo/wrae173) quantified donor-dependent CO2 fixation by Hydrogenovibrio strain 104:  
- **Thiosulfate-driven:** 1.26×10−4 mmol C ml−1 h−1 (and 23.30 fmol C cell−1 h−1). (laufermeiser2024oxidationofsulfur pages 4-6)  
- **H2-driven:** 5.16×10−6 mmol C ml−1 h−1 (0.29 fmol C cell−1 h−1). (laufermeiser2024oxidationofsulfur pages 4-6)  
- **Fe(II)-driven:** 7.77×10−7 mmol C ml−1 h−1 (0.09 fmol C cell−1 h−1). (laufermeiser2024oxidationofsulfur pages 4-6)  
These measurements provide curation-ready quantitative links from *inorganic electron donor identity* to *autotrophic carbon fixation flux* (chemolithoautotrophic expression of chemotrophy). (laufermeiser2024oxidationofsulfur pages 4-6)

### 3.2 Electrode-driven chemotrophic growth modes (electroautotrophy) in A. ferrooxidans (2024)
Wang et al. (Microorganisms, 2024-03-15; https://doi.org/10.3390/microorganisms12030590) demonstrate that A. ferrooxidans can grow with “electrons supplied by solid electrodes serving as the sole source of energy” and show differential gene expression consistent with distinct extracellular electron uptake routes (pilin/porin/EPS). (wang2024characterizethegrowth pages 1-2)

### 3.3 Bioleaching-focused mechanistic review consolidating ETC→pmf→ATP framing (2024)
Tonietti et al. (Microorganisms, 2024-11; https://doi.org/10.3390/microorganisms12122407) explicitly states: “electrons … can be transferred through the ETC, creating a proton motive force that drives the ATP synthesis.” (tonietti2024unveilingthebioleaching pages 2-4)

---

## 4. Current applications & real-world implementations

### 4.1 Biomining/bioleaching (acidophilic chemolithotrophy)
- A. ferrooxidans is described as widely used in industrial bioleaching; “Bioleaching … is believed to account for **over 30% of global copper production** from low-grade copper ores.” (Wang et al., 2024-03-15; https://doi.org/10.3390/microorganisms12030590) (wang2024characterizethegrowth pages 1-2)
- Tonietti et al. emphasizes bioleaching systems where Fe/S oxidation drives acid generation and metal mobilization (application framing), alongside explicit ETC→pmf→ATP language (mechanistic framing). (tonietti2024unveilingthebioleaching pages 2-4)

### 4.2 Renewable natural gas / biogas upgrading (hydrogenotrophic chemolithotrophy)
Enriquez & Ahring (Appl Environ Microbiol, 2024-04-15; https://doi.org/10.1128/aem.00268-24) report:
- M. wolfeii BSEL “displayed … (0.27 ± 0.03 h−1) using … CO2 … and H2 as electron donor.” (enriquez2024phenotypicandgenomic pages 1-2)
- Bubble column bioreactor: “CO2 conversion efficiency of **97%** and a final methane (CH4) titer of **98.5%v**,” demonstrating biogas upgrading. (enriquez2024phenotypicandgenomic pages 1-2)

---

## 5. Candidate mechanistic entities (nodes) with ontology grounding suggestions

| Node label | Node type | Suggested ontology grounding | Evidence/source (brief) | Notes for curation |
|---|---|---|---|---|
| **Processes / pathways** |  |  |  |  |
| chemotrophy | phenotype | METPO:1000641 | Defined as energy derivation from chemical reactions, contrasted with phototrophy (yousavich2024effectsoftransient pages 21-25) | Core trait node; energy-source axis, not carbon-source axis |
| redox reactions | process | GO:0055114 | Electron transfer through coupled oxidation-reduction reactions drives metabolism (yousavich2024effectsoftransient pages 21-25, simon2008theorganisationof pages 1-3) | Broad mechanistic parent; may be too generic unless linked to ETC/pmf |
| electron donor (ED) | process | label-only candidate | Catabolic pathways differ by ED; examples include reduced carbon, Fe(II), H2, sulfide, thiosulfate (yousavich2024effectsoftransient pages 21-25, yousavich2024effectsoftransient pages 25-30, wang2024characterizethegrowth pages 1-2, laufermeiser2024oxidationofsulfur pages 4-6) | Useful abstract node for general graph |
| terminal electron acceptor (TEA) | process | label-only candidate | Catabolic pathways differ by TEA; O2, nitrate, Fe(III), sulfate, CO2 discussed (yousavich2024effectsoftransient pages 21-25, yousavich2024effectsoftransient pages 25-30, enriquez2024phenotypicandgenomic pages 1-2) | Useful abstract node for general graph |
| electron transport chain | process | GO:0022900 | Electrons pass through ETC to TEA; ETC creates proton motive force (yousavich2024effectsoftransient pages 21-25, tonietti2024unveilingthebioleaching pages 2-4) | Central mechanistic node |
| proton gradient / proton motive force | process | GO:0015986 | Redox energy pumps H+ across membrane to build pmf that drives ATP synthesis (yousavich2024effectsoftransient pages 21-25, simon2008theorganisationof pages 1-3) | Consider separate nodes for proton gradient and pmf only if needed |
| ATP synthesis coupled proton transport | process | GO:0015986 / GO:0046933 | pmf drives ATP synthesis in respiration (yousavich2024effectsoftransient pages 21-25, simon2008theorganisationof pages 1-3) | ATP synthase complex itself not directly named in all sources, but ATP generation from pmf is explicit |
| glycolysis | pathway | MetaCyc:GLYCOLYSIS / KEGG:map00010 | Glucose converted to pyruvate with ATP and NADH generation (yousavich2024effectsoftransient pages 21-25) | Chemoorganotrophic submechanism, not universal to all chemotrophs |
| Krebs cycle / citric acid cycle | pathway | GO:0006099 / KEGG:map00020 | Pyruvate enters Krebs cycle to produce ATP and NADH (yousavich2024effectsoftransient pages 21-25) | Chemoorganotrophic submechanism |
| fermentation | pathway | GO:0006113 | Alternative to Krebs cycle; does not involve ETC and does not need a TEA (yousavich2024effectsoftransient pages 21-25) | Boundary case: may or may not be included under broad chemotrophy depending ontology policy |
| extracellular electron transfer | process | GO:0097009 (candidate) / label-only candidate | Iron reducers must transfer electrons extracellularly; A. ferrooxidans electroautotrophy uses direct electron transfer machinery (yousavich2024effectsoftransient pages 25-30, wang2024characterizethegrowth pages 1-2) | Curate as process if broad chemotrophy graph includes electrode/mineral electron uptake |
| Calvin–Benson–Bassham cycle | pathway | GO:0019253 / KEGG:map00710 | A. ferrooxidans uses CO2 fixation via CBB; autotrophic CO2 fixation in chemolithotrophs (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4) | Subtype-specific: chemoautotrophs, not all chemotrophs |
| bioleaching / biomining | phenotype | label-only candidate | A. ferrooxidans used in industrial bioleaching/biomining (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4) | Application node rather than core mechanism |
| **Proteins / complexes / enzymes** |  |  |  |  |
| ATP synthase | protein complex | GO:0045259 | Proton gradient used to generate ATP; ATP synthesis explicitly pmf-driven (yousavich2024effectsoftransient pages 21-25, simon2008theorganisationof pages 1-3) | Complex not named in all excerpts; still strongly implied by standard respiratory coupling |
| quinone/quinol | chemical | CHEBI:16389 (ubiquinone, candidate) / label-only candidate | Quinone/quinol cycling and redox loops generate pmf (simon2008theorganisationof pages 1-3, simon2008theorganisationof pages 3-5) | May need split into ubiquinone vs menaquinone in later curation |
| rusticyanin (Rus) | protein | UniProt family candidate / label-only candidate | Fe(II) electrons flow from Cyc2 to rusticyanin in A. ferrooxidans (wang2024characterizethegrowth pages 1-2) | Taxon-specific but direct mechanistic evidence |
| Cyc2 | protein | label-only candidate | Outer-membrane cytochrome c oxidizes Fe2+ to Fe3+ in A. ferrooxidans (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4) | Strong, species-specific node |
| Cyc1 | protein | label-only candidate | Downhill pathway includes Rus → Cyc1 → Cox (wang2024characterizethegrowth pages 1-2) | Species-specific respiratory component |
| cytochrome aa3 oxidase / Cox | protein complex | GO:0004129 (cytochrome-c oxidase activity, candidate) | Terminal step in A. ferrooxidans downhill pathway to O2 (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4) | Terminal oxidase node useful for oxic chemotrophy |
| bc1 complex | protein complex | GO:0008121 / GO:0005750 analog candidate | Mentioned as ETC component in A. ferrooxidans; differential roles in iron vs sulfur oxidation (tonietti2024unveilingthebioleaching pages 2-4, tonietti2024unveilingthebioleaching pages 21-23) | Species-specific/substrate-specific respiratory component |
| Sox system | pathway/enzyme system | MetaCyc / KEGG sulfur oxidation pathway candidate | soxAX, soxB, soxCD, soxYZ mediate sulfur compound oxidation (tonietti2024unveilingthebioleaching pages 2-4) | Chemolithotrophic sulfur oxidation module |
| SQR (sulfide:quinone reductase) | enzyme | EC 1.8.5.4 / GO:0008177 candidate | Sulfur oxidation enzyme in A. ferrooxidans; also noted in Hydrogenovibrio context (tonietti2024unveilingthebioleaching pages 2-4, laufermeiser2024oxidationofsulfur pages 4-6) | Good mechanistic node for sulfide-driven chemotrophy |
| SDO (sulfur dioxygenase) | enzyme | EC 1.13.11.18 (candidate) | Sulfur oxidation enzyme in A. ferrooxidans (tonietti2024unveilingthebioleaching pages 2-4) | Sulfur oxidation submodule |
| RubisCO | enzyme | EC 4.1.1.39 / GO:0016984 | Key carboxylating enzyme in autotrophic CO2 fixation; activity measured in Hydrogenovibrio (laufermeiser2024oxidationofsulfur pages 4-6) | Chemoautotrophy-specific, not universal |
| hydrogenases ([NiFe] group 1 and 2b) | enzyme | EC 1.12.-.- / UniProt family candidate | Hydrogenovibrio possesses [NiFe]-hydrogenases; genes upregulated on H2 (laufermeiser2024oxidationofsulfur pages 4-6) | H2 chemotrophy module; taxon-specific examples |
| TonB-dependent receptor | protein | GO:0009275 / label-only candidate | Upregulated during Fe(II) growth in Hydrogenovibrio, linked to Fe transport/acquisition (laufermeiser2024oxidationofsulfur pages 4-6) | Likely accessory rather than core chemotrophy node |
| pili / type IV pili | protein structure | GO:0009289 / label-only candidate | More pili under electroautotrophic growth; implicated in direct electron transfer (wang2024characterizethegrowth pages 1-2) | Curate as EEU-associated, not universal chemotrophy |
| EPS / biofilm | phenotype | GO:0042710 / GO:0042710-like candidate | More EPS under electrode growth; biofilms aid attachment and bioleaching (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4) | Important for mineral/electrode-associated chemotrophy, not universal |
| NADH / NADPH | chemical | CHEBI:57945 (NADH), CHEBI:57783 (NADPH) | Electron carriers store electrons from ED and feed ETC (yousavich2024effectsoftransient pages 21-25, simon2008theorganisationof pages 1-3) | Consider separate nodes if needed |
| **Chemicals** |  |  |  |  |
| Fe(II) / ferrous iron | chemical | CHEBI:29033 | A. ferrooxidans and Hydrogenovibrio use Fe(II) as electron donor (wang2024characterizethegrowth pages 1-2, laufermeiser2024oxidationofsulfur pages 4-6, tonietti2024unveilingthebioleaching pages 2-4) | Strong chemolithotrophic donor node |
| Fe(III) / ferric iron | chemical | CHEBI:29034 | Product of Fe(II) oxidation; also TEA under anaerobic conditions in A. ferrooxidans (wang2024characterizethegrowth pages 1-2, yousavich2024effectsoftransient pages 25-30) | Donor-product and acceptor roles; context-dependent |
| thiosulfate | chemical | CHEBI:30087 | Oxidized by Hydrogenovibrio and A. ferrooxidans sulfur pathways (laufermeiser2024oxidationofsulfur pages 4-6, tonietti2024unveilingthebioleaching pages 2-4) | Strong sulfur chemotrophy donor node |
| sulfide | chemical | CHEBI:16133 | Oxidized sulfur donor; sulfur oxidation produces sulfate and protons (yousavich2024effectsoftransient pages 25-30, tonietti2024unveilingthebioleaching pages 2-4) | Can be toxic and energetic substrate |
| oxygen | chemical | CHEBI:15379 | Most favorable TEA; terminal acceptor in aerobic chemotrophy (yousavich2024effectsoftransient pages 21-25, tonietti2024unveilingthebioleaching pages 2-4) | Major oxic chemotrophy acceptor |
| nitrate | chemical | CHEBI:17632 | Next most favorable common TEA after O2 in anoxic environments (yousavich2024effectsoftransient pages 25-30) | Respiratory acceptor; denitrification/DNRA branch |
| sulfate | chemical | CHEBI:16189 | Product of sulfur oxidation and common TEA in anoxic redox cascade (yousavich2024effectsoftransient pages 25-30, tonietti2024unveilingthebioleaching pages 2-4) | Distinguish oxidized sulfur product vs respiratory TEA contexts |
| carbon dioxide (CO2) | chemical | CHEBI:16526 | Autotrophic carbon source; also TEA in hydrogenotrophic methanogenesis (enriquez2024phenotypicandgenomic pages 1-2, yousavich2024effectsoftransient pages 25-30, tonietti2024unveilingthebioleaching pages 2-4) | Multifunctional node; role depends on metabolism |
| hydrogen (H2) | chemical | CHEBI:18276 | Electron donor in hydrogenotrophic methanogens and Hydrogenovibrio (enriquez2024phenotypicandgenomic pages 1-2, laufermeiser2024oxidationofsulfur pages 4-6, tonietti2024unveilingthebioleaching pages 2-4) | Strong chemolithotrophic donor node |
| ammonium (NH4+) | chemical | CHEBI:28938 | Sole nitrogen source supporting M. wolfeii BSEL growth (enriquez2024phenotypicandgenomic pages 1-2) | Nutrient node, not energy node |
| acetate | chemical | CHEBI:30089 | Example strong organic ED; substrate in heterotrophic/methanogenic pathways (yousavich2024effectsoftransient pages 21-25, yousavich2024effectsoftransient pages 25-30) | Chemoorganotrophic donor node |
| lactate | chemical | CHEBI:24996 | Fermentation product and ED for iron reducers (yousavich2024effectsoftransient pages 25-30) | Links fermentation to respiration |
| **Environmental factors / conditions** |  |  |  |  |
| oxic conditions | environmental factor | ENVO:01000324 (oxygenated environment, candidate) | Aerobic chemotrophy with O2 as TEA; A. ferrooxidans aerobic oxidation (yousavich2024effectsoftransient pages 21-25, tonietti2024unveilingthebioleaching pages 2-4) | Broad condition node |
| anoxic conditions | environmental factor | ENVO:01000254 (anoxic environment) | Redox cascade in oxygen-free environments; nitrate, Fe(III), sulfate, methanogenesis (yousavich2024effectsoftransient pages 21-25, yousavich2024effectsoftransient pages 25-30) | Broad condition node |
| hydrothermal vent environment | environmental factor | ENVO:00000215 (hydrothermal vent) | Hydrogenovibrio isolates from deep-sea hydrothermal vents oxidize sulfur, H2, Fe(II) (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2) | Useful ecological context node |
| acid mine drainage | environmental factor | ENVO candidate / label-only candidate | A. ferrooxidans contributes to acidic drainage waters via Fe/S oxidation (tonietti2024unveilingthebioleaching pages 2-4) | Application/environment impact node |
| mineral surface / ore | environmental factor | ENVO candidate / label-only candidate | Biofilms on mineral surfaces facilitate bioleaching and attachment (tonietti2024unveilingthebioleaching pages 2-4, wang2024characterizethegrowth pages 1-2) | Contextual node for biomining graphs |


*Table: This table lists evidence-supported candidate nodes for a chemotrophic TraitMech causal graph, grouped by type and grounded to ontology identifiers where feasible. It highlights broadly curatable core bioenergetic entities as well as narrower, taxon-specific modules relevant to chemolithotrophic examples.*

**Visual evidence (useful for curators):** Tonietti et al. includes schematic figures (acidophile tolerance and bioleaching/ETC context) supporting how ion homeostasis and energy conservation connect to chemolithotrophic lifestyles. (tonietti2024unveilingthebioleaching media cad1dfb2, tonietti2024unveilingthebioleaching media 90e2e134)

---

## 6. Evidence-backed candidate causal edges (triples)

| Subject node | Predicate | Object node | Reference (DOI + URL + pub date) | Supporting snippet (verbatim) | Notes/uncertainty + suggested ontology grounding for subject/object |
|---|---|---|---|---|---|
| chemotroph | derives_energy_from | chemical reactions | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “phototrophs derive energy from sunlight whereas chemotrophs derive energy from chemical reactions.” (yousavich2024effectsoftransient pages 21-25) | Core trait-defining edge. Subject: METPO:1000641. Object: label-only candidate “chemical redox reactions” / GO:0055114 broadly. |
| phototroph | derives_energy_from | sunlight | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “phototrophs derive energy from sunlight whereas chemotrophs derive energy from chemical reactions.” (yousavich2024effectsoftransient pages 21-25) | Boundary edge for disambiguation from chemotrophy. Subject/object are comparator nodes, not part of chemotrophy mechanism proper. |
| catabolic pathway | is_determined_by | electron donor (ED) | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “The specific pathways of catabolism differ depending on the electron donor (ED) and terminal electron acceptor (TEA).” (yousavich2024effectsoftransient pages 21-25) | General mechanistic rule. Subject: label-only “catabolic pathway”; object: label-only ED. |
| catabolic pathway | is_determined_by | terminal electron acceptor (TEA) | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “The specific pathways of catabolism differ depending on the electron donor (ED) and terminal electron acceptor (TEA).” (yousavich2024effectsoftransient pages 21-25) | General mechanistic rule. Subject: label-only “catabolic pathway”; object: label-only TEA. |
| NADPH/NADH | transfers_electrons_to | electron transport chain | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “electrons are first stored in a transfer molecule such as nicotinamide adenine dinucleotide phosphate (NADPH). This molecule then transfers the electrons gained from the ED to the first molecule of the electron transport chain.” (yousavich2024effectsoftransient pages 21-25) | Strong general edge. Subject: CHEBI:57783 (NADPH), CHEBI:57945 (NADH). Object: GO:0022900. |
| electron transport chain | transfers_electrons_to | terminal electron acceptor | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “Then a series of redox reactions, or coupled oxidation and reduction reactions, carry the electron through the transport chain. At the end of this process, the electron is transferred to the TEA” (yousavich2024effectsoftransient pages 21-25) | Core respiration edge. Object TEA label-only. |
| redox reactions in electron transport chain | pumps | H+ across membrane | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “During the electron transfer, the cell utilizes the energy gained from these redox reaction to pump H+ (protons) across a membrane within the cell.” (yousavich2024effectsoftransient pages 21-25) | Central chemotrophic energy-conservation edge. Subject: GO:0055114 + GO:0022900 context. Object: CHEBI:15378 (H+). |
| proton gradient / proton motive force | drives | ATP synthesis | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “In many organisms, this proton gradient is then used to generate adenosine triphosphate (ATP)” (yousavich2024effectsoftransient pages 21-25) | Core edge. Subject: GO:0015986. Object: GO:0015986 / GO:0006754 broadly; ATP CHEBI:15422. |
| fermentation | bypasses | electron transport chain | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “fermentation, which involves direct transformation of substrates to ATP and NADH and does not involve an electron transport chain” (yousavich2024effectsoftransient pages 21-25) | Important boundary case. Subject: GO:0006113. Object: GO:0022900. |
| fermentation | does_not_require | terminal electron acceptor | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “does not involve an electron transport chain (and thus does not need a TEA).” (yousavich2024effectsoftransient pages 21-25) | Important boundary edge for curation. Subject: GO:0006113. Object: label-only TEA. |
| free energy of membrane-bound redox reaction | is_transduced_via_generation_of | electrochemical ion gradient / pmf | Simon et al. 2008. DOI:10.1016/j.bbabio.2008.09.008. URL:https://doi.org/10.1016/j.bbabio.2008.09.008. Published 2008-12 (online 2008-09-30) | “the free energy of a redox reaction catalysed by a membrane-bound electron transport chain is transduced via the generation of an electrochemical ion (usually proton) gradient across a coupling membrane that drives ATP synthesis.” (simon2008theorganisationof pages 1-3) | Foundational bioenergetics edge. Subject/object label-only candidates; pmf core node. |
| proton motive force | has_equation | pmf (mV) = Δψ − 59 ΔpH | Simon et al. 2008. DOI:10.1016/j.bbabio.2008.09.008. URL:https://doi.org/10.1016/j.bbabio.2008.09.008. Published 2008-12 (online 2008-09-30) | “pmf (mV) = Δψ−59 ΔpH” (simon2008theorganisationof pages 1-3) | Useful annotation edge rather than biological causal edge; may be better as note than graph edge. Subject: pmf label/GO:0015986. Object: equation literal. |
| proton motive force | can_be_built_by | quinone/quinol cycling | Simon et al. 2008. DOI:10.1016/j.bbabio.2008.09.008. URL:https://doi.org/10.1016/j.bbabio.2008.09.008. Published 2008-12 (online 2008-09-30) | “The proton motive force (pmf) can be built up by different mechanisms like proton pumping, quinone/quinol cycling or by a redox loop.” (simon2008theorganisationof pages 1-3) | Broad mechanistic edge. Subject: GO:0015986. Object: quinone/quinol cycling label-only; quinone CHEBI class candidate. |
| redox loop | contributes_to_generation_of | proton motive force | Simon et al. 2008. DOI:10.1016/j.bbabio.2008.09.008. URL:https://doi.org/10.1016/j.bbabio.2008.09.008. Published 2008-12 (online 2008-09-30) | “The proton motive force (pmf) can be built up by different mechanisms like proton pumping, quinone/quinol cycling or by a redox loop.” (simon2008theorganisationof pages 1-3) | Broad mechanistic edge. Subject: label-only “redox loop”. Object: GO:0015986. |
| redox loop | couples | electron transport to net proton transfer across membrane | Simon et al. 2008. DOI:10.1016/j.bbabio.2008.09.008. URL:https://doi.org/10.1016/j.bbabio.2008.09.008. Published 2008-12 (online 2008-09-30) | “The latter couples electron transport to a net proton transfer across the membrane without proton pumping.” (simon2008theorganisationof pages 1-3) | Foundational mechanistic edge. Subject label-only. Object label-only proton transfer process. |
| Fe2+ | is_oxidized_by | Cyc2 | Wang et al. 2024. DOI:10.3390/microorganisms12030590. URL:https://doi.org/10.3390/microorganisms12030590. Published 2024-03-15 | “A. ferrooxidans oxidizes Fe2+ to Fe3+ with outer-membrane cytochrome c (Cyc2).” (wang2024characterizethegrowth pages 1-2) | Taxon-specific (A. ferrooxidans). Subject: CHEBI:29033. Object: Cyc2 label-only candidate / cytochrome c family. |
| Cyc2 | transfers_electrons_to | rusticyanin (Rus) | Wang et al. 2024. DOI:10.3390/microorganisms12030590. URL:https://doi.org/10.3390/microorganisms12030590. Published 2024-03-15 | “Electrons then flow toward rusticyanin (Rus)” (wang2024characterizethegrowth pages 1-2) | Taxon-specific. Subject/object label-only protein nodes. |
| rusticyanin (Rus) | transfers_electrons_to | Cyc1 | Wang et al. 2024. DOI:10.3390/microorganisms12030590. URL:https://doi.org/10.3390/microorganisms12030590. Published 2024-03-15 | “The downhill pathway for electron transfer is as follows: Fe2+ →Cyc2 (on outer membrane) →Rus →Cyc1 (cytoplasm) →Cox” (wang2024characterizethegrowth pages 1-2) | Taxon-specific. Subject/object label-only protein nodes. |
| Cyc1 | transfers_electrons_to | Cox (cytochrome aa3 oxidase) | Wang et al. 2024. DOI:10.3390/microorganisms12030590. URL:https://doi.org/10.3390/microorganisms12030590. Published 2024-03-15 | “The downhill pathway for electron transfer is as follows: Fe2+ →Cyc2 (on outer membrane) →Rus →Cyc1 (cytoplasm) →Cox” (wang2024characterizethegrowth pages 1-2) | Taxon-specific. Object could map broadly to cytochrome c oxidase complex / GO:0045277 candidate. |
| downhill Fe2+ oxidation pathway | enables | ATP synthesis | Wang et al. 2024. DOI:10.3390/microorganisms12030590. URL:https://doi.org/10.3390/microorganisms12030590. Published 2024-03-15 | “To ensure the survival of A. ferrooxidans, it is necessary to synthesize sufficient ATP through the downhill pathway” (wang2024characterizethegrowth pages 1-2) | Taxon-specific; mechanistically central for iron chemolithotrophy. Subject label-only pathway node. |
| sox system | participates_in | oxidation of reduced sulfur compounds | Tonietti et al. 2024. DOI:10.3390/microorganisms12122407. URL:https://doi.org/10.3390/microorganisms12122407. Published 2024-11 | “it is also able to oxidize reduced sulfur compounds such as elemental sulfur, thiosulfate, and tetrathionate through different enzymes, e.g., the sox system (soxAX, soxB, soxCD, and soxYZ)” (tonietti2024unveilingthebioleaching pages 2-4) | Taxon-specific/module-specific sulfur chemotrophy edge. Subject: label-only/KEGG sulfur oxidation pathway candidate. |
| sulfide:quinone reductase (SQR) | participates_in | oxidation of reduced sulfur compounds | Tonietti et al. 2024. DOI:10.3390/microorganisms12122407. URL:https://doi.org/10.3390/microorganisms12122407. Published 2024-11 | “through different enzymes, e.g., the sox system (soxAX, soxB, soxCD, and soxYZ), sulfide oxidoreductase (SQR), and sulfur dioxygenase (SDO).” (tonietti2024unveilingthebioleaching pages 2-4) | Taxon-specific/module-specific. Subject: EC 1.8.5.4 candidate. |
| sulfur dioxygenase (SDO) | participates_in | oxidation of reduced sulfur compounds | Tonietti et al. 2024. DOI:10.3390/microorganisms12122407. URL:https://doi.org/10.3390/microorganisms12122407. Published 2024-11 | “through different enzymes, e.g., the sox system (soxAX, soxB, soxCD, and soxYZ), sulfide oxidoreductase (SQR), and sulfur dioxygenase (SDO).” (tonietti2024unveilingthebioleaching pages 2-4) | Taxon-specific/module-specific. Subject: EC 1.13.11.18 candidate. |
| electrons from oxidized inorganic compounds | are_transferred_through | electron transport chain | Tonietti et al. 2024. DOI:10.3390/microorganisms12122407. URL:https://doi.org/10.3390/microorganisms12122407. Published 2024-11 | “A. ferrooxidans is able to derive energy by oxidizing inorganic compounds that release electrons which can be transferred through the ETC” (tonietti2024unveilingthebioleaching pages 2-4) | Strong taxon-specific support for chemotrophic mechanism in bioleaching context. |
| electron transport chain | creates | proton motive force | Tonietti et al. 2024. DOI:10.3390/microorganisms12122407. URL:https://doi.org/10.3390/microorganisms12122407. Published 2024-11 | “transferred through the ETC, creating a proton motive force that drives the ATP synthesis.” (tonietti2024unveilingthebioleaching pages 2-4) | Strong taxon-specific support; aligns with general respiration mechanism. Object: GO:0015986. |
| proton motive force | drives | ATP synthesis | Tonietti et al. 2024. DOI:10.3390/microorganisms12122407. URL:https://doi.org/10.3390/microorganisms12122407. Published 2024-11 | “creating a proton motive force that drives the ATP synthesis.” (tonietti2024unveilingthebioleaching pages 2-4) | Taxon-specific corroboration of general edge. |
| iron reduction | requires | extracellular electron transfer | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “they must perform extracellular electron transfer as the last step of their electron transport chain.” (yousavich2024effectsoftransient pages 25-30) | Broad but especially relevant for mineral-associated chemotrophy. Subject: iron reduction label-only; object: EET label-only. |
| Hydrogenovibrio strain 104 growth on thiosulfate | results_in | CO2 fixation rate 1.26×10−4 mmol C ml−1 h−1 | Laufer-Meiser et al. 2024. DOI:10.1093/ismejo/wrae173. URL:https://doi.org/10.1093/ismejo/wrae173. Published 2024-01 | “S2O32−oxidation strain 104 1.26x10−4 ± 9.31x10−6 mmol C-fixation ml−1 h−1” (laufermeiser2024oxidationofsulfur pages 4-6) | Taxon-specific quantitative edge. Good for demonstrating donor-dependent chemotrophy. Subject: thiosulfate growth condition label-only. |
| Hydrogenovibrio strain 104 growth on H2 | results_in | CO2 fixation rate 5.16×10−6 mmol C ml−1 h−1 | Laufer-Meiser et al. 2024. DOI:10.1093/ismejo/wrae173. URL:https://doi.org/10.1093/ismejo/wrae173. Published 2024-01 | “H2 oxidation strain 104 5.16x10−6 ± 3.27x10−7 mmol C-fixation ml−1 h−1” (laufermeiser2024oxidationofsulfur pages 4-6) | Taxon-specific quantitative edge. |
| Hydrogenovibrio strain 104 growth on Fe(II) | results_in | CO2 fixation rate 7.77×10−7 mmol C ml−1 h−1 | Laufer-Meiser et al. 2024. DOI:10.1093/ismejo/wrae173. URL:https://doi.org/10.1093/ismejo/wrae173. Published 2024-01 | “Fe(II) oxidation strain 104 7.77x10−7 ± 7.52x10−7 mmol C-fixation ml−1 h−1” (laufermeiser2024oxidationofsulfur pages 4-6) | Taxon-specific quantitative edge. Together with previous two rows, captures donor-dependent energy yield differences. |
| H2 | serves_as_electron_donor_for_reduction_of | CO2 to CH4 | Enriquez & Ahring 2024. DOI:10.1128/aem.00268-24. URL:https://doi.org/10.1128/aem.00268-24. Published 2024-04-15 | “Hydrogenotrophic methanogens use H2 as electron donor for the reduction of CO2 into CH4.” (enriquez2024phenotypicandgenomic pages 1-2) | Taxon-group specific (hydrogenotrophic methanogens), but broadly relevant chemolithotrophy edge. Subject: CHEBI:18276. Object: CO2 reduction to methane label-only process; CO2 CHEBI:16526; CH4 CHEBI:16183. |
| M. wolfeii BSEL growth on CO2 + H2 | has_specific_growth_rate | 0.27 ± 0.03 h−1 | Enriquez & Ahring 2024. DOI:10.1128/aem.00268-24. URL:https://doi.org/10.1128/aem.00268-24. Published 2024-04-15 | “M. wolfeii BSEL displayed the highest specific growth rate ever reported for the wolfeii species (0.27 ± 0.03 h−1) using carbon dioxide (CO2) as unique carbon source and hydrogen (H2) as electron donor.” (enriquez2024phenotypicandgenomic pages 1-2) | Taxon-specific phenotype edge. Good quantitative application evidence. |
| M. wolfeii BSEL bubble-column fermentation with synthetic biogas mimic + H2 | achieves | 97% CO2 conversion efficiency | Enriquez & Ahring 2024. DOI:10.1128/aem.00268-24. URL:https://doi.org/10.1128/aem.00268-24. Published 2024-04-15 | “resulted in a CO2 conversion efficiency of 97%” (enriquez2024phenotypicandgenomic pages 1-2) | Application edge, not core TraitMech. Taxon-specific. |
| M. wolfeii BSEL bubble-column fermentation with synthetic biogas mimic + H2 | achieves | final methane titer 98.5% v/v | Enriquez & Ahring 2024. DOI:10.1128/aem.00268-24. URL:https://doi.org/10.1128/aem.00268-24. Published 2024-04-15 | “and a final methane (CH4) titer of 98.5%v” (enriquez2024phenotypicandgenomic pages 1-2) | Application edge, not core TraitMech. Taxon-specific. |
| chemoautotroph | uses | inorganic reactions instead of light for energy derivation | Yousavich 2024. DOI unavailable in provided context. URL unavailable in provided context. 2024 | “chemoautotrophic organisms conduct CO2 fixation to build biomass, but inorganic reactions are used in energy derivation instead of light.” (yousavich2024effectsoftransient pages 25-30) | Useful subtype edge for distinguishing chemoautotrophy from generic chemotrophy and photoautotrophy. Subject label-only chemautotroph subtype. |


*Table: This table compiles candidate subject–predicate–object edges for a TraitMech graph of chemotrophy, with verbatim supporting snippets, source details, and curation notes. It covers core bioenergetics, boundary cases, and taxon-specific exemplar mechanisms and applications.*

---

## 7. Expert opinions / authoritative synthesis (interpretation for curation)

1. **Trait as a mechanistic capacity rather than environment:** The chemotrophic trait is not tied to a single habitat but to a conserved *bioenergetic logic*: ED→ETC→pmf→ATP (respiration) with optional variants (redox loops; quinone cycling) that change stoichiometry and coupling. (simon2008theorganisationof pages 1-3, yousavich2024effectsoftransient pages 21-25)
2. **Use ED/TEA abstraction as graph backbone:** Because chemotrophy spans diverse metabolisms, representing ED and TEA as abstract nodes allows reuse across chemolithoautotrophy (Fe2+, H2, sulfur compounds) and chemoorganotrophy (organic donors), while remaining compatible with taxon-specific instantiations (e.g., Cyc2/Rus/Cox in A. ferrooxidans). (yousavich2024effectsoftransient pages 21-25, wang2024characterizethegrowth pages 1-2)
3. **Prefer modular subgraphs for ‘chemolithotrophic exemplars’:** The A. ferrooxidans iron-oxidation chain and sulfur oxidation enzyme sets are strong mechanistic exemplars but are taxon-specific; curating them as optional modules avoids overgeneralizing. (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4)

---

## 8. Statistics and quantitative data (recent studies)

- **Hydrogenovibrio CO2 fixation (2024):** 1.26×10−4 (thiosulfate), 5.16×10−6 (H2), 7.77×10−7 (Fe(II)) mmol C ml−1 h−1 for strain 104. (laufermeiser2024oxidationofsulfur pages 4-6)
- **M. wolfeii BSEL growth rate (2024):** μ = 0.27 ± 0.03 h−1 on CO2 (carbon source) with H2 (electron donor). (enriquez2024phenotypicandgenomic pages 1-2)
- **Biogas upgrading performance (2024):** 97% CO2 conversion efficiency; 98.5% v/v methane titer in bubble column gas fermentation. (enriquez2024phenotypicandgenomic pages 1-2)
- **Industrial bioleaching relevance (2024):** “over 30% of global copper production from low-grade copper ores” attributed to bioleaching mediated by microbiomes (application statistic). (wang2024characterizethegrowth pages 1-2)

---

## 9. Warnings / curation cautions

1. **DOI and peer-review status:** The Yousavich (2024) text used for several definitions/quotes appears as a nonstandard “Unknown journal” source in this workspace; despite being internally consistent and citing established literature, its provenance/peer-review status is unclear. Treat edges supported only by this source as *provisional* until cross-checked against a peer-reviewed review or textbook chapter with DOI. (yousavich2024effectsoftransient pages 21-25, yousavich2024effectsoftransient pages 25-30)
2. **Taxon-specific mechanisms:** Cyc2/Rus/Cyc1/Cox chains and specific sulfur oxidation gene sets (sox, SQR, SDO) should be curated as *taxon- or clade-specific modules* (e.g., Acidithiobacillaceae) rather than universal chemotrophy machinery. (wang2024characterizethegrowth pages 1-2, tonietti2024unveilingthebioleaching pages 2-4)
3. **Application nodes vs trait mechanism:** Bioleaching/biomining and biogas upgrading are valuable “implementation” contexts, but should not be conflated with the core trait definition unless TraitMech explicitly includes “functions in X application.” (wang2024characterizethegrowth pages 1-2, enriquez2024phenotypicandgenomic pages 1-2)
4. **Electroautotrophy / extracellular electron uptake:** Evidence supports electrode-driven growth and EEU-associated structures (pili/porins/EPS), but whether these are part of a generalized chemotrophy graph or a separate “electrotrophic/electroautotrophic” extension should be decided by ontology scope. (wang2024characterizethegrowth pages 1-2)

---

## 10. DOI-first bibliography (with URLs and publication dates where available)

1. **Wang Q, Long H, Wang H, Lau Vetter MCY.** *Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions.* **Microorganisms** (Published **2024-03-15**). DOI: **10.3390/microorganisms12030590**. URL: https://doi.org/10.3390/microorganisms12030590 (wang2024characterizethegrowth pages 1-2)

2. **Tonietti L, Esposito M, Cascone M, et al.** *Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.* **Microorganisms** (Published **2024-11**). DOI: **10.3390/microorganisms12122407**. URL: https://doi.org/10.3390/microorganisms12122407 (tonietti2024unveilingthebioleaching pages 2-4)

3. **Laufer-Meiser K, Alawi M, Böhnke S, et al.** *Oxidation of sulfur, hydrogen, and iron by metabolically versatile Hydrogenovibrio from deep sea hydrothermal vents.* **The ISME Journal** (Published **2024-01**). DOI: **10.1093/ismejo/wrae173**. URL: https://doi.org/10.1093/ismejo/wrae173 (laufermeiser2024oxidationofsulfur pages 4-6)

4. **Enriquez FA, Ahring BK.** *Phenotypic and genomic characterization of Methanothermobacter wolfeii strain BSEL, a CO2-capturing archaeon with minimal nutrient requirements.* **Applied and Environmental Microbiology** (Published **2024-04-15**). DOI: **10.1128/aem.00268-24**. URL: https://doi.org/10.1128/aem.00268-24 (enriquez2024phenotypicandgenomic pages 1-2)

5. **Simon J, van Spanning RJM, Richardson DJ.** *The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems.* **Biochimica et Biophysica Acta** (Online **2008-09-30**, issue **2008-12**). DOI: **10.1016/j.bbabio.2008.09.008**. URL: https://doi.org/10.1016/j.bbabio.2008.09.008 (simon2008theorganisationof pages 1-3)

6. **Yousavich DJ.** *Effects of transient deoxygenation on sulfur cycling in aquatic systems.* (2024; DOI/URL not available in provided context). Used here for definitions and mechanistic narrative; should be cross-validated. (yousavich2024effectsoftransient pages 21-25, yousavich2024effectsoftransient pages 25-30)


References

1. (yousavich2024effectsoftransient pages 21-25): DJ Yousavich. Effects of transient deoxygenation on sulfur cycling in aquatic systems. Unknown journal, 2024.

2. (simon2008theorganisationof pages 1-3): Jörg Simon, Rob J.M. van Spanning, and David J. Richardson. The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems. Biochimica et biophysica acta, 1777 12:1480-90, Dec 2008. URL: https://doi.org/10.1016/j.bbabio.2008.09.008, doi:10.1016/j.bbabio.2008.09.008. This article has 228 citations.

3. (yousavich2024effectsoftransient pages 25-30): DJ Yousavich. Effects of transient deoxygenation on sulfur cycling in aquatic systems. Unknown journal, 2024.

4. (laufermeiser2024oxidationofsulfur pages 4-6): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 8 citations.

5. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

6. (tonietti2024unveilingthebioleaching pages 2-4): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 44 citations.

7. (enriquez2024phenotypicandgenomic pages 1-2): Fuad Ale Enriquez and Birgitte K. Ahring. Phenotypic and genomic characterization of <i>methanothermobacter wolfeii</i> strain bsel, a co <sub>2</sub> -capturing archaeon with minimal nutrient requirements. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00268-24, doi:10.1128/aem.00268-24. This article has 11 citations and is from a peer-reviewed journal.

8. (simon2008theorganisationof pages 3-5): Jörg Simon, Rob J.M. van Spanning, and David J. Richardson. The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems. Biochimica et biophysica acta, 1777 12:1480-90, Dec 2008. URL: https://doi.org/10.1016/j.bbabio.2008.09.008, doi:10.1016/j.bbabio.2008.09.008. This article has 228 citations.

9. (tonietti2024unveilingthebioleaching pages 21-23): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 44 citations.

10. (laufermeiser2024oxidationofsulfur pages 1-2): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 8 citations.

11. (tonietti2024unveilingthebioleaching media cad1dfb2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 44 citations.

12. (tonietti2024unveilingthebioleaching media 90e2e134): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 44 citations.