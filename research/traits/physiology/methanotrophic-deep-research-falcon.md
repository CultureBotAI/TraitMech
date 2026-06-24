---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:44:21.636189'
end_time: '2026-06-18T11:54:52.500626'
duration_seconds: 630.86
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: methanotrophic
  trait_identifier: METPO:1000650
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: methanotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses methane as the primary carbon
    and energy source through oxidation of methane to carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: methanotroph
  evidence_summary: 'DOI:10.1039/D3CY00737E: convert methane to methanol using methane
    monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy
    step.)'
  causal_graph_summary: 'methanotrophic_methane_oxidation: 10 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methanotrophic
- **METPO identifier:** METPO:1000650
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** methanotroph
- **Existing evidence:** DOI:10.1039/D3CY00737E: convert methane to methanol using methane monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy step.)
- **Existing causal graph summary:** methanotrophic_methane_oxidation: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **methanotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methanotrophic.yaml`.

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
- **Trait label:** methanotrophic
- **METPO identifier:** METPO:1000650
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** methanotroph
- **Existing evidence:** DOI:10.1039/D3CY00737E: convert methane to methanol using methane monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy step.)
- **Existing causal graph summary:** methanotrophic_methane_oxidation: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **methanotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methanotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **methanotrophic** (METPO:1000650)

### Scope summary (trait meaning, boundaries, and current understanding)
The trait **methanotrophic** denotes the physiological capacity to use **methane (CH4) as the primary carbon and energy source**, initiated by enzymatic oxidation of methane to methanol. The defining mechanistic commitment is the presence of a methane-activating system—classically methane monooxygenase (MMO) in bacteria—such that methane is the growth substrate rather than a co-metabolized compound. (sakai2023methanemonooxygenases;physiology pages 1-2, tucci2024directmethaneoxidation pages 1-3)

**Boundary case 1: methanotrophy vs methylotrophy.** Methanotrophs are considered a **subgroup of methylotrophs**: methylotrophs can grow on reduced one-carbon compounds like methanol, whereas methanotrophs can use methane (and then typically also methanol downstream) (ahmadi2024recentfindingsin pages 1-2). This boundary is important for curation because many downstream nodes (methanol dehydrogenases, formaldehyde assimilation) are shared across methylotrophs and do not uniquely define the methanotrophic trait. (ahmadi2024recentfindingsin pages 9-11, sakai2023methanemonooxygenases;physiology pages 2-3)

**Boundary case 2: aerobic vs intra-aerobic vs anaerobic methane oxidation.** The canonical trait maps to **aerobic bacterial methanotrophy**, in which the first step (methane → methanol) requires O2 and is catalyzed by methane monooxygenase (MMO). (tucci2024directmethaneoxidation pages 1-3, tucci2024directmethaneoxidation pages 3-5)

However, recent and authoritative sources emphasize that “methanotrophy” in nature spans additional physiological regimes:
- **Intra-aerobic (nitrite-dependent) methane oxidation (NC10 bacteria, e.g., *Candidatus Methylomirabilis*)**: nitrite is reduced to NO, and **NO dismutation generates O2 internally**, enabling an O2-dependent MMO (notably pMMO) to activate methane even under externally anoxic conditions. (wissink2024probingdenitrifyinganaerobic pages 1-2, sina2024persistentactivityof pages 1-2)
- **Anaerobic archaeal methane oxidation (e.g., *Candidatus Methanoperedens*/ANME)**: methane activation proceeds via **reverse methanogenesis**, relying on methyl-coenzyme M reductase (MCR), coupled to alternative electron acceptors (e.g., nitrate, sulfate, metals). (wissink2024probingdenitrifyinganaerobic pages 1-2, tucci2024directmethaneoxidation pages 1-3)

**Curation guidance:** METPO:1000650’s definition (“uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide”) is broad enough to include aerobic and anaerobic methanotrophy, but many mechanistic nodes/edges are clade-specific (MMO vs MCR). For TraitMech, it is advisable to represent this as (i) a **core shared functional module** (methane oxidation for growth) plus (ii) **alternative implementation modules** (MMO-based vs reverse-methanogenesis-based) and (iii) explicit **electron acceptor context**. (wissink2024probingdenitrifyinganaerobic pages 1-2, tucci2024directmethaneoxidation pages 1-3)

---

## Key mechanistic entities (candidate nodes) with ontology grounding
The following node inventory is curation-oriented and grounded where possible.

| Node label | Group | Suggested grounding / CURIE | Notes | Key support |
|---|---|---|---|---|
| particulate methane monooxygenase (pMMO) | enzyme/protein/complex | EC:1.14.18.3 | Membrane-bound, copper-dependent methane monooxygenase catalyzing methane to methanol | (sakai2023methanemonooxygenases;physiology pages 2-3, sakai2023methanemonooxygenases;physiology pages 1-2) |
| PmoA | enzyme/protein/complex |  | pMMO subunit A; encoded in pmoCAB operon | (sakai2023methanemonooxygenases;physiology pages 3-4, sakai2023methanemonooxygenases;physiology pages 5-6) |
| PmoB | enzyme/protein/complex |  | pMMO subunit B; copper-containing subunit implicated in metal centers | (sakai2023methanemonooxygenases;physiology pages 2-3, sakai2023methanemonooxygenases;physiology pages 5-6) |
| PmoC | enzyme/protein/complex |  | pMMO subunit C; membrane subunit with proposed metal site | (sakai2023methanemonooxygenases;physiology pages 3-4, sakai2023methanemonooxygenases;physiology pages 5-6) |
| soluble methane monooxygenase hydroxylase alpha subunit (MmoX) | enzyme/protein/complex |  | sMMO hydroxylase α subunit; binuclear iron active center in hydroxylase complex | (sakai2023methanemonooxygenases;physiology pages 3-4, samanta2024geneticalandbiochemical pages 1-2) |
| soluble methane monooxygenase hydroxylase beta subunit (MmoY) | enzyme/protein/complex |  | sMMO hydroxylase β subunit | (sakai2023methanemonooxygenases;physiology pages 3-4, samanta2024geneticalandbiochemical pages 1-2) |
| soluble methane monooxygenase hydroxylase gamma subunit (MmoZ) | enzyme/protein/complex |  | sMMO hydroxylase γ subunit | (sakai2023methanemonooxygenases;physiology pages 3-4, samanta2024geneticalandbiochemical pages 1-2) |
| soluble methane monooxygenase regulatory protein B (MmoB) | enzyme/protein/complex |  | Regulatory component of sMMO controlling electron transfer/reactivity | (sakai2023methanemonooxygenases;physiology pages 3-4, sakai2023methanemonooxygenases;physiology pages 2-3) |
| soluble methane monooxygenase reductase (MmoC / MMOR) | enzyme/protein/complex |  | NADH-dependent reductase with FAD and 2Fe-2S cluster supplying electrons to sMMO | (sakai2023methanemonooxygenases;physiology pages 3-4, sakai2023methanemonooxygenases;physiology pages 2-3) |
| methanol dehydrogenase MxaFI | enzyme/protein/complex | EC:1.1.2.7 | PQQ-dependent methanol dehydrogenase oxidizing methanol to formaldehyde | (sakai2023methanemonooxygenases;physiology pages 2-3, ahmadi2024recentfindingsin pages 9-11) |
| methanol dehydrogenase XoxF | enzyme/protein/complex | EC:1.1.2.10 | Lanthanide-dependent/PQQ-associated methanol dehydrogenase | (sakai2023methanemonooxygenases;physiology pages 2-3) |
| methyl-coenzyme M reductase (MCR) | enzyme/protein/complex | EC:2.8.4.1 | Methane-activating enzyme in reverse methanogenesis of anaerobic archaeal methanotrophs | (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| periplasmic nitrate reductase (NapAB) | enzyme/protein/complex | EC:1.7.99.4 | Nitrate reductase expressed in Methylomirabilis-associated complete denitrification | (yao2024methanedependentcompletedenitrification pages 1-3, yao2024methanedependentcompletedenitrification pages 8-9) |
| membrane nitrate reductase (Nar) | enzyme/protein/complex | EC:1.7.5.1 | Alternative nitrate reductase type discussed in denitrifying methanotrophy | (yao2024methanedependentcompletedenitrification pages 1-3) |
| methanobactin | enzyme/protein/complex |  | Copper-binding chalkophore/peptide for Cu acquisition and copper-switch physiology | (tucci2024directmethaneoxidation pages 3-5, samanta2024geneticalandbiochemical pages 1-2) |
| nitric oxide dismutation | enzyme/protein/complex | GO:0019377 | Intra-aerobic process producing O2 and N2 from NO in nitrite-dependent methanotrophy | (wissink2024probingdenitrifyinganaerobic pages 1-2, sina2024persistentactivityof pages 1-2) |
| methane oxidation to methanol | pathway/module | GO:0015948 | First committed step of aerobic methanotrophy via MMO | (tucci2024directmethaneoxidation pages 3-5, sakai2023methanemonooxygenases;physiology pages 1-2) |
| methanol oxidation to formaldehyde | pathway/module | GO:0015949 | MDH-mediated downstream step after methane oxidation | (sakai2023methanemonooxygenases;physiology pages 2-3, ahmadi2024recentfindingsin pages 9-11) |
| ribulose monophosphate (RuMP) pathway | pathway/module |  | Formaldehyde assimilation pathway in many gammaproteobacterial methanotrophs | (tucci2024directmethaneoxidation pages 3-5) |
| serine pathway | pathway/module |  | Formaldehyde assimilation pathway in many alphaproteobacterial methanotrophs | (tucci2024directmethaneoxidation pages 3-5, ahmadi2024recentfindingsin pages 7-9) |
| reverse methanogenesis | pathway/module |  | Anaerobic methane oxidation route in ANME / Methanoperedens lineages | (tucci2024directmethaneoxidation pages 1-3, wissink2024probingdenitrifyinganaerobic pages 1-2) |
| denitrification | pathway/module | GO:0019646 | Nitrate/nitrite reduction coupled to methane oxidation in N-DAMO systems | (yao2024methanedependentcompletedenitrification pages 8-9, molinamacias2024implementationofan pages 1-2) |
| methane | chemical/metabolite | CHEBI:16183 | Primary carbon and energy source defining trait | (sakai2023methanemonooxygenases;physiology pages 1-2) |
| oxygen | chemical/metabolite | CHEBI:15379 | Required for aerobic MMO catalysis; can be generated intracellularly in Methylomirabilis | (tucci2024directmethaneoxidation pages 1-3, wissink2024probingdenitrifyinganaerobic pages 1-2) |
| methanol | chemical/metabolite | CHEBI:17790 | Product of MMO and substrate for MDH | (sakai2023methanemonooxygenases;physiology pages 2-3, sakai2023methanemonooxygenases;physiology pages 1-2) |
| formaldehyde | chemical/metabolite | CHEBI:16842 | Central intermediate in methanotroph catabolism/anabolism | (ahmadi2024recentfindingsin pages 9-11, ahmadi2024recentfindingsin pages 1-2) |
| formate | chemical/metabolite | CHEBI:15740 | Downstream oxidation product of formaldehyde | (ahmadi2024recentfindingsin pages 9-11) |
| carbon dioxide | chemical/metabolite | CHEBI:16526 | End product of complete methane oxidation / reverse methanogenesis | (wissink2024probingdenitrifyinganaerobic pages 1-2) |
| nitrate | chemical/metabolite | CHEBI:17632 | Electron acceptor in nitrate-dependent methane oxidation | (wissink2024probingdenitrifyinganaerobic pages 1-2, molinamacias2024implementationofan pages 1-2) |
| nitrite | chemical/metabolite | CHEBI:16301 | Electron acceptor and precursor to NO in nitrite-dependent methanotrophy | (wissink2024probingdenitrifyinganaerobic pages 1-2, sina2024persistentactivityof pages 1-2) |
| nitric oxide | chemical/metabolite | CHEBI:16480 | Intermediate disproportionated to O2 and N2 in Methylomirabilis | (wissink2024probingdenitrifyinganaerobic pages 1-2, sina2024persistentactivityof pages 1-2) |
| dinitrogen | chemical/metabolite | CHEBI:17997 | Product of denitrification / NO dismutation | (wissink2024probingdenitrifyinganaerobic pages 1-2, yao2024methanedependentcompletedenitrification pages 8-9) |
| copper | chemical/metabolite | CHEBI:28694 | Central cofactor regulating pMMO activity and copper switch | (tucci2024directmethaneoxidation pages 3-5, samanta2024geneticalandbiochemical pages 1-2) |
| iron | chemical/metabolite | CHEBI:18248 | Metal center of sMMO and relevant alternative electron acceptor context as ferric iron | (sakai2023methanemonooxygenases;physiology pages 3-4, sina2024persistentactivityof pages 1-2) |
| pyrroloquinoline quinone (PQQ) | chemical/metabolite | CHEBI:26490 | Cofactor of MxaFI/XoxF methanol dehydrogenases | (sakai2023methanemonooxygenases;physiology pages 2-3) |
| NADH | chemical/metabolite | CHEBI:16908 | Electron donor to sMMO reductase and some formaldehyde/formate oxidation steps | (sakai2023methanemonooxygenases;physiology pages 3-4, ahmadi2024recentfindingsin pages 9-11) |
| copper availability | environmental factor |  | Major regulator of sMMO/pMMO expression and methanobactin response | (samanta2024geneticalandbiochemical pages 16-17, samanta2024geneticalandbiochemical pages 1-2) |
| oxygen availability | environmental factor |  | Distinguishes aerobic methanotrophy from anoxic/intra-aerobic variants | (tucci2024directmethaneoxidation pages 1-3, sina2024persistentactivityof pages 1-2) |
| methane concentration | environmental factor |  | Controls kinetics from atmospheric ppm to elevated µM/ppm growth conditions | (lidstrom2024directmethaneremoval pages 2-4) |
| acidic pH / acidophily | environmental factor | ENVO:3100031 | Acidophilic methanotroph niche boundary/environmental preference | (ahmadi2024recentfindingsin pages 1-2) |
| sulfate | environmental factor | CHEBI:16189 | Alternative electron acceptor in anaerobic methane oxidation | (tucci2024directmethaneoxidation pages 1-3, wissink2024probingdenitrifyinganaerobic pages 1-2) |
| ferric iron | environmental factor | CHEBI:29033 | Alternative electron acceptor stimulating AOM in some peat systems | (sina2024persistentactivityof pages 1-2) |
| methane oxidation rate | phenotype/assay |  | Quantitative assay phenotype; reported in µM d−1, µg g−1 h−1, etc. | (sina2024persistentactivityof pages 1-2, lidstrom2024directmethaneremoval pages 2-4) |
| methane removal efficiency | phenotype/assay |  | Engineering performance phenotype; e.g., biofilters and UFBR systems | (molinamacias2024implementationofan pages 1-2, lidstrom2024directmethaneremoval pages 2-4) |
| copper switch | phenotype/assay |  | Cu-responsive switch between sMMO and pMMO expression/activity | (sakai2023methanemonooxygenases;physiology pages 3-4, samanta2024geneticalandbiochemical pages 1-2) |


*Table: This table lists candidate TraitMech causal-graph nodes for the methanotrophic trait, grouped by entity type and annotated with suggested CURIEs and supporting evidence IDs. It is useful as a starting inventory for curation into a mechanistic trait graph.*

**Notes on grounding and near-neighbor traits**
- MMO enzymes are shared with nearby monooxygenases capable of methane oxidation (e.g., ammonia monooxygenase, butane monooxygenase), creating potential false positives if only generic “monooxygenase” evidence is used. Curate using **pmoCAB**/**mmoXYZ** and/or methanotroph-specific physiological evidence. (sakai2023methanemonooxygenases;physiology pages 1-2)
- Several nodes (MDH, formaldehyde assimilation) are common to methylotrophs broadly; they support methanotrophy mechanistically but are not alone diagnostic of methane utilization. (ahmadi2024recentfindingsin pages 9-11, ahmadi2024recentfindingsin pages 1-2)

---

## Candidate causal edges (evidence-backed triples)
The table below is structured for direct conversion into a TraitMech/TraitGraph YAML edge list. Each edge is supported by a DOI-first reference and an evidence snippet.

| Subject | Predicate | Object | Evidence snippet (verbatim/near-verbatim) | Reference (DOI + URL + pub month/year) | Citation ID | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| methane + O2 | converted_to_via | methanol via methane monooxygenase (MMO) | “methanotrophs converting methane to methanol as the first metabolic step” and MMO enzymes “react with methane and dioxygen to form methanol and water” | 10.1021/acs.chemrev.3c00727 · https://doi.org/10.1021/acs.chemrev.3c00727 · Feb 2024 | (tucci2024directmethaneoxidation pages 1-3) | Core defining edge for aerobic methanotrophy; strong review support. |
| copper availability | positively_regulates_expression_of | pMMO | “high copper favors pMMO and represses sMMO” | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 3-4) | Canonical “copper switch”; curate as regulatory edge. |
| copper availability | negatively_regulates_expression_of | sMMO | “high copper favors pMMO and represses sMMO; low copper/biomass favors sMMO” | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 3-4) | Canonical “copper switch”; curate as regulatory edge. |
| pmoCAB operon | encodes | PmoA/PmoB/PmoC | “pMMO is a membrane-bound, copper-containing particulate methane monooxygenase… composed of subunits PmoA, PmoB, and PmoC, encoded by the pmoCAB operon” | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 2-3) | Strong gene-to-protein grounding for pMMO complex. |
| mmoXYZ genes | encodes | MmoX/MmoY/MmoZ (MMOH α/β/γ) | “MMOH is a dimer of heterotrimers encoded by the mmoXYZ genes” and “mmoX/mmoY/mmoZ give the α (60 kDa), β (45 kDa) and γ (19 kDa) subunits” | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 2-3, sakai2023methanemonooxygenases;physiology pages 3-4) | Strong encoding edge for soluble MMO hydroxylase. |
| methanol | oxidized_to_via | formaldehyde via methanol dehydrogenase (MDH) | “Methanol is then oxidized to formaldehyde by methanol dehydrogenase (MDH)” | 10.1021/acs.chemrev.3c00727 · https://doi.org/10.1021/acs.chemrev.3c00727 · Feb 2024 | (tucci2024directmethaneoxidation pages 3-5) | Core downstream step after methane oxidation. |
| MxaFI | catalyzes | methanol oxidation to formaldehyde | “methanol is oxidized to formaldehyde by PQQ-dependent MDHs (MxaFI) and the lanthanide-dependent MDH XoxF” | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 2-3) | Specific MDH isozyme edge. |
| XoxF | catalyzes | methanol oxidation to formaldehyde | “methanol is oxidized to formaldehyde by PQQ-dependent MDHs (MxaFI) and the lanthanide-dependent MDH XoxF” | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 2-3) | Specific MDH isozyme edge. |
| formaldehyde assimilation | proceeds_via | ribulose monophosphate (RuMP) pathway | “carbon assimilation follows either the ‘ribulose monophosphate pathway’ (Gammaproteobacteria)” | 10.1021/acs.chemrev.3c00727 · https://doi.org/10.1021/acs.chemrev.3c00727 · Feb 2024 | (tucci2024directmethaneoxidation pages 3-5) | Taxon-dependent assimilation route; annotate as common in gammaproteobacterial methanotrophs. |
| formaldehyde assimilation | proceeds_via | serine pathway | “or the ‘serine pathway’ (Alphaproteobacteria)” | 10.1021/acs.chemrev.3c00727 · https://doi.org/10.1021/acs.chemrev.3c00727 · Feb 2024 | (tucci2024directmethaneoxidation pages 3-5) | Taxon-dependent assimilation route; annotate as common in alphaproteobacterial methanotrophs. |
| methanobactin | binds | Cu(I) | “Mbns are ribosomally synthesized…that bind Cu(I) with particularly high affinity” | 10.1021/acs.chemrev.3c00727 · https://doi.org/10.1021/acs.chemrev.3c00727 · Feb 2024 | (tucci2024directmethaneoxidation pages 3-5) | Strong biochemical edge; useful for copper-acquisition mechanism. |
| methanobactin | enables | copper acquisition | “some methanotrophs produce methanobactin (high affinity for Cu(I))” for copper collection | 10.1039/d3cy00737e · https://doi.org/10.1039/d3cy00737e · Jan 2023 | (sakai2023methanemonooxygenases;physiology pages 2-3) | Supports Cu uptake role; mechanism broad but not always fully resolved. |
| copper acquisition | promotes | pMMO-dependent physiology | “As a required cofactor for pMMO activity … copper is central to methanotroph physiology” | 10.1021/acs.chemrev.3c00727 · https://doi.org/10.1021/acs.chemrev.3c00727 · Feb 2024 | (tucci2024directmethaneoxidation pages 3-5) | Indirect but strong support linking Cu acquisition to pMMO function. |
| Methylomirabilis oxyfera | uses | nitric oxide dismutation | “it reduces nitrite to nitric oxide, follows with dismutation of nitric oxide to N2 and O2” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Strong mechanistic edge for intra-aerobic methanotrophy. |
| nitric oxide dismutation | produces | O2 | “dismutation of nitric oxide to N2 and O2” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Key enabling process under anoxia. |
| intracellular O2 in Methylomirabilis | enables | pMMO-mediated methane activation under anoxia | “the produced O2 is used by particulate methane monooxygenase (pMMO) to activate methane” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Strong edge; specifically for NC10/Methylomirabilis, not general methanotrophs. |
| Methanoperedens nitroreducens | uses | reverse methanogenesis pathway | “operates via a reverse methanogenesis pathway” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Strong taxon-specific edge for archaeal anaerobic methanotrophy. |
| methyl-coenzyme M reductase (MCR) | activates | methane in Methanoperedens | “relies on methyl-coenzyme M reductase (MCR) for methane activation” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Strong mechanistic edge. |
| nitrate | serves_as_electron_acceptor_for | Methanoperedens-dependent methane oxidation | “producing CO2 while reducing nitrate to nitrite” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Strong edge for nitrate-dependent AOM. |
| 1,7-octadiyne | inhibits | pMMO / Methylomirabilis activity | “Ca. M. oxyfera was shown to be susceptible to the particulate methane monooxygenase inhibitor 1,7-octadiyne (100 μM)” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Inhibitor edge; taxon/process-specific. |
| 2-bromoethanesulfonate (2-BES) | inhibits | MCR / Methanoperedens activity | “Methanoperedens is susceptible to puromycin and 2-bromoethanesulfonate (2-BES, MCR inhibitor at 20 mM)” | 10.1021/acs.est.3c07197 · https://doi.org/10.1021/acs.est.3c07197 · Mar 2024 | (wissink2024probingdenitrifyinganaerobic pages 1-2) | Inhibitor edge; taxon/process-specific. |
| upflow fixed bed bioreactor (UFBR) configuration | enables | denitrification coupled to methane oxidation (DOM) under anoxic conditions | “the study’s UFBR achieved up to 77% methane removal and up to 90% nitrite/nitrate removal after ~400 days” | 10.1007/s11270-024-07555-x · https://doi.org/10.1007/s11270-024-07555-x · Oct 2024 | (molinamacias2024implementationofan pages 1-2) | Application edge; engineered system rather than intrinsic trait. |
| UFBR DOM system | achieves | 77% methane removal | “achieved up to 77% methane removal” | 10.1007/s11270-024-07555-x · https://doi.org/10.1007/s11270-024-07555-x · Oct 2024 | (molinamacias2024implementationofan pages 1-2) | Performance metric for engineered implementation. |
| UFBR DOM system | achieves | 17.6 mgN-NO2−/L-d nitrite removal rate | “maximum nitrite and nitrate removal rates of 17.6 mgN-NO2−/L-d and 8.9 mgN-NO3−/L-d” | 10.1007/s11270-024-07555-x · https://doi.org/10.1007/s11270-024-07555-x · Oct 2024 | (molinamacias2024implementationofan pages 1-2) | Performance metric for engineered implementation. |
| aerobic methanotroph biofilters at 1000 ppm CH4 | can_remove | ~0.32 tonnes CH4/m3/year | “measured capacities include 0.32 tonnes/m3/year at 1000 ppm” | 10.1101/cshperspect.a041671 · https://doi.org/10.1101/cshperspect.a041671 · Nov 2024 | (lidstrom2024directmethaneremoval pages 2-4) | Application edge from review/modeling summary; likely context-dependent and not universal. |


*Table: This table lists candidate subject–predicate–object edges for curating the methanotrophic trait, linking core enzymes, regulators, pathways, inhibitors, and engineered applications to direct literature evidence. It is useful as a starting point for TraitMech graph curation because it pairs each edge with a near-verbatim snippet, DOI-first reference, and uncertainty note.*

---

## Recent developments and expert analysis (2023–2024 emphasis)

### 1) Structural/biochemical advances and persistent uncertainties in MMO mechanisms
A 2024 **Chemical Reviews** synthesis emphasizes that methanotrophs “convert methane to methanol” first via complex MMO enzyme systems; it distinguishes **copper-dependent pMMO** and **diiron sMMO**, noting that while pMMO structure has been extensively studied, aspects of its regulation and mechanism remain “enigmatic.” (tucci2024directmethaneoxidation pages 1-3)

The 2023 **Catalysis Science & Technology** review provides curated details for pMMO and sMMO subunits and the “copper switch,” including explicit gene-level mapping (pmoCAB; mmoXYZ plus mmoB/mmoC), which is highly actionable for mechanistic curation. (sakai2023methanemonooxygenases;physiology pages 3-4, sakai2023methanemonooxygenases;physiology pages 2-3)

### 2) Copper-dependent regulation (“copper switch”) as a central causal lever
Copper is repeatedly identified as central to methanotroph physiology because it is a required cofactor for pMMO, and expression shifts between sMMO and pMMO under differing copper availability (“copper switch”). (tucci2024directmethaneoxidation pages 3-5, sakai2023methanemonooxygenases;physiology pages 3-4)

The 2024 Methane journal paper on *Methylosinus trichosporium* OB3b provides a quantitative regime for this switch, reporting that **Cu concentrations between 3–5 µM** allow expression of both sMMO and pMMO in OB3b, with transcriptional downregulation of sMMO genes and upregulation of pMMO at higher Cu. (samanta2024geneticalandbiochemical pages 16-17)

### 3) Expansion of recognized methanotrophic modes in anoxic environments
A 2024 **Nature Microbiology** study reports methane-dependent complete denitrification by a single *Methylomirabilis* bacterium (“Ca. *M. sinica*”), revising a two-organism paradigm and providing kinetic/statistical constraints relevant to engineered systems (e.g., nitrate Km = **10.5 ± 0.9 µM**). (yao2024methanedependentcompletedenitrification pages 8-9)

A 2024 **Nature Communications** study demonstrates that aerobic methane-oxidizing bacteria (MOB; Methylococcales) can remain active in anoxic lake waters, with measured anaerobic methane oxidation rates **up to 0.2 µM d−1**, and proposes metabolic versatility including fermentation-based methanotrophy and denitrification as explanatory mechanisms. (sina2024persistentactivityof pages 1-2)

---

## Current applications and real-world implementations (with quantitative data)

### A) Methane mitigation using aerobic methanotroph biofilters (air treatment)
A 2024 perspective on **direct methane removal from air** compiles modeling and measured biofilter capacities for elevated-methane air streams. It reports **measured capacities** around **0.32 tonnes CH4·m−3·year−1 at 1000 ppm**, with modeled/estimated values lower at 500 ppm (e.g., ~0.1–0.16 tonnes·m−3·year−1 depending on assumptions). These values are directly relevant for evaluating real-world engineered capture at point sources or near-source air. (lidstrom2024directmethaneremoval pages 2-4)

**Curation relevance:** This motivates assay/phenotype nodes such as “methane removal efficiency” and “elimination capacity,” but these should be stored as application-level performance rather than intrinsic trait edges unless assay context is captured explicitly. (lidstrom2024directmethaneremoval pages 2-4)

### B) Wastewater and nitrogen removal via denitrification coupled to methane oxidation (DOM / N-DAMO engineering)
A 2024 engineered-system report implementing an **upflow fixed bed bioreactor (UFBR)** for DOM under anoxic conditions achieved **up to 77% methane removal** and **up to 90% nitrite/nitrate removal**, with **maximum nitrite removal 17.6 mgN-NO2−·L−1·d−1** and **maximum nitrate removal 8.9 mgN-NO3−·L−1·d−1**, after a long stabilization (~400 days). (molinamacias2024implementationofan pages 1-2)

**Curation relevance:** These data support the existence of a viable engineered ecology where methanotrophic activity is coupled to denitrification. Edges should be marked “engineered-system context” because the UFBR configuration is not a microbial mechanism per se. (molinamacias2024implementationofan pages 1-2)

### C) Methane-to-methanol bioconversion (biomanufacturing)
A 2024 methanotroph review reports that adding hydrogen “nearly doubled” methanol production “to approximately **0.32 g·L−1**” with “**66% conversion efficiency**” (context: methanol production strategies using MMO). (ahmadi2024recentfindingsin pages 7-9)

---

## Candidate statistics and datapoints for trait context (recent sources)
- Methanotrophs consume methane and are estimated in one review to consume **~30 Tg yr−1** methane (bacterial methanotroph consumption, review-level estimate). (tucci2024directmethaneoxidation pages 1-3)
- In a stratified lake system, anaerobic methane oxidation rates in anoxic hypolimnion reached **up to 0.2 µM d−1**. (sina2024persistentactivityof pages 1-2)
- In an anoxic UFBR DOM system: **77% methane removal**, with nitrogen removal rates **17.6 mgN-NO2−·L−1·d−1** and **8.9 mgN-NO3−·L−1·d−1**. (molinamacias2024implementationofan pages 1-2)
- For direct air/biofilter treatment at elevated methane: **0.32 tonnes CH4·m−3·year−1 at 1000 ppm** (reported as measured capacity in the review). (lidstrom2024directmethaneremoval pages 2-4)
- Copper-switch regime example: **3–5 µM Cu** supports expression of both sMMO and pMMO in OB3b (with relative regulation outside this range). (samanta2024geneticalandbiochemical pages 16-17)

---

## Warnings / claims not yet safe to curate into TraitMech
1. **pMMO catalytic metal site identity and full mechanistic scheme** remains debated/“enigmatic” in authoritative reviews; avoid over-curating a single active-site model as canonical unless explicitly supported by strong consensus evidence. (tucci2024directmethaneoxidation pages 1-3, sakai2023methanemonooxygenases;physiology pages 5-6)
2. **Anoxic activity of “aerobic MOB”** (e.g., Methylococcales in anoxic hypolimnion) involves proposed versatility (fermentation-based methanotrophy/denitrification). These are compelling but may be ecosystem- and taxon-specific; curate as **uncertain** unless coupled to direct genetic/enzymatic evidence for the taxa in question. (sina2024persistentactivityof pages 1-2)
3. **Application performance metrics** (biofilters, UFBRs) are not intrinsic traits; curate them only with explicit assay/engineering context nodes (reactor type, influent ppm/µM, residence time, temperature). (molinamacias2024implementationofan pages 1-2, lidstrom2024directmethaneremoval pages 2-4)

---

## DOI-first bibliography (URLs + publication dates)
1. Tucci FJ, Rosenzweig AC. *Direct Methane Oxidation by Copper- and Iron-Dependent Methane Monooxygenases.* **Chemical Reviews** (Feb 2024). DOI: **10.1021/acs.chemrev.3c00727**. https://doi.org/10.1021/acs.chemrev.3c00727 (tucci2024directmethaneoxidation pages 1-3)
2. Sakai Y, Yurimoto H, Shima S. *Methane monooxygenases; physiology, biochemistry and structure.* **Catalysis Science & Technology** (Jan 2023). DOI: **10.1039/D3CY00737E**. https://doi.org/10.1039/D3CY00737E (sakai2023methanemonooxygenases;physiology pages 1-2)
3. Ahmadi F, Lackner M. *Recent findings in methanotrophs: genetics, molecular ecology, and biopotential.* **Applied Microbiology and Biotechnology** (Jan 2024). DOI: **10.1007/s00253-023-12978-3**. https://doi.org/10.1007/s00253-023-12978-3 (ahmadi2024recentfindingsin pages 1-2)
4. Yao X, et al. *Methane-dependent complete denitrification by a single Methylomirabilis bacterium.* **Nature Microbiology** (Jan 2024). DOI: **10.1038/s41564-023-01578-6**. https://doi.org/10.1038/s41564-023-01578-6 (yao2024methanedependentcompletedenitrification pages 1-3)
5. Wissink M, et al. *Probing Denitrifying Anaerobic Methane Oxidation via Antimicrobial Intervention: Implications for Innovative Wastewater Management.* **Environmental Science & Technology** (Mar 2024). DOI: **10.1021/acs.est.3c07197**. https://doi.org/10.1021/acs.est.3c07197 (wissink2024probingdenitrifyinganaerobic pages 1-2)
6. Schorn S, et al. *Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility.* **Nature Communications** (Jun 2024). DOI: **10.1038/s41467-024-49602-5**. https://doi.org/10.1038/s41467-024-49602-5 (sina2024persistentactivityof pages 1-2)
7. Molina-Macías AK, et al. *Implementation of an Upflow Fixed Bed Bioreactor for Denitrification Coupled to Methane Oxidation: Performance and Biomass Development Under Anoxic Conditions.* **Water, Air, & Soil Pollution** (Oct 2024). DOI: **10.1007/s11270-024-07555-x**. https://doi.org/10.1007/s11270-024-07555-x (molinamacias2024implementationofan pages 1-2)
8. Lidstrom ME. *Direct Methane Removal from Air by Aerobic Methanotrophs.* **Cold Spring Harbor Perspectives in Biology** (Nov 2024). DOI: **10.1101/cshperspect.a041671**. https://doi.org/10.1101/cshperspect.a041671 (lidstrom2024directmethaneremoval pages 2-4)
9. Samanta D, et al. *Genetical and Biochemical Basis of Methane Monooxygenases of Methylosinus trichosporium OB3b in Response to Copper.* **Methane** (Feb 2024). DOI: **10.3390/methane3010007**. https://doi.org/10.3390/methane3010007 (samanta2024geneticalandbiochemical pages 1-2)


References

1. (sakai2023methanemonooxygenases;physiology pages 1-2): Yasuyoshi Sakai, Hiroya Yurimoto, and Seigo Shima. Methane monooxygenases; physiology, biochemistry and structure. Catalysis Science &amp; Technology, 13:6342-6354, Jan 2023. URL: https://doi.org/10.1039/d3cy00737e, doi:10.1039/d3cy00737e. This article has 27 citations and is from a peer-reviewed journal.

2. (tucci2024directmethaneoxidation pages 1-3): Frank J. Tucci and Amy C. Rosenzweig. Direct methane oxidation by copper- and iron-dependent methane monooxygenases. Chemical reviews, 124:1288-1320, Feb 2024. URL: https://doi.org/10.1021/acs.chemrev.3c00727, doi:10.1021/acs.chemrev.3c00727. This article has 142 citations and is from a highest quality peer-reviewed journal.

3. (ahmadi2024recentfindingsin pages 1-2): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 33 citations and is from a domain leading peer-reviewed journal.

4. (ahmadi2024recentfindingsin pages 9-11): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 33 citations and is from a domain leading peer-reviewed journal.

5. (sakai2023methanemonooxygenases;physiology pages 2-3): Yasuyoshi Sakai, Hiroya Yurimoto, and Seigo Shima. Methane monooxygenases; physiology, biochemistry and structure. Catalysis Science &amp; Technology, 13:6342-6354, Jan 2023. URL: https://doi.org/10.1039/d3cy00737e, doi:10.1039/d3cy00737e. This article has 27 citations and is from a peer-reviewed journal.

6. (tucci2024directmethaneoxidation pages 3-5): Frank J. Tucci and Amy C. Rosenzweig. Direct methane oxidation by copper- and iron-dependent methane monooxygenases. Chemical reviews, 124:1288-1320, Feb 2024. URL: https://doi.org/10.1021/acs.chemrev.3c00727, doi:10.1021/acs.chemrev.3c00727. This article has 142 citations and is from a highest quality peer-reviewed journal.

7. (wissink2024probingdenitrifyinganaerobic pages 1-2): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 16 citations and is from a domain leading peer-reviewed journal.

8. (sina2024persistentactivityof pages 1-2): Sina Schorn, Jon S. Graf, Sten Littmann, Philipp F. Hach, Gaute Lavik, Daan R. Speth, Carsten Schubert, Marcel M.M. Kuypers, and Jana Milucka. Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49602-5, doi:10.1038/s41467-024-49602-5. This article has 61 citations and is from a highest quality peer-reviewed journal.

9. (sakai2023methanemonooxygenases;physiology pages 3-4): Yasuyoshi Sakai, Hiroya Yurimoto, and Seigo Shima. Methane monooxygenases; physiology, biochemistry and structure. Catalysis Science &amp; Technology, 13:6342-6354, Jan 2023. URL: https://doi.org/10.1039/d3cy00737e, doi:10.1039/d3cy00737e. This article has 27 citations and is from a peer-reviewed journal.

10. (sakai2023methanemonooxygenases;physiology pages 5-6): Yasuyoshi Sakai, Hiroya Yurimoto, and Seigo Shima. Methane monooxygenases; physiology, biochemistry and structure. Catalysis Science &amp; Technology, 13:6342-6354, Jan 2023. URL: https://doi.org/10.1039/d3cy00737e, doi:10.1039/d3cy00737e. This article has 27 citations and is from a peer-reviewed journal.

11. (samanta2024geneticalandbiochemical pages 1-2): Dipayan Samanta, Tanvi Govil, Priya Saxena, Lee Krumholz, Venkataramana Gadhamshetty, Kian Mau Goh, and Rajesh K. Sani. Genetical and biochemical basis of methane monooxygenases of methylosinus trichosporium ob3b in response to copper. Methane, 3:103-121, Feb 2024. URL: https://doi.org/10.3390/methane3010007, doi:10.3390/methane3010007. This article has 7 citations.

12. (yao2024methanedependentcompletedenitrification pages 1-3): Xiangwu Yao, Jiaqi Wang, Mingyue He, Zishu Liu, Yuxiang Zhao, Yufen Li, Taolve Chi, Lin Zhu, Ping Zheng, Mike S. M. Jetten, and Baolan Hu. Methane-dependent complete denitrification by a single methylomirabilis bacterium. Nature microbiology, 9:464-476, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01578-6, doi:10.1038/s41564-023-01578-6. This article has 97 citations and is from a highest quality peer-reviewed journal.

13. (yao2024methanedependentcompletedenitrification pages 8-9): Xiangwu Yao, Jiaqi Wang, Mingyue He, Zishu Liu, Yuxiang Zhao, Yufen Li, Taolve Chi, Lin Zhu, Ping Zheng, Mike S. M. Jetten, and Baolan Hu. Methane-dependent complete denitrification by a single methylomirabilis bacterium. Nature microbiology, 9:464-476, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01578-6, doi:10.1038/s41564-023-01578-6. This article has 97 citations and is from a highest quality peer-reviewed journal.

14. (ahmadi2024recentfindingsin pages 7-9): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 33 citations and is from a domain leading peer-reviewed journal.

15. (molinamacias2024implementationofan pages 1-2): Anngie K. Molina-Macías, Yudy Andrea Londoño, Nancy Pino, and Gustavo A. Peñuela. Implementation of an upflow fixed bed bioreactor for denitrification coupled to methane oxidation: performance and biomass development under anoxic conditions. Water, Air, &amp; Soil Pollution, Oct 2024. URL: https://doi.org/10.1007/s11270-024-07555-x, doi:10.1007/s11270-024-07555-x. This article has 2 citations.

16. (samanta2024geneticalandbiochemical pages 16-17): Dipayan Samanta, Tanvi Govil, Priya Saxena, Lee Krumholz, Venkataramana Gadhamshetty, Kian Mau Goh, and Rajesh K. Sani. Genetical and biochemical basis of methane monooxygenases of methylosinus trichosporium ob3b in response to copper. Methane, 3:103-121, Feb 2024. URL: https://doi.org/10.3390/methane3010007, doi:10.3390/methane3010007. This article has 7 citations.

17. (lidstrom2024directmethaneremoval pages 2-4): Mary E. Lidstrom. Direct methane removal from air by aerobic methanotrophs. Cold Spring Harbor perspectives in biology, 16:a041671, Nov 2024. URL: https://doi.org/10.1101/cshperspect.a041671, doi:10.1101/cshperspect.a041671. This article has 19 citations and is from a peer-reviewed journal.