---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:24:52.609925'
end_time: '2026-08-04T04:32:05.767175'
duration_seconds: 433.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid4
  trait_identifier: METPO:1000453
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid4
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 34\u201340 \xB0C, characteristic of warm-mesophilic\
    \ physiology (including many mammalian host-associated bacteria)."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_34_to_40
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 34\u201340 \xB0C range as the\
    \ warm-mesophile (mammalian-host) growth range.)"
  causal_graph_summary: 'temperature_range_mid4_warm_mesophile: 17 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid4
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000453
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 34–40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 34–40 °C range as the warm-mesophile (mammalian-host) growth range.)
- **Existing causal graph summary:** temperature_range_mid4_warm_mesophile: 17 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature range mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid4.yaml`.

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
- **Trait label:** temperature range mid4
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000453
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 34–40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 34–40 °C range as the warm-mesophile (mammalian-host) growth range.)
- **Existing causal graph summary:** temperature_range_mid4_warm_mesophile: 17 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature range mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid4.yaml`.

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


# Curation-focused research report: **temperature range mid4**

## 1. Trait scope

**Trait:** `temperature range mid4`  
**Identifier:** `METPO:1000453`  
**Parent:** `METPO:1000306`  
**Category:** environment  
**Definition supplied for curation:** growth-supporting ambient-temperature range spanning approximately **34–40 °C**, characteristic of warm-mesophilic physiology, including many mammalian host-associated bacteria.

This trait should represent an **assay-observed capacity for net microbial growth over a temperature interval**, not merely survival after temperature exposure. Ideally, assignment should be supported by growth curves, colony formation, biomass accumulation, or repeated-transfer data at temperatures spanning or substantially overlapping 34–40 °C. It does not imply that every temperature in that interval is optimal.

### Boundaries and exclusions

* **Optimum versus range:** A reported optimum of 37 or 40 °C alone does not prove a growth-supporting range of 34–40 °C. Cardinal-temperature data—minimum, optimum, and maximum—or measurements at multiple temperatures are preferable.
* **Heat-shock response:** Transient induction of chaperones after a thermal upshift is not itself this phenotype. Acute heat shock can occur inside or outside an organism’s normal growth range.
* **Thermotolerance/thermoduricity:** Survival at 40 °C or after brief exposure to substantially higher temperatures does not establish sustained growth.
* **Thermophily:** A recent experimental-evolution paper operationally defined thermophiles as organisms with growth optima above 45 °C and mesophiles as having optima of 25–45 °C. Accordingly, `METPO:1000453` is a narrow warm-mesophile range class, not a generic thermophile class. (lehmann2023adaptivelaboratoryevolution pages 6-7)
* **Host-temperature sensing:** A shift to approximately 37 °C can activate virulence programs in pathogens, but that regulatory response should only enter this graph where it demonstrably contributes to growth or fitness across the target range. (samtani2022microbialmechanismsof pages 1-3)

## 2. Current mechanistic interpretation

The most defensible general mechanism is **temperature-dependent maintenance of membrane physical state**. Cooling orders the lipid bilayer, whereas warming increases fluidity. Microbes alter lipid unsaturation, branching, chain length, cyclization, and lipid-class abundance to keep membrane properties within a functional window. This preserves transport, respiration, permeability barriers, and membrane-protein activity. The *Bacillus subtilis* DesK–DesR–Des pathway supplies unusually strong causal evidence because membrane composition can activate the pathway at a constant 37 °C; thus DesK senses membrane physical state rather than temperature as an isolated variable. (mendoza2014temperaturesensingby pages 5-6)

A second module is **proteostasis**. Thermal upshifts increase protein damage and misfolding, inducing chaperones and proteases. Nevertheless, most retrieved chaperone evidence concerns acute heat stress rather than constitutive warm-mesophile growth. It should therefore be treated as a supporting or boundary-protection module, not automatically as the core cause of `METPO:1000453`. (samtani2022microbialmechanismsof pages 1-3)

## 3. Candidate graph nodes

### Environmental and assay nodes

* `METPO:1000453` — temperature range mid4, quoted verbatim as requested.
* Ambient temperature, 34–40 °C — label-only range node unless the project has an established temperature-bin vocabulary.
* Temperature decrease / cold shift.
* Temperature increase / thermal upshift.
* Sustained microbial growth — candidate grounding: `GO:0016049` (cell growth), subject to ontology-policy review.
* Acute heat shock — candidate biological-process grounding: `GO:0009408` (response to heat).
* Growth medium composition, oxygen availability, pH, incubation duration, inoculum state, and growth endpoint — experimental covariates that can shift observed temperature boundaries.

### Cellular structures and physical-state nodes

* Cytoplasmic membrane — `GO:0005886`.
* Membrane fluidity / membrane order — label-only physical-state nodes; avoid conflating them with membrane organization.
* Proton-motive force — `GO:0015988` is a possible process-level grounding for proton-motive-force-driven ATP synthesis, but a label-only “proton motive force” node may be more exact.
* Protein folding — `GO:0006457`.
* Protein aggregation / misfolded-protein burden — use label-only unless the exact intended ontology class is verified.

### Lipids and metabolites

* Unsaturated fatty acids — `CHEBI:27283`.
* Saturated fatty acids — `CHEBI:26607`.
* Branched-chain fatty acids — label-only candidate.
* Anteiso-branched-chain fatty acids — label-only candidate.
* Ladderane fatty acids/lipids — label-only candidate; taxon-specific to anammox Planctomycetota.
* Plasmalogens — `CHEBI:17762`.
* Oleic acid — `CHEBI:16196`, if a source specifically demonstrates its role.

### Genes, proteins, and complexes

**Strong *B. subtilis* module**

* DesK — membrane histidine kinase/thermosensor; retain as label-only or ground to a reviewed strain-specific UniProt accession during organism-specific curation.
* DesR — response regulator; same grounding caution.
* `des` — cold-inducible acyl-lipid desaturase gene.
* Des acyl-lipid desaturase — molecular-function candidate `GO:0016717` is too broad unless project practice permits it; strain-specific protein grounding is preferable.
* DesK–DesR two-component system — label-only module.

**Proteostasis candidates**

* GroEL chaperonin — `GO:0005524` captures ATP binding but not identity; use reviewed UniProt accessions per organism or label-only family node.
* GroES, DnaK, ClpB, HtpG, GrpE, HtpX, and small heat-shock proteins — candidate nodes, but graph inclusion requires phenotype-relevant causal evidence rather than expression alone.
* RpoH/σ32 and SigH — taxon-specific heat/stress sigma factors; do not merge these as orthologous causal nodes without explicit organism-level modeling.

### Processes and pathways

* Homeoviscous adaptation.
* Two-component signal transduction — `GO:0000160`.
* Protein phosphorylation — `GO:0006468`.
* Fatty-acid desaturation.
* Unsaturated-fatty-acid biosynthesis.
* Membrane-lipid remodeling.
* Chaperone-mediated protein folding — `GO:0061077`.
* Proteolysis — `GO:0006508`.

## 4. Candidate causal edges

The table below separates direct or experimentally anchored causal links from recent correlations and taxon-specific observations.

| subject | predicate | object | evidence strength | taxon/temperature | DOI and publication date | short supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| decreased ambient temperature / cooling | increases membrane order sensed by | DesK sensor histidine kinase signaling state | direct experimental + review synthesis | *Bacillus subtilis*; cold shock 37°C → 20°C; also isothermal membrane-order manipulations at 37°C | 10.1146/annurev-micro-091313-103612 (Sep 2014) | “Cold shock (37°C to 20°C) induces unsaturated fatty acid (UFA) synthesis through des gene transcription… experiments manipulating branched-chain fatty acids show membrane fluidity—not temperature itself—directly controls des transcription via DesK” (mendoza2014temperaturesensingby pages 5-6) | Strong candidate edge for generic graph: model is membrane-state sensing rather than direct thermometry. Node grounding for DesK may remain label-only unless curated to a stable protein identifier. |
| increased membrane order / reduced fluidity | activates kinase activity of | DesK | direct experimental + review synthesis | *B. subtilis*; <30°C and isothermal fluidity perturbation | 10.1007/s12088-022-01009-w (Mar 2022); 10.1146/annurev-micro-091313-103612 (Sep 2014) | “DesK senses membrane physical state and acts as a kinase at low temperatures (<30°C) to phosphorylate DesR” (samtani2022microbialmechanismsof pages 1-3) | Good mechanistic edge; review-based wording but anchored to classic genetic/biochemical studies summarized in Mendoza review. |
| DesK | phosphorylates | DesR | direct experimental + review synthesis | *B. subtilis*; cold-sensing pathway | 10.1146/annurev-micro-091313-103612 (Sep 2014) | “DesK autophosphorylates and transfers phosphate to DesR, which in its phosphorylated form activates des transcription” (mendoza2014temperaturesensingby pages 5-6) | High-confidence causal step in the canonical DesK/DesR pathway. |
| phosphorylated DesR | activates transcription of | des gene | direct experimental + review synthesis | *B. subtilis*; cold-sensing pathway | 10.1146/annurev-micro-091313-103612 (Sep 2014) | “DesR, which in its phosphorylated form activates des transcription” (mendoza2014temperaturesensingby pages 5-6) | High-confidence edge; can be grounded to transcription regulation process (GO label-level if desired). |
| des gene product (acyl-lipid desaturase, Des) | increases biosynthesis of | unsaturated fatty acids | direct experimental + review synthesis | *B. subtilis*; cold-inducible pathway | 10.1046/j.1365-2958.2002.03103.x (Sep 2002); 10.1146/annurev-micro-091313-103612 (Sep 2014) | “Cold shock… induces unsaturated fatty acid (UFA) synthesis through des gene transcription” (mendoza2014temperaturesensingby pages 5-6) | Foundational mechanistic link; quote available from review summary rather than primary text excerpt. Suitable but note evidence snippet comes via review context. |
| increased unsaturated fatty acid content | restores / increases | membrane fluidity | direct experimental + review synthesis | bacteria broadly; *B. subtilis* exemplar | 10.1146/annurev-micro-091313-103612 (Sep 2014) | “Bacteria remodel the fluidity of their membrane bilayer precisely via the incorporation of proportionally more unsaturated fatty acids… optimizes the performance of a large array of cellular physiological processes” (mendoza2014temperaturesensingby pages 5-6) | Strong generic edge for warm-mesophile trait graph because membrane composition mediates temperature accommodation. |
| restored membrane fluidity | promotes phosphatase state / feedback shutoff of | DesK–DesR–des signaling | direct experimental + review synthesis | *B. subtilis*; isothermal feedback at 37°C | 10.1146/annurev-micro-091313-103612 (Sep 2014) | “Restoring membrane fluidity shuts off des transcription through DesK's phosphatase activity” (mendoza2014temperaturesensingby pages 5-6) | Important negative-feedback edge; highly useful for graph closure. |
| warm temperature / increased membrane fluidity | switches DesK to | phosphatase activity | review synthesis of direct studies | *B. subtilis*; high temperature relative to cold-induction threshold | 10.1007/s12088-022-01009-w (Mar 2022) | “at high temperatures, DesK switches to phosphatase activity, dephosphorylating DesR to terminate des gene transcription” (samtani2022microbialmechanismsof pages 1-3) | Appropriate reciprocal edge to cold-sensing pathway; use with note that citation is a review. |
| DesK phosphatase activity | dephosphorylates | DesR | review synthesis of direct studies | *B. subtilis*; warm state | 10.1007/s12088-022-01009-w (Mar 2022) | “DesK switches to phosphatase activity, dephosphorylating DesR” (samtani2022microbialmechanismsof pages 1-3) | High-confidence pathway step, but quoted from review. |
| dephosphorylated DesR | reduces activation of | des transcription | inferred from direct pathway + review synthesis | *B. subtilis*; warm state | 10.1007/s12088-022-01009-w (Mar 2022) | “dephosphorylating DesR to terminate des gene transcription” (samtani2022microbialmechanismsof pages 1-3) | Reasonable curation edge, but slightly inferred because the snippet states termination of transcription rather than explicit “DesR inactive.” |
| temperature increase 30°C → 40°C | associated with increased | ladderane lipid cyclization | correlative preprint | anammox enrichment (*Candidatus Brocadia*); 30°C → 40°C | 10.1101/2024.07.23.604647 (Jul 2024, preprint) | “The most notable adaptation mechanisms included… doubled ladderane cyclization…”; “C15 alkyl chains increased from 0.37 to 0.50 (p=0.008) and C16 decreased from 0.40 to 0.22 (p=0.002) at 40°C” (christina2024mechanismsofanammox pages 22-26) | Useful recent quantitative signal for 34–40°C adaptation, but keep marked uncertain/correlative until peer-reviewed. |
| increased ladderane cyclization | may maintain | membrane fluidity / proton motive force at high temperature | correlative preprint | anammox enrichment; 30°C → 40°C | 10.1101/2024.07.23.604647 (Jul 2024, preprint) | “increased cyclization of ladderane fatty acids at elevated temperature to maintain membrane fluidity and proton motive force” (christina2024mechanismsofanammox pages 22-26) | Mechanistically plausible and directly stated by authors, but still correlative and taxon-specific. |
| temperature increase 30°C → 40°C | associated with upregulation of | GroEL chaperonin | correlative preprint | anammox enrichment; 30°C → 40°C | 10.1101/2024.07.23.604647 (Jul 2024, preprint) | “Proteome response: upregulation of chaperonin GroEL at 40°C, with detection but non-upregulation of GroES, DnaK, ClpB, and HtpG” (christina2024mechanismsofanammox pages 22-26) | Recent 34–40°C-relevant proteostasis evidence; correlative only, but stronger than generic heat-shock claims because the temperature range overlaps the target trait. |
| growth at reduced temperature 45°C during ALE | associated with altered | fatty-acid composition and increased plasmalogens | correlative experimental evolution | *Thermoanaerobacter kivui*; cultivated at 45°C vs optimum 66°C | 10.3389/fmicb.2023.1265216 (Oct 2023) | “While the proportion of short-chain fatty acids increased at 50°C vs. 66°C in both strains, Adpt45_67 also showed a significantly increased proportion of plasmalogens” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Valuable as a recent lipid adaptation example, but it concerns thermophile → lower-temperature adaptation, not a direct warm-mesophile determinant. |
| adaptive laboratory evolution at 45°C | associated with | mutations in regulators / stress-related genes | correlative experimental evolution | *T. kivui*; 67 transfers (~180 generations) at 45°C | 10.3389/fmicb.2023.1265216 (Oct 2023) | “genomic sequencing revealing 67 SNPs… mutation P216L in fabG… G28V mutation in sigma factor SigH (5.7% of population)” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Do not curate as generic causal edge for METPO:1000453 yet; highly taxon-specific and associative. |
| high-temperature stress | causes | protein misfolding / damage requiring chaperone response | review synthesis | bacteria broadly | 10.1007/s12275-023-00031-x (Mar 2023); 10.1007/s12088-022-01009-w (Mar 2022) | “Upon the heat shock, diverse chaperones and proteases…” and temperature-controlled heat-shock genes help prevent aggregation from heat-induced misfolding (samtani2022microbialmechanismsof pages 1-3) | Acceptable high-level stress edge, but not specific to the 34–40°C growth trait; curate only as background unless linked to direct warm-mesophile fitness evidence. |
| heat stress | induces | chaperones/proteases (e.g., DnaK, GroEL, ClpB, Hsp families) | mixed: review + organism-specific studies | bacteria broadly; severe heat shock rather than routine 34–40°C growth | 10.1007/s12275-023-00031-x (Mar 2023); 10.1128/jb.00182-06 (Aug 2006) | “diverse chaperones and proteases”; organism-specific heat-shock regulons include “dnaK, grpE, clpB, groES, htpX, and hspA” (samtani2022microbialmechanismsof pages 1-3) | Keep as lower-priority background edges; evidence often concerns acute heat shock, not constitutive support for warm-mesophile temperature range. |
| thermophile / mesophile boundary concept | distinguishes | mesophily from thermophily by optimum temperature >45°C for thermophiles | review / definitional | general microbial temperature classes | 10.3389/fmicb.2023.1265216 (Oct 2023) | “thermophiles, i.e., organisms with growth temperature optima (TOPT) above 45°C” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Useful scope edge/note for ontology curation only; not a mechanistic causal edge. |


*Table: This table compiles compact, curation-ready causal edges and caveats for METPO:1000453 using only gathered evidence. It separates strong mechanistic DesK/DesR membrane-sensing links from recent but correlative 2023–2024 lipid/proteostasis studies relevant to the 34–40 °C range.*

### Recommended first-pass graph core

The highest-confidence chain for immediate curation is:

1. **decreased temperature → increases membrane order**;
2. **increased membrane order → activates DesK kinase state**;
3. **DesK → phosphorylates DesR**;
4. **phosphorylated DesR → activates `des` transcription**;
5. **Des desaturase → increases unsaturated-fatty-acid synthesis**;
6. **increased unsaturated-fatty-acid content → increases/restores membrane fluidity**;
7. **restored membrane fluidity → promotes DesK phosphatase state**;
8. **DesK phosphatase → dephosphorylates DesR**;
9. **dephosphorylated DesR → reduces `des` transcription**.

The decisive evidence is that reducing anteiso-branched fatty acids activated `des` at a constant 37 °C, while restoring fluidity shut the response down. This supports the causal interpretation **lipid composition → membrane state → DesK signaling**, rather than a simplistic direct edge from temperature to gene expression. (mendoza2014temperaturesensingby pages 5-6)

This module should be annotated **taxon-specific: *Bacillus subtilis***. It is a mechanistic exemplar of how a bacterium maintains function around warm-mesophilic temperatures, not evidence that every organism assigned `METPO:1000453` possesses DesK, DesR, or Des.

## 5. Recent developments, 2023–2024

### Anammox adaptation from 30 to 40 °C

A 2024 preprint gradually raised an anammox enrichment dominated by *Candidatus Brocadia* from 30 to 40 °C. The prominent reported responses were GroEL upregulation and increased ladderane-lipid cyclization. At 40 °C, the C15 alkyl-chain fraction increased from **0.37 to 0.50** (`p=0.008`), whereas C16 decreased from **0.40 to 0.22** (`p=0.002`). The NL3 and NL5 indices rose from 0.90 to 0.93 and from 0.69 to 0.72, respectively. GroES, DnaK, ClpB, and HtpG were detected but were not reported as upregulated. (christina2024mechanismsofanammox pages 22-26)

This is unusually relevant because the experiment reaches the upper boundary of `METPO:1000453`. However, it remains a **preprint**, the data are principally correlative, and ladderanes are specialized anammox lipids. Candidate edges should therefore be marked `uncertain`, `taxon_specific`, and `assay_specific` rather than merged into the universal graph core. (christina2024mechanismsofanammox pages 22-26)

### Experimental evolution toward lower-temperature growth

Lehmann and colleagues evolved the thermophile *Thermoanaerobacter kivui* at 45 °C for 67 transfers, approximately 180 generations. The ancestral organism had an optimum of 66 °C and a reported lower growth boundary of 39 °C under the study conditions. The evolved strain shifted its optimum to 60 °C but did not grow better at 45 °C. It accumulated **67 SNPs**, showed altered fatty-acid composition and increased plasmalogens, and contained candidate mutations including `fabG` P216L and a SigH G28V variant present in 5.7% of the population. (lehmann2023adaptivelaboratoryevolution pages 6-7)

This study demonstrates that temperature-range evolution can involve membrane lipids and regulatory changes, but it does not establish that any individual mutation caused the phenotype. These observations should inform candidate discovery, not be curated as generic gene-to-trait causal edges. (lehmann2023adaptivelaboratoryevolution pages 6-7)

### Contemporary expert synthesis

The 2023 review *Temperature Matters: Bacterial Response to Temperature Change* emphasizes coordinated regulation of membrane saturation, chaperones, proteases, transcription, and translation during thermal shifts. Its value is architectural: temperature adaptation is a systems phenotype, not a single-gene property. The review does not, by itself, establish that each listed response determines growth across 34–40 °C. (samtani2022microbialmechanismsof pages 1-3)

## 6. Current applications and implementations

* **Industrial bioprocess control:** Temperature-adaptation mechanisms guide reactor start-up and loading-rate management. In the 30-to-40 °C anammox study, successful adaptation required reducing the original loading rate to at least half—or preferably below half—of contemporaneous specific anammox activity. This is a concrete implementation relevant to high-temperature wastewater treatment, although it awaits peer-reviewed confirmation. (christina2024mechanismsofanammox pages 22-26)
* **Strain engineering:** Membrane-lipid pathways are potential engineering targets for broadening productive temperature windows. The *B. subtilis* system shows why interventions must account for sensor feedback: changing lipid composition can alter DesK signaling even without changing ambient temperature. (mendoza2014temperaturesensingby pages 5-6)
* **Adaptive laboratory evolution:** The *T. kivui* work demonstrates ALE as a practical route to shift cardinal temperatures, while also showing that hundreds of generations and many linked mutations may produce only modest movement of the optimum. (lehmann2023adaptivelaboratoryevolution pages 6-7)
* **Pathogen and host-association studies:** Approximately 37 °C can serve simultaneously as a permissive growth temperature and a host-entry signal. TraitMech should keep “supports growth” separate from “induces virulence,” even when both occur at the same temperature. (samtani2022microbialmechanismsof pages 1-3)

## 7. Curation warnings

1. **Do not encode the supplied existing statement “more unsaturated fatty acids” as a monotonic warm-temperature rule.** In homeoviscous adaptation, UFA abundance generally rises as growth temperature decreases. At the warm end, bacteria commonly reduce unsaturation or use alternative remodeling. The causal graph should represent a feedback-controlled membrane-fluidity window, not “higher temperature causes more UFA.” (mendoza2014temperaturesensingby pages 5-6, samtani2022microbialmechanismsof pages 1-3)
2. **Do not infer the full 34–40 °C range from a single 37 °C measurement or reported optimum.**
3. **Do not use heat-shock survival as equivalent evidence for growth.** Chaperone induction can be protective without shifting cardinal growth temperatures.
4. **Do not universalize DesK/DesR.** It is a strong *B. subtilis* exemplar, not a universal bacterial thermosensor.
5. **Do not curate GroEL expression as causal without perturbation evidence.** The anammox result is an association at 40 °C. (christina2024mechanismsofanammox pages 22-26)
6. **Do not universalize ladderane cyclization.** It is restricted to anammox biology and currently supported here by preprint evidence.
7. **Do not assign causality to the 67 ALE mutations.** Linkage, clonal interference, and population frequency prevent attribution to `fabG`, SigH, or any single regulator without reconstruction experiments. (lehmann2023adaptivelaboratoryevolution pages 6-7)
8. **Record assay context.** Medium, pH, oxygen, nutrient loading, pressure, incubation time, and endpoint can materially change observed temperature limits.
9. **Avoid unverified CURIEs.** Organism-specific genes and proteins should remain label-only until reviewed UniProt or genome-locus identifiers are selected for the exact strain.

## 8. DOI-first bibliography

1. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68:101–116. Published September 2014. DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). Foundational review of membrane-state sensing and the *B. subtilis* DesK–DesR pathway. (mendoza2014temperaturesensingby pages 5-6)
2. **Cybulski LE et al.** “Mechanism of membrane fluidity optimization: isothermal control of the *Bacillus subtilis* acyl-lipid desaturase.” *Molecular Microbiology* 45:1379–1388. Published September 2002. DOI: [10.1046/j.1365-2958.2002.03103.x](https://doi.org/10.1046/j.1365-2958.2002.03103.x). Primary foundation for isothermal control of the Des pathway, as summarized in the retrieved review evidence. (mendoza2014temperaturesensingby pages 5-6)
3. **Moon S et al.** “Temperature Matters: Bacterial Response to Temperature Change.” *Journal of Microbiology* 61:343–357. Published March 2023. DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). Recent systems-level review of bacterial thermal responses. (samtani2022microbialmechanismsof pages 1-3)
4. **Lehmann M et al.** “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14. Published October 2023. DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). Experimental evolution, lipid remodeling, and quantitative cardinal-temperature evidence. (lehmann2023adaptivelaboratoryevolution pages 6-7)
5. **Karmann C et al.** “Mechanisms of Anammox Adaptation to High Temperatures: Increased Cyclization of Ladderane Lipids and Proteomic Insights.” *bioRxiv*. Posted July 2024. DOI: [10.1101/2024.07.23.604647](https://doi.org/10.1101/2024.07.23.604647). Preprint reporting 30-to-40 °C adaptation, quantitative lipid changes, and GroEL upregulation. (christina2024mechanismsofanammox pages 22-26)
6. **Samtani H, Unni G, Khurana P.** “Microbial Mechanisms of Heat Sensing.” *Indian Journal of Microbiology* 62:175–186. Published March 2022. DOI: [10.1007/s12088-022-01009-w](https://doi.org/10.1007/s12088-022-01009-w). Review of DesK/DesR, lipid thermosensing, and heat-controlled responses. (samtani2022microbialmechanismsof pages 1-3)

## 9. Recommended curation decision

For the next revision of `data/traits/environment/temperature_range_mid4.yaml`, curate the **membrane-order → DesK/DesR → desaturase → UFA → membrane-fluidity feedback loop** as a taxon-specific, strongly supported mechanistic exemplar. Add the anammox ladderane and GroEL observations only as uncertain, taxon-specific 2024 evidence. Keep generic chaperone/protease and ALE mutation edges provisional until direct loss-of-function, complementation, lipid-supplementation, or reconstructed-mutation studies show altered growth boundaries specifically within approximately 34–40 °C.

References

1. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (samtani2022microbialmechanismsof pages 1-3): Harsha Samtani, Gopika Unni, and Paramjit Khurana. Microbial mechanisms of heat sensing. Indian Journal of Microbiology, 62:175-186, Mar 2022. URL: https://doi.org/10.1007/s12088-022-01009-w, doi:10.1007/s12088-022-01009-w. This article has 23 citations and is from a peer-reviewed journal.

3. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

4. (christina2024mechanismsofanammox pages 22-26): Karmann Christina, Navrátilová Klára, Behner Adam, Noor Tayyaba, Danner Stella, Majchrzak Anastasia, Šantrůček Jiří, Podzimek Tomáš, Marin Lopez Marco A., Hajšlová Jana, Lipovová Petra, Bartáček Jan, and Kouba Vojtěch. Mechanisms of anammox adaptation to high temperatures: increased cyclization of ladderane lipids and proteomic insights. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.23.604647, doi:10.1101/2024.07.23.604647. This article has 1 citations.