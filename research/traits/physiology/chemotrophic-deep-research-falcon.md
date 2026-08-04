---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:04:34.906899'
end_time: '2026-08-04T11:11:25.717333'
duration_seconds: 410.81
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
  causal_graph_summary: 'chemotrophic_chemical_redox_energy: 13 nodes, 12 edges'
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
- **Trait label:** chemotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000641
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_chemotroph, chemotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports chemical redox reactions as energy sources for respiratory energy conservation.)
- **Existing causal graph summary:** chemotrophic_chemical_redox_energy: 13 nodes, 12 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000641
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_chemotroph, chemotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports chemical redox reactions as energy sources for respiratory energy conservation.)
- **Existing causal graph summary:** chemotrophic_chemical_redox_energy: 13 nodes, 12 edges

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


# Curation report: microbial chemotrophic trait

## 1. Scope summary

**Target:** `METPO:1000641` — **chemotrophic**; category **PHYSIOLOGY**; term kind **CLASS**; mapping **REVIEWED**; parent `METPO:1000631`.

**Operational definition.** Chemotrophy is the physiological capacity to obtain usable energy from oxidation–reduction reactions involving chemical compounds. A donor is oxidized, electrons pass to an acceptor, and the released free energy is conserved—commonly through a membrane electron-transfer chain, ion-motive force, and ATP synthesis. This agrees with the supplied definition: “A trophic type in which an organism obtains energy from chemical oxidation of either inorganic or organic compounds.” Modern reviews likewise describe chemotrophs as exploiting environmental electron donors and acceptors and respiratory complexes as generating proton-motive force for ATP synthase. (gupta2020extracellularelectronuptake pages 5-6)

### Important boundaries

1. **Chemotrophy is an energy-source classification, not a carbon-source classification.** Chemotrophs may be autotrophic, using CO₂, or heterotrophic, using organic carbon. Therefore, neither “autotrophic” nor “heterotrophic” should be made equivalent to `METPO:1000641`.
2. **Chemolithotrophy** is the subset using inorganic electron donors such as H₂, Fe(II), reduced sulfur compounds, ammonia, nitrite, or CO. **Chemoorganotrophy** uses organic donors. The parent chemotrophic graph should remain donor-agnostic, with these as branches.
3. **Phototrophy** differs because light is the primary energy input. A facultative organism can express both modes under different conditions, but phototrophic growth alone is not evidence for chemotrophy.
4. **Aerobic versus anaerobic respiration** concerns the terminal acceptor, not whether an organism is chemotrophic. Oxygen, nitrate, sulfate, sulfur species, metals, and other compounds can serve as acceptors in different taxa. Sulfur oxidizers, for example, couple reduced-sulfur oxidation to oxygen or nitrate reduction. (gupta2020extracellularelectronuptake pages 8-9)
5. **Fermentation is a boundary case.** It is chemical energy metabolism, but it lacks an external terminal electron acceptor and often conserves energy by substrate-level phosphorylation. Curating fermentation under this broad METPO definition may be defensible, but a respiratory-chain mechanism must not be asserted for every fermentative chemotroph.
6. **Electroautotrophy/electrolithotrophy is another boundary case.** Electrode-derived electrons can support metabolism and CO₂ fixation, but an electrode is not conventionally a molecular compound. It should be represented as an assay-specific extension or sibling mode rather than silently generalized to all chemotrophy. (wang2024characterizethegrowth pages 22-23, llorente2024novelelectrochemicalstrategies pages 1-2)
7. **Genes alone do not establish the trait.** Detection of `sox`, hydrogenase, or carbon-fixation genes supports metabolic potential, but physiological evidence requires donor-dependent growth, substrate turnover, energy conservation, or comparable functional measurements.

## 2. Recommended graph architecture

The existing 13-node/12-edge graph appears appropriately sized for a **minimal core**, but it should separate universal bioenergetics from taxon-specific examples:

**chemical electron donor → donor oxidation/redox reaction → electron transfer → energy-conserving membrane complex → ion-motive force → ATP synthase → ATP → growth/maintenance**

Add conditional branches for:

- terminal electron acceptor reduction;
- reverse electron transport and reducing-equivalent generation;
- carbon fixation only for chemoautotrophs;
- substrate-level phosphorylation for fermentative chemoorganotrophs;
- donor-specific modules such as Fe(II)/Cyc2/Rus or thiosulfate/Sox.

The literature supports outer-membrane cytochromes, periplasmic carriers, and inner-membrane respiratory complexes as an electron-transfer route that generates proton-motive force, which ATP synthase uses to make ATP. Reverse electron flow can generate NADH for CO₂ fixation. (gupta2020extracellularelectronuptake pages 5-6)

## 3. Candidate nodes grouped by type

Ontology identifiers below are limited to high-confidence mappings. Labels without CURIEs should undergo ontology lookup before YAML insertion.

### Trait and taxon/context nodes

- chemotrophic — `METPO:1000641`
- chemolithotrophy — label-only pending METPO verification
- chemoorganotrophy — label-only pending METPO verification
- chemoautotrophy — label-only pending METPO verification
- *Acidithiobacillus ferrooxidans* — NCBITaxon identifier should be verified at curation time
- *Hydrogenovibrio* strain 104 / hydrothermal-vent *Hydrogenovibrio* isolates — strain-specific label
- sulfate-reducing bacteria — taxonomic/functional group; not one NCBITaxon node
- autotrophic electroactive microbial enrichment — assay-community node

### Chemicals and environmental substrates

- chemical electron donor — role node; label-only
- chemical electron acceptor — role node; label-only
- dioxygen — `CHEBI:15379`
- carbon dioxide — `CHEBI:16526`
- proton — `CHEBI:15378`
- ATP — `CHEBI:30616`
- Fe(II), Fe(III), molecular hydrogen, sulfide, elemental sulfur, thiosulfate, nitrate, sulfate, water, NADH, acetate, formate, propionate — use ChEBI after identifier validation
- reduced inorganic sulfur compounds — collection/class node rather than a single molecule
- polarized carbon electrode — experimental-factor/material node
- electron — chemical/physical carrier node; verify ChEBI mapping

### Molecular functions, proteins, and complexes

- oxidoreductase activity — `GO:0016491`
- ATP synthase; ATP synthesis coupled proton transport — `GO:0015986`
- electron-transfer/respiratory chain — `GO:0022900` is a candidate broad process mapping; confirm suitability for prokaryotic annotation
- outer-membrane cytochrome c Cyc2
- rusticyanin, Rus
- Sox sulfur-oxidation system: SoxXA, SoxYZ, SoxB, SoxCD
- hydrogenase; specific [NiFe]-hydrogenase should be subtype-resolved where evidence permits
- RubisCO large/small subunits, `cbbL`/`cbbS`
- Qrc, Tmc, QmoABC, and Dsr complexes
- PioAB and MtoAB extracellular/iron electron-transfer modules
- pilin and porin
- NADH-generating reverse-electron-transport machinery

For Cyc2, Rus, Sox proteins, and hydrogenases, use UniProt identifiers only when a strain and sequence are specified. Gene-symbol-only nodes are safer for the current cross-taxon graph.

### Pathways and biological processes

- chemical oxidation–reduction reaction
- donor oxidation
- terminal electron-acceptor reduction
- respiratory electron transport
- proton translocation and proton-motive-force generation
- oxidative phosphorylation
- ATP production
- reverse electron transport
- CO₂ fixation
- Calvin–Benson–Bassham cycle
- Wood–Ljungdahl pathway
- Sox pathway/thiosulfate oxidation
- Fe(II) oxidation
- hydrogen oxidation
- extracellular electron uptake
- biomass production and cellular growth

### Cellular locations

- extracellular space or cell exterior
- outer membrane
- periplasm
- cytoplasmic membrane
- cytoplasm

These locations are especially useful for Gram-negative exemplars such as *A. ferrooxidans*, but they should not be universalized to monoderm bacteria or archaea.

### Environmental and experimental factors

- availability and concentration of electron donor
- availability and redox potential of terminal acceptor
- donor–acceptor redox disequilibrium/Gibbs-energy yield
- oxygen concentration and redox gradient
- pH and temperature
- sulfide-rich, oxygen-poor sediment or water
- hydrothermal vent
- acid mine drainage or metal-sulfide ore
- electrode potential
- carbon-source composition and nutrient limitation

For *A. ferrooxidans*, reported favorable conditions include approximately pH 2 and 30 °C, but these are taxon-specific rather than defining properties of chemotrophy. (wang2024characterizethegrowth pages 1-2)

## 4. Candidate evidence-backed causal edges

The compact table below summarizes the strongest candidates.

| subject | predicate | object | evidence context/taxon | confidence/curation status |
|---|---|---|---|---|
| chemical electron donor oxidation | drives | electron transfer through redox carriers/respiratory chain | General chemotroph mechanism across bacteria and archaea (gupta2020extracellularelectronuptake pages 5-6, wang2024characterizethegrowth pages 1-2) | High; broad core mechanism |
| respiratory electron transfer chain | generates | proton motive force | General chemotroph bioenergetics (gupta2020extracellularelectronuptake pages 5-6) | High; broad core mechanism |
| proton motive force | powers | ATP synthase and ATP production | General chemotroph bioenergetics (gupta2020extracellularelectronuptake pages 5-6) | High; broad core mechanism |
| Fe(II) | is oxidized by | Cyc2 | *Acidithiobacillus ferrooxidans* chemoautotrophy (wang2024characterizethegrowth pages 1-2) | High; taxon-specific, experimental/literature-backed |
| Cyc2-mediated Fe(II) oxidation | transfers electrons to | rusticyanin (Rus) | *A. ferrooxidans* iron-oxidation pathway (wang2024characterizethegrowth pages 1-2) | High; taxon-specific |
| reduced inorganic sulfur compounds | provide electrons for | chemolithoautotrophic growth and CO2 fixation | *A. ferrooxidans* and sulfur oxidizers broadly (wang2024characterizethegrowth pages 1-2, gupta2020extracellularelectronuptake pages 8-9) | High for trait relevance; moderate for cross-taxon generalization |
| thiosulfate oxidation | upregulates | Sox pathway genes (soxZ/soxC/soxY/soxX) | *Hydrogenovibrio* strain 104 on S2O3^2− (laufermeiser2024oxidationofsulfur pages 6-8) | High; taxon-specific, transcriptomic |
| thiosulfate-supported growth | upregulates | RubisCO structural genes (cbbLS) | *Hydrogenovibrio* strain 104 on S2O3^2− (laufermeiser2024oxidationofsulfur pages 6-8) | High; taxon-specific, transcriptomic |
| thiosulfate oxidation | supports | autotrophic CO2 fixation | Hydrothermal-vent *Hydrogenovibrio* isolates (laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur pages 6-8) | High; taxon-specific, physiological + transcriptomic |
| H2 oxidation | supports | autotrophic CO2 fixation | Hydrothermal-vent *Hydrogenovibrio* isolates (laufermeiser2024oxidationofsulfur pages 1-2) | High; taxon-specific, physiological |
| Fe(II) oxidation | supports | autotrophic CO2 fixation | Hydrothermal-vent *Hydrogenovibrio* isolates (laufermeiser2024oxidationofsulfur pages 1-2) | Moderate; taxon-specific physiology, iron-oxidation machinery unresolved |
| unknown iron-oxidation pathway | may mediate | Fe(II)-derived electron transfer | *Hydrogenovibrio* on Fe(II), no known Fe-oxidation genes detected (laufermeiser2024oxidationofsulfur pages 1-2) | Uncertain; do not curate as specific gene edge yet |
| electrode-derived electrons | feed | autotrophic electron uptake metabolism | Enriched electroactive autotrophs in microbial electrosynthesis reactor (llorente2024novelelectrochemicalstrategies pages 1-2, gupta2020extracellularelectronuptake pages 5-6) | High; assay-specific/system-specific |
| electrode-derived electrons | support | Wood-Ljungdahl pathway CO2 fixation | Homoacetogenic enrichment in fluidized-bed biocathode reactor (llorente2024novelelectrochemicalstrategies pages 1-2) | Moderate; pathway assignment from enrichment context, not isolate-resolved |
| Wood-Ljungdahl CO2 fixation | produces | acetate | Microbial electrosynthesis fluidized-bed reactor (llorente2024novelelectrochemicalstrategies pages 1-2) | High; assay-specific output |
| electrode-derived electrons | support production of | biomass | Microbial electrosynthesis fluidized-bed reactor (llorente2024novelelectrochemicalstrategies pages 1-2) | High; assay-specific output |
| electroautotrophic growth | increases expression of | pilin/porin and ATP-related genes | *A. ferrooxidans* on electrode versus Fe(II) chemoautotrophy (wang2024characterizethegrowth pages 22-23) | Moderate; mode-specific and not generic chemotrophy |
| electrode electron uptake | is distinct from | canonical chemoautotrophic Fe(II)/RISC pathway | *A. ferrooxidans* comparison of electroautotrophy vs chemoautotrophy (wang2024characterizethegrowth pages 22-23) | Moderate; useful boundary-case warning |
| low pH (around 2.0) and 30°C | favor | growth of *A. ferrooxidans* chemotrophy | *A. ferrooxidans* physiology (wang2024characterizethegrowth pages 1-2) | Moderate; strongly taxon-specific environmental control |


*Table: This table summarizes the strongest candidate causal edges for curating the chemotrophic trait, emphasizing core bioenergetic mechanisms and a few well-supported taxon-specific pathways. It also flags assay-specific and uncertain edges that should be treated cautiously in TraitMech curation.*

The following expanded triples provide source snippets and curation notes.

| Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---|---|---|---|---|
| chemical electron-donor oxidation | drives | respiratory electron transfer | Gupta et al. (2020): outer-membrane cytochromes and periplasmic shuttles deliver electrons to inner-membrane respiratory complexes. (gupta2020extracellularelectronuptake pages 5-6) | **High-confidence core edge.** Avoid implying the same proteins occur in every chemotroph. |
| respiratory electron transfer | generates | proton-motive force | Gupta et al. (2020): inner-membrane respiratory complexes “generate proton motive force.” (gupta2020extracellularelectronuptake pages 5-6) | **High-confidence for respiratory chemotrophy**, not universal to fermentation. |
| proton-motive force | powers | ATP synthase-dependent ATP formation | Gupta et al. (2020): proton-motive force is “used by ATP synthase to produce ATP.” (gupta2020extracellularelectronuptake pages 5-6) | **High-confidence core respiratory edge.** Ground process with `GO:0015986`. |
| reverse electron flow | produces | NADH/reducing power for CO₂ fixation | Gupta et al. (2020): “NADH is generated by reverse electron flow for CO₂ fixation.” (gupta2020extracellularelectronuptake pages 5-6) | **Conditional**, particularly important where donor potential is insufficient to reduce NAD(P)⁺ directly. |
| Fe(II) | is oxidized by | Cyc2 | Wang et al. (2024): the pathway includes “outer-membrane cytochrome c (Cyc2) oxidizing Fe2+ to Fe3+.” (wang2024characterizethegrowth pages 1-2) | **Strong, taxon-specific** edge for *A. ferrooxidans*. Do not generalize Cyc2 to all iron oxidizers. |
| Cyc2-mediated Fe(II) oxidation | transfers electrons to | rusticyanin | Wang et al. (2024): electrons flow from Cyc2 “to rusticyanin (Rus).” (wang2024characterizethegrowth pages 1-2) | **Strong, taxon-specific.** |
| Fe(II) or reduced inorganic sulfur compounds | supplies energy for | *A. ferrooxidans* chemolithoautotrophic growth | Wang et al. (2024): the organism “derives energy from oxidation of Fe2+ or reduced inorganic sulfur compounds,” uses O₂, and fixes CO₂ by the Calvin cycle. (wang2024characterizethegrowth pages 1-2) | **Strong physiological edge.** Separate energy donor, acceptor, and carbon source in YAML. |
| thiosulfate growth condition | increases expression of | `soxZ`, `soxC`, `soxY`, and `soxX` | Laufer-Meiser et al. (2024): these Sox genes “were upregulated during S₂O₃²⁻ growth.” (laufermeiser2024oxidationofsulfur pages 6-8) | **Strong transcriptomic association**, but “increases expression of” is safer than “is required for” without knockout evidence. |
| thiosulfate-supported chemotrophy | increases expression of | `cbbL`/`cbbS` | Laufer-Meiser et al. (2024): RubisCO genes “were markedly upregulated during S₂O₃²⁻ growth.” (laufermeiser2024oxidationofsulfur pages 6-8) | **Taxon-specific and transcriptomic.** Supports coupling to carbon fixation but does not alone prove direct regulation. |
| thiosulfate oxidation | supports | autotrophic CO₂ fixation | Hydrothermal-vent *Hydrogenovibrio* oxidized thiosulfate and fixed CO₂; estimated maxima were 952 mmol oxidation and 84 mmol CO₂ fixation per vent per hour. (laufermeiser2024oxidationofsulfur pages 1-2) | **Strong physiology plus quantitative estimate**, but rates are model-based vent-scale maxima, not universal cellular rates. |
| H₂ oxidation | supports | autotrophic CO₂ fixation | The same isolates showed estimated maxima of 24 mmol H₂ oxidation and 1 mmol CO₂ fixation per vent per hour. (laufermeiser2024oxidationofsulfur pages 1-2) | **Strong, taxon- and environment-specific.** |
| Fe(II) oxidation | supports | autotrophic CO₂ fixation | The isolates showed estimated maxima of 10 mmol iron oxidation and 0.3 mmol CO₂ fixation per vent per hour. (laufermeiser2024oxidationofsulfur pages 1-2) | **Moderate confidence.** Physiology is supported, but the responsible iron-oxidation machinery remains unresolved. |
| specific known iron-oxidation gene | mediates | *Hydrogenovibrio* Fe(II) oxidation | Laufer-Meiser et al. detected “no known iron-oxidation genes”; upregulated transcripts suggested an unknown pathway. (laufermeiser2024oxidationofsulfur pages 1-2) | **Do not curate as a positive specific-gene edge.** Preserve as an explicit knowledge gap. |
| polarized electrode | donates electrons to | autotrophic electroactive enrichment | Llorente et al. (2024): a carbon bed polarized at −0.6, −0.8, or −1 V acted as an electron-donating biocathode. (llorente2024novelelectrochemicalstrategies pages 1-2) | **Strong but assay-specific.** Treat as electroautotrophy, not canonical molecular chemolithotrophy. |
| electrode-derived electrons plus CO₂ | supports | acetate and biomass formation | The reactor produced acetate at approximately 1 g L⁻¹ day⁻¹ and planktonic biomass up to approximately 0.7 g L⁻¹ dry weight. (llorente2024novelelectrochemicalstrategies pages 1-2) | **Strong reactor-level edge.** Community enrichment prevents assignment to one taxon. |
| electroautotrophic growth | increases expression of | pilin, porin, and ATP-related genes | Wang et al. found increased expression of transmembrane proteins and ATP-related genes under electrode growth; 493 genes differed overall. (wang2024characterizethegrowth pages 22-23, wang2024characterizethegrowth pages 1-2) | **Moderate, condition-specific.** Differential expression is not proof that each gene is causally required. |
| sulfide/reduced sulfur oxidation | couples to | oxygen or nitrate reduction | Gupta et al. describe sulfur-oxidizing chemoautotrophs oxidizing H₂S/HS⁻ while reducing oxygen or nitrate. (gupta2020extracellularelectronuptake pages 8-9) | **Strong pathway-level edge**, but enzyme implementation varies by taxon. |
| extracellular solid electron donor | transfers electrons through | PioAB-like outer-membrane conduit | Gupta et al. describe PioAB-mediated electron transfer from Fe(II) across the outer membrane. (gupta2020extracellularelectronuptake pages 8-9) | **Taxon-specific exemplar**, not a universal chemotrophy node. |
| low pH and 30 °C | favor | *A. ferrooxidans* growth | Wang et al. report optimum growth around pH 2.0 and 30 °C. (wang2024characterizethegrowth pages 1-2) | **Taxon-specific environmental edge.** It should not define `METPO:1000641`. |

## 5. Recent developments and quantitative findings

### Metabolic versatility at hydrothermal vents

The 2024 *Hydrogenovibrio* study provides unusually direct evidence that one lineage can switch among three inorganic donors—Fe(II), H₂, and thiosulfate—while fixing CO₂. The estimated vent-scale maxima differed markedly: 10, 24, and 952 mmol donor oxidation per vent per hour, respectively, paired with 0.3, 1, and 84 mmol CO₂ fixation. This supports a graph in which environmental donor availability selects among alternative oxidation modules feeding a shared autotrophic program. It also cautions against representing chemolithotrophy as a one-donor/one-organism trait. (laufermeiser2024oxidationofsulfur pages 1-2)

Transcriptomics connected thiosulfate growth to induction of `soxZ/C/Y/X` and `cbbLS`, whereas several assimilatory sulfate-reduction genes increased under Fe(II) or H₂ growth. Nevertheless, expression data demonstrate condition-responsive association, not strict enzyme necessity. (laufermeiser2024oxidationofsulfur pages 6-8)

### Electroautotrophic extensions

A 2024 fluidized-bed microbial-electrosynthesis reactor converted electrode-derived electrons and CO₂ into biomass and volatile fatty acids. At −0.6 to −1 V versus Ag/AgCl, acetate reached approximately 1 g L⁻¹ day⁻¹ and planktonic biomass approximately 0.7 g L⁻¹ dry weight. This is a real reactor implementation of chemically/electrochemically driven microbial production, but the enrichment and reactor context make the corresponding edges community- and assay-specific. (llorente2024novelelectrochemicalstrategies pages 1-2)

In *A. ferrooxidans*, comparison of Fe(II)-supported chemoautotrophy with electrode-supported electroautotrophy identified 493 differentially expressed genes—297 downregulated and 196 upregulated under electroautotrophy. Increased pilin, porin, ATP-associated expression and EPS production indicate that direct electron uptake invokes a distinct surface-interaction program rather than merely substituting an electrode for dissolved Fe(II). (wang2024characterizethegrowth pages 22-23, wang2024characterizethegrowth pages 1-2)

### Mechanistic uncertainty remains important

The absence of recognizable iron-oxidation genes in the versatile *Hydrogenovibrio* isolates, despite measured Fe(II)-dependent physiology, illustrates an expert curation principle: a demonstrated trait may be stronger evidence than annotation-based pathway prediction, while the causal gene edge remains unresolved. (laufermeiser2024oxidationofsulfur pages 1-2)

## 6. Current applications and real-world implementations

- **Biomining and bioleaching.** *A. ferrooxidans* oxidizes Fe(II) and reduced sulfur in acidic ores and mine drainage. The 2024 study describes industrial bioleaching as contributing more than 30% of global copper production from low-grade ores, making this the clearest mature implementation of chemolithotrophic energy metabolism. The percentage should be retained with its source and not generalized to all copper production routes. (wang2024characterizethegrowth pages 1-2)
- **Microbial electrosynthesis and carbon conversion.** Electrode-fed enrichments can convert CO₂ into acetate, formate, propionate, and biomass. Current limitations include electron-transfer efficiency, mass transport, product selectivity, and community attribution. (llorente2024novelelectrochemicalstrategies pages 1-2)
- **Wastewater and nutrient removal.** Sulfur-, hydrogen-, iron-, ammonia-, and nitrite-oxidizing chemotrophs underpin autotrophic nitrogen and sulfur transformations. For TraitMech, these should be represented in process-specific child graphs because donors, acceptors, enzymes, and environmental constraints differ.
- **Biogeochemical cycling and ecosystem primary production.** Sulfur- and hydrogen-oxidizing chemolithoautotrophs sustain biomass in oxygen-poor sediments, sulfide-rich springs, and hydrothermal vents; donor–acceptor interfaces and redox gradients are therefore ecological enabling conditions rather than merely locations. (gupta2020extracellularelectronuptake pages 8-9, laufermeiser2024oxidationofsulfur pages 1-2)
- **Bioelectrochemical corrosion and remediation.** Sulfate reducers can take up electrons from elemental iron or electrodes, although mechanisms are incompletely resolved and may involve direct uptake, H₂ intermediates, or both. Species-specific electrode potentials in reported experiments ranged approximately from −310 to −500 mV versus SHE. (gupta2020extracellularelectronuptake pages 5-6)

## 7. Expert analysis for TraitMech curation

The most defensible graph is **mechanism-centered but modular**. The invariant concept is not a particular donor, acceptor, pathway, carbon source, or enzyme. It is conservation of energy from a chemical redox process. Accordingly:

1. Keep a compact, high-confidence respiratory backbone.
2. Make electron donor and acceptor explicit roles rather than hard-coding oxygen.
3. Add chemolithotrophic and chemoorganotrophic branches.
4. Make CO₂ fixation conditional on chemoautotrophy.
5. Represent fermentation separately from the electron-transport-chain branch.
6. Place Cyc2/Rus, Sox, hydrogenases, PioAB, and extracellular uptake under taxon- or mechanism-specific modules.
7. Use experimental qualifiers such as `condition_increases_expression_of`, `supports_growth_of`, and `associated_with` when evidence is transcriptomic or community-level; reserve `required_for` for genetics or decisive inhibition/complementation evidence.

## 8. Warnings: claims not yet ready for curation

- **Do not assert that all chemotrophs use respiration, a proton gradient, or oxidative phosphorylation.** Fermentative chemotrophy is a counterexample.
- **Do not equate chemotrophy with chemoautotrophy or CO₂ fixation.** Organic-carbon chemotrophs are included by definition.
- **Do not assert oxygen as the universal acceptor.** Nitrate, sulfate, sulfur compounds, metals, and other acceptors support anaerobic chemotrophy.
- **Do not infer a phenotype from pathway genes alone.** Metagenomic occurrence or transcript induction does not prove donor-dependent energy conservation.
- **Do not curate a named Fe(II)-oxidation enzyme for the 2024 *Hydrogenovibrio* isolates.** The study explicitly lacked known iron-oxidation genes. (laufermeiser2024oxidationofsulfur pages 1-2)
- **Do not universalize Cyc2/Rus or Sox.** They are strong exemplars but are not present in all iron- or sulfur-oxidizing microorganisms.
- **Do not treat electrode uptake as unqualified canonical chemotrophy.** Mark it electroautotrophic/electrolithotrophic and assay-specific.
- **Do not treat differential expression as necessity.** The `sox`, `cbb`, pilin, porin, and ATP-related results support regulation or association, not knockout-level causality. (wang2024characterizethegrowth pages 22-23, laufermeiser2024oxidationofsulfur pages 6-8)
- **Do not curate pH 2 or 30 °C as trait-wide preferences.** Those conditions concern *A. ferrooxidans*. (wang2024characterizethegrowth pages 1-2)
- **Validate all ontology identifiers before committing YAML.** In particular, strain-level NCBITaxon, UniProt, Rhea, KEGG, EC, and ChEBI identifiers should be sequence- or reaction-specific; no identifier should be inferred from a gene label alone.

## 9. DOI-first bibliography

1. Wang Q, Long H, Wang H, Vetter MCY Lau. **Characterize the Growth and Metabolism of *Acidithiobacillus ferrooxidans* under Electroautotrophic and Chemoautotrophic Conditions.** *Microorganisms* 12:590. Published **15 March 2024**. DOI: [10.3390/microorganisms12030590](https://doi.org/10.3390/microorganisms12030590). (wang2024characterizethegrowth pages 1-2)
2. Laufer-Meiser K et al. **Oxidation of sulfur, hydrogen, and iron by metabolically versatile *Hydrogenovibrio* from deep sea hydrothermal vents.** *ISME Journal* 18. Published **2024**. DOI: [10.1093/ismejo/wrae173](https://doi.org/10.1093/ismejo/wrae173). (laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur pages 6-8)
3. Llorente M, Tejedor-Sanz S, Berná A, Manchón C, Esteve-Núñez A. **Novel electrochemical strategies for the microbial conversion of CO₂ into biomass and volatile fatty acids using a fluid-like bed electrode in a three-phase reactor.** *Microbial Biotechnology* 17. Published **January 2024**. DOI: [10.1111/1751-7915.14383](https://doi.org/10.1111/1751-7915.14383). (llorente2024novelelectrochemicalstrategies pages 1-2)
4. Gupta D, Guzman MS, Bose A. **Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications.** *Journal of Industrial Microbiology and Biotechnology* 47:863–876. Published **October 2020**. DOI: [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0). (gupta2020extracellularelectronuptake pages 5-6, gupta2020extracellularelectronuptake pages 8-9)

## Curation recommendation

Retain `METPO:1000641` as a broad energy-source trait. Curate the generic redox-to-energy-conservation backbone first, with explicit exceptions for fermentation. Add Fe(II)/Cyc2/Rus, thiosulfate/Sox, H₂ oxidation, CO₂ fixation, and electrode uptake as qualified subgraphs carrying taxon, environmental, and evidence-type annotations. The strongest new 2024 additions are the multi-donor *Hydrogenovibrio* physiology, donor-responsive Sox/RubisCO expression, the quantified microbial-electrosynthesis outputs, and the direct comparison between electrode- and Fe(II)-supported *A. ferrooxidans* growth.

References

1. (gupta2020extracellularelectronuptake pages 5-6): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

2. (gupta2020extracellularelectronuptake pages 8-9): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

3. (wang2024characterizethegrowth pages 22-23): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

4. (llorente2024novelelectrochemicalstrategies pages 1-2): María Llorente, Sara Tejedor‐Sanz, Antonio Berná, Carlos Manchón, and Abraham Esteve‐Núñez. Novel electrochemical strategies for the microbial conversion of co2 into biomass and volatile fatty acids using a fluid‐like bed electrode in a three‐phase reactor. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14383, doi:10.1111/1751-7915.14383. This article has 17 citations and is from a peer-reviewed journal.

5. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

6. (laufermeiser2024oxidationofsulfur pages 6-8): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

7. (laufermeiser2024oxidationofsulfur pages 1-2): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.