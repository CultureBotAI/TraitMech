---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:59:30.158501'
end_time: '2026-08-04T08:08:05.648611'
duration_seconds: 515.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cream pigmented
  trait_identifier: METPO:1003024
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cream_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which colony or cell coloration is a pale,
    off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing
    pigments.
  parent_traits: METPO:1003021
  synonyms: Pigment_cream
  evidence_summary: 'DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid
    pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the
    basis for cream/pale coloration in many bacterial taxa.)'
  causal_graph_summary: 'cream_pigmented_low_carotenoid_density: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cream pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003024
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which colony or cell coloration is a pale, off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_cream
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the basis for cream/pale coloration in many bacterial taxa.)
- **Existing causal graph summary:** cream_pigmented_low_carotenoid_density: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **cream pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cream_pigmented.yaml`.

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
- **Trait label:** cream pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003024
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which colony or cell coloration is a pale, off-white or cream hue, typically reflecting low-density carotenoid or other light-absorbing pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_cream
- **Existing evidence:** DOI:10.1146/annurev.micro.62.081307.162844: bacterial carotenoid pigments (Bacterial-carotenoid review supports low-abundance carotenoids as the basis for cream/pale coloration in many bacterial taxa.)
- **Existing causal graph summary:** cream_pigmented_low_carotenoid_density: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **cream pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cream_pigmented.yaml`.

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


# Curation-focused research report: microbial “cream pigmented”

## Executive assessment

**Target trait:** **METPO:1003024** (“cream pigmented”; synonym *Pigment_cream*)  
**Category/kind:** MORPHOLOGY / CLASS  
**Parent:** METPO:1003021  
**Recommended interpretation:** an **assay-observed colony or cell-color phenotype**, not a metabolic capacity. It denotes pale off-white/cream coloration under specified culture conditions.

The strongest support for the existing graph concept is that visible color depends on intracellular pigment concentration and that cream can be an early, weakly pigmented state preceding yellow/orange pigmentation. However, the literature does **not** establish a universal equation of “cream” with “low carotenoid density.” Cream colonies may instead be non-carotenogenic, transiently carotenogenic, affected by medium/background, or colored by chemically unrelated pigments. The causal graph should therefore represent low carotenoid abundance as one **candidate mechanism with an uncertainty qualifier**, rather than the defining mechanism of METPO:1003024. Pigment visibility has explicitly been reported to depend on concentration, while *Mycobacterium goodii* changes from off-white/cream at 2–4 days to yellow-orange at 10–15 days. (tran2020broughttoyou pages 7-9)

## 1. Trait scope and boundaries

### Included phenotype

The trait covers colonies or cells described as **cream, creamy, pale cream, buff-cream, or off-white-to-cream**, provided color is intrinsic to the organism and recorded with assay conditions. A useful direct boundary example is *M. goodii*, which produces “off-white to cream colonies in 2–4 days” that subsequently “turn yellow-orange after 10–15 days.” Thus, cream may be a time-dependent point on a pigment-accumulation trajectory rather than a stable endpoint. (tran2020broughttoyou pages 7-9)

In *Staphylococcus capitis*, investigators likewise observed pigmented strains change “from cream with a yellowish tinge to yellow.” Yellow pigmentation was visible on low-nutrient R2A agar after 24 h but only after 72 h on TSA, demonstrating that medium and observation time are integral parts of the phenotype. (siems2023identificationofstaphyloxanthin pages 3-4, siems2023identificationofstaphyloxanthin pages 4-6)

### Boundary cases

1. **White/colorless or non-pigmented:** do not automatically map to cream. In *S. capitis*, non-pigmented strains appeared white and lacked the multiple carotenoid peaks seen in yellow strains. (siems2023identificationofstaphyloxanthin pages 4-6)
2. **Yellow, gold, orange, or rust:** adjacent but stronger/different pigmentation classes. A colony that matures from cream to yellow-orange should have time-indexed observations rather than one timeless color assertion. (tran2020broughttoyou pages 7-9)
3. **Buff or tan:** potentially compatible only where the source or curation standard treats the hue as pale cream; otherwise retain the original descriptor.
4. **Medium-derived appearance:** blood agar, colored substrates, pH indicators, precipitates, opacity, and reflected light can obscure intrinsic color. In *S. capitis*, all strains appeared similarly white on Columbia blood agar, whereas strain-specific yellow pigmentation was apparent on R2A/TSA. The published colony photographs reinforce this assay dependence. (siems2023identificationofstaphyloxanthin media 0222358e, siems2023identificationofstaphyloxanthin pages 4-6)
5. **Non-carotenoid cream pigmentation:** melanin, flavins, phenazines, quinones, extracellular polymers, cell density, and scattering may affect pale colony color. No carotenoid mechanism should be assigned without chemical, spectroscopic, genetic, or perturbational evidence.

## 2. Current mechanistic understanding

Carotenoids are conjugated isoprenoid pigments; a generic pathway begins with precursor supply, CrtE-mediated geranylgeranyl pyrophosphate (GGPP) formation, CrtB-mediated phytoene synthesis, and CrtI-mediated desaturation to increasingly conjugated—and therefore more visibly colored—carotenoids. In purple bacteria, CrtE supplies GGPP, and CrtB converts two GGPP molecules into 15-cis-phytoene. CrtI-deficient mutants accumulate phytoene, establishing CrtI as the phytoene desaturase catalyzing sequential conversion through phytofluene to neurosporene in that pathway. (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5)

The phenotype-producing bridge is pigment abundance and composition. A mycobacterial review states directly that whether pigment is visible depends on its concentration. In 2023 *S. capitis* experiments, pigmented strains had several HPLC peaks and strong carotenoid Raman bands, whereas non-pigmented strains had only one minor/indistinct peak. This supports **carotenoid abundance/composition → visible pigmentation**, but does not establish a universal numerical threshold for cream. (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 4-6)

## 3. Candidate nodes grouped by type

### Trait and process nodes

- **cream pigmented** — **METPO:1003024**
- **carotenoid biosynthetic process** — **GO:0016117**
- **low intracellular carotenoid abundance/density** — label-only candidate
- **visible colony pigmentation** — label-only candidate
- **oxidative-stress protection / free-radical scavenging** — grounding should be selected only after deciding the exact process represented

### Chemicals and metabolites

- **carotenoid** — **CHEBI:35186**
- **dioxygen** — **CHEBI:33019**
- geranylgeranyl pyrophosphate (GGPP) — label-only pending identifier verification
- 15-cis-phytoene — label-only pending identifier verification
- phytofluene — label-only
- neurosporene — label-only
- 4,4′-diaponeurosporene — label-only
- all-trans-4,4′-diaponeurosporenoic acid — label-only
- staphyloxanthin — label-only pending verified ChEBI/database mapping

### Genes, enzymes, and regulatory modules

- **crtE** / GGPP synthase — label-only
- **crtB** / phytoene synthase — label-only
- **crtI** / phytoene desaturase — label-only
- **crtY** / lycopene cyclase — label-only
- **crtOPQMN operon** / staphyloxanthin biosynthetic cluster — label-only
- **crtM** / dehydrosqualene synthase — label-only
- **crtN** / dehydrosqualene desaturase — label-only
- **sigF** regulatory sigma factor — label-only
- **TspO** negative regulator and **RegA** positive regulator in purple bacteria — label-only; taxon-specific

Gene symbols should not be assigned universal UniProt accessions because proteins and accessions are taxon/strain specific.

### Environmental and assay nodes

- incubation duration
- nutrient availability / low-nutrient medium
- culture-medium composition
- light and UV exposure
- oxygen availability
- incubation temperature
- colony age/cell density
- wavelength-specific pigment measurement, HPLC-DAD, Raman spectroscopy, or extraction assay

## 4. Candidate causal edges

The table below is optimized for graph curation. **Direct** means the cited experiment or review explicitly supports the relation; **inferred** means multiple observations make the edge plausible but it should not yet be treated as universal.

| # | Subject–predicate–object triple | Evidence | Supporting snippet | Curation notes |
|---|---|---|---|---|
| 1 | incubation duration — **increases** → visible yellow/orange pigmentation | Direct; taxon-specific | *M. goodii* forms “off-white to cream colonies in 2–4 days that turn yellow-orange after 10–15 days.” | Strong evidence that cream can be a transient low-color state; curate with *M. goodii* and assay context. (tran2020broughttoyou pages 7-9) |
| 2 | incubation duration — **increases** → *S. capitis* yellow pigmentation | Direct | “Yellow pigmentation seemed to increase over time”; visible on R2A after 24 h and TSA after 72 h. | Supports time-dependent accumulation, not necessarily cream as endpoint. (siems2023identificationofstaphyloxanthin pages 4-6) |
| 3 | culture-medium composition — **modulates** → visible colony pigmentation | Direct | K1/H17 were yellow on R2A/TSA, but “on CBA…colonies appeared round and white.” | High-value assay edge; phenotype records should include medium. (siems2023identificationofstaphyloxanthin media 0222358e, siems2023identificationofstaphyloxanthin pages 4-6) |
| 4 | low nutrient availability — **may increase** → carotenoid pigmentation | Suggestive; taxon-specific | Authors state stronger pigmentation on lower-nutrient R2A “might indicate” a response to nutrient-depletion stress. | Preserve “may”; association was not established by a controlled nutrient titration. (siems2023identificationofstaphyloxanthin pages 1-2, siems2023identificationofstaphyloxanthin pages 4-6) |
| 5 | intracellular pigment concentration — **determines detectability of** → visible pigmentation | Direct, broad | “Whether the pigment is visible by the naked eye…depends on its concentration within an organism.” | Strong conceptual edge, although the cited review concerns NTM. (tran2020broughttoyou pages 7-9) |
| 6 | low carotenoid abundance — **contributes to** → cream pigmentation | **Inferred/uncertain** | Cream precedes yellow-orange in *M. goodii*; visibility depends on concentration. | Candidate bridge for the existing seven-node graph, but not directly demonstrated by paired carotenoid quantification of cream versus mature colonies. Do not encode as universal or necessary. (tran2020broughttoyou pages 7-9) |
| 7 | CrtE — **produces** → GGPP | Direct biochemical review | “The reaction catalysed by CrtE provides geranylgeranyl pyrophosphate (GGPP).” | Core upstream carotenoid edge; cross-taxon applicability should be checked. (sandmann2023genesandpathway pages 5-6) |
| 8 | CrtB — **converts two GGPP molecules to** → 15-cis-phytoene | Direct biochemical review | CrtB “converts two molecules of GGPP to 15-cis phytoene.” | Core pathway edge. (sandmann2023genesandpathway pages 5-6) |
| 9 | CrtI — **desaturates** → phytoene to phytofluene/neurosporene | Direct mutant plus in-vitro evidence | “crtI-deficient mutants…accumulated phytoene”; one enzyme catalyzed the three-step sequence to neurosporene. | Strong in purple-bacterial pathway; product count differs among CrtI orthologs. (sandmann2023genesandpathway pages 3-5) |
| 10 | crtB transfer/expression — **causes** → yellow colony pigmentation | Direct genetic transfer | Transfer of *M. marinum crtB* into nonchromogenic *M. smegmatis* produced yellow colonies. | Strong gene-to-color causality, but endpoint is yellow rather than cream. (tran2020broughttoyou pages 7-9) |
| 11 | light/UV exposure — **induces** → mycobacterial carotenoid pigmentation | Direct; historical experiments summarized in review | Dark-grown cultures were colorless, whereas sunlight/UV produced deep orange; full color followed 15 min sunlight, 30 min ambient light, or 1 min UV. | Photochromogenic mycobacteria only; prolonged exposure was lethal. (tran2020broughttoyou pages 7-9) |
| 12 | oxygen — **up-regulates** → crtI–crtB transcription/carotenoid biosynthesis | Direct; purple bacteria | “crtI-crtB operon is transcriptionally up-regulated by oxygen.” | Taxon-specific regulatory edge; oxygen effects may differ elsewhere. (sandmann2023genesandpathway pages 3-5) |
| 13 | multiple/high carotenoid signals — **associate with** → yellow *S. capitis* colonies | Direct chemical/spectroscopic comparison | Pigmented K1/H17 had several peaks and Raman bands at 1160 and 1525 cm⁻¹; these were absent/weak in D2T/D3. | Strong phenotype–chemistry association; contrast is predominantly yellow versus white. (siems2023identificationofstaphyloxanthin pages 4-6) |
| 14 | crtOPQMN operon presence — **enables** → staphyloxanthin biosynthetic potential | Direct genomic annotation | All four strains possessed the five-gene operon. | Necessary-potential edge only: operon presence did **not** predict pigmentation, because non-pigmented strains also carried it. (siems2023identificationofstaphyloxanthin pages 4-6) |
| 15 | carotenoid abundance — **decreases** → UV sensitivity | Direct association across mycobacteria | “The higher the concentration of carotene present, the less sensitive the mycobacterium to UV exposure.” | Functional downstream edge; not a defining edge for cream. (tran2020broughttoyou pages 7-9) |
| 16 | carotenoid-producing state — **increases** → long-term −20°C survival | Direct association; *S. capitis* | Pigmented strains had significantly higher survival after 44 days at −20°C. | No knockout/isogenic comparison; strain background may confound causality. (siems2023identificationofstaphyloxanthin pages 1-2, siems2023identificationofstaphyloxanthin pages 4-6) |

The candidate graph and evidence cautions are summarized here:

| graph layer | candidate node/edge | grounding | evidence strength | key caveat |
|---|---|---|---|---|
| trait | cream pigmented colony/cell coloration | METPO:1003024 | Reviewed trait; direct phenotype examples include "off-white to cream colonies" early in incubation and colonies shifting "from cream with a yellowish tinge to yellow" (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 3-4) | Assay-observed morphology only; not a unique mechanism |
| boundary | cream phenotype distinct from white/colorless and from yellow/orange mature pigmentation | label-only | Direct: unpigmented strains remained white/colorless, while pigmented strains became visibly yellow with time/media effects (siems2023identificationofstaphyloxanthin pages 4-6, tran2020broughttoyou pages 7-9) | Boundary is culture-condition and time dependent |
| environment | increased incubation time -> cream/low-color state can progress to yellow/orange pigmentation | label-only | Direct: *M. goodii* produced "off-white to cream colonies in 2–4 days" that "turn yellow-orange after 10–15 days"; *S. capitis* yellow pigmentation increased over time (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 4-6) | Taxon-specific; supports transient cream state, not all cream phenotypes |
| environment | low-nutrient medium/stress -> stronger visible carotenoid pigmentation | label-only | Direct in *S. capitis*: pigmentation visible earlier/on R2A and authors note possible response to nutrient depletion stress (siems2023identificationofstaphyloxanthin pages 1-2, siems2023identificationofstaphyloxanthin pages 4-6, siems2023identificationofstaphyloxanthin media 0222358e) | Evidence is species-specific and supports yellow intensification more than cream per se |
| environment | light exposure -> increased carotenoid pigmentation | label-only | Direct in mycobacteria: dark-grown cultures colorless, light/UV exposure produced orange pigment; 24/185 isolates (13%) produced pigment when exposed to light (tran2020broughttoyou pages 7-9) | Mycobacterial evidence; not direct for cream phenotype |
| environment | oxygen -> up-regulates carotenoid biosynthesis genes/process | CHEBI:33019 | Direct in purple bacteria: "crtI-crtB operon is transcriptionally up-regulated by oxygen" and carotenoid biosynthesis is up-regulated under aerobic conditions (sandmann2023genesandpathway pages 3-5) | Regulatory evidence from purple bacteria, not direct colony-cream evidence |
| process | carotenoid biosynthetic process | GO:0016117 | Strong direct pathway review evidence across bacteria (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5) | Broad process node; specific branch to cream remains indirect |
| chemical class | carotenoids | CHEBI:35186 | Direct: visibility depends on pigment concentration; carotenoids are major pigments in NTM and detected in pigmented *S. capitis* extracts (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 4-6) | Different carotenoids yield different hues |
| pathway edge | carotenoid abundance/concentration -> visible colony pigmentation | CHEBI:35186 | Direct: "Whether the pigment is visible by the naked eye ... depends on its concentration within an organism"; pigmented strains had several carotenoid peaks while unpigmented strains had only one minor/indistinct peak (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 4-6) | Supports abundance-intensity relation, not a universal cream threshold |
| pathway edge | low carotenoid abundance/density -> cream phenotype | label-only | Moderate/inferred: early cream states precede stronger yellow/orange pigmentation, and visible pigmentation depends on concentration (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 3-4) | Plausible bridge for TraitMech, but not directly demonstrated as universal across taxa |
| genes | crtOPQMN operon present in staphyloxanthin pathway | label-only | Direct in *S. capitis*: all four strains possessed crtOPQMN; pathway identified as staphyloxanthin biosynthesis cluster (siems2023identificationofstaphyloxanthin pages 4-6) | Presence alone did not explain pigmentation differences |
| genes | crtB, crtE, crtI, crtY carotenoid genes | label-only | Direct review evidence in mycobacteria and purple bacteria (tran2020broughttoyou pages 7-9, sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5) | Cross-taxon pathway core; not all taxa use the same end products |
| gene-to-phenotype edge | crtB transfer -> yellow colonies in nonchromogenic host | label-only | Direct: transfer of *M. marinum* crtB into nonchromogenic *M. smegmatis* produced yellow colonies (tran2020broughttoyou pages 7-9) | Supports causality for pigmentation, but endpoint is yellow not cream |
| enzyme step | CrtE -> geranylgeranyl pyrophosphate (GGPP) synthesis | label-only | Direct review evidence: "The reaction catalysed by CrtE provides geranylgeranyl pyrophosphate (GGPP)" (sandmann2023genesandpathway pages 5-6) | Exact identifier not verified here |
| enzyme step | GGPP -> phytoene via CrtB phytoene synthase | label-only | Direct review evidence: phytoene is "the first compound in the specific carotenoid pathway, which is catalysed by CrtB" (sandmann2023genesandpathway pages 5-6) | Exact identifier not verified here |
| enzyme step | phytoene -> desaturated carotenoids via CrtI phytoene desaturase | label-only | Direct review evidence: crtI-deficient mutants accumulated phytoene; CrtI catalyzes sequential desaturation from phytoene via phytofluene to neurosporene (sandmann2023genesandpathway pages 3-5) | Review evidence from purple bacteria |
| product branch | staphyloxanthin precursor all-trans-4,4′-diaponeurosporenoic acid and staphyloxanthin accumulate in pigmented strains | label-only | Direct quantitative evidence: precursor was 37%/31% and staphyloxanthin 26%–30% in pigmented *S. capitis* strains; unpigmented D2T showed only detectable 4,4′-diaponeurosporene (siems2023identificationofstaphyloxanthin pages 4-6) | Strong for *S. capitis*; cream endpoint not isolated as a separate chemical state |
| phenotype comparison | multiple carotenoid peaks -> yellow-pigmented strains; single minor/indistinct peak -> nonpigmented strains | CHEBI:35186 | Direct HPLC/Raman contrast in *S. capitis* (siems2023identificationofstaphyloxanthin pages 4-6, siems2023identificationofstaphyloxanthin pages 3-4) | Contrasts yellow vs nonpigmented more clearly than cream vs yellow |
| application/function | carotenoid pigmentation -> oxidative/UV/cold-stress protection and possible virulence relevance | CHEBI:35186 | Direct/strong but taxon-specific: inverse carotene-UV sensitivity correlation; sigF mutants more sensitive to H2O2; pigmented *S. capitis* had higher long-term survival at −20°C; staphyloxanthin is an anti-virulence target (tran2020broughttoyou pages 7-9, siems2023identificationofstaphyloxanthin pages 1-2, siems2023identificationofstaphyloxanthin pages 4-6) | Functional relevance does not itself define cream phenotype |


*Table: This table summarizes candidate nodes and causal edges for curating METPO:1003024 cream pigmented, emphasizing supported pathway components and assay/environment effects. It also flags the key inference that low carotenoid density may bridge to cream coloration, while noting that this is not yet a universal direct claim.*

## 5. Recent developments and quantitative findings

### 2023 *S. capitis* chemical characterization

Siems and colleagues compared two pigmented and two non-pigmented strains using colony imaging, Raman spectroscopy, HPLC-DAD, and mass spectrometry. In pigmented K1/H17, all-trans-4,4′-diaponeurosporenoic acid accounted for **37% and 31%** of carotenoids, respectively; staphyloxanthin accounted for **26–30%**, and four staphyloxanthin-like compounds each represented **3–18%**. Seven major pigment peaks were observed in pigmented extracts, whereas the non-pigmented reference had only one minor peak corresponding to a compound also present at low abundance in pigmented strains. (siems2023identificationofstaphyloxanthin pages 4-6)

A key mechanistic caution from this study is that all four strains contained the complete annotated **crtOPQMN** cluster. Therefore, pathway-gene presence alone is insufficient to infer either pigmentation or cream coloration; expression, enzyme activity, mutations, regulation, and culture environment must be represented or investigated. (siems2023identificationofstaphyloxanthin pages 4-6)

The same work found that all extracts scavenged radicals: the non-pigmented D2T extract reached approximately **50% DPPH scavenging after 120 min**, while K1 reached approximately **65%**. This undermines a simplistic graph in which carotenoid pigmentation is the sole determinant of antioxidant capacity. (siems2023identificationofstaphyloxanthin pages 4-6)

### 2023 pathway synthesis

Sandmann’s 2023 review consolidated mutant, complementation, expression, and biochemical evidence for carotenoid pathways in purple bacteria. It emphasizes that CrtI product specificity can determine pathway endpoints and that light and oxygen regulate carotenoid synthesis. These findings are useful for defining generic pathway nodes but are not direct evidence that purple-bacterial pathway perturbations produce the METPO cream phenotype. (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5)

### Evidence gap for 2024

Targeted searches identified 2024 work on small-molecule inhibition of staphyloxanthin biosynthesis, including eugenol targeting CrtM, but full-text evidence adequate for quote-level curation was not retrieved. Such papers should be evaluated directly before adding inhibitor → CrtM → reduced pigment → cream/white edges. They are not used here as evidence for a curated triple.

## 6. Applications and real-world relevance

1. **Clinical identification:** colony color remains part of traditional mycobacterial classification and preliminary isolate description, although the Runyon system is now considered outdated and pigmentation can vary with conditions. (tran2020broughttoyou pages 7-9)
2. **Anti-virulence discovery:** staphyloxanthin is investigated as a drug target because pigment pathways can contribute to oxidative-stress resistance and virulence. The 2023 *S. capitis* authors identify the pathway as potentially relevant to anti-virulence design. (siems2023identificationofstaphyloxanthin pages 1-2)
3. **Bioprocess engineering:** bacterial crt genes are used to redirect carotenoid products and engineer cell factories. Replacing phytoene-desaturase activity and increasing precursor supply can alter carotenoid accumulation, illustrating how graph nodes can support strain design. (sandmann2023genesandpathway pages 5-6)
4. **Stress/ecology phenotyping:** pigmentation can mark responses to light, oxygen, nutrient depletion, temperature, and colony age, but color is not a reliable proxy for one stress-resistance mechanism. (tran2020broughttoyou pages 7-9, sandmann2023genesandpathway pages 3-5, siems2023identificationofstaphyloxanthin pages 4-6)

## 7. Recommended minimal TraitMech graph

A conservative graph suitable for initial curation is:

1. **CrtE** → *produces* → **GGPP**  
2. **CrtB** → *produces from GGPP* → **phytoene**  
3. **CrtI/desaturase activity** → *increases conjugation/produces downstream carotenoids* → **colored carotenoid pool**  
4. **carotenoid biosynthetic process (GO:0016117)** → *increases abundance of* → **carotenoid (CHEBI:35186)**  
5. **carotenoid abundance** → *increases detectability/intensity of* → **visible pigmentation**  
6. **low carotenoid abundance** → *may contribute to* → **METPO:1003024**  
7. **incubation time, medium, light, and oxygen** → *modulate* → **carotenoid biosynthesis/pigmentation**

Edges 1–5 are well supported at the pathway or pigment-detectability level. Edge 6 must remain **uncertain/inferred**, and edge 7 should be decomposed into taxon- and assay-specific relations rather than asserted universally.

## 8. Warnings: claims not yet ready for TraitMech curation

- **Do not curate “cream pigmentation is caused by low-density carotenoids” as universal.** Existing evidence supports plausibility but not necessity or sufficiency.
- **Do not infer pigmentation from crt gene-cluster presence alone.** Pigmented and non-pigmented *S. capitis* strains all carried crtOPQMN. (siems2023identificationofstaphyloxanthin pages 4-6)
- **Do not treat cream, white, non-pigmented, buff, tan, and pale yellow as exact synonyms.** Preserve source wording and assay metadata.
- **Do not transfer purple-bacterial CrtI pathway endpoints to staphylococci or mycobacteria without orthology and reaction validation.** Crt enzymes differ in substrate/product specificity. (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5)
- **Do not assert CrtM/CrtN inhibition produces cream colonies from the evidence retrieved here.** This is mechanistically plausible for staphyloxanthin-producing staphylococci, but quote-level phenotype evidence was unavailable.
- **Do not curate carotenoid pigmentation as the sole cause of antioxidant activity.** Non-pigmented *S. capitis* extracts retained substantial DPPH-scavenging activity. (siems2023identificationofstaphyloxanthin pages 4-6)
- **Do not assert medium-independent phenotype status.** Colony photographs and chemical measurements demonstrate pronounced medium and time dependence. (siems2023identificationofstaphyloxanthin media 0222358e, siems2023identificationofstaphyloxanthin pages 4-6)

## DOI-first bibliography

1. **Siems K, et al.** “Identification of staphyloxanthin and derivates in yellow-pigmented *Staphylococcus capitis* subsp. *capitis*.” *Frontiers in Microbiology* 14 (published **29 September 2023**). DOI: **10.3389/fmicb.2023.1272734**. https://doi.org/10.3389/fmicb.2023.1272734 (siems2023identificationofstaphyloxanthin pages 1-2)
2. **Sandmann G.** “Genes and Pathway Reactions Related to Carotenoid Biosynthesis in Purple Bacteria.” *Biology* 12:1346 (published **October 2023**). DOI: **10.3390/biology12101346**. https://doi.org/10.3390/biology12101346 (sandmann2023genesandpathway pages 5-6, sandmann2023genesandpathway pages 3-5)
3. **Tran T, Dawrs SN, Norton GJ, Virdi R, Honda JR.** “Brought to you courtesy of the red, white, and blue—pigments of nontuberculous mycobacteria.” *AIMS Microbiology* 6:434–450 (published **November 2020**). DOI: **10.3934/microbiol.2020026**. https://doi.org/10.3934/microbiol.2020026 (tran2020broughttoyou pages 7-9)
4. **Existing supplied evidence:** “Bacterial Carotenoids: From Genes to Applications.” *Annual Review of Microbiology* 62 (2008). DOI: **10.1146/annurev.micro.62.081307.162844**. https://doi.org/10.1146/annurev.micro.62.081307.162844. This foundational review is appropriate as background, but the cream-specific causal bridge should rely on phenotype-linked evidence rather than the review alone.

References

1. (tran2020broughttoyou pages 7-9): Tru Tran, Stephanie N. Dawrs, Grant J. Norton, Ravleen Virdi, and Jennifer R. Honda. Brought to you courtesy of the red, white, and blue–pigments of nontuberculous mycobacteria. AIMS Microbiology, 6:434-450, Nov 2020. URL: https://doi.org/10.3934/microbiol.2020026, doi:10.3934/microbiol.2020026. This article has 17 citations and is from a peer-reviewed journal.

2. (siems2023identificationofstaphyloxanthin pages 3-4): Katharina Siems, Katharina Runzheimer, Katarina Rebrosova, Lara Etzbach, Alina Auerhammer, Anna Rehm, Oliver Schwengers, Martin Šiler, Ota Samek, Filip Růžička, and Ralf Moeller. Identification of staphyloxanthin and derivates in yellow-pigmented staphylococcus capitis subsp. capitis. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1272734, doi:10.3389/fmicb.2023.1272734. This article has 11 citations and is from a peer-reviewed journal.

3. (siems2023identificationofstaphyloxanthin pages 4-6): Katharina Siems, Katharina Runzheimer, Katarina Rebrosova, Lara Etzbach, Alina Auerhammer, Anna Rehm, Oliver Schwengers, Martin Šiler, Ota Samek, Filip Růžička, and Ralf Moeller. Identification of staphyloxanthin and derivates in yellow-pigmented staphylococcus capitis subsp. capitis. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1272734, doi:10.3389/fmicb.2023.1272734. This article has 11 citations and is from a peer-reviewed journal.

4. (siems2023identificationofstaphyloxanthin media 0222358e): Katharina Siems, Katharina Runzheimer, Katarina Rebrosova, Lara Etzbach, Alina Auerhammer, Anna Rehm, Oliver Schwengers, Martin Šiler, Ota Samek, Filip Růžička, and Ralf Moeller. Identification of staphyloxanthin and derivates in yellow-pigmented staphylococcus capitis subsp. capitis. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1272734, doi:10.3389/fmicb.2023.1272734. This article has 11 citations and is from a peer-reviewed journal.

5. (sandmann2023genesandpathway pages 5-6): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 17 citations.

6. (sandmann2023genesandpathway pages 3-5): Gerhard Sandmann. Genes and pathway reactions related to carotenoid biosynthesis in purple bacteria. Biology, 12:1346, Oct 2023. URL: https://doi.org/10.3390/biology12101346, doi:10.3390/biology12101346. This article has 17 citations.

7. (siems2023identificationofstaphyloxanthin pages 1-2): Katharina Siems, Katharina Runzheimer, Katarina Rebrosova, Lara Etzbach, Alina Auerhammer, Anna Rehm, Oliver Schwengers, Martin Šiler, Ota Samek, Filip Růžička, and Ralf Moeller. Identification of staphyloxanthin and derivates in yellow-pigmented staphylococcus capitis subsp. capitis. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1272734, doi:10.3389/fmicb.2023.1272734. This article has 11 citations and is from a peer-reviewed journal.