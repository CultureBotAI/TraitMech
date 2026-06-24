---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:40:40.701665'
end_time: '2026-06-18T07:58:50.045207'
duration_seconds: 1089.34
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: flagellated
  trait_identifier: METPO:1000704
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: flagellated
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motile in which an organism possesses flagella for locomotion.
  parent_traits: METPO:1000702
  synonyms: flagella
  evidence_summary: 'DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous
    organelle responsible for motility (Supports flagella as locomotory structures.)'
  causal_graph_summary: 'flagellated_flagellar_motor: 7 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellated
- **METPO identifier:** METPO:1000704
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism possesses flagella for locomotion.
- **Parent traits:** METPO:1000702
- **Synonyms:** flagella
- **Existing evidence:** DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous organelle responsible for motility (Supports flagella as locomotory structures.)
- **Existing causal graph summary:** flagellated_flagellar_motor: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **flagellated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellated.yaml`.

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
- **Trait label:** flagellated
- **METPO identifier:** METPO:1000704
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism possesses flagella for locomotion.
- **Parent traits:** METPO:1000702
- **Synonyms:** flagella
- **Existing evidence:** DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous organelle responsible for motility (Supports flagella as locomotory structures.)
- **Existing causal graph summary:** flagellated_flagellar_motor: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **flagellated** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellated.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **flagellated** (METPO:1000704)

**Trait label:** flagellated  
**METPO:** METPO:1000704  
**Category:** MORPHOLOGY (CLASS)  
**Definition (given):** “A motile in which an organism possesses flagella for locomotion.”

### 0) Executive scope summary (curation-oriented)
The trait **flagellated** is best treated as a **morphological phenotype**: the organism possesses one or more **flagellar filaments** (and associated basal-body motor and hook structures) used for locomotion, typically observed by microscopy or inferred from a complete, functional flagellar assembly/genetic program. Recent reviews emphasize that a bacterial flagellum is a supramolecular organelle with three principal functional parts—**basal body (rotary motor), hook (universal joint), and filament (helical propeller)**—plus accessory features such as caps and junction proteins. (minamino2023structureassemblyand pages 1-3)

**Boundary cases important for curation:**
- **Genomic remnants do not guarantee flagellation:** some strains retain **fliC (flagellin)** and **fliD (cap)** yet are **non-motile** due to missing early operon genes (e.g., fliP–fliM deletions). (marvaud2024clostridioidesdifficileflagella pages 2-5)
- **Nonflagellated taxa may retain subsets of flagellar genes** (e.g., retained fT3SS modules) without assembling flagella (risk of false positive if using gene markers alone). (xiong2023lossofflagellarelated pages 1-2)
- Distinguish from **type IV pili-based twitching motility** and other motility modes; flagella are powered by **ion motive force** through stator complexes, unlike pili retraction motors. (nakamura2024structureanddynamics pages 1-3)

### 1) Key concepts & definitions (current understanding)

#### 1.1 Bacterial flagellum structure
Recent authoritative sources describe a canonical flagellum as consisting of:  
- **Basal body**: includes rings (MS, C-ring, etc.) and the motor/stators. (minamino2023structureassemblyand pages 4-6, nakamura2024structureanddynamics pages 1-3)
- **Hook**: flexible universal joint transmitting torque. (minamino2023structureassemblyand pages 1-3, nakamura2024structureanddynamics pages 6-8)
- **Filament**: long helical propeller assembled from flagellin subunits and a cap. (nakamura2024structureanddynamics pages 6-8)

Minamino & Kinoshita (2023) detail multiple structural subassemblies and stoichiometries useful for mechanistic nodes: MS ring formed by **34 FliF subunits**, C-ring composed of **FliG/FliM/FliN**, and a core export complex **FliP5–FliQ4–FliR1** in the fT3SS export gate. (minamino2023structureassemblyand pages 4-6)

#### 1.2 Assembly and export (fT3SS)
Flagella are built by a dedicated **flagellar type III secretion system (fT3SS)** that exports structural subunits through a narrow channel to the distal tip where polymerization occurs. (minamino2023structureassemblyand pages 1-3)

Assembly includes checkpoint-like transitions, such as hook-length control and substrate switching, mediated by the secreted ruler **FliK** acting through **FlhA/FlhB**. (nakamura2024structureanddynamics pages 6-8)

#### 1.3 Energetics and motor mechanism
Flagellar rotation is powered by **ion motive force** (often **PMF**, sometimes sodium motive force) through stator complexes; MotA/MotB form a transmembrane channel and generate torque via interactions with rotor protein **FliG**. (minamino2023structureassemblyand pages 1-3, nakamura2024structureanddynamics pages 1-3)

#### 1.4 Regulation and behavior (chemotaxis and transcriptional hierarchy)
Motor switching is controlled by chemotaxis signaling: chemoreceptors **Tar/Tsr → CheA kinase → CheY-P**, which binds the C-ring to switch rotation direction; **CheZ** dephosphorylates CheY. (nakamura2024structureanddynamics pages 1-3)

Transcriptional regulation is hierarchical (Salmonella model): **class 1 (flhDC)** initiates the cascade; class 2 includes basal body/hook and regulators (FliA/FlgM); class 3 includes filament/motility/chemotaxis genes, with FlgM inhibiting FliA until hook completion, after which FlgM is secreted and FliA activates late genes. (minamino2023structureassemblyand pages 16-18, minamino2023structureassemblyand media c16510b7)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 High-resolution structural mechanism of switching (2024)
Cryo-EM structures of intact Salmonella basal bodies clarified rotational switching: **CheY-P binding** triggers reversal and is associated with large conformational changes including **180° rotations** of both N- and C-terminal domains of **FliG**. (johnson2024structuralbasisof pages 1-5)

#### 2.2 Quantitative mechanics and new measurement implementations (2024)
A 2024 mBio study introduced an **optical trapping + fluorescence labeling** method for measuring torque–speed relationships in **Pseudomonas aeruginosa** motors with dual stators. It reports distinct speed peaks (61 Hz and 98 Hz), torque around **~1,100 pN·nm**, and a characteristic torque–speed curve with a knee near **~370 Hz** and near-zero torque by **~810 Hz** under their conditions. (wu2024torquespeedrelationshipof pages 17-19, wu2024torquespeedrelationshipof pages 2-5)

#### 2.3 Assembly quality control and chaperoning (2024)
A 2024 Nature Communications paper highlights that **FlhE** functions as a periplasmic chaperone affecting proper assembly and preventing aberrant periplasmic flagella formation; it also recapitulates the ordered assembly sequence and core components (MS ring, C ring, export gate, rod/hook/filament). (halte2024flhefunctionsas pages 1-2)

#### 2.4 Pathogen genomics and regulation in real settings (2024)
In **Clostridioides difficile**, a 2024 review summarizes strain/ribotype variation and phase variation affecting motility: RT078 strains can lose early flagellar regions; deletions of genes **fliP to fliM** are associated with **immobility**; the “flagellar switch” is a **154 bp invertible DNA sequence** flanked by **21 bp** inverted repeats. (marvaud2024clostridioidesdifficileflagella pages 2-5)

### 3) Current applications and real-world implementations

1) **Clinical microbiology / pathogenesis context:** Flagella contribute to motility and host interactions; C. difficile flagella are discussed as a pathogenicity factor and a potential therapeutic/vaccine-relevant structure (review context), while also showing natural variation (some strains non-motile). (marvaud2024clostridioidesdifficileflagella pages 1-2, marvaud2024clostridioidesdifficileflagella pages 2-5)

2) **Biophysical assay implementation:** Optical trapping enables torque–speed measurements without bead tethering, providing a tool for profiling motors across flagellated species, including dual-stator adaptation to different loads/viscosities (e.g., swarming on agar vs liquid). (wu2024torquespeedrelationshipof pages 1-2)

3) **Ecology/biocontrol tradeoffs:** In a nonflagellated antifungal bacterium (Lysobacter enzymogenes), reintroduction/expression of flagellar genes from a related flagellated species (motA/motB/fliE/fleQ) can reduce antifungal weapon synthesis, illustrating pleiotropic tradeoffs relevant to trait evolution and engineering. (xiong2023lossofflagellarelated pages 1-2)

### 4) Expert opinions / authoritative synthesis (evidence-backed)
- Recent ASM EcoSal Plus and Biomolecules reviews treat the bacterial flagellum as a canonical model of a complex self-assembling nanomachine powered by ion motive force and regulated by sensory signal transduction. (minamino2023structureassemblyand pages 1-3, nakamura2024structureanddynamics pages 1-3)
- Current structural consensus supports a stator architecture compatible with a **MotA5B2** stoichiometry and dynamic stator recruitment with mechanical load. (johnson2024structuralbasisof pages 1-5)

### 5) Relevant statistics and data (recent studies)

- **Stator and rotor stoichiometries / cooperativity (2024, cryo-EM):** C-ring comprises ~**34** copies of FliG/FliM/FliN subcomplexes; stators can be recruited up to **~11** depending on load; switching Hill coefficient can be as high as **21** with respect to CheY-P. (johnson2024structuralbasisof pages 1-5)
- **Torque-speed measurements (2024):** P. aeruginosa motor output torque around **~1,100 pN·nm**; rotation-speed distribution peaks at **61 Hz** and **98 Hz**; curve knee **~370 Hz** and near-zero torque by **~810 Hz** (reported for their assay context). (wu2024torquespeedrelationshipof pages 17-19, wu2024torquespeedrelationshipof pages 2-5)
- **Morphology prevalence in a measured population (2024):** in one dataset, **>70%** of cells had a single polar flagellum (remainder 2–3). (wu2024torquespeedrelationshipof pages 17-19)
- **Genomic variation linked to immobility (2024):** deletion of genes **fliP–fliM** in an early operon reported “resulting in immobility” in a C. difficile RT078 strain; in 10 ribotypes producing only CDT, 2 had deletions in F2 and early regions and 7 lacked F2 region; **fliC** and **fliD** were conserved across strains surveyed in that review. (marvaud2024clostridioidesdifficileflagella pages 2-5)

---

## Candidate mechanistic nodes for `flagellated.yaml` (grouped by type)

### A) Phenotype / morphology nodes
- **flagellated** (METPO:1000704)
- flagellum (bacterial-type; label-only)  
- basal body (GO:0009288) (candidate)  
- hook (bacterial flagellar hook; label-only/GO candidate)  
- filament (flagellar filament; label-only)

### B) Macromolecular complexes and structural proteins
- **MS ring**: FliF (34-mer in Salmonella model) (minamino2023structureassemblyand pages 4-6)  
- **C ring / switch complex**: FliG, FliM, FliN (minamino2023structureassemblyand pages 4-6, johnson2024structuralbasisof pages 1-5)  
- **Hook**: FlgE (nakamura2024structureanddynamics pages 6-8)  
- **Hook–filament junction**: FlgK, FlgL (nakamura2024structureanddynamics pages 6-8)  
- **Filament/cap**: FliC (flagellin), FliD (cap) (nakamura2024structureanddynamics pages 6-8, marvaud2024clostridioidesdifficileflagella pages 2-5)

### C) Assembly/export pathway nodes
- **fT3SS export gate**: FlhA, FlhB, FliP/Q/R/(O) (minamino2023structureassemblyand pages 3-4, minamino2023structureassemblyand pages 1-3)  
- export complex stoichiometry node: FliP5–FliQ4–FliR1 (minamino2023structureassemblyand pages 4-6)  
- **ATPase complex for export**: FliH/FliI/FliJ (minamino2023structureassemblyand pages 3-4)  
- **Hook-length ruler / substrate switch**: FliK acting via FlhA/FlhB (nakamura2024structureanddynamics pages 6-8)  
- **Chaperoning/quality control**: FlhE (periplasmic chaperone) (halte2024flhefunctionsas pages 1-2)

### D) Energetics / chemicals
- proton motive force (PMF) (label-only) (minamino2023structureassemblyand pages 1-3)  
- proton (CHEBI:15378) (nakamura2024structureanddynamics pages 1-3)  
- sodium ion (CHEBI:29101) and Na+ gradient/sodium motive force (label-only) (minamino2023structureassemblyand pages 1-3)

### E) Motor/stator and torque generation
- MotA/MotB stator complex (H+-driven) (nakamura2024structureanddynamics pages 1-3)  
- PomA/PomB stator complex (Na+-driven; taxon-specific) (minamino2023structureassemblyand pages 1-3)  
- rotor–stator coupling via FliG (nakamura2024structureanddynamics pages 1-3)

### F) Regulation / signal transduction
- **Transcriptional hierarchy:** flhDC (class 1), FliA (σ28), FlgM (anti-sigma) (minamino2023structureassemblyand pages 16-18, minamino2023structureassemblyand media c16510b7)  
- **Chemotaxis:** Tar/Tsr → CheA → CheY-P; CheZ (nakamura2024structureanddynamics pages 1-3)  
- **Alternative master regulator (taxon-specific):** FleQ (regulated by c-di-GMP) (xiong2023lossofflagellarelated pages 1-2)

---

## Candidate causal edges (evidence-backed table)
The following table is designed to be directly curatable as candidate edges for a TraitMech causal graph.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet / quote | Source | DOI | URL | Notes |
|---|---|---|---|---|---|---|---|
| Flagellar basal body (GO:0009288) | part_of | flagellum / flagellated trait (METPO:1000704) | "The flagellum of *Salmonella enterica* serovar Typhimurium is a supramolecular assembly consisting of at least three distinct functional parts: a basal body ... a hook ... and a filament" (minamino2023structureassemblyand pages 1-3) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Strong scope-defining edge for bacterial flagella. |
| Hook (label-only candidate; GO:0009289 bacterial-type flagellum hook if used) | part_of | flagellum / flagellated trait (METPO:1000704) | "The flagellum ... consist[s] of at least three distinct functional parts: a basal body ... a hook ... and a filament" (minamino2023structureassemblyand pages 1-3) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Structural component of the phenotype. |
| Filament / flagellar filament (GO:0009288 descendant; label-only acceptable) | part_of | flagellum / flagellated trait (METPO:1000704) | "The flagellum ... consist[s] of ... a filament that functions as a helical propeller" (minamino2023structureassemblyand pages 1-3) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Directly ties filament presence to the flagellated morphology. |
| FliF / MS ring protein (UniProt:label-only candidate) | enables_assembly_of | MS ring (label-only candidate) | "MS ring formed by '34 FliF subunits'" (minamino2023structureassemblyand pages 4-6) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Strong bacterial edge; exact UniProt depends on taxon/strain. |
| MS ring (label-only candidate) | houses | flagellar type III secretion export gate / fT3SS (label-only candidate) | "the MS ring comprises 34 copies of FliF and houses the FT3SS" (xiong2023lossofflagellarelated pages 1-2) | Xiong 2023, Microbiology Spectrum | 10.1128/spectrum.04149-22 | https://doi.org/10.1128/spectrum.04149-22 | Supports basal-body-to-export-system organization. |
| FliG/FliM/FliN C ring complex (label-only candidate) | assembles_into | C ring (label-only candidate) | "FliG, FliM, and FliN assemble into the C ring" (minamino2023structureassemblyand pages 4-6) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Strong structural edge. |
| FliG N-terminus (label-only candidate) | binds | FliF C-terminal cytoplasmic domain (label-only candidate) | "FliGN binds directly to the C-terminal cytoplasmic domain of FliF" (minamino2023structureassemblyand pages 4-6) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Useful if graph includes assembly contacts; taxon modeled in *Salmonella*. |
| FliP5-FliQ4-FliR1 complex (label-only candidate) | part_of | flagellar type III secretion system export gate (label-only candidate) | "Core fT3SS export complex: 'FliP5-FliQ4-FliR1 complex' located inside the M-ring pore" (minamino2023structureassemblyand pages 4-6) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Good export-gate node; stoichiometry from structural model. |
| Flagellar type III secretion system (GO:0030694 bacterial-type flagellum-dependent cell motility may be broader; label-only candidate) | exports | flagellar structural subunits (label-only candidate) | "a flagellar type III secretion system (fT3SS) at the base exports structural subunits from the cytoplasm through a narrow central channel to the distal tip where assembly occurs" (minamino2023structureassemblyand pages 1-3) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Central mechanistic edge for trait formation. |
| FlhA/FlhB/FliP/FliQ/FliR/FliO export gate proteins (label-only candidate) | part_of | flagellar type III secretion system (label-only candidate) | "membrane export gate proteins (FlhA, FlhB, FliP/Q/R/O)" (minamino2023structureassemblyand pages 3-4) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Good candidate module node. |
| FliH-FliI-FliJ ATPase complex (label-only candidate) | powers | flagellar protein export by fT3SS (label-only candidate) | "the ATPase ring complex (FliI, with FliH and FliJ) provides ATP hydrolysis for export" (minamino2023structureassemblyand pages 3-4) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Strong mechanistic edge; export rather than rotation. |
| ATP hydrolysis (GO:0016887) | provides_energy_for | flagellar protein export by fT3SS (label-only candidate) | "the ATPase ring complex ... provides ATP hydrolysis for export" (minamino2023structureassemblyand pages 3-4) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Process-level energy edge. |
| FliK (label-only candidate) | measures_and_signals_completion_of | hook length / hook completion (label-only candidate) | "FliK transmits a hook-length signal via interactions with FlhB and FlhA to terminate hook assembly and initiate filament assembly" (nakamura2024structureanddynamics pages 6-8) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Strong bacterial hook-length control edge. |
| FliK (label-only candidate) | triggers_switch_to | filament assembly (GO:0044781 bacterial-type flagellum assembly) | "FliK transmits a hook-length signal via interactions with FlhB and FlhA to terminate hook assembly and initiate filament assembly" (nakamura2024structureanddynamics pages 6-8) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Good substrate-specificity-switch edge. |
| FlgK/FlgL hook-filament junction proteins (label-only candidate) | enable | filament polymerization (label-only candidate) | "the hook–filament junction is formed by 11 FlgK and 11 FlgL subunits acting as an adapter" and "absence of FlgK/FlgL/FliD prevents filament polymerization" (nakamura2024structureanddynamics pages 6-8) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Strong structural/assembly edge. |
| FliD filament cap (label-only candidate) | enables | filament polymerization (label-only candidate) | "flagellin subunits (~30,000) polymerize into a filament aided by a five-subunit FliD cap" (nakamura2024structureanddynamics pages 6-8) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Strong assembly edge. |
| FlgE (label-only candidate) | structural_component_of | hook (label-only candidate) | "hook composed mainly of FlgE" (nakamura2024structureanddynamics pages 6-8) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Can support node inclusion for hook formation. |
| FliC / flagellin (label-only candidate; e.g., UniProt taxon-specific) | polymerizes_into | flagellar filament (label-only candidate) | "filament flagellins FliC" and "flagellin subunits (~30,000) polymerize into a filament" (minamino2023structureassemblyand pages 3-4, nakamura2024structureanddynamics pages 6-8) | Minamino 2023, EcoSal Plus; Nakamura 2024, Biomolecules | 10.1128/ecosalplus.esp-0011-2023; 10.3390/biom14121488 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 ; https://doi.org/10.3390/biom14121488 | Broad bacterial flagellin edge; exact flagellin gene varies by taxon. |
| MotA-MotB stator complex (label-only candidate) | acts_as | transmembrane H+ channel (CHEBI:15378 proton) | "stator units formed by MotA and MotB ... act as a transmembrane H+ channel" (nakamura2024structureanddynamics pages 1-3) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Strong energetics edge for proton-driven motors. |
| Proton motive force (PMF) (label-only candidate) | powers | flagellar rotation / motility (GO:0071973 bacterial-type flagellum-dependent motility) | "the Salmonella motor is powered by proton motive force (PMF) across the membrane" (minamino2023structureassemblyand pages 1-3) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Canonical bacterial energetics edge. |
| Na+ gradient / sodium motive force (CHEBI:29101 sodium(1+)) | powers | flagellar rotation in some bacteria (label-only candidate) | "other bacteria can use Na+ gradients" (minamino2023structureassemblyand pages 1-3) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Broad but weaker/taxon-dependent edge. |
| PomA-PomB stator complex (label-only candidate) | is_a | sodium-dependent flagellar stator (label-only candidate) | "homologous PomA5-PomB2 (Vibrio)" and "Vibrio spp. ... are exclusively driven by sodium-dependent stator units (PomAB)" (minamino2023structureassemblyand pages 1-3, wu2024torquespeedrelationshipof pages 1-2) | Minamino 2023, EcoSal Plus; Wu 2024, mBio | 10.1128/ecosalplus.esp-0011-2023; 10.1128/mbio.00745-24 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 ; https://doi.org/10.1128/mbio.00745-24 | Taxon-specific to sodium-driven systems such as *Vibrio*. |
| H+ conduction through MotA-MotB (label-only candidate) | generates_torque_via | electrostatic interaction with FliG (label-only candidate) | "H+ conduction through MotA-MotB generates torque via electrostatic interactions between MotA and rotor protein FliG" (nakamura2024structureanddynamics pages 1-3) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Strong motor mechanism edge. |
| CheY-P (label-only candidate) | binds | FliM / C ring (label-only candidate) | "CheY-P ... binds with high affinity to FliMN and with low affinity to FliMM and FliN" (minamino2023structureassemblyand pages 4-6); "Directional switching is triggered by the chemotaxis regulator CheY-P binding to FliM" (johnson2024structuralbasisof pages 1-5) | Minamino 2023, EcoSal Plus; Johnson 2024, Nature Microbiology | 10.1128/ecosalplus.esp-0011-2023; 10.1038/s41564-024-01630-z | https://doi.org/10.1128/ecosalplus.esp-0011-2023 ; https://doi.org/10.1038/s41564-024-01630-z | Strong switching edge; binding-site granularity varies by source. |
| CheY-P binding to C ring (label-only candidate) | causes | rotational switching (CCW/CW) (label-only candidate) | "As a result, the C ring switches its conformational state" (minamino2023structureassemblyand pages 4-6) and "Directional switching is triggered by ... CheY-P binding to FliM, causing full reversal of rotation" (johnson2024structuralbasisof pages 1-5) | Minamino 2023, EcoSal Plus; Johnson 2024, Nature Microbiology | 10.1128/ecosalplus.esp-0011-2023; 10.1038/s41564-024-01630-z | https://doi.org/10.1128/ecosalplus.esp-0011-2023 ; https://doi.org/10.1038/s41564-024-01630-z | Strong chemotaxis-to-motor edge. |
| Chemoreceptors Tar/Tsr (UniProt:label-only candidate) | activate_via_CheA_CheY_pathway | flagellar motor switching (label-only candidate) | "transmembrane chemoreceptors (Tar, Tsr) → CheA kinase → phosphorylated CheY, which binds the C-ring to switch rotation direction" (nakamura2024structureanddynamics pages 1-3) | Nakamura 2024, Biomolecules | 10.3390/biom14121488 | https://doi.org/10.3390/biom14121488 | Good higher-level sensory regulation edge. |
| flhDC operon (label-only candidate) | activates_expression_of | class 2 flagellar genes (label-only candidate) | "Figure 12 illustrates ... Class 1 consists of the flhDC operon, which initiates the expression of Class 2 genes" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Figure-derived evidence; curate with note that snippet comes from extracted figure/caption context. |
| Class 2 flagellar genes (label-only candidate) | encode | basal body and hook components (label-only candidate) | "Class 2 genes encode the basal body and hook components" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Useful transcription-to-structure edge. |
| Class 2 flagellar genes (label-only candidate) | encode | FliA / sigma-28 (label-only candidate) | "Class 2 genes encode ... the sigma factor FliA (σ28) and its anti-sigma factor FlgM" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Figure-derived. |
| Class 2 flagellar genes (label-only candidate) | encode | FlgM anti-sigma factor (label-only candidate) | "Class 2 genes encode ... the sigma factor FliA (σ28) and its anti-sigma factor FlgM" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Figure-derived. |
| FlgM (label-only candidate) | inhibits | FliA / sigma-28 (label-only candidate) | "During assembly, FlgM inhibits FliA until the hook is completed" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Strong regulation edge, but from figure/caption extraction. |
| Hook completion (label-only candidate) | enables_secretion_of | FlgM (label-only candidate) | "until the hook is completed, at which point FlgM is secreted" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Figure-derived; mechanistically important export-coupled regulatory edge. |
| FlgM secretion (label-only candidate) | relieves_inhibition_of | FliA / sigma-28 (label-only candidate) | "FlgM is secreted, allowing FliA to activate Class 3 genes" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Figure-derived. |
| FliA / sigma-28 (label-only candidate) | activates_expression_of | class 3 flagellar genes (label-only candidate) | "allowing FliA to activate Class 3 genes responsible for filament formation, motility, and chemotaxis" (minamino2023structureassemblyand media c16510b7) | Minamino 2023, EcoSal Plus | 10.1128/ecosalplus.esp-0011-2023 | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | Strong hierarchy edge. |
| FleQ (label-only candidate) | activates_expression_of | class II flagellar genes (label-only candidate) | "FleQ ... activates transcription of class II genes encoding basal body, motor, and export apparatus components, promoting flagellar assembly and swimming motility" (xiong2023lossofflagellarelated pages 1-2) | Xiong 2023, Microbiology Spectrum | 10.1128/spectrum.04149-22 | https://doi.org/10.1128/spectrum.04149-22 | Taxon-specific regulator for pseudomonads/xanthomonads, not universal bacterial flagella. |
| Loss of genes from fliP to fliM (label-only candidate genomic deletion) | causes | immobility / nonmotile phenotype (label-only candidate) | "a series of genes from fliP to fliM in the early operon were absent ... resulting in immobility" (marvaud2024clostridioidesdifficileflagella pages 2-5) | Marvaud 2024, Int. J. Mol. Sci. | 10.3390/ijms25042202 | https://doi.org/10.3390/ijms25042202 | Boundary-case evidence: gene loss abolishes flagellar function; in *C. difficile*. |
| Loss of flagellar genes (label-only candidate) | causes | nonmotile phenotype (label-only candidate) | "Loss of flagellar genes causes a nonmotile phenotype" (xiong2023lossofflagellarelated pages 1-2) | Xiong 2023, Microbiology Spectrum | 10.1128/spectrum.04149-22 | https://doi.org/10.1128/spectrum.04149-22 | Broad but somewhat generic; useful negative/control edge. |
| Retention of flagellin gene fliC and cap gene fliD (label-only candidate) | does_not_guarantee | motility / flagellated phenotype (METPO:1000704) | "The flagellin fliC and flagellar cap fliD genes were conserved in all strains," yet "C. difficile is mostly a motile bacterium, but some strains could be non-motile" (marvaud2024clostridioidesdifficileflagella pages 2-5) | Marvaud 2024, Int. J. Mol. Sci. | 10.3390/ijms25042202 | https://doi.org/10.3390/ijms25042202 | Important warning/boundary case: single marker genes are insufficient evidence for trait curation. |
| Archaellum / archaeal flagellum analog (label-only candidate) | analogous_to | bacterial flagellum (label-only candidate) | "rotary swimming propellers analogous to bacterial flagella (archaella)" (minamino2023structureassemblyand pages 3-4) | Gaines 2024, Nature Communications | 10.1038/s41467-024-53986-9 | https://doi.org/10.1038/s41467-024-53986-9 | Optional boundary edge if ontology spans Archaea; archaella are functionally analogous but structurally distinct from bacterial flagella, so curate cautiously. |
| ArlI ATPase (label-only candidate) | powers | archaellum rotation/assembly (label-only candidate) | "via the action of a single cytoplasmic ATPase (ArlI)" (minamino2023structureassemblyand pages 3-4) | Gaines 2024, Nature Communications | 10.1038/s41467-024-53986-9 | https://doi.org/10.1038/s41467-024-53986-9 | Include only if trait definition is broadened to archaeal motility appendages; otherwise keep out of main TraitMech graph. |


*Table: This table lists candidate evidence-backed causal edges for curating a TraitMech graph for the microbial morphology trait 'flagellated' (METPO:1000704). It covers structural components, export/assembly, energetics, chemotactic switching, transcriptional hierarchy, and boundary cases where gene loss disrupts motility or visible flagellation.*

---

## Ontology grounding notes
- **GO:** basal body (GO:0009288) is a reasonable anchor node; other bacterial flagellar substructures may require label-only nodes if an exact GO term is uncertain. (minamino2023structureassemblyand pages 1-3, nakamura2024structureanddynamics pages 1-3)
- **CHEBI:** proton (CHEBI:15378), sodium(1+) (CHEBI:29101). (nakamura2024structureanddynamics pages 1-3)
- **Gene/protein identifiers:** exact UniProt IDs are taxon/strain specific; for TraitMech, consider modeling proteins as **gene-family nodes** (e.g., MotA, MotB, FliF) plus optional NCBITaxon constraints.

---

## Warnings / claims to treat as uncertain (do not curate without additional evidence)
1) **Gene-marker shortcuts:** presence of **fliC/fliD** alone should *not* be curated as “flagellated,” as non-motile/nonflagellated strains may retain these late genes while lacking early operons. (marvaud2024clostridioidesdifficileflagella pages 2-5)
2) **Taxon-specific regulators:** **FleQ**-centered regulatory architecture applies to certain proteobacteria (e.g., Pseudomonas/Xanthomonas) and should be curated as conditional (NCBITaxon-scoped) edges. (xiong2023lossofflagellarelated pages 1-2)
3) **Figure-derived regulatory edges:** the FlgM→FliA inhibition and FlgM secretion upon hook completion were extracted from a figure; curate with a note that the evidence is figure/caption-based and confirm in full text if possible. (minamino2023structureassemblyand media c16510b7)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Minamino T, Kinoshita M. **Structure, Assembly, and Function of Flagella Responsible for Bacterial Locomotion.** *EcoSal Plus.* Published Dec 2023. DOI: **10.1128/ecosalplus.esp-0011-2023**. https://doi.org/10.1128/ecosalplus.esp-0011-2023 (minamino2023structureassemblyand pages 1-3, minamino2023structureassemblyand pages 4-6, minamino2023structureassemblyand pages 3-4, minamino2023structureassemblyand pages 16-18)
2. Nakamura S, Minamino T. **Structure and Dynamics of the Bacterial Flagellar Motor Complex.** *Biomolecules.* Published Nov 2024. DOI: **10.3390/biom14121488**. https://doi.org/10.3390/biom14121488 (nakamura2024structureanddynamics pages 1-3, nakamura2024structureanddynamics pages 6-8)
3. Johnson S, et al. **Structural basis of directional switching by the bacterial flagellum.** *Nature Microbiology.* Published Mar 2024. DOI: **10.1038/s41564-024-01630-z**. https://doi.org/10.1038/s41564-024-01630-z (johnson2024structuralbasisof pages 1-5)
4. Halte M, et al. **FlhE functions as a chaperone to prevent formation of periplasmic flagella in Gram-negative bacteria.** *Nature Communications.* Published Jul 2024. DOI: **10.1038/s41467-024-50278-0**. https://doi.org/10.1038/s41467-024-50278-0 (halte2024flhefunctionsas pages 1-2)
5. Wu H, Wu Z, Tian M, Zhang R, Yuan J. **Torque-speed relationship of the flagellar motor with dual-stator systems in Pseudomonas aeruginosa.** *mBio.* Published Dec 2024. DOI: **10.1128/mbio.00745-24**. https://doi.org/10.1128/mbio.00745-24 (wu2024torquespeedrelationshipof pages 1-2, wu2024torquespeedrelationshipof pages 17-19, wu2024torquespeedrelationshipof pages 2-5)
6. Marvaud J-C, Bouttier S, Saunier J, Kansau I. **Clostridioides difficile Flagella.** *International Journal of Molecular Sciences.* Published 12 Feb 2024. DOI: **10.3390/ijms25042202**. https://doi.org/10.3390/ijms25042202 (marvaud2024clostridioidesdifficileflagella pages 1-2, marvaud2024clostridioidesdifficileflagella pages 2-5)
7. Xiong D, et al. **Loss of Flagella-Related Genes Enables a Nonflagellated, Fungal-Predating Bacterium To Strengthen the Synthesis of an Antifungal Weapon.** *Microbiology Spectrum.* Published Feb 2023. DOI: **10.1128/spectrum.04149-22**. https://doi.org/10.1128/spectrum.04149-22 (xiong2023lossofflagellarelated pages 1-2)
8. Kinosita Y, Sowa Y. **Flagellar polymorphism-dependent bacterial swimming motility in a structured environment.** *Biophysics and Physicobiology.* Published May 2023. DOI: **10.2142/biophysico.bppb-v20.0024**. https://doi.org/10.2142/biophysico.bppb-v20.0024 (kinosita2023flagellarpolymorphismdependentbacterial pages 7-8)

---

### Embedded visual evidence
- Figure illustrating the Salmonella flagellar transcriptional hierarchy (Class 1–3; flhDC, FliA, FlgM; FlgM secretion upon hook completion) was extracted for curation support. (minamino2023structureassemblyand media c16510b7)


References

1. (minamino2023structureassemblyand pages 1-3): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 57 citations.

2. (marvaud2024clostridioidesdifficileflagella pages 2-5): Jean-Christophe Marvaud, Sylvie Bouttier, Johanna Saunier, and Imad Kansau. Clostridioides difficile flagella. International Journal of Molecular Sciences, 25:2202, Feb 2024. URL: https://doi.org/10.3390/ijms25042202, doi:10.3390/ijms25042202. This article has 11 citations.

3. (xiong2023lossofflagellarelated pages 1-2): Dan Xiong, Zixiang Yang, Xueting He, Weimei He, Danyu Shen, Lu Wang, Long Lin, Aprodisia Murero, Tohru Minamino, Xiaolong Shao, and Guoliang Qian. Loss of flagella-related genes enables a nonflagellated, fungal-predating bacterium to strengthen the synthesis of an antifungal weapon. Feb 2023. URL: https://doi.org/10.1128/spectrum.04149-22, doi:10.1128/spectrum.04149-22. This article has 5 citations and is from a domain leading peer-reviewed journal.

4. (nakamura2024structureanddynamics pages 1-3): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 26 citations.

5. (minamino2023structureassemblyand pages 4-6): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 57 citations.

6. (nakamura2024structureanddynamics pages 6-8): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 26 citations.

7. (minamino2023structureassemblyand pages 16-18): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 57 citations.

8. (minamino2023structureassemblyand media c16510b7): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 57 citations.

9. (johnson2024structuralbasisof pages 1-5): Steven Johnson, Justin C. Deme, Emily J. Furlong, Joseph J. E. Caesar, Fabienne F. V. Chevance, Kelly T. Hughes, and Susan M. Lea. Structural basis of directional switching by the bacterial flagellum. Nature microbiology, 9:1282-1292, Mar 2024. URL: https://doi.org/10.1038/s41564-024-01630-z, doi:10.1038/s41564-024-01630-z. This article has 59 citations and is from a highest quality peer-reviewed journal.

10. (wu2024torquespeedrelationshipof pages 17-19): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

11. (wu2024torquespeedrelationshipof pages 2-5): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

12. (halte2024flhefunctionsas pages 1-2): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

13. (marvaud2024clostridioidesdifficileflagella pages 1-2): Jean-Christophe Marvaud, Sylvie Bouttier, Johanna Saunier, and Imad Kansau. Clostridioides difficile flagella. International Journal of Molecular Sciences, 25:2202, Feb 2024. URL: https://doi.org/10.3390/ijms25042202, doi:10.3390/ijms25042202. This article has 11 citations.

14. (wu2024torquespeedrelationshipof pages 1-2): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

15. (minamino2023structureassemblyand pages 3-4): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 57 citations.

16. (kinosita2023flagellarpolymorphismdependentbacterial pages 7-8): Yoshiaki Kinosita and Yoshiyuki Sowa. Flagellar polymorphism-dependent bacterial swimming motility in a structured environment. Biophysics and Physicobiology, 20:n/a, May 2023. URL: https://doi.org/10.2142/biophysico.bppb-v20.0024, doi:10.2142/biophysico.bppb-v20.0024. This article has 6 citations.