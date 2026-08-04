---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:00:40.748225'
end_time: '2026-08-04T08:11:24.954571'
duration_seconds: 644.21
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: crescent shaped
  trait_identifier: METPO:1000669
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: crescent_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a curved crescent-like morphology
    with a concave inner side and a convex outer side.
  parent_traits: METPO:1000666
  synonyms: crescent-shaped
  evidence_summary: 'DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid
    and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal
    determinant of curved Caulobacter cell shape.)'
  causal_graph_summary: 'crescent_shaped_crescentin_curvature: 8 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** crescent shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000669
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved crescent-like morphology with a concave inner side and a convex outer side.
- **Parent traits:** METPO:1000666
- **Synonyms:** crescent-shaped
- **Existing evidence:** DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal determinant of curved Caulobacter cell shape.)
- **Existing causal graph summary:** crescent_shaped_crescentin_curvature: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **crescent shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/crescent_shaped.yaml`.

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
- **Trait label:** crescent shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000669
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved crescent-like morphology with a concave inner side and a convex outer side.
- **Parent traits:** METPO:1000666
- **Synonyms:** crescent-shaped
- **Existing evidence:** DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal determinant of curved Caulobacter cell shape.)
- **Existing causal graph summary:** crescent_shaped_crescentin_curvature: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **crescent shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/crescent_shaped.yaml`.

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


# Curation-focused research report: crescent-shaped microbial cells

## Executive summary

The target trait is **“crescent shaped”**, identifier **“METPO:1000669”**, defined as a cell with a curved, crescent-like body having a concave inner side and convex outer side. The literature commonly calls this phenotype **vibrioid**, **curved rod**, or—especially for *Vibrio cholerae*—**comma-shaped**. These terms are appropriate mappings only when they denote persistent curvature of the cell body rather than a transient bend or a multi-turn helix.

The principal curation conclusion is that crescent morphology is a **convergent phenotype**, not one universal pathway. At least four experimentally supported mechanisms produce it:

1. a cytoplasmic, membrane-associated crescentin scaffold that mechanically biases peptidoglycan growth in *Caulobacter*;
2. a periplasmic CrvAB curvature module in *V. cholerae*;
3. asymmetric peptidoglycan editing by the Bd1075 LD-carboxypeptidase in *Bdellovibrio bacteriovorus*; and
4. outer-membrane Por39/Por41–PapS assemblies that spatially constrain the elongasome in *Rhodospirillum rubrum*.

These should be represented as **separate, taxon-qualified causal branches** converging on “METPO:1000669,” rather than merged into a single universal crescentin pathway. The two most important recent advances are the 2024 near-atomic structural and cellular description of crescentin and the discovery in 2024 of the porin–PapS–elongasome mechanism in *R. rubrum*. (liu2024filamentstructureand pages 6-8, pohl2024anoutermembrane pages 1-2)

## 1. Trait scope and boundaries

### Positive scope

A positive annotation should normally require microscopy or an authoritative morphological description demonstrating:

- persistent curvature along the longitudinal axis of an individual cell;
- one identifiable concave and one convex face;
- a curved-rod, comma-like, vibrioid, or crescent-like outline;
- an intrinsic morphology maintained during ordinary growth, unless the annotation explicitly records an induced phenotype.

The cell-wall sacculus is the proximate load-bearing determinant of bacterial shape. In *Caulobacter*, isolated sacculi retain curvature, and crescentin generates an elongation-rate gradient around the sidewall rather than merely bending a flexible membrane. (sundararajan2017cytoskeletalproteinsin pages 16-17, cabeen2009bacterialcellcurvature pages 1-2)

### Boundary cases to exclude or qualify

- **Straight rod:** the null or reduced-curvature phenotype in many perturbation studies, not a positive instance of “METPO:1000669.”
- **Helical or spiral cell:** multiple turns or torsion should be assigned to a helical/spiral trait rather than automatically mapped to crescent shaped. Division-blocked *Caulobacter* and crescentin-expressing filamentous *E. coli* can become left-handed helices, illustrating the length-dependent transition from a curved rod to a helix. (cabeen2009bacterialcellcurvature pages 6-7)
- **Filamentous morphology:** elongation without septation is a separate dimension. A filament may be straight, curved, or helical.
- **Transient mechanical deformation:** crescentin-null cells forced to grow in circular microchambers become curved, but lose curvature progressively after release if growth continues. This is an experimentally induced curvature phenotype and should not establish a constitutive species trait. (cabeen2009bacterialcellcurvature pages 6-7)
- **Division-site constriction or polar curvature:** local curvature at a septum or pole does not by itself establish a crescent-shaped whole cell.
- **Curved stalk, hypha, flagellum, or other appendage:** appendage geometry is not equivalent to cell-body morphology.
- **Helicobacter/Campylobacter helical morphology:** related peptidoglycan hydrolases are mechanistically informative, but their canonical multi-turn helical phenotype should not be curated as “METPO:1000669” without strain- and assay-specific evidence of a crescent/vibrioid state.

## 2. Current mechanistic understanding

The common physical principle is **asymmetric cell-envelope growth or remodeling**. Curvature arises when the two longitudinal faces acquire different effective lengths: growth is inhibited on one side, enhanced on the other, or peptidoglycan chemistry is edited asymmetrically. The molecular implementation varies substantially by lineage.

### 2.1 *Caulobacter*: crescentin-dependent mechanical control

Crescentin, encoded by **creS**, forms a stable filamentous structure along the inner, concave face. The foundational model is that membrane-associated crescentin is held in an extended state and imposes strain that reduces cell-wall expansion proximally, producing progressively greater insertion toward the outer face. D-cysteine pulse–chase experiments showed trapezoidal zones of new wall synthesis in hypercurved sacculi, with longer new-growth regions at the outer curvature; straight ΔcreS sacculi instead showed approximately rectangular regions. (cabeen2009bacterialcellcurvature pages 1-2, cabeen2009bacterialcellcurvature pages 6-7)

The strongest necessity/sufficiency observations are:

- loss of crescentin gives straight rods;
- attachment-defective or nonfunctional variants fail to curve cells;
- producing crescentin in *E. coli* is sufficient to induce robust curvature;
- physical confinement can phenocopy curvature by generating growth-dependent mechanical strain. (sundararajan2017cytoskeletalproteinsin pages 16-17, cabeen2009bacterialcellcurvature pages 1-2, cabeen2009bacterialcellcurvature pages 6-7)

The 2024 structural study substantially refined the entity model. Cryo-EM/cryo-ET resolved crescentin as a non-polar, octameric filament assembled from two strands, each involving paired dimers. Cellular filaments are approximately 4 nm thick, form bands 30–40 nm wide, lie about 5 nm from the inner membrane on the concave side, and were reconstructed at approximately 3.3 Å resolution. Deleting the disordered N-terminal 27 residues produced straight cells despite filament assembly in vitro, supporting a distinct requirement for correct membrane-proximal organization. (liu2024filamentstructureand pages 6-8, liu2024filamentstructureand pages 10-11)

MreB should be treated as a supporting rather than uniquely crescent-specific determinant. The 2023 authoritative review describes MreB as organizing the Rod complex and directing general cell-wall insertion, while crescentin superimposes an asymmetric mechanical bias. Earlier work indicates that MreB function is important for crescentin-envelope association, but this does not prove a simple direct CreS–MreB binding edge. (barrows2023synchronizedswarmersand pages 11-13, cabeen2010mutationsinthe pages 1-2)

An important envelope modifier is **WbqL-dependent O-polysaccharide biosynthesis**. Deleting wbqL generated aberrant O-polysaccharide, detached crescentin from the envelope, and abolished curvature. This is not evidence that normal O-polysaccharide or the S-layer is intrinsically required: S-layer-null and O-polysaccharide-null strains retained near-wild-type curvature. The deleterious causal entity is specifically the **altered O-polysaccharide species**. (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 5-7)

### 2.2 *Vibrio cholerae*: CrvAB and regulatory switching

CrvA polymerizes in the periplasm and promotes the characteristic curved rod. CrvA-deficient cells become straighter and show attenuated colonization in animal models. Later work established CrvA and CrvB as a transferable curvature-inducing module, but the retrieved evidence supports the direct regulatory branch more completely than the detailed CrvA–CrvB molecular interface. (nikolai2020rnamediatedcontrolof pages 1-2, pohl2024anoutermembrane pages 1-2)

The Hfq-dependent small RNA **VadR** directly base-pairs with the translation-initiation region of crvA mRNA and represses CrvA production. Compensatory base-pair experiments support a direct RNA–RNA interaction. Deleting vadR increased CrvA approximately 1.5-fold and increased curvature; VadR overexpression reduced CrvA approximately twofold and reduced curvature without materially changing cell length or volume. (nikolai2020rnamediatedcontrolof pages 4-6)

VadR is activated by the **VxrAB/WigKR two-component system**, particularly during cell-envelope stress. A genomic-library screen assayed approximately 23,000 colonies; all seven positive clones mapped to the vxrABCDE region. Deleting vxrABCDE reduced vadR promoter activity approximately 50-fold and eliminated detectable VadR in Northern blots. Cell-wall-targeting antibiotics activate this pathway, and cells unable to repress crvA through VadR survive penicillin G challenge less well. (nikolai2020rnamediatedcontrolof pages 1-2)

A second regulatory axis is cyclic di-GMP. High cyclic di-GMP, acting through VpsT-associated regulation, represses crvA and favors straighter cells in the sessile biofilm program; low cyclic di-GMP permits stronger curvature in motile cells. The ΔcrvA mutant had approximately fourfold lower curvature and was 1.08-fold longer than wild type. Across more than 1,000 trajectories and four replicates, curved wild-type cells swam 5.5% faster than straight ΔcrvA cells (95% CI 5.5–5.9%; P<10⁻⁵), while reversal frequency was not significantly different. (fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 1-1)

### 2.3 *Bdellovibrio*: asymmetric enzymatic editing

In *B. bacteriovorus*, **Bd1075** provides a mechanistically distinct route. It is a periplasm-targeted, monomeric LD-carboxypeptidase that localizes to the convex outer face; this localization requires its C-terminal NTF2-like domain. Deleting bd1075 changed median curvature from 0.64 arbitrary units in wild type (95% CI 0.63–0.66) to 0.11 (95% CI 0.10–0.12; P<0.0001), producing straight rods. (banks2022asymmetricpeptidoglycanediting pages 1-2)

Bd1075 removes terminal D-alanine from peptidoglycan tetrapeptides. Δbd1075 sacculi contained 23.7±0.8% monomeric tetrapeptides and 33.2±0.7% cross-linked tetratetrapeptides, versus 9.6±0.8% and 18.6±0.6% in wild type, and lacked the tripeptide products associated with Bd1075 activity. Thus, spatially asymmetric enzymatic editing—not a crescentin-like cytoplasmic scaffold—causes curvature. (banks2022asymmetricpeptidoglycanediting pages 4-6)

The shape also has a directly tested ecological function. Straight Δbd1075 predators entered prey more slowly, and approximately 9.2% of observed bdelloplasts showed visible stretching/deformation by the mutant predator. Morphometric comparisons involved hundreds of cells across three biological repeats. This supports a taxon-specific edge from curvature to improved prey invasion and fit within the rounded bdelloplast. (banks2022asymmetricpeptidoglycanediting pages 4-6, banks2022asymmetricpeptidoglycanediting pages 1-2)

### 2.4 2024 discovery in *Rhodospirillum rubrum*

Pöhl and colleagues discovered a different curvature module in which the porins **Por39/Por41** form outer-curve helical assemblies that recruit the peptidoglycan-binding lipoprotein **PapS**. PapS is highly abundant—more than 15,000 copies per cell—and forms a stable outer-curve ribbon. Its peptidoglycan-binding OmpA-like domain is required for bending, whereas outer-membrane tethering has an auxiliary role. (pohl2024anoutermembrane pages 4-5, pohl2024anoutermembrane pages 1-2)

Por41 D71S delocalized the porin pattern, abolished PapS ribbons, and straightened cells; the corresponding Por39 substitution did not. PapS constrains RodZ-marked elongasome complexes at the outer curve: deleting papS increased diffusive RodZ molecules and equalized their distribution between cell faces. The resulting model is that Por39/Por41–PapS assemblies act as molecular cages, stabilizing elongasomes and biasing peptidoglycan growth toward the convex face. (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 7-8)

This finding is especially important for TraitMech because it demonstrates that an outer-membrane spatial pattern can regulate inner-membrane elongasome dynamics across the envelope. It should be curated as a new, taxon-specific branch rather than as evidence for crescentin conservation. (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 1-2)

## 3. Candidate nodes grouped by type

### Trait and taxa

- **crescent shaped** — **“METPO:1000669”**
- *Caulobacter crescentus* / currently accepted *Caulobacter vibrioides* — label pending taxonomic normalization
- *Vibrio cholerae*
- *Bdellovibrio bacteriovorus*
- *Rhodospirillum rubrum*
- *Escherichia coli* — heterologous-expression and mechanical-confinement assay host

Exact NCBITaxon CURIEs should be added only after resolving strain names and historical synonymy; the papers use several strain-level designations.

### Genes, RNAs, proteins, and complexes

- **creS**; crescentin/CreS; crescentin filament
- **MreB**, **RodZ**, Rod/elongasome complex
- **wbqL**, WbqL; altered O-polysaccharide product
- **crvA**, CrvA; **crvB**, CrvB; CrvAB complex
- **vadR**, VadR sRNA; **Hfq**
- **VxrA/VxrB** two-component system; VpsT
- **bd1075**, Bd1075; C-terminal NTF2-like localization domain
- **por39**, Por39; **por41**, Por41; **papS**, PapS; Por39/Por41–PapS assembly

Organism-specific protein nodes should remain label-only until UniProt accessions are verified against the exact experimental strain.

### Chemicals and macromolecular structures

- peptidoglycan sacculus — candidate **GO:0009274** (“peptidoglycan-based cell wall”)
- peptidoglycan biosynthetic process — **GO:0009252**
- lipopolysaccharide and O-polysaccharide — label-level pending exact chemical grounding
- cyclic di-GMP — candidate **CHEBI:49537**, to be registry-verified before insertion
- D-alanine; peptidoglycan tetra-, tri-, and dipeptide muropeptides
- penicillin G, cefalexin, mecillinam, and chloramphenicol — experimental perturbagens, not constitutive trait causes

### Locations and processes

- concave/inner cell face — label-only spatial node
- convex/outer cell face — label-only spatial node
- cytoplasm, inner membrane, periplasm, outer membrane
- crescentin polymerization; membrane attachment
- asymmetric peptidoglycan insertion
- LD-carboxypeptidase activity
- elongasome entrapment/stabilization
- cell curvature generation
- swimming, surface colonization, biofilm development, antibiotic survival, and prey invasion

## 4. Candidate causal edges

The following compact table summarizes the highest-priority edges. All are taxon-qualified.

| taxon/branch | subject | predicate | object | evidence strength | DOI |
|---|---|---|---|---|---|
| *Caulobacter crescentus* | creS / crescentin | assembles_as | concave membrane-associated filament | strong direct | 10.1038/emboj.2009.61 (cabeen2009bacterialcellcurvature pages 1-2, sundararajan2017cytoskeletalproteinsin pages 16-17) |
| *Caulobacter crescentus* | concave membrane-associated crescentin filament | biases | differential peptidoglycan insertion (less proximal, more distal) | strong direct | 10.1038/emboj.2009.61 (cabeen2009bacterialcellcurvature pages 6-7, barrows2023synchronizedswarmersand pages 11-13) |
| *Caulobacter crescentus* | differential peptidoglycan insertion | causes | crescent-shaped / curved cell morphology | strong direct | 10.1038/emboj.2009.61 (cabeen2009bacterialcellcurvature pages 6-7, sundararajan2017cytoskeletalproteinsin pages 16-17) |
| *Caulobacter crescentus* | altered WbqL-dependent O-polysaccharide | disrupts | crescentin–cell-envelope association | strong direct | 10.1128/JB.01371-09 (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 5-7) |
| *Caulobacter crescentus* | disrupted crescentin–cell-envelope association | causes | straightening / loss of curvature | strong direct | 10.1128/JB.01371-09 (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 5-7) |
| *Vibrio cholerae* | VxrAB two-component system | activates | VadR sRNA expression | strong direct | 10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2) |
| *Vibrio cholerae* | VadR sRNA | represses_post_transcriptionally | crvA mRNA | strong direct | 10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 4-6, nikolai2020rnamediatedcontrolof pages 1-2) |
| *Vibrio cholerae* | CrvA | promotes | curved / crescent-shaped cell morphology | strong direct | 10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2) |
| *Vibrio cholerae* | high c-di-GMP / VpsT | represses | crvA expression | strong direct | 10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 1-1) |
| *Vibrio cholerae* | crvA repression under high c-di-GMP | causes | straightening / reduced curvature | strong direct | 10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 1-1) |
| *Bdellovibrio bacteriovorus* | Bd1075 | localizes_to | outer convex face | strong direct | 10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| *Bdellovibrio bacteriovorus* | Bd1075 | exerts | LD-carboxypeptidase peptidoglycan editing | strong direct | 10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 4-6, banks2022asymmetricpeptidoglycanediting pages 1-2) |
| *Bdellovibrio bacteriovorus* | convex-face Bd1075-dependent peptidoglycan editing | promotes | curved / vibrioid morphology | strong direct | 10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 4-6, banks2022asymmetricpeptidoglycanediting pages 1-2) |
| *Bdellovibrio bacteriovorus* | curved / vibrioid morphology | increases | prey invasion fitness / faster entry | strong direct | 10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 4-6, banks2022asymmetricpeptidoglycanediting pages 1-2) |
| *Rhodospirillum rubrum* | Por39/Por41 porin assemblies | recruit / position | PapS at outer curve | strong direct | 10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 7-8) |
| *Rhodospirillum rubrum* | PapS | entraps / stabilizes | RodZ-marked elongasome complexes | strong direct | 10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 4-5) |
| *Rhodospirillum rubrum* | PapS–elongasome entrapment | biases | outer-curve peptidoglycan growth | strong direct | 10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 1-2) |
| *Rhodospirillum rubrum* | outer-curve-biased growth | causes | curved cell morphology | strong direct | 10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 1-2) |


*Table: This table summarizes the strongest curation-priority causal edges for the crescent-shaped microbial morphology trait across the best-supported taxa and mechanisms. It is useful for deciding which edges are most ready for inclusion in a TraitMech causal graph and which branches should remain taxon-scoped.*

### Supporting snippets and curation notes

| Proposed triple | Supporting source snippet | Curation note |
|---|---|---|
| *Caulobacter* creS —encodes/produces→ crescentin | “crescentin (encoded by creS)…is required for cell curvature” | Direct and curation-ready. DOI: [10.1128/jb.00384-22](https://doi.org/10.1128/jb.00384-22), February 2023. (barrows2023synchronizedswarmersand pages 11-13) |
| crescentin —localizes_to→ concave inner face | “localizes to the inner cell curvature” | Direct microscopy; curation-ready. DOI: [10.1038/emboj.2009.61](https://doi.org/10.1038/emboj.2009.61), published online 12 March 2009. (cabeen2009bacterialcellcurvature pages 1-2) |
| crescentin mechanical strain —biases→ peptidoglycan insertion | “longer cleared spaces at the outer curvature” and “differential peptidoglycan insertion rates” | Strong pulse–chase evidence; predicate should express bias/regulation, not direct enzymatic synthesis. (cabeen2009bacterialcellcurvature pages 6-7) |
| differential sidewall growth —causes→ “METPO:1000669” | “creating a longitudinal cell length differential and hence curvature” | Central mechanistic edge; curation-ready for *Caulobacter*. (cabeen2009bacterialcellcurvature pages 1-2) |
| altered WbqL-dependent O-polysaccharide —disrupts→ crescentin-envelope association | “altered O-polysaccharide species abolishes cell curvature by apparently interfering with…association” | Strong genetics but “apparently” signals incomplete molecular mechanism. Curate with an uncertainty qualifier. (cabeen2010mutationsinthe pages 1-2) |
| VxrAB —activates→ vadR transcription | “vadR transcription is activated by the VxrAB two-component system” | Direct reporter/Northern evidence; curation-ready for *V. cholerae*. (nikolai2020rnamediatedcontrolof pages 1-2) |
| VadR —represses→ crvA mRNA | “VadR is a direct inhibitor of crvA” | Compensatory base-pair evidence supports a direct post-transcriptional edge. (nikolai2020rnamediatedcontrolof pages 4-6) |
| CrvA —promotes→ curved-rod morphology | “CrvA protein polymerizes in the periplasmic space to promote cell bending” | Direct deletion/phenotype evidence; taxon-specific. (nikolai2020rnamediatedcontrolof pages 1-2) |
| high cyclic di-GMP/VpsT —represses→ crvA/curvature | “high c-di-GMP concentrations promote straight rod morphology” | Regulatory state edge; do not imply cyclic di-GMP physically bends the cell. (fernandez2020vibriocholeraeadapts pages 1-1) |
| cell-wall antibiotics —activate→ VxrAB–VadR response | “activated by ß-lactam antibiotics” | Assay- and dose-dependent environmental edge; retain treatment context. (nikolai2020rnamediatedcontrolof pages 1-2) |
| Bd1075 —has_activity→ LD-carboxypeptidase activity | “remove the terminal D-alanine…to generate a tripeptide” | Supported in vivo and in vitro; strong enzymatic edge. (banks2022asymmetricpeptidoglycanediting pages 4-6) |
| Bd1075 —localizes_to→ convex outer face | “localizes to the outer convex face” | Direct localization; NTF2-like-domain dependence may be represented as a separate structural edge. (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| Bd1075-dependent PG editing —causes→ curved morphology | “Δbd1075 mutant cells had a distinct straight rod-shaped morphology” | Deletion, complementation, chemistry, and localization jointly support causality. (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| curved *Bdellovibrio* morphology —promotes→ prey-entry fitness | “Rod-shaped Δbd1075 mutants invade prey more slowly” | Strong but species- and lifecycle-specific fitness edge. (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| Por39/Por41 —recruit/position→ PapS | “form a helical ribbon-like structure at the outer curve…that recruits…PapS” | 2024 primary evidence; curation-ready for *R. rubrum*. (pohl2024anoutermembrane pages 1-2) |
| PapS —stabilizes/entraps→ RodZ-marked elongasome | “act as molecular cages that entrap the cell elongation machinery” | Strong dynamics and mutant evidence; “entraps” is the authors’ mechanistic model. (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 1-2) |
| PapS-associated elongasome —biases→ convex-face growth | “biasing cell growth towards the outer curve” | Strong integrated mechanistic edge. (pohl2024anoutermembrane pages 1-2) |
| convex-face-biased growth —causes→ curved morphology | “spatial bias…established by PapS-mediated elongasome entrapment” | Curation-ready, taxon-qualified endpoint. (pohl2024anoutermembrane pages 13-14) |

## 5. Applications and real-world relevance

### Experimental and synthetic-biology applications

Crescentin is both necessary in its native setting and sufficient to curve heterologous *E. coli*, making it a useful modular perturbation for studying how mechanical strain alters cell-wall growth. The 2024 structure now provides residue- and domain-level targets for engineering filament assembly and membrane organization. (liu2024filamentstructureand pages 6-8, cabeen2009bacterialcellcurvature pages 6-7)

The *R. rubrum* system offers a complementary engineering principle: morphology can be controlled from the outer membrane by spatially trapping the elongasome rather than by introducing a cytoplasmic filament. This expands the potential design space for synthetic bacterial morphogenesis. (pohl2024anoutermembrane pages 13-14, pohl2024anoutermembrane pages 1-2)

### Pathogenesis, biofilms, and antibiotics

In *V. cholerae*, curvature is integrated with motile-versus-sessile lifestyle switching. Curvature modestly but reproducibly increases swimming speed, whereas high cyclic di-GMP straightens cells during biofilm development. VadR coordinates cell shape with envelope-stress survival and represses several biofilm transcripts in addition to crvA. These pathways are potential antimicrobial or antivirulence targets, but no evidence retrieved here establishes a clinically validated morphology-directed drug. (fernandez2020vibriocholeraeadapts pages 5-6, nikolai2020rnamediatedcontrolof pages 4-6, nikolai2020rnamediatedcontrolof pages 1-2)

### Predatory-bacterium biotechnology

*B. bacteriovorus* is investigated as a living antibacterial because it attacks diverse Gram-negative prey, including multidrug-resistant pathogens. Bd1075-dependent curvature improves prey entry and fit within the bdelloplast, so morphology is relevant to optimizing predatory fitness. This remains a preclinical biotechnology concept rather than an approved therapeutic application. (banks2022asymmetricpeptidoglycanediting pages 4-6, banks2022asymmetricpeptidoglycanediting pages 1-2)

### Surface colonization and ecology

The 2023 *Caulobacter* review considers curvature relevant to adhesion during division under flow and potentially to swimming efficiency in nutrient-poor aquatic environments. These functional edges are biologically plausible and experimentally motivated, but should be stored separately from the core morphogenesis graph because they are downstream fitness consequences rather than causes of the trait. (barrows2023synchronizedswarmersand pages 11-13)

## 6. Warnings and claims not yet ready for TraitMech

1. **Do not make crescentin universal.** CreS is a strong determinant in *Caulobacter*, but *Vibrio*, *Bdellovibrio*, and *Rhodospirillum* use different proteins and envelope compartments.
2. **Do not merge crescent and helical morphology.** Long or division-blocked cells can convert single-arc curvature into a helix; annotate both length state and geometry where necessary. (cabeen2009bacterialcellcurvature pages 6-7)
3. **Do not curate “normal LPS is required for curvature.”** S-layer-null and O-polysaccharide-null *Caulobacter* retained near-normal curvature. The supported claim is that a particular aberrant O-polysaccharide produced in wbqL mutants interferes with crescentin-envelope association. (cabeen2010mutationsinthe pages 5-7)
4. **Do not assert direct CreS–MreB binding without additional evidence.** MreB is required for general elongasome organization and affects crescentin-envelope association, but the retrieved sources do not establish a simple direct molecular interaction. (barrows2023synchronizedswarmersand pages 11-13, cabeen2010mutationsinthe pages 1-2)
5. **Treat physical confinement as an induced phenotype.** Circular chambers can curve genetically straight cells through growth-dependent forces; this is an environmental/assay edge, not evidence of a constitutive trait. (cabeen2009bacterialcellcurvature pages 6-7)
6. **Keep antibiotics as contextual regulators.** β-lactams activate the VxrAB–VadR response, but dose, growth state, and organism are integral to the claim. Antibiotics should not be represented as universal causes of straight or curved morphology. (nikolai2020rnamediatedcontrolof pages 1-2)
7. **Keep CrvB mechanistic details provisional in this report.** CrvAB is supported as a curvature module by the literature, but the retrieved full-text evidence did not provide enough detail to curate every proposed CrvA–CrvB molecular edge confidently.
8. **Avoid unverified accessions.** Protein CURIEs should be added only after matching the experimental strain. Label-only nodes are preferable to incorrect UniProt identifiers.
9. **Separate morphology from fitness.** Swimming speed, colonization, biofilm formation, antibiotic survival, and prey invasion are downstream outcomes and are taxon- and assay-specific.

## 7. DOI-first bibliography

1. **Liu Y, van den Ent F, Löwe J.** “Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin.” *Proceedings of the National Academy of Sciences* 121, February 2024. DOI: [10.1073/pnas.2309984121](https://doi.org/10.1073/pnas.2309984121). (liu2024filamentstructureand pages 6-8, liu2024filamentstructureand pages 10-11)
2. **Pöhl S, et al.** “An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in *Rhodospirillum rubrum*.” *Nature Communications* 15:7616, accepted 14 August 2024; published September 2024. DOI: [10.1038/s41467-024-51790-z](https://doi.org/10.1038/s41467-024-51790-z). (pohl2024anoutermembrane pages 4-5, pohl2024anoutermembrane pages 1-2)
3. **Barrows JM, Goley ED.** “Synchronized Swarmers and Sticky Stalks: *Caulobacter crescentus* as a Model for Bacterial Cell Biology.” *Journal of Bacteriology* 205(2), February 2023. DOI: [10.1128/jb.00384-22](https://doi.org/10.1128/jb.00384-22). (barrows2023synchronizedswarmersand pages 11-13)
4. **Banks EJ, et al.** “Asymmetric peptidoglycan editing generates cell curvature in *Bdellovibrio* predatory bacteria.” *Nature Communications* 13:1509, March 2022. DOI: [10.1038/s41467-022-29007-y](https://doi.org/10.1038/s41467-022-29007-y). (banks2022asymmetricpeptidoglycanediting pages 4-6, banks2022asymmetricpeptidoglycanediting pages 1-2)
5. **Peschek N, et al.** “RNA-mediated control of cell shape modulates antibiotic resistance in *Vibrio cholerae*.” *Nature Communications* 11:6067, November 2020. DOI: [10.1038/s41467-020-19890-8](https://doi.org/10.1038/s41467-020-19890-8). (nikolai2020rnamediatedcontrolof pages 4-6, nikolai2020rnamediatedcontrolof pages 1-2)
6. **Fernandez NL, et al.** “*Vibrio cholerae* adapts to sessile and motile lifestyles by cyclic di-GMP regulation of cell shape.” *Proceedings of the National Academy of Sciences* 117:29046–29054, November 2020. DOI: [10.1073/pnas.2010199117](https://doi.org/10.1073/pnas.2010199117). (fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 1-1)
7. **Cabeen MT, et al.** “Mutations in the Lipopolysaccharide Biosynthesis Pathway Interfere with Crescentin-Mediated Cell Curvature in *Caulobacter crescentus*.” *Journal of Bacteriology* 192:3368–3378, July 2010. DOI: [10.1128/JB.01371-09](https://doi.org/10.1128/JB.01371-09). (cabeen2010mutationsinthe pages 1-2, cabeen2010mutationsinthe pages 5-7)
8. **Cabeen MT, et al.** “Bacterial cell curvature through mechanical control of cell growth.” *The EMBO Journal* 28:1208–1219, published online 12 March 2009. DOI: [10.1038/emboj.2009.61](https://doi.org/10.1038/emboj.2009.61). (cabeen2009bacterialcellcurvature pages 1-2, cabeen2009bacterialcellcurvature pages 6-7)
9. **Ausmees N, Kuhn JR, Jacobs-Wagner C.** “The bacterial cytoskeleton: an intermediate filament-like function in cell shape.” *Cell* 115:705–713, December 2003. DOI: [10.1016/S0092-8674(03)00935-8](https://doi.org/10.1016/S0092-8674(03)00935-8). This is the supplied foundational evidence for crescentin necessity and remains appropriate provenance for the existing graph.

## Recommended curation decision

Retain the existing **crescent_shaped_crescentin_curvature** graph as a **Caulobacter-specific branch**, update its crescentin structure/localization nodes with the 2024 evidence, and add separate branches for **CrvAB/VadR/cyclic-di-GMP**, **Bd1075-dependent asymmetric peptidoglycan editing**, and **Por39/Por41–PapS–elongasome entrapment**. All branches should converge on **“METPO:1000669”** through an intermediate process such as **asymmetric longitudinal cell-envelope growth/remodeling**. This captures the shared physical principle without falsely asserting conserved molecular machinery.

References

1. (liu2024filamentstructureand pages 6-8): Yue Liu, Fusinita van den Ent, and Jan Löwe. Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin. Proceedings of the National Academy of Sciences, Feb 2024. URL: https://doi.org/10.1073/pnas.2309984121, doi:10.1073/pnas.2309984121. This article has 7 citations and is from a highest quality peer-reviewed journal.

2. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

3. (sundararajan2017cytoskeletalproteinsin pages 16-17): Kousik Sundararajan and Erin D. Goley. Cytoskeletal proteins in caulobacter crescentus: spatial orchestrators of cell cycle progression, development, and cell shape. Sub-cellular biochemistry, 84:103-137, Jan 2017. URL: https://doi.org/10.1007/978-3-319-53047-5\_4, doi:10.1007/978-3-319-53047-5\_4. This article has 25 citations.

4. (cabeen2009bacterialcellcurvature pages 1-2): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

5. (cabeen2009bacterialcellcurvature pages 6-7): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 203 citations.

6. (liu2024filamentstructureand pages 10-11): Yue Liu, Fusinita van den Ent, and Jan Löwe. Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin. Proceedings of the National Academy of Sciences, Feb 2024. URL: https://doi.org/10.1073/pnas.2309984121, doi:10.1073/pnas.2309984121. This article has 7 citations and is from a highest quality peer-reviewed journal.

7. (barrows2023synchronizedswarmersand pages 11-13): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 61 citations and is from a peer-reviewed journal.

8. (cabeen2010mutationsinthe pages 1-2): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

9. (cabeen2010mutationsinthe pages 5-7): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

10. (nikolai2020rnamediatedcontrolof pages 1-2): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 46 citations and is from a highest quality peer-reviewed journal.

11. (nikolai2020rnamediatedcontrolof pages 4-6): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 46 citations and is from a highest quality peer-reviewed journal.

12. (fernandez2020vibriocholeraeadapts pages 5-6): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

13. (fernandez2020vibriocholeraeadapts pages 1-1): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 53 citations and is from a highest quality peer-reviewed journal.

14. (banks2022asymmetricpeptidoglycanediting pages 1-2): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

15. (banks2022asymmetricpeptidoglycanediting pages 4-6): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

16. (pohl2024anoutermembrane pages 4-5): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (pohl2024anoutermembrane pages 13-14): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

18. (pohl2024anoutermembrane pages 7-8): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.