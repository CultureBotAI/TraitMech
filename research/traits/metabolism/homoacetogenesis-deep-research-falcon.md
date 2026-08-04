---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:16:21.995950'
end_time: '2026-08-04T06:24:16.374296'
duration_seconds: 474.38
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Homoacetogenesis
  trait_identifier: METPO:1000846
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: homoacetogenesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which acetate is produced as the sole reduced end product
    from reduction of CO2 via the acetyl-CoA pathway.
  parent_traits: METPO:1000060
  synonyms: Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
  evidence_summary: 'DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide
    are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction
    of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl
    Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway
    for CO2 fixation.)'
  causal_graph_summary: 'homoacetogenesis_wood_ljungdahl_acetate: 21 nodes, 20 edges'
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
- **Trait label:** Homoacetogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000846
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which acetate is produced as the sole reduced end product from reduction of CO2 via the acetyl-CoA pathway.
- **Parent traits:** METPO:1000060
- **Synonyms:** Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
- **Existing evidence:** DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway for CO2 fixation.)
- **Existing causal graph summary:** homoacetogenesis_wood_ljungdahl_acetate: 21 nodes, 20 edges

## Research Objective

Research the microbial trait **Homoacetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/homoacetogenesis.yaml`.

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
- **Trait label:** Homoacetogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000846
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which acetate is produced as the sole reduced end product from reduction of CO2 via the acetyl-CoA pathway.
- **Parent traits:** METPO:1000060
- **Synonyms:** Reductive acetyl-CoA pathway, Wood-Ljungdahl pathway
- **Existing evidence:** DOI:10.1016/j.tibtech.2019.05.008: two mol of carbon dioxide are reduced to one mol of acetyl-CoA (Review supports Wood-Ljungdahl reduction of CO2 to acetyl-CoA and acetate.) | DOI:10.1016/j.bbapap.2008.08.012: Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogens using the Wood-Ljungdahl pathway for CO2 fixation.)
- **Existing causal graph summary:** homoacetogenesis_wood_ljungdahl_acetate: 21 nodes, 20 edges

## Research Objective

Research the microbial trait **Homoacetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/homoacetogenesis.yaml`.

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


# Homoacetogenesis (`METPO:1000846`): TraitMech curation report

## Executive curation recommendation

Homoacetogenesis should represent the **physiological capacity for reductive acetogenesis in which CO₂ is reduced through the Wood–Ljungdahl pathway (WLP) and acetate is the sole or principal reduced end product**. For autotrophic growth on H₂/CO₂, the canonical reaction is:

**2 CO₂ + 4 H₂ → CH₃COO⁻ + H⁺ + 2 H₂O**

A focused review reports ΔG°′ ≈ **−105 kJ mol⁻¹ acetate**, whereas under low-H₂ environmental conditions the available free energy may fall below approximately **−20 kJ mol⁻¹**, close to the energetic limit of microbial life. Thus, standard-state thermodynamics must not be interpreted as the energy actually available in situ. (karekar2022homoacetogenstheirmetabolism pages 1-3, baum2024theenergyconvertinghydrogenase pages 1-2)

The trait should **not** be assigned from an `acs`/`codh` gene, a partial WLP, acetate production, or even a complete WLP alone. Required evidence should ideally include growth or substrate-conversion experiments under anoxic conditions, CO₂ incorporation into acetate, and/or a mechanistically diagnostic perturbation. WLP enzymes also support assimilation, acetate oxidation, methanogenesis, and redox balancing in nonclassical organisms. (ragsdale2008enzymologyofthe pages 1-2, gencic2020diverseenergyconservingpathways pages 1-4, jiao2024cultivationofnovel pages 1-2)

## 1. Scope and boundaries

### Included phenotype

The core phenotype comprises:

1. anaerobic reduction of CO₂ through the reductive acetyl-CoA/Wood–Ljungdahl pathway;
2. convergence of a methyl branch and carbonyl branch at CODH/ACS;
3. production of acetyl-CoA and then acetate as the sole or predominant reduced product;
4. use of H₂, CO, formate, or substrate-derived reducing equivalents, depending on organism and growth condition;
5. bioenergetic coupling through a taxon-dependent Rnf- or Ech-type membrane system because the WLP-to-acetate sequence is substrate-level ATP-neutral. (basen2023editorialacetogens pages 1-2, karekar2022homoacetogenstheirmetabolism pages 1-3, baum2024theenergyconvertinghydrogenase pages 1-2)

Classical acetogens are strict anaerobic bacteria, but they are phylogenetically polyphyletic and occupy soils, sediments, extreme environments, and animal gastrointestinal tracts. The trait is therefore metabolic rather than taxonomic. (basen2023editorialacetogens pages 1-2, karekar2022homoacetogenstheirmetabolism pages 1-3, ragsdale2008enzymologyofthe pages 1-2)

### Boundary cases and exclusions

- **Broad “acetogenesis”:** acetate production by ordinary sugar fermentation is insufficient. Homoacetogenesis specifically requires reductive CO₂ incorporation through the WLP.
- **Assimilatory WLP:** methanogens, sulfate reducers, and other anaerobes can use WLP chemistry for cell-carbon synthesis without exhibiting the target phenotype. (ragsdale2008enzymologyofthe pages 1-2)
- **Reverse WLP/syntrophic acetate oxidation:** this consumes acetate and generates CO₂, the opposite trait direction. Acetate-utilizing methanogens can run relevant reactions in reverse. (ragsdale2008enzymologyofthe pages 1-2)
- **Methanogenesis:** hydrogenotrophic methanogens also consume H₂ and CO₂ but reduce carbon to methane rather than acetate. They commonly outcompete homoacetogens thermodynamically at low H₂, although environmental conditions such as high CO₂ can shift competition. (basen2023editorialacetogens pages 1-2, karekar2022homoacetogenstheirmetabolism pages 1-3)
- **Nonclassical WLP use:** in *Clostridioides difficile*, Δ`acsB`, enzyme assays, and product analyses showed that WLP flux disposes of carbohydrate-derived reducing equivalents and couples to butyrate formation; this is not automatically classical homoacetogenesis. (gencic2020diverseenergyconservingpathways pages 1-4)
- **Partial pathway or isolated modules:** 2024 comparative genomics found that Atribacterota lack a complete WLP even though some possess `acsABCDE`, hydrogenases, or reductive-glycine-pathway genes and produce acetate during fermentation. These observations do not establish homoacetogenesis. (jiao2024cultivationofnovel pages 1-2)

## 2. Candidate nodes grouped by type

Ontology identifiers below are deliberately conservative. Label-only nodes are preferable to uncertain or invented CURIEs.

### Trait and pathway nodes

| Candidate node | Suggested grounding | Curation comment |
|---|---|---|
| Homoacetogenesis | `METPO:1000846` | Quote verbatim in YAML. Reviewed class; parent supplied as `METPO:1000060`. |
| Wood–Ljungdahl pathway | Label; optionally map after pathway-database verification | Synonyms: reductive acetyl-CoA pathway, reductive acetyl-CoA pathway/WLP. |
| Methyl branch of WLP | Label-only | CO₂/formate to methyl-tetrahydrofolate and methyl-CoFeSP. |
| Carbonyl branch of WLP | Label-only | CO₂ to enzyme-bound CO. |
| Chemiosmotic energy conservation | `GO:0015988` candidate | Verify exact intended GO scope before committing. |
| ATP synthesis coupled to ion gradient | `GO:0015986` candidate | General process node; Na⁺ versus H⁺ is organism-specific. |

### Genes, proteins, enzymes, and complexes

| Node | Common gene labels | Suggested grounding/comment |
|---|---|---|
| Formate dehydrogenase / hydrogen-dependent CO₂ reductase | `fdh`, `fdhF`, `hdcr` subunits | Multiple non-orthologous systems; curate by species-specific complex rather than one universal gene. |
| Formate–tetrahydrofolate ligase | `fhs` | `EC:6.3.4.3` candidate. Consumes ATP during formate activation. |
| Methenyl-THF cyclohydrolase / methylene-THF dehydrogenase | often `folD` | Cofactor specificity and protein architecture vary. |
| Methylene-THF reductase | `metF`, frequently complex-associated | `EC:1.5.1.20` candidate; electron-bifurcating implementations are taxon-specific. |
| Methyltransferase | `acsE` | Transfers methyl group to corrinoid Fe–S protein. |
| Corrinoid iron–sulfur protein | `acsC`, `acsD` | Cobalamin-containing methyl carrier; subunit naming varies. |
| Carbon monoxide dehydrogenase | commonly `acsA`/`cooS` | `EC:1.2.7.4` candidate; distinguish anabolic/monofunctional homologs. |
| Acetyl-CoA synthase | commonly `acsB` | Catalytic core of CODH/ACS; gene name must not be confused with AMP-forming acetyl-CoA synthetase. |
| CODH/ACS complex | `acsABCDE`-type cluster | Strong pathway-defining module, but insufficient alone to infer phenotype. |
| Phosphotransacetylase | `pta` | `EC:2.3.1.8` candidate. |
| Acetate kinase | `ackA` | `EC:2.7.2.1` candidate. |
| Electron-bifurcating hydrogenase | `hydABC(D)` | Soluble source of NAD(P)H and reduced ferredoxin; composition varies. |
| Rnf complex | `rnfCDGEAB` or variants | Ion-translocating ferredoxin:NAD⁺ oxidoreductase; Na⁺ or H⁺ coupling is taxon-specific. |
| Ech complex | `ech` cluster | Energy-converting hydrogenase; an alternative to Rnf in characterized acetogens. |
| F₁F₀ ATP synthase | `atp` operon | Converts ion motive force to ATP; ion specificity must be experimentally supported. |
| Ferredoxin | multiple genes | Low-potential electron carrier; no single universal locus. |

### Chemicals and redox carriers

High-confidence candidates include carbon dioxide (`CHEBI:16526`), dihydrogen (`CHEBI:18276`), carbon monoxide (`CHEBI:17245`), formate (`CHEBI:15740`), acetate (`CHEBI:30089`), acetyl-CoA (`CHEBI:15351`), coenzyme A (`CHEBI:15346`), ATP (`CHEBI:15422`), ADP (`CHEBI:16761`), NAD⁺ (`CHEBI:15846`), NADH (`CHEBI:16908`), sodium ion (`CHEBI:29101`), and proton (`CHEBI:15378`). Tetrahydrofolate-bound intermediates, reduced ferredoxin, corrinoid-bound methyl, and enzyme-bound CO should be added only after confirming the precise ontology form required by the graph schema.

### Environmental, cellular, and assay nodes

- anoxic/anaerobic environment—ENVO mapping should be verified against the intended habitat versus quality distinction;
- high versus low H₂ partial pressure;
- CO₂ availability and gas–liquid mass transfer;
- temperature, including thermophilic operation;
- cytoplasm, where soluble WLP reactions occur;
- cytoplasmic membrane, containing Rnf/Ech and ATP synthase;
- gas-fermentation bioreactor and microbial-electrosynthesis reactor as application contexts;
- growth on H₂/CO₂ or CO;
- acetate quantification by HPLC/GC;
- isotope tracing from ¹³CO₂ into acetate;
- gene deletion/complementation;
- membrane-potential, ion-translocation, ATP, and enzyme-activity assays.

## 3. Candidate causal edges

The following table is deliberately more granular than the existing 21-node/20-edge summary. “Core” edges are broadly suitable for the trait graph; “contextual” edges should carry taxon or assay qualifiers.

| # | Subject — predicate — object | Reference | Supporting snippet | Curation note |
|---:|---|---|---|---|
| 1 | H₂ + CO₂ — **is converted by** — homoacetogenesis to acetate | DOI:10.3390/microorganisms10020397 | “4 H₂ molecules and 2 CO₂ molecules, yielding acetate” | **Core.** Canonical autotrophic reaction; include charge-balanced form in machine-readable reaction. (karekar2022homoacetogenstheirmetabolism pages 1-3) |
| 2 | Homoacetogenesis — **requires** — anaerobic conditions | DOI:10.3389/fmicb.2023.1186930 | Acetogens are described as “strict anaerobic bacteria” using the WLP. | **Core**, while acknowledging oxygen tolerance differs among strains. (basen2023editorialacetogens pages 1-2) |
| 3 | H₂ — **donates electrons to** — CO₂ reduction | DOI:10.1196/annals.1419.015 | “When acetogens grow on H₂/CO₂…H₂ [serves] as the electron donor.” | **Core for H₂-dependent phenotype**, not obligatory for CO- or formate-dependent acetogenesis. (ragsdale2008enzymologyofthe pages 1-2) |
| 4 | WLP — **reduces and condenses** — two CO₂ to acetyl-CoA | DOI:10.3389/fmicb.2023.1186930 | “two molecules of carbon dioxide…are reduced and condensed to one molecule of acetyl-CoA.” | **Core.** (basen2023editorialacetogens pages 1-2) |
| 5 | Methyl branch — **reduces** — CO₂ to formate and methyl-CoFeSP | DOI:10.3390/microorganisms10020397 | The western branch “reduces CO₂ to formate then to methyl-CoFeSP.” | **Core**, but branch nomenclature differs among sources; prefer functional labels. (karekar2022homoacetogenstheirmetabolism pages 1-3) |
| 6 | HDCR — **catalyzes** — CO₂ → formate | DOI:10.1128/spectrum.03380-23 | HDCR “directly reduces CO₂ to formate in the first step of the methyl branch.” | **Contextual: *Acetobacterium woodii* and organisms with homologous HDCR.** Do not make universal. (baum2024theenergyconvertinghydrogenase pages 1-2) |
| 7 | Formate activation — **consumes** — ATP | DOI:10.1128/spectrum.03380-23 | “one ATP must be invested to bind formate to tetrahydrofolate.” | **Core pathway-level edge.** (baum2024theenergyconvertinghydrogenase pages 1-2) |
| 8 | Carbonyl branch/CODH — **reduces** — CO₂ to enzyme-bound CO | DOI:10.3390/microorganisms10020397 | The eastern branch “reduces CO₂ to CO.” | **Core chemistry**; source branch naming conflicts with other conventions, so avoid eastern/western names in YAML. (karekar2022homoacetogenstheirmetabolism pages 1-3) |
| 9 | CODH/ACS — **combines** — methyl carrier, CO, and CoA into acetyl-CoA | DOI:10.3390/microorganisms10020397 | “Both branches converge at acetyl-CoA synthase,” producing acetyl-CoA. | **Core.** Represent substrates individually if graph schema supports n-ary reactions. (karekar2022homoacetogenstheirmetabolism pages 1-3) |
| 10 | Acetyl-CoA — **is converted through acetyl-phosphate to** — acetate | DOI:10.3389/fmicb.2023.1186930 | Acetyl-CoA “is converted to acetate via acetyl-phosphate.” | **Core.** Add Pta and Ack only where genes/activities are supported. (basen2023editorialacetogens pages 1-2) |
| 11 | Acetate kinase reaction — **produces/reclaims** — ATP | DOI:10.1128/spectrum.03380-23 | ATP invested in formate activation “is reclaimed in the acetate kinase reaction.” | **Core.** (baum2024theenergyconvertinghydrogenase pages 1-2) |
| 12 | WLP plus acetate formation — **has net substrate-level yield of** — approximately zero ATP | DOI:10.3389/fmicb.2023.1186930 | “one ATP consumed…one generated from acetate synthesis.” | **Core bioenergetic constraint.** Distinguish from total ATP conserved chemiosmotically. (basen2023editorialacetogens pages 1-2) |
| 13 | Reduced ferredoxin oxidation by Rnf — **drives** — transmembrane ion gradient | DOI:10.1128/JB.00357-18 | Rnf oxidizes reduced ferredoxin, reduces NAD⁺, and uses the free-energy change to generate an ion gradient. | **Contextual Rnf-type edge with direct experimental support.** (westphal2018thernfcomplex pages 1-2) |
| 14 | Rnf-dependent ion gradient — **drives** — ATP synthesis | DOI:10.3390/microorganisms9020258 | *C. aceticum* uses Na⁺-Rnf and Na⁺-F₁F₀ ATP synthase. | **Taxon-specific:** sodium coupling must not be generalized to all acetogens. (wiechmann2021energyconservationin pages 8-11) |
| 15 | `rnf` deletion — **abolishes** — H₂/CO₂ growth, acetate production, ATP production, Na⁺ translocation | DOI:10.1128/JB.00357-18 | The mutant “did not grow on H₂ plus CO₂, nor did it produce acetate or ATP,” and Na⁺ translocation was lost. | **Strong causal edge; *A. woodii*-specific.** Suitable as high-confidence mechanistic evidence. (westphal2018thernfcomplex pages 1-2) |
| 16 | Ech — **couples** — ferredoxin oxidation/proton reduction to proton-gradient formation | DOI:10.1128/spectrum.03380-23 | Ech couples Fd-dependent proton reduction to H₂ with formation of a proton gradient. | **Contextual Ech-type alternative**, not co-required with Rnf. (baum2024theenergyconvertinghydrogenase pages 1-2) |
| 17 | `ech2` deletion — **impairs** — growth on CO and acetate formation from CO | DOI:10.1128/spectrum.03380-23 | Δ`ech2` “did not adapt to CO”; cell suspensions produced “no acetate…from CO.” | **Strong 2024 causal evidence**, but not a universal homoacetogenesis edge. (baum2024theenergyconvertinghydrogenase pages 1-2) |
| 18 | `ech2` deletion — **does not abolish** — H₂/CO₂ growth | DOI:10.1128/spectrum.03380-23 | The mutant “grew as fast as the wild type…on H₂ + CO₂.” | **Critical negative edge:** prevents incorrect assertion that Ech2 alone is essential; Ech1 or another enzyme compensates. (baum2024theenergyconvertinghydrogenase pages 1-2) |
| 19 | Homoacetogens — **compete with** — hydrogenotrophic methanogens for H₂/CO₂ | DOI:10.3390/microorganisms10020397 | Review evaluates homoacetogens as competing H₂ scavengers and potential methane-diversion organisms. | **Ecological contextual edge.** Outcome depends on thermodynamics, mass transfer, community, and inhibitors. (karekar2022homoacetogenstheirmetabolism pages 1-3) |
| 20 | Complete WLP gene set — **does not necessarily imply** — classical homoacetogenesis | DOI:10.1128/JB.00233-20 | In *C. difficile*, WLP “functions to dispose of metabolically-generated reducing equivalents.” | **Core exclusion/quality-control rule.** (gencic2020diverseenergyconservingpathways pages 1-4) |
| 21 | Partial WLP or `acsABCDE` — **does not establish** — homoacetogenesis | DOI:10.1186/s40168-024-01836-7 | Atribacterota “lack a complete WLP,” despite variable CODH/ACS and acetate-producing fermentation. | **Core exclusion supported by 2024 culture, transcriptomic, and comparative-genomic evidence.** (jiao2024cultivationofnovel pages 1-2) |
| 22 | Reverse WLP — **oxidizes** — acetate to CO₂ | DOI:10.1196/annals.1419.015 | Acetate-utilizing methanogens “run the pathway in reverse” and oxidize acetate to two CO₂. | **Boundary edge; explicitly not the target trait.** (ragsdale2008enzymologyofthe pages 1-2) |

| subject | predicate | object | evidence strength/scope |
|---|---|---|---|
| Homoacetogenesis | has_canonical_overall_reaction | 2 CO2 + 4 H2 -> acetate | Strong review support; canonical stoichiometry and thermodynamics for autotrophic homoacetogenesis in acetogens (karekar2022homoacetogenstheirmetabolism pages 1-3, basen2023editorialacetogens pages 1-2) |
| Homoacetogenesis | requires_pathway | Wood-Ljungdahl pathway (WLP) | Strong review support; trait-defining pathway in classical acetogens under anaerobic conditions (basen2023editorialacetogens pages 1-2, karekar2022homoacetogenstheirmetabolism pages 1-3, ragsdale2008enzymologyofthe pages 1-2) |
| WLP | has_branch | methyl branch: CO2 -> formate -> formyl-THF -> methenyl-THF/methylene-THF -> methyl group on corrinoid Fe-S protein | Strong mechanistic support from reviews and bioenergetic model summaries; intermediate list partly summarized at review level (karekar2022homoacetogenstheirmetabolism pages 1-3, ragsdale2008enzymologyofthe pages 1-2, wiechmann2021energyconservationin pages 8-11) |
| WLP | has_branch | carbonyl branch: CO2 -> CO | Strong mechanistic support; CODH reduces CO2 to enzyme-bound CO in acetogens (karekar2022homoacetogenstheirmetabolism pages 1-3, ragsdale2008enzymologyofthe pages 1-2, basen2023editorialacetogens pages 1-2) |
| H2 | donates_electrons_for | WLP-dependent CO2 reduction | Strong support in acetogens; H2 is primary reductant during H2/CO2 growth, via hydrogenases/HDCR depending on taxon (basen2023editorialacetogens pages 1-2, baum2024theenergyconvertinghydrogenase pages 1-2, wiechmann2021energyconservationin pages 8-11) |
| HDCR | catalyzes | CO2 -> formate in first step of methyl branch | Strong direct support in Acetobacterium woodii model; taxon-specific enzyme implementation (baum2024theenergyconvertinghydrogenase pages 1-2) |
| CODH/ACS complex | catalyzes | methyl group + CO + CoA -> acetyl-CoA | Strong mechanistic support; defining convergent step of the two WLP branches (karekar2022homoacetogenstheirmetabolism pages 1-3, ragsdale2008enzymologyofthe pages 1-2, wiechmann2021energyconservationin pages 8-11) |
| acetyl-CoA | is_converted_to | acetate | Strong support across acetogen reviews/models (basen2023editorialacetogens pages 1-2, karekar2022homoacetogenstheirmetabolism pages 1-3, wiechmann2021energyconservationin pages 8-11) |
| acetate kinase reaction | recovers | ATP invested earlier in formate activation | Strong support; WLP plus acetate formation is ATP-neutral overall at substrate level (basen2023editorialacetogens pages 1-2, baum2024theenergyconvertinghydrogenase pages 1-2) |
| Rnf complex | couples | reduced ferredoxin oxidation to NAD+ reduction and Na+-dependent ion gradient formation | Strong direct genetic/physiological support in Acetobacterium woodii; required for autotrophic growth on H2 + CO2 (westphal2018thernfcomplex pages 1-2, baum2024theenergyconvertinghydrogenase pages 1-2) |
| rnf deletion | abolishes | growth, acetate production, and ATP formation from H2 + CO2 | Strong causal knockout evidence in Acetobacterium woodii; species-specific but highly informative for graph edge curation (westphal2018thernfcomplex pages 1-2) |
| Ech complex | couples | ferredoxin-dependent proton reduction/H2 cycling to proton-gradient energy conservation | Strong support for Ech-type acetogens; direct physiological context in Thermoanaerobacter kivui (baum2024theenergyconvertinghydrogenase pages 1-2) |
| ech2 deletion | impairs | growth on ferredoxin-dependent substrates, especially CO | Strong 2024 knockout evidence in Thermoanaerobacter kivui; does not abolish H2 + CO2 growth because Ech1/other enzymes may compensate (baum2024theenergyconvertinghydrogenase pages 1-2) |
| homoacetogenesis | occurs_in | strict anaerobic conditions | Strong scope support from reviews and model acetogen literature (basen2023editorialacetogens pages 1-2, westphal2018thernfcomplex pages 1-2, ragsdale2008enzymologyofthe pages 1-2) |
| WLP gene presence alone | is_insufficient_for_inference_of | homoacetogenesis | Strong exclusion; WLP can be used for assimilation or other redox roles, so phenotype evidence is required (ragsdale2008enzymologyofthe pages 1-2, gencic2020diverseenergyconservingpathways pages 1-4, jiao2024cultivationofnovel pages 1-2) |
| methanogens using WLP | are_not_equivalent_to | homoacetogens | Strong exclusion; methanogens use WLP for cell carbon, and acetoclastic methanogens can run pathway in reverse during acetate oxidation (ragsdale2008enzymologyofthe pages 1-2) |
| reverse WLP / syntrophic acetate oxidation | is_not_same_trait_as | homoacetogenesis | Strong exclusion at phenotype level; reverse operation oxidizes acetate rather than producing it as sole reduced end product (ragsdale2008enzymologyofthe pages 1-2, jiao2024cultivationofnovel pages 1-2) |
| Clostridium difficile WLP | functions_in | disposal of reducing equivalents during carbohydrate metabolism rather than classical homoacetogenesis | Strong exclusion from primary study; complete WLP does not establish the trait (gencic2020diverseenergyconservingpathways pages 1-4) |
| Atribacterota genomes | often_lack | complete WLP | Strong 2024 exclusion; acetate production and some CODH/ACS genes do not justify curation as homoacetogenesis (jiao2024cultivationofnovel pages 1-2) |


*Table: This table summarizes the strongest candidate causal edges for a TraitMech graph of homoacetogenesis, including core Wood-Ljungdahl pathway steps, energy conservation modules, and key exclusions. It is useful for deciding which edges are sufficiently supported for curation and which require phenotype-specific caution.*

## 4. Quantitative and recent evidence

### Bioenergetic values

- Canonical standard-state stoichiometry is four H₂ plus two CO₂ per acetate, with ΔG°′ reported as approximately **−105 kJ mol⁻¹**. (karekar2022homoacetogenstheirmetabolism pages 1-3)
- Under environmentally low H₂, *Thermoanaerobacter kivui* researchers report available energy of about **−20 kJ mol⁻¹ or less**. (baum2024theenergyconvertinghydrogenase pages 1-2)
- A *Clostridium aceticum* model estimated **0.3 or 0.9 ATP per acetate**, depending on whether methylene-THF reductase is modeled as non-bifurcating or bifurcating and using an assumed Na⁺/ATP stoichiometry of 3.3. These are organism/model-specific estimates, not universal trait values. (wiechmann2021energyconservationin pages 8-11)
- A foundational review estimated that acetogens collectively produce over **10¹³ kg acetate annually**. This is an older global estimate and should be cited as historical context rather than a current census. (ragsdale2008enzymologyofthe pages 1-2)

### 2023–2024 developments

1. **Ech paralog specialization:** Baum et al., published 22 February 2024, deleted the complete `ech2` cluster from *T. kivui*. H₂/CO₂ growth remained wild-type-like, but growth on ferredoxin-dependent substrates was impaired and acetate formation from CO was lost. All five independently CO-adapted strains carried mutations in HDCR subunit `hycB3`, linking redox balancing, Ech paralogs, and CO adaptation. *T. kivui* has a reported optimum of **66°C**. (baum2024theenergyconvertinghydrogenase pages 1-2)
2. **Thermophilic cell factories:** a 2024 review identifies thermophilic acetogens as platforms for converting industrial waste-gas syngas—CO, CO₂, and H₂—into acetate, biomass, and engineered products. Reported advantages include high turnover and reduced cooling/contamination burdens; constrained metabolism and inadequate genetic tools remain major implementation barriers. *Moorella* species commonly have optima around **55–60°C**. (bourgade2024progressesandchallenges pages 1-2)
3. **Genomic inference corrected by cultivation:** Jiao et al. (2024) combined isolation, short-term cultivation, metatranscriptomics, and comparative genomics to show that Atribacterota ferment sugars or alkanes to H₂, CO₂, and acetate but lack a complete WLP; the reductive glycine pathway is instead central. This is a particularly important warning against assigning homoacetogenesis from environmental MAGs or acetate production alone. (jiao2024cultivationofnovel pages 1-2)
4. **Current conceptual consensus:** a 2023 expert editorial emphasizes that the WLP’s substrate-level ATP balance is zero and that energy conservation depends on reduced-ferredoxin oxidation through Rnf or Ech systems. It also frames acetogens as ancient carbon-fixing organisms with modern biotechnology potential. (basen2023editorialacetogens pages 1-2)

## 5. Applications and real-world implementation

- **Gas fermentation and carbon recycling:** acetogens can convert CO-rich syngas and H₂/CO₂ from industrial waste gases into acetate and acetyl-CoA-derived products. Thermophilic platforms may lower cooling requirements but remain less genetically tractable than established mesophilic strains. (baum2024theenergyconvertinghydrogenase pages 1-2, bourgade2024progressesandchallenges pages 1-2)
- **Methane mitigation in ruminants:** stimulating homoacetogenesis could redirect reducing equivalents from CH₄ toward acetate, which remains available to the host. However, hydrogenotrophic methanogens generally have a thermodynamic advantage at low H₂, so inhibition of methanogenesis does not guarantee stable redirection to acetate. This application should be represented as ecological competition, not a constitutive trait mechanism. (basen2023editorialacetogens pages 1-2, karekar2022homoacetogenstheirmetabolism pages 1-3)
- **Biological H₂ storage/power-to-gas systems:** reversible conversion between H₂/CO₂ and acetate is of interest as a storage intermediate, but reversibility and energy-conservation architecture are strongly strain-dependent.
- **Microbial electrosynthesis:** cathodic reducing power can support CO₂-to-acetate conversion, but electrode electron-transfer edges should not enter the core trait graph unless supported for a named strain and experimental system.
- **Anaerobic digestion:** homoacetogens influence H₂/formate turnover and acetate pools. They must be distinguished from syntrophic acetate oxidizers, which consume rather than produce acetate.

## 6. Expert interpretation for graph design

The most defensible graph architecture is a **conserved chemical core plus alternative bioenergetic modules**:

1. CO₂ enters methyl and carbonyl branches.
2. The branches converge at CODH/ACS to generate acetyl-CoA.
3. Pta/Ack-type conversion produces acetate and recovers the ATP consumed in methyl-branch formate activation.
4. Because this sequence is ATP-neutral, a membrane system conserves additional energy.
5. That membrane system should be represented as an **OR relationship**: Rnf-type or Ech-type, with ion specificity, hydrogenase complement, cofactor specificity, and exact ATP yield attached at strain level.

The strongest causal evidence currently available is the *A. woodii* `rnf` deletion: loss of H₂/CO₂ growth, acetate, ATP, oxidoreductase activity, and Na⁺ translocation directly connects Rnf to the phenotype. Conversely, the 2024 *T. kivui* Δ`ech2` result is equally valuable as negative evidence: Ech2 contributes to ferredoxin-dependent metabolism and CO conversion but is not independently necessary for H₂/CO₂ growth. (baum2024theenergyconvertinghydrogenase pages 1-2, westphal2018thernfcomplex pages 1-2)

## 7. Claims not yet ready for TraitMech curation

1. **“Every complete WLP genome is homoacetogenic.”** Rejected by assimilatory, reverse, and redox-balancing WLP use. (ragsdale2008enzymologyofthe pages 1-2, gencic2020diverseenergyconservingpathways pages 1-4)
2. **“`acsB`, `acsABCDE`, or CODH/ACS is a sufficient marker.”** Not supported; homolog function and pathway completeness must be resolved. (gencic2020diverseenergyconservingpathways pages 1-4, jiao2024cultivationofnovel pages 1-2)
3. **“Acetate production proves homoacetogenesis.”** Fermenters can produce acetate, H₂, and CO₂ without a complete WLP. (jiao2024cultivationofnovel pages 1-2)
4. **“Rnf and Ech are both universally required.”** They represent alternative, taxon-dependent architectures; paralogs may compensate. (basen2023editorialacetogens pages 1-2, baum2024theenergyconvertinghydrogenase pages 1-2)
5. **Universal Na⁺ coupling.** *A. woodii* and *C. aceticum* support Na⁺-dependent models, whereas Ech-type organisms can use proton gradients. (wiechmann2021energyconservationin pages 8-11, baum2024theenergyconvertinghydrogenase pages 1-2, westphal2018thernfcomplex pages 1-2)
6. **Universal electron-bifurcating methylene-THF reductase or ATP yield.** Cofactor use and complex architecture differ substantially; retain as strain-level hypotheses unless directly assayed. (wiechmann2021energyconservationin pages 8-11)
7. **Branch names “eastern” and “western.”** Literature usage is inconsistent. Curate “methyl branch” and “carbonyl branch” instead.
8. **Genus-level trait inheritance.** Acetogens are polyphyletic, and pathway function can vary even among related organisms. (basen2023editorialacetogens pages 1-2)
9. **Environmental metagenomic assignment without activity evidence.** MAG completeness, paralogy, and reversible pathway operation create high false-positive risk. The preferred evidence ladder is isotope-resolved physiology > genetic perturbation/biochemistry > transcript/protein-supported complete pathway > genome-only inference.

## DOI-first bibliography

1. Baum C, et al. “The energy-converting hydrogenase Ech2 is important for the growth of the thermophilic acetogen *Thermoanaerobacter kivui* on ferredoxin-dependent substrates.” *Microbiology Spectrum*. Published 22 February 2024; issue April 2024. DOI: [10.1128/spectrum.03380-23](https://doi.org/10.1128/spectrum.03380-23). (baum2024theenergyconvertinghydrogenase pages 1-2)
2. Bourgade B, et al. “Progresses and challenges of engineering thermophilic acetogenic cell factories.” *Frontiers in Microbiology*. August 2024. DOI: [10.3389/fmicb.2024.1476253](https://doi.org/10.3389/fmicb.2024.1476253). (bourgade2024progressesandchallenges pages 1-2)
3. Jiao J-Y, et al. “Cultivation of novel Atribacterota from oil well provides new insight into their diversity, ecology, and evolution in anoxic, carbon-rich environments.” *Microbiome*. July 2024. DOI: [10.1186/s40168-024-01836-7](https://doi.org/10.1186/s40168-024-01836-7). (jiao2024cultivationofnovel pages 1-2)
4. Basen M, Müller V. “Editorial: Acetogens—from the origin of life to biotechnological applications.” *Frontiers in Microbiology*. April 2023. DOI: [10.3389/fmicb.2023.1186930](https://doi.org/10.3389/fmicb.2023.1186930). (basen2023editorialacetogens pages 1-2)
5. Karekar S, Stefanini R, Ahring B. “Homo-Acetogens: Their Metabolism and Competitive Relationship with Hydrogenotrophic Methanogens.” *Microorganisms*. February 2022. DOI: [10.3390/microorganisms10020397](https://doi.org/10.3390/microorganisms10020397). (karekar2022homoacetogenstheirmetabolism pages 1-3)
6. Wiechmann A, Müller V. “Energy Conservation in the Acetogenic Bacterium *Clostridium aceticum*.” *Microorganisms*. January 2021. DOI: [10.3390/microorganisms9020258](https://doi.org/10.3390/microorganisms9020258). (wiechmann2021energyconservationin pages 8-11)
7. Gencic S, Grahame DA. “Diverse Energy-Conserving Pathways in *Clostridium difficile*: Growth in the Absence of Amino Acid Stickland Acceptors and the Role of the Wood–Ljungdahl Pathway.” *Journal of Bacteriology*. September 2020. DOI: [10.1128/JB.00233-20](https://doi.org/10.1128/JB.00233-20). (gencic2020diverseenergyconservingpathways pages 1-4)
8. Westphal L, et al. “The Rnf Complex Is an Energy-Coupled Transhydrogenase Essential To Reversibly Link Cellular NADH and Ferredoxin Pools in the Acetogen *Acetobacterium woodii*.” *Journal of Bacteriology*. November 2018. DOI: [10.1128/JB.00357-18](https://doi.org/10.1128/JB.00357-18). (westphal2018thernfcomplex pages 1-2)
9. Ragsdale SW. “Enzymology of the Wood–Ljungdahl Pathway of Acetogenesis.” *Annals of the New York Academy of Sciences*. March 2008. DOI: [10.1196/annals.1419.015](https://doi.org/10.1196/annals.1419.015). (ragsdale2008enzymologyofthe pages 1-2)
10. Müller V. “New horizons in acetogenic conversion of one-carbon substrates and biological hydrogen storage.” *Trends in Biotechnology*. December 2019. DOI: [10.1016/j.tibtech.2019.05.008](https://doi.org/10.1016/j.tibtech.2019.05.008). This is one of the supplied existing-evidence references; its full text was not independently extracted in this search.
11. Ragsdale SW, Pierce E. “Acetogenesis and the Wood–Ljungdahl pathway of CO₂ fixation.” *Biochimica et Biophysica Acta*. December 2008. DOI: [10.1016/j.bbapap.2008.08.012](https://doi.org/10.1016/j.bbapap.2008.08.012). This is the second supplied existing-evidence reference; retain as foundational pathway support.

References

1. (karekar2022homoacetogenstheirmetabolism pages 1-3): Supriya Karekar, Renan Stefanini, and Birgitte Ahring. Homo-acetogens: their metabolism and competitive relationship with hydrogenotrophic methanogens. Microorganisms, 10:397, Feb 2022. URL: https://doi.org/10.3390/microorganisms10020397, doi:10.3390/microorganisms10020397. This article has 115 citations.

2. (baum2024theenergyconvertinghydrogenase pages 1-2): Christoph Baum, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, Volker Müller, and Mirko Basen. The energy-converting hydrogenase ech2 is important for the growth of the thermophilic acetogen <i>thermoanaerobacter kivui</i> on ferredoxin-dependent substrates. Apr 2024. URL: https://doi.org/10.1128/spectrum.03380-23, doi:10.1128/spectrum.03380-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

3. (ragsdale2008enzymologyofthe pages 1-2): Stephen W. Ragsdale. Enzymology of the wood–ljungdahl pathway of acetogenesis. Annals of the New York Academy of Sciences, 1125:129-136, Mar 2008. URL: https://doi.org/10.1196/annals.1419.015, doi:10.1196/annals.1419.015. This article has 530 citations and is from a peer-reviewed journal.

4. (gencic2020diverseenergyconservingpathways pages 1-4): Simonida Gencic and David A. Grahame. Diverse energy-conserving pathways in clostridium difficile: growth in the absence of amino acid stickland acceptors and the role of the wood-ljungdahl pathway. Sep 2020. URL: https://doi.org/10.1128/jb.00233-20, doi:10.1128/jb.00233-20. This article has 77 citations and is from a peer-reviewed journal.

5. (jiao2024cultivationofnovel pages 1-2): Jian-Yu Jiao, Shi-Chun Ma, Nimaichand Salam, Zhuo Zhou, Zheng-Han Lian, Li Fu, Ying Chen, Cheng-Hui Peng, Yu-Ting OuYang, Hui Fan, Ling Li, Yue Yi, Jing-Yi Zhang, Jing-Yuan Wang, Lan Liu, Lei Gao, Aharon Oren, Tanja Woyke, Jeremy A. Dodsworth, Brian P. Hedlund, Wen-Jun Li, and Lei Cheng. Cultivation of novel atribacterota from oil well provides new insight into their diversity, ecology, and evolution in anoxic, carbon-rich environments. Microbiome, Jul 2024. URL: https://doi.org/10.1186/s40168-024-01836-7, doi:10.1186/s40168-024-01836-7. This article has 20 citations and is from a highest quality peer-reviewed journal.

6. (basen2023editorialacetogens pages 1-2): Mirko Basen and Volker Müller. Editorial: acetogens - from the origin of life to biotechnological applications. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1186930, doi:10.3389/fmicb.2023.1186930. This article has 7 citations and is from a peer-reviewed journal.

7. (westphal2018thernfcomplex pages 1-2): Lars Westphal, Anja Wiechmann, Jonathan Baker, Nigel P. Minton, and Volker Müller. The rnf complex is an energy-coupled transhydrogenase essential to reversibly link cellular nadh and ferredoxin pools in the acetogen acetobacterium woodii. Journal of Bacteriology, Nov 2018. URL: https://doi.org/10.1128/jb.00357-18, doi:10.1128/jb.00357-18. This article has 162 citations and is from a peer-reviewed journal.

8. (wiechmann2021energyconservationin pages 8-11): Anja Wiechmann and Volker Müller. Energy conservation in the acetogenic bacterium clostridium aceticum. Microorganisms, 9:258, Jan 2021. URL: https://doi.org/10.3390/microorganisms9020258, doi:10.3390/microorganisms9020258. This article has 16 citations.

9. (bourgade2024progressesandchallenges pages 1-2): Barbara Bourgade, M. A. Islam, S. Scully, and Simone Antonio De Rose. Progresses and challenges of engineering thermophilic acetogenic cell factories. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1476253, doi:10.3389/fmicb.2024.1476253. This article has 9 citations and is from a peer-reviewed journal.