---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:52:44.498464'
end_time: '2026-06-18T04:08:07.736257'
duration_seconds: 923.24
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: anaerobic oxidation of methane
  trait_identifier: traitmech:000033
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: anaerobic_oxidation_of_methane
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which methane is oxidized under anoxic conditions, classically
    coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic
    archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in
    marine sediments.
  parent_traits: METPO:1000802
  synonyms: AOM, anaerobic methanotrophy
  evidence_summary: 'DOI:10.1038/35036572:  (Boetius et al. described the marine microbial
    consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation
    of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments
    supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane
    sink.)'
  causal_graph_summary: 'aom_anme_sulfate_consortium: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** anaerobic oxidation of methane
- **METPO identifier:** traitmech:000033
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is oxidized under anoxic conditions, classically coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in marine sediments.
- **Parent traits:** METPO:1000802
- **Synonyms:** AOM, anaerobic methanotrophy
- **Existing evidence:** DOI:10.1038/35036572:  (Boetius et al. described the marine microbial consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane sink.)
- **Existing causal graph summary:** aom_anme_sulfate_consortium: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **anaerobic oxidation of methane** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_oxidation_of_methane.yaml`.

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
- **Trait label:** anaerobic oxidation of methane
- **METPO identifier:** traitmech:000033
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which methane is oxidized under anoxic conditions, classically coupled to sulfate reduction and mediated by consortia of anaerobic methanotrophic archaea (ANME) and sulfate-reducing bacteria. It is a major sink for methane in marine sediments.
- **Parent traits:** METPO:1000802
- **Synonyms:** AOM, anaerobic methanotrophy
- **Existing evidence:** DOI:10.1038/35036572:  (Boetius et al. described the marine microbial consortium of ANME archaea and sulfate-reducing bacteria mediating anaerobic oxidation of methane.) | DOI:10.3389/fmars.2025.1609892:  (Review of AOM in marine sediments supports sulfate- and metal-coupled anaerobic methane oxidation as a major methane sink.)
- **Existing causal graph summary:** aom_anme_sulfate_consortium: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **anaerobic oxidation of methane** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/anaerobic_oxidation_of_methane.yaml`.

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


## Research report: Anaerobic oxidation of methane (AOM) as a TraitMech causal graph candidate

### Trait summary and scope (TraitMech target)
**Trait label:** anaerobic oxidation of methane (AOM)  
**METPO identifier:** traitmech:000033  
**Working definition (curation scope):** A microbial metabolic capacity to oxidize methane under anoxic conditions, coupled to an external electron acceptor (classically sulfate, but also nitrate/nitrite, Fe(III)/Mn(IV) oxides, or electrodes), and mediated either by archaeal **reverse methanogenesis** (MCR-dependent) or by **intra-aerobic** nitrite-dependent bacterial pathways that generate intracellular O2 from NO (Methylomirabilis). (zheng2023intermediatesproductionin pages 5-7, wissink2024probingdenitrifyinganaerobic pages 1-2, yao2024methanedependentcompletedenitrification pages 1-3)

**Included in-scope subtypes**
- **Sulfate-driven AOM (SD-AOM):** ANME archaea in obligate syntrophy with sulfate-reducing bacteria (SRB), with electron sharing via DIET-like conduits. (murali2023physiologicalpotentialand pages 1-2)
- **Nitrate/nitrite-driven AOM (N-DAMO / denitrifying AOM):** e.g., *Ca.* Methanoperedens nitrate-to-nitrite reduction coupled to reverse methanogenesis; nitrite-driven intra-aerobic methane oxidation by *Ca.* Methylomirabilis; and (newly) single-organism methane-dependent complete denitrification by *Ca.* Methylomirabilis sinica. (wissink2024probingdenitrifyinganaerobic pages 1-2, zheng2023intermediatesproductionin pages 5-7, yao2024methanedependentcompletedenitrification pages 1-3)
- **Metal-dependent AOM:** Fe(III)/Mn(IV) as terminal electron acceptors, potentially via extracellular electron transfer (EET) through multiheme cytochromes and/or conductive structures. (sivan2024enigmaticfemnfueledanaerobic pages 1-4, slobodkin2023compositionandmetabolic pages 8-9)
- **Electrode-coupled AOM:** methane-dependent current generation with ANME (e.g., *Ca.* Methanoperedens) in bioelectrochemical systems. (ouboter2024mechanismsofextracellular pages 16-21)

**Boundary cases / exclusions**
- **Classical aerobic methane oxidation by MOB requiring external O2** is not AOM (even if occurring at oxic–anoxic interfaces); however, *Methylomirabilis* intra-aerobic methane oxidation is **included** because methane oxidation proceeds in anoxic bulk conditions using internally generated O2 from NO dismutation. (wissink2024probingdenitrifyinganaerobic pages 1-2, zheng2023intermediatesproductionin pages 5-7)
- **Methanogenesis** (CH4 production) is a related but distinct trait; it shares MCR homologs and gene markers, and can be coupled tightly to AOM in “cryptic methane cycling”. (krause2024spatialevidenceof pages 1-6)

### Key concepts and current understanding (mechanistic overview)

#### 1) Core intracellular pathway: reverse methanogenesis (archaeal AOM)
A central concept for archaeal AOM is that methane oxidation proceeds by **reversing the methanogenesis pathway** (“reverse methanogenesis”). In a reviewed mechanistic description of denitrification-coupled methane oxidation, methane is first converted to methyl-S-CoM by **methyl-coenzyme M reductase (MCR)** and then proceeds through methyl transfer to H4MPT (via **Mtr**) and subsequent oxidation steps toward CO2. (zheng2023intermediatesproductionin pages 5-7)

This makes **MCR and its genes (mcrA; mcrABCD)** high-value nodes for TraitMech graphs and high-value biomarkers for detecting AOM potential/activity (with the caveat that mcr genes also occur in methanogens and alkane-activating archaea). Marker-gene co-occurrence of **mcrA** with sulfate-reduction markers (**dsrAB, aprAB**) is used as evidence for sulfate-driven AOM consortia in marine subsurface sediments. (schnabel2024influenceofminor pages 17-20)

#### 2) Syntrophic sulfate-AOM and DIET
Sulfate-coupled AOM is performed by multicellular consortia of ANME archaea in **obligate syntrophy** with SRB. Comparative genomics of four major syntrophic SRB clades (HotSeep-1, Seep-SRB2, Seep-SRB1a, Seep-SRB1g) supports that **direct interspecies electron transfer (DIET)**-related complexes transferring electrons from ANME to the SRB outer membrane are conserved, while inner-membrane electron transfer modules differ, suggesting convergent evolution. (murali2023physiologicalpotentialand pages 1-2)

#### 3) Denitrifying AOM and intra-aerobic nitrite-dependent methanotrophy
In N-DAMO enrichment communities, *Ca.* Methanoperedens nitroreducens oxidizes methane via reverse methanogenesis and couples it to nitrate reduction to nitrite; *Ca.* Methylomirabilis oxyfera reduces nitrite to NO, dismutates NO to N2 and O2, and uses the produced O2 with pMMO to activate methane. (wissink2024probingdenitrifyinganaerobic pages 1-2)

A major 2024 development is the demonstration that a single bacterium, *Candidatus Methylomirabilis sinica*, can carry out **methane-dependent complete denitrification** (complete nitrate reduction to N2) in one organism, revising earlier models that implied obligatory division of labor among multiple organisms for complete denitrification-linked methane oxidation. (yao2024methanedependentcompletedenitrification pages 1-3)

#### 4) Metal-oxide and electrode electron acceptors; extracellular electron transfer
Recent work emphasizes EET as a key mechanistic bridge between methane oxidation and insoluble electron acceptors (metals, electrodes) in ANME.
- An ANME-2d (*Ca.* Methanoperedens) enrichment in bioelectrochemical systems showed **strong methane-dependent current**, with *Ca.* Methanoperedens highly enriched on anodes; transcriptomic evidence pointed to **OmcZ-like nanowires** and an uncharacterized short-range electron transport complex. (ouboter2024mechanismsofextracellular pages 16-21)
- Fe/Mn-AOM is thermodynamically more favorable than sulfate-AOM in principle, and is discussed as potentially mediated via direct contact, electron shuttles/chelates, or nanowires, with multiheme cytochromes invoked for metal reduction by some ANME lineages. (sivan2024enigmaticfemnfueledanaerobic pages 1-4)
- In Fe(III)-reducing ANME-2a enrichments, ANME MAGs encode reverse-methanogenesis genes and many multiheme cytochromes, supporting a capacity for EET to Fe(III)/Mn(IV) oxides or partners. (slobodkin2023compositionandmetabolic pages 8-9)

### Candidate nodes for curation (grouped by type, with grounding suggestions)
The following artifact provides a candidate node list aligned to TraitMech needs.

| Node type | Label | Brief definition / role in AOM | Suggested grounding CURIE | Supporting citation snippet with reference |
|---|---|---|---|---|
| Organism/taxon | ANME (anaerobic methanotrophic archaea) | Archaeal methane oxidizers central to AOM; include marine and freshwater clades and can couple methane oxidation to sulfate, nitrate/nitrite-associated processes, metals, or electrodes depending on lineage/context | NCBITaxon:label ANME | “anaerobic methanotrophic archaea (ANME) … mitigating the release of the potent greenhouse gas methane” and ANME can engage in EET with “other microorganisms, metal oxides, and electrodes” (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21, ouboter2024mechanismsofextracellular pages 1-5) |
| Organism/taxon | ANME-2a | ANME subclade enriched in Fe(III)-reducing methane-oxidizing cultures; encodes reverse-methanogenesis genes and many MHCs | NCBITaxon:label ANME-2a | “we enriched a microbial community containing ANME-2a, using methane as an electron donor, Fe(III) oxide (ferrihydrite) as an electron acceptor” and ANME-2a MAGs contained “mcrABCD” and numerous MHC genes (Slobodkin et al. 2023, DOI:10.3390/microorganisms11030555, https://doi.org/10.3390/microorganisms11030555) (slobodkin2023compositionandmetabolic pages 8-9) |
| Organism/taxon | ANME-2d / Methanoperedenaceae | Freshwater/nitrate- or electrode-associated ANME lineage; often represented by Methanoperedens and notable for extracellular electron transfer | NCBITaxon:label ANME-2d | “we cultivated ANME-2d archaea (‘Ca. Methanoperedens’) in bioelectrochemical systems” and observed methane-dependent current (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21) |
| Organism/taxon | Sulfate-reducing bacteria (SRB) | Canonical syntrophic bacterial partners in sulfate-coupled AOM consortia; receive electrons from ANME and reduce sulfate | NCBITaxon:label sulfate-reducing bacteria | “sulfate-coupled AOM is performed by multicellular consortia of anaerobic methanotrophic archaea (ANME) in obligate syntrophic partnership with sulfate-reducing bacteria (SRB)” (Murali et al. 2023, DOI:10.1371/journal.pbio.3002292, https://doi.org/10.1371/journal.pbio.3002292) (murali2023physiologicalpotentialand pages 1-2) |
| Organism/taxon | Seep-SRB clades (Seep-SRB1a, Seep-SRB1g, Seep-SRB2, HotSeep-1) | Major syntrophic SRB lineages associated with ANME in sulfate-AOM; differ in inner-membrane electron transfer and nutritional traits | NCBITaxon:label Seep-SRB clades | “the 4 main syntrophic SRB clades (HotSeep-1, Seep-SRB2, Seep-SRB1a, and Seep-SRB1g)” were compared for adaptation to syntrophy (Murali et al. 2023, DOI:10.1371/journal.pbio.3002292, https://doi.org/10.1371/journal.pbio.3002292) (murali2023physiologicalpotentialand pages 1-2) |
| Organism/taxon | Candidatus Methanoperedens nitroreducens | ANME-2d archaeon that performs reverse-methanogenesis-based methane oxidation coupled to nitrate reduction; also electroactive in some studies | NCBITaxon:2480895 | “‘Ca. Methanoperedens nitroreducens’ performs methane oxidation via a reverse methanogenesis pathway … coupling to nitrate reduction to nitrite” (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Organism/taxon | Candidatus Methylomirabilis oxyfera | NC10 bacterium carrying out nitrite-dependent methane oxidation via intra-aerobic metabolism using internally generated O2 | NCBITaxon:label Candidatus Methylomirabilis oxyfera | “‘Ca. Methylomirabilis oxyfera’ uses an intra-aerobic pathway that reduces nitrite to nitric oxide, dismutates NO to N2 and O2, and uses the produced O2 with particulate methane monooxygenase (pMMO) to activate methane” (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Organism/taxon | Candidatus Methylomirabilis sinica | Purified denitrifying methanotroph able to couple methane oxidation to complete nitrate reduction to N2 in one organism | NCBITaxon:label Candidatus Methylomirabilis sinica | “a purified bacterium, ‘Candidatus Methylomirabilis sinica’, that alone couples aerobic methane oxidation to complete denitrification: methane-dependent complete nitrate reduction to N2” (Yao et al. 2024, DOI:10.1038/s41564-023-01578-6, https://doi.org/10.1038/s41564-023-01578-6) (yao2024methanedependentcompletedenitrification pages 1-3) |
| Pathway/process | Reverse methanogenesis | Core intracellular pathway for many archaeal AOM lineages; methane is activated to methyl-S-CoM and oxidized to CO2 | GO:label reverse methanogenesis | “AOM proceeds via the reverse methanogenesis pathway: CH4 is converted to methyl-S-CoM by Mcr … then oxidized to CO2” (Zheng et al. 2023, DOI:10.3390/fermentation9070645, https://doi.org/10.3390/fermentation9070645) (zheng2023intermediatesproductionin pages 5-7) |
| Pathway/process | Direct interspecies electron transfer (DIET) | Electron-sharing mechanism from ANME to SRB in sulfate-AOM consortia | GO:label direct interspecies electron transfer | “protein complexes involved in direct interspecies electron transfer (DIET) from ANME to the SRB outer membrane are conserved” (Murali et al. 2023, DOI:10.1371/journal.pbio.3002292, https://doi.org/10.1371/journal.pbio.3002292) (murali2023physiologicalpotentialand pages 1-2) |
| Pathway/process | Extracellular electron transfer (EET) | Electron transfer from ANME to external acceptors such as metal oxides or electrodes | GO:label extracellular electron transfer | “During methane oxidation ANME archaea engage in extracellular electron transfer (EET) with other microorganisms, metal oxides, and electrodes” (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21) |
| Pathway/process | Sulfate reduction | Terminal respiratory process in bacterial partners of sulfate-AOM consortia; couples to electron uptake from ANME | GO:0000103 | “sulfate-coupled AOM is performed by multicellular consortia … with sulfate-reducing bacteria” (Murali et al. 2023, DOI:10.1371/journal.pbio.3002292, https://doi.org/10.1371/journal.pbio.3002292) (murali2023physiologicalpotentialand pages 1-2) |
| Pathway/process | Denitrification / nitrate- and nitrite-dependent AOM | Methane oxidation linked to reduction of nitrate/nitrite; includes archaeal and bacterial variants | GO:0019646 | “methane-dependent complete nitrate reduction to N2” and nitrate/nitrite are documented electron acceptors for methane oxidation (Yao et al. 2024, DOI:10.1038/s41564-023-01578-6, https://doi.org/10.1038/s41564-023-01578-6; Zheng et al. 2023, DOI:10.3390/fermentation9070645, https://doi.org/10.3390/fermentation9070645) (yao2024methanedependentcompletedenitrification pages 1-3, zheng2023intermediatesproductionin pages 5-7) |
| Pathway/process | Nitric oxide dismutation | Proposed/central intra-aerobic step in Methylomirabilis generating intracellular O2 from NO | GO:label nitric oxide dismutation | “a proposed NO dismutase (NOD) could convert NO to N2 and O2 enabling aerobic methane oxidation under anaerobic conditions” (Zheng et al. 2023, DOI:10.3390/fermentation9070645, https://doi.org/10.3390/fermentation9070645) (zheng2023intermediatesproductionin pages 5-7) |
| Gene/protein/complex | Methyl-coenzyme M reductase (MCR) | Methane-activating enzyme for reverse methanogenesis; key catalytic entry point in archaeal AOM | EC:2.8.4.1 | “methane activation by methyl-coenzyme M reductase (MCR)” in reverse-methanogenesis AOM (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Gene/protein/complex | mcrA / mcrABCD | Marker gene / catalytic subunit set for MCR and reverse methanogenesis in ANME | label:mcrA / label:mcrABCD | “ANME MAGs encode core reverse-methanogenesis… methyl-coenzyme M reductase (mcrABCD)” and “Marker genes for … methanogenesis and methanotrophy (i.e. mcrA)” (Slobodkin et al. 2023, DOI:10.3390/microorganisms11030555, https://doi.org/10.3390/microorganisms11030555; Schnabel et al. 2024, DOI:10.5194/egusphere-2024-1603, https://doi.org/10.5194/egusphere-2024-1603) (slobodkin2023compositionandmetabolic pages 8-9, schnabel2024influenceofminor pages 17-20) |
| Gene/protein/complex | Mtr (tetrahydromethanopterin S-methyltransferase) | Transfers methyl group in reverse methanogenesis after methane activation | EC:2.1.1.86 | “CH4 is converted to methyl-S-CoM by Mcr … methyl transferred to H4MPT by Mtr” (Zheng et al. 2023, DOI:10.3390/fermentation9070645, https://doi.org/10.3390/fermentation9070645) (zheng2023intermediatesproductionin pages 5-7) |
| Gene/protein/complex | HdrDE | Membrane heterodisulfide reductase complex routing electrons from CoM-S-S-CoB to quinone pools in Methanoperedens-like nitrate-AOM | EC:1.8.98.1 | “electrons from CoM-S-S-CoB are routed via HdrDE to menaquinone (MQ) and the quinone loop to Nar” (Zheng et al. 2023, DOI:10.3390/fermentation9070645, https://doi.org/10.3390/fermentation9070645) (zheng2023intermediatesproductionin pages 5-7) |
| Gene/protein/complex | NarG(H) / nitrate reductase | Terminal reductase enabling nitrate respiration in nitrate-dependent AOM | EC:1.7.5.1 | “narGH nitrate reductase is present in M. nitroreducens” (Zheng et al. 2023, DOI:10.3390/fermentation9070645, https://doi.org/10.3390/fermentation9070645) (zheng2023intermediatesproductionin pages 5-7) |
| Gene/protein/complex | pMMO (particulate methane monooxygenase) | Methane-activating enzyme in intra-aerobic Methylomirabilis metabolism using internally produced O2 | EC:1.14.18.3 | “‘Ca. M. oxyfera’ … uses the produced O2 with particulate methane monooxygenase (pMMO) to activate methane” (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Gene/protein/complex | Multiheme c-type cytochromes (MHCs) | Candidate surface/extracellular redox proteins supporting EET to metals, electrodes, or partners | label:multiheme c-type cytochromes | “genomic and expression data indicate extracellular MHCs are differentially expressed with different acceptors” and support “cytochrome-mediated EET to metals and electrodes” (Zhang et al. 2023, DOI unavailable in context) (zhang2023multihemecytochromemediatedextracellular pages 1-2) |
| Gene/protein/complex | OmcZ-like nanowires | Putative conductive extracellular filaments implicated in electrode-associated EET in ANME-2d/Methanoperedens | label:OmcZ-like nanowires | “suggesting a unique EET pathway in all ANME-2 archaea … involvement of … OmcZ nanowires” (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21) |
| Electron acceptor/donor/metabolite | Methane | Electron donor and substrate oxidized in AOM | CHEBI:16183 | “using methane as an electron donor” in ANME-2a Fe(III)-reducing enrichments (Slobodkin et al. 2023, DOI:10.3390/microorganisms11030555, https://doi.org/10.3390/microorganisms11030555) (slobodkin2023compositionandmetabolic pages 8-9) |
| Electron acceptor/donor/metabolite | Sulfate | Classical terminal electron acceptor in marine AOM consortia | CHEBI:16189 | “sulfate-coupled AOM” and “porewater sulfate was high and non-limiting (9–91 mM)” in marsh AOM zones (Murali et al. 2023, DOI:10.1371/journal.pbio.3002292, https://doi.org/10.1371/journal.pbio.3002292; Krause et al. 2024, DOI:10.1101/2024.07.16.603764, https://doi.org/10.1101/2024.07.16.603764) (murali2023physiologicalpotentialand pages 1-2, krause2024spatialevidenceof pages 1-6) |
| Electron acceptor/donor/metabolite | Nitrate | Electron acceptor for Methanoperedens and for complete denitrification by Methylomirabilis sinica | CHEBI:17632 | “methane-dependent complete nitrate reduction to N2” and Methanoperedens couples methane oxidation “to nitrate reduction to nitrite” (Yao et al. 2024, DOI:10.1038/s41564-023-01578-6, https://doi.org/10.1038/s41564-023-01578-6; Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (yao2024methanedependentcompletedenitrification pages 1-3, wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Electron acceptor/donor/metabolite | Nitrite | Electron acceptor in nitrite-dependent methane oxidation by Methylomirabilis and in sewer n-DAMO implementations | CHEBI:16301 | “‘Ca. M. oxyfera’ uses an intra-aerobic pathway that reduces nitrite to nitric oxide” (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Electron acceptor/donor/metabolite | Fe(III) / ferric iron | Alternative electron acceptor in metal-dependent AOM; often supplied as ferrihydrite or ferric citrate | CHEBI:18248 | “metal oxides (Fe(III), Mn(IV))” are documented acceptors and ANME-2a was enriched with “Fe(III) oxide (ferrihydrite) as an electron acceptor” (Zhang et al. 2023, DOI unavailable in context; Slobodkin et al. 2023, DOI:10.3390/microorganisms11030555, https://doi.org/10.3390/microorganisms11030555) (zhang2023multihemecytochromemediatedextracellular pages 1-2, slobodkin2023compositionandmetabolic pages 8-9) |
| Electron acceptor/donor/metabolite | Mn(IV) / manganese oxide | Alternative electron acceptor in metal-dependent AOM; thermodynamically favorable | CHEBI:18291 | “Terminal electron acceptors include Fe(III) and Mn(IV)” and MnO2-driven AOM is thermodynamically favorable (Sivan et al. 2024, DOI:10.5194/egusphere-2024-1829, https://doi.org/10.5194/egusphere-2024-1829) (sivan2024enigmaticfemnfueledanaerobic pages 1-4) |
| Electron acceptor/donor/metabolite | Ferrihydrite | Reactive Fe(III) oxyhydroxide used experimentally and considered highly bioavailable for Fe-AOM | CHEBI:label ferrihydrite | “using methane as an electron donor, Fe(III) oxide (ferrihydrite) as an electron acceptor” and ferrihydrite supports higher AOM activity (Slobodkin et al. 2023, DOI:10.3390/microorganisms11030555, https://doi.org/10.3390/microorganisms11030555; Sivan et al. 2024, DOI:10.5194/egusphere-2024-1829, https://doi.org/10.5194/egusphere-2024-1829) (slobodkin2023compositionandmetabolic pages 8-9, sivan2024enigmaticfemnfueledanaerobic pages 1-4) |
| Electron acceptor/donor/metabolite | Birnessite | Mn oxide used as a model solid electron acceptor in Methanoperedens EET studies | CHEBI:label birnessite | Methanoperedenaceae species are linked to “ferrihydrite, birnessite reduction” (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21) |
| Electron acceptor/donor/metabolite | Electrode / anode | Experimental solid electron acceptor for electrode-AOM and cultivation of electroactive ANME | ENVO:label electrode | “‘Ca. Methanoperedens’ on the anode” produced “strong methane-dependent current” in bioelectrochemical systems (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21) |
| Environmental/experimental factor | Sulfate–methane transition zone (SMTZ) | Sediment depth interval where methane and sulfate overlap and AOM is commonly concentrated | ENVO:label sulfate-methane transition zone | “AOM rates … overlapped with methylotrophic methanogenesis” in sulfate-rich marsh intervals interpreted as “SMTZ-like overlap” (Krause et al. 2024, DOI:10.1101/2024.07.16.603764, https://doi.org/10.1101/2024.07.16.603764) (krause2024spatialevidenceof pages 1-6, krause2024spatialevidenceof pages 40-44) |
| Environmental/experimental factor | 2-bromoethanesulfonate (2-BES) | MCR inhibitor used to probe archaeal reverse-methanogenesis AOM | CHEBI:label 2-bromoethanesulfonate | “2-BES inhibited ‘Ca. M. nitroreducens’” and “MCR inhibition (2-bromoethanosulfonate) strongly reduces current” (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197; Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (wissink2024probingdenitrifyinganaerobic pages 1-2, ouboter2024mechanismsofextracellular pages 16-21) |
| Environmental/experimental factor | 1,7-octadiyne | pMMO inhibitor used to probe bacterial nitrite-dependent methane oxidation | CHEBI:label 1,7-octadiyne | “1,7-octadiyne (pMMO inhibitor) at 100 μM inhibited ‘Ca. M. oxyfera’” (Wissink et al. 2024, DOI:10.1021/acs.est.3c07197, https://doi.org/10.1021/acs.est.3c07197) (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| Assay/measurement/biomarker | dsrAB | Marker gene for dissimilatory sulfate reduction associated with sulfate-driven AOM consortia | label:dsrAB | “Marker genes for … sulfate reduction (i.e. dsrAB, aprAB) … revealed metabolic activities by a consortium of sulfate-reducing bacteria and ANME archaea” (Schnabel et al. 2024, DOI:10.5194/egusphere-2024-1603, https://doi.org/10.5194/egusphere-2024-1603) (schnabel2024influenceofminor pages 17-20) |
| Assay/measurement/biomarker | aprAB | Additional sulfate-reduction biomarker supporting sulfate-AOM | label:aprAB | “Marker genes for … sulfate reduction (i.e. dsrAB, aprAB)” (Schnabel et al. 2024, DOI:10.5194/egusphere-2024-1603, https://doi.org/10.5194/egusphere-2024-1603) (schnabel2024influenceofminor pages 17-20) |
| Assay/measurement/biomarker | mcrA | Functional marker for methanogenesis/methanotrophy used to infer AOM potential/activity | label:mcrA | “Marker genes for … methanogenesis and methanotrophy (i.e. mcrA)” (Schnabel et al. 2024, DOI:10.5194/egusphere-2024-1603, https://doi.org/10.5194/egusphere-2024-1603) (schnabel2024influenceofminor pages 17-20) |
| Assay/measurement/biomarker | Methane-dependent current | Electrochemical readout of electrode-coupled AOM in bioelectrochemical systems | label:methane-dependent current | “strong methane-dependent current (91-93% of total current) associated with high enrichment of ‘Ca. Methanoperedens’ on the anode” (Ouboter et al. 2024, DOI:10.1101/2023.07.24.550278, https://doi.org/10.1101/2023.07.24.550278) (ouboter2024mechanismsofextracellular pages 16-21) |
| Assay/measurement/biomarker | AOM rate | Rate measurement for methane consumption in field incubations; useful phenotype-level readout | label:AOM rate | “AOM rates (14C-CH4) … ranged 0.03–19.4 nmol cm-3 d-1” in salt-marsh sediments (Krause et al. 2024, DOI:10.1101/2024.07.16.603764, https://doi.org/10.1101/2024.07.16.603764) (krause2024spatialevidenceof pages 1-6) |
| Assay/measurement/biomarker | Sulfate reduction rate | Complementary rate readout used to contextualize sulfate-coupled AOM zones | label:sulfate reduction rate | “sulfate reduction rates 1.5–2,506 nmol cm-3 d-1” in sulfate-rich marsh sediments supporting sulfate-coupled AOM potential (Krause et al. 2024, DOI:10.1101/2024.07.16.603764, https://doi.org/10.1101/2024.07.16.603764) (krause2024spatialevidenceof pages 1-6) |


*Table: This table lists candidate TraitMech nodes for anaerobic oxidation of methane, grouped by entity type and annotated with proposed ontology groundings and evidence snippets. It is designed to support curation of a causal graph by highlighting organisms, pathways, molecular machinery, electron acceptors, experimental factors, and measurable biomarkers.*

### Evidence-backed candidate causal edges (triples)
The following artifact compiles candidate edges with supporting snippets and references, marking edges as core/optional/uncertain for curation.

| Subject | Subject grounding | Predicate | Object | Object grounding | Edge type | Context | Supporting snippet / quote | Reference |
|---|---|---|---|---|---|---|---|---|
| anaerobic oxidation of methane | METPO:traitmech:000033 | has_core_pathway | reverse methanogenesis | label: reverse methanogenesis | core | general AOM | “AOM proceeds via the reverse methanogenesis pathway: CH4 is converted to methyl-S-CoM by Mcr … then oxidized to CO2.” (zheng2023intermediatesproductionin pages 5-7) | Zheng et al. 2023. DOI:10.3390/fermentation9070645. https://doi.org/10.3390/fermentation9070645 |
| methyl-coenzyme M reductase (MCR) | EC:2.8.4.1 | catalyzes_initial_step_of | anaerobic oxidation of methane | METPO:traitmech:000033 | core | general AOM | “methane activation by methyl-coenzyme M reductase (MCR)” and MCR is the methane-activation step in reverse methanogenesis (wissink2024probingdenitrifyinganaerobic pages 1-2, zheng2023intermediatesproductionin pages 5-7) | Wissink et al. 2024. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197; Zheng et al. 2023. DOI:10.3390/fermentation9070645. https://doi.org/10.3390/fermentation9070645 |
| mcrABCD genes | label: mcrABCD | enables | reverse methanogenesis capacity in ANME-2a | NCBITaxon:label ANME-2a | core | metal-AOM | “ANME MAGs encode core reverse-methanogenesis… mtrABCDEFGH and methyl-coenzyme M reductase (mcrABCD)” (slobodkin2023compositionandmetabolic pages 8-9) | Slobodkin et al. 2023. DOI:10.3390/microorganisms11030555. https://doi.org/10.3390/microorganisms11030555 |
| sulfate | CHEBI:16189 | serves_as_terminal_electron_acceptor_for | anaerobic oxidation of methane | METPO:traitmech:000033 | core | sulfate-AOM | “sulfate-coupled AOM is performed by multicellular consortia of anaerobic methanotrophic archaea (ANME) in obligate syntrophic partnership with sulfate-reducing bacteria (SRB)” (murali2023physiologicalpotentialand pages 1-2) | Murali et al. 2023. DOI:10.1371/journal.pbio.3002292. https://doi.org/10.1371/journal.pbio.3002292 |
| ANME archaea | NCBITaxon:label ANME | forms_obligate_syntrophy_with | sulfate-reducing bacteria | label: sulfate-reducing bacteria (SRB) | core | sulfate-AOM | “obligate syntrophic partnership with sulfate-reducing bacteria (SRB)” (murali2023physiologicalpotentialand pages 1-2) | Murali et al. 2023. DOI:10.1371/journal.pbio.3002292. https://doi.org/10.1371/journal.pbio.3002292 |
| direct interspecies electron transfer (DIET) complexes | label: DIET complexes | mediate_electron_transfer_from | ANME archaea to SRB outer membrane | NCBITaxon:label ANME / label: SRB outer membrane | core | sulfate-AOM | “protein complexes involved in direct interspecies electron transfer (DIET) from ANME to the SRB outer membrane are conserved” (murali2023physiologicalpotentialand pages 1-2) | Murali et al. 2023. DOI:10.1371/journal.pbio.3002292. https://doi.org/10.1371/journal.pbio.3002292 |
| CbcBA pathway genes | label: CbcBA | contributes_to_adaptation_for | syntrophic electron transfer lifestyle | label: syntrophic electron transfer lifestyle | optional | sulfate-AOM | “adaptation likely occurred … involve horizontal gene transfers within pathways for electron transfer (CbcBA)” (murali2023physiologicalpotentialand pages 1-2) | Murali et al. 2023. DOI:10.1371/journal.pbio.3002292. https://doi.org/10.1371/journal.pbio.3002292 |
| Pel biofilm genes | label: Pel | contributes_to | biofilm formation in syntrophic SRB partners | label: biofilm formation | optional | sulfate-AOM | “horizontal gene transfers within pathways for electron transfer (CbcBA) and biofilm formation (Pel)” (murali2023physiologicalpotentialand pages 1-2) | Murali et al. 2023. DOI:10.1371/journal.pbio.3002292. https://doi.org/10.1371/journal.pbio.3002292 |
| dsrAB | label: dsrAB | biomarker_of | sulfate reduction associated with sulfate-driven AOM | GO:0000103? / label: sulfate reduction | optional | sulfate-AOM | “Marker genes for … sulfate reduction (i.e. dsrAB, aprAB), methanogenesis and methanotrophy (i.e. mcrA) revealed metabolic activities by a consortium of sulfate-reducing bacteria and ANME archaea” (schnabel2024influenceofminor pages 17-20) | Schnabel et al. 2024. DOI:10.5194/egusphere-2024-1603. https://doi.org/10.5194/egusphere-2024-1603 |
| aprAB | label: aprAB | biomarker_of | sulfate reduction associated with sulfate-driven AOM | label: sulfate reduction | optional | sulfate-AOM | “Marker genes for … sulfate reduction (i.e. dsrAB, aprAB)” (schnabel2024influenceofminor pages 17-20) | Schnabel et al. 2024. DOI:10.5194/egusphere-2024-1603. https://doi.org/10.5194/egusphere-2024-1603 |
| mcrA | label: mcrA | biomarker_of | methanotrophic/methanogenic methane-cycling activity in AOM settings | label: methane cycling activity | optional | sulfate-AOM, cryptic methane cycling | “Marker genes for … methanogenesis and methanotrophy (i.e. mcrA)” (schnabel2024influenceofminor pages 17-20) | Schnabel et al. 2024. DOI:10.5194/egusphere-2024-1603. https://doi.org/10.5194/egusphere-2024-1603 |
| nitrate | CHEBI:17632 | serves_as_terminal_electron_acceptor_for | nitrate-dependent AOM by Methanoperedens | NCBITaxon:2480895 | core | nitrate/nitrite-DAMO | “‘Ca. Methanoperedens nitroreducens’ performs methane oxidation via a reverse methanogenesis pathway … coupling to nitrate reduction to nitrite.” (wissink2024probingdenitrifyinganaerobic pages 1-2) | Wissink et al. 2024. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197 |
| nitrite | CHEBI:16301 | serves_as_terminal_electron_acceptor_for | nitrite-dependent methane oxidation by Methylomirabilis | NCBITaxon:label Candidatus Methylomirabilis | core | nitrate/nitrite-DAMO | “‘Ca. Methylomirabilis oxyfera’ uses an intra-aerobic pathway that reduces nitrite to nitric oxide” (wissink2024probingdenitrifyinganaerobic pages 1-2) | Wissink et al. 2024. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197 |
| Candidatus Methanoperedens nitroreducens | NCBITaxon:2480895 | reduces | nitrate to nitrite during AOM | CHEBI:16301 | core | nitrate/nitrite-DAMO | “coupling to nitrate reduction to nitrite” (wissink2024probingdenitrifyinganaerobic pages 1-2) | Wissink et al. 2024. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197 |
| Nar / narGH nitrate reductase | label: narGH / nitrate reductase | enables | nitrate-dependent AOM in Methanoperedens | NCBITaxon:2480895 | core | nitrate/nitrite-DAMO | “narGH nitrate reductase is present in M. nitroreducens” (zheng2023intermediatesproductionin pages 5-7) | Zheng et al. 2023. DOI:10.3390/fermentation9070645. https://doi.org/10.3390/fermentation9070645 |
| nitric oxide dismutase (candidate NOD) | label: nitric oxide dismutase | converts | nitric oxide to dinitrogen and oxygen | CHEBI:16480 / CHEBI:15379 | core | nitrate/nitrite-DAMO | “a proposed NO dismutase (NOD) could convert NO to N2 and O2 enabling aerobic methane oxidation under anaerobic conditions” (zheng2023intermediatesproductionin pages 5-7) | Zheng et al. 2023. DOI:10.3390/fermentation9070645. https://doi.org/10.3390/fermentation9070645 |
| intracellular oxygen from NO dismutation | CHEBI:15379 | enables | methane oxidation by particulate methane monooxygenase | EC:1.14.18.3 | core | nitrate/nitrite-DAMO | “uses intracellular oxygen produced by nitric oxide dismutation to support methane oxidation” (yao2024methanedependentcompletedenitrification pages 1-3) | Yao et al. 2024. DOI:10.1038/s41564-023-01578-6. https://doi.org/10.1038/s41564-023-01578-6 |
| Candidatus Methylomirabilis sinica | NCBITaxon:label Candidatus Methylomirabilis sinica | performs | methane-dependent complete denitrification to N2 | label: complete denitrification to N2 | core | nitrate/nitrite-DAMO | “a purified bacterium, ‘Candidatus Methylomirabilis sinica’, that alone couples aerobic methane oxidation to complete denitrification: methane-dependent complete nitrate reduction to N2” (yao2024methanedependentcompletedenitrification pages 1-3) | Yao et al. 2024. DOI:10.1038/s41564-023-01578-6. https://doi.org/10.1038/s41564-023-01578-6 |
| ferric iron / Fe(III) oxides | CHEBI:18248 | serves_as_terminal_electron_acceptor_for | metal-dependent AOM | label: Fe-AOM | core | metal-AOM | “Documented electron acceptors include … metal oxides (Fe(III), Mn(IV))” and “supporting iron-dependent AOM” (zhang2023multihemecytochromemediatedextracellular pages 1-2) | Zhang et al. 2023. DOI unavailable in provided context; 2023 URL not provided in context |
| manganese(IV) oxides | CHEBI:18291 | serves_as_terminal_electron_acceptor_for | metal-dependent AOM | label: Mn-AOM | optional | metal-AOM | “Terminal electron acceptors include Fe(III) and Mn(IV) … Fe-/Mn-(oxyhydr)oxides” (sivan2024enigmaticfemnfueledanaerobic pages 1-4) | Sivan et al. 2024. DOI:10.5194/egusphere-2024-1829. https://doi.org/10.5194/egusphere-2024-1829 |
| ANME-2 variants | NCBITaxon:label ANME-2 | can_reduce | metal oxides via multiheme cytochromes | label: metal oxides / multiheme cytochromes | optional | metal-AOM | “ANME-2 variants can reduce metal oxides via multiheme cytochromes without partners” (sivan2024enigmaticfemnfueledanaerobic pages 1-4) | Sivan et al. 2024. DOI:10.5194/egusphere-2024-1829. https://doi.org/10.5194/egusphere-2024-1829 |
| multiheme c-type cytochromes (MHCs) | label: multiheme c-type cytochromes | mediate | extracellular electron transfer to Fe(III) or electrodes | label: extracellular electron transfer | core | metal-AOM, electrode-AOM | “genomic and expression data indicate extracellular MHCs are differentially expressed with different acceptors” and support “cytochrome-mediated EET to metals and electrodes” (zhang2023multihemecytochromemediatedextracellular pages 1-2) | Zhang et al. 2023. DOI unavailable in provided context; 2023 URL not provided in context |
| Candidatus Methanoperedens | NCBITaxon:2480895 | produces_methane-dependent_current_on | anode electrode | ENVO:label electrode / anode | core | electrode-AOM | “strong methane-dependent current (91-93% of total current) associated with high enrichment of ‘Ca. Methanoperedens’ on the anode” (ouboter2024mechanismsofextracellular pages 16-21) | Ouboter et al. 2024. DOI:10.1101/2023.07.24.550278. https://doi.org/10.1101/2023.07.24.550278 |
| OmcZ-like nanowires | label: OmcZ nanowires | participates_in | extracellular electron transfer in ANME-2d | NCBITaxon:label ANME-2d / Methanoperedenaceae | core | electrode-AOM | “suggesting a unique EET pathway … involvement of an … short-range electron transport protein complex and OmcZ nanowires” (ouboter2024mechanismsofextracellular pages 16-21) | Ouboter et al. 2024. DOI:10.1101/2023.07.24.550278. https://doi.org/10.1101/2023.07.24.550278 |
| short-range electron transport protein complex | label: short-range electron transport protein complex | participates_in | extracellular electron transfer in ANME archaea | NCBITaxon:label ANME archaea | optional | electrode-AOM | “pointing to the involvement of an so far uncharacterized short-range electron transport protein complex” (ouboter2024mechanismsofextracellular pages 16-21) | Ouboter et al. 2024. DOI:10.1101/2023.07.24.550278. https://doi.org/10.1101/2023.07.24.550278 |
| ferrihydrite reduction by AOM enrichment | CHEBI:label ferrihydrite | is_associated_with | Fe3+ reduction stoichiometry near 1:8 with methane oxidation | label: Fe3+ reduction stoichiometry 1:8 | optional | metal-AOM | “Fe3+ reduction occurred at a stoichiometry near 1:8, supporting iron-dependent AOM” (zhang2023multihemecytochromemediatedextracellular pages 1-2) | Zhang et al. 2023. DOI unavailable in provided context; 2023 URL not provided in context |
| 2-bromoethanesulfonate (2-BES) | CHEBI:label 2-bromoethanesulfonate | inhibits | MCR-dependent AOM in Methanoperedens | EC:2.8.4.1 / NCBITaxon:2480895 | core | nitrate/nitrite-DAMO, electrode-AOM | “2-BES inhibited ‘Ca. M. nitroreducens’” and “MCR inhibition (2-bromoethanosulfonate) strongly reduces current” (wissink2024probingdenitrifyinganaerobic pages 1-2, ouboter2024mechanismsofextracellular pages 16-21) | Wissink et al. 2024. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197; Ouboter et al. 2024. DOI:10.1101/2023.07.24.550278. https://doi.org/10.1101/2023.07.24.550278 |
| 1,7-octadiyne | CHEBI:label 1,7-octadiyne | inhibits | particulate methane monooxygenase in Methylomirabilis | EC:1.14.18.3 | core | nitrate/nitrite-DAMO | “1,7-octadiyne (pMMO inhibitor) at 100 μM inhibited ‘Ca. M. oxyfera’” (wissink2024probingdenitrifyinganaerobic pages 1-2) | Wissink et al. 2024. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197 |
| sulfate-rich porewater | label: high sulfate porewater | supports | AOM overlapping with sulfate reduction in marsh sediments | label: sulfate-coupled AOM zone | optional | cryptic methane cycling | “Porewater sulfate was high and non-limiting (9–91 mM), with sulfate reduction rates 1.5–2,506 nmol cm-3 d-1, indicating strong potential for sulfate-coupled AOM” (krause2024spatialevidenceof pages 1-6) | Krause et al. 2024. DOI:10.1101/2024.07.16.603764. https://doi.org/10.1101/2024.07.16.603764 |
| cryptic methane cycling | label: cryptic methane cycling | includes_concurrent | methylotrophic methanogenesis and AOM | label: methylotrophic methanogenesis / anaerobic oxidation of methane | optional | cryptic methane cycling | “AOM rates … overlapped with methylotrophic methanogenesis … consistent with a cryptic methane cycle where concurrent methanogenesis … and AOM prevent methane buildup” (krause2024spatialevidenceof pages 1-6) | Krause et al. 2024. DOI:10.1101/2024.07.16.603764. https://doi.org/10.1101/2024.07.16.603764 |
| direct cell contact / electron shuttles / nanowires | label: direct contact / electron shuttles / nanowires | may_mediate | Fe-Mn-coupled AOM electron transfer | label: Fe-Mn-AOM electron transfer | uncertain | metal-AOM | “potential electron-transfer routes include direct cell contact, electron shuttles, metal chelates, and nanowires” (sivan2024enigmaticfemnfueledanaerobic pages 1-4) | Sivan et al. 2024. DOI:10.5194/egusphere-2024-1829. https://doi.org/10.5194/egusphere-2024-1829 |


*Table: This table lists candidate subject–predicate–object edges for curating a TraitMech causal graph of anaerobic oxidation of methane. It spans core intracellular methane activation, syntrophic sulfate-AOM, denitrifying AOM, metal/electrode electron transfer, inhibitors, and biomarker genes, using only the provided evidence contexts.*

### Recent developments (prioritizing 2023–2024)

1) **Electrode-AOM and archaeal EET machinery (2024):** Bioelectrochemical cultivation of ANME-2d (*Ca.* Methanoperedens) showed methane-dependent current and implicated OmcZ-like nanowires and a short-range electron transport complex, supporting electrode/solid-acceptor AOM as both an ecological and experimental platform for isolating electroactive ANME. (ouboter2024mechanismsofextracellular pages 16-21)

2) **New metabolic capability in NC10/Methylomirabilis (2024):** *Ca.* Methylomirabilis sinica performs methane-dependent complete denitrification as a single bacterium. This changes how “denitrifying AOM” may be represented in causal graphs (i.e., not necessarily requiring archaeal–bacterial division of labor in all contexts). (yao2024methanedependentcompletedenitrification pages 1-3)

3) **Comparative genomics of syntrophic SRB partners (2023):** Conservation of DIET-related outer-membrane conduits across SRB lineages and diversification of inner-membrane electron transfer components (including HGT in CbcBA electron transfer and Pel biofilm genes) provides a mechanistic/evolutionary basis for representing “SRB partner capacity” as modular rather than taxonomically fixed. (murali2023physiologicalpotentialand pages 1-2)

4) **Cryptic methane cycling quantified in coastal wetland sediment (2024):** Radiotracer incubations across a land–ocean salt marsh transect reported AOM rates spanning ~0.03–19.4 nmol cm−3 d−1 and sulfate reduction rates up to ~2,506 nmol cm−3 d−1, supporting a model where concurrent AOM and methylotrophic methanogenesis prevent methane build-up (cryptic cycling). (krause2024spatialevidenceof pages 1-6)

5) **Subsurface/low-flux seepage contexts and marker genes (2024):** At minor hydrocarbon seepage sites, sulfate reduction rates were extremely low (≤300 pmol cm−3 d−1) while meta-omics marker genes (dsrAB/aprAB/mcrA) supported depth-localized sulfate-driven AOM activity. This highlights that gene evidence may indicate AOM even when in-interval rates are low and processes occur below the sampled zone. (schnabel2024influenceofminor pages 17-20)

### Current applications and real-world implementations (with quantitative metrics)

#### 1) Sewer methane + sulfide control via nitrite dosing (2024)
A continuous nitrite-dosed sewer reactor (>120 days) demonstrated coupled **nitrite-dependent anaerobic methane oxidation (n-DAMO)** and nitrite-driven sulfide oxidation. Key performance data:
- Dissolved methane decreased by ~53% during the first 120 days (from 18.5 ± 3.5 to 8.5 ± 2.9 mg CH4/L), and ~58% overall reduction was reported. (zuo2024nitritedependentmicrobialutilization pages 1-2)
- Sulfide removal averaged ~71% (to ~8.1 ± 6.6 mg S/L), with >90% sulfide removal noted in the abstract. (zuo2024nitritedependentmicrobialutilization pages 1-2)
- Batch oxidation rates: ~15.6 mg CH4/(L·h) and ~29.4 mg S/(L·h); mass balance indicated ~70% of dosed nitrite was consumed via n-DAMO (with batch calculations attributing ~78% of nitrite reduction to n-DAMO). (zuo2024nitritedependentmicrobialutilization pages 1-2, zuo2024nitritedependentmicrobialutilization pages 3-5)
These results demonstrate an implementable control strategy in engineered sewers where nitrite supply can be sustained (e.g., from partial nitridation of urine). (zuo2024nitritedependentmicrobialutilization pages 1-2)

#### 2) Denitrification coupled to methane oxidation in a fixed-bed reactor (2024)
An upflow fixed-bed bioreactor (UFBR) for denitrification coupled to methane oxidation (DOM) under anoxic conditions reported:
- Long stabilization/startup: stable nitrogen removal after ~400 days. (molinamacias2024implementationofan pages 1-2)
- After stabilization: maximum nitrite and nitrate removal rates of 17.6 mgN-NO2−/L-d and 8.9 mgN-NO3−/L-d, and methane removal efficiency up to 77% (with up to 90% nitrite/nitrate removal after 400 days). (molinamacias2024implementationofan pages 1-2)
This provides realistic deployment constraints (slow biomass development) and performance envelopes for scaling beyond commonly used membrane/SBR configurations. (molinamacias2024implementationofan pages 1-2)

#### 3) Wastewater deployment constraints: inhibitor sensitivity and heavy-metal tolerance (2024)
Antimicrobial intervention in N-DAMO enrichment cultures provides actionable constraints for engineered systems:
- 2-BES inhibited *Ca.* Methanoperedens nitroreducens (MCR-linked), while 1,7-octadiyne inhibited *Ca.* Methylomirabilis oxyfera (pMMO-linked). (wissink2024probingdenitrifyinganaerobic pages 1-2)
- Heavy metals: the community showed high tolerance to Pb (IC50 > 1000 µM; 100–500 µM no significant impact; 10 µM Pb increased AOM rate by 38 ± 7%), but susceptibility to Ni (IC50 0.23 mM) and strong toxicity of Cd (IC50 < 10 µM; methane oxidation abolished at 500 µM). (wissink2024probingdenitrifyinganaerobic pages 5-7)
- Ammonium: AOM IC50 52 mM; typical wastewater levels (~2 mM) should not hinder N-DAMO, although activity decreased at 20–100 mM. (wissink2024probingdenitrifyinganaerobic pages 5-7)

### Expert interpretation / curation guidance (authoritative analysis grounded in sources)

1) **Graph modularity is essential:** AOM is not a single mechanism but a family of methane-oxidizing phenotypes coupled to multiple acceptors. The causal graph should thus include (a) a shared “methane oxidation module” (reverse methanogenesis/MCR for ANME) and (b) acceptor-specific “terminal electron accepting/EET modules” (sulfate+SRB DIET; nitrate/nitrite+Nar/Nap/nir/nor+NO dismutation; metals+MHC/EET; electrode+nanowires). (zheng2023intermediatesproductionin pages 5-7, murali2023physiologicalpotentialand pages 1-2, wissink2024probingdenitrifyinganaerobic pages 1-2, ouboter2024mechanismsofextracellular pages 16-21, sivan2024enigmaticfemnfueledanaerobic pages 1-4)

2) **Sulfate-AOM edges should encode syntrophy explicitly:** Murali et al. provides evidence for conserved DIET complexes bridging ANME to SRB outer membranes; these should be represented as mechanistic intermediate nodes/edges rather than a single direct “ANME causes sulfate reduction” edge. (murali2023physiologicalpotentialand pages 1-2)

3) **Denitrifying AOM should represent alternative organismal implementations:** The existence of *Methylomirabilis sinica* performing methane-dependent complete denitrification suggests that “methane oxidation coupled to denitrification” should not be hard-coded as strictly archaeal–bacterial syntrophy in all environments. Consider encoding optional edges for single-organism denitrifying methane oxidation in NC10 lineages. (yao2024methanedependentcompletedenitrification pages 1-3)

4) **EET nodes are key for metals/electrodes but remain partially unresolved:** Ouboter et al. points to OmcZ-like nanowires and an uncharacterized short-range complex; these are strong candidates for nodes, but the mechanistic completeness (e.g., exact protein identities and electron path) is still emerging and may warrant “uncertain” labeling for some edges. (ouboter2024mechanismsofextracellular pages 16-21)

### Statistics and quantitative data (recent)
- Salt-marsh sediments: AOM rates 0.03–19.4 nmol cm−3 d−1; sulfate reduction rates 1.5–2,506 nmol cm−3 d−1; sulfate 9–91 mM (non-limiting). (krause2024spatialevidenceof pages 1-6)
- Subsurface seepage setting: sulfate reduction rate ≤300 pmol cm−3 d−1; CH4 < 10 µM at sampled core bottoms; dsrAB/aprAB/mcrA markers support sulfate-AOM consortia. (schnabel2024influenceofminor pages 17-20)
- Sewer n-DAMO implementation: methane reduced 53% (18.5 ± 3.5 to 8.5 ± 2.9 mg CH4/L); sulfide removal ~71%; methane oxidation 15.6 mg CH4/(L·h). (zuo2024nitritedependentmicrobialutilization pages 1-2)
- UFBR DOM implementation: methane removal up to 77%; nitrate removal rate 8.9 mgN-NO3−/L-d; nitrite removal rate 17.6 mgN-NO2−/L-d; stabilization ~400 days. (molinamacias2024implementationofan pages 1-2)
- N-DAMO tolerance: Pb IC50 >1000 µM; Ni IC50 0.23 mM; Cd IC50 <10 µM; ammonium IC50 52 mM. (wissink2024probingdenitrifyinganaerobic pages 5-7)

### Warnings / claims not ready for strong curation
- **Metal-AOM electron-transfer mechanism diversity:** Proposed mechanisms (nanowires, chelates, shuttles, direct contact) are often hypothesis-level in geochemical syntheses; treat these as **uncertain** unless supported by organism-specific molecular evidence (e.g., demonstrated MHC expression/localization and stoichiometry). (sivan2024enigmaticfemnfueledanaerobic pages 1-4)
- **Marker genes are not uniquely diagnostic:** mcrA indicates methane cycling (methanogenesis or methanotrophy) and must be contextualized with geochemistry, rates, and partner markers (e.g., dsrAB/aprAB for sulfate-AOM). (schnabel2024influenceofminor pages 17-20)
- **Zhang 2023 Methanoperedens EET paper lacks stable DOI in retrieved context:** edges drawn from it should be treated as provisional until the final journal/DOI metadata is verified. (zhang2023multihemecytochromemediatedextracellular pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates when available)

- Ouboter HT, et al. *Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea.* bioRxiv. Posted 2023-07-24; accessed in 2024. DOI:10.1101/2023.07.24.550278. https://doi.org/10.1101/2023.07.24.550278 (ouboter2024mechanismsofextracellular pages 16-21, ouboter2024mechanismsofextracellular pages 1-5)
- Murali R, et al. *Physiological potential and evolutionary trajectories of syntrophic sulfate-reducing bacterial partners of anaerobic methanotrophic archaea.* PLOS Biology. 2023-09. DOI:10.1371/journal.pbio.3002292. https://doi.org/10.1371/journal.pbio.3002292 (murali2023physiologicalpotentialand pages 1-2)
- Wissink M, et al. *Probing Denitrifying Anaerobic Methane Oxidation via Antimicrobial Intervention: Implications for Innovative Wastewater Management.* Environmental Science & Technology. 2024-03. DOI:10.1021/acs.est.3c07197. https://doi.org/10.1021/acs.est.3c07197 (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 5-7)
- Yao X, et al. *Methane-dependent complete denitrification by a single Methylomirabilis bacterium.* Nature Microbiology. 2024-01. DOI:10.1038/s41564-023-01578-6. https://doi.org/10.1038/s41564-023-01578-6 (yao2024methanedependentcompletedenitrification pages 1-3)
- Zuo Z, et al. *Nitrite-dependent microbial utilization for simultaneous removal of sulfide and methane in sewers.* Water Research X. 2024-09. DOI:10.1016/j.wroa.2024.100231. https://doi.org/10.1016/j.wroa.2024.100231 (zuo2024nitritedependentmicrobialutilization pages 1-2, zuo2024nitritedependentmicrobialutilization pages 3-5)
- Molina-Macías AK, et al. *Implementation of an Upflow Fixed Bed Bioreactor for Denitrification Coupled to Methane Oxidation: Performance and Biomass Development Under Anoxic Conditions.* Water, Air, & Soil Pollution. 2024-10. DOI:10.1007/s11270-024-07555-x. https://doi.org/10.1007/s11270-024-07555-x (molinamacias2024implementationofan pages 1-2)
- Krause SJE, et al. *Spatial evidence of cryptic methane cycling and methylotrophic metabolisms along a land-ocean transect in a southern California salt marsh.* bioRxiv. Posted 2024-07-16. DOI:10.1101/2024.07.16.603764. https://doi.org/10.1101/2024.07.16.603764 (krause2024spatialevidenceof pages 1-6, krause2024spatialevidenceof pages 23-30, krause2024spatialevidenceof pages 40-44)
- Schnabel E, et al. *Influence of minor hydrocarbon seepage on sulfur cycling in marine subsurface sediments and its significance for hydrocarbon reservoir detection.* EGUsphere (preprint). 2024-07. DOI:10.5194/egusphere-2024-1603. https://doi.org/10.5194/egusphere-2024-1603 (schnabel2024influenceofminor pages 17-20)
- Slobodkin AI, et al. *Composition and Metabolic Potential of Fe(III)-Reducing Enrichment Cultures of Methanotrophic ANME-2a Archaea and Associated Bacteria.* Microorganisms. 2023-02. DOI:10.3390/microorganisms11030555. https://doi.org/10.3390/microorganisms11030555 (slobodkin2023compositionandmetabolic pages 8-9)
- Zheng X-C, et al. *Intermediates Production in Methane Oxidation Coupled with Denitrification: Current Status, Challenges, and Future Opportunities.* Fermentation. 2023-07. DOI:10.3390/fermentation9070645. https://doi.org/10.3390/fermentation9070645 (zheng2023intermediatesproductionin pages 5-7)
- Sivan K, et al. *Enigmatic Fe-Mn-fueled Anaerobic Oxidation of Methane in sulfidic coastal sediments of the Eastern Arabian Sea.* EGUsphere (preprint). 2024-07. DOI:10.5194/egusphere-2024-1829. https://doi.org/10.5194/egusphere-2024-1829 (sivan2024enigmaticfemnfueledanaerobic pages 1-4)
- Zhang X, et al. *Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph ‘Candidatus Methanoperedens nitroreducens’.* 2023. (DOI not available in retrieved context; treat as provisional until verified). (zhang2023multihemecytochromemediatedextracellular pages 1-2)


References

1. (zheng2023intermediatesproductionin pages 5-7): Xiao-Chuan Zheng, Hong-Shan Li, Zi-Han Wang, Zhong-Fang Sun, and Lei Zhao. Intermediates production in methane oxidation coupled with denitrification: current status, challenges, and future opportunities. Fermentation, 9:645, Jul 2023. URL: https://doi.org/10.3390/fermentation9070645, doi:10.3390/fermentation9070645. This article has 15 citations.

2. (wissink2024probingdenitrifyinganaerobic pages 1-2): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 16 citations and is from a domain leading peer-reviewed journal.

3. (yao2024methanedependentcompletedenitrification pages 1-3): Xiangwu Yao, Jiaqi Wang, Mingyue He, Zishu Liu, Yuxiang Zhao, Yufen Li, Taolve Chi, Lin Zhu, Ping Zheng, Mike S. M. Jetten, and Baolan Hu. Methane-dependent complete denitrification by a single methylomirabilis bacterium. Nature microbiology, 9:464-476, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01578-6, doi:10.1038/s41564-023-01578-6. This article has 97 citations and is from a highest quality peer-reviewed journal.

4. (murali2023physiologicalpotentialand pages 1-2): Ranjani Murali, Hang Yu, Daan R. Speth, Fabai Wu, Kyle S. Metcalfe, Antoine Crémière, Rafael Laso-Pèrez, Rex R. Malmstrom, Danielle Goudeau, Tanja Woyke, Roland Hatzenpichler, Grayson L. Chadwick, Stephanie A. Connon, and Victoria J. Orphan. Physiological potential and evolutionary trajectories of syntrophic sulfate-reducing bacterial partners of anaerobic methanotrophic archaea. PLOS Biology, 21:e3002292, Sep 2023. URL: https://doi.org/10.1371/journal.pbio.3002292, doi:10.1371/journal.pbio.3002292. This article has 55 citations and is from a highest quality peer-reviewed journal.

5. (sivan2024enigmaticfemnfueledanaerobic pages 1-4): Kalyani Sivan, Aditya Peketi, Aninda Mazumdar, Anjali Zatale, Sai Pavan Kumar Pillutla, Ankita Ghosh, Mohd Sadique, and Jittu Mathai. Enigmatic fe-mn-fueled anaerobic oxidation of methane in sulfidic coastal sediments of the eastern arabian sea. Jul 2024. URL: https://doi.org/10.5194/egusphere-2024-1829, doi:10.5194/egusphere-2024-1829.

6. (slobodkin2023compositionandmetabolic pages 8-9): Alexander I. Slobodkin, Nataliya M. Ratnikova, Galina B. Slobodkina, Alexandra A. Klyukina, Nikolay A. Chernyh, and Alexander Y. Merkel. Composition and metabolic potential of fe(iii)-reducing enrichment cultures of methanotrophic anme-2a archaea and associated bacteria. Microorganisms, 11:555, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030555, doi:10.3390/microorganisms11030555. This article has 31 citations.

7. (ouboter2024mechanismsofextracellular pages 16-21): Heleen T Ouboter, Rob Mesman, Tom Sleutels, Jelle Postma, Martijn Wissink, Mike S M Jetten, Annemiek ter Heijne, Tom Berben, and Cornelia U Welte. Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2023.07.24.550278, doi:10.1101/2023.07.24.550278. This article has 69 citations.

8. (krause2024spatialevidenceof pages 1-6): Sebastian J.E. Krause, Rebecca Wipfler, Jiarui Liu, David J. Yousavich, DeMarcus Robinson, David W. Hoyt, Victoria J. Orphan, and Tina Treude. Spatial evidence of cryptic methane cycling and methylotrophic metabolisms along a land-ocean transect in a southern california salt marsh. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.07.16.603764, doi:10.1101/2024.07.16.603764. This article has 2 citations.

9. (schnabel2024influenceofminor pages 17-20): Ellen Schnabel, Aurèle Vuillemin, Cédric C. Laczny, Benoit J. Kunath, André R. Soares, Rolando Di Primio, and Jens Kallmeyer. Influence of minor hydrocarbon seepage on sulfur cycling in marine subsurface sediments and its significance for hydrocarbon reservoir detection. Unknown journal, Jul 2024. URL: https://doi.org/10.5194/egusphere-2024-1603, doi:10.5194/egusphere-2024-1603.

10. (ouboter2024mechanismsofextracellular pages 1-5): Heleen T Ouboter, Rob Mesman, Tom Sleutels, Jelle Postma, Martijn Wissink, Mike S M Jetten, Annemiek ter Heijne, Tom Berben, and Cornelia U Welte. Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2023.07.24.550278, doi:10.1101/2023.07.24.550278. This article has 69 citations.

11. (zhang2023multihemecytochromemediatedextracellular pages 1-2): X Zhang, GH Joyce, AO Leu, J Zhao, and H Rabiee. Multi-heme cytochrome-mediated extracellular electron transfer by the anaerobic methanotroph 'candidatus methanoperedens nitroreducens'. Unknown journal, 2023.

12. (krause2024spatialevidenceof pages 40-44): Sebastian J.E. Krause, Rebecca Wipfler, Jiarui Liu, David J. Yousavich, DeMarcus Robinson, David W. Hoyt, Victoria J. Orphan, and Tina Treude. Spatial evidence of cryptic methane cycling and methylotrophic metabolisms along a land-ocean transect in a southern california salt marsh. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.07.16.603764, doi:10.1101/2024.07.16.603764. This article has 2 citations.

13. (zuo2024nitritedependentmicrobialutilization pages 1-2): Zhiqiang Zuo, Yaxin Xing, Xi Lu, Tao Liu, Min Zheng, Miao Guo, Yanchen Liu, and Xia Huang. Nitrite-dependent microbial utilization for simultaneous removal of sulfide and methane in sewers. Sep 2024. URL: https://doi.org/10.1016/j.wroa.2024.100231, doi:10.1016/j.wroa.2024.100231. This article has 10 citations and is from a peer-reviewed journal.

14. (zuo2024nitritedependentmicrobialutilization pages 3-5): Zhiqiang Zuo, Yaxin Xing, Xi Lu, Tao Liu, Min Zheng, Miao Guo, Yanchen Liu, and Xia Huang. Nitrite-dependent microbial utilization for simultaneous removal of sulfide and methane in sewers. Sep 2024. URL: https://doi.org/10.1016/j.wroa.2024.100231, doi:10.1016/j.wroa.2024.100231. This article has 10 citations and is from a peer-reviewed journal.

15. (molinamacias2024implementationofan pages 1-2): Anngie K. Molina-Macías, Yudy Andrea Londoño, Nancy Pino, and Gustavo A. Peñuela. Implementation of an upflow fixed bed bioreactor for denitrification coupled to methane oxidation: performance and biomass development under anoxic conditions. Water, Air, &amp; Soil Pollution, Oct 2024. URL: https://doi.org/10.1007/s11270-024-07555-x, doi:10.1007/s11270-024-07555-x. This article has 2 citations.

16. (wissink2024probingdenitrifyinganaerobic pages 5-7): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 16 citations and is from a domain leading peer-reviewed journal.

17. (krause2024spatialevidenceof pages 23-30): Sebastian J.E. Krause, Rebecca Wipfler, Jiarui Liu, David J. Yousavich, DeMarcus Robinson, David W. Hoyt, Victoria J. Orphan, and Tina Treude. Spatial evidence of cryptic methane cycling and methylotrophic metabolisms along a land-ocean transect in a southern california salt marsh. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.07.16.603764, doi:10.1101/2024.07.16.603764. This article has 2 citations.