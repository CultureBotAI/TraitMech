---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:40:01.117127'
end_time: '2026-06-18T09:54:43.845138'
duration_seconds: 882.73
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spiral shaped
  trait_identifier: METPO:1000684
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spiral_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a spiral or helically curved morphology
    rather than a straight rod or sphere.
  parent_traits: METPO:1000666
  synonyms: S_curved_spiral, spiral, spiral-shaped
  evidence_summary: 'DOI:10.1371/journal.pbio.1002565: spirillar types (Supports spiral/spirillar
    morphology as a recognized bacterial cell-shape class within broader bacterial
    morphology diversity.)'
  causal_graph_summary: 'spiral_shaped_curvature_mechanisms: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spiral shaped
- **METPO identifier:** METPO:1000684
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spiral or helically curved morphology rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, spiral, spiral-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: spirillar types (Supports spiral/spirillar morphology as a recognized bacterial cell-shape class within broader bacterial morphology diversity.)
- **Existing causal graph summary:** spiral_shaped_curvature_mechanisms: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **spiral shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spiral_shaped.yaml`.

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
- **Trait label:** spiral shaped
- **METPO identifier:** METPO:1000684
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spiral or helically curved morphology rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, spiral, spiral-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: spirillar types (Supports spiral/spirillar morphology as a recognized bacterial cell-shape class within broader bacterial morphology diversity.)
- **Existing causal graph summary:** spiral_shaped_curvature_mechanisms: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **spiral shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spiral_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Spiral shaped (METPO:1000684)

### 0. Scope summary (TraitMech curation)
**Trait label:** spiral shaped (METPO:1000684; MORPHOLOGY; CLASS).

**Operational phenotype:** cells with a spiral/helically curved morphology (a 3D helix or 2D “helical/flat-wave” waveform) rather than straight rods or spheres. In the curated evidence, the trait is instantiated in at least two mechanistically distinct regimes:
1) **Helically curved rods** whose curvature is encoded in the **cell wall architecture (peptidoglycan, PG)** and its spatially patterned synthesis/remodeling (e.g., *Campylobacter jejuni* helical morphology maintained by PG; *Helicobacter pylori* helical/spiral morphology influenced by PG-crosslinking state and envelope networks). (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 17-17, frirdich2023multiplecampylobacterjejuni pages 15-16)
2) **Spirochetes** in which **periplasmic (endo)flagella** act as an internal cytoskeletal/propulsive system that **distorts and pushes the cell body**, producing a spiral/flat-wave cell form. (zambacampero2024broadlyconservedflgv pages 1-2, lynch2023lysinoalaninecrosslinkingis pages 1-2)

**Boundary cases / neighboring traits:**
- **Curved rod / vibrioid**: single-axis curvature without a repeating helical pitch (frequently observed as intermediate phenotypes when helical-shape genes are perturbed in *C. jejuni* and *H. pylori*). (frirdich2023multiplecampylobacterjejuni pages 2-3, frirdich2023multiplecampylobacterjejuni pages 15-16)
- **Coccoid conversion**: a stress/age-associated or mutant-associated transition to spherical cells (e.g., 48 h morphology in certain *H. pylori* LPS mutants; stress-induced coccoids in *C. jejuni*). (frirdich2023multiplecampylobacterjejuni pages 1-2, tang2023rolesoflipopolysaccharide pages 4-7, tang2023rolesoflipopolysaccharide pages 11-12)

**Assay/measurement considerations:** morphology is time- and method-dependent; examples include DIC/TEM + morphometrics and PG muropeptide HPLC profiling (for *C. jejuni*), and Gram staining with 24 h vs 48 h comparisons (for *H. pylori* LPS mutants). (frirdich2023multiplecampylobacterjejuni pages 3-5, tang2023rolesoflipopolysaccharide pages 4-7)

---

### 1. Key concepts and current mechanistic understanding
#### 1.1 Spiral/helical morphology as an envelope-encoded mechanical state
In helical-rod bacteria, curvature is strongly tied to PG composition, crosslinking, and local remodeling. In *C. jejuni*, the helical morphology is explicitly “maintained by the peptidoglycan (PG) layer,” and the trait is sensitive to PG hydrolase perturbations that alter muropeptide profiles. (frirdich2023multiplecampylobacterjejuni pages 1-2)

A recurring mechanistic theme is **patterned PG insertion and remodeling**, where enzymatic activities (carboxypeptidases/endopeptidases) reshape the peptide stem distribution and/or crosslinking, shifting the mechanical anisotropy of the wall. (frirdich2023multiplecampylobacterjejuni pages 2-3)

#### 1.2 Spiral/flat-wave morphology as a flagella-imposed body deformation (spirochetes)
In spirochetes, spiral-shaped morphology is not only a passive wall property: periplasmic flagellar filaments reside within the periplasm and “distort and push the cell body,” linking flagellar structure/assembly to cell form and motility/virulence phenotypes. (lynch2023lysinoalaninecrosslinkingis pages 1-2)

---

### 2. Recent developments (prioritizing 2023–2024)
#### 2.1 2024: Outer membrane patterning as a curvature generator (new morphogenetic module)
A 2024 *Nature Communications* study in *Rhodospirillum rubrum* identifies a mechanistically distinct module: two outer-membrane porins (**Por39, Por41**) form a **helical ribbon-like structure** at the **outer curve** that recruits a PG-binding lipoprotein (**PapS**). Perturbing PapS or disrupting the porin–PapS interface causes **cell straightening**. (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 2-3)

Mechanistic model: porin–PapS assemblies act as “molecular cages” that entrap the elongation machinery (elongasome), biasing PG insertion toward the outer curve and thereby establishing curvature. (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13)

A quantitative modeling result from this work states that a modest **~15% bias** toward increased outer-curve wall growth is sufficient to generate curvature. (pohl2024anoutermembrane pages 11-12)

A mechanistic schematic (Figure 10) is available showing the “roadblock model” for elongasome caging and curvature generation. (pohl2024anoutermembrane media 79ad3ada)

#### 2.2 2023: Expanded PG-enzyme networks influencing helical curvature in *Campylobacter*
A 2023 *Frontiers in Microbiology* study expands beyond known PG hydrolases (Pgp1/Pgp2) to identify additional candidate morphogenesis genes (a **bactofilin-domain protein** and multiple **M23 peptidases**) whose deletions and overexpression shift curvature and alter PG muropeptide profiles, supporting dose-dependent and networked control of helical curvature. (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 2-3)

#### 2.3 2023: Envelope (LPS) biosynthesis genes linked to maintenance of *H. pylori* spiral morphology
A 2023 *International Journal of Molecular Sciences* study reports that systematic deletion of eight *H. pylori* LPS glycosyltransferase genes leads to “significant morphological changes (coccoid, coiled ‘c’-shape, and irregular shapes) after 48 h growth” compared with wild type. (tang2023rolesoflipopolysaccharide pages 1-2, tang2023rolesoflipopolysaccharide pages 12-13)

#### 2.4 2023–2024: Spirochete studies linking flagellar assembly components/chemistry to morphology-enabled behavior
A 2024 *Nature Communications* paper identifies **FlgV (BB0268)** as a conserved flagellar superoperon component; its deletion produces fewer/shorter filaments with motility and cell division defects, consistent with flagellar architecture influencing the characteristic spirochete body plan and behaviors needed for dissemination. (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 2-4)

A 2023 *PNAS Nexus* paper shows the flagellar hook protein **FlgE** carries a conserved **lysinoalanine crosslink** across spirochetes; the crosslink is not required for hook assembly but is required for motility, implying a biomechanical stabilizer enabling effective torque transmission to the body. (lynch2023lysinoalaninecrosslinkingis pages 1-2)

---

### 3. Candidate causal-graph nodes (grouped by type)
Below are candidate nodes for `spiral_shaped.yaml`. Groundings are suggested only where stable identifiers are clear.

#### 3.1 Genes/proteins/complexes
**PG remodeling & morphogenesis (helical rods):**
- *C. jejuni*: **Pgp1**, **Pgp2**, **Pgp3** (PG carboxypeptidase/endopeptidase activities), **AmiA** (amidase; mentioned in enzyme-class context), **Cjj81176_1104** (bactofilin-domain), **Cjj81176_0166 / 1105 / 1228** (M23 peptidase-domain proteins). (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 2-3)

**Helicobacter helical-shape factors:**
- **CcmA (bactofilin homolog)**; **Csd1, Csd2, Csd3, Csd5, Csd7** (cell-shape-determining proteins; crosslinking/morphology associations summarized in recent literature). (tang2023rolesoflipopolysaccharide pages 11-12, frirdich2023multiplecampylobacterjejuni pages 15-16)

**Outer membrane–patterning curvature module (curved/helical rods):**
- *R. rubrum*: **Por39**, **Por41** (outer membrane porins), **PapS** (lipoprotein with OmpA-like PG-binding domain), **RodZ** (elongasome-associated factor used as a marker for elongasome behavior in the study). (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13)

**Spirochete periplasmic flagellar apparatus:**
- **Periplasmic/endoflagella** (as a structure/module), **flgB superoperon** (encodes basal body/hook/rod/filament components), **FlgV (BB0268)**, **FlhF/FlhG** (co-conserved regulators), **FlgE** (hook protein) with **lysinoalanine crosslink PTM**. (zambacampero2024broadlyconservedflgv pages 2-4, lynch2023lysinoalaninecrosslinkingis pages 1-2)

#### 3.2 Pathways / biological processes (candidate GO)
- **Peptidoglycan biosynthetic process** (GO:0009252) and associated **cell wall organization/remodeling** (label-only here; specific GO term depends on curator preference). Supported generally through PG synthesis/remodeling being central to curvature outcomes in helical rods. (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 2-3)
- **Polysaccharide biosynthetic process** (GO:0000271) as a proxy for **LPS biosynthesis** (more specific LPS terms could be chosen during curation). (tang2023rolesoflipopolysaccharide pages 1-2)

#### 3.3 Chemicals / metabolites (candidate CHEBI)
- **UDP-N-acetylglucosamine (UDP-GlcNAc)** (CHEBI:28938): invoked as a shared precursor pool that may connect LPS glycosylation perturbations to PG sacculus outcomes (interpretive claim; see warnings). (tang2023rolesoflipopolysaccharide pages 11-12)

#### 3.4 Environmental/experimental factors
- **Culture age**: 24 h vs 48 h strongly affects observed *H. pylori* morphology in LPS mutants (spiral/rod-like early; coccoid/coiled/irregular later). (tang2023rolesoflipopolysaccharide pages 4-7)
- **Stress/adverse growth** and **aging**: associated with filamented/coccoid forms in *C. jejuni*. (frirdich2023multiplecampylobacterjejuni pages 1-2)
- **Microaerobic growth conditions** (label-only ENVO candidate): specified for *C. jejuni* culturing during morphometrics and PG profiling. (frirdich2023multiplecampylobacterjejuni pages 3-5)
- **Calcofluor white selection**: can select rod-shaped variants of *C. jejuni* (experimental shape modulator). (frirdich2023multiplecampylobacterjejuni pages 1-2)

---

### 4. Evidence-backed candidate causal edges (curation table)
The following table is designed to be directly mined into a TraitMech causal graph (subject–predicate–object triples), with snippets, context, and uncertainty flags.

| Subject node | Predicate | Object node | Evidence snippet (verbatim/near-verbatim) | System/Taxon | Experimental context/modulators | Strength/uncertainty | Reference (DOI + URL + year) | Citation ID |
|---|---|---|---|---|---|---|---|---|
| Pgp1 | required_for_generation_of | helical cell morphology | “PG hydrolases Pgp1 and Pgp2 are important for generating C. jejuni helical morphology, with deletion mutants being rod-shaped” | *Campylobacter jejuni* | Gene deletion mutants; morphology + muropeptide profiling | Strong | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 1-2) |
| Pgp2 | required_for_generation_of | helical cell morphology | “PG hydrolases Pgp1 and Pgp2 are important for generating C. jejuni helical morphology, with deletion mutants being rod-shaped” | *Campylobacter jejuni* | Gene deletion mutants; morphology + muropeptide profiling | Strong | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 1-2) |
| Pgp2 | converts | tetrapeptides to tripeptides | “Pgp2 (LD-carboxypeptidase) converts tetrapeptides to tripeptides” | *Campylobacter jejuni* | Enzymatic/PG remodeling context | Strong | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| Pgp1 | cleaves | tripeptides to dipeptides | “Pgp1 (DL-carboxypeptidase) … cleaves tripeptides to dipeptides” | *Campylobacter jejuni* | Enzymatic/PG remodeling context | Strong | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| loss_of_pgp1_or_pgp2 | causes | rod-shaped cells | “loss of pgp1 or pgp2 yields rod-shaped cells with altered muropeptide profiles” | *Campylobacter jejuni* | Deletion mutants | Strong | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| Pgp3 | has_activity | DD-carboxypeptidase and DD-endopeptidase activity | “Pgp3 has DD-carboxypeptidase and DD-endopeptidase activities” | *Campylobacter jejuni* | PG enzyme annotation in mutant study | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| Δpgp3 | causes | curved rod phenotype | “a Δpgp3 mutant shows a curved rod phenotype” | *Campylobacter jejuni* | Gene deletion mutant | Strong | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| gene_1104_bactofilin | influences | degree of helical cell curvature | “the putative bactofilin 1104 … deletions in the corresponding genes resulted in varying curved rod morphologies” | *Campylobacter jejuni* | Gene deletion mutants; DIC/TEM/CellTool morphometrics; mid-exponential cultures under microaerobic growth | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 3-5, frirdich2023multiplecampylobacterjejuni pages 1-2) |
| gene_1105_M23_peptidase | influences | degree of helical cell curvature | “the M23 peptidase domain-containing proteins 0166, 1105, and 1228 … deletions … resulted in varying curved rod morphologies” | *Campylobacter jejuni* | Gene deletion mutants; DIC/TEM/CellTool morphometrics | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 3-5, frirdich2023multiplecampylobacterjejuni pages 1-2) |
| gene_0166_M23_peptidase | influences | degree of helical cell curvature | “0166 … deletions … resulted in varying curved rod morphologies” | *Campylobacter jejuni* | Gene deletion mutants | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 3-5, frirdich2023multiplecampylobacterjejuni pages 1-2) |
| gene_1228_M23_peptidase | influences | degree of helical cell curvature | “1228 … deletions … resulted in varying curved rod morphologies” | *Campylobacter jejuni* | Gene deletion mutants | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 3-5, frirdich2023multiplecampylobacterjejuni pages 1-2) |
| overexpression_of_1104 | decreases | cell curvature | “Overexpression of 1104 … resulted in changes in the morphology and in the muropeptide profiles” and “overexpression of 1104 decreases curvature” | *Campylobacter jejuni* | Overexpression strains | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| overexpression_of_1105 | increases | cell curvature | “Overexpression of 1105 also resulted in changes in the morphology and in the muropeptide profiles” and “overexpression of 1105 increases curvature” | *Campylobacter jejuni* | Overexpression strains | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 2-3) |
| Pgp1_Pgp2_1104_1105_0166_1228 | alters | PG muropeptide profile | “deletions produce varied curved-rod morphologies and muropeptide changes” | *Campylobacter jejuni* | PG isolation and HPLC muropeptide profiling | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 2-3) |
| aging_or_stress_adverse_growth_conditions | causes | filamented or coccoid forms | “aging, stress/adverse growth conditions (leading to filamented or coccoid forms)” | *Campylobacter jejuni* | Environmental/growth-state effect | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 1-2) |
| calcofluor_white_selection | produces | rod variants | “selection with calcofluor white (CFW) producing rod variants” | *Campylobacter jejuni* | Experimental chemical selection | Moderate | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 17-17) |
| disruption_of_LPS_glycosyltransferases | alters | typical spiral/helical morphology | “deletion of eight LPS glycosyltransferase genes … caused pronounced changes in cell morphology — producing coccoid, coiled ‘c’-shape, and irregular forms — after 48 h of growth” | *Helicobacter pylori* strain G27 | 24 h vs 48 h culture; Gram-staining; microaerobic culture at 37 °C | Strong | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 1-2, tang2023rolesoflipopolysaccharide pages 12-13) |
| wecA_deletion | causes | loss_of_typical_helical_shape | “Interfering with LPS biosynthesis via deletion/inhibition of glycosyltransferases (e.g., wecA) ‘prevents the bacteria from forming a typical helical shape’” | *Helicobacter pylori* | Mutant construction by Xer-cise deletion; morphology at 24–48 h | Strong | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 12-13) |
| ΔwecA | causes | almost completely coccoid morphology | “G27∆HP1578 and G27∆wecA became almost completely coccoid after 48 h of culture” | *Helicobacter pylori* strain G27 | 48 h culture in liquid broth; Gram staining | Strong | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 11-12, tang2023rolesoflipopolysaccharide pages 7-11) |
| ΔHP1578 | causes | almost completely coccoid morphology | “G27∆HP1578 and G27∆wecA became almost completely coccoid after 48 h of culture” | *Helicobacter pylori* strain G27 | 48 h culture in liquid broth; Gram staining | Strong | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 11-12, tang2023rolesoflipopolysaccharide pages 7-11) |
| ΔHP1283_or_ΔHP0102_or_ΔHP1284 | causes | coccoid_coiled_c_shape_or_irregular_forms | “G27∆HP1283, G27∆HP0102, and G27∆HP1284 exhibited mixtures of coccoid, coiled ‘c’-shape, and irregular forms” | *Helicobacter pylori* strain G27 | 48 h culture in liquid broth; Gram staining | Strong | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 4-7, tang2023rolesoflipopolysaccharide pages 1-2) |
| wecA_deletion | abolishes | O-antigen | “The wecA deletion also causes loss of the whole O-antigen” | *Helicobacter pylori* | Silver staining; confirmed in 26695, J99, P12 | Strong | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 4-7, tang2023rolesoflipopolysaccharide pages 7-11) |
| HP1578_and_WecA_GlcNAc_transferases | may_indirectly_alter | peptidoglycan_sacculus_and_shape | “blocking GlcNAc use in LPS may redirect precursors to peptidoglycan synthesis and alter cell-wall remodeling” | *Helicobacter pylori* | Mechanistic interpretation from mutant phenotypes | Weak/inferred | 10.3390/ijms241411381; https://doi.org/10.3390/ijms241411381; 2023 | (tang2023rolesoflipopolysaccharide pages 11-12) |
| ccmA_csd1_csd3_mutation | increases | PG cross-linking | “mutants in genes such as ccmA, csd1, and csd3 … ‘had increased levels of cross-linking’” | *Helicobacter pylori* | Prior mutant + muropeptide analyses cited in 2023 review | Moderate; secondary summary | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 15-16) |
| increased_PG_cross-linking | associated_with | curved_rod_rather_than_helical_morphology | “mutants in genes such as ccmA, csd1, and csd3 were associated with altered cell shape (curved rods rather than helical) and ‘had increased levels of cross-linking’” | *Helicobacter pylori* | Prior mutant + muropeptide analyses cited in 2023 review | Moderate; secondary summary | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 15-16) |
| relaxation_of_PG_crosslinking | promotes | helical_shape | “Peptidoglycan crosslinking relaxation promotes Helicobacter pylori's helical shape and stomach colonization” | *Helicobacter pylori* | Prior primary study summarized in 2023–2023 literature | Moderate; secondary summary | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 17-17, richter2023interactingbactofilinsimpact pages 26-27) |
| Csd5 | interacts_with | cell_wall_MurF_and_cytoskeleton | “Csd5 ‘interacts with the cell wall, MurF, and the bacterial cytoskeleton’” | *Helicobacter pylori* | Prior primary study summarized in review | Moderate; secondary summary | 10.1371/journal.pgen.1010788; https://doi.org/10.1371/journal.pgen.1010788; 2023 | (richter2023interactingbactofilinsimpact pages 26-27) |
| CcmA_and_other_cytoskeletal_proteins | define | zones_of_enhanced_cell_wall_synthesis | “Distinct cytoskeletal proteins define zones of enhanced cell wall synthesis in Helicobacter pylori” | *Helicobacter pylori* | Cytoskeletal localization/cell-wall synthesis studies summarized in review | Moderate; secondary summary | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 17-17, richter2023interactingbactofilinsimpact pages 26-27) |
| distinct_zones_of_enhanced_cell_wall_synthesis | contributes_to | helical_cell_shape | “Distinct cytoskeletal proteins define zones of enhanced cell wall synthesis … supporting … localized cell-wall synthesis patterns → helical morphology” | *Helicobacter pylori* | Mechanistic interpretation from cited studies | Moderate; secondary summary | 10.3389/fmicb.2023.1162806; https://doi.org/10.3389/fmicb.2023.1162806; 2023 | (frirdich2023multiplecampylobacterjejuni pages 17-17) |
| Por39_and_Por41 | form | helical_ribbon_like_structure_at_outer_curve | “Por39 and Por41 assemble into a helical ribbon-like structure localized at the outer cell curve” | *Rhodospirillum rubrum* | Imaging/localization in 2024 primary study | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 1-2) |
| Por39_and_Por41 | recruit | PapS | “Por39 and Por41 … recruits PapS” | *Rhodospirillum rubrum* | Imaging/localization in 2024 primary study | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 1-2) |
| PapS | binds | peptidoglycan | “PapS is a periplasmic lipoprotein with a C-terminal OmpA-like peptidoglycan-binding domain” and “PapS … bridges the outer membrane to the peptidoglycan; its OmpA-like domain binds mDAP” | *Rhodospirillum rubrum* | Periplasmic localization assay; PG-binding context | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2) |
| PapS_assemblies | entrap | elongasome_complexes | “Porin–PapS assemblies function as molecular cages that entrap the cell elongation machinery” | *Rhodospirillum rubrum* | Mechanistic primary study; single-molecule and localization analyses | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13) |
| entrapment_of_elongasome | biases | peptidoglycan_insertion_toward_outer_curve | “biasing peptidoglycan insertion and elongasome movement toward the outer curve” | *Rhodospirillum rubrum* | Mechanistic primary study | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 1-2) |
| biased_outer_curve_PG_biosynthesis | establishes | cell_curvature | “creating a longitudinal zone of elevated peptidoglycan biosynthesis that distorts the cell wall cylinder and establishes curvature” | *Rhodospirillum rubrum* | Mechanistic primary study; sacculus analysis | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 2-3) |
| ΔpapS | causes | straight_rod_like_cells | “an in-frame deletion of papS (ΔpapS) produces straight, rod-like cells (loss of curvature)” | *Rhodospirillum rubrum* | Gene deletion; complementation restores curvature | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 2-3) |
| ectopic_papS_expression | restores | curvature | “ectopic expression of papS restores curvature” | *Rhodospirillum rubrum* | Complementation of ΔpapS | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 2-3) |
| Por41_D71S | abolishes | cell_curvature | “por41D71S mutants ‘had completely lost their curved morphology’” | *Rhodospirillum rubrum* | Targeted porin substitution | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 7-8) |
| Por39_D71S | has_no_noticeable_effect_on | cell_curvature | “Por39D71S showed no noticeable effect on cell curvature” | *Rhodospirillum rubrum* | Targeted porin substitution | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 7-8, pohl2024anoutermembrane pages 7-7) |
| PapS_W22A_W58A | abolishes | helical_localization_pattern_of_PapS_and_curved_morphology | “completely abolished the helical localization pattern of PapS-mNG, accompanied by a loss of curved cell morphology” | *Rhodospirillum rubrum* | PapS porin-binding interface mutation | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 9-10) |
| disruption_of_porin_PapS_interface | delocalizes | PapS | “mutations that disrupt porin localization or porin–PapS complex formation delocalize PapS and abolish curvature” | *Rhodospirillum rubrum* | Interface mutants | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 2-3) |
| ΔpapS | increases | elongasome_mobility_and_even_distribution_of_RodZ_foci | “mNG-RodZ foci become more dynamic and evenly distributed, elongasome mobility increases” | *Rhodospirillum rubrum* | Gene deletion; single-molecule tracking/localization | Strong | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 13-14) |
| ~15_percent_bias_in_outer_curve_growth | sufficient_to_generate | observed_curvature | “a modest (~15%) bias toward increased cell-wall growth at the outer curve suffices to generate the observed curvature” | *Rhodospirillum rubrum* | Modeling interpretation | Moderate | 10.1038/s41467-024-51790-z; https://doi.org/10.1038/s41467-024-51790-z; 2024 | (pohl2024anoutermembrane pages 11-12) |
| periplasmic_endoflagella | determine | spiral_flat-wave_cell_shape | “endoflagella anchored at cell poles and running within the periplasm create the flat-wave morphology of Borrelia burgdorferi” | Spirochetes / *Borreliella burgdorferi* | Structural and genetic context in 2024 primary study | Strong | 10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w; 2024 | (zambacampero2024broadlyconservedflgv pages 1-2) |
| periplasmic_flagella | serves_as_cytoskeleton_to_maintain | spiral-shaped_cell_body | “The periplasmic flagella serves as a cytoskeleton to maintain a spiral-shaped cell body” | Spirochetes | Review statement | Moderate | 10.3390/biom14121488; https://doi.org/10.3390/biom14121488; 2024 | (from tool result text on nakamura2024structureanddynamics pages 1-3, summarized in spirochete evidence request) |
| FlgV_BB0268 | localizes_to | flagellar_basal_body | “FlgV localizes to flagellar basal bodies” | *Borreliella burgdorferi* | 2024 primary study | Strong | 10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w; 2024 | (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 2-4) |
| flgV_deletion | reduces | flagellar_filament_number_and_length | “flgV deletion strains have fewer and shorter filaments” | *Borreliella burgdorferi* | Gene deletion mutant | Strong | 10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w; 2024 | (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 2-4) |
| flgV_deletion | causes | motility_and_cell_division_defects | “flgV deletion strains have fewer and shorter filaments and show defects in cell division and motility” | *Borreliella burgdorferi* | Gene deletion mutant | Strong | 10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w; 2024 | (zambacampero2024broadlyconservedflgv pages 1-2) |
| flgB_superoperon | encodes | periplasmic_flagellar_apparatus_components | “a contiguous 'flgB superoperon' … encodes basal body, hook, rod, filament components, motor ATPases, and assembly factors” | *Borreliella burgdorferi* | Operon/genetic architecture | Strong | 10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w; 2024 | (zambacampero2024broadlyconservedflgv pages 2-4) |
| FlhF_and_FlhG | co-conserved_with | FlgV_flagellar_assembly_module | “Comparative genomics shows FlgV homologs co-conserved with flagellar regulators FlhF and FlhG” | Spirochetes / broader bacteria | Comparative genomics | Moderate | 10.1038/s41467-024-54806-w; https://doi.org/10.1038/s41467-024-54806-w; 2024 | (zambacampero2024broadlyconservedflgv pages 2-4) |
| FlhF | regulates | number_configuration_of_periplasmic_flagella | “Flhf … regulates number/configuration of periplasmic flagella” | Spirochetes | Summary of cited genetic analyses in 2023 primary article | Moderate; secondary summary | 10.1093/pnasnexus/pgad349; https://doi.org/10.1093/pnasnexus/pgad349; 2023 | (lynch2023lysinoalaninecrosslinkingis pages 10-11) |
| FlgE_lysinoalanine_crosslink | required_for | motility | “Lal is dispensable for hook assembly but required for motility” | Spirochetes | Comparative primary study across Treponema, Borreliella, Brachyspira, Leptospira | Strong | 10.1093/pnasnexus/pgad349; https://doi.org/10.1093/pnasnexus/pgad349; 2023 | (lynch2023lysinoalaninecrosslinkingis pages 1-2) |
| inability_to_form_FlgE_Lal_crosslink | impairs | motility | “mutant Borreliella burgdorferi strains that cannot form the cross-link are greatly impaired or non-motile” | *Borreliella burgdorferi* | Hook PTM mutant | Strong | 10.1093/pnasnexus/pgad349; https://doi.org/10.1093/pnasnexus/pgad349; 2023 | (lynch2023lysinoalaninecrosslinkingis pages 1-2) |
| FlgE_Lal_crosslink | stabilizes | hook_for_torque_transmission_to_cell_body | “implying the cross-link stabilizes the hook to transmit motor torque to the cell body” | Spirochetes | Mechanistic interpretation from primary PTM study | Moderate | 10.1093/pnasnexus/pgad349; https://doi.org/10.1093/pnasnexus/pgad349; 2023 | (lynch2023lysinoalaninecrosslinkingis pages 1-2) |
| periplasmic_flagella | distort_and_push | cell_body | “spirochete flagella are located inside the periplasm and … their filaments distort and push the cell body” | Spirochetes | General structural mechanism | Strong | 10.1093/pnasnexus/pgad349; https://doi.org/10.1093/pnasnexus/pgad349; 2023 | (lynch2023lysinoalaninecrosslinkingis pages 1-2) |


*Table: This table compiles candidate causal graph edges for the microbial trait 'spiral shaped' across key model systems, using only the supplied evidence contexts. It is structured for TraitMech curation, with mechanism-focused triples, supporting snippets, experimental context, and uncertainty flags.*

**Visual evidence:** Mechanistic model schematic for the Por39/Por41/PapS module (“roadblock model”) is available as Figure 10 from Pöhl et al. 2024. (pohl2024anoutermembrane media 79ad3ada)

---

### 5. Current applications and real-world implementations
#### 5.1 Pathogenesis and host colonization
- *C. jejuni*: The helical morphology “plays a key role in its transmission in the environment, colonization, and pathogenic properties,” making spiral/helical shape a functional trait with direct relevance for infection biology and potentially for intervention strategies that target cell-wall remodeling enzymes. (frirdich2023multiplecampylobacterjejuni pages 1-2)
- *H. pylori*: PG crosslinking state is linked to helical shape and stomach colonization in prior work summarized in recent literature, motivating curation of PG-remodeling and cytoskeletal components as virulence-associated morphogenesis determinants. (frirdich2023multiplecampylobacterjejuni pages 17-17, richter2023interactingbactofilinsimpact pages 26-27)
- Spirochetes (*Borreliella burgdorferi*): Flagellar assembly component FlgV influences dissemination and infection in mice, tying endoflagellar architecture (and thus spiral/flat-wave motility) to in vivo outcomes. (zambacampero2024broadlyconservedflgv pages 1-2)

#### 5.2 Antimicrobial/anti-virulence targeting concepts (evidence-based leads)
- *H. pylori*: LPS glycosyltransferases are proposed as promising drug targets; mutants (notably ΔwecA) show dramatic increases in polymyxin B susceptibility and altered morphology, suggesting envelope glycosylation may be a leverage point affecting both survival and morphology. (tang2023rolesoflipopolysaccharide pages 7-11, tang2023rolesoflipopolysaccharide pages 12-13)
- Spirochetes: FlgE lysinoalanine crosslinking is conserved and required for motility, providing a candidate spirochete-specific vulnerability (motility-linked). (lynch2023lysinoalaninecrosslinkingis pages 1-2)

---

### 6. Statistics and quantitative data from recent studies
- **~15% growth bias sufficiency**: Modeling indicates a ~15% bias toward increased cell-wall growth at the outer curve can generate observed curvature in *R. rubrum*. (pohl2024anoutermembrane pages 11-12)
- **High co-localization of curvature module components**: Porin–PapS complexes show **90.3% overlap** by 3D-SIM colocalization analysis in *R. rubrum*. (pohl2024anoutermembrane pages 7-7)

---

### 7. Expert synthesis/analysis (grounded in authoritative sources)
**Unifying model across helical rods:** multiple independent datasets converge on the idea that **cell-wall remodeling enzymes** (carboxypeptidases/endopeptidases; M23 peptidases) and **cytoskeletal/scaffolding elements** (bactofilins) regulate where and how PG is inserted/relaxed, producing stable curvature or helical pitch. (frirdich2023multiplecampylobacterjejuni pages 2-3, frirdich2023multiplecampylobacterjejuni pages 17-17)

**A key 2024 conceptual advance:** curvature can also be generated by **outer membrane protein patterning** that cages the elongasome from “outside-in,” without requiring specialized curvature-specific PG enzymes; instead, the module modulates the dynamics of the standard elongation machinery (RodZ-associated complexes) to bias growth. (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 11-12)

**Spirochetes remain mechanistically distinct:** their “spiral-shaped” trait is best modeled as a flagellar–cell-body mechanical coupling trait rather than purely PG-encoded curvature; thus, spirochete edges should attach to nodes for **periplasmic flagella, basal body/hook/filament components, and PTMs** that tune mechanical performance. (zambacampero2024broadlyconservedflgv pages 2-4, lynch2023lysinoalaninecrosslinkingis pages 1-2)

---

### 8. Warnings / curation caveats (do not over-curate)
1) **Precursor rerouting hypothesis (UDP-GlcNAc → PG changes)** in *H. pylori* LPS mutants is explicitly presented as a mechanistic proposal rather than direct measurement of PG flux; treat as **weak/inferred** unless confirmed by direct PG composition/flux experiments in the same study. (tang2023rolesoflipopolysaccharide pages 11-12)
2) Several *H. pylori* mechanistic claims about Csd/CcmA/PG crosslinking are **secondary summaries** embedded in the *C. jejuni* paper’s discussion; for high-confidence edges, ideally retrieve and cite the primary *H. pylori* morphogenesis papers directly (not available in the current evidence set). (frirdich2023multiplecampylobacterjejuni pages 15-16, richter2023interactingbactofilinsimpact pages 26-27)
3) **Time dependence**: *H. pylori* LPS mutant morphology changes are prominent at 48 h; curators should include an explicit “culture age/timepoint” condition node or qualifier to avoid mis-annotation of baseline morphology. (tang2023rolesoflipopolysaccharide pages 4-7)

---

## DOI-first bibliography (with publication dates and URLs)
1. Pöhl S, et al. *An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in Rhodospirillum rubrum.* **Nature Communications**. **Sep 2024**. DOI: **10.1038/s41467-024-51790-z**. URL: https://doi.org/10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2)
2. Zamba-Campero M, et al. *Broadly conserved FlgV controls flagellar assembly and Borrelia burgdorferi dissemination in mice.* **Nature Communications**. **Nov 2024**. DOI: **10.1038/s41467-024-54806-w**. URL: https://doi.org/10.1038/s41467-024-54806-w (zambacampero2024broadlyconservedflgv pages 1-2)
3. Tang X, et al. *Roles of Lipopolysaccharide Glycosyltransferases in Maintenance of Helicobacter pylori Morphology, Cell Wall Permeability, and Antimicrobial Susceptibilities.* **International Journal of Molecular Sciences**. **Jul 2023**. DOI: **10.3390/ijms241411381**. URL: https://doi.org/10.3390/ijms241411381 (tang2023rolesoflipopolysaccharide pages 1-2)
4. Frirdich E, et al. *Multiple Campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature.* **Frontiers in Microbiology**. **Apr 2023**. DOI: **10.3389/fmicb.2023.1162806**. URL: https://doi.org/10.3389/fmicb.2023.1162806 (frirdich2023multiplecampylobacterjejuni pages 1-2)
5. Lynch MJ, et al. *Lysinoalanine cross-linking is a conserved post-translational modification in the spirochete flagellar hook.* **PNAS Nexus**. **Oct 2023**. DOI: **10.1093/pnasnexus/pgad349**. URL: https://doi.org/10.1093/pnasnexus/pgad349 (lynch2023lysinoalaninecrosslinkingis pages 1-2)

---

### Notes for `spiral_shaped.yaml` implementation
- Consider modeling **two subgraphs** under the same trait: (i) PG-driven helical rods; (ii) endoflagella-driven spirochetes. Crosslinks between the subgraphs should be limited to high-level nodes (e.g., “spiral-shaped morphology”) unless taxon-specific constraints are intended.
- Include explicit condition nodes for **culture age** and **chemical selection (CFW)** where edges are time/assay dependent.


References

1. (frirdich2023multiplecampylobacterjejuni pages 1-2): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 10 citations and is from a peer-reviewed journal.

2. (frirdich2023multiplecampylobacterjejuni pages 17-17): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 10 citations and is from a peer-reviewed journal.

3. (frirdich2023multiplecampylobacterjejuni pages 15-16): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 10 citations and is from a peer-reviewed journal.

4. (zambacampero2024broadlyconservedflgv pages 1-2): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

5. (lynch2023lysinoalaninecrosslinkingis pages 1-2): Michael J Lynch, Maithili Deshpande, Kurni Kurniyati, Kai Zhang, Milinda James, Michael Miller, Sheng Zhang, Felipe J Passalia, Elsio A Wunder, Nyles W Charon, Chunhao Li, and Brian R Crane. Lysinoalanine cross-linking is a conserved post-translational modification in the spirochete flagellar hook. PNAS Nexus, Oct 2023. URL: https://doi.org/10.1093/pnasnexus/pgad349, doi:10.1093/pnasnexus/pgad349. This article has 4 citations and is from a peer-reviewed journal.

6. (frirdich2023multiplecampylobacterjejuni pages 2-3): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 10 citations and is from a peer-reviewed journal.

7. (tang2023rolesoflipopolysaccharide pages 4-7): Xiaoqiong Tang, Tiankuo Yang, Yalin Shen, Xiaona Song, Mohammed Benghezal, Barry J. Marshall, Hong Tang, and Hong Li. Roles of lipopolysaccharide glycosyltransferases in maintenance of helicobacter pylori morphology, cell wall permeability, and antimicrobial susceptibilities. International Journal of Molecular Sciences, 24:11381, Jul 2023. URL: https://doi.org/10.3390/ijms241411381, doi:10.3390/ijms241411381. This article has 13 citations.

8. (tang2023rolesoflipopolysaccharide pages 11-12): Xiaoqiong Tang, Tiankuo Yang, Yalin Shen, Xiaona Song, Mohammed Benghezal, Barry J. Marshall, Hong Tang, and Hong Li. Roles of lipopolysaccharide glycosyltransferases in maintenance of helicobacter pylori morphology, cell wall permeability, and antimicrobial susceptibilities. International Journal of Molecular Sciences, 24:11381, Jul 2023. URL: https://doi.org/10.3390/ijms241411381, doi:10.3390/ijms241411381. This article has 13 citations.

9. (frirdich2023multiplecampylobacterjejuni pages 3-5): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 10 citations and is from a peer-reviewed journal.

10. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

11. (pohl2024anoutermembrane pages 2-3): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

12. (pohl2024anoutermembrane pages 12-13): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (pohl2024anoutermembrane pages 11-12): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

14. (pohl2024anoutermembrane media 79ad3ada): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

15. (tang2023rolesoflipopolysaccharide pages 1-2): Xiaoqiong Tang, Tiankuo Yang, Yalin Shen, Xiaona Song, Mohammed Benghezal, Barry J. Marshall, Hong Tang, and Hong Li. Roles of lipopolysaccharide glycosyltransferases in maintenance of helicobacter pylori morphology, cell wall permeability, and antimicrobial susceptibilities. International Journal of Molecular Sciences, 24:11381, Jul 2023. URL: https://doi.org/10.3390/ijms241411381, doi:10.3390/ijms241411381. This article has 13 citations.

16. (tang2023rolesoflipopolysaccharide pages 12-13): Xiaoqiong Tang, Tiankuo Yang, Yalin Shen, Xiaona Song, Mohammed Benghezal, Barry J. Marshall, Hong Tang, and Hong Li. Roles of lipopolysaccharide glycosyltransferases in maintenance of helicobacter pylori morphology, cell wall permeability, and antimicrobial susceptibilities. International Journal of Molecular Sciences, 24:11381, Jul 2023. URL: https://doi.org/10.3390/ijms241411381, doi:10.3390/ijms241411381. This article has 13 citations.

17. (zambacampero2024broadlyconservedflgv pages 2-4): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

18. (tang2023rolesoflipopolysaccharide pages 7-11): Xiaoqiong Tang, Tiankuo Yang, Yalin Shen, Xiaona Song, Mohammed Benghezal, Barry J. Marshall, Hong Tang, and Hong Li. Roles of lipopolysaccharide glycosyltransferases in maintenance of helicobacter pylori morphology, cell wall permeability, and antimicrobial susceptibilities. International Journal of Molecular Sciences, 24:11381, Jul 2023. URL: https://doi.org/10.3390/ijms241411381, doi:10.3390/ijms241411381. This article has 13 citations.

19. (richter2023interactingbactofilinsimpact pages 26-27): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

20. (pohl2024anoutermembrane pages 7-8): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

21. (pohl2024anoutermembrane pages 7-7): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

22. (pohl2024anoutermembrane pages 9-10): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

23. (pohl2024anoutermembrane pages 13-14): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

24. (lynch2023lysinoalaninecrosslinkingis pages 10-11): Michael J Lynch, Maithili Deshpande, Kurni Kurniyati, Kai Zhang, Milinda James, Michael Miller, Sheng Zhang, Felipe J Passalia, Elsio A Wunder, Nyles W Charon, Chunhao Li, and Brian R Crane. Lysinoalanine cross-linking is a conserved post-translational modification in the spirochete flagellar hook. PNAS Nexus, Oct 2023. URL: https://doi.org/10.1093/pnasnexus/pgad349, doi:10.1093/pnasnexus/pgad349. This article has 4 citations and is from a peer-reviewed journal.