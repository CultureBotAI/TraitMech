---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:42:08.864201'
end_time: '2026-06-18T09:58:00.477287'
duration_seconds: 951.61
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spore shaped
  trait_identifier: METPO:1000682
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spore_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism or differentiated cell has an endospore-like
    morphology, reflecting a dormant spore body with specialized protective layers.
  parent_traits: METPO:1000666
  synonyms: spore-shaped
  evidence_summary: 'DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports
    endospore morphology as a differentiated structure with specialized surface layers.)'
  causal_graph_summary: 'spore_shaped_endospore_layers: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spore shaped
- **METPO identifier:** METPO:1000682
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism or differentiated cell has an endospore-like morphology, reflecting a dormant spore body with specialized protective layers.
- **Parent traits:** METPO:1000666
- **Synonyms:** spore-shaped
- **Existing evidence:** DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports endospore morphology as a differentiated structure with specialized surface layers.)
- **Existing causal graph summary:** spore_shaped_endospore_layers: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spore shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_shaped.yaml`.

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
- **Trait label:** spore shaped
- **METPO identifier:** METPO:1000682
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism or differentiated cell has an endospore-like morphology, reflecting a dormant spore body with specialized protective layers.
- **Parent traits:** METPO:1000666
- **Synonyms:** spore-shaped
- **Existing evidence:** DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports endospore morphology as a differentiated structure with specialized surface layers.)
- **Existing causal graph summary:** spore_shaped_endospore_layers: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **spore shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **spore shaped** (METPO:1000682)

### Scope summary (TraitMech curation intent)
**Trait meaning.** The METPO term *spore shaped* (METPO:1000682) corresponds to an **endospore-like morphology**: a differentiated, dormant cellular form with a specialized multilayer envelope (at minimum **core + cortex + proteinaceous coat**, and in some taxa an outer **exosporium**), produced through a regulated **sporulation** developmental program. The defining morphology is therefore not merely “round/ovoid” shape, but **spore ultrastructure** (cortex/coats/exosporium) and the morphogenetic sequence that produces it (asymmetric septation → engulfment → cortex/coat deposition → maturation). This is supported by a recent C. difficile mechanistic description that explicitly enumerates endospore layers (cortex, coat, exosporium) and by a classic Bacillus coat-assembly synthesis that defines coat layers and “encasement” as a key morphogenetic transformation (nerber2024thesmallacidsoluble pages 1-2, mckenney2013thebacillussubtilis pages 20-24, mckenney2013thebacillussubtilis pages 11-13).

**Boundary cases / exclusions.** For curation, *spore shaped* should be **restricted to endospores** (Firmicutes-like endospore formers and closely related lineages) and should generally **exclude**:
- **Non-endospore resting cells** (e.g., cyst-like morphologies) that lack a cortex/coat architecture.
- **Exospores/aerial spores** (Actinobacteria) formed externally by different developmental programs and envelope architectures.
- “Spore-like” morphologies observed under stress without evidence of the canonical sporulation program.

**Assay observables.** In practice, the trait is often observed by microscopy (phase-bright spores, TEM-defined layers) and/or by correlated functional assays (heat/lysozyme resistance), but note that **resistance is downstream** of morphology and should be modeled as an outcome rather than the defining trait (kuwana2024spoivaisan pages 4-6, kuwana2024spoivaisan pages 1-2).

---

## 1) Key concepts and definitions (current understanding)

### Endospore structural components (nodes)
Recent and foundational sources agree on the following core structural decomposition:
- **Core**: contains DNA/RNA/ribosomes and key protective molecules including **calcium dipicolinate (Ca–DPA)** and **small acid-soluble proteins (SASPs)** (nerber2024thesmallacidsoluble pages 1-2).
- **Cortex**: a specialized peptidoglycan layer; in C. difficile, cortex PG includes **muramic-δ-lactam** residues recognized by cortex lytic enzymes during germination (nerber2024thesmallacidsoluble pages 1-2).
- **Coat**: proteinaceous multilayer shell; in *B. subtilis* commonly described as **basement layer, inner coat, outer coat, and crust** (mckenney2013thebacillussubtilis pages 20-24). Coat **encasement** is a morphogenetic transition from a polar cap to a complete shell around the forespore (mckenney2013thebacillussubtilis pages 6-7, mckenney2013thebacillussubtilis pages 24-26).
- **Exosporium** (taxon-dependent): an additional outer layer in some Bacillus/Clostridioides, functioning as a permeability barrier and robustness layer; assembly can proceed from a cap to a full shell (mckenney2013thebacillussubtilis pages 11-13, marini2023asporulationsignature pages 2-3).

Figure evidence for coat-layer definitions and the encasement model is available in the cropped images from McKenney et al. (Nat Rev Microbiol 2013) (mckenney2013thebacillussubtilis media fbb58921, mckenney2013thebacillussubtilis media 597936fc).

### Developmental program (sporulation) as the morphogenetic backbone
A key mechanistic definition for curation is that endospore morphology is produced by a regulated differentiation program:
- **Sporulation initiation** is triggered by **Spo0A phosphorylation** (master regulator) (nerber2024thesmallacidsoluble pages 1-2).
- Morphogenesis proceeds through **asymmetric division** (mother cell + forespore), followed by **engulfment**, then **cortex/coat deposition** (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2).
- A **compartmental sigma factor cascade** coordinates stage- and compartment-specific gene expression (σF/σG in forespore; σE/σK in mother cell) with strong stage-specific phenotypes when disrupted (nerber2024thesmallacidsoluble pages 1-2).

---

## 2) Recent developments and latest research (prioritized 2023–2024)

### 2.1 In situ cryo-electron tomography resolves nascent coat regions and quantifies ultrastructure (2024)
Bauda et al. used cryo-FIB milling and **in situ cryo-electron tomography** to resolve multiple coat-associated regions above the outer forespore membrane in *B. subtilis*, distinguishing **seven nascent coat regions** and quantifying multiple layer thicknesses with nm-scale precision (e.g., thin light matrix **3.2 ± 0.2 nm**, thick dark matrix **22.5 ± 4.5 nm**, with reported n values) (bauda2024ultrastructureofmacromolecular pages 5-7). The same study ties morphogenetic proteins to specific ultrastructural defects, explicitly stating that the main morphogenetic proteins’ absence causes major early architecture defects and that **SafA and CotE are required for inner and outer coat deposition** (bauda2024ultrastructureofmacromolecular pages 2-3). These measurements strengthen the curatability of edges that connect particular morphogenetic proteins to particular coat regions/architectures.

### 2.2 Protease control of surface-layer assembly and germination (2023)
Marini et al. (PLOS Pathogens, Nov 2023) show that the sporulation signature protease **YabG is critical for assembly of the coat and exosporium layers** in *C. difficile*, and link YabG to processing of germination-related precursors (CspBA processing that releases CspB) and to downstream phenotypes including layer misassembly and impaired colonization (marini2023asporulationsignature pages 2-3). This connects **proteolysis** as a causal mechanism upstream of “spore-shaped” envelope architecture.

### 2.3 SASPs as developmental regulators affecting cortex morphogenesis (2024)
Nerber et al. (PLOS Pathogens, Aug 2024) report that *C. difficile* SASPs **SspA and SspB are required for formation of the spore cortex layer**, and propose a mechanism where SASPs regulate sporulation in a **spoIVB2-dependent** manner; suppressor mutations increase spoIVB2 translation efficiency/abundance during late sporulation (nerber2024thesmallacidsoluble pages 1-2). This moves SASPs beyond “DNA protection” into the causal graph upstream of morphological layer formation.

### 2.4 Conservation and taxon-specific implementation of SpoIVA (2024)
Kuwana et al. (Frontiers in Microbiology, Apr 2024) demonstrate in *Clostridium sporogenes* that **spoIVA inactivation causes abnormal forespore development, misassembly/accumulation of coat and exosporium proteins in mother cells, and loss of resistance to heat and lysozyme** (assayed at **80°C for 20 min** and **250 µg/mL lysozyme for 10 min**, with statistics) (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 4-6). This provides recent, species-specific knockout evidence reinforcing SpoIVA as a conserved morphogenetic node.

---

## 3) Current applications and real-world implementations

### 3.1 Spore surface display and mucosal vaccine/drug delivery platforms
A 2024 review on **Bacillus subtilis spore surface display (BSSD)** describes real-world development of using the stability and robustness of spores to display antigens and deliver therapeutics to mucosal sites, leveraging the durable coat/crust architecture as the engineering substrate (Bahrulolum et al., Nov 2024, DOI:10.3390/ddc3040044; retrieved but not evidence-mined in depth here). Mechanistically, this application depends on the coat layer organization and on which coat proteins are surface-exposed (conceptually supported by the coat/crust coverage model where the crust can cover outer coat proteins and modulate adsorption/surface availability) (mckenney2013thebacillussubtilis pages 20-24).

### 3.2 Infection control and pathogenesis contexts (C. difficile)
Spore morphology (coat/exosporium) is directly tied to pathogen persistence and host interactions. For example, a 2024 mechanistic study shows *C. difficile* spores can carry toxin (TcdA) at the spore surface and that regulatory control during sporulation (σG/SpoVT control of tcdR production) drives toxin-associated phenotypes, illustrating that sporulation-stage regulation can change spore surface properties relevant to disease transmission (cassona2024sporesofclostridioides pages 1-2). A 2024 review of *C. difficile* interventions explicitly frames sporulation inhibition as a therapeutic strategy (Cun et al., Jun 2024, DOI:10.3390/microorganisms12061206; retrieved but not evidence-mined here).

---

## 4) Expert synthesis and authoritative perspectives (evidence-backed)

### Modular morphogenetic logic of spore coat construction
McKenney et al. (Nature Reviews Microbiology, Dec 2013; highly cited) provide a canonical expert synthesis: the *B. subtilis* coat is organized into layers, each organized by a distinct **morphogenetic protein** (SpoIVA for basement; SafA inner coat; CotE outer coat; CotX/Y/Z crust) and assembled through a dynamic localization/encasement process in which SpoVM and SpoVID are required for the transition from a cap to a full shell (mckenney2013thebacillussubtilis pages 20-24, mckenney2013thebacillussubtilis pages 6-7). This layered, modular concept is directly compatible with a TraitMech causal graph with layer nodes and morphogenetic-protein nodes.

### Ultrastructure-driven refinement of “layer” nodes
Bauda et al. (Nat Commun, Feb 2024) extend the “layer” view to finer subregions with quantified thicknesses and distinct electron densities and then causally map these regions to SpoIVA/SpoVID/SafA/CotE dependencies (bauda2024ultrastructureofmacromolecular pages 5-7, bauda2024ultrastructureofmacromolecular pages 2-3). This supports curating additional, more granular structure nodes (e.g., “thin dark matrix”, “bead-like layer”) where desired, though these may be difficult to generalize across taxa.

---

## 5) Relevant statistics and recent data

- **Cryo-ET quantitative ultrastructure (B. subtilis)**: multiple coat matrix thicknesses measured with means ± SD and n values (e.g., 3.2 ± 0.2 nm; 8.9 ± 0.8 nm; 17.8 ± 3.7 nm; 22.5 ± 4.5 nm; each with reported n) (bauda2024ultrastructureofmacromolecular pages 5-7). Additional quantitative metrics include mother-cell peptidoglycan thickness 26.9 ± 1.3 nm (n=36) and other structural distances (bauda2024ultrastructureofmacromolecular pages 2-3).
- **Resistance assay parameters (C. sporogenes spoIVA knockout)**: heating **80°C for 20 min** and lysozyme **250 µg/mL for 10 min**, with viability enumeration and statistical testing (two-way ANOVA/Tukey; P≤0.05) (kuwana2024spoivaisan pages 4-6).
- **Public health contextual statistic (C. difficile burden)**: ~220,000 cases and ~13,000 deaths annually are cited in Nerber et al. as context for why sporulation/spores matter, though not a morphology metric per se (nerber2024thesmallacidsoluble pages 1-2).

---

## Candidate nodes for `spore_shaped.yaml` (grouped by type)

### A) Processes / pathways
- Sporulation (GO:0043934) (nerber2024thesmallacidsoluble pages 1-2)
- Sporulation resulting in formation of a cellular spore (GO:0030435) (grounding suggestion; consistent with sporulation framing) (nerber2024thesmallacidsoluble pages 1-2)
- Asymmetric septation (label-only) (nerber2024thesmallacidsoluble pages 1-2)
- Engulfment (label-only) (nerber2024thesmallacidsoluble pages 1-2)
- Spore coat assembly / encasement (label-only) (mckenney2013thebacillussubtilis pages 6-7, mckenney2013thebacillussubtilis pages 24-26)

### B) Cellular structures (morphology-defining)
- Spore core (label-only) (nerber2024thesmallacidsoluble pages 1-2)
- Spore cortex (specialized peptidoglycan) (label-only) (nerber2024thesmallacidsoluble pages 1-2)
- Spore coat (basement layer, inner coat, outer coat, crust) (label-only) (mckenney2013thebacillussubtilis pages 20-24)
- Exosporium (label-only; taxon-specific) (mckenney2013thebacillussubtilis pages 11-13, marini2023asporulationsignature pages 2-3)
- Cryo-ET-defined nascent coat regions (e.g., thin/thick matrices; bead-like patterns) (label-only) (bauda2024ultrastructureofmacromolecular pages 5-7)

### C) Genes/proteins/complexes (morphogenetic & regulators)
**Regulators**
- Spo0A (master regulator; phosphorylation-driven initiation) (nerber2024thesmallacidsoluble pages 1-2)
- Sigma factors: σE, σK (mother cell); σF, σG (forespore) (nerber2024thesmallacidsoluble pages 1-2)
- SpoVT (forespore regulator) (cassona2024sporesofclostridioides pages 1-2)

**Coat/crust morphogenesis (B. subtilis core model)**
- SpoIVA (anchor/tether) (mckenney2013thebacillussubtilis pages 6-7, bauda2024ultrastructureofmacromolecular pages 5-7)
- SpoVM (curvature sensing; encasement requirement) (mckenney2013thebacillussubtilis pages 20-24)
- SpoVID (encasement; interacts with CotE and guides SafA) (mckenney2013thebacillussubtilis pages 7-9, mckenney2013thebacillussubtilis pages 15-17)
- SafA (inner coat organizer) (mckenney2013thebacillussubtilis pages 6-7, bauda2024ultrastructureofmacromolecular pages 2-3)
- CotE (outer coat organizer; CotE polymers in bead-like structures) (mckenney2013thebacillussubtilis pages 6-7, bauda2024ultrastructureofmacromolecular pages 5-7)
- CotX/CotY/CotZ (crust morphogenesis) (mckenney2013thebacillussubtilis pages 7-9, mckenney2013thebacillussubtilis pages 26-27)

**Exosporium morphogenesis (taxon-specific)**
- ExsY (exosporium encasement; cap-to-shell) (mckenney2013thebacillussubtilis pages 11-13)
- CdeC/CdeM (C. difficile exosporium determinants) (marini2023asporulationsignature pages 2-3)

**Proteolysis/processing affecting surface layers and germination**
- YabG protease (required for coat/exosporium assembly; CspBA processing context) (marini2023asporulationsignature pages 2-3)
- spoIVB2 (σF-regulated protease; SASP-linked control) (nerber2024thesmallacidsoluble pages 1-2)

**DNA/core protection with morphology coupling**
- SASPs: SspA/SspB (DNA-binding; also required for cortex formation in C. difficile) (nerber2024thesmallacidsoluble pages 1-2)

### D) Chemicals / metabolites
- Calcium(2+) (CHEBI:60039) (voitsekhovsky2024peculiaritiesofthe pages 5-7)
- Dipicolinic acid (label-only; DPA) (voitsekhovsky2024peculiaritiesofthe pages 5-7)
- Muramic-δ-lactam (label-only; cortex PG modification) (nerber2024thesmallacidsoluble pages 1-2)

### E) Environmental / experimental factors
- Starvation (ENVO:01000981) as trigger (updegrove2024altruisticfeedingand pages 14-14)
- Heat challenge (80°C for 20 min) (kuwana2024spoivaisan pages 4-6)
- Lysozyme exposure (250 µg/mL for 10 min) (kuwana2024spoivaisan pages 4-6)

---

## Candidate causal edges (evidence-backed) — curation table
The following table is designed for direct transcription into a TraitMech YAML, including taxon scope and uncertainty flags.

| Edge (subject–predicate–object) | Node types | Suggested ontology grounding | Taxon scope | Evidence snippet | Reference | Uncertainty flag / notes |
|---|---|---|---|---|---|---|
| Spo0A phosphorylation → positively regulates → sporulation initiation | regulator → process | Spo0A (label-only); GO:0043934 sporulation; GO:0030435 sporulation resulting in formation of a cellular spore | Bacillus subtilis; Clostridioides difficile | “sporulation initiates upon phosphorylation of Spo0A”; Spo0A is the “master regulator” governing entry into sporulation (nerber2024thesmallacidsoluble pages 1-2, updegrove2024altruisticfeedingand pages 14-14) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507; 10.1126/sciadv.adq0791 (2024) https://doi.org/10.1126/sciadv.adq0791 | Strong, but generalized across endospore formers; exact upstream phosphorelay differs by taxon |
| Starvation → positively regulates → sporulation initiation | environmental factor → process | ENVO:01000981 starvation; GO:0043934 sporulation | Bacillus subtilis | “Starvation triggers bacterial spore formation, a committed differentiation program” (updegrove2024altruisticfeedingand pages 14-14) | 10.1126/sciadv.adq0791 (2024) https://doi.org/10.1126/sciadv.adq0791 | Strong for B. subtilis; environmental trigger may vary by organism/culture conditions |
| Loss of σE → causes block in → asymmetric septation | sigma factor → process | sigma E (label-only); GO:0030435 sporulation resulting in formation of a cellular spore; asymmetric septation (label-only) | Clostridioides difficile | “Loss of σE results in a strain that is blocked at asymmetric septation” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific phenotype |
| Loss of σF → negatively affects → engulfment completion | sigma factor → process | sigma F (label-only); engulfment (label-only) | Clostridioides difficile | “Loss of σF results in a strain that does not complete engulfment” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific phenotype |
| Loss of σF → prevents formation of → spore cortex layer | sigma factor → structure/process | sigma F (label-only); cortex (label-only) | Clostridioides difficile | “Loss of σF results in a strain that does not… form the cortex layer” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific phenotype |
| Loss of σG → negatively affects → engulfment completion | sigma factor → process | sigma G (label-only); engulfment (label-only) | Clostridioides difficile | “Loss of σG results in a strain… [that] does not fully complete engulfment” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific phenotype |
| Loss of σG → prevents formation of → spore cortex layer | sigma factor → structure/process | sigma G (label-only); cortex (label-only) | Clostridioides difficile | “Loss of σG results in a strain… [that does not] form the cortex layer” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific phenotype |
| Loss of σK → prevents formation of → visible coat layer | sigma factor → structure | sigma K (label-only); spore coat (label-only) | Clostridioides difficile | “Loss of σK results in a strain that fully engulfs the forespore and forms a correctly localized cortex layer, but no visible coat layer” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific phenotype |
| SpoIVA → anchors/tethers → coat to spore surface / outer forespore membrane | protein → structure | SpoIVA (label-only); outer forespore membrane (label-only); spore coat (label-only) | Bacillus subtilis; Clostridium sporogenes | “SpoIVA functions to anchor coat material to the spore surface”; ΔspoIVA causes all nascent coat layers to be mislocalized; SpoIVA is “required to tether the coat to the OFM” (mckenney2013thebacillussubtilis pages 6-7, bauda2024ultrastructureofmacromolecular pages 5-7) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921; 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Strong in Bacillus; conserved role supported in Clostridium by morphology/resistance study |
| spoIVA inactivation → causes misassembly of → spore coat and exosporium proteins | gene disruption → structures | SpoIVA (label-only); spore coat (label-only); exosporium (label-only) | Clostridium sporogenes | “the spore coat and exosporium proteins were misassembled and… accumulated in the mother cells of the mutant” (kuwana2024spoivaisan pages 1-2) | 10.3389/fmicb.2024.1338751 (2024) https://doi.org/10.3389/fmicb.2024.1338751 | Strong, species-specific knockout evidence |
| SpoVM → required for → spore encasement | protein → process | SpoVM (label-only); encasement (label-only) | Bacillus subtilis | “SpoVM and SpoVID are required for the morphological transition from a single scaffold cap to a full spherical shell that encases the forespore” (mckenney2013thebacillussubtilis pages 6-7, mckenney2013thebacillussubtilis pages 20-24) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921 | Strong, foundational Bacillus evidence |
| SpoVID → required for → spore encasement | protein → process | SpoVID (label-only); encasement (label-only) | Bacillus subtilis | “SpoVID is explicitly required for spore encasement”; spoVID mutants “block formation of a full coat shell” (mckenney2013thebacillussubtilis pages 7-9, mckenney2013thebacillussubtilis pages 24-26) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921 | Strong, foundational Bacillus evidence |
| CotE → required for assembly of → outer coat | protein → structure | CotE (label-only); outer coat (label-only) | Bacillus subtilis | “SafA is necessary for inner coat assembly and CotE for outer coat assembly” (mckenney2013thebacillussubtilis pages 6-7, bauda2024ultrastructureofmacromolecular pages 2-3) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921; 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Strong in B. subtilis |
| SafA → required for assembly of → inner coat | protein → structure | SafA (label-only); inner coat (label-only) | Bacillus subtilis | “SafA is necessary for inner coat assembly”; “SafA and CotE are respectively required for the deposition of the inner and outer coat” (mckenney2013thebacillussubtilis pages 6-7, bauda2024ultrastructureofmacromolecular pages 2-3) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921; 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Strong in B. subtilis |
| CotX/CotY/CotZ → required for assembly of → crust | proteins → structure | CotX (label-only); CotY (label-only); CotZ (label-only); crust (label-only) | Bacillus subtilis | “CotX, CotY and CotZ are morphogenetic proteins required for assembly of an additional outermost electron-dense layer (the ‘crust’) absent in ΔcotXYZ mutants” (mckenney2013thebacillussubtilis pages 7-9, mckenney2013thebacillussubtilis pages 26-27) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921 | Strong in B. subtilis |
| ExsY deletion → prevents encasement of → exosporium shell | protein/gene loss → structure/process | ExsY (label-only); exosporium (label-only) | Bacillus anthracis | “Deletion of exsY… yields an exosporium that forms a cap but fails to encase the spore” (mckenney2013thebacillussubtilis pages 11-13) | 10.1038/nrmicro2921 (2013) https://doi.org/10.1038/nrmicro2921 | Strong for B. anthracis; exosporium-specific, not universal to all endospores |
| ExsY → required for non-cap assembly of → exosporium basal layer | protein → structure | ExsY (label-only); exosporium basal layer (label-only) | Bacillus anthracis | “ExsY identified as the major structural protein for this non-cap assembly”; loss of ExsY forms “only the exosporium cap structure” (heredia2023interplayofbacillus pages 185-189) | 10.32469/10355/98752 (2023) https://doi.org/10.32469/10355/98752 | Moderate: thesis evidence, not primary journal article |
| YabG protease → required for assembly of → coat and exosporium layers | protease → structures | YabG (label-only); spore coat (label-only); exosporium (label-only) | Clostridioides difficile | “YabG is critical for the assembly of the coat and exosporium layers of spores” (marini2023asporulationsignature pages 2-3) | 10.1371/journal.ppat.1011741 (2023) https://doi.org/10.1371/journal.ppat.1011741 | Strong, taxon-specific |
| YabG protease → proteolytically processes → CspBA | protease → protein substrate | YabG (label-only); CspBA (label-only) | Clostridioides difficile | loss of yabG leads to “accumulation of unprocessed forms of CspBA”; YabG auto-proteolysis/interdomain processing “releases the CspB protease” (marini2023asporulationsignature pages 2-3) | 10.1371/journal.ppat.1011741 (2023) https://doi.org/10.1371/journal.ppat.1011741 | Strong for processing relationship; downstream morphology link indirect but supported |
| SspA/SspB (SASPs) → required for formation of → spore cortex layer | proteins → structure | SspA (label-only); SspB (label-only); cortex (label-only) | Clostridioides difficile | “C. difficile sspA and sspB are required for the formation of the spore cortex layer” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong, taxon-specific |
| SspA/SspB → positively regulate → spoIVB2 expression/abundance during late sporulation | proteins → protease/regulatory step | SspA (label-only); SspB (label-only); spoIVB2 (label-only) | Clostridioides difficile | “σG-regulated SspA/SspB directly or indirectly activate spoIVB2 expression during late sporulation”; suppressors act “by increasing spoivb2 translation efficiency and, thus, abundance” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Moderate: directness uncertain; authors allow “directly or indirectly” |
| Muramic-δ-lactam residues in cortex → are recognized by → cortex lytic enzymes during germination | chemical moiety/structure → enzyme activity | muramic-δ-lactam (label-only); cortex lytic enzymes (label-only) | Clostridioides difficile / endospores generally | “in the cortex many N-acetylmuramic acid residues are converted to muramic-δ-lactam, which are recognized by cortex lytic enzymes during germination” (nerber2024thesmallacidsoluble pages 1-2) | 10.1371/journal.ppat.1012507 (2024) https://doi.org/10.1371/journal.ppat.1012507 | Strong structural-functional statement; more about germination than morphology, but defines cortex specialization |
| Dipicolinic acid accumulation + Ca2+ accumulation → associated with → increased spore refractivity / maturation | chemicals → morphology/physical property | CHEBI:60039 calcium(2+); dipicolinic acid (label-only); refractivity (label-only) | Bacillus spp. | “coat formation accompanied by increased refractivity/enlightenment correlated with DPA and Ca2+ accumulation” (voitsekhovsky2024peculiaritiesofthe pages 5-7) | 10.15407/microbiolj86.04.091 (2024) https://doi.org/10.15407/microbiolj86.04.091 | Moderate: correlation language, not direct mechanistic proof; older concept summarized in review-style article |
| Spo0A/Spo0F phosphorelay activity noise → drives heterogeneity in → sporulation entry | signaling process → process phenotype | Spo0A (label-only); Spo0F (label-only); GO:0043934 sporulation | Bacillus subtilis | “Noise in a phosphorelay drives stochastic entry into sporulation” (updegrove2024altruisticfeedingand pages 14-14) | 10.1126/sciadv.adq0791 (2024) https://doi.org/10.1126/sciadv.adq0791 | Useful environmental/regulatory context; not a core morphology edge |
| spoIVA disruption → causes loss of → heat- and lysozyme-resistant spores | gene disruption → phenotype | SpoIVA (label-only); lysozyme CHEBI:610244? (grounding uncertain); heat resistance (label-only) | Clostridium sporogenes | “Inactivation of spoIVA… resulted in the loss of resistance… to lysozyme and heat treatments”; assays used 80°C for 20 min and 250 µg/mL lysozyme for 10 min (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 4-6) | 10.3389/fmicb.2024.1338751 (2024) https://doi.org/10.3389/fmicb.2024.1338751 | Strong phenotype link; resistance is downstream of morphogenesis rather than morphology itself |
| CotE deletion → abolishes → bead-like coat patterns / alters coat layer localization | protein loss → ultrastructural region | CotE (label-only); coat bead-like layer (label-only) | Bacillus subtilis | “deletion of cotE abolishes the bead-like patterns and alters localization of matrices and the dark smooth layer; cotE-dependent structures are made of CotE polymers” (bauda2024ultrastructureofmacromolecular pages 5-7) | 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Strong, recent ultrastructural evidence |
| spoVID deletion → removes/misorganizes → thin and thick dark coat matrices | protein loss → ultrastructural regions | SpoVID (label-only); coat matrix regions (label-only) | Bacillus subtilis | “Deletion of spoVID removes the thin dark matrix and leads to additional strata of the thick dark matrix” (bauda2024ultrastructureofmacromolecular pages 5-7) | 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Strong, recent ultrastructural evidence |
| safA deletion → abolishes/mislocalizes → thick dark coat matrix | protein loss → ultrastructural region | SafA (label-only); thick dark matrix (label-only) | Bacillus subtilis | “deletion of safA causes the thick dark matrix to be absent or mislocalized as a large aggregate” (bauda2024ultrastructureofmacromolecular pages 5-7) | 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Strong, recent ultrastructural evidence |
| SpoIIIA–SpoIIQ transenvelope tether → contributes to → sporangial/forespore structural organization during engulfment | complex → process/structure | SpoIIIA-SpoIIQ (label-only); engulfment (label-only) | Bacillus subtilis | cryo-ET study identifies “the SpoIIIA-SpoIIQ transenvelope tether” among key structures visualized during sporulation (bauda2024ultrastructureofmacromolecular pages 1-2) | 10.1038/s41467-024-45770-6 (2024) https://doi.org/10.1038/s41467-024-45770-6 | Weak for direct trait curation here: structural relevance clear, but explicit causal edge to “spore shaped” less directly stated in provided context |


*Table: This table summarizes evidence-backed candidate causal edges for curation of the microbial morphology trait 'spore shaped' as endospore-like morphology. It emphasizes experimentally supported regulators, structures, and environmental triggers, with ontology suggestions, taxon scope, and uncertainty notes for TraitMech curation.*

---

## Curation warnings / “do not curate yet” items
1. **Fine-grained coat subregions may not generalize across taxa.** The seven cryo-ET coat regions and bead-like patterns are very well supported in *B. subtilis*, but may not map cleanly to other endospore-formers; curate as Bacillus-specific nodes/edges unless cross-taxon corroboration is added (bauda2024ultrastructureofmacromolecular pages 5-7).
2. **Exosporium-related edges are taxon-restricted.** Exosporium is absent in many endospores; therefore edges involving ExsY/CotY/BxpB/BclA should be modeled under a conditional “exosporium present” branch or annotated as Bacillus cereus group/B. anthracis-specific (mckenney2013thebacillussubtilis pages 11-13).
3. **Correlation vs causation for Ca–DPA and refractivity.** The link between Ca2+/DPA accumulation and refractivity is described as correlated in the reviewed ontogenesis summary; curate with an uncertainty flag unless a primary mechanistic source is added (voitsekhovsky2024peculiaritiesofthe pages 5-7).
4. **Thesis-only evidence should be flagged.** The B. anthracis exosporium thesis provides useful mechanistic statements, but should be treated as supporting/gray literature unless key claims are corroborated with peer-reviewed primary articles (heredia2023interplayofbacillus pages 185-189).

---

## DOI-first bibliography (with URLs and publication dates)

1. **Bauda E, et al.** “Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography.” *Nature Communications* (Feb **2024**). DOI: **10.1038/s41467-024-45770-6**. URL: https://doi.org/10.1038/s41467-024-45770-6 (bauda2024ultrastructureofmacromolecular pages 5-7, bauda2024ultrastructureofmacromolecular pages 2-3)
2. **Nerber HN, et al.** “The small acid-soluble proteins of *Clostridioides difficile* regulate sporulation in a SpoIVB2-dependent manner.” *PLOS Pathogens* (Aug **2024**). DOI: **10.1371/journal.ppat.1012507**. URL: https://doi.org/10.1371/journal.ppat.1012507 (nerber2024thesmallacidsoluble pages 1-2)
3. **Marini E, et al.** “A sporulation signature protease is required for assembly of the spore surface layers, germination and host colonization in *Clostridioides difficile*.” *PLOS Pathogens* (Nov **2023**). DOI: **10.1371/journal.ppat.1011741**. URL: https://doi.org/10.1371/journal.ppat.1011741 (marini2023asporulationsignature pages 2-3)
4. **Kuwana R, et al.** “SpoIVA is an essential morphogenetic protein for the formation of heat- and lysozyme-resistant spores in *Clostridium sporogenes* NBRC 14293.” *Frontiers in Microbiology* (Apr **2024**). DOI: **10.3389/fmicb.2024.1338751**. URL: https://doi.org/10.3389/fmicb.2024.1338751 (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 4-6)
5. **McKenney PT, Driks A, Eichenberger P.** “The *Bacillus subtilis* endospore: assembly and functions of the multilayered coat.” *Nature Reviews Microbiology* (Dec **2013**). DOI: **10.1038/nrmicro2921**. URL: https://doi.org/10.1038/nrmicro2921 (mckenney2013thebacillussubtilis pages 6-7, mckenney2013thebacillussubtilis pages 20-24, mckenney2013thebacillussubtilis pages 24-26, mckenney2013thebacillussubtilis pages 11-13)
6. **Updegrove TB, et al.** “Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity.” *Science Advances* (Oct **2024**). DOI: **10.1126/sciadv.adq0791**. URL: https://doi.org/10.1126/sciadv.adq0791 (updegrove2024altruisticfeedingand pages 14-14)
7. **Cassona CP, et al.** “Spores of *Clostridioides difficile* are toxin delivery vehicles.” *Communications Biology* (Jul **2024**). DOI: **10.1038/s42003-024-06521-x**. URL: https://doi.org/10.1038/s42003-024-06521-x (cassona2024sporesofclostridioides pages 1-2)
8. **Voitsekhovsky VG, et al.** “Peculiarities of the Ontogenesis of Bacilli During Development from a Vegetative Cell to a Spore.” *Mikrobiolohichnyi Zhurnal* (Sep **2024**). DOI: **10.15407/microbiolj86.04.091**. URL: https://doi.org/10.15407/microbiolj86.04.091 (voitsekhovsky2024peculiaritiesofthe pages 5-7)
9. **Heredia JD.** “Interplay of *Bacillus anthracis* spore proteins in the assembly process of the exosporium.” PhD thesis (Year **2023**). DOI: **10.32469/10355/98752**. URL: https://doi.org/10.32469/10355/98752 (heredia2023interplayofbacillus pages 185-189)

---

## Notes for YAML implementation (`data/traits/morphology/spore_shaped.yaml`)
- Consider structuring the causal graph around: **environmental trigger → Spo0A activation → sigma cascade → morphogenetic proteins → envelope layers → spore-shaped morphology**, with optional branches for **exosporium** and for **taxon-specific regulators** (nerber2024thesmallacidsoluble pages 1-2, mckenney2013thebacillussubtilis pages 20-24, marini2023asporulationsignature pages 2-3).
- Treat **resistance phenotypes** (heat/lysozyme) as downstream properties; include them only if the TraitMech schema permits phenotype outcomes linked from morphology nodes (kuwana2024spoivaisan pages 4-6).


References

1. (nerber2024thesmallacidsoluble pages 1-2): Hailee N. Nerber, Marko Baloh, Joshua N. Brehm, and Joseph A. Sorg. The small acid-soluble proteins of clostridioides difficile regulate sporulation in a spoivb2-dependent manner. PLOS Pathogens, 20:e1012507, Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012507, doi:10.1371/journal.ppat.1012507. This article has 12 citations and is from a highest quality peer-reviewed journal.

2. (mckenney2013thebacillussubtilis pages 20-24): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

3. (mckenney2013thebacillussubtilis pages 11-13): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

4. (kuwana2024spoivaisan pages 4-6): Ritsuko Kuwana, Bruno Dupuy, Isabelle Martin-Verstraete, and Hiromu Takamatsu. Spoiva is an essential morphogenetic protein for the formation of heat- and lysozyme-resistant spores in clostridium sporogenes nbrc 14293. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1338751, doi:10.3389/fmicb.2024.1338751. This article has 5 citations and is from a peer-reviewed journal.

5. (kuwana2024spoivaisan pages 1-2): Ritsuko Kuwana, Bruno Dupuy, Isabelle Martin-Verstraete, and Hiromu Takamatsu. Spoiva is an essential morphogenetic protein for the formation of heat- and lysozyme-resistant spores in clostridium sporogenes nbrc 14293. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1338751, doi:10.3389/fmicb.2024.1338751. This article has 5 citations and is from a peer-reviewed journal.

6. (mckenney2013thebacillussubtilis pages 6-7): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

7. (mckenney2013thebacillussubtilis pages 24-26): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

8. (marini2023asporulationsignature pages 2-3): Eleonora Marini, Carmen Olivença, Sara Ramalhete, Andrea Martinez Aguirre, Patrick Ingle, Manuel N. Melo, Wilson Antunes, Nigel P. Minton, Guillem Hernandez, Tiago N. Cordeiro, Joseph A. Sorg, Mónica Serrano, and Adriano O. Henriques. A sporulation signature protease is required for assembly of the spore surface layers, germination and host colonization in clostridioides difficile. PLOS Pathogens, 19:e1011741, Nov 2023. URL: https://doi.org/10.1371/journal.ppat.1011741, doi:10.1371/journal.ppat.1011741. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (mckenney2013thebacillussubtilis media fbb58921): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

10. (mckenney2013thebacillussubtilis media 597936fc): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

11. (cassona2024sporesofclostridioides pages 1-2): Carolina P. Cassona, Sara Ramalhete, Khira Amara, Thomas Candela, Imad Kansau, Cécile Denève-Larrazet, Claire Janoir-Jouveshomme, Luís Jaime Mota, Bruno Dupuy, Mónica Serrano, and Adriano O. Henriques. Spores of clostridioides difficile are toxin delivery vehicles. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06521-x, doi:10.1038/s42003-024-06521-x. This article has 3 citations and is from a peer-reviewed journal.

12. (bauda2024ultrastructureofmacromolecular pages 5-7): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

13. (bauda2024ultrastructureofmacromolecular pages 2-3): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 18 citations and is from a highest quality peer-reviewed journal.

14. (mckenney2013thebacillussubtilis pages 7-9): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

15. (mckenney2013thebacillussubtilis pages 15-17): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

16. (mckenney2013thebacillussubtilis pages 26-27): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 880 citations and is from a highest quality peer-reviewed journal.

17. (voitsekhovsky2024peculiaritiesofthe pages 5-7): V.G. Voitsekhovsky, L.V. Avdeeva, O.B. Balko, and O.I. Balko. Peculiarities of the ontogenesis of bacilli during development from a vegetative cell to a spore. Mikrobiolohichnyi Zhurnal, 86:91-105, Sep 2024. URL: https://doi.org/10.15407/microbiolj86.04.091, doi:10.15407/microbiolj86.04.091. This article has 0 citations.

18. (updegrove2024altruisticfeedingand pages 14-14): Taylor B. Updegrove, Thomas Delerue, Vivek Anantharaman, Hyomoon Cho, Carissa Chan, Thomas Nipper, Hyoyoung Choo-Wosoba, Lisa M. Jenkins, Lixia Zhang, Yijun Su, Hari Shroff, Jiji Chen, Carole A. Bewley, L. Aravind, and Kumaran S. Ramamurthi. Altruistic feeding and cell-cell signaling during bacterial differentiation actively enhance phenotypic heterogeneity. Science Advances, Oct 2024. URL: https://doi.org/10.1126/sciadv.adq0791, doi:10.1126/sciadv.adq0791. This article has 7 citations and is from a highest quality peer-reviewed journal.

19. (heredia2023interplayofbacillus pages 185-189): Jorge Durand Heredia. Interplay of Bacillus anthracis spore proteins in the assembly process of the exosporium. PhD thesis, University of Missouri Libraries, 2023. URL: https://doi.org/10.32469/10355/98752, doi:10.32469/10355/98752.

20. (bauda2024ultrastructureofmacromolecular pages 1-2): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 18 citations and is from a highest quality peer-reviewed journal.