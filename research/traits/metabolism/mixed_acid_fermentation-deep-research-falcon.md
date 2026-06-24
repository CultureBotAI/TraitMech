---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:19:03.561405'
end_time: '2026-06-18T05:30:17.401598'
duration_seconds: 673.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mixed-acid fermentation
  trait_identifier: traitmech:000027
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: mixed_acid_fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation in which sugars are converted via the glycolytic pathway
    to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and
    H2. Characteristic of enteric bacteria such as Escherichia coli.
  parent_traits: METPO:1002005
  synonyms: ''
  evidence_summary: 'DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy
    conservation lists acetate, ethanol, lactate, succinate and formate as products
    of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation
    pathways describes mixed-acid fermentation by enterobacteria and its characteristic
    acid product spectrum.)'
  causal_graph_summary: 'mixed_acid_fermentation_enterobacterial: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mixed-acid fermentation
- **METPO identifier:** traitmech:000027
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which sugars are converted via the glycolytic pathway to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and H2. Characteristic of enteric bacteria such as Escherichia coli.
- **Parent traits:** METPO:1002005
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation lists acetate, ethanol, lactate, succinate and formate as products of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation pathways describes mixed-acid fermentation by enterobacteria and its characteristic acid product spectrum.)
- **Existing causal graph summary:** mixed_acid_fermentation_enterobacterial: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mixed-acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/mixed_acid_fermentation.yaml`.

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
- **Trait label:** mixed-acid fermentation
- **METPO identifier:** traitmech:000027
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which sugars are converted via the glycolytic pathway to a mixture of acids (lactic, acetic, formic, succinic) plus ethanol, CO2 and H2. Characteristic of enteric bacteria such as Escherichia coli.
- **Parent traits:** METPO:1002005
- **Synonyms:** 
- **Existing evidence:** DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation lists acetate, ethanol, lactate, succinate and formate as products of mixed-acid fermentation.) | DOI:10.3390/molecules31020333:  (Review of fermentation pathways describes mixed-acid fermentation by enterobacteria and its characteristic acid product spectrum.)
- **Existing causal graph summary:** mixed_acid_fermentation_enterobacterial: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mixed-acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/mixed_acid_fermentation.yaml`.

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


## Mixed-acid fermentation (METPO:traitmech:000027) — curation-focused research report (2023–2024)

### 1) Scope summary (trait meaning, assays, boundary cases)

**Mixed-acid fermentation** is a fermentative metabolic phenotype typical of many enteric/facultatively anaerobic bacteria in which sugars are catabolized via glycolysis to pyruvate and then distributed into multiple product branches, yielding a characteristic mixture of **formate, acetate, lactate, succinate, and ethanol** (plus CO2 and sometimes H2 via formate cleavage). A concise definition consistent with current literature is that, in *E. coli*, “mixed acid fermentation (MAF) produces formate, acetate, lactate, succinate, and ethanol” under anaerobic conditions (brothwell2023formateproductionis pages 1-2).

**Trait boundary conditions and distinguishing from nearby traits**:
- **Oxygen limitation is a primary switch**: Under oxygen-limiting conditions, pyruvate is cleaved by **pyruvate formate-lyase (PFL/PflB)** to form **acetyl‑CoA + formate** (taggar2024hydrogenproductionvia pages 5-7). Under aerobic conditions, electrons are transferred to oxygen and hydrogen formation is suppressed; a recent review states “the presence of oxygen prevents the generation of hydrogen” in dark fermentation contexts (taggar2024hydrogenproductionvia pages 5-7).
- **pH is mechanistically relevant**, particularly for formate handling: “The pH of the environment influences the shape of the [FocA] transport channel and subsequently the directionality of formate transport” (brothwell2023formateproductionis pages 1-2). Also, FHL-mediated formate cleavage is described as occurring “under acidic conditions into H2 and CO2” (taggar2024hydrogenproductionvia pages 5-7).
- **Distinguish from homolactic fermentation** (mostly lactate, minimal mixed products) and from **solventogenic clostridial fermentation** (e.g., butanol/acetone dominant). In contrast, enteric mixed-acid fermentation maintains **multiple acidic end-products** and often uses **formate metabolism (FocA/FHL)** as part of redox/acid stress handling (li2024agrowthbasedscreening pages 2-4, brothwell2023formateproductionis pages 1-2).

Operationally (for phenotype curation), the trait is typically observed under **anaerobic or microaerobic growth on sugars**, where secreted end-products include multiple organic acids/alcohols rather than a single dominant product (brothwell2023formateproductionis pages 1-2). Quantitative “fingerprints” depend on strain and conditions; engineered strains can be used to validate branches but should be curated with uncertainty flags (zhu2024acetateproductionfrom pages 4-7).

---

### 2) Key concepts and definitions (current understanding)

#### Core product spectrum
In *E. coli*, mixed-acid fermentation yields “formate, acetate, lactate, succinate, and ethanol” (brothwell2023formateproductionis pages 1-2). A 2024 pathway diagram in *Applied and Environmental Microbiology* explicitly depicts mixed-acid fermentation “yielding succinate, ethanol, acetate, formate, and lactate” and links this to formate hydrogenlyase (FHL) function (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768).

#### Branching logic from pyruvate
A central defining step is **PflB (PFL)**:
- “Pyruvate formate lyase (PflB) catalyzes the conversion of pyruvate into formate and acetyl‑CoA” (brothwell2023formateproductionis pages 1-2).
The acetyl‑CoA branch then supports acetate production:
- “Acetyl‑CoA is further metabolized by Pta and AckA to generate acetate” (brothwell2023formateproductionis pages 1-2).
A review further highlights energy conservation:
- “The formation of acetate from acetyl CoA generates ATP through the action of phosphotransacetylase and acetate kinase” (taggar2024hydrogenproductionvia pages 5-7).

#### Formate export and formate-to-H2/CO2 conversion
**FocA**: A mechanistic pathway figure states that “formate channel (FocA) facilitate[s] the passage of … formate … across the cytoplasmic membrane” (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768), and environmental pH influences transport directionality (brothwell2023formateproductionis pages 1-2).

**FHL**: The same figure and text describe formate disproportionation: “Formate is disproportionated into CO2 and H+ by the formate hydrogenlyase complex,” with electrons released at **FdhF** and transferred to hydrogenase 3 (**HycE**) “to yield H2” (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768).

---

### 3) Candidate nodes (grouped by type, with ontology grounding suggestions)

#### A. Pathways / processes / complexes
- Mixed-acid fermentation (METPO:traitmech:000027)
- Glycolysis (GO:0006096; suggested)
- Formate hydrogenlyase complex (FHL; label-only if complex ID not yet chosen)

#### B. Genes / proteins / enzymes (enteric model-centric)
- **pflB / PFL** (EC:2.3.1.54) — pyruvate → formate + acetyl‑CoA (brothwell2023formateproductionis pages 1-2)
- **pta** (EC:2.3.1.8) and **ackA** (EC:2.7.2.1) — acetyl‑CoA → acetate; ATP via acetate branch (brothwell2023formateproductionis pages 1-2, taggar2024hydrogenproductionvia pages 5-7)
- **focA** — formate channel/transport (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768)
- **fdhF** (formate dehydrogenase H) — electron input module of FHL (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768)
- **hycE** (hydrogenase 3 catalytic subunit) and **hycB** (electron transfer subunit) — part of FHL electron transfer chain (li2024agrowthbasedscreening media c0f20768)
- **ldhA**, **adhE**, **frdA** (and broader FRD module) — key branch enzymes frequently manipulated to shift product profiles (zhu2024acetateproductionfrom pages 4-7)

#### C. Chemicals / metabolites (CHEBI grounding)
- Pyruvate (CHEBI:15361)
- Acetyl‑CoA (CHEBI:15351)
- Formate (CHEBI:15740)
- Acetate (CHEBI:30089)
- Lactate (CHEBI:24996)
- Succinate (CHEBI:15741)
- Ethanol (CHEBI:16236)
- CO2 (CHEBI:16526)
- H2 (CHEBI:18276)
- ATP (CHEBI:15422)
- O2 (CHEBI:15379)

#### D. Environmental / experimental factors
- Oxygen limitation / anaerobiosis (ENVO label-only suggested)
- Acidic conditions / environmental pH (PATO label-only suggested)
- Strictly anoxic assay conditions (experimental constraint for oxygen-sensitive metal centers) (li2024agrowthbasedscreening pages 2-4)

---

### 4) Evidence-backed candidate causal edges (triples)

The following table is designed for direct translation into a TraitMech causal graph (subject–predicate–object), with grounding suggestions, quotes, and curation notes.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Reference | Notes / uncertainty |
|---|---|---|---|---|---|
| mixed-acid fermentation (METPO:traitmech:000027) | has_output | pyruvate (CHEBI:15361) | “Pyruvate, ATP, and NADH are produced, when glucose or other carbon sources … reach the primary glycolytic pathway.” (taggar2024hydrogenproductionvia pages 5-7) | Taggar et al., 2024. DOI: 10.35812/cellulosechemtechnol.2024.58.90. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Supports upstream glycolysis→pyruvate context for mixed-acid fermentation; review-level evidence rather than direct edge wording. |
| pyruvate formate lyase / PflB (EC:2.3.1.54; gene: pflB) | catalyzes_conversion_of | pyruvate (CHEBI:15361) -> formate (CHEBI:15740) + acetyl-CoA (CHEBI:15351) | “Pyruvate formate lyase (PflB) catalyzes the conversion of pyruvate into formate and acetyl-CoA.” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Strong mechanistic edge; primary literature. |
| pyruvate formate lyase / PFL (EC:2.3.1.54; gene: pflB) | active_under | oxygen-limiting conditions (label only) | “pyruvate is cleaved in the presence of pyruvate formate lyase (PFL) under oxygen limiting conditions, where it generates acetyl coenzyme A (AcCoA) and formic acid.” (taggar2024hydrogenproductionvia pages 5-7) | Taggar et al., 2024. DOI: 10.35812/cellulosechemtechnol.2024.58.90. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Review source; useful environmental condition edge for trait scope. |
| phosphotransacetylase / Pta (EC:2.3.1.8) + acetate kinase / AckA (EC:2.7.2.1) | converts | acetyl-CoA (CHEBI:15351) -> acetate (CHEBI:30089) | “Acetyl-CoA is further metabolized by Pta and AckA to generate acetate.” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Strong branch-defining edge for acetate production. |
| acetate formation branch via Pta/AckA (label only) | generates | ATP (CHEBI:15422) | “The formation of acetate from acetyl CoA generates ATP through the action of phosphotransacetylase and acetate kinase.” (taggar2024hydrogenproductionvia pages 5-7) | Taggar et al., 2024. DOI: 10.35812/cellulosechemtechnol.2024.58.90. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Good energetic edge; review-level but explicit. |
| formate channel FocA (gene: focA) | transports | formate (CHEBI:15740) | “The membrane-bound glucose-specific phosphotransferase system (PtsG) and formate channel (FocA) facilitate the passage of glucose and formate, respectively, across the cytoplasmic membrane.” (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768) | Li et al., 2024. DOI: 10.1128/aem.01472-24. URL: https://doi.org/10.1128/aem.01472-24 | Figure-backed mechanistic transport edge in E. coli. |
| environmental pH (PATO/label only) | influences_directionality_of | FocA-mediated formate transport (label only) | “The pH of the environment influences the shape of the transport channel and subsequently the directionality of formate transport.” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Strong condition edge; transport polarity is pH-dependent. |
| formate (CHEBI:15740) | induces_synthesis_of | formate hydrogenlyase complex / FHL (label only; includes FdhF/HycE/HycB) | “Formate … induces the synthesis of the membrane-bound FHL complex that catalyzes formate disproportionation into CO2 and H2.” (li2024agrowthbasedscreening pages 2-4) | Li et al., 2024. DOI: 10.1128/aem.01472-24. URL: https://doi.org/10.1128/aem.01472-24 | Useful regulatory edge in E. coli; direct statement. |
| acidic conditions (label only) | activate_or_favor | formate hydrogenlyase complex / FHL (label only) | “The enzyme complex formate:hydrogen lyase (FHL) cleaves formate under acidic conditions into H2 and CO2…” (taggar2024hydrogenproductionvia pages 5-7) | Taggar et al., 2024. DOI: 10.35812/cellulosechemtechnol.2024.58.90. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong environmental edge; review source. |
| formate hydrogenlyase complex / FHL (fdhF/hyc) | disproportionates | formate (CHEBI:15740) -> CO2 (CHEBI:16526) + H2 (CHEBI:18276) | “Formate is disproportionated into CO2 and H+ by the formate hydrogenlyase complex. Here, two electrons are released at the formate dehydrogenase H subunit (FdhF …), passed on to the hydrogenase 3 (HycE) subunit … to yield H2.” (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768) | Li et al., 2024. DOI: 10.1128/aem.01472-24. URL: https://doi.org/10.1128/aem.01472-24 | Figure and text support a detailed mechanistic edge; note snippet says H+ then explains H2 formation. |
| oxygen / aerobic conditions (CHEBI:15379) | inhibits | hydrogen production (CHEBI:18276) | “The presence of oxygen prevents the generation of hydrogen…” (taggar2024hydrogenproductionvia pages 5-7) | Taggar et al., 2024. DOI: 10.35812/cellulosechemtechnol.2024.58.90. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 | Strong environmental inhibition edge. |
| molecular oxygen (CHEBI:15379) | inactivates | metal centers of FHL-linked redox enzymes (label only) | “The metal centers employed by these redox-active enzymes are easily inactivated by molecular oxygen.” (li2024agrowthbasedscreening pages 2-4) | Li et al., 2024. DOI: 10.1128/aem.01472-24. URL: https://doi.org/10.1128/aem.01472-24 | Supports anoxia requirement for FHL/formate dehydrogenase activity. |
| mixed-acid fermentation products / acid generation (label only) | lowers_pH_of | cytoplasm / growth medium (GO:0005737 for cytoplasm if needed) | “MAF results in the generation of acid, which subsequently lowers the pH of the cytoplasm.” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Core phenotype edge linking pathway to acidification. |
| deletion of fdhF / loss of EcFDH-H (gene: fdhF) | reduces | fermentative growth (label only) | “strain JG-X reached a final cell density (OD600) of 1.25 ± 0.05 while strain FL004 did not exceed an OD600 value of 0.357 ± 0.006 revealing a strong growth retardation effect of the EcFDH-H deletion.” (li2024agrowthbasedscreening pages 2-4) | Li et al., 2024. DOI: 10.1128/aem.01472-24. URL: https://doi.org/10.1128/aem.01472-24 | Perturbation edge in engineered E. coli strain background; valuable but assay/genotype-specific. |
| deletion of fdhF / loss of EcFDH-H (gene: fdhF) | accelerates | culture acidification (label only) | “The culture broth pH of the EcFDH-H-deficient strain FL004 decreased from 7.0 to below 6.1 within 4 h while the strain JG-X maintained the culture medium pH above 6.1…” (li2024agrowthbasedscreening pages 2-4) | Li et al., 2024. DOI: 10.1128/aem.01472-24. URL: https://doi.org/10.1128/aem.01472-24 | Perturbation edge; supports role of FHL-linked formate oxidation in deacidification. |
| deletion of frdA (gene: frdA) | decreases | succinate production (CHEBI:15741) | “deletion of frdA, ldhA, and adhE obviously decreased the generation of succinate, lactate and ethanol, respectively” (zhu2024acetateproductionfrom pages 4-7) | Zhu et al., 2024. DOI: 10.1186/s12934-024-02575-y. URL: https://doi.org/10.1186/s12934-024-02575-y | Strong gene→product branch edge in engineered E. coli BL21(DE3). |
| deletion of ldhA (gene: ldhA) | decreases | lactate production (CHEBI:24996) | “deletion of frdA, ldhA, and adhE obviously decreased the generation of succinate, lactate and ethanol, respectively” (zhu2024acetateproductionfrom pages 4-7) | Zhu et al., 2024. DOI: 10.1186/s12934-024-02575-y. URL: https://doi.org/10.1186/s12934-024-02575-y | Strong gene→product branch edge in engineered E. coli BL21(DE3). |
| deletion of adhE (gene: adhE) | decreases | ethanol production (CHEBI:16236) | “deletion of frdA, ldhA, and adhE obviously decreased the generation of succinate, lactate and ethanol, respectively” (zhu2024acetateproductionfrom pages 4-7) | Zhu et al., 2024. DOI: 10.1186/s12934-024-02575-y. URL: https://doi.org/10.1186/s12934-024-02575-y | Strong gene→product branch edge in engineered E. coli BL21(DE3). |
| combined deletion of frdA + ldhA + adhE (genes: frdA, ldhA, adhE) | increases | acetate proportion / acetate yield (CHEBI:30089) | “The strain E. coli 3K produced 7.93 g/L acetate from 18 g/L glucose within 24 h. The proportion of acetate in the total fermentation products increased to 94.18% while the yield of acetate increased to 0.44 g/g glucose.” (zhu2024acetateproductionfrom pages 4-7) | Zhu et al., 2024. DOI: 10.1186/s12934-024-02575-y. URL: https://doi.org/10.1186/s12934-024-02575-y | Perturbation edge for metabolic redirection; engineered-production context, not native trait-defining. |
| mixed-acid fermentation in E. coli (METPO:traitmech:000027) | has_end_product | succinate (CHEBI:15741) | “In Escherichia coli, MAF produces formate, acetate, lactate, succinate, and ethanol…” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Product-spectrum edge; good high-level trait assertion. |
| mixed-acid fermentation in E. coli (METPO:traitmech:000027) | has_end_product | formate (CHEBI:15740) | “In Escherichia coli, MAF produces formate, acetate, lactate, succinate, and ethanol…” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Product-spectrum edge. |
| mixed-acid fermentation in E. coli (METPO:traitmech:000027) | has_end_product | acetate (CHEBI:30089) | “In Escherichia coli, MAF produces formate, acetate, lactate, succinate, and ethanol…” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Product-spectrum edge. |
| mixed-acid fermentation in E. coli (METPO:traitmech:000027) | has_end_product | lactate (CHEBI:24996) | “In Escherichia coli, MAF produces formate, acetate, lactate, succinate, and ethanol…” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Product-spectrum edge. |
| mixed-acid fermentation in E. coli (METPO:traitmech:000027) | has_end_product | ethanol (CHEBI:16236) | “In Escherichia coli, MAF produces formate, acetate, lactate, succinate, and ethanol…” (brothwell2023formateproductionis pages 1-2) | Brothwell et al., 2023. DOI: 10.1128/iai.00176-23. URL: https://doi.org/10.1128/iai.00176-23 | Product-spectrum edge. |
| acetate synthesis from acetyl-CoA (label only) | required_for | fermentative growth (label only) | “This result suggests that ATP generated via acetate synthesis from acetyl-CoA … is required for the fermentative growth of MR-1.” (ikeda2023supplementationwithamino pages 7-9) | Ikeda et al., 2023. DOI: 10.1128/aem.00868-23. URL: https://doi.org/10.1128/aem.00868-23 | Supporting context only; organism is Shewanella oneidensis, not enteric bacterium, so curate with caution. |


*Table: This table compiles candidate subject-predicate-object edges for a TraitMech causal graph of mixed-acid fermentation, using only evidence from the cited 2023–2024 sources in the conversation. It highlights core pathway steps, environmental controls, perturbation evidence, and notes where evidence is organism-specific or better treated as supporting context.*

**Figure evidence (visual)**: The mixed-acid pathway and the FHL complex components (including FocA and key enzymes) are explicitly diagrammed in Figure 1 of Li et al. 2024 (li2024agrowthbasedscreening media c0f20768).

---

### 5) Recent developments and latest research (emphasis 2023–2024)

#### 5.1 Mechanistic refinement and tool-building around FHL/formate handling (2024)
Li et al. (2024) developed a **growth-based screening strategy** for engineering the oxygen-sensitive **formate dehydrogenase H (FdhF/EcFDH-H)**, explicitly coupling mixed-acid fermentation physiology to enzyme activity via FHL complementation (published Sep 2024; DOI: 10.1128/aem.01472-24; https://doi.org/10.1128/aem.01472-24) (li2024agrowthbasedscreening pages 2-4). The paper provides quantitative evidence that disrupting FHL electron input impacts growth and acidification:
- **Final OD600**: EcFDH-H-producing strain vs EcFDH-H-deficient strain: “OD600 of 1.25 ± 0.05” vs “0.357 ± 0.006” (li2024agrowthbasedscreening pages 2-4).
- **Acidification kinetics**: pH dropped “from 7.0 to below 6.1 within 4 h” in the EcFDH-H-deficient strain, whereas the producing strain maintained “pH above 6.1” for up to 10 h (li2024agrowthbasedscreening pages 2-4).
- **Gas stoichiometry**: CO2 and H2 were produced at a “molar ratio … slightly different from 1:1,” consistent with (but not exclusively explained by) FHL-based formate conversion (li2024agrowthbasedscreening pages 2-4).

These data support curated edges linking **FHL activity** to reduced acid stress (deacidification) and improved fermentative growth under mixed-acid product accumulation (li2024agrowthbasedscreening pages 2-4).

#### 5.2 Industrial metabolic engineering leveraging mixed-acid branch knockouts (2024)
Zhu et al. (2024) engineered *E. coli* BL21(DE3) to enhance acetate production from glucose and corn stover hydrolysate by suppressing mixed-acid byproduct branches (published Nov 2024; DOI: 10.1186/s12934-024-02575-y; https://doi.org/10.1186/s12934-024-02575-y) (zhu2024acetateproductionfrom pages 4-7). They report in the parental strain that “succinate (8.20%), lactate (45.31%), and ethanol (12.07%) were also produced … through the mixed acid fermentation pathway” (zhu2024acetateproductionfrom pages 4-7), and show that deleting **frdA, ldhA, adhE** decreases those byproducts (zhu2024acetateproductionfrom pages 4-7). Quantitative outcomes include:
- Baseline shake-flask profile: consumption of “17.33 g/L glucose … accumulated 1.25 g/L succinate, 6.91 g/L lactate, 1.84 g/L ethanol and 5.25 g/L acetate” (zhu2024acetateproductionfrom pages 4-7).
- Engineered acetate enhancement: after sequential knockouts, “E. coli 3K produced 7.93 g/L acetate from 18 g/L glucose … proportion of acetate … 94.18% … yield … 0.44 g/g glucose” (zhu2024acetateproductionfrom pages 4-7).

These results are directly relevant as **real-world implementations**: industrial bioprocess designs often treat mixed-acid fermentation as a competing network whose branches are **targeted for deletion** to improve a desired product.

#### 5.3 Updated synthesis of mixed-acid fermentation for biohydrogen (2024 review)
Taggar et al. (2024) summarize how, in facultative anaerobes like *E. coli*, oxygen depletion triggers a shift from aerobic metabolism to fermentation; under oxygen-limiting conditions, “pyruvate is cleaved in the presence of pyruvate formate lyase (PFL) … [to] acetyl coenzyme A … and formic acid” and enteric bacteria “carry out a mixed-acid fermentation” producing multiple acids and ethanol (published Nov 2024; DOI: 10.35812/cellulosechemtechnol.2024.58.90; https://doi.org/10.35812/cellulosechemtechnol.2024.58.90) (taggar2024hydrogenproductionvia pages 5-7). They also link acidic conditions to FHL: “FHL cleaves formate under acidic conditions into H2 and CO2” (taggar2024hydrogenproductionvia pages 5-7). The review provides an explicit yield summary: mixed product formation diminishes H2 yield “to approximately 1 to 2.5 moles for one mole of glucose utilized” in practice (taggar2024hydrogenproductionvia pages 5-7).

---

### 6) Applications and real-world implementations

1. **Biohydrogen production (dark fermentation / formate-to-H2 route)**
   - Mixed-acid fermentation is relevant to biohydrogen because formate can be converted to H2 + CO2 by **FHL**, with oxygen presence suppressing hydrogen generation and acidic conditions favoring formate cleavage (taggar2024hydrogenproductionvia pages 5-7). The practical-yield statistic of “~1 to 2.5 moles [H2] for one mole of glucose” situates expected performance in applied systems (taggar2024hydrogenproductionvia pages 5-7).

2. **Industrial organic acid production and branch redirection**
   - Acetate bioproduction from lignocellulosic hydrolysate is an explicit example where mixed-acid byproduct branches are engineered away. Zhu et al. show titers/yields and acetate tolerance, including the note that BL21(DE3) can “still slightly grow in the presence of 30 g/L acetate” (zhu2024acetateproductionfrom pages 4-7).

3. **Enzyme engineering platforms for oxygen-sensitive metalloenzymes**
   - Li et al. connect mixed-acid fermentation physiology (acid accumulation) to growth-coupled screening for variants of oxygen-sensitive **FdhF** relevant to “hydrogen and formate economy … green nitrogen fixation and production of chemical feedstocks” (li2024agrowthbasedscreening pages 2-4). This is a methodological application in biocatalyst development.

---

### 7) Expert opinions / authoritative analysis (as reflected in sources)

- **Physiological framing of mixed-acid fermentation as acid stress challenge**: Brothwell et al. state that “MAF results in the generation of acid, which subsequently lowers the pH of the cytoplasm” and that cells must export or further metabolize acids to avoid detrimental effects (brothwell2023formateproductionis pages 1-2). This provides an authoritative basis to include acid stress and pH homeostasis edges.
- **FHL as a deacidification/relief mechanism under product accumulation**: Li et al. attribute growth retardation in an FdhF-deficient background to “accumulation of weak organic acids during mixed acid fermentation,” and show faster pH drop without FdhF (li2024agrowthbasedscreening pages 2-4). This supports curation of FHL-linked edges as causal contributors to fermentation robustness.

---

## Warnings / claims that should be curated cautiously

1. **Engineered-strain perturbations are not the same as trait definition**: Knockouts (e.g., ΔfrdA, ΔldhA, ΔadhE) strongly support branch assignments (gene→metabolite) but may not represent native flux distributions or environmental relevance. Curate these edges as mechanistic support with “engineered context” notes (zhu2024acetateproductionfrom pages 4-7).
2. **Non-enteric organism evidence (Shewanella)**: Ikeda et al. provide high-quality quantitative fermentation product data but in *Shewanella oneidensis*; use only as supportive context or for cross-taxon generalization with uncertainty flags (ikeda2023supplementationwithamino pages 7-9).
3. **Review-level statements vs primary mechanistic demonstration**: Taggar et al. provide useful condition/yield summaries but as a review; key enzymatic edges should ideally be backed by primary sources when feasible (taggar2024hydrogenproductionvia pages 5-7).

---

## DOI-first bibliography (with publication dates and URLs)

1. **Li F, Scheller S, Lienemann M.** (Sep 2024). *A growth-based screening strategy for engineering the catalytic activity of an oxygen-sensitive formate dehydrogenase.* **Applied and Environmental Microbiology** 90(9). DOI: **10.1128/aem.01472-24**. URL: https://doi.org/10.1128/aem.01472-24 (li2024agrowthbasedscreening pages 2-4, li2024agrowthbasedscreening media c0f20768)

2. **Zhu J-m, Liu W, Guo L, et al.** (Nov 2024). *Acetate production from corn stover hydrolysate using recombinant Escherichia coli BL21 (DE3) with an EP-bifido pathway.* **Microbial Cell Factories** 23. DOI: **10.1186/s12934-024-02575-y**. URL: https://doi.org/10.1186/s12934-024-02575-y (zhu2024acetateproductionfrom pages 4-7)

3. **Taggar MS, Kaur A, Jain C, et al.** (Nov 2024). *Hydrogen production via dark fermentation: a review of influential factors.* **Cellulose Chemistry and Technology** 58:1051–1063. DOI: **10.35812/cellulosechemtechnol.2024.58.90**. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90 (taggar2024hydrogenproductionvia pages 5-7)

4. **Brothwell JA, Fortney KR, Williams JS, et al.** (Published Aug 18, 2023; Sep 2023 issue). *Formate production is dispensable for Haemophilus ducreyi virulence in human volunteers.* **Infection and Immunity** 91(9). DOI: **10.1128/iai.00176-23**. URL: https://doi.org/10.1128/iai.00176-23 (brothwell2023formateproductionis pages 1-2)

5. **Ikeda S, Tomita K, Nakagawa G, Kouzuma A, Watanabe K.** (Jul 2023). *Supplementation with amino acid sources facilitates fermentative growth of Shewanella oneidensis MR-1 in defined media.* **Applied and Environmental Microbiology** 89(7). DOI: **10.1128/aem.00868-23**. URL: https://doi.org/10.1128/aem.00868-23 (ikeda2023supplementationwithamino pages 7-9)


References

1. (brothwell2023formateproductionis pages 1-2): Julie A. Brothwell, Kate R. Fortney, Jalan S. Williams, Teresa A. Batteiger, Rory Duplantier, Danielle Grounds, Amber S. Jannasch, Barry P. Katz, and Stanley M. Spinola. Formate production is dispensable for <i>haemophilus ducreyi</i> virulence in human volunteers. Infection and Immunity, Sep 2023. URL: https://doi.org/10.1128/iai.00176-23, doi:10.1128/iai.00176-23. This article has 4 citations and is from a peer-reviewed journal.

2. (taggar2024hydrogenproductionvia pages 5-7): Monica SACHDEVA TAGGAR, Amanpreet Kaur, Chahak Jain, Anu Kalia, and Sarbjit SINGH SOOCH. Hydrogen production via dark fermentation: a review of influential factors. Cellulose Chemistry and Technology, 58:1051-1063, Nov 2024. URL: https://doi.org/10.35812/cellulosechemtechnol.2024.58.90, doi:10.35812/cellulosechemtechnol.2024.58.90. This article has 11 citations and is from a peer-reviewed journal.

3. (li2024agrowthbasedscreening pages 2-4): Feilong Li, Silvan Scheller, and Michael Lienemann. A growth-based screening strategy for engineering the catalytic activity of an oxygen-sensitive formate dehydrogenase. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01472-24, doi:10.1128/aem.01472-24. This article has 5 citations and is from a peer-reviewed journal.

4. (zhu2024acetateproductionfrom pages 4-7): Jie-min Zhu, Wei Liu, Leilei Guo, Xiaoxu Tan, Weikang Sun, Hongxu Zhang, Hui Zhang, Wenjia Tian, Tianyi Jiang, Wensi Meng, Yidong Liu, Zhaoqi Kang, Chao Gao, Chuanjuan Lü, Ping Xu, and Cuiqing Ma. Acetate production from corn stover hydrolysate using recombinant escherichia coli bl21 (de3) with an ep-bifido pathway. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02575-y, doi:10.1186/s12934-024-02575-y. This article has 7 citations and is from a peer-reviewed journal.

5. (li2024agrowthbasedscreening media c0f20768): Feilong Li, Silvan Scheller, and Michael Lienemann. A growth-based screening strategy for engineering the catalytic activity of an oxygen-sensitive formate dehydrogenase. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01472-24, doi:10.1128/aem.01472-24. This article has 5 citations and is from a peer-reviewed journal.

6. (ikeda2023supplementationwithamino pages 7-9): Sota Ikeda, Keisuke Tomita, Gen Nakagawa, Atsushi Kouzuma, and Kazuya Watanabe. Supplementation with amino acid sources facilitates fermentative growth of shewanella oneidensis mr-1 in defined media. Applied and Environmental Microbiology, Jul 2023. URL: https://doi.org/10.1128/aem.00868-23, doi:10.1128/aem.00868-23. This article has 4 citations and is from a peer-reviewed journal.