---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:10:06.511673'
end_time: '2026-08-04T02:16:52.708849'
duration_seconds: 406.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: optimum phenotype with numerical limits
  trait_identifier: METPO:1000536
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: optimum_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the value at which an organism exhibits
    maximum growth rate or activity.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review
    supports the environmental value at which growth is maximal as a standard quantitative
    descriptor.) | DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports the external pH at which cytoplasmic homeostasis sustains peak growth
    as an analogous optimum on the pH axis.)'
  causal_graph_summary: 'optimum_phenotype_descriptor: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** optimum phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000536
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the value at which an organism exhibits maximum growth rate or activity.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the environmental value at which growth is maximal as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic homeostasis sustains peak growth as an analogous optimum on the pH axis.)
- **Existing causal graph summary:** optimum_phenotype_descriptor: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **optimum phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/optimum_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** optimum phenotype with numerical limits
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000536
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the value at which an organism exhibits maximum growth rate or activity.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the environmental value at which growth is maximal as a standard quantitative descriptor.) | DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports the external pH at which cytoplasmic homeostasis sustains peak growth as an analogous optimum on the pH axis.)
- **Existing causal graph summary:** optimum_phenotype_descriptor: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **optimum phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/optimum_phenotype_with_numerical_limits.yaml`.

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


# Curation report: microbial optimum phenotype with numerical limits

## Executive summary

**Trait:** “optimum phenotype with numerical limits”  
**Identifier:** **METPO:1000536**  
**Category/kind/status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** METPO:1000059

For TraitMech, this trait is best interpreted as an **assay-conditioned numerical argmax**: the environmental value, or experimentally unresolved interval, at which a specified organism displays its maximum measured growth rate or activity. Formally, for environmental variable \(x\), response \(y\), and fixed background conditions \(c\), the optimum is \(x^*=\arg\max_x y(x\mid c)\). It is therefore a descriptor of a response curve—not a universal intrinsic constant—and must retain the response endpoint, environmental axis, units, organism/strain, medium, atmosphere, and assay method.

The strongest recent mechanistic exemplar is *Natranaerobius thermophilus*: optimum growth was reported at **3.3–3.9 M Na+**, **pH 9.5**, and **53°C**, whereas its Na+ growth range extended to **3.1–4.9 M**. Proteomics, ddPCR, and metabolite/ion measurements support a hybrid compatible-solute plus K+ “salt-in” mechanism under salinity stress. This cleanly demonstrates why optimum and growth range must be represented separately. (xing2024thepolyextremophilenatranaerobius pages 1-2)

## 1. Trait scope and boundary cases

### 1.1 In scope

A record should instantiate **METPO:1000536** when it provides:

1. a microbial taxon, preferably strain-level;
2. a controlled environmental axis—such as temperature, extracellular pH, NaCl, Na+ concentration, salinity, water activity, oxygen, pressure, or irradiance;
3. a numerical value or interval with units;
4. an explicitly optimized endpoint, such as specific growth rate, doubling rate, biomass-production rate, respiration, substrate conversion, enzyme activity, or product formation; and
5. sufficient experimental context to interpret the value.

An interval such as 3.3–3.9 M Na+ is acceptable when the assay resolution does not identify a unique peak. It should be represented as an optimum interval, not converted to an unsupported midpoint.

### 1.2 Out of scope or separately represented

- **Minimum/maximum growth limits:** cardinal boundaries delimiting detectable growth, not the maximum response.
- **Tolerance or viable range:** all conditions permitting growth/survival. In *N. thermophilus*, 3.1–4.9 M Na+ is a range, while 3.3–3.9 M is the optimum interval. (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Survival optimum:** maximal viability after stress is not necessarily maximal growth rate.
- **Enzyme optimum:** include only if the endpoint is explicitly microbial activity and the graph records that endpoint; an isolated purified-enzyme optimum should not automatically become an organismal-growth optimum.
- **Categorical preference:** “thermophile,” “acidophile,” and “halophile” are ecological classifications, not numerical optimum observations.
- **In situ abundance peak:** an environmental abundance maximum may reflect competition, dispersal, or sampling and is not automatically an intrinsic physiological optimum.
- **Multifactor optimum:** temperature, pH, salinity, nutrients, oxygen, and medium interact. A value measured while other variables are uncontrolled should be annotated as conditional or uncertain.
- **Adapted versus ancestral optimum:** acclimation and evolution can shift response curves. A 2024 theoretical study predicts that evolution of species’ pH niches can stabilize communities, but this is modeling evidence rather than direct measurement of molecular causation. (mougi2024phadaptationstabilizes pages 1-2)

### 1.3 Recommended observation model

The YAML record should separate the **descriptor layer** from the **mechanism layer**:

- `environmental_axis`
- `optimum_lower_bound`
- `optimum_upper_bound`
- `unit`
- `optimized_response`
- `taxon` and `strain`
- `medium`, electron donor/acceptor, atmosphere, pressure, incubation time, and culture format
- `measurement_method`
- `growth_minimum` and `growth_maximum`, when available
- `evidence_type`: direct growth curve, activity curve, review statement, prediction, correlation, or model
- `mechanism_scope`: general, taxon-specific, or assay-specific

## 2. Candidate nodes grouped by type

Only identifiers that can be stated confidently are supplied; uncertain molecular families remain label-only rather than receiving invented CURIEs.

### Trait and assay nodes

- **optimum phenotype with numerical limits** — **METPO:1000536**
- **parent environmental trait** — **METPO:1000059**
- optimum growth temperature
- optimum extracellular pH
- optimum NaCl concentration / optimum Na+ concentration
- maximum specific growth rate
- maximum activity
- growth-response curve
- numerical optimum interval
- minimum growth limit; maximum growth limit; tolerance range

### Environmental and chemical nodes

- temperature
- extracellular pH
- salinity / osmolarity / water activity
- sodium ion — **CHEBI:29101**
- potassium ion — **CHEBI:29103**
- proton — **CHEBI:15378**
- glycine betaine — **CHEBI:17750**
- L-proline — **CHEBI:17203**
- L-glutamate — **CHEBI:29985**
- trehalose — **CHEBI:27082**
- oxygen — **CHEBI:15379**

Salinity records must state what was measured: NaCl % w/v, molar Na+, practical salinity units, total dissolved salts, and water activity are related but not interchangeable.

### Cellular structures and processes

- cytoplasm
- plasma membrane
- cytoplasmic pH homeostasis
- ion homeostasis
- osmotic adjustment / response to osmotic stress
- compatible-solute accumulation
- “salt-in” strategy
- “salt-out” strategy
- membrane-fluidity homeostasis
- protein folding and proteostasis
- heat-shock response
- cold-shock response
- RNA-temperature sensing
- DNA-topology regulation

### Genes, proteins, transporters, and complexes

- Opu-family glycine-betaine ABC transporters
- ProU-family glycine-betaine/proline ABC transporter
- SSS-family Na+/solute symporters
- Trk-type K+ transporter; COG0168 where a COG node is permitted
- Na+/K+/H+ transporter or antiporter, exact locus unresolved
- F1Fo-ATPase / Na+-translocating FOF1-ATPase
- amino-acid decarboxylase systems
- RNA thermometers in 5′ untranslated regions
- CspA and CsdA RNA chaperones
- heat-shock proteins, including Hsp17 in cited examples
- peptidyl-prolyl isomerases
- trigger factor
- *otsAB* trehalose-biosynthesis operon
- RpoS, *bolA*, curli/cellulose regulatory system

These labels should be resolved to strain-specific gene or UniProt identifiers only after consulting the cited organism’s genome annotation. Family-level review evidence does not justify a strain-specific accession.

### Taxon-specific candidate

- *Natranaerobius thermophilus* — retain as a label pending validation of the exact NCBITaxon identifier and strain used in the primary article.

## 3. Evidence-backed candidate causal edges

“Snippet” below is concise evidence text or a close source-preserving extraction. Predicates are deliberately conservative.

| # | Candidate subject–predicate–object triple | Reference and date | Supporting snippet | Curation note |
|---|---|---|---|---|
| 1 | external temperature — **alters** → nucleic acids, proteins, and membranes | Moon et al.; DOI [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x), March 2023 | “Temperature change alters cellular molecules including nucleic acids, proteins, and membranes.” | Broad review-supported edge; does not establish an exact optimum. (moon2023temperaturemattersbacterial pages 1-3)
| 2 | high temperature — **causes** → protein denaturation | Moon et al., 2023; same DOI | “High temperatures cause protein denaturation, threatening bacterial survival.” | Curatable as a generic stress edge; numerical threshold is taxon-specific. (moon2023temperaturemattersbacterial pages 1-3)
| 3 | high temperature — **melts** → inhibitory RNA-thermometer structure | Moon et al., 2023 | At low temperature the 5′-UTR closes the Shine–Dalgarno sequence; at high temperature “the structure melts, enabling translation.” | Mechanistic sensor edge; locus-specific RNA thermometers require taxon/locus evidence. (moon2023temperaturemattersbacterial pages 1-3)
| 4 | RNA-thermometer melting — **enables** → heat-shock-protein translation | Moon et al., 2023 | Melting exposes the ribosome-binding site and enables translation. | Curatable at class level; uncertain as a determinant of the exact optimum. (moon2023temperaturemattersbacterial pages 1-3)
| 5 | temperature change — **induces** → membrane-lipid remodeling | Moon et al., 2023 | “Temperature changes alter lipid composition in bacterial membranes, affecting membrane fluidity.” | Examples include *E. coli* and *Bacillus subtilis*; annotate taxon scope. (moon2023temperaturemattersbacterial pages 7-9)
| 6 | CspA/CsdA — **reduces formation of** → inhibitory RNA secondary structures at low temperature | Moon et al., 2023 | “CspA and CsdA function as RNA chaperones preventing secondary RNA structure formation at low temperatures.” | Taxon-specific examples; supports cold-growth capacity, not a numerical argmax. (moon2023temperaturemattersbacterial pages 7-9)
| 7 | low temperature — **increases abundance of** → trigger factor | Moon et al., 2023 | Trigger factor showed “~40-fold overexpression at low temperatures.” | Quantitative but context-specific; retain experimental taxon/conditions before curation. (moon2023temperaturemattersbacterial pages 7-9)
| 8 | low temperature — **induces** → *otsAB*-dependent trehalose accumulation | Moon et al., 2023 | In *E. coli*, trehalose accumulation via the *otsAB* operon is induced by cold shock and contributes to cold tolerance. | Taxon-specific; indirect relationship to optimum. (moon2023temperaturemattersbacterial pages 9-10)
| 9 | acidic external pH — **induces** → pH-homeostasis and acid-stress systems | Atasoy et al.; DOI [10.1093/femsre/fuad062](https://doi.org/10.1093/femsre/fuad062), November 2024 | Acid stress triggers “pH homeostasis, membrane modifications, alkalinity changes via amino acid decarboxylase systems, and stress protein production.” | Authoritative review synthesis; split into individual edges only when primary evidence identifies the organism and system. (atasoy2024exploitationofmicrobial pages 3-4)
| 10 | amino-acid decarboxylase systems — **increase** → intracellular alkalinity / acid resistance | Atasoy et al., 2024 | The review identifies “alkalinity changes via amino acid decarboxylase systems.” | Mechanistically plausible and review-supported; substrate-specific systems need primary references. (atasoy2024exploitationofmicrobial pages 3-4)
| 11 | acidophile pH-homeostasis mechanisms — **maintain** → circumneutral intracellular pH | González et al.; DOI [10.3389/fmicb.2024.1374800](https://doi.org/10.3389/fmicb.2024.1374800), May 2024 | “Despite extreme external pH, acidophiles maintain circumneutral intracellular pH.” | Curatable as an acidophile-level process; do not universalize the precise internal setpoint. (gonzalez2024acidophilicheterotrophsbasic pages 2-3)
| 12 | preadaptation at pH 4.5–5.0 — **improves** → probiotic viability in yogurt | Atasoy et al., 2024 | *Lactobacillus rhamnosus* GG and *Bifidobacterium animalis* BB12 had improved viability after adaptation at pH 4.5–5.0. | Assay- and strain-specific application; this is improved stress survival, not necessarily optimum growth. (atasoy2024exploitationofmicrobial pages 3-4)
| 13 | increasing salinity — **increases** → intracellular glycine betaine, glutamate, and proline | Xing et al.; DOI [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), May 2024 | Intracellular compatible solutes “increase with rising salinity levels.” | Strong, taxon-specific multi-omics evidence in *N. thermophilus*. (xing2024thepolyextremophilenatranaerobius pages 1-2)
| 14 | Opu/ProU ABC transporters and SSS symporters — **mediate** → compatible-solute accumulation | Xing et al., 2024 | The organism employs “glycine betaine ABC transporters (Opu and ProU families)” and “Na+/solute symporters (SSS family).” | Curatable as family-level, taxon-specific edges; identify loci before gene-level curation. (xing2024thepolyextremophilenatranaerobius pages 1-2)
| 15 | increasing salinity — **increases** → intracellular K+ | Xing et al., 2024 | Compatible-solute and K+ concentrations increased with external salinity. | Strong taxon-specific evidence for the hybrid strategy. (xing2024thepolyextremophilenatranaerobius pages 1-2)
| 16 | Na+/K+/H+ transporters — **support** → K+ and ion homeostasis under salinity stress | Xing et al., 2024 | Upregulated transporters facilitate maintenance of intracellular K+ under varying salinity. | Curatable if exact transporter annotations and directionality are checked in the primary data. (xing2024thepolyextremophilenatranaerobius pages 1-2)
| 17 | compatible-solute accumulation plus K+ accumulation — **supports** → osmotic adjustment and growth across high salinity | Xing et al., 2024 | The proteome, transcript, metabolite, and ion data support a hybrid “compatible solute” plus “salt-in” strategy. | Strongest mechanistic path, but it supports capacity near the optimum rather than proving that it sets 3.3–3.9 M. (xing2024thepolyextremophilenatranaerobius pages 1-2)
| 18 | increasing estuarine salinity — **is associated with increased abundance of** → Trk-type K+ transporter COG0168 | Wu et al.; DOI [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w), June 2024 | COG0168 was the most important feature and its relative abundance increased with salinity. | Natural-gradient association, not direct causation or an organismal optimum. (wu2024metagenomicinsightsinto pages 1-2)
| 19 | aquatic-biome salinity transition — **is associated with** → proteome pI/composition and gene-content change | Jurdzinski et al.; DOI [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059), May 2023 | Cross-biome transitions involved amino-acid and isoelectric-point changes plus convergent gene gains/losses. | Comparative evolutionary evidence; useful background, not a direct TraitMech optimum edge. (jurdzinski2023largescalephylogenomicsof pages 1-2)
| 20 | measured Na+ concentration 3.3–3.9 M — **is optimum condition for growth of** → *N. thermophilus* | Xing et al., 2024 | “Optimal growth occurs at 3.3–3.9 M Na+, pH 9.5, and 53°C.” | Direct descriptor edge suitable for curation with assay metadata. Keep the three axes as separate observations unless the paper explicitly reports a joint optimum. (xing2024thepolyextremophilenatranaerobius pages 1-2)

The main evidence and its curation readiness are summarized here:

| Environmental axis | Upstream perturbation | Mechanistic mediators | Homeostatic consequence | Relation to measured optimum | Strongest source / DOI | Evidence class | Curation status |
|---|---|---|---|---|---|---|---|
| Temperature | Shift above or below growth temperature | Membrane lipid remodeling; protein folding/chaperones; heat-shock and cold-shock proteins; RNA thermometers in 5'-UTRs; DNA topology changes (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 10-11) | Preserves membrane fluidity, translation, RNA handling, and proteostasis during temperature stress | Supports generic mechanism linking temperature to growth capacity, but does **not** by itself identify the numerical temperature argmax; assay- and taxon-dependent | Moon et al., 2023, *Journal of Microbiology*, DOI: 10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 10-11) | Review synthesis with taxon-specific examples | **Uncertain for TraitMech edge to exact optimum**; curate only broad temperature-response/homeostasis edges |
| pH | External acidification or alkalinization relative to preferred pH | Proton-translocating F1Fo-ATPase; proton pumps; amino-acid decarboxylase systems; membrane modifications; intracellular pH homeostasis systems (atasoy2024exploitationofmicrobial pages 3-4, atasoy2024exploitationofmicrobial pages 5-6, gonzalez2024acidophilicheterotrophsbasic pages 2-3) | Limits cytoplasmic acidification and maintains near-circumneutral intracellular pH or other viable intracellular setpoints | Strong evidence that deviation from optimal pH alters growth/activity and that homeostasis supports growth near preferred pH, but most sources do **not** resolve the exact numerical pH optimum for a given strain | Atasoy et al., 2024, *FEMS Microbiology Reviews*, DOI: 10.1093/femsre/fuad062; González et al., 2024, *Frontiers in Microbiology*, DOI: 10.3389/fmicb.2024.1374800 (atasoy2024exploitationofmicrobial pages 3-4, atasoy2024exploitationofmicrobial pages 5-6, gonzalez2024acidophilicheterotrophsbasic pages 2-3) | Review synthesis grounded in experimental literature | **Uncertain for exact argmax**; acceptable for generic pH-homeostasis subgraph, not for direct optimum value edge |
| Salinity / osmolarity | Increased external Na+ / salinity causing osmotic stress | Compatible-solute uptake and synthesis (glycine betaine, glutamate, proline); Opu/ProU ABC transporters; SSS-family Na+/solute symporters; Trk-type K+ uptake; Na+/K+/H+ transporters (xing2024thepolyextremophilenatranaerobius pages 1-2, wu2024metagenomicinsightsinto pages 1-2) | Osmotic adjustment, intracellular K+ maintenance, ion homeostasis, reduced salt stress burden | Strong mechanistic support that these systems enable growth across salinity conditions; in some taxa, quantitative salinity optima are reported, but many environmental studies establish adaptation rather than exact argmax | Xing et al., 2024, *Applied and Environmental Microbiology*, DOI: 10.1128/aem.00145-24; Wu et al., 2024, *Microbiome*, DOI: 10.1186/s40168-024-01817-w (xing2024thepolyextremophilenatranaerobius pages 1-2, wu2024metagenomicinsightsinto pages 1-2) | Primary experimental study plus natural-gradient metagenomics | **Partially curatable**: homeostasis edges yes; direct salinity→numerical optimum edge only when tied to strain-specific measurements |
| Salinity / osmolarity (taxon-specific numerical example) | 2.5, 3.1, 3.7, 4.3 M Na+ tested in *Natranaerobius thermophilus* | Glycine betaine transporters (Opu/ProU), SSS-family symporters, glutamate/proline synthesis, Na+/K+/H+ transporters; compatible-solute and K+ accumulation increase with salinity (xing2024thepolyextremophilenatranaerobius pages 1-2) | Hybrid “salt-out” + “salt-in” osmoadaptation; intracellular compatible solute and K+ accumulation support ion/osmotic homeostasis | **Strongest numerical example**: optimum growth reported at **3.3–3.9 M Na+**, with pH **9.5** and temperature **53°C**; supports a taxon-specific path from salinity adaptation machinery to observed optimum-associated growth regime, but still not a universal mechanism for all microbes | Xing et al., 2024, *Applied and Environmental Microbiology*, DOI: 10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2) | Direct primary experimental evidence | **Curate as taxon-specific, quantitative exemplar**; mark organism-specific and avoid over-generalization |
| Salinity (macroecological / comparative) | Transition among freshwater, brackish, and marine conditions | Proteome isoelectric-point shifts; convergent gene gain/loss; inorganic ion transport functions enriched with salinity (jurdzinski2023largescalephylogenomicsof pages 1-2, wu2024metagenomicinsightsinto pages 1-2) | Long-term adaptation of proteome chemistry and transporter repertoire to saline regime | Explains why salinity strongly structures niches and distributions, but does **not** provide organism-level numerical optima | Jurdzinski et al., 2023, *Science Advances*, DOI: 10.1126/sciadv.adg2059; Wu et al., 2024, *Microbiome*, DOI: 10.1186/s40168-024-01817-w (jurdzinski2023largescalephylogenomicsof pages 1-2, wu2024metagenomicinsightsinto pages 1-2) | Comparative phylogenomics / metagenomics | **Uncertain for direct TraitMech optimum edge**; useful as background support only |


*Table: This table summarizes candidate mechanistic routes linking environmental perturbations to microbial growth optima for METPO:1000536. It distinguishes broadly supported homeostasis edges from organism-specific evidence that more directly supports a measured numerical optimum.*

## 4. Recent developments, statistics, and expert analysis

### Genome-based prediction of optima

Barnum et al. trained amino-acid-composition models using growth-condition and genome data from **15,596 bacteria and archaea**, then applied them to **85,205 sequenced species** and **3,349 environmental samples**. Reported out-of-clade performance was salinity \(R^2=0.81\), RMSE **2.8% w/v NaCl**; temperature \(R^2=0.73\), RMSE **6.5°C**; and pH \(R^2=0.48\), RMSE **1.1 pH unit**. Protein-localization features particularly improved pH prediction. However, the manuscript was a March 2024 bioRxiv preprint in the retrieved record, and predictions were biased at extreme pH, below 15–25°C, and at 10–20% NaCl; they are prioritization tools rather than substitutes for measured optima. (barnum2024predictingmicrobialgrowth pages 6-9, barnum2024predictingmicrobialgrowth pages 14-16)

This work is important for cultivation design, but amino-acid composition is a slowly changing genomic signature and does not itself identify a causal molecular determinant. A predicted value should therefore be stored as `predicted_optimum`, never merged with a directly observed METPO phenotype without an evidence qualifier. (barnum2024predictingmicrobialgrowth pages 14-16)

### Salinity adaptation at organism and ecosystem scales

Xing et al. profiled *N. thermophilus* at **2.5, 3.1, 3.7, and 4.3 M Na+**, used iTRAQ proteomics, performed ddPCR on **109 upregulated proteins’ corresponding transcripts**, and measured intracellular compatible solutes and K+. The integration of these measurements makes this study the most suitable seed for a taxon-specific salinity mechanism module. (xing2024thepolyextremophilenatranaerobius pages 1-2)

Wu et al. reconstructed **127 MAGs** across a Pearl River Estuary salinity gradient. Of **12,162 COGs**, machine-learning feature selection identified **40** important features; eight were related to osmoregulation—four salt-in, three salt-out, and one water-channel function. Trk-type K+ transporter COG0168 ranked first. These data support ecological relevance of K+ transport but remain abundance-based associations. (wu2024metagenomicinsightsinto pages 1-2)

Jurdzinski et al. analyzed **13,783 MAGs**; only **14 of 3,561 genome clusters** contained MAGs from multiple freshwater, brackish, or marine biomes. This indicates that salinity is a major evolutionary barrier associated with proteome-wide and gene-content remodeling, but it does not measure individual strains’ numerical optima. (jurdzinski2023largescalephylogenomicsof pages 1-2)

### pH applications

Recent authoritative reviews emphasize that deviation from optimum pH reshapes microbial activity and community composition. Low-pH mechanisms are already exploited in food preservation, probiotic preparation, selective fermentation, biomining, bioremediation, and low-contamination bioprocessing. Conditions below **pH 5** can favor lactic-acid-bacterium/ethanol-producer consortia, while probiotic selection commonly tests survival around **pH 2.5** to simulate gastric transit. These are application thresholds or selection conditions, not automatically organismal growth optima. (atasoy2024exploitationofmicrobial pages 5-6)

Acidophilic heterotrophs can maintain near-circumneutral cytoplasmic pH and perform dissimilatory Fe(III) reduction, including reduction of jarosite, magnetite, goethite, and hematite. This supports applications in biomining, bioremediation, low-pH fermentation, microbial electrochemical systems, and extremozymes. (gonzalez2024acidophilicheterotrophsbasic pages 2-3)

### Temperature applications

Temperature-response mechanisms inform fermentation control, food safety, cold-chain spoilage, pathogen management, and cultivation of environmental isolates. Current expert synthesis emphasizes a systems-level balance involving membrane fluidity, RNA structure and processing, DNA topology, protein folding, compatible solutes, and stress regulons rather than one universal “optimum-temperature gene.” (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 9-10)

## 5. Recommended TraitMech graph architecture

A defensible graph should not connect every stress-response gene directly to **METPO:1000536**. Use an intermediate causal architecture:

1. `environmental value` → perturbs → `cellular physicochemical state`;
2. `sensor/homeostasis machinery` → regulates → `cellular physicochemical state`;
3. `homeostatic state` → supports → `growth or activity capacity`;
4. `growth/activity response curve` → has numerical argmax → **METPO:1000536 observation**.

For the strongest salinity exemplar:

`external Na+` → increases → `osmotic/ionic stress`  
`Opu/ProU and SSS transport systems` → increase → `compatible-solute accumulation`  
`Na+/K+/H+ transport systems` → support → `intracellular K+ maintenance`  
`compatible-solute accumulation + K+ accumulation` → support → `osmotic/ion homeostasis`  
`osmotic/ion homeostasis` → supports → `growth at high salinity`  
`growth-response curve` → has optimum interval → `3.3–3.9 M Na+`.

The last edge is directly observed; the claim that any individual transporter **sets** the exact optimum remains unproven. (xing2024thepolyextremophilenatranaerobius pages 1-2)

## 6. Warnings: claims not yet ready for curation

1. **Do not curate “stress-response gene determines optimum”** from induction alone. Induction outside the optimum may reflect damage control rather than peak-growth causation.
2. **Do not equate tolerance with optimum.** Survival at pH 2.5, growth below pH 4, or a 3.1–4.9 M Na+ range is not an optimum observation. (xing2024thepolyextremophilenatranaerobius pages 1-2, atasoy2024exploitationofmicrobial pages 5-6)
3. **Do not generalize *N. thermophilus* mechanisms across microbes.** Its hybrid strategy is explicitly taxon-specific and was reported as unusual within Clostridia. (xing2024thepolyextremophilenatranaerobius pages 1-2)
4. **Do not treat metagenomic enrichment as causal.** COG0168 abundance and proteome-pI patterns are salinity-associated comparative evidence. (jurdzinski2023largescalephylogenomicsof pages 1-2, wu2024metagenomicinsightsinto pages 1-2)
5. **Do not curate theoretical pH-niche adaptation as experimentally established causality.** Mougi’s community-stabilization result is model-based. (mougi2024phadaptationstabilizes pages 1-2)
6. **Do not treat machine-learning output as observed phenotype.** Barnum et al.’s substantial errors and extreme-condition biases require explicit prediction provenance. (barnum2024predictingmicrobialgrowth pages 6-9, barnum2024predictingmicrobialgrowth pages 14-16)
7. **Do not assign unverified CURIEs.** Opu, ProU, SSS, Trk, ATPase, and antiporter families require organism/locus resolution before UniProt, KEGG, Rhea, or EC identifiers are added.
8. **Do not collapse different salinity units.** M Na+, M NaCl, % w/v NaCl, PSU, total dissolved salts, and water activity need separate typed values.
9. **Do not infer a joint three-dimensional optimum** merely because salinity, pH, and temperature optima are listed together; curate separate axes unless a factorial response surface was measured.
10. **Mechanistic completeness remains limited.** The current evidence strongly supports homeostasis modules that permit growth around environmental optima, but rarely demonstrates that perturbing one component shifts the numerical argmax.

## 7. DOI-first bibliography

1. Xing Q, Zhang S, Tao X, et al. “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.” *Applied and Environmental Microbiology*. Published May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2)
2. Wu Z, Li M, Qu L, Zhang C, Xie W. “Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.” *Microbiome*. Published June 2024. DOI: [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w). (wu2024metagenomicinsightsinto pages 1-2)
3. Atasoy M, Álvarez Ordóñez A, Cenian A, et al. “Exploitation of microbial activities at low pH to enhance planetary health.” *FEMS Microbiology Reviews*. Published November 2024. DOI: [10.1093/femsre/fuad062](https://doi.org/10.1093/femsre/fuad062). (atasoy2024exploitationofmicrobial pages 3-4, atasoy2024exploitationofmicrobial pages 5-6)
4. González E, Vera F, Scott F, et al. “Acidophilic heterotrophs: basic aspects and technological applications.” *Frontiers in Microbiology*. Published May 2024. DOI: [10.3389/fmicb.2024.1374800](https://doi.org/10.3389/fmicb.2024.1374800). (gonzalez2024acidophilicheterotrophsbasic pages 2-3)
5. Mougi A. “pH adaptation stabilizes bacterial communities.” *npj Biodiversity*. Published October 2024. DOI: [10.1038/s44185-024-00063-5](https://doi.org/10.1038/s44185-024-00063-5). (mougi2024phadaptationstabilizes pages 1-2)
6. Barnum TP, Crits-Christoph A, Molla M, Carini P, Lee HH, Ostrov N. “Predicting microbial growth conditions from amino acid composition.” *bioRxiv*. Posted March 2024. DOI: [10.1101/2024.03.22.586313](https://doi.org/10.1101/2024.03.22.586313). **Preprint in the retrieved record.** (barnum2024predictingmicrobialgrowth pages 6-9, barnum2024predictingmicrobialgrowth pages 14-16)
7. Jurdzinski KT, Mehrshad M, Delgado LF, Deng Z, Bertilsson S, Andersson AF. “Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity.” *Science Advances*. Published May 2023. DOI: [10.1126/sciadv.adg2059](https://doi.org/10.1126/sciadv.adg2059). (jurdzinski2023largescalephylogenomicsof pages 1-2)
8. Moon S, Ham S, Jeong J, et al. “Temperature Matters: Bacterial Response to Temperature Change.” *Journal of Microbiology*. Published March 2023;61:343–357. DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 9-10)

## Curation conclusion

**METPO:1000536 should be curated primarily as a quantitatively measured, context-rich phenotype descriptor.** Mechanistic subgraphs should explain how environmental perturbations affect cellular homeostasis and thereby shape the response curve, while the numerical optimum itself should be linked only to direct growth/activity measurements. The *N. thermophilus* salinity study is presently the strongest seed for a concrete TraitMech implementation; temperature and pH modules are well supported at the homeostasis level but need more strain-specific perturbation studies before individual genes can be asserted to determine exact numerical optima.

References

1. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

2. (mougi2024phadaptationstabilizes pages 1-2): Akihiko Mougi. Ph adaptation stabilizes bacterial communities. npj Biodiversity, Oct 2024. URL: https://doi.org/10.1038/s44185-024-00063-5, doi:10.1038/s44185-024-00063-5. This article has 38 citations and is from a peer-reviewed journal.

3. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

5. (moon2023temperaturemattersbacterial pages 9-10): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

6. (atasoy2024exploitationofmicrobial pages 3-4): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 104 citations and is from a domain leading peer-reviewed journal.

7. (gonzalez2024acidophilicheterotrophsbasic pages 2-3): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.

8. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

9. (jurdzinski2023largescalephylogenomicsof pages 1-2): Krzysztof T. Jurdzinski, Maliheh Mehrshad, Luis Fernando Delgado, Ziling Deng, Stefan Bertilsson, and Anders F. Andersson. Large-scale phylogenomics of aquatic bacteria reveal molecular mechanisms for adaptation to salinity. Science Advances, May 2023. URL: https://doi.org/10.1126/sciadv.adg2059, doi:10.1126/sciadv.adg2059. This article has 61 citations and is from a highest quality peer-reviewed journal.

10. (moon2023temperaturemattersbacterial pages 10-11): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

11. (atasoy2024exploitationofmicrobial pages 5-6): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 104 citations and is from a domain leading peer-reviewed journal.

12. (barnum2024predictingmicrobialgrowth pages 6-9): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.

13. (barnum2024predictingmicrobialgrowth pages 14-16): Tyler P. Barnum, Alexander Crits-Christoph, Michael Molla, Paul Carini, Henry H. Lee, and Nili Ostrov. Predicting microbial growth conditions from amino acid composition. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.22.586313, doi:10.1101/2024.03.22.586313. This article has 57 citations.