---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:15:05.377633'
end_time: '2026-08-04T07:23:53.100901'
duration_seconds: 527.72
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: axially filamented
  trait_identifier: METPO:1000705
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: axially_filamented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motility where the flagellum filament of an organism is located in
    the periplasm and does not extend past the cell envelope.
  parent_traits: METPO:1000702
  synonyms: axial filament
  evidence_summary: 'DOI:10.3390/biom10040550: flagella are hidden within the periplasmic
    space (Supports axial/periplasmic flagella as the defining motility structure.)'
  causal_graph_summary: 'axially_filamented_periplasmic_flagella: 10 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** axially filamented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000705
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility where the flagellum filament of an organism is located in the periplasm and does not extend past the cell envelope.
- **Parent traits:** METPO:1000702
- **Synonyms:** axial filament
- **Existing evidence:** DOI:10.3390/biom10040550: flagella are hidden within the periplasmic space (Supports axial/periplasmic flagella as the defining motility structure.)
- **Existing causal graph summary:** axially_filamented_periplasmic_flagella: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **axially filamented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/axially_filamented.yaml`.

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
- **Trait label:** axially filamented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000705
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility where the flagellum filament of an organism is located in the periplasm and does not extend past the cell envelope.
- **Parent traits:** METPO:1000702
- **Synonyms:** axial filament
- **Existing evidence:** DOI:10.3390/biom10040550: flagella are hidden within the periplasmic space (Supports axial/periplasmic flagella as the defining motility structure.)
- **Existing causal graph summary:** axially_filamented_periplasmic_flagella: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **axially filamented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/axially_filamented.yaml`.

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


# Curation report: axially filamented

## Executive summary

**Trait:** axially filamented  
**Identifier:** **METPO:1000705**  
**Category:** morphology; class; reviewed  
**Parent:** METPO:1000702  
**Synonym:** axial filament

The trait should denote a bacterium possessing one or more **flagellar filaments confined to the periplasm**, rather than flagella projecting beyond the outer membrane. In spirochetes these structures are usually called **periplasmic flagella (PFs), endoflagella, or axial filaments**. They arise from motors at one or both poles and run along the protoplasmic cylinder beneath the outer membrane. Their rotation deforms or rotates the cell body, producing rolling or undulatory propulsion; in several taxa they also mechanically determine cell shape. The defining feature is therefore **filament topology/localization**, not motility alone and not merely a spiral cell shape. Nakamura states that spirochetal flagella are “hidden within the periplasmic space,” whereas external flagella directly interact with the surrounding fluid (published 4 April 2020; DOI [10.3390/biom10040550](https://doi.org/10.3390/biom10040550)). (nakamura2020spirocheteflagellaand pages 1-3)

The most defensible TraitMech causal chain is:

**FlaB-containing filament assembly + sheath/coiling proteins → periplasmic flagellar filament → hook/motor coupling → proton-driven stator–rotor torque → PF rotation → cell-body deformation/rolling/undulation → spirochetal motility**, with a parallel structural branch from **PF integrity → taxon-specific cell morphology**. Virulence and tissue dissemination are biologically important downstream consequences, but should remain taxon- and assay-qualified rather than defining the morphology trait. (nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 9-11, chang2019structuralinsightsinto pages 10-12)

## 1. Trait scope and boundaries

### Included phenotype

A positive instance should have:

1. A bona fide bacterial flagellar filament.
2. Localization within the space bounded by the inner and outer membranes.
3. Connection through a hook to a basal motor embedded in the cytoplasmic membrane/peptidoglycan region.
4. No normal extension of the filament beyond the cell envelope.

The filament may be polar, bipolar, overlapping, or non-overlapping. *Borrelia burgdorferi* has approximately **14–22 PFs** that overlap near midcell; *Brachyspira hyodysenteriae* has **16–18**, also overlapping; *Leptospira interrogans* has **two short, non-overlapping PFs**. These are variants of the same topological trait, not separate trait states. (nakamura2020spirocheteflagellaand pages 1-3)

### Boundary cases and nearby traits

- **External polar or amphitrichous flagella:** exclude. *Campylobacter jejuni*, for example, bears external polar flagella; its motor findings can inform general flagellar mechanics but do not establish axial/periplasmic filamentation. (ribardo2024viscositydependentdeterminantsof pages 1-2)
- **Motility:** not equivalent. A cell can possess structurally defective PFs and be weakly motile or nonmotile. Conversely, nonflagellar gliding or twitching does not imply this trait.
- **Spiral or wavy morphology:** not sufficient. PFs straighten the whole body when lost in *B. burgdorferi*, but in *Leptospira* PF depletion principally changes the bent ends while the protoplasmic-cylinder helix is thought to involve MreB. Thus, “helical cell” must not be used as a proxy. (nakamura2020spirocheteflagellaand pages 3-5)
- **Flagellar sheath:** not universal in composition. FlaA/Fcp-dependent core–sheath organization is particularly developed in *Brachyspira* and *Leptospira*; *B. burgdorferi* has a different organization, with FlaB forming the filament and FlaA concentrated near its base. (nakamura2020spirocheteflagellaand pages 3-5)
- **Cytoplasmic axial structures or nonflagellar filaments:** exclude unless continuity with a flagellar motor, hook, and periplasmic filament is demonstrated.
- **Assay inference:** spiral motion in viscous medium, soft-agar migration, or gene presence alone is insufficient to assign the morphology trait without localization evidence.

## 2. Candidate graph nodes

### Trait and anatomical/localization nodes

- **axially filamented:** METPO:1000705
- **periplasmic flagellum / endoflagellum / axial filament:** label-only pending exact ontology alignment
- **periplasmic space:** GO:0042597
- **bacterial-type flagellum:** GO:0009288
- **bacterial-type flagellum hook:** GO:0009424
- **bacterial-type flagellum basal body:** GO:0009425
- **cell outer membrane:** GO:0009279
- **plasma membrane:** GO:0005886
- **peptidoglycan-based cell wall:** GO:0009274
- **protoplasmic cylinder:** label-only
- **flagellar core filament; flagellar sheath; P-collar/periplasmic collar; C-ring/rotor; stator complex:** retain as label-only if an exact ontology term cannot be verified.

### Genes and proteins

- **FlaB/FlaB1/FlaB2/FlaB3:** core flagellins; paralog requirements are taxon-specific.
- **FlaA/FlaA1/FlaA2:** sheath-associated or basal filament proteins; function differs among genera.
- **FcpA, FcpB:** *Leptospira*-specific sheath/coiling proteins.
- **FlgE:** hook protein; *Treponema denticola* FlgE has self-catalytic intersubunit crosslinks that stabilize the hook. (nakamura2020spirocheteflagellaand pages 3-5)
- **MotA, MotB:** proton-conducting stator components.
- **FliG:** rotor/C-ring interaction protein; suitable as a mechanistic node, although the retrieved direct spirochete evidence is stronger for MotB, FliL, and the C-ring.
- **FliL and P-collar proteins:** motor scaffold/stator-recruitment machinery.
- **MreB:** morphology comparator in *Leptospira*, not a core cause of the axially filamented trait.
- **FlgM/σ28 regulatory module:** candidate regulatory branch requiring direct extraction from the 2023 *T. denticola* study before curation.

Protein identifiers should be assigned at the organism/strain level from UniProt during YAML implementation; a single generic UniProt CURIE would incorrectly collapse non-orthologous or paralog-specific functions.

### Processes and molecular functions

- bacterial-type flagellum assembly: GO:0044781
- bacterial-type flagellum-dependent cell motility: GO:0071973
- bacterial-type flagellum-dependent swimming motility: GO:0071977
- proton transmembrane transport: GO:1902600
- torque generation; stator recruitment; rotor conformational change; filament coiling; cell-body undulation; crawling; host-tissue dissemination: label-only where exact ontology alignment is uncertain.

### Chemicals, environmental factors, and assays

- **proton:** CHEBI:15378
- **proton motive force:** label-only process/energy state
- **CCCP:** CHEBI:3259; experimental protonophore/inhibitor
- **lipopolysaccharide:** CHEBI:16412; surface-adhesion node in leptospiral crawling
- **viscosity / viscoelastic or gel-like medium:** environmental/experimental factor; ENVO grounding should be assigned only to a particular habitat or material, not to viscosity itself.
- **cryo-electron tomography, cryo-EM, soft-agar motility, microscopy, optical trapping:** experimental-factor or assay nodes, not biological causes.

### Taxon contexts

Use organism-specific contexts rather than universalizing edges: *Borrelia burgdorferi*, *Brachyspira hyodysenteriae*, *Leptospira interrogans*, *Leptospira biflexa*, and *Treponema denticola*. NCBITaxon CURIEs should be resolved against the exact species/strain record at curation time; none should be guessed.

## 3. Candidate causal edges

The following compact table identifies the highest-value core edges.

| subject | predicate | object | taxon/context | evidence strength |
|---|---|---|---|---|
| FlaB | forms | periplasmic flagellar core filament | Spirochetes; explicit in *B. burgdorferi*, *Brachyspira hyodysenteriae*, *Leptospira* spp. (nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 1-3) | Strong review synthesis |
| FcpA | contributes to / is a major component of | periplasmic flagellar sheath and filament coiling | *Leptospira* spp.; supported by knockout and interaction data summarized in review (nakamura2020spirocheteflagellaand pages 3-5) | Moderate, taxon-specific |
| FcpB | localizes to / contributes to | outer-curve sheath region and periplasmic flagellar coiling | *Leptospira* spp.; cryo-EM-based localization summarized in review (nakamura2020spirocheteflagellaand pages 3-5) | Moderate, taxon-specific |
| FlgE hook | connects | flagellar motor to filament for torque transmission | Spirochetes generally; hook corresponds to universal-joint-like connector (nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 1-3) | Moderate review-based |
| periplasmic collar + FliL | recruits / provides locations for assembly of | 16 stator units around the motor | *Borrelia burgdorferi* motor (chang2019structuralinsightsinto pages 10-12) | Strong primary, taxon-specific |
| MotB proton conduction | enables | torque-dependent C-ring conformational changes and flagellar rotation | *Borrelia burgdorferi* motB-D24E / motB-D24N mutants (chang2019structuralinsightsinto pages 10-12) | Strong primary, taxon-specific |
| periplasmic flagella rotation | drives | cell-body wave propagation or rolling/undulation for swimming thrust | Spirochetes generally; *Borrelia*, *Brachyspira*, *Leptospira* examples (nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 1-3) | Strong review synthesis |
| periplasmic flagella integrity | maintains | wavy/spiral cell morphology | Spirochetes generally; loss of PF straightens *B. burgdorferi* and alters *Leptospira* cell ends (nakamura2020spirocheteflagellaand pages 3-5) | Strong review synthesis |
| proton motive force | drives | *Leptospira* crawling via PF-dependent rotation | *Leptospira* on surfaces; CCCP-sensitive crawling summarized in review (nakamura2020spirocheteflagellaand pages 9-11) | Moderate, taxon-specific |


*Table: This table summarizes the strongest candidate causal edges for the axially filamented trait, emphasizing directly supported mechanistic relations and marking where evidence is taxon-specific or review-derived.*

Additional curation-ready detail follows. Quoted snippets are short extracts or closely delimited wording from the retrieved sources.

| Subject | Predicate | Object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|---|
| periplasmic flagellum | located in | periplasmic space | 10.3390/biom10040550 | “their flagella are hidden within the periplasmic space” | **High confidence; defining edge.** General for the reviewed spirochetes. (nakamura2020spirocheteflagellaand pages 1-3) |
| periplasmic flagellum | connects via FlgE hook to | basal flagellar motor | 10.3390/biom10040550 | “Each PF filament connects with a basal motor…via a short, bent structure corresponding to the universal joint hook” | **High confidence anatomical edge.** (nakamura2020spirocheteflagellaand pages 1-3) |
| FlaB | forms | PF core filament | 10.3390/biom10040550 | “FlaB forms the entire PF filament” in *B. burgdorferi*; three FlaB proteins form the *Brachyspira* core | **Strong but taxon-dependent composition.** Do not assert that every FlaB paralog is individually necessary. (nakamura2020spirocheteflagellaand pages 3-5) |
| flaB1 + flaB2 loss | decreases | PF synthesis and swimming motility | 10.3390/biom10040550 | synthesis and motility are affected by “double knockout of flaB1-flaB2” but not the stated alternative knockouts | **Review-derived perturbation evidence; *B. hyodysenteriae*-specific.** Supports redundancy/compensation. (nakamura2020spirocheteflagellaand pages 3-5) |
| FlaA sheath + FlaB core association | determines | mature PF helical morphology | 10.3390/biom10040550 | their association “determines the morphology of the fully assembled PFs” | **Strong review synthesis; *B. hyodysenteriae*-specific.** Core: 2.4-µm wavelength/0.6-µm diameter; assembled PF: 2.8/0.9 µm. (nakamura2020spirocheteflagellaand pages 3-5) |
| FcpA | forms/contributes to | leptospiral PF sheath | 10.3390/biom10040550 | “fcpA knockout mutants lack a sheath”; FcpA interacts with FlaB1 and FlaA2 | **High-value, taxon-specific.** Predicate “contributes to assembly of” is safer than universal “is the sheath.” (nakamura2020spirocheteflagellaand pages 3-5) |
| FcpA–core interaction | promotes | leptospiral PF coiling | 10.3390/biom10040550 | FcpA “plays a central role in coiling via its interaction with the core filament” | **Moderate; review interpretation.** (nakamura2020spirocheteflagellaand pages 3-5) |
| FcpB | localizes to | outer curve of PF sheath | 10.3390/biom10040550 | cryo-EM revealed FcpB “localized along the outer curve of the PF” | **Moderate structural edge; *Leptospira*-specific.** (nakamura2020spirocheteflagellaand pages 3-5) |
| PF sheath | enables | bending/coiling of leptospiral PF core | 10.3390/biom10040550 | “the core filament is straight in the absence of a sheath” | **Strong morphology mechanism, taxon-specific.** (nakamura2020spirocheteflagellaand pages 3-5) |
| FlgE hook | transmits | motor torque to PF filament | 10.3390/biom10040550 | the hook functions as a universal joint “to transmit the torque generated by the basal motor to the filament” | **Conserved-mechanism inference.** Direct wording is explained with the canonical motor; spirochetal FlgE composition is supported, but avoid claiming identical elasticity. (nakamura2020spirocheteflagellaand pages 3-5) |
| P-collar + FliL | recruits | 16 stator units | 10.7554/eLife.48979 | “the large periplasmic collar and FliL help to recruit sixteen stator units” | **Strong primary cryo-ET evidence; *B. burgdorferi*-specific.** (chang2019structuralinsightsinto pages 10-12) |
| MotB proton conduction | increases | stator occupancy | 10.7554/eLife.48979 | occupancy fell to **65%** in less-motile MotB-D24E and **45%** in nonmotile MotB-D24N motors | **Strong primary perturbation edge.** Phrase as graded association/requirement, because stators remain partially bound without conduction. (chang2019structuralinsightsinto pages 10-12) |
| proton flux through stator | generates | torque | 10.7554/eLife.48979 | “the torque induced by proton flux is required” | **Strong primary mechanistic conclusion.** (chang2019structuralinsightsinto pages 10-12) |
| stator-generated torque | causes | C-ring conformational change | 10.7554/eLife.48979 | MotB-D24E versus D24N produced a **3.4°** versus **1.2°** tilt change; stator binding alone was insufficient | **Strong primary structural edge; *B. burgdorferi*.** (chang2019structuralinsightsinto pages 10-12) |
| C-ring conformational change + torque | enables | PF rotation | 10.7554/eLife.48979 | stator–rotor interactions coupled to proton gradient trigger changes “required for flagellar rotation” | **Strong primary evidence.** (chang2019structuralinsightsinto pages 10-12) |
| PF rotation | drives | cell-body wave propagation/rolling/undulation | 10.3390/biom10040550 | spirochetes swim by “rolling or undulation of a cell body driven by PFs rotation” | **High confidence process edge.** Mode differs among genera. (nakamura2020spirocheteflagellaand pages 1-3) |
| cell-body wave propagation | generates | swimming thrust | 10.3390/biom10040550 | in *Borrelia* and *Brachyspira*, PF rotation “drives wave propagation…providing thrust” | **Strong review synthesis.** (nakamura2020spirocheteflagellaand pages 3-5) |
| PF integrity | maintains | wavy cell morphology | 10.3390/biom10040550 | “loss of the PF in *B. burgdorferi* straightens the entire cell body” | **Strong, taxon-specific perturbation effect.** For *Leptospira*, restrict the effect to cell ends. (nakamura2020spirocheteflagellaand pages 3-5) |
| proton motive force | drives | PF-dependent leptospiral crawling | 10.3390/biom10040550 | crawling was “completely inhibited by CCCP” | **Moderate; inhibitor-based and assay-specific.** CCCP may have pleiotropic effects, although the interpretation is consistent with proton-driven motors. (nakamura2020spirocheteflagellaand pages 9-11) |
| LPS-mediated adhesion + PF-dependent rolling | enables | surface crawling | 10.3390/biom10040550 | LPS serves as an adhesin, and “PF-dependent rolling…propels the cell” | **Leptospira- and surface-assay-specific; downstream of the morphology trait.** (nakamura2020spirocheteflagellaand pages 9-11) |
| PF-dependent motility | promotes | host dissemination/pathogenicity | 10.3390/biom10040550 | loss of flagellar genes attenuates infection in *B. burgdorferi*, *B. hyodysenteriae*, and *L. interrogans* | **Biologically important but broad and review-derived.** Curate as separate taxon-specific edges to measured infection outcomes, not a universal PF→virulence edge. (nakamura2020spirocheteflagellaand pages 9-11) |

## 4. Current understanding and recent developments

### Structural and mechanical consensus

The modern view treats PFs as both propulsive and, in many species, cytoskeletal elements. Their mechanical interaction with the cell cylinder accounts for species-specific waveforms. The filament is not simply an internal version of an external propeller: it transmits force to the envelope and cell body, which then interact with the environment. Direct observation of PF rotation remained unresolved in the 2020 review, so the rotation-to-cell-deformation model rests on convergent genetic, structural, and biophysical evidence rather than direct visualization of every intermediate. (nakamura2020spirocheteflagellaand pages 3-5)

Cryo-ET of *B. burgdorferi* established a particularly strong motor mechanism. The collar and FliL provide 16 stator positions; proton-channel MotB mutants retain some stators but lose occupancy, torque-linked C-ring deformation, and motility. This distinguishes **stator binding** from **productive proton conduction and torque generation**. The primary study was published in July 2019 (DOI [10.7554/eLife.48979](https://doi.org/10.7554/eLife.48979)). (chang2019structuralinsightsinto pages 10-12)

### 2023–2024 literature assessment

The principal recent synthesis is San Martin et al., **“Diving into the complexity of the spirochetal endoflagellum,”** *Trends in Microbiology* 31:294–307, published March 2023 (online 2022), DOI [10.1016/j.tim.2022.09.010](https://doi.org/10.1016/j.tim.2022.09.010). It is highly relevant to current architecture and diversity, but full-text evidence was not retrievable in this search; it should be manually reviewed before using it as evidence for new YAML edges.

A 2023 primary paper reported that anti-σ28 factor FlgM regulates flagellin expression and flagellar polarity in *T. denticola*: Kurniyati et al., *Journal of Bacteriology*, published February 2023, DOI [10.1128/jb.00463-22](https://doi.org/10.1128/jb.00463-22). Because only bibliographic metadata was retrieved, the precise FlgM→flagellin/polarity triples should be treated as **candidates requiring full-text verification**, not curated from this report.

The retrieved 2024 mBio work on *C. jejuni* showed contemporary interest in viscosity-sensitive motor control and quantified high-viscosity swimming at approximately **50–100 µm/s**, but *C. jejuni* has external polar flagella. VidA/VidB and its viscosity mechanism therefore must **not** be imported into the axial-filament causal graph; it is only a comparative flagellar-motor example (published January 2024; DOI [10.1128/mbio.02544-23](https://doi.org/10.1128/mbio.02544-23)). (ribardo2024viscositydependentdeterminantsof pages 1-2)

## 5. Quantitative findings

- PF abundance and layout vary markedly: **14–22 overlapping** PFs in *B. burgdorferi*, **16–18 overlapping** in *B. hyodysenteriae*, and **2 non-overlapping** PFs in *L. interrogans*. (nakamura2020spirocheteflagellaand pages 1-3)
- The spirochetal rotor ring is comparatively large: approximately **31 nm** in *B. burgdorferi*, versus approximately 20 nm in *Salmonella*, 22 nm in *Vibrio fischeri*, and 27 nm in *C. jejuni*. (nakamura2020spirocheteflagellaand pages 3-5)
- Estimated/measured stall torque is approximately **4,000 pN·nm** for *Leptospira*, versus approximately **2,000 pN·nm** for *E. coli*. This supports—but does not alone prove—the proposal that enlarged, fully occupied spirochetal motors are high-torque machines. (nakamura2020spirocheteflagellaand pages 3-5)
- In *B. burgdorferi*, MotB-D24E and MotB-D24N motors showed approximately **65%** and **45%** stator occupancy, respectively; the mutants were less motile and nonmotile. (chang2019structuralinsightsinto pages 10-12)
- In *B. hyodysenteriae*, the FlaB core has a wavelength/diameter of approximately **2.4/0.6 µm**, whereas the assembled core–sheath filament measures approximately **2.8/0.9 µm**, directly linking sheath association to filament geometry. (nakamura2020spirocheteflagellaand pages 3-5)

## 6. Applications and authoritative interpretation

1. **Pathogenesis and antimicrobial discovery.** PF assembly, stator energization, and motility are candidate intervention points in Lyme disease, leptospirosis, syphilis, and swine dysentery. However, essentiality and accessibility differ by organism, and the periplasmic location may complicate drug delivery. Motility loss attenuates infection in several experimental systems, but “PF causes virulence” is too coarse for curation. (nakamura2020spirocheteflagellaand pages 9-11)
2. **Diagnostic and phenotypic identification.** Dark-field microscopy, cryo-ET, and motility morphology can support spirochete identification. Definitive assignment of METPO:1000705 should rely on ultrastructural localization or equivalent evidence rather than waveform alone.
3. **Host-tissue mechanics.** *B. burgdorferi* displays translocating, wriggling, and lunging states in dermis-like environments; translocation supports dissemination, while transient adhesion may aid reorientation. These behaviors are downstream ecological manifestations, not definitional trait components. (nakamura2020spirocheteflagellaand pages 9-11)
4. **Biomimetics.** The internal rotary mechanism, efficient movement in confined or gel-like environments, and deformable body have been proposed as design principles for autonomous microrobots. This remains a translational concept rather than a mature real-world implementation. (nakamura2020spirocheteflagellaand pages 1-3)
5. **Structural biology.** In situ cryo-ET offers a real-world experimental implementation for resolving motor occupancy and torque-dependent conformations directly in intact cells. (chang2019structuralinsightsinto pages 10-12)

## 7. Recommended minimal TraitMech graph

For a conservative first revision of `axially_filamented.yaml`, prioritize these nodes and relations:

1. FlaB-containing PF filament — **located_in** → periplasmic space.
2. FlaB — **forms_part_of** → PF core.
3. PF core — **surrounded_or_modified_by** → sheath *(only in explicitly supported taxa)*.
4. FcpA/FcpB — **contributes_to** → sheath/coiling *(Leptospira context)*.
5. PF filament — **connected_via** → FlgE hook → basal motor.
6. P-collar/FliL — **promotes_assembly_of** → stator complex *(*B. burgdorferi* context)*.
7. proton transmembrane flow through MotA/MotB — **generates** → stator torque.
8. stator torque — **induces** → rotor/C-ring conformational change and PF rotation.
9. PF rotation — **causes** → cell-body rolling/undulation.
10. cell-body rolling/undulation — **enables** → swimming/crawling.
11. PF integrity — **contributes_to** → species-specific cell morphology.

This graph preserves the morphology trait’s core while allowing taxon-specific extension modules for *Borrelia*, *Brachyspira*, *Leptospira*, and *Treponema*.

## 8. Warnings: claims not yet ready for curation

- Do not equate **axially filamented** with “spirochete,” “helical,” or “motile.”
- Do not import VidA/VidB or high-viscosity *C. jejuni* results into this trait; that organism’s filaments are external. (ribardo2024viscositydependentdeterminantsof pages 1-2)
- Do not assert a universal FlaA–FlaB–Fcp sheath. Composition and localization differ by genus. (nakamura2020spirocheteflagellaand pages 3-5)
- Do not assign all FlaB paralogs identical necessity; *Brachyspira* knockout results indicate partial functional compensation. (nakamura2020spirocheteflagellaand pages 3-5)
- Do not curate direct PF rotation as visually observed; the 2020 review explicitly notes that direct observation had not succeeded. (nakamura2020spirocheteflagellaand pages 3-5)
- Treat CCCP→loss of crawling as inhibitor-based evidence, not proof that PMF acts only through PFs. (nakamura2020spirocheteflagellaand pages 9-11)
- Keep PF→virulence, PF→tissue penetration, and viscosity→enhanced infection as uncertain downstream edges until supported by organism-specific primary experiments and defined endpoints.
- Do not curate the 2023 FlgM regulatory edges until the full paper is inspected for mutant, complementation, expression, and polarity evidence.
- Verify every proposed GO, CHEBI, NCBITaxon, and UniProt identifier in the target repository’s ontology release before committing; label-only nodes are preferable to invented or overly broad CURIEs.

## DOI-first bibliography

1. **San Martin F, Fule L, Iraola G, Buschiazzo A, Picardeau M.** “Diving into the complexity of the spirochetal endoflagellum.” *Trends in Microbiology* 31:294–307. **March 2023**. DOI: [10.1016/j.tim.2022.09.010](https://doi.org/10.1016/j.tim.2022.09.010). Recent authoritative review; full text not retrieved here.
2. **Kurniyati K, Chang Y, Guo W, Liu J, Malkowski MG, Li C.** “Anti-σ28 factor FlgM regulates flagellin gene expression and flagellar polarity of *Treponema denticola*.” *Journal of Bacteriology*. **February 2023**. DOI: [10.1128/jb.00463-22](https://doi.org/10.1128/jb.00463-22). Recent primary study; metadata only in this retrieval.
3. **Nakamura S.** “Spirochete Flagella and Motility.” *Biomolecules* 10:550. **4 April 2020**. DOI: [10.3390/biom10040550](https://doi.org/10.3390/biom10040550). Core accessible synthesis of localization, filament architecture, mechanics, and virulence. (nakamura2020spirocheteflagellaand pages 3-5, nakamura2020spirocheteflagellaand pages 1-3, nakamura2020spirocheteflagellaand pages 9-11)
4. **Chang Y, Moon KH, Zhao X, et al.** “Structural insights into flagellar stator–rotor interactions.” *eLife* 8:e48979. **July 2019**. DOI: [10.7554/eLife.48979](https://doi.org/10.7554/eLife.48979). Primary cryo-ET and MotB-mutant evidence. (chang2019structuralinsightsinto pages 10-12)
5. **Ribardo DA, Johnson JJ, Hendrixson DR.** “Viscosity-dependent determinants of *Campylobacter jejuni* impacting the velocity of flagellar motility.” *mBio* 15(1). **January 2024**. DOI: [10.1128/mbio.02544-23](https://doi.org/10.1128/mbio.02544-23). Comparative external-flagellum study; not direct evidence for METPO:1000705. (ribardo2024viscositydependentdeterminantsof pages 1-2)

**Overall curation judgment:** the defining localization edge and the motor-to-morphology/motility backbone are well supported. The safest expansion beyond the existing 10-node graph is to add explicit **core–sheath organization**, **hook coupling**, and **proton-driven stator–rotor mechanics**, while representing Fcp proteins, morphology effects, crawling, and virulence in taxon-specific subgraphs with uncertainty annotations.

References

1. (nakamura2020spirocheteflagellaand pages 1-3): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 70 citations.

2. (nakamura2020spirocheteflagellaand pages 3-5): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 70 citations.

3. (nakamura2020spirocheteflagellaand pages 9-11): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 70 citations.

4. (chang2019structuralinsightsinto pages 10-12): Yunjie Chang, Ki Hwan Moon, Xiaowei Zhao, Steven J Norris, MD A Motaleb, and Jun Liu. Structural insights into flagellar stator–rotor interactions. eLife, Jul 2019. URL: https://doi.org/10.7554/elife.48979, doi:10.7554/elife.48979. This article has 45 citations and is from a domain leading peer-reviewed journal.

5. (ribardo2024viscositydependentdeterminantsof pages 1-2): Deborah A. Ribardo, Jeremiah J. Johnson, and David R. Hendrixson. Viscosity-dependent determinants of <i>campylobacter jejuni</i> impacting the velocity of flagellar motility. Jan 2024. URL: https://doi.org/10.1128/mbio.02544-23, doi:10.1128/mbio.02544-23. This article has 8 citations and is from a domain leading peer-reviewed journal.