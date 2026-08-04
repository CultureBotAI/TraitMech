---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:38:00.789733'
end_time: '2026-08-04T09:45:52.015807'
duration_seconds: 471.23
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: prosthecate
  trait_identifier: traitmech:000065
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: prosthecate
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A morphology trait in which the cell bears one or more prosthecae \u2014\
    \ tubular extensions of the cell envelope (stalks) \u2014 that increase nutrient-uptake\
    \ surface area or mediate attachment, as in Caulobacter."
  parent_traits: METPO:1000059
  synonyms: stalked, prostheca
  evidence_summary: 'DOI:10.1111/j.1365-2958.2007.05633.x:  (Wagner & Brun describe
    the Caulobacter stalk (prostheca) as a cell-envelope extension and a specialized
    form of cell elongation aiding nutrient uptake.) | DOI:10.1128/MMBR.00040-09:  (Curtis
    & Brun''s review of Caulobacter development supports the stalk as a regulated
    developmental appendage.)'
  causal_graph_summary: 'prosthecate_stalk_nutrient_uptake: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prosthecate
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000065
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell bears one or more prosthecae — tubular extensions of the cell envelope (stalks) — that increase nutrient-uptake surface area or mediate attachment, as in Caulobacter.
- **Parent traits:** METPO:1000059
- **Synonyms:** stalked, prostheca
- **Existing evidence:** DOI:10.1111/j.1365-2958.2007.05633.x:  (Wagner & Brun describe the Caulobacter stalk (prostheca) as a cell-envelope extension and a specialized form of cell elongation aiding nutrient uptake.) | DOI:10.1128/MMBR.00040-09:  (Curtis & Brun's review of Caulobacter development supports the stalk as a regulated developmental appendage.)
- **Existing causal graph summary:** prosthecate_stalk_nutrient_uptake: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **prosthecate** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/prosthecate.yaml`.

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
- **Trait label:** prosthecate
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000065
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell bears one or more prosthecae — tubular extensions of the cell envelope (stalks) — that increase nutrient-uptake surface area or mediate attachment, as in Caulobacter.
- **Parent traits:** METPO:1000059
- **Synonyms:** stalked, prostheca
- **Existing evidence:** DOI:10.1111/j.1365-2958.2007.05633.x:  (Wagner & Brun describe the Caulobacter stalk (prostheca) as a cell-envelope extension and a specialized form of cell elongation aiding nutrient uptake.) | DOI:10.1128/MMBR.00040-09:  (Curtis & Brun's review of Caulobacter development supports the stalk as a regulated developmental appendage.)
- **Existing causal graph summary:** prosthecate_stalk_nutrient_uptake: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **prosthecate** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/prosthecate.yaml`.

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


# Curation report: prosthecate morphology

## Executive summary

**Trait:** `traitmech:000065` (**prosthecate**); category **MORPHOLOGY**; term kind **CLASS**; reviewed parent **METPO:1000059**.

The defensible core phenotype is: **a cell bearing one or more thin, tubular/cylindrical extensions continuous with the cell envelope and produced by spatially restricted peptidoglycan (PG) growth**. In *Caulobacter crescentus*, the prostheca contains inner membrane, PG, and outer membrane, is depleted of cytoplasm, DNA, and ribosomes, and is subdivided by proteinaceous crossbands. It is therefore unlike a proteinaceous flagellum or pilus. The adhesive holdfast may occur at its tip, but is a separate organelle and—notably—attachment can precede stalk synthesis. (billini2019aspecializedmrebdependent pages 2-3, curtis2010gettinginthe pages 2-3, barrows2023synchronizedswarmersand pages 5-7)

The best-supported causal core for an initial TraitMech graph is:

**phosphate limitation → polar concentration/operation of a specialized MreB-dependent PG complex → zonal PG synthesis and remodeling near the stalk base → prostheca elongation**, with **BacA/BacB–PbpC** contributing to normal stalk length in *Caulobacter*. In *Asticcacaulis biprosthecum*, **BacA positions SpmX and constrains the stalk PG growth zone**; loss of that organization produces broad pseudostalks rather than normal prosthecae. (billini2019aspecializedmrebdependent pages 14-16, billini2019aspecializedmrebdependent pages 19-21, billini2019aspecializedmrebdependent pages 18-19, jacq2024functionalspecializationof pages 1-6)

Directly asserting **prostheca → increased nutrient uptake** is not presently advisable as a universal curated edge. It is a classic adaptive hypothesis, but the 2023 authoritative review notes that crossband-mediated restriction of protein diffusion challenges the simple “nutrient-scavenging antenna” model. Nutrient access by elevation above a biofilm and increased surface area in other taxa remain plausible but incompletely tested alternatives. (billini2019aspecializedmrebdependent pages 2-3, barrows2023synchronizedswarmersand pages 5-7, hao2018novelprosthecatebacteria pages 9-10)

| Candidate causal module | Representative subject-predicate-object edge | Evidence strength | Principal taxon | Curation recommendation |
|---|---|---|---|---|
| Phosphate-responsive stalk elongation | phosphate limitation -> increases -> stalk elongation / stalk length | strong | *Caulobacter crescentus* | Curate as an environmental driver of prostheca elongation, but keep separate from initiation control because some stalkless mutants recover under phosphate limitation, implying distinct regulation of initiation vs elongation (billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 7-8, barrows2023synchronizedswarmersand pages 5-7) |
| Hybrid stalk PG synthesis complex | MreB/RodZ/RodA/PBP2 hybrid complex -> mediates -> zonal stalk-base peptidoglycan synthesis | strong | *Caulobacter crescentus* | High-priority core module for TraitMech; supported by localization, depletion, mutant, and labeling data showing a specialized stalk biosynthetic complex distinct from generic elongasome/divisome functions (billini2019aspecializedmrebdependent pages 18-19, billini2019aspecializedmrebdependent pages 14-16, billini2019aspecializedmrebdependent pages 8-10) |
| BacA/BacB-PbpC stalk elongation module | BacA/BacB -> recruits/positions -> PbpC; PbpC -> promotes -> normal stalk length | moderate | *Caulobacter crescentus* | Curate as a taxon-specific elongation module with moderate confidence; evidence supports contribution to stalk length, but not absolute necessity for stalk synthesis (billini2019aspecializedmrebdependent pages 19-21, jacq2024functionalspecializationof pages 1-6, barrows2023synchronizedswarmersand pages 5-7) |
| BacA-SpmX topological organizer | BacA -> anchors/positions -> SpmX at stalk base | strong | *Asticcacaulis biprosthecum* | Curate, but mark as lineage-specific; strong evidence that BacA constrains zonal PG insertion by positioning SpmX, and loss causes pseudostalks rather than true stalks (jacq2024functionalspecializationof pages 1-6, kysela2016diversitytakesshape pages 7-9) |
| Crossband compartmentalization | crossbands -> restricts -> protein diffusion between cell body and stalk / among stalk compartments | strong | *Caulobacter crescentus* | Curate as a structural compartmentalization feature associated with prosthecae; useful for downstream edges involving localization and stalk physiology (billini2019aspecializedmrebdependent pages 2-3, barrows2023synchronizedswarmersand pages 5-7) |
| Prostheca-mediated nutrient access | prostheca -> increases -> nutrient uptake/access | uncertain | *Caulobacter crescentus*; candidate phylum Acetothermia bacterium Ran1 | Do not yet curate as a direct universal causal edge; retain as hypothesis/weak adaptive claim because reviews note the classic uptake model is challenged, and some recent sources frame it as possible nutrient access or surface-area advantage rather than demonstrated mechanism (barrows2023synchronizedswarmersand pages 5-7, hao2018novelprosthecatebacteria pages 9-10, billini2019aspecializedmrebdependent pages 2-3) |
| Holdfast-mediated attachment | holdfast -> mediates -> surface attachment | strong | *Caulobacter crescentus* | Curate separately from prostheca proper; sources explicitly distinguish holdfast-driven adhesion from stalk identity and indicate the prostheca itself should not be equated with the attachment organelle (billini2019aspecializedmrebdependent pages 2-3, curtis2010gettinginthe pages 2-3, barrows2023synchronizedswarmersand pages 5-7) |


*Table: This table summarizes the highest-priority causal modules for curating the prosthecate trait, highlighting which edges are strongly supported versus uncertain. It is useful for deciding what should enter the TraitMech graph now and what should remain provisional or taxon-specific.*

## 1. Trait scope and boundaries

### 1.1 Inclusion rule

Annotate **prosthecate** when microscopy or equivalent morphological evidence demonstrates one or more narrow cell-envelope extensions. Diagnostic features are:

1. continuity with cell-envelope layers;
2. thin tubular or cylindrical geometry;
3. formation by localized/zonal PG synthesis rather than assembly of an extracellular protein filament;
4. polar, subpolar, lateral, or bilateral placement is permitted;
5. the structure need not carry a holdfast and need not mediate reproduction.

In *C. crescentus*, stalk synthesis begins when a swarmer differentiates into a stalked cell at the previously flagellated pole. The stalked form is replication- and division-competent, whereas the swarmer bears flagellum and pili. (billini2019aspecializedmrebdependent pages 2-3, curtis2010gettinginthe pages 2-3)

### 1.2 Morphological diversity and taxonomic scope

The trait is broader than *Caulobacter*. Comparative evidence supports ancestral polar prosthecae, subsequent subpolar and lateral repositioning in *Asticcacaulis*, duplication to bilateral prosthecae in *A. biprosthecum*, and independent losses in some related lineages. Representative configurations include polar *C. crescentus*, subpolar *A. excentricus*, and bilateral midcell *A. biprosthecum*. (kysela2016diversitytakesshape pages 7-9)

A morphologically distinct anaerobic-digester organism, “Candidatus Bipolaricaulis anaerobius” (Acetothermia), has a rod-shaped body with bipolar prosthecae. Its inferred surface-area and substrate-competition benefits are ecological hypotheses rather than experimentally demonstrated causal mechanisms. (hao2018novelprosthecatebacteria pages 9-10)

### 1.3 Boundary cases

- **Flagella and pili:** exclude. They are distinct appendages, not continuous three-layer envelope extensions. In *Caulobacter*, the flagellum and pili are removed/retracted during differentiation before stalk establishment. (curtis2010gettinginthe pages 2-3, barrows2023synchronizedswarmersand pages 5-7)
- **Holdfast:** exclude from the trait definition. It is an adhesive polysaccharide organelle that can tip the stalk, but holdfast production and initial attachment precede stalk biogenesis. Some prosthecate bacteria place adhesion and stalks at different sites. (barrows2023synchronizedswarmersand pages 5-7)
- **Pseudostalks:** do not annotate as unqualified normal prosthecae when the phenotype is a short, broad protrusion caused by dysregulated PG insertion, such as *A. biprosthecum* Δ*bacA*. Represent these as an abnormal-prostheca morphology or failed prostheca morphogenesis. (jacq2024functionalspecializationof pages 1-6)
- **Reproductive stalks/hyphae:** a stalk used to bud a daughter cell, as in *Hyphomonas*, can still be a prostheca if it is a narrow envelope extension. Reproductive function should be modeled separately; it is not defining for `traitmech:000065`. (jacq2024functionalspecializationof pages 1-6)
- **“Stalked” cells without envelope continuity:** the English synonym is ambiguous. Require structural evidence rather than name-based annotation.
- **Stalk length:** environmentally plastic length is not a separate prerequisite. Phosphate starvation can elongate existing prosthecae or induce prostheca formation where none was visible under replete conditions. (caccamo2018themolecularbasis pages 4-6)

## 2. Candidate causal-graph nodes

### Environmental and experimental factors

- phosphate limitation / phosphate starvation — label-only pending verified ENVO or assay identifier;
- phosphate-replete medium — label-only;
- surface-attached biofilm context — label-only;
- HADA or fluorescent D-amino-acid labeling — experimental factor, not a biological causal node;
- A22, an MreB perturbant used experimentally — assay/inhibitor node only;
- mecillinam/PBP2 inhibition — supporting perturbation node, if the intended graph permits experimental interventions.

### Structures and cellular locations

- prostheca / stalk — target phenotype `traitmech:000065`;
- stalk base / stalk-proximal polar cap — label-only candidate;
- stalked pole / old cell pole — label-only;
- peptidoglycan-based cell wall — **GO:0009274**;
- periplasmic space — **GO:0030288**;
- inner membrane and outer membrane — use verified GO cellular-component terms during implementation;
- crossband complex — label-only;
- holdfast — label-only and separate from prostheca;
- specialized stalk PG biosynthetic complex — label-only complex;
- pseudostalk — label-only abnormal morphology.

### Genes and proteins

**Core *Caulobacter* module:** MreB, RodZ, RodA, PBP2, MreC/MreD, DipM, SdpA, SdpB, CrbA, BacA, BacB, PbpC, and LdpA. Protein identifiers should remain label-only until strain-specific UniProt accessions are checked; ortholog names alone are insufficient for safe grounding. The evidence supports a hybrid complex containing elongasome-associated MreB/RodZ/RodA/PBP2 and proteins typically associated with division/remodeling, including DipM/SdpA/SdpB/CrbA. (billini2019aspecializedmrebdependent pages 14-16, billini2019aspecializedmrebdependent pages 18-19)

**PG chemistry module:** LdtD and LdtX LD-transpeptidases; 3–3 PG crosslinks; 4–3 PG crosslinks; trimeric muropeptides; PG synthesis and PG remodeling. Stalk PG is enriched in 3–3 crosslinks and total peptide crosslinking, although LD-transpeptidase activity is not essential for stalk formation because compensatory 4–3 crosslinking occurs. (billini2019aspecializedmrebdependent pages 7-8, billini2019aspecializedmrebdependent pages 8-10)

**Topological-developmental module:** SpmX and BacA in *Asticcacaulis*. Species-qualified nodes are essential because BacA has different degrees of necessity and distinct partners across taxa. (jacq2024functionalspecializationof pages 1-6, kysela2016diversitytakesshape pages 7-9)

**Developmental signaling candidates:** PleC, DivJ, PleD, c-di-GMP, and the swarmer-to-stalked transition. These regulate cell fate, and *pleC* mutants can lose stalks, but the evidence assembled here does not justify a simple direct edge from every signaling component to prostheca synthesis. Treat this as a secondary, taxon-specific module requiring primary-source edge validation. (barrows2023synchronizedswarmersand pages 9-11)

**Physiology candidates:** StpX, Zn²⁺ toxicity protection, and Cu²⁺ storage/utilization. These concern stalk-associated physiology rather than production of the trait and require their original primary paper before graph inclusion. (barrows2023synchronizedswarmersand pages 5-7)

### Processes and functions

- regulation of cell shape — **GO:0008360**;
- cell cycle — **GO:0007049**;
- zonal PG biosynthesis — label-only unless an exact GO term is verified;
- PG remodeling, stalk initiation, stalk elongation, protein diffusion restriction, surface attachment, nutrient uptake/access, and swarmer-to-stalked differentiation — retain as label-only candidate processes pending exact ontology review.

## 3. Candidate evidence-backed causal edges

The snippets below are short source-derived excerpts or close extractive summaries. “Strong” denotes direct perturbation, localization, chemical-labeling, or structural evidence; “moderate” denotes convergent but partial evidence; “uncertain” denotes an adaptive hypothesis.

| # | Candidate subject–predicate–object triple | Evidence snippet | Reference | Strength and curation note |
|---:|---|---|---|---|
| 1 | phosphate starvation → **increases** → prostheca elongation | “its length increases up to 20-fold under conditions of phosphate limitation” | Billini et al. 2019 | **Strong; *C. crescentus*.** Curate as environmental modulation, not as a universal prerequisite. (billini2019aspecializedmrebdependent pages 2-3) |
| 2 | phosphate starvation → **redirects** → PG synthesis toward stalked pole | “phosphate starvation induces a switch…that ultimately limits cell growth to the stalked cell pole” | Billini et al. 2019 | **Strong.** HADA time course supports redistribution of growth activity. (billini2019aspecializedmrebdependent pages 7-8) |
| 3 | zonal PG incorporation at stalk base → **drives** → prostheca formation/elongation | Formation is “driven by zonal incorporation of new cell wall material at the stalk base” | Billini et al. 2019 | **Strong.** Supported by tritiated glucose, radiolabeled D-cysteine, and fluorescent D-alanine derivatives. (billini2019aspecializedmrebdependent pages 2-3) |
| 4 | stalk-proximal polar-cap expansion/remodeling → **produces** → new stalk segment | New PG occurs mainly in adjacent polar regions rather than the basal stalk segment | Billini et al. 2019 | **Strong but mechanistically specific.** Prefer over a simplistic “material added directly to stalk tube” model. (billini2019aspecializedmrebdependent pages 18-19) |
| 5 | MreB → **organizes/enables** → polar stalk PG biosynthetic complex | An *mreB* sandwich-fusion strain “failed to form stalks” in both standard and phosphate-limited media | Billini et al. 2019 | **Strong; allele-specific evidence.** The variant blocked polar condensation/interactions and was stalkless under tested conditions. (billini2019aspecializedmrebdependent pages 18-19) |
| 6 | RodZ → **promotes** → stalk biosynthesis under phosphate limitation | RodZ was specifically required for stalk biosynthesis during phosphate limitation | Billini et al. 2019 | **Strong, condition-qualified.** Do not infer universal essentiality. (billini2019aspecializedmrebdependent pages 14-16) |
| 7 | RodA → **promotes** → stalk elongation | RodA depletion “severely reduces stalk elongation under phosphate limitation” | Billini et al. 2019 | **Strong; *C. crescentus*.** (billini2019aspecializedmrebdependent pages 8-10) |
| 8 | PBP2 → **participates in** → stalk PG synthesis | RodA and PBP2 are required and show a focus at the stalked pole | Billini et al. 2019 | **Strong/moderate.** Include within the complex rather than overstate a unique standalone role. (billini2019aspecializedmrebdependent pages 8-10) |
| 9 | MreB–RodZ–RodA–PBP2 plus DipM/SdpA/SdpB/CrbA → **constitute** → specialized stalk PG complex | The complex is a “hybrid composed of factors typically associated with the elongasome…or divisome” | Billini et al. 2019 | **Strong conceptual complex edge.** FtsZ itself is not detected at the stalked pole. (billini2019aspecializedmrebdependent pages 18-19) |
| 10 | SdpA and SdpB → **enable** → stalk PG remodeling/formation | Lytic transglycosylases SdpA and SdpB are essential for stalk formation | Billini et al. 2019 | **Strong, taxon-specific.** (billini2019aspecializedmrebdependent pages 19-21) |
| 11 | BacA → **recruits** → PbpC at stalked pole | BacA is required for proper length and recruits class-A PBP PbpC | Billini et al. 2019 | **Moderate/strong.** Curate as a stalk-length module, not absolute trait determination. (billini2019aspecializedmrebdependent pages 19-21) |
| 12 | PbpC → **promotes** → normal stalk length | “*pbpC* deletion causes moderate reduction in stalk length” | Billini et al. 2019 | **Moderate.** Quantitative direction is supported; effect is not all-or-none. (billini2019aspecializedmrebdependent pages 8-10) |
| 13 | LdpA with BacA → **promotes** → stalk formation/length | *ldpA* deletion reduces stalk length; *ldpA* and *bacA* occur in a conserved operon | Billini et al. 2019 | **Moderate.** Cooperation is supported, but avoid encoding direct physical interaction without additional evidence. (billini2019aspecializedmrebdependent pages 14-16, billini2019aspecializedmrebdependent pages 19-21) |
| 14 | BacA (*A. biprosthecum*) → **anchors/positions** → SpmX at stalk base | BacA “anchors…SpmX, which in turn regulates PG synthesis at the base” | Jacq et al. 2024 preprint | **Strong but preprint/lineage-specific.** Earlier comparative work also supports SpmX positioning of prosthecal PG synthesis. (jacq2024functionalspecializationof pages 1-6, kysela2016diversitytakesshape pages 7-9) |
| 15 | loss of BacA → **causes** → pseudostalks through unregulated PG insertion | Δ*bacA* makes “shorter and wider protrusions”; SpmX is mislocalized throughout pseudostalks | Jacq et al. 2024 preprint | **Strong phenotype; preprint.** Curate as abnormal morphogenesis, not as loss of every envelope protrusion. (jacq2024functionalspecializationof pages 1-6) |
| 16 | BacA polymerization and terminal domains → **enable** → proper stalk morphogenesis | Polymerization-defective substitutions and N-/C-terminal deletions produce localization and stalk defects | Jacq et al. 2024 preprint | **Moderate/strong, preprint.** One reported comparison found only **5 ± 1%** wild-type-like stalks in an N-terminal deletion mutant versus **46 ± 3%** in controls. (jacq2024functionalspecializationof pages 6-10) |
| 17 | crossbands → **restrict** → protein diffusion between body and stalk compartments | Crossbands “create diffusion barriers that prevent exchange of proteins” | Barrows & Goley 2023 | **Strong structural/physiological edge.** Curate separately from stalk formation. (barrows2023synchronizedswarmersand pages 5-7) |
| 18 | holdfast → **mediates** → surface attachment | The stalk tip carries an “adhesive holdfast mediating surface attachment” | Billini et al. 2019 | **Strong, but not a prostheca-production edge.** Keep holdfast and stalk distinct. (billini2019aspecializedmrebdependent pages 2-3) |
| 19 | prostheca → **increases** → nutrient uptake | Initially proposed through increased surface area, but “challenged by the apparent lack of protein diffusion along the stalk” | Barrows & Goley 2023 | **Uncertain; do not curate as universal/direct.** (barrows2023synchronizedswarmersand pages 5-7) |
| 20 | prostheca elongation → **elevates** → cell body beyond biofilm surface → **may increase** nutrient exposure | Review presents elevation into nutrient-rich medium as a newer hypothesis | Barrows & Goley 2023 | **Uncertain and context-specific.** Difficult to generalize to *Asticcacaulis*. (barrows2023synchronizedswarmersand pages 5-7) |
| 21 | bipolar prosthecae → **increase** → surface-area-to-volume ratio → **may improve** substrate competition | The Acetothermia study states the morphology “might enable it to compete for substrates” | Hao et al. 2018 | **Uncertain ecological inference.** No direct uptake measurement; do not merge with the *Caulobacter* mechanism. (hao2018novelprosthecatebacteria pages 9-10) |
| 22 | stalk formation → **is not required for** → cell division | Stalk formation “is not strictly required for division to occur” | Barrows & Goley 2023 | **Strong negative boundary edge.** Useful to prevent an erroneous obligatory stalk→division relation. (barrows2023synchronizedswarmersand pages 5-7) |

## 4. Quantitative findings relevant to curation

- Under phosphate limitation, *C. crescentus* stalk length can increase by **up to 20-fold**. (billini2019aspecializedmrebdependent pages 2-3)
- During the phosphate-starvation assay, stalk elongation remained approximately constant at **0.28 ± 0.03 μm h⁻¹**. (billini2019aspecializedmrebdependent pages 7-8)
- PG-labeling analyses found that cells longer than approximately **4 μm** often also exhibited a midcell growth focus early in starvation; after **>18 h**, midcell foci were nearly absent and signal was largely confined to the stalk base. (billini2019aspecializedmrebdependent pages 7-8)
- The 2019 mutant/localization study commonly quantified approximately **200–210 cells per strain/condition**; one reported mutant comparison used **n=208** and **p<10⁻⁶**. These values strengthen the measured morphological effects but do not establish universality beyond the tested strain and conditions. (billini2019aspecializedmrebdependent pages 14-16, billini2019aspecializedmrebdependent pages 18-19)
- The 2024 *A. biprosthecum* preprint reported **5 ± 1%** wild-type-like stalk formation for one N-terminal BacA deletion mutant versus **46 ± 3%** in the control comparison. Treat these data as provisional until peer review. (jacq2024functionalspecializationof pages 6-10)

## 5. Recent developments, applications, and expert analysis

### 2023 synthesis

Barrows and Goley’s February 2023 review is the most useful recent authoritative synthesis. It emphasizes that the stalk is an envelope-derived, crossband-compartmentalized structure; separates holdfast-mediated adhesion from stalk function; and concludes that no single nutrient-acquisition model explains prosthecae across *Caulobacter* and *Asticcacaulis*. It also highlights *Caulobacter* as a model for cell-cycle asymmetry, synchronization, cryo-electron tomography, protein localization, chromosome segregation, and integrated “localisome,” CauloBrowser, and mutant-fitness resources. (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 9-11)

### 2024 mechanistic advance

The December 16, 2024 *A. biprosthecum* preprint dissects BacA into a polymerizing central β-helical core and flanking domains implicated in membrane association and SpmX interaction. Its principal advance is that stalk morphogenesis depends not merely on BacA presence, but on polymerization, correct membrane localization, and domain-specific scaffolding. This is valuable for representing **topological organization** as an explicit causal layer between a cytoskeletal protein and zonal PG synthesis. Because this source was a preprint in 2024, its fine-grained domain edges should carry provisional evidence status. (jacq2024functionalspecializationof pages 6-10, jacq2024functionalspecializationof pages 1-6)

### Real-world and research implementations

1. **Nonessential organelle model:** the prostheca provides a tractable system for studying localized cell-wall synthesis without directly abolishing cell division, helping disentangle PG elongation, division, and specialized morphogenesis. (billini2019aspecializedmrebdependent pages 18-19, randich2015molecularmechanismsfor pages 7-9)
2. **Environmental-response assays:** phosphate withdrawal provides an experimentally useful way to suppress division while strongly promoting stalk elongation, exposing stalk-specific machinery. (billini2019aspecializedmrebdependent pages 18-19)
3. **Morphology discovery:** fluorescent D-amino acids, automated microscopy, single-cell genomics, and comparative genetics can reveal prostheca growth zones and determinants in uncultured or experimentally underdeveloped taxa. (kysela2016diversitytakesshape pages 7-9)
4. **Wastewater microbiome interpretation:** combined metagenomics, FISH, confocal imaging, Raman microspectroscopy, and atomic-force microscopy identified a bipolar prosthecate Acetothermia population in full-scale anaerobic digesters. Its role in consuming soluble intermediates and supplying acetate, formate, and hydrogen to methanogens is reconstructed from genomic/ecological evidence, not a deployed engineering intervention. (hao2018novelprosthecatebacteria pages 9-10)

## 6. Recommended minimal graph for `prosthecate.yaml`

A conservative first expansion of the existing graph should prioritize:

1. `phosphate limitation` → **increases** → `stalk elongation` [*C. crescentus*, condition-specific];
2. `MreB` → **organizes** → `specialized stalk PG biosynthetic complex`;
3. `RodZ`, `RodA`, `PBP2` → **participate in** → `specialized stalk PG biosynthetic complex`;
4. `specialized stalk PG biosynthetic complex` → **mediates** → `zonal PG synthesis at stalk-proximal pole`;
5. `zonal PG synthesis/remodeling` → **produces** → `prostheca elongation`;
6. `BacA/BacB` → **positions or recruits** → `PbpC`;
7. `PbpC` → **promotes** → `normal stalk length`;
8. `crossbands` → **restrict** → `protein diffusion between stalk and cell body`;
9. species-specific branch: `A. biprosthecum BacA` → **positions** → `SpmX` → **constrains** → `stalk-base PG synthesis`;
10. abnormal branch: `loss of A. biprosthecum BacA` → **causes** → `SpmX mislocalization/unregulated PG insertion` → **causes** → `pseudostalk`.

The nutrient-uptake and direct-attachment edges should not be part of the required core. If retained, model them as explicitly **hypothesized** adaptive consequences and separate `holdfast → surface attachment` from the prostheca node.

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not curate “prostheca directly causes nutrient uptake” as established or universal.** Current expert analysis regards stalk function as unresolved and explicitly challenges the simple uptake model. (barrows2023synchronizedswarmersand pages 5-7)
2. **Do not equate stalk with holdfast or adhesion.** Attachment is mediated by holdfast; holdfast synthesis can precede stalk synthesis, and stalk and adhesin can occur at separate sites. (barrows2023synchronizedswarmersand pages 5-7)
3. **Do not generalize the *Caulobacter* polar mechanism to every prosthecate lineage.** *Asticcacaulis* uses different positioning logic, and Acetothermia mechanisms remain largely unknown. (jacq2024functionalspecializationof pages 1-6, kysela2016diversitytakesshape pages 7-9, hao2018novelprosthecatebacteria pages 9-10)
4. **Do not treat LD-transpeptidase-generated 3–3 crosslinks as necessary for the trait.** They characterize stalk PG, but compensatory 4–3 crosslinking permits stalk formation when LdtD/LdtX activity is lost. (billini2019aspecializedmrebdependent pages 8-10)
5. **Do not infer that FtsZ directly forms the stalk growth zone.** FtsZ was not detectable at the stalked pole; the specialized complex borrows some divisome-associated remodeling proteins without the canonical FtsZ-organized divisome. (billini2019aspecializedmrebdependent pages 18-19)
6. **Do not represent BacA as universally essential.** BacA/BacB deletion reduces stalk length in *C. crescentus*, whereas *A. biprosthecum* BacA is a key topological organizer whose loss yields pseudostalks. (jacq2024functionalspecializationof pages 1-6)
7. **Do not over-curate the 2024 BacA domain model.** It is valuable recent evidence but was a preprint; mark polymerization-domain, membrane-binding, and SpmX-interaction edges provisional. (jacq2024functionalspecializationof pages 6-10, jacq2024functionalspecializationof pages 1-6)
8. **Verify all species-specific UniProt, KEGG, Rhea, EC, CHEBI, ENVO, and NCBITaxon CURIEs before YAML insertion.** This report intentionally leaves uncertain nodes label-only rather than inventing identifiers.

## 8. DOI-first bibliography

1. **Barrows JM, Goley ED.** “Synchronized Swarmers and Sticky Stalks: *Caulobacter crescentus* as a Model for Bacterial Cell Biology.” *Journal of Bacteriology* 205(2), **February 2023**. DOI: [10.1128/jb.00384-22](https://doi.org/10.1128/jb.00384-22). (barrows2023synchronizedswarmersand pages 5-7, barrows2023synchronizedswarmersand pages 9-11)
2. **Jacq M, Caccamo PD, Brun YV.** “Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in *Asticcacaulis biprosthecum*.” bioRxiv, **December 16, 2024**. DOI: [10.1101/2024.12.16.628611](https://doi.org/10.1101/2024.12.16.628611). Preprint. (jacq2024functionalspecializationof pages 6-10, jacq2024functionalspecializationof pages 1-6)
3. **Billini M, Biboy J, Kühn J, Vollmer W, Thanbichler M.** “A specialized MreB-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in *Caulobacter crescentus*.” *PLOS Genetics* 15:e1007897, **February 1, 2019**. DOI: [10.1371/journal.pgen.1007897](https://doi.org/10.1371/journal.pgen.1007897). (billini2019aspecializedmrebdependent pages 7-8, billini2019aspecializedmrebdependent pages 2-3, billini2019aspecializedmrebdependent pages 18-19)
4. **Hao L et al.** “Novel prosthecate bacteria from the candidate phylum Acetothermia.” *ISME Journal* 12:2225–2237, **June 2018**. DOI: [10.1038/s41396-018-0187-9](https://doi.org/10.1038/s41396-018-0187-9). (hao2018novelprosthecatebacteria pages 9-10)
5. **Caccamo PD, Brun YV.** “The Molecular Basis of Noncanonical Bacterial Morphology.” *Trends in Microbiology* 26:191–208, **March 2018**. DOI: [10.1016/j.tim.2017.09.012](https://doi.org/10.1016/j.tim.2017.09.012). (caccamo2018themolecularbasis pages 4-6)
6. **Kysela DT, Randich AM, Caccamo PD, Brun YV.** “Diversity Takes Shape: Understanding the Mechanistic and Adaptive Basis of Bacterial Morphology.” *PLOS Biology* 14:e1002565, **October 3, 2016**. DOI: [10.1371/journal.pbio.1002565](https://doi.org/10.1371/journal.pbio.1002565). (kysela2016diversitytakesshape pages 7-9)
7. **Randich AM, Brun YV.** “Molecular mechanisms for the evolution of bacterial morphologies and growth modes.” *Frontiers in Microbiology* 6:580, **June 2015**. DOI: [10.3389/fmicb.2015.00580](https://doi.org/10.3389/fmicb.2015.00580). (randich2015molecularmechanismsfor pages 7-9)
8. **Curtis PD, Brun YV.** “Getting in the Loop: Regulation of Development in *Caulobacter crescentus*.” *Microbiology and Molecular Biology Reviews* 74:13–41, **March 2010**. DOI: [10.1128/MMBR.00040-09](https://doi.org/10.1128/MMBR.00040-09). (curtis2010gettinginthe pages 2-3)
9. **Wagner JK, Brun YV.** “Out on a limb: how the *Caulobacter* stalk can boost the study of bacterial cell shape.” *Molecular Microbiology* 64:28–33, **April 2007**. DOI: [10.1111/j.1365-2958.2007.05633.x](https://doi.org/10.1111/j.1365-2958.2007.05633.x). This is foundational existing evidence, but the nutrient-uptake interpretation should be reconciled with the more cautious 2023 synthesis.

References

1. (billini2019aspecializedmrebdependent pages 2-3): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

2. (curtis2010gettinginthe pages 2-3): Patrick D. Curtis and Yves V. Brun. Getting in the loop: regulation of development in caulobacter crescentus. Microbiology and Molecular Biology Reviews, 74:13-41, Mar 2010. URL: https://doi.org/10.1128/mmbr.00040-09, doi:10.1128/mmbr.00040-09. This article has 313 citations and is from a domain leading peer-reviewed journal.

3. (barrows2023synchronizedswarmersand pages 5-7): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 61 citations and is from a peer-reviewed journal.

4. (billini2019aspecializedmrebdependent pages 14-16): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

5. (billini2019aspecializedmrebdependent pages 19-21): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

6. (billini2019aspecializedmrebdependent pages 18-19): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

7. (jacq2024functionalspecializationof pages 1-6): Maxime Jacq, Paul D. Caccamo, and Yves V. Brun. Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in asticcacaulis biprosthecum. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.16.628611, doi:10.1101/2024.12.16.628611. This article has 1 citations.

8. (hao2018novelprosthecatebacteria pages 9-10): Liping Hao, Simon Jon McIlroy, Rasmus Hansen Kirkegaard, Søren Michael Karst, Warnakulasuriya Eustace Yrosh Fernando, Hüsnü Aslan, Rikke Louise Meyer, Mads Albertsen, Per Halkjær Nielsen, and Morten Simonsen Dueholm. Novel prosthecate bacteria from the candidate phylum acetothermia. The ISME Journal, 12:2225-2237, Jun 2018. URL: https://doi.org/10.1038/s41396-018-0187-9, doi:10.1038/s41396-018-0187-9. This article has 77 citations.

9. (billini2019aspecializedmrebdependent pages 7-8): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

10. (billini2019aspecializedmrebdependent pages 8-10): Maria Billini, Jacob Biboy, Juliane Kühn, Waldemar Vollmer, and Martin Thanbichler. A specialized mreb-dependent cell wall biosynthetic complex mediates the formation of stalk-specific peptidoglycan in caulobacter crescentus. PLoS Genetics, 15:e1007897, Feb 2019. URL: https://doi.org/10.1371/journal.pgen.1007897, doi:10.1371/journal.pgen.1007897. This article has 49 citations and is from a domain leading peer-reviewed journal.

11. (kysela2016diversitytakesshape pages 7-9): David T. Kysela, Amelia M. Randich, Paul D. Caccamo, and Yves V. Brun. Diversity takes shape: understanding the mechanistic and adaptive basis of bacterial morphology. PLOS Biology, 14:e1002565, Oct 2016. URL: https://doi.org/10.1371/journal.pbio.1002565, doi:10.1371/journal.pbio.1002565. This article has 150 citations and is from a highest quality peer-reviewed journal.

12. (caccamo2018themolecularbasis pages 4-6): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.

13. (barrows2023synchronizedswarmersand pages 9-11): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 61 citations and is from a peer-reviewed journal.

14. (jacq2024functionalspecializationof pages 6-10): Maxime Jacq, Paul D. Caccamo, and Yves V. Brun. Functional specialization of the subdomains of a bactofilin driving stalk morphogenesis in asticcacaulis biprosthecum. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.16.628611, doi:10.1101/2024.12.16.628611. This article has 1 citations.

15. (randich2015molecularmechanismsfor pages 7-9): Amelia M. Randich and Yves V. Brun. Molecular mechanisms for the evolution of bacterial morphologies and growth modes. Frontiers in Microbiology, Jun 2015. URL: https://doi.org/10.3389/fmicb.2015.00580, doi:10.3389/fmicb.2015.00580. This article has 105 citations and is from a peer-reviewed journal.