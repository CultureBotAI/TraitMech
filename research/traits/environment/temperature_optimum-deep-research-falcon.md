---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:53:39.506333'
end_time: '2026-06-18T02:08:21.464204'
duration_seconds: 881.96
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum
  trait_identifier: METPO:1000304
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature phenotype with numerical limits that represents the ambient-temperature
    conditions at which an organism exhibits the most efficient growth and reproduction.
  parent_traits: METPO:1000533, METPO:1000536
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports the ambient temperature
    at which membrane and enzyme function are best maintained as the operational definition
    of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated
    fatty acids (Membrane-adaptation review supports homoviscous membrane composition
    as a key mechanism setting the temperature optimum.)'
  causal_graph_summary: 'temperature_optimum_balanced_adaptation: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum
- **METPO identifier:** METPO:1000304
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000533, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the ambient temperature at which membrane and enzyme function are best maintained as the operational definition of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition as a key mechanism setting the temperature optimum.)
- **Existing causal graph summary:** temperature_optimum_balanced_adaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **temperature optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum.yaml`.

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
- **Trait label:** temperature optimum
- **METPO identifier:** METPO:1000304
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that represents the ambient-temperature conditions at which an organism exhibits the most efficient growth and reproduction.
- **Parent traits:** METPO:1000533, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the ambient temperature at which membrane and enzyme function are best maintained as the operational definition of temperature optimum.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition as a key mechanism setting the temperature optimum.)
- **Existing causal graph summary:** temperature_optimum_balanced_adaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **temperature optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Temperature Optimum (METPO:1000304)

### Scope summary (trait meaning, assay context, boundary cases)
**Temperature optimum** (often operationalized as **optimal growth temperature, OGT**) is the ambient temperature at which a microbe’s growth rate (and thus reproduction) is maximal under specified conditions (medium, oxygen, pH, etc.). OGT is typically measured by quantifying growth across a temperature gradient (growth curves, doubling times, or maximum specific growth rate) and identifying the peak of the response curve (ramoneda2024leveraginggenomicinformation pages 2-4, ramoneda2024leveraginggenomicinformation pages 1-2).

**Boundary cases / nearby traits.** Temperature optimum is distinct from (i) *temperature tolerance* (e.g., maximum growth temperature), (ii) *temperature range for growth*, and (iii) *short-term survival after shock* (e.g., heat-shock survival). Category definitions commonly used in microbiology include: psychrophiles (grow at 0 °C, optimum near ~15 °C, do not grow at 20 °C), psychrotolerant/psychrotrophs (grow at 4 °C, optimum >20 °C), mesophiles (~20–45 °C), thermophiles (optima 50–80 °C), and hyperthermophiles (80–110 °C) (Jul 2023) (ramon2023ageneraloverview pages 1-2). A complementary review provides illustrative examples and notes that mesophilic *E. coli* grows best near 37 °C, grows poorly at 44 °C, and becomes frail near 50 °C (Mar 2023) (moon2023temperaturemattersbacterial pages 1-3).

**Assay considerations (curation-critical).**
* Temperature-response curves can be interpreted using Arrhenius-type plots: linear regions reflect physiological growth regimes, whereas deviations from linearity can indicate stress/non-physiological conditions (Oct 2024) (purwar2024adaptationsofpsychrophilic pages 8-10). 
* OGT is sensitive to interacting environmental variables (e.g., pH, oxygen, moisture). A 2024 perspective emphasizes that cultivation-based measurements are biased toward “standard” laboratory conditions (often ~30 °C, neutral pH, aerobic) and that laborious gradient assays and interacting variables can confound optima (Jan 2024) (ramoneda2024leveraginggenomicinformation pages 2-4).

### Key concepts and current understanding (mechanistic summary)
Temperature optimum emerges from **balanced adaptation across cellular subsystems**, with membrane physical state being a particularly well-supported mechanistic “bottleneck.” Multiple 2023–2024 sources converge on the framework that cells tune lipid composition to keep membrane properties within a functional range (“homeoviscous adaptation”) and coordinate this with macromolecular stability and gene regulation (ramon2023ageneraloverview pages 2-4, lee2024theintricatelink pages 8-8, singh2024(p)ppgppbufferscell pages 1-4).

#### 1) Membrane-centered mechanisms (homeoviscous adaptation)
**Bacteria:** Decreasing temperature tends to reduce membrane fluidity, triggering increased unsaturation and other lipid features that lower melting transitions and maintain appropriate viscosity. Quantitatively, a 2024 Chemical Science perspective reports that in *E. coli* total unsaturated fatty acids increased from ~45 mol% at 37 °C to ~60 mol% at 17 °C (Jan 2024) (lee2024theintricatelink pages 8-8). It also reports that increasing unsaturation from 20% to 60% can produce an ~10-fold decrease in membrane viscosity (20 → 2 poise) (FRAP/NBD-PE diffusion) (lee2024theintricatelink pages 8-8).

**Regulatory sensors (model systems):** In *Bacillus subtilis*, temperature downshift leads to membrane rigidification/thickening and activation of a two-component system. The 2024 Microbiology Spectrum study describes DesK as a membrane-associated histidine kinase/phosphatase that senses bilayer thickness changes and phosphorylates DesR, which induces the fatty acid desaturase gene *des*; Des desaturates fatty acyl chains to fluidize/thin the membrane (Jun 2024) (sidarta2024lipidphaseseparation pages 1-2). It also highlights a key caveat: strong rigidification can cause lipid phase separation, impairing sensing because DesK partitions into the fluid phase; the Pdes reporter was activated by mild shifts (37→25 °C) but not by harsher cold shock, suggesting **assay-specific nonlinearity** in sensor outputs (sidarta2024lipidphaseseparation pages 12-14).

**Strain- and species-specific lipidomic implementations:** A 2024 lipidomics study of *Acinetobacter baumannii* compared 37 °C vs 18 °C and found that at 18 °C five strains increased palmitoleic acid (C16:1), whereas one strain increased oleic acid (C18:1); total unsaturated fatty acids at 18 °C were ~60–80% across strains. Genomic context implicated desaturases and an insertion containing *fabA/fabB* among others (Oct 2024) (dessenne2024lipidomicanalysesreveal pages 8-12, dessenne2024lipidomicanalysesreveal pages 1-2).

**Archaea:** Thermoacidophilic archaeal membranes dominated by bipolar tetraethers (GDGT/GDNT) respond to temperature and pH by altering cyclopentane ring number and other features affecting packing/rigidity and proton permeability (Jan 2024) (chong2024archaeamembranesin pages 1-2). Quantitatively, *Sulfolobus acidocaldarius* increases average rings per tetraether from 3.4 to 4.8 as growth temperature rises 65→82 °C; critically, ring number also varies with growth rate (a confounder): rings decreased from 5.1 to 4.6 as growth rate increased 0.011→0.035 h⁻¹ at 75 °C and pH 3.1 (chong2024archaeamembranesin pages 1-2).

A major 2024 advance is the gene-level identification of enzymes for archaeal tetraether modification linked to temperature: a PNAS paper identifies **Gms** (GMGT synthase) and **Gmm** (GMGT methylase) and shows that GMGT abundance increases strongly with growth temperature in multiple archaea (e.g., *A. profundus* 18.5% at 70 °C → 94.2% at 90 °C; *A. fulgidus* 0.1% at 60 °C → 40.2% at 85 °C; *V. distributa* 0.5% at 85 °C → 22.1% at 99 °C). A methylation index also rose (0.09 ± 0.01 at 85 °C to 0.34 ± 0.01 at 99 °C in *V. distributa*) (Jun 2024) (garcia2024identificationoftwo pages 4-6, garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo pages 1-2). A Nature Communications study independently identifies Gms as a radical SAM enzyme catalyzing the GDGT→GMGT cross-link and notes mixed evidence across taxa (e.g., *Pyrococcus furiosus* showing decreased GMGT with increasing temperature), indicating the edge “temperature↑ → GMGT↑” is **strong but not universal** (Jun 2024) (li2024biosynthesisofgmgt pages 1-2).

#### 2) Regulatory coupling between membrane adaptation and growth/division
A 2024 Molecular Microbiology study provides a mechanistic bridge from membrane composition to growth phenotype. It states that in *E. coli* homeoviscous adaptation involves increasing cis-vaccenic acid (18:1) with decreasing temperature. When unsaturated fatty acid proportion was reduced (e.g., via *fadR* inactivation), cell division became dependent on (p)ppGpp; growth defects at low temperature could be rescued by expressing *ftsQ/ftsA/ftsZ* or supplementing exogenous palmitoleic acid (16:1), while saturated 16:0 did not rescue (Oct 2024) (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 8-11). This supports causal edges linking temperature-driven lipid remodeling to division control and to nucleotide stress signaling.

#### 3) Genome-informed prediction of temperature preferences (recent perspective)
A 2024 ISME Journal perspective summarizes the emerging practice of **predicting OGT/environmental preferences from genomes**, using genome/proteome-derived features (k-mers, amino acid composition, tRNA features, gene presence/absence). It highlights limitations: sparse and biased training sets (overrepresentation of readily culturable taxa), unknown causal genes, and phylogenetic structure that can inflate model performance if not validated properly. Recommended best practices include phylogenetically-aware validation and independent clade testing, and integrating genome-based prediction with cultivation-based assays (Jan 2024) (ramoneda2024leveraginggenomicinformation pages 4-6, ramoneda2024leveraginggenomicinformation pages 6-7, ramoneda2024leveraginggenomicinformation pages 7-7).

### Recent developments & latest research (2023–2024 prioritized)
1. **Quantitative membrane biophysics integration (2024):** Linking UFA fraction changes with measured viscosity changes and phase-transition considerations provides curatable intermediate states (membrane viscosity/fluidity) rather than only gene lists (Jan 2024) (lee2024theintricatelink pages 8-8).
2. **In vivo limitations of classic temperature sensors (2024):** The DesK system’s apparent inability to report harsh cold shocks due to phase separation implies that some “sensor → response” edges are **conditional on membrane phase state** (Jun 2024) (sidarta2024lipidphaseseparation pages 12-14).
3. **Strain-resolved lipidomics (2024):** *A. baumannii* strain-to-strain differences in which UFAs increase at low temperature (C16:1 vs C18:1) paired with genomic features (FabA/FabB presence, candidate desaturases) points to curatable nodes for mechanistic diversity (Oct 2024) (dessenne2024lipidomicanalysesreveal pages 8-12).
4. **Gene discovery in archaeal temperature adaptation (2024):** Identification of Gms and Gmm and demonstration of temperature-associated GMGT increases and methylation provides rare, high-confidence genotype-to-phenotype-to-lipid links in archaea relevant to high-temperature optima (Jun 2024) (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 6-7).

### Current applications and real-world implementations
* **Environmental microbiology & cultivation guidance:** Genome-based inference of temperature preferences is positioned as a way to guide cultivation of uncultured taxa and anticipate community shifts with global change, but requires careful validation and accounting for biases (Jan 2024) (ramoneda2024leveraginggenomicinformation pages 4-6, ramoneda2024leveraginggenomicinformation pages 2-4).
* **Clinical and applied microbiology:** Temperature-dependent lipidome remodeling in pathogens (e.g., *A. baumannii* at 18 vs 37 °C) informs hypotheses about persistence across environments and could inform interventions targeting membrane homeostasis (Oct 2024) (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12).
* **Extremophile-inspired membrane engineering (enabling technology context):** While not directly an OGT assay, 2024 literature emphasizes homeoviscous adaptation and osmolyte-mediated membrane stabilization as design principles in extremophile-like systems (Aug 2024) (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 3-4).

### Candidate nodes grouped by type (curation-oriented)
A node list with conservative ontology grounding is provided below.

| Node label | Node type (gene/protein/process/metabolite/environment/assay) | Suggested ontology grounding | Notes |
|---|---|---|---|
| temperature optimum / OGT | assay | METPO:1000304 | Target trait; operationally the temperature yielding maximal growth under a defined assay (ramon2023ageneraloverview pages 1-2, ramoneda2024leveraginggenomicinformation pages 2-4) |
| growth temperature | environment | label-only | Environmental input varied across culture assays; distinct from the optimum itself (ramoneda2024leveraginggenomicinformation pages 2-4, ramoneda2024leveraginggenomicinformation pages 1-2) |
| membrane fluidity | process | label-only | Central mechanistic intermediate in homeoviscous adaptation; avoid uncertain GO grounding here (lee2024theintricatelink pages 8-8, sidarta2024lipidphaseseparation pages 12-14) |
| membrane thickness | process | label-only | Mechanistically sensed by DesK in *Bacillus subtilis*; no confident ontology CURIE supplied here (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14) |
| homeoviscous adaptation | process | label-only | Widely used physiological concept for lipid remodeling that maintains membrane physical state across temperatures (maiti2024extrememakeoverthe pages 1-2, ramon2023ageneraloverview pages 2-4) |
| fatty acid biosynthetic process | process | GO:0006633 | Useful parent process for fabA/fabB/FadR-linked remodeling edges (singh2024(p)ppgppbufferscell pages 1-4, ramon2023ageneraloverview pages 2-4) |
| lipid biosynthetic process | process | GO:0008610 | Broad parent process for membrane lipid remodeling and archaeal tetraether changes (chong2024archaeamembranesin pages 1-2, lee2024theintricatelink pages 8-8) |
| fatty acid desaturase (Des) | protein | label-only | *B. subtilis* Δ5 acyl-lipid desaturase; exact protein accession not specified in evidence (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 18-19) |
| DesK | protein | label-only | Membrane-associated histidine kinase/phosphatase sensing thickness/fluidity changes in *B. subtilis* (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14) |
| DesR | protein | label-only | Response regulator phosphorylated by DesK; activates des promoter (sidarta2024lipidphaseseparation pages 1-2) |
| FadR | protein | label-only | *E. coli* transcriptional regulator activating unsaturated fatty acid biosynthesis genes (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 8-11) |
| FabR | protein | label-only | *E. coli* transcriptional repressor/sensor modulating fabA/fabB transcription in response to UFA/SFA state (ramon2023ageneraloverview pages 2-4) |
| fabA | gene | label-only | UFA biosynthesis gene; rescued low-fluidity phenotype when expressed in *E. coli* (singh2024(p)ppgppbufferscell pages 8-11, ramon2023ageneraloverview pages 2-4) |
| fabB | gene | label-only | UFA biosynthesis gene; activated by FadR and modulated by FabR (singh2024(p)ppgppbufferscell pages 1-4, ramon2023ageneraloverview pages 2-4) |
| ftsQ | gene | label-only | Cell division gene; combined plasmid expression with ftsA/ftsZ rescues low-fluidity division defects (singh2024(p)ppgppbufferscell pages 1-4) |
| ftsA | gene | label-only | Cell division gene in rescue of low-fluidity phenotype (singh2024(p)ppgppbufferscell pages 1-4) |
| ftsZ | gene | label-only | Cell division gene in rescue of low-fluidity phenotype (singh2024(p)ppgppbufferscell pages 1-4) |
| cis-vaccenic acid | metabolite | label-only | Major *E. coli* UFA associated with cold adaptation; CHEBI not asserted without high confidence here (singh2024(p)ppgppbufferscell pages 1-4, ramon2023ageneraloverview pages 4-5) |
| palmitoleic acid | metabolite | CHEBI:32395 | C16:1 fatty acid elevated at low temperature in several bacteria (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12) |
| oleic acid | metabolite | CHEBI:28837 | C18:1 fatty acid elevated in strain-specific low-temperature adaptation (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12) |
| saturated fatty acids | metabolite | label-only | Aggregate class used in UFA/SFA balance; no single CHEBI class asserted here (singh2024(p)ppgppbufferscell pages 8-11, ramon2023ageneraloverview pages 2-4) |
| unsaturated fatty acids | metabolite | label-only | Aggregate class central to membrane fluidization across temperature downshifts (lee2024theintricatelink pages 8-8, dessenne2024lipidomicanalysesreveal pages 8-12) |
| (p)ppGpp | metabolite | CHEBI:63972 | Alarmone state node; evidence explicitly ties low UFA proportion to ppGpp-dependent division buffering in *E. coli* (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 8-11) |
| cell division | process | GO:0051301 | Downstream process buffered by (p)ppGpp under low-fluidity conditions (singh2024(p)ppgppbufferscell pages 1-4) |
| GMGT | metabolite | label-only | Glycerol monoalkyl glycerol tetraether; archaeal membrane-spanning lipid increased at elevated temperature in several taxa (garcia2024identificationoftwo pages 6-7, li2024biosynthesisofgmgt pages 1-2) |
| GDGT | metabolite | label-only | Glycerol dialkyl glycerol tetraether; archaeal tetraether precursor/product class with temperature-linked cyclization (chong2024archaeamembranesin pages 1-2, li2024biosynthesisofgmgt pages 1-2) |
| cyclopentane ring index | assay | label-only | Quantitative descriptor for GDGT/GMGT cyclization state; affected by temperature and growth rate (garcia2024identificationoftwo pages 6-7, chong2024archaeamembranesin pages 1-2) |
| Gms | protein | label-only | GMGT synthase; radical SAM enzyme catalyzing GDGT-to-GMGT cross-link formation (garcia2024identificationoftwo pages 1-2, li2024biosynthesisofgmgt pages 1-2) |
| Gmm | protein | label-only | GMGT methylase; methylates GMGT hydrocarbon tail (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 3-4) |
| radical SAM enzyme | protein | label-only | Mechanistic enzyme class containing Gms/Gmm in archaeal lipid modification studies (garcia2024identificationoftwo pages 2-2, li2024biosynthesisofgmgt pages 6-7) |
| Arrhenius plot | assay | label-only | Growth-rate versus temperature interpretation tool; deviations from linearity indicate stress/non-physiological regime (purwar2024adaptationsofpsychrophilic pages 8-10) |
| growth rate (h-1) | assay | label-only | Important quantitative phenotype and confounder; e.g., archaeal ring number shifts with growth rate (chong2024archaeamembranesin pages 1-2) |
| thermoacidophile environment (low pH, high temperature) | environment | label-only | Composite environmental context for archaeal tetraether adaptation; no single confident ENVO term asserted (chong2024archaeamembranesin pages 1-2) |
| *Escherichia coli* | environment | NCBITaxon:562 | Key bacterial model for FadR/FabR/UFA/(p)ppGpp edges (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 8-11) |
| *Bacillus subtilis* | environment | NCBITaxon:1423 | Key model for DesK/DesR/Des membrane-thickness sensing (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14) |
| *Sulfolobus acidocaldarius* | environment | NCBITaxon:2285 | Thermoacidophile with quantitative GDGT ring changes across temperature/growth rate (chong2024archaeamembranesin pages 1-2) |
| *Archaeoglobus fulgidus* | environment | NCBITaxon:2234 | Archaeal producer showing temperature-linked GMGT increases (garcia2024identificationoftwo pages 4-6, garcia2024identificationoftwo pages 6-7) |


*Table: This table lists candidate nodes for a temperature-optimum causal graph and suggests conservative ontology grounding where confidence is high. It is useful for YAML curation because it separates confidently grounded entities from label-only nodes that still need expert review.*

### Candidate causal edges (evidence-backed triples)
The following table provides a curation-ready set of candidate edges with verbatim/near-verbatim snippets and notes (including confounders such as growth rate affecting archaeal ring indices).

| Subject node | Predicate | Object node | Evidence (DOI, year, URL) | Supporting snippet (verbatim/near-verbatim) | Notes/limitations (e.g., taxon-specific, assay-specific, uncertain) |
|---|---|---|---|---|---|
| decreased temperature | decreases | membrane fluidity | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | “to maintain membrane fluidity at low temperature organisms alter membrane lipid composition (‘homeoviscous adaptation’)” (ramon2023ageneraloverview pages 2-4) | Broad bacterial review inference; supports environmental input to membrane state rather than direct OGT value. |
| decreased temperature | increases | membrane unsaturated fatty acid proportion | 10.1039/d3sc04523d, 2024, https://doi.org/10.1039/d3sc04523d | “total UFA ~45 mole% at 37 °C → ~60 mole% at 17 °C” in *E. coli* (lee2024theintricatelink pages 8-8) | Taxon-specific quantitative example from *E. coli*; likely generalizable as homeoviscous adaptation but not universal. |
| increased membrane unsaturation | decreases | membrane viscosity | 10.1039/d3sc04523d, 2024, https://doi.org/10.1039/d3sc04523d | “increasing unsaturation from 20% to 60% produced an estimated 10-fold decrease in membrane viscosity (20 → 2 poise)” (lee2024theintricatelink pages 8-8) | Biophysical readout from inner membrane vesicles/FRAP; assay-specific. |
| temperature decrease | causes | membrane rigidification and thickening | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | “DesK senses small membrane thickness changes… when shifted from 37°C to 25°C” and larger downshifts caused “measurable membrane rigidification” (sidarta2024lipidphaseseparation pages 12-14) | *Bacillus subtilis* specific; in vivo reporter/sensing context. |
| membrane thickening | activates | DesK histidine kinase | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | “DesK, a membrane-associated histidine kinase/phosphatase, senses bilayer thickness (activated upon membrane thickening)” (sidarta2024lipidphaseseparation pages 1-2) | Strong mechanistic support, but from model Gram-positive bacterium. |
| DesK | phosphorylates/activates | DesR | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | “DesK… autophosphorylates at His188, and phosphorylates the response regulator DesR” (sidarta2024lipidphaseseparation pages 1-2) | Well-supported pathway edge; species-specific. |
| DesR~P | induces expression of | des fatty acid desaturase gene | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | “Phosphorylated DesR tetramerizes, binds the des promoter, and induces des expression” (sidarta2024lipidphaseseparation pages 1-2) | Canonical *B. subtilis* cold-shock response; regulatory edge. |
| Des fatty acid desaturase | increases | membrane fatty acyl desaturation | 10.1128/spectrum.03925-23, 2024, https://doi.org/10.1128/spectrum.03925-23 | “Des then desaturates fatty acyl chains, fluidizing and thinning the membrane” (sidarta2024lipidphaseseparation pages 1-2) | Strong mechanistic edge; localized to membrane adaptation. |
| FabR | represses/modulates | fabA/fabB transcription | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | “FabR is a transcriptional repressor that senses UFAs/SFAs… and modulates fabA/fabB transcription” (ramon2023ageneraloverview pages 2-4) | Review-based; strongest for *E. coli* UFA biosynthesis control. |
| FadR | activates | unsaturated fatty acid biosynthesis genes | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | “FadR is a key transcriptional regulator that activates unsaturated fatty acid biosynthesis (fabA, fabB, fabHDG)” (singh2024(p)ppgppbufferscell pages 1-4) | Strong *E. coli* evidence; regulatory edge linked to low-fluidity adaptation. |
| reduced membrane UFA proportion | causes dependency on | (p)ppGpp for cell division/growth | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | “Reducing the membrane proportion of unsaturated fatty acids made cell division dependent on (p)ppGpp” (singh2024(p)ppgppbufferscell pages 1-4) | Strong but specific to *E. coli* genetic backgrounds. |
| exogenous palmitoleic acid (16:1) | rescues | low-temperature growth defect under low-fluidity conditions | 10.1111/mmi.15323, 2024, https://doi.org/10.1111/mmi.15323 | “Exogenous palmitoleic acid (16:1) rescued low-temperature growth… whereas 16:0 did not” (singh2024(p)ppgppbufferscell pages 8-11) | Assay-specific rescue experiment in *E. coli* mutants; good causal support. |
| elevated temperature | increases | archaeal GMGT abundance | 10.1073/pnas.2318761121, 2024, https://doi.org/10.1073/pnas.2318761121 | “GMGT abundance increases with temperature… *A. profundus* shifts to >90% GMGT of monolayer lipids at 90 °C” (garcia2024identificationoftwo pages 6-7) | Strong primary evidence, but archaeal and taxon-specific. |
| Gms (GMGT synthase) | catalyzes formation of | GMGT from GDGT | 10.1073/pnas.2318761121, 2024, https://doi.org/10.1073/pnas.2318761121 | “a GMGT synthase (Gms)… forms the covalent interbiphytanyl bond” and heterologous expression “produced GMGTs” (garcia2024identificationoftwo pages 1-2) | Strong enzymatic/genetic edge for archaeal membrane adaptation. |
| Gmm (GMGT methylase) | methylates | GMGT hydrocarbon tail | 10.1073/pnas.2318761121, 2024, https://doi.org/10.1073/pnas.2318761121 | “coexpression of Gms with Gmm yielded mono-, di-, and minor tri-methylated GMGTs” (garcia2024identificationoftwo pages 1-2) | Strong for archaeal lipid modification; relation to OGT is indirect but plausible. |
| increased growth temperature | increases | GDGT/GMGT cyclopentane ring number | 10.3389/frbis.2023.1338019, 2024, https://doi.org/10.3389/frbis.2023.1338019 | “*Sulfolobus acidocaldarius* increases rings per tetraether from 3.4 to 4.8 when growth temperature rises from 65°C to 82°C” (chong2024archaeamembranesin pages 1-2) | Strong archaeal quantitative example; may reflect thermoacidophile-specific membrane optimization. |
| increased growth rate | decreases | GDGT ring number | 10.3389/frbis.2023.1338019, 2024, https://doi.org/10.3389/frbis.2023.1338019 | “rings decrease from 5.1 to 4.6 when growth rate increases from 0.011 to 0.035 h−1 at 75°C and pH 3.1” (chong2024archaeamembranesin pages 1-2) | Important confounder: ring number reflects growth rate as well as temperature; caution for curation. |
| Arrhenius plot deviation from linearity | indicates | stress/non-physiological growth regime | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | “Arrhenius plots, with linear regions indicating physiological growth and deviations indicating stress” (purwar2024adaptationsofpsychrophilic pages 8-10) | Assay/interpretation edge rather than mechanism; useful for phenotype boundary/measurement curation. |
| biased and sparse phenotype reference data | limits | genome-based OGT prediction generalizability | 10.1093/ismejo/wrae195, 2024, https://doi.org/10.1093/ismejo/wrae195 | “model accuracy is limited by small, sparse training datasets and by overrepresentation of readily culturable taxa” (ramoneda2024leveraginggenomicinformation pages 4-6) | Methodological caveat, not biological mechanism; should likely remain annotation-level rather than core TraitMech edge. |


*Table: This table lists candidate causal edges for curating microbial temperature optimum, covering membrane adaptation, lipid-regulatory pathways, archaeal tetraether modifications, assay interpretation, and genome-based prediction caveats. It is useful as a starting set of subject-predicate-object triples with source-backed snippets and curation notes.*

### Statistics and quantitative findings (for curation and QC)
* *E. coli* membrane UFA fraction: ~45 mol% at 37 °C → ~60 mol% at 17 °C (Jan 2024) (lee2024theintricatelink pages 8-8).
* Membrane viscosity estimate: unsaturation 20% → 60% corresponds to viscosity ~20 → 2 poise (10× decrease) (Jan 2024) (lee2024theintricatelink pages 8-8).
* *B. subtilis* lipid composition (LB): branched-chain fatty acids 80–96%; straight-chain 5–6%; UFA:SFA ratio ~0.075 (Jun 2024) (sidarta2024lipidphaseseparation pages 12-14).
* Archaeal tetraether ring index: *S. acidocaldarius* rings per tetraether 3.4 → 4.8 for 65→82 °C; and rings 5.1 → 4.6 when growth rate increases 0.011→0.035 h⁻¹ (Jan 2024) (chong2024archaeamembranesin pages 1-2).
* GMGT abundance increases with temperature in multiple archaea (examples):
  * *A. profundus* 18.5% at 70 °C → 94.2% at 90 °C;
  * *A. fulgidus* 0.1% at 60 °C → 40.2% at 85 °C;
  * *V. distributa* 0.5% at 85 °C → 22.1% at 99 °C;
  * methylation index 0.09±0.01 → 0.34±0.01 (85→99 °C) (Jun 2024) (garcia2024identificationoftwo pages 4-6, garcia2024identificationoftwo pages 6-7).
* In *A. baumannii* at 18 °C, total UFA content ~60–80% and specific increases in C16:1 or C18:1 depending on strain (Oct 2024) (dessenne2024lipidomicanalysesreveal pages 8-12).

### Expert opinions / analysis (authoritative source synthesis)
A strong consensus across 2023–2024 reviews and primary studies is that membrane physical properties are a proximal determinant of temperature preference because they constrain core processes (transport, signaling, division, and enzymatic function). Multiple sources explicitly frame homeoviscous adaptation as a fundamental/“universal” strategy, while also acknowledging context dependence (species-specific lipid systems and conditional sensor behavior) (lee2024theintricatelink pages 8-8, sidarta2024lipidphaseseparation pages 12-14, maiti2024extrememakeoverthe pages 1-2).

The 2024 ISME Journal perspective emphasizes that OGT is a multi-trait phenotype and cautions against overconfident genome-only inference due to dataset bias and unknown causal genes; it advocates integrating cultivation gradients with genomic modeling and robust validation (ramoneda2024leveraginggenomicinformation pages 4-6, ramoneda2024leveraginggenomicinformation pages 2-4).

### Warnings (claims not yet ready for TraitMech curation)
1. **Do not treat “GMGT abundance always increases with temperature” as universal.** Culture evidence includes at least one counterexample (reported for *Pyrococcus furiosus*), so the edge should be tagged **uncertain/taxon-dependent** unless constrained to specific clades/conditions (li2024biosynthesisofgmgt pages 1-2).
2. **Archaeal GDGT ring indices are confounded by growth rate and possibly growth phase.** Because ring number depends on temperature *and* growth rate, edges that map “temperature → cyclization” should include growth rate as a modifier or conditional node where possible (chong2024archaeamembranesin pages 1-2).
3. **DesK-based sensing may fail under harsh cold shock due to phase separation.** This implies “temperature downshift → DesK activation” is **assay- and regime-dependent** (mild vs harsh shifts) (sidarta2024lipidphaseseparation pages 12-14).
4. **Genome-based OGT predictions reflect training-set biases and phylogenetic signal.** These are best curated as metadata/annotation edges (e.g., ‘genome model predicts’) rather than direct mechanistic edges unless causal genes are established (ramoneda2024leveraginggenomicinformation pages 4-6).

---

## DOI-first bibliography (with dates and URLs)

1. **10.1128/spectrum.00757-24** (Oct 2024). Dessenne C. et al. *Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.* Microbiology Spectrum. https://doi.org/10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)
2. **10.1073/pnas.2318761121** (Jun 2024). Garcia A.A. et al. *Identification of two archaeal GDGT lipid–modifying proteins reveals diverse microbes capable of GMGT biosynthesis and modification.* PNAS. https://doi.org/10.1073/pnas.2318761121 (garcia2024identificationoftwo pages 1-2, garcia2024identificationoftwo pages 6-7, garcia2024identificationoftwo pages 4-6)
3. **10.1038/s41467-024-49650-x** (Jun 2024). Li Y. et al. *Biosynthesis of GMGT lipids by a radical SAM enzyme associated with anaerobic archaea and oxygen-deficient environments.* Nature Communications. https://doi.org/10.1038/s41467-024-49650-x (li2024biosynthesisofgmgt pages 1-2, li2024biosynthesisofgmgt pages 6-7)
4. **10.1128/spectrum.03925-23** (Jun 2024). Sidarta M. et al. *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK.* Microbiology Spectrum. https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)
5. **10.1093/ismejo/wrae195** (Jan 2024). Ramoneda J. et al. *Leveraging genomic information to predict environmental preferences of bacteria.* ISME Journal. https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 4-6, ramoneda2024leveraginggenomicinformation pages 2-4, ramoneda2024leveraginggenomicinformation pages 6-7)
6. **10.1039/d3sc04523d** (Jan 2024). Lee T.-H. et al. *The intricate link between membrane lipid structure and composition and membrane structural properties in bacterial membranes.* Chemical Science. https://doi.org/10.1039/d3sc04523d (lee2024theintricatelink pages 8-8)
7. **10.1111/mmi.15323** (Oct 2024). Singh V., Harinarayanan R. *(p)ppGpp buffers cell division when membrane fluidity decreases in Escherichia coli.* Molecular Microbiology. https://doi.org/10.1111/mmi.15323 (singh2024(p)ppgppbufferscell pages 1-4, singh2024(p)ppgppbufferscell pages 8-11)
8. **10.3389/frbis.2023.1338019** (Jan 2024). Chong P.L.-G. *Archaea membranes in response to extreme acidic environments.* Frontiers in Biophysics. https://doi.org/10.3389/frbis.2023.1338019 (chong2024archaeamembranesin pages 1-2)
9. **10.1039/d4cc03114h** (Aug 2024). Maiti A. et al. *Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.* Chemical Communications. https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 1-2, maiti2024extrememakeoverthe pages 3-4, maiti2024extrememakeoverthe pages 4-5)
10. **10.1007/s12275-023-00031-x** (Mar 2023). Moon S. et al. *Temperature Matters: Bacterial Response to Temperature Change.* Journal of Microbiology. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3)
11. **10.1007/s42770-023-01057-4** (Jul 2023). Ramón A. et al. *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* Brazilian Journal of Microbiology. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5)
12. **10.37256/amtt.5220244537** (Oct 2024). Purwar S., Srivastava S. *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* Applied Microbiology: Theory & Technology. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10)


References

1. (ramoneda2024leveraginggenomicinformation pages 2-4): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

2. (ramoneda2024leveraginggenomicinformation pages 1-2): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

3. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

5. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

6. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

7. (lee2024theintricatelink pages 8-8): Tzong-Hsien Lee, Patrick Charchar, Frances Separovic, Gavin E. Reid, Irene Yarovsky, and Marie-Isabel Aguilar. The intricate link between membrane lipid structure and composition and membrane structural properties in bacterial membranes. Chemical Science, 15:3408-3427, Jan 2024. URL: https://doi.org/10.1039/d3sc04523d, doi:10.1039/d3sc04523d. This article has 116 citations and is from a highest quality peer-reviewed journal.

8. (singh2024(p)ppgppbufferscell pages 1-4): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

10. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (dessenne2024lipidomicanalysesreveal pages 8-12): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

12. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 9 citations.

14. (garcia2024identificationoftwo pages 4-6): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

15. (garcia2024identificationoftwo pages 6-7): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

16. (garcia2024identificationoftwo pages 1-2): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

17. (li2024biosynthesisofgmgt pages 1-2): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

18. (singh2024(p)ppgppbufferscell pages 8-11): Vani Singh and Rajendran Harinarayanan. (p)<scp>ppgpp</scp> buffers cell division when membrane fluidity decreases in <i>escherichia coli</i>. Molecular Microbiology, 122:847-865, Oct 2024. URL: https://doi.org/10.1111/mmi.15323, doi:10.1111/mmi.15323. This article has 5 citations and is from a domain leading peer-reviewed journal.

19. (ramoneda2024leveraginggenomicinformation pages 4-6): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

20. (ramoneda2024leveraginggenomicinformation pages 6-7): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

21. (ramoneda2024leveraginggenomicinformation pages 7-7): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

22. (maiti2024extrememakeoverthe pages 1-2): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

23. (maiti2024extrememakeoverthe pages 3-4): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

24. (sidarta2024lipidphaseseparation pages 18-19): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

25. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

26. (garcia2024identificationoftwo pages 3-4): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

27. (garcia2024identificationoftwo pages 2-2): Andy A. Garcia, Grayson L. Chadwick, Xiao-Lei Liu, and Paula V. Welander. Identification of two archaeal gdgt lipid–modifying proteins reveals diverse microbes capable of gmgt biosynthesis and modification. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2318761121, doi:10.1073/pnas.2318761121. This article has 20 citations and is from a highest quality peer-reviewed journal.

28. (li2024biosynthesisofgmgt pages 6-7): Yanan Li, Ting Yu, Xi Feng, Bo Zhao, Huahui Chen, Huan Yang, Xing Chen, Xiao-Hua Zhang, Hayden R. Anderson, Noah Z. Burns, Fuxing Zeng, Lizhi Tao, and Zhirui Zeng. Biosynthesis of gmgt lipids by a radical sam enzyme associated with anaerobic archaea and oxygen-deficient environments. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49650-x, doi:10.1038/s41467-024-49650-x. This article has 21 citations and is from a highest quality peer-reviewed journal.

29. (maiti2024extrememakeoverthe pages 4-5): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.