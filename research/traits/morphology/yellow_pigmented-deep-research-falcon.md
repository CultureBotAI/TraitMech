---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:24:49.086053'
end_time: '2026-06-18T10:47:04.222281'
duration_seconds: 1335.14
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: yellow pigmented
  trait_identifier: METPO:1003030
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: yellow_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    yellow due to production of yellow pigments such as carotenoids.
  parent_traits: METPO:1003021
  synonyms: Pigment_yellow
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow
    pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated
    bacterial color phenotype.)'
  causal_graph_summary: 'yellow_pigmented_carotenoid_color: 5 nodes, 4 edges'
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
- **Trait label:** yellow pigmented
- **METPO identifier:** METPO:1003030
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear yellow due to production of yellow pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_yellow
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated bacterial color phenotype.)
- **Existing causal graph summary:** yellow_pigmented_carotenoid_color: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **yellow pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/yellow_pigmented.yaml`.

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
- **Trait label:** yellow pigmented
- **METPO identifier:** METPO:1003030
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear yellow due to production of yellow pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_yellow
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated bacterial color phenotype.)
- **Existing causal graph summary:** yellow_pigmented_carotenoid_color: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **yellow pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/yellow_pigmented.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **yellow pigmented** (METPO:1003030)

### Executive scope summary (TraitMech curation)
**Trait label:** yellow pigmented (METPO:1003030; MORPHOLOGY; CLASS). The trait represents an **assay-observed colony/cell appearance** where colonies or cells are visibly yellow, typically because the organism accumulates **yellow chromophores** (most often carotenoids/xanthophylls, but also membrane-associated aryl polyenes such as **xanthomonadin**, or **flexirubin-type** pigments; in some cases yellow flavins such as **riboflavin** may contribute). The trait is **phenotypic and context-dependent**: visible hue can shift with **pH**, **light/heat/low pH stability**, pigment oxidation/aging, extraction/assay conditions, and pigment class (yellow vs orange vs red carotenoids). (liu2024multiomicsdissectionof pages 11-12, anshi2024unveilingtheintricacies pages 2-4, jimenez2024estudoinvitro pages 54-60)

**Key boundary cases / “nearby traits”**:
- **Orange/red pigmented** phenotypes: many carotenoids span yellow→orange→red; engineering toward astaxanthin (red) or lycopene (red) is mechanistically related but should be curated as distinct pigments/hues unless the observed phenotype is yellow. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)
- **Non-yellow pigments**: e.g., violacein (violet) and prodigiosin (red) are common bacterial pigments and should not be conflated with yellow. (huang2024bacterialpigmentsas pages 6-8)
- **Assay artifacts / misclassification**: aryl polyenes, xanthomonadins, flexirubins, and carotenoids can appear similar by eye; chemical tests (e.g., KOH for flexirubin) and spectral/chemical profiling may be required for confident mechanism assignment. (jimenez2024estudoinvitroa pages 54-60, jimenez2024estudoinvitro pages 54-60, jimenez2024estudoinvitro pages 92-96)

---

## 1) Key concepts and current understanding (definitions)

### 1.1 “Yellow pigmented” as a morphology phenotype
Yellow pigmentation is primarily a **visible-color outcome** from the presence of one or more pigment families rather than a single biosynthetic pathway. Major pigment families that can yield yellow colonies/cells in microbes include:

1) **Carotenoids / xanthophylls** (isoprenoids): derived from IPP/DMAPP, proceeding via GGPP and lycopene to various carotenoids; **β-carotene** is a canonical yellow/orange carotenoid and is explicitly discussed as a food colorant and provitamin A precursor. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, huang2024bacterialpigmentsas pages 6-8)

2) **Xanthomonadin / aryl polyenes (APE/APEL)**: **membrane-associated yellow aryl polyenes** produced by Xanthomonas and related taxa. In Xanthomonas, colonies are described as yellow because of **membrane-bound xanthomonadin**, which is protective against photobiological damage. (dey2024aninsightinto pages 1-2, jimenez2024estudoinvitroa pages 96-99)

3) **Flexirubin-type pigments**: common in some Bacteroidota (e.g., Flavobacterium spp.), where colonies can be **yellow or orange depending on pH**. Flexirubin is described as a yellow pigment protecting against reactive oxygen species (ROS). (liu2024multiomicsdissectionof pages 11-12)

4) **Flavins (riboflavin; vitamin B2)**: riboflavin is a yellow pigment used industrially; review tables include **Bacillus subtilis riboflavin** production values. (anshi2024unveilingtheintricacies pages 4-5, anshi2024unveilingtheintricacies pages 2-4)

### 1.2 Diagnostic/interpretation notes for curators (boundary-setting)
- **pH-dependent hue**: flexirubin-type pigmentation can shift between yellow and orange at different pH values; thus “yellow pigmented” should be curated with the assay/environment explicitly recorded when possible. (liu2024multiomicsdissectionof pages 11-12)
- **Stability to light/heat/low pH**: review literature notes microbial pigments have limitations/sensitivity to light, heat and acidic pH, which can alter observed coloration. (anshi2024unveilingtheintricacies pages 2-4)
- **Chemical discrimination**: UV–Vis band shape and chemical reactivity (e.g., KOH test) can help distinguish pigment classes; aryl polyenes may show broad bands (often ~415–460 nm) whereas carotenoids often show sharper peaks; aggressive saponification/alkali can alter carotenoid chromophores. (jimenez2024estudoinvitroa pages 54-60, jimenez2024estudoinvitro pages 54-60)

---

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Carotenoids as major, engineerable yellow pigment chemistry
**Mechanistic state-of-the-art** (2024): Carotenoid synthesis is described as beginning from **IPP and DMAPP**, proceeding to **GGPP**, then **lycopene**, and cyclization to **β-carotene** via **crtY**; oxygenation to keto-/hydroxy-carotenoids uses **crtZ** and **crtW**, and glycosylation can be enabled by **crtX**. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, gottl2024enhancingastaxanthinbiosynthesis media f31745ca)

**Engineering + quantitative outputs (real-world implementation evidence):** In an engineered *Corynebacterium glutamicum* platform, β-carotene (yellow/orange) and downstream carotenoids are increased by precursor and terminal-pathway tuning, including idi/idsA and crt genes. The study reports **β-carotene 18 mg g−1 CDW** (cellular titer) and a fed-batch **astaxanthin 103 mg L−1** with **1.5 mg L−1 h−1** productivity; glycosylated carotenoids (e.g., astaxanthin-β-D-diglucoside) are also produced. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, gottl2024enhancingastaxanthinbiosynthesis pages 8-9)

**Toolbox and strain engineering (2024):** CRISPR/MAD7 engineering in *C. glutamicum* targets carotenoid branching and regulation (e.g., knocking out crtEb and crtR; screening crtE/crtB/crtI/idsA/idi and a membrane protein cg0722), enabling high lycopene accumulation (not yellow but mechanistically proximal). (zhan2024expandingthecrispr pages 1-2, zhan2024expandingthecrispr pages 12-14)

### 2.2 Xanthomonadin/aryl polyene yellow membrane pigments (Xanthomonas)
A 2024 review of Xanthomonas pathogenicity notes: **“Xanthomonas colonies are morphologically yellow due to membrane-bound xanthomonadin pigment”** and that this pigment **protects from photobiological damage**. (dey2024aninsightinto pages 1-2)

Additional mechanistic synthesis in 2024 pigment-focused work summarizes the **biochemical origin** and **enzymology** of xanthomonadin: derived from **3-hydroxybenzoic acid** and assembled via an **ATP-dependent 3-hydroxybenzoic acid:ACP ligase** and an **unusual type II PKS pathway**, encoded in APE/xan gene clusters; xanthomonadins are described as **yellow, membrane-associated aryl polyenes** and functionally related to antioxidative pigments. (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 96-99)

### 2.3 Flexirubin-type pigments (Bacteroidota; plant-associated context)
A 2024 *Nature Communications* study on rapeseed endophytes describes a Flavobacterium isolate C2 as **flexirubin-type pigment-producing**, **yellow or orange depending on pH**, and states that flexirubin **protects against ROS damage**. It further notes that polyene chains in the chromophore are synthesized from **acetates** in a manner similar to **fatty acid biosynthesis**, suggesting a mechanistic connection to acetyl-unit elongation and lipid metabolism. (liu2024multiomicsdissectionof pages 11-12)

---

## 3) Current applications and real-world implementations

### 3.1 Industrial/biotech production of yellow pigments and related carotenoids
- **Food-grade pigments and supplements:** β-carotene is described as a food colorant and nutritional supplement; microbial fermentation is discussed as advantageous compared with plant extraction for carotene production in terms of feasibility/cost/quality (review-level). (huang2024bacterialpigmentsas pages 6-8)
- **Quantitative examples (2024 review table):** riboflavin production by *Bacillus subtilis* on corn steep liquor is reported as **26.8 mg/L**, demonstrating a microbial route to a yellow flavin pigment. (anshi2024unveilingtheintricacies pages 4-5)
- **Engineered microbial carotenoid platforms:** *C. glutamicum* carotenoid engineering demonstrates scalable titers and product diversification (e.g., glycosylated carotenoids). (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)

### 3.2 Ecological/functional applications
- **Photoprotection in plant-pathogenic bacteria:** xanthomonadin contributes to survival on leaf surfaces by protecting against photobiological damage (interpretable as UV/light stress tolerance). (dey2024aninsightinto pages 1-2)
- **Plant symbiosis and oxidative stress tolerance:** flexirubin-associated ROS protection is proposed to aid symbiosis/colonization in a plant-associated Flavobacterium. (liu2024multiomicsdissectionof pages 11-12)

---

## 4) Expert opinions and authoritative synthesis (2023–2024)

- **Pigment stability constraints and environmental sensitivity:** 2024 review literature emphasizes that microbial pigments are attractive industrial alternatives yet can be limited by exposure to **light, heat, and acidic pH**, which is important for interpreting and standardizing the “yellow pigmented” phenotype across assays. (anshi2024unveilingtheintricacies pages 2-4)
- **Analytical consensus for pigment identification:** a 2024 bacterial pigment review highlights the use of **HPLC, Raman spectroscopy, and MS** for pigment identification/quantification, consistent with curation needs when a colony-color phenotype must be grounded to a pigment chemistry. (huang2024bacterialpigmentsas pages 6-8)

---

## 5) Recent statistics and data (2023–2024)

### 5.1 Quantitative pigment production (selected recent examples)
- *C. glutamicum* engineered: β-carotene **18 mg g−1 CDW**; astaxanthin **103 mg L−1** in fed-batch; productivity **1.5 mg L−1 h−1**; glycosylated astaxanthin derivative **39 mg L−1**. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, gottl2024enhancingastaxanthinbiosynthesis pages 8-9)
- *Bacillus subtilis* riboflavin: **26.8 mg/L** (reviewed compilation). (anshi2024unveilingtheintricacies pages 4-5)

### 5.2 Market/application statistics (contextual, not for mechanistic graph)
A 2024 review compiles market estimates: organic pigments market projected to reach **$8.4B by 2031** and reports an estimate that chemical synthesis remains dominant (**~80–90%** of overall pigment synthesis). These provide application context but are not direct TraitMech causal edges. (anshi2024unveilingtheintricacies pages 2-4)

---

## Candidate nodes for `yellow_pigmented.yaml` (grouped)

### A) Pigments / metabolites
- **β-carotene** (CHEBI:17579) (huang2024bacterialpigmentsas pages 6-8, gottl2024enhancingastaxanthinbiosynthesis pages 1-3)
- **Lycopene** (CHEBI:15948) (proximal, red; useful intermediate node) (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, zhan2024expandingthecrispr pages 1-2)
- **Astaxanthin** (CHEBI:26966) (red; downstream of pathway; keep as boundary) (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)
- **Xanthomonadin** (label-only; aryl polyene pigment class) (dey2024aninsightinto pages 1-2, jimenez2024estudoinvitroa pages 96-99)
- **Aryl polyene pigments (APE/APEL)** (label-only) (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitroa pages 87-92)
- **Flexirubin-type pigments** (label-only) (liu2024multiomicsdissectionof pages 11-12)
- **Riboflavin (vitamin B2)** (CHEBI:17015) (anshi2024unveilingtheintricacies pages 4-5)
- **3-hydroxybenzoic acid** (CHEBI:30746) (xanthomonadin precursor node) (jimenez2024estudoinvitroa pages 96-99)

### B) Genes / enzymes (carotenoids)
- **idi** (isopentenyl diphosphate isomerase; EC 5.3.3.2 candidate) (gottl2024enhancingastaxanthinbiosynthesis pages 3-3, zhan2024expandingthecrispr pages 1-2)
- **idsA / crtE** (GGPP synthase) (gottl2024enhancingastaxanthinbiosynthesis pages 3-3, zhan2024expandingthecrispr pages 1-2)
- **crtB** (phytoene synthase) (zhan2024expandingthecrispr pages 1-2)
- **crtI** (phytoene desaturase) (zhan2024expandingthecrispr pages 1-2)
- **crtY** (lycopene β-cyclase) (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, gottl2024enhancingastaxanthinbiosynthesis media f31745ca)
- **crtZ** (β-carotene hydroxylase) (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)
- **crtW** (β-carotene ketolase) (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)
- **crtX** (carotenoid glycosyltransferase) (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)

### C) Genes / enzymes (xanthomonadin/aryl polyenes)
- **APE/PIG/xan biosynthetic gene cluster** (label-only cluster node) (jimenez2024estudoinvitroa pages 87-92, jimenez2024estudoinvitroa pages 96-99)
- **ATP-dependent 3-hydroxybenzoic acid:ACP ligase** (label-only) (jimenez2024estudoinvitroa pages 96-99)
- **Type II polyketide synthase machinery** (label-only) (jimenez2024estudoinvitroa pages 96-99)

### D) Environmental / experimental factors
- **pH** (ENVO:00002006 or label-only; affects flexirubin hue) (liu2024multiomicsdissectionof pages 11-12)
- **Light/heat/acidic pH** as stability modifiers (label-only) (anshi2024unveilingtheintricacies pages 2-4)

### E) Processes / functions
- **Response to photobiological damage / photoprotection** (label-only; map to GO stress response terms as appropriate) (dey2024aninsightinto pages 1-2)
- **Response to reactive oxygen species** (GO:0000302 candidate) (liu2024multiomicsdissectionof pages 11-12)

---

## Candidate causal edges (evidence-backed triples)
The table below is designed for direct curation into the TraitMech causal graph, with grounding suggestions, evidence snippets, and confidence notes.

| Edge (S-P-O) | Node type(s) | Suggested ontology grounding | Evidence snippet (short quote) | Reference (DOI + year + URL) | Confidence/notes |
|---|---|---|---|---|---|
| IPP/DMAPP - precursor_of - GGPP | metabolites to metabolite | CHEBI:53467 isopentenyl diphosphate; CHEBI:17211 dimethylallyl diphosphate; label: geranylgeranyl diphosphate | "Carotenoid synthesis begins from the C5 isoprenoid precursors IPP and DMAPP, which are converted via chain elongation to the C20 precursor GGPP" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High; core carotenoid precursor edge suitable for generic yellow carotenoid mechanism. |
| idi - positively_regulates_or_enables - IPP/DMAPP balance | gene/protein to process | label: idi/isopentenyl-diphosphate isomerase; EC candidate 5.3.3.2 | "the major GGPP synthase IdsA and the isoprenoid pyrophosphate isomerase Idi are promising engineering targets" and "overexpressing idi and idsA raises total carotenoids" (gottl2024enhancingastaxanthinbiosynthesis pages 3-3, gottl2024enhancingastaxanthinbiosynthesis pages 6-8) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High for carotenoid flux; effect is on precursor balance, not yellow color alone. |
| IdsA/CrtE - catalyzes_or_enables - GGPP biosynthesis | enzyme/gene to process | label: idsA / crtE; GGPP synthase | "IdsA, the major geranylgeranyl diphosphate synthase converting IPP and DMAPP to GGPP" (gottl2024enhancingastaxanthinbiosynthesis pages 3-3); "GGPPS, annotated CrtE/IdsA" (zhan2024expandingthecrispr pages 1-2) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9; DOI:10.3390/microorganisms12040803 (2024) https://doi.org/10.3390/microorganisms12040803 | High. |
| GGPP - precursor_of - lycopene | metabolite to pigment intermediate | label: geranylgeranyl diphosphate; CHEBI:15948 lycopene | "two GGPP molecules condense to form the C40 backbone lycopene" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High. Lycopene itself is red, but this is upstream of yellow carotenoids. |
| crtB - enables - phytoene/lycopene branch of carotenoid biosynthesis | gene/enzyme to pathway step | label: crtB phytoene synthase | "the pathway proceeds through... phytoene synthase (CrtB), and phytoene desaturase (CrtI) to produce lycopene" (zhan2024expandingthecrispr pages 1-2) | DOI:10.3390/microorganisms12040803 (2024) https://doi.org/10.3390/microorganisms12040803 | Medium-high; pathway step supported in lycopene-engineering context. |
| crtI - enables - lycopene biosynthesis | gene/enzyme to pathway step | label: crtI phytoene desaturase | "phytoene desaturase (CrtI) to produce lycopene" (zhan2024expandingthecrispr pages 1-2) | DOI:10.3390/microorganisms12040803 (2024) https://doi.org/10.3390/microorganisms12040803 | High. |
| crtY - catalyzes - lycopene to beta-carotene conversion | gene/enzyme to reaction | label: crtY lycopene beta-cyclase; CHEBI:17579 beta-carotene | "Lycopene is cyclized to beta-carotene by lycopene beta-cyclase (crtY)" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High; beta-carotene is a canonical yellow/orange trait-causing pigment. |
| beta-carotene - causes_or_contributes_to - yellow pigmented | pigment to phenotype | CHEBI:17579; METPO:1003030 | "beta-carotene functions as the precursor of provitamin A... serves as a colorant" and carotenoids are common pigment classes; beta-carotene is the classic yellow/orange carotenoid (huang2024bacterialpigmentsas pages 6-8, ruizUnknownyearproduçãodecarotenóides pages 38-41) | DOI:10.4014/jmb.2404.04018 (2024) https://doi.org/10.4014/jmb.2404.04018; DOI:10.11606/d.97.2024.tde-12122024-113132 (2024) https://doi.org/10.11606/d.97.2024.tde-12122024-113132 | Medium; broad phenotype-level edge, color may range yellow to orange depending on amount/context. |
| crtZ - catalyzes - beta-carotene hydroxylation | gene/enzyme to reaction | label: crtZ beta-carotene hydroxylase | "Conversion of beta-carotene to oxy-functionalized carotenoids such as astaxanthin requires beta-carotene hydroxylase (crtZ)" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High. Hydroxylated carotenoids can still be yellow/orange depending on terminal modifications. |
| crtW - catalyzes - beta-carotene ketolation | gene/enzyme to reaction | label: crtW beta-carotene ketolase | "Conversion of beta-carotene to oxy-functionalized carotenoids such as astaxanthin requires... beta-carotene ketolase (crtW)" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High; often shifts pigment away from yellow toward orange/red, so boundary-case note. |
| crtX - catalyzes - carotenoid glycosylation | gene/enzyme to reaction | label: crtX glycosyltransferase | "crtX as a glycosyltransferase that can add glucose moieties to hydroxy groups" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High for glycosylated carotenoid products; may affect solubility/stability rather than hue alone. |
| crtZ overexpression - increases - astaxanthin accumulation | gene expression change to metabolite abundance | label: crtZ; CHEBI:26966 astaxanthin | "extra crtZ expression... significantly increased astaxanthin (3.5 mg/g CDW)" (gottl2024enhancingastaxanthinbiosynthesis pages 5-6) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High but taxon/engineering-specific; not direct yellow phenotype edge. |
| engineered C. glutamicum - produces - astaxanthin-beta-D-diglucoside | organism/strain to metabolite | NCBITaxon:1718; label: astaxanthin-beta-D-diglucoside | "astaxanthin-beta-d-diglucoside... titers of 39 mg L-1" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High quantitative application edge; product is red/orange, included as carotenoid engineering endpoint. |
| engineered C. glutamicum - produces - beta-carotene | organism/strain to metabolite | NCBITaxon:1718; CHEBI:17579 | "BETA6 exhibited a 1.5-fold higher beta-carotene production reaching 18 mg g-1 CDW" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High; directly relevant yellow-carotenoid production example. |
| Xanthomonas xanthomonadin pigment - located_in - cell membrane/outer membrane | pigment to cellular component | NCBITaxon:338; label: xanthomonadin; GO candidate outer membrane GO:0019867 | "The Xanthomonas colonies are morphologically yellow due to membrane-bound xanthomonadin pigment" (dey2024aninsightinto pages 1-2); "genetic locus... required both for xanthomonadin biosynthesis and for outer membrane localization" (jimenez2024estudoinvitro pages 114-118) | DOI:10.1016/j.heliyon.2024.e34275 (2024) https://doi.org/10.1016/j.heliyon.2024.e34275 | High for membrane localization and phenotype. |
| xanthomonadin - protects_against - photobiological damage | pigment to process/stress | label: xanthomonadin; GO:0006979 response to oxidative stress approximate; ENVO light stress label-only | "protects them from photobiological damage" (dey2024aninsightinto pages 1-2); "protection against photobiological damage" (dey2024aninsightinto pages 11-12) | DOI:10.1016/j.heliyon.2024.e34275 (2024) https://doi.org/10.1016/j.heliyon.2024.e34275 | High. Excellent candidate edge for mechanism-to-fitness, but not direct yellow trait causation. |
| 3-hydroxybenzoic acid - precursor_of - xanthomonadin/aryl polyene pigment | metabolite to pigment class | CHEBI:30746 3-hydroxybenzoic acid; label: xanthomonadin | "xanthomonadins are... derived from an aryl precursor originating from 3-hydroxybenzoic acid" (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 96-99) | DOI:10.1016/j.heliyon.2024.e34275 cited indirectly via 2024 synthesis pages; supporting excerpt in 2024 thesis context (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 96-99) | Medium-high; mechanistically strong but proxied through synthesis/summary source. |
| ATP-dependent 3-hydroxybenzoic acid:ACP ligase - enables - xanthomonadin biosynthesis | enzyme to pathway | label-only candidate enzyme | "biosynthesis involves an ATP-dependent 3-hydroxybenzoic acid:acyl carrier protein ligase" (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 114-118) | Supporting synthesis of Cao et al. reported in 2024 source; https://doi.org/10.1016/j.heliyon.2024.e34275 and cited summary contexts (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 114-118) | Medium-high; curate with note that direct primary enzymology is older than 2023-2024. |
| unusual type II PKS pathway - enables - xanthomonadin biosynthesis | pathway to pigment biosynthesis | label: type II polyketide synthase pathway | "an unusual type II polyketide synthase pathway" (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 114-118) | Supporting synthesis in 2024 contexts (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 114-118) | Medium-high; same caution as above. |
| APE/PIG xan gene cluster - participates_in - xanthomonadin/aryl polyene biosynthesis | gene cluster to pathway | label-only candidate: Xcc PIG/APE cluster | "xanthomonadin-like pigments to the APE (formerly Xcc PIG) gene cluster" (jimenez2024estudoinvitroa pages 87-92); "dedicated biosynthetic gene clusters (APE/xan BGCs)" (jimenez2024estudoinvitroa pages 96-99) | Supporting 2024 summary contexts (jimenez2024estudoinvitroa pages 87-92, jimenez2024estudoinvitroa pages 96-99) | Medium; gene-cluster naming varies across literature, curate as label-level if no stable ID. |
| xanthomonadin/aryl polyenes - functionally_related_to - antioxidative carotenoids | pigment class to pigment class/function | label-only | "APEs (including xanthomonadins) are functionally related to antioxidative carotenoids" (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 96-99) | Supporting 2024 summary contexts (jimenez2024estudoinvitroa pages 96-99, jimenez2024estudoinvitro pages 96-99) | Medium; functional analogy, not direct biochemical identity. |
| flexirubin-type pigment - contributes_to - yellow/orange colony color | pigment class to phenotype | label: flexirubin-type pigment; METPO:1003030 | "C2 is a flexirubin-type pigment-producing bacterium that is yellow or orange in color at different pH values" (liu2024multiomicsdissectionof pages 11-12) | DOI:10.1038/s41467-024-54112-5 (2024) https://doi.org/10.1038/s41467-024-54112-5 | High for phenotype edge. |
| pH - affects - flexirubin color state yellow vs orange | environmental factor to phenotype | ENVO:00001998 hydrogen ion concentration/pH label-only; flexirubin label-only | "yellow or orange in color at different pH values" (liu2024multiomicsdissectionof pages 11-12) | DOI:10.1038/s41467-024-54112-5 (2024) https://doi.org/10.1038/s41467-024-54112-5 | High; assay/environment-dependent boundary case. |
| flexirubin - protects_against - reactive oxygen species damage | pigment to stress response | label: flexirubin; GO:0000302 response to reactive oxygen species | "Flexirubin is known as a yellow pigment that effectively protects against reactive oxygen species damage" (liu2024multiomicsdissectionof pages 11-12) | DOI:10.1038/s41467-024-54112-5 (2024) https://doi.org/10.1038/s41467-024-54112-5 | High. |
| acetate-derived polyene chain biosynthesis - contributes_to - flexirubin chromophore formation | process to pigment formation | label-only | "polyene chains in chromophore groups are synthesized from acetates in a manner similar to fatty acid biosynthesis" (liu2024multiomicsdissectionof pages 11-12) | DOI:10.1038/s41467-024-54112-5 (2024) https://doi.org/10.1038/s41467-024-54112-5 | Medium-high; process-level edge, no specific enzyme named here. |
| fabZ - enables - flexirubin biosynthesis | gene/enzyme to pigment biosynthesis | label: fabZ; EC candidate 4.2.1.59 and 3-hydroxyacyl-ACP dehydratase family | "Identification of a fabZ gene essential for flexirubin synthesis in Cytophaga hutchinsonii" (jimenez2024estudoinvitroa pages 114-118, jimenez2024estudoinvitro pages 114-118) | Cited in 2024 synthesis context (jimenez2024estudoinvitroa pages 114-118, jimenez2024estudoinvitro pages 114-118) | Medium-low for TraitMech now: useful older mechanistic lead, but organism-specific and not from 2023-2024 primary evidence. Mark uncertain. |
| KOH test positivity - indicative_of - flexirubin-type pigment | assay to pigment class | label-only diagnostic assay | "A simple test for flexirubin-type pigments" and KOH color-change discussion (jimenez2024estudoinvitroa pages 114-118, jimenez2024estudoinvitroa pages 54-60) | Cited in 2024 synthesis context (jimenez2024estudoinvitroa pages 114-118, jimenez2024estudoinvitroa pages 54-60) | Medium; diagnostic, not causal. Probably keep out of causal graph core. |
| light exposure - decreases_stability_of - microbial pigments | environmental factor to pigment stability | ENVO light label-only; GO:0042440 pigment metabolic process | "microbial pigments are... limitations to light, heat, and low pH" (anshi2024unveilingtheintricacies pages 2-4); "exposure to light, heat, and acidic pH can affect them" (anshi2024unveilingtheintricacies pages 2-4) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium; broad review-level edge across pigment classes, not yellow-specific. |
| heat - decreases_stability_of - microbial pigments | environmental factor to pigment stability | ENVO heat label-only | "limitations to light, heat, and low pH" (anshi2024unveilingtheintricacies pages 2-4) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium; broad and likely true, but not specific to one yellow chemistry. |
| acidic pH - decreases_stability_of - microbial pigments | environmental factor to pigment stability | pH label-only | "limitations to light, heat, and low pH" (anshi2024unveilingtheintricacies pages 2-4) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium; good for assay notes, maybe not core graph. |
| oxidation/aging - shifts - pigment appearance toward brownish color | process to phenotype | label-only | "brownish shift after greater than 48 h, possibly from oxidation/polymerization" (jimenez2024estudoinvitro pages 54-60, jimenez2024estudoinvitroa pages 54-60) | 2024 characterization context (jimenez2024estudoinvitro pages 54-60, jimenez2024estudoinvitroa pages 54-60) | Medium-low; useful warning for assay interpretation, not robust generic mechanism. |
| engineered C. glutamicum ASTA - produces - astaxanthin at 103 mg/L | strain/process to quantitative output | NCBITaxon:1718; CHEBI:26966 | "achieved 103 mg L-1 astaxanthin with a volumetric productivity of 1.5 mg L-1 h-1" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High quantitative application edge; orange/red endpoint but demonstrates real-world carotenoid implementation. |
| engineered C. glutamicum - produces - astaxanthin-beta-D-diglucoside at 39 mg/L | strain/process to quantitative output | NCBITaxon:1718; label: astaxanthin-beta-D-diglucoside | "first production of astaxanthin-beta-d-diglucoside... titers of 39 mg L-1" (gottl2024enhancingastaxanthinbiosynthesis pages 1-3) | DOI:10.1038/s41598-024-58700-9 (2024) https://doi.org/10.1038/s41598-024-58700-9 | High quantitative application edge. |
| Bacillus subtilis - produces - riboflavin | organism to pigment/metabolite | NCBITaxon:1423; CHEBI:17015 riboflavin | "Riboflavin yellow/flavin production by Bacillus subtilis... 26.8 mg/L" (anshi2024unveilingtheintricacies pages 4-5) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium; supports flavin-based yellow phenotype possibility and production application. |
| microbial pigments - applied_in - food/pharma/cosmetics/textiles | pigment class to application sector | label-only application nodes | "used in food and pharma industries"; applications in "textiles, cosmetics, food, and pharmaceutical industries" (anshi2024unveilingtheintricacies pages 2-4, anshi2024unveilingtheintricacies pages 4-5) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium-high; application edge, not causal to phenotype. |
| carotenoids - represent - major microbial pigment market segment | pigment class to market/application status | label-only | "carotenoids are the most common pigment to be used in food and pharma industries" (anshi2024unveilingtheintricacies pages 2-4) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium; market/context rather than mechanistic causation. |
| organic pigments market - projected_to_reach - 8.4 billion USD by 2031 | market entity to statistic | label-only | "organic pigments market projected to reach 8.4 billion USD by 2031" (anshi2024unveilingtheintricacies pages 2-4) | DOI:10.3390/micro4040038 (2024) https://doi.org/10.3390/micro4040038 | Medium; useful context only, not curate into TraitMech graph. |


*Table: This table compiles candidate subject-predicate-object edges for curating the microbial trait METPO:1003030 yellow pigmented, spanning carotenoid, xanthomonadin and aryl polyene, flexirubin, and assay or environment effects. It also includes quantitative application rows and confidence notes to help separate core causal claims from broader contextual evidence.*

---

## Warnings / curation cautions (do not over-curate)
1) **Color ≠ chemistry**: “yellow” is a convergent phenotype. Without chemical/genetic evidence, avoid asserting a specific pigment class (carotenoid vs flexirubin vs xanthomonadin/APE). (jimenez2024estudoinvitro pages 92-96, jimenez2024estudoinvitro pages 54-60)
2) **Taxon specificity**: some mechanistic genes are validated in specific taxa (e.g., fabZ essentiality for flexirubin synthesis was cited via earlier work and may not generalize). Mark such edges as **uncertain** unless corroborated in the target organism/context. (jimenez2024estudoinvitroa pages 114-118)
3) **Assay dependence**: flexirubin hue depends on **pH**; pigment stability depends on **light/heat/acidic pH**; colony age/oxidation can shift appearance (e.g., brownish). Capture assay conditions when possible. (liu2024multiomicsdissectionof pages 11-12, anshi2024unveilingtheintricacies pages 2-4, jimenez2024estudoinvitro pages 54-60)
4) **Downstream carotenoids can shift hue**: engineering for astaxanthin/lycopene is mechanistically adjacent but may not produce a “yellow” phenotype; keep graph edges focused on the pigment(s) that actually yield yellow appearance. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3)

---

## DOI-first bibliography (with publication dates and URLs)

1) Göttl VL, et al. **Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated C40 carotenoids by Corynebacterium glutamicum.** *Scientific Reports* (Apr 2024). DOI: **10.1038/s41598-024-58700-9**. URL: https://doi.org/10.1038/s41598-024-58700-9 (gottl2024enhancingastaxanthinbiosynthesis pages 1-3, gottl2024enhancingastaxanthinbiosynthesis media f31745ca)

2) Zhan Z, et al. **Expanding the CRISPR toolbox for engineering lycopene biosynthesis in Corynebacterium glutamicum.** *Microorganisms* (Apr 2024). DOI: **10.3390/microorganisms12040803**. URL: https://doi.org/10.3390/microorganisms12040803 (zhan2024expandingthecrispr pages 1-2)

3) Liu C, et al. **Multiomics dissection of Brassica napus L. lateral roots and endophytes interactions under phosphorus starvation.** *Nature Communications* (Nov 2024). DOI: **10.1038/s41467-024-54112-5**. URL: https://doi.org/10.1038/s41467-024-54112-5 (liu2024multiomicsdissectionof pages 11-12)

4) Dey R, Raghuwanshi R. **An insight into pathogenicity and virulence gene content of Xanthomonas spp. and its biocontrol strategies.** *Heliyon* (Available online 8 Jul 2024; accepted 7 Jul 2024). DOI: **10.1016/j.heliyon.2024.e34275**. URL: https://doi.org/10.1016/j.heliyon.2024.e34275 (dey2024aninsightinto pages 1-2)

5) Anshi, et al. **Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements.** *Micro* (Oct 2024). DOI: **10.3390/micro4040038**. URL: https://doi.org/10.3390/micro4040038 (anshi2024unveilingtheintricacies pages 2-4, anshi2024unveilingtheintricacies pages 4-5)

6) Huang X, et al. **Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications.** *Journal of Microbiology and Biotechnology* (Sep 2024). DOI: **10.4014/jmb.2404.04018**. URL: https://doi.org/10.4014/jmb.2404.04018 (huang2024bacterialpigmentsas pages 6-8)

7) Shende VV, Bauman KD, Moore BS. **The shikimate pathway: gateway to metabolic diversity.** *Natural Product Reports* (Jan 2024). DOI: **10.1039/d3np00037k**. URL: https://doi.org/10.1039/d3np00037k (background on shikimate-derived specialized metabolism; supports grounding for aromatic precursors relevant to aryl polyenes) (shende2024theshikimatepathway pages 3-4)

8) Jiménez MEP. **Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas.** (2024; venue unclear in retrieved text). Used here for pigment-class discrimination, APE/xanthomonadin/flexirubin boundaries, and mechanistic summaries; treat as supportive/secondary where primary sources are not directly retrieved. (jimenez2024estudoinvitro pages 54-60, jimenez2024estudoinvitroa pages 96-99)



References

1. (liu2024multiomicsdissectionof pages 11-12): Can Liu, Zhen Bai, Yu Luo, Yanfeng Zhang, Yongfeng Wang, Hexin Liu, Meng Luo, Xiaofang Huang, Anle Chen, Lige Ma, Chen Chen, Jinwei Yuan, Ying Xu, Yantao Zhu, Jianxin Mu, Ran An, Cuiling Yang, Hao Chen, Jiajie Chen, Zaifang Li, Xiaodan Li, Yachen Dong, Jianhua Zhao, Xingxing Shen, Lixi Jiang, Xianzhong Feng, Peng Yu, Daojie Wang, Xinping Chen, and Nannan Li. Multiomics dissection of brassica napus l. lateral roots and endophytes interactions under phosphorus starvation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54112-5, doi:10.1038/s41467-024-54112-5. This article has 50 citations and is from a highest quality peer-reviewed journal.

2. (anshi2024unveilingtheintricacies pages 2-4): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 17 citations.

3. (jimenez2024estudoinvitro pages 54-60): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

4. (gottl2024enhancingastaxanthinbiosynthesis pages 1-3): Vanessa L. Göttl, Florian Meyer, Ina Schmitt, Marcus Persicke, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated c40 carotenoids by corynebacterium glutamicum. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58700-9, doi:10.1038/s41598-024-58700-9. This article has 34 citations and is from a peer-reviewed journal.

5. (huang2024bacterialpigmentsas pages 6-8): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 31 citations and is from a peer-reviewed journal.

6. (jimenez2024estudoinvitroa pages 54-60): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

7. (jimenez2024estudoinvitro pages 92-96): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

8. (dey2024aninsightinto pages 1-2): Riddha Dey and Richa Raghuwanshi. An insight into pathogenicity and virulence gene content of xanthomonas spp. and its biocontrol strategies. Heliyon, 10:e34275, Jul 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e34275, doi:10.1016/j.heliyon.2024.e34275. This article has 18 citations.

9. (jimenez2024estudoinvitroa pages 96-99): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

10. (anshi2024unveilingtheintricacies pages 4-5): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 17 citations.

11. (gottl2024enhancingastaxanthinbiosynthesis media f31745ca): Vanessa L. Göttl, Florian Meyer, Ina Schmitt, Marcus Persicke, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated c40 carotenoids by corynebacterium glutamicum. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58700-9, doi:10.1038/s41598-024-58700-9. This article has 34 citations and is from a peer-reviewed journal.

12. (gottl2024enhancingastaxanthinbiosynthesis pages 8-9): Vanessa L. Göttl, Florian Meyer, Ina Schmitt, Marcus Persicke, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated c40 carotenoids by corynebacterium glutamicum. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58700-9, doi:10.1038/s41598-024-58700-9. This article has 34 citations and is from a peer-reviewed journal.

13. (zhan2024expandingthecrispr pages 1-2): Zhimin Zhan, Xiong Chen, Zhifang Ye, Ming Zhao, Cheng Li, Shipeng Gao, Anthony J. Sinskey, Lan Yao, Jun Dai, Yiming Jiang, and Xueyun Zheng. Expanding the crispr toolbox for engineering lycopene biosynthesis in corynebacterium glutamicum. Microorganisms, 12:803, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040803, doi:10.3390/microorganisms12040803. This article has 10 citations.

14. (zhan2024expandingthecrispr pages 12-14): Zhimin Zhan, Xiong Chen, Zhifang Ye, Ming Zhao, Cheng Li, Shipeng Gao, Anthony J. Sinskey, Lan Yao, Jun Dai, Yiming Jiang, and Xueyun Zheng. Expanding the crispr toolbox for engineering lycopene biosynthesis in corynebacterium glutamicum. Microorganisms, 12:803, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040803, doi:10.3390/microorganisms12040803. This article has 10 citations.

15. (jimenez2024estudoinvitro pages 96-99): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

16. (jimenez2024estudoinvitroa pages 87-92): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

17. (gottl2024enhancingastaxanthinbiosynthesis pages 3-3): Vanessa L. Göttl, Florian Meyer, Ina Schmitt, Marcus Persicke, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated c40 carotenoids by corynebacterium glutamicum. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58700-9, doi:10.1038/s41598-024-58700-9. This article has 34 citations and is from a peer-reviewed journal.

18. (gottl2024enhancingastaxanthinbiosynthesis pages 6-8): Vanessa L. Göttl, Florian Meyer, Ina Schmitt, Marcus Persicke, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated c40 carotenoids by corynebacterium glutamicum. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58700-9, doi:10.1038/s41598-024-58700-9. This article has 34 citations and is from a peer-reviewed journal.

19. (ruizUnknownyearproduçãodecarotenóides pages 38-41): Erick Diaz Ruiz. Produção de carotenóides a partir de bagaço de cana-de-açúcar por rhodotorula glutinis cct-2186. ArXiv, Unknown year. URL: https://doi.org/10.11606/d.97.2024.tde-12122024-113132, doi:10.11606/d.97.2024.tde-12122024-113132. This article has 0 citations.

20. (gottl2024enhancingastaxanthinbiosynthesis pages 5-6): Vanessa L. Göttl, Florian Meyer, Ina Schmitt, Marcus Persicke, Petra Peters-Wendisch, Volker F. Wendisch, and Nadja A. Henke. Enhancing astaxanthin biosynthesis and pathway expansion towards glycosylated c40 carotenoids by corynebacterium glutamicum. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58700-9, doi:10.1038/s41598-024-58700-9. This article has 34 citations and is from a peer-reviewed journal.

21. (jimenez2024estudoinvitro pages 114-118): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

22. (dey2024aninsightinto pages 11-12): Riddha Dey and Richa Raghuwanshi. An insight into pathogenicity and virulence gene content of xanthomonas spp. and its biocontrol strategies. Heliyon, 10:e34275, Jul 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e34275, doi:10.1016/j.heliyon.2024.e34275. This article has 18 citations.

23. (jimenez2024estudoinvitroa pages 114-118): ME Pailliè Jiménez. Estudo in vitro e in silico de pigmentos aril polienos produzidos por duas bactérias queratinolíticas. Unknown journal, 2024.

24. (shende2024theshikimatepathway pages 3-4): Vikram V. Shende, Katherine D. Bauman, and Bradley S. Moore. The shikimate pathway: gateway to metabolic diversity. Natural product reports, 41:604-648, Jan 2024. URL: https://doi.org/10.1039/d3np00037k, doi:10.1039/d3np00037k. This article has 183 citations and is from a peer-reviewed journal.