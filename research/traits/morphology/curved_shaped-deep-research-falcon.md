---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:22:07.717438'
end_time: '2026-06-18T07:38:47.607762'
duration_seconds: 999.89
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: curved shaped
  trait_identifier: METPO:1000670
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: curved_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a bent or curved cell body rather
    than a straight rod or sphere.
  parent_traits: METPO:1000666
  synonyms: S_curved_spiral, curved-shaped
  evidence_summary: 'DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized
    for motility (Supports curved cells as a recognized bacterial morphology with
    possible functional associations.)'
  causal_graph_summary: 'curved_shaped_scaffolded_curvature: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** curved shaped
- **METPO identifier:** METPO:1000670
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bent or curved cell body rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, curved-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized for motility (Supports curved cells as a recognized bacterial morphology with possible functional associations.)
- **Existing causal graph summary:** curved_shaped_scaffolded_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **curved shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/curved_shaped.yaml`.

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
- **Trait label:** curved shaped
- **METPO identifier:** METPO:1000670
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a bent or curved cell body rather than a straight rod or sphere.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_curved_spiral, curved-shaped
- **Existing evidence:** DOI:10.1371/journal.pbio.1002565: curved cells appear to be optimized for motility (Supports curved cells as a recognized bacterial morphology with possible functional associations.)
- **Existing causal graph summary:** curved_shaped_scaffolded_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **curved shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/curved_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Curved shaped** (METPO:1000670)

**Trait label:** curved shaped  
**METPO identifier:** METPO:1000670  
**Trait category:** MORPHOLOGY (CLASS)  
**Definition (given):** “A cell shape in which an organism has a bent or curved cell body rather than a straight rod or sphere.”  

### Executive scope summary (TraitMech-ready)
“Curved shaped” in this curation is best operationalized as a **stable, genetically programmed, crescent/vibrioid bending of an otherwise rod-like cell body**, produced by **asymmetric patterning of cell-envelope mechanics and peptidoglycan (PG) synthesis/remodeling**, rather than transient mechanical deformation. Recent and authoritative sources emphasize that curved and related shapes are widespread and linked to **motility, virulence, and fitness** (pohl2024anoutermembrane pages 1-2). Mechanistically, multiple symmetry-breaking solutions exist: (i) cytoskeletal/periskeletal scaffolds localized to the **inner curve** (e.g., crescentin/CreS in *Caulobacter*) (liu2024filamentstructureand pages 1-2, pohl2024anoutermembrane pages 1-2), (ii) **asymmetric enzymatic PG editing** (e.g., Bd1075 LD-carboxypeptidase in *Bdellovibrio*) (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11), and (iii) a newly described **outer-membrane patterning module** (Por39/Por41/PapS) that **entraps elongasomes** to bias growth to the outer curve (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13).

Boundary cases:
* **Helical/spiral** morphologies are adjacent but distinct; they frequently involve ensembles of PG hydrolases in *Campylobacter/Helicobacter* (banks2022asymmetricpeptidoglycanediting pages 1-2) and should generally be curated under a separate “helical/spiral” trait rather than METPO:1000670 unless METPO’s parent class explicitly includes them.
* **Transient curvature induced by confinement/stress** should not be curated as “curved shaped” without evidence of stable morphogenetic determinants; a general caution that adaptive explanations can become “just-so stories” is emphasized by Kysela et al. (kysela2016diversitytakesshape pages 4-5).

---

## 1. Key concepts and definitions (current understanding)

### 1.1 Shape as an envelope-encoded, actively maintained trait
Bacterial morphology is typically determined by the **peptidoglycan cell wall (sacculus)** and requires regulated synthesis and remodeling (pohl2024anoutermembrane pages 1-2, liu2024filamentstructureand pages 1-2). As synthesized PG has no intrinsic “blueprint,” **non-spherical shapes require spatially and temporally non-uniform insertion/remodeling** (expert synthesis) (teeseling2017determinantsofbacterial pages 3-4).

### 1.2 Adaptive significance (expert synthesis)
Kysela et al. (PLOS Biology) summarize a widely cited hypothesis that “helical and curved cells appear to be optimized for motility, especially in viscous solutions” (kysela2016diversitytakesshape pages 4-5). The 2024 *Rhodospirillum rubrum* work frames curved shapes as “important for cellular motility, virulence and fitness” (pohl2024anoutermembrane pages 1-2). These are strong *expert framing* statements but are not universally species-proven; they should be curated with “broad/expert-synthesis” uncertainty where used as causal edges.

---

## 2. Recent developments and latest research (prioritize 2023–2024)

### 2.1 2024: Outer-membrane porin–lipoprotein module that cages the elongasome (new mechanism class)
Pöhl et al. (Nature Communications; received 2024-02-22, accepted 2024-08-14; published 2024; DOI:10.1038/s41467-024-51790-z; URL: https://doi.org/10.1038/s41467-024-51790-z) identify **Por39/Por41 porins** forming a helical ribbon at the **outer curve** that recruits **PapS**, and show that disrupting PapS or the porin–PapS interface straightens cells (pohl2024anoutermembrane pages 1-2). They propose a “roadblock”/caging model in which **porin–PapS assemblies entrap the elongasome** and bias PG insertion toward the outer curve, inducing bending (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13). Quantitatively, single-molecule tracking reports two mobility populations for mNG-RodZ, with mean apparent diffusion coefficients reported (e.g., 0.0884 µm² s⁻¹ and 0.0174 µm² s⁻¹ in the center plane) (pohl2024anoutermembrane pages 12-13).

**Visual evidence**: Figure crops supporting the roadblock model and diffusion data are available (pohl2024anoutermembrane media 1cc947a9, pohl2024anoutermembrane media 12d35527).

### 2.2 2024: Structural resolution of crescentin filaments (mechanistic refinement of scaffold model)
Liu et al. (PNAS; published 2024-02-07; DOI:10.1073/pnas.2309984121; URL: https://doi.org/10.1073/pnas.2309984121) provide cryo-EM/cryo-ET structural evidence that **crescentin forms a filamentous band on the inner, concave side of curved cells** and is “required for the crescent shape” of *Caulobacter crescentus* (liu2024filamentstructureand pages 1-2). They also report perturbation sensitivity: crescentin’s membrane proximity is lost with the MreB inhibitor A22 and cell-wall inhibitors mecillinam and phosphomycin (liu2024filamentstructureand pages 1-2), supporting a mechanistic link between cytoskeletal scaffolds and PG synthesis/remodeling.

### 2.3 2023 context: Cell-envelope mechanosensing and curvature determinants in *Vibrio cholerae*
A 2023 Scientific Reports study on mechanical stimuli and VxrAB signaling in *V. cholerae* references that “removal of crvA results in rod-shaped cells” (pohl2024anoutermembrane pages 1-2). While not a primary shape paper in this evidence set, it supports CrvA as a determinant node for vibrioid curvature (taxon-specific; evidence indirect in provided excerpt).

---

## 3. Current applications and real-world implementations

### 3.1 Predatory bacteria as antibacterial agents: curvature as a fitness-linked trait
Banks et al. (Nature Communications; 2022; DOI:10.1038/s41467-022-29007-y; URL: https://doi.org/10.1038/s41467-022-29007-y) note *Bdellovibrio bacteriovorus* as a predator with therapeutic potential, stating it can clear pathogen infections in animal models (background) (banks2022asymmetricpeptidoglycanediting pages 1-2). In this context, curvature is directly tied to function: “Rod-shaped Δbd1075 mutants invade prey more slowly than curved wild-type predators” and the authors “propose that the vibrioid shape… contributes to predatory fitness” (banks2022asymmetricpeptidoglycanediting pages 1-2). This supports a TraitMech-style link between a morphology determinant (Bd1075) and an applied functional outcome (predation efficiency), though the “fitness” conclusion should be flagged as proposed.

### 3.2 Imaging and single-molecule tracking as implementation tools for curvature mechanisms
The *R. rubrum* system uses fluorescent tagging and single-molecule tracking (mNG-RodZ) to quantify how curvature modules alter elongasome dynamics (pohl2024anoutermembrane pages 12-13). This is a reusable experimental implementation for discovering curvature modules in other taxa.

---

## 4. Expert opinions and authoritative synthesis

* Kysela et al. emphasize both adaptive hypotheses (motility in viscous solutions) and a caution that validating morphology’s function requires “clear, falsifiable hypothesis” testing, warning against untested narrative explanations (kysela2016diversitytakesshape pages 4-5).
* van Teeseling et al. synthesize that morphology is dictated by the PG sacculus and shaped by **cytoskeletal guidance vs post-synthesis PG modification** as broad mechanistic categories (teeseling2017determinantsofbacterial pages 1-3).
* Pöhl et al. (2024) summarize current consensus that curved shapes promote “surface colonization, motility in viscous environments, and virulence,” while noting mechanisms remain incompletely understood (pohl2024anoutermembrane pages 1-2).

---

## 5. Relevant statistics and data (recent studies)

### 5.1 Bd1075 deletion strongly reduces curvature (quantitative)
In *B. bacteriovorus*, wild-type median curvature was **0.64 A.U.** (95% CI [0.63, 0.66]) versus **0.11 A.U.** (95% CI [0.10, 0.12]) for Δbd1075 (p < 0.0001) (banks2022asymmetricpeptidoglycanediting pages 1-2). Loss of bd1075 also slightly increased PG peptide crosslinkage (**64.4% vs 61.1%** in wild-type) (banks2022asymmetricpeptidoglycanediting pages 10-11).

### 5.2 PapS reduces elongasome/RodZ mobility (quantitative)
In *R. rubrum*, single-molecule MSD analysis reports two populations with mean apparent diffusion coefficients (example values in center plane): **0.0884 µm² s⁻¹ (diffusive)** and **0.0174 µm² s⁻¹ (immobile)** (pohl2024anoutermembrane pages 12-13). This supports a quantitative “caging/roadblock” mechanism.

---

## Candidate causal-graph nodes (grouped by type)
The following node inventory is curated for direct use in `data/traits/morphology/curved_shaped.yaml` candidate node lists.

| Node label | Type | Suggested grounding | Taxon examples (NCBITaxon labels only) | Evidence note with a short cited phrase |
|---|---|---|---|---|
| curved shaped | Phenotype/trait | METPO:1000670 | Caulobacter crescentus; Vibrio cholerae; Bdellovibrio bacteriovorus; Rhodospirillum rubrum | “curved cell shapes are widespread among bacteria” (pohl2024anoutermembrane pages 1-2) |
| vibrioid cell shape | Phenotype/trait | label-only | Caulobacter crescentus; Bdellovibrio bacteriovorus | “vibrioid cell shape of Caulobacter and Vibrio” (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| crescent cell shape | Phenotype/trait | label-only | Caulobacter crescentus | “required for the crescent shape” (liu2024filamentstructureand pages 1-2) |
| straight rod-shaped morphology | Phenotype/trait | label-only | Bdellovibrio bacteriovorus; Rhodospirillum rubrum | “distinct straight rod-shaped morphology” / “resulting in cell straightening” (banks2022asymmetricpeptidoglycanediting pages 1-2, pohl2024anoutermembrane pages 1-2) |
| peptidoglycan sacculus | Cellular structure/process | GO:0009274 | Caulobacter crescentus; Rhodospirillum rubrum; Bdellovibrio bacteriovorus | “distorting the sacculus into curved structures” (pohl2024anoutermembrane pages 1-2) |
| peptidoglycan remodeling | Cellular structure/process | GO:0009253 | Caulobacter crescentus; Bdellovibrio bacteriovorus; Rhodospirillum rubrum | “regulate cell wall synthesis and remodeling” (liu2024filamentstructureand pages 1-2) |
| peptidoglycan synthesis | Cellular structure/process | GO:0009252 | Rhodospirillum rubrum; Caulobacter crescentus | “Peptidoglycan synthesis is achieved by a diverse set” (pohl2024anoutermembrane pages 1-2) |
| lateral cell elongation | Cellular structure/process | label-only | Rhodospirillum rubrum | “elongate by lateral growth” (pohl2024anoutermembrane pages 1-2) |
| elongasome movement/localization | Cellular structure/process | label-only | Rhodospirillum rubrum | “modulates elongasome movement” / “spatial bias in the formation and localization of elongasome complexes” (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13) |
| divisome-mediated constriction | Cellular structure/process | label-only | Rhodospirillum rubrum | “divisome… mediates cell constriction” (pohl2024anoutermembrane pages 1-2) |
| LD-carboxypeptidase activity | Cellular structure/process | GO:0047064 | Bdellovibrio bacteriovorus | “exerting LD-carboxypeptidase activity upon the predator cell wall” (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| periplasmic localization | Cellular structure/process | GO:0042597 | Rhodospirillum rubrum; Bdellovibrio bacteriovorus | “targeting to the periplasmic space” (pohl2024anoutermembrane pages 1-2) |
| Sec-dependent translocation signal | Cellular structure/process | label-only | Bdellovibrio bacteriovorus; Rhodospirillum rubrum | “predicted N-terminal sec signal peptide” (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| outer-curve localization | Cellular structure/process | label-only | Bdellovibrio bacteriovorus; Rhodospirillum rubrum | “localized to the convex cell face” / “strongly enriched at the outer curve” (banks2022asymmetricpeptidoglycanediting pages 10-11, pohl2024anoutermembrane pages 12-13) |
| mechanical force on cell envelope | Cellular structure/process | label-only | Caulobacter crescentus; Vibrio cholerae | “thought to act by exerting a mechanical force on the cell envelope” (pohl2024anoutermembrane pages 1-2) |
| crescentin | Protein/gene | label-only | Caulobacter crescentus | “The protein crescentin is required for the crescent shape” (liu2024filamentstructureand pages 1-2) |
| CreS | Protein/gene | label-only | Caulobacter crescentus | “Whatever the biological reason… dependent on the function of the protein crescentin (CreS)” (liu2024filamentstructureand pages 1-2) |
| Bd1075 | Protein/gene | label-only | Bdellovibrio bacteriovorus | “Bd1075, generates cell curvature” (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| PapS | Protein/gene | label-only | Rhodospirillum rubrum | “PapS is required for cell curvature” (pohl2024anoutermembrane pages 1-2) |
| Por39 | Protein/gene | label-only | Rhodospirillum rubrum | “porins Por39 and Por41 form a helical ribbon-like structure” (pohl2024anoutermembrane pages 1-2) |
| Por41 | Protein/gene | label-only | Rhodospirillum rubrum | “porins Por39 and Por41 form a helical ribbon-like structure” (pohl2024anoutermembrane pages 1-2) |
| RodZ | Protein/gene | label-only | Rhodospirillum rubrum | “mNG-RodZ was strongly enriched at the outer curve” (pohl2024anoutermembrane pages 12-13) |
| MreB | Protein/gene | label-only | Rhodospirillum rubrum; Caulobacter crescentus | “elongasome is organized by the actin homolog MreB” (pohl2024anoutermembrane pages 1-2) |
| FtsZ | Protein/gene | label-only | Rhodospirillum rubrum | “dependent on the tubulin homolog FtsZ” (pohl2024anoutermembrane pages 1-2) |
| CrvA | Protein/gene | label-only | Vibrio cholerae | “removal of crvA results in rod-shaped cells” (pohl2024anoutermembrane pages 1-2) |
| CrvAB | Complex/module | label-only | Vibrio cholerae | “the periplasmic CrvAB complex of Vibrio cholerae” (pohl2024anoutermembrane pages 1-2) |
| crescentin filament | Complex/module | label-only | Caulobacter crescentus | “forms a filamentous structure on the inner, concave side” (liu2024filamentstructureand pages 1-2) |
| porin–PapS complex | Complex/module | label-only | Rhodospirillum rubrum | “porin-PapS assemblies act as molecular cages” (pohl2024anoutermembrane pages 1-2) |
| Por39/Por41 helical ribbon | Complex/module | label-only | Rhodospirillum rubrum | “form a helical ribbon-like structure at the outer curve” (pohl2024anoutermembrane pages 1-2) |
| elongasome | Complex/module | label-only | Rhodospirillum rubrum | “Two widely conserved complexes… the elongasome” (pohl2024anoutermembrane pages 1-2) |
| divisome | Complex/module | label-only | Rhodospirillum rubrum | “the elongasome and the divisome” (pohl2024anoutermembrane pages 1-2) |
| NTF2-like domain | Complex/module | label-only | Bdellovibrio bacteriovorus | “requires a nuclear transport factor 2-like (NTF2) domain” (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| OmpA-like peptidoglycan-binding domain | Complex/module | label-only | Rhodospirillum rubrum | “a C-terminal OmpA-like peptidoglycan-binding domain” (pohl2024anoutermembrane pages 1-2) |
| A22 | Chemical/inhibitor | CHEBI:3392 | Caulobacter crescentus | “MreB inhibitor A22” (liu2024filamentstructureand pages 1-2) |
| mecillinam | Chemical/inhibitor | CHEBI:6995 | Caulobacter crescentus | “cell wall inhibitors mecillinam and phosphomycin” (liu2024filamentstructureand pages 1-2) |
| phosphomycin/fosfomycin | Chemical/inhibitor | CHEBI:28915 | Caulobacter crescentus | “cell wall inhibitors mecillinam and phosphomycin” (liu2024filamentstructureand pages 1-2) |
| meso-diaminopimelic acid (mDAP) | Chemical/inhibitor | CHEBI:18022 | Rhodospirillum rubrum | “MST assays to test binding to meso-diaminopimelic acid (mDAP)” (pohl2024anoutermembrane pages 18-19) |
| turgor pressure | Environmental/experimental factor | label-only | Bdellovibrio bacteriovorus | “becomes deformed by internal cellular turgor” (banks2022asymmetricpeptidoglycanediting pages 10-11) |
| osmotic pressure fluctuations | Environmental/experimental factor | label-only | Bdellovibrio bacteriovorus | “protection against lysis due to osmotic pressure fluctuations” (banks2022asymmetricpeptidoglycanediting pages 1-2) |
| viscous environments | Environmental/experimental factor | ENVO:01001208 | Vibrio cholerae; Helicobacter pylori; Campylobacter jejuni | “motility in viscous environments” (pohl2024anoutermembrane pages 1-2) |
| flow / surface colonization in flow | Environmental/experimental factor | label-only | Caulobacter crescentus | “promoting surface colonization” / “enhances surface colonization in flow” (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 18-19) |
| spherical prey bdelloplast environment | Environmental/experimental factor | label-only | Bdellovibrio bacteriovorus | “as it grows inside spherical prey” / “forming a spherical structure called a prey bdelloplast” (banks2022asymmetricpeptidoglycanediting pages 1-2) |


*Table: This table lists candidate causal-graph nodes for the microbial trait 'curved shaped' (METPO:1000670), organized by entity type and anchored to evidence from the provided sources. It is useful as a curation-ready inventory of plausible TraitMech nodes before edge selection.*

---

## Candidate evidence-backed causal edges (triples)
The following table compiles proposed edges with supporting snippets, DOI-first references, and curation notes/uncertainty.

| Edge (subject–predicate–object) | Edge type | Suggested grounding | Strength/uncertainty | Taxon context | Reference (DOI, year, URL) | Supporting snippet | Curation notes |
|---|---|---|---|---|---|---|---|
| crescentin/CreS → required for → crescent/curved cell shape | gene→phenotype | CreS/crescentin: label-only; phenotype: METPO:1000670 | Strong, taxon-specific | *Caulobacter crescentus* | 10.1073/pnas.2309984121, 2024, https://doi.org/10.1073/pnas.2309984121 | “The protein crescentin is required for the crescent shape of the freshwater bacterium Caulobacter crescentus” (liu2024filamentstructureand pages 1-2) | Direct requirement statement. Suitable as a curated taxon-specific edge linking a named determinant to curved morphology. |
| crescentin filament → localizes to → inner concave side of curved cells | complex→process | crescentin filament: label-only; cellular localization: GO:0044228? / label-only | Strong, taxon-specific | *Caulobacter crescentus* | 10.1073/pnas.2309984121, 2024, https://doi.org/10.1073/pnas.2309984121 | “Crescentin forms a filamentous structure on the inner, concave side of the curved cells.” (liu2024filamentstructureand pages 1-2) | Good mechanistic localization edge. Supports scaffold asymmetry rather than phenotype directly. Ground localization conservatively as label-only if exact GO term is unclear. |
| A22 (MreB inhibitor) → disrupts → crescentin membrane proximity/localization | inhibitor→localization/process | A22: CHEBI:3392; MreB: label-only; crescentin localization: label-only | Strong for perturbation, mechanistic interpretation uncertain | *Caulobacter crescentus* | 10.1073/pnas.2309984121, 2024, https://doi.org/10.1073/pnas.2309984121 | “The proximity of the crescentin structure to the cell membrane was lost during treatment with the MreB inhibitor A22” (liu2024filamentstructureand pages 1-2) | Strong perturbational evidence that MreB-dependent organization affects crescentin placement; edge should be annotated as inhibitor-specific. |
| mecillinam → disrupts → crescentin membrane proximity/localization | inhibitor→localization/process | mecillinam: CHEBI:6995; crescentin localization: label-only | Strong for perturbation, assay-specific | *Caulobacter crescentus* | 10.1073/pnas.2309984121, 2024, https://doi.org/10.1073/pnas.2309984121 | “The proximity of the crescentin structure to the cell membrane was lost during treatment with… the cell wall inhibitors mecillinam and phosphomycin” (liu2024filamentstructureand pages 1-2) | Indicates cell-wall synthesis contributes to correct crescentin positioning; use as perturbation edge, not direct biosynthetic edge. |
| phosphomycin/fosfomycin → disrupts → crescentin membrane proximity/localization | inhibitor→localization/process | fosfomycin: CHEBI:28915; crescentin localization: label-only | Strong for perturbation, assay-specific | *Caulobacter crescentus* | 10.1073/pnas.2309984121, 2024, https://doi.org/10.1073/pnas.2309984121 | “The proximity of the crescentin structure to the cell membrane was lost during treatment with… the cell wall inhibitors mecillinam and phosphomycin” (liu2024filamentstructureand pages 1-2) | Same rationale as mecillinam; useful for connecting PG synthesis perturbation to scaffold localization. |
| heterologous crescentin expression → induces → curved cells | gene→phenotype | crescentin: label-only; phenotype: METPO:1000670 | Moderate, heterologous-system | *Escherichia coli* expressing *Caulobacter* crescentin | 10.1073/pnas.2309984121, 2024, https://doi.org/10.1073/pnas.2309984121 | “the heterologous expression of crescentin in Escherichia coli leads to curved cells” (liu2024filamentstructureand pages 1-2) | Valuable sufficiency-style evidence, but should be flagged as heterologous and not native-trait regulation. |
| Bd1075 → generates → curved/vibrioid cell shape | gene→phenotype | Bd1075: label-only; phenotype: METPO:1000670 | Strong, taxon-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “The protein, Bd1075, generates cell curvature in B. bacteriovorus” (banks2022asymmetricpeptidoglycanediting pages 1-2) | One of the clearest direct causal statements in the corpus; appropriate as a core edge. |
| deletion of bd1075 → causes loss of curvature / straight rod morphology | gene→phenotype | bd1075: label-only; straight rod morphology: label-only | Strong, quantitative, taxon-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “Δbd1075 mutant cells had a distinct straight rod-shaped morphology… Wild-type median curvature (0.64 A.U., 95% CI [0.63, 0.66]) was significantly higher… than the Δbd1075 mutant (0.11 A.U., 95% CI [0.10, 0.12])” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Strongest quantitative phenotype edge. Add notes in curation that this is loss-of-function evidence with effect size and CI. |
| Bd1075 LD-carboxypeptidase activity → acts on → predator cell wall peptidoglycan | process→process | LD-carboxypeptidase activity: GO:0047064; peptidoglycan remodeling: GO:0009253 | Strong, taxon-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “Bd1075, generates cell curvature… by exerting LD-carboxypeptidase activity upon the predator cell wall” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Mechanistic enzymatic edge connecting enzyme function to substrate/process. Good upstream causal link for morphology. |
| Bd1075 NTF2-like domain → required for → asymmetric outer-convex localization of Bd1075 | complex→process | NTF2-like domain: label-only; localization: label-only | Strong, taxon-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “this asymmetric localization requires a nuclear transport factor 2-like (NTF2) domain” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Clear domain-to-localization causality. Useful intermediate edge in graph. |
| asymmetric outer-convex localization of Bd1075 → required for → cell curvature | process→phenotype | localization: label-only; phenotype: METPO:1000670 | Strong, taxon-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “this specific localization is required to generate cell curvature” (banks2022asymmetricpeptidoglycanediting pages 10-11) | Excellent process-to-phenotype edge because localization mutants lost complementation. |
| Bd1075 C156 catalytic residue / LD-CPase activity → required for → curvature complementation | gene→phenotype | catalytic activity: GO:0047064; C156A mutant: label-only | Strong, mutation-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “The LD-CPase catalytic domain point mutant C156A did not restore curvature” (banks2022asymmetricpeptidoglycanediting pages 10-11) | Strong evidence that catalysis, not merely localization, is necessary. Curate as mutation-specific mechanistic requirement. |
| loss of bd1075 → increases → peptidoglycan crosslinkage | gene→process | peptidoglycan crosslinkage: label-only | Strong, quantitative, taxon-specific | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “The overall peptide crosslinkage was slightly higher in cells lacking bd1075 (64.4% compared to 61.1% in wild-type” (banks2022asymmetricpeptidoglycanediting pages 10-11) | Quantitative biochemical phenotype supporting a PG-remodeling mechanism upstream of curvature. |
| vibrioid shape → contributes to → rapid prey invasion / predatory fitness | environment→fitness | vibrioid shape: label-only; predatory fitness: label-only | Moderate, taxon-specific fitness inference | *Bdellovibrio bacteriovorus* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “Rod-shaped Δbd1075 mutants invade prey more slowly than curved wild-type predators… We therefore propose that the vibrioid shape… contributes to predatory fitness.” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Good shape-to-fitness edge, but note wording “propose”; retain uncertainty flag for fitness interpretation. |
| Por39/Por41 porins → recruit → PapS | complex→process | Por39: label-only; Por41: label-only; PapS: label-only | Strong, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “Por39 and Por41 form a helical ribbon-like structure at the outer curve of the cell that recruits the peptidoglycan-binding lipoprotein PapS” (pohl2024anoutermembrane pages 1-2) | Direct module-assembly edge from primary paper; suitable in graph as complex formation/localization step. |
| PapS inactivation or disruption of porin–PapS interface → results in → cell straightening | complex→phenotype | PapS: label-only; porin-PapS complex: label-only; phenotype: METPO:1000670 | Strong, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “PapS inactivation, porin delocalization or disruption of the porin-PapS interface resulting in cell straightening” (pohl2024anoutermembrane pages 1-2) | Strong loss-of-function/module disruption evidence for curvature maintenance. |
| porin–PapS assemblies → entrap → elongasome complexes | complex→process | porin–PapS assemblies: label-only; elongasome: label-only | Strong, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “porin-PapS assemblies act as molecular cages that entrap the cell elongation machinery” (pohl2024anoutermembrane pages 1-2) | Central mechanistic edge of the 2024 study; directly links OM patterning to growth machinery behavior. |
| elongasome entrapment by PapS → biases → growth toward outer curve | process→process | elongasome localization: label-only; biased PG growth: label-only | Strong, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “thus biasing cell growth towards the outer curve” (pohl2024anoutermembrane pages 1-2) | Good intermediate process edge leading to morphology. |
| biased outer-curve growth → generates → curved cell shape | process→phenotype | biased PG growth: label-only; phenotype: METPO:1000670 | Strong, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “promote elevated longitudinal growth of the peptidoglycan sacculus… thereby inducing cell bending” (pohl2024anoutermembrane pages 12-13) | Direct process-to-shape edge, close to TraitMech phenotype. |
| PapS → promotes → stable outer-curve RodZ/elongasome localization | gene→process | PapS: label-only; RodZ: label-only | Strong, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “mNG-RodZ was strongly enriched at the outer curve… In the ΔpapS background, this pattern was completely abolished” (pohl2024anoutermembrane pages 12-13) | Strong localization dependency edge; good quantitative support from imaging. |
| PapS → reduces → RodZ/elongasome mobility at outer curve | gene→process | PapS: label-only; RodZ mobility: label-only | Strong, quantitative, taxon-specific | *Rhodospirillum rubrum* | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “the overall mobility of mNG-RodZ molecules at the outer curve was significantly lower than that at the inner curve” and “mean apparent diffusion coefficients of 0.0884 µm2 s-1 and 0.0174 µm2 s-1” (pohl2024anoutermembrane pages 12-13) | Quantitative single-molecule evidence for the roadblock mechanism. Good as process refinement rather than direct phenotype edge. |
| curved/helical morphology → optimized for → motility in viscous solutions | environment→fitness | curved morphology: METPO:1000670; viscous environment: ENVO:01001208 | Moderate, broad expert synthesis | Broad bacterial scope | 10.1371/journal.pbio.1002565, 2016, https://doi.org/10.1371/journal.pbio.1002565 | “helical and curved cells appear to be optimized for motility, especially in viscous solutions” (kysela2016diversitytakesshape pages 4-5) | Useful expert-opinion/adaptive edge, but should be flagged as broad and not a direct mechanistic causal edge for all taxa. |
| bacterial cell shape determinants → act through → spatially constrained peptidoglycan remodeling (“zonal” growth) | process→phenotype | peptidoglycan remodeling: GO:0009253 | Moderate, broad expert synthesis | Broad bacterial scope | 10.1371/journal.pbio.1002565, 2016, https://doi.org/10.1371/journal.pbio.1002565 | “Because PG synthesis is constrained in space, all cell wall growth and remodeling can be described as ‘zonal’ growth” (kysela2016diversitytakesshape pages 4-5) | Helpful conceptual edge for graph scaffolding; not specific to curved cells, so best used as high-level background node/edge. |
| curved/helical morphology → promotes → surface colonization, motility in viscous environments, virulence | environment→fitness | phenotype: METPO:1000670; viscous environment: ENVO:01001208 | Moderate, broad expert synthesis | Broad bacterial scope | 10.1038/s41467-024-51790-z, 2024, https://doi.org/10.1038/s41467-024-51790-z | “curved and helical cell shapes… are widespread among bacteria, promoting surface colonization, motility in viscous environments, and virulence” (pohl2024anoutermembrane pages 1-2) | Good current expert framing from primary introduction; still broad and not sufficient alone for species-specific causal curation. |
| cytoskeletal/periskeletal proteins → determine → curved vibrioid cell shape | gene→phenotype | cytoskeletal/periskeletal proteins: label-only; phenotype: METPO:1000670 | Moderate, broad/taxon-class | *Caulobacter*, *Vibrio* and related vibrioid bacteria | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “cytoskeletal or periskeletal proteins determine the curved, vibrioid cell shape of Caulobacter and Vibrio” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Useful for scope and mechanistic categorization, but too generic for direct TraitMech curation unless instantiated with specific proteins like CreS or CrvAB. |
| peptidoglycan hydrolases → contribute to → helical cell shape | process→phenotype | peptidoglycan hydrolases: label-only | Uncertain for this trait boundary; neighboring morphology | *Campylobacter*, *Helicobacter* | 10.1038/s41467-022-29007-y, 2022, https://doi.org/10.1038/s41467-022-29007-y | “Peptidoglycan hydrolases contribute to the generation of helical cell shape in Campylobacter and Helicobacter bacteria” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Important boundary-case edge: supports distinction from curved/vibrioid trait and should generally not be curated directly into METPO:1000670 unless trait scope expands. |
| MreB/cytoskeletal guidance → directs → localized cell-wall synthesis at specific curvature regions | process→process | MreB: label-only; PG synthesis: GO:0009252 | Moderate, broad expert synthesis | Broad bacterial scope | 10.3389/fmicb.2017.01264, 2017, https://doi.org/10.3389/fmicb.2017.01264 | “the actin-like protein MreB localizes to specific curvature regions… and directs localized cell-wall synthesis” (teeseling2017determinantsofbacterial pages 3-4) | Useful upstream mechanistic edge; not specific to curved-shaped taxa but supports scaffold-guided PG remodeling as a causal class. |


*Table: This table compiles candidate evidence-backed causal edges for the microbial trait 'curved shaped' (METPO:1000670), spanning specific determinants, mechanisms, perturbations, and adaptive consequences. It is designed to support TraitMech curation by pairing each proposed edge with a direct source snippet, grounding notes, and uncertainty flags.*

---

## Visual evidence (figures/tables)
Pöhl et al. Figure crops (PapS reduces RodZ/elongasome motion; roadblock model) support the mechanistic claim that porin–PapS assemblies bias elongasome dynamics to generate curvature (pohl2024anoutermembrane media 1cc947a9, pohl2024anoutermembrane media 12d35527).

---

## Warnings / claims not ready for TraitMech curation

1. **Helical/spiral mechanisms**: Statements that PG hydrolases generate **helical** shapes (e.g., *Campylobacter/Helicobacter*) are valuable for boundary definition but should not be directly curated as edges for METPO:1000670 unless the trait scope explicitly includes helical morphologies (banks2022asymmetricpeptidoglycanediting pages 1-2).
2. **Broad adaptive claims** (motility/virulence/fitness): These are frequently framed as general truths (e.g., “optimized for motility” or “promoting virulence”) but should be curated as **broad/expert-synthesis** or **taxon-specific** edges unless species-specific experimental evidence is present in the same source excerpt (kysela2016diversitytakesshape pages 4-5, pohl2024anoutermembrane pages 1-2).
3. **CrvA/CrvAB evidence gap in provided excerpts**: CrvA is referenced as causing rod-shape upon removal (pohl2024anoutermembrane pages 1-2) and CrvAB is described as a curvature system (pohl2024anoutermembrane pages 1-2), but primary mechanistic details (e.g., polymer properties, PG insertion bias) are not extracted here; curate cautiously until primary CrvAB/CrvA papers are ingested.

---

## DOI-first bibliography (with dates/URLs where available)

1. **Pöhl S. et al.** “An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in *Rhodospirillum rubrum*.” *Nature Communications* (2024). Received 2024-02-22; accepted 2024-08-14. DOI: **10.1038/s41467-024-51790-z**. URL: https://doi.org/10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13)
2. **Liu Y. et al.** “Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin.” *PNAS* (Published 2024-02-07). DOI: **10.1073/pnas.2309984121**. URL: https://doi.org/10.1073/pnas.2309984121 (liu2024filamentstructureand pages 1-2)
3. **Banks E.J. et al.** “Asymmetric peptidoglycan editing generates cell curvature in *Bdellovibrio* predatory bacteria.” *Nature Communications* (2022). DOI: **10.1038/s41467-022-29007-y**. URL: https://doi.org/10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2, banks2022asymmetricpeptidoglycanediting pages 10-11)
4. **Kysela D.T. et al.** “Diversity Takes Shape: Understanding the Mechanistic and Adaptive Basis of Bacterial Morphology.” *PLOS Biology* (2016-10-03). DOI: **10.1371/journal.pbio.1002565**. URL: https://doi.org/10.1371/journal.pbio.1002565 (kysela2016diversitytakesshape pages 4-5)
5. **van Teeseling M.C.F. et al.** “Determinants of Bacterial Morphology: From Fundamentals to Possibilities for Antimicrobial Targeting.” *Frontiers in Microbiology* (2017). DOI: **10.3389/fmicb.2017.01264**. URL: https://doi.org/10.3389/fmicb.2017.01264 (teeseling2017determinantsofbacterial pages 1-3, teeseling2017determinantsofbacterial pages 3-4)



References

1. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

2. (liu2024filamentstructureand pages 1-2): Yue Liu, Fusinita van den Ent, and Jan Löwe. Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin. Proceedings of the National Academy of Sciences, Feb 2024. URL: https://doi.org/10.1073/pnas.2309984121, doi:10.1073/pnas.2309984121. This article has 7 citations and is from a highest quality peer-reviewed journal.

3. (banks2022asymmetricpeptidoglycanediting pages 1-2): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 31 citations and is from a highest quality peer-reviewed journal.

4. (banks2022asymmetricpeptidoglycanediting pages 10-11): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 31 citations and is from a highest quality peer-reviewed journal.

5. (pohl2024anoutermembrane pages 12-13): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

6. (kysela2016diversitytakesshape pages 4-5): David T. Kysela, Amelia M. Randich, Paul D. Caccamo, and Yves V. Brun. Diversity takes shape: understanding the mechanistic and adaptive basis of bacterial morphology. PLOS Biology, 14:e1002565, Oct 2016. URL: https://doi.org/10.1371/journal.pbio.1002565, doi:10.1371/journal.pbio.1002565. This article has 149 citations and is from a highest quality peer-reviewed journal.

7. (teeseling2017determinantsofbacterial pages 3-4): Muriel C. F. van Teeseling, Miguel A. de Pedro, and Felipe Cava. Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01264, doi:10.3389/fmicb.2017.01264. This article has 224 citations and is from a peer-reviewed journal.

8. (pohl2024anoutermembrane media 1cc947a9): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (pohl2024anoutermembrane media 12d35527): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

10. (teeseling2017determinantsofbacterial pages 1-3): Muriel C. F. van Teeseling, Miguel A. de Pedro, and Felipe Cava. Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01264, doi:10.3389/fmicb.2017.01264. This article has 224 citations and is from a peer-reviewed journal.

11. (pohl2024anoutermembrane pages 18-19): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.