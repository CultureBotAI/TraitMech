---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:58:50.610681'
end_time: '2026-08-04T10:05:45.877709'
duration_seconds: 415.27
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: spirochete shaped
  trait_identifier: METPO:1000693
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spirochete_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has an elongated, tightly coiled helical
    morphology with periplasmic flagella (endoflagella) located between the cell wall
    and outer membrane.
  parent_traits: METPO:1000666
  synonyms: spirochete
  evidence_summary: 'DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in
    part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder
    and periplasmic-flagella interaction.)'
  causal_graph_summary: 'spirochete_shaped_periplasmic_flagella: 11 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spirochete shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000693
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.
- **Parent traits:** METPO:1000666
- **Synonyms:** spirochete
- **Existing evidence:** DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder and periplasmic-flagella interaction.)
- **Existing causal graph summary:** spirochete_shaped_periplasmic_flagella: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **spirochete shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spirochete_shaped.yaml`.

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
- **Trait label:** spirochete shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000693
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an elongated, tightly coiled helical morphology with periplasmic flagella (endoflagella) located between the cell wall and outer membrane.
- **Parent traits:** METPO:1000666
- **Synonyms:** spirochete
- **Existing evidence:** DOI:10.1073/pnas.200221797: periplasmic flagella ... confer in part its flat-wave morphology (Supports spirochete morphology as a cell-cylinder and periplasmic-flagella interaction.)
- **Existing causal graph summary:** spirochete_shaped_periplasmic_flagella: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **spirochete shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spirochete_shaped.yaml`.

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


# Curation report: **spirochete shaped**

## Target record

- **Trait label:** spirochete shaped
- **Trait identifier:** `METPO:1000693`
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000666`
- **Synonym:** spirochete
- **Working definition:** an elongated spiral, corkscrew-like, or flat-wave cell-body morphology associated with periplasmic flagella situated between the peptidoglycan-bearing cell cylinder and outer membrane.

## 1. Scope and current mechanistic understanding

The trait should denote **whole-cell morphology**, not taxonomic membership in Spirochaetota and not motility alone. The most defensible common mechanism is mechanical coupling between a flexible or rigid peptidoglycan-bearing cell cylinder and internally located periplasmic flagella. The flagella act as both motility organelles and shape-generating cytoskeletal elements. In *Borrelia burgdorferi*, they impose a planar flat-wave form; *Leptospira interrogans* instead has a right-handed helical cylinder with dynamically hook- or spiral-shaped ends; other spirochetes differ in wavelength, handedness, rigidity, and flagellar number. A review reports 7–11 overlapping periplasmic flagella in *B. burgdorferi*, 16–18 in *Brachyspira hyodysenteriae*, but only two non-overlapping flagella in *L. interrogans*. Thus, “tightly coiled helix” is too narrow if the term is intended to include canonical flat-wave *Borrelia*. (nakamura2020spirocheteflagellaand pages 1-3)

In *B. burgdorferi*, flagellar bundles originate subterminally at both poles and extend inward between the cell cylinder and outer membrane. Oppositely directed bundle rotation produces backward-propagating waves in the cell body. The primary literature explicitly states that periplasmic flagella are “critical in providing the characteristic flat-wave morphology.” (sal2008borreliaburgdorferiuniquely pages 1-2)

Cryo-electron tomography of *Treponema pallidum* supports a complementary envelope mechanism: the peptidoglycan layer maintains cell-cylinder integrity and “serves as the interface between the rotating flagella and cell cylinder.” The authors infer that without this layer the fragile cell body could not withstand flagellar friction and torque. This is strong structural-mechanical evidence, but not a peptidoglycan-loss experiment and should therefore be qualified as an inferred interface edge. (liu2010cellulararchitectureof pages 8-9)

### Boundary cases

1. **Generic helical bacteria are not necessarily spirochete-shaped.** Externally flagellated curved or helical bacteria lack the defining periplasmic flagellum–cell-cylinder architecture.
2. **Flat-wave forms belong in scope.** *Borrelia* is described experimentally as flat-wave rather than a tightly coiled cylindrical helix. (sal2008borreliaburgdorferiuniquely pages 1-2)
3. **Flagellar-filament supercoiling is not the target phenotype.** It is an upstream structural state that can deform the cell body.
4. **Hook- and spiral-shaped ends are taxon-specific substates.** These are especially diagnostic of *Leptospira*, not universal spirochete morphology. (wunder2018fcpbisa pages 6-7)
5. **Motility is distinct.** Nonmotility can follow loss of morphology machinery, but an edge to motility does not by itself establish an edge to whole-cell shape.
6. **Cell length, chaining, and failed cytokinesis are distinct phenotypes.** They can accompany flagellar defects without demonstrating loss of helicity.

## 2. Candidate nodes and ontology grounding

### Trait and cellular-structure nodes

- `METPO:1000693` — spirochete shaped.
- Periplasmic flagellum / endoflagellum — use a verified GO cellular-component term if available in the curation environment; otherwise retain as a label-only node rather than assigning an unverified CURIE.
- Flagellar filament; hook; basal body; motor; rotor; stator; spirochete-specific collar.
- Periplasmic flagellar bundle/ribbon.
- Cell cylinder or protoplasmic cylinder.
- Peptidoglycan layer — `GO:0009274` is a candidate GO cellular-component grounding, subject to local ontology validation.
- Periplasmic space — `GO:0042597` is a candidate grounding.
- Outer membrane — `GO:0019867` is a candidate grounding.
- Cytoplasmic membrane — `GO:0005886` is a candidate grounding.
- Flat-wave whole-cell morphology; helical/corkscrew whole-cell morphology; hook-shaped end; spiral-shaped end; rod-shaped loss-of-shape phenotype. These may need label-only or METPO-specific nodes.

### Genes and proteins

- **FlaB:** major flagellin/core-filament protein. Exact gene copies and functions vary by taxon.
- **FlaA:** minor flagellin or filament-associated protein; composition and role vary substantially among spirochetes.
- **FlgE:** flagellar hook structural protein.
- **FcpA:** *Leptospira* flagellar sheath protein.
- **FcpB:** *Leptospira* flagellar-coiling/sheath protein.
- **FlgV / BB0268:** basal-body-associated structural component in *B. burgdorferi*.
- **DnaA:** replication initiator and pleiotropic transcriptional regulator; only an indirect/contextual morphology candidate.
- **CfpA:** treponemal cytoplasmic-filament protein; evidence for a direct conserved shape role remains insufficient.
- **FlbB and collar proteins:** promising *Borrelia*-specific motor/collar nodes, but the retrieved direct evidence was inadequate for a fully resolved edge in the present graph.

Stable protein accessions should be assigned **per species and strain** from UniProt during implementation. A bare symbol such as `flaB` should not be mapped to one universal protein identifier.

### Processes and mechanical states

- Periplasmic flagellum assembly.
- Flagellar filament supercoiling/curvature.
- Flagellar rotation.
- Flagellum–cell-cylinder mechanical interaction.
- Cell-body deformation and wave propagation.
- Translational motility and cell-cylinder rolling—downstream phenotypes, not synonyms of shape.
- Cell division/separation—contextual because some flagellar perturbations produce elongated or conjoined cells.

### Chemicals and environmental or experimental factors

No specific nutrient, electron donor, acceptor, or metabolic pathway is established as a proximal determinant of this morphology. Relevant experimental factors include targeted deletion, CRISPR interference, complementation, protein overexpression, medium viscosity, dark-field microscopy, negative-stain EM, and cryo-electron tomography. Viscosity changes locomotor performance and waveform dynamics, but current evidence does not establish it as a cause of the constitutive trait itself.

## 3. Candidate causal graph

The following table separates whole-cell morphology evidence from filament geometry, motility, and division phenotypes.

| subject node | predicate | object node | taxon | evidence class/confidence | key qualification |
|---|---|---|---|---|---|
| FlgE (flagellar hook protein) | enables assembly of | periplasmic flagellum | *Borrelia burgdorferi* | direct perturbation; high (sal2008borreliaburgdorferiuniquely pages 1-2, sal2008borreliaburgdorferiuniquely pages 2-2) | `flgE` mutants “lacked PFs, were rod shaped, and were nonmotile”; whole-cell-shape outcome observed directly, but edge is specifically PF assembly → downstream shape loss |
| periplasmic flagella | confers | flat-wave whole-cell morphology | *Borrelia burgdorferi* | direct perturbation/foundational; high (sal2008borreliaburgdorferiuniquely pages 1-2) | Source states PFs are “critical in providing the characteristic flat-wave morphology”; whole-cell morphology, not merely filament shape |
| FcpA (flagellar sheath protein) | supports | coiled periplasmic flagellum morphology | *Leptospira interrogans* | direct knockout + cryo-ET; high (wunder2016anovelflagellar pages 7-8, wunder2016anovelflagellar pages 8-9) | `fcpA` inactivation reduced PF diameter from 20.5 nm to 15.7 nm and produced straight/thinner PF; filament-shape outcome |
| FcpA (flagellar sheath protein) | supports | hook-shaped cell ends / translational spirochete morphology | *Leptospira interrogans* | direct knockout; high (wunder2016anovelflagellar pages 7-8) | Whole-cell-shape outcome: loss of hook-shaped ends and translational motility; taxon-specific Leptospira end morphology rather than generic all-spirochete shape |
| FcpB (flagellar-coiling protein B) | supports | coiled periplasmic flagellum morphology | *Leptospira biflexa* / *Leptospira interrogans* | direct mutant + EM; high (wunder2018fcpbisa pages 6-7) | `fcpB−` PF were “unusually straight” and lacked tightly wound coiling; filament-shape outcome |
| FcpB (flagellar-coiling protein B) | supports | hook-/spiral-shaped cell ends | *Leptospira biflexa* / *Leptospira interrogans* | direct mutant microscopy; high (wunder2018fcpbisa pages 6-7) | Whole-cell-shape outcome: mutant was deficient in forming hook- and spiral-shaped ends; specific to Leptospira end morphology |
| asymmetric FcpA/FcpB sheath | increases curvature of | periplasmic flagellar filament | *Leptospira* sp. | direct structural/quantitative; high (gibson2020anasymmetricsheath pages 11-13, gibson2020anasymmetricsheath pages 10-11) | Filament-shape edge, not directly whole-cell-shape edge; WT curvature ~5 mm⁻¹ vs reduced curvature in sheath mutants |
| peptidoglycan layer of cell cylinder | interfaces with | rotating periplasmic flagella | *Treponema pallidum* (likely broader spirochetes) | structural inference from cryo-ET; medium-high (liu2010cellulararchitectureof pages 8-9) | Source says PG “serves as the interface between the rotating flagella and cell cylinder”; mechanistically plausible broad spirochete principle, but directly shown in *T. pallidum* |
| FlgV | modulates assembly of | flagellar filaments (number/length) | *Borrelia burgdorferi* | direct 2024 perturbation; medium (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 4-6, zambacampero2024broadlyconservedflgv pages 7-10) | Deletion/overexpression changed filament number and length and caused division/motility defects; no direct demonstrated edge to loss of flat-wave/helical morphology in cited text |
| FlgV | affects | cell division / spirochete length | *Borrelia burgdorferi* | direct 2024 perturbation; medium (zambacampero2024broadlyconservedflgv pages 4-6) | Longer, conjoined cells with septa were observed; contextual for morphology graph but primarily a division phenotype |
| DnaA depletion | causes abnormality of | corkscrew/helical whole-cell morphology | *Borrelia burgdorferi* | direct but pleiotropic preprint; medium/uncertain (krusenstjerna2024dnaamodulatesthe pages 10-13) | About 13% induced cells showed complete/partial loss of corkscrew shape; likely indirect/global regulatory effect, not a clean morphology-specific mechanism |
| DnaA | modulates expression of | elongasome/divisome and flagellar-homeostasis-related functions | *Borrelia burgdorferi* | transcriptomic/pleiotropic preprint; uncertain (krusenstjerna2024dnaamodulatesthe pages 10-13) | Useful context only; should not yet be curated as a direct conserved morphology mechanism without stronger causally resolved evidence |


*Table: This table summarizes candidate causal edges for curating METPO:1000693, separating high-confidence direct morphology mechanisms from contextual or uncertain regulators. It is designed to help decide which nodes and edges are safe to include now versus defer pending stronger evidence.*

### Recommended minimal high-confidence backbone

A conservative first implementation could contain the following chain:

1. **FlgE → enables assembly of → periplasmic flagella** in *B. burgdorferi*.
2. **FlaB-containing flagellar filament → part of → periplasmic flagella**.
3. **Periplasmic flagella → mechanically interact with → peptidoglycan-bearing cell cylinder**.
4. **Periplasmic flagella–cell-cylinder interaction → confers → spirochete-shaped/flat-wave morphology**.
5. **Loss of periplasmic flagella → causes → rod-shaped morphology** in *B. burgdorferi*.

The key intervention is the *B. burgdorferi flgE* mutant: it “lacked PFs, [was] rod shaped, and [was] nonmotile,” while FlaA and FlaB levels were markedly reduced. This directly joins hook assembly, flagellum presence, and whole-cell shape, although the downstream FlaA/FlaB reductions mean FlgE should connect first to assembly rather than directly to morphology. (sal2008borreliaburgdorferiuniquely pages 1-2)

### Taxon-specific *Leptospira* branch

- **FcpA → supports → flagellar sheath structure/coiling.** In an *L. interrogans fcpA* mutant, filament diameter fell from **20.5 nm to 15.7 nm**; the mutant lost normal hook-ended morphology and translational motility. Complementation restored relevant phenotypes. (wunder2016anovelflagellar pages 7-8)
- **FcpB → supports → asymmetric filament sheath and curvature.** The *L. biflexa fcpB* mutant was deficient in hook- and spiral-shaped ends, and purified filaments were unusually straight. The mutant filament was approximately **170 Å**, versus approximately **200 Å** for wild type, owing to missing density on the convex side. (wunder2018fcpbisa pages 6-7)
- **Asymmetric FcpA/FcpB sheath → increases → filament curvature.** Structural analysis measured wild-type curvature near **5 mm⁻¹**, versus approximately **3 mm⁻¹** after FcpA loss, with thinner populations near **2 mm⁻¹**. The sheathed and unsheathed filament diameters were approximately **170 Å** and **120 Å**, respectively. These values describe filament geometry, not cell-body pitch. (gibson2020anasymmetricsheath pages 11-13, gibson2020anasymmetricsheath pages 10-11)
- **Coiled/stiff periplasmic filament → bends → cell ends.** This is supported by mutant morphology and complementation, but dynamic claims assigning hook versus spiral state to clockwise versus counterclockwise rotation remain partly biophysical-model dependent. (wunder2018fcpbisa pages 6-7)

FcpA and FcpB should be represented in a **Leptospira-specific subgraph**, not as universal causes of `METPO:1000693`. FcpB is reported as conserved within *Leptospira* but absent from other organisms, including other spirochetes. (wunder2018fcpbisa pages 6-7)

## 4. Recent developments, 2023–2024

### FlgV reannotation and flagellar assembly

A November 2024 *Nature Communications* study reannotated *B. burgdorferi* BB0268—previously described as an atypical Hfq homolog—as **FlgV**, a two-transmembrane flagellar structural component. FlgV localizes near the C and MS rings of the basal body. Deletion produced fewer and shorter filaments, division defects, and impaired motility; altered FlgV dosage also increased cell length during exponential growth. (zambacampero2024broadlyconservedflgv pages 1-2, zambacampero2024broadlyconservedflgv pages 4-6)

Cryo-ET counts provide useful graph evidence. At one pole, deletion reduced mean filament number from **8.2** in wild type to **6.7**, while complementation gave **8.5**; basal-body means remained similar at **8.2**, **7.7**, and **8.4**, respectively. Overexpression produced only **4.2** filaments on average versus **9.2** in its wild-type control. These data support `FlgV → modulates → flagellar filament assembly`, but the retrieved evidence does **not** show conversion from flat-wave to rod shape. FlgV should therefore not yet be connected directly to `METPO:1000693`. (zambacampero2024broadlyconservedflgv pages 7-10)

The same work links flagellar regulation to real-world infection biology: *flgV*-deficient bacteria survived and replicated in *Ixodes* ticks but were attenuated for mouse infection and dissemination. This is important downstream evidence, not evidence that morphology alone causes virulence. The paper also notes an estimated **nearly half a million Lyme disease infections annually in the United States**, emphasizing the biomedical relevance of this motility machinery. (zambacampero2024broadlyconservedflgv pages 1-2)

### DnaA as an indirect morphology regulator

A June 2024 bioRxiv preprint used inducible CRISPRi to deplete DnaA in *B. burgdorferi*. Approximately **13%** of induced cells and **8.7%** of uninduced knockdown cells showed complete or partial loss of the characteristic corkscrew morphology; some became elongated tubes with incomplete division. DnaA depletion also perturbed chromosome partitioning and altered expression of many replication, elongasome/divisome, and flagellar genes. (krusenstjerna2024dnaamodulatesthe pages 10-13)

This supports the qualified edge `DnaA depletion → causes → abnormal helicity`, but not a direct structural role for DnaA. The result is pleiotropic, affected by leaky CRISPRi expression, and was a preprint in the retrieved 2024 source. It should be placed in a provisional regulatory branch or omitted from the production graph pending peer-reviewed validation and mediator-resolving experiments.

### Current structural consensus

The 2024 literature continues to frame spirochetal periplasmic flagella as cytoskeletal as well as propulsive structures. The most mature interpretation is therefore a multiscale mechanism: assembly proteins create a polar motor–hook–filament apparatus; filament composition establishes curvature and stiffness; the periplasmic bundle presses against the peptidoglycan-bearing cylinder; and that mechanical coupling generates the stable flat-wave or helical cell shape and, upon rotation, propagating waves or rolling motion. (nakamura2020spirocheteflagellaand pages 1-3, liu2010cellulararchitectureof pages 8-9, sal2008borreliaburgdorferiuniquely pages 1-2)

## 5. Applications and expert analysis

### Infection and intervention targets

Morphology machinery is medically relevant because the same structures enable movement through viscous host environments. In *L. interrogans*, *fcpA* inactivation increased hamster LD50 by more than sevenfold, prevented infection through a mucosal route, and impaired translocation across polarized epithelial monolayers. These outcomes identify the sheath–filament system as a candidate anti-virulence target, although the experiments do not prove that altered shape, rather than impaired propulsion, is the operative cause. (wunder2016anovelflagellar pages 7-8)

The 2024 FlgV work similarly connects flagellar assembly to dissemination in mice. The practical implication is that basal-body and sheath proteins could support species-specific drug, vaccine, or diagnostic development. However, broad-spectrum targeting is complicated by marked compositional diversity: FcpA/FcpB are *Leptospira*-associated, whereas *Borrelia* uses a distinct filament and collar architecture. (wunder2018fcpbisa pages 6-7, zambacampero2024broadlyconservedflgv pages 1-2)

### Imaging and phenotype assays

Dark-field microscopy directly distinguishes flat-wave, helical, rod-shaped, and hook/spiral-end states. Cryo-ET resolves whether a phenotype arises from missing filaments, altered filament diameter or curvature, basal-body defects, or disrupted cell-envelope contacts. Negative-stain EM of purified flagella is valuable for filament geometry but cannot alone establish a whole-cell morphology edge. The strongest curation evidence combines genetic perturbation, whole-cell imaging, ultrastructure, and complementation, as in the FcpA and FcpB studies. (wunder2018fcpbisa pages 6-7, wunder2016anovelflagellar pages 7-8)

### Biomimetic engineering

Authoritative reviews propose that propulsion by internally confined rotating filaments in viscous fluids could inspire efficient autonomous microrobots. This remains a design concept rather than a mature real-world implementation, and it should not enter the causal graph. (nakamura2020spirocheteflagellaand pages 1-3)

## 6. Warnings and claims not ready for TraitMech

1. **Do not curate “all spirochetes are tightly coiled helices.”** Canonical *Borrelia* is flat-wave, and morphologies vary substantially among taxa.
2. **Do not equate flagellar-filament curvature with whole-cell morphology.** Keep intermediate nodes and explicit mechanical edges.
3. **Do not equate morphology with motility or virulence.** These are downstream, correlated phenotypes with possible independent contributions.
4. **Do not generalize FcpA/FcpB beyond *Leptospira*.** FcpB is explicitly lineage restricted. (wunder2018fcpbisa pages 6-7)
5. **Do not assign a direct FlgV-to-shape edge yet.** The 2024 data establish effects on filament number/length, cell division, length, motility, and dissemination, but not direct loss of helicity. (zambacampero2024broadlyconservedflgv pages 7-10, zambacampero2024broadlyconservedflgv pages 4-6)
6. **Treat DnaA as uncertain and indirect.** Its morphology phenotype is pleiotropic and reported in a preprint. (krusenstjerna2024dnaamodulatesthe pages 10-13)
7. **Treat peptidoglycan’s torque-bearing role as a structural inference.** Direct PG perturbation evidence was not retrieved. (liu2010cellulararchitectureof pages 8-9)
8. **Do not curate CfpA or the treponemal terminal cone as established universal shape determinants.** Their composition or exact morphology function remains unresolved. (liu2010cellulararchitectureof pages 8-9)
9. **Avoid unverified CURIEs.** Species-specific UniProt and NCBITaxon identifiers should be resolved programmatically during YAML implementation rather than inferred from gene names.
10. **Keep environmental viscosity outside the core constitutive graph** unless the intended trait is an assay-specific waveform or motility phenotype.

## 7. DOI-first bibliography

1. Zamba-Campero M. et al. “Broadly conserved FlgV controls flagellar assembly and *Borrelia burgdorferi* dissemination in mice.” *Nature Communications* 15, 10417. **Published November 2024.** DOI: [10.1038/s41467-024-54806-w](https://doi.org/10.1038/s41467-024-54806-w). (zambacampero2024broadlyconservedflgv pages 1-2)
2. Krusenstjerna A.C. et al. “DnaA modulates the gene expression and morphology of the Lyme disease spirochete.” bioRxiv. **Posted June 2024; preprint.** DOI: [10.1101/2024.06.08.598065](https://doi.org/10.1101/2024.06.08.598065). (krusenstjerna2024dnaamodulatesthe pages 10-13)
3. Nakamura S., Minamino T. “Structure and Dynamics of the Bacterial Flagellar Motor Complex.” *Biomolecules* 14, 1488. **Published November 2024.** DOI: [10.3390/biom14121488](https://doi.org/10.3390/biom14121488).
4. San Martin F. et al. “Diving into the complexity of the spirochetal endoflagellum.” *Trends in Microbiology* 31:294–307. **Published March 2023.** DOI: [10.1016/j.tim.2022.09.010](https://doi.org/10.1016/j.tim.2022.09.010).
5. Gibson K.H. et al. “An asymmetric sheath controls flagellar supercoiling and motility in the *Leptospira* spirochete.” *eLife* 9:e53672. **Published March 2020.** DOI: [10.7554/eLife.53672](https://doi.org/10.7554/eLife.53672). (gibson2020anasymmetricsheath pages 11-13)
6. Nakamura S. “Spirochete Flagella and Motility.” *Biomolecules* 10:550. **Published April 2020.** DOI: [10.3390/biom10040550](https://doi.org/10.3390/biom10040550). (nakamura2020spirocheteflagellaand pages 1-3)
7. Wunder E.A. et al. “FcpB Is a Surface Filament Protein of the Endoflagellum Required for the Motility of the Spirochete *Leptospira*.” *Frontiers in Cellular and Infection Microbiology* 8:130. **Published May 2018.** DOI: [10.3389/fcimb.2018.00130](https://doi.org/10.3389/fcimb.2018.00130). (wunder2018fcpbisa pages 6-7)
8. Wunder E.A. et al. “A novel flagellar sheath protein, FcpA, determines filament coiling, translational motility and virulence for the *Leptospira* spirochete.” *Molecular Microbiology* 101:457–470. **Published August 2016.** DOI: [10.1111/mmi.13403](https://doi.org/10.1111/mmi.13403). (wunder2016anovelflagellar pages 7-8)
9. Liu J. et al. “Cellular architecture of *Treponema pallidum*: novel flagellum, periplasmic cone, and cell envelope as revealed by cryo-electron tomography.” *Journal of Molecular Biology* 403:546–561. **Published November 2010.** DOI: [10.1016/j.jmb.2010.09.020](https://doi.org/10.1016/j.jmb.2010.09.020). (liu2010cellulararchitectureof pages 8-9)
10. Sal M.S. et al. “*Borrelia burgdorferi* uniquely regulates its motility genes and has an intricate flagellar hook-basal body structure.” *Journal of Bacteriology* 190:1912–1921. **Published March 2008.** DOI: [10.1128/JB.01421-07](https://doi.org/10.1128/JB.01421-07). (sal2008borreliaburgdorferiuniquely pages 1-2)
11. Motaleb M.A. et al. “*Borrelia burgdorferi* periplasmic flagella have both skeletal and motility functions.” *PNAS* 97:10899–10904. **Published September 2000.** DOI: [10.1073/pnas.200221797](https://doi.org/10.1073/pnas.200221797). This is the supplied foundational evidence for the existing graph and remains central to the conserved backbone.

References

1. (nakamura2020spirocheteflagellaand pages 1-3): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 70 citations.

2. (sal2008borreliaburgdorferiuniquely pages 1-2): Melanie S. Sal, Chunhao Li, M. A. Motalab, Satoshi Shibata, Shin-Ichi Aizawa, and Nyles W. Charon. <i>borrelia burgdorferi</i> uniquely regulates its motility genes and has an intricate flagellar hook-basal body structure. Mar 2008. URL: https://doi.org/10.1128/jb.01421-07, doi:10.1128/jb.01421-07. This article has 112 citations and is from a peer-reviewed journal.

3. (liu2010cellulararchitectureof pages 8-9): Jun Liu, Jerrilyn K. Howell, Sherille D. Bradley, Yesha Zheng, Z. Hong Zhou, and Steven J. Norris. Cellular architecture of treponema pallidum: novel flagellum, periplasmic cone, and cell envelope as revealed by cryo electron tomography. Journal of molecular biology, 403 4:546-61, Nov 2010. URL: https://doi.org/10.1016/j.jmb.2010.09.020, doi:10.1016/j.jmb.2010.09.020. This article has 166 citations and is from a domain leading peer-reviewed journal.

4. (wunder2018fcpbisa pages 6-7): Elsio A. Wunder, Leyla Slamti, David N. Suwondo, Kimberley H. Gibson, Zhiguo Shang, Charles V. Sindelar, Felipe Trajtenberg, Alejandro Buschiazzo, Albert I. Ko, and Mathieu Picardeau. Fcpb is a surface filament protein of the endoflagellum required for the motility of the spirochete leptospira. Frontiers in Cellular and Infection Microbiology, May 2018. URL: https://doi.org/10.3389/fcimb.2018.00130, doi:10.3389/fcimb.2018.00130. This article has 27 citations.

5. (sal2008borreliaburgdorferiuniquely pages 2-2): Melanie S. Sal, Chunhao Li, M. A. Motalab, Satoshi Shibata, Shin-Ichi Aizawa, and Nyles W. Charon. <i>borrelia burgdorferi</i> uniquely regulates its motility genes and has an intricate flagellar hook-basal body structure. Mar 2008. URL: https://doi.org/10.1128/jb.01421-07, doi:10.1128/jb.01421-07. This article has 112 citations and is from a peer-reviewed journal.

6. (wunder2016anovelflagellar pages 7-8): Elsio A. Wunder, Cláudio P. Figueira, Nadia Benaroudj, Bo Hu, Brian A. Tong, Felipe Trajtenberg, Jun Liu, Mitermayer G. Reis, Nyles W. Charon, Alejandro Buschiazzo, Mathieu Picardeau, and Albert I. Ko. A novel flagellar sheath protein, fcpa, determines filament coiling, translational motility and virulence for the leptospira spirochete. Molecular Microbiology, 101:457-470, Aug 2016. URL: https://doi.org/10.1111/mmi.13403, doi:10.1111/mmi.13403. This article has 104 citations and is from a domain leading peer-reviewed journal.

7. (wunder2016anovelflagellar pages 8-9): Elsio A. Wunder, Cláudio P. Figueira, Nadia Benaroudj, Bo Hu, Brian A. Tong, Felipe Trajtenberg, Jun Liu, Mitermayer G. Reis, Nyles W. Charon, Alejandro Buschiazzo, Mathieu Picardeau, and Albert I. Ko. A novel flagellar sheath protein, fcpa, determines filament coiling, translational motility and virulence for the leptospira spirochete. Molecular Microbiology, 101:457-470, Aug 2016. URL: https://doi.org/10.1111/mmi.13403, doi:10.1111/mmi.13403. This article has 104 citations and is from a domain leading peer-reviewed journal.

8. (gibson2020anasymmetricsheath pages 11-13): Kimberley H Gibson, Felipe Trajtenberg, Elsio A Wunder, Megan R Brady, Fabiana San Martin, Ariel Mechaly, Zhiguo Shang, Jun Liu, Mathieu Picardeau, Albert Ko, Alejandro Buschiazzo, and Charles Vaughn Sindelar. An asymmetric sheath controls flagellar supercoiling and motility in the leptospira spirochete. Mar 2020. URL: https://doi.org/10.7554/elife.53672, doi:10.7554/elife.53672. This article has 42 citations and is from a domain leading peer-reviewed journal.

9. (gibson2020anasymmetricsheath pages 10-11): Kimberley H Gibson, Felipe Trajtenberg, Elsio A Wunder, Megan R Brady, Fabiana San Martin, Ariel Mechaly, Zhiguo Shang, Jun Liu, Mathieu Picardeau, Albert Ko, Alejandro Buschiazzo, and Charles Vaughn Sindelar. An asymmetric sheath controls flagellar supercoiling and motility in the leptospira spirochete. Mar 2020. URL: https://doi.org/10.7554/elife.53672, doi:10.7554/elife.53672. This article has 42 citations and is from a domain leading peer-reviewed journal.

10. (zambacampero2024broadlyconservedflgv pages 1-2): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 11 citations and is from a highest quality peer-reviewed journal.

11. (zambacampero2024broadlyconservedflgv pages 4-6): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (zambacampero2024broadlyconservedflgv pages 7-10): Maxime Zamba-Campero, Daniel Soliman, Huaxin Yu, Amanda G. Lasseter, Yuen-Yan Chang, Julia L. Silberman, Jun Liu, L. Aravind, Mollie W. Jewett, Gisela Storz, and Philip P. Adams. Broadly conserved flgv controls flagellar assembly and borrelia burgdorferi dissemination in mice. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54806-w, doi:10.1038/s41467-024-54806-w. This article has 11 citations and is from a highest quality peer-reviewed journal.

13. (krusenstjerna2024dnaamodulatesthe pages 10-13): Andrew C. Krusenstjerna, Nerina Jusufovic, Timothy C. Saylor, and Brian Stevenson. Dnaa modulates the gene expression and morphology of the lyme disease spirochete. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.08.598065, doi:10.1101/2024.06.08.598065. This article has 4 citations.