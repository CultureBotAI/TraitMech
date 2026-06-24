---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:08:31.554746'
end_time: '2026-06-18T01:28:39.254085'
duration_seconds: 1207.7
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: psychrotolerant
  trait_identifier: METPO:1000618
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: psychrotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature preference in which growth can occur at low temperatures
    without an obligate low-temperature preference.
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel
    psychrotolerant bacterium (Organism example: Pseudomonas guineae is described
    as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity
    (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant
    facultative adaptation overcomes without full psychrophile dedication.)'
  causal_graph_summary: 'psychrotolerant_facultative_cold_adaptation: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** psychrotolerant
- **METPO identifier:** METPO:1000618
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel psychrotolerant bacterium (Organism example: Pseudomonas guineae is described as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant facultative adaptation overcomes without full psychrophile dedication.)
- **Existing causal graph summary:** psychrotolerant_facultative_cold_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **psychrotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrotolerant.yaml`.

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
- **Trait label:** psychrotolerant
- **METPO identifier:** METPO:1000618
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel psychrotolerant bacterium (Organism example: Pseudomonas guineae is described as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant facultative adaptation overcomes without full psychrophile dedication.)
- **Existing causal graph summary:** psychrotolerant_facultative_cold_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **psychrotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrotolerant.yaml`.

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


## Research report: Psychrotolerant (METPO:1000618) as a microbial TraitMech causal graph candidate

**Target trait:** psychrotolerant (METPO:1000618)  
**Trait category:** ENVIRONMENT  
**Definition (given):** “A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.”

### 1) Scope summary (definitions, boundary cases, assays)

**Current operational understanding.** Across microbiology subfields, *psychrotolerant* is typically synonymous with *psychrotroph/psychrotrophic* (especially in food microbiology) and denotes organisms that **can grow at refrigeration temperatures (commonly 4 °C, sometimes defined as <7 °C), but have growth optima above the psychrophile range**. Ramón et al. define psychrotolerant/psychrotroph microorganisms as those that “can grow at **4 °C** and have optimal growth temperatures **above 20 °C** (contrasted with psychrophiles that grow at 0 °C and have optimum around 15 °C).” (ramon2023ageneraloverview pages 1-2). Moyer et al. similarly distinguish psychrophiles (optimum ≈15 °C or lower; max ≈20 °C) from psychrotrophs/psychrotolerant, which “grow at low temperatures but have optimum and maximum above 15 °C and ~20 °C” and note that food microbiologists prefer the term “psychrotrophic.” (moyer2017psychrophilesandpsychrotrophs pages 1-2). In cold-environment isolates, Ponder et al. describe permafrost isolates as “psychrotolerant in that they can grow at **4 °C and above 20 °C**.” (ponder2005characterizationofpotential pages 1-2).

**Boundary cases.** A key curation caution is that **minimum growth temperature alone is insufficient**: some microbes can grow subzero but still have mesophile-like optima (e.g., Planococcus halocryophilus; described in foundational scope text) (moyer2017psychrophilesandpsychrotrophs pages 1-2). For curation, the trait should be tied to a **growth-temperature profile** (minimum + ability at 4 °C/7 °C + optimum) rather than a single cutoff.

**Assay implications.** Practical assays include (i) growth/no-growth at 4 °C and at >20 °C, (ii) growth at ≤7 °C in food matrices (milk/meat/fish), and (iii) Arrhenius plots of growth rate versus temperature used in cold-environment studies (ponder2005characterizationofpotential pages 1-2).

### 2) Key mechanistic concepts (entities that enable psychrotolerant growth)

Psychrotolerant growth is generally treated as a **systems property** of cells under low temperature, mediated by membrane physics, solute/osmoprotection, protein/RNA homeostasis, and extracellular matrices. A central mechanistic theme is **homeoviscous/homeophasic membrane adaptation**: at low temperatures membranes become more rigid/thicker, impairing embedded protein function and transport, so cells remodel lipids to restore function (moyer2017psychrophilesandpsychrotrophs pages 1-2, sidarta2024lipidphaseseparation pages 1-2, ramon2023ageneraloverview pages 2-4).

#### 2.1 Membrane rigidification as the initiating stressor
Sidarta et al. (2024) summarize the physical trigger: “Cold shock causes **membrane rigidification and concomitant thickening**, potentially culminating in a gel-phase transition.” (sidarta2024lipidphaseseparation pages 1-2).

#### 2.2 Lipid remodeling and quantitative membrane-fluidity measurements (recent 2024 developments)
**Direct quantification of membrane fluidity in vivo.** Barbotin et al. (Biophysical Journal 2024; preprint DOI in retrieved text) introduced TIR-FCS to quantify membrane fluidity proxies via diffusion coefficients of membrane dyes in *Bacillus subtilis*. They report a ~2× decrease in diffusion after a 37→20 °C shift: Nile Red D37°C = 4.4±0.3 µm²/s vs D20°C = 2.2±0.2 µm²/s, and Di4-ANEPPS D37°C = 1.9±0.1 vs D20°C = 0.9±0.07 µm²/s (barbotin2024quantificationofmembrane pages 10-11). They further report “the observed adaptation timescale is **~30 minutes**,” consistent with rapid fatty-acid remodeling (barbotin2024quantificationofmembrane pages 10-11). These kinds of quantitative assays provide potential *TraitMech measurement nodes* (“membrane dye diffusion coefficient”, “time to recovery of steady-state fluidity”) for evaluating psychrotolerant adaptation.

**Hopanoid unsaturation shifts with temperature.** Ramón et al. review quantitative evidence for lipid-like membrane components: as growth temperature decreased from 20 to 4 °C, “the total percent of **unsaturated hopanoids increased from 27 to 49%**.” (ramon2023ageneraloverview pages 4-5).

#### 2.3 Two-component sensing and the Bacillus DesK/DesR/des module (mechanistic exemplar)
A particularly well-characterized causal chain links **membrane thickness sensing** to **fatty-acid desaturation**:

* Low temperature → thickened membrane activates DesK kinase state (“membrane thickening upon cooling activates DesK … into a kinase-dominant state”) (sidarta2024lipidphaseseparation pages 1-2).
* DesK → DesR phosphorylation (“DesK … phosphorylates DesR”) (sidarta2024lipidphaseseparation pages 1-2).
* P-DesR → des transcription (“P-DesR tetramers bind Pdes to induce des expression”) (sidarta2024lipidphaseseparation pages 1-2).
* Des desaturase → lipid desaturation → fluidization (“Des desaturates fatty acyl chains, causing membrane fluidization and decreased bilayer thickness”) (sidarta2024lipidphaseseparation pages 1-2).
* Negative feedback: “membrane fluidization and decreased bilayer thickness trigger DesK phosphatase activity” stopping des transcription (sidarta2024lipidphaseseparation pages 2-5).

This module is **taxon-specific (B. subtilis model)** but it is valuable as a *curatable mechanistic pattern* for “membrane physical state sensing → transcriptional program → lipid remodeling” (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 2-5).

Recent nuance: Sidarta et al. report that in vivo Pdes activation did not correlate cleanly with bulk fluidity readouts and that harsh cold shifts could impair sensing via lipid phase separation, suggesting that **DesK may sense subtle changes** and that some commonly used reporters may miss them (sidarta2024lipidphaseseparation pages 12-14, sidarta2024lipidphaseseparation pages 5-9).

#### 2.4 Compatible solutes and osmoprotection (chemicals + genes/transporters)
**Concept.** Compatible solutes act as cryo-/osmo-protectants and chemical chaperones. Purwar & Srivastava list compatible solutes such as “glycine betaine, trehalose, glycerol, sucrose, sarcosine, mannitol, and sorbitol” and attribute protective functions including freezing point depression and stabilization of proteins/membranes (purwar2024adaptationsofpsychrophilic pages 10-11). These solutes are also described as preventing aggregation and scavenging radicals in cold stress (purwar2024adaptationsofpsychrophilic pages 10-11).

**Gene/transport-level evidence (2024 primary transcriptomics).** Li et al. (Frontiers Microbiology 2024) studied a *Rhodococcus* strain at 10 °C and report upregulation of a “betaine synthesis gene (**betB**)” and multiple transporter systems for organic osmoregulators, listing “ProP, OpuB, OpuC, OsmX, MalE, MalF, SugB” among transporters for proline/glycine betaine/carnitine/choline and others (li2024mechanismsunderlyingthe pages 10-12). This supports curating edges from **transport capacity → compatible-solute accumulation → low-temperature adaptation**.

#### 2.5 EPS/biofilm-like extracellular matrices
EPS is repeatedly linked to cold survival.

*Purwar & Srivastava* state: “EPS surrounding cells play a critical role in cold adaptation by providing protection against freeze-thaw cycles and acting as cryoprotectants.” (purwar2024adaptationsofpsychrophilic pages 8-10).

*Moyer et al.* state: “the production of exopolysaccharides also seems to yield an important role in the cryoprotection of psychrophiles and psychrotrophs,” and they cite high EPS concentrations at low temperatures in sea ice (moyer2017psychrophilesandpsychrotrophs pages 2-3).

*Ponder et al.* add supportive but more tentative language that a “membrane-associated exopolysaccharide … may improve survival” and cite sea-ice EPS accumulation supporting a stabilizing role (ponder2005characterizationofpotential pages 10-11).

### 3) Candidate nodes for `psychrotolerant.yaml` (grouped by type)

Below are curation-oriented node candidates; where stable grounding is obvious, CURIE types are suggested (IDs should be filled in during curation; no identifiers are invented here).

#### 3.1 Phenotype / trait nodes
- **psychrotolerant** (METPO:1000618)
- psychrotroph / psychrotrophic (label-only synonym node; map-to METPO:1000618 in curation)
- growth at 4 °C (assay endpoint) (ramon2023ageneraloverview pages 1-2, ponder2005characterizationofpotential pages 1-2)
- growth below 7 °C (food microbiology operational criterion) (oh2024psychrotrophicbacteriathreatening pages 1-5)

#### 3.2 Environmental / experimental nodes
- low temperature / cold shock (ENVO candidate: “cold environment”; label-only if exact ENVO term not chosen)
- refrigerated food chain / cold storage (ENVO or food processing environment label-only) (oh2024psychrotrophicbacteriathreatening pages 1-5, kovacova2024effectofselected pages 1-2)
- freeze–thaw cycles (label-only) (purwar2024adaptationsofpsychrophilic pages 8-10)

#### 3.3 Membrane composition / physical state nodes
- membrane rigidification; membrane thickness increase (GO process/phenotype label-only) (sidarta2024lipidphaseseparation pages 1-2)
- membrane fluidity (GO: label-only; measurable by dye diffusion coefficients) (barbotin2024quantificationofmembrane pages 10-11)
- unsaturated fatty acids; branched-chain fatty acids; cis-monounsaturated FAs (label-only; lipid ontology optional) (ramon2023ageneraloverview pages 2-4)
- **hopanoids** and **unsaturated hopanoids** (chemical class; label-only unless CHEBI term selected) (ramon2023ageneraloverview pages 4-5)

#### 3.4 Regulatory proteins / genes (taxon-specific exemplars)
- **DesK** (sensor histidine kinase; GO MF/EC class label-only; UniProt IDs strain-specific) (sidarta2024lipidphaseseparation pages 1-2)
- **DesR** (response regulator; label-only) (sidarta2024lipidphaseseparation pages 1-2)
- **des** (fatty acid desaturase gene/protein; label-only) (sidarta2024lipidphaseseparation pages 1-2)
- **betB** (betaine aldehyde dehydrogenase; label-only) (li2024mechanismsunderlyingthe pages 10-12)
- Transporters: **ProP**, **OpuB**, **OpuC**, **OsmX**, **MalE**, **MalF**, **SugB** (label-only; UniProt/KEGG grounding recommended later) (li2024mechanismsunderlyingthe pages 10-12)

#### 3.5 Compatible solutes / metabolites (CHEBI grounding recommended)
- glycine betaine (CHEBI) (purwar2024adaptationsofpsychrophilic pages 10-11, li2024mechanismsunderlyingthe pages 10-12)
- trehalose (CHEBI) (purwar2024adaptationsofpsychrophilic pages 10-11)
- glycerol (CHEBI) (purwar2024adaptationsofpsychrophilic pages 10-11)
- proline (CHEBI) (li2024mechanismsunderlyingthe pages 10-12)
- carnitine, choline (CHEBI) (li2024mechanismsunderlyingthe pages 10-12)

#### 3.6 Extracellular matrix nodes
- exopolysaccharide / EPS (GO biological process “biofilm formation” could be added as separate node; EPS itself as material entity label-only) (purwar2024adaptationsofpsychrophilic pages 8-10, moyer2017psychrophilesandpsychrotrophs pages 2-3)

#### 3.7 Applied-food microbiology nodes (real-world implementation)
- Pseudomonas spp. (NCBITaxon; or genus-level label-only) (kovacova2024effectofselected pages 1-2)
- Listeria spp./L. monocytogenes (NCBITaxon) (oh2024psychrotrophicbacteriathreatening pages 29-34)
- milk spoilage; proteolysis; lipolysis (GO processes label-only) (kovacova2024effectofselected pages 1-2)

### 4) Evidence-backed candidate causal edges (triples)

The following artifact consolidates candidate edges with direct snippets, references, and notes.

| Subject (node) | Predicate | Object (node) | Evidence snippet (quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| psychrotolerant microbe | capable_of_growth_at | 4°C | “psychrotolerant/psychrotroph microbes ... can grow at 4 °C and have optimal growth temperatures above 20 °C” (ramon2023ageneraloverview pages 1-2) | 10.1007/s42770-023-01057-4 (2023), https://doi.org/10.1007/s42770-023-01057-4 | Strong scope-defining edge; aligns with METPO definition. |
| psychrotolerant microbe | has_optimal_growth_temperature_above | 20°C | “permafrost isolates are not psychrophiles, but psychrotolerant in that they can grow at 4 C and above 20 C” (ponder2005characterizationofpotential pages 1-2) | 10.1016/j.femsec.2004.12.003 (2005), https://doi.org/10.1016/j.femsec.2004.12.003 | Useful boundary-case definition; older but directly operational. |
| low temperature shift | causes | membrane rigidification and thickening | “Cold shock causes membrane rigidification and concomitant thickening, potentially culminating in a gel-phase transition” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Strong mechanistic starter edge for causal graph. |
| membrane thickening upon cooling | activates | DesK kinase state | “membrane thickening upon cooling activates DesK ... into a kinase-dominant state” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Model established in Bacillus subtilis; taxon-specific regulatory edge. |
| DesK | phosphorylates | DesR | “DesK autophosphorylates at His188, phosphorylates DesR” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Specific two-component signaling edge; likely curatable as taxon-specific exemplar. |
| phosphorylated DesR | induces_expression_of | des fatty acid desaturase gene | “P-DesR tetramers bind Pdes to induce des expression” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Strong within Bacillus des system; not universal to all psychrotolerants. |
| Des fatty acid desaturase | increases | membrane lipid unsaturation | “Des desaturates fatty acyl chains” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Direct enzyme-to-lipid-composition edge. |
| increased fatty acid unsaturation | causes | membrane fluidization and decreased bilayer thickness | “Des desaturates fatty acyl chains, causing membrane fluidization and decreased bilayer thickness” (sidarta2024lipidphaseseparation pages 1-2) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Strong mechanistic edge connecting lipid remodeling to phenotype. |
| membrane fluidization and decreased thickness | activates | DesK phosphatase activity | “membrane fluidization and decreased bilayer thickness trigger DesK phosphatase activity” (sidarta2024lipidphaseseparation pages 2-5) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Negative-feedback edge in des system. |
| DesK phosphatase activity | decreases | des transcription | “leading to DesK-mediated dephosphorylation of P-DesR and stopping des transcription” (sidarta2024lipidphaseseparation pages 2-5) | 10.1128/spectrum.03925-23 (2024), https://doi.org/10.1128/spectrum.03925-23 | Negative-feedback shutdown; taxon-specific. |
| growth temperature decrease (20→4°C) | increases | unsaturated hopanoids | “as the growth temperature decreased from 20 to 4 °C, the total percent of unsaturated hopanoids increased from 27 to 49%” (ramon2023ageneraloverview pages 4-5) | 10.1007/s42770-023-01057-4 (2023), https://doi.org/10.1007/s42770-023-01057-4 | Quantitative compositional adaptation; likely broader than one taxon but still review-synthesized. |
| acute cold shock (37→20°C) | decreases | membrane marker diffusion | “Nile Red D37°C = 4.4 +/- 0.3 µm2/s and D20°C = 2.2 +/- 0.2 ... Di4-ANEPPS D37°C = 1.9 +/- 0.1 and D20°C = 0.9 +/- 0.07” (barbotin2024quantificationofmembrane pages 10-11) | 10.1101/2023.10.13.562271 (2024), https://doi.org/10.1101/2023.10.13.562271 | Quantitative proxy for fluidity loss; DOI resolves to preprint DOI in retrieved context, so curation should verify final journal DOI if needed. |
| membrane adaptation after cold shock | recovers | steady-state fluidity within ~30 min | “the observed adaptation timescale is ~30 minutes, consistent with reported fatty-acid remodeling within 30 min” (barbotin2024quantificationofmembrane pages 10-11) | 10.1101/2023.10.13.562271 (2024), https://doi.org/10.1101/2023.10.13.562271 | Quantitative timing edge; same DOI caveat as above. |
| compatible solute accumulation | protects | proteins and membranes during low-temperature stress | “compatible solutes ... depress freezing point, stabilize proteins and membranes, ... scavenge radicals, and act as cryoprotectants” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537 (2024), https://doi.org/10.37256/amtt.5220244537 | Broad review-based edge; good high-level curation target. |
| compatible solutes (glycine betaine, trehalose, glycerol, sucrose, sarcosine, mannitol, sorbitol) | supports | low-temperature adaptation | “glycine betaine, trehalose, glycerol, sucrose, sarcosine, mannitol, and sorbitol accumulate in cold-adapted bacteria and contribute to low-temperature survival” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537 (2024), https://doi.org/10.37256/amtt.5220244537 | Collapses several chemicals into one edge; could be split into separate CHEBI-grounded nodes later. |
| ProP/OpuB/OpuC/OsmX/MalE/MalF/SugB transport systems | enables_uptake_of | organic osmoregulators / compatible solutes | “Genes for transport of organic osmoregulators — explicitly listing proline, glycine betaine, carnitine, choline ... and their transporters (ProP, OpuB, OpuC, OsmX, MalE, MalF, SugB)” (li2024mechanismsunderlyingthe pages 10-12) | 10.3389/fmicb.2024.1465627 (2024), https://doi.org/10.3389/fmicb.2024.1465627 | Strong transporter edge, but from one Rhodococcus strain under 10°C transcriptomics. |
| betB | contributes_to | glycine betaine synthesis during low-temperature adaptation | “at 10°C RCBS9 ... increased expression of a betaine synthesis gene (betB)” (li2024mechanismsunderlyingthe pages 10-12) | 10.3389/fmicb.2024.1465627 (2024), https://doi.org/10.3389/fmicb.2024.1465627 | Gene-specific edge; taxon- and condition-specific. |
| extracellular polymeric substances (EPS) | provides | cryoprotection against freeze-thaw cycles | “EPS surrounding cells play a critical role in cold adaptation by providing protection against freeze-thaw cycles and acting as cryoprotectants” (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537 (2024), https://doi.org/10.37256/amtt.5220244537 | Good general adaptation edge; review-based but explicit. |
| exopolysaccharide accumulation | improves | survival in cold environments | “a membrane-associated exopolysaccharide ... may improve survival” and “exopolysaccharide accumulation in sea ice supports the stabilizing role ... thought to aid environmental survival” (ponder2005characterizationofpotential pages 10-11) | 10.1016/j.femsec.2004.12.003 (2005), https://doi.org/10.1016/j.femsec.2004.12.003 | More tentative wording (“may”, “thought to”); mark uncertain. |
| psychrotrophic Pseudomonas spp. in raw milk | causes | milk spoilage via proteases and lipases active at 7°C | “proteolytic activity ... at 7°C was positive ... in 60% isolates ... lipolytic activity ... at 7°C was confirmed in 35%” (kovacova2024effectofselected pages 1-2) | 10.24425/pjvs.2024.149353 (2024), https://doi.org/10.24425/pjvs.2024.149353 | Strong applied edge connecting psychrotolerance to spoilage phenotype. |
| raw cow milk samples | contains | psychrotrophic Pseudomonas isolates | “in a PCR survey of 320 raw milk samples, 73 Pseudomonas isolates were found” (kovacova2024effectofselected pages 1-2) | 10.24425/pjvs.2024.149353 (2024), https://doi.org/10.24425/pjvs.2024.149353 | Prevalence/statistical evidence rather than mechanism; useful application edge. |
| refrigerated animal-derived foods | are_contaminated_by | psychrotrophic Listeria spp. | “raw cow milk 10/90 (22.6%), raw milk 41/140 (29.2%), raw meats 103/295 (34.9%), poultry 57/158 (36.1%)” (oh2024psychrotrophicbacteriathreatening pages 29-34) | 10.5851/kosfa.2024.e70 (2024), https://doi.org/10.5851/kosfa.2024.e70 | Prevalence edge from review compilation; product- and study-specific, not a universal rate. |


*Table: This table compiles candidate causal edges for the psychrotolerant trait, including scope-defining phenotype edges, membrane-centered cold adaptation mechanisms, compatible-solute and EPS protection, and applied food cold-chain evidence with quantitative statistics.*

### 5) Recent developments and latest research (prioritizing 2023–2024)

**Quantitative, live-cell membrane-fluidity assays.** The 2024 TIR-FCS approach provides a quantitative bridge between cold shock and membrane adaptation, showing a ~2× diffusion drop at 20 °C vs 37 °C and recovery within ~30 minutes (barbotin2024quantificationofmembrane pages 10-11). This is directly useful for TraitMech because it offers an observable/measurable intermediate between “temperature” and “growth capacity”.

**Revisiting the DesK/DesR model in vivo.** Sidarta et al. (2024) show that des promoter activation can be decoupled from bulk laurdan GP readouts and can be impaired by phase separation, and that deletion mutants did not show growth defects under tested rigidifying conditions—raising caution about using a single canonical module as the sole explanation of psychrotolerance (sidarta2024lipidphaseseparation pages 12-14, sidarta2024lipidphaseseparation pages 14-16, sidarta2024lipidphaseseparation pages 5-9).

**Systems-level cold adaptation synthesis.** Ramón et al. (2023) emphasize membrane-state sensing and multifactorial responses, including hopanoid unsaturation changes (27→49% unsaturated hopanoids from 20→4 °C) (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4).

**Transcriptome-guided compatible-solute machinery.** Li et al. (2024) provide gene-level edges at 10 °C, linking betaine synthesis (betB) and multiple osmoregulator transporter genes to low-temperature adaptation in *Rhodococcus* (li2024mechanismsunderlyingthe pages 10-12).

### 6) Current applications and real-world implementations

#### 6.1 Food cold-chain spoilage and safety
Psychrotrophic/psychrotolerant bacteria are widely treated as a principal threat to refrigerated animal-derived foods (meat, milk, fish). Oh & Lee (2024) define psychrotrophs as “cold-tolerant bacteria” able to grow below 7 °C and highlight prominent genera including *Pseudomonas*, *Listeria*, and *Yersinia* (oh2024psychrotrophicbacteriathreatening pages 1-5). Their review compiles prevalence in products (e.g., Listeria spp. 22.6% (10/90) in raw cow milk and 34.9% (103/295) in raw meats in cited studies) (oh2024psychrotrophicbacteriathreatening pages 29-34).

Kováčová et al. (2024) provide a concrete milk dataset: of **320 raw milk samples**, PCR identified **73 Pseudomonas isolates** (species distribution: P. putida 34.25%, P. fragi 13.70%, P. lundensis 9.59%) (kovacova2024effectofselected pages 1-2). They also quantify cold-active spoilage enzymes: proteolytic activity positive in **60%** of isolates at **7 °C** and **85%** at 25 °C; lipolytic activity **35%** at 7 °C and **70%** at 25 °C (kovacova2024effectofselected pages 1-2). These statistics justify causal edges linking “psychrotrophic growth at refrigeration temperature” to “spoilage via extracellular enzymes”.

#### 6.2 Control technologies in cold-chain contexts
Oh & Lee (2024) summarize nonthermal and adjunct technologies with measured reductions under cold/refrigerated contexts, including **cold plasma (~2 Log CFU/g reductions)** and phage/HPP approaches (oh2024psychrotrophicbacteriathreatening pages 13-17). These are real-world implementations (industrial and pre-industrial) where psychrotolerant traits directly affect control efficacy.

### 7) Expert opinions / authoritative synthesis

- Membranes are repeatedly framed as a central bottleneck: cold drives a liquid–crystalline → gel shift, and organisms must restore fluidity through lipid remodeling (ramon2023ageneraloverview pages 2-4).  
- EPS/exopolysaccharides are widely treated as cryoprotective in cold ecosystems (sea ice) and are proposed to improve survival under freezing conditions (purwar2024adaptationsofpsychrophilic pages 8-10, moyer2017psychrophilesandpsychrotrophs pages 2-3).  
- The DesK/DesR/des pathway is presented as a canonical membrane-thickness sensor with negative feedback, but 2024 work highlights that its in vivo contribution to global fluidity adaptation and growth phenotypes may be subtle and context-dependent (sidarta2024lipidphaseseparation pages 14-16, sidarta2024lipidphaseseparation pages 5-9).

### 8) Warnings / items not yet ready for curation into TraitMech

1. **Taxon specificity vs universal mechanism.** DesK/DesR/des is a strong mechanistic exemplar, but it is not universal; it should be curated either as (i) a Bacillus-specific subgraph or (ii) a generic “two-component membrane thickness sensor → desaturase expression” pattern explicitly marked taxon-specific (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16).  
2. **EPS evidence strength varies.** Some EPS claims are explicitly causal (“providing protection … acting as cryoprotectants”), but others are framed as hypotheses (“may improve survival”; “thought to aid environmental survival”) and should be marked uncertain (purwar2024adaptationsofpsychrophilic pages 8-10, ponder2005characterizationofpotential pages 10-11).  
3. **Barbotin 2024 DOI form.** The retrieved DOI corresponds to the preprint record; curators should verify the Biophysical Journal final DOI if different before freezing metadata (barbotin2024quantificationofmembrane pages 10-11).  
4. **Food prevalence statistics are study-specific.** Prevalence values compiled in reviews depend on region/product/study design; use them as evidence of relevance, not as universal rates (oh2024psychrotrophicbacteriathreatening pages 29-34).

---

## DOI-first bibliography (with dates and URLs where available)

**Core psychrotolerance/cold adaptation mechanisms (2023–2024 prioritized)**
1. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* **Brazilian Journal of Microbiology**. 2023-07. DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4)
2. Sidarta M, Martín AIL, Monsalve A, et al. *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK.* **Microbiology Spectrum**. 2024-06. DOI: **10.1128/spectrum.03925-23**. https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 12-14, sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 14-16, sidarta2024lipidphaseseparation pages 5-9, sidarta2024lipidphaseseparation pages 2-5)
3. Barbotin A, Billaudeau C, Sezgin E, Carballido-López R. *Quantification of membrane fluidity in bacteria using TIR-FCS.* **Biophysical Journal**. 2024-10 (preprint DOI in retrieved text). DOI: **10.1101/2023.10.13.562271**. https://doi.org/10.1101/2023.10.13.562271 (barbotin2024quantificationofmembrane pages 10-11)
4. Li Q, Pan H, Hao P, et al. *Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain Rhodococcus sp. RCBS9: insights from physiological and transcriptomic analyses.* **Frontiers in Microbiology**. 2024-11. DOI: **10.3389/fmicb.2024.1465627**. https://doi.org/10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 10-12)
5. Purwar S, Srivastava S. *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* **Applied Microbiology: Theory & Technology**. 2024-10. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 6-7)

**Applied psychrotroph/psychrotolerant contexts (food cold chain; 2024 prioritized)**
6. Oh H, Lee J. *Psychrotrophic Bacteria Threatening the Safety of Animal-Derived Foods: Characteristics, Contamination, and Control Strategies.* **Food Science of Animal Resources**. 2024-09. DOI: **10.5851/kosfa.2024.e70**. https://doi.org/10.5851/kosfa.2024.e70 (oh2024psychrotrophicbacteriathreatening pages 1-5, oh2024psychrotrophicbacteriathreatening pages 5-9, oh2024psychrotrophicbacteriathreatening pages 29-34, oh2024psychrotrophicbacteriathreatening pages 9-13, oh2024psychrotrophicbacteriathreatening pages 13-17)
7. Kováčová M, Výrostková J, Regecová I, et al. *Effect of selected bacteria of the genus Pseudomonas on the quality of raw cow’s milk.* **Polish Journal of Veterinary Sciences**. 2024-06. DOI: **10.24425/pjvs.2024.149353**. https://doi.org/10.24425/pjvs.2024.149353 (kovacova2024effectofselected pages 1-2, kovacova2024effectofselected pages 9-10)

**Foundational scope and cold-environment physiology (older, for definitions/boundary cases)**
8. Moyer CL, Collins RE, Morita RY. *Psychrophiles and Psychrotrophs.* **Reference Module in Life Sciences**. 2017-01. DOI: **10.1016/B978-0-12-809633-8.02282-2**. https://doi.org/10.1016/B978-0-12-809633-8.02282-2 (moyer2017psychrophilesandpsychrotrophs pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 2-3)
9. Ponder MA, Gilmour SJ, Bergholz PW, et al. *Characterization of potential stress responses in ancient Siberian permafrost psychroactive bacteria.* **FEMS Microbiology Ecology**. 2005-06. DOI: **10.1016/j.femsec.2004.12.003**. https://doi.org/10.1016/j.femsec.2004.12.003 (ponder2005characterizationofpotential pages 1-2, ponder2005characterizationofpotential pages 10-11)

**Supplementary (older) compatible-solute overview**
10. Subramanian P, Joe MM, Yim WJ, et al. *Psychrotolerance Mechanisms in Cold-Adapted Bacteria and their Perspectives as Plant Growth-Promoting Bacteria in Temperate Agriculture.* 2011-08. DOI: **10.7745/kjssf.2011.44.4.625**. https://doi.org/10.7745/kjssf.2011.44.4.625 (subramanian2011psychrotolerancemechanismsin pages 4-5)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (moyer2017psychrophilesandpsychrotrophs pages 1-2): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

3. (ponder2005characterizationofpotential pages 1-2): Monica A. Ponder, Sarah J. Gilmour, Peter W. Bergholz, Carol A. Mindock, Rawle Hollingsworth, Michael F. Thomashow, and James M. Tiedje. Characterization of potential stress responses in ancient siberian permafrost psychroactive bacteria. FEMS microbiology ecology, 53 1:103-15, Jun 2005. URL: https://doi.org/10.1016/j.femsec.2004.12.003, doi:10.1016/j.femsec.2004.12.003. This article has 147 citations and is from a peer-reviewed journal.

4. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

6. (barbotin2024quantificationofmembrane pages 10-11): Aurélien Barbotin, Cyrille Billaudeau, Erdinc Sezgin, and Rut Carballido-López. Quantification of membrane fluidity in bacteria using tir-fcs. Biophysical Journal, 123:2484-2495, Oct 2024. URL: https://doi.org/10.1101/2023.10.13.562271, doi:10.1101/2023.10.13.562271. This article has 19 citations and is from a domain leading peer-reviewed journal.

7. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

8. (sidarta2024lipidphaseseparation pages 2-5): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

10. (sidarta2024lipidphaseseparation pages 5-9): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

12. (li2024mechanismsunderlyingthe pages 10-12): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

13. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

14. (moyer2017psychrophilesandpsychrotrophs pages 2-3): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

15. (ponder2005characterizationofpotential pages 10-11): Monica A. Ponder, Sarah J. Gilmour, Peter W. Bergholz, Carol A. Mindock, Rawle Hollingsworth, Michael F. Thomashow, and James M. Tiedje. Characterization of potential stress responses in ancient siberian permafrost psychroactive bacteria. FEMS microbiology ecology, 53 1:103-15, Jun 2005. URL: https://doi.org/10.1016/j.femsec.2004.12.003, doi:10.1016/j.femsec.2004.12.003. This article has 147 citations and is from a peer-reviewed journal.

16. (oh2024psychrotrophicbacteriathreatening pages 1-5): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

17. (kovacova2024effectofselected pages 1-2): M. Kováčová, J. Výrostková, I. Regecová, E. Dudriková, J. Záhumenská, and S. Marcinčák. Effect of selected bacteria of the genus pseudomonas on the quality of raw cow’s milk. Polish Journal of Veterinary Sciences, 27 2:229-239, Jun 2024. URL: https://doi.org/10.24425/pjvs.2024.149353, doi:10.24425/pjvs.2024.149353. This article has 6 citations and is from a peer-reviewed journal.

18. (oh2024psychrotrophicbacteriathreatening pages 29-34): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

19. (sidarta2024lipidphaseseparation pages 14-16): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

20. (oh2024psychrotrophicbacteriathreatening pages 13-17): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

21. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

22. (oh2024psychrotrophicbacteriathreatening pages 5-9): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

23. (oh2024psychrotrophicbacteriathreatening pages 9-13): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

24. (kovacova2024effectofselected pages 9-10): M. Kováčová, J. Výrostková, I. Regecová, E. Dudriková, J. Záhumenská, and S. Marcinčák. Effect of selected bacteria of the genus pseudomonas on the quality of raw cow’s milk. Polish Journal of Veterinary Sciences, 27 2:229-239, Jun 2024. URL: https://doi.org/10.24425/pjvs.2024.149353, doi:10.24425/pjvs.2024.149353. This article has 6 citations and is from a peer-reviewed journal.

25. (subramanian2011psychrotolerancemechanismsin pages 4-5): Parthiban Subramanian, Manoharan Melvin Joe, Woo-Jong Yim, Bo-Hui Hong, Sherlyn C. Tipayno, Venkatakrishnan Sivaraj Saravanan, Jae-Hong Yoo, Jong-Bae Chung, Tahera Sultana, and Tong-Min Sa. Psychrotolerance mechanisms in cold-adapted bacteria and their perspectives as plant growth-promoting bacteria in temperate agriculture. ArXiv, 44:625-636, Aug 2011. URL: https://doi.org/10.7745/kjssf.2011.44.4.625, doi:10.7745/kjssf.2011.44.4.625. This article has 25 citations.