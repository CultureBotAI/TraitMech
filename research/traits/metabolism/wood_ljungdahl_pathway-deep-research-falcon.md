---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:09:21.838576'
end_time: '2026-08-04T07:16:43.601980'
duration_seconds: 441.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Wood-Ljungdahl pathway
  trait_identifier: traitmech:000022
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: wood_ljungdahl_pathway
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway (the reductive acetyl-CoA pathway)
    in which two molecules of CO2 are reduced and combined into acetyl-CoA. It is
    energetically efficient and used by acetogenic bacteria, methanogenic archaea,
    and some sulfate-reducing bacteria.
  parent_traits: traitmech:000019
  synonyms: reductive acetyl-CoA pathway
  evidence_summary: 'DOI:10.1016/j.bbapap.2008.08.012:  (Ragsdale & Pierce, "Acetogenesis
    and the Wood-Ljungdahl pathway of CO2 fixation", is the reference treatment of
    this reductive acetyl-CoA pathway.) | DOI:10.1128/AEM.02473-10:  (Berg review
    places the reductive acetyl-CoA (Wood-Ljungdahl) pathway among the recognized
    autotrophic carbon-fixation pathways.)'
  causal_graph_summary: 'wood_ljungdahl_reductive_acetyl_coa: 15 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Wood-Ljungdahl pathway
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000022
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive acetyl-CoA pathway) in which two molecules of CO2 are reduced and combined into acetyl-CoA. It is energetically efficient and used by acetogenic bacteria, methanogenic archaea, and some sulfate-reducing bacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive acetyl-CoA pathway
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012:  (Ragsdale & Pierce, "Acetogenesis and the Wood-Ljungdahl pathway of CO2 fixation", is the reference treatment of this reductive acetyl-CoA pathway.) | DOI:10.1128/AEM.02473-10:  (Berg review places the reductive acetyl-CoA (Wood-Ljungdahl) pathway among the recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** wood_ljungdahl_reductive_acetyl_coa: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **Wood-Ljungdahl pathway** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/wood_ljungdahl_pathway.yaml`.

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
- **Trait label:** Wood-Ljungdahl pathway
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000022
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (the reductive acetyl-CoA pathway) in which two molecules of CO2 are reduced and combined into acetyl-CoA. It is energetically efficient and used by acetogenic bacteria, methanogenic archaea, and some sulfate-reducing bacteria.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive acetyl-CoA pathway
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012:  (Ragsdale & Pierce, "Acetogenesis and the Wood-Ljungdahl pathway of CO2 fixation", is the reference treatment of this reductive acetyl-CoA pathway.) | DOI:10.1128/AEM.02473-10:  (Berg review places the reductive acetyl-CoA (Wood-Ljungdahl) pathway among the recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** wood_ljungdahl_reductive_acetyl_coa: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **Wood-Ljungdahl pathway** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/wood_ljungdahl_pathway.yaml`.

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


# Curation report: Wood–Ljungdahl pathway

## Trait record and scope

- **Trait label:** Wood–Ljungdahl pathway
- **Trait identifier:** **`traitmech:000022`**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000019`
- **Synonym:** reductive acetyl-CoA pathway

### Recommended operational definition

For TraitMech, this trait should mean the **physiological capacity to operate the complete reductive Wood–Ljungdahl pathway (WLP)**: one C1 unit is reduced through a methyl branch, a second CO₂ is reduced to enzyme-bound CO in a carbonyl branch, and CODH/ACS combines the methyl group, CO, and CoA to produce acetyl-CoA. It is a linear, strictly anaerobic carbon-assimilation mechanism that may support both catabolism and anabolism. In acetogens, acetyl-CoA is commonly converted to acetate; acetate production itself, however, should not define pathway identity because methanogenic archaea and some sulfate-reducing bacteria use homologous modules in different physiological contexts. A 2023 experimental paper describes the pathway in strictly anaerobic acetogens, methanogens, and sulfate reducers and explicitly states that it forms acetyl-CoA from two CO₂ molecules. (moon2023anewmetabolic pages 1-2)

The defining graph endpoint should therefore be **acetyl-CoA formation**, not acetate, ethanol, growth, or autotrophy alone. Acetate formation and energy conservation are important downstream consequences in acetogens. Recent reviews describe more than 100 acetogenic species distributed across roughly 23–28 genera, with most isolates in Firmicutes/Bacillota but representatives also reported among Spirochaetes, Desulfobacterota, and Acidobacteria. The discrepancy in genus counts reflects source scope and taxonomy rather than a mechanistic difference. (frolov2023obligateautotrophyat pages 1-2, zhang2024engineeredacetogenicbacteria pages 1-2)

### Boundary cases

1. **Acetogenesis is not identical to WLP presence.** Acetogenesis is an organismal physiology in which acetate is a major reduced product; the WLP is the underlying carbon-fixation/acetyl-CoA module. Curate `produces acetate` as an acetogen-context consequence, not a universal defining edge. (zhang2024engineeredacetogenicbacteria pages 2-3, moon2023anewmetabolic pages 1-2)
2. **Methanogenesis is a nearby but distinct trait.** Methanogens can use the methyl branch or related WLP machinery, but carbon flow and terminal energy metabolism may lead to methane rather than acetate.
3. **Reverse/oxidative WLP is directionally distinct.** Some organisms oxidize acetyl-CoA through pathway homologues. Gene presence alone does not establish the reductive trait; directionality requires physiological, transcriptomic, flux, or thermodynamic evidence.
4. **Partial pathways are insufficient.** FDH, FolD, CODH, ACS-like proteins, or an incomplete methyl branch can participate in other C1 processes. A genome lacking branch convergence at functional CODH/ACS should be annotated as `partial WLP module`, not as the complete trait.
5. **Hydrogenogenic CO oxidation is distinct.** CODH-mediated CO oxidation coupled to H₂ evolution—the water–gas shift reaction—can occur without acetyl-CoA synthesis. The reported standard free-energy change is approximately −20 kJ mol⁻¹ CO. (bahrle2023currentstatusof pages 8-9)
6. **Reductive glycine metabolism is distinct.** It shares formate/THF chemistry but uses glycine-cleavage-system reactions rather than the canonical CFeSP–CODH/ACS convergence.
7. **Autotrophy alone is nonspecific.** Six other recognized CO₂-fixation routes exist, and heterotrophic or mixotrophic organisms can use the WLP as an electron sink.

## Current mechanistic understanding

The WLP has two converging branches. In the **methyl branch**, CO₂ is reduced to formate by FDH; in organisms such as *Acetobacterium woodii* and *Thermoanaerobacter kivui*, a hydrogen-dependent CO₂ reductase, HDCR, performs this reaction. Formate is ATP-dependently attached to tetrahydrofolate and then converted through methenyl-, methylene-, and methyl-THF. The methyl group is transferred to a corrinoid iron–sulfur protein (CFeSP). In the **carbonyl branch**, Ni,Fe-CODH reduces a second CO₂ to CO. Acetyl-CoA synthase receives the CFeSP methyl group and combines it with CO and CoA to form acetyl-CoA. (zhang2024engineeredacetogenicbacteria pages 2-3, moon2023anewmetabolic pages 1-2, bahrle2023currentstatusof pages 8-9, davin2024clostridiumautoethanogenumalters pages 1-2)

The pathway operates close to the energetic limit of life. Reported standard free energies for H₂/CO₂ acetogenesis are −95 to −104 kJ mol⁻¹ acetate, depending on reaction convention. The CO₂-to-CO step is a major thermodynamic barrier, with an approximate standard reduction potential of −520 mV and a requirement for low-potential electrons, commonly supplied by reduced ferredoxin. (moon2023anewmetabolic pages 1-2, frolov2023obligateautotrophyat pages 1-2)

Net energy conservation cannot be represented solely as substrate-level phosphorylation. Conversion of acetyl-CoA through phosphotransacetylase and acetate kinase generates ATP, but upstream formyl-THF synthesis consumes ATP. Acetogens consequently depend on chemiosmotic coupling. Rnf-type acetogens couple reduced-ferredoxin oxidation to NAD⁺ reduction and Na⁺ or H⁺ translocation; Ech-type acetogens use an energy-converting hydrogenase. The resulting ion gradient drives ATP synthase. Rnf and Ech are **alternative, taxon-dependent modules**, not universal components of the WLP. (zhang2024engineeredacetogenicbacteria pages 2-3, bahrle2023currentstatusof pages 8-9, frolov2023obligateautotrophyat pages 1-2)

## Candidate nodes and ontology grounding

Identifiers below are deliberately conservative. Where an exact stable identifier was not verified, a label-only node is preferable to an invented CURIE.

### Trait, pathway, and process nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Wood–Ljungdahl pathway | `traitmech:000022` | Root trait node; quote CURIE verbatim in YAML. |
| Methyl branch of WLP | Label only | Pathway module, not independently sufficient for trait assertion. |
| Carbonyl branch of WLP | Label only | Pathway module centered on CODH. |
| Anaerobic carbon fixation | GO label candidate | Verify exact GO term before import. |
| Acetogenesis | GO or METPO label candidate | Downstream physiology, not synonymous with WLP. |
| Chemiosmotic ATP synthesis | GO label candidate | Consequence of Rnf/Ech-generated gradient. |
| Autotrophic growth on H₂ + CO₂ | METPO label candidate | Assay phenotype supporting pathway operation. |
| Autotrophic growth on CO | METPO label candidate | Carboxydotrophic assay phenotype; not specific by itself. |

### Chemicals and cofactors

| Node | Suggested CURIE |
|---|---|
| carbon dioxide | `CHEBI:16526` |
| carbon monoxide | `CHEBI:17245` |
| formate | `CHEBI:15740` |
| hydrogen | `CHEBI:18276` |
| coenzyme A | `CHEBI:15346` |
| acetyl-CoA | `CHEBI:15351` |
| acetate | `CHEBI:30089` |
| pyruvate | `CHEBI:15361` |
| ATP | `CHEBI:15422` |
| ADP | `CHEBI:16761` |
| tetrahydrofolate | `CHEBI:15635` |
| 10-formyl-THF, 5,10-methenyl-THF, 5,10-methylene-THF, 5-methyl-THF | CHEBI candidates; verify exact protonation-specific records | Avoid mixing conjugate-acid and anion records within one reaction model. |
| oxidized/reduced ferredoxin | Label only unless protein-specific electron-carrier records are chosen | Ferredoxin identity differs among taxa. |
| NAD⁺/NADH and NADP⁺/NADPH | CHEBI candidates | Cofactor usage is enzyme- and taxon-specific. |
| sodium ion / proton | CHEBI candidates | Rnf coupling ion can vary. |

### Genes, proteins, enzymes, and complexes

| Candidate | Suggested grounding | Role and caveat |
|---|---|---|
| formate dehydrogenase | `EC:1.17.1.9` candidate | CO₂ → formate; exact EC depends on electron acceptor/donor specificity. |
| HDCR | Label only / complex-specific UniProt entries | H₂-dependent CO₂ reductase in selected acetogens; not universal. |
| formate–THF ligase (`fhs`) | `EC:6.3.4.3` | Formate + THF + ATP → 10-formyl-THF. |
| methenyl-THF cyclohydrolase (`folD`) | `EC:3.5.4.9` | Often bifunctional with methylene-THF dehydrogenase. |
| methylene-THF dehydrogenase (`folD`) | `EC:1.5.1.5` candidate | Cofactor specificity must be checked per organism. |
| methylene-THF reductase (`metF` or `metVF`) | `EC:1.5.1.20` candidate | Electron donor and subunit composition vary. |
| methyl-THF:CFeSP methyltransferase (`acsE`) | `EC:2.1.1.258` candidate | Transfers methyl group to CFeSP; verify EC in target schema. |
| corrinoid iron–sulfur protein (`acsCD`/`cdhDE`) | Label only or taxon-specific UniProt | Mobile methyl carrier. |
| anaerobic carbon monoxide dehydrogenase (`acsA`/`cdhA`) | `EC:1.2.7.4` candidate | Reversible CO₂/CO chemistry; paralogy makes gene-presence calls risky. |
| acetyl-CoA synthase (`acsB`/`cdhC`) | `EC:2.3.1.169` candidate | Condenses methyl, CO, and CoA. |
| CODH/ACS complex | Label only | Strongest signature of complete pathway when paired with methyl branch. |
| phosphotransacetylase (`pta`) | `EC:2.3.1.8` | Acetyl-CoA → acetyl phosphate. |
| acetate kinase (`ackA`) | `EC:2.7.2.1` | Acetyl phosphate → acetate + ATP. |
| electron-bifurcating [FeFe]-hydrogenase (`hydABC`) | Label only | Supplies reduced ferredoxin/NADH in selected taxa. |
| Rnf complex (`rnfABCDEG`) | GO/KEGG-module candidate | Ion-pumping ferredoxin:NAD oxidoreductase; taxon-specific. |
| Ech complex | GO/KEGG-module candidate | Energy-converting hydrogenase; taxon-specific alternative to Rnf. |
| ATP synthase | `GO:0045259` candidate | Converts ion motive force to ATP. |
| pyruvate:ferredoxin oxidoreductase | `EC:1.2.7.1` | Reverse reaction links acetyl-CoA to pyruvate biosynthesis. |

### Environmental and experimental nodes

- **Anoxic environment** — ENVO candidate; WLP enzymes and low-potential metal centers are generally oxygen sensitive.
- **CO₂/H₂ gas phase**, **CO-containing syngas**, and **industrial waste gas** — label nodes unless a suitable ENVO material term is verified.
- **H₂:CO uptake/feed ratio** — experimental-factor node, not an intrinsic pathway component.
- **pH, temperature, gas–liquid mass transfer, dissolved CO/H₂, acetate, and ethanol concentrations** — process modifiers. A 2024 kinetic review concluded that missing dissolved-gas measurements remain a major obstacle to predictive syngas-fermentation models; inhibition by acetate and ethanol is only partly resolved.
- **Nickel, iron, corrinoid/cobalt, folate, and selenium or tungsten/molybdenum availability** — plausible cofactor/environment nodes, but metal requirements must be assigned to specific enzyme forms rather than generalized across all WLP organisms.

## Candidate causal edges

The following table is a prioritized synopsis; detailed evidence notes follow it.

| Priority | subject | predicate | object | evidence strength/scope | primary DOI |
|---|---|---|---|---|---|
| High | Anaerobic H2 oxidation / electron-bifurcating hydrogenase | generates | reduced ferredoxin and NAD(P)H for WLP reduction steps | Strong for acetogens; taxon-specific modules differ; HydABC/related hydrogenases emphasized in thermophilic acetogens and acetogen reviews (frolov2023obligateautotrophyat pages 1-2, frolov2023obligateautotrophyat pages 8-9, zhang2024engineeredacetogenicbacteria pages 2-3) | 10.3389/fmicb.2023.1185739 |
| High | CO2 | reduced_by | formate dehydrogenase (FDH) / hydrogen-dependent CO2 reductase (HDCR) to formate | Strong for core WLP; HDCR explicitly taxon-specific (e.g., Acetobacterium woodii, Thermoanaerobacter kivui) (moon2023anewmetabolic pages 1-2, frolov2023obligateautotrophyat pages 8-9, zhang2024engineeredacetogenicbacteria pages 2-3) | 10.1111/1758-2229.13160 |
| High | Formate | converted_via | THF-bound C1 intermediates to methyl-THF | Strong pathway-level support across acetogen reviews; enzyme chain includes Fhs, FolD, MetF/MetVF-associated steps (zhang2024engineeredacetogenicbacteria pages 2-3, moon2023anewmetabolic pages 1-2, davin2024clostridiumautoethanogenumalters pages 1-2) | 10.3389/fbioe.2024.1395540 |
| High | Methyl-THF | transfers_methyl_to | corrinoid iron-sulfur protein (CFeSP) | Canonical mechanistic support; strongest from enzymology/structure reviews rather than recent genetics (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1021/cr400461p |
| High | Second CO2 | reduced_by | carbon monoxide dehydrogenase (CODH) to CO | Strong for carbonyl branch; low-potential ferredoxin requirement highlighted (bahrle2023currentstatusof pages 8-9, frolov2023obligateautotrophyat pages 1-2, davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s40643-023-00705-9 |
| High | CODH/ACS complex | condenses | methyl group + CO + CoA to form acetyl-CoA | Strong defining edge of complete WLP; central convergence step (moon2023anewmetabolic pages 1-2, bahrle2023currentstatusof pages 8-9, davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1111/1758-2229.13160 |
| High | Acetyl-CoA | converted_via | PTA/ACK to acetate with substrate-level ATP formation | Strong for acetogenic output phenotype, but note acetate is characteristic for acetogens rather than all WLP-bearing organisms (zhang2024engineeredacetogenicbacteria pages 2-3, moon2023anewmetabolic pages 1-2) | 10.3389/fbioe.2024.1395540 |
| High | Rnf complex | creates | Na+ ion gradient coupled to ATP synthase | Strong but taxon-specific; documented in A. woodii and some clostridia, not universal (bahrle2023currentstatusof pages 8-9, zhang2024engineeredacetogenicbacteria pages 2-3, frolov2023obligateautotrophyat pages 1-2) | 10.1186/s40643-023-00705-9 |
| High | Ech complex | creates | ion gradient coupled to ATP synthase | Strong but taxon-specific; emphasized for Moorella thermoacetica, Thermoanaerobacter kivui, and related Ech-acetogens (bahrle2023currentstatusof pages 8-9, frolov2023obligateautotrophyat pages 1-2) | 10.3389/fmicb.2023.1185739 |
| High | metVF deletion | blocks_growth_on | C1 compounds | Direct experimental evidence in A. woodii; strong but taxon-specific genotype→phenotype edge (moon2023anewmetabolic pages 1-2) | 10.1111/1758-2229.13160 |
| Medium | Acetyl-CoA + CO2 + reduced ferredoxin | converted_by | pyruvate:ferredoxin oxidoreductase (PFOR) to pyruvate | Strong for anabolic connection from WLP to central biosynthesis; not a defining WLP step itself (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1074/jbc.M003291200 |
| Context | Elevated H2:CO feed ratio (11:1) in chemostat | increases | fraction of ethanol carbon derived from CO2 to >=75% in Clostridium autoethanogenum | Recent application/context, not a defining trait edge; industrially relevant physiology (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s13068-024-02554-w |
| Context | Gas fermentation using WLP acetogens | implemented_with | industrial waste gases from steel mills, ferroalloy plants, and refineries | Real-world implementation context, not defining mechanism (davin2024clostridiumautoethanogenumalters pages 1-2) | 10.1186/s13068-024-02554-w |


*Table: This table prioritizes candidate causal edges for curating traitmech:000022, separating core defining Wood–Ljungdahl steps from taxon-specific energy modules and application-only context. It is useful as a compact checklist for what should be curated first into a causal graph.*

### Detailed evidence table

| Subject–predicate–object | Reference and date | Supporting snippet | Curation notes |
|---|---|---|---|
| CO₂ —`is_reduced_to`→ formate | DOI [10.1111/1758-2229.13160](https://doi.org/10.1111/1758-2229.13160), May 2023 | “the methyl branch reduces CO₂ to formate via formate dehydrogenase” | **Core edge.** HDCR is specifically supported for *A. woodii* and *T. kivui*; do not make HDCR universal. (moon2023anewmetabolic pages 1-2) |
| Formate —`is_converted_via`→ THF-bound C1 intermediates | DOI [10.3389/fbioe.2024.1395540](https://doi.org/10.3389/fbioe.2024.1395540), July 2024 | “formyl-THF synthetase → formyl-THF cyclohydrolase → methylene-THF dehydrogenase/reductase” | **Core module.** Represent individual reactions if the graph supports reaction granularity. Cofactor specificity needs taxon-level validation. (zhang2024engineeredacetogenicbacteria pages 2-3) |
| 5-methyl-THF —`donates_methyl_group_to`→ CFeSP | DOI [10.1186/s13068-024-02554-w](https://doi.org/10.1186/s13068-024-02554-w), September 2024 | methyl branch proceeds “to methylated cobalamin” | **Core edge**, supported at pathway level here and canonically by CODH/ACS enzymology. Prefer direct biochemical references for atom-level assertions. (davin2024clostridiumautoethanogenumalters pages 1-2) |
| second CO₂ —`is_reduced_to`→ CO | DOI [10.1186/s40643-023-00705-9](https://doi.org/10.1186/s40643-023-00705-9), November 2023 | carbonyl branch reduces “a second CO₂ to CO via CODH” | **Core edge.** CO may also enter directly from the environment. (bahrle2023currentstatusof pages 8-9) |
| reduced ferredoxin —`provides_electrons_for`→ CO₂-to-CO reduction | DOI [10.3389/fmicb.2023.1185739](https://doi.org/10.3389/fmicb.2023.1185739), May 2023 | carbonyl reduction has “E0′ = −520 mV,” requiring “low-potential ferredoxin” | **Core functional dependency**, although exact ferredoxin proteins differ. (frolov2023obligateautotrophyat pages 1-2) |
| CODH/ACS —`combines`→ methyl group + CO + CoA into acetyl-CoA | DOI [10.1111/1758-2229.13160](https://doi.org/10.1111/1758-2229.13160), May 2023 | “CO bound to the central enzyme CODH/ACS” converges with the methyl branch to acetyl-CoA | **Defining convergence edge.** Strong candidate for the graph’s central necessary mechanism. (moon2023anewmetabolic pages 1-2) |
| acetyl-CoA —`is_converted_by`→ PTA/ACK → acetate + ATP | DOI [10.3389/fbioe.2024.1395540](https://doi.org/10.3389/fbioe.2024.1395540), July 2024 | acetyl-CoA is converted “to acetate via PTA/ACK with net ATP yield” | **Acetogen-specific downstream edge.** More precisely, ATP is generated at ACK, while pathway-wide energy accounting includes ATP consumption at Fhs. (zhang2024engineeredacetogenicbacteria pages 2-3) |
| H₂ —`is_oxidized_by`→ hydrogenase → reducing equivalents | DOI [10.3389/fmicb.2023.1185739](https://doi.org/10.3389/fmicb.2023.1185739), May 2023 | HydABC transfers “electrons from H₂ to NAD⁺ and ferredoxin” | **Taxon-specific molecular implementation** but broadly relevant physiological input. (frolov2023obligateautotrophyat pages 8-9) |
| Rnf —`translocates`→ Na⁺ while coupling Fd oxidation to NAD⁺ reduction | DOI [10.1186/s40643-023-00705-9](https://doi.org/10.1186/s40643-023-00705-9), November 2023 | Rnf couples “ferredoxin oxidation to NAD⁺ reduction with Na⁺ translocation” | **Strong, taxon-specific.** Supported in *A. woodii* and several clostridial acetogens; not universal. (bahrle2023currentstatusof pages 8-9) |
| Ech —`generates`→ ion motive force | DOI [10.3389/fmicb.2023.1185739](https://doi.org/10.3389/fmicb.2023.1185739), May 2023 | acetogenic energy conservation uses “Rnf or Ech complexes” coupled to ATP synthase | **Strong, taxon-specific alternative** to Rnf. Avoid asserting both complexes for every organism. (frolov2023obligateautotrophyat pages 1-2) |
| ion motive force —`drives`→ ATP synthase | DOI [10.3389/fbioe.2024.1395540](https://doi.org/10.3389/fbioe.2024.1395540), July 2024 | Rnf and Ech are “coupled to ATP synthase via proton/sodium gradients” | **Core bioenergetic consequence** in energy-conserving acetogens, though ion identity varies. (zhang2024engineeredacetogenicbacteria pages 2-3) |
| `metVF` deletion —`abolishes`→ growth on C1 compounds | DOI [10.1111/1758-2229.13160](https://doi.org/10.1111/1758-2229.13160), May 2023 | “the mutant did not grow on C1 compounds” | **Direct genetic evidence in *A. woodii*.** Curate with taxon and assay context. The mutant also failed on lactate, ethanol, and butanediol but retained altered fructose growth. (moon2023anewmetabolic pages 1-2) |
| acetyl-CoA + CO₂ + reduced ferredoxin —`is_converted_by`→ PFOR → pyruvate | DOI [10.1074/jbc.M003291200](https://doi.org/10.1074/jbc.M003291200), September 2000 | PFOR is “a highly efficient pyruvate synthase” | **Downstream anabolic edge, not a defining WLP step.** Reported parameters include kcat 3.2 s⁻¹, Km acetyl-CoA 9 μM, and Km CO₂ 2 mM. |
| complete WLP —`supports`→ H₂/CO₂ acetogenic growth | DOI [10.3389/fmicb.2023.1185739](https://doi.org/10.3389/fmicb.2023.1185739), May 2023 | *Aceticella autotrophica* has complete encoding for chemolithoautotrophic acetogenic growth using hydrogen | **Strong organism-level experimental association.** Do not infer obligate autotrophy from WLP presence; this isolate’s obligate phenotype was additionally associated with loss of sugar transport/catabolism. (frolov2023obligateautotrophyat pages 8-9) |

## Recent developments, applications, and quantitative evidence

### 1. Genetic causality in *Acetobacterium woodii* (2023)

Deletion of `metVF`, encoding methylene-THF reductase subunits, eliminated growth on C1 compounds and on several reduced organic substrates. Fructose growth persisted at reduced rate and yield, and external electron sinks restored growth. This shows that the WLP can function as both a carbon-fixation route and an electron-balancing mechanism during heterotrophy; it also provides unusually strong genotype-to-trait evidence for `metVF` in this species. (moon2023anewmetabolic pages 1-2)

### 2. Obligate acetogenic autotrophy near the thermodynamic limit (2023)

*Aceticella autotrophica* strain 3443-3AcT was reported as the first obligately autotrophic acetogenic bacterium. It uses an Ech-type energy-conservation architecture and a hydrogen-dependent reductive pathway. Its obligate phenotype should not be attributed to WLP alone: comparative genomics associated it with missing sugar transporters and carbohydrate-catabolic enzymes. The study reports approximately −104 kJ mol⁻¹ for H₂/CO₂ acetogenesis and identifies the −520 mV CO₂/CO step as a central energetic barrier. (frolov2023obligateautotrophyat pages 1-2, frolov2023obligateautotrophyat pages 8-9)

### 3. High-H₂ gas fermentation and carbon capture (2024)

Controlled *Clostridium autoethanogenum* chemostats at an **11:1 H₂:CO uptake ratio** achieved conditions in which **at least 75% of ethanol carbon originated from CO₂**, compared with approximately **50%** at 5:1. WLP protein abundances remained relatively stable; changes in redox/cofactor metabolism and lysine acetylation suggested that post-translational regulation contributes to fine-tuning rather than wholesale pathway induction. The same paper identifies LanzaTech deployment of acetogenic gas fermentation on waste gases from steel mills, ferroalloy plants, and refineries. (davin2024clostridiumautoethanogenumalters pages 1-2)

### 4. Engineered acetogenic cell factories (2024)

A July 2024 review describes acetogens as platforms for converting CO, CO₂/H₂, syngas, and waste gases into acetate, ethanol, 2,3-butanediol, lactate, and engineered non-native products. Expert analysis emphasizes that expanding genetic tools is enabling product diversification, while redox balance, energy limitation, gas transfer, and strain-specific enzyme architecture remain key constraints. (zhang2024engineeredacetogenicbacteria pages 2-3, zhang2024engineeredacetogenicbacteria pages 1-2)

### 5. CODH engineering—promising but not yet curation-grade (December 2024 preprint)

A non-peer-reviewed bioRxiv study reported heterologous clostridial CODH expression in *E. coli*: CODH activity increased from **0.07 to 0.31 U mg⁻¹**, acetate from **2.4 to 7.8 g L⁻¹**, and ethanol reached **3.9 g L⁻¹** under one engineered condition. These data are application-relevant but should **not** establish that *E. coli* acquired a complete functional WLP: overexpressing CODH alone does not recreate the methyl branch, CFeSP, ACS convergence, or native acetogenic energy conservation. (tharak2024heterologousexpressionof pages 20-23)

### 6. Emerging environmental application

A 2024 microbiome study found that anaerobic CO metabolism produced H₂ and acetate that supported *Dehalococcoides*-mediated trichloroethene dechlorination; *Acetobacterium* also helped protect the dechlorinator from CO inhibition. This illustrates a community-level application in which WLP acetogens provide electron donor and carbon substrate to another functional guild. It is best represented in a separate ecological interaction graph, not as a defining edge of `traitmech:000022`.

## Expert interpretation

The literature supports treating CODH/ACS-mediated branch convergence as the most discriminating mechanistic center of the trait. FDH, FolD, MetF, hydrogenases, or CODH considered individually are poor diagnostic markers because each occurs in other metabolic contexts. Conversely, a genome containing a coherent methyl branch, CFeSP methyl-transfer machinery, and anaerobic CODH/ACS locus is strong genomic evidence, but still does not prove reductive direction or growth phenotype.

Energy conservation should be modeled as a **polymorphic subgraph**. The conserved pathway imposes a low-energy budget, but organisms solve it with different combinations of bifurcation, Rnf, Ech, soluble hydrogenases, and ion-coupled ATP synthases. A single graph requiring Rnf, Ech, HDCR, NADH, and NADPH simultaneously would incorrectly exclude valid taxa and create biologically impossible composite organisms. (zhang2024engineeredacetogenicbacteria pages 2-3, bahrle2023currentstatusof pages 8-9, frolov2023obligateautotrophyat pages 1-2)

## Warnings: claims not yet suitable for TraitMech curation

1. **Do not curate “WLP causes obligate autotrophy.”** The pathway permits autotrophy; obligacy depends on the rest of the metabolic network. (frolov2023obligateautotrophyat pages 8-9)
2. **Do not require acetate as the universal output.** Use acetyl-CoA as the defining product and annotate acetate production as acetogen-specific.
3. **Do not infer the complete pathway from CODH alone.** CODH supports reversible CO₂/CO chemistry and hydrogenogenic CO oxidation outside acetogenesis. (bahrle2023currentstatusof pages 8-9)
4. **Do not require both Rnf and Ech.** They are alternative, taxon-dependent energy-conservation systems. (zhang2024engineeredacetogenicbacteria pages 2-3, frolov2023obligateautotrophyat pages 1-2)
5. **Do not universalize HDCR or HydABC.** These are experimentally supported in particular acetogens, not all bacteria or archaea using WLP. (moon2023anewmetabolic pages 1-2, frolov2023obligateautotrophyat pages 8-9)
6. **Do not curate oxygen, sulfide, CO, acetate, or ethanol as universal inhibitors without concentration and taxon context.** Sensitivity depends on enzyme form, exposure, medium, and adaptation.
7. **Do not treat metagenomic gene inventories as demonstrated flux.** Require completeness plus expression, isotope tracing, metabolite production, or growth evidence for high-confidence phenotype calls.
8. **Do not use the December 2024 CODH-engineering preprint as evidence of complete WLP acquisition.** It is non-peer-reviewed and tests an engineered enzyme/activity context. (tharak2024heterologousexpressionof pages 20-23)
9. **Verify ontology identifiers before YAML import.** In particular, EC assignments for FDH, methylene-THF dehydrogenase/reductase, and methyltransferase depend on electron donor and reaction definition.

## DOI-first bibliography

1. Zhang J-Z et al. **Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals.** *Frontiers in Bioengineering and Biotechnology*. Published July 2024. DOI: [10.3389/fbioe.2024.1395540](https://doi.org/10.3389/fbioe.2024.1395540). (zhang2024engineeredacetogenicbacteria pages 2-3, zhang2024engineeredacetogenicbacteria pages 1-2)
2. Davin ME et al. **Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated H₂:CO feedstock ratios for enhancing carbon capture efficiency.** *Biotechnology for Biofuels and Bioproducts*. Published September 2024. DOI: [10.1186/s13068-024-02554-w](https://doi.org/10.1186/s13068-024-02554-w). (davin2024clostridiumautoethanogenumalters pages 1-2)
3. Moon J et al. **A new metabolic trait in an acetogen: Mixed acid fermentation of fructose in a methylene-tetrahydrofolate reductase mutant of Acetobacterium woodii.** *Environmental Microbiology Reports* 15:339–351. Published May 2023. DOI: [10.1111/1758-2229.13160](https://doi.org/10.1111/1758-2229.13160). (moon2023anewmetabolic pages 1-2)
4. Frolov EN et al. **Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium.** *Frontiers in Microbiology* 14. Published May 2023. DOI: [10.3389/fmicb.2023.1185739](https://doi.org/10.3389/fmicb.2023.1185739). (frolov2023obligateautotrophyat pages 1-2, frolov2023obligateautotrophyat pages 8-9)
5. Bährle R et al. **Current status of carbon monoxide dehydrogenases (CODH) and their potential for electrochemical applications.** *Bioresources and Bioprocessing* 10. Published November 2023. DOI: [10.1186/s40643-023-00705-9](https://doi.org/10.1186/s40643-023-00705-9). (bahrle2023currentstatusof pages 8-9)
6. Tharak A et al. **Heterologous expression of the carbon monoxide dehydrogenase gene from Clostridium sp. to enhance acetic acid and alcohol production from CO₂.** *bioRxiv*. Posted December 2024; **preprint**. DOI: [10.1101/2024.12.21.629878](https://doi.org/10.1101/2024.12.21.629878). (tharak2024heterologousexpressionof pages 20-23)
7. Can M, Armstrong FA, Ragsdale SW. **Structure, Function, and Mechanism of the Nickel Metalloenzymes, CO Dehydrogenase, and Acetyl-CoA Synthase.** *Chemical Reviews* 114:4149–4174. Published February 2014. DOI: [10.1021/cr400461p](https://doi.org/10.1021/cr400461p).
8. Ragsdale SW. **Enzymology of the Wood–Ljungdahl Pathway of Acetogenesis.** *Annals of the New York Academy of Sciences* 1125:129–136. Published March 2008. DOI: [10.1196/annals.1419.015](https://doi.org/10.1196/annals.1419.015).
9. Ragsdale SW, Pierce E. **Acetogenesis and the Wood–Ljungdahl pathway of CO₂ fixation.** *Biochimica et Biophysica Acta*. 2008. DOI: [10.1016/j.bbapap.2008.08.012](https://doi.org/10.1016/j.bbapap.2008.08.012).
10. Furdui C, Ragsdale SW. **The role of pyruvate:ferredoxin oxidoreductase in pyruvate synthesis during autotrophic growth by the Wood–Ljungdahl pathway.** *Journal of Biological Chemistry* 275:28494–28499. Published September 2000. DOI: [10.1074/jbc.M003291200](https://doi.org/10.1074/jbc.M003291200).

References

1. (moon2023anewmetabolic pages 1-2): Jimyung Moon, Anja Schubert, Anja Poehlein, Rolf Daniel, and Volker Müller. A new metabolic trait in an acetogen: mixed acid fermentation of fructose in a methylene‐tetrahydrofolate reductase mutant of acetobacterium woodii. Environmental Microbiology Reports, 15:339-351, May 2023. URL: https://doi.org/10.1111/1758-2229.13160, doi:10.1111/1758-2229.13160. This article has 6 citations and is from a peer-reviewed journal.

2. (frolov2023obligateautotrophyat pages 1-2): Evgenii N. Frolov, Alexander G. Elcheninov, Alexandra V. Gololobova, Stepan V. Toshchakov, Andrei A. Novikov, Alexander V. Lebedinsky, and Ilya V. Kublanov. Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1185739, doi:10.3389/fmicb.2023.1185739. This article has 29 citations and is from a peer-reviewed journal.

3. (zhang2024engineeredacetogenicbacteria pages 1-2): Jun-Zhe Zhang, Yu-Zhen Li, Zhi-Ning Xi, Hui-Peng Gao, Quan Zhang, Li-Cheng Liu, Fu-Li Li, and Xiao-Qing Ma. Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals. Frontiers in Bioengineering and Biotechnology, Jul 2024. URL: https://doi.org/10.3389/fbioe.2024.1395540, doi:10.3389/fbioe.2024.1395540. This article has 27 citations.

4. (zhang2024engineeredacetogenicbacteria pages 2-3): Jun-Zhe Zhang, Yu-Zhen Li, Zhi-Ning Xi, Hui-Peng Gao, Quan Zhang, Li-Cheng Liu, Fu-Li Li, and Xiao-Qing Ma. Engineered acetogenic bacteria as microbial cell factory for diversified biochemicals. Frontiers in Bioengineering and Biotechnology, Jul 2024. URL: https://doi.org/10.3389/fbioe.2024.1395540, doi:10.3389/fbioe.2024.1395540. This article has 27 citations.

5. (bahrle2023currentstatusof pages 8-9): Rebecca Bährle, Stefanie Böhnke, Jonas Englhard, Julien Bachmann, and Mirjam Perner. Current status of carbon monoxide dehydrogenases (codh) and their potential for electrochemical applications. Bioresources and Bioprocessing, Nov 2023. URL: https://doi.org/10.1186/s40643-023-00705-9, doi:10.1186/s40643-023-00705-9. This article has 33 citations and is from a peer-reviewed journal.

6. (davin2024clostridiumautoethanogenumalters pages 1-2): Megan E. Davin, R. Adam Thompson, Richard J. Giannone, Lucas W. Mendelson, Dana L. Carper, Madhavi Z. Martin, Michael E. Martin, Nancy L. Engle, Timothy J. Tschaplinski, Steven D. Brown, and Robert L. Hettich. Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated h2:co feedstock ratios for enhancing carbon capture efficiency. Biotechnology for Biofuels and Bioproducts, Sep 2024. URL: https://doi.org/10.1186/s13068-024-02554-w, doi:10.1186/s13068-024-02554-w. This article has 19 citations and is from a domain leading peer-reviewed journal.

7. (frolov2023obligateautotrophyat pages 8-9): Evgenii N. Frolov, Alexander G. Elcheninov, Alexandra V. Gololobova, Stepan V. Toshchakov, Andrei A. Novikov, Alexander V. Lebedinsky, and Ilya V. Kublanov. Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1185739, doi:10.3389/fmicb.2023.1185739. This article has 29 citations and is from a peer-reviewed journal.

8. (tharak2024heterologousexpressionof pages 20-23): Athmakuri Tharak, G Suresh, Sreeram Kaveti, Nishant Jain, and S Venkata Mohan. Heterologous expression of the carbon monoxide dehydrogenase gene from clostridium sp. to enhance acetic acid and alcohol production from co₂. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.21.629878, doi:10.1101/2024.12.21.629878. This article has 1 citations.