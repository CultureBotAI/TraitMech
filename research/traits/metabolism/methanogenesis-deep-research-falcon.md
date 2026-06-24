---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:18:46.909787'
end_time: '2026-06-18T05:35:16.581941'
duration_seconds: 989.67
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Methanogenesis
  trait_identifier: METPO:1000844
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: methanogenesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which methane is produced as the primary end product
    through the reduction of carbon-containing compounds, formate, methanol, or acetate,
    exclusively performed by methanogenic archaea under strictly anaerobic conditions.
  parent_traits: METPO:1000060
  synonyms: Biological methanation, Biomethanation, Carbonate respiration
  evidence_summary: 'DOI:10.1146/annurev-micro-011720-122807: from CO2 and H2 to methane
    (Supports hydrogenotrophic methanogenesis as a methane-producing archaeal pathway.)
    | DOI:10.1021/acs.biochem.9b00164: catalyzes the reversible reduction of methyl-coenzyme
    M (Supports methyl-coenzyme M reductase as the terminal methane-forming enzyme.)'
  causal_graph_summary: 'methanogenesis_c1_reduction: 7 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Methanogenesis
- **METPO identifier:** METPO:1000844
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is produced as the primary end product through the reduction of carbon-containing compounds, formate, methanol, or acetate, exclusively performed by methanogenic archaea under strictly anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Biological methanation, Biomethanation, Carbonate respiration
- **Existing evidence:** DOI:10.1146/annurev-micro-011720-122807: from CO2 and H2 to methane (Supports hydrogenotrophic methanogenesis as a methane-producing archaeal pathway.) | DOI:10.1021/acs.biochem.9b00164: catalyzes the reversible reduction of methyl-coenzyme M (Supports methyl-coenzyme M reductase as the terminal methane-forming enzyme.)
- **Existing causal graph summary:** methanogenesis_c1_reduction: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **Methanogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/methanogenesis.yaml`.

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
- **Trait label:** Methanogenesis
- **METPO identifier:** METPO:1000844
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is produced as the primary end product through the reduction of carbon-containing compounds, formate, methanol, or acetate, exclusively performed by methanogenic archaea under strictly anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Biological methanation, Biomethanation, Carbonate respiration
- **Existing evidence:** DOI:10.1146/annurev-micro-011720-122807: from CO2 and H2 to methane (Supports hydrogenotrophic methanogenesis as a methane-producing archaeal pathway.) | DOI:10.1021/acs.biochem.9b00164: catalyzes the reversible reduction of methyl-coenzyme M (Supports methyl-coenzyme M reductase as the terminal methane-forming enzyme.)
- **Existing causal graph summary:** methanogenesis_c1_reduction: 7 nodes, 5 edges

## Research Objective

Research the microbial trait **Methanogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/methanogenesis.yaml`.

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


## Research Report: Methanogenesis (METPO:1000844) — TraitMech Causal Graph Curation

### Scope summary (Trait scope & boundary cases)
Methanogenesis (METPO:1000844) is an archaeal anaerobic energy metabolism in which methane (CH4) is the terminal reduced end product; mechanistically it is an anaerobic respiration process using oxidized carbon (classically CO2) as terminal electron acceptor in the hydrogenotrophic route, and it also includes acetoclastic and methyl-based routes (szuhaj2023regulationofthe pages 1-2, mesquita2023methylbasedmethanogenesisan pages 2-4). It is constrained to strictly anoxic conditions (strict anaerobiosis) and is commonly positioned at the end of anaerobic redox cascades because it becomes favorable mainly after more energy-yielding electron acceptors (nitrate, Fe(III), Mn(IV), sulfate) are depleted (szuhaj2023regulationofthe pages 1-2, mesquita2023methylbasedmethanogenesisan pages 4-5).

Boundary cases important for curation:
- **Not methanotrophy**: methanogenesis produces CH4; methane oxidation is a distinct phenotype (not supported by the extracted evidence and should be excluded from this trait).
- **Not generic “anaerobic digestion” (AD)**: methanogenesis is one stage within AD; AD includes hydrolysis/acidogenesis/acetogenesis upstream of methanogenesis (zbair2024integrationofdigestatederived pages 4-6). Trait curation should focus on archaeal CH4-forming capacity, while AD-level interactions (syntrophy, DIET) can be modeled as environmental/process modifiers.
- **Competition with other anaerobic respirations**: sulfate reducers can outcompete methanogens for shared substrates (H2, acetate), suppressing hydrogenotrophic and acetoclastic routes; methyl-based methanogens can remain active under high sulfate (mesquita2023methylbasedmethanogenesisan pages 4-5).
- **Assay boundary/inhibition controls**: 2-bromoethanesulfonate (BES) and chloroform are used experimentally to inhibit methanogens and confirm biogenic methane sources (mesquita2023methylbasedmethanogenesisan pages 8-11).

### Key concepts & current mechanistic understanding

#### Major pathway classes
Methanogenesis is commonly partitioned by carbon/electron source into:
1) **Hydrogenotrophic methanogenesis**: CO2 reduction by H2 (CO2 + 4H2 → CH4 + 2H2O) (szuhaj2023regulationofthe pages 1-2). H2 (and sometimes formate) supplies reducing equivalents in CO2-reduction methanogens (khairunisa2023evolvingunderstandingof pages 10-11).
2) **Acetoclastic methanogenesis**: acetate is cleaved to CH4 and CO2 (szuhaj2023regulationofthe pages 1-2).
3) **Methyl-based methanogenesis**: methane formation from methylated compounds. A 2023 MMBR review scopes methyl-based methanogenesis as including **methyl dismutation** and **methyl-reducing (hydrogen-dependent methylotrophic)** routes, with substrates including methanol and methylamines (e.g., TMA/DMA/MMA) among others (mesquita2023methylbasedmethanogenesisan pages 8-11, mesquita2023methylbasedmethanogenesisan pages 2-4).

A gene-centric summary table/figure in de Mesquita et al. (2023) shows pathway-associated marker genes (e.g., acetoclastic cdhD, hydrogenotrophic frhA, methylotrophic genes such as mtaA/mttC) and the universal presence of mcrA in methanogens (mesquita2023methylbasedmethanogenesisan media 81c08583, mesquita2023methylbasedmethanogenesisan media 479fdb47).

#### Universal terminal step: methyl-coenzyme M reductase (Mcr)
A central unifying biochemical feature is that **methyl-coenzyme M reductase (Mcr)** catalyzes the terminal methane-forming step and is conserved across methanogenic pathways; Szuhaj et al. (2023) states Mcr is “the single enzyme present in all methanogenesis types” catalyzing the final methyl-to-methane step (szuhaj2023regulationofthe pages 1-2). de Mesquita et al. (2023) likewise describes the terminal methane-forming step as catalyzed by Mcr (encoded by **mcrABG**) in which methyl-CoM reacts with coenzyme B (CoB) to yield methane (mesquita2023methylbasedmethanogenesisan pages 8-11), and provides visual evidence that all pathways require mcrABG (mesquita2023methylbasedmethanogenesisan media 81c08583).

#### Cofactors and electron carriers (Wolfe cycle components)
Mechanistic cofactor requirements include coenzyme carriers and low-potential electron transfer:
- CO2 reduction proceeds stepwise with intermediates carried on methanofuran (MFR), tetrahydromethanopterin (H4MPT), and coenzyme M (CoM) (khairunisa2023evolvingunderstandingof pages 10-11).
- Reduced coenzyme F420 (F420H2) donates electrons for specific reduction steps (khairunisa2023evolvingunderstandingof pages 10-11).
- Coenzyme B (CoB) participates in the terminal reduction to methane, producing the heterodisulfide CoM-S-S-CoB (khairunisa2023evolvingunderstandingof pages 10-11).

#### Environmental controls: strict anaerobiosis, H2 partial pressure, and competitive electron acceptors
Key environmental and community-level regulators include:
- **Strict anaerobiosis**: methanogenesis is framed as an anaerobic respiration process and strict anaerobiosis is a practical and biological constraint (szuhaj2023regulationofthe pages 1-2, khairunisa2023evolvingunderstandingof pages 2-3).
- **H2 availability and pH2 regulation**: Szuhaj et al. (2023) emphasizes “tightly regulated local H2 levels and interspecies H2 transfer” and notes very low aqueous H2 solubility as limiting (szuhaj2023regulationofthe pages 1-2). In rumen ecology, methanogens act as H2 sinks enabling fermentation; H2 accumulation elevates pH2 and can block NADH oxidation thermodynamically, linking methanogenesis to syntrophic network stability (khairunisa2023evolvingunderstandingof pages 2-3).
- **Competition with sulfate reduction and other anaerobic respirations**: methanogenesis typically occurs after nitrate/Fe(III)/Mn(IV)/sulfate depletion; sulfate reducers can outcompete methanogens at high sulfate (mesquita2023methylbasedmethanogenesisan pages 4-5). Competition is strongest for shared substrates (H2 and acetate), suppressing hydrogenotrophic and acetoclastic routes, while methyl-based methanogens can “avoid this competition” under high sulfate (mesquita2023methylbasedmethanogenesisan pages 4-5).

### Recent developments (2023–2024 prioritized)

#### Expanding appreciation of methyl-based methanogenesis
A 2023 Microbiology and Molecular Biology Reviews synthesis highlights that methyl-based methanogenesis includes methyl dismutation and methyl-reducing pathways and catalogues a broad substrate space (methanol, methylamines, sulfonium compounds, etc.), with pathway discrimination supported by gene content and environmental context (mesquita2023methylbasedmethanogenesisan pages 8-11, mesquita2023methylbasedmethanogenesisan pages 2-4).

A 2024 genome-resolved multi-omics study in thawing permafrost peatland (Stordalen Mire) argues methylotrophic potential and expression are underappreciated in wetland methane production. It reports detection of methanogenic substrates (e.g., acetate, formate, methanol; methylated amines) and substantial proportions of methanogen MAGs encoding methylotrophic potential (mean 64% in bog and 30% in fen) (ellenbogen2024methylotrophyinthe pages 5-7). This supports including methylotrophic routes as first-class mechanistic branches in the trait causal graph.

#### Transcriptomic regulation by hydrogen and isoenzyme adaptation
A 2023 transcriptomic study emphasizes that hydrogen can rapidly “switch off” and “switch on” methanogenesis in some methanogens (within about an hour in a tested autotrophic methanogen) and stresses the importance of community composition for fluctuating H2/CO2 inputs in power-to-gas systems (szuhaj2023regulationofthe pages 1-2). A 2023 rumen review notes distinct Mcr isoenzymes (Mcr I vs Mcr II; mcr vs mrt) adapted to different H2 partial pressures, reinforcing pH2 as a regulatory dimension for methanogenic capacity expression (khairunisa2023evolvingunderstandingof pages 11-12).

#### Systems integration: CCU and bio-integrated capture concepts
A 2024 Nature Communications Perspective proposes Bio‑Integrated Carbon Capture and Utilization (BICCU), in which methanogens catalyze CO2 release from capture agents coupled to CO2 reduction to methane using green hydrogen, aiming to avoid energy-intensive thermal desorption (sieborg2024biointegratedcarboncapture pages 1-2). Although conceptual/low TRL, it is relevant for applications and motivates nodes/edges linking capture chemistry conditions to methanogenic CO2 reduction.

### Current applications & real-world implementations (with recent statistics)

#### Anaerobic digestion (AD) optimization and yield improvements
- A 2024 Scientific Reports study on coal–straw co-digestion reports a **1246.05%** increase in methane yield versus control and associates this with microbial community shifts (Methanosarcinaceae ~51.14%, Methanobacteriaceae ~39.90%) and increased abundance of enzymes related to CO2-to-methane conversion (khan2024coalstrawcodigestioninducedbiogenic pages 1-2). This provides application-level evidence connecting substrate amendments → community composition/enzyme abundance → methane yield.
- An AD-focused review notes methanogenesis is often a bottleneck due to slow-growing methanogens and sensitivity to H2/VFA accumulation, and emphasizes that syntrophic conversions of VFAs to acetate/H2 depend on **very low H2 partial pressures (<10−3 atm)** (zbair2024integrationofdigestatederived pages 4-6). This supports adding edges linking low H2 partial pressure → syntrophy → stable methanogenesis in engineered ecosystems.
- Functional biochar is reviewed as an AD additive that can enhance methane production via promoting electron transfer (supporting DIET), buffering, microbial immobilization, and mitigation of inhibitory effects (chen2024functionalbiocharas pages 1-3). Conductive materials are similarly linked to DIET/IET concepts and methanogenesis sensitivity to inhibitors (e.g., ammonia, sulfide) (mishra2024useofconductive pages 3-6).

#### Power-to-Gas (P2G) / biomethanation
- A 2024 biomethanation-oriented CCU analysis reports lab-scale coupling of post-combustion CO2 capture with biomethanation achieving **CO2 conversion (CDC) 96.65%** and **methane content 68.03%** (V/V) (sinorosszabo2024carboncaptureand pages 1-2). It highlights oxygen as particularly detrimental to biomethanation performance (sinorosszabo2024carboncaptureand pages 1-2).
- A 2023 review of biological H2 methanation emphasizes that **low gas–liquid mass transfer** is a major limitation (“low transport of gases into the liquid phase”), and reports performance ranges for reactor configurations (e.g., packed bed values expressed as volumetric methane productivities; and methane fraction increasing from **64.13% to 86.51%** when pressure increased from 1.5 to 9 bar in an example) (gonzalez2023biologicalhydrogenmethanation pages 13-15, gonzalez2023biologicalhydrogenmethanation pages 16-17). These observations justify incorporating engineering nodes (gas–liquid mass transfer, pressure) as experimental factors affecting observed methanogenesis rates.

### Expert synthesis (authoritative interpretations)
- Methanogenesis is typically the terminal anaerobic respiration in redox ladders and is suppressed by alternative electron acceptors; de Mesquita et al. frame this as methanogenesis occurring only after nitrate/Fe(III)/Mn(IV)/sulfate depletion, and quantify pathway ΔG° ranges (context-dependent) (mesquita2023methylbasedmethanogenesisan pages 4-5).
- Methyl-based methanogenesis is increasingly treated as both ecologically important and genomically diverse; de Mesquita et al. organize methyl-based substrates and genes and provide marker-gene logic for distinguishing pathways, while noting taxonomic ambiguity because some taxa (e.g., Methanosarcinaceae) can perform multiple pathways (mesquita2023methylbasedmethanogenesisan pages 2-4, mesquita2023methylbasedmethanogenesisan pages 7-8).
- Rumen-focused synthesis emphasizes methanogens’ ecosystem role as a thermodynamic sink for H2, with methanogen diversity and enzyme isoforms adapting to pH2 regimes (khairunisa2023evolvingunderstandingof pages 2-3, khairunisa2023evolvingunderstandingof pages 11-12).

### Candidate nodes for TraitMech curation (grouped)

#### Trait / pathway nodes
- Methanogenesis (METPO:1000844)
- Hydrogenotrophic methanogenesis (label candidate)
- Acetoclastic methanogenesis (label candidate)
- Methyl-based methanogenesis (label candidate), including methyl dismutation and methyl-reducing / hydrogen-dependent methylotrophic routes (mesquita2023methylbasedmethanogenesisan pages 8-11)

#### Genes / proteins / complexes (markers and core machinery)
- methyl-coenzyme M reductase (Mcr) (EC:2.8.4.1 suggested); genes **mcrABG**; marker gene **mcrA** (szuhaj2023regulationofthe pages 1-2, mesquita2023methylbasedmethanogenesisan pages 8-11, mesquita2023methylbasedmethanogenesisan media 81c08583)
- Hydrogenotrophic marker gene: **frhA** (F420-reducing hydrogenase subunit A; per figure/table summary) (mesquita2023methylbasedmethanogenesisan media 81c08583)
- Acetoclastic marker gene: **cdhD** (as shown in pathway gene summary) (mesquita2023methylbasedmethanogenesisan media 81c08583)
- Methylotrophic pathway genes (examples): **mtaA**, **mttC** (as shown in pathway gene summary) (mesquita2023methylbasedmethanogenesisan media 81c08583)

#### Key chemicals (CHEBI suggested where established)
- Substrates/e-donors: CO2 (CHEBI:16526), H2 (CHEBI:18276), acetate (CHEBI:30089), methanol (CHEBI:17790), methylamines including trimethylamine (CHEBI:11417), dimethylamine (CHEBI:17928), monomethylamine (CHEBI:59313) (szuhaj2023regulationofthe pages 1-2, mesquita2023methylbasedmethanogenesisan pages 2-4)
- Electron carriers/cofactors (grounding to be verified): coenzyme M (CoM), coenzyme B (CoB), coenzyme F420/F420H2 (khairunisa2023evolvingunderstandingof pages 10-11, mesquita2023methylbasedmethanogenesisan pages 8-11)
- Competing electron acceptor/process node: sulfate (CHEBI:16189) and sulfate reduction (process/organism node) (mesquita2023methylbasedmethanogenesisan pages 4-5)
- Inhibitors/assay reagents: 2-bromoethanesulfonic acid (BES; CHEBI candidate), chloroform (CHEBI:35254) (mesquita2023methylbasedmethanogenesisan pages 8-11)

#### Environmental / experimental factors
- Anaerobic conditions / strict anaerobiosis (ENVO candidate) (szuhaj2023regulationofthe pages 1-2)
- H2 partial pressure (pH2) (environmental/experimental factor) (szuhaj2023regulationofthe pages 1-2, khairunisa2023evolvingunderstandingof pages 11-12)
- Very low H2 partial pressure threshold in AD syntrophy (<10−3 atm) (zbair2024integrationofdigestatederived pages 4-6)
- Gas–liquid mass transfer limitation (H2 solubility/KLa) (gonzalez2023biologicalhydrogenmethanation pages 13-15)
- Pressure (reactor/experimental factor) affecting methane fraction (gonzalez2023biologicalhydrogenmethanation pages 16-17)
- Oxygen contamination/exposure (O2 CHEBI:15379) as negative factor for biomethanation (sinorosszabo2024carboncaptureand pages 1-2)

### Candidate causal edges table (curation-ready)
The following table is structured for direct conversion into `methanogenesis.yaml` edges, with notes on where edges are implementation-specific or need ontology verification.

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Pathway context | Evidence snippet | Source | DOI URL | Curation notes / uncertainty |
|---|---|---|---|---|---|---|---|
| Methanogenesis (METPO:1000844) | occurs_under | anaerobic conditions (ENVO:01000254 candidate) | all | “methanogenesis is an anaerobic respiration process” and strict anaerobiosis is highlighted as a core constraint | Szuhaj 2023, *Applied Microbiology and Biotechnology* (szuhaj2023regulationofthe pages 1-2) | https://doi.org/10.1007/s00253-023-12700-3 | Strong scope-defining edge; ENVO grounding for “anaerobic conditions” should be checked before curation. |
| methyl-coenzyme M reductase complex / Mcr (EC:2.8.4.1; gene cluster mcrABG) | catalyzes_terminal_step_of | methanogenesis (METPO:1000844) | all | “Mcr… is the single enzyme present in all methanogenesis types, catalyzing the final methyl-to-methane step” | Szuhaj 2023, *Applied Microbiology and Biotechnology* (szuhaj2023regulationofthe pages 1-2) | https://doi.org/10.1007/s00253-023-12700-3 | Very strong generic edge for TraitMech. Gene-level representation via mcrABG is also supported separately. |
| mcrABG gene cluster | enables | methyl-coenzyme M reductase complex / Mcr (EC:2.8.4.1) | all | “A key genetic requirement across these pathways is the presence of mcrABG” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 2-4) | https://doi.org/10.1128/mmbr.00024-22 | Strong genotype→function edge; “enables” preferred over direct trait assertion if graph separates gene and enzyme nodes. |
| CO2 (CHEBI:16526) + H2 (CHEBI:18276) | serves_as_substrate_for | hydrogenotrophic methanogenesis (label candidate) | hydrogenotrophic | “hydrogenotrophic (reducing CO2 with H2 to CH4)” | Szuhaj 2023, *Applied Microbiology and Biotechnology* (szuhaj2023regulationofthe pages 1-2) | https://doi.org/10.1007/s00253-023-12700-3 | Strong pathway-defining edge. Could be split into two substrate edges if needed. |
| acetate (CHEBI:30089) | serves_as_substrate_for | acetoclastic methanogenesis (label candidate) | acetoclastic | “acetoclastic (splitting acetate to CH4 and CO2)” | Szuhaj 2023, *Applied Microbiology and Biotechnology* (szuhaj2023regulationofthe pages 1-2) | https://doi.org/10.1007/s00253-023-12700-3 | Strong pathway-defining edge. |
| methylated compounds (methanol CHEBI:17790; methylamines CHEBI candidates) | serves_as_substrate_for | methyl-based methanogenesis (label candidate) | methyl-based | “methylotrophic (using methylated compounds)” | Szuhaj 2023, *Applied Microbiology and Biotechnology* (szuhaj2023regulationofthe pages 1-2) | https://doi.org/10.1007/s00253-023-12700-3 | Broad but useful pathway-defining edge; curate substrate-specific children where possible. |
| trimethylamine (CHEBI:11417) / dimethylamine (CHEBI:17928) / monomethylamine (CHEBI:59313) / methanol (CHEBI:17790) | feeds | methyl-based methanogenesis (label candidate) | methyl-based | “main methyl substrates… TMA, DMA, MMA, MeOH…” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 2-4, mesquita2023methylbasedmethanogenesisan pages 8-11) | https://doi.org/10.1128/mmbr.00024-22 | Strong substrate list from review; consider separate rows per substrate in YAML. |
| methyl-CoM / 2-(methylthio)ethanesulfonate derivative (CHEBI candidate) | is_reduced_by | methyl-coenzyme M reductase complex / Mcr (EC:2.8.4.1) | all | “methyl-CoM reacts with coenzyme B (CoB) to yield methane” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 8-11) | https://doi.org/10.1128/mmbr.00024-22 | Strong biochemical edge, but CHEBI grounding for methyl-CoM should be verified. |
| coenzyme B / CoB (CHEBI candidate) | is_required_for | methane formation (CHEBI:16183) | all | “methyl-CoM reacts with coenzyme B (CoB) to yield methane” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 8-11) | https://doi.org/10.1128/mmbr.00024-22 | Strong terminal-step cofactor edge; may be modeled via Mcr reaction rather than direct trait edge. |
| coenzyme M / CoM (CHEBI candidate) | carries_methyl_group_in | methanogenesis (METPO:1000844) | hydrogenotrophic, methyl-based | CO2 reduction proceeds through intermediates to “methyl” on “coenzyme M (CoM)” and methyltransferases transfer methyl groups “ultimately to CoM to form methyl-CoM” | Khairunisa 2023, *Frontiers in Microbiology*; de Mesquita 2023, *MMBR* (khairunisa2023evolvingunderstandingof pages 10-11, mesquita2023methylbasedmethanogenesisan pages 11-13) | https://doi.org/10.3389/fmicb.2023.1296008 ; https://doi.org/10.1128/mmbr.00024-22 | Strong mechanistic edge; exact ontology for CoM should be checked. |
| coenzyme F420 / F420H2 (CHEBI candidate) | donates_electrons_to | CO2-reduction steps in methanogenesis (label candidate) | hydrogenotrophic | “Reduced coenzyme F420 (F420H2)… donates electrons for reductions of methenyl/methylene intermediates” | Khairunisa 2023, *Frontiers in Microbiology* (khairunisa2023evolvingunderstandingof pages 10-11) | https://doi.org/10.3389/fmicb.2023.1296008 | Strong pathway-mechanism edge, but object may be better represented as specific reductase reactions rather than whole trait. |
| H2 partial pressure (label candidate) | regulates | methanogenesis pathway expression/activity (label candidate) | hydrogenotrophic, community regulation | “H2/CO2 affected several… metabolic pathways” and H2 availability is a bottleneck; Mcr isoenzymes are “adapted to low vs. high pH2” | Szuhaj 2023, *Applied Microbiology and Biotechnology*; Khairunisa 2023, *Frontiers in Microbiology* (szuhaj2023regulationofthe pages 1-2, khairunisa2023evolvingunderstandingof pages 11-12) | https://doi.org/10.1007/s00253-023-12700-3 ; https://doi.org/10.3389/fmicb.2023.1296008 | Strong but somewhat broad regulatory edge; taxon-specific details for Mcr I vs Mcr II should be flagged if encoded. |
| low H2 partial pressure (<10^-3 atm) | promotes | syntrophic acetogenesis supporting methanogenesis (label candidate) | AD | syntrophs convert VFAs to acetate and H2 under “strict low H2 partial pressures (notably <10−3 atm)” | Zbair 2024, *Materials* (zbair2024integrationofdigestatederived pages 4-6) | https://doi.org/10.3390/ma17143527 | Strong AD ecosystem edge; indirect support for methanogenesis via syntrophy rather than direct archaeal biochemistry. |
| sulfate (CHEBI:16189) / sulfate-reducing bacteria (NCBITaxon candidate) | inhibits_competes_with | hydrogenotrophic and acetoclastic methanogenesis (label candidate) | environmental competition | sulfate reducers “can outcompete methanogens when sulfate concentrations are high”; “hydrogenotrophic and acetoclastic methanogenesis were inhibited” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 4-5) | https://doi.org/10.1128/mmbr.00024-22 | Strong ecological competition edge; object could be modeled as pathways rather than whole trait. |
| methyl-based methanogens (NCBITaxon candidate) | remains_active_under | high sulfate conditions (ENVO/condition candidate) | methyl-based | methyl-based methanogens “avoided this competition and remained active even under high sulfate conditions” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 4-5) | https://doi.org/10.1128/mmbr.00024-22 | Useful boundary-case edge distinguishing methyl-based routes from H2/acetate routes. |
| 2-bromoethanesulfonate / BES (CHEBI candidate) | inhibits | methanogens / methanogenesis (METPO:1000844) | assay/inhibitor | “2-bromoethanesulfonic acid… [is] used experimentally to inhibit methanogens and confirm biogenic methane” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 8-11) | https://doi.org/10.1128/mmbr.00024-22 | Strong assay edge; curate as experimental inhibitor, not natural ecology. |
| chloroform (CHEBI:35254) | inhibits | methanogens / methanogenesis (METPO:1000844) | assay/inhibitor | “chloroform” used experimentally “to inhibit methanogens and confirm biogenic methane” | de Mesquita 2023, *Microbiology and Molecular Biology Reviews* (mesquita2023methylbasedmethanogenesisan pages 8-11) | https://doi.org/10.1128/mmbr.00024-22 | Strong assay edge; mechanism not specified in extracted text. |
| hydrogenotrophic methanogens (NCBITaxon candidate) | compete_for | H2 (CHEBI:18276) | AD/ecology | “low concentrations create competition among hydrogenotrophic methanogens, sulfate-reducing bacteria, and homoacetogens” | Niya 2024, *Heliyon* (niya2024currentstatusand pages 10-11) | https://doi.org/10.1016/j.heliyon.2024.e28221 | Strong community ecology edge; taxon/process-level rather than single-organism biochemistry. |
| methylotrophic methanogens (NCBITaxon candidate) | does_not_compete_for | H2 (CHEBI:18276) | AD/ecology | “methylotrophic methanogens do not compete for H2” | Niya 2024, *Heliyon* (niya2024currentstatusand pages 10-11) | https://doi.org/10.1016/j.heliyon.2024.e28221 | Useful negative edge for pathway discrimination; wording should match graph schema. |
| acetoclastic methanogenesis (label candidate) | contributes_major_fraction_of | biologically derived methane (CHEBI:16183) | acetoclastic | “acetoclastic methanogenesis… accounts for roughly 65–75% of biologically derived methane” | Niya 2024, *Heliyon* (niya2024currentstatusand pages 10-11) | https://doi.org/10.1016/j.heliyon.2024.e28221 | Statistic is context-dependent and broad; suitable as note/annotation rather than universal causal edge. |
| functional biochar (CHEBI/label candidate) | promotes | electron transfer / DIET (GO/label candidate) | AD | functional biochar improves AD by “promoting electron transfer (supporting DIET)” | Chen 2024, *Biochar* (chen2024functionalbiocharas pages 1-3) | https://doi.org/10.1007/s42773-024-00345-y | Strong applied-process edge; indirect to archaeal trait, best curated as environmental/process modifier. |
| promoted electron transfer / DIET (label candidate) | increases | methane production (CHEBI:16183) | AD | these effects “lead to increased methane production” | Chen 2024, *Biochar* (chen2024functionalbiocharas pages 1-3) | https://doi.org/10.1007/s42773-024-00345-y | Moderate-strength review-level edge; causal chain likely mediated by multiple taxa and syntrophies. |
| low gas–liquid H2 mass transfer (label candidate) | limits | H2/CO2 biomethanation (label candidate) | P2G | “The main limitation of the H2/CO2 conversion process is dictated by the low transport of gases into the liquid phase” | Gonzalez 2023, *Environments* (gonzalez2023biologicalhydrogenmethanation pages 13-15) | https://doi.org/10.3390/environments10050082 | Strong engineering edge for P2G implementations; not a core intrinsic trait edge. |
| increased pressure (label candidate) | increases | methane fraction in biogas (CHEBI:16183 proportion) | P2G | methane fraction increased “from 64.13% to 86.51% when pressure increased from 1.5 to 9 bar” | Gonzalez 2023, *Environments* (gonzalez2023biologicalhydrogenmethanation pages 16-17) | https://doi.org/10.3390/environments10050082 | Quantitative applied edge; specific reactor context, so mark as implementation-specific. |
| oxygen / O2 (CHEBI:15379) exposure | negatively_affects | biomethanation performance (label candidate) | P2G | “oxygen having a particularly negative effect on methanation performance” | Sinóros-Szabó 2024, *Periodica Polytechnica Chemical Engineering* (sinorosszabo2024carboncaptureand pages 1-2, sinorosszabo2024carboncaptureand pages 2-4) | https://doi.org/10.3311/ppch.22248 | Strong operational constraint; may generalize to oxygen sensitivity of methanogens but extracted evidence is process-focused. |
| post-combustion CO2 capture coupled to biomethanation (label candidate) | achieved | CO2 conversion 96.65% and methane content 68.03% | P2G/CCU | “CDC of 96.65% (V/V) and a methane content of 68.03% (V/V)” | Sinóros-Szabó 2024, *Periodica Polytechnica Chemical Engineering* (sinorosszabo2024carboncaptureand pages 1-2) | https://doi.org/10.3311/ppch.22248 | Valuable implementation statistic; not a generic biological causal edge, but useful application annotation. |


*Table: This table lists curation-ready candidate causal edges for a TraitMech methanogenesis graph, grounded where possible to stable identifiers and backed by evidence available in the conversation. It prioritizes pathway-defining, biochemical, ecological, and applied-process relationships while flagging context-dependent or implementation-specific claims.*

### Warnings / claims to treat as uncertain before curation
1) **Context dependence of quantitative fractions**: the statement that acetoclastic methanogenesis accounts for ~65–75% of biologically derived methane is system- and community-dependent; it may be better represented as an annotation conditioned on AD-like environments rather than as a universal trait assertion (niya2024currentstatusand pages 10-11).
2) **Pathway marker gene generalization**: marker genes (e.g., frhA, cdhD, mtaA/mttC) are useful for inference but can be incomplete in metagenomes/MAGs; treat as evidence for potential rather than confirmed activity unless paired with expression or flux assays (mesquita2023methylbasedmethanogenesisan media 81c08583).
3) **Cofactor ontology grounding**: CoM, CoB, and F420 identifiers were not fully grounded here; verify CHEBI entries before committing identifiers (khairunisa2023evolvingunderstandingof pages 10-11, mesquita2023methylbasedmethanogenesisan pages 8-11).
4) **Engineering-factor edges are not intrinsic trait edges**: pressure, KLa, biochar/DIET, and O2 sensitivity edges reflect process performance modulation and should be categorized as experimental/environmental modifiers, not required components of the intrinsic methanogenesis trait (gonzalez2023biologicalhydrogenmethanation pages 13-15, gonzalez2023biologicalhydrogenmethanation pages 16-17, chen2024functionalbiocharas pages 1-3, sinorosszabo2024carboncaptureand pages 1-2).

### DOI-first bibliography (with publication dates and URLs)
- de Mesquita, C.P.B. et al. (Mar 2023). *Methyl-Based Methanogenesis: an Ecological and Genomic Review*. **Microbiology and Molecular Biology Reviews** 87(1). https://doi.org/10.1128/mmbr.00024-22 (mesquita2023methylbasedmethanogenesisan pages 8-11, mesquita2023methylbasedmethanogenesisan pages 4-5, mesquita2023methylbasedmethanogenesisan pages 2-4, mesquita2023methylbasedmethanogenesisan pages 11-13, mesquita2023methylbasedmethanogenesisan pages 23-24, mesquita2023methylbasedmethanogenesisan pages 7-8, mesquita2023methylbasedmethanogenesisan pages 5-7, mesquita2023methylbasedmethanogenesisan media 81c08583, mesquita2023methylbasedmethanogenesisan media 479fdb47)
- Khairunisa, B.H. et al. (Nov 2023). *Evolving understanding of rumen methanogen ecophysiology*. **Frontiers in Microbiology** 14. https://doi.org/10.3389/fmicb.2023.1296008 (khairunisa2023evolvingunderstandingof pages 11-12, khairunisa2023evolvingunderstandingof pages 10-11, khairunisa2023evolvingunderstandingof pages 2-3)
- Szuhaj, M. et al. (Aug 2023). *Regulation of the methanogenesis pathways by hydrogen at transcriptomic level in time*. **Applied Microbiology and Biotechnology** 107:6315–6324. https://doi.org/10.1007/s00253-023-12700-3 (szuhaj2023regulationofthe pages 1-2)
- Niya, B. et al. (Mar 2024). *Current status and future developments of assessing microbiome composition and dynamics in anaerobic digestion systems using metagenomic approaches*. **Heliyon** 10:e28221. https://doi.org/10.1016/j.heliyon.2024.e28221 (niya2024currentstatusand pages 10-11)
- Zbair, M. et al. (Jul 2024). *Integration of Digestate-Derived Biochar into the Anaerobic Digestion Process through Circular Economic and Environmental Approaches—A Review*. **Materials** 17:3527. https://doi.org/10.3390/ma17143527 (zbair2024integrationofdigestatederived pages 4-6)
- Chen, B. et al. (Jun 2024). *Functional biochar as sustainable precursors to boost the anaerobic digestion of waste activated sludge from a circular economy perspective: a review*. **Biochar** 6:1–24. https://doi.org/10.1007/s42773-024-00345-y (chen2024functionalbiocharas pages 1-3)
- Ellenbogen, J.B. et al. (Jan 2024). *Methylotrophy in the Mire: direct and indirect routes for methane production in thawing permafrost*. **mSystems** 9(1). https://doi.org/10.1128/msystems.00698-23 (ellenbogen2024methylotrophyinthe pages 5-7)
- Sieborg, M.U. et al. (Aug 2024). *Bio-integrated carbon capture and utilization: at the interface between capture chemistry and archaeal CO2 reduction*. **Nature Communications** 15. https://doi.org/10.1038/s41467-024-51700-3 (sieborg2024biointegratedcarboncapture pages 1-2)
- Sinóros-Szabó, B. (Mar 2024). *Carbon Capture and Utilization Technology Development Opportunities Based on Biomethanation*. **Periodica Polytechnica Chemical Engineering** 68:162–171. https://doi.org/10.3311/ppch.22248 (sinorosszabo2024carboncaptureand pages 1-2, sinorosszabo2024carboncaptureand pages 2-4)
- González, R. et al. (May 2023). *Biological Hydrogen Methanation with Carbon Dioxide Utilization: Methanation Acting as Mediator in the Hydrogen Economy*. **Environments** 10(5):82. https://doi.org/10.3390/environments10050082 (gonzalez2023biologicalhydrogenmethanation pages 13-15, gonzalez2023biologicalhydrogenmethanation pages 16-17, gonzalez2023biologicalhydrogenmethanation pages 23-24, gonzalez2023biologicalhydrogenmethanation pages 7-8)
- Khan, S. et al. (Nov 2024). *Coal-straw co-digestion-induced biogenic methane production: perspectives on microbial communities and associated metabolic pathways*. **Scientific Reports** 14. https://doi.org/10.1038/s41598-024-75655-z (khan2024coalstrawcodigestioninducedbiogenic pages 1-2)

### Visual evidence (tables/figures)
- Gene/substrate summary tables for methyl-based methanogenesis and cross-pathway marker genes, including universal requirement for **mcrABG/mcrA**, are shown in de Mesquita et al. (2023) (mesquita2023methylbasedmethanogenesisan media 81c08583, mesquita2023methylbasedmethanogenesisan media 479fdb47).

References

1. (szuhaj2023regulationofthe pages 1-2): Márk Szuhaj, Balázs Kakuk, Roland Wirth, Gábor Rákhely, Kornél Lajos Kovács, and Zoltán Bagi. Regulation of the methanogenesis pathways by hydrogen at transcriptomic level in time. Applied Microbiology and Biotechnology, 107:6315-6324, Aug 2023. URL: https://doi.org/10.1007/s00253-023-12700-3, doi:10.1007/s00253-023-12700-3. This article has 26 citations and is from a domain leading peer-reviewed journal.

2. (mesquita2023methylbasedmethanogenesisan pages 2-4): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

3. (mesquita2023methylbasedmethanogenesisan pages 4-5): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

4. (zbair2024integrationofdigestatederived pages 4-6): Mohamed Zbair, Lionel Limousy, Méghane Drané, Charlotte Richard, Marine Juge, Quentin Aemig, Eric Trably, Renaud Escudié, Christine Peyrelasse, and Simona Bennici. Integration of digestate-derived biochar into the anaerobic digestion process through circular economic and environmental approaches—a review. Materials, 17:3527, Jul 2024. URL: https://doi.org/10.3390/ma17143527, doi:10.3390/ma17143527. This article has 23 citations.

5. (mesquita2023methylbasedmethanogenesisan pages 8-11): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

6. (khairunisa2023evolvingunderstandingof pages 10-11): Bela Haifa Khairunisa, Christian Heryakusuma, Kelechi Ike, Biswarup Mukhopadhyay, and Dwi Susanti. Evolving understanding of rumen methanogen ecophysiology. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1296008, doi:10.3389/fmicb.2023.1296008. This article has 67 citations and is from a peer-reviewed journal.

7. (mesquita2023methylbasedmethanogenesisan media 81c08583): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

8. (mesquita2023methylbasedmethanogenesisan media 479fdb47): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

9. (khairunisa2023evolvingunderstandingof pages 2-3): Bela Haifa Khairunisa, Christian Heryakusuma, Kelechi Ike, Biswarup Mukhopadhyay, and Dwi Susanti. Evolving understanding of rumen methanogen ecophysiology. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1296008, doi:10.3389/fmicb.2023.1296008. This article has 67 citations and is from a peer-reviewed journal.

10. (ellenbogen2024methylotrophyinthe pages 5-7): Jared B. Ellenbogen, Mikayla A. Borton, Bridget B. McGivern, Dylan R. Cronin, David W. Hoyt, Viviana Freire-Zapata, Carmody K. McCalley, Ruth K. Varner, Patrick M. Crill, Richard A. Wehr, Jeffrey P. Chanton, Ben J. Woodcroft, Malak M. Tfaily, Gene W. Tyson, Virginia I. Rich, and Kelly C. Wrighton. Methylotrophy in the mire: direct and indirect routes for methane production in thawing permafrost. Jan 2024. URL: https://doi.org/10.1128/msystems.00698-23, doi:10.1128/msystems.00698-23. This article has 30 citations and is from a peer-reviewed journal.

11. (khairunisa2023evolvingunderstandingof pages 11-12): Bela Haifa Khairunisa, Christian Heryakusuma, Kelechi Ike, Biswarup Mukhopadhyay, and Dwi Susanti. Evolving understanding of rumen methanogen ecophysiology. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1296008, doi:10.3389/fmicb.2023.1296008. This article has 67 citations and is from a peer-reviewed journal.

12. (sieborg2024biointegratedcarboncapture pages 1-2): Mads Ujarak Sieborg, Amalie Kirstine Hessellund Nielsen, Lars Ditlev Mørck Ottosen, Kim Daasbjerg, and Michael Vedel Wegener Kofoed. Bio-integrated carbon capture and utilization: at the interface between capture chemistry and archaeal co2 reduction. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51700-3, doi:10.1038/s41467-024-51700-3. This article has 53 citations and is from a highest quality peer-reviewed journal.

13. (khan2024coalstrawcodigestioninducedbiogenic pages 1-2): Sohail Khan, Ze Deng, Bobo Wang, and Zhisheng Yu. Coal-straw co-digestion-induced biogenic methane production: perspectives on microbial communities and associated metabolic pathways. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-75655-z, doi:10.1038/s41598-024-75655-z. This article has 12 citations and is from a peer-reviewed journal.

14. (chen2024functionalbiocharas pages 1-3): Bi Chen, Hong Zeng, Fan Yang, Yafei Yang, Zhi Qiao, Xiaoli Zhao, Li Wang, and Fengchang Wu. Functional biochar as sustainable precursors to boost the anaerobic digestion of waste activated sludge from a circular economy perspective: a review. Biochar, 6:1-24, Jun 2024. URL: https://doi.org/10.1007/s42773-024-00345-y, doi:10.1007/s42773-024-00345-y. This article has 43 citations.

15. (mishra2024useofconductive pages 3-6): Satchidananda Mishra, Sagarika Panigrahi, and Debapriya Kar. Use of conductive material in the anaerobic digestion for improving process performance. Waste-to-Wealth, pages 162-175, Oct 2024. URL: https://doi.org/10.1201/9781003327646-11, doi:10.1201/9781003327646-11. This article has 1 citations.

16. (sinorosszabo2024carboncaptureand pages 1-2): Botond Sinóros-Szabó. Carbon capture and utilization technology development opportunities based on biomethanation. Periodica Polytechnica Chemical Engineering, 68:162-171, Mar 2024. URL: https://doi.org/10.3311/ppch.22248, doi:10.3311/ppch.22248. This article has 0 citations.

17. (gonzalez2023biologicalhydrogenmethanation pages 13-15): Rubén González, Iván Orlando Cabeza, Miguel Casallas-Ojeda, and Xiomar Gómez. Biological hydrogen methanation with carbon dioxide utilization: methanation acting as mediator in the hydrogen economy. Environments, 10:82, May 2023. URL: https://doi.org/10.3390/environments10050082, doi:10.3390/environments10050082. This article has 20 citations.

18. (gonzalez2023biologicalhydrogenmethanation pages 16-17): Rubén González, Iván Orlando Cabeza, Miguel Casallas-Ojeda, and Xiomar Gómez. Biological hydrogen methanation with carbon dioxide utilization: methanation acting as mediator in the hydrogen economy. Environments, 10:82, May 2023. URL: https://doi.org/10.3390/environments10050082, doi:10.3390/environments10050082. This article has 20 citations.

19. (mesquita2023methylbasedmethanogenesisan pages 7-8): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

20. (mesquita2023methylbasedmethanogenesisan pages 11-13): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

21. (niya2024currentstatusand pages 10-11): Btissam Niya, Kaoutar Yaakoubi, Fatima Zahra Beraich, Moha Arouch, and Issam Meftah Kadmiri. Current status and future developments of assessing microbiome composition and dynamics in anaerobic digestion systems using metagenomic approaches. Heliyon, 10:e28221, Mar 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e28221, doi:10.1016/j.heliyon.2024.e28221. This article has 32 citations.

22. (sinorosszabo2024carboncaptureand pages 2-4): Botond Sinóros-Szabó. Carbon capture and utilization technology development opportunities based on biomethanation. Periodica Polytechnica Chemical Engineering, 68:162-171, Mar 2024. URL: https://doi.org/10.3311/ppch.22248, doi:10.3311/ppch.22248. This article has 0 citations.

23. (mesquita2023methylbasedmethanogenesisan pages 23-24): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

24. (mesquita2023methylbasedmethanogenesisan pages 5-7): Clifton P. Bueno de Mesquita, Dongying Wu, and Susannah G. Tringe. Methyl-based methanogenesis: an ecological and genomic review. Microbiology and Molecular Biology Reviews, Mar 2023. URL: https://doi.org/10.1128/mmbr.00024-22, doi:10.1128/mmbr.00024-22. This article has 133 citations and is from a domain leading peer-reviewed journal.

25. (gonzalez2023biologicalhydrogenmethanation pages 23-24): Rubén González, Iván Orlando Cabeza, Miguel Casallas-Ojeda, and Xiomar Gómez. Biological hydrogen methanation with carbon dioxide utilization: methanation acting as mediator in the hydrogen economy. Environments, 10:82, May 2023. URL: https://doi.org/10.3390/environments10050082, doi:10.3390/environments10050082. This article has 20 citations.

26. (gonzalez2023biologicalhydrogenmethanation pages 7-8): Rubén González, Iván Orlando Cabeza, Miguel Casallas-Ojeda, and Xiomar Gómez. Biological hydrogen methanation with carbon dioxide utilization: methanation acting as mediator in the hydrogen economy. Environments, 10:82, May 2023. URL: https://doi.org/10.3390/environments10050082, doi:10.3390/environments10050082. This article has 20 citations.