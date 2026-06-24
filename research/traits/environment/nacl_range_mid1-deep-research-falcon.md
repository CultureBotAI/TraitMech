---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:24:00.787947'
end_time: '2026-06-17T23:41:01.016422'
duration_seconds: 1020.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range mid1
  trait_identifier: METPO:1000470
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl range phenotype in which the growth-supporting NaCl range spans\
    \ approximately 1\u20133% (w/v), characteristic of slight-halophilic or halotolerant\
    \ organisms."
  parent_traits: METPO:1000334
  synonyms: Halotolerant, Slight halophile, NaR_1_to_3
  evidence_summary: "DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review\
    \ supports the 1\u20133% NaCl growth range as the slight-halophile/halotolerant\
    \ category.)"
  causal_graph_summary: 'nacl_range_mid1_slight_halophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range mid1
- **METPO identifier:** METPO:1000470
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 1–3% (w/v), characteristic of slight-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Slight halophile, NaR_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl growth range as the slight-halophile/halotolerant category.)
- **Existing causal graph summary:** nacl_range_mid1_slight_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid1.yaml`.

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
- **Trait label:** NaCl range mid1
- **METPO identifier:** METPO:1000470
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 1–3% (w/v), characteristic of slight-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Slight halophile, NaR_1_to_3
- **Existing evidence:** DOI:10.1093/femsre/fuy009: slight halophile (Osmoadaptation review supports the 1–3% NaCl growth range as the slight-halophile/halotolerant category.)
- **Existing causal graph summary:** nacl_range_mid1_slight_halophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid1.yaml`.

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


## Research report: NaCl range mid1 (slight-halophile/halotolerant growth at ~1–3% w/v NaCl)

### 1) Scope summary (trait definition, boundaries, and assay interpretation)

**Trait definition.** The target trait “NaCl range mid1” (METPO:1000470) represents a growth-supporting **NaCl range spanning approximately 1–3% (w/v)**, matching the conventional category **“slight halophiles”** (and overlapping operationally with many “halotolerant” organisms depending on assay design). The clearest categorical definition found states: **“slight halophiles grow best in media with 1 to 3% NaCl”**. (sessitsch2008microbiologyofextreme pages 100-102)

**Nearby traits / boundary conditions.** In the same classification framework, **moderate halophiles** are distinguished by higher optima: **“grow optimally in media with 3 to 15% NaCl”**. (sessitsch2008microbiologyofextreme pages 100-102)

A second widely used definition emphasizes the dependence on molarity and “optimal growth” rather than absolute range: **“moderate halophiles as organisms growing optimally between 0.5 and 2.5 M salt”**. (ventosa1998biologyofmoderately pages 2-3)

**Halotolerant vs. slight-halophilic edge cases.** Halotolerant organisms are defined by the ability to grow from **no added salt** up to relatively high salinity (e.g., *Staphylococcus aureus* cited as growing up to 8% NaCl). (ventosa1998biologyofmoderately pages 2-3)

**Assay/medium dependence (important curation warning).** Salt requirement/tolerance depends on **medium composition** (minimal vs. complex), **temperature**, and **osmoprotectant availability**. A key example is that compatible-solute supplementation can shift the apparent NaCl requirement: **“glucose or glycerol lowered the NaCl requirement to 0.3 M”** in at least one system. (ventosa1998biologyofmoderately pages 12-13)

**Implication for METPO/TraitMech curation.** The most curator-safe interpretation is: *NaCl range mid1* is a **phenotype defined by an observed growth window or optimum in a specified medium/assay** (typically laboratory culture), not necessarily a strict ecological niche boundary.

---

### 2) Current mechanistic understanding (key concepts and definitions)

Microbial growth at 1–3% NaCl is generally enabled by **osmoadaptation**, classically through:

1. **Ion homeostasis / “salt-in” components** (rapid uptake/management of Na+ and K+; in some taxa KCl accumulation), and
2. **“Salt-out” compatible-solute strategies** (biosynthesis and/or uptake of organic osmolytes such as ectoine, glycine betaine, proline, glutamate). (lee2018naclsaturatedbrinesare pages 15-17)

Even when a species’ overall tolerance spans much higher NaCl, **the same modules** often support growth in the 1–3% window.

#### Mechanistic modules supported by recent evidence (2024 emphasis)

**A. Emergency osmotic response: Na+/K+ uptake and amino acid pool shifts.** In *Halomonas elongata*, within a **tolerable NaCl shock range of 1–8%**, cells rapidly mitigate osmotic stress by **“uptaking sodium and potassium ions”** and **augmenting intracellular amino acid pools** (notably **glutamate** and **glutamine**). (yu2024temporaldynamicsof pages 1-2)

**B. Compatible solute dominance for sustained osmoprotection (ectoine-centered).** In the same system, **“ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant”**, indicating a delayed but decisive shift from ion/amino-acid buffering to ectoine-based osmoprotection. (yu2024temporaldynamicsof pages 1-2)

**C. Genetic causal evidence for the 1–3% boundary (ΔectABC).** A particularly trait-relevant perturbation is the ectoine operon knockout in *H. elongata*: **“ΔectABC… only grows well in minimal medium containing up to 3% NaCl”**. This links loss of ectoine biosynthesis directly to a growth limit at the upper edge of the *mid1* range. (zou2024metabolicengineeringof pages 1-2)

**D. Alternative osmolytes can substitute for ectoine (engineering evidence).** In *H. elongata*, engineered accumulation of other osmolytes restores tolerance beyond ectoine-deficient limits. Examples include:
- **Glu overproduction** enabling growth at **6% NaCl**, and 
- **GAD-mediated conversion of Glu to GABA** (via engineered *HopgadBmut*) improving tolerance by accumulating **GABA** as an osmolyte (reported as **176.94 µmol/g cell dry weight** at 7% NaCl in the engineered strain). (zou2024metabolicengineeringof pages 1-2)

**E. Proline module as an osmolyte substitute.** Engineering *H. elongata* to overproduce proline (replacing ectoine operon with a proline biosynthesis cluster and deleting *putA*) produced a strain that “thrived” at **8% NaCl** by accumulating intracellular proline (reported **353.1 ± 40.5 µmol/g cell fresh weight**). (khanh2024metabolicpathwayengineering pages 1-2)

**F. Transport-driven osmoprotection: betaine/proline uptake systems.** In the 2024 long-term salinity adaptation study of *Natranaerobius thermophilus*, osmoprotection is linked to both synthesis and uptake of compatible solutes, including use of **glycine betaine ABC transporters (Opu/ProU families)** and **Na+/proline symporter PutP** (“facilitates the sodium ion-dependent uptake of proline”). (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19)

**G. Oxidative stress coupling and regulatory factors.** NaCl shock also induces oxidative stress, with regulatory and enzymatic antioxidant defenses including **“transcription factor cysB”** upregulation and increased peroxidase/catalase activities; the peroxidase gene **HELO_RS18165** is highlighted as part of this defense. (yu2024temporaldynamicsof pages 1-2)

---

### 3) Recent developments and latest research (prioritizing 2023–2024)

**Mechanistic multi-omics in *Halomonas elongata* under salt shock (2024).** A 2024 study integrates physiology, metabolomics, and transcriptomics to show that NaCl shock induces **both osmotic and oxidative stress** and reveals a time-resolved shift from rapid ion/amino-acid responses to delayed ectoine dominance. (yu2024temporaldynamicsof pages 1-2)

**Quantitative bioprocess-relevant metrics (2024).** Under 5–8% NaCl shock, intracellular ectoine reached **4.08 ± 0.28 g/L (5%)** and **4.58 ± 0.19 g/L (8%)** at 4 h; volumetric productivities during the first 4 h were **1230 ± 112 mg/L/h (5%)** and **1450 ± 99 mg/L/h (8%)**, and a specific ectoine production rate of **66.54 ± 1.86 mg ectoine/g DCW/h** at 8% is reported. (yu2024temporaldynamicsof pages 2-5)

**Genetic “necessity” signal aligned with the 3% boundary (2024).** The ΔectABC observation (“only grows well… up to 3% NaCl”) provides unusually direct causal evidence that can be used to justify mechanistic edges anchored on the *mid1* upper boundary. (zou2024metabolicengineeringof pages 1-2)

**Engineering alternative osmolyte strategies (2024).** Two independent 2024 *Applied and Environmental Microbiology* studies demonstrate that ectoine-deficient *H. elongata* can regain salt tolerance via engineered **GABA** or **proline** accumulation, highlighting modularity of osmolyte choice in salt tolerance. (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2)

**Transport/synthesis details for glycine betaine and proline (2024).** The 2024 *N. thermophilus* work provides explicit gene/transporter sets (Opu/ProU/BetT/PutP; *gsmt/sdmt*) tied to increased intracellular compatible solutes with rising salinity, offering curated transport-and-biosynthesis nodes. (xing2024thepolyextremophilenatranaerobius pages 14-17)

---

### 4) Current applications and real-world implementations

#### A. Industrial biotechnology: ectoine production and saline biomanufacturing

**Industrial ectoine production context.** *Halomonas elongata* is described as an “industrially important strain for ectoine production,” and *Halomonas* systems are positioned as **high-salinity seawater-based unsterile open fermentation chassis** for low-cost biomanufacturing. (zou2024metabolicengineeringof pages 1-2)

**Salinity ranges relevant to including the 1–3% window.** *H. elongata* industrial strains are reported to adapt across broad NaCl ranges that include 1–3% (e.g., **0.1%–32.5%** and **0.3%–21%** NaCl, depending on strain). (zou2024metabolicengineeringof pages 1-2, khanh2024metabolicpathwayengineering pages 1-2)

**Industrial process implementation (“bacterial milking”).** An authoritative review reports ectoine recovery by osmotic down-shock **“10→2% NaCl causing excretion of ~80% intracellular ectoine”**, with recovery by subsequent hyperosmotic shock and a yield of **“about 2 g ectoine per liter of medium per day.”** (ventosa1998biologyofmoderately pages 33-33)

#### B. Bioremediation at high salt (contextual, adjacent to mid1)

A review describes high-salt wastewater treatment using moderate halophiles, including a biofilm reactor removing **“more than 99% of the phenol”** from waste with **15% salt**. This is outside the 1–3% trait window but is relevant as a downstream application of halotolerance modules that scale across salinities. (ventosa1998biologyofmoderately pages 33-33)

---

### 5) Expert opinions and analysis (authoritative synthesis)

**Consensus framing of mechanisms.** An authoritative FEMS Microbiology Reviews synthesis distinguishes two core strategies: “salt-in” versus “salt-out/compatible solute,” noting that halotolerant and moderate halophiles often rely on ion exclusion and compatible solutes (e.g., glycine betaine) rather than deeply “acidic proteome” salt-in specialization. (lee2018naclsaturatedbrinesare pages 15-17)

**Interpretation for NaCl range mid1.** The *mid1* phenotype is most consistent with organisms whose enzymes/cytoplasm remain functional near seawater salinity (≈3.5% NaCl) and slightly below, using **compatible solutes and regulated transport** rather than obligate salt-in proteome remodeling. Mechanistically, the strongest curation-ready evidence presently ties *mid1* to **ectoine availability (ectABC)** and to **rapid ion/compatible-solute responses** that stabilize growth when moving between low and modest NaCl conditions (including 1–3%). (zou2024metabolicengineeringof pages 1-2, yu2024temporaldynamicsof pages 1-2)

---

## Candidate nodes (curation-oriented)

| Node type | Candidate node label | Suggested CURIE | Brief justification | Key supporting citation IDs |
|---|---|---|---|---|
| Trait/Phenotype | NaCl range mid1 | METPO:1000470 | Target trait: growth-supporting NaCl range ~1–3% (w/v), corresponding to slight halophile / halotolerant boundary | (sessitsch2008microbiologyofextreme pages 100-102, ventosa1998biologyofmoderately pages 2-3) |
| Trait/Phenotype | slight halophile |  | Explicitly defined as organisms that “grow best in media with 1 to 3% NaCl” | (sessitsch2008microbiologyofextreme pages 100-102) |
| Trait/Phenotype | halotolerant |  | Boundary case: organisms able to grow from no salt to relatively high salt; useful distinction from obligate slight halophiles | (ventosa1998biologyofmoderately pages 2-3) |
| Trait/Phenotype | moderate halophile |  | Adjacent trait; defined as optimal growth at 3–15% NaCl or 0.5–2.5 M salt, useful for excluding higher-salt phenotypes | (sessitsch2008microbiologyofextreme pages 100-102, ventosa1998biologyofmoderately pages 2-3) |
| Environment/Assay | sodium chloride stress / NaCl shock | CHEBI:26710 | Core environmental input used experimentally to elicit osmotic stress responses and test tolerance windows | (yu2024temporaldynamicsof pages 1-2) |
| Environment/Assay | 1–3% (w/v) NaCl medium |  | Assay context that operationalizes the target phenotype | (sessitsch2008microbiologyofextreme pages 100-102) |
| Environment/Assay | minimal medium with NaCl |  | Important assay background because salt requirement changes with medium composition | (ventosa1998biologyofmoderately pages 12-13, zou2024metabolicengineeringof pages 1-2) |
| Environment/Assay | compatible-solute-supplemented medium |  | Medium composition can lower apparent NaCl requirement (e.g., glucose/glycerol effect) | (ventosa1998biologyofmoderately pages 12-13) |
| Processes/Pathways | osmoadaptation | GO:0006970 | Central biological process underlying growth at elevated NaCl | (yu2024temporaldynamicsof pages 1-2, lee2018naclsaturatedbrinesare pages 15-17) |
| Processes/Pathways | response to osmotic stress | GO:0006970 | Immediate stress-response program engaged after NaCl upshift | (yu2024temporaldynamicsof pages 1-2) |
| Processes/Pathways | ectoine biosynthetic process | GO:0019491 | Major compatible-solute pathway repeatedly linked to salt tolerance | (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| Processes/Pathways | glycine betaine biosynthetic process | GO:0009088 | Supported by gsmt/sdmt methylation pathway evidence under salt stress | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Processes/Pathways | proline biosynthetic process | GO:0006561 | Alternate osmolyte production route that restores tolerance in engineered strains | (khanh2024metabolicpathwayengineering pages 1-2) |
| Processes/Pathways | potassium ion transport | GO:0006813 | Emergency osmotic balancing response after NaCl shock | (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 18-18) |
| Processes/Pathways | sodium ion transport | GO:0006814 | Early ion uptake and Na+-coupled osmolyte transport contribute to salt response | (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Processes/Pathways | cellular response to oxidative stress | GO:0034599 | Salt shock induces oxidative stress alongside osmotic stress | (yu2024temporaldynamicsof pages 1-2) |
| Genes/Proteins/Complexes | ectABC operon |  | Canonical ectoine biosynthesis locus; deletion constrains growth to up to 3% NaCl in H. elongata | (zou2024metabolicengineeringof pages 1-2) |
| Genes/Proteins/Complexes | EctA |  | Part of ectoine biosynthetic machinery; curate as component if gene-level detail is desired | (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| Genes/Proteins/Complexes | EctB |  | Part of ectoine biosynthetic machinery; common mechanistic node for ectoine pathway | (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/Proteins/Complexes | EctC |  | Part of ectoine biosynthetic machinery; common mechanistic node for ectoine pathway | (khanh2024metabolicpathwayengineering pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| Genes/Proteins/Complexes | gsmt |  | Glycine N-methyltransferase gene in betaine methylation pathway; upregulated under salt | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | sdmt |  | Sarcosine dimethylglycine N-methyltransferase gene in betaine methylation pathway; upregulated under salt | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | GSMT |  | Enzyme product of gsmt supporting glycine betaine synthesis | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | SDMT |  | Enzyme product of sdmt supporting glycine betaine synthesis | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | OpuA ABC transporter |  | Compatible-solute uptake system implicated in osmoprotection; broadly relevant osmolyte importer | (xing2024thepolyextremophilenatranaerobius pages 14-17, yu2024temporaldynamicsof pages 18-18) |
| Genes/Proteins/Complexes | OpuB transporter |  | Glycine betaine/carnitine/choline-type uptake system implicated in salt adaptation | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | OpuC transporter |  | Compatible-solute uptake system found in salt adaptation module | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | OpuD transporter |  | BCCT-family compatible-solute transporter implicated in halotolerance | (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | ProU transporter (ProVWX/ProX) |  | ABC-type glycine betaine uptake system used in adaptation to salinity | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Genes/Proteins/Complexes | BetT |  | BCCT-family transporter associated with betaine/choline uptake under salt stress | (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 4-6) |
| Genes/Proteins/Complexes | PutP |  | Na+/proline symporter facilitating sodium-dependent proline uptake | (xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Genes/Proteins/Complexes | proB |  | Encodes γ-glutamyl kinase in proline biosynthesis route used to restore salt tolerance | (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/Proteins/Complexes | proA |  | Encodes γ-glutamyl phosphate reductase in proline biosynthesis route | (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/Proteins/Complexes | proC |  | Encodes pyrroline-5-carboxylate reductase in proline biosynthesis route | (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/Proteins/Complexes | putA |  | Proline catabolic gene; deletion increases proline retention and salt tolerance | (khanh2024metabolicpathwayengineering pages 1-2) |
| Genes/Proteins/Complexes | cysB |  | Salt-shock-upregulated transcription factor linked to sulfur metabolism and cysteine biosynthesis | (yu2024temporaldynamicsof pages 1-2) |
| Genes/Proteins/Complexes | HELO_RS18165 |  | Peroxidase gene upregulated after salt shock as part of antioxidant defense | (yu2024temporaldynamicsof pages 1-2) |
| Genes/Proteins/Complexes | catalase (CAT) |  | Antioxidant enzyme activity rises after salt shock | (yu2024temporaldynamicsof pages 1-2) |
| Genes/Proteins/Complexes | peroxidase (POD) |  | Antioxidant enzyme activity rises after salt shock | (yu2024temporaldynamicsof pages 1-2) |
| Genes/Proteins/Complexes | TrkH |  | Potassium uptake system cited as relevant to osmoregulation in halophiles | (yu2024temporaldynamicsof pages 18-18) |
| Genes/Proteins/Complexes | TrkI |  | Potassium uptake system cited as relevant to osmoregulation in halophiles | (yu2024temporaldynamicsof pages 18-18) |
| Chemicals/Compatible solutes | ectoine | CHEBI:45974 | Dominant compatible solute in H. elongata and major osmoprotectant in halophiles | (yu2024temporaldynamicsof pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| Chemicals/Compatible solutes | hydroxyectoine | CHEBI:58170 | Stress-protective derivative of ectoine; common halophile osmolyte | (khanh2024metabolicpathwayengineering pages 1-2, reang2024extremozymesandcompatible pages 16-17) |
| Chemicals/Compatible solutes | glycine betaine | CHEBI:17750 | Primary compatible solute in several halophiles; imported and/or synthesized under salt | (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Chemicals/Compatible solutes | L-proline | CHEBI:26271 | Compatible solute whose biosynthesis/accumulation can restore salt tolerance | (khanh2024metabolicpathwayengineering pages 1-2) |
| Chemicals/Compatible solutes | L-glutamate | CHEBI:29985 | Immediate-response osmolyte / amino acid pool increase after salt shock | (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Chemicals/Compatible solutes | L-glutamine | CHEBI:28300 | Early amino acid pool augmentation after salt shock | (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 4-6) |
| Chemicals/Compatible solutes | γ-aminobutyric acid (GABA) | CHEBI:16865 | Engineered alternative osmolyte improving tolerance and pH homeostasis | (zou2024metabolicengineeringof pages 1-2) |
| Chemicals/Compatible solutes | glycerol | CHEBI:17754 | Example compatible/osmotic supplement lowering apparent NaCl requirement in some assays | (ventosa1998biologyofmoderately pages 12-13) |
| Ions | sodium ion | CHEBI:29101 | Core extracellular stressor and intracellularly transported ion in salt-shock response | (yu2024temporaldynamicsof pages 1-2) |
| Ions | potassium ion | CHEBI:29103 | Emergency-response ion accumulated for osmotic balance | (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| Ions | chloride | CHEBI:17996 | Relevant counterion in halophile ion-homeostasis strategies, especially KCl-type balancing | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Taxa | Halomonas elongata |  | Best-supported model from 2024 literature for linking osmoadaptation mechanisms to growth limits, including 3% boundary in ΔectABC mutant | (yu2024temporaldynamicsof pages 1-2, zou2024metabolicengineeringof pages 1-2) |
| Taxa | Natranaerobius thermophilus |  | Provides detailed 2024 evidence for transporters, glycine betaine synthesis, PutP, and K+ accumulation | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Taxa | Halobacillus halophilus |  | Comparative model for glutamate/proline-based osmoadaptation and KCl/compatible-solute strategy switching | (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 14-17) |
| Taxa | Chromohalobacter salexigens |  | Established moderate-halophile reference for ectoine-centered osmoadaptation, useful comparative taxon | (yu2024temporaldynamicsof pages 18-18, athauda2025ectoinefromhalophilic pages 2-3) |
| Taxa | Halomonadaceae |  | Family-level representative of salt-out strategists using compatible solutes rather than salt-in proteomes | (lee2018naclsaturatedbrinesare pages 15-17, ventosa1998biologyofmoderately pages 2-3) |


*Table: This table lists candidate curation nodes for the NaCl range mid1 trait, grouped by biological type and annotated with suggested stable identifiers where confidently known. It is designed to support TraitMech curation by highlighting the most evidence-backed phenotype, mechanism, molecule, ion, and taxon nodes from the gathered literature.*

---

## Candidate causal edges (subject–predicate–object triples with evidence)

| Subject node | Predicate | Object node | Evidence snippet (quoted) | Reference (DOI + URL + year) | Notes/curation flags |
|---|---|---|---|---|---|
| NaCl range mid1 (1–3% w/v) | corresponds_to | slight halophile | “slight halophiles grow best in media with 1 to 3% NaCl” (sessitsch2008microbiologyofextreme pages 100-102) | 10.1007/978-3-540-74231-9; https://doi.org/10.1007/978-3-540-74231-9; 2008 | Strong trait-definition edge; directly matches target phenotype |
| slight halophile | distinct_from | moderate halophile | “moderate halophiles ‘grow optimally in media with 3 to 15 % NaCl’” (sessitsch2008microbiologyofextreme pages 100-102) | 10.1007/978-3-540-74231-9; https://doi.org/10.1007/978-3-540-74231-9; 2008 | Strong boundary edge for neighboring trait |
| moderate halophile | defined_as | optimal growth between 0.5 and 2.5 M salt | “moderate halophiles as organisms growing optimally between 0.5 and 2.5 M salt” (ventosa1998biologyofmoderately pages 2-3) | 10.1128/MMBR.62.2.504-544.1998; https://doi.org/10.1128/mmbr.62.2.504-544.1998; 1998 | Background classification edge; helps separate mid1 from higher-salt phenotypes |
| halotolerant organism | can_grow_without | added NaCl | “Organisms able to grow over a wide range of salt concentrations, extending from no salt up to relatively high salt concentrations, are termed halotolerant” (ventosa1998biologyofmoderately pages 2-3) | 10.1128/MMBR.62.2.504-544.1998; https://doi.org/10.1128/mmbr.62.2.504-544.1998; 1998 | Useful boundary case; not all NaCl mid1 organisms are obligate halophiles |
| compatible solute supplementation (glucose/glycerol) | lowers | minimum NaCl requirement | “glucose or glycerol lowered the NaCl requirement to 0.3 M” (ventosa1998biologyofmoderately pages 12-13) | 10.1128/MMBR.62.2.504-544.1998; https://doi.org/10.1128/mmbr.62.2.504-544.1998; 1998 | Important assay-context modifier; medium-dependent, taxon-specific |
| NaCl shock within tolerable range | causes | Na+ and K+ uptake | “within the cell’s tolerable range (1–8% NaCl shock), H. elongata urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Mechanistic edge; taxon-specific to H. elongata, but plausibly generalizable |
| NaCl shock | increases | intracellular glutamate/glutamine pools | “uptaking sodium and potassium ions and augmenting intracellular amino acid pools, particularly glutamate and glutamine” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Mechanistic edge; short-term osmoadaptation response |
| ectoine biosynthesis/accumulation | enables | sustained osmoprotection under salt stress | “ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Strong mechanistic edge; taxon-specific but central to many halophiles |
| ectABC operon deletion | decreases | salt tolerance | “ΔectABC… only grows well in minimal medium containing up to 3% NaCl” (zou2024metabolicengineeringof pages 1-2) | 10.1128/AEM.01905-23; https://doi.org/10.1128/aem.01905-23; 2024 | Strong causal perturbation evidence; directly relevant to 1–3% boundary |
| glutamate overproduction | increases | NaCl tolerance | “a Glu-overproducing suppressor ‘could grow on a medium containing 6% NaCl’” (zou2024metabolicengineeringof pages 1-2) | 10.1128/AEM.01905-23; https://doi.org/10.1128/aem.01905-23; 2024 | Strong perturbation edge; taxon-specific and above target salinity range |
| HopgadBmut / GABA production | increases | salt tolerance | “the GOP-Gad strain exhibits higher salt tolerance… by accumulating high concentration of GABA as an osmolyte” (zou2024metabolicengineeringof pages 1-2) | 10.1128/AEM.01905-23; https://doi.org/10.1128/aem.01905-23; 2024 | Mechanistic engineering edge; taxon-specific, useful as alternative osmolyte evidence |
| proBm1AC-mediated proline biosynthesis | restores/enhances | growth at high salinity | “the Ect-deficient H. elongata KA1 could not grow in minimal media containing more than 4% NaCl, H. elongata HN6 thrived in the medium containing 8% NaCl by accumulating Pro” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24; 2024 | Strong perturbation evidence; above target range but supports osmolyte mechanism |
| putA deletion | increases | intracellular proline retention | “the putA gene… was deleted… to generate H. elongata HN6” and this strain accumulated Pro while improving salt tolerance (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24; 2024 | Inferred causal edge from engineering design/results; moderate confidence |
| gsmt/sdmt pathway | increases | glycine betaine synthesis under salt stress | “the gsmt and sdmt genes… and their proteins (GSMT, SDMT) are upregulated at higher Na+… supporting a causal link… to increased betaine synthesis/accumulation under salt stress” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/AEM.00145-24; https://doi.org/10.1128/aem.00145-24; 2024 | Strong mechanistic edge; salinity range differs greatly from target and taxon-specific |
| ABC-type glycine betaine transporters (Opu/ProU families) | mediate_uptake_of | glycine betaine | “N. thermophilus employs the glycine betaine ABC transporters (Opu and ProU families)… to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/AEM.00145-24; https://doi.org/10.1128/aem.00145-24; 2024 | Strong transport edge; high-salt organism, extrapolation to mid1 should be flagged |
| PutP Na+/proline symporter | facilitates_uptake_of | proline | “the Na+/proline symporter PutP ‘facilitates the sodium ion-dependent uptake of proline’” (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/AEM.00145-24; https://doi.org/10.1128/aem.00145-24; 2024 | Strong transport/mechanism edge; high-salt taxon, indirect for mid1 |
| K+ accumulation | contributes_to | osmotic balance / salt adaptation | “simultaneously accumulating compatible solutes and K+” (xing2024thepolyextremophilenatranaerobius pages 10-14, xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/AEM.00145-24; https://doi.org/10.1128/aem.00145-24; 2024 | General osmoadaptation edge; strong but from extreme/polyextreme context |
| cysB upregulation | positively_regulates | sulfur metabolism and cysteine biosynthesis | “transcription factor cys B was significantly upregulated, positively regulating the sulfur metabolism and cysteine biosynthesis” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Mechanistic regulatory edge; oxidative-stress submodule under salt shock |
| peroxidase gene HELO_RS18165 upregulation | contributes_to | antioxidant defense after NaCl shock | “the upregulation of the crucial peroxidase gene (HELO_RS18165)… collectively constitute the antioxidant defense” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Strong mechanistic edge; oxidative-stress response rather than direct osmolyte production |
| increased POD and CAT activities | mitigate | salt-induced oxidative stress | “the simultaneous enhancement of peroxidase (POD) and catalase (CAT) activities collectively constitute the antioxidant defense” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Good process-level edge; assay-specific to shock experiment |
| inhibition of respiratory chain and ATP synthase | causes | stagnation of growth and ectoine biosynthesis beyond tolerance | “the sustained compromised energy status, resulting from the pronounced inhibition of the respiratory chain and ATP synthase, may be a crucial factor leading to the stagnation of both cell growth and ectoine biosynthesis” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5; https://doi.org/10.1186/s12934-024-02358-5; 2024 | Negative causal edge; useful for upper-bound failure state rather than mid1 support |
| compatible solute strategy | characterizes | halotolerant and moderate halophiles | “halotolerant and moderate halophiles… rely on excluding ions and producing compatible solutes such as glycine betaine” (lee2018naclsaturatedbrinesare pages 15-17) | 10.1093/FEMSRE/FUY026; https://doi.org/10.1093/femsre/fuy026; 2018 | Secondary/background edge; not one of the requested core sources but useful mechanistic generalization |
| H. elongata wild type | grows_across | broad salinity range including 1–3% NaCl | “H. elongata OUT30018 grows across a wide salinity range (0.3%–21% NaCl)” (khanh2024metabolicpathwayengineering pages 1-2) | 10.1128/AEM.01195-24; https://doi.org/10.1128/aem.01195-24; 2024 | Organism-level support that target range lies within known growth window; not itself a mechanism |


*Table: This table lists candidate causal edges for the NaCl range mid1 trait, combining direct trait-definition boundaries with mechanistic osmoadaptation edges supported by recent and authoritative literature. It is formatted for curation use, with quotes, DOI-first references, and flags for taxon specificity or uncertainty.*

---

## Warnings / claims not ready for TraitMech curation (or should be marked “uncertain”)

1. **Salinity-regime mismatch.** Some mechanistic evidence (e.g., *Natranaerobius thermophilus* and parts of the “salt-in” literature) is derived from **very high salinities (molar Na+ / multiple molar NaCl)**. These are mechanistically informative (transporters/solute pathways) but should be flagged as **uncertain extrapolation** to 1–3% NaCl unless corroborated in slight-halophile range experiments. (xing2024thepolyextremophilenatranaerobius pages 14-17)

2. **Assay dependence.** The same organism can appear halophilic vs halotolerant depending on medium and temperature; compatible solute supplementation can change minimum NaCl requirements (e.g., 0.3 M with glucose/glycerol). Curate assay modifiers explicitly (medium composition; supplementation) if edges are sensitive to conditions. (ventosa1998biologyofmoderately pages 12-13, ventosa1998biologyofmoderately pages 2-3)

3. **Food fermentation link is under-supported here.** While halotolerant LAB and fermented-food ecosystems are a major real-world domain, the retrieved evidence set did not yield strong, direct mechanistic quotes for 1–3% NaCl growth classification in LAB specifically; avoid curating LAB-specific nodes/edges without additional primary sources.

---

## DOI-first bibliography (with URLs and publication dates)

1. Ventosa A, Nieto JJ, Oren A. **Biology of moderately halophilic aerobic bacteria.** *Microbiology and Molecular Biology Reviews* (June 1998). DOI: **10.1128/MMBR.62.2.504-544.1998**. https://doi.org/10.1128/mmbr.62.2.504-544.1998 (ventosa1998biologyofmoderately pages 2-3, ventosa1998biologyofmoderately pages 12-13, ventosa1998biologyofmoderately pages 33-33)

2. Ventosa A, Mellado E, Sanchez-Porro C. **Microbiology of extreme soils.** (Book chapter; January 2008). DOI: **10.1007/978-3-540-74231-9**. https://doi.org/10.1007/978-3-540-74231-9 (sessitsch2008microbiologyofextreme pages 100-102)

3. Lee CJD, McMullan PE, O’Kane CJ, et al. **NaCl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats.** *FEMS Microbiology Reviews* (June 2018). DOI: **10.1093/femsre/fuy026**. https://doi.org/10.1093/femsre/fuy026 (lee2018naclsaturatedbrinesare pages 15-17)

4. Yu J, Zhang Y, Liu H, et al. **Temporal dynamics of stress response in Halomonas elongata to NaCl shock: physiological, metabolomic, and transcriptomic insights.** *Microbial Cell Factories* (March 2024). DOI: **10.1186/s12934-024-02358-5**. https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5)

5. Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H. **Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance… Halomonas elongata.** *Applied and Environmental Microbiology* (January 2024). DOI: **10.1128/aem.01905-23**. https://doi.org/10.1128/aem.01905-23 (zou2024metabolicengineeringof pages 1-2)

6. Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. **Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance… Halomonas elongata.** *Applied and Environmental Microbiology* (September 2024). DOI: **10.1128/aem.01195-24**. https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)

7. Xing Q, Zhang S, Tao X, et al. **The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy…** *Applied and Environmental Microbiology* (May 2024). DOI: **10.1128/aem.00145-24**. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19)

8. Amoozegar MA, Safarpour A, Noghabi KA, et al. **Halophiles and their vast potential in biofuel production.** *Frontiers in Microbiology* (August 2019). DOI: **10.3389/fmicb.2019.01895**. https://doi.org/10.3389/fmicb.2019.01895 (amoozegar2019halophilesandtheir pages 1-2)


References

1. (sessitsch2008microbiologyofextreme pages 100-102): A Ventosa, E Mellado, and C Sanchez-Porro. Microbiology of extreme soils. ArXiv, Jan 2008. URL: https://doi.org/10.1007/978-3-540-74231-9, doi:10.1007/978-3-540-74231-9. This article has 124 citations.

2. (ventosa1998biologyofmoderately pages 2-3): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 1999 citations and is from a domain leading peer-reviewed journal.

3. (ventosa1998biologyofmoderately pages 12-13): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 1999 citations and is from a domain leading peer-reviewed journal.

4. (lee2018naclsaturatedbrinesare pages 15-17): Callum J D Lee, Phillip E McMullan, Callum J O’Kane, Andrew Stevenson, Inês C Santos, Chayan Roy, Wriddhiman Ghosh, Rocco L Mancinelli, Melanie R Mormile, Geoffrey McMullan, Horia L Banciu, Mario A Fares, Kathleen C Benison, Aharon Oren, Mike L Dyall-Smith, and John E Hallsworth. Nacl-saturated brines are thermodynamically moderate, rather than extreme, microbial habitats. FEMS microbiology reviews, 42 5:672-693, Jun 2018. URL: https://doi.org/10.1093/femsre/fuy026, doi:10.1093/femsre/fuy026. This article has 90 citations and is from a domain leading peer-reviewed journal.

5. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

6. (zou2024metabolicengineeringof pages 1-2): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 17 citations and is from a peer-reviewed journal.

7. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

8. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

9. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

10. (yu2024temporaldynamicsof pages 2-5): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

11. (ventosa1998biologyofmoderately pages 33-33): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 1999 citations and is from a domain leading peer-reviewed journal.

12. (yu2024temporaldynamicsof pages 18-18): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

13. (xing2024thepolyextremophilenatranaerobius pages 4-6): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

14. (reang2024extremozymesandcompatible pages 16-17): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 16 citations and is from a peer-reviewed journal.

15. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

16. (athauda2025ectoinefromhalophilic pages 2-3): Uthpala S. Athauda and I.V.N Rathnayake. Ectoine from halophilic bacteria: biosynthesis, diversity, and industrial applications. Nepal Journal of Biotechnology, 13(2):126-137, Dec 2025. URL: https://doi.org/10.54796/njb.v13i2.444, doi:10.54796/njb.v13i2.444. This article has 0 citations.

17. (amoozegar2019halophilesandtheir pages 1-2): Mohammad Ali Amoozegar, Atefeh Safarpour, Kambiz Akbari Noghabi, Tala Bakhtiary, and Antonio Ventosa. Halophiles and their vast potential in biofuel production. Frontiers in Microbiology, Aug 2019. URL: https://doi.org/10.3389/fmicb.2019.01895, doi:10.3389/fmicb.2019.01895. This article has 163 citations and is from a peer-reviewed journal.