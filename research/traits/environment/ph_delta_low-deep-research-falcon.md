---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:03:56.218018'
end_time: '2026-06-18T00:27:01.071230'
duration_seconds: 1384.85
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta low
  trait_identifier: METPO:1000474
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 1\u20132 pH units, characteristic of organisms with limited pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_1_2
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports limited pH-homeostasis flexibility as the basis for a narrow pH-tolerance
    breadth.)'
  causal_graph_summary: 'ph_delta_low_limited_breadth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta low
- **METPO identifier:** METPO:1000474
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 1–2 pH units, characteristic of organisms with limited pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_1_2
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports limited pH-homeostasis flexibility as the basis for a narrow pH-tolerance breadth.)
- **Existing causal graph summary:** ph_delta_low_limited_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_low.yaml`.

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
- **Trait label:** pH delta low
- **METPO identifier:** METPO:1000474
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 1–2 pH units, characteristic of organisms with limited pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_1_2
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports limited pH-homeostasis flexibility as the basis for a narrow pH-tolerance breadth.)
- **Existing causal graph summary:** ph_delta_low_limited_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_low.yaml`.

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


# Research report: Microbial trait “pH delta low” (METPO:1000474) as a candidate TraitMech causal graph

## 1) Scope summary (trait meaning, boundaries, distinctions)

**Trait definition (operational):** *pH delta low* denotes a **narrow growth-supporting pH breadth (~1–2 pH units)**—i.e., organisms whose **growth** (not merely survival) is supported only across a small external pH interval (METPO:1000474). A central mechanistic interpretation is that such narrow breadth reflects **limited flexibility of cytoplasmic pH homeostasis**: microbes must keep internal pH within a growth-permissive window, and if the homeostatic machinery (transport, buffering, envelope properties, regulation, energy supply) cannot compensate outside a narrow external range, growth ceases. This framing is consistent with authoritative pH-homeostasis literature describing pH tolerance as dependent on mechanisms that allow growth “at external pH values that are outside the cytoplasmic pH range they must maintain for growth.” (krulwich2011molecularaspectsof pages 3-5).

**Distinguish from nearby traits:**
- **pH preference/optimum** vs **pH breadth**: many taxa have **narrow pH optima (often within ~1 pH unit)** and “putative pH preferences” that cluster strongly between pH 6–8 (Ramoneda et al. 2023) (ramoneda2023buildingagenomebased pages 6-7). A narrow optimum does not always imply a narrow growth breadth, but it often co-occurs.
- **Growth vs survival:** *pH delta low* should be curated from **growth-supporting** pH range, because some organisms can **survive** extreme acidity without growing (e.g., E. coli can “survive for several hours at pH = 2 but cannot grow”) (li2024responseofescherichia pages 1-2).

**Boundary/assay-sensitive cases:**
- **Weak-acid effects**: weak acids can cross membranes in uncharged form and distort ΔpH and cytoplasmic pH, affecting apparent tolerance (krulwich2011molecularaspectsof pages 3-5).
- **Measurement heterogeneity and method choice:** cytoplasmic pH regulation is often heterogeneous at the single-cell level and can be influenced by probe loading/expression and perturbants (e.g., CCCP/nigericin used to collapse gradients) (perezrodriguez2024methodsforstudying pages 12-13, atasoy2024methodsforstudying pages 36-37).

## 2) Current understanding: key concepts and definitions

### 2.1 Cytoplasmic pH homeostasis as the proximate constraint
The dominant conceptual model is that microbes maintain growth by keeping **cytoplasmic pH** within a functional range despite external pH variation. This is governed by the **proton motive force (PMF = Δψ + ΔpH)**, whose architecture and directionality can shift under pH stress (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 14-15). Because PMF is simultaneously an energy currency and a pH-control mechanism, organisms with limited energetic capacity or transporter repertoire may have a narrower workable pH range.

### 2.2 Mechanism classes that expand vs constrain pH tolerance breadth
Mechanistic determinants recurrently implicated across bacteria/archaea include:
- **Active transport:** proton pumps and proton-coupled ATPases; cation/proton antiporters that exchange Na+ or K+ for H+ (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 12-14).
- **Metabolic proton consumption/production:** amino-acid decarboxylation (e.g., GadB) and related fermentations (krulwich2011molecularaspectsof pages 5-6, li2024responseofescherichia pages 2-4).
- **Envelope control of proton leak:** membrane lipid/porin composition and specialized archaeal lipids can drastically reduce passive proton permeability (chong2024archaeamembranesin pages 2-3, krulwich2011molecularaspectsof pages 17-18).
- **Surface polymers / proton capture:** S-layers and acidic cell wall polymers can influence near-surface proton availability (krulwich2011molecularaspectsof pages 6-8, yao2023howmethanotrophsrespond pages 5-7).

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Genome-informed pH preference prediction and gene associations (2023)
Ramoneda et al. (Science Advances, 2023) integrated multi-environment distribution data and genomes to infer bacterial pH preferences and identify gene associations. They found **332 gene types** significantly associated with pH in ≥2 datasets and **56 gene types** consistent across ≥3 datasets, including multiple transport and buffering candidates (e.g., **KdpACD**, **Na+/H+ antiporters**, **urease-related genes**, amino-acid decarboxylase-related domains) (ramoneda2023buildingagenomebased pages 3-5). They also emphasized that **no gene type was significant across all datasets**, highlighting habitat/taxon specificity—important for curation rules (ramoneda2023buildingagenomebased pages 3-5).

### 3.2 Methods + single-cell cytoplasmic pH measurements (2024)
Atasoy et al. (FEMS Microbiology Reviews, 2024) surveyed modern approaches for acid stress responses, including **ratiometric reporters (pHluorin2)** and multi-omics and genetic screens to identify tolerance determinants (atasoy2024methodsforstudying pages 36-37, atasoy2024methodsforstudying pages 18-19). Complementary methods summaries discuss tools and confounders: E. coli pHi trajectories upon acidification (drop and recovery), and use of uncouplers/ionophores (benzoate, CCCP, nigericin) as experimental controls (perezrodriguez2024methodsforstudying pages 12-13).

### 3.3 Quantitative trade-offs in acid-resistance regulation (2024)
Gorelik et al. (Journal of Bacteriology, 2024) quantified a key evolutionary/physiological trade-off: **disrupting csrA** derepresses an acid resistance regulatory cascade (EvgA–YdeO–GadE), leading to **markedly improved survival under extreme acidity** but **impaired growth at mildly acidic pH** (growth defect at pH ≤6) (gorelik2024multitierregulationof pages 3-5). Example effect sizes: ~12-fold higher survival at pH 2.5 with glutamate shock; ~100-fold higher survival after pH 5.5 preadaptation without glutamate; ~55-fold better survival in simulated fasted-stomach media (gorelik2024multitierregulationof pages 3-5).

### 3.4 Quantitative membrane proton permeability limits in archaea (2024)
Chong (Frontiers in Biophysics, 2024) synthesized evidence that thermoacidophiles maintain near-neutral intracellular pH partly by **extremely low passive proton permeability** of archaeal tetraether membranes. Liposome assays showed **PLFE liposomes** with proton permeability **~0.3–0.5 ×10−8 cm s−1 at 65–82°C** versus **~3–9 ×10−8 cm s−1** for egg yolk PC liposomes, with minimal temperature dependence (chong2024archaeamembranesin pages 2-3). Such data quantify a physical constraint that can plausibly differentiate narrow vs broad tolerance breadth.

## 4) Current applications and real-world implementations

### 4.1 Bioprocessing and industrial fermentation
A 2024 review highlights that in high-glucose fermentation, organic acid accumulation can drop medium pH below 5 and inhibit growth; it further notes that **~50 g/L organic acids (pKa 3–5)** could reduce environmental pH to **~2.0** without alkali intervention, motivating engineering of acid-resistant chassis to reduce neutralization costs and expand operating pH windows (li2024responseofescherichia pages 1-2).

### 4.2 Environmental/biogeochemical and engineered microbiomes
pH tolerance breadth and preference are used to interpret and predict microbial distributions across soil and freshwater pH gradients, and can inform selection of inoculants and cultivation strategies by predicting pH preference from genomes (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 6-7). In engineered systems, exogenous compounds (e.g., putrescine) can modulate pH stress adaptability through effects on membrane permeability and proton-consuming pathways, suggesting interventions for biofilm/activated sludge control (jiang2024exogenousputrescineplays pages 1-2).

## 5) Expert opinions and authoritative analysis

**Authoritative consensus (still current):** Krulwich, Sachs & Padan (Nature Reviews Microbiology, 2011; cited >1000×) articulate that pH tolerance relies on a network of **PMF management**, **antiporters**, **ATPases**, **metabolic proton consumption**, and **envelope properties**; extremophiles often express these constitutively at energetic cost (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 5-6). This framework remains the dominant conceptual model and is repeatedly echoed in 2023–2024 reviews and studies on pH stress, measurement, and comparative physiology (atasoy2024methodsforstudying pages 36-37, yao2023howmethanotrophsrespond pages 5-7).

**Modern perspective (2023–2024):** Recent work adds that (i) **genome content can be predictive of pH preference** but is strongly **habitat-conditional** (ramoneda2023buildingagenomebased pages 3-5); (ii) **regulatory trade-offs** (growth vs stress survival) can explain why potent homeostasis systems are not always constitutively active, supporting narrow growth breadth phenotypes in some contexts (gorelik2024multitierregulationof pages 3-5).

## 6) Candidate nodes grouped by type (curation-oriented)

| Group | Proposed node label | Brief description | Example evidence source(s) with DOI | Suggested ontology grounding |
|---|---|---|---|---|
| Phenotype/trait | Candidate nodes for pH delta low causal graph | Narrow growth-supporting pH breadth of ~1–2 pH units; reflects limited flexibility of pH homeostasis rather than a specific optimum pH (ramoneda2023buildingagenomebased pages 6-7, krulwich2011molecularaspectsof pages 3-5) | Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998; Krulwich et al. 2011, DOI:10.1038/nrmicro2549 | METPO:1000474 |
| Phenotype/trait | limited cytoplasmic pH homeostasis flexibility | Restricted ability to maintain growth-permissive intracellular pH across changing external pH | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Atasoy et al. 2024, DOI:10.1093/femsre/fuae015 (krulwich2011molecularaspectsof pages 3-5, atasoy2024methodsforstudying pages 36-37) | GO:0006885 |
| Environmental factors | external pH | Environmental hydrogen ion condition to which growth breadth is measured | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Li et al. 2024, DOI:10.3390/microorganisms12091774 (krulwich2011molecularaspectsof pages 3-5, li2024responseofescherichia pages 1-2) | label-only |
| Environmental factors | low extracellular pH | Acidic environment challenging neutralophiles and activating acid-resistance systems | Li et al. 2024, DOI:10.3390/microorganisms12091774; Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (li2024responseofescherichia pages 2-4, gorelik2024multitierregulationof pages 3-5) | ENVO:01000324 |
| Environmental factors | high extracellular pH | Alkaline environment requiring proton capture and inward proton-coupled antiport | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164 (krulwich2011molecularaspectsof pages 12-14, yao2023howmethanotrophsrespond pages 5-7) | label-only |
| Environmental factors | sodium ion | Cation coupled to Na+/H+ antiport and alkaline pH homeostasis | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14) | CHEBI:29101 |
| Environmental factors | potassium ion | Cation involved in K+ uptake and K+/H+ antiport contributing to pH homeostasis | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164 (krulwich2011molecularaspectsof pages 5-6, yao2023howmethanotrophsrespond pages 5-7) | CHEBI:29103 |
| Environmental factors | weak organic acids | Uncharged weak acids cross membranes and perturb ΔpH, affecting apparent tolerance breadth | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Li et al. 2024, DOI:10.3390/microorganisms12091774 (krulwich2011molecularaspectsof pages 3-5, li2024responseofescherichia pages 1-2) | CHEBI:35801 |
| Assay/experimental factors | growth-supporting pH breadth assay | Trait should be curated from growth range, not survival-only assays | Li et al. 2024, DOI:10.3390/microorganisms12091774; Perez-Rodriguez et al. 2024, no DOI in snippet (li2024responseofescherichia pages 1-2, perezrodriguez2024methodsforstudying pages 12-13) | label-only |
| Assay/experimental factors | cytoplasmic pH measurement | Measurement of intracellular pH using fluorescent reporters or related methods to infer homeostasis limits | Atasoy et al. 2024, DOI:10.1093/femsre/fuae015; Perez-Rodriguez et al. 2024, no DOI in snippet (atasoy2024methodsforstudying pages 36-37, perezrodriguez2024methodsforstudying pages 37-38) | label-only |
| Assay/experimental factors | pHluorin / pHluorin2 reporter | Ratiometric GFP-based biosensors for intracellular pH | Atasoy et al. 2024, DOI:10.1093/femsre/fuae015; Perez-Rodriguez et al. 2024, no DOI in snippet (atasoy2024methodsforstudying pages 36-37, perezrodriguez2024methodsforstudying pages 12-13) | label-only |
| Assay/experimental factors | 31P NMR intracellular pH assay | Method for measuring cytoplasmic pH and pH responses | Perez-Rodriguez et al. 2024, no DOI in snippet (perezrodriguez2024methodsforstudying pages 39-40) | label-only |
| Assay/experimental factors | proton gradient collapse control | Use of benzoate, CCCP, or nigericin to perturb ΔpH during pH homeostasis assays | Perez-Rodriguez et al. 2024, no DOI in snippet (perezrodriguez2024methodsforstudying pages 12-13) | CHEBI:5292 / CHEBI:3423 / CHEBI:75355 |
| Assay/experimental factors | liposome proton permeability assay | Reconstituted membrane assay using pH-sensitive fluorophores to quantify passive proton leak | Chong 2024, DOI:10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 2-3) | label-only |
| Cellular processes | cytoplasmic pH homeostasis | Maintenance of intracellular pH in a growth-permissive range | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Atasoy et al. 2024, DOI:10.1093/femsre/fuae015 (krulwich2011molecularaspectsof pages 3-5, atasoy2024methodsforstudying pages 36-37) | GO:0006885 |
| Cellular processes | proton motive force | Composite of Δψ and ΔpH that powers and constrains pH homeostasis | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 14-15) | GO:0015985 |
| Cellular processes | proton efflux | Active removal of excess H+ during acid stress | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Jiang et al. 2024, DOI:10.1128/aem.00569-24 (krulwich2011molecularaspectsof pages 5-6, jiang2024exogenousputrescineplays pages 1-2) | GO:1990574 |
| Cellular processes | proton influx / proton capture | Inward proton movement important under alkaline stress, including capture near the surface | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164 (krulwich2011molecularaspectsof pages 12-14, yao2023howmethanotrophsrespond media 3be20d84) | label-only |
| Cellular processes | amino acid decarboxylation-based acid resistance | Proton-consuming decarboxylation cycles that buffer cytoplasm under acid stress | Li et al. 2024, DOI:10.3390/microorganisms12091774; Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (li2024responseofescherichia pages 2-4, krulwich2011molecularaspectsof pages 5-6) | GO:0046392 |
| Cellular processes | membrane proton permeability limitation | Reduced passive H+ leak through membrane as a determinant of pH tolerance | Chong 2024, DOI:10.3389/frbis.2023.1338019; Jiang et al. 2024, DOI:10.1128/aem.00569-24 (chong2024archaeamembranesin pages 2-3, jiang2024exogenousputrescineplays pages 1-2) | GO:1902600 |
| Cellular processes | oxidative phosphorylation supporting H+ transport | Respiratory energy generation supports ATPase activity and proton transport | Jiang et al. 2024, DOI:10.1128/aem.00569-24; Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164 (jiang2024exogenousputrescineplays pages 1-2, yao2023howmethanotrophsrespond pages 5-7) | GO:0006119 |
| Transporters/complexes | F1Fo-ATPase / F0F1-ATPase | ATP-driven or ATP-synthesizing proton-translocating ATPase contributing to pH homeostasis | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Li et al. 2024, DOI:10.3390/microorganisms12091774 (krulwich2011molecularaspectsof pages 5-6, li2024responseofescherichia pages 2-4) | GO:0046933 |
| Transporters/complexes | NhaA Na+/H+ antiporter | Canonical electrogenic Na+/H+ antiporter with steep pH-dependent activation | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 8-9) | KEGG:K03313 |
| Transporters/complexes | Mrp Na+/H+ antiporter complex | Multi-subunit antiporter essential for alkaline pH homeostasis in alkaliphiles | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998 (krulwich2011molecularaspectsof pages 12-14, ramoneda2023buildingagenomebased pages 3-5) | KEGG:K05571 |
| Transporters/complexes | KdpACD potassium pump | K+ uptake system associated with low-pH preferring taxa | Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 3-5) | KEGG:K01546 / K01547 / K01548 |
| Transporters/complexes | GadC glutamate/GABA antiporter | Exchanges extracellular glutamate for intracellular GABA in glutamate-dependent acid resistance | Li et al. 2024, DOI:10.3390/microorganisms12091774; Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (li2024responseofescherichia pages 2-4, gorelik2024multitierregulationof pages 1-3) | KEGG:K03372 |
| Transporters/complexes | AdiC arginine/agmatine antiporter | Antiporter in arginine-dependent acid resistance | Li et al. 2024, DOI:10.3390/microorganisms12091774 (li2024responseofescherichia pages 4-5) | KEGG:K03294 |
| Transporters/complexes | CadB lysine/cadaverine antiporter | Antiporter in lysine-dependent acid resistance | Li et al. 2024, DOI:10.3390/microorganisms12091774 (li2024responseofescherichia pages 4-5) | KEGG:K03400 |
| Transporters/complexes | UreI urea channel | pH-gated channel enabling acid acclimation in H. pylori | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 8-9) | KEGG:K03187 |
| Transporters/complexes | primary proton pumps (respiratory complexes I/III/IV) | Respiratory chain components that generate PMF and support pH regulation | Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164; Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (yao2023howmethanotrophsrespond pages 5-7, krulwich2011molecularaspectsof pages 5-6) | GO:0015992 |
| Enzymatic buffering systems | GadA glutamate decarboxylase | Proton-consuming glutamate decarboxylase in GDAR | Li et al. 2024, DOI:10.3390/microorganisms12091774; Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (li2024responseofescherichia pages 2-4, gorelik2024multitierregulationof pages 1-3) | EC:4.1.1.15 |
| Enzymatic buffering systems | GadB glutamate decarboxylase | Second glutamate decarboxylase isozyme in GDAR | Li et al. 2024, DOI:10.3390/microorganisms12091774; Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (li2024responseofescherichia pages 2-4, gorelik2024multitierregulationof pages 3-5) | EC:4.1.1.15 |
| Enzymatic buffering systems | YbaS glutaminase | Produces glutamate and ammonia, complementing glutamate decarboxylation during acid stress | Li et al. 2024, DOI:10.3390/microorganisms12091774 (li2024responseofescherichia pages 2-4) | EC:3.5.1.2 |
| Enzymatic buffering systems | AdiA arginine decarboxylase | Proton-consuming enzyme in arginine-dependent acid resistance | Li et al. 2024, DOI:10.3390/microorganisms12091774 (li2024responseofescherichia pages 4-5) | EC:4.1.1.19 |
| Enzymatic buffering systems | CadA lysine decarboxylase | Proton-consuming enzyme in lysine-dependent acid resistance | Li et al. 2024, DOI:10.3390/microorganisms12091774; Atasoy et al. 2024, DOI:10.1093/femsre/fuae015 (li2024responseofescherichia pages 4-5, atasoy2024methodsforstudying pages 36-37) | EC:4.1.1.18 |
| Enzymatic buffering systems | urease | Urea hydrolysis yields NH3/NH4+ and CO2 for acid acclimation | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Ramoneda et al. 2023, DOI:10.1126/sciadv.adf8998 (krulwich2011molecularaspectsof pages 27-28, ramoneda2023buildingagenomebased pages 3-5) | EC:3.5.1.5 |
| Enzymatic buffering systems | carbonic anhydrase | Works with urease system to maintain periplasmic pH in acid | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 27-28) | EC:4.2.1.1 |
| Enzymatic buffering systems | malolactic fermentation | Metabolic proton-consuming strategy cited as pH homeostasis mechanism | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6) | MetaCyc:PWY-5265 |
| Envelope/membrane features | saturated membrane fatty acids | Reduced proton permeability associated with acidophily | Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164; Jiang et al. 2024, DOI:10.1128/aem.00569-24 (yao2023howmethanotrophsrespond pages 5-7, jiang2024exogenousputrescineplays pages 1-2) | label-only |
| Envelope/membrane features | cyclopropane fatty acids | Membrane modification reducing H+ permeability | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Li et al. 2024, DOI:10.3390/microorganisms12091774 (krulwich2011molecularaspectsof pages 17-18, li2024responseofescherichia pages 5-7) | label-only |
| Envelope/membrane features | archaeal bipolar tetraether lipids | Tetraether membrane lipids that strongly reduce passive proton leak | Chong 2024, DOI:10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 2-3) | label-only |
| Envelope/membrane features | cyclopentane ring-rich archaeal lipids | Membrane structural feature associated with lower proton permeability | Chong 2024, DOI:10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 2-3) | label-only |
| Envelope/membrane features | acidic secondary cell wall polymers | Surface polymers proposed to retain/capture protons near the cell surface | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 27-28) | label-only |
| Envelope/membrane features | S-layer / SlpA | Surface layer implicated in proton capture and rapid alkaline adaptation | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Yao et al. 2023, DOI:10.3389/fmicb.2022.1034164 (krulwich2011molecularaspectsof pages 6-8, yao2023howmethanotrophsrespond media 3be20d84) | GO:0097489 |
| Envelope/membrane features | porin composition | Porin remodeling can alter proton leakage and acid-resistance substrate entry | Krulwich et al. 2011, DOI:10.1038/nrmicro2549; Li et al. 2024, DOI:10.3390/microorganisms12091774 (krulwich2011molecularaspectsof pages 5-6, li2024responseofescherichia pages 5-7) | GO:0015288 |
| Regulators | RpoS (σS) | Global stress sigma factor required for sustained acid tolerance and AR1 regulation | Li et al. 2024, DOI:10.3390/microorganisms12091774; Perez-Rodriguez et al. 2024, no DOI in snippet (li2024responseofescherichia pages 2-4, perezrodriguez2024methodsforstudying pages 39-40) | KEGG:K03088 |
| Regulators | CsrA | Post-transcriptional repressor of acid-stress circuitry; trade-off between growth and acid survival | Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (gorelik2024multitierregulationof pages 3-5, gorelik2024multitierregulationof pages 1-3) | KEGG:K03546 |
| Regulators | EvgA | Top-tier response regulator activating acid resistance circuitry under mild acidity | Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (gorelik2024multitierregulationof pages 3-5, gorelik2024multitierregulationof pages 1-3) | KEGG:K07665 |
| Regulators | EvgS | Sensor kinase upstream of EvgA in acid-responsive signaling | Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (gorelik2024multitierregulationof pages 3-5, gorelik2024multitierregulationof pages 24-24) | KEGG:K07664 |
| Regulators | YdeO | Intermediate regulator in the EvgA-YdeO-GadE acid resistance branch | Gorelik et al. 2024, DOI:10.1128/jb.00354-23 (gorelik2024multitierregulationof pages 3-5, gorelik2024multitierregulationof pages 24-24) | label-only |
| Regulators | GadE | Central activator required for GDAR expression | Gorelik et al. 2024, DOI:10.1128/jb.00354-23; Li et al. 2024, DOI:10.3390/microorganisms12091774 (gorelik2024multitierregulationof pages 3-5, li2024responseofescherichia pages 4-5) | KEGG:K12340 |
| Regulators | GadX | Transcriptional regulator in Gad acid response network | Li et al. 2024, DOI:10.3390/microorganisms12091774 (li2024responseofescherichia pages 4-5) | KEGG:K12341 |
| Regulators | GadW | Transcriptional regulator in Gad acid response network | Li et al. 2024, DOI:10.3390/microorganisms12091774; Atasoy et al. 2024, DOI:10.1093/femsre/fuae015 (li2024responseofescherichia pages 4-5, atasoy2024methodsforstudying pages 36-37) | label-only |
| Regulators | GadY | Small RNA regulator modulating Gad network | Li et al. 2024, DOI:10.3390/microorganisms12091774; Atasoy et al. 2024, DOI:10.1093/femsre/fuae015 (li2024responseofescherichia pages 4-5, atasoy2024methodsforstudying pages 36-37) | label-only |
| Regulators | CadC | Acid-response regulator controlling cadBA system | Li et al. 2024, DOI:10.3390/microorganisms12091774; Paterson et al. 2023 noted in search output but not used here (li2024responseofescherichia pages 4-5) | KEGG:K07729 |
| Regulators | ArsRS two-component system | pH-responsive regulatory system controlling acid acclimation in H. pylori | Krulwich et al. 2011, DOI:10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 17-18) | label-only |


*Table: This table lists candidate mechanistic and contextual nodes for a TraitMech causal graph of the narrow microbial pH breadth trait. It groups evidence-backed node ideas by biological role and includes suggested ontology grounding where supported by the cited evidence.*

## 7) Evidence-backed causal edges (triples) for TraitMech curation

| Subject node | Predicate | Object node | Reference (first author year, DOI, URL, pub date) | Supporting snippet/quote (verbatim from evidence snippets) | Notes for curation (mechanistic rationale; whether edge is general vs taxon-specific; mark uncertain if inferred) |
|---|---|---|---|---|---|
| external pH stress | challenges | cytoplasmic pH homeostasis | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "Diverse mechanisms for pH sensing and cytoplasmic pH homeostasis enable most bacteria to tolerate or grow at external pH values that are outside the cytoplasmic pH range they must maintain for growth." (krulwich2011molecularaspectsof pages 3-5) | Core framing edge for the trait. Supports the idea that limited homeostasis capacity underlies narrow growth-supporting pH breadth. General across bacteria. |
| proton motive force (PMF) architecture | determines | pH homeostasis capacity | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "A central concept is the proton-motive force (PMF), composed of Δψ (electrical potential) and ΔpH (proton gradient); different bacteria tune the relative magnitudes and even reverse the orientation of these components under pH stress." (krulwich2011molecularaspectsof pages 3-5) | Strong general mechanistic edge. Good candidate parent mechanism linking to narrow pH breadth via limited flexibility of PMF balancing. |
| weak organic acids | cross membrane and perturb | ΔpH / cytoplasmic pH | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "Membrane permeability to weak acids/bases underlies measurements of ΔpH because uncharged forms cross membranes and become trapped when charged" (krulwich2011molecularaspectsof pages 3-5) | Supports environmental/chemical factor edge. Relevant to assay and ecology; weak acids can narrow apparent growth breadth. General, but partly assay-contextual. |
| electrogenic Na+/H+ antiport | supports | alkaline pH homeostasis | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "Under alkaline stress, inward proton transport through up-regulated cation/proton antiporters is crucial; a substantial membrane potential (Δψ) drives electrogenic antiport." (krulwich2011molecularaspectsof pages 5-6) | Strong general edge connecting transporter-mediated proton uptake to tolerance at high pH; failure of this capacity is relevant to narrow pH breadth. |
| NhaA Na+/H+ antiporter | mediates | electrogenic Na+/H+ antiport | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "E. coli NhaA = 2H+/1Na+" (krulwich2011molecularaspectsof pages 5-6) | Canonical mechanistic edge; stoichiometry directly supports H+ import during alkaline stress. Taxon exemplified by E. coli but widely used as reference antiporter. |
| external alkaline pH increase | activates | NhaA Na+/H+ antiporter | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "shows steep pH-dependent activation (≈1,000-fold between pHout 6.5 and 8.5)" (krulwich2011molecularaspectsof pages 6-8) | Strong edge for pH sensing/response. Good for explaining threshold-like failure outside tolerated range. Likely specific to NhaA-class systems; not universal to all taxa. |
| Mrp antiporter complex | is essential for | alkaline pH homeostasis | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "In extreme alkaliphiles, Na+/H+ antiporter-dependent pH homeostasis is dominant: multi-subunit, hetero-oligomeric Mrp antiporters (all Mrp proteins required) are essential for alkaline homeostasis" (krulwich2011molecularaspectsof pages 12-14) | Strong but mainly from alkaliphile systems; use as mechanism for broad/high-pH tolerance, with loss/absence plausibly contributing to pH delta low. Taxon/ecology-specific. |
| F1Fo-ATPase | contributes to | cytoplasmic pH homeostasis | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "respiratory chain complexes and proton-coupled ATPases generate or use the proton-motive force (PMF) to expel or import H+" (krulwich2011molecularaspectsof pages 5-6) | General edge. Appropriate higher-level curation when organism-specific ATPase directionality is unknown. |
| F0F1-ATPase hydrolysis | consumes | intracellular H+ | Li 2024, DOI:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774, Aug 2024 | "F0F1-ATPase associates with AR1 and, under acid stress, shifts to hydrolyze ATP to consume intracellular H+ to maintain homeostasis." (li2024responseofescherichia pages 2-4) | Acid-stress-specific, mostly E. coli-focused but mechanistically clear. Strong edge for low-pH tolerance breadth. |
| glutamate decarboxylation system (GadA/GadB/GadC) | consumes | H+ | Li 2024, DOI:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774, Aug 2024 | "GadA and GadB (glutamate decarboxylases) plus the antiporter GadC decarboxylate intracellular glutamate to GABA+CO2, consuming H+" (li2024responseofescherichia pages 2-4) | Strong acid-resistance edge. Mostly enteric model systems, so should be marked taxon-specific if curated as direct trait mechanism rather than broad candidate. |
| glutamine deamidation + glutamate decarboxylation | consumes | two H+ per cycle | Li 2024, DOI:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774, Aug 2024 | "glutamine deamidation plus glutamate decarboxylation can together consume two H+ per cycle" (li2024responseofescherichia pages 2-4) | Strong mechanistic edge for enhanced acid resistance. Useful as a pathway-level node if enzyme-level detail is too specific. Taxon-specific evidence. |
| arginine-dependent acid resistance (AdiA/AdiC) | mitigates | extreme acid stress | Li 2024, DOI:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774, Aug 2024 | "AR3 (Adi) is arginine-dependent and can \"effectively mitigated at pH 2.5,\" involving AdiA (decarboxylase) and AdiC (antiporter)" (li2024responseofescherichia pages 4-5) | Supports decarboxylation-cycle mechanism broadening low-pH tolerance. Wording from review is imperfect, but mechanistic meaning is clear. Taxon-specific. |
| lysine-dependent acid resistance (CadA/CadB) | consumes | H+ | Li 2024, DOI:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774, Aug 2024 | "AR4 (Cad) is lysine-dependent, active around \"pH 5.8,\" with CadA/CadB and CadC regulation; CadA decarboxylates lysine to consume H+." (li2024responseofescherichia pages 4-5) | Good mechanistic edge with useful activation range. Mainly enteric bacteria; mark taxon-specific if curated directly. |
| saturated membrane fatty acids | reduce | proton permeability | Yao 2023, DOI:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164, Jan 2023 | "acidophilic verrucomicrobial methanotroph membranes are ‘almost made up of saturated fatty acids’ (minimizing proton permeability)" (yao2023howmethanotrophsrespond pages 5-7) | Strong edge for membrane-level limitation of proton leak. Evidence is from methanotrophs, so taxon-specific exemplar but broadly plausible. |
| archaeal bipolar tetraether lipids | maintain | low passive proton permeability | Chong 2024, DOI:10.3389/frbis.2023.1338019, https://doi.org/10.3389/frbis.2023.1338019, Jan 2024 | "As such, a low passive proton permeability and a near neutral intracellular pH can be maintained" (chong2024archaeamembranesin pages 2-3) | Strong edge for archaeal acid tolerance; relevant negative inference is that lack of such low-leak membranes may constrain breadth. Archaeal/tetraether-specific. |
| cyclopentane rings / branched archaeal lipid features | reduce | proton permeability | Chong 2024, DOI:10.3389/frbis.2023.1338019, https://doi.org/10.3389/frbis.2023.1338019, Jan 2024 | "structural features that reduce permeability include cyclopentane rings, branched methyl groups, and extensive polar headgroup hydrogen bonding" (chong2024archaeamembranesin pages 2-3) | Strong structure-function edge for archaeal membranes. Use cautiously outside archaeal taxa. |
| S-layer / surface polymers | attract or retain | protons near cell surface | Yao 2023, DOI:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164, Jan 2023 | "Surface polymers (S-layer as a ‘monolayer of cup-shaped structures’) increase net negative charge to attract external protons in alkaliphiles." (yao2023howmethanotrophsrespond pages 5-7) | Mechanistically useful for alkaline tolerance. Taxon-specific exemplar; could be generalized to proton-capturing surface structures with uncertainty. |
| urease + carbonic anhydrase system | maintains | periplasmic pH ~6.1 | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "membrane-bound α-carbonic anhydrase converts CO2 to HCO3−, \"maintaining periplasmic pH at ~6.1\"" (krulwich2011molecularaspectsof pages 27-28) | Strong acid-acclimation edge in H. pylori. Clear mechanism but taxon-specific; should be marked uncertain if generalized to trait broadly. |
| UreI urea channel | controls | urease substrate access under acid stress | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549, May 2011 | "Urease activity and substrate access are controlled by the pH-responsive UreI channel" (krulwich2011molecularaspectsof pages 27-28) | Strong regulatory/transport edge for acid acclimation. Highly specific to Helicobacter-like systems. |
| CCCP / nigericin / sodium benzoate treatment | collapses or perturbs | proton gradient during pHi assays | Pérez-Rodríguez 2024, no DOI available in snippet, publication year 2024 | "methods to collapse the proton gradient (sodium benzoate, CCCP / carbonyl cyanide m‑chlorophenyl hydrazone, nigericin)" (perezrodriguez2024methodsforstudying pages 12-13) | Assay-confounder/control edge, not a natural trait mechanism. Useful warning node for curation to separate experimental perturbation from endogenous mechanism. |
| csrA disruption | increases | extreme acid survival but impairs growth at mildly acidic pH | Gorelik 2024, DOI:10.1128/jb.00354-23, https://doi.org/10.1128/jb.00354-23, Apr 2024 | "loss of csrA causes overexpression, producing a trade-off—markedly improved survival under extreme acidity but impaired growth under mildly acidic conditions (growth defect at pH ≤6)." (gorelik2024multitierregulationof pages 3-5) | Valuable trade-off edge showing why acid-resistance mechanisms may not be constitutively favored, helping explain narrow pH breadth. Specific to E. coli regulatory context. |


*Table: This table compiles evidence-backed candidate causal edges relevant to the narrow microbial pH breadth trait, emphasizing homeostasis mechanisms, membrane properties, transporter systems, acid-resistance cycles, and assay confounders. It is designed to support TraitMech curation by pairing each proposed edge with a source quote and curation note.*

## 8) Visual evidence (mechanism schematic)

Yao et al. (2023) provides a schematic of pH homeostasis in acidophilic vs alkaliphilic methanotrophs (membrane saturation, proton pumps/ATPase, antiporters, K+ uptake, and S-layer/phospholipid remodeling), which can be used to support high-level mechanism nodes and edges in the graph (yao2023howmethanotrophsrespond media 3be20d84).

## 9) Relevant statistics and data (recent studies)

- **Narrow pH preference distributions (community-scale inference):** many taxa have narrow pH distributions; “putative pH preferences [85.4%]” fall between pH 6 and 8, and taxa “generally have pH optima within ~1 pH unit” in the Ramoneda et al. synthesis (ramoneda2023buildingagenomebased pages 6-7).
- **Cytoplasmic pH homeostasis dynamics (methods summary):** E. coli cytoplasmic pH ~7.6; external acidification to pH 5.5 can cause rapid pHi drop to ~6–6.5 with recovery to ~7.6 (perezrodriguez2024methodsforstudying pages 12-13).
- **Membrane physical constraint (archaea):** proton permeability of PLFE tetraether liposomes **~0.3–0.5 ×10−8 cm s−1** (65–82°C), vs egg yolk PC **~3–9 ×10−8 cm s−1** (chong2024archaeamembranesin pages 2-3).
- **Regulatory trade-off effect sizes:** csrA mutant survival improvements under acid shock/pre-adaptation up to **~100-fold** depending on conditions (gorelik2024multitierregulationof pages 3-5).
- **Industrial context statistic:** “organic acid titers of about 50 g/L with pKa 3–5” can lower pH to ~2.0 without alkali intervention (li2024responseofescherichia pages 1-2).

## 10) Warnings / curation caveats (claims not yet ready for TraitMech)

1. **Habitat-specific gene associations:** pH-associated genes identified across environments may not generalize to all taxa; Ramoneda et al. report no gene significant across all datasets (ramoneda2023buildingagenomebased pages 3-5). Curate gene nodes/edges with explicit provenance and consider marking as **context-conditional**.
2. **Survival vs growth:** many acid resistance mechanisms primarily support survival during transient extremes, not growth (e.g., E. coli survival at pH 2 without growth) (li2024responseofescherichia pages 1-2). Use growth-range evidence for *pH delta low*.
3. **Assay perturbants are not trait mechanisms:** CCCP/nigericin/benzoate are experimental tools that collapse gradients; include as **experimental factor nodes** rather than endogenous mechanisms (perezrodriguez2024methodsforstudying pages 12-13).
4. **Taxon specificity:** urease/UreI/periplasmic acid acclimation is well-supported for Helicobacter but should be tagged **taxon-specific** if included (krulwich2011molecularaspectsof pages 27-28).

## 11) DOI-first bibliography (with URLs and dates)

| Citation (first author et al.) | Year | Title | Journal/Server | Publication month | DOI | URL |
|---|---:|---|---|---|---|---|
| Krulwich et al. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 17-18, krulwich2011molecularaspectsof pages 8-9, krulwich2011molecularaspectsof pages 14-15) | 2011 | Molecular aspects of bacterial pH sensing and homeostasis | Nature Reviews Microbiology | May | 10.1038/nrmicro2549 | https://doi.org/10.1038/nrmicro2549 |
| Ramoneda et al. (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 6-7) | 2023 | Building a genome-based understanding of bacterial pH preferences | Science Advances | Apr | 10.1126/sciadv.adf8998 | https://doi.org/10.1126/sciadv.adf8998 |
| Yao et al. (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond media 3be20d84) | 2023 | How methanotrophs respond to pH: A review of ecophysiology | Frontiers in Microbiology | Jan | 10.3389/fmicb.2022.1034164 | https://doi.org/10.3389/fmicb.2022.1034164 |
| Atasoy et al. (atasoy2024methodsforstudying pages 36-37, atasoy2024methodsforstudying pages 18-19) | 2024 | Methods for studying microbial acid stress responses: from molecules to populations | FEMS Microbiology Reviews | May | 10.1093/femsre/fuae015 | https://doi.org/10.1093/femsre/fuae015 |
| Chong (chong2024archaeamembranesin pages 2-3) | 2024 | Archaea membranes in response to extreme acidic environments | Frontiers in Biophysics | Jan | 10.3389/frbis.2023.1338019 | https://doi.org/10.3389/frbis.2023.1338019 |
| Jiang et al. (jiang2024exogenousputrescineplays pages 1-2) | 2024 | Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge | Applied and Environmental Microbiology | Jul | 10.1128/aem.00569-24 | https://doi.org/10.1128/aem.00569-24 |
| Gorelik et al. (gorelik2024multitierregulationof pages 3-5, gorelik2024multitierregulationof pages 1-3, gorelik2024multitierregulationof pages 24-24) | 2024 | Multitier regulation of the *E. coli* extreme acid stress response by CsrA | Journal of Bacteriology | Apr | 10.1128/jb.00354-23 | https://doi.org/10.1128/jb.00354-23 |
| Li et al. (li2024responseofescherichia pages 4-5, li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 10-12, li2024responseofescherichia pages 5-7, li2024responseofescherichia pages 1-2) | 2024 | Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review | Microorganisms | Aug | 10.3390/microorganisms12091774 | https://doi.org/10.3390/microorganisms12091774 |
| Pérez-Rodríguez et al. (perezrodriguez2024methodsforstudying pages 12-13, perezrodriguez2024methodsforstudying pages 37-38, perezrodriguez2024methodsforstudying pages 39-40) | 2024 | Methods for studying microbial acid stress responses | Unknown journal | 2024 | DOI not available in retrieved evidence | URL not available in retrieved evidence |


*Table: This table compiles the core sources used to support the pH delta low trait analysis, prioritizing DOI-resolved references with URLs and publication timing. It is useful as a curation-ready bibliography for tracing all major mechanistic and methodological claims back to the cited literature.*


References

1. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

3. (li2024responseofescherichia pages 1-2): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

4. (perezrodriguez2024methodsforstudying pages 12-13): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

5. (atasoy2024methodsforstudying pages 36-37): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 14-15): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

8. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

9. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

10. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

11. (chong2024archaeamembranesin pages 2-3): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

12. (krulwich2011molecularaspectsof pages 17-18): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

13. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

14. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

15. (atasoy2024methodsforstudying pages 18-19): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 9 citations and is from a domain leading peer-reviewed journal.

16. (gorelik2024multitierregulationof pages 3-5): Mark G. Gorelik, Helen Yakhnin, Archana Pannuri, Alyssa C. Walker, Christine Pourciau, Daniel Czyz, Tony Romeo, and Paul Babitzke. Multitier regulation of the <i>e. coli</i> extreme acid stress response by csra. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00354-23, doi:10.1128/jb.00354-23. This article has 13 citations and is from a peer-reviewed journal.

17. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

18. (perezrodriguez2024methodsforstudying pages 37-38): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

19. (perezrodriguez2024methodsforstudying pages 39-40): F Pérez-Rodríguez, A Possas, and O Scheler. Methods for studying microbial acid stress responses. Unknown journal, 2024.

20. (yao2023howmethanotrophsrespond media 3be20d84): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

21. (krulwich2011molecularaspectsof pages 8-9): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

22. (gorelik2024multitierregulationof pages 1-3): Mark G. Gorelik, Helen Yakhnin, Archana Pannuri, Alyssa C. Walker, Christine Pourciau, Daniel Czyz, Tony Romeo, and Paul Babitzke. Multitier regulation of the <i>e. coli</i> extreme acid stress response by csra. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00354-23, doi:10.1128/jb.00354-23. This article has 13 citations and is from a peer-reviewed journal.

23. (li2024responseofescherichia pages 4-5): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

24. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

25. (li2024responseofescherichia pages 5-7): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

26. (gorelik2024multitierregulationof pages 24-24): Mark G. Gorelik, Helen Yakhnin, Archana Pannuri, Alyssa C. Walker, Christine Pourciau, Daniel Czyz, Tony Romeo, and Paul Babitzke. Multitier regulation of the <i>e. coli</i> extreme acid stress response by csra. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00354-23, doi:10.1128/jb.00354-23. This article has 13 citations and is from a peer-reviewed journal.

27. (li2024responseofescherichia pages 10-12): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.