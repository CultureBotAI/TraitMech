---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:04:36.837660'
end_time: '2026-06-18T11:19:21.462949'
duration_seconds: 884.63
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoorganoheterotrophic
  trait_identifier: METPO:1000640
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoorganoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains both energy and carbon from
    organic compounds through oxidation.
  parent_traits: METPO:1000631
  synonyms: chemoorganoheterotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph)
    (Encyclopedia chapter maps chemical energy, reduced organic electron source, and
    reduced organic carbon source to chemoorganoheterotrophy.) | DOI:10.1021/acsomega.3c02205:
    chemoorganoheterotrophic (Review table supports organic molecules as energy, electron,
    and carbon sources in chemoorganoheterotrophy.)'
  causal_graph_summary: 'chemoorganoheterotrophic_organic_energy_carbon: 8 nodes,
    10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoorganoheterotrophic
- **METPO identifier:** METPO:1000640
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds through oxidation.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemical energy, reduced organic electron source, and reduced organic carbon source to chemoorganoheterotrophy.) | DOI:10.1021/acsomega.3c02205: chemoorganoheterotrophic (Review table supports organic molecules as energy, electron, and carbon sources in chemoorganoheterotrophy.)
- **Existing causal graph summary:** chemoorganoheterotrophic_organic_energy_carbon: 8 nodes, 10 edges

## Research Objective

Research the microbial trait **chemoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganoheterotrophic.yaml`.

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
- **Trait label:** chemoorganoheterotrophic
- **METPO identifier:** METPO:1000640
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds through oxidation.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemical energy, reduced organic electron source, and reduced organic carbon source to chemoorganoheterotrophy.) | DOI:10.1021/acsomega.3c02205: chemoorganoheterotrophic (Review table supports organic molecules as energy, electron, and carbon sources in chemoorganoheterotrophy.)
- **Existing causal graph summary:** chemoorganoheterotrophic_organic_energy_carbon: 8 nodes, 10 edges

## Research Objective

Research the microbial trait **chemoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganoheterotrophic.yaml`.

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


## Research report: Chemoorganoheterotrophic (METPO:1000640) TraitMech causal-graph curation

### 1) Scope summary (trait meaning, boundaries, and current understanding)

**Trait definition (curation target).** *Chemoorganoheterotrophic growth* is a trophic mode in which **organic molecules provide carbon, electrons, and energy**, typically via oxidation of the organic substrate(s). In a recent review of heterotrophy in cyanobacteria, the definition is stated explicitly: “**In the dark, organic molecules are used as a source of carbon, energy, and electrons, and this growth mode is called chemoorganoheterotrophic growth**” (10.1021/acsomega.3c02205; published Sep 2023) (stebegg2023heterotrophyamongcyanobacteria pages 1-2). 

**Distinguish from nearby traits / boundary cases.**
- **Photolithoautotrophy**: energy from light, electrons from water, carbon from CO2 (described for cyanobacteria as the typical mode) (stebegg2023heterotrophyamongcyanobacteria pages 1-2).
- **Photoheterotrophy / photoorganoheterotrophy** (light + organic electron source) and **photomixotrophy** (light-dependent growth stimulated by organics) are distinct; photomixotrophy is “**not a true form of heterotrophy**” because of retained light dependence (stebegg2023heterotrophyamongcyanobacteria pages 2-4). 
- **Light-activated heterotrophic growth (LAHG)** represents partial/light-dependent heterotrophy (e.g., requires brief illumination); this should be treated as a boundary mode rather than strict chemoorganoheterotrophy (stebegg2023heterotrophyamongcyanobacteria pages 2-2).
- **Chemolithotrophy / chemolithoautotrophy**: energy from oxidation of inorganic compounds (e.g., H2, sulfide, ammonia, Fe2+), rather than organic substrates (contrasted in a marine eco-energetics review) (dang2017ecologicalenergeticperspectives pages 1-2).

**Assay/annotation interpretation.** For curation, the trait should be interpreted as a **physiological capacity**: the organism can sustain metabolism and (often) growth by oxidizing organic substrates that simultaneously supply carbon and reducing equivalents, under conditions where energy is derived from chemical reactions (not light). Evidence often comes from growth experiments (dark growth on defined organics), respiration measurements, or genomic/metabolic reconstructions indicating uptake and catabolic potential (stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria pages 9-10, carini2013nutrientrequirementsfor pages 1-2).

### 2) Recent developments and latest research (prioritizing 2023–2024)

**(a) Mechanistic clarity in a 2023 synthesis (cyanobacteria as a boundary-rich case).** The 2023 ACS Omega review systematizes chemoorganoheterotrophic growth conditions across cyanobacteria and emphasizes mechanistic dependencies on transport and respiratory metabolism. It notes that imported organics must be metabolized “**for the synthesis of ATP and NAD(P)H**” (stebegg2023heterotrophyamongcyanobacteria pages 2-4), and provides substrate-specific distinctions (e.g., in some strains fructose supports dark growth whereas glucose may only support light-dependent growth modes) (stebegg2023heterotrophyamongcyanobacteria pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 10-11). A key mechanistic example is respiratory dependence: “**fructose-based dark growth is strictly dependent on an aa3-type cytochrome c oxidase**,” and deleting the *coxBAC1* locus prevents growth on fructose in the dark (stebegg2023heterotrophyamongcyanobacteria pages 10-11). These are strong mechanistic edges but taxon- and substrate-specific.

**(b) Quantifying energy use in chemoorganoheterotroph-dominated soils (2023).** A 2023 Global Change Biology synthesis frames soil microbial metabolism as largely chemoorganoheterotrophic, linking substrate thermodynamics (nominal oxidation state of carbon, NOSC) to energy yield and to emergent ecosystem parameters (EUE vs CUE). It explicitly connects heterotrophic microbes to oxidation of organic compounds and emphasizes that “**microorganisms use organic C mainly as an energy source**” (wang2023energyuseefficiency pages 1-2). The paper reports quantitative relationships useful for trait-context annotation: NOSC-energy content relationship (R2 = 0.98; 108 kJ mol−1 C per NOSC unit), microbial biomass NOSC ~ −0.52 with energy content ~ −510 kJ mol−1 C, and a mean microbial **EUE ~0.32–0.35** vs **CUE ~0.41** (glucose), with EUE ~15–22% lower than CUE (10.1111/gcb.16925; published Aug 2023) (wang2023energyuseefficiency pages 1-2, wang2023energyuseefficiency pages 14-15).

**(c) Community-scale organotrophy under extreme conditions (2024).** A 2024 Environmental Microbiome study uses metagenome-assembled genomes (MAGs) from hot spring biofilms and details carbohydrate degradation as a route to organotrophic energy and carbon acquisition: extracellular CAZymes hydrolyze polymers, and sugar transporters import monomers/oligosaccharides “**for energy and downstream metabolism**” (10.1186/s40793-024-00572-7; published May 2024) (liew2024integratingmultiplatformassembly pages 11-15). This supports upstream “substrate availability → transport → catabolism” nodes that can feed a chemoorganoheterotrophy graph, though many details are community- and habitat-specific.

**(d) Organic-substrate oxidation coupled to non-O2 electron acceptors (2024).** In an applied/environmental context (oil seep sediments), anaerobic oxidation of hydrocarbons is described with multiple possible terminal electron acceptors (HCO3−, sulfate, nitrate, Fe3+), supporting inclusion of alternative-respiration edges relevant to anaerobic chemoorganoheterotrophy (10.1134/S0026261724605608; published Sep 2024) (pavlova2024anaerobicoxidationof pages 1-2).

### 3) Current applications and real-world implementations

**Wastewater/sewer infrastructure microbiomes (corrosion as real-world system).** A highly cited review of concrete sewer corrosion ecosystems notes multi-functional acidophilic biofilms including chemoorganoheterotrophs, and that activity is influenced by **H2S**, **CO2**, **organic matter**, and **iron** (10.3389/fmicb.2017.00683; published Apr 2017) (li2017theecologyof pages 1-2). Within these communities, heterotrophs scavenge organics/EPS/debris produced by sulfur-oxidizing chemolithoautotrophs, produce CO2 available to autotrophs, and can remove inhibitory organic compounds that otherwise inhibit autotroph growth—illustrating how chemoorganoheterotrophic metabolism participates in engineered/urban systems (li2017theecologyof pages 11-12, li2017theecologyof pages 4-6).

**Bioprocessing on complex carbohydrates (extreme-environment enzyme discovery).** Hot spring biofilms provide a pipeline to discover thermostable carbohydrate-active enzymes (CAZymes) for biomass conversion; mechanistically, extracellular polymer hydrolysis and uptake/catabolism enable chemoorganoheterotrophic energy capture from plant litter, with potential translation to industrial enzyme and bioprocess applications (liew2024integratingmultiplatformassembly pages 11-15).

**Bioremediation / hydrocarbon degradation.** Environmental monitoring and enrichment of oil-contaminated sediments demonstrate measurable decreases in n-alkanes and PAHs over long incubations and connect organotrophic oxidation of hydrocarbons to available electron acceptors, informing remediation strategies in anoxic sediments (pavlova2024anaerobicoxidationof pages 1-2).

### 4) Candidate causal-graph entities (nodes) for curation

Below is a curation-oriented node inventory grouped by type, emphasizing nodes supported by the evidence above. Where exact ontology grounding is unclear, label-only nodes are provided.

#### 4.1 Pathways / modules (candidate nodes)
- Organic-substrate catabolism to ATP and reducing power (label-only; supports ATP/NAD(P)H generation) (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- Aerobic respiration / terminal oxidase activity (GO:0006119 and related; aa3-type cytochrome c oxidase as a mechanistic anchor in one system) (stebegg2023heterotrophyamongcyanobacteria pages 10-11)
- Alternative/anaerobic respiration using nitrate, sulfate, Fe(III), bicarbonate (terminal electron acceptors; environment-dependent) (pavlova2024anaerobicoxidationof pages 1-2)
- Polysaccharide depolymerization by extracellular CAZymes (label-only set of CAZymes; see below) (liew2024integratingmultiplatformassembly pages 11-15)

#### 4.2 Genes/proteins/complexes (candidate nodes)
- aa3-type cytochrome c oxidase (GO:0004129; cyanobacteria example) (stebegg2023heterotrophyamongcyanobacteria pages 10-11)
- *coxBAC1* locus (label-only; deletion phenotype for fructose dark growth) (stebegg2023heterotrophyamongcyanobacteria pages 10-11)
- Sugar transporters (GO:0005351 generalized; specific transporters are taxon-dependent) (stebegg2023heterotrophyamongcyanobacteria pages 2-4, liew2024integratingmultiplatformassembly pages 11-15)
- Carbohydrate-active enzymes (CAZymes; label-only: endoglucanase, exoglucanase, β-glucosidase, xylanase, mannanase) (liew2024integratingmultiplatformassembly pages 11-15)

#### 4.3 Chemicals / substrates / metabolites
- Organic molecules / organic carbon (CHEBI:50860) (stebegg2023heterotrophyamongcyanobacteria pages 1-2, wang2023energyuseefficiency pages 1-2)
- Representative sugars: glucose (CHEBI:17234), fructose (CHEBI:15824) (stebegg2023heterotrophyamongcyanobacteria pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 10-11)
- CO2 (CHEBI:16526) as a community-level product of heterotrophy (li2017theecologyof pages 11-12)
- Hydrocarbons / petroleum hydrocarbons (CHEBI:24632) (pavlova2024anaerobicoxidationof pages 1-2)

#### 4.4 Electron acceptors / environmental inputs
- O2 (CHEBI:15379) (implied in aerobic respiration dependence; also listed in terminal acceptors in symbioses) (stebegg2023heterotrophyamongcyanobacteria pages 10-11, sogin2021lifeinthe pages 9-11)
- Nitrate (CHEBI:17632), sulfate (CHEBI:16189), Fe(III) (CHEBI:29033), bicarbonate (CHEBI:17544) (pavlova2024anaerobicoxidationof pages 1-2)
- Environmental drivers: H2S (label-only; sewer corrosion driver), CO2 (CHEBI:16526), organic matter (label-only), iron (label-only) (li2017theecologyof pages 1-2, li2017theecologyof pages 7-8)

#### 4.5 Experimental/assay factors (boundary conditions)
- Dark conditions / prolonged darkness (label-only; critical in cyanobacteria definition) (stebegg2023heterotrophyamongcyanobacteria pages 1-2)
- Light-activated heterotrophic growth (LAHG; label-only boundary phenotype) (stebegg2023heterotrophyamongcyanobacteria pages 2-2)
- Substrate concentration effects (e.g., 50 mM fructose; 100 mM glucose impacts respiration) (stebegg2023heterotrophyamongcyanobacteria pages 9-10)

### 5) Evidence-backed causal edges (triples)

The following table compiles candidate edges with direct evidence and curation caveats.

| Edge (subject–predicate–object) | Suggested grounding (subject/object) | Evidence snippet (verbatim/near-verbatim) | Source (DOI, publication year, URL) | Curation notes/uncertainty |
|---|---|---|---|---|
| chemoorganoheterotrophic growth – uses as carbon source – organic molecules | METPO:1000640 / CHEBI:50860 | “In the dark, organic molecules are used as a source of carbon, energy, and electrons” (stebegg2023heterotrophyamongcyanobacteria pages 1-2) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Core defining edge; strong trait-level support. |
| chemoorganoheterotrophic growth – uses as electron source – organic molecules | METPO:1000640 / CHEBI:50860 | “In the dark, organic molecules are used as a source of carbon, energy, and electrons” (stebegg2023heterotrophyamongcyanobacteria pages 1-2) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Core defining edge; strong trait-level support. |
| chemoorganoheterotrophic growth – uses as energy source – organic molecules | METPO:1000640 / CHEBI:50860 | “In the dark, organic molecules are used as a source of carbon, energy, and electrons” (stebegg2023heterotrophyamongcyanobacteria pages 1-2) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Core defining edge; strong trait-level support. |
| imported organic substrate – is required for – ATP and NAD(P)H synthesis during heterotrophic growth | label-only / GO:0006091, CHEBI:15422 | “the entering molecule has to be metabolized in some way for the synthesis of ATP and NAD(P)H” (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | General mechanistic edge; from cyanobacterial review but broadly consistent with organotrophy. |
| substrate transport system – enables – chemoorganoheterotrophic growth on organics | GO:0005215 / METPO:1000640 | “heterotrophic growth requires import of appropriate organic substrates into the cell” (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Reasonable generic edge; exact transporter families are taxon/substrate specific. |
| aa3-type cytochrome c oxidase – required for – fructose-based dark chemoorganoheterotrophic growth | GO:0004129 / label-only fructose dark growth | “fructose-based dark growth is strictly dependent on an aa3-type cytochrome c oxidase” (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Taxon- and substrate-specific (cyanobacteria); mark uncertain for general trait graph. |
| coxBAC1 deletion – abolishes – growth on fructose in the dark | label-only coxBAC1 / label-only fructose dark growth | “Deletion of the coxBAC1 locus... results in a strain unable to grow on fructose in the dark” (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Strong mechanistic evidence, but highly taxon-specific; uncertain for general curation. |
| glucose supplementation – increases – dark respiration | CHEBI:17234 / GO:0006119 | “increased dark respiration... but an even stronger effect with 100 mM glucose” (stebegg2023heterotrophyamongcyanobacteria pages 9-10) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Cyanobacteria-specific observation; useful as assay/mechanism evidence, uncertain as universal edge. |
| fructose – supports – chemoorganoheterotrophic growth in total darkness | CHEBI:15824 / METPO:1000640 | “50 mM fructose also supports chemoheterotrophic growth in total darkness” (stebegg2023heterotrophyamongcyanobacteria pages 9-10) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Substrate-specific growth support; cyanobacterial example, uncertain for broad trait graph. |
| soil environment – enriches/dominates in – chemoorganoheterotrophs | ENVO:00001998 / METPO:1000640 | “most microbes are chemoorganoheterotrophs” and “over 95% of energy-rich organic compounds occur as litter, rhizodeposits, microbial necromass, organic fertilizers, and soil organic matter” (wang2023energyuseefficiency pages 4-4) | 10.1111/gcb.16925, 2023, https://doi.org/10.1111/gcb.16925 | Ecological prevalence edge; useful context but not a cell-intrinsic mechanism. |
| organic carbon uptake – primarily supplies – microbial energy demand | CHEBI:50860 / label-only microbial energy demand | “microorganisms use organic C mainly as an energy source” (wang2023energyuseefficiency pages 1-2) | 10.1111/gcb.16925, 2023, https://doi.org/10.1111/gcb.16925 | Strong ecological/physiological support for organotrophic energy use. |
| glucose-fed soil microbial metabolism – has EUE – 0.32–0.35 | CHEBI:17234 / label-only EUE | “The mean microbial EUE (0.32–0.35)” (wang2023energyuseefficiency pages 1-2) | 10.1111/gcb.16925, 2023, https://doi.org/10.1111/gcb.16925 | Quantitative systems-level parameter; not a causal edge in strict molecular sense, but useful trait annotation evidence. |
| glucose-fed soil microbial metabolism – has CUE – ~0.41 | CHEBI:17234 / label-only CUE | “CUE (0.41) using glucose as a substrate” (wang2023energyuseefficiency pages 1-2) | 10.1111/gcb.16925, 2023, https://doi.org/10.1111/gcb.16925 | Quantitative systems-level parameter; not a direct mechanistic edge. |
| microbial EUE – is lower than – microbial CUE | label-only EUE / label-only CUE | “EUE is 15%–22% lower than CUE” and “mean microbial EUE... is 18% lower than CUE” (wang2023energyuseefficiency pages 14-15, wang2023energyuseefficiency pages 1-2) | 10.1111/gcb.16925, 2023, https://doi.org/10.1111/gcb.16925 | Good quantitative relation; likely annotation/statistics rather than graph edge. |
| extracellular CAZymes – hydrolyze – complex plant polysaccharides | GO:0003824 / CHEBI:16646 | “microbes produce extracellular carbohydrate-active enzymes... that hydrolyse complex plant polysaccharides” (liew2024integratingmultiplatformassembly pages 11-15) | 10.1186/s40793-024-00572-7, 2024, https://doi.org/10.1186/s40793-024-00572-7 | Useful upstream mechanism for organotrophic substrate generation; hot spring biofilm-specific community context. |
| polysaccharide hydrolysis products – are imported by – sugar transporters | label-only sugars/oligosaccharides / GO:0005351 | “a diversity of sugar transporters then import monomers and short oligosaccharides” (liew2024integratingmultiplatformassembly pages 11-15) | 10.1186/s40793-024-00572-7, 2024, https://doi.org/10.1186/s40793-024-00572-7 | Mechanistically useful but community/taxon-specific; uncertain for general trait graph. |
| imported sugars – feed into – intracellular energy metabolism | CHEBI:35381 / GO:0006091 | “import monomers and short oligosaccharides for energy and downstream metabolism” (liew2024integratingmultiplatformassembly pages 11-15) | 10.1186/s40793-024-00572-7, 2024, https://doi.org/10.1186/s40793-024-00572-7 | Generic organotrophic edge; evidence comes from hot spring biofilms. |
| petroleum hydrocarbons – are oxidized anaerobically with electron acceptors – HCO3-/SO4(2-)/NO3-/Fe3+ | CHEBI:24632 / CHEBI:17544, CHEBI:16189, CHEBI:17632, CHEBI:29033 | “microorganisms can oxidize petroleum hydrocarbons using HCO3-, SO4(2-), NO3-, and Fe3+ as terminal electron acceptors” (pavlova2024anaerobicoxidationof pages 1-2) | 10.1134/S0026261724605608, 2024, https://doi.org/10.1134/s0026261724605608 | Important evidence for anaerobic organotrophic respiration; sediment/oil context, partly community-level. |
| heterotrophs in sewer biofilms – scavenge – organic exudates/EPS/cellular debris | label-only heterotrophs / CHEBI:24402 | “utilize organic exudates, EPS and cellular debris generated by chemolithoautotrophs” (li2017theecologyof pages 11-12) | 10.3389/fmicb.2017.00683, 2017, https://doi.org/10.3389/fmicb.2017.00683 | Community ecology edge; sewer corrosion-specific, uncertain for general trait graph. |
| sewer biofilm heterotrophs – produce – CO2 | label-only heterotrophs / CHEBI:16526 | “These heterotrophs produce CO2 that is then available to chemolithoautotrophs” (li2017theecologyof pages 11-12) | 10.3389/fmicb.2017.00683, 2017, https://doi.org/10.3389/fmicb.2017.00683 | Cross-feeding edge; ecosystem-specific and indirect for trait mechanism. |
| heterotroph-mediated removal of inhibitory organics – enables – chemolithoautotroph growth | label-only inhibitory organics / label-only chemolithoautotroph growth | “removing small organic molecules excreted by ASOM that can otherwise be toxic and inhibit autotroph growth” and “important to enable continued chemolithoautotrophic activity” (li2017theecologyof pages 11-12) | 10.3389/fmicb.2017.00683, 2017, https://doi.org/10.3389/fmicb.2017.00683 | Strong community interaction evidence; likely out-of-scope for a trait-intrinsic graph. |
| chemosynthetic symbiont energy metabolism – can use terminal electron acceptor – oxygen | CHEBI:15379 / CHEBI:15379 | “terminal electron acceptors include oxygen, nitrate, fumarate... and dimethyl sulfoxide” (sogin2021lifeinthe pages 9-11) | 10.1146/annurev-micro-051021-123130, 2021, https://doi.org/10.1146/annurev-micro-051021-123130 | Supports respiratory flexibility; not exclusive to chemoorganoheterotrophy. |
| chemosynthetic symbiont energy metabolism – can use terminal electron acceptor – nitrate | CHEBI:17632 / CHEBI:17632 | “terminal electron acceptors include oxygen, nitrate, fumarate... and dimethyl sulfoxide” (sogin2021lifeinthe pages 9-11) | 10.1146/annurev-micro-051021-123130, 2021, https://doi.org/10.1146/annurev-micro-051021-123130 | Supports anaerobic/low-O2 respiration possibilities; broad but not trait-exclusive. |
| chemosynthetic symbiont energy metabolism – can use terminal electron acceptor – fumarate | CHEBI:18012 / CHEBI:18012 | “terminal electron acceptors include oxygen, nitrate, fumarate... and dimethyl sulfoxide” (sogin2021lifeinthe pages 9-11) | 10.1146/annurev-micro-051021-123130, 2021, https://doi.org/10.1146/annurev-micro-051021-123130 | Broad respiratory flexibility; context is symbioses rather than free-living trait generalization. |
| chemosynthetic symbiont energy metabolism – can use terminal electron acceptor – dimethyl sulfoxide | CHEBI:16385 / CHEBI:16385 | “terminal electron acceptors include oxygen, nitrate, fumarate... and dimethyl sulfoxide” (sogin2021lifeinthe pages 9-11) | 10.1146/annurev-micro-051021-123130, 2021, https://doi.org/10.1146/annurev-micro-051021-123130 | Broad respiratory flexibility; context-specific, use cautiously. |


*Table: This table compiles candidate subject–predicate–object edges for chemoorganoheterotrophy, emphasizing source-backed mechanistic and ecological relationships plus curation caveats. It is useful as a starting point for TraitMech edge selection and for separating core trait-defining edges from taxon- or environment-specific evidence.*

### 6) Key statistics and data points relevant to the trait (recent sources)

- **Soil chemoorganoheterotrophy as dominant mode (ecological prevalence).** Soil microbes are described as predominantly chemoorganoheterotrophic, and the dominance is rationalized by the prevalence of energy-rich organic matter; one statement notes “most microbes are chemoorganoheterotrophs” and that “over 95% of energy-rich organic compounds occur as litter, rhizodeposits, microbial necromass, organic fertilizers, and soil organic matter” (10.1111/gcb.16925; Aug 2023) (wang2023energyuseefficiency pages 4-4).
- **CUE vs EUE (glucose example; 2023).** Mean microbial **EUE 0.32–0.35** and **CUE ~0.41** (glucose), with EUE ~15–22% lower than CUE; additionally, a global soil microbial EUE estimate of **0.32 ± 0.01** is reported (10.1111/gcb.16925; Aug 2023) (wang2023energyuseefficiency pages 1-2, wang2023energyuseefficiency pages 14-14, wang2023energyuseefficiency pages 14-15).
- **Thermodynamic linkage (NOSC).** Energy content per carbon correlates strongly with NOSC (R2 = 0.98), increasing by 108 kJ mol−1 C per NOSC unit (10.1111/gcb.16925; Aug 2023) (wang2023energyuseefficiency pages 1-2).

### 7) Visual evidence extracted

A key synthesis table contrasting carbon vs energy utilization processes (supporting the conceptual separation between CUE and EUE and highlighting processes where energy is expended without proportional carbon incorporation) was extracted from Wang & Kuzyakov 2023 (Table 2) (wang2023energyuseefficiency media a8f2f7de).

### 8) Expert interpretation and analysis (what is safe to curate now)

**What is robust for a general TraitMech graph:**
1. The definitional triad (organic substrates supply **C, electrons, and energy**) is strongly supported and should be core (stebegg2023heterotrophyamongcyanobacteria pages 1-2).
2. A minimal mechanistic backbone is well supported across contexts: **organic substrate availability → transport/import → catabolism producing ATP and reducing power (NAD(P)H) → biomass synthesis**, with respiration as a common energy-conservation route (stebegg2023heterotrophyamongcyanobacteria pages 2-4).
3. Environmental flexibility (aerobic vs alternative electron acceptors) is plausible for many chemoorganoheterotrophs; however, evidence in this packet is environment- and community-specific (oil seep sediments; symbionts) and should be curated as conditional edges (pavlova2024anaerobicoxidationof pages 1-2, sogin2021lifeinthe pages 9-11).

**What should be curated as conditional / uncertain:**
- **Specific terminal oxidases or loci (e.g., aa3-type cytochrome c oxidase; *coxBAC1*)** as general requirements: strong evidence exists in a cyanobacterial system for fructose dark growth but this is not universal (stebegg2023heterotrophyamongcyanobacteria pages 10-11).
- **Specific substrates (fructose vs glucose phenotypes)** and concentration thresholds: these are species/strain-specific and assay-specific (stebegg2023heterotrophyamongcyanobacteria pages 9-10).
- **Community ecological interactions** (heterotroph detoxification enabling chemolithoautotroph activity in sewer corrosion): valuable for applied microbiome graphs, but not necessarily intrinsic to the chemoorganoheterotrophic trait definition (li2017theecologyof pages 11-12).

### 9) DOI-first bibliography (with publication dates and URLs)

1. Stebegg R, Schmetterer G, Rompel A. **Heterotrophy among Cyanobacteria.** *ACS Omega.* Published Sep 2023. DOI: **10.1021/acsomega.3c02205**. URL: https://doi.org/10.1021/acsomega.3c02205 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria pages 10-11, stebegg2023heterotrophyamongcyanobacteria pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 2-2).
2. Wang C, Kuzyakov Y. **Energy use efficiency of soil microorganisms: Driven by carbon recycling and reduction.** *Global Change Biology.* Published Aug 2023. DOI: **10.1111/gcb.16925**. URL: https://doi.org/10.1111/gcb.16925 (wang2023energyuseefficiency pages 1-2, wang2023energyuseefficiency pages 4-4, wang2023energyuseefficiency pages 14-14, wang2023energyuseefficiency pages 14-15, wang2023energyuseefficiency media a8f2f7de).
3. Liew KJ et al. **Integrating multi-platform assembly to recover MAGs from hot spring biofilms: insights into microbial diversity, biofilm formation, and carbohydrate degradation.** *Environmental Microbiome.* Published May 2024. DOI: **10.1186/s40793-024-00572-7**. URL: https://doi.org/10.1186/s40793-024-00572-7 (liew2024integratingmultiplatformassembly pages 11-15).
4. Pavlova ON et al. **Anaerobic Oxidation of Oil by Microbial Communities of Bottom Sediments of a Natural Oil Seepage Site (Bolshaya Zelenovskaya, Middle Baikal).** *Microbiology.* Published Sep 2024. DOI: **10.1134/S0026261724605608**. URL: https://doi.org/10.1134/s0026261724605608 (pavlova2024anaerobicoxidationof pages 1-2).
5. Sogin EM et al. **Life in the Dark: Phylogenetic and Physiological Diversity of Chemosynthetic Symbioses.** *Annual Review of Microbiology.* Published Oct 2021. DOI: **10.1146/annurev-micro-051021-123130**. URL: https://doi.org/10.1146/annurev-micro-051021-123130 (sogin2021lifeinthe pages 9-11).
6. Li X et al. **The Ecology of Acidophilic Microorganisms in the Corroding Concrete Sewer Environment.** *Frontiers in Microbiology.* Published Apr 2017. DOI: **10.3389/fmicb.2017.00683**. URL: https://doi.org/10.3389/fmicb.2017.00683 (li2017theecologyof pages 1-2, li2017theecologyof pages 11-12, li2017theecologyof pages 4-6, li2017theecologyof pages 7-8).

### 10) Warnings / non-curatable (yet) claims

- Do **not** generalize cyanobacteria-specific gene requirements (e.g., aa3-type oxidase dependency for fructose dark growth) to all chemoorganoheterotrophs; curate as **taxon-specific** if needed (stebegg2023heterotrophyamongcyanobacteria pages 10-11).
- Treat community-interaction edges (e.g., heterotroph detoxification enabling sulfur-oxidizing chemolithotrophs in sewers) as **ecosystem-context graphs**, not as intrinsic trait mechanisms (li2017theecologyof pages 11-12).
- Quantitative EUE/CUE relationships are valuable **annotation/statistics**, but should be curated carefully: they are emergent parameters measured under specific substrate and environmental conditions rather than universal mechanistic constants (wang2023energyuseefficiency pages 1-2, wang2023energyuseefficiency pages 14-15).

References

1. (stebegg2023heterotrophyamongcyanobacteria pages 1-2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

2. (stebegg2023heterotrophyamongcyanobacteria pages 2-4): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

3. (stebegg2023heterotrophyamongcyanobacteria pages 2-2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

4. (dang2017ecologicalenergeticperspectives pages 1-2): Hongyue Dang and Chen-Tung A. Chen. Ecological energetic perspectives on responses of nitrogen-transforming chemolithoautotrophic microbiota to changes in the marine environment. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01246, doi:10.3389/fmicb.2017.01246. This article has 60 citations and is from a peer-reviewed journal.

5. (stebegg2023heterotrophyamongcyanobacteria pages 9-10): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

6. (carini2013nutrientrequirementsfor pages 1-2): P. Carini, L. Steindler, Sára Beszteri, and S. Giovannoni. Nutrient requirements for growth of the extreme oligotroph ‘candidatus pelagibacter ubique’ htcc1062 on a defined medium. The ISME Journal, 7:592-602, Oct 2013. URL: https://doi.org/10.1038/ismej.2012.122, doi:10.1038/ismej.2012.122. This article has 294 citations.

7. (stebegg2023heterotrophyamongcyanobacteria pages 10-11): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

8. (wang2023energyuseefficiency pages 1-2): Chaoqun Wang and Yakov Kuzyakov. Energy use efficiency of soil microorganisms: driven by carbon recycling and reduction. Global Change Biology, 29:6170-6187, Aug 2023. URL: https://doi.org/10.1111/gcb.16925, doi:10.1111/gcb.16925. This article has 144 citations and is from a highest quality peer-reviewed journal.

9. (wang2023energyuseefficiency pages 14-15): Chaoqun Wang and Yakov Kuzyakov. Energy use efficiency of soil microorganisms: driven by carbon recycling and reduction. Global Change Biology, 29:6170-6187, Aug 2023. URL: https://doi.org/10.1111/gcb.16925, doi:10.1111/gcb.16925. This article has 144 citations and is from a highest quality peer-reviewed journal.

10. (liew2024integratingmultiplatformassembly pages 11-15): Kok Jun Liew, Saleha Shahar, Mohd Shahir Shamsir, Nawal Binti Shaharuddin, Chee Hung Liang, Kok-Gan Chan, Stephen Brian Pointing, Rajesh Kumar Sani, and Kian Mau Goh. Integrating multi-platform assembly to recover mags from hot spring biofilms: insights into microbial diversity, biofilm formation, and carbohydrate degradation. Environmental Microbiome, May 2024. URL: https://doi.org/10.1186/s40793-024-00572-7, doi:10.1186/s40793-024-00572-7. This article has 21 citations and is from a peer-reviewed journal.

11. (pavlova2024anaerobicoxidationof pages 1-2): O. N. Pavlova, S. V. Bukin, O. N. Izosimova, S. M. Chernitsina, V. G. Ivanov, A. V. Khabuev, T. V. Pogodaeva, I. S. Elovskaya, A. G. Gorshkov, and T. I. Zemskaya. Anaerobic oxidation of oil by microbial communities of bottom sediments of a natural oil seepage site (bolshaya zelenovskaya, middle baikal). Microbiology, 93:563-575, Sep 2024. URL: https://doi.org/10.1134/s0026261724605608, doi:10.1134/s0026261724605608. This article has 7 citations and is from a peer-reviewed journal.

12. (li2017theecologyof pages 1-2): Xuan Li, Ulrike Kappler, Guangming Jiang, and Philip L. Bond. The ecology of acidophilic microorganisms in the corroding concrete sewer environment. Frontiers in Microbiology, Apr 2017. URL: https://doi.org/10.3389/fmicb.2017.00683, doi:10.3389/fmicb.2017.00683. This article has 169 citations and is from a peer-reviewed journal.

13. (li2017theecologyof pages 11-12): Xuan Li, Ulrike Kappler, Guangming Jiang, and Philip L. Bond. The ecology of acidophilic microorganisms in the corroding concrete sewer environment. Frontiers in Microbiology, Apr 2017. URL: https://doi.org/10.3389/fmicb.2017.00683, doi:10.3389/fmicb.2017.00683. This article has 169 citations and is from a peer-reviewed journal.

14. (li2017theecologyof pages 4-6): Xuan Li, Ulrike Kappler, Guangming Jiang, and Philip L. Bond. The ecology of acidophilic microorganisms in the corroding concrete sewer environment. Frontiers in Microbiology, Apr 2017. URL: https://doi.org/10.3389/fmicb.2017.00683, doi:10.3389/fmicb.2017.00683. This article has 169 citations and is from a peer-reviewed journal.

15. (sogin2021lifeinthe pages 9-11): E. Maggie Sogin, Manuel Kleiner, Christian Borowski, Harald R. Gruber-Vodicka, and Nicole Dubilier. Life in the dark: phylogenetic and physiological diversity of chemosynthetic symbioses. Annual Review of Microbiology, 75:695-718, Oct 2021. URL: https://doi.org/10.1146/annurev-micro-051021-123130, doi:10.1146/annurev-micro-051021-123130. This article has 79 citations and is from a peer-reviewed journal.

16. (li2017theecologyof pages 7-8): Xuan Li, Ulrike Kappler, Guangming Jiang, and Philip L. Bond. The ecology of acidophilic microorganisms in the corroding concrete sewer environment. Frontiers in Microbiology, Apr 2017. URL: https://doi.org/10.3389/fmicb.2017.00683, doi:10.3389/fmicb.2017.00683. This article has 169 citations and is from a peer-reviewed journal.

17. (wang2023energyuseefficiency pages 4-4): Chaoqun Wang and Yakov Kuzyakov. Energy use efficiency of soil microorganisms: driven by carbon recycling and reduction. Global Change Biology, 29:6170-6187, Aug 2023. URL: https://doi.org/10.1111/gcb.16925, doi:10.1111/gcb.16925. This article has 144 citations and is from a highest quality peer-reviewed journal.

18. (wang2023energyuseefficiency pages 14-14): Chaoqun Wang and Yakov Kuzyakov. Energy use efficiency of soil microorganisms: driven by carbon recycling and reduction. Global Change Biology, 29:6170-6187, Aug 2023. URL: https://doi.org/10.1111/gcb.16925, doi:10.1111/gcb.16925. This article has 144 citations and is from a highest quality peer-reviewed journal.

19. (wang2023energyuseefficiency media a8f2f7de): Chaoqun Wang and Yakov Kuzyakov. Energy use efficiency of soil microorganisms: driven by carbon recycling and reduction. Global Change Biology, 29:6170-6187, Aug 2023. URL: https://doi.org/10.1111/gcb.16925, doi:10.1111/gcb.16925. This article has 144 citations and is from a highest quality peer-reviewed journal.