---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T22:47:32.784926'
end_time: '2026-08-03T22:59:21.897353'
duration_seconds: 709.11
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: biofilm formation
  trait_identifier: traitmech:000053
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: biofilm_formation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An ecological lifestyle in which cells form surface-attached, matrix-enclosed\
    \ multicellular communities (biofilms) held together by extracellular polymeric\
    \ substances \u2014 a widespread mode of microbial life."
  parent_traits: METPO:1000059
  synonyms: biofilm-forming
  evidence_summary: 'DOI:10.1038/nrmicro.2016.94:  (Flemming et al. describe matrix-enclosed,
    surface-associated communities (biofilms) as an emergent, distinct mode of bacterial
    life.) | DOI:10.1038/s41579-019-0162-0:  (Flemming & Wuertz support the global
    ubiquity of the biofilm lifestyle across microbial habitats.)'
  causal_graph_summary: 'biofilm_eps_matrix_community: 13 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** biofilm formation
- **METPO identifier:** traitmech:000053
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which cells form surface-attached, matrix-enclosed multicellular communities (biofilms) held together by extracellular polymeric substances — a widespread mode of microbial life.
- **Parent traits:** METPO:1000059
- **Synonyms:** biofilm-forming
- **Existing evidence:** DOI:10.1038/nrmicro.2016.94:  (Flemming et al. describe matrix-enclosed, surface-associated communities (biofilms) as an emergent, distinct mode of bacterial life.) | DOI:10.1038/s41579-019-0162-0:  (Flemming & Wuertz support the global ubiquity of the biofilm lifestyle across microbial habitats.)
- **Existing causal graph summary:** biofilm_eps_matrix_community: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **biofilm formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biofilm_formation.yaml`.

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
- **Trait label:** biofilm formation
- **METPO identifier:** traitmech:000053
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological lifestyle in which cells form surface-attached, matrix-enclosed multicellular communities (biofilms) held together by extracellular polymeric substances — a widespread mode of microbial life.
- **Parent traits:** METPO:1000059
- **Synonyms:** biofilm-forming
- **Existing evidence:** DOI:10.1038/nrmicro.2016.94:  (Flemming et al. describe matrix-enclosed, surface-associated communities (biofilms) as an emergent, distinct mode of bacterial life.) | DOI:10.1038/s41579-019-0162-0:  (Flemming & Wuertz support the global ubiquity of the biofilm lifestyle across microbial habitats.)
- **Existing causal graph summary:** biofilm_eps_matrix_community: 13 nodes, 10 edges

## Research Objective

Research the microbial trait **biofilm formation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/biofilm_formation.yaml`.

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


# TraitMech curation report: biofilm formation

**Target:** biofilm formation (`traitmech:000053`; ECOLOGY; CLASS; REVIEWED)  
**Recommended graph strategy:** retain a small, taxon-neutral core and place *Pseudomonas aeruginosa*, *Bacillus subtilis*, and specialized matrix functions in explicitly scoped subgraphs.

## 1. Scope summary

Biofilm formation is the developmental capacity/process by which microorganisms produce spatially organized, matrix-embedded multicellular aggregates. Surface attachment is common, but it should not be made logically necessary: a 2024 primer defines biofilms as aggregates embedded in extracellular polymeric substances (EPS) and explicitly states that they may be surface-attached microcolonies or non-attached entities. The matrix generally contains polysaccharides, extracellular DNA (eDNA), proteins/amyloid fibres, lipid vesicles, adhesins, and sometimes incorporated host or environmental material (goltermann2024microbialprimerthe pages 1-3).

A recent structural review calls the extracellular matrix “a defining feature of all biofilms” and describes development from attachment through colony expansion and maturation. Matrix organization generates properties absent from planktonic cells, including mechanical cohesion and tolerance of chemical or physical stress (bohning2024theroleof pages 1-2). Thus, the supplied definition is broadly sound, but “surface-attached” should be interpreted as prototypical rather than universal.

### Boundaries

* **Adhesion is an upstream subprocess, not the complete trait.** Reversible attachment alone does not establish a mature, matrix-enclosed community. The commonly used sequence is reversible attachment → irreversible attachment → microcolony formation → maturation → dispersal (park2022controllingbiofilmdevelopment pages 1-2, sahoo2024biofilmformationin pages 2-3).
* **Aggregation alone is insufficient** unless cells exhibit a community-associated extracellular matrix or equivalent biofilm organization.
* **EPS production is central but not identical to biofilm formation.** A strain can express one matrix component without completing attachment, maturation, and architecture.
* **Pellicles are included.** Air–liquid-interface communities, such as *B. subtilis* pellicles, are biofilms even though their substrate is an interface rather than a solid surface (kovacs2019evolvedbiofilmreview pages 1-3).
* **Dispersal is a lifecycle transition/outcome**, not a positive instance of formation. It should be connected by `promotes`/`inhibits` edges but not treated as a synonym.
* **Antimicrobial tolerance, persistence, virulence, corrosion, and extracellular electron transfer are downstream or emergent properties**, not defining criteria.
* **Assay results require qualification.** Crystal-violet biomass, pellicle formation, colony wrinkling, attachment, viable-cell counts, and flow-cell architecture measure different aspects of the trait. A 2024 review warns that laboratory models vary in surfaces, shear, temperature, redox, pH, and nutrients and often do not reproduce real settings (yang2024classicalandmodern pages 1-2).

## 2. Candidate nodes and ontology grounding

Only identifiers that can be assigned conservatively are proposed. Label-only nodes are preferable to an unverified CURIE.

### Trait and biological-process nodes

| Node | Suggested grounding | Comment |
|---|---|---|
| biofilm formation | `traitmech:000053`; `GO:0042710` | Target trait; GO cross-reference is useful but does not replace METPO identity. |
| reversible attachment | Label only | Stage-specific subprocess. |
| irreversible attachment | Label only | Distinguished from initial surface contact. |
| microcolony formation | Label only | Intermediate developmental stage. |
| biofilm maturation | Label only | Matrix-rich, structured community development. |
| biofilm dispersal | Label only | Exit transition; generally inversely related to sessility. |
| extracellular-polymeric-substance matrix production | Label only | Core mechanistic process. |
| flagellar motility | `GO:0071973` | Use only where the experiment specifically concerns flagellum-dependent motility. |
| extracellular electron transfer | Label only | Specialized downstream function rather than core trait. |

### Chemicals and matrix materials

| Node | Suggested grounding | Role |
|---|---|---|
| cyclic di-GMP | `CHEBI:49537` | Intracellular second messenger controlling motile–sessile transitions. |
| GTP | `CHEBI:15996` | Diguanylate-cyclase substrate. |
| nitric oxide | `CHEBI:16480` | Dispersal cue in specific systems. |
| dioxygen | `CHEBI:15379` | Environmental electron acceptor; gradients shape pellicles and biofilm physiology. |
| extracellular DNA | Label only | Structural, chemical-binding, and electron-transfer matrix component. |
| Pel polysaccharide | Label only | *Pseudomonas*/Proteobacteria-specific matrix polymer. |
| Psl polysaccharide | Label only | *P. aeruginosa* attachment and matrix polymer. |
| alginate | `CHEBI:58187` | Mucoid matrix polysaccharide; importance is strain/context dependent. |
| TasA amyloid fibre | Label only | *B. subtilis* matrix protein. |
| pyocyanin | `CHEBI:62202` | Phenazine electron shuttle retained by eDNA. |
| EPS matrix | Label only | Composition varies markedly by species and environment. |

### Genes, proteins, complexes, and pathways

* **Broad bacterial signaling:** GGDEF-domain diguanylate cyclases (DGCs); EAL- and HD-GYP-domain phosphodiesterases (PDEs); c-di-GMP-binding effectors.
* ***P. aeruginosa* module:** `pelABCDEFG`; PelD/E/F/G synthase complex; `psl` locus; alginate-biosynthesis machinery including Alg44; flagellum; type-IV pili; OprF; SigX; DsbA; PA2200; LasI/LasR; RhlI/RhlR; GacS/GacA–RsmY/RsmZ; RpoS.
* ***B. subtilis* module:** Spo0A; AbrB; SinI; SinR; `epsA-O`; `tapA-sipW-tasA`; TasA.
* **Candidate taxa:** *Pseudomonas aeruginosa* (`NCBITaxon:287`) and *Bacillus subtilis* (`NCBITaxon:1423`). Taxon CURIEs should be attached to assertions, not used to imply universality.
* **Environmental/experimental nodes:** solid surface, air–liquid interface, conditioning film, surface roughness/hydrophobicity, shear, nutrient availability/depletion, carbon starvation, oxygen gradient, pH, ionic strength, temperature, sub-MIC antibiotic exposure, and redox stress.

## 3. Evidence-backed candidate edges

The following table is the proposed graph backbone and associated scoped modules.

| subject | predicate | object | scope/taxon | evidence strength |
|---|---|---|---|---|
| GGDEF-domain diguanylate cyclases (DGCs) | synthesize | c-di-GMP | conserved bacteria; especially well supported in *Pseudomonas aeruginosa* reviews/model systems | Strong, conserved, review-supported with mechanistic consensus (park2022controllingbiofilmdevelopment pages 1-2, valentini2016biofilmsandcyclic pages 1-2) |
| EAL- or HD-GYP-domain phosphodiesterases (PDEs) | degrade | c-di-GMP | conserved bacteria; especially well supported in *P. aeruginosa* reviews/model systems | Strong, conserved, review-supported with mechanistic consensus (park2022controllingbiofilmdevelopment pages 1-2, valentini2016biofilmsandcyclic pages 1-2) |
| high intracellular c-di-GMP | promotes | sessile/biofilm lifestyle and EPS production | conserved trend across many bacteria; quantitative data emphasized in *P. aeruginosa* | Strong for directionality; broad but species-tuned outputs differ (park2022controllingbiofilmdevelopment pages 1-2, park2022controllingbiofilmdevelopment pages 7-9, valentini2016biofilmsandcyclic pages 1-2) |
| high intracellular c-di-GMP | inhibits | motility | conserved trend across many bacteria; strong in *P. aeruginosa* | Strong, conserved, review-supported (park2022controllingbiofilmdevelopment pages 1-2, park2022controllingbiofilmdevelopment pages 7-9, valentini2016biofilmsandcyclic pages 1-2) |
| extracellular matrix / EPS production | enables | biofilm maturation and structural integrity | broad bacterial biofilms | Strong, broad, recent review support; not sufficient alone to define all biofilms (sahoo2024biofilmformationin pages 2-3, bohning2024theroleof pages 1-2) |
| c-di-GMP | binds/activates | PelD | *P. aeruginosa* / Pel-producing Proteobacteria | Strong but taxon-specific; primary and review support (wang2023biofilmformationmechanistic pages 10-11, whitfield2020pelpolysaccharidebiosynthesis pages 1-2) |
| PelD-PelE-PelF-PelG inner-membrane complex | synthesizes/transports | Pel polysaccharide | *P. aeruginosa* / diverse Proteobacteria with pelDEFG | Strong primary evidence; taxon-specific apparatus (whitfield2020pelpolysaccharidebiosynthesis pages 1-2) |
| Pel and Psl polysaccharides | promote | irreversible attachment / early surface adhesion | *P. aeruginosa* | Strong within *Pseudomonas*; not universally generalizable (yaeger2024ageneticscreen pages 1-2) |
| carbon starvation or nitric oxide signaling | activates/increases | PDE activity, lowering c-di-GMP and promoting dispersal | *P. aeruginosa* | Moderate to strong, taxon-specific; drawn from mechanistic review synthesis and should be curated with scope notes (wang2023biofilmformationmechanistic pages 10-11) |
| sub-MIC antibiotics via OprF/SigX-linked periplasmic redox response | elevates | c-di-GMP | *P. aeruginosa* laboratory biofilm assays | Strong primary evidence, taxon- and condition-specific (yaeger2024ageneticscreen pages 1-2) |
| elevated c-di-GMP after sub-MIC antibiotic exposure | promotes | biofilm formation | *P. aeruginosa* laboratory biofilm assays | Strong primary evidence, assay-specific (yaeger2024ageneticscreen pages 1-2) |
| oxygen gradient at high cell density | drives | localization to the air-liquid interface | *Bacillus subtilis* pellicle biofilms | Moderate to strong; review of primary pellicle literature, taxon- and habitat-specific (kovacs2019evolvedbiofilmreview pages 1-3) |
| Spo0A activation / threshold phosphorylation | derepresses | epsA-O and tapA-sipW-tasA matrix operons | *Bacillus subtilis* | Moderate to strong, taxon-specific, review-derived pathway summary (kovacs2019evolvedbiofilmreview pages 1-3) |
| de-repression of epsA-O and tapA-sipW-tasA | promotes | EPS/TasA matrix production and pellicle biofilm formation | *Bacillus subtilis* | Moderate to strong, taxon-specific, review-derived (kovacs2019evolvedbiofilmreview pages 1-3) |
| extracellular DNA (eDNA) | supports | mature biofilm structural integrity | broad bacterial biofilms; especially discussed in *P. aeruginosa* | Strong broad review support; precise mechanism can vary by taxon (bohning2024theroleof pages 1-2, yaeger2024ageneticscreen pages 1-2) |
| eDNA | binds/retains | phenazines such as pyocyanin | *P. aeruginosa* biofilms | Strong primary evidence; taxon-specific functional edge (saunders2020extracellulardnapromotes pages 1-3) |
| eDNA-phenazine interaction | promotes | efficient extracellular electron transfer | *P. aeruginosa* biofilms | Strong primary evidence; specialized functional module, not core to all biofilms (saunders2020extracellulardnapromotes pages 1-3) |
| quorum sensing | promotes/regulates | biofilm maturation and matrix-associated behaviors | many bacteria; details differ strongly by taxon | Moderate, broad but heterogeneous; review-only unless broken into taxon-specific circuits (sahoo2024biofilmformationin pages 2-3, bancucerzan2025persistentthreatsa pages 2-4) |
| LasI/LasR and RhlI/RhlR circuits | regulate | maturation/architecture/dispersal-associated functions | *P. aeruginosa* | Moderate, taxon-specific, review-only in current evidence set (bancucerzan2025persistentthreatsa pages 2-4) |


*Table: This table summarizes the strongest curation-ready causal edges for biofilm formation across conserved, Pseudomonas-specific, Bacillus-specific, and specialized eDNA-mediated mechanisms. It is designed to help prioritize high-confidence TraitMech nodes and edges while flagging taxon-specific and review-only claims.*

A more curation-oriented rendering, including source snippets, follows. Quotation marks contain concise text taken directly or nearly directly from the retrieved source passage; explanatory notes delimit the claim.

| # | Subject–predicate–object | Reference and supporting snippet | Curation note |
|---:|---|---|---|
| 1 | GGDEF-domain DGC — **synthesizes** → c-di-GMP | Park & Sauer: DGCs with GG(D/E)EF motifs produce c-di-GMP from GTP (2022; DOI [10.1007/978-3-031-08491-1_3](https://doi.org/10.1007/978-3-031-08491-1_3)) (park2022controllingbiofilmdevelopment pages 1-2) | **Strong core edge.** Conserved in many, but not all, bacterial clades. |
| 2 | EAL/HD-GYP PDE — **degrades** → c-di-GMP | Park & Sauer describe degradation by PDEs with EAL-like motifs or HD-GYP domains (park2022controllingbiofilmdevelopment pages 1-2). | **Strong core edge.** Enzyme-family annotation should precede species-specific gene assignment. |
| 3 | increased c-di-GMP — **promotes** → sessile biofilm state | “High c-di-GMP levels correlate with sessile biofilm lifestyle while low levels promote motility”; wild-type *P. aeruginosa* biofilms contained 75–78 pmol mg⁻¹ versus 33 ± 2 pmol mg⁻¹ in attachment-arrested Δ*sagS* cells (park2022controllingbiofilmdevelopment pages 7-9). | **Strong direction, quantitative but taxon/assay-specific.** Do not encode the concentrations as universal thresholds. |
| 4 | increased c-di-GMP — **inhibits** → motility | Biofilms contained approximately 75–110 pmol mg⁻¹ versus <30 pmol mg⁻¹ in planktonic *P. aeruginosa*, with high levels favoring formation and low levels motility (2016; DOI [10.1074/jbc.R115.711507](https://doi.org/10.1074/jbc.R115.711507)) (valentini2016biofilmsandcyclic pages 1-2). | **Strong broad trend**, but local signaling can make individual DGC/PDE phenotypes non-additive. |
| 5 | EPS secretion/organization — **promotes** → maturation and structural integrity | “During the maturation stage, bacterial cells secrete extracellular polymeric substances … forming an extracellular matrix … that surrounds bacterial cells and scaffolds the biofilm” (published 15 February 2024; DOI [10.1042/BCJ20210301](https://doi.org/10.1042/BCJ20210301)) (bohning2024theroleof pages 1-2). | **Strong core edge.** Prefer matrix production/organization over any single polymer as the universal node. |
| 6 | flagella and type-IV pili — **promote** → reversible attachment | In *P. aeruginosa*, “reversible attachment is mediated by flagella and pili at the cell pole” (published March 2024; DOI [10.1038/s41522-024-00496-7](https://doi.org/10.1038/s41522-024-00496-7)) (yaeger2024ageneticscreen pages 1-2). | **Taxon-specific primary-study background.** Motility structures can have different roles in other organisms. |
| 7 | Pel/Psl — **promote** → irreversible attachment | Increased c-di-GMP accompanies longitudinal, irreversible attachment “via Psl or Pel polysaccharides acting as adhesins”; both also support early attachment and mature structure (yaeger2024ageneticscreen pages 1-2). | **Strong for *P. aeruginosa*.** Keep Pel and Psl as parallel, partially redundant paths. |
| 8 | c-di-GMP — **binds/activates** → PelD-dependent Pel production | Mutations abolishing c-di-GMP binding to PelD did not disrupt complex assembly, “suggesting that c-di-GMP binding stimulates Pel production through quaternary structural rearrangements” (published 26 March 2020; DOI [10.1128/JB.00684-19](https://doi.org/10.1128/JB.00684-19)) (whitfield2020pelpolysaccharidebiosynthesis pages 1-2). | **Strong but precise:** binding regulates activity, not assembly of the PelDEFG complex. |
| 9 | PelD–PelE–PelF–PelG complex — **polymerizes/transports** → Pel | The study demonstrates an inner-membrane complex and proposes it as the Pel synthase “responsible for Pel polymerization and transport across the cytoplasmic membrane” (whitfield2020pelpolysaccharidebiosynthesis pages 1-2). | **Strong primary evidence**, scoped to Pel-producing Proteobacteria. PelF is the glycosyltransferase component. |
| 10 | Pel and eDNA interaction — **promotes** → mature-biofilm structural integrity | “Interactions between eDNA and Pel polysaccharide provide structural integrity” in mature *P. aeruginosa* biofilms (yaeger2024ageneticscreen pages 1-2). | **Strong taxon-specific edge.** Avoid generalizing the Pel interaction to organisms lacking Pel. |
| 11 | sub-MIC antibiotics — **promote** → *P. aeruginosa* biofilm formation | Multiple antibiotic classes at sub-MIC “induce biofilm formation”; the response required OprF, SigX, DsbA, and PA2200-associated signaling (yaeger2024ageneticscreen pages 1-2). | **Strong but assay-specific.** Sub-MIC exposure is not a universal enhancer; dose, drug, medium, strain, and endpoint matter. |
| 12 | OprF-linked periplasmic redox response — **increases** → c-di-GMP-responsive signaling | A c-di-GMP-responsive promoter was activated after sub-MIC treatment in wild type but not an *oprF* mutant; authors conclude that periplasmic redox changes elevate biofilm formation through increased c-di-GMP (yaeger2024ageneticscreen pages 1-2). | **Promising 2024 edge; mark `uncertain` at fine mechanistic resolution.** PA2200 is predicted to be a PDE, and the exact signal-transduction sequence remains incomplete. |
| 13 | carbon starvation / nitric-oxide signaling — **increases** → PDE activity | The 2023 review reports that these cues induce PDE activity and decrease intracellular c-di-GMP (DOI [10.1186/s43556-023-00164-w](https://doi.org/10.1186/s43556-023-00164-w)) (wang2023biofilmformationmechanistic pages 10-11). | **Moderate, review-derived, *P. aeruginosa*-focused.** Split carbon starvation and nitric oxide into separate edges when primary citations are curated. |
| 14 | decreased c-di-GMP — **promotes** → biofilm dispersal | The same synthesis connects cue-induced PDE activity, reduced c-di-GMP, and dispersal (wang2023biofilmformationmechanistic pages 10-11). | **Strong general direction; specific cue-response systems are taxon dependent.** |
| 15 | quorum sensing — **regulates/promotes** → maturation and matrix-associated behavior | A 2024 review defines QS as density-dependent extracellular signaling that collectively modifies biofilm and virulence behavior (DOI [10.3390/antibiotics13070623](https://doi.org/10.3390/antibiotics13070623)) (mishra2024medicaldeviceassociatedinfections pages 1-2). | **Do not curate as an unconditional universal positive edge.** QS can be stage-, species-, signal-, and condition-dependent. |
| 16 | LasI/LasR — **promotes/regulates** → *P. aeruginosa* maturation/virulence program | Review evidence identifies LasI-produced 3OC12-HSL binding LasR and regulating maturation-associated and virulence genes (bancucerzan2025persistentthreatsa pages 2-4). | **Uncertain for TraitMech until primary evidence is attached.** Avoid the stronger claim “QS is required for biofilm formation.” |
| 17 | RhlI/RhlR — **regulates** → rhamnolipid production and architecture/dispersal | Review synthesis connects the Rhl circuit to rhamnolipids affecting architecture and dispersal (bancucerzan2025persistentthreatsa pages 2-4). | **Taxon-specific and review-only in the present evidence set.** |
| 18 | oxygen gradient — **promotes** → *B. subtilis* localization at air–liquid interface | “Pellicle lifestyle is stimulated by an oxygen gradient”; aerotaxis drives cells toward the oxygen-rich interface (2019; DOI [10.1016/j.jmb.2019.02.005](https://doi.org/10.1016/j.jmb.2019.02.005)) (kovacs2019evolvedbiofilmreview pages 1-3). | **Strong pellicle-model edge**, not a universal oxygen effect on all biofilms. |
| 19 | Spo0A phosphorylation threshold — **derepresses** → `epsA-O` and `tapA-sipW-tasA` | Matrix production depends on derepression of these operons; Spo0A reaching a phosphorylation threshold represses AbrB in the summarized pathway (kovacs2019evolvedbiofilmreview pages 1-3). | **Moderate–strong, *B. subtilis*-specific review evidence.** The complete Spo0A–AbrB/SinI–SinR architecture should be curated from primary studies before asserting every intermediate. |
| 20 | `epsA-O` / `tapA-sipW-tasA` expression — **promotes** → EPS/TasA matrix and pellicle formation | The operons encode enzymes for exopolysaccharide production and the amyloid fibre protein TasA (kovacs2019evolvedbiofilmreview pages 1-3). | **Strong taxon-specific module.** Keep EPS and TasA as complementary matrix branches. |
| 21 | eDNA — **binds/retains** → pyocyanin and other phenazines | “Retention of pyocyanin … in the biofilm matrix is facilitated by eDNA binding” (published 20 August 2020; DOI [10.1016/j.cell.2020.07.006](https://doi.org/10.1016/j.cell.2020.07.006)) (saunders2020extracellulardnapromotes pages 1-3). | **Strong specialized primary edge.** It concerns biofilm function, not formation per se. |
| 22 | eDNA–phenazine interaction — **promotes** → extracellular electron transfer | The interaction supports “an efficient redox cycle with rapid EET” in *P. aeruginosa* biofilms (saunders2020extracellulardnapromotes pages 1-3). | **Strong downstream functional edge** suitable for an optional metabolic-function branch, not the minimal causal core. |

## 4. Recommended YAML-level graph organization

### Minimal cross-taxon backbone

1. environmental/surface cue → reversible attachment;
2. reversible attachment → irreversible attachment;
3. DGC → c-di-GMP;
4. PDE ┤ c-di-GMP;
5. increased c-di-GMP → reduced motility;
6. increased c-di-GMP → adhesin/EPS production;
7. adhesin/EPS production → irreversible attachment;
8. EPS matrix production/organization → microcolony formation and maturation;
9. mature matrix-enclosed community → `traitmech:000053` realization;
10. reduced c-di-GMP → dispersal.

Use predicates such as `increases`, `decreases`, `promotes`, `inhibits`, `produces`, `binds`, `part_of`, and `enables`. Avoid ambiguous `causes` when the source shows only regulation or necessity in one assay.

### Scoped extensions

* ***P. aeruginosa*:** Pel/Psl/alginate, PelDEFG–PelD, flagella/type-IV pili, OprF/SigX/sub-MIC stress, Las/Rhl QS, nitric-oxide dispersal.
* ***B. subtilis*:** oxygen-gradient/aerotaxis, Spo0A–AbrB and SinI–SinR regulatory branches, `epsA-O`, `tapA-sipW-tasA`, TasA, pellicle formation.
* **Functional matrix branch:** eDNA–phenazine electron transfer, catalytic enzymes, ion capture, genetic exchange, and pollutant transformation.

## 5. Recent developments and expert interpretation (2023–2024)

1. **The matrix is now understood as active rather than merely structural.** A 2024 expert primer emphasizes migration, genetic exchange, ion capture, signaling, catalysis, and extracellular electron transport. It identifies applications in wastewater treatment, biofuel production, bioelectrochemical systems, pollutant degradation, and element cycling (goltermann2024microbialprimerthe pages 1-3).
2. **Molecular architecture is becoming experimentally resolvable.** Cryo-EM, structural modeling, and spatial imaging increasingly connect atomic structures of amyloid fibres and other polymers to whole-biofilm mechanics. The 2024 assessment nevertheless identifies lack of multiscale information as a major limitation (bohning2024theroleof pages 1-2).
3. **Environmental realism is a central research priority.** Modern models increasingly use additive manufacturing, synthetic biology, and bioengineering, but model choice must account for substrate chemistry, topography, shear, redox, nutrients, pH, and community composition (yang2024classicalandmodern pages 1-2).
4. **Stress-induced formation is mechanistically richer than passive cell lysis.** The 2024 OprF study found that exogenous eDNA or lysate did not reproduce antibiotic stimulation, supporting a coordinated redox/c-di-GMP response rather than a simple “lysis seeds matrix” explanation (yaeger2024ageneticscreen pages 1-2).
5. **Anti-biofilm translation remains stage-specific.** Current implementations include antifouling/antibacterial device coatings, matrix-degrading enzymes, quorum-quenching strategies, nanoparticles, biosurfactants, and dispersal-inducing approaches. Preventing initial adhesion and eradicating an established matrix are distinct engineering objectives (shineh2023biofilmformationand pages 1-2, mishra2024medicaldeviceassociatedinfections pages 1-2).

## 6. Applications and recent quantitative context

* **Clinical devices:** Biofilms colonize catheters, stents, orthopedic and dental implants, contact lenses, and water lines. A 2023 review reports dialysis-catheter bloodstream-infection rates of **3.8–5.5 per 1,000 catheter-days**, versus **2.5–4 per 1,000 catheter-days** for non-dialysis catheters; these are device-infection figures, not proof that every case is biofilm-mediated (shineh2023biofilmformationand pages 1-2).
* **Healthcare burden:** A 2024 review reports that bacterial pathogens account for up to **70% of nosocomial infections in ICU patients** and cites roughly **40,000 deaths annually worldwide from healthcare-associated infections**. These values describe HAIs broadly and must not be relabeled as biofilm-specific mortality (mishra2024medicaldeviceassociatedinfections pages 1-2).
* **Tolerance:** The 2024 structural review states that matrix-associated growth can raise antibiotic tolerance by **up to 1,000-fold**; another 2024 device review gives a broader **500–5,000-fold** comparison for sessile versus planktonic cells. Such maxima vary by organism, agent, assay, and physiological state and should remain report-level context, not graph attributes (mishra2024medicaldeviceassociatedinfections pages 1-2, bohning2024theroleof pages 1-2).
* **Environmental biotechnology:** Biofilms drive wastewater transformations, anaerobic digestion, carbon/nitrogen cycling, microbial fuel-cell electron transfer, and bioremediation. Matrix-associated cytochromes, conductive pili, eDNA, phenazines, and enzymes enable extracellular catalysis and respiration (goltermann2024microbialprimerthe pages 1-3, saunders2020extracellulardnapromotes pages 1-3).
* **Industrial control:** Real implementations include antifouling coatings, alternating biocides, enzymatic matrix disruption, and biosurfactant biodispersants in water systems. Biofilms also cause food-plant persistence, pipeline biofouling, ship-hull fouling, and microbially influenced corrosion (shineh2023biofilmformationand pages 1-2, goltermann2024microbialprimerthe pages 1-3).

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not require a solid surface.** Non-attached matrix-embedded aggregates are recognized biofilms (goltermann2024microbialprimerthe pages 1-3).
2. **Do not encode “quorum sensing → biofilm formation” as universally positive or necessary.** Curate individual signal/receptor circuits with taxon, strain, medium, and stage.
3. **Do not universalize Pel, Psl, alginate, Las/Rhl, Spo0A, SinR, TasA, or curli.** They are lineage-specific realizations of broader matrix/signaling functions.
4. **Do not treat alginate as the universal *P. aeruginosa* matrix.** Pel and Psl dominate many non-mucoid isolates, whereas alginate is especially associated with mucoid chronic-infection variants (whitfield2020pelpolysaccharidebiosynthesis pages 1-2, yaeger2024ageneticscreen pages 1-2).
5. **Do not infer causality from crystal-violet biomass alone.** It conflates attached cells and matrix and does not establish architecture, viability, or maturation.
6. **Keep sub-MIC antibiotic stimulation assay-specific.** It is well supported in the 2024 *P. aeruginosa* system, but it is not a general rule for every antibiotic or organism (yaeger2024ageneticscreen pages 1-2).
7. **Mark the detailed OprF–DsbA–PA2200 signaling order uncertain.** Genetic necessity and a c-di-GMP-responsive output are demonstrated, but the complete biochemical chain remains unresolved.
8. **Do not curate the full Spo0A→SinI→SinR chain from the current excerpt alone.** The retrieved source directly supports Spo0A-threshold/AbrB regulation and matrix-operon derepression; primary SinI/SinR experiments should be added before committing every intermediate (kovacs2019evolvedbiofilmreview pages 1-3).
9. **Do not make antimicrobial tolerance part of the trait definition.** It is an emergent and variable consequence.
10. **Do not use “biofilm-associated infections constitute 80% of infections” as a graph fact.** Such frequently repeated estimates depend on definitions and attribution methods and were not supported here by a sufficiently authoritative current primary dataset.

## 8. DOI-first bibliography

1. Böhning J, Tarafder AK, Bharat TAM. “The role of filamentous matrix molecules in shaping the architecture and emergent properties of bacterial biofilms.” *Biochemical Journal*. **15 February 2024**. DOI: [10.1042/BCJ20210301](https://doi.org/10.1042/BCJ20210301) (bohning2024theroleof pages 1-2).
2. Goltermann L, Shahryari S, Rybtke M, Tolker-Nielsen T. “Microbial Primer: The catalytic biofilm matrix.” *Microbiology*. **30 August 2024**. DOI: [10.1099/mic.0.001497](https://doi.org/10.1099/mic.0.001497) (goltermann2024microbialprimerthe pages 1-3).
3. Yaeger LN et al. “A genetic screen identifies a role for oprF in Pseudomonas aeruginosa biofilm stimulation by subinhibitory antibiotics.” *npj Biofilms and Microbiomes*. **March 2024**. DOI: [10.1038/s41522-024-00496-7](https://doi.org/10.1038/s41522-024-00496-7) (yaeger2024ageneticscreen pages 1-2).
4. Yang Z et al. “Classical and Modern Models for Biofilm Studies: A Comprehensive Review.” *Antibiotics*. **18 December 2024**. DOI: [10.3390/antibiotics13121228](https://doi.org/10.3390/antibiotics13121228) (yang2024classicalandmodern pages 1-2).
5. Mishra A, Aggarwal A, Khan F. “Medical Device-Associated Infections Caused by Biofilm-Forming Microbial Pathogens and Controlling Strategies.” *Antibiotics*. **4 July 2024**. DOI: [10.3390/antibiotics13070623](https://doi.org/10.3390/antibiotics13070623) (mishra2024medicaldeviceassociatedinfections pages 1-2).
6. Wang X et al. “Biofilm formation: mechanistic insights and therapeutic targets.” *Molecular Biomedicine*. **December 2023**. DOI: [10.1186/s43556-023-00164-w](https://doi.org/10.1186/s43556-023-00164-w) (wang2023biofilmformationmechanistic pages 10-11).
7. Shineh G et al. “Biofilm Formation, and Related Impacts on Healthcare, Food Processing and Packaging, Industrial Manufacturing, Marine Industries, and Sanitation—A Review.” *Applied Microbiology*. **26 June 2023**. DOI: [10.3390/applmicrobiol3030044](https://doi.org/10.3390/applmicrobiol3030044) (shineh2023biofilmformationand pages 1-2).
8. Park S, Sauer K. “Controlling Biofilm Development Through Cyclic di-GMP Signaling.” *Advances in Experimental Medicine and Biology*. **2022**. DOI: [10.1007/978-3-031-08491-1_3](https://doi.org/10.1007/978-3-031-08491-1_3) (park2022controllingbiofilmdevelopment pages 1-2, park2022controllingbiofilmdevelopment pages 7-9).
9. Buzzo JR et al. “Z-form extracellular DNA is a structural component of the bacterial biofilm matrix.” *Cell*. **November 2021**. DOI: [10.1016/j.cell.2021.10.010](https://doi.org/10.1016/j.cell.2021.10.010).
10. Whitfield GB et al. “Pel Polysaccharide Biosynthesis Requires an Inner Membrane Complex Comprised of PelD, PelE, PelF, and PelG.” *Journal of Bacteriology*. **26 March 2020**. DOI: [10.1128/JB.00684-19](https://doi.org/10.1128/JB.00684-19) (whitfield2020pelpolysaccharidebiosynthesis pages 1-2).
11. Saunders SH et al. “Extracellular DNA Promotes Efficient Extracellular Electron Transfer by Pyocyanin in Pseudomonas aeruginosa Biofilms.” *Cell*. **20 August 2020**. DOI: [10.1016/j.cell.2020.07.006](https://doi.org/10.1016/j.cell.2020.07.006) (saunders2020extracellulardnapromotes pages 1-3).
12. Kovács ÁT, Dragoš A. “Evolved Biofilm: Review on the Experimental Evolution Studies of Bacillus subtilis Pellicles.” *Journal of Molecular Biology*. **2019**. DOI: [10.1016/j.jmb.2019.02.005](https://doi.org/10.1016/j.jmb.2019.02.005) (kovacs2019evolvedbiofilmreview pages 1-3).
13. Valentini M, Filloux A. “Biofilms and Cyclic di-GMP Signaling: Lessons from Pseudomonas aeruginosa and Other Bacteria.” *Journal of Biological Chemistry*. **June 2016**. DOI: [10.1074/jbc.R115.711507](https://doi.org/10.1074/jbc.R115.711507) (valentini2016biofilmsandcyclic pages 1-2).

**Curation conclusion:** the most defensible expansion of the existing 13-node/10-edge graph is a conserved c-di-GMP–motility–matrix–maturation–dispersal backbone, with separately scoped *P. aeruginosa* Pel/Psl and *B. subtilis* pellicle modules. Quorum sensing, antibiotic-stress sensing, and catalytic matrix functions should be secondary modules with explicit taxon, assay, and evidence qualifiers.

References

1. (goltermann2024microbialprimerthe pages 1-3): Lise Goltermann, Shahab Shahryari, Morten Rybtke, and Tim Tolker-Nielsen. Microbial primer: the catalytic biofilm matrix. Aug 2024. URL: https://doi.org/10.1099/mic.0.001497, doi:10.1099/mic.0.001497. This article has 8 citations and is from a peer-reviewed journal.

2. (bohning2024theroleof pages 1-2): Jan Böhning, Abul K. Tarafder, and Tanmay A.M. Bharat. The role of filamentous matrix molecules in shaping the architecture and emergent properties of bacterial biofilms. Biochemical Journal, 481:245-263, Feb 2024. URL: https://doi.org/10.1042/bcj20210301, doi:10.1042/bcj20210301. This article has 49 citations and is from a domain leading peer-reviewed journal.

3. (park2022controllingbiofilmdevelopment pages 1-2): Soyoung Park and Karin Sauer. Controlling biofilm development through cyclic di-gmp signaling. Advances in experimental medicine and biology, 1386:69-94, Jan 2022. URL: https://doi.org/10.1007/978-3-031-08491-1\_3, doi:10.1007/978-3-031-08491-1\_3. This article has 103 citations and is from a peer-reviewed journal.

4. (sahoo2024biofilmformationin pages 2-3): Kaushik Sahoo and Supriya Meshram. Biofilm formation in chronic infections: a comprehensive review of pathogenesis, clinical implications, and novel therapeutic approaches. Cureus, Oct 2024. URL: https://doi.org/10.7759/cureus.70629, doi:10.7759/cureus.70629. This article has 103 citations.

5. (kovacs2019evolvedbiofilmreview pages 1-3): Ákos T. Kovács and Anna Dragoš. Evolved biofilm: review on the experimental evolution studies of bacillus subtilis pellicles. Journal of Molecular Biology, 431:4749-4759, Nov 2019. URL: https://doi.org/10.1016/j.jmb.2019.02.005, doi:10.1016/j.jmb.2019.02.005. This article has 100 citations and is from a domain leading peer-reviewed journal.

6. (yang2024classicalandmodern pages 1-2): Zhihe Yang, Sadaf Aiman Khan, Laurence J. Walsh, Zyta M. Ziora, and Chaminda Jayampath Seneviratne. Classical and modern models for biofilm studies: a comprehensive review. Antibiotics, 13:1228, Dec 2024. URL: https://doi.org/10.3390/antibiotics13121228, doi:10.3390/antibiotics13121228. This article has 9 citations.

7. (valentini2016biofilmsandcyclic pages 1-2): Martina Valentini and Alain Filloux. Biofilms and cyclic di-gmp (c-di-gmp) signaling: lessons from pseudomonas aeruginosa and other bacteria. Journal of Biological Chemistry, 291:12547-12555, Jun 2016. URL: https://doi.org/10.1074/jbc.r115.711507, doi:10.1074/jbc.r115.711507. This article has 879 citations and is from a domain leading peer-reviewed journal.

8. (park2022controllingbiofilmdevelopment pages 7-9): Soyoung Park and Karin Sauer. Controlling biofilm development through cyclic di-gmp signaling. Advances in experimental medicine and biology, 1386:69-94, Jan 2022. URL: https://doi.org/10.1007/978-3-031-08491-1\_3, doi:10.1007/978-3-031-08491-1\_3. This article has 103 citations and is from a peer-reviewed journal.

9. (wang2023biofilmformationmechanistic pages 10-11): Xinyu Wang, Ming Liu, Chuanjiang Yu, Jing Li, and Xikun Zhou. Biofilm formation: mechanistic insights and therapeutic targets. Molecular Biomedicine, Dec 2023. URL: https://doi.org/10.1186/s43556-023-00164-w, doi:10.1186/s43556-023-00164-w. This article has 190 citations and is from a peer-reviewed journal.

10. (whitfield2020pelpolysaccharidebiosynthesis pages 1-2): Gregory B. Whitfield, Lindsey S. Marmont, Alex Ostaszewski, Jacquelyn D. Rich, John C. Whitney, Matthew R. Parsek, Joe J. Harrison, and P. Lynne Howell. Pel polysaccharide biosynthesis requires an inner membrane complex comprised of peld, pele, pelf, and pelg. Mar 2020. URL: https://doi.org/10.1128/jb.00684-19, doi:10.1128/jb.00684-19. This article has 73 citations and is from a peer-reviewed journal.

11. (yaeger2024ageneticscreen pages 1-2): Luke N. Yaeger, Michael R. M. Ranieri, Jessica Chee, Sawyer Karabelas-Pittman, Madeleine Rudolph, Alessio M. Giovannoni, Hanjeong Harvey, and Lori L. Burrows. A genetic screen identifies a role for oprf in pseudomonas aeruginosa biofilm stimulation by subinhibitory antibiotics. npj Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00496-7, doi:10.1038/s41522-024-00496-7. This article has 18 citations and is from a peer-reviewed journal.

12. (saunders2020extracellulardnapromotes pages 1-3): Scott H. Saunders, Edmund C.M. Tse, Matthew D. Yates, Fernanda Jiménez Otero, Scott A. Trammell, Eric D.A. Stemp, Jacqueline K. Barton, Leonard M. Tender, and Dianne K. Newman. Extracellular dna promotes efficient extracellular electron transfer by pyocyanin in pseudomonas aeruginosa biofilms. Cell, 182:919-932.e19, Aug 2020. URL: https://doi.org/10.1016/j.cell.2020.07.006, doi:10.1016/j.cell.2020.07.006. This article has 362 citations and is from a highest quality peer-reviewed journal.

13. (bancucerzan2025persistentthreatsa pages 2-4): Alexandra Ban-Cucerzan, K. Imre, A. Morar, Adela Marcu, I. Hotea, S. Popa, Răzvan-Tudor Pătrînjan, I. Bucur, Cristina Gașpar, Ana-Maria Plotuna, and Sergiu-Constantin Ban. Persistent threats: a comprehensive review of biofilm formation, control, and economic implications in food processing environments. Microorganisms, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081805, doi:10.3390/microorganisms13081805. This article has 47 citations.

14. (mishra2024medicaldeviceassociatedinfections pages 1-2): Akanksha Mishra, Ashish Aggarwal, and Fazlurrahman Khan. Medical device-associated infections caused by biofilm-forming microbial pathogens and controlling strategies. Antibiotics, 13:623, Jul 2024. URL: https://doi.org/10.3390/antibiotics13070623, doi:10.3390/antibiotics13070623. This article has 169 citations.

15. (shineh2023biofilmformationand pages 1-2): Ghazal Shineh, Mohammadmahdi Mobaraki, Mohammad Jabed Perves Bappy, and David K. Mills. Biofilm formation, and related impacts on healthcare, food processing and packaging, industrial manufacturing, marine industries, and sanitation–a review. Applied Microbiology, 3:629-665, Jun 2023. URL: https://doi.org/10.3390/applmicrobiol3030044, doi:10.3390/applmicrobiol3030044. This article has 209 citations.