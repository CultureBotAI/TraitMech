---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:50:00.767440'
end_time: '2026-06-18T04:11:58.720345'
duration_seconds: 1317.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Aerobic respiration
  trait_identifier: METPO:1000801
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: aerobic_respiration
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A respiration in which molecular oxygen serves as the terminal electron
    acceptor in the electron transport chain, generating ATP through oxidative phosphorylation
    with water as the final product.
  parent_traits: METPO:1000800
  synonyms: Oxic respiration, Oxygen respiration
  evidence_summary: 'DOI:10.1146/annurev.biophys.27.1.329: terminal enzyme of respiratory
    chains (Review supports cytochrome c oxidase reducing molecular oxygen to water
    in aerobic respiratory chains.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound
    electron transport chain (Review supports proton-gradient energy conservation
    by prokaryotic respiratory chains.)'
  causal_graph_summary: 'aerobic_respiration_terminal_oxidase: 8 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 64
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Aerobic respiration
- **METPO identifier:** METPO:1000801
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which molecular oxygen serves as the terminal electron acceptor in the electron transport chain, generating ATP through oxidative phosphorylation with water as the final product.
- **Parent traits:** METPO:1000800
- **Synonyms:** Oxic respiration, Oxygen respiration
- **Existing evidence:** DOI:10.1146/annurev.biophys.27.1.329: terminal enzyme of respiratory chains (Review supports cytochrome c oxidase reducing molecular oxygen to water in aerobic respiratory chains.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports proton-gradient energy conservation by prokaryotic respiratory chains.)
- **Existing causal graph summary:** aerobic_respiration_terminal_oxidase: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **Aerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/aerobic_respiration.yaml`.

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
- **Trait label:** Aerobic respiration
- **METPO identifier:** METPO:1000801
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A respiration in which molecular oxygen serves as the terminal electron acceptor in the electron transport chain, generating ATP through oxidative phosphorylation with water as the final product.
- **Parent traits:** METPO:1000800
- **Synonyms:** Oxic respiration, Oxygen respiration
- **Existing evidence:** DOI:10.1146/annurev.biophys.27.1.329: terminal enzyme of respiratory chains (Review supports cytochrome c oxidase reducing molecular oxygen to water in aerobic respiratory chains.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports proton-gradient energy conservation by prokaryotic respiratory chains.)
- **Existing causal graph summary:** aerobic_respiration_terminal_oxidase: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **Aerobic respiration** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/aerobic_respiration.yaml`.

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


## Microbial Trait Causal Graph Research Report: Aerobic Respiration (METPO:1000801)

### Trait metadata
- **Trait:** Aerobic respiration
- **METPO:** METPO:1000801
- **Definition (given):** Respiration in which molecular oxygen is the terminal electron acceptor in the electron transport chain, generating ATP through oxidative phosphorylation with water as the final product.

---

## 1) Key concepts, definitions, and current understanding

### 1.1 What the trait represents (scope)
Aerobic respiration (METPO:1000801) should be curated as a **physiological capacity** to couple electron transfer through a membrane electron transport chain (ETC) to **molecular oxygen reduction to water**, while conserving energy as a **proton motive force (PMF)/membrane potential** used by ATP synthase (oxidative phosphorylation). In a bacterial description of aerobic respiration, terminal oxidases (Complex IV) “shuttle electrons from cytochrome c or quinol to O2, reducing it to water” and the overall pathway is framed as oxidative phosphorylation (OXPHOS) using PMF (giordano2024nitricoxideand pages 8-13).

A minimal defining biochemical statement is the terminal step: **“4e- + 4H+ + O2 → 2H2O”** (giordano2024nitricoxideand pages 8-13). This equation captures the trait boundary: **O2 is the terminal electron acceptor and is reduced to water**.

### 1.2 Distinguishing from nearby traits (boundary cases)
- **Aerobic respiration vs. aerobic growth:** Growth rate/yield under air is an *outcome* influenced by aerobic respiration, but not equivalent to the trait; strains can have aerobic respiration machinery while growth is limited by nutrients or stressors. Oxygen consumption assays and growth under specific conditions (e.g., CO exposure) are therefore **assay readouts**, not the trait itself (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 10-11).
- **Aerobic respiration vs. microaerophily (oxygen preference):** Oxygen preference reflects **regulation and terminal oxidase choice** rather than mere capacity. For example, cytochrome bd is described as “maximally expressed… under conditions of low oxygen supply” with expression peaking at “<2% oxygen tension” in E. coli, indicating oxygen-dependent regulation that can drive microaerobic specialization (borisov2021bacterialoxidasesof pages 6-7).
- **Aerobic respiration vs. oxygen tolerance/ROS defense:** Some respiratory oxidases (notably bd-type) also contribute to detoxification and stress tolerance, but ROS detoxification alone should not be conflated with the ability to perform O2-terminal respiration. Reviews explicitly describe bd oxidases as conferring resistance to multiple stresses in addition to respiration (borisov2021bacterialoxidasesof pages 1-2, giordano2024nitricoxideand pages 13-19).
- **Boundary case—“anaerobes” that encode bd oxidases:** Cytochrome bd occurs “surprisingly, in bacteria formally denoted as anaerobes,” implying that annotation of aerobic respiration based solely on taxonomy/lifestyle labels can be misleading; gene content and functional evidence matter (borisov2021bacterialoxidasesof pages 1-2).
- **Boundary case—cofactor-dependent respiration (LAB):** Lactic acid bacteria can operate a minimal respiratory chain (NDH-2 → menaquinone → cytochrome bd) but often require **exogenous heme** (and sometimes quinone) to enable respiration because many LAB “cannot synthesize heme… and thus rely on exogenous heme to enable respiration” (yamamoto2024rolesofflavoprotein pages 3-5).

### 1.3 Mechanistic definition of the “aerobic respiration” module
A useful mechanistic decomposition for curation is:
1) **Electron input** (e.g., NADH dehydrogenase, succinate dehydrogenase) to reduce quinones (giordano2024nitricoxideand pages 8-13, uriberamirez2024modificationsofthe pages 1-2).
2) **Mobile carrier pool(s):** quinone/quinol pool; in some systems cytochrome c (giordano2024nitricoxideand pages 8-13, giordano2024nitricoxideand pages 13-19).
3) **Terminal oxidases (Complex IV):** heme–copper oxidases (HCOs such as aa3/bo3/cbb3/ba3) and/or bd-type oxidases; these reduce O2 to H2O (giordano2024nitricoxideand pages 13-19, giordano2024nitricoxideanda pages 13-19).
4) **Energy conservation:** PMF generation by proton pumping (HCOs) or charge separation mechanisms (bd), then ATP synthase uses PMF to synthesize ATP (giordano2024nitricoxideand pages 8-13, giordano2024nitricoxideand pages 13-19).

---

## 2) Candidate causal graph entities (nodes), grouped by type

The following table lists candidate nodes for curating `data/traits/metabolism/aerobic_respiration.yaml`, with suggested ontology grounding where supported.

| Node label | Suggested ontology CURIE(s) | Node type | Evidence source(s) |
|---|---|---|---|
| Aerobic respiration | METPO:1000801; GO:0009060 | process | Giordano 2024, DOI unavailable/URL unavailable; Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (giordano2024nitricoxideand pages 8-13, yamamoto2024rolesofflavoprotein pages 3-5) |
| Electron transport chain | GO:0022900 | process | Giordano 2024, DOI unavailable/URL unavailable; Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (giordano2024nitricoxideand pages 8-13, henry2024drugrepurposingapproachesto pages 24-28) |
| Oxidative phosphorylation | GO:0006119 | process | Giordano 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13) |
| Proton motive force | GO:0015986 | process | Giordano 2024, DOI unavailable/URL unavailable; Walters 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 29-33) |
| ATP synthesis coupled proton transport / ATP synthase function | GO:0015986; EC:7.1.2.2 | process | Giordano 2024, DOI unavailable/URL unavailable; Walters 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 29-33) |
| NADH:quinone oxidoreductase (Complex I, NDH-1) | EC:7.1.1.2 | protein complex | Giordano 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13) |
| Type II NADH dehydrogenase (NDH-2) | EC:7.1.1.- | protein complex | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002; González-Montalvo 2024, https://doi.org/10.3389/fmicb.2024.1479714 (yamamoto2024rolesofflavoprotein pages 3-5, gonzalezmontalvo2024therespiratorychain pages 1-2) |
| Succinate dehydrogenase (Complex II) | EC:7.1.1.2; EC:1.3.5.1 | protein complex | Giordano 2024, DOI unavailable/URL unavailable; Uribe-Ramírez 2024, https://doi.org/10.1007/s10863-024-10041-y (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 8-13) |
| Cytochrome bc1 complex (Complex III) | EC:7.1.1.8 | protein complex | Giordano 2024, DOI unavailable/URL unavailable; Walters 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 21-25) |
| Cytochrome c | CHEBI:35227 | chemical | Giordano 2024, DOI unavailable/URL unavailable; Uribe-Ramírez 2024, https://doi.org/10.1007/s10863-024-10041-y (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 13-19) |
| Heme-copper oxygen reductase / terminal oxidase | GO:0015002 | protein complex | Giordano 2024, DOI unavailable/URL unavailable; Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (henry2024drugrepurposingapproachesto pages 28-31, giordano2024nitricoxideand pages 8-13) |
| Cytochrome bo3 quinol oxidase | EC:7.1.1.3 | protein complex | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (henry2024drugrepurposingapproachesto pages 28-31, khalfaouihassani2023theescherichiacoli pages 1-2) |
| Cytochrome aa3 oxidase | label-only candidate | protein complex | de Jong 2024, https://doi.org/10.3389/fmicb.2024.1468929; Giordano 2024, DOI unavailable/URL unavailable (jong2024quantitativeproteomicsreveals pages 1-2, giordano2024nitricoxideand pages 13-19) |
| Cytochrome ba3 oxidase | label-only candidate | protein complex | de Jong 2024, https://doi.org/10.3389/fmicb.2024.1468929; Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (jong2024quantitativeproteomicsreveals pages 1-2, khalfaouihassani2023theescherichiacoli pages 2-3) |
| cbb3-type cytochrome c oxidase | label-only candidate | protein complex | Giordano 2024, DOI unavailable/URL unavailable; Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (giordano2024nitricoxideand pages 13-19, khalfaouihassani2023theescherichiacoli pages 1-2) |
| Cytochrome bd oxidase | GO:0015003 | protein complex | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (henry2024drugrepurposingapproachesto pages 31-37, yamamoto2024rolesofflavoprotein pages 3-5) |
| Cyanide-insensitive oxidase (CIO) | label-only candidate | protein complex | Nastasi 2024, https://doi.org/10.3390/antiox13030383; Giordano 2024, DOI unavailable/URL unavailable (nastasi2024cyanideinsensitiveoxidase pages 1-2, giordano2024nitricoxideand pages 13-19) |
| ATP synthase (Complex V, FoF1 ATP synthase) | EC:7.1.2.2 | protein complex | Giordano 2024, DOI unavailable/URL unavailable; Walters 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 29-33) |
| cyoABCDE operon | label-only candidate | gene | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; Nastasi 2024, https://doi.org/10.3390/ijms25021277 (henry2024drugrepurposingapproachesto pages 28-31, nastasi2024membraneboundredoxenzyme pages 10-11) |
| cydA | label-only candidate | gene | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002; Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (yamamoto2024rolesofflavoprotein pages 3-5, henry2024drugrepurposingapproachesto pages 31-37) |
| cydB | label-only candidate | gene | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002; Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (yamamoto2024rolesofflavoprotein pages 3-5, henry2024drugrepurposingapproachesto pages 31-37) |
| cydX | label-only candidate | gene | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; Nastasi 2024, https://doi.org/10.3390/ijms25021277 (henry2024drugrepurposingapproachesto pages 28-31, nastasi2024membraneboundredoxenzyme pages 10-11) |
| cydH / ynhF | label-only candidate | gene | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (henry2024drugrepurposingapproachesto pages 28-31, henry2024drugrepurposingapproachesto pages 31-37) |
| appCB / appCBX | label-only candidate | gene | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (henry2024drugrepurposingapproachesto pages 31-37) |
| noxA | label-only candidate | gene | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5) |
| noxB | label-only candidate | gene | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5) |
| yhjE | label-only candidate | gene | Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (khalfaouihassani2023theescherichiacoli pages 1-2, khalfaouihassani2023theescherichiacoli pages 23-24) |
| ydiM | label-only candidate | gene | Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (khalfaouihassani2023theescherichiacoli pages 1-2, khalfaouihassani2023theescherichiacoli pages 23-24) |
| yfcJ | label-only candidate | gene | Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (khalfaouihassani2023theescherichiacoli pages 1-2, khalfaouihassani2023theescherichiacoli pages 23-24) |
| Molecular oxygen | CHEBI:15379 | chemical | Giordano 2024, DOI unavailable/URL unavailable; Walters 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 29-33) |
| Water | CHEBI:15377 | chemical | Giordano 2024, DOI unavailable/URL unavailable; Walters 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 29-33) |
| Quinone pool | label-only candidate | chemical | Giordano 2024, DOI unavailable/URL unavailable; Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (giordano2024nitricoxideand pages 8-13, henry2024drugrepurposingapproachesto pages 28-31) |
| Ubiquinone | CHEBI:16389 | chemical | Giordano 2024, DOI unavailable/URL unavailable; Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (giordano2024nitricoxideand pages 8-13, henry2024drugrepurposingapproachesto pages 28-31) |
| Ubiquinol | CHEBI:17976 | chemical | Giordano 2024, DOI unavailable/URL unavailable; Mele 2023, https://doi.org/10.1042/ebc20230012 (giordano2024nitricoxideand pages 13-19, mele2023oxidoreductasesandmetal pages 8-9) |
| Menaquinone | CHEBI:18009 | chemical | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5) |
| Heme | CHEBI:30413 | chemical | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002; Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015 (yamamoto2024rolesofflavoprotein pages 3-5, khalfaouihassani2023theescherichiacoli pages 1-2) |
| Heme d | label-only candidate | chemical | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244 (henry2024drugrepurposingapproachesto pages 28-31, henry2024drugrepurposingapproachesto pages 31-37) |
| Heme b558 | label-only candidate | chemical | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; Giordano 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideanda pages 13-19, henry2024drugrepurposingapproachesto pages 31-37) |
| Heme b595 | label-only candidate | chemical | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; Giordano 2024, DOI unavailable/URL unavailable (giordano2024nitricoxideanda pages 13-19, henry2024drugrepurposingapproachesto pages 31-37) |
| Copper | CHEBI:28694 | chemical | Khalfaoui-Hassani 2023, https://doi.org/10.1371/journal.pone.0293015; Giordano 2024, DOI unavailable/URL unavailable (khalfaouihassani2023theescherichiacoli pages 1-2, giordano2024nitricoxideand pages 8-13) |
| Carbon monoxide | CHEBI:17245 | chemical | Nastasi 2024, https://doi.org/10.3390/ijms25021277; Henry 2024, https://doi.org/10.1093/infdis/jiad540 (nastasi2024membraneboundredoxenzyme pages 4-7, henry2024steroiddrugsinhibit pages 1-3) |
| Nitric oxide | CHEBI:16480 | chemical | Nastasi 2024, https://doi.org/10.3390/antiox13030383; Giordano 2024, DOI unavailable/URL unavailable (nastasi2024cyanideinsensitiveoxidase pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 3-5) |
| Hydrogen sulfide | CHEBI:16136 | chemical | Nastasi 2024, https://doi.org/10.3390/antiox13030383; Giordano 2024, DOI unavailable/URL unavailable (nastasi2024cyanideinsensitiveoxidase pages 1-2, giordano2024nitricoxideand pages 65-69) |
| Cyanide | CHEBI:17514 | chemical | Nastasi 2024, https://doi.org/10.3390/antiox13030383; Uribe-Ramírez 2024, https://doi.org/10.1007/s10863-024-10041-y (nastasi2024cyanideinsensitiveoxidase pages 2-3, uriberamirez2024modificationsofthe pages 1-2) |
| High oxygen condition | label-only candidate | environmental factor | de Jong 2024, https://doi.org/10.3389/fmicb.2024.1468929; Nastasi 2024, https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7, jong2024quantitativeproteomicsreveals pages 1-2) |
| Low oxygen / microaerobic condition | ENVO:01000925 candidate | environmental factor | Borisov 2021, https://doi.org/10.1089/ars.2020.8039; de Jong 2024, https://doi.org/10.3389/fmicb.2024.1468929 (borisov2021bacterialoxidasesof pages 6-7, jong2024quantitativeproteomicsreveals pages 1-2) |
| Oxygen tension below 50% | label-only candidate | environmental factor | González-Montalvo 2024, https://doi.org/10.3389/fmicb.2024.1479714 (gonzalezmontalvo2024therespiratorychain pages 9-10) |
| Stationary phase | label-only candidate | environmental factor | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; González-Montalvo 2024, https://doi.org/10.3389/fmicb.2024.1479714 (henry2024drugrepurposingapproachesto pages 31-37, gonzalezmontalvo2024therespiratorychain pages 9-10) |
| Phosphate starvation | label-only candidate | environmental factor | Henry 2024 thesis, https://doi.org/10.22024/unikent/01.02.107244; González-Montalvo 2024, https://doi.org/10.3389/fmicb.2024.1479714 (henry2024drugrepurposingapproachesto pages 31-37, gonzalezmontalvo2024therespiratorychain pages 9-10) |
| Exogenous heme availability | label-only candidate | environmental factor | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5) |
| Exogenous quinone availability | label-only candidate | environmental factor | Yamamoto 2024, https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5) |
| Oxygen consumption rate | label-only candidate | assay readout | Nastasi 2024, https://doi.org/10.3390/ijms25021277; Nastasi 2024, https://doi.org/10.3390/antiox13030383 (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024cyanideinsensitiveoxidase pages 3-5) |
| Apparent IC50 for CO inhibition | label-only candidate | assay readout | Nastasi 2024, https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024membraneboundredoxenzyme pages 13-15) |
| Apparent IC50 for NO inhibition | label-only candidate | assay readout | Nastasi 2024, https://doi.org/10.3390/antiox13030383; Giordano 2024, DOI unavailable/URL unavailable (nastasi2024cyanideinsensitiveoxidase pages 3-5, giordano2024nitricoxideand pages 81-88) |
| Km(O2) | label-only candidate | assay readout | Nastasi 2024, https://doi.org/10.3390/ijms25021277; Nastasi 2024, https://doi.org/10.3390/antiox13030383 (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024cyanideinsensitiveoxidase pages 2-3) |
| Growth under urine-like conditions | label-only candidate | assay readout | González-Montalvo 2024, https://doi.org/10.3389/fmicb.2024.1479714 (gonzalezmontalvo2024therespiratorychain pages 7-9, gonzalezmontalvo2024therespiratorychain pages 1-2) |


*Table: This table lists candidate nodes for a TraitMech causal graph of microbial aerobic respiration, grouped across processes, complexes, genes, chemicals, environmental factors, and assay readouts. It is useful as a curation scaffold because each node is tied to source-backed evidence from the gathered literature.*

---

## 3) Evidence-backed candidate causal edges (triples)

The following table proposes evidence-backed subject–predicate–object edges suitable for a TraitMech causal graph. Each edge includes a supporting quote/snippet, DOI/URL where available, and notes on uncertainty/taxon-specificity.

| Subject node | Predicate | Object node | Evidence snippet | Source (DOI, year, URL) | Notes / uncertainty |
|---|---|---|---|---|---|
| NADH:quinone oxidoreductase / Complex I (EC:7.1.1.2; GO:0008137) | reduces | quinone pool / ubiquinone (CHEBI:16389) | “Complex I transfers electrons from NADH to quinone” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Core ETC edge; review/thesis-like source, not primary mechanistic assay |
| Quinone pool / ubiquinol (CHEBI:16389 / CHEBI:17976) | donates electrons to | cytochrome bc1 complex / Complex III (EC:7.1.1.8) | “Complex III... transfers electrons from the quinone pool to cytochrome c” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Well-established generic edge |
| Cytochrome bc1 complex / Complex III (EC:7.1.1.8) | reduces | cytochrome c (CHEBI:35227) | “Complex III... transfers electrons from the quinone pool to cytochrome c” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Generic bacterial ETC edge |
| Cytochrome c (CHEBI:35227) | donates electrons to | heme-copper terminal oxidases / Complex IV (GO:0015002) | “electrons are transferred from cytochrome c to the aa3, cbb3-1, and cbb3-2 oxidases” (giordano2024nitricoxideand pages 13-19) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Taxon example is Pseudomonas aeruginosa; generalizable to cytochrome-c oxidases |
| Quinol / ubiquinol (CHEBI:17976) | donates electrons to | bo3 quinol oxidase (EC:7.1.1.3) | “quinone transfers electrons to bo3 and CIO oxygen reductases” (giordano2024nitricoxideand pages 13-19) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Taxon example from P. aeruginosa |
| Quinol / ubiquinol (CHEBI:17976) | donates electrons to | cytochrome bd oxidase / CIO (GO:0015003) | “quinone transfers electrons to bo3 and CIO oxygen reductases” (giordano2024nitricoxideand pages 13-19) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Taxon example from P. aeruginosa |
| Terminal oxidase / Complex IV (GO:0015002) | reduces | molecular oxygen (CHEBI:15379) | “terminal oxidases (complex IV) that shuttle electrons from cytochrome c or quinol to O2, reducing it to water” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | High-confidence trait-defining edge |
| Molecular oxygen (CHEBI:15379) | is reduced to | water (CHEBI:15377) | “4e- + 4H+ + O2 → 2H2O” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Canonical reaction equation |
| Electron transport chain (GO:0022900) | generates | proton motive force (GO:0015986) | “Proton/sodium translocation during these redox reactions creates a proton motive force (PMF)” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Broad process-level edge |
| Proton motive force (GO:0015986) | powers | ATP synthase / Complex V (EC:7.1.2.2) | “PMF used by Complex V (ATP synthase) to synthesize ATP” (giordano2024nitricoxideand pages 8-13) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Broad OXPHOS edge |
| Cytochrome bd oxidase (GO:0015003) | generates | proton motive force (GO:0015986) | “can generate PMF through transmembrane charge separation” (giordano2024nitricoxideanda pages 13-19) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Important because bd does not pump protons canonically |
| Heme-copper oxidases (GO:0015002) | pump protons to generate | proton motive force (GO:0015986) | “A-HCOs have D and K proton channels... move both substrate and ‘pumped protons’ across the membrane” (giordano2024nitricoxideand pages 13-19) | 2024, Giordano et al., DOI unavailable in evidence, URL unavailable in evidence | Applies mainly to HCO family; mechanistic wording from review |
| Low oxygen tension / microaerobic condition (ENVO:01000925 candidate) | upregulates expression of | cytochrome bd oxidase genes cydAB (gene labels; E. coli) | “maximally expressed in E. coli under conditions of low oxygen supply” and expression peaks at “<2% oxygen tension” (borisov2021bacterialoxidasesof pages 6-7) | 2021, Borisov et al., DOI:10.1089/ars.2020.8039, https://doi.org/10.1089/ars.2020.8039 | Useful regulatory edge; species-specific to E. coli |
| Decreased oxygen availability (label-only environmental node) | shifts usage from | bo3 oxidase (cyoABCDE) to bd oxidase (cydABX) | “expression shifts from bo3 to bd with decreasing O2 during growth” (nastasi2024membraneboundredoxenzyme pages 4-7) | 2024, Nastasi et al., DOI:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277 | Regulatory edge inferred from transcript/physiology in E. coli |
| High oxygen level (4.2% O2) | increases abundance of | cytochrome aa3 oxidase (label-only; HCO family) | “Cyt. aa3 abundance was highest at the upper tested level (4.2% O2)” (jong2024quantitativeproteomicsreveals pages 1-2) | 2024, de Jong et al., DOI:10.3389/fmicb.2024.1468929, https://doi.org/10.3389/fmicb.2024.1468929 | Species-specific to Caldalkalibacillus thermarum |
| Lower oxygen level (~0.42–1.05% O2) | favors abundance of | cytochrome ba3 oxidase (label-only; HCO family) | “Cyt. ba3 was more abundant across most other O2 conditions but began to decline below ~0.42% O2” (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 4-6) | 2024, de Jong et al., DOI:10.3389/fmicb.2024.1468929, https://doi.org/10.3389/fmicb.2024.1468929 | Species-specific; not universal |
| Carbon monoxide (CHEBI:17245) | inhibits | bo3 terminal oxidase (EC:7.1.1.3) | “96.3 µM CO inhibited... bo3... by 44.3 ± 1.5%” at 100 µM O2 (nastasi2024membraneboundredoxenzyme pages 4-7) | 2024, Nastasi et al., DOI:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277 | Quantitative, E. coli membrane assay |
| Carbon monoxide (CHEBI:17245) | inhibits | bd-II oxidase (label-only; appCBX complex) | “96.3 µM CO inhibited... bd-II... by 43.3 ± 7.6%” at 100 µM O2 (nastasi2024membraneboundredoxenzyme pages 4-7) | 2024, Nastasi et al., DOI:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277 | Quantitative, E. coli membrane assay |
| Carbon monoxide (CHEBI:17245) | weakly inhibits | bd-I oxidase / CydABXH (gene labels) | “96.3 µM CO inhibited bd-I O2 consumption by 11.6 ± 1.1%” (nastasi2024membraneboundredoxenzyme pages 4-7) | 2024, Nastasi et al., DOI:10.3390/ijms25021277, https://doi.org/10.3390/ijms25021277 | Quantitative; indicates relative resistance rather than absence of inhibition |
| Nitric oxide (CHEBI:16480) | reversibly inhibits | cyanide-insensitive oxidase / CIO (cytochrome bd-type oxidase) | “CIO is reversibly inhibited by NO with full, fast recovery after NO exhaustion” (nastasi2024cyanideinsensitiveoxidase pages 1-2) | 2024, Nastasi et al., DOI:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383 | High-confidence but taxon-specific to P. aeruginosa |
| Hydrogen sulfide (CHEBI:16136) | does not inhibit / is tolerated by | cyanide-insensitive oxidase / CIO (cytochrome bd-type oxidase) | “O2 consumption by P. aeruginosa CIO is unaltered even in the presence of high H2S” (nastasi2024cyanideinsensitiveoxidase pages 1-2) | 2024, Nastasi et al., DOI:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383 | Negative-causal/tolerance edge; taxon-specific |
| Cyanide (CHEBI:17514) | inhibits | non-CIO terminal oxidases in P. aeruginosa | “1 mM cyanide ‘completely suppressed NADH-mediated O2 consumption in the ∆cio strain only’” (nastasi2024cyanideinsensitiveoxidase pages 3-5) | 2024, Nastasi et al., DOI:10.3390/antiox13030383, https://doi.org/10.3390/antiox13030383 | Inference: suppression in ∆cio implies cyanide-sensitive remaining oxidases; strain-specific |
| Cytochrome bd oxidase genes cydA/cydB (gene labels; E. coli/LAB) | enable | aerobic respiration trait (METPO:1000801) | “minimal respiratory chain composed of a type II NADH dehydrogenase (NDH-2), menaquinone... and cytochrome bd oxidase” (yamamoto2024rolesofflavoprotein pages 3-5) | 2024, Yamamoto, DOI:10.12938/bmfh.2024-002, https://doi.org/10.12938/bmfh.2024-002 | Strong for LAB with exogenous cofactors; not universal mechanism across all taxa |
| Exogenous heme (CHEBI:30413) | enables | cytochrome oxidase-dependent respiration in LAB | “LAB generally cannot synthesize heme... and thus rely on exogenous heme to enable respiration” (yamamoto2024rolesofflavoprotein pages 3-5) | 2024, Yamamoto, DOI:10.12938/bmfh.2024-002, https://doi.org/10.12938/bmfh.2024-002 | Important boundary case; taxon-specific |
| Exogenous quinone / menaquinone (CHEBI:18009 candidate) | enables | respiratory chain function in some LAB | “strains lacking both heme and quinone require exogenous heme and quinone” (yamamoto2024rolesofflavoprotein pages 3-5) | 2024, Yamamoto, DOI:10.12938/bmfh.2024-002, https://doi.org/10.12938/bmfh.2024-002 | Taxon-specific; phrased for certain LAB |
| Copper (CHEBI:28694) | is required for biogenesis of | bo3 quinol oxidase / heme-CuB center (EC:7.1.1.3) | “bo3-Qox... contains one Cu at CuB” and YdiM/YhjE affect Cu/Fe homeostasis required for active bo3-Qox (khalfaouihassani2023theescherichiacoli pages 1-2) | 2023, Khalfaoui-Hassani et al., DOI:10.1371/journal.pone.0293015, https://doi.org/10.1371/journal.pone.0293015 | Supported for bo3 biogenesis; mechanistic requirement not directly shown for all taxa |
| MFS transporter YdiM (gene label; E. coli) | promotes biogenesis of | active bo3 quinol oxidase (EC:7.1.1.3) | “yhjE, ydiM, and yfcJ are required to produce an active bo3 quinol oxidase” (khalfaouihassani2023theescherichiacoli pages 1-2) | 2023, Khalfaoui-Hassani et al., DOI:10.1371/journal.pone.0293015, https://doi.org/10.1371/journal.pone.0293015 | Gene-specific and E. coli-specific |
| MFS transporter YhjE (gene label; E. coli) | promotes biogenesis of | active bo3 quinol oxidase (EC:7.1.1.3) | “yhjE, ydiM, and yfcJ are required to produce an active bo3 quinol oxidase” (khalfaouihassani2023theescherichiacoli pages 1-2) | 2023, Khalfaoui-Hassani et al., DOI:10.1371/journal.pone.0293015, https://doi.org/10.1371/journal.pone.0293015 | Gene-specific and E. coli-specific |
| MFS transporter YfcJ (gene label; E. coli) | promotes biogenesis of | active bo3 quinol oxidase (EC:7.1.1.3) | “yhjE, ydiM, and yfcJ are required to produce an active bo3 quinol oxidase” (khalfaouihassani2023theescherichiacoli pages 1-2) | 2023, Khalfaoui-Hassani et al., DOI:10.1371/journal.pone.0293015, https://doi.org/10.1371/journal.pone.0293015 | Gene-specific and E. coli-specific |


*Table: This table compiles evidence-backed candidate causal edges for curating a TraitMech graph of microbial aerobic respiration, including ETC core steps, regulation by oxygen, inhibition/tolerance by gases, and oxidase cofactor/biogenesis dependencies.*

---

## 4) Recent developments (prioritizing 2023–2024)

### 4.1 Oxygen-dependent remodeling of terminal oxidases (controlled oxygen systems)
**Chemostat microaerobiosis (2024):** In *Caldalkalibacillus thermarum* chemostats spanning **0.25%–4.2% O2**, proteomics showed terminal oxidase abundance shifts: cytochrome **aa3** was highest at **4.2% O2**, while **ba3** dominated across most other O2 conditions but “started to decline below 0.42% O2,” and bb3/bd were not detected under the tested conditions (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 4-6). This supports curation of **environmental oxygen level → oxidase usage/abundance** edges.

### 4.2 Quantitative inhibitor biology of terminal oxidases (CO/NO/H2S/cyanide)
**CO resistance as an aerobic-respiration phenotype (2024):** In E. coli membrane/cell systems expressing single terminal oxidases, CO inhibition is oxidase-specific and oxygen-dependent. At **[O2] = 100 µM**, **96.3 µM CO** inhibited O2 consumption by **11.6 ± 1.1%** in bd-I-only cells versus **43.3 ± 7.6%** (bd-II) and **44.3 ± 1.5%** (bo3) (nastasi2024membraneboundredoxenzyme pages 4-7). This provides quantitative evidence for edges linking **CO → terminal oxidase inhibition → decreased aerobic respiration rate**.

**Cyanide/H2S/NO tolerance via CIO in Pseudomonas (2024):** P. aeruginosa’s bd-type **cyanide-insensitive oxidase (CIO)** is reported as H2S-tolerant (oxygen consumption “unaltered” even with high H2S) and NO-recovering (reversible inhibition with rapid/full recovery), supporting a protective role during infection contexts where H2S/NO are present (nastasi2024cyanideinsensitiveoxidase pages 1-2).

### 4.3 Respiration-targeting drug discovery in 2024
**Steroid drug inhibition of bacterial respiratory oxidases (2024):** A drug-repurposing screen found steroid inhibitors of cytochrome bd. Quinestrol inhibited E. coli bd-I with **IC50 = 0.5 ± 0.1 µM** and inhibited growth of an E. coli “bd-I only” strain with **IC50 = 0.2 ± 0.07 µM**; growth of an S. aureus “bd only” strain was inhibited with **IC50 = 6.0 ± 1.2 µM**, and quinestrol was bactericidal toward S. aureus (henry2024steroiddrugsinhibit pages 1-3). These data support application-oriented edges (inhibitor → oxidase inhibition → growth/viability phenotype).

**Anti-tubercular rationale (2024):** A 2024 medicinal chemistry review frames M. tuberculosis cytochrome bd as an “emerging anti-tubercular drug target,” emphasizing redundancy between terminal oxidases and the need for combination strategies; cytochrome bd’s prokaryote-specificity underpins selectivity claims, and the 2021 cryo-EM structure is described as accelerating inhibitor discovery (saha2024cytochromebdoxidase pages 3-5).

---

## 5) Current applications and real-world implementations

### 5.1 Clinical microbiology: infection-site metabolism and antibiotic target discovery
**Urine-like infection niche (2024):** *Klebsiella aerogenes* respiration was studied in urine-like media to identify drug targets. Bd-type oxidases were quantified as dominating respiration: “bd-oxidases carry out **76–81%** of the respiratory activity in K. aerogenes,” and NDH-2 was identified as the main entry point, with the explicit rationale that NDH-2 and bd oxidases are attractive targets because they are absent in humans (gonzalezmontalvo2024therespiratorychain pages 9-10, gonzalezmontalvo2024therespiratorychain pages 1-2).

**Cystic fibrosis and persistent infections (2024):** In P. aeruginosa, branched aerobic respiration and oxidase tolerance to host-derived gases (NO; H2S exposure) are framed as virulence-relevant, and bacteria-specific energy metabolism is argued to be a therapeutic target to help eliminate chronic/persister infections (nastasi2024cyanideinsensitiveoxidase pages 1-2).

### 5.2 Bioprocessing / oxygen-control implementations (laboratory-to-engineering bridge)
Continuous culture oxygen titrations (chemostats) provide an implementation pattern for engineering and mechanistic inference: oxygen control over 0.25–4.2% O2 was achieved by sparging defined air–N2 mixes, enabling causal attribution of oxygen to terminal oxidase abundance and regulation (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 4-6). Although these are laboratory-scale, the methods are directly transferable to industrial bioreactors for controlling respiratory state.

---

## 6) Expert opinions and authoritative analysis (why this trait matters)

### 6.1 Why cytochrome bd is repeatedly highlighted
A domain-leading review (Borisov et al.) positions cytochrome bd as a **high-affinity ubiquinol:oxygen oxidoreductase** whose “primary bioenergetic role” is reducing O2 to H2O “even at submicromolar O2… [with] generation of a proton motive force for ATP production,” and emphasizes its importance in pathogens and its uniquely bacterial nature as a drug target (borisov2021bacterialoxidasesof pages 1-2).

The same review explicitly flags key open questions: “Fundamental questions remain regarding the precise delineation of electron flow… and how the extraordinarily high affinity for oxygen is accomplished” (borisov2021bacterialoxidasesof pages 1-2). These uncertainties should temper overly specific mechanistic edges unless directly evidenced.

### 6.2 Tuberculosis and redundancy as a mechanistic “expert model”
The 2024 RSC Medicinal Chemistry review emphasizes that in M. tuberculosis, functional redundancy between terminal oxidases can render inhibition of one branch bacteriostatic, motivating combination regimens and supporting a causal-graph view in which **parallel oxidase nodes buffer aerobic respiration output** under stress (saha2024cytochromebdoxidase pages 3-5).

---

## 7) Curation warnings (what not to over-curate yet)

1) **Taxon specificity:** Many oxidase/regulation/inhibitor edges are species-specific (E. coli; P. aeruginosa; C. thermarum; K. aerogenes). They are valuable as **candidate generic edges** but should be flagged as taxon-conditional unless corroborated broadly (nastasi2024membraneboundredoxenzyme pages 4-7, nastasi2024cyanideinsensitiveoxidase pages 1-2, jong2024quantitativeproteomicsreveals pages 1-2, gonzalezmontalvo2024therespiratorychain pages 9-10).
2) **Assay readouts vs trait:** Oxygen consumption, IC50 values, and growth inhibition are assay outcomes; curate them as downstream phenotypes (e.g., “inhibits oxidase activity” → “decreases O2 consumption rate”), not as defining nodes of aerobic respiration itself (nastasi2024membraneboundredoxenzyme pages 4-7, henry2024steroiddrugsinhibit pages 1-3).
3) **Unpublished/unclear source status:** Some mechanistic summaries (Giordano 2024; Walters 2024) were retrieved with incomplete bibliographic metadata in this session. Use them primarily to guide node/edge hypotheses, and prefer DOI-tracked sources when formalizing key edges (giordano2024nitricoxideand pages 8-13, walters2024spectroscopicinvestigationsof pages 29-33).
4) **Negative edges (“unaltered by H2S”):** Tolerance claims can be context-dependent (concentration, redox state, membrane prep). Curate as conditional (e.g., “CIO confers tolerance to H2S”) with explicit conditions where available (nastasi2024cyanideinsensitiveoxidase pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 3-5).

---

## DOI-first bibliography (with dates and URLs where available)

1. **Henry SA et al.** Steroid Drugs Inhibit Bacterial Respiratory Oxidases and Are Lethal Toward Methicillin-Resistant *Staphylococcus aureus*. *Journal of Infectious Diseases*. **Feb 2024**. DOI: **10.1093/infdis/jiad540**. URL: https://doi.org/10.1093/infdis/jiad540 (henry2024steroiddrugsinhibit pages 1-3)
2. **Nastasi MR et al.** Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant *Escherichia coli* Growth and Respiration. *International Journal of Molecular Sciences*. **Jan 2024**. DOI: **10.3390/ijms25021277**. URL: https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 4-7)
3. **Nastasi MR et al.** Cyanide Insensitive Oxidase Confers Hydrogen Sulfide and Nitric Oxide Tolerance to *Pseudomonas aeruginosa* Aerobic Respiration. *Antioxidants*. **Mar 2024**. DOI: **10.3390/antiox13030383**. URL: https://doi.org/10.3390/antiox13030383 (nastasi2024cyanideinsensitiveoxidase pages 1-2)
4. **de Jong SI et al.** Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures. *Frontiers in Microbiology*. **Oct 2024**. DOI: **10.3389/fmicb.2024.1468929**. URL: https://doi.org/10.3389/fmicb.2024.1468929 (jong2024quantitativeproteomicsreveals pages 1-2)
5. **González-Montalvo MA et al.** The respiratory chain of *Klebsiella aerogenes* in urine-like conditions: critical roles of NDH-2 and bd-terminal oxidases. *Frontiers in Microbiology*. **Nov 2024**. DOI: **10.3389/fmicb.2024.1479714**. URL: https://doi.org/10.3389/fmicb.2024.1479714 (gonzalezmontalvo2024therespiratorychain pages 1-2)
6. **Khalfaoui-Hassani B et al.** The *Escherichia coli* MFS-type transporter genes yhjE, ydiM, and yfcJ are required to produce an active bo3 quinol oxidase. *PLOS ONE*. **Oct 2023**. DOI: **10.1371/journal.pone.0293015**. URL: https://doi.org/10.1371/journal.pone.0293015 (khalfaouihassani2023theescherichiacoli pages 1-2)
7. **Yamamoto Y.** Roles of flavoprotein oxidase and the exogenous heme- and quinone-dependent respiratory chain in lactic acid bacteria. *Bioscience of Microbiota, Food and Health*. **May 2024**. DOI: **10.12938/bmfh.2024-002**. URL: https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5)
8. **Saha P et al.** Cytochrome bd oxidase: an emerging anti-tubercular drug target. *RSC Medicinal Chemistry*. **Mar 2024**. DOI: **10.1039/d3md00587a**. URL: https://doi.org/10.1039/d3md00587a (saha2024cytochromebdoxidase pages 3-5)
9. **Borisov VB et al.** Bacterial Oxidases of the Cytochrome bd Family: Redox Enzymes of Unique Structure, Function, and Utility As Drug Targets. *Antioxidants & Redox Signaling*. **Jun 2021**. DOI: **10.1089/ars.2020.8039**. URL: https://doi.org/10.1089/ars.2020.8039 (borisov2021bacterialoxidasesof pages 1-2)
10. **Uribe-Ramírez D et al.** Modifications of the respiratory chain of *Bacillus licheniformis* as an alkalophilic and cyanide-degrading microorganism. *Journal of Bioenergetics and Biomembranes*. **Nov 2024**. DOI: **10.1007/s10863-024-10041-y**. URL: https://doi.org/10.1007/s10863-024-10041-y (uriberamirez2024modificationsofthe pages 1-2)
11. **Henry SA.** Drug-repurposing approaches to target bacterial respiratory complexes. University of Kent (thesis/text). **Jan 2024**. DOI: **10.22024/unikent/01.02.107244**. URL: https://doi.org/10.22024/unikent/01.02.107244 (henry2024drugrepurposingapproachesto pages 24-28)

(Additional sources were retrieved with incomplete bibliographic metadata during this session and are therefore cited in-text but not fully enumerated here.)

References

1. (giordano2024nitricoxideand pages 8-13): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

2. (nastasi2024membraneboundredoxenzyme pages 4-7): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

3. (nastasi2024membraneboundredoxenzyme pages 10-11): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

4. (borisov2021bacterialoxidasesof pages 6-7): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 142 citations and is from a domain leading peer-reviewed journal.

5. (borisov2021bacterialoxidasesof pages 1-2): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 142 citations and is from a domain leading peer-reviewed journal.

6. (giordano2024nitricoxideand pages 13-19): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

7. (yamamoto2024rolesofflavoprotein pages 3-5): Yuji Yamamoto. Roles of flavoprotein oxidase and the exogenous heme- and quinone-dependent respiratory chain in lactic acid bacteria. Bioscience of Microbiota, Food and Health, 43:183-191, May 2024. URL: https://doi.org/10.12938/bmfh.2024-002, doi:10.12938/bmfh.2024-002. This article has 3 citations.

8. (uriberamirez2024modificationsofthe pages 1-2): Daniel Uribe-Ramírez, Lucero Romero-Aguilar, Héctor Vázquez-Meza, Eliseo Cristiani-Urbina, and Juan Pablo Pardo. Modifications of the respiratory chain of bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. Journal of Bioenergetics and Biomembranes, 56:591-605, Nov 2024. URL: https://doi.org/10.1007/s10863-024-10041-y, doi:10.1007/s10863-024-10041-y. This article has 1 citations and is from a peer-reviewed journal.

9. (giordano2024nitricoxideanda pages 13-19): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

10. (henry2024drugrepurposingapproachesto pages 24-28): Samantha Amoy Henry. Drug-repurposing approaches to target bacterial respiratory complexes. Text, Jan 2024. URL: https://doi.org/10.22024/unikent/01.02.107244, doi:10.22024/unikent/01.02.107244. This article has 0 citations and is from a peer-reviewed journal.

11. (walters2024spectroscopicinvestigationsof pages 29-33): R Walters. Spectroscopic investigations of mycobacterial cytochromes. Unknown journal, 2024.

12. (gonzalezmontalvo2024therespiratorychain pages 1-2): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

13. (walters2024spectroscopicinvestigationsof pages 21-25): R Walters. Spectroscopic investigations of mycobacterial cytochromes. Unknown journal, 2024.

14. (henry2024drugrepurposingapproachesto pages 28-31): Samantha Amoy Henry. Drug-repurposing approaches to target bacterial respiratory complexes. Text, Jan 2024. URL: https://doi.org/10.22024/unikent/01.02.107244, doi:10.22024/unikent/01.02.107244. This article has 0 citations and is from a peer-reviewed journal.

15. (khalfaouihassani2023theescherichiacoli pages 1-2): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 7 citations and is from a peer-reviewed journal.

16. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

17. (khalfaouihassani2023theescherichiacoli pages 2-3): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 7 citations and is from a peer-reviewed journal.

18. (henry2024drugrepurposingapproachesto pages 31-37): Samantha Amoy Henry. Drug-repurposing approaches to target bacterial respiratory complexes. Text, Jan 2024. URL: https://doi.org/10.22024/unikent/01.02.107244, doi:10.22024/unikent/01.02.107244. This article has 0 citations and is from a peer-reviewed journal.

19. (nastasi2024cyanideinsensitiveoxidase pages 1-2): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

20. (khalfaouihassani2023theescherichiacoli pages 23-24): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 7 citations and is from a peer-reviewed journal.

21. (mele2023oxidoreductasesandmetal pages 8-9): Bruno Hay Mele, Maria Monticelli, Serena Leone, Deborah Bastoni, Bernardo Barosa, Martina Cascone, Flavia Migliaccio, Francesco Montemagno, Annarita Ricciardelli, Luca Tonietti, Alessandra Rotundi, Angelina Cordone, and Donato Giovannelli. Oxidoreductases and metal cofactors in the functioning of the earth. Essays in Biochemistry, 67:653-670, Aug 2023. URL: https://doi.org/10.1042/ebc20230012, doi:10.1042/ebc20230012. This article has 55 citations and is from a peer-reviewed journal.

22. (henry2024steroiddrugsinhibit pages 1-3): Samantha A. Henry, Calum M. Webster, L. Shaw, Nathanial J Torres, Mary-Elizabeth Jobson, Brendan C. Totzke, Jessica K. Jackson, Jake E. McGreig, Mark N. Wass, Gary K. Robinson, and Mark Shepherd. Steroid drugs inhibit bacterial respiratory oxidases and are lethal toward methicillin-resistant staphylococcus aureus. The Journal of Infectious Diseases, 230:e149-e158, Feb 2024. URL: https://doi.org/10.1093/infdis/jiad540, doi:10.1093/infdis/jiad540. This article has 13 citations.

23. (nastasi2024cyanideinsensitiveoxidase pages 3-5): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

24. (giordano2024nitricoxideand pages 65-69): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

25. (nastasi2024cyanideinsensitiveoxidase pages 2-3): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

26. (gonzalezmontalvo2024therespiratorychain pages 9-10): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

27. (nastasi2024membraneboundredoxenzyme pages 13-15): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 13 citations.

28. (giordano2024nitricoxideand pages 81-88): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

29. (gonzalezmontalvo2024therespiratorychain pages 7-9): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

30. (jong2024quantitativeproteomicsreveals pages 4-6): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

31. (saha2024cytochromebdoxidase pages 3-5): Pallavi Saha, Samarpita Das, Harish K. Indurthi, Rohit Kumar, Arnab Roy, Nitin Pal Kalia, and Deepak K. Sharma. Cytochrome bd oxidase: an emerging anti-tubercular drug target. RSC medicinal chemistry, 15 3:769-787, Mar 2024. URL: https://doi.org/10.1039/d3md00587a, doi:10.1039/d3md00587a. This article has 23 citations and is from a peer-reviewed journal.