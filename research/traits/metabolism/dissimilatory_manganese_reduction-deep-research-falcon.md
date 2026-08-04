---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:57:30.043474'
end_time: '2026-08-04T06:04:42.345438'
duration_seconds: 432.3
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory manganese reduction
  trait_identifier: traitmech:000108
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_manganese_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism conserves energy
    by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while
    oxidizing organic matter or hydrogen.
  parent_traits: traitmech:000039
  synonyms: Mn(IV) reduction
  evidence_summary: 'DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory
    Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide
    acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in
    anaerobic respiration as terminal electron acceptors.)'
  causal_graph_summary: 'dmr_mn_oxide_respiration: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory manganese reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000108
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while oxidizing organic matter or hydrogen.
- **Parent traits:** traitmech:000039
- **Synonyms:** Mn(IV) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in anaerobic respiration as terminal electron acceptors.)
- **Existing causal graph summary:** dmr_mn_oxide_respiration: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **dissimilatory manganese reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`.

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
- **Trait label:** dissimilatory manganese reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000108
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy by reducing Mn(IV) oxides to soluble Mn(II) as a terminal electron acceptor while oxidizing organic matter or hydrogen.
- **Parent traits:** traitmech:000039
- **Synonyms:** Mn(IV) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991:  (Lovley establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration on metal-oxide acceptors.) | PMID:7826009:  (Nealson & Saffarini review iron and manganese in anaerobic respiration as terminal electron acceptors.)
- **Existing causal graph summary:** dmr_mn_oxide_respiration: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **dissimilatory manganese reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`.

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


# Curation report: dissimilatory manganese reduction

## Trait record and scope

- **Trait label:** dissimilatory manganese reduction
- **Trait identifier:** `traitmech:000108`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000039`
- **Synonym:** Mn(IV) reduction

The trait should denote an **anaerobic, energy-conserving respiratory capacity** in which extracellular Mn(IV) oxide is used as the terminal electron acceptor while an organic compound or H₂ supplies electrons, with Mn(II) normally accumulating as the reduced product. Lovley’s operational definition was use of Mn(IV) as an external electron acceptor; Mn(II) is generally the endpoint, although Mn(III) can occur as an intermediate. Growth on the nonfermentable donor acetate coincident with Mn(IV) reduction and proton translocation with lactate/Mn(IV) provide physiological evidence that this can support energy conservation. (lovley1991dissimilatoryfe(iii)and pages 20-21, lovley1991dissimilatoryfe(iii)and pages 2-3)

### Boundaries

**Include** a phenotype when Mn(IV) reduction is linked to anaerobic electron transport and preferably to growth, increased biomass, proton translocation, ATP formation, or a donor/acceptor-dependent growth yield.

**Exclude or represent separately:**

1. **Assimilatory Mn reduction**, where manganese is reduced during incorporation into enzymes, cofactors, or cellular material. Dissimilatory reduction instead produces substantial extracellular Mn(II). (lovley1991dissimilatoryfe(iii)and pages 2-3)
2. **Mn(II) oxidation**, the reverse biogeochemical process.
3. **Incidental or detoxifying reduction** by aerobically grown/resting cells without evidence of energy conservation.
4. **Minor fermentative electron disposal.** Some fermenters transfer less than 5% of substrate reducing equivalents to Fe(III)/Mn(IV), with no demonstrated growth energy from metal reduction. (lovley1991dissimilatoryfe(iii)and pages 2-3)
5. **Indirect abiotic Mn(IV) reduction** by microbially produced Fe(II), sulfide, FeS, pyrite, sulfite, or other reductants. A rise in dissolved Mn alone therefore does not establish direct enzymatic respiration. (lovley1991dissimilatoryfe(iii)and pages 2-3, wunder2024manganesereductionand pages 6-7)
6. **Mn(III)-only respiration** unless the experiment establishes that Mn(III) is an intermediate or relevant Mn(IV)-oxide phase rather than a separate terminal acceptor.

## Candidate graph nodes

### Trait and process nodes

- Dissimilatory manganese reduction — `traitmech:000108`
- Anaerobic respiration — candidate `GO:0009061`
- Extracellular electron transfer — label-only pending ontology review
- Electron-transport-linked energy conservation — label-only
- Proton translocation / proton-motive-force generation — use an appropriate GO term only after confirming the intended granularity
- Organic-matter oxidation and mineralization — label-only at this graph granularity

### Chemicals and minerals

- Mn(IV) oxide / manganese dioxide — terminal electron acceptor; mineral phase should remain label-only unless the experimental form is known
- Birnessite — experimentally supplied Mn oxide; label-only mineral node
- Mn(II) — candidate `CHEBI:29035` (manganese(2+)); verify whether the graph intends the ion or total dissolved Mn
- Mn(III) — possible intermediate; do not make obligatory
- Acetate — candidate `CHEBI:30089`
- Lactate — stereochemistry varies; ground only when reported
- Formate — candidate `CHEBI:15740`
- Hydrogen — candidate `CHEBI:18276`
- Elemental sulfur, thiosulfate, sulfide — potential donors in some systems, but negative or inconclusive in the 2024 Potter Cove experiment
- Menaquinone-7 / menaquinol-7 and ubiquinone-8 — membrane electron carriers in *Shewanella*; exact CHEBI mappings should be registry-validated
- Flavins/FMN — extracellular shuttles or cytochrome-associated cofactors; not universally required
- Fe(II), FeS, pyrite and sulfide — confounders capable of abiotic Mn-oxide reduction
- AQDS — experimental electron shuttle; not intrinsic to the core trait

### Genes, proteins, and complexes

**Conservative *Shewanella* module:**

- NADH dehydrogenases, lactate dehydrogenases, formate dehydrogenases — donor oxidation and quinone reduction
- **CymA** — inner/cytoplasmic-membrane tetraheme c-type cytochrome; oxidizes membrane quinols and distributes electrons
- Periplasmic carriers, including **STC**, **FccA**, and **ScyA** — candidate intermediate carriers, but redundancy and Mn specificity remain unresolved
- **MtrA** — periplasm-facing decaheme cytochrome
- **MtrB** — outer-membrane β-barrel scaffold
- **MtrC** — extracellular/outer-surface decaheme cytochrome
- **OmcA** — outer-surface decaheme cytochrome with explicit Mn-respiration mutant evidence
- **MtrCAB/OmcA extended respiratory chain** — complex/module node

Protein identifiers should be added as **taxon-specific UniProt accessions**, not generic protein CURIEs, after the target strain is fixed. The literature summarized here concerns principally *Shewanella oneidensis* MR-1.

**Possible *Geobacter* nodes:** outer-surface multiheme c-type cytochromes and conductive extracellular filaments/pili. These belong in a taxon-specific extension, not the universal core: much of the detailed evidence concerns Fe(III) oxide or electrodes, and extracellular-electron-transfer components can be acceptor-specific. The review explicitly shows that cytochromes important for one acceptor may be dispensable for another. (richter2012dissimilatoryreductionof pages 4-5)

### Cellular localizations

- Cytoplasmic/inner membrane: quinone pool, CymA, donor dehydrogenases
- Periplasm: soluble c-type cytochrome carriers and MtrA-facing electron-transfer space
- Outer membrane: MtrB scaffold
- Cell exterior/outer surface: MtrC, OmcA, extracellular Mn oxide
- Extracellular space: insoluble Mn(IV) mineral and soluble/adsorbed Mn(II)

### Organisms and environments

- *Shewanella oneidensis* MR-1 — model facultative anaerobe; use strain-level NCBITaxon identifier only after registry verification
- GS-15, historically corresponding to *Geobacter metallireducens* — foundational acetate/Mn(IV) growth evidence; verify taxonomic identifier before curation
- *Desulfuromusa ferrireducens* and Antarctic *Desulfuromusa* ASV — Mn reduction evidence, but the 2024 environmental ASV is not an isolate
- *Desulfuromonas*, Sva1033/Desulfuromonadales, and Arcobacteraceae — associated taxa with differing evidence strengths
- Anoxic marine sediment, cold Antarctic sediment, and metal-oxide-rich sediment — environmental contexts
- Experimental factors: anoxia, 2°C, birnessite amendment, acetate amendment, 20-day slurry incubation, and dissolved-Mn assay

## Candidate causal edges

The following table is a conservative starting set; its confidence qualifiers should be retained in YAML evidence annotations.

| subject | predicate | object | confidence/qualifier | key evidence DOI |
|---|---|---|---|---|
| Mn(IV) oxide | is terminal electron acceptor in | dissimilatory manganese reduction yielding extracellular Mn(II) | High; trait-defining, broad but older review evidence; distinguish from assimilatory reduction and abiotic Mn oxide reduction (lovley1991dissimilatoryfe(iii)and pages 2-3, wunder2024manganesereductionand pages 6-7) | 10.1128/mr.55.2.259-287.1991 |
| acetate oxidation | can be coupled to | Mn(IV) oxide reduction | High for organotrophic coupling; broad review support and 2024 birnessite+acetate incubation support (wunder2024manganesereductionand pages 6-7, wunder2024manganesereductionand pages 3-4) | 10.1128/mr.55.2.259-287.1991; 10.3389/fmicb.2024.1398021 |
| lactate oxidation | can be coupled to | Mn(IV) oxide reduction | Moderate; broad review support, not universal across taxa (lovley1991dissimilatoryfe(iii)and pages 20-21, wunder2024manganesereductionand pages 1-2) | 10.1128/mr.55.2.259-287.1991; 10.3389/fmicb.2024.1398021 |
| dissimilatory Mn(IV) reduction | supports | anaerobic growth / energy conservation | High; GS-15 and S. putrefaciens evidence, including proton translocation; taxon-specific physiological evidence (lovley1991dissimilatoryfe(iii)and pages 20-21) | 10.1128/mr.55.2.259-287.1991 |
| menaquinone pool | donates electrons to | CymA | Moderate-High; Shewanella-specific respiratory-chain model, Mn-relevant because cymA mutant is affected in Mn oxide use (richter2012dissimilatoryreductionof pages 2-4, beblawy2018extracellularreductionof pages 4-6) | 10.1128/AEM.06803-11; 10.1111/mmi.14067 |
| CymA | is required for efficient use of | Mn oxide as electron acceptor | High; Shewanella-specific mutant phenotype (richter2012dissimilatoryreductionof pages 2-4, beblawy2018extracellularreductionof pages 4-6) | 10.1128/AEM.06803-11; 10.1111/mmi.14067 |
| MtrA | transfers electrons toward | MtrB/MtrC outer-membrane module | Moderate; Shewanella-specific topology inferred from pathway studies; not exclusively Mn-specific (richter2012dissimilatoryreductionof pages 4-5, beblawy2018extracellularreductionof pages 4-6) | 10.1128/AEM.06803-11; 10.1111/mmi.14067 |
| MtrB | connects | periplasmic MtrA to outer-membrane cytochromes MtrC/OmcA | Moderate; Shewanella-specific topology, broadly EET-oriented with Mn relevance (richter2012dissimilatoryreductionof pages 4-5, beblawy2018extracellularreductionof pages 4-6) | 10.1128/AEM.06803-11; 10.1111/mmi.14067 |
| MtrC | transfers electrons to | OmcA / external Mn(IV) oxide | Moderate; Shewanella-specific model, Mn-relevant but partly inferred from general extracellular electron transfer data (richter2012dissimilatoryreductionof pages 4-5) | 10.1128/AEM.06803-11 |
| OmcA | contributes to | manganese respiration | High; Shewanella-specific mutant evidence explicitly notes negative effect in manganese respiration (richter2012dissimilatoryreductionof pages 4-5) | 10.1128/AEM.06803-11 |
| birnessite + acetate amendment | increases | dissolved Mn to ~600 uM after 20 days | High; 2024 Antarctic slurry incubation-specific (wunder2024manganesereductionand pages 6-7, wunder2024manganesereductionand pages 3-4) | 10.3389/fmicb.2024.1398021 |
| birnessite + acetate amendment | stimulates | Desulfuromusa growth/activity | High; 2024 Antarctic slurry incubation-specific, strongest taxon association with Mn reduction signal (wunder2024manganesereductionand pages 4-6, wunder2024manganesereductionand pages 7-9) | 10.3389/fmicb.2024.1398021 |
| Desulfuromusa enrichment under birnessite + acetate | correlates with | peak dissolved Mn production | High; incubation-specific correlation, not yet pure-culture mechanism (wunder2024manganesereductionand pages 4-6, wunder2024manganesereductionand pages 7-9) | 10.3389/fmicb.2024.1398021 |


*Table: This table summarizes the strongest curation-ready causal edges for traitmech:000108, emphasizing core physiology, Shewanella-specific electron-transfer components, and the most informative 2024 incubation evidence from Antarctic sediments. It is useful for selecting conservative graph edges while clearly flagging taxon-specific and assay-specific claims.*

### Additional evidence notes and supporting snippets

1. **Mn(IV) oxide → terminal electron acceptor in → dissimilatory manganese reduction.** Supporting text: “Dissimilatory Fe(III) or Mn(IV) reduction can be defined as the use of Fe(III) or Mn(IV) as an external electron acceptor in metabolism.” The same source states that “Mn(II) is generally regarded as the end product,” with Mn(III) sometimes intermediate. This is the strongest trait-defining edge. (lovley1991dissimilatoryfe(iii)and pages 2-3)

2. **Mn(IV) reduction → supports → anaerobic growth/energy conservation.** Supporting text: “Growth of GS-15 on acetate, a nonfermentable substrate, coincide[d] with Mn(IV) reduction,” indicating that electron transport yielded energy for growth. In *S. putrefaciens* MR-1, “Proton translocation was observed” with lactate donor and Mn(IV) acceptor. The edge is robust as a trait-level concept, although the experiments are taxon-specific. (lovley1991dissimilatoryfe(iii)and pages 20-21)

3. **Donor oxidation → supplies electrons to → Mn(IV) reduction.** Current literature recognizes lactate, acetate, formate, and hydrogen as donors; reduced sulfur compounds can operate in some environments. In the 2024 Antarctic experiment, however, elemental sulfur and thiosulfate did not produce a statistically distinguishable Mn response from the birnessite control, so those donor edges should not be generalized. (wunder2024manganesereductionand pages 6-7, wunder2024manganesereductionand pages 1-2)

4. **Menaquinol pool → transfers electrons through → CymA.** In *S. oneidensis*, electrons move from the menaquinol pool to the periplasm through tetraheme CymA. CymA is a respiratory branch point, and a `cymA` deletion impairs use of manganese oxides as electron acceptors. This is strong *Shewanella*-specific support, not a universal Mn-reducer mechanism. (richter2012dissimilatoryreductionof pages 2-4)

5. **MtrA/MtrB/MtrC/OmcA → conducts extracellular electron transfer to → Mn oxide.** The proposed topology is CymA/periplasmic carriers → MtrA → MtrB-associated MtrC → OmcA/solid acceptor. The review characterizes this topology as plausible and notes that OmcA may receive electrons through MtrC, MtrB, and MtrA. Because parts of the topology derive from Fe-oxide/electrode studies, curate it as a *Shewanella* mechanistic model rather than an invariant Mn pathway. (richter2012dissimilatoryreductionof pages 4-5, beblawy2018extracellularreductionof pages 4-6)

6. **OmcA → contributes to → manganese respiration.** This is among the best Mn-specific protein edges: an `omcA` mutant was “negatively affected in manganese respiration,” and OmcA could rescue an outer-membrane-cytochrome-deficient mutant under Mn-reducing conditions. (richter2012dissimilatoryreductionof pages 4-5, richter2012dissimilatoryreductionof pages 2-4)

## Recent research and quantitative evidence

The strongest retrieved 2023–2024 contribution was Wunder et al., published **3 July 2024**, examining Potter Cove, West Antarctica. Under anoxic slurry conditions at **2°C**, birnessite produced **300–600 µM dissolved Mn**, whereas controls lacking manganese oxide remained below **10 µM**. The acetate-plus-birnessite treatment was the only donor amendment with a significant effect and reached approximately **600 µM after 20 days**. In situ dissolved Mn increased to **20–50 µM** in the sampled cores; older nearby profiles reached 100–200 µM. (wunder2024manganesereductionand pages 6-7, wunder2024manganesereductionand pages 3-4)

*Desulfuromusa* responded specifically to combined acetate and birnessite, reaching approximately **15% of 16S rRNA** and **7% of 16S rRNA genes** after 20 days versus generally below 0.5% in controls. Its abundance increased approximately **50-fold**, coincident with maximum dissolved Mn. The closest cultured relative was *D. bakii* at 99.6% 16S identity, but manganese-oxide use had previously been demonstrated only for *D. ferrireducens*. Thus, the environmental taxon–trait connection is strong but not equivalent to a pure-culture gene-level mechanism. (wunder2024manganesereductionand pages 7-9, wunder2024manganesereductionand pages 4-6)

The study also illustrates ecological scale: Mn reduction may contribute up to **45% of carbon mineralization** in Mn-oxide-rich sediments, while Potter Cove solid Mn oxide was approximately **20 µmol cm⁻³** through the sampled core. Previously studied Mn-rich sites contained about **200–600 µmol cm⁻³**. These numbers support ecological importance but should not be encoded as universal trait thresholds. (wunder2024manganesereductionand pages 7-9, wunder2024manganesereductionand pages 1-2)

## Applications and real-world relevance

1. **Carbon and manganese cycling.** Mn reducers couple anaerobic organic-matter oxidation to mineral dissolution and influence carbon mineralization, pore-water Mn export, and linked Fe/S cycles. The Antarctic evidence suggests this remains active in permanently cold, glacier-influenced sediment. (wunder2024manganesereductionand pages 6-7, wunder2024manganesereductionand pages 1-2)
2. **Bioremediation and contaminant transformation.** Metal-reducing extracellular-electron-transfer systems can alter mineral sorption capacity and contaminant speciation. These are pathway-level applications; they do not show that every application specifically depends on Mn respiration.
3. **Biomining and Mn-oxide dissolution.** Anaerobic microbial reduction can mobilize Mn(II) from oxide ores or wastes. Process claims require reactor-specific evidence and should not be part of the biological core graph.
4. **Bioelectrochemical engineering.** The *Shewanella* Mtr pathway is used to engineer electron exchange with electrodes and nanoparticle synthesis. Electrode reduction is mechanistically informative but is not evidence by itself for Mn(IV) respiration.
5. **Environmental monitoring.** Dissolved Mn profiles plus donor/acceptor amendments and RNA/DNA community responses can identify likely Mn-reducing zones. Dissolved Mn is not a direct rate measurement because Mn²⁺ can adsorb or precipitate as MnCO₃ or MnS. (wunder2024manganesereductionand pages 6-7)

## Recommended minimal TraitMech graph

A conservative seven-node core consistent with the existing graph size is:

1. Electron donor oxidation
2. Membrane quinone pool
3. CymA
4. MtrA–MtrB–MtrC/OmcA extracellular-electron-transfer module
5. Extracellular Mn(IV) oxide
6. Mn(II)
7. Anaerobic growth/energy conservation

Recommended directional chain:

**electron-donor oxidation → reduces quinone pool → donates electrons to CymA → transfers electrons through Mtr/EET module → reduces extracellular Mn(IV) oxide → produces Mn(II); Mn(IV)-linked electron transport → supports anaerobic growth/energy conservation.**

This compact graph is **explicitly *Shewanella*-anchored** at the protein level. For a taxon-neutral trait graph, collapse nodes 2–4 into “extracellular respiratory electron-transfer chain” and place the named proteins in a taxon-specific mechanism variant.

## Warnings: claims not yet ready for curation

- Do not assert that **MtrCAB/OmcA is universal** among Mn reducers.
- Do not assign a single universal “Mn(IV) reductase”; multiheme cytochromes are frequently promiscuous and partially redundant.
- Do not infer Mn respiration from an **Mtr-like gene cluster alone** without phenotype or expression/genetic evidence.
- Do not curate **Geobacter OmcS/OmcZ or conductive pili as obligatory Mn-reduction components** from Fe-oxide/electrode evidence.
- Do not treat flavins, AQDS, pili, nanowires, or outer-membrane vesicles as required core components.
- Do not infer direct microbial reduction from dissolved Mn accumulation without excluding Fe(II)-, sulfide-, FeS-, or pyrite-driven abiotic reduction. (wunder2024manganesereductionand pages 6-7)
- Do not interpret 16S enrichment as proof of the responsible enzyme. The 2024 *Desulfuromusa* result is a donor/acceptor-dependent ecological association, not gene-level causality. (wunder2024manganesereductionand pages 7-9, wunder2024manganesereductionand pages 4-6)
- Do not encode 20 µmol cm⁻³ Mn oxide, 2°C, or 20 days as universal trait requirements; these are site or assay parameters.
- Verify all CHEBI, GO, NCBITaxon, and UniProt mappings against their current registries before committing YAML. Label-only nodes are preferable to uncertain identifiers.

## DOI-first bibliography

1. Lovley DR. **Dissimilatory Fe(III) and Mn(IV) reduction.** *Microbiological Reviews*. Published June 1991. DOI: [10.1128/mr.55.2.259-287.1991](https://doi.org/10.1128/mr.55.2.259-287.1991). Foundational definition, physiology, growth, inhibitors, and boundary cases. (lovley1991dissimilatoryfe(iii)and pages 20-21, lovley1991dissimilatoryfe(iii)and pages 2-3)
2. Wunder LC et al. **Manganese reduction and associated microbial communities in Antarctic surface sediments.** *Frontiers in Microbiology*. Published 3 July 2024. DOI: [10.3389/fmicb.2024.1398021](https://doi.org/10.3389/fmicb.2024.1398021). Recent environmental and quantitative evidence. (wunder2024manganesereductionand pages 6-7, wunder2024manganesereductionand pages 1-2, wunder2024manganesereductionand pages 4-6, wunder2024manganesereductionand pages 3-4)
3. Richter K, Schicklberger M, Gescher J. **Dissimilatory Reduction of Extracellular Electron Acceptors in Anaerobic Respiration.** *Applied and Environmental Microbiology*. Published February 2012. DOI: [10.1128/AEM.06803-11](https://doi.org/10.1128/AEM.06803-11). Comparative EET mechanisms and Mn-specific mutant evidence. (richter2012dissimilatoryreductionof pages 4-5, richter2012dissimilatoryreductionof pages 2-4)
4. Beblawy S et al. **Extracellular reduction of solid electron acceptors by Shewanella oneidensis.** *Molecular Microbiology*. Published July 2018. DOI: [10.1111/mmi.14067](https://doi.org/10.1111/mmi.14067). Donor oxidation, quinones, CymA, and extended respiratory-chain framework. (beblawy2018extracellularreductionof pages 4-6)

The evidence supports a robust physiological core—**donor oxidation coupled through extracellular electron transfer to Mn(IV)-oxide reduction, Mn(II) production, and energy conservation**—but only a taxon-specific molecular implementation is presently defensible. The YAML should therefore distinguish the universal trait-level chain from the better-resolved *Shewanella* mechanism and the assay-specific 2024 *Desulfuromusa* ecological evidence.

References

1. (lovley1991dissimilatoryfe(iii)and pages 20-21): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2594 citations.

2. (lovley1991dissimilatoryfe(iii)and pages 2-3): D R Lovley. Dissimilatory fe(iii) and mn(iv) reduction. Microbiological Reviews, 55:259-287, Jun 1991. URL: https://doi.org/10.1128/mr.55.2.259-287.1991, doi:10.1128/mr.55.2.259-287.1991. This article has 2594 citations.

3. (wunder2024manganesereductionand pages 6-7): Lea C. Wunder, Inga Breuer, Graciana Willis-Poratti, David A. Aromokeye, Susann Henkel, Tim Richter-Heitmann, Xiuran Yin, and Michael W. Friedrich. Manganese reduction and associated microbial communities in antarctic surface sediments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1398021, doi:10.3389/fmicb.2024.1398021. This article has 13 citations and is from a peer-reviewed journal.

4. (richter2012dissimilatoryreductionof pages 4-5): Katrin Richter, Marcus Schicklberger, and Johannes Gescher. Dissimilatory reduction of extracellular electron acceptors in anaerobic respiration. Applied and Environmental Microbiology, 78:913-921, Feb 2012. URL: https://doi.org/10.1128/aem.06803-11, doi:10.1128/aem.06803-11. This article has 356 citations and is from a peer-reviewed journal.

5. (wunder2024manganesereductionand pages 3-4): Lea C. Wunder, Inga Breuer, Graciana Willis-Poratti, David A. Aromokeye, Susann Henkel, Tim Richter-Heitmann, Xiuran Yin, and Michael W. Friedrich. Manganese reduction and associated microbial communities in antarctic surface sediments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1398021, doi:10.3389/fmicb.2024.1398021. This article has 13 citations and is from a peer-reviewed journal.

6. (wunder2024manganesereductionand pages 1-2): Lea C. Wunder, Inga Breuer, Graciana Willis-Poratti, David A. Aromokeye, Susann Henkel, Tim Richter-Heitmann, Xiuran Yin, and Michael W. Friedrich. Manganese reduction and associated microbial communities in antarctic surface sediments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1398021, doi:10.3389/fmicb.2024.1398021. This article has 13 citations and is from a peer-reviewed journal.

7. (richter2012dissimilatoryreductionof pages 2-4): Katrin Richter, Marcus Schicklberger, and Johannes Gescher. Dissimilatory reduction of extracellular electron acceptors in anaerobic respiration. Applied and Environmental Microbiology, 78:913-921, Feb 2012. URL: https://doi.org/10.1128/aem.06803-11, doi:10.1128/aem.06803-11. This article has 356 citations and is from a peer-reviewed journal.

8. (beblawy2018extracellularreductionof pages 4-6): Sebastian Beblawy, Thea Bursac, Catarina Paquete, Ricardo Louro, Thomas A. Clarke, and Johannes Gescher. Extracellular reduction of solid electron acceptors by shewanella oneidensis. Molecular Microbiology, 109:571-583, Jul 2018. URL: https://doi.org/10.1111/mmi.14067, doi:10.1111/mmi.14067. This article has 141 citations and is from a domain leading peer-reviewed journal.

9. (wunder2024manganesereductionand pages 4-6): Lea C. Wunder, Inga Breuer, Graciana Willis-Poratti, David A. Aromokeye, Susann Henkel, Tim Richter-Heitmann, Xiuran Yin, and Michael W. Friedrich. Manganese reduction and associated microbial communities in antarctic surface sediments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1398021, doi:10.3389/fmicb.2024.1398021. This article has 13 citations and is from a peer-reviewed journal.

10. (wunder2024manganesereductionand pages 7-9): Lea C. Wunder, Inga Breuer, Graciana Willis-Poratti, David A. Aromokeye, Susann Henkel, Tim Richter-Heitmann, Xiuran Yin, and Michael W. Friedrich. Manganese reduction and associated microbial communities in antarctic surface sediments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1398021, doi:10.3389/fmicb.2024.1398021. This article has 13 citations and is from a peer-reviewed journal.