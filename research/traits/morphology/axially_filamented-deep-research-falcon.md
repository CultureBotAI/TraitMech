---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:17:36.092160'
end_time: '2026-06-18T06:29:27.543221'
duration_seconds: 711.45
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: axially filamented
  trait_identifier: METPO:1000705
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: axially_filamented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motility where the flagellum filament of an organism is located in
    the periplasm and does not extend past the cell envelope.
  parent_traits: METPO:1000702
  synonyms: axial filament
  evidence_summary: 'DOI:10.3390/biom10040550: flagella are hidden within the periplasmic
    space (Supports axial/periplasmic flagella as the defining motility structure.)'
  causal_graph_summary: 'axially_filamented_periplasmic_flagella: 6 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** axially filamented
- **METPO identifier:** METPO:1000705
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility where the flagellum filament of an organism is located in the periplasm and does not extend past the cell envelope.
- **Parent traits:** METPO:1000702
- **Synonyms:** axial filament
- **Existing evidence:** DOI:10.3390/biom10040550: flagella are hidden within the periplasmic space (Supports axial/periplasmic flagella as the defining motility structure.)
- **Existing causal graph summary:** axially_filamented_periplasmic_flagella: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **axially filamented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/axially_filamented.yaml`.

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
- **Trait label:** axially filamented
- **METPO identifier:** METPO:1000705
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility where the flagellum filament of an organism is located in the periplasm and does not extend past the cell envelope.
- **Parent traits:** METPO:1000702
- **Synonyms:** axial filament
- **Existing evidence:** DOI:10.3390/biom10040550: flagella are hidden within the periplasmic space (Supports axial/periplasmic flagella as the defining motility structure.)
- **Existing causal graph summary:** axially_filamented_periplasmic_flagella: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **axially filamented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/axially_filamented.yaml`.

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


# Research Report: Microbial Trait **axially filamented** (METPO:1000705)

## 1. Scope summary (trait concept, boundaries, and nearby traits)

### Definition and current understanding
The trait **axially filamented** (synonym: **axial filament**) refers to a **flagellum filament located in the periplasm that does not extend beyond the cell envelope**, i.e., an **internal/periplasmic/endoflagellum** rather than an external flagellum (METPO:1000705; consistent with spirochete biology). In spirochetes, periplasmic flagella are explicitly described as being **“confined to the periplasmic space between the peptidoglycan and outer membrane”** and are key to spirochete propulsion and morphology (botting2025flbbformsa pages 1-2). In Borrelia, endoflagella are described as **“anchored at each cell pole and extend through the periplasmic space”** (zambacampero2024broadlyconservedflgv pages 1-2).

### What the trait represents (phenotype vs capacity vs assay)
* **Primary phenotype/anatomical trait:** presence of **periplasmic flagellar filaments** (axial filaments) in the **periplasm** (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 1-3).
* **Physiological capacity (downstream):** **motility** and **cell-shape determination** (flat-wave/helical morphology) via rotation of those internal filaments (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 3-5).
* **Assay-observed proxy (common):** motility ring spread in semi-solid/soft agar (e.g., quantitative motility measurements used in Borrelia genetics) (zambacampero2024broadlyconservedflgv pages 7-10).

### Boundary cases and how to distinguish from nearby traits
1. **External flagellation (polar/lateral/peritrichous) vs axially filamented:** external flagella traverse the envelope and extend into the extracellular space; axial/periplasmic flagella remain internal and periplasm-confined (contrast discussed through spirochete-specific location and envelope confinement) (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 1-3).
2. **Aberrant “periplasmic filaments” due to assembly defects (not a true axially filamented trait):** a 2024 study shows that **loss of FlhE** in *Salmonella enterica* leads to **“ectopic assembly of flagellar filaments in the periplasm”**, disrupting peptidoglycan synthesis and causing abnormal morphology/lysis—this is a *pathological misassembly state*, not a canonical spirochete endoflagellum (halte2024flhefunctionsas pages 3-4). This provides a clear curation warning: **periplasmic filament presence can arise from failure of rod/PL-ring/OM penetration checkpoints** and should not automatically be curated as “axially filamented” without lineage/architecture support (halte2024flhefunctionsas pages 3-4, halte2024flhefunctionsas pages 8-9).
3. **Other internal motility systems (gliding, pili-based twitching):** spirochete crawling on surfaces is powered by PF rotation, but “axially filamented” should be grounded to the periplasmic flagellum structure itself; surface adhesion components (e.g., LPS) may be optional or context-specific (nakamura2020spirocheteflagellaand pages 9-11).

## 2. Recent developments and latest research (prioritizing 2023–2024)

### 2024: FlgV as a basal-body localized modulator of periplasmic flagellar filament assembly (Borrelia)
A 2024 *Nature Communications* study reannotated *B. burgdorferi* bb0268 as **flgV** and provided multiple lines of evidence that FlgV is a structural component impacting filament assembly and downstream phenotypes (cell division, motility, infection kinetics) (zambacampero2024broadlyconservedflgv pages 1-2). Cryo-electron tomography and fluorescence microscopy localized FlgV to the **flagellar basal body**, with density positioned between motor rings in reconstructions (zambacampero2024broadlyconservedflgv pages 7-10, zambacampero2024broadlyconservedflgv media d97bf532). Quantitatively, ΔflgV reduced average filament number (mean ~6.7 vs ~8.2 in WT in one experiment) and FlgV overproduction reduced filament number further (mean ~4.2) (zambacampero2024broadlyconservedflgv pages 7-10). These results support **gene dosage–sensitive control of filament assembly** as a candidate mechanistic subgraph for the trait.

### 2024: FlhE as a periplasmic checkpoint preventing periplasmic-flagellum mislocalization (non-spirochete diderms)
A 2024 *Nature Communications* paper proposes FlhE as a **periplasmic chaperone** that prevents formation of periplasmic flagella in certain Gammaproteobacteria by controlling rod assembly until PL-ring formation and OM penetration (halte2024flhefunctionsas pages 3-4). This is highly relevant for trait curation because it mechanistically explains a **false-positive “periplasmic filament” morphology** that arises from assembly failure rather than a dedicated axial-flagellum program (halte2024flhefunctionsas pages 3-4, halte2024flhefunctionsas pages 8-9).

### Note on 2025 structural advances
A 2025 *PLOS Pathogens* cryo-ET study provides high-resolution mechanistic evidence for a spirochete-specific motor scaffold: **FlbB forms a periplasmic ring around the rotor**, acts as a collar scaffold, and supports recruitment of stator complexes (botting2025flbbformsa pages 1-2). Although outside the user’s 2023–2024 priority window, it provides unusually direct structure–function evidence and a quantitative stator count (16) suitable for causal edges (botting2025flbbformsa pages 1-2).

## 3. Current applications and real-world implementations

### Clinical/biomedical relevance (pathogenesis and dissemination)
* **Motility and tissue invasion:** periplasmic flagella enable spirochetes to generate backward-moving waves and penetrate complex host tissues; this is explicitly linked to host infection in pathogenic spirochetes (botting2025flbbformsa pages 1-2).
* **In vivo dissemination timing:** the 2024 FlgV study identifies infection timepoints where motility/flagellar assembly is crucial, showing ΔflgV strains are attenuated in dissemination in mice (e.g., reduced tissue reisolation positivity at day 14 and day 21 vs WT) (zambacampero2024broadlyconservedflgv pages 10-13).

### Bioengineering/biophysics relevance (biomimetic design concept)
The spirochetal strategy—propulsion by rotation of periplasmic flagella in a narrow periplasmic space—has been framed as a design basis for efficient microswimmers/microrobots (review perspective) (nakamura2020spirocheteflagellaand pages 1-3).

## 4. Expert opinions and analysis (authoritative sources)

### Structural/mechanistic consensus
Across spirochete-focused work, periplasmic flagella are treated as a **distinct, lineage-associated architecture**: anchored at poles, confined to the periplasm, wrapped along the cell cylinder, generating shape and motility (botting2025flbbformsa pages 1-2, zambacampero2024broadlyconservedflgv pages 1-2, nakamura2020spirocheteflagellaand pages 1-3).

### Curation-relevant interpretation: “axially filamented” should be a structural trait, not merely a motility outcome
The strongest curation anchor is **subcellular localization and envelope confinement** (“between peptidoglycan and outer membrane”) rather than motility ring sizes or generic “flagellated” annotations (botting2025flbbformsa pages 1-2). The FlhE boundary-case study supports the expert caution that periplasmic filaments can arise in non-spirochetes as an **assembly failure phenotype** and should not be curated as the same trait without evidence of dedicated spirochete-like architecture (halte2024flhefunctionsas pages 3-4).

## 5. Relevant statistics and quantitative data (from recent studies)

* **Periplasmic flagellar filament assembly depends on FlgV levels (Borrelia, 2024):** 
  * WT/p mean filaments at one pole: **8.2 (n=18)**; ΔflgV/pind: **6.7 (n=21)**; complemented: **8.5 (n=18)** (zambacampero2024broadlyconservedflgv pages 7-10). 
  * Overexpression strain mean filaments: **4.2 (n=18)** (zambacampero2024broadlyconservedflgv pages 7-10). 
  * Visual support: cryo-ET figures show basal body localization of FlgV and filament/basal body tally panels (zambacampero2024broadlyconservedflgv media d97bf532, zambacampero2024broadlyconservedflgv media 2bc20e12).
* **Motor scaffold/stator statistic (Borrelia, 2025):** per motor, a collar network based on FlbB bridges rotor and **“16 torque-generating stator complexes”** (botting2025flbbformsa pages 1-2).
* **Torque statistic (Leptospira, review):** stall torque reported as **~4000 pN·nm** (nakamura2020spirocheteflagellaand pages 3-5). This is useful as a performance phenotype, but is review-derived and taxon-specific.

## Candidate causal-graph nodes (grouped by type)

| Node label | Node type | Suggested CURIE(s) | Short role in trait |
|---|---|---|---|
| **Anatomical location** | **Anatomical location** |  |  |
| periplasmic space | anatomical location | GO:0042597 | Compartment in which axial/periplasmic flagella reside; positioned between cell envelope layers in spirochetes (nakamura2020spirocheteflagellaand pages 1-3, botting2025flbbformsa pages 1-2) |
| outer membrane | anatomical location | GO:0019867 | Outer boundary of diderm spirochete envelope; periplasmic flagella are confined internal to it (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 1-3) |
| peptidoglycan layer | anatomical location | GO:0009274 | Inner boundary adjacent to periplasmic flagella; defines the compartment between PG and OM where PFs are located (botting2025flbbformsa pages 1-2, halte2024flhefunctionsas pages 8-9) |
| cytoplasmic membrane | anatomical location | GO:0005886 | Houses motor, stator, and export apparatus; source of ion motive force for rotation (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 1-3) |
| cell pole | anatomical location | GO:0048475 | Attachment site where endoflagella are anchored in spirochetes (zambacampero2024broadlyconservedflgv pages 1-2, botting2025flbbformsa pages 1-2) |
| outer curve of periplasmic flagellar sheath | anatomical location |  | Specific asymmetric sheath locale for FcpB in Leptospira PFs (nakamura2020spirocheteflagellaand pages 3-5) |
| flagellar basal body | complex | GO:0030694 | Membrane-embedded rotary base of the PF; localization site for FlgV in Borrelia (zambacampero2024broadlyconservedflgv pages 7-10) |
| **Trait / phenotype** | **Trait / phenotype** |  |  |
| periplasmic flagellum / endoflagellum / axial filament | complex | METPO:1000705 | Defining structural basis of the trait: flagellar filament located within the periplasm rather than external to the cell (nakamura2020spirocheteflagellaand pages 1-3, zambacampero2024broadlyconservedflgv pages 1-2, botting2025flbbformsa pages 1-2) |
| axially filamented motility | process |  | Motility and morphology phenotype produced by rotation of internal PFs around the cell cylinder (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 3-5) |
| crawling motility (Leptospira) | process | GO:0071973 | Surface-associated motility powered by PF rotation and aided by surface adhesins such as LPS (nakamura2020spirocheteflagellaand pages 9-11) |
| soft agar motility ring | assay |  | Common assay readout for flagellar motility defects or enhancement (zambacampero2024broadlyconservedflgv pages 7-10) |
| **Core flagellar structures / complexes** | **Core flagellar structures / complexes** |  |  |
| flagellar filament | complex | GO:0009288 | Helical propulsive/cytoskeleton-like element of PFs; composed of FlaB core and additional sheath/minor proteins depending on taxon (nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 1-3) |
| MS ring | complex | GO:0009427 | Rotor component of the basal body; built from FliF and interfaces with FlbB/collar in spirochetes (botting2025flbbformsa pages 10-11, botting2025flbbformsa pages 1-2) |
| FliF (MS-ring protein) | protein |  | Structural protein forming the MS ring; proposed electrostatic interface with FlbB ring (botting2025flbbformsa pages 10-11) |
| C ring | complex |  | Rotor/switch complex below the MS ring; part of conserved flagellar motor architecture (botting2025flbbformsa pages 1-2, islam2023ancestralsequencereconstructions pages 21-26) |
| FliG | protein |  | Rotor/switch protein in the C ring; core motor component in bacterial flagella (islam2023ancestralsequencereconstructions pages 21-26) |
| FliM | protein |  | C-ring switch component contributing to motor switching/control (islam2023ancestralsequencereconstructions pages 21-26) |
| FliN | protein |  | C-ring component of conserved motor/switch machinery (islam2023ancestralsequencereconstructions pages 21-26) |
| rod | complex |  | Driveshaft-like structure spanning the envelope from motor toward hook/filament (botting2025flbbformsa pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FliE | protein |  | Proximal rod component assembled early in rod biogenesis (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FlgB | protein |  | Proximal rod protein (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FlgC | protein |  | Proximal rod protein (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FlgF | protein |  | Proximal rod protein (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FlgG | protein |  | Distal rod protein; levels decrease when FlgV is overexpressed in Borrelia (zambacampero2024broadlyconservedflgv pages 7-10) |
| hook | complex | GO:0009289 | Universal-joint-like connector between rod and filament in PF systems (nakamura2020spirocheteflagellaand pages 1-3, nakamura2020spirocheteflagellaand pages 3-5) |
| FlgE | protein |  | Hook protein; in spirochetes forms the PF hook and may be structurally stabilized in some taxa (nakamura2020spirocheteflagellaand pages 3-5) |
| P-ring | complex |  | Envelope bushing at the peptidoglycan layer; part of core motor architecture and relevant to compartment penetration (botting2025flbbformsa pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FlgI | protein |  | P-ring protein; absence blocks proper transition through envelope in model systems (halte2024flhefunctionsas pages 8-9) |
| L-ring | complex |  | Outer-membrane-associated bushing ring; part of envelope-spanning flagellar machine (botting2025flbbformsa pages 1-2, halte2024flhefunctionsas pages 8-9) |
| FlgH | protein |  | L-ring protein; completion required for proper rod progression through outer envelope in model systems (halte2024flhefunctionsas pages 8-9) |
| stator complex | complex |  | Ion-powered torque generator surrounding the rotor; recruited/stabilized by spirochete collar structures (botting2025flbbformsa pages 1-2, botting2025flbbformsa pages 10-11, nakamura2020spirocheteflagellaand pages 3-5) |
| MotA | protein |  | Stator transmembrane ion-channel component contributing torque generation (botting2025flbbformsa pages 1-2, islam2023ancestralsequencereconstructions pages 21-26) |
| MotB | protein |  | Stator component anchored to peptidoglycan; part of MotA/MotB torque-generating unit (botting2025flbbformsa pages 1-2, nakamura2024structureanddynamics pages 18-19) |
| flagellar type III secretion system / export apparatus | complex | GO:0030257 | Secretes rod, hook, and filament components during assembly (botting2025flbbformsa pages 1-2, halte2024flhefunctionsas pages 1-2) |
| FlhA | protein |  | Core export apparatus component in flagellar T3SS (halte2024flhefunctionsas pages 1-2) |
| FlhB | protein |  | Export gate component; part of conserved assembly machine (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 3-4) |
| FliP | protein |  | Export gate subunit (halte2024flhefunctionsas pages 1-2) |
| FliQ | protein |  | Export gate subunit (halte2024flhefunctionsas pages 1-2) |
| FliR | protein |  | Export gate subunit (halte2024flhefunctionsas pages 1-2) |
| FliI | protein |  | Cytoplasmic ATPase of flagellar export machinery (nguyen2025thecharacterizationof pages 21-24, nakamura2024structureanddynamics pages 18-19) |
| FliH | protein |  | ATPase-associated export factor in flagellar assembly (nguyen2025thecharacterizationof pages 21-24, nakamura2024structureanddynamics pages 18-19) |
| FliJ | protein |  | Export apparatus cofactor/chaperone-like component (nguyen2025thecharacterizationof pages 21-24) |
| **Periplasmic filament components** | **Periplasmic filament components** |  |  |
| FlaB | protein |  | Major PF/core flagellin in spirochetes; forms entire PF filament in Borrelia and core filament in Leptospira/Brachyspira (nakamura2020spirocheteflagellaand pages 3-5, zambacampero2024broadlyconservedflgv pages 7-10) |
| FlaA | protein |  | Minor PF/sheath-associated flagellin; localized near filament base in Borrelia and contributes to sheath architecture in other spirochetes (nakamura2020spirocheteflagellaand pages 3-5, zambacampero2024broadlyconservedflgv pages 7-10) |
| FcpA | protein |  | Leptospira sheath protein required for sheath formation and core–sheath interaction/coiling (nakamura2020spirocheteflagellaand pages 3-5) |
| FcpB | protein |  | Leptospira sheath protein localized to outer curve of PF; contributes to coiling/asymmetry (nakamura2020spirocheteflagellaand pages 3-5) |
| sheath (periplasmic flagellar sheath) | complex |  | Asymmetric covering around PF core in some spirochetes, especially Leptospira/Brachyspira (nakamura2020spirocheteflagellaand pages 3-5) |
| core filament | complex |  | Internal PF filament portion built largely from FlaB proteins in some spirochetes (nakamura2020spirocheteflagellaand pages 3-5) |
| **Spirochete-specific collar/scaffold components** | **Spirochete-specific collar/scaffold components** |  |  |
| collar / P-collar | complex |  | Spirochete-specific motor scaffold linked to stable stator assembly, high torque, and PF-based motility (nakamura2020spirocheteflagellaand pages 3-5, botting2025flbbformsa pages 1-2) |
| FlbB | protein |  | Collar protein forming a novel periplasmic ring around the rotor; scaffold/bearing for collar assembly and stator recruitment (botting2025flbbformsa pages 1-2, botting2025flbbformsa pages 10-11) |
| FlcA | protein |  | Collar-associated protein implicated in stator assembly/stabilization in Borrelia (botting2025flbbformsa pages 10-11, botting2025flbbformsa pages 1-2) |
| FlcB | protein |  | Collar-associated structural protein in Borrelia motor scaffold (botting2025flbbformsa pages 1-2) |
| FlcC | protein |  | Collar-associated structural protein in Borrelia motor scaffold (botting2025flbbformsa pages 1-2) |
| FlcD (Bb0236) | protein |  | Collar-associated component contributing with FlbB to collar foundation assembly (botting2025flbbformsa pages 10-11, botting2025flbbformsa pages 1-2) |
| **Assembly/regulatory factors** | **Assembly/regulatory factors** |  |  |
| FlgV (bb0268) | protein |  | Broadly conserved structural flagellar factor in Borrelia; localizes to basal body and modulates filament number/length and motility (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 7-10) |
| flhF | gene/protein |  | Potential regulator of flagellar biosynthesis/number and configuration; adjacent to flgV in Borrelia locus (zambacampero2024broadlyconservedflgv pages 1-2, botting2025flbbformsa pages 16-17) |
| flhG | gene/protein |  | Potential regulator of flagellar biosynthesis/number and configuration; adjacent to flgV/flhF (zambacampero2024broadlyconservedflgv pages 1-2) |
| FlhE | protein |  | Periplasmic chaperone in some Gammaproteobacteria that prevents aberrant periplasmic flagella by controlling rod assembly until OM penetration (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 3-4, halte2024flhefunctionsas pages 8-9) |
| FlgJ | protein |  | Rod-cap muramidase enabling penetration of the peptidoglycan layer during rod assembly (halte2024flhefunctionsas pages 8-9, halte2024flhefunctionsas pages 1-2) |
| **Processes / functions** | **Processes / functions** |  |  |
| flagellar assembly | process | GO:0044780 | Biogenesis program producing basal body, rod, hook, and PF filament; directly modulated by FlgV, FlbB/collar, and FlhE in different taxa (zambacampero2024broadlyconservedflgv pages 1-2, botting2025flbbformsa pages 10-11, halte2024flhefunctionsas pages 8-9) |
| stator recruitment/stable stator assembly | process |  | Key spirochete motor-assembly process promoted by collar and FlbB; linked to high torque (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 3-5) |
| filament coiling / supercoiling | process |  | Morphogenetic process influenced by sheath asymmetry and FcpA/FcpB in Leptospira PFs (nakamura2020spirocheteflagellaand pages 3-5) |
| torque generation | process | GO:0006935 | Mechanical output of stator–rotor interaction that rotates PFs (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 3-5) |
| proton motive force-dependent flagellar rotation | process | GO:0097588 | Energetic driver of PF rotation and Leptospira crawling; collapsible by CCCP (nakamura2020spirocheteflagellaand pages 9-11) |
| peptidoglycan digestion during rod penetration | process |  | Required rod-assembly step mediated by FlgJ for envelope traversal (halte2024flhefunctionsas pages 8-9) |
| cell lysis secondary to aberrant periplasmic filament assembly | process | GO:0008210 | Pathological outcome in ΔflhE Gram-negative cells when periplasmic filaments disrupt PG synthesis/cell morphology (halte2024flhefunctionsas pages 3-4, halte2024flhefunctionsas pages 8-9) |
| **Chemicals / energetic factors** | **Chemicals / energetic factors** |  |  |
| proton motive force | chemical/process | GO:0015986 | Energy source that powers stator complexes and PF rotation (botting2025flbbformsa pages 1-2, nakamura2020spirocheteflagellaand pages 9-11) |
| CCCP | chemical | CHEBI:34910 | Protonophore used experimentally; inhibits Leptospira crawling by collapsing PMF (nakamura2020spirocheteflagellaand pages 9-11) |
| lipopolysaccharide (LPS) | chemical | CHEBI:16412 | Surface adhesin candidate contributing to Leptospira crawling on surfaces (nakamura2020spirocheteflagellaand pages 9-11) |
| **Environmental / experimental factors** | **Environmental / experimental factors** |  |  |
| host tissue / dermal collagen | environmental factor | ENVO:01001831 | Complex environment penetrated by spirochetes using PF-based motility (botting2025flbbformsa pages 1-2) |
| surface-associated growth / glass surface | environmental factor | ENVO:00000070 | Experimental surface used to assess Leptospira crawling and adhesin-dependent motility (nakamura2020spirocheteflagellaand pages 9-11) |
| soft agar medium | assay |  | Standard motility assay environment for ring-spread quantification (zambacampero2024broadlyconservedflgv pages 7-10) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of the axially filamented trait, covering structural components, localizations, assembly factors, processes, and experimental modifiers. It is designed to support direct curation of grounded entities and their likely mechanistic roles.*

## Candidate causal edges (triples) with evidence, snippets, and curation notes

| Subject | Predicate | Object | Evidence snippet (verbatim quote) | Reference (DOI + URL + publication date) | Notes/curation guidance |
|---|---|---|---|---|---|
| periplasmic flagella | located_in | periplasmic space between peptidoglycan and outer membrane | “periplasmic flagella, which are confined to the periplasmic space between the peptidoglycan and outer membrane.” (botting2025flbbformsa pages 1-2) | Botting et al. 2025. DOI: 10.1371/journal.ppat.1012812. https://doi.org/10.1371/journal.ppat.1012812. Published 2025-01-08 | Strong definition-level edge for the trait scope. Taxon focus is spirochetes/Borrelia, but likely broadly applicable to axial/periplasmic flagella. |
| endoflagella / periplasmic flagella | anchored_at | cell pole | “unique endoflagella, which are anchored at each cell pole and extend through the periplasmic space” (zambacampero2024broadlyconservedflgv pages 1-2) | Zamba-Campero et al. 2024. DOI: 10.1038/s41467-024-54806-w. https://doi.org/10.1038/s41467-024-54806-w. Published 2024-11 | Strong for Borrelia; suitable edge if scoped as spirochetal architecture. |
| endoflagella / periplasmic flagella | extends_through | periplasmic space | “unique endoflagella, which are anchored at each cell pole and extend through the periplasmic space” (zambacampero2024broadlyconservedflgv pages 1-2) | Zamba-Campero et al. 2024. DOI: 10.1038/s41467-024-54806-w. https://doi.org/10.1038/s41467-024-54806-w. Published 2024-11 | Strong direct statement; complements localization edge above. |
| FlaB | part_of | periplasmic flagellar filament | “In B. burgdorferi, FlaB forms the entire PF filament” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Strong but taxon-specific for Borrelia. For broader curation use weaker statement that spirochete PFs “generally contain FlaA and FlaB.” Review-derived. |
| FlaA | part_of | periplasmic flagellar filament sheath / minor component | “All spirochete PFs known also consist of more than two proteins, and they generally contain FlaA and FlaB.” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Broad review support for FlaA as PF component. Role varies by taxon; in Borrelia “FlaA is believed to be localized around the base of the filament,” while in Brachyspira it forms sheath, so curate as uncertain/taxon-dependent. |
| FcpA | required_for | flagellar sheath formation | “whereas fcpA knockout mutants lack a sheath” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Strong but Leptospira-specific. Good causal edge for a taxon-qualified subgraph. |
| FcpB | localized_to | outer curve of periplasmic flagellar sheath | “FcpB is a sheath protein that is localized along the outer curve of the PF” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Strong structural localization; Leptospira-specific. |
| FcpB | contributes_to | periplasmic flagellar coiling | “suggesting a contribution to PF coiling” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Inferred/interpretive language from review; mark uncertain. |
| FlbB | forms_ring_around | rotor | “FlbB forms a novel periplasmic ring around the rotor” (botting2025flbbformsa pages 1-2) | Botting et al. 2025. DOI: 10.1371/journal.ppat.1012812. https://doi.org/10.1371/journal.ppat.1012812. Published 2025-01-08 | Strong direct structural edge for Borrelia and likely other spirochetes with homologs. |
| FlbB | promotes | collar assembly | “acts as a scaffold supporting collar assembly” (botting2025flbbformsa pages 1-2) | Botting et al. 2025. DOI: 10.1371/journal.ppat.1012812. https://doi.org/10.1371/journal.ppat.1012812. Published 2025-01-08 | Strong mechanistic edge; Borrelia-specific experiment. |
| FlbB ring / collar | recruits | stator complexes | “acts as a scaffold supporting collar assembly and subsequent recruitment of stator complexes” (botting2025flbbformsa pages 1-2) | Botting et al. 2025. DOI: 10.1371/journal.ppat.1012812. https://doi.org/10.1371/journal.ppat.1012812. Published 2025-01-08 | Strong direct causal edge. Consider node choice carefully: FlbB ring, collar, or collar scaffold. |
| collar protein network based on FlbB ring | bridges | 16 torque-generating stator complexes | “The complex protein network based on the FlbB ring effectively bridges the rotor and 16 torque-generating stator complexes in each flagellar motor” (botting2025flbbformsa pages 1-2) | Botting et al. 2025. DOI: 10.1371/journal.ppat.1012812. https://doi.org/10.1371/journal.ppat.1012812. Published 2025-01-08 | Good quantitative edge/statistic. Borrelia-specific count; do not overgeneralize stator number across spirochetes. |
| FlgV | localized_to | flagellar basal body | “FlgV is localized to the flagellar basal body.” (zambacampero2024broadlyconservedflgv pages 7-10) | Zamba-Campero et al. 2024. DOI: 10.1038/s41467-024-54806-w. https://doi.org/10.1038/s41467-024-54806-w. Published 2024-11 | Strong direct localization edge in Borrelia. |
| FlgV | modulates | flagellar filament assembly | “bb0268 (flgV) is a structural flagellar component that ‘modulates flagellar assembly.’” (zambacampero2024broadlyconservedflgv pages 1-2) | Zamba-Campero et al. 2024. DOI: 10.1038/s41467-024-54806-w. https://doi.org/10.1038/s41467-024-54806-w. Published 2024-11 | Strong summary statement from article excerpt. |
| loss of flgV | decreases | flagellar filament number | “there was a significant reduction in the average number of flagellar filaments for ΔflgV/pind, mean value of 6.7 (n = 21), compared to WT/p, 8.2 (n = 18)” (zambacampero2024broadlyconservedflgv pages 7-10) | Zamba-Campero et al. 2024. DOI: 10.1038/s41467-024-54806-w. https://doi.org/10.1038/s41467-024-54806-w. Published 2024-11 | Strong quantitative phenotype edge; model as mutant phenotype rather than wild-type causal edge if needed. |
| FlgV overexpression | decreases | flagellar filament number | “there was a significant reduction in the average number of flagellar filaments in spirochetes overproducing FlgV protein, mean value of 4.2 (n = 18)” (zambacampero2024broadlyconservedflgv pages 7-10) | Zamba-Campero et al. 2024. DOI: 10.1038/s41467-024-54806-w. https://doi.org/10.1038/s41467-024-54806-w. Published 2024-11 | Useful regulatory edge showing dosage sensitivity; taxon-specific. |
| absence of FlhE | causes | ectopic periplasmic filament assembly | “the ectopic assembly of flagellar filaments in the periplasm in the absence of FlhE” (halte2024flhefunctionsas pages 3-4) | Halte et al. 2024. DOI: 10.1038/s41467-024-50278-0. https://doi.org/10.1038/s41467-024-50278-0. Published 2024-07 | Strong but not a positive trait mechanism; rather a suppressive/preventive edge in externally flagellated Gammaproteobacteria. Important boundary-case evidence. |
| FlhE | prevents | formation of periplasmic flagella | “FlhE functions as a periplasmic chaperone to control the assembly of the flagellar rod until formation of the PL-rings and penetration of the OM, thereby preventing formation of periplasmic flagella” (halte2024flhefunctionsas pages 3-4) | Halte et al. 2024. DOI: 10.1038/s41467-024-50278-0. https://doi.org/10.1038/s41467-024-50278-0. Published 2024-07 | Negative regulatory edge; useful to distinguish axial/periplasmic flagella as a specialized morphology rather than generic assembly failure. |
| absence of FlhE | disrupts | peptidoglycan synthesis | “periplasmic flagella, which would otherwise disrupt PG synthesis resulting in abnormal cell morphology and ultimately cell lysis.” (halte2024flhefunctionsas pages 3-4) | Halte et al. 2024. DOI: 10.1038/s41467-024-50278-0. https://doi.org/10.1038/s41467-024-50278-0. Published 2024-07 | Strong in Salmonella mutant context only; not a trait-defining edge for spirochetes. Mark as boundary-case/non-curation candidate for core graph. |
| stable stator assembly via P-collar/collar | enables | higher torque generation | “Such stable assembly of the spirochete stators is thought to involve a spirochete-specific motor component called ‘P-collar’... This knowledge predicts that the spirochetal motor can produce higher torque” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Review-derived mechanistic inference; curate as uncertain unless matched with primary structural papers. |
| Leptospira flagellar motor | has_stall_torque | ~4000 pN·nm | “Leptospira spp. produce a stall torque of ~4000 pN nm” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Useful quantitative statistic; phenotype/performance edge rather than core morphology edge. |
| proton motive force | drives | periplasmic-flagella-dependent crawling | “A recent study by Tahara et al. showed that crawling is completely inhibited by CCCP, indicating that PMF-dependent PF rotation drives crawling” (nakamura2020spirocheteflagellaand pages 9-11) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Good energetic/mechanistic edge for Leptospira crawling; review-derived and phenotype-specific. |
| CCCP | inhibits | Leptospira crawling | “crawling is completely inhibited by CCCP” (nakamura2020spirocheteflagellaand pages 9-11) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Strong inhibitor edge, but assay-specific and focused on crawling rather than filament biogenesis. |
| LPS | contributes_to | adhesin function in crawling | “These results suggest that LPS is responsible for crawling, serving as one of the adhesins anchoring the cell to the surface” (nakamura2020spirocheteflagellaand pages 9-11) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Useful environmental/surface-interaction edge; specific to Leptospira surface crawling, not universal to axial filament trait. |
| periplasmic flagella | contributes_to | wavy / flat-wave cell morphology | “Another important role of the PF is to establish a wavy morphology, similar to a cytoskeleton” (nakamura2020spirocheteflagellaand pages 3-5) | Nakamura 2020. DOI: 10.3390/biom10040550. https://doi.org/10.3390/biom10040550. Published 2020-04 | Useful phenotype edge connecting structure to morphology. Review-derived but central to trait consequences. |


*Table: This table compiles evidence-backed subject–predicate–object edges for curating a TraitMech graph of the axially filamented trait. It emphasizes direct localization and assembly evidence, while marking review-derived, taxon-specific, and assay-specific claims that need cautious curation.*

## Ontology grounding suggestions (non-exhaustive)

* **Trait:** METPO:1000705 (axially filamented).
* **Compartment:** periplasmic space (GO:0042597), outer membrane (GO:0019867), cytoplasmic membrane (GO:0005886), peptidoglycan layer (GO:0009274) (artifact-01).
* **Process:** flagellar assembly (GO:0044780); PMF-related energy coupling (e.g., GO:0015986) (artifact-01).
* **Chemicals:** CCCP (CHEBI:34910); LPS (CHEBI:16412) (artifact-01).

## Warnings / “do not curate yet” items (or curate only with qualifiers)

1. **Avoid curating “periplasmic filament formation” as axially filamented without lineage/architecture evidence.** In *Salmonella*, periplasmic filament assembly is a deleterious misassembly state triggered by ΔflhE and associated with cell-wall defects/lysis (halte2024flhefunctionsas pages 3-4, halte2024flhefunctionsas pages 8-9). This is mechanistically informative but is not equivalent to spirochete axial filaments.
2. **Taxon-specific sheath/coiling proteins (FcpA/FcpB) should be curated with an explicit spirochete/Leptospira qualifier.** Their roles are strong for Leptospira PF morphology, but not general across all spirochetes (nakamura2020spirocheteflagellaand pages 3-5).
3. **Review-derived mechanistic statements (e.g., P-collar → stable stator assembly → higher torque) should be tagged as ‘uncertain’ unless confirmed by primary structural genetics in the target taxon.** The review uses inferential language (“thought to involve”, “predicts”) (nakamura2020spirocheteflagellaand pages 3-5).

---

# DOI-first bibliography (with URLs and publication dates)

1. **Zamba-Campero M, et al.** *Broadly conserved FlgV controls flagellar assembly and Borrelia burgdorferi dissemination in mice.* **Nature Communications** (Published **2024-11**). DOI: **10.1038/s41467-024-54806-w**. URL: https://doi.org/10.1038/s41467-024-54806-w (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 7-10, zambacampero2024broadlyconservedflgv pages 10-13, zambacampero2024broadlyconservedflgv media d97bf532, zambacampero2024broadlyconservedflgv media 2bc20e12)
2. **Halte M, et al.** *FlhE functions as a chaperone to prevent formation of periplasmic flagella in Gram-negative bacteria.* **Nature Communications** (Published **2024-07**). DOI: **10.1038/s41467-024-50278-0**. URL: https://doi.org/10.1038/s41467-024-50278-0 (halte2024flhefunctionsas pages 1-2, halte2024flhefunctionsas pages 3-4, halte2024flhefunctionsas pages 8-9)
3. **Nakamura S.** *Spirochete Flagella and Motility.* **Biomolecules** (Published **2020-04**). DOI: **10.3390/biom10040550**. URL: https://doi.org/10.3390/biom10040550 (nakamura2020spirocheteflagellaand pages 1-3, nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 9-11)
4. **Botting JM, et al.** *FlbB forms a distinctive ring essential for periplasmic flagellar assembly and motility in Borrelia burgdorferi.* **PLOS Pathogens** (Published **2025-01-08**). DOI: **10.1371/journal.ppat.1012812**. URL: https://doi.org/10.1371/journal.ppat.1012812 (botting2025flbbformsa pages 1-2, botting2025flbbformsa pages 10-11)



References

1. (botting2025flbbformsa pages 1-2): Jack M. Botting, Md Khalesur Rahman, Hui Xu, Jian Yue, Wangbiao Guo, Joshua T. Del Mundo, Michal Hammel, Md A. Motaleb, and Jun Liu. Flbb forms a distinctive ring essential for periplasmic flagellar assembly and motility in borrelia burgdorferi. Jan 2025. URL: https://doi.org/10.1371/journal.ppat.1012812, doi:10.1371/journal.ppat.1012812. This article has 7 citations and is from a highest quality peer-reviewed journal.

2. (zambacampero2024broadlyconservedflgv pages 1-2): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

3. (nakamura2020spirocheteflagellaand pages 1-3): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 68 citations.

4. (nakamura2020spirocheteflagellaand pages 3-5): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 68 citations.

5. (zambacampero2024broadlyconservedflgv pages 7-10): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

6. (halte2024flhefunctionsas pages 3-4): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

7. (halte2024flhefunctionsas pages 8-9): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

8. (nakamura2020spirocheteflagellaand pages 9-11): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 68 citations.

9. (zambacampero2024broadlyconservedflgv media d97bf532): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

10. (zambacampero2024broadlyconservedflgv pages 10-13): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

11. (zambacampero2024broadlyconservedflgv media 2bc20e12): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

12. (botting2025flbbformsa pages 10-11): Jack M. Botting, Md Khalesur Rahman, Hui Xu, Jian Yue, Wangbiao Guo, Joshua T. Del Mundo, Michal Hammel, Md A. Motaleb, and Jun Liu. Flbb forms a distinctive ring essential for periplasmic flagellar assembly and motility in borrelia burgdorferi. Jan 2025. URL: https://doi.org/10.1371/journal.ppat.1012812, doi:10.1371/journal.ppat.1012812. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (islam2023ancestralsequencereconstructions pages 21-26): Ancestral Sequence Reconstructions of Stator Proteins of the Bacterial Flagellar Motor This article has 0 citations.

14. (halte2024flhefunctionsas pages 1-2): Manuel Halte, Ekaterina P. Andrianova, Christian Goosmann, Fabienne F. V. Chevance, Kelly T. Hughes, Igor B. Zhulin, and Marc Erhardt. Flhe functions as a chaperone to prevent formation of periplasmic flagella in gram-negative bacteria. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50278-0, doi:10.1038/s41467-024-50278-0. This article has 9 citations and is from a highest quality peer-reviewed journal.

15. (nakamura2024structureanddynamics pages 18-19): Shuichi Nakamura and Tohru Minamino. Structure and dynamics of the bacterial flagellar motor complex. Biomolecules, 14:1488, Nov 2024. URL: https://doi.org/10.3390/biom14121488, doi:10.3390/biom14121488. This article has 26 citations.

16. (nguyen2025thecharacterizationof pages 21-24): D Nguyen. The characterization of the helicobacter pylori flagellar sheath. Unknown journal, 2025.

17. (botting2025flbbformsa pages 16-17): Jack M. Botting, Md Khalesur Rahman, Hui Xu, Jian Yue, Wangbiao Guo, Joshua T. Del Mundo, Michal Hammel, Md A. Motaleb, and Jun Liu. Flbb forms a distinctive ring essential for periplasmic flagellar assembly and motility in borrelia burgdorferi. Jan 2025. URL: https://doi.org/10.1371/journal.ppat.1012812, doi:10.1371/journal.ppat.1012812. This article has 7 citations and is from a highest quality peer-reviewed journal.