---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:55:23.718450'
end_time: '2026-08-04T15:05:59.791386'
duration_seconds: 636.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: bacillus shaped
  trait_identifier: METPO:1000667
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: bacillus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape characterized by an elongated, rod cylindrical morphology
    with relatively parallel sides and rounded ends.
  parent_traits: METPO:1000666
  synonyms: bacillus
  evidence_summary: 'DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape
    formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)'
  causal_graph_summary: 'bacillus_shaped_rod_elongation: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** bacillus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000667
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an elongated, rod cylindrical morphology with relatively parallel sides and rounded ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** bacillus
- **Existing evidence:** DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)
- **Existing causal graph summary:** bacillus_shaped_rod_elongation: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **bacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/bacillus_shaped.yaml`.

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
- **Trait label:** bacillus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000667
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an elongated, rod cylindrical morphology with relatively parallel sides and rounded ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** bacillus
- **Existing evidence:** DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)
- **Existing causal graph summary:** bacillus_shaped_rod_elongation: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **bacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/bacillus_shaped.yaml`.

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


# Curation report: bacillus-shaped morphology

## Trait record and scope

- **Trait:** bacillus shaped
- **Identifier:** **“METPO:1000667”**
- **Category/kind/status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000666
- **Operational meaning:** a single microbial cell with an elongated cylindrical body, approximately parallel lateral sides, and rounded ends. Here, **bacillus** denotes morphology, not membership in the genus *Bacillus*.

The trait should be assigned from an observed cell-shape phenotype, ideally during a specified growth phase and condition. It is not itself a physiological capacity or growth preference. In canonical bacteria, rod shape is propagated as the peptidoglycan (PG) sacculus expands: the Rod complex directs lateral PG insertion, whereas the divisome makes septal wall. A 2023 review states that the elongasome directs lateral insertion “along the long axis, enabling cylindrical growth,” with RodA and FtsW supporting elongation and division, respectively (galinier2023recentadvancesin pages 3-5).

### Boundaries

- **Include:** straight rods and ordinary rod-length variants whose sides remain approximately parallel.
- **Curved rods:** retain rod architecture but may merit an additional curvature trait; curvature-specific modules such as CrvA, crescentin, or porin–PapS should not define the generic bacillus-shaped graph.
- **Coccobacilli/ovococci:** borderline where length-to-width ratio and parallel sidewalls are weak; require an explicit assay rule.
- **Filaments:** elongated rods without normal septation should additionally receive a filamentous phenotype; filamentation is not equivalent to ordinary bacillus shape.
- **Spheres, disks, L-forms, and pleomorphic cells:** exclude unless documenting a transition into or out of the rod state. Wall-deficient *Vibrio cholerae* spheroplasts lose rod organization and later regenerate branches of normal rod diameter, making this a useful regeneration assay rather than a constitutive trait (goudin2023recoveryofvibrio pages 1-2).
- **Archaeal rods:** phenotypically in scope but mechanistically separate. *Haloferax volcanii* lacks bacterial PG and changes between rods and disks according to growth phase and swimming state; bacterial elongasome edges must not be projected onto it (schiller2024identificationofstructural pages 1-2).
- **Noncanonical bacterial rods:** some Rhizobiales produce rods through unipolar growth without the standard MreB-mediated dispersed-growth program (williams2019mechanismsofpolar pages 57-61).

## Current mechanistic model

The strongest general model is **distributed envelope synthesis plus mechanical feedback**, not “MreB alone specifies a cylinder.” MreB filaments orient active Rod complexes approximately around the circumference; RodA polymerizes glycan and PBP2 cross-links peptide stems. This yields anisotropic sidewall expansion while septal synthesis closes and rounds the ends. MreC, MreD, RodZ, hydrolases, aPBPs, precursor supply, and envelope mechanics regulate this core process (fivenson2023arolefor pages 1-2, galinier2023recentadvancesin pages 3-5).

Recent work expands the model beyond PG alone. In Gram-negative *E. coli*, strengthening the outer membrane rescued growth and rod-shape defects of hypomorphic Rod-complex mutants and restored proper orientation of MreB-directed synthesis. Thus, rod propagation depends on the mechanical state of the whole envelope, although this result is taxon-specific (fivenson2023arolefor pages 1-2, fivenson2023arolefor media 0289c886).

## Candidate nodes grouped by type

### Trait and processes

- bacillus shaped — **METPO:1000667**
- cell morphogenesis — candidate **GO:0000902**
- regulation of cell shape — candidate **GO:0008360**
- peptidoglycan-based cell-wall biogenesis — candidate **GO:0009273**
- cell-wall organization or biogenesis — candidate **GO:0071554**
- lateral PG synthesis / cylindrical cell elongation — label-only until the project’s preferred process term is verified
- septal PG synthesis / cell division
- circumferential glycan insertion
- sacculus mechanical anisotropy
- cell diameter control
- de novo rod-shape recovery

### Complexes and cellular structures

- Rod complex / elongasome — MreB, MreC, MreD, RodZ, RodA, PBP2
- divisome — FtsZ-associated apparatus including FtsW–FtsI
- peptidoglycan sacculus
- cytoplasmic membrane
- periplasm — candidate **GO:0042597**
- Gram-negative outer membrane — candidate **GO:0009279**
- MreB cytoskeletal filaments
- FtsZ ring

### Genes and proteins

- **mreB / MreB:** actin-like organizer of circumferential Rod-complex activity
- **mreC / MreC:** Rod-complex regulator; evidence supports activation through PBP2–RodA in *E. coli*
- **mreD / MreD:** core component, but its precise causal function remains incompletely resolved
- **rodZ / RodZ:** membrane-associated MreB/Rod-complex organizer
- **mrdB (rodA) / RodA:** SEDS-family PG glycan polymerase
- **mrdA (pbpA) / PBP2:** class-B PBP transpeptidase for elongation
- **ponA / PBP1:** representative class-A bifunctional PBP; diameter effect is taxon/context dependent
- **ftsW / FtsW** and **ftsI / FtsI (PBP3):** septal synthase pair; useful negative/contrast nodes
- **murJ / MurJ:** lipid-II flippase
- **glmS, glmM, glmU:** UDP-GlcNAc precursor pathway
- PG hydrolases/autolysins, including MltG-like lytic transglycosylases
- **lpxC / LpxC, LPS-modification machinery:** candidate upstream envelope-mechanics nodes in Gram-negative taxa
- **rdfA / RdfA:** archaeal rod-determining factor A; label-only and *H. volcanii*-specific
- **cetZ1 / CetZ1, lonB / LonB, artA / ArtA, pssA/PssD:** archaeal boundary nodes, not part of the canonical bacterial graph
- **gpsB / GpsB:** coccoid comparator controlling PBP localization; not a generic rod determinant
- **bacA and lmdC:** curvature/remodeling module; exclude from the generic straight-rod core

Protein identifiers should be assigned per organism and strain from UniProt rather than treating gene symbols as universal accessions.

### Chemicals and substrates

- peptidoglycan
- lipid II — stable ChEBI identifier should be verified for the exact chemical form before curation
- UDP-N-acetylglucosamine — candidate **CHEBI:16264**
- N-acetylglucosamine — candidate **CHEBI:28009**
- N-acetylmuramic acid — candidate **CHEBI:28880**
- glucosamine 6-phosphate — candidate **CHEBI:16077**
- fructose 6-phosphate — candidate **CHEBI:15946**
- undecaprenyl phosphate / undecaprenyl pyrophosphate — exact protonation-specific CURIE should be verified
- lipopolysaccharide
- amino sugars, which can bypass the GlmS requirement under appropriate conditions (galinier2023recentadvancesin pages 3-5)
- A22, mecillinam, β-lactams, vancomycin, nisin, and other envelope inhibitors as experimental factors—not constitutive trait causes

### Environmental and experimental factors

- growth phase and nutrient condition
- osmotic/turgor stress
- cell-wall-targeting antibiotics
- induced spheroplast or L-form state
- MreB/Rod-system depletion, overexpression, or chemical inhibition
- aPBP depletion/overexpression
- outer-membrane fortification or LPS remodeling
- swimming versus surface-associated state in *H. volcanii*
- microscopy-based length/width measurement, fluorescent D-amino-acid labeling, MreB tracking, bacterial cytological profiling, and CRISPRi perturbation

## Candidate causal edges

The compact edge set below is followed by curation-level evidence details.

| Subject | Predicate | Object | Taxon/scope | Evidence strength | DOI |
|---|---|---|---|---|---|
| Peptidoglycan sacculus | maintains | rod shape / cell shape under turgor | Broad bacteria; review + primary support | Strong; review-supported; boundary: not universal in archaea/wall-less states (goudin2023recoveryofvibrio pages 1-2, galinier2023recentadvancesin pages 3-5) | 10.1371/journal.pone.0293276; 10.3390/biom13050720 |
| MreB filaments | orient | circumferential Rod-complex PG synthesis | Rod-shaped bacteria, especially *E. coli*/*B. subtilis* | Strong; review/primary mix (fivenson2023arolefor pages 1-2, goudin2023recoveryofvibrio pages 1-2) | 10.1073/pnas.2301987120; 10.1371/journal.pone.0293276 |
| RodA–PBP2 complex | drives | lateral elongation / cylindrical growth | Rod-shaped bacteria; broad review scope | Strong; review-backed (fivenson2023arolefor pages 1-2, galinier2023recentadvancesin pages 3-5) | 10.1073/pnas.2301987120; 10.3390/biom13050720 |
| MreC | activates | PBP2, which activates RodA | *E. coli* Rod complex | Moderate-strong; direct in peer-reviewed paper intro/mechanistic summary (fivenson2023arolefor pages 1-2) | 10.1073/pnas.2301987120 |
| Rod system activity | increases | sacculus anisotropy and narrower diameter | *Bacillus subtilis*; generalized to *E. coli* | Strong but preprint (dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 3-6) | 10.1101/392837 |
| Class A PBPs (aPBPs/PBP1/PonA) | widen and repair | cell wall / promote wider diameter and anti-lytic repair | *B. subtilis*; broad PG maintenance role | Strong but partly preprint; taxon-specific for diameter (dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 10-12, goudin2023recoveryofvibrio pages 1-2) | 10.1101/392837; 10.1371/journal.pone.0293276 |
| Outer-membrane fortification | rescues | growth and rod-shape defects of Rod-complex hypomorphs | Gram-negative *E. coli* | Strong; peer-reviewed; taxon-specific (fivenson2023arolefor pages 1-2, fivenson2023arolefor media 0289c886) | 10.1073/pnas.2301987120 |
| PBP2 (MreB-associated) | drives | de novo elongation and branching during rod recovery | *Vibrio cholerae* spheroplast recovery | Strong; peer-reviewed; taxon- and assay-specific (goudin2023recoveryofvibrio pages 1-2) | 10.1371/journal.pone.0293276 |
| RdfA | required for | rod formation | *Haloferax volcanii* | Strong; peer-reviewed; boundary: archaeal mechanism, non-PG (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0 |
| Early-log / swimming conditions | favor | rod morphology over disks | *Haloferax volcanii* | Strong; peer-reviewed; environmental/growth-phase specific (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0 |
| GpsB | localizes/regulates | PBP2/PBP4 to permit elongation and avoid rounder cells | *Staphylococcus aureus* | Moderate-strong; peer-reviewed; boundary: coccoid comparator, not bacillus trait itself (costa2024theroleof pages 13-14) | 10.1128/mbio.03235-23 |
| Fluorescent MreB profiling | supports | antibiotic mode-of-action / envelope-target assays | Phenotypic assay toolkit | Strong for application; not causal for trait (schafer2024dissectingantibioticeffects pages 1-2) | 10.1128/spectrum.03275-23 |


*Table: This table summarizes compact, curation-ready candidate causal edges relevant to bacillus/rod morphology, emphasizing well-supported mechanisms, boundary cases, and practical assay relevance. It helps distinguish core rod-shape determinants from taxon-specific or application-focused evidence.*

| # | Subject–predicate–object | Supporting snippet | Reference | Curation note |
|---|---|---|---|---|
| 1 | PG sacculus — **enables/maintains** → bacterial cell shape | “The shape of bacteria is maintained by a rigid cell-wall consisting of cross-linked peptidoglycan.” | Goudin et al., 2023, DOI 10.1371/journal.pone.0293276 (goudin2023recoveryofvibrio pages 1-2) | **Curate broadly for PG-walled bacteria**, not archaea or stable wall-less forms. |
| 2 | elongasome — **directs** → lateral PG insertion and cylindrical growth | “direct the lateral insertion of PG…enabling cylindrical growth” | Galinier et al., 2023, DOI 10.3390/biom13050720 (galinier2023recentadvancesin pages 3-5) | Strong review-backed core edge. |
| 3 | MreB filaments — **orient** → Rod-complex synthesis perpendicular to the long axis | Rod complex “dynamically rotate[s] around the long axis”; MreB is thought to orient it orthogonally | Fivenson et al., 2023, DOI 10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2) | Strong canonical edge; retain “thought to” nuance for the exact rudder mechanism. |
| 4 | RodA–PBP2 — **catalyzes** → sidewall PG polymerization/cross-linking and elongation | SEDS protein polymerizes glycan and bPBP cross-links it; “RodA–PBP2…play[s an] essential role in rod shape determination” | Fivenson et al., 2023 (fivenson2023arolefor pages 1-2) | Strong. Ground RodA and PBP2 per taxon. |
| 5 | MreC — **activates through conformational signaling** → PBP2, then RodA | “MreC activates…PBP2, which in turn activates RodA” | Fivenson et al., 2023 (fivenson2023arolefor pages 1-2) | Strongest for *E. coli*; mark taxon-specific rather than universal. |
| 6 | increased Rod-system activity — **increases** → oriented PG/mechanical anisotropy and **decreases** diameter | Circumferential synthesis “increases…oriented material…mechanical anisotropy,” reinforcing rod shape | Dion et al., 2018 preprint, DOI 10.1101/392837 (dion2018celldiameterin pages 1-3, dion2018celldiameterin pages 8-10) | Mechanistically valuable but preprint-derived; verify against the final journal article before production curation. |
| 7 | aPBP/PBP1 activity — **opposes Rod-system narrowing and repairs** → PG wall | aPBPs insert less-oriented material, widen cells, and aPBP-deficient thin rods lyse more frequently | Dion et al., 2018 (dion2018celldiameterin pages 10-12) | Taxon/context dependent; do not encode “aPBPs cause rod shape” as a universal edge. |
| 8 | stronger Gram-negative outer membrane — **rescues** → rod shape in Rod-complex hypomorphs | OM changes predicted to strengthen it “suppress the growth and shape defects” of Rod-complex mutants | Fivenson et al., 2023 (fivenson2023arolefor pages 1-2, fivenson2023arolefor media 0289c886) | Strong *E. coli*-specific modifier edge; not applicable to Gram-positive bacteria. |
| 9 | MreB-associated PBP2 — **drives** → elongation/branching during de novo rod recovery | “Elongation and branching relied on…PBP2”; FtsI was not involved | Goudin et al., 2023 (goudin2023recoveryofvibrio pages 1-2) | Strong but spheroplast-recovery assay-specific. Branching is an intermediate, not the target trait. |
| 10 | aPBPs — **drive** → excess-periplasm elimination before rod recovery | “Periplasm elimination was driven by…aPBPs” | Goudin et al., 2023 (goudin2023recoveryofvibrio pages 1-2) | Curate only in a *V. cholerae* recovery subgraph. |
| 11 | early-log growth/swimming — **favors** → rod state in *H. volcanii* | Cells are “rod-shaped during early-log growth phase and when swimming” | Schiller et al., 2024, DOI 10.1038/s41467-024-45196-0 (schiller2024identificationofstructural pages 1-2) | Strong environmental boundary edge; archaeal, non-PG mechanism. |
| 12 | RdfA — **is required for** → rod formation in *H. volcanii* | Deletion-strain phenotyping established RdfA as required for rods | Schiller et al., 2024 (schiller2024identificationofstructural pages 1-2) | Strong, taxon-specific, label-only until stable gene/protein accession is verified. |
| 13 | loss of GpsB — **delocalizes/increases peripheral activity of** → PBP2/PBP4 — **causes** → rounder cells | Increased peripheral cross-linking yields a stiffer wall and “rounder, smaller cells” | Costa et al., 2024, DOI 10.1128/mbio.03235-23 (costa2024theroleof pages 13-14) | **Boundary evidence only:** *S. aureus* is coccoid; useful for general spatial-PG logic, not the bacillus core. |
| 14 | BacA–LmdC module — **localizes remodeling to** → inner curve and modulates curvature | BacA localizes LmdC; localized hydrolysis/insertion increases inner-curve elongation | Pöhl et al., 2024, DOI 10.7554/eLife.86577.2 (pohl2024adynamicbactofilin pages 19-21) | Curvature-specific. Do not curate as necessary for straight rods. |

### Quantitative evidence

In *B. subtilis*, direct inducible perturbations showed that lowering PBP1 made cells **23% thinner**, whereas PBP1 overexpression produced rods approaching **twice wild-type diameter**. Increased mreBCD expression progressively narrowed cells; the reported PBP1/MreB abundance ratio of approximately **0.8–1.5** maintained width within about **±5%** of wild type (dion2018celldiameterin pages 3-6). These are useful evidence annotations for diameter regulation, but they come from a 2018 preprint and should not be elevated to universal thresholds.

The 2024 archaeal study examined rod-only, disk-only, and wild-type proteomes across growth phases and used deletion phenotyping to separate shape-dependent from growth-phase-dependent abundance changes. Its principal contribution is the explicit demonstration that a rod phenotype can be environmentally switched and genetically controlled without the bacterial PG elongasome (schiller2024identificationofstructural pages 1-2).

## Recent developments and interpretation

1. **Envelope-level mechanics:** Fivenson et al. showed that the Gram-negative outer membrane is not merely a permeability barrier; its load-bearing capacity can restore rod propagation when PG synthesis is compromised. The authors’ model is a feedback loop: envelope strength preserves a long axis, allowing MreB-guided synthesis to become correctly oriented, which then reinforces the rod (fivenson2023arolefor pages 1-2, fivenson2023arolefor media 0289c886).
2. **De novo morphogenesis:** Goudin et al. separated early aPBP-dependent periplasm removal from subsequent MreB/PBP2-dependent elongation. This argues that rod formation can be rebuilt without inheriting a pre-existing cylindrical sacculus, but by sequentially activating distinct PG systems (goudin2023recoveryofvibrio pages 1-2).
3. **Cross-domain caution:** Schiller et al. identified RdfA and growth-state regulation in an archaeon, demonstrating convergent rod phenotypes with different molecular substrates (schiller2024identificationofstructural pages 1-2).
4. **Spatial regulation beyond canonical rods:** GpsB-dependent localization of PG enzymes in *S. aureus* and BacA–LmdC-dependent curvature control illustrate a broader principle: local synthesis, cross-linking, and hydrolysis—not enzyme abundance alone—determine shape (costa2024theroleof pages 13-14, pohl2024adynamicbactofilin pages 19-21).

## Applications and real-world implementations

- **Antibiotic mode-of-action profiling:** A 2024 *Microbiology Spectrum* study recommends a minimal toolkit combining bacterial cytological profiling, a membrane-potential probe, and fluorescent MinD/MreB fusions, optionally supplemented with Laurdan fluidity measurements and a PliaI reporter. It distinguished valinomycin, vancomycin, and dual-action nisin and is designed for laboratories without highly specialized equipment (schafer2024dissectingantibioticeffects pages 1-2).
- **Drug-target interpretation:** RodA, PBP2, lipid-II handling, and precursor synthesis are attractive envelope targets, but morphology is a systems-level output. Outer-membrane mechanics and compensatory aPBP activity can suppress shape defects, so a spherical phenotype is not a uniquely specific readout of one target (fivenson2023arolefor pages 1-2, galinier2023recentadvancesin pages 3-5).
- **Infection biology:** Cell-wall-deficient spherical states can be induced by environmental insults, including wall-targeting antibiotics; recovery assays reveal how pathogens re-establish growth and polarity (goudin2023recoveryofvibrio pages 1-2). In *S. aureus*, mild elongation may matter in infection contexts such as osteomyelitis, but this is not evidence that the organism is bacillus-shaped (costa2024theroleof pages 13-14).
- **Bioprocess engineering:** Morphology genes such as mreB and PG-remodeling genes are being explored to change cell dimensions or coordinate lysis for recovery of intracellular biopolymers. Such engineering is application evidence, not proof that any single perturbation universally causes the target trait.

## Recommended initial TraitMech graph

For `bacillus_shaped.yaml`, the most defensible conserved core is:

1. PG precursor biosynthesis → lipid II availability.
2. MurJ-mediated translocation → extracellular/periplasmic lipid-II supply.
3. MreB/MreC/MreD/RodZ organization → circumferential Rod-complex activity.
4. RodA glycan polymerization + PBP2 transpeptidation → lateral PG insertion.
5. Oriented lateral insertion → anisotropic cylindrical elongation.
6. aPBP-mediated synthesis/repair → envelope integrity and diameter modulation.
7. septal FtsW–FtsI synthesis → division and rounded new poles.
8. PG sacculus plus envelope mechanical resistance → stable bacillus-shaped morphology.

Encode organism-specific branches separately: Gram-negative outer-membrane reinforcement, *V. cholerae* spheroplast recovery, polar-growing Rhizobiales, and archaeal RdfA/CetZ1 regulation.

## Warnings: claims not yet ready for generic curation

- Do not equate **bacillus shaped** with genus *Bacillus* or spore formation.
- Do not assert that MreB is necessary for every microbial rod; polar-growing bacteria and archaea are counterexamples.
- Do not curate an exact universal length-to-width threshold without a METPO assay standard.
- Do not treat curved rods, coccobacilli, branched intermediates, or filaments as unqualified instances without secondary morphology annotations.
- Do not generalize the outer-membrane rescue mechanism beyond Gram-negative organisms.
- Do not add RdfA, GpsB, BacA, LmdC, CrvA, or crescentin to the conserved straight-rod core.
- Do not use A22 or mecillinam phenotypes as target-specific evidence without controls; morphology effects can be downstream and condition dependent.
- Verify final GO, ChEBI, UniProt, Rhea, and EC accessions against the precise organism and chemical form before committing YAML. Label-only nodes are preferable to uncertain identifiers.
- The diameter-balance study cited here is a preprint; its quantitative values need confirmation against the final peer-reviewed version before production curation (dion2018celldiameterin pages 3-6).

## DOI-first bibliography

1. Fivenson EM et al. “A role for the Gram-negative outer membrane in bacterial shape determination.” *PNAS*. Published **22 August 2023**. https://doi.org/10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2)
2. Galinier A et al. “Recent Advances in Peptidoglycan Synthesis and Regulation in Bacteria.” *Biomolecules* 13:720. Published **April 2023**. https://doi.org/10.3390/biom13050720 (galinier2023recentadvancesin pages 3-5)
3. Goudin A et al. “Recovery of Vibrio cholerae polarized cellular organization after exit from a non-proliferating spheroplast state.” *PLOS ONE* 18:e0293276. Published **26 October 2023**. https://doi.org/10.1371/journal.pone.0293276 (goudin2023recoveryofvibrio pages 1-2)
4. Schiller H et al. “Identification of structural and regulatory cell-shape determinants in Haloferax volcanii.” *Nature Communications* 15:1414. Accepted **16 January 2024**. https://doi.org/10.1038/s41467-024-45196-0 (schiller2024identificationofstructural pages 1-2)
5. Costa SF et al. “The role of GpsB in Staphylococcus aureus cell morphogenesis.” *mBio* 15. Published **March 2024**. https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 13-14)
6. Schäfer A-B et al. “Dissecting antibiotic effects on the cell envelope using bacterial cytological profiling.” *Microbiology Spectrum* 12. Published **30 January 2024**. https://doi.org/10.1128/spectrum.03275-23 (schafer2024dissectingantibioticeffects pages 1-2)
7. Pöhl S et al. “A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.” eLife reviewed version, **January 2024**. https://doi.org/10.7554/eLife.86577.2 (pohl2024adynamicbactofilin pages 19-21)
8. Dion MF et al. “Cell Diameter in Bacillus subtilis is Determined by the Opposing Actions of Two Distinct Cell Wall Synthetic Systems.” bioRxiv preprint, **August 2018**. https://doi.org/10.1101/392837 (dion2018celldiameterin pages 1-3)
9. Garner EC. “Toward a Mechanistic Understanding of Bacterial Rod Shape Formation and Regulation.” *Annual Review of Cell and Developmental Biology*. **2021**. https://doi.org/10.1146/annurev-cellbio-010521-010834
10. Egan AJF, Errington J, Vollmer W. “Regulation of peptidoglycan synthesis and remodelling.” *Nature Reviews Microbiology* 18:446–460. Published **May 2020**. https://doi.org/10.1038/s41579-020-0366-3

References

1. (galinier2023recentadvancesin pages 3-5): Anne Galinier, Clémentine Delan-Forino, Elodie Foulquier, Hakima Lakhal, and Frédérique Pompeo. Recent advances in peptidoglycan synthesis and regulation in bacteria. Biomolecules, 13:720, Apr 2023. URL: https://doi.org/10.3390/biom13050720, doi:10.3390/biom13050720. This article has 78 citations.

2. (goudin2023recoveryofvibrio pages 1-2): Anthony Goudin, Jean-Luc Ferat, Christophe Possoz, François-Xavier Barre, and Elisa Galli. Recovery of vibrio cholerae polarized cellular organization after exit from a non-proliferating spheroplast state. PLOS ONE, 18:e0293276, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293276, doi:10.1371/journal.pone.0293276. This article has 3 citations and is from a peer-reviewed journal.

3. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

4. (williams2019mechanismsofpolar pages 57-61): Michelle A. Williams. Mechanisms of polar growth in the alphaproteobacterial order rhizobiales. PhD thesis, University of Missouri Libraries, 2019. URL: https://doi.org/10.32469/10355/79574, doi:10.32469/10355/79574.

5. (fivenson2023arolefor pages 1-2): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

6. (fivenson2023arolefor media 0289c886): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

7. (dion2018celldiameterin pages 8-10): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

8. (dion2018celldiameterin pages 3-6): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

9. (dion2018celldiameterin pages 10-12): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

10. (costa2024theroleof pages 13-14): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (schafer2024dissectingantibioticeffects pages 1-2): Ann-Britt Schäfer, Margareth Sidarta, Ireny Abdelmesseh Nekhala, Gabriela Marinho Righetto, Aysha Arshad, and Michaela Wenzel. Dissecting antibiotic effects on the cell envelope using bacterial cytological profiling: a phenotypic analysis starter kit. Mar 2024. URL: https://doi.org/10.1128/spectrum.03275-23, doi:10.1128/spectrum.03275-23. This article has 19 citations and is from a domain leading peer-reviewed journal.

12. (dion2018celldiameterin pages 1-3): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

13. (pohl2024adynamicbactofilin pages 19-21): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.