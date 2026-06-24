---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:07:49.141284'
end_time: '2026-06-17T23:16:45.441389'
duration_seconds: 536.3
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum high
  trait_identifier: METPO:1000468
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration above
    approximately 8% (w/v), corresponding to extreme-halophile physiology.
  parent_traits: METPO:1000333
  synonyms: Extreme halophile, NaO_>8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation
    review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2:
    KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in
    (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)'
  causal_graph_summary: 'nacl_optimum_high_extreme_halophile: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum high
- **METPO identifier:** METPO:1000468
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration above approximately 8% (w/v), corresponding to extreme-halophile physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Extreme halophile, NaO_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)
- **Existing causal graph summary:** nacl_optimum_high_extreme_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_high.yaml`.

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
- **Trait label:** NaCl optimum high
- **METPO identifier:** METPO:1000468
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration above approximately 8% (w/v), corresponding to extreme-halophile physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Extreme halophile, NaO_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)
- **Existing causal graph summary:** nacl_optimum_high_extreme_halophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_high.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **NaCl optimum high** (METPO:1000468)

## 1) Scope summary (TraitMech curation intent)

**Target trait definition (given):** *NaCl optimum phenotype with the best-growth NaCl concentration above ~8% (w/v), corresponding to extreme-halophile physiology.*

### What this trait represents
This trait is best interpreted as a **measured growth optimum** (peak growth rate or biomass yield) in **high NaCl** media, not merely survival or growth at high salt. Multiple classification schemes define *extreme halophiles* by **optimum** salinity at very high NaCl; for example, one widely used scheme sets “extreme halophiles” at **4–5.9 M NaCl**, while “borderline” is **2.5–4.0 M** (and moderate is 0.5–2.5 M). (cirachavez2019kineticsofhalophilic pages 1-3, cirachavez2019kineticsofhalophilic pages 3-6)

### Distinguishing from nearby traits / boundary cases
*Halotolerant* organisms are explicitly distinguished as those that **do not require high salt** but can grow in it (“does not require high salt but can grow in it”), i.e., high-salt **tolerance** rather than a high-salt **optimum**. (bartha2022investigatingextremotolerantmicrobes pages 21-25, cirachavez2019kineticsofhalophilic pages 1-3)

Because the METPO definition uses **>~8% (w/v)**, it overlaps with “moderate halophile” ranges in some older schemes (e.g., moderate up to 15% w/v), while still aiming to capture **extreme-halophile physiology** (often salt-in strategists). Therefore, for curation it is recommended to:

* treat **>8% w/v** as the minimal threshold for this METPO class, but
* preferentially map **canonical extreme-halophile physiology** (typically **≥15% w/v** and/or **≥2.5–4 M NaCl**) when selecting mechanistic edges. (cirachavez2019kineticsofhalophilic pages 1-3, bartha2022investigatingextremotolerantmicrobes pages 139-143)

### Empirical anchoring examples
A concrete extreme-halophile example: *Haloterrigena* strain SGH1 grows at **15–30% (w/v) NaCl** with an **optimum at 25% (w/v)**; growth is severely restricted below 15% and the strain requires at least ~10% NaCl to avoid lysis. (flores2020haloterrigenasp.strain pages 1-2)

A recent haloarchaeal tolerance summary reports that haloarchaea “**require a minimum salt concentration of 10% (w/v) for growth** and can survive up to **35% (w/v)** salinity,” which is consistent with the trait’s intended extreme-halophile scope. (matarredona2024understandingthetolerance pages 1-2)

## 2) Key concepts and mechanistic understanding (current)

### Osmoadaptation strategies: salt-in vs salt-out
Two broad strategies are consistently invoked:

1) **Salt-in strategy** (canonical for haloarchaea and a few bacteria): accumulation of intracellular inorganic ions, especially **K+ and Cl−** (functionally “KCl”), requiring macromolecular adaptation to high ionic strength. (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

2) **Compatible-solute (salt-out) strategy**: maintenance of lower intracellular salt by accumulating organic osmolytes such as **ectoine** or **glycine betaine**, providing broader salinity flexibility (common in moderate halophiles and halotolerants). (bartha2022investigatingextremotolerantmicrobes pages 25-28, yu2024temporaldynamicsof pages 1-2)

### Mechanistic core of extreme-halophile physiology (salt-in)
Recent and high-authority sources converge on a mechanistic package:

* **High intracellular K+ (and Cl−)**: haloarchaea “accumulate up to **~4 M K+**” in cytoplasm; this “salt-in” strategy is linked with proteome adaptation. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* **Acidic proteomes / low protein pI**: proteins are enriched in **acidic residues (Asp/Glu)**; extreme cases show “the most acidic proteomes ever observed” with **median pI ≤ 4.4** in near life-limiting hypersaline systems. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* **Protein surface composition shifts**: halophilic proteins increase “short, polar and acidic amino acids,” reducing hydrophobic/basic residues; this supports stability/solubility in high salt but may reduce stability at low salt. (herrero‐alfonso2024electrostaticsintroducea pages 1-2)

### Transport and bioenergetic components supporting salt-in (candidate mechanistic entities)
A 2024 haloarchaea chassis review summarizes a mechanistic model for ionic homeostasis in salt-in strategists:

* **Active exclusion of Na+**: Na+ extrusion via **Na+/H+ antiporters** powered by proton motive force. (bonnaud2024haloarchaeaaspromising pages 2-4)
* **K+ uptake**: K+ accumulation via uptake systems (described generally as uniport driven by membrane potential; other sources mention “potassium-selective ion channels”). (bonnaud2024haloarchaeaaspromising pages 2-4, herrero‐alfonso2024electrostaticsintroducea pages 1-2)
* **Cl− acquisition**: Cl− uptake by **Cl−/Na+ symport** plus light-driven **halorhodopsin** Cl− pump. (bonnaud2024haloarchaeaaspromising pages 2-4)
* **Energy coupling**: proton gradients generated by respiratory chain and **bacteriorhodopsin** (light-driven proton pump), supporting antiport and ATP synthesis. (bonnaud2024haloarchaeaaspromising pages 2-4)

Curation note: evidence above is strong for **functions** (antiport, rhodopsins) but is not always gene-specific across taxa in the available excerpts; treat gene-level nodes (e.g., Trk/Kdp subunits) as **taxon-specific/uncertain** unless a gene-anchored reference is added.

## 3) Recent developments and latest research (prioritizing 2023–2024)

### (A) Extremes of proteome acidification and community adaptation (2024)
Metagenomic/proteomic comparative work in 2024 reports extreme halophily is associated with **molar K+ “salt-in”** and exceptional proteome acidification (median pI ≤ 4.4) in near life-limiting brines, broadening the known diversity of lineages capable of extreme halophily. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

### (B) Refinement of halophilic protein adaptation models (2024)
A 2024 Protein Science study describes the trade-off: halophilic amino acid composition can decrease stability at low salt but improves stability/solubility at high salt; it reiterates salt-in strategists accumulate intracellular KCl “even above 3 M” and highlights acidic residue enrichment as a central protein-level adaptation. (herrero‐alfonso2024electrostaticsintroducea pages 1-2)

### (C) Mixed/hybrid osmoregulation as a boundary-case trend (2024)
Increasing evidence indicates some lineages can combine salt-in and salt-out. A 2024 *Applied and Environmental Microbiology* study on *Natranaerobius thermophilus* shows long-term salinity adaptation via both compatible solutes and K+ handling, including **glycine betaine transporters (Opu/ProU)**, Na+/solute symporters (SSS), and Na+/K+/H+ transport elements; measured intracellular glycine betaine increased from ~52.7 to ~893.1 mM across salinity conditions (2.5–4.3 M Na+). (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19)

Curation implication: hybrid strategies should be modeled as **adjacent mechanisms** and often treated as **uncertain edges** for the specific trait “NaCl optimum high” if the trait is intended to represent classic haloarchaeal-type extreme halophily.

## 4) Current applications and real-world implementations (2023–2024)

### Bioremediation in hypersaline matrices (2024)
A 2024 review positions haloarchaea as “tools for bioremediation technologies” targeting **brines, salty water and saline soils** contaminated with nitrate/nitrite, oxychlorates (perchlorate/chlorate), heavy metals, hydrocarbons, and aromatic compounds. It notes haloarchaea can be major microbial populations in environments with **>20–25% (w/v)** total salts. (martinezespinosa2024halophilicarchaeaas pages 1-2, martinezespinosa2024halophilicarchaeaas pages 2-4)

### Haloarchaea as industrial chassis for “green chemistry” (2024)
A 2024 review argues industrial deployment of halophilic extremozymes is constrained by lack of suitable hosts, and proposes **haloarchaea-based cellular chassis**. It reports haloarchaea are mostly obligate halophiles with optimal growth at **10–35% (1.71–6 M) NaCl**. (bonnaud2024haloarchaeaaspromising pages 1-2)

### Bioactive products and bioplastics (2023–2024)
A 2023 review synthesizes evidence that haloarchaea produce carotenoids, enzymes, and **polyhydroxyalkanoates (PHAs)**, and can transform pollutants (e.g., hydrocarbons and oxychlorides), with further prospects in biomedical materials (e.g., exopolysaccharides binding SARS‑CoV‑2 spike protein). (moopantakath2023bioactivemoleculesfrom pages 1-2, moopantakath2023bioactivemoleculesfrom pages 4-5)

A 2024 Dead Sea-focused review lists product classes obtained from Dead Sea halophiles (antimicrobials, bioplastics, biofuels, extremozymes, retinal proteins, pigments, exopolysaccharides, compatible solutes) and emphasizes process advantages such as reduced freshwater demand and potential continuous production. (aldaghistani2024microbialcommunitiesin pages 1-3)

## 5) Relevant statistics and quantitative data (recent)

* **Minimum salt requirement / survival envelope (haloarchaea)**: minimum **10% (w/v)** for growth; survival up to **35% (w/v)** reported for a panel of haloarchaea. (matarredona2024understandingthetolerance pages 1-2)
* **Example extreme optimum**: *Haloterrigena* SGH1 optimum **25% (w/v) NaCl**, growth range 15–30% (w/v). (flores2020haloterrigenasp.strain pages 1-2)
* **Intracellular K+ scale for salt-in**: cytoplasmic K+ up to **~4 M** (salt-in). (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* **Proteome halophilicity metric**: extreme cases with **median protein pI ≤ 4.4** in high-salinity brines. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
* **Compatible-solute productivity (boundary case)**: *Halomonas elongata* ectoine reached maximum productivity **1450 ± 99 mg/L/h** after NaCl shock (industrial relevance but represents salt-out rather than canonical salt-in extreme halophily). (yu2024temporaldynamicsof pages 1-2)

## 6) Candidate nodes and causal edges for `nacl_optimum_high.yaml`

The following artifact provides a curation-oriented inventory of candidate nodes (with suggested CURIEs where available) and a first-pass edge table with supporting snippets and curator notes.

| Section | Category | Node label | Suggested CURIE | Notes |
|---|---|---|---|---|
| Nodes | Phenotype/assay | NaCl optimum high (>~8% w/v NaCl optimum) | METPO:1000468 | Trait scope corresponds to extreme-halophile physiology; distinguish optimum from mere tolerance. Extreme halophiles are defined by optimal growth at very high salinity, often >15% w/v in older schemes, while haloarchaea may require ≥10% w/v for growth (cirachavez2019kineticsofhalophilic pages 1-3, matarredona2024understandingthetolerance pages 1-2) |
| Nodes | Phenotype/assay | Extreme halophile | label only | Classification boundary often overlaps 2.5–5.2 M NaCl or >15% w/v, depending on scheme; use cautiously as a class label distinct from measured optimum (bartha2022investigatingextremotolerantmicrobes pages 139-143, cirachavez2019kineticsofhalophilic pages 1-3) |
| Nodes | Phenotype/assay | Halotolerant | label only | Boundary case: tolerates salt but does not require it for growth; should not be equated with NaCl optimum high (bartha2022investigatingextremotolerantmicrobes pages 21-25, cirachavez2019kineticsofhalophilic pages 1-3) |
| Nodes | Environment | hypersaline environment | ENVO:01000215 | Broad environmental context for trait; includes salterns, hypersaline lakes, brines, halite-associated systems (oren2024novelinsightsinto pages 1-2, aldaghistani2024microbialcommunitiesin pages 1-3) |
| Nodes | Environment | halite brine inclusion habitat | label only | Relevant assay/ecological context for saturated NaCl and acclimation studies in Halobacterium salinarum (favreau2023molecularacclimationof pages 1-2) |
| Nodes | Environment | NaCl-saturated brine | label only | Near-saturation environment where some halophiles show optimum growth/metabolism (lee2018naclsaturatedbrinesare pages 15-17) |
| Nodes | Cellular strategy | salt-in osmoadaptation strategy | GO:0006970 | Central mechanism for many extreme halophiles: osmotic balance via intracellular inorganic ions, mainly KCl (bonnaud2024haloarchaeaaspromising pages 2-4, gutierrezpreciado2024extremelyacidicproteomes pages 1-4, oren2024novelinsightsinto pages 1-2) |
| Nodes | Cellular strategy | compatible-solute / salt-out osmoadaptation strategy | GO:0006970 | Important nearby mechanism for moderate halophiles and boundary cases; usually not primary for canonical extreme haloarchaea (bartha2022investigatingextremotolerantmicrobes pages 25-28, yu2024temporaldynamicsof pages 1-2) |
| Nodes | Cellular strategy | hybrid salt-in/salt-out strategy | label only | Reported in some bacteria/polyextremophiles; likely boundary case rather than canonical node for this trait (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| Nodes | Ion transporters | potassium uptake system (Trk-family candidate) | label only | Literature support for K+ uptake as a core salt-in feature; direct transporter naming is uneven across sources and often taxon-specific (herrero‐alfonso2024electrostaticsintroducea pages 1-2, chen2020comparativegenomicsanalysis pages 11-12) |
| Nodes | Ion transporters | Na+/H+ antiporter | GO:0015385 | Supports Na+ exclusion/homeostasis in high salt; highlighted in haloarchaeal salt-in physiology and hybrid strategists (bonnaud2024haloarchaeaaspromising pages 2-4, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Nodes | Ion transporters | halorhodopsin chloride pump | label only | Light-driven Cl− uptake mechanism reported as part of haloarchaeal ion balance under salt-in adaptation (bonnaud2024haloarchaeaaspromising pages 2-4) |
| Nodes | Ion transporters | bacteriorhodopsin proton pump | label only | Generates proton motive force supporting Na+/H+ antiport and ATP synthesis in haloarchaea (bonnaud2024haloarchaeaaspromising pages 2-4) |
| Nodes | Ion transporters | Na+-translocating FOF1-ATPase | label only | Reported in hybrid salinity adaptation; likely boundary-case transporter rather than core universal extreme-halophile node (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Nodes | Compatible solutes | ectoine | CHEBI:27886 | Canonical salt-out osmolyte; useful as negative/boundary-case node because presence often indicates moderate-halophile strategy rather than classic extreme-halophile salt-in (yu2024temporaldynamicsof pages 1-2, reang2024extremozymesandcompatible pages 1-2) |
| Nodes | Compatible solutes | glycine betaine | CHEBI:17750 | Compatible solute present in salt-out or mixed strategies; some extreme halophiles encode pathways too, so edge to trait should be uncertain (oren2024novelinsightsinto pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Nodes | Compatible solutes | L-glutamate | CHEBI:29985 | Osmoadaptive metabolite in salt-out/mixed systems; also transiently rises after salt shock in Halomonas elongata (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Nodes | Compatible solutes | L-proline | CHEBI:26271 | Compatible solute in mixed or salt-out systems; boundary marker (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Nodes | Protein adaptations | acidic proteome | label only | Hallmark of salt-in extreme halophiles; proteomes enriched in Asp/Glu and low median pI (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| Nodes | Protein adaptations | increased acidic amino-acid content (Asp/Glu enriched proteins) | label only | Mechanistic subfeature of acidic proteome that promotes solubility/function in high intracellular KCl (herrero‐alfonso2024electrostaticsintroducea pages 1-2, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| Nodes | Protein adaptations | reduced hydrophobic surface / increased protein solubility in high salt | label only | Reported adaptation in halophilic proteins enabling folding and function at molar salt concentrations (herrero‐alfonso2024electrostaticsintroducea pages 1-2, lee2018naclsaturatedbrinesare pages 15-17) |
| Nodes | Protein adaptations | low median protein pI | label only | Quantitative proxy of proteome acidification; extreme examples median pI ≤4.4 in 2024 study (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| Nodes | Key taxa | Halobacterium salinarum | NCBITaxon:2242 | Model extreme haloarchaeon; canonical salt-in strategist and halite-brine acclimation model (favreau2023molecularacclimationof pages 1-2, herrero‐alfonso2024electrostaticsintroducea pages 1-2) |
| Nodes | Key taxa | Salinibacter ruber | NCBITaxon:309807 | Rare bacterial extreme halophile using archaeal-like salt-in adaptation (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, oren2024novelinsightsinto pages 1-2) |
| Nodes | Key taxa | Halorutilus salinus | NCBITaxon:label only | Newly described halophilic archaeon; genomic evidence suggests typical haloarchaeal salt-in strategy (oren2024novelinsightsinto pages 1-2) |
| Nodes | Key taxa | Haloarcula terrestris | NCBITaxon:label only | Example strain with growth at 15–30% w/v NaCl, optimum 25% w/v; useful assay example for trait anchoring (flores2020haloterrigenasp.strain pages 1-2) |
| Nodes | Key taxa | Haloterrigena sp. SGH1 | NCBITaxon:label only | Example extreme haloarchaeon with 15–30% w/v growth range and 25% optimum; growth improved by 50 mM KCl (flores2020haloterrigenasp.strain pages 1-2) |

| Subject | Predicate | Object | Supporting snippet | Citation IDs |
|---|---|---|---|---|
| high external NaCl concentration | selects_for | salt-in osmoadaptation strategy | “cells accumulate K+ (predominantly) and Cl− in the cytoplasm to match external osmolarity” (bonnaud2024haloarchaeaaspromising pages 2-4) | (bonnaud2024haloarchaeaaspromising pages 2-4, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| salt-in osmoadaptation strategy | increases | intracellular KCl concentration | “accumulate intracellular concentrations of potassium chloride even above 3 M” (herrero‐alfonso2024electrostaticsintroducea pages 1-2) | (herrero‐alfonso2024electrostaticsintroducea pages 1-2, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| salt-in osmoadaptation strategy | requires | potassium uptake system | “upregulating potassium-selective ion channels” / Trk-related support in comparative genomics (herrero‐alfonso2024electrostaticsintroducea pages 1-2) | (herrero‐alfonso2024electrostaticsintroducea pages 1-2, chen2020comparativegenomicsanalysis pages 11-12) |
| Na+/H+ antiporter activity | supports | salt-in osmoadaptation strategy | “Na+ extrusion via Na+/H+ antiporters driven by a proton electrochemical gradient” (bonnaud2024haloarchaeaaspromising pages 2-4) | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| halorhodopsin chloride pump | contributes_to | intracellular Cl− accumulation | “Cl− uptake through a Cl−/Na+ symport plus a light-dependent Cl− pump (halorhodopsin)” (bonnaud2024haloarchaeaaspromising pages 2-4) | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| bacteriorhodopsin proton pump | generates | proton motive force | “The proton gradient… is generated by the respiratory chain and by light-driven bacteriorhodopsin” (bonnaud2024haloarchaeaaspromising pages 2-4) | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| proton motive force | powers | Na+/H+ antiporter activity | “Na+ extrusion via Na+/H+ antiporters driven by a proton electrochemical gradient” (bonnaud2024haloarchaeaaspromising pages 2-4) | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| intracellular high KCl | selects_for | acidic proteome | “This ‘salt-in’ strategy is concomitant with an excess of acidic amino acids” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| acidic proteome | enables | protein function at high salinity | “proteins are enriched in negatively charged acidic residues… Such proteome acidification preserves protein structure/function under high intracellular salt” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | (lee2018naclsaturatedbrinesare pages 15-17, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) |
| increased acidic amino-acid content | increases | protein solubility in high salt | “increase the number of short, polar and acidic amino acids… improve salt-induced stabilization and solubility” (herrero‐alfonso2024electrostaticsintroducea pages 1-2) | (herrero‐alfonso2024electrostaticsintroducea pages 1-2) |
| reduced hydrophobic surface | contributes_to | halophilic protein stability at high salt | “reducing apolar surface content and modulation of the hydrophobic effect are key” (herrero‐alfonso2024electrostaticsintroducea pages 1-2) | (herrero‐alfonso2024electrostaticsintroducea pages 1-2, lee2018naclsaturatedbrinesare pages 15-17) |
| NaCl optimum high trait | exemplified_by | Halobacterium salinarum | canonical extreme haloarchaeon in halite and salt-in discussions (favreau2023molecularacclimationof pages 1-2) | (herrero‐alfonso2024electrostaticsintroducea pages 1-2, favreau2023molecularacclimationof pages 1-2) |
| NaCl optimum high trait | exemplified_by | Salinibacter ruber | “Salinibacter… mimicking archaeal ‘salt-in’ adaptations” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, oren2024novelinsightsinto pages 1-2) |
| low external salinity | impairs | salt-in extreme halophile growth | “cellular vitality is compromised below ~2.2 M K+ with misfolding/aggregation” / SGH1 growth severely restricted below 15% NaCl (lee2018naclsaturatedbrinesare pages 15-17) | (flores2020haloterrigenasp.strain pages 1-2, lee2018naclsaturatedbrinesare pages 15-17) |
| compatible-solute strategy | associated_with | ectoine accumulation | “H. elongata primarily accumulates ectoine as its main compatible solute” (yu2024temporaldynamicsof pages 1-2) | (yu2024temporaldynamicsof pages 1-2, reang2024extremozymesandcompatible pages 1-2) |
| compatible-solute strategy | associated_with | glycine betaine accumulation or transport | “glycine betaine ABC transporters (Opu and ProU families)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | (xing2024thepolyextremophilenatranaerobius pages 1-2, reang2024extremozymesandcompatible pages 1-2) |
| ectoine biosynthesis genes | supports | moderate/salt-out halophily rather_than extreme salt-in | Aquibacillus genomes “harbor the genes for biosynthesis and transport of the compatible solutes ectoine and glycine betaine” and show optimum 4–10% NaCl (galisteo2023astepinto pages 1-2) | (galisteo2023astepinto pages 1-2) |
| glycine betaine biosynthesis/transport | may_support | high-salt growth (uncertain, taxon-specific) | some Halomicroarcula encode complete pathways for trehalose and glycine betaine despite typical salt-in strategy (oren2024novelinsightsinto pages 1-2) | (oren2024novelinsightsinto pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) |
| hybrid salt-in/salt-out strategy | may_support | high salinity adaptation (uncertain boundary case) | Natranaerobius “combining the ‘compatible solute’ and ‘salt-in’ mechanisms” (xing2024thepolyextremophilenatranaerobius pages 1-2) | (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) |


*Table: This artifact provides curation-oriented candidate nodes and evidence-backed edges for the microbial trait 'NaCl optimum high'. It separates core extreme-halophile mechanisms from boundary-case salt-out or hybrid strategies, helping prioritize what to curate into a TraitMech causal graph.*

## 7) Expert opinion / synthesis (authoritative interpretation)

Across recent authoritative reviews and primary studies, **high NaCl optimum** in extreme halophiles is consistently attributed to a **system-level coupling** of:

1) **Ionic osmotic balance via KCl accumulation** (salt-in),
2) **bioenergetic support for Na+ exclusion and ion cycling** (antiport + rhodopsins/respiration), and
3) **proteome-wide adaptation (acidic proteins, altered surface chemistry) to maintain folding/solubility under high ionic strength**. (bonnaud2024haloarchaeaaspromising pages 2-4, herrero‐alfonso2024electrostaticsintroducea pages 1-2, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

This package differentiates the trait from **halotolerance** and **moderate halophily**, where compatible solutes (ectoine/betaine) and flexible osmoregulation dominate and the proteome is not necessarily globally acidified to the same degree. (cirachavez2019kineticsofhalophilic pages 1-3, yu2024temporaldynamicsof pages 1-2)

## 8) Curation warnings (do not curate yet / uncertain)

1) **Gene-level specificity is incomplete in current excerpts.** Several key components (K+ uptake systems such as Trk/Kdp; specific antiporter families) are described functionally, but not consistently mapped to named genes in the retrieved snippets. Curating **gene nodes** (e.g., TrkH/TrkA, KdpABC) should be marked *uncertain* unless supported by a gene-specific reference. (bonnaud2024haloarchaeaaspromising pages 2-4, herrero‐alfonso2024electrostaticsintroducea pages 1-2)

2) **Compatible-solute pathways appear in some salt-in taxa.** The presence of trehalose/betaine pathways in salt-in haloarchaea (e.g., Halomicroarcula) suggests these compounds can be auxiliary; edges linking glycine betaine directly to “NaCl optimum high” should be considered **taxon-specific/uncertain**. (oren2024novelinsightsinto pages 1-2)

3) **The METPO threshold (>~8% w/v) may capture moderate halophiles depending on schema.** If the curator intent is strict “extreme halophile physiology,” consider operationally enforcing a stronger optimum threshold (e.g., ≥15% w/v or ≥2.5–4 M NaCl) in assay metadata or via additional traits. (cirachavez2019kineticsofhalophilic pages 1-3, bartha2022investigatingextremotolerantmicrobes pages 139-143)

4) **Hybrid strategies are real but may not define the class.** Mixed salt-in/salt-out (e.g., *Natranaerobius*) should be treated as **adjacent mechanisms** and curated cautiously to avoid conflating classic haloarchaeal extreme halophily with polyextremophile-specific solutions. (xing2024thepolyextremophilenatranaerobius pages 1-2)

## 9) DOI-first bibliography (with URLs and publication dates where available)

1. Gutiérrez‑Preciado A, et al. *Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines*. **Nature Ecology & Evolution** (Aug **2024**). DOI: **10.1038/s41559-024-02505-6**. https://doi.org/10.1038/s41559-024-02505-6 (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

2. Oren A. *Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems*. **npj Biodiversity** (Aug **2024**). DOI: **10.1038/s44185-024-00050-w**. https://doi.org/10.1038/s44185-024-00050-w (oren2024novelinsightsinto pages 1-2)

3. Herrero‑Alfonso P, et al. *Electrostatics introduce a trade‐off between mesophilic stability and adaptation in halophilic proteins*. **Protein Science** (May **2024**). DOI: **10.1002/pro.5003**. https://doi.org/10.1002/pro.5003 (herrero‐alfonso2024electrostaticsintroducea pages 1-2)

4. Bonnaud E, et al. *Haloarchaea as Promising Chassis to Green Chemistry*. **Microorganisms** (Aug **2024**). DOI: **10.3390/microorganisms12081738**. https://doi.org/10.3390/microorganisms12081738 (bonnaud2024haloarchaeaaspromising pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4)

5. Martínez‑Espinosa RM. *Halophilic archaea as tools for bioremediation technologies*. **Applied Microbiology and Biotechnology** (Jun **2024**). DOI: **10.1007/s00253-024-13241-z**. https://doi.org/10.1007/s00253-024-13241-z (martinezespinosa2024halophilicarchaeaas pages 1-2, martinezespinosa2024halophilicarchaeaas pages 2-4, martinezespinosa2024halophilicarchaeaas pages 4-5)

6. Yu J, et al. *Temporal dynamics of stress response in Halomonas elongata to NaCl shock: physiological, metabolomic, and transcriptomic insights*. **Microbial Cell Factories** (Mar **2024**). DOI: **10.1186/s12934-024-02358-5**. https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2)

7. Xing Q, et al. *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+*. **Applied and Environmental Microbiology** (May **2024**). DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19)

8. Matarredona L, et al. *Understanding the tolerance of halophilic archaea to stress landscapes*. **Environmental Microbiology Reports** (Nov **2024**). DOI: **10.1111/1758-2229.70039**. https://doi.org/10.1111/1758-2229.70039 (matarredona2024understandingthetolerance pages 1-2)

9. Favreau C, et al. *Molecular acclimation of Halobacterium salinarum to halite brine inclusions*. **Frontiers in Microbiology** (Jan **2023**; published in vol. 13 with DOI year 2022). DOI: **10.3389/fmicb.2022.1075274**. https://doi.org/10.3389/fmicb.2022.1075274 (favreau2023molecularacclimationof pages 1-2)

10. Moopantakath J, et al. *Bioactive molecules from haloarchaea: Scope and prospects for industrial and therapeutic applications*. **Frontiers in Microbiology** (Mar **2023**). DOI: **10.3389/fmicb.2023.1113540**. https://doi.org/10.3389/fmicb.2023.1113540 (moopantakath2023bioactivemoleculesfrom pages 1-2, moopantakath2023bioactivemoleculesfrom pages 4-5)

11. Al‑Daghistani HI, et al. *Microbial communities in the Dead Sea and their potential biotechnological applications*. **Communicative & Integrative Biology** (Jun **2024**). DOI: **10.1080/19420889.2024.2369782**. https://doi.org/10.1080/19420889.2024.2369782 (aldaghistani2024microbialcommunitiesin pages 1-3)

12. Flores N, et al. *Haloterrigena sp. strain SGH1...* **Frontiers in Microbiology** (Mar **2020**). DOI: **10.3389/fmicb.2020.00324**. https://doi.org/10.3389/fmicb.2020.00324 (flores2020haloterrigenasp.strain pages 1-2)

13. Lee CJD, et al. *NaCl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats*. **FEMS Microbiology Reviews** (Jun **2018**). DOI: **10.1093/femsre/fuy026**. https://doi.org/10.1093/femsre/fuy026 (lee2018naclsaturatedbrinesare pages 15-17)

14. Cira‑Chávez LA, et al. *Kinetics of Halophilic Enzymes*. IntechOpen chapter (Jan **2019**). DOI: **10.5772/intechopen.81100**. https://doi.org/10.5772/intechopen.81100 (cirachavez2019kineticsofhalophilic pages 1-3, cirachavez2019kineticsofhalophilic pages 3-6)


References

1. (cirachavez2019kineticsofhalophilic pages 1-3): Luis Alberto Cira-Chávez, Joseph Guevara-Luna, Marisela Yadira Soto-Padilla, Brenda Román-Ponce, María Soledad Vásquez- Murrieta, and María Isabel Estrada-Alvarado. Kinetics of halophilic enzymes. Kinetics of Enzymatic Synthesis, Jan 2019. URL: https://doi.org/10.5772/intechopen.81100, doi:10.5772/intechopen.81100. This article has 20 citations.

2. (cirachavez2019kineticsofhalophilic pages 3-6): Luis Alberto Cira-Chávez, Joseph Guevara-Luna, Marisela Yadira Soto-Padilla, Brenda Román-Ponce, María Soledad Vásquez- Murrieta, and María Isabel Estrada-Alvarado. Kinetics of halophilic enzymes. Kinetics of Enzymatic Synthesis, Jan 2019. URL: https://doi.org/10.5772/intechopen.81100, doi:10.5772/intechopen.81100. This article has 20 citations.

3. (bartha2022investigatingextremotolerantmicrobes pages 21-25): E Bartha. Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles. Unknown journal, 2022.

4. (bartha2022investigatingextremotolerantmicrobes pages 139-143): E Bartha. Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles. Unknown journal, 2022.

5. (flores2020haloterrigenasp.strain pages 1-2): Nataly Flores, Sebastián Hoyos, Mauricio Venegas, Alexandra Galetović, Lidia M. Zúñiga, Francisca Fábrega, Bernardo Paredes, Camila Salazar-Ardiles, Claudia Vilo, Carmen Ascaso, Jacek Wierzchos, Virginia Souza-Egipsy, Jorge E. Araya, Ramón Alberto Batista-García, and Benito Gómez-Silva. Haloterrigena sp. strain sgh1, a bacterioruberin-rich, perchlorate-tolerant halophilic archaeon isolated from halite microbial communities, atacama desert, chile. Frontiers in Microbiology, Mar 2020. URL: https://doi.org/10.3389/fmicb.2020.00324, doi:10.3389/fmicb.2020.00324. This article has 60 citations and is from a peer-reviewed journal.

6. (matarredona2024understandingthetolerance pages 1-2): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

7. (lee2018naclsaturatedbrinesare pages 15-17): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 90 citations and is from a domain leading peer-reviewed journal.

8. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

9. (bartha2022investigatingextremotolerantmicrobes pages 25-28): E Bartha. Investigating extremotolerant microbes in non-extreme environments and altering the salinity growth limits of halophiles. Unknown journal, 2022.

10. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

11. (herrero‐alfonso2024electrostaticsintroducea pages 1-2): Pablo Herrero‐Alfonso, Alba Pejenaute, Oscar Millet, and Gabriel Ortega‐Quintanilla. Electrostatics introduce a trade‐off between mesophilic stability and adaptation in halophilic proteins. Protein Science, May 2024. URL: https://doi.org/10.1002/pro.5003, doi:10.1002/pro.5003. This article has 9 citations and is from a peer-reviewed journal.

12. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

13. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

14. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

15. (martinezespinosa2024halophilicarchaeaas pages 1-2): Rosa María Martínez-Espinosa. Halophilic archaea as tools for bioremediation technologies. Applied Microbiology and Biotechnology, Jun 2024. URL: https://doi.org/10.1007/s00253-024-13241-z, doi:10.1007/s00253-024-13241-z. This article has 37 citations and is from a domain leading peer-reviewed journal.

16. (martinezespinosa2024halophilicarchaeaas pages 2-4): Rosa María Martínez-Espinosa. Halophilic archaea as tools for bioremediation technologies. Applied Microbiology and Biotechnology, Jun 2024. URL: https://doi.org/10.1007/s00253-024-13241-z, doi:10.1007/s00253-024-13241-z. This article has 37 citations and is from a domain leading peer-reviewed journal.

17. (bonnaud2024haloarchaeaaspromising pages 1-2): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

18. (moopantakath2023bioactivemoleculesfrom pages 1-2): Jamseel Moopantakath, Madangchanok Imchen, V. T. Anju, Siddhardha Busi, Madhu Dyavaiah, Rosa María Martínez-Espinosa, and Ranjith Kumavath. Bioactive molecules from haloarchaea: scope and prospects for industrial and therapeutic applications. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1113540, doi:10.3389/fmicb.2023.1113540. This article has 65 citations and is from a peer-reviewed journal.

19. (moopantakath2023bioactivemoleculesfrom pages 4-5): Jamseel Moopantakath, Madangchanok Imchen, V. T. Anju, Siddhardha Busi, Madhu Dyavaiah, Rosa María Martínez-Espinosa, and Ranjith Kumavath. Bioactive molecules from haloarchaea: scope and prospects for industrial and therapeutic applications. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1113540, doi:10.3389/fmicb.2023.1113540. This article has 65 citations and is from a peer-reviewed journal.

20. (aldaghistani2024microbialcommunitiesin pages 1-3): Hala I. Al-Daghistani, Sima Zein, and Manal A. Abbas. Microbial communities in the dead sea and their potential biotechnological applications. Communicative & Integrative Biology, Jun 2024. URL: https://doi.org/10.1080/19420889.2024.2369782, doi:10.1080/19420889.2024.2369782. This article has 23 citations and is from a peer-reviewed journal.

21. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

22. (favreau2023molecularacclimationof pages 1-2): Charly Favreau, Alicia Tribondeau, Marie Marugan, François Guyot, Beatrice Alpha-Bazin, Arul Marie, Remy Puppo, Thierry Dufour, Arnaud Huguet, Séverine Zirah, and Adrienne Kish. Molecular acclimation of halobacterium salinarum to halite brine inclusions. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1075274, doi:10.3389/fmicb.2022.1075274. This article has 12 citations and is from a peer-reviewed journal.

23. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

24. (chen2020comparativegenomicsanalysis pages 11-12): Dai-Di Chen, Ye Tian, Jian-Yu Jiao, Xiao-Tong Zhang, Yong-Guang Zhang, Zhou-Yan Dong, Meng-Jie Xiong, Min Xiao, Wen-Sheng Shu, and Wen-Jun Li. Comparative genomics analysis of nitriliruptoria reveals the genomic differences and salt adaptation strategies. Extremophiles, 24:249-264, Dec 2020. URL: https://doi.org/10.1007/s00792-019-01150-3, doi:10.1007/s00792-019-01150-3. This article has 21 citations and is from a peer-reviewed journal.

25. (reang2024extremozymesandcompatible pages 1-2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 16 citations and is from a peer-reviewed journal.

26. (galisteo2023astepinto pages 1-2): Cristina Galisteo, Rafael R. de la Haba, Cristina Sánchez-Porro, and Antonio Ventosa. A step into the rare biosphere: genomic features of the new genus terrihalobacillus and the new species aquibacillus salsiterrae from hypersaline soils. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1192059, doi:10.3389/fmicb.2023.1192059. This article has 12 citations and is from a peer-reviewed journal.

27. (martinezespinosa2024halophilicarchaeaas pages 4-5): Rosa María Martínez-Espinosa. Halophilic archaea as tools for bioremediation technologies. Applied Microbiology and Biotechnology, Jun 2024. URL: https://doi.org/10.1007/s00253-024-13241-z, doi:10.1007/s00253-024-13241-z. This article has 37 citations and is from a domain leading peer-reviewed journal.