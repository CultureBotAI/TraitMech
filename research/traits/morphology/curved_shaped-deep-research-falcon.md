---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:03:40.747055'
end_time: '2026-08-04T08:17:55.410174'
duration_seconds: 854.66
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: curved shaped
  trait_identifier: METPO:1000670
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: curved_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a bent or curved cell body rather
    than a straight rod or sphere.
  parent_traits: METPO:1000666
  synonyms: S_curved_spiral, curved-shaped
  evidence_summary: 'DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized
    for motility (Supports curved cells as a recognized bacterial morphology with
    possible functional associations.)'
  causal_graph_summary: 'curved_shaped_scaffolded_curvature: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** curved shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000670
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bent or curved cell body rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, curved-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized for motility (Supports curved cells as a recognized bacterial morphology with possible functional associations.)
- **Existing causal graph summary:** curved_shaped_scaffolded_curvature: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **curved shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/curved_shaped.yaml`.

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
- **Trait label:** curved shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000670
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bent or curved cell body rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, curved-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized for motility (Supports curved cells as a recognized bacterial morphology with possible functional associations.)
- **Existing causal graph summary:** curved_shaped_scaffolded_curvature: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **curved shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/curved_shaped.yaml`.

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


# Comprehensive Research Report: Bacterial Curved-Shaped Cell Morphology (METPO:1000670)

---

## 1. Trait Scope and Boundary Cases

The microbial trait **curved shaped** (METPO:1000670) refers to bacterial cells exhibiting a bent or vibrioid morphology—characterized by a single-axis curvature producing a curved rod shape—rather than helical, spiral, straight rod, or spherical forms. The trait is defined as cells displaying a detectable deviation from linearity along the longitudinal axis without forming multiple turns or coils (fernandez2020vibriocholeraeadapts pages 5-6, martin2020theevolutionof pages 5-9, banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 1-2). 

Boundary cases include:
- **Straight rods**: zero curvature cells (e.g., *Caulobacter* Δ*creS* mutants or *Vibrio cholerae* Δ*crvA* mutants) lack the defining feature (fernandez2020vibriocholeraeadapts pages 5-6, cabeen2010mutationsinthe pages 1-2, barrows2023synchronizedswarmersand pages 11-13).
- **Helical and spiral morphologies**: multi-turn helices (*Campylobacter jejuni*, *Helicobacter pylori*) represent distinct morphological classes under different METPO terms; genes such as *pgp1* and *pgp2* of *Campylobacter* produce helical cell shape, whereas deletions yield curved rods or straight rods (frirdich2023multiplecampylobacterjejuni pages 2-3, frirdich2023multiplecampylobacterjejuni pages 1-2). These are boundary evidence that should be marked as belonging to neighboring helical-shape traits, not curated as primary curved-shape evidence unless the measured phenotype is explicitly a curved rod.
- **Coccoid, filamentous, and other transient shape variants** are excluded from this trait.

Current expert consensus (2023 review by Barrows and Goley) identifies crescentin as the bacterial intermediate filament-like protein responsible for *Caulobacter crescentus* curvature, and recognizes curved morphology as a functional adaptation for motility, adhesion, and colonization (barrows2023synchronizedswarmersand pages 11-13).

---

## 2. Candidate Nodes by Type

### Genes and Proteins
- **CreS / crescentin** (*Caulobacter crescentus*): intermediate filament-like cytoskeletal protein, inner-membrane-associated
- **CrvA** (*Vibrio cholerae*): periplasmic polymer forming the curvature module
- **CrvB** (*Vibrio cholerae*): periplasmic protein promoting CrvA higher-order assembly
- **VadR** (*Vibrio cholerae*): small regulatory RNA (sRNA) ~85 nucleotides, Hfq-dependent
- **VxrAB** (*Vibrio cholerae*): two-component system activating VadR transcription
- **wbqL** (*Caulobacter crescentus*): lipopolysaccharide biosynthesis pathway gene
- **Bd1075** (*Bdellovibrio bacteriovorus*): LD-carboxypeptidase with NTF2 localization domain
- Homologous candidates from helical bacteria (**Pgp1, Pgp2, CcmA, Csd proteins** in *Campylobacter* and *Helicobacter*) should be marked as helical-shape evidence unless functional outcomes explicitly include curved rods

### Chemicals and Metabolites
- **Cyclic di-GMP (c-di-GMP)** (CHEBI:58805): second messenger regulating *crvA* expression and cell shape transitions
- **Lipopolysaccharide (LPS)** / **O-polysaccharide**: cell envelope components required for crescentin membrane attachment
- **Peptidoglycan (PG)**: cell wall polymer whose asymmetric synthesis or editing produces curvature
- **Penicillin G** and other cell-wall-targeting antibiotics: environmental stressors inducing VadR via VxrAB

### Processes and Functions
- **Asymmetric peptidoglycan insertion** (GO:0071555 may partially apply): spatially biased cell wall synthesis
- **LD-carboxypeptidase activity** (GO:0008747 or similar peptidase GO terms): asymmetric editing of PG crosslinks
- **Inner membrane localization** (GO:0005886)
- **Periplasmic localization** (GO:0030288)
- **Outer convex face localization**: specialized asymmetric subcellular targeting (no fixed GO CURIE; label-only node for now)
- **Post-transcriptional regulation by sRNA**: VadR → *crvA* mRNA interaction

### Environmental and Experimental Factors
- **Cell-wall antibiotics / envelope stress**: induces VadR expression via VxrAB
- **Cell density / quorum sensing**: *V. cholerae* high cell density increases *crvA* expression and curvature
- **Biofilm vs. planktonic lifestyle**: sessile biofilms correlate with low curvature and high VadR expression; motile planktonic lifestyle favors curved cells
- **Nutrient availability**: low-nutrient aquatic conditions correlate with curved *Caulobacter*
- **Flow / shear stress**: surface colonization under flow conditions in *Caulobacter* is enhanced by curvature

### Phenotypic Consequences
- **Enhanced swimming speed**: curved *V. cholerae* swim ~5.5% faster than straight rods
- **Increased rotational resistance during swimming**: proposed mechanism for motility advantage
- **Improved predatory invasion**: curved *Bdellovibrio* invade prey faster (4.0 min vs. 6.0 min median)
- **Enhanced surface colonization**: *Caulobacter* curvature facilitates attachment under flow conditions
- **Decreased antibiotic survival**: *V. cholerae* vadR mutants show reduced penicillin G survival
- **Altered biofilm formation**: VadR-mediated repression of *vps*, *rbm*, and *bap* genes

---

## 3. Evidence-Backed Causal Edges

| taxon/context | subject | predicate | object | evidence/perturbation | confidence |
|---|---|---|---|---|---|
| *Caulobacter crescentus* | CreS (crescentin) | causes asymmetric rate of | peptidoglycan insertion across cell sidewalls | creS-dependent inner-curve filament; deletion or membrane-dissociation abolishes asymmetric growth pattern and cells become straighter (sundararajan2017cytoskeletalproteinsin pages 16-17) | high |
| *Caulobacter crescentus* | asymmetric peptidoglycan insertion | causes | curved cell shape | expert synthesis and primary perturbation evidence indicate slower wall insertion proximal to crescentin and greater distal insertion yields curvature (sundararajan2017cytoskeletalproteinsin pages 16-17, barrows2023synchronizedswarmersand pages 11-13) | high |
| *Caulobacter crescentus* | wbqL | required for | proper lipopolysaccharide/O-polysaccharide state permitting crescentin envelope association | wbqL deletion in LPS biosynthesis disrupts crescentin-mediated curvature without abolishing crescentin assembly (cabeen2010mutationsinthe pages 1-2, sundararajan2017cytoskeletalproteinsin pages 16-17) | high |
| *Caulobacter crescentus* | altered lipopolysaccharide/O-polysaccharide | disrupts | crescentin attachment to cell envelope | envelope-association defect observed in wbqL mutants; attachment-defective crescentin cannot support curvature (cabeen2010mutationsinthe pages 1-2, sundararajan2017cytoskeletalproteinsin pages 16-17) | high |
| *Caulobacter crescentus* | crescentin envelope attachment | enables | curved cell shape | membrane-associated crescentin supports curvature, whereas attachment-defective or membrane-dissociated crescentin does not (sundararajan2017cytoskeletalproteinsin pages 16-17, cabeen2010mutationsinthe pages 1-2) | high |
| *Vibrio cholerae* | CrvA + CrvB | forms | asymmetrically localized inner-curvature periplasmic curvature module | CrvAB colocalize as periplasmic/periskeletal module; sufficient to induce curvature in heterologous Gram-negative hosts (martin2020theevolutionof pages 5-9) | high |
| *Vibrio cholerae* | CrvA | promotes | curved/vibrioid cell shape | crvA loss straightens cells; CrvA is the direct shape determinant in perturbation studies (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 5-6, nikolai2020rnamediatedcontrolof pages 1-2) | high |
| *Vibrio cholerae* | cyclic-di-GMP signaling | represses expression of | crvA | elevated c-di-GMP during sessile program decreases crvA expression and straightens cells (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 5-6, lin2021peptidoglycanbindingby pages 38-42) | high |
| *Vibrio cholerae* | VxrAB two-component system | activates transcription of | VadR sRNA | vadR promoter activity depends on VxrAB and is induced by cell-wall stress (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 46-48, nikolai2020rnamediatedcontrolof pages 6-7) | high |
| *Vibrio cholerae* | cell-wall-targeting antibiotics | induce | VadR sRNA | penicillin G and related envelope stress conditions increase VadR levels (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 46-48, nikolai2020rnamediatedcontrolof pages 6-7) | high |
| *Vibrio cholerae* | VadR sRNA | represses | crvA mRNA | direct post-transcriptional inhibition supported by compensatory base-pairing evidence; vadR mutation increases curvature and overexpression decreases it (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 46-48, nikolai2020rnamediatedcontrolof pages 6-7) | high |
| *Vibrio cholerae* | repression of crvA | decreases | curved/vibrioid cell shape | straighter morphology follows VadR overexpression or high c-di-GMP states (fernandez2020vibriocholeraeadapts pages 1-1, nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 46-48) | high |
| *Bdellovibrio bacteriovorus* | Bd1075 | has molecular function | LD-carboxypeptidase activity on peptidoglycan | catalytic mutant fails to restore curvature; biochemical and muropeptide evidence support tetrapeptide-to-tripeptide editing (banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 11-12) | high |
| *Bdellovibrio bacteriovorus* | Bd1075 NTF2 domain | mediates localization to | outer convex cell face | NTF2-domain mutants/truncations mislocalize and fail to restore curvature (banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 11-12, banks2022asymmetricpeptidoglycanediting pages 7-10) | high |
| *Bdellovibrio bacteriovorus* | convex-face-localized Bd1075 activity | causes | localized peptidoglycan editing | asymmetric localization plus catalytic requirement link localized LD-carboxypeptidase activity to side-specific wall remodeling (banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 7-10) | high |
| *Bdellovibrio bacteriovorus* | localized peptidoglycan editing by Bd1075 | causes | curved/vibrioid cell shape | bd1075 deletion produces rod-shaped cells and complementation restores curvature (banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 1-2) | high |


*Table: This table lists the strongest, directly supported causal triples for curating the curved-shaped trait across representative bacterial systems. It emphasizes experimentally perturbed shape determinants, regulatory inputs, and side-specific cell wall remodeling mechanisms while keeping identifiers conservative.*

### Detailed Supporting Evidence and References

#### *Caulobacter crescentus* CreS/Crescentin Pathway
**Edge 1: CreS → asymmetric peptidoglycan insertion → curved shape**

- **Reference**: Sundararajan and Goley, 2017. DOI: 10.1007/978-3-319-53047-5_4
- **Snippet**: "crescentin mediates curvature through mechanical regulation of peptidoglycan synthesis, creating a synthesis gradient across the cell axis (slower proximal to crescentin, faster distally)" (sundararajan2017cytoskeletalproteinsin pages 16-17).
- **Quantitative data**: Crescentin filament pitch measures 1.6 ± 0.1 µm (membrane-attached) versus 1.4 ± 0.15 µm (dissociated) (sundararajan2017cytoskeletalproteinsin pages 16-17).
- **Notes**: Deletion or membrane-dissociation of crescentin produces straight cells. Both filament assembly and membrane attachment are required; non-polymerizing or envelope-dissociated crescentin variants fail to generate curvature. Mechanism is conserved localized compression of the cell wall.

**Edge 2: wbqL/LPS biosynthesis → crescentin envelope association → curvature**

- **Reference**: Cabeen et al., 2010. DOI: 10.1128/jb.01371-09
- **Snippet**: "Deletion of wbqL abolished cell curvature through accumulation of aberrant O-polysaccharide, which interfered with crescentin's cell envelope association" (cabeen2010mutationsinthe pages 1-2).
- **Notes**: wbqL mutation in the LPS biosynthesis pathway disrupts crescentin membrane attachment without affecting crescentin intrinsic assembly or stability. Attachment-defective crescentin mutants cannot support curvature. This edge highlights a taxon-specific dependency on envelope structure.

**Recent Expert Perspective (2023)**

- **Reference**: Barrows and Goley, 2023. DOI: 10.1128/jb.00384-22
- **Snippet**: "Crescentin (encoded by creS) is the first intermediate filament-like protein described in bacteria and is responsible for Caulobacter curvature. It assembles into curved filaments along the inner membrane curvature and mechanically regulates cell wall insertion" (barrows2023synchronizedswarmersand pages 11-13).
- **Notes**: This recent review establishes crescentin as the canonical model for cytoskeletal shape determinants and notes that curvature increases bacterial motility and swimming efficiency through low flagellar motor torque, helical body movement, and improved surface adhesion under flow.

---

#### *Vibrio cholerae* CrvA/CrvB and Regulatory Circuitry

**Edge 3: CrvA + CrvB → inner-curvature periplasmic module → curved shape**

- **Reference**: Martin et al., 2020. DOI: 10.1101/2020.02.20.954503
- **Snippet**: "CrvA and CrvB proteins form dynamic periskeletal filaments localized to the inner curvature of cells and colocalize in the periplasm. The module functions as an asymmetric structure independent of species-specific shape machinery (MreB/FtsZ)" (martin2020theevolutionof pages 5-9).
- **Notes**: CrvAB is sufficient to curve heterologous species separated by 2.5 billion years of evolution. CrvB promotes CrvA higher-order assembly in a dose-dependent manner. Functional consequence includes enhanced intestinal colonization.

**Edge 4: c-di-GMP signaling → repression of *crvA* → straighter cells**

- **Reference**: Fernandez et al., 2020. DOI: 10.1073/pnas.2010199117
- **Snippet**: "c-di-GMP signaling post-transcriptionally represses crvA expression. Low cell density populations have higher c-di-GMP concentrations than high cell density populations" (fernandez2020vibriocholeraeadapts pages 1-1).
- **Quantitative data**: ΔcrvA mutant showed a 4-fold difference in curvature. Curved cells swim 5.5% faster than straight rods (95% CI [5.5%, 5.9%], P<1e-5) (fernandez2020vibriocholeraeadapts pages 5-6).
- **Notes**: c-di-GMP regulation mediates lifestyle transitions; elevated c-di-GMP during biofilm formation decreases *crvA* expression and straightens cells.

**Edge 5: Cell-wall antibiotics → VxrAB → VadR sRNA → repression of *crvA* → straighter cells**

- **Reference**: Peschek et al., 2020. DOI: 10.1038/s41467-020-19890-8
- **Snippet**: "VadR expression is activated by the VxrAB two-component system and triggered by cell-wall-targeting antibiotics. Cells unable to repress crvA through VadR show decreased survival when challenged with penicillin G" (nikolai2020rnamediatedcontrolof pages 1-2).
- **Quantitative data**: Penicillin G induces ~7-fold increase in VadR levels and ~25-fold promoter induction. VadR protein increases ~1.5-fold in *vadR* deletions and decreases ~2-fold with VadR overexpression (herzog2020smallregulatoryrnas pages 46-48, nikolai2020rnamediatedcontrolof pages 6-7).
- **Notes**: VadR directly represses *crvA* mRNA via complementary base-pairing confirmed by compensatory mutation analysis. VadR also blocks biofilm genes (*vps*, *rbmA*, *rbmC*, *bap1*). VadR expression peaks during early biofilm formation and is switched off in mature biofilms, showing negative correlation between VadR expression and cell curvature during biofilm development.

---

#### *Bdellovibrio bacteriovorus* Bd1075 Pathway

**Edge 6: Bd1075 (LD-carboxypeptidase) → localized PG editing at outer convex face → curved shape**

- **Reference**: Banks et al., 2022. DOI: 10.1038/s41467-022-29007-y
- **Snippet**: "Bd1075 generates vibrioid cell curvature through LD-carboxypeptidase activity on the predator cell wall. The protein localizes asymmetrically to the outer convex face of B. bacteriovorus, with an NTF2-like domain at the C-terminus required for this localization" (banks2022asymmetricpeptidoglycanediting pages 1-2).
- **Quantitative data**:
  - Wild-type curvature: 0.64 A.U. (95% CI [0.63, 0.66])
  - Δbd1075 mutant: 0.11 A.U. (95% CI [0.10, 0.12], p < 0.0001)
  - Alternative measurement: WT 0.29 A.U. vs Δbd1075 0.17 A.U. (p < 0.0001)
  - Prey invasion time: WT median 4.0 min (95% CI [4.0, 5.0]) vs Δbd1075 median 6.0 min (95% CI [5.0, 6.0]); 35.6% of Δbd1075 invasions ≥7 min vs max 7 min for WT (banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 1-2).
  - Peptidoglycan crosslinkage: 64.4% in Δbd1075 vs 61.1% in WT (banks2022asymmetricpeptidoglycanediting pages 11-12).
- **Notes**: Bd1075 crystal structure resolved at 1.34 Å resolution, containing catalytic LD-CPase domain (aa 47–180) and NTF2 domain (aa 196–304). NTF2 domain mutants (Y274A, E302, W303) fail proper outer-convex localization and cannot restore curvature. Catalytic mutant C156A does not restore curvature. Rod-shaped Δbd1075 mutants are slower to invade prey and stretch invaded prey from within, consistent with reduced predatory fitness (banks2022asymmetricpeptidoglycanediting pages 10-11, banks2022asymmetricpeptidoglycanediting pages 7-10).

---

#### Boundary Evidence: Helical Shape Systems

**Edge 7 (boundary warning): *Campylobacter jejuni* Pgp1/Pgp2 → helical shape (not simple curved rod)**

- **Reference**: Frirdich et al., 2023. DOI: 10.3389/fmicb.2023.1162806
- **Snippet**: "Pgp1 and Pgp2 deletion mutants are rod-shaped with altered muropeptide profiles, while Pgp1/Pgp2 wild-type maintains helical morphology. Deletions of genes 0166, 1105, and 1228 produced varying curved rod morphologies" (frirdich2023multiplecampylobacterjejuni pages 2-3, frirdich2023multiplecampylobacterjejuni pages 1-2).
- **Notes**: *Campylobacter* and *Helicobacter* systems produce helical/spiral morphology (multi-turn coils), not simple vibrioid curvature. Homologous systems (e.g., CcmA bactofilin, Csd proteins) should be annotated as helical-shape mechanisms unless the functional outcome is specifically a curved rod. The 2023 Frirdich paper emphasizes that related organisms with homologous proteins can have diverse outcomes, highlighting the importance of taxon-specific validation.

---

## 4. Ontology Grounding (Conservative CURIEs)

**Chemical entities:**
- Cyclic-di-GMP: **CHEBI:58805**
- Peptidoglycan: **CHEBI:8005**
- Lipopolysaccharide: **CHEBI:16412**
- Penicillin G: **CHEBI:18208**

**Gene products:**
- CreS/crescentin (*Caulobacter*): label-only (species-specific gene product; no stable cross-species CURIE)
- CrvA (*Vibrio*): label-only
- CrvB (*Vibrio*): label-only
- VadR: label-only (sRNA, limited ontology coverage)
- VxrAB: label-only (two-component system)
- Bd1075: label-only

**Molecular functions:**
- LD-carboxypeptidase activity: **GO:0008747** (carboxypeptidase activity) or more specific EC/GO terms if available
- Cell wall organization or biogenesis: **GO:0071555**
- Peptidoglycan biosynthetic process: **GO:0009252**

**Cellular compartments:**
- Inner membrane: **GO:0005886**
- Periplasm: **GO:0030288**

**Biological processes:**
- Determination of bacterial cell shape: **GO:0051261**
- Peptidoglycan-based cell wall organization: **GO:0009274**

**Trait:**
- Curved shaped: **METPO:1000670** (as provided)

**Taxonomy:**
- *Caulobacter crescentus*: **NCBITaxon:155892**
- *Vibrio cholerae*: **NCBITaxon:666**
- *Bdellovibrio bacteriovorus*: **NCBITaxon:959**
- *Campylobacter jejuni*: **NCBITaxon:197**
- *Helicobacter pylori*: **NCBITaxon:210**

**Note:** Do not invent CURIEs for organism-specific proteins without stable database entries. Label-only nodes are acceptable and preferred when stable identifiers are unavailable.

---

## 5. Current Applications and Functional Consequences

### Motility and Swimming Efficiency
Curved cell shape provides a direct swimming advantage in *Vibrio cholerae*: curved cells swim 5.5% faster than straight mutants (95% CI [5.5%, 5.9%], P < 1e-5) in minimal medium at early stationary phase, with increased rotational resistance improving propulsion efficiency (fernandez2020vibriocholeraeadapts pages 5-6). *Caulobacter* curvature is associated with increased swimming efficiency through low flagellar motor torque and helical body movement in low-nutrient aquatic environments (barrows2023synchronizedswarmersand pages 11-13).

### Predatory Fitness
Curved *Bdellovibrio bacteriovorus* predators invade prey significantly faster than straight-rod Δbd1075 mutants: wild-type median invasion time is 4.0 min versus 6.0 min for mutants (95% CI [5.0, 6.0]), with 35.6% of mutant invasions requiring ≥7 min versus a maximum of 7 min for wild-type. Curved morphology is proposed to distribute mechanical forces as glancing blows rather than head-on impacts, facilitating efficient periplasmic entry (banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 1-2).

### Surface Colonization and Biofilm Formation
*Caulobacter* curvature enhances surface colonization under flow conditions by positioning the new pole to facilitate transient pilus-mediated and irreversible holdfast-mediated attachment (woldemeskel2017shapeshiftingtosurvive pages 6-8). In *Vibrio cholerae*, VadR-mediated curvature regulation coordinates cell shape transitions with biofilm development: VadR expression peaks during early biofilm formation (straight cells), is switched off in mature biofilms (curved cells), and directly represses biofilm matrix genes *vps*, *rbm*, and *bap* (herzog2020smallregulatoryrnas pages 46-48, nikolai2020rnamediatedcontrolof pages 7-7).

### Antibiotic Resistance and Envelope Stress
*Vibrio cholerae* VadR-mediated *crvA* repression is critical for antibiotic resistance. Cells unable to repress *crvA* through VadR show decreased survival when challenged with penicillin G, establishing that cell shape maintenance is functionally linked to envelope homeostasis. Cell-wall-targeting antibiotics induce VadR via the VxrAB two-component system (~7-fold VadR increase, ~25-fold promoter induction), synchronizing peptidoglycan synthesis, shape, and stress response (nikolai2020rnamediatedcontrolof pages 1-2, herzog2020smallregulatoryrnas pages 46-48, nikolai2020rnamediatedcontrolof pages 6-7).

---

## 6. Expert Analysis and Recent Developments

The 2023 Barrows and Goley review highlights *Caulobacter crescentus* as a premier model for bacterial cell shape and identifies crescentin as the first described bacterial intermediate filament-like protein. Crescentin's membrane-associated filament structure mechanically regulates asymmetric peptidoglycan synthesis, establishing curvature as a stable, inherited trait linked to ecological fitness (barrows2023synchronizedswarmersand pages 11-13).

Martin et al. (2020) demonstrated that the CrvAB module can induce curvature autonomously across evolutionarily distant Gram-negative species, suggesting a modular and evolvable architecture for cell shape complexity (martin2020theevolutionof pages 5-9). The 2020 Fernandez study revealed dynamic c-di-GMP-mediated cell shape transitions that allow *Vibrio* to switch between motile curved and sessile straight morphologies, highlighting active regulation of curvature rather than passive determination (fernandez2020vibriocholeraeadapts pages 1-1, fernandez2020vibriocholeraeadapts pages 5-6).

The 2022 Banks study identified the first LD-carboxypeptidase-based curvature mechanism in *Bdellovibrio*, showing that localized peptidoglycan editing (rather than cytoskeletal or periskeletal scaffolds) can generate curvature through enzymatic asymmetry (banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 1-2).

The 2023 Frirdich study on *Campylobacter* emphasizes that even closely related organisms with similar morphologies employ diverse peptidoglycan biosynthetic pathways, cautioning against cross-taxon extrapolation of mechanisms (frirdich2023multiplecampylobacterjejuni pages 2-3, frirdich2023multiplecampylobacterjejuni pages 1-2).

---

## 7. Quantitative Summary of Key Statistics

| Measurement | Value | Species | Context | Reference |
|---|---|---|---|---|
| Swimming speed advantage | +5.5% (95% CI [5.5%, 5.9%]) | *V. cholerae* | Curved vs. straight rods, minimal medium, early stationary phase | pqac-00000001, pqac-00000020 |
| Prey invasion time (WT) | 4.0 min (median, 95% CI [4.0, 5.0]) | *B. bacteriovorus* | Attack-phase curved predators | pqac-00000012 |
| Prey invasion time (Δbd1075) | 6.0 min (median, 95% CI [5.0, 6.0]) | *B. bacteriovorus* | Rod-shaped mutants | pqac-00000012 |
| Cell curvature (WT) | 0.64 A.U. (95% CI [0.63, 0.66]) | *B. bacteriovorus* | Wild-type HD100 | pqac-00000014 |
| Cell curvature (Δbd1075) | 0.11 A.U. (95% CI [0.10, 0.12]) | *B. bacteriovorus* | Deletion mutant | pqac-00000014 |
| VadR induction by penicillin G | ~7-fold (Northern blot) | *V. cholerae* | Envelope stress response | pqac-00000006, pqac-00000008 |
| VadR promoter induction | ~25-fold | *V. cholerae* | Cell-wall antibiotics via VxrAB | pqac-00000006 |
| CrvA protein change (Δ*vadR*) | ~1.5-fold increase | *V. cholerae* | Regulatory derepression | pqac-00000006 |
| Crescentin filament pitch (attached) | 1.6 ± 0.1 µm | *C. crescentus* | Membrane-associated form | pqac-00000003 |
| Crescentin filament pitch (free) | 1.4 ± 0.15 µm | *C. crescentus* | Membrane-dissociated form | pqac-00000003 |
| PG crosslinkage (WT) | 61.1% | *B. bacteriovorus* | Wild-type attack-phase cells | pqac-00000013 |
| PG crosslinkage (Δbd1075) | 64.4% | *B. bacteriovorus* | Rod-shaped mutant | pqac-00000013 |

---

## 8. Curation Warnings and Limitations

1. **Do not extrapolate helical-shape mechanisms to curved-shape without explicit phenotypic validation.** *Campylobacter* Pgp1, Pgp2, and *Helicobacter* CcmA/Csd systems produce helical/spiral shapes and should be curated under distinct METPO terms unless experimental evidence demonstrates a curved-rod phenotype (frirdich2023multiplecampylobacterjejuni pages 2-3, frirdich2023multiplecampylobacterjejuni pages 1-2).

2. **Taxon-specific mechanisms predominate.** Crescentin, CrvAB, and Bd1075 represent phylogenetically restricted, independent solutions to curvature. Cross-species generalization should be avoided; each mechanism requires validation in its native context.

3. **Regulatory pathways are context-dependent.** The c-di-GMP/VadR/VxrAB regulatory circuitry is *Vibrio*-specific and may not generalize to other curved bacteria. Crescentin-mediated curvature in *Caulobacter* lacks known regulatory inputs analogous to VadR.

4. **Functional consequences vary by ecological niche.** Motility advantages (+5.5% swimming speed in *Vibrio*), predatory efficiency (faster invasion in *Bdellovibrio*), and surface colonization (*Caulobacter*) are measured in specific experimental contexts and should not be assumed universal.

5. **Quantitative curvature metrics are assay-dependent.** Arbitrary curvature units (A.U.) from image analysis are not directly comparable across studies without standardized calibration.

6. **Weak or uncertain edges:**
   - The precise molecular linkage between LPS/O-polysaccharide structure and crescentin membrane attachment in *Caulobacter* remains incompletely characterized at atomic resolution.
   - The downstream mechanisms by which c-di-GMP signaling represses *crvA* expression (direct binding vs. transcription factor mediation) are not fully resolved.
   - The structural details of CrvA–CrvB interactions and their force transmission to the peptidoglycan layer require further study.

7. **Do not curate claims unsupported by direct perturbation or localization evidence.** Only include edges where deletion, overexpression, localization, or complementation experiments establish causality.

---

## 9. DOI-First Bibliography

- **Barrows, J. M., & Goley, E. D. (2023).** Synchronized swarmers and sticky stalks: *Caulobacter crescentus* as a model for bacterial cell biology. *Journal of Bacteriology*, 205(2). DOI: [10.1128/jb.00384-22](https://doi.org/10.1128/jb.00384-22) (February 2023)

- **Banks, E. J., Valdivia-Delgado, M., Biboy, J., Wilson, A., Cadby, I. T., Vollmer, W., Lambert, C., Lovering, A. L., & Sockett, R. E. (2022).** Asymmetric peptidoglycan editing generates cell curvature in *Bdellovibrio* predatory bacteria. *Nature Communications*, 13, 1–14. DOI: [10.1038/s41467-022-29007-y](https://doi.org/10.1038/s41467-022-29007-y) (March 2022)

- **Cabeen, M. T., Murolo, M. A., Briegel, A., Bui, N. K., Vollmer, W., Ausmees, N., Jensen, G. J., & Jacobs-Wagner, C. (2010).** Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in *Caulobacter crescentus*. *Journal of Bacteriology*, 192(13), 3368–3378. DOI: [10.1128/jb.01371-09](https://doi.org/10.1128/jb.01371-09) (July 2010)

- **Fernandez, N. L., Hsueh, B. Y., Nhu, N. T. Q., Franklin, J. L., Dufour, Y. S., & Waters, C. M. (2020).** *Vibrio cholerae* adapts to sessile and motile lifestyles by cyclic di-GMP regulation of cell shape. *Proceedings of the National Academy of Sciences*, 117(46), 29046–29054. DOI: [10.1073/pnas.2010199117](https://doi.org/10.1073/pnas.2010199117) (November 2020)

- **Frirdich, E., Vermeulen, J., Biboy, J., Vollmer, W., & Gaynor, E. C. (2023).** Multiple *Campylobacter jejuni* proteins affecting the peptidoglycan structure and the degree of helical cell curvature. *Frontiers in Microbiology*, 14. DOI: [10.3389/fmicb.2023.1162806](https://doi.org/10.3389/fmicb.2023.1162806) (April 2023)

- **Herzog, R. (2020).** Small regulatory RNAs controlling complex phenotypes in *Vibrio cholerae*. Dissertation, Ludwig-Maximilians-Universität München. DOI: [10.5282/edoc.27302](https://doi.org/10.5282/edoc.27302) (January 2020)

- **Martin, N. R., Blackman, E., Bratton, B. P., Bartlett, T. M., & Gitai, Z. (2020).** The evolution of bacterial shape complexity by a curvature-inducing module. *bioRxiv*. DOI: [10.1101/2020.02.20.954503](https://doi.org/10.1101/2020.02.20.954503) (February 2020)

- **Peschek, N. (2020).** Functional characterization of bacterial sRNAs involved in stress responses and quorum sensing of bacterial pathogens. Dissertation, Ludwig-Maximilians-Universität München. DOI: [10.5282/edoc.26477](https://doi.org/10.5282/edoc.26477) (January 2020)

- **Peschek, N., Herzog, R., Singh, P. K., Sprenger, M., Meyer, F., Fröhlich, K. S., Schröger, L., Bramkamp, M., Drescher, K., & Papenfort, K. (2020).** RNA-mediated control of cell shape modulates antibiotic resistance in *Vibrio cholerae*. *Nature Communications*, 11, 1–14. DOI: [10.1038/s41467-020-19890-8](https://doi.org/10.1038/s41467-020-19890-8) (November 2020)

- **Sundararajan, K., & Goley, E. D. (2017).** Cytoskeletal proteins in *Caulobacter crescentus*: Spatial orchestrators of cell cycle progression, development, and cell shape. *Sub-cellular Biochemistry*, 84, 103–137. DOI: [10.1007/978-3-319-53047-5_4](https://doi.org/10.1007/978-3-319-53047-5_4) (January 2017)

- **Woldemeskel, S. A., & Goley, E. D. (2017).** Shapeshifting to survive: Shape determination and regulation in *Caulobacter crescentus*. *Trends in Microbiology*, 25(8), 673–687. DOI: [10.1016/j.tim.2017.03.006](https://doi.org/10.1016/j.tim.2017.03.006) (August 2017)

---

## 10. Summary for Curation

The trait **METPO:1000670 curved shaped** is a well-characterized bacterial morphology with three documented independent molecular mechanisms:

1. **Crescentin-mediated asymmetric peptidoglycan insertion** (*Caulobacter crescentus*): cytoskeletal filament anchored at the inner membrane compresses the cell wall, slowing proximal PG synthesis and accelerating distal synthesis.
2. **CrvAB periplasmic polymer** (*Vibrio cholerae*): dynamically regulated by c-di-GMP signaling, quorum sensing, and VadR sRNA in response to cell density, biofilm state, and envelope stress.
3. **Bd1075 localized LD-carboxypeptidase** (*Bdellovibrio bacteriovorus*): NTF2-domain-mediated targeting to the outer convex face drives asymmetric peptidoglycan crosslink editing.

Functional advantages include enhanced motility (+5.5% swimming speed in *Vibrio*), faster predatory invasion (4.0 vs. 6.0 min in *Bdellovibrio*), and improved surface colonization under flow (*Caulobacter*). Regulatory integration with antibiotic resistance and biofilm development is established in *Vibrio*.

Evidence is strongest for direct perturbations (deletions, complementations, localization studies) in species-specific contexts. Cross-taxon extrapolation, conflation with helical/spiral morphologies, and generalization of functional consequences without experimental validation should be avoided during curation.

References

1. (fernandez2020vibriocholeraeadapts pages 5-6): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

2. (martin2020theevolutionof pages 5-9): Nicholas R. Martin, Edith Blackman, Benjamin P. Bratton, Thomas M. Bartlett, and Zemer Gitai. The evolution of bacterial shape complexity by a curvature-inducing module. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.20.954503, doi:10.1101/2020.02.20.954503. This article has 4 citations.

3. (banks2022asymmetricpeptidoglycanediting pages 2-4): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

4. (banks2022asymmetricpeptidoglycanediting pages 1-2): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

5. (cabeen2010mutationsinthe pages 1-2): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

6. (barrows2023synchronizedswarmersand pages 11-13): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 61 citations and is from a peer-reviewed journal.

7. (frirdich2023multiplecampylobacterjejuni pages 2-3): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 11 citations and is from a peer-reviewed journal.

8. (frirdich2023multiplecampylobacterjejuni pages 1-2): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 11 citations and is from a peer-reviewed journal.

9. (sundararajan2017cytoskeletalproteinsin pages 16-17): Kousik Sundararajan and Erin D. Goley. Cytoskeletal proteins in caulobacter crescentus: spatial orchestrators of cell cycle progression, development, and cell shape. Sub-cellular biochemistry, 84:103-137, Jan 2017. URL: https://doi.org/10.1007/978-3-319-53047-5\_4, doi:10.1007/978-3-319-53047-5\_4. This article has 25 citations.

10. (fernandez2020vibriocholeraeadapts pages 1-1): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

11. (nikolai2020rnamediatedcontrolof pages 1-2): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 46 citations and is from a highest quality peer-reviewed journal.

12. (lin2021peptidoglycanbindingby pages 38-42): Chang Sheng-Huei Lin. Peptidoglycan binding by pgp2 and ape1 determines campylobacter jejuni helical cell shape. ArXiv, Jan 2021. URL: https://doi.org/10.14288/1.0401780, doi:10.14288/1.0401780. This article has 0 citations.

13. (herzog2020smallregulatoryrnas pages 46-48): Roman Herzog. Small regulatory rnas controlling complex phenotypes in vibrio cholerae. Dissertation, Jan 2020. URL: https://doi.org/10.5282/edoc.27302, doi:10.5282/edoc.27302. This article has 0 citations.

14. (nikolai2020rnamediatedcontrolof pages 6-7): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 46 citations and is from a highest quality peer-reviewed journal.

15. (banks2022asymmetricpeptidoglycanediting pages 10-11): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

16. (banks2022asymmetricpeptidoglycanediting pages 11-12): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

17. (banks2022asymmetricpeptidoglycanediting pages 7-10): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

18. (woldemeskel2017shapeshiftingtosurvive pages 6-8): Selamawit Abi Woldemeskel and Erin D. Goley. Shapeshifting to survive: shape determination and regulation in caulobacter crescentus. Trends in microbiology, 25 8:673-687, Aug 2017. URL: https://doi.org/10.1016/j.tim.2017.03.006, doi:10.1016/j.tim.2017.03.006. This article has 59 citations and is from a domain leading peer-reviewed journal.

19. (nikolai2020rnamediatedcontrolof pages 7-7): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 46 citations and is from a highest quality peer-reviewed journal.