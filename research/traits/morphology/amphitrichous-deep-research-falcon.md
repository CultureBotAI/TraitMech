---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:16:40.340082'
end_time: '2026-06-18T06:37:27.023897'
duration_seconds: 1246.68
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: amphitrichous
  trait_identifier: traitmech:000059
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: amphitrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with flagella (single filaments or tufts) at
    both poles of the cell.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar
    (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.)
    | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments
    as locomotory organelles.)'
  causal_graph_summary: 'amphitrichous_bipolar_flagella: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** amphitrichous
- **METPO identifier:** traitmech:000059
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella (single filaments or tufts) at both poles of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.) | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments as locomotory organelles.)
- **Existing causal graph summary:** amphitrichous_bipolar_flagella: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **amphitrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/amphitrichous.yaml`.

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
- **Trait label:** amphitrichous
- **METPO identifier:** traitmech:000059
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella (single filaments or tufts) at both poles of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe bipolar (amphitrichous) flagellation among the flagellation patterns governed by FlhF/FlhG.) | DOI:10.3390/biom9070279:  (Flagellum review supports polar flagellar filaments as locomotory organelles.)
- **Existing causal graph summary:** amphitrichous_bipolar_flagella: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **amphitrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/amphitrichous.yaml`.

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


## Microbial Trait Causal Graph Research Report: **amphitrichous** (METPO:traitmech:000059)

### Scope summary (trait meaning, assay context, and boundaries)
**Amphitrichous** flagellation (also called **bipolar** flagellation) is a **flagellar arrangement phenotype** defined morphologically as **a single flagellum at each pole of the cell**. This phenotype is classically exemplified by *Campylobacter jejuni*, which “constructs one flagellum at each pole, a pattern known as amphitrichous flagellation”. (cohen2020campylobacterjejunimotility pages 1-2)

**Distinguishing from nearby traits/patterns**:
- **Monotrichous (polar monotrichous)**: a single flagellum at one pole (chu2020phylogeneticdistributionultrastructure pages 1-3, nedeljkovic2021bacterialflagellarfilament pages 1-2).
- **Lophotrichous**: multiple flagella (tuft) at one pole; can also occur as **bipolar lophotrichous** (tufts at both poles) which is distinct from amphitrichous because amphitrichous specifies *single* filaments at each pole (grognot2021morethanpropellers pages 4-5, grognot2021morethanpropellers pages 1-2).
- **Peritrichous**: multiple flagella distributed over the cell surface (chu2020phylogeneticdistributionultrastructure pages 1-3, nedeljkovic2021bacterialflagellarfilament pages 1-2).

**Boundary cases and curation cautions**:
- Some taxa have **mixed systems** (e.g., polar plus lateral flagella; or sheathed polar and unsheathed lateral flagella), complicating morphology-only classification (chu2020phylogeneticdistributionultrastructure pages 1-3).
- Spirochete **periplasmic/endoflagella** are often treated separately from canonical external flagellar arrangements (thomasUnknownyearthedesignof pages 57-59, chu2020phylogeneticdistributionultrastructure pages 1-3).

### Key concepts and current understanding (mechanistic framing)
Amphitrichous flagellation is a **patterning problem**: cells must (i) select poles as assembly sites and (ii) regulate number/placement of motors/filaments. In many polar-flagellated bacteria, a conserved module of NTPases and polarity factors contributes to this patterning:
- **FlhF**: SRP-type GTPase; a positive determinant of polar flagellum placement/assembly (arroyoperez2024aconservedcellpole pages 2-3).
- **FlhG**: MinD/ParA-family ATPase; often a negative regulator restricting flagellar number and antagonizing FlhF (arroyoperez2024aconservedcellpole pages 14-15, arroyoperez2024aconservedcellpole pages 2-3).
- **HubP/FimV**: polar landmark scaffold recruiting/coupling proteins at the pole; interacts with FlhF in *Shewanella* model (dornes2024polarconfinementof pages 4-6).
- **FipA**: a 2024-discovered conserved membrane protein that binds FlhF and promotes its polar membrane targeting/activity (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15).

**Important caveat for this trait**: amphitrichous is a **cell-level morphology** and is **not synonymous** with “polar flagellation controlled by FlhF/FlhG”. The best-supported mechanistic work in 2023–2024 explains **polar placement** generally (and monopolar systems), and should be curated with explicit taxon/model scope tags when applied to amphitrichous lineages.

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) 2024: HubP–FlhF–FliG/FliF recruitment cascade (domain-resolved)
A major 2024 mechanistic advance (Nature Communications) provides a **molecular recruitment cascade** connecting a pole landmark to early flagellar assembly:
- **FlhF binds FliG strongly**, and this is specific to the **polar** flagellar system in *Shewanella putrefaciens* (dornes2024polarconfinementof pages 2-4).
- The **N-terminal B-domain/FID of FlhF** is **necessary and sufficient** for FliG binding (N-terminal 60 aa; structured 44-aa domain) (dornes2024polarconfinementof pages 2-4).
- **FlhF-bound FliG can interact with FliF**, but **cannot interact with FliM/FliN**, suggesting FlhF biases early assembly steps and prevents premature C-ring partner association (dornes2024polarconfinementof pages 2-4).
- **FlhF NG-domain binds the cytoplasmic region of HubP (HubP-C)**, and FlhF can form a ternary complex bridging HubP and FliG (dornes2024polarconfinementof pages 4-6).
- A functional test shows that deleting the **N-terminal 44 residues of FlhF** uncouples FlhF pole localization from correct hook/flagellar placement (hooks become subpolar/lateral), demonstrating the recruitment interface is required for polar placement (dornes2024polarconfinementof pages 4-6).

A visual summary model of this recruitment cascade is provided in Dornes et al. figures (dornes2024polarconfinementof media 7605f948, dornes2024polarconfinementof media 650f532b, dornes2024polarconfinementof media 9eac1fa6, dornes2024polarconfinementof media fc913750).

#### 2) 2024: FipA as a conserved membrane licensing factor for FlhF
A 2024 eLife study identifies **FipA** (FlhF interaction partner A) as a conserved, membrane-associated FlhF activator:
- “FipA… facilitates the recruitment of FlhF to the membrane at the cell pole” and can act “in concert with… HubP/FimV” (arroyoperez2024aconservedcellpole pages 2-3).
- FipA **directly interacts with FlhF**, and loss of FipA reduces FlhF polar localization; dual loss (ΔfipA + ΔhubP/fimV) nearly abolishes FlhF polar localization (arroyoperez2024aconservedcellpole pages 14-15).
- The paper argues FipA “stimulates the activity of FlhF to initiate polar flagellation” rather than acting as a general polarity factor for all flagellar components (arroyoperez2024aconservedcellpole pages 14-15).

This is particularly relevant for TraitMech curation because it supplies a new mechanistic node (FipA) upstream of FlhF localization/activity.

#### 3) 2023: Quantitative distributions for flagella number and mislocalization phenotypes
While not amphitrichous per se, Gibson et al. (2023, *Journal of Bacteriology*) provides unusually **quantitative** phenotype distributions for FlhF/FlhG perturbations in a polarly-flagellated, multi-flagellated (lophotrichous) pathogen *Helicobacter pylori*:
- Wild-type: **mode and mean = 4 flagella/cell; SD = 1.2; 82% within 1 SD** (100-cell TEM count) (gibson2023controlofthe pages 2-5).
- ΔflhG: **wider, more even distribution**; mode = 5; mean = 3.5; SD = 2.1; **18% aflagellate or single-flagellum vs 1% in WT**; only a small fraction hyperflagellated, occasionally up to 12 flagella (gibson2023controlofthe pages 2-5).
- ΔflhF: strong hypoflagellation and mislocalization: **~30% aflagellate and ~45% single flagellum** in G27M ΔflhF; mislocalization includes **~37% lateral and ~25% subpolar** (gibson2023controlofthe pages 2-5).

These data support graph edges linking FlhF to placement and number control, and caution that ΔflhG does not always yield hyperflagellation (species/architecture dependent) (gibson2023controlofthe pages 2-5, arroyoperez2024aconservedcellpole pages 2-3).

### Current applications and real-world implementations
**Trait inference and taxonomy**: Flagellation patterns (including amphitrichous) remain used as descriptive traits in microbiology and comparative physiology; the “flagellation pattern” is noted as species-specific and a long-standing taxonomic criterion in the modern mechanistic literature that studies FlhF/FlhG-dependent pattern replication across divisions (dornes2024polarconfinementof pages 1-2).

**Pathogenesis and colonization contexts**: In amphitrichous *C. jejuni*, opposed polar flagella are linked to motility through viscous mucosa and host colonization (cohen2020campylobacterjejunimotility pages 1-2). Thus amphitrichous patterning can be seen as an ecological/host-adaptation trait (movement in viscous environments), though causal links from amphitrichous pattern *per se* to fitness require strain- and context-specific evidence.

**Mechanism-guided engineering (emerging)**: The 2024 HubP–FlhF–FliG/FliF cascade and 2024 FipA licensing provide modular targets to perturb or rewire polar flagellar placement in synthetic/experimental settings (e.g., manipulating FlhF recruitment, landmark binding, or early assembly bias). This is mostly research-stage rather than deployed biotechnology, but it is a clear mechanistic framework for rational perturbation (dornes2024polarconfinementof pages 4-6, arroyoperez2024aconservedcellpole pages 14-15).

### Expert opinions and authoritative synthesis
Recent primary studies emphasize that polar flagellation is governed by a **coordinated localization + assembly checkpoint**, rather than by FlhF localizing “autonomously.” The eLife 2024 paper explicitly argues against FlhF self-localization and frames FlhF recruitment as mediated by factors like FipA and HubP/FimV (arroyoperez2024aconservedcellpole pages 2-3). The Nat Commun 2024 paper offers a domain-level molecular mechanism consistent with that view: FlhF links a pole landmark to early ring components via separable domains (dornes2024polarconfinementof pages 2-4, dornes2024polarconfinementof pages 4-6).

### Candidate nodes for `amphitrichous.yaml` (grouped by type; grounding suggestions)
Below are candidate nodes strongly motivated by 2023–2024 mechanistic evidence (and a few definition nodes). For ontology grounding, GO identifiers are suggested where stable; many protein identifiers will be taxon-specific and should be curated as **label-only** nodes unless a UniProt accession is selected per taxon during curation.

#### Phenotype / trait nodes
- **amphitrichous** (METPO:traitmech:000059) (cohen2020campylobacterjejunimotility pages 1-2)
- bipolar flagella (synonym label) (chu2020phylogeneticdistributionultrastructure pages 1-3)
- polar flagellum arrangement (related phenotype label) (chu2020phylogeneticdistributionultrastructure pages 1-3)
- flagellar number per cell (assay phenotype) (gibson2023controlofthe pages 2-5)
- flagellar localization categories: polar / subpolar / lateral (assay phenotype) (gibson2023controlofthe pages 2-5)

#### Cellular structures / processes
- flagellum (GO:0097588 suggested) (chu2020phylogeneticdistributionultrastructure pages 1-3)
- MS ring (flagellar basal-body MS ring; GO term exists but may vary by ontology release) (dornes2024polarconfinementof pages 2-4)
- C ring / switch complex (process/structure label) (dornes2024polarconfinementof pages 2-4)
- flagellar hook (structure; labeled in Dornes via hook stains) (dornes2024polarconfinementof pages 4-6)

#### Genes/proteins/complexes (mechanistic entities)
- **FlhF** (SRP-type GTPase; localization/assembly organizer) (dornes2024polarconfinementof pages 2-4)
- **FlhG** (MinD/ParA-family ATPase; FlhF antagonist; number restriction) (arroyoperez2024aconservedcellpole pages 14-15)
- **HubP/FimV** (polar landmark scaffold) (dornes2024polarconfinementof pages 4-6)
- **FipA** (FlhF interaction partner; membrane licensing/recruitment) (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15)
- **FliG** (C-ring protein; early assembly interface) (dornes2024polarconfinementof pages 2-4)
- **FliF** (MS-ring protein) (dornes2024polarconfinementof pages 2-4)
- **FliM/FliN** (C-ring partners; interaction prevented by FlhF-bound state) (dornes2024polarconfinementof pages 2-4)
- **FlrA/FleQ** (flagellar master regulator; FlhG interaction/repression in model) (arroyoperez2024aconservedcellpole pages 14-15)

#### Environmental/experimental factors and assays
- soft agar motility (swim halo diameter) (gibson2023controlofthe pages 2-5)
- TEM flagella counting (100 cells) (gibson2023controlofthe pages 2-5)

### Candidate causal edges (curation table)
The following table is prepared for direct curation and includes quotes, DOIs, URLs, publication dates, and uncertainty notes.

| Edge (Subject —predicate→ Object) | Edge type | Proposed node grounding | Strength/uncertainty | Key evidence snippet | Source | DOI | URL | Publication date | Curation notes |
|---|---|---|---|---|---|---|---|---|---|
| amphitrichous —has_definition→ flagellar arrangement with one flagellum at each pole | phenotype | amphitrichous = METPO:traitmech:000059; flagellum = GO:0097588 | Strong | “C. jejuni constructs one flagellum at each pole, a pattern known as amphitrichous flagellation” (cohen2020campylobacterjejunimotility pages 1-2) | Cohen 2020, *PLoS Pathogens* | 10.1371/journal.ppat.1008620 | https://doi.org/10.1371/journal.ppat.1008620 | 07/2020 | Good trait-defining edge; use as scope anchor, not mechanism. |
| amphitrichous —synonym_of→ bipolar flagellation | phenotype | amphitrichous = METPO:traitmech:000059; bipolar flagella = label-only | Strong | “a single flagellum at each cell pole (amphitrichous or bipolar flagella)” (chu2020phylogeneticdistributionultrastructure pages 1-3) | Chu 2020, *Biomolecules* | 10.3390/biom10030363 | https://doi.org/10.3390/biom10030363 | 02/2020 | Useful synonym mapping for curation; morphology only. |
| FlhF —binds→ FliG (polar-system FliG) | molecular interaction | FlhF = label-only SRP-type GTPase; FliG = GO:0097589-associated flagellar C ring protein, label-only gene product | Strong | “FlhF did not interact with FliF-C, FliM, or FliN, it exhibited a strong interaction with FliG” and “FlhF specifically interacts with FliG from the polar flagellar system” (dornes2024polarconfinementof pages 2-4) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Strong biochemical evidence; demonstrated in *Shewanella putrefaciens*; likely generalizable to FlhF-dependent polar systems but taxon scope should be noted. |
| FlhF N-terminal FID/B-domain —mediates_binding_to→ FliG | molecular interaction | FlhF FID = label-only domain; FliG = label-only gene product | Strong | “The N-terminal 60 amino acids are necessary and sufficient for the interaction of FlhF and FliG” (dornes2024polarconfinementof pages 2-4) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Domain-resolved mechanism; suitable for a finer-grained graph if domains are allowed as nodes. |
| FlhF-bound FliG —binds→ FliF | molecular interaction | FliG = label-only; FliF/MS ring protein = GO:0097560 or label-only | Strong | “When bound to FlhF, FliG was able to interact with the cytoplasmic domain of the flagellar MS-ring forming protein FliF” (dornes2024polarconfinementof pages 2-4) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Supports early assembly cascade toward polar flagellum formation. |
| FlhF-bound FliG —prevents_interaction_with→ FliM/FliN | regulation | FliG, FliM, FliN = label-only flagellar C-ring proteins | Strong | “Upon binding to FlhF, FliG exhibited an inability to interact with FliM/N” (dornes2024polarconfinementof pages 2-4) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Negative edge; indicates FlhF biases FliG toward FliF capture rather than mature C-ring interactions. |
| FlhF NG-domain —binds→ HubP cytoplasmic region | molecular interaction | FlhF NG domain = label-only; HubP/FimV = polar landmark protein, label-only | Strong | “the NG domain of FlhF is required for the interaction with HubP-C” and interaction is with “residues 860–1033” (dornes2024polarconfinementof pages 4-6) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Strong direct interaction evidence; *S. putrefaciens* HubP homologous to FimV-type polar landmarks. |
| FlhF —bridges→ HubP and FliG | localization | FlhF, HubP, FliG = label-only | Strong | “FlhF is able to bridge HubP and FliG in vitro” (dornes2024polarconfinementof pages 4-6) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Excellent candidate edge for recruitment cascade; mechanistic but in vitro. |
| HubP —recruits_to_pole→ FlhF–FliG complex | localization | HubP/FimV = label-only; FlhF–FliG complex = label-only complex | Moderate | “The FlhF-FliG complex is then recruited to the designated cell pole by HubP” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Mechanistic statement cites Dornes model; strong conceptual support, but may be partly model-based outside *S. putrefaciens*. |
| FlhF-bound FliG —captures→ FliF | localization | FliG = label-only; FliF = label-only MS-ring protein | Moderate | “FlhF-bound FliG captures the transmembrane protein FliF and promotes formation of the MS-ring” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Secondary mechanistic summary of Dornes model; reasonable graph edge but note source summarizes prior 2024 study. |
| FliF capture —promotes_formation_of→ MS ring | localization | FliF/MS ring = GO:0097560 or label-only; MS ring formation = GO label-only | Moderate | “captures the transmembrane protein FliF and promotes formation of the MS-ring” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Early flagellar assembly edge; useful if graph includes assembly intermediate. |
| GTP-bound dimeric FlhF —localizes_to→ cell pole | localization | FlhF = label-only; cell pole = GO:0044459? label-only preferred if uncertain | Strong | “GTP-bound dimeric FlhF localizes to the cell pole” / “localizes to the cell pole to where it recruits the initial flagellar building blocks” (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Central positive localization step in FlhF/FlhG model. |
| FlhF —recruits→ initial flagellar building blocks | localization | FlhF = label-only; initial flagellar building blocks = label-only process/node | Moderate | “GTP-bound dimeric FlhF… recruits the initial flagellar building blocks” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Broad process-level edge; may be too generic unless refined to FliG/FliF. |
| FipA —directly_interacts_with→ FlhF | molecular interaction | FipA = label-only membrane protein with DUF2802; FlhF = label-only | Strong | “In all three species, FipA directly interacts with FlhF” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Strong multi-species evidence (*Vibrio parahaemolyticus*, *Pseudomonas putida*, *Shewanella putrefaciens*). |
| FipA —facilitates_recruitment_of→ FlhF to cell pole membrane | localization | FipA = label-only; FlhF = label-only; membrane/cell pole = GO label-only | Strong | “FipA… facilitates the recruitment of FlhF to the membrane at the cell pole” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Good candidate edge; explicitly framed as causal recruitment. |
| FipA —promotes→ FlhF polar localization | localization | FipA = label-only; FlhF polar localization = label-only process | Strong | “In the absence of FipA, polar localization of FlhF was significantly decreased in all three species” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Strong loss-of-function support; multi-species. |
| FipA membrane localization/TM domain —required_for→ FlhF-targeting function | regulation | FipA TM domain = label-only domain; FlhF targeting = label-only process | Strong | “a FipA mutant lacking its N-terminal transmembrane domain was non-functional” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Domain-specific requirement; may be too fine-grained for first-pass graph. |
| FipA —stimulates→ FlhF activity to initiate polar flagellation | regulation | FipA = label-only; FlhF activity = label-only; polar flagellation = label-only | Moderate | “FipA does not act as a general polarity factor… but rather it stimulates the activity of FlhF to initiate polar flagellation” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Strong narrative statement, but mechanistic biochemical details still incomplete. |
| HubP/FimV deletion —decreases→ FlhF polar localization | phenotype | HubP/FimV = label-only; FlhF polar localization = label-only process | Strong | “Removing HubP/FimV alone had a similar effect as removing FipA on the localization of FlhF” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Supports HubP/FimV as parallel positive pathway; species-specific strength varies. |
| FipA loss + HubP/FimV loss —almost abolishes→ FlhF polar localization | phenotype | ΔfipA + ΔhubP/fimV = label-only genotype; FlhF polar localization = label-only | Strong | “almost completely diminished when hubP or fimV was deleted together with fipA” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Suggests combinatorial pathway architecture; genotype node may be less portable for core graph. |
| HubP and FipA pathways —jointly_enable→ sufficient active FlhF for MS-ring formation | regulation | HubP/FimV = label-only; FipA = label-only; MS-ring formation = label-only | Moderate | “both are required to bring sufficient (active) FlhF molecules to trigger MS-ring formation and start flagellum assembly” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Integrative model edge; useful but more inferred than direct binary interaction. |
| FlhG —stimulates_GTPase_activity_of→ FlhF | regulation | FlhG = MinD/ParA-family ATPase, label-only; FlhF = label-only GTPase | Strong | “the ATP-bound FlhG dimer can… interact with the GTP-bound FlhF dimer, thereby stimulating its GTPase activity” (arroyoperez2024aconservedcellpole pages 14-15, gibson2023controlofthe pages 2-5) | Arroyo-Pérez 2024, *eLife*; Gibson 2023, *J Bacteriol* | 10.7554/eLife.93004.3; 10.1128/jb.00110-23 | https://doi.org/10.7554/eLife.93004.3 ; https://doi.org/10.1128/jb.00110-23 | 12/2024; 09/2023 | Cross-source consistency; central negative control edge. |
| FlhG-stimulated FlhF GTP hydrolysis —causes→ FlhF monomerization and loss of polar localization | regulation | FlhF monomerization = label-only; polar localization = label-only | Strong | “This leads to monomerization of FlhF and loss of polar localization” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Clear causal model; suitable process edge if intermediate nodes are allowed. |
| FlhG —interacts_with→ FlrA/FleQ | regulation | FlrA/FleQ = master regulator of flagella synthesis, label-only | Moderate | “Dimeric FlhG does also interact with the master regulator of flagella synthesis, FlrA (or FleQ in Pseudomonas)” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Based on integrated model and prior studies; could be curated with uncertainty flag. |
| FlhG —prevents_synthesis_of→ further early flagellar building blocks | regulation | early flagellar building blocks = label-only process; FlrA/FleQ pathway = label-only | Moderate | “prevents the synthesis of further early flagellar building blocks” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Regulation edge tied to transcriptional control; indirect and species-contextual. |
| FlhG —restricts→ number of polar flagella formed | phenotype | FlhG = label-only; flagellar number control = label-only phenotype | Strong | “FlhG links flagella synthesis with transcription regulation and effectively restricts the number of polar flagella that are formed” (arroyoperez2024aconservedcellpole pages 14-15) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Good high-level node-to-phenotype edge. |
| flhG deletion —causes→ hyperflagellated cells | phenotype | flhG gene = label-only; hyperflagellation = label-only phenotype | Strong but taxon-specific | “the absence of MinD-like ATPase FlhG results in hyper-flagellated cells” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Not universal: contradicted in *H. pylori* lophotrichous background, where ΔflhG broadened distribution and increased hypoflagellated cells. Do not over-generalize to all polar bacteria. |
| flhF deletion —causes→ reduced flagella number and mislocalized flagella | phenotype | flhF gene = label-only; flagellar localization phenotype = label-only | Strong | “A deletion of flhF results in reduced number and mis-localization of flagella” (arroyoperez2024aconservedcellpole pages 2-3) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Broad claim across polarly flagellated species; good generic edge. |
| flhF deletion in *H. pylori* —increases→ lateral/subpolar flagellar localization | phenotype | NCBITaxon:210; flhF = label-only; lateral/subpolar flagella = label-only phenotype | Strong, species-specific | “~37% of the flagella were located on the side of the cell… and ~25%… had a subpolar location in the G27M ΔflhF mutant” (gibson2023controlofthe pages 2-5, gibson2023controlofthe pages 5-7) | Gibson 2023, *Journal of Bacteriology* | 10.1128/jb.00110-23 | https://doi.org/10.1128/jb.00110-23 | 09/2023 | Quantitative phenotype, but from lophotrichous *H. pylori*, not amphitrichous bacterium. Useful for general polar localization control. |
| flhF deletion in *H. pylori* —causes→ hypoflagellation | phenotype | NCBITaxon:210; hypoflagellation = label-only | Strong, species-specific | “Approximately 30% of the H. pylori G27M ∆flhF mutant cells lacked flagella, and ~45% of the cells had a single flagellum” (gibson2023controlofthe pages 2-5) | Gibson 2023, *Journal of Bacteriology* | 10.1128/jb.00110-23 | https://doi.org/10.1128/jb.00110-23 | 09/2023 | Quantitative support for FlhF as positive assembly/localization factor. |
| flhG deletion in *H. pylori* —broadens→ flagella-per-cell distribution | phenotype | NCBITaxon:210; flagella-per-cell distribution = label-only assay phenotype | Strong, species-specific | “Four flagella per cell were both the mode and mean… In contrast, cells of the ∆flhG mutant did not display a Gaussian distribution… but instead had a wider and more even distribution” (gibson2023controlofthe pages 2-5) | Gibson 2023, *Journal of Bacteriology* | 10.1128/jb.00110-23 | https://doi.org/10.1128/jb.00110-23 | 09/2023 | Important caveat against simplistic “ΔflhG = hyperflagellated” generalization. |
| FliF N255D —partially_compensates_for→ loss of FlhF | phenotype | FliF = label-only MS-ring protein; N255D variant = label-only | Moderate, species-specific | “introducing the fliF allele into the H. pylori G27M ∆flhF mutant resulted in enhanced motility and an increased number of flagella” (gibson2023controlofthe pages 2-5) | Gibson 2023, *Journal of Bacteriology* | 10.1128/jb.00110-23 | https://doi.org/10.1128/jb.00110-23 | 09/2023 | Suppressor edge; useful as support that FlhF acts early at MS-ring assembly, but variant-specific and not core trait graph material. |
| FliF N255D —promotes→ MS-ring-like assembly in vitro | molecular interaction | FliF = label-only MS-ring protein | Moderate, species-specific | “recombinant FliFN255D formed ordered ring-like assemblies in vitro that displayed the MS ring architecture” (gibson2023controlofthe pages 2-5) | Gibson 2023, *Journal of Bacteriology* | 10.1128/jb.00110-23 | https://doi.org/10.1128/jb.00110-23 | 09/2023 | Supports assembly role of FliF downstream of FlhF; variant-specific suppressor evidence. |
| FlhF N-terminus/FID deletion —causes→ subpolar/lateral hook placement | phenotype | FlhF ΔN44 = label-only genotype; hook localization/FlgE = label-only | Strong, species-specific | “single flagellar hooks appeared in subpolar/lateral positions (about 40%, 10% polar)” (dornes2024polarconfinementof pages 4-6) | Dornes 2024, *Nature Communications* | 10.1038/s41467-024-50274-4 | https://doi.org/10.1038/s41467-024-50274-4 | 07/2024 | Strong evidence connecting FlhF-FliG interface to polar positioning; from *S. putrefaciens* monopolar system, informative but not amphitrichous-specific. |
| FlhF localization machinery —contributes_to→ polar flagellar synthesis | regulation | FlhF/FlhG/FipA/HubP module = label-only | Moderate | “FipA… is required for normal FlhF activity and function in polar flagellar synthesis” (arroyoperez2024aconservedcellpole pages 1-2) | Arroyo-Pérez 2024, *eLife* | 10.7554/eLife.93004.3 | https://doi.org/10.7554/eLife.93004.3 | 12/2024 | Higher-level module edge; useful for summary graph but less atomic than protein-protein edges. |


*Table: This table compiles candidate mechanistic and phenotype edges relevant to amphitrichous/bipolar flagellation, prioritizing 2023–2024 primary studies on FlhF/FlhG, HubP/FimV, and FipA. It is designed for TraitMech curation, with grounding suggestions, evidence snippets, and caveats about taxon specificity and boundary conditions.*

### Statistics and quantitative data highlights (recent studies)
- *H. pylori* G27M WT: mean flagella/cell = **4.0** (mode 4), SD **1.2**, **82%** within one SD (gibson2023controlofthe pages 2-5).
- *H. pylori* ΔflhG: mean **3.5**, SD **2.1**; **18%** aflagellate/single-flagellum vs **1%** in WT; occasional extreme (12 flagella) but generally not strongly hyperflagellated (gibson2023controlofthe pages 2-5).
- *H. pylori* ΔflhF: **~30%** aflagellate and **~45%** single-flagellum; substantial lateral (**~37%**) and subpolar (**~25%**) localization (gibson2023controlofthe pages 2-5).
- *C. jejuni* (amphitrichous) reported to swim at speeds “approaching **100 μm/second**” in the context of opposed polar flagella and viscous motility (cohen2020campylobacterjejunimotility pages 1-2).

### Warnings / claims not ready for TraitMech curation (or to mark as uncertain)
1) **“ΔflhG causes hyperflagellation” is not universal.** While broadly stated for multiple polar proteobacteria (arroyoperez2024aconservedcellpole pages 2-3), *H. pylori* ΔflhG shows a broadened distribution with more hypoflagellated cells (gibson2023controlofthe pages 2-5). Curate as taxon-specific or “often/typically” with uncertainty.
2) **HubP is not the only polarity factor** for polar localization/flagellation even in *Shewanella* systems; alternative anchors (e.g., TonBm-PocA-PocB) are hypothesized (arroyoperez2024aconservedcellpole pages 14-15). Avoid overcommitting a single universal anchoring mechanism.
3) **Trait specificity**: Much of the best mechanistic evidence addresses **polar localization generally**, not amphitrichous specifically. Amphitrichous lineages may share modules, but explicit “causes amphitrichous” links should be curated cautiously unless amphitrichous-specific evidence is added.

---

## DOI-first bibliography (with URLs and dates where available)
1. Dornes A, Schmidt LM, Mais C-N, et al. **Polar confinement of a macromolecular machine by an SRP-type GTPase.** *Nature Communications*. **Jul 2024**. DOI: **10.1038/s41467-024-50274-4**. URL: https://doi.org/10.1038/s41467-024-50274-4 (dornes2024polarconfinementof pages 4-6, dornes2024polarconfinementof pages 2-4)
2. Arroyo-Pérez EE, Hook JC, Alvarado A, et al. **A conserved cell-pole determinant organizes proper polar flagellum formation.** *eLife*. **Dec 2024**. DOI: **10.7554/eLife.93004.3**. URL: https://doi.org/10.7554/eLife.93004.3 (arroyoperez2024aconservedcellpole pages 2-3, arroyoperez2024aconservedcellpole pages 14-15)
3. Gibson KH, Botting JM, Al-Otaibi N, et al. **Control of the flagellation pattern in Helicobacter pylori by FlhF and FlhG.** *Journal of Bacteriology*. **Sep 2023**. DOI: **10.1128/jb.00110-23**. URL: https://doi.org/10.1128/jb.00110-23 (gibson2023controlofthe pages 2-5)
4. Cohen EJ, Nakane D, Kabata Y, et al. **Campylobacter jejuni motility integrates specialized cell shape, flagellar filament, and motor, to coordinate action of its opposed flagella.** *PLOS Pathogens*. **Jul 2020**. DOI: **10.1371/journal.ppat.1008620**. URL: https://doi.org/10.1371/journal.ppat.1008620 (cohen2020campylobacterjejunimotility pages 1-2)
5. Chu J, Liu J, Hoover TR. **Phylogenetic Distribution, Ultrastructure, and Function of Bacterial Flagellar Sheaths.** *Biomolecules*. **Feb 2020**. DOI: **10.3390/biom10030363**. URL: https://doi.org/10.3390/biom10030363 (chu2020phylogeneticdistributionultrastructure pages 1-3)
6. Nedeljković M, Sastre D, Sundberg E. **Bacterial Flagellar Filament: A Supramolecular Multifunctional Nanostructure.** *International Journal of Molecular Sciences*. **Jul 2021**. DOI: **10.3390/ijms22147521**. URL: https://doi.org/10.3390/ijms22147521 (nedeljkovic2021bacterialflagellarfilament pages 1-2)
7. Grognot M, Taute KM. **More than propellers: how flagella shape bacterial motility behaviors.** *Current Opinion in Microbiology*. **Jun 2021**. DOI: **10.1016/j.mib.2021.02.005**. URL: https://doi.org/10.1016/j.mib.2021.02.005 (grognot2021morethanpropellers pages 4-5)

---

### Curation-ready next steps (YAML strategy)
- Use **amphitrichous** as the phenotype root; connect to a **polar-flagellation placement module** (FlhF/FlhG + landmark + licensing) with explicit taxon-scope warnings.
- Prefer edges with direct mechanistic binding/localization evidence in 2024 (FlhF–FliG; FlhF–HubP; ternary complex) for core graph.
- Add FipA as an upstream recruitment/licensing node; represent HubP/FimV as parallel/partially redundant pathway.
- Represent quantitative phenotype nodes (flagella number distribution; polar/subpolar/lateral) as assay outputs tied to ΔflhF/ΔflhG perturbations, flagged as organism-specific (currently best quantified in *H. pylori*).


References

1. (cohen2020campylobacterjejunimotility pages 1-2): Eli J. Cohen, Daisuke Nakane, Yoshiki Kabata, David R. Hendrixson, Takayuki Nishizaka, and Morgan Beeby. Campylobacter jejuni motility integrates specialized cell shape, flagellar filament, and motor, to coordinate action of its opposed flagella. PLOS Pathogens, 16:e1008620, Jul 2020. URL: https://doi.org/10.1371/journal.ppat.1008620, doi:10.1371/journal.ppat.1008620. This article has 99 citations and is from a highest quality peer-reviewed journal.

2. (chu2020phylogeneticdistributionultrastructure pages 1-3): Joshua Chu, Jun Liu, and Timothy R. Hoover. Phylogenetic distribution, ultrastructure, and function of bacterial flagellar sheaths. Biomolecules, 10:363, Feb 2020. URL: https://doi.org/10.3390/biom10030363, doi:10.3390/biom10030363. This article has 47 citations.

3. (nedeljkovic2021bacterialflagellarfilament pages 1-2): Marko Nedeljković, Diego Sastre, and Eric Sundberg. Bacterial flagellar filament: a supramolecular multifunctional nanostructure. International Journal of Molecular Sciences, 22:7521, Jul 2021. URL: https://doi.org/10.3390/ijms22147521, doi:10.3390/ijms22147521. This article has 116 citations.

4. (grognot2021morethanpropellers pages 4-5): Marianne Grognot and Katja M Taute. More than propellers: how flagella shape bacterial motility behaviors. Current Opinion in Microbiology, 61:73-81, Jun 2021. URL: https://doi.org/10.1016/j.mib.2021.02.005, doi:10.1016/j.mib.2021.02.005. This article has 102 citations and is from a peer-reviewed journal.

5. (grognot2021morethanpropellers pages 1-2): Marianne Grognot and Katja M Taute. More than propellers: how flagella shape bacterial motility behaviors. Current Opinion in Microbiology, 61:73-81, Jun 2021. URL: https://doi.org/10.1016/j.mib.2021.02.005, doi:10.1016/j.mib.2021.02.005. This article has 102 citations and is from a peer-reviewed journal.

6. (thomasUnknownyearthedesignof pages 57-59): D Thomas. The design of bacterial flagella: part 2—flagellar diversity across bacterial species. Unknown journal, Unknown year.

7. (arroyoperez2024aconservedcellpole pages 2-3): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.

8. (arroyoperez2024aconservedcellpole pages 14-15): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.

9. (dornes2024polarconfinementof pages 4-6): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

10. (dornes2024polarconfinementof pages 2-4): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

11. (dornes2024polarconfinementof media 7605f948): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

12. (dornes2024polarconfinementof media 650f532b): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

13. (dornes2024polarconfinementof media 9eac1fa6): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

14. (dornes2024polarconfinementof media fc913750): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

15. (gibson2023controlofthe pages 2-5): Katherine H. Gibson, Jack M. Botting, Natalie Al-Otaibi, Kriti Maitre, Julien Bergeron, Vincent J. Starai, and Timothy R. Hoover. Control of the flagellation pattern in <i>helicobacter pylori</i> by flhf and flhg. Journal of Bacteriology, Sep 2023. URL: https://doi.org/10.1128/jb.00110-23, doi:10.1128/jb.00110-23. This article has 10 citations and is from a peer-reviewed journal.

16. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

17. (gibson2023controlofthe pages 5-7): Katherine H. Gibson, Jack M. Botting, Natalie Al-Otaibi, Kriti Maitre, Julien Bergeron, Vincent J. Starai, and Timothy R. Hoover. Control of the flagellation pattern in <i>helicobacter pylori</i> by flhf and flhg. Journal of Bacteriology, Sep 2023. URL: https://doi.org/10.1128/jb.00110-23, doi:10.1128/jb.00110-23. This article has 10 citations and is from a peer-reviewed journal.

18. (arroyoperez2024aconservedcellpole pages 1-2): Erick Eligio Arroyo-Pérez, John C. Hook, Alejandra Alvarado, Stephan Wimmi, Timo Glatter, K. Thormann, and S. Ringgaard. A conserved cell-pole determinant organizes proper polar flagellum formation. Dec 2024. URL: https://doi.org/10.7554/elife.93004.3, doi:10.7554/elife.93004.3. This article has 6 citations and is from a domain leading peer-reviewed journal.