---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:59:31.315663'
end_time: '2026-06-18T09:19:49.532464'
duration_seconds: 1218.22
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pink pigmented
  trait_identifier: METPO:1003027
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: pink_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    pink due to accumulation of pink or rose carotenoid pigments.
  parent_traits: METPO:1003021
  synonyms: Pigment_pink
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow
    pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated
    color phenotype.)'
  causal_graph_summary: 'pink_pigmented_carotenoid_color: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pink pigmented
- **METPO identifier:** METPO:1003027
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear pink due to accumulation of pink or rose carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_pink
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated color phenotype.)
- **Existing causal graph summary:** pink_pigmented_carotenoid_color: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **pink pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pink_pigmented.yaml`.

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
- **Trait label:** pink pigmented
- **METPO identifier:** METPO:1003027
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear pink due to accumulation of pink or rose carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_pink
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated color phenotype.)
- **Existing causal graph summary:** pink_pigmented_carotenoid_color: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **pink pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pink_pigmented.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **pink pigmented** (METPO:1003027)

### 1) Scope summary (TraitMech-oriented)
**Trait definition (curation scope).** *Pink pigmented* is an **assay-observed morphological phenotype** in which microbial colonies or cells appear pink due to accumulation of pigments. In the current mechanistic literature, pink coloration most commonly arises from **carotenoid accumulation** (particularly C50 carotenoids such as **bacterioruberin** in haloarchaea, or carotenoids produced by **crt** genes in bacterial photosynthesis gene clusters). (ma2024thebiosynthesismechanism pages 2-6, strakova2024unveilingthegenomic pages 11-13, sandmann2023genesandpathway pages 1-3)

**Boundary cases / exclusion criteria.** The *pink* descriptor is not uniquely carotenoid-derived. For example, *Serratia marcescens* is described as producing a **“pink pigment prodigiosin”**, a **non-carotenoid tripyrrole** pigment system; this should be treated as a **separate mechanism** and not merged into a carotenoid causal graph without taxon-specific evidence. (wang2024hostsmanipulatelifestyle pages 1-5, guryanov2024bacterialpigmentprodigiosin pages 1-2)

**Assay contexts that influence observation.** Pigmentation can vary with growth phase, oxygen/light regimes (especially in phototrophs where pigment genes are embedded in photosynthesis gene clusters), and salinity/nutrient conditions (notably for haloarchaeal bacterioruberin). (godoy2023asingularppaaaerrlike pages 5-9, ma2024thebiosynthesismechanism pages 6-8, sandmann2023genesandpathway pages 3-5)

### 2) Key concepts and definitions (current understanding)
#### 2.1 Carotenoid-driven pink pigmentation
Carotenoids are isoprenoid pigments produced from prenyl precursors (e.g., via the **mevalonate (MVA) pathway** in many archaea) and modified by desaturases/cyclases/oxygenases to yield colored molecules; in purple bacteria, pigmentation reflects a **combination of bacteriochlorophylls and carotenoids**. (barreto2023microbialpigmentsmajor pages 4-6, ma2024thebiosynthesismechanism pages 2-6, sandmann2023genesandpathway pages 1-3)

In haloarchaea, **bacterioruberin (BR)** (a C50 carotenoid) is a major determinant of pink-to-red coloration and is often emphasized as an adaptive protective pigment. (strakova2024unveilingthegenomic pages 11-13, ma2024thebiosynthesismechanism pages 2-6)

#### 2.2 Genetic organization: photosynthesis gene clusters (PGCs)
In purple bacteria, **carotenoid pathway genes are part of photosynthesis gene clusters**, enabling coordinated regulation and horizontal transfer of pigment capacity. (sandmann2023genesandpathway pages 1-3)

A concrete example appears in a novel *Bradyrhizobium* species description where photosynthesis genes and **carotenoid biosynthesis genes (crtCBICDEF)** are present; colonies are described as **pink** on agar. (zhang2023geneticdiversityinto pages 9-10, zhang2023geneticdiversityinto pages 7-8)

#### 2.3 Non-carotenoid “pink” pigments (boundary mechanism)
Prodigiosin is chemically distinct (tripyrrole) and can be described as yielding hues including **pink**, but it should be curated under a separate pigment mechanism rather than carotenoid biosynthesis. (wang2024hostsmanipulatelifestyle pages 1-5, guryanov2024bacterialpigmentprodigiosin pages 1-2)

### 3) Recent developments and latest research (prioritizing 2023–2024)
#### 3.1 Mechanistic dissection of bacterioruberin biosynthesis and regulation (2024)
A 2024 *Applied and Environmental Microbiology* study on **Halorubrum sp. HRM-150** provides a detailed **genome + transcriptome + perturbation** view of bacterioruberin synthesis, including:
- **Dominance of BR** in total carotenoids (~85% in this strain). (ma2024thebiosynthesismechanism pages 2-6)
- A proposed **de novo BR pathway** with **lyeJ** as a **key gene**, and explicit recognition of **competitive branches** (notably **retinal** biosynthesis) that share the substrate **lycopene**. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 6-8)
- Strong environmental modulation: an **osmotic down-shock** (to 14% salinity) increased BR per cell significantly (quantified) and altered expression of BR-pathway genes. (ma2024thebiosynthesismechanism pages 6-8)

Figure-level mechanistic support (pathway + expression overlays) is available from the same paper. (ma2024thebiosynthesismechanism media 27651990, ma2024thebiosynthesismechanism media 848c505f, ma2024thebiosynthesismechanism media 1f0d76f2)

#### 3.2 Genome-based linking of bacterioruberin genes in new haloarchaeal isolates (2024)
A 2024 *Frontiers in Marine Science* taxogenomic study of *Halogeometricum* highlights that genomes encode **CrtD, LyeJ and CruF**, described as being **“responsible for the production of bacterioruberin from lycopene”**. It also notes presence of **blh** (β-carotene 15,15′-dioxygenase) in some strains that converts β-carotene to **retinal**, connecting pigment biosynthesis to rhodopsin physiology and potential metabolic competition. (strakova2024unveilingthegenomic pages 11-13)

#### 3.3 Modern synthesis of carotenoid gene/pathway knowledge in phototrophs (2023)
A 2023 review in *Biology* synthesizes crt gene organization and regulation in purple bacteria, including:
- crt genes frequently arranged in clusters (e.g., **crtFECD** and **crtBIA**).
- Oxygen-dependent regulation: **“oxygen up-regulates the crtI-crtB operon”**, providing an environmental regulator node for pigmentation intensity. (sandmann2023genesandpathway pages 3-5)

### 4) Current applications and real-world implementations
#### 4.1 Haloarchaea as pigment cell factories (bacterioruberin)
Haloarchaeal bacterioruberin is presented as a **bioactive natural pigment** with **potential food, cosmetic, and biomedical applications**, and haloarchaea are positioned as promising microbial factories due to stress tolerance and production characteristics. (ma2024thebiosynthesismechanism pages 1-2, strakova2024unveilingthegenomic pages 11-13)

#### 4.2 Process optimization using inexpensive substrates and salinity perturbations
The Halorubrum study provides concrete examples of process-level levers:
- **Glucose (10 g/L)** and **tryptone (15 g/L)** improved BR production.
- **Glucose + starch** induced diauxic growth and increased biomass and BR productivity.
- **Osmotic down-shock** increased BR content per cell without sacrificing biomass, suggesting a scalable, operational knob for improving pink pigmentation intensity/yield. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 6-8, ma2024thebiosynthesismechanism pages 2-6)

#### 4.3 Pigment as an ecological/physiological indicator (boundary-case)
In a host–microbe model, prodigiosin was described as a **visible bioindicator** of *Serratia* metabolism because its production is “characteristically oscillatory to metabolic activities.” While not carotenoid-based, this supports the general point that “pink pigmentation” may be used observationally as a proxy for physiological state. (wang2024hostsmanipulatelifestyle pages 1-5)

### 5) Relevant statistics and data from recent studies
#### 5.1 Quantitative bacterioruberin composition and yields (2024)
From Halorubrum sp. HRM-150:
- **Bacterioruberin fraction:** ~**85%** of total carotenoids. (ma2024thebiosynthesismechanism pages 2-6)
- **Maximum OD600 and BR productivity:** **OD600 2.73 ± 0.14**; **BR productivity 1.44 ± 0.04 μg/mL** (reported in the same study’s results summary). (ma2024thebiosynthesismechanism pages 2-6)
- **Carbon-source effects:** glucose increased BR productivity (e.g., **1.98 ± 0.05 μg/mL**); glucose+starch improved BR productivity to **3.04 ± 0.31 μg/mL** (54% higher than glucose alone). (ma2024thebiosynthesismechanism pages 2-6)
- **Osmotic down-shock effect:** at **14% salinity**, BR per cell peaked at **4.83 × 10−10 μg/cell**, a **48% increase** vs 20% salinity. (ma2024thebiosynthesismechanism pages 6-8)

### 6) Candidate causal-graph nodes (grouped by type)
The following node inventory is intended to seed `data/traits/morphology/pink_pigmented.yaml`.

| Group | Candidate node label | Suggested CURIE | Role in pink pigmentation | Evidence note | Citation |
|---|---|---|---|---|---|
| Pigments/metabolites | bacterioruberin |  | Major C50 carotenoid directly underlying pink-red coloration in haloarchaea; dominant pigment in Halorubrum sp. HRM-150 | Reported as the main carotenoid, ~85% of total carotenoids, with pink/red phenotype relevance | (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) |
| Pigments/metabolites | lycopene | CHEBI:15948 | Central precursor for bacterioruberin and retinal branches; diversion of lycopene affects final hue/intensity | Ma 2024 identifies competition between retinal and BR for common substrate lycopene | (ma2024thebiosynthesismechanism pages 6-8, strakova2024unveilingthegenomic pages 11-13) |
| Pigments/metabolites | retinal | CHEBI:17336 | Competing branch product from β-carotene; may reduce flux to bacterioruberin-associated pink pigmentation | β-carotene dioxygenase branch to retinal is linked to rhodopsin physiology and competition with BR pathway | (ma2024thebiosynthesismechanism pages 6-8, strakova2024unveilingthegenomic pages 11-13) |
| Pigments/metabolites | β-carotene | CHEBI:7382 | Intermediate/branch-point carotenoid feeding retinal production; indirect effect on pink phenotype via flux competition | blh-mediated conversion of β-carotene to retinal noted in haloarchaeal genomes | (strakova2024unveilingthegenomic pages 11-13) |
| Pigments/metabolites | phytoene | CHEBI:26128 | Early carotenoid precursor in crt pathway; required upstream of colored carotenoids | Sandmann review and haloarchaeal BGC summaries identify crtB/phytoene synthase step | (sandmann2023genesandpathway pages 3-5, nagar2024genomicinsightson pages 5-6) |
| Pigments/metabolites | neurosporene |  | Colored carotenoid intermediate in purple-bacterial pathways; relevant for pink/orange/red shades in phototrophs | Review documents crt-mediated formation and pathway branching | (sandmann2023genesandpathway pages 12-14) |
| Pigments/metabolites | spheroidene |  | Colored carotenoid product in purple bacteria; contributes to visible colony pigmentation | Carotenoid pathways in purple bacteria produce spheroidene/spirilloxanthin family pigments | (sandmann2023genesandpathway pages 12-14, sandmann2023genesandpathway pages 1-3) |
| Pigments/metabolites | spirilloxanthin |  | Colored carotenoid product in purple bacteria; can contribute to pink-red appearance in phototrophs | Review highlights spirilloxanthin pathway genes and enzymes | (sandmann2023genesandpathway pages 12-14, sandmann2023genesandpathway pages 3-5) |
| Pigments/metabolites | prodigiosin |  | Boundary-case non-carotenoid pink/red pigment; should not be conflated with carotenoid-based trait mechanism without taxon-specific evidence | Serratia sources describe pink/red prodigiosin as a distinct tripyrrole pigment system | (wang2024hostsmanipulatelifestyle pages 1-5, guryanov2024bacterialpigmentprodigiosin pages 14-15, guryanov2024bacterialpigmentprodigiosin pages 1-2) |
| Pathways/modules | bacterioruberin biosynthetic pathway |  | Direct causal pathway producing haloarchaeal pink pigmentation | De-novo BR pathway resolved by genome/transcriptome analysis | (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism media 27651990) |
| Pathways/modules | carotenoid biosynthetic process | GO:0016117 | General pathway class producing colored carotenoids underlying many pink phenotypes | Supported across purple bacteria and haloarchaea | (sandmann2023genesandpathway pages 12-14, sandmann2023genesandpathway pages 1-3) |
| Pathways/modules | mevalonate pathway | GO:0006695 | Supplies IPP for archaeal carotenoid biosynthesis and thus BR production | Ma 2024 places BR biosynthesis downstream of alternative MVA route | (ma2024thebiosynthesismechanism pages 2-6) |
| Pathways/modules | photosynthesis gene cluster (PGC) |  | Genomic module co-localizing crt genes with photosynthesis genes in pigmented phototrophs | Bradyrhizobium roseus-like strain carries crt genes in PGC; review states carotenoid genes are part of PGCs | (zhang2023geneticdiversityinto pages 7-8, zhang2023geneticdiversityinto pages 8-9, sandmann2023genesandpathway pages 1-3) |
| Pathways/modules | retinal biosynthetic branch |  | Competing pathway that can drain carotenoid precursors away from BR-associated pink pigmentation | Transcriptome evidence indicates competing retinal branch genes are downregulated when BR synthesis is favored | (ma2024thebiosynthesismechanism pages 6-8, nagar2024genomicinsightson pages 6-8) |
| Pathways/modules | prodigiosin biosynthetic pathway |  | Boundary-case alternative pigment pathway producing pink/red color outside carotenoid systems | Distinct MAP+MBC condensation pathway in Serratia/Streptomyces | (kumar2024isolationandcharacterization pages 18-22, guryanov2024bacterialpigmentprodigiosin pages 1-2) |
| Genes/enzymes/proteins | lyeJ |  | Key BR-pathway gene; promotes conversion toward bacterioruberin and stronger pink/red pigmentation | Ma 2024 identifies lyeJ as key gene and proposes overexpression to improve BR yield | (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 6-8) |
| Genes/enzymes/proteins | CruF |  | BR-pathway enzyme/protein contributing to conversion from lycopene-derived intermediates to bacterioruberin | Conserved in haloarchaeal BR pathway; expression responds early after osmotic down-shock | (ma2024thebiosynthesismechanism pages 6-8, strakova2024unveilingthegenomic pages 11-13, nagar2024genomicinsightson pages 5-6) |
| Genes/enzymes/proteins | CrtD |  | Carotenoid desaturase involved in BR or purple-bacterial carotenoid pathway progression | Named in haloarchaeal BR pathway and purple-bacterial carotenoid review | (ma2024thebiosynthesismechanism pages 2-6, sandmann2023genesandpathway pages 3-5) |
| Genes/enzymes/proteins | crtB / phytoene synthase |  | Early committed carotenoid enzyme; required for colored carotenoid accumulation | Present in haloarchaeal BGCs and Bradyrhizobium/PGC-associated carotenoid systems | (zhang2023geneticdiversityinto pages 7-8, nagar2024genomicinsightson pages 5-6) |
| Genes/enzymes/proteins | crtI / phytoene desaturase |  | Converts phytoene toward colored carotenoids; major determinant of pathway output | Review emphasizes crtI function and regulation; haloarchaeal BGCs include crtI | (sandmann2023genesandpathway pages 3-5, nagar2024genomicinsightson pages 5-6) |
| Genes/enzymes/proteins | crtC |  | Hydratase in purple-bacterial carotenoid pathways; affects downstream pigment profile | Presence/absence changes specific carotenoid outcomes such as rhodopin/spirilloxanthin-pathway products | (nery2023quantummechanicaleffects pages 46-49, sandmann2023genesandpathway pages 3-5) |
| Genes/enzymes/proteins | crtF |  | Methylase in purple-bacterial carotenoid pathway; influences final carotenoid composition | Included in purple-bacterial crt clusters and pathway steps | (sandmann2023genesandpathway pages 3-5) |
| Genes/enzymes/proteins | crtA |  | Ketolase in some purple-bacterial pathways; absence/presence alters ketolated carotenoids and color | Review notes species differences in crtA content and pigment outcomes | (sandmann2023genesandpathway pages 3-5) |
| Genes/enzymes/proteins | crtE / idsA1 / idsA2 (GGPP synthase-associated) |  | Supplies prenyl precursor for carotenoid synthesis; supports pigment accumulation | Upregulated early in BR-producing conditions; annotated in haloarchaeal pathway | (ma2024thebiosynthesismechanism pages 6-8, nagar2024genomicinsightson pages 5-6) |
| Genes/enzymes/proteins | blh / β-carotene 15,15'-dioxygenase |  | Converts β-carotene to retinal, potentially reducing flux to bacterioruberin | Retinal branch gene present in some haloarchaea; competing branch discussed in Ma 2024 | (ma2024thebiosynthesismechanism pages 6-8, strakova2024unveilingthegenomic pages 11-13) |
| Genes/enzymes/proteins | brp |  | Retinal/β-carotene-branch associated gene in haloarchaea; competitor to BR pathway | Downregulated when BR-favoring conditions are present | (ma2024thebiosynthesismechanism pages 6-8, nagar2024genomicinsightson pages 6-8) |
| Genes/enzymes/proteins | crtCBICDEF cluster |  | Bradyrhizobium PGC carotenoid gene set supporting pigmented phenotype | Genomic evidence for carotenoid synthesis genes in strain with pink colonies | (zhang2023geneticdiversityinto pages 9-10, zhang2023geneticdiversityinto pages 7-8) |
| Environmental/experimental factors | salinity | ENVO:01000368 | Core habitat/assay factor shaping haloarchaeal carotenoid accumulation and visible pink phenotype | Osmotic down-shock from standard salinity altered BR content per cell | (ma2024thebiosynthesismechanism pages 6-8, ma2024thebiosynthesismechanism pages 13-15) |
| Environmental/experimental factors | osmotic down-shock |  | Experimental decrease in salinity that increases BR productivity/content per cell | 14% salinity gave significantly increased BR per cell vs 20% | (ma2024thebiosynthesismechanism pages 6-8, ma2024thebiosynthesismechanism pages 13-15) |
| Environmental/experimental factors | glucose | CHEBI:17234 | Carbon source that increases BR productivity in Halorubrum sp. HRM-150 | 10 g/L glucose identified as favorable for BR production | (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) |
| Environmental/experimental factors | starch | CHEBI:28017 | Carbon source that, alone or with glucose, increases biomass/BR productivity | Glucose+starch diauxic growth increased biomass and BR productivity | (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) |
| Environmental/experimental factors | tryptone |  | Nitrogen source associated with improved BR production | 15 g/L tryptone identified as favorable in Ma 2024 | (ma2024thebiosynthesismechanism pages 1-2) |
| Environmental/experimental factors | logarithmic growth phase | GO:0072690 | Growth phase where BR synthesis is most active; key temporal determinant of visible pigmentation | BR synthesis described as growth-coupled and most active in log phase | (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) |
| Environmental/experimental factors | oxygen | CHEBI:15379 | Regulatory cue for crt operons and carotenoid output in purple bacteria; also affects pigment expression in phototrophs | Review notes oxygen regulation of crt operons; pigmentation phenotypes can change with O2 regime | (godoy2023asingularppaaaerrlike pages 5-9, sandmann2023genesandpathway pages 3-5) |
| Environmental/experimental factors | light | ENVO:01001148 | Regulatory cue for photosynthetic/pigment gene expression in phototrophs | Light-dependent pigment loss/gain phenotypes reported in phototrophic bacteria | (godoy2023asingularppaaaerrlike pages 5-9) |
| Cellular structures/functions | cell membrane | GO:0005886 | Bacterioruberin is a structural membrane component; membrane demand couples growth to pigmentation | Ma 2024 states BR acts as structural component of membranes and synthesis is growth-coupled | (ma2024thebiosynthesismechanism pages 1-2) |
| Cellular structures/functions | photosynthetic apparatus | GO:0009521 | Pigment-producing phototrophs often integrate carotenoids with photosystem assembly; loss of regulation can cause colorless phenotype | R. rubrum and purple-bacterial studies connect pigment formation with photosystem/PGC expression | (godoy2023asingularppaaaerrlike pages 5-9, sandmann2023genesandpathway pages 1-3) |
| Cellular structures/functions | proton-pumping rhodopsin / bacteriorhodopsin system | GO:0016036 | Retinal-consuming photoprotein branch can compete with BR biosynthesis and influence pigmentation balance | Haloarcula/Halobacterium discussion links bacteriorhodopsin-retinal branch with reduced BR accumulation | (nagar2024genomicinsightson pages 6-8, strakova2024unveilingthegenomic pages 11-13) |
| Cellular structures/functions | antioxidant activity | GO:0016209 | Functional consequence of pink carotenoids; often explains maintenance of pigmentation under stress | Bacterioruberin described as protective antioxidant pigment in haloarchaea | (strakova2024unveilingthegenomic pages 11-13) |


*Table: This table groups candidate causal-graph nodes for the microbial trait 'pink pigmented' across pigments, pathways, genes, environmental factors, and cellular functions. It emphasizes carotenoid-based mechanisms supported by haloarchaeal bacterioruberin and Bradyrhizobium crt/PGC evidence, while flagging prodigiosin as an important boundary-case alternative pigment system.*

### 7) Candidate causal edges (evidence-backed triples)
Edges below are proposed as subject–predicate–object statements suitable for TraitMech, including strength annotations and ontology grounding suggestions.

| Edge (S–P–O) | Strength | Mechanism notes | Reference (DOI + URL + pub date) | Evidence snippet (short quote) | Ontology grounding suggestions (CURIEs) |
|---|---|---|---|---|---|
| lyeJ — positively_regulates — bacterioruberin biosynthetic pathway | strong | Ma et al. identify **lyeJ** as the key haloarchaeal gene in the de novo bacterioruberin pathway; increased flux to bacterioruberin supports pink/red colony coloration where bacterioruberin is the dominant pigment. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “the de-novo pathway for BR synthesis with a key gene of lyeJ” (ma2024thebiosynthesismechanism pages 1-2) | lyeJ [label-only]; bacterioruberin [label-only]; carotenoid biosynthetic process GO:0016117 |
| bacterioruberin biosynthetic pathway — causally_underlies — pink pigmented phenotype | strong | In haloarchaea, bacterioruberin is the major visible C50 carotenoid; when dominant, it explains pink to pink-red pigmentation. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6, strakova2024unveilingthegenomic pages 11-13) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “contained ~85% BR” (ma2024thebiosynthesismechanism pages 1-2) | bacterioruberin [label-only]; METPO:1003027; carotenoid biosynthetic process GO:0016117 |
| osmotic down-shock — increases — bacterioruberin accumulation | strong | Lowering salinity during logarithmic phase increased BR per cell without sacrificing biomass, so salt perturbation is a direct environmental determinant of stronger pink coloration in haloarchaea. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 6-8, ma2024thebiosynthesismechanism pages 13-15) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “Osmotic down shock to 14% salinity significantly increased BR per cell” (ma2024thebiosynthesismechanism pages 6-8) | osmotic down-shock [label-only]; salinity ENVO:01000368; bacterioruberin [label-only] |
| 14% salinity treatment — increases — bacterioruberin content per cell | strong | Specific assay condition from Ma et al.; useful as an experimental-factor node rather than a universal biological rule. (ma2024thebiosynthesismechanism pages 6-8) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “peaking at 48 h with 4.83 × 10−10 µg/cell — a 48% increase versus 20% salinity” (ma2024thebiosynthesismechanism pages 6-8) | salinity ENVO:01000368; bacterioruberin [label-only] |
| glucose — increases — bacterioruberin productivity | strong | Carbon availability changes carotenoid output; glucose was one of the best substrates for BR production in Halorubrum sp. HRM-150. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “glucose (10 g/L) and tryptone (15 g/L) were tested to be better sources for BR production” (ma2024thebiosynthesismechanism pages 1-2) | glucose CHEBI:17234; bacterioruberin [label-only] |
| glucose_plus_starch — increases — bacterioruberin productivity | strong | Mixed carbon sources caused diauxic growth and higher BR productivity, making nutrient composition a causal experimental factor for visible pigmentation intensity. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “the biomass and BR productivity increased by 85% and 54% than using glucose” (ma2024thebiosynthesismechanism pages 1-2) | glucose CHEBI:17234; starch CHEBI:28017; bacterioruberin [label-only] |
| logarithmic growth phase — increases — bacterioruberin synthesis | strong | BR is growth-coupled and most actively synthesized during log phase; pigmentation therefore depends on growth state. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 2-6) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “BR synthesis is highly coupled with growth, which was most active in the logarithm phase” (ma2024thebiosynthesismechanism pages 1-2) | logarithmic growth phase GO:0072690; bacterioruberin [label-only] |
| lyeJ expression — positively_correlates_with — bacterioruberin accumulation | strong | Under osmotic down-shock, lyeJ expression tracks BR accumulation, supporting a causal gene-expression edge. (ma2024thebiosynthesismechanism pages 6-8) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “lyeJ expression mirrored BR accumulation” (ma2024thebiosynthesismechanism pages 6-8) | lyeJ [label-only]; bacterioruberin [label-only] |
| crtY/brp/blh retinal branch — competes_with — bacterioruberin biosynthetic pathway | strong | Ma et al. identify retinal as a competing sink for lycopene-derived precursors; lowering competitor-gene expression favors BR-linked pigmentation. (ma2024thebiosynthesismechanism pages 6-8, nagar2024genomicinsightson pages 6-8, strakova2024unveilingthegenomic pages 11-13) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “competition between retinal and BR for the common substrate lycopene” (ma2024thebiosynthesismechanism pages 6-8) | retinal CHEBI:17336; lycopene CHEBI:15948; blh [label-only]; crtY [label-only]; brp [label-only] |
| early downregulation of crtY/brp/blh — increases — flux to bacterioruberin | strong | Competing retinal-branch genes were downregulated when BR synthesis was favored, supporting a flux-competition edge. (ma2024thebiosynthesismechanism pages 6-8) | 10.1128/AEM.00540-24; https://doi.org/10.1128/aem.00540-24; Jul 2024 | “genes of a competing pathway (crtY, brp, blh) were downregulated at early stage” (ma2024thebiosynthesismechanism pages 6-8) | crtY [label-only]; brp [label-only]; blh [label-only]; bacterioruberin [label-only] |
| lycopene — precursor_of — bacterioruberin | strong | Haloarchaeal bacterioruberin biosynthesis proceeds from lycopene through LyeJ/CrtD/CruF-associated steps. (ma2024thebiosynthesismechanism pages 2-6, strakova2024unveilingthegenomic pages 11-13) | 10.3389/fmars.2024.1421769; https://doi.org/10.3389/fmars.2024.1421769; Oct 2024 | “CrtD, LyeJ and CruF, ‘responsible for the production of bacterioruberin from lycopene’” (strakova2024unveilingthegenomic pages 11-13) | lycopene CHEBI:15948; bacterioruberin [label-only]; CrtD [label-only]; LyeJ [label-only]; CruF [label-only] |
| CrtD/LyeJ/CruF — enable_conversion_of — lycopene_to_bacterioruberin | strong | Straková et al. provide a compact mechanistic statement grounding three pathway proteins to the lycopene→bacterioruberin branch. (strakova2024unveilingthegenomic pages 11-13) | 10.3389/fmars.2024.1421769; https://doi.org/10.3389/fmars.2024.1421769; Oct 2024 | “genomes encode CrtD, LyeJ and CruF, ‘responsible for the production of bacterioruberin from lycopene’” (strakova2024unveilingthegenomic pages 11-13) | CrtD [label-only]; LyeJ [label-only]; CruF [label-only]; lycopene CHEBI:15948; bacterioruberin [label-only] |
| blh — converts — β-carotene to retinal | strong | This branch can divert carotenoid intermediates away from bacterioruberin-associated pink pigmentation and toward rhodopsin physiology. (strakova2024unveilingthegenomic pages 11-13) | 10.3389/fmars.2024.1421769; https://doi.org/10.3389/fmars.2024.1421769; Oct 2024 | “blh, encoding β-carotene 15,15'-dioxygenase that converts β-carotene into retinal” (strakova2024unveilingthegenomic pages 11-13) | blh [label-only]; beta-carotene CHEBI:7382; retinal CHEBI:17336 |
| carotenoid biosynthesis genes in photosynthesis gene clusters — contribute_to — visible pigmentation | strong | Sandmann’s review generalizes that pigment phenotype in purple bacteria is caused by carotenoids plus bacteriochlorophylls, and that crt genes occur in PGCs. (sandmann2023genesandpathway pages 1-3, sandmann2023genesandpathway pages 3-5) | 10.3390/biology12101346; https://doi.org/10.3390/biology12101346; Oct 2023 | “The pigmentation of purple bacteria is caused by a combination of bacteriochlorophylls and carotenoids” (sandmann2023genesandpathway pages 1-3) | photosynthesis gene cluster [label-only]; carotenoid biosynthetic process GO:0016117 |
| crt genes — part_of — photosynthesis gene cluster | strong | Supports a reusable gene-cluster node for TraitMech; useful for phototrophic bacteria with pinkish carotenoid pigmentation. (sandmann2023genesandpathway pages 1-3) | 10.3390/biology12101346; https://doi.org/10.3390/biology12101346; Oct 2023 | “the genes of the carotenoid pathways are part of photosynthesis gene clusters” (sandmann2023genesandpathway pages 1-3) | crt genes [label-only]; photosynthesis gene cluster [label-only] |
| oxygen — upregulates — crtI-crtB operon | strong | Sandmann summarizes oxygen-responsive regulation of carotenoid genes, making oxygen a causal environmental regulator of pigment output. (sandmann2023genesandpathway pages 3-5) | 10.3390/biology12101346; https://doi.org/10.3390/biology12101346; Oct 2023 | “oxygen up-regulates the crtI-crtB operon” (sandmann2023genesandpathway pages 3-5) | oxygen CHEBI:15379; crtI [label-only]; crtB [label-only] |
| crtI/crtB expression — increases — colored carotenoid production | uncertain | Inference from Sandmann’s operon/regulatory summary; mechanism is strong at pathway level but not tied in the quoted text to a specific pink colony assay. (sandmann2023genesandpathway pages 3-5) | 10.3390/biology12101346; https://doi.org/10.3390/biology12101346; Oct 2023 | “mutations/deletions in crt genes lead to accumulation of pathway intermediates” (sandmann2023genesandpathway pages 3-5) | crtI [label-only]; crtB [label-only]; carotenoid biosynthetic process GO:0016117 |
| Bradyrhizobium crtCBICDEF-containing PGC — contributes_to — pink colonies | uncertain | Zhang et al. provide phenotype plus genomic evidence in the same strain, but not a direct experimental knockout/complementation link; curate as inferred/taxon-specific. (zhang2023geneticdiversityinto pages 9-10, zhang2023geneticdiversityinto pages 7-8, zhang2023geneticdiversityinto pages 8-9) | 10.3389/fmicb.2023.1295854; https://doi.org/10.3389/fmicb.2023.1295854; Nov 2023 | “Colonies grown on R2A agar are pink” and “carotenoid biosynthesis genes denoted as crtCBICDEF” (zhang2023geneticdiversityinto pages 9-10, zhang2023geneticdiversityinto pages 7-8) | NCBITaxon:Bradyrhizobium [label-only]; crtCBICDEF [label-only]; METPO:1003027 |
| Bradyrhizobium roseus pink colony phenotype — associated_with — carotenoid-synthesizing genes | uncertain | Good phenotype-genome association, but still not a direct causality experiment. (zhang2023geneticdiversityinto pages 9-10) | 10.3389/fmicb.2023.1295854; https://doi.org/10.3389/fmicb.2023.1295854; Nov 2023 | “Colonies grown on R2A agar are pink” and the genome “with carotenoids synthesizing genes” (zhang2023geneticdiversityinto pages 9-10) | METPO:1003027; carotenoid biosynthetic process GO:0016117 |
| prodigiosin — can_underlie — pink pigmented phenotype | uncertain | Important boundary case: Wang et al. explicitly call prodigiosin a pink pigment in Serratia, but this is a non-carotenoid tripyrrole mechanism and should not be merged with carotenoid edges without taxon-specific evidence. (wang2024hostsmanipulatelifestyle pages 1-5) | 10.1101/2024.02.14.580325; https://doi.org/10.1101/2024.02.14.580325; Jun 2024 | “Serratia marcescens … generates a pink pigment prodigiosin” (wang2024hostsmanipulatelifestyle pages 1-5) | prodigiosin [label-only]; NCBITaxon:615 [Serratia marcescens] |
| prodigiosin biosynthetic mechanism — distinct_from — carotenoid biosynthetic mechanism | strong | Boundary-case separation for ontology curation: prodigiosin is a different chemical class and should not automatically support carotenoid-based pink graph edges. (kumar2024isolationandcharacterization pages 18-22, guryanov2024bacterialpigmentprodigiosin pages 1-2) | 10.3390/applmicrobiol4040115; https://doi.org/10.3390/applmicrobiol4040115; Dec 2024 | “Prodigiosin … is specified as a tripyrrole” (guryanov2024bacterialpigmentprodigiosin pages 1-2) | prodigiosin [label-only]; carotenoid [label-only] |


*Table: This table lists candidate subject–predicate–object edges for curating the microbial 'pink pigmented' trait, emphasizing carotenoid-based mechanisms and key environmental modulators while flagging non-carotenoid boundary cases such as prodigiosin. It is useful for selecting high-confidence TraitMech nodes and for separating direct evidence from inferred or taxon-specific links.*

### 8) Expert synthesis / analysis (authoritative-source grounded)
1. **Pink pigmentation is a phenotype-level umbrella, not a single mechanism.** In haloarchaea, strong evidence supports bacterioruberin-driven pigmentation with measurable yields and defined genetic control (lyeJ; lyeJ/CrtD/CruF; retinal-branch competition). In contrast, in *Serratia* the “pink pigment” label refers to prodigiosin, a chemically distinct tripyrrole system. Curations should therefore attach **taxon-specific mechanistic subgraphs** under a shared phenotype node rather than merging pigments indiscriminately. (ma2024thebiosynthesismechanism pages 6-8, strakova2024unveilingthegenomic pages 11-13, wang2024hostsmanipulatelifestyle pages 1-5, guryanov2024bacterialpigmentprodigiosin pages 1-2)
2. **Environmental and process variables are legitimate causal nodes** for this trait, especially in industrial/bioprocess contexts: salinity shifts, carbon source composition, and growth phase directly change bacterioruberin yield per cell and productivity and therefore modulate observable pink intensity. (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 6-8, ma2024thebiosynthesismechanism pages 2-6)
3. **Photosynthesis gene-cluster coupling supports modular graph reuse.** In phototrophs, the embedding of crt genes within PGCs suggests curated nodes such as “photosynthesis gene cluster” and “crt operon” can generalize across taxa, with oxygen/light as key regulators. (sandmann2023genesandpathway pages 3-5, sandmann2023genesandpathway pages 1-3)

### 9) Warnings / curation cautions (do not over-curate)
- **Do not assume “pink” implies carotenoids.** Prodigiosin is explicitly called a pink pigment in *Serratia*, but it is not a carotenoid; keep prodigiosin edges separate unless the target organism is known to produce prodiginines. (wang2024hostsmanipulatelifestyle pages 1-5, guryanov2024bacterialpigmentprodigiosin pages 1-2)
- **Association vs causation in genome-only evidence.** The *Bradyrhizobium roseus* paper provides both *pink colony phenotype* and presence of **crt** genes, but does not show gene knockout/complementation linking crt genes to pink color; mark such edges **uncertain/inferred**. (zhang2023geneticdiversityinto pages 9-10, zhang2023geneticdiversityinto pages 7-8)
- **Gene presence ≠ expression.** Regulatory signals may be absent in laboratory conditions; treat “gene present → pigment produced” as conditional unless supported by expression/phenotype assays. (strakova2024unveilingthegenomic pages 11-13)

---

## DOI-first bibliography (with URLs and dates where available)

1. Ma Y, Sun Z, Yang H, et al. **The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis.** *Applied and Environmental Microbiology.* **Jul 2024.** DOI: **10.1128/aem.00540-24**. URL: https://doi.org/10.1128/aem.00540-24 (ma2024thebiosynthesismechanism pages 1-2, ma2024thebiosynthesismechanism pages 6-8, ma2024thebiosynthesismechanism pages 2-6)
2. Straková D, Sánchez-Porro C, de la Haba RR, Ventosa A. **Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus Halogeometricum: spotlight on thiamine biosynthesis.** *Frontiers in Marine Science.* **Oct 2024.** DOI: **10.3389/fmars.2024.1421769**. URL: https://doi.org/10.3389/fmars.2024.1421769 (strakova2024unveilingthegenomic pages 11-13)
3. Giani M, Pire C, Martínez-Espinosa RM. **Bacterioruberin: Biosynthesis, Antioxidant Activity, and Therapeutic Applications in Cancer and Immune Pathologies.** *Marine Drugs.* **Apr 2024.** DOI: **10.3390/md22040167**. URL: https://doi.org/10.3390/md22040167 (strakova2024unveilingthegenomic pages 11-13)
4. Sandmann G. **Genes and Pathway Reactions Related to Carotenoid Biosynthesis in Purple Bacteria.** *Biology.* **Oct 2023.** DOI: **10.3390/biology12101346**. URL: https://doi.org/10.3390/biology12101346 (sandmann2023genesandpathway pages 3-5, sandmann2023genesandpathway pages 1-3)
5. Zhang N, Jin C-Z, Zhuo Y, et al. **Genetic diversity into a novel free-living species of Bradyrhizobium from contaminated freshwater sediment.** *Frontiers in Microbiology.* **Nov 2023.** DOI: **10.3389/fmicb.2023.1295854**. URL: https://doi.org/10.3389/fmicb.2023.1295854 (zhang2023geneticdiversityinto pages 9-10, zhang2023geneticdiversityinto pages 7-8)
6. Wang Z, Li S, Zhang S, et al. **Hosts manipulate lifestyle switch and pathogenicity heterogeneity of opportunistic pathogens in the single-cell resolution.** *eLife* (preprint DOI). **Jun 2024.** DOI: **10.1101/2024.02.14.580325**. URL: https://doi.org/10.1101/2024.02.14.580325 (wang2024hostsmanipulatelifestyle pages 1-5)
7. Guryanov I, Naumenko E. **Bacterial Pigment Prodigiosin as Multifaceted Compound for Medical and Industrial Application.** *Applied Microbiology.* **Dec 2024.** DOI: **10.3390/applmicrobiol4040115**. URL: https://doi.org/10.3390/applmicrobiol4040115 (guryanov2024bacterialpigmentprodigiosin pages 1-2, guryanov2024bacterialpigmentprodigiosin pages 14-15)
8. de Oliveira Barreto JV, Casanova LM, Junior AN, et al. **Microbial Pigments: Major Groups and Industrial Applications.** *Microorganisms.* **Dec 2023.** DOI: **10.3390/microorganisms11122920**. URL: https://doi.org/10.3390/microorganisms11122920 (barreto2023microbialpigmentsmajor pages 4-6, barreto2023microbialpigmentsmajor pages 6-8)

### Visual evidence
- De novo bacterioruberin pathway and transcriptional expression overlay (Figure extraction). (ma2024thebiosynthesismechanism media 27651990, ma2024thebiosynthesismechanism media 848c505f, ma2024thebiosynthesismechanism media 1f0d76f2)


References

1. (ma2024thebiosynthesismechanism pages 2-6): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

2. (strakova2024unveilingthegenomic pages 11-13): Dáša Straková, Cristina Sánchez-Porro, Rafael R. de la Haba, and Antonio Ventosa. Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus halogeometricum: spotlight on thiamine biosynthesis. Frontiers in Marine Science, Oct 2024. URL: https://doi.org/10.3389/fmars.2024.1421769, doi:10.3389/fmars.2024.1421769. This article has 6 citations.

3. (sandmann2023genesandpathway pages 1-3): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 15 citations.

4. (wang2024hostsmanipulatelifestyle pages 1-5): Ziguang Wang, Shuai Li, Sheng Zhang, Tianyu Zhang, Yujie Wu, Anqi Liu, Kui Wang, Xiaowen Ji, Haiqun Cao, Yinglao Zhang, Eng-King Tan, Yongcheng Wang, Yirong Wang, and Wei Liu. Hosts manipulate lifestyle switch and pathogenicity heterogeneity of opportunistic pathogens in the single-cell resolution. eLife, Jun 2024. URL: https://doi.org/10.1101/2024.02.14.580325, doi:10.1101/2024.02.14.580325. This article has 15 citations and is from a domain leading peer-reviewed journal.

5. (guryanov2024bacterialpigmentprodigiosin pages 1-2): Ivan Guryanov and Ekaterina Naumenko. Bacterial pigment prodigiosin as multifaceted compound for medical and industrial application. Applied Microbiology, Dec 2024. URL: https://doi.org/10.3390/applmicrobiol4040115, doi:10.3390/applmicrobiol4040115. This article has 19 citations.

6. (godoy2023asingularppaaaerrlike pages 5-9): Manuel S. Godoy, Santiago R. de Miguel, and M. Auxiliadora Prieto. A singular ppaa/aerr-like protein in <i>rhodospirillum rubrum</i> rules beyond the boundaries of photosynthesis in response to the intracellular redox state. Dec 2023. URL: https://doi.org/10.1128/msystems.00702-23, doi:10.1128/msystems.00702-23. This article has 7 citations and is from a peer-reviewed journal.

7. (ma2024thebiosynthesismechanism pages 6-8): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

8. (sandmann2023genesandpathway pages 3-5): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 15 citations.

9. (barreto2023microbialpigmentsmajor pages 4-6): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

10. (zhang2023geneticdiversityinto pages 9-10): Naxue Zhang, Chun-Zhi Jin, Ye Zhuo, Taihua Li, Feng-Jie Jin, Hyung-Gwan Lee, and Long Jin. Genetic diversity into a novel free-living species of bradyrhizobium from contaminated freshwater sediment. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1295854, doi:10.3389/fmicb.2023.1295854. This article has 21 citations and is from a peer-reviewed journal.

11. (zhang2023geneticdiversityinto pages 7-8): Naxue Zhang, Chun-Zhi Jin, Ye Zhuo, Taihua Li, Feng-Jie Jin, Hyung-Gwan Lee, and Long Jin. Genetic diversity into a novel free-living species of bradyrhizobium from contaminated freshwater sediment. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1295854, doi:10.3389/fmicb.2023.1295854. This article has 21 citations and is from a peer-reviewed journal.

12. (ma2024thebiosynthesismechanism pages 1-2): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

13. (ma2024thebiosynthesismechanism media 27651990): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

14. (ma2024thebiosynthesismechanism media 848c505f): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

15. (ma2024thebiosynthesismechanism media 1f0d76f2): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

16. (nagar2024genomicinsightson pages 5-6): DN Nagar, K Mani, and JM Braganca. Genomic insights on carotenoid synthesis by extremely halophilic archaea haloarcula rubripromontorii bs2, haloferax lucentense bbk2 and halogeometricum …. Unknown journal, 2024.

17. (sandmann2023genesandpathway pages 12-14): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 15 citations.

18. (guryanov2024bacterialpigmentprodigiosin pages 14-15): Ivan Guryanov and Ekaterina Naumenko. Bacterial pigment prodigiosin as multifaceted compound for medical and industrial application. Applied Microbiology, Dec 2024. URL: https://doi.org/10.3390/applmicrobiol4040115, doi:10.3390/applmicrobiol4040115. This article has 19 citations.

19. (zhang2023geneticdiversityinto pages 8-9): Naxue Zhang, Chun-Zhi Jin, Ye Zhuo, Taihua Li, Feng-Jie Jin, Hyung-Gwan Lee, and Long Jin. Genetic diversity into a novel free-living species of bradyrhizobium from contaminated freshwater sediment. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1295854, doi:10.3389/fmicb.2023.1295854. This article has 21 citations and is from a peer-reviewed journal.

20. (nagar2024genomicinsightson pages 6-8): DN Nagar, K Mani, and JM Braganca. Genomic insights on carotenoid synthesis by extremely halophilic archaea haloarcula rubripromontorii bs2, haloferax lucentense bbk2 and halogeometricum …. Unknown journal, 2024.

21. (kumar2024isolationandcharacterization pages 18-22): A Kumar and AK Nadda. Isolation and characterization of a prodigiosin pigment producing bacterial straing from himalayan region. Unknown journal, 2024.

22. (nery2023quantummechanicaleffects pages 46-49): ET Nery. Quantum mechanical effects in the light-harvesting complexes of genetically engineered purple non-sulfur bacteria. Unknown journal, 2023.

23. (ma2024thebiosynthesismechanism pages 13-15): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

24. (barreto2023microbialpigmentsmajor pages 6-8): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.