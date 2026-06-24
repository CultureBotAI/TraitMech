---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:06:43.208049'
end_time: '2026-06-17T22:33:28.480320'
duration_seconds: 1605.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: growth range phenotype with numerical limits
  trait_identifier: METPO:1000535
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: growth_range_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the span of values within which an organism
    can maintain growth.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports the bounded span of a growth-supporting environmental variable as a standard
    quantitative descriptor.) | DOI:10.1038/nrmicro2549: external pH (pH-homeostasis
    review supports the external-pH range over which cytoplasmic pH homeostasis sustains
    growth as an analogous range descriptor on the pH axis.)'
  causal_graph_summary: 'growth_range_phenotype_descriptor: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** growth range phenotype with numerical limits
- **METPO identifier:** METPO:1000535
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the span of values within which an organism can maintain growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the bounded span of a growth-supporting environmental variable as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports the external-pH range over which cytoplasmic pH homeostasis sustains growth as an analogous range descriptor on the pH axis.)
- **Existing causal graph summary:** growth_range_phenotype_descriptor: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **growth range phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** growth range phenotype with numerical limits
- **METPO identifier:** METPO:1000535
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the span of values within which an organism can maintain growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the bounded span of a growth-supporting environmental variable as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: external pH (pH-homeostasis review supports the external-pH range over which cytoplasmic pH homeostasis sustains growth as an analogous range descriptor on the pH axis.)
- **Existing causal graph summary:** growth_range_phenotype_descriptor: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **growth range phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Growth range phenotype with numerical limits (METPO:1000535)

### 1) Scope summary (trait definition, boundaries, and near-neighbor traits)

**Trait meaning.** *Growth range phenotype with numerical limits* denotes the **bounded interval (minimum–maximum) of an environmental variable** within which an organism can maintain growth (positive growth rate / net population increase) and is typically reported with numeric endpoints (e.g., Tmin–Tmax, pHmin–pHmax, salinitymin–salinitymax), sometimes also including an **optimum** within the interval. This aligns with quantitative phenotyping practice where growth is modeled as a curve and growth rate (µ) is estimated as a continuous parameter rather than a categorical label (gonzalez2023microbialgrowthunder pages 3-5).

**What counts as “growth.”** In batch culture, microbial growth is commonly conceptualized as a sigmoidal curve (lag → exponential → stationary → decline), with **maximum growth rate (µmax)** near the inflection point and growth rates spanning “from zero growth to the maximum achievable” within the same culture (gonzalez2023microbialgrowthunder pages 3-5). Growth-rate regimes can be operationalized (e.g., slow growth ≥0.025 h−1 and near-zero growth <0.025 h−1 in one reviewed framework), highlighting that *growth range* can include very slow-growth states depending on assay design (gonzalez2023microbialgrowthunder pages 3-5).

**Boundary cases / distinctions.**
- **Optimum-only traits (e.g., optimal pH, optimal temperature)** are *single-point* descriptors; **growth range** explicitly requires **numeric bounds** (min and max) along an axis.
- **Survival-only tolerance** (viability without replication) is not the same as growth; growth range should be grounded in evidence of replication or sustained positive growth, not merely persistence.
- **Assay dependence** is central: medium composition, buffering, inoculum history/acclimation, and measurement approach can shift apparent bounds; this is emphasized in discussions of growth-rate estimation and experimental constraints (gonzalez2023microbialgrowthunder pages 3-5, gonzalez2023microbialgrowthundera pages 5-7).

### 2) Key concepts and definitions (current understanding)

#### 2.1 Cardinal points and performance curves
A widely used conceptual framework is the **performance curve** with **minimum**, **optimum**, and **maximum** points (Tmin/Topt/Tmax for temperature; analogous min/opt/max for pH, salinity, etc.). For temperature in particular, community or organismal growth can be described with a temperature performance curve that increases to an optimum (Topt) and can be parameterized below Topt using the **Ratkowsky square-root model**, yielding an “apparent” Tmin (x-intercept) (baath2024temperatureadaptationof pages 1-2, baath2024temperatureadaptationof pages 2-4). The existence of these “cardinal” parameters is also reflected in recent computational phenotype prediction efforts that explicitly model Topt/Tmin/Tmax as numeric targets (barnum2024predictingmicrobialgrowth pages 22-24).

#### 2.2 Mechanistic interpretation of “limits”
Across environmental axes, a **growth boundary** can be interpreted as the point where **homeostasis fails** (e.g., internal pH, ionic strength, turgor/volume, membrane function, macromolecular crowding) and essential processes can no longer operate. A current synthesis emphasizes that bacteria maintain multiple physicochemical variables “within limits,” notably cytoplasmic pH, ionic strength, and turgor/volume, and these constraints directly define feasible growth conditions (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4).

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 (2024) Mechanistic, quantitative salinity-growth range with omics: *Natranaerobius thermophilus*
A 2024 Applied and Environmental Microbiology study provides an unusually curation-friendly package: **explicit numeric growth salinity bounds and optimum** plus **measured mechanistic intermediates**.
- Reported growth across **~3.1–4.9 M Na+** with **optimum ~3.3–3.9 M Na+** (and polyextreme context including alkaline pH and elevated temperature) (xing2024thepolyextremophilenatranaerobius pages 1-2).
- Evidence supports a **hybrid osmoadaptation strategy** combining **compatible solute accumulation** and a **salt-in (K+) component**, with explicit transport systems (Opu/ProU families; SSS symporters) and ion homeostasis machinery (Na+/K+/H+ transporters; Na+(K+)/H+ antiporters; Na+-translocating FOF1-ATPase) (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 6-7).
- Intracellular compatible solutes were quantified and increased with salinity, notably glycine betaine rising dramatically (e.g., 52.7 mM at 2.5 M Na+ to 893.1 mM at 4.3 M Na+) (xing2024thepolyextremophilenatranaerobius pages 17-19).

Figures visually summarizing growth curves and intracellular solute/K+ levels across salinity are available from this study (xing2024thepolyextremophilenatranaerobius media eec50655, xing2024thepolyextremophilenatranaerobius media 7eed915d).

#### 3.2 (2023–2024) pH range as a homeostasis problem (review synthesis)
A 2023 FEMS Microbiology Reviews synthesis frames growth across external pH as dependent on maintaining **near-neutral cytoplasmic pH** (often ~7.0–7.5) despite very small absolute proton numbers, requiring buffering and active transport/energy coupling (poolman2023physicochemicalhomeostasisin pages 1-2). Mechanisms include:
- **Ion/H+ antiporters** that “acidify the cytoplasm” by exporting K+ or Na+ in exchange for protons when internal pH becomes too high (poolman2023physicochemicalhomeostasisin pages 1-2).
- **F0F1-ATPase and proton-pumping respiratory chains** as mechanisms to counter cytoplasmic acidification (poolman2023physicochemicalhomeostasisin pages 1-2).
- **Amino-acid decarboxylase/antiporter systems** that generate PMF and respond intrinsically to low internal pH (activity increases as internal pH drops), contributing to pH homeostasis and acid stress response (poolman2023physicochemicalhomeostasisin pages 2-4).

This review explicitly notes neutralophiles can keep PMF relatively constant “across an external pH range of about 5–8,” connecting homeostasis to a plausible growth-supporting external pH interval (poolman2023physicochemicalhomeostasisin pages 1-2).

#### 3.3 (2024) Temperature adaptation tracked via shifts in Tmin/SI at the community level
A 2024 Microbial Ecology study uses cardinal-temperature concepts to quantify **how growth temperature adaptation changes over time**, estimating Tmin with Ratkowsky modeling and using a temperature sensitivity index (SI) (baath2024temperatureadaptationof pages 1-2, baath2024temperatureadaptationof pages 2-4). It reports that apparent Tmin in aquatic systems has been suggested to range globally from about −17 to 0 °C and shows rapid adaptation of a winter community to warming within ~2 weeks, while cooling adaptation is slower (baath2024temperatureadaptationof pages 1-2).

#### 3.4 (2024) Genome-based prediction of numeric growth-condition ranges (cultivation guidance)
Barnum et al. (2024, bioRxiv) introduce **GenomeSPOT**, predicting multiple numeric growth-condition traits from amino-acid composition and other sequence-derived features, using a large curation from BacDive:
- Training dataset: **15,596 bacteria/archaea**; achieved **92% balanced accuracy** for oxygen tolerance; regression performance **R2=0.73 (temperature optimum), R2=0.81 (salinity), R2=0.48 (pH)** (barnum2024predictingmicrobialgrowth pages 1-3).
- Trait-label ranges compiled include **temperature 4–105 °C**, **salinity 0.0–27.5% w/v NaCl**, and **pH 1.1–12.0** (barnum2024predictingmicrobialgrowth pages 22-24).
- The authors applied predictions to **85,205 sequenced species** and **3,349 metagenomic samples**, reporting that uncultivated taxa are enriched for thermophiles/anaerobes/acidophiles and giving quantitative enrichment examples (e.g., anaerobes 54% of uncultivated vs 16% of cultivated) (barnum2024predictingmicrobialgrowth pages 11-14).

### 4) Current applications and real-world implementations

1. **Cultivation and bioprospecting / strain screening.** Genome-based inference of growth requirements (temperature/pH/salinity/oxygen) is positioned explicitly as a tool to guide selection of viable culturing conditions for uncultivated taxa, with the potential to reduce trial-and-error experimentation (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 11-14).

2. **Environmental microbiology and climate-change response.** Temperature adaptation metrics based on Tmin and growth assays provide a mechanistic path to predict how community functioning changes under warming vs cooling regimes (baath2024temperatureadaptationof pages 1-2, baath2024temperatureadaptationof pages 2-4).

3. **Agriculture and salinity management using PGPR.** Salt-tolerant plant-associated bacteria with measurable salinity tolerance limits are proposed as practical interventions. For example, Priestia megaterium ZS-3 is reported to tolerate salinity up to **9%**, with distinct osmoadaptation metabolite strategies at lower vs higher NaCl (glutamate/trehalose vs proline/K+/EPS) (shi2023mechanismofsalt pages 1-2).

4. **Food safety / pathogen risk across salinity regimes.** Vibrio parahaemolyticus shows survival across NaCl concentrations except 9% NaCl in M9 and displays transcriptome changes including compatible-solute systems at low salinity (0.5% vs 3% NaCl), linking salinity environments to growth/fitness and virulence-related regulation (zhang2023transcriptomeanalysisreveals pages 1-2).

### 5) Candidate causal-graph nodes (grouped) with ontology grounding suggestions

> Note: Groundings are *suggestions* limited to high-confidence, stable ontologies; label-only nodes are used when a specific CURIE cannot be asserted from the extracted snippets without risk of invention.

#### 5.1 Trait node
- **Growth range phenotype with numerical limits** — METPO:1000535 (given)

#### 5.2 Environmental / exposure nodes (ENVO suggested)
- external pH (environmental hydrogen ion concentration) — ENVO: label-only suggestion “pH”
- salinity / NaCl / osmolarity / hypertonicity — ENVO: label-only suggestion “saline water”, “hypersaline environment”
- temperature — ENVO: label-only suggestion “temperature”

#### 5.3 Phenotype/assay nodes (GO / assay concepts)
- growth rate (µ), µmax; growth curve phases (lag/exponential/stationary/decline) — label-only; modeled via Gompertz/logistic fits (gonzalez2023microbialgrowthunder pages 3-5)
- chemostat dilution-rate set growth; retentostat near-zero growth — label-only (gonzalez2023microbialgrowthundera pages 5-7)

#### 5.4 Cellular processes (GO suggested)
- **pH homeostasis** — GO: label-only suggestion “pH homeostasis” (poolman2023physicochemicalhomeostasisin pages 1-2)
- **osmotic stress response / osmoadaptation** — GO: label-only suggestion “response to osmotic stress” (poolman2023physicochemicalhomeostasisin pages 2-4, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **maintenance of PMF** — GO: label-only suggestion “proton motive force-driven transport/ATP synthesis” (poolman2023physicochemicalhomeostasisin pages 2-4)
- **ion homeostasis / turgor regulation** — GO: label-only suggestions (poolman2023physicochemicalhomeostasisin pages 2-4)

#### 5.5 Molecular functions / complexes (GO suggested; label-only where needed)
- **F0F1 ATP synthase / F0F1-ATPase** — GO/complex: label-only (poolman2023physicochemicalhomeostasisin pages 1-2)
- **Na+/H+ antiporter**, **K+/H+ antiporter** — GO: label-only (poolman2023physicochemicalhomeostasisin pages 1-2)
- amino-acid decarboxylases and coupled antiporters — GO/EC: label-only (poolman2023physicochemicalhomeostasisin pages 2-4)
- ABC-type compatible solute transporters (Opu/ProU families) — label-only (xing2024thepolyextremophilenatranaerobius pages 1-2)
- SSS (Na+/solute symporter) family — label-only (xing2024thepolyextremophilenatranaerobius pages 1-2)

#### 5.6 Chemicals / metabolites (CHEBI suggested)
- glycine betaine — CHEBI: label-only suggestion (xing2024thepolyextremophilenatranaerobius pages 17-19)
- L-glutamate — CHEBI: label-only suggestion (xing2024thepolyextremophilenatranaerobius pages 17-19)
- L-proline — CHEBI: label-only suggestion (xing2024thepolyextremophilenatranaerobius pages 17-19)
- trehalose — CHEBI: label-only suggestion (shi2023mechanismofsalt pages 1-2)
- potassium ion (K+) — CHEBI: label-only suggestion (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 17-19)
- sodium ion (Na+) — CHEBI: label-only suggestion (xing2024thepolyextremophilenatranaerobius pages 1-2)

#### 5.7 Example taxa (NCBITaxon)
- *Natranaerobius thermophilus* — NCBITaxon: label-only suggestion (xing2024thepolyextremophilenatranaerobius pages 1-2)
- *Priestia megaterium* — NCBITaxon: label-only suggestion (shi2023mechanismofsalt pages 1-2)
- *Vibrio parahaemolyticus* — NCBITaxon: label-only suggestion (zhang2023transcriptomeanalysisreveals pages 1-2)

### 6) Candidate causal edges (curation table)

The following table is intended for direct transfer into a TraitMech-style YAML graph as candidate edges with provenance.

| Edge (S–P–O) | Node type(s) | Evidence snippet (short quote) | Reference (DOI + URL + year) | Notes/uncertainty |
|---|---|---|---|---|
| external pH range → requires maintenance of near-neutral cytoplasmic pH → microbial growth across pH range | environmental factor → biological process → phenotype | “neutralophilic bacteria to keep PMF relatively constant across an external pH range of about 5–8” and cytoplasmic pH is kept “within the range of 7.0 to 7.5” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033, 2023 | **General.** Strong review-level support that pH homeostasis underlies pH growth boundaries, but not a species-specific edge. |
| K+/H+ or Na+/H+ antiporter activity → acidifies cytoplasm → supports growth at alkaline external pH | transporter/molecular function → physiological state → phenotype | “ion/H+ antiporters acidify the cytoplasm by exporting K+ or Na+ in exchange for protons when the internal pH gets too high” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033, 2023 | **General.** Mechanistic edge for pH-axis boundary control; likely relevant mainly near upper external pH limit. |
| F0F1-ATPase / proton-pumping respiratory chain activity → prevents cytoplasmic acidification → supports growth across external pH range | protein complex/process → physiological state → phenotype | “Activation/upregulation of proton-pumping respiratory chains, the F0F1-ATPase… prevents cytoplasmic acidification” (poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033, 2023 | **General.** Review evidence; curate as broad mechanism, not as taxon-specific gene edge without narrower source. |
| amino-acid decarboxylase/antiporter systems → generate PMF and raise internal pH → enable growth under acidic external pH | enzyme + transporter system → process → phenotype | “Each decarboxylation effectively 'pumps' one proton equivalent” and decarboxylases “increase activity when internal pH falls” (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033, 2023 | **General.** Strong mechanistic support for acid-side boundary extension. |
| glutamate/arginine decarboxylase acid-resistance systems → increase internal pH / reverse membrane potential → acid tolerance and likely lower pH growth boundary extension | pathway/system → physiological state → phenotype | “increase internal pH and reverse transmembrane potential” (li2024responseofescherichia pages 10-12) | Li et al. 2024, doi:10.3390/microorganisms12091774, https://doi.org/10.3390/microorganisms12091774, 2024 | **Taxon-focused/uncertain for curation.** Evidence is mainly for *E. coli* acid resistance; direct growth-range limit effect is inferred rather than measured. |
| hypertonic salinity increase → cell shrinkage and lower turgor → growth ceases at salinity limit | environmental factor → physiological state → phenotype | “Hypertonicity leads to cell shrinkage and a lowering of the turgor” and “the lower limit of turgor should be before cell growth ceases” (poolman2023physicochemicalhomeostasisin pages 2-4, poolman2023physicochemicalhomeostasisin pages 1-2) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033, 2023 | **General.** Good high-level edge linking osmotic stress to salinity growth boundary. |
| OpuA-mediated glycine betaine uptake → accumulation of compatible solute → counteracts hyperosmotic stress and supports salinity range growth | transporter → chemical/process → phenotype | OpuA “accumulat[es] the compatible solute glycine betaine to (sub)molar levels” (poolman2023physicochemicalhomeostasisin pages 2-4) | Poolman 2023, doi:10.1093/femsre/fuad033, https://doi.org/10.1093/femsre/fuad033, 2023 | **General.** Broad osmoadaptation mechanism; transporter family-level grounding is possible. |
| high salinity → increased intracellular glycine betaine / glutamate / proline → adaptation to high-salinity growth conditions | environmental factor → metabolite accumulation → phenotype | “intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24, https://doi.org/10.1128/aem.00145-24, 2024 | **Taxon-specific (*Natranaerobius thermophilus*).** Strong direct support across tested Na+ conditions. |
| glycine betaine ABC transporters (Opu/ProU) and Na+/solute symporters → compatible-solute uptake → growth in 3.1–4.9 M Na+ range | transporter families → process → phenotype | “employs the glycine betaine ABC transporters (Opu and ProU families), Na+/solute symporters… to adapt to high salinity” and grows in “3.1–4.9 M Na+” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24, https://doi.org/10.1128/aem.00145-24, 2024 | **Taxon-specific.** Strong candidate causal edge with explicit numeric salinity limits. |
| Na+/K+/H+ transporters and Na+(K+)/H+ antiporters → maintain intracellular K+ / ion homeostasis → support high-salinity growth | transporter families → physiological state → phenotype | “upregulation of Na+/K+/H+ transporters facilitates the maintenance of intracellular K+ concentration” (xing2024thepolyextremophilenatranaerobius pages 1-2) and NhaC is “strongly upregulated” (xing2024thepolyextremophilenatranaerobius pages 6-7) | Xing et al. 2024, doi:10.1128/aem.00145-24, https://doi.org/10.1128/aem.00145-24, 2024 | **Taxon-specific.** Strong mechanistic support for upper salinity boundary. |
| high salinity → cytoplasmic acidification → part of adaptation to salinity growth conditions | environmental factor → physiological state → phenotype | “N. thermophilus exhibits cytoplasmic acidification in response to high Na+ concentrations” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24, https://doi.org/10.1128/aem.00145-24, 2024 | **Taxon-specific/uncertain.** Observed response is clear, but whether acidification is protective vs collateral should be curated cautiously. |
| hybrid salt-in + compatible-solute strategy → broad salinity growth range / optimum at 3.3–3.9 M Na+ | strategy/process → phenotype | “a hybrid strategy, combining the ‘compatible solute’ and ‘salt-in’ mechanisms” with optimum “3.3–3.9 M Na+” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24, https://doi.org/10.1128/aem.00145-24, 2024 | **Taxon-specific.** Very strong for a trait-mechanism edge because mechanism and numerical limits co-occur in one study. |
| low NaCl stress → glutamate and trehalose accumulation → osmoadaptation at lower salinity stress | environmental factor → metabolites → phenotype | “under low NaCl stress ZS-3 accumulates glutamate and trehalose” (shi2023mechanismofsalt pages 1-2) | Shi et al. 2023, doi:10.3390/ijms242115751, https://doi.org/10.3390/ijms242115751, 2023 | **Taxon-specific (*Priestia megaterium* ZS-3).** Useful but limited because exact low-NaCl threshold not given. |
| high salinity stress → proline, K+, and extracellular polysaccharides accumulation → osmotic response and growth up to 9% salinity | environmental factor → metabolites/cellular component → phenotype | “under high-salt conditions it relies on proline, K+ and extracellular polysaccharides” and “tolerates salinity up to 9%” (shi2023mechanismofsalt pages 1-2) | Shi et al. 2023, doi:10.3390/ijms242115751, https://doi.org/10.3390/ijms242115751, 2023 | **Taxon-specific.** Good candidate edge linking mechanism to numerical upper limit. |
| 0.5% NaCl medium → altered compatible-solute systems and transporters → higher stationary-phase cell density than other tested NaCl concentrations | environmental factor → gene-expression program → phenotype | “658 genes… including… compatible solute synthesis systems, transporters” and “0.5% NaCl had a higher cell density than… other NaCl concentrations” (zhang2023transcriptomeanalysisreveals pages 1-2) | Zhang et al. 2023, doi:10.3390/ijms24032621, https://doi.org/10.3390/ijms24032621, 2023 | **Taxon-specific (*Vibrio parahaemolyticus*).** Edge is assay-specific and condition-specific; direct causality from DE genes to cell density remains partial. |
| inability to grow in 9% NaCl M9 medium → indicates upper salinity growth boundary under that assay | assay condition → phenotype boundary → trait value | “could survive in… different NaCl concentrations, except for the M9 medium containing 9% NaCl” (zhang2023transcriptomeanalysisreveals pages 1-2) | Zhang et al. 2023, doi:10.3390/ijms24032621, https://doi.org/10.3390/ijms24032621, 2023 | **Taxon-specific / assay-specific.** This is a direct phenotype boundary observation, but medium-dependent and not mechanistic by itself. |
| exposure above Topt → increases apparent Tmin / shifts thermal performance toward warmer adaptation | environmental factor → cardinal-temperature parameter → phenotype | “Tmin… increased when incubated above Topt” (baath2024temperatureadaptationof pages 1-2) | Bååth & Kritzberg 2024, doi:10.1007/s00248-024-02353-8, https://doi.org/10.1007/s00248-024-02353-8, 2024 | **General/community-level.** Good temperature-adaptation edge, though at community rather than single-organism scale. |
| rising temperature treatment → rapid increase in temperature sensitivity index (SI) → faster adaptation to higher-temperature growth conditions | environmental factor → quantitative adaptation metric → phenotype | “high treatment temperatures produced increased SI within days for the winter community” (baath2024temperatureadaptationof pages 1-2) | Bååth & Kritzberg 2024, doi:10.1007/s00248-024-02353-8, https://doi.org/10.1007/s00248-024-02353-8, 2024 | **General/community-level.** Supports dynamic shift of growth-range descriptor rather than a fixed species trait. |
| each taxon’s specific optimum growth temperature → constrains environmental growth range occupancy | phenotype parameter → environmental distribution/growth range → phenotype | “each taxon has a specific optimum growth temperature” and microbes often have “narrower temperature ranges in nature than in the lab” (gonzalez2023microbialgrowthunder pages 2-3) | Gonzalez & Aranda 2023, doi:10.3390/microorganisms11071641, https://doi.org/10.3390/microorganisms11071641, 2023 | **General.** Conceptual edge useful for scope, but not a molecular mechanism. |
| amino-acid composition features → predict cardinal growth values (Topt/Tmin/Tmax, salinity, pH) → genome-based estimation of growth-range phenotype | sequence feature → computational inference → phenotype | “Temperature Optimum (Topt), Minimum (Tmin), and Maximum (Tmax) were modeled” and salinity/pH ranges were predicted from amino-acid composition (barnum2024predictingmicrobialgrowth pages 22-24) | Barnum et al. 2024, doi:10.1101/2024.03.22.586313, https://doi.org/10.1101/2024.03.22.586313, 2024 | **General/computational.** Not a biological causal edge for TraitMech, but valuable as evidence that numerical growth-range phenotypes are coherent predictive targets. |


*Table: This table lists candidate subject–predicate–object edges for curating the microbial trait 'growth range phenotype with numerical limits,' emphasizing pH and salinity mechanisms plus a few temperature-adaptation edges. It uses only evidence available in the conversation and marks whether support is general or taxon-specific.*

### 7) Expert opinions and analysis (authoritative synthesis)

**Homeostasis as the mechanistic substrate of growth ranges.** Poolman (2023) frames growth feasibility as a consequence of maintaining physicochemical variables “within limits,” especially **cytoplasmic pH**, **ionic strength**, **turgor/volume**, and **crowding**; this provides a mechanistic interpretation for why growth ranges exist along pH and salinity axes and why endpoints are biologically meaningful (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4).

**Lab vs environment and the interpretability of growth limits.** Gonzalez & Aranda (2023) emphasize that each taxon has a specific optimum growth temperature and that temperature (plus pH, salinity, water content, pollutants) sets boundaries, while also noting that **ranges in nature can be narrower than in lab** and that community growth is time-dependent net growth/decay, underscoring that “growth ranges” depend on context and measurement (gonzalez2023microbialgrowthunder pages 2-3).

**Quantitative trait prediction is now practical at scale but data quality is limiting.** Barnum et al. (2024) show numerical limits/optima are predictable from sequences, and highlight dataset biases (cultivation bias; discretized reported intervals) and higher error at extremes—important warnings for curating inferred traits versus measured traits (barnum2024predictingmicrobialgrowth pages 14-16, barnum2024predictingmicrobialgrowth pages 1-3).

### 8) Relevant statistics and quantitative data (recent studies)

- Cytoplasmic pH in many cells is kept “within the range of **7.0 to 7.5**” (poolman2023physicochemicalhomeostasisin pages 1-2).
- Neutralophiles can maintain PMF across an external pH range “about **5–8**” (poolman2023physicochemicalhomeostasisin pages 1-2).
- *N. thermophilus* growth across **3.1–4.9 M Na+**, with optimum **3.3–3.9 M Na+** (xing2024thepolyextremophilenatranaerobius pages 1-2).
- In *N. thermophilus*, intracellular glycine betaine increased from **52.7 mM → 893.1 mM** across 2.5 → 4.3 M Na+ (xing2024thepolyextremophilenatranaerobius pages 17-19).
- *Priestia megaterium* ZS-3 “tolerated salinity levels up to **9%**” (shi2023mechanismofsalt pages 1-2).
- GenomeSPOT (Barnum et al. 2024): trained on **15,596** genomes; predicted oxygen tolerance with **92% balanced accuracy**, temperature with **R2=0.73**, salinity **R2=0.81**, pH **R2=0.48**; curated ranges include pH **1.1–12.0**, salinity **0.0–27.5%** w/v NaCl, and temperature **4–105 °C**; applied to **85,205** sequenced species and **3,349** metagenomic samples (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 22-24, barnum2024predictingmicrobialgrowth pages 11-14).

### 9) Warnings / claims that should not yet be curated (or should be curated as uncertain)

1. **Assay-specific growth limits.** Example: *V. parahaemolyticus* inability to grow/survive at 9% NaCl in **M9** medium is a numeric boundary but may not generalize across media; curate as **assay-conditioned** trait evidence (zhang2023transcriptomeanalysisreveals pages 1-2).

2. **Survival/acid-resistance vs growth-range extension.** Acid-resistance mechanisms in *E. coli* (decarboxylase systems) are strong for homeostasis, but the excerpted evidence is primarily about acid resistance and regulation, not necessarily measured growth-range endpoints; curate such edges as **inferred** unless paired with growth-boundary assays (li2024responseofescherichia pages 10-12).

3. **Community-level vs species-level temperature parameters.** Tmin shifts/SI in lake-water communities are informative but reflect community compositional change and acclimation, not a single genome-defined trait; curate as **community trait** or as evidence for plasticity (baath2024temperatureadaptationof pages 1-2, baath2024temperatureadaptationof pages 2-4).

4. **Computational predictions are not mechanistic edges.** GenomeSPOT provides powerful trait estimates and statistics, but amino-acid composition → phenotype is not a direct causal mechanism without additional biological validation; curate as *evidence of predictability* rather than a TraitMech mechanism (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 14-16).

---

## DOI-first bibliography (with URLs and publication dates)

1. Poolman B. **Physicochemical homeostasis in bacteria**. *FEMS Microbiology Reviews* (Jun 2023). DOI: **10.1093/femsre/fuad033**. URL: https://doi.org/10.1093/femsre/fuad033 (poolman2023physicochemicalhomeostasisin pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4)

2. Gonzalez JM, Aranda B. **Microbial Growth under Limiting Conditions—Future Perspectives**. *Microorganisms* (Jun 2023). DOI: **10.3390/microorganisms11071641**. URL: https://doi.org/10.3390/microorganisms11071641 (gonzalez2023microbialgrowthunder pages 2-3, gonzalez2023microbialgrowthunder pages 3-5, gonzalez2023microbialgrowthundera pages 5-7)

3. Xing Q et al. **The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+**. *Applied and Environmental Microbiology* (May 2024). DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media eec50655, xing2024thepolyextremophilenatranaerobius media 7eed915d)

4. Shi L et al. **Mechanism of Salt Tolerance and Plant Growth Promotion in Priestia megaterium ZS-3 Revealed by Cellular Metabolism and Whole-Genome Studies**. *International Journal of Molecular Sciences* (Oct 2023). DOI: **10.3390/ijms242115751**. URL: https://doi.org/10.3390/ijms242115751 (shi2023mechanismofsalt pages 1-2)

5. Zhang Y et al. **Transcriptome Analysis Reveals the Effect of Low NaCl Concentration on Osmotic Stress and Type III Secretion System in Vibrio parahaemolyticus**. *International Journal of Molecular Sciences* (Jan 2023). DOI: **10.3390/ijms24032621**. URL: https://doi.org/10.3390/ijms24032621 (zhang2023transcriptomeanalysisreveals pages 1-2)

6. Bååth E, Kritzberg ES. **Temperature Adaptation of Aquatic Bacterial Community Growth Is Faster in Response to Rising than to Falling Temperature**. *Microbial Ecology* (Feb 2024). DOI: **10.1007/s00248-024-02353-8**. URL: https://doi.org/10.1007/s00248-024-02353-8 (baath2024temperatureadaptationof pages 1-2, baath2024temperatureadaptationof pages 2-4)

7. Barnum TP et al. **Predicting microbial growth conditions from amino acid composition**. *bioRxiv* (Mar 2024). DOI: **10.1101/2024.03.22.586313**. URL: https://doi.org/10.1101/2024.03.22.586313 (barnum2024predictingmicrobialgrowth pages 1-3, barnum2024predictingmicrobialgrowth pages 22-24, barnum2024predictingmicrobialgrowth pages 14-16, barnum2024predictingmicrobialgrowth pages 11-14)

8. Ramoneda J et al. **Building a genome-based understanding of bacterial pH preferences**. *Science Advances* (Apr 2023). DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-2)

9. Li Z et al. **Response of Escherichia coli to Acid Stress: Mechanisms and Applications—A Narrative Review**. *Microorganisms* (Aug 2024). DOI: **10.3390/microorganisms12091774**. URL: https://doi.org/10.3390/microorganisms12091774 (li2024responseofescherichia pages 10-12)

10. Yao X et al. **How methanotrophs respond to pH: A review of ecophysiology**. *Frontiers in Microbiology* (Jan 2023). DOI: **10.3389/fmicb.2022.1034164**. URL: https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)


References

1. (gonzalez2023microbialgrowthunder pages 3-5): Juan M. Gonzalez and Beatriz Aranda. Microbial growth under limiting conditions-future perspectives. Microorganisms, 11:1641, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071641, doi:10.3390/microorganisms11071641. This article has 244 citations.

2. (gonzalez2023microbialgrowthundera pages 5-7): JM Gonzalez and B Aranda. Microbial growth under limiting conditions-future perspectives. microorganisms 2023; 11: 1641. Unknown journal, 2023.

3. (baath2024temperatureadaptationof pages 1-2): Erland Bååth and Emma S. Kritzberg. Temperature adaptation of aquatic bacterial community growth is faster in response to rising than to falling temperature. Microbial Ecology, Feb 2024. URL: https://doi.org/10.1007/s00248-024-02353-8, doi:10.1007/s00248-024-02353-8. This article has 30 citations and is from a domain leading peer-reviewed journal.

4. (baath2024temperatureadaptationof pages 2-4): Erland Bååth and Emma S. Kritzberg. Temperature adaptation of aquatic bacterial community growth is faster in response to rising than to falling temperature. Microbial Ecology, Feb 2024. URL: https://doi.org/10.1007/s00248-024-02353-8, doi:10.1007/s00248-024-02353-8. This article has 30 citations and is from a domain leading peer-reviewed journal.

5. (barnum2024predictingmicrobialgrowth pages 22-24): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

6. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

7. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 47 citations and is from a domain leading peer-reviewed journal.

8. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

9. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius media eec50655): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

12. (xing2024thepolyextremophilenatranaerobius media 7eed915d): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

13. (barnum2024predictingmicrobialgrowth pages 1-3): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

14. (barnum2024predictingmicrobialgrowth pages 11-14): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

15. (shi2023mechanismofsalt pages 1-2): Lina Shi, Xiaoxia Zhu, Ting Qian, Jiazhou Du, Yuanyuan Du, and Jianren Ye. Mechanism of salt tolerance and plant growth promotion in priestia megaterium zs-3 revealed by cellular metabolism and whole-genome studies. International Journal of Molecular Sciences, 24:15751, Oct 2023. URL: https://doi.org/10.3390/ijms242115751, doi:10.3390/ijms242115751. This article has 21 citations.

16. (zhang2023transcriptomeanalysisreveals pages 1-2): Youkun Zhang, Xiaotong Tan, Mingzhu Li, Peng Liu, Xinan Jiao, and Dan Gu. Transcriptome analysis reveals the effect of low nacl concentration on osmotic stress and type iii secretion system in vibrio parahaemolyticus. International Journal of Molecular Sciences, 24:2621, Jan 2023. URL: https://doi.org/10.3390/ijms24032621, doi:10.3390/ijms24032621. This article has 19 citations.

17. (li2024responseofescherichia pages 10-12): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 35 citations.

18. (gonzalez2023microbialgrowthunder pages 2-3): Juan M. Gonzalez and Beatriz Aranda. Microbial growth under limiting conditions-future perspectives. Microorganisms, 11:1641, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071641, doi:10.3390/microorganisms11071641. This article has 244 citations.

19. (barnum2024predictingmicrobialgrowth pages 14-16): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 47 citations.

20. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

21. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.