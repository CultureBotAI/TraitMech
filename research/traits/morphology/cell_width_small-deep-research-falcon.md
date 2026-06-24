---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:05:57.247851'
end_time: '2026-06-18T07:22:26.723370'
duration_seconds: 989.48
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width small
  trait_identifier: METPO:1000888
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_small
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension lies approximately
    between 0.5 and 0.65 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_0.5_0.65
  evidence_summary: "DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan\
    \ synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths\
    \ in the 0.5\u20130.65 \u03BCm range.)"
  causal_graph_summary: 'cell_width_small_mreb_setpoint: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width small
- **METPO identifier:** METPO:1000888
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.5 and 0.65 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.5_0.65
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths in the 0.5–0.65 μm range.)
- **Existing causal graph summary:** cell_width_small_mreb_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_small.yaml`.

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
- **Trait label:** cell width small
- **METPO identifier:** METPO:1000888
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension lies approximately between 0.5 and 0.65 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_0.5_0.65
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports the MreB/Rod-complex set-point producing narrow rod widths in the 0.5–0.65 μm range.)
- **Existing causal graph summary:** cell_width_small_mreb_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_small.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **cell width small** (METPO:1000888)

## 1) Scope summary (trait semantics and boundary cases)

**Trait definition (curation target).** *Cell width small* (METPO:1000888) is a **morphology** class describing rod/ovoid cells whose **shorter dimension (width/diameter)** lies approximately **0.5–0.65 µm**.

**Operationalization in experiments/assays.** In single-cell microscopy datasets/model fits for *E. coli*, fitted width parameters include **wmin ≈ 0.65 µm** (linear model), and typical widths around **0.7–0.75 µm** depending on the phenomenological model, supporting that **~0.65 µm** is a plausible lower bound for “small” rod width in common laboratory contexts (and motivating the METPO upper bound of 0.65 µm) (kale2024mechanicsofe. pages 27-29, kale2024mechanicsofe. pages 10-13).

**Nearby traits / boundary cases (must be excluded).**
- **Widening / increased diameter**: MreB perturbation produces markedly increased cell diameter (reported range ~**790 nm to 1700 nm** in *E. coli* across A22 treatment and point mutants), which is the opposite direction from the target trait and should be modeled as a negative/control state (ouzounov2016mreborientationcorrelates pages 1-2).
- **Bulging (local width excursions)**: in *B. subtilis* ΔmreB, peptidoglycan (PG) hydrolase activity becomes anisotropic “especially at sites of increased cell width and bulging,” a pathology distinct from a stable small-width setpoint (tesson2022magnesiumrescuesthe pages 1-2).

## 2) Current mechanistic understanding (key concepts and definitions)

### 2.1 Elongasome/Rod complex vs divisome
Recent primary literature provides concise, curatable definitions:
- The **Rod complex (elongasome)** uses **RodA–PBP2** with **MreCD and RodZ** (shlosman2023allostericactivationof pages 1-2).
- The **divisome** core is **FtsW–FtsI** with accessory factors (e.g., FtsQLB and FtsN) (shlosman2023allostericactivationof pages 1-2).

A recent *E. coli* study defines the **Rod complex** as a multi-protein machine controlling PG synthesis during **cell elongation**, listing key components **MreB, RodA, PBP2, RodZ, MreC, MreD**, and linking complex integrity to global PG architecture (holes, muropeptide composition) and morphology (ago2023relationshipbetweenthe pages 1-3).

### 2.2 Width control as a consequence of spatially patterned PG synthesis and remodeling
Two dominant (non-exclusive) causal themes recur across sources:
1. **Cytoskeletal guidance & geometry feedback**: MreB is described as a primary determinant of rod shape and diameter, with polymer orientation and curvature-sensing/localization linked to steady-state diameter (shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2).
2. **Coupled synthesis + controlled hydrolysis**: balanced PG synthase/hydrolase activities are required; in ΔmreB B. subtilis, increased endopeptidase activities correlate with bulging and width-loss pathology (tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2).

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Allosteric activation of RodA–PBP2 (2023)
A major 2023 advance is the mechanistic demonstration that **RodA–PBP2** toggles between **closed and open states**, where **opening activates and couples polymerization and crosslinking** (shlosman2023allostericactivationof pages 1-2). **MreC** is supported as an activator that favors the open (active) state; **PBP2 suppressor alleles** bypass defective MreC and increase polymerization activity, consistent with an activation-by-conformation model (shlosman2023allostericactivationof pages 6-7).

### 3.2 Rod complex integrity shapes peptidoglycan architecture (2023)
A 2023 MicrobiologyOpen study perturbs RodZ (RMR transmembrane chimera) and shows Rod-complex defects yield PG with larger/more numerous “holes” and altered muropeptides; suppressor mutations in **mreB/mreC/mreD/pbp2/rodA** restore morphology and PG structure, supporting a causal chain from Rod-complex integrity → PG architecture → cell shape/width phenotype (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 11-14).

### 3.3 Ion dependence of elongasome-directed shape (2023)
In *Acinetobacter baumannii*, a conserved **Zn2+-binding site in PBP2** is required for stability and rod morphology; disruption yields rod-to-sphere transitions and altered β-lactam susceptibility, suggesting **metal availability** can modulate shape through PBP2 integrity (micelli2023aconservedzincbinding pages 1-2).

### 3.4 Mechanics-focused modeling of width homeostasis and perturbation (2024 preprint)
A 2024 bioRxiv preprint quantifies *E. coli* width dynamics and models width as saturating rather than fixed, with fitted parameters including **wmin ~0.65–0.68 µm** and typical widths ~0.7–0.75 µm. It reports that **A22 (MreB inhibition)** and **cephalexin (septal inhibitor)** perturb width control and generate bulging phenotypes, linking mechanical parameters (e.g., envelope bending rigidity) to regulated vs deregulated width states (kale2024mechanicsofe. pages 10-13, kale2024mechanicsofe. pages 27-29).

## 4) Current applications and real-world implementations

### 4.1 Antibiotic mechanism-of-action and screening via morphology
- **A22** is used to disrupt MreB localization/polymerization and thereby probe the Rod-complex-dependent width setpoint and widening responses (shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2).
- **Mecillinam** sensitivity functions as a readout of RodA–PBP2 activation state; hyperactive/open-state variants increase sensitivity to sub-MIC mecillinam, enabling chemical-genetic interrogation of Rod-complex regulation (shlosman2023allostericactivationof pages 6-7).
- **Cephalexin** (a septal inhibitor) in combination with A22 produces bulging/diverse morphologies in *E. coli*, supporting combined perturbation designs to map elongation–division coupling (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13).

### 4.2 Environmental modulation of cell-wall remodeling (divalent cations)
Millimolar **Mg2+** is used experimentally to **rescue rod-shape/morphology** in *B. subtilis* mreB mutants by inhibiting PG hydrolases (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9). This is an actionable environmental lever for stabilizing morphology during genetic perturbations that otherwise cause width defects and lysis.

## 5) Statistics and quantitative data (recent studies)

- *E. coli* width parameter near the trait boundary: model fits include **wmin = 0.65 µm** (linear fit) and typical widths around **0.7–0.75 µm**, depending on model form (kale2024mechanicsofe. pages 27-29, kale2024mechanicsofe. pages 10-13).
- *E. coli* diameter range under MreB perturbation: reported steady-state diameters spanning ~**790 ± 30 nm** to **1700 ± 20 nm** across perturbations (A22, point mutants), illustrating the dynamic range of widening beyond the target trait class (ouzounov2016mreborientationcorrelates pages 1-2).
- *B. subtilis* rescue condition: ΔmreB cell wall mechanical properties “become indistinguishable from wild-type” in the presence of **25 mM Mg2+** (tesson2022magnesiumrescuesthe pages 8-9).

## 6) Candidate nodes (grouped by type; ontology grounding suggestions)

| Group | Candidate node label | Suggested grounding / CURIE | Node type | Curation note / role in small-width trait | Evidence |
|---|---|---|---|---|---|
| Trait/Phenotype | cell width small | METPO:1000888 | trait | Target morphology class: shorter cell dimension approximately 0.5–0.65 µm; distinct from generic rod shape, bulging, or filamentation | (kale2024mechanicsofe. pages 27-29, kale2024mechanicsofe. pages 10-13) |
| Trait/Phenotype | narrow rod cell width setpoint | label only | phenotype attribute | Useful intermediate phenotype node for graphing Rod-complex-dependent width homeostasis around low diameter values | (shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2, kale2024mechanicsofe. pages 27-29) |
| Trait/Phenotype | increased cell width / widening | label only | phenotype attribute | Boundary/contrast phenotype; often produced by A22, Rod-complex defects, or hydrolase imbalance | (kale2024mechanicsofe. pages 10-13, ouzounov2016mreborientationcorrelates pages 1-2, tesson2022magnesiumrescuesthe pages 1-2) |
| Trait/Phenotype | bulging sidewall | label only | morphology phenotype | Important boundary case: width dysregulation rather than stable small width | (kale2024mechanicsofe. pages 1-4, tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) |
| Cellular processes | peptidoglycan biosynthetic process | GO:0009252 | biological process | Core wall-building process determining rod width and shape | (galinier2023recentadvancesin pages 1-3, shlosman2023allostericactivationof pages 1-2) |
| Cellular processes | cell wall organization or biogenesis | GO:0071554 | biological process | High-level process linking synthesis/remodeling balance to maintained narrow width | (tesson2022magnesiumrescuesthe pages 1-2, galinier2023recentadvancesin pages 1-3) |
| Cellular processes | cell elongation | GO:0032989 | biological process | Width trait is coupled to elongasome-mediated sidewall elongation | (ago2023relationshipbetweenthe pages 1-3, costa2024theroleof pages 1-2) |
| Cellular processes | peptidoglycan polymerization | label only | biological process | RodA/FtsW SEDS polymerase-dependent glycan strand synthesis | (shlosman2023allostericactivationof pages 6-7, shlosman2023allostericactivationof pages 1-2) |
| Cellular processes | peptidoglycan transpeptidation | GO:0009253 | molecular function/process proxy | PBP2/FtsI/aPBP-mediated crosslinking contributes to width-supporting wall mechanics | (shlosman2023allostericactivationof pages 6-7, galinier2023recentadvancesin pages 1-3) |
| Cellular processes | peptidoglycan hydrolysis / autolysis | GO:0009253? | biological process | Balanced hydrolase activity required; excess sidewall hydrolysis causes widening/bulging | (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) |
| Cellular processes | sidewall peptidoglycan insertion | label only | cellular process | Spatially patterned lateral wall growth underlying diameter control | (shi2018howtobuild pages 6-7, ago2023relationshipbetweenthe pages 1-3) |
| Cellular processes | Rod-complex activation by conformational opening | label only | regulatory process | MreC/MreD/PBP2 conformational control is a strong mechanistic candidate upstream of width setpoint | (shlosman2023allostericactivationof pages 6-7, shlosman2023allostericactivationof pages 1-2) |
| Cellular processes | curvature sensing / curvature-guided wall synthesis | label only | cellular process | MreB orientation/localization couples geometry to width maintenance | (shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2) |
| Complexes | Rod complex / elongasome | GO:1990357? | protein complex | Central candidate complex setting rod diameter during elongation | (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 1-2) |
| Complexes | RodA–PBP2 complex | label only | protein complex | Core SEDS-bPBP synthase for elongation and width control in many Gram-negatives | (shlosman2023allostericactivationof pages 6-7, micelli2023aconservedzincbinding pages 1-2, shlosman2023allostericactivationof pages 1-2) |
| Complexes | MreB-associated elongasome superstructure | label only | protein complex | Includes MreB, RodZ, MreC, MreD and synthases; candidate graph node when subunit resolution is unnecessary | (ago2023relationshipbetweenthe pages 1-3) |
| Complexes | divisome | GO:1902493 | protein complex | Contrast/comparator complex; septal synthesis interacts with width phenotypes under perturbation | (costa2024theroleof pages 1-2, shlosman2023allostericactivationof pages 1-2) |
| Complexes | FtsW–FtsI complex | label only | protein complex | Septal SEDS-bPBP counterpart to RodA–PBP2; useful comparator/inhibitor target node | (shlosman2023allostericactivationof pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | MreB | gene/protein label | cytoskeletal protein | Primary actin-like determinant of rod width/orientation of wall insertion | (shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | RodA | gene/protein label | SEDS glycosyltransferase | Core elongation polymerase in Rod complex | (ago2023relationshipbetweenthe pages 1-3, micelli2023aconservedzincbinding pages 1-2, shlosman2023allostericactivationof pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | PBP2 / MrdA | gene/protein label | class B PBP transpeptidase | Core elongation transpeptidase; activity/state linked to width control | (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 6-7, micelli2023aconservedzincbinding pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | MreC | gene/protein label | periplasmic/accessory Rod protein | Activates or promotes open state of PBP2; key upstream regulator | (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 6-7) |
| Genes/Proteins (Gram-negative Rod complex) | MreD | gene/protein label | membrane/accessory Rod protein | Controls MreC conformation and Rod-complex activation | (ago2023relationshipbetweenthe pages 1-3, shlosman2023allostericactivationof pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | RodZ | gene/protein label | membrane linker protein | Bridges MreB with periplasmic Rod components; required for Rod-complex integrity | (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 1-3) |
| Genes/Proteins (Gram-negative Rod complex) | FtsW | gene/protein label | SEDS glycosyltransferase | Divisome comparator; included because septal inhibition affects width/bulging states | (shlosman2023allostericactivationof pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | FtsI / PBP3 | gene/protein label | class B PBP transpeptidase | Septal comparator; cephalexin target used in width/bulging perturbation studies | (kale2024mechanicsofe. pages 1-4, shlosman2023allostericactivationof pages 1-2) |
| Genes/Proteins (Gram-negative Rod complex) | FtsZ | gene/protein label | tubulin-like cytoskeletal protein | Division protein interacting genetically/physiologically with width tolerance | (shi2018howtobuild pages 7-9, costa2024theroleof pages 1-2) |
| Genes/Proteins (Gram-positive Rod system variants) | Mbl | gene/protein label | MreB-family actin homolog | Bacillus subtilis width/elongation determinant paralog; useful taxon-specific node | (tesson2022magnesiumrescuesthe pages 2-3, middlemiss2023moleculartugofwarregulates pages 19-23) |
| Genes/Proteins (Gram-positive Rod system variants) | MreBH | gene/protein label | MreB-family actin homolog | Bacillus subtilis paralog with sidewall/autolysin-related functions | (tesson2022magnesiumrescuesthe pages 2-3, middlemiss2023moleculartugofwarregulates pages 19-23) |
| Genes/Proteins (Gram-positive Rod system variants) | PBPH | gene/protein label | class B PBP | Gram-positive elongation transpeptidase variant | (middlemiss2023moleculartugofwarregulatesa pages 19-23, middlemiss2023moleculartugofwarregulates pages 19-23) |
| Genes/Proteins (Gram-positive Rod system variants) | PBP2A | gene/protein label | class B PBP | Gram-positive elongation transpeptidase variant | (middlemiss2023moleculartugofwarregulatesa pages 19-23, middlemiss2023moleculartugofwarregulates pages 19-23) |
| Genes/Proteins (Gram-positive Rod system variants) | class A PBPs (aPBPs) | label only | enzyme family | Parallel PG synthesis system affecting wall robustness and shape, often not direct width setpoint node | (galinier2023recentadvancesin pages 15-16, costa2024theroleof pages 1-2) |
| Genes/Proteins (Gram-positive Rod system variants) | LytE | gene/protein label | DL-endopeptidase/autolysin | Sidewall hydrolase linked to MreB-family function and Mg2+-sensitive morphology rescue | (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9) |
| Genes/Proteins (Gram-positive Rod system variants) | CwlO | gene/protein label | DL-endopeptidase/autolysin | Co-essential sidewall hydrolase relevant to width homeostasis in Bacillus | (tesson2022magnesiumrescuesthe pages 2-3) |
| Enzymes and pathways | peptidoglycan precursor synthesis pathway | label only | pathway | Upstream pathway generating lipid II substrate for width-setting wall growth | (galinier2023recentadvancesin pages 1-3) |
| Enzymes and pathways | MraY | gene/protein label | phospho-MurNAc-pentapeptide transferase | Produces lipid I in precursor pathway | (galinier2023recentadvancesin pages 1-3) |
| Enzymes and pathways | MurG | gene/protein label | glycosyltransferase | Converts lipid I to lipid II | (galinier2023recentadvancesin pages 1-3) |
| Enzymes and pathways | MurJ | gene/protein label | lipid II flippase | Flips lipid II across membrane for PG synthesis | (galinier2023recentadvancesin pages 1-3, middlemiss2023moleculartugofwarregulates pages 19-23) |
| Enzymes and pathways | lipid II | CHEBI:2441 | metabolite | Immediate PG precursor consumed by Rod/divisome synthases | (galinier2023recentadvancesin pages 1-3) |
| Enzymes and pathways | undecaprenyl phosphate cycle / lipid carrier cycle | label only | pathway | Supports precursor trafficking for wall synthesis | (galinier2023recentadvancesin pages 1-3) |
| Enzymes and pathways | DL-endopeptidase activity | label only | enzymatic activity | Elevated in mreB mutants; associated with widening/bulging | (tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) |
| Enzymes and pathways | DD-endopeptidase activity | label only | enzymatic activity | Also elevated in mreB mutants; part of dysregulated hydrolase state | (tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) |
| Environmental/Experimental factors | excess extracellular magnesium condition | ENVO:01000324? | environmental condition | Experimental condition rescuing shape defects and suppressing hydrolase-driven width loss | (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9) |
| Environmental/Experimental factors | zinc starvation | label only | experimental condition | Perturbs PBP2 stability/function in A. baumannii and causes rod-to-sphere transition | (micelli2023aconservedzincbinding pages 1-2) |
| Environmental/Experimental factors | sublethal cell-wall synthesis inhibition | label only | experimental factor | Produces widening and probes width homeostasis | (shi2018howtobuild pages 7-9) |
| Environmental/Experimental factors | MreB inhibition | label only | experimental factor | Direct perturbation causing loss of width control and rod shape | (kale2024mechanicsofe. pages 10-13, shi2018howtobuild pages 6-7) |
| Environmental/Experimental factors | septal synthesis inhibition | label only | experimental factor | Used with MreB perturbation to generate bulging and altered width dynamics | (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13) |
| Chemicals/Inhibitors | A22 | CHEBI:131704 | small-molecule inhibitor | MreB polymerization inhibitor; canonical widening/shape-loss perturbagen | (kale2024mechanicsofe. pages 10-13, shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2) |
| Chemicals/Inhibitors | mecillinam | CHEBI:6993 | beta-lactam antibiotic | PBP2-targeting probe; altered sensitivity tracks Rod-complex activation/state | (ago2023relationshipbetweenthe pages 11-14, shlosman2023allostericactivationof pages 6-7) |
| Chemicals/Inhibitors | cephalexin | CHEBI:3487 | beta-lactam antibiotic | FtsI/PBP3-targeting probe causing filamentation/bulging in width mechanics studies | (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13) |
| Ions/Metals | magnesium(2+) | CHEBI:18420 | divalent cation | Strong candidate environmental modulator; inhibits hydrolase-driven width loss/bulging and rescues rod shape | (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) |
| Ions/Metals | zinc(2+) | CHEBI:29105 | divalent cation | Supports PBP2 structural integrity in A. baumannii elongasome-directed shape control | (micelli2023aconservedzincbinding pages 1-2) |
| Ions/Metals | calcium(2+) | CHEBI:29108 | divalent cation | Similar protective effect to Mg2+ against LytE/lysozyme lysis; secondary candidate | (tesson2022magnesiumrescuesthe pages 8-9) |


*Table: This table lists curation-ready candidate nodes for a TraitMech graph of the microbial morphology trait 'cell width small' (0.5–0.65 µm). It groups evidence-backed molecular, process, pathway, and environmental nodes relevant to width homeostasis, widening, and rescue phenotypes.*

## 7) Evidence-backed candidate causal edges (triples) for TraitMech curation

| Edge (S–P–O) | Direction | Taxon scope | Evidence snippet | Reference (DOI, year, URL) | Evidence strength | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| MreC – activates – RodA–PBP2 open conformation | activates | *Escherichia coli* / conserved Rod complex | “MreC favors the open, active PBP2 state; PBP2 suppressor alleles bypass defective MreC and increase polymerization activity.” (shlosman2023allostericactivationof pages 6-7, shlosman2023allostericactivationof pages 1-2) | 10.1038/s41467-023-39037-9, 2023, https://doi.org/10.1038/s41467-023-39037-9 | strong | Best-supported activation edge for Rod-complex control; mechanistic and structural. |
| RodA–PBP2 open conformation – increases – peptidoglycan polymerization/crosslinking | increases | *E. coli* / conserved SEDS-bPBP systems | “Structural opening couples activation of polymerization and crosslinking; open-state mutants show stronger polymerization.” (shlosman2023allostericactivationof pages 6-7, shlosman2023allostericactivationof pages 1-2) | 10.1038/s41467-023-39037-9, 2023, https://doi.org/10.1038/s41467-023-39037-9 | strong | Useful intermediate process edge linking conformation to output. |
| RodZ – bridges – MreB and periplasmic Rod components | required_for | *E. coli* | “RodZ interacts with MreB cytoplasmically and with MreC/MreD/PBP2 periplasmically, supporting a bridging role in the Rod complex.” (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | strong | Curate as physical/organizational link rather than direct enzymatic activation. |
| RodZ integrity – increases – Rod complex integrity/activity | increases | *E. coli* | “RodZ mutant RMR lowered Rod-complex activity, causing slow growth, abnormal shape, and defective peptidoglycan.” (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 1-3) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | strong | Good causal path to morphology, though width-specific output is indirect. |
| Suppressor mutations in MreB/MreC/MreD/PBP2/RodA – increase – Rod complex integrity/activity | increases | *E. coli* | “Suppressors in Rod components restored growth/rod shape and re-established Rod-complex assembly, consistent with increased integrity or activity.” (ago2023relationshipbetweenthe pages 1-3, ago2023relationshipbetweenthe pages 11-14) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | strong | Mutation-class node is broad but well supported. |
| Increased Rod complex integrity/activity – restores – normal peptidoglycan architecture | causes | *E. coli* | “Suppressors restored PG structure toward normal; defective RMR complexes produced PG with larger/more numerous holes.” (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 11-14) | 10.1002/mbo3.1385, 2023, https://doi.org/10.1002/mbo3.1385 | strong | Supports mechanism from Rod complex to wall architecture. |
| MreB – required_for – stable rod width/diameter control | required_for | Rod-shaped bacteria, especially *E. coli* | “MreB is a key determinant of rod shape and diameter; perturbing MreB changes steady-state diameter and width control.” (shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2) | 10.1016/j.cell.2018.02.050, 2018, https://doi.org/10.1016/j.cell.2018.02.050; 10.1016/j.bpj.2016.07.017, 2016, https://doi.org/10.1016/j.bpj.2016.07.017 | strong | Broad, foundational edge; closest to existing graph summary. |
| A22 – inhibits – MreB polymerization/localization | inhibits | Rod-shaped bacteria, especially *E. coli* | “A22 disrupts MreB localization/polymerization, breaking MreB–shape feedback.” (kale2024mechanicsofe. pages 10-13, shi2018howtobuild pages 6-7, ouzounov2016mreborientationcorrelates pages 1-2) | 10.1016/j.cell.2018.02.050, 2018, https://doi.org/10.1016/j.cell.2018.02.050; 10.1016/j.bpj.2016.07.017, 2016, https://doi.org/10.1016/j.bpj.2016.07.017 | strong | Canonical perturbation edge. |
| A22-mediated MreB inhibition – increases – cell diameter/width | increases | *E. coli* | “Chemical MreB perturbation substantially altered steady-state diameter, with reported range from ~790 nm to ~1700 nm.” (ouzounov2016mreborientationcorrelates pages 1-2) | 10.1016/j.bpj.2016.07.017, 2016, https://doi.org/10.1016/j.bpj.2016.07.017 | strong | Strong widening edge; opposite of target trait, useful as contrast/boundary. |
| Increased DL-endopeptidase activity – causes – sidewall bulging / increased width sites | causes | *Bacillus subtilis* ΔmreB | “ΔmreB cells showed anisotropic hydrolase activity especially at sites of increased cell width and bulging.” (tesson2022magnesiumrescuesthe pages 1-2) | 10.1038/s41598-021-04294-5, 2022, https://doi.org/10.1038/s41598-021-04294-5 | strong | Very relevant negative edge: hydrolase excess drives widening, not small width. |
| Increased DD-endopeptidase activity – contributes to – wall dysregulation/widening in ΔmreB | increases | *B. subtilis* ΔmreB | “ΔmreB cells had altered PG composition consistent with increased DL- and DD-endopeptidase activities and width/bulging defects.” (tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) | 10.1038/s41598-021-04294-5, 2022, https://doi.org/10.1038/s41598-021-04294-5 | moderate | Contribution to widening is supported, but direct DD-endopeptidase-to-width causality is less isolated than for DL-endopeptidase. |
| Mg2+ – inhibits – peptidoglycan hydrolase activity | inhibits | *B. subtilis* | “Exogenous Mg2+ inhibits autolysins/CW hydrolases and compensates increased DL-endopeptidase activity.” (tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2) | 10.1038/s41598-021-04294-5, 2022, https://doi.org/10.1038/s41598-021-04294-5 | strong | One of the clearest environmental modifier edges. |
| Mg2+ – decreases – bulging / width loss in ΔmreB | decreases | *B. subtilis* ΔmreB | “Millimolar Mg2+ rescues morphology and prevents lysis; ΔmreB wall properties become indistinguishable from wild type at 25 mM Mg2+.” (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9) | 10.1038/s41598-021-04294-5, 2022, https://doi.org/10.1038/s41598-021-04294-5 | strong | Rescue edge is robust, though it restores rod shape rather than directly specifying ‘small’ width. |
| Mg2+ – causes – rescue of rod shape in mreB mutants | causes | *B. subtilis* ΔmreB | “5–25 mM Mg2+ allows mreB mutants to maintain rod shape and avoid lysis.” (tesson2022magnesiumrescuesthe pages 2-3) | 10.1038/s41598-021-04294-5, 2022, https://doi.org/10.1038/s41598-021-04294-5 | strong | Useful environmental rescue edge; may be curated as context-specific. |
| Zn2+ binding to PBP2 – required_for – PBP2 stability / rod shape | required_for | *Acinetobacter baumannii* | “A conserved Zn-binding site in PBP2 is required for complementation, protein stability, and elongasome-directed rod shape.” (micelli2023aconservedzincbinding pages 1-2) | 10.1073/pnas.2215237120, 2023, https://doi.org/10.1073/pnas.2215237120 | strong | Strong but taxon-specific; likely not universal across bacteria. |
| Hyperactive/open RodA–PBP2 – increases – mecillinam sensitivity | increases | *E. coli* | “Open-state/hyperactive RodA–PBP2 mutants show increased sensitivity to sub-MIC mecillinam.” (shlosman2023allostericactivationof pages 6-7) | 10.1038/s41467-023-39037-9, 2023, https://doi.org/10.1038/s41467-023-39037-9 | strong | Good assay edge for Rod-complex activation; not directly a morphology edge. |
| Cephalexin (PBP3/FtsI inhibition) – causes – filamentation | causes | *E. coli* | “Cephalexin, a septum inhibitor, causes filamentation.” (kale2024mechanicsofe. pages 10-13) | 10.1101/2024.11.22.624946, 2024, https://doi.org/10.1101/2024.11.22.624946 | moderate | Preprint evidence; useful as perturbation/background condition. |
| Cephalexin + A22 – causes – bulging / diverse widened morphologies | causes | *E. coli* | “Combined septal inhibition and MreB inhibition yields bulging and diverse morphologies, indicating loss of width regulation.” (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13) | 10.1101/2024.11.22.624946, 2024, https://doi.org/10.1101/2024.11.22.624946 | moderate | Preprint and combinatorial perturbation; curate as experimental-factor edge, not baseline mechanism. |


*Table: This table lists evidence-backed subject–predicate–object edges relevant to curating a TraitMech graph for the 'cell width small' phenotype. It prioritizes mechanistically specific Rod-complex, MreB, hydrolase, and ion-modulation edges, while flagging taxon-specific or perturbation-specific claims.*

## 8) Bibliography (DOI-first; includes publication dates and URLs)

**2024**
- Kale T, Dasgupta R, Inamdar MM, Athale CA. *Mechanics of E. coli cell width homeostasis and bulging dynamics from MreB and septum inhibition.* bioRxiv (posted Nov 2024). DOI: **10.1101/2024.11.22.624946**. https://doi.org/10.1101/2024.11.22.624946 (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13, kale2024mechanicsofe. pages 27-29)
- Costa SF et al. *The role of GpsB in Staphylococcus aureus cell morphogenesis.* mBio (Mar 2024). DOI: **10.1128/mbio.03235-23**. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)

**2023**
- Shlosman I et al. *Allosteric activation of cell wall synthesis during bacterial growth.* Nature Communications (Jun 2023). DOI: **10.1038/s41467-023-39037-9**. https://doi.org/10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 6-7, shlosman2023allostericactivationof pages 1-2)
- Ago R et al. *Relationship between the Rod complex and peptidoglycan structure in Escherichia coli.* MicrobiologyOpen (Oct 2023). DOI: **10.1002/mbo3.1385**. https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 1-3, ago2023relationshipbetweenthe pages 11-14)
- Micelli C et al. *A conserved zinc-binding site in Acinetobacter baumannii PBP2 required for elongasome-directed bacterial cell shape.* PNAS (Feb 2023). DOI: **10.1073/pnas.2215237120**. https://doi.org/10.1073/pnas.2215237120 (micelli2023aconservedzincbinding pages 1-2)
- Galinier A et al. *Recent Advances in Peptidoglycan Synthesis and Regulation in Bacteria.* Biomolecules (Apr 2023). DOI: **10.3390/biom13050720**. https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 1-3, galinier2023recentadvancesin pages 15-16)
- Jain P. *Understanding Elongasome Unit of Mycobacterium and its Comparative Analysis with Other Model Organisms.* Journal of Cellular Signaling (Sep 2023). DOI: **10.33696/signaling.4.101**. https://doi.org/10.33696/signaling.4.101 (jain2023understandingelongasomeunit pages 2-4, jain2023understandingelongasomeunit pages 5-7)

**2022**
- Tesson B et al. *Magnesium rescues the morphology of Bacillus subtilis mreB mutants through its inhibitory effect on peptidoglycan hydrolases.* Scientific Reports (Jan 2022). DOI: **10.1038/s41598-021-04294-5**. https://doi.org/10.1038/s41598-021-04294-5 (tesson2022magnesiumrescuesthe pages 2-3, tesson2022magnesiumrescuesthe pages 8-9, tesson2022magnesiumrescuesthe pages 1-2)

**Foundational (context for MreB/width regulation)**
- Shi H et al. *How to Build a Bacterial Cell: MreB as the Foreman of E. coli Construction.* Cell (Mar 2018). DOI: **10.1016/j.cell.2018.02.050**. https://doi.org/10.1016/j.cell.2018.02.050 (shi2018howtobuild pages 6-7, shi2018howtobuild pages 7-9)
- Ouzounov N et al. *MreB Orientation Correlates with Cell Diameter in Escherichia coli.* Biophysical Journal (Sep 2016). DOI: **10.1016/j.bpj.2016.07.017**. https://doi.org/10.1016/j.bpj.2016.07.017 (ouzounov2016mreborientationcorrelates pages 1-2)

## 9) Warnings / “do not yet curate” notes

1. **Direct causation of “small width (0.5–0.65 µm)” by a specific Rod-complex allele set is not yet explicitly demonstrated in the provided evidence**; most sources show mechanisms of *width control* or *widening* under perturbation, and one recent preprint provides ~0.65 µm as a fitted lower bound in an *E. coli* dataset/model. Curating an edge like “RodA–PBP2 activity → cell width small” should therefore be marked **inferred** unless supported by a source directly mapping that activity to widths in the 0.5–0.65 µm band.
2. **Cephalexin/A22 combinatorial bulging and mechanical parameter thresholds** come from a 2024 preprint and should be labeled **uncertain/preprint** if curated (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13).
3. **Zn2+→PBP2 stability→rod shape** is strong but likely **taxon-specific** to *A. baumannii* PBP2 Zn-binding; avoid generalizing across bacteria without cross-taxon evidence (micelli2023aconservedzincbinding pages 1-2).


References

1. (kale2024mechanicsofe. pages 27-29): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

2. (kale2024mechanicsofe. pages 10-13): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

3. (ouzounov2016mreborientationcorrelates pages 1-2): Nikolay Ouzounov, Jeffrey P. Nguyen, Benjamin P. Bratton, David Jacobowitz, Zemer Gitai, and Joshua W. Shaevitz. Mreb orientation correlates with cell diameter in escherichia coli. Biophysical journal, 111 5:1035-43, Sep 2016. URL: https://doi.org/10.1016/j.bpj.2016.07.017, doi:10.1016/j.bpj.2016.07.017. This article has 114 citations and is from a domain leading peer-reviewed journal.

4. (tesson2022magnesiumrescuesthe pages 1-2): Benoit Tesson, Alex Dajkovic, Ruth Keary, Christian Marlière, Christine C. Dupont-Gillain, and Rut Carballido-López. Magnesium rescues the morphology of bacillus subtilis mreb mutants through its inhibitory effect on peptidoglycan hydrolases. Scientific Reports, Jan 2022. URL: https://doi.org/10.1038/s41598-021-04294-5, doi:10.1038/s41598-021-04294-5. This article has 34 citations and is from a peer-reviewed journal.

5. (shlosman2023allostericactivationof pages 1-2): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

6. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

7. (shi2018howtobuild pages 6-7): Handuo Shi, Benjamin P. Bratton, Zemer Gitai, and Kerwyn Casey Huang. How to build a bacterial cell: mreb as the foreman of e. coli construction. Cell, 172:1294-1305, Mar 2018. URL: https://doi.org/10.1016/j.cell.2018.02.050, doi:10.1016/j.cell.2018.02.050. This article has 220 citations and is from a highest quality peer-reviewed journal.

8. (tesson2022magnesiumrescuesthe pages 8-9): Benoit Tesson, Alex Dajkovic, Ruth Keary, Christian Marlière, Christine C. Dupont-Gillain, and Rut Carballido-López. Magnesium rescues the morphology of bacillus subtilis mreb mutants through its inhibitory effect on peptidoglycan hydrolases. Scientific Reports, Jan 2022. URL: https://doi.org/10.1038/s41598-021-04294-5, doi:10.1038/s41598-021-04294-5. This article has 34 citations and is from a peer-reviewed journal.

9. (shlosman2023allostericactivationof pages 6-7): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

10. (ago2023relationshipbetweenthe pages 14-16): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

11. (ago2023relationshipbetweenthe pages 11-14): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 15 citations and is from a peer-reviewed journal.

12. (micelli2023aconservedzincbinding pages 1-2): Carmina Micelli, Yunfei Dai, Nicole Raustad, Ralph R. Isberg, Christopher G. Dowson, Adrian J. Lloyd, Edward Geisinger, Allister Crow, and David I. Roper. A conserved zinc-binding site in acinetobacter baumannii pbp2 required for elongasome-directed bacterial cell shape. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2215237120, doi:10.1073/pnas.2215237120. This article has 21 citations and is from a highest quality peer-reviewed journal.

13. (kale2024mechanicsofe. pages 1-4): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

14. (tesson2022magnesiumrescuesthe pages 2-3): Benoit Tesson, Alex Dajkovic, Ruth Keary, Christian Marlière, Christine C. Dupont-Gillain, and Rut Carballido-López. Magnesium rescues the morphology of bacillus subtilis mreb mutants through its inhibitory effect on peptidoglycan hydrolases. Scientific Reports, Jan 2022. URL: https://doi.org/10.1038/s41598-021-04294-5, doi:10.1038/s41598-021-04294-5. This article has 34 citations and is from a peer-reviewed journal.

15. (galinier2023recentadvancesin pages 1-3): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.

16. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

17. (shi2018howtobuild pages 7-9): Handuo Shi, Benjamin P. Bratton, Zemer Gitai, and Kerwyn Casey Huang. How to build a bacterial cell: mreb as the foreman of e. coli construction. Cell, 172:1294-1305, Mar 2018. URL: https://doi.org/10.1016/j.cell.2018.02.050, doi:10.1016/j.cell.2018.02.050. This article has 220 citations and is from a highest quality peer-reviewed journal.

18. (middlemiss2023moleculartugofwarregulates pages 19-23): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

19. (middlemiss2023moleculartugofwarregulatesa pages 19-23): SA Middlemiss. Molecular tug-of-war regulates bacillus subtilis elongasome dynamics and bacterial cell shape. Unknown journal, 2023.

20. (galinier2023recentadvancesin pages 15-16): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 68 citations.

21. (jain2023understandingelongasomeunit pages 2-4): Preeti Jain. Understanding elongasome unit of mycobacterium and its comparative analysis with other model organisms. Journal of Cellular Signaling, 4:142-150, Sep 2023. URL: https://doi.org/10.33696/signaling.4.101, doi:10.33696/signaling.4.101. This article has 0 citations.

22. (jain2023understandingelongasomeunit pages 5-7): Preeti Jain. Understanding elongasome unit of mycobacterium and its comparative analysis with other model organisms. Journal of Cellular Signaling, 4:142-150, Sep 2023. URL: https://doi.org/10.33696/signaling.4.101, doi:10.33696/signaling.4.101. This article has 0 citations.