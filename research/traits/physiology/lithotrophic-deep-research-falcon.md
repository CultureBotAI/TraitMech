---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:20:14.273649'
end_time: '2026-08-04T11:30:29.664231'
duration_seconds: 615.39
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: lithotrophic
  trait_identifier: METPO:1000649
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: lithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses inorganic compounds as electron
    donors for energy generation.
  parent_traits: METPO:1000631
  synonyms: TT_lithotroph, lithotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms
    or molecules (Encyclopedia review supports inorganic compounds as growth-supporting
    reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation
    of an electrochemical ion gradient (Review supports respiratory energy conservation
    through ion gradients and ATP synthesis.)'
  causal_graph_summary: 'lithotrophic_inorganic_donor_energy: 19 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000649
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses inorganic compounds as electron donors for energy generation.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_lithotroph, lithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Encyclopedia review supports inorganic compounds as growth-supporting reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation of an electrochemical ion gradient (Review supports respiratory energy conservation through ion gradients and ATP synthesis.)
- **Existing causal graph summary:** lithotrophic_inorganic_donor_energy: 19 nodes, 12 edges

## Research Objective

Research the microbial trait **lithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithotrophic.yaml`.

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
- **Trait label:** lithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000649
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses inorganic compounds as electron donors for energy generation.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_lithotroph, lithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Encyclopedia review supports inorganic compounds as growth-supporting reductants and energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: generation of an electrochemical ion gradient (Review supports respiratory energy conservation through ion gradients and ATP synthesis.)
- **Existing causal graph summary:** lithotrophic_inorganic_donor_energy: 19 nodes, 12 edges

## Research Objective

Research the microbial trait **lithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithotrophic.yaml`.

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


# Curation report: lithotrophic

## Trait record and scope

- **Trait label:** lithotrophic
- **Trait identifier:** **“METPO:1000649”**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000631
- **Synonyms:** TT_lithotroph; lithotroph
- **Operational definition:** a trophic type in which an organism uses inorganic compounds as electron donors for energy generation.

### Interpretation for TraitMech

Lithotrophy classifies the **source of reducing electrons**, not the carbon source, terminal electron acceptor, or primary energy source. A lithotroph oxidizes an inorganic donor—commonly H₂, NH₃/NH₄⁺, NO₂⁻, H₂S/HS⁻, S⁰, S₂O₃²⁻, Fe(II), CO, or an inorganic mineral/electrode—and transfers the electrons into an energy-conserving system. The recurrent mechanistic pattern is:

**inorganic donor → donor-specific oxidoreductase/conduit → electron carriers and respiratory or photosynthetic chain → electrochemical ion gradient → ATP synthesis**, often with reverse electron transport or electron bifurcation supplying low-potential reductant for biosynthesis.

Lithotrophy does **not** imply autotrophy. A lithoautotroph fixes inorganic carbon, whereas a lithoheterotroph uses an inorganic electron donor but obtains biomass carbon from organic compounds. Similarly, chemolithotrophs derive energy from chemical oxidation, while photolithotrophs combine inorganic electron donors with light-driven energy conversion. Organisms may switch among lithotrophic, organotrophic, autotrophic, heterotrophic, and mixotrophic modes; therefore, the trait should be curated from demonstrated physiology rather than inferred solely from taxonomy.

Extracellular electron uptake (EEU) is a boundary case. It qualifies when an insoluble inorganic mineral or electrode is experimentally shown to supply electrons that support energy metabolism or growth. EEU includes direct outer-membrane conduits and indirect redox shuttles, but it is not a universal mechanism of lithotrophy. (gupta2020extracellularelectronuptake pages 1-2)

## Recommended graph design

The existing 19-node/12-edge graph should be retained as a **generic core**, with donor-specific branches represented as alternative modules rather than a single universal pathway. This avoids implying that every lithotroph carries hydrogenase, Sox, AMO, NXR, Cyc2, or the same carbon-fixation pathway.

| donor/module | initiating catalyst or conduit | downstream energy-conservation module | representative acceptor/carbon-fixation coupling | evidence strength/limitations |
|---|---|---|---|---|
| H2 lithotrophy | [NiFe]-hydrogenase; membrane-bound/extracellular uptake hydrogenase in some taxa (colman2024themicrobialecology pages 21-24) | electrons relayed to quinones/ubiquinone, then cytochrome complexes/terminal oxidases or ferrireductase; proton translocation generates PMF; ATP and NADH generation supported (colman2024themicrobialecology pages 21-24, gupta2020extracellularelectronuptake pages 5-6) | O2 or Fe(III) can serve as acceptors in documented systems; H2-supported autotrophy occurs in serpentinites and SRB/acetogen systems; carbon fixation may couple via Wood–Ljungdahl or other autotrophic routes depending on taxon (colman2024themicrobialecology pages 11-14, gupta2020extracellularelectronuptake pages 5-6) | Strong for H2 as inorganic donor and hydrogenase–quinone–PMF coupling; specific chain architecture is taxon-specific and partly inferred from omics/models outside a few systems (colman2024themicrobialecology pages 21-24, gupta2020extracellularelectronuptake pages 5-6) |
| Reduced sulfur oxidation | Sox pathway components (soxXA, soxYZ, soxB, soxCD); S4I components tsdA and tetH; rDsr/incomplete Sox in some lineages (twible2024phandthiosulfate pages 1-2) | sulfur oxidation feeds respiratory electron transport; pathway choice correlates with acidity generation vs limited acidity generation under different pH regimes (twible2024phandthiosulfate pages 1-2) | Commonly coupled to O2 or NO3- reduction in sulfur oxidizers; sulfur oxidizers often fix CO2 via CBB cycle in reviewed examples (gupta2020extracellularelectronuptake pages 8-9, twible2024phandthiosulfate pages 1-2) | Strong for sulfur donors supporting lithotrophy; exact initiating enzyme differs among sulfur species and taxa; SQR-specific evidence was not directly retrieved here, so curate Sox/S4I/rDsr conservatively and leave SQR as candidate-only (twible2024phandthiosulfate pages 1-2, gupta2020extracellularelectronuptake pages 8-9) |
| Ammonia oxidation | AMO (ammonia monooxygenase); downstream oxidation of hydroxylamine and possibly nitric oxide remains mechanistically unresolved in AOA compared with canonical bacterial models (wright2023nitrificationandbeyond pages 5-7) | ammonia oxidation supplies reductant for respiratory energy conservation and autotrophy; detailed electron-transfer steps vary across AOA/AOB and are incompletely resolved in AOA (wright2023nitrificationandbeyond pages 5-7) | AOA are chemolithoautotrophs fixing carbon via the 3-hydroxypropionate/4-hydroxybutyrate pathway; experimentally confirmed energy-yielding substrates include ammonia, urea, cyanate, hydroxylamine, and hydrazine (wright2023nitrificationandbeyond pages 5-7) | Strong that ammonia oxidation is lithotrophic; weak/moderate for universal mechanistic edges beyond AMO because archaeal downstream pathway details remain uncertain and differ from bacterial textbook schemes (wright2023nitrificationandbeyond pages 5-7) |
| Nitrite oxidation | nitrite oxidoreductase (NXR/NOR) (supported in retrieved nitrite-oxidizer summaries) | nitrite oxidation transfers electrons into electron transport and can require reverse electron transport for reducing power (supported in retrieved nitrite-oxidizer summaries) | nitrite-oxidizing bacteria are chemolithoautotrophs; carbon fixation can proceed via reductive TCA in Nitrospina/Nitrospira examples from retrieved searches, but these details were not in gathered-context IDs and should be added cautiously | Moderate: nitrite oxidation is a clear lithotrophic module, but direct citation support in gathered context IDs is limited; avoid over-curating transporter/topology details without stronger in-context evidence |
| Fe(II) oxidation | outer membrane cytochrome c conduit Cyc2 in iron oxidizers; Fe(II)-derived electrons transferred toward periplasmic/interior carriers (gupta2020extracellularelectronuptake pages 3-3) | reviewed examples support electron transfer through cytochrome networks and reverse electron transfer in some Fe-oxidizing/autotrophic systems; PMF generation is part of the broader EEU/Fe oxidation framing (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 9-10) | Fe(II) oxidation supports chemolithotrophic carbon assimilation in iron oxidizers; representative donors include FeS, FeCO3, FeS2, Fe3O4, and green rust in reviewed EEU context (gupta2020extracellularelectronuptake pages 3-3) | Moderate: Fe(II) as donor and Cyc2 as conduit are well supported, but specific downstream chain components are lineage-specific and much evidence is comparative/review-based rather than direct biochemistry in the gathered set (gupta2020extracellularelectronuptake pages 3-3, gupta2020extracellularelectronuptake pages 8-9) |
| Extracellular electron uptake (electrode/mineral/cell-derived electrons) | multiheme c-type cytochromes; outer membrane conduits; periplasmic cytochromes such as tetraheme c3 in SRB examples (gupta2020extracellularelectronuptake pages 1-2, gupta2020extracellularelectronuptake pages 5-6) | electrons routed to inner-membrane quinone-interacting complexes (for example Qrc/Tmc, QmoABC, DsrMKJOP in SRB examples), generating transmembrane proton gradients and supporting ATP synthesis/reverse electron flow (gupta2020extracellularelectronuptake pages 5-6) | documented in autotrophs including sulfur oxidizers, iron oxidizers, SRB, acetogens, and phototroph-linked systems; can support CO2 fixation where reducing power is generated (gupta2020extracellularelectronuptake pages 1-2, gupta2020extracellularelectronuptake pages 9-10) | Moderate and assay-specific: EEU is relevant as a lithotrophic-like edge when insoluble inorganic donors/electrodes serve as electron sources, but mechanisms are not universal and many examples are model-system specific (gupta2020extracellularelectronuptake pages 1-2, gupta2020extracellularelectronuptake pages 5-6) |
| Shared respiratory core across lithotrophs | donor-specific oxidoreductase/conduit feeds quinone pool and cytochrome carriers (colman2024themicrobialecology pages 21-24, gupta2020extracellularelectronuptake pages 5-6) | quinone/cytochrome electron transport drives ion-gradient formation (PMF); ATP synthesis and often reverse electron flow/NADH generation follow (gupta2020extracellularelectronuptake pages 5-6) | coupled variably to O2, NO3-, Fe(III), and carbon fixation modules depending on taxon and environment (colman2024themicrobialecology pages 11-14, gupta2020extracellularelectronuptake pages 8-9) | Strong as a high-level conserved motif, but not every lithotroph uses the same quinone, cytochromes, or carbon-fixation pathway; curate as an abstract module, not a single universal gene set (gupta2020extracellularelectronuptake pages 5-6, colman2024themicrobialecology pages 21-24) |


*Table: This table summarizes evidence-backed donor modules and shared bioenergetic architecture relevant to curating the lithotrophic trait. It highlights where evidence is strong enough for core TraitMech edges and where mechanisms remain taxon-specific or uncertain.*

## Candidate nodes grouped by type

### 1. Trait and process nodes

| Candidate node | Suggested grounding | Curation role |
|---|---|---|
| lithotrophic | **METPO:1000649** | Target trait |
| oxidation–reduction process | GO:0055114 | Broad process; use only if allowed by schema |
| electron transport chain | GO:0022900 | Shared energy-conservation module |
| respiratory electron transport chain | GO:0022904 | Chemolithotrophic branch |
| proton motive force / proton electrochemical gradient | Label; GO:0015988 may be considered for energy coupled proton transport | Intermediate energetic state |
| ATP synthesis coupled proton transport | GO:0015986 | Conserved energetic output |
| carbon fixation | GO:0015977 | Optional downstream process; not part of the defining trait |
| reverse electron transport | Label-only candidate | Generates low-potential reductant in several lithotrophs |
| extracellular electron uptake | Label-only candidate | Assay-specific extension |

### 2. Inorganic electron donors and products

Recommended chemical nodes include molecular hydrogen (**CHEBI:18276**), ammonia (**CHEBI:16134**), ammonium (**CHEBI:28938**), nitrite (**CHEBI:16301**), nitrate (**CHEBI:17632**), hydrogen sulfide (**CHEBI:16136**), thiosulfate (**CHEBI:26977**), elemental sulfur (label; validate the intended CHEBI form), ferrous iron/Fe(II) (**CHEBI:29033**), ferric iron/Fe(III) (**CHEBI:29034**), carbon monoxide (**CHEBI:17245**), carbon dioxide (**CHEBI:16526**), oxygen (**CHEBI:15379**), and electron (**CHEBI:10545**). Exact protonation states should match assay pH and source wording.

Additional sulfur nodes—HS⁻, sulfite, sulfate, tetrathionate, and polysulfides—should be added only to the relevant sulfur-oxidation subgraph. Mineral donors such as FeS, FeCO₃, FeS₂, Fe₃O₄, and green rust are documented in the EEU/iron-lithotrophy literature, but mineral phase and oxidation state must be represented precisely. (gupta2020extracellularelectronuptake pages 3-3)

### 3. Enzymes, proteins, and complexes

| Module | Candidate entities | Grounding recommendation |
|---|---|---|
| H₂ oxidation | [NiFe]-hydrogenase; [FeFe]-hydrogenase; uptake hydrogenase; hydrogenase accessory proteins | Use EC:1.12.1.2 only when the reaction and cofactor class match; otherwise retain family labels and use taxon-specific UniProt accessions |
| Ammonia oxidation | ammonia monooxygenase, AMO; AmoA/AmoB/AmoC | EC:1.14.99.39 is a candidate; verify against the curated enzyme record and organism |
| Bacterial hydroxylamine oxidation | hydroxylamine dehydrogenase/oxidoreductase, Hao | EC:1.7.2.6 candidate; do not project universally to AOA |
| Nitrite oxidation | nitrite oxidoreductase, NXR | Use protein/accession-level grounding; topology and subunits vary |
| Sulfur oxidation | SoxXA, SoxYZ, SoxB, SoxCD; TsdA; TetH; reverse Dsr system; sulfide:quinone oxidoreductase candidate | Prefer UniProt/EC grounding per protein and reaction; avoid treating “Sox” as one enzyme |
| Fe(II) oxidation | Cyc2; rusticyanin; Cyc1/cytochrome c₄; MtoAB/PioAB in relevant taxa | Protein-family labels plus taxon-specific UniProt IDs |
| EEU | outer-membrane multiheme c-type cytochromes; tetraheme cytochrome c₃; Qrc/Tmc; QmoABC; DsrMKJOP | Extension module restricted to demonstrated taxa/assays |
| Shared carriers | ubiquinone/ubiquinol or menaquinone/menaquinol; cytochrome bc₁; cytochrome c; terminal oxidase | Do not collapse chemically distinct quinone pools |
| Energy conversion | F-, A-, or V-type ATP synthase | GO:0042777/GO:0015986 as appropriate; complex identity is taxon-specific |
| Carbon fixation | RuBisCO/CBB cycle; Wood–Ljungdahl pathway; reductive TCA cycle; 3-hydroxypropionate/4-hydroxybutyrate cycle | Downstream contextual nodes, not defining nodes |

### 4. Cellular locations

Candidate locations include outer membrane, periplasm, cytoplasmic membrane, cytoplasm, extracellular mineral surface, and electrode–biofilm interface. These should be grounded with GO cellular-component terms only when the source organism’s cell architecture is known; “periplasm” and “outer membrane” are inappropriate universal nodes for Archaea and monoderm bacteria.

### 5. Environmental and experimental factors

- Availability and concentration of the inorganic donor.
- Terminal acceptor availability: O₂, nitrate, sulfate, Fe(III), or others.
- Redox potential and donor–acceptor interface.
- pH, especially for sulfur and iron oxidation.
- Light for photolithotrophic branches.
- CO₂ or bicarbonate availability when testing lithoautotrophic growth.
- Electrode potential and material for EEU assays.
- Organic-carbon availability when distinguishing obligate lithoautotrophy from mixotrophy.
- Inhibitors such as acetylene for AMO assays or donor-specific competitors should be curated only with direct experimental evidence.

## Candidate evidence-backed causal edges

Predicates below are intentionally simple and should be mapped to the project’s controlled relation vocabulary.

| # | Subject–predicate–object | Reference | Supporting snippet | Curation notes |
|---:|---|---|---|---|
| 1 | inorganic electron donor — **is oxidized to supply** → electrons for energy metabolism | Gupta et al., 2020, DOI: [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0) | EEU is the capacity to use electrons from insoluble donors, including minerals and electrodes, for essential redox processes. | **Core conceptual edge.** Keep donor class abstract; donor-specific reactions belong in branches. (gupta2020extracellularelectronuptake pages 1-2)
| 2 | donor-derived electron flow — **drives formation of** → transmembrane proton gradient | Gupta et al., 2020 | Quinone-interacting complexes in sulfate reducers contribute to transmembrane proton gradients. | Strong respiratory architecture, but demonstrated complexes are taxon-specific. (gupta2020extracellularelectronuptake pages 5-6)
| 3 | transmembrane proton gradient — **powers** → ATP synthesis | Gupta et al., 2020 | The gradient generates proton motive force for ATP synthesis. | **Core edge**, consistent with the existing BBA Bioenergetics evidence. (gupta2020extracellularelectronuptake pages 5-6)
| 4 | reverse electron flow — **generates** → NADH/reducing power for CO₂ fixation | Gupta et al., 2020 | PMF supports “NADH production via reverse electron flow for CO₂ fixation.” | Common but not universal; some anaerobes instead use electron bifurcation or other mechanisms. (gupta2020extracellularelectronuptake pages 5-6)
| 5 | H₂ — **is oxidized by** → hydrogenase | Colman et al., 2024, DOI: [10.1101/2024.11.10.622848](https://doi.org/10.1101/2024.11.10.622848) | The review identifies [FeFe]-, [NiFe]-, and [Fe]-hydrogenases enabling reversible H₂ metabolism. | Strong family-level edge; preprint review and enzyme directionality require organism-specific confirmation. (colman2024themicrobialecology pages 21-24)
| 6 | membrane-bound [NiFe]-hydrogenase — **transfers electrons to** → quinone pool | Colman et al., 2024 | Membrane-associated hydrogenases couple through accessory subunits to hydride carriers, including quinones. | **Taxon-specific extension**, not universal to all hydrogenases. (colman2024themicrobialecology pages 21-24)
| 7 | H₂ oxidation — **supports** → aerobic autotrophic growth of *Serpentinimonas* | Colman et al., 2024 | *Serpentinimonas* is described as an “H₂-dependent aerobic autotroph.” | Taxon-specific phenotype; suitable as exemplar evidence, not as a universal edge. (colman2024themicrobialecology pages 11-14)
| 8 | sulfate concentration above 10 μM — **favors** → *Thermodesulfovibrio* over methanogens | Colman et al., 2024 | *Thermodesulfovibrio* outcompeted methanogens when sulfate exceeded 10 μM. | Environmental-selection edge; likely system/taxon-specific and should not enter the generic trait graph. (colman2024themicrobialecology pages 11-14)
| 9 | ammonia oxidation — **supplies reductant for** → 3-hydroxypropionate/4-hydroxybutyrate carbon fixation | Wright & Lehtovirta-Morley, 2023, DOI: [10.1038/s41396-023-01467-0](https://doi.org/10.1038/s41396-023-01467-0) | AOA are chemolithoautotrophs that use reductant from ammonia oxidation to fix carbon through the 3-HP/4-HB pathway. | Strong for AOA; do not generalize this fixation pathway to AOB. (wright2023nitrificationandbeyond pages 5-7)
| 10 | ammonia — **is substrate for** → ammonia monooxygenase | Wright & Lehtovirta-Morley, 2023 | The review identifies ammonia as an energy-yielding substrate and AMO as the initiating enzyme. | Strong, but archaeal downstream chemistry remains incompletely resolved. (wright2023nitrificationandbeyond pages 5-7)
| 11 | urea/cyanate — **supplies ammonia or supports** → AOA energy metabolism | Wright & Lehtovirta-Morley, 2023 | Confirmed AOA energy-yielding substrates include ammonia, urea, cyanate, hydroxylamine, and hydrazine. | **Taxon- and pathway-specific.** Avoid direct urea→AMO edges without urease-mediated conversion evidence. (wright2023nitrificationandbeyond pages 5-7)
| 12 | thiosulfate — **is oxidized by** → complete Sox pathway | Twible et al., 2024, DOI: [10.3389/fmicb.2024.1426584](https://doi.org/10.3389/fmicb.2024.1426584) | Complete-Sox organisms drove S₂O₃²⁻ consumption; SoxXA, SoxYZ, SoxB, and SoxCD comprise the pathway. | Strong in mine-tailings SOB; represent Sox components rather than a fictitious single Sox enzyme. (twible2024phandthiosulfate pages 1-2)
| 13 | complete Sox-mediated thiosulfate oxidation — **increases** → acidity generation | Twible et al., 2024 | Complete-Sox-dominant SOB drove thiosulfate consumption and acidity generation at pH approximately 5–6.5. | Context-specific geochemical outcome; conditional edge requiring oxic tailings conditions. (twible2024phandthiosulfate pages 1-2)
| 14 | pH 5–6.5 — **selects for** → complete-Sox-dominant SOB | Twible et al., 2024 | *Halothiobacillus* and *Thiomonas* with complete Sox dominated at lower pH. | Ecological association rather than a direct molecular mechanism; mark **uncertain/observational**. (twible2024phandthiosulfate pages 1-2)
| 15 | pH 6.5–8.5 — **associates with** → incomplete-Sox/rDsr sulfur oxidation strategies | Twible et al., 2024 | *Thiobacillus* and *Sulfuriferula* carrying incomplete Sox/rDsr occurred at circumneutral pH with limited acidity generation. | Observational and community-specific; not a universal inhibition edge. (twible2024phandthiosulfate pages 1-2)
| 16 | TsdA — **catalyzes** → thiosulfate-to-tetrathionate conversion | Twible et al., 2024 | S4I part 1 is described as “tsdA; S₂O₃²⁻ to S₄O₆²⁻.” | Suitable donor-specific reaction edge after checking exact enzyme accession. (twible2024phandthiosulfate pages 1-2)
| 17 | TetH — **participates in** → tetrathionate disproportionation | Twible et al., 2024 | S4I part 2 was TetH-mediated tetrathionate disproportionation and was restricted to *Thiobacillus*. | **Taxon-specific**; reaction products should be verified before adding product edges. (twible2024phandthiosulfate pages 1-2)
| 18 | H₂S/HS⁻ or S⁰ — **serves as electron donor for** → O₂ or nitrate reduction | Gupta et al., 2020 | Sulfur oxidizers couple H₂S/HS⁻ or S⁰ oxidation to reduction of O₂ or NO₃⁻. | Strong high-level sulfur-lithotrophy edge; individual enzyme routes vary. (gupta2020extracellularelectronuptake pages 8-9)
| 19 | sulfur oxidation — **supports** → CBB-cycle CO₂ fixation | Gupta et al., 2020 | Reviewed sulfur oxidizers use the CBB cycle for CO₂ fixation. | Common but not universal; keep carbon fixation as an optional taxon-specific branch. (gupta2020extracellularelectronuptake pages 8-9)
| 20 | Fe(II)/iron-bearing mineral — **donates electrons through** → Cyc2/PioAB-type conduit | Gupta et al., 2020 | PioAB transfers electrons from Fe(II) or electrodes across the outer membrane; iron minerals are recognized donors. | **Lineage-specific.** Do not equate PioAB and Cyc2 or apply either universally. (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 3-3)
| 21 | outer-membrane multiheme cytochrome — **accepts electrons from** → insoluble donor | Gupta et al., 2020 | Multiheme c-type cytochromes accept electrons from elemental iron or electrodes. | EEU-specific; require direct electrochemical or growth evidence. (gupta2020extracellularelectronuptake pages 5-6, gupta2020extracellularelectronuptake pages 1-2)
| 22 | periplasmic tetraheme cytochrome c₃ — **transfers electrons to** → Qrc/Tmc complexes | Gupta et al., 2020 | Tetraheme c₃ shuttles electrons to inner-membrane Qrc/Tmc complexes in sulfate reducers. | Strong only for the described SRB systems. (gupta2020extracellularelectronuptake pages 5-6)
| 23 | electrode-derived electron uptake — **supports** → autotrophic carbon fixation | Gupta et al., 2020 | Electrode-based EEU supports autotrophic metabolism in tested sulfur oxidizers, iron oxidizers, sulfate reducers, acetogens, and phototrophs. | **Assay-specific**; electrode current alone is insufficient without biomass/carbon-assimilation evidence. (gupta2020extracellularelectronuptake pages 9-10, gupta2020extracellularelectronuptake pages 1-2)
| 24 | light-excited anoxygenic photosystem — **drives** → cyclic electron flow and PMF | Gupta et al., 2020 | Anoxygenic phototrophs generate PMF by cyclic photophosphorylation and synthesize ATP. | Valid photolithotrophic branch, but light—not donor oxidation alone—is the primary energy input. (gupta2020extracellularelectronuptake pages 8-9)

## Recent developments and data

### Ammonia-oxidizing Archaea

The 2023 ISME Journal review emphasizes that AOA are globally abundant nitrogen-cycle organisms and are more metabolically versatile than the traditional “highly streamlined specialist” model suggests. It identifies ammonia, urea, cyanate, hydroxylamine, and hydrazine as experimentally supported energy-yielding substrates in at least some AOA. It also reports group 3b [NiFe]-hydrogenases in thermophilic *Nitrosocaldus* strains growing near **70°C**, while hydrogenase-related group 4a complexes occur in selected *Nitrosotalea*, *Nitrososphaera*, and *Nitrosocosmicus*. These distributions do not establish universal H₂-supported growth in AOA. (wright2023nitrificationandbeyond pages 5-7)

### Environmentally partitioned sulfur oxidation

Twible et al. analyzed mine-tailings waters over **four years (2016–2019)** and found pathway partitioning by pH and thiosulfate availability. Complete-Sox organisms were associated with **pH ≈5–6.5**, thiosulfate consumption, and acidity generation, whereas incomplete-Sox/rDsr strategies occurred chiefly at **pH ≈6.5–8.5** and were associated with higher residual thiosulfate and limited acid generation. The result supports conditional environmental edges rather than one universal sulfur-oxidation mechanism. (twible2024phandthiosulfate pages 1-2)

### Hydrogen-driven serpentinite ecosystems

A 2024 serpentinite review reports that approximately **90%** of population genomes from Samail Ophiolite fracture waters encoded at least one hydrogenase isoform, compared with a cited baseline of **26%** across archaeal and bacterial genomes. Hydrogenase abundance increased significantly with pH (**R²=0.31; p<0.001**). These are ecological genomic associations, not proof that every detected hydrogenase mediates growth-supporting H₂ oxidation. (colman2024themicrobialecology pages 21-24)

### Extracellular electrons as lithotrophic inputs

Electroautotrophy and mineral EEU extend the donor concept beyond dissolved molecules. Documented mechanisms include direct multiheme-cytochrome conduits, periplasmic electron relays, quinone-interacting complexes, and indirect shuttles. In studied sulfate reducers, electrode potentials ranged from approximately **−310 to −500 mV versus SHE**. Mechanistic diversity and the frequent reliance on electrochemical rather than pure-culture growth evidence remain major limitations. (gupta2020extracellularelectronuptake pages 5-6, gupta2020extracellularelectronuptake pages 9-10)

## Current applications and real-world relevance

1. **Nitrification and wastewater treatment.** Ammonia- and nitrite-oxidizing lithotrophs drive conversion of reduced nitrogen to nitrate. Process engineering manipulates oxygen, substrate loading, pH, solids retention, and inhibitors to favor complete or partial nitrification. AOA activity also bears on fertilizer nitrogen-use efficiency and N₂O emissions, but the trait graph should represent the underlying metabolism rather than downstream management claims.

2. **Biomining and mine-water management.** Iron- and sulfur-oxidizing lithotrophs mobilize metals from sulfide ores and influence acid generation. The pH/thiosulfate partitioning observed in 2024 suggests that manipulating donor availability and pH could steer mine-water sulfur speciation and acidity; this is promising management evidence, not yet a universal control rule. (twible2024phandthiosulfate pages 1-2)

3. **CO₂-based biomanufacturing.** Hydrogen-oxidizing lithoautotrophs such as *Cupriavidus necator* are engineered to convert H₂, CO₂, and O₂ into biomass, polyhydroxyalkanoates, fuels, and chemicals. Industrial implementation must address gas-transfer limitations and the explosive H₂/O₂ mixture hazard. Carbon fixation should be modeled downstream of lithotrophy because heterotrophic and mixotrophic operation is also possible.

4. **Microbial electrosynthesis.** Electroautotrophs can use cathodic electrons directly or indirectly—often through abiotically/electrochemically generated H₂—to reduce CO₂. Direct electron uptake must be distinguished from mediated hydrogenotrophy. Reviewed EEU organisms can persist where soluble donors are scarce and function as primary producers. (gupta2020extracellularelectronuptake pages 1-2)

5. **Deep-subsurface and astrobiology models.** H₂ generated by water–rock reactions can sustain primary production under dark, oligotrophic conditions. Serpentinite systems exhibit H₂-, CO-, sulfur-, sulfate-, Fe(III)-, and O₂-linked metabolic networks across reported pH values as high as **12.5**. Extrapolation from genes to in situ fluxes remains uncertain. (colman2024themicrobialecology pages 11-14, colman2024themicrobialecology pages 21-24)

## Expert synthesis

The strongest curation strategy is a **mechanistic hub-and-spoke graph**. The hub should contain only the abstract causal chain from inorganic donor oxidation to electron transfer, ion-gradient formation, and ATP synthesis. Spokes should encode donor-specific entry modules. Carbon fixation should be an optional consequence, never a definitional requirement.

This architecture reflects authoritative reviews showing that the same phenotype is achieved through evolutionarily and biochemically distinct systems. Even within one donor class, taxonomic variation is substantial: sulfur oxidation can use complete Sox, incomplete Sox plus rDsr, or S4I modules; hydrogen metabolism uses several hydrogenase classes; Fe(II) oxidation can involve Cyc2, MtoAB, PioAB, or incompletely characterized routes; and AOA should not be forced into the canonical bacterial AMO–HAO model. (gupta2020extracellularelectronuptake pages 8-9, colman2024themicrobialecology pages 21-24, wright2023nitrificationandbeyond pages 5-7, twible2024phandthiosulfate pages 1-2)

## Warnings: claims not yet ready for TraitMech

1. **Do not encode lithotrophic → autotrophic.** Carbon and electron sources are orthogonal.
2. **Do not infer phenotype from a single marker gene.** Hydrogenases can be H₂-producing, bidirectional, sensory, or energy-converting; Sox genes can be incomplete; Cyc2 homologues and multiheme cytochromes are not sufficient proof of Fe(II) oxidation or EEU.
3. **Do not universalize HAO downstream of AMO.** The AOA hydroxylamine/NO intermediates and electron-transfer chemistry remain incompletely resolved. (wright2023nitrificationandbeyond pages 5-7)
4. **Do not merge direct EEU with H₂-mediated cathodic growth.** Demonstrating current consumption does not establish the electron-transfer route.
5. **Do not use electrode as a universal inorganic chemical donor without an assay qualifier.** Electrode potential, material, mediators, abiotic H₂, and growth/carbon-assimilation controls are essential.
6. **Do not treat all sulfur compounds as interchangeable.** H₂S/HS⁻, S⁰, thiosulfate, sulfite, and tetrathionate enter different enzymes and yield different products.
7. **Do not curate pH associations as universal causal laws.** The 2024 pH partitioning was observed in specific mine-tailings communities. (twible2024phandthiosulfate pages 1-2)
8. **Do not add dark-O₂ production as a core lithotrophy mechanism.** Chlorite, nitric oxide, peroxide, and ammonia-linked O₂ generation are system-specific hypotheses or pathways and require direct evidence. (colman2024themicrobialecology pages 11-14)
9. **Do not assign periplasmic or outer-membrane nodes universally.** Cell-envelope architecture differs across Bacteria and Archaea.
10. **Validate every ontology identifier before YAML insertion.** CHEBI protonation state, EC reaction direction, taxon-specific UniProt accession, and GO term scope must match the cited experiment.

## DOI-first bibliography

1. **Twible LE et al.** “pH and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments.” *Frontiers in Microbiology* 15. Published July 2024. DOI: [10.3389/fmicb.2024.1426584](https://doi.org/10.3389/fmicb.2024.1426584). (twible2024phandthiosulfate pages 1-2)
2. **Colman DR, Templeton AS, Spear JR, Boyd ES.** “The Microbial Ecology of Serpentinites.” *bioRxiv*. Posted November 2024. DOI: [10.1101/2024.11.10.622848](https://doi.org/10.1101/2024.11.10.622848). **Preprint.** (colman2024themicrobialecology pages 11-14, colman2024themicrobialecology pages 21-24)
3. **Wright CL, Lehtovirta-Morley LE.** “Nitrification and beyond: metabolic versatility of ammonia oxidising archaea.” *The ISME Journal* 17:1358–1368. Published July 2023. DOI: [10.1038/s41396-023-01467-0](https://doi.org/10.1038/s41396-023-01467-0). (wright2023nitrificationandbeyond pages 5-7)
4. **Gupta D, Guzman MS, Bose A.** “Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications.” *Journal of Industrial Microbiology & Biotechnology* 47:863–876. Published October 2020. DOI: [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0). (gupta2020extracellularelectronuptake pages 8-9, gupta2020extracellularelectronuptake pages 5-6, gupta2020extracellularelectronuptake pages 9-10, gupta2020extracellularelectronuptake pages 1-2)
5. **Existing supplied evidence:** “Lithotrophy.” Encyclopedia chapter. DOI: [10.1016/B978-0-12-378630-2.00219-X](https://doi.org/10.1016/B978-0-12-378630-2.00219-X). Supports inorganic atoms or molecules as growth-supporting reductants and energy sources.
6. **Existing supplied evidence:** bioenergetics review. DOI: [10.1016/j.bbabio.2008.09.008](https://doi.org/10.1016/j.bbabio.2008.09.008). Supports respiratory generation of an electrochemical ion gradient and ATP synthesis.

## Recommended conservative YAML core

The first curation pass should add only the following abstract chain:

1. **“METPO:1000649” lithotrophic** — has defining input → **inorganic electron donor**  
2. **inorganic electron donor** — is oxidized by → **donor-specific oxidoreductase or electron conduit**  
3. **donor-specific oxidoreductase or conduit** — transfers electrons to → **electron transport system**  
4. **electron transport system** — generates → **electrochemical ion gradient**  
5. **electrochemical ion gradient** — powers → **ATP synthesis coupled ion transport**  
6. **ATP synthesis** — supports → **growth/maintenance**

Then add H₂/hydrogenase, sulfur/Sox, ammonia/AMO, nitrite/NXR, Fe(II)/Cyc2 or Mto/Pio, and EEU branches only where each edge has donor-specific experimental support. Carbon fixation, reverse electron transfer, terminal acceptors, and environmental controls should remain optional contextual subgraphs.

References

1. (gupta2020extracellularelectronuptake pages 1-2): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

2. (colman2024themicrobialecology pages 21-24): Daniel R. Colman, Alexis S. Templeton, John R. Spear, and Eric S. Boyd. The microbial ecology of serpentinites. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.10.622848, doi:10.1101/2024.11.10.622848. This article has 1 citations.

3. (gupta2020extracellularelectronuptake pages 5-6): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

4. (colman2024themicrobialecology pages 11-14): Daniel R. Colman, Alexis S. Templeton, John R. Spear, and Eric S. Boyd. The microbial ecology of serpentinites. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.10.622848, doi:10.1101/2024.11.10.622848. This article has 1 citations.

5. (twible2024phandthiosulfate pages 1-2): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 29 citations and is from a peer-reviewed journal.

6. (gupta2020extracellularelectronuptake pages 8-9): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

7. (wright2023nitrificationandbeyond pages 5-7): Chloe L Wright and Laura E Lehtovirta-Morley. Nitrification and beyond: metabolic versatility of ammonia oxidising archaea. The ISME Journal, 17:1358-1368, Jul 2023. URL: https://doi.org/10.1038/s41396-023-01467-0, doi:10.1038/s41396-023-01467-0. This article has 157 citations.

8. (gupta2020extracellularelectronuptake pages 3-3): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

9. (gupta2020extracellularelectronuptake pages 9-10): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.