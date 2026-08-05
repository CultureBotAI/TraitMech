---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:55:36.679788'
end_time: '2026-08-04T09:04:28.313022'
duration_seconds: 531.63
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: irregular shaped
  trait_identifier: METPO:1000691
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: irregular_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape lacking a consistent geometric form across individual cells
    of a population.
  parent_traits: METPO:1000666
  synonyms: irregular
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control
    as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x:
    coryneform morphology (Corynebacterineae review supports irregular and coryneform
    morphologies associated with apical polar growth and reduced lateral wall patterning.)'
  causal_graph_summary: 'irregular_shaped_loss_of_patterning: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** irregular shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000691
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape lacking a consistent geometric form across individual cells of a population.
- **Parent traits:** METPO:1000666
- **Synonyms:** irregular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x: coryneform morphology (Corynebacterineae review supports irregular and coryneform morphologies associated with apical polar growth and reduced lateral wall patterning.)
- **Existing causal graph summary:** irregular_shaped_loss_of_patterning: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **irregular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/irregular_shaped.yaml`.

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
- **Trait label:** irregular shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000691
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape lacking a consistent geometric form across individual cells of a population.
- **Parent traits:** METPO:1000666
- **Synonyms:** irregular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x: coryneform morphology (Corynebacterineae review supports irregular and coryneform morphologies associated with apical polar growth and reduced lateral wall patterning.)
- **Existing causal graph summary:** irregular_shaped_loss_of_patterning: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **irregular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/irregular_shaped.yaml`.

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


# Curation report: microbial trait “irregular shaped”

**Trait:** “irregular shaped”  
**Identifier:** **METPO:1000691**  
**Category:** MORPHOLOGY; **term kind:** CLASS; **mapping:** REVIEWED  
**Provided definition:** “A cell shape lacking a consistent geometric form across individual cells of a population.”  
**Parent:** METPO:1000666; **synonym:** irregular

## 1. Scope and current mechanistic interpretation

The best-supported interpretation is a **population-level failure of shape homeostasis**, not merely a noncanonical shape. Cells should vary substantially in contour, local width, curvature, branching, bulging, or pole geometry such that no consistent sphere, rod, curved rod, helix, filament, or other reproducible geometry describes the population.

For most walled bacteria, the proximate physical determinant is the peptidoglycan (PG) sacculus. Shape depends less on unusual PG chemistry than on **where and when synthesis, cleavage, and cross-linking occur**. In canonical rods, MreB-associated elongasomes pattern lateral PG insertion, whereas FtsZ-associated divisomes organize septal PG synthesis. Loss of this spatial coordination can therefore produce nonuniform, irregular contours even when PG synthesis continues. This supports the existing graph’s high-level mechanism, “loss of patterning → irregular morphology.” (caccamo2018themolecularbasis pages 1-2, kysela2016diversitytakesshape pages 4-5, shi2018howtobuild pages 2-3)

### Boundary cases

- **Stable curved, helical, branched, prosthecate, club-shaped, or V-shaped cells:** exclude when the form is reproducible and species-typical. These are noncanonical but not necessarily irregular.
- **Pleomorphism:** overlaps strongly, but is broader; it may include regulated transitions among several reproducible forms. Curate as irregular only when within-population geometric inconsistency is demonstrated.
- **Filamentation:** division failure primarily changes length. It is insufficient by itself unless cells also develop variable widths, bulges, branching, or inconsistent contours.
- **L-forms/spheroplasts:** important boundary evidence. L-forms lack PG, are pleomorphic and osmotically sensitive, and proliferate by irregular blebbing/tubulation. They support the principle that loss of the shape-bearing wall causes irregularity, but should not automatically be merged with irregular morphology in intact, walled cells. (errington2017cellwalldeficientlform pages 4-5, errington2017cellwalldeficientlform pages 1-2)
- **Size heterogeneity or asymmetric division:** not equivalent to irregular shape. Mycobacteria can show more than a twofold difference between fast- and slow-growing poles while retaining an overall rod-like geometry. (joyce2012celldivisionsite pages 1-2)
- **Assay artifacts:** apparent irregularity caused by fixation, osmotic shock, stationary-phase degeneration, segmentation errors, or mixed taxa should be excluded unless experimentally controlled.

## 2. Candidate nodes grouped by type

Ontology grounding is deliberately conservative. Labels without verified stable identifiers should remain label-only until checked against the project’s ontology release.

### Trait and taxon nodes

- **irregular shaped — METPO:1000691**
- *Escherichia coli*, *Bacillus subtilis*, *Caulobacter crescentus*, *Mycobacterium smegmatis*, *Corynebacterium glutamicum*, *Campylobacter jejuni*, *Helicobacter pylori*, *Streptomyces coelicolor* — use verified **NCBITaxon** identifiers at YAML-authoring time.

### Cellular structures and localizations

- peptidoglycan sacculus / bacterial cell wall — GO-groundable
- cytoplasmic membrane — GO-groundable
- cell pole; old pole; new pole — GO-groundable where matching terms exist
- division septum / mid-cell — GO-groundable
- intracellular membrane domain (IMD) — label-only candidate
- elongasome / Rod complex — GO-groundable if the desired ontology release contains the complex term
- divisome / FtsZ ring — GO-groundable
- polarisome — GO-groundable or label-only depending on release

### Genes, proteins, enzymes, and complexes

- **MreB**, bacterial actin homolog
- **MreC, MreD, RodZ, RodA** and PBP2; lateral-wall Rod complex
- **FtsZ**, FtsA, FtsW, FtsI/PBP3; divisome/septal PG synthesis
- **DivIVA/Wag31**; polar growth scaffold in Actinobacteria
- **MurG**; terminal cytoplasmic enzyme in PG-precursor synthesis
- **PBP1a**; bifunctional PG synthase implicated in polar/septal synthesis
- **AccA3/ACCase complexes**; fatty-acid and mycolic-acid precursor metabolism
- **Pgp1, Pgp2**; PG hydrolases shaping *C. jejuni*
- *C. jejuni* proteins **CJJ81176_0166, CJJ81176_1104, CJJ81176_1105, CJJ81176_1228**; retain locus labels unless verified UniProt accessions are added
- **CcmA** bactofilin and M23 peptidases in curved/helical bacteria
- **SepF**, Min proteins, SulA, ZapD/YacF; division-positioning/regulatory boundary nodes

### Chemicals and metabolites

- **peptidoglycan** — ChEBI-groundable
- **lipid II** — ChEBI-groundable
- N-acetylglucosamine and N-acetylmuramic acid — ChEBI-groundable
- ATP, ADP, GTP, GDP — ChEBI-groundable
- acetyl-CoA, propionyl-CoA, malonyl-CoA — ChEBI-groundable
- membrane phospholipids and branched-chain fatty acids — ChEBI-groundable
- **A22**, an MreB inhibitor — verify exact ChEBI record before use
- **fosfomycin/phosphomycin** — verify preferred ontology label and ChEBI identifier
- β-lactams, penicillins, and vancomycin — ChEBI-groundable
- HADA and other fluorescent D-amino acids — assay-reagent nodes; verify identifiers individually

### Processes and functions

- peptidoglycan biosynthetic process; PG remodeling
- spatial patterning of cell-wall synthesis
- lateral cell-wall elongation
- apical/polar growth
- septation and cytokinesis
- MreB polymerization and membrane binding
- FtsZ-ring assembly
- membrane synthesis, blebbing, tubulation, and scission
- DD-endopeptidase, DD-carboxypeptidase, transglycosylase, and transpeptidase activities — GO/EC-groundable where exact catalytic activity is known

## 3. Evidence-backed candidate causal edges

The following table gives curation-oriented triples. “Core” means suitable for the main graph; “boundary” means useful context but not sufficient by itself to assert METPO:1000691.

| Subject | Predicate | Object | Reference | Supporting snippet | Curation notes |
|---|---|---|---|---|---|
| Spatially patterned PG synthesis | maintains | consistent bacterial cell shape | 10.1016/j.tim.2017.09.012; 10.1371/journal.pbio.1002565 | PG synthesis/remodeling is spatially zoned, and different insertion patterns generate different morphologies. | **Core, broad, review-backed.** Invert cautiously as “loss of patterning causes irregular shape.” (caccamo2018themolecularbasis pages 1-2, kysela2016diversitytakesshape pages 4-5)
| MreB/Rod complex | spatially directs | lateral PG insertion | 10.1016/j.cell.2018.02.050 | MreB filaments “determine the spatiotemporal pattern of insertion of cell-wall precursors” through MreC/D and RodZ. | **Core mechanistic intermediate**, strongest for canonical rods. (shi2018howtobuild pages 2-3)
| MreB point mutation | causes | variable width, bending, or branching | 10.1016/j.cell.2018.02.050 | MreB substitutions produced “substantial intracellular width variation,” bending, and branching. | **Core but allele/taxon-specific.** These outputs directly operationalize irregularity better than simple rounding. (shi2018howtobuild pages 2-3)
| MreB inhibition by A22 | disrupts | MreB localization and shape recovery | 10.1016/j.cell.2018.02.050 | “A22 treatment disrupts MreB’s localization”; treated cells “gradually lose shape.” | **Core experimental-factor edge**, principally *E. coli*; avoid claiming every treated cell is irregular without image-level scoring. (shi2018howtobuild pages 6-7)
| RodZ loss | impairs | MreB curvature sensing/cylindrical uniformity | 10.1016/j.cell.2018.02.050 | Without RodZ, MreB loses curvature preference; cells exhibit increased intracellular width variation. | **Core, taxon-specific.** Good intermediate between loss of patterning and irregular contour. (shi2018howtobuild pages 6-7)
| ATP or GTP plus membrane lipids | facilitates | MreB protofilament assembly | 10.7554/eLife.84505 | *Geobacillus* MreB formed straight protofilament pairs on lipid surfaces with ATP or GTP, but not ADP, GDP, or nonhydrolysable ATP analogs. | **Recent biochemical edge, 2023.** Mechanistic support for MreB assembly, but not a direct irregular-shape phenotype. (mao2023ontherole pages 1-2)
| Wag31/DivIVA | directs | polar cell-wall metabolism | 10.3389/fmicb.2022.1085918 | Wag31 is essential for polar growth and “needed to direct [cell-wall] metabolism to the poles.” | **Core for Actinobacteria**, not universal across bacteria. (arejan2023polarproteinwag31 pages 1-2)
| wag31 K20A | decreases | old-pole elongation | 10.3389/fmicb.2022.1085918 | K20A showed 22% less elongation than wild type and reduced old-pole HADA staining. | **Direct, quantitative, allele-specific.** Curate to defective polar growth; link to irregular shape only if phenotype annotation confirms inconsistent geometry. (arejan2023polarproteinwag31 pages 5-7)
| wag31 L34A | decreases | new-pole elongation | 10.3389/fmicb.2022.1085918 | New-pole elongation was approximately 76% lower; about 65% of mutant cells versus 11% of wild type showed no observable new-pole elongation. | **Direct, quantitative, allele-specific.** Strong evidence for loss of balanced pole growth. (arejan2023polarproteinwag31 pages 5-7)
| wag31 D7A | causes | uncontrolled septation | 10.3389/fmicb.2022.1085918 | The authors conclude that D7A “causes septation to occur in an uncontrolled manner.” | **Direct but allele-specific.** Strong candidate upstream cause of heterogeneous morphology. (arejan2023polarproteinwag31 pages 5-7)
| Wag31 K20A/L34A | decreases | ACCase activity | 10.3389/fmicb.2022.1085918 | Mutant lysates showed decreased acetyl-CoA carboxylase activity; results were from three independent experiments. | **Direct biochemical edge.** The path from ACCase change to irregular shape remains unresolved and should be uncertain. (arejan2023polarproteinwag31 pages 9-11)
| Wag31 depletion | delocalizes | intracellular membrane domain | 10.3389/fmicb.2022.1085918 | Prior work showed that Wag31 depletion delocalizes the IMD. | **Secondary evidence.** The 2023 study found pole elongation did not correlate with MurG/GlfT2 localization, so do not assert this as the operative causal route. (arejan2023polarproteinwag31 pages 9-11)
| Differential polar PG growth | causes | asymmetric daughter growth | 10.1371/journal.pone.0044582 | Fast and slow poles differed by more than twofold in growth rate, while septa remained accurately placed at mid-cell. | **Boundary mechanism.** Asymmetry is not itself irregular shape. (joyce2012celldivisionsite pages 1-2)
| PG-precursor synthesis inhibition by fosfomycin | induces | wall-deficient L-form transition | 10.1042/BST20160435 | Antibiotics blocking wall-precursor synthesis, “such as phosphomycin,” efficiently induced L-forms without genetic change. | **Boundary, condition-dependent.** Requires osmoprotection; resulting pleomorphism should be represented separately if possible. (errington2017cellwalldeficientlform pages 1-2)
| Loss of PG wall | causes | pleomorphism and osmotic sensitivity | 10.1042/BST20160435 | “L-forms are pleomorphic and osmotically sensitive because of their cell wall defect.” | **Strong boundary edge.** Do not generalize to intact irregular-shaped bacteria. (errington2017cellwalldeficientlform pages 1-2)
| Increased membrane synthesis | promotes | L-form blebbing/tubulation and scission | 10.1042/BST20160435 | L-form proliferation requires increased membrane synthesis and surface-area-to-volume ratio and is independent of the FtsZ machinery. | **Boundary mechanism**, relevant to irregular outlines in wall-free cells. (errington2017cellwalldeficientlform pages 4-5, errington2017cellwalldeficientlform pages 1-2)
| Reduced membrane fluidity | impairs | L-form progeny scission | 10.1042/BST20160435 | A branched-chain-fatty-acid defect allowed shape changes but prevented resolution into separate progeny. | **Boundary, taxon-specific.** Useful only in a dedicated L-form branch. (errington2017cellwalldeficientlform pages 4-5)
| CJJ81176_1104/1105/1228 perturbation | alters | PG muropeptides and cell curvature | 10.3389/fmicb.2023.1162806 | Deletions produced varying curved-rod forms and changed PG profiles; overexpression of 1104/1105 also changed morphology and muropeptides. | **Boundary evidence.** Altered curvature is not necessarily irregularity; mechanisms differ even between related taxa. (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 5-6)
| Pgp1 or Pgp2 deletion | converts | helical cells to rods | 10.3389/fmicb.2023.1162806 | Deletion mutants were rod-shaped and had altered PG muropeptide profiles. | **Do not use as an irregular-shape edge.** It demonstrates PG remodeling control of a stable geometry. (frirdich2023multiplecampylobacterjejuni pages 1-2)
| FtsZ/divisome disruption | causes | filamentation or aberrant septation | 10.1016/j.tim.2017.09.012 | Divisome regulators and FtsZ assembly control transitions between elongation and septation. | **Conditional upstream edge.** Filamentation alone should map to a separate trait unless contour irregularity is demonstrated. (caccamo2018themolecularbasis pages 6-7, caccamo2018themolecularbasis pages 1-2)

A compact subset suitable for initial graph implementation is provided below.

| subject node | causal predicate | object node | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| spatially patterned peptidoglycan synthesis [GO candidate label]; peptidoglycan [CHEBI candidate label] | disruption/loss of patterning causes | irregular shaped (METPO:1000691) | broad bacterial morphogenesis; shape maintained by directed PG synthesis | Review-backed, broad; curate as high-level mechanism, not gene-specific (arejan2023polarproteinwag31 pages 1-2, caccamo2018themolecularbasis pages 1-2, kysela2016diversitytakesshape pages 4-5, woldemeskel2017shapeshiftingtosurvive pages 2-5) | 10.3389/fmicb.2022.1085918; 10.1016/j.tim.2017.09.012; 10.1371/journal.pbio.1002565; 10.1016/j.tim.2017.03.006 |
| MreB [gene/protein label; actin homolog] | perturbation/disrupted localization causes | loss of rod uniformity / irregular cell shape | rod-shaped bacteria; direct examples include Caulobacter irregular-shape mutant and A22-disrupted shape recovery in E. coli | Strong but partly taxon-specific; direct experimental + review synthesis (shi2018howtobuild pages 6-7, shi2018howtobuild pages 2-3, mao2023ontherole pages 1-2) | 10.1016/j.cell.2018.02.050; 10.7554/eLife.84505 |
| RodZ [gene/protein label] | loss impairs | MreB curvature sensing / cylindrical uniformity | E. coli rod morphogenesis | Strong mechanistic review synthesis; gene-specific but mainly from E. coli studies (shi2018howtobuild pages 6-7, shi2018howtobuild pages 2-3) | 10.1016/j.cell.2018.02.050 |
| Wag31 (DivIVA ortholog) [gene/protein label] | mutation causes | defective polar elongation and short/heterogeneous morphology | Mycobacterium smegmatis polar growth | Strong direct primary evidence; taxon-specific to mycobacteria (arejan2023polarproteinwag31 pages 1-2, arejan2023polarproteinwag31 pages 5-7) | 10.3389/fmicb.2022.1085918 |
| Wag31 D7A [mutant allele label] | causes | uncontrolled septation | Mycobacterium smegmatis | Strong direct primary evidence; allele-specific and taxon-specific (arejan2023polarproteinwag31 pages 5-7) | 10.3389/fmicb.2022.1085918 |
| peptidoglycan precursor synthesis inhibition; phosphomycin/fosfomycin [CHEBI candidate label] | induces | L-form pleomorphism (boundary phenotype near irregular shaped) | Bacillus subtilis and broad bacteria in osmoprotective conditions | Strong for wall-deficient pleomorphism; boundary evidence rather than core irregular-shape curation (errington2017cellwalldeficientlform pages 1-2) | 10.1042/BST20160435 |
| increased membrane synthesis | promotes | L-form blebbing / tubulation and scission | L-form bacteria, especially Bacillus subtilis model | Strong for L-form proliferation mechanism; boundary evidence relative to irregular-shaped wall-bearing cells (errington2017cellwalldeficientlform pages 1-2, errington2017cellwalldeficientlform pages 4-5) | 10.1042/BST20160435 |
| M23 peptidase / bactofilin dosage (e.g., CJJ81176_1104, CJJ81176_1105, CJJ81176_1228) | alters | degree of curvature / curved-rod morphology | Campylobacter jejuni PG morphogenesis | Direct primary evidence but boundary evidence for irregular-shaped because phenotype is altered curvature, not true irregularity (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 5-6) | 10.3389/fmicb.2023.1162806 |


*Table: This table summarizes the strongest graph-ready causal mechanisms relevant to METPO:1000691 irregular shaped, emphasizing direct evidence and clearly marking boundary cases such as L-form pleomorphism and altered curvature phenotypes.*

## 4. Recommended causal-graph architecture

A conservative main path is:

**genetic or chemical perturbation of MreB/RodZ/Rod complex**  
→ **impaired cytoskeletal assembly, curvature sensing, or circumferential motion**  
→ **loss of spatially uniform lateral PG insertion**  
→ **local imbalance of wall expansion**  
→ **width variation, bulging, bending, or branching across cells**  
→ **“irregular shaped” (METPO:1000691)**.

A taxon-specific Actinobacterial branch is:

**wag31/DivIVA perturbation**  
→ **unbalanced old/new-pole elongation and/or uncontrolled septation**  
→ **heterogeneous pole geometry and cell dimensions**  
→ **METPO:1000691**, but only where the source phenotype explicitly shows inconsistent form rather than uniformly short rods.

An L-form branch should remain separate:

**PG-precursor inhibition + osmoprotective environment**  
→ **loss of PG wall**  
→ **increased membrane-synthesis-driven blebbing/tubulation**  
→ **wall-deficient pleomorphism**  
→ optional broader relation to METPO:1000691.

## 5. Recent developments and quantitative evidence

The strongest directly relevant recent work retrieved was published in **2023**:

1. **Wag31 functional dissection.** Arejan and colleagues used alanine-scanning mutants and FDAA labeling to separate old-pole elongation, new-pole elongation, and septation functions. Microscopy used at least 100 cells from each of three independent replicate strains. K20A reduced elongation by 22%; L34A reduced new-pole elongation by about 76%, with absent new-pole elongation in roughly 65% of mutant versus 11% of wild-type cells. ACCase assays used three independent experiments. These data make Wag31 an unusually well-supported upstream regulator, although the final “irregular” phenotype must still be scored explicitly. Published **12 January 2023**. (arejan2023polarproteinwag31 pages 9-11, arejan2023polarproteinwag31 pages 1-2, arejan2023polarproteinwag31 pages 5-7)

2. **MreB assembly biochemistry.** Mao et al. showed that membrane lipids and nucleotide state jointly regulate Gram-positive MreB assembly. ATP or GTP supported membrane-associated protofilament pairs, whereas ADP, GDP, and nonhydrolysable ATP analogs did not. This adds molecular resolution to the established MreB → Rod-complex patterning model but does not itself demonstrate irregular cells. Published **11 October 2023**. (mao2023ontherole pages 1-2)

3. **Species-specific PG morphogenesis.** Frirdich et al. quantified approximately 300 cells per strain and showed that deleting or overexpressing candidate bactofilin/M23-peptidase genes altered both cell curvature and muropeptide profiles. Importantly, homologous perturbations differed between *C. jejuni* and *H. pylori*, warning against transferring morphology edges across taxa solely by homology. Published **18 April 2023**. (frirdich2023multiplecampylobacterjejuni pages 1-2, frirdich2023multiplecampylobacterjejuni pages 5-6)

4. **High-content phenotype mapping.** A 2023 preprint, later associated with a 2024 *Cell Systems* publication, quantified 77 morphology, growth, and cell-cycle phenotypes in an *E. coli* reference and more than 800 deletion derivatives across nutrient conditions. It found extensive nutrient-dependent phenotypic plasticity, illustrating why trait assertions should record medium and growth phase. The study examined 41 carbon-source conditions, cell volumes of approximately 1–5 µm³, and doubling times from roughly 20 minutes to 3 hours. (govers2023apparentsimplicityand pages 1-4)

No retrieved 2024 primary paper directly established a new universal causal route specifically to **irregular-shaped** morphology. The 2023 evidence therefore remains the most directly actionable recent evidence, while foundational MreB/PG work remains necessary.

## 6. Applications and expert analysis

- **Antimicrobial discovery:** Morphology is a sensitive phenotypic readout for inhibitors of PG precursor synthesis, PBPs, SEDS proteins, MreB, and divisome function. However, an irregular-shape readout is mechanistically nonspecific and should be paired with FDAA incorporation, muropeptide profiling, localization imaging, or rescue experiments.
- **Pathogenesis and transmission:** In *C. jejuni*, shape changes alter environmental transmission, colonization, and host interaction. Yet its stable helical-to-rod transitions should be annotated as specific shape changes rather than automatically as irregularity. (frirdich2023multiplecampylobacterjejuni pages 1-2)
- **Morphology engineering:** Reviews describe CRISPRi repression of MreB and tunable division regulators as ways to engineer microbial dimensions for bioproduction. Such implementations support manipulability of the pathway, but engineered elongation or rounding is not necessarily METPO:1000691. (caccamo2018themolecularbasis pages 11-12)
- **Single-cell phenotyping:** High-content microscopy can separate width variability, curvature variance, branching, and constriction defects from average length/width. For this trait, dispersion metrics are more appropriate than population means alone. (govers2023apparentsimplicityand pages 1-4)
- **L-form biotechnology and persistence research:** Wall-free cells have potential applications in strain engineering and origins-of-life models and have been proposed in chronic/recurrent infection contexts. Clinical relevance remains unsettled; it should not be encoded as a settled causal consequence of irregular morphology. (errington2017cellwalldeficientlform pages 1-2)

The authoritative consensus is that **PG is the load-bearing shape material, whereas cytoskeletal and landmark proteins pattern its synthesis**. Consequently, “irregular shaped” is better modeled as a convergent terminal phenotype reached through several taxon-specific failures of spatial control, rather than as the output of one conserved gene or metabolic pathway. (caccamo2018themolecularbasis pages 1-2, kysela2016diversitytakesshape pages 4-5, shi2018howtobuild pages 2-3)

## 7. Claims not yet suitable for TraitMech curation

1. **Do not curate “Wag31 → MurG localization → polar elongation” as established.** The 2023 study found no correlation between polar MurG/GlfT2 signal and elongation across tested mutants. (arejan2023polarproteinwag31 pages 9-11)
2. **Do not equate Wag31 phosphorylation with substantive PG control.** T73 phosphomutants had only subtle effects, and the authors concluded phosphorylation was not a critical regulator of PG metabolism under the tested conditions. (arejan2023polarproteinwag31 pages 1-2, arejan2023polarproteinwag31 pages 5-7)
3. **Do not infer irregular shape from every elongasome or divisome mutation.** Outcomes include uniform rounding, stable rods, filamentation, lysis, or growth arrest.
4. **Do not transfer *C. jejuni* curvature genes to other taxa by homology alone.** Related organisms showed different PG and morphology phenotypes. (frirdich2023multiplecampylobacterjejuni pages 1-2)
5. **Do not place L-form pleomorphism directly in the core wall-patterning path without osmoprotection and wall-deficiency qualifiers.** (errington2017cellwalldeficientlform pages 1-2)
6. **Do not curate ACCase reduction as causing irregular shape.** Wag31 mutants altered ACCase activity, but the causal route from lipid metabolism to morphology was not resolved. (arejan2023polarproteinwag31 pages 9-11)
7. **Do not treat asymmetric growth, variable length, or filamentation as sufficient evidence.** The defining observation must be inconsistency of geometric form across individual cells.
8. **Do not assign unverified CURIEs.** Gene names, locus tags, IMD, old/new pole, and specific mutant alleles can remain label-only until mapped against authoritative ontology and protein databases.

## 8. DOI-first bibliography

1. Arejan NH et al. **Polar protein Wag31 both activates and inhibits cell wall metabolism at the poles and septum.** *Frontiers in Microbiology* 13:1085918. Published 12 January 2023. DOI: [10.3389/fmicb.2022.1085918](https://doi.org/10.3389/fmicb.2022.1085918). (arejan2023polarproteinwag31 pages 1-2)
2. Mao W et al. **On the role of nucleotides and lipids in the polymerization of the actin homolog MreB from a Gram-positive bacterium.** *eLife* 12:e84505. Published 11 October 2023. DOI: [10.7554/eLife.84505](https://doi.org/10.7554/eLife.84505). (mao2023ontherole pages 1-2)
3. Frirdich E et al. **Multiple Campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature.** *Frontiers in Microbiology* 14:1162806. Published 18 April 2023. DOI: [10.3389/fmicb.2023.1162806](https://doi.org/10.3389/fmicb.2023.1162806). (frirdich2023multiplecampylobacterjejuni pages 1-2)
4. Govers SK et al. **Apparent simplicity and emergent robustness in bacterial cell cycle control.** Preprint posted 2023; later publication associated with *Cell Systems*. Preprint DOI: [10.1101/2023.01.16.524295](https://doi.org/10.1101/2023.01.16.524295). (govers2023apparentsimplicityand pages 1-4)
5. Shi H et al. **How to Build a Bacterial Cell: MreB as the Foreman of E. coli Construction.** *Cell* 172:1294–1305. Published March 2018. DOI: [10.1016/j.cell.2018.02.050](https://doi.org/10.1016/j.cell.2018.02.050). (shi2018howtobuild pages 6-7, shi2018howtobuild pages 2-3)
6. Caccamo PD, Brun YV. **The Molecular Basis of Noncanonical Bacterial Morphology.** *Trends in Microbiology* 26:191–208. Published March 2018. DOI: [10.1016/j.tim.2017.09.012](https://doi.org/10.1016/j.tim.2017.09.012). (caccamo2018themolecularbasis pages 6-7, caccamo2018themolecularbasis pages 1-2)
7. Woldemeskel SA, Goley ED. **Shapeshifting to Survive: Shape Determination and Regulation in Caulobacter crescentus.** *Trends in Microbiology* 25:673–687. Published August 2017. DOI: [10.1016/j.tim.2017.03.006](https://doi.org/10.1016/j.tim.2017.03.006). (woldemeskel2017shapeshiftingtosurvive pages 2-5)
8. Errington J. **Cell wall-deficient, L-form bacteria in the 21st century: a personal perspective.** *Biochemical Society Transactions* 45:287–295. Published 13 April 2017. DOI: [10.1042/BST20160435](https://doi.org/10.1042/BST20160435). (errington2017cellwalldeficientlform pages 4-5, errington2017cellwalldeficientlform pages 1-2)
9. Kysela DT et al. **Diversity Takes Shape: Understanding the Mechanistic and Adaptive Basis of Bacterial Morphology.** *PLOS Biology* 14:e1002565. Published October 2016. DOI: [10.1371/journal.pbio.1002565](https://doi.org/10.1371/journal.pbio.1002565). (kysela2016diversitytakesshape pages 4-5)
10. Joyce G et al. **Cell Division Site Placement and Asymmetric Growth in Mycobacteria.** *PLOS ONE* 7:e44582. Published 10 September 2012. DOI: [10.1371/journal.pone.0044582](https://doi.org/10.1371/journal.pone.0044582). (joyce2012celldivisionsite pages 1-2)

## Curation recommendation

Retain **loss of spatial PG patterning** as the central mechanism. The highest-value additions are separate branches for **MreB/RodZ-dependent lateral-wall patterning** and **Wag31/DivIVA-dependent polar growth/septation**, terminating in explicitly measured width/contour heterogeneity before reaching **METPO:1000691**. Keep L-form pleomorphism and programmed helical/curved morphologies as qualified boundary branches rather than core evidence.

References

1. (caccamo2018themolecularbasis pages 1-2): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.

2. (kysela2016diversitytakesshape pages 4-5): David T. Kysela, Amelia M. Randich, Paul D. Caccamo, and Yves V. Brun. Diversity takes shape: understanding the mechanistic and adaptive basis of bacterial morphology. PLOS Biology, 14:e1002565, Oct 2016. URL: https://doi.org/10.1371/journal.pbio.1002565, doi:10.1371/journal.pbio.1002565. This article has 150 citations and is from a highest quality peer-reviewed journal.

3. (shi2018howtobuild pages 2-3): Handuo Shi, Benjamin P. Bratton, Zemer Gitai, and Kerwyn Casey Huang. How to build a bacterial cell: mreb as the foreman of e. coli construction. Cell, 172:1294-1305, Mar 2018. URL: https://doi.org/10.1016/j.cell.2018.02.050, doi:10.1016/j.cell.2018.02.050. This article has 225 citations and is from a highest quality peer-reviewed journal.

4. (errington2017cellwalldeficientlform pages 4-5): Jeff Errington. Cell wall-deficient, l-form bacteria in the 21st century: a personal perspective. Biochemical Society Transactions, 45:287-295, Apr 2017. URL: https://doi.org/10.1042/bst20160435, doi:10.1042/bst20160435. This article has 78 citations and is from a peer-reviewed journal.

5. (errington2017cellwalldeficientlform pages 1-2): Jeff Errington. Cell wall-deficient, l-form bacteria in the 21st century: a personal perspective. Biochemical Society Transactions, 45:287-295, Apr 2017. URL: https://doi.org/10.1042/bst20160435, doi:10.1042/bst20160435. This article has 78 citations and is from a peer-reviewed journal.

6. (joyce2012celldivisionsite pages 1-2): Graham Joyce, Kerstin J. Williams, Matthew Robb, Elke Noens, Barbara Tizzano, Vahid Shahrezaei, and Brian D. Robertson. Cell division site placement and asymmetric growth in mycobacteria. PLoS ONE, 7:e44582, Sep 2012. URL: https://doi.org/10.1371/journal.pone.0044582, doi:10.1371/journal.pone.0044582. This article has 125 citations and is from a peer-reviewed journal.

7. (shi2018howtobuild pages 6-7): Handuo Shi, Benjamin P. Bratton, Zemer Gitai, and Kerwyn Casey Huang. How to build a bacterial cell: mreb as the foreman of e. coli construction. Cell, 172:1294-1305, Mar 2018. URL: https://doi.org/10.1016/j.cell.2018.02.050, doi:10.1016/j.cell.2018.02.050. This article has 225 citations and is from a highest quality peer-reviewed journal.

8. (mao2023ontherole pages 1-2): Wei Mao, Lars D Renner, Charlène Cornilleau, Ines Li de la Sierra-Gallay, Sana Afensiss, Sarah Benlamara, Yoan Ah-Seng, Herman Van Tilbeurgh, Sylvie Nessler, Aurélie Bertin, Arnaud Chastanet, and Rut Carballido-Lopez. On the role of nucleotides and lipids in the polymerization of the actin homolog mreb from a gram-positive bacterium. eLife, Oct 2023. URL: https://doi.org/10.7554/elife.84505, doi:10.7554/elife.84505. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (arejan2023polarproteinwag31 pages 1-2): Neda Habibi Arejan, Delfina Ensinck, Lautaro Diacovich, Parthvi Bharatkumar Patel, Samantha Y. Quintanilla, Arash Emami Saleh, Hugo Gramajo, and Cara C. Boutte. Polar protein wag31 both activates and inhibits cell wall metabolism at the poles and septum. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1085918, doi:10.3389/fmicb.2022.1085918. This article has 18 citations and is from a peer-reviewed journal.

10. (arejan2023polarproteinwag31 pages 5-7): Neda Habibi Arejan, Delfina Ensinck, Lautaro Diacovich, Parthvi Bharatkumar Patel, Samantha Y. Quintanilla, Arash Emami Saleh, Hugo Gramajo, and Cara C. Boutte. Polar protein wag31 both activates and inhibits cell wall metabolism at the poles and septum. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1085918, doi:10.3389/fmicb.2022.1085918. This article has 18 citations and is from a peer-reviewed journal.

11. (arejan2023polarproteinwag31 pages 9-11): Neda Habibi Arejan, Delfina Ensinck, Lautaro Diacovich, Parthvi Bharatkumar Patel, Samantha Y. Quintanilla, Arash Emami Saleh, Hugo Gramajo, and Cara C. Boutte. Polar protein wag31 both activates and inhibits cell wall metabolism at the poles and septum. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1085918, doi:10.3389/fmicb.2022.1085918. This article has 18 citations and is from a peer-reviewed journal.

12. (frirdich2023multiplecampylobacterjejuni pages 1-2): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 11 citations and is from a peer-reviewed journal.

13. (frirdich2023multiplecampylobacterjejuni pages 5-6): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 11 citations and is from a peer-reviewed journal.

14. (caccamo2018themolecularbasis pages 6-7): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.

15. (woldemeskel2017shapeshiftingtosurvive pages 2-5): Selamawit Abi Woldemeskel and Erin D. Goley. Shapeshifting to survive: shape determination and regulation in caulobacter crescentus. Trends in microbiology, 25 8:673-687, Aug 2017. URL: https://doi.org/10.1016/j.tim.2017.03.006, doi:10.1016/j.tim.2017.03.006. This article has 59 citations and is from a domain leading peer-reviewed journal.

16. (govers2023apparentsimplicityand pages 1-4): Sander K. Govers, Manuel Campos, Bhavyaa Tyagi, Géraldine Laloux, and Christine Jacobs-Wagner. Apparent simplicity and emergent robustness in bacterial cell cycle control. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.16.524295, doi:10.1101/2023.01.16.524295. This article has 9 citations.

17. (caccamo2018themolecularbasis pages 11-12): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.