---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:53:46.826692'
end_time: '2026-08-04T10:00:32.941279'
duration_seconds: 406.11
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spiral shaped
  trait_identifier: METPO:1000684
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spiral_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a spiral or helically curved morphology
    rather than a straight rod or sphere.
  parent_traits: METPO:1000666
  synonyms: S_curved_spiral, spiral, spiral-shaped
  evidence_summary: 'DOI:10.1371/journal.pbio.1002565: spirillar types (Supports spiral/spirillar
    morphology as a recognized bacterial cell-shape class within broader bacterial
    morphology diversity.)'
  causal_graph_summary: 'spiral_shaped_curvature_mechanisms: 11 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spiral shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000684
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spiral or helically curved morphology rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, spiral, spiral-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: spirillar types (Supports spiral/spirillar morphology as a recognized bacterial cell-shape class within broader bacterial morphology diversity.)
- **Existing causal graph summary:** spiral_shaped_curvature_mechanisms: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **spiral shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spiral_shaped.yaml`.

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
- **Trait label:** spiral shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000684
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spiral or helically curved morphology rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, spiral, spiral-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: spirillar types (Supports spiral/spirillar morphology as a recognized bacterial cell-shape class within broader bacterial morphology diversity.)
- **Existing causal graph summary:** spiral_shaped_curvature_mechanisms: 11 nodes, 10 edges

## Research Objective

Research the microbial trait **spiral shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spiral_shaped.yaml`.

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


# Curation-focused research report: microbial trait “spiral shaped”

## Executive summary

The target is the reviewed morphology class **“spiral shaped”**, identifier **“METPO:1000684”**, parent **METPO:1000666**. It denotes a whole microbial cell whose longitudinal axis has persistent helical curvature/twist rather than being a straight rod or sphere. The evidence supports **multiple, non-universal causal architectures**: (i) spatial remodeling of the peptidoglycan sacculus in *Helicobacter pylori* and *Campylobacter jejuni*; (ii) membrane-associated MreB/fibril cytoskeletons in wall-less *Spiroplasma*; and (iii) cell-wall/periplasmic-flagellar mechanics in spirochetes. These mechanisms should be represented as taxon-scoped branches rather than merged into one universal pathway.

The strongest graph-ready chain is:

> **peptidoglycan hydrolase or shape-complex activity → altered peptidoglycan crosslink/muropeptide architecture → helical curvature and twist → enhanced host colonization in a specified assay**.

In *H. pylori*, csd/ccmA mutants have **20–50% more tetrapentapeptide crosslinking**, and shape mutants are attenuated in stomach colonization despite apparently normal motility. In *C. jejuni*, deletion of **pgp1** changes cells from helical to rod-shaped and reduces chick colonization by **more than three orders of magnitude**. These are unusually strong links between molecular activity, wall chemistry, cell geometry, and an ecological/pathogenic outcome. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)

## 1. Trait scope and boundaries

### Included phenotype

For TraitMech, the node should represent an **assay-observed whole-cell morphology** with both longitudinal curvature and repeated twist/helical pitch. In *H. pylori*, helicity can be decomposed into elongation, curvature, and twist; shape mutations can affect these components separately. (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2)

Appropriate observations include phase-contrast microscopy, electron or cryoelectron microscopy, and quantitative centerline measurements showing pitch, radius, handedness, or repeated curvature. The trait is structural, not itself a physiological capacity.

### Boundary cases

- **Curved rod:** curvature without repeated axial twist is an adjacent phenotype, not necessarily spiral shaped. Several *C. jejuni* and *H. pylori* mutants are curved rods rather than fully helical cells. (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5, frirdich2023multiplecampylobacterjejuni pages 3-5)
- **Straight rod, coccoid, spherical, filamentous, or pleomorphic cells:** these are alternate morphologies. Growth phase and stress can cause transitions, so assay conditions and life-cycle stage should be recorded.
- **Helical flagellar filament:** the shape of an external flagellum is not evidence that the whole cell is spiral shaped.
- **Spirochete wave or bend:** “spiral,” “wavy,” and hooked-end morphologies can have distinct mechanical origins. Periplasmic flagella may determine terminal bending without being solely responsible for the cylindrical body’s underlying helicity.
- **Kink propagation and swimming:** these are dynamic motility phenotypes. They should be separate nodes. MreB5 can produce helicity and kinks in a heterologous wall-less cell without producing efficient broth swimming, directly demonstrating that shape, kink generation, and productive motility are separable. (lartigue2022cytoskeletalcomponentscan pages 7-8, lartigue2022cytoskeletalcomponentscan pages 1-2)
- **Colonization or virulence:** these are downstream organism–environment outcomes, not synonyms for spiral shape. They require host, site, and assay qualifiers.

## 2. Current mechanistic understanding

### 2.1 Peptidoglycan-remodeling route

In walled Gram-negative bacteria, morphology is encoded physically in the peptidoglycan sacculus. In *H. pylori*, Csd1, Csd2, Csd3, and the bactofilin CcmA coordinate relaxation or spatial redistribution of peptidoglycan crosslinks. Their disruption changes both intact-cell and isolated-sacculus geometry, supporting a wall-encoded—not merely membrane- or flagellum-induced—shape mechanism. Csd-family proteins contain LytM-related peptidase domains; loss of Csd3 causes variable curvature and abnormal pitch, reversible by complementation. (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5)

The quantitative chemical result is especially useful for a causal graph: csd/ccmA mutants show **20–50% increases in tetrapentapeptide crosslinking**. The proposed physical mechanism is localized hydrolysis of mDap–D-Ala crosslinks: differential relaxation across the cell produces curvature, while patterned or diagonal relaxation contributes twist. The precise spatial-mechanical subedges remain partly model-based, whereas the gene→crosslinking and crosslinking→shape relationships are experimentally strong. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)

Csd5 is a candidate scaffold connecting the periplasmic wall to cytosolic morphogenesis machinery: it binds peptidoglycan and interacts with CcmA and MurF, supporting a membrane-associated “shapesome” that coordinates precursor synthesis, cytoskeleton, and wall remodeling. This protein-interaction architecture is well supported, but converting each physical interaction into a directional causal edge requires care. (salama2020cellmorphologyas pages 5-6)

In *C. jejuni*, the clearest enzyme is Pgp1, a peptidoglycan DL-carboxypeptidase that converts monomeric tripeptides to dipeptides. Deleting pgp1 yields rod-shaped cells; both loss and overexpression disturb morphology, motility, and biofilm behavior, indicating that the correct activity level—not merely presence—is important. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2)

Pgp3 provides a second chemical route. It has DD-carboxypeptidase and DD-endopeptidase activities, and deletion produces a curved-rod phenotype, suggesting modulation of degree of helicity rather than a simple binary switch. (lin2021peptidoglycanbindingby pages 42-46)

### 2.2 Cytoskeleton–membrane route in wall-less bacteria

*Spiroplasma* lacks peptidoglycan and therefore cannot use sacculus remodeling. Heterologous reconstruction in spherical *Mycoplasma capricolum* showed that Spiroplasma MreB proteins and fibril can induce helicity and kink propagation. **MreB5 alone was sufficient** to produce helicity and kinks; cryoelectron microscopy showed membrane-associated MreB filaments, supporting direct membrane-curvature generation. (lartigue2022cytoskeletalcomponentscan pages 1-2, lartigue2022cytoskeletalcomponentscan pages 6-7)

Fibril and MreB5 cooperate to stabilize extended helices, while MreB5 helps position MreB1 and fibril at the membrane. The proposed force-transmission model—MreB polymers acting through fibril to deform the membrane—is mechanistically plausible and imaging-supported, but some detailed force-direction and handedness steps remain model-level. Functions of MreB2–MreB4 are not yet sufficiently resolved. (lartigue2022cytoskeletalcomponentscan pages 8-9)

### 2.3 Spirochete route

Spirochetes combine a peptidoglycan-containing cell cylinder with periplasmic flagella. Rotation and mechanical coupling of these flagella affect whole-cell waveform, bending, and propulsion. This is a distinct route from both epsilon-proteobacterial peptidoglycan sculpting and wall-less Spiroplasma cytoskeletons. The available evidence here is primarily review-level; primary perturbation studies should be added before specific flagellar proteins are curated as core causes of the broad spiral-shaped trait.

## 3. Candidate nodes grouped by type

### Trait and phenotype nodes

- **spiral shaped — “METPO:1000684”**
- helical curvature — label-only candidate
- helical twist / pitch — label-only candidate
- curved-rod morphology — label-only boundary node
- straight-rod morphology — label-only alternative
- coccoid or spherical morphology — label-only alternative
- kink propagation — label-only dynamic phenotype
- swimming motility — **GO:0048870** may be considered only after curator verification of intended scope
- host colonization — label-only; qualify by host and anatomical site

### Cellular structures and locations

- peptidoglycan sacculus / peptidoglycan-based cell wall — use an appropriate GO cellular-component term after ontology verification
- periplasm — **GO:0042597**, subject to release verification
- plasma/cytoplasmic membrane — use a verified GO cellular-component term
- bacterial cytoskeleton — label-only unless a suitable current GO term is confirmed
- periplasmic flagellum — label-only candidate
- MreB/fibril membrane-associated filament — label-only complex
- *H. pylori* shapesome — label-only complex

### Genes and proteins

**Taxon-specific *H. pylori* candidates:** Csd1, Csd2, Csd3, Csd4, Csd5, Csd6, Csd7, CcmA, MurF. Csd1/2/3 and CcmA have the strongest direct shape evidence; Csd5 is best represented initially as a PG-binding scaffold interacting with CcmA and MurF. (salama2020cellmorphologyas pages 5-6, sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5)

**Taxon-specific *C. jejuni* candidates:** Pgp1, Pgp2, Pgp3, Cj1104, Cj1105, Cj0166, and Cj1228. The 2023 study identifies Cj1104 as a bactofilin homolog and the other candidates as M23-domain proteins, but homologous proteins can have different effects even between *C. jejuni* and *H. pylori*. (frirdich2023multiplecampylobacterjejuni pages 3-5)

**Wall-less *Spiroplasma* candidates:** MreB1, MreB5, fibril; MreB2–MreB4 should remain provisional. (lartigue2022cytoskeletalcomponentscan pages 1-2, lartigue2022cytoskeletalcomponentscan pages 8-9)

**Spirochete candidates:** periplasmic flagellar filament and motor components, MreB, and cell-cylinder peptidoglycan. Specific gene-level edges require primary-source validation.

Protein identifiers should be strain-specific UniProt CURIEs. None should be assigned from gene names alone because paralogy and strain-dependent locus naming create a substantial mapping risk.

### Molecular functions and processes

- peptidoglycan DL-carboxypeptidase activity — verified GO/EC identifier should be added after checking substrate stereochemistry
- peptidoglycan DD-carboxypeptidase activity
- peptidoglycan DD-endopeptidase activity
- peptidoglycan crosslink hydrolysis/relaxation
- peptidoglycan precursor synthesis by MurF
- cytoskeletal filament polymerization
- membrane curvature generation
- peptidoglycan binding
- spatial localization/recruitment of PG synthesis machinery

### Chemicals and chemical structures

- peptidoglycan
- mDap–D-Ala crosslink
- monomeric PG tripeptide
- monomeric PG dipeptide
- A22, an MreB-perturbing chemical—use a CHEBI CURIE only after identity/salt verification
- phalloidin—use a verified CHEBI identifier only after confirming the compound form used

No electron donor, electron acceptor, nutrient, or metabolic pathway has strong evidence as a direct determinant of this morphology in the retrieved mechanistic studies. Such nodes should not be inserted merely to fill metabolic categories.

### Environmental and experimental contexts

- gastric mucus and mammalian stomach colonization (*H. pylori*)
- chick intestinal/cecal colonization (*C. jejuni*)
- broth swimming assay
- growth phase in *Spiroplasma*
- heterologous expression in *Mycoplasma capricolum*
- A22 or phalloidin exposure
- microscopy and PG-muropeptide profiling

## 4. Candidate causal edges

The table below is intended as an evidence ledger, not as a claim that all branches belong in one organism-level graph.

| taxon/context | subject | predicate | object | evidence snippet | DOI/date | confidence and curation note |
|---|---|---|---|---|---|---|
| *Helicobacter pylori* | Csd1/Csd2/Csd3/CcmA | promotes | relaxed peptidoglycan crosslinking | "All four proteins influence peptidoglycan crosslinking" and mutants show "20–50% increases in tetrapentapeptide crosslinking"; mechanism proposed as "selective hydrolysis of mDap–D-Ala peptidoglycan crosslinks" (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10, sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5) | 10.1016/j.cell.2010.03.046; 2010-05 | High; direct genetic and PG-chemistry evidence in *H. pylori*. Curate as taxon-specific morphogenesis module rather than universal bacterial spiral mechanism. |
| *Helicobacter pylori* | relaxed peptidoglycan crosslinking | promotes | helical cell shape | "Peptidoglycan crosslinking relaxation promotes *Helicobacter pylori*'s helical shape" and the proteins "function coordinately to relax peptidoglycan crosslinks, enabling helical curvature and twist" (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10) | 10.1016/j.cell.2010.03.046; 2010-05 | High; direct title-level and experimental support. Useful core edge for TraitMech. |
| *Helicobacter pylori* | Csd3 loss | causes | severe helical morphology defects / aberrant pitch | "Loss of csd3 causes severe morphological abnormalities including variable curvature and aberrant helical pitch, with normal morphology restored by complementation" (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5) | 10.1016/j.cell.2010.03.046; 2010-05 | High; direct perturbation edge. Object should remain phenotype-level unless finer morphology terms are available. |
| *Helicobacter pylori* | helical cell shape | promotes | stomach colonization | "three shape mutants were attenuated for stomach colonization despite apparently normal motility, demonstrating that helical shape itself—not motility enhancement—is required for robust colonization" (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10) | 10.1016/j.cell.2010.03.046; 2010-05 | High; important boundary-case edge separating morphology from motility. Curate as host-context phenotype. |
| *Campylobacter jejuni* | Pgp1 | has activity | peptidoglycan DL-carboxypeptidase converting tripeptides to dipeptides | "Pgp1 functions as a peptidoglycan DL-carboxypeptidase that cleaves monomeric tripeptides to dipeptides" (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602; 2012-03 | High; direct biochemical evidence. Good enzyme-to-PG-chemistry edge. |
| *Campylobacter jejuni* | Pgp1-mediated PG modification | promotes | helical cell shape | "Deletion of pgp1 causes dramatic morphological change from helical to rod-shaped cells" (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602; 2012-03 | High; direct gene-to-trait evidence. Recommended core edge for *C. jejuni*. |
| *Campylobacter jejuni* | pgp1 deletion | causes | rod shape | "Deletion of pgp1 resulted in a striking, rod-shaped morphology" (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602; 2012-03 | High; direct knockout phenotype. Useful negative regulator edge if encoding wild-type gene presence as required for spiral shape. |
| *Campylobacter jejuni* | rod-shaped pgp1 mutant | decreases | chick colonization | "the rod-shaped pgp1 mutant was deficient in chick colonization by over three orders of magnitude" (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602; 2012-03 | High; quantitative host-associated outcome. Curate carefully as morphology-associated pathogenesis edge. |
| *Campylobacter jejuni* | Pgp3 | has activity | DD-carboxypeptidase and DD-endopeptidase activities | "Pgp3 is a bifunctional metalloprotease with DD-carboxypeptidase and DD-endopeptidase activities" (lin2021peptidoglycanbindingby pages 42-46) | 10.1038/s41467-019-13934-4; 2020-01 | High; direct enzymology, but role is in degree of helicity rather than binary spiral/not-spiral. |
| *Campylobacter jejuni* | pgp3 deletion | causes | curved-rod morphology | "Pgp3 deletion produces curved-rod morphology" (lin2021peptidoglycanbindingby pages 42-46) | 10.1038/s41467-019-13934-4; 2020-01 | Medium-high; direct but phenotype is intermediate/boundary case, not loss to straight rod in all contexts. |
| *Campylobacter jejuni* | 1104 / 1105 / 0166 / 1228 perturbation | alters | peptidoglycan structure and degree of helical curvature | "Deletions in the corresponding genes resulted in varying curved rod morphologies with changes in their PG muropeptide profiles" and "Overexpression of 1104 and 1105 also resulted in changes in the morphology and in the muropeptide profiles" (frirdich2023multiplecampylobacterjejuni pages 3-5) | 10.3389/fmicb.2023.1162806; 2023-04 | Medium; direct for morphology/PG alteration, but mostly taxon-specific candidate nodes and often curved-rod outcomes. Mark uncertain for broad TraitMech generalization. |
| wall-less *Spiroplasma* components in *Mycoplasma capricolum* heterologous system | MreB5 | is sufficient for | helicity and kink propagation | "MreB isoform 5 alone is sufficient to induce helicity and kink propagation" (lartigue2022cytoskeletalcomponentscan pages 1-2) | 10.1038/s41467-022-34478-0; 2022-11 | High within heterologous assay; curate as wall-less, assay-specific mechanism not directly transferable to walled spiral bacteria. |
| wall-less *Spiroplasma* components in *Mycoplasma capricolum* heterologous system | fibril and MreB proteins | promote | membrane curvature / helical shape / kinking ability | "Spiroplasma fibril and MreB proteins confers helical shape and kinking ability" and cryo-EM showed membrane-associated filaments indicating "a direct effect on membrane curvature" (lartigue2022cytoskeletalcomponentscan pages 1-2, lartigue2022cytoskeletalcomponentscan pages 6-7) | 10.1038/s41467-022-34478-0; 2022-11 | High for heterologous reconstitution. Strong evidence for non-PG helical mechanism in Mollicutes. |
| wall-less *Spiroplasma* components in *Mycoplasma capricolum* heterologous system | MreB/Fib expression | does not efficiently produce | swimming motility in broth | "did not produce efficient swimming motility in culture broth" and additional unknown components are required (lartigue2022cytoskeletalcomponentscan pages 1-2, lartigue2022cytoskeletalcomponentscan pages 7-8) | 10.1038/s41467-022-34478-0; 2022-11 | High; important negative edge distinguishing helical morphology/kinking from full swimming behavior. |
| *Spiroplasma eriocheiris* chemical perturbation | A22 | decreases | pathogenicity and alters morphology via MreB expression changes | "A22 affect the *S. eriocheiris* morphology by altering MreB expression" and "the pathogenicity of *S. eriocheiris* decreased after treatment with A22" (li2024decipheringtheimpact pages 1-2) | 10.1186/s13062-024-00537-3; 2024-10 | Medium; direct but chemical/assay-specific and based on inhibitor treatment, not gene knockout. Curate with caution. |
| *Spiroplasma eriocheiris* chemical perturbation | phalloidin | increases | pathogenicity and alters morphology via MreB expression changes | "Phalloidin and A22 affect the *S. eriocheiris* morphology by altering MreB expression" and "the ability of *S. eriocheiris* to invade *E. sinensis* was increased after treatment with Phalloidin" (li2024decipheringtheimpact pages 1-2) | 10.1186/s13062-024-00537-3; 2024-10 | Medium; direct but assay-specific chemical effect, not a stable endogenous morphogenesis edge. |
| spirochetes | periplasmic flagella | shape | spiral/bent whole-cell morphology | spirochetes have "spiral (or wavy) cell bodies and endoflagella that reside within the periplasmic space"; "Leptospira PF depletion affects only the bent morphology" (lartigue2022cytoskeletalcomponentscan pages 1-2) | 10.3390/biom10040550; 2020-04 | Medium; mechanistically authoritative but retrieved support is review-style summary rather than primary perturbation details here. Curate as broader comparative context, not core trait edge unless primary source added. |


*Table: This table summarizes the strongest curation-ready causal triples linking genes, peptidoglycan chemistry, cytoskeletal elements, and assay perturbations to microbial spiral/helical morphology. It emphasizes direct perturbation evidence, notes taxon specificity, and flags host- or assay-dependent claims for cautious curation.*

### Recommended minimal graph for immediate curation

The following high-confidence edges are the best initial additions to `spiral_shaped.yaml`:

1. **H. pylori Csd1/Csd2/Csd3/CcmA activity → decreases or relaxes selected peptidoglycan crosslinking.**
2. **Relaxed/spatially patterned peptidoglycan crosslinking → promotes helical curvature and twist → “METPO:1000684”.**
3. **H. pylori spiral shape → promotes robust stomach colonization**, with a host-context qualifier and evidence that mutant motility remained apparently normal. (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
4. **C. jejuni Pgp1 → catalyzes PG tripeptide-to-dipeptide conversion.**
5. **Pgp1-mediated PG remodeling → promotes spiral shape; pgp1 deletion → rod shape.**
6. **C. jejuni spiral/normal morphology → promotes chick colonization**, annotated as morphology-associated because pgp1 can have pleiotropic envelope effects. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2)
7. In a separate wall-less-taxon branch, **Spiroplasma MreB5 polymerization/membrane association → membrane curvature → helical shape and kink propagation.** (lartigue2022cytoskeletalcomponentscan pages 1-2, lartigue2022cytoskeletalcomponentscan pages 6-7)

## 5. Recent developments, 2023–2024

### Expanded *Campylobacter* morphogenesis network (April 2023)

Frirdich and colleagues extended the established Pgp1/Pgp2 network to Cj1104, Cj1105, Cj0166, and Cj1228. Deletions generated varying curved-rod morphologies with altered muropeptide profiles; overexpression of Cj1104 and Cj1105 also changed morphology and muropeptides. The important current conclusion is that **protein dosage and species-specific PG networks control degree of curvature**, and apparently homologous proteins do not guarantee conserved phenotypic direction across related taxa. (frirdich2023multiplecampylobacterjejuni pages 3-5)

### Chemical perturbation of wall-less *Spiroplasma* (October 2024)

A 2024 *S. eriocheiris* study reported that A22 and phalloidin changed morphology together with MreB expression. Phalloidin increased invasion and several host-cell injury readouts, whereas A22 decreased pathogenicity. This gives a recent applied link between cytoskeletal perturbation, morphology, and aquaculture disease, but it is weaker for core graph curation than a targeted knockout or allelic replacement because both chemicals may be pleiotropic and morphology was coupled to expression changes rather than a clean structural mechanism. (li2024decipheringtheimpact pages 1-2)

### Current expert interpretation

The literature now favors **distributed morphogenesis systems** over a single “spiral-shape gene.” Enzymes set local wall chemistry; scaffolds and bactofilins position activities; dosage determines the degree of curvature; and distinct taxa can reach visually similar helices through nonhomologous physical systems. The 2023 comparative work explicitly warns that related organisms with similar morphologies and homologous proteins can have different PG biosynthetic outcomes. (frirdich2023multiplecampylobacterjejuni pages 3-5)

## 6. Applications and real-world relevance

- **Anti-virulence targeting:** shape determinants are attractive because disrupting morphology can reduce colonization without necessarily blocking growth. *H. pylori* shape mutants lose colonization fitness even when motility appears normal, suggesting a niche-specific anti-colonization strategy. However, no clinical implementation is established. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
- **Food safety and enteric infection:** *C. jejuni* Pgp1 links wall chemistry and geometry to motility, biofilm behavior, immune sensing, and avian colonization. The >1,000-fold chick-colonization defect highlights potential relevance to poultry reservoirs, but Pgp1 pleiotropy complicates attribution solely to shape. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2)
- **Aquaculture disease control:** the 2024 A22 result suggests MreB perturbation could reduce *S. eriocheiris* pathogenicity, but pharmacology, toxicity, specificity, environmental persistence, and resistance remain unresolved. (li2024decipheringtheimpact pages 1-2)
- **Synthetic morphology and microrobotics:** transferring Spiroplasma MreB/fibril components into wall-less Mycoplasma demonstrates partial engineering of helicity and kinks. Failure to obtain efficient swimming shows that morphology alone is insufficient for a functional motility chassis. (lartigue2022cytoskeletalcomponentscan pages 7-8, lartigue2022cytoskeletalcomponentscan pages 1-2)
- **Diagnostic morphology:** spiral shape can aid microscopy-based recognition, but morphology varies with growth phase and stress and therefore should not be treated as a species-exclusive diagnostic marker.

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not encode one universal spiral-shape pathway.** Peptidoglycan remodeling, wall-less cytoskeletal deformation, and spirochete flagellar mechanics are distinct, taxon-bounded mechanisms.
2. **Do not equate spiral shape with motility.** Normal motility can coexist with colonization-defective *H. pylori* shape mutants, while engineered helices can kink yet fail to swim efficiently. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10, lartigue2022cytoskeletalcomponentscan pages 1-2)
3. **Do not curate corkscrew penetration as a proven universal edge.** It is a plausible physical interpretation, but direct causal evidence varies by organism and medium.
4. **Do not infer conserved function from homology alone.** Cj1104/1105/1228 and *H. pylori* homologs can yield different morphology or muropeptide effects. (frirdich2023multiplecampylobacterjejuni pages 3-5)
5. **Treat Cj1104 complementation cautiously.** The reported deletion phenotype was not complemented under the tested conditions, unlike the other candidates; polarity, expression level, or secondary effects must be excluded before a definitive gene→shape edge.
6. **Treat A22 and phalloidin edges as inhibitor- and assay-specific.** They are not substitutes for clean genetic evidence and should not be represented as endogenous pathway components. (li2024decipheringtheimpact pages 1-2)
7. **Do not assign unverified CURIEs.** Protein identifiers must be strain-specific; chemical IDs must match the exact compound form; GO/EC terms must match demonstrated substrate chemistry.
8. **Separate direct from downstream effects.** Colonization, biofilm formation, immune sensing, and pathogenicity can result from altered PG composition independently of gross shape.
9. **Do not curate detailed spatial mechanics as settled fact.** Local outer-curvature hydrolysis and diagonal relaxation are useful models, but the experimentally strongest result is the association of altered crosslink chemistry with altered sacculus and cell shape. (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
10. **Spirochete protein-level edges need primary evidence.** The present support is sufficient for comparative context, not for a detailed flagellar causal module.

## 8. DOI-first bibliography

1. Sycuro LK et al. **Peptidoglycan Crosslinking Relaxation Promotes *Helicobacter pylori*’s Helical Shape and Stomach Colonization.** *Cell*. Published May 2010. DOI: [10.1016/j.cell.2010.03.046](https://doi.org/10.1016/j.cell.2010.03.046). (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
2. Frirdich E et al. **Peptidoglycan-Modifying Enzyme Pgp1 Is Required for Helical Cell Shape and Pathogenicity Traits in *Campylobacter jejuni*.** *PLoS Pathogens*. Published March 2012. DOI: [10.1371/journal.ppat.1002602](https://doi.org/10.1371/journal.ppat.1002602). (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2)
3. Blair KM et al. **The *Helicobacter pylori* cell shape promoting protein Csd5 interacts with the cell wall, MurF, and the bacterial cytoskeleton.** *Molecular Microbiology*. Published September 2018. DOI: [10.1111/mmi.14087](https://doi.org/10.1111/mmi.14087). (salama2020cellmorphologyas pages 5-6)
4. Min K et al. **Peptidoglycan reshaping by a noncanonical peptidase for helical cell shape in *Campylobacter jejuni*.** *Nature Communications*. Published January 2020. DOI: [10.1038/s41467-019-13934-4](https://doi.org/10.1038/s41467-019-13934-4). (lin2021peptidoglycanbindingby pages 42-46)
5. Salama NR. **Cell morphology as a virulence determinant: lessons from *Helicobacter pylori*.** *Current Opinion in Microbiology*. Published April 2020. DOI: [10.1016/j.mib.2019.12.002](https://doi.org/10.1016/j.mib.2019.12.002). (salama2020cellmorphologyas pages 5-6)
6. Nakamura S. **Spirochete Flagella and Motility.** *Biomolecules*. Published April 2020. DOI: [10.3390/biom10040550](https://doi.org/10.3390/biom10040550).
7. Lartigue C et al. **Cytoskeletal components can turn wall-less spherical bacteria into kinking helices.** *Nature Communications*. Published November 2022. DOI: [10.1038/s41467-022-34478-0](https://doi.org/10.1038/s41467-022-34478-0). (lartigue2022cytoskeletalcomponentscan pages 7-8, lartigue2022cytoskeletalcomponentscan pages 1-2)
8. Frirdich E et al. **Multiple *Campylobacter jejuni* proteins affecting the peptidoglycan structure and the degree of helical cell curvature.** *Frontiers in Microbiology*. Published April 2023. DOI: [10.3389/fmicb.2023.1162806](https://doi.org/10.3389/fmicb.2023.1162806). (frirdich2023multiplecampylobacterjejuni pages 3-5)
9. Li R et al. **Deciphering the impact of MreB on the morphology and pathogenicity of the aquatic pathogen *Spiroplasma eriocheiris*.** *Biology Direct*. Published October 2024. DOI: [10.1186/s13062-024-00537-3](https://doi.org/10.1186/s13062-024-00537-3). (li2024decipheringtheimpact pages 1-2)

## Curation recommendation

Retain **“METPO:1000684”** as the shared terminal morphology node, but create taxon-qualified upstream modules. The first production-quality module should center on *H. pylori* Csd/CcmA-mediated PG relaxation; a second should center on *C. jejuni* Pgp1/Pgp3-mediated muropeptide remodeling; and a separate wall-less branch should represent Spiroplasma MreB5/fibril-driven membrane curvature. Downstream colonization edges should carry explicit host, anatomical-site, and assay qualifiers.

References

1. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2): Emilisa Frirdich, Jacob Biboy, Calvin Adams, Jooeun Lee, Jeremy Ellermeier, Lindsay Davis Gielda, Victor J. DiRita, Stephen E. Girardin, Waldemar Vollmer, and Erin C. Gaynor. Peptidoglycan-modifying enzyme pgp1 is required for helical cell shape and pathogenicity traits in campylobacter jejuni. PLoS Pathogens, 8:e1002602, Mar 2012. URL: https://doi.org/10.1371/journal.ppat.1002602, doi:10.1371/journal.ppat.1002602. This article has 139 citations and is from a highest quality peer-reviewed journal.

2. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

3. (sycuro2010peptidoglycancrosslinkingrelaxation pages 1-2): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

4. (sycuro2010peptidoglycancrosslinkingrelaxation pages 4-5): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

5. (frirdich2023multiplecampylobacterjejuni pages 3-5): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 11 citations and is from a peer-reviewed journal.

6. (lartigue2022cytoskeletalcomponentscan pages 7-8): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

7. (lartigue2022cytoskeletalcomponentscan pages 1-2): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

8. (salama2020cellmorphologyas pages 5-6): Nina R Salama. Cell morphology as a virulence determinant: lessons from helicobacter pylori. Apr 2020. URL: https://doi.org/10.1016/j.mib.2019.12.002, doi:10.1016/j.mib.2019.12.002. This article has 44 citations and is from a peer-reviewed journal.

9. (lin2021peptidoglycanbindingby pages 42-46): Chang Sheng-Huei Lin. Peptidoglycan binding by pgp2 and ape1 determines campylobacter jejuni helical cell shape. ArXiv, Jan 2021. URL: https://doi.org/10.14288/1.0401780, doi:10.14288/1.0401780. This article has 0 citations.

10. (lartigue2022cytoskeletalcomponentscan pages 6-7): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

11. (lartigue2022cytoskeletalcomponentscan pages 8-9): Carole Lartigue, Bastien Lambert, Fabien Rideau, Yorick Dahan, Marion Decossas, Mélanie Hillion, Jean-Paul Douliez, Julie Hardouin, Olivier Lambert, Alain Blanchard, and Laure Béven. Cytoskeletal components can turn wall-less spherical bacteria into kinking helices. Nature Communications, Nov 2022. URL: https://doi.org/10.1038/s41467-022-34478-0, doi:10.1038/s41467-022-34478-0. This article has 19 citations and is from a highest quality peer-reviewed journal.

12. (li2024decipheringtheimpact pages 1-2): Rong Li, Xiaohui Cao, Jiaxin Chen, Tingting He, Yan Zhang, Wen Wang, Yaqi Wang, Yifei Wang, Yanyan Qiu, Mengji Xie, Kailin Shi, Yuhua Xu, Siyuan Zhang, and Peng Liu. Deciphering the impact of mreb on the morphology and pathogenicity of the aquatic pathogen spiroplasma eriocheiris. Biology Direct, Oct 2024. URL: https://doi.org/10.1186/s13062-024-00537-3, doi:10.1186/s13062-024-00537-3. This article has 9 citations and is from a peer-reviewed journal.