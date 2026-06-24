---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:21:12.364011'
end_time: '2026-06-18T06:40:55.841695'
duration_seconds: 1183.48
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: black pigmented
  trait_identifier: METPO:1003022
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: black_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    black or very dark due to accumulation of dark pigments such as melanins.
  parent_traits: METPO:1003021
  synonyms: Pigment_black
  evidence_summary: 'DOI:10.1016/j.biotechadv.2021.107773: dark-colored pigment (Supports
    black/dark microbial pigmentation as a melanin-associated color phenotype.)'
  causal_graph_summary: 'black_pigmented_melanin_polymer: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** black pigmented
- **METPO identifier:** METPO:1003022
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear black or very dark due to accumulation of dark pigments such as melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_black
- **Existing evidence:** DOI:10.1016/j.biotechadv.2021.107773: dark-colored pigment (Supports black/dark microbial pigmentation as a melanin-associated color phenotype.)
- **Existing causal graph summary:** black_pigmented_melanin_polymer: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **black pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/black_pigmented.yaml`.

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
- **Trait label:** black pigmented
- **METPO identifier:** METPO:1003022
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear black or very dark due to accumulation of dark pigments such as melanins.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_black
- **Existing evidence:** DOI:10.1016/j.biotechadv.2021.107773: dark-colored pigment (Supports black/dark microbial pigmentation as a melanin-associated color phenotype.)
- **Existing causal graph summary:** black_pigmented_melanin_polymer: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **black pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/black_pigmented.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **black pigmented** (METPO:1003022)

### Executive scope summary
The trait **black pigmented** (METPO:1003022) is best curated as an **assay-observed morphology phenotype** in which microbial colonies, cells, or secreted products appear **black, very dark brown, or form dark halos** due to accumulation of **melanin-family polymers**. Mechanistically, the dominant causes are: (i) **DOPA/eumelanin-type melanins** produced from L-tyrosine/L-DOPA by **tyrosinase and/or laccase** (dark brown to black pigments) (munoztorres2024exploringtheagricultural pages 2-4, suthar2023theenigmaticworld pages 4-6, kordjazi2024streptomycetesasmicrobial pages 3-4); (ii) **DHN/allomelanin** produced via a **polyketide synthase (PKS) → THN → DHN → oxidative polymerization** route (munoztorres2024exploringtheagricultural pages 2-4, suthar2023theenigmaticworld pages 2-4); and (iii) **pyomelanin**, produced when **homogentisic acid (HGA)** accumulates (often due to loss of **HmgA**) and then auto-oxidizes/polymerizes (moustafa2024mutationofhmga pages 2-4, pavan2020melaninbiosynthesisin pages 3-4). In engineered systems, recombinant tyrosinase expression can yield **“dark black coloration”** in bacterial cellulose materials, showing the phenotype can be implemented beyond colony assays into real products (walker2025selfpigmentingtextilesgrown pages 1-2).

### 1) Trait scope (curation-relevant definition, boundary cases, and assays)
**What the trait represents.**
*Black pigmented* should be interpreted as a **visible dark pigmentation phenotype** at the level of colony/cell/supernatant/material, typically melanin-associated. In Streptomyces, melanization is frequently scored as **dark brown melanin halos** around colonies when the melanogenesis operon is present/expressed (zhu2005expressionofthe pages 1-2). In production/bioprocess studies, pigmentation can be quantified in **cell-free supernatant** by absorbance (e.g., OD480 for pigment in Burkholderia pyomelanin work (moustafa2024mutationofhmga pages 2-4); OD430 for pyomelanin proxy assays tied to HPPD activity (thiourmauprivez2023assessingtheeffects pages 5-8)).

**Boundary cases and “nearby traits.”**
1. **Dark brown vs black:** many sources describe melanins as *brown/dark brown* rather than pure black (e.g., Streptomyces produce “dark brown eumelanin” (kordjazi2024streptomycetesasmicrobial pages 3-4); pyomelanin can be “dark brown” (elzawawy2024bioproductionandoptimization pages 1-2)). For METPO:1003022, these should still be treated as within-scope if the phenotype is clearly “very dark” and melanin-associated.
2. **Non-melanin dark pigments:** some microbes produce dark pigments that are not melanins (e.g., quinones, phenazines). These should be treated as **out-of-scope unless the source explicitly attributes the phenotype to melanin/pyomelanin/DHN melanin or the pathway is demonstrated**.
3. **Medium artifacts / iron sulfide / biofilm matrix darkening:** dark color due to chemical precipitation or matrix effects should not be curated unless mechanistically linked to pigment biosynthesis.

**Practical assay readouts to curate.**
- **Colony phenotype:** “dark brown haloes of melanin around colonies” (melC operon marker) (zhu2005expressionofthe pages 1-2).
- **Supernatant absorbance:** OD480 pigment (Burkholderia; pyomelanin context) (moustafa2024mutationofhmga pages 2-4); OD430 normalized readout in whole-cell pyomelanin/HPPD assay (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 8-11).
- **Chemical confirmation:** UV–Vis/FT-IR/NMR/EPR used to confirm eumelanin-like or pyomelanin identity in bioprocess studies (restaino2024biotechnologicalproductionand pages 1-2, elzawawy2024bioproductionandoptimization pages 1-2).

### 2) Key concepts & current mechanistic understanding (2023–2024 prioritized)
#### 2.1 DOPA/eumelanin pathway (tyrosinase/laccase-driven)
Microbial DOPA-melanin is produced when tyrosine (or L-DOPA) is oxidized to **dopaquinone**, which proceeds through intermediates (e.g., dopachrome, dihydroxyindoles) that **polymerize into DOPA-melanins** (munoztorres2024exploringtheagricultural pages 2-4, suthar2023theenigmaticworld pages 4-6). In Streptomyces-focused synthesis descriptions, tyrosinase converts L-tyrosine to L-DOPA and then oxidizes to DOPA-quinone; downstream intermediates (DHICA/DHI) polymerize to eumelanin (kordjazi2024streptomycetesasmicrobial pages 3-4). Tyrosinase and laccase are **copper-dependent** enzymes (“require bound copper ions”) (suthar2023theenigmaticworld pages 4-6).

Key concept for curation: the trait “black pigmented” is often the downstream consequence of (enzyme activity) → (reactive quinone intermediates) → (polymerization) rather than a single gene product.

#### 2.2 DHN/allomelanin pathway (PKS-driven)
A major alternative melanin class is **DHN-melanin** (often called allomelanin in fungi). In the summary of microbial melanin biosynthesis, a **PKS** uses acetyl-CoA/malonyl-CoA to form **1,3,6,8-tetrahydroxynaphthalene (THN)**, followed by reduction/dehydration steps to **1,8-dihydroxynaphthalene (DHN)**; polymerization of DHN yields melanin (munoztorres2024exploringtheagricultural pages 2-4). Laccases can catalyze steps in DHN conversion/polymerization (munoztorres2024exploringtheagricultural pages 2-4).

#### 2.3 Pyomelanin pathway (tyrosine catabolism / homogentisate)
Pyomelanin is a **HGA-derived melanin-like pigment** produced when the tyrosine catabolic pathway accumulates **homogentisic acid (HGA)**, which is then oxidized/polymerized.

A clear mechanistic chain is described in Burkholderia cenocepacia: HppD converts 4-hydroxyphenylpyruvate to HGA; HmgA converts HGA to maleylacetoacetate; if HmgA is nonfunctional, the pathway stops at HGA, which is excreted and auto-oxidizes to benzoquinoneacetic acid, then self-polymerizes to pyomelanin (moustafa2024mutationofhmga pages 2-4). This is a direct gene-to-phenotype causal link suitable for curation.

### 3) Recent developments and latest research (2023–2024 emphasis)
#### 3.1 Bioprocess optimization and quantitative production yields
- **Streptomyces nashvillensis extracellular eumelanin-like pigment:** optimal conditions 28 °C and pH 7.0 yielded **0.74 ± 0.01 g/L melanin** and tyrosinase activity **10.1 ± 0.1 U/mL** (restaino2024biotechnologicalproductionand pages 1-2). This supports edges linking pH/temperature to pigment production for streptomycete systems.
- **Fungal production yields and process factors:** fungal production can reach multi-g/L and higher values depending on organism and fermentation time. Reported yields include **2.97 g/L** (Auricularia auricula), **5.60 g/L** (Hortaea werneckii), up to **20.76 g/L** (Aspergillus carbonicus), and **27.98 g/L** (Armillaria cepistipes) (the latter with long fermentation) (qin2024melanininfungi pages 4-5). This provides recent “statistics” for expected ranges of melanin production and informs what production nodes to consider in graph curation.
- **Pyomelanin characterization and functional statistics:** a Streptomyces djakartensis extracellular pigment was characterized as nitrogen-free pyomelanin, with **in vitro SPF = 18.5**, antioxidant **IC50 = 18.03 µg/mL**, and antimicrobial **MICs** (e.g., **6.25 µg/mL** against one MDR strain; **25 µg/mL** against another) (elzawawy2024bioproductionandoptimization pages 1-2). These are directly usable application metrics for “real-world implementation” nodes.

#### 3.2 Environmental chemicals inhibiting pigment formation (HPPD inhibition)
A 2023 environmental microbiology study developed a **96-well whole-cell colorimetric assay** to monitor **HPPD activity via pyomelanin production**, quantifying pigment as OD430 (thiourmauprivez2023assessingtheeffects pages 5-8). It reports OD430N values across strains (e.g., P. fluorescens F113 OD430N = 1.43 ± 0.11) and herbicide-dependent inhibition trends (thiourmauprivez2023assessingtheeffects pages 8-11). This supports curating chemical-inhibition edges (β-triketone herbicides → decreased HPPD activity proxy → reduced pyomelanin signal), but these should be marked assay-proxy/uncertain for direct “melanin decreased” unless chemically confirmed.

#### 3.3 Engineered living materials: black pigmentation in bacterial cellulose (published online 2024)
A Nature Biotechnology paper (published online 2 Apr 2024) demonstrates a concrete implementation: engineering **Komagataeibacter rhaeticus** with recombinant tyrosinase enables melanin formation that produces **“dark black coloration robust to material use”** in bacterial cellulose pellicles, and the process can be scaled to prototype fashion products (walker2025selfpigmentingtextilesgrown pages 1-2). They also show pigmentation is pH-sensitive (melanin synthesis readily above pH 7) and requires separating pellicle growth (acidifying) from melanin development in a buffered, tyrosine + CuSO4 solution (walker2025selfpigmentingtextilesgrown pages 1-2). This is an authoritative demonstration connecting genes, environmental conditions, and a visible black phenotype in a real product.

### 4) Candidate nodes for `black_pigmented.yaml` (grouped by type)
A curated node set should include three melanin route subgraphs (DOPA/eumelanin; DHN; pyomelanin) plus shared regulators/assays.

| Node label | Type | Suggested grounding CURIE(s) | Grounding confidence | Notes |
|---|---|---|---|---|
| black pigmented | Phenotype | METPO:1003022 | high | Trait phenotype: microbial colonies/cells appear black or very dark, commonly melanin-associated; boundary cases include dark brown rather than strictly black pigmentation (restaino2024biotechnologicalproductionand pages 1-2, elzawawy2024bioproductionandoptimization pages 1-2, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| dark brown melanin halo around colony | Phenotype | unresolved | low | Common assay-visible manifestation in Streptomyces melC systems; useful phenotype synonym/boundary case rather than separate ontology-grounded trait (zhu2005expressionofthe pages 1-2) |
| DOPA-melanin / eumelanin biosynthetic pathway | Pathways/processes | unresolved | low | Tyrosine/L-DOPA-derived route through dopaquinone, dopachrome, DHI/DHICA to dark pigment; no explicit pathway identifier in sources (munoztorres2024exploringtheagricultural pages 2-4, suthar2023theenigmaticworld pages 4-6, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| DHN-melanin / allomelanin biosynthetic pathway | Pathways/processes | unresolved | low | PKS-dependent pathway via THN and DHN to melanin; strongly supported mechanistically, but no explicit stable pathway CURIE in provided evidence (munoztorres2024exploringtheagricultural pages 2-4, suthar2023theenigmaticworld pages 2-4) |
| pyomelanin biosynthetic pathway | Pathways/processes | unresolved | low | Tyrosine catabolism branch via HppD/HGA, with HmgA loss causing HGA accumulation and polymerization to pyomelanin (moustafa2024mutationofhmga pages 2-4, pavan2020melaninbiosynthesisin pages 3-4) |
| melanin biosynthetic process | Pathways/processes | unresolved | low | Broad process node useful for causal graph, but no explicit GO term provided in sources (qin2024melanininfungi pages 4-5, qin2024melanininfungi pages 15-15) |
| oxidative polymerization of melanin precursors | Pathways/processes | unresolved | low | Shared chemistry across DOPA- and pyomelanin formation; may be represented as process node if needed (munoztorres2024exploringtheagricultural pages 2-4, moustafa2024mutationofhmga pages 2-4) |
| tyrosinase | Genes/proteins/enzymes | EC:1.14.18.1 | high | Explicit EC given in Zhu 2005; copper-containing monooxygenase central to DOPA-melanin formation (zhu2005expressionofthe pages 1-2) |
| MelC2 tyrosinase | Genes/proteins/enzymes | EC:1.14.18.1 | medium | Streptomyces melC operon product; extracellular tyrosinase driving melanin phenotype in melC+ strains (zhu2005expressionofthe pages 1-2, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| MelC1 | Genes/proteins/enzymes | unresolved | low | Chaperone/helper for MelC2 secretion and copper incorporation; no explicit EC or stable identifier in sources (zhu2005expressionofthe pages 1-2, munoztorres2024exploringtheagricultural pages 2-4) |
| melC operon | Genes/proteins/enzymes | unresolved | low | Bicistronic melanogenesis operon used as phenotype marker in Streptomyces; represented at locus/operon level (zhu2005expressionofthe pages 1-2) |
| laccase | Genes/proteins/enzymes | unresolved | low | Copper-dependent phenol oxidase involved in DOPA and DHN routes; no explicit EC in provided sources (suthar2023theenigmaticworld pages 4-6, munoztorres2024exploringtheagricultural pages 2-4) |
| polyketide synthase | Genes/proteins/enzymes | unresolved | low | DHN-melanin pathway enzyme family; type III PKS specifically noted for bacterial DHN pathway (munoztorres2024exploringtheagricultural pages 2-4) |
| type III polyketide synthase | Genes/proteins/enzymes | unresolved | low | Sequential condensation of malonyl-CoA units to form THN in bacterial DHN pathway; no explicit EC in sources (munoztorres2024exploringtheagricultural pages 2-4) |
| HppD / 4-hydroxyphenylpyruvate dioxygenase | Genes/proteins/enzymes | unresolved | low | Converts 4-hydroxyphenylpyruvate to HGA in pyomelanin pathway; no EC explicitly stated in provided texts (moustafa2024mutationofhmga pages 2-4, pavan2020melaninbiosynthesisin pages 3-4) |
| HmgA / homogentisate 1,2-dioxygenase | Genes/proteins/enzymes | unresolved | low | Converts HGA to maleylacetoacetate; loss-of-function causes pyomelanin accumulation (moustafa2024mutationofhmga pages 2-4, pavan2020melaninbiosynthesisin pages 3-4) |
| apotyrosinase | Genes/proteins/enzymes | unresolved | low | Inactive precursor secreted/activated by MelC1 in Streptomyces systems (zhu2005expressionofthe pages 1-2, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| L-tyrosine | Metabolites/chemicals | unresolved | low | Substrate for DOPA-melanin route and inducer/supplement increasing melanin production in several systems (qin2024melanininfungi pages 4-5, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| L-DOPA | Metabolites/chemicals | unresolved | low | Immediate tyrosinase product and DOPA-melanin precursor (restaino2024biotechnologicalproductionand pages 1-2, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| dopaquinone | Metabolites/chemicals | unresolved | low | Reactive intermediate in DOPA-melanin route (munoztorres2024exploringtheagricultural pages 2-4, suthar2023theenigmaticworld pages 4-6) |
| dopachrome | Metabolites/chemicals | unresolved | low | Intermediate downstream of dopaquinone in eumelanin synthesis (munoztorres2024exploringtheagricultural pages 2-4, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| 5,6-dihydroxyindole (DHI) | Metabolites/chemicals | unresolved | low | Eumelanin monomer precursor named explicitly in Streptomyces/microbial melanin reviews (restaino2024biotechnologicalproductionand pages 1-2, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| 5,6-dihydroxyindole-2-carboxylic acid (DHICA) | Metabolites/chemicals | unresolved | low | Eumelanin monomer precursor named explicitly (restaino2024biotechnologicalproductionand pages 1-2, suthar2023theenigmaticworld pages 4-6, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| malonyl-CoA | Metabolites/chemicals | unresolved | low | Precursor for DHN-melanin via PKS condensation (munoztorres2024exploringtheagricultural pages 2-4, restaino2024biotechnologicalproductionand pages 1-2) |
| 1,3,6,8-tetrahydroxynaphthalene (THN) | Metabolites/chemicals | unresolved | low | PKS-derived DHN-pathway intermediate (munoztorres2024exploringtheagricultural pages 2-4) |
| 1,8-dihydroxynaphthalene (DHN) | Metabolites/chemicals | unresolved | low | Immediate monomeric precursor for DHN-melanin/allomelanin (munoztorres2024exploringtheagricultural pages 2-4, restaino2024biotechnologicalproductionand pages 1-2) |
| homogentisic acid (HGA) | Metabolites/chemicals | unresolved | low | Central pyomelanin precursor; accumulates when HmgA is impaired (moustafa2024mutationofhmga pages 2-4, moustafa2024mutationofhmga pages 1-2) |
| maleylacetoacetate | Metabolites/chemicals | unresolved | low | Product of HmgA-catalyzed step in tyrosine catabolism (moustafa2024mutationofhmga pages 2-4) |
| benzoquinoneacetic acid | Metabolites/chemicals | unresolved | low | Auto-oxidation product of excreted HGA before pyomelanin polymerization (moustafa2024mutationofhmga pages 2-4) |
| copper ion | Metabolites/chemicals | unresolved | low | Required cofactor for tyrosinase/laccase activity and medium component affecting melanization (qin2024melanininfungi pages 4-5, suthar2023theenigmaticworld pages 4-6, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| glutathione | Metabolites/chemicals | unresolved | low | Presence diverts DOPA intermediates toward pheomelanin-like route rather than eumelanin; useful boundary-case chemistry (kordjazi2024streptomycetesasmicrobial pages 3-4) |
| cysteine | Metabolites/chemicals | unresolved | low | Presence diverts DOPA intermediates toward pheomelanin-like route rather than eumelanin (restaino2024biotechnologicalproductionand pages 1-2, kordjazi2024streptomycetesasmicrobial pages 3-4) |
| pH 7.0 | Environmental/assay factors | unresolved | low | Optimal condition for extracellular melanin production by S. nashvillensis in one study; cultivation-specific factor (restaino2024biotechnologicalproductionand pages 1-2) |
| 28 °C | Environmental/assay factors | unresolved | low | Optimal temperature for extracellular melanin production by S. nashvillensis in one study (restaino2024biotechnologicalproductionand pages 1-2) |
| neutral to slightly acidic pH | Environmental/assay factors | unresolved | low | Broad fungal fermentation preference for melanin production (qin2024melanininfungi pages 4-5) |
| dark environment | Environmental/assay factors | unresolved | low | Reported to improve fungal dry weight and melanin production (qin2024melanininfungi pages 4-5) |
| proper ventilation | Environmental/assay factors | unresolved | low | Reported to improve fungal melanin production (qin2024melanininfungi pages 4-5) |
| L-tyrosine supplementation | Environmental/assay factors | unresolved | low | Increases melanin production in multiple taxa/culture systems; may be modeled as experimental factor (qin2024melanininfungi pages 4-5, suthar2023theenigmaticworld pages 4-6) |
| CuSO4 supplementation | Environmental/assay factors | unresolved | low | Improves tyrosinase activity at tested concentrations; excess can precipitate melanin (qin2024melanininfungi pages 4-5) |
| OD430 pyomelanin assay | Environmental/assay factors | unresolved | low | Spectrophotometric proxy for pyomelanin/HPPD activity in whole-cell assay; assay/readout node, not mechanism node (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 8-11) |
| OD480 pigment assay | Environmental/assay factors | unresolved | low | Used to quantify pigment production in B. cenocepacia pyomelanin study; assay/readout node (moustafa2024mutationofhmga pages 2-4) |
| kojic acid | Inhibitors | unresolved | low | Tyrosinase inhibitor that chelates Cu2+ at active site and decreases DOPA-melanin formation (suthar2023theenigmaticworld pages 4-6) |
| azelaic acid | Inhibitors | unresolved | low | Tyrosinase inhibitor reducing DOPA-melanin formation (suthar2023theenigmaticworld pages 4-6) |
| β-triketone herbicides | Inhibitors | unresolved | low | Inhibit bacterial HPPD activity in strain-dependent manner, reducing pyomelanin readout in OD430 assay (thiourmauprivez2023assessingtheeffects pages 1-5, thiourmauprivez2023assessingtheeffects pages 8-11) |
| sulcotrione | Inhibitors | unresolved | low | Specific β-triketone HPPD inhibitor tested in whole-cell pyomelanin assay (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 8-11) |
| mesotrione | Inhibitors | unresolved | low | Specific β-triketone HPPD inhibitor tested in whole-cell pyomelanin assay (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 1-5) |
| tembotrione | Inhibitors | unresolved | low | Specific β-triketone HPPD inhibitor tested in whole-cell pyomelanin assay (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 1-5) |


*Table: This table lists candidate nodes for a melanin-centered causal graph of the microbial 'black pigmented' trait, grouped by biological type. It emphasizes conservative grounding: only tyrosinase receives an explicit EC CURIE from the cited evidence, while other nodes are left unresolved for later ontology curation.*

### 5) Evidence-backed candidate causal edges (triples) for TraitMech
The following table (artifact-00) lists candidate edges with direct evidence snippets, notes on taxon/assay specificity, and DOI/URL metadata.

| Edge (triple) | Evidence (short quote/snippet) | Notes/uncertainty | Source (first author year, DOI, URL) | Pub date |
|---|---|---|---|---|
| tyrosinase — catalyzes conversion of — L-tyrosine to L-DOPA | “Tyrosinase first catalyzes the hydroxylation of L-tyrosine to 3,4-dihydroxy-L-phenylalanine (L-DOPA)” (kordjazi2024streptomycetesasmicrobial pages 3-4) | Strong mechanistic edge for DOPA/eumelanin-producing taxa; not universal for pyomelanin/DHN routes. | Kordjazi 2024, 10.3390/ijms25053013, https://doi.org/10.3390/ijms25053013 | 2024-03 |
| tyrosinase — catalyzes oxidation of — L-DOPA to dopaquinone | “If tyrosine is the substrate, it is transformed to L-Dopa and then to dopaquinone. The enzyme tyrosinase catalyzes both steps.” (munoztorres2024exploringtheagricultural pages 2-4) | Strong mechanistic edge; central to DOPA-melanin pathway. | Muñoz-Torres 2024, 10.3390/microorganisms12071352, https://doi.org/10.3390/microorganisms12071352 | 2024-07 |
| dopaquinone / dihydroxyindole intermediates — polymerize into — DOPA-melanin (eumelanin) | “Dopaquinone… oxidized into dopachrome… dihydroxy-indoles, which can polymerize to form DOPA-melanins.” (suthar2023theenigmaticworld pages 4-6) | Strong pathway edge; phenotype contribution is typically dark brown to black. | Suthar 2023, 10.3390/jof9090891, https://doi.org/10.3390/jof9090891 | 2023-08 |
| copper ion — required cofactor for — tyrosinase activity | “Tyrosinases are copper-dependent enzymes” (munoztorres2024exploringtheagricultural pages 2-4) | Strong enzymology edge across many bacterial/fungal tyrosinases. | Muñoz-Torres 2024, 10.3390/microorganisms12071352, https://doi.org/10.3390/microorganisms12071352 | 2024-07 |
| CuSO4 supplementation — increases — tyrosinase activity | “gradual addition of CuSO4 in the concentration range of 0.01–0.2 g/L improves tyrosinase activity” (qin2024melanininfungi pages 4-5) | Strong but cultivation-specific; higher Cu can precipitate melanin. | Qin 2024, 10.1186/s12934-024-02614-8, https://doi.org/10.1186/s12934-024-02614-8 | 2024-12 |
| excess copper ions — causes — melanin precipitation | “once the limit is exceeded, excessive metal ions can cause melanin precipitation” (qin2024melanininfungi pages 4-5) | Process/assay-specific cultivation effect; not a universal biological regulation edge. | Qin 2024, 10.1186/s12934-024-02614-8, https://doi.org/10.1186/s12934-024-02614-8 | 2024-12 |
| melC1 — promotes secretion of — apotyrosinase/MelC2 | “The MelC1 protein… promotes secretion of apotyrosinase via a transient MelC1-MelC2 complex” (zhu2005expressionofthe pages 1-2) | Strong for Streptomyces melC systems; taxon-specific. | Zhu 2005, 10.1128/JB.187.9.3180-3187.2005, https://doi.org/10.1128/JB.187.9.3180-3187.2005 | 2005-05 |
| melC1 — promotes copper incorporation into — MelC2 tyrosinase | “The MelC1 protein… regulates copper incorporation” (zhu2005expressionofthe pages 1-2) | Strong for Streptomyces melC systems; taxon-specific. | Zhu 2005, 10.1128/JB.187.9.3180-3187.2005, https://doi.org/10.1128/JB.187.9.3180-3187.2005 | 2005-05 |
| melC operon expression — enables — dark brown melanin halo phenotype | “Dark brown haloes of melanin around colonies are an easily visualized phenotype displayed by many Streptomyces strains harboring plasmid pIJ702 carrying the melC operon” (zhu2005expressionofthe pages 1-2) | Strong phenotype edge, but plasmid/host-context dependent. | Zhu 2005, 10.1128/JB.187.9.3180-3187.2005, https://doi.org/10.1128/JB.187.9.3180-3187.2005 | 2005-05 |
| polyketide synthase (PKS) — synthesizes precursor for — DHN-melanin pathway | “the activity of the polyketide synthase enzyme… forms 1,3,6,8-tetrahydroxynaphthalene (THN)… The polymerization of DHN leads to the formation of melanin” (munoztorres2024exploringtheagricultural pages 2-4) | Strong for fungal/bacterial DHN routes; pathway distinct from DOPA route. | Muñoz-Torres 2024, 10.3390/microorganisms12071352, https://doi.org/10.3390/microorganisms12071352 | 2024-07 |
| laccase — oxidizes/polymerizes — DHN to melanin | “DHN, which is finally converted to melanin in a reaction catalyzed by laccases” (munoztorres2024exploringtheagricultural pages 2-4) | Strong for DHN/allomelanin; taxon/pathway specific. | Muñoz-Torres 2024, 10.3390/microorganisms12071352, https://doi.org/10.3390/microorganisms12071352 | 2024-07 |
| HppD — converts — 4-hydroxyphenylpyruvate to homogentisic acid (HGA) | “hppD gene codes for a protein that is responsible for the conversion of 4-hydroxyphenylpyruvate to HGA” (moustafa2024mutationofhmga pages 2-4) | Strong pyomelanin-pathway edge. | Moustafa 2024, 10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | 2024-07 |
| HmgA — converts — HGA to maleylacetoacetate | “Homogentisate 1,2-dioxygenase, encoded by the hmgA gene, converts HGA to maleylacetoacetate” (moustafa2024mutationofhmga pages 2-4) | Strong pyomelanin-pathway edge. | Moustafa 2024, 10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | 2024-07 |
| loss of HmgA function — causes accumulation of — HGA | “The G378R change renders HmgA non-functional, and the pathway stops at the intermediate molecule HGA” (moustafa2024mutationofhmga pages 2-4) | Strong causal edge for pyomelanin in this Burkholderia model; likely generalizable to other pyomelanogenic bacteria but still taxon-context dependent. | Moustafa 2024, 10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | 2024-07 |
| accumulated HGA — auto-oxidizes/polymerizes into — pyomelanin | “HGA is excreted and spontaneously auto-oxidizes to form benzoquinoneacetic acid, followed by self-polymerization to produce pyomelanin” (moustafa2024mutationofhmga pages 2-4) | Strong pyomelanin chemistry edge. | Moustafa 2024, 10.1128/spectrum.00410-24, https://doi.org/10.1128/spectrum.00410-24 | 2024-07 |
| pyomelanin — contributes to — black/dark pigmented phenotype | “Only one isolate, ACT3, produced a dark brown melanin pigment extracellularly… characterized as belonging to nitrogen-free pyomelanin” (elzawawy2024bioproductionandoptimization pages 1-2) | Strong phenotype association for this isolate; color described as dark brown rather than black. | El-Zawawy 2024, 10.1186/s12934-023-02276-y, https://doi.org/10.1186/s12934-023-02276-y | 2024-01 |
| L-tyrosine supplementation — increases — melanin production | “The addition of L-tyrosine has significantly increased the melanin production of A. auricula and the yeast Y. lipolytica W29” (qin2024melanininfungi pages 4-5) | Strong cultivation edge but strain-specific magnitude. | Qin 2024, 10.1186/s12934-024-02614-8, https://doi.org/10.1186/s12934-024-02614-8 | 2024-12 |
| neutral/slightly acidic pH — favors — fungal melanin fermentation | “Fungal fermentation mainly requires a neutral or slightly acidic environment” (qin2024melanininfungi pages 4-5) | Broad cultivation trend; exact optimum is strain-specific. | Qin 2024, 10.1186/s12934-024-02614-8, https://doi.org/10.1186/s12934-024-02614-8 | 2024-12 |
| dark environment and ventilation — improve — fungal melanin production | “A total dark environment and proper ventilation can improve dry weight and melanin production in fungi” (qin2024melanininfungi pages 4-5) | Cultivation-specific and fungal-focused. | Qin 2024, 10.1186/s12934-024-02614-8, https://doi.org/10.1186/s12934-024-02614-8 | 2024-12 |
| pH 7.0 and 28 °C — increase — extracellular melanin production in Streptomyces nashvillensis | “the optimal growth parameters resulted to be 28 °C and pH 7.0, at which… a melanin concentration of 0.74 ± 0.01 g/L” (restaino2024biotechnologicalproductionand pages 1-2) | Strong but species- and assay-specific cultivation edge. | Restaino 2024, 10.3390/microorganisms12020297, https://doi.org/10.3390/microorganisms12020297 | 2024-01 |
| fungal tyrosinase inhibitors (kojic acid, azelaic acid) — decrease — DOPA-melanin production | “kojic acid… prevents the formation of… DHICA… Similarly, azelaic acid also inhibits the action of tyrosinase… effectively decreasing the formation of DOPA-melanin” (suthar2023theenigmaticworld pages 4-6) | Mechanistically strong, but inhibitor-based and assay-specific rather than native regulation. | Suthar 2023, 10.3390/jof9090891, https://doi.org/10.3390/jof9090891 | 2023-08 |
| β-triketone herbicides — inhibit — HPPD activity | “all three β-triketones inhibited HPPD in Bacillus cereus ATCC14579 and Shewanella oneidensis MR-1” (thiourmauprivez2023assessingtheeffects pages 1-5) | Strong for tested strains; herbicide sensitivity is strain-dependent. | Thiour-Mauprivez 2023, 10.1007/s11356-022-22801-7, https://doi.org/10.1007/s11356-022-22801-7 | 2023-09 |
| HPPD inhibition by herbicides — reduces — pyomelanin readout (OD430) | “After 48 hours of incubation, OD430… were measured… Pyomelanin detection was measured at OD430” and several strains showed “≥31% reduction at 1× RfD and ≥74% at 10× RfD” (thiourmauprivez2023assessingtheeffects pages 5-8, thiourmauprivez2023assessingtheeffects pages 8-11) | Assay-specific proxy edge; useful for curation but should be marked uncertain because OD430 is a readout, not direct structural confirmation. | Thiour-Mauprivez 2023, 10.1007/s11356-022-22801-7, https://doi.org/10.1007/s11356-022-22801-7 | 2023-09 |
| recombinant Tyr1 tyrosinase expression — causes — dark black coloration in bacterial cellulose | “Melanin biosynthesis in the bacteria from recombinant tyrosinase expression achieves dark black coloration robust to material use” (walker2025selfpigmentingtextilesgrown pages 1-2) | Strong engineered-system edge; directly relevant to phenotype but synthetic biology context. | Walker 2025, 10.1038/s41587-024-02194-3, https://doi.org/10.1038/s41587-024-02194-3 | 2025-04 |
| melanin development buffer (pH 7.4 + L-tyrosine + CuSO4) — enables — eumelanin production by Tyr1-engineered K. rhaeticus | “PBS, buffered to pH 7.4, containing 0.5 g l−1 l-tyrosine and 10 μM CuSO4” was used to “drive melanin synthesis” (walker2025selfpigmentingtextilesgrown pages 1-2) | Strong engineered-process edge; assay/implementation specific. | Walker 2025, 10.1038/s41587-024-02194-3, https://doi.org/10.1038/s41587-024-02194-3 | 2025-04 |
| low culture pH during growth — suppresses — Tyr1-dependent pigmentation in K. rhaeticus | “Melanin synthesis by Tyr1 is sensitive to pH—only occurring readily at pH values above 7… culture pH had lowered to below pH 4… displayed no pigmentation during growth” (walker2025selfpigmentingtextilesgrown pages 1-2) | Strong but engineered-host specific. | Walker 2025, 10.1038/s41587-024-02194-3, https://doi.org/10.1038/s41587-024-02194-3 | 2025-04 |


*Table: This table lists evidence-backed candidate causal edges for melanin-associated black or dark microbial pigmentation, emphasizing pathways, genes, enzymes, and environmental factors useful for TraitMech curation. It highlights which edges are strong versus assay- or taxon-specific so curators can prioritize robust graph components.*

### 6) Current applications and real-world implementations
1. **Textiles / biomaterials (engineered living materials):** melanin-based self-pigmentation in bacterial cellulose enables “dark black coloration” and scaling to prototype fashion products (walker2025selfpigmentingtextilesgrown pages 1-2). This is a direct real-world implementation of the trait.
2. **Cosmetic/photoprotective materials:** Streptomyces-derived pyomelanin showed sunscreen-relevant in vitro SPF = 18.5 (elzawawy2024bioproductionandoptimization pages 1-2) and microbial melanins are discussed as UV-light absorbent materials for sunscreen creams and UV-protective packaging (restaino2024biotechnologicalproductionand pages 1-2).
3. **Environmental remediation:** melanins are described as useful for filtering systems for water decontamination from heavy metals and toxins (restaino2024biotechnologicalproductionand pages 1-2). In fungal melanin review contexts, melanin is discussed in relation to extraction/purification for scalable biomaterial production (qin2024melanininfungi pages 4-5).

### 7) Expert opinions / authoritative synthesis (from reviews)
- Reviews emphasize that microbial melanins’ **UV–visible absorption, metal-chelation, redox/antioxidant properties** drive applications across industries (restaino2024biotechnologicalproductionand pages 1-2, elzawawy2024bioproductionandoptimization pages 1-2).
- A 2024 fungal melanin review stresses that industrial-scale production depends on **fermentation optimization (pH, temperature, humidity, light/dark, ventilation), precursors (tyrosine), and cofactors (CuSO4)** and that excessive metal can precipitate pigment (qin2024melanininfungi pages 4-5). This directly supports modeling **environmental and process variables as causal graph parents** of pigment production.

### 8) Key quantitative statistics/data points (recent)
- **Streptomyces nashvillensis extracellular melanin:** 0.74 ± 0.01 g/L at 28 °C, pH 7.0 (restaino2024biotechnologicalproductionand pages 1-2).
- **Fungal yields reported in 2024 review:** 2.97 g/L (A. auricula), 5.60 g/L (H. werneckii), 20.76 g/L (A. carbonicus), 27.98 g/L (A. cepistipes; long fermentation) (qin2024melanininfungi pages 4-5).
- **Pyomelanin bioactivity stats:** SPF 18.5; MIC 6.25–25 µg/mL (selected strains); antioxidant IC50 18.03 µg/mL (elzawawy2024bioproductionandoptimization pages 1-2).
- **Environmental assay stats for pyomelanin/HPPD proxy:** OD430N values across strains and herbicide-dependent inhibition magnitudes (thiourmauprivez2023assessingtheeffects pages 8-11, thiourmauprivez2023assessingtheeffects pages 5-8).

### 9) Curation warnings (do-not-curate-yet / uncertain edges)
1. **OD-based pigment proxies:** Edges that equate OD430/OD480 changes directly to melanin quantity should be labeled **assay-dependent** unless corroborated by chemical characterization (e.g., FT-IR/NMR) (thiourmauprivez2023assessingtheeffects pages 5-8, moustafa2024mutationofhmga pages 2-4).
2. **Cross-taxon generalization:** melC1/melC2 secretion/copper-chaperone edges are **Streptomyces-specific** and should not be generalized to all bacteria with tyrosinase genes (zhu2005expressionofthe pages 1-2).
3. **“Black pigmented” ≠ “melanin” in all microbes:** Only curate edges to melanin pathways when the source explicitly ties the pigment to melanin/pyomelanin/DHN melanin or demonstrates pathway genetics/chemistry (elzawawy2024bioproductionandoptimization pages 1-2, moustafa2024mutationofhmga pages 2-4).
4. **Industrial yield comparisons:** Very high yields in reviews may be contingent on long fermentations or specific substrates; these should be captured as **contextual notes**, not universal expectations (qin2024melanininfungi pages 4-5).

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Walker KT, Li IS, Keane J, et al. *Self-pigmenting textiles grown from cellulose-producing bacteria with engineered tyrosinase expression.* **Nature Biotechnology**. Published online **2024-04-02** (journal issue March 2025). DOI: **10.1038/s41587-024-02194-3**. https://doi.org/10.1038/s41587-024-02194-3 (walker2025selfpigmentingtextilesgrown pages 1-2)
2. Qin Y, Xia Y. *Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering.* **Microbial Cell Factories**. **2024-12**. DOI: **10.1186/s12934-024-02614-8**. https://doi.org/10.1186/s12934-024-02614-8 (qin2024melanininfungi pages 4-5)
3. Restaino OF, Manini P, Kordjazi T, et al. *Biotechnological Production and Characterization of Extracellular Melanin by Streptomyces nashvillensis.* **Microorganisms**. **2024-01-30** (published). DOI: **10.3390/microorganisms12020297**. https://doi.org/10.3390/microorganisms12020297 (restaino2024biotechnologicalproductionand pages 1-2)
4. Muñoz-Torres P, Cárdenas-Ninasivincha S, Aguilar Y. *Exploring the Agricultural Applications of Microbial Melanin.* **Microorganisms**. **2024-07**. DOI: **10.3390/microorganisms12071352**. https://doi.org/10.3390/microorganisms12071352 (munoztorres2024exploringtheagricultural pages 2-4)
5. El-Zawawy NA, Kenawy E-R, Ahmed S, El-Sapagh S. *Bioproduction and optimization of newly characterized melanin pigment from Streptomyces djakartensis NSS-3 with its anticancer, antimicrobial, and radioprotective properties.* **Microbial Cell Factories**. **2024-01**. DOI: **10.1186/s12934-023-02276-y**. https://doi.org/10.1186/s12934-023-02276-y (elzawawy2024bioproductionandoptimization pages 1-2)
6. Moustafa DA, Wu L, Ivey M, et al. *Mutation of hmgA, encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production…* **Microbiology Spectrum**. **2024-07**. DOI: **10.1128/spectrum.00410-24**. https://doi.org/10.1128/spectrum.00410-24 (moustafa2024mutationofhmga pages 2-4)
7. Thiour-Mauprivez C, Dayan FE, Terol H, et al. *Assessing the effects of β-triketone herbicides on HPPD from environmental bacteria…* **Environmental Science and Pollution Research**. **2023-09**. DOI: **10.1007/s11356-022-22801-7**. https://doi.org/10.1007/s11356-022-22801-7 (thiourmauprivez2023assessingtheeffects pages 5-8)
8. Suthar M, Dufossé L, Singh SK. *The Enigmatic World of Fungal Melanin: A Comprehensive Review.* **Journal of Fungi**. **2023-08**. DOI: **10.3390/jof9090891**. https://doi.org/10.3390/jof9090891 (suthar2023theenigmaticworld pages 4-6)
9. Zhu D, He X, Zhou X, Deng Z. *Expression of the melC Operon in Several Streptomyces Strains Is Positively Regulated by AdpA…* **Journal of Bacteriology**. **2005-05**. DOI: **10.1128/JB.187.9.3180-3187.2005**. https://doi.org/10.1128/JB.187.9.3180-3187.2005 (zhu2005expressionofthe pages 1-2)



References

1. (munoztorres2024exploringtheagricultural pages 2-4): Patricio Muñoz-Torres, Steffany Cárdenas-Ninasivincha, and Yola Aguilar. Exploring the agricultural applications of microbial melanin. Microorganisms, 12:1352, Jul 2024. URL: https://doi.org/10.3390/microorganisms12071352, doi:10.3390/microorganisms12071352. This article has 25 citations.

2. (suthar2023theenigmaticworld pages 4-6): Malika Suthar, Laurent Dufossé, and Sanjay K. Singh. The enigmatic world of fungal melanin: a comprehensive review. Journal of Fungi, 9:891, Aug 2023. URL: https://doi.org/10.3390/jof9090891, doi:10.3390/jof9090891. This article has 95 citations.

3. (kordjazi2024streptomycetesasmicrobial pages 3-4): Talayeh Kordjazi, Loredana Mariniello, Concetta Valeria Lucia Giosafatto, Raffaele Porta, and Odile Francesca Restaino. Streptomycetes as microbial cell factories for the biotechnological production of melanin. International Journal of Molecular Sciences, 25:3013, Mar 2024. URL: https://doi.org/10.3390/ijms25053013, doi:10.3390/ijms25053013. This article has 30 citations.

4. (suthar2023theenigmaticworld pages 2-4): Malika Suthar, Laurent Dufossé, and Sanjay K. Singh. The enigmatic world of fungal melanin: a comprehensive review. Journal of Fungi, 9:891, Aug 2023. URL: https://doi.org/10.3390/jof9090891, doi:10.3390/jof9090891. This article has 95 citations.

5. (moustafa2024mutationofhmga pages 2-4): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

6. (pavan2020melaninbiosynthesisin pages 3-4): María Elisa Pavan, Nancy I. López, and M. Julia Pettinari. Melanin biosynthesis in bacteria, regulation and production perspectives. Applied Microbiology and Biotechnology, 104:1357-1370, Dec 2020. URL: https://doi.org/10.1007/s00253-019-10245-y, doi:10.1007/s00253-019-10245-y. This article has 199 citations and is from a domain leading peer-reviewed journal.

7. (walker2025selfpigmentingtextilesgrown pages 1-2): Kenneth T. Walker, Ivy S. Li, Jennifer Keane, Vivianne J. Goosens, Wenzhe Song, Koon-Yang Lee, and Tom Ellis. Self-pigmenting textiles grown from cellulose-producing bacteria with engineered tyrosinase expression. Nature Biotechnology, 43:345-354, Apr 2025. URL: https://doi.org/10.1038/s41587-024-02194-3, doi:10.1038/s41587-024-02194-3. This article has 72 citations and is from a highest quality peer-reviewed journal.

8. (zhu2005expressionofthe pages 1-2): Dongqing Zhu, Xinyi He, Xiufen Zhou, and Zixin Deng. Expression of the melc operon in several streptomyces strains is positively regulated by adpa, an arac family transcriptional regulator involved in morphological development in streptomyces coelicolor. Journal of Bacteriology, 187:3180-3187, May 2005. URL: https://doi.org/10.1128/jb.187.9.3180-3187.2005, doi:10.1128/jb.187.9.3180-3187.2005. This article has 40 citations and is from a peer-reviewed journal.

9. (thiourmauprivez2023assessingtheeffects pages 5-8): Clémence Thiour-Mauprivez, Franck Emmanuel Dayan, Hugo Terol, Marion Devers, Christophe Calvayrac, Fabrice Martin-Laurent, and Lise Barthelmebs. Assessing the effects of β-triketone herbicides on hppd from environmental bacteria using a combination of in silico and microbiological approaches. Environmental Science and Pollution Research, 30:9932-9944, Sep 2023. URL: https://doi.org/10.1007/s11356-022-22801-7, doi:10.1007/s11356-022-22801-7. This article has 5 citations and is from a peer-reviewed journal.

10. (elzawawy2024bioproductionandoptimization pages 1-2): Nessma A. El-Zawawy, El-Refaie Kenawy, Sara Ahmed, and Shimaa El-Sapagh. Bioproduction and optimization of newly characterized melanin pigment from streptomyces djakartensis nss-3 with its anticancer, antimicrobial, and radioprotective properties. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02276-y, doi:10.1186/s12934-023-02276-y. This article has 47 citations and is from a peer-reviewed journal.

11. (thiourmauprivez2023assessingtheeffects pages 8-11): Clémence Thiour-Mauprivez, Franck Emmanuel Dayan, Hugo Terol, Marion Devers, Christophe Calvayrac, Fabrice Martin-Laurent, and Lise Barthelmebs. Assessing the effects of β-triketone herbicides on hppd from environmental bacteria using a combination of in silico and microbiological approaches. Environmental Science and Pollution Research, 30:9932-9944, Sep 2023. URL: https://doi.org/10.1007/s11356-022-22801-7, doi:10.1007/s11356-022-22801-7. This article has 5 citations and is from a peer-reviewed journal.

12. (restaino2024biotechnologicalproductionand pages 1-2): Odile Francesca Restaino, Paola Manini, Talayeh Kordjazi, Maria Laura Alfieri, Massimo Rippa, Loredana Mariniello, and Raffaele Porta. Biotechnological production and characterization of extracellular melanin by streptomyces nashvillensis. Microorganisms, 12:297, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020297, doi:10.3390/microorganisms12020297. This article has 24 citations.

13. (qin2024melanininfungi pages 4-5): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 54 citations and is from a peer-reviewed journal.

14. (qin2024melanininfungi pages 15-15): Yanping Qin and Yuxian Xia. Melanin in fungi: advances in structure, biosynthesis, regulation, and metabolic engineering. Microbial Cell Factories, Dec 2024. URL: https://doi.org/10.1186/s12934-024-02614-8, doi:10.1186/s12934-024-02614-8. This article has 54 citations and is from a peer-reviewed journal.

15. (moustafa2024mutationofhmga pages 1-2): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

16. (thiourmauprivez2023assessingtheeffects pages 1-5): Clémence Thiour-Mauprivez, Franck Emmanuel Dayan, Hugo Terol, Marion Devers, Christophe Calvayrac, Fabrice Martin-Laurent, and Lise Barthelmebs. Assessing the effects of β-triketone herbicides on hppd from environmental bacteria using a combination of in silico and microbiological approaches. Environmental Science and Pollution Research, 30:9932-9944, Sep 2023. URL: https://doi.org/10.1007/s11356-022-22801-7, doi:10.1007/s11356-022-22801-7. This article has 5 citations and is from a peer-reviewed journal.