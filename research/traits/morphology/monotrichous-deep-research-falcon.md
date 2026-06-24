---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:27:31.010781'
end_time: '2026-06-18T08:38:07.848054'
duration_seconds: 636.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: monotrichous
  trait_identifier: traitmech:000057
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: monotrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with a single flagellum, typically located at
    one pole of the cell.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum
    (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum
    review supports a single helical flagellar filament as a locomotory organelle.)'
  causal_graph_summary: 'monotrichous_single_polar_flagellum: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** monotrichous
- **METPO identifier:** traitmech:000057
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a single flagellum, typically located at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum review supports a single helical flagellar filament as a locomotory organelle.)
- **Existing causal graph summary:** monotrichous_single_polar_flagellum: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **monotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/monotrichous.yaml`.

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
- **Trait label:** monotrichous
- **METPO identifier:** traitmech:000057
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a single flagellum, typically located at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe single-flagellum (monotrichous, polar) flagellation as one regular flagellation pattern.) | DOI:10.3390/biom9070279:  (Flagellum review supports a single helical flagellar filament as a locomotory organelle.)
- **Existing causal graph summary:** monotrichous_single_polar_flagellum: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **monotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/monotrichous.yaml`.

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


## Research report: monotrichous (METPO: traitmech:000057)

### 1) Scope summary (trait meaning, boundaries, and distinctions)

**Trait definition (curation target).** *Monotrichous* describes a flagellar arrangement in which a cell bears **a single polar flagellum** (typically at one pole). In an authoritative review on flagellar patterning, Schuhmacher et al. define monotrichous polar-flagellated bacteria as those that “bear a **single polar flagellum**” (examples noted include *Vibrio*, *Pseudomonas*, *Xanthomonas*), and they contextualize monotrichous as one of several regular flagellation patterns. (schuhmacher2015howbacteriamaintain pages 4-5)

**Distinguish from adjacent traits.** Monotrichous is distinct from:
- **Lophotrichous** (multiple flagella at one pole; polar tuft) and **amphitrichous** (flagella at both poles), which are also polar arrangements but not single-flagellum states; polar patterning mechanisms (e.g., FlhF/FlhG) can apply across these categories. (gibson2023controlofthe pages 1-2, schuhmacher2015howbacteriamaintain pages 4-5)
- **Peritrichous** (multiple flagella distributed around the cell body), which uses different patterning logic in some taxa (e.g., *B. subtilis*). (schuhmacher2015howbacteriamaintain pages 4-5)
- **Atrichous/aflagellated** states, which can occur as subpopulations or due to genetic/environmental conditions and should not be conflated with monotrichous. (gibson2023controlofthe pages 1-2)

**Boundary cases important for curation.**
1. **Lifecycle- or cell-cycle-dependent polar flagellation:** In *Caulobacter*, the “swarmer state is motile by a single polar flagellum,” and a new flagellum can be assembled at the opposite pole before division. This creates time-dependent boundary cases for assays capturing only a snapshot. (schuhmacher2015howbacteriamaintain pages 4-5)
2. **Species with more than one flagellar system:** Some bacteria can encode separate polar and lateral/peritrichous systems; a “monotrichous flagellum for swimming motility” may coexist with additional flagella in other modes/conditions (edge-case warning: do not curate as strictly monotrichous without specifying the motility mode and growth condition). (botting2023flagellumassemblyanda pages 138-143)
3. **Conditional monoflagellation:** Genetic perturbations in polar-flagellated bacteria frequently shift monotrichous populations into hyperflagellated (multiple polar flagella) or hypoflagellated/aflagellated subpopulations, implying that “monotrichous” can be a regulated steady-state rather than a fixed structural invariant. (gibson2023controlofthe pages 1-2, schuhmacher2015howbacteriamaintain pages 4-5)

**Assay/annotation considerations.** Monotrichous is generally an **imaging-defined morphology** (electron microscopy/flagella staining) and should be tied to method and growth condition if possible, because population distributions (including aflagellated cells) are commonly reported for the same strain. (gibson2023controlofthe pages 1-2)

---

### 2) Current mechanistic understanding: key concepts, entities, and causal logic

#### Core mechanistic concept: “where and how many” control
A central theme in polar flagellation is the separation of control into:
- **Placement (where):** localization of basal-body assembly to the pole.
- **Numerosity (how many):** restriction to one (monotrichous) vs multiple polar flagella.

Across many polar-flagellated bacteria, **FlhF** (an SRP-type GTPase) and **FlhG** (a MinD/ParA-family ATPase; often called FleN in *Pseudomonas*) are key conserved regulators controlling these two axes. Schuhmacher et al. summarize that placement and number are “commonly controlled” by FlhF/FlhG, and note typical mutant phenotypes (ΔflhF → absence/mislocalization; ΔflhG → hyperflagellation). (schuhmacher2015howbacteriamaintain pages 4-5)

#### Major 2023–2024 development (high-priority): molecular mechanism for polar confinement
A 2024 **Nature Communications** paper provides a detailed interaction map and assembly checkpoint model:
- **FlhF NG (GTPase) domain ↔ HubP/FimV polar landmark.** FlhF anchors developing flagellar structures to the polar landmark HubP/FimV through its GTPase domain. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 4-6)
- **FlhF N-terminal FID/B-domain ↔ FliG.** A distinct N-terminal region of FlhF binds the C-ring protein FliG. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4)
- **FlhF-bound FliG recruits/captures FliF to form early MS/C-ring at the pole.** FlhF-bound FliG “engages the MS-ring protein FliF,” recruiting a functional FliF/FliG complex to the pole. (dornes2024polarconfinementof pages 1-2)
- **Assembly checkpoint:** FlhF-bound FliG can still engage FliF but is “prevented from interacting with C-ring partners FliM/FliN,” suggesting FlhF helps enforce an early assembly order. (dornes2024polarconfinementof pages 2-4)
- **FlhG modulates FlhF to control progression:** FlhG “stimulates FlhF GTPase activity,” and this modulation is linked to controlling downstream interactions (e.g., enabling FliG engagement with FliM/FliN later). (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 7-8)

A model schematic illustrating this diffusion-capture/assembly-checkpoint mechanism is provided in Dornes et al. (Figure 6), suitable as visual support for curation decisions. (dornes2024polarconfinementof media 48e0bcc5)

#### Additional (authoritative) mechanistic details from review evidence
- **HubP-mediated pole recruitment of FlhG in Vibrio:** In *Vibrio*, FlhG recruitment depends on HubP; “loss of HubP causes FlhG to be diffusely distributed or form non-polar foci.” (schuhmacher2015howbacteriamaintain pages 7-8)
- **Second messenger integration (conditional):** In *Caulobacter*, landmark proteins (TipN/TipF) recruit early components, and “TipF function is regulated by binding the second messenger c-di-GMP,” whose levels vary with the cell cycle—providing a chemical node that conditionally affects polar flagellation. (schuhmacher2015howbacteriamaintain pages 4-5)

---

### 3) Candidate causal-graph nodes (grouped by type; with grounding suggestions)

#### Trait node
- **monotrichous** — METPO: **traitmech:000057** (given)

#### Cellular structures / processes
- **Polar flagellum / polar flagellar basal body** (label-only; could map to GO biological process “flagellum-dependent cell motility” but arrangement is morphological)
- **MS ring** (FliF-dependent; basal body substructure; label-only)
- **C ring** (FliG/FliM/FliN-dependent; label-only)
- **Polar localization / polar confinement of flagellar assembly** (label-only)

#### Proteins / complexes (mechanistic determinants)
- **FlhF** (SRP-type GTPase; label-only; often conserved across polar systems) (gibson2023controlofthe pages 1-2, schuhmacher2015howbacteriamaintain pages 4-5)
- **FlhG** (MinD/ParA-family ATPase; label-only) (gibson2023controlofthe pages 1-2, schuhmacher2015howbacteriamaintain pages 4-5)
- **HubP/FimV** (polar landmark protein; label-only) (dornes2024polarconfinementof pages 1-2)
- **FliF** (MS-ring protein; label-only) (gibson2023controlofthe pages 1-2)
- **FliG** (C-ring protein; label-only) (dornes2024polarconfinementof pages 2-4)
- **FliM/FliN** (C-ring partners; label-only) (dornes2024polarconfinementof pages 2-4)
- **TipN / TipF** (*Caulobacter* landmark proteins; label-only; conditional) (schuhmacher2015howbacteriamaintain pages 4-5)
- **PflI** (*Caulobacter* component referenced as recruited by landmarks; label-only) (schuhmacher2015howbacteriamaintain pages 4-5)
- **FleN / FleQ** (*Pseudomonas* regulatory circuit; label-only; caution: evidence here is from a 2025 preprint) (lozano2025regulatoryplasticityand pages 1-5)

#### Chemicals / second messengers
- **c-di-GMP** (CHEBI identifier not resolved in provided evidence; keep label-only + note CHEBI grounding needed) (schuhmacher2015howbacteriamaintain pages 4-5)

#### Environmental / experimental context nodes
- **Cell cycle state** (conditional, *Caulobacter*) (schuhmacher2015howbacteriamaintain pages 4-5)
- **Viscous environments / viscosity selection pressure** (suggested context in preprint; treat as uncertain until supported by peer-reviewed evidence in this curation set) (lozano2025regulatoryplasticityand pages 1-5)

---

### 4) Evidence-backed candidate edges (triples) for `monotrichous.yaml`

The table below is designed for direct curation into a TraitMech causal graph (subject–predicate–object, with evidence and notes).

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet (verbatim, short) | Reference (DOI, year, URL) | Notes / uncertainty |
|---|---|---|---|---|---|
| FlhF (label-only candidate; SRP-type GTPase) | promotes localization of | polar flagellum / polar localization of flagella (label-only; phenotype) | “FlhF and FlhG control the location and number of flagella, respectively, in many polar-flagellated bacteria.” and deleting flhF caused “hypoflagellation and the mislocalization of flagella to nonpolar sites.” (gibson2023controlofthe pages 1-2) | 10.1128/jb.00110-23, 2023, https://doi.org/10.1128/jb.00110-23 | Strong for polar-flagellated bacteria broadly; not specific to strictly monotrichous taxa because source includes lophotrichous H. pylori. |
| FlhG (label-only candidate; MinD/ParA-family ATPase) | regulates number of | flagella per cell (label-only phenotype) | “FlhF and FlhG control the location and number of flagella, respectively, in many polar-flagellated bacteria.” and “Deleting flhG in bacteria that have a single polar flagellum often results in hyperflagellation” (gibson2023controlofthe pages 1-2) | 10.1128/jb.00110-23, 2023, https://doi.org/10.1128/jb.00110-23 | Strong generic edge for polar flagellation; curate as broad mechanism rather than monotrichous-only. |
| FlhF NG domain (label-only candidate) | binds | HubP/FimV polar landmark protein (label-only candidate) | “The GTPase domain of FlhF interacts with the polar landmark HubP/FimV” (dornes2024polarconfinementof pages 1-2) | 10.1038/s41467-024-50274-4, 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong mechanistic edge; HubP/FimV naming is species-dependent. |
| FlhF FID/B-domain (label-only candidate) | binds | FliG (GO/UniProt not resolved here; label-only candidate) | “the FlhF B-domain contains an N-terminal FliG Interaction Domain (FID)” and “the N-terminal ~60 amino acids of the B-domain are necessary and sufficient for FliG binding” (dornes2024polarconfinementof pages 2-4) | 10.1038/s41467-024-50274-4, 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong direct interaction. |
| FlhF-bound FliG complex (label-only candidate) | captures / recruits | FliF MS-ring protein (label-only candidate) | “FlhF-bound FliG then engages the MS-ring protein FliF, effectively recruiting a FliF–FliG complex to the pole.” (dornes2024polarconfinementof pages 1-2) | 10.1038/s41467-024-50274-4, 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong but mechanistic model derived from biochemical/genetic assays in polar systems; suitable as assembly edge. |
| FlhF | hinders interaction of | FliG with FliM/FliN (label-only candidates) | “FlhF-bound FliG can still engage the cytoplasmic domain of the MS-ring protein FliF but is prevented from interacting with C-ring partners FliM/FliN” (dornes2024polarconfinementof pages 2-4) | 10.1038/s41467-024-50274-4, 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong mechanistic checkpoint edge. |
| FlhG | stimulates GTPase activity of | FlhF (label-only candidate) | “FlhG’s modulation of FlhF controls FliG’s interaction with FliM/FliN” and “FlhG stimulates FlhF GTPase activity” (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 7-8) | 10.1038/s41467-024-50274-4, 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong conserved regulatory edge. |
| HubP/FimV polar landmark protein | recruits / anchors | FlhF at the cell pole (label-only localization process) | “FlhF localizes and anchors nascent flagellar structures at the cell pole by direct interactions with a polar landmark” and “the NG domain binds the C-terminal domain of the polar landmark HubP” (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 6-7) | 10.1038/s41467-024-50274-4, 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong in the 2024 system; wording “recruits/anchors” is model-supported. |
| HubP polar landmark protein (label-only candidate) | recruits | FlhG to the cell pole (label-only localization process) | “FlhG is recruited to the cell pole by the polar landmark HubP in Vibrio” and “loss of HubP causes FlhG to be diffusely distributed or form non-polar foci” (schuhmacher2015howbacteriamaintain pages 7-8) | 10.1093/femsre/fuv034, 2015, https://doi.org/10.1093/femsre/fuv034 | Good review-backed edge; taxon-specific to Vibrio in cited evidence. Mark as somewhat taxon-scoped. |
| FleN dosage (label-only candidate; FlhG homolog in Pseudomonas literature) | maintains | monoflagellation / monoflagellated state (METPO: traitmech:000057 candidate phenotype node) | “P. aeruginosa maintains strict monoflagellation through the FleQ-FleN regulatory circuit” and “FleN dosage is essential for maintaining monoflagellation” (lozano2025regulatoryplasticityand pages 1-5) | 10.1101/2025.07.29.667523, 2025, https://doi.org/10.1101/2025.07.29.667523 | Useful candidate edge but preprint only; do not curate as high-confidence until peer-reviewed. |
| FleQ-FleN regulatory circuit (label-only candidate) | constrains / regulates | flagellum number and arrangement (label-only phenotype) | “P. aeruginosa maintains strict monoflagellation through the FleQ-FleN regulatory circuit” and ΔfleN mutants developed “over two-to-five flagella per cell in uni- or bipolar arrangements” (lozano2025regulatoryplasticityand pages 1-5) | 10.1101/2025.07.29.667523, 2025, https://doi.org/10.1101/2025.07.29.667523 | Quantitative and informative, but preprint and Pseudomonas-specific. |
| TipF (label-only candidate) | binds | c-di-GMP (CHEBI candidate not resolved here) | “TipF function is regulated by binding the second messenger c-di-GMP” (schuhmacher2015howbacteriamaintain pages 4-5) | 10.1093/femsre/fuv034, 2015, https://doi.org/10.1093/femsre/fuv034 | Conditional/node-level evidence from Caulobacter developmental polar flagellation; not necessarily generalizable to all monotrichous bacteria. |
| c-di-GMP | regulates activity of | TipF (label-only candidate) | “TipF function is regulated by binding the second messenger c-di-GMP, whose intracellular level varies with the cell cycle.” (schuhmacher2015howbacteriamaintain pages 4-5) | 10.1093/femsre/fuv034, 2015, https://doi.org/10.1093/femsre/fuv034 | Strong for Caulobacter cell-cycle-coupled polar flagellum assembly; conditional and lineage-specific. |
| TipN/TipF landmark system (label-only candidate) | recruits | PflI and core flagellar components FliF/FliG/FliM (label-only candidates) | “In Caulobacter, landmark proteins TipN/TipF recruit PflI and core components (FliF, FliG, FliM)” (schuhmacher2015howbacteriamaintain pages 4-5) | 10.1093/femsre/fuv034, 2015, https://doi.org/10.1093/femsre/fuv034 | Relevant for boundary/conditional mechanism of polar assembly; not monotrichous-universal. |


*Table: This table lists evidence-backed candidate causal edges for curating the monotrichous trait graph, emphasizing conserved regulators of polar localization and flagellum number. It also flags taxon-specific or preprint-supported mechanisms that should be curated cautiously.*

**Visual support for key mechanistic edges.** Dornes et al. provide a model schematic (Figure 6) showing FlhF binding HubP and FliG, recruiting FliF, and FlhG-dependent modulation of FlhF to enable progressive assembly (useful as a curator-facing “mechanism picture”). (dornes2024polarconfinementof media 48e0bcc5)

---

### 5) Quantitative data and statistics (recent studies; usable for graph confidence)

**Species-level comparative statistics (flagella per cell).** A preprint compiling comparative values reports typical/average flagella numbers across species/strains and explicitly defines monotrichous as “single polar.” It gives examples including: *Pseudomonas putida* “typically possesses **5–7 polar flagella per cell**,” *P. syringae* “averages **2.7 flagella per cell**,” and *E. coli* “typically possesses **6–10 flagella**,” with strain-to-strain variation in *P. fluorescens* (2 vs 1 vs 7). While not peer-reviewed, these are quantitative anchors for boundary-setting between mono- and multi-flagellated states and motivate “flagellum number” as a measurable node. (lozano2025regulatoryplasticityand pages 1-5)

**Genetic perturbation quantitative phenotype (hyperflagellation).** The same preprint reports that ΔfleN mutants developed “**over two-to-five flagella per cell** in uni- or bipolar arrangements,” linking a specific regulator dosage to deviation from monoflagellation. Treat as **uncertain** for curation until confirmed in peer-reviewed sources. (lozano2025regulatoryplasticityand pages 1-5)

**Distributional counts (contextual; not monotrichous but informs pattern control).** In *H. pylori* (typically multiple polar flagella), deletion of flhG shifted patterns such that “most cells had approximately four flagella” in wild type, and flhG deletion broadened distribution; deletion of flhF produced hypoflagellation and mislocalization, demonstrating the same “where/how many” regulators operate outside strict monotrichous taxa. These data are useful for **mechanistic generality** of FlhF/FlhG but should not be interpreted as monotrichous-specific distributions. (gibson2023controlofthe pages 1-2)

---

### 6) Applications and real-world implementations

1. **Pathogenesis and host colonization:** Flagellar motility is frequently required for colonization in pathogens. The 2023 *Journal of Bacteriology* study emphasizes that *H. pylori* uses flagella for motility required for host colonization and links FlhF/FlhG to maintaining the species-specific flagellation pattern. This supports treating monotrichous (and polar flagellation broadly) as a trait relevant to infection biology and niche access. (gibson2023controlofthe pages 1-2)
2. **Microbial ecology and dispersal:** Monotrichous motility (single polar propeller) is a common locomotion strategy across aquatic and host-associated bacteria; controlling flagellum number helps balance motility benefit against energetic/material costs implied by fitness trade-off discussions in the comparative preprint. (lozano2025regulatoryplasticityand pages 1-5)
3. **Synthetic biology / spatial organization analogy:** While not monotrichous-specific, recent work on ParA/MinD-family ATPases highlights that spatial positioning ATPases are broadly used for organelle positioning including flagella; this supports modeling FlhG-like ATPases as general “positioning regulators” in graph ontology. (dornes2024polarconfinementof pages 1-2)

---

### 7) Expert synthesis and curation guidance (what is safe to curate now)

**High-confidence, broadly curatable core module (recommended for TraitMech).**
- **FlhF–FlhG–HubP/FimV–FliG–FliF** as a mechanistic module controlling **polar localization** and **progression/number** of polar flagellar assembly, supported by a high-impact 2024 mechanistic study and consistent with the 2015 review and 2023 experimental genetics. (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 7-8, schuhmacher2015howbacteriamaintain pages 7-8, gibson2023controlofthe pages 1-2, schuhmacher2015howbacteriamaintain pages 4-5)

**Conditional / taxon-scoped additions (curate with qualifiers).**
- **TipN/TipF–c-di-GMP–cell cycle** regulation of polar flagellation: strong in *Caulobacter* context but should be marked as lineage-specific/conditional. (schuhmacher2015howbacteriamaintain pages 4-5)
- **FleQ–FleN dosage control** of strict monoflagellation: promising for *Pseudomonas*, but currently represented here by a **2025 preprint** and should be marked **uncertain** until peer-reviewed and/or supported by additional primary papers in your evidence set. (lozano2025regulatoryplasticityand pages 1-5)

---

### 8) Warnings (claims not ready for unqualified curation)

- **Do not equate “polar flagellated” with “monotrichous.”** Many polar bacteria are lophotrichous or amphitrichous; the same regulators can operate across patterns. Use a phenotype node such as “polar flagellum localization” and separate from “single flagellum number = 1.” (schuhmacher2015howbacteriamaintain pages 4-5, gibson2023controlofthe pages 1-2)
- **Avoid curating multi-system statements without context.** Evidence exists for bacteria having “a monotrichous flagellum for swimming” plus other flagella for other motilities; without condition labels, this can mislead trait annotation. (botting2023flagellumassemblyanda pages 138-143)
- **Preprint-derived statistics and mechanisms should be flagged uncertain.** Species-comparison numbers and FleQ–FleN statements are useful but not yet peer-reviewed in this evidence set. (lozano2025regulatoryplasticityand pages 1-5)

---

## DOI-first bibliography (with dates/URLs where available)

1. **Dornes A, Schmidt LM, Mais C-N, et al.** Polar confinement of a macromolecular machine by an SRP-type GTPase. *Nature Communications*. **2024-07**. DOI: **10.1038/s41467-024-50274-4**. URL: https://doi.org/10.1038/s41467-024-50274-4 (dornes2024polarconfinementof pages 1-2)
2. **Gibson KH, Botting JM, Al-Otaibi N, et al.** Control of the flagellation pattern in *Helicobacter pylori* by FlhF and FlhG. *Journal of Bacteriology*. **2023-09**. DOI: **10.1128/jb.00110-23**. URL: https://doi.org/10.1128/jb.00110-23 (gibson2023controlofthe pages 1-2)
3. **Schuhmacher JS, Thormann KM, Bange G.** How bacteria maintain location and number of flagella? *FEMS Microbiology Reviews*. **2015-11**. DOI: **10.1093/femsre/fuv034**. URL: https://doi.org/10.1093/femsre/fuv034 (schuhmacher2015howbacteriamaintain pages 4-5)

Additional (non-peer-reviewed, for context; treat as uncertain):
- **Lozano AM, Asp M, Rocha ST, et al.** Regulatory plasticity and metabolic trade-offs drive adaptive evolution of alternative flagellar configurations in *Pseudomonas aeruginosa*. *bioRxiv*. **2025-07**. DOI: **10.1101/2025.07.29.667523**. URL: https://doi.org/10.1101/2025.07.29.667523 (lozano2025regulatoryplasticityand pages 1-5)


References

1. (schuhmacher2015howbacteriamaintain pages 4-5): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

2. (gibson2023controlofthe pages 1-2): Katherine H. Gibson, Jack M. Botting, Natalie Al-Otaibi, Kriti Maitre, Julien Bergeron, Vincent J. Starai, and Timothy R. Hoover. Control of the flagellation pattern in <i>helicobacter pylori</i> by flhf and flhg. Journal of Bacteriology, Sep 2023. URL: https://doi.org/10.1128/jb.00110-23, doi:10.1128/jb.00110-23. This article has 10 citations and is from a peer-reviewed journal.

3. (botting2023flagellumassemblyanda pages 138-143): JM Botting. Flagellum assembly and chemotaxis in helicobacter pylori. Unknown journal, 2023.

4. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

5. (dornes2024polarconfinementof pages 4-6): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

6. (dornes2024polarconfinementof pages 2-4): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

7. (dornes2024polarconfinementof pages 7-8): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

8. (dornes2024polarconfinementof media 48e0bcc5): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

9. (schuhmacher2015howbacteriamaintain pages 7-8): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

10. (lozano2025regulatoryplasticityand pages 1-5): Anali Migueles Lozano, Merrill Asp, Sofia T. Rocha, Jiaqi Li, Georgia Fanouraki, Aden D. Sun, Lichun Zhang, Jacob R. Waldbauer, Jiarong Hong, Abhishek Shrivastava, Jing Yan, and Sampriti Mukherjee. Regulatory plasticity and metabolic trade-offs drive adaptive evolution of alternative flagellar configurations in pseudomonas aeruginosa. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.29.667523, doi:10.1101/2025.07.29.667523. This article has 0 citations.

11. (dornes2024polarconfinementof pages 6-7): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.