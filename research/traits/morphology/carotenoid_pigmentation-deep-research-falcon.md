---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:37:40.770185'
end_time: '2026-06-18T06:51:48.809693'
duration_seconds: 848.04
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: carotenoid pigmentation
  trait_identifier: METPO:1003031
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: carotenoid_pigmentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype caused by microbial production and accumulation
    of carotenoid pigments.
  parent_traits: METPO:1003021
  synonyms: Pigment_carotenoid
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid
    pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)'
  causal_graph_summary: 'carotenoid_pigmentation_crt_pathway: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carotenoid pigmentation
- **METPO identifier:** METPO:1003031
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype caused by microbial production and accumulation of carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_carotenoid
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)
- **Existing causal graph summary:** carotenoid_pigmentation_crt_pathway: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **carotenoid pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carotenoid_pigmentation.yaml`.

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
- **Trait label:** carotenoid pigmentation
- **METPO identifier:** METPO:1003031
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype caused by microbial production and accumulation of carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_carotenoid
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: Carotenoids are isoprenoid pigments (Supports carotenoid pigmentation as a bacterial isoprenoid-pigment phenotype.)
- **Existing causal graph summary:** carotenoid_pigmentation_crt_pathway: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **carotenoid pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/carotenoid_pigmentation.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Carotenoid Pigmentation (METPO:1003031)

### 1) Scope summary (trait meaning, assay readouts, boundary cases)

**Trait definition (curation-ready):** *Carotenoid pigmentation* is an observable microbial coloration phenotype (typically yellow/orange/red) caused by **microbial production and accumulation of carotenoid pigments** (carotenes and xanthophylls). In curated graphs, this trait should be represented as a **morphological phenotype** that can be assayed by **colony color** and/or **pigment extraction and quantification** (e.g., UV–Vis absorbance spectra, chromatography/HPLC/UPLC, LC–MS). For example, staphyloxanthin in *Staphylococcus aureus* “serves not only to impart color” and is a carotenoid pigment (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2), and carotenoids broadly “impart hues of yellow, orange, and red” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2).

**Operational phenotype readouts used in recent studies (2023–2024):**
- **Colony color shifts** as a proxy for carotenoid accumulation (e.g., *Corynebacterium glutamicum* colonies shifting “from light yellow to pink” upon engineering that increases lycopene) (zhan2024expandingthecrispr pages 10-12).
- **Spectral/chemical measurements** of extracted pigments (UV–Vis peaks/shift; chromatography). In a staphyloxanthin study, enhanced pigmentation was associated with wavelength shifts “ranging from 450 nm … to 470 nm … /480 nm” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2).

**Boundary cases and nearby traits (should be distinguished):**
1. **Rhodopsin chromophore/retinal-related crt clusters:** In some marine bacteria, a proteorhodopsin (PR) locus has an adjacent “rhodopsin chromophore biosynthesis cluster (crtE-crtI-crtB-crtY)” (lee2024effectsoflight pages 10-11). These genes may contribute to retinal/chromophore production and may not always produce a strong visible colony pigment phenotype; include them only if evidence supports visible carotenoid accumulation.
2. **Photosynthesis gene clusters (PGC) that contain crt genes:** Carotenoid genes within PGCs can be tied to phototrophy and pigment-protein complexes; phenotypic pigmentation may be part of phototrophic physiology rather than a standalone colony-color trait (kopejtka2024minimaltranscriptionalregulation pages 4-8).
3. **Non-carotenoid pigments:** Melanins, violacein, prodigiosin, etc. are distinct pigment classes and should not be conflated with carotenoid pigmentation.

### 2) Key concepts and current understanding (mechanistic overview)

#### 2.1 Core biochemical concept: carotenoid classes and pathways
Carotenoids in microbes include:
- **Carotenes** (hydrocarbon carotenoids; e.g., phytoene, lycopene, β-carotene).
- **Xanthophylls** (oxygenated carotenoids; e.g., zeaxanthin, astaxanthin, nostoxanthin). A recent bacterial study reiterates classification: “Carotenoid pigments are classified as either carotenes or xanthophylls… when oxygen atoms are added, they are converted into xanthophylls.” (raman2024nostoxanthinbiosynthesisby pages 1-2).

Carotenoid biosynthesis generally draws on isoprenoid precursors produced by either:
- The **MEP (non-mevalonate) pathway**, supported in *Sphingopyxis* where metabolomics/genomics indicate absence of MVA genes and MVA intermediate mevalonate-5-pyrophosphate was “undetected” (liu2024metabolomicanalysisof pages 4-6).
- The **MVA pathway**, central in red yeasts such as *Xanthophyllomyces dendrorhous*, where upstream MVA genes (MVK/PMVK/MVD/IDI/FPS) were profiled in stress/light experiments (tobin2024omicsdrivenonboardingof pages 7-9).

#### 2.2 Canonical carotenoid gene set (crt genes) as graph backbone
Across diverse taxa, a reusable “core” causal chain is supported:
- **crtE**: geranylgeranyl pyrophosphate synthesis (GGPP node).
- **crtB**: phytoene synthase.
- **crtI**: phytoene desaturase controlling desaturation depth and product identity.
- **crtY / crtYB**: lycopene cyclization (often bifunctional in yeasts).

A high-impact 2023 *Nature Communications* study provides direct functional evidence for crtI’s role in desaturation “synthesizing both neurosporene and lycopene” via heterologous complementation and HPLC/spectral analysis (li2023globallydistributedmyxococcota pages 6-7). This supports a central graph edge: **crtI activity → carotenoid product identity**.

#### 2.3 Functional roles connected to pigmentation (why carotenoids matter)
Although the TraitMech focus is pigmentation, many studies connect carotenoids to:
- **Oxidative stress protection / free-radical scavenging**: staphyloxanthin “serves as an antioxidant… combating free radicals such as hydrogen peroxide and hydroxyl radicals” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2); bacterioruberin protects against “UV light and oxidative stresses” (ma2024thebiosynthesismechanism pages 1-2).
- **Membrane association/biophysics**: bacterioruberin is described as increasing “stability of membranes under high osmotic conditions” (ma2024thebiosynthesismechanism pages 1-2). Lycopene engineering figures/text note lycopene “is distributed in lipid structures” (zhan2024expandingthecrispr pages 10-12).
These functional links are important because they motivate causal edges from environment/stress → carotenoid biosynthesis → pigmentation phenotype.

### 3) Candidate nodes for `carotenoid_pigmentation.yaml` (grouped by type)

#### 3.1 Phenotype/trait nodes
- **METPO:1003031** carotenoid pigmentation (given)
- Candidate related phenotypes (label-only unless mapped):
  - “pigment intensity” / “colony color (yellow/orange/red/pink)” (zhan2024expandingthecrispr pages 10-12, raman2024nostoxanthinbiosynthesisby pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)
  - oxidative-stress resistance phenotype (linked to carotenoids in *Deinococcus* and *S. aureus*) (wang2024insightsintothe pages 12-12, nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)

#### 3.2 Pathways / modules
- **MEP pathway** (non-mevalonate isoprenoid biosynthesis) (liu2024metabolomicanalysisof pages 4-6)
- **MVA pathway** (mevalonate/terpenoid backbone in yeasts) (tobin2024omicsdrivenonboardingof pages 7-9)
- **Photosynthesis gene cluster (PGC)** containing crt genes (kopejtka2024minimaltranscriptionalregulation pages 4-8)
- **Proteorhodopsin chromophore/retinoid biosynthesis cluster** adjacent to PR: crtE-crtI-crtB-crtY (lee2024effectsoflight pages 10-11)

#### 3.3 Genes / proteins / enzymes (grounded where available)
- **crtE** (GGPP synthase) (tobin2024omicsdrivenonboardingof pages 7-9)
- **crtB** (phytoene synthase) (raman2024nostoxanthinbiosynthesisby pages 1-2)
- **crtI** (phytoene desaturase) (li2023globallydistributedmyxococcota pages 6-7)
- **crtY / crtYB** (lycopene β-cyclase; bifunctional lycopene cyclase/phytoene synthase in *X. dendrorhous*) (tobin2024omicsdrivenonboardingof pages 9-10)
- **crtS** (cytochrome P450 hydroxylase; astaxanthin pathway; KEGG K23037 referenced in yeast genomics) (tobin2024omicsdrivenonboardingof pages 9-10, hoondee2024comparativegenomicanalysis pages 10-13)
- **crtR** (P450 reductase; KEGG K14338 referenced in yeast genomics) (hoondee2024comparativegenomicanalysis pages 10-13)
- **Staphyloxanthin branch:**
  - **crtOPQMN operon** (staphyloxanthin synthesis regulation) (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)
  - **crtM** (dehydrosqualene synthase) (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)
- **Haloarchaeal C50 branch:** **lyeJ**, **crtD**, **cruF** (bacterioruberin pathway context) (ma2024thebiosynthesismechanism pages 1-2)
- **Engineering/support gene:** **cg0722** (membrane protein affecting lycopene production in *C. glutamicum*) (zhan2024expandingthecrispr pages 10-12)

#### 3.4 Chemicals / metabolites / products
(Label-only unless curies are added during curation)
- Precursors: IPP/DMAPP, GGPP, GFDP (liu2024metabolomicanalysisof pages 4-6, tobin2024omicsdrivenonboardingof pages 9-10)
- Carotenes: phytoene, phytofluene, lycopene, β-carotene (liu2024metabolomicanalysisof pages 4-6)
- Xanthophylls: zeaxanthin, astaxanthin, nostoxanthin (liu2024metabolomicanalysisof pages 4-6, raman2024nostoxanthinbiosynthesisby pages 1-2, duran2024increasingcarotenoidproduction pages 9-10)
- Specialized carotenoids: staphyloxanthin, bacterioruberin (ma2024thebiosynthesismechanism pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)

#### 3.5 Environmental and experimental factors
- **Ultraviolet / blue light exposure** (tobin2024omicsdrivenonboardingof pages 9-10, tobin2024omicsdrivenonboardingof pages 7-9)
- **Hydrogen peroxide oxidative stress** (tobin2024omicsdrivenonboardingof pages 7-9)
- **Osmotic down-shock** (ma2024thebiosynthesismechanism pages 1-2)
- Carbon/nutrient sources influencing titers: glucose, yeast extract, starch, tryptone (ma2024thebiosynthesismechanism pages 1-2, raman2024nostoxanthinbiosynthesisby pages 1-2)

#### 3.6 Regulators (transcriptional/signaling)
- **SREBP pathway / Sre1N (active Sre1 transcription factor)** (duran2024increasingcarotenoidproduction pages 9-10)
- **ECF sigma factor** controlling light-induced carotenogenesis in *Streptomyces coelicolor* (reported via cited work within Raman et al. excerpt) (raman2024nostoxanthinbiosynthesisby pages 13-13)
- Candidate light-sensing families in *X. dendrorhous*: cryptochrome, BLUF, rhodopsin, white collar (tobin2024omicsdrivenonboardingof pages 9-10)

#### 3.7 Inhibitors and perturbagens
- Anti-staphyloxanthin inhibitors (reported from prior work summarized in a 2024 study): “cerulenin, dihydrobisvertinol, xanthohumol, zaragozic acid… methylrabelomycin, and tetrangomycin” inhibiting pigment production (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)

### 4) Candidate causal edges (evidence-backed triples)

The following artifact compiles candidate edges with snippets, DOI-first references, and curation notes (including uncertainty flags).

| Edge (subject–predicate–object) | Node grounding hints (CURIEs/IDs if available) | Evidence snippet (short quote) | Reference (authors, year, DOI, URL, publication month/year) | Notes/uncertainty |
|---|---|---|---|---|
| crtI phytoene desaturase – determines product branch – neurosporene/lycopene | crtI; GO: phytoene desaturase activity candidate; CHEBI: phytoene / neurosporene / lycopene candidates | “crtI… functions as phytoene desaturase synthesizing both neurosporene and lycopene” and “Spheroidene-type carotenoids result from three desaturation/oxidation reactions… while spirilloxanthin-type pigments are synthesized via four desaturations to form lycopene.” (li2023globallydistributedmyxococcota pages 6-7) | Li et al., 2023. DOI:10.1038/s41467-023-42193-7. URL:https://doi.org/10.1038/s41467-023-42193-7. Oct 2023 | Strong functional evidence from heterologous complementation in Rba. sphaeroides mutant; taxon context is Myxococcota-derived crtI. |
| crtB knockout – blocks – carotenoid biosynthetic pathway | crtB; GO candidate: phytoene synthase activity | “Knockout of crtB or crtI gene blocks the carotenoid biosynthetic pathway in Deinococcus radiodurans R1” (wang2024insightsintothe pages 12-12) | Zhang et al., 2007, cited in Wang et al., 2024. DOI:10.1007/s00203-007-0262-5. Review URL:https://doi.org/10.3389/fmicb.2024.1447785. Jul 2024 review citing 2007 primary study | Curate with caution because snippet is from a 2024 review bibliography quoting the 2007 primary study rather than direct experimental pages. |
| crtI knockout – blocks – carotenoid biosynthetic pathway | crtI; GO candidate: phytoene desaturase activity | “Knockout of crtB or crtI gene blocks the carotenoid biosynthetic pathway in Deinococcus radiodurans R1” (wang2024insightsintothe pages 12-12) | Zhang et al., 2007, cited in Wang et al., 2024. DOI:10.1007/s00203-007-0262-5. Review URL:https://doi.org/10.3389/fmicb.2024.1447785. Jul 2024 review citing 2007 primary study | Same caution as above. |
| loss of crtB/crtI-dependent carotenoid synthesis – reduces resistance to – oxidative DNA-damaging agents | carotenoid biosynthetic pathway; phenotype node: oxidative stress resistance | “Knockout of crtB or crtI gene blocks the carotenoid biosynthetic pathway… and influences its resistance to oxidative DNA-damaging agents due to change of free radicals scavenging ability.” (wang2024insightsintothe pages 12-12) | Zhang et al., 2007, cited in Wang et al., 2024. DOI:10.1007/s00203-007-0262-5. Review URL:https://doi.org/10.3389/fmicb.2024.1447785. Jul 2024 review citing 2007 primary study | Supports edge from carotenoid pigmentation to oxidative/radiation-protection phenotype in Deinococcus; review-mediated evidence. |
| ultraviolet light exposure – upregulates – crtI expression | environmental factor: UV light; crtI; NCBITaxon candidate: Xanthophyllomyces dendrorhous | “Upstream mevalonate and terpenoid genes are not affected by ultraviolet, but downstream carotenoid biosynthetic genes crtI and crtS are upregulated, crtI most strongly.” (tobin2024omicsdrivenonboardingof pages 9-10) | Tobin et al., 2024. DOI:10.1007/s00253-024-13379-w. URL:https://doi.org/10.1007/s00253-024-13379-w. Dec 2024 | Strong RT-qPCR evidence. |
| ultraviolet light exposure – upregulates – crtS expression | UV light; crtS; KEGG:K23037 | “Upstream mevalonate and terpenoid genes are not affected by ultraviolet, but downstream carotenoid biosynthetic genes crtI and crtS are upregulated” (tobin2024omicsdrivenonboardingof pages 9-10) | Tobin et al., 2024. DOI:10.1007/s00253-024-13379-w. URL:https://doi.org/10.1007/s00253-024-13379-w. Dec 2024 | Strong RT-qPCR evidence. |
| ultraviolet light exposure – upregulates – crtYB expression | UV light; crtYB; bifunctional lycopene cyclase/phytoene synthase | “the expression of crtYB, crtI, and crtS was upregulated.” (tobin2024omicsdrivenonboardingof pages 7-9) | Tobin et al., 2024. DOI:10.1007/s00253-024-13379-w. URL:https://doi.org/10.1007/s00253-024-13379-w. Dec 2024 | Evidence from transcriptomics/qPCR summary; weaker than crtI/crtS figure-specific wording but still direct. |
| hydrogen peroxide oxidative stress – upregulates – IDI | hydrogen peroxide; IDI; mevalonate pathway | “oxidative stress upregulated genes in both pathways (MVK, PMVK, IDI, FPS, crtYB, and crtI), with IDI having the greatest increase” (tobin2024omicsdrivenonboardingof pages 7-9) | Tobin et al., 2024. DOI:10.1007/s00253-024-13379-w. URL:https://doi.org/10.1007/s00253-024-13379-w. Dec 2024 | Strong expression evidence; supports IDI as bottleneck/regulatory leverage point. |
| hydrogen peroxide oxidative stress – upregulates – crtYB/crtI and terpenoid genes | hydrogen peroxide; crtYB; crtI; MVK; PMVK; FPS | “oxidative stress upregulated genes in both pathways (MVK, PMVK, IDI, FPS, crtYB, and crtI)” (tobin2024omicsdrivenonboardingof pages 7-9) | Tobin et al., 2024. DOI:10.1007/s00253-024-13379-w. URL:https://doi.org/10.1007/s00253-024-13379-w. Dec 2024 | Good general regulatory edge; may be split into several edges during curation. |
| active Sre1N + HMGS promoter substitution – increases – crtE transcript levels | SREBP pathway; Sre1N; HMGS promoter; crtE | “Replacing the crtE promoter with the HMGS promoter containing SRE sites (pHMGS/crtE) raised crtE transcripts up to four-fold in strains with active Sre1N” (duran2024increasingcarotenoidproduction pages 9-10) | Durán et al., 2024. DOI:10.1186/s40659-024-00559-1. URL:https://doi.org/10.1186/s40659-024-00559-1. Nov 2024 | Strong mechanistic engineering evidence in X. dendrorhous. |
| increased crtE transcription under active Sre1N – increases – carotenoid production | crtE; GGPP synthesis; carotenoid biosynthetic process | “resulting in 1.43-fold and 1.22-fold increases in carotenoid production” and “total carotenoids increased… to 921.8 ± 57.6” (duran2024increasingcarotenoidproduction pages 9-10) | Durán et al., 2024. DOI:10.1186/s40659-024-00559-1. URL:https://doi.org/10.1186/s40659-024-00559-1. Nov 2024 | Strong quantitative evidence; phenotype includes visible reddish color increase in active-Sre1 strains. |
| bacterioruberin biosynthesis – is coupled to – growth/logarithmic phase | bacterioruberin; growth phase; NCBITaxon candidate: Halorubrum sp. | “BR synthesis is highly coupled with growth, which was most active in the logarithm phase.” (ma2024thebiosynthesismechanism pages 1-2) | Ma et al., 2024. DOI:10.1128/AEM.00540-24. URL:https://doi.org/10.1128/AEM.00540-24. Jul 2024 | Strong for haloarchaeal BR-specific subgraph; taxon/product-specific. |
| osmotic down-shock at logarithmic phase – increases – bacterioruberin productivity | osmotic down-shock; bacterioruberin productivity | “the osmotic down shock at the logarithm phase could increase the BR productivity without sacrificing the biomass.” (ma2024thebiosynthesismechanism pages 1-2) | Ma et al., 2024. DOI:10.1128/AEM.00540-24. URL:https://doi.org/10.1128/AEM.00540-24. Jul 2024 | Strong condition-to-output edge for BR-producing haloarchaea. |
| bacterioruberin – stabilizes – membranes under high osmotic conditions | bacterioruberin; membrane stabilization; GO candidate: membrane organization | “BR has been reported to increase the stability of membranes under high osmotic conditions” (ma2024thebiosynthesismechanism pages 1-2) | Ma et al., 2024. DOI:10.1128/AEM.00540-24. URL:https://doi.org/10.1128/AEM.00540-24. Jul 2024 | Functional role, partly based on prior literature summarized in introduction. |
| bacterioruberin – protects against – UV light and oxidative stresses | bacterioruberin; UV protection; oxidative stress protection | “and protect cells against UV light and oxidative stresses” (ma2024thebiosynthesismechanism pages 1-2) | Ma et al., 2024. DOI:10.1128/AEM.00540-24. URL:https://doi.org/10.1128/AEM.00540-24. Jul 2024 | Functional role; useful phenotype-level edge. |
| MEP pathway – produces – GFDP in Sphingopyxis sp. USTB-05 | MEP pathway; GFDP; NCBITaxon candidate: Sphingopyxis sp. USTB-05 | “Sphingopyxis sp. USTB-05 synthesized Geranylfarnesyldiphosphate (GFDP) through the MEP pathway” (liu2024metabolomicanalysisof pages 4-6) | Liu et al., 2024. DOI:10.3390/molecules29174235. URL:https://doi.org/10.3390/molecules29174235. Sep 2024 | Strong metabolomics/genome-supported pathway edge. |
| phytoene synthase – converts – GFDP to phytoene | phytoene synthase / crtB; GFDP; phytoene | “Through the catalytic action of phytoene synthase, GFDP undergoes condensation to form phytoene.” (liu2024metabolomicanalysisof pages 4-6) | Liu et al., 2024. DOI:10.3390/molecules29174235. URL:https://doi.org/10.3390/molecules29174235. Sep 2024 | Strong pathway step. Grounding of GFDP may require label-only if no stable CHEBI used. |
| phytoene dehydrogenase/desaturase – converts – phytoene to phytofluene to lycopene | crtI/dehydrogenase; phytoene; phytofluene; lycopene | “Phytoene is further dehydrogenated by dehydrogenase to generate phytofluene, which is subsequently converted into lycopene.” (liu2024metabolomicanalysisof pages 4-6) | Liu et al., 2024. DOI:10.3390/molecules29174235. URL:https://doi.org/10.3390/molecules29174235. Sep 2024 | Strong pathway step; exact enzyme naming generic in paper excerpt. |
| lycopene cyclases – convert – lycopene to α-/ε-/β-carotene | crtY / lycopene cyclases; lycopene; β-carotene | “The cyclization of lycopene… lead[s] to the formation of α-carotene, ε-carotene, and β-carotene under the catalysis of various lycopene cyclases.” (liu2024metabolomicanalysisof pages 4-6) | Liu et al., 2024. DOI:10.3390/molecules29174235. URL:https://doi.org/10.3390/molecules29174235. Sep 2024 | Good pathway edge; specific cyclase gene may vary across taxa. |
| Sphingopyxis sp. USTB-05 – accumulates – zeaxanthin abundantly | zeaxanthin; Sphingopyxis sp. USTB-05 | “The average content of zeaxanthin was the highest… with 37.06 µg/g and 35.25 µg/g, respectively.” (liu2024metabolomicanalysisof pages 4-6) | Liu et al., 2024. DOI:10.3390/molecules29174235. URL:https://doi.org/10.3390/molecules29174235. Sep 2024 | Useful phenotype-output edge; abundance rather than direct causation. |
| crtOPQMN operon – mediates – staphyloxanthin biosynthesis | crtOPQMN operon; staphyloxanthin; NCBITaxon: Staphylococcus aureus candidate | “Its synthesis is regulated by the crtOPQMN operon.” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | Nirmala et al., 2024. DOI:10.7759/cureus.59892. URL:https://doi.org/10.7759/cureus.59892. May 2024 | Good organism-specific carotenoid operon edge. |
| CrtM – converts – farnesyl diphosphate to dehydrosqualene | CrtM; farnesyl diphosphate (FPP); dehydrosqualene | “Staphyloxanthin synthesis begins with the conversion of farnesyl diphosphate into dehydrosqualene catalyzed by the enzyme dehydrosqualene synthase (CrtM).” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | Nirmala et al., 2024. DOI:10.7759/cureus.59892. URL:https://doi.org/10.7759/cureus.59892. May 2024 | Strong pathway-start edge for staphyloxanthin branch. |
| staphyloxanthin – protects against – hydrogen peroxide and hydroxyl radicals | staphyloxanthin; reactive oxygen species | “Staphyloxanthin serves as an antioxidant, aiding S. aureus in combating free radicals such as hydrogen peroxide and hydroxyl radicals” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | Nirmala et al., 2024. DOI:10.7759/cureus.59892. URL:https://doi.org/10.7759/cureus.59892. May 2024 | Strong function edge; ties pigment to oxidative-stress phenotype. |
| staphyloxanthin – contributes to – virulence | staphyloxanthin; virulence trait | “serves not only to impart color but also functions as a crucial antioxidant contributing to virulence” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | Nirmala et al., 2024. DOI:10.7759/cureus.59892. URL:https://doi.org/10.7759/cureus.59892. May 2024 | Supports phenotype-level pathogenicity edge; may be outside core TraitMech if focusing only pigmentation. |
| cerulenin / dihydrobisvertinol / xanthohumol / zaragozic acid / methylrabelomycin / tetrangomycin – inhibit – staphyloxanthin production | inhibitor nodes as labels; staphyloxanthin biosynthetic process | “cerulenin, dihydrobisvertinol, xanthohumol, zaragozic acid… methylrabelomycin, and tetrangomycin, effectively hindered staphyloxanthin production” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | Nirmala et al., 2024. DOI:10.7759/cureus.59892. URL:https://doi.org/10.7759/cureus.59892. May 2024 | Inhibitor list is from cited prior work summarized in 2024 paper; curate as literature-backed but not directly re-tested here. |
| double knockout crtEb/crtR – increases – lycopene accumulation and changes colony color to pink | crtEb; crtR; lycopene; colony color phenotype | “the simultaneous knockout of crtR and crtEb caused a distinct shift in the colony colour from light yellow to pink” and “reaching lycopene production of 8.35 mg/L” (zhan2024expandingthecrispr pages 10-12) | Zhan et al., 2024. DOI:10.3390/microorganisms12040803. URL:https://doi.org/10.3390/microorganisms12040803. Apr 2024 | Strong engineering evidence in C. glutamicum; excellent phenotype readout edge. |
| overexpression of cg0722-crtB-crtI in ΔcrtEbΔcrtR background – increases – lycopene titer | cg0722; crtB; crtI; lycopene; NCBITaxon: Corynebacterium glutamicum | “the CBIEbR strain produced the highest lycopene yields of 23.12 mg/L” and in fed-batch “405.02 mg/L (9.52 mg/g DCW)” (zhan2024expandingthecrispr pages 10-12) | Zhan et al., 2024. DOI:10.3390/microorganisms12040803. URL:https://doi.org/10.3390/microorganisms12040803. Apr 2024 | Strong synthetic-biology edge; phenotype is engineered lycopene pigmentation rather than native trait expression. |
| Sphingomonas sp. COS14-R2 crtB/crtI/crtY gene set – enables – nostoxanthin production / deep yellow colony pigmentation | crtB; crtI; crtY; nostoxanthin; NCBITaxon candidate: Sphingomonas sp. COS14-R2 | “The genome consists of three carotenoid biosynthesis genes, specifically crtB… crtI… and crtY… involved in the synthesis of nostoxanthin.” (raman2024nostoxanthinbiosynthesisby pages 1-2) | Raman et al., 2024. DOI:10.1007/s00284-024-03956-7. URL:https://doi.org/10.1007/s00284-024-03956-7. Nov 2024 | Gene-to-product link is stated in abstract; direct knockout evidence not shown in excerpt. |
| Sphingomonas sp. COS14-R2 – has phenotype – deep yellow colony | carotenoid pigmentation phenotype; nostoxanthin candidate | “The strain has a circular, undulated colony morphology with a deep yellow color.” (raman2024nostoxanthinbiosynthesisby pages 1-2) | Raman et al., 2024. DOI:10.1007/s00284-024-03956-7. URL:https://doi.org/10.1007/s00284-024-03956-7. Nov 2024 | Useful assay-observed phenotype edge. |
| proteorhodopsin-adjacent crtE-crtI-crtB-crtY cluster – is genomically linked to – retinal/chromophore biosynthesis | crtE-crtI-crtB-crtY cluster; proteorhodopsin locus | “a proteorhodopsin (PR) locus with an adjacent rhodopsin chromophore biosynthesis cluster (crtE-crtI-crtB-crtY).” (lee2024effectsoflight pages 10-11) | Lee & Oh, 2024. DOI:10.1007/s12275-024-00125-0. URL:https://doi.org/10.1007/s12275-024-00125-0. Apr 2024 | Boundary-case edge: carotenoid-pathway genes used for retinal/chromophore context, not necessarily visible pigmentation. |
| light regime – regulates – proteorhodopsin-adjacent crtE-crtI-crtB-crtY cluster | light/dark condition; crt cluster | “the rhodopsin chromophore cluster (crtE-crtI-crtB-crtY) ‘was downregulated under LL6,’ while a ‘retinoid biosynthesis gene was upregulated in LD6.’” (lee2024effectsoflight pages 12-14) | Lee & Oh, 2024. DOI:10.1007/s12275-024-00125-0. URL:https://doi.org/10.1007/s12275-024-00125-0. Apr 2024 | Strong light-dependent regulation evidence, but this is a boundary case linking carotenoid genes to rhodopsin chromophore metabolism rather than canonical carotenoid pigmentation. |


*Table: This table compiles curation-ready candidate causal edges for microbial carotenoid pigmentation, including grounded nodes, exact supporting snippets, and DOI-first references. It is useful for selecting robust TraitMech edges while flagging taxon-specific and boundary-case claims.*

### 5) Recent developments (2023–2024) and what they change for TraitMech graphs

#### 5.1 Regulatory layer: light/UV and oxidative stress directly modulate crt expression
- In *Xanthophyllomyces dendrorhous* (2024), UV exposure primarily affected **downstream carotenoid genes**: “Upstream mevalonate and terpenoid genes are not affected by ultraviolet, but downstream carotenoid biosynthetic genes crtI and crtS are upregulated” (tobin2024omicsdrivenonboardingof pages 9-10). This supports adding explicit **UV/light → crtI/crtS transcription → carotenoid accumulation/pigmentation** edges.
- Oxidative stress (H2O2) broadened transcriptional activation in *X. dendrorhous*: “oxidative stress upregulated genes in both pathways… with IDI having the greatest increase (log2 fold-change of 1.79)” (tobin2024omicsdrivenonboardingof pages 7-9). This supports a graph where oxidative stress increases precursor supply (IDI and upstream MVA flux) plus carotenogenesis.
- In a marine bacterium with PR-adjacent crt genes, the “rhodopsin chromophore cluster (crtE-crtI-crtB-crtY) ‘was downregulated under LL6’” and retinoid genes were condition-dependent (lee2024effectsoflight pages 12-14), supporting **light-regulated carotenoid-related loci** as a boundary-case module.

#### 5.2 Engineering: stronger genotype→pigmentation links and quantitative phenotype mapping
- A 2024 CRISPR/MAD7 engineering study in *C. glutamicum* achieved high lycopene titers and a strong visual phenotype: double knockout caused colony color to shift “from light yellow to pink” and yielded 8.35 mg/L; the engineered CBIEbR strain reached “405.02 mg/L (9.52 mg/g DCW)” in fed-batch fermentation (zhan2024expandingthecrispr pages 10-12). This is a clear model for curating **genetic perturbation → carotenoid accumulation → visible pigmentation**.

#### 5.3 Expanding taxonomic coverage: haloarchaeal C50 carotenoid modules
- A 2024 *Applied and Environmental Microbiology* study frames bacterioruberin (C50 carotenoid) as a **membrane structural component** with stress protective roles: it “increase[s] the stability of membranes under high osmotic conditions, and protect[s] cells against UV light and oxidative stresses” (ma2024thebiosynthesismechanism pages 1-2), and its synthesis is “highly coupled with growth” (ma2024thebiosynthesismechanism pages 1-2). This supports adding a C50-specific subgraph (lyeJ/crtD/cruF) when curating haloarchaeal carotenoid pigmentation.

### 6) Current applications and real-world implementations

**(i) Industrial/bioprocess production of carotenoids (real implementations):**
- Microbial fermentation is emphasized as a practical alternative to plant extraction: “Bacterial fermentation presents a very efficient substitute source” for carotenoids (raman2024nostoxanthinbiosynthesisby pages 1-2). Recent demonstrations include:
  - *Sphingomonas* COS14-R2 fed-batch: 217.22 ± 9.60 mg/L nostoxanthin (raman2024nostoxanthinbiosynthesisby pages 1-2).
  - *C. glutamicum* fed-batch: 405.02 mg/L lycopene (zhan2024expandingthecrispr pages 10-12).
  - Red yeasts (*Rhodotorula* spp.) optimized astaxanthin yields reaching ~3.689–4.680 mg/L (hoondee2024comparativegenomicanalysis pages 16-18).

**(ii) Food/cosmetics pigments:**
- Staphyloxanthin work explicitly positions microbial carotenoids for “industrial applications, such as integration into paints, fabrics, and sunscreen lotions” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2). Although the paper is not an industrial deployment report, it reflects ongoing translation of microbial pigments into materials/cosmetics.

**(iii) Anti-virulence strategies (staphyloxanthin):**
- Staphyloxanthin is described as a “significant virulence factor” and antioxidant in *S. aureus* (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2). The same paper summarizes prior identification of multiple inhibitors that “hindered staphyloxanthin production” (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2), motivating a TraitMech-adjacent subgraph linking inhibitors → reduced carotenoid pigmentation → reduced virulence/ROS resistance.

### 7) Statistics and recent quantitative data (curation-relevant)

Selected quantitative data points useful for weighting edges or benchmarking trait expression:
- **Engineered lycopene:** CBIEbR *C. glutamicum* reached **405.02 mg/L** lycopene (**9.52 mg/g DCW**) at 96 h in 5 L fed-batch; OD600 reached 228 (zhan2024expandingthecrispr pages 10-12).
- **Nostoxanthin production:** COS14-R2 produced **217.22 ± 9.60 mg/L** nostoxanthin (fed-batch) with **72.32% selectivity** and DPPH scavenging **75.5 ± 0.33%** (raman2024nostoxanthinbiosynthesisby pages 1-2).
- **Red yeast astaxanthin:** optimized yields of **3.689 ± 0.031 mg/L** and **4.680 ± 0.019 mg/L** in *Rhodotorula paludigena* TL35-5 and *R. sampaioana* PL61-2, respectively (hoondee2024comparativegenomicanalysis pages 16-18).
- **X. dendrorhous carotenoid composition:** total carotenoids up to **921.8 ± 57.6 ppm (µg/g dry yeast)** in an engineered strain background with pHMGS/crtE and active Sre1 signaling (duran2024increasingcarotenoidproduction pages 9-10).
- **Bacterial natural carotenoid profiles:** *Sphingopyxis* USTB-05 zeaxanthin ~**37.06 µg/g** at mid-log and phytoene ~**2.32 µg/g**, with strong decreases by end-log for β-carotene and phytoene (~84% reductions) (liu2024metabolomicanalysisof pages 4-6).

### 8) Expert/authoritative analysis (as stated by study authors)

- **Photoregulation insight:** Authors conclude “carotenoid biosynthesis is light regulated through transcriptional activation” in *X. dendrorhous* (tobin2024omicsdrivenonboardingof pages 7-9), supporting incorporation of transcriptional regulation nodes (light receptors; stress-response) into causal graphs.
- **Industrial translation framing in haloarchaea:** Halophilic archaea are positioned as “promising… microbial cell factories” due to reduced contamination risk and ability to use seawater/brine, with carotenoids as key metabolites (ma2024thebiosynthesismechanism pages 1-2). This provides an authoritative rationale for including **environment (hypersalinity) → carotenoid accumulation** context nodes.

### 9) Warnings / claims not yet ready for TraitMech curation

1. **Review-mediated claims about *Deinococcus* crt knockouts:** The evidence that crtB/crtI knockouts affect oxidative DNA-damage resistance is quoted in a 2024 review bibliography section (wang2024insightsintothe pages 12-12) that cites a 2007 primary study. This is credible, but for curation it is preferable to pull the **primary paper text** directly before treating as high-confidence edges.
2. **Inhibitor lists for staphyloxanthin:** The inhibitor set (cerulenin, dihydrobisvertinol, etc.) is summarized in 2024 from prior work (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2). Curate as literature-backed but label as **not experimentally re-validated in the 2024 media-formulation study**.
3. **PR-adjacent crt clusters:** These loci may primarily support retinal/chromophore metabolism (functional for proteorhodopsin) rather than strong visible colony carotenoid pigmentation; include only if your trait definition includes this broader chromophore-related “carotenoid module” boundary case (lee2024effectsoflight pages 10-11, lee2024effectsoflight pages 12-14).
4. **Product-specific edges may be taxon-specific:** e.g., bacterioruberin (C50) membrane coupling and osmotic regulation are archaeal-specific (ma2024thebiosynthesismechanism pages 1-2). This should be modeled as a branch/subgraph rather than assumed universal.

---

## DOI-first bibliography (with URLs and publication dates)

1. Li L, Huang D, Hu Y, et al. *Globally distributed Myxococcota with photosynthesis gene clusters illuminate the origin and evolution of a potentially chimeric lifestyle.* Nature Communications. **Oct 2023**. DOI: **10.1038/s41467-023-42193-7**. https://doi.org/10.1038/s41467-023-42193-7 (li2023globallydistributedmyxococcota pages 6-7)
2. Zhan Z, Chen X, Ye Z, et al. *Expanding the CRISPR Toolbox for Engineering Lycopene Biosynthesis in Corynebacterium glutamicum.* Microorganisms. **Apr 2024**. DOI: **10.3390/microorganisms12040803**. https://doi.org/10.3390/microorganisms12040803 (zhan2024expandingthecrispr pages 10-12)
3. Ma Y, Sun Z, Yang H, et al. *The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis.* Applied and Environmental Microbiology. **Jul 2024** (published online **Jun 2024** in text). DOI: **10.1128/aem.00540-24**. https://doi.org/10.1128/aem.00540-24 (ma2024thebiosynthesismechanism pages 1-2)
4. Liu C, Xu Q, Liu Y, et al. *Metabolomic Analysis of Carotenoids Biosynthesis by Sphingopyxis sp. USTB-05.* Molecules. **Sep 2024**. DOI: **10.3390/molecules29174235**. https://doi.org/10.3390/molecules29174235 (liu2024metabolomicanalysisof pages 4-6)
5. Lee JH, Oh H-M. *Effects of Light and Dark Conditions on the Transcriptome of Aging Cultures of Candidatus Puniceispirillum marinum IMCC1322.* Journal of Microbiology. **Apr 2024**. DOI: **10.1007/s12275-024-00125-0**. https://doi.org/10.1007/s12275-024-00125-0 (lee2024effectsoflight pages 12-14)
6. Nirmala B, Omar BJ, Omar Sr B. *Enhancing Staphyloxanthin Synthesis in Staphylococcus aureus Using Innovative Agar Media Formulations.* Cureus. **May 2024**. DOI: **10.7759/cureus.59892**. https://doi.org/10.7759/cureus.59892 (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)
7. Hoondee P, Phuengjayaem S, Kingkaew E, et al. *Comparative genomic analysis and optimization of astaxanthin production of Rhodotorula paludigena TL35-5 and Rhodotorula sampaioana PL61-2.* PLOS ONE. **Jul 2024**. DOI: **10.1371/journal.pone.0304699**. https://doi.org/10.1371/journal.pone.0304699 (hoondee2024comparativegenomicanalysis pages 16-18)
8. Durán A, Venegas M, Barahona S, et al. *Increasing carotenoid production in Xanthophyllomyces dendrorhous/Phaffia rhodozyma: SREBP pathway activation and promoter engineering.* Biological Research. **Nov 2024**. DOI: **10.1186/s40659-024-00559-1**. https://doi.org/10.1186/s40659-024-00559-1 (duran2024increasingcarotenoidproduction pages 9-10)
9. Tobin EE, Collins JH, Marsan CB, et al. *Omics-driven onboarding of the carotenoid producing red yeast Xanthophyllomyces dendrorhous CBS 6938.* Applied Microbiology and Biotechnology. **Dec 2024**. DOI: **10.1007/s00253-024-13379-w**. https://doi.org/10.1007/s00253-024-13379-w (tobin2024omicsdrivenonboardingof pages 7-9)
10. Wang Y, Liu J, Yi Y, et al. *Insights into the synthesis, engineering, and functions of microbial pigments in Deinococcus bacteria.* Frontiers in Microbiology. **Jul 2024**. DOI: **10.3389/fmicb.2024.1447785**. https://doi.org/10.3389/fmicb.2024.1447785 (wang2024insightsintothe pages 12-12)
11. Raman J, Kim J-S, Ko Y-J, Kim S-J. *Nostoxanthin Biosynthesis by Sphingomonas Species (COS14-R2): Isolation, Identification, and Optimization of Culture Conditions.* Current Microbiology. **Published online Nov 2024**. DOI: **10.1007/s00284-024-03956-7**. https://doi.org/10.1007/s00284-024-03956-7 (raman2024nostoxanthinbiosynthesisby pages 1-2)


References

1. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 5 citations.

2. (zhan2024expandingthecrispr pages 10-12): Zhimin Zhan, Xiong Chen, Zhifang Ye, Ming Zhao, Cheng Li, Shipeng Gao, Anthony J. Sinskey, Lan Yao, Jun Dai, Yiming Jiang, and Xueyun Zheng. Expanding the crispr toolbox for engineering lycopene biosynthesis in corynebacterium glutamicum. Microorganisms, 12:803, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040803, doi:10.3390/microorganisms12040803. This article has 10 citations.

3. (lee2024effectsoflight pages 10-11): Ji Hyen Lee and Hyun-Myung Oh. Effects of light and dark conditions on the transcriptome of aging cultures of candidatus puniceispirillum marinum imcc1322. Journal of microbiology, 62:297-314, Apr 2024. URL: https://doi.org/10.1007/s12275-024-00125-0, doi:10.1007/s12275-024-00125-0. This article has 2 citations and is from a peer-reviewed journal.

4. (kopejtka2024minimaltranscriptionalregulation pages 4-8): Karel Kopejtka, Jürgen Tomasch, Sahana Shivaramu, Mohit Kumar Saini, David Kaftan, and Michal Koblížek. Minimal transcriptional regulation of horizontally transferred photosynthesis genes in phototrophic bacterium <i>gemmatimonas phototrophica</i>. mSystems, Sep 2024. URL: https://doi.org/10.1128/msystems.00706-24, doi:10.1128/msystems.00706-24. This article has 7 citations and is from a peer-reviewed journal.

5. (raman2024nostoxanthinbiosynthesisby pages 1-2): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 4 citations and is from a peer-reviewed journal.

6. (liu2024metabolomicanalysisof pages 4-6): Chaowang Liu, Qianqian Xu, Yang Liu, Meijie Song, Xiaoyu Cao, Xinyue Du, and Hai Yan. Metabolomic analysis of carotenoids biosynthesis by sphingopyxis sp. ustb-05. Molecules, 29:4235, Sep 2024. URL: https://doi.org/10.3390/molecules29174235, doi:10.3390/molecules29174235. This article has 3 citations.

7. (tobin2024omicsdrivenonboardingof pages 7-9): Emma E. Tobin, Joseph H. Collins, Celeste B. Marsan, Gillian T. Nadeau, Kim Mori, Anna Lipzen, Stephen Mondo, Igor V. Grigoriev, and Eric M. Young. Omics-driven onboarding of the carotenoid producing red yeast xanthophyllomyces dendrorhous cbs 6938. Dec 2024. URL: https://doi.org/10.1007/s00253-024-13379-w, doi:10.1007/s00253-024-13379-w. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (li2023globallydistributedmyxococcota pages 6-7): Liuyang Li, Danyue Huang, Yaoxun Hu, Nicola M. Rudling, Daniel P. Canniffe, Fengping Wang, and Yinzhao Wang. Globally distributed myxococcota with photosynthesis gene clusters illuminate the origin and evolution of a potentially chimeric lifestyle. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42193-7, doi:10.1038/s41467-023-42193-7. This article has 73 citations and is from a highest quality peer-reviewed journal.

9. (ma2024thebiosynthesismechanism pages 1-2): Yingchao Ma, Zhongshi Sun, Huan Yang, Weiguang Xie, Mengyu Song, Bo Zhang, and Liying Sui. The biosynthesis mechanism of bacterioruberin in halophilic archaea revealed by genome and transcriptome analysis. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00540-24, doi:10.1128/aem.00540-24. This article has 14 citations and is from a peer-reviewed journal.

10. (wang2024insightsintothe pages 12-12): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 17 citations and is from a peer-reviewed journal.

11. (tobin2024omicsdrivenonboardingof pages 9-10): Emma E. Tobin, Joseph H. Collins, Celeste B. Marsan, Gillian T. Nadeau, Kim Mori, Anna Lipzen, Stephen Mondo, Igor V. Grigoriev, and Eric M. Young. Omics-driven onboarding of the carotenoid producing red yeast xanthophyllomyces dendrorhous cbs 6938. Dec 2024. URL: https://doi.org/10.1007/s00253-024-13379-w, doi:10.1007/s00253-024-13379-w. This article has 4 citations and is from a domain leading peer-reviewed journal.

12. (hoondee2024comparativegenomicanalysis pages 10-13): Patcharaporn Hoondee, Sukanya Phuengjayaem, Engkarat Kingkaew, Pornchai Rojsitthisak, Boonchoo Sritularak, Somphob Thompho, Natapol Pornputtapong, Worathat Thitikornpong, and Somboon Tanasupawat. Comparative genomic analysis and optimization of astaxanthin production of rhodotorula paludigena tl35-5 and rhodotorula sampaioana pl61-2. PLOS ONE, 19:e0304699, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0304699, doi:10.1371/journal.pone.0304699. This article has 9 citations and is from a peer-reviewed journal.

13. (duran2024increasingcarotenoidproduction pages 9-10): Alejandro Durán, Maximiliano Venegas, Salvador Barahona, Dionisia Sepúlveda, Marcelo Baeza, Víctor Cifuentes, and Jennifer Alcaíno. Increasing carotenoid production in xanthophyllomyces dendrorhous/phaffia rhodozyma: srebp pathway activation and promoter engineering. Biological Research, Nov 2024. URL: https://doi.org/10.1186/s40659-024-00559-1, doi:10.1186/s40659-024-00559-1. This article has 5 citations and is from a peer-reviewed journal.

14. (raman2024nostoxanthinbiosynthesisby pages 13-13): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 4 citations and is from a peer-reviewed journal.

15. (lee2024effectsoflight pages 12-14): Ji Hyen Lee and Hyun-Myung Oh. Effects of light and dark conditions on the transcriptome of aging cultures of candidatus puniceispirillum marinum imcc1322. Journal of microbiology, 62:297-314, Apr 2024. URL: https://doi.org/10.1007/s12275-024-00125-0, doi:10.1007/s12275-024-00125-0. This article has 2 citations and is from a peer-reviewed journal.

16. (hoondee2024comparativegenomicanalysis pages 16-18): Patcharaporn Hoondee, Sukanya Phuengjayaem, Engkarat Kingkaew, Pornchai Rojsitthisak, Boonchoo Sritularak, Somphob Thompho, Natapol Pornputtapong, Worathat Thitikornpong, and Somboon Tanasupawat. Comparative genomic analysis and optimization of astaxanthin production of rhodotorula paludigena tl35-5 and rhodotorula sampaioana pl61-2. PLOS ONE, 19:e0304699, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0304699, doi:10.1371/journal.pone.0304699. This article has 9 citations and is from a peer-reviewed journal.