---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:56:23.489544'
end_time: '2026-06-18T10:18:13.329973'
duration_seconds: 1309.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: star shaped
  trait_identifier: METPO:1000685
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: star_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has multiple radiating projections
    from a central body.
  parent_traits: METPO:1000666
  synonyms: S_star_dumbbell_pleomorphic, star, star-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape
    review supports multi-pole peptidoglycan growth as the basis for prosthecate or
    appendaged geometries.) | DOI:10.1146/annurev.micro.061705.103240: prosthecate
    bacteria (Prosthecate-bacteria review supports star-shaped morphology in Stella/Ancalomicrobium
    and related stalked lineages.)'
  causal_graph_summary: 'star_shaped_multiple_prosthecae: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** star shaped
- **METPO identifier:** METPO:1000685
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has multiple radiating projections from a central body.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, star, star-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports multi-pole peptidoglycan growth as the basis for prosthecate or appendaged geometries.) | DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports star-shaped morphology in Stella/Ancalomicrobium and related stalked lineages.)
- **Existing causal graph summary:** star_shaped_multiple_prosthecae: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **star shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/star_shaped.yaml`.

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
- **Trait label:** star shaped
- **METPO identifier:** METPO:1000685
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has multiple radiating projections from a central body.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, star, star-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: polar growth (Cell-shape review supports multi-pole peptidoglycan growth as the basis for prosthecate or appendaged geometries.) | DOI:10.1146/annurev.micro.061705.103240: prosthecate bacteria (Prosthecate-bacteria review supports star-shaped morphology in Stella/Ancalomicrobium and related stalked lineages.)
- **Existing causal graph summary:** star_shaped_multiple_prosthecae: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **star shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/star_shaped.yaml`.

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


# Microbial Trait Causal Graph Report: **star shaped** (METPO:1000685)

**Target trait:** star shaped (METPO:1000685; MORPHOLOGY; CLASS)

**Working definition (METPO-aligned):** A cell shape in which an organism has multiple radiating projections from a central body.

## 1. Scope summary (trait meaning, boundaries, and nearby traits)

### 1.1 What the trait represents
“Star-shaped” morphology is best treated as a **geometric phenotype** visible by microscopy in which a central cell body exhibits **multiple radiating envelope projections** (“arms”). Mechanistically, the most evidence-supported route to such geometry in bacteria is **multipolar / multi-site localized peptidoglycan (PG) synthesis and remodeling** that generates **multiple prosthecae (stalk-like envelope extensions) and/or branches**. This interpretation is consistent with the broader mechanistic framing that bacterial shape is an emergent property of *spatiotemporally regulated PG synthesis* organized by cytoskeletal and polarity modules, especially in morphologically complex Alphaproteobacteria (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 2-4).

### 1.2 Distinguishing star shaped from nearby traits (boundary cases)
1. **Single prostheca (stalked) morphologies:** A single stalk can produce a “lollipop” outline but not a star. Star shape should require **≥3 radiating projections** (or at least clearly “multiple” projections), whereas single-stalk prosthecate bacteria are adjacent phenotypes. Mechanistic modules overlap strongly (bactofilins, localized PG synthesis) (caccamo2018themolecularbasis pages 7-9).
2. **Bilateral prosthecae (two opposite stalks):** Some taxa develop **two** prosthecae (e.g., bilateral Asticcacaulis), which is closer to “dumbbell”/“biprosthecate” than “star”. This is an important boundary because the same positioning machinery (e.g., SpmX co-option) can shift/duplicate prostheca sites (caccamo2018themolecularbasis pages 7-9).
3. **Curved/spiral shapes without projections:** Curvature control (e.g., local remodeling at the inner curve) is related mechanistically but is not itself star shape unless it also produces radiating projections (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21).
4. **Filamentous hyphae without radiating arms:** Hyphal projection (one or more) is adjacent, but “star shaped” requires a central body with multiple arms. Hyphal systems are still relevant because they reveal how cells build and maintain narrow projections by apical PG synthesis and cytoskeletal scaffolds (richter2023interactingbactofilinsimpact pages 11-13).
5. **Fixation or sample-preparation artifacts:** “Star-shaped” morphologies can be **artifact-prone** in some organisms under electron microscopy preparation; fixation conditions can impact observed crescent/star shapes in Chlamydiales, which is a caution for curation unless live-cell or robust prep controls exist (richter2023interactingbactofilinsimpact pages 2-4).

## 2. Key mechanistic concepts and current understanding

### 2.1 Core causal hypothesis for star-shaped geometry
A curation-usable hypothesis for METPO:1000685 is:

> **Multiple discrete zones of PG insertion/remodeling** (each organized by polarity/cytoskeletal modules and PG enzymes) produce **multiple envelope projections**, yielding a star-shaped outline.

Mechanistic work in prosthecate and budding Alphaproteobacteria provides direct evidence that **cytoskeletal scaffolds (bactofilins)** and **PG hydrolases/synthases** create and constrain **localized growth zones** (stalk base, bud neck, hyphal tip) (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21, richter2023interactingbactofilinsimpact pages 11-13).

### 2.2 Spatial organization modules: bactofilins and client PG enzymes
Recent work (2023–2024) establishes **bactofilins** as *spatial organizers* that localize to specific morphogenetic sites and recruit cell-wall enzymes:
- In *Hyphomonas neptunium*, **bactofilin polymers localize dynamically to the stalk base and the bud neck**, and their absence causes **unconstrained stalk and bud growth**, indicating that bactofilins restrict/shape projection growth by spatial regulation of PG processes (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin media e51c436f, pohl2023adynamicbactofilin media 9663cd1f).
- A conserved module pairs bactofilins with an **M23-family endopeptidase (LmdC)**: LmdC **binds bactofilin** and is required for proper cell shape; the authors conclude that **bactofilins and M23 peptidases form a conserved functional module** that promotes local changes in cell wall biosynthesis to drive morphogenesis (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin pages 12-14).

These provide strong candidate nodes and edges for TraitMech curation even if “star shape” is realized only when these modules act at **multiple sites**.

### 2.3 Zonal PG insertion and apical tip growth as intermediate phenotypes
Evidence across model systems supports two intermediate mechanistic phenotypes highly relevant to multi-arm/star outcomes:
- **Zonal insertion in budding prosthecate bacteria:** *Hyphomonas neptunium* exhibits **four distinct PG insertion zones** (dispersed swarmer insertion; zonal insertion at stalk base; dispersed insertion at stalk tip for bud; zonal insertion at bud neck for division) (williams2019mechanismsofpolar pages 32-37).
- **Apical PG insertion in hyphal projection systems:** In *Rhodomicrobium vannielii*, fluorescent D-amino acid labeling indicates PG incorporation is **terminal at hyphal tips**, consistent with apical extension of projections (richter2023interactingbactofilinsimpact pages 11-13).

These patterns constitute the clearest mechanistic “building blocks” for a star-shaped phenotype: if multiple stable apical zones are established around a central body, multiple arms can arise.

## 3. Candidate causal-graph nodes (grounded where possible)

The following node inventory is designed for direct transfer into `data/traits/morphology/star_shaped.yaml`.

| Node type | Label | Suggested grounding | Brief justification with supporting citation IDs |
|---|---|---|---|
| Phenotype | star shaped | METPO:1000685 | Target phenotype: central cell body with multiple radiating projections; mechanistically best approximated by multi-prosthecate or multipolar branched morphology rather than simple curvature alone (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 2-4) |
| Phenotype | multiple prosthecae | label-only | Multiple envelope projections are the most direct structural route to a star-like outline; prostheca repositioning and multiplication are documented across prosthecate alphaproteobacteria (caccamo2018themolecularbasis pages 7-9) |
| Phenotype | branched/wide pseudostalk extensions | label-only | BacA-deficient Hyphomonas produces wide, often branched extensions from uncontrolled PG incorporation, a relevant boundary phenotype for malformed star-like projections (pohl2023adynamicbactofilin pages 12-14) |
| Phenotype | buckled/kinked hyphae | label-only | Loss or misregulation of bactofilins in Rhodomicrobium alters projection geometry, indicating projection maintenance is part of the morphology program rather than only projection initiation (richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 15-16) |
| Process/Function | polar growth | GO:0048754 | Alphaproteobacterial prosthecate and hyphal morphologies are built by tip/pole-focused envelope growth rather than dispersed lateral elongation (richter2023interactingbactofilinsimpact pages 1-2, williams2019mechanismsofpolar pages 32-37) |
| Process/Function | peptidoglycan biosynthetic process | GO:0009252 | All direct mechanistic accounts converge on localized PG synthesis as the immediate driver of stalk/hypha/projection formation (richter2023interactingbactofilinsimpact pages 11-13, pohl2024adynamicbactofilin pages 1-2) |
| Process/Function | peptidoglycan remodeling | GO:0009253 | Shape determination requires local PG remodeling/hydrolysis as well as synthesis; M23 peptidases and other hydrolases are implicated (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21) |
| Process/Function | zonal peptidoglycan insertion | label-only | Hyphomonas shows discrete insertion zones at stalk base, stalk tip, and bud neck; zonal insertion is a strong candidate intermediate for radiating projections (williams2019mechanismsofpolar pages 32-37) |
| Process/Function | tip growth / apical PG incorporation | label-only | HADA labeling in Rhodomicrobium shows strongest incorporation at hyphal tips, supporting apical extension of projections (richter2023interactingbactofilinsimpact pages 11-13) |
| Process/Function | cell polarity switching / multipolar growth | label-only | Branched and radiating morphologies require polarity establishment and switching beyond a single pole; noted as a key unresolved controller in multipolar growth systems (richter2023interactingbactofilinsimpact pages 15-16) |
| Process/Function | bactofilin polymerization | label-only | BacA polymerization is required for proper morphogenesis and localization of client factors in stalk-forming systems (jacq2024functionalspecializationof pages 1-6) |
| Protein/Gene | BacA bactofilin | label-only | Central morphogenetic scaffold in Hyphomonas, Asticcacaulis, and Rhodomicrobium-related systems; localizes to stalk base, bud neck, or hyphal growth zones (richter2023interactingbactofilinsimpact pages 11-13, jacq2024functionalspecializationof pages 1-6, pohl2024adynamicbactofilin pages 1-2) |
| Protein/Gene | BacB bactofilin | label-only | Interacts with BacA and contributes to filament/bundle behavior affecting hyphal shape in Rhodomicrobium (richter2023interactingbactofilinsimpact pages 11-13) |
| Protein/Gene | BacC bactofilin | label-only | BacC localization depends on BacA and overexpression perturbs hyphal morphology, supporting a client/regulatory role in projection shaping (richter2023interactingbactofilinsimpact pages 11-13) |
| Protein/Gene | LmdC M23 endopeptidase | EC:3.4.24.- | Direct BacA-interacting cell-wall hydrolase required for proper morphogenesis; part of a conserved bactofilin–M23 module (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin pages 12-14) |
| Protein/Gene | SpmX | label-only | Developmental/morphogenetic regulator required for stalk synthesis in Asticcacaulis and upstream of localized PG synthesis positioning (jacq2024functionalspecializationof pages 1-6, caccamo2018themolecularbasis pages 28-30, caccamo2018themolecularbasis pages 7-9) |
| Protein/Gene | PbpC | label-only | Bifunctional PBP recruited by bactofilins to the prosthecate pole in Caulobacteraceae, linking scaffold localization to PG synthesis (jacq2024functionalspecializationof pages 1-6, caccamo2018themolecularbasis pages 7-9) |
| Protein/Gene | PBP1a | label-only | Essential polar-growth PBP in Rhizobiales; relevant as a candidate PG synthase for projection-forming polar growth modules (williams2019mechanismsofpolar pages 32-37) |
| Protein/Gene | LD-transpeptidases | EC:3.4.16.- | Proposed contributors to polar/stalk PG architecture and stiffness; altered crosslinking may affect projection rigidity and shape (richter2023interactingbactofilinsimpact pages 15-16, williams2019mechanismsofpolar pages 32-37) |
| Protein/Gene | MreB | UniProtKB:label-only | Canonical elongasome organizer absent from some multipolar/prosthecate taxa; presence/absence helps define alternate pathways to radiating morphologies (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 2-4, williams2019mechanismsofpolar pages 32-37) |
| Protein/Gene | RodZ | label-only | Mentioned as elongasome component whose movement may be restricted by bactofilin barriers in localized growth zones (pohl2024adynamicbactofilin pages 19-21) |
| Protein/Gene | FtsZ | UniProtKB:P0A9A6 | Divisome organizer retained in polar-growing systems; coordinates division-related spatial organization but is not sufficient alone for projection growth (williams2019mechanismsofpolar pages 32-37) |
| Protein/Gene | FtsA | UniProtKB:P0AAI3 | Divisome-associated polarity/organization factor present in polar-growing systems relevant to projection timing and division (williams2019mechanismsofpolar pages 32-37) |
| Protein/Gene | PopZ | label-only | Polar scaffold important for chromosome segregation and polar organization in unipolar growers; candidate indirect regulator of projection positioning (williams2019mechanismsofpolar pages 32-37) |
| Complex/Module | bactofilin cytoskeleton | label-only | Recurrent spatial organizer of noncanonical morphogenesis, including stalks, buds, hyphae, and localized PG assembly (richter2023interactingbactofilinsimpact pages 1-2, pohl2024adynamicbactofilin pages 1-2) |
| Complex/Module | BacA–LmdC module | label-only | Strong 2023–2024 candidate module: couples cytoskeletal localization with local PG hydrolysis/remodeling to constrain projection morphology (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21, pohl2023adynamicbactofilin pages 12-14) |
| Complex/Module | elongasome | GO:0071555 | Conventional lateral-growth machinery whose absence or spatial restriction helps explain shift to polar/multipolar projection growth (richter2023interactingbactofilinsimpact pages 2-4, pohl2024adynamicbactofilin pages 19-21) |
| Complex/Module | divisome | GO:0043190 | Repurposed divisome/polar components are implicated in apical growth in MreB-less Alphaproteobacteria (richter2023interactingbactofilinsimpact pages 15-16, williams2019mechanismsofpolar pages 32-37) |
| Complex/Module | prostheca growth zone | label-only | Functional module at prosthecate pole/base where scaffolds, PBPs, and hydrolases concentrate to build projections (jacq2024functionalspecializationof pages 1-6, williams2019mechanismsofpolar pages 32-37) |
| Cellular location | stalk base | GO:0005737 label-only-localization | BacA and LmdC localize here in Hyphomonas; a major node for constrained projection synthesis (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin media e51c436f) |
| Cellular location | bud neck | label-only | Another BacA/LmdC localization site marking constrained envelope growth during budding extension morphogenesis (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin media e51c436f) |
| Cellular location | hyphal tip | label-only | Site of strongest PG incorporation in Rhodomicrobium; key location for apical projection elongation (richter2023interactingbactofilinsimpact pages 11-13) |
| Cellular location | prosthecate pole | label-only | Prostheca-forming pole where SpmX, DivJ, and PbpC-associated machinery are positioned in stalked alphaproteobacteria (caccamo2018themolecularbasis pages 7-9) |
| Cellular location | inner cell curvature | label-only | Localization site for BacA–LmdC homologs in Rhodospirillum; useful comparative location for local wall remodeling (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21, pohl2023adynamicbactofilin pages 12-14) |
| Environmental factor | oligotrophic aquatic habitat | ENVO:00000148 | Prosthecate morphologies are reported as common in aquatic, oligotrophic bacteria, suggesting ecological association with projection-based surface/nutrient strategies (caccamo2018themolecularbasis pages 7-9) |
| Environmental factor | starvation / nutrient limitation | label-only | Mentioned as influencing stalk elongation or morphology in related prosthecate systems, but direct evidence for star-shaped causation is limited in retrieved excerpts (richter2023interactingbactofilinsimpact pages 13-15, williams2019mechanismsofpolar pages 32-37) |
| Environmental factor | phosphate limitation | CHEBI:18367 | Environmental cue noted in the literature context as modulating prostheca elongation in some stalked bacteria; relevant but weakly supported here for star-shape curation (richter2023interactingbactofilinsimpact pages 13-15) |
| Assay/measurement | HADA fluorescent D-amino-acid labeling | CHEBI:label-only | Direct assay for mapping new PG incorporation at hyphal tips and other growth zones in living cells (richter2023interactingbactofilinsimpact pages 11-13) |
| Assay/measurement | fluorescence microscopy / demograph analysis | label-only | Used to quantify BacA/BacC localization patterns and compare them with PG insertion zones across hundreds of cells (richter2023interactingbactofilinsimpact pages 11-13) |
| Assay/measurement | BACTH interaction assay | label-only | Supports specific BacA/BacB and BacA/BacC interactions underlying scaffold assembly (richter2023interactingbactofilinsimpact pages 11-13) |
| Assay/measurement | in vitro binding / KD measurement | label-only | Demonstrated direct BacA–LmdC interaction with measurable affinity, strengthening edge confidence for the module (pohl2023adynamicbactofilin pages 12-14) |
| Assay/measurement | microfluidics / fluorescent cell-wall probes | label-only | Applied to analyze polar growth dynamics and PG insertion timing in prosthecate/polar-growing alphaproteobacteria (williams2019mechanismsofpolar pages 32-37) |
| Taxon exemplars | Hyphomonas neptunium | NCBITaxon:92 | Strong recent mechanistic model for stalked/budding projection morphogenesis via BacA–LmdC and zonal PG control (pohl2024adynamicbactofilin pages 1-2, williams2019mechanismsofpolar pages 32-37) |
| Taxon exemplars | Asticcacaulis biprosthecum | NCBITaxon:163913 | Bilateral prosthecate bacterium with BacA- and SpmX-dependent stalk morphogenesis, highly relevant to multi-projection logic (jacq2024functionalspecializationof pages 1-6, caccamo2018themolecularbasis pages 7-9) |
| Taxon exemplars | Rhodomicrobium vannielii | NCBITaxon:48 | MreB-less, branching/hyphal alphaproteobacterium with bactofilin-controlled tip growth and multipolar morphogenesis (richter2023interactingbactofilinsimpact pages 11-13, richter2023interactingbactofilinsimpact pages 15-16) |
| Taxon exemplars | Caulobacter crescentus | NCBITaxon:190650 | Canonical prosthecate model where bactofilins recruit PbpC to the stalked pole; useful comparator for conserved projection machinery (jacq2024functionalspecializationof pages 1-6, caccamo2018themolecularbasis pages 7-9) |
| Taxon exemplars | Asticcacaulis excentricus | NCBITaxon:163912 | Comparative prosthecate species showing evolutionary repositioning of prosthecae from polar to subpolar locations (caccamo2018themolecularbasis pages 7-9) |
| Taxon exemplars | Stella spp. | NCBITaxon:label-only | Classical exemplar of star-shaped bacteria, but direct mechanistic evidence was not retrieved in the current evidence set; include only as phenotype anchor, not mechanistic support (caccamo2018themolecularbasis pages 7-9) |
| Taxon exemplars | Ancalomicrobium spp. | NCBITaxon:label-only | Historically associated with prosthecate/noncanonical morphologies, but no direct mechanistic or primary retrieved support for star-shape in current set (caccamo2018themolecularbasis pages 7-9) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of the microbial morphology trait 'star shaped' (METPO:1000685). It groups phenotype, mechanism, localization, environmental, assay, and exemplar-taxon nodes with suggested grounding and evidence anchors for curation.*

## 4. Evidence-backed causal edges (triples) suitable for curation

The following candidate edges are phrased as subject–predicate–object triples with evidence snippets, DOIs/URLs/dates, and uncertainty notes.

| Edge ID | Subject node | Predicate | Object node | Evidence snippet (short quote) | Reference (DOI + URL + year/month) | Citation context ID(s) | Notes/uncertainty for curation |
|---|---|---|---|---|---|---|---|
| E1 | bactofilin BacA | localizes_to | stalk base | "Bactofilin polymers localize dynamically to the stalk base and the bud neck" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Direct experimental evidence in *Hyphomonas neptunium*; taxon-specific but strong. |
| E2 | bactofilin BacA | localizes_to | bud neck | "Bactofilin polymers localize dynamically to the stalk base and the bud neck" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Direct experimental evidence in *H. neptunium*; relevant to spatial control of projection morphogenesis. |
| E3 | loss of bactofilin BacA | causes | unconstrained stalk growth | "their absence leading to unconstrained growth of the stalk and bud compartments" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Direct mutant phenotype; supports negative regulation/confinement of projection growth rather than initiation alone. |
| E4 | loss of bactofilin BacA | causes | unconstrained bud growth | "their absence leading to unconstrained growth of the stalk and bud compartments" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Direct in *H. neptunium*; useful as boundary phenotype for malformed multi-projection states. |
| E5 | BacA | interacts_with | LmdC | "the H. neptunium M23 homolog LmdC binds bactofilin in vitro" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Direct biochemical interaction; strong edge for conserved morphogenesis module. |
| E6 | LmdC (M23 endopeptidase) | required_for | proper cell shape | "LmdC ... is required for correct cell shape in vivo" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Direct experimental evidence; phenotype is not specifically 'star-shaped' but supports projection/cell-shape control. |
| E7 | BacA–LmdC module | promotes | local peptidoglycan remodeling | "bactofilins and M23 peptidases form a conserved functional module that promotes local changes in the mode of cell wall biosynthesis" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Strong mechanistic synthesis from 2024 paper; object phrased as PG remodeling/cell wall biosynthesis change. |
| E8 | local peptidoglycan remodeling | drives | cell shape determination | "thereby driving cell shape determination in morphologically complex bacteria" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 1-2) | Generalized edge; direct article conclusion but not star-shape-specific. |
| E9 | BacA | recruits | LmdC to curvature/growth zones | "BacA directly binds the N-terminal cytoplasmic region of LmdC" and "BacA homologs recruit LmdC homologs to specific subcellular locations" | 10.1101/2023.02.27.530196 — https://doi.org/10.1101/2023.02.27.530196 — 2023-03 | (pohl2023adynamicbactofilin pages 12-14) | Direct in preprint; strong but preprint status should be noted. |
| E10 | loss of bacA | causes | wide and branched cellular extensions | "stalks ... remodeled into wide and often branched cellular extensions" | 10.1101/2023.02.27.530196 — https://doi.org/10.1101/2023.02.27.530196 — 2023-03 | (pohl2023adynamicbactofilin pages 12-14) | Direct mutant phenotype; highly relevant as malformed multi-radiating/projection morphology analog. |
| E11 | uncontrolled peptidoglycan incorporation | causes | bulges / branched extensions | "uncontrolled peptidoglycan incorporation leading to bulges" | 10.1101/2023.02.27.530196 — https://doi.org/10.1101/2023.02.27.530196 — 2023-03 | (pohl2023adynamicbactofilin pages 12-14) | Direct phenotype interpretation in *H. neptunium*; useful mechanistic edge for projection dysmorphogenesis. |
| E12 | BacA polymers | create_barrier_to | elongasome movement | "Bactofilin polymers act as a physical/functional barrier that restricts movement of elongasome complexes" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 19-21) | Mechanistic model with strong support in source; partly interpretive, still suitable as uncertain mechanistic edge. |
| E13 | restriction of elongasome movement | confines | peptidoglycan biosynthesis to growth zones | "thereby confines peptidoglycan biosynthesis to specific growth zones" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 19-21) | Mechanistic model; supports zonal growth node for radiating projections. |
| E14 | BacA | concentrates | LmdC at stalk bases and bud necks | "loss of bacA ... disrupts LmdC concentration at stalk bases and bud necks" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 19-21) | Direct localization dependence in *H. neptunium*. |
| E15 | loss of bacA | causes | pseudo-stalks and unregulated budding | "producing pseudo-stalks and unregulated budding" | 10.7554/eLife.86577.2 — https://doi.org/10.7554/eLife.86577.2 — 2024-01 | (pohl2024adynamicbactofilin pages 19-21) | Direct phenotype; strong for malformed projection states related to star-like outlines. |
| E16 | BacA | positions | SpmX | "terminal domains ... may be involved in ... interactions with the stalk-specific morphological regulator SpmX" and loss of BacA causes "SpmX mislocalization" | 10.1101/2024.12.16.628611 — https://doi.org/10.1101/2024.12.16.628611 — 2024-12 | (jacq2024functionalspecializationof pages 1-6) | Preprint and somewhat summarized wording, but mechanistically important in *Asticcacaulis biprosthecum*. |
| E17 | SpmX | regulates | localized peptidoglycan synthesis | "anchors the developmental regulator SpmX, which then regulates localized peptidoglycan (PG) synthesis" | 10.1101/2024.12.16.628611 — https://doi.org/10.1101/2024.12.16.628611 — 2024-12 | (jacq2024functionalspecializationof pages 1-6) | Direct summary from preprint abstract/context; strong but preprint. |
| E18 | loss of BacA | causes | unregulated PG insertion | "loss of BacA ... causes SpmX mislocalization and unregulated PG insertion" | 10.1101/2024.12.16.628611 — https://doi.org/10.1101/2024.12.16.628611 — 2024-12 | (jacq2024functionalspecializationof pages 1-6) | Direct summary from preprint; relevant to mechanism of abnormal projections. |
| E19 | unregulated PG insertion | causes | pseudostalks | "producing short, wide 'pseudostalks'" | 10.1101/2024.12.16.628611 — https://doi.org/10.1101/2024.12.16.628611 — 2024-12 | (jacq2024functionalspecializationof pages 1-6) | Direct phenotype in *A. biprosthecum*; likely transferable only to prosthecate relatives. |
| E20 | bactofilins | recruit/localize | PbpC to prosthecate pole | "in C. crescentus bactofilins localize the bifunctional PBP PbpC to the prosthecate pole" | 10.1016/j.tim.2017.09.012 — https://doi.org/10.1016/j.tim.2017.09.012 — 2018-03 | (caccamo2018themolecularbasis pages 7-9) | Review-supported, not a primary experiment here; still useful as conserved prostheca mechanism. |
| E21 | PbpC localization at prosthecate pole | promotes | prostheca synthesis | "deletion reduces prostheca synthesis" | 10.1016/j.tim.2017.09.012 — https://doi.org/10.1016/j.tim.2017.09.012 — 2018-03 | (caccamo2018themolecularbasis pages 7-9) | Review-level evidence; indirect for star shape but relevant to multi-prostheca mechanisms. |
| E22 | SpmX | positions/co-opts | prostheca synthesis site | "SpmX ... has been co-opted as a morphogen to position prosthecae via zonal peptidoglycan remodeling" | 10.1016/j.tim.2017.09.012 — https://doi.org/10.1016/j.tim.2017.09.012 — 2018-03 | (caccamo2018themolecularbasis pages 7-9) | Review synthesis; strong conceptually, but not direct star-shaped evidence. |
| E23 | ancestral polar prostheca repositioning | results_in | bilateral prosthecae | "shifted to subpolar ... and then bilateral arrangements (A. biprosthecum) yielding two prosthecae opposite each other at midcell" | 10.1016/j.tim.2017.09.012 — https://doi.org/10.1016/j.tim.2017.09.012 — 2018-03 | (caccamo2018themolecularbasis pages 7-9) | Evolutionary/morphogenetic edge; useful for multi-projection logic, though not a molecular causal edge. |
| E24 | HADA-labeled PG incorporation | localizes_to | hyphal tips | "HADA labeling ... shows peptidoglycan (PG) incorporation is terminal at hyphal tips" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 11-13) | Direct imaging in *Rhodomicrobium vannielii*; strong evidence for tip growth in radiating projections. |
| E25 | BacA | localizes_near | hyphal tips | "BacA localizes tightly associated with tips but slightly distal to the PG incorporation peak" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 11-13) | Direct localization evidence in *R. vannielii*. |
| E26 | BacA | recruits/positions | BacC | "BacC localization depends on BacA" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 11-13) | Direct dependency; supports hierarchical scaffold assembly in projection morphogenesis. |
| E27 | BacA and BacB | form | polymeric filaments/bundles | "BacA and BacB form polymeric filament/bundle structures autonomously" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 11-13) | Direct assay-based evidence; supports cytoskeletal scaffold node. |
| E28 | overexpression of BacB or BacC | causes | buckled hyphae | "overexpression of BacB or BacC yields buckled hyphae" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 11-13) | Direct phenotype; indicates dosage sensitivity of projection shape control. |
| E29 | loss of bacA | causes | kinked/buckled hyphae | "Loss of bacA produces kinked/buckled hyphae" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 13-15, richter2023interactingbactofilinsimpact pages 15-16) | Direct mutant phenotype in *R. vannielii*; useful for maintenance of slender radiating arms. |
| E30 | bactofilins | maintain | straight narrow projections | "implying bactofilins contribute to maintaining straight, narrow projections" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 13-15) | Interpretive inference from mutant phenotypes; curate as uncertain/generalized. |
| E31 | higher 3–3 PG crosslinks / LD-transpeptidase activity | increases | stalk stiffness | "higher 3–3 crosslinks produced by LD-transpeptidases ... correlate with stiffer stalks" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 15-16) | Correlative/mechanistic inference from discussion; not directly tested for star-shape. |
| E32 | misregulated hypha-specific LD-transpeptidases | causes | flexible buckled PG / kinked hyphae | "misregulation ... can produce too-flexible, improperly modified PG giving kinks/buckles" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 15-16) | Explicitly speculative; mark uncertain and do not over-curate. |
| E33 | absence of canonical elongasome/MreB in some Alphaproteobacteria | necessitates | alternative polar growth module | "R. vannielii lacks a canonical elongasome and MreB, implying polar/divisome components are repurposed for apical growth" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 15-16) | Comparative mechanistic inference; useful background edge, not star-shape-specific. |
| E34 | peptidoglycan insertion | occurs_at | stalk base, stalk tip, bud neck, swarmer compartment | "four distinct peptidoglycan insertion zones were identified" | 10.32469/10355/79574 — https://doi.org/10.32469/10355/79574 — 2019 | (williams2019mechanismsofpolar pages 32-37) | Strong quantitative spatial evidence in *H. neptunium*; thesis source, not peer-reviewed article. |
| E35 | zonal PG insertion at stalk base | drives | stalk growth | "zonal insertion at the stalk base for stalk growth" | 10.32469/10355/79574 — https://doi.org/10.32469/10355/79574 — 2019 | (williams2019mechanismsofpolar pages 32-37) | Direct from summarized thesis evidence; supports growth-zone node. |
| E36 | dispersed PG insertion at stalk tip | drives | bud formation | "dispersed insertion at the stalk tip to form the bud" | 10.32469/10355/79574 — https://doi.org/10.32469/10355/79574 — 2019 | (williams2019mechanismsofpolar pages 32-37) | Direct in *H. neptunium*; important for branching/projection transition logic. |
| E37 | phosphate/nutrient starvation | modulates | prostheca elongation | "Environmental cues (e.g., phosphate starvation) can modulate prosthecae elongation" | 10.1371/journal.pgen.1010788 — https://doi.org/10.1371/journal.pgen.1010788 — 2023-05 | (richter2023interactingbactofilinsimpact pages 13-15) | Weak/background claim in summarized context; should be marked uncertain until primary citation is checked. |
| E38 | star-shaped morphology in some Chlamydiales preparations | may_be_artifact_of | fixation method | "Crescent and star shapes of members of the Chlamydiales order: impact of fixative methods" | 10.1007/s10482-013-9999-9 — https://doi.org/10.1007/s10482-013-9999-9 — 2013-08 | (richter2023interactingbactofilinsimpact pages 2-4) | Boundary-case warning rather than positive causal edge; useful to avoid curating fixation artifacts as biology. |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for a TraitMech causal graph of the microbial 'star shaped' morphology trait. It prioritizes recent mechanistic studies on prosthecate and multipolar growth systems, while flagging taxon-specific, inferred, or artifact-prone claims for cautious curation.*

## 5. Recent developments and latest research (prioritizing 2023–2024)

### 5.1 2023–2024: a conserved **BacA–LmdC (bactofilin–M23 endopeptidase)** module for morphogenesis
A major advance is the explicit mechanistic linking of a cytoskeletal scaffold (bactofilin) to a specific PG hydrolase class (M23 endopeptidase):
- Bactofilin polymers localize to morphogenetic zones (stalk base, bud neck), and LmdC binds bactofilin and is required for shape (pohl2024adynamicbactofilin pages 1-2).
- Model schematics and microscopy show BacA and LmdC co-localization and propose that bactofilin assemblies create topological barriers and target remodeling activity to specific curvature/growth zones (pohl2023adynamicbactofilin media e51c436f, pohl2023adynamicbactofilin media 9663cd1f).

This is directly relevant to star-shaped phenotypes because star-like outlines can be produced by **replicating such growth-zone modules at multiple sites**, consistent with “multiple radiating projections from a central body.”

### 5.2 2023: Genetic tractability and multipolar projection control in *Rhodomicrobium vannielii*
Richter et al. (2023) introduce and exploit genetic tools to show that *R. vannielii* bactofilins (BacA/BacB/BacC) are associated with hyphal growth zones and that at least one paralog is essential for proper hypha formation (richter2023interactingbactofilinsimpact pages 1-2). Specific findings useful for curation include:
- Tip-localized PG insertion (HADA signal at hyphal tips) (richter2023interactingbactofilinsimpact pages 11-13).
- BacA localization at/near hyphal tips, slightly distal to the tip incorporation peak, consistent with a scaffolding/positioning role (richter2023interactingbactofilinsimpact pages 11-13).
- Interaction dependencies among bactofilins (BacC localization depends on BacA) and morphology phenotypes (buckled hyphae upon perturbation) (richter2023interactingbactofilinsimpact pages 11-13).

### 5.3 2024: Domain-level understanding of bactofilin function in prostheca morphogenesis
In *Asticcacaulis biprosthecum*, BacA functions as a topological organizer of stalk synthesis and influences localization and interactions (including with SpmX), with disruptions producing pseudostalk phenotypes (jacq2024functionalspecializationof pages 1-6). While preprint status warrants caution, the domain dissection strengthens mechanistic node definitions (polymerization, membrane association, client interactions).

## 6. Current applications and real-world implementations

### 6.1 Practical “implementations” in research and diagnostics: microscopy-based phenotyping pipelines
The star-shaped phenotype is typically observed in microscopy, and the most *operationally reliable* implementation for linking mechanism to phenotype is **live-cell or controlled-preparation imaging of PG insertion and protein localization**:
- **Fluorescent D-amino-acid labeling (e.g., HADA)** to map new PG incorporation in projections/tips (richter2023interactingbactofilinsimpact pages 11-13).
- **Demograph analysis across many cells** (e.g., n=200 per condition in *R. vannielii*) to quantify spatial distributions of signals and compare to PG insertion patterns (richter2023interactingbactofilinsimpact pages 11-13).
- **Protein interaction assays (BACTH) and in vitro binding** to ground edges like BacA–BacC and BacA–LmdC (richter2023interactingbactofilinsimpact pages 11-13, pohl2023adynamicbactofilin pages 12-14).

These pipelines are directly transferable to any candidate “star-shaped” organism to validate whether the arms correspond to multiple discrete growth zones.

### 6.2 Translational relevance: cell-wall morphogenesis as a design/control target
Although not “applications” in the engineering sense in the retrieved evidence set, the mechanistic advances are immediately relevant to:
- **Antimicrobial target discovery**, because localized PG synthesis/remodeling modules (bactofilin-client interactions; M23 endopeptidases; PBPs; LDTs) are potential vulnerabilities in morphologically complex bacteria (pohl2024adynamicbactofilin pages 1-2, caccamo2018themolecularbasis pages 7-9).
- **Morphology engineering in biotechnology**, where controlling projection formation could alter surface attachment, nutrient access, or spatial organization in biofilms—traits often correlated with prosthecate lifestyles in oligotrophic aquatic environments (caccamo2018themolecularbasis pages 7-9).

## 7. Relevant statistics and data points (from available evidence)

Quantitative values and counts available in the retrieved sources include:
- **Four** distinct PG insertion zones in *Hyphomonas neptunium* (swarmer dispersed; stalk base zonal; stalk tip dispersed for bud; bud neck zonal for division) (williams2019mechanismsofpolar pages 32-37).
- Timing in *H. neptunium*: initial stalk + first bud formation takes ~**4 h**, subsequent buds every ~**2.5 h** (williams2019mechanismsofpolar pages 32-37).
- Biochemical binding: BacA–LmdC interaction with apparent **KD ~15 µM** (pohl2023adynamicbactofilin pages 12-14).
- Spatial quantification: demographs with **200 cells per condition** in *R. vannielii* analyses (richter2023interactingbactofilinsimpact pages 11-13).

These data are most directly useful as *assay constraints* and *model priors* for star-shaped candidate organisms (e.g., expecting multiple insertion zones; quantifying how many arms correspond to how many stable growth zones).

## 8. Expert interpretation / analysis (curation guidance)

### 8.1 What is ready to curate with high confidence
Edges connecting **bactofilins (BacA-family)** → **localized PG remodeling/synthesis** → **projection/stalk/bud/hypha morphogenesis** are repeatedly supported across taxa and are strongly evidenced (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21, richter2023interactingbactofilinsimpact pages 11-13).

In particular, the **BacA–LmdC module** is both mechanistically specific and well supported by localization/interaction evidence and is therefore a high-priority causal subgraph to include, even if the trait is “star shaped” rather than “stalked/budding” per se (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin pages 12-14).

### 8.2 What remains uncertain for star-shape-specific curation
- **Star-shaped exemplars (e.g., Stella/Ancalomicrobium):** In the current retrieved evidence, these genera appear only as exemplars in review context rather than as mechanistically interrogated systems; therefore, edges specifically asserting that the BacA–LmdC/SpmX/PBP modules *cause* star shape in those taxa should be marked **uncertain** until primary morphology/genetics data are added.
- **Environmental triggers (phosphate starvation / nutrient limitation) → star shape:** Environmental modulation of prostheca length is noted in context, but direct causal evidence linking a specific cue to star-shaped multi-arm geometry is not established in the retrieved excerpts and should not be curated without checking the primary sources (richter2023interactingbactofilinsimpact pages 13-15).
- **LD-transpeptidases and crosslinking → projection rigidity:** Discussed as correlates/speculation; curate only as tentative edges unless direct experimental evidence is added (richter2023interactingbactofilinsimpact pages 15-16).

### 8.3 Warning on artifact-prone “star-shaped” observations
Because star-like shapes can be preparation dependent in some taxa (fixative effects), curation should prefer:
- live-cell imaging, or
- multiple fixation protocols with consistent morphology,
before encoding “star shaped” as a stable trait for a given organism (richter2023interactingbactofilinsimpact pages 2-4).

## 9. DOI-first bibliography (with URLs and publication dates)

1. **Richter P, Melzer B, Müller FD.** *Interacting bactofilins impact cell shape of the MreB-less multicellular Rhodomicrobium vannielii.* **PLOS Genetics** (2023-05). DOI: **10.1371/journal.pgen.1010788**. https://doi.org/10.1371/journal.pgen.1010788 (richter2023interactingbactofilinsimpact pages 11-13)
2. **Pöhl S, Osorio-Valeriano M, et al.** *A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.* **eLife** (version DOI record; 2024-01). DOI: **10.7554/eLife.86577.2**. https://doi.org/10.7554/eLife.86577.2 (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 19-21, pohl2023adynamicbactofilin media e51c436f, pohl2023adynamicbactofilin media 9663cd1f)
3. **Pöhl S, Osorio-Valeriano M, et al.** *A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.* **bioRxiv** (2023-03). DOI: **10.1101/2023.02.27.530196**. https://doi.org/10.1101/2023.02.27.530196 (pohl2023adynamicbactofilin pages 12-14)
4. **Jacq M, Caccamo PD, Brun YV.** *Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in Asticcacaulis biprosthecum.* **bioRxiv** (2024-12). DOI: **10.1101/2024.12.16.628611**. https://doi.org/10.1101/2024.12.16.628611 (jacq2024functionalspecializationof pages 1-6)
5. **Caccamo PD, Brun YV.** *The molecular basis of noncanonical bacterial morphology.* **Trends in Microbiology** (2018-03). DOI: **10.1016/j.tim.2017.09.012**. https://doi.org/10.1016/j.tim.2017.09.012 (caccamo2018themolecularbasis pages 7-9, caccamo2018themolecularbasis pages 28-30)
6. **Williams MA.** *Mechanisms of polar growth in the alphaproteobacterial order Rhizobiales.* **PhD thesis** (2019). DOI: **10.32469/10355/79574**. https://doi.org/10.32469/10355/79574 (williams2019mechanismsofpolar pages 32-37)
7. **Rusconi B, Lienard J, et al.** *Crescent and star shapes of members of the Chlamydiales order: impact of fixative methods.* **Antonie van Leeuwenhoek** (2013-08). DOI: **10.1007/s10482-013-9999-9**. https://doi.org/10.1007/s10482-013-9999-9 (richter2023interactingbactofilinsimpact pages 2-4)

## 10. Curation warnings (claims not yet ready)

1. **Do not curate “Stella/Ancalomicrobium star-shape mechanism” edges** from the current evidence set; primary mechanistic sources are missing here.
2. **Treat environmental cue edges** (e.g., phosphate starvation → prostheca elongation → star shape) as **uncertain** until primary experimental citations are added (richter2023interactingbactofilinsimpact pages 13-15).
3. **Flag fixation-dependent star shapes** as potential artifacts unless validated by live-cell or robust prep controls (richter2023interactingbactofilinsimpact pages 2-4).

---

## Appendix: Visual evidence (figures)

Microscopy and model schematics supporting BacA/LmdC localization and the proposed barrier/remodeling model for localized projection morphogenesis are available in the retrieved figures (pohl2023adynamicbactofilin media e51c436f, pohl2023adynamicbactofilin media 9663cd1f).

References

1. (richter2023interactingbactofilinsimpact pages 1-2): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

2. (richter2023interactingbactofilinsimpact pages 2-4): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (caccamo2018themolecularbasis pages 7-9): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 79 citations and is from a domain leading peer-reviewed journal.

4. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

5. (pohl2024adynamicbactofilin pages 19-21): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

6. (richter2023interactingbactofilinsimpact pages 11-13): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (pohl2023adynamicbactofilin media e51c436f): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. BioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.02.27.530196, doi:10.1101/2023.02.27.530196. This article has 0 citations.

8. (pohl2023adynamicbactofilin media 9663cd1f): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. BioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.02.27.530196, doi:10.1101/2023.02.27.530196. This article has 0 citations.

9. (pohl2023adynamicbactofilin pages 12-14): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. BioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.02.27.530196, doi:10.1101/2023.02.27.530196. This article has 0 citations.

10. (williams2019mechanismsofpolar pages 32-37): Michelle A. Williams. Mechanisms of polar growth in the alphaproteobacterial order rhizobiales. PhD thesis, University of Missouri Libraries, 2019. URL: https://doi.org/10.32469/10355/79574, doi:10.32469/10355/79574.

11. (richter2023interactingbactofilinsimpact pages 13-15): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (richter2023interactingbactofilinsimpact pages 15-16): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (jacq2024functionalspecializationof pages 1-6): Maxime Jacq, Paul D. Caccamo, and Yves V. Brun. Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in asticcacaulis biprosthecum. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.16.628611, doi:10.1101/2024.12.16.628611. This article has 1 citations.

14. (caccamo2018themolecularbasis pages 28-30): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 79 citations and is from a domain leading peer-reviewed journal.