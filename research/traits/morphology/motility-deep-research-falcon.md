---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:04:36.410724'
end_time: '2026-08-04T09:12:31.700100'
duration_seconds: 475.29
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: motility
  trait_identifier: METPO:1000701
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: motility
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype in which an organism has the capability to move independently
    through its environment, typically by means of flagella, pili, gliding mechanisms,
    or other locomotory structures.
  parent_traits: METPO:1000059
  synonyms: Morphology.cell morphology.motility
  evidence_summary: 'DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria
    to move around (Supports bacterial motility as a phenotype mediated by multiple
    molecular machines and physical mechanisms.)'
  causal_graph_summary: 'motility_locomotion_machinery: 12 nodes, 11 edges'
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
- **Trait label:** motility
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000701
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype in which an organism has the capability to move independently through its environment, typically by means of flagella, pili, gliding mechanisms, or other locomotory structures.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.motility
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria to move around (Supports bacterial motility as a phenotype mediated by multiple molecular machines and physical mechanisms.)
- **Existing causal graph summary:** motility_locomotion_machinery: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motility.yaml`.

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
- **Trait label:** motility
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000701
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype in which an organism has the capability to move independently through its environment, typically by means of flagella, pili, gliding mechanisms, or other locomotory structures.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.motility
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria to move around (Supports bacterial motility as a phenotype mediated by multiple molecular machines and physical mechanisms.)
- **Existing causal graph summary:** motility_locomotion_machinery: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motility.yaml`.

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


# Curation-focused research report: microbial motility

## Executive summary

**Target:** `METPO:1000701` (“motility”); category MORPHOLOGY; class; parent `METPO:1000059`.

For TraitMech, motility should mean the **intrinsic capacity for active, self-generated translocation**, not merely observed displacement. It includes flagellar swimming, flagellar swarming, type-IV-pilus (T4P) twitching, and independently powered gliding systems. Chemotaxis is a directional-control process layered onto motility; passive advection, rainfall transport, animal-mediated transport, and microbial hitchhiking are movement but not this trait. Growth-driven colony spreading, sliding, appendage presence without demonstrated function, and Brownian displacement should also remain outside the core definition.

The strongest graph backbone is:

1. ion motive force → stator ion flux → flagellar torque/rotation → filament propulsion → motility;
2. ATP hydrolysis by PilB/PilT → T4P extension/retraction → substrate-coupled cell translocation → twitching motility;
3. environmental and regulatory modifiers—including surface hydrophilicity and c-di-GMP-linked regulation—modulate those machines in specific taxa and assays.

## 1. Trait scope and boundaries

### Operational definition

The supplied definition is consistent with current mechanistic understanding: an organism has motility when it can move independently through its environment using a biological propulsion apparatus. Active bacterial movement includes flagellar swimming/swarming and T4P twitching, whereas passive movement can arise from rainfall, protists, nematodes, or hitchhiking on another microbe’s appendage (Alexandre, October 2025; DOI URL: https://doi.org/10.1128/aem.00246-25). (alexandre2025movementofbacteria pages 1-2)

### Included phenotypes

- **Swimming:** individual-cell movement through liquid, usually driven by rotating flagella.
- **Swarming:** coordinated flagellum-dependent surface movement on hydrated semisolid media; it is a composite phenotype influenced by cell density, surfactants, differentiation, chemotaxis, growth, and agar concentration.
- **Twitching:** non-flagellar surface translocation driven by repeated T4P extension, substrate attachment, and retraction.
- **Gliding:** smooth active surface translocation without external flagella; because unrelated gliding machines exist, this should be represented by mechanism-specific child branches rather than one universal machinery edge.
- **Archaeal swimming:** conceptually included when driven by archaella, but bacterial flagellar proteins must not be projected onto archaea.

### Excluded or separately modeled boundary cases

- **Chemotaxis/taxis:** chemotaxis is “the ability to sense chemical gradients and actively direct motility along them,” so it controls direction rather than establishing propulsion capacity. Surface twitching *Pseudomonas aeruginosa* can use spatial sensing, whereas canonical swimming bacteria generally use temporal sensing. These should be regulatory edges, not synonyms for motility (Wheeler et al., published 2 September 2024; https://doi.org/10.1038/s41564-024-01729-3). (wheeler2024individualbacterialcells pages 1-2)
- **Passive transport:** advection, rainfall, sediment movement, vectors, or hitchhiking do not demonstrate independent locomotion. (alexandre2025movementofbacteria pages 1-2)
- **Growth and colony expansion:** increased colony diameter may reflect growth, sliding, wetting, or active motility. A growth control and/or single-cell tracking is required.
- **Biofilm formation and adhesion:** these are associated functions or consequences of motility machines, not motility itself.
- **Appendage presence:** flagella or pili visualized by microscopy support machinery formation, but a functional motility assay is still needed.
- **Magnetotaxis, buoyancy regulation, and passive settling:** these require explicit evidence of energy-dependent self-translocation before inclusion under this term.

## 2. Candidate causal-graph nodes

Identifiers below are limited to mappings that can be stated confidently. Label-only nodes are preferable to unverified CURIEs.

### Trait and biological-process nodes

- Motility — `METPO:1000701`; target node.
- Parent trait — `METPO:1000059`.
- Bacterial-type flagellum-dependent cell motility — `GO:0071973`.
- Bacterial-type flagellum-dependent swarming motility — `GO:0071978`.
- Twitching motility — `GO:0071977`.
- Chemotaxis — `GO:0006935`; regulatory/navigation process, not equivalent to motility.
- Pilus organization — `GO:0043711`.
- Bacterial-type flagellum assembly — `GO:0044780`.
- Gliding motility — retain as a label unless the repository’s ontology release is checked for the exact mechanism-specific term.

### Flagellar machinery and localization nodes

- Flagellar basal body; rotor; stator; hook; filament; hook–filament junction; filament cap.
- MotA, MotB; sodium-driven homologous stators PomA, PomB.
- FliF MS ring; FliG/FliM/FliN C ring; FlgE hook; FliC/FljB flagellin; FliD cap; FlgK/FlgL junction; FliK ruler; FlhA/FlhB export-switch proteins.
- Cytoplasmic membrane — `GO:0005886` is usable as a general cellular-component grounding, though bacterial-envelope-specific ontology terms may be preferable locally.
- Peptidoglycan layer — label or verified GO/ChEBI mapping according to graph conventions.
- Flagellar type III secretion system — label-only composite node pending ontology-version verification.

The 2024 structural review describes a basal body, hook, and filament: the basal body is powered by an electrochemical H⁺ or Na⁺ gradient, the hook transfers rotational force as a universal joint, and the filament is the propeller. In *E. coli* and *Salmonella*, MotA–MotB conducts H⁺ and generates torque through interaction with FliG (Nakamura and Minamino, published 22 November 2024; https://doi.org/10.3390/biom14121488). (nakamura2024structureanddynamics pages 1-3)

### T4P machinery nodes

- Type IV pilus machine; T4P filament.
- PilA major pilin; minor pilins FimU, PilE, PilV, PilW, PilX.
- PilB extension ATPase; PilT and PilU retraction ATPases.
- PilC inner-membrane platform; PilQ secretin; PilM/PilN/PilO/PilP alignment complex.
- PilY1 adhesin/mechanosensor; PilZ regulatory protein; PlzR regulator.
- Pilus–substrate attachment; pilus extension; pilus retraction.

In *P. aeruginosa*, PilB assembles and PilT/PilU disassemble T4P, while PilC coordinates the motor. At least 40 proteins are associated with T4P functions in this organism (Hendrix et al., accepted 16 September 2024; https://doi.org/10.1038/s41467-024-52732-5). (hendrix2024plzrregulatestype pages 1-2)

### Chemotaxis and regulatory nodes

- Chemoreceptor/MCP; CheA kinase; CheW; CheY and CheY-P; CheZ; CheR; CheB.
- c-di-GMP — `CHEBI:49537`.
- ATP — `CHEBI:15422`; ADP — `CHEBI:16761`.
- Proton — `CHEBI:15378`; sodium ion — `CHEBI:29101`.
- Proton motive force and sodium motive force — label-only energetic-state nodes.
- PlzR–PilZ binding; PilZ–PilB regulation.

CheY-P binds FliM/FliN, alters the FliG–MotA interaction, and switches motor rotation from counterclockwise to clockwise. This is a steering edge downstream of chemosensing, not a core “creates motility” edge. (nakamura2024structureanddynamics pages 12-14, nakamura2024structureanddynamics pages 1-3)

### Environmental, experimental, and assay nodes

- Liquid medium; hydrated semisolid surface; solid substrate.
- Agar concentration; viscosity; external mechanical load.
- Surface hydrophilicity; polystyrene; tissue-culture-treated polystyrene; glass.
- Bile salts; detergent exposure; polymyxin B.
- Nutrient availability; pH; temperature; salinity.
- Swimming-zone assay; swarming-zone assay; interstitial twitching stab assay; microscopy/single-cell tracking; microfluidic gradient assay; TEM/cryo-ET.

Surface chemistry deserves an explicit experimental-factor branch. Bile salts enhanced twitching by altering surface physicochemical properties rather than by a demonstrated envelope-stress response; hydrophilic glass and treated polystyrene promoted twitching directly (O’Hara et al., published 28 August 2024; https://doi.org/10.1128/msphere.00390-24). (ohara2024surfacehydrophilicitypromotes pages 1-2)

### Taxon/context nodes

Recommended taxon labels for edge qualifiers include *Escherichia coli*, *Salmonella enterica*, *Pseudomonas aeruginosa*, *Acinetobacter baumannii*, *Acinetobacter nosocomialis*, *Xanthomonas albilineans*, *Helicobacter pylori*, *Myxococcus xanthus*, *Vibrio* spp., and spirochetes. Exact `NCBITaxon` CURIEs should be resolved programmatically against NCBI Taxonomy rather than entered from memory.

## 3. Candidate evidence-backed causal edges

The following table is the recommended high-level prioritization.

| priority | subject | predicate | object | taxon/context | evidence strength |
|---|---|---|---|---|---|
| High | ion motive force (H+ or Na+) | powers | flagellar basal body / rotary motor rotation | Broad flagellated bacteria; especially *E. coli*/*Salmonella* reviews and structures (nakamura2024structureanddynamics pages 1-3, nakamura2024structureanddynamics pages 12-14) | Strong, broadly conserved |
| High | MotA–MotB stator complex | converts ion flux into | torque / flagellar motor rotation | Broad flagellated bacteria; proton-driven stator emphasized in *E. coli*/*Salmonella* (nakamura2024structureanddynamics pages 1-3, nakamura2024structureanddynamics pages 12-14) | Strong, broadly conserved |
| High | flagellar motor rotation | enables | swimming motility | Broad flagellated bacteria (nakamura2024structureanddynamics pages 1-3, antani2024reassessingthestandard pages 1-3) | Strong, broadly conserved |
| High | CheY-P | switches | flagellar motor rotation direction (CCW↔CW) | Canonical chemotaxis in *E. coli*/*Salmonella*; steering not motility machinery per se (nakamura2024structureanddynamics pages 1-3, nakamura2024structureanddynamics pages 12-14) | Strong, but regulation of direction rather than core capacity |
| High | PilB ATPase | drives | T4P extension / pilus assembly | *Pseudomonas aeruginosa* and broadly T4P systems (hendrix2024plzrregulatestype pages 1-2, ohara2024surfacehydrophilicitypromotes pages 1-2) | Strong, broadly conserved across T4P taxa |
| High | PilT ATPase | drives | T4P retraction / pilus disassembly | *Pseudomonas aeruginosa* and broadly T4P systems (guo2024pily1regulatesthe pages 1-2, hendrix2024plzrregulatestype pages 1-2, ohara2024surfacehydrophilicitypromotes pages 1-2) | Strong, broadly conserved across T4P taxa |
| High | recurrent T4P extension–retraction cycles | power | twitching motility | Broad T4P-mediated surface motility; explicitly reviewed and assayed in pathogens (ohara2024surfacehydrophilicitypromotes pages 1-2, guo2024pily1regulatesthe pages 1-2) | Strong, broadly conserved across T4P taxa |
| Medium | hydrophilic surface | promotes | twitching motility | Assay/material context: glass and tissue-culture-treated polystyrene; *Acinetobacter* spp. and *P. aeruginosa* (ohara2024surfacehydrophilicitypromotes pages 1-2) | Strong but assay- and surface-specific |
| Medium | bile salts / detergents | increase via altered surface hydrophilicity | twitching motility | Assay context in *A. nosocomialis*, *A. baumannii*, *P. aeruginosa* on LB/polystyrene (ohara2024surfacehydrophilicitypromotes pages 1-2) | Strong but environmental/assay-specific |
| Medium | PlzR | binds | PilZ | *Pseudomonas aeruginosa* (hendrix2024plzrregulatestype pages 1-2, hendrix2024plzrregulatestype pages 2-3) | Strong, taxon-specific |
| Medium | PilZ | regulates | PilB ATPase | *Pseudomonas aeruginosa* (hendrix2024plzrregulatestype pages 1-2, hendrix2024plzrregulatestype pages 2-3) | Strong, taxon-specific |
| Medium | PlzR overexpression | reduces / inhibits | T4P assembly | *Pseudomonas aeruginosa*; no pili detected in overexpression context (hendrix2024plzrregulatestype pages 2-3) | Strong, taxon-specific perturbation |
| Medium | reduced T4P assembly | decreases | twitching motility | *Pseudomonas aeruginosa*; overexpression reduced twitching-zone diameter 63% (1.40 to 0.51 cm) (hendrix2024plzrregulatestype pages 2-3) | Strong, taxon-specific perturbation |
| Medium | PilY1–minor pilin / PilQ interplay | regulates | T4P machine conformation / pilus dynamics | *Pseudomonas aeruginosa* structural model (guo2024pily1regulatesthe pages 1-2) | Moderate; mechanistic model, taxon-specific |
| Medium | virB11 deletion | causes loss of | flagella formation | *Xanthomonas albilineans* mutant ΔvirB11 (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6) | Strong, taxon-specific perturbation |
| Medium | virB11 deletion | causes loss of | type IV pilus morphogenesis | *Xanthomonas albilineans* mutant ΔvirB11 (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6) | Strong, taxon-specific perturbation |
| Medium | loss of flagella formation | abolishes | swimming motility | *Xanthomonas albilineans* ΔvirB11 (li2024virb11atraffic pages 1-2) | Strong, taxon-specific perturbation |
| Medium | loss of T4P morphogenesis | abolishes | twitching motility | *Xanthomonas albilineans* ΔvirB11 (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6) | Strong, taxon-specific perturbation |
| Low | virB11 deletion | reduces | swarming motility | *Xanthomonas albilineans* semisolid 0.6% agar assay; integrates flagella, pili, chemotaxis (li2024virb11atraffic pages 5-6) | Moderate; composite phenotype |
| Low | spatial sensing across cell body | directs | twitching chemotaxis on surfaces | *Pseudomonas aeruginosa*; chemotaxis behavior, not core motility capacity (wheeler2024individualbacterialcells pages 1-2) | Strong for behavior, but outside core motility trait |
| Low | active motility | contributes to | virulence / colonization | Multiple pathogens and plant-associated bacteria (matilla2023targetingmotilityand pages 1-2, li2024virb11atraffic pages 1-2, ohara2024surfacehydrophilicitypromotes pages 1-2) | Moderate; biologically important but downstream and context-dependent |


*Table: This table prioritizes candidate causal edges for curating microbial motility into a TraitMech-style graph. It separates broadly conserved core machinery from taxon-specific regulatory and perturbational edges, helping curators decide what to include first.*

### Detailed edge evidence

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| Ion motive force across cytoplasmic membrane | powers | flagellar rotary motor | “a membrane-embedded rotary motor fueled by an ion motive force”; the basal body is “powered by a transmembrane electrochemical gradient” of H⁺ or Na⁺. DOI: https://doi.org/10.3390/biom14121488 (22 Nov 2024). (nakamura2024structureanddynamics pages 1-3) | **Curate.** Broadly conserved, but retain H⁺- versus Na⁺-dependent alternatives rather than asserting both for every taxon. |
| MotA–MotB H⁺ channel | generates | flagellar torque | MotA–MotB “can act as a transmembrane H⁺ channel that conducts H⁺ through the channel to generate torque by electrostatic interactions between MotA and FliG.” (nakamura2024structureanddynamics pages 1-3) | **Curate.** Strong for proton-driven *E. coli/Salmonella*-type motors. |
| MotA C-terminal region | interacts_with | FliG C-ring region | “The C-terminal domains of the MotA5 ring interact with FliG…to power flagellar motor rotation.” (nakamura2024structureanddynamics pages 12-14) | **Curate with taxon/model qualifier.** Structural mechanism may vary in detail. |
| Flagellar rotation | drives | swimming motility | Rotating flagella enable bacteria to swim; the filament functions as the propeller and hook transfers force. (nakamura2024structureanddynamics pages 1-3) | **Curate.** Core mechanistic edge. |
| FlgE hook | transfers | motor rotation to filament | The hook “works as a universal joint that transfers the rotational force” to the helical filament. (nakamura2024structureanddynamics pages 1-3) | **Curate.** |
| CCW rotation and flagellar bundling | enables | straight swimming | In *Salmonella*, CCW motors bundle normal filaments, “enabling the Salmonella cell to swim straight.” (nakamura2024structureanddynamics pages 6-8) | **Curate only as *Salmonella/E. coli*-like peritrichous model.** Not universal. |
| CW switching | disrupts bundle and causes | tumble/reorientation | Switching CCW→CW changes filament form and disrupts the bundle, “enabling the cell to tumble.” (nakamura2024structureanddynamics pages 6-8) | **Taxon-specific.** Do not apply to polar flagellates such as *H. pylori*. |
| CheY-P | causes | motor direction switch | “CheY-P binds to FliM and FliN…resulting in…a switch…from CCW to CW.” (nakamura2024structureanddynamics pages 12-14) | **Curate as chemotaxis regulation**, separate from basal motility capacity. |
| PilB ATPase | drives | T4P extension/assembly | “the ATPase PilB provides the energy for pili extension.” DOI: https://doi.org/10.1038/s41467-024-52732-5 (2024). (hendrix2024plzrregulatestype pages 2-3) | **Curate.** Broad T4P mechanism, with homolog-specific qualifiers where necessary. |
| PilT ATPase | drives | T4P retraction/disassembly | PilB and PilT “polymerize and depolymerize pilins into or from the T4P filament, respectively.” DOI: https://doi.org/10.1128/msphere.00390-24 (28 Aug 2024). (ohara2024surfacehydrophilicitypromotes pages 1-2) | **Curate.** PilU may provide auxiliary retraction in some taxa. |
| Extended T4P attachment plus retraction | pulls | cell toward attachment point | “When the tip…attaches to a solid substratum, the retraction…moves a bacterium toward the point of attachment.” (ohara2024surfacehydrophilicitypromotes pages 1-2) | **Curate.** Direct physical mechanism of twitching. |
| Repeated T4P extension–retraction | powers | twitching motility | “recurrent cycles…of extension and retraction…powers this form of bacterial surface motility.” (ohara2024surfacehydrophilicitypromotes pages 1-2) | **Curate.** Core T4P branch. |
| Hydrophilic surface | promotes | twitching motility | “bacteria displayed increased twitching on hydrophilic surfaces such as…glass and tissue culture-treated polystyrene.” (ohara2024surfacehydrophilicitypromotes pages 1-2) | **Curate as experimental/environmental modifier**, not a universal biological requirement. |
| Bile salts/detergents | increase via surface hydrophilicity | twitching-zone expansion | Bile salts enabled *A. nosocomialis* twitching in LB and enhanced *A. baumannii* and *P. aeruginosa*; the effect arose from altered surface properties. (ohara2024surfacehydrophilicitypromotes pages 1-2) | **Curate cautiously.** Assay- and material-specific; do not encode as direct intracellular activation. |
| PlzR | binds | PilZ | Authors report PlzR “directly binding the T4P chaperone PilZ.” DOI: https://doi.org/10.1038/s41467-024-52732-5. (hendrix2024plzrregulatestype pages 1-2, hendrix2024plzrregulatestype pages 2-3) | **Curate for *P. aeruginosa*.** |
| PilZ | regulates/interacts_with | PilB | PilZ–PilB interaction was positive in bacterial two-hybrid analysis; PilB supplies extension energy. (hendrix2024plzrregulatestype pages 2-3) | **Curate for *P. aeruginosa*.** Predicate should distinguish physical interaction from functional regulation. |
| PlzR overexpression | inhibits | T4P assembly | No pili were detected after PlzR expression, indicating “complete inhibition of T4P assembly.” (hendrix2024plzrregulatestype pages 2-3) | **Curate as perturbation edge**, not normal physiological directionality. |
| PlzR overexpression | decreases | twitching motility | Twitching-zone diameter fell from 1.40 ± 0.18 cm to 0.51 ± 0.12 cm, a 63% reduction. (hendrix2024plzrregulatestype pages 2-3) | **Curate with overexpression and 1% agar qualifiers.** Swimming and swarming also decreased, so pleiotropy is possible. |
| c-di-GMP | induces promoter activity of | plzR | Elevated c-di-GMP significantly increased activity of the promoter upstream of *plzR*. (hendrix2024plzrregulatestype pages 2-3) | **Potentially curate.** The downstream statement that PlzR physiologically couples T4P to c-di-GMP remains partly interpretive. |
| PilY1 | participates in | T4P gatekeeping/dynamics | PilY1 is modeled as blocking the PilQ secretin; PilQ–PilY1/minor-pilin interplay is proposed to optimize T4P conformations. DOI: https://doi.org/10.1038/s41467-024-53638-y (accepted 16 Oct 2024). (guo2024pily1regulatesthe pages 1-2) | **Uncertain/model edge.** Structural inference is explicitly hypothetical. |
| virB11 deletion | causes loss of | flagella and T4P morphology | Δ*virB11* “failed to develop flagella formation and type IV pilus morphology.” DOI: https://doi.org/10.1111/mpp.70001 (2024). (li2024virb11atraffic pages 1-2) | **Curate only for *X. albilineans*.** Complementation details for pilus morphology require scrutiny because one excerpt reports the complemented strain lacking visible pili. |
| virB11 deletion | abolishes | swimming and twitching | Δ*virB11* showed “a loss in swimming and twitching motility,” without discernible growth impact. (li2024virb11atraffic pages 1-2) | **Curate as strong taxon-specific perturbation.** Growth independence strengthens interpretation. |
| virB11 deletion | reduces | swarming | On 0.6% agar at 28°C for five days, wild type reached 1.66 cm versus 1.03 cm for Δ*virB11* (p<0.0001). (li2024virb11atraffic pages 5-6) | **Curate cautiously.** Swarming is composite and the mutant alters flagella, pili, and chemotaxis genes. |
| virB11 deletion | downregulates | chemotaxis genes | Δ*virB11* downregulated *cheA, cheW, cheY, cheR,* and *cheB*; RNA-seq identified 11 chemotaxis-associated DEGs. (li2024virb11atraffic pages 5-6) | **Curate as expression association**, not necessarily direct transcriptional regulation. |
| Motility/chemotaxis interference | can reduce | pathogen virulence | Saturating the rhizosphere with 1 mM malate reduced *Ralstonia pseudosolanacearum* disease severity by 40–50%; this perturbs a chemotactic gradient rather than the motor itself. DOI: https://doi.org/10.1111/1751-7915.14306 (received 13 Jun 2023). (matilla2023targetingmotilityand pages 1-2) | **Application edge, not core trait mechanism.** Indirect and pathosystem-specific. |

## 4. Recent developments and current understanding

### High-resolution flagellar-motor structure

The major 2024 advance is integration of cryo-EM structures into a rotary mechanism. The proton-driven stator is a MotA₅MotB₂ complex; inward H⁺ movement is proposed to rotate the MotA ring relative to MotB, and MotA–FliG interactions transmit torque to the rotor. The review estimates approximately 42 Å spacing between adjacent FliG subunits and a roughly 46 Å arc for a 72° MotA-ring step, providing a structural-scale correspondence, although direct observation of stator rotation remains an unresolved experimental need. (nakamura2024structureanddynamics pages 3-4, nakamura2024structureanddynamics pages 12-14)

The same work quantifies the *Salmonella* machine: approximately 30 proteins contribute to the flagellum; the hook contains about 120 FlgE subunits and is maintained near 55 nm; a filament can reach about 15 µm and contain roughly 30,000 flagellin subunits; and peritrichous *E. coli/Salmonella* typically carry about 5–10 flagella per cell. These values are useful descriptors, but they should not become universal constraints. (nakamura2024structureanddynamics pages 1-3, nakamura2024structureanddynamics pages 6-8)

### In-situ T4P architecture

Cryo-electron tomography in 2024 resolved a sevenfold cage-like *P. aeruginosa* T4P machine spanning the envelope. PilQ forms the outer-membrane secretin; PilP/O/N/M form an alignment subcomplex; PilC coordinates ATPase-driven assembly/disassembly; and a roughly 5.5-nm pilus occupies the central channel. PilY1 appears as a gatekeeping structure, but the detailed conformational mechanism remains a model rather than a fully tested causal chain. (guo2024pily1regulatesthe pages 1-2)

### c-di-GMP-linked control of T4P

Hendrix et al. identified PlzR through a gain-of-function phage-resistance screen. PlzR bound PilZ, disturbed PilB-dependent assembly, eliminated detectable pili during overexpression, and reduced twitching-zone diameter by 63%. The *plzR* promoter responded to c-di-GMP, suggesting a route by which a sessility-associated second messenger may suppress T4P function. The overexpression design means physiological dosage and breadth across strains remain open questions. (hendrix2024plzrregulatestype pages 1-2, hendrix2024plzrregulatestype pages 2-3)

### Surface physicochemistry as a causal assay variable

O’Hara et al. showed that apparent twitching can change because detergents alter substrate hydrophilicity. This is important for both biology and curation: agar formulation and plate material are active causal variables, not neutral metadata. Hydrophilic tissue surfaces or implants could similarly influence T4P activity, but direct in-vivo extrapolation requires validation. (ohara2024surfacehydrophilicitypromotes pages 1-2)

### Spatial sensing during twitching chemotaxis

Massively parallel tracking and microfluidics showed that surface-attached *P. aeruginosa* can compare concentration across its cell length. The reported illustrative speeds—about 2,000 µm min⁻¹ for flagellar swimming versus 0.2 µm min⁻¹ for pili-based twitching—explain why temporal sensing is advantageous for fast swimmers while spatial sensing can serve slow surface movers. This revises the prevailing assumption that bacteria are necessarily too small for spatial gradient sensing. (wheeler2024individualbacterialcells pages 1-2)

## 5. Applications and real-world implementations

### Anti-virulence strategies

Motility and chemotaxis are being considered anti-infective targets because they can impair host access or colonization without directly inhibiting growth. This may impose different selection pressures from bactericidal antibiotics, although reduced evolutionary pressure should not be assumed without competition and resistance experiments. Chemotaxis genes occur in about half of surveyed bacterial and archaeal genomes, and nine of the ten most important phytopathogens cited by Matilla and Krell possess them. (matilla2023targetingmotilityand pages 1-2)

Examples include gradient masking in plant disease: 1 mM malate lowered *R. pseudosolanacearum* disease severity by 40–50%. In *P. aeruginosa*, T4P are simultaneously motility devices, adhesins, biofilm determinants, virulence factors, and phage receptors; therefore, drugs or engineered phages targeting T4P could affect several infection stages but may also select receptor-loss resistance. (hendrix2024plzrregulatestype pages 1-2, matilla2023targetingmotilityand pages 1-2)

### Clinical materials and infection control

Surface hydrophilicity alters twitching by *Acinetobacter* and *Pseudomonas*. This provides a mechanistic basis for testing implant coatings, catheter materials, wound surfaces, and tissue-culture plastics for their effects on T4P-mediated colonization. The 2024 evidence is laboratory-based; it motivates material design but is not yet a clinical implementation claim. (ohara2024surfacehydrophilicitypromotes pages 1-2)

### Plant pathology and agriculture

In the sugarcane pathogen *X. albilineans*, VirB11 loss eliminated swimming and twitching, reduced swarming and virulence, and did not measurably alter growth. VirB11 or its downstream appendage-biogenesis network is therefore a candidate control point, but VirB11 is a secretion-system ATPase with pleiotropic functions, making target specificity important. (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6)

### Phage biotechnology

T4P-dependent phages use pili as receptors. PlzR expression inhibited adsorption of such phages by blocking T4P assembly, while lipopolysaccharide-dependent phages retained infectivity. This has direct relevance to phage therapy and to avoiding phage losses in bacteria-based food or biotechnology processes. (hendrix2024plzrregulatestype pages 1-2, hendrix2024plzrregulatestype pages 2-3)

## 6. Expert analysis and recommended TraitMech architecture

Authoritative reviews converge on a **modular**, not monolithic, representation. The existing 12-node/11-edge locomotion-machinery graph should be expanded into parallel branches:

1. **Flagellar propulsion module:** ion motive force → stator ion channel → torque → rotor → hook → filament → swimming.
2. **T4P module:** ATP → PilB/PilT → extension/retraction → adhesion point → cell displacement → twitching.
3. **Mechanism-specific gliding modules:** T9SS-, focal-adhesion-, or other machinery-specific branches; avoid one generic gliding motor.
4. **Directional-control module:** chemoreceptor → CheA/CheW → CheY-P → motor switching or polarity control → biased migration.
5. **Environmental/assay module:** medium, viscosity, agar, wetness, surface chemistry, temperature, and ion availability modify observed expression.
6. **Downstream outcome module:** colonization, biofilm initiation, virulence, dispersal, and resource acquisition.

This design prevents three common errors: treating chemotaxis as propulsion, treating appendage genes as universally sufficient, and treating plate-zone diameter as a direct measure of single-cell locomotion.

## 7. Warnings—claims not yet ready for broad curation

1. **Do not universalize the *E. coli/Salmonella* run–tumble mechanism.** Polar flagellates use different forward/backward or run–reverse strategies; *H. pylori*, for example, runs forward with CCW and backward with CW rotation. Flagellar motility can reach approximately 10–50 body lengths s⁻¹, but this is a range rather than a universal trait value. (antani2024reassessingthestandard pages 1-3)
2. **Do not equate swarming-zone expansion with flagellar propulsion alone.** Growth, pili, chemotaxis, surfactants, agar concentration, hydration, and incubation duration can all contribute. The *X. albilineans* Δ*virB11* swarming edge is therefore composite. (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6)
3. **Do not encode bile salts as a direct intracellular twitching activator.** Current evidence supports alteration of surface hydrophilicity. (ohara2024surfacehydrophilicitypromotes pages 1-2)
4. **Keep PilY1 gatekeeping uncertain.** The 2024 study explicitly presents a hypothetical structural model. (guo2024pily1regulatesthe pages 1-2)
5. **Treat PlzR effects as overexpression-specific until endogenous perturbations establish physiological effect size.** The quantitative reduction is compelling, but overexpression also reduced swimming and swarming. (hendrix2024plzrregulatestype pages 2-3)
6. **Do not infer direct VirB11 transcriptional control from differential expression.** VirB11 deletion changes appendage formation and numerous transcripts; indirect stress or regulatory effects remain possible. (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6)
7. **Resolve the reported pilus-complementation inconsistency before curating rescue.** One excerpt states both Δ*virB11* and the complemented strain lacked visible pilus morphology, despite broader restoration claims. (li2024virb11atraffic pages 5-6)
8. **Do not project bacterial flagellar GO terms onto archaella.** These are evolutionarily and structurally distinct machines.
9. **Do not infer phenotype from gene presence alone.** Expression, assembly, energetic state, environment, and regulatory inhibition determine whether machinery is functional.
10. **Validate all CURIEs against the ontology versions used by TraitMech.** Label-only nodes are safer than invented or obsolete identifiers.

## DOI-first bibliography

1. Nakamura S, Minamino T. “Structure and Dynamics of the Bacterial Flagellar Motor Complex.” *Biomolecules* 14, 1488. Published 22 November 2024. https://doi.org/10.3390/biom14121488. (nakamura2024structureanddynamics pages 3-4, nakamura2024structureanddynamics pages 12-14, nakamura2024structureanddynamics pages 1-3, nakamura2024structureanddynamics pages 6-8)
2. Guo S et al. “PilY1 regulates the dynamic architecture of the type IV pilus machine in Pseudomonas aeruginosa.” *Nature Communications* 15, 9382. Accepted 16 October 2024. https://doi.org/10.1038/s41467-024-53638-y. (guo2024pily1regulatesthe pages 1-2)
3. Hendrix H et al. “PlzR regulates type IV pili assembly in Pseudomonas aeruginosa via PilZ binding.” *Nature Communications* 15, 8717. Accepted 16 September 2024. https://doi.org/10.1038/s41467-024-52732-5. (hendrix2024plzrregulatestype pages 1-2, hendrix2024plzrregulatestype pages 2-3)
4. O’Hara MT et al. “Surface hydrophilicity promotes bacterial twitching motility.” *mSphere* 9. Published 28 August 2024. https://doi.org/10.1128/msphere.00390-24. (ohara2024surfacehydrophilicitypromotes pages 1-2)
5. Wheeler JHR, Foster KR, Durham WM. “Individual bacterial cells can use spatial sensing of chemical gradients to direct chemotaxis on surfaces.” *Nature Microbiology* 9:2308–2322. Published 2 September 2024. https://doi.org/10.1038/s41564-024-01729-3. (wheeler2024individualbacterialcells pages 1-2)
6. Li M et al. “VirB11, a traffic ATPase, mediated flagella assembly and type IV pilus morphogenesis to control the motility and virulence of Xanthomonas albilineans.” *Molecular Plant Pathology* 25:e70001. Accepted 13 August 2024. https://doi.org/10.1111/mpp.70001. (li2024virb11atraffic pages 1-2, li2024virb11atraffic pages 5-6)
7. Antani JD et al. “Reassessing the Standard Chemotaxis Framework for Understanding Biased Migration in Helicobacter pylori.” *Annual Review of Chemical and Biomolecular Engineering* 15:51–62. July 2024. https://doi.org/10.1146/annurev-chembioeng-100722-114625. (antani2024reassessingthestandard pages 1-3)
8. Matilla MA, Krell T. “Targeting motility and chemotaxis as a strategy to combat bacterial pathogens.” *Microbial Biotechnology* 16:2205–2211. Received 13 June 2023. https://doi.org/10.1111/1751-7915.14306. (matilla2023targetingmotilityand pages 1-2)
9. Wong GCL et al. “Roadmap on emerging concepts in the physical biology of bacterial biofilms: from surface sensing to community formation.” *Physical Biology* 18:051501. June 2021. https://doi.org/10.1088/1478-3975/abdc0e. (wong2021roadmaponemerging pages 48-49)
10. Alexandre G. “Movement of bacteria in the soil and the rhizosphere.” *Applied and Environmental Microbiology* 91. October 2025. https://doi.org/10.1128/aem.00246-25. Used principally for current scope distinctions. (alexandre2025movementofbacteria pages 1-2)

References

1. (alexandre2025movementofbacteria pages 1-2): Gladys Alexandre. Movement of bacteria in the soil and the rhizosphere. Applied and Environmental Microbiology, Oct 2025. URL: https://doi.org/10.1128/aem.00246-25, doi:10.1128/aem.00246-25. This article has 10 citations and is from a peer-reviewed journal.

2. (wheeler2024individualbacterialcells pages 1-2): James H. R. Wheeler, Kevin R. Foster, and William M. Durham. Individual bacterial cells can use spatial sensing of chemical gradients to direct chemotaxis on surfaces. Nature Microbiology, 9:2308-2322, Sep 2024. URL: https://doi.org/10.1038/s41564-024-01729-3, doi:10.1038/s41564-024-01729-3. This article has 34 citations and is from a highest quality peer-reviewed journal.

3. (nakamura2024structureanddynamics pages 1-3): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 30 citations.

4. (hendrix2024plzrregulatestype pages 1-2): Hanne Hendrix, Annabel Itterbeek, Hannelore Longin, Lize Delanghe, Eveline Vriens, Marta Vallino, Eveline-Marie Lammens, Farhana Haque, Ahmed Yusuf, Jean-Paul Noben, Maarten Boon, Matthias D. Koch, Vera van Noort, and Rob Lavigne. Plzr regulates type iv pili assembly in pseudomonas aeruginosa via pilz binding. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52732-5, doi:10.1038/s41467-024-52732-5. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (nakamura2024structureanddynamics pages 12-14): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 30 citations.

6. (ohara2024surfacehydrophilicitypromotes pages 1-2): Megan T. O'Hara, Tori M. Shimozono, Keane J. Dye, David Harris, and Zhaomin Yang. Surface hydrophilicity promotes bacterial twitching motility. mSphere, Sep 2024. URL: https://doi.org/10.1128/msphere.00390-24, doi:10.1128/msphere.00390-24. This article has 13 citations and is from a peer-reviewed journal.

7. (antani2024reassessingthestandard pages 1-3): Jyot D. Antani, Aakansha Shaji, Rachit Gupta, and Pushkar P. Lele. Reassessing the standard chemotaxis framework for understanding biased migration in helicobacter pylori. Annual Review of Chemical and Biomolecular Engineering, 15:51-62, Jul 2024. URL: https://doi.org/10.1146/annurev-chembioeng-100722-114625, doi:10.1146/annurev-chembioeng-100722-114625. This article has 8 citations and is from a peer-reviewed journal.

8. (guo2024pily1regulatesthe pages 1-2): Shuaiqi Guo, Yunjie Chang, Yves V. Brun, P. L. Howell, Lori L. Burrows, and Jun Liu. Pily1 regulates the dynamic architecture of the type iv pilus machine in pseudomonas aeruginosa. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53638-y, doi:10.1038/s41467-024-53638-y. This article has 47 citations and is from a highest quality peer-reviewed journal.

9. (hendrix2024plzrregulatestype pages 2-3): Hanne Hendrix, Annabel Itterbeek, Hannelore Longin, Lize Delanghe, Eveline Vriens, Marta Vallino, Eveline-Marie Lammens, Farhana Haque, Ahmed Yusuf, Jean-Paul Noben, Maarten Boon, Matthias D. Koch, Vera van Noort, and Rob Lavigne. Plzr regulates type iv pili assembly in pseudomonas aeruginosa via pilz binding. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52732-5, doi:10.1038/s41467-024-52732-5. This article has 20 citations and is from a highest quality peer-reviewed journal.

10. (li2024virb11atraffic pages 1-2): Meilin Li, Liya Xiong, Wenhan Chen, YiSha Li, Abdullah Khan, Charles A. Powell, Baoshan Chen, and Muqing Zhang. Virb11, a traffic atpase, mediated flagella assembly and type iv pilus morphogenesis to control the motility and virulence of xanthomonas albilineans. Molecular Plant Pathology, Sep 2024. URL: https://doi.org/10.1111/mpp.70001, doi:10.1111/mpp.70001. This article has 4 citations and is from a peer-reviewed journal.

11. (li2024virb11atraffic pages 5-6): Meilin Li, Liya Xiong, Wenhan Chen, YiSha Li, Abdullah Khan, Charles A. Powell, Baoshan Chen, and Muqing Zhang. Virb11, a traffic atpase, mediated flagella assembly and type iv pilus morphogenesis to control the motility and virulence of xanthomonas albilineans. Molecular Plant Pathology, Sep 2024. URL: https://doi.org/10.1111/mpp.70001, doi:10.1111/mpp.70001. This article has 4 citations and is from a peer-reviewed journal.

12. (matilla2023targetingmotilityand pages 1-2): Miguel A. Matilla and Tino Krell. Targeting motility and chemotaxis as a strategy to combat bacterial pathogens. Microbial Biotechnology, 16:2205-2211, Jun 2023. URL: https://doi.org/10.1111/1751-7915.14306, doi:10.1111/1751-7915.14306. This article has 32 citations and is from a peer-reviewed journal.

13. (nakamura2024structureanddynamics pages 6-8): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 30 citations.

14. (nakamura2024structureanddynamics pages 3-4): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 30 citations.

15. (wong2021roadmaponemerging pages 48-49): Gerard C L Wong, Jyot D Antani, Pushkar P Lele, Jing Chen, Beiyan Nan, Marco J Kühn, Alexandre Persat, Jean-Louis Bru, Nina Molin Høyland-Kroghsbo, Albert Siryaporn, Jacinta C Conrad, Francesco Carrara, Yutaka Yawata, Roman Stocker, Yves V Brun, Gregory B Whitfield, Calvin K Lee, Jaime de Anda, William C Schmidt, Ramin Golestanian, George A O’Toole, Kyle A Floyd, Fitnat H Yildiz, Shuai Yang, Fan Jin, Masanori Toyofuku, Leo Eberl, Nobuhiko Nomura, Lori A Zacharoff, Mohamed Y El-Naggar, Sibel Ebru Yalcin, Nikhil S Malvankar, Mauricio D Rojas-Andrade, Allon I Hochbaum, Jing Yan, Howard A Stone, Ned S Wingreen, Bonnie L Bassler, Yilin Wu, Haoran Xu, Knut Drescher, and Jörn Dunkel. Roadmap on emerging concepts in the physical biology of bacterial biofilms: from surface sensing to community formation. Physical Biology, 18:051501, Jun 2021. URL: https://doi.org/10.1088/1478-3975/abdc0e, doi:10.1088/1478-3975/abdc0e. This article has 90 citations and is from a peer-reviewed journal.