---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:09:47.095130'
end_time: '2026-06-18T08:24:06.072850'
duration_seconds: 858.98
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: green pigmented
  trait_identifier: METPO:1003025
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: green_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cultures appear
    green or blue-green due to pigments such as pyocyanin and pyoverdine.
  parent_traits: METPO:1003021
  synonyms: Pigment_green
  evidence_summary: 'DOI:10.1186/s12934-023-02122-1: green colorization of the culture
    plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or
    pyoverdine-like pigments in representative bacteria.)'
  causal_graph_summary: 'green_pigmented_pyocyanin_phenazine: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** green pigmented
- **METPO identifier:** METPO:1003025
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cultures appear green or blue-green due to pigments such as pyocyanin and pyoverdine.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_green
- **Existing evidence:** DOI:10.1186/s12934-023-02122-1: green colorization of the culture plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or pyoverdine-like pigments in representative bacteria.)
- **Existing causal graph summary:** green_pigmented_pyocyanin_phenazine: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **green pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/green_pigmented.yaml`.

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
- **Trait label:** green pigmented
- **METPO identifier:** METPO:1003025
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cultures appear green or blue-green due to pigments such as pyocyanin and pyoverdine.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_green
- **Existing evidence:** DOI:10.1186/s12934-023-02122-1: green colorization of the culture plate (Supports green/blue-green pigmentation from pyocyanin and fluorescein or pyoverdine-like pigments in representative bacteria.)
- **Existing causal graph summary:** green_pigmented_pyocyanin_phenazine: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **green pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/green_pigmented.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **green pigmented** (METPO:1003025)

### Scope summary (trait meaning, assay contexts, boundary cases)
The **green pigmented** trait (METPO:1003025) is best interpreted as an **assay-observed colony or culture coloration phenotype** in which microbial growth appears **green to blue‑green** due to pigment absorbance and/or fluorescence. In *Pseudomonas aeruginosa*, a canonical mechanism is the **combination of blue pyocyanin and yellow fluorescein-like pigment**, producing a visibly green culture plate appearance (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2). A second widely relevant mechanism—especially for “fluorescent pseudomonads”—is **pyoverdine**, a **yellow‑green to blue‑green fluorescent siderophore**, which can dominate visual appearance under **UV/blue excitation** and whose emission range depends on chemical state and conditions (herr2024commonfluorescentpseudomonas pages 1-6).

**Boundary cases and pitfalls for curation**:
- “Green” may reflect **fluorescence** (pyoverdine under UV/blue excitation) rather than a strongly absorbing visible pigment; thus, the trait should encode **assay context** (ambient light vs UV/blue excitation) as an experimental factor (herr2024commonfluorescentpseudomonas pages 1-6, zhang2024amultimodalnonlinear pages 11-16).
- Pyocyanin color is **conditional on pH and redox state** (blue-green at neutral/alkaline pH; pink/red in acid; reduced form transparent), so the same strain can appear differently under different culture conditions (jabłonska2023thetwofaces pages 1-2).
- “Fluorescein” is used in some literature as a **yellow pigment contributing to green coloration** (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) but may not always be chemically disambiguated from **pyoverdine-like fluorescent pigments**; treat this node as label-level unless chemical identity is confirmed.

### Key concepts and definitions (current understanding)
**Pyocyanin-driven green/blue-green pigmentation**
- Pyocyanin (PYO) is a **blue-green phenazine pigment** and major virulence-associated secondary metabolite of *P. aeruginosa*; reviews cite production by ~90–95% of strains (mudaliar2024abiomedicalperspective pages 1-4, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2). It is directly responsible for the characteristic bluish-green coloration in many *P. aeruginosa* cultures (mudaliar2024abiomedicalperspective pages 4-6).
- Biosynthesis proceeds from **chorismic acid (chorismate)** to **phenazine‑1‑carboxylic acid (PCA)** via two homologous operons **phz1** and **phz2**, followed by conversion of PCA to pyocyanin by the modifying enzymes **PhzM (SAM-dependent methyltransferase)** and **PhzS (oxygen-dependent monooxygenase)** (mendoza2024thehistidinekinase pages 2-5).

**Pyoverdine/fluorescent siderophore-driven green fluorescence**
- Pyoverdine (PVD) is the **main siderophore** of *P. aeruginosa* used for iron acquisition and is synthesized as a **nonribosomal peptide** by large NRPS enzymes **PvdL, PvdI, PvdJ, PvdD** with accessory enzymes (PvdA/PvdF/PvdH) contributing specialized building blocks (manko2024pvdlorchestratesthe pages 1-2).
- Pyoverdine is produced under **iron limitation**, and pyoverdine pathway components (including fluorescently tagged enzymes in microscopy studies) are **induced under iron-deficient growth conditions** (manko2024pvdlorchestratesthe pages 2-5).
- In environmental “fluorescent pseudomonads,” pyoverdine fluorescence can range from **blue‑green to yellow‑green** when excited by UV, and emission properties depend on chemical state and conditions (herr2024commonfluorescentpseudomonas pages 1-6).

### Recent developments and latest research (prioritizing 2023–2024)
**1) New regulatory linkages for pyocyanin production (2024)**
A key 2024 mechanistic advance is the identification of **NahK** (a histidine kinase in the GacS multi-kinase network) as a regulator of pyocyanin output. Deleting **nahK** produces a **~4‑fold increase in pyocyanin** in planktonic culture (and ~2-fold in biofilm), driven largely by **upregulation of phz2**, and attributed to mis-regulation of quorum sensing with increased PQS signaling (mendoza2024thehistidinekinase pages 2-5, mendoza2024thehistidinekinase pages 1-2). This provides a curation-relevant upstream control point beyond the classic las/rhl/pqs hierarchy.

**2) Condition-dependent QS wiring of phenazine genes (2024)**
Quorum sensing remains central for phenazine pigment regulation. In particular:
- Reviews emphasize that **las, rhl, and pqs** form an interlinked hierarchical network (las activates rhl; las positively controls PQS; rhl negatively influences PQS) (jabłonska2023thetwofaces pages 1-2).
- Newer transcriptomic/reporter evidence indicates **PqsR activates the pqsA–E operon**, and **PqsE can modulate RhlR-dependent activation** of phenazine genes such as **phzA1**, with effects that can be condition-dependent (sotoaceves2024therelationshipbetween pages 2-4, sotoaceves2024therelationshipbetween pages 6-8).

**3) Spatial organization (“siderosomes”) of pyoverdine biosynthesis machinery (2024)**
Single-molecule microscopy studies in 2024 provided cell-biological evidence that pyoverdine NRPS proteins form organized assemblies: PvdL localizes predominantly at the **inner membrane** and appears to **co-localize** with other NRPSs, consistent with a role coordinating pyoverdine biosynthesis (manko2024pvdlorchestratesthe pages 1-2).

**4) Optical readouts of pyoverdine in advanced microscopy and viability assays (2024)**
A 2024 biophotonics study used label-free optical microscopy modalities and compared wild-type to pyoverdine biosynthesis mutants (**pvdA**, **pvdD**) to attribute a major autofluorescence signal to pyoverdine and quantify responses to treatments (zhang2024amultimodalnonlinear pages 11-16). This supports inclusion of “blue/UV excitation” and “fluorescence channel” as explicit experimental nodes affecting the green-pigmented trait readout.

### Current applications and real-world implementations
**Biotechnology and engineering applications (pyocyanin, pyoverdine)**
- Pyocyanin is discussed as a molecule with dual roles—virulence factor yet also a candidate for biotechnological applications and modulation strategies (culture additives, physical factors, genetic engineering) (jabłonska2023thetwofaces pages 10-11, jabłonska2023thetwofaces pages 6-7).
- Pyoverdine engineering has moved toward **bioconjugation and imaging**: an engineered “clickable pyoverdine” retained iron chelation and uptake/recognition and enabled copper-free click chemistry, motivated by applications in **diagnosis, bio-imaging, and biosensing** (puja2024biosynthesisofa pages 1-2).

**Optical/diagnostic applications (pyoverdine fluorescence)**
- Pyoverdine’s strong fluorescence supports imaging-based detection. UV-excited fluorescence is explicitly described, and emission ranges from blue-green to yellow-green, making it a plausible basis for colony-level or host-surface readouts (herr2024commonfluorescentpseudomonas pages 1-6).
- Advanced optical microscopy and spectral approaches use pyoverdine as an endogenous fluorophore to quantify bacterial responses and treatment effects (zhang2024amultimodalnonlinear pages 11-16).

### Expert opinions and analysis from authoritative sources
Authoritative reviews emphasize that a “green pigmented” phenotype is not a single biochemical entity but often a **composite output** of:
1) phenazine biosynthesis and modification (phz operons and PhzM/PhzS) producing pyocyanin, and
2) siderophore production and fluorescence (pyoverdine) influenced by iron restriction.
These reviews highlight the **environmental sensitivity** of pigment output and appearance (media composition, nutrients, pH/redox), reinforcing that trait curation should include **environment/assay nodes** to avoid overgeneralization (jabłonska2023thetwofaces pages 1-2, jabłonska2023thetwofaces pages 6-7).

### Relevant statistics and quantitative data (recent studies)
- **Pyocyanin prevalence:** reviews report pyocyanin produced by **~90–95%** of *P. aeruginosa* strains (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2, mudaliar2024abiomedicalperspective pages 1-4).
- **NahK deletion effect size:** ΔnahK leads to a **~4‑fold increase** in pyocyanin production (planktonic) (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 2-5).
- **Antibiotic-driven transcriptional induction:** sub-lethal antibiotic exposure can strongly increase expression of pyocyanin synthesis genes; e.g., cefotaxime treatment yielded **phzA1 235.56-fold**, **phzM 340.14-fold**, **phzS 280.13-fold** changes in one qPCR study, while tetracycline effects were near baseline (~1–2×) (faisal2024effectofantibiotics pages 1-2).
- **Pyoverdine production prevalence in a clinical sampling study:** among 50 *P. aeruginosa* isolates from burns/wounds, **4/50 (8%)** produced pyoverdine in that dataset (jassim2024anticanceractivityof pages 1-2).
- **Pyoverdine-like siderophore antibacterial metrics:** a pyoverdine-class siderophore preparation showed MIC **6.3 µg/mL** and MBC **12.5 µg/mL** against *E. coli* ATCC 8739; and **82.1%** inhibition of established *Salmonella enterica* biofilms (almuhawish2024productionandantibacterial pages 1-2).

---

## Candidate causal-graph nodes (grouped by type)

### Phenotype node
- **green pigmented** (METPO:1003025)

### Chemicals / pigments / metabolites
- **Pyocyanin** (blue-green phenazine pigment; CHEBI: candidate) (mudaliar2024abiomedicalperspective pages 4-6, jabłonska2023thetwofaces pages 1-2)
- **Phenazine-1-carboxylic acid (PCA)** (CHEBI: candidate) (mendoza2024thehistidinekinase pages 2-5)
- **Pyoverdine** (fluorescent siderophore; CHEBI: candidate) (manko2024pvdlorchestratesthe pages 1-2, herr2024commonfluorescentpseudomonas pages 1-6)
- **Fluorescein** (label-only: “yellow fluorescein” in some sources; potential overlap with pyoverdine-like pigments) (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2)
- **Chorismic acid / chorismate** (CHEBI: candidate) (mendoza2024thehistidinekinase pages 2-5)

### Genes / proteins / complexes (mechanistic)
**Pyocyanin / phenazine branch**
- **phzA–phzG** (phenazine biosynthetic genes; label-only) (mudaliar2024abiomedicalperspective pages 4-6)
- **phz1 operon**, **phz2 operon** (label-only) (mudaliar2024abiomedicalperspective pages 4-6, mendoza2024thehistidinekinase pages 2-5)
- **phzM** (SAM-dependent methyltransferase; label-only) (mendoza2024thehistidinekinase pages 2-5)
- **phzS** (monooxygenase; label-only) (mendoza2024thehistidinekinase pages 2-5)

**Quorum sensing and regulatory branch**
- **LasR/LasI** (AHL QS; label-only) (jabłonska2023thetwofaces pages 1-2, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2)
- **RhlR/RhlI** (AHL QS; label-only) (jabłonska2023thetwofaces pages 1-2, abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2)
- **PqsR**, **pqsA–E operon**, **PqsE** (quinolone QS; label-only) (sotoaceves2024therelationshipbetween pages 2-4, sotoaceves2024therelationshipbetween pages 6-8)
- **NahK** histidine kinase (label-only) (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 2-5)
- **AlgR** (coordinates pyocyanin vs pyoverdine output; label-only) (mudaliar2024abiomedicalperspective pages 4-6)

**Pyoverdine branch**
- **PvdL, PvdI, PvdJ, PvdD** (NRPSs; label-only) (manko2024pvdlorchestratesthe pages 1-2)
- **PvdA, PvdF, PvdH** (accessory enzymes; label-only) (manko2024pvdlorchestratesthe pages 1-2)
- **pvdA, pvdD** (biosynthesis mutants used as assay controls; label-only) (zhang2024amultimodalnonlinear pages 11-16)
- **pvdL** (marker gene for pyoverdine biosynthesis in genomes/metagenomes; label-only) (herr2024commonfluorescentpseudomonas pages 52-55)

### Environmental and experimental factors (ENVO/assay nodes)
- **Iron limitation / iron-deficient growth conditions** (drives pyoverdine pathway expression) (manko2024pvdlorchestratesthe pages 2-5, herr2024commonfluorescentpseudomonas pages 1-6)
- **pH (acidic vs neutral/alkaline)** (alters pyocyanin visible color) (jabłonska2023thetwofaces pages 1-2)
- **Redox state** (oxidized vs reduced pyocyanin) (jabłonska2023thetwofaces pages 1-2)
- **UV/blue excitation and fluorescence imaging conditions** (determines whether pyoverdine appears “green pigmented”) (herr2024commonfluorescentpseudomonas pages 1-6, zhang2024amultimodalnonlinear pages 11-16)
- **Antibiotic exposure at sub-lethal concentrations** (can upregulate pigment genes) (faisal2024effectofantibiotics pages 1-2)

---

## Candidate causal edges (evidence-backed)
The following table is designed for direct curation into a TraitMech/TraitGraph representation.

| Edge (subject–predicate–object) | Node grounding suggestions (CURIEs where possible) | Evidence snippet (verbatim quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|
| pyocyanin + fluorescein/pyoverdine-like pigment → causes → green culture/colony appearance | pyocyanin [CHEBI:candidate]; fluorescein [label-only candidate]; pyoverdine [CHEBI:candidate]; green pigmented [METPO:1003025] | “blue (pyocyanin) and yellow (fluorescein), which lead to the green colorization of the culture plate” (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) | DOI:10.1186/s12934-023-02122-1; 2023; https://doi.org/10.1186/s12934-023-02122-1 | Strong for assay-observed green color in *Pseudomonas aeruginosa*. “Fluorescein” may overlap historically with pyoverdine-like fluorescent pigments; curate cautiously as label-level node if exact chemistry is unclear. |
| chorismate/chorismic acid → precursor_of → phenazine-1-carboxylic acid (PCA) | chorismate [CHEBI:candidate]; PCA [CHEBI:candidate]; phenazine biosynthetic process [GO:candidate] | “Biosynthesis of PYO and other phenazines proceeds from chorismate via the shikimate pathway” and “P. aeruginosa carries two homologous phenazine clusters (phz1 and phz2)” (jabłonska2023thetwofaces pages 1-2) | DOI:10.1007/s11274-023-03548-w; 2023; https://doi.org/10.1007/s11274-023-03548-w | Good mechanistic support; exact enzymatic step from chorismate to PCA is summarized in review context rather than single-enzyme resolution. |
| phz1/phz2 operons → enable biosynthesis_of → PCA | phz1 [label-only gene cluster]; phz2 [label-only gene cluster]; PCA [CHEBI:candidate] | “chorismic acid is converted to PCA by the phz1 and phz2 operons” (mendoza2024thehistidinekinase pages 2-5) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong and curation-ready for *P. aeruginosa* phenazine branch. Taxon-specific. |
| PhzM → converts → PCA-derived intermediate toward pyocyanin | phzM [gene/protein, label-only]; pyocyanin [CHEBI:candidate]; S-adenosyl-L-methionine-dependent methyltransferase activity [GO:candidate] | “PCA is converted to PYO by PhzM (SAM-dependent methyltransferase) and PhzS (oxygen-dependent monooxygenase)” (mendoza2024thehistidinekinase pages 2-5) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong, though intermediate metabolite is not named in this snippet. |
| PhzS → converts → pyocyanin from methylated PCA intermediate | phzS [gene/protein, label-only]; pyocyanin [CHEBI:candidate]; monooxygenase activity [GO:candidate] | “PCA is converted to PYO by PhzM (SAM-dependent methyltransferase) and PhzS (oxygen-dependent monooxygenase)” (mendoza2024thehistidinekinase pages 2-5) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong, commonly cited pyocyanin terminal step. |
| las quorum-sensing system → activates → rhl quorum-sensing system | LasI/LasR [label-only]; RhlI/RhlR [label-only]; quorum sensing [GO:0009372] | “P. aeruginosa has las and rhl HSL systems and a pqs quinolone system with hierarchical and interlinked regulation (las activates rhl” (jabłonska2023thetwofaces pages 1-2) | DOI:10.1007/s11274-023-03548-w; 2023; https://doi.org/10.1007/s11274-023-03548-w | Strong review-level support; broad regulatory edge. |
| las quorum-sensing system → positively_regulates → PQS system | LasI/LasR [label-only]; PQS system [label-only] | “las positively controls PQS while rhl negatively influences PQS” (jabłonska2023thetwofaces pages 1-2) | DOI:10.1007/s11274-023-03548-w; 2023; https://doi.org/10.1007/s11274-023-03548-w | Strong review-level support. |
| rhl quorum-sensing system → negatively_regulates → PQS system | RhlI/RhlR [label-only]; PQS system [label-only] | “las positively controls PQS while rhl negatively influences PQS” (jabłonska2023thetwofaces pages 1-2) | DOI:10.1007/s11274-023-03548-w; 2023; https://doi.org/10.1007/s11274-023-03548-w | Strong review-level support. |
| quorum sensing (las/rhl/pqs) → positively_regulates → pyocyanin production | quorum sensing [GO:0009372]; pyocyanin [CHEBI:candidate] | “Quorum sensing controls pyocyanin synthesis: AHL and PQS are named autoinducers and the LasR-LasI and RhlR-RhlI systems are said to activate expressions including pyocyanin.” (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) | DOI:10.1186/s12934-023-02122-1; 2023; https://doi.org/10.1186/s12934-023-02122-1 | Strong but summary-level; combine with more specific phz edges below for curation. |
| las and rhl systems → activate → phz1 operon | phz1 [label-only gene cluster]; LasI/LasR [label-only]; RhlI/RhlR [label-only] | “phz1 is activated by the las and rhl systems” (mendoza2024thehistidinekinase pages 2-5) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong, taxon-specific to *P. aeruginosa*. |
| QS systems → regulate → phzM and phzS | phzM [label-only]; phzS [label-only]; quorum sensing [GO:0009372] | “phzM/phzS and the phz operons are QS-regulated” (mendoza2024thehistidinekinase pages 2-5) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong. |
| NahK deletion → increases → pyocyanin production | NahK [histidine kinase, label-only]; pyocyanin [CHEBI:candidate] | “Deleting nahK (ΔnahK) causes a pronounced increase in PYO (fourfold planktonic; twofold biofilm)” (mendoza2024thehistidinekinase pages 2-5) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong experimental support. Edge should likely be modeled as NahK normally represses pyocyanin. |
| NahK deletion → upregulates → phz2 | NahK [label-only]; phz2 [label-only gene cluster] | “Deletion of the histidine kinase nahK causes a ~4-fold increase in pyocyanin (PYO) production, driven almost entirely by upregulation of the phenazine operon phz2.” (mendoza2024thehistidinekinase pages 1-2) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong and highly relevant to causal graph expansion beyond core pyocyanin pathway. |
| NahK → modulates → PQS system | NahK [label-only]; PQS system [label-only] | “This PYO increase is attributed to mis-regulation of quorum sensing: a large upregulation of the PQS system and decreased production from the las AHL system.” (mendoza2024thehistidinekinase pages 1-2) | DOI:10.1128/jb.00276-23; 2024; https://doi.org/10.1128/jb.00276-23 | Strong but directionality is partly inferred from deletion phenotype; annotate as regulatory edge with note. |
| PqsR → activates → pqsA-E operon | PqsR [label-only]; pqsA-E operon [label-only] | “PqsR activates the pqsA-E operon (including pqsE)” (sotoaceves2024therelationshipbetween pages 2-4) | DOI:10.1128/jb.00138-24; 2024; https://doi.org/10.1128/jb.00138-24 | Strong. Useful upstream QS node. |
| PqsE → promotes → RhlR-dependent activation of phzA1/phenazine genes | PqsE [label-only]; RhlR [label-only]; phzA1 [label-only]; pyocyanin [CHEBI:candidate] | “The phzA1 operon is QS dependent and the phz genes synthesize pyocyanin; production of this pigment is reported as QS- and PqsE-dependent.” (sotoaceves2024therelationshipbetween pages 6-8) | DOI:10.1128/jb.00138-24; 2024; https://doi.org/10.1128/jb.00138-24 | Strong, but some PqsE effects are condition-dependent in the source study. |
| pyocyanin redox state / pH → alters → apparent color | pyocyanin [CHEBI:candidate]; pH [ENVO:candidate]; redox state [GO:candidate] | “PYO exhibits a blue-green colour at neutral/alkaline pH, shifting to pink-red in acidic conditions; oxidized PYO is blue while the reduced form is transparent” (jabłonska2023thetwofaces pages 1-2) | DOI:10.1007/s11274-023-03548-w; 2023; https://doi.org/10.1007/s11274-023-03548-w | Strong. Important boundary-case edge: visible color is conditional on environment and redox chemistry. |
| PvdL/PvdI/PvdJ/PvdD → participate_in → pyoverdine biosynthesis | PvdL [label-only]; PvdI [label-only]; PvdJ [label-only]; PvdD [label-only]; pyoverdine [CHEBI:candidate]; siderophore biosynthetic process [GO:candidate] | “The pyoverdine peptide backbone is synthesized by four NRPSs (PvdL, PvdI, PvdJ, PvdD)” (manko2024pvdlorchestratesthe pages 1-2) | DOI:10.3390/ijms25116013; 2024; https://doi.org/10.3390/ijms25116013 | Strong and curation-ready for pyoverdine branch. |
| iron-deficient conditions → induce expression_of → pyoverdine biosynthetic enzymes | iron limitation [ENVO:candidate]; PvdL/PvdI/PvdJ/PvdD [label-only]; pyoverdine biosynthetic process [GO:candidate] | “The expression of the fluorescent enzymes was induced by iron-deficient growing conditions similarly to the wild-type PAO1” (manko2024pvdlorchestratesthe pages 2-5) | DOI:10.3390/ijms25116013; 2024; https://doi.org/10.3390/ijms25116013 | Strong direct support for environmental regulation of pyoverdine pathway. |
| pyoverdine → exhibits → blue-green to yellow-green fluorescence under UV excitation | pyoverdine [CHEBI:candidate]; fluorescence [GO:candidate]; UV light [ENVO:candidate] | “Pyoverdine emits visible light when excited by UV and its emission can range from blue-green to yellow-green (wavelengths ~400–550 nm).” (herr2024commonfluorescentpseudomonas pages 1-6) | DOI:10.1101/2024.04.26.591271; 2024; https://doi.org/10.1101/2024.04.26.591271 | Useful for assay-context edges; preprint and broader pseudomonads, so mark as somewhat uncertain for stable TraitMech curation. |
| pvdA / pvdD loss → decreases_or_abrogates → pyoverdine fluorescence signal | pvdA [label-only]; pvdD [label-only]; pyoverdine [CHEBI:candidate]; fluorescence phenotype [label-only] | “compared strains including PAO and pyoverdine biosynthesis mutants (pvdA and pvdD) after background subtraction” and the study “link[s] pyoverdine to visible/fluorescent pigmentation” (zhang2024amultimodalnonlinear pages 11-16) | DOI:10.1002/jbio.202300384; 2024; https://doi.org/10.1002/jbio.202300384 | Moderate support: snippet is summary-style rather than direct mutant result quote; useful but should be marked assay-specific until direct figure/text quote is curated. |
| pvdL presence → associated_with → fluorescent pseudomonad capacity | pvdL [label-only]; fluorescent pseudomonads [NCBITaxon:candidate group]; pyoverdine biosynthesis [GO:candidate] | “genes for pyoverdine biosynthesis were found ‘in the genomes of all sequenced fluorescent pseudomonas isolates.’” (herr2024commonfluorescentpseudomonas pages 27-31) | DOI:10.1101/2024.04.26.591271; 2024; https://doi.org/10.1101/2024.04.26.591271 | Moderate support; broad genomic association across environmental pseudomonads, not direct causal proof for the trait in all taxa. |
| pvdL read detection in metagenomes → indicates → pyoverdine-producing fluorescent pseudomonads in sample | pvdL [label-only]; metagenome [label-only]; fluorescent phenotype [label-only] | “The excerpt reports detection of the pyoverdine biosynthesis gene pvdL in epiphytic metagenomic samples” (herr2024commonfluorescentpseudomonas pages 52-55) | DOI:10.1101/2024.04.26.591271; 2024; https://doi.org/10.1101/2024.04.26.591271 | Weak for TraitMech because this is ecological association, not direct trait causation in isolate-level phenotype. |
| pyoverdine-mediated fluorescence assay → detects → Pseudomonas signal under blue/UV imaging | pyoverdine [CHEBI:candidate]; fluorescence detection [label-only]; imaging assay [label-only] | “the authors measured UV–VIS spectra of pure pyoverdine … alongside P. aeruginosa culture spectra, and compared strains including PAO and pyoverdine biosynthesis mutants (pvdA and pvdD)” (zhang2024amultimodalnonlinear pages 11-16) | DOI:10.1002/jbio.202300384; 2024; https://doi.org/10.1002/jbio.202300384 | Assay-specific edge for detection implementation rather than biology per se; still useful as experimental-factor node. |


*Table: This table compiles curation-ready candidate causal edges for the microbial trait green pigmented (METPO:1003025), covering pyocyanin, pyoverdine, quorum sensing, environmental modulation, and assay-specific fluorescence evidence. It is designed to help prioritize which mechanisms are strong enough for TraitMech curation and which should remain provisional.*

---

## Warnings / do-not-curate-yet items
1) **Preprint-only evidence**: some pyoverdine fluorescence ecology/genomics evidence is from a 2024 bioRxiv preprint; treat edges relying exclusively on that source (e.g., pvdL prevalence across fluorescent pseudomonads, emission descriptions) as *provisional* unless corroborated by peer-reviewed sources (herr2024commonfluorescentpseudomonas pages 1-6, herr2024commonfluorescentpseudomonas pages 27-31, herr2024commonfluorescentpseudomonas pages 52-55).
2) **Ambiguous pigment naming**: “fluorescein” as a yellow pigment contributing to green color is explicitly stated (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2) but may not always map cleanly to a specific chemical distinct from pyoverdine-like fluorescent siderophores; consider a label-only node or add a synonym mapping step rather than hard-grounding to CHEBI fluorescein without confirmation.
3) **Assay dependence**: edges involving “green” via pyoverdine should capture **excitation wavelength** and measurement channel; otherwise the same strain could be scored inconsistently across labs (zhang2024amultimodalnonlinear pages 11-16, herr2024commonfluorescentpseudomonas pages 1-6).

---

## DOI-first bibliography (with dates and URLs)
- Abdelaziz AA, et al. **Pseudomonas aeruginosa’s greenish-blue pigment pyocyanin: its production and biological activities**. *Microbial Cell Factories*. **2023-06**. DOI:10.1186/s12934-023-02122-1. https://doi.org/10.1186/s12934-023-02122-1 (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2)
- Jabłońska J, et al. **The two faces of pyocyanin - why and how to steer its production?** *World Journal of Microbiology & Biotechnology*. **2023-02**. DOI:10.1007/s11274-023-03548-w. https://doi.org/10.1007/s11274-023-03548-w (jabłonska2023thetwofaces pages 1-2)
- Mudaliar SB, Prasad ASB. **A biomedical perspective of pyocyanin from Pseudomonas aeruginosa: its applications and challenges**. *World Journal of Microbiology & Biotechnology*. **2024-02**. DOI:10.1007/s11274-024-03889-0. https://doi.org/10.1007/s11274-024-03889-0 (mudaliar2024abiomedicalperspective pages 4-6)
- Mendoza AG, et al. **The histidine kinase NahK regulates pyocyanin production through the PQS system**. *Journal of Bacteriology*. **2024-01**. DOI:10.1128/jb.00276-23. https://doi.org/10.1128/jb.00276-23 (mendoza2024thehistidinekinase pages 1-2, mendoza2024thehistidinekinase pages 2-5)
- Soto-Aceves MP, et al. **The relationship between pqs gene expression and acylhomoserine lactone signaling in Pseudomonas aeruginosa**. *Journal of Bacteriology*. **2024-10**. DOI:10.1128/jb.00138-24. https://doi.org/10.1128/jb.00138-24 (sotoaceves2024therelationshipbetween pages 2-4, sotoaceves2024therelationshipbetween pages 6-8)
- Manko H, et al. **PvdL orchestrates the assembly of the nonribosomal peptide synthetases involved in pyoverdine biosynthesis in Pseudomonas aeruginosa**. *International Journal of Molecular Sciences*. **2024-05**. DOI:10.3390/ijms25116013. https://doi.org/10.3390/ijms25116013 (manko2024pvdlorchestratesthe pages 1-2, manko2024pvdlorchestratesthe pages 2-5)
- Puja H, et al. **Biosynthesis of a clickable pyoverdine via in vivo enzyme engineering of an adenylation domain**. *Microbial Cell Factories*. **2024-07**. DOI:10.1186/s12934-024-02472-4. https://doi.org/10.1186/s12934-024-02472-4 (puja2024biosynthesisofa pages 1-2)
- Zhang C, et al. **A multimodal nonlinear optical microscopy study of the responses of Pseudomonas aeruginosa to blue light and antibiotic treatment**. *Journal of Biophotonics*. **2024-12**. DOI:10.1002/jbio.202300384. https://doi.org/10.1002/jbio.202300384 (zhang2024amultimodalnonlinear pages 11-16)
- Faisal RM, Younis RM. **Effect of antibiotics on the expression of pyocyanin synthetic genes in Pseudomonas aeruginosa…** *Journal of Applied and Natural Science*. **2024-06**. DOI:10.31018/jans.v16i2.5590. https://doi.org/10.31018/jans.v16i2.5590 (faisal2024effectofantibiotics pages 1-2)
- Almuhawish MA, et al. **Production and Antibacterial Activity of Atypical Siderophore from Pseudomonas sp. QCS59…** *Pharmaceuticals*. **2024-08**. DOI:10.3390/ph17091126. https://doi.org/10.3390/ph17091126 (almuhawish2024productionandantibacterial pages 1-2)
- Jassim YA, Aniz EHS. **Anticancer activity of pyoverdine (PVD) producing by antibiotic-resistant Pseudomonas aeruginosa…** *Journal of Applied and Natural Science*. **2024-06**. DOI:10.31018/jans.v16i2.5506. https://doi.org/10.31018/jans.v16i2.5506 (jassim2024anticanceractivityof pages 1-2)
- Herr K, et al. **Common fluorescent Pseudomonas in the phyllosphere can influence aphid behavior in diverse ways**. *bioRxiv* (preprint). **2024-04**. DOI:10.1101/2024.04.26.591271. https://doi.org/10.1101/2024.04.26.591271 (herr2024commonfluorescentpseudomonas pages 1-6, herr2024commonfluorescentpseudomonas pages 52-55)


References

1. (abdelaziz2023pseudomonasaeruginosa’sgreenishblue pages 1-2): Ahmed A. Abdelaziz, Amal M. Abo Kamer, Khaled B. Al-Monofy, and Lamiaa A. Al-Madboly. Pseudomonas aeruginosa’s greenish-blue pigment pyocyanin: its production and biological activities. Microbial Cell Factories, Jun 2023. URL: https://doi.org/10.1186/s12934-023-02122-1, doi:10.1186/s12934-023-02122-1. This article has 202 citations and is from a peer-reviewed journal.

2. (herr2024commonfluorescentpseudomonas pages 1-6): Kathryn Herr, Jonah Schieber, and Tory A Hendry. Common fluorescent pseudomonas in the phyllosphere can influence aphid behavior in diverse ways. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.26.591271, doi:10.1101/2024.04.26.591271. This article has 2 citations.

3. (zhang2024amultimodalnonlinear pages 11-16): Chi Zhang, Farzana R. Zaki, Jungeun Won, and Stephen A. Boppart. A multimodal nonlinear optical microscopy study of the responses of <i>pseudomonas aeruginosa</i> to blue light and antibiotic treatment. Journal of Biophotonics, Dec 2024. URL: https://doi.org/10.1002/jbio.202300384, doi:10.1002/jbio.202300384. This article has 6 citations and is from a peer-reviewed journal.

4. (jabłonska2023thetwofaces pages 1-2): Joanna Jabłońska, Adrian Augustyniak, Kamila Dubrowska, and Rafał Rakoczy. The two faces of pyocyanin - why and how to steer its production? World Journal of Microbiology & Biotechnology, Feb 2023. URL: https://doi.org/10.1007/s11274-023-03548-w, doi:10.1007/s11274-023-03548-w. This article has 48 citations and is from a peer-reviewed journal.

5. (mudaliar2024abiomedicalperspective pages 1-4): Samriti Balaji Mudaliar and Alevoor Srinivas Bharath Prasad. A biomedical perspective of pyocyanin from pseudomonas aeruginosa: its applications and challenges. World Journal of Microbiology & Biotechnology, Feb 2024. URL: https://doi.org/10.1007/s11274-024-03889-0, doi:10.1007/s11274-024-03889-0. This article has 99 citations and is from a peer-reviewed journal.

6. (mudaliar2024abiomedicalperspective pages 4-6): Samriti Balaji Mudaliar and Alevoor Srinivas Bharath Prasad. A biomedical perspective of pyocyanin from pseudomonas aeruginosa: its applications and challenges. World Journal of Microbiology & Biotechnology, Feb 2024. URL: https://doi.org/10.1007/s11274-024-03889-0, doi:10.1007/s11274-024-03889-0. This article has 99 citations and is from a peer-reviewed journal.

7. (mendoza2024thehistidinekinase pages 2-5): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

8. (manko2024pvdlorchestratesthe pages 1-2): Hanna Manko, Tania Steffan, Véronique Gasser, Yves Mély, Isabelle Schalk, and Julien Godet. Pvdl orchestrates the assembly of the nonribosomal peptide synthetases involved in pyoverdine biosynthesis in pseudomonas aeruginosa. International Journal of Molecular Sciences, 25:6013, May 2024. URL: https://doi.org/10.3390/ijms25116013, doi:10.3390/ijms25116013. This article has 8 citations.

9. (manko2024pvdlorchestratesthe pages 2-5): Hanna Manko, Tania Steffan, Véronique Gasser, Yves Mély, Isabelle Schalk, and Julien Godet. Pvdl orchestrates the assembly of the nonribosomal peptide synthetases involved in pyoverdine biosynthesis in pseudomonas aeruginosa. International Journal of Molecular Sciences, 25:6013, May 2024. URL: https://doi.org/10.3390/ijms25116013, doi:10.3390/ijms25116013. This article has 8 citations.

10. (mendoza2024thehistidinekinase pages 1-2): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

11. (sotoaceves2024therelationshipbetween pages 2-4): Martín P. Soto-Aceves, Nicole E. Smalley, Amy L. Schaefer, and E. Peter Greenberg. The relationship between <i>pqs</i> gene expression and acylhomoserine lactone signaling in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00138-24, doi:10.1128/jb.00138-24. This article has 7 citations and is from a peer-reviewed journal.

12. (sotoaceves2024therelationshipbetween pages 6-8): Martín P. Soto-Aceves, Nicole E. Smalley, Amy L. Schaefer, and E. Peter Greenberg. The relationship between <i>pqs</i> gene expression and acylhomoserine lactone signaling in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00138-24, doi:10.1128/jb.00138-24. This article has 7 citations and is from a peer-reviewed journal.

13. (jabłonska2023thetwofaces pages 10-11): Joanna Jabłońska, Adrian Augustyniak, Kamila Dubrowska, and Rafał Rakoczy. The two faces of pyocyanin - why and how to steer its production? World Journal of Microbiology & Biotechnology, Feb 2023. URL: https://doi.org/10.1007/s11274-023-03548-w, doi:10.1007/s11274-023-03548-w. This article has 48 citations and is from a peer-reviewed journal.

14. (jabłonska2023thetwofaces pages 6-7): Joanna Jabłońska, Adrian Augustyniak, Kamila Dubrowska, and Rafał Rakoczy. The two faces of pyocyanin - why and how to steer its production? World Journal of Microbiology & Biotechnology, Feb 2023. URL: https://doi.org/10.1007/s11274-023-03548-w, doi:10.1007/s11274-023-03548-w. This article has 48 citations and is from a peer-reviewed journal.

15. (puja2024biosynthesisofa pages 1-2): Hélène Puja, Laurent Bianchetti, Johan Revol-Tissot, Nicolas Simon, Anastasiia Shatalova, Julian Nommé, Sarah Fritsch, Roland H. Stote, Gaëtan L. A. Mislin, Noëlle Potier, Annick Dejaegere, and Coraline Rigouin. Biosynthesis of a clickable pyoverdine via in vivo enzyme engineering of an adenylation domain. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02472-4, doi:10.1186/s12934-024-02472-4. This article has 7 citations and is from a peer-reviewed journal.

16. (faisal2024effectofantibiotics pages 1-2): Rayan Mazin Faisal and Rafal Mhaide Younis. Effect of antibiotics on the expression of pyocyanin synthetic genes in pseudomonas aeruginosa isolated from different clinical sources of a few hospitals in mosul, iraq. Journal of Applied and Natural Science, 16:812-819, Jun 2024. URL: https://doi.org/10.31018/jans.v16i2.5590, doi:10.31018/jans.v16i2.5590. This article has 11 citations.

17. (jassim2024anticanceractivityof pages 1-2): Yazi Abdullah Jassim and Eman Hamid Sadiq Aniz. Anticancer activity of pyoverdine (pvd) producing by antibiotic-resistant pseudomonas aeruginosa isolated from burn and wound infections. Journal of Applied and Natural Science, 16:777-785, Jun 2024. URL: https://doi.org/10.31018/jans.v16i2.5506, doi:10.31018/jans.v16i2.5506. This article has 7 citations.

18. (almuhawish2024productionandantibacterial pages 1-2): Mashael A. Almuhawish, Essam Kotb, Eida Alkhaldi, and Asmaa A. Ahmed. Production and antibacterial activity of atypical siderophore from pseudomonas sp. qcs59 recovered from harpachene schimperi. Pharmaceuticals, 17:1126, Aug 2024. URL: https://doi.org/10.3390/ph17091126, doi:10.3390/ph17091126. This article has 5 citations.

19. (herr2024commonfluorescentpseudomonas pages 52-55): Kathryn Herr, Jonah Schieber, and Tory A Hendry. Common fluorescent pseudomonas in the phyllosphere can influence aphid behavior in diverse ways. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.26.591271, doi:10.1101/2024.04.26.591271. This article has 2 citations.

20. (herr2024commonfluorescentpseudomonas pages 27-31): Kathryn Herr, Jonah Schieber, and Tory A Hendry. Common fluorescent pseudomonas in the phyllosphere can influence aphid behavior in diverse ways. bioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.26.591271, doi:10.1101/2024.04.26.591271. This article has 2 citations.