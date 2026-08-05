---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:31:49.095420'
end_time: '2026-08-04T09:37:58.683741'
duration_seconds: 369.59
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pink pigmented
  trait_identifier: METPO:1003027
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: pink_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    pink due to accumulation of pink or rose carotenoid pigments.
  parent_traits: METPO:1003021
  synonyms: Pigment_pink
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow
    pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated
    color phenotype.)'
  causal_graph_summary: 'pink_pigmented_carotenoid_color: 10 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pink pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003027
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear pink due to accumulation of pink or rose carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_pink
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated color phenotype.)
- **Existing causal graph summary:** pink_pigmented_carotenoid_color: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **pink pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pink_pigmented.yaml`.

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
- **Trait label:** pink pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003027
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear pink due to accumulation of pink or rose carotenoid pigments.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_pink
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports pink bacterial pigmentation as a carotenoid-associated color phenotype.)
- **Existing causal graph summary:** pink_pigmented_carotenoid_color: 10 nodes, 11 edges

## Research Objective

Research the microbial trait **pink pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pink_pigmented.yaml`.

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


# Curation report: microbial **pink pigmented**

## 1. Scope and recommended interpretation

**Target:** `METPO:1003027` (quote verbatim)  
**Category:** morphology; **term kind:** class; **status:** reviewed  
**Parent:** `METPO:1003021`  
**Synonym:** *Pigment_pink*

The trait should represent an **observed colony- or cell-level color phenotype**, not merely genomic capacity for carotenoid synthesis. Operationally, it is the appearance of a pink or rose color caused by intracellular or membrane-associated accumulation of colored metabolites, most often carotenoids. The strongest causal evidence retrieved is from *Methylobacterium extorquens* PA1: LC–MS and mutant/complementation experiments show that pigmentation depends on a **squalene-derived C30 carotenoid pathway**, rather than the previously presumed canonical C40 phytoene pathway (rizk2021functionaldiversityof pages 2-3).

Pink is not chemically unique. In *Rhodotorula*, colony colors form an orange–salmon–pink–red continuum determined by pigment composition and concentration; reported carotenoids include β-carotene, γ-carotene, lycopene, torulene, and torularhodin. Thus, color alone does not identify a particular molecule or pathway (ochoavinals2024currentadvancesin pages 1-2).

### Boundary cases

1. **Pink versus red, salmon, or orange:** These are neighboring assay categories, not necessarily distinct pathways. Lighting, medium, colony age, pigment concentration, and observer thresholds can change the assigned color.
2. **Pigment-production capacity versus observed pigmentation:** A complete biosynthetic gene cluster predicts capacity but is insufficient for `METPO:1003027` unless pink color is actually observed.
3. **PPFM versus pink pigmentation:** “Pink-pigmented facultative methylotroph” combines color and C1 metabolism. Methanol growth is not part of this morphology trait and should be represented separately.
4. **Carotenoid pigmentation versus other pigments:** The supplied definition restricts the class to pink/rose carotenoids. Pink caused by unrelated pigments, medium indicators, adsorbed compounds, host material, or mixed cultures should not be included without revising the definition.
5. **Stress response versus constitutive morphology:** Stress-induced red-pink astaxanthin accumulation in *Phaffia rhodozyma* is relevant but conditional and taxon-specific, rather than a universal mechanism (florescotera2021decipheringthemechanism pages 1-2).

## 2. Current mechanistic understanding

### 2.1 Strongest bacterial mechanism: squalene-derived C30 carotenoids

In *M. extorquens* PA1, all detected carotenoids had C30 backbones. Deleting `crtN` or `crtP` abolished pigmentation, and complementation restored it. By contrast, deleting `crtB`, associated with C40 phytoene production, did not alter pigmentation under the tested conditions. This establishes a causal chain from squalene production through the C30 pathway to visible pigmentation (rizk2021functionaldiversityof pages 2-3).

The carotenoids occur in the outer membrane. Carotenoid-deficient mutants did not show major growth defects over 10–34°C or substantial membrane-permeability changes, but showed slightly increased hydrogen-peroxide/oxidative-stress sensitivity. Therefore, oxidative protection is a supported secondary function, but it should not be represented as necessary for pink color (rizk2021functionaldiversityof pages 9-11).

### 2.2 Fungal C40 carotenoid mechanisms

Recent synthesis for *Rhodotorula* describes HMG-CoA-dependent isoprenoid precursor supply, `CRTYB`-encoded phytoene synthesis from geranylgeranyl diphosphate, and `CRTI`-mediated desaturation toward neurosporene and downstream carotenoids. γ-Carotene precedes β-carotene and torulene, while torulene is hydroxylated and oxidized to torularhodin. These reactions explain pink-to-red yeast pigmentation, but they must not be merged with the bacterial C30 mechanism as though they were one universal pathway (ochoavinals2024currentadvancesin pages 2-5).

For *Rhodotorula* sp. CP72-2, genome analysis found putative `CrtE`, `CrtYB`, `CrtI`, `CrtS`, `CrtR`, `CrtW`, `CrtO`, and `CrtZ` genes. Because these assignments were genomic candidates rather than individual knockout or enzyme-kinetic demonstrations, they are lower-confidence causal nodes (kingkaew2023genomicinsightand pages 1-2).

### 2.3 Environmental control

In *P. rhodozyma*, nitrogen or copper limitation, antimycin A, and mutations affecting respiration or nitrogen metabolism are associated with intense red-pink astaxanthin accumulation. The proposed convergence mechanism is an NADH/NAD+ imbalance in an oxidative environment, but the source explicitly treats the complete signaling mechanism as unresolved (florescotera2021decipheringthemechanism pages 1-2).

In *Rhodotorula*, light, pH, salts, metals, and carbon-to-nitrogen ratio influence carotenoid accumulation. Low C/N generally favors carotenoids, whereas high C/N promotes lipids. These are fermentation- and strain-dependent modifiers rather than defining causes of the trait (ochoavinals2024currentadvancesin pages 1-2, ochoavinals2024currentadvancesin pages 2-5).

## 3. Candidate nodes

### Trait and observational nodes

- `METPO:1003027` — pink pigmented
- `METPO:1003021` — supplied parent trait
- pink/rose colony pigmentation — label-only observational node
- orange, salmon, red pigmentation — label-only boundary states
- pigment concentration — experimental/quantitative factor
- colony age, growth medium, illumination, observation method — assay factors

### Pathways and biological processes

- C30 carotenoid biosynthesis from squalene — label-only pathway; strongest in *M. extorquens* PA1
- C40 carotenoid biosynthesis from geranylgeranyl diphosphate — label-only pathway
- carotenoid biosynthetic process — `GO:0016117`
- isoprenoid biosynthetic process — use only after identifier verification in the target ontology release
- oxidative-stress response — label or verified GO term during implementation
- carotenoid accumulation — label-only process

### Genes, proteins, and modules

- `hpnC`, `hpnD`, `hpnE` / HpnCDE — squalene-producing module; taxon-specific role in precursor supply
- `crtN` — C30 carotenoid-pathway enzyme; required for PA1 pigmentation
- `crtP` — C30 carotenoid-pathway enzyme; required for PA1 pigmentation
- `crtB` — phytoene synthase candidate; negative evidence for PA1 pigmentation under standard conditions
- `CRTYB` — bifunctional fungal phytoene synthase/lycopene cyclase
- `CRTI` — fungal phytoene desaturase
- `CrtE`, `CrtS`, `CrtR`, `CrtW`, `CrtO`, `CrtZ` — candidate astaxanthin-pathway proteins; retain as label-only unless exact species-specific accessions are curated

Gene symbols should not be treated as universally equivalent functions. Exact UniProt, EC, Rhea, KEGG, or MetaCyc grounding should be added only after species and reaction identity are verified.

### Chemicals and metabolites

- squalene — `CHEBI:15440`
- geranylgeranyl diphosphate — `CHEBI:57533`
- phytoene — `CHEBI:26119`
- lycopene — `CHEBI:15948`
- β-carotene — `CHEBI:17579`
- γ-carotene — verify database identifier before curation
- neurosporene — verify identifier
- torulene — verify identifier
- torularhodin — verify identifier
- astaxanthin — `CHEBI:40968`
- reactive oxygen species and hydrogen peroxide — add verified CHEBI identifiers during implementation
- NADH/NAD+ redox pair — add verified CHEBI identifiers if the conditional yeast mechanism is represented

### Localization and environmental nodes

- bacterial outer membrane — `GO:0009279`
- intracellular lipid droplets in red yeasts — relevant to sequestration, but no direct trait edge should be added from the evidence set without a localization-specific primary source
- temperature, pH, light, C/N ratio, nutrient limitation, copper limitation, antimycin A, and cultivation duration — experimental/environmental nodes

## 4. Candidate causal edges

The following table separates direct genetic evidence from review-supported, predicted, and taxon-limited relationships.

| subject | predicate | object | evidence strength/taxon | DOI | short supporting snippet | curation note |
|---|---|---|---|---|---|---|
| HpnCDE / squalene biosynthesis | supplies precursor for | C30 carotenoid biosynthesis pathway | High; direct genetics/LC-MS; *Methylobacterium extorquens* PA1 | 10.1111/mmi.14794 | “carotenoid biosynthesis utilizes squalene as a precursor resulting in pigmentation with a C30 backbone” (rizk2021functionaldiversityof pages 2-3) | Good candidate generic mechanism node, but direct causal evidence is currently strongest in *M. extorquens* PA1. |
| squalene-derived C30 carotenoid pathway | produces | carotenoid pigmentation | High; direct genetics/LC-MS; *M. extorquens* PA1 | 10.1111/mmi.14794 | “all detected carotenoids possessed C30 backbones with no C40 structures present” (rizk2021functionaldiversityof pages 2-3) | Strong evidence that visible pigmentation is mediated by a non-canonical C30 pathway in this taxon. |
| crtN | enables | pigmentation | High; knockout/complementation; *M. extorquens* PA1 | 10.1111/mmi.14794 | “deletion of crtN and crtP genes in the C30 pathway caused loss of pigmentation” (rizk2021functionaldiversityof pages 2-3) | Curate as taxon-specific unless broader conservation is independently sourced. |
| crtP | enables | pigmentation | High; knockout/complementation; *M. extorquens* PA1 | 10.1111/mmi.14794 | “deletion of crtN and crtP genes in the C30 pathway caused loss of pigmentation” (rizk2021functionaldiversityof pages 2-3) | Same as above; strong for this lineage. |
| deletion of crtN/crtP | causes loss of | pigmentation | High; direct mutant phenotype; *M. extorquens* PA1 | 10.1111/mmi.14794 | “caused loss of pigmentation” and “no pigmentation was observed in mutants with disrupted C30 carotenoid synthesis” (rizk2021functionaldiversityof pages 2-3) | Very strong edge for phenotype loss under tested conditions. |
| complementation of carotenoid-deficient mutants | restores | pigmentation | High; direct complementation; *M. extorquens* PA1 | 10.1111/mmi.14794 | “Gene complementation studies restored pigmentation in the non-pigmented mutant strains” (rizk2021functionaldiversityof pages 2-3) | Strong rescue evidence; useful as confirmatory support rather than a standalone generic edge. |
| C30 carotenoids | localize to | outer membrane | Moderate; direct study summary; *M. extorquens* PA1 | 10.1111/mmi.14794 | “Methylobacterium extorquens contains hopanoids and carotenoids in their outer membrane” (rizk2021functionaldiversityof pages 2-3) | Suitable candidate node/edge if localization is needed; taxon-specific. |
| loss of carotenoid synthesis | modestly increases sensitivity to | hydrogen peroxide / oxidative stress | Moderate; direct phenotype; *M. extorquens* PA1 | 10.1111/mmi.14794 | “slightly increased sensitivity to oxidative stress” and “carotenoid deficiency increased sensitivity to hydrogen peroxide stress” (rizk2021functionaldiversityof pages 9-11) | Supportive function edge; not specific to pink color itself. |
| crtB / C40 phytoene pathway | does not explain | pigmentation under tested conditions | High; direct negative result; *M. extorquens* PA1 | 10.1111/mmi.14794 | “deletion of crtB (C40 pathway) had no effect” and the “C40 pathway is non-functional under standard growth conditions” (rizk2021functionaldiversityof pages 2-3) | Important exclusion edge; curate with explicit condition/taxon notes. |
| CRTYB | converts | geranylgeranyl pyrophosphate (GGPP) to phytoene | Moderate; review-supported; fungal/yeast carotenoid pathway | 10.3390/fermentation10040190 | “phytoene synthase (CRTYB, forming phytoene from GGPP)” (ochoavinals2024currentadvancesin pages 2-5) | Mechanistically useful but from review synthesis; not specific to pink phenotype. |
| CRTI | desaturates | phytoene toward neurosporene/lycopene | Moderate; review-supported; fungal/yeast carotenoid pathway | 10.3390/fermentation10040190 | “phytoene desaturase (CRTI, producing neurosporene). The pathway branches to form lycopene or β-zeacarotene” (ochoavinals2024currentadvancesin pages 2-5) | Use as pathway background; taxon/pathway-specific and review-derived. |
| gamma-carotene | precedes | beta-carotene / torulene | Moderate; review-supported; *Rhodotorula* spp. | 10.3390/fermentation10040190 | “γ-carotene serves as precursor for β-carotene and torulene” (ochoavinals2024currentadvancesin pages 2-5) | Candidate metabolic edge for yeasts; not yet generic across microbes. |
| torulene oxidation / hydroxylation | yields | torularhodin | Moderate; review-supported; *Rhodotorula* spp. | 10.3390/fermentation10040190 | “Torulene … is converted to torularhodin … via hydroxylation and oxidation” (ochoavinals2024currentadvancesin pages 2-5) | Useful for pigment chemistry branch; review-based and lineage-specific. |
| carotenoid accumulation | results in | orange–salmon–pink–red phenotype range | Moderate; review-supported; *Rhodotorula* spp. | 10.3390/fermentation10040190 | “Colony pigmentation varies from orange to salmon, pink, and red depending on pigment type and concentration” (ochoavinals2024currentadvancesin pages 1-2) | Valuable boundary-case note: pink is a color class within a continuum, not a single pigment. |
| redox imbalance / nutrient or toxic stress | induces | astaxanthin accumulation | Moderate; review-supported; *Phaffia rhodozyma* | 10.1093/jimb/kuab048 | “produces intense red-pink coloration under stress conditions including nutrient limitation … toxic substances” and induction is “linked to NADH/NAD+ redox imbalances” (florescotera2021decipheringthemechanism pages 1-2) | Not suitable for generic bacterial curation; yeast- and stress-context specific. |
| astaxanthin accumulation | contributes to | antioxidant defense / ROS protection | Moderate; review-supported; *Phaffia rhodozyma* | 10.1093/jimb/kuab048 | “functions as a primary antioxidant defense against reactive oxygen species” (florescotera2021decipheringthemechanism pages 1-2) | Functional support for pigmented state, but not a direct determinant of pink color class. |
| cultivation pH 4.5, 25°C, glucose 50 g/L, 3-day cultivation | increases production of | astaxanthin in *Rhodotorula* sp. CP72-2 | Moderate; primary study but production optimization/genomic context; *Rhodotorula* sp. CP72-2 | 10.3390/fermentation9060501 | “most efficient conditions for astaxanthin production were glucose (50 g/L), pH 4.5, 25 °C, and three days of cultivation” (kingkaew2023genomicinsightand pages 1-2) | Specific optimization edge; not appropriate as generic pink-pigmentation mechanism. |
| CrtE/CrtYB/CrtI/CrtS/CrtR/CrtW/CrtO/CrtZ genes | indicate genomic capacity for | astaxanthin biosynthesis | Low–moderate; genomic prediction; *Rhodotorula* sp. CP72-2 | 10.3390/fermentation9060501 | “Eight putative astaxanthin biosynthesis genes … were detected” (kingkaew2023genomicinsightand pages 1-2) | Mark as genomic-prediction only; do not equate presence with pink phenotype without expression/phenotype data. |
| carbon/nitrogen ratio, light, pH, salts, heavy metals | influence | carotenoid accumulation in *Rhodotorula* | Moderate; review-supported environmental factors | 10.3390/fermentation10040190 | “Environmental factors affecting carotenoid accumulation include light, pH, salts, and heavy metal tolerance” and “low C/N favors carotenoids” (ochoavinals2024currentadvancesin pages 1-2, ochoavinals2024currentadvancesin pages 2-5) | Useful assay/environment modulators; not direct universal mechanism for METPO:1003027. |
| complete carotenoid gene pathway in genomes | predicts | pigment production capacity | Low; inference only; Binatota genomes | 10.1128/mbio.00985-21 | “Pigmentation is inferred from a complete pathway for carotenoids production” (rizk2021functionaldiversityof pages 2-3) | Not suitable for direct TraitMech curation of pink pigmentation because phenotype was inferred, not observed. |


*Table: This table compiles candidate causal edges for METPO:1003027 pink pigmented, separating high-confidence direct genetic evidence from review-based, genomic-prediction, and taxon-specific claims. It is designed to help curators decide which mechanisms are appropriate for generic TraitMech inclusion versus which should remain lineage- or assay-limited.*

### Recommended minimal graph core

For an initial conservative revision of `pink_pigmented.yaml`, the most defensible core is:

1. **HpnCDE-dependent squalene biosynthesis → supplies → squalene**.
2. **Squalene → precursor_for → C30 carotenoid biosynthesis**.
3. **`crtN` → positively_regulates/enables → C30 carotenoid formation**.
4. **`crtP` → positively_regulates/enables → C30 carotenoid formation**.
5. **C30 carotenoid formation → causes → visible carotenoid pigmentation**.
6. **Visible carotenoid accumulation → causes → `METPO:1003027`**, with the final color edge explicitly conditional on concentration, medium, and observation.
7. **C30 carotenoids → located_in → outer membrane**.
8. **C30 carotenoids → contributes_to → hydrogen-peroxide tolerance**, marked secondary and taxon-specific.

Edges 1–8 should carry a *M. extorquens* PA1 taxon qualifier. A separate fungal branch may be added only if TraitMech supports taxon-qualified alternative mechanisms.

## 5. Recent developments, applications, and quantitative data

### Recent research

- A 2024 *Rhodotorula* review consolidates fermentation regulation, pathway engineering, inexpensive feedstocks, and stress-based enhancement strategies. It reports that β-carotene can constitute approximately **70% of total carotenoids** in some reviewed *Rhodotorula* contexts, while emphasizing that pigment composition varies among strains and conditions (ochoavinals2024currentadvancesin pages 1-2).
- A 2023 study of *Rhodotorula* sp. CP72-2 identified eight putative astaxanthin-associated genes in a **21.36-Mbp, 64.90% GC** genome and found optimal tested production at **50 g/L glucose, pH 4.5, 25°C, and three days**. These conditions are strain-specific optimization results, not universal determinants of pink pigmentation (kingkaew2023genomicinsightand pages 1-2).
- Reported production values summarized in 2024 include **2.59 mg/L** carotenoids for *R. kratochvilovae* Y-42 at C/N 80, **121.3 µg/g** for one *R. mucilaginosa* context, and **1.6 mg/g** for *R. glutinis* JMT 21978 at C/N 50:1, with torulene comprising **30%** in the latter example. Cross-study comparisons are limited by different strains, denominators, extraction procedures, and culture conditions (ochoavinals2024currentadvancesin pages 2-5).

### Applications and implementation status

Pink/red microbial carotenoids are being developed as natural colorants, antioxidants, feed additives, and ingredients for food, cosmetics, and pharmaceutical formulations. *Rhodotorula* fermentation increasingly uses molasses, glycerol, wastewater-derived nutrients, and lignocellulosic substrates, while genetic engineering and stress-based cultivation seek higher yields (ochoavinals2024currentadvancesin pages 1-2). Astaxanthin production has particular relevance to aquaculture, food, cosmetics, and pharmaceutical research, although genomic pathway detection does not by itself establish commercial performance (kingkaew2023genomicinsightand pages 1-2).

PPFMs are also studied as plant-associated inoculants. However, crop-growth promotion, methylotrophy, drought effects, and bioremediation are organism-level applications—not consequences of pink pigmentation itself—and should not be encoded downstream of `METPO:1003027` without experiments that isolate pigment function.

## 6. Expert assessment

The key expert conclusion is that **“pink pigmented” is an emergent optical phenotype with multiple mechanistic realizations**, not a synonym for one carotenoid or one biosynthetic pathway. The strongest direct graph is the squalene-derived C30 mechanism in *M. extorquens* PA1. Recent fungal literature supports an alternative C40 branch involving `CRTYB`, `CRTI`, torulene/torularhodin, or astaxanthin, but much of that evidence is review-level, strain-specific, or based on genomic prediction (rizk2021functionaldiversityof pages 2-3, ochoavinals2024currentadvancesin pages 1-2, kingkaew2023genomicinsightand pages 1-2, ochoavinals2024currentadvancesin pages 2-5).

Accordingly, TraitMech should use **taxon-qualified alternative branches** rather than a single universal linear pathway. The final metabolite-to-color edge should also carry an assay/context qualifier because pigment concentration and composition determine whether a culture is called pink, salmon, orange, or red.

## 7. Claims not yet ready for curation

- Do not assert that all pink microbes use C30 carotenoids; this is directly established only for the studied *M. extorquens* lineage.
- Do not assign β-carotene, astaxanthin, torularhodin, or any single carotenoid as the universal cause of pink color.
- Do not infer pink pigmentation solely from a complete carotenoid gene cluster. Genomic pathway completion establishes potential, not color, expression, or pigment concentration.
- Do not treat `crtB` as causal for PA1 pigmentation; its deletion had no effect under the tested conditions (rizk2021functionaldiversityof pages 2-3).
- Do not curate the proposed NADH/NAD+ stress-sensing mechanism as settled; it remains a model for *P. rhodozyma* (florescotera2021decipheringthemechanism pages 1-2).
- Do not generalize strain-specific production conditions or yields to the trait class.
- Do not make methylotrophy, plant growth promotion, drought amelioration, radiation resistance, or industrial utility downstream effects of pink morphology without pigment-specific perturbation evidence.
- Do not add exact UniProt/Rhea/KEGG/MetaCyc accessions for `crtN`, `crtP`, or fungal `CRT*` proteins until species-specific reactions and accessions are checked.
- The supplied 2025 review DOI `10.1080/1040841X.2025.2526423` is useful as broad supporting evidence for red/pink/orange/yellow bacterial carotenoid phenotypes, but it falls outside the requested 2023–2024 priority window and should not replace direct genetic evidence.

## 8. DOI-first bibliography

1. **Rizk S, et al.** “Functional diversity of isoprenoid lipids in *Methylobacterium extorquens* PA1.” *Molecular Microbiology* 116:1064–1078. **August 2021.** DOI: [10.1111/mmi.14794](https://doi.org/10.1111/mmi.14794). Direct knockout, complementation, LC–MS, localization, and stress evidence (rizk2021functionaldiversityof pages 2-3, rizk2021functionaldiversityof pages 9-11).
2. **Ochoa-Viñals N, et al.** “Current Advances in Carotenoid Production by *Rhodotorula* sp.” *Fermentation* 10:190. **March 2024.** DOI: [10.3390/fermentation10040190](https://doi.org/10.3390/fermentation10040190). Recent pathway, environmental-regulation, yield, and application review (ochoavinals2024currentadvancesin pages 1-2, ochoavinals2024currentadvancesin pages 2-5).
3. **Kingkaew E, et al.** “Genomic Insight and Optimization of Astaxanthin Production from a New *Rhodotorula* sp. CP72-2.” *Fermentation* 9:501. **May 2023.** DOI: [10.3390/fermentation9060501](https://doi.org/10.3390/fermentation9060501). Genomic candidates and strain-specific optimization (kingkaew2023genomicinsightand pages 1-2).
4. **Flores-Cotera LB, et al.** “Deciphering the mechanism by which the yeast *Phaffia rhodozyma* responds adaptively to environmental, nutritional, and genetic cues.” *Journal of Industrial Microbiology & Biotechnology* 48. **July 2021.** DOI: [10.1093/jimb/kuab048](https://doi.org/10.1093/jimb/kuab048). Stress-induced red-pink astaxanthin and proposed redox mechanism (florescotera2021decipheringthemechanism pages 1-2).
5. **Sandmann G.** “Genes and Pathway Reactions Related to Carotenoid Biosynthesis in Purple Bacteria.” *Biology* 12:1346. **October 2023.** DOI: [10.3390/biology12101346](https://doi.org/10.3390/biology12101346). Authoritative recent review of bacterial `crt` reactions; useful background, but not specific proof of pink morphology.
6. **Mo X, et al.** “Characterization of C30 carotenoid and identification of its biosynthetic gene cluster in *Methylobacterium extorquens* AM1.” *Synthetic and Systems Biotechnology* 8:527–535. **August 2023.** DOI: [10.1016/j.synbio.2023.08.002](https://doi.org/10.1016/j.synbio.2023.08.002). Highly relevant recent source for future full-text verification before adding AM1-specific edges.
7. **Van Dien SJ, et al.** “Genetic characterization of the carotenoid biosynthetic pathway in *Methylobacterium extorquens* AM1 and isolation of a colorless mutant.” *Applied and Environmental Microbiology* 69:7563–7566. **December 2003.** DOI: [10.1128/AEM.69.12.7563-7566.2003](https://doi.org/10.1128/AEM.69.12.7563-7566.2003). Foundational genetics; pathway interpretation should be reconciled with later C30 evidence.
8. **Murphy CL, et al.** “Genomic Analysis of the Yet-Uncultured Binatota Reveals Broad Methylotrophic, Alkane-Degradation, and Pigment Production Capacities.” *mBio* 12:e00985-21. **June 2021.** DOI: [10.1128/mbio.00985-21](https://doi.org/10.1128/mbio.00985-21). Genomic inference only; not evidence of observed pink pigmentation.
9. **Mondal P, et al.** “Bioprospects of pink pigmented facultative methylotrophs.” *Arab Gulf Journal of Scientific Research* 42:1849–1863. **March 2024.** DOI: [10.1108/AGJSR-03-2023-0127](https://doi.org/10.1108/AGJSR-03-2023-0127). Recent applications review; organism-level benefits should not be attributed directly to color.
10. **Existing supplied evidence:** “red, pink, orange, and yellow pigmentation in bacteria.” **2025.** DOI: [10.1080/1040841X.2025.2526423](https://doi.org/10.1080/1040841X.2025.2526423). Broad phenotype support; secondary to direct mechanistic studies.

References

1. (rizk2021functionaldiversityof pages 2-3): Sandra Rizk, Petra Henke, Carlos Santana‐Molina, Gesa Martens, Marén Gnädig, Ngoc Anh Nguyen, Damien P. Devos, Meina Neumann‐Schaal, and James P. Saenz. Functional diversity of isoprenoid lipids in <i>methylobacterium extorquens</i> pa1. Molecular Microbiology, 116:1064-1078, Aug 2021. URL: https://doi.org/10.1111/mmi.14794, doi:10.1111/mmi.14794. This article has 26 citations and is from a domain leading peer-reviewed journal.

2. (ochoavinals2024currentadvancesin pages 1-2): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 57 citations.

3. (florescotera2021decipheringthemechanism pages 1-2): Luis B Flores-Cotera, Cipriano Chávez-Cabrera, Anahi Martínez-Cárdenas, Sergio Sánchez, and Oscar Ulises García-Flores. Deciphering the mechanism by which the yeast phaffia rhodozyma responds adaptively to environmental, nutritional, and genetic cues. Journal of Industrial Microbiology & Biotechnology, Jul 2021. URL: https://doi.org/10.1093/jimb/kuab048, doi:10.1093/jimb/kuab048. This article has 24 citations and is from a peer-reviewed journal.

4. (rizk2021functionaldiversityof pages 9-11): Sandra Rizk, Petra Henke, Carlos Santana‐Molina, Gesa Martens, Marén Gnädig, Ngoc Anh Nguyen, Damien P. Devos, Meina Neumann‐Schaal, and James P. Saenz. Functional diversity of isoprenoid lipids in <i>methylobacterium extorquens</i> pa1. Molecular Microbiology, 116:1064-1078, Aug 2021. URL: https://doi.org/10.1111/mmi.14794, doi:10.1111/mmi.14794. This article has 26 citations and is from a domain leading peer-reviewed journal.

5. (ochoavinals2024currentadvancesin pages 2-5): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 57 citations.

6. (kingkaew2023genomicinsightand pages 1-2): Engkarat Kingkaew, Nisachon Tedsree, Sukanya Phuengjayaem, Pornchai Rojsitthisak, Boonchoo Sritularak, Worathat Thitikornpong, Somphob Thompho, Wuttichai Mhuantong, and Somboon Tanasupawat. Genomic insight and optimization of astaxanthin production from a new rhodotorula sp. cp72-2. Fermentation, 9:501, May 2023. URL: https://doi.org/10.3390/fermentation9060501, doi:10.3390/fermentation9060501. This article has 13 citations.