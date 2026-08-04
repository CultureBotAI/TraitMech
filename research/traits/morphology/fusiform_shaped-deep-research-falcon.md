---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:25:46.286312'
end_time: '2026-08-04T08:36:49.797138'
duration_seconds: 663.51
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: fusiform shaped
  trait_identifier: METPO:1000690
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: fusiform_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape that is wide in the middle and tapers at both ends.
  parent_traits: METPO:1000666
  synonyms: fusiform
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports tapered cell ends as a genetically determined
    geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731:
    Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology
    in the Fusobacterium genus.)'
  causal_graph_summary: 'fusiform_shaped_tapered_polar_growth: 14 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** fusiform shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000690
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is wide in the middle and tapers at both ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** fusiform
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports tapered cell ends as a genetically determined geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731: Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology in the Fusobacterium genus.)
- **Existing causal graph summary:** fusiform_shaped_tapered_polar_growth: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **fusiform shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/fusiform_shaped.yaml`.

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
- **Trait label:** fusiform shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000690
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is wide in the middle and tapers at both ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** fusiform
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports tapered cell ends as a genetically determined geometry maintained by graded wall synthesis.) | DOI:10.1111/1462-2920.13731: Fusobacterium nucleatum (Fusobacterium-genome review supports fusiform morphology in the Fusobacterium genus.)
- **Existing causal graph summary:** fusiform_shaped_tapered_polar_growth: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **fusiform shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/fusiform_shaped.yaml`.

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


# Curation report: microbial fusiform shape

## Executive assessment

**Target:** `METPO:1000690` (“fusiform shaped”), a reviewed morphology class defined as a cell that is wide in the middle and tapers at both ends.

The literature strongly supports fusiform shape as a recognizable whole-cell phenotype, but direct mechanism-to-phenotype evidence remains sparse. The strongest current TraitMech candidates fall into two taxon-specific branches:

1. **Spatial peptidoglycan branch:** altered nucleotide-binding states of MreB drive polar localization and are associated with extremely tapered, pointed poles in *Caulobacter crescentus*. This is compelling evidence for formation of the tapered-pole component of fusiform geometry, although the mutant phenotype is not explicitly classified as `METPO:1000690`. (randich2015molecularmechanismsfor pages 7-9)
2. **Energy/metabolism branch:** deletion of `rnfC` in the naturally elongated *Fusobacterium nucleatum* produces short/stubby cells, sharply reduced ATP production, premature growth cessation, and broad amino-acid-metabolism defects. This establishes Rnf as necessary for normal fusobacterial morphology, but not yet as a fusiform-specific morphogen. (britton2024therespiratoryenzyme pages 5-7, britton2024therespiratoryenzyme media caddd5ad)

Accordingly, a conservative graph should curate the direct perturbation edges while marking the final links to `METPO:1000690` as **taxon-specific or uncertain**.

## 1. Trait scope

### Operational meaning

For microbial curation, fusiform should mean a **spindle-like whole cell whose transverse width reaches a maximum near midcell and declines toward both poles**. The phenotype should ideally be established by microscopy of intact cells rather than inferred from a genus name. A 2023 review provides a clear exemplar: *Helicobacter cetorum* has a “slightly helical, fusiform cell body that is tapered at both ends.” (bansil2023motilityofdifferent pages 1-2)

*Tannerella forsythia* is independently described as a Gram-negative, anaerobic fusiform bacterium, and its historical designation was “fusiform Bacteroides.” (posch2012glycobiologyaspectsof pages 1-3, veith2015tannerellaforsythiaouter pages 1-2)

### Boundary cases

Exclude or annotate separately:

- **Ordinary rods:** approximately parallel lateral walls with rounded or blunt poles.
- **Filamentous cells:** length alone does not imply fusiform shape.
- **Vibrioid, curved, or helical cells:** curvature/helicity is an independent axis. *H. cetorum* can be both slightly helical and fusiform. (bansil2023motilityofdifferent pages 1-2)
- **Unipolar tapering, prosthecae, or stalks:** fusiform requires narrowing at both ends of the cell body.
- **Club-shaped or pleomorphic cells:** asymmetric width distributions do not meet the strict definition.
- **Spores, fungal conidia, and transient division intermediates:** these should not be merged automatically with vegetative bacterial cell shape.
- **Drug-induced or moribund shapes:** retain as assay-specific phenotypes unless normal growth and viability are demonstrated.
- **“Extremely tapered and pointed poles” in MreB mutants:** highly relevant mechanistically, but curate as fusiform-like or tapered-pole morphology unless the source explicitly establishes maximum midcell width and bilateral tapering. (randich2015molecularmechanismsfor pages 7-9)

## 2. Current mechanistic understanding

Peptidoglycan is the principal load-bearing bacterial cell-wall polymer, while MreB organizes elongation-associated wall synthesis in many rod-shaped bacteria. Fluorescent labeling shows that nascent peptidoglycan synthesis resembles MreB/Mbl distributions; MreB-associated synthetic and degradative proteins organize wall synthesis and normally enforce a cylindrical shape. This is authoritative background, not direct evidence for fusiform morphology. (egan2020regulationofpeptidoglycan pages 8-9)

The more specific evidence comes from *C. crescentus*. MreB depletion produces lemon-shaped cells, whereas nucleotide-binding-pocket substitutions E213G, D16G, N21D, and A325P cause variable width with “extremely tapered and pointed” ends. In these mutants MreB localizes at the poles rather than dispersing laterally or condensing at the division plane. The review states that this behavior “presumably drives aberrant peptidoglycan synthesis,” and that wild-type tapered poles develop in the following cell cycle rather than during septation or medial elongation. The resulting model is that MreB nucleotide/ATPase state controls polar localization, which redirects polar wall remodeling and creates tapering. Because “presumably” and “could participate” are used, the localization-to-wall-synthesis edge is interpretive rather than fully demonstrated. (randich2015molecularmechanismsfor pages 7-9)

The principal recent development is the 2024 *F. nucleatum* Rnf study. A non-polar, in-frame `rnfC` deletion drastically reduced ATP, caused premature cessation of culture growth, and converted elongated parental cells into short/stubby forms by electron microscopy. Viable counts remained comparable, arguing that the optical-density and morphology effects were not simply caused by cell death. Complementation restored relevant phenotypes. (britton2024therespiratoryenzyme pages 5-7, britton2024therespiratoryenzyme media caddd5ad)

The same mutant had reduced `kamA`/`kamD` expression and extracellular lysine accumulation; 15 mM lysine blocked RadD-mediated coaggregation. It also showed reduced MegL, `cysK1`, and `cysK2` expression, deficient H₂S production, altered abundance of 17 of more than 80 detected metabolites, and reduced butyrate. These results connect ion-gradient-dependent energy conservation and amino-acid metabolism to envelope growth and morphology, but the study does not isolate which metabolic lesion causes the short/stubby phenotype. (britton2024therespiratoryenzyme pages 2-5, britton2024therespiratoryenzyme pages 5-7)

## 3. Candidate nodes grouped by type

### Trait and taxa

- **fusiform shaped** — `METPO:1000690`
- *Fusobacterium* — `NCBITaxon:851`
- *Fusobacterium nucleatum* — `NCBITaxon:203492`
- *Tannerella forsythia* — `NCBITaxon:28112`
- *Helicobacter cetorum* — label-only pending curator verification of the taxon CURIE
- *Caulobacter crescentus* — label-only pending curator verification of the strain/taxon CURIE

### Genes and proteins

- **MreB**, including E213G, D16G, N21D, and A325P variants — label-only; species-specific identifiers should be assigned from the exact strain record.
- **Rnf respiratory complex** and `rnfC`, `rnfD` — label-only pending exact strain-specific protein accessions.
- **FtsZ**, elongasome, and divisome — contextual nodes only; no direct fusiform-specific perturbation was retrieved.
- **MegL**, **CysK1**, **CysK2**, **KamA**, **KamD**, and adhesin **RadD** — label-only pending strain-specific grounding.
- Penicillin-binding proteins **PBP1A, PbpC, PbpX, PbpY, PbpZ** — context candidates in *C. crescentus*, not demonstrated fusiform determinants. (randich2015molecularmechanismsfor pages 7-9)

### Chemicals and cell-envelope entities

- peptidoglycan — `CHEBI:59640`
- ATP — `CHEBI:15422`
- L-lysine — `CHEBI:25017`
- hydrogen sulfide — `CHEBI:16136`
- butyrate — `CHEBI:17968`
- N-acetylmuramic acid — label-only here; *T. forsythia* identification/growth criteria include a requirement for it, but no causal shape evidence was recovered. (posch2012glycobiologyaspectsof pages 1-3)
- L-lanthionine — label-only pending verified CHEBI mapping

### Processes and localizations

- regulation of cell shape — `GO:0008360`
- peptidoglycan biosynthetic process — `GO:0009252`
- cell cycle — `GO:0007049`
- division-site formation — `GO:0000917`
- ATP binding — `GO:0005524`
- **cell pole**, **polar MreB localization**, **polar peptidoglycan remodeling**, **medial elongation**, and **zonal growth** — retain as label-only candidates unless exact ontology terms are verified.

### Environmental and experimental factors

- Anaerobic culture context for *F. nucleatum* and *T. forsythia*.
- Electron microscopy/TEM and negative staining as morphology assays.
- `rnfC` or `rnfD` non-polar in-frame deletion and plasmid complementation.
- MreB nucleotide-pocket substitutions.
- 15 mM extracellular lysine as a demonstrated coaggregation inhibitor, **not** a demonstrated shape perturbant. (britton2024therespiratoryenzyme pages 5-7)

## 4. Candidate causal edges

The table below separates direct causal or perturbational evidence from inferred mechanistic bridges and non-causal phenotype assertions.

| subject | predicate | object | taxon/context | confidence | DOI reference | short exact supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| MreB nucleotide-binding-site mutations (E213G, D16G, N21D, N21D, A325P) | localizes_to | cell poles | *Caulobacter crescentus* mutant context | medium | 10.3389/fmicb.2015.00580 | “for a subset of the nucleotide binding site MreB mutants (E213G, D16G, N21D, and A325P)… MreB still exhibits wild type function, it localizes to the cell poles” (randich2015molecularmechanismsfor pages 7-9) | Direct mutant evidence from review summarizing Dye et al. 2011/Harris et al. 2014; taxon-specific and not a fusiform taxon per se. |
| polar MreB localization | causes_or_promotes | aberrant polar peptidoglycan synthesis | *Caulobacter crescentus* mutant context | low | 10.3389/fmicb.2015.00580 | “it localizes to the cell poles… This behavior presumably drives aberrant peptidoglycan synthesis” (randich2015molecularmechanismsfor pages 7-9) | Keep as inferred/author interpretation because wording is “presumably drives.” |
| aberrant polar peptidoglycan synthesis | causes_or_promotes | extremely tapered and pointed cell poles | *Caulobacter crescentus* mutant context | medium | 10.3389/fmicb.2015.00580 | “cells exhibit a variable width phenotype in which the ends of the cells become extremely tapered and pointed… This behavior presumably drives aberrant peptidoglycan synthesis to create elongated cell poles.” (randich2015molecularmechanismsfor pages 7-9) | Best direct mechanistic edge for tapered-pole morphology; supports a fusiform-like geometry component rather than full trait across taxa. |
| polar cell wall remodeling | contributes_to | tapered pole development | wild-type *Caulobacter crescentus* | low | 10.3389/fmicb.2015.00580 | “the tapered shape of the wild type C. crescentus cell pole develops during the next cell cycle… corroborates the idea that MreB could participate in remodeling the cell wall at the poles.” (randich2015molecularmechanismsfor pages 7-9) | Wild-type remodeling is plausible but still couched as “corroborates the idea”; curate as uncertain and taxon-specific. |
| rnfC deletion | decreases | ATP production | *Fusobacterium nucleatum* ΔrnfC mutant | high | 10.1128/mbio.01751-23 | “compared to the parent strain, the ΔrnfC mutant drastically reduced ATP production” (britton2024therespiratoryenzyme pages 5-7) | Direct recent mutant evidence; pleiotropic physiology edge, not specific enough alone for fusiform shape. |
| rnfC deletion | causes_or_promotes | short/stubby cell morphology | *Fusobacterium nucleatum* ΔrnfC mutant | high | 10.1128/mbio.01751-23 | “the morphological abnormality of the ΔrnfC mutant with short/stubby cells as examined by electron microscopy” (britton2024therespiratoryenzyme pages 5-7) | Direct recent mutant evidence that loss of Rnf perturbs normal elongated morphology; useful negative-shape edge. |
| rnfC deletion | causes_or_promotes | premature growth cessation after suboptimal density | *Fusobacterium nucleatum* ΔrnfC mutant | high | 10.1128/mbio.01751-23 | “The ΔrnfC mutant was also severely defective in growth displaying premature growth cessation after the culture reached a suboptimal density” (britton2024therespiratoryenzyme pages 5-7) | Direct recent phenotype; likely indirect with respect to morphology. |
| rnfC deletion | decreases | MegL expression | *Fusobacterium nucleatum* ΔrnfC mutant | high | 10.1128/mbio.01751-23 | “the ΔrnfC mutant expressed a significantly reduced level of MegL” (britton2024therespiratoryenzyme pages 5-7) | Direct protein-expression consequence. |
| rnfC deletion | decreases | cysK1 and cysK2 expression | *Fusobacterium nucleatum* ΔrnfC mutant | medium | 10.1128/mbio.01751-23 | “the expression of both cysK1 and cysK2… was also reduced in the absence of rnfC” (britton2024therespiratoryenzyme pages 5-7) | Direct but reported in supplemental qRT-PCR context; still useful. |
| rnfC deletion | decreases | hydrogen sulfide production | *Fusobacterium nucleatum* ΔrnfC mutant | high | 10.1128/mbio.01751-23 | “the ΔrnfC mutant showed a significant defect in H2S production” (britton2024therespiratoryenzyme pages 5-7) | Direct metabolic phenotype. |
| reduced CysK1 activity/expression | may_decrease | lanthionine-dependent peptidoglycan formation | *Fusobacterium nucleatum* inferred from cited discussion | low | 10.1128/mbio.01751-23 | “the expression of both cysK1 and cysK2… was also reduced in the absence of rnfC” (britton2024therespiratoryenzyme pages 5-7) | Uncertain/inferred edge only; supporting note from evidence summary indicates CysK1 is linked to L-lanthionine for fusobacterial peptidoglycan, but exact quotation was not retrieved from readable text, so do not hard-curate yet. |
| *Helicobacter cetorum* | has_phenotype | fusiform cell body tapered at both ends | descriptive, non-causal morphology row | high | 10.3390/microorganisms11030634 | “H. cetorum having a slightly helical, fusiform cell body that is tapered at both ends.” (bansil2023motilityofdifferent pages 1-2) | Non-causal descriptive row defining phenotype scope; useful exemplar of fusiform morphology. |
| *Tannerella forsythia* | has_phenotype | fusiform bacterium | descriptive, non-causal morphology row | high | 10.1021/acs.jproteome.5b00878 | “T. forsythia is a Gram-negative, anaerobic, fusiform bacterium.” (veith2015tannerellaforsythiaouter pages 1-2) | Non-causal descriptive row; supports scope but not mechanism. |


*Table: This table summarizes evidence-backed candidate triples relevant to microbial fusiform morphology, separating direct mechanistic edges from descriptive non-causal phenotype rows. It is useful for deciding which claims are strong enough for TraitMech curation and which should remain provisional.*

### Recommended first-pass YAML backbone

The most defensible causal chain is:

- **MreB nucleotide-binding-pocket mutation** → `causes` → **polar MreB localization**
- **polar MreB localization** → `inferred_to_promote` → **aberrant polar peptidoglycan synthesis**
- **aberrant polar peptidoglycan synthesis** → `associated_with` → **extremely tapered/pointed poles**
- **extremely tapered/pointed poles** → `contributes_to` → `METPO:1000690` **[uncertain; geometry-component mapping]** (randich2015molecularmechanismsfor pages 7-9)

A separate *F. nucleatum* branch should be:

- **Rnf complex function** → `promotes` → **ATP production**
- `rnfC` deletion → `decreases` → **ATP production**
- `rnfC` deletion → `causes` → **short/stubby morphology**
- **short/stubby morphology** → `contrasts_with_or_reduces` → **normal elongated/fusiform morphology** **[uncertain final trait mapping]** (britton2024therespiratoryenzyme pages 5-7, britton2024therespiratoryenzyme media caddd5ad)

Do not yet merge the two branches into a universal Rnf→MreB→polar-PG pathway; no retrieved source demonstrates that connection.

## 5. Applications and real-world relevance

Fusiform morphology remains useful in **microscopy-supported taxonomic identification**, including recognition of *H. cetorum* and *T. forsythia*. (bansil2023motilityofdifferent pages 1-2, veith2015tannerellaforsythiaouter pages 1-2)

Morphology can also act as a **functional screening readout**. The 2024 Rnf experiment used electron microscopy to reveal a short/stubby phenotype following `rnfC` deletion, accompanying energy, metabolic, biofilm, and virulence defects. Rnf therefore represents a potential antimicrobial or anti-virulence target, but the morphology is currently a pleiotropic pharmacodynamic marker rather than a validated fusiform-specific endpoint. (britton2024therespiratoryenzyme pages 1-2, britton2024therespiratoryenzyme pages 5-7)

For experimental implementation, quantitative shape analysis should measure cell length, maximum width, the axial position of maximum width, and taper slopes toward each pole. This would distinguish true fusiform cells from rods, filaments, curved cells, and asymmetric tapering. The retrieved papers provide microscopy scale bars and qualitative classifications but not a standardized fusiform index or population-level taper statistics. (bansil2023motilityofdifferent pages 1-2, britton2024therespiratoryenzyme pages 5-7, britton2024therespiratoryenzyme media caddd5ad)

## 6. Recent data and statistics

- The 2024 Rnf study detected **more than 80 metabolites**; **10 were elevated and 7 depleted** in Δ`rnfC` relative to the parent strain. (britton2024therespiratoryenzyme pages 5-7)
- Biofilm, ATP, and related assays were reported from **three independent experiments performed in triplicate**, with statistical thresholds extending to *P* < 0.0001 depending on the comparison. (britton2024therespiratoryenzyme pages 5-7)
- The Δ`rnfC` strain retained parent-comparable colony-forming units over the examined growth period despite lower optical density and short/stubby morphology. (britton2024therespiratoryenzyme pages 5-7)
- The morphology review identifies **four** MreB nucleotide-pocket variants—E213G, D16G, N21D, and A325P—associated with extreme polar tapering. (randich2015molecularmechanismsfor pages 7-9)
- *T. forsythia* ATCC 43037 was reported with a **3,405,543-bp genome and 3,034 predicted open reading frames**, but these genomic statistics do not identify a fusiform-shape determinant. (posch2012glycobiologyaspectsof pages 1-3)

## 7. Expert interpretation

The best-supported general principle is that bacterial shape emerges from spatial regulation of peptidoglycan synthesis and remodeling rather than from a dedicated “fusiform gene.” MreB ordinarily helps orient wall synthesis to maintain cylindrical geometry; altered MreB localization can redirect synthesis toward poles and create tapering. (randich2015molecularmechanismsfor pages 7-9, egan2020regulationofpeptidoglycan pages 8-9)

The Rnf result adds a metabolic constraint: maintaining an elongated fusobacterial body evidently requires sufficient energy conservation and amino-acid metabolic homeostasis. However, because `rnfC` loss affects ATP, growth, biofilms, multiple metabolites, sulfur metabolism, and virulence, Rnf should be classified as a **pleiotropic upstream requirement**, not a dedicated shape-patterning module. (britton2024therespiratoryenzyme pages 1-2, britton2024therespiratoryenzyme pages 5-7)

Thus, the existing graph summary “fusiform_shaped_tapered_polar_growth” is directionally plausible, but its strongest direct support comes from *Caulobacter* tapered-pole mutants rather than a genetic study in a canonical fusiform species. Taxon provenance must be attached to every edge.

## 8. Warnings: claims not ready for TraitMech

1. **Do not curate a universal MreB→fusiform edge.** MreB is broadly associated with rod-shape maintenance, and its effects differ by taxon. (egan2020regulationofpeptidoglycan pages 8-9)
2. **Do not assert that Rnf directly patterns tapered poles.** Δ`rnfC` alters morphology, but no spatial wall-synthesis mechanism was shown. (britton2024therespiratoryenzyme pages 5-7)
3. **Do not curate CysK1/lanthionine→fusiform as established.** Reduced `cysK1` expression is documented, but the full bridge through lanthionine-containing peptidoglycan to tapering was not directly tested in the retrieved study. (britton2024therespiratoryenzyme pages 10-12, britton2024therespiratoryenzyme pages 5-7)
4. **Do not treat lysine as a shape inhibitor.** At 15 mM it inhibited RadD-mediated coaggregation; morphology was not the tested endpoint. (britton2024therespiratoryenzyme pages 5-7)
5. **Do not infer mechanism from taxonomic descriptions.** “Fusiform bacterium” establishes phenotype presence, not causation. (bansil2023motilityofdifferent pages 1-2, veith2015tannerellaforsythiaouter pages 1-2)
6. **Do not equate all pointed-pole mutants with `METPO:1000690`.** Bilateral tapering and central maximum width should be verified quantitatively.
7. **Do not generalize from *Caulobacter* to Fusobacteria without an explicit orthology and perturbation study.** The relevant MreB evidence is taxon-specific. (randich2015molecularmechanismsfor pages 7-9)
8. No direct 2023–2024 study was found that systematically maps fusiform geometry to a dedicated gene set, environmental variable, or standardized quantitative index. The 2024 Rnf paper is the most recent direct morphology perturbation found, but it is pleiotropic.

## DOI-first bibliography

1. Britton TA et al. **The respiratory enzyme complex Rnf is vital for metabolic adaptation and virulence in *Fusobacterium nucleatum*.** *mBio*. Published January 2024. DOI: [10.1128/mbio.01751-23](https://doi.org/10.1128/mbio.01751-23). (britton2024therespiratoryenzyme pages 5-7)
2. Bansil R et al. **Motility of Different Gastric *Helicobacter* spp.** *Microorganisms*. Published 1 March 2023. DOI: [10.3390/microorganisms11030634](https://doi.org/10.3390/microorganisms11030634). (bansil2023motilityofdifferent pages 1-2)
3. Egan AJF, Errington J, Vollmer W. **Regulation of peptidoglycan synthesis and remodelling.** *Nature Reviews Microbiology*. Published May 2020. DOI: [10.1038/s41579-020-0366-3](https://doi.org/10.1038/s41579-020-0366-3). (egan2020regulationofpeptidoglycan pages 8-9)
4. Randich AM, Brun YV. **Molecular mechanisms for the evolution of bacterial morphologies and growth modes.** *Frontiers in Microbiology*. Published June 2015. DOI: [10.3389/fmicb.2015.00580](https://doi.org/10.3389/fmicb.2015.00580). (randich2015molecularmechanismsfor pages 7-9)
5. Veith PD et al. ***Tannerella forsythia* Outer Membrane Vesicles Are Enriched with Substrates of the Type IX Secretion System and TonB-Dependent Receptors.** *Journal of Proteome Research*. Published 2015. DOI: [10.1021/acs.jproteome.5b00878](https://doi.org/10.1021/acs.jproteome.5b00878). (veith2015tannerellaforsythiaouter pages 1-2)
6. Posch G et al. **Glycobiology Aspects of the Periodontal Pathogen *Tannerella forsythia*.** *Biomolecules*. Published 11 October 2012. DOI: [10.3390/biom2040467](https://doi.org/10.3390/biom2040467). (posch2012glycobiologyaspectsof pages 1-3)

### Important primary source underlying the MreB mutant model

Dye NA et al. **Mutations in the nucleotide binding pocket of MreB can alter cell curvature and polar morphology in *Caulobacter*.** *Molecular Microbiology*. Published 2011. DOI: [10.1111/j.1365-2958.2011.07698.x](https://doi.org/10.1111/j.1365-2958.2011.07698.x). This source was identified through the retrieved review but its full text was unavailable in the tool corpus; therefore, the proposed edges above cite the accessible review and should be checked against the primary paper before final YAML acceptance. (randich2015molecularmechanismsfor pages 7-9)

References

1. (randich2015molecularmechanismsfor pages 7-9): Amelia M. Randich and Yves V. Brun. Molecular mechanisms for the evolution of bacterial morphologies and growth modes. Frontiers in Microbiology, Jun 2015. URL: https://doi.org/10.3389/fmicb.2015.00580, doi:10.3389/fmicb.2015.00580. This article has 105 citations and is from a peer-reviewed journal.

2. (britton2024therespiratoryenzyme pages 5-7): Timmie A. Britton, Chenggang Wu, Yi-Wei Chen, Dana Franklin, Yimin Chen, Martha I. Camacho, Truc T. Luong, Asis Das, and Hung Ton-That. The respiratory enzyme complex rnf is vital for metabolic adaptation and virulence in <i>fusobacterium nucleatum</i>. Jan 2024. URL: https://doi.org/10.1128/mbio.01751-23, doi:10.1128/mbio.01751-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

3. (britton2024therespiratoryenzyme media caddd5ad): Timmie A. Britton, Chenggang Wu, Yi-Wei Chen, Dana Franklin, Yimin Chen, Martha I. Camacho, Truc T. Luong, Asis Das, and Hung Ton-That. The respiratory enzyme complex rnf is vital for metabolic adaptation and virulence in <i>fusobacterium nucleatum</i>. Jan 2024. URL: https://doi.org/10.1128/mbio.01751-23, doi:10.1128/mbio.01751-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

4. (bansil2023motilityofdifferent pages 1-2): Rama Bansil, Maira A. Constantino, Clover Su-Arcaro, Wentian Liao, Zeli Shen, and James G. Fox. Motility of different gastric helicobacter spp. Microorganisms, 11:634, Mar 2023. URL: https://doi.org/10.3390/microorganisms11030634, doi:10.3390/microorganisms11030634. This article has 14 citations.

5. (posch2012glycobiologyaspectsof pages 1-3): Gerald Posch, Gerhard Sekot, Valentin Friedrich, Zoë A. Megson, Andrea Koerdt, Paul Messner, and Christina Schäffer. Glycobiology aspects of the periodontal pathogen tannerella forsythia. Biomolecules, 2:467-482, Oct 2012. URL: https://doi.org/10.3390/biom2040467, doi:10.3390/biom2040467. This article has 37 citations.

6. (veith2015tannerellaforsythiaouter pages 1-2): Paul D. Veith, Yu-Yen Chen, Dina Chen, Neil M. O’Brien-Simpson, Jessica D. Cecil, James A. Holden, Jason C. Lenzo, and Eric C. Reynolds. Tannerella forsythia outer membrane vesicles are enriched with substrates of the type ix secretion system and tonb-dependent receptors. Journal of proteome research, 14 12:5355-66, Nov 2015. URL: https://doi.org/10.1021/acs.jproteome.5b00878, doi:10.1021/acs.jproteome.5b00878. This article has 47 citations and is from a peer-reviewed journal.

7. (egan2020regulationofpeptidoglycan pages 8-9): Alexander J. F. Egan, Jeff Errington, and Waldemar Vollmer. Regulation of peptidoglycan synthesis and remodelling. Nature Reviews Microbiology, 18:446-460, May 2020. URL: https://doi.org/10.1038/s41579-020-0366-3, doi:10.1038/s41579-020-0366-3. This article has 693 citations and is from a highest quality peer-reviewed journal.

8. (britton2024therespiratoryenzyme pages 2-5): Timmie A. Britton, Chenggang Wu, Yi-Wei Chen, Dana Franklin, Yimin Chen, Martha I. Camacho, Truc T. Luong, Asis Das, and Hung Ton-That. The respiratory enzyme complex rnf is vital for metabolic adaptation and virulence in <i>fusobacterium nucleatum</i>. Jan 2024. URL: https://doi.org/10.1128/mbio.01751-23, doi:10.1128/mbio.01751-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (britton2024therespiratoryenzyme pages 1-2): Timmie A. Britton, Chenggang Wu, Yi-Wei Chen, Dana Franklin, Yimin Chen, Martha I. Camacho, Truc T. Luong, Asis Das, and Hung Ton-That. The respiratory enzyme complex rnf is vital for metabolic adaptation and virulence in <i>fusobacterium nucleatum</i>. Jan 2024. URL: https://doi.org/10.1128/mbio.01751-23, doi:10.1128/mbio.01751-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

10. (britton2024therespiratoryenzyme pages 10-12): Timmie A. Britton, Chenggang Wu, Yi-Wei Chen, Dana Franklin, Yimin Chen, Martha I. Camacho, Truc T. Luong, Asis Das, and Hung Ton-That. The respiratory enzyme complex rnf is vital for metabolic adaptation and virulence in <i>fusobacterium nucleatum</i>. Jan 2024. URL: https://doi.org/10.1128/mbio.01751-23, doi:10.1128/mbio.01751-23. This article has 17 citations and is from a domain leading peer-reviewed journal.