---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:25:38.430041'
end_time: '2026-08-04T02:34:09.590145'
duration_seconds: 511.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta mid3
  trait_identifier: METPO:1000477
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 4\u20135 pH units, characteristic of organisms with wide pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_4_5
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)'
  causal_graph_summary: 'ph_delta_mid3_wide_breadth: 15 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000477
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 4–5 pH units, characteristic of organisms with wide pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_4_5
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)
- **Existing causal graph summary:** ph_delta_mid3_wide_breadth: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid3.yaml`.

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
- **Trait label:** pH delta mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000477
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 4–5 pH units, characteristic of organisms with wide pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_4_5
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports wide pH-homeostasis flexibility as the basis of euryphilic pH-tolerance.)
- **Existing causal graph summary:** ph_delta_mid3_wide_breadth: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid3.yaml`.

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


# Curation-focused research report: pH delta mid3

**Target trait:** **pH delta mid3**  
**Trait identifier:** **METPO:1000477**  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Supplied synonym:** `pHd_4_5`  
**Parent:** METPO:1000232

## Executive conclusion

METPO:1000477 should be interpreted as an **assay-observed growth breadth**, namely an organism’s upper growth-supporting external-pH boundary minus its lower boundary being approximately **4–5 pH units**. It is not the optimum pH, environmental pH preference, cytoplasmic-pH range, or survival after a short lethal-pH challenge.

The strongest mechanistic interpretation is that wide breadth emerges from coordinated **cytoplasmic pH homeostasis**, combining acid-side proton exclusion/consumption and damage control with alkaline-side proton acquisition. The literature strongly supports the individual modules, but the sources reviewed do **not** establish that any one module causes the specific 4–5-unit phenotype. Accordingly, most direct module → METPO:1000477 edges should remain hypotheses until paired growth-range and perturbation data are available.

## 1. Trait scope and boundaries

### Positive operational definition

For curation, require growth measurements at multiple buffered external pH values under otherwise comparable conditions. Define:

`pH breadth = highest pH supporting growth − lowest pH supporting growth`.

A breadth near 4–5 units qualifies, subject to the project’s numerical inclusion tolerance. “Growth supporting” should ideally be based on reproducible increases in biomass, viable counts, or growth rate—not mere post-exposure viability.

Bacteria can tolerate external pH values outside the narrower cytoplasmic range required for growth because pH sensing and homeostatic mechanisms decouple external from intracellular pH. Extreme acidophiles, for example, can grow below external pH 3 while maintaining cytoplasm near pH 6; alkaliphilic bacilli growing optimally around external pH 7.5–10.5 maintain cytoplasm around pH 7.5–8.3. These are demonstrations of homeostatic decoupling, not by themselves evidence for METPO:1000477. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 12-14)

### Boundary cases to exclude or annotate separately

1. **Optimum or preferred pH:** a single pH coordinate has no breadth information.
2. **Realized environmental niche:** field abundance reflects pH plus competition, dispersal, nutrients, and other covariates. Ramoneda et al. explicitly define preference as the pH of maximal relative abundance in nature, not a fundamental growth niche. (ramoneda2023buildingagenomebased pages 1-2)
3. **Acid resistance or alkaline resistance alone:** survival at pH 2 or pH 11 for one hour is not sustained growth across a 4–5-unit interval.
4. **Acid adaptation:** preconditioning can increase subsequent survival without widening the growth interval.
5. **Intracellular-pH span:** the trait concerns external assay pH, not variation in pHᵢ.
6. **Unbuffered cultures:** metabolism can shift medium pH, making nominal starting pH unreliable.
7. **Sparse pH testing:** endpoints inferred from intervals of 1–2 pH units should be marked approximate or censored.
8. **Conditional breadth:** medium composition, carbon source, sodium/potassium, oxygen, temperature, inoculum history, and buffering system should be retained as assay context.

## 2. Candidate nodes grouped by type

### Trait, environment, and assay nodes

- **pH delta mid3 — METPO:1000477**
- External pH; lower growth-supporting pH boundary; upper growth-supporting pH boundary — label-only
- Buffered pH-gradient growth assay — label-only
- Cytoplasmic pH regulation — **GO:0006885**
- Cellular response to pH — **GO:0043462**
- Cytoplasmic pH / proton-motive force / membrane potential — retain label-only unless the local ontology policy supplies reviewed terms

### Transport and bioenergetic modules

- Proton-transporting two-sector ATPase complex — **GO:0042777**
- Proton transmembrane transporter activity — **GO:0015078**
- Sodium:proton antiporter activity — **GO:0015385**
- NhaA Na⁺/H⁺ antiporter — label-only until organism and gene product are specified
- MrpABCDEFG multisubunit Na⁺/H⁺ antiporter — label-only
- K⁺/H⁺ antiporter — label-only
- UreI urea channel — taxon-specific, label-only
- Glutamate/GABA antiporter — label-only

### Enzymes, pathways, and regulatory systems

- Glutamate-dependent acid-resistance pathway; GadB glutamate decarboxylase; GadEWX regulon — label-only pending taxon-specific grounding
- Urease and urea-hydrolysis module — label-only at complex level
- Cyclopropane fatty-acid synthesis / Cfa — label-only pending sequence-specific curation
- Membrane-lipid and porin remodeling — label-only
- Clp protease complex; molecular chaperones; macromolecule repair — label-only or **GO:0006457** for protein folding
- Two-component response regulator activity — **GO:0016986**
- HP0165/HP0166 (ArsRS), PhoP/PhoQ, and other pH-responsive systems — taxon-specific label-only nodes

### Chemicals and ions

- Hydron/proton — **CHEBI:15378**
- Sodium(1+) — **CHEBI:29101**
- Potassium(1+) — **CHEBI:29103**
- Urea — **CHEBI:16199**
- Ammonia — **CHEBI:16134**
- L-glutamate — **CHEBI:29985**
- 4-aminobutanoic acid/GABA — **CHEBI:16865**
- Putrescine — **CHEBI:17148**
- ATP, ADP, carbon dioxide, cyclopropane fatty acids — use reviewed ChEBI records after identifier verification during YAML implementation

### Cellular localizations and processes

- Cytoplasm, cytoplasmic membrane, periplasm, extracellular medium
- Transmembrane proton transport, cation homeostasis, membrane permeability, protein folding/repair
- For *Helicobacter pylori*, explicitly distinguish periplasmic buffering from cytoplasmic pH regulation; urease recruitment to the membrane at pH 4.5 was reported to double activity relative to neutral pH. (krulwich2011molecularaspectsof pages 11-12)

## 3. Candidate causal edges

“Curate” below means that the mechanistic edge is sufficiently supported in its stated taxon/context. It does **not** mean that a direct edge to METPO:1000477 is established.

| # | Proposed subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | Cytoplasmic pH regulation → **enables growth across** → external-pH values outside the cytoplasmic growth range | 10.1038/nrmicro2549 | “mechanisms for pH sensing and cytoplasmic pH homeostasis enable most bacteria to tolerate or grow at external pH values…outside the cytoplasmic pH range” | **Strong general mechanism.** Use as the central intermediate node; direct connection to the exact 4–5-unit class remains inferred. (krulwich2011molecularaspectsof pages 5-6)
| 2 | Acidic external pH → **increases** → proton-consuming glutamate decarboxylase activity/expression | 10.1038/nrmicro2549 | Acid conditions increase “proton-consuming enzymes like glutamate decarboxylase (GadB)” | **Review-supported; *E. coli*-weighted.** Curate only with taxon/context. (krulwich2011molecularaspectsof pages 5-6)
| 3 | Glutamate decarboxylation → **consumes** → cytoplasmic H⁺ | 10.1038/nrmicro2549; 10.1007/s11274-019-2770-2 | GadB converts glutamate to GABA; decarboxylase systems “consume cytoplasmic protons” | **Mechanistically strong.** Acid-side contribution only; not evidence of broad bidirectional growth. (krulwich2011molecularaspectsof pages 5-6, guo2019recentadvancesof pages 3-4)
| 4 | Glutamate/GABA antiport → **replenishes substrate and exports product for** → glutamate-dependent acid resistance | 10.1038/nrmicro2549 | A “coupled antiporter system…regenerates substrate” | **Strong pathway edge**, but system composition is taxon-specific. (krulwich2011molecularaspectsof pages 5-6)
| 5 | F₁F₀-ATPase operating in ATP-hydrolysis mode → **exports** → H⁺ | 10.1007/s11274-019-2770-2 | “F1F0-ATPase-mediated direct proton extrusion using ATP hydrolysis energy” | **Supported general acid-homeostasis mechanism.** Direction depends on physiological state and organism. (guo2019recentadvancesof pages 3-4)
| 6 | F₁F₀-ATP synthase during alkaline growth → **imports/captures** → H⁺ | 10.1038/nrmicro2549 | Alkaline conditions increase ATP synthase “to capture protons inward”; alkaliphile ATP synthase contributes via proton uptake | **Strong but context-dependent.** Do not encode ATPase with one invariant direction across all pH conditions. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14)
| 7 | Na⁺/H⁺ antiporter activity → **promotes** → alkaline cytoplasmic-pH homeostasis | 10.1016/S0021-9258(18)34835-X | An antiporter-impaired *E. coli* mutant failed to grow at nonpermissive alkaline pH until pH homeostasis was restored | **Direct functional evidence.** Recovery of pHᵢ preceded growth; strong edge for alkaline growth, not exact breadth. (zilberstein1982thesodiumprotonantiporter pages 5-5)
| 8 | NhaA Na⁺/H⁺ antiporter → **imports 2 H⁺ per exported** → Na⁺ | 10.1038/nrmicro2549 | *E. coli* NhaA is described with “2H+/1Na+ stoichiometry” | **Strong molecular edge**, explicitly organism/system-specific. (krulwich2011molecularaspectsof pages 5-6)
| 9 | Mrp Na⁺/H⁺ antiporter → **promotes** → alkaliphilic growth/pH homeostasis | 10.1038/nrmicro2549 | “mrpA mutations cause loss of alkaliphilic phenotype and antiport activity” | **Direct mutant-supported**, especially alkaliphilic *Bacillus*. Do not generalize Mrp necessity to all wide-breadth microbes. (krulwich2011molecularaspectsof pages 12-14)
| 10 | Urease → **catalyzes** → urea hydrolysis producing ammonia | 10.1038/nrmicro2549; 10.1007/s11274-019-2770-2 | Urease hydrolysis generates ammonia that “neutralize[s] protons” | **Strong chemistry; taxon and substrate dependent.** (krulwich2011molecularaspectsof pages 11-12, guo2019recentadvancesof pages 3-4)
| 11 | Ammonia production → **buffers/raises** → local cellular pH | 10.1038/nrmicro2549 | *H. pylori* maintains periplasmic buffering through urease-catalyzed urea hydrolysis | **Strong in urease-positive organisms**, particularly *H. pylori*; do not assume cytoplasmic localization. (krulwich2011molecularaspectsof pages 11-12)
| 12 | HP0165/HP0166 pH-sensing system → **regulates** → urease acid-acclimation genes | 10.1038/nrmicro2549 | HP0165/HP0166 controls acid-acclimation genes “including urease genes” | **Taxon-specific regulatory edge** for *H. pylori*. (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 20-22)
| 13 | Acidic external pH → **induces** → membrane-lipid/porin remodeling | 10.1038/nrmicro2549 | Acid response includes “membrane lipid and porin remodeling” | **Moderate/generalized.** Preserve the cited organism and assay when available. (krulwich2011molecularaspectsof pages 5-6)
| 14 | Cyclopropane fatty-acid incorporation → **decreases** → membrane proton permeability | 10.1038/nrmicro2549; 10.1007/s11274-019-2770-2 | Cyclopropane fatty acids “reduce membrane proton permeability” | **Mechanistically plausible and review-supported**, mainly acid-side; direct breadth edge is unsupported. (krulwich2011molecularaspectsof pages 17-18, guo2019recentadvancesof pages 3-4)
| 15 | Acid stress → **damages** → cellular proteins/macromolecules | 10.1007/s11274-019-2770-2 | Acid-homeostasis review describes removal of “acid-damaged proteins” | **General stress edge.** Not specific enough to connect directly to the target trait. (guo2019recentadvancesof pages 3-4)
| 16 | Clp protease complex → **removes** → acid-damaged proteins | 10.1007/s11274-019-2770-2 | “Clp protease complex removal of acid-damaged proteins” | **Review-supported, acid-side, nonspecific.** (guo2019recentadvancesof pages 3-4)
| 17 | Exogenous putrescine under acidic conditions → **enhances** → glutamate-based acid resistance/GABA metabolism | 10.1128/AEM.00569-24 | Putrescine “consumed intracellular H+ by enhancing the glutamate-based acid resistance strategy” | **2024 community/biofilm evidence; conditional.** Not a constitutive organismal trait mechanism. (jiang2024exogenousputrescineplays pages 12-14)
| 18 | Exogenous putrescine under alkaline conditions → **exacerbates** → alkaline stress/inhibits biofilm growth | 10.1128/AEM.00569-24 | Putrescine promoted acidic biofilm responses but “restricted biofilm growth” under alkaline conditions | **Important sign reversal.** Do not curate putrescine as a general positive regulator of pH breadth. (jiang2024exogenousputrescineplays pages 12-14)
| 19 | Presence of a 56-gene genomic feature set → **predicts** → realized bacterial pH preference | 10.1126/sciadv.adf8998 | A model using 56 gene types achieved R² 0.80 and MAE 0.63 pH units | **Association/prediction only.** Object is realized preference, not METPO:1000477. (ramoneda2023buildingagenomebased pages 6-7)
| 20 | Coordinated acid-side and alkaline-side homeostasis modules → **may increase** → METPO:1000477 | Multiple | Individual modules support pH homeostasis on opposite sides of neutrality | **Uncertain integrative hypothesis. Do not curate as established** without matched breadth assays and perturbations. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, guo2019recentadvancesof pages 3-4)

The core curation decisions are summarized below.

| Candidate module | Representative nodes | Direction/role under acid or alkaline pH | Strongest evidence type | Confidence for mechanism | Safe to connect directly to METPO:1000477? |
|---|---|---|---|---|---|
| Cytoplasmic pH homeostasis | cytoplasmic pH regulation; intracellular pH; external pH range | Core integrative mechanism: cells maintain a narrower internal pH while growing across a wider external pH range; explains breadth conceptually but not a measured 4–5-unit trait by itself (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14) | Authoritative review synthesis with organismal examples | High for general mechanism | **No, not alone** — best as an intermediate parent mechanism, not a direct proof of 4–5-unit breadth |
| F1Fo ATPase | proton-translocating F1Fo-ATP synthase; ATPase complex | Acid side: can expel protons by ATP hydrolysis in many bacteria; alkaline side: can capture scarce protons inward during ATP synthesis, depending on taxon/physiology (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, guo2019recentadvancesof pages 3-4) | Review synthesis with comparative physiology; some taxon-specific functional support | High for pH-homeostasis role | **Usually no** — curatable as contributing to pH homeostasis; not direct proof of METPO:1000477 |
| Na+/H+ and K+/H+ antiporters | NhaA; Mrp complex; K+/H+ antiporter | Especially important under alkaline pH for proton uptake/cation export; direct growth linkage shown in antiporter-defective mutants and alkaliphile studies (krulwich2011molecularaspectsof pages 12-14, zilberstein1982thesodiumprotonantiporter pages 5-5, krulwich2011molecularaspectsof pages 27-28) | Direct mutant/physiology evidence plus review | High for alkaline homeostasis | **Conditionally** — safe to connect to alkaline-side pH homeostasis; **not yet directly** to METPO:1000477 without breadth-specific data |
| Glutamate decarboxylase/GABA antiport | GadB/Gad system; glutamate; GABA; glutamate/GABA antiport | Acid-side mechanism that consumes cytoplasmic protons and exports product via antiport; strong for acid resistance/homeostasis, weak for broad bidirectional growth breadth (krulwich2011molecularaspectsof pages 5-6, guo2019recentadvancesof pages 3-4, jiang2024exogenousputrescineplays pages 12-14) | Regulatory/mechanistic studies and reviews; community-level modulation in 2024 biofilm study | High for acid resistance | **No** — one-sided acid adaptation is not direct evidence of 4–5-unit growth breadth |
| Urease | urease; urea; ammonia; UreI-linked acid acclimation context | Acid-side buffering: urea hydrolysis yields ammonia/CO2 and raises local/internal pH; strong in acid acclimation organisms such as *H. pylori* and in recent acid-stress omics (krulwich2011molecularaspectsof pages 11-12, guo2019recentadvancesof pages 3-4) | Direct mechanistic literature in specific taxa plus review | High for acid acclimation in relevant taxa | **No** — strongly taxon-specific and usually one-sided |
| Membrane lipid remodeling | cyclopropane fatty acids; altered membrane lipids; proton permeability | Primarily acid-side passive protection by reducing proton permeability; may support tolerance range indirectly via envelope remodeling (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 17-18, guo2019recentadvancesof pages 3-4) | Review-supported mechanism with cited experimental precedent | Moderate to high | **No** — supportive but indirect and usually acid-biased |
| Proteostasis / macromolecule repair | Clp protease; chaperones; protein folding/repair | Stress-damage mitigation under low or high pH; improves survival and growth robustness but is not specific to pH breadth (guo2019recentadvancesof pages 3-4) | Review synthesis; some 2024 heterologous overexpression studies in *E. coli* are supportive but broad-stress and not native breadth evidence | Moderate | **No** — too nonspecific for direct linkage |
| pH-responsive regulators | two-component systems; ArsRS; HP0165/HP0166; PhoP/PhoQ; GadEWX | Sense external pH and regulate downstream homeostasis modules; can organize acid acclimation or multistress programs, but typically taxon- and condition-specific (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 17-18) | Direct regulatory studies in specific taxa plus review | Moderate to high | **No** — use as upstream regulators of downstream mechanisms, not direct trait causes |
| Recent genomic pH-preference associations | pH-associated gene sets; ATPases; transporters; phosphatases; antiporters | 2023 association studies identify genes enriched with acidic vs alkaline environmental preference, but they estimate realized niche preference, not experimentally measured growth breadth (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 8-9, ramoneda2023buildingagenomebased pages 2-3) | Cross-dataset comparative genomics / machine learning association | Moderate for association, low for causality | **No** — valuable prioritization layer only; not direct TraitMech evidence for METPO:1000477 |


*Table: This table summarizes which commonly cited pH-response modules are mechanistically credible and which are currently safe to connect to METPO:1000477. It is useful for separating strong pH-homeostasis evidence from weaker or non-breadth-specific evidence, especially recent genomic association studies.*

## 4. Recent developments and quantitative evidence

### Genome-based prediction of bacterial pH preference (2023)

Ramoneda et al. combined **795 soil and 675 freshwater samples**—1,470 samples spanning approximately pH 3–10—with 250,275 ASVs. They inferred preferences for 4,568 ASVs across 38 phyla. (ramoneda2023buildingagenomebased pages 1-2)

The genomic analysis found **332 gene types** associated with pH preference in at least two datasets and **56** consistent across at least three; 30 of the 56 had prior links to pH adaptation. Associated functions included ATPases, antiporters, other ion transporters, and phosphatases. (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 2-3)

A gradient-boosted model based on the 56 genes achieved cross-dataset **R² = 0.80** and **mean absolute error = 0.63 pH units**; independent validation produced **R² = 0.55**. Its supported prediction range was pH 4–9, and 85.4% of pre-existing phenotypic records lay between pH 6 and 8. (ramoneda2023buildingagenomebased pages 6-7)

These results are valuable for prioritizing candidate genes, but not for direct TraitMech edges: the phenotype is realized environmental preference, observational covariates remain, and the authors did not establish that the genes cause growth breadth. Only 669 ASV–genome matches representing 580 unique genomes entered parts of the genomic analysis, and genome coverage was 10.6% in soils and 22.4% in freshwater. (ramoneda2023buildingagenomebased pages 8-9, ramoneda2023buildingagenomebased pages 2-3)

### pH-dependent biofilm manipulation (2024)

In activated-sludge biofilms, exogenous putrescine promoted acid-side adaptation through glutamate/GABA metabolism but inhibited development under alkaline conditions. Acid-associated fungal forward-scatter signals increased by **120%** in the reported analysis. This is a useful real-world demonstration that a proposed intervention can have opposite effects at opposite pH extremes; it argues for condition-qualified graph edges. (jiang2024exogenousputrescineplays pages 12-14)

## 5. Applications and expert interpretation

### Current and emerging applications

- **Industrial organic-acid fermentation:** reducing proton influx, consuming intracellular protons, and improving repair can increase robustness as products acidify the broth. However, engineering acid tolerance does not necessarily widen the alkaline boundary.
- **Food preservation and pathogen control:** urease, decarboxylase systems, membrane remodeling, and acid-adaptation regulators are potential intervention points. Conversely, acid preadaptation may increase cross-protection and complicate sanitation.
- **Fruit-juice spoilage control:** acidophilic, heat-resistant *Alicyclobacillus acidoterrestris* uses amino-acid decarboxylation, urea hydrolysis, energy supply, transport, and membrane responses under pH 3 stress; these are control targets, but the evidence is omics/physiology rather than proof of a 4–5-unit breadth mechanism.
- **Wastewater biofilms:** putrescine can be used to modulate biofilm formation under acidic conditions, but its inhibitory alkaline effect makes deployment pH-specific. (jiang2024exogenousputrescineplays pages 12-14)
- **Microbial inoculant selection and cultivation:** the 2023 genomic model may help shortlist organisms for a desired pH niche, although direct growth-range testing remains necessary. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)
- **Alkaline bioprocessing:** Mrp/Nha-type antiport and alkaliphile-adapted ATP synthases are mechanistic targets for improving alkaline growth, contingent on sodium/potassium availability and membrane energetics. (krulwich2011molecularaspectsof pages 12-14, zilberstein1982thesodiumprotonantiporter pages 5-5)

### Expert analysis

The authoritative pH-homeostasis synthesis treats wide external-pH tolerance as a **systems phenotype**, not the product of a universal “wide-pH gene.” The acid and alkaline ends impose opposite proton-management problems: acid conditions favor proton exclusion, proton consumption, buffering, and repair, whereas alkaline conditions favor proton capture and cation/H⁺ exchange. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14)

Therefore, the best graph architecture is:

`environmental pH challenge → pH sensing/regulation → condition-specific transport/metabolic/envelope modules → cytoplasmic pH homeostasis and damage limitation → growth at that external pH → measured pH breadth → METPO:1000477`.

This avoids the biologically misleading shortcut `gadB → METPO:1000477` or `urease → METPO:1000477`.

## 6. Recommended graph-curation strategy

### Safe now

1. Curate mechanistic subgraphs for acid-side and alkaline-side homeostasis with explicit taxa and conditions.
2. Use **GO:0006885 cytoplasmic pH regulation** as the main convergent process.
3. Represent ATPase direction conditionally.
4. Preserve compartment distinctions, especially for urease-mediated buffering.
5. Attach evidence strength: direct mutant, biochemical, regulatory, omics association, review synthesis, or inference.

### Require before a direct mechanism → METPO:1000477 edge

- Growth curve or reproducible growth endpoint at enough pH values to establish a 4–5-unit interval.
- Isogenic deletion, knockdown, inhibition, complementation, or controlled overexpression.
- Demonstration that perturbation narrows or widens the interval, rather than changing only survival at one pH.
- Reporting of medium, buffer, temperature, oxygen, carbon source, sodium/potassium, and adaptation history.
- Ideally, simultaneous pHᵢ measurement showing that altered breadth tracks altered homeostasis.

## 7. Warnings: claims not ready for TraitMech

1. **Do not curate pH-preference genes from Ramoneda et al. as causes of METPO:1000477.** They are associations with realized niche preference. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5)
2. **Do not equate one-sided acid resistance with wide pH breadth.** Gad, urease, cyclopropane lipids, and putrescine evidence is predominantly acid-side.
3. **Do not make putrescine a universally positive node.** Its effect reverses under alkaline conditions. (jiang2024exogenousputrescineplays pages 12-14)
4. **Do not assign ATPase a single universal transport direction.** Acid-side ATP hydrolysis can extrude protons, whereas alkaline ATP synthesis draws protons inward. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, guo2019recentadvancesof pages 3-4)
5. **Do not generalize *H. pylori* urease regulation or alkaliphilic *Bacillus* Mrp dependence across microbes.** These are strong but taxon-specific mechanisms. (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 12-14)
6. **Do not infer breadth from genome presence alone.** Regulation, ion availability, membrane context, and pathway coupling determine function.
7. **Do not add unverified identifiers.** Keep taxon-specific proteins, complexes, assay states, and ambiguous ontology concepts label-only until reviewed.
8. **No source reviewed directly demonstrated that one perturbation creates or abolishes the specific 4–5-unit growth breadth.** The final integrative trait edge therefore remains uncertain.

## DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology.* Published May 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 12-14)
2. Ramoneda J, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances.* Published April 2023. DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-2)
3. Jiang G, et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology.* Published July 2024. DOI: [10.1128/AEM.00569-24](https://doi.org/10.1128/AEM.00569-24). (jiang2024exogenousputrescineplays pages 12-14)
4. Zilberstein D, Agmon V, Schuldiner S, Padan E. **The sodium/proton antiporter is part of the pH homeostasis mechanism in Escherichia coli.** *Journal of Biological Chemistry.* Published April 1982. DOI: [10.1016/S0021-9258(18)34835-X](https://doi.org/10.1016/S0021-9258(18)34835-X). (zilberstein1982thesodiumprotonantiporter pages 5-5)
5. Guo J, et al. **Recent advances of pH homeostasis mechanisms in Corynebacterium glutamicum.** *World Journal of Microbiology and Biotechnology.* Published November 2019. DOI: [10.1007/s11274-019-2770-2](https://doi.org/10.1007/s11274-019-2770-2). (guo2019recentadvancesof pages 3-4)

**Bottom line for `data/traits/environment/ph_delta_mid3.yaml`:** retain METPO:1000477 as a measured breadth phenotype; build condition-specific acid and alkaline homeostasis subgraphs beneath it; and mark their convergence on the trait as **inferred/uncertain** until direct growth-breadth perturbation evidence is obtained.

References

1. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

4. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

5. (guo2019recentadvancesof pages 3-4): Jing Guo, Zhenping Ma, Jinshan Gao, Jinhua Zhao, Liang Wei, Jun Liu, and Ning Xu. Recent advances of ph homeostasis mechanisms in corynebacterium glutamicum. World Journal of Microbiology and Biotechnology, Nov 2019. URL: https://doi.org/10.1007/s11274-019-2770-2, doi:10.1007/s11274-019-2770-2. This article has 39 citations and is from a peer-reviewed journal.

6. (zilberstein1982thesodiumprotonantiporter pages 5-5): D. Zilberstein, V. Agmon, S. Schuldiner, and E. Padan. The sodium/proton antiporter is part of the ph homeostasis mechanism in escherichia coli. The Journal of biological chemistry, 257 7:3687-91, Apr 1982. URL: https://doi.org/10.1016/s0021-9258(18)34835-x, doi:10.1016/s0021-9258(18)34835-x. This article has 157 citations.

7. (krulwich2011molecularaspectsof pages 20-22): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (krulwich2011molecularaspectsof pages 17-18): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

9. (jiang2024exogenousputrescineplays pages 12-14): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

10. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

11. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

12. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

13. (ramoneda2023buildingagenomebased pages 8-9): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

14. (ramoneda2023buildingagenomebased pages 2-3): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.