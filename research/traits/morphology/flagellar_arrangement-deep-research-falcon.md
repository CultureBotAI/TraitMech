---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:38:55.310020'
end_time: '2026-06-18T07:51:39.049318'
duration_seconds: 763.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: flagellar arrangement
  trait_identifier: traitmech:000056
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: flagellar_arrangement
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait describing the number and spatial distribution of
    flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous,
    amphitrichous, or peritrichous.
  parent_traits: METPO:1000704
  synonyms: flagellation pattern
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe
    how bacteria maintain a regular number and cellular location of flagella (the
    flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial
    flagellum review supports the flagellum as the locomotory organelle whose number
    and placement define flagellar arrangement.)'
  causal_graph_summary: 'flagellar_arrangement_flhf_flhg: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** flagellar arrangement
- **METPO identifier:** traitmech:000056
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing the number and spatial distribution of flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous, amphitrichous, or peritrichous.
- **Parent traits:** METPO:1000704
- **Synonyms:** flagellation pattern
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe how bacteria maintain a regular number and cellular location of flagella (the flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial flagellum review supports the flagellum as the locomotory organelle whose number and placement define flagellar arrangement.)
- **Existing causal graph summary:** flagellar_arrangement_flhf_flhg: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **flagellar arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellar_arrangement.yaml`.

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
- **Trait label:** flagellar arrangement
- **METPO identifier:** traitmech:000056
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait describing the number and spatial distribution of flagella on a cell (the flagellation pattern), e.g. monotrichous, lophotrichous, amphitrichous, or peritrichous.
- **Parent traits:** METPO:1000704
- **Synonyms:** flagellation pattern
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher, Thormann & Bange describe how bacteria maintain a regular number and cellular location of flagella (the flagellation pattern); parent of the specific arrangement sub-variants.) | DOI:10.3390/biom9070279:  (Bacterial flagellum review supports the flagellum as the locomotory organelle whose number and placement define flagellar arrangement.)
- **Existing causal graph summary:** flagellar_arrangement_flhf_flhg: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **flagellar arrangement** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/flagellar_arrangement.yaml`.

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


## Research report: Flagellar arrangement (flagellation pattern) — TraitMech causal-graph evidence

### Target trait
- **Trait:** flagellar arrangement (flagellation pattern)
- **METPO/TraitMech identifier:** traitmech:000056 (given)
- **Definition (curation):** the **number** and **spatial distribution** of flagella on a cell (e.g., monotrichous, lophotrichous, amphitrichous, peritrichous; and, in some taxa, distinct *polar* vs *lateral* flagellar systems). This is an **anatomical/morphology trait** describing where flagellar basal bodies/filaments are positioned, not the motor’s torque/speed or chemotactic signaling state. Species-specific flagellation pattern is described as an early taxonomic criterion and is actively replicated across cell divisions (dornes2024polarconfinementof pages 1-2, schuhmacher2015howbacteriamaintain pages 1-2).

---

## 1) Trait scope and boundary cases

### What the trait represents
Flagellar arrangement represents a **morphological patterning outcome** of flagellar biogenesis: the cell builds **0, 1, or multiple** flagella and places them at defined locations (pole(s), lateral positions, or distributed around the cell body) (schuhmacher2015howbacteriamaintain pages 1-2, dornes2024polarconfinementof pages 1-2).

### Boundary cases / distinctions from nearby traits
- **Not “flagellum present/absent”**: arrangement includes presence/absence but is broader—e.g., “single polar” vs “multiple polar” vs “lateral-near-pole” are distinct arrangements (kumar2016syntheticcysticfibrosis pages 4-7, dornes2024polarconfinementof pages 1-2).
- **Not “motility performance”** (speed/torque) or **chemotaxis**: motility can change without increased flagellin/flagella (e.g., amino acids increasing motility via chemotaxis-like effects without raising flagellin expression) (kumar2016syntheticcysticfibrosis pages 1-2).
- **Dual-system species (polar + lateral)**: some bacteria encode separate systems (polar swimming vs lateral/surface-associated swarming), so the trait may need context: **which flagellar system** is being scored (schuhmacher2015howbacteriamaintain pages 2-4). A 2024 mechanistic study shows FlhF can discriminate between polar and lateral rotor components, explaining system specificity (dornes2024polarconfinementof pages 2-4).
- **Periplasmic flagella (spirochetes)**: periplasmic location complicates “spatial distribution” relative to Gram-negative external filaments, but the trait still maps to “number and location” of flagellar structures; curation may require a separate submodel for spirochetes.

---

## 2) Current understanding (key concepts & mechanistic determinants)

### Conceptual models for positioning
Two broad positioning strategies are described:
1. **Landmark-directed placement** (e.g., Caulobacter TipN/TipF/PflI pathway; polar landmarks) (schuhmacher2015howbacteriamaintain pages 2-4, schuhmacher2015howbacteriamaintain pages 4-5).
2. **Stochastic/diffusion–capture placement** (often invoked for peritrichous patterning, where distributed nucleation can arise without dedicated landmarks) (schuhmacher2015howbacteriamaintain pages 2-4).

### Core mechanistic modules and definitions

#### A. FlhF/FlhG spatial control module (widely conserved in polar and some peritrichous bacteria)
- **FlhF**: SRP-type GTPase that directs early assembly components to specific sites; in polar systems, it is required to direct the earliest MS-ring component (FliF) to the pole (dornes2024polarconfinementof pages 1-2).
- **FlhG**: MinD/ParA-family ATPase (also called MinD2/FleN/MotR/YlxH in some contexts) that negatively regulates flagellar number and participates in assembly-state feedback by modulating FlhF and rotor assembly progression (pulianmackal2024positioningofcellular pages 3-4, dornes2024polarconfinementof pages 1-2).

Mechanistic resolution (2024): FlhF anchors developing flagellar structures to a polar landmark (HubP/FimV) and couples landmarking to rotor component recruitment (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 4-6).

#### B. TipN/TipF/PflI landmark module (Caulobacter-type)
- **TipN** is a polar “landmark protein” that is positioned in a cell-cycle-dependent manner (schuhmacher2015howbacteriamaintain pages 2-4).
- **TipF** is a transmembrane factor that **binds c-di-GMP** and is stabilized by it; TipF mediates recruitment of additional factors and basal-body building blocks to the pole (schuhmacher2015howbacteriamaintain pages 2-4, schuhmacher2015howbacteriamaintain pages 4-5).
- **PflI** is recruited downstream of TipF (schuhmacher2015howbacteriamaintain pages 4-5).

#### C. ParA/MinD (A/D) family positioning principle (generalizable mechanism)
A/D-family ATPases position diverse cargos by ATP-dependent dimerization and binding to a matrix (membrane or nucleoid) followed by partner-stimulated ATP hydrolysis and release, yielding spatial patterns/gradients; FlhG is a MinD-like instance in flagellar placement control (pulianmackal2024positioningofcellular pages 12-14, pulianmackal2024positioningofcellular pages 3-4).

---

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Polar confinement mechanism resolved (Nature Communications, July 2024)
Dornes et al. (2024) provide a molecular interaction model connecting:
- **HubP/FimV (polar landmark)**
- **FlhF (SRP-type GTPase)**
- **Rotor/MS-ring proteins (FliG, FliF)**
- **FlhG (MinD-type ATPase)**

Key mechanistic points include:
- FlhF **anchors developing flagellar structures** to HubP/FimV (dornes2024polarconfinementof pages 1-2).
- FlhF’s **NG domain** binds the **C-terminal** cytoplasmic region of HubP (dornes2024polarconfinementof pages 4-6).
- FlhF’s **B-domain/FID** binds **FliG** (dornes2024polarconfinementof pages 2-4).
- FlhF-bound FliG engages/captures **FliF**, recruiting a FliF–FliG complex to the pole and initiating MS-ring assembly (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 6-7).
- FlhF binding to FliG **prevents** FliG from interacting with FliM/FliN until assembly progresses, and FlhG modulates FlhF to control this transition (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 1-2).

A schematic summarizing this model (Figure 6) is available from the paper and was retrieved here (dornes2024polarconfinementof media 7c7a570b).

### 3.2 Updated positioning ATPase synthesis (Current Opinion in Microbiology, June 2024)
Pulianmackal & Vecchiarelli (2024) synthesize how ParA/MinD-family ATPases position cellular components, specifically noting **FlhG** as a MinD-like positioning ATPase collaborating with **FlhF** and often assisted by polar landmarks such as HubP (pulianmackal2024positioningofcellular pages 12-14, pulianmackal2024positioningofcellular pages 4-6).

---

## 4) Candidate causal-graph nodes (grouped by type)

### Trait node
- **Flagellar arrangement / flagellation pattern** (TraitMech: traitmech:000056)

### Biological processes / functions (suggested GO grounding candidates)
(Label-only here; curators can map to precise GO IDs)
- bacterial-type flagellum assembly (GO)
- flagellum-dependent cell motility (GO)
- cellular component localization / polar localization of macromolecular complexes (GO)
- C-ring (switch complex) assembly / MS-ring assembly (GO; may be modeled as sub-process nodes)

### Proteins/genes (mechanistic entities)
- **FlhF** (SRP-type GTPase) (dornes2024polarconfinementof pages 1-2)
- **FlhG** (MinD/ParA-family ATPase) (dornes2024polarconfinementof pages 1-2, pulianmackal2024positioningofcellular pages 4-6)
- **HubP/FimV** (polar landmark) (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 4-6)
- **FliF** (MS-ring protein) (dornes2024polarconfinementof pages 1-2)
- **FliG** (C-ring rotor/switch component) (dornes2024polarconfinementof pages 2-4)
- **FliM, FliN** (C-ring components) (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4)
- **TipN** (landmark protein; Caulobacter) (schuhmacher2015howbacteriamaintain pages 2-4)
- **TipF** (c-di-GMP-binding factor) (schuhmacher2015howbacteriamaintain pages 2-4, schuhmacher2015howbacteriamaintain pages 4-5)
- **PflI** (downstream recruitment factor) (schuhmacher2015howbacteriamaintain pages 4-5)

### Chemicals / second messengers
- **c-di-GMP** (CHEBI grounding recommended) (schuhmacher2015howbacteriamaintain pages 2-4)

### Environmental / experimental factors
- **Surface contact / swarming-associated conditions** (condition-dependent switch to lateral flagella in some taxa) (schuhmacher2015howbacteriamaintain pages 2-4)
- **Synthetic cystic fibrosis sputum medium (SCFM)** as a defined nutritional milieu affecting flagellation pattern (kumar2016syntheticcysticfibrosis pages 4-7)

### Example taxa for grounding (NCBITaxon)
- *Shewanella putrefaciens* (polar + lateral system context; FlhF discriminates systems) (dornes2024polarconfinementof pages 1-2)
- *Vibrio* spp. (HubP recruitment of FlhG; landmarked polar system) (schuhmacher2015howbacteriamaintain pages 7-8)
- *Caulobacter crescentus* (TipN/TipF landmark pathway) (schuhmacher2015howbacteriamaintain pages 2-4)
- *Burkholderia cenocepacia* (nutritional modulation + flhF dependence quantified) (kumar2016syntheticcysticfibrosis pages 4-7)

---

## 5) Evidence-backed candidate causal edges

The following artifact compiles candidate edges as curation-ready triples with snippets, dates, DOIs, URLs, and curation notes.

| Subject node | Predicate | Object node | Evidence source (first author, year, DOI) | Publication date | URL | Supporting snippet | Notes for curation |
|---|---|---|---|---|---|---|---|
| FlhF | anchors developing flagellar structures to | HubP/FimV polar landmark protein | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhF anchors developing flagellar structures to the polar landmark protein HubP/FimV” (dornes2024polarconfinementof pages 1-2) | Strong, direct mechanistic edge for polar systems; central to spatial confinement of flagellar assembly. |
| FlhF NG domain | binds | HubP C-terminal domain | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhF binds the C-terminal cytoplasmic region of the polar landmark HubP (HubP-C) via FlhF's NG domain” (dornes2024polarconfinementof pages 4-6) | Strong biochemical interaction; taxon-specific to HubP-containing polar flagellates. |
| FlhF B-domain / FID | binds | FliG | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “The FlhF B-domain is necessary and sufficient for FliG binding; the N-terminal 60 amino acids form a structured FliG Interaction Domain (FID)” (dornes2024polarconfinementof pages 2-4) | Strong interaction; good candidate node split if domain-level curation is allowed. |
| FlhF-bound FliG | engages / recruits | FliF (MS-ring protein) | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhF-bound FliG then engages the MS-ring protein FliF, recruiting a FliF–FliG complex to the pole” (dornes2024polarconfinementof pages 1-2) | Strong mechanistic edge linking landmarking to earliest basal-body assembly. |
| FlhF–FliG complex | captures at pole | FliF | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “the FlhF–FliG complex… capture[s] FliF via its C-terminal domain” (dornes2024polarconfinementof pages 6-7) | Similar to row above but more specific to diffusion-capture model; may be redundant if graph prefers one edge. |
| FlhF binding to FliG | inhibits | FliG interaction with FliM/FliN | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhF-bound FliG can engage the MS-ring protein FliF but is prevented from interacting with C-ring partners FliM/FliN” (dornes2024polarconfinementof pages 2-4) | Strong mechanistic gating step for assembly order; useful process edge for C-ring progression. |
| FlhG | stimulates GTPase activity of | FlhF | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhG acts on FlhF by stimulating its GTPase activity” (dornes2024polarconfinementof pages 6-7) | Strong conserved core edge; central negative/regulatory interaction. |
| FlhG | controls | FliG–FliM/FliN interaction / C-ring assembly progression | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhG… controls FliG interactions with FliM–FliN, regulating progression of flagellar assembly at the pole” (dornes2024polarconfinementof pages 1-2) | Strong but assembly-state dependent; object may need normalization as biological process rather than direct protein edge. |
| FlhF | directs initial MS-ring protein to | cell pole | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “FlhF… is required to direct the initial MS-ring protein FliF to the cell pole” (dornes2024polarconfinementof pages 1-2) | Strong phenotype/process edge; object could be “polar localization of FliF” if graph uses process nodes. |
| FlhF B-domain | recruits | FliF to cell pole | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “the FlhF B-domain has been shown to recruit the MS-ring component FliF to the cell pole” (schuhmacher2015howbacteriamaintain pages 5-7) | Review-based summary, not a primary interaction assay here; still useful as supporting legacy evidence. |
| FlhF | marks | future flagellar assembly site | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “After FlhF marked the future flagellar site, assembly of the basal body will proceed” (schuhmacher2015howbacteriamaintain pages 8-9) | Mechanistic model from review; curate as process edge with moderate confidence. |
| FlhG monomer | binds | FliM/FliN(Y) | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “Monomeric FlhG binds FliM/FliN(Y) independently of nucleotide state” (schuhmacher2015howbacteriamaintain pages 8-9) | Review synthesis; species variation noted. Consider taxon-specific or uncertain if broad generalization is undesirable. |
| FlhG | assists incorporation of | FliM/FliN(Y) into nascent C-ring | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “assists their incorporation into the nascent C-ring (via FliG)” (schuhmacher2015howbacteriamaintain pages 8-9) | Good process edge, but indirect and model-based. Mark moderate confidence. |
| HubP | recruits | FlhG to cell pole | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “HubP recruits FlhG to the pole in Vibrio (loss of HubP delocalizes FlhG)” (schuhmacher2015howbacteriamaintain pages 7-8) | Review-based, Vibrio-focused; valuable as landmark→positioning ATPase edge. |
| FlhG | inhibits pole localization of | FlhF | Pulianmackal, 2024, 10.1016/j.mib.2024.102485 | Jun 2024 | https://doi.org/10.1016/j.mib.2024.102485 | “FlhG… interacts with and inhibits FlhF pole localization to limit flagella number” (pulianmackal2024positioningofcellular pages 4-6) | Useful higher-level regulatory edge from review; not as direct as FlhG→FlhF GTPase stimulation. |
| FlhG deletion | causes | mispositioned multi-flagellated tufts | Pulianmackal, 2024, 10.1016/j.mib.2024.102485 | Jun 2024 | https://doi.org/10.1016/j.mib.2024.102485 | “FlhG deletion causes mispositioned multi-flagellated tufts” (pulianmackal2024positioningofcellular pages 4-6) | Phenotype edge rather than molecular mechanism; useful for trait evidence but may be too phenotype-level for TraitMech core graph. |
| FlhF deletion | causes | loss or random flagellation | Pulianmackal, 2024, 10.1016/j.mib.2024.102485 | Jun 2024 | https://doi.org/10.1016/j.mib.2024.102485 | “FlhF deletion yields loss or random flagellation” (pulianmackal2024positioningofcellular pages 4-6) | Phenotype edge; broad review statement across species. |
| FlhG ATP-bound dimer | sequesters | FlrA transcriptional regulator | Pulianmackal, 2024, 10.1016/j.mib.2024.102485 | Jun 2024 | https://doi.org/10.1016/j.mib.2024.102485 | “ATP-bound FlhG dimers bind and sequester transcriptional regulator FlrA” (pulianmackal2024positioningofcellular pages 4-6) | Strong regulatory concept but more about flagellar gene expression/number than spatial placement; taxon-specific (Shewanella context). |
| FlrA | stimulates ATPase activity of | FlhG | Pulianmackal, 2024, 10.1016/j.mib.2024.102485 | Jun 2024 | https://doi.org/10.1016/j.mib.2024.102485 | “FlrA stimulating FlhG ATPase activity” (pulianmackal2024positioningofcellular pages 4-6) | Regulatory feedback edge; likely species-specific. Mark uncertain for cross-taxon curation. |
| TipN landmark protein | recruits via TipF pathway | polar flagellar assembly factors | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “TipN acts as a polar ‘landmark protein’… together with TipF, recruits flagellar assembly in a cell-cycle-dependent manner” (schuhmacher2015howbacteriamaintain pages 2-4) | Landmark-system edge for Caulobacter-type mechanism; object may need decomposition into TipF/PflI/FliF/FliG/FliM. |
| c-di-GMP | stabilizes | TipF | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “TipF binds c-di-GMP and is stabilized upon binding” (schuhmacher2015howbacteriamaintain pages 2-4) | Strong signaling edge in Caulobacter landmark pathway. CHEBI grounding possible for c-di-GMP. |
| TipF | recruits | PflI | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “TipF then recruits PflI” (schuhmacher2015howbacteriamaintain pages 4-5) | Strong pathway edge from review; taxon-specific to Caulobacter system. |
| TipF | directs basal-body building blocks to | cell pole | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “TipF then recruits PflI and directs basal-body building blocks (FliF, FliG, FliM) to the pole” (schuhmacher2015howbacteriamaintain pages 4-5) | Strong process edge; can be expanded into separate edges to FliF/FliG/FliM if needed. |
| Loss of TipF | causes | non-flagellated cells | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “loss of TipF yields non-flagellated cells” (schuhmacher2015howbacteriamaintain pages 4-5) | Useful phenotype evidence for landmark importance; not a direct molecular interaction. |
| Surface contact / swarming-associated conditions | increases number of | lateral flagella in some species | Schuhmacher, 2015, 10.1093/femsre/fuv034 | Nov 2015 | https://doi.org/10.1093/femsre/fuv034 | “many species encode separate operons for a polar swimming flagellum and for lateral flagella used during swarming or surface-associated growth, and flagellar number can change with environmental conditions” (schuhmacher2015howbacteriamaintain pages 2-4) | Broad environmental/process edge; uncertain because species-dependent and not tied to one defined molecular mediator here. |
| Synthetic cystic fibrosis sputum medium (SCFM) | increases proportion of | multiple-flagellated B. cenocepacia cells | Kumar, 2016, 10.3389/fcimb.2016.00065 | Jun 2016 | https://doi.org/10.3389/fcimb.2016.00065 | “in SCFM the multiple:single:aflagellated ratio is reported as 7:2:1, while in MOPS-glucose 20 mM it is 2:3.5:4.5” (kumar2016syntheticcysticfibrosis pages 4-7) | Strong environmental/experimental factor edge; explicitly assay- and taxon-specific. |
| SCFM | shifts flagellar localization toward | lateral-near-pole / non-strictly polar positioning | Kumar, 2016, 10.3389/fcimb.2016.00065 | Jun 2016 | https://doi.org/10.3389/fcimb.2016.00065 | “SCFM-grown cells display laterally localized flagella near the pole, whereas MOPS-glucose cells show predominantly polar flagella” (kumar2016syntheticcysticfibrosis pages 4-7) | Valuable because it affects arrangement, not just abundance; taxon- and condition-specific. |
| flhF | positively regulates | flagellation pattern in B. cenocepacia under CF-like conditions | Kumar, 2016, 10.3389/fcimb.2016.00065 | Jun 2016 | https://doi.org/10.3389/fcimb.2016.00065 | “The authors conclude FlhF positively regulates flagellin expression and the flagellation pattern in B. cenocepacia K56-2 during CF nutritional conditions” (kumar2016syntheticcysticfibrosis pages 1-2) | Strong phenotype/regulatory edge; environmental context should be retained in graph notes. |
| flhF deletion | increases | aflagellated subpopulation | Kumar, 2016, 10.3389/fcimb.2016.00065 | Jun 2016 | https://doi.org/10.3389/fcimb.2016.00065 | “the mutant population was 80% aflagellated, 14% single-flagellated, and 6% multiple-flagellated” (kumar2016syntheticcysticfibrosis pages 4-7) | Quantitative phenotype edge; useful as supporting evidence for FlhF control of arrangement/number. |
| Individual amino acids at SCFM concentrations | increase | motility without increasing flagellin expression | Kumar, 2016, 10.3389/fcimb.2016.00065 | Jun 2016 | https://doi.org/10.3389/fcimb.2016.00065 | “Individual amino acids… increased motility but did not raise flagellin expression, suggesting chemotaxis contributes to motility changes independent of flagellin abundance” (kumar2016syntheticcysticfibrosis pages 1-2) | Important boundary case: affects motility but not necessarily flagellar arrangement; probably should not be curated into arrangement graph. |
| FlhF B-domain / FID | discriminates between | polar FliG and lateral FliG-Lat | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “this interaction is specific to the polar FliG versus lateral FliG-Lat” (dornes2024polarconfinementof pages 2-4) | Strong explanation for why FlhF/FlhG govern monopolar but not lateral systems; useful if graph includes dual-system specificity. |
| FlhF ΔN44 / loss of FID function | causes | subpolar/lateral flagellar hooks | Dornes, 2024, 10.1038/s41467-024-50274-4 | Jul 2024 | https://doi.org/10.1038/s41467-024-50274-4 | “ΔN44… uncouples recruitment of FliG and flagellar assembly, leading to subpolar/lateral flagellar hooks” (dornes2024polarconfinementof pages 4-6) | Strong mutant evidence linking FID-mediated interaction to correct arrangement; mutation-specific edge. |


*Table: This table compiles candidate causal edges for curating the microbial trait 'flagellar arrangement,' emphasizing core spatial regulators, landmark pathways, assembly components, and condition-specific modifiers. It is designed to support TraitMech graph construction with source-linked snippets, publication metadata, and curation notes.*

Additionally, a key mechanistic model figure supporting many edges (FlhF–FlhG–HubP–FliF/FliG/FliM/FliN diffusion–capture and gating model) was retrieved from Dornes et al. 2024 (dornes2024polarconfinementof media 7c7a570b).

---

## 6) Recent statistics and data from studies (trait-relevant)

### Environment-driven shifts in arrangement and number (quantitative)
In *Burkholderia cenocepacia* K56-2, growth in **synthetic cystic fibrosis sputum medium (SCFM)** altered the population distribution of flagellation classes compared with minimal medium, quantified by TEM scoring (n=100):
- **SCFM:** multiple:single:aflagellated = **7:2:1**
- **Minimal (MOPS-glucose 20 mM):** multiple:single:aflagellated = **2:3.5:4.5**
- Correspondingly, **aflagellated cells** were **45%** in minimal vs **10%** in SCFM (kumar2016syntheticcysticfibrosis pages 4-7).

SCFM also shifted **spatial placement** toward **laterally localized flagella near the pole** vs predominantly polar positioning in minimal medium (kumar2016syntheticcysticfibrosis pages 4-7). These data support edges from “nutritional environment” to “flagellar arrangement.”

### Gene perturbation effects (quantitative)
In the same system, **ΔflhF** shifted the subpopulation distribution under CF-like conditions to **80% aflagellated, 14% single, 6% multiple flagellated**, and reduced the multiple:single ratio relative to WT (WT vs ΔflhF multiple:single = 3.5 vs 0.43) (kumar2016syntheticcysticfibrosis pages 4-7). This provides direct quantitative support that FlhF controls number and arrangement under specific environmental conditions.

---

## 7) Current applications and real-world implementations

### Mechanism-driven design of trait assays (implementation)
- **High-resolution mechanistic mapping of arrangement determinants**: Dornes et al. (2024) combine interaction mapping with a model that explains **polar confinement** through a **landmark–GTPase–rotor** interaction chain (HubP/FimV–FlhF–FliG–FliF), providing a clear blueprint for selecting TraitMech nodes and edges (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4).
- **Quantitative morphology scoring** for arrangement phenotyping: the Burkholderia study demonstrates a simple, curation-relevant quantification approach (TEM-based classification of aflagellated/single/multiple) suitable for linking environmental conditions and gene perturbations to arrangement outcomes (kumar2016syntheticcysticfibrosis pages 4-7).

### Clinical/host-associated relevance (implementation context)
Although not an “application” in the engineered sense, flagellar arrangement control is repeatedly tied to **host colonization and pathogenicity** contexts (e.g., CF-like lung nutritional environment influencing flagellation pattern in *B. cenocepacia*) (kumar2016syntheticcysticfibrosis pages 4-7). This motivates including environment nodes (host-like media, viscosity/surface contact) as modulators, while keeping the trait graph focused on **arrangement** rather than motility output.

---

## 8) Expert synthesis and analysis (authoritative interpretations)

- Schuhmacher et al. (2015) emphasize that bacteria use at least two broad strategies (stochastic vs landmark-directed) to maintain **species-specific flagellation patterns**, and they connect FlhF/FlhG to interactions with rotor components and transcriptional regulators, underscoring that arrangement is maintained by integrated spatial and regulatory circuits rather than by assembly alone (schuhmacher2015howbacteriamaintain pages 2-4, schuhmacher2015howbacteriamaintain pages 1-2).
- Dornes et al. (2024) provide a specific mechanistic interpretation—**polar confinement via HubP/FimV and FlhF**—and show how FlhF’s domain-specific interactions order early assembly events (FliG/FliF recruitment) and gate later ones (FliM/FliN incorporation) (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4).
- Pulianmackal & Vecchiarelli (2024) interpret FlhG within a general ParA/MinD ATPase positioning framework, supporting inclusion of “ATPase cycle / matrix binding” as an abstract mechanistic process node if TraitMech supports it (pulianmackal2024positioningofcellular pages 12-14, pulianmackal2024positioningofcellular pages 3-4).

---

## 9) Ontology grounding suggestions (non-fabricated, curation guidance)

Because stable IDs are taxon- and database-dependent, the recommendations below specify **appropriate namespaces** rather than inventing IDs.

- **Trait:** TraitMech/METPO: traitmech:000056 (given).
- **Genes/proteins:** Use **UniProt** accessions or **NCBIGene** IDs for specific taxa/strains (FlhF, FlhG, HubP/FimV, FliF, FliG, FliM, FliN; TipN, TipF, PflI).
- **Second messenger:** **c-di-GMP** → CHEBI (recommended) (schuhmacher2015howbacteriamaintain pages 2-4).
- **Processes:** Map to appropriate **GO** terms (e.g., bacterial-type flagellum assembly; cellular component localization; membrane targeting; GTPase activity; ATPase activity).
- **Environmental context:** Use **ENVO** (where applicable) for “host-associated environment” or “biofilm/surface-associated growth,” but be cautious: SCFM is an experimental medium and may be better represented as a study-condition node with a label and/or curated medium ontology if available (kumar2016syntheticcysticfibrosis pages 4-7).

---

## 10) Warnings / curation pitfalls (claims to treat cautiously)

1. **Do not conflate arrangement with motility outcomes.** Amino acids in SCFM increased motility without increasing flagellin expression, indicating chemotaxis or motor behavior effects that do not necessarily alter arrangement (kumar2016syntheticcysticfibrosis pages 1-2).
2. **Species- and system-specificity is common.** FlhF can discriminate polar vs lateral rotor components (dornes2024polarconfinementof pages 2-4); edges should often be annotated with whether they apply to **polar** flagellar systems, **lateral** systems, or both.
3. **Review-derived edges should be labeled as such.** Several mechanistic edges in Schuhmacher et al. (2015) are synthesis/model statements; curate with appropriate evidence codes/notes if TraitMech distinguishes primary vs review evidence (schuhmacher2015howbacteriamaintain pages 8-9, schuhmacher2015howbacteriamaintain pages 4-5).
4. **Phenotype-only edges may be insufficient for a mechanistic core graph.** Statements like “ΔflhG causes mispositioned multi-flagellated tufts” are helpful for validating relevance but may require accompanying molecular-interaction edges for mechanistic graphs (pulianmackal2024positioningofcellular pages 4-6).

---

## DOI-first bibliography (with dates and URLs)

1. **Dornes A, et al.** *Polar confinement of a macromolecular machine by an SRP-type GTPase.* **Nature Communications** (Jul 2024). DOI: **10.1038/s41467-024-50274-4**. URL: https://doi.org/10.1038/s41467-024-50274-4 (dornes2024polarconfinementof pages 1-2, dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof media 7c7a570b)
2. **Pulianmackal LT, Vecchiarelli AG.** *Positioning of cellular components by the ParA/MinD family of ATPases.* **Current Opinion in Microbiology** (Jun 2024). DOI: **10.1016/j.mib.2024.102485**. URL: https://doi.org/10.1016/j.mib.2024.102485 (pulianmackal2024positioningofcellular pages 12-14, pulianmackal2024positioningofcellular pages 4-6)
3. **Schuhmacher JS, Thormann KM, Bange G.** *How bacteria maintain location and number of flagella?* **FEMS Microbiology Reviews** (Nov 2015). DOI: **10.1093/femsre/fuv034**. URL: https://doi.org/10.1093/femsre/fuv034 (schuhmacher2015howbacteriamaintain pages 2-4, schuhmacher2015howbacteriamaintain pages 4-5, schuhmacher2015howbacteriamaintain pages 8-9)
4. **Kumar B, Cardona ST.** *Synthetic cystic fibrosis sputum medium regulates flagellar biosynthesis through the flhF gene in Burkholderia cenocepacia.* **Frontiers in Cellular and Infection Microbiology** (Jun 2016). DOI: **10.3389/fcimb.2016.00065**. URL: https://doi.org/10.3389/fcimb.2016.00065 (kumar2016syntheticcysticfibrosis pages 4-7, kumar2016syntheticcysticfibrosis pages 1-2)



References

1. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

2. (schuhmacher2015howbacteriamaintain pages 1-2): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

3. (kumar2016syntheticcysticfibrosis pages 4-7): Brijesh Kumar and Silvia T. Cardona. Synthetic cystic fibrosis sputum medium regulates flagellar biosynthesis through the flhf gene in burkholderia cenocepacia. Frontiers in Cellular and Infection Microbiology, Jun 2016. URL: https://doi.org/10.3389/fcimb.2016.00065, doi:10.3389/fcimb.2016.00065. This article has 27 citations.

4. (kumar2016syntheticcysticfibrosis pages 1-2): Brijesh Kumar and Silvia T. Cardona. Synthetic cystic fibrosis sputum medium regulates flagellar biosynthesis through the flhf gene in burkholderia cenocepacia. Frontiers in Cellular and Infection Microbiology, Jun 2016. URL: https://doi.org/10.3389/fcimb.2016.00065, doi:10.3389/fcimb.2016.00065. This article has 27 citations.

5. (schuhmacher2015howbacteriamaintain pages 2-4): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

6. (dornes2024polarconfinementof pages 2-4): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

7. (schuhmacher2015howbacteriamaintain pages 4-5): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

8. (pulianmackal2024positioningofcellular pages 3-4): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 16 citations and is from a peer-reviewed journal.

9. (dornes2024polarconfinementof pages 4-6): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

10. (pulianmackal2024positioningofcellular pages 12-14): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 16 citations and is from a peer-reviewed journal.

11. (dornes2024polarconfinementof pages 6-7): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

12. (dornes2024polarconfinementof media 7c7a570b): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

13. (pulianmackal2024positioningofcellular pages 4-6): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 16 citations and is from a peer-reviewed journal.

14. (schuhmacher2015howbacteriamaintain pages 7-8): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

15. (schuhmacher2015howbacteriamaintain pages 5-7): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.

16. (schuhmacher2015howbacteriamaintain pages 8-9): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 163 citations and is from a domain leading peer-reviewed journal.