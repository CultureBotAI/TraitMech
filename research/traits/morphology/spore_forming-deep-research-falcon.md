---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:59:42.547418'
end_time: '2026-08-04T10:06:09.552292'
duration_seconds: 387.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spore forming
  trait_identifier: METPO:1000871
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spore_forming
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A sporulation in which an organism has the ability to produce endospores.
  parent_traits: METPO:1000870
  synonyms: spore, yes
  evidence_summary: 'DOI:10.1038/nrmicro2921: production of a highly resistant dormant
    cell type known as the spore (Supports spore forming as the ability to produce
    dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis
    (Organism example: Bacillus subtilis is described as endospore-forming.)'
  causal_graph_summary: 'spore_forming_endospore_assembly: 15 nodes, 11 edges'
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
- **Trait label:** spore forming
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000871
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism has the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** spore, yes
- **Existing evidence:** DOI:10.1038/nrmicro2921: production of a highly resistant dormant cell type known as the spore (Supports spore forming as the ability to produce dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis (Organism example: Bacillus subtilis is described as endospore-forming.)
- **Existing causal graph summary:** spore_forming_endospore_assembly: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_forming.yaml`.

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
- **Trait label:** spore forming
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000871
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A sporulation in which an organism has the ability to produce endospores.
- **Parent traits:** METPO:1000870
- **Synonyms:** spore, yes
- **Existing evidence:** DOI:10.1038/nrmicro2921: production of a highly resistant dormant cell type known as the spore (Supports spore forming as the ability to produce dormant resistant spores.) | PMID:32660383: Endospore formation in Bacillus subtilis (Organism example: Bacillus subtilis is described as endospore-forming.)
- **Existing causal graph summary:** spore_forming_endospore_assembly: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **spore forming** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spore_forming.yaml`.

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


# Curation-focused research report: spore forming

## Executive summary

**Target:** `METPO:1000871` — **spore forming**; category **MORPHOLOGY**; term kind **CLASS**; mapping **REVIEWED**.

For TraitMech, this trait should mean the **genetically encoded capacity of a bacterium to complete endosporulation and produce a mature, dormant endospore**, not merely the observation of a refractile body, survival after heating, or expression of one sporulation gene. Endosporulation is a developmental program involving asymmetric division, forespore engulfment, compartment-specific transcription, cortex and coat assembly, core dehydration/mineralization, maturation, and release from the mother cell. The end product is usually highly resistant, but resistance is a consequence of several structures and core properties rather than the definition of spore formation itself. Recent work reinforces that the canonical *Bacillus subtilis* pathway is a powerful reference model but is not universally portable to Clostridia. (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2, galperin2022conservationandevolution pages 18-20)

## 1. Trait scope and boundary cases

### In scope

The positive phenotype is the capacity to produce an **endospore inside a mother-cell sporangium**. A defensible positive assay should demonstrate mature endospores by microscopy or ultrastructure, recovery of resistant spores followed by germination/outgrowth, or completion of the characteristic developmental sequence. In *Clostridioides difficile*, this sequence includes asymmetric division, engulfment, cortex/coat/exosporium deposition, mother-cell lysis, and release of the mature spore. (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2)

The trait is best represented as a **capacity**, because vegetative cells grown under nutrient-rich conditions may be phenotypically “not sporulating” even though the organism is genetically spore forming. Nutrient deprivation commonly triggers development, but temperature, pH, aeration, culture medium, cell density, and taxon-specific signals alter penetrance and timing.

### Out of scope or requiring separation

1. **Fungal spores and actinobacterial exospores:** these arise through developmentally and evolutionarily distinct pathways. They should not be merged into this endospore trait.
2. **Germination:** germination is the return of a dormant spore to metabolic activity; it is downstream of, and distinct from, spore-forming capacity.
3. **Dormancy, persistence, and VBNC states:** these do not require asymmetric septation, engulfment, cortex, or coat biogenesis.
4. **Heat or disinfectant resistance alone:** resistance is multifactorial and can vary among spores; survival alone is not proof of endospore morphogenesis.
5. **Partial sporulation:** asymmetric septa, phase-bright intermediates, or activation of Spo0A/sigma factors do not establish production of mature viable spores.
6. **Genomic prediction alone:** presence of `spo0A` or a subset of sporulation genes is insufficient. A 2022 comparative study found sporulation-associated genes in non-spore-formers and widespread lineage-specific gene loss. (galperin2022conservationandevolution pages 18-20)

## 2. Candidate graph nodes

Ontology identifiers below are limited to mappings that can be stated conservatively. Nodes for which an exact ontology term was not verified should remain **label-only** pending ontology lookup.

### Trait and taxa

- **spore forming:** `METPO:1000871`
- **parent trait:** `METPO:1000870`
- *Bacillus subtilis*: `NCBITaxon:1423`
- *Clostridioides difficile*: `NCBITaxon:1496`
- Bacillota/Firmicutes: use the current NCBI Taxonomy identifier after curator verification; nomenclature has changed.

### Environmental and experimental inputs

- nutrient deprivation/starvation — label-only candidate
- stationary phase — `GO:0070285` may be considered only if it matches the intended bacterial stationary-phase concept
- temperature, pH, aeration, medium composition, cell density — contextual experimental-factor nodes
- oxygen exposure — especially relevant to transmission by anaerobic Clostridia
- sporulation-inducing medium and incubation time — assay metadata, not intrinsic trait nodes

### Regulators and pathways

- Spo0A and phosphorylated Spo0A (`Spo0A~P`) — master response regulator/state node
- *Bacillus* phosphorelay: KinA/KinB → Spo0F → Spo0B → Spo0A
- orphan histidine kinases and phosphatases — Clostridia-specific candidates
- Rap phosphatases, including RapP — *B. subtilis*-specific regulatory candidates
- sigma factors σF/SigF, σE/SigE, σG/SigG, σK/SigK
- SpoIIE, SpoIIAA/SpoIIAB — forespore σF-control module
- SpoIIR and pro-σE processing machinery — intercompartmental signaling module
- SpoIIIA–SpoIIQ channel — label-only candidate pending edge-specific evidence
- SpoIVB-family proteases and SpoIVFB/BofA/SpoIVFA — late σK-control candidates
- SpoVT — forespore transcriptional regulator

### Morphogenesis machinery and processes

- asymmetric septation
- forespore and mother-cell compartments
- chromosome translocation/SpoIIIE
- forespore engulfment
- membrane fission
- cortex peptidoglycan biosynthesis
- coat and crust/exosporium assembly
- spore maturation
- mother-cell lysis and mature-spore release

### Structural and chemical nodes

- cortex peptidoglycan; muramic-δ-lactam
- spore coat and exosporium
- spore core and inner membrane
- calcium dipicolinate/CaDPA — use verified ChEBI mappings for calcium and dipicolinic acid rather than inventing a complex identifier
- dipicolinic acid/pyridine-2,6-dicarboxylic acid — verify exact ChEBI CURIE before curation
- low core water content/core dehydration
- 3-phosphoglycerate energy reserve — candidate `CHEBI:17794`, requiring curator verification

### Proteins and modules involved in maturation/resistance

- SpoVA proteins, including SpoVAD/SpoVAE — CaDPA transport/accumulation module
- small acid-soluble spore proteins (SASPs)
- SspA and SspB — especially the *C. difficile* paralogs
- SpoIVB2 — *C. difficile*-specific late-sporulation candidate
- cortex synthases/remodeling enzymes — SpoVD, SpoVE, SpoVB and taxon-specific homologs
- coat morphogenetic proteins — SpoIVA, SipL, CotE and others; taxon-specificity must be retained
- photoproduct lyase — DNA repair/resistance node

## 3. Candidate causal edges

The compact graph below is suitable as a starting point, but its taxonomic qualifiers must be retained.

| subject | predicate | object | taxonomic scope | confidence |
|---|---|---|---|---|
| nutrient deprivation | promotes | Spo0A phosphorylation | Bacillus subtilis model; nutrient-linked initiation broadly supported in endospore formers (nerber2024thesmallacidsoluble pages 1-2) | medium |
| Spo0A~P | activates | sporulation entry program | Bacillus and Clostridioides/Clostridia; master regulator conserved function with initiation-system differences (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | high |
| Spo0A-dependent sporulation program | causes | asymmetric septation | Bacillus model; broadly conserved early morphogenesis step (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | medium |
| asymmetric septation | establishes | forespore and mother cell compartments | broadly described for endospore formation; shown in C. difficile and Bacillus literature (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | high |
| sigma factor σF | promotes | forespore program and engulfment completion | C. difficile evidence; Bacillus-model-consistent cascade (nerber2024thesmallacidsoluble pages 1-2) | high |
| sigma factor σE | promotes | mother-cell program and proper asymmetric septation | C. difficile evidence; role wording kept cautious across taxa (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | medium |
| engulfment | enables | sigma factor σG activation | Bacillus model and C. difficile-consistent late sporulation logic (nerber2024thesmallacidsoluble pages 1-2) | medium |
| sigma factor σG | promotes | membrane fission and cortex formation | C. difficile evidence; likely not universally identical in detail (nerber2024thesmallacidsoluble pages 1-2) | medium |
| sigma factor σK | promotes | coat layer formation | C. difficile evidence; late mother-cell program broadly conserved (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | high |
| SpoVA proteins | import | Ca-dipicolinic acid into developing forespore/spore core | Bacillus and Clostridioides evidence summarized in recent literature (nerber2024thesmallacidsoluble pages 27-28, setlow2023newthoughtson pages 1-2) | medium |
| SASPs | protect | spore DNA | broad endospore resistance mechanism across Firmicutes (nerber2024thesmallacidsoluble pages 1-2, setlow2023newthoughtson pages 1-2) | high |
| SspA/SspB | promote | cortex formation via SpoIVB2-associated mechanism | Clostridioides difficile specific (nerber2024thesmallacidsoluble pages 1-2) | high |
| cortex peptidoglycan | promotes | spore resistance | broad endospore mechanism; resistance is multifactorial (nerber2024thesmallacidsoluble pages 1-2, setlow2023newthoughtson pages 1-2) | medium |
| low core water content | promotes | heat resistance and dormancy-associated resilience | broad endospore mechanism, especially Bacillus-derived biophysics (setlow2023newthoughtson pages 2-4, setlow2023newthoughtson pages 1-2) | high |
| Ca-dipicolinic acid | promotes | core dehydration and resistance | broad endospore mechanism; exact contribution can vary by stress and taxon (nerber2024thesmallacidsoluble pages 1-2, setlow2023newthoughtson pages 1-2) | medium |
| spore coat | promotes | exclusion of damaging macromolecules and resistance | broad endospore mechanism (setlow2023newthoughtson pages 1-2) | high |
| low-permeability inner membrane | promotes | chemical resistance of the spore core | broad endospore mechanism (setlow2023newthoughtson pages 14-16, setlow2023newthoughtson pages 1-2) | high |
| mother-cell lysis | releases | mature endospore | broadly described; directly noted for C. difficile (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | high |


*Table: This table lists compact candidate subject-predicate-object edges for curating the spore-forming trait METPO:1000871. It emphasizes the staged developmental logic of endospore formation while flagging Bacillus-model and C. difficile-specific claims.*

### Evidence notes and supporting snippets

| Proposed triple | Reference and supporting snippet | Curation note |
|---|---|---|
| nutrient deprivation → promotes → Spo0A phosphorylation | Nerber et al., 2024: sporulation “initiates upon Spo0A phosphorylation in response to nutrient deprivation.” DOI: [10.1371/journal.ppat.1012507](https://doi.org/10.1371/journal.ppat.1012507), published August 2024. (nerber2024thesmallacidsoluble pages 1-2) | Curate with a taxonomic qualifier. The signal-transduction route differs between *Bacillus* and Clostridia. |
| Spo0A~P → activates → sporulation entry | Spo0A is described as the master regulatory protein governing entry into sporulation; phosphorylated Spo0A initiates the *C. difficile* program. (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | Strong conserved high-level edge; do not encode one universal upstream kinase pathway. |
| asymmetric septation → establishes → mother cell and forespore | The 2024 studies describe asymmetric division producing distinct mother-cell and forespore compartments. (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | Strong morphogenetic edge applicable broadly to canonical endosporulation. |
| σF → promotes → engulfment/cortex program | In *C. difficile*, loss of σF “blocks engulfment and cortex formation.” (nerber2024thesmallacidsoluble pages 1-2) | A loss-of-function result supports necessity, but phrase the positive edge as “promotes” rather than “directly activates.” |
| σE → promotes → mother-cell development/asymmetric septation | Loss of σE blocks asymmetric septation in the summarized *C. difficile* evidence; σE is mother-cell specific. (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | Potential timing issue: canonical *Bacillus* σE activation follows septation. Keep this edge *C. difficile*-specific or inspect the full experiment before curation. |
| engulfment → enables → σG activation | Recent *B. subtilis* work states that the cell-within-a-cell state created by engulfment is required for activation of late forespore σG. | Strong in the *B. subtilis* model; avoid universalizing without taxon-specific confirmation. |
| σG → promotes → membrane fission and cortex formation | In *C. difficile*, σG loss prevents membrane fission and cortex formation. (nerber2024thesmallacidsoluble pages 1-2) | Curate as taxon-specific necessity evidence. |
| σK → promotes → coat-layer formation | In *C. difficile*, σK loss prevents coat formation despite successful engulfment and cortex assembly. (nerber2024thesmallacidsoluble pages 1-2) | Strong stage-specific edge in *C. difficile*. |
| SpoVA proteins → promote/import → CaDPA accumulation in developing spores | Recent literature cites SpoVAD and SpoVAE as required for CaDPA uptake into spores. (nerber2024thesmallacidsoluble pages 27-28) | Use “required for” or “promotes transport” unless direct transporter activity is established for the exact protein/taxon. |
| SASPs → protect → spore DNA | The 2023 authoritative review identifies SASP saturation of DNA as central to radiation, dry-heat, and chemical resistance. DOI: [10.1128/mmbr.00080-22](https://doi.org/10.1128/mmbr.00080-22), June 2023. (setlow2023newthoughtson pages 1-2) | Strong resistance edge, but resistance is downstream of spore formation rather than evidence of morphogenesis. |
| SspA/SspB → promote → cortex formation | Nerber et al. report that *C. difficile* `sspA` and `sspB` are required for cortex formation and UV protection. (nerber2024thesmallacidsoluble pages 1-2) | Strong, explicitly *C. difficile*-specific edge. |
| SspA/SspB → regulate through → SpoIVB2 | `spoIVB2` mutations suppress sporulation defects of SASP mutants, revealing a genetic connection. (nerber2024thesmallacidsoluble pages 1-2) | **Uncertain direction/mechanism:** suppression supports epistasis, not necessarily direct transcriptional regulation. Do not curate a direct binding edge yet. |
| low core water → promotes → heat resistance/dormancy | Spore core water is approximately 25% of wet weight versus approximately 80% after germination; reduced water immobilizes macromolecules and limits denaturation/aggregation. (setlow2023newthoughtson pages 2-4, setlow2023newthoughtson pages 1-2) | Strong biophysical edge, largely derived from *Bacillus*. |
| spore coat → excludes → macromolecules ≥10 kDa | The coat impedes passage of moieties of at least 10 kDa. (setlow2023newthoughtson pages 1-2) | Quantitative and curatable as a resistance mechanism, not a defining morphogenesis edge. |
| low-permeability inner membrane → limits → chemical entry into core | The compressed, low-fluidity inner membrane is described as the principal barrier to diffusion of damaging chemicals into the core. (setlow2023newthoughtson pages 1-2) | Strong expert-review support; molecular determinants remain incompletely resolved. |
| mother-cell lysis → releases → mature endospore | Both 2024 *C. difficile* studies describe lysis of the mother cell and mature-spore release. (nerber2024thesmallacidsoluble pages 1-2, cassona2024sporesofclostridioides pages 1-2) | Strong endpoint edge. |

## 4. Recommended causal-graph organization

A useful TraitMech graph should separate four modules:

1. **Commitment/initiation:** environmental state → taxon-specific phosphosignaling → Spo0A~P.
2. **Morphogenesis:** Spo0A program → asymmetric septation → forespore/mother-cell differentiation → engulfment and membrane fission.
3. **Compartment-specific gene expression:** σF/σG in the forespore and σE/σK in the mother cell, with intercompartmental checkpoints.
4. **Maturation and output:** cortex + coat/exosporium + SpoVA/CaDPA + SASPs → mature dormant resistant spore → mother-cell lysis/release.

This modular representation is preferable to a single linear chain. Sporulation includes checkpoints, feed-forward regulation, intercompartmental signaling, and parallel structural programs.

## 5. Recent developments and quantitative evidence

### 2024: SASPs participate in morphogenesis, not only DNA protection

Nerber et al. showed that *C. difficile* SspA and SspB are required for formation of the cortex, extending their role beyond classical UV protection. Suppressor mutations in `spoIVB2` connect SASPs genetically to a late-sporulation protease pathway. This is a significant mechanistic update, but the proposed gene-regulatory mechanism remains a hypothesis rather than a demonstrated direct interaction. The paper also reports a public-health context of approximately **220,000 U.S. infections and 13,000 deaths annually** from *C. difficile*. (nerber2024thesmallacidsoluble pages 1-2)

### 2024: spores can carry virulence factors

Cassona et al. detected TcdA at the *C. difficile* spore surface and found that toxin-locus expression can occur in sporulating cells. Forespore expression is controlled by σG and SpoVT, while persistent whole-sporangium expression can originate from σD-dependent vegetative transcription. The resulting cytopathic activity indicates that mature spores can function as toxin-delivery vehicles, linking sporulation directly to early host interaction rather than only environmental transmission. DOI: [10.1038/s42003-024-06521-x](https://doi.org/10.1038/s42003-024-06521-x), published July 2024. (cassona2024sporesofclostridioides pages 1-2)

### 2023: resistance is a distributed systems property

Setlow and Christie argue that there is no single “spore-resistance gene.” Heat resistance depends strongly on a mineralized, gel-like core with low water; SASPs, CaDPA, photoproduct lyase, coat exclusion, and the inner-membrane permeability barrier protect against different insults. Reported values include approximately **25% core water by wet weight**, compared with **80% after germination**, and high-pressure germination over approximately **150–330 MPa**, with responses reported up to **900 MPa**. Dry spores can remain viable for at least a century under some conditions, although million-year projections are model-based extrapolations rather than observations. (setlow2023newthoughtson pages 2-4, setlow2023newthoughtson pages 14-16, setlow2023newthoughtson pages 1-2)

### Comparative genomics

Galperin et al. examined **180 firmicute genomes from 160 genera**, including **76 spore-forming species**. They catalogued **237 sporulation-associated protein families**, including 22 onset/checkpoint genes, 12 engulfment genes, 19 forespore-maturation genes, 25 mother-cell-maturation genes, nine cortex genes, eight coat/crust genes, and eight germination genes. A phylogeny based on 41 core sporulation proteins supported an early origin and predominantly vertical inheritance, while substantial lineage-specific losses explain why one fixed gene checklist cannot perfectly classify the phenotype. (galperin2022conservationandevolution pages 18-20)

## 6. Applications and real-world relevance

- **Food safety and sterilization:** heat-resistant spores from *Bacillus*, *Clostridium*, and related organisms determine thermal-process stringency and motivate high-pressure-assisted sterilization, germination-inactivation strategies, and improved sporicidal treatments. The coat and inner-membrane barriers explain why vegetative-cell antimicrobial results cannot be transferred directly to spores. (setlow2023newthoughtson pages 14-16, setlow2023newthoughtson pages 1-2)
- **Healthcare and infection control:** *C. difficile* spores tolerate oxygen and environmental insults, enabling transmission outside the anaerobic intestine. Inhibiting cortex, coat, or CaDPA maturation could render newly formed spores more susceptible to cleaning, but interventions must be validated for human safety and taxon specificity. (nerber2024thesmallacidsoluble pages 1-2)
- **Pathogenesis and surveillance:** sporulation is a transmission determinant in clostridial disease. The 2024 toxin-loading result broadens the functional interpretation of the spore surface. (cassona2024sporesofclostridioides pages 1-2)
- **Biotechnology:** the stability of *B. subtilis* spores is exploited for spore-surface display, oral/mucosal delivery, probiotics, enzyme immobilization, and agricultural inoculants. These are applications of the mature spore state; they are not causal evidence for the trait itself.
- **Evolution and microbiome transmission:** resistant endospores facilitate environmental persistence and host-to-host transfer. Sporulation loss can accompany host adaptation, so phenotype prediction should integrate complete gene modules, ecology, and experimental validation rather than taxonomic name alone. (galperin2022conservationandevolution pages 18-20)

## 7. Curation warnings

1. **Do not encode the complete *B. subtilis* phosphorelay as universal.** Clostridia may use direct Spo0A phosphorylation by orphan histidine kinases, phosphatases, partial phosphorelays, or combinations thereof.
2. **Do not infer a positive trait from `spo0A` alone.** Spo0A has regulatory roles beyond sporulation, and partial sporulation modules occur in non-spore-formers.
3. **Do not treat every σ-factor edge as taxon invariant.** Timing and dependency relationships differ between bacilli and clostridia.
4. **Do not curate SspA/SspB → direct regulation of `spoIVB2` yet.** Suppressor genetics establishes pathway interaction, not direct binding or a settled causal direction. (nerber2024thesmallacidsoluble pages 1-2)
5. **Keep germination nodes outside the core positive-trait mechanism** unless they are used to demonstrate that morphologically detected spores are mature and viable.
6. **Separate formation from resistance.** CaDPA, SASPs, core dehydration, coat, and inner membrane explain resistance phenotypes, but a strain may form structurally abnormal or poorly resistant spores.
7. **Avoid unverified CURIEs.** Gene symbols are not ontology identifiers; add UniProt, GO, ChEBI, Rhea, or taxon-specific locus IDs only after checking the exact organism and molecular entity.
8. **Require direct phenotype validation for unusual taxa.** Comparative genomics reveals extensive loss and remodeling of the sporulation gene set. (galperin2022conservationandevolution pages 18-20)

## DOI-first bibliography

1. Nerber HN, Baloh M, Brehm JN, Sorg JA. “The small acid-soluble proteins of *Clostridioides difficile* regulate sporulation in a SpoIVB2-dependent manner.” *PLOS Pathogens* 20:e1012507. **Published August 2024.** DOI: [10.1371/journal.ppat.1012507](https://doi.org/10.1371/journal.ppat.1012507). (nerber2024thesmallacidsoluble pages 1-2)
2. Cassona CP et al. “Spores of *Clostridioides difficile* are toxin delivery vehicles.” *Communications Biology* 7. **Published July 2024.** DOI: [10.1038/s42003-024-06521-x](https://doi.org/10.1038/s42003-024-06521-x). (cassona2024sporesofclostridioides pages 1-2)
3. Setlow P, Christie G. “New Thoughts on an Old Topic: Secrets of Bacterial Spore Resistance Slowly Being Revealed.” *Microbiology and Molecular Biology Reviews* 87. **Published June 2023.** DOI: [10.1128/mmbr.00080-22](https://doi.org/10.1128/mmbr.00080-22). (setlow2023newthoughtson pages 2-4, setlow2023newthoughtson pages 1-2)
4. Galperin MY, Yutin N, Wolf YI, Vera Alvarez R, Koonin EV. “Conservation and Evolution of the Sporulation Gene Set in Diverse Members of the Firmicutes.” *Journal of Bacteriology* 204. **Published June 2022.** DOI: [10.1128/jb.00079-22](https://doi.org/10.1128/jb.00079-22). (galperin2022conservationandevolution pages 18-20)
5. Beskrovnaya P et al. “Structural, Metabolic and Evolutionary Comparison of Bacterial Endospore and Exospore Formation.” *Frontiers in Microbiology* 12. **Published March 2021.** DOI: [10.3389/fmicb.2021.630573](https://doi.org/10.3389/fmicb.2021.630573).

**Recommended curation decision:** expand the existing 15-node/11-edge graph into a modular, taxon-qualified network centered on Spo0A-dependent commitment, compartment-specific σ-factor programs, engulfment, cortex/coat assembly, SpoVA–CaDPA loading, SASP-dependent core maturation, and mother-cell lysis. The strongest immediately curatable additions are asymmetric septation → compartment formation, engulfment → late forespore differentiation, σK → coat formation, SpoVA → CaDPA accumulation, SASPs → DNA protection, cortex/coat/core properties → resistance, and mother-cell lysis → mature-spore release. The SspA/SspB–SpoIVB2 relationship should be represented as an uncertain *C. difficile*-specific pathway association until direct molecular regulation is demonstrated.

References

1. (nerber2024thesmallacidsoluble pages 1-2): Hailee N. Nerber, Marko Baloh, Joshua N. Brehm, and Joseph A. Sorg. The small acid-soluble proteins of clostridioides difficile regulate sporulation in a spoivb2-dependent manner. Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012507, doi:10.1371/journal.ppat.1012507. This article has 12 citations and is from a highest quality peer-reviewed journal.

2. (cassona2024sporesofclostridioides pages 1-2): Carolina P. Cassona, Sara Ramalhete, Khira Amara, Thomas Candela, Imad Kansau, Cécile Denève-Larrazet, Claire Janoir-Jouveshomme, Luís Jaime Mota, Bruno Dupuy, Mónica Serrano, and Adriano O. Henriques. Spores of clostridioides difficile are toxin delivery vehicles. Communications Biology, Jul 2024. URL: https://doi.org/10.1038/s42003-024-06521-x, doi:10.1038/s42003-024-06521-x. This article has 4 citations and is from a peer-reviewed journal.

3. (galperin2022conservationandevolution pages 18-20): Michael Y. Galperin, Natalya Yutin, Yuri I. Wolf, Roberto Vera Alvarez, and Eugene V. Koonin. Conservation and evolution of the sporulation gene set in diverse members of the <i>firmicutes</i>. Jun 2022. URL: https://doi.org/10.1128/jb.00079-22, doi:10.1128/jb.00079-22. This article has 104 citations and is from a peer-reviewed journal.

4. (nerber2024thesmallacidsoluble pages 27-28): Hailee N. Nerber, Marko Baloh, Joshua N. Brehm, and Joseph A. Sorg. The small acid-soluble proteins of clostridioides difficile regulate sporulation in a spoivb2-dependent manner. Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012507, doi:10.1371/journal.ppat.1012507. This article has 12 citations and is from a highest quality peer-reviewed journal.

5. (setlow2023newthoughtson pages 1-2): Peter Setlow and Graham Christie. New thoughts on an old topic: secrets of bacterial spore resistance slowly being revealed. Microbiology and Molecular Biology Reviews, Jun 2023. URL: https://doi.org/10.1128/mmbr.00080-22, doi:10.1128/mmbr.00080-22. This article has 147 citations and is from a domain leading peer-reviewed journal.

6. (setlow2023newthoughtson pages 2-4): Peter Setlow and Graham Christie. New thoughts on an old topic: secrets of bacterial spore resistance slowly being revealed. Microbiology and Molecular Biology Reviews, Jun 2023. URL: https://doi.org/10.1128/mmbr.00080-22, doi:10.1128/mmbr.00080-22. This article has 147 citations and is from a domain leading peer-reviewed journal.

7. (setlow2023newthoughtson pages 14-16): Peter Setlow and Graham Christie. New thoughts on an old topic: secrets of bacterial spore resistance slowly being revealed. Microbiology and Molecular Biology Reviews, Jun 2023. URL: https://doi.org/10.1128/mmbr.00080-22, doi:10.1128/mmbr.00080-22. This article has 147 citations and is from a domain leading peer-reviewed journal.