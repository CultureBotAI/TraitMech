---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:45:41.906608'
end_time: '2026-08-04T11:54:07.265167'
duration_seconds: 505.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photoheterotrophic
  trait_identifier: METPO:1000657
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses light as the energy source
    and organic compounds as the primary carbon source for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: photoheterotroph, photoheterotrophy
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: light and reduced organic
    compounds (Encyclopedia chapter defines photoheterotrophy by light energy and
    reduced organic carbon.) | DOI:10.1128/AEM.01747-12: accumulated 25% to 110% more
    biomass (Experimental AAP study supports light-enhanced assimilation of supplied
    organic carbon.)'
  causal_graph_summary: 'photoheterotrophic_light_organic_carbon: 16 nodes, 14 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000657
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoheterotroph, photoheterotrophy
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: light and reduced organic compounds (Encyclopedia chapter defines photoheterotrophy by light energy and reduced organic carbon.) | DOI:10.1128/AEM.01747-12: accumulated 25% to 110% more biomass (Experimental AAP study supports light-enhanced assimilation of supplied organic carbon.)
- **Existing causal graph summary:** photoheterotrophic_light_organic_carbon: 16 nodes, 14 edges

## Research Objective

Research the microbial trait **photoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoheterotrophic.yaml`.

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
- **Trait label:** photoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000657
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoheterotroph, photoheterotrophy
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: light and reduced organic compounds (Encyclopedia chapter defines photoheterotrophy by light energy and reduced organic carbon.) | DOI:10.1128/AEM.01747-12: accumulated 25% to 110% more biomass (Experimental AAP study supports light-enhanced assimilation of supplied organic carbon.)
- **Existing causal graph summary:** photoheterotrophic_light_organic_carbon: 16 nodes, 14 edges

## Research Objective

Research the microbial trait **photoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoheterotrophic.yaml`.

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


# Curation report: microbial photoheterotrophy

## 1. Scope summary

**Target term:** `METPO:1000657` — **photoheterotrophic**  
**Category:** PHYSIOLOGY | **Kind:** CLASS | **Status:** REVIEWED  
**Parent:** `METPO:1000631`

The trait denotes a trophic state in which **light supplies energy while organic compounds supply the primary carbon used for biosynthesis**. It is therefore a physiological capacity or realized growth mode, not merely the presence of a phototrophy gene. Two mechanistically distinct implementations should be represented beneath the same trait:

1. **Pigment–reaction-center photoheterotrophy:** bacteriochlorophyll-containing reaction centers drive photophosphorylation while organic substrates provide carbon. Aerobic anoxygenic phototrophs (AAPs) are a major example; they generate ATP with bacteriochlorophyll-*a* reaction centers but rely principally on dissolved organic matter. (villenaalemany2024phenologyandecological pages 1-2, stojan2024ecologyofaerobic pages 1-2)
2. **Rhodopsin photoheterotrophy:** retinal-bound microbial rhodopsins use light to pump ions—usually protons—creating proton motive force (PMF) that can support ATP synthesis, transport, maintenance, or survival while organic substrates provide cellular carbon. (tu2023engineeringartificialphotosynthesis pages 1-2, johnson2010enhancementofsurvival pages 1-2)

### Boundary cases

- **Not photoautotrophy:** CO₂ is not the primary biosynthetic carbon source. *Rhodospirillum rubrum*, for example, uses light and organic acetate or malate under photoheterotrophic conditions, but it can switch to other trophic modes. (hernandezherreros2024boostinghydrogenproduction pages 1-3)
- **Not chemoheterotrophy:** growth on organic carbon in darkness does not establish photoheterotrophy; a reproducible light-dependent energetic or physiological contribution is required.
- **Not equivalent to anoxygenic phototrophy:** anoxygenic phototrophs can be photoautotrophic or photoheterotrophic. Purple non-sulfur bacteria can also switch among photoautotrophy, photoheterotrophy, chemolithoautotrophy, and chemoorganotrophy. (dhar2023anoxygenicphototrophicpurple pages 1-3)
- **Not equivalent to aerobic anoxygenic phototrophy:** AAP is an important taxon-independent ecological implementation, but anaerobic purple non-sulfur bacteria and rhodopsin-bearing heterotrophs also qualify.
- **Gene presence is insufficient:** `pufM` DNA indicates reaction-center potential, not expression or phenotype; DNA- and RNA-based community profiles can differ substantially. (villenaalemany2025lineagespecificphototrophyand pages 4-7, villenaalemany2025particleattachmentdrives pages 11-15)
- **Light-enhanced survival alone is borderline:** it supports photoheterotrophic energy capture, but should establish the full trait only when organic-carbon assimilation or heterotrophic growth is also demonstrated.
- **Artificial rhodopsin-driven CO₂ fixation is not this trait:** engineered *Cupriavidus necator* couples rhodopsin PMF to extracellular electrons and autotrophic carbon fixation; it is an application of the energetic module, not natural photoheterotrophy as defined here. (tu2023engineeringartificialphotosynthesis pages 1-2)

## 2. Recommended graph architecture

The existing graph should retain a common upstream/downstream spine but branch by energy-capture system:

- **Common:** light + organic carbon availability → light-energy capture and organic-substrate uptake → ATP/transport/redox effects → increased heterotrophic assimilation, biomass yield, or maintenance → `METPO:1000657`.
- **Branch A:** bacteriochlorophyll-*a* → type-II reaction center (`pufL/pufM`) → photosynthetic electron transport → PMF → ATP synthase.
- **Branch B:** retinal + proteorhodopsin → outward proton transport → PMF → ATP synthase and PMF-coupled transport.

| mechanism branch | subject | predicate | object | evidence strength | key taxon/context |
|---|---|---|---|---|---|
| BChl reaction-center | light | activates | bacteriochlorophyll-a-containing reaction center | strong | Aerobic anoxygenic phototrophs (AAP), marine/freshwater bacterioplankton (villenaalemany2024phenologyandecological pages 1-2, stojan2024ecologyofaerobic pages 1-2) |
| BChl reaction-center | bacteriochlorophyll-a reaction center photophosphorylation | generates | ATP | strong | AAP physiology; facultative photoheterotrophy in surface waters (stojan2024ecologyofaerobic pages 1-2) |
| BChl reaction-center | dissolved organic matter / organic compounds | supplies primary carbon and major energy source for | AAP growth and biosynthesis | strong | AAPs primarily rely on DOM while light supplements metabolism (villenaalemany2024phenologyandecological pages 1-2, stojan2024ecologyofaerobic pages 1-2) |
| BChl reaction-center | pufM | encodes | M subunit of anoxygenic type-II reaction center | strong | Standard AAP marker gene in community studies (villenaalemany2025particleattachmentdrives pages 1-4, stojan2024ecologyofaerobic pages 1-2) |
| BChl reaction-center | pufM presence | is marker for | phototrophy potential, not phenotype proof | moderate | DNA libraries can differ from RNA/activity; presence alone does not prove active photoheterotrophy (villenaalemany2025lineagespecificphototrophyand pages 4-7, villenaalemany2025particleattachmentdrives pages 11-15) |
| Rhodopsin | light | activates | retinal-bound proteorhodopsin | strong | Recombinant and native rhodopsin systems (johnson2010enhancementofsurvival pages 1-2, tu2023engineeringartificialphotosynthesis pages 1-2) |
| Rhodopsin | proteorhodopsin | pumps protons / generates | proton motive force | strong | Shewanella oneidensis recombinant system; engineered/artificial rhodopsin systems (johnson2010enhancementofsurvival pages 1-2, tu2023engineeringartificialphotosynthesis pages 1-2) |
| Rhodopsin | proton motive force | drives | ATP synthase / ATP synthesis | strong | Heterologous PR evidence and rhodopsin-powered systems (johnson2010enhancementofsurvival pages 1-2, tu2023engineeringartificialphotosynthesis pages 1-2, oh2024effectoflight pages 1-2) |
| Rhodopsin | light-activated proteorhodopsin | increases | lactate uptake / consumption rate | moderate | Engineered Shewanella oneidensis MR-1 under illumination (johnson2010enhancementofsurvival pages 1-2) |
| Rhodopsin | proteorhodopsin expression under light | preserves | viability under nutrient-limited conditions | moderate | Engineered Shewanella oneidensis MR-1 starvation context (johnson2010enhancementofsurvival pages 1-2) |
| Rhodopsin | nutrient-replete organic-carbon context | enables / strengthens | measurable PR photoheterotrophy | moderate | Candidatus Puniceispirillum marinum IMCC1322; high inoculum, amino-acid-rich conditions (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14) |
| Rhodopsin | nutrient limitation / proton stress context | constrains | anabolic benefit of PR-driven ATP synthesis | moderate | IMCC1322: light-driven ATP detected but insufficient for strong growth/anabolism in poor conditions (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14) |


*Table: This table summarizes the strongest curation-ready causal edges for microbial photoheterotrophy across bacteriochlorophyll reaction-center and proteorhodopsin branches. It is useful as a compact seed set for TraitMech graph construction, while keeping context-dependent claims separated from broadly supported ones.*

## 3. Candidate nodes grouped by type

Identifiers below are restricted to well-established CURIEs; uncertain molecular records are left label-only rather than guessed.

### A. Trait and biological-process nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| photoheterotrophic | `METPO:1000657` | Target phenotype. |
| photosynthesis, light reaction | `GO:0019684` | Broad process; use only if compatible with TraitMech granularity. |
| photophosphorylation | `GO:0009767` | Strong candidate for bacteriochlorophyll reaction-center branch. |
| proton transmembrane transport | `GO:1902600` | Rhodopsin and respiratory/photosynthetic proton movement. |
| ATP synthesis coupled proton transport | `GO:0015986` | PMF-to-ATP edge. |
| generation of precursor metabolites and energy | `GO:0006091` | Broad energetic endpoint. |
| organic-substrate assimilation | Label only | Carbon-source-specific child processes may be added per organism/assay. |
| dissolved organic matter recycling | Label only | Ecological consequence, not a constitutive intracellular mechanism. |
| biomass accumulation | Label only | Assay-observed phenotype. |
| starvation survival/maintenance | Label only | Context-dependent rhodopsin outcome. |

### B. Genes, proteins, enzymes, and complexes

| Candidate node | Suggested grounding | Role/qualification |
|---|---|---|
| `pufM` | Gene symbol; label-only unless taxon-specific accession is supplied | Encodes M subunit of anoxygenic type-II reaction center; widely used AAP marker. (villenaalemany2025particleattachmentdrives pages 1-4, stojan2024ecologyofaerobic pages 1-2) |
| `pufL` | Gene symbol; label-only | L reaction-center subunit; should normally accompany `pufM` mechanistically. |
| photosynthetic reaction center L/M complex | `GO:0030089` may be considered after ontology verification | Photochemical charge separation/electron transfer. |
| proteorhodopsin | Label-only or taxon-specific UniProt | Light-driven bacterial proton pump; do not use a single protein accession across taxa. |
| Gloeobacter rhodopsin | Label-only/taxon-specific UniProt | Demonstrated synthetic-biology proton-pump module. (tu2023engineeringartificialphotosynthesis pages 1-2) |
| retinal biosynthesis enzymes | `crtE`, `crtB`, `crtI`, `blh` as label-only gene nodes | Required in many rhodopsin systems to supply chromophore; genomic presence alone is not phenotype proof. |
| F-type H⁺-transporting ATP synthase | `GO:0000276`; taxon-specific subunits/EC records as appropriate | Converts PMF into ATP. |
| quinone pool | Label-only or individual ChEBI quinone | Electron carrier in type-II reaction-center cyclic electron transport. |
| cytochrome *bc* complex | `GO:0005750` is mitochondrial and unsuitable for bacteria; use label-only bacterial complex | Avoid inappropriate eukaryotic localization identifiers. |
| PpsR | Gene/protein label-only | Redox/oxygen-responsive photopigment transcriptional repressor in some purple bacteria; taxon-specific. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |
| HP1/PpaA-family regulator (`Rru_A0625`) | Label-only | *R. rubrum*-specific candidate linking light/redox signals to photosynthetic-gene regulation. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |
| carbon monoxide dehydrogenase, CooF, CooH | EC/taxon-specific records after strain-level verification | Application-specific WGSR branch, not core photoheterotrophy. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |

### C. Chemicals, donors, acceptors, nutrients, and metabolites

| Candidate node | Suggested grounding | Role |
|---|---|---|
| photon/light | `CHEBI:30212` for photon | Environmental energy input. |
| organic compound / organic carbon | Label-only broad node | Primary carbon source in the trait definition. Prefer measured substrates as children. |
| dissolved organic matter | `ENVO:01000155` if verified in local ontology release | Ecological substrate pool for AAPs. |
| acetate | `CHEBI:30089` | Demonstrated organic co-substrate in *R. rubrum* photoheterotrophic syngas experiments. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |
| lactate | `CHEBI:24996` | PR illumination increased consumption in engineered *S. oneidensis*. (johnson2010enhancementofsurvival pages 1-2) |
| malate | `CHEBI:30797` | Example organic carbon source for *R. rubrum*. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |
| retinal | `CHEBI:15035` | Rhodopsin chromophore; light-induced isomerization initiates pumping. (johnson2010enhancementofsurvival pages 1-2) |
| proton | `CHEBI:15378` | Transported ion and PMF component. |
| ATP | `CHEBI:15422` | Conserved energetic product. |
| ADP | `CHEBI:16761` | ATP-synthase substrate. |
| phosphate | `CHEBI:18367` | ATP-synthase substrate; protonation state should be normalized by project policy. |
| oxygen | `CHEBI:15379` | Environmental regulator/boundary factor; AAPs operate aerobically whereas many PNSB photoheterotrophic assays are anaerobic. |
| carbon monoxide | `CHEBI:17245` | Syngas energy/electron substrate; not the defining organic biosynthetic carbon source. |
| carbon dioxide | `CHEBI:16526` | Product of CO oxidation or autotrophic carbon source; distinguish from organic-carbon assimilation. |
| hydrogen | `CHEBI:18276` | Product/substrate in application branches. |
| bacteriochlorophyll *a* | ChEBI identifier should be verified before insertion | Light-harvesting/reaction-center pigment. Do not guess the CURIE. |
| NADH/NADPH | `CHEBI:16908` / `CHEBI:16474` | Reducing equivalents; rhodopsin alone does not directly generate reductant. (oh2024effectoflight pages 13-14, tu2023engineeringartificialphotosynthesis pages 1-2) |

### D. Environmental and experimental factors

- Light availability, intensity, wavelength, and light–dark regime.
- Organic-carbon identity and concentration.
- Dissolved oxygen/redox condition.
- Nutrient-replete versus nutrient-limited medium.
- Cell density/inoculum size.
- Amino-acid pool.
- Particle-attached versus free-living lifestyle.
- Growth phase.
- Temperature, salinity, inorganic nutrients, and chlorophyll-*a* as ecological covariates rather than universal causal determinants. A 2024 Adriatic study connected AAP community composition to these factors but did not establish each as a direct molecular cause. (stojan2024ecologyofaerobic pages 1-2)

### E. Cellular locations

- Cytoplasmic membrane.
- Periplasm/extracellular side of the bacterial membrane.
- Cytoplasm.
- Intracytoplasmic photosynthetic membrane in relevant purple bacteria.
- Photosynthetic reaction center embedded in membrane.

## 4. Candidate evidence-backed causal edges

Predicates are deliberately simple and YAML-friendly. “Strong” means suitable for a core graph; “conditional” requires taxon/assay qualifiers; “inferred” should remain outside the core until directly tested.

| # | Subject–predicate–object | Reference | Supporting snippet | Evidence and curation note |
|---:|---|---|---|---|
| 1 | light **provides energy for** `METPO:1000657` | Hernández-Herreros et al. 2024, DOI: [10.1016/j.biortech.2024.130972](https://doi.org/10.1016/j.biortech.2024.130972) | “Under photoheterotrophic conditions, *R. rubrum* harnesses energy from light and acquires carbon from organic compounds” | **Strong definition-level edge**, although stated in an introduction. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |
| 2 | organic compounds **provide primary carbon for** `METPO:1000657` | Same | “acquires carbon from organic compounds, e.g. acetate or malate” | **Strong**, with direct named substrate examples. (hernandezherreros2024boostinghydrogenproduction pages 1-3) |
| 3 | AAP bacteria **rely primarily on** dissolved organic matter | Stojan et al. 2024, DOI: [10.1186/s40793-024-00573-6](https://doi.org/10.1186/s40793-024-00573-6) | “they primarily rely on dissolved organic matter as an energy source” | **Strong for AAP ecology**, but organic matter supplies both carbon and chemical energy; light supplements the energy budget. (stojan2024ecologyofaerobic pages 1-2) |
| 4 | bacteriochlorophyll-*a* reaction center **harvests** light energy | Villena-Alemany et al. 2024, DOI: [10.1186/s40168-024-01786-0](https://doi.org/10.1186/s40168-024-01786-0) | AAPs “use bacteriochlorophyll-a to harvest light energy” | **Strong AAP branch**. (villenaalemany2024phenologyandecological pages 1-2) |
| 5 | reaction-center photophosphorylation **generates** ATP | Stojan et al. 2024 | AAPs “generate ATP by photophosphorylation using a unique type of bacteriochlorophyll-a-containing reaction center” | **Strong**, source-backed mechanistic summary. (stojan2024ecologyofaerobic pages 1-2) |
| 6 | `pufM` **encodes subunit of** anoxygenic type-II reaction center | Villena-Alemany et al. 2025 preprint, DOI: [10.1101/2025.04.22.649935](https://doi.org/10.1101/2025.04.22.649935) | “pufM gene (encoding the M subunit of the anoxygenic type-II reaction center)” | Mechanistically **strong**, but the retrieved explicit wording is from a 2025 preprint; verify against a primary molecular source before core insertion. (villenaalemany2025particleattachmentdrives pages 1-4) |
| 7 | `pufM` detection **indicates potential for** AAP phototrophy | Villena-Alemany et al. 2024 | “amplicon sequencing of the pufM marker gene”; database contained “3633 reference sequences” | **Assay edge only**. Do not encode `pufM presence → photoheterotrophic phenotype`. (villenaalemany2024phenologyandecological pages 1-2) |
| 8 | retinal photoisomerization **activates** proteorhodopsin ion transport | Johnson et al. 2010, DOI: [10.1128/AEM.02425-09](https://doi.org/10.1128/AEM.02425-09) | PRs “use the light-induced isomerization of retinal … to catalyze the transfer of ions across cell membranes” | **Strong mechanistic edge**. (johnson2010enhancementofsurvival pages 1-2) |
| 9 | proteorhodopsin **generates** membrane potential/PMF | Johnson et al. 2010 | “light-induced changes in membrane potential”; lactate uptake was consistent with PR “increasing the proton motive force” | **Strong for membrane potential; conditional for inferred PMF-mediated uptake**. (johnson2010enhancementofsurvival pages 1-2) |
| 10 | rhodopsin-generated PMF **drives** ATP synthesis | Tu et al. 2023, DOI: [10.1038/s41467-023-43524-4](https://doi.org/10.1038/s41467-023-43524-4) | “The light-activated proton pump … powers ATP synthesis” | **Strong energetic module**, demonstrated in an engineered system. (tu2023engineeringartificialphotosynthesis pages 1-2) |
| 11 | proteorhodopsin-generated membrane potential **drives** ATP synthesis | Johnson et al. 2010 | “membrane potential generated by light-driven proton pumping by PR has been confirmed to drive ATP synthesis” | **Strong supporting mechanism**, although this sentence summarizes earlier heterologous evidence. (johnson2010enhancementofsurvival pages 1-2) |
| 12 | illuminated proteorhodopsin **increases** lactate consumption | Johnson et al. 2010 | engineered strain “consume[d] lactate at an increased rate when it is illuminated” | **Conditional/direct experiment:** engineered *S. oneidensis* MR-1; do not generalize to all substrates or taxa. (johnson2010enhancementofsurvival pages 1-2) |
| 13 | illuminated proteorhodopsin **preserves** viability during nutrient limitation | Johnson et al. 2010 | “Expression of proteorhodopsin also preserved the viability … under nutrient-limited conditions” | **Conditional/direct experiment**, maintenance phenotype rather than growth. (johnson2010enhancementofsurvival pages 1-2) |
| 14 | nutrient-replete conditions and high cell density **enable observable** PR photoheterotrophy | Oh et al. 2024, DOI: [10.4014/jmb.2410.10034](https://doi.org/10.4014/jmb.2410.10034) | “Photoheterotrophy was observed only in nutrient-replete cultures with higher inoculum densities” | **Taxon- and assay-specific:** *Ca. Puniceispirillum marinum* IMCC1322. (oh2024effectoflight pages 1-2) |
| 15 | light regime **alters** cellular ATP in PR-bearing IMCC1322 | Oh et al. 2024 | ATP was “0.0331–1.74 mM,” or “13.9–367 zeptomoles per cell,” in stationary/death phases | **Direct quantitative evidence**, but strongly phase- and nutrient-dependent. (oh2024effectoflight pages 1-2) |
| 16 | PR-driven PMF **does not directly produce** NADPH | Oh et al. 2024 | “PR generates proton motive force (PMF) but cannot produce NADPH for anabolic metabolism” | **Important negative/constraint edge**; prevents over-modeling rhodopsin as a complete photosynthetic ETC. (oh2024effectoflight pages 13-14) |
| 17 | light-driven PR ATP **is insufficient for** protein turnover under nutrient limitation | Oh et al. 2024 | “insufficient to support protein turnover after the log phase, as well as in nutrient-limited conditions” | **Conditional negative edge** for IMCC1322. (oh2024effectoflight pages 1-2) |
| 18 | phytoplankton bloom-derived DOM **supports** spring AAP peak/DOM recycling | Villena-Alemany et al. 2024 | spring maximum followed the phytoplankton bloom; AAPs recycle DOM released during it | **Ecological association plus model-supported interpretation**, not a universal intracellular edge. (villenaalemany2024phenologyandecological pages 1-2, villenaalemany2024phenologyandecological pages 11-12) |
| 19 | light-supported AAP metabolism **increases** secondary production/carbon transfer | Villena-Alemany et al. 2024 | AAPs show “efficient photoheterotrophic metabolism, increasing secondary bacterial production and carbon transfer” | **Ecological consequence**, suitable as a downstream ecosystem edge with an inference qualifier. (villenaalemany2024phenologyandecological pages 9-11) |
| 20 | particle attachment **modulates** phototrophy-gene expression | Villena-Alemany et al. 2025 preprint | expression was regulated by “particle attachment status in addition to carbon availability and light” | **Uncertain/preprint and lifestyle-specific**; hold outside the reviewed core. (villenaalemany2025particleattachmentdrives pages 8-11, villenaalemany2025particleattachmentdrives pages 11-15) |

### Minimal curation-ready core

The most defensible core is:

1. photon → activates → bacteriochlorophyll-*a* reaction center;
2. bacteriochlorophyll reaction center → drives → photophosphorylation;
3. photophosphorylation → produces → ATP;
4. organic compound → supplies carbon for → biomass biosynthesis;
5. photon → activates → retinal-bound proteorhodopsin;
6. proteorhodopsin → transports → proton across cytoplasmic membrane;
7. proton transport → generates → PMF;
8. PMF → drives → ATP synthase;
9. ATP synthesis + organic-substrate assimilation → supports → photoheterotrophic growth/maintenance;
10. active light-dependent organic-carbon phenotype → realizes → `METPO:1000657`.

The two energy-capture branches should be alternatives, not mandatory co-requirements.

## 5. Recent research, statistics, and expert interpretation

### 2024 ecology

A three-year freshwater study found a recurrent **spring maximum after phytoplankton bloom** and a secondary autumn maximum; fewer than **2% of detected AAP species occurred throughout the year**. Its new `pufM` primers produced approximately **450-bp amplicons**, and the reference database contained **3,633 sequences**. The authors interpret AAPs as important recyclers of bloom-derived dissolved organic matter. (villenaalemany2024phenologyandecological pages 1-2)

An Adriatic Sea survey measured maximum average AAP abundance of **2.136 ± 0.081 × 10⁴ cells mL⁻¹ in spring**, versus **0.86 × 10⁴ cells mL⁻¹ in summer**. FISH-IR assignments averaged 37.66% Roseobacter-clade, 35.25% Gammaproteobacteria, and 31.15% general Alphaproteobacteria; these probe categories should not be summed because they are not necessarily mutually exclusive. Historical estimates reached **11% of the upper-ocean microbial community**, while event-associated Adriatic piconeuston observations reached **30% of bacteria**. (stojan2024ecologyofaerobic pages 1-2)

These studies support the expert view that photoheterotrophy changes carbon-transfer efficiency rather than converting heterotrophs into primary producers: light offsets part of the energetic cost of processing organic matter, potentially reducing respiratory carbon loss and increasing transfer into microbial biomass. However, ecosystem-scale CO₂ effects remain model- and context-dependent. (villenaalemany2024phenologyandecological pages 1-2, villenaalemany2024phenologyandecological pages 9-11)

### 2024 proteorhodopsin physiology

The IMCC1322 work sharply qualifies the common assumption that light-driven PMF automatically increases growth. Measured ATP varied from **0.0331 to 1.74 mM** and **13.9 to 367 zmol cell⁻¹**, but benefit depended on nutrient supply, inoculum, and growth phase; PR energy was inadequate for sustained protein turnover during nutrient limitation, and light did not significantly enhance inorganic-carbon assimilation in late log phase. (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14)

Thus, the best current interpretation is that rhodopsin photoheterotrophy is often an **energetic supplement** whose observable endpoint may be ATP maintenance, solute transport, stress tolerance, or modest growth enhancement—not a universal increase in biomass.

## 6. Current applications and implementations

### Wastewater treatment and resource recovery

Purple non-sulfur bacteria are being developed for wastewater treatment, biohydrogen, and recovery of polyhydroxyalkanoates, single-cell protein, carotenoids, and 5-aminolevulinic acid. A 2023 review describes PNSB treatment as potentially sustainable and cost-effective but notes that pollutant-specific mechanisms and scale-up remain incomplete. (dhar2023anoxygenicphototrophicpurple pages 1-3)

### Bioremediation

*Rhodobacter sphaeroides* and *Rhodopseudomonas palustris* strains have been reported to remediate arsenic, cadmium, chromium, and lead and to use lignocellulosic compounds and some xenobiotics. The authoritative 2023 review explicitly warns that evidence for degradation of many toxic organic pollutants remains limited; these application claims should not become core trait edges. (dhar2023anoxygenicphototrophicpurple pages 1-3)

### Photofermentative hydrogen and syngas valorization

A 2024 *R. rubrum* study used anaerobic light, acetate, and syngas containing **40% CO, 40% H₂, 10% CO₂, and 10% N₂** at 1.5 bar. The study applied approximately **200 generations** of adaptive evolution. In this system, H₂ can arise through photofermentation of organic compounds or through the water–gas shift route involving CO dehydrogenase, CooF, and CooH. These are application-specific extensions, not universal photoheterotrophy mechanisms. (hernandezherreros2024boostinghydrogenproduction pages 1-3)

### Engineered rhodopsin bioenergetics

In 2023, engineered *C. necator* combined Gloeobacter rhodopsin, canthaxanthin, and the *Shewanella* MtrCAB extracellular-electron conduit. Rhodopsin-generated PMF powered ATP synthesis and reverse electron transport for NADH/NADPH regeneration, enabling photoelectrosynthetic CO₂ fixation. This demonstrates portability of the rhodopsin→PMF→ATP module, but the complete engineered phenotype is photoelectroautotrophic and should not be asserted as evidence for organic-carbon-based `METPO:1000657`. (tu2023engineeringartificialphotosynthesis pages 1-2)

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not curate `pufM present → photoheterotrophic`.** Require expression, pigment/reaction-center activity, or a light-versus-dark physiological assay. (villenaalemany2025lineagespecificphototrophyand pages 4-7, villenaalemany2025particleattachmentdrives pages 11-15)
2. **Do not require `pufM` for all photoheterotrophs.** It excludes type-I reaction centers and rhodopsin systems.
3. **Do not encode oxygen as universally required or inhibitory.** AAPs are aerobic; many PNSB photoheterotrophic assays are anaerobic or microaerobic.
4. **Do not encode PR as producing NADPH directly.** PR primarily creates an electrochemical gradient; reductant regeneration requires an electron source and coupled ETC. (oh2024effectoflight pages 13-14, tu2023engineeringartificialphotosynthesis pages 1-2)
5. **Do not generalize light-enhanced lactate uptake or starvation survival across taxa.** Those direct data come from engineered *S. oneidensis*. (johnson2010enhancementofsurvival pages 1-2)
6. **Do not generalize IMCC1322 nutrient dependence to all PR organisms.** It is strain-, density-, phase-, and medium-specific. (oh2024effectoflight pages 1-2)
7. **Do not curate community correlations as molecular causation.** Temperature, nutrients, salinity, phytoplankton, and predators correlate with AAP abundance but are not each demonstrated direct causes. (stojan2024ecologyofaerobic pages 1-2)
8. **Hold particle-attachment regulation as uncertain.** The clearest retrieved evidence is a 2025 preprint. (villenaalemany2025particleattachmentdrives pages 8-11)
9. **Keep biotechnology outputs outside the core trait graph.** H₂, PHA, pollutant removal, electricity, and CO₂ fixation require organism- and process-specific modules.
10. **Verify ontology releases before committing uncertain CURIEs**, especially bacteriochlorophyll-*a*, bacterial reaction-center complexes, bacterial cytochrome *bc* complexes, DOM, and taxon-specific proteins.
11. The supplied **25–110% additional-biomass** result from DOI:10.1128/AEM.01747-12 is consistent with the literature summary, but the full text was not retrieved here; retain the existing evidence record rather than adding more detailed edges without checking the original experiment.

## 8. DOI-first bibliography

1. **Villena-Alemany C, et al.** “Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters.” *Microbiome* 12 (published March 2024). DOI: [10.1186/s40168-024-01786-0](https://doi.org/10.1186/s40168-024-01786-0). (villenaalemany2024phenologyandecological pages 1-2, villenaalemany2024phenologyandecological pages 9-11, villenaalemany2024phenologyandecological pages 11-12)
2. **Stojan I, et al.** “Ecology of aerobic anoxygenic phototrophs on a fine-scale taxonomic resolution in Adriatic Sea unravelled by unsupervised neural network.” *Environmental Microbiome* 19:28 (published April 2024). DOI: [10.1186/s40793-024-00573-6](https://doi.org/10.1186/s40793-024-00573-6). (stojan2024ecologyofaerobic pages 1-2)
3. **Oh H-M, et al.** “Effect of Light Regime on *Candidatus Puniceispirillum marinum* IMCC1322 in Nutrient-Replete Conditions.” *Journal of Microbiology and Biotechnology* (published November 2024). DOI: [10.4014/jmb.2410.10034](https://doi.org/10.4014/jmb.2410.10034). (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14)
4. **Hernández-Herreros N, et al.** “Boosting hydrogen production in *Rhodospirillum rubrum* by syngas-driven photoheterotrophic adaptive evolution.” *Bioresource Technology* 406:130972 (published August 2024). DOI: [10.1016/j.biortech.2024.130972](https://doi.org/10.1016/j.biortech.2024.130972). (hernandezherreros2024boostinghydrogenproduction pages 1-3)
5. **Tu W, et al.** “Engineering artificial photosynthesis based on rhodopsin for CO₂ fixation.” *Nature Communications* 14:8012 (accepted 11 November; published December 2023). DOI: [10.1038/s41467-023-43524-4](https://doi.org/10.1038/s41467-023-43524-4). (tu2023engineeringartificialphotosynthesis pages 1-2)
6. **Dhar K, Venkateswarlu K, Megharaj M.** “Anoxygenic phototrophic purple non-sulfur bacteria: tool for bioremediation of hazardous environmental pollutants.” *World Journal of Microbiology and Biotechnology* 39:283 (published online 18 August 2023). DOI: [10.1007/s11274-023-03729-7](https://doi.org/10.1007/s11274-023-03729-7). (dhar2023anoxygenicphototrophicpurple pages 1-3)
7. **Hauruseu D, Koblížek M.** “Influence of light on carbon utilization in aerobic anoxygenic phototrophs.” *Applied and Environmental Microbiology* 78:7414–7419 (October 2012). DOI: [10.1128/AEM.01747-12](https://doi.org/10.1128/AEM.01747-12). Existing supplied evidence reports 25–110% more biomass in light.
8. **Johnson ET, et al.** “Enhancement of Survival and Electricity Production in an Engineered Bacterium by Light-Driven Proton Pumping.” *Applied and Environmental Microbiology* 76:4123–4129 (published online 7 May; issue July 2010). DOI: [10.1128/AEM.02425-09](https://doi.org/10.1128/AEM.02425-09). (johnson2010enhancementofsurvival pages 1-2)
9. **Villena-Alemany C, et al.** “Particle attachment drives seasonal abundance and photoheterotrophy of marine aerobic anoxygenic phototrophs.” *bioRxiv* (April 2025; **preprint**). DOI: [10.1101/2025.04.22.649935](https://doi.org/10.1101/2025.04.22.649935). Use only for provisional edges. (villenaalemany2025particleattachmentdrives pages 11-15, villenaalemany2025particleattachmentdrives pages 8-11, villenaalemany2025particleattachmentdrives pages 1-4)

References

1. (villenaalemany2024phenologyandecological pages 1-2): Cristian Villena-Alemany, Izabela Mujakić, Livia K. Fecskeová, Jason Woodhouse, Adrià Auladell, Jason Dean, Martina Hanusová, Magdalena Socha, Carlota R. Gazulla, Hans-Joachim Ruscheweyh, Shinichi Sunagawa, Vinicius Silva Kavagutti, Adrian-Ştefan Andrei, Hans-Peter Grossart, Rohit Ghai, Michal Koblížek, and Kasia Piwosz. Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters. Microbiome, Mar 2024. URL: https://doi.org/10.1186/s40168-024-01786-0, doi:10.1186/s40168-024-01786-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

2. (stojan2024ecologyofaerobic pages 1-2): Iva Stojan, Danijela Šantić, Cristian Villena-Alemany, Željka Trumbić, Frano Matić, Ana Vrdoljak Tomaš, Ivana Lepen Pleić, Kasia Piwosz, Grozdan Kušpilić, Živana Ninčević Gladan, Stefanija Šestanović, and Mladen Šolić. Ecology of aerobic anoxygenic phototrophs on a fine-scale taxonomic resolution in adriatic sea unravelled by unsupervised neural network. Environmental Microbiome, Apr 2024. URL: https://doi.org/10.1186/s40793-024-00573-6, doi:10.1186/s40793-024-00573-6. This article has 6 citations and is from a peer-reviewed journal.

3. (tu2023engineeringartificialphotosynthesis pages 1-2): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 76 citations and is from a highest quality peer-reviewed journal.

4. (johnson2010enhancementofsurvival pages 1-2): Ethan T. Johnson, Daniel B. Baron, Belén Naranjo, Daniel R. Bond, Claudia Schmidt-Dannert, and Jeffrey A. Gralnick. Enhancement of survival and electricity production in an engineered bacterium by light-driven proton pumping. Applied and Environmental Microbiology, 76:4123-4129, Jul 2010. URL: https://doi.org/10.1128/aem.02425-09, doi:10.1128/aem.02425-09. This article has 97 citations and is from a peer-reviewed journal.

5. (hernandezherreros2024boostinghydrogenproduction pages 1-3): Natalia Hernández-Herreros, Alberto Rodríguez, Beatriz Galán, and M. Auxiliadora Prieto. Boosting hydrogen production in rhodospirillum rubrum by syngas-driven photoheterotrophic adaptive evolution. Aug 2024. URL: https://doi.org/10.1016/j.biortech.2024.130972, doi:10.1016/j.biortech.2024.130972. This article has 11 citations and is from a domain leading peer-reviewed journal.

6. (dhar2023anoxygenicphototrophicpurple pages 1-3): Kartik Dhar, Kadiyala Venkateswarlu, and Mallavarapu Megharaj. Anoxygenic phototrophic purple non-sulfur bacteria: tool for bioremediation of hazardous environmental pollutants. World Journal of Microbiology & Biotechnology, Aug 2023. URL: https://doi.org/10.1007/s11274-023-03729-7, doi:10.1007/s11274-023-03729-7. This article has 62 citations and is from a peer-reviewed journal.

7. (villenaalemany2025lineagespecificphototrophyand pages 4-7): Cristian Villena-Alemany, Ana Vrdoljak Tomaš, Izabela Mujakić, Karel Kopejtka, Danijela Šantić, and Michal Koblížek. Lineage-specific phototrophy and lifestyle of coastal marine aerobic anoxygenic phototrophs. Ocean Microbiology, Sep 2025. URL: https://doi.org/10.1186/s44375-025-00005-x, doi:10.1186/s44375-025-00005-x. This article has 2 citations.

8. (villenaalemany2025particleattachmentdrives pages 11-15): Cristian Villena-Alemany, Ana Vrdoljak Tomaš, Izabela Mujakić, Karel Kopejtka, Danijela Šantić, and Michal Koblížek. Particle attachment drives seasonal abundance and photoheterotrophy of marine aerobic anoxygenic phototrophs. bioRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.22.649935, doi:10.1101/2025.04.22.649935. This article has 0 citations.

9. (villenaalemany2025particleattachmentdrives pages 1-4): Cristian Villena-Alemany, Ana Vrdoljak Tomaš, Izabela Mujakić, Karel Kopejtka, Danijela Šantić, and Michal Koblížek. Particle attachment drives seasonal abundance and photoheterotrophy of marine aerobic anoxygenic phototrophs. bioRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.22.649935, doi:10.1101/2025.04.22.649935. This article has 0 citations.

10. (oh2024effectoflight pages 1-2): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

11. (oh2024effectoflight pages 13-14): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

12. (villenaalemany2024phenologyandecological pages 11-12): Cristian Villena-Alemany, Izabela Mujakić, Livia K. Fecskeová, Jason Woodhouse, Adrià Auladell, Jason Dean, Martina Hanusová, Magdalena Socha, Carlota R. Gazulla, Hans-Joachim Ruscheweyh, Shinichi Sunagawa, Vinicius Silva Kavagutti, Adrian-Ştefan Andrei, Hans-Peter Grossart, Rohit Ghai, Michal Koblížek, and Kasia Piwosz. Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters. Microbiome, Mar 2024. URL: https://doi.org/10.1186/s40168-024-01786-0, doi:10.1186/s40168-024-01786-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

13. (villenaalemany2024phenologyandecological pages 9-11): Cristian Villena-Alemany, Izabela Mujakić, Livia K. Fecskeová, Jason Woodhouse, Adrià Auladell, Jason Dean, Martina Hanusová, Magdalena Socha, Carlota R. Gazulla, Hans-Joachim Ruscheweyh, Shinichi Sunagawa, Vinicius Silva Kavagutti, Adrian-Ştefan Andrei, Hans-Peter Grossart, Rohit Ghai, Michal Koblížek, and Kasia Piwosz. Phenology and ecological role of aerobic anoxygenic phototrophs in freshwaters. Microbiome, Mar 2024. URL: https://doi.org/10.1186/s40168-024-01786-0, doi:10.1186/s40168-024-01786-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

14. (villenaalemany2025particleattachmentdrives pages 8-11): Cristian Villena-Alemany, Ana Vrdoljak Tomaš, Izabela Mujakić, Karel Kopejtka, Danijela Šantić, and Michal Koblížek. Particle attachment drives seasonal abundance and photoheterotrophy of marine aerobic anoxygenic phototrophs. bioRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.22.649935, doi:10.1101/2025.04.22.649935. This article has 0 citations.