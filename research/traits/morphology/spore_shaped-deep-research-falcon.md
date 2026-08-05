---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:00:37.611594'
end_time: '2026-08-04T10:10:10.533596'
duration_seconds: 572.92
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: spore shaped
  trait_identifier: METPO:1000682
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spore_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism or differentiated cell has an endospore-like
    morphology, reflecting a dormant spore body with specialized protective layers.
  parent_traits: METPO:1000666
  synonyms: spore-shaped
  evidence_summary: 'DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports
    endospore morphology as a differentiated structure with specialized surface layers.)'
  causal_graph_summary: 'spore_shaped_endospore_layers: 18 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spore shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000682
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism or differentiated cell has an endospore-like morphology, reflecting a dormant spore body with specialized protective layers.
- **Parent traits:** METPO:1000666
- **Synonyms:** spore-shaped
- **Existing evidence:** DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports endospore morphology as a differentiated structure with specialized surface layers.)
- **Existing causal graph summary:** spore_shaped_endospore_layers: 18 nodes, 13 edges

## Research Objective

Research the microbial trait **spore shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_shaped.yaml`.

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
- **Trait label:** spore shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000682
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism or differentiated cell has an endospore-like morphology, reflecting a dormant spore body with specialized protective layers.
- **Parent traits:** METPO:1000666
- **Synonyms:** spore-shaped
- **Existing evidence:** DOI:10.1038/nrmicro2921: structure of the endospore coat (Supports endospore morphology as a differentiated structure with specialized surface layers.)
- **Existing causal graph summary:** spore_shaped_endospore_layers: 18 nodes, 13 edges

## Research Objective

Research the microbial trait **spore shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_shaped.yaml`.

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


# Curation-focused research report: **spore shaped**

## 1. Scope and recommended interpretation

**Trait:** spore shaped  
**Identifier:** **METPO:1000682**  
**Category:** MORPHOLOGY  
**Term kind:** CLASS  
**Parent:** METPO:1000666  
**Synonym:** spore-shaped

### Scope summary

For TraitMech, **METPO:1000682** should denote the morphology of a differentiated bacterial **endospore-like cell body**, not merely the genetic capacity to sporulate. The canonical phenotype is an ovoid or ellipsoidal, metabolically dormant body containing a partially dehydrated core and genome, surrounded by an inner membrane, germ-cell-wall peptidoglycan, a thick cortex, an outer membrane, and a proteinaceous coat; some taxa additionally possess a crust or exosporium. This architecture is produced through polar septation, chromosome transfer, engulfment, cortex synthesis, coat encasement, maturation, and mother-cell lysis (khanna2020shapinganendospore pages 1-2, mckenney2013thebacillussubtilis pages 2-4, khanna2020shapinganendospore pages 2-4).

A useful graph endpoint is therefore:

> **mature layered endospore architecture —realizes→ METPO:1000682**

The morphology is related to—but should not be equated with—heat resistance, lysozyme resistance, dormancy, germination ability, phase brightness, or sporulation frequency. These are correlated physiological or assay traits. For example, *Clostridium sporogenes* `spoIVA` mutants generated immature and heteromorphic bodies with defective cortex, coat, and exosporium and failed to acquire normal resistance, demonstrating that resistance and morphology may fail together without being identical phenotypes (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 8-9).

### Boundary cases

**Include:**
- Mature free bacterial endospores with the characteristic layered dormant-cell body.
- Developing forespores only when an assay explicitly scores progression toward or disruption of this morphology.
- Taxon-specific surface variants—coat plus crust or coat plus exosporium—provided that the central endospore architecture is present.

**Exclude or model separately:**
- The general capacity to form spores: **GO:0030435**, “sporulation resulting in formation of a cellular spore,” is a biological process, not the morphology itself.
- Vegetative rod, coccoid, filamentous, or swollen-cell morphology.
- Fungal spores, actinomycete exospores/conidia, myxospores, cysts, and reproductive spores not formed by bacterial endosporulation.
- Phase-bright objects without structural confirmation; debris and storage granules can confound light-microscopy scoring.
- Resistance-only measurements. Heat- or lysozyme-resistant CFU provide useful maturation evidence but do not directly establish shape.
- Abnormal swirl structures, cortex-free immature spores, and mother-cell protein aggregates; these are negative or aberrant morphogenesis phenotypes rather than positive instances of **METPO:1000682** (kuwana2024spoivaisan pages 8-9).

## 2. Current mechanistic understanding

The best-resolved model is *Bacillus subtilis*. Polar septation creates a small forespore and a larger mother cell. Because only approximately one-third of the chromosome is initially trapped in the forespore, SpoIIIE transfers the remainder across the septum. The mother-cell membrane then migrates around the forespore in a phagocytosis-like engulfment event. After engulfment, cortex peptidoglycan is deposited between the two forespore membranes, while mother-cell proteins assemble a multilayered coat around the outer forespore membrane (khanna2020shapinganendospore pages 2-4).

Direct cryo-electron tomography showed that engulfment involves 10–30-nm-wide, 5–20-nm-long membrane projections. The process lasts approximately 60 minutes, increases mother-cell membrane area by about 2 µm² or 25%, and remodels the forespore from hemispherical toward ovoid while approximately doubling its size. Loss of any SpoIID–SpoIIM–SpoIIP component blocks membrane migration after polar septation; inhibition of new peptidoglycan synthesis also reduces or eliminates the projections. These experiments support a model in which newly synthesized peptidoglycan ahead of the leading edge is tethered and cleaved by the SpoIIDMP machinery, enabling membrane advance (khanna2019themoleculararchitecture pages 10-12, khanna2020shapinganendospore pages 9-11, khanna2019themoleculararchitecture pages 13-14, khanna2019themoleculararchitecture pages 4-5).

The cortex and coat then establish the mature boundary. The cortex is specialized peptidoglycan assembled between the inner and outer forespore membranes. The coat contains at least 70 proteins in *B. subtilis* and begins localizing during engulfment. Mature *B. subtilis* spores have inner coat, outer coat, and crust; other taxa may instead have an exosporium separated from the coat by an interspace (mckenney2013thebacillussubtilis pages 2-4).

## 3. Candidate graph nodes

### A. Trait and biological-process nodes

- **spore shaped** — **METPO:1000682**
- Parent morphology — **METPO:1000666**
- Sporulation resulting in formation of a cellular spore — **GO:0030435**
- Polar septation — label-only candidate pending exact ontology verification
- Chromosome translocation into forespore — label-only candidate
- Forespore engulfment — label-only candidate
- Cortex peptidoglycan biosynthesis — **GO:0009252** is a conservative generic grounding for peptidoglycan biosynthesis
- Coat assembly / spore encasement — label-only candidates
- Endospore maturation — label-only candidate
- Mother-cell lysis and spore release — label-only candidate

### B. Cellular structures and localizations

- Endospore-forming forespore — candidate **GO:0042601**
- Mother cell; polar septum; inner forespore membrane; outer forespore membrane — label-only unless exact GO cellular-component terms are verified
- Spore core
- Germ cell wall
- Cortex
- Spore coat; basement layer; inner coat; outer coat; crust
- Exosporium and interspace
- Toroidal forespore chromosome
- Peptidoglycan-based cell wall — **GO:0009274**
- “Thin light matrix,” “thin dark matrix,” “thick light matrix,” “thick dark matrix,” bead-like layers, and dark smooth layer — retain as **label-only ultrastructural observations**, not universal coat-layer classes

### C. Genes, proteins, and complexes

**Early development:** Spo0A, σH, polar division machinery, SpoIIIE.

**Engulfment:** SpoIID, SpoIIM, SpoIIP, and the SpoIIDMP/DMP complex; forespore penicillin-binding proteins and peptidoglycan-synthesis machinery.

**Cortex candidates:** SpoVE and SpoVD are well-established candidates from the broader *B. subtilis* literature, but the retrieved primary snippets did not provide sufficient direct mutant detail for a high-confidence edge here. They should remain provisional until a primary cortex-biogenesis paper is attached.

**Coat morphogenesis:** SpoVM, SpoIVA, SpoVID, SafA, CotE. These constitute the strongest source-backed morphogenetic set for the present graph. Regulatory nodes include σE, σK, SpoIIID, and GerE; these regulate assembly timing but are upstream of morphology and should only be included if the graph supports regulatory edges (mckenney2013thebacillussubtilis pages 24-26).

**Core protection:** small acid-soluble spore proteins (SASPs), RecA-associated repair machinery, and proteins mediating dipicolinate accumulation. These primarily explain resistance and chromosome organization rather than external shape.

Use label-only protein nodes unless species-specific UniProt accessions are verified during YAML curation; this avoids conflating orthologues from *B. subtilis*, *C. difficile*, and *C. sporogenes*.

### D. Chemicals and environmental factors

- Peptidoglycan — **CHEBI grounding should be verified before insertion**; GO:0009274 can conservatively ground the corresponding cellular structure.
- Calcium dipicolinate — candidate **CHEBI:58746**.
- Water depletion / core dehydration.
- Nutrient limitation or starvation.
- Medium composition, magnesium availability, pH, temperature, aeration, and sporulation-inducing metabolites.
- Peptidoglycan-synthesis inhibitors as experimental perturbations.
- Heat and lysozyme as maturation/resistance assay factors.
- Auramine O, pararosaniline hydrochloride, and APBT as assay reagents used to visualize spore surface development in *C. sporogenes* (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 8-9).

### E. Taxon context

- *Bacillus subtilis* — candidate **NCBITaxon:1423**; principal architectural model.
- *Clostridium sporogenes* — candidate **NCBITaxon:1509**; direct 2024 SpoIVA evidence.
- Endospore-forming Bacillota/Firmicutes — use an appropriate current NCBI taxon only after checking the desired taxonomic rank.
- Do not transfer detailed *B. subtilis* coat-layer assignments wholesale to Clostridia. Conservation of basic morphological stages does not imply identical genetic orchestration or surface architecture (kuwana2024spoivaisan pages 8-9).

## 4. Candidate causal graph

The following matrix summarizes the recommended backbone.

| mechanistic stage | subject node | causal predicate | object node | strongest organism/evidence | confidence/caveat |
|---|---|---|---|---|---|
| environmental induction | nutrient starvation / reduced growth substrates | promotes | sporulation initiation | Bacilli review: starvation described as the starting signal for sporulation; medium composition, pH, temperature, aeration, and metabolites also implicated (voitsekhovsky2024peculiaritiesofthe pages 1-3) | Medium; mechanism explicitly debated and often indirect, so curate as upstream environmental input rather than direct morphology determinant |
| early sporulation patterning | polar septation | creates | forespore | *Bacillus subtilis* review: stage II polar septum creates the smaller forespore and larger mother cell (khanna2020shapinganendospore pages 2-4, khanna2020shapinganendospore pages 1-2) | High for *B. subtilis* and endospore-forming Firmicutes; developmental step, not by itself sufficient for mature spore-shaped morphology |
| chromosome partitioning | SpoIIIE | translocates | forespore chromosome | *B. subtilis* review: trapped chromosome is actively transported to the forespore by SpoIIIE at septal midpoint (khanna2020shapinganendospore pages 2-4) | High for *B. subtilis*; supports normal forespore development, but indirect to final shape |
| engulfment machinery | SpoIID/SpoIIM/SpoIIP complex (DMP) | enables | engulfment membrane migration | *B. subtilis* cryo-ET and review: loss-of-function mutants block membrane migration after polar septation (khanna2019themoleculararchitecture pages 10-12, khanna2020shapinganendospore pages 9-11, khanna2019themoleculararchitecture pages 13-14) | High in *B. subtilis*; ortholog conservation broader than direct evidence |
| engulfment substrate coupling | new peptidoglycan ahead of leading edge | is degraded by / coupled with | SpoIID/SpoIIM/SpoIIP-driven engulfment | *B. subtilis* cryo-ET with PG synthesis inhibitors: new PG synthesis and DMP jointly required for finger-like projections and membrane advance (khanna2019themoleculararchitecture pages 10-12, khanna2019themoleculararchitecture pages 13-14, khanna2019themoleculararchitecture pages 4-5) | High in *B. subtilis*; mechanistic model well supported but still framed as model in parts |
| cell-shape remodeling | engulfment completion | produces | double-membrane ovoid forespore | *B. subtilis* review: engulfment surrounds forespore; forespore remodels toward ovoid endospore architecture (khanna2020shapinganendospore pages 1-2, khanna2020shapinganendospore pages 9-11) | Medium-high; morphology transition is clear, but exact edge is developmental summary rather than single-gene experiment |
| cortex biogenesis | cortex peptidoglycan | surrounds / shapes | forespore core | Structural reviews and microscopy define cortex between inner and outer forespore membranes as a major protective layer of mature spore architecture (mckenney2013thebacillussubtilis pages 2-4, khanna2020shapinganendospore pages 2-4, kuwana2024spoivaisan pages 8-9) | High for structural role; direct gene-to-cortex edges for SpoVE/SpoVD are better grounded in review than in retrieved primary snippets |
| coat biogenesis | spore coat | encases | forespore surface | Structural review: coat proteins localize during engulfment and form outermost shell; mature spores show coat external to cortex (mckenney2013thebacillussubtilis pages 2-4, kuwana2024spoivaisan pages 8-9) | High for structural role; specific layer composition is taxon-variable |
| basement layer morphogenesis | SpoIVA | tethers / organizes | nascent coat layers at forespore outer membrane | *B. subtilis* review and 2024 cryo-ET/TEM: absence of SpoIVA mislocalizes all nascent coat layers; *C. sporogenes* spoIVA mutant has abnormal forespores lacking normal cortex/coat/exosporium (bauda2024ultrastructureofmacromolecular pages 5-7, mckenney2013thebacillussubtilis pages 11-13, kuwana2024spoivaisan pages 8-9) | High; strong cross-taxon support for coat morphogenesis, though downstream layer details differ by species |
| coat encasement | SpoVID | contributes to assembly of | thin dark and thick dark coat matrices / spore encasement | *B. subtilis* 2024 cryo-ET/TEM: thin dark matrix absent and thick dark matrix altered in ΔspoVID; review identifies SpoVID as required for encasement (bauda2024ultrastructureofmacromolecular pages 5-7, mckenney2013thebacillussubtilis pages 24-26) | High in *B. subtilis*; matrix naming from ultrastructure paper may need label-only nodes |
| inner coat morphogenesis | SafA | required for proper assembly of | thick dark matrix / inner coat | *B. subtilis* 2024 cryo-ET/TEM: thick dark matrix absent or aggregated in ΔsafA; prior review places SafA in inner coat morphogenesis (bauda2024ultrastructureofmacromolecular pages 5-7, mckenney2013thebacillussubtilis pages 24-26, bauda2024ultrastructureofmacromolecular pages 7-9) | High in *B. subtilis*; mapping thick dark matrix to named coat layer is partly interpretive |
| outer coat morphogenesis | CotE | required for formation of | bead-like layers / outer coat organization | *B. subtilis* 2024 cryo-ET/TEM: bead-like layers disappear in ΔcotE and dark smooth layer becomes abnormal; review assigns CotE to outer coat assembly (bauda2024ultrastructureofmacromolecular pages 5-7, mckenney2013thebacillussubtilis pages 24-26, bauda2024ultrastructureofmacromolecular pages 7-9) | High in *B. subtilis*; outermost structures can differ in exosporium-forming taxa |
| mature morphology | layered endospore architecture (dehydrated core + cortex + coat, optional exosporium) | realizes | METPO:1000682 | Reviews and TEM define mature endospore as a dormant cell with concentric protective layers distinct from vegetative cells (mckenney2013thebacillussubtilis pages 2-4, khanna2020shapinganendospore pages 1-2, kuwana2024spoivaisan pages 8-9) | High for phenotype definition; should not be conflated with sporulation ability, heat resistance, or phase-brightness alone |


*Table: This table summarizes candidate mechanistic nodes and causal edges for curating METPO:1000682, focusing on endospore morphogenesis from induction through mature layered architecture. It highlights where evidence is strong versus upstream, taxon-specific, or indirect.*

## 5. Evidence-backed edge proposals

| # | Subject–predicate–object | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | Nutrient starvation —promotes→ sporulation initiation | Voitsekhovsky et al., 2024, DOI:10.15407/microbiolj86.04.091 | “Starvation—a decrease in growth substrates—is established as the starting signal for sporulation.” | **Uncertain/upstream.** The same review says mechanisms by which environmental variables act remain debatable; do not encode starvation as directly causing shape (voitsekhovsky2024peculiaritiesofthe pages 1-3). |
| 2 | Polar septation —creates→ smaller forespore and larger mother cell | Khanna et al., 2020, DOI:10.1146/annurev-micro-022520-074650 | “Stage II marks the formation of the polar septum, creating the smaller forespore and the larger mother cell.” | Strong developmental edge in *B. subtilis*; septation alone is insufficient for mature morphology (khanna2020shapinganendospore pages 2-4). |
| 3 | SpoIIIE —translocates→ chromosome into forespore | Khanna et al., 2020 | “The trapped chromosome is actively transported to the forespore by the SpoIIIE translocation complex.” | Strong in *B. subtilis* but indirect to outer shape (khanna2020shapinganendospore pages 2-4). |
| 4 | SpoIIDMP complex —enables→ engulfment membrane migration | Khanna et al., 2019, DOI:10.7554/eLife.45257 | SpoIIP-deficient cells produced no finger-like projections and showed no membrane movement; loss of any DMP component blocks migration. | **High confidence, direct mutant microscopy/cryo-ET**, *B. subtilis* (khanna2019themoleculararchitecture pages 10-12, khanna2020shapinganendospore pages 9-11). |
| 5 | New peptidoglycan synthesis —supports→ engulfing-membrane projections | Khanna et al., 2019 | PG-synthesis inhibitors “reduced or eliminated projections.” | High-confidence experimental perturbation; the exact molecular coupling to DMP remains a mechanistic model (khanna2019themoleculararchitecture pages 10-12, khanna2019themoleculararchitecture pages 4-5). |
| 6 | SpoIIDMP —degrades/tethers to→ newly synthesized septal peptidoglycan | Khanna et al., 2019 | DMP complexes were localized at the leading edge and proposed to tether the membrane while degrading new PG. | **Model-supported**, not a purely morphological observation; retain the qualifier “proposed” if the schema permits (khanna2019themoleculararchitecture pages 13-14). |
| 7 | Engulfment —remodels→ hemispherical forespore into ovoid forespore | Khanna et al., 2020 | During engulfment, the forespore “remodels from hemispherical to ovoid and doubles in size.” | Strong developmental summary; directly relevant to shape (khanna2020shapinganendospore pages 9-11). |
| 8 | Cortex peptidoglycan —assembles between→ inner and outer forespore membranes | McKenney et al., 2013, DOI:10.1038/nrmicro2921 | “The cortex is composed of peptidoglycan and is assembled between the inner and outer forespore membranes.” | High-confidence structural edge across canonical endospores (mckenney2013thebacillussubtilis pages 2-4). |
| 9 | Mother-cell coat proteins —encase→ forespore surface | McKenney et al., 2013 | “The coat is composed of at least 70 individual proteins” that begin localizing during engulfment. | High in *B. subtilis*; the count and composition should not be generalized to every taxon (mckenney2013thebacillussubtilis pages 2-4). |
| 10 | SpoIVA —tethers/organizes→ nascent coat layers at outer forespore membrane | Bauda et al., 2024, DOI:10.1038/s41467-024-45770-6 | “In the absence of SpoIVA…all the nascent coat layers are mislocalized.” | **High-confidence direct TEM mutant edge**, *B. subtilis* (bauda2024ultrastructureofmacromolecular pages 5-7). |
| 11 | SpoIVA loss —causes→ abnormal cortex, coat, exosporium, and heteromorphic immature spores | Kuwana et al., 2024, DOI:10.3389/fmicb.2024.1338751 | “Immature and heteromorphic spores” were observed; “no cortex structure” and abnormal coat/exosporium occurred in the mutant. | **High-confidence, direct TEM and light microscopy**, *C. sporogenes* NBRC 14293 (kuwana2024spoivaisan pages 8-9). |
| 12 | SpoVID —contributes to→ thin-dark and thick-dark coat matrices / encasement | Bauda et al., 2024 | “The thin dark matrix is not observed in ΔspoVID” and the thick dark matrix forms additional strata. | High for the observed *B. subtilis* matrices; mapping those matrices to universal named layers is partly interpretive (bauda2024ultrastructureofmacromolecular pages 5-7). |
| 13 | SafA —required for proper assembly of→ thick-dark matrix / inner coat | Bauda et al., 2024 | In Δ`safA`, the thick dark matrix was “either absent or mislocalized as a large aggregate.” | High direct mutant evidence in *B. subtilis*; “inner coat” mapping comes from synthesis with prior literature (bauda2024ultrastructureofmacromolecular pages 7-9, bauda2024ultrastructureofmacromolecular pages 5-7). |
| 14 | CotE —required for→ bead-like coat layers | Bauda et al., 2024 | “In the absence of CotE…bead-like patterns are absent.” | High direct mutant cryo-ET/TEM evidence; likely outer-coat organization in *B. subtilis* (bauda2024ultrastructureofmacromolecular pages 5-7). |
| 15 | Dehydrated core + cortex + coat ± exosporium —constitutes→ mature spore-shaped morphology | McKenney et al., 2013; Kuwana et al., 2024 | Mature spores contain a dehydrated core surrounded by cortex and coat; *C. sporogenes* additionally showed an attached exosporium. | Recommended terminal edge to **METPO:1000682**. Exosporium must be optional because it is taxon-dependent (mckenney2013thebacillussubtilis pages 2-4, kuwana2024spoivaisan pages 8-9). |

### Provisional edges requiring more primary evidence

- **SpoVE —participates in→ cortex glycan synthesis.**
- **SpoVD —participates in→ cortex peptidoglycan polymerization/cross-linking.**
- **SpoVM —anchors/recruits→ SpoIVA at curved forespore membrane.**
- **Spo0A~P —initiates→ sporulation transcriptional program.**

These relationships are biologically well established, but the retrieved evidence set did not supply enough direct, edge-specific primary text to meet the requested stringent quote-and-reference standard. They should be added only after attaching the relevant primary papers.

## 6. Recent developments and quantitative findings

### 2024 in situ structural resolution

Bauda et al. combined cryo-focused-ion-beam milling, cryo-electron tomography, and TEM to resolve early *B. subtilis* coat architecture. Forespore DNA formed a toroid containing approximately **5.5-nm fibers**. The authors distinguished seven stained or structured coat regions. Four amorphous matrices measured **3.2 ± 0.2 nm**, **8.9 ± 0.8 nm**, **17.8 ± 3.7 nm**, and **22.5 ± 4.5 nm** thick. CotE-dependent structured layers occurred approximately **55 nm** from the outer forespore membrane. Mutants separated SpoIVA-, SpoVID-, SafA-, and CotE-dependent architectural contributions (bauda2024ultrastructureofmacromolecular pages 7-9, bauda2024ultrastructureofmacromolecular pages 5-7, bauda2024ultrastructureofmacromolecular pages 1-2).

This study substantially refines the older three-layer description. However, the seven “regions” are experimentally distinguished density/staining classes, not yet seven universally conserved biological layers. The authoritative interpretation is therefore to curate them as assay-specific ultrastructural nodes and connect them to proteins only in the *B. subtilis* context.

### 2024 cross-taxon SpoIVA validation

Kuwana et al. showed that SpoIVA is an essential morphogenetic protein in anaerobic *C. sporogenes* NBRC 14293. Wild-type 24-hour cultures produced approximately **10⁸ heat- and lysozyme-resistant spores per mL**. In the mutant, **59.6%** of scored cells accumulated at stages IV–V versus **13.6%** in wild type, whereas stage-VI cells fell from **62.1%** to **13.5%**. TEM showed absent or abnormally thin cortex, malformed surface layers, nondehydrated cores, and heteromorphic immature spores (kuwana2024spoivaisan pages 8-9).

This provides valuable cross-taxon support for a conserved high-level edge—**SpoIVA promotes normal endospore morphogenesis**—while also documenting important architectural differences: mature *C. sporogenes* spores lacked the lamellar structures seen in *B. subtilis* and *C. difficile* (kuwana2024spoivaisan pages 8-9).

## 7. Applications and real-world relevance

1. **Food sterilization and spoilage control.** Endospore morphology is coupled to cortex and coat integrity, which contributes to heat, enzyme, desiccation, and chemical resistance. Morphogenesis genes such as `spoIVA` are therefore candidate intervention points for reducing formation of resistant spores in anaerobic food-spoilage or botulism-related lineages. The *C. sporogenes* result is particularly relevant because the organism is genetically related to Group-I *C. botulinum* but lacks toxin genes (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 8-9).

2. **Clinical infection control.** Durable spores drive environmental persistence and recurrence of infections caused by spore-forming pathogens. Nonetheless, edges from coat genes to disease transmission should not be inserted into this morphology graph without pathogen-specific evidence.

3. **Spore-surface display and delivery.** The stable coat architecture is used as an antigen- or cargo-display scaffold in *B. subtilis*. This application depends on predictable coat localization and robust dormant particles, but engineered surface display is downstream of coat morphology and should be represented in a separate application graph.

4. **Microscopy-based phenotyping and strain annotation.** Phase-contrast microscopy can stage sporulation, while TEM and cryo-ET establish cortex, coat, exosporium, and shape directly. High-throughput TraitMech evidence should favor morphology-confirming imaging over resistance-only readouts.

5. **Environmental and industrial sporulation control.** Medium composition, pH, temperature, aeration, minerals, and metabolites can alter sporulation yield. A 2024 review concludes that these factors are well documented but their mechanisms remain debated; consequently, they belong upstream of sporulation initiation and should not be asserted as direct determinants of the final shape (voitsekhovsky2024peculiaritiesofthe pages 1-3).

## 8. Expert analysis and recommended YAML strategy

A defensible first revision of `data/traits/morphology/spore_shaped.yaml` should be **modular and taxon-qualified**:

1. **Core developmental module:** polar septation → forespore; SpoIIIE → chromosome transfer; SpoIIDMP plus new PG → engulfment; engulfment → ovoid double-membrane forespore.
2. **Envelope module:** cortex synthesis plus coat encasement → layered endospore body.
3. **Morphogenetic layer module:** SpoIVA → coat tethering; SpoVID → encasement/matrix organization; SafA → inner-coat-associated matrix; CotE → outer structured layers.
4. **Terminal phenotype:** layered, dormant endospore body → **METPO:1000682**.
5. **Optional taxon modules:** crust in *B. subtilis*; exosporium in selected Bacillales and Clostridia.
6. **Separate proxy branch:** mature morphology → often associated with phase brightness and resistance, but never infer the morphology solely from those proxies.

This organization is preferable to a single linear pathway because endospore shape is an emergent developmental phenotype. Engulfment establishes geometry, cortex deposition stabilizes the body, and coat morphogenesis encases it. Mutations can disrupt one layer, arrest maturation, or mislocalize material without producing identical phenotypes.

## 9. Warnings: claims not yet suitable for TraitMech curation

- **Do not curate “starvation directly causes spore-shaped morphology.”** It promotes initiation, and its mechanism varies with medium and taxon (voitsekhovsky2024peculiaritiesofthe pages 1-3).
- **Do not equate heat or lysozyme resistance with METPO:1000682.** Resistance is a maturation-associated function and may reflect several structures.
- **Do not generalize the seven 2024 ultrastructural regions to all endospores.** They were resolved in *B. subtilis* under specific mutant/staging conditions (bauda2024ultrastructureofmacromolecular pages 5-7).
- **Do not require an exosporium.** Its presence is species-dependent; *B. subtilis* has a crust, whereas many other spores have an exosporium or neither clearly resolved structure (mckenney2013thebacillussubtilis pages 2-4).
- **Do not transfer individual coat-protein functions unqualified across Bacillus and Clostridium.** Basic morphological transformations are conserved, but genetic regulation and coat composition differ substantially (kuwana2024spoivaisan pages 8-9, mckenney2013thebacillussubtilis pages 11-13).
- **Do not curate SpoVE or SpoVD edges from this report as high confidence** until direct primary cortex-biogenesis evidence is attached.
- **Do not assign CURIEs to the newly described light/dark matrices.** No stable ontology identifiers were established in the retrieved literature.
- **Verify all candidate GO, CHEBI, NCBITaxon, and UniProt records against the project’s ontology release** before committing YAML. Protein accessions must be strain- and species-specific.

## 10. DOI-first bibliography

1. **Bauda E, et al.** “Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography.” *Nature Communications* 15, 1376. **Published February 2024.** DOI: [10.1038/s41467-024-45770-6](https://doi.org/10.1038/s41467-024-45770-6) (bauda2024ultrastructureofmacromolecular pages 7-9, bauda2024ultrastructureofmacromolecular pages 5-7).
2. **Kuwana R, Dupuy B, Martin-Verstraete I, Takamatsu H.** “SpoIVA is an essential morphogenetic protein for the formation of heat- and lysozyme-resistant spores in *Clostridium sporogenes* NBRC 14293.” *Frontiers in Microbiology* 15. **Published April 2024.** DOI: [10.3389/fmicb.2024.1338751](https://doi.org/10.3389/fmicb.2024.1338751) (kuwana2024spoivaisan pages 1-2, kuwana2024spoivaisan pages 8-9).
3. **Voitsekhovsky VG, et al.** “Peculiarities of the Ontogenesis of Bacilli During Development from a Vegetative Cell to a Spore.” *Mikrobiolohichnyi Zhurnal* 86:91–105. **Published September 2024.** DOI: [10.15407/microbiolj86.04.091](https://doi.org/10.15407/microbiolj86.04.091) (voitsekhovsky2024peculiaritiesofthe pages 1-3).
4. **Khanna K, Lopez-Garrido J, Pogliano K.** “Shaping an Endospore: Architectural Transformations During *Bacillus subtilis* Sporulation.” *Annual Review of Microbiology* 74:361–386. **Published September 2020.** DOI: [10.1146/annurev-micro-022520-074650](https://doi.org/10.1146/annurev-micro-022520-074650) (khanna2020shapinganendospore pages 1-2, khanna2020shapinganendospore pages 2-4).
5. **Khanna K, et al.** “The molecular architecture of engulfment during *Bacillus subtilis* sporulation.” *eLife* 8:e45257. **Published July 2019.** DOI: [10.7554/eLife.45257](https://doi.org/10.7554/eLife.45257) (khanna2019themoleculararchitecture pages 10-12, khanna2019themoleculararchitecture pages 4-5).
6. **McKenney PT, Driks A, Eichenberger P.** “The *Bacillus subtilis* endospore: assembly and functions of the multilayered coat.” *Nature Reviews Microbiology* 11:33–44. **Published December 2012 for the January 2013 issue.** DOI: [10.1038/nrmicro2921](https://doi.org/10.1038/nrmicro2921) (mckenney2013thebacillussubtilis pages 11-13, mckenney2013thebacillussubtilis pages 2-4).

## Curation conclusion

The strongest graph backbone is **developmental geometry plus envelope assembly**, not a generic “sporulation causes spore shape” edge. The highest-confidence causal entities are polar septation, SpoIIIE, the SpoIIDMP engulfment complex, newly synthesized peptidoglycan, cortex, coat, SpoIVA, SpoVID, SafA, and CotE. The terminal phenotype should require an ovoid/ellipsoidal differentiated endospore body with cortex and coat, while treating exosporium, crust, resistance, and phase brightness as optional structures or associated traits.

References

1. (khanna2020shapinganendospore pages 1-2): Kanika Khanna, Javier Lopez-Garrido, and Kit Pogliano. Shaping an endospore: architectural transformations during <i>bacillus subtilis</i> sporulation. Annual Review of Microbiology, 74:361-386, Sep 2020. URL: https://doi.org/10.1146/annurev-micro-022520-074650, doi:10.1146/annurev-micro-022520-074650. This article has 103 citations and is from a peer-reviewed journal.

2. (mckenney2013thebacillussubtilis pages 2-4): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 883 citations and is from a highest quality peer-reviewed journal.

3. (khanna2020shapinganendospore pages 2-4): Kanika Khanna, Javier Lopez-Garrido, and Kit Pogliano. Shaping an endospore: architectural transformations during <i>bacillus subtilis</i> sporulation. Annual Review of Microbiology, 74:361-386, Sep 2020. URL: https://doi.org/10.1146/annurev-micro-022520-074650, doi:10.1146/annurev-micro-022520-074650. This article has 103 citations and is from a peer-reviewed journal.

4. (kuwana2024spoivaisan pages 1-2): Ritsuko Kuwana, Bruno Dupuy, Isabelle Martin-Verstraete, and Hiromu Takamatsu. Spoiva is an essential morphogenetic protein for the formation of heat- and lysozyme-resistant spores in clostridium sporogenes nbrc 14293. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1338751, doi:10.3389/fmicb.2024.1338751. This article has 5 citations and is from a peer-reviewed journal.

5. (kuwana2024spoivaisan pages 8-9): Ritsuko Kuwana, Bruno Dupuy, Isabelle Martin-Verstraete, and Hiromu Takamatsu. Spoiva is an essential morphogenetic protein for the formation of heat- and lysozyme-resistant spores in clostridium sporogenes nbrc 14293. Frontiers in Microbiology, Apr 2024. URL: https://doi.org/10.3389/fmicb.2024.1338751, doi:10.3389/fmicb.2024.1338751. This article has 5 citations and is from a peer-reviewed journal.

6. (khanna2019themoleculararchitecture pages 10-12): Kanika Khanna, Javier Lopez-Garrido, Ziyi Zhao, Reika Watanabe, Yuan Yuan, Joseph Sugie, Kit Pogliano, and Elizabeth Villa. The molecular architecture of engulfment during bacillus subtilis sporulation. Jul 2019. URL: https://doi.org/10.7554/elife.45257, doi:10.7554/elife.45257. This article has 59 citations and is from a domain leading peer-reviewed journal.

7. (khanna2020shapinganendospore pages 9-11): Kanika Khanna, Javier Lopez-Garrido, and Kit Pogliano. Shaping an endospore: architectural transformations during <i>bacillus subtilis</i> sporulation. Annual Review of Microbiology, 74:361-386, Sep 2020. URL: https://doi.org/10.1146/annurev-micro-022520-074650, doi:10.1146/annurev-micro-022520-074650. This article has 103 citations and is from a peer-reviewed journal.

8. (khanna2019themoleculararchitecture pages 13-14): Kanika Khanna, Javier Lopez-Garrido, Ziyi Zhao, Reika Watanabe, Yuan Yuan, Joseph Sugie, Kit Pogliano, and Elizabeth Villa. The molecular architecture of engulfment during bacillus subtilis sporulation. Jul 2019. URL: https://doi.org/10.7554/elife.45257, doi:10.7554/elife.45257. This article has 59 citations and is from a domain leading peer-reviewed journal.

9. (khanna2019themoleculararchitecture pages 4-5): Kanika Khanna, Javier Lopez-Garrido, Ziyi Zhao, Reika Watanabe, Yuan Yuan, Joseph Sugie, Kit Pogliano, and Elizabeth Villa. The molecular architecture of engulfment during bacillus subtilis sporulation. Jul 2019. URL: https://doi.org/10.7554/elife.45257, doi:10.7554/elife.45257. This article has 59 citations and is from a domain leading peer-reviewed journal.

10. (mckenney2013thebacillussubtilis pages 24-26): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 883 citations and is from a highest quality peer-reviewed journal.

11. (voitsekhovsky2024peculiaritiesofthe pages 1-3): V.G. Voitsekhovsky, L.V. Avdeeva, O.B. Balko, and O.I. Balko. Peculiarities of the ontogenesis of bacilli during development from a vegetative cell to a spore. Mikrobiolohichnyi Zhurnal, 86:91-105, Sep 2024. URL: https://doi.org/10.15407/microbiolj86.04.091, doi:10.15407/microbiolj86.04.091. This article has 0 citations.

12. (bauda2024ultrastructureofmacromolecular pages 5-7): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (mckenney2013thebacillussubtilis pages 11-13): Peter T. McKenney, Adam Driks, and Patrick Eichenberger. The bacillus subtilis endospore: assembly and functions of the multilayered coat. Nature Reviews Microbiology, 11:33-44, Dec 2013. URL: https://doi.org/10.1038/nrmicro2921, doi:10.1038/nrmicro2921. This article has 883 citations and is from a highest quality peer-reviewed journal.

14. (bauda2024ultrastructureofmacromolecular pages 7-9): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 20 citations and is from a highest quality peer-reviewed journal.

15. (bauda2024ultrastructureofmacromolecular pages 1-2): Elda Bauda, Benoit Gallet, Jana Moravcova, Gregory Effantin, Helena Chan, Jiri Novacek, Pierre-Henri Jouneau, Christopher D. A. Rodrigues, Guy Schoehn, Christine Moriscot, and Cecile Morlot. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45770-6, doi:10.1038/s41467-024-45770-6. This article has 20 citations and is from a highest quality peer-reviewed journal.