---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:02:26.883700'
end_time: '2026-06-17T23:15:18.263966'
duration_seconds: 771.38
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta low
  trait_identifier: METPO:1000479
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl delta phenotype with a narrow growth-supporting NaCl breadth
    of at most approximately 1% (w/v), characteristic of stenohaline organisms.
  parent_traits: METPO:1000335
  synonyms: Nad_<=1
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports narrow salinity-tolerance breadths as the stenohaline phenotype, contrasted
    with euryhaline organisms.)'
  causal_graph_summary: 'nacl_delta_low_stenohaline: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta low
- **METPO identifier:** METPO:1000479
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a narrow growth-supporting NaCl breadth of at most approximately 1% (w/v), characteristic of stenohaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports narrow salinity-tolerance breadths as the stenohaline phenotype, contrasted with euryhaline organisms.)
- **Existing causal graph summary:** nacl_delta_low_stenohaline: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_low.yaml`.

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
- **Trait label:** NaCl delta low
- **METPO identifier:** METPO:1000479
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a narrow growth-supporting NaCl breadth of at most approximately 1% (w/v), characteristic of stenohaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports narrow salinity-tolerance breadths as the stenohaline phenotype, contrasted with euryhaline organisms.)
- **Existing causal graph summary:** nacl_delta_low_stenohaline: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_low.yaml`.

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


## Curation-Focused Research Report: Microbial Trait “NaCl delta low” (METPO:1000479)

### 0. Scope summary (curation-ready)
**Trait label:** NaCl delta low (METPO:1000479) 
**Definition (METPO-aligned interpretation):** a **NaCl delta phenotype** with a **narrow growth-supporting NaCl breadth** (ΔNaCl) of **≤ ~1% (w/v)**, consistent with a **stenohaline** microbial lifestyle (growth only across a small NaCl interval). The operational interpretation for curation is: 
- **ΔNaCl = (highest NaCl % w/v supporting growth) – (lowest NaCl % w/v supporting growth)** under a specified assay. 
- “Low” indicates ΔNaCl ≤ ~1% (w/v); this must be tied to an explicit growth assay and medium. 

**Direct microbial exemplar:** A freshwater cyanobacterium (*Geminocystis urbisnovae*) was explicitly labeled **“Freshwater, stenohaline”** and showed **growth inhibition at ≥0.3% NaCl** in a modified BG-11 medium, demonstrating a **very narrow tolerated NaCl window** consistent with NaCl delta low. (polyakova2023geminocystisurbisnovaesp. pages 9-11, polyakova2023geminocystisurbisnovaesp. pages 8-9)

**Boundary cases / distinctions for curation:**
1. **Assay dependence:** NaCl tolerance breadth can differ substantially by medium. *Vibrio parahaemolyticus* survived up to **9% NaCl in LB**, but **could not grow at 9% NaCl in M9** (minimal medium), implying that “NaCl delta low” should not be assigned without recording medium/conditions. (zhang2023transcriptomeanalysisreveals pages 2-4)
2. **Not equivalent to halophily/halotolerance:** Organisms may have broad ranges (euryhaline-like) via robust osmoadaptation systems, while stenohaline organisms lack/underutilize those systems or are maladapted outside a narrow niche. Engineered and natural halophiles illustrate mechanisms that broaden tolerance, serving as mechanistic contrasts. (zou2024metabolicengineeringof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2)

---

### 1. Key concepts and definitions (current understanding)

#### 1.1 What “NaCl delta” captures
“NaCl delta” describes **tolerance breadth** rather than the optimum: an organism can have a low-salt optimum but still a wide NaCl breadth, or vice versa. In curated graphs, NaCl delta low should be treated as **a phenotype constrained by limited osmoadaptation capacity and/or specialization to a narrow salinity niche**, and should be tied to:
- medium composition (rich vs minimal; baseline salt content), 
- temperature/pH, 
- growth endpoint (growth rate, final OD, colony formation), 
- exposure mode (step change vs acclimated growth).
Medium dependence is empirically demonstrated by *V. parahaemolyticus* where NaCl tolerance differs between LB and M9. (zhang2023transcriptomeanalysisreveals pages 2-4)

#### 1.2 Stenohaline vs euryhaline framing (microbial operationalization)
A “stenohaline” microbe is one that supports growth only across a narrow salinity interval. *G. urbisnovae* provides an explicit microbial usage of “stenohaline” linked to inhibition by small NaCl additions (≥0.3% NaCl), supporting the mapping of NaCl delta low to stenohaline behavior in microbial systems. (polyakova2023geminocystisurbisnovaesp. pages 9-11)

---

### 2. Recent developments and latest research (prioritizing 2023–2024)
Recent work has strengthened **mechanistic interpretability** of salinity breadth by providing **causal tests** (knockout/rescue/engineering) and **systems-level profiling** across salinity steps.

#### 2.1 Causal tests: compatible-solute pathways can widen or narrow NaCl breadth (2024)
In *Halomonas elongata*, deletion of **ectoine biosynthesis (ΔectABC)** produces a salt-sensitive phenotype with **growth only up to ~3–4% NaCl** depending on context, demonstrating that loss of a major compatible-solute system can dramatically **narrow high-salt tolerance breadth** (a mechanistic route toward NaCl delta low–like behavior at the high-salt end). (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2)

Two independent rescue strategies causally increased tolerance:
- **Proline as substitute osmolyte:** engineering proline biosynthesis and blocking proline catabolism enabled an ectoine-deficient strain to **thrive at 8% NaCl**. (khanh2024metabolicpathwayengineering pages 1-2)
- **GABA as substitute osmolyte & pH buffering:** converting glutamate to GABA improved pH homeostasis and enabled higher tolerance, with reported intracellular **GABA 176.94 µmol/g CDW at 7% NaCl** in the engineered strain. (zou2024metabolicengineeringof pages 1-2)

These experiments are highly informative because they connect **specific pathways → osmolyte accumulation → measurable tolerance range**.

#### 2.2 Multi-omics across salinity steps identifies salinity-responsive transport and proteome remodeling (2024)
For the extreme halophile *Natranaerobius thermophilus*, iTRAQ proteomics across **2.5, 3.1, 3.7, 4.3 M Na+** found **658 significantly regulated proteins** (criteria fold change ≥1.5 or ≤0.67; P<0.05), with functional enrichments in **membrane transport**, **energy metabolism**, and **amino acid metabolism**. (xing2024thepolyextremophilenatranaerobius pages 7-10)

Quantitative proteome adaptation included an **acidic proteome shift**: acidic proteins increased from **81.82% to 88.71%**, while median pI decreased **5.20 → 4.95** as salinity increased, consistent with specialization to high-salt environments. (xing2024thepolyextremophilenatranaerobius pages 4-6)

Transport and ion-handling systems associated with salinity response include **compatible-solute ABC transporters (Opu/ProU)**, **K+ uptake (TrkH)**, and **Na+/H+ antiporters (NhaC)**. These appear in a table of fold changes across salinity steps (Table 2). (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius media d8e7b8b7, xing2024thepolyextremophilenatranaerobius media aeb3cc5d, xing2024thepolyextremophilenatranaerobius media d3cac98a, xing2024thepolyextremophilenatranaerobius media 85033f2b)

#### 2.3 Low-salinity response is not merely “less stress” (2023)
Transcriptomics in *V. parahaemolyticus* comparing **0.5% vs 3% NaCl** found **658 differentially expressed genes** (278 up, 380 down), including **outer membrane proteins**, **sodium-dependent transporters**, and **compatible solute synthesis/transport systems**. Low NaCl induced a distinct physiological state including **T3SS1 induction** and **T6SS1 repression**. (zhang2023transcriptomeanalysisreveals pages 2-4)

---

### 3. Current applications and real-world implementations

#### 3.1 Industrial/biotech: osmolyte production and stress-tolerance engineering
Compatible solutes are directly exploited in microbial engineering and bioprocessing as:
- **targets for production** (ectoine, proline, GABA),
- **traits to stabilize industrial strains** under saline/waste-stream conditions.

Recent primary studies demonstrate this in practice:
- *H. elongata* engineered to overproduce **proline** (a feed additive) as the major osmolyte enabling growth at **8% NaCl** in an ectoine-deficient background, supporting use as a “cell factory” under high-salt conditions. (khanh2024metabolicpathwayengineering pages 1-2)
- *H. elongata* engineered for **GABA accumulation** improves salt tolerance; measured **176.94 µmol/g CDW at 7% NaCl** provides a concrete performance metric. (zou2024metabolicengineeringof pages 1-2)

#### 3.2 Environmental and ecological interpretation
For TraitMech curation, NaCl delta low is practically useful for predicting:
- restriction to low-salinity habitats (freshwater specialists),
- sensitivity to salinization,
- failure to persist across fluctuating salinity regimes.
A direct example is the freshwater cyanobacterium *G. urbisnovae* with growth inhibited at **≥0.3% NaCl**, implying high vulnerability to modest salinization in its growth medium context. (polyakova2023geminocystisurbisnovaesp. pages 9-11)

---

### 4. Expert opinions / analysis (authoritative sources)

1. **Compatible-solute systems are central determinants of tolerance breadth.** In *V. parahaemolyticus*, authors emphasize osmotic adaptive responses including compatible-solute synthesis/transport and sodium-dependent transporters as salient under salinity changes. (zhang2023transcriptomeanalysisreveals pages 2-4)
2. **Regulation matters, not only pathway presence.** In *V. parahaemolyticus*, ectoine biosynthesis is described as energetically costly and under tight regulation; regulators (LeuO, NhaR, H-NS) affect expression and mutants show growth defects at **6% NaCl**, tying regulatory architecture to high-salt fitness. (lichty2023nharleuoand pages 1-2)
3. **Specialization can trade off breadth.** In *N. thermophilus*, increasing proteome acidity with salinity (lower pI; higher acidic protein proportion) is consistent with the broader notion that high-salt specialization can reduce performance outside that niche (i.e., narrow breadth on the low-salt side), though the direct low-salt failure mechanism is not experimentally established in these excerpts. (xing2024thepolyextremophilenatranaerobius pages 4-6)

---

### 5. Relevant statistics and quantitative data (from recent studies)
- **Direct stenohaline inhibition:** *G. urbisnovae* growth inhibited at **≥0.3% NaCl** in modified BG-11. (polyakova2023geminocystisurbisnovaesp. pages 9-11)
- **Assay dependence:** *V. parahaemolyticus* survives up to **9% NaCl in LB**, but **fails at 9% NaCl in M9**. (zhang2023transcriptomeanalysisreveals pages 2-4)
- **Transcriptomics:** 0.5% vs 3% NaCl in *V. parahaemolyticus* yields **658 DEGs** (278 up, 380 down). (zhang2023transcriptomeanalysisreveals pages 2-4)
- **Proteomics:** in *N. thermophilus*, **658 proteins** significantly regulated across elevated salinities vs 2.5 M Na+; 1,489 proteins identified (~52.3% of predicted genes). (xing2024thepolyextremophilenatranaerobius pages 7-10)
- **Proteome acidity shift:** acidic proteins **81.82% → 88.71%**; median pI **5.20 → 4.95** with increasing salinity. (xing2024thepolyextremophilenatranaerobius pages 4-6)
- **Engineered osmolyte accumulation:** **GABA 176.94 µmol/g CDW** at 7% NaCl in engineered *H. elongata*. (zou2024metabolicengineeringof pages 1-2)
- **Tolerance-range rescue:** ectoine-deficient *H. elongata* cannot grow above **~4% NaCl** but engineered strain thrives at **8% NaCl**. (khanh2024metabolicpathwayengineering pages 1-2)

---

## 6. Candidate causal-graph entities (nodes)
The following node inventory is proposed for curation into `data/traits/environment/nacl_delta_low.yaml`.

| Node type | Node label | Suggested ontology grounding | Notes on relevance to narrow NaCl breadth (≤~1% w/v) and/or evidence source |
|---|---|---|---|
| Trait/phenotype | NaCl delta low | METPO:1000479 | Target trait: narrow growth-supporting NaCl breadth, interpreted as stenohaline behavior; existing METPO definition and reviewed mapping status. |
| Trait/phenotype | stenohaline organism | label-only | Conceptual parent phenotype for organisms with narrow salinity tolerance breadth; directly exemplified by freshwater cyanobacterium with growth inhibition at ≥0.3% NaCl (Polyakova 2023, 10.4490/algae.2023.38.6.12) (polyakova2023geminocystisurbisnovaesp. pages 9-11, polyakova2023geminocystisurbisnovaesp. pages 8-9) |
| Trait/phenotype | euryhaline organism | label-only | Boundary contrast trait: broad salinity range; useful negative comparator when deciding whether NaCl breadth is truly low. Mentioned in osmoadaptation literature context and broad-range halophiles in 2024 studies (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| Environmental/exposure factors | sodium chloride | CHEBI:26710 | Primary environmental variable defining the phenotype; small NaCl increases can inhibit stenohaline strains, whereas broad-range taxa tolerate much larger changes (polyakova2023geminocystisurbisnovaesp. pages 9-11, zhang2023transcriptomeanalysisreveals pages 2-4) |
| Environmental/exposure factors | salinity stress | GO:0009651 | General osmotic/salt challenge context driving osmoadaptation mechanisms; useful environmental parent node for causal edges. Supported across 2023–2024 studies (xing2024thepolyextremophilenatranaerobius pages 1-2, zhang2023transcriptomeanalysisreveals pages 2-4) |
| Environmental/exposure factors | low salinity environment | ENVO:01001888 | Relevant because some halophiles/proteomes become maladapted at low salt, highlighting breadth limits at the low-salt end as well as the high-salt end (goszcz2025bacterialosmoprotectants—away pages 5-5, zhang2023transcriptomeanalysisreveals pages 2-4) |
| Environmental/exposure factors | freshwater habitat | ENVO:00002011 | Ecological setting strongly associated with stenohaline low-NaCl breadth in Geminocystis urbisnovae; useful environmental preference node (polyakova2023geminocystisurbisnovaesp. pages 9-11, polyakova2023geminocystisurbisnovaesp. pages 8-9) |
| Assay/media factors | modified BG-11 medium | label-only | Assay context for cyanobacterial stenohaline call; medium had low total salt and growth was inhibited at ≥0.3% NaCl, so curation should preserve assay context (polyakova2023geminocystisurbisnovaesp. pages 9-11) |
| Assay/media factors | M9 minimal medium | label-only | Medium dependence matters: V. parahaemolyticus failed at 9% NaCl in M9 but survived broader range in LB; illustrates assay-specific salinity breadth measurements (zhang2023transcriptomeanalysisreveals pages 2-4) |
| Assay/media factors | LB medium | label-only | Rich medium can broaden apparent NaCl tolerance relative to minimal medium; important warning node for phenotype assay dependence (zhang2023transcriptomeanalysisreveals pages 2-4) |
| Biological processes | osmoadaptation | GO:0006970 | Central process linking salt exposure to tolerance breadth; absence/weakness of osmoadaptation capacity is a plausible positive cause of NaCl delta low (xing2024thepolyextremophilenatranaerobius pages 1-2, zhang2023transcriptomeanalysisreveals pages 2-4) |
| Biological processes | compatible solute accumulation | GO:0019491 | Major mechanism expanding salinity tolerance breadth; lack or reduced capacity is a plausible contributor to stenohaline phenotypes (xing2024thepolyextremophilenatranaerobius pages 1-2, lichty2023nharleuoand pages 1-2) |
| Biological processes | potassium ion transport | GO:0006813 | Short-term and long-term salt adaptation often requires K+ uptake; limited K+ homeostasis may constrain breadth (lichty2023nharleuoand pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) |
| Biological processes | sodium ion export | GO:0036376 | Na+/H+ antiport and related export functions support tolerance; weaker export capacity may narrow tolerable NaCl range (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) |
| Biological processes | regulation of ectoine biosynthetic process | label-only | Regulatory control over osmolyte synthesis affects high-salt fitness; defects broaden/limit tolerance depending on context (lichty2023nharleuoand pages 1-2) |
| Biological processes | maintenance of intracellular pH | GO:0051453 | Important because acidic osmolytes such as glutamate can impose pH-homeostasis costs, limiting salt tolerance unless converted to GABA (zou2024metabolicengineeringof pages 1-2) |
| Pathways/modules | ectoine biosynthesis | MetaCyc:PWY-7315 | Canonical compatible-solute pathway supporting growth at elevated salinity; loss of ectABC narrows salinity range in Halomonas elongata mutants (zou2024metabolicengineeringof pages 1-2, lichty2023nharleuoand pages 1-2) |
| Pathways/modules | proline biosynthesis | MetaCyc:PROSYN-PWY | Alternative osmolyte pathway; engineered overproduction restored higher salt tolerance in ectoine-deficient H. elongata (khanh2024metabolicpathwayengineering pages 1-2) |
| Pathways/modules | glutamate biosynthesis/accumulation | label-only | Glutamate can partly compensate for ectoine loss, but acidity may constrain further tolerance; relevant as partial, imperfect rescue (zou2024metabolicengineeringof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Pathways/modules | GABA biosynthesis from glutamate | label-only | Engineered conversion of glutamate to GABA improved salt tolerance by helping restore pH homeostasis (zou2024metabolicengineeringof pages 1-2) |
| Pathways/modules | glycine betaine uptake system | label-only | Widely used salt-out module; transporter abundance rises with salinity in broad/high-salt taxa, implying absence may contribute to narrow breadth (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Pathways/modules | salt-in strategy | label-only | Accumulation of K+ and proteome adaptation to salts; specialization can either support high salt or reduce low-salt breadth depending on proteome constraints (goszcz2025bacterialosmoprotectants—away pages 5-5, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Genes/proteins/complexes | ectABC operon | label-only | Ectoine biosynthesis genes; deletion in H. elongata sharply narrows high-salt tolerance, making them strong negative correlates of NaCl delta low when absent (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/proteins/complexes | asp_ect | label-only | Part of ectoine biosynthesis locus/regulatory region discussed in Vibrio; useful if curation captures complete operon architecture (lichty2023nharleuoand pages 1-2) |
| Genes/proteins/complexes | LeuO | UniProtKB:label-only | Positive regulator of ectoine expression in V. parahaemolyticus; regulatory insufficiency could reduce osmolyte production capacity (lichty2023nharleuoand pages 1-2) |
| Genes/proteins/complexes | NhaR | UniProtKB:label-only | Negative regulator in ectoine network and linked to nhaA-related salt response; indicates regulatory coupling of ion transport and osmolytes (lichty2023nharleuoand pages 1-2) |
| Genes/proteins/complexes | H-NS | UniProtKB:label-only | Represses ectoine promoter region in part of regulatory network; relevant for conditional expression of salt tolerance machinery (lichty2023nharleuoand pages 1-2) |
| Genes/proteins/complexes | proB | UniProtKB:label-only | Encodes γ-glutamyl kinase; first committed step of proline synthesis and important engineered determinant of restored salt tolerance (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/proteins/complexes | proA | UniProtKB:label-only | Proline biosynthetic enzyme used in engineered osmolyte rescue of H. elongata (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/proteins/complexes | proC | UniProtKB:label-only | Proline biosynthetic enzyme used in engineered osmolyte rescue of H. elongata (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/proteins/complexes | putA | UniProtKB:label-only | Proline catabolism enzyme; deletion helps proline accumulation and improved salt tolerance, so presence/activity may reduce osmolyte retention (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/proteins/complexes | gadB | UniProtKB:label-only | Glutamate decarboxylase; engineered activity increased GABA accumulation and salt tolerance in an ectoine-deficient background (zou2024metabolicengineeringof pages 1-2) |
| Genes/proteins/complexes | gudB | UniProtKB:label-only | Glutamate dehydrogenase upregulated with increasing salinity in N. thermophilus, supporting amino-acid osmolyte adaptation (xing2024thepolyextremophilenatranaerobius pages 4-6) |
| Genes/proteins/complexes | Na+-translocating FOF1-ATPase | GO:0046933 | Genome/proteome candidate for ion homeostasis under high salinity; relevant comparator for broad/high-salt phenotypes rather than direct stenohaline marker (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Transporters | OpuA/OpuAC glycine betaine ABC transporter | label-only | Multiple OpuA-family proteins increase under higher salinity in N. thermophilus; osmolyte uptake capacity likely expands NaCl breadth (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) |
| Transporters | ProU (ProX/ProV/ProW) glycine betaine/L-proline ABC transporter | label-only | Classic osmoprotectant uptake system; increased abundance with salinity in N. thermophilus and down/up regulation under salt shifts in Vibrio (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 1-2, zhang2023transcriptomeanalysisreveals pages 2-4) |
| Transporters | BetT | UniProtKB:label-only | Glycine betaine/choline transporter candidate in N. thermophilus table; uptake capacity is relevant to salinity breadth (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 4-6) |
| Transporters | BCCT family transporter | label-only | Broad compatible-solute uptake family emphasized as energetically cheaper than de novo synthesis; likely broadens salinity tolerance if available (goszcz2025bacterialosmoprotectants—away pages 1-2) |
| Transporters | TrkH potassium uptake transporter | UniProtKB:label-only | K+ uptake component upregulated with salinity in N. thermophilus; important short-term osmotic balancing determinant (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) |
| Transporters | NhaC Na+/H+ antiporter | UniProtKB:label-only | Antiporter family strongly induced at higher salinity in N. thermophilus table; failure/absence could narrow NaCl tolerance breadth (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) |
| Transporters | sodium-dependent transporters | label-only | Differentially expressed under low-salt vs moderate-salt conditions in V. parahaemolyticus; generic assay-supported node if exact transporter identity is unresolved (zhang2023transcriptomeanalysisreveals pages 2-4) |
| Metabolites/chemicals | ectoine | CHEBI:27689 | Major compatible solute whose biosynthesis supports salt tolerance; loss narrows growth range, rescue by alternative osmolytes demonstrates causal relevance (zou2024metabolicengineeringof pages 1-2, lichty2023nharleuoand pages 1-2) |
| Metabolites/chemicals | glycine betaine | CHEBI:17750 | High-value compatible solute accumulated/imported under salt stress; uptake/synthesis capacity expands tolerance breadth (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 6-7) |
| Metabolites/chemicals | L-proline | CHEBI:17203 | Osmolyte used in engineered rescue of ectoine-deficient H. elongata, enabling growth at 8% NaCl (khanh2024metabolicpathwayengineering pages 1-2) |
| Metabolites/chemicals | L-glutamate | CHEBI:29985 | Osmolyte/intermediate that can partially restore tolerance, but excessive accumulation may impair pH homeostasis and limit breadth (zou2024metabolicengineeringof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Metabolites/chemicals | GABA | CHEBI:16865 | Alternative osmolyte whose accumulation improved salt tolerance in engineered H. elongata (zou2024metabolicengineeringof pages 1-2) |
| Metabolites/chemicals | potassium ion | CHEBI:29103 | Key intracellular counterion in salt-in or hybrid responses; important mechanistic comparator for taxa with broader/high-salt tolerance (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 23-24) |
| Metabolites/chemicals | sodium ion | CHEBI:29101 | Toxic/osmotic challenge ion whose extracellular increase triggers transport, osmolyte, and proteome responses (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) |


*Table: This table lists candidate causal-graph nodes for curating the microbial trait NaCl delta low (stenohaline). It groups phenotype, environmental, mechanistic, and molecular entities that are relevant to narrow NaCl growth breadth and ties them to available evidence contexts.*

---

## 7. Evidence-backed candidate causal edges (triples)
Edges below are phrased as **subject–predicate–object** triples suitable for TraitMech. Edges include assay- and taxon-dependence notes.

| Edge (S–P–O) | Edge type | Evidence snippet | Citation IDs | Notes/uncertainty for curation |
|---|---|---|---|---|
| Increased NaCl in modified BG-11 medium → inhibits growth of *Geminocystis urbisnovae* → stenohaline freshwater phenotype | assay/ecological | Authors describe the species as “Freshwater, stenohaline,” with growth inhibited at NaCl additions ≥0.3% in modified BG-11 medium. | (polyakova2023geminocystisurbisnovaesp. pages 9-11, polyakova2023geminocystisurbisnovaesp. pages 8-9) | Strong for this taxon and assay; useful as direct exemplar of NaCl delta low, but threshold is medium-specific and taxon-specific. |
| Freshwater habitat association → selects/reflects narrow salinity breadth → stenohaline phenotype | ecological | *G. urbisnovae* was isolated from freshwater habitats and authors justify the “stenohaline” label together with low-NaCl growth inhibition. | (polyakova2023geminocystisurbisnovaesp. pages 9-11, polyakova2023geminocystisurbisnovaesp. pages 8-9) | Ecological association, not a universal mechanism; curate as contextual/supporting rather than core mechanistic edge. |
| Loss of ectoine biosynthesis (*ectABC* deletion) → narrows high-salt growth range → salt-sensitive phenotype in *Halomonas elongata* | molecular/mechanistic | Ectoine-deficient mutant KA1 “only grows well in minimal medium containing up to 3% NaCl”; another report states it “could not grow in minimal media containing more than 4% NaCl.” | (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) | Strong causal evidence in one species/background; supports general role of ectoine pathway in broadening NaCl tolerance, but inference to stenohaline natural taxa is indirect. |
| Ectoine biosynthesis capacity → supports salt tolerance breadth → growth at higher NaCl | molecular/mechanistic | Wild-type *H. elongata* synthesizes ectoine as a major osmolyte, whereas ectoine-deficient strains become salt sensitive. | (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2) | Good mechanistic comparator edge; polarity is opposite of NaCl delta low, so useful mainly as “absence/reduction may contribute to narrow breadth.” |
| Engineered proline biosynthesis (*proBm1AC*) plus blocked proline catabolism (*ΔputA*) → increases intracellular proline → restores growth at 8% NaCl | molecular/mechanistic | Engineered strain HN6 “thrived in the medium containing 8% NaCl” whereas ectoine-deficient KA1 could not grow above 4% NaCl. | (khanh2024metabolicpathwayengineering pages 1-2) | Strong rescue evidence in engineered *H. elongata*; taxon- and construct-specific, but highly informative for osmolyte mechanism. |
| Engineered glutamate-to-GABA conversion (*gadB* system) → improves pH homeostasis and GABA accumulation → increases salt tolerance | molecular/mechanistic | GAD-engineered strain showed “higher salt tolerance” and accumulated GABA (176.94 µmol/g cell dry weight at 7% NaCl); authors link this to restored cellular pH homeostasis. | (zou2024metabolicengineeringof pages 1-2) | Strong in engineered background; mechanism depends on mutant context and should be marked as rescue/engineering evidence. |
| Excess glutamate accumulation → interferes with pH homeostasis → limits salt-tolerance breadth | mechanistic | Authors note the glutamate-overproducing strain had lower tolerance than wild type, “possibly because the acidity of Glu interferes with the pH homeostasis of the cell.” | (zou2024metabolicengineeringof pages 1-2) | Mechanistically plausible but somewhat interpretive (“possibly”); curate as uncertain/inferred. |
| Increased salinity → induces Opu/ProU-family compatible-solute transporters → supports osmoadaptation | molecular/mechanistic | In *N. thermophilus*, proteomics showed salinity-linked increases in compatible-solute transporters, e.g., opuAC and proX/proV/proW fold changes above baseline across higher Na+ conditions. | (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) | Strong transporter-response evidence, but from an extreme halophile with broad/high-salt adaptation; opposite comparator to stenohaline low breadth. |
| Increased salinity → induces TrkH potassium uptake system → supports intracellular K+ homeostasis | molecular/mechanistic | Table data list TrkH among salinity-responsive proteins; paper title and summary emphasize simultaneous accumulation of compatible solutes and K+. | (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) | Good mechanistic comparator; evidence is in a haloalkalithermophile, not a stenohaline microbe. |
| Increased salinity → induces NhaC-family Na+/H+ antiporters → supports ion homeostasis under salt stress | molecular/mechanistic | *N. thermophilus* proteomics show strong salinity-linked increases for NhaC-family antiporters (e.g., one entry rising to ~3.27 and 3.22-fold). | (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius media d8e7b8b7) | Strong transporter evidence from one species; useful as a candidate breadth-expanding mechanism whose absence may contribute to NaCl delta low. |
| Increased salinity → increases proportion of acidic proteins / lowers proteome pI → acidic proteome shift | mechanistic | Proteome adaptation data show acidic-protein proportion rose from 81.82% to 88.71%, with median pI decreasing from 5.20 to 4.95 as salinity increased. | (xing2024thepolyextremophilenatranaerobius pages 4-6) | Strong quantitative evidence, but mainly relevant to high-salt specialists; should not be directly asserted for stenohaline taxa without species-specific support. |
| Medium composition (LB vs M9) → changes apparent NaCl tolerance range → assay-dependent breadth measurement | assay | *V. parahaemolyticus* survived 0.5%–9% NaCl in LB, but in M9 “could not grow under 9% NaCl.” | (zhang2023transcriptomeanalysisreveals pages 2-4) | Important curation warning: NaCl breadth is medium dependent; assay conditions must be preserved in TraitMech annotations. |
| Low NaCl (0.5% vs 3%) → changes expression of compatible-solute systems, sodium transporters, and outer-membrane proteins → altered osmotic response | molecular/mechanistic | RNA-seq identified 658 DEGs, including “sodium-dependent transporters, compatible solute synthesis and transport systems,” under low NaCl. | (zhang2023transcriptomeanalysisreveals pages 2-4) | Strong transcriptomic response evidence, but in a moderately halophilic pathogen rather than a stenohaline organism. |
| Low NaCl (0.5%) → increases stationary-phase cell density in M9 → improved fitness at low salinity | assay/mechanistic | In M9, 0.5% NaCl cultures reached higher stationary-phase density than other NaCl conditions. | (zhang2023transcriptomeanalysisreveals pages 2-4) | Species-specific optimum effect; useful for boundary-case comparisons, not direct evidence of NaCl delta low. |
| Low NaCl → induces T3SS1 and T3SS2-associated secretion / represses T6SS1 → salinity-dependent virulence-state shift | molecular | Low NaCl “induce[d] the expression of T3SS1,” with biofilm/T3SS1 genes up and T6SS1 down; secretion of T3SS2 translocon VPA1361 also increased. | (zhang2023transcriptomeanalysisreveals pages 2-4) | Strong salinity-regulated phenotype in *Vibrio*; not a core edge for stenohaline breadth, but a useful downstream-response edge. |
| Regulatory network (LeuO positive, NhaR negative, H-NS context-dependent) → controls ectoine biosynthesis expression → affects growth at high salinity | molecular/mechanistic | In *V. parahaemolyticus*, LeuO positively and NhaR negatively regulate ectoine operon expression; mutants had growth defects in 6% NaCl. | (lichty2023nharleuoand pages 1-2) | Good regulatory evidence for osmolyte-control machinery; taxon-specific and not directly a stenohaline claim. |


*Table: This table compiles candidate subject–predicate–object edges supported by the retrieved literature for curating the NaCl delta low trait and its mechanistic comparators. It includes direct stenohaline evidence, experimentally demonstrated osmolyte rescue mechanisms, transporter and proteome responses to salinity, and key assay-dependence warnings.*

---

## 8. Ontology grounding suggestions (high priority)
- **METPO:** NaCl delta low = METPO:1000479 (given). 
- **CHEBI:** NaCl (CHEBI:26710), ectoine (CHEBI:27689), glycine betaine (CHEBI:17750), proline (CHEBI:17203), glutamate (CHEBI:29985), GABA (CHEBI:16865), Na+ (CHEBI:29101), K+ (CHEBI:29103). (artifact-00)
- **GO:** salinity stress (GO:0009651), potassium ion transport (GO:0006813), sodium ion export (GO:0036376), intracellular pH maintenance (GO:0051453). (artifact-00)
- **ENVO:** freshwater habitat (ENVO:00002011), low salinity environment (ENVO:01001888). (artifact-00)

Where gene/protein IDs are strain-specific (e.g., Nther_####), curate as **label-only** unless a stable UniProt accession is retrieved during a later curation pass.

---

## 9. Warnings / claims not yet ready to curate
1. **Do not generalize high-salt specialist mechanisms as stenohaline causes without species evidence.** Acidic proteome shifts and transporter induction are strongly supported in *N. thermophilus* but represent a high-salt adaptation context; use as mechanistic comparators, not as direct stenohaline determinants. (xing2024thepolyextremophilenatranaerobius pages 4-6, xing2024thepolyextremophilenatranaerobius media d8e7b8b7)
2. **Avoid assigning NaCl delta low from single-medium tests unless assay is explicit.** The LB vs M9 discrepancy in *V. parahaemolyticus* illustrates that medium can broaden or narrow apparent NaCl breadth. Curate assay context nodes/edges. (zhang2023transcriptomeanalysisreveals pages 2-4)
3. **Foundational review not directly quotable in this run:** the osmoadaptation review DOI **10.1093/femsre/fuy009** was identified but full text was unobtainable; any stenohaline/euryhaline definitions from it should be added only after direct text verification. (tool limitation noted in plan; no direct evidence snippet available)

---

## 10. DOI-first bibliography (with URLs and publication dates)

1. **Polyakova E, Averina S, Pinevich A.** *Geminocystis urbisnovae* sp. nov. (Chroococcales, Cyanobacteria): polyphasic description… **Algae**. **June 2023**. DOI: **10.4490/algae.2023.38.6.12**. URL: https://doi.org/10.4490/algae.2023.38.6.12 (polyakova2023geminocystisurbisnovaesp. pages 9-11, polyakova2023geminocystisurbisnovaesp. pages 8-9)

2. **Zhang Y, Tan X, Li M, Liu P, Jiao X, Gu D.** Transcriptome analysis reveals the effect of low NaCl concentration on osmotic stress and type III secretion system in *Vibrio parahaemolyticus*. **Int J Mol Sci**. **Jan 2023**. DOI: **10.3390/ijms24032621**. URL: https://doi.org/10.3390/ijms24032621 (zhang2023transcriptomeanalysisreveals pages 2-4)

3. **Lichty KEB, Gregory GJ, Boyd EF.** NhaR, LeuO, and H-NS are part of an expanded regulatory network for ectoine biosynthesis expression. **Appl Environ Microbiol**. **Jun 2023**. DOI: **10.1128/aem.00479-23**. URL: https://doi.org/10.1128/aem.00479-23 (lichty2023nharleuoand pages 1-2)

4. **Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H.** Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in an ectoine-deficient *Halomonas elongata*. **Appl Environ Microbiol**. **Jan 2024**. DOI: **10.1128/aem.01905-23**. URL: https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 1-2)

5. **Xing Q, Zhang S, Tao X, Mesbah NM, Mao X, Wang H, Wiegel J, Zhao B.** The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy… **Appl Environ Microbiol**. **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 4-6, xing2024thepolyextremophilenatranaerobius pages 7-10, xing2024thepolyextremophilenatranaerobius media d8e7b8b7)

6. **Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H.** Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*. **Appl Environ Microbiol**. **Sep 2024**. DOI: **10.1128/aem.01195-24**. URL: https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)

---

### 11. Notes for TraitMech YAML curation
- Encode NaCl delta low as a **phenotype derived from assay-defined NaCl range** (min, max, delta), not as an intrinsic “salt sensitivity” label without context. 
- Prefer edges that are either: 
  (i) **direct growth inhibition thresholds** (stenohaline exemplar), or 
  (ii) **causal genetic perturbations/rescues** (ectABC deletion; proline/GABA rescue), 
  as these are most defensible for mechanistic graphs. (polyakova2023geminocystisurbisnovaesp. pages 9-11, zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2)


References

1. (polyakova2023geminocystisurbisnovaesp. pages 9-11): Elena Polyakova, Svetlana Averina, and Alexander Pinevich. Geminocystis urbisnovae sp. nov. (chroococcales, cyanobacteria): polyphasic description complemented with a survey of the family geminocystaceae. Algae, 38:93-110, Jun 2023. URL: https://doi.org/10.4490/algae.2023.38.6.12, doi:10.4490/algae.2023.38.6.12. This article has 8 citations and is from a peer-reviewed journal.

2. (polyakova2023geminocystisurbisnovaesp. pages 8-9): Elena Polyakova, Svetlana Averina, and Alexander Pinevich. Geminocystis urbisnovae sp. nov. (chroococcales, cyanobacteria): polyphasic description complemented with a survey of the family geminocystaceae. Algae, 38:93-110, Jun 2023. URL: https://doi.org/10.4490/algae.2023.38.6.12, doi:10.4490/algae.2023.38.6.12. This article has 8 citations and is from a peer-reviewed journal.

3. (zhang2023transcriptomeanalysisreveals pages 2-4): Youkun Zhang, Xiaotong Tan, Mingzhu Li, Peng Liu, Xinan Jiao, and Dan Gu. Transcriptome analysis reveals the effect of low nacl concentration on osmotic stress and type iii secretion system in vibrio parahaemolyticus. International Journal of Molecular Sciences, 24:2621, Jan 2023. URL: https://doi.org/10.3390/ijms24032621, doi:10.3390/ijms24032621. This article has 19 citations.

4. (zou2024metabolicengineeringof pages 1-2): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

5. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

6. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

7. (xing2024thepolyextremophilenatranaerobius pages 7-10): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

8. (xing2024thepolyextremophilenatranaerobius pages 4-6): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

9. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius media d8e7b8b7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius media aeb3cc5d): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

12. (xing2024thepolyextremophilenatranaerobius media d3cac98a): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

13. (xing2024thepolyextremophilenatranaerobius media 85033f2b): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

14. (lichty2023nharleuoand pages 1-2): Katherine E. Boas Lichty, Gwendolyn J. Gregory, and E. Fidelma Boyd. Nhar, leuo, and h-ns are part of an expanded regulatory network for ectoine biosynthesis expression. Applied and Environmental Microbiology, Jun 2023. URL: https://doi.org/10.1128/aem.00479-23, doi:10.1128/aem.00479-23. This article has 10 citations and is from a peer-reviewed journal.

15. (goszcz2025bacterialosmoprotectants—away pages 5-5): Aleksandra Goszcz, Karolina Furtak, Robert Stasiuk, Joanna Wójtowicz, Marcin Musiałowski, Michela Schiavon, and Klaudia Dębiec-Andrzejewska. Bacterial osmoprotectants—a way to survive in saline conditions and potential crop allies. FEMS Microbiology Reviews, May 2025. URL: https://doi.org/10.1093/femsre/fuaf020, doi:10.1093/femsre/fuaf020. This article has 45 citations and is from a domain leading peer-reviewed journal.

16. (goszcz2025bacterialosmoprotectants—away pages 1-2): Aleksandra Goszcz, Karolina Furtak, Robert Stasiuk, Joanna Wójtowicz, Marcin Musiałowski, Michela Schiavon, and Klaudia Dębiec-Andrzejewska. Bacterial osmoprotectants—a way to survive in saline conditions and potential crop allies. FEMS Microbiology Reviews, May 2025. URL: https://doi.org/10.1093/femsre/fuaf020, doi:10.1093/femsre/fuaf020. This article has 45 citations and is from a domain leading peer-reviewed journal.

17. (xing2024thepolyextremophilenatranaerobius pages 23-24): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.