---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:44:18.973866'
end_time: '2026-08-04T12:03:39.928908'
duration_seconds: 1160.96
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photoautotrophic
  trait_identifier: METPO:1000656
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of light as the energy source
    and carbon dioxide as the primary carbon source for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation,
    anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation,
    photoautotroph, photoautotrophy
  evidence_summary: 'DOI:10.3390/life10050071: capture solar energy (Review supports
    cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10:
    Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson
    cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis
    sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic
    cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation
    (Kaneko et al. 1996, DNA Res, full genome).)'
  causal_graph_summary: 'photoautotrophic_cyanobacterial_carbon_fixation: 16 nodes,
    12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000656
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation, anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation, photoautotroph, photoautotrophy
- **Existing evidence:** DOI:10.3390/life10050071: capture solar energy (Review supports cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** photoautotrophic_cyanobacterial_carbon_fixation: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **photoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoautotrophic.yaml`.

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
- **Trait label:** photoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000656
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of light as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** anoxygenic_photoautotrophy, anoxygenic_photoautotrophy_hydrogen_oxidation, anoxygenic_photoautotrophy_iron_oxidation, anoxygenic_photoautotrophy_sulfur_oxidation, photoautotroph, photoautotrophy
- **Existing evidence:** DOI:10.3390/life10050071: capture solar energy (Review supports cyanobacterial photoautotrophic use of solar energy and CO2 fixation.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports the Calvin-Benson cycle as a microbial autotrophic CO2-fixation pathway.) | PMID:8590279: Synechocystis sp. strain PCC6803 (Organism example: Synechocystis sp. PCC 6803 is a model photoautotrophic cyanobacterium that uses oxygenic photosynthesis to drive Calvin-Benson CO2 fixation (Kaneko et al. 1996, DNA Res, full genome).)
- **Existing causal graph summary:** photoautotrophic_cyanobacterial_carbon_fixation: 16 nodes, 12 edges

## Research Objective

Research the microbial trait **photoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoautotrophic.yaml`.

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


# Curation-focused research report: microbial photoautotrophy

## 1. Scope and interpretation

**Target trait:** photoautotrophic  
**Trait identifier:** **METPO:1000656**  
**Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** METPO:1000631

### Operational definition

The trait denotes the physiological capacity to use **light as the primary energy source** while assimilating **CO₂ or another dissolved inorganic-carbon species as the principal carbon source for biomass**. The defining phenotype is therefore the conjunction of phototrophic energy conservation and autotrophic carbon assimilation—not merely the presence of pigments, reaction-center genes, or CO₂-fixation genes.

The trait should encompass at least two mechanistically distinct branches:

1. **Oxygenic photoautotrophy**, represented by cyanobacteria: PSII extracts electrons from water and releases O₂; PSI and the electron-transport chain generate reducing power and ATP; carbon is commonly assimilated through the Calvin–Benson–Bassham (CBB) cycle.
2. **Anoxygenic photoautotrophy**, represented by several bacterial lineages: reduced sulfur compounds, H₂, Fe(II), or other donors supply electrons without oxygen evolution; carbon may be fixed through the CBB cycle, reverse TCA cycle, or another autotrophic pathway. Green sulfur bacteria, for example, use H₂S, oxidize it toward elemental sulfur, and assimilate CO₂ through reverse TCA (kushkevych2024anoxygenicphotosynthesiswith pages 1-2).

### Boundary cases

- **Photoheterotrophy:** light supplies energy, but organic carbon is the principal carbon source. This is not photoautotrophy. Many cyanobacteria and purple bacteria can switch between trophic modes, so the trait should be attached to a demonstrated capacity under specified conditions rather than treated as an invariant property of every culture (mantovani2023rolesofsecond pages 1-2, lucius2024theprimarycarbon pages 1-2).
- **Mixotrophy:** simultaneous inorganic- and organic-carbon use is not equivalent to strict photoautotrophy. A strain may nevertheless possess photoautotrophic capacity if it also grows with inorganic carbon as the principal or sole carbon source.
- **Chemoautotrophy:** inorganic carbon is fixed, but energy derives from chemical oxidation rather than light; exclude it even where CBB, Rubisco, carbonic anhydrase, or carboxysomes are shared.
- **Phototrophy without demonstrated carbon fixation:** bacteriochlorophyll, chlorosomes, reaction centers, or light-dependent ATP formation alone are insufficient.
- **Anoxygenic photosynthesis versus anoxygenic photoautotrophy:** some anoxygenic phototrophs are primarily photoheterotrophic. The electron donor, light dependence, inorganic-carbon assimilation, and growth phenotype must all be established.
- **Genotype-only calls:** `rbcL`, reaction-center genes, or CCM genes support mechanistic plausibility but do not alone demonstrate the phenotype. Growth in light with isotope incorporation from bicarbonate/CO₂ is stronger evidence.

## 2. Current mechanistic model

### 2.1 Oxygenic cyanobacterial branch

In cyanobacteria, PSII oxidizes water at the oxygen-evolving complex, yielding electrons, protons, and O₂ while reducing plastoquinone. Electrons pass through cytochrome *b*₆*f* and plastocyanin to PSI; PSI reduces ferredoxin, and ferredoxin–NADP⁺ reductase supports NADPH production. Coupled proton translocation drives ATP synthesis. ATP and NADPH then power biosynthesis and CBB carbon fixation (grettenberger2024limitingfactorsin pages 2-4). Cyanobacteria are the only prokaryotes known to perform oxygenic photosynthesis (lucius2024theprimarycarbon pages 1-2).

Rubisco catalyzes addition of CO₂ to ribulose-1,5-bisphosphate (RuBP), producing 3-phosphoglycerate through the first committed CBB-cycle reaction (kurkela2024inorganiccarbonsensing pages 3-3, kupriyanova2023adaptingfromlow pages 1-2). Because cyanobacterial Rubisco has limited CO₂ affinity and competes with O₂, cyanobacteria employ a carbon-concentrating mechanism (CCM). SbtA, BicA, and BCT1 import HCO₃⁻, while specialized NDH-1₃/CupA and NDH-1₄/CupB systems convert CO₂ into cytosolic HCO₃⁻. HCO₃⁻ enters carboxysomes, where carbonic anhydrase regenerates CO₂ near encapsulated Rubisco; the shell restricts CO₂ escape (kurkela2024inorganiccarbonsensing pages 3-3, lucius2024theprimarycarbon pages 1-2).

The CCM is an efficiency module rather than the definition of photoautotrophy. Coordinated carbonic anhydrases and CO₂/HCO₃⁻ uptake systems compensate for Rubisco’s kinetic limitations by elevating CO₂ near its active sites (kupriyanova2023adaptingfromlow pages 1-2). In model cyanobacteria, Ci enrichment can suppress Rubisco oxygenase flux to below 1%; without effective CO₂ concentration, photorespiratory carbon loss can reach approximately 25–30% in susceptible photoautotrophs (lucius2024theprimarycarbon pages 1-2, kupriyanova2023adaptingfromlow pages 1-2).

### 2.2 Regulation

The trait is condition-dependent and tightly regulated.

- **Low inorganic carbon:** RuBP and 2-phosphoglycolate act as co-activators of CmpR, promoting the BCT1 operon; low Ci strongly induces NDH-1₃-associated expression, while NDH-1₄ regulation is less clearly resolved (kurkela2024inorganiccarbonsensing pages 8-8).
- **SbtA–SbtB control:** the PII-like regulator SbtB controls the bicarbonate transporter SbtA according to cellular energy state, light, CO₂ availability, adenyl nucleotides, and cAMP-associated signaling (mantovani2023rolesofsecond pages 1-2).
- **Carboxysomal feedback:** in *Cyanobium* sp. PCC7001, RuBP allosterically activates the α-carboxysome carbonic anhydrase CsoSCA. Phylogenetic and mutational evidence indicates that this mechanism may be restricted to cyanobacterial α-carboxysome carbonic anhydrases, so it must not be generalized to all cyanobacteria or carboxysomes (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2).
- **Dark shutdown:** Cp12 downregulates the CBB cycle in darkness by inhibiting phosphoribulokinase and glyceraldehyde-3-phosphate dehydrogenase, limiting futile carbon-fixation flux when photochemical energy is unavailable (lucius2024theprimarycarbon pages 1-2).

### 2.3 Anoxygenic branches

Green sulfur bacteria use chlorosomes as low-light antennae, commonly oxidize H₂S to elemental sulfur, and assimilate CO₂ through reverse TCA. Their adaptation to dim, sulfide-rich anoxic environments makes light, redox state, and donor availability essential contextual nodes (kushkevych2024anoxygenicphotosynthesiswith pages 1-2).

Photoferrotrophs use Fe(II) as the electron donor for anoxygenic photoautotrophy. A 2024 study further showed that *Allochromatium vinosum* can grow autotrophically with insoluble pyrite as both electron and sulfur source. Pyrite-supported growth was slower than sulfide-supported growth and induced c- and b-type cytochrome genes by as much as approximately 200-fold, consistent with electron scavenging from the mineral. However, the proposed direct coupling of pyrite-derived electrons to carbon fixation remains mechanistically inferred (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24).

Nitric oxide and related reactive nitrogen intermediates are important negative environmental factors. Experiments with four green-sulfur and purple-nonsulfur photoferrotrophs showed that nitrate-reducing Fe(II) oxidizers can outcompete them for Fe(II) and inhibit photoferrotrophy through toxic intermediates, despite genomic potential for NO detoxification (nikeleit2024inhibitionofphototrophic pages 1-2).

## 3. Candidate graph nodes

Identifiers below are conservative candidates. Label-only nodes are preferable wherever the exact ontology class or isoform cannot be verified against the project’s pinned ontology release.

### Trait, taxa, and environments

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| photoautotrophic | **METPO:1000656** | Root trait; quote the identifier verbatim. |
| Cyanobacteria | NCBITaxon:1117 | Oxygenic prokaryotic branch. |
| *Synechocystis* sp. PCC 6803 | NCBITaxon:1148 | Model oxygenic photoautotroph; strain-specific graph context. |
| *Cyanobium* sp. PCC7001 | label only pending strain-ID verification | RuBP–CsoSCA evidence is strain-specific. |
| green sulfur bacteria / Chlorobiaceae | NCBITaxon grounding should be release-verified | H₂S oxidation, chlorosomes, reverse TCA. |
| *Allochromatium vinosum* | NCBITaxon grounding should be strain-verified | Pyrite-supported anoxygenic autotrophic growth. |
| anoxic environment | ENVO term to be selected by habitat | Necessary context for many sulfur- and iron-dependent branches. |
| photic zone | ENVO grounding candidate | Light availability is defining but depth is habitat-specific. |
| ferruginous environment | label or release-verified ENVO term | Context for photoferrotrophy and NO inhibition. |

### Pathways and biological processes

| Candidate node | Suggested grounding | Note |
|---|---|---|
| photosynthesis | GO:0015979 | Broad process; child terms should distinguish oxygenic/anoxygenic implementations where available. |
| photosynthetic electron transport | GO term to be release-verified | Includes PSII→PQ→cytochrome *b*₆*f*→plastocyanin→PSI→ferredoxin. |
| carbon fixation | GO:0015977 | Broad process. |
| Calvin–Benson–Bassham cycle | GO:0019253 | Dominant cyanobacterial and many proteobacterial carbon-fixation module. |
| reverse/reductive TCA cycle | label plus pathway-database identifier after verification | Green sulfur bacterial branch. |
| carbon-concentrating mechanism | label only | Composite module rather than a single conserved pathway. |
| photorespiration | GO:0009853 | Competing consequence of Rubisco oxygenation. |
| anoxygenic photosynthesis | GO term should be release-verified | Do not equate automatically with autotrophy. |
| phototrophic Fe(II) oxidation / photoferrotrophy | label only | Mechanistically and environmentally specific. |
| sulfide oxidation | GO term or MetaCyc pathway after verification | Product and route vary among taxa. |

### Complexes, compartments, proteins, and activities

| Candidate node | Suggested grounding | Note |
|---|---|---|
| photosystem II | GO:0009523 | Water-oxidizing oxygenic reaction-center complex. |
| oxygen-evolving complex | GO:0009654 | PSII-associated water oxidation. |
| photosystem I | GO:0009522 | Light-driven plastocyanin–ferredoxin oxidoreductase. |
| cytochrome *b*₆*f* complex | GO:0009512 | Electron transport/proton translocation. |
| ATP synthase | GO:0045259 or taxon-appropriate child | Produces ATP from proton motive force. |
| ferredoxin–NADP⁺ reductase | EC:1.18.1.2 | Supports NADPH formation. |
| Rubisco | GO:0016984; EC:4.1.1.39 | CO₂ fixation and competing oxygenase activity. |
| phosphoribulokinase | EC:2.7.1.19 | Regenerates RuBP; Cp12 target. |
| NAD(P)-dependent GAPDH | exact EC depends on isoform | Cp12 target; avoid an isoform-independent EC assignment. |
| Cp12 | label or UniProt per strain | Regulatory protein; cyanobacterial context. |
| carboxysome | GO:0031470 | Protein microcompartment containing Rubisco and carbonic anhydrase. |
| carbonic anhydrase | GO:0004089; EC:4.2.1.1 | Direction depends on compartment and physicochemical context. |
| CsoSCA | UniProt per organism | α-carboxysomal CA; RuBP activation is lineage-specific. |
| SbtA | UniProt per strain | High-affinity Na⁺/HCO₃⁻ transporter in many cyanobacteria. |
| SbtB | UniProt per strain | PII-like regulator of SbtA and carbon acclimation. |
| BicA | UniProt per strain | Na⁺-dependent bicarbonate transporter. |
| BCT1/CmpABCD | UniProt entries per strain | ABC-type bicarbonate uptake system. |
| NDH-1₃/CupA and NDH-1₄/CupB | label or strain-specific UniProt complexes | CO₂-uptake modules; nomenclature is easily corrupted typographically. |
| chlorosome | GO:0031471 | Green-sulfur and some other anoxygenic phototroph antenna compartment. |
| c-/b-type cytochromes | protein-family or strain-specific UniProt IDs | Pyrite result is expression evidence, not proof of a unique electron-transfer chain. |
| FccAB and SoxYZ | strain-specific UniProt IDs | Candidate sulfur-oxidation/electron-transfer modules in pyrite-grown *A. vinosum*. |

### Chemicals and physical factors

| Candidate node | Suggested grounding |
|---|---|
| light / photon | CHEBI:30212 for photon; wavelength/intensity as experimental attributes |
| carbon dioxide | CHEBI:16526 |
| hydrogencarbonate/bicarbonate | CHEBI:17544 |
| water | CHEBI:15377 |
| dioxygen | CHEBI:15379 |
| ATP | CHEBI:15422 |
| NADPH | CHEBI:16474 |
| ribulose 1,5-bisphosphate | CHEBI:16710 |
| 3-phosphoglycerate | CHEBI term should be release-verified |
| hydrogen sulfide / sulfide | Distinguish protonation states; use the appropriate CHEBI class for assay pH |
| elemental sulfur | CHEBI term should be release-verified |
| dihydrogen | CHEBI:18276 |
| iron(2+) | CHEBI:29033 |
| pyrite (FeS₂) | mineral ontology or label-only node |
| nitric oxide | CHEBI:16480 |
| 2-phosphoglycolate | CHEBI term should be release-verified |
| cAMP, ATP/ADP/AMP | CHEBI terms; regulatory interpretation is state-dependent |
| CO₂ concentration, pH, salinity, temperature, light intensity/wavelength, UV, nutrient availability | Experimental/environmental-factor nodes rather than molecular actors |

## 4. Candidate causal edges

The following compact core set is recommended as the starting point for review:

| subject | predicate | object | scope/confidence | DOI |
|---|---|---|---|---|
| light | activates | photosystem II (PSII) | broad oxygenic cyanobacterial photoautotrophy; high (grettenberger2024limitingfactorsin pages 2-4) | 10.1111/1751-7915.14519 |
| photosystem II (PSII) | oxidizes | water, producing O2, electrons, and protons | broad oxygenic cyanobacterial photoautotrophy; high (grettenberger2024limitingfactorsin pages 2-4, lucius2024theprimarycarbon pages 1-2) | 10.1111/1751-7915.14519 |
| photosynthetic electron transport chain | supports production of | ATP and NADPH | broad oxygenic cyanobacterial photoautotrophy; high (grettenberger2024limitingfactorsin pages 2-4) | 10.1111/1751-7915.14519 |
| RuBisCO | carboxylates | ribulose-1,5-bisphosphate (RuBP) | broad cyanobacterial CCM/CBB; high (kurkela2024inorganiccarbonsensing pages 3-3, kupriyanova2023adaptingfromlow pages 1-2) | 10.1111/ppl.14140 |
| SbtA/BicA/BCT1 | transport | HCO3- | cyanobacterial CCM; high, taxon-scoped (kurkela2024inorganiccarbonsensing pages 3-3, lucius2024theprimarycarbon pages 1-2) | 10.1111/ppl.14140 |
| NDH-13/NDH-14 | convert | CO2 to HCO3- | cyanobacterial CCM; high, taxon-scoped (kurkela2024inorganiccarbonsensing pages 3-3, lucius2024theprimarycarbon pages 1-2) | 10.1111/ppl.14140 |
| carboxysomal carbonic anhydrase | converts | HCO3- to CO2 in carboxysome | cyanobacterial CCM; high, taxon-scoped (lucius2024theprimarycarbon pages 1-2, pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2, kupriyanova2023adaptingfromlow pages 1-2) | 10.3389/fpls.2024.1417680 |
| carboxysome | elevates CO2 near | RuBisCO | cyanobacterial CCM; high, taxon-scoped (lucius2024theprimarycarbon pages 1-2, pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) | 10.3389/fpls.2024.1417680 |
| RuBP | allosterically activates | Cyanobium sp. PCC7001 CsoSCA | alpha-cyanobacterial carboxysome CA only; high, taxon-specific (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) | 10.1126/sciadv.adk7283 |
| Cp12 | inhibits in darkness | phosphoribulokinase and glyceraldehyde-3-phosphate dehydrogenase | cyanobacteria; high, regulatory/taxon-scoped (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680 |
| H2S | supports | green sulfur bacterial anoxygenic photoautotrophy via reverse TCA carbon fixation | green sulfur bacteria; high, taxon-specific (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 |
| Fe(II) | supports | anoxygenic photoferrotrophy | anoxygenic photoautotrophs; high, taxon-scoped (nikeleit2024inhibitionofphototrophic pages 1-2, conners2024thephototrophicpurple pages 1-2) | 10.1038/s41561-024-01560-9 |
| nitric oxide | inhibits | photoferrotrophy | photoferrotrophs in ferruginous settings; high, taxon/environment-specific (nikeleit2024inhibitionofphototrophic pages 1-2) | 10.1038/s41561-024-01560-9 |


*Table: This compact curation table lists the strongest evidence-backed mechanistic edges for microbial photoautotrophy across oxygenic and anoxygenic systems. It is useful as a starting set of candidate TraitMech triples, while flagging cyanobacteria- and taxon-specific relations.*

Additional curation detail and source snippets follow.

| Subject–predicate–object | Reference | Supporting snippet | Curation notes |
|---|---|---|---|
| light — activates/drives → PSII-dependent water oxidation | 10.1111/1751-7915.14519, Aug 2024 | “PSII oxidizes water at the oxygen-evolving complex…to produce electrons, protons, and O₂” | **Strong**, oxygenic branch. “Activates” may be represented more precisely as `provides_energy_for`. (grettenberger2024limitingfactorsin pages 2-4) |
| PSII — reduces → plastoquinone | 10.1111/1751-7915.14519, Aug 2024 | PSII water oxidation is coupled to reduction of plastoquinone to plastoquinol. | **Strong**, oxygenic branch. (grettenberger2024limitingfactorsin pages 2-4) |
| PSI — reduces → ferredoxin | 10.1111/1751-7915.14519, Aug 2024 | PSI catalyzes light-dependent plastocyanin oxidation and ferredoxin reduction. | **Strong**. (grettenberger2024limitingfactorsin pages 2-4) |
| ferredoxin/FNR electron transfer — enables → NADPH production | 10.1111/1751-7915.14519, Aug 2024 | “Ferredoxin transfers electrons via FNR to reduce NADP+ to NADPH.” | **Strong**. (grettenberger2024limitingfactorsin pages 2-4) |
| photosynthetic electron transport — supplies → ATP and NADPH for carbon fixation | 10.1111/1751-7915.14519, Aug 2024 | ATP and NADPH convert light energy into chemical energy and support biosynthesis including Rubisco-dependent fixation. | **Strong**, but split ATP and NADPH into separate edges if graph predicates require directness. (grettenberger2024limitingfactorsin pages 2-4) |
| Rubisco — carboxylates → RuBP | 10.1111/ppl.14140, Jan 2024 | Rubisco adds CO₂ to RuBP to form 3-PGA in the first carbon-fixation reaction. | **Strong**; represent CO₂ as a second input if the schema supports reactions. (kurkela2024inorganiccarbonsensing pages 3-3) |
| SbtA/BicA/BCT1 — transports → HCO₃⁻ into the cell | 10.1111/ppl.14140, Jan 2024 | The CCM includes “bicarbonate transporters SbtA, BicA and BCT1.” | **Strong but cyanobacteria-specific**; transporter repertoires vary by strain. (kurkela2024inorganiccarbonsensing pages 3-3) |
| NDH-1₃/CupA and NDH-1₄/CupB — convert → CO₂ to HCO₃⁻ | 10.1111/ppl.14140, Jan 2024 | Specialized NDH complexes “convert CO₂ to HCO₃⁻ in the cytoplasm.” | **Strong**, cyanobacterial module; retain complex identity and location. (kurkela2024inorganiccarbonsensing pages 3-3) |
| carboxysomal carbonic anhydrase — converts → HCO₃⁻ to CO₂ | 10.3389/fpls.2024.1417680, 5 Jul 2024 | “bicarbonate is converted back to CO₂ by CA.” | **Strong** in carboxysome context; CA catalysis is reversible, so direction requires compartmental context. (lucius2024theprimarycarbon pages 1-2) |
| carboxysome shell — restricts loss of → CO₂ | 10.3389/fpls.2024.1417680, 5 Jul 2024 | “the carboxysome shell prevents the loss of CO₂.” | **Strong functional model**, although shell permeability is biophysical rather than absolute. (lucius2024theprimarycarbon pages 1-2) |
| carboxysome — increases local concentration of → CO₂ near Rubisco | 10.1126/sciadv.adk7283, 10 May 2024 | Carboxysomes house CA and Rubisco; CA elevates luminal CO₂ and promotes Rubisco-catalyzed fixation. | **Strong**, cyanobacteria and some autotrophic bacteria, but not universal to all photoautotrophs. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) |
| RuBP — allosterically activates → CsoSCA | 10.1126/sciadv.adk7283, 10 May 2024 | “Cyanobium CsoSCA is allosterically activated by…ribulose-1,5-bisphosphate.” | **Strong but explicitly taxon/lineage-specific**; do not generalize to β-carboxysomes or chemoautotrophic CsoSCA. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2) |
| SbtB — regulates → SbtA | 10.1093/femsml/uqad008, 23 Feb 2023 | SbtA “is regulated via SbtB depending on the energy state…light conditions, and different CO₂ availability.” | **Strong review synthesis**; the sign of regulation depends on ligand and state, so use `regulates`, not constitutive inhibition. (mantovani2023rolesofsecond pages 1-2) |
| low Ci via RuBP/2-phosphoglycolate and CmpR — activates expression of → BCT1 operon | 10.1111/ppl.14140, Jan 2024 | RuBP and 2-PG co-activate CmpR, which activates the BCT1 operon under low CO₂. | **Strong regulatory model**, cyanobacterial and strain-dependent. (kurkela2024inorganiccarbonsensing pages 8-8) |
| low Ci — induces → NDH-1₃ expression | 10.1111/ppl.14140, Jan 2024 | NDH-1₃ expression is “highly activated in low inorganic carbon.” | **Strong**; do not assign the same response to NDH-1₄, whose Ci dependence is less clear. (kurkela2024inorganiccarbonsensing pages 8-8) |
| darkness/Cp12 — inhibits → phosphoribulokinase and GAPDH | 10.3389/fpls.2024.1417680, 5 Jul 2024 | “Cp12 protein downregulates the CBB cycle in darkness by inhibiting phosphoribulokinase and glyceraldehyde 3-phosphate dehydrogenase.” | **Strong**, cyanobacterial regulation. Model darkness as context and Cp12 as direct regulator. (lucius2024theprimarycarbon pages 1-2) |
| H₂S — donates electrons for → green-sulfur-bacterial anoxygenic photosynthesis | 10.3389/fmicb.2024.1417714, Jul 2024 | H₂S is the main electron donor; GSB oxidize it to elemental sulfur. | **Strong but taxon-specific**. Speciation and oxidation products depend on organism and conditions. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| green-sulfur-bacterial phototrophy — powers → reverse-TCA CO₂ assimilation | 10.3389/fmicb.2024.1417714, Jul 2024 | “The carbon source of GSB is carbon dioxide, which is assimilated through the reverse tricarboxylic acid cycle.” | **Strong review support**, family-level generalization should still allow exceptions. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) |
| pyrite — supports → autotrophic growth of *A. vinosum* | 10.1128/aem.00863-24, Jul 2024 | Pyrite served as “electron and sulfur source”; cultures grew robustly but more slowly than sulfide controls. | **Strong primary evidence, single species/assay**. Light dependence should be explicit in the experimental context. (alarcon2024evidenceforautotrophic pages 1-2) |
| pyrite exposure — increases expression of → c-/b-type cytochromes | 10.1128/aem.00863-24, Jul 2024 | “Up to ~200-fold upregulation” of cytochrome genes occurred in pyrite cultures. | **Strong transcriptomic association**, but not proof that each cytochrome transfers electrons from pyrite. (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24) |
| nitrate-reducing Fe(II) oxidizers — compete for → Fe(II) | 10.1038/s41561-024-01560-9, 4 Oct 2024 | Incubations showed nitrate-reducing Fe(II) oxidizers “outcompete photoferrotrophs for dissolved Fe(II).” | **Strong environmental interaction**, not a cell-intrinsic trait mechanism. (nikeleit2024inhibitionofphototrophic pages 1-2) |
| nitric oxide/reactive nitrogen intermediates — inhibit → photoferrotrophy | 10.1038/s41561-024-01560-9, 4 Oct 2024 | Four photoferrotrophs were susceptible despite genomic NO-detoxification capability. | **Strong inhibitor edge**, demonstrated across four strains but still assay/environment-specific. (nikeleit2024inhibitionofphototrophic pages 1-2) |

## 5. Applications, implementations, and recent quantitative findings

### Carbon capture and cell factories

Cyanobacterial CCMs and carboxysomes are targets for engineered CO₂ capture, carbon utilization, and biomanufacturing. Current expert analysis emphasizes that cyanobacteria can combine sunlight and CO₂ utilization with redirected carbon flux, but industrial performance remains constrained by light delivery, CO₂ supply, Rubisco/carboxysome capacity, nutrient status, temperature, salinity, UV exposure, and photoinhibition (lucius2024theprimarycarbon pages 1-2, grettenberger2024limitingfactorsin pages 2-4). These constraints should be modeled as modifiers of trait expression rather than universal causal requirements.

Ecologically, picocyanobacterial *Synechococcus* and *Prochlorococcus* are estimated to account for at least **25% of marine primary production**, illustrating the global importance of the oxygenic branch (lucius2024theprimarycarbon pages 1-2). The bacterial CCM itself is described as contributing to roughly half of global photosynthetic carbon fixation, although this is a synthesis-level estimate rather than a directly measured trait frequency (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2).

### Sulfide removal and environmental management

Green sulfur bacteria can couple light-dependent H₂S oxidation to CO₂ assimilation, producing elemental sulfur and offering a potential biological route for detoxifying sulfide-rich anoxic waters or waste streams. The 2024 review presents this as a promising substitute or supplement for physicochemical H₂S-removal processes, but implementation maturity and performance depend strongly on illumination and reactor redox structure (kushkevych2024anoxygenicphotosynthesiswith pages 1-2).

### Bioplastics and microbial electrosynthesis

Purple nonsulfur *Rhodomicrobium* species accumulated PHA under photoheterotrophic, photohydrogenotrophic, photoferrotrophic, and photoelectrotrophic conditions. The highest reported PHA titre was **44.08 mg L⁻¹**, equivalent to **43.61% of cell dry weight**, under photoheterotrophic growth on butyrate with N₂; photoelectrotrophy yielded as little as **0.04 mg L⁻¹** or **0.16% dry weight**. Photohydrogenotrophic cultures with NH₄Cl reached electron yields of **58.89%** (conners2024thephototrophicpurple pages 1-2). These results demonstrate application potential but must not be used as direct evidence for photoautotrophy in conditions containing organic carbon.

### Mineral-driven carbon fixation and early-Earth models

The pyrite-supported growth of *A. vinosum* expands the recognized donor range of anoxygenic autotrophy and suggests applications in extracellular electron transfer and artificial photosynthesis. Nevertheless, the approximately 200-fold cytochrome induction identifies candidates rather than a fully resolved electron-transfer chain (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24). Photoferrotrophic models of ancient banded iron formation must also incorporate competition and NO toxicity, not simply photon and Fe(II) availability (nikeleit2024inhibitionofphototrophic pages 1-2).

## 6. Expert synthesis for graph design

A single linear “photoautotrophy pathway” would be biologically misleading. The recommended graph architecture is a **trait root with alternative mechanistic subgraphs**:

1. **Shared trait logic:** light availability → photochemical energy conservation; inorganic carbon availability → carbon fixation; both → photoautotrophic growth.
2. **Oxygenic cyanobacterial module:** water → PSII → electron transport → ATP/NADPH → CBB; CCM → elevated carboxysomal CO₂ → Rubisco carboxylation.
3. **Anoxygenic sulfur module:** H₂S/reduced sulfur → reaction center/electron transport → ATP/reducing equivalents; reverse TCA or CBB → biomass.
4. **Photoferrotrophic module:** Fe(II) or mineral-associated electrons → anoxygenic photochemistry → inorganic-carbon fixation, with NO and donor competition as negative modifiers.
5. **Regulatory context:** light/dark, Ci, energy charge, pH, salinity, temperature, nutrients, and redox state modify flux or expression rather than defining the trait independently.

This modular approach avoids incorrectly asserting that PSII, oxygen evolution, CBB, Rubisco, carboxysomes, or H₂S oxidation is universal across every photoautotrophic microbe.

## 7. Claims not yet suitable for unqualified TraitMech curation

1. **Do not treat the supplied synonyms as exact equivalents of the root class.** `anoxygenic_photoautotrophy_hydrogen_oxidation`, `_iron_oxidation`, and `_sulfur_oxidation` are narrower mechanistic subclasses, not synonyms of all photoautotrophy.
2. **Do not infer phenotype from genes alone.** Reaction-center, `rbcL`, or CCM genes require physiological confirmation.
3. **Do not generalize RuBP activation of CsoSCA.** Current evidence supports *Cyanobium* PCC7001 and sequence conservation in cyanobacterial α-carboxysome CAs, not all carbonic anhydrases (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2).
4. **Do not assert NDH-1₄ induction by low Ci.** Its response is less clear than that of NDH-1₃ (kurkela2024inorganiccarbonsensing pages 8-8).
5. **Do not curate every pyrite-induced cytochrome as a direct pyrite reductant/oxidant.** Expression and proposed electron scavenging do not establish direct biochemical transfer for each protein (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24).
6. **Do not equate PHA production under photoheterotrophy with photoautotrophic product formation.** The carbon source differs (conners2024thephototrophicpurple pages 1-2).
7. **Do not model carbonic anhydrase as intrinsically unidirectional.** HCO₃⁻→CO₂ is justified only in carboxysome/CCM context.
8. **Do not make oxygen production universal.** It is restricted to oxygenic photoautotrophy.
9. **Do not make CBB universal.** Green sulfur bacteria commonly use reverse TCA, and other lineages may employ additional fixation pathways (kushkevych2024anoxygenicphotosynthesiswith pages 1-2).
10. **Do not curate application claims as core phenotype mechanisms.** Carbon capture, sulfide detoxification, PHA synthesis, and mineral transformations are downstream uses or ecological consequences.

## 8. DOI-first bibliography

1. **Pulsford SB et al.** “Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the Rubisco substrate RuBP.” *Science Advances* 10, published **10 May 2024**. DOI: [10.1126/sciadv.adk7283](https://doi.org/10.1126/sciadv.adk7283). (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2)
2. **Kurkela J, Tyystjärvi T.** “Inorganic carbon sensing and signalling in cyanobacteria.” *Physiologia Plantarum* 176, published **January 2024**. DOI: [10.1111/ppl.14140](https://doi.org/10.1111/ppl.14140). (kurkela2024inorganiccarbonsensing pages 3-3, kurkela2024inorganiccarbonsensing pages 8-8)
3. **Lucius S, Hagemann M.** “The primary carbon metabolism in cyanobacteria and its regulation.” *Frontiers in Plant Science* 15, published **5 July 2024**. DOI: [10.3389/fpls.2024.1417680](https://doi.org/10.3389/fpls.2024.1417680). (lucius2024theprimarycarbon pages 1-2)
4. **Grettenberger CL, Abou-Shanab R, Hamilton TL.** “Limiting factors in the operation of photosystems I and II in cyanobacteria.” *Microbial Biotechnology* 17, published **August 2024**. DOI: [10.1111/1751-7915.14519](https://doi.org/10.1111/1751-7915.14519). (grettenberger2024limitingfactorsin pages 2-4)
5. **Kushkevych I et al.** “Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.” *Frontiers in Microbiology* 15, published **July 2024**. DOI: [10.3389/fmicb.2024.1417714](https://doi.org/10.3389/fmicb.2024.1417714). (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
6. **Alarcon HV et al.** “Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source.” *Applied and Environmental Microbiology* 90, published **July 2024**. DOI: [10.1128/aem.00863-24](https://doi.org/10.1128/aem.00863-24). (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 22-24)
7. **Nikeleit V et al.** “Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments.” *Nature Geoscience* 17:1169–1174, published online **4 October 2024**. DOI: [10.1038/s41561-024-01560-9](https://doi.org/10.1038/s41561-024-01560-9). (nikeleit2024inhibitionofphototrophic pages 1-2)
8. **Conners EM et al.** “The phototrophic purple non-sulfur bacteria *Rhodomicrobium* spp. are novel chassis for bioplastic production.” *Microbial Biotechnology* 17, accepted **31 July 2024**. DOI: [10.1111/1751-7915.14552](https://doi.org/10.1111/1751-7915.14552). (conners2024thephototrophicpurple pages 1-2)
9. **Mantovani O et al.** “Roles of second messengers in the regulation of cyanobacterial physiology: the carbon-concentrating mechanism and beyond.” *microLife* 4, published **23 February 2023**. DOI: [10.1093/femsml/uqad008](https://doi.org/10.1093/femsml/uqad008). (mantovani2023rolesofsecond pages 1-2)
10. **Kupriyanova EV, Pronina NA, Los DA.** “Adapting from Low to High: An Update to CO₂-Concentrating Mechanisms of Cyanobacteria and Microalgae.” *Plants* 12:1569, published **6 April 2023**. DOI: [10.3390/plants12071569](https://doi.org/10.3390/plants12071569). (kupriyanova2023adaptingfromlow pages 1-2)

### Recommended first-pass YAML emphasis

For `data/traits/physiology/photoautotrophic.yaml`, the safest first expansion is the oxygenic cyanobacterial module—light, PSII/water oxidation, PSI/electron transport, ATP/NADPH, CBB/Rubisco, bicarbonate uptake, carboxysome/CA, and CO₂ fixation—followed by separately scoped anoxygenic sulfur and Fe(II) modules. Taxon restrictions and experimental context should be encoded on every non-universal edge.

References

1. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 30 citations and is from a peer-reviewed journal.

2. (mantovani2023rolesofsecond pages 1-2): Oliver Mantovani, Michael Haffner, Khaled A Selim, Martin Hagemann, and Karl Forchhammer. Roles of second messengers in the regulation of cyanobacterial physiology: the carbon-concentrating mechanism and beyond. microLife, Feb 2023. URL: https://doi.org/10.1093/femsml/uqad008, doi:10.1093/femsml/uqad008. This article has 22 citations and is from a peer-reviewed journal.

3. (lucius2024theprimarycarbon pages 1-2): Stefan Lucius and Martin Hagemann. The primary carbon metabolism in cyanobacteria and its regulation. Frontiers in Plant Science, Jul 2024. URL: https://doi.org/10.3389/fpls.2024.1417680, doi:10.3389/fpls.2024.1417680. This article has 97 citations.

4. (grettenberger2024limitingfactorsin pages 2-4): Christen L. Grettenberger, Reda Abou‐Shanab, and Trinity L. Hamilton. Limiting factors in the operation of photosystems i and ii in cyanobacteria. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14519, doi:10.1111/1751-7915.14519. This article has 17 citations and is from a peer-reviewed journal.

5. (kurkela2024inorganiccarbonsensing pages 3-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

6. (kupriyanova2023adaptingfromlow pages 1-2): Elena V. Kupriyanova, Natalia A. Pronina, and Dmitry A. Los. Adapting from low to high: an update to co2-concentrating mechanisms of cyanobacteria and microalgae. Plants, 12:1569, Apr 2023. URL: https://doi.org/10.3390/plants12071569, doi:10.3390/plants12071569. This article has 110 citations.

7. (kurkela2024inorganiccarbonsensing pages 8-8): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

8. (pulsford2024cyanobacterialαcarboxysomecarbonic pages 1-2): Sacha B. Pulsford, Megan A. Outram, Britta Förster, Timothy Rhodes, Simon J. Williams, Murray R. Badger, G. Dean Price, Colin J. Jackson, and Benedict M. Long. Cyanobacterial α-carboxysome carbonic anhydrase is allosterically regulated by the rubisco substrate rubp. Science Advances, May 2024. URL: https://doi.org/10.1126/sciadv.adk7283, doi:10.1126/sciadv.adk7283. This article has 27 citations and is from a highest quality peer-reviewed journal.

9. (alarcon2024evidenceforautotrophic pages 1-2): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 6 citations and is from a peer-reviewed journal.

10. (alarcon2024evidenceforautotrophic pages 22-24): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 6 citations and is from a peer-reviewed journal.

11. (nikeleit2024inhibitionofphototrophic pages 1-2): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 3 citations and is from a highest quality peer-reviewed journal.

12. (conners2024thephototrophicpurple pages 1-2): Eric M. Conners, Karthikeyan Rengasamy, Tahina Ranaivoarisoa, and Arpita Bose. The phototrophic purple non‐sulfur bacteria rhodomicrobium spp. are novel chassis for bioplastic production. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14552, doi:10.1111/1751-7915.14552. This article has 14 citations and is from a peer-reviewed journal.