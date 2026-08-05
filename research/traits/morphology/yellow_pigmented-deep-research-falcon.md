---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:30:30.094081'
end_time: '2026-08-04T10:36:46.891636'
duration_seconds: 376.8
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: yellow pigmented
  trait_identifier: METPO:1003030
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: yellow_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    yellow due to production of yellow pigments such as carotenoids.
  parent_traits: METPO:1003021
  synonyms: Pigment_yellow
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow
    pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated
    bacterial color phenotype.)'
  causal_graph_summary: 'yellow_pigmented_carotenoid_color: 15 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** yellow pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003030
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear yellow due to production of yellow pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_yellow
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated bacterial color phenotype.)
- **Existing causal graph summary:** yellow_pigmented_carotenoid_color: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **yellow pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/yellow_pigmented.yaml`.

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
- **Trait label:** yellow pigmented
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003030
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear yellow due to production of yellow pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_yellow
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: red, pink, orange, and yellow pigmentation in bacteria (Supports yellow microbial pigmentation as a carotenoid-associated bacterial color phenotype.)
- **Existing causal graph summary:** yellow_pigmented_carotenoid_color: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **yellow pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/yellow_pigmented.yaml`.

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


# Curation report: microbial “yellow pigmented”

**Target:** `METPO:1003030`  
**Category:** MORPHOLOGY | **Kind:** CLASS | **Mapping:** REVIEWED  
**Parent:** `METPO:1003021` | **Synonym:** *Pigment_yellow*

## 1. Scope and current interpretation

`METPO:1003030` should represent an **observed yellow appearance of microbial colonies or cells under stated assay conditions**, not merely possession of a pigment-biosynthesis gene or the ability to produce an extractable pigment. The proximate cause is accumulation of chromophores whose visible absorption produces a yellow phenotype. Carotenoids are especially important: they are lipid-soluble isoprenoids, generally absorb at 440–520 nm, and span yellow through deep-red colors depending on structure. Bacteria principally derive them through the MEP/DOXP or mevalonate precursor pathways. More than 700 carotenoid varieties have been described, emphasizing that color does not uniquely identify a compound (huang2024bacterialpigmentsas pages 3-4).

The strongest experimentally resolved examples are **β-carotene, zeaxanthin, and nostoxanthin**. In *Novosphingobium aromaticivorans*, both a zeaxanthin-accumulating `ΔcrtG` mutant and a β-carotene-accumulating `ΔcrtGΔcrtZ` mutant formed yellow colonies; the authors explicitly noted that colonies can look similar despite containing different carotenoids because their absorption spectra overlap (hall2023productionofcarotenoids pages 2-6). Thus, yellow appearance is a morphological endpoint downstream of several possible chemistries—not a synonym for “carotenoid producer.”

### Boundary cases

Include only when the cells or colonies themselves are documented as yellow:

- **Include:** yellow or deep-yellow colony/cell pigmentation supported by visual observation, colorimetry, or a linked pigment assay.
- **Do not automatically include:** an organism carrying `crt` genes without observed yellow color; genomic prediction is insufficient.
- **Distinguish from adjacent colors:** lycopene accumulation can produce red or light-pink colonies, whereas phytoene is colorless. Orange, golden, cream, tan, and pink phenotypes require explicit mapping policy rather than automatic inclusion (hall2023productionofcarotenoids pages 2-6, liu2021engineeringsphingobiumsp. pages 2-4).
- **Distinguish from medium pigmentation:** secreted yellow pigment that colors the supernatant is a pigment-production phenotype unless cell/colony color is also demonstrated.
- **Distinguish from fluorescence:** yellow fluorescence under excitation is not necessarily yellow pigmentation in visible reflected light.
- **Non-carotenoid boundary:** flexirubin-type pigments, xanthomonadins, aryl polyenes, and some melanins can appear yellow. They belong in this trait only where yellow colony/cell appearance is documented; their pathways should remain separate from the carotenoid branch.
- **Condition dependence:** temperature, pH, nutrients, light, oxygen, growth phase, and medium can alter pigment abundance. Record assay conditions rather than treating color as invariably expressed.

## 2. Recommended graph architecture

A useful graph should separate:

1. **precursor supply**—MEP/DOXP or MVA pathway → IPP/DMAPP → GGPP;
2. **carotenoid pathway**—GGPP → phytoene → lycopene → β-carotene → zeaxanthin → caloxanthin/nostoxanthin;
3. **regulation and environment**—for example, cAMP–CRP regulation and culture conditions;
4. **physical accumulation/localization**—cell-associated or membrane-associated carotenoid;
5. **assay endpoint**—yellow colony/cell appearance (`METPO:1003030`).

This avoids asserting that every upstream carotenoid step directly causes yellow color: phytoene is colorless and lycopene is generally red, while pathway blocks can change the final hue (liu2021engineeringsphingobiumsp. pages 4-5, liu2021engineeringsphingobiumsp. pages 2-4).

## 3. Candidate nodes grouped by type

### Trait and assay nodes

- Yellow pigmented — `METPO:1003030`
- Pigmentation phenotype — `METPO:1003021`
- Yellow colony appearance — label-only assay endpoint
- Yellow cell appearance — label-only assay endpoint
- Nonpigmented colony; light-pink colony; red colony; deep-yellow colony — label-only comparator states
- HPLC/UV–visible carotenoid detection; LC–MS pigment identification; visual colony-color screening — label-only experimental nodes

### Pathways and biological processes

- Carotenoid biosynthetic process — `GO:0016117`
- Isoprenoid biosynthetic process — `GO:0008299`
- MEP/DOXP pathway — label plus pathway-database mapping after curator verification
- Mevalonate pathway — label plus pathway-database mapping after curator verification
- β-carotene biosynthesis, zeaxanthin biosynthesis, nostoxanthin biosynthesis — label-only until exact pathway identifiers are verified
- Carotenoid accumulation; pigment accumulation; response to oxidative stress; photoprotection — GO grounding should be selected only after matching the precise experimental claim

### Genes, proteins, and enzymes

- `crtE` / geranylgeranyl-diphosphate synthase
- `crtB` / phytoene synthase
- `crtI` / phytoene desaturase
- `crtY` or `crtYcd` / lycopene β-cyclase
- `crtZ` / β-carotene hydroxylase
- `crtG` / 2,2′-β-ionone-ring hydroxylase
- `crtW` / β-carotene ketolase
- `cyaA` / adenylate cyclase
- CRP / cAMP receptor protein
- DXS and other MEP/MVA precursor-supply enzymes

**Grounding caution:** gene symbols are not globally unique identifiers. Use taxon-specific NCBI Gene, UniProt, or locus identifiers in YAML only after sequence/strain verification. For example, the directly tested *N. aromaticivorans* loci include Saro_1814 (`crtB`), Saro_1817 (`crtY`), Saro_0236 (`crtG`), and Saro_1168 (`crtZ`) (hall2023productionofcarotenoids pages 2-6).

### Chemicals and metabolites

- IPP; DMAPP; geranylgeranyl diphosphate (GGPP)
- Phytoene — colorless pathway intermediate
- Lycopene — red/pink-associated intermediate
- β-carotene — yellow carotenoid and provitamin A
- Zeaxanthin — yellow xanthophyll
- Caloxanthin and nostoxanthin — yellow xanthophyll products/intermediates
- Astaxanthin and adonixanthin — pathway comparators, generally not the core yellow endpoint
- cAMP; glucose; yeast extract; vanillate; oxygen
- Sorghum alkaline-pretreatment liquor and mixed lignocellulosic aromatics

Use verified ChEBI accessions during implementation; identifiers are intentionally not guessed here.

### Cellular localization and molecular roles

- Cell membrane / plasma membrane — `GO:0005886` where appropriate
- Intracellular lipophilic fraction — assay/localization label
- Pigment–protein complex and photosynthetic membrane — applicable only to photosynthetic taxa
- Antioxidant activity; reactive-oxygen-species scavenging; photoprotection

Carotenoids are commonly membrane-associated lipophilic compounds. However, generic membrane localization should not be copied to every taxon without direct or appropriately scoped evidence. The 2023 *N. aromaticivorans* study explicitly describes carotenoids as membrane-bound/intracellular products, whereas a 2024 review describes association with photosynthetic membranes specifically in photosynthetic organisms (hall2023productionofcarotenoids pages 2-6, huang2024bacterialpigmentsas pages 3-4).

### Taxa and contexts

- *Novosphingobium aromaticivorans* DSM 12444
- *Sphingobium* sp. KIB
- *Sphingomonas* sp. COS14-R2
- *Sphingopyxis* sp. USTB-05
- Engineered *Escherichia coli* XL1-Blue/JM109
- Yellow-carotenoid-producing *Flavobacterium* spp.

Add NCBITaxon CURIEs only after validating each strain’s accepted taxonomic record.

## 4. Candidate causal edges

The following compact scaffold distinguishes direct perturbations from pathway inference.

| confidence | subject | predicate | object | taxon/context | evidence type |
|---|---|---|---|---|---|
| high | CrtB (phytoene synthase) | catalyzes formation of | phytoene | carotenogenic bacteria; heterologous Sphingobium crt modules in *E. coli* | pathway reconstruction / heterologous expression (liu2021engineeringsphingobiumsp. pages 2-4) |
| high | crtB deletion | abolishes | yellow pigmentation | *Novosphingobium aromaticivorans* 12444ΔcrtB nonpigmented colonies | direct gene deletion (hall2023productionofcarotenoids pages 2-6) |
| high | CrtI (phytoene desaturase) | converts | phytoene to lycopene | Sphingobium carotenoid pathway; phytoene is colorless, lycopene red | mutational pathway inference / heterologous expression (liu2021engineeringsphingobiumsp. pages 4-5, liu2021engineeringsphingobiumsp. pages 2-4) |
| medium | CrtY (lycopene β-cyclase) | converts | lycopene to β-carotene | bacterial carotenoid pathway | pathway inference from mutant accumulation (hall2023productionofcarotenoids pages 2-6, raman2024nostoxanthinbiosynthesisby pages 1-2) |
| high | crtY deletion | causes accumulation of | lycopene and light-pink phenotype | *N. aromaticivorans* 12444ΔcrtY | direct gene deletion (hall2023productionofcarotenoids pages 2-6) |
| medium | CrtZ (β-carotene hydroxylase) | converts | β-carotene to zeaxanthin | sphingomonad carotenoid pathway | pathway inference / genomic annotation (liu2021engineeringsphingobiumsp. pages 4-5, raman2024nostoxanthinbiosynthesisby pages 1-2) |
| medium | CrtG (2,2′-β-ionone hydroxylase) | converts | zeaxanthin toward nostoxanthin | sphingomonad carotenoid pathway | pathway inference supported by mutant accumulation (liu2021engineeringsphingobiumsp. pages 4-5, hall2023productionofcarotenoids pages 2-6) |
| high | crtG deletion | causes accumulation of | zeaxanthin with yellow colonies | *N. aromaticivorans* 12444ΔcrtG | direct gene deletion (hall2023productionofcarotenoids pages 2-6) |
| high | crtG + crtZ deletion | causes accumulation of | β-carotene with yellow colonies | *N. aromaticivorans* 12444ΔcrtGZ | direct double deletion (hall2023productionofcarotenoids pages 2-6) |
| high | heterologous crtEBIYZ | causes | yellow phenotype | *E. coli* carrying Sphingobium crt module; zeaxanthin-producing | heterologous expression (liu2021engineeringsphingobiumsp. pages 2-4) |
| high | heterologous crtEBIYZG | causes | deep-yellow phenotype | *E. coli* carrying Sphingobium crt module; nostoxanthin-producing | heterologous expression (liu2021engineeringsphingobiumsp. pages 2-4) |
| high | cyaA deletion / reduced cyaA copy number | enhances | β-carotene production and intensified yellow pigmentation | engineered *E. coli* with crtEBIY pathway | targeted knockout / regulatory perturbation (kwon2024genomicinsightsinto pages 10-11, kwon2024genomicinsightsinto pages 1-3) |
| medium | MEP pathway | supplies precursors for | carotenoid biosynthesis | engineered *E. coli* β-carotene system | pathway description linked to perturbation study (kwon2024genomicinsightsinto pages 1-3) |
| low | MVA pathway | can supply precursors for | carotenoid biosynthesis | some bacteria including zeaxanthin-producing *Flavobacterium* spp. | review / comparative genomics, not direct perturbation for yellow trait (huang2024bacterialpigmentsas pages 3-4, zhuo2025comparativegenomicsand pages 1-2) |
| high | 35 °C, pH 7.5, glucose 40 g/L, yeast extract 5 g/L, dark incubation | increases | nostoxanthin production | *Sphingomonas* sp. COS14-R2 deep-yellow colonies | culture optimization / fermentation (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 4-5) |
| medium | yellow colony phenotype | indicates accumulation of | yellow carotenoids such as zeaxanthin, β-carotene, or nostoxanthin | assay-observed colony color across sphingomonads and engineered strains | phenotype-to-metabolite association; chemically validated in several cases (raman2024nostoxanthinbiosynthesisby pages 1-2, hall2023productionofcarotenoids pages 2-6, huang2024bacterialpigmentsas pages 8-9) |


*Table: This table summarizes compact candidate causal triples for microbial yellow pigmentation, prioritizing direct perturbation evidence and clearly separating pathway predictions from experimentally demonstrated effects. It is useful as a starting scaffold for TraitMech node-edge curation of METPO:1003030.*

### Evidence-rich triples for initial YAML curation

| Subject–predicate–object triple | Reference and supporting snippet | Curation assessment |
|---|---|---|
| `crtB deletion` — **causes loss of** → `pigmentation` | Hall et al. 2023: “Deletion of Saro_1814… resulted in… nonpigmented colonies”; only CoQ10 remained a major lipophilic compound. DOI: [10.1128/aem.01268-23](https://doi.org/10.1128/aem.01268-23) (hall2023productionofcarotenoids pages 2-6) | **High confidence; direct deletion.** Strong necessity edge for carotenoid-dependent pigmentation in this strain, but taxon-specific. |
| `CrtB` — **catalyzes production of** → `phytoene` | The same experiment states this was expected from CrtB’s role in phytoene synthesis; heterologous `crtEB` produced phytoene in *E. coli* (hall2023productionofcarotenoids pages 2-6, liu2021engineeringsphingobiumsp. pages 2-4). | **High confidence enzymatic step.** Phytoene itself is colorless, so do not connect it directly to yellow color with a positive edge. |
| `crtY deletion` — **causes accumulation of** → `lycopene` | `ΔcrtY` formed light-pink colonies and contained lycopene. DOI: [10.1128/aem.01268-23](https://doi.org/10.1128/aem.01268-23) (hall2023productionofcarotenoids pages 2-6) | **High confidence; direct deletion.** Useful contrast edge showing pathway diversion away from yellow products. |
| `CrtY activity` — **converts** → `lycopene to β-carotene` | In the MEP-fed pathway, GGPP is converted through CrtB and CrtI to lycopene, then CrtY to β-carotene; `crtY` loss accumulates lycopene (kwon2024genomicinsightsinto pages 1-3, hall2023productionofcarotenoids pages 2-6). | **Moderate-to-high confidence.** Biochemically established, but the retrieved direct experiment infers the reaction from substrate accumulation. |
| `crtG deletion` — **causes accumulation of** → `zeaxanthin` | `ΔcrtG` “formed yellow colonies” and zeaxanthin was a major lipophilic component. DOI: [10.1128/aem.01268-23](https://doi.org/10.1128/aem.01268-23) (hall2023productionofcarotenoids pages 2-6) | **High confidence.** One of the best phenotype-linked edges for `METPO:1003030`. |
| `zeaxanthin accumulation` — **causes/contributes to** → `yellow colony appearance` | The chemically characterized `ΔcrtG` strain accumulated zeaxanthin and formed yellow colonies; heterologous `crtEBIYZ` likewise produced a yellow phenotype (hall2023productionofcarotenoids pages 2-6, liu2021engineeringsphingobiumsp. pages 2-4). | **High confidence**, supported in two engineered systems. |
| `crtG + crtZ deletion` — **causes accumulation of** → `β-carotene` | The double mutant formed yellow colonies and its extract contained β-carotene as a major component. DOI: [10.1128/aem.01268-23](https://doi.org/10.1128/aem.01268-23) (hall2023productionofcarotenoids pages 2-6) | **High confidence; direct double deletion.** Do not attribute the outcome to either deletion alone without qualification. |
| `β-carotene accumulation` — **causes/contributes to** → `yellow colony appearance` | Chemically characterized `ΔcrtGΔcrtZ` colonies were yellow; engineered *E. coli* β-carotene was detected at 453 nm alongside yellow pigmentation (kwon2024genomicinsightsinto pages 10-11, hall2023productionofcarotenoids pages 2-6). | **High confidence.** Cross-system support. |
| `crtEBIYZ expression` — **causes** → `zeaxanthin production and yellow phenotype` | Recombinant *E. coli* carrying `pACCARcrtEBIYZ` displayed yellow pigmentation due to zeaxanthin synthesis. DOI: [10.3389/fbioe.2021.784559](https://doi.org/10.3389/fbioe.2021.784559) (liu2021engineeringsphingobiumsp. pages 2-4) | **High confidence; sufficiency via heterologous expression.** Use an engineered-organism context qualifier. |
| `crtEBIYZG expression` — **causes** → `nostoxanthin production and deep-yellow phenotype` | Recombinant *E. coli* carrying `pACCARcrtEBIYZG` displayed a deep-yellow phenotype due to nostoxanthin synthesis (liu2021engineeringsphingobiumsp. pages 2-4). | **High confidence; sufficiency edge**, but specific to the tested gene set and host. |
| `cyaA deletion` — **increases** → `β-carotene production` | Kwon et al. 2024 used a targeted knockout to validate that reduced `cyaA` copy number enhanced β-carotene biosynthesis; the proposed mechanism is reduced cAMP and relief of cAMP–CRP catabolite repression. DOI: [10.3390/ijms252312796](https://doi.org/10.3390/ijms252312796) (kwon2024genomicinsightsinto pages 10-11, kwon2024genomicinsightsinto pages 1-3) | **High confidence for engineered *E. coli*.** The cAMP–CRP explanation is mechanistic interpretation; do not generalize across naturally yellow taxa. |
| `reduced cAMP–CRP signaling` — **relieves repression of** → `carotenoid metabolic flux` | Targeted `cyaA` deletion enhanced β-carotene, consistent with lower cAMP alleviating catabolite repression and redirecting flux (kwon2024genomicinsightsinto pages 1-3). | **Moderate confidence.** Curate as a regulatory model with “inferred mechanism” qualifier unless direct promoter/flux evidence is required. |
| `35°C + pH 7.5 + 40 g/L glucose + 5 g/L yeast extract + darkness` — **maximizes under tested conditions** → `nostoxanthin production` | Raman et al. 2024 found these optimal tested conditions for deep-yellow *Sphingomonas* COS14-R2; efficiency reached 92% at 35°C. DOI: [10.1007/s00284-024-03956-7](https://doi.org/10.1007/s00284-024-03956-7) (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 4-5) | **Moderate-to-high, assay-specific.** Encode individual environmental edges only if factorial evidence supports them; otherwise preserve the condition bundle. |
| `vanillate or sorghum alkaline-pretreatment liquor` — **supports production of** → `cell-associated carotenoids` | Engineered *N. aromaticivorans* produced carotenoids from vanillate and from mixed aromatics in sorghum pretreatment liquor. DOI: [10.1128/aem.01268-23](https://doi.org/10.1128/aem.01268-23) (hall2023productionofcarotenoids pages 1-2, hall2023productionofcarotenoids pages 6-8) | **High confidence for substrate support**, not necessarily induction of yellow pigmentation. |
| `5–21% O₂` — **has no consistent significant effect on** → `carotenoid abundance` | Across the tested range, oxygen availability did not consistently affect carotenoid levels; only the β-carotene strain differed significantly across concentrations (hall2023productionofcarotenoids pages 6-8). | **Context-specific negative result.** Do not curate a universal “oxygen has no effect” edge. |

## 5. Recent developments, applications, and quantitative evidence

### 2023–2024 mechanistic and engineering advances

- **Defined pathway deletions in a lignin-aromatic-utilizing chassis (2023):** *N. aromaticivorans* mutants accumulated zeaxanthin at 0.25–0.54 µg/mg dry cell weight and β-carotene at 0.29–0.64 µg/mg under tested oxygen conditions. These strains also produced carotenoids from sorghum alkaline-pretreatment liquor, demonstrating a real biorefinery application rather than only growth on refined glucose (hall2023productionofcarotenoids pages 6-8).
- **Global-regulator engineering (2024):** targeted `cyaA` knockout in engineered *E. coli* increased β-carotene production and intensified yellow pigmentation, connecting central carbon regulation to the trait through the cAMP–CRP system (kwon2024genomicinsightsinto pages 10-11, kwon2024genomicinsightsinto pages 1-3).
- **Nostoxanthin fermentation (2024):** deep-yellow *Sphingomonas* COS14-R2 reached **217.22 ± 9.60 mg/L**, 72.32% selectivity, and reported productivity of 2.59 g/L/h under fed-batch conditions. Purified pigment gave m/z 600.5098 and **75.5 ± 0.33% DPPH radical scavenging** (raman2024nostoxanthinbiosynthesisby pages 1-2). The productivity unit/value should be checked against the original tables before database curation because it appears unusually large relative to the titer.
- **Metabolomics (2024):** yellow *Sphingopyxis* USTB-05 contained seven carotenes and six xanthophylls; zeaxanthin was most abundant at **37.1 µg/g dry cells**. The authors explicitly stated that proposed pathway details still require isotope labeling, knockout, and enzyme assays, making this discovery evidence rather than a causal graph backbone (liu2024metabolomicanalysisof pages 11-13).

### Current applications

Current uses are mainly pigment and carotenoid **biomanufacturing**, including food colorants, nutritional supplements, feed, cosmetics, and pharmaceutical ingredients. β-Carotene is used as a colorant in dairy products, canned fruit, jams, confectionery, and beverages and as a nutritional supplement. Yellow zeaxanthin from *Flavobacterium* has been used in poultry-feed contexts, while antioxidant carotenoids are incorporated into UV/anti-aging cosmetic formulations (huang2024bacterialpigmentsas pages 8-9).

Renewable-feedstock implementations are particularly relevant. *Sphingobium* sp. was engineered to accumulate carotenoids using glycerol, okara, and corn-steep liquor, reaching approximately **5.4 mg/g dry-cell weight**; these substrates are underused by-products of biodiesel, soymilk, and starch manufacture (liu2021engineeringsphingobiumsp. pages 4-5, liu2021engineeringsphingobiumsp. pages 2-4). *N. aromaticivorans* offers a complementary route using lignocellulosic aromatics and can co-produce intracellular carotenoids with extracellular 2-pyrone-4,6-dicarboxylic acid, potentially improving product separation and biorefinery economics (hall2023productionofcarotenoids pages 1-2, hall2023productionofcarotenoids pages 2-6).

The 2024 review’s expert assessment is that bacterial production offers robustness and potential quality/cost advantages over plant extraction, but commercialization remains constrained by **low yields, unstable quality, and high production costs**. Recommended solutions include high-yield strain screening, optimization of nutrients, pH, temperature, and oxygen, and genetic engineering (huang2024bacterialpigmentsas pages 8-9).

## 6. Suggested minimal TraitMech backbone

For a conservative first revision of `yellow_pigmented.yaml`, prioritize this experimentally anchored branch:

`MEP/MVA precursor supply` → `IPP + DMAPP` → `GGPP` —CrtB→ `phytoene` —CrtI→ `lycopene` —CrtY→ `β-carotene` —CrtZ→ `zeaxanthin` —CrtG→ `caloxanthin/nostoxanthin` → `cell-associated yellow carotenoid accumulation` → `METPO:1003030`.

Add perturbation branches:

- `crtB loss` → absence of carotenoid accumulation → nonpigmented colony;
- `crtG loss` → zeaxanthin accumulation → yellow colony;
- `crtG + crtZ loss` → β-carotene accumulation → yellow colony;
- `crtEBIYZ` expression → zeaxanthin accumulation → yellow colony;
- `crtEBIYZG` expression → nostoxanthin accumulation → deep-yellow colony;
- `cyaA loss` → reduced cAMP signaling → increased β-carotene flux → intensified yellow pigmentation, explicitly restricted to engineered *E. coli*.

This backbone is preferable to a single “carotenoid causes yellow” edge because it captures both pathway sufficiency and color-changing blocks.

## 7. Warnings: claims not ready for curation

1. **Do not equate yellow color with carotenoid identity.** β-Carotene and zeaxanthin can both yield yellow colonies, and spectral overlap makes visual identification non-specific (hall2023productionofcarotenoids pages 2-6).
2. **Do not curate genomic presence as causality.** The `crtB/crtI/crtY` cluster in COS14-R2 is genomic support, not knockout validation. Likewise, several *Sphingopyxis* conversions remain predictions requiring isotope tracing or enzyme assays (raman2024nostoxanthinbiosynthesisby pages 1-2, liu2024metabolomicanalysisof pages 11-13).
3. **Do not generalize `cyaA` regulation.** Its evidence comes from an engineered *E. coli* β-carotene system, not diverse naturally yellow bacteria (kwon2024genomicinsightsinto pages 1-3).
4. **Do not assert universal environmental effects.** The COS14-R2 optimum is strain- and medium-specific; oxygen had little consistent effect in *N. aromaticivorans* over only 5–21% O₂ (raman2024nostoxanthinbiosynthesisby pages 1-2, hall2023productionofcarotenoids pages 6-8).
5. **Do not use antioxidant or photoprotective function as the cause of color.** These are downstream biological roles of pigments. A 2024 review supports microbial stress protection broadly, but not every yellow isolate has demonstrated protection (huang2024bacterialpigmentsas pages 3-4).
6. **Do not merge chemically distinct yellow pathways.** Xanthomonadin, flexirubin, aryl-polyene, and carotenoid branches need independent evidence and nodes.
7. **Avoid unverified ontology CURIEs.** Gene/protein and chemical identifiers should be resolved against the exact taxon, sequence, and chemical entity before YAML insertion.
8. **Check suspicious quantitative reporting.** In particular, reconcile the reported COS14-R2 productivity of 2.59 g/L/h with its 217.22 mg/L titer before curating that statistic (raman2024nostoxanthinbiosynthesisby pages 1-2).
9. **The supplied 2025 review is contextual evidence only.** DOI [10.1080/1040841X.2025.2526423](https://doi.org/10.1080/1040841X.2025.2526423) supports the broad association between bacterial yellow/red/orange/pink pigmentation and carotenoids, but primary perturbation studies above should support graph edges.

## 8. DOI-first bibliography

1. **Kwon S-J, Park CB, Lee PC.** “Genomic Insights into the Role of cAMP in Carotenoid Biosynthesis: Enhancing β-Carotene Production in *Escherichia coli* via `cyaA` Deletion.” *International Journal of Molecular Sciences* 25:12796. **November 2024.** [https://doi.org/10.3390/ijms252312796](https://doi.org/10.3390/ijms252312796) (kwon2024genomicinsightsinto pages 10-11, kwon2024genomicinsightsinto pages 1-3)
2. **Raman J, Kim J-S, Ko Y-J, Kim S-J.** “Nostoxanthin Biosynthesis by *Sphingomonas* Species (COS14-R2): Isolation, Identification, and Optimization of Culture Conditions.” *Current Microbiology* 81. **November 2024.** [https://doi.org/10.1007/s00284-024-03956-7](https://doi.org/10.1007/s00284-024-03956-7) (raman2024nostoxanthinbiosynthesisby pages 1-2, raman2024nostoxanthinbiosynthesisby pages 4-5)
3. **Liu C et al.** “Metabolomic Analysis of Carotenoids Biosynthesis by *Sphingopyxis* sp. USTB-05.” *Molecules* 29:4235. **September 2024.** [https://doi.org/10.3390/molecules29174235](https://doi.org/10.3390/molecules29174235) (liu2024metabolomicanalysisof pages 11-13)
4. **Huang X et al.** “Bacterial Pigments as a Promising Alternative to Synthetic Colorants: From Fundamentals to Applications.” *Journal of Microbiology and Biotechnology* 34:2153–2165. **September/November 2024 issue.** [https://doi.org/10.4014/jmb.2404.04018](https://doi.org/10.4014/jmb.2404.04018) (huang2024bacterialpigmentsas pages 8-9, huang2024bacterialpigmentsas pages 3-4)
5. **Hall BW et al.** “Production of Carotenoids from Aromatics and Pretreated Lignocellulosic Biomass by *Novosphingobium aromaticivorans*.” *Applied and Environmental Microbiology* 89(12). **December 2023.** [https://doi.org/10.1128/aem.01268-23](https://doi.org/10.1128/aem.01268-23) (hall2023productionofcarotenoids pages 1-2, hall2023productionofcarotenoids pages 2-6, hall2023productionofcarotenoids pages 6-8)
6. **Liu M et al.** “Engineering *Sphingobium* sp. to Accumulate Various Carotenoids Using Agro-Industrial Byproducts.” *Frontiers in Bioengineering and Biotechnology* 9:784559. **November 2021.** [https://doi.org/10.3389/fbioe.2021.784559](https://doi.org/10.3389/fbioe.2021.784559) (liu2021engineeringsphingobiumsp. pages 4-5, liu2021engineeringsphingobiumsp. pages 2-4)
7. **Henke N et al.** “Production of the Marine Carotenoid Astaxanthin by Metabolically Engineered *Corynebacterium glutamicum*.” *Marine Drugs* 14:124. **June 2016.** [https://doi.org/10.3390/md14070124](https://doi.org/10.3390/md14070124) (henke2016productionofthe pages 15-17)
8. **Existing supplied evidence:** “Red, pink, orange, and yellow pigmentation in bacteria.” **2025.** [https://doi.org/10.1080/1040841X.2025.2526423](https://doi.org/10.1080/1040841X.2025.2526423).

References

1. (huang2024bacterialpigmentsas pages 3-4): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 40 citations and is from a peer-reviewed journal.

2. (hall2023productionofcarotenoids pages 2-6): Benjamin W. Hall, Wayne S. Kontur, Jeanette C. Neri, Derek M. Gille, Daniel R. Noguera, and Timothy J. Donohue. Production of carotenoids from aromatics and pretreated lignocellulosic biomass by <i>novosphingobium aromaticivorans</i>. Applied and Environmental Microbiology, Dec 2023. URL: https://doi.org/10.1128/aem.01268-23, doi:10.1128/aem.01268-23. This article has 19 citations and is from a peer-reviewed journal.

3. (liu2021engineeringsphingobiumsp. pages 2-4): Mengmeng Liu, Yang Yang, Li Li, Yan Ma, Junchao Huang, and Jingrun Ye. Engineering sphingobium sp. to accumulate various carotenoids using agro-industrial byproducts. Frontiers in Bioengineering and Biotechnology, Nov 2021. URL: https://doi.org/10.3389/fbioe.2021.784559, doi:10.3389/fbioe.2021.784559. This article has 6 citations.

4. (liu2021engineeringsphingobiumsp. pages 4-5): Mengmeng Liu, Yang Yang, Li Li, Yan Ma, Junchao Huang, and Jingrun Ye. Engineering sphingobium sp. to accumulate various carotenoids using agro-industrial byproducts. Frontiers in Bioengineering and Biotechnology, Nov 2021. URL: https://doi.org/10.3389/fbioe.2021.784559, doi:10.3389/fbioe.2021.784559. This article has 6 citations.

5. (raman2024nostoxanthinbiosynthesisby pages 1-2): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 6 citations and is from a peer-reviewed journal.

6. (kwon2024genomicinsightsinto pages 10-11): Soon-Jae Kwon, Chan Bae Park, and Pyung Cheon Lee. Genomic insights into the role of camp in carotenoid biosynthesis: enhancing β-carotene production in escherichia coli via cyaa deletion. International Journal of Molecular Sciences, 25:12796, Nov 2024. URL: https://doi.org/10.3390/ijms252312796, doi:10.3390/ijms252312796. This article has 4 citations.

7. (kwon2024genomicinsightsinto pages 1-3): Soon-Jae Kwon, Chan Bae Park, and Pyung Cheon Lee. Genomic insights into the role of camp in carotenoid biosynthesis: enhancing β-carotene production in escherichia coli via cyaa deletion. International Journal of Molecular Sciences, 25:12796, Nov 2024. URL: https://doi.org/10.3390/ijms252312796, doi:10.3390/ijms252312796. This article has 4 citations.

8. (zhuo2025comparativegenomicsand pages 1-2): Ye Zhuo, Chun-Zhi Jin, Chang-Soo Lee, Kee-Sun Shin, and Hyung-Gwan Lee. Comparative genomics and evolutionary insights into zeaxanthin biosynthesis in two novel flavobacterium species. BMC Microbiology, Apr 2025. URL: https://doi.org/10.1186/s12866-025-03954-0, doi:10.1186/s12866-025-03954-0. This article has 4 citations and is from a peer-reviewed journal.

9. (raman2024nostoxanthinbiosynthesisby pages 4-5): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 6 citations and is from a peer-reviewed journal.

10. (huang2024bacterialpigmentsas pages 8-9): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 40 citations and is from a peer-reviewed journal.

11. (hall2023productionofcarotenoids pages 1-2): Benjamin W. Hall, Wayne S. Kontur, Jeanette C. Neri, Derek M. Gille, Daniel R. Noguera, and Timothy J. Donohue. Production of carotenoids from aromatics and pretreated lignocellulosic biomass by <i>novosphingobium aromaticivorans</i>. Applied and Environmental Microbiology, Dec 2023. URL: https://doi.org/10.1128/aem.01268-23, doi:10.1128/aem.01268-23. This article has 19 citations and is from a peer-reviewed journal.

12. (hall2023productionofcarotenoids pages 6-8): Benjamin W. Hall, Wayne S. Kontur, Jeanette C. Neri, Derek M. Gille, Daniel R. Noguera, and Timothy J. Donohue. Production of carotenoids from aromatics and pretreated lignocellulosic biomass by <i>novosphingobium aromaticivorans</i>. Applied and Environmental Microbiology, Dec 2023. URL: https://doi.org/10.1128/aem.01268-23, doi:10.1128/aem.01268-23. This article has 19 citations and is from a peer-reviewed journal.

13. (liu2024metabolomicanalysisof pages 11-13): Chaowang Liu, Qianqian Xu, Yang Liu, Meijie Song, Xiaoyu Cao, Xinyue Du, and Hai Yan. Metabolomic analysis of carotenoids biosynthesis by sphingopyxis sp. ustb-05. Molecules, 29:4235, Sep 2024. URL: https://doi.org/10.3390/molecules29174235, doi:10.3390/molecules29174235. This article has 3 citations.

14. (henke2016productionofthe pages 15-17): Nadja Henke, Sabine Heider, Petra Peters-Wendisch, and Volker Wendisch. Production of the marine carotenoid astaxanthin by metabolically engineered corynebacterium glutamicum. Marine Drugs, 14:124, Jun 2016. URL: https://doi.org/10.3390/md14070124, doi:10.3390/md14070124. This article has 141 citations.