---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:30:37.003844'
end_time: '2026-06-18T11:46:23.971861'
duration_seconds: 946.97
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: lithoautotrophic
  trait_identifier: METPO:1000647
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: lithoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from inorganic electron
    donors and carbon from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: lithoautotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules
    (Review supports inorganic compounds as reductants for lithotrophic growth.) |
    DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation
    as the autotrophic carbon-assimilation process.)'
  causal_graph_summary: 'lithoautotrophic_inorganic_donor_co2_fixation: 7 nodes, 6
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoautotrophic
- **METPO identifier:** METPO:1000647
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from inorganic electron donors and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoautotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules (Review supports inorganic compounds as reductants for lithotrophic growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** lithoautotrophic_inorganic_donor_co2_fixation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **lithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoautotrophic.yaml`.

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
- **Trait label:** lithoautotrophic
- **METPO identifier:** METPO:1000647
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from inorganic electron donors and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoautotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules (Review supports inorganic compounds as reductants for lithotrophic growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** lithoautotrophic_inorganic_donor_co2_fixation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **lithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoautotrophic.yaml`.

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


## Curation-Focused Research Report: **Lithoautotrophic** (METPO:1000647)

### 0) Executive scope summary
The microbial trait **lithoautotrophic** (METPO:1000647) denotes a trophic physiology in which organisms **obtain energy from oxidation of inorganic electron donors** (lithotrophy) while assimilating carbon primarily from **CO2/dissolved inorganic carbon (DIC)** via one of several **autotrophic carbon fixation pathways** (e.g., Calvin–Benson–Bassham (CBB), reverse TCA (rTCA), Wood–Ljungdahl (WL)). Mechanistically, lithoautotrophy requires (i) electron donor oxidation systems, (ii) electron transport and energy conservation (ETC → proton motive force → ATP), and (iii) reductant generation (often including **reverse electron flow**) to supply reducing power for CO2 fixation. Evidence from recent work also emphasizes boundary cases: some organisms oxidize inorganic donors (e.g., reduced sulfur) yet **lack canonical CO2-fixation genes**, making them **lithoheterotrophs/chemolithoheterotrophs** rather than lithoautotrophs. (jahn2024theenergymetabolism pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2, seah2019sulfuroxidizingsymbiontswithout pages 2-4)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Definition aligned to METPO scope
A practical curation definition consistent with METPO:1000647 is:
- **Energy source**: inorganic electron donor(s) (e.g., H2, reduced sulfur compounds, Fe(II), formate in some taxa)
- **Carbon source**: CO2 / DIC
- **Physiological requirement**: coupling of donor oxidation to ATP generation and reductant provision for CO2 fixation.

A clear recent model statement comes from *Cupriavidus necator* physiology: “C. necator can use hydrogen or formic acid as an energy source, fixes CO2 via the Calvin-Benson-Bassham (CBB) cycle” (peer-reviewed 2024). (jahn2024theenergymetabolism pages 1-2)

### 1.2 Boundary cases and distinctions
**Lithoautotrophy vs lithoheterotrophy (chemolithoheterotrophy).** A direct boundary-case definition is provided in a symbiosis study: Kentron shows “a lithoheterotrophic metabolism, in which energy is produced by oxidation of reduced sulfur and carbon is assimilated in the form of organic compounds,” and critically lacks “genes for… RuBisCO and other key enzymes in the six canonical autotrophic CO2 fixation pathways.” (seah2019sulfuroxidizingsymbiontswithout pages 2-4)

**Mixotrophy warning.** Many organisms can combine inorganic electron donors with organic carbon uptake; such cases should not be curated as obligate lithoautotrophy unless CO2 fixation is demonstrated and sufficiently supports growth. The Kentron example shows sulfur oxidation capacity does not guarantee lithoautotrophy. (seah2019sulfuroxidizingsymbiontswithout pages 2-4)

---

## 2) Trait scope for TraitMech curation

### What the trait represents
For TraitMech, lithoautotrophic is best treated as a **physiological capacity**: the ability to grow (or maintain biomass production) using inorganic electron donors while using CO2/DIC as the predominant carbon source. Evidence can come from:
- growth on H2/CO2 (knallgas growth), reduced sulfur/CO2, Fe(II)/CO2, etc.
- presence + expression/fitness-essentiality of (a) electron donor oxidation systems, (b) carbon fixation pathways, and (c) energy conservation components.

### Suggested inclusion/exclusion boundaries
**Include**: organisms and conditions where CO2 fixation pathway genes are present and functionally linked to donor oxidation and energy conservation (e.g., H2 oxidation fueling CBB). (jahn2024theenergymetabolism pages 1-2)

**Exclude / flag**: cases with lithotrophic sulfur oxidation but absent canonical CO2 fixation genes (lithoheterotrophy). (seah2019sulfuroxidizingsymbiontswithout pages 2-4)

**Assay dependence**: electroautotrophy/EEU cases depend on electrode potential and set-ups; curate as conditional subgraph if included. (gupta2020extracellularelectronuptake pages 4-5)

---

## 3) Candidate causal-graph nodes (grounded where possible)
The following curation-ready node list includes chemicals, pathways, modules, and environmental factors.

| Node type | Candidate node label | Suggested identifier(s) | Notes for curation | Evidence citation |
|---|---|---|---|---|
| Trait | lithoautotrophic | METPO:1000647 | Defined by energy from inorganic electron donors and carbon from CO2; curate as a class-level physiology trait | (jahn2024theenergymetabolism pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2) |
| Trait | lithoheterotrophy / chemolithoheterotrophy |  | Boundary-case comparator: inorganic donor oxidation with organic carbon assimilation, not lithoautotrophy | (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| Electron donors | hydrogen | CHEBI:18276 | Canonical inorganic electron donor for many lithoautotrophs | (jahn2024theenergymetabolism pages 1-2, prioretti2023carbonfixationin pages 1-2) |
| Electron donors | formic acid / formate | CHEBI:30751 / CHEBI:15740 | Used by some lithoautotrophs such as Cupriavidus necator; taxon-specific | (jahn2024theenergymetabolism pages 1-2) |
| Electron donors | thiosulfate | CHEBI:9567 | Major reduced sulfur donor in sulfur-oxidizing lithoautotrophs | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2) |
| Electron donors | sulfide | CHEBI:16189 | Common reduced sulfur donor; often coupled to O2 or nitrate reduction | (gupta2020extracellularelectronuptake pages 8-9, whaleymartin2023o2partitioningof pages 1-2) |
| Electron donors | elemental sulfur | CHEBI:26806 | Common sulfur donor or disproportionation substrate; may be intracellularly stored in some taxa | (seah2019sulfuroxidizingsymbiontswithout pages 2-4, nosalova2023coldsulfursprings—neglected pages 11-12) |
| Electron donors | Fe(II) | CHEBI:29033 | Common donor in iron-oxidizing lithoautotrophs; also relevant to EEU-linked lithotrophy | (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 4-5) |
| Electron donors | insoluble reduced iron minerals / electrodes |  | Useful generalized donor node for extracellular electron uptake cases; likely uncertain for core trait graph | (gupta2020extracellularelectronuptake pages 5-6, gupta2020extracellularelectronuptake pages 1-2) |
| Electron donors | carbon monoxide | CHEBI:17245 | Inorganic donor in some taxa; often taxon-specific and may overlap with carboxydotrophy | (seah2019sulfuroxidizingsymbiontswithout pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2) |
| Electron acceptors | oxygen | CHEBI:15379 | Frequent terminal electron acceptor in aerobic lithoautotrophy | (jahn2024theenergymetabolism pages 1-2, whaleymartin2023o2partitioningof pages 1-2) |
| Electron acceptors | nitrate | CHEBI:17632 | Important alternative acceptor in sulfur oxidation and some H2/formate oxidizers | (jahn2024theenergymetabolism pages 1-2, whaleymartin2023o2partitioningof pages 1-2) |
| Carbon sources / DIC species | carbon dioxide | CHEBI:16526 | Primary carbon source defining autotrophy | (jahn2024theenergymetabolism pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon sources / DIC species | bicarbonate | CHEBI:17544 | Important dissolved inorganic carbon species, especially near neutral pH | (scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon sources / DIC species | dissolved inorganic carbon |  | Useful umbrella node connecting transport, carbonic anhydrase, and fixation pathway demand | (scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon fixation pathways | Calvin-Benson-Bassham cycle | GO:0015977 | Major CO2 fixation pathway in many bacterial lithoautotrophs | (jahn2024theenergymetabolism pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon fixation pathways | reverse tricarboxylic acid cycle |  | Key pathway in Aquifex and other lithoautotrophs; GO term not confidently assigned here | (prioretti2023carbonfixationin pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon fixation pathways | Wood-Ljungdahl pathway |  | Also called reductive acetyl-CoA pathway; important in anaerobic autotrophs | (gupta2020extracellularelectronuptake pages 5-6, scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon fixation pathways | reductive glycine pathway |  | Mentioned in 2024 DIC toolkit survey; not core enough for all taxa | (scott2024widespreaddissolvedinorganic pages 1-2) |
| Carbon fixation pathways | 3-hydroxypropionate bicycle / related autotrophic pathways |  | Present in some autotrophs; more peripheral for a minimal core graph | (seah2019sulfuroxidizingsymbiontswithout pages 16-16, scott2024widespreaddissolvedinorganic pages 1-2) |
| Energy conservation components | electron transport chain | GO:0022900 | General causal intermediate between donor oxidation and ATP/reductant generation | (seah2019sulfuroxidizingsymbiontswithout pages 2-4, jahn2024theenergymetabolism pages 1-2) |
| Energy conservation components | proton motive force | GO:0015986 | Generated by respiratory electron transport; supports ATP synthesis | (gupta2020extracellularelectronuptake pages 8-9, jahn2024theenergymetabolism pages 1-2) |
| Energy conservation components | ATP synthase | EC:7.1.2.2 | Core ATP-generating complex downstream of PMF | (gupta2020extracellularelectronuptake pages 5-6, seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| Energy conservation components | reverse electron flow |  | Important mechanistic node linking donor oxidation to NAD(H) production for biosynthesis | (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 4-5) |
| Energy conservation components | quinone pool |  | Useful intermediate node for membrane-bound donor oxidation feeding respiration | (jahn2024theenergymetabolism pages 1-2, gupta2020extracellularelectronuptake pages 4-5) |
| Key enzymes / complexes / genes | hydrogenase (uptake / soluble / membrane-bound) | EC:1.12.5.1 / EC:1.12.1.2 | Central H2 oxidation machinery; exact subtype depends on taxon | (jahn2024theenergymetabolism pages 1-2) |
| Key enzymes / complexes / genes | formate dehydrogenase | EC:1.17.1.9 | Central formate oxidation enzyme in formate-based lithoautotrophy | (jahn2024theenergymetabolism pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2) |
| Key enzymes / complexes / genes | RuBisCO | EC:4.1.1.39 | Hallmark carboxylase of CBB cycle | (scott2024widespreaddissolvedinorganic pages 1-2) |
| Key enzymes / complexes / genes | carbonic anhydrase | EC:4.2.1.1 | DIC-modifying enzyme connecting environmental DIC to fixation demand | (scott2024widespreaddissolvedinorganic pages 1-2) |
| Key enzymes / complexes / genes | DIC transporter(s) |  | Candidate transport node for bicarbonate/CO2 acquisition | (scott2024widespreaddissolvedinorganic pages 1-2) |
| Key enzymes / complexes / genes | Sox system (SoxXYZABCD) |  | Central sulfur oxidation machinery in many sulfur-oxidizing lithoautotrophs | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2, nosalova2023coldsulfursprings—neglected pages 11-12) |
| Key enzymes / complexes / genes | reverse Dsr pathway (rDsr; dsrABCEFH and associated components) |  | Important sulfur oxidation module, especially in lower-O2 settings | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2) |
| Key enzymes / complexes / genes | TsdA thiosulfate dehydrogenase |  | Connects thiosulfate to tetrathionate branch (S4I pathway) | (whaleymartin2023o2partitioningof pages 1-2, nosalova2023coldsulfursprings—neglected pages 11-12) |
| Key enzymes / complexes / genes | TetH tetrathionate hydrolase |  | Important tetrathionate-processing enzyme in some sulfur oxidizers | (whaleymartin2023o2partitioningof pages 1-2, nosalova2023coldsulfursprings—neglected pages 11-12) |
| Key enzymes / complexes / genes | pyruvate:ferredoxin oxidoreductase (PFOR) | EC:1.2.7.1 | Key reductive carboxylation enzyme in rTCA-linked lithoautotrophy | (prioretti2023carbonfixationin pages 1-2) |
| Key enzymes / complexes / genes | 2-oxoglutarate:ferredoxin oxidoreductase (OGOR) | EC:1.2.7.3 | Key reductive carboxylation enzyme in rTCA-linked lithoautotrophy | (prioretti2023carbonfixationin pages 1-2) |
| Key enzymes / complexes / genes | low-potential ferredoxin |  | Electron donor to PFOR/OGOR in rTCA carbon fixation | (prioretti2023carbonfixationin pages 1-2) |
| Key enzymes / complexes / genes | cytochrome bc1 complex |  | Important for reverse electron flow and respiratory coupling | (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 4-5) |
| Key enzymes / complexes / genes | cbb3-type cytochrome c oxidase |  | Microaerobic terminal oxidase relevant in some sulfur oxidizers | (seah2019sulfuroxidizingsymbiontswithout pages 2-4, gupta2020extracellularelectronuptake pages 4-5) |
| Key enzymes / complexes / genes | nitrate reductase | EC:1.7.5.1 / EC:1.7.99.4 | Candidate terminal reductase for nitrate-respiring lithoautotrophs | (gupta2020extracellularelectronuptake pages 4-5, whaleymartin2023o2partitioningof pages 1-2) |
| Environmental / assay factors | low oxygen / microoxic conditions | ENVO:01001023 | Strong selector for many sulfur- and hydrogen-oxidizing lithoautotrophs | (seah2019sulfuroxidizingsymbiontswithout pages 2-4, whaleymartin2023o2partitioningof pages 3-5) |
| Environmental / assay factors | anoxic conditions | ENVO:01001026 | Relevant for nitrate-coupled sulfur oxidation and WL-pathway autotrophy | (whaleymartin2023o2partitioningof pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2) |
| Environmental / assay factors | oxic conditions |  | Relevant for O2-coupled sulfur and hydrogen oxidation | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2) |
| Environmental / assay factors | low pH |  | Shifts DIC speciation toward CO2 and can shape sulfur oxidation strategy | (whaleymartin2023o2partitioningof pages 3-5, scott2024widespreaddissolvedinorganic pages 1-2) |
| Environmental / assay factors | circumneutral pH |  | Favors bicarbonate prevalence and distinct sulfur oxidation modules | (whaleymartin2023o2partitioningof pages 3-5, scott2024widespreaddissolvedinorganic pages 1-2) |
| Environmental / assay factors | thiosulfate availability |  | Important ecological determinant of sulfur oxidation pathways | (whaleymartin2023o2partitioningof pages 3-5) |
| Environmental / assay factors | hydrogen availability |  | Key determinant for hydrogenotrophic lithoautotrophy | (jahn2024theenergymetabolism pages 1-2, prioretti2023carbonfixationin pages 1-2) |
| Environmental / assay factors | hydrothermal vent environment | ENVO:01000084 | Canonical habitat for sulfur- and hydrogen-based lithoautotrophs | (prioretti2023carbonfixationin pages 1-2) |
| Environmental / assay factors | mine tailings / mining waters | ENVO:00002008 | Important applied habitat for sulfur-oxidizing lithoautotrophs | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2) |
| Example taxa | Cupriavidus necator | NCBITaxon:106590 | Model hydrogen/formate-oxidizing lithoautotroph using CBB cycle | (jahn2024theenergymetabolism pages 1-2) |
| Example taxa | Aquifex aeolicus | NCBITaxon:224324 | Hydrogen- and sulfur-oxidizing lithoautotroph using rTCA cycle | (prioretti2023carbonfixationin pages 1-2) |
| Example taxa | Halothiobacillus | NCBITaxon:927 | Sulfur-oxidizing chemolithoautotroph associated with complete Sox and acidity generation | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2) |
| Example taxa | Thiobacillus | NCBITaxon:943 | Sulfur-oxidizing chemolithoautotroph associated with incomplete Sox + rDsr and nitrate coupling | (whaleymartin2023o2partitioningof pages 3-5, whaleymartin2023o2partitioningof pages 1-2) |
| Example taxa | Sulfurimonas | NCBITaxon:179488 | Major Campylobacterota sulfur-based chemolithoautotroph in vents; also disproportionation-capable | (seah2019sulfuroxidizingsymbiontswithout pages 16-16) |
| Example taxa | Sulfurovum | NCBITaxon:228657 | Major Campylobacterota sulfur-based chemolithoautotroph in vents; also disproportionation-capable | (seah2019sulfuroxidizingsymbiontswithout pages 16-16) |


*Table: This table lists candidate nodes for a lithoautotrophic TraitMech graph, grouped by biological role and annotated with suggested identifiers where they are clear and stable. It is designed to help curators choose core, broadly reusable entities while keeping taxon-specific or uncertain nodes visible but clearly marked.*

---

## 4) Evidence-backed causal edges (triples) for lithoautotrophic TraitMech
The table below provides candidate edges with supporting snippets and curation notes.

| Subject node | Predicate | Object node | Evidence snippet | Reference | Notes |
|---|---|---|---|---|---|
| H2 oxidation | generates | ATP and reduction equivalents for CO2 fixation by CBB cycle | “To fuel CO2 fixation by the Calvin-Benson-Bassham (CBB) cycle, C. necator generates ATP and reduction equivalents from the oxidation of molecular hydrogen” | Jahn et al., 2024, DOI:10.1128/aem.00748-24, https://doi.org/10.1128/aem.00748-24 | Strong, direct, taxon-specific to *Cupriavidus necator* but broadly representative of hydrogenotrophic lithoautotrophy. (jahn2024theenergymetabolism pages 1-2) |
| formic acid oxidation | generates | ATP and reduction equivalents for CO2 fixation by CBB cycle | “To fuel CO2 fixation by the Calvin-Benson-Bassham (CBB) cycle, C. necator generates ATP and reduction equivalents from the oxidation of… formic acid” | Jahn et al., 2024, DOI:10.1128/aem.00748-24, https://doi.org/10.1128/aem.00748-24 | Strong, but formate-based lithoautotrophy is taxon-specific and should be curated as optional, not universal. (jahn2024theenergymetabolism pages 1-2) |
| membrane-bound hydrogenases / dehydrogenases | drives | electron transport chain | “Membrane-bound (de-)hydrogenases couple the oxidation reaction to the reduction of a universal quinone e− carrier which in turn drives the electron transport chain (ETC)” | Jahn et al., 2024, DOI:10.1128/aem.00748-24, https://doi.org/10.1128/aem.00748-24 | Strong mechanistic edge for donor oxidation → ETC. (jahn2024theenergymetabolism pages 1-2) |
| electron transport chain | builds | proton motive force | “drives the electron transport chain (ETC) to build up a proton motive force” | Jahn et al., 2024, DOI:10.1128/aem.00748-24, https://doi.org/10.1128/aem.00748-24 | Strong mechanistic edge. (jahn2024theenergymetabolism pages 1-2) |
| cyclic photosynthesis / cytochrome bc1 | generates | proton motive force | “electrons flow cyclically from the reaction center to the ubiquinone pool to re-oxidize cytochrome bc1. This process generates a proton motive force” | Gupta et al., 2020, DOI:10.1007/s10295-020-02309-0, https://doi.org/10.1007/s10295-020-02309-0 | Phototrophic EEU case; relevant to lithoautotrophy broadly but not specific to chemolithoautotrophy. (gupta2020extracellularelectronuptake pages 8-9) |
| proton motive force | drives | ATP synthesis | “This process generates a proton motive force to drive ATP synthesis via cyclic photophosphorylation” | Gupta et al., 2020, DOI:10.1007/s10295-020-02309-0, https://doi.org/10.1007/s10295-020-02309-0 | Strong ATP-coupling edge; phototrophic context. (gupta2020extracellularelectronuptake pages 8-9) |
| reverse electron flow | generates | NAD(H) for carbon fixation | “an uphill (endergonic) pathway to generate NAD(H) through reverse electron flow” | Gupta et al., 2020, DOI:10.1007/s10295-020-02309-0, https://doi.org/10.1007/s10295-020-02309-0 | Strong mechanistic edge in Fe-oxidizing chemolithoautotroph review figure text. (gupta2020extracellularelectronuptake pages 4-5) |
| rusticyanin branch point | balances generation of | ATP and NAD(H) required for CBB cycle | “Rusticyanin represents a ‘branch point’ that balances ATP and NAD(H) generation… required for carbon fixation via the Calvin–Benson–Bassham (CBB) cycle” | Gupta et al., 2020, DOI:10.1007/s10295-020-02309-0, https://doi.org/10.1007/s10295-020-02309-0 | Strong, but specific to iron-oxidizing chemolithoautotroph models. (gupta2020extracellularelectronuptake pages 4-5) |
| cytochrome bc1 and NADH dehydrogenase | mediates | reverse electron transfer to reduce NAD+ to NAD(H) | “This is likely mediated by cytochrome bc1 and NADH dehydrogenase which transfer electrons from the ubiquinone pool to reduce NAD+ to NAD(H)” | Gupta et al., 2020, DOI:10.1007/s10295-020-02309-0, https://doi.org/10.1007/s10295-020-02309-0 | Strong mechanistic edge for reverse electron flow. (gupta2020extracellularelectronuptake pages 8-9) |
| CBB cycle | fixes | CO2 during lithoautotrophic growth | “C. necator can use hydrogen or formic acid as an energy source, fixes CO2 via the Calvin-Benson-Bassham (CBB) cycle” | Jahn et al., 2024, DOI:10.1128/aem.00748-24, https://doi.org/10.1128/aem.00748-24 | Strong direct pathway edge. (jahn2024theenergymetabolism pages 1-2) |
| rTCA cycle | assimilates | CO2 in *Aquifex aeolicus* | “Aquifex aeolicus is a microaerophilic hydrogen- and sulfur-oxidizing bacterium that assimilates CO2 via the reverse tricarboxylic acid cycle (rTCA)” | Prioretti et al., 2023, DOI:10.3390/life13030627, https://doi.org/10.3390/life13030627 | Strong direct pathway edge; taxon-specific. (prioretti2023carbonfixationin pages 1-2) |
| low-potential ferredoxins Fd6/Fd7 | donates electrons to | PFOR and OGOR | “Fd6 and Fd7… can physically interact and exchange electrons with both PFOR and OGOR” | Prioretti et al., 2023, DOI:10.3390/life13030627, https://doi.org/10.3390/life13030627 | Strong mechanistic support for reductive carboxylation in rTCA. (prioretti2023carbonfixationin pages 1-2) |
| PFOR and OGOR | catalyzes | reductive carboxylation in rTCA cycle | “PFOR and 2-oxoglutarate:ferredoxin oxidoreductase (OGOR)… are responsible, respectively, for the reductive carboxylation of acetyl-CoA to pyruvate and of succinyl-CoA to 2-oxoglutarate” | Prioretti et al., 2023, DOI:10.3390/life13030627, https://doi.org/10.3390/life13030627 | Strong direct pathway edge. (prioretti2023carbonfixationin pages 1-2) |
| Wood–Ljungdahl pathway | is a known | autotrophic DIC fixation pathway | “there are the reductive citric acid cycle (rTCA), Wood-Ljungdahl pathway (WL)” | Scott et al., 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23 | Strong for pathway-class grounding, but not a direct growth assay edge. (scott2024widespreaddissolvedinorganic pages 1-2) |
| carbonic anhydrase enzymes and DIC transporters | facilitates | DIC fixation | “Autotrophs using the Calvin-Benson-Bassham cycle (CBB) are known to make use of a toolkit comprised of DIC transporters and carbonic anhydrase enzymes (CA) to facilitate DIC fixation” | Scott et al., 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23 | Strong DIC-toolkit edge; broad across autotrophs. (scott2024widespreaddissolvedinorganic pages 1-2) |
| low pH | shifts dominance toward | CO2 form of DIC | “The composition of DIC is sensitive to pH; CO2 dominates at low pH, HCO3− at circumneutral pH” | Scott et al., 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23 | Useful environmental-factor edge for DIC availability. (scott2024widespreaddissolvedinorganic pages 1-2) |
| circumneutral pH | shifts dominance toward | HCO3− form of DIC | “CO2 dominates at low pH, HCO3− at circumneutral pH” | Scott et al., 2024, DOI:10.1128/aem.01557-23, https://doi.org/10.1128/aem.01557-23 | Useful environmental-factor edge. (scott2024widespreaddissolvedinorganic pages 1-2) |
| complete Sox pathway + O2 | drives | lower pH and lower thiosulfate | “Under oxic conditions, novel Halothiobacillus drive lower pH conditions (as low as 4.3) and lower [S2O32−] via the complete Sox pathway coupled to O2” | Whaley-Martin et al., 2023, DOI:10.1038/s41467-023-37426-8, https://doi.org/10.1038/s41467-023-37426-8 | Strong sulfur-pathway-to-geochemistry edge; mining-water specific. (whaleymartin2023o2partitioningof pages 1-2) |
| incomplete Sox + rDSR + NO3− | results in | higher thiosulfate and no net significant acidity generation | “via the incomplete Sox and rDSR pathways coupled to NO3−, resulting in higher [S2O32−] and no net significant acidity generation” | Whaley-Martin et al., 2023, DOI:10.1038/s41467-023-37426-8, https://doi.org/10.1038/s41467-023-37426-8 | Strong sulfur-pathway-to-geochemistry edge; anoxic niche-specific. (whaleymartin2023o2partitioningof pages 1-2) |
| tsdA | catalyzes | S2O32− to S4O62− | “The S4I pathway part 1 (tsdA; S2O32− to S4O62−)” | Twible et al., 2024, DOI:10.3389/fmicb.2024.1426584, https://doi.org/10.3389/fmicb.2024.1426584 | Strong enzyme-level edge. (twible2024phandthiosulfate pages 1-2) |
| tetH | mediates | S4O62− disproportionation | “S4I pathway part 2 (S4O62− disproportionation via tetH)” | Twible et al., 2024, DOI:10.3389/fmicb.2024.1426584, https://doi.org/10.3389/fmicb.2024.1426584 | Strong enzyme-level edge. (twible2024phandthiosulfate pages 1-2) |
| complete Sox-dominant SOB | drives | acidity generation and thiosulfate consumption at lower pH | “Complete sox (csox) dominant SOB… drove acidity generation and S2O32− consumption via the csox pathway at lower pH (pH ~5 to ~6.5)” | Twible et al., 2024, DOI:10.3389/fmicb.2024.1426584, https://doi.org/10.3389/fmicb.2024.1426584 | Strong environment-specific phenotype edge. (twible2024phandthiosulfate pages 1-2) |
| incomplete sox / rdsr dominant SOB | associated with | higher thiosulfate and limited acidity generation at circumneutral pH | “At circumneutral pH conditions (pH ~6.5 to ~8.5), the presence of non-csox dominant SOB… were associated with higher [S2O32−] and limited acidity generation” | Twible et al., 2024, DOI:10.3389/fmicb.2024.1426584, https://doi.org/10.3389/fmicb.2024.1426584 | Strong geochemistry edge, but association rather than direct single-gene causation. (twible2024phandthiosulfate pages 1-2) |
| hybrid Sox-reverse Dsr pathway | allows oxidation of | thiosulfate, elemental sulfur, and sulfide as energy sources | “a hybrid Sox-reverse Dsr pathway… would allow the oxidation of thiosulfate, elemental sulfur, and sulfide as energy sources” | Seah et al., 2019, DOI:10.1128/mbio.01112-19, https://doi.org/10.1128/mbio.01112-19 | Strong sulfur-donor oxidation edge in boundary-case organism. (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| oxidation of reduced sulfur | produces energy for | lithoheterotrophic metabolism | “lithoheterotrophic metabolism, in which energy is produced by oxidation of reduced sulfur and carbon is assimilated in the form of organic compounds” | Seah et al., 2019, DOI:10.1128/mbio.01112-19, https://doi.org/10.1128/mbio.01112-19 | Strong boundary-case edge distinguishing lithoautotrophy from lithoheterotrophy. (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| absence of RuBisCO and other key autotrophy enzymes | indicates absence of | canonical autotrophic CO2 fixation | “genes for ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO) and other key enzymes in the six canonical autotrophic CO2 fixation pathways… were not predicted” | Seah et al., 2019, DOI:10.1128/mbio.01112-19, https://doi.org/10.1128/mbio.01112-19 | Strong negative evidence; important warning against over-curating sulfur oxidation as lithoautotrophy. (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |
| cbb3-type cytochrome c oxidase | is adapted to | microoxic conditions | “cbb3-type cytochrome c oxidase… has a high oxygen affinity and is typically expressed under microoxic conditions” | Seah et al., 2019, DOI:10.1128/mbio.01112-19, https://doi.org/10.1128/mbio.01112-19 | Useful environmental edge for sulfur oxidizers; not specific to lithoautotrophy. (seah2019sulfuroxidizingsymbiontswithout pages 2-4) |


*Table: This table compiles candidate evidence-backed subject-predicate-object edges for curating a lithoautotrophic TraitMech graph. It emphasizes mechanistic links among inorganic donor oxidation, respiratory energy conservation, reductant generation, carbon fixation, sulfur oxidation modules, DIC handling, and key boundary cases.*

---

## 5) Recent developments and latest research (prioritizing 2023–2024)

### 5.1 Gene-fitness resolution of lithoautotrophic energy metabolism (2024)
A 2024 barcoded transposon fitness study in *Cupriavidus necator* directly connects lithoautotrophic growth regimes to specific enzymes: soluble formate dehydrogenase dominates formate oxidation and **both soluble and membrane-bound hydrogenases** are used for lithoautotrophic growth; membrane-bound dehydrogenases couple oxidation to quinones and drive ETC → PMF. This advances curation by supporting edges beyond “gene presence” toward condition-specific requirement. (jahn2024theenergymetabolism pages 1-2)

### 5.2 Mechanistic refinement of rTCA reductive carboxylation (2023)
A 2023 biochemical/proteomic study in the chemolithoautotroph *Aquifex aeolicus* identifies low-potential ferredoxins (Fd6/Fd7, ~−440/−460 mV) as electron donors interacting with rTCA signature enzymes PFOR/OGOR, strengthening mechanistic edges that link electron transfer proteins to CO2 fixation steps in rTCA-based lithoautotrophy. (prioretti2023carbonfixationin pages 1-2)

### 5.3 DIC acquisition and speciation as a cross-pathway constraint (2024)
A 2024 minireview synthesizes that autotrophs use **DIC transporters and carbonic anhydrases** to “facilitate DIC fixation” and emphasizes that DIC speciation depends strongly on pH (“CO2 dominates at low pH, HCO3− at circumneutral pH”), implying environment → DIC form → enzyme substrate matching as an important layer in lithoautotrophic trait graphs. (scott2024widespreaddissolvedinorganic pages 1-2)

### 5.4 Ecological niche partitioning by electron acceptor availability (2023–2024)
Two complementary studies in mining-impacted waters show that O2 vs NO3− availability partitions sulfur-oxidizing chemolithoautotroph strategies with distinct outcomes:
- In a mine tailings impoundment, oxic Halothiobacillus with complete Sox coupled to O2 drove pH as low as 4.3 and low thiosulfate, while anoxic Thiobacillus with incomplete Sox + rDSR coupled to NO3− yielded higher thiosulfate and no net acidity. (whaleymartin2023o2partitioningof pages 1-2)
- Across systems, csox-dominant SOB drove acidity generation and thiosulfate consumption at pH ~5–6.5, while non-csox strategies correlated with higher thiosulfate and limited acidity at pH ~6.5–8.5; tsdA and tetH were partitioned by pH/taxa. (twible2024phandthiosulfate pages 1-2)

---

## 6) Current applications and real-world implementations

### 6.1 Mine tailings water management / in situ biotreatment (sulfur lithoautotrophs)
Mine tailings impoundments are dominated by neutrophilic chemolithoautotrophic sulfur oxidizers at large relative abundances (~55–76% depending on year). The work explicitly positions gene-based monitoring as a tool to predict acidification events and suggests in situ management via controlling sulfur species oxidation niches. (whaleymartin2023o2partitioningof pages 1-2)

### 6.2 Biomining and bioleaching
A 2024 review on copper tailings bioleaching provides quantitative operating ranges and industry context:
- dissolved O2: **1.5–4.1 mg/L**; pH: **0.5–7.2** (depending on system)
- notes **bioleaching contributed ~1.2% of global copper production through 2020**
- reports **2020 tailings production ~4.3 billion tons at ~0.46% Cu average** and gives examples of commercial operations (e.g., Dexing, Zijinshan, Jinchuan). (zhang2024accumulatedcoppertailing pages 1-2)

A 2024 circularity-focused biomining review describes commercial/pilot implementations and scale figures (e.g., a plant designed for ~1000 tons Ni and 20 tons Co annually; BIOX® biooxidation across 13 plants processing >25 million ounces Au), supporting the claim that litho/chemolithoautotrophic metabolisms are operationalized at industrial scales. (cozma2024biorecoveryofmetals pages 22-24)

### 6.3 Microbial electrosynthesis / electroautotrophic biomanufacturing (near-term implementation)
A 2025 study (included as near-term “implementation-style” evidence) demonstrates CO2 conversion coupled to electron supply in bioelectrochemical systems using *Cupriavidus necator*:
- CO2 removal from gas mix: **73% (MECs) vs 65% (MFCs)**
- PHB accumulation: **73% of cell volume in MFCs** (vs 23% MECs; 40% controls)
This illustrates practical use of lithoautotrophic CO2 fixation capability in engineered reactors, though it is not strictly 2023–2024. (nastro2025bioelectrosynthesisofpolyhydroxybutyrate pages 1-2)

### 6.4 Underground H2 storage / hydrogen economy constraints
A 2024 high-pressure reactor simulation of **2% H2 coinjection** into a natural gas blend for **3 months** showed microbial succession (sulfate reduction → acetogenesis → methanogenesis), with methanogenesis as the main driver of H2 consumption, but overall limited H2 loss likely due to nutrient depletion; the paper argues low-salinity, electron-acceptor-poor aquifers may be preferable for H2 co-storage. These processes are relevant to lithoautotrophic and hydrogenotrophic guilds (including methanogens and acetogens). (mura2024experimentalsimulationof pages 1-2)

---

## 7) Relevant statistics and quantitative data (from cited studies)
- **Mine tailings impoundment SOB relative abundances**: chemolithoautotrophic SOB ~76% (2015), ~55% (2016/2017), ~60% (2018). (whaleymartin2023o2partitioningof pages 1-2)
- **Mine tailings acidification outcome**: pH as low as **4.3** under oxic complete Sox activity. (whaleymartin2023o2partitioningof pages 1-2)
- **Mine tailings thiosulfate**: mean thiosulfate concentration **0.2 ± 0.3 mM** in the dataset described. (whaleymartin2023o2partitioningof pages 3-5)
- **Bioleaching operating envelope (reviewed)**: dissolved O2 **1.5–4.1 mg/L**, pH **0.5–7.2**; bioleaching ~**1.2%** of global copper production through 2020; tailings production **4.3 billion tons** at **~0.46% Cu** (2020 estimate). (zhang2024accumulatedcoppertailing pages 1-2)
- **Electroautotrophy implementation-style metrics (2025)**: CO2 removal **73% vs 65%**; PHB accumulation **73% cell volume** (MFC). (nastro2025bioelectrosynthesisofpolyhydroxybutyrate pages 1-2)
- **Underground H2 co-storage simulation**: **2% H2** in blend; **3-month** experiment; succession to methanogenesis with limited total H2 loss. (mura2024experimentalsimulationof pages 1-2)

---

## 8) Warnings / non-curatable (yet) claims
1. **Do not equate sulfur oxidation genes with lithoautotrophy by default.** The Kentron symbiont example shows sulfur oxidation capacity but absence of canonical CO2 fixation genes (including RuBisCO), supporting lithoheterotrophy instead. Curate this as a strong negative control/boundary-case. (seah2019sulfuroxidizingsymbiontswithout pages 2-4)
2. **Electrode-based lithoautotrophy (EEU/electroautotrophy) is assay-conditional.** Edges involving electrodes/minerals and EEU depend on redox potential and reactor conditions; curate as conditional modules unless the TraitMech scope explicitly includes EEU. (gupta2020extracellularelectronuptake pages 4-5)
3. **Formate as an electron donor is taxon-specific.** C. necator uses formate and has specific FDH systems; this should likely be an optional node/edge set rather than a core lithoautotrophy requirement. (jahn2024theenergymetabolism pages 1-2)

---

## 9) DOI-first bibliography (with URLs and publication dates where available)

1. **Jahn M, et al.** (Published **25 Sep 2024**). *The energy metabolism of Cupriavidus necator in different trophic conditions.* Applied and Environmental Microbiology. DOI: **10.1128/aem.00748-24**. URL: https://doi.org/10.1128/aem.00748-24 (jahn2024theenergymetabolism pages 1-2)

2. **Scott KM, Payne RR, Gahramanova A.** (Published **1 Feb 2024**). *Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea…* Applied and Environmental Microbiology. DOI: **10.1128/aem.01557-23**. URL: https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 1-2)

3. **Prioretti L, et al.** (Published **23 Feb 2023**). *Carbon Fixation in the Chemolithoautotrophic Bacterium Aquifex aeolicus…* Life. DOI: **10.3390/life13030627**. URL: https://doi.org/10.3390/life13030627 (prioretti2023carbonfixationin pages 1-2)

4. **Whaley-Martin KJ, et al.** (Published **Apr 2023**; accepted 14 Mar 2023). *O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters.* Nature Communications. DOI: **10.1038/s41467-023-37426-8**. URL: https://doi.org/10.1038/s41467-023-37426-8 (whaleymartin2023o2partitioningof pages 1-2, whaleymartin2023o2partitioningof pages 3-5)

5. **Twible LE, et al.** (Published **19 Jul 2024**). *pH and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments.* Frontiers in Microbiology. DOI: **10.3389/fmicb.2024.1426584**. URL: https://doi.org/10.3389/fmicb.2024.1426584 (twible2024phandthiosulfate pages 1-2)

6. **Mura J, et al.** (Published **Jul 2024**). *Experimental simulation of H2 coinjection… in a deep aquifer used for current underground gas storage.* Frontiers in Microbiology. DOI: **10.3389/fmicb.2024.1439866**. URL: https://doi.org/10.3389/fmicb.2024.1439866 (mura2024experimentalsimulationof pages 1-2)

7. **Zhang J, et al.** (Published **Oct 2024**). *Accumulated copper tailing solid wastes… advances in microbial leaching.* Minerals. DOI: **10.3390/min14101051**. URL: https://doi.org/10.3390/min14101051 (zhang2024accumulatedcoppertailing pages 1-2)

8. **Cozma P, et al.** (Published **Aug 2024**). *Bio-Recovery of Metals through Biomining within Circularity-Based Solutions.* Processes. DOI: **10.3390/pr12091793**. URL: https://doi.org/10.3390/pr12091793 (cozma2024biorecoveryofmetals pages 22-24)

9. **Seah BKB, et al.** (Published **2019**). *Sulfur-oxidizing symbionts without canonical genes for autotrophic CO2 fixation.* mBio. DOI: **10.1128/mbio.01112-19**. URL: https://doi.org/10.1128/mbio.01112-19 (seah2019sulfuroxidizingsymbiontswithout pages 2-4)

10. **Gupta D, Guzman MS, Bose A.** (Published **Oct 2020**). *Extracellular electron uptake by autotrophic microbes…* Journal of Industrial Microbiology and Biotechnology. DOI: **10.1007/s10295-020-02309-0**. URL: https://doi.org/10.1007/s10295-020-02309-0 (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 4-5)

11. **Nastro RA, et al.** (Published **Feb 2025**; included as near-term implementation example). *Bio-electrosynthesis of polyhydroxybutyrate and surfactants in microbial fuel cells…* Frontiers in Microbiology. DOI: **10.3389/fmicb.2025.1372302**. URL: https://doi.org/10.3389/fmicb.2025.1372302 (nastro2025bioelectrosynthesisofpolyhydroxybutyrate pages 1-2)


References

1. (jahn2024theenergymetabolism pages 1-2): Michael Jahn, Nick Crang, Arvid H. Gynnå, Deria Kabova, Stefan Frielingsdorf, Oliver Lenz, Emmanuelle Charpentier, and Elton P. Hudson. The energy metabolism of <i>cupriavidus necator</i> in different trophic conditions. Oct 2024. URL: https://doi.org/10.1128/aem.00748-24, doi:10.1128/aem.00748-24. This article has 39 citations and is from a peer-reviewed journal.

2. (scott2024widespreaddissolvedinorganic pages 1-2): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

3. (seah2019sulfuroxidizingsymbiontswithout pages 2-4): Brandon K. B. Seah, Chakkiath Paul Antony, Bruno Huettel, Jan Zarzycki, Lennart Schada von Borzyskowski, Tobias J. Erb, Angela Kouris, Manuel Kleiner, Manuel Liebeke, Nicole Dubilier, and Harald R. Gruber-Vodicka. Sulfur-oxidizing symbionts without canonical genes for autotrophic co <sub>2</sub> fixation. mBio, Jun 2019. URL: https://doi.org/10.1128/mbio.01112-19, doi:10.1128/mbio.01112-19. This article has 32 citations and is from a domain leading peer-reviewed journal.

4. (gupta2020extracellularelectronuptake pages 4-5): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 78 citations and is from a peer-reviewed journal.

5. (prioretti2023carbonfixationin pages 1-2): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 7 citations.

6. (whaleymartin2023o2partitioningof pages 3-5): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

7. (whaleymartin2023o2partitioningof pages 1-2): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

8. (gupta2020extracellularelectronuptake pages 8-9): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 78 citations and is from a peer-reviewed journal.

9. (nosalova2023coldsulfursprings—neglected pages 11-12): Lea Nosalova, Maria Piknova, Mariana Kolesarova, and Peter Pristas. Cold sulfur springs—neglected niche for autotrophic sulfur-oxidizing bacteria. Microorganisms, 11:1436, May 2023. URL: https://doi.org/10.3390/microorganisms11061436, doi:10.3390/microorganisms11061436. This article has 16 citations.

10. (gupta2020extracellularelectronuptake pages 5-6): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 78 citations and is from a peer-reviewed journal.

11. (gupta2020extracellularelectronuptake pages 1-2): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 78 citations and is from a peer-reviewed journal.

12. (seah2019sulfuroxidizingsymbiontswithout pages 16-16): Brandon K. B. Seah, Chakkiath Paul Antony, Bruno Huettel, Jan Zarzycki, Lennart Schada von Borzyskowski, Tobias J. Erb, Angela Kouris, Manuel Kleiner, Manuel Liebeke, Nicole Dubilier, and Harald R. Gruber-Vodicka. Sulfur-oxidizing symbionts without canonical genes for autotrophic co <sub>2</sub> fixation. mBio, Jun 2019. URL: https://doi.org/10.1128/mbio.01112-19, doi:10.1128/mbio.01112-19. This article has 32 citations and is from a domain leading peer-reviewed journal.

13. (twible2024phandthiosulfate pages 1-2): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

14. (zhang2024accumulatedcoppertailing pages 1-2): Juan Zhang, Xiaojun Liu, Xinyue Du, Xin Wang, Yifan Zeng, and Shu-kai Fan. Accumulated copper tailing solid wastes with specific compositions encourage advances in microbial leaching. Minerals, 14:1051, Oct 2024. URL: https://doi.org/10.3390/min14101051, doi:10.3390/min14101051. This article has 4 citations.

15. (cozma2024biorecoveryofmetals pages 22-24): Petronela Cozma, Camelia Bețianu, Raluca-Maria Hlihor, Isabela Maria Simion, and Maria Gavrilescu. Bio-recovery of metals through biomining within circularity-based solutions. Processes, 12:1793, Aug 2024. URL: https://doi.org/10.3390/pr12091793, doi:10.3390/pr12091793. This article has 25 citations.

16. (nastro2025bioelectrosynthesisofpolyhydroxybutyrate pages 1-2): Rosa Anna Nastro, Chandrasekhar Kuppam, Maria Toscanesi, Marco Trifuoggi, Andrea Pietrelli, Vincenzo Pasquale, and Claudio Avignone-Rossa. Bio-electrosynthesis of polyhydroxybutyrate and surfactants in microbial fuel cells: a preliminary study. Frontiers in Microbiology, Feb 2025. URL: https://doi.org/10.3389/fmicb.2025.1372302, doi:10.3389/fmicb.2025.1372302. This article has 11 citations and is from a peer-reviewed journal.

17. (mura2024experimentalsimulationof pages 1-2): Jean Mura, Magali Ranchou-Peyruse, Marion Guignard, Marion Ducousso, Marie Larregieu, Marie-Pierre Isaure, Isabelle Le Hécho, Guilhem Hoareau, Marie Poulain, Mateus de Souza Buruti, Pierre Chiquet, Guilhem Caumette, Anélia Petit, Pierre Cézac, and Anthony Ranchou-Peyruse. Experimental simulation of h2 coinjection via a high-pressure reactor with natural gas in a low-salinity deep aquifer used for current underground gas storage. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1439866, doi:10.3389/fmicb.2024.1439866. This article has 9 citations and is from a peer-reviewed journal.