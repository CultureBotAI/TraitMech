---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:32:24.007018'
end_time: '2026-08-04T09:43:31.268810'
duration_seconds: 667.26
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pleomorphic shaped
  trait_identifier: METPO:1000679
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: pleomorphic_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape characterized by variable and irregular morphology, where
    individual cells within a population exhibit multiple distinct shapes.
  parent_traits: METPO:1000666
  synonyms: S_star_dumbbell_pleomorphic, pleomorphic, pleomorphic-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review establishes pleomorphism as a phenotype of relaxed
    or absent cytoskeletal/wall shape control.) | DOI:10.1126/science.1170701: cell-wall-deficient
    L-forms (L-form review supports pleomorphism in wall-deficient or wall-less cells.)'
  causal_graph_summary: 'pleomorphic_shaped_relaxed_shape_control: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pleomorphic shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000679
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by variable and irregular morphology, where individual cells within a population exhibit multiple distinct shapes.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, pleomorphic, pleomorphic-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review establishes pleomorphism as a phenotype of relaxed or absent cytoskeletal/wall shape control.) | DOI:10.1126/science.1170701: cell-wall-deficient L-forms (L-form review supports pleomorphism in wall-deficient or wall-less cells.)
- **Existing causal graph summary:** pleomorphic_shaped_relaxed_shape_control: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **pleomorphic shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pleomorphic_shaped.yaml`.

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
- **Trait label:** pleomorphic shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000679
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by variable and irregular morphology, where individual cells within a population exhibit multiple distinct shapes.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, pleomorphic, pleomorphic-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review establishes pleomorphism as a phenotype of relaxed or absent cytoskeletal/wall shape control.) | DOI:10.1126/science.1170701: cell-wall-deficient L-forms (L-form review supports pleomorphism in wall-deficient or wall-less cells.)
- **Existing causal graph summary:** pleomorphic_shaped_relaxed_shape_control: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **pleomorphic shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pleomorphic_shaped.yaml`.

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


# Curation report: microbial pleomorphic shape

## Executive summary

**Target:** `METPO:1000679` (“pleomorphic shaped”); category **MORPHOLOGY**; term kind **CLASS**; mapping **REVIEWED**; parent `METPO:1000666`.

For TraitMech, this trait should represent an **observed cellular morphology in which cells within a population, or the same lineage across time, occupy multiple distinct or irregular shape states**. It should not be equated with one mechanism. The strongest curatable mechanisms recovered are:

1. **Bacterial wall-relaxation/L-form module:** inhibition or loss of peptidoglycan (PG), followed by synthase–autolysin-dependent wall escape, removes the rigid shape constraint and produces heterogeneous, irregular cells. Excess membrane synthesis then drives blebbing, tubulation, and scission.
2. **Haloarchaeal regulated-plasticity module:** *Haloferax volcanii* switches between rods and pleomorphic disks according to growth state, using genetically separable rod- and disk-determining systems.

The first module directly supports “relaxed shape control.” The second shows that pleomorphism can also be an actively regulated program rather than merely wall damage. These modules should remain separate in the YAML because their envelopes, taxa, and causal mechanisms differ fundamentally. (mercier2013excessmembranesynthesis pages 7-8, schiller2024identificationofstructural pages 1-2, tian2024implementationoffluorescentproteinbased pages 4-6)

| module | causal chain | strongest source DOI/year | confidence | principal caveat |
|---|---|---|---|---|
| **Bacillus subtilis L-form route** | PG precursor synthesis inhibition (e.g., D-cycloserine or glmM repression) → residual **aPBP** synthesis or enhanced **RodA** pathway + **LytE/CwlO** autolysis → wall lesions and often bulging → wall-free L-form state → loss of rigid wall-based shape constraint → pleomorphic/irregular morphology; in parallel, **excess membrane synthesis** increases surface area-to-volume ratio → blebbing/tubulation/scission for FtsZ-independent proliferation; **ROS reduction** supports survival/proliferation but is not evidenced as the direct cause of pleomorphic shape (kawai2023dissectingtheroles pages 7-9, kawai2023dissectingtheroles pages 1-2, kawai2023dissectingtheroles pages 5-7, mercier2013excessmembranesynthesis pages 7-8, kawai2015cellgrowthof pages 1-3, kawai2015cellgrowthof pages 5-6, tian2024implementationoffluorescentproteinbased pages 4-6) | 10.3389/fmicb.2023.1204979 (2023); 10.1016/j.cell.2013.01.043 (2013); 10.1016/j.cub.2015.04.031 (2015) | High | Strongly supported for **B. subtilis** under osmoprotective experimental conditions; pleomorphism is largely inferred from wall-loss/irregular L-form morphology and should not be overgeneralized to all bacteria or all wall-deficient states. |
| **Haloferax volcanii shape-plasticity route** | Growth phase/state cues → **RdfA/Sph3/CetZ1** rod-promoting program versus **DdfA/volactin** disk-promoting program → rods in early-log/swimming states and disks in mid/late-log or other states → population/time-dependent coexistence of multiple morphologies consistent with pleomorphic shape plasticity (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 6-7, schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 5-5, schiller2024identificationofstructural pages 7-9, schiller2024identificationofstructural pages 2-3) | 10.1038/s41467-024-45196-0 (2024) | Moderate-High | Evidence is strongest for regulated **rod↔disk transitions** in a specific haloarchaeon; this supports shape plasticity/pleomorphism at the population or temporal level, but not a generic archaeal pleomorphism mechanism, and some cited determinants are shape-state specific rather than direct causes of irregular morphology. |


*Table: This table summarizes two evidence-supported mechanistic routes linked to METPO:1000679 using only gathered evidence. It is useful for deciding which causal chains are strong enough for TraitMech curation and where taxon or assay caveats remain.*

## 1. Trait scope and boundaries

### Operational definition

Use the supplied definition verbatim: **“A cell shape characterized by variable and irregular morphology, where individual cells within a population exhibit multiple distinct shapes.”** The synonyms “pleomorphic,” “pleomorphic-shaped,” and `S_star_dumbbell_pleomorphic` are compatible, although the last may encode a narrower image-analysis vocabulary and should not constrain the biological definition.

The trait is best modeled as an **assay-observed morphology**, not as a physiological capacity. Evidence may come from microscopy, live-cell imaging, imaging flow cytometry, or a reproducible distribution of shape descriptors. In 2024, fluorescently labeled *Bacillus subtilis* LR2 L-forms showed medium-dependent short rods, small spheres with irregular division, and marked shape diversity. The imaging-flow workflow sampled at least **3 × 10⁴ cells per sample**, used nine replicates, and produced mean fluorescence above **10⁴ units per cell**, demonstrating a practical high-throughput implementation for quantifying heterogeneous L-form morphology. (tian2024implementationoffluorescentproteinbased pages 4-6)

### Include

- Concurrent irregular spheres, blebs, tubules, dumbbells, or other distinct forms in a culture.
- Reproducible shape plasticity across growth phase or environmental state when multiple forms occur within the defined population/time window.
- Genetically wall-less organisms or induced L-forms **only when multiple/irregular shapes are documented**, rather than inferred solely from wall absence.
- Archaeal polygonal disks with variable outlines when the assay establishes pleomorphic morphology.

### Exclude or annotate separately

- **Dimorphism:** a strictly binary, developmentally ordered switch is not necessarily pleomorphism unless the population exhibits heterogeneous or irregular forms.
- **Filamentation, branching, swelling, coccoid conversion, or elongation alone:** each is a nearby morphology and does not establish multiple distinct shapes.
- **Spheroplast/protoplast status:** this describes envelope loss or removal. It is a potential upstream state, not synonymous with pleomorphism.
- **L-form status:** L-forms are proliferative wall-deficient states; they often are pleomorphic, but nonproliferating protoplasts and regular spherical wall-deficient cells should not automatically receive this trait.
- **Cell-size heterogeneity alone:** variable area or volume without shape variation is insufficient.
- **Phase-separated rods and disks:** if no coexistence or irregularity is demonstrated, curate a shape transition rather than pleomorphism.

## 2. Candidate graph nodes

Identifiers below are deliberately conservative. Organism-specific proteins are retained by gene name and locus tag where the evidence did not establish a stable cross-database CURIE; UniProt accessions should be resolved against the exact strain before YAML insertion.

### Trait and taxa

| Node | Suggested grounding | Role |
|---|---|---|
| pleomorphic shaped | `METPO:1000679` | Target phenotype |
| *Bacillus subtilis* | `NCBITaxon:1423` | Main L-form model |
| *Escherichia coli* | `NCBITaxon:562` | Cross-phylum L-form/ROS validation |
| *Haloferax volcanii* | `NCBITaxon:309800` | Regulated archaeal shape-plasticity model |

### Cellular structures and processes

| Candidate node | Suggested grounding/status | Curation note |
|---|---|---|
| peptidoglycan | `CHEBI:8005` | Verify ontology release before commit |
| cell wall / peptidoglycan wall | GO grounding should be release-verified | Rigid shape-constraining structure |
| plasma membrane | `GO:0005886` | Membrane deformation becomes dominant after wall loss |
| cell morphogenesis | `GO:0000902` | Broad process node |
| peptidoglycan biosynthetic process | `GO:0009252` | Upstream wall-synthesis module |
| fatty-acid biosynthetic process | `GO:0006633` | Supplies excess membrane synthesis |
| L-form emergence | Label-only candidate | Transition from walled to proliferative wall-free state |
| cell bulging | Label-only candidate | Morphological intermediate in the aPBP route |
| membrane blebbing/tubulation/scission | Label-only candidates | Alternative proliferation mechanism |
| reactive-oxygen-species accumulation | Label-only or GO term after verification | Growth-limiting consequence, not established shape cause |
| osmoprotection/isotonic medium | Label-only environmental factor | Permissive condition for wall-free survival |
| growth phase | Standard ontology term to be resolved | Upstream context for archaeal rod–disk switching |

### Genes, proteins, and complexes

| Node | Taxon | Function in evidence | Grounding status |
|---|---|---|---|
| class-A PBPs: PonA, PbpD, PbpF, PbpG | *B. subtilis* | Residual PG synthesis supporting autolysis and bulging | Gene labels; resolve strain-specific UniProt IDs |
| RodA | *B. subtilis* | Alternative glycosyltransferase route for wall escape | Gene/protein label |
| PbpA/PbpH | *B. subtilis* | Cognate bPBPs required in enhanced Rod route | Gene labels |
| MreB/Mbl | *B. subtilis* | Elongasome components required in Rod-dependent escape | Gene labels |
| LytE | *B. subtilis* | Principal autolysin required in both tested escape routes | Gene/protein label |
| CwlO | *B. subtilis* | Partially overlapping autolysin in aPBP-associated route | Gene/protein label |
| AccDA | *B. subtilis* | Overproduction raises membrane synthesis | Protein-complex label |
| IspA | *B. subtilis* | Mutation reduces oxidative limitation of L-form growth | Gene/protein label |
| SodA, BshA/BshB1, Zwf | *B. subtilis* | Antioxidant functions permitting L-form proliferation | Gene labels |
| RdfA (`HVO_2174`) | *H. volcanii* | Required for rod formation | Locus-tag grounded |
| Sph3 (`HVO_2175`) | *H. volcanii* | SMC-like rod determinant | Locus-tag grounded |
| DdfA (`HVO_2176`) | *H. volcanii* | Required for disk formation | Locus-tag grounded |
| Volactin/VolA (`HVO_2015`) | *H. volcanii* | Dynamic actin homolog involved in disk morphogenesis | Locus-tag grounded |
| CetZ1 | *H. volcanii* | Archaeal tubulin-family rod/shape determinant | Protein label; resolve accession |
| LonB | *H. volcanii* | Modulates CetZ1 abundance; depletion favors rods | Indirect regulator; protein label |
| S-layer/Sph3-associated envelope system | *H. volcanii* | Candidate structural context | Do not encode a direct pleomorphism edge yet |

### Chemicals and experimental/environmental factors

| Node | Role | Grounding recommendation |
|---|---|---|
| D-cycloserine | Inhibits de novo PG-precursor synthesis; used at **200 µg/mL** in the 2023 study | Resolve ChEBI identifier before commit |
| fosfomycin | Known L-form inducer through PG-precursor inhibition | Resolve ChEBI identifier before commit |
| reduced glutathione | ROS scavenger supporting *E. coli* L-form growth | Resolve ChEBI identifier |
| oxygen limitation/anaerobiosis | Reduces oxidative damage and enables proliferation | Environmental/process node |
| lysozyme | Exogenous muralytic activity rescuing autolysin-defective escape | Resolve protein/activity grounding by assay |
| Mg²⁺ and isotonic medium | Osmoprotective culture conditions | `CHEBI:18420` may ground Mg²⁺; verify |

## 3. Candidate causal edges

Predicates are phrased for readability; map them to the project’s approved relation vocabulary during YAML editing.

| Subject → predicate → object | Evidence reference/date | Supporting snippet or result | Curation assessment |
|---|---|---|---|
| D-cycloserine → **inhibits** → de novo PG-precursor synthesis | [DOI 10.3389/fmicb.2023.1204979](https://doi.org/10.3389/fmicb.2023.1204979), June 2023 | DCS at **200 µg/mL** was used to deplete PG precursors in *B. subtilis*. | **High**, drug- and assay-specific. (kawai2023dissectingtheroles pages 7-9, kawai2023dissectingtheroles pages 2-3) |
| PG-precursor inhibition → **promotes** → L-form emergence | Same, 2023 | The study reports that precursor depletion promotes wall escape on isotonic medium. | **High** for *B. subtilis* under osmoprotection; do not generalize unconditionally. (kawai2023dissectingtheroles pages 7-9, kawai2023dissectingtheroles pages 5-7) |
| residual aPBP PG synthesis → **enables** → continued LytE/CwlO autolysis | Same, 2023 | “Residual PG synthesis” through aPBPs was required for continued autolytic activity. | **High**, *B. subtilis*. (kawai2023dissectingtheroles pages 1-2) |
| LytE/CwlO autolysis → **causes/enables** → wall lesion and bulging | Same, 2023 | Deleting all four aPBPs or both autolysins blocked bulging and emergence. | **High** for the combined module; CwlO alone had limited effect, so avoid asserting equal necessity. (kawai2023dissectingtheroles pages 7-9, kawai2023dissectingtheroles pages 5-7) |
| aPBP-supported synthesis + autolysis → **promotes** → bulging L-form escape | Same, 2023 | The aPBP route produced dispersed synthesis, bulging, and wall escape. | **High**, taxon- and condition-specific. (kawai2023dissectingtheroles pages 1-2, kawai2023dissectingtheroles pages 5-7) |
| RodA overproduction + PbpA/PbpH + MreB/Mbl → **enables** → L-form escape without extensive bulging | Same, 2023 | Enhanced RodA rescued the Δ4-aPBP background; the route required RodA GTase, bPBPs, and elongation proteins. | **High**, engineered *B. subtilis* route. (kawai2023dissectingtheroles pages 7-9, kawai2023dissectingtheroles pages 5-7) |
| LytE → **is required for** → Rod-dependent L-form escape | Same, 2023 | LytE was essential in both routes; exogenous lysozyme rescued its loss. | **High**, *B. subtilis*. (kawai2023dissectingtheroles pages 7-9) |
| loss of PG wall constraint → **permits** → pleomorphic/irregular morphology | [DOI 10.3390/bioengineering11010081](https://doi.org/10.3390/bioengineering11010081), January 2024 | Wall-less LR2 cells exhibited small spheres, irregular division, short rods, and medium-dependent shape diversity. | **Moderate–high**; morphology is directly observed, but a single linear molecular cause was not tested in that assay. (tian2024implementationoffluorescentproteinbased pages 4-6) |
| excess membrane synthesis → **drives** → blebbing/tubulation | [DOI 10.1016/j.cell.2013.01.043](https://doi.org/10.1016/j.cell.2013.01.043), February 2013 | AccDA elevation or PG-precursor inhibition produced excess membrane and L-form-like pleomorphic deformation. | **High**, *B. subtilis* experimental model. (mercier2013excessmembranesynthesis pages 7-8) |
| blebbing/tubulation → **leads to** → membrane scission and progeny formation | Same, 2013 | Shape change and membrane scission generated smaller progeny independently of normal division machinery. | **High**. (mercier2013excessmembranesynthesis pages 7-8) |
| L-form proliferation → **is independent of** → FtsZ-based division | Same, 2013 | Proliferation occurred through membrane deformation/scission rather than conventional FtsZ cytokinesis. | **High** for tested L-forms; this is a division edge, not the direct origin of pleomorphic shape. (mercier2013excessmembranesynthesis pages 7-8) |
| PG synthesis blockade → **increases** → electron-transport-associated ROS | [DOI 10.1016/j.cub.2015.04.031](https://doi.org/10.1016/j.cub.2015.04.031), June 2015 | Wall-deficient cells accumulated abnormal ROS and lipid peroxidation. | **High**, *B. subtilis*, with cross-support in *E. coli*. (kawai2015cellgrowthof pages 1-3, kawai2015cellgrowthof pages 5-6) |
| elevated ROS → **inhibits** → L-form survival/proliferation | Same, 2015 | **94%** of `ispA+` protoplasts lysed versus **35%** of `ispA−` protoplasts; antioxidant-gene repression inhibited growth. | **High**, quantitative. Do **not** connect ROS directly to pleomorphic shape. (kawai2015cellgrowthof pages 1-3, kawai2015cellgrowthof pages 5-6) |
| anaerobiosis/ROS scavenging/`ispA` mutation → **promotes** → L-form proliferation | Same, 2015 | Anaerobiosis, reduced glutathione, or ETC/ROS-reducing mutations improved growth in Gram-positive and Gram-negative models. | **High** as a permissive survival edge, not a morphogenesis edge. (kawai2015cellgrowthof pages 1-3, kawai2015cellgrowthof pages 5-6) |
| early-log/swimming state → **promotes** → rod morphology | [DOI 10.1038/s41467-024-45196-0](https://doi.org/10.1038/s41467-024-45196-0), February 2024 | Wild-type *H. volcanii* formed rods during early log and swimming states. | **High**, *H. volcanii*. (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 2-3) |
| mid/late-log state → **promotes** → pleomorphic disk morphology | Same, 2024 | Cells became disks during mid/late log and at motility-halo centers. | **Moderate–high** for temporal shape plasticity; verify coexistence if assigning the target trait to a narrowly sampled culture. (schiller2024identificationofstructural pages 1-2) |
| RdfA/Sph3 → **required for** → rod formation | Same, 2024 | `ΔrdfA` and `Δsph3` formed disks and were nonmotile; complementation restored rods. | **High**, *H. volcanii*. (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 5-5) |
| DdfA → **required for** → disk formation | Same, 2024 | `ΔHVO_2176` formed only rods regardless of growth phase. | **High**, *H. volcanii*. (schiller2024identificationofstructural pages 5-5) |
| CetZ1 → **promotes/is required for** → rod formation | Same, 2024 | `ΔcetZ1` was disk-only and nonmotile. | **High** for rod state; connection to general pleomorphism is indirect. (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 2-3) |
| Volactin → **promotes** → disk morphogenesis/rod-to-disk transition | Same, 2024 | Dynamic Volactin polymers and the `ΔvolA*` transition defect support a structural role in disk formation. | **Moderate–high**; reported abundance/activity descriptions vary by growth phase, so encode only the tested transition phenotype. (schiller2024identificationofstructural pages 6-7, schiller2024identificationofstructural pages 7-9) |
| rod/disk regulatory programs → **generate** → temporal/population shape plasticity | Same, 2024 | Mutants locked in rods or disks demonstrate genetically separable programs underlying wild-type switching. | **Moderate** as an edge to `METPO:1000679`; strongest direct endpoints are rod and disk morphology. (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 5-5) |

## 4. Recommended YAML graph architecture

### Module A: relaxed bacterial wall-shape control

A conservative graph should be:

`PG-precursor synthesis inhibition` → `reduced PG integrity` → `residual aPBP or enhanced RodA synthesis` + `LytE-dominant autolysis` → `wall lesion/bulging` → `L-form emergence` → `loss of rigid shape constraint` → `METPO:1000679`.

Add a parallel proliferation branch:

`excess fatty-acid/membrane synthesis` → `increased membrane area relative to volume` → `blebbing/tubulation` → `membrane scission` → `FtsZ-independent proliferation`.

Add ROS only as an enabling branch:

`PG blockade` → `electron-transport-associated ROS` → `lysis/inhibited proliferation`; `anaerobiosis or ROS scavenging` inhibits that edge. ROS reduction should **not** point directly to pleomorphic shape because PG-inhibited cells could lyse “even in the absence of L-form-like shape changes and cell division.” (kawai2015cellgrowthof pages 1-3)

### Module B: regulated haloarchaeal shape plasticity

Use a separate taxon-specific graph:

`growth phase/state` → (`RdfA` + `Sph3` + `CetZ1`) → `rod morphology`; and `growth phase/state` → (`DdfA` + `Volactin`) → `disk morphology`; heterogeneous or temporally mixed rod/disk outcomes → `METPO:1000679`.

This should not contain peptidoglycan nodes because *H. volcanii* uses an archaeal envelope and the cited work addresses an independent shape-control system. The 2024 study quantified **1,944 proteins**, identified **314 differentially abundant proteins**, and used genetics and live-cell imaging to separate shape-associated effects from growth-phase effects. (schiller2024identificationofstructural pages 3-5)

## 5. Recent developments and applications

### 2023–2024 mechanistic advances

- **2023:** Kawai and Errington resolved two routes through the wall during *B. subtilis* L-form emergence. The standard route couples residual aPBP synthesis to LytE/CwlO-mediated remodeling and bulging; an engineered enhanced-RodA route uses RodA, cognate bPBPs, and MreB/Mbl and can escape without extensive bulging. This replaces an overly simple “PG inhibition directly causes L-forms” graph with a synthase–hydrolase coordination mechanism. (kawai2023dissectingtheroles pages 7-9, kawai2023dissectingtheroles pages 1-2, kawai2023dissectingtheroles pages 5-7)
- **2024:** Schiller and colleagues identified genetically separable rod and disk determinants in *H. volcanii*, including RdfA, Sph3, DdfA, CetZ1, and Volactin. Their integrated proteomics/genetics strategy is an authoritative demonstration that microbial pleomorphism may be regulated and adaptive rather than merely structural failure. (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 5-5, schiller2024identificationofstructural pages 7-9)
- **2024:** Tian and colleagues established fluorescent-protein labeling and imaging-flow cytometry for morphologically heterogeneous L-forms, enabling quantitative analysis across tens of thousands of cells per sample. This is directly applicable to automated phenotype assignment and causal-graph validation. (tian2024implementationoffluorescentproteinbased pages 4-6)

### Current and potential implementations

1. **Antimicrobial mechanism and persistence research.** Cell-wall-active antibiotics can induce wall-deficient states, so morphology-aware assays may identify transient wall escape that conventional rod/coccus classifiers miss. However, clinical persistence is not established by morphology alone.
2. **Synthetic/minimal-cell research.** L-forms provide a tractable system for studying membrane-driven proliferation without canonical wall or FtsZ division machinery. (mercier2013excessmembranesynthesis pages 7-8)
3. **High-content phenotyping.** Stable fluorescent labeling plus imaging flow cytometry permits distributions of shape, size, and reporter abundance to replace subjective visual labels. The ≥30,000-cell sampling in the 2024 implementation is especially relevant to pleomorphism, which is inherently a distribution-level trait. (tian2024implementationoffluorescentproteinbased pages 4-6)
4. **Archaeal cell biology and biotechnology.** Shape-locked *H. volcanii* mutants can test how morphology affects motility, attachment, nutrient acquisition, and production phenotypes. The retrieved evidence directly links disk-only rod-defective mutants to nonmotility, but broader industrial benefits remain hypotheses. (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 3-5)

## 6. Expert interpretation

The evidence supports a two-axis understanding of pleomorphism:

- **Constraint axis:** Removing or weakening a rigid wall exposes membrane mechanics, producing irregular forms. In L-forms, the same surface-area imbalance that causes pleomorphism also supplies a primitive division mechanism. (mercier2013excessmembranesynthesis pages 7-8)
- **Regulatory axis:** Cells with flexible envelopes can actively choose alternative stable shapes through cytoskeletal and signaling programs. *H. volcanii* demonstrates that distinct genes can lock cells into rod or disk states. (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 5-5)

Accordingly, `METPO:1000679` should be an endpoint reached by multiple causal modules. Encoding “absence of cell wall” as its universal parent mechanism would be biologically incorrect, particularly for archaea and for organisms whose pleomorphism reflects regulated developmental programs.

## 7. Warnings: claims not ready for TraitMech curation

- **Do not use the supplied DOI `10.1146/annurev-cellbio-101011-155745` as a cell-shape source.** It resolves to *Inflammasomes and Their Roles in Health and Disease*, not a bacterial cell-shape review. This appears to be a metadata mismatch and should be corrected before migration.
- **The supplied DOI `10.1126/science.1170701` was not independently recovered in the available evidence.** Verify its title and exact statements before attaching it to an edge.
- Do not assert `cell-wall absence → pleomorphism` universally. Wall loss often produces spheres or irregular cells, but direct phenotype evidence is required.
- Do not curate ROS reduction, `ispA`, SodA, glutathione, or anaerobiosis as direct causes of pleomorphic shape. They enable survival/proliferation under wall-deficient conditions. (kawai2015cellgrowthof pages 1-3, kawai2015cellgrowthof pages 5-6)
- Do not make CwlO individually essential: the 2023 evidence indicates that LytE is the dominant requirement and CwlO deletion alone has comparatively little effect. (kawai2023dissectingtheroles pages 7-9)
- Do not merge the aPBP-bulging and enhanced-RodA nonbulging pathways into a single obligatory sequence. They are experimentally separable. (kawai2023dissectingtheroles pages 1-2, kawai2023dissectingtheroles pages 5-7)
- Do not generalize the *B. subtilis* DCS/isotonic-medium mechanism to all L-forms or natural wall-deficient infections.
- Do not generalize *H. volcanii* RdfA/DdfA/Volactin/CetZ1 relationships to all archaea.
- RdfA, DdfA, Sph3, and Volactin should be grounded by exact *H. volcanii* strain and database accession before release; locus tags are safer than guessed UniProt CURIEs.
- S-layer organization, N-glycosylation proteins, transporters, chemotaxis factors, LonB, ArtA, PssA, and PssD are promising extensions but presently have indirect, correlational, or transition-timing evidence in the retrieved material. Do not connect them directly to `METPO:1000679` without a perturbation-specific edge and source passage. (schiller2024identificationofstructural pages 6-7, schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 9-9)
- Corynebacterial Wag31, mycoplasmal terminal organelles, *Helicobacter* coccoid conversion, and halofilins are biologically plausible additional modules, but sufficiently specific causal evidence was not recovered here. They should not yet enter this graph.
- “Pleomorphic” annotations derived only from taxonomic descriptions should remain phenotype assertions, not mechanistic edges.

## DOI-first bibliography

1. **Schiller H, et al.** “Identification of structural and regulatory cell-shape determinants in *Haloferax volcanii*.” *Nature Communications* 15 (February 2024). DOI: [10.1038/s41467-024-45196-0](https://doi.org/10.1038/s41467-024-45196-0). (schiller2024identificationofstructural pages 1-2)
2. **Tian D, et al.** “Implementation of Fluorescent-Protein-Based Quantification Analysis in L-Form Bacteria.” *Bioengineering* 11:81 (January 2024). DOI: [10.3390/bioengineering11010081](https://doi.org/10.3390/bioengineering11010081). (tian2024implementationoffluorescentproteinbased pages 4-6)
3. **Kawai Y, Errington J.** “Dissecting the roles of peptidoglycan synthetic and autolytic activities in the walled to L-form bacterial transition.” *Frontiers in Microbiology* 14 (June 2023). DOI: [10.3389/fmicb.2023.1204979](https://doi.org/10.3389/fmicb.2023.1204979). (kawai2023dissectingtheroles pages 7-9)
4. **Kawai Y, Mercier R, Wu LJ, et al.** “Cell Growth of Wall-Free L-Form Bacteria Is Limited by Oxidative Damage.” *Current Biology* 25:1613–1618 (June 2015). DOI: [10.1016/j.cub.2015.04.031](https://doi.org/10.1016/j.cub.2015.04.031). (kawai2015cellgrowthof pages 1-3)
5. **Mercier R, Kawai Y, Errington J.** “Excess Membrane Synthesis Drives a Primitive Mode of Cell Proliferation.” *Cell* 152:997–1007 (February 2013). DOI: [10.1016/j.cell.2013.01.043](https://doi.org/10.1016/j.cell.2013.01.043). (mercier2013excessmembranesynthesis pages 7-8)

**Curation recommendation:** retain the existing relaxed-shape-control graph, but revise it into the explicit PG-synthase/autolysin, wall-escape, and membrane-mechanics branches above. Add the *H. volcanii* rod–disk module as a separate, taxon-qualified graph only if the project’s trait policy accepts temporally or population-level mixed shape states as `METPO:1000679`.

References

1. (mercier2013excessmembranesynthesis pages 7-8): Romain Mercier, Yoshikazu Kawai, and Jeff Errington. Excess membrane synthesis drives a primitive mode of cell proliferation. Cell, 152:997-1007, Feb 2013. URL: https://doi.org/10.1016/j.cell.2013.01.043, doi:10.1016/j.cell.2013.01.043. This article has 262 citations and is from a highest quality peer-reviewed journal.

2. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

3. (tian2024implementationoffluorescentproteinbased pages 4-6): Di Tian, Yiyuan Liu, Yueyue Zhang, Yunfei Liu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Implementation of fluorescent-protein-based quantification analysis in l-form bacteria. Bioengineering, 11:81, Jan 2024. URL: https://doi.org/10.3390/bioengineering11010081, doi:10.3390/bioengineering11010081. This article has 2 citations.

4. (kawai2023dissectingtheroles pages 7-9): Yoshikazu Kawai and Jeff Errington. Dissecting the roles of peptidoglycan synthetic and autolytic activities in the walled to l-form bacterial transition. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1204979, doi:10.3389/fmicb.2023.1204979. This article has 7 citations and is from a peer-reviewed journal.

5. (kawai2023dissectingtheroles pages 1-2): Yoshikazu Kawai and Jeff Errington. Dissecting the roles of peptidoglycan synthetic and autolytic activities in the walled to l-form bacterial transition. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1204979, doi:10.3389/fmicb.2023.1204979. This article has 7 citations and is from a peer-reviewed journal.

6. (kawai2023dissectingtheroles pages 5-7): Yoshikazu Kawai and Jeff Errington. Dissecting the roles of peptidoglycan synthetic and autolytic activities in the walled to l-form bacterial transition. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1204979, doi:10.3389/fmicb.2023.1204979. This article has 7 citations and is from a peer-reviewed journal.

7. (kawai2015cellgrowthof pages 1-3): Yoshikazu Kawai, Romain Mercier, Ling Juan Wu, Patricia Domínguez-Cuevas, Taku Oshima, and Jeff Errington. Cell growth of wall-free l-form bacteria is limited by oxidative damage. Current Biology, 25:1613-1618, Jun 2015. URL: https://doi.org/10.1016/j.cub.2015.04.031, doi:10.1016/j.cub.2015.04.031. This article has 125 citations and is from a highest quality peer-reviewed journal.

8. (kawai2015cellgrowthof pages 5-6): Yoshikazu Kawai, Romain Mercier, Ling Juan Wu, Patricia Domínguez-Cuevas, Taku Oshima, and Jeff Errington. Cell growth of wall-free l-form bacteria is limited by oxidative damage. Current Biology, 25:1613-1618, Jun 2015. URL: https://doi.org/10.1016/j.cub.2015.04.031, doi:10.1016/j.cub.2015.04.031. This article has 125 citations and is from a highest quality peer-reviewed journal.

9. (schiller2024identificationofstructural pages 6-7): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

10. (schiller2024identificationofstructural pages 3-5): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

11. (schiller2024identificationofstructural pages 5-5): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

12. (schiller2024identificationofstructural pages 7-9): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

13. (schiller2024identificationofstructural pages 2-3): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

14. (kawai2023dissectingtheroles pages 2-3): Yoshikazu Kawai and Jeff Errington. Dissecting the roles of peptidoglycan synthetic and autolytic activities in the walled to l-form bacterial transition. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1204979, doi:10.3389/fmicb.2023.1204979. This article has 7 citations and is from a peer-reviewed journal.

15. (schiller2024identificationofstructural pages 9-9): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.