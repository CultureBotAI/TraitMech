---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:40:34.880024'
end_time: '2026-08-04T06:47:47.857556'
duration_seconds: 432.98
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: oxygenic photosynthesis
  trait_identifier: traitmech:000034
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: oxygenic_photosynthesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phototrophic metabolism that uses light energy to fix CO2, oxidizing
    water as the electron donor and releasing molecular oxygen. It uses two linked
    photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant
    chloroplasts).
  parent_traits: traitmech:000038
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic
    photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis
    (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.)
    | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic
    Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a
    distinct, cyanobacterial innovation.)'
  causal_graph_summary: 'oxygenic_photosynthesis_water_splitting: 13 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oxygenic photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000034
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy to fix CO2, oxidizing water as the electron donor and releasing molecular oxygen. It uses two linked photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant chloroplasts).
- **Parent traits:** traitmech:000038
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a distinct, cyanobacterial innovation.)
- **Existing causal graph summary:** oxygenic_photosynthesis_water_splitting: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **oxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxygenic_photosynthesis.yaml`.

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
- **Trait label:** oxygenic photosynthesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000034
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phototrophic metabolism that uses light energy to fix CO2, oxidizing water as the electron donor and releasing molecular oxygen. It uses two linked photosystems and chlorophyll, and is characteristic of cyanobacteria (and plant chloroplasts).
- **Parent traits:** traitmech:000038
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.tim.2006.09.001:  (Bryant & Frigaard, "Prokaryotic photosynthesis and phototrophy illuminated", contrasts oxygenic photosynthesis (water-splitting, O2-evolving) in cyanobacteria with anoxygenic phototrophy.) | DOI:10.1146/annurev-earth-060313-054810:  (Fischer et al., "Evolution of Oxygenic Photosynthesis", supports water-oxidizing, oxygen-evolving photosynthesis as a distinct, cyanobacterial innovation.)
- **Existing causal graph summary:** oxygenic_photosynthesis_water_splitting: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **oxygenic photosynthesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/oxygenic_photosynthesis.yaml`.

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


# TraitMech curation report: oxygenic photosynthesis

## Record and scope

- **Trait:** oxygenic photosynthesis
- **Identifier:** `traitmech:000034`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000038`

### Recommended scope definition

This trait represents the cellular capacity for **light-driven linear electron transfer from water through PSII, plastoquinone, cytochrome b6f, and PSI to terminal reductants**, with water oxidation releasing molecular oxygen and the resulting proton motive force and reducing equivalents supporting ATP synthesis and CO2 fixation. In cyanobacteria, the machinery is embedded in cytoplasmic thylakoid membranes; in oxygenic microbial eukaryotes it is in chloroplast thylakoids. PSII and PSI convert absorbed light into charge separation, and the linear “Z-scheme” transfers electrons from H2O toward NADP+ reduction. (shevela2023solarenergyconversion pages 1-2)

A practical positive phenotype is therefore demonstrable **light-dependent O2 evolution from water**, ideally coupled to whole-chain electron transport, ATP/NADPH formation, and photoautotrophic CO2 assimilation. PSII alone is the water-oxidizing/O2-evolving module, whereas complete trait expression normally requires both photosystems and the intervening electron-transfer chain. (shevela2023solarenergyconversion pages 1-2, tian2024photosystemia pages 1-2)

### Boundaries

1. **Exclude anoxygenic phototrophy.** It uses electron donors such as H2S rather than water and does not evolve O2. Possession of bacteriochlorophyll, a single reaction-center type, chlorosomes, or light-dependent ATP production alone is insufficient.
2. **Do not equate oxygen evolution with carbon fixation.** Isolated PSII preparations and metabolically supplemented mutants can evolve O2 without supporting photoautotrophic growth. A 2024 *Synechocystis* experiment found that a strain with approximately 8% of wild-type PSI could retain oxygen-evolution capacity yet fail to grow photoautotrophically. (moore2024functionalconsequencesof pages 13-15, moore2024functionalconsequencesof pages 12-13)
3. **Cyclic electron flow around PSI is auxiliary, not itself oxygenic photosynthesis.** It increases ATP-generating proton translocation but neither oxidizes water nor directly produces NADPH. Reduced PSI abundance slowed cyclic electron transport in *Synechocystis*. (moore2024functionalconsequencesof pages 1-2, moore2024functionalconsequencesof pages 7-9)
4. **Respiratory or chlororespiratory electron flow through a shared plastoquinone pool is not sufficient.** In cyanobacteria, photosynthetic and respiratory components can share thylakoid membranes; evidence should connect the phenotype specifically to light-driven PSII water oxidation.
5. **Far-red acclimation and alternative chlorophyll composition remain within scope** if the organism still uses linked PSII/PSI chemistry to oxidize water. PSI pigment and antenna composition is environmentally plastic even though its heterodimeric core is conserved. (tian2024photosystemia pages 1-2)
6. The trait is characteristic of **Cyanobacteria** and of chloroplast-containing microbial eukaryotes. For a microbial trait graph, cyanobacterial mechanisms should be the default; plant- or alga-specific assembly proteins should be separately qualified.

## Candidate nodes

### Trait, pathway, and process nodes

- oxygenic photosynthesis — `traitmech:000034`
- photosynthetic light reactions — label-only candidate
- linear photosynthetic electron transport / Z-scheme — label-only candidate
- photosynthetic water oxidation — label-only candidate
- oxygen evolution — label-only candidate
- photosynthetic electron transport chain — `GO:0009767` candidate
- proton-motive-force-driven ATP synthesis — `GO:0015986` candidate
- Calvin–Benson–Bassham cycle — `GO:0019253`
- carbon fixation — `GO:0015977` candidate
- photoautotrophic growth — label-only candidate
- cyclic electron flow around PSI — label-only auxiliary process
- PSII repair cycle — label-only auxiliary process

### Complexes and structural modules

- photosystem II — `GO:0009523`
- oxygen-evolving complex — `GO:0009654`
- Mn4CaO5 catalytic cluster — label-only; do not assign a chemical CURIE without validation
- photosystem I — `GO:0009522`
- cytochrome b6f complex — `GO:0009512`
- chlorophyll-containing antenna / phycobilisome — label-only pending taxon-specific graph design
- chloroplast or cyanobacterial F-type ATP synthase — label-only complex; `GO:0015986` describes the coupled process rather than a taxon-specific complex
- Rubisco — label-only complex; ground individual forms only after taxon resolution

### Genes and proteins

- `psbA` / D1 protein and `psbD` / D2 protein: PSII reaction-center core
- CP43 (`psbC`) and CP47 (`psbB`): inner antenna/core subunits
- PsbO, PsbU, PsbV/cytochrome c550: cyanobacterial extrinsic OEC-stabilizing proteins
- TyrZ/D1-Tyr161: redox-active tyrosine between P680 chemistry and the OEC
- `psaA` and `psaB`: PSI reaction-center heterodimer
- cytochrome f/PetA and other cytochrome b6f subunits
- plastocyanin/PetE and cytochrome c6/PetJ: alternative soluble electron carriers
- ferredoxin/PetF
- ferredoxin–NADP+ reductase/PetH
- ATP synthase subunits (`atp` genes)
- Rubisco large and small subunits (`rbcL`, `rbcS`)

D1 and D2 form the PSII reaction center containing the primary redox cofactors. Most active electron-transfer cofactors are on the D1 branch; cyanobacterial PsbO/PsbU/PsbV and corresponding algal/plant extrinsic proteins stabilize the OEC and optimize water oxidation. (shevela2023solarenergyconversion pages 4-5)

### Chemicals and energetic states

- water — `CHEBI:15377`
- molecular oxygen — `CHEBI:15379`
- proton — `CHEBI:15378`
- electron — `CHEBI:10545`
- carbon dioxide — `CHEBI:16526`
- ATP — `CHEBI:15422`
- NADPH — `CHEBI:16474`
- plastoquinone — `CHEBI:26214`
- plastoquinol — `CHEBI:60144`
- chlorophyll a — label or validated ChEBI mapping to be added during implementation
- pheophytin, QA and QB — label-only until chemical/state representation is standardized
- P700 and P680 — functional pigment-state labels, not single proteins
- manganese, calcium, bicarbonate, iron, copper, phosphate, and fixed nitrogen — candidate nutrient/cofactor nodes; causal edges need trait-specific evidence
- proton motive force — `GO:0015990` process candidate, comprising ΔpH and ΔΨ

### Localization and taxon nodes

- thylakoid membrane — `GO:0042651`
- thylakoid lumen — `GO:0031977` candidate
- chloroplast — `GO:0009507`, applicable only to microbial eukaryotes
- Cyanobacteria — `NCBITaxon:1117`
- *Synechocystis* sp. PCC 6803 — use the current NCBI Taxonomy record after checking strain-level identifier

### Environmental and experimental nodes

- photosynthetically active radiation/light intensity
- high light, low light, far-red light
- CO2 availability, inorganic carbon limitation
- iron limitation, copper availability, salinity, temperature
- DCMU/diuron: PSII QB-site electron-transfer inhibitor; label-only here because no inhibitor-specific primary evidence was retrieved
- P700 redox kinetics, pulse-amplitude-modulated chlorophyll fluorescence, Fv/Fm, oxygen electrode measurements, 77-K fluorescence, growth without organic carbon

## Candidate causal edges

The following table is a conservative core graph. “High-confidence” means broadly curatable for oxygenic phototrophs; experimental thresholds and stress responses require taxon or assay qualifiers.

| Subject | Predicate | Object | Grounding | Evidence snippet | DOI/date | Curation note |
|---|---|---|---|---|---|---|
| light | drives | PSII charge separation | light = CHEBI:30212; PSII = GO:0009523; charge separation = label-only | “Light energy is trapped by photoactive pigments in Reaction Centers (RCs) of PSII and PSI, resulting in charge separation” (shevela2023solarenergyconversion pages 1-2) | 10.1007/s11120-022-00991-y; 2023-02 | High-confidence general mechanism. |
| Photosystem II / oxygen-evolving complex | enables | photosynthetic water oxidation | PSII = GO:0009523; oxygen-evolving complex = GO:0009654; water oxidation = label-only | “Photosynthetic water oxidation by Photosystem II (PSII)” and “PSII is identified as the critical component for photosynthetic water oxidation” (shevela2023solarenergyconversion pages 1-2) | 10.1007/s11120-022-00991-y; 2023-02 | High-confidence core defining edge. |
| Mn4CaO5 oxygen-evolving complex | oxidizes | water | Mn4CaO5 oxygen-evolving complex = label-only; water = CHEBI:15377 | “TyrZ (YZ) functions as an electron carrier between P680 and the Mn4CaO5 oxygen-evolving complex (OEC)” and the OEC is the site of water oxidation (shevela2023solarenergyconversion pages 9-10, shevela2023solarenergyconversion pages 1-2) | 10.1007/s11120-022-00991-y; 2023-02 | Mechanistically central; complex composition supported, exact ontology for cluster left label-only. |
| water oxidation | produces | O2 + protons + electrons | O2 = CHEBI:15379; proton = CHEBI:15378; electron = CHEBI:10545 | “water and carbon dioxide into organic matter while releasing molecular oxygen” and PQ reduction generates “lumenal protons” in the linear chain from water (shevela2023solarenergyconversion pages 1-2) | 10.1007/s11120-022-00991-y; 2023-02 | Curatable, though exact stoichiometry not quoted here. |
| Photosystem II | reduces | plastoquinone to plastoquinol | PSII = GO:0009523; plastoquinone = CHEBI:26214; plastoquinol = CHEBI:60144 | “PSII facilitates the light-induced reactions of water-splitting and plastoquinone reduction” and “QB site accepts two electrons sequentially and two protons to form plastoquinol (PQH2)” (tian2024photosystemia pages 1-2, shevela2023solarenergyconversion pages 9-10) | 10.3390/ijms25168767; 2024-08; 10.1007/s11120-022-00991-y; 2023-02 | High-confidence; QB-mediated step. |
| plastoquinol (PQH2) | donates electrons to | cytochrome b6f complex | plastoquinol = CHEBI:60144; cytochrome b6f complex = GO:0009512 | “PQH2 diffuses in the membrane to reduce the cytochrome b6f complex” (milrad2024regulationofmicroalgal pages 1-3) | 10.3390/plants13152103; 2024-07 | High-confidence, broadly applicable in oxygenic phototrophs. |
| cytochrome b6f complex | increases | proton motive force across thylakoid membrane | cytochrome b6f complex = GO:0009512; proton motive force = GO:0015990; thylakoid membrane = GO:0042651 | “reduce the cytochrome b6f complex, increasing proton motive force (pmf) generation across the thylakoid membrane” (milrad2024regulationofmicroalgal pages 1-3) | 10.3390/plants13152103; 2024-07 | High-confidence energetic coupling edge. |
| proton motive force | powers | ATP synthase ATP production | proton motive force = GO:0015990; ATP synthase = GO:0015986; ATP = CHEBI:15422 | the chain generates “lumenal protons needed for NADPH and ATP synthesis” and “an increased generation of ATP by the ATP synthase” (shevela2023solarenergyconversion pages 1-2) | 10.1007/s11120-022-00991-y; 2023-02 | Strong but somewhat indirect in gathered snippets; still standard and curatable. |
| plastocyanin or cytochrome c6 | donates electrons to | Photosystem I | plastocyanin = label-only; cytochrome c6 = label-only; PSI = GO:0009522 | “Electron transfer from cytochrome b6f to PSI is mediated by either plastocyanin (Pc) or cytochrome c6 (Cytc6)” and PSI is replenished by “plastocyanin or cytochrome” (milrad2024regulationofmicroalgal pages 1-3, tian2024photosystemia pages 1-2) | 10.3390/plants13152103; 2024-07; 10.3390/ijms25168767; 2024-08 | High-confidence; choice of donor can depend on metal availability/environment. |
| Photosystem I | reduces | ferredoxin | PSI = GO:0009522; ferredoxin = label-only | “PSI functions as the light-driven plastocyanin-ferredoxin oxidoreductase” and “Electrons are transferred… to ferredoxin” (tian2024photosystemia pages 1-2) | 10.3390/ijms25168767; 2024-08 | High-confidence defining PSI function. |
| linear electron transfer chain | supports | NADPH production | linear electron transfer chain = label-only; NADPH = CHEBI:16474 | “The linear electron transfer chain (Z-scheme) transfers electrons from H2O through PSII to NADP+ reduction” and generates components “needed for NADPH and ATP synthesis” (shevela2023solarenergyconversion pages 1-2) | 10.1007/s11120-022-00991-y; 2023-02 | High-confidence, but FNR not directly evidenced in retrieved snippets. |
| ATP + NADPH | powers | Calvin-Benson(-Bassham) CO2 fixation | ATP = CHEBI:15422; NADPH = CHEBI:16474; CO2 = CHEBI:16526; Calvin-Benson-Bassham cycle = GO:0019253 | oxygenic photosynthesis uses water as electron donor for “CO2 fixation via the Calvin-Benson-Bassham cycle” and reduced ferredoxin provides reducing power used in “CO2 fixation” (milrad2024regulationofmicroalgal pages 1-3, tian2024photosystemia pages 1-2) | 10.3390/plants13152103; 2024-07; 10.3390/ijms25168767; 2024-08 | High-confidence phenotype-level output edge. |
| reduced psaAB expression / low PSI abundance | decreases likelihood of | photoautotrophic growth | psaAB = label-only; PSI = GO:0009522; photoautotrophic growth = label-only | “Mutants with 25-70% wild-type PSI levels remained photoautotrophic” but “strains with less than 10% PSI became obligate photoheterotrophs” (moore2024functionalconsequencesof pages 1-2); “photoautotrophy requires PSI:PSII ratios higher than 1:5” (moore2024functionalconsequencesof pages 13-15) | 10.1128/jb.00454-23; 2024-05 | Strong experimental edge, but taxon-specific to *Synechocystis* PCC 6803; mark uncertain for universal threshold. |
| high light | causes | PSII photodamage / D1 repair cycle activation | high light = ENVO:01001242; PSII = GO:0009523; D1/PsbA = label-only | “High light stress decreases the photosynthetic rate… due to photooxidative damage to photosynthetic apparatus, photoinhibition of PSII” and “degradation of the D1 protein of PSII and its repair cycle help” (from retrieved 2023 review summary) | 10.32615/ps.2023.021; 2023-06 | Useful stress-regulation edge, but evidence here is broader than microbes and should be marked uncertain pending cyanobacteria-specific primary support. |


*Table: This table compiles concise, evidence-backed causal triples for a TraitMech graph of oxygenic photosynthesis, emphasizing high-confidence mechanistic relations and clearly flagging taxon-specific or indirectly supported claims.*

### Additional fine-grained edges supported for expansion

- **D1/D2 reaction-center core — contains/positions → PSII redox cofactors.** Supporting text: “The D1 and D2 proteins form the reaction center … containing redox cofactors essential for primary charge separation.” This supports a structural-enabling edge, not the stronger claim that either protein alone causes oxygen evolution. (shevela2023solarenergyconversion pages 4-5)
- **TyrZ — transfers electrons between → OEC and oxidized PSII donor chemistry.** Supporting text: “TyrZ … functions as an electron carrier between P680 and the Mn4CaO5 oxygen-evolving complex.” Direction should be represented carefully because conventional mechanistic language often describes TyrZ as transferring an electron from the OEC side to P680+. (shevela2023solarenergyconversion pages 9-10)
- **QB — accepts → two electrons and two protons; QB chemistry — produces → PQH2.** Supporting text: “The QB site accepts two electrons sequentially and two protons to form plastoquinol.” (shevela2023solarenergyconversion pages 9-10)
- **PsbO/PsbU/PsbV — stabilizes → Mn4CaO5 OEC in cyanobacteria.** The source says cyanobacterial extrinsic proteins “stabilize the Mn4CaO5 cluster and optimize water-oxidizing activity.” This edge should carry a cyanobacterial qualifier because extrinsic-subunit composition differs in algae and plants. (shevela2023solarenergyconversion pages 4-5)
- **Copper versus iron availability — influences → plastocyanin versus cytochrome c6 use.** The 2024 microalgal review states that carrier expression depends on metal cofactor availability and environmental factors. This is useful for an environmental-regulation branch but is not universal across all cyanobacteria or algae. (milrad2024regulationofmicroalgal pages 1-3)
- **PSI antenna pigments — absorb light and transfer excitation to → P700; P700 excitation — causes → PSI charge separation; PSI electron-transfer chain — reduces → ferredoxin.** These relations are directly summarized in the 2024 PSI review. (tian2024photosystemia pages 1-2)

## Recent developments and quantitative evidence

### Structural resolution of PSII water oxidation

The 2023 authoritative PSII review reports structures not only for the dark-stable state but for semi-stable reaction intermediates and some transient states, enabling molecular-level testing of water-oxidation pathways. A cyanobacterial PSII core monomer contains **17 integral membrane proteins, more than 80 cofactors, and 35 chlorophylls**. The Mn4CaO5 cluster is ligated principally by D1 and CP43 residues, and three water-containing channels connect it to the lumen for substrate access and proton egress. Under optimal low light, reported PSII quantum efficiency is approximately **90%**, while solar-to-chemical conversion at PSII can reach approximately **16%**. These are PSII-level efficiencies, not organismal biomass-conversion efficiencies. (shevela2023solarenergyconversion pages 9-10)

### PSI structure as environmental adaptation

The August 2024 review characterizes PSI as a light-driven plastocyanin–ferredoxin oxidoreductase. Its heterodimeric core is highly conserved, whereas pigment composition and peripheral antenna proteins vary in organisms adapted to fluctuating light, far-red light, iron deficiency, and salinity. This supports a graph architecture in which the PSI core is necessary machinery while antenna variants and stress-responsive remodeling are modulators rather than defining nodes. (tian2024photosystemia pages 1-2)

### Experimental PSI dosage and trait expression

Moore and Vermaas genetically altered `psaAB` regulation in *Synechocystis* PCC 6803. Mutants retaining **25–70%** of wild-type PSI remained photoautotrophic and could show whole-chain oxygen evolution comparable to wild type, whereas strains with **<10%** PSI were obligate photoheterotrophs. (moore2024functionalconsequencesof pages 1-2)

More detailed assays found a photoautotrophic threshold above a PSI:PSII ratio of approximately **1:5**; a strain with about **8%** wild-type PSI could evolve oxygen but could not sustain photoautotrophic survival at 50 µmol photons m−2 s−1. (moore2024functionalconsequencesof pages 13-15) Reduced-PSI strains exhibited approximately **twofold slower P700+ re-reduction**, consistent with reduced cyclic electron flow. Nevertheless, cellular energy charge remained around **0.85–0.87**, versus **0.79 ± 0.01** for wild type, illustrating compensatory energetic regulation. (moore2024functionalconsequencesof pages 7-9) These numerical thresholds are valuable experimental annotations but must not be generalized beyond this strain and growth regime.

### Regulatory understanding

A July 2024 synthesis emphasizes that oxygenic phototrophs regulate antenna capture, electron-carrier connectivity, ion flux, and organelle coupling to tolerate light changes spanning orders of magnitude. It also highlights environment-dependent use of copper-containing plastocyanin versus iron-heme cytochrome c6 between cytochrome b6f and PSI. (milrad2024regulationofmicroalgal pages 1-3)

## Applications and real-world implementation

1. **Biotechnology strain engineering.** Lowering excess PSI can reduce antenna burden and shift light saturation upward. The *Synechocystis* mutants with reduced PSI grew less efficiently under low light but could be productive at higher irradiance, suggesting utility in dense photobioreactors where light distribution and photosystem stoichiometry are engineered. This remains a strain-engineering result rather than a broadly validated industrial implementation. (moore2024functionalconsequencesof pages 18-20, moore2024functionalconsequencesof pages 1-2)
2. **Photosynthetic biomanufacturing.** The causal chain identifies intervention points for redirecting reducing power or ATP toward fuels, chemicals, and biomass: antenna size, PSII repair, cytochrome b6f control, PSI abundance, ferredoxin partitioning, and cyclic electron flow. However, perturbations that improve one light regime can reduce low-light fitness.
3. **Biohybrid/artificial photosynthesis.** Atomic and intermediate-state knowledge of the Mn4CaO5 water-oxidizing catalyst is used as a blueprint for synthetic water-splitting catalysts. The 2023 review explicitly frames PSII water oxidation as inspiration for scalable renewable-energy catalysis. (shevela2023solarenergyconversion pages 1-2)
4. **Ecophysiological monitoring.** Oxygen evolution, P700 redox kinetics, fluorescence yields, and 77-K spectra provide complementary readouts. No single assay establishes the whole trait: PSII-specific oxygen evolution can persist when PSI abundance is insufficient for photoautotrophy. (moore2024functionalconsequencesof pages 13-15, moore2024functionalconsequencesof pages 12-13)

## Recommended minimum YAML graph

A compact first implementation should prioritize:

`light → PSII charge separation → OEC water oxidation → O2 + H+ + electrons → PQ reduction/PQH2 → cytochrome b6f → thylakoid pmf → ATP synthase/ATP`, together with `cytochrome b6f → plastocyanin or cytochrome c6 → PSI charge separation → ferredoxin → NADPH`, and `ATP + NADPH → Calvin–Benson–Bassham CO2 fixation → photoautotrophic biomass`.

Add D1/D2, TyrZ, QB, PsbO/PsbU/PsbV, `psaAB`, and environmental regulation as second-layer mechanistic nodes. This preserves the existing water-splitting core while making the graph discriminate complete oxygenic photoautotrophy from isolated PSII activity.

## Warnings: claims not yet ready for unqualified curation

- **Do not curate “PSII activity causes photoautotrophic growth” without PSI and downstream-chain context.** Oxygen evolution can persist below the PSI abundance needed for autotrophy. (moore2024functionalconsequencesof pages 13-15)
- **Do not encode the <10% PSI or PSI:PSII >1:5 thresholds as universal.** They are specific to engineered *Synechocystis* PCC 6803 under particular culture and illumination conditions. (moore2024functionalconsequencesof pages 13-15, moore2024functionalconsequencesof pages 1-2)
- **Do not infer the trait from `psbA` or `psbD` alone.** These genes occur in cyanophages and divergent paralogs can have specialized or inactive roles; complete machinery and phenotype evidence are needed.
- **Do not universalize extrinsic OEC subunits.** Cyanobacteria commonly use PsbV and PsbU where plants/algae have different complements. (shevela2023solarenergyconversion pages 4-5)
- **Do not curate FNR-specific or DCMU-specific edges from this evidence set.** The broader NADP+ reduction and PSII-to-PQ relations are supported, but a direct retrieved passage for FNR catalysis or DCMU binding/inhibition was not obtained.
- **Do not represent CO2 fixation as the chemical source of evolved oxygen.** The evolved O2 comes from water oxidation at PSII; CO2 is reduced into organic carbon.
- **Do not use cyclic PSI electron flow as a defining positive assay.** It contributes pmf/ATP but does not split water or evolve O2.
- **Treat high-light → D1 repair as provisional for this microbial graph.** The retrieved 2023 source is broader than microbial systems; add a cyanobacterial primary study before unqualified curation.
- **Verify all CURIEs against the target ontology release before committing YAML.** Labels such as P680, P700, QA/QB, Mn4CaO5, photoautotrophic growth, and individual electron carriers may be better represented as label-only nodes than forced into inappropriate ontology classes.

## DOI-first bibliography

1. Shevela D, Kern J, Govindjee, Messinger J. **Solar energy conversion by photosystem II: principles and structures.** *Photosynthesis Research* 156, 279–307. Published February 2023. DOI: [10.1007/s11120-022-00991-y](https://doi.org/10.1007/s11120-022-00991-y). (shevela2023solarenergyconversion pages 1-2, shevela2023solarenergyconversion pages 9-10)
2. Milrad Y, Mosebach L, Buchert F. **Regulation of Microalgal Photosynthetic Electron Transfer.** *Plants* 13, 2103. Published July 2024. DOI: [10.3390/plants13152103](https://doi.org/10.3390/plants13152103). (milrad2024regulationofmicroalgal pages 1-3)
3. Tian L-R, Chen J-H. **Photosystem I: A Paradigm for Understanding Biological Environmental Adaptation Mechanisms in Cyanobacteria and Algae.** *International Journal of Molecular Sciences* 25, 8767. Published August 2024. DOI: [10.3390/ijms25168767](https://doi.org/10.3390/ijms25168767). (tian2024photosystemia pages 1-2)
4. Moore V, Vermaas W. **Functional consequences of modification of the photosystem I/photosystem II ratio in the cyanobacterium *Synechocystis* sp. PCC 6803.** *Journal of Bacteriology* 206(5). Published May 2024. DOI: [10.1128/jb.00454-23](https://doi.org/10.1128/jb.00454-23). (moore2024functionalconsequencesof pages 18-20, moore2024functionalconsequencesof pages 1-2)
5. Sharma N et al. **Photosystems under high light stress: throwing light on mechanism and adaptation.** *Photosynthetica* 61, 250–263. Published June 2023. DOI: [10.32615/ps.2023.021](https://doi.org/10.32615/ps.2023.021). Use only provisionally for the microbial high-light/D1-repair branch.

The two supplied foundational references should remain attached to the trait-level definition: Bryant and Frigaard, DOI [10.1016/j.tim.2006.09.001](https://doi.org/10.1016/j.tim.2006.09.001), for the oxygenic/anoxygenic distinction; and Fischer et al., DOI [10.1146/annurev-earth-060313-054810](https://doi.org/10.1146/annurev-earth-060313-054810), for the evolution of cyanobacterial water-oxidizing, oxygen-evolving photosynthesis.

References

1. (shevela2023solarenergyconversion pages 1-2): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 201 citations and is from a peer-reviewed journal.

2. (tian2024photosystemia pages 1-2): Li-Rong Tian and Jing-Hua Chen. Photosystem i: a paradigm for understanding biological environmental adaptation mechanisms in cyanobacteria and algae. International Journal of Molecular Sciences, 25:8767, Aug 2024. URL: https://doi.org/10.3390/ijms25168767, doi:10.3390/ijms25168767. This article has 8 citations.

3. (moore2024functionalconsequencesof pages 13-15): Vicki Moore and Wim Vermaas. Functional consequences of modification of the photosystem i/photosystem ii ratio in the cyanobacterium <i>synechocystis</i> sp. pcc 6803. Journal of Bacteriology, May 2024. URL: https://doi.org/10.1128/jb.00454-23, doi:10.1128/jb.00454-23. This article has 25 citations and is from a peer-reviewed journal.

4. (moore2024functionalconsequencesof pages 12-13): Vicki Moore and Wim Vermaas. Functional consequences of modification of the photosystem i/photosystem ii ratio in the cyanobacterium <i>synechocystis</i> sp. pcc 6803. Journal of Bacteriology, May 2024. URL: https://doi.org/10.1128/jb.00454-23, doi:10.1128/jb.00454-23. This article has 25 citations and is from a peer-reviewed journal.

5. (moore2024functionalconsequencesof pages 1-2): Vicki Moore and Wim Vermaas. Functional consequences of modification of the photosystem i/photosystem ii ratio in the cyanobacterium <i>synechocystis</i> sp. pcc 6803. Journal of Bacteriology, May 2024. URL: https://doi.org/10.1128/jb.00454-23, doi:10.1128/jb.00454-23. This article has 25 citations and is from a peer-reviewed journal.

6. (moore2024functionalconsequencesof pages 7-9): Vicki Moore and Wim Vermaas. Functional consequences of modification of the photosystem i/photosystem ii ratio in the cyanobacterium <i>synechocystis</i> sp. pcc 6803. Journal of Bacteriology, May 2024. URL: https://doi.org/10.1128/jb.00454-23, doi:10.1128/jb.00454-23. This article has 25 citations and is from a peer-reviewed journal.

7. (shevela2023solarenergyconversion pages 4-5): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 201 citations and is from a peer-reviewed journal.

8. (shevela2023solarenergyconversion pages 9-10): D. Shevela, J. Kern, Govindjee Govindjee, and J. Messinger. Solar energy conversion by photosystem ii: principles and structures. Photosynthesis Research, 156:279-307, Feb 2023. URL: https://doi.org/10.1007/s11120-022-00991-y, doi:10.1007/s11120-022-00991-y. This article has 201 citations and is from a peer-reviewed journal.

9. (milrad2024regulationofmicroalgal pages 1-3): Yuval Milrad, Laura Mosebach, and Felix Buchert. Regulation of microalgal photosynthetic electron transfer. Plants, 13:2103, Jul 2024. URL: https://doi.org/10.3390/plants13152103, doi:10.3390/plants13152103. This article has 13 citations.

10. (moore2024functionalconsequencesof pages 18-20): Vicki Moore and Wim Vermaas. Functional consequences of modification of the photosystem i/photosystem ii ratio in the cyanobacterium <i>synechocystis</i> sp. pcc 6803. Journal of Bacteriology, May 2024. URL: https://doi.org/10.1128/jb.00454-23, doi:10.1128/jb.00454-23. This article has 25 citations and is from a peer-reviewed journal.