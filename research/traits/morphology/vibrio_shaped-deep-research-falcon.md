---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:55:47.012635'
end_time: '2026-08-04T15:09:41.623927'
duration_seconds: 834.61
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: vibrio shaped
  trait_identifier: METPO:1000686
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: vibrio_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a curved rod or comma morphology,
    characterized by a short curved cylindrical form with a single arc.
  parent_traits: METPO:1000666
  synonyms: vibrio, vibrio-shaped
  evidence_summary: 'DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic
    curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature
    mechanism in Vibrio cholerae.)'
  causal_graph_summary: 'vibrio_shaped_crvA_curvature: 10 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** vibrio shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000686
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc.
- **Parent traits:** METPO:1000666
- **Synonyms:** vibrio, vibrio-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature mechanism in Vibrio cholerae.)
- **Existing causal graph summary:** vibrio_shaped_crvA_curvature: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **vibrio shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/vibrio_shaped.yaml`.

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
- **Trait label:** vibrio shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000686
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc.
- **Parent traits:** METPO:1000666
- **Synonyms:** vibrio, vibrio-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature mechanism in Vibrio cholerae.)
- **Existing causal graph summary:** vibrio_shaped_crvA_curvature: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **vibrio shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/vibrio_shaped.yaml`.

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


# Vibrio-Shaped Microbial Trait Research Report
## TraitMech Curation Template for METPO:1000686

---

## Executive Summary

This report synthesizes current mechanistic understanding of the vibrio-shaped (comma-like curved rod) morphology trait for curation into the TraitMech causal graph database. The vibrio-shaped trait (METPO:1000686) is characterized by a single-arc curvature distinguishing it from multi-arc helical morphologies and straight rods. Research identifies three distinct mechanistic modules across bacterial taxa: (1) the CrvAB periplasmic filament system in *Vibrio cholerae* regulated by c-di-GMP and stress-responsive pathways, (2) the Bd1075 LD-carboxypeptidase-mediated asymmetric peptidoglycan editing in *Bdellovibrio bacteriovorus*, and (3) the outer-membrane porin-lipoprotein elongasome-trapping complex in *Rhodospirillum rubrum* described in 2024 (fernandez2020vibriocholeraeadapts pages 1-1, nikolai2020rnamediatedcontrolof pages 1-2, banks2022asymmetricpeptidoglycanediting pages 1-2, pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2).

---

## 1. Trait Scope and Boundaries

### 1.1 Phenotype Definition

**Vibrio-shaped morphology** (METPO:1000686) is defined as a cell shape exhibiting a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc. The trait is exemplified by *Vibrio cholerae*, which displays a "characteristic curved rod morphology" or "comma-shaped cell morphology" (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 1-1). The curvature represents a stable structural property encoded in the peptidoglycan cell wall architecture, as purified peptidoglycan sacculi from wild-type curved cells retain curvature ex vivo (pohl2024anoutermembrane pages 2-3).

### 1.2 Boundary Cases

**Distinction from helical morphology:** Vibrio-shaped cells possess a single arc along the cell length, contrasting with multi-arc helical spirals characteristic of *Campylobacter jejuni* and *Helicobacter pylori*, which employ distinct peptidoglycan hydrolase-based mechanisms to generate multiple turns (banks2022asymmetricpeptidoglycanediting pages 1-2).

**Straight rod state as regulatory alternative:** Vibrio-shaped cells can transition to straight rod morphology under specific regulatory or environmental conditions. In *V. cholerae*, elevated intracellular cyclic di-GMP concentrations "drive curved *V. cholerae* to adopt a straight cell morphology that is advantageous to a sessile biofilm lifestyle," demonstrating active shape modulation between curved and straight states (fernandez2020vibriocholeraeadapts pages 1-1). Deletion of curvature determinants such as *crvA* in *V. cholerae* or *bd1075* in *B. bacteriovorus* produces constitutively straight cells (nikolai2020rnamediatedcontrolof pages 1-2, banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11).

### 1.3 Taxonomic Distribution and Mechanisms

Three mechanistically distinct systems generate vibrio-shaped morphology:

1. **CrvAB periplasmic polymer module** (*Vibrio cholerae*, *NCBITaxon:666*): Periplasmic intermediate filament-like proteins forming asymmetric structures (nikolai2020rnamediatedcontrolof pages 1-2, martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9).

2. **Bd1075 LD-carboxypeptidase localization** (*Bdellovibrio bacteriovorus*, *NCBITaxon:959*): Asymmetric peptidoglycan hydrolysis at the outer convex face via NTF2 domain-mediated localization (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 2-4).

3. **Por39/Por41/PapS elongasome trapping** (*Rhodospirillum rubrum*, *NCBITaxon:1085*): Outer-membrane porin-lipoprotein complexes that cage elongation machinery at the outer curve, biasing peptidoglycan synthesis (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 1-2).

---

## 2. Causal Graph Entities

### 2.1 Genes and Proteins

#### *Vibrio cholerae* Module

- **CrvA** (label-only; species-specific identifier): Periplasmic intermediate filament-like protein; polymerizes in periplasm; "determines cell curvature" and "decreases net growth on the minor axis relative to the major axis" (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 2-3, herzog2020smallregulatoryrnas pages 37-43).

- **CrvB** (label-only; species-specific identifier): Cooperates with CrvA; "promotes higher-order CrvA polymerization in dose-dependent fashion"; colocalized in periplasmic filaments at inner cell curvature (martin2020theevolutionof pages 5-9, martin2020theevolutionof pages 11-18).

- **VadR** (label-only; small regulatory RNA): Post-transcriptional inhibitor; "VadR small RNA (sRNA) as a post-transcriptional inhibitor of the *crvA* mRNA"; mutation increases curvature, overexpression decreases curvature (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

- **VxrAB** (label-only; two-component system): Transcriptional activator; "*vadR* transcription is activated by the VxrAB two-component system" (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

- **VpsR** (label-only; transcription factor): c-di-GMP-responsive regulator; "Loss of *vpsR* abolishes c-di-GMP-mediated curvature reduction"; "directly activates *vpsT* transcription" (fernandez2020vibriocholeraeadapts pages 2-3).

- **VpsT** (label-only; transcription factor): c-di-GMP-binding transcription factor; "VpsT overexpression can decrease curvature independently of c-di-GMP concentration" (fernandez2020vibriocholeraeadapts pages 2-3).

#### *Bdellovibrio bacteriovorus* Module

- **Bd1075** (label-only; species-specific): LD-carboxypeptidase (*EC:3.4.17.-* candidate); "exerting LD-carboxypeptidase activity upon the predator cell wall"; "localizes specifically to the outer convex face"; deletion produces straight rod morphology (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 2-4).

- **Bd1075 NTF2 domain** (nuclear transport factor 2-like domain; residues 196–304): "The NTF2 domain is necessary for proper localization" and "asymmetric targeting to the outer convex cell face" (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11).

#### *Rhodospirillum rubrum* Module (2024)

- **PapS** (label-only; peptidoglycan-associated protein, lipoprotein): Contains OmpA-like peptidoglycan-binding domain (*GO:0008658* candidate: peptidoglycan binding); "localizes exclusively to the outer curve of cells…in a continuous ribbon-like helical structure"; ">15,000 copies per cell"; deletion produces straight cells (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 4-5, pohl2024anoutermembrane pages 1-2).

- **Por39** and **Por41** (label-only; outer membrane porins): Form helical assemblies; "Por39 and Por41 form a helical ribbon-like structure…and recruit the peptidoglycan-binding lipoprotein PapS"; "Por41 mutations completely abolish cell curvature" (pohl2024anoutermembrane pages 9-10, pohl2024anoutermembrane pages 1-2).

- **RodZ** (label-only; elongasome component): Marker of elongation machinery; "RodZ protein…shows strong enrichment at the outer curve" in wild-type cells; "In Δ*papS* deletion mutants, RodZ localization becomes evenly distributed" (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 10-11).

### 2.2 Small Molecules and Metabolites

- **Cyclic di-GMP (c-di-GMP)** (*CHEBI:58805*): Second messenger; "c-di-GMP reduces cell curvature in a dose-dependent manner" via post-transcriptional repression of *crvA* (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 2-3).

- **meso-Diaminopimelic acid (mDAP)** (*CHEBI:16488* candidate): Peptidoglycan crosslinker; PapS "specifically interacts with meso-diaminopimelic acid (mDAP) residues in peptidoglycan" via R223 residue (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 4-5).

- **Cell-wall-targeting antibiotics (β-lactams, e.g., penicillin G)**: Environmental stimuli; "triggered by cell-wall-targeting antibiotics" inducing VxrAB-mediated *vadR* transcription; cells deficient in VadR-mediated *crvA* repression "display decreased survival upon challenge with penicillin G" (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

### 2.3 Cellular Structures and Localizations

- **Periplasm** (*GO:0042597*): Subcellular localization; "CrvA protein localizes to the periplasmic space where it polymerizes" (herzog2020smallregulatoryrnas pages 37-43).

- **Peptidoglycan (cell wall)** (*GO:0009274* peptidoglycan-based cell wall; *GO:0008360* peptidoglycan metabolic process): Structural macromolecule; asymmetric editing or synthesis generates curvature (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 12-12, pohl2024anoutermembrane pages 2-3).

- **Elongasome (cell elongation machinery)**: Multi-protein complex; CrvAB module "functions autonomously from core shape machineries" (MreB-driven elongasome); R. rubrum porin-PapS assemblies "entrap the cell elongation machinery" (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9, pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 1-2).

### 2.4 Biological Processes

- **Cell shape determination** (*GO:0008360* regulation of cell shape candidate): Overarching process.

- **Asymmetric peptidoglycan growth/synthesis**: CrvA "decreases net growth on the minor axis relative to the major axis"; porin-PapS assemblies "bias growth toward the outer curve" (fernandez2020vibriocholeraeadapts pages 2-3, pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2).

- **Asymmetric peptidoglycan editing**: "Asymmetric peptidoglycan editing generates cell curvature" in *B. bacteriovorus* via Bd1075 LD-carboxypeptidase activity (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 12-12).

- **Biofilm formation** (*GO:0042710*): VadR "inhibits biofilm formation"; high c-di-GMP promotes straight morphology "advantageous to a sessile biofilm lifestyle" (fernandez2020vibriocholeraeadapts pages 1-1, nikolai2020rnamediatedcontrolof pages 1-2).

- **Bacterial motility** (*GO:0071973*): "Curved rods swim 5.5% faster than straight rods" (95% CI [5.5%, 5.9%], *P*<1e-5); curved morphology "promotes motility in dense hydrogels" (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 5-6).

- **Pathogenesis/virulence**: Curved morphology "promotes infectivity"; *crvA* deletion mutants show "attenuated colonization in animal infection models" and "reduced virulence" (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

- **Prey invasion** (predatory bacteria): "Curved wild-type predators invade prey significantly faster (median 4.0 min) than rod-shaped Δ*bd1075* mutants (median 6.0 min, *p* < 0.0001)" (banks2022asymmetricpeptidoglycanediting pages 2-4).

### 2.5 Environmental and Experimental Factors

- **Cell density / quorum sensing**: CrvA is "a quorum sensing-regulated gene with higher expression in high cell density (HCD) state" (fernandez2020vibriocholeraeadapts pages 5-6).

- **Cell-wall stress / β-lactam antibiotics**: Induce VxrAB-VadR pathway to repress *crvA* and modulate shape for antibiotic survival (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

- **Lifestyle transition (motile vs. sessile)**: Curvature associated with planktonic motility; straight morphology with biofilm formation (fernandez2020vibriocholeraeadapts pages 1-1).

---

## 3. Evidence-Backed Causal Edges

The following edges represent source-verified mechanistic relationships suitable for TraitMech curation. A comprehensive table of 40 edges is provided in **Artifact artifact-00** embedded below.

| Subject | Predicate | Object | Taxon | Reference | Snippet | Notes |
|---|---|---|---|---|---|---|
| CrvA | required_for | vibrio-shaped curvature | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "Periplasmic protein CrvA determines cell curvature" | Strong, direct phenotype-gene link; taxon-specific to *V. cholerae*. |
| CrvA | localizes_to | periplasm | *Vibrio cholerae* | Herzog, 2020 dissertation, DOI:10.5282/edoc.27302 (herzog2020smallregulatoryrnas pages 37-43) | "CrvA protein localizes to the periplasmic space" | Dissertation support; use as lower-priority corroboration unless matched to peer-reviewed source. |
| CrvA | polymerizes_in | periplasm | *Vibrio cholerae* | Herzog, 2020 dissertation, DOI:10.5282/edoc.27302 (herzog2020smallregulatoryrnas pages 37-43) | "where it polymerizes to promote cell bending/curvature" | Useful mechanistic detail, but source is dissertation; curate cautiously if peer-reviewed quote unavailable. |
| CrvA | decreases_net_growth_on | minor cell axis relative to major axis | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 2-3) | "generates curvature by decreasing net growth on the minor axis relative to the major axis" | Strong mechanistic edge connecting CrvA to asymmetric wall growth. |
| CrvA | sufficient_with_CrvB_to_induce | curvature | *Vibrio cholerae* and heterologous Gram-negative hosts | Martin et al., 2020 preprint for Nat Microbiol 2021, DOI:10.1101/2020.02.20.954503 (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 11-18) | "CrvA and CrvB form a two-protein module essential and sufficient for bacterial cell curvature" | Strong but quoted from preprint summary; final peer-reviewed article is Nat Microbiol 2021 DOI:10.1038/s41564-021-00924-w. |
| CrvA | colocalizes_with | CrvB in periplasmic filament | *Vibrio cholerae* | Martin et al., 2020 preprint, DOI:10.1101/2020.02.20.954503 (martin2020theevolutionof pages 5-9, martin2020theevolutionof pages 11-18) | "Both proteins colocalize to periplasmic filaments at the inner cell curvature" | Taxon-specific module architecture; source is preprint-derived evidence. |
| CrvB | promotes | higher-order CrvA polymerization | *Vibrio cholerae* | Martin et al., 2020 preprint, DOI:10.1101/2020.02.20.954503 (martin2020theevolutionof pages 5-9) | "CrvB promotes higher-order CrvA polymerization in dose-dependent fashion" | Mechanistic and specific; peer-reviewed confirmation desirable before strict curation. |
| CrvAB module | functions_independently_of | MreB/FtsZ core elongation/division machineries | *Vibrio cholerae* | Martin et al., 2020 preprint, DOI:10.1101/2020.02.20.954503 (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9) | "functions autonomously from core shape machineries" | Important boundary: curvature is not merely generic elongasome/divisome output. |
| elevated c-di-GMP | decreases | cell curvature | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 2-3) | "c-di-GMP reduces cell curvature in a dose-dependent manner" | Strong regulatory edge. |
| elevated c-di-GMP | reduces | crvA mRNA abundance | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 2-3) | "crvA mRNA abundance decreased ~1.5-fold at high c-di-GMP conditions" | Strong post-transcriptional regulatory evidence. |
| VpsR | required_for | c-di-GMP-dependent curvature reduction | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 2-3) | "Loss of vpsR abolishes c-di-GMP-mediated curvature reduction" | Strong regulatory necessity edge. |
| VpsR | activates | vpsT transcription | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 2-3) | "VpsR, which directly activates vpsT transcription" | Supports hierarchy VpsR → VpsT in curvature regulation. |
| VpsT | sufficient_to_decrease | curvature | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 2-3) | "VpsT overexpression can decrease curvature independently of c-di-GMP concentration" | Strong sufficiency edge. |
| high c-di-GMP / sessile program | promotes | straight rod morphology | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 1-1) | "drives curved V. cholerae to adopt a straight cell morphology that is advantageous to a sessile biofilm lifestyle" | Trait boundary case: straight rods are alternative regulated state. |
| VadR sRNA | inhibits | crvA mRNA | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "VadR small RNA (sRNA) as a post-transcriptional inhibitor of the crvA mRNA" | Strong direct regulatory edge. |
| vadR mutation | increases | cell curvature | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "Mutation of vadR increases cell curvature" | Strong genotype-phenotype support. |
| VadR overexpression | decreases | cell curvature | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "whereas overexpression has the inverse effect" | Complements deletion/mutation evidence. |
| VxrAB two-component system | activates_transcription_of | vadR | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "vadR transcription is activated by the VxrAB two-component system" | Strong upstream regulation edge. |
| cell-wall-targeting antibiotics | induce | vadR transcription | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "triggered by cell-wall-targeting antibiotics" | Environmental/experimental factor; assay context should be retained. |
| failure to repress crvA via VadR | decreases_survival_upon | penicillin G challenge | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "display decreased survival upon challenge with penicillin G" | Strong condition-specific fitness edge; antibiotic context essential. |
| VadR | inhibits | biofilm formation | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "thereby inhibits biofilm formation in V. cholerae" | Broader program coordination, not shape-exclusive. |
| curved morphology | promotes | infectivity | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2) | "curved rod morphology, which promotes infectivity" | Functional consequence; likely taxon- and host-assay-specific. |
| curved morphology | promotes | motility in dense hydrogels | *Vibrio cholerae* | Peschek et al., 2020, Nature Communications, DOI:10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2) | "promotes infectivity and motility in dense hydrogels" | Assay/environment-specific; curate with condition note. |
| curved cells | swim_faster_than | straight ΔcrvA cells | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 5-6) | "Curved rods swim 5.5% faster than straight rods" | Quantitative phenotype-function edge; strong. |
| CrvA deletion | reduces | soft-agar migration | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 1-2) | "Mutants lacking CrvA produce straight rods with reduced migration in soft agar" | Functional evidence for morphology-linked motility. |
| CrvA deletion | reduces | virulence/colonization | *Vibrio cholerae* | Fernandez et al., 2020, PNAS, DOI:10.1073/pnas.2010199117; Peschek et al., 2020, Nat Commun (fernandez2020vibriocholeraeadapts pages 1-2, herzog2020smallregulatoryrnas pages 37-43) | "reduced virulence in animal infection models" / "attenuated colonization in animal models" | Strong but host-model-specific; keep assay context. |
| Bd1075 | has_molecular_function | LD-carboxypeptidase activity on peptidoglycan | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11) | "exerting LD-carboxypeptidase activity" | Distinct non-CrvA mechanism; taxon-specific. |
| Bd1075 | localizes_to | outer convex cell face | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 2-4) | "localizes specifically to the outer convex face" | Strong localization-mechanism edge. |
| Bd1075 NTF2 domain | required_for | asymmetric targeting/localization | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11) | "The NTF2 domain is necessary for proper localization" | Strong domain-function relationship. |
| Bd1075 | generates | cell curvature by asymmetric peptidoglycan editing | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 12-12) | "Asymmetric peptidoglycan editing generates cell curvature" | Mechanistic core of Bdellovibrio module. |
| bd1075 deletion | causes | straight rod morphology | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11) | "Δbd1075 deletion mutants ... adopt straight rod morphology" | Strong direct phenotype effect. |
| wild-type curvature | greater_than | Δbd1075 curvature | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 2-4) | "0.64 A.U. compared to 0.11 A.U." / "0.29 A.U. ... compared to ... 0.17 A.U." | Quantitative support exists from different analyses/pages; retain one metric in curation notes. |
| curved wild type | invades_prey_faster_than | rod-shaped Δbd1075 mutant | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 2-4) | "median 4.0 min" vs "median 6.0 min" | Strong fitness consequence linked to curvature. |
| Δbd1075 mutant | deforms | prey bdelloplasts | *Bdellovibrio bacteriovorus* | Banks et al., 2022, Nature Communications, DOI:10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 2-4) | "stretch and deform the invaded prey cell from within" | Secondary consequence; useful but less central to trait definition. |
| Por39/Por41 porins | recruit | PapS | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 10-11) | "Por39 and Por41 form a helical ribbon-like structure ... and recruit the peptidoglycan-binding lipoprotein PapS" | Recent 2024 mechanistically distinct module; taxon-specific. |
| PapS | localizes_to | outer curve in helical ribbon-like assemblies | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 4-5) | "localizes exclusively to the outer curve of cells ... in a continuous ribbon-like helical structure" | Strong localization edge. |
| PapS | binds | peptidoglycan mDAP via OmpA-like domain | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 4-5) | "specifically interacts with meso-diaminopimelic acid (mDAP) residues in peptidoglycan" | Good ontology candidate for PG binding; highly specific. |
| PapS R223 | required_for | mDAP binding and cell bending activity | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 4-5) | "A mutation in R223 abolishes mDAP binding and cell-bending activity" | Strong residue-level support. |
| PapS W22/W58 interface | required_for | PapS helical localization and curved morphology | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 9-10) | "W22A/W58A completely abolish PapS helical localization and curved morphology" | Strong structure-function evidence. |
| PapS inactivation | causes | straight rod-like cells | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2) | "Deletion of papS results in straight, rod-like cells" | Strong direct phenotype effect. |
| Por41 mutation | abolishes | cell curvature | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 9-10) | "Por41 mutations completely abolish cell curvature" | Strong, but specific mutated residues/alleles should be retained. |
| porin-PapS assemblies | entrap | elongasome complexes | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 13-14) | "assemblies function as molecular cages that entrap the cell elongation machinery" | Strong mechanistic edge; recent and high value for graph expansion. |
| porin-PapS assemblies | bias | growth toward outer curve | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2) | "biasing growth toward the outer curve" | Strong causal link from complex to asymmetric PG synthesis. |
| PapS | enriches/stabilizes | RodZ at outer curve | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 10-11) | "RodZ protein ... shows strong enrichment at the outer curve" | Supports elongasome subnode (RodZ) in graph. |
| ΔpapS | increases_mobility_and_even_distribution_of | RodZ/elongasome | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 13-14) | "In ΔpapS deletion mutants, RodZ localization becomes evenly distributed" | Strong perturbational support for PapS-dependent trapping. |
| asymmetric peptidoglycan remodeling | sufficient_to_preserve | curved sacculus shape ex vivo | *Rhodospirillum rubrum* | Pöhl et al., 2024, Nature Communications, DOI:10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 2-3) | "Purified peptidoglycan sacculi from wild-type cells retain curvature" | Strong indication curvature is encoded in wall architecture, not transient bending. |


*Table: This table compiles curation-ready, evidence-backed causal triples for vibrio-shaped morphology across three mechanistic systems: the CrvAB module and its regulation in *Vibrio cholerae*, Bd1075-dependent asymmetric peptidoglycan editing in *Bdellovibrio bacteriovorus*, and the Por39/Por41/PapS elongasome-trapping module in *Rhodospirillum rubrum*. It is useful for drafting TraitMech graph edges with direct quotes, perturbation context, and taxon-specific cautions.*

### 3.1 Key Highlights from Causal Edges

#### 3.1.1 *Vibrio cholerae* CrvAB Module

**Core morphogenetic pathway:**

- CrvA → vibrio-shaped curvature (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- CrvA + CrvB → curvature (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 11-18).
- CrvA localizes to periplasm and polymerizes; CrvB promotes higher-order CrvA polymerization (martin2020theevolutionof pages 5-9, herzog2020smallregulatoryrnas pages 37-43).
- CrvA decreases net growth on minor cell axis relative to major axis, generating asymmetric curvature (fernandez2020vibriocholeraeadapts pages 2-3).
- CrvAB module functions independently of MreB/FtsZ core elongation/division machineries (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9).

**c-di-GMP regulatory pathway:**

- Elevated c-di-GMP → reduced cell curvature (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 2-3).
- Elevated c-di-GMP → reduced *crvA* mRNA (fernandez2020vibriocholeraeadapts pages 2-3).
- VpsR required for c-di-GMP-dependent curvature reduction; VpsR → VpsT transcription (fernandez2020vibriocholeraeadapts pages 2-3).
- VpsT overexpression sufficient to decrease curvature independently of c-di-GMP (fernandez2020vibriocholeraeadapts pages 2-3).
- High c-di-GMP/sessile program → straight rod morphology (fernandez2020vibriocholeraeadapts pages 1-1).

**VxrAB-VadR antibiotic-responsive pathway:**

- VxrAB two-component system → *vadR* transcription activation (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- Cell-wall-targeting antibiotics (β-lactams) → VxrAB-mediated *vadR* induction (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- VadR sRNA → post-transcriptional inhibition of *crvA* mRNA (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- *vadR* mutation → increased curvature; VadR overexpression → decreased curvature (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- Failure to repress *crvA* via VadR → decreased survival upon penicillin G challenge (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- VadR → inhibition of biofilm formation (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

**Functional consequences:**

- Curved morphology → enhanced motility in dense hydrogels and enhanced infectivity (nikolai2020rnamediatedcontrolof pages 1-2).
- Curved cells swim 5.5% faster than straight Δ*crvA* cells (fernandez2020vibriocholeraeadapts pages 5-6).
- *crvA* deletion → reduced soft-agar migration, reduced virulence/colonization in animal models (fernandez2020vibriocholeraeadapts pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

#### 3.1.2 *Bdellovibrio bacteriovorus* Bd1075 LD-Carboxypeptidase Module (2022)

**Core morphogenetic pathway:**

- Bd1075 → LD-carboxypeptidase activity on peptidoglycan (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11).
- Bd1075 → asymmetric localization to outer convex cell face via NTF2 domain (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11).
- Bd1075 NTF2 domain → required for asymmetric targeting/localization (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11).
- Bd1075 → asymmetric peptidoglycan editing → cell curvature (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 12-12).
- Δ*bd1075* → straight rod morphology (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 2-4).

**Functional consequences:**

- Wild-type curved cells → faster prey invasion (median 4.0 min) compared to Δ*bd1075* straight cells (banks2022asymmetricpeptidoglycanediting pages 2-4).
- Δ*bd1075* mutants → prey bdelloplast deformation (banks2022asymmetricpeptidoglycanediting pages 2-4).

#### 3.1.3 *Rhodospirillum rubrum* Por39/Por41/PapS Elongasome-Trapping Module (2024)

**Core morphogenetic pathway (recent work):**

- Por39 and Por41 porins → recruit PapS lipoprotein (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 10-11).
- PapS → localization to outer curve in helical ribbon-like assemblies (pohl2024anoutermembrane pages 4-5).
- PapS OmpA-like domain → peptidoglycan binding via mDAP interaction (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 4-5).
- PapS R223 → required for mDAP binding and cell-bending activity (pohl2024anoutermembrane pages 4-5).
- PapS W22/W58 interface → required for helical localization and curved morphology (pohl2024anoutermembrane pages 9-10).
- Porin-PapS assemblies → entrapment of elongasome complexes (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 10-11).
- Porin-PapS assemblies → bias growth toward outer curve (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2).
- Δ*papS* → straight rod-like cells (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2).
- Por41 mutation → abolishes cell curvature; double porin mutations → eliminate PapS localization (pohl2024anoutermembrane pages 9-10).
- Δ*papS* → increased RodZ/elongasome mobility and even distribution (pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 13-14).

**Structural encoding:**

- Purified peptidoglycan sacculi from wild-type cells retain curvature ex vivo, confirming asymmetric peptidoglycan remodeling encodes curvature in wall architecture (pohl2024anoutermembrane pages 2-3).

---

## 4. Ontology Grounding Candidates

Below are suggested stable ontology CURIEs for nodes where grounding confidence is high. Protein-specific nodes lacking cross-species stable identifiers are left as label-only candidates for curator judgment.

| Node Label | Suggested CURIE(s) | Confidence | Notes |
|------------|-------------------|------------|-------|
| vibrio-shaped curvature | METPO:1000686 | High | Target trait; existing definition. |
| peptidoglycan binding | GO:0008658 | High | PapS OmpA-like domain function. |
| peptidoglycan-based cell wall | GO:0009274 | High | Structural substrate. |
| peptidoglycan metabolic process | GO:0008360 | High | Parent process for asymmetric synthesis/editing. |
| periplasm | GO:0042597 | High | Localization of CrvA, CrvB, PapS, Bd1075. |
| biofilm formation | GO:0042710 | High | Functional consequence regulated by VadR and c-di-GMP. |
| bacterial motility | GO:0071973 | High | Functional consequence enhanced by curvature. |
| cyclic di-GMP | CHEBI:58805 | High | Second messenger in *V. cholerae* regulation. |
| meso-diaminopimelic acid | CHEBI:16488 | Medium-High | PG crosslinker; PapS binding target (confirm stereochemistry). |
| LD-carboxypeptidase activity | EC:3.4.17.- | Medium | Bd1075 function; specific subclass may refine. |
| *Vibrio cholerae* | NCBITaxon:666 | High | Taxon-specific nodes. |
| *Bdellovibrio bacteriovorus* | NCBITaxon:959 | High | Taxon-specific nodes. |
| *Rhodospirillum rubrum* | NCBITaxon:1085 | High | Taxon-specific nodes. |
| CrvA, CrvB, VadR, VpsR, VpsT, VxrA, VxrB, Bd1075, PapS, Por39, Por41, RodZ | Label-only | N/A | Species-specific protein labels; curators may consult UniProt or strain-specific databases but should not invent CURIEs. |

---

## 5. Current Understanding and Recent Developments

### 5.1 Key Concepts (2020–2024)

**Modular morphogenesis:**  
The discovery that CrvA and CrvB form a "curvature-inducing module sufficient to induce cell shape complexity in Gram-negative bacteria" spanning 2.5 billion years of evolution (heterologous function in *E. coli*, *P. aeruginosa*, *C. crescentus*, *A. tumefaciens*) demonstrates that vibrio-shaped morphology can be conferred as a portable module independently of core elongation and division machineries (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9, martin2020theevolutionof pages 11-18). This contrasts with earlier assumptions that bacterial shape is strictly determined by cytoskeletal MreB and FtsZ systems.

**Regulatory integration with lifestyle:**  
The 2020 PNAS study by Fernandez et al. established that *V. cholerae* actively modulates curvature via c-di-GMP signaling, coordinating cell shape with biofilm versus planktonic lifestyles (fernandez2020vibriocholeraeadapts pages 1-1). High c-di-GMP concentrations reduce *crvA* expression through VpsR/VpsT transcriptional regulation, producing straight rods during biofilm formation, while low c-di-GMP permits curvature during motile, planktonic states. This adaptive shape-shifting represents a sophisticated environmental response mechanism.

**Antibiotic stress response:**  
The VxrAB-VadR pathway links cell-wall-targeting antibiotic exposure to shape modulation and survival (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43). VadR sRNA, induced by β-lactam antibiotics via the VxrAB two-component system, post-transcriptionally represses *crvA*, modulating curvature and enhancing penicillin G resistance. This pathway synchronizes peptidoglycan integrity, cell shape, and antibiotic defense.

### 5.2 Latest Research (2024)

**Unprecedented outer-membrane morphogenetic control (*R. rubrum*, September 2024):**  
The Pöhl et al. study in *Nature Communications* (DOI:10.1038/s41467-024-51790-z) describes a fundamentally distinct curvature mechanism in *Rhodospirillum rubrum* (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2). The outer-membrane porins Por39 and Por41 form helical assemblies that recruit the lipoprotein PapS, which bridges to the peptidoglycan layer via an OmpA-like domain binding mDAP residues. This porin-PapS complex acts as a "molecular cage" entrapping the RodZ-associated elongasome at the outer cell curve, biasing peptidoglycan synthesis and generating curvature. This work "reveals a mechanistically distinct morphogenetic module" and "an unprecedented role of outer-membrane protein patterning in the spatial control of intracellular processes," reversing the conventional inside-to-outside regulatory hierarchy (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 13-14). The mechanism is structurally encoded in peptidoglycan architecture, as isolated sacculi retain curvature (pohl2024anoutermembrane pages 2-3).

---

## 6. Current Applications and Real-World Implementations

### 6.1 Pathogenesis and Infection

Vibrio-shaped curvature is a virulence determinant in *V. cholerae*. The curved morphology "promotes infectivity and motility in dense hydrogels" (nikolai2020rnamediatedcontrolof pages 1-2). Deletion of *crvA* results in "attenuated colonization in animal infection models" and "reduced virulence" (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 1-2, herzog2020smallregulatoryrnas pages 37-43). This positions CrvA and curvature-regulatory pathways as potential targets for antivirulence therapeutics.

### 6.2 Predatory Ecology

In the predatory bacterium *B. bacteriovorus*, vibrioid curvature enhances prey invasion efficiency. Curved wild-type predators invade prey cells in a median of 4.0 minutes, whereas straight Δ*bd1075* mutants require 6.0 minutes (*p*<0.0001), with 35.6% of Δ*bd1075* invasions lasting ≥7 minutes versus a single 7-minute event in wild-type (banks2022asymmetricpeptidoglycanediting pages 2-4). The curved morphology also prevents mechanical deformation of spherical prey bdelloplasts during intracellular growth, suggesting curvature is an adaptive trait for efficient predation in confined periplasmic environments (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 2-4).

### 6.3 Antibiotic Resistance Mechanisms

The VxrAB-VadR-CrvA axis in *V. cholerae* links cell shape to antibiotic survival. Cells unable to repress *crvA* via VadR "display decreased survival upon challenge with penicillin G," indicating that shape maintenance is critical for β-lactam resistance (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43). This pathway integrates cell-wall stress sensing with morphological adaptation, offering insights into non-enzymatic antibiotic resistance strategies.

### 6.4 Motility in Structured Environments

Curvature enhances swimming speed: curved *V. cholerae* swim 5.5% faster than straight Δ*crvA* mutants (fernandez2020vibriocholeraeadapts pages 5-6). The functional advantage is attributed to increased rotational resistance relative to translational resistance, directing more flagellar power into forward motion (fernandez2020vibriocholeraeadapts pages 5-6). This applies to motility in dense hydrogels and soft agar, relevant to intestinal mucus penetration (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 1-2).

---

## 7. Expert Opinions and Analysis

### 7.1 Mechanistic Diversity

Three distinct mechanisms converge on the vibrio-shaped phenotype:

1. **Periskeletal polymer (CrvAB):** Periplasmic filament localizes to inner curvature; polymerization-driven asymmetric wall expansion (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9).
2. **Asymmetric hydrolase (Bd1075):** Outer-convex-localized LD-carboxypeptidase; differential peptidoglycan cleavage (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11).
3. **Elongasome spatial control (Por39/Por41/PapS):** Outer-membrane complex cages elongation machinery at outer curve; biased synthesis (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 1-2).

This mechanistic plurality highlights convergent evolution: distantly related bacteria achieve similar morphologies via non-homologous molecular systems (banks2022asymmetricpeptidoglycanediting pages 1-2).

### 7.2 Regulatory Logic

In *V. cholerae*, two independent regulatory circuits control curvature:

- **c-di-GMP/VpsR/VpsT pathway:** Coordinates curvature with biofilm/planktonic lifestyle transitions (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 2-3).
- **VxrAB/VadR pathway:** Couples curvature to cell-wall stress and antibiotic survival (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

These pathways integrate environmental cues (quorum sensing, antibiotics) with morphological adaptation, illustrating bacterial cell shape as a dynamically regulated phenotype rather than a static structural property.

### 7.3 Evolutionary Portability

The CrvAB module is "sufficient to induce curvature in heterologous species spanning 2.5 billion years of evolution," including γ-proteobacteria and α-proteobacteria (martin2020theevolutionof pages 1-5). This suggests modular shape determinants can be horizontally transferred or co-opted across taxa, enabling rapid morphological innovation independently of core cytoskeletal remodeling (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9).

---

## 8. Warnings and Curation Notes

### 8.1 Taxon Specificity

**Critical:** All three curvature modules are taxon-specific. CrvAB is native to *Vibrio* and related genera; Bd1075 is *Bdellovibrio*-specific; Por39/Por41/PapS is *Rhodospirillum*-specific. Claims of necessity, sufficiency, and mechanism must be tagged with appropriate NCBITaxon identifiers. Edges should not be generalized across bacterial domains without explicit experimental evidence of conservation.

### 8.2 Assay and Condition Dependencies

- **Antibiotic resistance phenotypes (VadR pathway):** Tested with penicillin G and cell-wall-targeting β-lactams; generalization to other antibiotic classes requires validation (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- **Motility advantages (curved vs. straight):** Measured in soft agar and dense hydrogels; may not extrapolate to liquid culture or low-viscosity environments (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 1-2).
- **Virulence/infectivity:** Assessed in animal infection models (e.g., infant mouse colonization); host-specific and route-dependent (nikolai2020rnamediatedcontrolof pages 1-2, fernandez2020vibriocholeraeadapts pages 1-2, herzog2020smallregulatoryrnas pages 37-43).
- **Prey invasion (Bd1075):** Specific to predatory lifecycle inside Gram-negative prey periplasm (banks2022asymmetricpeptidoglycanediting pages 2-4).

### 8.3 Source Quality Hierarchy

1. **Highest priority:** Peer-reviewed Nature Communications (2020, 2022, 2024), PNAS (2020), Nature Microbiology (2021; preprint 2020 accessible as DOI:10.1101/2020.02.20.954503).
2. **Lower priority:** Dissertation-derived evidence (Herzog 2020, DOI:10.5282/edoc.27302; Peschek 2020, DOI:10.5282/edoc.26477) should be cross-validated with peer-reviewed sources where possible (herzog2020smallregulatoryrnas pages 37-43).

### 8.4 Preprint vs. Final Publication

Martin et al. 2020 bioRxiv preprint (DOI:10.1101/2020.02.20.954503) corresponds to the final peer-reviewed article in *Nature Microbiology* 2021 (DOI:10.1038/s41564-021-00924-w, noted as unobtainable in this search). Curators should cite the final DOI:10.1038/s41564-021-00924-w when available, using preprint evidence where text access is limited (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9, martin2020theevolutionof pages 11-18).

### 8.5 Boundary Between Vibrio-Shaped and Helical

Do **not** curate edges from *Campylobacter jejuni* or *Helicobacter pylori* helical-shape mechanisms (Pgp1/Pgp2, Csd proteins) into METPO:1000686 graphs, as these produce multi-arc helical spirals rather than single-arc vibrio/comma morphology. Maintain distinct trait nodes for helical vs. vibrio-shaped curvature.

### 8.6 Quantitative Metrics

Retain quantitative values in edge notes for reproducibility:

- *V. cholerae*: ΔcrvA curvature 4-fold reduced; straight cells 1.08-fold longer; curved cells swim 5.5% faster (95% CI [5.5%, 5.9%], *P*<1e-5); *crvA* mRNA reduced ~1.5-fold at high c-di-GMP (fernandez2020vibriocholeraeadapts pages 2-3, fernandez2020vibriocholeraeadapts pages 5-6).
- *B. bacteriovorus*: wild-type curvature 0.29–0.64 A.U.; Δ*bd1075* curvature 0.11–0.17 A.U. (*p*<0.0001); wild-type prey invasion 4.0 min median vs. Δ*bd1075* 6.0 min (*p*<0.0001) (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 2-4).
- *R. rubrum*: PapS >15,000 copies/cell; PapS-PG binding K_D = 2.5 mM; Por39-PapS colocalization 90.3%; RodZ/PapS colocalization 57.9% (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 4-5, pohl2024anoutermembrane pages 7-7, pohl2024anoutermembrane pages 10-11).

### 8.7 Ontology Grounding Caution

Do **not** invent protein-specific CURIEs (e.g., fabricated UniProt accessions). If stable cross-species identifiers are unavailable, leave nodes as label-only with species context (e.g., "CrvA (*V. cholerae*)"). Curators may manually link to UniProtKB or NCBI Gene entries post-hoc but should not embed unstable accessions in TraitMech YAML.

---

## 9. DOI-First Bibliography

1. **Peschek et al., 2020** (November 2020). RNA-mediated control of cell shape modulates antibiotic resistance in *Vibrio cholerae*. *Nature Communications* 11. DOI:10.1038/s41467-020-19890-8. URL: https://doi.org/10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 37-43).

2. **Fernandez et al., 2020** (November 2020). *Vibrio cholerae* adapts to sessile and motile lifestyles by cyclic di-GMP regulation of cell shape. *Proceedings of the National Academy of Sciences* 117(46):29046–29054. DOI:10.1073/pnas.2010199117. URL: https://doi.org/10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 2-3, fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 1-2).

3. **Martin et al., 2020 preprint** (February 2020; corresponds to *Nature Microbiology* 2021, DOI:10.1038/s41564-021-00924-w). The evolution of bacterial shape complexity by a curvature-inducing module. *bioRxiv*. DOI:10.1101/2020.02.20.954503. URL: https://doi.org/10.1101/2020.02.20.954503 (martin2020theevolutionof pages 1-5, martin2020theevolutionof pages 5-9, martin2020theevolutionof pages 11-18).

4. **Herzog, 2020** (January 2020). Small regulatory RNAs controlling complex phenotypes in *Vibrio cholerae*. Dissertation, Ludwig-Maximilians-Universität München. DOI:10.5282/edoc.27302. URL: https://doi.org/10.5282/edoc.27302 (herzog2020smallregulatoryrnas pages 37-43).

5. **Banks et al., 2022** (March 2022). Asymmetric peptidoglycan editing generates cell curvature in *Bdellovibrio* predatory bacteria. *Nature Communications* 13. DOI:10.1038/s41467-022-29007-y. URL: https://doi.org/10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 12-12, banks2022asymmetricpeptidoglycanediting pages 2-4).

6. **Pöhl et al., 2024** (September 2024). An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in *Rhodospirillum rubrum*. *Nature Communications* 15. DOI:10.1038/s41467-024-51790-z. URL: https://doi.org/10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 2-3, pohl2024anoutermembrane pages 4-5, pohl2024anoutermembrane pages 7-7, pohl2024anoutermembrane pages 12-13, pohl2024anoutermembrane pages 9-10, pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 10-11).

7. **Bartlett et al., 2017** (Cell 2017, cited as existing evidence; unobtainable in this search). A periplasmic polymer curves *Vibrio cholerae* and promotes pathogenesis. *Cell* 168:172–185.e15. DOI:10.1016/j.cell.2016.12.019. URL: https://doi.org/10.1016/j.cell.2016.12.019.

**Related contextual literature (2023–2025, not directly curated but informative):**

8. **Frirdich et al., 2023** (April 2023). Multiple *Campylobacter jejuni* proteins affecting the peptidoglycan structure and the degree of helical cell curvature. *Frontiers in Microbiology* 14. DOI:10.3389/fmicb.2023.1162806. URL: https://doi.org/10.3389/fmicb.2023.1162806. (Helical morphology; boundary case.)

9. **Alvarez et al., 2024** (September 2024). Control of bacterial cell wall autolysins by peptidoglycan crosslinking mode. *Nature Communications* 15. DOI:10.1038/s41467-024-52325-2. URL: https://doi.org/10.1038/s41467-024-52325-2. (LD-crosslinks and autolysin regulation; contextual for LD-carboxypeptidase activity.)

10. **Escobar-Salom et al., 2023** (March 2023). Bacterial virulence regulation through soluble peptidoglycan fragments sensing and response. *FEMS Microbiology Reviews* 47(2). DOI:10.1093/femsre/fuad010. URL: https://doi.org/10.1093/femsre/fuad010. (Peptidoglycan signaling context.)

---

## 10. Summary and Curation Recommendations

The vibrio-shaped trait (METPO:1000686) is a mechanistically diverse morphological phenotype conferring fitness advantages in motility, pathogenesis, predation, and antibiotic resistance across multiple bacterial taxa. Three non-homologous molecular systems generate vibrio-shaped curvature:

1. **CrvAB periplasmic polymer module** (*V. cholerae*): Regulated by c-di-GMP and antibiotic stress via VpsR/VpsT and VxrAB/VadR pathways.
2. **Bd1075 asymmetric LD-carboxypeptidase** (*B. bacteriovorus*): NTF2 domain-mediated localization to outer convex face.
3. **Por39/Por41/PapS elongasome-trapping complex** (*R. rubrum*): Outer-membrane porin-lipoprotein cages directing asymmetric peptidoglycan synthesis (2024).

**Curation priorities:**

- Focus on well-supported edges with deletion/overexpression/mutation phenotypes and quantitative measurements.
- Tag all edges with taxon identifiers (NCBITaxon:666, NCBITaxon:959, NCBITaxon:1085).
- Annotate assay/condition context (antibiotic challenge, animal models, prey invasion, soft agar).
- Prefer DOI-cited peer-reviewed sources; cross-validate dissertation evidence.
- Use ontology grounding conservatively (GO, CHEBI, EC where stable; label-only for species-specific proteins).
- Maintain boundary distinctions: vibrio-shaped (single arc) ≠ helical (multi-arc).

This report provides 40 curation-ready causal edges (artifact-00), source-backed node definitions, ontology grounding candidates, and comprehensive warnings for TraitMech YAML generation.

References

1. (fernandez2020vibriocholeraeadapts pages 1-1): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

2. (nikolai2020rnamediatedcontrolof pages 1-2): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 46 citations and is from a highest quality peer-reviewed journal.

3. (banks2022asymmetricpeptidoglycanediting pages 1-2): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

4. (pohl2024anoutermembrane pages 2-3): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

5. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

6. (banks2022asymmetricpeptidoglycanediting pages 10-11): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

7. (martin2020theevolutionof pages 1-5): Nicholas R. Martin, Edith Blackman, Benjamin P. Bratton, Thomas M. Bartlett, and Zemer Gitai. The evolution of bacterial shape complexity by a curvature-inducing module. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.20.954503, doi:10.1101/2020.02.20.954503. This article has 4 citations.

8. (martin2020theevolutionof pages 5-9): Nicholas R. Martin, Edith Blackman, Benjamin P. Bratton, Thomas M. Bartlett, and Zemer Gitai. The evolution of bacterial shape complexity by a curvature-inducing module. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.20.954503, doi:10.1101/2020.02.20.954503. This article has 4 citations.

9. (banks2022asymmetricpeptidoglycanediting pages 2-4): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

10. (pohl2024anoutermembrane pages 12-13): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

11. (fernandez2020vibriocholeraeadapts pages 2-3): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

12. (herzog2020smallregulatoryrnas pages 37-43): Roman Herzog. Small regulatory rnas controlling complex phenotypes in vibrio cholerae. Dissertation, Jan 2020. URL: https://doi.org/10.5282/edoc.27302, doi:10.5282/edoc.27302. This article has 0 citations.

13. (martin2020theevolutionof pages 11-18): Nicholas R. Martin, Edith Blackman, Benjamin P. Bratton, Thomas M. Bartlett, and Zemer Gitai. The evolution of bacterial shape complexity by a curvature-inducing module. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.20.954503, doi:10.1101/2020.02.20.954503. This article has 4 citations.

14. (pohl2024anoutermembrane pages 4-5): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

15. (pohl2024anoutermembrane pages 9-10): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

16. (pohl2024anoutermembrane pages 13-14): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (pohl2024anoutermembrane pages 10-11): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

18. (banks2022asymmetricpeptidoglycanediting pages 12-12): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

19. (fernandez2020vibriocholeraeadapts pages 5-6): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

20. (fernandez2020vibriocholeraeadapts pages 1-2): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

21. (pohl2024anoutermembrane pages 7-7): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.