---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:11:50.135768'
end_time: '2026-06-17T21:27:57.623546'
duration_seconds: 967.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: alkaphilic
  trait_identifier: METPO:1003002
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: alkaphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism grows optimally at pH values
    above 9.
  parent_traits: METPO:1003000
  synonyms: alkaliphile, alkaliphilic, alkalophile, alkalophilic
  evidence_summary: 'DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports
    alkaliphilic growth at strongly alkaline external pH.)'
  causal_graph_summary: 'alkaliphilic_na_cycle_homeostasis: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** alkaphilic
- **METPO identifier:** METPO:1003002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values above 9.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkaliphile, alkaliphilic, alkalophile, alkalophilic
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports alkaliphilic growth at strongly alkaline external pH.)
- **Existing causal graph summary:** alkaliphilic_na_cycle_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkaphilic.yaml`.

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
- **Trait label:** alkaphilic
- **METPO identifier:** METPO:1003002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism grows optimally at pH values above 9.
- **Parent traits:** METPO:1003000
- **Synonyms:** alkaliphile, alkaliphilic, alkalophile, alkalophilic
- **Existing evidence:** DOI:10.1038/nrmicro2549: external pH range of 9.5-11.0 (Supports alkaliphilic growth at strongly alkaline external pH.)
- **Existing causal graph summary:** alkaliphilic_na_cycle_homeostasis: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/alkaphilic.yaml`.

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


## Curation-focused research report: **alkaphilic / alkaliphilic** (METPO:1003002)

### 1) Scope summary (trait meaning, boundaries, current understanding)

**Trait definition (operational):** *Alkaphilic/alkaliphilic* denotes a growth preference where an organism’s **optimal growth occurs at external pH > 9**, typically in carbonate-buffered alkaline environments (e.g., soda lakes, serpentinizing systems). This is an **organism-level phenotype** (growth optimum/range), not a single molecular function. 

**Key boundary case—alkalitolerant vs (obligate) alkaliphile:** A recent 2023 study on aceticlastic methanogens explicitly contrasts an **alkalitolerant** strain with an **obligate alkaliphile**: strain **M04Ac** grows from **pH 7.5–10.0** (optimum **pH 9.0**), while soda-lake strain **Mx** is an **obligate alkaliphile** growing from **pH 7.7–10.2** (optimum **pH 9.3–9.5**) with optimal total Na+ **0.2–0.3 M** (10.3389/fmicb.2023.1233691; Oct 2023) (khomyakova2023phenotypicandgenomic pages 1-2).

**External pH vs cytoplasmic pH homeostasis:** Alkaliphily does **not** necessarily imply perfect cytoplasmic pH constancy at high pH. In the high-authority Nat Rev Microbiol review, **Bacillus pseudofirmus OF4** is described as maintaining “complete pH homeostasis” (pHin ~7.5) only from **pHout 7.5–9.5**, while it **still grows optimally** up to **pHout ~10.5** where **pHin = 8.3**, and can grow with **pHin ≥ 9.5 at pHout ≥ 11** (10.1038/nrmicro2549; May 2011) (krulwich2011molecularaspectsof pages 12-14). This distinction is important for TraitMech curation: edges may support **growth at high pH** via partial homeostasis and bioenergetic compensation rather than strict pHin clamping.

### 2) Key mechanistic concepts (nodes for causal graph)

Below are **candidate nodes** grouped by type. CURIEs are suggested where stable identifiers are clear; otherwise label-only nodes are provided.

#### A. Environmental / experimental factors
- **High external pH (>9)** (label-only; maps to METPO:1003002 context)
- **Carbonate alkalinity / soda lake chemistry** (label-only; ENVO candidate: soda lake)
- **High Na+ / saline-alkaline conditions** (label-only)
- **Low proton availability at cell surface** (label-only)
- **Oxygen limitation / microaerobic conditions** (label-only; affects Mrp regulation in one alkaliphile) (jong2024quantitativeproteomicsreveals pages 1-2)

#### B. Core homeostasis and transport systems
- **Mrp (multiple resistance and pH) Na+/H+ antiporter complex** (label-only; TCDB CPA3 family candidate). A hetero-oligomeric antiporter encoded by a **7-gene operon**, critical in extreme alkaliphilic Bacillus (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22).
- **Other monovalent cation/proton antiporters** (label-only; e.g., Nha families) (xing2024thepolyextremophilenatranaerobius pages 19-21, krulwich2011molecularaspectsof pages 6-8).
- **NhaA Na+/H+ antiporter (E. coli model)** (label-only; useful mechanistic exemplar of pH sensing/activation) (krulwich2011molecularaspectsof pages 6-8).
- **NhaC-family antiporters (archaea/bacteria)** (label-only; NhaC1/NhaC2 examples) (wang2023characterizationoftwo pages 7-8).
- **TrkAH K+ uptake system** (label-only; supports ion homeostasis/membrane potential in haloalkaliphiles) (xing2024thepolyextremophilenatranaerobius pages 19-21).
- **Na+/solute symporters** (label-only; support Na+ cycle) (krulwich2011molecularaspectsof pages 12-14).
- **Na+ channels: MotPS and NavBP** (label-only; support Na+ cycle in Bacillus model) (krulwich2011molecularaspectsof pages 12-14).

#### C. Bioenergetics / respiratory chain
- **F1Fo-ATP synthase (alkaliphile-adapted)** (GO candidate: ATP synthesis coupled proton transport). Includes **subunit a/c motifs** and rotor features proposed to increase proton affinity/retention at high pH (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof media 64f40140).
- **Terminal oxidases and H+/e− stoichiometry (Caldalkalibacillus thermarum)**: Cyt. aa3 (~0.7 H+/e−), Cyt. ba3/bb3 (~0.5 H+/e−), Cyt. bd (no proton pumping) (jong2024quantitativeproteomicsreveals pages 1-2).
- **Outer-surface cytochrome c “H+ capacitor”** (label-only; a mechanism to retain/accumulate protons near membrane surface) (goto2022differencesinbioenergetic pages 1-2).

#### D. Cell envelope / surface chemistry
- **Acidic S-layer proteins and acidic secondary cell walls** (label-only; attract/retain protons at high pH) (goto2022differencesinbioenergetic pages 1-2).
- **Teichuronic/teichuronopeptide-like cell wall components** (label-only; mentioned as acidic surface contributors) (goto2022differencesinbioenergetic pages 1-2).

#### E. Osmoprotection / compatible solutes (often co-occurring with alkaliphily)
- **Ectoine biosynthesis** (CHEBI:27745 ectoine; pathway label-only) (khomyakova2023phenotypicandgenomic pages 1-2).
- **Glycine betaine, proline, glutamate** (CHEBI candidates; used in a polyextremophilic alkalithermophile under high salinity/pH) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21).

#### F. Metabolic capabilities in alkaline habitats (contextual nodes)
- **Nitrate respiration / nitrate as terminal electron acceptor** (GO candidate; supports growth in serpentinizing alkaliphile isolate) (thompson2023insightsintothe pages 1-2).
- **Hydrogenotrophic respiration + nitrate reduction** (label-only; inferred from genome analysis of a probable alkaliphile) (thompson2023insightsintothe pages 1-2).
- **Flavin-mediated iron reduction and siderophore (bacillibactin-like) synthesis** (label-only; alkaline serpentinizing isolate) (thompson2023insightsintothe pages 1-2).

### 3) Recent developments and latest research (prioritizing 2023–2024)

#### 3.1. New isolate-anchored pH ranges and metabolisms in extreme alkaline systems (2023)
A 2023 serpentinizing-system isolate study reports multiple **alkaliphiles with explicit pH ranges** and links alkaliphily to **respiratory strategies under electron-acceptor limitation**. For example, **Alishewanella sp. BS5-314** is reported as an “alkaliphile” growing **pH 10–12** and using **nitrate as a terminal electron acceptor** (genome-supported) (10.3389/fmicb.2023.1179857; Jul 2023) (thompson2023insightsintothe pages 1-2). This strengthens curation of nodes that represent **electron-acceptor usage under alkaline conditions** as context nodes (not necessarily causal).

#### 3.2. First alkaliphilic aceticlastic methanogens + ectoine in archaea (2023)
Khomyakova et al. (Frontiers in Microbiology, Oct 2023) provide **genome-backed alkaliphile physiology** for aceticlastic methanogens, with **growth optima in the 9.3–9.5 range** and **ectoine biosynthesis** identified as a haloalkaline adaptation (10.3389/fmicb.2023.1233691) (khomyakova2023phenotypicandgenomic pages 1-2). This is notable for TraitMech because it expands alkaliphily mechanisms beyond Bacillus models and ties a canonical compatible-solute pathway (ectoine) to alkaline archaeal ecology.

#### 3.3. Quantitative ion-homeostasis data under combined extremes (2024)
Xing et al. (Appl Environ Microbiol, May 2024) measured quantitative ion parameters in **Natranaerobius thermophilus**, an alkalithermophile with optimal growth at **pH ~9.5** and high Na+ (3.3–3.9 M) (10.1128/aem.00145-24) (xing2024thepolyextremophilenatranaerobius pages 1-2). The study reports **Δψ = −124 mV**, **pmf = −56 mV**, and **intracellular K+ ~250 mM** at **pH 9.5**, and documents intracellular K+ increasing to **227–440 mM** across salinity conditions (xing2024thepolyextremophilenatranaerobius pages 19-21). These data directly support edges connecting K+ uptake (TrkAH) and membrane potential in alkaline/saline growth.

#### 3.4. Oxygen-dependent regulation of Mrp and alternative exporters (2024)
In **Caldalkalibacillus thermarum TA2.A1**, proteomics showed **Mrp downregulation at low oxygen**, despite the canonical view that Mrp is “crucial for sodium homeostasis” in alkaliphiles. The authors propose a **sodium:acetate exporter** could reduce reliance on Mrp under strong oxygen limitation (Frontiers in Microbiology, Oct 2024; 10.3389/fmicb.2024.1468929) (jong2024quantitativeproteomicsreveals pages 1-2). This is an example of a **recent, testable hypothesis** about conditional redundancy in alkaliphile sodium cycling.

#### 3.5. Archaeal NhaC antiporters with alkaline optima (2023)
Wang et al. characterized two archaeal **NhaC-family Na+(K+,Li+)/H+ antiporters** (NhaC1/NhaC2) and show **pH-dependent activity from pH 7.0–10.0 with an optimum at pH 9.5**, and growth complementation enabling tolerance up to **pH 9.5** for nhaC2 in E. coli KNabc (Int J Mol Sci, Jun 2023; 10.3390/ijms241310786) (wang2023characterizationoftwo pages 7-8). This provides concrete gene-level candidates for trait graphs in haloalkaliphilic archaea.

### 4) Current applications and real-world implementations (with quantitative metrics)

#### 4.1. Textile wastewater (alkaline/saline azo dyes): performance and deployment logic (2024)
A 2024 review on azo-dye textile wastewater notes industrial drivers: textile effluents are often **alkaline and saline** (“pH often >10”; chloride **1756–6022 mg/L**; dyeing uses **~15–20% salt**), and the textile sector contributes **≈20% of global industrial wastewater** with **≈280,000 tons dye effluent annually** (3 Biotech, Aug 2024; 10.1007/s13205-024-04036-0) (wadhawan2024potentialofhalophiles pages 1-2). The same review compiles multiple **quantitative decolorization examples** under harsh conditions, including a halo-alkaliphile **Nesterenkonia lacusekhoensis** decolorizing Reactive Red 35 (100 mg/L) in **9 h at pH 11.5**, **35 °C**, and **15% NaCl**, and Bacillus strains achieving **~82–100%** dye removal across **pH 7–10** (wadhawan2024potentialofhalophiles pages 7-8). Table-level summaries show reported decolorization often **~92–100%** across strains and dyes, with pH optima extending into strongly alkaline regimes (wadhawan2024potentialofhalophiles pages 10-11). These data support a “real-world implementation” framing: alkaliphiles/haloalkaliphiles can treat wastewater **without pre-neutralization**, reducing process complexity (wadhawan2024potentialofhalophiles pages 6-7).

#### 4.2. Saline-alkali soil improvement (2023)
An applied microbial/plant co-treatment study used **saline-alkali-tolerant bacteria** (*Priestia aryabhattai* JL-5 and *Staphylococcus pseudoxylosus* XW-4) plus corn straw and *Leymus chinensis* to improve soil properties, increasing soil available nutrients (N/P/K, organic matter) and plant antioxidant activities; the authors highlight commercial development potential (Int J Mol Sci, Apr 2023; 10.3390/ijms24097737) (wang2023salinealkalisoilproperty pages 1-2). This is not a direct alkaliphily mechanism paper, but provides an implementation context for “alkali-adapted” microbial inoculants.

#### 4.3. Bioextraction/bioremediation of metals in harsh wastes (2024)
A 2024 overview describes extremophiles (including alkaliphiles) as candidates for bioleaching/bioextraction and heavy-metal removal, citing alkaliphilic *Citricoccus alkalitolerans* CSB1 as a biosorbent for arsenic in tannery wastewater (Minerals, Aug 2024; 10.3390/min14090861) (adetunji2024unravelingthepotentials pages 19-20). Quantitative metrics are not provided in the excerpted portion, so this application should be treated as **indicative** pending primary-source extraction.

### 5) Expert synthesis and analysis (authoritative viewpoints)

**Central consensus mechanism—ion-transport-centered pH homeostasis:** The high-citation Nat Rev Microbiol synthesis frames extreme alkaliphile survival as a coupled **Na+ cycle** and **H+ acquisition problem**, with **Mrp** as a central “indispensable” proton-uptake system at high pH and complementary Na+ entry routes (Na+/solute symporters; Na+ channels MotPS and NavBP) supporting continuous cycling (10.1038/nrmicro2549) (krulwich2011molecularaspectsof pages 12-14).

**Bioenergetic compensation beyond bulk chemiosmosis:** Work on obligate alkaliphilic Bacillaceae emphasizes that alkaliphiles can retain/accumulate scarce protons at the cell surface (e.g., via surface-localized cytochrome c and acidic envelope structures), effectively constructing an outer-surface “H+ capacitor” to make ATP synthesis feasible under low proton availability (Frontiers in Microbiology, Mar 2022; 10.3389/fmicb.2022.842785) (goto2022differencesinbioenergetic pages 1-2).

**Recent nuance—conditional remodeling of canonical alkaliphile components:** 2024 proteomics in *Caldalkalibacillus thermarum* suggests that even “core” alkaliphile components (Mrp) can be downregulated under specific conditions (oxygen limitation), and alternative exporters may partially substitute—an important reminder for TraitMech that edges may be **conditional** (jong2024quantitativeproteomicsreveals pages 1-2).

### 6) Candidate causal edges (evidence-backed triples)

The following artifact compiles candidate edges with **DOI-first references**, **verbatim snippets**, and **curation notes/uncertainty**.

| Subject node (label + suggested CURIE) | Predicate | Object node (label + suggested CURIE) | Evidence (DOI/URL + year) | Supporting snippet (verbatim short quote) | Notes/uncertainty for curation |
|---|---|---|---|---|---|
| Mrp Na+/H+ antiporter complex (TCDB:CPA3 family; GO:0015385 candidate) | enables | proton uptake / pH homeostasis (GO:0006885 candidate) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “Na+/H+ antiporter-dependent pH homeostasis” and Mrp plays an “indispensible role at high pH” (krulwich2011molecularaspectsof pages 12-14) | Strong, foundational evidence; curatable as core alkaliphily mechanism, though exact GO term for “proton uptake” should be checked. |
| Na+/solute symporters (label-only; TCDB family candidate) | supplies Na+ for | Na+ cycle supporting Mrp-mediated antiport (label-only) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “Cytoplasmic Na+ is supplied by numerous Na+/solute symporters” (krulwich2011molecularaspectsof pages 12-14) | Mechanistically strong in Bacillus pseudofirmus OF4; broad generalization to all alkaliphiles should be marked moderate. |
| MotPS Na+ channel (label-only) | supplies Na+ for | Na+ cycle supporting antiport/pH homeostasis (label-only) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “two Na+ channels, the flagella-associated MotPS channel and a voltage-gated sodium channel (NavBP)” (krulwich2011molecularaspectsof pages 12-14) | Taxon-specific to Bacillus model; likely accessory rather than universal. |
| NavBP voltage-gated sodium channel (label-only) | supplies Na+ for | Na+ cycle supporting antiport/pH homeostasis (label-only) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “two Na+ channels… MotPS… and a voltage-gated sodium channel (NavBP)” (krulwich2011molecularaspectsof pages 12-14) | Same caution as above; useful candidate edge but likely not universal. |
| ATP synthase c-subunit alkaline-adaptive motifs (label-only) | increases | proton binding / ATP synthase efficiency at high pH (GO:0046933 candidate) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “two c-subunit motifs that alter rotor shape and promote tight proton binding in the ion site” (krulwich2011molecularaspectsof pages 27-28) | Strong mechanistic support in alkaliphilic Bacillus ATP synthase; motif-level curation may need sequence-feature representation rather than generic node. |
| NhaA Na+/H+ antiporter (TCDB:2.A.33.1.1 candidate) | activity increases with | alkaline external pH (CHEBI: no pH CURIE; label-only environmental factor) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “activity rises by about three orders of magnitude between pHout 6.5 and 8.5” (krulwich2011molecularaspectsof pages 6-8) | High-quality mechanistic evidence, but from E. coli rather than obligate alkaliphile; curate as general antiporter principle or mark indirect for trait. |
| NhaA Na+/H+ antiporter (TCDB:2.A.33.1.1 candidate) | enables | growth at alkaline pH in presence of Na+ (METPO:1003002 context) | 10.1038/nrmicro2549 · https://doi.org/10.1038/nrmicro2549 · 2011 | “NhaA is essential for E. coli adaptation to alkaline pH in the presence of Na+” (krulwich2011molecularaspectsof pages 6-8) | Useful supporting principle, but not evidence for alkaliphily per se; best marked indirect/not core TraitMech edge. |
| NhaC2 antiporter from Natronorubrum daqingense (label-only; TCDB NhaC family candidate) | confers | alkaline tolerance up to pH 9.5 (METPO:1003002 context) | 10.3390/ijms241310786 · https://doi.org/10.3390/ijms241310786 · 2023 | “KNabc/pUC-nhaC2… a pH of up to 9.5” (wang2023characterizationoftwo pages 7-8) | Strong primary evidence from heterologous complementation; assay-specific and gene-specific, so curate as taxon-specific supportive edge. |
| NhaC1/NhaC2 antiporters (label-only; TCDB NhaC family candidate) | has optimal activity at | pH 9.5 (label-only assay condition) | 10.3390/ijms241310786 · https://doi.org/10.3390/ijms241310786 · 2023 | “antiport activities… are both pH-dependent in the range of pH 7.0–10.0, and the optimal pH is 9.5” (wang2023characterizationoftwo pages 7-8) | Strong assay evidence; antiporter activity optimum is not identical to whole-organism growth optimum. |
| TrkAH K+ uptake system (TCDB Trk family candidate) | increases | intracellular K+ concentration (CHEBI:29103 potassium(1+)) | 10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 · 2024 | “The TrkAH system is the sole K+ uptake system… intracellular K+ rising with salinity to 227–440 mM” (xing2024thepolyextremophilenatranaerobius pages 19-21) | Strong recent primary evidence in Natranaerobius; direct K+ measurements support edge. |
| Increased intracellular K+ (CHEBI:29103) | supports | membrane potential / pH homeostasis (GO:0006811 candidate) | 10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 · 2024 | “under 3.3 M NaCl, pH 9.5, 53°C report Δψ = −124 mV… intracellular K+ ≈ 250 mM” (xing2024thepolyextremophilenatranaerobius pages 19-21) | Inference from coupled measurements and text interpretation; useful but should be marked moderate/inferred. |
| Membrane-bound cytochrome c on outer surface (label-only) | retains | protons as H+ capacitor (label-only) | 10.3389/fmicb.2022.842785 · https://doi.org/10.3389/fmicb.2022.842785 · 2022 | “uses cytochrome c bound on its outer surface of the membrane as an H+ capacitor” (goto2022differencesinbioenergetic pages 1-2) | Strong for Evansella clarkii; taxon-specific bioenergetic adaptation, not clearly universal. |
| Acidic S-layer / cell-wall components (S-layer proteins, teichuronic components; label-only) | attracts/retains | protons at cell surface (label-only) | 10.3389/fmicb.2022.842785 · https://doi.org/10.3389/fmicb.2022.842785 · 2022 | “acidic secondary cell walls and S-layer proteins… attract H+” (goto2022differencesinbioenergetic pages 1-2) | Good mechanistic support for surface proton retention; specific polymers/terms need exact grounding before curation. |
| Ectoine biosynthesis pathway (CHEBI:27745 ectoine; pathway label-only) | supports | haloalkaline adaptation / osmoprotection (GO:0006970 candidate) | 10.3389/fmicb.2023.1233691 · https://doi.org/10.3389/fmicb.2023.1233691 · 2023 | “different mechanisms of (halo)alkaline adaptations, including ectoine biosynthesis” (khomyakova2023phenotypicandgenomic pages 1-2) | Strong recent primary evidence in alkaliphilic methanogens; mechanism may be more osmotic than directly pH-homeostatic. |
| Nitrate respiration (GO:0042128 candidate) | supports growth of | Alishewanella sp. BS5-314 under alkaliphilic conditions (NCBITaxon: label-only) | 10.3389/fmicb.2023.1179857 · https://doi.org/10.3389/fmicb.2023.1179857 · 2023 | “Ali-BS5-314 is an alkaliphile growing between pH 10–12… Nitrate is used as a terminal electron acceptor” (thompson2023insightsintothe pages 1-2) | Strong isolate-level evidence; edge is about metabolism in an alkaliphile, not necessarily causal for alkaliphily itself. |
| Sodium:acetate exporter (label-only) | decreases requirement for | Mrp antiporter under low O2 (label-only) | 10.3389/fmicb.2024.1468929 · https://doi.org/10.3389/fmicb.2024.1468929 · 2024 | “We propose that the existence of a sodium:acetate exporter decreases the requirement for Mrp under strong oxygen limitation” (jong2024quantitativeproteomicsreveals pages 1-2) | Explicitly proposed by authors; should be marked uncertain/inferred until directly tested. |
| Alkaline/saline textile wastewater (ENVO:industrial wastewater candidate) | selects for / is treatable by | haloalkaliphilic dye-decolorizing microbes (label-only) | 10.1007/s13205-024-04036-0 · https://doi.org/10.1007/s13205-024-04036-0 · 2024 | “textile effluents are often alkaline and saline (pH often >10)” and a “halo-alkaliphile Nesterenkonia lacusekhoensis treated Reactive Red 35… at pH 11.5, 35 °C with 15% NaCl” (wadhawan2024potentialofhalophiles pages 1-2, wadhawan2024potentialofhalophiles pages 7-8) | Application edge rather than intrinsic mechanism; useful as environment/application context, not core TraitMech mechanism. |


*Table: This table compiles evidence-backed candidate subject-predicate-object edges for curating the alkaphilic trait, including mechanisms of sodium/proton cycling, ATP synthase adaptation, potassium uptake, surface proton retention, and applied haloalkaliphile use in alkaline waste treatment. It is useful for prioritizing which claims are strong enough for TraitMech curation and which should remain tentative or taxon-specific.*

**Figure evidence for mechanistic context:** Krulwich et al. include a schematic of alkaliphile Na+/H+ cycling, the Mrp operon, and ATP synthase adaptations (Figure 4, page 28) (krulwich2011molecularaspectsof media 64f40140). This figure is useful for curators to align node boundaries (Mrp complex subunits; Na+ entry routes; ATP synthase motifs) with graph structure.

### 7) Warnings / claims not ready for TraitMech curation

1. **Do not equate antiporter activity optima with growth optima.** For example, NhaC1/NhaC2 show transport activity optimum at pH 9.5 and confer alkaline tolerance in E. coli (wang2023characterizationoftwo pages 7-8), but this does not by itself establish organism-level “alkaphilic” growth preference in the native archaeon.
2. **Treat author proposals as uncertain edges unless experimentally validated.** The sodium:acetate exporter reducing Mrp requirement is explicitly framed as a proposal (jong2024quantitativeproteomicsreveals pages 1-2).
3. **Application contexts are not intrinsic mechanisms.** Wastewater decolorization performance supports feasibility and selection pressure but does not directly evidence mechanistic nodes unless paired with enzyme/omics evidence.
4. **Taxon-specific envelope and ‘H+ capacitor’ mechanisms** (e.g., Evansella clarkii cytochrome c outer-surface capacitor) should be curated as **taxon-limited** or “candidate” edges unless replicated across multiple alkaliphile lineages (goto2022differencesinbioenergetic pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates)

1. **Krulwich TA, Sachs G, Padan E.** Molecular aspects of bacterial pH sensing and homeostasis. *Nature Reviews Microbiology.* **May 2011**. DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22, krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof media 64f40140)
2. **Wang Q, Qiao M, Song J.** Characterization of Two Na+(K+, Li+)/H+ Antiporters from *Natronorubrum daqingense*. *International Journal of Molecular Sciences.* **Jun 2023**. DOI: **10.3390/ijms241310786**. URL: https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8, wang2023characterizationoftwo pages 10-12)
3. **Thompson J et al.** Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. *Frontiers in Microbiology.* **Jul 2023**. DOI: **10.3389/fmicb.2023.1179857**. URL: https://doi.org/10.3389/fmicb.2023.1179857 (thompson2023insightsintothe pages 1-2, thompson2023insightsintothe pages 2-3)
4. **Khomyakova MA et al.** Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens… *Frontiers in Microbiology.* **Oct 2023**. DOI: **10.3389/fmicb.2023.1233691**. URL: https://doi.org/10.3389/fmicb.2023.1233691 (khomyakova2023phenotypicandgenomic pages 1-2)
5. **Xing Q et al.** The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy… *Applied and Environmental Microbiology.* **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21)
6. **de Jong SI et al.** Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures. *Frontiers in Microbiology.* **Oct 2024**. DOI: **10.3389/fmicb.2024.1468929**. URL: https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 1-2)
7. **Wadhawan G, Kalra A, Gupta A.** Potential of halophiles and alkaliphiles in bioremediation of azo dyes-laden textile wastewater: a review. *3 Biotech.* **Aug 2024**. DOI: **10.1007/s13205-024-04036-0**. URL: https://doi.org/10.1007/s13205-024-04036-0 (wadhawan2024potentialofhalophiles pages 1-2, wadhawan2024potentialofhalophiles pages 7-8, wadhawan2024potentialofhalophiles pages 10-11, wadhawan2024potentialofhalophiles pages 6-7)
8. **Goto T et al.** Differences in bioenergetic metabolism of obligately alkaliphilic Bacillaceae under high pH depend on the aeration conditions. *Frontiers in Microbiology.* **Mar 2022**. DOI: **10.3389/fmicb.2022.842785**. URL: https://doi.org/10.3389/fmicb.2022.842785 (goto2022differencesinbioenergetic pages 1-2)
9. **Adetunji AI, Erasmus M.** Unraveling the Potentials of Extremophiles in Bioextraction of Valuable Metals from Industrial Solid Wastes: An Overview. *Minerals.* **Aug 2024**. DOI: **10.3390/min14090861**. URL: https://doi.org/10.3390/min14090861 (adetunji2024unravelingthepotentials pages 19-20)
10. **Wang Y et al.** Saline-Alkali Soil Property Improved by the Synergistic Effects of *Priestia aryabhattai* JL-5… *International Journal of Molecular Sciences.* **Apr 2023**. DOI: **10.3390/ijms24097737**. URL: https://doi.org/10.3390/ijms24097737 (wang2023salinealkalisoilproperty pages 1-2)
11. **Rekadwad BN et al.** Extremophiles: the species that evolve and survive under hostile conditions. *3 Biotech.* **Aug 2023**. DOI: **10.1007/s13205-023-03733-6**. URL: https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 8-10)


References

1. (khomyakova2023phenotypicandgenomic pages 1-2): Maria A. Khomyakova, Alexander Y. Merkel, Alexander I. Slobodkin, and Dimitry Y. Sorokin. Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus methanocrinis gen.nov. within the family methanotrichaceae. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1233691, doi:10.3389/fmicb.2023.1233691. This article has 13 citations and is from a peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 20-22): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 19-21): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (wang2023characterizationoftwo pages 7-8): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

8. (krulwich2011molecularaspectsof media 64f40140): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

9. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 7 citations and is from a peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (thompson2023insightsintothe pages 1-2): Jaclyn Thompson, Casey Barr, Lydia Babcock-Adams, Lina Bird, Eugenio La Cava, Arkadiy Garber, Yuichi Hongoh, Mark Liu, Kenneth H. Nealson, Akihiro Okamoto, Daniel Repeta, Shino Suzuki, Clarissa Tacto, Michelle Tashjian, and Nancy Merino. Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1179857, doi:10.3389/fmicb.2023.1179857. This article has 7 citations and is from a peer-reviewed journal.

12. (wadhawan2024potentialofhalophiles pages 1-2): Gunisha Wadhawan, Anuja Kalra, and Anshu Gupta. Potential of halophiles and alkaliphiles in bioremediation of azo dyes-laden textile wastewater: a review. 3 Biotech, 14 9:194, Aug 2024. URL: https://doi.org/10.1007/s13205-024-04036-0, doi:10.1007/s13205-024-04036-0. This article has 8 citations and is from a peer-reviewed journal.

13. (wadhawan2024potentialofhalophiles pages 7-8): Gunisha Wadhawan, Anuja Kalra, and Anshu Gupta. Potential of halophiles and alkaliphiles in bioremediation of azo dyes-laden textile wastewater: a review. 3 Biotech, 14 9:194, Aug 2024. URL: https://doi.org/10.1007/s13205-024-04036-0, doi:10.1007/s13205-024-04036-0. This article has 8 citations and is from a peer-reviewed journal.

14. (wadhawan2024potentialofhalophiles pages 10-11): Gunisha Wadhawan, Anuja Kalra, and Anshu Gupta. Potential of halophiles and alkaliphiles in bioremediation of azo dyes-laden textile wastewater: a review. 3 Biotech, 14 9:194, Aug 2024. URL: https://doi.org/10.1007/s13205-024-04036-0, doi:10.1007/s13205-024-04036-0. This article has 8 citations and is from a peer-reviewed journal.

15. (wadhawan2024potentialofhalophiles pages 6-7): Gunisha Wadhawan, Anuja Kalra, and Anshu Gupta. Potential of halophiles and alkaliphiles in bioremediation of azo dyes-laden textile wastewater: a review. 3 Biotech, 14 9:194, Aug 2024. URL: https://doi.org/10.1007/s13205-024-04036-0, doi:10.1007/s13205-024-04036-0. This article has 8 citations and is from a peer-reviewed journal.

16. (wang2023salinealkalisoilproperty pages 1-2): Yujue Wang, Yan Wang, Qian Zhang, Hangzhe Fan, Xinyu Wang, Jianan Wang, Ying Zhou, Zhanyu Chen, Fengjie Sun, and Xiyan Cui. Saline-alkali soil property improved by the synergistic effects of priestia aryabhattai jl-5, staphylococcus pseudoxylosus xw-4, leymus chinensis and soil microbiota. International Journal of Molecular Sciences, 24:7737, Apr 2023. URL: https://doi.org/10.3390/ijms24097737, doi:10.3390/ijms24097737. This article has 20 citations.

17. (adetunji2024unravelingthepotentials pages 19-20): Adegoke Isiaka Adetunji and Mariana Erasmus. Unraveling the potentials of extremophiles in bioextraction of valuable metals from industrial solid wastes: an overview. Minerals, 14:861, Aug 2024. URL: https://doi.org/10.3390/min14090861, doi:10.3390/min14090861. This article has 7 citations.

18. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

19. (wang2023characterizationoftwo pages 10-12): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

20. (thompson2023insightsintothe pages 2-3): Jaclyn Thompson, Casey Barr, Lydia Babcock-Adams, Lina Bird, Eugenio La Cava, Arkadiy Garber, Yuichi Hongoh, Mark Liu, Kenneth H. Nealson, Akihiro Okamoto, Daniel Repeta, Shino Suzuki, Clarissa Tacto, Michelle Tashjian, and Nancy Merino. Insights into the physiological and genomic characterization of three bacterial isolates from a highly alkaline, terrestrial serpentinizing system. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1179857, doi:10.3389/fmicb.2023.1179857. This article has 7 citations and is from a peer-reviewed journal.

21. (rekadwad2023extremophilesthespecies pages 8-10): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.