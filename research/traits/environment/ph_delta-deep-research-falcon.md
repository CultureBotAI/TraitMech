---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:14:35.666177'
end_time: '2026-08-04T02:24:05.231762'
duration_seconds: 569.57
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta
  trait_identifier: METPO:1000232
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH phenotype with numerical limits expressing the breadth (maximum
    minus minimum) of external pH supporting growth of an organism.
  parent_traits: METPO:1000531, METPO:1000534
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports the breadth of the pH-tolerance span as a derived descriptor reflecting
    overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive
    force (pH-homeostasis review supports the proton motive force as the energetic
    constraint underlying broad versus narrow pH tolerance.)'
  causal_graph_summary: 'ph_delta_homeostasis_flexibility: 12 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000232
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the breadth of the pH-tolerance span as a derived descriptor reflecting overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force as the energetic constraint underlying broad versus narrow pH tolerance.)
- **Existing causal graph summary:** ph_delta_homeostasis_flexibility: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta.yaml`.

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
- **Trait label:** pH delta
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000232
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits expressing the breadth (maximum minus minimum) of external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the breadth of the pH-tolerance span as a derived descriptor reflecting overall pH-homeostasis flexibility.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports the proton motive force as the energetic constraint underlying broad versus narrow pH tolerance.)
- **Existing causal graph summary:** ph_delta_homeostasis_flexibility: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta.yaml`.

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


# Curation-focused research report: microbial **pH delta**

## 1. Scope and recommended interpretation

**Trait:** “pH delta”  
**Identifier:** `METPO:1000232`  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Definition supplied:** the numerical breadth of external pH supporting organismal growth, calculated as:

\[
\mathrm{pH\ delta}=\mathrm{maximum\ growth\ pH}-\mathrm{minimum\ growth\ pH}.
\]

This is an **assay-observed growth-range descriptor**, not a molecular process. Its value depends on medium composition, buffering capacity, temperature, salinity, oxygen, carbon and energy source, inoculum, incubation time, and the operational threshold used to call growth. Consequently, provenance for both endpoints and assay conditions should accompany every curated value.

The most defensible mechanistic interpretation is that a large pH delta reflects the integrated capacity to preserve membrane energetics, intracellular pH, macromolecular function, and nutrient transport across both acidic and alkaline conditions. It should not be treated as synonymous with any single mechanism.

### Boundary cases

* **pH optimum or preference:** a location on the pH axis, not its breadth. A taxon may have an extreme optimum but a narrow range, or a neutral optimum and broad range. The 2023 genome–environment study estimated bacterial pH preferences from 1,470 soil and freshwater samples but did not directly measure culture-based pH delta; preference associations therefore must not be substituted for growth-range evidence. (ramoneda2023buildingagenomebased pages 1-1)
* **Minimum and maximum growth pH:** the two component endpoints. They may be graph inputs to pH delta but are not equivalent to the derived delta.
* **Survival/resistance:** viability after exposure without contemporaneous replication. For example, bacteria can survive gastric acid or alkaline seawater and later resume growth at neutral pH; such observations do not establish growth at the exposure pH. (krulwich2011molecularaspectsof pages 1-3)
* **Intracellular pH or pH homeostasis:** mechanistic intermediate rather than the target phenotype. Neutralophilic bacteria may grow over approximately pH 5.5–9 while maintaining cytoplasmic pH near 7.5–7.7; a 2023 review gives *E. coli* growth at pH 5.5–9.0 with cytoplasmic pH 7.2–7.8. (rebelo2023unravelingtherole pages 18-20, krulwich2011molecularaspectsof pages 1-3)
* **Acid/alkali acclimation:** a state induced by prior exposure. Curate separately unless the pH-range assay explicitly controls acclimation history.
* **Community pH niche breadth:** occurrence or activity across environmental pH is affected by interactions, dispersal, and geochemistry. It is not automatically an isolate-level growth range.

## 2. Current mechanistic model

External pH alters both the proton gradient and membrane potential that together constitute the proton-motive force. Acidic conditions impose proton-influx pressure and threaten cytoplasmic acidification; alkaline conditions reduce proton availability and can impede proton-coupled ATP synthesis and solute uptake. Broad-range organisms therefore require complementary acid-side and alkaline-side modules rather than one universal “pH-delta gene.” (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3)

At low pH, candidate modules include restricted proton permeability, an inside-positive membrane potential in extreme acidophiles, active proton extrusion, proton-consuming reactions, cytoplasmic buffering, and envelope repair. At high pH, electrogenic Na+/H+ or K+/H+ antiporters capture protons using membrane potential, while respiratory chains, ATP synthase, sodium cycling, and cell-surface adaptations preserve bioenergetic function. The authoritative assessment is explicitly integrative: the relevant mechanism changes with oxygen availability, salinity, and taxon. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 11-12)

The strongest conservative edge set is summarized below.

| subject | predicate | object | evidence class/taxon | DOI |
|---|---|---|---|---|
| low external pH | increases | inward proton stress / proton influx pressure | review synthesis; neutralophilic bacteria broadly (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| glutamate decarboxylase GadB | consumes | cytoplasmic protons during glutamate decarboxylation | review-backed mechanism; *Escherichia coli* and other bacteria (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | 10.1038/nrmicro2549 |
| urease + UreI | enables | periplasmic buffering via NH3/CO2 production and transport | direct physiological/regulatory evidence; *Helicobacter pylori* (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 27-28) | 10.1038/nrmicro2549 |
| membrane / envelope adaptations | reduces | proton leakage across the cell boundary | review synthesis; acid-stressed bacteria and extremophiles (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| high external pH | induces | cation/proton antiporters (Na+/H+, K+/H+) | review synthesis; alkaliphile/alkali-stressed bacteria (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 |
| Mrp Na+/H+ antiporter | supports | proton uptake and high-pH growth | direct genetic/physiological evidence summarized in review; alkaliphilic *Bacillus* spp. including *B. pseudofirmus* OF4 (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22, krulwich2011molecularaspectsof pages 22-23) | 10.1038/nrmicro2549 |
| F1Fo ATP synthase | contributes to | pH homeostasis | review synthesis with organism-specific evidence; acidophiles, alkaliphiles, and neutralophiles (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 11-12) | 10.1038/nrmicro2549 |
| broad external pH growth range (pH delta) | inferred to reflect | pH-homeostasis flexibility | inferred terminal trait link; cross-taxon interpretation from pH-homeostasis review and comparative physiology (krulwich2011molecularaspectsof pages 1-3, maksimova2024metabolicandmorphological pages 1-2) | 10.1038/nrmicro2549; 10.1155/2024/3087296 |


*Table: This table summarizes the strongest conservative candidate causal edges for curating microbial pH delta, emphasizing well-supported acid and alkaline homeostasis mechanisms and marking the terminal pH-delta interpretation as inferred.*

## 3. Candidate graph nodes grouped by type

### Trait and assay nodes

* **pH delta:** `METPO:1000232`.
* **Parent traits:** `METPO:1000531`, `METPO:1000534`—retain verbatim, but verify labels and intended direction against the current METPO release.
* Minimum external pH supporting growth—label-only unless a verified METPO term is available.
* Maximum external pH supporting growth—label-only.
* Growth detection threshold, incubation duration, medium buffer capacity, initial pH, final pH, and pH drift—experimental-factor nodes.
* Microbial growth: `GO:0040007`.
* Cellular response to pH: `GO:0071467`.
* Intracellular pH and cytoplasmic pH homeostasis—use labels pending identifier verification.

### Environmental and physicochemical nodes

* Hydrogen ion: `CHEBI:15378`.
* Acidic environment and alkaline environment—label-only unless the intended ENVO classes are verified.
* Proton electrochemical gradient/proton-motive force.
* Transmembrane pH gradient, ΔpH.
* Membrane potential, Δψ.
* Sodium ion: `CHEBI:29101`.
* Potassium ion: `CHEBI:29103`.
* Buffer concentration/capacity, oxygen availability, salinity, temperature, carbon source, organic acids, and weak-acid concentration.

### Transporters and complexes

* F-type H+-transporting ATP synthase/F1Fo ATPase—complex node; `GO:0005753` can ground the molecular function “proton-transporting ATP synthase activity, rotational mechanism.” Direction must be represented separately because ATP synthesis and ATP-driven proton pumping are condition-dependent.
* Mrp multisubunit Na+/H+ antiporter—label-only complex until organism-specific gene products are selected.
* NhaA Na+/H+ antiporter—organism-specific protein node; the *E. coli* transporter has an electrogenic 2H+:1Na+ stoichiometry in the review synthesis. (krulwich2011molecularaspectsof pages 5-6)
* K+/H+ antiporter.
* UreI urea channel and urease complex in *Helicobacter pylori*.
* Respiratory-chain proton pumps and sodium transport/symport systems.
* Porins and ion channels influencing proton permeability.

### Enzymes, genes, and regulatory systems

* Glutamate decarboxylase GadA/GadB; glutamate-dependent acid-resistance system.
* Arginine, lysine, and ornithine decarboxylase acid-resistance systems. A 2023 review identifies GDAR, ADAR, LDAR, and ODAR and emphasizes GDAR as a robust extreme-acid-protection mechanism in *E. coli*, *Shigella*, *Listeria monocytogenes*, and other bacteria. (rebelo2023unravelingtherole pages 18-20)
* Urease structural genes `ureAB`, UreI, and the *H. pylori* HP0165–HP0166 acid-responsive two-component system.
* Hydrogenases that consume protons during H2 production.
* Amino-acid deaminases and organic-acid-producing alkaline-response pathways.
* Yeast transcriptional/regulatory candidates Stb5, Mac1, Rtg1/Rtg3; RTG retrograde signaling and cell-wall-integrity pathways. These remain candidate regulators because the 2024 evidence is principally comparative transcriptomics. (dubinkina2024atranscriptomicatlas pages 1-2)

### Metabolites and chemical products

* Glutamate, γ-aminobutanoate/GABA, arginine, lysine, ornithine.
* Urea, ammonia, ammonium, carbon dioxide, and bicarbonate.
* ATP and ADP.
* Trehalose and polyols.
* Organic acids and their protonated forms; distinguish low external pH from weak-acid toxicity because membrane-permeant undissociated acids have additional effects.

### Cellular structures and processes

* Cytoplasm, periplasm, plasma membrane, cell wall, S-layer/secondary cell-wall polymers.
* Membrane proton permeability.
* Membrane lipid remodeling and porin remodeling.
* Protein-surface charge/pI adaptation.
* Cytoplasmic buffering by amino acids, proteins, polyamines, and polyphosphate.
* Cell-wall integrity, translation, energy metabolism, glycolysis, and trehalose biosynthesis.

## 4. Candidate evidence-backed causal edges

The snippets below are short source-faithful extracts or close excerpted formulations returned from full-text evidence. Predicates should be mapped to the project’s controlled relation vocabulary before YAML insertion.

| Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---|---|---|---|---|
| Low external pH | increases | inward proton stress | DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549), May 2011: acid challenge requires mechanisms that “minimize proton leakage” and consume or expel cytoplasmic protons. (krulwich2011molecularaspectsof pages 5-6) | Strong general physicochemical edge, but avoid claiming measured growth-range expansion directly. |
| Proton-motive force | constrains | growth across external-pH extremes | Same review: PMF comprises ΔpH and Δψ and is central to growth outside the maintained cytoplasmic range. (krulwich2011molecularaspectsof pages 1-3) | Strong conceptual edge; represents the supplied 2007 PMF evidence conservatively. |
| Inside-positive membrane potential | opposes | proton influx in extreme acidophiles | DOI: 10.1038/nrmicro2549: acidophiles maintain an inside-alkaline gradient supported by “an inside-positive membrane potential (reversed Δψ).” (krulwich2011molecularaspectsof pages 11-12) | Strong review-supported mechanism; taxon-specific to extreme acidophiles. Do not universalize. |
| Membrane-lipid/porin remodeling | reduces | proton leakage | DOI: 10.1038/nrmicro2549: “strategic membrane lipid and porin composition changes” minimize proton leakage during acid stress. (krulwich2011molecularaspectsof pages 5-6) | Moderate; mechanism class rather than one universal lipid or gene. |
| GadB glutamate decarboxylase | consumes | cytoplasmic H+ | DOI: 10.1038/nrmicro2549: GadB “consume[s] cytoplasmic protons during decarboxylation to GABA.” (krulwich2011molecularaspectsof pages 5-6) | Strong biochemical mechanism; growth-range effect is likely taxon/medium dependent and requires glutamate. |
| Amino-acid-dependent acid-resistance systems | support | extreme-acid survival | DOI: [10.3390/antibiotics12091474](https://doi.org/10.3390/antibiotics12091474), September 2023: GDAR, ADAR, LDAR, and ODAR operate at approximately pH 2.5–3.0. (rebelo2023unravelingtherole pages 18-20) | Curate initially to acid resistance/survival, not pH delta, unless growth endpoints were measured. |
| Urease | produces | NH3 and CO2 | DOI: 10.1038/nrmicro2549: urease-based buffering occurs through “CO2, NH3, and NH4+ production.” (krulwich2011molecularaspectsof pages 11-12) | Strong, *H. pylori*-specific biochemical edge. |
| Urease products plus UreI | buffer | *H. pylori* periplasm | DOI: 10.1038/nrmicro2549: NH3/NH4+ transport and urease recruitment buffer the periplasm; urease activity rose approximately twofold at pH 4.5 versus 7.4. (krulwich2011molecularaspectsof pages 11-12) | Strong physiological edge. Link to gastric growth/acclimation, not universal pH delta. |
| Low pH sensed by HP0165–HP0166 | activates | `ureAB` expression | DOI: 10.1038/nrmicro2549: phosphorylated HP0166 binds the ureA promoter at low pH, increasing urease expression/activity. (krulwich2011molecularaspectsof pages 27-28) | Strong taxon-specific regulatory edge. |
| High external pH | induces | Na+/H+ and K+/H+ antiporters | DOI: 10.1038/nrmicro2549: bacteria “up-regulate cation/proton antiporters” during alkaline stress. (krulwich2011molecularaspectsof pages 5-6) | Strong response edge; induction is not by itself proof of necessity. |
| Mrp Na+/H+ antiporter | imports | H+ in exchange for Na+ | DOI: 10.1038/nrmicro2549: Mrp mediates “active proton uptake” in alkaliphilic *B. pseudofirmus* OF4. (krulwich2011molecularaspectsof pages 27-28) | Strong mechanistic edge. |
| Mrp complex | supports | high-pH growth/homeostasis | DOI: 10.1038/nrmicro2549: deletion and point-mutant studies impair antiporter activity and high-pH growth. (krulwich2011molecularaspectsof pages 20-22, krulwich2011molecularaspectsof pages 22-23) | Among the best graph-ready genetic edges; taxon-specific. |
| F1Fo ATP synthase | contributes to | cytoplasmic pH homeostasis | DOI: 10.1038/nrmicro2549: alkaliphile-adapted ATP synthase supports proton uptake; direction and coupling ion differ among taxa and conditions. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 5-6) | Curate with direction/organism qualifiers. Do not encode “always exports protons.” |
| Maintenance of ΔpH | supports | resistance across acidic and alkaline pH | DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296), January 2024: broad-resistant *Bacillus aequororis* 5-DB maintained ΔpH, metabolic activity, and limited damage better than *B. subtilis* ATCC 6633. (maksimova2024metabolicandmorphological pages 1-2) | Recent comparative physiological evidence; causal perturbation of a specific gene was not reported. Mark “supports/associated with,” not “causes.” |
| Broad homeostatic flexibility | enables | larger pH delta | DOI: 10.1038/nrmicro2549 and 10.1155/2024/3087296: broad external growth/resistance accompanies maintenance of intracellular conditions across changing pH. (maksimova2024metabolicandmorphological pages 1-2, krulwich2011molecularaspectsof pages 1-3) | **Inferred terminal edge.** Appropriate as graph synthesis only if explicitly flagged inferred. |
| Stb5/Mac1/Rtg1–Rtg3-associated responses | associated with | low-pH tolerance in *Issatchenkia orientalis* | DOI: [10.1128/spectrum.02536-23](https://doi.org/10.1128/spectrum.02536-23), January 2024: 12 strains—six tolerant and six susceptible—showed divergent transcriptional responses; energy metabolism, translation, cell-wall integrity, RTG signaling, glycolysis, and trehalose biosynthesis were implicated. (dubinkina2024atranscriptomicatlas pages 1-2) | **Uncertain candidate edges.** Authors state that experimental perturbation/engineering validation is needed. |

## 5. Recent developments and quantitative evidence

### Genome- and environment-based inference

Ramoneda et al. combined five datasets totaling **1,470 soil and freshwater samples**. Taxonomy and phylogeny were generally poor predictors of bacterial pH preference, whereas reproducible gene associations enabled a genome-based machine-learning predictor. This is valuable for inoculant selection, cultivation design, and species-distribution modeling, but it predicts preference rather than culture-measured pH delta and supplies associations rather than a causal gene set. DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998), April 2023. (ramoneda2023buildingagenomebased pages 1-1)

### Comparative physiology of broad resistance

The 2024 comparison of alkaliphilic *B. aequororis* 5-DB with weakly alkali-resistant *B. subtilis* ATCC 6633 used resazurin reduction, ATP bioluminescence, atomic-force microscopy, phase-contrast microscopy, and carboxyfluorescein-based intracellular-pH measurement. The broader-resistant strain maintained metabolic activity and ΔpH and avoided major cell damage more effectively, including under low-pH challenge. This supports a multicomponent homeostasis-flexibility model rather than a single-gene explanation. DOI: 10.1155/2024/3087296, January 2024. (maksimova2024metabolicandmorphological pages 1-2)

### Strain-resolved transcriptomics

The *I. orientalis* study profiled **12 strains** split evenly between tolerant and susceptible phenotypes. Hundreds of response genes and several regulators differed, but the authors expressly characterize the targets as requiring perturbational validation. This is a useful discovery layer for future causal tests, not yet a basis for deterministic YAML edges to pH delta. DOI: 10.1128/spectrum.02536-23, January 2024. (dubinkina2024atranscriptomicatlas pages 1-2)

### Reference quantitative examples

* Neutralophilic bacterial growth is commonly approximately pH **5.5–9.0**, while cytoplasmic pH remains much narrower; *E. coli* was summarized as maintaining pH **7.2–7.8**. (rebelo2023unravelingtherole pages 18-20, krulwich2011molecularaspectsof pages 1-3)
* *B. pseudofirmus* OF4 maintains near-complete cytoplasmic homeostasis from external pH **7.5–9.5**, grows optimally around external pH **10.5** with cytoplasmic pH about **8.3**, and grows slowly at external pH ≥**11**, where cytoplasmic pH can reach ≥**9.5**. (krulwich2011molecularaspectsof pages 12-14)
* The review identifies extremophiles inhabiting environments below pH **3** or above pH **11**. These environmental limits do not automatically equal verified isolate growth endpoints. (krulwich2011molecularaspectsof pages 1-3)

## 6. Applications and real-world relevance

* **Industrial organic-acid fermentation:** acid-tolerant *I. orientalis* is a candidate chassis for organic acids and other bioproducts; low-pH operation can reduce bacterial contamination and downstream neutralization requirements. Mechanistic engineering targets remain provisional. (dubinkina2024atranscriptomicatlas pages 1-2)
* **Cultivation and inoculant design:** genome-based pH-preference models may prioritize organisms for culture media, environmental inoculants, and distribution models, but should be validated with pH-range growth curves. (ramoneda2023buildingagenomebased pages 1-1)
* **Pathogen control:** disrupting urease/UreI acid acclimation in *H. pylori*, amino-acid decarboxylation in enteric organisms, or conserved bioenergetic homeostasis could sensitize organisms to host or food-chain acidity. (krulwich2011molecularaspectsof pages 11-12, rebelo2023unravelingtherole pages 18-20)
* **Extremophile biotechnology:** broad pH and salinity resistance can improve process robustness where feedstocks or waste streams fluctuate; the 2024 *Bacillus* comparison explicitly identifies this as a biotechnologically useful property. (maksimova2024metabolicandmorphological pages 1-2)
* **Environmental prediction:** pH is a major structuring variable for bacterial communities, so pH-range phenotypes can support biogeochemical and climate-response models. Preference, realized niche breadth, and fundamental growth breadth must nevertheless remain separate data fields. (ramoneda2023buildingagenomebased pages 1-1)

## 7. Recommended initial TraitMech graph architecture

A conservative graph should have two condition-specific branches converging on the trait:

1. **Acid branch:** low external pH → increased proton stress → membrane/envelope restriction plus proton extrusion/consumption and buffering → maintained cytoplasmic pH and macromolecular function → growth at lower pH endpoint.
2. **Alkaline branch:** high external pH → proton scarcity/large outward ΔpH → electrogenic cation/H+ antiport plus respiratory/ATP-synthase and sodium-cycle support → proton uptake and maintained energetics → growth at higher pH endpoint.
3. **Derived trait:** lower growth-pH endpoint plus upper growth-pH endpoint → larger `METPO:1000232`.

The terminal construction should preferably be arithmetic—`pH_max minus pH_min`—rather than a direct molecular edge. Mechanisms should connect first to endpoint growth or homeostasis phenotypes. A generic “pH-homeostasis flexibility → pH delta” edge may be retained only as explicitly inferred.

## 8. Claims that should not yet be curated

1. **Do not convert survival limits into growth limits.** Acid-resistance systems frequently demonstrate survival at pH 2.5–3.0, not replication there. (rebelo2023unravelingtherole pages 18-20, krulwich2011molecularaspectsof pages 1-3)
2. **Do not infer pH delta from pH optimum, environmental occurrence, or machine-learning preference alone.** The 1,470-sample study addresses preference. (ramoneda2023buildingagenomebased pages 1-1)
3. **Do not encode transcriptomic association as causation.** Stb5, Mac1, Rtg1/Rtg3, glycolysis, trehalose biosynthesis, translation, and cell-wall integrity are promising *I. orientalis* candidates but need knockout, overexpression, rescue, or allele-swap tests. (dubinkina2024atranscriptomicatlas pages 1-2)
4. **Do not universalize taxon-specific mechanisms.** Urease/UreI is especially relevant to *H. pylori*; Mrp evidence is strongest in alkaliphilic *Bacillus*; amino-acid decarboxylase systems depend on substrate availability and species.
5. **Do not assign one fixed direction to F1Fo ATPase.** It may synthesize ATP during proton influx or hydrolyze ATP to pump protons, depending on organism and energetic state. (krulwich2011molecularaspectsof pages 5-6)
6. **Do not curate membrane lipids, osmolytes, protein pI, or S-layer features as direct causes of broad pH delta without perturbation.** Existing evidence is mechanistically plausible but often comparative or review-level. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 27-28)
7. **Do not collapse weak-organic-acid toxicity into H+ stress.** Undissociated acids cross membranes and impose anion and metabolic stress in addition to lowering pH.
8. **Do not report a pH delta without assay metadata.** Initial versus maintained pH, buffer concentration, pH drift, growth threshold, duration, oxygen, salinity, temperature, and medium should be mandatory qualifiers.

## 9. DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology.* Published May 2011. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational authoritative review. (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 12-14)
2. Ramoneda J, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances.* Published April 2023. DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 1-1)
3. Rebelo A, Almeida A, Peixe L, Antunes P, Novais C. **Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain.** *Antibiotics.* Published September 2023. DOI: [10.3390/antibiotics12091474](https://doi.org/10.3390/antibiotics12091474). (rebelo2023unravelingtherole pages 18-20)
4. Dubinkina V, et al. **A transcriptomic atlas of acute stress response to low pH in multiple *Issatchenkia orientalis* strains.** *Microbiology Spectrum.* Published January 2024. DOI: [10.1128/spectrum.02536-23](https://doi.org/10.1128/spectrum.02536-23). (dubinkina2024atranscriptomicatlas pages 1-2)
5. Maksimova YG, Eliseeva A, Maksimov A. **Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633 to Changes in pH and Mineralization.** *International Journal of Microbiology.* Published January 2024. DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 1-2)
6. Baker-Austin C, Dopson M. **Life in acid: pH homeostasis in acidophiles.** *Trends in Microbiology.* Published April 2007. DOI: [10.1016/j.tim.2007.02.005](https://doi.org/10.1016/j.tim.2007.02.005). This supplied foundational PMF reference was identified bibliographically, but full-text evidence was unavailable in the retrieval corpus; use it as corroboration after manual verification rather than as the sole support for a new edge.

## Curation conclusion

`METPO:1000232` is suitable for a TraitMech causal graph if modeled as a **derived, assay-dependent endpoint breadth**. The highest-confidence mechanistic backbone comprises proton-motive-force constraints, intracellular-pH homeostasis, membrane proton permeability, proton-consuming reactions, urease-mediated buffering in designated taxa, and electrogenic cation/proton antiport—especially the genetically supported Mrp system in alkaliphilic *Bacillus*. The graph should connect these modules to lower- and upper-pH growth endpoints and compute pH delta from those endpoints; direct gene-to-pH-delta edges should remain taxon-qualified and generally marked inferred until perturbational growth-range experiments are available.

References

1. (ramoneda2023buildingagenomebased pages 1-1): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (rebelo2023unravelingtherole pages 18-20): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 35 citations.

4. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

9. (krulwich2011molecularaspectsof pages 20-22): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (krulwich2011molecularaspectsof pages 22-23): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

11. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

12. (dubinkina2024atranscriptomicatlas pages 1-2): Veronika Dubinkina, Shounak Bhogale, Ping-Hung Hsieh, Payam Dibaeinia, Ananthan Nambiar, Sergei Maslov, Yasuo Yoshikuni, and Saurabh Sinha. A transcriptomic atlas of acute stress response to low ph in multiple <i>issatchenkia orientalis</i> strains. Jan 2024. URL: https://doi.org/10.1128/spectrum.02536-23, doi:10.1128/spectrum.02536-23. This article has 12 citations and is from a domain leading peer-reviewed journal.