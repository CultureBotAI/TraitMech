---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:56:47.533629'
end_time: '2026-08-04T09:03:49.936440'
duration_seconds: 422.4
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: lophotrichous
  trait_identifier: traitmech:000058
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: lophotrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with a tuft of multiple flagella at one pole
    of the cell.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar
    tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria
    maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar
    filaments acting as locomotory organelles.)'
  causal_graph_summary: 'lophotrichous_polar_tuft: 10 nodes, 8 edges'
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
- **Trait label:** lophotrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000058
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar filaments acting as locomotory organelles.)
- **Existing causal graph summary:** lophotrichous_polar_tuft: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **lophotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/lophotrichous.yaml`.

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
- **Trait label:** lophotrichous
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000058
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe polar tufts of flagella (lophotrichous) among the regular flagellation patterns bacteria maintain.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple flagellar filaments acting as locomotory organelles.)
- **Existing causal graph summary:** lophotrichous_polar_tuft: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **lophotrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/lophotrichous.yaml`.

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


# Curation report: lophotrichous flagellation

## Trait record and scope

- **Trait label:** lophotrichous
- **Trait identifier:** `traitmech:000058`
- **Category / term kind:** MORPHOLOGY / CLASS
- **Mapping status:** REVIEWED
- **Parent:** `traitmech:000056`
- **Operational definition:** a cell bears a tuft of a few or multiple flagella at one pole. This is a spatial-and-numerical morphology, not simply the capacities for flagellar assembly or swimming. Burnham et al. explicitly distinguish lophotrichous from monotrichous—one flagellum at one pole—and amphitrichous—flagellation at both poles. Peritrichous cells instead distribute flagella over the lateral cell surface (burnham2020apolarflagellar pages 1-2).

The immediate causal phenotype should therefore be represented as **multiple flagellar filaments assembled at one cellular pole**. Flagellum-mediated motility is a frequent downstream function, but should not be made logically equivalent to lophotrichy: nonmotile cells can retain visible flagella, aflagellate cells can move by other mechanisms, and experimentally induced multiple polar flagella can reduce rather than improve swimming (burnham2020apolarflagellar pages 17-19, pulianmackal2024positioningofcellular pages 3-4).

### Boundary cases

1. **Monotrichous-to-hyperflagellated mutants:** deletion of `flhG` in normally monotrichous *Vibrio cholerae* produces multiple flagella at one pole. Morphologically this can look lophotrichous, but it is an induced numerical-control defect rather than evidence that wild-type *V. cholerae* possesses the trait (burnham2020apolarflagellar pages 17-19).
2. **Amphilophotrichous/bipolar tufts:** tufts at both poles are not strictly lophotrichous under the supplied definition. They should be represented separately or as a conjunction of “polar tuft” and “bipolar distribution.”
3. **Bundling:** several spatially separate filaments can bundle during swimming. A bundle observed by light microscopy is not sufficient to establish that several basal bodies arise as a tuft from one pole; electron microscopy, fluorescence labeling of filaments/basal bodies, or cryo-electron tomography is preferable.
4. **Detached or mislocalized filaments:** a polar filament found near a cell is not evidence of a polar tuft. In *Shewanella putrefaciens*, loss of FlhF can reduce the fraction of flagellated cells and cause frequent detachment from the pole (schwan2022constitutiveproductionof pages 1-4).
5. **Archaella:** archaeal motility structures are evolutionarily distinct from bacterial flagella. MinD4-dependent archaellum positioning in *Haloferax volcanii* is mechanistically informative but should not be curated directly into this bacterial morphology without an explicit cross-domain abstraction (pulianmackal2024positioningofcellular pages 8-9).

## Current mechanistic understanding

The strongest conserved model is an opposing **FlhF–FlhG nucleotide-switch circuit**. FlhF is an SRP-family GTPase that promotes selection of a polar assembly site and recruitment/assembly of early flagellar components. FlhG, a MinD/ParA-family ATPase also called FleN in some taxa, constrains flagellar number and can antagonize FlhF through stimulation of FlhF GTPase activity and/or transcriptional control. The molecular implementation varies substantially by taxon (burnham2020apolarflagellar pages 1-2, schuhmacher2015howbacteriamaintain pages 8-9).

Polar flagellates also commonly impose a transcriptional checkpoint: assembly of the MS ring, C ring, and core flagellar type III secretion system precedes activation of rod- and hook-gene transcription. This was experimentally supported in *V. cholerae* and *Pseudomonas aeruginosa* and appears broadly distributed among Gram-negative polar flagellates (burnham2020apolarflagellar pages 17-19, burnham2020apolarflagellar pages 1-2).

A 2024 expert review places FlhG within the wider ParA/MinD ATPase family that spatially organizes bacterial mesoscale cargo. It emphasizes that FlhF and FlhG are opposing regulators, that FlhG loss usually causes hyperflagellation and reduced motility, and that phenotypes vary among organisms. In *Halothiobacillus neapolitanus*, `flhG` deletion causes mispositioned flagellar tufts as well as cell-division defects (pulianmackal2024positioningofcellular pages 4-6, pulianmackal2024positioningofcellular pages 3-4). The underlying positioning mechanism nevertheless remains incompletely resolved, so the circuit should not be presented as universally identical across all lophotrichous bacteria (pulianmackal2024positioningofcellular pages 3-4).

Recent systems-level work found that **more than one-third of sequenced bacterial genomes encode multiple ParA/MinD-family ATPases**. In *H. neapolitanus*, five such ATPases were experimentally assigned to distinct cargos, including the flagellum, chromosome, divisome, carboxysome, and chemoreceptor cluster. This supports cargo-specific spatial regulation rather than a single generic positioning ATPase (pulianmackal2024positioningofcellular pages 6-8).

## Candidate graph nodes

### Trait and phenotype nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| lophotrichous | morphology class | `traitmech:000058` | Target node; quote identifier verbatim. |
| polar flagellar tuft | cellular morphology | Label only | Immediate morphological realization of the trait. |
| multiple flagella at one pole | assay-observed phenotype | Label only | Useful explicit phenotype node for microscopy evidence. |
| hyperflagellation | phenotype | Label only | Not synonymous with lophotrichy; may be nonpolar or mutant-induced. |
| mispositioned flagellar tuft | phenotype | Label only | Relevant to *H. neapolitanus* `flhG` deletion. |
| flagellum-dependent motility | biological process | `GO:0071973` | Downstream capacity, not part of the defining morphology. |

### Genes and proteins

| Node | Molecular role | Grounding recommendation |
|---|---|---|
| FlhF | SRP-family GTPase; promotes polar site selection and early flagellar assembly | Gene/protein label plus organism-specific UniProt ID after strain selection; do not assign one universal UniProt accession. |
| FlhG / FleN | MinD/ParA-family ATPase; controls number, localization, C-ring assembly, and in some taxa transcription | Keep `FlhG` and `FleN` as aliases only where orthology is established. |
| HubP | polar landmark recruiting FlhG in *Vibrio* | Taxon-specific protein node; label only until a strain is fixed. |
| FliF | MS-ring protein and early basal-body component | Taxon-specific protein node. |
| FliG | C-ring/rotor component | Taxon-specific protein node. |
| FliM | C-ring switch protein and FlhG partner in *Shewanella* | Taxon-specific protein node. |
| FliN / FliY | C-ring components; family usage varies among taxa | Do not collapse paralog-specific functions across organisms. |
| FlrA / FleQ-like master regulator | transcriptional regulator of flagellar genes | Preserve organism-specific names and regulatory relationships. |
| flagellum-associated two-component system | signal-transduction system | Label only unless the precise histidine kinase/response regulator pair is identified for the curated taxon. |

### Complexes, structures, and localizations

- Cell pole / old cell pole.
- Flagellar MS ring.
- Flagellar C ring/rotor-switch complex.
- Flagellar basal body.
- Flagellar type III secretion system (fT3SS).
- Rod, hook, and extracellular filament.
- Cytoplasmic membrane and cytoplasm.
- Nascent polar flagellar assembly site.

The Gene Ontology term `GO:0009288` can ground “bacterial-type flagellum.” More specific structural nodes should be checked against the current GO release during implementation rather than assigned unverified identifiers.

### Molecular functions and processes

- GTP binding/hydrolysis by FlhF.
- ATP binding/hydrolysis and nucleotide-dependent dimerization by FlhG.
- Protein localization to the cell pole.
- Flagellar basal-body/C-ring assembly.
- Flagellar protein export through fT3SS.
- Activation or repression of flagellar-gene transcription.
- Numerical control of flagellar biogenesis.
- Flagellar rotation and swimming.

### Experimental and environmental nodes

| Node | Role in graph |
|---|---|
| `flhF` deletion/depletion | Perturbation expected to impair polar assembly, placement, or flagellation. |
| `flhG` deletion/depletion | Perturbation causing excess or mispositioned polar flagella in several taxa. |
| `hubP` deletion | Disrupts FlhG polar localization in *Vibrio*; taxon-specific. |
| C-ring binding-site mutation | Tests FlhG recruitment/partner switching. |
| nucleotide-state mutation | Tests FlhF/FlhG switching and partner selection. |
| electron microscopy/cryo-ET | Preferred assay for number and basal-body origin. |
| fluorescent flagellin or basal-body imaging | Supports cell-cycle-resolved placement and number measurements. |
| soft-agar swimming assay | Functional output; cannot by itself diagnose lophotrichy. |
| medium viscosity | Modifies flagellar mechanics and observed swimming behavior; not established as a cause of lophotrichous assembly in the retrieved evidence. |

No specific chemical nutrient, electron donor, electron acceptor, metabolite, or environmental exposure is sufficiently supported here as a direct cause of lophotrichous morphology. GTP, ATP, and membrane lipids are mechanistic participants, but bulk availability of these chemicals should not be curated as a trait-inducing environmental edge without direct perturbation evidence.

## Candidate causal edges

The following table is suitable as a starting point for `lophotrichous.yaml`. “Core” means broadly supported for polar flagellation, not demonstrated in every naturally lophotrichous species.

| # | Subject–predicate–object | Reference | Supporting snippet | Interpretation and curation status |
|---|---|---|---|---|
| 1 | **FlhF — promotes — polar flagellar assembly-site establishment** | DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034), 2015 | “FlhF marks the future flagellar site to establish polar location.” | **High confidence, core polar mechanism.** Directly relevant to the polar component of lophotrichy, but does not itself explain why multiple flagella form (schuhmacher2015howbacteriamaintain pages 8-9). |
| 2 | **FlhF — recruits/promotes localization of — FliF/MS-ring machinery at the pole** | DOI: [10.17192/z2017.0061](https://doi.org/10.17192/z2017.0061), 2017 | “FlhF is sufficient for polar localization and recruiting the MS-ring protein FliF.” | **Medium confidence.** Mechanistically useful but supported here through a dissertation-level source; seek the underlying peer-reviewed experiment before final curation (rossmann2017spatialregulationof pages 17-20). |
| 3 | **FlhG — negatively regulates — polar flagellum number** | DOI: [10.1128/mbio.03107-19](https://doi.org/10.1128/mbio.03107-19), 2020 | “FlhG influences flagellar numbers either by stimulating FlhF GTPase activity or by repressing master transcriptional regulators.” | **High confidence, core polar mechanism.** Predicate should remain “negatively regulates,” not “prevents lophotrichy,” because natural tufts require a species-specific set point above one (burnham2020apolarflagellar pages 1-2). |
| 4 | **FlhG — stimulates — FlhF GTPase activity** | DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034), 2015 | “FlhG interacts with FlhF to stimulate its GTPase activity.” | **Medium-high confidence.** A plausible molecular edge connecting the number-control ATPase to the polar-site GTPase; conservation across all taxa is uncertain (schuhmacher2015howbacteriamaintain pages 8-9). |
| 5 | **`flhG` deletion — causes — multiple polar flagella/hyperflagellation** | DOI: [10.1128/mbio.03107-19](https://doi.org/10.1128/mbio.03107-19), 2020 | “*V. cholerae* ΔflhG mutants display hyperflagellation (multiple flagella at one pole).” | **High-confidence perturbation edge, but boundary-case evidence.** Wild-type *V. cholerae* is monotrichous; annotate `mutant-induced`, not natural lophotrichy (burnham2020apolarflagellar pages 17-19). |
| 6 | **`flhG` deletion — causes — mispositioned flagellar tufts** | DOI: [10.1016/j.mib.2024.102485](https://doi.org/10.1016/j.mib.2024.102485), published June 2024 | “In *H. neapolitanus*, FlhG deletion causes mispositioned flagellar tufts.” | **Medium-high confidence, taxon-specific.** Strong recent support for tuft positioning, but retrieved through a review; link the cited primary 2023 experiment when available (pulianmackal2024positioningofcellular pages 4-6, pulianmackal2024positioningofcellular pages 3-4). |
| 7 | **HubP — recruits/localizes — FlhG to the cell pole** | DOI: [10.1128/JB.00462-16](https://doi.org/10.1128/JB.00462-16), 2016; reviewed in DOI:10.1093/femsre/fuv034 | “HubP recruits FlhG to the cell pole”; HubP loss produces diffuse or nonpolar FlhG. | **High confidence but *Vibrio*-specific.** Do not generalize HubP as the universal landmark of lophotrichous bacteria (schuhmacher2015howbacteriamaintain pages 7-8). |
| 8 | **HubP — does not determine — FlhF polar targeting** | DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034), 2015 | “FlhF polar targeting occurs independently of HubP.” | **Medium-high confidence, contextual negative edge.** Useful for avoiding an incorrect HubP→FlhF localization assertion (schuhmacher2015howbacteriamaintain pages 7-8). |
| 9 | **FliM/C-ring assembly — recruits or interacts with — FlhG** | DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034), 2015; DOI: [10.1101/2022.07.21.500047](https://doi.org/10.1101/2022.07.21.500047), posted July 2022 | FlhG “bind[s] FliM… and travel[s] to the nascent basal body”; C-ring assembly causes release and ATP-dependent dimerization. | **Medium-high, *Shewanella*-specific.** The 2022 source is a preprint; the general interaction is also supported by the peer-reviewed review (schwan2022constitutiveproductionof pages 1-4, schuhmacher2015howbacteriamaintain pages 8-9). |
| 10 | **ATP-bound FlhG dimer — interacts with/regulates — FlrA** | DOI: [10.1016/j.mib.2024.102485](https://doi.org/10.1016/j.mib.2024.102485), June 2024 | FlhG binds “FliM (monomeric form, nucleotide-independent)” and “FlrA (ATP-bound dimer form).” | **Medium confidence, *S. putrefaciens*-specific.** Represents a nucleotide-dependent partner switch linking assembly to transcription (pulianmackal2024positioningofcellular pages 4-6, pulianmackal2024positioningofcellular pages 8-9). |
| 11 | **MS-ring+C-ring+fT3SS assembly — enables activation of — rod/hook gene transcription** | DOI: [10.1128/mbio.03107-19](https://doi.org/10.1128/mbio.03107-19), published April 2020 | The basal structures “contribute to a regulatory checkpoint” before “rod and hook gene transcription.” | **High confidence in tested polar flagellates.** Demonstrated in *V. cholerae* and *P. aeruginosa*; likely broad but not universal (burnham2020apolarflagellar pages 17-19, burnham2020apolarflagellar pages 1-2). |
| 12 | **rod/hook transcription and fT3SS export — promote — completion of polar flagella** | DOI: [10.1128/mbio.03107-19](https://doi.org/10.1128/mbio.03107-19), 2020 | Ordered transcription follows production of “MS ring, C ring, and fT3SS core proteins that form a competent fT3SS.” | **High confidence as a general assembly edge.** It explains construction of each filament but not the tuft-number set point (burnham2020apolarflagellar pages 1-2). |
| 13 | **multiple rotating polar flagella — can decrease — swimming motility** | DOI: [10.1128/mbio.03107-19](https://doi.org/10.1128/mbio.03107-19), 2020 | The *V. cholerae* ΔflhG mutant “produces multiple rotating flagella but exhibits reduced motility.” | **High-confidence taxon/assay-specific edge.** Use “can decrease,” because effects depend on geometry, coordination, medium, and species (burnham2020apolarflagellar pages 17-19). |
| 14 | **FlhF localization — is interdependent with — FlhG localization** | DOI: [10.3389/fmicb.2021.655239](https://doi.org/10.3389/fmicb.2021.655239), published March 2021 | FlhF and FlhG localization patterns were “interdependent” and required for proper recruitment to the pole. | **Medium-high, *V. parahaemolyticus*-specific.** This monotrichous model informs the polar circuit but does not establish natural tuft formation (pulianmackal2024positioningofcellular pages 4-6). |
| 15 | **FlhG-mediated flagellum positioning — influences — chemoreceptor-array positioning** | DOI: [10.1016/j.mib.2024.102485](https://doi.org/10.1016/j.mib.2024.102485), 2024 | The review describes an “epistatic relationship” between FlhG-dependent flagellar positioning and downstream ParC-dependent chemoreceptor positioning. | **Uncertain for target graph.** This is a downstream spatial-organization edge, not necessary for defining lophotrichy; curate only in a taxon-specific expanded graph (pulianmackal2024positioningofcellular pages 6-8). |

The highest-confidence subset is summarized below.

| subject | predicate | object | organism/context | confidence | DOI |
|---|---|---|---|---|---|
| FlhF | promotes polar placement/assembly of | polar flagellum / initial assembly site | Broad polar flagellates; essential for polar flagellar biogenesis and placement, including Vibrio and other Gram-negative polar taxa; direct lophotrichous relevance is inferred from shared polar flagellation machinery (burnham2020apolarflagellar pages 1-2, rossmann2017spatialregulationof pages 17-20, schuhmacher2015howbacteriamaintain pages 8-9) | High | 10.1128/mbio.03107-19; 10.1093/femsre/fuv034 |
| FlhG | negatively regulates / limits number of | polar flagella | Broad polar flagellates; FlhG constrains flagellar number, often by modulating FlhF activity or flagellar gene expression (burnham2020apolarflagellar pages 1-2, schuhmacher2015howbacteriamaintain pages 8-9, pulianmackal2024positioningofcellular pages 3-4) | High | 10.1128/mbio.03107-19; 10.1093/femsre/fuv034; 10.1016/j.mib.2024.102485 |
| HubP | recruits / localizes | FlhG to the cell pole | Vibrio spp.; taxon-specific landmark mechanism; FlhG localization is HubP-dependent whereas FlhF is HubP-independent (schuhmacher2015howbacteriamaintain pages 7-8) | High (taxon-specific) | 10.1093/femsre/fuv034 |
| FliM (C-ring protein) | recruits / interacts with | FlhG | Shewanella putrefaciens; FlhG binds C-ring protein FliM during C-ring assembly, linking spatial control to nascent basal body formation; likely not universal in all lophotrichous taxa (rossmann2017spatialregulationof pages 117-120, schwan2022constitutiveproductionof pages 1-4, schuhmacher2015howbacteriamaintain pages 8-9) | Medium-High (taxon-specific) | 10.1101/2022.07.21.500047; 10.1093/femsre/fuv034; 10.17192/z2017.0061 |
| MS ring + C ring + flagellar T3SS assembly checkpoint | enables transcription of | rod/hook flagellar genes | Polar flagellates including Vibrio cholerae and Pseudomonas aeruginosa; conserved polar transcriptional program assisting FlhF/FlhG-dependent flagellation (burnham2020apolarflagellar pages 17-19, burnham2020apolarflagellar pages 1-2) | High | 10.1128/mbio.03107-19 |
| flhG deletion | causes | hyperflagellation / aberrant multiple polar flagella | Mutant-induced tuft evidence, commonly in normally monotrichous polar bacteria such as V. cholerae, V. parahaemolyticus, and P. aeruginosa; boundary case for curating natural lophotrichy (burnham2020apolarflagellar pages 17-19, rossmann2017spatialregulationof pages 17-20, pulianmackal2024positioningofcellular pages 3-4) | High | 10.1128/mbio.03107-19; 10.1016/j.mib.2024.102485 |
| flhG deletion | causes | mispositioned flagellar tufts | Halothiobacillus neapolitanus; recent 2024 review summarizing direct phenotype from dedicated flagellum-positioning ATPase system; strongest recent tuft/misposition evidence but not a canonical lophotrichous model (pulianmackal2024positioningofcellular pages 4-6, pulianmackal2024positioningofcellular pages 3-4, pulianmackal2024positioningofcellular pages 6-8) | Medium-High (taxon-specific, review-summarized) | 10.1016/j.mib.2024.102485 |
| multiple polar flagella | can reduce | swimming motility | V. cholerae ΔflhG mutant: multiple rotating polar flagella yet reduced motility versus wild type; supports that tuft-like mutant states need not improve locomotion (burnham2020apolarflagellar pages 17-19, pulianmackal2024positioningofcellular pages 3-4) | Medium-High | 10.1128/mbio.03107-19; 10.1016/j.mib.2024.102485 |
| FlhF localization | is interdependent with | FlhG localization | Vibrio parahaemolyticus; both proteins require each other for proper intracellular/polar localization, refining polar assembly control (closest direct evidence from monotrichous model) (pulianmackal2024positioningofcellular pages 4-6) | Medium (taxon-specific) | 10.3389/fmicb.2021.655239 |


*Table: This table compiles the strongest candidate causal edges for a lophotrichous TraitMech graph, emphasizing broadly supported FlhF/FlhG mechanisms and clearly marking taxon-specific or mutant-induced tuft evidence. It is useful for separating likely core polar-flagellation mechanisms from boundary-case observations that may need caution during curation.*

## Suggested minimal causal-graph architecture

A conservative graph should separate **polar placement**, **copy-number control**, **assembly**, and **functional output**:

1. `FlhF` → **positive regulation** → `polar flagellar assembly site`.
2. `HubP` → **positive regulation of localization** → `FlhG at pole` **[Vibrio only]**.
3. `FliM/C-ring` → **recruits/interacts with** → `FlhG` **[Shewanella-supported]**.
4. `FlhG` → **negative regulation** → `number of polar flagella`.
5. `FlhG` → **positive regulation** → `FlhF GTP hydrolysis/inactivation`.
6. `MS ring + C ring + fT3SS` → **enables** → `rod/hook transcription`.
7. `rod/hook/filament assembly` + `polar site specification` + `species-specific number set point >1` → **causally contributes to** → `polar flagellar tuft`.
8. `polar flagellar tuft` → **enables** → `flagellum-dependent motility`, with a qualification that excess or uncoordinated filaments can decrease motility.
9. `polar flagellar tuft` → **has phenotype** → `traitmech:000058`.

The node **species-specific number set point >1** is deliberately label-only. Current evidence strongly explains how polar flagella are positioned and how excess number arises when FlhG control fails, but it does not yet establish a universal molecular switch that specifies the normal tuft size of all naturally lophotrichous taxa.

## Applications and real-world relevance

- **Pathogenesis and colonization:** polar flagella power movement through host-associated environments in pathogens such as *Vibrio*, *Pseudomonas*, and *Campylobacter*. However, those genera contain different flagellation patterns, and pathogenic relevance should not be equated with lophotrichy itself. The ordered polar flagellar transcription program is conserved across multiple Gram-negative pathogens and maintains motility when FlhF/FlhG activity is perturbed (burnham2020apolarflagellar pages 17-19).
- **Antimicrobial strategy:** FlhF/FlhG, polar landmarks, assembly checkpoints, and fT3SS are mechanistic intervention candidates, but inhibition may exert strong selective pressure and could affect nonpathogenic polar bacteria. No clinically implemented lophotrichy-specific inhibitor was identified in the retrieved evidence.
- **Synthetic biology:** ParA/MinD systems are being considered as programmable cargo-positioning modules. Their demonstrated ability to position distinct cargos in the same bacterium suggests possible engineering of spatially organized synthetic organelles or motility machinery (pulianmackal2024positioningofcellular pages 6-8).
- **Phenotyping and taxonomy:** flagellar arrangement remains useful in microbial description, but reliable assignment increasingly requires high-resolution imaging rather than motility assays alone.

## Claims not ready for TraitMech curation

1. **A universal HubP pathway for lophotrichy:** unsupported; HubP evidence is primarily from *Vibrio*.
2. **FlhG loss as the natural cause of lophotrichous morphology:** incorrect. It often creates pathological hyperflagellation in normally monotrichous organisms.
3. **A fixed tuft size:** “a few” or “multiple” is supported, but no universal numerical cutoff was found.
4. **More flagella cause faster swimming:** contradicted by reduced motility in hyperflagellated *V. cholerae* (burnham2020apolarflagellar pages 17-19).
5. **Environmental induction by viscosity, nutrient, oxygen, or salinity:** plausible in some taxa but not directly supported as a causal determinant of tuft morphology by the retrieved sources.
6. **Universal FliM–FlhG or FlrA partner switching:** presently best supported in *Shewanella* and should be taxon-qualified (pulianmackal2024positioningofcellular pages 4-6, pulianmackal2024positioningofcellular pages 8-9).
7. **Direct transfer of monotrichous-model edges to natural lophotrichous species:** these edges can support a conserved polar-flagellation module, but the normal multi-flagellum set point requires evidence from a naturally lophotrichous organism.
8. **Unverified ontology identifiers:** organism-specific UniProt, NCBITaxon, KEGG, or Rhea identifiers should only be added after choosing an exact strain and checking the current database record.

## DOI-first bibliography

1. Pulianmackal LT, Vecchiarelli AG. **Positioning of cellular components by the ParA/MinD family of ATPases.** *Current Opinion in Microbiology*. Published June 2024;79:102485. DOI: [10.1016/j.mib.2024.102485](https://doi.org/10.1016/j.mib.2024.102485). Recent authoritative review of FlhG and related cargo-positioning ATPases (pulianmackal2024positioningofcellular pages 4-6, pulianmackal2024positioningofcellular pages 3-4, pulianmackal2024positioningofcellular pages 8-9, pulianmackal2024positioningofcellular pages 6-8).
2. Pulianmackal LT et al. **Multiple ParA/MinD ATPases coordinate the positioning of disparate cargos in a bacterial cell.** *Nature Communications*. Published June 2023;14:3255. The retrieved record supplies a preprint DOI, [10.1101/2022.06.09.495121](https://doi.org/10.1101/2022.06.09.495121); verify the final journal DOI before YAML insertion. Its principal reported statistic is that over one-third of sequenced bacteria encode multiple ParA/MinD ATPases (pulianmackal2024positioningofcellular pages 6-8).
3. Arroyo-Pérez EE, Ringgaard S. **Interdependent Polar Localization of FlhF and FlhG and Their Importance for Flagellum Formation of *Vibrio parahaemolyticus*.** *Frontiers in Microbiology*. Published March 2021;12:655239. DOI: [10.3389/fmicb.2021.655239](https://doi.org/10.3389/fmicb.2021.655239) (pulianmackal2024positioningofcellular pages 4-6).
4. Burnham PM, Kolar WP, Hendrixson DR. **A Polar Flagellar Transcriptional Program Mediated by Diverse Two-Component Signal Transduction Systems and Basal Flagellar Proteins Is Broadly Conserved in Polar Flagellates.** *mBio*. Published April 2020;11(2). DOI: [10.1128/mbio.03107-19](https://doi.org/10.1128/mbio.03107-19) (burnham2020apolarflagellar pages 17-19, burnham2020apolarflagellar pages 1-2).
5. Takekawa N et al. **HubP, a polar landmark protein, regulates flagellar number by assisting in the proper polar localization of FlhG in *Vibrio alginolyticus*.** *Journal of Bacteriology*. Published November 2016;198:3091–3098. DOI: [10.1128/JB.00462-16](https://doi.org/10.1128/JB.00462-16). The primary paper was identified bibliographically; the retrieved mechanistic evidence came through the FEMS review (schuhmacher2015howbacteriamaintain pages 7-8).
6. Schuhmacher JS, Thormann KM, Bange G. **How bacteria maintain location and number of flagella?** *FEMS Microbiology Reviews*. Published November 2015;39(6):812–822. DOI: [10.1093/femsre/fuv034](https://doi.org/10.1093/femsre/fuv034) (schuhmacher2015howbacteriamaintain pages 7-8, schuhmacher2015howbacteriamaintain pages 8-9).
7. Schuhmacher JS et al. **MinD-like ATPase FlhG effects location and number of bacterial flagella during C-ring assembly.** *Proceedings of the National Academy of Sciences USA*. Published March 2015;112:3092–3097. DOI: [10.1073/pnas.1419388112](https://doi.org/10.1073/pnas.1419388112). Identified as the relevant primary C-ring study; full text was not retrieved here.
8. Schwan M et al. **Constitutive production of flagellar proteins is required for proper flagellation in *Shewanella putrefaciens*.** bioRxiv preprint. Posted July 2022. DOI: [10.1101/2022.07.21.500047](https://doi.org/10.1101/2022.07.21.500047). Treat as preprint evidence unless a final peer-reviewed version is located (schwan2022constitutiveproductionof pages 1-4).

## Curation recommendation

Retain the existing `lophotrichous_polar_tuft` graph concept, but make its mechanistic core modular. The strongest curatable edges are **FlhF→polar site specification**, **FlhG⊣polar flagellum number**, **FlhG→FlhF GTPase activation**, and **basal-body/fT3SS checkpoint→rod/hook transcription**. Add HubP and FliM/FlrA partner-switch edges only in explicitly taxon-qualified branches. Most importantly, include a provenance distinction between **natural lophotrichous morphology** and **mutant-induced polar hyperflagellation**; the latter is excellent mechanistic evidence for number control but is not by itself evidence that a species carries `traitmech:000058`.

References

1. (burnham2020apolarflagellar pages 1-2): Peter M. Burnham, William P. Kolar, and David R. Hendrixson. A polar flagellar transcriptional program mediated by diverse two-component signal transduction systems and basal flagellar proteins is broadly conserved in polar flagellates. mBio, Apr 2020. URL: https://doi.org/10.1128/mbio.03107-19, doi:10.1128/mbio.03107-19. This article has 22 citations and is from a domain leading peer-reviewed journal.

2. (burnham2020apolarflagellar pages 17-19): Peter M. Burnham, William P. Kolar, and David R. Hendrixson. A polar flagellar transcriptional program mediated by diverse two-component signal transduction systems and basal flagellar proteins is broadly conserved in polar flagellates. mBio, Apr 2020. URL: https://doi.org/10.1128/mbio.03107-19, doi:10.1128/mbio.03107-19. This article has 22 citations and is from a domain leading peer-reviewed journal.

3. (pulianmackal2024positioningofcellular pages 3-4): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 15 citations and is from a peer-reviewed journal.

4. (schwan2022constitutiveproductionof pages 1-4): Meike Schwan, Ariane Khaledi, Sven Willger, Kai Papenfort, Timo Glatter, Susanne Häußler, and Kai M. Thormann. Constitutive production of flagellar proteins is required for proper flagellation in shewanella putrefaciens. bioRxiv, Jul 2022. URL: https://doi.org/10.1101/2022.07.21.500047, doi:10.1101/2022.07.21.500047. This article has 1 citations.

5. (pulianmackal2024positioningofcellular pages 8-9): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 15 citations and is from a peer-reviewed journal.

6. (schuhmacher2015howbacteriamaintain pages 8-9): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

7. (pulianmackal2024positioningofcellular pages 4-6): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 15 citations and is from a peer-reviewed journal.

8. (pulianmackal2024positioningofcellular pages 6-8): Lisa T Pulianmackal and Anthony G. Vecchiarelli. Positioning of cellular components by the para/mind family of atpases. Jun 2024. URL: https://doi.org/10.1016/j.mib.2024.102485, doi:10.1016/j.mib.2024.102485. This article has 15 citations and is from a peer-reviewed journal.

9. (rossmann2017spatialregulationof pages 17-20): Florian Roßmann. Spatial regulation of dual flagellar systems. ArXiv, Jan 2017. URL: https://doi.org/10.17192/z2017.0061, doi:10.17192/z2017.0061. This article has 0 citations.

10. (schuhmacher2015howbacteriamaintain pages 7-8): Jan S. Schuhmacher, Kai M. Thormann, and Gert Bange. How bacteria maintain location and number of flagella? FEMS microbiology reviews, 39 6:812-22, Nov 2015. URL: https://doi.org/10.1093/femsre/fuv034, doi:10.1093/femsre/fuv034. This article has 167 citations and is from a domain leading peer-reviewed journal.

11. (rossmann2017spatialregulationof pages 117-120): Florian Roßmann. Spatial regulation of dual flagellar systems. ArXiv, Jan 2017. URL: https://doi.org/10.17192/z2017.0061, doi:10.17192/z2017.0061. This article has 0 citations.