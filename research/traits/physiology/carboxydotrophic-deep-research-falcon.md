---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:41:37.246194'
end_time: '2026-08-04T10:47:45.838424'
duration_seconds: 368.59
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: carboxydotrophic
  trait_identifier: METPO:1000633
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: carboxydotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism derives energy from the oxidation
    of carbon monoxide.
  parent_traits: METPO:1000631
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth
    and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.)
    | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase
    (Review supports CODH and CO-insensitive respiratory-chain features in aerobic
    carboxydotrophs.)'
  causal_graph_summary: 'carboxydotrophic_co_oxidation: 18 nodes, 16 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxydotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000633
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism derives energy from the oxidation of carbon monoxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.) | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase (Review supports CODH and CO-insensitive respiratory-chain features in aerobic carboxydotrophs.)
- **Existing causal graph summary:** carboxydotrophic_co_oxidation: 18 nodes, 16 edges

## Research Objective

Research the microbial trait **carboxydotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/carboxydotrophic.yaml`.

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
- **Trait label:** carboxydotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000633
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism derives energy from the oxidation of carbon monoxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.) | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase (Review supports CODH and CO-insensitive respiratory-chain features in aerobic carboxydotrophs.)
- **Existing causal graph summary:** carboxydotrophic_co_oxidation: 18 nodes, 16 edges

## Research Objective

Research the microbial trait **carboxydotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/carboxydotrophic.yaml`.

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


# Curation-focused research report: carboxydotrophic

**Target trait:** `METPO:1000633`  
**Category:** PHYSIOLOGY | **Term kind:** CLASS | **Mapping:** REVIEWED  
**Proposed operational meaning:** an organism conserves energy from oxidation of carbon monoxide (CO), whether coupled to aerobic respiration, anaerobic respiration, hydrogenogenesis, acetogenesis, or another experimentally demonstrated energy-conserving process.

## 1. Scope and boundaries

The chemically invariant core is:

**CO + H₂O → CO₂ + 2H⁺ + 2e⁻**, catalyzed by carbon monoxide dehydrogenase (CODH). The released electrons must feed an energy-conserving system for the phenotype to qualify under the supplied definition. Aerobic organisms commonly couple CO oxidation to O₂ reduction; anaerobes can couple it to H₂ evolution, acetogenesis, methanogenesis, or anaerobic respiration. The enzyme families differ substantially: aerobic CODHs are generally Mo,Cu-containing CoxLMS enzymes, whereas anaerobic CODHs are Ni,Fe,S enzymes that may be monofunctional or associated with acetyl-CoA synthase (ACS). (bahrle2023currentstatusof pages 5-8, oelgeschlager2008carbonmonoxidedependentenergy pages 1-2, svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2)

### Recommended inclusion rule

Curate `METPO:1000633` when at least one of the following is demonstrated:

1. growth with CO as an energy source;
2. CO-dependent ATP generation, ion-gradient formation, respiration, or H₂ evolution;
3. CO-dependent production of reduced electron carriers connected experimentally to energy conservation;
4. a complete mechanistic chain from CODH-catalyzed CO oxidation to a respiratory or chemiosmotic module.

CO need not be the sole carbon source. Strict “growth on CO as sole carbon and energy source” is a particularly strong assay, but it is narrower than the supplied ontology definition.

### Boundary cases

- **Carboxydovory:** some organisms oxidize low or atmospheric CO to support maintenance or respiration without fixing CO-derived CO₂ or growing autotrophically. This overlaps the supplied energy-based definition but is distinguished in the literature from classical carboxydotrophy. Represent it as a narrower assay/context rather than requiring carbon fixation in every carboxydotroph. (bahrle2023currentstatusof pages 5-8)
- **CODH gene presence alone:** not sufficient. Approximately 6% of surveyed microbial genomes were estimated to encode at least one Ni,Fe-CODH gene, but homologs may serve reversible CO₂ reduction, acetyl-CoA metabolism, or backup energy metabolism; genomic presence is therefore predictive rather than phenotypic evidence. (bahrle2023currentstatusof pages 5-8)
- **CODH/ACS-dependent carbonyl synthesis:** production and channeling of CO as an internal Wood–Ljungdahl-pathway intermediate is not necessarily energy derivation from exogenous CO.
- **CO production:** composting, heme degradation, or other CO-generating processes are outside scope unless the same organism also oxidizes CO for energy.
- **Community-level CO conversion:** a consortium may be carboxydotrophic while the responsible organism remains unresolved. Do not assign the phenotype to every community member.
- **Methanogenesis, acetogenesis, or dechlorination supported indirectly by H₂/acetate:** downstream consumers are not themselves carboxydotrophs unless direct CO oxidation is shown.

## 2. Candidate graph nodes

Identifiers below are deliberately conservative. Labels are retained where an exact ontology term was not verified.

### Trait and processes

- `METPO:1000633` — carboxydotrophic
- `METPO:1000631` — supplied parent trait
- CO oxidation / carbon-monoxide dehydrogenase reaction
- aerobic respiration
- anaerobic respiration
- hydrogenogenesis / water–gas-shift metabolism
- acetogenesis
- methanogenesis
- Calvin–Benson–Bassham (CBB) cycle
- Wood–Ljungdahl pathway (reductive acetyl-CoA pathway)
- proton- or sodium-motive-force generation
- ATP synthesis
- autotrophic growth
- reductive dechlorination — downstream community application, not part of the core trait

### Chemicals and electron carriers

- `CHEBI:17245` — carbon monoxide
- `CHEBI:16526` — carbon dioxide
- `CHEBI:15377` — water
- `CHEBI:15378` — proton
- `CHEBI:15379` — dioxygen
- `CHEBI:18276` — dihydrogen
- acetate; acetyl-CoA; coenzyme A
- nitrate — alternative acceptor reported for some aerobic-type CO respiratory chains
- quinone/ubiquinone
- oxidized and reduced ferredoxin
- NAD⁺/NADH and NADP⁺/NADPH
- sodium ion
- trichloroethene, vinyl chloride, and ethene — application-specific
- acetic acid/undissociated acetate and Na⁺ — experimental modifiers/inhibitors

### Genes, proteins, enzymes, and complexes

- carbon monoxide dehydrogenase — candidate `EC:1.2.5.3`; verify the database/version-specific EC representation before YAML insertion
- **CoxL** — large catalytic subunit containing the Mo,Cu active site
- **CoxM** — FAD-containing medium subunit
- **CoxS** — small Fe–S subunit
- Mo,Cu-CODH `(CoxLMS)₂` complex
- Ni,Fe,S-CODH / **CooS**
- **CooF** ferredoxin-like electron-transfer protein
- **CooA** heme CO sensor/transcriptional regulator
- energy-converting hydrogenase (**EcH/Ech**)
- CODH/acetyl-CoA synthase complex
- corrinoid iron–sulfur protein (**CFeSP**)
- Rnf complex (`rnfCDEAB`)
- respiratory complex I, cytochrome bc complex III, cytochrome-c oxidase, cytochrome-bd quinol oxidase
- F₀F₁ ATP synthase
- RubisCO and phosphoribulokinase
- CO-insensitive/high-O₂-affinity terminal oxidase — label-only pending exact taxon-specific identity

Aerobic Mo,Cu-CODH is a dimer of CoxLMS heterotrimers: CoxL carries the Mo,Cu catalytic site, CoxM contains FAD, and CoxS carries Fe–S clusters. Anaerobic Ni,Fe,S-CODHs include bifunctional CODH/ACS and monofunctional enzymes; these classes should not be collapsed into one protein-complex node. (bahrle2023currentstatusof pages 5-8, svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2)

### Cellular locations

- cytoplasm
- cytoplasmic membrane, inner/cytoplasmic face
- respiratory membrane
- hydrophobic intracomplex CO tunnel in CODH/ACS

In *Carboxydothermus hydrogenoformans*, more than 92% of CODH I and II in intact CO-grown cells was associated with the inner aspect of the cytoplasmic membrane, although about 70% became soluble after cell disruption, indicating weak noncovalent membrane association. (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9)

### Representative taxa and environments

- *Oligotropha carboxidovorans* — canonical aerobic CBB-coupled carboxydotroph
- *Carboxydochorda subterranea* strain L945ᵀ — aerobic thermophilic carboxydotroph isolated from a deep subsurface aquifer
- *Carboxydothermus hydrogenoformans* — anaerobic thermophilic hydrogenogen
- *Rhodospirillum rubrum* — CO-responsive CooA/CooFS/EcH model
- *Acetobacterium woodii* and *Moorella thermoacetica* — mechanistically distinct acetogens
- *Clostridium autoethanogenum*, *C. ljungdahlii*, and *C. carboxidivorans* — syngas-fermentation organisms
- *Acetobacterium* strain Z1 and *Dehalococcoides* — consortium-specific CO-driven dechlorination
- deep terrestrial aquifer; volcanic hot spring; hydrothermal systems; anaerobic sludge/bioreactor; syngas-fermentation reactor

## 3. Evidence-backed causal edges

The strongest compact edge scaffold is shown first.

| subject | predicate | object | scope (aerobic/anaobic/taxon/community) | evidence strength | DOI |
|---|---|---|---|---|---|
| carbon monoxide (CHEBI:17245) | is oxidized by | carbon monoxide dehydrogenase (CODH; EC 1.2.99.2 / EC 1.2.7.4) | aerobic + anaerobic | strong | 10.1007/s00203-008-0382-6 (oelgeschlager2008carbonmonoxidedependentenergy pages 1-2) |
| aerobic Mo,Cu-CODH (CoxLMS complex) | transfers electrons to | quinone or cytochrome b complex | aerobic | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9) |
| electron transfer from aerobic CODH | enables | O2 reduction by respiratory chain | aerobic | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| electron transfer from aerobic CODH | generates | proton motive force / motive force | aerobic | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| proton motive force / motive force | drives | ATP synthesis | aerobic | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| CO oxidation-derived CO2 | is assimilated via | Calvin-Benson-Bassham cycle | aerobic carboxydotroph | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| ribulose-1,5-bisphosphate carboxylase/oxygenase (RubisCO) + phosphoribulokinase | enable | autotrophic CO2 fixation in Carboxydochorda subterranea L945T | taxon-specific aerobic | strong | 10.3389/fmicb.2024.1441865 (karnachuk2024novelthermophilicgenera pages 8-10, karnachuk2024novelthermophilicgenera pages 5-8) |
| Carboxydochorda subterranea L945T | uses electron donor | carbon monoxide | taxon-specific aerobic | strong | 10.3389/fmicb.2024.1441865 (karnachuk2024novelthermophilicgenera pages 8-10) |
| Carboxydochorda subterranea L945T | uses electron acceptor | oxygen | taxon-specific aerobic | strong | 10.3389/fmicb.2024.1441865 (karnachuk2024novelthermophilicgenera pages 8-10) |
| anaerobic Ni,Fe-S CODH | reduces | ferredoxin | anaerobic acetogen/hydrogenogen | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| reduced ferredoxin | donates electrons via | Rnf complex | anaerobic acetogen | moderate | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| Rnf complex | generates | transmembrane Na+ ion gradient | anaerobic acetogen | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| transmembrane ion gradient | drives | ATP synthesis | anaerobic acetogen | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| Ni,Fe-S CODH | transfers electrons via | CooF iron-sulfur protein | anaerobic hydrogenogen (Rhodospirillum rubrum model) | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| CooF-mediated electron transfer | fuels | energy-converting hydrogenase (EcH) | anaerobic hydrogenogen (Rhodospirillum rubrum model) | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| energy-converting hydrogenase (EcH) | produces | H2 | anaerobic hydrogenogen | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| hydrogenogenic CO oxidation | generates | H2 + CO2 | anaerobic | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| Wood-Ljungdahl pathway | converts | CO/CO2 to acetyl-CoA | anaerobic acetogen | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| acetyl-CoA | is converted to | acetate | anaerobic acetogen | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| CooA | positively regulates transcription of | CO oxidation / CO-induced hydrogenase machinery | anaerobic hydrogenogen (Rhodospirillum rubrum model) | strong | 10.1186/s40643-023-00705-9 (bahrle2023currentstatusof pages 8-9) |
| CODH I and CODH II | localize to | inner aspect of cytoplasmic membrane | taxon-specific anaerobic (Carboxydothermus hydrogenoformans) | strong | 10.1128/JB.183.17.5134-5144.2001 (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9, svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2) |
| CODH I + protein B (ferredoxin-like fraction) | promote | CO-dependent H2 evolution | taxon-specific anaerobic (Carboxydothermus hydrogenoformans) | strong | 10.1128/JB.183.17.5134-5144.2001 (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9) |
| CO oxidation by Acetobacterium in consortium | produces | H2 + acetate | community | moderate | 10.1186/s40168-024-01869-y (wang2024codrivenelectronand pages 7-8) |
| H2 + acetate from CO oxidation | supports | Dehalococcoides reductive dechlorination of TCE to ethene | community | moderate | 10.1186/s40168-024-01869-y (wang2024codrivenelectronand pages 7-8) |
| acetate supplementation | increases | carboxydotrophic CO conversion rates | community | moderate | 10.1111/1751-7915.70063 (robazza2024acetateshockloads pages 1-2, robazza2024acetateshockloads pages 11-12) |
| high undissociated acetic acid / Na+ | inhibits earlier than carboxydotrophy | methanogenesis | community | moderate | 10.1111/1751-7915.70063 (robazza2024acetateshockloads pages 11-12) |


*Table: This table lists compact, curation-ready candidate causal edges for the trait carboxydotrophic (METPO:1000633), emphasizing the strongest mechanistic relationships and selected 2024 taxon/community findings. It is useful as a starting scaffold for TraitMech YAML curation because it separates broadly supported core edges from narrower taxon- or consortium-specific ones.*

### Edge evidence, snippets, and curation notes

| Candidate triple | Supporting snippet | Reference | Curation note |
|---|---|---|---|
| CO — **is oxidized by** → CODH | “Both enzymes catalyze the reaction CO + H₂O → CO₂ + 2e⁻ + 2H⁺.” | Svetlitchnyi et al., 2001 | **Core, strong.** Direct enzyme evidence. (svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2) |
| Mo,Cu-CODH — **comprises** → CoxL, CoxM, CoxS | “large subunit containing Mo,Cu active site… medium FAD containing… small iron–sulfur subunit.” | Bährle et al., 2023 | **Aerobic module, strong.** Do not apply to anaerobic CODHs. (bahrle2023currentstatusof pages 5-8) |
| aerobic CODH — **transfers electrons to** → quinone/cytochrome-b complex | Electrons and protons “are accepted by a cytochrome b complex or a quinone.” | Bährle et al., 2023 | **Strong review-supported edge.** Exact carrier may be taxon-specific. (bahrle2023currentstatusof pages 8-9) |
| respiratory electron transfer — **enables** → O₂ reduction | Quinone/cytochrome-b transfer “can then… lead to O₂ reduction.” | Bährle et al., 2023 | **Strong aerobic edge.** Nitrate is an alternative in some organisms, not universal. (bahrle2023currentstatusof pages 8-9) |
| aerobic CO respiration — **generates** → motive force — **drives** → ATP synthesis | “The motive force resulting from this process is then used to generate ATP.” | Bährle et al., 2023 | **Core aerobic energy-conservation chain.** (bahrle2023currentstatusof pages 8-9) |
| CO oxidation-derived CO₂ — **is assimilated through** → CBB cycle | “CO₂… generated by CO oxidation is then assimilated within the CBB cycle via the RubisCO.” | Bährle et al., 2023 | **Common but not definitionally universal.** Suitable for an aerobic-autotrophic branch. (bahrle2023currentstatusof pages 8-9) |
| CO — **serves as electron donor for** → aerobic respiration in *C. subterranea* | “H₂, CO, and formate are used as electron donors for aerobic respiration.” | Karnachuk et al., 2024 | **Strong, taxon-specific phenotype.** (karnachuk2024novelthermophilicgenera pages 8-10) |
| RubisCO + phosphoribulokinase — **enable** → CBB fixation in *C. subterranea* | “key genes… including ribulose bisphosphate carboxylase and phosphoribulokinase”; WLP was absent. | Karnachuk et al., 2024 | **Strong genomic-plus-physiological support.** Keep strain scoped. (karnachuk2024novelthermophilicgenera pages 8-10, karnachuk2024novelthermophilicgenera pages 5-8) |
| CODH — **reduces** → ferredoxin | “A. woodii oxidizes CO by its CODH, whereby ferredoxin is reduced.” | Bährle et al., 2023 | **Taxon/module-specific**, not universal to all CODHs. (bahrle2023currentstatusof pages 8-9) |
| reduced ferredoxin — **is reoxidized by** → Rnf — **causes** → Na⁺ translocation | Rnf “links… re-oxidation of ferredoxin to reduction of NAD⁺… [and] transmembrane Na⁺ translocation.” | Bährle et al., 2023 | **Strong for Rnf-type acetogens**, especially *A. woodii*. (bahrle2023currentstatusof pages 8-9) |
| ion gradient — **drives** → ATP synthesis | CO metabolism through the WLP forms “an ion motive force, which results in ATP synthesis.” | Bährle et al., 2023 | **Strong anaerobic acetogenic edge.** Gradient may be H⁺ or Na⁺ depending on organism. (bahrle2023currentstatusof pages 8-9) |
| CODH/ACS — **condenses** → methyl group + carbonyl group + CoA into acetyl-CoA | CODH/ACS “catalyzes the condensation… to acetyl-CoA, which is further converted to acetate.” | Bährle et al., 2023 | **Strong WLP branch.** Distinguish exogenous CO oxidation from internally generated CO. (bahrle2023currentstatusof pages 8-9) |
| Ni,Fe-CODH — **transfers electrons through** → CooF — **to** → EcH | Electrons “are shuttled through… CooF… to the EcH.” | Bährle et al., 2023 | **Strong in the *R. rubrum* model; taxon-specific.** (bahrle2023currentstatusof pages 8-9) |
| EcH-mediated proton reduction — **produces** → H₂ and ion gradient | CO oxidation can be coupled to “H₂ production and the formation of transmembrane electrochemical ion gradients.” | Bährle et al., 2023 | **Strong hydrogenogenic module.** (bahrle2023currentstatusof pages 8-9) |
| CooA — **activates transcription of** → CO-utilization machinery | CooA functions “as a CO sensor… controlling the transcription of the enzymatic machinery needed for chemoautotrophic growth.” | Bährle et al., 2023 | **Strong, *R. rubrum*-specific regulation.** (bahrle2023currentstatusof pages 8-9) |
| CODH I + ferredoxin-like protein B — **promote** → CO-dependent H₂ evolution | “H₂ evolution increased considerably when both CODH I and protein B were present.” | Svetlitchnyi et al., 2001 | **Strong biochemical edge**, but “protein B” was not molecularly resolved. (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9) |
| CO oxidation by consortium/*Acetobacterium* — **supplies** → H₂ + acetate — **support** → *Dehalococcoides* dechlorination | CO oxidation generated H₂/acetate subsequently used for TCE-to-ethene dechlorination. | Wang et al., 2024 | **Community/application edge; moderate.** Avoid assigning all steps to one organism. (wang2024codrivenelectronand pages 7-8) |
| acetate supplementation — **increases** → community CO conversion | Rates increased “up to about 20-fold” at pH 5.5, 55°C, and 48 g/L acetate. | Robazza et al., 2024 | **Assay-specific and community-level.** Acetate supplies additional energy/carbon; it is not a universal activator. (robazza2024acetateshockloads pages 1-2) |
| high acetate/Na⁺ — **inhibits** → CO uptake | At 40 g/L acetate and pH 6.7, mesophilic and thermophilic CO uptake fell approximately 20% and 70%. | Robazza et al., 2024 | **Context-dependent inhibition.** Separate undissociated-acid and sodium effects where possible. (robazza2024acetateshockloads pages 11-12) |

## 4. Recent developments and quantitative evidence

### 2023 mechanistic synthesis

A 2023 CODH review consolidated the present structural division between aerobic Mo,Cu-CODHs and anaerobic Ni,Fe-CODHs and highlighted electrochemical CO₂/CO interconversion as an emerging application. It reports aerobic CO oxidation as highly exergonic—`2 CO + O₂ → 2 CO₂`, ΔG°′ approximately −514 kJ mol⁻¹ CO—and hydrogenogenic oxidation as `CO + H₂O ⇌ CO₂ + H₂`, ΔG°′ approximately −20 kJ mol⁻¹ CO. The review’s expert assessment is that uncultured microorganisms probably contain substantial unexplored CODH diversity and that identifying these enzymes should be a major research priority. (bahrle2023currentstatusof pages 5-8, bahrle2023currentstatusof pages 8-9)

### 2024 aerobic deep-biosphere isolate

Karnachuk et al. described *Carboxydochorda subterranea* L945ᵀ, a thermophile from a Western Siberian deep aquifer. It grows from 37–60°C, optimally at 55°C, and at pH 6.5–9.0, optimally 7.0–7.5. Physiological tests showed CO as an electron donor for aerobic respiration; genomic analysis identified aerobic CODH genes, RubisCO, phosphoribulokinase, complete respiratory-chain components, and F₀F₁ ATPase. The WLP was absent, supporting a CBB—not acetyl-CoA-pathway—assimilation branch. This provides a strong modern example of aerobic carboxydotrophy in the nutrient-limited deep biosphere. (karnachuk2024novelthermophilicgenera pages 8-10, karnachuk2024novelthermophilicgenera pages 5-8)

### 2024 CO-driven bioremediation consortium

In a CO-fed dechlorinating consortium, 5 mL CO dosing was associated with a 416.9-fold increase in *Dehalococcoides*, from `3.6 × 10⁵` to `1.5 × 10⁸ cells mL⁻¹`; acetate reached `4.4 ± 0.4 mM`, and H₂ accumulation during vinyl-chloride-to-ethene conversion reached `631.8 ± 172.5 nmol bottle⁻¹`. The proposed division of labor is CO conversion by an *Acetobacterium*-associated WLP module, followed by use of H₂ and acetate by *Dehalococcoides*. This supports CO-driven reductive dechlorination as a real-world bioremediation concept, but the causal edges are consortium-specific. (wang2024codrivenelectronand pages 7-8)

### 2024 mixed-culture process control

Anaerobic microbiomes converted syngas at acetate concentrations up to `64 g L⁻¹` and pH 5.5. Acetate supplementation increased CO-conversion rates by as much as approximately 20-fold under one tested condition—pH 5.5, 55°C, 48 g/L acetate—but high acetate also shifted product profiles and inhibited methanogenesis. At pH 6.7, 40 g/L acetate reduced CO uptake by about 20% at 37°C and 70% at 55°C. Thus, acetate is simultaneously cosubstrate and stressor; pH, temperature, sodium, and undissociated acetic acid determine the net effect. (robazza2024acetateshockloads pages 1-2, robazza2024acetateshockloads pages 11-12)

### Foundational enzyme kinetics

Purified *C. hydrogenoformans* CODH I and II displayed specific activities of `15,756` and `13,828 µmol CO min⁻¹ mg⁻¹ protein` at pH 8.0 and 70°C with methyl viologen. Their apparent Kₘ values were `30` and `18 µM CO`, and catalytic efficiencies were `1.3 × 10⁹` and `1.7 × 10⁹ M⁻¹ s⁻¹`, respectively. These values establish exceptionally efficient CO oxidation but come from an artificial electron-acceptor assay and should not be represented as in vivo flux. (svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2)

## 5. Applications and implementations

1. **Syngas and waste-gas fermentation:** acetogenic carboxydotrophs convert CO/CO₂/H₂ into acetate, ethanol, butanol, and other products. Principal engineering constraints include gas–liquid mass transfer, variable syngas composition, contaminants, CO toxicity, redox balance, and product inhibition. (sobieraj2023biologicaltreatmentof pages 5-6, sobieraj2023biologicaltreatmentof pages 3-5, robazza2024acetateshockloads pages 1-2)
2. **Biological hydrogen production:** hydrogenogenic organisms couple CO oxidation to proton reduction through CODH–electron-transfer-protein–EcH systems. (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9, svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2, bahrle2023currentstatusof pages 8-9)
3. **Biomethanation:** CO can feed methanogenesis directly in some organisms or, commonly in mixed cultures, indirectly through acetate, H₂, and CO₂. Community route attribution requires inhibitor, isotope, transcriptomic, or isolate-level evidence. (sobieraj2023biologicaltreatmentof pages 5-6, sobieraj2023biologicaltreatmentof pages 3-5)
4. **Bioremediation:** CO-derived H₂ and acetate can sustain organohalide-respiring populations and TCE dechlorination. (wang2024codrivenelectronand pages 7-8)
5. **Enzymatic/electrochemical catalysis:** reversible CODHs are being investigated for CO₂-to-CO and CO-oxidation electrodes. This is an enzyme application rather than evidence that an engineered device possesses the microbial trait. (bahrle2023currentstatusof pages 8-9, bahrle2023currentstatusof pages 5-8)
6. **Deep-biosphere ecology and atmospheric CO sinks:** aerobic and anaerobic CO oxidation provide supplementary energy in oligotrophic environments, but genomic prediction should be distinguished from measured growth or flux. (karnachuk2024novelthermophilicgenera pages 8-10, karnachuk2024novelthermophilicgenera pages 5-8, bahrle2023currentstatusof pages 5-8)

## 6. Recommended TraitMech graph architecture

Rather than one linear 18-node graph, use a shared core followed by mutually scoped branches:

- **Core:** CO → CODH-catalyzed oxidation → CO₂ + reducing equivalents.
- **Aerobic respiratory branch:** Mo,Cu-CODH/CoxLMS → quinone or cytochrome b → terminal oxidase/O₂ → motive force → ATP.
- **Aerobic autotrophic branch:** CO-derived CO₂ → RubisCO/CBB cycle → biomass.
- **Anaerobic hydrogenogenic branch:** Ni,Fe-CODH → CooF/ferredoxin → EcH → H₂ + ion gradient → ATP.
- **Anaerobic acetogenic branch:** Ni,Fe-CODH/CODH-ACS + CFeSP/WLP → acetyl-CoA → acetate; Rnf or EcH provides organism-specific chemiosmotic coupling.
- **Regulatory branch:** CO → CooA → transcription of `coo` machinery, restricted to supported taxa.
- **Context/application branch:** products such as H₂ and acetate → syntrophic consumers or bioprocess outputs; keep outside the defining trait core.

This architecture prevents the biologically incorrect implication that every carboxydotroph has both Mo,Cu- and Ni,Fe-CODH, fixes carbon through both CBB and WLP, or produces H₂, acetate, and methane simultaneously.

## 7. Warnings: claims not yet suitable for unqualified curation

- Do **not** make carbon fixation obligatory: the supplied definition concerns energy derivation, and carboxydovorous CO oxidation may support respiration without autotrophic growth.
- Do **not** infer phenotype solely from `coxL`, `cooS`, or another CODH-like sequence. Catalytic motifs, gene neighborhood, expression, and physiological evidence are needed.
- Do **not** use “CO tolerance,” growth in a CO-containing headspace, or CO consumption by a community as proof that a named isolate is carboxydotrophic.
- Do **not** merge Mo,Cu-CODH and Ni,Fe,S-CODH into a single mechanistic complex.
- Do **not** generalize CooA–CooF–EcH regulation from *R. rubrum*, Rnf-dependent Na⁺ translocation from *A. woodii*, or the two membrane-associated CODHs from *C. hydrogenoformans* to all taxa.
- Do **not** curate the CODH/ACS hydrophobic tunnel as a universal cellular CO-detoxification mechanism; it applies to bifunctional complexes and primarily channels an internal intermediate. (bahrle2023currentstatusof pages 5-8)
- Treat nitrate reduction by an aerobic-type CO respiratory chain as taxon-specific until direct organism-level evidence is attached.
- Treat the 20-fold acetate stimulation, 20–70% uptake inhibition, and dechlorination results as assay- or community-specific, not universal trait edges. (wang2024codrivenelectronand pages 7-8, robazza2024acetateshockloads pages 1-2, robazza2024acetateshockloads pages 11-12)
- Enzyme activities measured with methyl viologen at 70°C should not be converted into organismal growth rates or environmental fluxes. (svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2)
- Exact CURIEs for CODH subclasses, hydrogenogenesis, Rnf, CooA, and some electron-transfer complexes should be verified against the ontology releases used by TraitMech; label-only nodes are safer than invented identifiers.

## DOI-first bibliography

1. Bährle R, Böhnke S, Englhard J, Bachmann J, Perner M. **Current status of carbon monoxide dehydrogenases (CODH) and their potential for electrochemical applications.** *Bioresources and Bioprocessing*. Published November 2023. DOI: [10.1186/s40643-023-00705-9](https://doi.org/10.1186/s40643-023-00705-9). (bahrle2023currentstatusof pages 8-9, bahrle2023currentstatusof pages 5-8)
2. Karnachuk OV et al. **Novel thermophilic genera Geochorda gen. nov. and Carboxydochorda gen. nov. from the deep terrestrial subsurface reveal the ecophysiological diversity in the class Limnochordia.** *Frontiers in Microbiology*. Published September 2024. DOI: [10.3389/fmicb.2024.1441865](https://doi.org/10.3389/fmicb.2024.1441865). (karnachuk2024novelthermophilicgenera pages 8-10, karnachuk2024novelthermophilicgenera pages 5-8)
3. Wang J et al. **CO-driven electron and carbon flux fuels synergistic microbial reductive dechlorination.** *Microbiome*. Published August 2024. DOI: [10.1186/s40168-024-01869-y](https://doi.org/10.1186/s40168-024-01869-y). (wang2024codrivenelectronand pages 7-8)
4. Robazza A et al. **Acetate Shock Loads Enhance CO Uptake Rates of Anaerobic Microbiomes.** *Microbial Biotechnology*. Received August 4, accepted November 18, published December 2024. DOI: [10.1111/1751-7915.70063](https://doi.org/10.1111/1751-7915.70063). (robazza2024acetateshockloads pages 1-2, robazza2024acetateshockloads pages 11-12)
5. Sobieraj K et al. **Biological treatment of biowaste as an innovative source of CO—the role of composting process.** *Frontiers in Bioengineering and Biotechnology*. Published February 2023. DOI: [10.3389/fbioe.2023.1126737](https://doi.org/10.3389/fbioe.2023.1126737). (sobieraj2023biologicaltreatmentof pages 5-6, sobieraj2023biologicaltreatmentof pages 3-5)
6. Svetlitchnyi V, Peschel C, Acker G, Meyer O. **Two Membrane-Associated NiFeS-Carbon Monoxide Dehydrogenases from the Anaerobic Carbon-Monoxide-Utilizing Eubacterium Carboxydothermus hydrogenoformans.** *Journal of Bacteriology*. Published September 2001. DOI: [10.1128/JB.183.17.5134-5144.2001](https://doi.org/10.1128/JB.183.17.5134-5144.2001). (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9, svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2)
7. Oelgeschläger E, Rother M. **Carbon monoxide-dependent energy metabolism in anaerobic bacteria and archaea.** *Archives of Microbiology*. Published June 2008. DOI: [10.1007/s00203-008-0382-6](https://doi.org/10.1007/s00203-008-0382-6). (oelgeschlager2008carbonmonoxidedependentenergy pages 1-2)
8. Meyer O, Jacobitz S, Krüger B. **Biochemistry and physiology of aerobic carbon monoxide-utilizing bacteria.** *FEMS Microbiology Letters*. Published 1986. DOI: [10.1111/j.1574-6968.1986.tb01858.x](https://doi.org/10.1111/j.1574-6968.1986.tb01858.x). Foundational existing evidence supplied with the trait record.

References

1. (bahrle2023currentstatusof pages 5-8): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 33 citations and is from a peer-reviewed journal.

2. (oelgeschlager2008carbonmonoxidedependentenergy pages 1-2): Ellen Oelgeschläger and Michael Rother. Carbon monoxide-dependent energy metabolism in anaerobic bacteria and archaea. Archives of Microbiology, 190:257-269, Jun 2008. URL: https://doi.org/10.1007/s00203-008-0382-6, doi:10.1007/s00203-008-0382-6. This article has 306 citations and is from a peer-reviewed journal.

3. (svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2): Vitali Svetlitchnyi, Christine Peschel, Georg Acker, and Ortwin Meyer. Two membrane-associated nifes-carbon monoxide dehydrogenases from the anaerobic carbon-monoxide-utilizing eubacteriumcarboxydothermus hydrogenoformans. Journal of Bacteriology, 183:5134-5144, Sep 2001. URL: https://doi.org/10.1128/jb.183.17.5134-5144.2001, doi:10.1128/jb.183.17.5134-5144.2001. This article has 285 citations and is from a peer-reviewed journal.

4. (svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9): Vitali Svetlitchnyi, Christine Peschel, Georg Acker, and Ortwin Meyer. Two membrane-associated nifes-carbon monoxide dehydrogenases from the anaerobic carbon-monoxide-utilizing eubacteriumcarboxydothermus hydrogenoformans. Journal of Bacteriology, 183:5134-5144, Sep 2001. URL: https://doi.org/10.1128/jb.183.17.5134-5144.2001, doi:10.1128/jb.183.17.5134-5144.2001. This article has 285 citations and is from a peer-reviewed journal.

5. (bahrle2023currentstatusof pages 8-9): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 33 citations and is from a peer-reviewed journal.

6. (karnachuk2024novelthermophilicgenera pages 8-10): Olga V. Karnachuk, Anastasia P. Lukina, Marat R. Avakyan, Vitaly V. Kadnikov, Shahjahon Begmatov, Alexey V. Beletsky, Ksenia G. Vlasova, Andrei A. Novikov, Viktoria A. Shcherbakova, Andrey V. Mardanov, and Nikolai V. Ravin. Novel thermophilic genera geochorda gen. nov. and carboxydochorda gen. nov. from the deep terrestrial subsurface reveal the ecophysiological diversity in the class limnochordia. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1441865, doi:10.3389/fmicb.2024.1441865. This article has 18 citations and is from a peer-reviewed journal.

7. (karnachuk2024novelthermophilicgenera pages 5-8): Olga V. Karnachuk, Anastasia P. Lukina, Marat R. Avakyan, Vitaly V. Kadnikov, Shahjahon Begmatov, Alexey V. Beletsky, Ksenia G. Vlasova, Andrei A. Novikov, Viktoria A. Shcherbakova, Andrey V. Mardanov, and Nikolai V. Ravin. Novel thermophilic genera geochorda gen. nov. and carboxydochorda gen. nov. from the deep terrestrial subsurface reveal the ecophysiological diversity in the class limnochordia. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1441865, doi:10.3389/fmicb.2024.1441865. This article has 18 citations and is from a peer-reviewed journal.

8. (wang2024codrivenelectronand pages 7-8): Jingjing Wang, Xiuying Li, Huijuan Jin, Shujing Yang, Lian Yu, Hongyan Wang, Siqi Huang, Hengyi Liao, Xuhao Wang, Jun Yan, and Yi Yang. Co-driven electron and carbon flux fuels synergistic microbial reductive dechlorination. Microbiome, Aug 2024. URL: https://doi.org/10.1186/s40168-024-01869-y, doi:10.1186/s40168-024-01869-y. This article has 12 citations and is from a highest quality peer-reviewed journal.

9. (robazza2024acetateshockloads pages 1-2): Alberto Robazza, Ada Raya i Garcia, Flávio C. F. Baleeiro, Sabine Kleinsteuber, and Anke Neumann. Acetate shock loads enhance co uptake rates of anaerobic microbiomes. Microbial Biotechnology, Dec 2024. URL: https://doi.org/10.1111/1751-7915.70063, doi:10.1111/1751-7915.70063. This article has 3 citations and is from a peer-reviewed journal.

10. (robazza2024acetateshockloads pages 11-12): Alberto Robazza, Ada Raya i Garcia, Flávio C. F. Baleeiro, Sabine Kleinsteuber, and Anke Neumann. Acetate shock loads enhance co uptake rates of anaerobic microbiomes. Microbial Biotechnology, Dec 2024. URL: https://doi.org/10.1111/1751-7915.70063, doi:10.1111/1751-7915.70063. This article has 3 citations and is from a peer-reviewed journal.

11. (sobieraj2023biologicaltreatmentof pages 5-6): Karolina Sobieraj, Sylwia Stegenta-Dąbrowska, Gang Luo, Jacek A. Koziel, and Andrzej Białowiec. Biological treatment of biowaste as an innovative source of co—the role of composting process. Frontiers in Bioengineering and Biotechnology, Feb 2023. URL: https://doi.org/10.3389/fbioe.2023.1126737, doi:10.3389/fbioe.2023.1126737. This article has 18 citations.

12. (sobieraj2023biologicaltreatmentof pages 3-5): Karolina Sobieraj, Sylwia Stegenta-Dąbrowska, Gang Luo, Jacek A. Koziel, and Andrzej Białowiec. Biological treatment of biowaste as an innovative source of co—the role of composting process. Frontiers in Bioengineering and Biotechnology, Feb 2023. URL: https://doi.org/10.3389/fbioe.2023.1126737, doi:10.3389/fbioe.2023.1126737. This article has 18 citations.