---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:04:17.933183'
end_time: '2026-06-18T08:09:45.390529'
duration_seconds: 327.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gram variable
  trait_identifier: METPO:1000700
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gram_variable
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A gram stain in which bacteria from the same culture show both gram-positive
    and gram-negative staining characteristics, often due to age of culture or cell
    wall degradation.
  parent_traits: METPO:1000697
  synonyms: variable
  evidence_summary: 'DOI:10.1128/CMR.00043-07: cell wall structure (Bacterial cell-wall
    review supports peptidoglycan thinning and autolysis-mediated loss of crystal-violet
    retention as the basis for gram-variable staining.)'
  causal_graph_summary: 'gram_variable_wall_thinning: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gram variable
- **METPO identifier:** METPO:1000700
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria from the same culture show both gram-positive and gram-negative staining characteristics, often due to age of culture or cell wall degradation.
- **Parent traits:** METPO:1000697
- **Synonyms:** variable
- **Existing evidence:** DOI:10.1128/CMR.00043-07: cell wall structure (Bacterial cell-wall review supports peptidoglycan thinning and autolysis-mediated loss of crystal-violet retention as the basis for gram-variable staining.)
- **Existing causal graph summary:** gram_variable_wall_thinning: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **gram variable** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_variable.yaml`.

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
- **Trait label:** gram variable
- **METPO identifier:** METPO:1000700
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A gram stain in which bacteria from the same culture show both gram-positive and gram-negative staining characteristics, often due to age of culture or cell wall degradation.
- **Parent traits:** METPO:1000697
- **Synonyms:** variable
- **Existing evidence:** DOI:10.1128/CMR.00043-07: cell wall structure (Bacterial cell-wall review supports peptidoglycan thinning and autolysis-mediated loss of crystal-violet retention as the basis for gram-variable staining.)
- **Existing causal graph summary:** gram_variable_wall_thinning: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **gram variable** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gram_variable.yaml`.

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


# Gram-variable (METPO:1000700) — Curation-Focused Research Report (2023–2024 emphasis)

## 0. Scope summary (TraitMech framing)
**Trait label:** gram variable (METPO:1000700; MORPHOLOGY; CLASS)

**Operational phenotype (assay-observed):** “Gram-variable” describes a **single culture** (or population derived from a single sample) in which **some cells stain Gram-positive and others stain Gram-negative** under the Gram stain procedure, producing mixed microscopic appearances. The most defensible interpretation for TraitMech is that gram-variability can arise from **(A) intrinsic biological heterogeneity** in cell-envelope state (e.g., peptidoglycan depletion or cell-wall-deficient subpopulations) and/or **(B) experimental/assay artifacts** (especially decolorization and smear quality) that make a genetically consistent population appear mixed. (carvalho2024aquaticenvironmentdrives pages 2-3, mitra2023practicaltipsand pages 2-3)

**Key boundary cases and distinctions:**
1. **True Gram-negative vs gram-variable:** Gram-negative staining is not always evidence of a diderm (outer membrane/LPS) envelope; some **monoderm** Bacillota can stain Gram-negative due to **thin peptidoglycan**, even without LPS/outer-membrane genes. This is a structural boundary case distinct from “gram-variable” (within-culture mixed staining). (choi2024deeplybranchingbacillota pages 1-2, choi2024deeplybranchingbacillota pages 2-4)
2. **Procedural variability vs biological variability:** Over- or under-decolorization and thick/uneven smears can produce apparent Gram variability without underlying cell-envelope differences. (mitra2023practicaltipsand pages 2-3, mitra2023practicaltipsand pages 3-5)

## 1. Key concepts and definitions (current understanding)
### 1.1 Gram stain chemistry relevant to gram-variability
The Gram stain outcome depends on the ability of cells to retain the **crystal violet–iodide** complex during the decolorization step; loss of retention yields a Gram-negative appearance. A 2024 analysis of atypical staining in Bacillota summarizes this logic and explicitly connects Gram-negative staining to diminished retention of the crystal violet signal. (choi2024deeplybranchingbacillota pages 1-2)

**Curation implication:** trait-mechanism nodes should include at least (i) crystal violet entry/retention, (ii) iodine complex formation, and (iii) decolorization sensitivity, with **peptidoglycan thickness or integrity** as a central mediator. (choi2024deeplybranchingbacillota pages 1-2)

### 1.2 Biological gram-variability: heterogeneous envelope states in one culture
A strong recent mechanistic model is that stress conditions can drive some cells into **cell wall–deficient (CWD)** or **VBNC-associated** states where peptidoglycan is substantially reduced or lost; these subpopulations then stain differently from walled cells in the same culture.

In *Listeria monocytogenes*, starvation in mineral water (aquatic/hypoosmotic, oligotrophic stress) drove a transition to osmotically stable **cell wall-deficient coccoid forms**, and accompanying biochemical evidence showed a time-dependent depletion of peptidoglycan “until virtually no peptidoglycan was detected.” This provides a direct biological basis for mixed or shifting Gram-stain phenotypes within a culture over time. (carvalho2024aquaticenvironmentdrives pages 2-3)

### 1.3 Procedural gram-variability: decolorization and smear artifacts
A clinical microbiology troubleshooting review (ocular microbiology context) emphasizes that **decolorization is the critical step**, and that both over- and under-decolorization are common sources of erroneous Gram interpretation. Thick or uneven smears also reduce visibility and can distort interpretation; corrective actions include repeating decolorization/re-staining and ensuring appropriate decolorizer quality (e.g., adequate acetone concentration). (mitra2023practicaltipsand pages 2-3, mitra2023practicaltipsand pages 3-5)

**Curation implication:** these should be represented as **experimental factors** (assay nodes) rather than intrinsic microbial mechanisms. (mitra2023practicaltipsand pages 2-3)

## 2. Recent developments and latest research (2023–2024 prioritized)
### 2.1 2024 (Nature Communications): stress-driven cell wall shedding creates CWD/VBNC populations (mechanistic, high-authority)
Carvalho et al. (Oct 2024) show that starvation in mineral water drives *Listeria monocytogenes* to become VBNC and to convert into **cell wall-deficient coccoid forms**. The study further identifies regulators/actors for the transition, including the stress regulator **SigB** and the autolysin **NamA**, and indicates that export machinery (**SecA2**) mediates surface export of NamA and p60 autolysins. This chain supports a mechanistic “edge set” from stress → regulated autolysin activity/export → peptidoglycan depletion → altered staining phenotype. (carvalho2024aquaticenvironmentdrives pages 2-3, carvalho2024aquaticenvironmentdrives pages 6-8)

**Quantitative / data-like statements extractable from the available evidence:** the population can reach **>95% CWD by day 28** in the described conditions, and peptidoglycan can become **virtually undetectable by day 28**, implying that Gram-variable staining can reflect time-dependent population shifts. (carvalho2024aquaticenvironmentdrives pages 2-3)

### 2.2 2024 (Microbiology Spectrum): atypical Gram-negative staining in monoderm Bacillota is linked to thin peptidoglycan (boundary case)
Choi et al. (Oct 2024) compiled Gram staining and ultrastructural/genomic data and report that many deeply branching Bacillota stain Gram-negative **without genes for LPS/outer-membrane biosynthesis**, suggesting that Gram-negative staining can reflect a **thin peptidoglycan layer** rather than a diderm envelope. They identified **45** such atypical Gram-negative-staining species in their dataset. This reframes interpretation of Gram results and helps avoid mis-curating “Gram-negative” as an envelope class when the organism is monoderm. (choi2024deeplybranchingbacillota pages 2-4)

### 2.3 2023 (Indian Journal of Ophthalmology): Gram stain troubleshooting highlights common causes of false Gram reactions
Mitra et al. (May 2023) emphasize common mistakes that can generate false Gram results: errors in decolorization (both directions), thick/uneven smears, and stain precipitates that can mimic bacterial morphology (e.g., dye crystals mimicking Gram-positive cocci). These are real-world implementation details that explain many laboratory instances of “gram-variable” readouts. (mitra2023practicaltipsand pages 2-3, mitra2023practicaltipsand pages 3-5)

### 2.4 2023 preprint context: wall-deficient states and stress-induced envelope changes
A 2023 bioRxiv preprint by Carvalho et al. (Nov 2023) provides broader context that multiple stressors and states (e.g., VBNC, L-forms) involve cell-wall modification or loss that can plausibly produce mixed staining in one culture; however, specific mechanistic edges from this preprint should be curated cautiously unless directly supported by the peer-reviewed 2024 version or other primary sources. (carvalho2023divingintobacterial pages 34-36, carvalho2023divingintobacterial pages 32-34)

## 3. Current applications and real-world implementations
### 3.1 Clinical and diagnostic microbiology: interpreting “gram-variable” results
In routine microscopy, “gram-variable” is often handled as a **flag for uncertainty** requiring follow-up (culture, molecular ID, repeat smear). Practical recommendations include repeating the stain/decolorization and ensuring smear quality; Mitra et al. explicitly recommend troubleshooting decolorization timing and decolorizer quality. (mitra2023practicaltipsand pages 3-5)

### 3.2 Environmental/food/pathogen monitoring: dormant or wall-deficient forms can evade growth-based detection
The 2024 *Listeria* study highlights that stress can push pathogens into VBNC and cell-wall-deficient forms, which are **harder to detect by growth-based methods** and may also change staining behavior; this is relevant for water/food safety monitoring where organisms may persist under oligotrophic aquatic conditions. (carvalho2024aquaticenvironmentdrives pages 2-3)

## 4. Expert opinions and analysis (authoritative sources)
### 4.1 Interpretation caution: Gram-negative staining is not equivalent to diderm cell envelope
Choi et al. explicitly challenge the conventional equivalence between Gram-negative staining and diderm structure, showing monoderms that stain Gram-negative and attributing this to peptidoglycan thickness/envelope architecture. For gram-variable curation, this supports treating **Gram stain** as an **assay output** influenced by structure, not as a definitive envelope-class label. (choi2024deeplybranchingbacillota pages 1-2, choi2024deeplybranchingbacillota pages 2-4)

### 4.2 Mechanistic emphasis: stress-regulated autolysins can drive wall loss and altered staining
Carvalho et al. identify SigB and NamA as major actors in the VBNC/CWD transition and connect SecA2 export to surface localization of autolysins, supporting an expert interpretation that gram variability can be produced by regulated, stress-induced remodeling and degradation of peptidoglycan. (carvalho2024aquaticenvironmentdrives pages 6-8)

### 4.3 Laboratory best practices: decolorization and smear quality are dominant preventable causes
Mitra et al. emphasize that over/under-decolorization are common and correctable, and that smear thickness affects interpretation. This supports modeling procedural factors in the causal graph as upstream causes of “apparent gram-variable staining” that should be separated from true biological variability. (mitra2023practicaltipsand pages 2-3)

## 5. Candidate causal graph entities (nodes), grouped by type
### 5.1 Assay / observation nodes (Gram stain)
- Gram staining outcome: gram-variable (METPO:1000700)
- Crystal violet (CHEBI:53742; suggested in artifact)
- Iodide/iodine reagent (CHEBI:18248 iodide; suggested)
- Decolorization solvent: acetone (CHEBI:15347) and ethanol (CHEBI:16284) (suggested)
- Smear thickness / smear uniformity (label-only)
- Stain precipitates / dye crystals (label-only)

### 5.2 Environmental / experimental condition nodes
- Starvation / nutrient deprivation (label-only)
- Mineral water / aquatic low-nutrient environment (ENVO:00002006 mineral water; suggested)
- Low starting cell density / inoculum density (label-only; contextual factor) (carvalho2024aquaticenvironmentdrives pages 2-3)

### 5.3 Cellular structures and processes
- Peptidoglycan layer thickness (label-only)
- Peptidoglycan depletion / cell wall loss (label-only)
- Cell wall-deficient (CWD) form (label-only)
- VBNC state (label-only)
- Peptidoglycan catabolic process (GO:0009253; suggested)

### 5.4 Genes / proteins / regulators (taxon-specific exemplars)
- SigB (stress response regulator; label-only grounding pending taxon mapping) (carvalho2024aquaticenvironmentdrives pages 6-8)
- NamA (autolysin; label-only grounding pending) (carvalho2024aquaticenvironmentdrives pages 6-8)
- SecA2 (export ATPase; label-only grounding pending) (carvalho2024aquaticenvironmentdrives pages 6-8)
- p60 autolysins (label-only) (carvalho2024aquaticenvironmentdrives pages 6-8)

## 6. Candidate evidence-backed causal edges (curation table)
The following artifact compiles candidate triples with citations, snippets, and curation notes.

| Edge (subject—predicate→object) | Evidence type | Reference (first author, year, journal) | DOI + URL | Publication date (month/year) | Supporting snippet (verbatim short quote) | Notes for curation (include uncertainty, taxon/assay specificity) | Suggested ontology grounding (CURIEs where possible) |
|---|---|---|---|---|---|---|---|
| Starvation in mineral water — induces → VBNC state | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “bacteria starved in mineral water become VBNC” (carvalho2024aquaticenvironmentdrives pages 2-3) | Strong direct evidence in *Listeria monocytogenes* under aquatic/mineral-water starvation; taxon- and condition-specific but broadly relevant to gram-variable mechanisms via wall loss. | ENVO:00002006 mineral water; GO:0098708 detection of nutrient levels (broad stress context, tentative); label-only: starvation; label-only: viable but non-culturable state |
| Starvation in mineral water — drives → cell wall-deficient coccoid forms | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “by converting into osmotically stable cell wall-deficient coccoid forms” (carvalho2024aquaticenvironmentdrives pages 2-3) | Strong direct evidence for a mixed population with altered wall status; useful for gram-variable graph because CWD cells are expected to stain atypically. | GO:0009272 peptidoglycan-based cell wall biogenesis; label-only: cell wall-deficient cell; label-only: coccoid morphology |
| Lower starting cell density — accelerates → culturability loss / VBNC transition | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “lower starting concentrations accelerate culturability loss” (carvalho2024aquaticenvironmentdrives pages 2-3) | Secondary ecological/experimental factor; may modulate frequency of gram-variable populations rather than directly determine staining chemistry. Mark as contextual. | label-only: low inoculum density; label-only: loss of culturability |
| SigB stress response regulator — promotes → CW loss / VBNC transition | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “SigB and the autolysin NamA as major actors of VBNC state transition” (carvalho2024aquaticenvironmentdrives pages 2-3) | Good direct genetics evidence in *Listeria*; support is strongest for contribution to transition, not necessarily direct biochemical cleavage of PG. | label-only: SigB; GO:0006950 response to stress; label-only: cell wall loss |
| SecA2 — mediates surface export of → NamA and p60 autolysins | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “the SecA2 export ATPase mediates surface export of NamA and p60 autolysins” (carvalho2024aquaticenvironmentdrives pages 6-8) | Strong mechanistic edge for a gene/protein entity enabling downstream wall degradation; currently supported in *Listeria*. | label-only: SecA2; GO:0015031 protein transport; label-only: NamA; label-only: p60 autolysin |
| NamA autolysin — required for timely → cell wall loss | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “NamA is required for timely CW loss” (carvalho2024aquaticenvironmentdrives pages 6-8) | Strong recent evidence; direct and curation-ready, though taxon-specific to *Listeria* unless generalized cautiously. | label-only: NamA; GO:0016998 cell wall macromolecule catabolic process; GO:0043285 maintenance of cell shape |
| NamA / autolysin activity — causes → peptidoglycan degradation/loss | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “regulated peptidoglycan degradation can produce mixed populations with and without intact cell walls” (carvalho2024aquaticenvironmentdrives pages 6-8) | Summative phrasing from evidence extraction rather than article quotation from full text; still supported by the experimental narrative. Mark slightly uncertain if strict verbatim curation is required. | GO:0009253 peptidoglycan catabolic process; GO:0019835 cytolysis? (avoid unless needed); label-only: autolysin activity |
| Peptidoglycan depletion — leads to → loss of Gram-positive crystal-violet retention / Gram-negative appearance | mechanistic | Carvalho, 2024, Nature Communications | 10.1038/s41467-024-52633-7; https://doi.org/10.1038/s41467-024-52633-7 | 10/2024 | “virtually no peptidoglycan was detected by day 28” and coccoid VBNC cells “no longer” display the usual crystal violet Gram-positive staining (carvalho2024aquaticenvironmentdrives pages 2-3) | Strong, directly relevant to gram-variable trait; links wall depletion to altered stain outcome in one culture over time. | GO:0009253 peptidoglycan catabolic process; CHEBI:53742 crystal violet; label-only: Gram-negative staining |
| Thin peptidoglycan layer — results in → Gram-negative staining despite monoderm envelope | mechanistic | Choi, 2024, Microbiology Spectrum | 10.1128/spectrum.00732-24; https://doi.org/10.1128/spectrum.00732-24 | 10/2024 | “certain bacteria can stain Gram-negative despite having a monoderm cell wall structure” (choi2024deeplybranchingbacillota pages 1-2) | Strong evolutionary/cell-envelope evidence; important boundary case showing that Gram-negative staining is not equivalent to diderm structure. | label-only: thin peptidoglycan layer; label-only: monoderm cell envelope; label-only: Gram-negative staining |
| Thin peptidoglycan layer — reduces retention of → CV-iodide complex | mechanistic | Choi, 2024, Microbiology Spectrum | 10.1128/spectrum.00732-24; https://doi.org/10.1128/spectrum.00732-24 | 10/2024 | “to retain the CV-iodide complex, resulting in the loss of the CV” (choi2024deeplybranchingbacillota pages 1-2) | This is the core staining-chemistry edge; highly relevant to trait mechanism. | CHEBI:53742 crystal violet; CHEBI:18248 iodide; label-only: CV-iodide complex; label-only: retention of stain |
| Absence of canonical LPS/OM genes with alternative outer layers — co-occurs with → atypical Gram-negative staining | mechanistic | Choi, 2024, Microbiology Spectrum | 10.1128/spectrum.00732-24; https://doi.org/10.1128/spectrum.00732-24 | 10/2024 | “stain Gram-negative but do not harbor genes for outer membrane protein or lipopolysaccharide biosynthesis” (choi2024deeplybranchingbacillota pages 1-2) | Useful boundary-case edge; not necessarily a direct cause of gram-variability within one culture, but helps distinguish phenotype from diderm status. Mark as structural/phylogenomic context. | label-only: lipopolysaccharide biosynthetic process; label-only: outer membrane biogenesis; label-only: S-layer |
| Over-decolorization — causes → false Gram-negative result | procedural | Mitra, 2023, Indian Journal of Ophthalmology | 10.4103/ijo.ijo_2190_22; https://doi.org/10.4103/ijo.ijo_2190_22 | 05/2023 | “Over-decolorization and under-decolorization are common” (mitra2023practicaltipsand pages 2-3) | Strong procedural edge; assay artifact rather than organismal trait. Should likely be modeled as experimental factor, not intrinsic mechanism. | CHEBI:16284 ethanol; CHEBI:15347 acetone; label-only: decolorization step; label-only: false Gram-negative |
| Under-decolorization — causes → false Gram-positive result | procedural | Mitra, 2023, Indian Journal of Ophthalmology | 10.4103/ijo.ijo_2190_22; https://doi.org/10.4103/ijo.ijo_2190_22 | 05/2023 | “Over-decolorization and under-decolorization are common” (mitra2023practicaltipsand pages 2-3) | Companion assay-artifact edge; important to distinguish apparent gram variability from biological variability. | CHEBI:16284 ethanol; CHEBI:15347 acetone; label-only: under-decolorization; label-only: false Gram-positive |
| Thick, uneven smear — causes → Gram-stain misinterpretation | procedural | Mitra, 2023, Indian Journal of Ophthalmology | 10.4103/ijo.ijo_2190_22; https://doi.org/10.4103/ijo.ijo_2190_22 | 05/2023 | “thick, uneven smears reduce light transmission and visualization and are ‘not ideal’ for Gram staining” (mitra2023practicaltipsand pages 2-3) | Strong practical edge; morphology/readout artifact, not a causal microbial mechanism. | label-only: thick smear; label-only: microscopy misinterpretation |
| Low acetone concentration / exhausted decolorizer — causes → under-decolorization | procedural | Mitra, 2023, Indian Journal of Ophthalmology | 10.4103/ijo.ijo_2190_22; https://doi.org/10.4103/ijo.ijo_2190_22 | 05/2023 | “replacing decolorizer if acetone concentration falls” (mitra2023practicaltipsand pages 3-5) | Strong assay-maintenance edge; curation should place under experimental factors. | CHEBI:15347 acetone; label-only: decolorizer quality; label-only: under-decolorization |
| Crystal violet precipitates / dye crystals — mimic → false Gram-positive cocci | procedural | Mitra, 2023, Indian Journal of Ophthalmology | 10.4103/ijo.ijo_2190_22; https://doi.org/10.4103/ijo.ijo_2190_22 | 05/2023 | “crystal violet deposits and dye crystals can mimic Gram-positive cocci” (mitra2023practicaltipsand pages 3-5) | Strong artifact edge; especially important in low-biomass specimens. | CHEBI:53742 crystal violet; label-only: stain precipitate; label-only: false Gram-positive cocci |
| Stress-induced cell wall-deficient forms — can produce → mixed Gram reactions in one culture | mechanistic | Carvalho, 2023, bioRxiv | 10.1101/2023.11.16.566987; https://doi.org/10.1101/2023.11.16.566987 | 11/2023 | “mechanisms that can produce cell-wall alterations or loss that would lead to mixed Gram reactions in a single culture” (carvalho2023divingintobacterial pages 34-36) | Preprint, so lower evidentiary weight than 2024 peer-reviewed version; still useful as supporting context. | label-only: stress-induced cell wall-deficient cell; label-only: mixed Gram reaction |
| Lysozyme or β-lactam stress — promotes emergence of → L-form / wall-deficient bacteria | mechanistic | Carvalho, 2023, bioRxiv | 10.1101/2023.11.16.566987; https://doi.org/10.1101/2023.11.16.566987 | 11/2023 | “Lysozyme Counteracts β-Lactam Antibiotics by Promoting the Emergence of L-Form Bacteria” (carvalho2023divingintobacterial pages 34-36) | Indirect citation within a preprint discussion, not primary 2023–2024 experimental evidence in this context; retain as hypothesis-generating, uncertain. | CHEBI:25017 lysozyme; CHEBI:27933 beta-lactam antibiotic; label-only: L-form bacterium |


*Table: This table compiles candidate mechanistic and procedural causal edges relevant to the gram-variable trait, using only the available cited context. It is designed to support TraitMech curation by linking stain outcomes to cell-wall biology, stress responses, and assay artifacts with ontology suggestions.*

## 7. Warnings and “do not curate yet” items
1. **Separate intrinsic vs procedural causes:** Over/under-decolorization, thick smears, and stain precipitates are robust causes of apparent Gram variability but should be curated as **assay confounders**, not microbial mechanisms. (mitra2023practicaltipsand pages 2-3, mitra2023practicaltipsand pages 3-5)
2. **Preprint-only edges:** The 2023 bioRxiv discussion includes plausible links (e.g., lysozyme/β-lactam promoting L-forms) but these are not primary, directly quoted experimental results in the provided evidence set; treat as **hypothesis-generating** unless corroborated with peer-reviewed primary data. (carvalho2023divingintobacterial pages 34-36)
3. **Taxon specificity:** SigB/NamA/SecA2 edges are experimentally supported in *Listeria monocytogenes* under specific starvation/mineral-water conditions; generalizing to other taxa should be marked uncertain without additional sources. (carvalho2024aquaticenvironmentdrives pages 6-8)
4. **Boundary case misclassification:** A stable Gram-negative stain in monoderm Bacillota due to thin peptidoglycan is not necessarily “gram-variable”; it is an important **adjacent phenotype** that prevents incorrect inference of diderm envelope. (choi2024deeplybranchingbacillota pages 2-4)

## 8. DOI-first bibliography (with dates and URLs)
1. Carvalho F, et al. **Aquatic environment drives the emergence of cell wall-deficient dormant forms in Listeria.** *Nature Communications*. **Oct 2024**. DOI: **10.1038/s41467-024-52633-7**. URL: https://doi.org/10.1038/s41467-024-52633-7 (carvalho2024aquaticenvironmentdrives pages 2-3, carvalho2024aquaticenvironmentdrives pages 6-8)
2. Choi JK, Poudel S, Yee N, Goff JL. **Deeply branching Bacillota species exhibit atypical Gram-negative staining.** *Microbiology Spectrum*. **Oct 2024**. DOI: **10.1128/spectrum.00732-24**. URL: https://doi.org/10.1128/spectrum.00732-24 (choi2024deeplybranchingbacillota pages 1-2, choi2024deeplybranchingbacillota pages 2-4)
3. Mitra S, Chandran K, Fernandes M. **Practical tips and common mistakes in ocular microbiology sampling and processing.** *Indian Journal of Ophthalmology*. **May 2023**. DOI: **10.4103/ijo.ijo_2190_22**. URL: https://doi.org/10.4103/ijo.ijo_2190_22 (mitra2023practicaltipsand pages 2-3, mitra2023practicaltipsand pages 3-5)
4. Carvalho F, et al. **Diving into bacterial dormancy: emergence of osmotically stable wall-less forms in an aquatic environment.** *bioRxiv* (preprint). **Nov 2023**. DOI: **10.1101/2023.11.16.566987**. URL: https://doi.org/10.1101/2023.11.16.566987 (carvalho2023divingintobacterial pages 34-36, carvalho2023divingintobacterial pages 32-34)


References

1. (carvalho2024aquaticenvironmentdrives pages 2-3): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 23 citations and is from a highest quality peer-reviewed journal.

2. (mitra2023practicaltipsand pages 2-3): Sanchita Mitra, Kavya Chandran, and Merle Fernandes. Practical tips and common mistakes in ocular microbiology sampling and processing. Indian Journal of Ophthalmology, 71:1698-1705, May 2023. URL: https://doi.org/10.4103/ijo.ijo\_2190\_22, doi:10.4103/ijo.ijo\_2190\_22. This article has 9 citations and is from a peer-reviewed journal.

3. (choi2024deeplybranchingbacillota pages 1-2): Jessica K. Choi, Saroj Poudel, Nathan Yee, and Jennifer L. Goff. Deeply branching <i>bacillota</i> species exhibit atypical gram-negative staining. Oct 2024. URL: https://doi.org/10.1128/spectrum.00732-24, doi:10.1128/spectrum.00732-24. This article has 12 citations and is from a domain leading peer-reviewed journal.

4. (choi2024deeplybranchingbacillota pages 2-4): Jessica K. Choi, Saroj Poudel, Nathan Yee, and Jennifer L. Goff. Deeply branching <i>bacillota</i> species exhibit atypical gram-negative staining. Oct 2024. URL: https://doi.org/10.1128/spectrum.00732-24, doi:10.1128/spectrum.00732-24. This article has 12 citations and is from a domain leading peer-reviewed journal.

5. (mitra2023practicaltipsand pages 3-5): Sanchita Mitra, Kavya Chandran, and Merle Fernandes. Practical tips and common mistakes in ocular microbiology sampling and processing. Indian Journal of Ophthalmology, 71:1698-1705, May 2023. URL: https://doi.org/10.4103/ijo.ijo\_2190\_22, doi:10.4103/ijo.ijo\_2190\_22. This article has 9 citations and is from a peer-reviewed journal.

6. (carvalho2024aquaticenvironmentdrives pages 6-8): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 23 citations and is from a highest quality peer-reviewed journal.

7. (carvalho2023divingintobacterial pages 34-36): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Diving into bacterial dormancy: emergence of osmotically stable wall-less forms in an aquatic environment. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.16.566987, doi:10.1101/2023.11.16.566987. This article has 1 citations.

8. (carvalho2023divingintobacterial pages 32-34): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Diving into bacterial dormancy: emergence of osmotically stable wall-less forms in an aquatic environment. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.16.566987, doi:10.1101/2023.11.16.566987. This article has 1 citations.