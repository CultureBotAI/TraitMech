---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:05:41.117254'
end_time: '2026-06-18T07:21:59.987634'
duration_seconds: 978.87
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width medium
  trait_identifier: METPO:1000889
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_medium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension lies approximately
    between 0.65 and 0.9 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_0.65_0.9
  evidence_summary: "DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan\
    \ synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths\
    \ in the 0.65\u20130.9 \u03BCm range.)"
  causal_graph_summary: 'cell_width_medium_typical_rod: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width medium
- **METPO identifier:** METPO:1000889
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.65 and 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.65_0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths in the 0.65–0.9 μm range.)
- **Existing causal graph summary:** cell_width_medium_typical_rod: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_medium.yaml`.

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
- **Trait label:** cell width medium
- **METPO identifier:** METPO:1000889
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.65 and 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.65_0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing typical rod widths in the 0.65–0.9 μm range.)
- **Existing causal graph summary:** cell_width_medium_typical_rod: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width medium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_medium.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **cell width medium** (METPO:1000889)

### Scope summary (trait meaning and boundaries)
**Trait definition (curation target):** *cell width medium* is a morphology phenotype describing the **shorter cell dimension (diameter/width)** being approximately **0.65–0.9 µm**, corresponding to “typical” rod widths for many bacteria under standard growth conditions.

**Operational quantitative anchors from recent data:** Recent single-cell analyses and modeling of *E. coli* width dynamics support a typical/regulated width set-point in the mid-range of this trait: untreated cells show **width saturation wmx ≈ 0.74–0.75 µm**, with a linear-model lower estimate **wmin ≈ 0.65 µm**, and a modeled “regulated” regime **wmx ≤ 0.83 µm**. These values fall squarely within METPO:1000889’s 0.65–0.9 µm bin and provide empirically grounded reference points for the medium-width category. (kale2024mechanicsofe. pages 10-13)

**Boundary cases / distinctions:**
- **<0.65 µm**: likely narrower-than-medium rods (neighbor trait not provided here). (kale2024mechanicsofe. pages 10-13)
- **>0.9 µm**: likely “wide rods” or approaching spherical morphology, depending on length and aspect ratio. Modeling suggests dysregulated widening becomes prominent above ~0.83 µm and severe dysregulation/bulging can extend beyond ~1.3 µm under envelope-compromising conditions. (kale2024mechanicsofe. pages 10-13)
- **Not cell length:** filamentation/elongation changes can occur without changing the width category; keep width and length as separate phenotypes. (kale2024mechanicsofe. pages 10-13)

### Key concepts and current mechanistic understanding
#### 1) Width is a **cell-envelope construction** and **mechanics** phenotype
Cell width is ultimately constrained by peptidoglycan (PG) architecture and envelope mechanics: PG is the major load-bearing structure determining cell shape and protecting against osmotic lysis. (shlosman2023allostericactivationof pages 1-2, zhang2023coordinatedpeptidoglycansynthases pages 1-2)

A recent mechanical model of *E. coli* width homeostasis emphasizes that width regulation can be described by a **width saturation** dynamic in untreated cells and becomes deregulated under perturbations; the authors explicitly connect similar kinetics across strains to shared mechanistic drivers including **total cellular pressure, cell wall growth, and MreB assembly dynamics**. (kale2024mechanicsofe. pages 10-13)

#### 2) The Rod complex / elongasome provides a major **width set-point** mechanism
Multiple recent papers (2023–2024) consolidate the view that the **Rod complex (elongasome)**—centered on the SEDS–bPBP synthase pair **RodA–PBP2** and organized by **MreB** with accessory factors (**MreC/MreD/RodZ**)—is a primary determinant of rod shape and width homeostasis.

- In *E. coli*, the Rod complex comprises **MreB, RodA, PBP2, RodZ, MreC, MreD** and supports evenly distributed wall insertion via circumferential movement; disrupted component interactions produce abnormal morphology and defective PG (holes, altered composition), consistent with a causal chain from Rod-complex integrity → PG structure → width/shape. (ago2023relationshipbetweenthe pages 1-3)
- In *A. baumannii*, perturbations to **PBP2** function (e.g., carbapenems or Zn deprivation) cause a **rod-to-sphere transition**, resembling RodA–PBP2 deficiency, indicating that PBP2 is a major elongasome-directed shape determinant. (micelli2023aconservedzincbinding pages 1-2)

#### 3) **Allosteric activation** of RodA–PBP2 couples polymerization and crosslinking
A major recent advance is direct structural/biophysical evidence that the essential elongation synthase **RodA–PBP2** transitions between **closed and open states**, and that **structural opening couples activation of glycan polymerization and peptide crosslinking**, being essential in vivo. This provides an explicit mechanistic entity (RodA–PBP2 conformational state) that can be curated as a causal regulator of envelope construction and, indirectly, width. (shlosman2023allostericactivationof pages 1-2)

A 2024 preprint further proposes that **MreC–MreD** interactions control MreC conformation in a way compatible with PBP2 allosteric activation and notes that loss of MreC/MreD can be rescued by mutations stabilizing an “open” PBP2 state—supporting MreC/MreD as upstream activators/modulators of the RodA–PBP2 synthase. (gilman2024mrecmredstructurereveals pages 1-2)

#### 4) Width depends on coordination between **PG synthases and PG hydrolases**
A 2023 Nature Communications study in *Myxococcus xanthus* highlights that two systems contribute to elongation PG dynamics: the **Rod system** (RodA, PBP2, MreB) and **class A PBPs (aPBPs)**. It explicitly states that while the Rod system determines rod shape, **aPBPs “regulate cell diameter”**. (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

The same study shows that **moenomycin inhibition of aPBPs** can rapidly collapse rod shape by promoting **DacB** (a PG hydrolase/peptidase) association with PG and accelerating pole degradation—illustrating that width/shape can be destabilized by disrupting synthase–hydrolase coordination rather than eliminating individual enzymes. (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

### Recent developments and latest research (prioritizing 2023–2024)
#### A) 2023: RodA–PBP2 open/closed states as a conserved regulatory mechanism
Single-molecule FRET + cryo-EM showed RodA–PBP2 toggles between closed/open states; opening couples polymerization and crosslinking and is essential in vivo. This provides a mechanistic basis for “activation” edges in the causal graph (RodA–PBP2 open state → active PG synthesis), which can be used to explain stable medium-width set-points in wild-type rods. (shlosman2023allostericactivationof pages 1-2)

#### B) 2023: Rod-complex integrity and interactions (RodZ, MreC/MreD) linked to PG architecture
In *E. coli*, RodZ is described as physically/genetically interacting with itself and major Rod components, forming a high molecular weight “superstructure” (hexamer dissociation) consistent with modular Rod-complex units. Perturbing RodZ (RMR chimera) yields abnormal morphology and PG with “many large holes,” while suppressors map to Rod components, consistent with restored complex activity/integrity. (ago2023relationshipbetweenthe pages 1-3)

#### C) 2023: aPBPs regulate diameter; moenomycin reveals hydrolase-driven rod collapse
In *M. xanthus*, aPBPs regulate cell diameter and mutant strains lacking aPBPs are “shorter and wider,” yet moenomycin inhibition causes rapid rod collapse via DacB pole degradation and altered DacB–PG binding/mobility. This supports a graph segment: moenomycin ⟶ inhibited aPBPs ⟶ increased DacB–PG binding/pole degradation ⟶ loss of rod shape (and width dysregulation). (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

#### D) 2024: Osmotic stress, K+ influx, and MreB remodeling as environmental modulators
In *Bacillus subtilis*, osmotic upshift releases MreB molecules from filaments, makes PG synthesis patterns less organized, and slows cell extension. The study reports that **potassium influx** after osmotic shock is required for MreB filament disassembly, consistent with a physical/ionic modulation of cytoskeletal control over wall synthesis. (dersch2024adaptationofbacillus pages 1-2)

#### E) 2024: Quantitative width homeostasis modeling (mechanical phase space)
A 2024 preprint provides quantitative width anchors for untreated rods (wmx ~0.74–0.75 µm) and proposes mechanistic control in terms of envelope **bending rigidity κ** and **surface tension γ**, including a threshold relation for well-regulated rod growth. It classifies regulated widths as wmx ≤ 0.83 µm and maps perturbations (e.g., A22, cephalexin) into a dysregulated regime with faster width growth. (kale2024mechanicsofe. pages 10-13)

### Current applications and real-world implementations
1. **Antibiotic mechanisms and antibiotic target discovery:** RodA–PBP2 and aPBPs are central antibiotic targets and mechanistic nodes; inhibition can drive width/shape changes, bulging, and rod-to-sphere transitions (e.g., β-lactams targeting PBPs; moenomycin targeting aPBPs). (zhang2023coordinatedpeptidoglycansynthases pages 1-2, micelli2023aconservedzincbinding pages 1-2)
2. **Morphology engineering / phenotype-driven screens:** Rod-complex integrity and accessory-factor function (RodZ/MreC/MreD) produce strong, scorable morphology phenotypes (abnormal widths, rounding, PG defects), enabling genetic suppressor screens and functional mapping. (ago2023relationshipbetweenthe pages 1-3)
3. **Biophysics-informed control and diagnostic phenotyping:** Mechanical modeling suggests measurable envelope parameters (κ, γ, pressure) can predict width regulation regimes and provide interpretable readouts of perturbation impact (e.g., A22 shifts cells toward a deregulated width regime). (kale2024mechanicsofe. pages 10-13)

### Expert interpretation and analysis (authority-weighted)
**Convergent interpretation across authoritative sources:**
- The most authoritative 2023 peer-reviewed sources (Nature Communications; PNAS) strongly support that **directed PG synthesis by SEDS–bPBP complexes (RodA–PBP2)** and their regulation by accessory proteins is central to bacterial shape control (shlosman2023allostericactivationof pages 1-2, micelli2023aconservedzincbinding pages 1-2).
- Recent work expands “width control” beyond only cytoskeletal guidance: **enzyme coordination (synthases vs hydrolases)** and **envelope mechanical properties** provide complementary causal layers that can shift cells out of the medium-width regime. (zhang2023coordinatedpeptidoglycansynthases pages 1-2, kale2024mechanicsofe. pages 10-13)
- Environmental conditions (osmotic stress, ion flux) can remodel MreB dynamics, plausibly coupling habitat stresses to width/shape outcomes via altered organization of wall synthesis. (dersch2024adaptationofbacillus pages 1-2)

### Relevant statistics and quantitative data (recent)
The following quantitative anchors are particularly relevant for defining and curating “medium width” and for separating regulated vs deregulated widening:

> Constant-width model benchmark: **w = 0.7 µm** fit poorly to untreated *E. coli* width dynamics (**R² = -0.62**). (kale2024mechanicsofe. pages 10-13)
>
> Linear-width model estimate: **wmin = 0.65 µm**. (kale2024mechanicsofe. pages 10-13)
>
> Untreated-cell width saturation estimate: **wmx ≈ 0.74–0.75 µm** (saturation model **0.75 µm**; logistic model **0.74 µm**). (kale2024mechanicsofe. pages 10-13)
>
> Regulated width regime: **Region 1 defined by wmx ≤ 0.83 µm**. (kale2024mechanicsofe. pages 10-13)
>
> Severe dysregulation/upper threshold reference: **maximum 1.3 µm**. (kale2024mechanicsofe. pages 10-13)
>
> Width growth rates across regimes: **~2 nm/min** in Region 1, **~4–7 nm/min** in Region 2, and **~7–18 nm/min** in Region 3. (kale2024mechanicsofe. pages 10-13)
>
> Mechanical threshold for well-regulated rod-width growth: **κ + 0.46γ ≥ 0.12**. (kale2024mechanicsofe. pages 10-13)
>
> Pressure estimates from model fitting: untreated growing cells had estimated **turgor pressure ≈ 0.15 MPa** and **growth pressure ≈ 0.4 MPa**. (kale2024mechanicsofe. pages 1-4)
>
> Bulging simulations/fit context: interior pressure differences (**Δpi**) were reported in the **0.2–0.5 MPa** range. (kale2024mechanicsofe. pages 1-4)


*Blockquote: This blockquote compiles the main quantitative values reported for rod-width homeostasis and dysregulation in recent mechanical modeling work on *E. coli*. It is useful for defining the numerical scope of the medium-width trait and for identifying quantitative thresholds relevant to curation.*

### Candidate nodes (grouped) for `cell_width_medium.yaml`
A curation-ready list of candidate nodes (with tentative grounding) is provided below.

| Node label | Node type | Suggested ontology grounding (CURIE if known; otherwise blank) | Role in width control | Key supporting citation IDs |
|---|---|---|---|---|
| **Genes / proteins** |  |  |  |  |
| MreB | protein | GO:0051015 | actin-like organizer of lateral wall synthesis and width homeostasis | (zhang2023coordinatedpeptidoglycansynthases pages 1-2, dersch2024adaptationofbacillus pages 1-2, ago2023relationshipbetweenthe pages 1-3) |
| RodA | protein |  | SEDS glycosyltransferase driving elongasome synthesis affecting diameter | (shlosman2023allostericactivationof pages 1-2, micelli2023aconservedzincbinding pages 1-2, middlemiss2023moleculartugofwarregulatesa pages 92-96) |
| PBP2 | protein |  | class B PBP transpeptidase for elongation and rod-width maintenance | (shlosman2023allostericactivationof pages 1-2, micelli2023aconservedzincbinding pages 1-2, ago2023relationshipbetweenthe pages 1-3) |
| RodZ | protein |  | scaffold/linker supporting Rod-complex integrity and MreB coupling | (dersch2024adaptationofbacillus pages 1-2, ago2023relationshipbetweenthe pages 1-3) |
| MreC | protein |  | activates/modulates PBP2 via conformational control | (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 1-2) |
| MreD | protein |  | modulates PBP2 activity through MreC/MreD balance | (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 1-2) |
| PBP1a2 | protein |  | aPBP whose inhibition promotes width/shape collapse via DacB | (zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| DacB (PBP4 family D-Ala-D-Ala endo/carboxypeptidase) | protein | EC:3.4.16.- | pole PG hydrolase that can collapse rod shape when misregulated | (zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| FtsI (PBP3) | protein |  | septal transpeptidase; inhibition contributes to bulging/width dysregulation | (kale2024mechanicsofe. pages 10-13) |
| **Complexes / modules** |  |  |  |  |
| Rod complex / elongasome | complex | GO:1990497 | core width-setting lateral PG synthesis machinery | (shlosman2023allostericactivationof pages 1-2, micelli2023aconservedzincbinding pages 1-2, ago2023relationshipbetweenthe pages 1-3) |
| RodA-PBP2 complex | complex |  | allosterically activated synthase coupling polymerization and crosslinking | (shlosman2023allostericactivationof pages 1-2) |
| aPBPs (class A PBPs) | complex |  | parallel PG synthases that regulate cell diameter | (zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| **Processes / functions** |  |  |  |  |
| peptidoglycan polymerization | process | GO:0009252 | glycan-strand synthesis contributing to rod width set-point | (shlosman2023allostericactivationof pages 1-2, micelli2023aconservedzincbinding pages 1-2) |
| peptidoglycan crosslinking | process | GO:0018149 | wall strengthening influencing diameter and shape stability | (shlosman2023allostericactivationof pages 1-2, ago2023relationshipbetweenthe pages 1-3) |
| peptidoglycan hydrolase activity | process | GO:0009253 | opening/remodeling wall; excess activity widens or collapses rods | (zhang2023coordinatedpeptidoglycansynthases pages 1-2, dersch2024adaptationofbacillus pages 1-2) |
| cell wall extension | process | GO:0042545 | growth process whose organization constrains width | (dersch2024adaptationofbacillus pages 1-2, kale2024mechanicsofe. pages 10-13) |
| **Physical / mechanical factors** |  |  |  |  |
| turgor pressure | measurement |  | inward-outward force balance opposing wall reinforcement | (kale2024mechanicsofe. pages 10-13) |
| envelope bending rigidity | measurement |  | dominant mechanical determinant of regulated width | (kale2024mechanicsofe. pages 10-13) |
| surface tension | measurement |  | secondary mechanical parameter shaping width regime | (kale2024mechanicsofe. pages 10-13) |
| **Environmental / experimental factors** |  |  |  |  |
| osmotic upshift / hyperosmotic stress | environmental factor | ENVO:01001405 | disassembles MreB and perturbs organized elongation | (dersch2024adaptationofbacillus pages 1-2) |
| potassium influx / K+ ions | environmental factor | CHEBI:29103 | required for osmotic-stress-induced MreB disassembly | (dersch2024adaptationofbacillus pages 1-2) |
| **Chemicals / inhibitors** |  |  |  |  |
| A22 | chemical |  | inhibits MreB polymerization causing rounding and width dysregulation | (kale2024mechanicsofe. pages 10-13) |
| moenomycin | chemical | CHEBI:75498 | inhibits aPBPs and triggers rapid rod-shape collapse | (zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| mecillinam | chemical | CHEBI:69944 | inhibits PBP2, perturbing elongation-based width control | (zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| cephalexin / FtsI inhibition | chemical | CHEBI:34832 | septation block promoting bulging when combined with MreB perturbation | (kale2024mechanicsofe. pages 10-13) |
| **Phenotypes / trait-adjacent outputs** |  |  |  |  |
| rod-to-sphere transition | phenotype |  | severe failure of rod-width maintenance | (micelli2023aconservedzincbinding pages 1-2, zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| regulated width regime (wmx ≤ 0.83 µm) | phenotype |  | model-defined stable width-control region | (kale2024mechanicsofe. pages 10-13) |
| cell width saturation (wmx ~0.74-0.75 µm) | phenotype |  | recent quantitative estimate of typical untreated rod width set-point | (kale2024mechanicsofe. pages 10-13) |


*Table: This table lists candidate entities for a TraitMech causal graph of medium cell width, grouped by node type. It highlights core Rod-complex components, physical factors, and perturbagens with direct evidence linking them to rod-width regulation or width dysregulation.*

### Evidence-backed candidate causal edges (triples)
The candidate mechanistic edges below are formatted for translation into TraitMech triples. Each includes a snippet and uncertainty notes.

| Subject (node) | Predicate | Object (node) | Evidence snippet (quote) | Reference (DOI + URL + pub month/year if available) | Notes/uncertainty |
|---|---|---|---|---|---|
| RodA-PBP2 complex | positively regulates | peptidoglycan polymerization and crosslinking during elongation | “RodA-PBP2… undergoes dynamic exchange between closed and open states. Structural opening couples the activation of polymerization and crosslinking and is essential in vivo.” (shlosman2023allostericactivationof pages 1-2) | 10.1038/s41467-023-39037-9 · https://doi.org/10.1038/s41467-023-39037-9 · Jun 2023 | Strong mechanistic edge for elongasome activation; effect on width is indirect via wall-growth control rather than width alone. |
| MreC | activates | PBP2 | “MreC also interacts with PBP2… and this interaction is thought to cause a structural change in PBP2 and stimulate peptidoglycan polymerization and crosslinking.” (ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385 · https://doi.org/10.1002/mbo3.1385 · Oct 2023 | Good curation candidate; “thought to” indicates partial inference from prior work summarized in this paper. |
| MreD | modulates activity of | PBP2 | “the balance between MreC and MreD determines the activity of PBP2.” (ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385 · https://doi.org/10.1002/mbo3.1385 · Oct 2023 | Mechanistically important but sign of effect depends on MreC:MreD balance; curate as modulatory, not simply positive/negative. |
| MreC-MreD interaction | stabilizes conformation compatible with activation of | PBP2 open/activated state | “loss of MreC and MreD can be rescued by mutations that stabilize PBP2's open (activated) state… the MreC–MreD interaction controls MreC conformation and stabilizes a geometry compatible with allosteric activation of PBP2.” (gilman2024mrecmredstructurereveals pages 1-2) | 10.1101/2024.10.08.617240 · https://doi.org/10.1101/2024.10.08.617240 · Oct 2024 | Preprint; high mechanistic relevance, but should be marked uncertain until peer-reviewed. |
| RodZ | interacts with | MreB/MreC/MreD/PBP2/RodA (Rod complex integrity) | “RodZ physically and genetically interacts with itself, MreB, MreC, MreD, PBP2, and RodA… RodZ interacts with all known major components of the Rod complex and therefore plays a key role in this complex.” (ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385 · https://doi.org/10.1002/mbo3.1385 · Oct 2023 | Strong interaction edge; width effect is indirect through Rod-complex integrity and localization. |
| Defective RodZ / reduced Rod complex integrity | causes | abnormal peptidoglycan structure and abnormal morphology | “The growth and morphology of RMR cells were abnormal… peptidoglycan purified from RMR cells had many large holes… suppressor mutations increase the integrity and/or the activity of the Rod complex.” (ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385 · https://doi.org/10.1002/mbo3.1385 · Oct 2023 | Good phenotype edge; width-specific consequence not always quantified. |
| Class A PBPs (aPBPs) | regulate | cell diameter / cell dimensions | “aPBPs… regulate cell diameter” and strains lacking aPBPs “were moderately, but significantly shorter and wider.” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | 10.1038/s41467-023-41082-3 · https://doi.org/10.1038/s41467-023-41082-3 · Sep 2023 | Strong direct relevance to width trait; taxon shown is Myxococcus xanthus. |
| Moenomycin | inhibits | aPBPs | “Moenomycin that inhibits a family of PG synthases known as Class-A penicillin-binding proteins (aPBPs)” and “specifically inhibits the GTase activity of aPBPs but does not affect RodA.” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | 10.1038/s41467-023-41082-3 · https://doi.org/10.1038/s41467-023-41082-3 · Sep 2023 | Strong chemical inhibition edge; useful experimental-factor node. |
| Moenomycin-inhibited PBP1a2 | promotes binding of | DacB to peptidoglycan | “inhibited PBP1a2… accelerates the degradation of cell poles by DacB” and “promotes the binding between DacB and PG and thus reduces the diffusion of DacB.” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | 10.1038/s41467-023-41082-3 · https://doi.org/10.1038/s41467-023-41082-3 · Sep 2023 | Strong causal edge in Myxococcus; likely assay/taxon specific. |
| DacB | degrades | cell poles / pole peptidoglycan | “DacB, a hydrolytic PG peptidase… collapses the rod shape of M. xanthus by degrading PG, especially at cell poles.” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | 10.1038/s41467-023-41082-3 · https://doi.org/10.1038/s41467-023-41082-3 · Sep 2023 | Strong morphogenesis edge; collapse of rod shape implies width dysregulation but not a medium-width set-point specifically. |
| A22 | inhibits polymerization of | MreB | “A22, an inhibitor of MreB polymerization” and “A22 dominates, inhibiting MreB polymerization.” (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13) | 10.1101/2024.11.22.624946 · https://doi.org/10.1101/2024.11.22.624946 · Nov 2024 | Preprint but widely consistent with prior field knowledge; useful assay perturbation. |
| MreB inhibition by A22 | causes | rounding / width dysregulation | “A22… causes rounding up of cells” and “the ellipsoidal cell morphology with A22 treatment is also consistent with the inhibition of MreB resulting in a loss of rod-shape.” (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13) | 10.1101/2024.11.22.624946 · https://doi.org/10.1101/2024.11.22.624946 · Nov 2024 | Strong phenotype edge; more about width dysregulation than stable medium width. |
| Adequate bending rigidity + surface tension of envelope | enables | regulated rod width regime | “cell widths are regulated in Region 1 (wmx ≤0.83 µm)” and “rod-shaped cell growth will be well regulated for a threshold relation… κ + 0.46γ ≥0.12.” (kale2024mechanicsofe. pages 10-13) | 10.1101/2024.11.22.624946 · https://doi.org/10.1101/2024.11.22.624946 · Nov 2024 | Mechanical/control-theory edge from a preprint model; useful but should be marked uncertain and model-based. |
| Osmotic upshift | causes | MreB filament disassembly | “In response to osmotic upshift, MreB molecules were released from filaments… and the peptidoglycan synthesis pattern became less organized, concomitant with slowed-down cell extension.” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309 · https://doi.org/10.3390/microorganisms12071309 · Jun 2024 | Strong stress-response edge; width consequence is indirect through altered elongation/wall synthesis organization. |
| Potassium influx after osmotic shock | required for | MreB filament disassembly | “mutant strains that prevent efficient potassium influx… show a failure to disassemble MreB filaments” and “potassium ions are known to negatively affect MreB polymerization in vitro.” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309 · https://doi.org/10.3390/microorganisms12071309 · Jun 2024 | Strong environmental/ionic-factor edge; indirect relevance to width homeostasis. |
| Altered RodA levels (depletion or overexpression) | increases | cell diameter | “the same cell widening affect was seen when RodA was either depleted or overexpressed” with medians 1.29 µm (100 nM IPTG), 1.10 µm (10 µM), and 1.23 µm (1 mM). (middlemiss2023moleculartugofwarregulatesa pages 92-96, middlemiss2023moleculartugofwarregulates pages 92-96) | Source text from 2023 thesis/manuscript context; no stable DOI in provided evidence | Useful quantitative edge, but source is not a peer-reviewed paper in provided context; curate cautiously or hold pending primary publication. |
| Higher aPBP:elongasome synthesis ratio | causes | wider cell diameter | “at low RodA expression levels… there is a higher aPBP to elongasome peptidoglycan ratio resulting in a wider cell.” (middlemiss2023moleculartugofwarregulatesa pages 92-96, middlemiss2023moleculartugofwarregulates pages 92-96) | Source text from 2023 thesis/manuscript context; no stable DOI in provided evidence | Explicit mechanistic hypothesis with direct width relevance, but currently speculative/non-peer-reviewed in provided context. |


*Table: This table compiles proposed mechanistic edges relevant to the microbial morphology trait ‘cell width medium,’ emphasizing Rod-complex control of rod diameter and width homeostasis. It is useful as a curation draft because it pairs each edge with a source-backed quote, citation details, and uncertainty notes.*

## Warnings / curation caveats (do not over-curate)
1. **Taxon specificity:** The aPBP–DacB–moenomycin mechanism is demonstrated in *Myxococcus xanthus* and may not generalize quantitatively to other rods; curate with explicit NCBITaxon constraints or mark uncertain. (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
2. **Preprint uncertainty:** The mechanical width-homeostasis model and the MreC–MreD structural activation model include preprint evidence; curate as provisional until peer-reviewed replication/validation. (kale2024mechanicsofe. pages 10-13, gilman2024mrecmredstructurereveals pages 1-2)
3. **Non-peer-reviewed RodA-level ↔ diameter quantitative claims:** The RodA induction vs diameter statistics are from an “unknown journal/unpublished” source in the retrieved corpus; do not curate quantitative width effects from this source as definitive without locating the peer-reviewed primary publication. (middlemiss2023moleculartugofwarregulatesa pages 92-96)
4. **Width vs shape collapse:** Many perturbations cause **loss of rod shape** (sphere/oval/bulging). These should not be conflated with “medium width” per se; treat them as transitions out of the medium-width state rather than causes of the medium-width phenotype. (zhang2023coordinatedpeptidoglycansynthases pages 1-2, micelli2023aconservedzincbinding pages 1-2, kale2024mechanicsofe. pages 10-13)

## DOI-first bibliography (with URLs and publication dates)

> 10.1038/s41467-023-39037-9 — Shlosman, Irina; Fivenson, Elayne M.; Gilman, Morgan S. A.; Sisley, Tyler A.; Walker, Suzanne; Bernhardt, Thomas G.; Kruse, Andrew C.; Loparo, Joseph J. *Allosteric activation of cell wall synthesis during bacterial growth*. **Nature Communications**. Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 1-2)
>
> 10.1038/s41467-023-41082-3 — Zhang, Huan; Venkatesan, Srutha; Ng, Emily; Nan, Beiyan. *Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall*. **Nature Communications**. Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3 (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
>
> 10.1002/mbo3.1385 — Ago, Risa; Tahara, Yuhei O.; Yamaguchi, Honoka; Saito, Motoya; Ito, Wakana; Yamasaki, Kaito; Kasai, Taishi; Okamoto, Sho; Chikada, Taiki; Oshima, Taku; Osaka, Issey; Miyata, Makoto; Niki, Hironori; Shiomi, Daisuke. *Relationship between the Rod complex and peptidoglycan structure in Escherichia coli*. **MicrobiologyOpen**. Oct 2023. URL: https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3)
>
> 10.1073/pnas.2215237120 — Micelli, Carmina; Dai, Yunfei; Raustad, Nicole; Isberg, Ralph R.; Dowson, Christopher G.; Lloyd, Adrian J.; Geisinger, Edward; Crow, Allister; Roper, David I. *A conserved zinc-binding site in Acinetobacter baumannii PBP2 required for elongasome-directed bacterial cell shape*. **Proceedings of the National Academy of Sciences of the United States of America**. Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2)
>
> 10.3390/microorganisms12071309 — Dersch, Simon; Graumann, Peter L. *Adaptation of Bacillus subtilis MreB Filaments to Osmotic Stress Depends on Influx of Potassium Ions*. **Microorganisms**. Jun 2024. URL: https://doi.org/10.3390/microorganisms12071309 (dersch2024adaptationofbacillus pages 1-2)
>
> 10.1101/2024.11.22.624946 — Kale, Tanvi; Dasgupta, Ryth; Inamdar, Mandar M.; Athale, Chaitanya A. *Mechanics of E. coli cell width homeostasis and bulging dynamics from MreB and septum inhibition*. **bioRxiv**. Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946 (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13)
>
> 10.1101/2024.10.08.617240 — Gilman, Morgan S. A.; Shlosman, Irina; Guerra, Daniel D. Samé; Domecillo, Masy; Fivenson, Elayne M.; Bourett, Claire; Bernhardt, Thomas G.; Polizzi, Nicholas F.; Loparo, Joseph J.; Kruse, Andrew C. *MreC-MreD structure reveals a multifaceted interface that controls MreC conformation*. **bioRxiv**. Oct 2024. URL: https://doi.org/10.1101/2024.10.08.617240 (gilman2024mrecmredstructurereveals pages 1-2)
>
> No DOI available — Middlemiss, S. A. *Molecular tug-of-war regulates Bacillus subtilis elongasome dynamics and bacterial cell shape*. **Unpublished / unknown journal**. 2023. URL: [blank] (middlemiss2023moleculartugofwarregulatesa pages 92-96, middlemiss2023moleculartugofwarregulates pages 19-23, middlemiss2023moleculartugofwarregulates pages 92-96)


*Blockquote: This blockquote lists the main primary sources used for the cell-width-medium curation report in DOI-first format. It is useful as a compact bibliography for downstream TraitMech curation and reference checking.*


References

1. (kale2024mechanicsofe. pages 10-13): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

2. (shlosman2023allostericactivationof pages 1-2): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

3. (zhang2023coordinatedpeptidoglycansynthases pages 1-2): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

4. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

5. (micelli2023aconservedzincbinding pages 1-2): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 21 citations and is from a highest quality peer-reviewed journal.

6. (gilman2024mrecmredstructurereveals pages 1-2): Morgan S.A. Gilman, Irina Shlosman, Daniel D. Samé Guerra, Masy Domecillo, Elayne M. Fivenson, Claire Bourett, Thomas G. Bernhardt, Nicholas F. Polizzi, Joseph J. Loparo, and Andrew C. Kruse. Mrec-mred structure reveals a multifaceted interface that controls mrec conformation. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.08.617240, doi:10.1101/2024.10.08.617240. This article has 2 citations.

7. (dersch2024adaptationofbacillus pages 1-2): Simon Dersch and Peter L. Graumann. Adaptation of bacillus subtilis mreb filaments to osmotic stress depends on influx of potassium ions. Microorganisms, 12:1309, Jun 2024. URL: https://doi.org/10.3390/microorganisms12071309, doi:10.3390/microorganisms12071309. This article has 5 citations.

8. (kale2024mechanicsofe. pages 1-4): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

9. (middlemiss2023moleculartugofwarregulatesa pages 92-96): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

10. (middlemiss2023moleculartugofwarregulates pages 92-96): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

11. (middlemiss2023moleculartugofwarregulates pages 19-23): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.