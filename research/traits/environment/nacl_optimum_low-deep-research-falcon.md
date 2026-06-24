---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:14:06.289296'
end_time: '2026-06-17T23:35:56.144409'
duration_seconds: 1309.86
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum low
  trait_identifier: METPO:1000465
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration at
    or below approximately 1% (w/v), corresponding to non-halophilic or halotolerant
    physiology.
  parent_traits: METPO:1000333
  synonyms: Halotolerant, Non-halophile, NaO_<=1
  evidence_summary: 'DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review
    supports low-salt optima as the non-halophilic / halotolerant end of the halophily
    axis.)'
  causal_graph_summary: 'nacl_optimum_low_non_halophile_setpoint: 4 nodes, 3 edges'
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
- **Trait label:** NaCl optimum low
- **METPO identifier:** METPO:1000465
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration at or below approximately 1% (w/v), corresponding to non-halophilic or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Non-halophile, NaO_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports low-salt optima as the non-halophilic / halotolerant end of the halophily axis.)
- **Existing causal graph summary:** nacl_optimum_low_non_halophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_low.yaml`.

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
- **Trait label:** NaCl optimum low
- **METPO identifier:** METPO:1000465
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration at or below approximately 1% (w/v), corresponding to non-halophilic or halotolerant physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Halotolerant, Non-halophile, NaO_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports low-salt optima as the non-halophilic / halotolerant end of the halophily axis.)
- **Existing causal graph summary:** nacl_optimum_low_non_halophile_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_low.yaml`.

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


## Research report: Microbial trait “NaCl optimum low” (METPO:1000465)

### Executive scope summary
The trait **NaCl optimum low** (METPO:1000465) is best interpreted as a *growth optimum phenotype* in which an organism’s maximal growth rate occurs at **≤ ~1% (w/v) NaCl**, aligning with the widely used non‑halophilic threshold of **<0.2 M NaCl (~1% w/v)**. This is distinct from *salt tolerance* (ability to grow at elevated NaCl) and from *slight halophily*, where the optimum is shifted upward (e.g., ~1–5% NaCl). Halotolerant organisms can still map to this trait when their **optimum is low** but they retain the capacity to grow at higher NaCl. (amoozegar2019halophilesandtheir pages 1-2, didari2020diversityofhalophilic pages 1-2, slizewska2025halophilicandhalotolerant pages 1-2)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Non‑halophilic vs halophilic vs halotolerant (thresholds)
* **Non‑halophilic optimum:** “non‑halophilic microorganisms grow optimally at **<0.2 M (1%) NaCl**.” (Amoozegar et al., 2019; DOI:10.3389/fmicb.2019.01895; published Aug 2019; URL https://doi.org/10.3389/fmicb.2019.01895) (amoozegar2019halophilesandtheir pages 1-2)
* **Halophilic vs non‑halophilic demarcation:** organisms are classified as halophilic if they “grow best on media containing **more than 0.2 M** salt” and non‑halophilic if they grow best at “**less than 0.2 M** salt.” (Didari et al., 2020; DOI:10.1007/s40201-020-00519-3; published Aug 2020; URL https://doi.org/10.1007/s40201-020-00519-3) (didari2020diversityofhalophilic pages 1-2)
* **Halotolerant definition:** halotolerant organisms are “those **non‑halophilic** … able to grow at high salt concentrations.” (Didari et al., 2020; DOI:10.1007/s40201-020-00519-3) (didari2020diversityofhalophilic pages 1-2). A similar framing appears for fungi/soil contexts, explicitly tying non‑halophilic optimum to <~1% (0.2 M) and distinguishing halotolerance as growth at higher NaCl. (Śliżewska et al., 2025; DOI:10.3389/fmicb.2025.1637496) (slizewska2025halophilicandhalotolerant pages 1-2)

#### 1.2 What “optimum” means in practice
For curation, **optimum** should be treated as the **peak of a growth‑rate vs NaCl curve** (or equivalent growth yield/biomass proxy), not simply growth at a single NaCl level or “maximum tolerated NaCl.” Mechanistically, even organisms whose optimum is low can carry osmoadaptation modules that allow transient survival/growth in higher salt (halotolerance). (didari2020diversityofhalophilic pages 1-2, amoozegar2019halophilesandtheir pages 1-2)

#### 1.3 Mechanistic framing: “salt‑out” vs “salt‑in” (context)
In high‑salt biology broadly, two strategies recur: **salt‑in** (accumulate inorganic ions, often K+) and **salt‑out** (exclude salt and accumulate organic compatible solutes such as glycine betaine). A review of NaCl‑saturated brines describes these strategies and notes that salt‑out is common in “most halotolerant/philic bacteria.” (Lee et al., 2018; DOI:10.1093/femsre/fuy026; published Jun 2018; URL https://doi.org/10.1093/femsre/fuy026) (lee2018naclsaturatedbrinesare pages 15-17)

### 2) Recent developments and latest research (prioritizing 2023–2024)

#### 2.1 2024: cyclic di‑AMP as a master regulator of osmoadaptation and cell volume
A 2024 **Microbiology and Molecular Biology Reviews** synthesis argues that cyclic di‑AMP (c‑di‑AMP) is a **“master regulator of cell volume”**, coordinating osmoadaptation by controlling K+ and compatible‑solute flux. It integrates evidence that c‑di‑AMP modulates **Trk/Ktr/KUP/Kdp** potassium systems and **OpuA/OpuC** compatible‑solute importers, and that transcriptional regulation can occur via **riboswitches** (e.g., ydaO) upstream of ion/osmolyte transport loci. (Foster et al., 2024; DOI:10.1128/mmbr.00181-23; published Jun 2024; URL https://doi.org/10.1128/mmbr.00181-23) (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 31-33)

A key quantitative argument from this review is that binding sites for c‑di‑AMP can be abundant enough that “the majority of the intracellular cyclic di‑AMP pool may exist in a **protein‑bound** state,” consistent with tight control of transporter activity and cell volume. (Foster et al., 2024; DOI:10.1128/mmbr.00181-23) (foster2024bacterialcellvolume pages 10-12)

**Figure evidence (schematic):** Foster et al. provide a schematic overview of osmolyte influx/efflux systems and highlight which are regulated by c‑di‑AMP, including Trk/Ktr/Kdp/Kup/KimA and OpuA/OpuC. (Foster et al., 2024; Fig. 1B) (foster2024bacterialcellvolume media 7ac30d40)

#### 2.2 2023: structural mechanism—c‑di‑AMP inhibits KUP‑family K+ uptake (KimA)
A 2023 **Nature Communications** study reports that in *Bacillus subtilis* the K+/H+ symporter **KimA** (KUP family) is **inactivated by c‑di‑AMP**. Functional assays showed reduced transporter capacity (Vmax reduction) when c‑di‑AMP is synthesized, and cryo‑EM/MD data indicate c‑di‑AMP binding traps KimA in an inward‑occluded conformation. (Fuss et al., 2023; DOI:10.1038/s41467-023-38944-1; published Jun 2023; URL https://doi.org/10.1038/s41467-023-38944-1) (fuss2023cyclicdiamptraps pages 1-2)

#### 2.3 2024: quantitative physiology and multi‑omics of NaCl shock (industrial ectoine producer)
A 2024 study on *Halomonas elongata* (important for ectoine production) quantified shock responses:
* NaCl shock within a “tolerable range” of **1–8% NaCl shock** triggers rapid ionic uptake (Na+, K+) and amino‑acid pool increases (notably glutamate/glutamine), followed by **delayed ectoine accumulation** that becomes dominant after ~20 min. (Yu et al., 2024; DOI:10.1186/s12934-024-02358-5; published Mar 2024; URL https://doi.org/10.1186/s12934-024-02358-5) (yu2024temporaldynamicsof pages 1-2)
* Ectoine productivity reached **1450 ± 99 mg/L/h** in the described conditions. (Yu et al., 2024) (yu2024temporaldynamicsof pages 1-2)
* 5% and 8% NaCl shocks induced ectoine accumulation to **4.08 ± 0.28 g/L** and **4.58 ± 0.19 g/L** at 4 h; by contrast, **13% shock** caused “hardly any ectoine accumulation” and strong growth inhibition. (Yu et al., 2024) (yu2024temporaldynamicsof pages 2-5)

Although this work is on a halophile (not a low‑optimum organism), it provides mechanistic/quantitative constraints on osmoadaptation modules (ion uptake first; compatible solutes later; energy crisis limits). (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5)

### 3) Current applications and real‑world implementations

#### 3.1 Industrial bioprocessing: osmoadaptation modules as engineering targets
*Halomonas elongata* is described as “industrial[ly] important … for ectoine production,” and the 2024 NaCl‑shock study explicitly frames mechanistic understanding as a basis to “guide future improvements in optimizing industrial ectoine production.” (Yu et al., 2024; DOI:10.1186/s12934-024-02358-5) (yu2024temporaldynamicsof pages 1-2)

At the mechanistic level, compatible solutes (e.g., glycine betaine, ectoine) are widely used osmoprotectants, and bacteria “respond to osmotic stress by intracellularly accumulating … compatible solutes.” (Thomas et al., 2025; DOI:10.1128/aem.00619-25; published May 2025; URL https://doi.org/10.1128/aem.00619-25) (thomas2025dualrolesof pages 1-2)

#### 3.2 Agriculture/host‑associated niches: osmoprotection genes in microbiomes
Genome mining of bacteria from maize silk microbiomes identified gene sets for osmoprotection including **ectABC**, **ectT**, **betA/betB**, multiple **trehalose** pathways, and mechanosensitive channels **mscS/mscL**, indicating real-world selection for osmotic survival modules in fluctuating plant microenvironments. (Thompson & Raizada, 2024; DOI:10.3390/microorganisms12071473; published Jul 2024; URL https://doi.org/10.3390/microorganisms12071473) (thompson2024themicrobiomeof pages 5-6)

### 4) Expert opinions and authoritative synthesis

#### 4.1 c‑di‑AMP integrates K+ and compatible‑solute transport to manage volume
Foster et al. (2024) synthesize evidence that c‑di‑AMP controls cell volume by inhibiting **K+ influx** and **compatible solute influx** and activating **K+ efflux**, emphasizing that many targets are transporters central to osmoadaptation. (Foster et al., 2024; DOI:10.1128/mmbr.00181-23) (foster2024bacterialcellvolume pages 31-33)

#### 4.2 Transporter-level regulation as a mechanistic axis for salt phenotype boundaries
Because “non‑halophilic” vs “halophilic” is defined by **optimum** salinity, while halotolerance is a **capacity** to grow at higher salt, mechanistic modules (e.g., betaine transport, K+ uptake/efflux, c‑di‑AMP regulation) are best modeled as causal contributors to **tolerance range and adaptation kinetics**, not as direct determinants of low optimum. This is consistent with evidence that the same organism can shift strategies depending on salt regime (e.g., uptake vs synthesis of glycine betaine; Trk vs Kdp emphasis) in halophiles/halotolerants. (nie2025ahalophilicbacterium pages 13-15, foster2024bacterialcellvolume pages 8-10)

### 5) Recent statistics and quantitative data
* **Definition threshold:** <0.2 M NaCl (~1% w/v) for non‑halophilic optimal growth. (Amoozegar et al., 2019; Didari et al., 2020) (amoozegar2019halophilesandtheir pages 1-2, didari2020diversityofhalophilic pages 1-2)
* **NaCl shock tolerance window (example halophile):** tolerable NaCl shock **1–8%**, with a reported tolerance threshold up to **~13%** in the studied design. (Yu et al., 2024) (yu2024temporaldynamicsof pages 1-2)
* **Ectoine productivity:** **1450 ± 99 mg/L/h** (H. elongata post‑shock dynamics). (Yu et al., 2024) (yu2024temporaldynamicsof pages 1-2)
* **Ectoine titers:** 5% and 8% shocks yielded **4.08 ± 0.28 g/L** and **4.58 ± 0.19 g/L** ectoine at 4 h, while 13% shock produced minimal ectoine. (Yu et al., 2024) (yu2024temporaldynamicsof pages 2-5)
* **Growth NaCl range (marine Vibrio example):** *Vibrio natriegens* “can grow in **1% to 7% NaCl**” and responds with compatible solute synthesis/import. (Thomas et al., 2025) (thomas2025dualrolesof pages 1-2)

## Curation-focused sections for TraitMech causal graph

### A) Trait scope (curation guidance)
**Recommended curation interpretation:**
* The trait represents **the NaCl concentration at which growth is maximal** (optimum) and is operationally **≤ ~1% w/v NaCl**. (amoozegar2019halophilesandtheir pages 1-2, didari2020diversityofhalophilic pages 1-2)
* **Do not equate** “growth at X% NaCl” or “tolerance up to X%” with optimum. Halotolerant organisms may still have low optimum. (didari2020diversityofhalophilic pages 1-2)

**Boundary cases to flag:**
* **Slight halophiles**: optimum in ~1–5% NaCl range should not be mapped to this trait even if they tolerate low NaCl. (Amoozegar et al., 2019) (amoozegar2019halophilesandtheir pages 1-2)
* **Media dependence:** availability of exogenous osmoprotectants (e.g., glycine betaine) can change observed salt-stress outcomes and may shift apparent “best growth” in certain assays. (Nie et al., 2025) (nie2025ahalophilicbacterium pages 1-2)

### B) Candidate nodes grouped by type
The following node inventory is curation-oriented and grounded in retrieved evidence:

| Node label | Type | Suggested CURIE(s) if known | Evidence/source (DOI, year, URL) | Notes |
|---|---|---|---|---|
| low NaCl concentration (optimal growth at <0.2 M, ~1% w/v) | environmental factor | CHEBI:26710 (sodium chloride) | 10.3389/fmicb.2019.01895, 2019, https://doi.org/10.3389/fmicb.2019.01895 (amoozegar2019halophilesandtheir pages 1-2) | Core trait-defining environment for non-halophilic optimum. |
| high NaCl concentration / salt stress | environmental factor | CHEBI:26710 | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Used in mechanistic studies as 12–20% NaCl stress; informative for boundary mechanisms but not direct evidence for low-optimum trait. |
| osmotic upshift / NaCl shock | assay factor | GO:0006970 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) | Common experimental perturbation to reveal salt-response mechanisms. |
| K+ limitation | assay factor |  | 10.1128/jb.00107-24, 2024, https://doi.org/10.1128/jb.00107-24 (quinteroyanes2024regulationofpotassium pages 1-2 summarized in search output) | Relevant assay condition for K+ uptake systems; indirect to NaCl optimum. |
| sodium chloride | chemical | CHEBI:26710 | 10.3389/fmicb.2019.01895, 2019, https://doi.org/10.3389/fmicb.2019.01895 (amoozegar2019halophilesandtheir pages 1-2) | Chemical whose optimal concentration defines the trait. |
| sodium ion | chemical | CHEBI:29101 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2) | Rapidly taken up during early NaCl shock response in H. elongata. |
| potassium ion | chemical | CHEBI:29103 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5; 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (yu2024temporaldynamicsof pages 1-2, foster2024bacterialcellvolume pages 8-10) | Central osmotic balancing cation and target of multiple regulated transport systems. |
| glycine betaine | chemical | CHEBI:17750 | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25; 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (thomas2025dualrolesof pages 1-2, nie2025ahalophilicbacterium pages 13-15) | Major compatible solute; can be synthesized or imported. |
| ectoine | chemical | CHEBI:59999 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5; 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 (yu2024temporaldynamicsof pages 1-2, thomas2025dualrolesof pages 1-2) | Dominant osmoprotectant in H. elongata after delay; common compatible solute node. |
| hydroxyectoine | chemical | CHEBI:58183 | 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6) | Candidate node from ectoine-related transport/catabolism systems. |
| proline | chemical | CHEBI:17203 | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 15-16) | Compatible solute synthesized from glutamate under salt stress in some taxa. |
| trehalose | chemical | CHEBI:18133 | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23; 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (foster2024bacterialcellvolume pages 6-8, thompson2024themicrobiomeof pages 5-6) | Mentioned as compatible solute in general osmoadaptation context. |
| glutamate | chemical | CHEBI:29991 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5; 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 (yu2024temporaldynamicsof pages 1-2, thomas2025dualrolesof pages 1-2) | Early osmotic-response amino acid and precursor for proline in some systems. |
| glutamine | chemical | CHEBI:28300 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2) | Rapidly augmented during NaCl shock response. |
| choline | chemical | CHEBI:15354 | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 (thomas2025dualrolesof pages 1-2) | Precursor for glycine betaine biosynthesis via bet genes. |
| glutathione | chemical | CHEBI:16856 | 10.1128/aem.01562-23, 2024, https://doi.org/10.1128/aem.01562-23 (wang2024effectofglutathionetransportrelated pages 1-2 summarized in search output) | Linked to desiccation/osmotic tolerance and K+ homeostasis; indirect candidate. |
| Trk potassium uptake system | pathway/process | GO:0006813 | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474; 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (nie2025ahalophilicbacterium pages 8-11, foster2024bacterialcellvolume pages 8-10) | Strong candidate core K+ uptake module in salt response. |
| Kdp potassium uptake system | pathway/process | GO:0006813 | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23; 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (foster2024bacterialcellvolume pages 8-10, nie2025ahalophilicbacterium pages 8-11) | High-affinity K+ uptake system; often transcriptionally regulated. |
| compatible solute transport | pathway/process | GO:0015840 | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25; 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (thomas2025dualrolesof pages 1-2, foster2024bacterialcellvolume pages 10-12) | Broad process covering betaine/ectoine uptake systems. |
| glycine betaine biosynthetic process | pathway/process | GO:0019491 | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25; 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (thomas2025dualrolesof pages 1-2, nie2025ahalophilicbacterium pages 13-15) | Candidate pathway node for salt-adaptive osmolyte synthesis. |
| ectoine biosynthetic process | pathway/process | GO:0019493 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5; 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (yu2024temporaldynamicsof pages 1-2, thompson2024themicrobiomeof pages 5-6) | Strong osmoprotection pathway, though more typical of halophiles/halotolerant taxa. |
| proline biosynthetic process | pathway/process | GO:0006561 | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 11-13, nie2025ahalophilicbacterium pages 15-16) | Upregulated under high-salt stress in DY09. |
| sodium ion export / Na+/H+ antiport | pathway/process | GO:0006814 | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Key ionic homeostasis process under elevated NaCl. |
| osmotic stress response | pathway/process | GO:0006970 | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25; 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 (thomas2025dualrolesof pages 1-2, yu2024temporaldynamicsof pages 1-2) | High-level process node for many causal edges. |
| oxidative stress response | pathway/process | GO:0006979 | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5; 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (yu2024temporaldynamicsof pages 1-2, nie2025ahalophilicbacterium pages 13-15) | Salt shock often triggers ROS defense alongside osmotic response. |
| betA | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474; 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 (nie2025ahalophilicbacterium pages 13-15, thomas2025dualrolesof pages 1-2) | Choline-to-betaine pathway enzyme; candidate enzyme node. |
| betB | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474; 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 (nie2025ahalophilicbacterium pages 13-15, thomas2025dualrolesof pages 1-2) | Betaine aldehyde dehydrogenase candidate. |
| betH / opuD | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 11-13, nie2025ahalophilicbacterium pages 13-15) | Major glycine betaine transporter candidate in DY09. |
| OpuA transporter | gene/protein |  | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13) | Compatible-solute ABC importer regulated by c-di-AMP. |
| OpuC transporter | gene/protein |  | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 10-12) | Additional compatible-solute importer regulated by c-di-AMP. |
| BCCT transporters | gene/protein |  | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 (thomas2025dualrolesof pages 1-2) | Secondary transporters for glycine betaine/dimethylglycine uptake. |
| ectA | gene/protein |  | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5; 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (yu2024temporaldynamicsof pages 10-13, thompson2024themicrobiomeof pages 5-6) | Ectoine biosynthesis enzyme candidate. |
| ectB | gene/protein |  | 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6) | Ectoine biosynthesis enzyme candidate. |
| ectC | gene/protein |  | 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6) | Ectoine biosynthesis enzyme candidate. |
| ectT | gene/protein |  | 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6) | High-affinity ectoine/hydroxyectoine importer candidate. |
| ehuABCD | gene/protein |  | 10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6) | Ectoine-specific import genes in some bacteria; candidate transport node. |
| trkA | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Part of Trk K+ uptake system. |
| trkH | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Membrane component of Trk K+ uptake system. |
| kdpD | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474; 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (nie2025ahalophilicbacterium pages 8-11, foster2024bacterialcellvolume pages 8-10) | Sensor kinase controlling kdp system; c-di-AMP target. |
| KdpFABC complex | gene/protein |  | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23; 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (foster2024bacterialcellvolume pages 8-10, nie2025ahalophilicbacterium pages 8-11) | High-affinity K+ pump complex. |
| KimA | gene/protein |  | 10.1038/s41467-023-38944-1, 2023, https://doi.org/10.1038/s41467-023-38944-1; 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (fuss2023cyclicdiamptraps pages 1-2, foster2024bacterialcellvolume pages 8-10) | KUP-family K+/H+ symporter inhibited by c-di-AMP. |
| Kup family transporter | gene/protein |  | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 8-10) | General KUP-family K+ uptake node when KimA-specific grounding is not desired. |
| chaA | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Na+/H+ antiporter candidate. |
| nhaC | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Na+/H+ antiporter candidate. |
| nhaD | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15) | Na+/H+ antiporter candidate. |
| mnhA-E | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | Multisubunit Na+/H+ antiporter complex candidate. |
| norM | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 8-11) | Upregulated with salt in DY09; role may be broader than Na+ homeostasis. |
| proA | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 11-13, nie2025ahalophilicbacterium pages 15-16) | Proline biosynthesis enzyme candidate. |
| proB | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 11-13, nie2025ahalophilicbacterium pages 15-16) | Proline biosynthesis enzyme candidate. |
| proC / pyrroline-5-carboxylate reductase | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 11-13, nie2025ahalophilicbacterium pages 15-16) | Strong candidate osmolyte-synthesis enzyme under high salt. |
| katE | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15) | Catalase, part of salt-induced oxidative stress defense. |
| tpx | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15) | Thiol peroxidase candidate salt-stress defense enzyme. |
| HELO_RS18165 | gene/protein |  | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2) | Peroxidase gene induced by NaCl shock in H. elongata. |
| groES | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15) | Chaperone upregulated under salt stress. |
| groEL | gene/protein |  | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 13-15) | Chaperone upregulated under salt stress. |
| cyclic di-AMP | regulator | CHEBI:90647 | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23; 10.1038/s41467-023-38944-1, 2023, https://doi.org/10.1038/s41467-023-38944-1 (foster2024bacterialcellvolume pages 8-10, fuss2023cyclicdiamptraps pages 1-2) | Master regulator of K+ and compatible-solute transport in many bacteria. |
| ydaO riboswitch | regulator |  | 10.1038/s41467-023-38944-1, 2023, https://doi.org/10.1038/s41467-023-38944-1; 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (fuss2023cyclicdiamptraps pages 1-2, foster2024bacterialcellvolume pages 8-10) | c-di-AMP-responsive riboswitch controlling kimA/ktrAB and related loci. |
| BusR | regulator |  | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 10-12) | c-di-AMP-binding regulator that represses opuA expression. |
| KdpDE two-component system | regulator | GO:0000156 | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 8-10) | Regulatory system linking c-di-AMP/K+ status to kdp transcription. |
| cysB | regulator |  | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2) | Salt-shock-induced transcription factor tied to sulfur metabolism/cysteine biosynthesis. |


*Table: This table lists candidate nodes for a NaCl optimum low causal graph, grouped across environmental factors, chemicals, pathways, proteins, and regulators. It is useful as a curation-ready inventory of mechanistic entities already supported by the retrieved literature.*

### C) Candidate causal edges (evidence-backed)
The following table compiles candidate edges suitable for a TraitMech causal graph. Note that many mechanistic edges are drawn from halophiles/halotolerants and therefore should be curated as **general osmoadaptation mechanisms** unless directly linked to low-NaCl optima.

| Edge (triple) | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|
| non-halophilic optimum NaCl defined_as optimal growth at less than 0.2 M NaCl or about 1 percent w/v (amoozegar2019halophilesandtheir pages 1-2, didari2020diversityofhalophilic pages 1-2) | “non-halophilic microorganisms grow optimally at less than 0.2 M (1%) NaCl”; “non-halophilic... growing best in media containing less than 0.2 M salt” (amoozegar2019halophilesandtheir pages 1-2, didari2020diversityofhalophilic pages 1-2) | 10.3389/fmicb.2019.01895, 2019, https://doi.org/10.3389/fmicb.2019.01895; 10.1007/s40201-020-00519-3, 2020, https://doi.org/10.1007/s40201-020-00519-3 | Strong scope edge; definitional rather than mechanistic. |
| halotolerant microorganism is_a non-halophilic organism able to grow at high salt (didari2020diversityofhalophilic pages 1-2) | “halotolerant organisms [are] those non-halophilic... able to grow at high salt concentrations” (didari2020diversityofhalophilic pages 1-2) | 10.1007/s40201-020-00519-3, 2020, https://doi.org/10.1007/s40201-020-00519-3 | Strong definitional edge; useful for boundary cases. |
| osmotic upshift or NaCl shock induces rapid K plus and Na plus uptake (yu2024temporaldynamicsof pages 1-2) | “balanced the surging osmotic pressure by uptaking sodium and potassium ions”; “Immediate osmotic responses include uptake of sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | Taxon-specific to Halomonas elongata; high-salt shock assay, not low-optimum phenotype directly. |
| osmotic upshift or NaCl shock increases intracellular glutamate and glutamine pools (yu2024temporaldynamicsof pages 1-2) | “augmenting intracellular amino acid pools, particularly glutamate and glutamine” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | Taxon-specific to H. elongata; likely a general osmoadaptation response. |
| osmotic upshift or NaCl shock delays then induces ectoine accumulation (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) | “ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant”; “5% and 8% NaCl shocks induced rapid biosynthesis and accumulation of intracellular ectoine” (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | Strong experimental support, but from a halophile model and not specific to low-NaCl-optimum organisms. |
| compatible solute accumulation supports osmotic stress adaptation (thomas2025dualrolesof pages 1-2) | “Bacteria respond to osmotic stress by intracellularly accumulating low molecular weight compounds called compatible solutes” (thomas2025dualrolesof pages 1-2) | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 | General mechanistic edge from Vibrio natriegens. |
| glycine betaine biosynthesis and import contributes_to osmotic stress response (thomas2025dualrolesof pages 1-2) | “V. natriegens can... biosynthesize GB, ectoine, and glutamate and import GB, DMG, and sarcosine in response to osmotic stress” (thomas2025dualrolesof pages 1-2) | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 | Taxon-specific; useful compatible-solute node and edge. |
| BCCT transporters mediate_uptake_of glycine betaine and dimethylglycine (thomas2025dualrolesof pages 1-2) | “Betaine-carnitine-choline transporters (BCCTs) for the uptake of GB and DMG... were identified” (thomas2025dualrolesof pages 1-2) | 10.1128/aem.00619-25, 2025, https://doi.org/10.1128/aem.00619-25 | Taxon-specific to V. natriegens; transporter family edge is strong. |
| high salt 12 to 20 percent NaCl upregulates betA and betB glycine betaine biosynthesis genes (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 11-13) | “both GB transport and biosynthesis genes (betA, betB) are significantly upregulated”; “betA and betB... are upregulated at 12% and 20%” (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 11-13) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Strong transcriptomic support in Oceanobacillus picturae DY09; high-salt condition. |
| high salt 12 to 20 percent NaCl upregulates betH or opuD glycine betaine transporter (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 11-13) | “opuD/betH shows progressive upregulation”; “transport gene opuD/betH... significantly upregulated under high salt” (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 11-13) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Strong transcriptomic support; taxon- and assay-specific. |
| low salt 4 percent NaCl upregulates betH or opuD without concurrent betA or betB induction (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 1-2) | “GB transport (opuD/betH) is upregulated at low salt (4% NaCl) without concurrent betA/betB induction”; “preferentially utilizing exogenous GB to maintain basic osmotic balance” (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 1-2) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Suggests uptake-first strategy; still not low-optimum trait evidence because 4 percent is not low NaCl for this trait. |
| high salt 12 to 20 percent NaCl upregulates Trk K plus uptake system trkA and trkH (nie2025ahalophilicbacterium pages 8-11, nie2025ahalophilicbacterium pages 13-15) | “Trk components (trkA, trkH) are significantly upregulated under high salt”; “Trk system (trkA, trkH) activated to raise intracellular K+” (nie2025ahalophilicbacterium pages 8-11, nie2025ahalophilicbacterium pages 13-15) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Strong transcriptomic support in one halophile; may generalize to osmotic upshift responses. |
| high salt 12 to 20 percent NaCl upregulates Na plus or H plus antiporters chaA nhaC nhaD and mnhA to E (nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11) | “single-subunit chaA, nhaC, nhaD and multi-subunit mnhA-E are significantly upregulated... to extrude Na+” (nie2025ahalophilicbacterium pages 13-15) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Strong transcriptomic support; direct antiporter mechanism. |
| high salt 12 to 20 percent NaCl upregulates oxidative stress defenses katE tpx ydfG GM000042 and yqjC (nie2025ahalophilicbacterium pages 13-15) | “detoxification genes (katE, tpx, ydfG, GM000042) rise ~2–6x, yqjC ~15x” (nie2025ahalophilicbacterium pages 13-15) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Strong in O. picturae; stress-response branch, indirect to optimum. |
| high salt upregulates groES and groEL chaperones (nie2025ahalophilicbacterium pages 13-15) | “groES ~6x at 4% and ~12x at 20%; groEL ~3x at 4% and ~2x at 20%” (nie2025ahalophilicbacterium pages 13-15) | 10.3390/microorganisms13071474, 2025, https://doi.org/10.3390/microorganisms13071474 | Strong transcriptomic support; indicates proteostasis role under salt stress. |
| NaCl shock upregulates cysB and antioxidant enzymes (yu2024temporaldynamicsof pages 1-2) | “transcription factor cys B was significantly upregulated”; “upregulation of the crucial peroxidase gene (HELO_RS18165) and... POD and CAT activities” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | Taxon-specific to H. elongata; oxidative-stress arm of osmotic response. |
| cyclic di-AMP inhibits K plus uptake systems Trk Ktr Kup and KimA (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 6-8) | “gating subunits of Trk/Ktr... all bind cyclic di-AMP”; “its activity is inhibited by cyclic di-AMP” for KUP-family transporters (foster2024bacterialcellvolume pages 8-10) | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 | Review-level synthesis across taxa; strong for general regulation but not specific to NaCl optimum low. |
| cyclic di-AMP inhibits_transcription_of kdpFABC via KdpD and riboswitch control (foster2024bacterialcellvolume pages 8-10) | “KdpD binds cyclic di-AMP... which leads to inhibition of kdpFABC-operon transcription”; riboswitches occur “upstream of trk, ktr, kdp, and kup genes” (foster2024bacterialcellvolume pages 8-10) | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 | Review-level edge integrating multiple studies; likely broad in c-di-AMP-producing bacteria. |
| cyclic di-AMP negatively_regulates OpuA and OpuC compatible-solute transport (foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 12-13) | “c-di-AMP binds CBS and RCK_C domains of compatible-solute importers (OpuA/OpuC) and negatively regulates their transport activity” (foster2024bacterialcellvolume pages 10-12) | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 | Strong review evidence; mostly Gram-positive model systems. |
| cyclic di-AMP inhibits_expression_of opuA via BusR (foster2024bacterialcellvolume pages 10-12) | “c-di-AMP binds the RCK_C domain of BusR... inhibiting opuA expression and decreasing glycine betaine uptake” (foster2024bacterialcellvolume pages 10-12) | 10.1128/mmbr.00181-23, 2024, https://doi.org/10.1128/mmbr.00181-23 | Strong regulatory edge; species specificity should be checked before direct curation. |
| cyclic di-AMP inhibits KimA KUP-family K plus H plus symporter activity (fuss2023cyclicdiamptraps pages 1-2) | “KimA... is inactivated by c-di-AMP”; co-production with cyclase “reduced KimA Vmax by ~64%” (fuss2023cyclicdiamptraps pages 1-2) | 10.1038/s41467-023-38944-1, 2023, https://doi.org/10.1038/s41467-023-38944-1 | Strong primary mechanistic evidence in Bacillus subtilis model; not directly tied to low-optimum phenotype. |
| ydaO riboswitch represses kimA and ktrAB transcription in response to cyclic di-AMP (fuss2023cyclicdiamptraps pages 1-2) | “c-di-AMP also suppresses gene expression via the ydaO riboswitch, which controls transcription of kimA and ktrAB” (fuss2023cyclicdiamptraps pages 1-2) | 10.1038/s41467-023-38944-1, 2023, https://doi.org/10.1038/s41467-023-38944-1 | Strong for Gram-positive c-di-AMP systems; regulatory edge rather than phenotype edge. |


*Table: This table lists candidate causal edges for NaCl optimum low and related osmoadaptation mechanisms, with short supporting quotes, DOI-first sources, and curation notes about scope and uncertainty.*

### D) Visual synthesis (supports mechanistic edge structure)
Foster et al. (2024) Figure 1B provides a curated schematic of ion/osmolyte influx/efflux systems, explicitly distinguishing those regulated by cyclic di‑AMP, which is directly useful for causal graph layout (transport modules and regulatory links). (foster2024bacterialcellvolume media 7ac30d40)

## Warnings / claims not ready for direct curation into a “NaCl optimum low” mechanism graph
1. **Mechanism vs optimum:** The retrieved mechanistic evidence largely explains **adaptation to increased salinity** (osmotic upshift, high-salt stress) rather than explaining why an organism’s **optimum** is at ≤1% NaCl. Edges should therefore be curated as contributing to **tolerance/adaptation** unless additional sources link them to shifting the growth optimum itself. (yu2024temporaldynamicsof pages 1-2, foster2024bacterialcellvolume pages 8-10, nie2025ahalophilicbacterium pages 13-15)
2. **Taxon specificity:** Some nodes/edges (e.g., *Halomonas elongata* ectoine dynamics; *B. subtilis* KimA inhibition by c‑di‑AMP; *Oceanobacillus* betaine/antiporter transcription patterns) may not generalize. Mark these edges as **uncertain** for TraitMech unless corroborated across taxa. (yu2024temporaldynamicsof pages 1-2, fuss2023cyclicdiamptraps pages 1-2, nie2025ahalophilicbacterium pages 13-15)
3. **Assay specificity:** Many edges are derived from **shock experiments** (rapid NaCl increase), which probe dynamic responses rather than steady-state optimum conditions. Curate as “response to osmotic upshift” rather than “determinant of optimum” unless additional steady-state evidence is available. (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5)
4. **Missing key legacy review:** The template’s existing evidence cites DOI:10.1093/femsre/fuy009, but this paper was not retrievable in the current tool run; therefore, its specific claims cannot be quoted/cited here and should not be treated as incorporated evidence. (tool retrieval log indicates unobtainable)

## DOI-first bibliography (with dates/URLs where available)
1. Foster AJ, van den Noort M, Poolman B. *Bacterial cell volume regulation and the importance of cyclic di-AMP.* **Microbiology and Molecular Biology Reviews**. Published Jun 2024. DOI:10.1128/mmbr.00181-23. https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 8-10, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 31-33, foster2024bacterialcellvolume media 7ac30d40)
2. Fuss MF, Wieferig J-P, Corey RA, et al. *Cyclic di-AMP traps proton-coupled K+ transporters of the KUP family in an inward-occluded conformation.* **Nature Communications**. Published Jun 2023. DOI:10.1038/s41467-023-38944-1. https://doi.org/10.1038/s41467-023-38944-1 (fuss2023cyclicdiamptraps pages 1-2)
3. Yu J, Zhang Y, Liu H, et al. *Temporal dynamics of stress response in Halomonas elongata to NaCl shock: physiological, metabolomic, and transcriptomic insights.* **Microbial Cell Factories**. Published Mar 2024. DOI:10.1186/s12934-024-02358-5. https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5)
4. Thompson MEH, Raizada MN. *The Microbiome of Fertilization-Stage Maize Silks (Style) Encodes Genes and Expresses Traits That Potentially Promote Survival in Pollen/Style Niches and Host Reproduction.* **Microorganisms**. Published Jul 2024. DOI:10.3390/microorganisms12071473. https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6)
5. Didari M, Bagheri M, Amoozegar MA, et al. *Diversity of halophilic and halotolerant bacteria in the largest seasonal hypersaline lake (Aran-Bidgol-Iran).* **Journal of Environmental Health Science and Engineering**. Published Aug 2020. DOI:10.1007/s40201-020-00519-3. https://doi.org/10.1007/s40201-020-00519-3 (didari2020diversityofhalophilic pages 1-2)
6. Amoozegar MA, Safarpour A, Noghabi KA, Bakhtiary T, Ventosa A. *Halophiles and Their Vast Potential in Biofuel Production.* **Frontiers in Microbiology**. Published Aug 2019. DOI:10.3389/fmicb.2019.01895. https://doi.org/10.3389/fmicb.2019.01895 (amoozegar2019halophilesandtheir pages 1-2)
7. Lee CJD, McMullan PE, O’Kane CJ, et al. *NaCl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats.* **FEMS Microbiology Reviews**. Published Jun 2018. DOI:10.1093/femsre/fuy026. https://doi.org/10.1093/femsre/fuy026 (lee2018naclsaturatedbrinesare pages 15-17)
8. Nie T, Wang L, Liu Y, et al. *A Halophilic Bacterium for Bioremediation of Saline–Alkali Land: The Triadic and Synergetic Response Mechanism of Oceanobacillus picturae DY09 to Salt Stress.* **Microorganisms**. Published Jun 2025. DOI:10.3390/microorganisms13071474. https://doi.org/10.3390/microorganisms13071474 (nie2025ahalophilicbacterium pages 1-2, nie2025ahalophilicbacterium pages 13-15, nie2025ahalophilicbacterium pages 8-11)
9. Thomas HE, Lichty KEB, Richards GP, Boyd EF. *Dual roles of glycine betaine, dimethylglycine, and sarcosine as osmoprotectants and nutrient sources for Vibrio natriegens.* **Applied and Environmental Microbiology**. Published May 2025. DOI:10.1128/aem.00619-25. https://doi.org/10.1128/aem.00619-25 (thomas2025dualrolesof pages 1-2)
10. Śliżewska W, Struszczyk-Świta K, Otlewska A, et al. *Halophilic and halotolerant fungi across diverse climates: a comparative study of Polish and Italian soil ecosystems.* **Frontiers in Microbiology**. Published Jul 2025. DOI:10.3389/fmicb.2025.1637496. https://doi.org/10.3389/fmicb.2025.1637496 (slizewska2025halophilicandhalotolerant pages 1-2)


References

1. (amoozegar2019halophilesandtheir pages 1-2): Mohammad Ali Amoozegar, Atefeh Safarpour, Kambiz Akbari Noghabi, Tala Bakhtiary, and Antonio Ventosa. Halophiles and their vast potential in biofuel production. Frontiers in Microbiology, Aug 2019. URL: https://doi.org/10.3389/fmicb.2019.01895, doi:10.3389/fmicb.2019.01895. This article has 163 citations and is from a peer-reviewed journal.

2. (didari2020diversityofhalophilic pages 1-2): Maryam Didari, Maryam Bagheri, Mohammad Ali Amoozegar, Saied Bouzari, Hamid Babavalian, Hamid Tebyanian, Mehdi Hassanshahian, and Antonio Ventosa. Diversity of halophilic and halotolerant bacteria in the largest seasonal hypersaline lake (aran-bidgol-iran). Journal of Environmental Health Science and Engineering, 18:961-971, Aug 2020. URL: https://doi.org/10.1007/s40201-020-00519-3, doi:10.1007/s40201-020-00519-3. This article has 27 citations.

3. (slizewska2025halophilicandhalotolerant pages 1-2): Weronika Śliżewska, Katarzyna Struszczyk-Świta, Anna Otlewska, Flavia Pinzari, Loredana Canfora, Katarzyna Dybka-Stȩpień, Rosario Napoli, Melania Migliore, Andrea Manfredini, and Olga Marchut-Mikołajczyk. Halophilic and halotolerant fungi across diverse climates: a comparative study of polish and italian soil ecosystems. Frontiers in Microbiology, Jul 2025. URL: https://doi.org/10.3389/fmicb.2025.1637496, doi:10.3389/fmicb.2025.1637496. This article has 6 citations and is from a peer-reviewed journal.

4. (lee2018naclsaturatedbrinesare pages 15-17): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 90 citations and is from a domain leading peer-reviewed journal.

5. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (foster2024bacterialcellvolume pages 10-12): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (foster2024bacterialcellvolume pages 31-33): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

8. (foster2024bacterialcellvolume media 7ac30d40): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (fuss2023cyclicdiamptraps pages 1-2): Michael F. Fuss, Jan-Philip Wieferig, Robin A. Corey, Yvonne Hellmich, Igor Tascón, Joana S. Sousa, Phillip J. Stansfeld, Janet Vonck, and Inga Hänelt. Cyclic di-amp traps proton-coupled k+ transporters of the kup family in an inward-occluded conformation. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38944-1, doi:10.1038/s41467-023-38944-1. This article has 23 citations and is from a highest quality peer-reviewed journal.

10. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

11. (yu2024temporaldynamicsof pages 2-5): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

12. (thomas2025dualrolesof pages 1-2): Heather E. Thomas, Katherine E. Boas Lichty, Gary P. Richards, and E. Fidelma Boyd. Dual roles of glycine betaine, dimethylglycine, and sarcosine as osmoprotectants and nutrient sources for <i>vibrio natriegens</i>. May 2025. URL: https://doi.org/10.1128/aem.00619-25, doi:10.1128/aem.00619-25. This article has 9 citations and is from a peer-reviewed journal.

13. (thompson2024themicrobiomeof pages 5-6): Michelle E. H. Thompson and Manish N. Raizada. The microbiome of fertilization-stage maize silks (style) encodes genes and expresses traits that potentially promote survival in pollen/style niches and host reproduction. Microorganisms, 12:1473, Jul 2024. URL: https://doi.org/10.3390/microorganisms12071473, doi:10.3390/microorganisms12071473. This article has 6 citations.

14. (nie2025ahalophilicbacterium pages 13-15): Tianying Nie, Liuqing Wang, Yilan Liu, Siqi Fu, Jiahui Wang, Kunpeng Cui, and Lu Wang. A halophilic bacterium for bioremediation of saline–alkali land: the triadic and synergetic response mechanism of oceanobacillus picturae dy09 to salt stress. Microorganisms, 13:1474, Jun 2025. URL: https://doi.org/10.3390/microorganisms13071474, doi:10.3390/microorganisms13071474. This article has 10 citations.

15. (nie2025ahalophilicbacterium pages 1-2): Tianying Nie, Liuqing Wang, Yilan Liu, Siqi Fu, Jiahui Wang, Kunpeng Cui, and Lu Wang. A halophilic bacterium for bioremediation of saline–alkali land: the triadic and synergetic response mechanism of oceanobacillus picturae dy09 to salt stress. Microorganisms, 13:1474, Jun 2025. URL: https://doi.org/10.3390/microorganisms13071474, doi:10.3390/microorganisms13071474. This article has 10 citations.

16. (nie2025ahalophilicbacterium pages 8-11): Tianying Nie, Liuqing Wang, Yilan Liu, Siqi Fu, Jiahui Wang, Kunpeng Cui, and Lu Wang. A halophilic bacterium for bioremediation of saline–alkali land: the triadic and synergetic response mechanism of oceanobacillus picturae dy09 to salt stress. Microorganisms, 13:1474, Jun 2025. URL: https://doi.org/10.3390/microorganisms13071474, doi:10.3390/microorganisms13071474. This article has 10 citations.

17. (nie2025ahalophilicbacterium pages 15-16): Tianying Nie, Liuqing Wang, Yilan Liu, Siqi Fu, Jiahui Wang, Kunpeng Cui, and Lu Wang. A halophilic bacterium for bioremediation of saline–alkali land: the triadic and synergetic response mechanism of oceanobacillus picturae dy09 to salt stress. Microorganisms, 13:1474, Jun 2025. URL: https://doi.org/10.3390/microorganisms13071474, doi:10.3390/microorganisms13071474. This article has 10 citations.

18. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

19. (nie2025ahalophilicbacterium pages 11-13): Tianying Nie, Liuqing Wang, Yilan Liu, Siqi Fu, Jiahui Wang, Kunpeng Cui, and Lu Wang. A halophilic bacterium for bioremediation of saline–alkali land: the triadic and synergetic response mechanism of oceanobacillus picturae dy09 to salt stress. Microorganisms, 13:1474, Jun 2025. URL: https://doi.org/10.3390/microorganisms13071474, doi:10.3390/microorganisms13071474. This article has 10 citations.

20. (foster2024bacterialcellvolume pages 12-13): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

21. (yu2024temporaldynamicsof pages 10-13): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.