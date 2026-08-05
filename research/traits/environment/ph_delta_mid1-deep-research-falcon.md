---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:21:34.625384'
end_time: '2026-08-04T02:34:58.660316'
duration_seconds: 804.03
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta mid1
  trait_identifier: METPO:1000475
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 2\u20133 pH units, characteristic of organisms with moderate pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_2_3
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports moderate pH-homeostasis flexibility as common among non-extreme microorganisms.)'
  causal_graph_summary: 'ph_delta_mid1_moderate_breadth: 13 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000475
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 2–3 pH units, characteristic of organisms with moderate pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_2_3
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports moderate pH-homeostasis flexibility as common among non-extreme microorganisms.)
- **Existing causal graph summary:** ph_delta_mid1_moderate_breadth: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid1.yaml`.

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
- **Trait label:** pH delta mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000475
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 2–3 pH units, characteristic of organisms with moderate pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_2_3
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports moderate pH-homeostasis flexibility as common among non-extreme microorganisms.)
- **Existing causal graph summary:** ph_delta_mid1_moderate_breadth: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **pH delta mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid1.yaml`.

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


# Microbial Trait Causal Graph Research Report

## Target Trait: pH delta mid1 (METPO:1000475)

**Trait identifier:** METPO:1000475  
**Trait category:** ENVIRONMENT  
**Trait label:** pH delta mid1  
**Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 2–3 pH units, characteristic of organisms with moderate pH-tolerance breadth.  
**Parent trait:** METPO:1000232

---

## 1. Trait Scope and Boundaries

METPO:1000475 represents an assay-observed **growth-supporting pH breadth** spanning approximately 2–3 pH units under defined cultivation conditions. It is operationally distinct from: (a) optimum pH (the single best pH value), (b) transient acid or alkali survival or shock tolerance measured over short exposures, (c) pH preference derived purely from field-survey distribution data, and (d) active pH modification by excretion of acids or bases that changes external pH during growth (sanchezclemente2020carbonsourceinfluence pages 14-16, sanchezclemente2020carbonsourceinfluence pages 1-3). The trait focuses on the range of **initial external pH values** across which reproducible vegetative growth can be sustained, reflecting an integrated physiological capacity to maintain intracellular homeostasis and structural integrity in moderately variable pH environments (krulwich2011molecularaspectsof pages 5-6).

Several experimental factors confound observed breadth: buffering capacity of medium, carbon source identity, and accumulation of metabolic end-products during growth can shift extracellular pH substantially and irreversibly. For example, *E. coli* grown on glucose in minimal medium showed a sudden pH drop during exponential growth that, if extracellular pH fell below 6, became irreversible and arrested further growth, whereas citrate or other oxidized carbon sources led to net alkalinization (sanchezclemente2020carbonsourceinfluence pages 1-3). Thus, the measured breadth is both an intrinsic microbial trait and assay-dependent (sanchezclemente2020carbonsourceinfluence pages 14-16).

---

## 2. Candidate Causal Graph Entities

Below are grouped candidate entities identified through literature review (2023–2024 recent sources plus foundational studies). Ontology CURIEs are provided where stable generic identifiers were verified; label-only entries are shown where species-specific or function-family identifiers were ambiguous.

### Environmental factors and assay parameters
- External pH (ENVO:3100033 or label; also recorded as pHe or pH_external)
- Medium buffering capacity (assay parameter, label-only)
- Carbon source identity (label-only; examples: glucose, citrate, glycerol, fumarate)
- Organic acid accumulation (label-only or CHEBI as specific compounds)

### Cellular biophysical quantities
- Intracellular pH / cytoplasmic pH (GO:0006885 regulation of intracellular pH; also pHi)
- Proton motive force (PMF; label-only or GO:0015986 proton-transporting ATP synthase activity related)
- Membrane potential / transmembrane electrical potential (ψ; label-only)
- Osmotic pressure (label-only)

### Chemical species
- Proton (CHEBI:15378)
- Hydroxide ion (CHEBI:16234)
- Sodium ion (CHEBI:29101)
- Potassium ion (CHEBI:29103)
- Chloride ion (CHEBI:17996)
- Glutamate (CHEBI:29985)
- GABA / γ-aminobutyric acid (CHEBI:16865)
- Arginine (CHEBI:29016)
- Agmatine (CHEBI:17431)
- Calcium ion (CHEBI:29108)
- Magnesium ion (CHEBI:18420)

### Proteins, enzymes, complexes, and transporters

**Proton pumps:**
- F1Fo ATPase (proton-translocating ATPase; EC:7.1.2.2; label for family or organism-specific UniProt entries)
- V-type H+-ATPase (vacuolar in eukaryotes; bacterial homologs; label-only in bacteria)
- H+-PPase (membrane pyrophosphatase; label or Rhea/EC)

**Proton-ion antiporters:**
- NhaA (Na+/H+ antiporter; label; in *E. coli* stoichiometry ~2H+/1Na+)
- NhaB (Na+/H+ antiporter; label)
- ClcA (Cl–/H+ antiporter; label)
- Potassium/proton antiporters (label-only or KefB/KefC families)

**Amino-acid decarboxylase acid-resistance systems:**
- GadA / GadB (glutamate decarboxylase; EC:4.1.1.15; label or UniProt family)
- GadC (glutamate/GABA antiporter; label or gene-family ID)
- AdiA (arginine decarboxylase; EC:4.1.1.19; label)
- AdiC (arginine/agmatine antiporter; label)
- CadA (lysine decarboxylase; label)
- Urease (EC:3.5.1.5; CHEBI:16199 urea substrate)

**Cell-wall synthesis enzymes (pH specialists):**
- PBP1a (penicillin-binding protein 1a, *mrcA* gene product in *E. coli*)
- PBP1b (penicillin-binding protein 1b, *mrcB* gene product in *E. coli*)

**Regulatory systems:**
- PhoP/PhoQ two-component system (label-only or gene-ontology process if available)
- RpoS (sigma factor; label)
- CRP (cyclic-AMP receptor protein; label)
- GadR (positive regulator of GAD system in some LAB; label-only)

**Additional pH-stress response factors:**
- Hydrogenase-3 (label; proton consumption)
- Organic acid permeases (lactate, citrate permeases; label-only)
- Putrescine biosynthesis/uptake (label; polyamine)
- Chaperone/protein repair machinery (label; e.g., DnaK, GroEL)

### Metabolic modules and pathways
- Glycolysis (KEGG pathway or MetaCyc)
- Pentose phosphate pathway (label or MetaCyc)
- TCA cycle (label or KEGG)
- Oxidative phosphorylation (label or MetaCyc)
- GABA shunt / glutamate-GABA metabolic pathway (label or MetaCyc)
- Arginine deiminase pathway (label or MetaCyc)

### Cellular components
- Cytoplasm (GO:0005737)
- Plasma membrane (GO:0005886)
- Cell wall / peptidoglycan layer (GO:0005618)
- Periplasm (GO:0042597)
- Vacuole (in eukaryotes; GO:0005773)

### Biological processes
- Cytoplasmic pH regulation (GO:0006885)
- Proton transport (GO:0015992)
- Response to acid chemical (GO:0001101)
- Response to alkaline pH (label or GO:1900077)
- Biofilm formation (label or GO:0042710)

---

## 3. Evidence-Backed Candidate Edges

Below is a curation-priority table of proposed causal edges with supporting snippets, references, and curation guidance. 

| Priority tier | Proposed mechanism/module | Strongest direct evidence | Applicability to METPO:1000475 | Curation decision |
|---|---|---|---|---|
| High | PMF / proton-ion antiporters / intracellular pH homeostasis | Simultaneous single-cell measurements in *E. coli* showed that lowering PMF impaired pHi maintenance; authors conclude antiporters help determine the extracellular pH range over which homeostasis holds. Strong mechanistic support for external pH -> PMF/antiporter function -> pHi maintenance, though centered on one species and not a 2-3 unit breadth class assay (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | Core generic mechanism plausibly relevant to moderate pH breadth in many neutralophiles | **Curate generic edges** linking external pH, PMF, antiporters, membrane potential, and pHi homeostasis; **do not** encode a specific breadth threshold from this paper |
| High | GadA/GadB-GadC glutamate decarboxylase acid-resistance system | Direct intervention in *E. coli*: glutamate-dependent AR2 raised pHi during pH 2.5 challenge; GadA/GadB + GadC are named structural components; mechanism consumes intracellular protons and reverses membrane potential. Strong but explicitly extreme-acid survival evidence, not growth-range evidence (richard2004escherichiacoliglutamate pages 1-2, richard2004escherichiacoliglutamate pages 6-7) | Relevant as a component mechanism at acidic edge of tolerated range; strongest support is survival at very low pH | **Curate as taxon-specific/acid-edge mechanism with uncertainty**; avoid asserting it defines moderate 2-3 unit growth breadth on its own |
| Medium-High | AdiA-AdiC arginine-dependent acid-resistance system | Same direct *E. coli* study shows arginine-dependent AR3 elevated pHi to 4.7 at pH 2.5 and reversed membrane potential; AdiA and AdiC identified as system components (richard2004escherichiacoliglutamate pages 1-2, richard2004escherichiacoliglutamate pages 6-7) | Mechanistically relevant to acid tolerance edge, but evidence is survival-only and taxon/system specific | **Curate cautiously as taxon-specific uncertain edge**; not sufficient as a generic breadth determinant |
| High | PBP1a/PBP1b cell-wall synthesis enzymes as pH-specialist growth determinants | Deletion study in *E. coli*: ΔmrcB (PBP1b) abolished growth at pH 4.8 and caused 10-25% growth defects at pH 5.1-5.9; ΔmrcA (PBP1a) impaired growth at neutral/alkaline pH. This is direct growth-across-pH evidence, not just survival (mueller2019plasticityofescherichia pages 2-3) | Strongly relevant because it directly modulates growth over a pH interval | **Curate strain-informed but strong growth edges** linking PBP1b to acidic growth fitness and PBP1a to neutral/alkaline fitness; likely best current direct growth-range evidence |
| Medium | F1Fo ATPase / H+-pumps | Reviews identify F1Fo-ATPase and H+-ATPases as central pHi regulators; direct recent experimental support in retrieved set is mainly from engineered yeast H+-PPase improving growth under pH 3.7 acetic acid stress, which is eukaryotic and heterologous (krulwich2011molecularaspectsof pages 5-6, sreenivas2024evaluationofpyrophosphatedriven pages 1-2, sreenivas2024evaluationofpyrophosphatedriven pages 15-17) | Generic proton-pump role is relevant, but direct microbial breadth evidence here is indirect or non-bacterial | **Curate only broad proton-pump -> pHi homeostasis edges if needed and mark weak/general**; **do not** use yeast engineering result as direct bacterial TraitMech evidence |
| High | Medium buffering / carbon source / assay environment | In *E. coli* and *Pseudomonas* spp., buffered minimal medium stabilized pH, whereas LB and carbon source strongly changed extracellular pH; for *E. coli*, a pH drop below 6 was irreversible and arrested further growth. This directly affects observed pH breadth assays (sanchezclemente2020carbonsourceinfluence pages 1-3, sanchezclemente2020carbonsourceinfluence pages 14-16) | Highly relevant as experimental-factor nodes controlling observed trait values | **Curate assay/environment edges** (buffering, carbon source, medium composition -> external pH trajectory -> observed growth breadth) |
| Medium | PhoP/PhoQ regulation under acid adaptation | In *Salmonella Typhimurium*, ΔphoP altered 452 genes after acid adaptation and reduced expression of acid-resistance associated functions; strong regulatory evidence, but adaptation and downstream phenotypes were not breadth-class measurements (gao2024theeffectof pages 7-10) | Potential regulator of acid-edge adaptation, but currently indirect for moderate growth-supporting breadth | **Curate only if regulator nodes are included with uncertainty/taxon-specific flag**; otherwise hold for later |
| Low | Exogenous putrescine / community biofilm pH-stress adaptability | Activated-sludge community study reports putrescine promoted acidic biofilm formation and stimulated glutamate-based AR/GABA pathway and ATPase expression; however evidence is community-level, mixed taxa, and engineering-context specific (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 12-14) | Limited relevance to single-organism trait graph; confounded by community composition and exogenous additive | **Do not curate into core TraitMech graph yet** except perhaps as a low-priority environmental modifier note |
| Medium-Low | Urease / urea-based alkalinization | Strongly supported in reviews and genome-association analysis as a pH-homeostasis mechanism, but retrieved direct evidence here is mostly review/genome-level rather than a direct mutant/growth-breadth experiment for this trait (krulwich2011molecularaspectsof pages 5-6, ramoneda2023buildingagenomebased pages 3-5, li2024responseofescherichia pages 10-12) | Biologically plausible for some taxa, especially acid-exposed organisms, but direct linkage to moderate pH breadth remains insufficient in current set | **Keep as candidate node/edge for future sourcing**; **do not curate as strong edge yet** |


*Table: This table ranks candidate mechanisms for curating METPO:1000475 by how directly they are supported and how well they map to a moderate growth-supporting pH breadth phenotype. It separates strong growth-range evidence from survival-only, taxon-specific, community-level, inferred, and do-not-curate claims.*

### Extended edge-by-edge synopsis with snippets and ontology suggestions:

#### **High-priority edges with direct growth-range evidence**

**Edge 1: PBP1b (MrcB) → growth at acidic pH**  
*Evidence:* Mueller et al. 2019 showed that deletion of *mrcB* (encoding PBP1b) in *E. coli* abolished growth at pH 4.8 and caused 10–25% growth defects (doublings/hour) at pH 5.1–5.9, while wild-type performance was restored at neutral and alkaline pH. Conversely, deletion of *mrcA* (PBP1a) and *mltG* showed specific growth impairment at pH 6.2–8.4 but restored growth at acidic pH (<6.0) (mueller2019plasticityofescherichia pages 2-3).  
*Snippet:* "The ΔmrcB (PBP1b) deletion abolished growth at pH 4.8 and showed 10-25% growth defects (measured as doublings per hour) at pH 5.1-5.9."  
*Curation:* **CURATE** as a strong taxon-informed edge: `PBP1b activity → enables growth in acidic pH range (4.8–5.9)`. Mark as *Escherichia coli*-specific but mechanistically plausible in other Gram-negative bacteria with class-A PBP diversity. Suggest CURIE: label "PBP1b" or UniProt *E. coli* P02919 for reference, generic "penicillin-binding protein 1B" function.  
*DOI:* 10.7554/eLife.40754 (2019)

**Edge 2: PBP1a (MrcA) → growth at neutral/alkaline pH**  
*Evidence:* Same study: ΔmrcA and ΔmltG mutants impaired growth at pH 6.2–8.4, restored at acidic and pH 9.0 (mueller2019plasticityofescherichia pages 2-3).  
*Snippet:* "ΔmrcA (PBP1a) and ΔmltG mutants showed specific growth impairment at neutral and alkaline pH (6.2-8.4 range), with growth restored to wild-type levels at acidic pH (<6.0) and pH 9.0."  
*Curation:* **CURATE** as: `PBP1a activity → enables growth in neutral/alkaline pH range`. Same taxon/uncertainty flags as PBP1b.  
*DOI:* 10.7554/eLife.40754 (2019)

#### **High-priority edges: PMF / antiporter / cytoplasmic pH homeostasis**

**Edge 3: Extracellular pH (acidic) + proton motive force → intracellular pH homeostasis**  
*Evidence:* Terradot et al. 2024 used concurrent single-cell measurements of flagellar motor speed (proxy for PMF) and pHi (pHluorin biosensor) in *E. coli*. Lowering PMF magnitude impaired cells' ability to maintain pHi during extracellular pH shifts, and cells had negligible membrane potential when PMF was zero. Authors propose antiporters generate membrane potential (ψ) powered by metabolism-driven proton export, with the strength of PMF setting the extracellular pH range over which homeostasis holds (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9, terradot2024escherichiacolimaintains pages 9-10).  
*Snippet:* "Decreasing the PMF's strength impairs the cells' ability to maintain pH… cells have negligible membrane potential when there is no PMF… our model predicts that the strength of the PMF sets the maximal rate at which the antiporters work, and so determines the extracellular pH range for which the two homeostases hold."  
*Curation:* **CURATE** generic edges: `external pH → proton gradient (PMF) → antiporter flux → cytoplasmic pH homeostasis`. Do **not** encode a specific 2–3 unit threshold from this paper; it did not define moderate breadth classes but provides the core mechanistic scaffold.  
*Ontology:* external pH (label or ENVO:3100033), PMF (label), pHi (GO:0006885), membrane potential (label).  
*DOI:* 10.1103/PRXLife.2.043015 (2024)

**Edge 4: NhaA (Na+/H+ antiporter, 2:1 stoichiometry) → membrane potential generation under alkaline pH**  
*Evidence:* Krulwich et al. 2011 foundational review: NhaA antiporter stoichiometry is 2H+/1Na+, critical for neutralophilic bacterial homeostasis under alkaline conditions. Ramoneda et al. 2023 genome-association study confirmed NhaA-like antiporters associated with high-pH preference across soil and freshwater bacteria (krulwich2011molecularaspectsof pages 5-6, ramoneda2023buildingagenomebased pages 3-5).  
*Snippet:* "NhaA-like antiporter in alkaline pH [30,54,55], with its activity increasing once pHe goes above 6.5."  
*Curation:* **CURATE** as: `alkaline external pH → NhaA antiporter activity → sodium efflux + proton import → membrane potential (ψ)`. Mark as generic bacterial mechanism but verify taxon presence. CURIE: gene family label or UniProt P13738 (*E. coli* NhaA).  
*DOI:* 10.1038/nrmicro2549 (2011); 10.1126/sciadv.adf8998 (2023)

**Edge 5: ClcA (Cl–/H+ antiporter) → membrane potential generation under acidic pH**  
*Evidence:* Terradot 2024 modeling and Krulwich 2011: ClcA exports chloride ions in acidic regimes to generate ψ, with central metabolism exporting the protons imported by ClcA (terradot2024escherichiacolimaintains pages 1-2, krulwich2011molecularaspectsof pages 5-6).  
*Snippet:* "ClcA, rather than exporting protons to raise pHi, exports chloride ions to generate ψ… consistently, ClcA is important at acidic pH."  
*Curation:* **CURATE**: `acidic external pH → ClcA antiporter activity → chloride efflux → membrane potential`. Chloride CURIE: CHEBI:17996.  
*DOI:* 10.1103/PRXLife.2.043015 (2024); 10.1038/nrmicro2549 (2011)

**Edge 6: K+/H+ antiporters → potassium homeostasis under osmotic/pH stress**  
*Evidence:* Multiple reviews (Krulwich 2011, Ramoneda 2023) cite K+ efflux/uptake systems as pH homeostasis factors (krulwich2011molecularaspectsof pages 5-6, ramoneda2023buildingagenomebased pages 3-5).  
*Curation:* **CURATE** generic edge if needed, but supporting evidence is less direct for moderate breadth; mark uncertain or pathway-level.  
*DOI:* 10.1038/nrmicro2549 (2011); 10.1126/sciadv.adf8998 (2023)

#### **Medium-priority edges: glutamate decarboxylase acid-resistance system (GadA/GadB-GadC)**

**Edge 7: GadA/GadB (glutamate decarboxylase) + GadC (antiporter) → intracellular proton consumption under extreme acid**  
*Evidence:* Richard & Foster 2004 showed that *E. coli* AR2 glutamate-dependent system (GadA/GadB + GadC antiporter) raised pHi from 3.6 to 4.2 during pH 2.5 challenge, consumed intracellular H+, and reversed membrane potential to positive-inside (Δψ ~+30 mV with glutamate) during extreme acid survival (richard2004escherichiacoliglutamate pages 1-2, richard2004escherichiacoliglutamate pages 6-7). Krulwich 2011 review confirms GadB activation under acid and consumption of cytoplasmic protons via conversion to GABA (krulwich2011molecularaspectsof pages 5-6).  
*Snippet:* "Glutamate-dependent systems elevated pHi from 3.6 to 4.2… glutamate or arginine reversed the membrane potential, and Δψ became positive inside… The accumulation of the positively charged decarboxylation product most likely accounts for the reversal of transmembrane potential."  
*Taxon scope:* *E. coli*, *Lactobacillus* spp., and other enteric/LAB with GAD operon (sezgin2023molecularevolutionand pages 13-20, sezgin2023molecularevolutionand pages 38-43).  
*Curation:* **CURATE with uncertainty and taxon-specific flag**: `acidic external pH → GadB activation → glutamate + H+ → GABA → proton consumption → pHi increase`. This is mechanistically relevant to the acidic edge of moderate pH breadth but strongest evidence is for transient extreme-acid survival, not steady-state growth across a 2–3 unit range. Do **not** assert this defines moderate breadth alone.  
*Ontology:* GadA/GadB (EC:4.1.1.15 or label), GadC (label), glutamate (CHEBI:29985), GABA (CHEBI:16865), proton (CHEBI:15378).  
*DOI:* 10.1128/JB.186.18.6032-6041.2004 (2004); 10.1038/nrmicro2549 (2011)

**Edge 8: GadR → positive regulation of GadC-Gad1 operon (in Lactobacillus brevis)**  
*Evidence:* Sezgin & Tekin 2023 report GadR is a positive regulator of the GAD system in *L. brevis*, increasing expression of gadC and gad1 genes, thereby enhancing GABA synthesis and acid resistance (sezgin2023molecularevolutionand pages 13-20, sezgin2023molecularevolutionand pages 38-43).  
*Snippet:* "Mutation studies of the L. brevis gadR gene have shown that the gadR gene is a positive regulator of the GAD system, increasing the expression of the gadC1 operon (gadC and gad1) and GABA synthesis."  
*Curation:* **CURATE cautiously** as taxon-specific regulatory edge if including transcription factors; otherwise hold for later curation stages.  
*DOI:* 10.3389/fgene.2023.1027156 (2023)

#### **Medium-priority edges: arginine-dependent acid resistance (AdiA-AdiC)**

**Edge 9: AdiA (arginine decarboxylase) + AdiC (antiporter) → proton consumption during extreme acid**  
*Evidence:* Richard & Foster 2004: *E. coli* AR3 arginine-dependent system raised pHi to 4.7 at pH 2.5 challenge and reversed membrane potential to Δψ ~+80 mV during extreme acid survival (richard2004escherichiacoliglutamate pages 1-2).  
*Snippet:* "Arginine-dependent AR3… elevated pHi… to 4.7… addition of arginine reversed the membrane potential, and Δψ became positive inside (~+80 for arginine)."  
*Curation:* **CURATE cautiously as taxon-specific uncertain edge**: `acidic external pH → AdiA activation → arginine + H+ → agmatine → proton consumption`. Same caveats as GadA/B-GadC: survival evidence, not steady growth range.  
*Ontology:* AdiA (EC:4.1.1.19 or label), AdiC (label), arginine (CHEBI:29016), agmatine (CHEBI:17431).  
*DOI:* 10.1128/JB.186.18.6032-6041.2004 (2004)

#### **Medium-priority edges: F1Fo ATPase and proton pumps**

**Edge 10: F1Fo ATPase → proton export → cytoplasmic pH homeostasis**  
*Evidence:* Krulwich 2011 and multiple reviews identify F1Fo-ATPase (and in Gram-positives, P-type H+-ATPases) as central active proton efflux mechanism under acid stress. Ramoneda 2023 genome-association study found cation/anion transporter genes (including components linked to proton pumps) associated with pH preference (krulwich2011molecularaspectsof pages 5-6, ramoneda2023buildingagenomebased pages 3-5).  
*Snippet:* "E. coli and other neutralophiles employ active proton extrusion via respiratory chain complexes and F1Fo ATPases under acid stress… F1Fo-ATPase regulates pHi of cells by pumping protons out."  
*Curation:* **CURATE broad generic edge if needed**: `acidic stress → F1Fo ATPase activity (ATP hydrolysis) → proton efflux → pHi maintenance`. However, note that direct moderate-breadth evidence here is less specific.  
*Ontology:* F1Fo ATPase (EC:7.1.2.2 or label), proton (CHEBI:15378), GO:0015992 proton transport.  
*DOI:* 10.1038/nrmicro2549 (2011); 10.1126/sciadv.adf8998 (2023)

**Edge 11: H+-PPase (membrane pyrophosphatase) → proton export using PPi**  
*Evidence:* Sreenivas et al. 2024 tested heterologous expression of plant H+-PPase in *Saccharomyces cerevisiae* (vacuolar or plasma membrane targeting) under acetic acid stress at pH 3.7. Vacuolar membrane H+-PPase strain showed 35% growth rate improvement versus parent. However, this is eukaryotic, engineered, and not direct bacterial TraitMech evidence (sreenivas2024evaluationofpyrophosphatedriven pages 1-2, sreenivas2024evaluationofpyrophosphatedriven pages 15-17).  
*Curation:* **Do not curate as strong bacterial edge**; if needed, mark as eukaryotic engineering example only. Bacterial H+-PPases exist but direct moderate-breadth evidence not in current set.  
*DOI:* 10.3390/microorganisms12030625 (2024)

#### **Medium-priority edges: medium buffering and carbon source**

**Edge 12: Carbon source oxidation state → extracellular pH trajectory during growth**  
*Evidence:* Sanchez-Clemente et al. 2020 demonstrated that in minimal medium with *E. coli*, *Pseudomonas putida*, and *P. pseudoalcaligenes*, oxidized carbon sources (citrate, 2-furoate, 2-oxoglutarate, fumarate) led to net alkalinization of medium, whereas reduced carbon sources (glucose, glycerol, octanoate) caused slight acidification. Genome-scale metabolic models correctly predicted these pH changes. In *E. coli*, a pH drop below 6 during growth on glucose became irreversible and arrested further growth (sanchezclemente2020carbonsourceinfluence pages 1-3, sanchezclemente2020carbonsourceinfluence pages 14-16).  
*Snippet:* "While glucose, glycerol, or octanoate slightly decreased extracellular pH, more oxidized carbon sources… ended up with the alkalinization of the medium… In the case of E. coli, a sudden drop in pH was observed during exponential cell growth that was later recovered at initial pH 7 or 8, but was irreversible below pH 6, thus arresting further cell-growth."  
*Curation:* **CURATE as assay-environment modifier edges**: `carbon source (oxidized) → alkalinization → change in effective pH range` and `carbon source (reduced) → acidification → may restrict pH breadth if unbuffered`. These are critical experimental factors that influence observed breadth phenotype.  
*Ontology:* carbon source (label-only, or specific compounds CHEBI), buffering capacity (assay parameter).  
*DOI:* 10.3390/genes11111292 (2020)

**Edge 13: Medium buffering capacity → stabilization of external pH during growth**  
*Evidence:* Same study: buffered minimal medium (M63) stabilized pH during growth, whereas unbuffered Luria-Bertani (LB) showed convergence to organism-specific pH (sanchezclemente2020carbonsourceinfluence pages 1-3).  
*Snippet:* "In Luria-Bertani (LB) media, pH evolved by converging to a certain value that is specific for each bacterium. By contrast, in the buffered Minimal Medium (MM), pH was generally more stable along the growth curve."  
*Curation:* **CURATE as assay parameter**: `buffering present → more stable external pH → observable breadth closer to intrinsic capacity`; `no buffer → pH drift → observed breadth may be narrower or distorted`.  
*DOI:* 10.3390/genes11111292 (2020)

#### **Medium-priority edges: PhoP/PhoQ regulation**

**Edge 14: PhoP/PhoQ two-component system → regulation of acid-resistance gene expression**  
*Evidence:* Gao et al. 2024 showed that in *Salmonella typhimurium*, deletion of *phoP* after acid adaptation (pH 5.4 for 90 min) led to 452 differentially expressed genes, with downregulation of acid-resistance functions (amino acid transporters, metal ion binding, redox activity), antimicrobial peptide resistance pathways (CAMP, quorum sensing), and membrane composition genes. Polymyxin B MIC was reduced 16-fold in ΔphoP (2 vs 32 µg/mL for adapted WT) (gao2024theeffectof pages 7-10).  
*Snippet:* "The ∆phoP mutant showed 452 differentially expressed genes… genes related to acidic environment resistance (amino acid transporters, metal ion binding, redox activity) were significantly downregulated in ∆phoP (p<0.05)."  
*Taxon:* *Salmonella typhimurium*, acid adaptation context.  
*Curation:* **CURATE only if including regulatory nodes**, with taxon-specific and uncertain flags; the study addressed acid adaptation and stress response, not direct growth-range breadth. May be valuable as a regulatory hub node but not a defining edge for moderate breadth.  
*DOI:* 10.3390/foods13101533 (2024)

#### **Low-priority edges: exogenous putrescine and community biofilm**

**Edge 15: Exogenous putrescine → enhanced acid-stress biofilm formation**  
*Evidence:* Jiang et al. 2024 studied activated-sludge biofilm communities with exogenous putrescine. Under acidic conditions, putrescine promoted biofilm formation, increased cell membrane permeability, stimulated glutamate-based acid resistance and GABA metabolic pathway, and enhanced ATPase expression. Under alkaline conditions, putrescine inhibited biofilm formation and increased alkaliphilic bacteria and *Bdellovibrio* predators (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 12-14).  
*Snippet:* "Exogenous putrescine acted as a switch-like distributor affecting microorganism pH stress, thus promoting biofilm formation under acid conditions while inhibiting it under alkaline conditions… putrescine consumed intracellular H+ by enhancing the glutamate-based acid resistance strategy and the γ-aminobutyric acid metabolic pathway."  
*Curation:* **Do not curate into core single-organism TraitMech graph yet**; evidence is community-level, mixed taxa, biofilm-specific, and engineering context. May be noted as a low-priority environmental modifier or application example.  
*DOI:* 10.1128/aem.00569-24 (2024)

#### **Candidate edges not yet strongly supported for METPO:1000475:**

- **Urease → urea hydrolysis → ammonia production → local alkalinization:** Reviewed as a mechanism in Krulwich 2011 and genome-association Ramoneda 2023, but direct deletion/growth-range experiments not in current evidence set. **Hold for future sourcing.**  
- **Lysine decarboxylase (CadA) → lysine-dependent acid resistance:** Mentioned in reviews as less effective than GadA/B or AdiA (krulwich2011molecularaspectsof pages 5-6, richard2004escherichiacoliglutamate pages 1-2). **Hold pending direct evidence.**  
- **Membrane lipid saturation/fluidity changes → proton permeability modulation:** Reviewed but not directly linked to moderate breadth in current set. **Hold.**  
- **Hydrogenase-3 → proton consumption during fermentation under extreme acid:** Reviewed in Krulwich 2011 (krulwich2011molecularaspectsof pages 5-6) as relevant to *E. coli* pH 2–2.5 survival. **Mark as survival-specific, not growth-range.**

---

## 4. Ontology Grounding Summary

Where stable, generic CURIEs were verified, they have been provided above. Key assignments include:

- **CHEBI:** proton (15378), sodium (29101), potassium (29103), chloride (17996), glutamate (29985), GABA (16865), arginine (29016), agmatine (17431), urea (16199)  
- **GO:** regulation of intracellular pH (0006885), proton transport (0015992), cytoplasm (0005737), plasma membrane (0005886), cell wall (0005618), response to acid chemical (0001101)  
- **ENVO:** environmental pH (3100033, or label)  
- **EC:** glutamate decarboxylase (4.1.1.15), arginine decarboxylase (4.1.1.19), urease (3.5.1.5), F1Fo ATPase (7.1.2.2)  
- **UniProt / gene families:** Where species-specific, such as *E. coli* NhaA (P13738), PBP1a (P02918), PBP1b (P02919), GadA, GadB, AdiA, etc., **use as reference only** or label "gene family" if cross-species curation is intended.

Label-only nodes (without stable IDs assigned in this report): medium buffering capacity, carbon source, membrane potential (ψ), PMF, biofilm, putrescine, many regulatory proteins, and protein complexes where family-level IDs were ambiguous.

---

## 5. Curation Warnings and Do-Not-Curate Flags

1. **Do not conflate extreme acid/alkali survival with moderate pH growth breadth.** The strongest mechanistic evidence for GadA/B-GadC and AdiA-AdiC systems comes from transient survival at pH 2–2.5, not from steady-state vegetative growth across a 2–3 unit interval (richard2004escherichiacoliglutamate pages 1-2, richard2004escherichiacoliglutamate pages 6-7). Curate these as component mechanisms relevant to the acidic edge of tolerated range, with explicit uncertainty and taxon flags.

2. **Do not use non-bacterial or heterologous engineering results as direct bacterial TraitMech evidence.** For example, yeast *S. cerevisiae* heterologous H+-PPase under acetic acid stress (Sreenivas et al. 2024) does not directly inform bacterial moderate pH breadth graphs (sreenivas2024evaluationofpyrophosphatedriven pages 1-2).

3. **Do not encode assay-dependent pH drift as an intrinsic mechanism.** Medium buffering, carbon source identity, and metabolic end-product accumulation are experimental factors that modulate observed pH breadth (sanchezclemente2020carbonsourceinfluence pages 1-3, sanchezclemente2020carbonsourceinfluence pages 14-16). Curate these as **assay environment nodes** that influence the trait measurement, not as microbial genes or pathways.

4. **Do not curate community-level or biofilm-specific polyamine results into single-organism graphs yet.** Activated-sludge biofilm putrescine responses (Jiang et al. 2024) are valuable for engineering but confounded by mixed taxa and exogenous additive (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 12-14).

5. **Distinguish between optimum pH and breadth.** The foundational Krulwich 2011 review (krulwich2011molecularaspectsof pages 5-6) and genome-association Ramoneda 2023 (ramoneda2023buildingagenomebased pages 3-5) address pH preference and homeostasis mechanisms but do not define breadth classes. Use these as mechanistic background, not as direct breadth-trait assertions.

6. **Mark PBP1a/PBP1b edges as *E. coli*-informed but mechanistically generalizable.** Mueller et al. 2019 provided the strongest direct growth-range deletion evidence but in one species (mueller2019plasticityofescherichia pages 2-3). Extrapolation to other Gram-negatives is plausible but requires taxon-specific flag in TraitMech YAML.

7. **Verify strain-specific protein identifiers before curation.** This report provides label-only or family-level names for most enzymes and transporters. Before finalizing YAML, cross-reference UniProt, InterPro, or KEGG for stable organism-agnostic or representative-strain identifiers.

---

## 6. DOI-First Bibliography (Recent First, Then Foundational)

**2024 sources:**

- Terradot, G., Krasnopeeva, E., Swain, P. S., & Pilizota, T. (2024). *Escherichia coli* maintains pH via the membrane potential. *PRX Life*, 2(4), 043015. DOI: [10.1103/PRXLife.2.043015](https://doi.org/10.1103/PRXLife.2.043015) — **Concurrent PMF/pHi measurements, antiporter role in membrane potential, E. coli.**

- Gao, X., Han, J., Zhu, L., Nychas, G.-J. E., Mao, Y., Yang, X., Liu, Y., Jiang, X., Zhang, Y., & Dong, P. (2024). The effect of the PhoP/PhoQ system on the regulation of multi-stress adaptation induced by acid stress in *Salmonella* Typhimurium. *Foods*, 13(10), 1533. DOI: [10.3390/foods13101533](https://doi.org/10.3390/foods13101533) — **PhoP/PhoQ deletion, transcriptomics, acid adaptation, Salmonella.**

- Li, Z., Huang, Z., & Gu, P. (2024). Response of *Escherichia coli* to acid stress: mechanisms and applications—a narrative review. *Microorganisms*, 12(9), 1774. DOI: [10.3390/microorganisms12091774](https://doi.org/10.3390/microorganisms12091774) — **Review: six AR systems, membrane protection, macromolecular repair, E. coli.**

- Sreenivas, K., Eisentraut, L., Brink, D. P., Persson, V. C., Carlquist, M., Gorwa-Grauslund, M. F., & van Niel, E. W. J. (2024). Evaluation of pyrophosphate-driven proton pumps in *Saccharomyces cerevisiae* under stress conditions. *Microorganisms*, 12(3), 625. DOI: [10.3390/microorganisms12030625](https://doi.org/10.3390/microorganisms12030625) — **Heterologous H+-PPase in yeast, acetic acid stress, eukaryotic.**

- Jiang, G., Wang, C., Wang, Y., Wang, J., Xue, Y., Lin, Y., Hu, X., & Lv, Y. (2024). Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge. *Applied and Environmental Microbiology*, 90(7), e00569-24. DOI: [10.1128/aem.00569-24](https://doi.org/10.1128/aem.00569-24) — **Community biofilm, putrescine, GAD pathway, ATPase, mixed taxa.**

**2023 sources:**

- Ramoneda, J., Stallard-Olivera, E., Hoffert, M., Winfrey, C. C., Stadler, M., Niño-García, J. P., & Fierer, N. (2023). Building a genome-based understanding of bacterial pH preferences. *Science Advances*, 9(17), eadf8998. DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998) — **Genome-wide association: 56 genes, decarboxylases, K+ pumps, Na+/H+ antiporters, urease, hydrogenase, multi-environment.**

- Sezgin, E., & Tekin, B. (2023). Molecular evolution and population genetics of glutamate decarboxylase acid resistance pathway in lactic acid bacteria. *Frontiers in Genetics*, 14, 1027156. DOI: [10.3389/fgene.2023.1027156](https://doi.org/10.3389/fgene.2023.1027156) — **GAD pathway evolution, L. brevis, L. plantarum, GadR regulator, operon structure.**

**2020–2021 sources:**

- Sánchez-Clemente, R., Guijo, M. I., Nogales, J., & Blasco, R. (2020). Carbon source influence on extracellular pH changes along bacterial cell-growth. *Genes*, 11(11), 1292. DOI: [10.3390/genes11111292](https://doi.org/10.3390/genes11111292) — **Carbon source oxidation state, pH trajectory, E. coli/Pseudomonas, genome-scale models.**

**2019 foundational:**

- Mueller, E. A., Egan, A. J. F., Breukink, E., Vollmer, W., & Levin, P. A. (2019). Plasticity of *Escherichia coli* cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions. *eLife*, 8, e40754. DOI: [10.7554/eLife.40754](https://doi.org/10.7554/eLife.40754) — **PBP1a/PBP1b deletion, direct pH growth-range phenotypes, 32 mutants, E. coli.**

**2004 foundational:**

- Richard, H., & Foster, J. W. (2004). *Escherichia coli* glutamate- and arginine-dependent acid resistance systems increase internal pH and reverse transmembrane potential. *Journal of Bacteriology*, 186(18), 6032–6041. DOI: [10.1128/JB.186.18.6032-6041.2004](https://doi.org/10.1128/JB.186.18.6032-6041.2004) — **Direct pHi and Δψ measurements, GadA/B-GadC AR2, AdiA-AdiC AR3, E. coli, pH 2.5 survival.**

**2011 foundational review:**

- Krulwich, T. A., Sachs, G., & Padan, E. (2011). Molecular aspects of bacterial pH sensing and homeostasis. *Nature Reviews Microbiology*, 9(5), 330–343. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549) — **Authoritative review: antiporters, F1Fo ATPase, GadB, hydrogenase-3, membrane lipids, acidophiles/alkaliphiles, neutralophiles.**

---

## 7. Summary and Recommended Next Steps

This report identifies a moderate-priority set of mechanistic entities and causal edges for curating METPO:1000475 into `data/traits/environment/ph_delta_mid1.yaml`. The **strongest direct evidence for growth-range modulation** comes from PBP1a/PBP1b deletion studies (Mueller 2019), which should form the core high-confidence edges. The **PMF–antiporter–pHi homeostasis module** (Terradot 2024, Krulwich 2011) provides the central electrophysiological scaffold and should be curated as generic bacterial mechanisms with appropriate abstraction. **GadA/B-GadC and AdiA-AdiC systems** are well-supported for extreme acid survival but must be marked as taxon-specific and survival-edge mechanisms, not defining moderate breadth alone. **Medium buffering and carbon source effects** are critical assay-environment modifiers and should be explicitly represented to avoid conflating intrinsic and experimental determinants of observed breadth.

**Curation priorities:**
1. High: PBP1a/PBP1b → pH-dependent growth edges (direct, quantitative).
2. High: external pH → PMF → antiporter → pHi homeostasis module (generic core).
3. Medium-high: GadA/B-GadC, AdiA-AdiC (acidic edge, taxon-specific, survival-supported).
4. High: buffering, carbon source → external pH trajectory (assay environment).
5. Medium: F1Fo ATPase, NhaA, ClcA (generic mechanisms, less direct breadth evidence).
6. Medium-low: PhoP/PhoQ, GadR (regulatory, indirect).
7. Low/hold: urease, CadA, putrescine community, H+-PPase in yeast (pending better evidence or marked uncertain).

**Do not curate until better sourcing:** urease (label-only, no direct deletion for breadth), eukaryotic H+-PPase, community putrescine responses, membrane lipid fluidity (review-only).

All edges should be entered into YAML with provenance (DOI), supporting snippet, taxon scope, and uncertainty flags as outlined in the curation-priority table above.

References

1. (sanchezclemente2020carbonsourceinfluence pages 14-16): Rubén Sánchez-Clemente, M. Isabel Guijo, Juan Nogales, and Rafael Blasco. Carbon source influence on extracellular ph changes along bacterial cell-growth. Genes, 11:1292, Oct 2020. URL: https://doi.org/10.3390/genes11111292, doi:10.3390/genes11111292. This article has 76 citations.

2. (sanchezclemente2020carbonsourceinfluence pages 1-3): Rubén Sánchez-Clemente, M. Isabel Guijo, Juan Nogales, and Rafael Blasco. Carbon source influence on extracellular ph changes along bacterial cell-growth. Genes, 11:1292, Oct 2020. URL: https://doi.org/10.3390/genes11111292, doi:10.3390/genes11111292. This article has 76 citations.

3. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

4. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

5. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

6. (richard2004escherichiacoliglutamate pages 1-2): Hope Richard and John W. Foster. Escherichia coli glutamate- and arginine-dependent acid resistance systems increase internal ph and reverse transmembrane potential. Journal of Bacteriology, 186:6032-6041, Sep 2004. URL: https://doi.org/10.1128/jb.186.18.6032-6041.2004, doi:10.1128/jb.186.18.6032-6041.2004. This article has 493 citations and is from a peer-reviewed journal.

7. (richard2004escherichiacoliglutamate pages 6-7): Hope Richard and John W. Foster. Escherichia coli glutamate- and arginine-dependent acid resistance systems increase internal ph and reverse transmembrane potential. Journal of Bacteriology, 186:6032-6041, Sep 2004. URL: https://doi.org/10.1128/jb.186.18.6032-6041.2004, doi:10.1128/jb.186.18.6032-6041.2004. This article has 493 citations and is from a peer-reviewed journal.

8. (mueller2019plasticityofescherichia pages 2-3): Elizabeth A Mueller, Alexander JF Egan, Eefjan Breukink, Waldemar Vollmer, and Petra Anne Levin. Plasticity of escherichia coli cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions. eLife, Apr 2019. URL: https://doi.org/10.7554/elife.40754, doi:10.7554/elife.40754. This article has 126 citations and is from a domain leading peer-reviewed journal.

9. (sreenivas2024evaluationofpyrophosphatedriven pages 1-2): Krishnan Sreenivas, Leon Eisentraut, Daniel P. Brink, Viktor C. Persson, Magnus Carlquist, Marie F. Gorwa-Grauslund, and Ed W. J. van Niel. Evaluation of pyrophosphate-driven proton pumps in saccharomyces cerevisiae under stress conditions. Microorganisms, 12:625, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030625, doi:10.3390/microorganisms12030625. This article has 4 citations.

10. (sreenivas2024evaluationofpyrophosphatedriven pages 15-17): Krishnan Sreenivas, Leon Eisentraut, Daniel P. Brink, Viktor C. Persson, Magnus Carlquist, Marie F. Gorwa-Grauslund, and Ed W. J. van Niel. Evaluation of pyrophosphate-driven proton pumps in saccharomyces cerevisiae under stress conditions. Microorganisms, 12:625, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030625, doi:10.3390/microorganisms12030625. This article has 4 citations.

11. (gao2024theeffectof pages 7-10): Xu Gao, Jina Han, Lixian Zhu, George-John E. Nychas, Yanwei Mao, Xiaoyin Yang, Yunge Liu, Xueqing Jiang, Yimin Zhang, and Pengcheng Dong. The effect of the phop/phoq system on the regulation of multi-stress adaptation induced by acid stress in salmonella typhimurium. Foods, 13:1533, May 2024. URL: https://doi.org/10.3390/foods13101533, doi:10.3390/foods13101533. This article has 18 citations.

12. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

13. (jiang2024exogenousputrescineplays pages 12-14): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

14. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

15. (li2024responseofescherichia pages 10-12): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

16. (terradot2024escherichiacolimaintains pages 9-10): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

17. (sezgin2023molecularevolutionand pages 13-20): Efe Sezgin and Burcu Tekin. Molecular evolution and population genetics of glutamate decarboxylase acid resistance pathway in lactic acid bacteria. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2023.1027156, doi:10.3389/fgene.2023.1027156. This article has 20 citations and is from a peer-reviewed journal.

18. (sezgin2023molecularevolutionand pages 38-43): Efe Sezgin and Burcu Tekin. Molecular evolution and population genetics of glutamate decarboxylase acid resistance pathway in lactic acid bacteria. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2023.1027156, doi:10.3389/fgene.2023.1027156. This article has 20 citations and is from a peer-reviewed journal.