---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:24:40.523909'
end_time: '2026-08-04T08:35:02.873002'
duration_seconds: 622.35
template_file: templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'flagellated_flagellar_motor: 16 nodes, 13 edges'
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
- **Trait label:** flagellated
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000704
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism possesses flagella for locomotion.
- **Parent traits:** METPO:1000702
- **Synonyms:** flagella
- **Existing evidence:** DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous organelle responsible for motility (Supports flagella as locomotory structures.)
- **Existing causal graph summary:** flagellated_flagellar_motor: 16 nodes, 13 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000704
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism possesses flagella for locomotion.
- **Parent traits:** METPO:1000702
- **Synonyms:** flagella
- **Existing evidence:** DOI:10.3390/biom9070279: bacterial flagellum is a helical filamentous organelle responsible for motility (Supports flagella as locomotory structures.)
- **Existing causal graph summary:** flagellated_flagellar_motor: 16 nodes, 13 edges

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


# Curation report: **flagellated**

## 1. Trait record and recommended scope

- **Trait label:** flagellated
- **Trait identifier:** **METPO:1000704**
- **Category / kind:** MORPHOLOGY / CLASS
- **Parent:** METPO:1000702
- **Reviewed definition supplied:** “A motile in which an organism possesses flagella for locomotion.”

For TraitMech, the operational phenotype should be **possession of at least one morphologically detectable locomotory flagellar appendage**, rather than active movement itself. A bacterial flagellum comprises a basal-body motor, hook, and helical filament; the filament is assembled from thousands of FliC/flagellin subunits and capped by FliD. The hook transmits motor torque to the filament, which acts as a propeller. (nedeljkovic2021bacterialflagellarfilament pages 1-2, minamino2023structureassemblyand pages 22-23)

### Scope boundaries

1. **Flagellated is not equivalent to motile.** A cell may possess an assembled but paralyzed flagellum because its stator, switch, ion motive force, or another motor component is defective. Conversely, surface translocation can be mediated by type-IV pili, surfactants, gliding systems, or growth and therefore does not establish flagellation. In *Pseudomonas aeruginosa*, PA4367 overexpression restored swarming in a Δ*fliA* background without restoring flagella by TEM and did not restore swimming, directly separating a surface-motility assay from flagellar morphology. (lo2016regulationofmotility pages 11-14)
2. **Swimming or soft-agar expansion is functional evidence, not sufficient morphological evidence.** The strongest phenotype annotation should use electron microscopy, flagellin-specific fluorescence, sheared-filament protein analysis, or another direct appendage assay. Motility assays should be represented as downstream observations.
3. **Swarming is compound and assay-specific.** It can require flagella but also surfactants, cell differentiation, surface hydration, and pili. It should not be used as a universal synonym for flagellation. (lo2016regulationofmotility pages 11-14)
4. **Archaella require a separate mechanistic branch.** Archaeal archaella are analogous locomotory appendages but are evolutionarily and mechanistically distinct from bacterial flagella: archaella assemble from the base and use ATP, whereas bacterial flagella assemble distally and use ion motive force for rotation. Whether METPO:1000704 intentionally includes archaella should be settled by ontology policy before adding archaeal mechanisms.
5. **Eukaryotic cilia/flagella are out of scope** for a bacterial flagellar graph. They are microtubule/dynein machines rather than homologues of bacterial flagella.
6. **Periplasmic flagella are included morphologically** if the intended taxonomic scope covers spirochetes, but they need a taxon-specific structural branch rather than assumptions copied from external flagella.

The supplied definition is therefore slightly circular (“A motile…”) and conflates structure with function. A curation-oriented wording would be: **“A microbial cell morphology in which the organism possesses one or more flagellar locomotory appendages.”** Add “whether or not actively rotating under the assay conditions” if METPO permits an editorial note.

## 2. Current mechanistic model

The best-supported bacterial causal chain is:

**flagellar transcriptional program → hook–basal-body assembly → assembly checkpoint and late-gene expression → flagellin export/polymerization → capped filament → ion-driven stator torque → hook-mediated torque transmission → filament rotation and propulsion.**

In the canonical *Salmonella/E. coli* hierarchy, FlhD/FlhC activates class-II genes needed for hook–basal-body construction. FlgM inhibits FliA/σ28 until hook–basal-body completion permits FlgM export; liberated FliA then drives class-III genes including *fliC*. This checkpoint couples morphological development to gene expression. (chilcott2000couplingofflagellar pages 7-8, chilcott2000couplingofflagellar pages 1-1, nedeljkovic2021bacterialflagellarfilament pages 9-10)

The flagellar type-III secretion system contains the membrane export gate FliP/Q/R–FlhA/B and cytoplasmic FliH/I/J complex. It transports structural subunits through the growing organelle. Recent synthesis describes FlhA docking of chaperone–substrate complexes—FlgN–FlgK/L, FliS–FliC, and FliT–FliD—and a FliK/FlhB-dependent switch from hook-type to filament-type export. The export gate can exploit electrochemical energy, with FlhA conducting H⁺ and Na⁺ under studied conditions. (minamino2023structureassemblyand pages 22-23)

FliC polymerization creates the helical filament, while FliD caps its distal end and supports elongation. Presence of the filament is the most direct molecular realization of the target morphology. (nedeljkovic2021bacterialflagellarfilament pages 1-2, nedeljkovic2021bacterialflagellarfilament pages 27-28)

For function, MotAB-family stators convert transmembrane ion flow into torque; many motors are H⁺-driven, whereas PomAB systems in taxa such as marine *Vibrio* are commonly Na⁺-driven. The hook acts as a universal joint, and the filament converts rotation into thrust. These are downstream causes of **flagellar motility**, but stator activity is not required for the narrow structural state “flagellated.” (nedeljkovic2021bacterialflagellarfilament pages 1-2, wu2024torquespeedrelationshipof pages 17-19, minamino2023structureassemblyand pages 22-23)

Chemotaxis regulates behavior rather than appendage presence. CheY-P binds the C-ring protein FliM and biases directional switching. Likewise, c-di-GMP-bound YcgR can alter motor direction and speed through a “backstop brake.” These edges belong downstream of the morphology node unless a taxon-specific pathway also regulates flagellar biogenesis. (mckee2013thesecondmessenger pages 10-11, nedeljkovic2021bacterialflagellarfilament pages 27-28)

## 3. Candidate nodes

### A. Trait and observed structures

- **flagellated:** `METPO:1000704`
- flagellar filament — candidate GO cellular-component grounding; verify the current GO release before YAML insertion
- bacterial-type flagellum — candidate GO cellular-component grounding; verify
- basal body; MS ring; C ring; rod; hook; hook–filament junction; filament cap
- polar flagellation, peritrichous flagellation, lateral flagellation, periplasmic flagellation — label-only phenotype candidates unless an approved morphology ontology term is found

### B. Transcriptional and assembly regulators

- FlhD/FlhC master regulator complex, preferably represented as **FlhD₄C₂** where supported
- FliA / σ28
- FlgM anti-σ28 factor
- FliK hook-length control/export-switch protein
- FlhB substrate-specificity switch component
- FleQ and alternative polar-flagellum regulators — **taxon-specific**, not substitutes for universal FlhDC

### C. Export and assembly machinery

- FliF MS-ring protein
- FliP, FliQ, FliR, FlhA, FlhB export-gate complex
- FliH, FliI, FliJ cytoplasmic ATPase complex
- FliE rod/export adaptor
- FlgB/C/F/G rod proteins; FlgE hook protein
- FlgK/FlgL hook–filament junction proteins
- FliC flagellin
- FliD filament-cap protein
- FliS–FliC, FliT–FliD, and FlgN–FlgK/L chaperone–substrate complexes

### D. Motor, switch, and energetic nodes

- MotA/MotB proton-coupled stator
- PomA/PomB sodium-coupled stator — taxon-specific
- MotC/MotD second stator system in *P. aeruginosa* — taxon-specific
- FliG/FliM/FliN C-ring switch complex
- proton motive force
- sodium motive force
- H⁺ — **CHEBI:15378**
- Na⁺ — **CHEBI:29101**
- torque generation; flagellar rotation; helical propulsion
- external viscous/mechanical load; pH; ion concentration; membrane potential

### E. Signaling and behavioral nodes

- methyl-accepting chemotaxis proteins, CheA, CheW, CheY-P, CheZ
- cyclic di-GMP — commonly grounded as **CHEBI:49537**; verify before committing
- YcgR c-di-GMP receptor/brake
- diguanylate cyclase and phosphodiesterase activities
- PA4367/BifA-like phosphodiesterase in *P. aeruginosa* — strain-specific node
- swimming, run, tumble/reorientation, chemotaxis, swarming, adhesion, biofilm formation

### F. Experimental nodes

- transmission or scanning electron microscopy
- cryo-electron tomography
- flagellin immunofluorescence
- swimming soft-agar assay
- swarming assay
- tethered-cell or bead-rotation assay
- optical trapping/tweezers
- protonophore treatment, sodium depletion, stator deletion, and motor-switch mutants

Protein identifiers should be assigned at the taxon/strain level using UniProt rather than attaching one species’ accession to a generic node. No UniProt, KEGG, Rhea, EC, or MetaCyc identifier should be inferred from a protein name alone.

## 4. Candidate causal edges

The following artifact summarizes the highest-confidence edges and their evidence status.

| subject | predicate | object | evidence type/taxon | DOI | concise supporting snippet | curation status |
|---|---|---|---|---|---|---|
| flhDC operon | activates transcription of | class II flagellar genes | review; *Salmonella enterica*/*Escherichia coli* | https://doi.org/10.1128/mmbr.64.4.694-708.2000 | “The flhDC operon (class 1) initiates the cascade” and FlhD/FlhC activate class II promoters (chilcott2000couplingofflagellar pages 7-8, chilcott2000couplingofflagellar pages 1-1) | strong |
| hook-basal body completion | enables secretion of | FlgM | review; *Salmonella enterica*/*Escherichia coli* | https://doi.org/10.1128/mmbr.64.4.694-708.2000 | “Once the hook-basal body is complete, FlgM is secreted” (chilcott2000couplingofflagellar pages 7-8) | strong |
| FlgM | inhibits | FliA / sigma-28 | review; *Salmonella enterica*/*Escherichia coli* | https://doi.org/10.1128/mmbr.64.4.694-708.2000 | “FlgM protein acts as an anti-σ28 factor” and inhibits class 3 expression until hook-basal body completion (chilcott2000couplingofflagellar pages 7-8, chilcott2000couplingofflagellar pages 1-1) | strong |
| FliA / sigma-28 | activates transcription of | class III / late flagellar genes including fliC | review; peritrichous bacteria | https://doi.org/10.3390/ijms22147521 | “releasing FliA to activate class III genes including flagellin (FliC)” (nedeljkovic2021bacterialflagellarfilament pages 9-10) | strong |
| flagellar T3SS export gate (FliP/FliQ/FliR/FlhA/FlhB) | exports | flagellar structural subunits | review; bacterial flagellum | https://doi.org/10.3390/biom11020186 | “The T3SS is composed of an export gate (FliPQR/FlhA/FlhB)… to export substrate proteins across the inner membrane” (minamino2023structureassemblyand pages 22-23) | strong |
| FliC / flagellin | polymerizes into | flagellar filament | review; bacterial flagellum | https://doi.org/10.3390/ijms22147521 | “The filament consists of thousands of flagellin (FliC) subunits arranged helically” (nedeljkovic2021bacterialflagellarfilament pages 1-2) | strong |
| FliD | promotes elongation/caps | flagellar filament tip | review; bacterial flagellum | https://doi.org/10.3390/ijms22147521 | “ending with a filament cap composed of an oligomer of the protein FliD” and FliD is “implicated in filament elongation mechanisms” (nedeljkovic2021bacterialflagellarfilament pages 1-2, nedeljkovic2021bacterialflagellarfilament pages 27-28) | strong |
| MotAB stator complex | couples ion flux to | torque generation | review; bacterial flagellum | https://doi.org/10.1016/j.tibs.2021.06.005 | “the stator… couples transmembrane ion flux” and the motor is powered by ion motive force (wu2024torquespeedrelationshipof pages 17-19) | strong |
| PomAB stator complex | uses Na+ flux for | torque generation | review; *Vibrio* and related marine bacteria | https://doi.org/10.1016/j.tim.2020.03.010 | “In the presence of sodium, the periplasmic region of the stator…” and Na+-driven flagellar motor energy conversion (wu2024torquespeedrelationshipof pages 17-19) | taxon-specific |
| torque generation by basal body motor | drives rotation of | filament / propulsion | review; *Salmonella enterica* | https://doi.org/10.1128/ecosalplus.esp-0011-2023 | basal body “acts as a bidirectional rotary motor,” filament “functions as a helical propeller that produces propulsion,” hook transmits torque (minamino2023structureassemblyand pages 22-23) | strong |
| CheY-P | binds | FliM | direct/review; chemotaxis in flagellated bacteria | https://doi.org/10.1128/mbio.00189-23 | “all of the FliM molecules in the C-ring… could be bound by the chemotactic response regulator CheY-P” (wu2024torquespeedrelationshipof pages 17-19) | strong |
| CheY-P binding to FliM | switches motor rotation toward | CW state | review; bacterial chemotaxis | https://doi.org/10.1146/annurev-micro-032421-110850 | “CheY-P binds FliM… and switches the flagella” and review evidence that CheY-P to FliM causes CCW→CW switching (wu2024torquespeedrelationshipof pages 17-19) | strong |
| c-di-GMP | activates braking via | YcgR | review; enteric bacteria and others | https://doi.org/10.1128/jb.00501-13 | “YcgR, a c-di-GMP-binding protein, controls flagellar motor direction and speed via a ‘backstop brake’ mechanism” (mckee2013thesecondmessenger pages 10-11, nedeljkovic2021bacterialflagellarfilament pages 27-28) | taxon-specific |
| PA4367 (c-di-GMP phosphodiesterase) overexpression | rescues | swarming motility in ΔfliA without restoring flagella | direct experiment; *Pseudomonas aeruginosa* PAO1 | https://doi.org/10.1371/journal.pone.0155397 | “TEM… showed that PA4367 overexpression in ΔfliA mutants did not restore flagella structure, yet swarming (but not swimming) motility was rescued” (lo2016regulationofmotility pages 11-14) | strong |
| presence of flagella | is not equivalent to | all motility phenotypes | direct experiment; *Pseudomonas aeruginosa* PAO1 | https://doi.org/10.1371/journal.pone.0155397 | rescue of swarming “did not restore flagella structure,” distinguishing flagellation from some surface-motility outputs (lo2016regulationofmotility pages 11-14) | strong |
| archaellum | is distinct from | bacterial flagellum | review; Archaea vs Bacteria | https://doi.org/10.1093/femsre/fuaa006 | “archaella… use ATP for motility, while flagella use ion-motive force” and are distinct propulsive nanomachines (nedeljkovic2021bacterialflagellarfilament pages 1-2) | uncertain |


*Table: This table compiles the strongest curation-ready causal edges for the microbial trait flagellated, emphasizing mechanism, assembly, regulation, energetics, and boundary conditions. It is designed to support TraitMech curation by distinguishing broadly supported edges from taxon-specific or boundary-case claims.*

### Additional YAML-oriented edges

| Subject | Predicate | Object | Evidence and proposed status |
|---|---|---|---|
| FliK-dependent hook-length checkpoint | triggers | FlhB/FlhA export-specificity remodeling | The 2023 review describes FliK-dependent termination and FlhB-associated remodeling that enables filament assembly; curate as **canonical enteric model**, not universal. (minamino2023structureassemblyand pages 22-23) |
| FlhA docking platform | recruits | FlgN–FlgK/L, FliS–FliC, FliT–FliD complexes | Directly described in the 2023 structural synthesis; strong but nomenclature/stoichiometry should follow the source organism. (minamino2023structureassemblyand pages 22-23) |
| hook | transmits torque to | filament | The hook is described as a universal joint between motor and helical propeller; strong structural-function edge. (minamino2023structureassemblyand pages 22-23) |
| filament rotation | causes | swimming propulsion | Strong for a functional, rotating flagellum in liquid; annotate dependence on fluid, load, filament geometry, and motor energization. (nedeljkovic2021bacterialflagellarfilament pages 1-2, minamino2023structureassemblyand pages 22-23) |
| counterclockwise rotation | promotes | bundled smooth swimming | Supported for canonical peritrichous bacteria; **do not generalize** to monotrichous/polar systems. (nedeljkovic2021bacterialflagellarfilament pages 1-2) |
| clockwise rotation | promotes | bundle disruption/tumbling | Supported for canonical peritrichous bacteria; **taxon and flagellar-arrangement specific**. (nedeljkovic2021bacterialflagellarfilament pages 1-2) |
| elevated c-di-GMP | inhibits or redirects | flagellar motor output through YcgR | Mechanistically supported in enteric systems; encode with taxon context because c-di-GMP effectors differ among organisms. (mckee2013thesecondmessenger pages 10-11, nedeljkovic2021bacterialflagellarfilament pages 27-28) |
| FliA | regulates | PA4367 phosphodiesterase expression | Direct RNA-seq/reporter evidence in *P. aeruginosa* PAO1; taxon-specific. (lo2016regulationofmotility pages 11-14) |
| PA4367 overexpression in Δ*fliA* | restores | swarming without restoring flagellar structure | Direct perturbation and TEM evidence; valuable negative-control edge demonstrating trait/assay separation. (lo2016regulationofmotility pages 11-14) |

## 5. Recent developments and quantitative evidence

### 2023: assembly at near-atomic mechanistic resolution

Minamino and Kinoshita’s December 2023 synthesis integrates cryo-EM structures into an atomic-level model of the *Salmonella* apparatus. Particularly useful for TraitMech are the chaperone–substrate docking relationships, the FliK/FlhB assembly checkpoint, and the dual-energy characteristics of the export machinery. The review also emphasizes a remaining gap: the complete atomic mechanism transmitting FliM-bound chemotaxis signals to cooperative FliG/C-ring remodeling is not resolved. (minamino2023structureassemblyand pages 22-23)

### 2023: adaptive switch stoichiometry

A 2023 fluorescence study used **34 FliG molecules** as a reference and estimated averages of **45 FliM molecules in clockwise motors and 58 in counterclockwise motors**. The finding supports adaptive C-ring remodeling and indicates that switch stoichiometry is not a single invariant number. It should inform a quantitative motor subgraph, but not the binary morphology trait itself.

### 2024: dual-stator mechanics under load

A December 2024 *mBio* study used optical trapping and fluorescence to examine the *P. aeruginosa* polar motor with MotAB and MotCD. Reported motor output was approximately **1,100 pN·nm**; acquisition used **5–10 kHz** sampling, and experiments varied Ficoll concentration to alter load. MotAB showed slip-bond behavior, whereas MotCD showed catch-bond-like load dependence; wild-type torque was approximately the additive output of the two stator systems. This supports an environment/load → stator occupancy/stability → torque branch, but it is specific to *P. aeruginosa* and should not be projected onto every flagellated bacterium. (wu2024torquespeedrelationshipof pages 17-19)

### 2024: chemotaxis diversity

Recent authoritative reviews caution against treating the canonical *E. coli* CheY-P→FliM scheme as a complete description of all bacteria. Chemotaxis systems vary in array architecture, sensor location, protein composition, motor wiring, and adaptation mechanisms. Thus, “CheY-P binds FliM and changes rotational bias” is a strong canonical edge, whereas any universal mapping from attractant to a fixed CW/CCW outcome requires taxon context.

### 2024: flagellotropic phages

Flagellotropic phages exploit flagella and, in some systems, active rotation to encounter or reach the cell surface. This gives flagella potential utility in phage-based selection or control, but receptor use and rotation dependence vary strongly among phages. It should be represented as a host–phage interaction module, not as part of the core cause of flagellation.

## 6. Applications and real-world relevance

1. **Clinical and agricultural pathogenesis.** Flagella can promote migration through mucus or tissue, initial surface contact, adhesion, biofilm development, and colonization. These effects are organism- and infection-stage-specific; flagella can also expose immunostimulatory flagellin. The filament has documented roles beyond locomotion, including adhesion and biofilm formation. (nedeljkovic2021bacterialflagellarfilament pages 1-2)
2. **Anti-virulence development.** Candidate intervention points include flagellar transcription, fT3SS assembly, stator ion conduction, motor switching, and c-di-GMP control. These are primarily research and preclinical strategies; broad clinical implementation should not be claimed from the retrieved evidence.
3. **Phage biocontrol.** Flagellotropic phages may select for loss or impairment of motility, potentially trading phage resistance against colonization fitness. The outcome is phage–host specific and requires empirical validation.
4. **Flagellin biotechnology.** Flagellin/filament structures are used in antigen display, vaccine-adjuvant research, and engineered supramolecular materials. This application derives from flagellin’s polymerization and immunostimulatory properties rather than from the binary morphology annotation. (nedeljkovic2021bacterialflagellarfilament pages 1-2)
5. **Microscale mechanics and biosensing.** Tethered-cell, bead-rotation, fluorescence, and optical-tweezer assays use the motor as a model rotary nanomachine. The 2024 dual-stator work demonstrates a practical high-frequency optical method for measuring torque–speed relationships across load conditions. (wu2024torquespeedrelationshipof pages 17-19)
6. **Ecology and biogeochemistry.** Flagellar motility permits navigation of nutrient, oxygen, redox, salinity, and host-derived gradients. However, the ecological benefit is conditional on spatial heterogeneity and the energetic cost of synthesis and operation.

## 7. Recommended initial graph architecture

A compact first release can extend the existing 16-node/13-edge graph with four modules:

1. **Morphogenesis:** FlhDC → class-II program → basal body/export gate → hook → assembly checkpoint → FliA late program → FliC/FliD → filament → `METPO:1000704`.
2. **Energetics:** proton or sodium motive force → MotAB/PomAB → torque → hook → filament rotation → swimming.
3. **Control:** chemotaxis pathway → CheY-P → FliM/C-ring switching; c-di-GMP → YcgR → reduced/altered motor output.
4. **Observation:** filament → EM/fluorescence-positive; active rotation → tethered-cell/bead-rotation-positive; propulsion → swimming-assay-positive. Keep these observations separate so that a motor-defective but visibly flagellated mutant remains correctly classified.

Only the **morphogenesis module through assembled filament** should be treated as constitutive causation of the morphology trait. Energetics, chemotaxis, and propulsion are functional downstream modules.

## 8. Claims not yet safe to curate

- Do not encode **flagellated ↔ motile** as an equivalence.
- Do not infer flagellation solely from a swarming halo, genome annotation, or presence of one flagellar gene.
- Do not make FlhDC universal; polar systems and many taxa use different regulatory hierarchies.
- Do not make H⁺ the universal motor fuel; Na⁺ and dual/alternative stators occur.
- Do not universalize the *E. coli/Salmonella* CCW-run/CW-tumble mapping to polar or periplasmic motors.
- Do not merge archaella with bacterial flagella without an explicit ontology decision.
- Do not treat c-di-GMP as acting exclusively through YcgR or always abolishing flagellation; it can affect transcription, assembly, motor output, pili, matrix, and biofilms through different effectors.
- Do not curate virulence, adhesion, or biofilm formation as inevitable consequences of flagellation. These are conditional, taxon-specific relationships.
- Do not assign generic protein nodes species-specific UniProt accessions.
- Treat torque values, stator stoichiometry, and load responses as organism- and assay-specific quantitative annotations, not universal constants.

## 9. DOI-first bibliography

1. Minamino T, Kinoshita M. **Structure, Assembly, and Function of Flagella Responsible for Bacterial Locomotion.** *EcoSal Plus*. Published December 2023. DOI: [10.1128/ecosalplus.esp-0011-2023](https://doi.org/10.1128/ecosalplus.esp-0011-2023). (minamino2023structureassemblyand pages 22-23)
2. Wu H, Wu Z, Tian M, Zhang R, Yuan J. **Torque-speed relationship of the flagellar motor with dual-stator systems in Pseudomonas aeruginosa.** *mBio*. Published December 2024. DOI: [10.1128/mbio.00745-24](https://doi.org/10.1128/mbio.00745-24). (wu2024torquespeedrelationshipof pages 17-19)
3. Nedeljković M, Sastre D, Sundberg E. **Bacterial Flagellar Filament: A Supramolecular Multifunctional Nanostructure.** *International Journal of Molecular Sciences*. Published July 2021. DOI: [10.3390/ijms22147521](https://doi.org/10.3390/ijms22147521). (nedeljkovic2021bacterialflagellarfilament pages 1-2, nedeljkovic2021bacterialflagellarfilament pages 27-28, nedeljkovic2021bacterialflagellarfilament pages 9-10)
4. Halte M, Erhardt M. **Protein Export via the Type III Secretion System of the Bacterial Flagellum.** *Biomolecules*. Published January 2021. DOI: [10.3390/biom11020186](https://doi.org/10.3390/biom11020186).
5. Chilcott GS, Hughes KT. **Coupling of Flagellar Gene Expression to Flagellar Assembly in Salmonella enterica Serovar Typhimurium and Escherichia coli.** *Microbiology and Molecular Biology Reviews*. Published December 2000. DOI: [10.1128/MMBR.64.4.694-708.2000](https://doi.org/10.1128/MMBR.64.4.694-708.2000). (chilcott2000couplingofflagellar pages 7-8, chilcott2000couplingofflagellar pages 1-1)
6. Lo Y-L et al. **Regulation of Motility and Phenazine Pigment Production by FliA Is Cyclic-di-GMP Dependent in Pseudomonas aeruginosa PAO1.** *PLoS ONE*. Published May 2016. DOI: [10.1371/journal.pone.0155397](https://doi.org/10.1371/journal.pone.0155397). (lo2016regulationofmotility pages 11-14, lo2016regulationofmotility pages 14-15)
7. McKee RW et al. **The Second Messenger Cyclic Di-GMP Regulates Clostridium difficile Toxin Production by Controlling Expression of sigD.** *Journal of Bacteriology*. Published November 2013. DOI: [10.1128/JB.00501-13](https://doi.org/10.1128/JB.00501-13). (mckee2013thesecondmessenger pages 10-11)
8. Tao A, Liu G, Zhang R, Yuan J. **Precise Measurement of the Stoichiometry of the Adaptive Bacterial Flagellar Switch.** *mBio*. Published April 2023. DOI: [10.1128/mbio.00189-23](https://doi.org/10.1128/mbio.00189-23).
9. Muok AR, Olsthoorn FA, Briegel A. **Unpacking Alternative Features of the Bacterial Chemotaxis System.** *Annual Review of Microbiology*. Published 2024. DOI: [10.1146/annurev-micro-032421-110850](https://doi.org/10.1146/annurev-micro-032421-110850).
10. Beeby M et al. **Propulsive nanomachines: the convergent evolution of archaella, flagella, and cilia.** *FEMS Microbiology Reviews*. Published 2020. DOI: [10.1093/femsre/fuaa006](https://doi.org/10.1093/femsre/fuaa006).

**Curation recommendation:** adopt the assembly-to-filament edges first; retain rotation, chemotaxis, c-di-GMP, ecology, and applications as linked but explicitly conditional modules. This preserves the distinction between the morphology `METPO:1000704` and the physiological capacity for flagellum-driven motility.

References

1. (nedeljkovic2021bacterialflagellarfilament pages 1-2): Marko Nedeljković, Diego Sastre, and Eric Sundberg. Bacterial flagellar filament: a supramolecular multifunctional nanostructure. International Journal of Molecular Sciences, 22:7521, Jul 2021. URL: https://doi.org/10.3390/ijms22147521, doi:10.3390/ijms22147521. This article has 121 citations.

2. (minamino2023structureassemblyand pages 22-23): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 61 citations.

3. (lo2016regulationofmotility pages 11-14): Yi-Ling Lo, Lunda Shen, Chih-Hsuan Chang, Manish Bhuwan, Cheng-Hsun Chiu, and Hwan-You Chang. Regulation of motility and phenazine pigment production by flia is cyclic-di-gmp dependent in pseudomonas aeruginosa pao1. PLoS ONE, 11:e0155397, May 2016. URL: https://doi.org/10.1371/journal.pone.0155397, doi:10.1371/journal.pone.0155397. This article has 47 citations and is from a peer-reviewed journal.

4. (chilcott2000couplingofflagellar pages 7-8): Gavin S. Chilcott and Kelly T. Hughes. Coupling of flagellar gene expression to flagellar assembly in salmonella enterica serovar typhimurium andescherichia coli. Microbiology and Molecular Biology Reviews, 64:694-708, Dec 2000. URL: https://doi.org/10.1128/mmbr.64.4.694-708.2000, doi:10.1128/mmbr.64.4.694-708.2000. This article has 909 citations and is from a domain leading peer-reviewed journal.

5. (chilcott2000couplingofflagellar pages 1-1): Gavin S. Chilcott and Kelly T. Hughes. Coupling of flagellar gene expression to flagellar assembly in salmonella enterica serovar typhimurium andescherichia coli. Microbiology and Molecular Biology Reviews, 64:694-708, Dec 2000. URL: https://doi.org/10.1128/mmbr.64.4.694-708.2000, doi:10.1128/mmbr.64.4.694-708.2000. This article has 909 citations and is from a domain leading peer-reviewed journal.

6. (nedeljkovic2021bacterialflagellarfilament pages 9-10): Marko Nedeljković, Diego Sastre, and Eric Sundberg. Bacterial flagellar filament: a supramolecular multifunctional nanostructure. International Journal of Molecular Sciences, 22:7521, Jul 2021. URL: https://doi.org/10.3390/ijms22147521, doi:10.3390/ijms22147521. This article has 121 citations.

7. (nedeljkovic2021bacterialflagellarfilament pages 27-28): Marko Nedeljković, Diego Sastre, and Eric Sundberg. Bacterial flagellar filament: a supramolecular multifunctional nanostructure. International Journal of Molecular Sciences, 22:7521, Jul 2021. URL: https://doi.org/10.3390/ijms22147521, doi:10.3390/ijms22147521. This article has 121 citations.

8. (wu2024torquespeedrelationshipof pages 17-19): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (mckee2013thesecondmessenger pages 10-11): Robert W. McKee, Mihnea R. Mangalea, Erin B. Purcell, Erin K. Borchardt, and Rita Tamayo. The second messenger cyclic di-gmp regulates clostridium difficile toxin production by controlling expression of <i>sigd</i>. Nov 2013. URL: https://doi.org/10.1128/jb.00501-13, doi:10.1128/jb.00501-13. This article has 169 citations and is from a peer-reviewed journal.

10. (lo2016regulationofmotility pages 14-15): Yi-Ling Lo, Lunda Shen, Chih-Hsuan Chang, Manish Bhuwan, Cheng-Hsun Chiu, and Hwan-You Chang. Regulation of motility and phenazine pigment production by flia is cyclic-di-gmp dependent in pseudomonas aeruginosa pao1. PLoS ONE, 11:e0155397, May 2016. URL: https://doi.org/10.1371/journal.pone.0155397, doi:10.1371/journal.pone.0155397. This article has 47 citations and is from a peer-reviewed journal.