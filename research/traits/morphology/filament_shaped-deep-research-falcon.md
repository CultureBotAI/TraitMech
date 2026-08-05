---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:18:00.774200'
end_time: '2026-08-04T08:24:36.195716'
duration_seconds: 395.42
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: filament shaped
  trait_identifier: METPO:1000674
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: filament_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism grows as elongated filamentous cells
    or hypha-like structures.
  parent_traits: METPO:1000666
  synonyms: S_filament, filament, filament-shaped
  evidence_summary: 'DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports
    filamentous Streptomyces morphology as a polar-growth cell-shape system.)'
  causal_graph_summary: 'filament_shaped_streptomyces_polar_growth: 13 nodes, 12 edges'
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
- **Trait label:** filament shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000674
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism grows as elongated filamentous cells or hypha-like structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_filament, filament, filament-shaped
- **Existing evidence:** DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports filamentous Streptomyces morphology as a polar-growth cell-shape system.)
- **Existing causal graph summary:** filament_shaped_streptomyces_polar_growth: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **filament shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/filament_shaped.yaml`.

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
- **Trait label:** filament shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000674
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism grows as elongated filamentous cells or hypha-like structures.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_filament, filament, filament-shaped
- **Existing evidence:** DOI:10.1016/j.mib.2010.10.002: polar growth of Streptomyces (Supports filamentous Streptomyces morphology as a polar-growth cell-shape system.)
- **Existing causal graph summary:** filament_shaped_streptomyces_polar_growth: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **filament shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/filament_shaped.yaml`.

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


# Curation report: filament shaped

## Trait record and scope

- **Trait:** filament shaped
- **Identifier:** **METPO:1000674**
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Definition:** an organism grows as elongated filamentous cells or hypha-like structures.
- **Parent:** METPO:1000666
- **Synonyms:** S_filament; filament; filament-shaped

For the proposed Streptomyces graph, the clearest operational phenotype is **sustained vegetative growth by apical cell-wall extension, accompanied by lateral branching to produce multinucleoid hyphae/mycelia**. DivIVA-containing apical complexes—polarisomes—concentrate envelope assembly at growing tips and are central to this growth mode. Importantly, Streptomyces polar growth is mechanistically separable from cell division. (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2)

### Boundary cases

1. **Rod-shaped cells are not filaments merely because they elongate before binary fission.** The trait should require conspicuously elongated, hypha-like growth.
2. **Transient division-inhibition filamentation is a distinct implementation.** For example, antibiotic-, SOS-, or host-induced elongation of ordinarily rod-shaped bacteria may satisfy the observed morphology but should not be merged mechanistically with constitutive Streptomyces hyphal growth.
3. **Aerial hyphae are filamentous, but their conversion into chains of spores is a developmental transition, not the mechanism that originally produces vegetative filaments.** SsgB, SepG, FtsZ ladders, and related division proteins therefore belong principally in a boundary or transition subgraph. (zhang2020branchingofsporogenic pages 27-41, sen2024adispensablesepiva pages 1-2)
4. **Branching is associated but not definitionally required.** An unbranched elongated cell can still be filament-shaped; hyperbranching is an altered topology rather than stronger evidence of the trait.
5. **Pellets, clumps, and mycelial aggregates are population-scale morphologies.** They arise from filament interactions and are important in fermentation, but should not be used as synonyms for cellular filament shape.
6. **SepIVA tip localization is insufficient to infer necessity.** Its deletion causes no detectable defect in S. venezuelae tip extension, branching, growth pattern, or wall composition. (sen2024adispensablesepiva pages 10-12)

## Recommended causal architecture

The most defensible core is:

**DivIVA/polarisome organization → localized apical envelope synthesis → hyphal tip extension → elongated vegetative hyphae**, with **Scy and FilP** supporting tip organization and branching, and **CglA-mediated wall glycopolymer attachment** maintaining normal filament width, integrity, and division-site organization. (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2, bhowmick2024cellshapeand pages 8-10, bhowmick2024cellshapeand pages 1-2)

| module | candidate subject | predicate | object | evidence class | recommended action |
|---|---|---|---|---|---|
| Apical polar growth | DivIVA | organizes/localizes | polar cell-wall assembly at hyphal tips | foundational Streptomyces mechanism; strong but mostly background in retrieved set (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2) | Curate as core trait mechanism; link to apical extension and lateral branching, but add a direct primary DivIVA perturbation paper in final YAML |
| Tip extension outcome | polar cell-wall assembly at hyphal tips | enables | apical extension / filamentous vegetative growth | supported by Streptomyces polar-growth summaries and tip-localization data (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2) | Curate as central process edge for filament-shaped scope |
| Polarisome architecture | Scy | stabilizes/supports | apical polarisome / normal branching pattern | mutant evidence indicates strong effects on morphology and branching; some evidence indirect in retrieved set (sen2024adispensablesepiva pages 10-12) | Curate, but mark taxon-specific to Streptomyces and seek direct Scy mutant primary citation |
| Cytoskeletal support | FilP | supports | apical growth / hyphal morphology | mutant and localization evidence weaker than for Scy; often contextual or interaction-based (sen2024adispensablesepiva pages 10-12) | Curate as contributing factor, not sole required cause; mark moderate confidence |
| Cell-wall glycopolymer ligation | CglA | attaches/ligates | cell-wall glycopolymers to peptidoglycan | strong 2024 perturbation evidence with wall-mass reduction and enlarged hyphae/FtsZ defects (bhowmick2024cellshapeand pages 8-10, bhowmick2024cellshapeand pages 1-2) | High-priority curation as direct causal module for maintaining normal filament shape |
| Shape maintenance | cell-wall glycopolymer decoration | maintains | normal hyphal width/shape | strong phenotype evidence from cglA mutant (bhowmick2024cellshapeand pages 8-10, bhowmick2024cellshapeand pages 1-2) | Curate as direct morphology-maintenance edge |
| Stress-adaptive tip organization | StlP | organizes | tip membrane microdomain / local membrane fluidity under hyperosmotic stress | 2024 preprint; mechanistically rich but not peer-reviewed; branching and wall defects reported (claessen2024thestomatinlikeprotein pages 27-28, claessen2024thestomatinlikeprotein pages 20-27) | Curate only as uncertain/contextual edge or hold until peer-reviewed publication |
| Stress phenotype | loss of StlP | causes | hyperbranching, diffuse wall synthesis, wall-deficient cell extrusion | preprint-only perturbation evidence (claessen2024thestomatinlikeprotein pages 27-28, claessen2024thestomatinlikeprotein pages 20-27) | Do not use as core universal edge yet; retain in warning list |
| Sporogenic branching control | SflA/SflB | restrict | ectopic DivIVA/FtsZ persistence and branching in sporogenic aerial hyphae | mutant phenotype plus localization/correlation; developmental stage-specific (zhang2020branchingofsporogenic pages 27-41) | Keep as contextual/boundary module, not core vegetative filament-shape mechanism |
| Sporulation septation | SsgB | recruits/positions | FtsZ at sporulation septum sites | strong for sporulation-specific septation, not vegetative filament maintenance (zhang2020branchingofsporogenic pages 27-41) | Boundary/context only; avoid using as direct cause of filament-shaped trait |
| Sporulation coordination | SepG | ensures localization of | SsgB/FtsZ complex during sporulation | strong but sporulation-specific context (zhang2020branchingofsporogenic pages 27-41) | Boundary/context only |
| Developmental division scaffold | FtsZ | forms | sporulation septa / Z-ladders | strong developmental evidence, but pertains to hypha-to-spore transition (zhang2020branchingofsporogenic pages 27-41) | Exclude from core trait graph except as boundary relation |
| Polar-growth-associated but dispensable factor | SepIVA | localizes to | growing hyphal tips / DivIVA-associated polar-growth zones | localization and interaction evidence, but deletion shows no detectable filament-growth defect (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2) | Do not curate as required cause of filament-shaped morphology |
| Negative causal claim | sepIVA deletion | does not measurably alter | hyphal growth pattern, tip extension, branching, or wall composition | strong 2024 negative evidence (sen2024adispensablesepiva pages 10-12) | Record as anti-edge/warning; prevents overcuration of SepIVA |
| Boundary case outside Streptomyces trait core | transient division-inhibition filamentation | differs from | sustained hypha-like polar growth | scope distinction supported by contrast between Streptomyces vegetative growth and non-Streptomyces reversible filamentation literature in conversation; core retrieved context emphasizes separation of polar growth from sporulation/division modules (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2) | Add as scope note only, not graph edge |


*Table: This table prioritizes candidate mechanisms for curating METPO:1000674 in Streptomyces, separating core vegetative filament-growth edges from contextual sporulation and uncertain stress-specific modules. It is useful for deciding which nodes and edges should enter the first TraitMech graph versus remain as warnings or boundary annotations.*

## Candidate nodes grouped by type

### Trait, taxon, and anatomical nodes

| Candidate node | Grounding recommendation | Comment |
|---|---|---|
| filament-shaped morphology | **METPO:1000674** | Target trait; quote CURIE exactly in YAML. |
| Streptomyces | **NCBITaxon:1883** | Appropriate genus-level taxon restriction. |
| Streptomyces venezuelae | Use a verified NCBITaxon record at implementation | Main organism in the 2024 CglA and SepIVA studies; do not insert an unchecked numeric CURIE. |
| Streptomyces coelicolor | Use a verified strain-specific NCBITaxon record | Many foundational morphogenesis results are strain-specific. |
| vegetative hypha | Label-only candidate | Distinguish from aerial/sporogenic hypha. |
| aerial hypha | Label-only candidate | Developmental filament that later undergoes synchronous septation. |
| hyphal tip / apical growth zone | Label-only candidate | Cellular region at which DivIVA and wall synthesis are concentrated. |
| lateral branch site | Label-only candidate | Site at which a new growth pole is established. |
| polarisome | Label-only candidate | Streptomyces apical protein assembly; avoid forcing an imprecise ontology mapping. |

### Genes and proteins

| Node | Function relevant to graph | Curation status |
|---|---|---|
| **DivIVA** | Essential apical organizer; tip clusters direct polar wall assembly and lateral branch establishment | Core, high priority. |
| **Scy** | Coiled-coil polarisome-associated protein; supports stable tip growth and normal branching | Core-supporting, taxon-specific. |
| **FilP** | Intermediate-filament-like/coiled-coil cytoskeletal protein associated with the apical growth apparatus | Core-supporting; avoid claiming absolute requirement. |
| **CglA** | LCP-family wall glycopolymer ligase; localizes to wall-synthesis zones | Core shape-maintenance module. |
| **SepIVA** | DivIVA-interacting, tip-localized coiled-coil protein | Context node only; experimentally dispensable in S. venezuelae. |
| **StlP** | Stomatin-like protein proposed to organize fluid tip membrane microdomains during osmotic stress | Uncertain; 2024 evidence retrieved is a preprint. |
| **SflA/SflB** | SepF-like proteins restricting ectopic DivIVA/FtsZ persistence and branching in sporogenic hyphae | Developmental boundary module. |
| **SsgA/SsgB** | Sporulation proteins; SsgB recruits FtsZ to future septa | Transition-to-spore module, not core filament formation. |
| **SepG** | Membrane protein needed for proper SsgB localization during sporulation | Transition module. |
| **FtsZ** | GTPase division scaffold forming Z-rings/Z-ladders | Boundary/transition node. |
| **DisA** | c-di-AMP cyclase genetically linked to CglA-dependent wall physiology under high salt | Contextual stress node; relationship requires careful predicate choice. |

Gene/protein CURIEs should be assigned from verified organism-specific UniProt or locus records during YAML implementation. Names alone are preferable to an incorrect cross-species accession.

### Processes, molecular functions, and cellular components

Candidate labels include **polar growth**, **apical cell-wall synthesis**, **peptidoglycan biosynthesis**, **cell-wall glycopolymer attachment**, **hyphal tip extension**, **lateral branching**, **membrane-microdomain organization**, **membrane fluidity**, **FtsZ-ring assembly**, **sporulation septation**, and **cell-shape maintenance**. Plausible ontology families are GO biological process for peptidoglycan biosynthesis and cell morphogenesis, GO cellular component for cell pole/cell wall, and GO molecular function for glycopolymer transferase or phosphotransferase activity. Exact GO terms should be resolved against the current ontology rather than inferred from labels.

### Chemicals and environmental or experimental factors

| Node | Suggested grounding | Role |
|---|---|---|
| peptidoglycan | **CHEBI:8005** | Load-bearing wall polymer and product/site of localized synthesis. |
| cell-wall glycopolymer | Label-only candidate | CglA-dependent wall constituent; chemical identity may vary. |
| cyclic di-AMP | Verify current ChEBI CURIE | Osmotic/cell-wall homeostasis signal implicated through DisA genetics. |
| hyperosmotic stress / high-salt condition | ENVO or ECTO term after verification | Context for the proposed StlP mechanism and cglA–disA interaction. |
| vancomycin | Verify current ChEBI CURIE | Experimental inhibitor of peptidoglycan synthesis; useful perturbation, not an endogenous cause. |
| membrane lipids / locally fluid membrane domain | Label-only candidate | Proposed StlP-dependent tip environment. |

## Candidate evidence-backed edges

“Snippet” below is kept short and faithful to the retrieved source text or evidence extraction. Predicates are normalized proposals, not necessarily verbs used by the authors.

| # | Subject–predicate–object | Evidence and supporting snippet | Interpretation and curation note |
|---:|---|---|---|
| 1 | **DivIVA → organizes → polar cell-wall assembly** | Sen et al. 2024: “DivIVA co-localizes with SepIVA at hyphal tips and directs polar cell wall assembly through interaction with peptidoglycan synthases.” (sen2024adispensablesepiva pages 10-12) | Strong mechanistic consensus, but the retrieved 2024 article treats much of this as established background. Retain the supplied foundational DOI 10.1016/j.mib.2010.10.002 or another direct DivIVA perturbation paper on the edge. |
| 2 | **DivIVA polarisome → enables → hyphal tip extension** | “DivIVA clusters (polarisomes) localize at hyphal tips and are essential for polar growth.” (sen2024adispensablesepiva pages 1-2) | Core causal edge; Streptomyces/Actinomycetota-specific. |
| 3 | **DivIVA polarisome → promotes → lateral branch formation** | The same source describes DivIVA as essential for “polar growth and lateral branching.” (sen2024adispensablesepiva pages 1-2) | Curatable, but branch formation should remain a downstream morphology feature rather than part of the trait definition. |
| 4 | **polar cell-wall synthesis → produces → apically extending vegetative hypha** | Streptomyces vegetative filamentous growth is described as “polar cell wall synthesis at hyphal tips with lateral branching.” (sen2024adispensablesepiva pages 1-2) | High-priority process-to-trait edge. |
| 5 | **Scy and FilP → support → normal apical growth architecture** | scy-filP mutants show “irregular, highly branched morphology compared to wild-type”; Scy has stronger effects and epistasis over FilP. (sen2024adispensablesepiva pages 10-12) | Direct mutant support, but avoid combining the proteins into one node in the final graph. Curate separate edges with moderate confidence. |
| 6 | **scy loss / unstable polarisome → increases → abnormal branching and tip-growth instability** | The 2024 analysis reports strong Scy effects and irregular hyperbranching in scy-filP mutants. (sen2024adispensablesepiva pages 10-12) | Curatable as a perturbation edge; obtain the direct Scy primary paper before asserting that Scy alone is sufficient for every phenotype. |
| 7 | **CglA → ligates → glycopolymers to peptidoglycan** | CglA is an “LCP family” phosphotransferase and “major cell wall glycopolymer ligase”; YPet-CglA localizes at tips and branch zones. (bhowmick2024cellshapeand pages 8-10) | Strong 2024 primary evidence; high-priority biochemical edge. |
| 8 | **CglA activity → maintains → normal vegetative-hypha dimensions and shape** | “CglA deletion reduces cell wall glycopolymers, causing enlarged vegetative hyphae.” (bhowmick2024cellshapeand pages 1-2) | Strong direct perturbation edge. More precise than claiming CglA generates filamentation itself. |
| 9 | **cglA deletion → decreases → wall-associated glycopolymer material** | From identical 2.5-g biomass samples, wild-type wall extracts yielded **217.7–216.7 mg**, versus **139.4–82.9 mg** for the mutant. (bhowmick2024cellshapeand pages 8-10) | Useful quantitative support. It measures recovered wall material, not necessarily pure glycopolymer abundance; preserve the assay context. |
| 10 | **reduced wall glycopolymer decoration → causes → enlarged/swollen and anomalously branched hyphae** | The cglA mutant had “striking enlargement of hyphae,” anomalous branching, and swollen tips. (bhowmick2024cellshapeand pages 8-10) | Strong morphology edge, taxon- and assay-specific. |
| 11 | **reduced wall glycopolymer decoration → disrupts → FtsZ-ring assembly/positioning** | cglA deletion produced “defective FtsZ-ring assembly and positioning” and misplaced septa. (bhowmick2024cellshapeand pages 1-2) | Curatable as a wall-to-division edge, but this is principally relevant to compartmentation/sporulation rather than establishment of filament shape. |
| 12 | **cglA deletion → suppresses → high-salt growth defect of disA mutant** | Deletion of cglA “restores growth of disA mutants under high-salt conditions.” (bhowmick2024cellshapeand pages 1-2) | Direct genetic interaction; mechanism and direction through c-di-AMP remain unresolved. Curate only with an experimental-genetic predicate, not “CglA inhibits c-di-AMP.” |
| 13 | **StlP → organizes → fluid tip membrane microdomain under hyperosmotic stress** | The preprint proposes that StlP oligomerization “creates membrane microdomains that maintain local membrane fluidity and coordinate cell wall synthesis.” (claessen2024thestomatinlikeprotein pages 27-28) | Mechanistically attractive but **uncertain/preprint-only**. Hold from the core graph or flag `confidence: low`. |
| 14 | **stlP deletion → causes → hyperbranching and increased hyphal diameter** | Quantitative branching analyses covered **n=188–282 hyphae**; mutants showed hyperbranching, increased diameter, diffuse wall synthesis, and altered wall architecture. (claessen2024thestomatinlikeprotein pages 20-27) | Direct perturbation evidence, but not yet peer reviewed in the retrieved record. |
| 15 | **StlP expression → prevents → hyperbranching under hyperosmotic stress** | Constitutive stlP expression increased colony size and prevented hyperbranching; assessed populations included **219 wild-type and 189 expression-strain filaments**. (claessen2024thestomatinlikeprotein pages 27-28) | Stress- and taxon-specific. Do not generalize to all filamentous bacteria. |
| 16 | **SepIVA → localizes to/interacts with → DivIVA-containing hyphal tips** | mNeonGreen-SepIVA accumulated at growing tips and bacterial two-hybrid analysis detected interaction with DivIVA. (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2) | Curate as localization/interaction only, not as a causal requirement. |
| 17 | **sepIVA deletion → has no detectable effect on → filament growth morphology** | Deletion caused “no detectable phenotype in hyphal growth pattern, tip extension, branching, or cell wall composition.” (sen2024adispensablesepiva pages 10-12) | Important negative evidence or anti-edge. It directly argues against SepIVA as a required graph node in S. venezuelae. |
| 18 | **SflA/SflB → restrict → ectopic branching of sporogenic aerial hyphae** | sflA and sflB null mutants formed branched, irregular spore chains, whereas wild type and complements were unbranched. (zhang2020branchingofsporogenic pages 27-41) | Causal mutant phenotype, but stage-specific. Include only in an aerial-hypha/sporulation extension. |
| 19 | **loss of SflA/SflB → correlates with → ectopic DivIVA and persistent FtsZ in spore chains** | DivIVA was ectopically present and FtsZ ladders persisted longer in mutants. (zhang2020branchingofsporogenic pages 27-41) | Localization/correlation, not proof that ectopic DivIVA or FtsZ independently causes branching. Mark uncertain. |
| 20 | **SsgB → recruits → FtsZ at sporulation septum sites** | The study describes “SsgB-mediated FtsZ recruitment during sporulation septation.” (zhang2020branchingofsporogenic pages 27-41) | Strong developmental edge, but it explains filament partitioning into spores—not vegetative filament production. |
| 21 | **SepG → enables localization of → SsgB–FtsZ complex** | Without SepG, SsgB fails to localize properly; SepG supports membrane localization of the division complex. | Relevant to sporulation-specific compartmentation. Treat as boundary-context rather than a direct trait edge. (zhang2020branchingofsporogenic pages 27-41) |

## Recent developments and interpretation

### 2024: wall glycopolymers become a direct shape-control module

Bhowmick et al. identify CglA as a key LCP-family ligase and connect wall glycopolymer attachment to hyphal dimensions, FtsZ-ring organization, septum placement, and vitality. This advances the graph beyond the traditional DivIVA–Scy–FilP polarisome by adding a directly perturbed **wall-composition/shape-maintenance module**. The wall-material yields—approximately 217 mg in wild type versus 83–139 mg in the mutant from equal biomass—provide quantitative biochemical support, although they should not be represented as a direct percentage of a chemically pure glycopolymer. Published October 2024, DOI: [10.1128/mbio.01492-24](https://doi.org/10.1128/mbio.01492-24). (bhowmick2024cellshapeand pages 8-10, bhowmick2024cellshapeand pages 1-2)

### 2024: SepIVA is associated with—but not required for—polar growth

Sen et al. show that SepIVA localizes to vegetative tips and interacts with DivIVA, yet is dispensable for growth, division, sporulation, tip extension, branching, and detectable wall composition in S. venezuelae. Triple-mutant analysis did not uncover redundancy with Scy and FilP. This is an instructive example of why localization should not be converted automatically into a causal TraitMech edge. Published November 2024, DOI: [10.1186/s12866-024-03625-6](https://doi.org/10.1186/s12866-024-03625-6). (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2)

### 2024 preprint: membrane microdomains under osmotic stress

The StlP study proposes that locally increased membrane fluidity keeps apical wall-synthesis machinery spatially organized. Loss of StlP produces hyperbranching, increased diameter, diffuse glycan deposition, wall thinning, and extrusion of wall-deficient cells; expression in another actinobacterium improves polar growth under hyperosmotic stress. This potentially adds an environmental-stress layer upstream of localized wall assembly, but the retrieved version is a January 2024 Research Square preprint and should not yet define a universal mechanism. DOI: [10.21203/rs.3.rs-3811693/v1](https://doi.org/10.21203/rs.3.rs-3811693/v1). (claessen2024thestomatinlikeprotein pages 27-28, claessen2024thestomatinlikeprotein pages 20-27)

### Current expert synthesis

The evidence favors a **modular** rather than single-gene definition of filament shape:

1. **Spatial organizer:** DivIVA-centered polarisome establishes the growth pole.
2. **Structural stabilization:** Scy and FilP maintain productive tip architecture and branching patterns.
3. **Envelope execution:** localized peptidoglycan synthesis extends the tip.
4. **Wall composition:** CglA-mediated glycopolymer attachment preserves normal width, shape, and divisome organization.
5. **Environmental robustness:** membrane organization may preserve tip synthesis during osmotic stress, with StlP as a provisional candidate.
6. **Developmental termination/partitioning:** SsgB–SepG–FtsZ and SflA/B remodel or partition aerial filaments during sporulation rather than create vegetative filamentation.

This interpretation is consistent with evidence that polar growth can proceed independently of conventional division, while later sporulation requires extensive coordinated FtsZ-ring formation. (sen2024adispensablesepiva pages 10-12, zhang2020branchingofsporogenic pages 27-41, sen2024adispensablesepiva pages 1-2)

## Applications and real-world relevance

Filament morphology is operationally important in industrial cultures of Streptomyces and other filamentous microorganisms because dispersed mycelia, loose clumps, and compact pellets alter broth rheology, mixing, oxygen and nutrient transfer, and product formation. There is no universal optimum: the preferred morphology depends on strain, product, and process. Consequently, DivIVA/polar-growth or wall-shape nodes may eventually be engineering targets, but interventions can be pleiotropic because development and secondary metabolism are coupled.

The most defensible near-term applications are:

- **Morphology engineering in fermentation:** controlling branch frequency, hyphal diameter, fragmentation, and aggregation to improve mass transfer or product recovery.
- **Natural-product production:** Streptomyces filament development is linked to antibiotic and specialized-metabolite regulation; perturbations must therefore be evaluated for both morphology and yield.
- **Stress-robust bioprocessing:** provisional StlP-like membrane organization could inform engineering for high-osmolarity media, pending peer-reviewed validation.
- **Antimicrobial mechanism studies:** inhibitors of apical peptidoglycan synthesis can cause growth arrest, lysis, or tip failure, making the growth zone a potential vulnerability.
- **Microscopy and phenotype annotation:** distinguishing vegetative hyphae from sporogenic septation and transient antibiotic-induced filaments improves automated morphology classification.

These are applications of understanding the trait; they do not establish that any single morphology universally increases production.

## Recommended first-pass YAML graph

A conservative first graph should contain approximately the following causal spine:

1. `DivIVA —organizes→ apical polarisome`
2. `apical polarisome —localizes→ peptidoglycan/cell-envelope synthesis at hyphal tip`
3. `localized apical cell-wall synthesis —enables→ hyphal tip extension`
4. `hyphal tip extension —produces→ METPO:1000674`
5. `DivIVA —promotes→ lateral branch-site establishment`
6. `Scy —stabilizes/supports→ apical polarisome`
7. `FilP —supports→ normal apical growth architecture`
8. `CglA —ligates→ cell-wall glycopolymer to peptidoglycan`
9. `cell-wall glycopolymer attachment —maintains→ normal hyphal shape`
10. `cglA loss —causes→ enlarged/swollen hyphae and abnormal branching`

Put SsgB, SepG, FtsZ, and SflA/B in a separate **sporulation/partitioning extension**. Put StlP in an **uncertain hyperosmotic-stress extension**. Record SepIVA as associated/localized but dispensable rather than placing it in the required causal spine.

## Warnings: claims not ready for TraitMech curation

- **Do not curate `SepIVA causes filament shape`.** The best recent deletion evidence is negative. (sen2024adispensablesepiva pages 10-12)
- **Do not infer causality from co-localization alone.** This particularly affects SepIVA and ectopic DivIVA/FtsZ in sfl mutants.
- **Do not make FtsZ a core positive cause of vegetative filament formation.** Its strongest evidence here concerns sporulation septation and division-site organization.
- **Do not equate abnormal hyperbranching with acquisition of the trait.** A mutant may remain filamentous while having defective filament architecture.
- **Do not universalize Streptomyces mechanisms to all filament-shaped bacteria.** Constitutive polar hyphal growth and reversible division-block filamentation are mechanistically distinct.
- **Do not curate the StlP model as established or universal yet.** The retrieved 2024 source is a preprint. (claessen2024thestomatinlikeprotein pages 27-28, claessen2024thestomatinlikeprotein pages 20-27)
- **Do not translate the CglA wall-extract masses directly into glycopolymer percentages.** The reported values are recovered wall-associated material from equal biomass, not necessarily pure polymer. (bhowmick2024cellshapeand pages 8-10)
- **Do not assign unverified GO, UniProt, ChEBI, or strain-level NCBITaxon CURIEs.** Label-only nodes are explicitly preferable to fabricated identifiers.
- **Do not encode `cglA inhibits DisA/c-di-AMP`.** Suppression of a high-salt growth defect is a genetic interaction and does not by itself establish the biochemical direction. (bhowmick2024cellshapeand pages 1-2)

## DOI-first bibliography

1. **Sen BC, Mavi PS, Irazoki O, et al.** “A dispensable SepIVA orthologue in *Streptomyces venezuelae* is associated with polar growth and not cell division.” *BMC Microbiology* 24 (November 2024). DOI: [10.1186/s12866-024-03625-6](https://doi.org/10.1186/s12866-024-03625-6). (sen2024adispensablesepiva pages 10-12, sen2024adispensablesepiva pages 1-2)
2. **Bhowmick S, Viveros RP, Latoscha A, et al.** “Cell shape and division septa positioning in filamentous *Streptomyces* require a functional cell wall glycopolymer ligase CglA.” *mBio* 15(10) (October 2024). DOI: [10.1128/mbio.01492-24](https://doi.org/10.1128/mbio.01492-24). (bhowmick2024cellshapeand pages 8-10, bhowmick2024cellshapeand pages 1-2)
3. **Claessen D, Zhong X, Baur S, et al.** “The stomatin-like protein StlP organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress.” Research Square preprint (January 2024). DOI: [10.21203/rs.3.rs-3811693/v1](https://doi.org/10.21203/rs.3.rs-3811693/v1). (claessen2024thestomatinlikeprotein pages 27-28, claessen2024thestomatinlikeprotein pages 20-27)
4. **Zhang L, Willemse J, Yagüe P, de Waal E, Claessen D, van Wezel GP.** “Branching of sporogenic aerial hyphae in sflA and sflB mutants of *Streptomyces coelicolor* correlates to ectopic localization of DivIVA and FtsZ in time and space.” bioRxiv preprint (December 2020). DOI: [10.1101/2020.12.26.424426](https://doi.org/10.1101/2020.12.26.424426). A later peer-reviewed version should replace this citation during curation. (zhang2020branchingofsporogenic pages 27-41)
5. **Existing supplied evidence:** “Polar growth of *Streptomyces*.” *Current Opinion in Microbiology* (2010/2011). DOI: [10.1016/j.mib.2010.10.002](https://doi.org/10.1016/j.mib.2010.10.002). Retain as foundational support for the DivIVA-centered polar-growth system.

## Curation conclusion

**METPO:1000674** is well suited to a Streptomyces-focused TraitMech graph if the graph represents **persistent polar hyphal growth**, not every route to bacterial elongation. DivIVA-centered spatial organization and localized envelope synthesis form the strongest causal core. CglA adds recent, direct evidence that wall glycopolymer attachment maintains normal filament architecture. Scy and FilP are justified supporting nodes, whereas SepIVA is specifically contraindicated as a required cause. Sporulation proteins should be modeled as a downstream filament-partitioning module, and the StlP–membrane-fluidity mechanism should remain explicitly uncertain until peer-reviewed confirmation.

References

1. (sen2024adispensablesepiva pages 10-12): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

2. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

3. (zhang2020branchingofsporogenic pages 27-41): Le Zhang, Joost Willemse, Paula Yagüe, Ellen de Waal, Dennis Claessen, and Gilles P. van Wezel. Branching of sporogenic aerial hyphae in sfla and sflb mutants of streptomyces coelicolor correlates to ectopic localization of diviva and ftsz in time and space. bioRxiv, Dec 2020. URL: https://doi.org/10.1101/2020.12.26.424426, doi:10.1101/2020.12.26.424426. This article has 2 citations.

4. (bhowmick2024cellshapeand pages 8-10): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (bhowmick2024cellshapeand pages 1-2): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (claessen2024thestomatinlikeprotein pages 27-28): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

7. (claessen2024thestomatinlikeprotein pages 20-27): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.