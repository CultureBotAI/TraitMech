---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:47:14.619755'
end_time: '2026-06-18T08:13:31.669827'
duration_seconds: 1577.05
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: fusiform shaped
  trait_identifier: METPO:1000690
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: fusiform_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape that is wide in the middle and tapers at both ends.
  parent_traits: METPO:1000666
  synonyms: fusiform
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports tapered cell ends as a genetically determined
    geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731:
    Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology
    in the Fusobacterium genus.)'
  causal_graph_summary: 'fusiform_shaped_tapered_polar_growth: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** fusiform shaped
- **METPO identifier:** METPO:1000690
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is wide in the middle and tapers at both ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** fusiform
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports tapered cell ends as a genetically determined geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731: Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology in the Fusobacterium genus.)
- **Existing causal graph summary:** fusiform_shaped_tapered_polar_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **fusiform shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/fusiform_shaped.yaml`.

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
- **Trait label:** fusiform shaped
- **METPO identifier:** METPO:1000690
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is wide in the middle and tapers at both ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** fusiform
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports tapered cell ends as a genetically determined geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731: Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology in the Fusobacterium genus.)
- **Existing causal graph summary:** fusiform_shaped_tapered_polar_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **fusiform shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/fusiform_shaped.yaml`.

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


## Research Report: Microbial Trait Causal Graph — **fusiform shaped** (METPO:1000690)

### 0. Executive scope summary
**Fusiform shaped** (METPO:1000690) denotes a *spindle-shaped* cell morphology: wide in the middle and tapering at both ends. In practice, it is most often curated from microscopy (brightfield/Gram stain, SEM/TEM, confocal) and may be used (i) as a stable taxon-associated morphology (e.g., *Fusobacterium nucleatum*) and/or (ii) as a state reached under specific growth conditions, genetic perturbations, or cell-envelope/cytoskeletal remodeling (e.g., tapered “tip” structures in wall-less *Spiroplasma*). (zhang2024outermembranevesicles pages 1-2, krieger2024reexaminingtherole pages 1-2, lartigue2022cytoskeletalcomponentscan media 31c75a03)

**Boundary cases (distinguish from nearby traits):**
- **Rod-shaped (cylindrical)**: roughly constant diameter along length; may have rounded ends but not pronounced tapering. Many MreB-guided elongation programs primarily maintain rod cylinders rather than spindle tapering. (egan2020regulationofpeptidoglycan pages 8-9)
- **Vibrio/crescent**: curved rods; curvature is distinct from fusiform tapering.
- **Helical**: non-zero torsion/helix; may coexist with tapered ends (e.g., *Spiroplasma* has a tapered tip plus helicity/kinking). (lartigue2022cytoskeletalcomponentscan pages 7-8, lartigue2022cytoskeletalcomponentscan media 31c75a03)
- **Filamentous/elongated**: increased length without necessarily changing end geometry (tapering is not guaranteed). (lim2025characterizationofclinical pages 9-12)


### 1. Key concepts and current understanding (definitions + mechanistic framing)
#### 1.1 Cell shape as a wall- and cytoskeleton-governed emergent property
A general (cross-taxon) concept supported by authoritative cell-wall synthesis literature is that bacterial cell shape emerges from **spatiotemporal patterns of peptidoglycan (PG) insertion/remodeling** controlled by cytoskeletal systems (notably **MreB** for elongation and **FtsZ** for division) and their partner enzymes (SEDS proteins and PBPs). (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 8-9)

#### 1.2 Two mechanistic “routes” to fusiform/tapered ends (supported in retrieved sources)
**Route A: Peptidoglycan-pattern-driven shaping (walled bacteria)**
- The **elongasome** (MreB/RodZ/MreC/MreD with RodA + PBP2 and related PBPs) organizes lateral wall growth and thus overall geometry. (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 4-5)
- **Pole-biased insertion** can be produced experimentally by inhibiting MreB with **A22**, which “shifts PG insertion to cell poles.” This is relevant because tapered ends are, geometrically, a form of pole-specific diameter control. (pazos2019peptidoglycan. pages 20-23)

**Route B: Cytoskeletal/membrane-curvature shaping (wall-less bacteria)**
In wall-less *Spiroplasma*, tapered-end (“tip”) structures are linked to an internal cytoskeletal system:
- The **Fib/fibril protein** can induce membrane curvature and, together with **multiple MreB isoforms**, supports helical/tip-associated morphogenesis. (lartigue2022cytoskeletalcomponentscan pages 7-8)
- A figure in the same work explicitly shows a **tapered, duckbill-shaped end** (tip) (lartigue2022cytoskeletalcomponentscan media 31c75a03, lartigue2022cytoskeletalcomponentscan media 7a02a6e9), establishing a concrete *assay-observed tapered-end phenotype*.


### 2. Recent developments and latest research (prioritizing 2023–2024 sources)
#### 2.1 2024: *Fusobacterium nucleatum* fusiform morphology linked to biofilm bridging/coaggregation
A 2024 review synthesizing clinical/experimental evidence states that *F. nucleatum*’s **“long, fusiform morphology”** together with **promiscuous coaggregation** is **central to its role as a bridge species in oral biofilms**. This provides a high-level *morphology → ecological function* linkage that is directly relevant to trait curation when fusiform shape is used as a functional proxy in microbiome studies. (krieger2024reexaminingtherole pages 1-2)

A 2024 primary research article (Advanced Science) again defines *F. nucleatum* as having a **“fusiform rod shape”** and describes its role in facilitating biofilm-based colonization by other oral pathogens. (zhang2024outermembranevesicles pages 1-2)

#### 2.2 2023: Continued synthesis of *F. nucleatum* as a coaggregation “bridge organism”
A 2023 review reiterates that *F. nucleatum* is a major **coaggregation bridge organism**, connecting early and late colonizers in oral biofilms and thereby shaping community assembly and disease-associated dysbiosis. (fan2023fusobacteriumnucleatumand pages 1-2)

*Interpretation for TraitMech:* 2023–2024 literature strengthens the view that, at least for *F. nucleatum*, “fusiform-shaped” is not merely a descriptive trait but is co-mentioned with community-structuring functions (coaggregation/bridging). However, these sources do not isolate fusiform geometry as the causal driver vs correlated property; this should be treated as an association edge unless experimentally dissected. (krieger2024reexaminingtherole pages 1-2, fan2023fusobacteriumnucleatumand pages 1-2)


### 3. Current applications and real-world implementations
#### 3.1 Taxonomy/diagnostics and microscopy-based phenotyping
- Clinical isolate workflows explicitly *use fusiform morphology* as part of isolate characterization (Gram stain microscopy + image analysis). In a recent dataset, *F. nucleatum* clinical isolates were confirmed as **fusiform-shaped rods** and their cell lengths were quantified. (lim2025characterizationofclinical pages 9-12)

**Example implementation details (useful for curation provenance):**
- Imaging at **1,000× oil immersion**, region sampling, and downstream quantitative analysis (e.g., Imaris-based volumetrics) were used to measure cell length distributions among fusiform isolates. (lim2025characterizationofclinical pages 6-9, lim2025characterizationofclinical pages 9-12)

#### 3.2 Biofilm and polymicrobial interaction modeling
- Fusiform *F. nucleatum* is implemented as an experimental **bridge species** in oral biofilm models and mechanistic studies of coaggregation and host interaction. (krieger2024reexaminingtherole pages 1-2, groeger2022pathogenicmechanismsof pages 1-2)

#### 3.3 Metagenomic surveillance/clinical association studies
- A large-scale metagenomic analysis framework (mBio, 2025) uses genome populations and detection thresholds to quantify *F. nucleatum* in oral vs gut samples and disease contexts. This supports real-world monitoring where fusiform taxa are tracked as biomarkers/associates (even though morphology is not directly measured in metagenomes). (connolly2025thephysicalbiogeography pages 3-5)

#### 3.4 Mechanistic perturbations to probe end/taper geometry
- Chemical perturbation with **A22** (MreB inhibitor) and lipid-context effects at poles provide a practical experimental route to shift insertion patterns toward poles (a plausible contributor to tapered/fusiform geometries). (pazos2019peptidoglycan. pages 20-23)


### 4. Expert opinions / authoritative synthesis (mechanistic consensus)
- Authoritative synthesis emphasizes that **MreB-directed orientation of PG insertion** is central to maintaining smooth rod geometry and that division-site patterning is controlled by **FtsZ treadmilling**, with PBPs/SEDS proteins executing synthesis at moving sites. (egan2020regulationofpeptidoglycan pages 8-9, egan2020regulationofpeptidoglycan pages 7-8)
- A complementary synthesis (Firmicutes PG assembly) frames **SEDS (RodA/FtsW) + cognate bPBPs** as key polymerase systems that implement lateral vs septal synthesis programs; membrane biophysics (fluidity/flotillins) influences these dynamics. (ducret2021recentprogressin pages 6-6)

*TraitMech implication:* fusiform/tapered ends can be conceptualized as arising from **spatial gradients** in (i) insertion rate, (ii) crosslinking, and/or (iii) remodeling at poles vs midcell, implemented by the above machinery. The present evidence set provides strong support for the machinery but limited direct fusiform-specific molecular determinants (see Warnings). (egan2020regulationofpeptidoglycan pages 7-8, pazos2019peptidoglycan. pages 20-23)


### 5. Relevant statistics and quantitative data (recent studies)
#### 5.1 Cell-size distributions in fusiform *F. nucleatum* isolates (2025 preprint; quantitative)
- Reported cell lengths spanned **~2–13 µm** across fusiform-shaped *F. nucleatum* isolates; an example isolate measured **11–13 µm** while an ATCC strain was **2–4 µm**, and “most isolates measured over 7 µm.” (lim2025characterizationofclinical pages 9-12)
- Clinical isolate counts: **3 strains from 117 OSCC patients** and **5 strains from 160 non-cancer individuals** in the sampling described (pilot analyzed 8 clinical isolates). (lim2025characterizationofclinical pages 1-6)

#### 5.2 Disease-association prevalence and sampling scale for *F. nucleatum* (2025; large scale)
- *F. nucleatum* is described as observed in **~30% of colorectal cancer (CRC) patient guts/tumors** (framed as “approximately a third” in the excerpt). (connolly2025thephysicalbiogeography pages 1-3)
- Dataset size and composition: **9,560 samples from 11 studies**, including **5,840 stool** and **3,720 oral** samples; clinical subgroup counts included CRC **n=252**, Crohn’s **n=596**, ulcerative colitis **n=371**, T2D **n=162**, periodontitis **n=48**, healthy **n=7,337**. (connolly2025thephysicalbiogeography pages 3-5)
- Detection thresholds (sequence breadth) differed by body site: gut threshold **0.01 (~22 kb)** vs oral threshold **0.1429 (~14.3% of genome)**, corresponding to **~310–343 kb** for 95% confidence given 2.17–2.4 Mb genomes. (connolly2025thephysicalbiogeography pages 3-5)


## 6. Curation-focused outputs
### 6.1 Candidate nodes grouped by type (with grounding suggestions)
| Node label | Node type | Suggested CURIE(s) | Rationale/evidence (1 line) | Key references (DOI) | Context IDs |
|---|---|---|---|---|---|
| fusiform shaped | taxon/phenotype | METPO:1000690 | Target morphology: spindle-shaped cell, wide in middle and tapered at both ends; explicitly used for *Fusobacterium nucleatum* and related morphology descriptions. | 10.1080/19490976.2024.2415490; 10.1002/advs.202400882 | (krieger2024reexaminingtherole pages 1-2, zhang2024outermembranevesicles pages 1-2) |
| *Fusobacterium nucleatum* | taxon/phenotype | NCBITaxon:851 | Repeatedly described as a Gram-negative anaerobe with fusiform rod shape and strong biofilm/coaggregation relevance. | 10.1002/advs.202400882; 10.1080/19490976.2024.2415490 | (zhang2024outermembranevesicles pages 1-2, krieger2024reexaminingtherole pages 1-2) |
| long-cell-length state in *F. nucleatum* | taxon/phenotype | label only | Clinical isolates varied from ~2 to 13 µm, making cell length a measurable fusiform-associated state for assays and strain comparison. | 10.1101/2025.01.08.631950 | (lim2025characterizationofclinical pages 9-12) |
| oral biofilm bridge role | pathway/process | GO:0042710 (biofilm formation) candidate | *F. nucleatum* fusiform morphology plus promiscuous coaggregation are described as central to its bridge-species role in oral biofilms. | 10.1080/19490976.2024.2415490 | (krieger2024reexaminingtherole pages 1-2) |
| coaggregation | pathway/process | GO:0098743 candidate | Core ecological process for *F. nucleatum*; repeatedly linked to its bridging function and adhesin repertoire. | 10.1080/20002297.2022.2145729; 10.3389/froh.2022.831607 | (fan2023fusobacteriumnucleatumand pages 1-2, groeger2022pathogenicmechanismsof pages 1-2) |
| peptidoglycan synthesis | pathway/process | GO:0009252 | Central shape-generating process; elongasome/divisome patterning of PG insertion underlies bacterial cell shape maintenance. | 10.1038/s41579-020-0366-3; 10.1016/j.mib.2021.01.011 | (egan2020regulationofpeptidoglycan pages 7-8, ducret2021recentprogressin pages 6-6) |
| lateral peptidoglycan incorporation | pathway/process | GO:0009252 candidate | RodA and cognate bPBPs are specifically linked to lateral/sidewall PG incorporation that supports elongated morphologies. | 10.1016/j.mib.2021.01.011 | (ducret2021recentprogressin pages 6-6) |
| septal peptidoglycan incorporation | pathway/process | GO:0009252 candidate | FtsW and divisome PBPs are linked to septal PG synthesis, relevant to end-shaping and growth pattern partitioning. | 10.1016/j.mib.2021.01.011; 10.1038/s41579-020-0366-3 | (ducret2021recentprogressin pages 6-6, egan2020regulationofpeptidoglycan pages 8-9) |
| polar peptidoglycan insertion | pathway/process | GO:0009252 candidate | A22 perturbation shifts PG insertion to poles, making pole-biased growth a candidate contributor to tapered-end geometry. | 10.1007/978-3-030-18768-2_5 | (pazos2019peptidoglycan. pages 20-23) |
| membrane curvature generation | pathway/process | GO:0032989 candidate | Spiroplasma Fib/fibril can induce membrane curvature directly, supporting a tapered-end mechanism without PG. | 10.1038/s41467-022-34478-0 | (lartigue2022cytoskeletalcomponentscan pages 7-8) |
| MreB | gene/protein | UniProt/COG candidate; label only | Canonical bacterial actin homolog that orients PG synthesis and is repeatedly linked to rod-shape maintenance and curvature-sensitive localization. | 10.1038/s41579-020-0366-3; 10.1186/s12964-025-02373-y | (egan2020regulationofpeptidoglycan pages 8-9, wang2025mrebunravelingthe pages 11-12) |
| MreB5 | gene/protein | label only | Specific Spiroplasma paralog sufficient to confer helicity/kink propagation, relevant to tapered-tip cytoskeletal specialization. | 10.1038/s41467-022-34478-0 | (lartigue2022cytoskeletalcomponentscan pages 7-8) |
| RodZ | gene/protein | label only | MreB-associated shape protein that modulates MreB geometric localization and elongasome scaffolding. | 10.1186/s12964-025-02373-y; 10.1038/s41579-020-0366-3 | (wang2025mrebunravelingthe pages 21-21, egan2020regulationofpeptidoglycan pages 4-5) |
| MreC | gene/protein | label only | Elongasome component that interacts with MreB/PBP2 and activates RodA-PBP2 synthesis functions needed for shape control. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 4-5) |
| MreD | gene/protein | label only | Membrane elongasome component paired with MreC and implicated in spatial organization of synthesis machinery. | 10.1038/s41579-020-0366-3; 10.1186/s12964-025-02373-y | (egan2020regulationofpeptidoglycan pages 7-8, wang2025mrebunravelingthe pages 11-12) |
| RodA | gene/protein | EC/UniProt candidate; label only | SEDS glycosyltransferase in elongasome; mediates lateral PG incorporation with PBP2 and is central to shape-generating sidewall growth. | 10.1038/s41579-020-0366-3; 10.1016/j.mib.2021.01.011 | (egan2020regulationofpeptidoglycan pages 7-8, ducret2021recentprogressin pages 6-6) |
| FtsW | gene/protein | EC/UniProt candidate; label only | SEDS divisome polymerase for septal PG incorporation; useful for modeling end-localized growth/remodeling. | 10.1038/s41579-020-0366-3; 10.1016/j.mib.2021.01.011 | (egan2020regulationofpeptidoglycan pages 4-5, ducret2021recentprogressin pages 6-6) |
| PBP2 | gene/protein | EC/UniProt candidate; label only | Class B PBP in elongasome activated by MreC and functionally coupled to RodA for rod-like wall growth. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 4-5) |
| PBP3 | gene/protein | EC/UniProt candidate; label only | Divisome class B PBP working with FtsW during septal synthesis; relevant to end morphology and constriction patterning. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 8-9) |
| PBP1A | gene/protein | EC/UniProt candidate; label only | Class A PBP that cooperates with PBP2 in elongation-associated sacculus insertion. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 4-5, egan2020regulationofpeptidoglycan pages 7-8) |
| PBP1B | gene/protein | EC/UniProt candidate; label only | Class A PBP regulated by divisome factors and involved in septal wall synthesis activation. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 8-9) |
| FtsZ | gene/protein | UniProt/GO candidate; label only | Treadmilling division protein that controls location/rate of septal PG synthesis and links division patterning to shape. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 8-9) |
| FtsA | gene/protein | UniProt candidate; label only | Division-associated actin-like protein; implicated in morphological transitions in comparative Neisseriaceae shape evolution work. | 10.1038/s41467-022-32260-w | (nyongesa2022evolutionofmulticellular pages 10-12) |
| FtsN | gene/protein | UniProt candidate; label only | Positive divisome regulator that relieves inhibition of septal PG synthases. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 8-9) |
| FtsQ-FtsL-FtsB complex | cellular component | GO:0097047 candidate; label only | Regulatory divisome subcomplex that inhibits septal PG enzymes until activation threshold is reached. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 8-9) |
| MurF | gene/protein | EC:6.3.2.10 | Lipid II precursor-pathway enzyme linked in review evidence to MreB-centered local feedback for wall synthesis positioning. | 10.1186/s12964-025-02373-y | (wang2025mrebunravelingthe pages 11-12) |
| MraY | gene/protein | EC:2.7.8.13 | Lipid I synthesis enzyme listed among MreB-associated PG precursor factors affecting synthesis localization. | 10.1186/s12964-025-02373-y | (wang2025mrebunravelingthe pages 11-12) |
| MurG | gene/protein | EC:2.4.1.227 | Lipid II synthesis enzyme associated with MreB-linked synthesis organization in review evidence. | 10.1186/s12964-025-02373-y | (wang2025mrebunravelingthe pages 11-12) |
| Fib / fibril protein | gene/protein | label only | Spiroplasma cytoskeletal fibril that can induce membrane curvature and contributes to tapered tip structure. | 10.1038/s41467-022-34478-0 | (lartigue2022cytoskeletalcomponentscan pages 7-8) |
| tapered tip / dumbbell-shaped core | cellular component | label only | Specialized tapered-end internal structure in Spiroplasma tied to cell polarization and motility initiation. | 10.1038/s41467-022-34478-0 | (lartigue2022cytoskeletalcomponentscan media 31c75a03, lartigue2022cytoskeletalcomponentscan media 7a02a6e9) |
| elongasome | cellular component | GO:1990077 candidate | Core lateral wall-growth machinery containing MreB/RodZ/MreC/MreD/RodA/PBP2 and central to elongated-shape maintenance. | 10.1038/s41579-020-0366-3; 10.1007/978-3-030-18768-2_5 | (egan2020regulationofpeptidoglycan pages 4-5, pazos2019peptidoglycan. pages 20-23) |
| divisome | cellular component | GO:0000921 candidate | Septal wall-growth machinery containing FtsZ/FtsW/PBP3/FtsN regulators; relevant to tip/end remodeling. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 8-9, egan2020regulationofpeptidoglycan pages 7-8) |
| cell pole | cellular component | GO:0060187 | Relevant localization node because pole lipids exclude assembled MreB and A22 redirects PG insertion to poles. | 10.1007/978-3-030-18768-2_5 | (pazos2019peptidoglycan. pages 20-23) |
| plasma membrane | cellular component | GO:0005886 | Site of MreB/Fib association and curvature generation, especially in wall-less tapered-tip systems. | 10.1038/s41467-022-34478-0; 10.1007/978-3-030-18768-2_5 | (lartigue2022cytoskeletalcomponentscan pages 7-8, pazos2019peptidoglycan. pages 20-23) |
| cardiolipin | chemical | CHEBI:28494 | Pole-enriched anionic phospholipid reported to block assembled MreB filaments, influencing polarity and insertion pattern. | 10.1007/978-3-030-18768-2_5 | (pazos2019peptidoglycan. pages 20-23) |
| phosphatidylglycerol | chemical | CHEBI:17517 | Pole-enriched anionic phospholipid reported with cardiolipin in blocking assembled MreB filaments. | 10.1007/978-3-030-18768-2_5 | (pazos2019peptidoglycan. pages 20-23) |
| lipid II | chemical | CHEBI:24402 candidate | Central PG precursor whose delivery/polymerization by SEDS-PBP systems determines insertion pattern and shape. | 10.1038/s41579-020-0366-3 | (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 4-5) |
| A22 | chemical | CHEBI:label only | Experimental MreB inhibitor that depolymerizes MreB and shifts PG insertion to poles, useful as perturbation node. | 10.1007/978-3-030-18768-2_5 | (pazos2019peptidoglycan. pages 20-23) |
| RadD | gene/protein | label only | Major *F. nucleatum* adhesin for coaggregation; included as ecology-associated node, not a proven fusiform determinant. | 10.1073/pnas.2006482118; 10.3389/froh.2022.831607 | (groeger2022pathogenicmechanismsof pages 1-2, lim2025characterizationofclinical pages 18-22) |
| Fap2 | gene/protein | label only | *F. nucleatum* adhesin involved in coaggregation/cell adhesion; relevant to bridge-species role associated with fusiform cells. | 10.1101/2025.01.08.631950 | (lim2025characterizationofclinical pages 18-22) |
| FadA | gene/protein | label only | Widely present adhesin in clinical *F. nucleatum* isolates; linked to attachment/invasion rather than shape per se. | 10.1101/2025.01.08.631950; 10.1080/21505594.2024.2399217 | (lim2025characterizationofclinical pages 9-12, lim2025characterizationofclinical pages 18-22) |
| CmpA | gene/protein | label only | Oral fusobacterial adhesin candidate relevant to coaggregation/biofilm behavior in fusiform taxa. | 10.1101/2025.01.08.631950; 10.3389/froh.2022.831607 | (lim2025characterizationofclinical pages 9-12, groeger2022pathogenicmechanismsof pages 1-2) |
| FomA | gene/protein | label only | Additional *F. nucleatum* surface factor measured across isolates; useful ecology-associated node. | 10.1101/2025.01.08.631950 | (lim2025characterizationofclinical pages 9-12) |
| Aim1 / Aid1 | gene/protein | label only | Adhesin candidates implicated in oral fusobacterial interbacterial interactions; associated with bridge/biofilm ecology. | 10.1101/2025.01.08.631950; 10.3389/froh.2022.831607 | (lim2025characterizationofclinical pages 9-12, groeger2022pathogenicmechanismsof pages 1-2) |
| anaerobic growth | environment/assay factor | ENVO:01000328 candidate | *F. nucleatum* and many biofilm assays here are under anaerobic conditions, making oxygen limitation a relevant context node. | 10.1002/advs.202400882; 10.3389/froh.2022.853618 | (zhang2024outermembranevesicles pages 1-2, muchova2022fusobacteriumnucleatumsubspecies pages 2-3) |
| oral biofilm environment | environment/assay factor | ENVO:label only | The main ecological setting where fusiform *F. nucleatum* acts as bridge species and promotes colonization of partners. | 10.1080/19490976.2024.2415490; 10.1080/20002297.2022.2145729 | (krieger2024reexaminingtherole pages 1-2, fan2023fusobacteriumnucleatumand pages 1-2) |
| membrane fluidity | environment/assay factor | GO:0016042 candidate | Biophysical state controlling MreB dynamics and PG synthesis behavior via flotillin-linked membrane organization. | 10.1016/j.mib.2021.01.011 | (ducret2021recentprogressin pages 6-6) |
| crystal violet biofilm assay | environment/assay factor | label only | Standard assay used to quantify *F. nucleatum* biofilm formation in recent isolate studies; useful for phenotype evidence. | 10.1101/2025.01.08.631950; 10.3389/froh.2022.853618 | (lim2025characterizationofclinical pages 6-9, muchova2022fusobacteriumnucleatumsubspecies pages 2-3) |
| brightfield/Gram-stain microscopy cell-length assay | environment/assay factor | label only | Used at 1,000× oil immersion to quantify fusiform-cell length differences among *F. nucleatum* isolates. | 10.1101/2025.01.08.631950 | (lim2025characterizationofclinical pages 6-9, lim2025characterizationofclinical pages 9-12) |
| confocal/SEM biofilm imaging | environment/assay factor | label only | Used to analyze architecture/thickness in *F. nucleatum* subspecies biofilms and can support morphology-context curation. | 10.3389/froh.2022.853618 | (muchova2022fusobacteriumnucleatumsubspecies pages 2-3) |


*Table: This table lists candidate nodes for a fusiform-shaped microbial trait causal graph, grouped across mechanism, chemistry, ecology, and assay context. It is useful for selecting which entities are directly shape-determining versus merely associated with fusiform taxa such as Fusobacterium nucleatum.*

### 6.2 Candidate causal edges (triples) with evidence snippets
| Edge ID | Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Reference (DOI + URL) | Pub date | Context ID | Notes/uncertainty |
|---|---|---|---|---|---|---|---|---|
| FUSI-EDGE-01 | MreB (GO:0051017 candidate; label-only protein node) | guides | lateral peptidoglycan synthesis (GO:0009252) | MreB filaments match discontinuous nascent-PG patterns; its role is to “orient peptidoglycan synthesis to generate or maintain a smooth cylindrical rod shape.” (egan2020regulationofpeptidoglycan pages 8-9) | 10.1038/s41579-020-0366-3 https://doi.org/10.1038/s41579-020-0366-3 | 2020-05 | pqac-00000023 | General rod-shape mechanism; relevant to tapered/fusiform inference but not fusiform-specific. |
| FUSI-EDGE-02 | RodZ (label-only; cell shape protein) | regulates | MreB polymer localization/assembly (label-only) | RodZ “modulates geometric localization of the bacterial actin MreB to regulate cell shape” and is “required for proper assembly of the MreB actin cytoskeleton.” (wang2025mrebunravelingthe pages 21-21) | 10.1186/s12964-025-02373-y https://doi.org/10.1186/s12964-025-02373-y | 2025-08 | pqac-00000026 | Review source; outside 2023-2024 but mechanistically explicit. |
| FUSI-EDGE-03 | RodZ (label-only) | scaffolds | elongasome complex (label-only) | RodZ interacts with “MreB, RodA, PBP2 and PBP1A (and PBP1B), thereby providing a scaffold for the elongasome.” (egan2020regulationofpeptidoglycan pages 4-5) | 10.1038/s41579-020-0366-3 https://doi.org/10.1038/s41579-020-0366-3 | 2020-05 | pqac-00000022 | Strong for rod-shape machinery; indirect for fusiform outcome. |
| FUSI-EDGE-04 | MreC (label-only) | activates | PBP2 (EC:3.4.16.- candidate; label-only) | MreC induces a structural change in PBP2, promoting PBP2 TPase activity and RodA GTase activity. (egan2020regulationofpeptidoglycan pages 7-8) | 10.1038/s41579-020-0366-3 https://doi.org/10.1038/s41579-020-0366-3 | 2020-05 | pqac-00000021 | Strong enzyme-regulation edge for shape machinery; not pole/taper-specific. |
| FUSI-EDGE-05 | MreC (label-only) | activates | RodA (SEDS glycosyltransferase; label-only) | Same evidence as above: MreC promotes RodA GTase activity through PBP2-associated conformational regulation. (egan2020regulationofpeptidoglycan pages 7-8) | 10.1038/s41579-020-0366-3 https://doi.org/10.1038/s41579-020-0366-3 | 2020-05 | pqac-00000021 | Mechanistic but inferred via complex activation path. |
| FUSI-EDGE-06 | RodA (label-only) | required_for | lateral peptidoglycan incorporation (GO:0009252) | SEDS proteins “RodA, FtsW” with cognate bPBPs mediate lateral versus septal PG incorporation. (ducret2021recentprogressin pages 6-6) | 10.1016/j.mib.2021.01.011 https://doi.org/10.1016/j.mib.2021.01.011 | 2021-04 | pqac-00000024 | Good pathway-level edge; taxon-general. |
| FUSI-EDGE-07 | FtsW (label-only) | required_for | septal peptidoglycan incorporation (GO:0009252) | FtsW with cognate bPBP mediates septal PG incorporation; complex movement depends on PG synthesis rather than FtsZ treadmilling. (ducret2021recentprogressin pages 6-6) | 10.1016/j.mib.2021.01.011 https://doi.org/10.1016/j.mib.2021.01.011 | 2021-04 | pqac-00000024 | Relevant for pole/septum-localized wall growth but not directly fusiform. |
| FUSI-EDGE-08 | membrane fluidity (label-only process/state) | regulates | MreB dynamics (label-only) | Flotillins control membrane fluidity, which in turn modulates MreB dynamics and PG synthesis patterning. (ducret2021recentprogressin pages 6-6) | 10.1016/j.mib.2021.01.011 https://doi.org/10.1016/j.mib.2021.01.011 | 2021-04 | pqac-00000024 | Environmental/biophysical factor; useful candidate node. |
| FUSI-EDGE-09 | cardiolipin / phosphatidylglycerol (CHEBI candidates; label-only lipid nodes) | inhibits | assembled MreB filaments (label-only) | Cell poles are enriched in cardiolipin/phosphatidylglycerol, which “block MreB filaments but not monomers.” (pazos2019peptidoglycan. pages 20-23) | 10.1007/978-3-030-18768-2_5 https://doi.org/10.1007/978-3-030-18768-2_5 | 2019-01 | pqac-00000019 | Strong pole-localization mechanism; extrapolated to tapered-pole morphogenesis. |
| FUSI-EDGE-10 | A22 (CHEBI candidate; MreB inhibitor) | inhibits | MreB polymerization (label-only) | “A22 prevents polymerization” of MreB and yields homogeneous cytoplasmic MreB. (pazos2019peptidoglycan. pages 20-23) | 10.1007/978-3-030-18768-2_5 https://doi.org/10.1007/978-3-030-18768-2_5 | 2019-01 | pqac-00000019 | Experimental perturbation edge. |
| FUSI-EDGE-11 | A22 (CHEBI candidate) | promotes | polar peptidoglycan insertion (GO:0009252 candidate) | Upon MreB inhibition by A22, PG insertion “shifts to cell poles.” (pazos2019peptidoglycan. pages 20-23) | 10.1007/978-3-030-18768-2_5 https://doi.org/10.1007/978-3-030-18768-2_5 | 2019-01 | pqac-00000019 | Useful assay-specific edge for pole-biased growth; not a native mechanism. |
| FUSI-EDGE-12 | Fib/fibril protein (label-only) | promotes | membrane curvature (GO:0032989 candidate) | In Spiroplasma, Fib can “induce membrane curvature on its own” and is observed close to the membrane. (lartigue2022cytoskeletalcomponentscan pages 7-8) | 10.1038/s41467-022-34478-0 https://doi.org/10.1038/s41467-022-34478-0 | 2022-11 | pqac-00000000 | Wall-less bacterium; taxon-specific, but directly relevant to tapered end generation. |
| FUSI-EDGE-13 | MreB5 (label-only paralog) | promotes | helical/tapered-end morphology program (label-only) | “MreB5 is sufficient to confer helicity and kink propagation” in recombinant mycoplasma cells. (lartigue2022cytoskeletalcomponentscan pages 7-8) | 10.1038/s41467-022-34478-0 https://doi.org/10.1038/s41467-022-34478-0 | 2022-11 | pqac-00000000 | Direct morphology perturbation, but outcome is helicity rather than fusiform alone. |
| FUSI-EDGE-14 | Fib/fibril protein + MreB isoforms (label-only complex/program) | required_for | tapered tip structure (label-only) | Spiroplasma tapered tip is linked to internal cytoskeletal system; tip/tapered “duckbill-shaped end” contains a dumbbell-shaped core involved in polarization/motility initiation. (lartigue2022cytoskeletalcomponentscan media 31c75a03, lartigue2022cytoskeletalcomponentscan media 7a02a6e9) | 10.1038/s41467-022-34478-0 https://doi.org/10.1038/s41467-022-34478-0 | 2022-11 | pqac-00000017 | Strong morphology-localization edge, but specialized to Spiroplasma tip. |
| FUSI-EDGE-15 | Fusiform morphology (METPO:1000690) | promotes | coaggregation bridge role in oral biofilm (label-only ecological role) | “its long, fusiform morphology and promiscuous coaggregation ability are central to its role as a bridge species in the oral biofilm.” (krieger2024reexaminingtherole pages 1-2) | 10.1080/19490976.2024.2415490 https://doi.org/10.1080/19490976.2024.2415490 | 2024-10 | pqac-00000027 | Strong organism-level association for F. nucleatum; not a gene-level mechanism. |
| FUSI-EDGE-16 | Fusobacterium nucleatum (NCBITaxon candidate; label-only) | has_phenotype | fusiform rod shape (METPO:1000690) | F. nucleatum is described as “a gram-negative, specialized anaerobic bacterium with a fusiform rod shape.” (zhang2024outermembranevesicles pages 1-2) | 10.1002/advs.202400882 https://doi.org/10.1002/advs.202400882 | 2024-10 | pqac-00000004 | Taxon-phenotype assertion; suitable phenotype grounding edge. |
| FUSI-EDGE-17 | Fusobacterium nucleatum (NCBITaxon candidate; label-only) | promotes | colonization of other oral pathogens (label-only) | F. nucleatum “helps promote the colonization of other pathogens ... by establishing an efficient biofilm.” (zhang2024outermembranevesicles pages 1-2) | 10.1002/advs.202400882 https://doi.org/10.1002/advs.202400882 | 2024-10 | pqac-00000004 | Ecological function; morphology contribution is implied, not isolated experimentally. |
| FUSI-EDGE-18 | FadA (label-only adhesin) | present_in | all 8 clinical F. nucleatum isolates (label-only strain set) | In the pilot strain set, “all carried the fadA gene.” (lim2025characterizationofclinical pages 9-12, lim2025characterizationofclinical pages 12-18) | 10.1101/2025.01.08.631950 https://doi.org/10.1101/2025.01.08.631950 | 2025-01 | pqac-00000029 | Evidence for common adhesin presence in fusiform isolates; preprint; not causal for fusiform shape. |
| FUSI-EDGE-19 | cmpA / fap2 / radD (label-only adhesins) | absent_from | 8 clinical F. nucleatum isolates (label-only strain set) | “none of the clinical isolates carried cmpA, fap2, or radD.” (lim2025characterizationofclinical pages 12-18) | 10.1101/2025.01.08.631950 https://doi.org/10.1101/2025.01.08.631950 | 2025-01 | pqac-00000034 | Presence/absence evidence only; useful caution against assuming these genes explain fusiform morphology. |
| FUSI-EDGE-20 | longer F. nucleatum cells (label-only morphology state) | associated_with | colonization/biofilm formation (label-only) | Clinical isolates showed ~2–13 µm lengths; increased length was suggested to aid colonization and biofilm formation, though controls were shorter yet stronger biofilm formers. (lim2025characterizationofclinical pages 9-12) | 10.1101/2025.01.08.631950 https://doi.org/10.1101/2025.01.08.631950 | 2025-01 | pqac-00000003 | Weak/inferred and internally mixed evidence; should be curated cautiously. |


*Table: This table lists evidence-backed candidate causal edges for curating the microbial fusiform-shaped trait, spanning general cell-shape machinery, tapered-tip mechanisms, and Fusobacterium nucleatum ecological associations. It is useful for selecting high-confidence versus cautionary TraitMech assertions.*


## 7. Ontology grounding notes (what can be grounded vs label-only)
- **Phenotype:** METPO:1000690 is directly provided and usable.
- **Processes:** GO:0009252 (peptidoglycan biosynthetic process) is stable; more specific “polar PG insertion” is not directly represented in cited evidence as a GO term, so may remain label-only unless mapped carefully. (egan2020regulationofpeptidoglycan pages 7-8, pazos2019peptidoglycan. pages 20-23)
- **Chemicals:** cardiolipin (CHEBI:28494) and phosphatidylglycerol (CHEBI:17517) are stable. (pazos2019peptidoglycan. pages 20-23)
- **Proteins/genes:** MreB/RodZ/MreC/MreD/RodA/FtsW/PBPs are best grounded per-organism (UniProt/NCBI Gene) in curation; current evidence here supports them as label-only nodes pending selection of a specific chassis taxon. (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 4-5)


## 8. Warnings / claims not yet ready for TraitMech curation
1. **Fusiform morphology is not yet mechanistically decomposed in *Fusobacterium* in the provided evidence.** The strongest 2024 statement links fusiform morphology to coaggregation/biofilm bridging at an organism/ecology level, but does not establish a gene-level causal chain for tapered-end geometry. Curate these as association edges unless a direct morphogenesis mechanism is sourced. (krieger2024reexaminingtherole pages 1-2)
2. **Cell length vs biofilm capacity relationships are inconsistent in the pilot isolate dataset.** The preprint suggests longer cells could aid colonization/biofilm, yet the shorter ATCC strains formed the strongest biofilms in vitro. This should be curated as uncertain/strain-dependent rather than a general rule. (lim2025characterizationofclinical pages 9-12)
3. **A22-induced pole insertion is an experimental perturbation, not a native determinant of fusiform shape.** It is valuable as an edge for “assay factor → pole-biased PG insertion” but should not be curated as a natural causal pathway to fusiform morphology without additional evidence. (pazos2019peptidoglycan. pages 20-23)
4. **Spiroplasma tapered-tip mechanisms are taxon-specific and wall-less.** Edges involving Fib/fibril and multiple MreB isoforms support tapered end generation in a membrane/cytoskeletal context, but may not transfer to walled fusiform bacteria. Mark as taxon-specific. (lartigue2022cytoskeletalcomponentscan pages 7-8, lartigue2022cytoskeletalcomponentscan media 31c75a03)


## 9. DOI-first bibliography (with URLs and publication dates)
- Krieger M, Guo M, Merritt J. *Reexamining the role of Fusobacterium nucleatum subspecies in clinical and experimental studies.* **Gut Microbes**. 2024-10. DOI: **10.1080/19490976.2024.2415490**. https://doi.org/10.1080/19490976.2024.2415490 (krieger2024reexaminingtherole pages 1-2)
- Zhang L, et al. *Outer Membrane Vesicles Derived From Fusobacterium nucleatum Trigger Periodontitis Through Host Overimmunity.* **Advanced Science**. 2024-10. DOI: **10.1002/advs.202400882**. https://doi.org/10.1002/advs.202400882 (zhang2024outermembranevesicles pages 1-2)
- Fan Z, et al. *Fusobacterium nucleatum and its associated systemic diseases: epidemiologic studies and possible mechanisms.* **Journal of Oral Microbiology**. 2023-11. DOI: **10.1080/20002297.2022.2145729**. https://doi.org/10.1080/20002297.2022.2145729 (fan2023fusobacteriumnucleatumand pages 1-2)
- Groeger S, et al. *Pathogenic Mechanisms of Fusobacterium nucleatum on Oral Epithelial Cells.* **Frontiers in Oral Health**. 2022-04. DOI: **10.3389/froh.2022.831607**. https://doi.org/10.3389/froh.2022.831607 (groeger2022pathogenicmechanismsof pages 1-2)
- Lartigue C, et al. *Cytoskeletal components can turn wall-less spherical bacteria into kinking helices.* **Nature Communications**. 2022-11. DOI: **10.1038/s41467-022-34478-0**. https://doi.org/10.1038/s41467-022-34478-0 (lartigue2022cytoskeletalcomponentscan pages 7-8, lartigue2022cytoskeletalcomponentscan media 31c75a03)
- Egan AJF, Errington J, Vollmer W. *Regulation of peptidoglycan synthesis and remodelling.* **Nature Reviews Microbiology**. 2020-05. DOI: **10.1038/s41579-020-0366-3**. https://doi.org/10.1038/s41579-020-0366-3 (egan2020regulationofpeptidoglycan pages 7-8, egan2020regulationofpeptidoglycan pages 8-9)
- Ducret A, Grangeasse C. *Recent progress in our understanding of peptidoglycan assembly in firmicutes.* **Current Opinion in Microbiology**. 2021-04. DOI: **10.1016/j.mib.2021.01.011**. https://doi.org/10.1016/j.mib.2021.01.011 (ducret2021recentprogressin pages 6-6)
- Pazos M, Peters K. *Peptidoglycan.* **Sub-cellular Biochemistry**. 2019-01. DOI: **10.1007/978-3-030-18768-2_5**. https://doi.org/10.1007/978-3-030-18768-2_5 (pazos2019peptidoglycan. pages 20-23)
- Lim S, et al. *Characterization of Clinical Fusobacterium nucleatum Isolates from Oral Squamous Cell Carcinoma Patients.* **bioRxiv** (preprint). 2025-01. DOI: **10.1101/2025.01.08.631950**. https://doi.org/10.1101/2025.01.08.631950 (lim2025characterizationofclinical pages 9-12, lim2025characterizationofclinical pages 1-6)
- Connolly JP, Kelly L. *The physical biogeography of Fusobacterium nucleatum in health and disease.* **mBio**. 2025-04. DOI: **10.1128/mbio.02989-24**. https://doi.org/10.1128/mbio.02989-24 (connolly2025thephysicalbiogeography pages 3-5)



References

1. (zhang2024outermembranevesicles pages 1-2): Li Zhang, Demao Zhang, Chengcheng Liu, Boyu Tang, Yujia Cui, Daimo Guo, Mengmeng Duan, Ying Tu, Huiling Zheng, Xinjie Ning, Yang Liu, Haoran Chen, Minglei Huang, Zhixing Niu, Yanfang Zhao, Xiaoheng Liu, and Jing Xie. Outer membrane vesicles derived from fusobacterium nucleatum trigger periodontitis through host overimmunity. Advanced Science, Oct 2024. URL: https://doi.org/10.1002/advs.202400882, doi:10.1002/advs.202400882. This article has 62 citations and is from a peer-reviewed journal.

2. (krieger2024reexaminingtherole pages 1-2): Madeline Krieger, Mingzhe Guo, and Justin Merritt. Reexamining the role of fusobacterium nucleatum subspecies in clinical and experimental studies. Gut Microbes, Oct 2024. URL: https://doi.org/10.1080/19490976.2024.2415490, doi:10.1080/19490976.2024.2415490. This article has 28 citations and is from a peer-reviewed journal.

3. (lartigue2022cytoskeletalcomponentscan media 31c75a03): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

4. (egan2020regulationofpeptidoglycan pages 8-9): Alexander J. F. Egan, Jeff Errington, and Waldemar Vollmer. Regulation of peptidoglycan synthesis and remodelling. Nature Reviews Microbiology, 18:446-460, May 2020. URL: https://doi.org/10.1038/s41579-020-0366-3, doi:10.1038/s41579-020-0366-3. This article has 682 citations and is from a highest quality peer-reviewed journal.

5. (lartigue2022cytoskeletalcomponentscan pages 7-8): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (lim2025characterizationofclinical pages 9-12): Serene Lim, Wan-Hsin Hsueh, Ni-Hung Wu, Claire Hodges, Christopher Vuong, Kynzi Smith, Jenn-Ren Hsiao, Jeffrey S Chang, Jang-Yang Chang, Jenn-Wei Chen, and I-Hsiu Huang. Characterization of clinical fusobacterium nucleatum isolates from oral squamous cell carcinoma patients. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.08.631950, doi:10.1101/2025.01.08.631950. This article has 1 citations.

7. (egan2020regulationofpeptidoglycan pages 7-8): Alexander J. F. Egan, Jeff Errington, and Waldemar Vollmer. Regulation of peptidoglycan synthesis and remodelling. Nature Reviews Microbiology, 18:446-460, May 2020. URL: https://doi.org/10.1038/s41579-020-0366-3, doi:10.1038/s41579-020-0366-3. This article has 682 citations and is from a highest quality peer-reviewed journal.

8. (egan2020regulationofpeptidoglycan pages 4-5): Alexander J. F. Egan, Jeff Errington, and Waldemar Vollmer. Regulation of peptidoglycan synthesis and remodelling. Nature Reviews Microbiology, 18:446-460, May 2020. URL: https://doi.org/10.1038/s41579-020-0366-3, doi:10.1038/s41579-020-0366-3. This article has 682 citations and is from a highest quality peer-reviewed journal.

9. (pazos2019peptidoglycan. pages 20-23): Manuel Pazos and Katharina Peters. Peptidoglycan. Sub-cellular biochemistry, 92:127-168, Jan 2019. URL: https://doi.org/10.1007/978-3-030-18768-2\_5, doi:10.1007/978-3-030-18768-2\_5. This article has 128 citations.

10. (lartigue2022cytoskeletalcomponentscan media 7a02a6e9): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

11. (fan2023fusobacteriumnucleatumand pages 1-2): Zixin Fan, Pengzhou Tang, Cheng Li, Qi Yang, Yan Xu, Chuan Su, and Lu Li. Fusobacterium nucleatum and its associated systemic diseases: epidemiologic studies and possible mechanisms. Journal of Oral Microbiology, Nov 2023. URL: https://doi.org/10.1080/20002297.2022.2145729, doi:10.1080/20002297.2022.2145729. This article has 160 citations and is from a domain leading peer-reviewed journal.

12. (lim2025characterizationofclinical pages 6-9): Serene Lim, Wan-Hsin Hsueh, Ni-Hung Wu, Claire Hodges, Christopher Vuong, Kynzi Smith, Jenn-Ren Hsiao, Jeffrey S Chang, Jang-Yang Chang, Jenn-Wei Chen, and I-Hsiu Huang. Characterization of clinical fusobacterium nucleatum isolates from oral squamous cell carcinoma patients. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.08.631950, doi:10.1101/2025.01.08.631950. This article has 1 citations.

13. (groeger2022pathogenicmechanismsof pages 1-2): Sabine Groeger, Yuxi Zhou, Sabine Ruf, and Joerg Meyle. Pathogenic mechanisms of fusobacterium nucleatum on oral epithelial cells. Frontiers in Oral Health, Apr 2022. URL: https://doi.org/10.3389/froh.2022.831607, doi:10.3389/froh.2022.831607. This article has 101 citations and is from a peer-reviewed journal.

14. (connolly2025thephysicalbiogeography pages 3-5): John P. Connolly and Libusha Kelly. The physical biogeography of <i>fusobacterium nucleatum</i> in health and disease. Apr 2025. URL: https://doi.org/10.1128/mbio.02989-24, doi:10.1128/mbio.02989-24. This article has 18 citations and is from a domain leading peer-reviewed journal.

15. (ducret2021recentprogressin pages 6-6): Adrien Ducret and Christophe Grangeasse. Recent progress in our understanding of peptidoglycan assembly in firmicutes. Current Opinion in Microbiology, 60:44-50, Apr 2021. URL: https://doi.org/10.1016/j.mib.2021.01.011, doi:10.1016/j.mib.2021.01.011. This article has 23 citations and is from a peer-reviewed journal.

16. (lim2025characterizationofclinical pages 1-6): Serene Lim, Wan-Hsin Hsueh, Ni-Hung Wu, Claire Hodges, Christopher Vuong, Kynzi Smith, Jenn-Ren Hsiao, Jeffrey S Chang, Jang-Yang Chang, Jenn-Wei Chen, and I-Hsiu Huang. Characterization of clinical fusobacterium nucleatum isolates from oral squamous cell carcinoma patients. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.08.631950, doi:10.1101/2025.01.08.631950. This article has 1 citations.

17. (connolly2025thephysicalbiogeography pages 1-3): John P. Connolly and Libusha Kelly. The physical biogeography of <i>fusobacterium nucleatum</i> in health and disease. Apr 2025. URL: https://doi.org/10.1128/mbio.02989-24, doi:10.1128/mbio.02989-24. This article has 18 citations and is from a domain leading peer-reviewed journal.

18. (wang2025mrebunravelingthe pages 11-12): Yaqi Wang, Yalan Jiang, Zhixuan Song, Chengbin Zhu, Yujun Tang, Jiaofeng Peng, and Peng Liu. Mreb: unraveling the molecular mechanisms of bacterial shape, division, and environmental adaptation. Cell Communication and Signaling, Aug 2025. URL: https://doi.org/10.1186/s12964-025-02373-y, doi:10.1186/s12964-025-02373-y. This article has 11 citations and is from a peer-reviewed journal.

19. (wang2025mrebunravelingthe pages 21-21): Yaqi Wang, Yalan Jiang, Zhixuan Song, Chengbin Zhu, Yujun Tang, Jiaofeng Peng, and Peng Liu. Mreb: unraveling the molecular mechanisms of bacterial shape, division, and environmental adaptation. Cell Communication and Signaling, Aug 2025. URL: https://doi.org/10.1186/s12964-025-02373-y, doi:10.1186/s12964-025-02373-y. This article has 11 citations and is from a peer-reviewed journal.

20. (nyongesa2022evolutionofmulticellular pages 10-12): Sammy Nyongesa, Philipp Weber, Eve Bernet, Francisco Pullido, Marta Nieckarz, Marie Delaby, Cecilia Nieves, Tobias Viehboeck, Nicole Krause, Alex Rivera-Millot, Arnaldo Nakamura, Norbert Vischer, Michael VanNieuwenhze, Yves Brun, Felipe Cava, Silvia Bulgheresi, and Frédéric Veyrier. Evolution of multicellular longitudinally dividing oral cavity symbionts (neisseriaceae). ArXiv, Jan 2022. URL: https://doi.org/10.21203/rs.3.rs-1200288/v1, doi:10.21203/rs.3.rs-1200288/v1. This article has 5 citations.

21. (lim2025characterizationofclinical pages 18-22): Serene Lim, Wan-Hsin Hsueh, Ni-Hung Wu, Claire Hodges, Christopher Vuong, Kynzi Smith, Jenn-Ren Hsiao, Jeffrey S Chang, Jang-Yang Chang, Jenn-Wei Chen, and I-Hsiu Huang. Characterization of clinical fusobacterium nucleatum isolates from oral squamous cell carcinoma patients. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.08.631950, doi:10.1101/2025.01.08.631950. This article has 1 citations.

22. (muchova2022fusobacteriumnucleatumsubspecies pages 2-3): Maria Muchova, Dario L. Balacco, Melissa M. Grant, Iain L. C. Chapple, Sarah A. Kuehne, and Josefine Hirschfeld. Fusobacterium nucleatum subspecies differ in biofilm forming ability in vitro. Frontiers in Oral Health, Mar 2022. URL: https://doi.org/10.3389/froh.2022.853618, doi:10.3389/froh.2022.853618. This article has 58 citations and is from a peer-reviewed journal.

23. (lim2025characterizationofclinical pages 12-18): Serene Lim, Wan-Hsin Hsueh, Ni-Hung Wu, Claire Hodges, Christopher Vuong, Kynzi Smith, Jenn-Ren Hsiao, Jeffrey S Chang, Jang-Yang Chang, Jenn-Wei Chen, and I-Hsiu Huang. Characterization of clinical fusobacterium nucleatum isolates from oral squamous cell carcinoma patients. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.08.631950, doi:10.1101/2025.01.08.631950. This article has 1 citations.