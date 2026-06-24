---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:03:54.376567'
end_time: '2026-06-18T01:15:08.771046'
duration_seconds: 674.39
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pressure optimum
  trait_identifier: traitmech:000004
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: pressure_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure phenotype with numerical limits giving the hydrostatic pressure
    at which an organism grows fastest.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum,
    120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a measurable
    pressure optimum (120 MPa), the quantitative value this phenotype records.) |
    DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known
    as piezophiles, referring to their preference for high pressure (Pressure-adaptation
    review supports an organism-specific optimal growth pressure as the defining quantity
    for piezophile classification.)'
  causal_graph_summary: 'pressure_optimum_balanced_adaptation: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pressure optimum
- **METPO identifier:** traitmech:000004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits giving the hydrostatic pressure at which an organism grows fastest.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a measurable pressure optimum (120 MPa), the quantitative value this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports an organism-specific optimal growth pressure as the defining quantity for piezophile classification.)
- **Existing causal graph summary:** pressure_optimum_balanced_adaptation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_optimum.yaml`.

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
- **Trait label:** pressure optimum
- **METPO identifier:** traitmech:000004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure phenotype with numerical limits giving the hydrostatic pressure at which an organism grows fastest.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Colwellia marinimaniae MTCD1 illustrates a measurable pressure optimum (120 MPa), the quantitative value this phenotype records.) | DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review supports an organism-specific optimal growth pressure as the defining quantity for piezophile classification.)
- **Existing causal graph summary:** pressure_optimum_balanced_adaptation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pressure optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/pressure_optimum.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **pressure optimum** (METPO: traitmech:000004)

## 0. Scope summary (curation-ready)

**Pressure optimum** is the **hydrostatic pressure at which an organism’s growth rate is maximal** under a specified set of culture conditions (e.g., temperature, medium, electron acceptor/donor). It is used operationally to classify organisms as (i) **non‑piezophiles** (optimum at atmospheric pressure and cannot grow at higher pressure), (ii) **piezosensitive** (optimum at atmospheric pressure but can still grow at higher pressure), and (iii) **piezophiles** (optimum at elevated pressure) (10.3390/microorganisms11071629; published 22 Jun 2023) (scheffer2023themysteryof pages 1-2).

**Boundary cases / distinctions for curation**:
- **Pressure optimum vs pressure range**: Optimum is a single (or narrow) maximum; growth range/tolerance is the span of pressures permitting growth/survival. These are distinct phenotypes and should not be conflated in a causal graph (scheffer2023themysteryof pages 1-2).
- **Pressure optimum vs “HHP tolerance/survival”**: Many studies (especially on non‑piezophiles) report short-term viability or transcriptomic responses at extreme pressures (e.g., 158 MPa) that do not imply a shifted *growth optimum* (10.3389/fmicb.2024.1293928; published 13 Feb 2024) (malas2024biologicalfunctionsat pages 1-2).
- **Assay dependence**: Pressure effects often covary with **low temperature, salinity, and redox** in deep environments; rigorous controls are needed to attribute changes specifically to pressure, including when interpreting compatible solutes or lipid remodeling (scheffer2023themysteryof pages 9-10).

**Assay/implementation constraints**:
- Cultivation and enrichment while maintaining pressure requires specialized pressure vessels/chambers (historically up to ~100 MPa) and modern high-pressure cultivation systems; this is a major practical limiter of available datasets (scheffer2023themysteryof pages 1-2, scheffer2023themysteryof pages 15-16).

## 1. Current understanding: key concepts and definitions

### 1.1 Conceptual model
Pressure optimum is an emergent phenotype reflecting the intersection of:
- **Membrane physical chemistry** under compression (homeoviscous adaptation, porins) (10.3389/fmolb.2022.1058381; published Jan 2023) (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4)
- **Protein/RNA structural constraints** (folding stability, ribosome structure–pressure correlations) (scheffer2023themysteryof pages 10-12)
- **Osmotic/solute and ionic homeostasis** (piezolytes/compatible solutes; cation accumulation) (scheffer2023themysteryof pages 9-10, zheng2023mechanismsofnucleic pages 7-11)
- **Energy metabolism and stress responses** (pressure-responsive respiration, chaperones; oxidative stress defenses) (scheffer2023themysteryof pages 7-9, malas2024biologicalfunctionsat pages 1-2)
- **Behavioral/ecological traits** such as motility that may support nutrient acquisition under pressure (scheffer2023themysteryof pages 6-7).

### 1.2 Quantitative context (statistics and benchmarks)
- Deep-sea pressures are ~**10–100 MPa**, reaching ~**110 MPa** at the deepest explored habitat (Challenger Deep) (scheffer2023themysteryof pages 3-6, malas2024biologicalfunctionsat pages 1-2).
- The review by Scheffer & Gieg reports **>80 piezophile isolates** as of March 2021 (scheffer2023themysteryof pages 3-6).
- A 2024 study frames the **demonstrated growth limit at high hydrostatic pressure as ~140 MPa** (citing prior work) (malas2024biologicalfunctionsat pages 1-2).

### 1.3 Examples of pressure optima (curatable data points)
Recent reviews compile many strain-level optima (often measured under strain-specific temperature conditions). Examples include:
- **Pyrococcus yayanosii**: optimum growth pressure **28 MPa** (scheffer2023themysteryof pages 3-6).
- **Pseudothermotoga elfii** DMS9442: optimum **40 MPa** (scheffer2023themysteryof pages 6-7).
- Multiple piezophilic/piezotolerant isolates with optima spanning **~10–70 MPa** are tabulated (e.g., Alteromonas sp. RS103 25 MPa; Psychromonas 2D2 40 MPa; Shewanella DSS12 30 MPa; Shewanella ATCC 43992 70 MPa; Colwellia Y223G 60 MPa) (10.3389/fmolb.2022.1058381; Jan 2023) (tamby2023microbialmembranelipid pages 4-6).

## 2. Recent developments (prioritizing 2023–2024)

### 2.1 Membrane lipid remodeling as a central mechanistic theme (2023)
A 2023 membrane-focused review emphasizes that, across many piezophiles, membrane lipids shift toward **more unsaturated and/or branched-chain fatty acids** under high hydrostatic pressure, consistent with homeoviscous adaptation (tamby2023microbialmembranelipid pages 1-2). It also provides a curated table linking strain-level pressure optima with reported lipid changes, including frequent mention of PUFAs such as **EPA (C20:5)** and **DHA (C22:6)** (tamby2023microbialmembranelipid pages 4-6, tamby2023microbialmembranelipid pages 2-4).

### 2.2 Mechanistic, multi-omics case study: ion import + unsaturated phospholipids (mBio 2023)
A 2023 mBio study of the wall-less deep-sea bacterium **Hujiaoplasma nucleasis zrk29** (cultured at **12 MPa** vs **0.1 MPa**) presents a coherent tolerance model: (i) increased cation import to raise intracellular osmotic pressure and (ii) increased unsaturated phospholipid chains to maintain membrane properties under pressure (10.1128/mbio.00958-23; Aug 2023) (zheng2023mechanismsofnucleic pages 7-11).
Key quantitative results include **~4–8× higher intracellular Mg2+, K+, Na+** at 12 MPa and a **~2–3× increase** in unsaturated fatty-acid-containing phospholipids, with major changes in PE/PG/PC/PS pools and increased unsaturated FAs (C16:1, C18:1, C18:2) (zheng2023mechanismsofnucleic pages 7-11).

### 2.3 High-pressure transcriptomics relevant to upper limits (Frontiers 2024)
A 2024 Frontiers in Microbiology study exposed **Shewanella oneidensis MR‑1** to **158 MPa** (15 min and 2 h). MR‑1 remained metabolically active and could resume viable growth after 2 h at 158 MPa, with **264 genes** regulated, including arginine biosynthesis genes (**argA/argB/argC/argF**), membrane reconfiguration functions, **cold-shock protein CspG**, and antioxidant defense-related genes (10.3389/fmicb.2024.1293928; published 13 Feb 2024) (malas2024biologicalfunctionsat pages 1-2).
This work is best interpreted as defining **acute survival/response mechanisms** near/above known growth limits rather than establishing a “pressure optimum” shift in MR‑1 (malas2024biologicalfunctionsat pages 1-2).

### 2.4 Systems-level metabolic remodeling under pressure (Applied Microbiology and Biotechnology 2024)
A 2024 multi-omics study of **Microbacterium sediminis YLB‑01** used **30 MPa at 4 °C for 7 days** and found pressure-linked remodeling of lipid metabolism, cell-wall precursor pools (UDP-glucose), and compatible solutes (notably **proline**) (10.1007/s00253-023-12906-5; Jan 2024) (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 11-12).

## 3. Current applications and real-world implementations

### 3.1 Deep biosphere and oceanography
Pressure optima are used to interpret **niche specialization** and to guide cultivation strategies for deep-sea microbes. Quantitative pressure gradients and depth links are central for framing environmental relevance (e.g., ≥10 MPa at ~1000 m depth; deep sea ~10–100 MPa) (scheffer2023themysteryof pages 3-6).

### 3.2 Astrobiology and “ocean worlds” analog experiments
The 2024 MR‑1 study explicitly positions **Titan’s modeled subsurface ocean pressures (≥150 MPa)** as beyond the highest known natural ecosystems on Earth and uses controlled high-pressure culturing/transcriptomics to infer whether pressure might limit life (malas2024biologicalfunctionsat pages 1-2).

### 3.3 Biotechnology / engineering of pressure robustness (adjacent phenotype)
While the provided evidence is primarily ecological/physiological, the mechanistic levers identified—membrane lipid composition, osmolytes, ion transport, and stress responses—are the same targets used in engineering robustness traits (e.g., altering lipid chemistry to resist compression). For trait curation, this supports inclusion of these nodes as mechanistically relevant even when pressure optimum per se is not directly measured in each study (tamby2023microbialmembranelipid pages 1-2, zheng2023mechanismsofnucleic pages 7-11).

## 4. Expert opinions and synthesis from authoritative sources (with curation implications)

- Scheffer & Gieg (2023) frame piezophiles as understudied largely due to the technical and sampling constraints of high-pressure cultivation, and highlight **motility, unsaturated membrane lipids, heat shock proteins, and gene regulation** as recurring adaptation themes (scheffer2023themysteryof pages 1-2).
- Tamby et al. (2023) stress that membrane lipid adaptation is important but **not universal** across piezophiles, and that pressure effects are hard to disentangle from co-varying low temperature—this is a key warning for causal-graph edges that assume a single “universal” mechanistic path to a given pressure optimum (tamby2023microbialmembranelipid pages 1-2).

## 5. Candidate causal-graph nodes (grouped by type, with grounding suggestions)

| Node label | Type | Suggested ontology grounding | Evidence source(s) |
|---|---|---|---|
| hydrostatic pressure | environmental factor | ENVO:09200014 high hydrostatic pressure (candidate); PATO/label-only if ENVO not adopted | (scheffer2023themysteryof pages 1-2, tamby2023microbialmembranelipid pages 1-2, malas2024biologicalfunctionsat pages 1-2) |
| temperature | environmental factor | ENVO:01000206 temperature | (scheffer2023themysteryof pages 1-2, scheffer2023themysteryof pages 15-16, tamby2023microbialmembranelipid pages 1-2) |
| salinity | environmental factor | ENVO:3100031 salinity (candidate) | (scheffer2023themysteryof pages 1-2, scheffer2023themysteryof pages 9-10) |
| redox conditions | environmental factor | label-only candidate; GO:0055114 oxidation-reduction process for related process | (scheffer2023themysteryof pages 3-6) |
| high-pressure chamber / high-pressure culturing system | assay factor | OBI:0000711 specimen culturing (broad); label-only candidate for high-pressure chamber | (scheffer2023themysteryof pages 15-16, scheffer2023themysteryof pages 1-2, malas2024biologicalfunctionsat pages 1-2) |
| growth under controlled pressure cultivation | assay factor | OBI:0000011 planned process; label-only candidate | (scheffer2023themysteryof pages 6-7, zheng2023mechanismsofnucleic pages 14-16) |
| membrane lipid unsaturation | membrane feature | GO:0006636 unsaturated fatty acid biosynthetic process; CHEBI:35567 unsaturated fatty acid | (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4, zheng2023mechanismsofnucleic pages 7-11) |
| branched-chain fatty acids | membrane feature | CHEBI:35819 branched-chain fatty acid | (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 4-6) |
| polyunsaturated fatty acids (PUFAs) | membrane feature | CHEBI:59549 polyunsaturated fatty acid | (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4) |
| eicosapentaenoic acid (C20:5) | metabolite | CHEBI:28694 | (tamby2023microbialmembranelipid pages 4-6, tamby2023microbialmembranelipid pages 2-4) |
| docosahexaenoic acid (C22:6) | metabolite | CHEBI:28814 | (tamby2023microbialmembranelipid pages 4-6, tamby2023microbialmembranelipid pages 2-4) |
| phosphatidylethanolamine (PE) | membrane feature | CHEBI:16038 phosphatidylethanolamine | (scheffer2023themysteryof pages 9-10, zheng2023mechanismsofnucleic pages 7-11) |
| phosphatidylglycerol (PG) | membrane feature | CHEBI:17517 phosphatidylglycerol | (scheffer2023themysteryof pages 9-10, zheng2023mechanismsofnucleic pages 7-11) |
| phosphatidylcholine (PC) | membrane feature | CHEBI:64482 phosphatidylcholine | (zheng2023mechanismsofnucleic pages 7-11) |
| phosphatidylserine (PS) | membrane feature | CHEBI:18303 phosphatidylserine | (zheng2023mechanismsofnucleic pages 7-11) |
| cardiolipin | membrane feature | CHEBI:28494 cardiolipin | (zheng2023mechanismsofnucleic pages 11-12) |
| pfa operon | gene/protein | label-only candidate | (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 9-10) |
| δ-9-acyl-phospholipid desaturase | gene/protein | EC:1.14.19.- fatty acid desaturase (approximate); label-only candidate | (scheffer2023themysteryof pages 6-7) |
| compatible solute accumulation / piezolyte accumulation | process | GO:0006970 response to osmotic stress (related); label-only candidate for piezolyte accumulation | (scheffer2023themysteryof pages 9-10, qiu2024metabolicadaptationsof pages 11-12) |
| glutamate | metabolite | CHEBI:29985 L-glutamate | (scheffer2023themysteryof pages 9-10) |
| betaine | metabolite | CHEBI:17750 betaine | (scheffer2023themysteryof pages 9-10) |
| β-hydroxybutyrate | metabolite | CHEBI:87672 3-hydroxybutyrate | (scheffer2023themysteryof pages 9-10) |
| trimethylamine N-oxide (TMAO) | metabolite | CHEBI:15724 trimethylamine N-oxide | (scheffer2023themysteryof pages 9-10, qiu2024metabolicadaptationsof pages 1-2) |
| proline | metabolite | CHEBI:26271 L-proline | (qiu2024metabolicadaptationsof pages 11-12) |
| intracellular osmotic pressure | process | label-only candidate | (zheng2023mechanismsofnucleic pages 7-11, zheng2023mechanismsofnucleic pages 11-12, zheng2023mechanismsofnucleic pages 1-3) |
| metal ABC transporter | gene/protein | GO:0042626 ATPase-coupled transmembrane transporter activity | (zheng2023mechanismsofnucleic pages 7-11, zheng2023mechanismsofnucleic pages 5-7) |
| heavy metal translocating P-type ATPase | gene/protein | GO:0019829 cation-transporting ATPase activity | (zheng2023mechanismsofnucleic pages 7-11, zheng2023mechanismsofnucleic pages 5-7) |
| calcium/sodium antiporter | gene/protein | GO:0015081 sodium ion transmembrane transporter activity; GO:0015085 calcium ion transmembrane transporter activity | (zheng2023mechanismsofnucleic pages 7-11, zheng2023mechanismsofnucleic pages 5-7) |
| toxR regulon | gene/protein | label-only candidate | (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7) |
| OmpH porin | gene/protein | label-only candidate; GO:0015288 porin activity (related) | (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7) |
| motility | process | GO:0048870 cell motility | (scheffer2023themysteryof pages 1-2, scheffer2023themysteryof pages 6-7) |
| chemotaxis | process | GO:0006935 chemotaxis | (scheffer2023themysteryof pages 3-6, scheffer2023themysteryof pages 6-7) |
| methyl-accepting chemotaxis protein (MCP) | gene/protein | label-only candidate; GO:0004888 transmembrane signaling receptor activity (related) | (scheffer2023themysteryof pages 6-7) |
| CheA/CheC/CheD chemotaxis proteins | gene/protein | label-only candidates | (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 3-6) |
| flagellar apparatus / flagellar biosynthesis | complex | GO:0009288 bacterial-type flagellum assembly | (scheffer2023themysteryof pages 6-7) |
| FlaB3 | gene/protein | label-only candidate | (scheffer2023themysteryof pages 6-7) |
| FliD | gene/protein | label-only candidate | (scheffer2023themysteryof pages 6-7) |
| FliA | gene/protein | label-only candidate | (scheffer2023themysteryof pages 6-7) |
| heat shock proteins | gene/protein | GO:0009408 response to heat; label-only candidate for HSP family | (scheffer2023themysteryof pages 1-2, tamby2023microbialmembranelipid pages 1-2) |
| cold shock protein CspG | gene/protein | label-only candidate | (malas2024biologicalfunctionsat pages 1-2) |
| antioxidant defense genes | process | GO:0016209 antioxidant activity | (malas2024biologicalfunctionsat pages 1-2) |
| arginine biosynthesis | process | GO:0006526 arginine biosynthetic process | (malas2024biologicalfunctionsat pages 1-2) |
| argA | gene/protein | label-only candidate; KEGG ortholog candidate | (malas2024biologicalfunctionsat pages 1-2) |
| argB | gene/protein | label-only candidate; KEGG ortholog candidate | (malas2024biologicalfunctionsat pages 1-2) |
| argC | gene/protein | label-only candidate; KEGG ortholog candidate | (malas2024biologicalfunctionsat pages 1-2) |
| argF | gene/protein | label-only candidate; KEGG ortholog candidate | (malas2024biologicalfunctionsat pages 1-2) |
| 16S rRNA loop-stem length / ribosomal structural adaptation | process | label-only candidate; GO:0005840 ribosome (related complex) | (scheffer2023themysteryof pages 10-12) |


*Table: This table lists candidate nodes for a causal graph of microbial pressure optimum, grouped by biological and experimental type. It is useful for TraitMech curation because it consolidates evidence-backed entities with tentative ontology grounding and direct context-ID citations.*

## 6. Candidate causal edges (triples) with evidence snippets and curation notes

| Edge (subject–predicate–object) | Proposed node grounding (CURIEs where possible) | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|
| Increased membrane unsaturated fatty acids/PUFAs — enables — growth at elevated hydrostatic pressure / higher pressure optimum | subject: CHEBI:35567 unsaturated fatty acid; CHEBI:59549 polyunsaturated fatty acid; process: GO:0006629 lipid metabolic process; object: METPO:traitmech:000004 pressure optimum | “the abundance of specific membrane lipids, such as those containing unsaturated and branched-chain fatty acids, rises with increasing HHP” (tamby2023microbialmembranelipid pages 1-2) | 10.3389/fmolb.2022.1058381, 2023, https://doi.org/10.3389/fmolb.2022.1058381 | Broad review-level support for membrane adaptation under pressure; supports causal relevance but not a single universal mechanism across taxa. |
| Increased C20:5/C22:6 PUFA content — associated_with / may_contribute_to — growth under HHP and strain-specific pressure optima | subject: CHEBI:28694 eicosapentaenoic acid; CHEBI:28814 docosahexaenoic acid; object: METPO:traitmech:000004 | “significantly increased the content of C20:5 and C22:6 under HHP” and table lists optima such as “5°C—40 MPa” and “10°C—70 MPa” for piezophiles (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid pages 4-6) | 10.3389/fmolb.2022.1058381, 2023, https://doi.org/10.3389/fmolb.2022.1058381 | Mostly associative/strain-level evidence; responses differ by species (e.g., some Shewanella decrease C20:5), so curate as uncertain and taxon-specific. |
| pfa operon — increases — ω-3 PUFA synthesis | subject: label-only candidate “pfa operon”; product: CHEBI:59549 polyunsaturated fatty acid | “the ‘pfa operon’ … role of the ‘pfa operon’ and a ‘δ-9-acyl-phospholipid-desaturase’” in membrane remodeling under pressure/cold conditions (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Mechanistically plausible and widely cited, but review notes mutant evidence was not always pressure-sensitive; likely contributes via membrane composition, not directly to optimum in all taxa. |
| δ-9-acyl-phospholipid desaturase — increases — unsaturated fatty acid content | subject: EC:1.14.19.- fatty acid desaturase (approx.); label-only candidate “δ-9-acyl-phospholipid-desaturase”; object: CHEBI:35567 unsaturated fatty acid | “only piezophilic Colwellia possess a δ-9-acyl-phospholipid-desaturase” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Presence/absence association, not direct perturbation proof; taxon-specific and best marked uncertain. |
| Metal ABC transporters / P-type ATPase / Ca2+/Na+ antiporter — increases — intracellular cation concentration | subject: GO:0042626 ATPase-coupled transmembrane transporter activity; GO:0019829 cation-transporting ATPase activity; GO:0015081 sodium ion transmembrane transporter activity; GO:0015085 calcium ion transmembrane transporter activity | “upregulation of genes encoding metal ABC transporters, a heavy metal translocating P-type ATPase, and a calcium/sodium antiporter” and intracellular “Mg2+, K+, and Na+ concentrations were ~4–8× higher at 12 MPa” (zheng2023mechanismsofnucleic pages 7-11) | 10.1128/mbio.00958-23, 2023, https://doi.org/10.1128/mbio.00958-23 | Stronger causal chain within one taxon (Hujiaoplasma nucleasis zrk29) under 12 MPa vs 0.1 MPa; supports HHP tolerance more directly than numerical pressure optimum. |
| Increased intracellular cation concentration — increases — intracellular osmotic pressure | subject: CHEBI:29103 potassium(1+); CHEBI:32599 sodium(1+); CHEBI:6636 magnesium cation; process: GO:0006970 response to osmotic stress | “suggesting increased cation import… to increase intracellular osmotic pressure” (zheng2023mechanismsofnucleic pages 7-11, zheng2023mechanismsofnucleic pages 11-12) | 10.1128/mbio.00958-23, 2023, https://doi.org/10.1128/mbio.00958-23 | Mechanistic interpretation explicitly proposed by authors; suitable as candidate edge, though node “intracellular osmotic pressure” may be label-only unless mapped later. |
| Increased intracellular osmotic pressure — enables — HHP tolerance | subject: label-only candidate “intracellular osmotic pressure”; object: label-only candidate “high hydrostatic pressure tolerance” | “The proposed HHP-tolerance model involves (i) importing cations to raise intracellular osmotic pressure” (zheng2023mechanismsofnucleic pages 7-11) | 10.1128/mbio.00958-23, 2023, https://doi.org/10.1128/mbio.00958-23 | Good mechanistic edge for tolerance; indirect relation to pressure optimum, so curate with note that optimum is downstream phenotype. |
| Glutamate / betaine / β-hydroxybutyrate / proline / TMAO — promotes — protein stabilization by preferential hydration | subjects: CHEBI:29985 L-glutamate; CHEBI:17750 betaine; CHEBI:87672 3-hydroxybutyrate; CHEBI:26271 proline; CHEBI:15724 trimethylamine N-oxide; process: label-only candidate “preferential hydration” | “Compatible solutes help by displacing the water molecules bound to proteins… ‘preferential hydration’” and in P. profundum “glutamate, betaine, and β-hydroxybutyrate were detected when the organism was grown at 20 to 30 MPa” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Strong review support for compatible solutes/piezolytes; some solutes may also respond to salinity/temperature, so causal attribution to pressure alone requires controls. |
| Compatible solute accumulation — enables — pressure tolerance | subject: GO:0006970 response to osmotic stress; label-only candidate “piezolyte accumulation”; object: label-only candidate “high hydrostatic pressure tolerance” | “proline… consistent with osmolyte-based protection” and pressure-linked accumulation of glutamate/betaine/β-hydroxybutyrate/TMAO discussed for piezophiles (qiu2024metabolicadaptationsof pages 11-12, scheffer2023themysteryof pages 9-10) | 10.1007/s00253-023-12906-5, 2024, https://doi.org/10.1007/s00253-023-12906-5; 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Supported across taxa, but primarily for tolerance/survival rather than explicitly shifting optimum pressure. |
| toxR regulon — positively_regulates — ompH porin expression under pressure | subject: label-only candidate “toxR regulon”; object: label-only candidate “OmpH porin” | “OmpH: controlled by the toxR regulon and increasing ~10–100× when pressure rises from 0.1 MPa to 28 MPa” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Good regulatory edge from review summary; specific to taxa where OmpH/ToxR system is present. |
| OmpH porin expression — may_facilitate — growth at high pressure | subject: label-only candidate “OmpH porin”; object: METPO:traitmech:000004 pressure optimum | “pressure-regulated outer membrane porins (notably OmpH)” linked to membrane adaptation under pressure (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | More inferential than direct; use uncertain flag because expression is pressure-responsive but direct effect on optimum is not demonstrated here. |
| argA/argB/argC/argF — participates_in — HHP response | subject: KEGG ortholog candidates argA/argB/argC/argF; pathway: arginine biosynthesis | “Adaptations include upregulation of the genes argA, argB, argC, and argF involved in arginine biosynthesis” at 158 MPa (malas2024biologicalfunctionsat pages 1-2) | 10.3389/fmicb.2024.1293928, 2024, https://doi.org/10.3389/fmicb.2024.1293928 | Transcriptomic response in non-piezophile S. oneidensis under 158 MPa; supports HHP response, not necessarily stable shift in optimal growth pressure. |
| Cold-shock protein CspG / antioxidant defense genes — contributes_to — HHP survival | subject: UniProt/GO label-only candidate “CspG”; GO:0016209 antioxidant activity | “MR-1 also utilizes stress response adaptations… genes encoding for the cold-shock protein CspG and antioxidant defense related genes” (malas2024biologicalfunctionsat pages 1-2) | 10.3389/fmicb.2024.1293928, 2024, https://doi.org/10.3389/fmicb.2024.1293928 | Strong evidence for acute survival/viability at 158 MPa; not direct evidence for optimum pressure trait. |
| Motility/chemotaxis genes (MCP, CheA/C/D) — promotes — growth performance around/above pressure optimum | subject: GO:0006935 chemotaxis; GO:0001539 cilium or flagellum-dependent cell motility; label-only candidates MCP, CheA, CheC, CheD | “MCP and CheACD were upregulated above an optimal growth pressure of 28 MPa” (scheffer2023themysteryof pages 3-6, scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Pressure-responsive expression near optimum suggests adaptation; direction to optimum is plausible but not directly manipulated. |
| Flagellar biosynthesis genes (flaB3, fliD, fliA) — required_for — growth under high pressure | subject: UniProt/GO label-only candidates FlaB3, FliD, FliA; GO:0009288 bacterial-type flagellum assembly | “flagellar biosynthesis genes essential for growth under high pressure” and mutants “were non-motile and had reduced growth when exposed to high pressure” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Stronger functional evidence than correlation; still taxon-specific and connects to high-pressure growth rather than measured optimum per se. |
| 16S rRNA structural features (longer loop stems) — correlated_with — optimal growth pressure | subject: RNAcentral/GO label-only candidate “16S rRNA loop-stem length”; object: METPO:traitmech:000004 pressure optimum | “Ribosomal adaptations (longer loop stems in 16S rRNA) correlate strongly with optimal growth pressure (r2 = 0.97)” (scheffer2023themysteryof pages 10-12) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 | Explicitly correlation, not causation; useful as candidate biomarker node but should not be curated as a causal edge without stronger perturbation evidence. |


*Table: This table summarizes candidate mechanistic edges for curating a causal graph of microbial pressure optimum. It distinguishes stronger causal evidence from correlations or taxon-specific inferences and includes provisional ontology grounding where possible.*

## 7. Warnings / claims not yet ready for TraitMech curation

1. **Do not treat “survival at extreme pressure” as equivalent to “pressure optimum”.** Transcriptomic survival at 158 MPa in MR‑1 is informative for mechanisms but does not establish a new optimum pressure trait (malas2024biologicalfunctionsat pages 1-2).
2. **Temperature/salinity confounding**: Compatible solute accumulation and lipid remodeling can respond to salinity and temperature as well as pressure; edges should often be contextualized as “under HHP (and temperature X) in assay Y” unless pressure-only controls are available (scheffer2023themysteryof pages 9-10).
3. **Correlation-only biomarker edges**: The 16S rRNA loop-stem length association with optimal growth pressure is explicitly correlational; curate only as a candidate biomarker node/association unless perturbation evidence is added (scheffer2023themysteryof pages 10-12).
4. **Taxon-specific lipid mechanisms**: Some taxa show opposite PUFA trends (e.g., strain-to-strain differences in C20:5 directionality), so “PUFA increase → higher pressure optimum” should be marked **uncertain** unless linked to a specific organism/experiment (tamby2023microbialmembranelipid pages 2-4).
5. **Preprints**: The 2024 bioRxiv hypothesis about electrostatic interactions in Colwellia proteins is useful for hypothesis generation but should be treated as lower-confidence for curation until peer reviewed and/or experimentally validated (makhatadze2024modulationofelectrostatic pages 6-8).

## 8. DOI-first bibliography (with URLs and dates)

| Citation (short) | Publication date | DOI | URL | Notes on relevance |
|---|---|---|---|---|
| Scheffer & Gieg, *Microorganisms* | Jun 2023 | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Core scope/definition source: defines non-piezophile, piezosensitive, and piezophile by growth optimum; summarizes assay constraints, co-stress confounding, quantitative context (>80 isolates by Mar 2021; ~10–100 MPa deep-sea range), and mechanisms including membrane unsaturation, motility, heat-shock proteins, osmolytes, outer-membrane proteins, and ribosomal features (scheffer2023themysteryof pages 1-2, scheffer2023themysteryof pages 3-6, scheffer2023themysteryof pages 9-10) |
| Tamby et al., *Frontiers in Molecular Biosciences* | Jan 2023 | 10.3389/fmolb.2022.1058381 | https://doi.org/10.3389/fmolb.2022.1058381 | Best recent membrane-focused review for curation: explains homeoviscous adaptation under HHP and provides a strain-level table of pressure optima (e.g., 20–70 MPa) with associated lipid changes such as increased unsaturated/branched fatty acids and PUFAs including C20:5 and C22:6 (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 4-6, tamby2023microbialmembranelipid pages 2-4) |
| Zheng et al., *mBio* | Aug 2023 | 10.1128/mbio.00958-23 | https://doi.org/10.1128/mbio.00958-23 | Strong mechanistic case study in a deep-sea wall-less bacterium: at 12 MPa vs 0.1 MPa, transcriptomics/lipidomics support a cation-import plus osmotic-pressure model and increased unsaturated phospholipid chains for HHP tolerance; includes metal ABC transporters, P-type ATPase, Ca/Na antiporter, and 4–8× higher intracellular Mg2+/K+/Na+ (zheng2023mechanismsofnucleic pages 7-11, zheng2023mechanismsofnucleic pages 14-16, zheng2023mechanismsofnucleic pages 11-12, zheng2023mechanismsofnucleic pages 5-7) |
| Malas et al., *Frontiers in Microbiology* | Feb 2024 | 10.3389/fmicb.2024.1293928 | https://doi.org/10.3389/fmicb.2024.1293928 | Recent high-pressure transcriptomics study relevant to upper pressure limits and acute HHP response: *Shewanella oneidensis* MR-1 remained metabolically active and viable after 2 h at 158 MPa; 264 genes responded, including argA/B/C/F, membrane reconfiguration functions, CspG, and antioxidant defenses; cites 140 MPa as demonstrated growth limit in prior literature (malas2024biologicalfunctionsat pages 1-2) |
| Qiu et al., *Applied Microbiology and Biotechnology* | Jan 2024 | 10.1007/s00253-023-12906-5 | https://doi.org/10.1007/s00253-023-12906-5 | 2024 metabolomics/proteomics study of pressure adaptation in *Microbacterium sediminis* YLB-01 under 30 MPa at 4 °C for 7 days; useful for candidate nodes involving proline/compatible solutes, carbohydrate rewiring, UDP-glucose-linked cell-wall synthesis, and membrane/lipid remodeling under HHP (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 11-12) |
| Makhatadze, *bioRxiv* (preprint) | Jul 2024 | 10.1101/2024.07.28.605522 | https://doi.org/10.1101/2024.07.28.605522 | Optional, lower-curation-confidence source: proposes electrostatic-interaction modulation as a cryptic adaptation in piezophilic *Colwellia* proteins; useful mainly for hypothesis generation on proteome-level adaptation, not for strong TraitMech causal edges yet (makhatadze2024modulationofelectrostatic pages 6-8) |


*Table: This table compiles the main papers used to support the pressure-optimum curation report, with DOI-first citations, URLs, publication dates, and concise notes on why each source is useful for trait scope or candidate mechanisms.*


References

1. (scheffer2023themysteryof pages 1-2): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

2. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

3. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

4. (scheffer2023themysteryof pages 15-16): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

5. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

6. (tamby2023microbialmembranelipid pages 2-4): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

7. (scheffer2023themysteryof pages 10-12): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

8. (zheng2023mechanismsofnucleic pages 7-11): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 16 citations and is from a domain leading peer-reviewed journal.

9. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

10. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

11. (scheffer2023themysteryof pages 3-6): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

12. (tamby2023microbialmembranelipid pages 4-6): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

13. (qiu2024metabolicadaptationsof pages 1-2): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 9 citations and is from a domain leading peer-reviewed journal.

14. (qiu2024metabolicadaptationsof pages 11-12): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 9 citations and is from a domain leading peer-reviewed journal.

15. (zheng2023mechanismsofnucleic pages 14-16): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 16 citations and is from a domain leading peer-reviewed journal.

16. (zheng2023mechanismsofnucleic pages 11-12): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 16 citations and is from a domain leading peer-reviewed journal.

17. (zheng2023mechanismsofnucleic pages 1-3): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 16 citations and is from a domain leading peer-reviewed journal.

18. (zheng2023mechanismsofnucleic pages 5-7): Rikuan Zheng, Chong Wang, Ruining Cai, Yeqi Shan, and Chaomin Sun. Mechanisms of nucleic acid degradation and high hydrostatic pressure tolerance of a novel deep-sea wall-less bacterium. mBio, Aug 2023. URL: https://doi.org/10.1128/mbio.00958-23, doi:10.1128/mbio.00958-23. This article has 16 citations and is from a domain leading peer-reviewed journal.

19. (makhatadze2024modulationofelectrostatic pages 6-8): George I. Makhatadze. Modulation of electrostatic interactions as a mechanism of cryptic adaptation of colwellia to high hydrostatic pressure. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.28.605522, doi:10.1101/2024.07.28.605522. This article has 1 citations.