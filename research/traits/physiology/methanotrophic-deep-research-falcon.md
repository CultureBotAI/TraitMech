---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:22:11.058938'
end_time: '2026-08-04T11:30:35.398421'
duration_seconds: 504.34
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
  causal_graph_summary: 'methanotrophic_methane_oxidation: 20 nodes, 15 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methanotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000650
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** methanotroph
- **Existing evidence:** DOI:10.1039/D3CY00737E: convert methane to methanol using methane monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy step.)
- **Existing causal graph summary:** methanotrophic_methane_oxidation: 20 nodes, 15 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000650
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses methane as the primary carbon and energy source through oxidation of methane to carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** methanotroph
- **Existing evidence:** DOI:10.1039/D3CY00737E: convert methane to methanol using methane monooxygenase (Review supports methane monooxygenase as the first aerobic methanotrophy step.)
- **Existing causal graph summary:** methanotrophic_methane_oxidation: 20 nodes, 15 edges

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


# Curation report: methanotrophic

**Trait:** `METPO:1000650`  
**Category:** PHYSIOLOGY · **Kind:** CLASS · **Status:** REVIEWED

## 1. Scope summary

`METPO:1000650` should denote the physiological capacity to use methane as a primary carbon and energy source through methane oxidation. The canonical aerobic route is **CH₄ → methanol → formaldehyde → formate → CO₂**, with methane carbon assimilated principally at the formaldehyde level. Methanotrophs are a methane-using subset of the broader methylotrophs; possession of methanol-dehydrogenase or other methylotrophy genes alone is therefore insufficient. A 2024 floodplain study found methanol-dehydrogenase-containing MAGs that lacked methane monooxygenase and should not be classified as methanotrophs. (rasmussen2024diverseandunconventional pages 7-10, semrau2018metalsandmethanotrophy pages 3-5, ahmadi2024recentfindingsin pages 1-2)

The supplied definition is broadly correct but is too narrow if the class is intended to include anaerobic methanotrophic archaea and NC10/Methylomirabilis bacteria. ANME archaea activate methane with methyl-coenzyme M reductase (MCR), not methane monooxygenase, and couple oxidation to external electron acceptors. *Ca. Methylomirabilis* performs “intra-aerobic” methane oxidation: nitrite-derived nitric oxide is dismutated to N₂ and O₂, and the internally generated O₂ supports pMMO. (wissink2024probingdenitrifyinganaerobic pages 1-2, dinh2024towardtheuse pages 2-4, dinh2024towardtheuse pages 1-2)

### Boundaries

- **Methanotroph versus methylotroph:** methane utilization is defining; methanol or methyl-compound utilization without methane activation is methylotrophy, not methanotrophy. The evolutionary evidence is consistent with methanotrophy arising from methylotrophy after acquisition of MMO genes. (rasmussen2024diverseandunconventional pages 7-10, kang2019theoriginof pages 1-1)
- **Facultative methanotrophs remain in scope:** methane need not be the organism’s exclusive carbon source. Some recognized methanotrophs also grow on acetate or other multicarbon compounds. Thus “primary carbon and energy source” should be interpreted as an assayed capacity, not an obligate nutritional restriction. (ahmadi2024recentfindingsin pages 7-9)
- **Methanogenesis is out of scope:** methane production is not methanotrophy, although MCR catalyzes methane formation in methanogens and the initial reverse reaction in ANME. (dinh2024towardtheuse pages 2-4, dinh2024towardtheuse pages 1-2)
- **Cometabolic oxidation alone is insufficient:** oxidation of methane or other hydrocarbons without methane-supported carbon assimilation and energy conservation should not automatically confer the trait.
- **Genotype is not phenotype:** `pmoA/pmoCAB`, `mmoX/mmoXYBZDC`, or `mcrA/mcrABG` supports mechanistic potential, but incomplete MAGs, promiscuous monooxygenases, and pathway directionality require activity or sufficiently complete pathway evidence. (rasmussen2024diverseandunconventional pages 7-10)
- **Aerobic versus anaerobic should be represented as alternative mechanistic branches**, not collapsed into one universal linear graph.

## 2. Candidate nodes

### Trait and processes

- `METPO:1000650` — methanotrophic
- aerobic methane oxidation
- anaerobic oxidation of methane (AOM)
- reverse methanogenesis
- nitrate-/nitrite-dependent anaerobic methane oxidation (N-DAMO)
- sulfate-dependent AOM
- extracellular electron transfer (EET)
- RuMP pathway
- serine cycle
- H₄MPT/H₄F-linked formaldehyde oxidation
- fermentation-based methanotrophy — **provisional**
- denitrification / partial denitrification — taxon-specific

### Chemicals and environmental inputs

Verified high-value chemical candidates are:

- `CHEBI:16183` — methane
- `CHEBI:17790` — methanol
- `CHEBI:16842` — formaldehyde
- `CHEBI:15740` — formate
- `CHEBI:16526` — carbon dioxide
- `CHEBI:15379` — dioxygen

Additional label-only candidates pending identifier verification include nitrate, nitrite, nitric oxide, dinitrogen, sulfate, sulfide, copper, calcium, lanthanides, NADH/NADPH, PQQ, coenzyme M, coenzyme B, coenzyme F430, iron oxide, manganese oxide, humic substances, electrodes, ammonium, lead, nickel, and cadmium.

### Enzymes, complexes, and genes

- particulate methane monooxygenase, **pMMO**; genes `pmoCAB`
- soluble methane monooxygenase, **sMMO**; genes commonly represented by `mmoXYBZDC`
- calcium-dependent methanol dehydrogenase, **MxaFI**; `mxaFI`
- lanthanide-dependent methanol dehydrogenase, **XoxF**; `xoxF`
- formaldehyde-oxidation modules linked to H₄MPT/H₄F
- formate dehydrogenase
- methyl-coenzyme M reductase, **MCR**; `mcrABG`
- nitrate reductase; nitrite reductase
- nitric-oxide dismutation machinery — exact enzymatic grounding remains unresolved
- multiheme c-type cytochromes
- candidate OmcZ-like nanowire machinery — **preprint/provisional**
- methanobactin and copper-uptake machinery
- LanA TonB-dependent receptor — taxon-specific lanthanide-switch component

Do not assign EC, Rhea, KEGG, MetaCyc, GO, or UniProt accessions until the exact reaction, enzyme form, taxon, and database record are checked. Label-only nodes are preferable to an incorrect identifier.

### Cellular locations and structures

- cytoplasm — sMMO
- cytoplasmic/intracytoplasmic membrane — pMMO
- periplasm — many bacterial PQQ-dependent MDHs
- extracellular/anode-associated biofilm
- archaeal cell envelope/S-layer and extracellular conductive structures — candidate EET branch

### Taxon-scoping nodes

- Type I/X aerobic methanotrophs — predominantly RuMP assimilation
- Type II aerobic methanotrophs — predominantly serine-cycle assimilation
- ANME-1, ANME-2abc, ANME-3 — commonly marine, sulfate-linked AOM
- ANME-2d / *Ca. Methanoperedens* — freshwater nitrate-, metal-, humic-, or electrode-linked AOM
- NC10/Methylomirabilota / *Ca. Methylomirabilis* — nitrite-dependent intra-aerobic methanotrophy
- Methylococcales — recent evidence for activity under apparent anoxia, but mechanism requires cautious representation

## 3. Candidate causal edges

The following table is the curation-ready core. It separates general mechanisms from organism-, habitat-, and assay-specific extensions.

| Subject | Predicate | Object | Scope/taxon | Supporting quote/snippet | DOI reference and publication date/year | Curation note/confidence |
|---|---|---|---|---|---|---|
| METPO:1000650 | has_primary_substrate | CHEBI:16183 methane | Methanotrophs, general | “methanotrophic bacteria … utilize methane as their sole carbon and energy source” (ahmadi2024recentfindingsin pages 1-2) | 10.1007/s00253-023-12978-3 (Applied Microbiology and Biotechnology, Jan 2024) | High confidence for trait scope; note some facultative methanotrophs can also use multicarbon compounds, so this is primary/defining substrate rather than exclusive substrate in all taxa. |
| methane monooxygenase (grounding pending) | catalyzes_oxidation_of | CHEBI:16183 methane | Aerobic methanotrophs, general | “use methane monooxygenases (MMOs) to activate methane, oxidizing it to methanol” (koo2021biochemistryofaerobic pages 1-2) | 10.1039/d0cs01291b (Chem. Soc. Rev., 2021) | High confidence; core aerobic edge. Enzyme node can later be split into pMMO and sMMO. |
| CHEBI:15379 dioxygen | required_for_initial_activation_of | CHEBI:16183 methane | Aerobic bacterial methanotrophs | “oxygen is required by the MOB for the first step of methane oxidation” and “activate methane … using molecular oxygen” (sina2024persistentactivityof pages 1-2) | 10.1038/s41467-024-49602-5 (Nature Communications, Jun 2024) | High confidence for aerobic bacterial methanotrophy. Do not overgeneralize to all methanotrophs because ANME use MCR-based AOM. |
| particulate methane monooxygenase (pMMO; grounding pending) | located_in | membrane | Aerobic methanotrophs, general | “particulate, membrane-bound pMMO” (koo2021biochemistryofaerobic pages 1-2) | 10.1039/d0cs01291b (Chem. Soc. Rev., 2021) | High confidence; cellular localization node grounding pending. |
| particulate methane monooxygenase (pMMO; grounding pending) | depends_on | copper | Aerobic methanotrophs, general | “the particulate, membrane-bound pMMO which is copper-dependent” (koo2021biochemistryofaerobic pages 1-2) | 10.1039/d0cs01291b (Chem. Soc. Rev., 2021) | High confidence. Copper ion CHEBI grounding could be added later if curated separately. |
| soluble methane monooxygenase (sMMO; grounding pending) | located_in | cytoplasm | Aerobic methanotrophs, general | “soluble, cytoplasmic sMMO” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (Applied and Environmental Microbiology, 2018) | High confidence. |
| soluble methane monooxygenase (sMMO; grounding pending) | has_cofactor | diiron active site | Aerobic methanotrophs, general | “sMMO … utilizes a diiron active site” (koo2021biochemistryofaerobic pages 1-2) | 10.1039/d0cs01291b (Chem. Soc. Rev., 2021) | High confidence; cofactor entity grounding pending. |
| copper availability | regulates_expression_of | pMMO versus sMMO | Aerobic methanotrophs expressing both MMOs | “expression controlled by copper availability” and “Cu(II) to biomass ratio determines whether methanotrophs express pMMO or sMMO, termed the 'copper switch'” (karthikeyan2021metal(loid)speciationand pages 3-5, semrau2018metalsandmethanotrophy pages 3-5) | 10.1186/s40168-021-01112-y (Microbiome, Jul 2021); 10.1128/AEM.02289-17 (AEM, 2018) | High confidence for taxa carrying both systems; taxon-specific, not universal because many strains encode only one MMO. |
| methanol dehydrogenase (MDH; grounding pending) | oxidizes | CHEBI:17790 methanol | Aerobic methanotrophs, general | “methanol … is then oxidized to formaldehyde by methanol dehydrogenase” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (AEM, 2018) | High confidence. |
| methanol dehydrogenase (MDH; grounding pending) | produces | CHEBI:16842 formaldehyde | Aerobic methanotrophs, general | “methanol … is then oxidized to formaldehyde by methanol dehydrogenase” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (AEM, 2018) | High confidence. |
| MxaFI methanol dehydrogenase (grounding pending) | has_metal_cofactor | calcium | Methanotrophs/methylotrophs with MxaFI | “the calcium-containing Mxa-MeDH” (kang2019theoriginof pages 1-1) | 10.1093/femsle/fnz096 (FEMS Microbiology Letters, May 2019) | High confidence for MxaFI; metal ion CHEBI grounding pending. |
| XoxF methanol dehydrogenase (grounding pending) | has_metal_cofactor | lanthanide | Methanotrophs/methylotrophs with XoxF | “the rare earth element-containing Xox-MeDH” (kang2019theoriginof pages 1-1) | 10.1093/femsle/fnz096 (FEMS Microbiology Letters, May 2019) | High confidence; lanthanide species-specific grounding pending. |
| lanthanides | repress_expression_of | mxaF | Type I methanotroph example; broader methylotroph switch literature | “Lanthanide metals … strongly repress the transcription of mxaF yet activate the transcription of xoxF” (karthikeyan2021metal(loid)speciationand pages 3-5) | 10.1128/JB.00120-19 (Journal of Bacteriology, Aug 2019) | High confidence for lanthanide switch, but mechanism/components are taxon-specific; curate as regulatory pattern, not universal quantitative rule. |
| lanthanides | activate_expression_of | xoxF | Type I methanotroph example; broader methylotroph switch literature | “strongly repress the transcription of mxaF yet activate the transcription of xoxF” (karthikeyan2021metal(loid)speciationand pages 3-5) | 10.1128/JB.00120-19 (Journal of Bacteriology, Aug 2019) | High confidence for lanthanide switch; taxon-specific implementation. |
| CHEBI:16842 formaldehyde | oxidized_to | CHEBI:15740 formate | Aerobic methanotrophs, general | “formaldehyde to formate via tetrahydrofolate/tetrahydromethanopterin pathways” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (AEM, 2018) | High confidence at pathway level; exact enzyme set may vary. |
| CHEBI:15740 formate | oxidized_to | CHEBI:16526 carbon dioxide | Aerobic methanotrophs, general | “formate to CO2 via formate dehydrogenase” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (AEM, 2018) | High confidence. |
| CHEBI:16842 formaldehyde | assimilated_via | RuMP pathway (grounding pending) | Type I/X and many aerobic methanotrophs | “Carbon assimilation occurs primarily at the formaldehyde level via ribulose monophosphate … cycles” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (AEM, 2018) | High confidence at general pathway level; not universal to every lineage. |
| CHEBI:16842 formaldehyde | assimilated_via | serine cycle (grounding pending) | Type II and many aerobic methanotrophs | “Carbon assimilation occurs primarily at the formaldehyde level via … serine cycles” (semrau2018metalsandmethanotrophy pages 3-5) | 10.1128/AEM.02289-17 (AEM, 2018) | High confidence at general pathway level. |
| type II methanotrophs | use_assimilation_pathway | serine cycle (grounding pending) | Alphaproteobacterial type II methanotrophs | “type II methanotrophs … use the serine pathway for formaldehyde assimilation” (ahmadi2024recentfindingsin pages 7-9) | 10.1007/s00253-023-12978-3 (Applied Microbiology and Biotechnology, Jan 2024) | High confidence, taxon-scoped. |
| methyl-coenzyme M reductase (MCR; grounding pending) | catalyzes_initial_step_of | anaerobic methane oxidation | ANME archaea | “MCR catalyzes … the initial methane oxidation step during the anaerobic oxidation of methane (AOM) in anaerobic methanotrophic archaea” (dinh2024towardtheuse pages 1-2) | 10.1021/acs.accounts.4c00413 (Accounts of Chemical Research, Aug 2024) | High confidence for ANME. Separate from aerobic MMO-based activation. |
| reverse methanogenesis pathway (grounding pending) | mediates | anaerobic methane oxidation | Ca. Methanoperedens nitroreducens | “‘Ca. M. nitroreducens’ … utilizes a reverse methanogenesis pathway for methane oxidation” (wissink2024probingdenitrifyinganaerobic pages 1-2) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence, taxon-specific. |
| marine ANME archaea | forms_syntrophy_with | sulfate-reducing bacteria | Marine sulfate-dependent AOM | “Most ANME exist in consortia with sulfate-reducing bacteria (SRB) that allow AOM to be coupled with sulfate reduction” (dinh2024towardtheuse pages 2-4) | 10.1021/acs.accounts.4c00413 (Accounts of Chemical Research, Aug 2024) | High confidence for many marine ANME; not all ANME. |
| Ca. Methanoperedens nitroreducens | reduces | nitrate to nitrite | Freshwater N-DAMO archaeon | “Methane is activated by the enzyme methyl-coenzyme M reductase (MCR) and further converted to CO2 while reducing nitrate to nitrite” (wissink2024probingdenitrifyinganaerobic pages 1-2) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence, organism-specific. |
| Ca. Methylomirabilis oxyfera | reduces | nitrite to nitric oxide | NC10/Methylomirabilis in N-DAMO | “‘Ca. Methylomirabilis oxyfera’ employs an intra-aerobic pathway reducing the nitrite … to nitric oxide” (wissink2024probingdenitrifyinganaerobic pages 1-2) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence, organism-specific. |
| nitric oxide dismutation (grounding pending) | produces | dinitrogen and CHEBI:15379 dioxygen | NC10/Methylomirabilis in N-DAMO | “followed by dismutation of nitric oxide to nitrogen gas and oxygen” (wissink2024probingdenitrifyinganaerobic pages 1-2) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence, organism-specific pathway step. |
| internally produced CHEBI:15379 dioxygen | used_by | pMMO | Ca. Methylomirabilis oxyfera | “this oxygen is directly used by its particulate methane monooxygenase (pMMO) to activate methane” (wissink2024probingdenitrifyinganaerobic pages 1-2) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence, organism-specific. |
| ANME-2d / Ca. Methanoperedens | uses_electron_acceptor | metal oxides | Freshwater ANME-2d | “ANME can use insoluble metal oxides as electron acceptors” and “can use … manganese oxides, iron oxides …” (ouboter2024mechanismsofextracellular pages 1-5) | 10.1101/2023.07.24.550278 (bioRxiv preprint, Jul 2024 version) | Moderate confidence because preprint; strong consistency with broader literature. Mark as provisional if strict peer-reviewed-only curation is required. |
| Ca. Methanoperedens | transfers_electrons_to | electrode | Bioelectrochemical enrichment assay | “observed strong methane-dependent current (91-93% of total current) associated with high enrichment of ‘Ca. Methanoperedens’ on the anode” (ouboter2024mechanismsofextracellular pages 1-5) | 10.1101/2023.07.24.550278 (bioRxiv preprint, Jul 2024 version) | Moderate confidence; assay-specific EET edge supported in electrode system, not necessarily universal environmental interaction. |
| Ca. Methanoperedens reverse methanogenesis genes | upregulated_in | electrode condition | Bioelectrochemical enrichment assay | “genes within the MAG encoding proteins of the reverse methanogenesis were upregulated in the electrode condition” (ouboter2024mechanismsofextracellular pages 10-16) | 10.1101/2023.07.24.550278 (bioRxiv preprint, Jul 2024 version) | Moderate confidence; mechanistic support for electrode-linked AOM but still preprint and system-specific. |
| 2-bromoethanesulfonate (2-BES; grounding pending) | inhibits | Ca. Methanoperedens-linked AOM/current | N-DAMO enrichment / bioelectrochemical assays | “susceptible to … 2-bromoethanesulfonate” and “20 mM 2-bromoethanosulfonate resulted in an immediate and strong reduction in current by 89%” (wissink2024probingdenitrifyinganaerobic pages 1-2, ouboter2024mechanismsofextracellular pages 10-16) | 10.1021/acs.est.3c07197 (Mar 29 2024); 10.1101/2023.07.24.550278 (Jul 2024 preprint) | High confidence that 2-BES is an effective inhibitor in these assays; do not curate as universal ANME inhibition because susceptibility varies by community/strain. |
| puromycin (grounding pending) | inhibits | Ca. Methanoperedens-linked AOM | N-DAMO enrichment | “‘Ca. M. nitroreducens’ was susceptible to puromycin” and “IC50 … <10 μg mL−1” (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 4-5) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence, assay-specific inhibitor edge. |
| 1,7-octadiyne (grounding pending) | inhibits | pMMO-dependent methane oxidation | Ca. Methylomirabilis oxyfera in N-DAMO enrichment | “susceptible to the particulate methane monooxygenase inhibitor 1,7-octadiyne” and “100 μM 1,7-OD resulted in a significant decrease in the AOM rate of 64 ± 23%” (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 4-5) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence for assay-specific inhibition of pMMO-linked activity. |
| 3-nitrooxypropanol (3-NOP; grounding pending) | does_not_significantly_inhibit | N-DAMO activity | N-DAMO enrichment | “3-nitrooxypropanol had no effect on N-DAMO” and “does not significantly affect AOM at concentrations 20 times higher” (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 4-5) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | High confidence for this enrichment; authors note possible degradation/modification, so mechanism of resistance should not yet be curated strongly. |
| ammonium | does_not_significantly_inhibit | N-DAMO activity below 10 mM | N-DAMO enrichment | “N-DAMO activity was not affected by ammonium concentrations below 10 mM” (wissink2024probingdenitrifyinganaerobic pages 1-2) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | Moderate-high confidence; engineering/application contextual edge, not defining trait mechanism. |
| lead | tolerated_by | N-DAMO community | N-DAMO enrichment | “remarkably resistant to lead (Pb)” and “IC50 value for Pb exceeds 1000 μM” (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 5-7) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | Moderate confidence; community-level, assay-specific. |
| nickel | inhibits | N-DAMO community | N-DAMO enrichment | “susceptible to nickel (Ni)” and “IC50 value of 0.23 mM” (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 5-7) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | Moderate confidence; community-level, assay-specific. |
| cadmium | strongly_inhibits | N-DAMO community | N-DAMO enrichment | “susceptible to … cadmium (Cd)” and “IC50 value for Cd below 10 μM” (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 5-7) | 10.1021/acs.est.3c07197 (Environmental Science & Technology, Mar 29 2024) | Moderate confidence; community-level, assay-specific. |
| Methylococcales aerobic MOB | may_use | fermentation-based methanotrophy | Anoxic lake waters; large rod-shaped gamma-MOB | “Our data suggest that these MOB use fermentation-based methanotrophy as well as denitrification under anoxic conditions” (sina2024persistentactivityof pages 1-2) | 10.1038/s41467-024-49602-5 (Nature Communications, Jun 2024) | Uncertain/provisional for TraitMech. Strong recent evidence, but mechanism remains partly inferential and still presumes trace O2 may be required for initial MMO step. |
| Methylococcales aerobic MOB | may_use | denitrification | Anoxic lake waters; large rod-shaped gamma-MOB | “these MOB use fermentation-based methanotrophy as well as denitrification under anoxic conditions” (sina2024persistentactivityof pages 1-2) | 10.1038/s41467-024-49602-5 (Nature Communications, Jun 2024) | Uncertain/provisional; taxon- and habitat-specific, with incomplete causal resolution. |
| trace CHEBI:15379 dioxygen | may_be_required_for | initial MMO step under apparent anoxia | Anoxic Methylococcales scenario | “this trace oxygen is likely indispensable for the initial oxidation of methane to methanol by methane monooxygenase” (sina2024persistentactivityof pages 6-7) | 10.1038/s41467-024-49602-5 (Nature Communications, Jun 2024) | Important caution: do not curate truly oxygen-independent bacterial MMO methanotrophy from this study. |
| Methylococcales in anoxic lake water | associated_with_rate | anaerobic methane oxidation up to 0.2 µM d−1 | Lake Zug hypolimnion | “rates of anaerobic methane oxidation in the anoxic hypolimnion reached up to 0.2 µM d−1” (sina2024persistentactivityof pages 1-2) | 10.1038/s41467-024-49602-5 (Nature Communications, Jun 2024) | Quantitative ecological support, not a causal edge per se; useful for evidence annotation and application context. |
| Ca. Methanoperedens in BES | associated_with | methane-dependent current 91–93% and abundance up to 82% | Bioelectrochemical system | “methane-dependent current (91-93% of total current)” and “‘Ca. Methanoperedens’ … up to 82% of the community” (ouboter2024mechanismsofextracellular pages 1-5) | 10.1101/2023.07.24.550278 (bioRxiv preprint, Jul 2024 version) | Quantitative assay support for EET-related nodes/edges; preprint and system-specific. |


*Table: This table compiles candidate TraitMech causal edges for methanotrophy (METPO:1000650) with short evidence snippets, scoped taxa, and curation confidence. It emphasizes which edges are broadly established versus taxon-specific, assay-specific, or still uncertain.*

## 4. Recommended graph architecture

The existing 20-node/15-edge graph should be refactored into a conserved trait root with alternative branches:

1. **Aerobic activation branch**  
   `methane + O2 → methanol`, catalyzed by either membrane-bound copper-dependent pMMO or cytoplasmic diiron sMMO. The two MMOs are unrelated in architecture and mechanism. (koo2021biochemistryofaerobic pages 1-2, karthikeyan2021metal(loid)speciationand pages 3-5)

2. **Shared aerobic downstream branch**  
   `methanol → formaldehyde → formate → CO2`, with MDH, H₄MPT/H₄F-linked oxidation, and formate dehydrogenase. Formaldehyde also supplies assimilatory carbon through RuMP or serine-cycle modules. (semrau2018metalsandmethanotrophy pages 3-5)

3. **Metal-regulation subgraph**  
   Copper availability regulates pMMO versus sMMO expression only in organisms possessing both systems. Mxa-MDH is calcium-dependent, whereas XoxF-MDH uses rare-earth elements; lanthanides can repress `mxaF` and activate `xoxF`. These are conditional switches, not universal requirements of the trait. (kang2019theoriginof pages 1-1, karthikeyan2021metal(loid)speciationand pages 3-5)

4. **ANME/AOM branch**  
   `methane —MCR/reverse methanogenesis→ oxidized C1 intermediates/CO2`, with electrons delivered to sulfate-reducing partners, nitrate, oxidized metals, humic substances, or electrodes depending on lineage and environment. MCR contains the nickel-hydrocorphin coenzyme F430, but ANME MCR biochemistry remains difficult to establish directly: no ANME MCR in-vitro activity had been reported in the 2024 account. (dinh2024towardtheuse pages 2-4, dinh2024towardtheuse pages 4-5, dinh2024towardtheuse pages 1-2)

5. **N-DAMO branch**  
   *Ca. Methanoperedens nitroreducens* oxidizes methane by reverse methanogenesis while reducing nitrate to nitrite. *Ca. Methylomirabilis oxyfera* consumes nitrite, forms NO, dismutates NO to N₂ and O₂, and directs the O₂ to pMMO. This is a taxon-specific cooperative module rather than a universal methanotrophic pathway. (wissink2024probingdenitrifyinganaerobic pages 1-2)

## 5. Recent developments and quantitative evidence

### Apparent anoxic activity of aerobic MOB

A 2024 Lake Zug study measured methane oxidation in anoxic, nitrate-amended incubations at 0.07, 0.18, and 0.06 µM d⁻¹ at 123, 135, and 160 m, respectively; rates reached approximately 0.2 µM d⁻¹ and were 5–20-fold below paired hypoxic incubations. Large rod-shaped, Methylobacter-like MOB grew from 1.4 × 10⁴ to 3.7 × 10⁴ cells mL⁻¹ in eight days. Their cell-specific methane-carbon assimilation was similar under hypoxic and anoxic treatments—9.8 versus 8.6 fmol ¹³C cell⁻¹ d⁻¹—and as much as 56–60% of consumed methane carbon was recovered in biomass in deep anoxic incubations. (sina2024persistentactivityof pages 6-7, sina2024persistentactivityof pages 2-3, sina2024persistentactivityof pages 3-4)

This does **not** establish oxygen-independent pMMO chemistry. The investigators explicitly could not exclude trace O₂ and considered it likely indispensable for methane-to-methanol activation. The supported provisional interpretation is that fermentation and partial denitrification reduce total oxygen demand after an MMO-dependent first step. (sina2024persistentactivityof pages 6-7, sina2024persistentactivityof pages 1-2)

### N-DAMO physiology and inhibitors

A 2024 enrichment contained *Ca. M. nitroreducens* at 19% and *Ca. M. oxyfera* at 28% metagenomic abundance and displayed 70–755 µmol CH₄ d⁻¹ g dry-weight⁻¹ over approximately one year. Inhibiting either organism reduced total AOM by roughly 70%; combining 2-BES with a bacteria-suppressing cocktail stopped methane oxidation, suggesting that each organism could sustain about 30% of the consortium’s total rate independently but that cooperation substantially enhanced activity. (wissink2024probingdenitrifyinganaerobic pages 4-5, wissink2024probingdenitrifyinganaerobic pages 2-3)

Specific assay results were:

- 20 mM 2-BES and 3-BPS inhibited AOM by 75 ± 2% and 68 ± 4%, respectively.
- 100 µM 1,7-octadiyne reduced AOM by 64 ± 23%, supporting pMMO-dependent activity by *Ca. M. oxyfera*.
- 200 µM 3-NOP did not significantly inhibit N-DAMO, apparently because the enrichment modified or degraded it; this is not evidence that ANME MCR is intrinsically 3-NOP-resistant.
- AOM IC₅₀ values were <10 µg mL⁻¹ for puromycin, 52 mM for ammonium, >1 mM for Pb, 0.23 mM for Ni, and <10 µM for Cd.
- Ten micromolar Pb increased AOM by 38 ± 7%, an unexplained community-level effect. (wissink2024probingdenitrifyinganaerobic pages 3-4, wissink2024probingdenitrifyinganaerobic pages 4-5, wissink2024probingdenitrifyinganaerobic pages 5-7)

These inhibitor and metal effects belong in evidence annotations or an assay-specific extension, not in the minimal trait-defining graph.

### Extracellular electron transfer

A 2024 bioRxiv study of *Ca. Methanoperedens* reported methane-dependent current reaching 91–93% of total current and enrichment to 82% of the anode community. At four anode potentials, the community consumed 71 ± 0.017 µmol methane d⁻¹; 20 mM 2-BES immediately reduced current by 89%. Reverse-methanogenesis genes and multiheme-cytochrome clusters were upregulated with the electrode, and OmcZ-like machinery was proposed. (ouboter2024mechanismsofextracellular pages 5-10, ouboter2024mechanismsofextracellular pages 1-5, ouboter2024mechanismsofextracellular pages 10-16)

This is strong mechanistic evidence for an electrode-linked EET candidate branch, but it remains a **preprint**, uses an enrichment rather than an isolate, and does not yet establish the proposed short-range complex or nanowire mechanism as universal among ANME-2.

### Genomic diversity

A 2024 pangenomic analysis identified 15 methane oxidizers among 75 type-II methylotroph genomes: five encoded sMMO only, five pMMO only, and five both. It reported 12 sMMO copies across ten organisms and 22 pMMO copies, while only ten organisms encoded formaldehyde dehydrogenase. These results reinforce modularity but do not justify the inference that copy number alone determines methane-oxidation rate. (samanta2024fromgenometo pages 12-14)

A separate 2024 floodplain study generated 1,233 MAGs and recovered 57 putative methanogens, methanotrophs, or methylotrophs. *Ca. Methanoperedens* exceeded 50% of the MAG library in one sample at approximately 1,400× coverage, while >10% of all MAGs encoded methanol dehydrogenase. The latter statistic demonstrates why MDH is not a methanotrophy-specific marker. (rasmussen2024diverseandunconventional pages 7-10)

## 6. Applications and implementation status

- **Methane mitigation:** methanotrophs act as biological methane filters in soils, wetlands, sediments, lakes, landfills, and engineered biofilters. Methane’s 100-year warming effect is commonly reported as roughly 28–34 times that of CO₂, making control of methane oxidation ecologically significant. (ahmadi2024recentfindingsin pages 1-2)
- **Wastewater treatment:** N-DAMO can simultaneously consume dissolved methane and nitrate/nitrite without an added organic-carbon donor. Practical barriers include slow growth, enrichment dependence, gas–liquid mass transfer, and sensitivity to Ni/Cd. The observed tolerance below 10 mM ammonium and to environmentally relevant Pb supports continued reactor development, but full-scale robustness is not yet established. (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 5-7, wissink2024probingdenitrifyinganaerobic pages 2-3)
- **Biomanufacturing:** methane can be converted to methanol, biomass/single-cell protein, PHAs, organic acids, lipids, and other products. Authoritative analyses emphasize low methane solubility, oxygen transfer, slow growth, difficult genetic manipulation, and product recovery as major scale-up constraints. MCR-based platforms are attractive because anaerobic routes may improve carbon/energy efficiency, but MCR complexity, oxygen sensitivity, post-translational maturation, lack of recombinant activity, and ANME cultivation remain substantial obstacles. (koo2021biochemistryofaerobic pages 1-2, dinh2024towardtheuse pages 2-4, dinh2024towardtheuse pages 1-2)
- **Bioremediation:** broad MMO substrate ranges and methanotroph-mediated metal transformations support pollutant-remediation concepts. These activities are secondary capabilities and should not define `METPO:1000650`.
- **Bioelectrochemical cultivation:** electrodes may provide controllable electron sinks and help enrich otherwise uncultivated ANME, but the evidence is not yet equivalent to a deployed industrial process. (ouboter2024mechanismsofextracellular pages 1-5)

## 7. Expert interpretation

The most defensible TraitMech model is **modular rather than taxonomically monolithic**. The causal invariant is methane activation linked to energy conservation and carbon utilization; the activating enzyme, electron acceptor, carbon-assimilation pathway, metal regulation, and partner dependence vary by lineage. Aerobic methanotrophy should use MMO-based activation, whereas archaeal AOM should use an MCR/reverse-methanogenesis module. Treating MCR and MMO as members of one linear pathway would be mechanistically incorrect. (koo2021biochemistryofaerobic pages 1-2, dinh2024towardtheuse pages 2-4)

Similarly, `pmoA` is a strong marker for bacterial methane activation but is not by itself proof of expressed phenotype, while MDH is explicitly non-specific because methylotrophs that cannot activate methane also possess it. Recent metagenomics expands the candidate diversity but increases, rather than removes, the need for activity validation. (rasmussen2024diverseandunconventional pages 7-10, samanta2024fromgenometo pages 12-14)

## 8. Claims not yet ready for TraitMech curation

1. **Do not curate “all methanotrophs are obligate methane users.”** Facultative and mixotrophic methanotrophs are recognized.
2. **Do not use MDH, `xoxF`, or methylotroph taxonomy alone as proof of methanotrophy.** (rasmussen2024diverseandunconventional pages 7-10)
3. **Do not make O₂ a universal methanotrophy requirement.** It is required for MMO chemistry, not MCR-based ANME metabolism.
4. **Do not claim oxygen-independent pMMO activity in conventional Methylococcales.** The 2024 Lake Zug study could not exclude indispensable trace O₂. (sina2024persistentactivityof pages 6-7)
5. **Do not universalize the copper switch.** It applies only to organisms with both pMMO and sMMO; many genomes encode only one. (samanta2024fromgenometo pages 12-14, karthikeyan2021metal(loid)speciationand pages 3-5)
6. **Do not universalize RuMP or serine assimilation.** Represent them as alternative, taxon-scoped modules; additional assimilation strategies occur.
7. **Do not curate 2-BES as a universal ANME inhibitor.** Published responses range from inhibition at 1 mM to no measurable effect at 50 mM, indicating strain/community dependence. (wissink2024probingdenitrifyinganaerobic pages 4-5)
8. **Do not curate intrinsic 3-NOP resistance.** Community degradation or modification is a plausible explanation for the observed lack of inhibition. (wissink2024probingdenitrifyinganaerobic pages 4-5, wissink2024probingdenitrifyinganaerobic pages 5-7)
9. **Do not yet curate OmcZ nanowires or a universal ANME-2 EET complex as established facts.** Evidence is enrichment-based and preprint-only. (ouboter2024mechanismsofextracellular pages 1-5, ouboter2024mechanismsofextracellular pages 10-16)
10. **Do not infer reaction rate from MMO gene-copy number.** The 2024 pangenomic result is comparative genomic evidence, not a controlled kinetic test. (samanta2024fromgenometo pages 12-14)
11. **Do not infer methane oxidation from `mcrA` without directionality and pathway context.** MCR also catalyzes methane formation in methanogens.
12. **Do not merge organism-level tolerance measurements into the core trait.** Pb, Ni, Cd, ammonium, solvent, and antibiotic effects are community- and assay-specific.

## 9. DOI-first bibliography

1. Sakai Y, Yurimoto H, Shima S. **Methane monooxygenases; physiology, biochemistry and structure.** *Catalysis Science & Technology* 13, 6342–6354. Published 2023. https://doi.org/10.1039/D3CY00737E.
2. Ahmadi F, Lackner M. **Recent findings in methanotrophs: genetics, molecular ecology, and biopotential.** *Applied Microbiology and Biotechnology* 108. Published January 2024. https://doi.org/10.1007/s00253-023-12978-3. (ahmadi2024recentfindingsin pages 7-9, ahmadi2024recentfindingsin pages 1-2)
3. Schorn S et al. **Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility.** *Nature Communications* 15, 5293. Accepted June 7, 2024. https://doi.org/10.1038/s41467-024-49602-5. (sina2024persistentactivityof pages 6-7, sina2024persistentactivityof pages 1-2, sina2024persistentactivityof pages 3-4)
4. Wissink M et al. **Probing Denitrifying Anaerobic Methane Oxidation via Antimicrobial Intervention.** *Environmental Science & Technology* 58, 6250–6257. Published March 29, 2024. https://doi.org/10.1021/acs.est.3c07197. (wissink2024probingdenitrifyinganaerobic pages 1-2, wissink2024probingdenitrifyinganaerobic pages 4-5, wissink2024probingdenitrifyinganaerobic pages 5-7)
5. Dinh T-A, Allen KD. **Toward the Use of Methyl-Coenzyme M Reductase for Methane Bioconversion Applications.** *Accounts of Chemical Research* 57, 2746–2757. Published August 27, 2024. https://doi.org/10.1021/acs.accounts.4c00413. (dinh2024towardtheuse pages 2-4, dinh2024towardtheuse pages 1-2)
6. Rasmussen AN et al. **Diverse and unconventional methanogens, methanotrophs, and methylotrophs in metagenome-assembled genomes from subsurface sediments.** *mSystems* 9. Published July 2024. https://doi.org/10.1128/msystems.00314-24. (rasmussen2024diverseandunconventional pages 7-10)
7. Samanta D et al. **From genome to evolution: investigating type II methylotrophs using a pangenomic analysis.** *mSystems* 9. Published June 2024. https://doi.org/10.1128/msystems.00248-24. (samanta2024fromgenometo pages 12-14)
8. Koo CW, Rosenzweig AC. **Biochemistry of aerobic biological methane oxidation.** *Chemical Society Reviews* 50, 3424–3436. Published 2021. https://doi.org/10.1039/D0CS01291B. (koo2021biochemistryofaerobic pages 1-2)
9. Karthikeyan OP et al. **Metal(loid) speciation and transformation by aerobic methanotrophs.** *Microbiome* 9. Published July 2021. https://doi.org/10.1186/s40168-021-01112-y. (karthikeyan2021metal(loid)speciationand pages 3-5)
10. Semrau JD et al. **Metals and Methanotrophy.** *Applied and Environmental Microbiology* 84. Published March 2018. https://doi.org/10.1128/AEM.02289-17. (semrau2018metalsandmethanotrophy pages 3-5)
11. Kang CS, Dunfield PF, Semrau JD. **The origin of aerobic methanotrophy within the Proteobacteria.** *FEMS Microbiology Letters* 366. Published May 2019. https://doi.org/10.1093/femsle/fnz096. (kang2019theoriginof pages 1-1)
12. Ouboter HT et al. **Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea.** bioRxiv preprint, 2024 version. https://doi.org/10.1101/2023.07.24.550278. (ouboter2024mechanismsofextracellular pages 5-10, ouboter2024mechanismsofextracellular pages 1-5, ouboter2024mechanismsofextracellular pages 10-16)

References

1. (rasmussen2024diverseandunconventional pages 7-10): Anna N. Rasmussen, Bradley B. Tolar, John R. Bargar, Kristin Boye, and Christopher A. Francis. Diverse and unconventional methanogens, methanotrophs, and methylotrophs in metagenome-assembled genomes from subsurface sediments of the slate river floodplain, crested butte, co, usa. Jul 2024. URL: https://doi.org/10.1128/msystems.00314-24, doi:10.1128/msystems.00314-24. This article has 12 citations and is from a peer-reviewed journal.

2. (semrau2018metalsandmethanotrophy pages 3-5): Jeremy D. Semrau, Alan A. DiSpirito, Wenyu Gu, and Sukhwan Yoon. Metals and methanotrophy. Applied and Environmental Microbiology, Mar 2018. URL: https://doi.org/10.1128/aem.02289-17, doi:10.1128/aem.02289-17. This article has 183 citations and is from a peer-reviewed journal.

3. (ahmadi2024recentfindingsin pages 1-2): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 37 citations and is from a domain leading peer-reviewed journal.

4. (wissink2024probingdenitrifyinganaerobic pages 1-2): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 21 citations and is from a domain leading peer-reviewed journal.

5. (dinh2024towardtheuse pages 2-4): Thuc-Anh Dinh and Kylie D. Allen. Toward the use of methyl-coenzyme m reductase for methane bioconversion applications. Accounts of Chemical Research, 57:2746-2757, Aug 2024. URL: https://doi.org/10.1021/acs.accounts.4c00413, doi:10.1021/acs.accounts.4c00413. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (dinh2024towardtheuse pages 1-2): Thuc-Anh Dinh and Kylie D. Allen. Toward the use of methyl-coenzyme m reductase for methane bioconversion applications. Accounts of Chemical Research, 57:2746-2757, Aug 2024. URL: https://doi.org/10.1021/acs.accounts.4c00413, doi:10.1021/acs.accounts.4c00413. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (kang2019theoriginof pages 1-1): Christina S Kang, Peter F Dunfield, and Jeremy D Semrau. The origin of aerobic methanotrophy within the proteobacteria. FEMS microbiology letters, May 2019. URL: https://doi.org/10.1093/femsle/fnz096, doi:10.1093/femsle/fnz096. This article has 30 citations and is from a peer-reviewed journal.

8. (ahmadi2024recentfindingsin pages 7-9): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 37 citations and is from a domain leading peer-reviewed journal.

9. (koo2021biochemistryofaerobic pages 1-2): Christopher W. Koo and Amy C. Rosenzweig. Biochemistry of aerobic biological methane oxidation. Chemical Society reviews, 50:3424-3436, Jan 2021. URL: https://doi.org/10.1039/d0cs01291b, doi:10.1039/d0cs01291b. This article has 168 citations and is from a highest quality peer-reviewed journal.

10. (sina2024persistentactivityof pages 1-2): Sina Schorn, Jon S. Graf, Sten Littmann, Philipp F. Hach, Gaute Lavik, Daan R. Speth, Carsten Schubert, Marcel M.M. Kuypers, and Jana Milucka. Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49602-5, doi:10.1038/s41467-024-49602-5. This article has 69 citations and is from a highest quality peer-reviewed journal.

11. (karthikeyan2021metal(loid)speciationand pages 3-5): Obulisamy Parthiba Karthikeyan, Thomas J. Smith, Shamsudeen Umar Dandare, Kamaludeen Sara Parwin, Heetasmin Singh, Hui Xin Loh, Mark R Cunningham, Paul Nicholas Williams, Tim Nichol, Avudainayagam Subramanian, Kumarasamy Ramasamy, and Deepak Kumaresan. Metal(loid) speciation and transformation by aerobic methanotrophs. Microbiome, Jul 2021. URL: https://doi.org/10.1186/s40168-021-01112-y, doi:10.1186/s40168-021-01112-y. This article has 31 citations and is from a highest quality peer-reviewed journal.

12. (ouboter2024mechanismsofextracellular pages 1-5): Heleen T Ouboter, Rob Mesman, Tom Sleutels, Jelle Postma, Martijn Wissink, Mike S M Jetten, Annemiek ter Heijne, Tom Berben, and Cornelia U Welte. Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2023.07.24.550278, doi:10.1101/2023.07.24.550278. This article has 73 citations.

13. (ouboter2024mechanismsofextracellular pages 10-16): Heleen T Ouboter, Rob Mesman, Tom Sleutels, Jelle Postma, Martijn Wissink, Mike S M Jetten, Annemiek ter Heijne, Tom Berben, and Cornelia U Welte. Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2023.07.24.550278, doi:10.1101/2023.07.24.550278. This article has 73 citations.

14. (wissink2024probingdenitrifyinganaerobic pages 4-5): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 21 citations and is from a domain leading peer-reviewed journal.

15. (wissink2024probingdenitrifyinganaerobic pages 5-7): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 21 citations and is from a domain leading peer-reviewed journal.

16. (sina2024persistentactivityof pages 6-7): Sina Schorn, Jon S. Graf, Sten Littmann, Philipp F. Hach, Gaute Lavik, Daan R. Speth, Carsten Schubert, Marcel M.M. Kuypers, and Jana Milucka. Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49602-5, doi:10.1038/s41467-024-49602-5. This article has 69 citations and is from a highest quality peer-reviewed journal.

17. (dinh2024towardtheuse pages 4-5): Thuc-Anh Dinh and Kylie D. Allen. Toward the use of methyl-coenzyme m reductase for methane bioconversion applications. Accounts of Chemical Research, 57:2746-2757, Aug 2024. URL: https://doi.org/10.1021/acs.accounts.4c00413, doi:10.1021/acs.accounts.4c00413. This article has 18 citations and is from a domain leading peer-reviewed journal.

18. (sina2024persistentactivityof pages 2-3): Sina Schorn, Jon S. Graf, Sten Littmann, Philipp F. Hach, Gaute Lavik, Daan R. Speth, Carsten Schubert, Marcel M.M. Kuypers, and Jana Milucka. Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49602-5, doi:10.1038/s41467-024-49602-5. This article has 69 citations and is from a highest quality peer-reviewed journal.

19. (sina2024persistentactivityof pages 3-4): Sina Schorn, Jon S. Graf, Sten Littmann, Philipp F. Hach, Gaute Lavik, Daan R. Speth, Carsten Schubert, Marcel M.M. Kuypers, and Jana Milucka. Persistent activity of aerobic methane-oxidizing bacteria in anoxic lake waters due to metabolic versatility. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49602-5, doi:10.1038/s41467-024-49602-5. This article has 69 citations and is from a highest quality peer-reviewed journal.

20. (wissink2024probingdenitrifyinganaerobic pages 2-3): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 21 citations and is from a domain leading peer-reviewed journal.

21. (wissink2024probingdenitrifyinganaerobic pages 3-4): Martijn Wissink, Martyna Glodowska, Marnix R. van der Kolk, Mike S. M. Jetten, and Cornelia U. Welte. Probing denitrifying anaerobic methane oxidation via antimicrobial intervention: implications for innovative wastewater management. Environmental Science & Technology, 58:6250-6257, Mar 2024. URL: https://doi.org/10.1021/acs.est.3c07197, doi:10.1021/acs.est.3c07197. This article has 21 citations and is from a domain leading peer-reviewed journal.

22. (ouboter2024mechanismsofextracellular pages 5-10): Heleen T Ouboter, Rob Mesman, Tom Sleutels, Jelle Postma, Martijn Wissink, Mike S M Jetten, Annemiek ter Heijne, Tom Berben, and Cornelia U Welte. Mechanisms of extracellular electron transfer in anaerobic methanotrophic archaea. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2023.07.24.550278, doi:10.1101/2023.07.24.550278. This article has 73 citations.

23. (samanta2024fromgenometo pages 12-14): Dipayan Samanta, Shailabh Rauniyar, Priya Saxena, and Rajesh K. Sani. From genome to evolution: investigating type ii methylotrophs using a pangenomic analysis. Jun 2024. URL: https://doi.org/10.1128/msystems.00248-24, doi:10.1128/msystems.00248-24. This article has 11 citations and is from a peer-reviewed journal.