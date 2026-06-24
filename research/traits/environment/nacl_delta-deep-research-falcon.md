---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:53:41.251240'
end_time: '2026-06-17T23:07:10.429476'
duration_seconds: 809.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta
  trait_identifier: METPO:1000335
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A salinity phenotype with numerical limits expressing the breadth (maximum
    minus minimum) of NaCl concentrations supporting growth of an organism.
  parent_traits: METPO:1000532, METPO:1000534
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta)
    reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2:
    cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive
    capacity as the basis of a wide NaCl-delta phenotype.)'
  causal_graph_summary: 'nacl_delta_euryhaline_breadth: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta
- **METPO identifier:** METPO:1000335
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits expressing the breadth (maximum minus minimum) of NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta) reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive capacity as the basis of a wide NaCl-delta phenotype.)
- **Existing causal graph summary:** nacl_delta_euryhaline_breadth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta.yaml`.

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
- **Trait label:** NaCl delta
- **METPO identifier:** METPO:1000335
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits expressing the breadth (maximum minus minimum) of NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta) reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive capacity as the basis of a wide NaCl-delta phenotype.)
- **Existing causal graph summary:** nacl_delta_euryhaline_breadth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta.yaml`.

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


## Microbial Trait Causal Graph Research Report: **NaCl delta** (METPO:1000335)

### Scope summary (curation-oriented)
**NaCl delta** is a *salinity phenotype with numerical limits* representing the **breadth of NaCl concentrations that support growth**, operationally: **(maximum NaCl supporting growth) − (minimum NaCl supporting growth)**. It is best interpreted as a *growth-supporting tolerance range*, not a single-point optimum. A closely related operationalization used in microbial ecology is **salinity niche breadth**, where breadth is derived from fitted growth/fitness curves across a NaCl gradient and can be split into **hypo-osmotic vs hyper-osmotic** sides around the optimum (rain‐franco2022nichebreadthaffects pages 3-3, rain‐franco2022nichebreadthaffects media 2b3f4334).

**What the trait is not**: 
- Not the *optimal* NaCl concentration for growth (a separate phenotype).
- Not necessarily the *maximum* NaCl survival limit (survival can exceed growth-supporting capacity).
- Not equivalent to “halophile/halotolerant class” labels; those are coarse and may be based on optima rather than growth-supporting min/max (van2009productionofpoly pages 13-16).

**Boundary cases to flag during curation**:
- **Assay dependence**: medium composition (osmoprotectants present/absent), growth endpoint definition (OD threshold vs colony formation), incubation time, and temperature can shift apparent min/max, and thus NaCl delta (rain‐franco2022nichebreadthaffects pages 2-3, rain‐franco2022nichebreadthaffects pages 3-3).
- **Asymmetry**: organisms can have different tolerance on the low- vs high-salt side; a single delta may hide this (rain‐franco2022nichebreadthaffects pages 3-3).

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Osmoadaptation strategies relevant to NaCl delta
Two broad microbial strategies shape the range of salinities supporting growth:

1) **“Salt-in” strategy**: maintain osmotic balance by accumulating inorganic ions (often **KCl**) inside the cytoplasm. In haloarchaea this is described as accumulating intracellular KCl roughly equal to external NaCl, enabled by extensive K+ uptake and active Na+ efflux systems (najjari2023physiologicalandgenomic pages 1-2). Salt-in is generally favored at *very high salt* because it is comparatively less energetically demanding than synthesizing large pools of organic solutes (bonnaud2024haloarchaeaaspromising pages 2-4).

2) **“Salt-out” (compatible-solute) strategy**: keep cytoplasmic inorganic ion levels lower and balance osmotic pressure using **organic compatible solutes** (e.g., glycine betaine, trehalose, ectoine, proline). This strategy relies on uptake and/or de novo synthesis of these solutes (bonnaud2024haloarchaeaaspromising pages 2-4, zeaiter2019phenomicsandgenomics pages 1-2).

### 1.2 Ion transport, compatible solutes, and regulatory control
A mechanistic framing particularly useful for TraitMech is a **two-stage osmotic response**:
- **Rapid stage**: upon hyperosmotic shock, cells quickly import **K+** (often using glutamate as counterion) as an immediate osmotic response; K+ is a major cytoplasmic cation and typical cytoplasmic K+ concentrations are reported around ~250 mM (E. coli), ~300 mM (B. subtilis), and ~500 mM (C. glutamicum, L. lactis) (foster2024bacterialcellvolume pages 6-8).
- **Secondary stage**: to avoid K+-associated cytotoxicity/high ionic strength, microbes accumulate/synthesize **neutral compatible solutes** such as **glycine betaine, trehalose, ectoine, and proline** (foster2024bacterialcellvolume pages 6-8).

A key modern regulatory concept is that **cyclic di-AMP (c-di-AMP)** acts as a “master regulator” of **cell volume control** in many bacteria by regulating ion homeostasis (especially K+ transport); both deficiency and excess can impair viability (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 6-8).

### 1.3 Quantifying “breadth”: niche breadth vs NaCl delta
Rain‑Franco et al. (2022) provide a concrete quantitative approach: fit a **fitness curve** across a NaCl gradient and define niche breadth as the **salinity range (g/L NaCl) where normalized fitness ≥ 50% of maximum**, including separate hypo- and hyper-osmotic components when curves are asymmetric (rain‐franco2022nichebreadthaffects pages 3-3). This is directly aligned with curating NaCl delta as a *numerical breadth*, while also suggesting an optional decomposition into low-salt vs high-salt sides.

A cropped table from this study summarizes strain-level quantitative NB parameters (optimum and breadth descriptors), useful as a template for representing range-like phenotypes:

(rain‐franco2022nichebreadthaffects media 2b3f4334)

---

## 2) Recent developments & latest research (prioritize 2023–2024)

### 2.1 c-di-AMP and quantitative cell-volume/osmotic control (2024)
A 2024 Microbiology and Molecular Biology Reviews article synthesizes evidence that **c-di-AMP controls K+ transport and cell volume**, connecting second-messenger signaling directly to osmotic fitness across changing external osmolarity (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 6-8). This is a mechanistic “hub” for NaCl delta because robust regulation of ion import/export is a prerequisite for growth across broad NaCl ranges.

### 2.2 Hybrid salt-in/salt-out strategies under fluctuating salinity (2024)
A 2024 Frontiers in Microbiomes study on Dead Sea spring biofilms reports that **extreme ambient salinity fluctuations** select for organisms whose genomes encode **both salt-in and salt-out** elements, proposing a “scalable” response to variable salinity intensity (bonnaud2024haloarchaeaaspromising pages 2-4). This supports treating NaCl delta as not only “how much salt can be tolerated,” but also as potentially shaped by *environmental variability*.

### 2.3 Engineering salt tolerance and its measurable effect on maximum NaCl (2024)
A 2024 experimental engineering study in *Pseudomonas putida* KT2440 provides direct quantitative evidence that manipulating ion export and osmolyte biosynthesis can increase the **maximum NaCl supporting growth**:
- Wild-type tolerance reported as **4% w/v NaCl** in minimal salts medium.
- Co-expression of an **E. coli Na+/H+ antiporter (EcnhaA)** and **betaine-aldehyde dehydrogenase (betB)** increased maximum tolerance to **5% w/v NaCl**.
- Adding compatible solutes (**betaine + proline**) further increased tolerance to **6% w/v NaCl** (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14).

These are directly usable quantitative benchmarks for edges linking specific genes to the “upper bound” component of NaCl delta.

### 2.4 Haloarchaea as industrial chassis and osmoadaptation as a design constraint (2024)
A 2024 review argues haloarchaea could be promising chassis for industrial biocatalysis/green chemistry, summarizing osmoadaptation mechanisms (Na+/H+ antiporters for Na+ exclusion, K+ uptake, Cl− transport systems, mechanosensitive channels as safety valves) and emphasizing that **salt-out is energetically costly** and thus less suited to saturating salinities compared with salt-in (bonnaud2024haloarchaeaaspromising pages 2-4). This supports mechanistic prioritization when predicting or engineering NaCl delta.

---

## 3) Current applications and real-world implementations

### 3.1 Bioremediation/bioconversion in saline wastewater (engineered strain example)
The engineered *P. putida* KT2440-EcnhaA-betB strain demonstrates a direct application: degradation of aromatic pollutants under saline conditions where the wild type fails. The study reports biodegradation in minimal salt medium at **4% w/v NaCl** within **48 h**, positioning improved NaCl tolerance as enabling function in high-salinity bioremediation contexts (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 2-3).

### 3.2 Genomics-driven discovery of halophiles and inference of osmoadaptation mode
Genome mining in halophiles/hypersaline-soil isolates routinely uses presence of **ectoine and glycine betaine** synthesis/transport genes to infer a compatible-solute (salt-out) strategy (zeaiter2019phenomicsandgenomics pages 1-2). This is a real-world implementation relevant to curating NaCl delta: genomic evidence can motivate candidate nodes/edges but should be flagged as inferential unless growth-range assays exist.

---

## 4) Expert opinions and authoritative synthesis (what experts emphasize)

### 4.1 Osmotic fitness is a systems property, not a single gene
A major theme from authoritative synthesis is that osmoadaptation is an integrated system spanning:
- **Rapid ion fluxes** (especially K+ uptake) and tight regulation.
- Transition to **compatible solute accumulation** to reduce cytotoxic ionic strength.
- “Safety valves” including **mechanosensitive channels** for sudden downshock.
- **Second messenger control** (c-di-AMP) coordinating transporters and cell-volume constraints.

This integrated view motivates curating NaCl delta as a “TraitMech” graph involving multiple interacting modules rather than a single determinant (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4).

### 4.2 Strategy-level perspective: limits at very high salinity
At very high salinity, expert reviews emphasize that the **salt-in strategy** is favored relative to salt-out because maintaining huge pools of organic osmolytes is energetically expensive; thus, strategy choice influences the feasible **upper bound** of growth-supporting salinity (bonnaud2024haloarchaeaaspromising pages 2-4).

---

## 5) Relevant statistics and data points (recent/quantitative)

### 5.1 Quantitative measurement of breadth (NB as half-max range)
- NaCl gradients used: **10–100 g/L NaCl** (10, 20, …, 100), with growth monitored by OD600 and fitness defined as (max density × growth rate). Niche breadth is defined as the **range where normalized fitness ≥ 50% of max**, optionally decomposed into hypo- vs hyper-osmotic sides (rain‐franco2022nichebreadthaffects pages 2-3, rain‐franco2022nichebreadthaffects pages 3-3).

### 5.2 Quantitative osmotic physiology constraints
- Hyperosmotic shock can cause rapid water efflux and major cell-volume decrease (review-level mechanistic quantitation). Cytoplasmic K+ concentrations typically reported near **~250–500 mM** across model bacteria, reflecting the magnitude of ionic adjustment involved (foster2024bacterialcellvolume pages 6-8).

### 5.3 Quantitative engineered improvement of NaCl tolerance (2024)
- *P. putida* KT2440: max tolerance **4% → 5% w/v NaCl** with **EcnhaA + betB**, and **to 6% w/v** with added **betaine + proline** (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 8-10).

### 5.4 Quantitative extremophile survival capacity (archaea)
- *Natrinema altunense* 4.1R: reported ability to “survive up to **36% salinity**” (note: survival vs growth should be clarified before mapping directly to NaCl delta) (najjari2023physiologicalandgenomic pages 1-2).

---

# Candidate causal-graph nodes for `nacl_delta.yaml`

## A) Trait/phenotype nodes
- **NaCl delta** (METPO:1000335)
- Candidate subtraits (if TraitMech allows decomposition):
  - “minimum NaCl supporting growth” (label-only)
  - “maximum NaCl supporting growth” (label-only)
  - “hypo-osmotic growth breadth” (label-only; derived) (rain‐franco2022nichebreadthaffects pages 3-3)
  - “hyper-osmotic growth breadth” (label-only; derived) (rain‐franco2022nichebreadthaffects pages 3-3)

## B) Environmental / experimental factor nodes
- Salinity (NaCl concentration; assay variable) (rain‐franco2022nichebreadthaffects pages 2-3)
- Hyperosmotic upshift / hypoosmotic downshift (label-only) (foster2024bacterialcellvolume pages 6-8, bonnaud2024haloarchaeaaspromising pages 2-4)
- Fluctuating environmental salinity regime (e.g., Dead Sea springs) (bonnaud2024haloarchaeaaspromising pages 2-4)
- Medium osmoprotectant availability (betaine/proline supplementation) (fan2024improvementinsalt pages 1-2)

## C) Processes / pathways
- Osmoadaptation / response to osmotic stress (GO:0006970) (foster2024bacterialcellvolume pages 6-8)
- Salt-in strategy (label-only) (najjari2023physiologicalandgenomic pages 1-2)
- Salt-out strategy / compatible-solute strategy (label-only) (bonnaud2024haloarchaeaaspromising pages 2-4, zeaiter2019phenomicsandgenomics pages 1-2)
- Cell volume homeostasis (label-only; c-di-AMP-associated) (foster2024bacterialcellvolume pages 1-2)

## D) Genes/proteins/complexes (candidate mechanistic nodes)
- **Na+/H+ antiporters**: NhaA-family; NhaB; (E. coli EcnhaA as heterologous antiporter used experimentally) (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14)
- **K+ uptake systems**: KdpFABC and regulator KdpDE; TrkAH/KtrAB/KtrCD; KimA (foster2024bacterialcellvolume pages 1-2, foster2024bacterialcellvolume pages 6-8)
- **Mechanosensitive channels**: MscL, MscS (bonnaud2024haloarchaeaaspromising pages 2-4, thompson2024themicrobiomeof pages 5-6)
- **Second messenger**: cyclic di-AMP (label-only chemical node) (foster2024bacterialcellvolume pages 1-2)

## E) Compatible solute molecules and biosynthesis genes
- Glycine betaine (CHEBI:17750); betA/betB; (betB used experimentally) (fan2024improvementinsalt pages 8-10, fan2024improvementinsalt pages 1-2)
- Trehalose (CHEBI:30911); otsA/otsB; tre pathways (najjari2023physiologicalandgenomic pages 1-2, thompson2024themicrobiomeof pages 5-6)
- Ectoine (CHEBI:17244); ectABC; (ectoine/GB genes used to infer salt-out) (zeaiter2019phenomicsandgenomics pages 1-2, thompson2024themicrobiomeof pages 5-6)
- Proline (CHEBI:26271 / CHEBI:27698); supplementation as osmoprotection (fan2024improvementinsalt pages 1-2)

---

# Evidence-backed candidate causal edges (triples)
The table below is structured for direct translation into TraitMech-style YAML edges.

| Edge (subject—predicate—object) | Evidence snippet (quote) | Notes/interpretation (including uncertainty) | Suggested ontology grounding (CURIEs for subject/object where feasible) | Source (DOI, year, URL) |
|---|---|---|---|---|
| c-di-AMP — negatively_regulates — K+ import systems | “high intracellular c-di-AMP reduces K+ import” and the review lists “c-di-AMP-dependent potassium transporters (KtrAB/TrkAH, KimA)” plus “the high-affinity K+ uptake system KdpFABC” among primary osmotic-response systems (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 1-2) | Strong review-level support that c-di-AMP modulates K+ uptake capacity, which is mechanistically relevant to growth across changing NaCl. Edge is broad across bacteria using c-di-AMP, not universal to all microbes. | subject: candidate node “cyclic di-AMP”; object: KEGG/label nodes “KtrAB”, “TrkAH”, “KimA”, “KdpFABC”; process: GO:0006813 potassium ion transport | DOI:10.1128/MMBR.00181-23, 2024, https://doi.org/10.1128/MMBR.00181-23 |
| c-di-AMP — regulates — cell volume homeostasis | “we argue that cyclic di-AMP is a master regulator of cell volume” and “both the lack and overproduction of cyclic di-AMP affect viability” (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 1-2) | Strong review evidence. Cell-volume control is an intermediate mechanism linking osmotic transitions to NaCl breadth, rather than a direct trait measurement. | subject: candidate node “cyclic di-AMP”; object: GO:0005623 cell / candidate process “cell volume homeostasis” | DOI:10.1128/MMBR.00181-23, 2024, https://doi.org/10.1128/MMBR.00181-23 |
| Hyperosmotic upshift — causes — K+ uptake | “cells import large amounts of K+ during osmotic upshift” and potassium is “the principal cytoplasmic cation” (foster2024bacterialcellvolume pages 6-8) | Strong mechanistic support. This is a generic osmoadaptive edge explaining rapid tolerance to increased NaCl; by itself it does not prove broader NaCl delta without downstream regulation/compatibility. | subject: ENVO/candidate “hyperosmotic stress”; object: GO:0006813 potassium ion transport / candidate transporters KtrAB, TrkAH, KdpFABC | DOI:10.1128/MMBR.00181-23, 2024, https://doi.org/10.1128/MMBR.00181-23 |
| K+ uptake — contributes_to — osmoadaptation | The review notes K+ import during osmotic upshift, with cytoplasmic K+ levels around “~250 mM in E. coli; ~300 mM in B. subtilis; ~500 mM in C. glutamicum and L. lactis” (foster2024bacterialcellvolume pages 6-8) | Quantitative support that K+ accumulation is a core early osmoadaptive response. Likely broad but not sufficient alone for wide NaCl delta because excess K+ is cytotoxic and often replaced/augmented by compatible solutes. | subject: GO:0006813 potassium ion transport; object: GO:0006970 response to osmotic stress | DOI:10.1128/MMBR.00181-23, 2024, https://doi.org/10.1128/MMBR.00181-23 |
| Compatible solute accumulation — enables — osmoadaptation | “To avoid K+-induced cytotoxicity and high ionic strength, cells accumulate or synthesize neutral compatible solutes (e.g., glycine betaine, trehalose, ectoine, proline)” (foster2024bacterialcellvolume pages 6-8) | Strong review-level support for a central causal mechanism behind broader NaCl-supporting growth ranges. This is one of the most curation-ready generic edges. | subject: candidate process “compatible solute accumulation”; object: GO:0006970 response to osmotic stress; chemicals: CHEBI:17750 glycine betaine, CHEBI:30911 trehalose, CHEBI:27698 L-proline, CHEBI:17244 ectoine | DOI:10.1128/MMBR.00181-23, 2024, https://doi.org/10.1128/MMBR.00181-23 |
| Glycine betaine biosynthesis/accumulation — increases — salt tolerance | “betAB were involved in glycine-betaine biosynthesis” and “glycine-betaine was a major osmolyte for strain KT2440”; overexpression of betB caused “a significant increase in the biomass to 1.12” under salt (fan2024improvementinsalt pages 8-10, fan2024improvementinsalt pages 1-2) | Direct experimental support in Pseudomonas putida KT2440. Taxon-specific but strong for a gene-to-phenotype edge. | subject: betB (betaine-aldehyde dehydrogenase), candidate betA; object: CHEBI:17750 glycine betaine / METPO:1000335 NaCl delta | DOI:10.3390/biology13060404, 2024, https://doi.org/10.3390/biology13060404 |
| Trehalose biosynthesis — contributes_to — osmoprotection | The halophilic archaeon study defines salting-out as using organic solutes such as “sugars (sucrose and trehalose)” and notes “trehalose-6-phosphate synthase OtsA and trehalose-phosphatase OtsB” (najjari2023physiologicalandgenomic pages 1-2); Thompson et al. list “otsA/otsB, treY/treZ, treS, treP” in osmoprotection-associated isolates (thompson2024themicrobiomeof pages 5-6) | Good mechanistic support, but direct linkage to NaCl delta breadth is somewhat inferred unless measured in the same strain. | subject: otsA/otsB pathway; object: CHEBI:30911 trehalose / GO:0006970 response to osmotic stress | DOI:10.1007/s10709-023-00182-0, 2023, https://doi.org/10.1007/s10709-023-00182-0; DOI:10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 |
| Ectoine biosynthesis/uptake — contributes_to — salt-out osmoadaptation | “harbor the genes for biosynthesis and transport of the compatible solutes ectoine and glycine betaine” (zeaiter2019phenomicsandgenomics pages 1-2); “Ectoine is a prominent member of these types of stress protectants” (van2009productionofpoly pages 13-16); Thompson et al. detected “ectABC… ectT… ehuABCD” (thompson2024themicrobiomeof pages 5-6) | Strong multi-source support. Genomic presence often indicates capacity, but phenotype should be confirmed per taxon when possible. | subject: ectABC / EctB / ectT / ehuABCD; object: CHEBI:17244 ectoine / GO:0006970 response to osmotic stress | DOI:10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059; DOI:10.3389/fmicb.2019.02811, 2019, https://doi.org/10.3389/fmicb.2019.02811; DOI:10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 |
| Proline accumulation/supplementation — increases — NaCl tolerance | In engineered P. putida, “Further addition of betaine and proline improved the salt tolerance of the engineered strain to 6% w/v NaCl” (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 10-12) | Direct experimental support, but this is supplementation-dependent and assay-specific. Curate as environmental/assay-mediated edge, not constitutive genetic mechanism alone. | subject: CHEBI:26271 proline / CHEBI:27698 L-proline; object: METPO:1000335 NaCl delta | DOI:10.3390/biology13060404, 2024, https://doi.org/10.3390/biology13060404 |
| Na+/H+ antiporter activity — improves_growth_at — high NaCl | In KT2440, “EcnhaA from E. coli significantly increased the growth of the strain KT2440 in 4% w/v NaCl” and “nhaA-II was upregulated ~7.429-fold” with slight improvement on overexpression (fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 8-10, fan2024improvementinsalt pages 1-2) | Strong experimental evidence for antiporter-mediated salt tolerance improvement. EcnhaA result is heterologous engineering; endogenous nhaA-II effect appears weaker. | subject: NhaA-family Na+/H+ antiporter / EcnhaA; object: GO:0015385 sodium:proton antiporter activity / METPO:1000335 NaCl delta | DOI:10.3390/biology13060404, 2024, https://doi.org/10.3390/biology13060404 |
| co-expression of EcnhaA and betB — increases — maximum NaCl tolerance | “co-expression of EcnhaA and betB … increased the maximum salt tolerance of strain KT2440 to 5% w/v NaCl” (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12) | Very strong, direct, quantitative experimental edge. Assay- and strain-specific, but highly valuable for mechanistic curation and as a benchmark for maximum NaCl support. | subject: composite node “EcnhaA + betB co-expression”; object: METPO:1000335 NaCl delta | DOI:10.3390/biology13060404, 2024, https://doi.org/10.3390/biology13060404 |
| Mechanosensitive channels (MscL/MscS) — protect_against — hypoosmotic shock | “Mechanosensitive (Msc) channels and compatible-solute efflux systems act as safety valves during sudden hypoosmotic shocks” (bonnaud2024haloarchaeaaspromising pages 2-4); Thompson et al. report “mscL and mscS” in osmoprotection-associated isolates (thompson2024themicrobiomeof pages 5-6) | Strong for downshock survival. Relevance to NaCl delta is indirect but important because broad NaCl range includes tolerance of decreases as well as increases in salinity. | subject: mscL / mscS; object: GO:candidate “response to hypoosmotic stress” / cell integrity | DOI:10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738; DOI:10.3390/microorganisms12071473, 2024, https://doi.org/10.3390/microorganisms12071473 |
| Salt-in strategy — supports — very high maximal salinity tolerance | The haloarchaea review states “salt-out is energetically costly and thus less suited to saturating salinities; salt-in is favored at very high salt” (bonnaud2024haloarchaeaaspromising pages 2-4); Najjari et al. define salting-in as accumulation of intracellular KCl equal to environmental NaCl (najjari2023physiologicalandgenomic pages 1-2) | Strong conceptual support, especially for extremophiles. This edge is broad and comparative rather than gene-specific; curate as strategy-level. | subject: candidate process “salt-in strategy”; object: METPO:1000335 NaCl delta / candidate “high maximal NaCl tolerance” | DOI:10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738; DOI:10.1007/s10709-023-00182-0, 2023, https://doi.org/10.1007/s10709-023-00182-0 |
| Salt-out strategy — uses — compatible solutes | “salt-out (excluding Na+ while accumulating organic compatible solutes like sugars, polyalcohols, ectoin, trehalose, glycine-betaine)” (bonnaud2024haloarchaeaaspromising pages 2-4) and Zeaiter et al. define the “compatible solute” strategy with osmoprotectant accumulation/uptake (zeaiter2019phenomicsandgenomics pages 1-2) | Strong, general edge and curation-ready. Breadth implication is broad but indirect unless tied to measured growth-range data. | subject: candidate process “salt-out strategy”; object: CHEBI:17750 glycine betaine / CHEBI:17244 ectoine / CHEBI:30911 trehalose / GO:0006970 response to osmotic stress | DOI:10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738; DOI:10.3389/fmicb.2019.01304, 2019, https://doi.org/10.3389/fmicb.2019.01304 |
| Fluctuating environmental salinity — selects_for — hybrid salt-in/salt-out strategy | “Extreme fluctuations in ambient salinity select for bacteria with a hybrid ‘salt-in’/’salt-out’ osmoregulation strategy” and the MAGs “contain genes for both the energetically cheaper ‘salt-in’ and more expensive ‘salt-out’ strategies” (bonnaud2024haloarchaeaaspromising pages 2-4) | Direct and recent evidence at community/genome level. Strong for environmental selection edge; direct effect on NaCl delta breadth is plausible but still somewhat inferred. | subject: ENVO:candidate “fluctuating salinity environment”; object: candidate process “hybrid salt-in/salt-out osmoregulation strategy” | DOI:10.3389/frmbi.2023.1329925, 2024, https://doi.org/10.3389/frmbi.2023.1329925 |
| Genomic presence of ectoine/glycine betaine pathways — indicates — salt-out adaptation | “In-silico studies of the osmoregulatory strategy revealed a salt-out mechanism … genes for biosynthesis and transport of the compatible solutes ectoine and glycine betaine” (zeaiter2019phenomicsandgenomics pages 1-2) | Good genome-to-strategy edge. Strong for annotation of adaptation mode, but phenotype inference should be marked moderate unless tested experimentally. | subject: ectoine/glycine betaine biosynthetic and transport genes; object: candidate process “salt-out adaptation” | DOI:10.3389/fmicb.2023.1192059, 2023, https://doi.org/10.3389/fmicb.2023.1192059 |
| NaCl niche breadth (half-max fitness range) — quantifies — NaCl delta | Niche breadth was measured as “the salinity range in g L−1 NaCl where normalized fitness is at least 50% of the extrapolated maximum,” with separate “hyperosmotic” and “hypoosmotic” components around the optimum (rain‐franco2022nichebreadthaffects pages 3-3, rain‐franco2022nichebreadthaffects pages 3-4, rain‐franco2022nichebreadthaffects media 2b3f4334) | Important trait-definition edge for curation. This is a measurement/assay interpretation, not a mechanism, but helps distinguish NaCl delta from optimum or maximum-only traits. | subject: METPO:1000335 NaCl delta; object: candidate assay node “half-maximum salinity fitness range” | DOI:10.1111/mec.16316, 2022, https://doi.org/10.1111/mec.16316 |


*Table: This table lists candidate causal edges for the microbial trait NaCl delta, linking osmoadaptation mechanisms, genes, transporters, and environmental drivers to the breadth of NaCl concentrations that support growth. It is designed to support TraitMech curation with direct quotes, ontology suggestions, and source details.*

---

## Warnings / curation notes (what should not yet be curated as “strong”)
1) **Genomics-only inference**: Presence of ectoine/betaine genes is strong evidence for capacity but does not alone establish the quantitative NaCl delta (min/max growth). Mark as *inferred/uncertain* unless paired with growth-range assays (zeaiter2019phenomicsandgenomics pages 1-2).
2) **Survival vs growth**: Reports of “survive up to X% salinity” may reflect survival, not growth-supporting maxima; do not map directly to NaCl delta without clarification (najjari2023physiologicalandgenomic pages 1-2).
3) **Assay dependence**: NaCl delta can shift with compatible solute supplementation (betaine/proline) and medium conditions; edges that change tolerance only under supplementation should be marked as **assay-/condition-specific** (fan2024improvementinsalt pages 1-2).
4) **Taxon specificity**: c-di-AMP is not universal across all microbial lineages; curate c-di-AMP edges with scope notes (Firmicutes/Actinobacteria/Cyanobacteria emphasis in the review) (foster2024bacterialcellvolume pages 1-2).
5) **Missing full-text of foundational review cited in template**: the provided evidence list includes DOI:10.1093/femsre/fuy009 as “existing evidence,” but it was unobtainable in this run; avoid quoting/edge claims that rely uniquely on that source until retrieved.

---

# DOI-first bibliography (with publication dates and URLs)

- Foster AJ, van den Noort M, Poolman B. **Bacterial cell volume regulation and the importance of cyclic di-AMP.** *Microbiology and Molecular Biology Reviews.* **Jun 2024.** DOI:10.1128/mmbr.00181-23. URL: https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 1-2)

- Fan M, Tan S, Wang W, Zhang X. **Improvement in Salt Tolerance Ability of *Pseudomonas putida* KT2440.** *Biology.* **Jun 2024.** DOI:10.3390/biology13060404. URL: https://doi.org/10.3390/biology13060404 (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 8-10, fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 2-3)

- Bonnaud E, Oger PM, Ohayon A, Louis Y. **Haloarchaea as Promising Chassis to Green Chemistry.** *Microorganisms.* **Aug 2024.** DOI:10.3390/microorganisms12081738. URL: https://doi.org/10.3390/microorganisms12081738 (bonnaud2024haloarchaeaaspromising pages 2-4)

- Ionescu D, Zoccarato L, Cabello-Yeves PJ, Tikochinski Y. **Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy.** *Frontiers in Microbiomes.* **Jan 2024.** DOI:10.3389/frmbi.2023.1329925. URL: https://doi.org/10.3389/frmbi.2023.1329925 (bonnaud2024haloarchaeaaspromising pages 2-4)

- Thompson MEH, Raizada MN. **The Microbiome of Fertilization-Stage Maize Silks (Style) Encodes Genes and Expresses Traits That Potentially Promote Survival in Pollen/Style Niches and Host Reproduction.** *Microorganisms.* **Jul 2024.** DOI:10.3390/microorganisms12071473. URL: https://doi.org/10.3390/microorganisms12071473 (thompson2024themicrobiomeof pages 5-6)

- Galisteo C, de la Haba RR, Ventosa A, Sánchez-Porro C. **The Hypersaline Soils of the Odiel Saltmarshes Natural Area as a Source for Uncovering a New Taxon: *Pseudidiomarina terrestris* sp. nov.** *Microorganisms.* **Feb 2024.** DOI:10.3390/microorganisms12020375. URL: https://doi.org/10.3390/microorganisms12020375 (galisteo2024thehypersalinesoils pages 19-20)

- Galisteo C, de la Haba RR, Sánchez-Porro C, Ventosa A. **A step into the rare biosphere: genomic features of the new genus *Terrihalobacillus* and the new species *Aquibacillus salsiterrae* from hypersaline soils.** *Frontiers in Microbiology.* **May 2023.** DOI:10.3389/fmicb.2023.1192059. URL: https://doi.org/10.3389/fmicb.2023.1192059 (zeaiter2019phenomicsandgenomics pages 1-2)

- Najjari A, et al. **Physiological and genomic insights into abiotic stress of halophilic archaeon *Natrinema altunense* 4.1R…** *Genetica.* **Feb 2023.** DOI:10.1007/s10709-023-00182-0. URL: https://doi.org/10.1007/s10709-023-00182-0 (najjari2023physiologicalandgenomic pages 1-2)

- Rain‑Franco A, et al. **Niche breadth affects bacterial transcription patterns along a salinity gradient.** *Molecular Ecology.* (online/issue year **2022**, month in record **Dec**). DOI:10.1111/mec.16316. URL: https://doi.org/10.1111/mec.16316 (rain‐franco2022nichebreadthaffects pages 2-3, rain‐franco2022nichebreadthaffects pages 3-3, rain‐franco2022nichebreadthaffects media 2b3f4334)

- Zeaiter Z, et al. **Phenomics and Genomics Reveal Adaptation of *Virgibacillus dokdonensis*…** *Frontiers in Microbiology.* **Jun 2019.** DOI:10.3389/fmicb.2019.01304. URL: https://doi.org/10.3389/fmicb.2019.01304 (zeaiter2019phenomicsandgenomics pages 1-2)

- Richter AA, et al. **Biosynthesis of the Stress-Protectant and Chemical Chaperon Ectoine: Biochemistry of the Transaminase EctB.** *Frontiers in Microbiology.* **Dec 2019.** DOI:10.3389/fmicb.2019.02811. URL: https://doi.org/10.3389/fmicb.2019.02811 (van2009productionofpoly pages 13-16)

---

## Summary for TraitMech curation
Mechanistically, **NaCl delta** can be modeled as the emergent consequence of (i) **ion homeostasis capacity and regulation** (Na+/H+ antiporters; K+ uptake; c-di-AMP control), (ii) **compatible solute synthesis/uptake capacity** (glycine betaine, ectoine, trehalose, proline), and (iii) **shock-response hardware** (mechanosensitive channels) interacting with (iv) **environmental salinity regimes**, especially fluctuation intensity. Direct engineered evidence shows that increasing Na+ export (EcnhaA) plus increasing betaine synthesis (betB) measurably raises the **upper growth-supporting NaCl limit**, thereby expanding the trait’s breadth under the tested conditions (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14).

References

1. (rain‐franco2022nichebreadthaffects pages 3-3): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.

2. (rain‐franco2022nichebreadthaffects media 2b3f4334): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.

3. (van2009productionofpoly pages 13-16): T Doan Van. Production of poly (3-hydroxybutyrate) and ectoines using a halophilic bacterium. Unknown journal, 2009.

4. (rain‐franco2022nichebreadthaffects pages 2-3): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.

5. (najjari2023physiologicalandgenomic pages 1-2): Afef Najjari, Ayoub Boussetta, Noha Youssef, Javier A. Linares-Pastén, Mouna Mahjoubi, Rahma Belloum, Haitham Sghaier, Ameur Cherif, and Hadda Imene Ouzari. Physiological and genomic insights into abiotic stress of halophilic archaeon natrinema altunense 4.1r isolated from a saline ecosystem of tunisian desert. Genetica, 151:133-152, Feb 2023. URL: https://doi.org/10.1007/s10709-023-00182-0, doi:10.1007/s10709-023-00182-0. This article has 5 citations and is from a peer-reviewed journal.

6. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

7. (zeaiter2019phenomicsandgenomics pages 1-2): Zahraa Zeaiter, Ramona Marasco, Jenny M. Booth, Erica M. Prosdocimi, Francesca Mapelli, Matteo Callegari, Marco Fusi, Grégoire Michoud, Francesco Molinari, Daniele Daffonchio, Sara Borin, and Elena Crotti. Phenomics and genomics reveal adaptation of virgibacillus dokdonensis strain 21d to its origin of isolation, the seawater-brine interface of the mediterranean sea deep hypersaline anoxic basin discovery. Frontiers in Microbiology, Jun 2019. URL: https://doi.org/10.3389/fmicb.2019.01304, doi:10.3389/fmicb.2019.01304. This article has 13 citations and is from a peer-reviewed journal.

8. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (foster2024bacterialcellvolume pages 1-2): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Microbiology and Molecular Biology Reviews, Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (fan2024improvementinsalt pages 1-2): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

11. (fan2024improvementinsalt pages 12-14): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

12. (fan2024improvementinsalt pages 2-3): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

13. (fan2024improvementinsalt pages 8-10): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

14. (thompson2024themicrobiomeof pages 5-6): Michelle E. H. Thompson and Manish N. Raizada. The microbiome of fertilization-stage maize silks (style) encodes genes and expresses traits that potentially promote survival in pollen/style niches and host reproduction. Microorganisms, 12:1473, Jul 2024. URL: https://doi.org/10.3390/microorganisms12071473, doi:10.3390/microorganisms12071473. This article has 6 citations.

15. (fan2024improvementinsalt pages 10-12): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

16. (rain‐franco2022nichebreadthaffects pages 3-4): Angel Rain‐Franco, Nicolas Mouquet, Claire Gougat‐Barbera, Thierry Bouvier, and Sara Beier. Niche breadth affects bacterial transcription patterns along a salinity gradient. Dec 2022. URL: https://doi.org/10.1111/mec.16316, doi:10.1111/mec.16316. This article has 33 citations and is from a highest quality peer-reviewed journal.

17. (galisteo2024thehypersalinesoils pages 19-20): Cristina Galisteo, Rafael R. de la Haba, Antonio Ventosa, and Cristina Sánchez-Porro. The hypersaline soils of the odiel saltmarshes natural area as a source for uncovering a new taxon: pseudidiomarina terrestris sp. nov. Microorganisms, 12:375, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020375, doi:10.3390/microorganisms12020375. This article has 8 citations.