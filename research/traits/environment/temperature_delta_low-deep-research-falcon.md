---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:31:49.671551'
end_time: '2026-08-04T03:41:07.383886'
duration_seconds: 557.71
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta low
  trait_identifier: METPO:1000484
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth of approximately 5\u201310 \xB0C, characteristic of organisms with limited\
    \ thermal-tolerance breadth."
  parent_traits: METPO:1000303
  synonyms: Td_5_10
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports limited thermal-adaptation flexibility
    as the basis of narrow thermal-tolerance breadths.)'
  causal_graph_summary: 'temperature_delta_low_limited_breadth: 8 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000484
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 5–10 °C, characteristic of organisms with limited thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_5_10
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports limited thermal-adaptation flexibility as the basis of narrow thermal-tolerance breadths.)
- **Existing causal graph summary:** temperature_delta_low_limited_breadth: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_low.yaml`.

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
- **Trait label:** temperature delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000484
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth of approximately 5–10 °C, characteristic of organisms with limited thermal-tolerance breadth.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_5_10
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports limited thermal-adaptation flexibility as the basis of narrow thermal-tolerance breadths.)
- **Existing causal graph summary:** temperature_delta_low_limited_breadth: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_low.yaml`.

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


# Curation report: **temperature delta low**

## Executive scope summary

**Trait:** “temperature delta low”  
**Identifier:** **METPO:1000484**  
**Parent:** **METPO:1000303**  
**Synonym:** *Td_5_10*  
**Proposed operational meaning:** an assay-observed, growth-supporting temperature breadth of approximately **5–10 °C**, calculated as **ΔT = Tmax − Tmin**, where Tmin and Tmax are the lower and upper temperatures permitting sustained population growth under a specified set of culture conditions.

This is principally an **environmental tolerance-breadth phenotype**, not a preferred or optimum temperature. Tmin can be operationalized as the temperature at which lag time or generation time tends toward infinity; the upper boundary reflects failure of growth as high-temperature damage overwhelms homeostasis (chandler2023theeffectof pages 31-35). Because the result depends on medium, pH, water activity, atmosphere, inoculum, incubation duration, and growth-detection threshold, those assay variables should accompany every assertion of **METPO:1000484**.

The evidence does **not** support a universal molecular cause of a 5–10 °C breadth. The strongest curatable mechanism is a *Bacillus subtilis*-specific membrane-sensing chain—DesK→DesR→*des*→fatty-acid desaturation→membrane fluidity. It explains one axis of low-temperature growth capacity, but not by itself why an organism has exactly a 5–10 °C total breadth. Recent work also shows that this pathway may fail during severe cold-induced membrane phase separation (mansilla2004controlofmembrane pages 5-5, sidarta2024lipidphaseseparation pages 1-2).

| Module | Representative triple | Evidence strength | Curate now? | Main caveat |
|---|---|---|---|---|
| Assay-defined thermal breadth | assay-derived Tmin/Tmax difference → defines low temperature delta (5–10 °C) | Strong for trait scope/definition (chandler2023theeffectof pages 31-35) | Yes | Definitional only; not a mechanism, and highly assay-dependent (medium, pH, atmosphere, time, inoculum). |
| DesK–DesR–des–UFA–fluidity | low membrane fluidity → DesK activates DesR → des transcription → more unsaturated fatty acids → maintained membrane fluidity at low temperature (mansilla2004controlofmembrane pages 5-5, hunger2004geneticevidencefor pages 1-2, mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 2-4) | Strong mechanistic | Yes, with taxon notes | Best-supported in *Bacillus subtilis* and related Gram-positives; 2024 work indicates sensing may fail under harsh cold/phase separation, so breadth-limiting interpretation should be qualified (sidarta2024lipidphaseseparation pages 1-2). |
| Extreme-temperature damage limits growth | temperature extremes → membrane/protein/RNA/DNA damage → growth limit/Tmin-Tmax boundaries (chandler2023theeffectof pages 31-35) | Moderate, broad/general | Yes, as coarse background edge | Too nonspecific to explain why breadth is specifically 5–10 °C; not diagnostic of narrow breadth. |
| Chaperone/proteostasis capacity | DnaK/DnaJ/GroEL/sHSP activity → improved protein folding/anti-aggregation → thermal tolerance (sionek2024theimpactof pages 3-5, hurtadobautista2024thermalplasticityand pages 17-18, liang2024interactionsbetweenchaperone pages 8-10, liang2024interactionsbetweenchaperone pages 16-17) | Moderate but mixed | Not yet, or curate only as supportive/uncertain | Often measures acute heat-shock survival rather than sustained growth breadth; effects can be lineage-specific and trade-off laden. |
| c-di-AMP–K+ homeostasis–thermotolerance | c-di-AMP pathway changes → altered potassium/osmotic homeostasis → increased thermotolerance (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 15-16) | Weak-to-moderate, recent | Not yet; mark uncertain | 2024 Bacillus evidence is largely convergent/correlative from evolution experiments; causative allele-to-breadth mapping remains unresolved. |


*Table: This table summarizes which mechanism modules for low temperature-delta breadth are ready for TraitMech curation versus which should remain provisional. It emphasizes the strongest current module, broad background constraints, and areas where recent evidence is promising but still too indirect.*

## 1. Trait scope and boundary cases

### 1.1 Included phenotype

A defensible TraitMech representation is:

> **Observed sustained growth over only ~5–10 °C under a defined assay, bounded by Tmin and Tmax.**

The phenotype should be established by measurements at enough temperatures to resolve both limits, preferably using a fitted thermal-performance curve or cardinal-temperature model. A 2024 comparison of **2,739 datasets and 83 thermal-performance models** found no universally best model, reinforcing the need to record the selected model and uncertainty rather than treating Tmin and Tmax as model-independent constants.

### 1.2 Excluded or adjacent traits

1. **Temperature optimum:** Topt is the temperature of maximal growth rate, not the breadth of temperatures permitting growth.
2. **Psychrophily, mesophily, or thermophily:** these locate the thermal niche; they do not specify its width. A cold stenotherm and hot stenotherm could both have **METPO:1000484**.
3. **Acute heat-shock survival:** survival for minutes at a lethal temperature is not sustained growth. For example, 2024 *Legionella pneumophila* experiments measured population decline during a **30-minute, 55 °C** challenge; such results concern heat-shock resistance, not directly ΔT (liang2024interactionsbetweenchaperone pages 8-10).
4. **Cold-shock survival or dormancy:** viability without replication does not establish a growth-supporting temperature.
5. **Spore survival:** *Bacillus* vegetative-cell thermal adaptation must be separated from the survival of spores (hurtadobautista2024thermalplasticityand pages 2-3).
6. **Niche breadth inferred from environmental occurrence:** detection across sites or seasons can reflect dispersal, dormancy, strain mixtures, or biotic interactions rather than growth by one genotype.
7. **A 5–10 °C assay window:** growth at every tested temperature within a narrow experimental window does not prove that Tmin and Tmax have been reached.

### 1.3 Recommended evidence rule

Curate the trait only when both bounds are observed or estimated with suitable bracketing temperatures. Record:

- strain and taxon;
- vegetative cells versus spores;
- medium and nutrient concentrations;
- pH, water activity/osmolarity, oxygen/electron acceptor;
- inoculum and preconditioning temperature;
- incubation duration and growth endpoint;
- fitted model and confidence intervals;
- measured Tmin, Topt, Tmax, and ΔT.

## 2. Current understanding and recent developments

### Membrane homeoviscous adaptation

Cooling orders and thickens lipid bilayers. Bacteria commonly compensate by increasing unsaturated fatty acids or fatty acids with comparable disordering effects, thereby lowering the lipid phase-transition temperature and maintaining membrane transport, permeability, and protein function. This is **homoviscous adaptation** (mendoza2014temperaturesensingby pages 2-4).

In *B. subtilis*, reduced membrane fluidity activates the membrane histidine kinase DesK. DesK phosphorylates DesR, phosphorylated DesR activates *des* transcription, and the Des Δ5-desaturase introduces cis double bonds into existing phospholipid acyl chains. Experiments changing anteiso-branched-chain fatty-acid availability at constant temperature show that membrane physical state, rather than temperature itself, is the proximal signal (mansilla2004controlofmembrane pages 5-5, hunger2004geneticevidencefor pages 1-2, mendoza2014temperaturesensingby pages 5-6).

A major 2024 qualification is that *des* expression responded to mild temperature shocks but not harsh cold or antibiotic-induced stress. Lipid phase separation apparently partitions DesK into fluid domains and impairs thickness sensing; deletion of *des*, *desK*, or *desR* also did not produce the anticipated stress-growth defects. Thus, this canonical pathway should not be represented as universally sufficient for broad cold adaptation (sidarta2024lipidphaseseparation pages 1-2).

### Proteostasis and heat/cold-shock systems

Heat damages or unfolds proteins; DnaK/DnaJ, GroEL/GroES, small HSPs, ClpB, and related systems assist folding, prevent irreversible aggregation, or promote recovery. In lactic-acid bacteria, DnaK, GroEL/GroES, small HSPs, and cold-shock proteins such as CspL/CspP/CspC are reported components of temperature-stress responses (sionek2024theimpactof pages 3-5).

Nevertheless, chaperone activity is not a monotonic proxy for sustained thermal breadth. In 2024 laboratory evolution of *L. pneumophila*, variants in *dnaK*, *dnaJ*, *htpG*, and *clpX* improved acute heat-shock survival, but the assays emphasized lethal-temperature survival rather than growth across cardinal temperatures; evolved variants were absent from surveyed natural isolates, suggesting ecological costs or limited generality (liang2024interactionsbetweenchaperone pages 8-10, liang2024interactionsbetweenchaperone pages 16-17). These edges are therefore mechanistically plausible but not diagnostic of **METPO:1000484**.

### c-di-AMP, potassium, and osmotic homeostasis

A 2024 *Bacillus* experimental-evolution study found convergent mutations affecting c-di-AMP synthesis or regulation—*disA* in *B. cereus* and *cdaR* in *B. subtilis*. c-di-AMP controls potassium transport and osmotic balance, and the authors proposed that this homeostatic axis mitigates heat-associated membrane destabilization. Compatible solutes such as glycine betaine and proline were also discussed as heat protectants (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 15-16).

The result is promising but not yet a direct causal chain from allele to thermal breadth. Multiple mutations arose together, genome sequencing alone did not identify the causal variants, and transcriptomic or reverse-genetic validation was recommended (hurtadobautista2024thermalplasticityand pages 16-17). This module should remain **uncertain** in the trait graph.

### Evolutionary constraints and statistics

The same 2024 study exposed six wild *Bacillus* strains from the *B. cereus* and *B. subtilis* lineages to gradual warming. Mesophilic strains were described as typically thriving around **27–40 °C**. Thermal adaptation remained limited: the maximum reported extension was approximately **4 °C**, only one *B. subtilis* line substantially expanded its niche, and the lineages generally failed to adapt robustly even to temperatures approximately **3 °C** beyond their prior range (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 2-3). These data demonstrate genetic and physiological constraint, but the ancestral ranges were broader than the target 5–10 °C class; they therefore support mechanism and context, not direct annotation of **METPO:1000484**.

## 3. Candidate graph nodes

### Trait and assay nodes

- **temperature delta low** — **METPO:1000484**
- Parent thermal-delta trait — **METPO:1000303**
- Minimum growth temperature — label-only candidate
- Maximum growth temperature — label-only candidate
- Optimum growth temperature — label-only candidate
- Sustained microbial growth — **GO:0016049** (*cell growth*), if compatible with the graph’s modeling convention
- Thermal-performance/cardinal-temperature assay — label-only candidate
- Incubation temperature — label-only environmental/experimental node

### Environmental and experimental factors

- Low-temperature exposure — label-only; use an ENVO term only after checking the exact environmental context
- High-temperature exposure — label-only
- Temperature downshift / cold shock — label-only
- Temperature upshift / heat shock — label-only
- Medium osmolarity — label-only
- Potassium availability — chemical entity **CHEBI:29103** (*potassium(1+)*) where ionic potassium is intended
- Oxygen availability — **CHEBI:15379** (*dioxygen*) where applicable
- Water activity, pH, incubation time, inoculum history — label-only assay covariates

### Cellular structures and processes

- Cytoplasmic membrane — **GO:0005886**
- Membrane lipid bilayer — label-only candidate
- Membrane fluidity / membrane viscosity — label-only candidate
- Membrane phase separation — label-only candidate
- Protein folding — **GO:0006457**
- Cellular response to heat — **GO:0034605**
- Response to cold — **GO:0009409**
- Potassium-ion homeostasis — **GO:0055075**
- Osmotic homeostasis / osmotic-stress response — use a GO term only after confirming the intended granularity
- DNA, rRNA, metabolic enzymes, cell wall — label-only damage targets unless a specific mechanism is supported

### Genes, proteins, and complexes

**Strong, taxon-specific membrane module:**

- DesK membrane histidine kinase/thermosensor — label-only; map to strain-specific UniProt record during implementation
- DesR response regulator — label-only; strain-specific UniProt mapping required
- *des* / Δ5-acyl-lipid desaturase — label-only; strain-specific UniProt and EC assignment should be verified
- DesK–DesR two-component system — label-only module

**Proteostasis candidates:**

- DnaK, DnaJ, GrpE
- GroEL/GroES
- HtpG
- ClpB and ClpX
- Small heat-shock proteins
- Cold-shock proteins CspL, CspP, CspC

All should receive organism-specific UniProt CURIEs only when the curated taxon/strain is known.

**c-di-AMP module:**

- *disA*, *cdaA*, *cdaS* — diadenylate cyclases
- *cdaR* — regulator associated with CdaA
- c-di-AMP — use a verified ChEBI identifier at implementation; no CURIE is asserted here
- Ktr/Kdp/KimA potassium-transport systems — label-only until taxon-specific complexes are selected

### Chemicals and metabolites

- Unsaturated fatty acids — **CHEBI:27283**
- Saturated fatty acids — label-only class pending exact ontology selection
- Anteiso-branched-chain fatty acids — label-only candidate
- Membrane phospholipids — **CHEBI:16247** (*phospholipid*) if the generic class is appropriate
- Glycine betaine — **CHEBI:17750**
- L-proline — **CHEBI:17203**
- Potassium(1+) — **CHEBI:29103**
- Cerulenin — label-only unless the ChEBI record is verified; it inhibits type-II fatty-acid synthesis and has been used experimentally to perturb DesK input.

### Taxon nodes

- *Bacillus subtilis* — **NCBITaxon:1423**
- *Bacillus cereus* — **NCBITaxon:1396**
- *Legionella pneumophila* — **NCBITaxon:446**
- Lactic-acid bacteria — use a specific NCBITaxon clade or species rather than an informal aggregate when curating edges

## 4. Candidate causal edges

| # | Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|---|
| 1 | Assay-derived Tmin and Tmax | **defines** | temperature delta, ΔT = Tmax−Tmin | Tmin is the point where “lag period or generation time becomes infinite”; high-temperature effects define Tmax (chandler2023theeffectof pages 31-35). | **Curate as definitional**, with complete assay context. The 5–10 °C threshold comes from the supplied METPO definition, not this paper. |
| 2 | Temperature decrease | **decreases** | membrane fluidity / increases membrane order | Cooling produces bilayer physical-state changes; lipid solidification can prevent metabolism below Tmin (mendoza2014temperaturesensingby pages 2-4, chandler2023theeffectof pages 31-35). | Broadly supported, but lipid composition and taxa alter the response. |
| 3 | Reduced membrane fluidity | **activates kinase activity of** | DesK | At constant 37 °C, manipulations that reduced anteiso-fatty acids and fluidity activated *des* through DesK/DesR, showing fluidity is the proximal signal (mansilla2004controlofmembrane pages 5-5, mendoza2014temperaturesensingby pages 5-6). | **Strong; curate with *B. subtilis* taxon restriction.** |
| 4 | DesK-P | **phosphorylates/activates** | DesR | DesK autophosphorylates at His-188 and transfers phosphate to DesR Asp-54 (mansilla2004controlofmembrane pages 5-5, mendoza2014temperaturesensingby pages 5-6). | **Strong biochemical edge; *B. subtilis*.** |
| 5 | Phosphorylated DesR | **activates transcription of** | *des* | DesR-P binds the *des* promoter and acts as its low-temperature transcriptional activator (mansilla2004controlofmembrane pages 5-5, mendoza2014temperaturesensingby pages 5-6). | **Strong; curate.** |
| 6 | Des Δ5-desaturase | **introduces cis double bonds into** | membrane phospholipid fatty-acyl chains | The desaturase converts existing fatty acids into Δ5/ω5-unsaturated forms (hunger2004geneticevidencefor pages 1-2, mendoza2014temperaturesensingby pages 5-6). | **Strong; curate**, but check exact reaction and Rhea/EC mapping before adding identifiers. |
| 7 | Increased unsaturated fatty acids | **increases/maintains** | membrane fluidity at low temperature | UFA accumulation lowers lipid transition temperature and preserves membrane fluidity—homoviscous adaptation (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 5-6). | **Strong general mechanism**, although lipid classes differ among taxa. |
| 8 | Maintained membrane fluidity | **supports** | low-temperature cellular function and growth | Appropriate viscosity/permeability supports membrane processes and minimizes energetic costs; rigidification can stop metabolism (mendoza2014temperaturesensingby pages 2-4, chandler2023theeffectof pages 31-35). | Curate as a broad process edge, not as proof of a 5–10 °C breadth. |
| 9 | Harsh cold-induced lipid phase separation | **impairs** | DesK membrane-thickness sensing | 2024 study: *des* was activated only by mild shocks; phase separation partitioned DesK into fluid domains and impaired sensing (sidarta2024lipidphaseseparation pages 1-2). | **Important negative/modifying edge; curate if graph permits inhibitors/context.** |
| 10 | High temperature | **causes damage to** | membrane, enzymes, rRNA, and DNA | High-temperature injury affects cell walls, membranes, metabolic enzymes, rRNA, and DNA as homeostasis fails (chandler2023theeffectof pages 31-35). | Supported but coarse; split into specific edges only with primary mechanistic evidence. |
| 11 | DnaK/DnaJ/GroEL/GroES/sHSP activity | **promotes** | protein folding/anti-aggregation under heat stress | LAB review identifies these chaperones in folding and repair; recent *Legionella* evolution implicates DnaK/DnaJ and other chaperones (sionek2024theimpactof pages 3-5, liang2024interactionsbetweenchaperone pages 8-10). | **Uncertain for thermal breadth**: stronger for stress survival than sustained growth. |
| 12 | Chaperone/proteostasis capacity | **supports** | high-temperature tolerance | *B. subtilis* was interpreted as having more efficient HSP/chaperone systems and greater plasticity than *B. cereus* (hurtadobautista2024thermalplasticityand pages 17-18). | Taxon-comparative interpretation; do not encode as a universal determinant of low ΔT. |
| 13 | c-di-AMP signaling | **regulates** | potassium transport/osmotic balance | Convergent DAC-pathway mutations and established c-di-AMP control of K+ transport connect the pathway to osmotic balance (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 15-16). | The K+-homeostasis edge is supported; its connection to temperature breadth is indirect. |
| 14 | Potassium/osmotic homeostasis | **may increase** | thermotolerance / upper growth limit | High osmolarity and K+-associated responses were linked to higher upper growth limits and lethal-heat survival (hurtadobautista2024thermalplasticityand pages 16-17). | **Uncertain and *Bacillus*-specific.** Requires reverse genetics and direct cardinal-temperature measurements. |
| 15 | *disA* or *cdaR* mutation | **may alter** | thermotolerance | Mutations converged in evolved *B. cereus* and *B. subtilis* lines (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 15-16). | **Do not curate as causal yet**: co-occurring mutations and absent functional validation. |
| 16 | Glycine betaine or proline accumulation | **may protect against** | heat-associated cellular damage | Compatible solutes were identified as heat protectants in the 2024 analysis (hurtadobautista2024thermalplasticityand pages 16-17). | Supportive but indirect; transport/synthesis and direct ΔT effects need species-specific evidence. |
| 17 | Limited membrane/proteostasis/osmotic adaptation capacity | **may constrain** | thermal niche breadth | Experimental evolution yielded at most ~4 °C niche extension and generally poor adaptation beyond ancestral ranges (hurtadobautista2024thermalplasticityand pages 1-2). | A useful high-level hypothesis, but too composite for an unqualified mechanistic edge. |

## 5. Recommended initial TraitMech graph

For an initial conservative graph, retain the phenotype plus a *B. subtilis*-anchored membrane module:

1. temperature downshift → decreased membrane fluidity;
2. decreased membrane fluidity → DesK kinase activation;
3. DesK-P → DesR phosphorylation;
4. DesR-P → activation of *des* transcription;
5. Des desaturase → increased membrane UFA content;
6. increased UFA content → increased membrane fluidity;
7. maintained membrane fluidity → supports growth at lower temperature;
8. Tmin/Tmax separation of 5–10 °C → **METPO:1000484**.

The last edge is an assay/classification relation, not a molecular mechanism. The graph should not imply that failure of the Des pathway is proven to cause every low-temperature-delta phenotype. A context or evidence qualifier should identify edges 2–6 as derived chiefly from **NCBITaxon:1423**.

The c-di-AMP/K+ and chaperone branches are best placed in a provisional section until mutation reconstruction or knockout/complementation experiments demonstrate altered Tmin, Tmax, and ΔT.

## 6. Applications and real-world relevance

- **Bioprocessing:** Temperature is normally controlled near Topt; strains with narrow ΔT require tighter reactor control and are more vulnerable to gradients or cooling failures. Thermal-response models can guide fermentation set points, but model choice and uncertainty must be documented.
- **Food fermentation and probiotics:** LAB viability depends on temperature, matrix, pH, and other combined stresses. Membrane-fat remodeling and HSP/CSP systems are practical targets for strain selection and process optimization, although typical LAB ranges reported in the 2024 review are much broader than 5–10 °C (sionek2024theimpactof pages 3-5).
- **Water-system pathogen control:** Heat-adapted *L. pneumophila* variants are relevant to hot-water pasteurization, but acute survival evolution must not be confused with expansion of the sustained-growth niche (liang2024interactionsbetweenchaperone pages 8-10, liang2024interactionsbetweenchaperone pages 16-17).
- **Climate-change forecasting:** Limited expansion in experimentally evolved *Bacillus* despite gradual warming suggests that some lineages may not track environmental warming rapidly; however, the result is lineage- and laboratory-specific and should not be generalized to all microbes (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 2-3).
- **Biosensors and antimicrobial research:** The DesK/DesR/*des* circuit has been explored as a reporter of membrane thickening. The 2024 failure under harsh stress is directly relevant to biosensor design and shows why in-vivo validation is necessary (sidarta2024lipidphaseseparation pages 1-2).

## 7. Warnings: claims not ready for TraitMech

1. **Do not equate “more unsaturated fatty acids” with low temperature delta.** UFA remodeling usually expands or preserves low-temperature function; limited remodeling could contribute to narrow breadth, but the supplied review does not directly show that UFA abundance causes a 5–10 °C phenotype (mendoza2014temperaturesensingby pages 2-4).
2. **Do not encode DesK/DesR as universal.** It is a well-resolved *B. subtilis* model, not a pan-microbial thermosensor.
3. **Do not assert that DesK failure causes narrow breadth.** The 2024 study questions the pathway’s contribution under harsh conditions but does not map that failure to measured Tmin/Tmax or ΔT (sidarta2024lipidphaseseparation pages 1-2).
4. **Do not use acute survival as evidence of sustained growth breadth.** This applies especially to *Legionella* chaperone-evolution results (liang2024interactionsbetweenchaperone pages 8-10).
5. **Do not yet curate *disA*/*cdaR* mutation → increased thermal breadth as causal.** The 2024 evidence is convergent but correlative (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 15-16).
6. **Do not infer organismal breadth from one enzyme’s activity range.** Growth requires coordinated membrane, translation, proteostasis, energetic, and regulatory function.
7. **Do not invent ontology identifiers.** DesK, DesR, Des, transporters, reactions, and c-di-AMP should receive strain-specific UniProt, EC, Rhea, or ChEBI mappings only after database verification.
8. **Do not curate the trait from incomplete temperature sampling.** A tested span of 5–10 °C is not necessarily an observed breadth of 5–10 °C.

## 8. DOI-first bibliography

1. **Hurtado-Bautista E, Islas-Robles A, Moreno-Hagelsieb G, Olmedo-Alvarez G.** “Thermal Plasticity and Evolutionary Constraints in *Bacillus*: Implications for Climate Change Adaptation.” *Biology* 13, 1088. **Published December 2024.** DOI: [10.3390/biology13121088](https://doi.org/10.3390/biology13121088). Main recent source for limited niche expansion, lineage differences, and candidate c-di-AMP mechanisms (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17).
2. **Sidarta M, et al.** “Lipid phase separation impairs membrane thickness sensing by the *Bacillus subtilis* sensor kinase DesK.” *Microbiology Spectrum* 12. **Published June 2024.** DOI: [10.1128/spectrum.03925-23](https://doi.org/10.1128/spectrum.03925-23). Key recent counterevidence concerning DesK under harsh stress (sidarta2024lipidphaseseparation pages 1-2).
3. **Liang J, Faucher S.** “Interactions between chaperone and energy storage networks during the evolution of *Legionella pneumophila* under heat shock.” *PeerJ* 12. **Published April 2024.** DOI: [10.7717/peerj.17197](https://doi.org/10.7717/peerj.17197). Acute heat-survival evolution and chaperone variants (liang2024interactionsbetweenchaperone pages 8-10, liang2024interactionsbetweenchaperone pages 16-17).
4. **Sionek B, Szydłowska A, Trząskowska M, Kołożyn-Krajewska D.** “The Impact of Physicochemical Conditions on Lactic Acid Bacteria Survival in Food Products.” *Fermentation* 10, 298. **Published June 2024.** DOI: [10.3390/fermentation10060298](https://doi.org/10.3390/fermentation10060298). Recent application-oriented review of membrane and stress-protein responses (sionek2024theimpactof pages 3-5).
5. **Kontopoulos D-G, et al.** “No universal mathematical model for thermal performance curves across traits and taxonomic groups.” *Nature Communications* 15. **Published October 2024.** DOI: [10.1038/s41467-024-53046-2](https://doi.org/10.1038/s41467-024-53046-2). Large comparison of thermal-performance models.
6. **Chandler RE.** “The effect of temperature and water activity on microbial growth rate and food spoilage.” University of Tasmania thesis. **Published January 2023.** DOI: [10.25959/23236217](https://doi.org/10.25959/23236217). Cardinal-temperature definitions and broad injury mechanisms (chandler2023theeffectof pages 31-35).
7. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68:101–116. **Published September 2014.** DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). Authoritative foundation for homoviscous adaptation and the Des pathway (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 5-6).
8. **Mansilla MC, Cybulski LE, Albanesi D, de Mendoza D.** “Control of Membrane Lipid Fluidity by Molecular Thermosensors.” *Journal of Bacteriology* 186:6681–6688. **Published October 2004.** DOI: [10.1128/JB.186.20.6681-6688.2004](https://doi.org/10.1128/JB.186.20.6681-6688.2004). DesK/DesR pathway and membrane-fluidity sensing (mansilla2004controlofmembrane pages 5-5).
9. **Hunger K, Beckering CL, Marahiel MA.** “Genetic evidence for the temperature-sensing ability of the membrane domain of the *Bacillus subtilis* histidine kinase DesK.” *FEMS Microbiology Letters* 230:41–46. **Published January 2004.** DOI: [10.1016/S0378-1097(03)00852-8](https://doi.org/10.1016/S0378-1097(03)00852-8). Genetic support for DesK→DesR→*des* (hunger2004geneticevidencefor pages 1-2).
10. **Porrini L, et al.** “Cerulenin inhibits unsaturated fatty acids synthesis in *Bacillus subtilis* by modifying the input signal of DesK thermosensor.” *MicrobiologyOpen* 3:213–224. **Published February 2014.** DOI: [10.1002/mbo3.154](https://doi.org/10.1002/mbo3.154). Experimental perturbation of fatty-acid synthesis and DesK signaling.

## Curation conclusion

The best-supported immediate addition to `temperature_delta_low.yaml` is a **taxon-qualified membrane-homeoviscosity subgraph**, combined with explicit assay nodes for Tmin, Tmax, and ΔT. The literature supports the molecular chain from membrane rigidification through DesK/DesR and Des-mediated fatty-acid desaturation, but it does **not** establish that this chain is a universal cause of a 5–10 °C growth breadth. Chaperone and c-di-AMP/K+ modules are valuable research candidates, yet should remain uncertain until experiments directly connect perturbations to cardinal growth temperatures and the resulting ΔT.

References

1. (chandler2023theeffectof pages 31-35): Robert Edward Chandler. The effect of temperature and water activity on microbial growth rate and food spoilage. Text, Jan 2023. URL: https://doi.org/10.25959/23236217, doi:10.25959/23236217. This article has 21 citations and is from a peer-reviewed journal.

2. (mansilla2004controlofmembrane pages 5-5): María C. Mansilla, Larisa E. Cybulski, Daniela Albanesi, and Diego de Mendoza. Control of membrane lipid fluidity by molecular thermosensors. Journal of Bacteriology, 186:6681-6688, Oct 2004. URL: https://doi.org/10.1128/jb.186.20.6681-6688.2004, doi:10.1128/jb.186.20.6681-6688.2004. This article has 406 citations and is from a peer-reviewed journal.

3. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 6 citations and is from a domain leading peer-reviewed journal.

4. (hunger2004geneticevidencefor pages 1-2): Karen Hunger, Carsten L Beckering, and Mohamed A Marahiel. Genetic evidence for the temperature-sensing ability of the membrane domain of the bacillus subtilis histidine kinase desk. FEMS microbiology letters, 230 1:41-6, Jan 2004. URL: https://doi.org/10.1016/s0378-1097(03)00852-8, doi:10.1016/s0378-1097(03)00852-8. This article has 39 citations and is from a peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

6. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

7. (sionek2024theimpactof pages 3-5): Barbara Sionek, Aleksandra Szydłowska, Monika Trząskowska, and Danuta Kołożyn-Krajewska. The impact of physicochemical conditions on lactic acid bacteria survival in food products. Fermentation, 10:298, Jun 2024. URL: https://doi.org/10.3390/fermentation10060298, doi:10.3390/fermentation10060298. This article has 139 citations.

8. (hurtadobautista2024thermalplasticityand pages 17-18): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

9. (liang2024interactionsbetweenchaperone pages 8-10): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

10. (liang2024interactionsbetweenchaperone pages 16-17): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

11. (hurtadobautista2024thermalplasticityand pages 16-17): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

12. (hurtadobautista2024thermalplasticityand pages 15-16): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

13. (hurtadobautista2024thermalplasticityand pages 2-3): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.

14. (hurtadobautista2024thermalplasticityand pages 1-2): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 8 citations.