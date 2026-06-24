---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:55:57.340896'
end_time: '2026-06-18T09:10:32.307483'
duration_seconds: 874.97
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: peritrichous
  trait_identifier: traitmech:000060
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: peritrichous
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagellar arrangement with flagella distributed over the entire cell
    surface rather than localized to the poles.
  parent_traits: traitmech:000056
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous
    (surface-distributed) flagellation as one of the conserved flagellation patterns.)
    | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar
    filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)'
  causal_graph_summary: 'peritrichous_surface_distributed_flagella: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** peritrichous
- **METPO identifier:** traitmech:000060
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella distributed over the entire cell surface rather than localized to the poles.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous (surface-distributed) flagellation as one of the conserved flagellation patterns.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)
- **Existing causal graph summary:** peritrichous_surface_distributed_flagella: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **peritrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/peritrichous.yaml`.

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
- **Trait label:** peritrichous
- **METPO identifier:** traitmech:000060
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagellar arrangement with flagella distributed over the entire cell surface rather than localized to the poles.
- **Parent traits:** traitmech:000056
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuv034:  (Schuhmacher et al. describe peritrichous (surface-distributed) flagellation as one of the conserved flagellation patterns.) | DOI:10.3390/biom9070279:  (Flagellum review supports multiple surface flagellar filaments as locomotory organelles, as in peritrichously flagellated enterobacteria.)
- **Existing causal graph summary:** peritrichous_surface_distributed_flagella: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **peritrichous** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/peritrichous.yaml`.

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


## Microbial TraitMech Curation Report: **peritrichous** (METPO: traitmech:000060)

### 1) Scope summary (trait meaning, boundaries, and observational context)

**Trait definition (curation-ready).** Peritrichous flagellation is a **flagellar arrangement** in which a cell has **multiple flagella distributed over/around the cell body**, rather than localized at one or both poles. This is explicitly defined in recent literature as “multiple flagella located uniformly across the cell body” / “evenly covering the cell body.” (thomasUnknownyearthedesignof pages 57-59, thomasUnknownyearthedesignof pages 55-57)

A 2024 applied biotechnology paper provides an explicit operational distinction used in practice: “flagella are located throughout the cell wall and are referred to as peritrichous,” contrasted with “polar flagella… located at one of the poles of the cell.” (frolov2024constructionofthe pages 1-2)

**Boundary cases / nearby traits to distinguish.**
- **Polar (monotrichous/lophotrichous/amphitrichous)** systems have flagella localized at one or both poles; these are contrasted against peritrichous arrangements in multiple sources. (frolov2024constructionofthe pages 1-2, thomasUnknownyearthedesignof pages 55-57)
- **Lateral flagella** are commonly described as flagella along the sides of cells and can be **conditionally expressed** (e.g., used for swarming), sometimes **co-existing with** a polar system; this is important to avoid conflating “peritrichous” with “lateral swarming system.” (thomasUnknownyearthedesignof pages 57-59, thomasUnknownyearthedesignof pages 55-57)
- **Periplasmic/endoflagella** (spirochetes) are sometimes excluded from “flagellar arrangement” taxonomies or treated as special cases; therefore, peritrichous (surface-distributed external filaments) should not be inferred from motility alone. (thomasUnknownyearthedesignof pages 57-59)

**Assay/measurement context (how this trait is observed).** In practice, peritrichous is typically assigned from microscopy/flagellar staining or EM/cryo-ET showing basal bodies/filaments distributed around the cell surface. Several studies also quantify *flagellar number per cell* and *fraction of flagellated cells* (which are related but distinct from arrangement). (alsenani2024manipulatingflagellargene pages 126-130, lisevich2025physicsofswimming pages 7-8)

### 2) Key concepts and current understanding (mechanistic overview)

Peritrichous arrangement is a **morphological pattern** emerging from (i) **where basal bodies are inserted** into the envelope and (ii) how assembly and cell-envelope remodeling constrain/enable insertion across the surface. Evidence across species supports a multi-layer model:

1. **Envelope/cell-wall constraints and assembly intermediates** can govern where a basal body can mature into a functional flagellum. In *Bacillus subtilis*, rod assembly and peptidoglycan (PG) constraints immobilize nascent basal bodies and are proposed to help establish a grid-like/peritrichous distribution. (dunn2025nascentflagellarbasal pages 6-9, dunn2025nascentflagellarbasal pages 1-2)
2. **Cytoplasmic patterning factors** (e.g., FlhF/FlhG family proteins) are widely implicated in controlling **flagellar number and placement**, though specific mechanisms can differ between **peritrichous** and **polar** bacteria; for example, polar systems can use FlhF anchoring to polar landmarks. (dornes2024polarconfinementof pages 1-2, rosinke2025characterizinghelicobacterpyloria pages 19-22)
3. **Hierarchical gene regulation** (master regulators, sigma factors, anti-sigma factors, secretion-coupled checkpoints) controls whether a cell builds flagella and how much it invests in flagellar biogenesis—affecting the *presence/abundance* of flagella (and thus the observable peritrichous phenotype if the species encodes a peritrichous program). (rosinke2025characterizinghelicobacterpylori pages 19-22, alsenani2024manipulatingflagellargene pages 126-130)

### 3) Candidate causal graph entities (grouped by type)

Below are candidate nodes (mechanistic entities) suitable for inclusion in `data/traits/morphology/peritrichous.yaml`. Grounding is suggested where stable IDs are available; otherwise, curate as label nodes and ground per taxon later.

#### A. Trait / phenotype nodes
- **peritrichous** (METPO: traitmech:000060)
- **flagellar localization** (concept node; “location relative to the cell body”) (rosinke2025characterizinghelicobacterpyloria pages 19-22)
- **hyperflagellation / hypoflagellation** (phenotype modifiers; affects number rather than arrangement) (rosinke2025characterizinghelicobacterpyloria pages 19-22)
- **flagellar filament number per cell** (quantitative phenotype) (lisevich2025physicsofswimming pages 7-8, alsenani2024manipulatingflagellargene pages 126-130)

#### B. Cellular structures / assemblies
- **flagellum** (basal body, rod, hook, filament; assembly modules)
- **basal body** (tracked via C-ring protein FliM in *B. subtilis*) (dunn2025nascentflagellarbasal pages 2-4)
- **rod** (including proximal rod; envelope transit through PG implicated in patterning) (dunn2025nascentflagellarbasal pages 6-9)
- **peptidoglycan (PG) layer** (constraint/“permissive holes” concept) (dunn2025nascentflagellarbasal pages 6-9, dunn2025nascentflagellarbasal pages 9-11)
- **MS-ring (FliF)**, **C-ring (FliG/FliM/FliN)** (assembly/interaction nodes; pole recruitment shown in polar system mechanism) (dornes2024polarconfinementof pages 1-2)

#### C. Genes / proteins / complexes (labels; ground to UniProt per taxon)
- **FlhF** (SRP-type GTPase; localization/pattern regulator) (dornes2024polarconfinementof pages 1-2, rosinke2025characterizinghelicobacterpyloria pages 19-22)
- **FlhG** (MinD/ParA-family ATPase; modulates FlhF; controls number/progression) (dornes2024polarconfinementof pages 1-2, rosinke2025characterizinghelicobacterpyloria pages 19-22)
- **HubP/FimV** (polar landmark in polar systems; anchoring partner for FlhF) (dornes2024polarconfinementof pages 1-2)
- **FliF, FliG, FliM, FliN** (ring proteins; interactions in placement/assembly) (dornes2024polarconfinementof pages 1-2, dunn2025nascentflagellarbasal pages 2-4)
- **FlgC** (proximal rod subunit; affects basal-body immobilization/mobility) (dunn2025nascentflagellarbasal pages 6-9)
- **FlhA** (flagellar export/T3SS component; used as deletion target in fermentation engineering) (frolov2024constructionofthe pages 4-5)
- **FlhDC** (master regulator in enteric peritrichous bacteria; mutation abolishes motility and FlgE expression in UPEC) (alsenani2024manipulatingflagellargene pages 126-130)
- **FliA (σ28)** and **FlgM (anti-σ28)** (late gene control) (rosinke2025characterizinghelicobacterpylori pages 19-22)
- **RpoN (σ54), RpoD (σ70)**; **FlgS/FlgR** two-component system (RpoN regulon activation, as summarized) (rosinke2025characterizinghelicobacterpylori pages 19-22)
- **ClpP** (protease; deletion associated with increased flagella in UPEC isolates) (alsenani2024manipulatingflagellargene pages 126-130)

#### D. Environmental / experimental factors
- **carbon limitation / growth rate** (motility inversely correlates with growth rate under carbon limitation in *E. coli*) (lisevich2025physicsofswimming pages 1-2)
- **porous/semi-solid media; surface growth** (affects observed motility fraction of swimmers in isolates) (lisevich2025physicsofswimming pages 7-8)
- **magnetic guidance; hypoxia (tumor microenvironment)** for biohybrid microrobot applications (zhang2024biohybridmagneticrobots pages 11-13, zhang2024biohybridmagneticrobots pages 10-11)

#### E. Processes (suggested GO grounding)
Label nodes suitable for GO mapping during curation:
- **flagellum-dependent cell motility** (GO term suggested)
- **bacterial-type flagellum assembly** (GO term suggested)
- **chemotaxis** (GO term suggested)
- **protein secretion by type III secretion system** (GO term suggested; note: flagellar T3SS is a specialized T3SS)

### 4) Candidate causal edges (evidence-backed triples)

The following table is designed for direct TraitMech curation decisions.

| Subject (node) | Predicate | Object (node) | Evidence snippet (quote) | Reference (authors, year, DOI/URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| peritrichous flagellar arrangement | defined_as | flagella distributed over the cell surface | “Multiple flagella located uniformly across the cell body” and peritrichous flagella “evenly cover[] the cell body” (thomasUnknownyearthedesignof pages 57-59, thomasUnknownyearthedesignof pages 55-57) | Thomas, year not stated, review on flagellar diversity; Frolov et al., 2024, https://doi.org/10.3390/fermentation10120606 | Scope/definition edge; morphology trait, not itself a mechanism. |
| peritrichous flagellar arrangement | distinguished_from | polar flagellar arrangement | “The flagellar systems of Pseudomonas… are located at one of the poles of the cell” versus peritrichous flagella “located throughout the cell wall” (frolov2024constructionofthe pages 1-2) | Frolov et al., 2024, https://doi.org/10.3390/fermentation10120606 | Good boundary-case edge for curation. |
| flagellar rod assembly | immobilizes | nascent basal bodies | “We infer that rod synthesis immobilizes basal bodies due to spatial constraints imposed by insertion through cell wall PG.” (dunn2025nascentflagellarbasal pages 6-9) | Dunn et al., 2025, https://doi.org/10.1128/mbio.00530-25 | Strong mechanistic evidence, but species-specific to *Bacillus subtilis*; may support a peritrichous-patterning subgraph rather than universal peritrichous trait. |
| proximal rod subunit FlgC | promotes | basal body immobilization | “its incorporation increases the fraction of, and decreases the time to, basal body immobilization” (dunn2025nascentflagellarbasal pages 6-9) | Dunn et al., 2025, https://doi.org/10.1128/mbio.00530-25 | Mechanistic and specific. Candidate node: FlgC. |
| FlgC mutation | increases | basal body mobility | “mutating it significantly increased the fraction of mobile basal bodies” and proximal rod mutation raised mobile basal bodies to “approximately 20% at steady state” (dunn2025nascentflagellarbasal pages 6-9, dunn2025nascentflagellarbasal pages 4-6) | Dunn et al., 2025, https://doi.org/10.1128/mbio.00530-25 | Species-specific quantitative edge in *B. subtilis*. |
| rod assembly defects | disrupt | grid-like/peritrichous basal body patterning | “defects in the flagellar rod lead to a more-random distribution of flagella and an increase in polar basal bodies” (dunn2025nascentflagellarbasal pages 1-2) | Dunn et al., 2025, https://doi.org/10.1128/mbio.00530-25 | Supports rod→patterning edge; useful but 2025 source. |
| FlhF | recruits | FliF–FliG complex to the pole | “FlhF anchors developing flagellar structures to the polar landmark HubP/FimV… FlhF-bound FliG subsequently engages with the MS-ring protein FliF… recruit[ing] a functional FliF/FliG complex to the pole” (dornes2024polarconfinementof pages 1-2) | Dornes et al., 2024, https://doi.org/10.1038/s41467-024-50274-4 | Direct mechanism, but demonstrated for polar systems; use cautiously for peritrichous trait except as a comparative/regulatory node. |
| FlhF GTPase domain | interacts_with | HubP/FimV polar landmark | “the GTPase domain of FlhF interacts with HubP” (dornes2024polarconfinementof pages 1-2) | Dornes et al., 2024, https://doi.org/10.1038/s41467-024-50274-4 | Comparative flagellation-pattern mechanism; likely not directly curatable for peritrichous unless trait graph includes exclusion/comparison edges. |
| FlhF N-terminal/B-domain | binds | FliG | “an as-yet-uncharacterized structured domain at the N-terminus of FlhF binds to FliG” (dornes2024polarconfinementof pages 1-2) | Dornes et al., 2024, https://doi.org/10.1038/s41467-024-50274-4 | Same caution as above. |
| FlhG | modulates | progression of flagellar assembly | “FlhG’s modulation of FlhF controls FliG’s interaction with FliM/FliN, thereby regulating the progression of flagellar assembly” (dornes2024polarconfinementof pages 1-2) | Dornes et al., 2024, https://doi.org/10.1038/s41467-024-50274-4 | Strong for placement/number control generally; direct evidence from polar system. |
| FlhF/FlhG | regulate | flagellar number and placement | “FlhF… and FlhG… are central determinants” and deletion of flhG causes “hyperflagellation” while flhF mutation can cause aflagellation/mislocalization (rosinke2025characterizinghelicobacterpylori pages 19-22, rosinke2025characterizinghelicobacterpyloria pages 19-22) | Rosinke, 2025; Botting, 2023 | Broad expert-summary edge; mixed taxa and partly review-level evidence. Mark as general/inferred. |
| flagellar T3SS assembly | required_for | RpoN-dependent flagellar gene expression | “Assembly of the flagellar-type III secretion system (f-T3SS) is reported to be required for expression of RpoN-dependent genes” (rosinke2025characterizinghelicobacterpylori pages 19-22) | Rosinke, 2025 | Review-style statement; DOI not available from retrieved metadata. Candidate edge for assembly-regulation subgraph, uncertain pending primary-source confirmation. |
| FlgM | inhibits | FliA (σ28) | “Late-gene sigma FliA is negatively regulated by anti-sigma FlgM” (rosinke2025characterizinghelicobacterpylori pages 19-22) | Rosinke, 2025 | Canonical regulatory edge; from review summary here. |
| carbon limitation | inversely_correlates_with | motility as growth rate rises | “during carbon-limited growth motility remains below maximal levels and inversely correlates with the growth rate” (lisevich2025physicsofswimming pages 1-2) | Lisevich et al., 2025, https://doi.org/10.1038/s41467-025-56980-x | Environmental-factor edge in peritrichous *E. coli*; functional, not patterning-specific. |
| flagellar filament number (~5) | saturates | swimming velocity in *E. coli* | “swimming velocity increases with flagellar-gene expression only up to a critical filament number of ~5 flagella… above this the swimming velocity saturates” (lisevich2025physicsofswimming pages 7-8) | Lisevich et al., 2025, https://doi.org/10.1038/s41467-025-56980-x | Useful quantitative phenotype edge for peritrichous flagellum function. |
| clpP deletion | increases | flagella number per cell | “Deleting clpP induced synthesis of up to seven flagella per cell… clpP mutants overall had >70% flagellated populations with an average >2.4 flagella per cell” (alsenani2024manipulatingflagellargene pages 126-130) | Alsenani, 2024 | UPEC/*E. coli* strain-specific regulatory edge; mechanism to peritrichous abundance rather than arrangement. |
| flhDC mutation | abolishes | motility / flagellation | “Motility assays… showed flhDC mutants lost motility” and “All flhDC mutants lacked FlgE expression” (alsenani2024manipulatingflagellargene pages 126-130) | Alsenani, 2024 | Strong strain-level support in UPEC; ties master regulator to flagellar biogenesis. |
| porous or surface growth conditions | increase | fraction of swimmers in natural *E. coli* isolates | “many natural ECOR isolates spread only on porous/semi-solid media… or show increased motility after surface growth… mainly due to a higher fraction of swimmers rather than higher single-cell velocities” (lisevich2025physicsofswimming pages 7-8) | Lisevich et al., 2025, https://doi.org/10.1038/s41467-025-56980-x | Environmental/assay-specific edge; useful for assay context. |
| flhA deletion (in engineered fermentation strain) | reduces | motility and biofilm formation | “absence of these genes reduces mobility and biofilm formation (40% lower after 72 h) in the mutant” (frolov2024constructionofthe pages 1-2) | Frolov et al., 2024, https://doi.org/10.3390/fermentation10120606 | Applied/engineering edge in *Pseudomonas putida*; not a peritrichous organism, so use only as application evidence, not direct trait mechanism. |
| flhA/pilQ/algA deletion strain LN6160 | increases | growth yield / CFU in fermentation | “1.39 × 10^10 CFU/mL in the mutant and 6.4 × 10^9 CFU/mL in the wild type” and in mineral medium “6.11 × 10^9 CFU/mL… and 1.36 × 10^9 CFU/mL” (frolov2024constructionofthe pages 8-10) | Frolov et al., 2024, https://doi.org/10.3390/fermentation10120606 | Application edge showing tradeoff between motility and production fitness. |
| peritrichously flagellated *E. coli* | enables | bio-hybrid microrobot propulsion / targeted delivery | “Escherichia coli — described as possessing multiple peritrichous flagella — … can be bio-engineered into microrobots for noninvasive targeted delivery in physiological environments” (zhang2024biohybridmagneticrobots pages 10-11) | Zhang et al., 2024, https://doi.org/10.3390/bioengineering11040311 | Real-world implementation edge; application-focused, not causal for trait origin. |
| engineered *E. coli* bio-hybrids | deliver | therapeutic payloads to tumors | “EcN… modified into self-propelled robots to deliver therapeutic payloads” with “triple-perception (magnetic, thermal, hypoxic)” and cargoes including DOX/ICG (zhang2024biohybridmagneticrobots pages 11-13, zhang2024biohybridmagneticrobots pages 13-15) | Zhang et al., 2024, https://doi.org/10.3390/bioengineering11040311 | High-value application evidence. Review/schematic examples; not all implementations are clinical. |


*Table: This table compiles candidate subject-predicate-object edges relevant to the peritrichous trait, with direct evidence snippets, citations, and curation notes. It is useful for deciding which claims are robust enough for TraitMech curation and which remain comparative, taxon-specific, or application-only.*

### 5) Recent developments and latest research (prioritize 2023–2024)

#### 5.1 Spatial confinement and pattern control via FlhF/FlhG (2024)
A key 2024 advance is a mechanistic dissection of **how FlhF restricts flagellar assembly to a pole** in a bacterium with dual flagellar systems. The study shows domain-resolved interactions: FlhF’s GTPase domain binds a polar landmark (HubP/FimV) and its N-terminal domain binds FliG; this recruits a FliF/FliG complex to the pole. FlhG modulates FlhF and influences progression of assembly through controlling FliG interactions with downstream C-ring proteins. (dornes2024polarconfinementof pages 1-2)

**Curation implication:** FlhF/FlhG are **flagellation-pattern regulators**, but the **exact edge direction and targets are context-dependent** (polar vs peritrichous). For peritrichous graphs, it may be appropriate to represent these as higher-level conserved regulators of “flagellar placement/number,” and then attach peritrichous-specific downstream mechanisms (e.g., PG/rod probing in *B. subtilis*) as taxon-specific subgraphs. (dornes2024polarconfinementof pages 1-2, dunn2025nascentflagellarbasal pages 6-9)

#### 5.2 Applied implementation: bio-hybrid magnetic microrobots using peritrichous *E. coli* (2024)
A 2024 mini-review synthesizes recent work where **peritrichously flagellated *E. coli*** (including probiotic strain **Nissle 1917/EcN**) is used as a **self-propelled chassis** in bio-hybrid robots for targeted therapy; it explicitly notes *E. coli* with multiple peritrichous flagella can be engineered into microrobots for targeted delivery. (zhang2024biohybridmagneticrobots pages 10-11)

The same review describes concrete designs (reviewed/cited examples) such as *E. coli* conjugated with magnetic nanoparticles and drug payloads (e.g., DOX and ICG), and “triple-perception” (magnetic, thermal, hypoxic) approaches to tumor targeting under magnetic guidance. (zhang2024biohybridmagneticrobots pages 11-13, zhang2024biohybridmagneticrobots pages 13-15)

#### 5.3 Real-world bioprocess engineering: reducing motility/biofilm in fermentation strains (2024)
A 2024 fermentation-focused study engineered **Pseudomonas putida** strains with deletions including **flhA** (flagellar export) and **pilQ** (pili) and reported reduced motility and reduced biofilm formation (reported as 40% lower after 72 h for the mutant). It also reported higher CFU yields in mutant vs wild type under both rich and mineral media (e.g., 1.39×10^10 vs 6.4×10^9 CFU/mL in rich medium after one day; 6.11×10^9 vs 1.36×10^9 CFU/mL in mineral medium after 24 h). (frolov2024constructionofthe pages 1-2, frolov2024constructionofthe pages 8-10)

**Curation implication:** This is not a peritrichous pattern mechanism (Pseudomonas is typically polar-flagellated), but it is important for “applications/real-world implementations” of flagellar engineering and illustrates causal links between removing flagellar assembly/export functions and reduced surface colonization/foaming/biofilm outcomes in bioreactors. (frolov2024constructionofthe pages 1-2, frolov2024constructionofthe pages 8-10)

### 6) Relevant quantitative statistics & data points (recent studies)

- **Critical flagella number for swimming in peritrichous *E. coli*.** In a quantitative study of motility investment, swimming velocity increased with flagellar gene expression only up to a **critical filament number of ~5 flagella**, after which velocity saturated. (lisevich2025physicsofswimming pages 7-8)
- **Motility vs physiology.** Under carbon-limited growth, motility remained below maximal levels and **inversely correlated with growth rate**, linking environment/physiology to motility investment. (lisevich2025physicsofswimming pages 1-2)
- **Clinical isolate variation and genetic perturbations (UPEC).** In UPEC isolates and mutants, clpP deletion was associated with higher flagellar counts: up to **7 flagella per cell**, with **>70%** of the population flagellated and average **>2.4 flagella per cell**; by contrast, many wild-type uro-associated strains had high fractions of non-flagellated or 1–2-flagella cells. flhDC mutants lost motility and lacked FlgE expression. (alsenani2024manipulatingflagellargene pages 126-130)
- **Patterning-linked cell-envelope mechanics (B. subtilis; 2025 but mechanistically central).** Rod/PG interactions immobilize basal bodies; proximal rod mutation increased mobile basal bodies to ~**20% at steady state**, compared with ~**5%** mobile in wild type tracking experiments (as reported in the excerpt), supporting a diffusion-and-capture model that can generate non-random/peritrichous patterns. (dunn2025nascentflagellarbasal pages 6-9, dunn2025nascentflagellarbasal pages 2-4)

### 7) Expert opinions / authoritative interpretations (with curation guidance)

- Reviews and syntheses treat **flagellar number and localization (“flagellation pattern”)** as species-specific, early taxonomic criteria, and widely attribute control to conserved regulators such as FlhF/FlhG families—yet the mechanistic implementation differs across taxa and must be curated with taxon context. (dornes2024polarconfinementof pages 1-2, rosinke2025characterizinghelicobacterpyloria pages 19-22)
- A key mechanistic interpretation for peritrichous *B. subtilis* is that patterning is **different from polar targeting** and may instead involve **rod polymerization probing PG superstructure**; this is important as a “do not overgeneralize” warning when building a general peritrichous TraitMech graph. (dunn2025nascentflagellarbasal pages 1-2, dunn2025nascentflagellarbasal pages 6-9)

### 8) Warnings / claims not ready (or only conditionally ready) for TraitMech curation

1. **Do not directly transfer polar-localization mechanisms into the peritrichous graph** without taxon scoping. The FlhF–HubP/FimV anchoring mechanism is demonstrated for polar confinement (2024) and should be represented either as (i) a comparative/exclusion edge or (ii) a separate “polar flagellation patterning” module, not as a universal peritrichous mechanism. (dornes2024polarconfinementof pages 1-2)
2. **Regulatory hierarchy edges from non-DOI or review-like sources** (e.g., “f-T3SS assembly required for RpoN-dependent gene expression,” “FlgM inhibits FliA”) are canonical and likely true, but in this retrieval set they appear in a review/thesis-style source without strong primary anchoring in the extracted snippet; for TraitMech, these should be marked **uncertain** until backed by primary, DOI-indexed sources for the target taxa. (rosinke2025characterizinghelicobacterpylori pages 19-22)
3. **Patterning mechanism (rod/PG probing) is species-specific evidence** (currently strongest in *B. subtilis*), and should be curated with **NCBITaxon constraints** if included. (dunn2025nascentflagellarbasal pages 6-9)
4. **Motility/flagellar number ≠ peritrichous arrangement.** Many quantitative datasets measure number, filament length, or fraction of swimmers; these are best represented as downstream phenotype modifiers rather than defining arrangement. (lisevich2025physicsofswimming pages 7-8, alsenani2024manipulatingflagellargene pages 126-130)

---

## DOI-first bibliography (with publication dates and URLs where available)

1. **Dornes A. et al.** *Polar confinement of a macromolecular machine by an SRP-type GTPase.* **Nature Communications** (Jul **2024**). DOI: **10.1038/s41467-024-50274-4**. URL: https://doi.org/10.1038/s41467-024-50274-4 (dornes2024polarconfinementof pages 1-2)
2. **Frolov M. et al.** *Construction of the Pseudomonas putida Strain with Low Motility and Reduced Biofilm Formation for Application in Fermentation.* **Fermentation** (Nov **2024**). DOI: **10.3390/fermentation10120606**. URL: https://doi.org/10.3390/fermentation10120606 (frolov2024constructionofthe pages 1-2, frolov2024constructionofthe pages 8-10, frolov2024constructionofthe pages 4-5)
3. **Zhang Q. et al.** *Bio-Hybrid Magnetic Robots: From Bioengineering to Targeted Therapy.* **Bioengineering** (Mar **2024**). DOI: **10.3390/bioengineering11040311**. URL: https://doi.org/10.3390/bioengineering11040311 (zhang2024biohybridmagneticrobots pages 11-13, zhang2024biohybridmagneticrobots pages 10-11, zhang2024biohybridmagneticrobots pages 13-15)
4. **Alsenani Q.** *Manipulating flagellar gene regulation in uropathogenic Escherichia coli to explore its effect(s) on the urothelial proinflammatory response.* (Year **2024**; DOI not captured in retrieved metadata). (alsenani2024manipulatingflagellargene pages 126-130)
5. **Lisevich I. et al.** *Physics of swimming and its fitness cost determine strategies of bacterial investment in flagellar motility.* **Nature Communications** (Feb **2025**). DOI: **10.1038/s41467-025-56980-x**. URL: https://doi.org/10.1038/s41467-025-56980-x (lisevich2025physicsofswimming pages 7-8, lisevich2025physicsofswimming pages 1-2)
6. **Dunn C.M. et al.** *Nascent flagellar basal bodies are immobilized by rod assembly in Bacillus subtilis.* **mBio** (Jun **2025**). DOI: **10.1128/mbio.00530-25**. URL: https://doi.org/10.1128/mbio.00530-25 (dunn2025nascentflagellarbasal pages 6-9, dunn2025nascentflagellarbasal pages 1-2, dunn2025nascentflagellarbasal pages 2-4)

Additional definitional support:
- **Thomas D.** *The design of bacterial flagella: part 2—flagellar diversity across bacterial species.* (Year not stated in retrieved metadata). (thomasUnknownyearthedesignof pages 57-59, thomasUnknownyearthedesignof pages 55-57)

---

## Summary for TraitMech YAML drafting

For `peritrichous.yaml`, the strongest universally curatable content from this evidence set is (i) **definition and boundaries** and (ii) a **modular mechanistic scaffold**: *flagellar assembly → basal body insertion/localization → peritrichous surface distribution*, where the specific localization mechanism should be taxon-scoped (PG/rod-probing module in *B. subtilis*; conserved placement/number regulators FlhF/FlhG as higher-level controllers). The edge table (artifact) can be used directly as the starting point, with uncertainty flags preserved and taxon constraints added where needed. (frolov2024constructionofthe pages 1-2, dunn2025nascentflagellarbasal pages 6-9, dornes2024polarconfinementof pages 1-2)

References

1. (thomasUnknownyearthedesignof pages 57-59): D Thomas. The design of bacterial flagella: part 2—flagellar diversity across bacterial species. Unknown journal, Unknown year.

2. (thomasUnknownyearthedesignof pages 55-57): D Thomas. The design of bacterial flagella: part 2—flagellar diversity across bacterial species. Unknown journal, Unknown year.

3. (frolov2024constructionofthe pages 1-2): Mikhail Frolov, Galim Alimzhanovich Kungurov, Emil Elmirovich Valiakhmetov, Artur Sergeyevich Gogov, Natalia Viktorovna Trachtmann, and Shamil Zavdatovich Validov. Construction of the pseudomonas putida strain with low motility and reduced biofilm formation for application in fermentation. Fermentation, 10:606, Nov 2024. URL: https://doi.org/10.3390/fermentation10120606, doi:10.3390/fermentation10120606. This article has 2 citations.

4. (alsenani2024manipulatingflagellargene pages 126-130): Q Alsenani. Manipulating flagellar gene regulation in uropathogenic escherichia coli to explore its effect (s) on the urothelial proinflammatory response. Unknown journal, 2024.

5. (lisevich2025physicsofswimming pages 7-8): Irina Lisevich, Remy Colin, Hao Yuan Yang, Bin Ni, and Victor Sourjik. Physics of swimming and its fitness cost determine strategies of bacterial investment in flagellar motility. Nature Communications, Feb 2025. URL: https://doi.org/10.1038/s41467-025-56980-x, doi:10.1038/s41467-025-56980-x. This article has 32 citations and is from a highest quality peer-reviewed journal.

6. (dunn2025nascentflagellarbasal pages 6-9): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 5 citations and is from a domain leading peer-reviewed journal.

7. (dunn2025nascentflagellarbasal pages 1-2): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 5 citations and is from a domain leading peer-reviewed journal.

8. (dornes2024polarconfinementof pages 1-2): Anita Dornes, Lisa Marie Schmidt, Christopher-Nils Mais, John C. Hook, Jan Pané-Farré, Dieter Kressler, Kai Thormann, and Gert Bange. Polar confinement of a macromolecular machine by an srp-type gtpase. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50274-4, doi:10.1038/s41467-024-50274-4. This article has 9 citations and is from a highest quality peer-reviewed journal.

9. (rosinke2025characterizinghelicobacterpyloria pages 19-22): K Rosinke. Characterizing helicobacter pylori flagellar motor accessory structures. Unknown journal, 2025.

10. (rosinke2025characterizinghelicobacterpylori pages 19-22): K Rosinke. Characterizing helicobacter pylori flagellar motor accessory structures. Unknown journal, 2025.

11. (dunn2025nascentflagellarbasal pages 2-4): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 5 citations and is from a domain leading peer-reviewed journal.

12. (dunn2025nascentflagellarbasal pages 9-11): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (frolov2024constructionofthe pages 4-5): Mikhail Frolov, Galim Alimzhanovich Kungurov, Emil Elmirovich Valiakhmetov, Artur Sergeyevich Gogov, Natalia Viktorovna Trachtmann, and Shamil Zavdatovich Validov. Construction of the pseudomonas putida strain with low motility and reduced biofilm formation for application in fermentation. Fermentation, 10:606, Nov 2024. URL: https://doi.org/10.3390/fermentation10120606, doi:10.3390/fermentation10120606. This article has 2 citations.

14. (lisevich2025physicsofswimming pages 1-2): Irina Lisevich, Remy Colin, Hao Yuan Yang, Bin Ni, and Victor Sourjik. Physics of swimming and its fitness cost determine strategies of bacterial investment in flagellar motility. Nature Communications, Feb 2025. URL: https://doi.org/10.1038/s41467-025-56980-x, doi:10.1038/s41467-025-56980-x. This article has 32 citations and is from a highest quality peer-reviewed journal.

15. (zhang2024biohybridmagneticrobots pages 11-13): Qian Zhang, Yun Zeng, Yang Zhao, Xuqi Peng, En Ren, and Gang Liu. Bio-hybrid magnetic robots: from bioengineering to targeted therapy. Bioengineering, 11:311, Mar 2024. URL: https://doi.org/10.3390/bioengineering11040311, doi:10.3390/bioengineering11040311. This article has 19 citations.

16. (zhang2024biohybridmagneticrobots pages 10-11): Qian Zhang, Yun Zeng, Yang Zhao, Xuqi Peng, En Ren, and Gang Liu. Bio-hybrid magnetic robots: from bioengineering to targeted therapy. Bioengineering, 11:311, Mar 2024. URL: https://doi.org/10.3390/bioengineering11040311, doi:10.3390/bioengineering11040311. This article has 19 citations.

17. (dunn2025nascentflagellarbasal pages 4-6): Caroline M. Dunn, Daniel J. Foust, Yongqiang Gao, Julie S. Biteen, Sidney L. Shaw, and Daniel B. Kearns. Nascent flagellar basal bodies are immobilized by rod assembly in <i>bacillus subtilis</i>. Jun 2025. URL: https://doi.org/10.1128/mbio.00530-25, doi:10.1128/mbio.00530-25. This article has 5 citations and is from a domain leading peer-reviewed journal.

18. (frolov2024constructionofthe pages 8-10): Mikhail Frolov, Galim Alimzhanovich Kungurov, Emil Elmirovich Valiakhmetov, Artur Sergeyevich Gogov, Natalia Viktorovna Trachtmann, and Shamil Zavdatovich Validov. Construction of the pseudomonas putida strain with low motility and reduced biofilm formation for application in fermentation. Fermentation, 10:606, Nov 2024. URL: https://doi.org/10.3390/fermentation10120606, doi:10.3390/fermentation10120606. This article has 2 citations.

19. (zhang2024biohybridmagneticrobots pages 13-15): Qian Zhang, Yun Zeng, Yang Zhao, Xuqi Peng, En Ren, and Gang Liu. Bio-hybrid magnetic robots: from bioengineering to targeted therapy. Bioengineering, 11:311, Mar 2024. URL: https://doi.org/10.3390/bioengineering11040311, doi:10.3390/bioengineering11040311. This article has 19 citations.