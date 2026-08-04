---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:51:34.708968'
end_time: '2026-08-04T07:01:15.514931'
duration_seconds: 580.81
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: reductive tricarboxylic acid cycle
  trait_identifier: traitmech:000021
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: reductive_tca_cycle
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan
    cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates
    in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium)
    and Aquificales.
  parent_traits: traitmech:000019
  synonyms: reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive\
    \ citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) |\
    \ DOI:10.1146/annurev-marine-120709-142712:  (H\xFCgler & Sievert document the\
    \ rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)"
  causal_graph_summary: 'rtca_reverse_tricarboxylic_acid_co2_fixation: 8 nodes, 8
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** reductive tricarboxylic acid cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000021
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium) and Aquificales.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert document the rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)
- **Existing causal graph summary:** rtca_reverse_tricarboxylic_acid_co2_fixation: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **reductive tricarboxylic acid cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/reductive_tca_cycle.yaml`.

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
- **Trait label:** reductive tricarboxylic acid cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000021
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium) and Aquificales.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert document the rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)
- **Existing causal graph summary:** rtca_reverse_tricarboxylic_acid_co2_fixation: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **reductive tricarboxylic acid cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/reductive_tca_cycle.yaml`.

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


# Curation report: reductive tricarboxylic acid cycle

## Trait record and scope

**Trait:** reductive tricarboxylic acid cycle  
**Identifier:** `traitmech:000021`  
**Category/kind/status:** METABOLISM / CLASS / REVIEWED  
**Parent:** `traitmech:000019`  
**Synonyms:** reductive citric acid cycle; rTCA cycle; Arnon–Buchanan cycle.

### Recommended operational definition

This trait is the physiological capacity for **net autotrophic inorganic-carbon assimilation through cyclic reverse flux around the tricarboxylic-acid network**, yielding acetyl-CoA and central biosynthetic precursors. The pathway reverses most oxidative-TCA reactions but replaces three conventionally irreversible steps with (i) ATP-dependent citrate cleavage, (ii) fumarate reduction, and (iii) ferredoxin-dependent reductive carboxylation of succinyl-CoA to 2-oxoglutarate. In the canonical Chlorobium-type pathway, two CO2 molecules yield acetyl-CoA; downstream pyruvate synthase and PEP carboxylase reactions distribute fixed carbon into pyruvate/PEP and oxaloacetate. Berg estimated at least two ATP equivalents to form pyruvate in Chlorobium, plus three additional ATP equivalents to reach triose phosphates. The pathway uses reduced ferredoxin and NAD(P)H. (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof media 8a2cffc6)

The trait is most securely associated with anaerobic or microaerophilic autotrophic bacteria, including green sulfur bacteria, Aquificota, Campylobacterota, Nitrospirota, and some Proteobacteria. Aquificota include thermophiles growing optimally at ≥70°C; *Aquifex aeolicus* can grow up to approximately 95°C. Nevertheless, oxygen tolerance is not an absolute exclusion: aerobic *Hydrogenobacter thermophilus* operates rTCA, and some sulfur-oxidizing symbionts encode both oxygen-sensitive rTCA and oxygen-tolerant CBB pathways. (berg2011ecologicalaspectsof pages 5-6, rubinblum2019geneticevidencefor pages 1-2)

### Inclusion criteria

Curate the trait as **experimentally supported** when there is evidence for net reverse-cycle flux, preferably autotrophic growth plus ^13CO2 incorporation, enzyme activity, metabolomics, or a combination of expression and physiological evidence. A complete diagnostic gene set is useful but establishes **genomic potential**, not the phenotype by itself.

A practical diagnostic core is:

1. citrate cleavage by `aclAB`, or the alternative `ccs` + `ccl` system;
2. ferredoxin-dependent 2-oxoglutarate synthase/oxidoreductase (`kor`/`oor`/`for` family, nomenclature taxon-dependent);
3. fumarate reductase;
4. the remaining reversible TCA reactions arranged so that oxaloacetate is regenerated.

### Boundary cases and exclusions

- **Oxidative TCA is not rTCA.** Shared enzymes do not establish reverse-cycle carbon fixation.
- **Reversed oxidative TCA (roTCA)** using ordinary citrate synthase under unusual thermodynamic conditions is a nearby but mechanistically distinct pathway and should not automatically be merged with canonical ACL/CCS–CCL rTCA. Ordinary citrate lyase can also support unusual variants, but bioinformatic discrimination is difficult. (garritano2022carbonfixationpathways pages 2-3)
- **Anaplerotic CO2 fixation is insufficient.** PEP carboxylase, pyruvate synthase, or reversible isocitrate-dehydrogenase activity alone does not demonstrate a closed autocatalytic rTCA cycle.
- **Incomplete rTCA segments** used biosynthetically or in heterotrophy should not receive the full trait.
- **Citrate cleavage alone is insufficient.** Eukaryotes commonly use ATP-citrate lyase for cytosolic acetyl-CoA production without operating rTCA. (sokolskyi2023roleofhorizontal pages 1-6)
- **Citrate-cleavage variants belong within the trait:** Chlorobium-type ACL and Aquificaceae-type CCS/CCL implement the same pathway function by one-step versus two-step chemistry. (sokolskyi2023roleofhorizontal pages 1-6, garritano2022carbonfixationpathways pages 2-3)
- **Aquificota low-CO2 variant:** biotin-dependent 2-oxoglutarate carboxylase can first produce oxalosuccinate, followed by nondecarboxylating isocitrate dehydrogenase. This is a taxon-specific implementation, not a universal required edge. (berg2011ecologicalaspectsof pages 4-5, scott2024widespreaddissolvedinorganic pages 13-15)

## Candidate nodes

### Pathway/process nodes

| Candidate | Suggested grounding | Curation note |
|---|---|---|
| reductive tricarboxylic acid cycle | `traitmech:000021`; KEGG module `M00173` | Primary trait node. |
| autotrophic CO2 fixation | GO label candidate; verify current GO CURIE before import | Parent biological capacity. |
| citrate-cleavage module | Label-only | Represent ACL and CCS/CCL alternatives beneath this node. |
| acetyl-CoA assimilation to pyruvate/PEP | Label-only | Downstream biosynthetic branch, not necessarily part of a minimal cycle definition. |
| dissolved inorganic carbon acquisition | Label-only | Modifier module involving transporters and carbonic anhydrases. |
| oxidative TCA cycle | KEGG pathway/module candidate | Explicit contrast node. |
| reversed oxidative TCA cycle | Label-only | Boundary-case pathway. |

### Enzymes, proteins, and genes

| Entity | Suggested identifier | Gene labels/notes |
|---|---|---|
| ATP-citrate lyase | `EC:2.3.3.8` | Usually `aclA`, `aclB` in bacteria; diagnostic citrate cleavage. |
| citryl-CoA synthetase | `EC:6.2.1.18` | Large/small subunits; nomenclature varies. |
| citryl-CoA lyase | `EC:4.1.3.34` | Completes two-step citrate cleavage. |
| fumarate reductase | `EC:1.3.5.4` for quinol:fumarate reductase where applicable | `frdABCD` or taxon-specific `tfrAB`; electron donor varies. |
| succinyl-CoA synthetase | `EC:6.2.1.5` | `sucCD`; reversible CoA activation step. |
| 2-oxoglutarate:ferredoxin oxidoreductase / synthase | `EC:1.2.7.3` candidate; verify exact enzyme variant | `korAB(CD)`, `oor`, or related labels. |
| isocitrate dehydrogenase | `EC:1.1.1.42` candidate for NADP-dependent enzyme | Direction and cofactor are organism-specific. |
| 2-oxoglutarate carboxylase | Label/EC verification required | Biotin-dependent Aquificota variant. |
| aconitate hydratase/aconitase | `EC:4.2.1.3` | Converts isocitrate through cis-aconitate to citrate. |
| fumarate hydratase | `EC:4.2.1.2` | Fumarate–malate step. |
| malate dehydrogenase | `EC:1.1.1.37` | Oxaloacetate–malate step. |
| pyruvate:ferredoxin oxidoreductase/synthase | `EC:1.2.7.1` | Reductive acetyl-CoA carboxylation into pyruvate. |
| PEP synthase | `EC:2.7.9.2` | Pyruvate-to-PEP biosynthetic branch. |
| PEP carboxylase | `EC:4.1.1.31` | HCO3−-dependent oxaloacetate formation. |
| carbonic anhydrase | `EC:4.2.1.1` | DIC-supply modifier, not a defining rTCA enzyme. |
| DIC transporter | Label-only unless family is known | SbtA/BicA/DAB-family grounding should be strain-specific. |
| Rnf complex | Label-only or GO/KEGG complex after verification | Candidate reduced-ferredoxin supply mechanism. |
| NADH dehydrogenase/heterodisulfide reductase-like complex | Label-only | Proposed electron-bifurcating supply route in tubeworm symbionts; uncertain. |

### Chemicals and cofactors

Use stable ChEBI identifiers only after registry validation during YAML import. High-value labels are: carbon dioxide, hydrogencarbonate/bicarbonate, citrate, citryl-CoA, oxaloacetate, acetyl-CoA, malate, fumarate, succinate, succinyl-CoA, 2-oxoglutarate, isocitrate, pyruvate, phosphoenolpyruvate, ATP, ADP, AMP, phosphate, CoA, NAD(P)H, oxidized ferredoxin, and reduced ferredoxin.

### Organisms and environments

Candidate taxon nodes include Chlorobiota/green sulfur bacteria, *Chlorobium*/*Chlorobaculum*, Aquificota/Aquificales, *Hydrogenobacter thermophilus*, Campylobacterota, Nitrospirota, *Nitrospira*, *Leptospirillum*, sulfur-oxidizing Gammaproteobacteria, and tubeworm symbionts. Add NCBITaxon CURIEs only after checking the current accepted name and strain.

Environmental nodes should include anoxic environment, microoxic environment, low-light photic habitat, hydrothermal/geothermal habitat, reduced-sulfur-rich habitat, and high-temperature environment. These are associations or selective contexts, not universally necessary conditions.

## Highest-confidence graph core

The following compact table summarizes the most defensible starting graph.

| subject | predicate | object | confidence/scope |
|---|---|---|---|
| reductive tricarboxylic acid cycle | fixes | CO2 to acetyl-CoA | high; canonical pathway definition in anaerobic/microaerophilic autotrophs (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof pages 1-2) |
| ATP-citrate lyase | cleaves | citrate to oxaloacetate + acetyl-CoA | high; canonical Chlorobium-type rTCA step (berg2011ecologicalaspectsof pages 5-6, sokolskyi2023roleofhorizontal pages 1-6) |
| citryl-CoA synthetase | forms | citryl-CoA from citrate | high; Aquificae-type citrate-cleavage variant (garritano2022carbonfixationpathways pages 2-3, sokolskyi2023roleofhorizontal pages 1-6) |
| citryl-CoA lyase | cleaves | citryl-CoA to oxaloacetate + acetyl-CoA | high; Aquificae-type citrate-cleavage variant (garritano2022carbonfixationpathways pages 2-3, sokolskyi2023roleofhorizontal pages 1-6) |
| fumarate reductase | reduces | fumarate to succinate | high; characteristic substituted rTCA reaction (berg2011ecologicalaspectsof pages 5-6, sokolskyi2023roleofhorizontal pages 1-6) |
| succinyl-CoA synthetase | forms | succinyl-CoA | high; canonical cycle step in Berg figure/legend (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof media 8a2cffc6) |
| ferredoxin-dependent 2-oxoglutarate synthase | carboxylates | succinyl-CoA to 2-oxoglutarate | high; characteristic reductive carboxylation step (berg2011ecologicalaspectsof pages 5-6, sokolskyi2023roleofhorizontal pages 1-6) |
| isocitrate dehydrogenase | reductively carboxylates | 2-oxoglutarate to isocitrate | high; canonical step, with Aquificae variant under some conditions (berg2011ecologicalaspectsof pages 4-5, scott2024widespreaddissolvedinorganic pages 13-15) |
| aconitase | isomerizes | isocitrate and citrate | high; canonical cycle step (berg2011ecologicalaspectsof pages 4-5, berg2011ecologicalaspectsof media 8a2cffc6) |
| reductive tricarboxylic acid cycle | requires | reduced ferredoxin | high; reduced ferredoxin explicitly used by key carboxylating steps (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof pages 1-2) |
| reductive tricarboxylic acid cycle | requires | ATP | high; ATP used in citrate cleavage and overall pathway energetics (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof pages 1-2) |


*Table: This table summarizes the most curation-ready causal edges for the reductive tricarboxylic acid cycle, focusing on canonical enzymatic steps and pathway-level requirements. It is useful as a compact starting point for constructing a TraitMech graph with only high-confidence, source-backed relationships.*

The canonical pathway topology and metabolite ordering are also directly shown in Berg’s Figure 3. (berg2011ecologicalaspectsof media 8a2cffc6)

## Evidence-backed candidate causal edges

| # | Subject — predicate — object | Reference and supporting snippet | Curation note |
|---|---|---|---|
| 1 | rTCA cycle — **fixes** — CO2 into acetyl-CoA | Berg 2011: the cycle “reverses the reactions of the oxidative citric acid cycle … and forms acetyl-CoA from two CO2s.” (berg2011ecologicalaspectsof pages 5-6) | **High confidence; core trait edge.** |
| 2 | rTCA cycle — **requires** — reduced ferredoxin | Berg 2011: “The rTCA cycle uses both reduced ferredoxin and NAD(P)H as electron donors.” (berg2011ecologicalaspectsof pages 5-6) | High confidence at pathway level; exact electron-delivery machinery is taxon-specific. |
| 3 | rTCA cycle — **consumes** — ATP | Berg 2011: “requires (at least in Chlorobium) only two ATP equivalents to form pyruvate.” (berg2011ecologicalaspectsof pages 5-6) | **Taxon/product-specific quantitative edge**; do not encode two ATP as a universal net stoichiometry. |
| 4 | ATP-citrate lyase — **cleaves** — citrate into oxaloacetate and acetyl-CoA | Sokolskyi & DasSarma 2023: Chlorobium ACL “catalyze[s] the citrate cleavage into oxaloacetate and acetyl-CoA.” (sokolskyi2023roleofhorizontal pages 1-6) | High confidence; defining Chlorobium-type edge. |
| 5 | ATP-citrate lyase — **uses** — ATP + CoA | Berg’s pathway shows ATP + CoA entering citrate cleavage and ADP + Pi leaving. (berg2011ecologicalaspectsof media 8a2cffc6) | High confidence for canonical ACL reaction. |
| 6 | citryl-CoA synthetase — **converts** — citrate to citryl-CoA | Sokolskyi & DasSarma: Aquificae CCS “produces citryl-CoA from citrate.” (sokolskyi2023roleofhorizontal pages 1-6) | High confidence; Aquificaceae-type alternative. |
| 7 | citryl-CoA lyase — **cleaves** — citryl-CoA into oxaloacetate and acetyl-CoA | Garritano et al.: “citryl-CoA is cleaved into OAA and acetyl-CoA.” (garritano2022carbonfixationpathways pages 2-3) | High confidence; curate in an alternative pathway branch. |
| 8 | citrate cleavage — **creates** — autocatalytic branching | The reaction “produces two oxaloacetate molecules per round.” (sokolskyi2023roleofhorizontal pages 1-6) | Mechanistically useful pathway-level edge; graph wording should avoid implying ACL alone synthesizes both OAA molecules. |
| 9 | fumarate reductase — **reduces** — fumarate to succinate | rTCA-specific reaction listed as “fumarate-succinate conversion by fumarate reductase.” (sokolskyi2023roleofhorizontal pages 1-6) | High confidence; donor should remain unspecified unless strain-specific evidence exists. |
| 10 | succinyl-CoA synthetase — **converts** — succinate + CoA + ATP to succinyl-CoA + ADP + Pi | Canonical figure shows ATP + CoA input and ADP + Pi output at the succinate/succinyl-CoA step. (berg2011ecologicalaspectsof media 8a2cffc6) | High confidence for the depicted ADP-forming variant; GDP-forming isoenzymes require separate modeling. |
| 11 | 2-oxoglutarate:ferredoxin oxidoreductase — **reductively carboxylates** — succinyl-CoA to 2-oxoglutarate | The defining step is “succinyl-CoA to 2-oxoglutarate by ferredoxin-dependent 2-oxoglutarate synthase.” (sokolskyi2023roleofhorizontal pages 1-6) | **High confidence; core carboxylation edge.** |
| 12 | reduced ferredoxin — **donates electrons to** — 2-oxoglutarate synthesis | Berg’s figure shows CO2 + CoA + Fdox produced while Fdred is consumed at this step. (berg2011ecologicalaspectsof media 8a2cffc6) | High confidence; balance exact ferredoxin stoichiometry against the selected reaction database. |
| 13 | isocitrate dehydrogenase — **reductively carboxylates** — 2-oxoglutarate to isocitrate | Berg describes normal reversible isocitrate dehydrogenase in mesophilic rTCA bacteria; the figure shows CO2 and NADPH consumption. (berg2011ecologicalaspectsof pages 4-5, berg2011ecologicalaspectsof media 8a2cffc6) | High confidence for canonical mesophilic variant; cofactor can differ. |
| 14 | 2-oxoglutarate carboxylase — **uses bicarbonate to form** — oxalosuccinate | Aquificota possess a biotin carboxylase that “assists isocitrate dehydrogenase by catalyzing the carboxylation of 2-oxoglutarate via HCO3−.” (scott2024widespreaddissolvedinorganic pages 13-15) | **Taxon-specific.** Add only to an Aquificota variant. |
| 15 | aconitase — **converts** — isocitrate to citrate | Berg’s canonical pathway places aconitate hydratase between isocitrate and citrate. (berg2011ecologicalaspectsof pages 4-5, berg2011ecologicalaspectsof media 8a2cffc6) | High confidence, though reversible chemistry should use a neutral predicate such as `catalyzes_interconversion`. |
| 16 | pyruvate:ferredoxin oxidoreductase — **reductively carboxylates** — acetyl-CoA to pyruvate | Berg: “Acetyl-CoA is reductively carboxylated to pyruvate by ferredoxin-dependent pyruvate synthase.” (berg2011ecologicalaspectsof pages 5-6) | High confidence downstream assimilation edge; optional for a minimal cycle graph. |
| 17 | PEP carboxylase — **carboxylates** — PEP to oxaloacetate | Berg identifies PEP carboxylase in the acetyl-CoA assimilation branch; the figure shows HCO3− input. (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof media 8a2cffc6) | High confidence branch edge; not specific to rTCA. |
| 18 | Fe–S type-I photosynthetic reaction center — **supports** — reduced-ferredoxin supply | Green sulfur bacteria possess a reaction center “capable of direct reduction of ferredoxin.” (berg2011ecologicalaspectsof pages 5-6) | **Taxon-specific ecological mechanism**, appropriate for Chlorobiota subgraphs. |
| 19 | DIC transporters/carbonic anhydrases — **increase availability of** — CO2/HCO3− to rTCA | Scott et al. 2024 found rTCA organisms have DIC-transporter and CA frequencies similar to CBB organisms and inferred adaptation to different CO2 regimes. (scott2024widespreaddissolvedinorganic pages 13-15) | **Supportive/inferred**, not part of the defining pathway. Curate only as a modifier with cautious predicates. |
| 20 | low-CO2 habitat — **selects for/associates with** — expanded DIC toolkit in Campylobacterota, Nitrospirota, and Aquificota | These groups typically encode multiple CAs, at least one DIC transporter, or both; authors state this “may suggest” low-CO2 adaptation. (scott2024widespreaddissolvedinorganic pages 13-15) | **Uncertain inference**, not a direct causal result. |
| 21 | rTCA cycle — **is inhibited by** — oxygen | Rubin-Blum et al. call rTCA oxygen-sensitive and CBB oxygen-tolerant in tubeworm symbionts. (rubinblum2019geneticevidencefor pages 1-2) | Keep qualified: pathway/enzyme oxygen sensitivity varies, and aerobic rTCA organisms exist. Do not encode oxygen as an absolute negative regulator. |
| 22 | fluctuating redox conditions — **may regulate partitioning between** — rTCA and CBB | Authors propose interplay under fluctuating redox conditions in sulfur-oxidizing symbionts. (rubinblum2019geneticevidencefor pages 1-2, rubinblum2019geneticevidencefor pages 2-3) | **Hypothesis**, not yet a universal curation edge. |
| 23 | Rnf/transhydrogenase/electron-bifurcating complex — **may supply reducing power to** — OGOR | Genomic/transcriptomic data “suggest[] a potential electron flow toward” OGOR through these complexes. (rubinblum2019geneticevidencefor pages 1-2) | **Uncertain, taxon-specific inferred edge.** |
| 24 | expression of heterologous `korAB` — **enables** — ^13CO2 incorporation into TCA metabolites in engineered *E. coli* | Peng et al. 2025 used ^13CO2 tracing; KOR supported assimilation, while ACL coexpression redirected flux toward amino acids and nucleotides. (peng2025carbonfluxesrewiring pages 1-2) | Current application evidence; engineered context, not natural sufficiency. |
| 25 | `aclAB` coexpression with `korAB` — **increases** — redistribution of fixed carbon into biosynthesis | Isotopic enrichment increased in methionine, threonine, glycine, deoxythymidine, and deoxycytidine. (peng2025carbonfluxesrewiring pages 1-2) | 2025 application; useful for engineering graphs, but outside a strictly natural-trait core. |

## Recent developments and relevant data

### 2023: evolutionary history remains contested

A 2023 phylogenetic preprint argues that the patchy modern distribution of citrate-cleavage enzymes and succinyl-CoA synthetase is better explained by extensive horizontal gene transfer than by repeated losses. It identified several taxa with **theoretical** complete rTCA capacity, including *Syntrophobacter*, *Desulfofundulus*, *Beggiatoa*, *Caldithrix*, “Ca. Acidulodesulfobacterales,” and “Ca. Micrarchaeota.” The study explicitly warns that few candidate taxa carry a complete cycle and that abundant HGT prevents confident inference that LUCA operated rTCA. These evolutionary propositions should remain outside the core causal graph. (sokolskyi2023roleofhorizontal pages 12-18, sokolskyi2023roleofhorizontal pages 6-12, sokolskyi2023roleofhorizontal pages 1-6)

The same work reports standard transformed free energies of approximately −1.2 kJ mol−1 for succinyl-CoA synthesis and −5.9 kJ mol−1 for citryl-CoA synthesis, based on eQuilibrator. These values are condition-dependent computational estimates, not universal cellular ΔG values. (sokolskyi2023roleofhorizontal pages 12-18)

### 2022–2024: broader genomic distribution and DIC acquisition

A survey of **52,515 MAGs** identified carbon-fixation pathways in **1,007** bacterial and archaeal genomes. For rTCA, its thresholds detected 207 ACL-type (`rTCA1`) and 10 CCS/CCL-type (`rTCA2`) MAGs. Two Thermoplasmatota MAGs had >97% adjusted pathway completeness; four Elusimicrobiota MAGs also exceeded 97%. These are important distributional statistics, but they represent predicted capacity rather than measured autotrophic flux. (garritano2022carbonfixationpathways pages 2-3)

A February 2024 review found a bimodal DIC-acquisition pattern: Chlorobiota commonly encode one carbonic anhydrase and no recognized DIC transporter, whereas Campylobacterota, Nitrospirota, and Aquificota generally possess multiple carbonic anhydrases, a DIC transporter, or both. The authors interpret this cautiously as possible adaptation to high- versus low-CO2 habitats. (scott2024widespreaddissolvedinorganic pages 13-15)

A 2024 Tuz Lake study reported rTCA as the highest predicted carbon-fixation pathway, with a significant seasonal maximum in spring. However, this was a PICRUSt2 inference from 16S profiles: ATP-citrate lyase was not detected, while citryl-CoA lyase was. Therefore, it does **not** securely demonstrate a complete active rTCA pathway and should not be used as direct trait evidence. (dogan2024seasonalgeneprofiling pages 5-6)

### Current applications

The pathway is relevant to carbon-capture biotechnology because it is ATP-efficient and produces central metabolites directly. Current implementations are principally laboratory metabolic engineering rather than commercial deployment. A 2025 peer-reviewed study expressed *Chlorobium tepidum* KOR and ACL in *E. coli* under hydrogen-powered anaerobic conditions; ^13CO2 tracing showed assimilation into TCA metabolites and increased labeling of selected amino acids and nucleotides when ACL accompanied KOR. This demonstrates practical flux rewiring but not a fully autonomous, native-like rTCA cycle from only two enzymes. (peng2025carbonfluxesrewiring pages 1-2)

The broader 2024 synthetic-carbon-fixation literature emphasizes cell-free pathway assembly, cofactor optimization, machine-learning-assisted pathway design, and eventual transplantation into lithotrophs or phototrophs. These are relevant engineering contexts, but artificial cycles should not be represented as instances of `traitmech:000021` unless they reproduce the defining rTCA topology. (tommasi2024thebiochemistryof pages 4-6, tommasi2024thebiochemistryof pages 2-4)

## Recommended graph architecture

Use an **OR branch** for citrate cleavage:

- `citrate →[ATP-citrate lyase] acetyl-CoA + oxaloacetate`, or
- `citrate →[citryl-CoA synthetase] citryl-CoA →[citryl-CoA lyase] acetyl-CoA + oxaloacetate`.

The main cycle should then connect oxaloacetate → malate → fumarate → succinate → succinyl-CoA → 2-oxoglutarate → isocitrate → citrate, with explicit CO2/reduced-ferredoxin input at 2-oxoglutarate synthesis and CO2/NAD(P)H input at reductive isocitrate-dehydrogenase chemistry. Add pyruvate/PEP assimilation as a downstream branch. Put Aquificota’s 2-oxoglutarate-carboxylase variant, Chlorobiota photochemical ferredoxin reduction, DIC acquisition, and sulfur/hydrogen oxidation in taxon- or environment-specific extension modules rather than the universal core.

## Warnings: claims not ready for TraitMech curation

1. **Do not infer the trait from `acl`, `ccl`, `kor`, or ordinary TCA genes individually.** Citrate cleavage occurs in other biological contexts, and most TCA reactions are reversible.
2. **Do not curate MAG completeness as demonstrated phenotype.** The 207/10 MAG counts and newly proposed archaeal distributions are genomic predictions. (garritano2022carbonfixationpathways pages 2-3)
3. **Do not treat oxygen as an absolute inhibitor.** Some complete pathways operate in aerobic organisms; sensitivity is enzyme-, organism-, and redox-context dependent. (berg2011ecologicalaspectsof pages 5-6, rubinblum2019geneticevidencefor pages 1-2)
4. **Do not curate LUCA possession, primordial autocatalysis, or syntrophic completion as established causal biology.** These remain evolutionary hypotheses. (sokolskyi2023roleofhorizontal pages 6-12, sokolskyi2023roleofhorizontal pages 1-6)
5. **Do not curate Haloarchaea–Nanohaloarchaea pathway complementation without experimental flux evidence.** It is a proposed syntrophic model. (sokolskyi2023roleofhorizontal pages 18-23)
6. **Do not use the Tuz Lake result as direct pathway activity.** It is marker inference, lacks detected ACL, and may reflect incomplete or misassigned modules. (dogan2024seasonalgeneprofiling pages 5-6)
7. **Do not assign a single universal gene name or electron donor to fumarate reductase.** The natural donor is unknown in some green sulfur bacteria, while NADH was demonstrated in *Hydrogenobacter*. (berg2011ecologicalaspectsof pages 5-6)
8. **Validate every ontology identifier at import time.** Enzyme direction, subunit composition, gene nomenclature, and accepted taxon names vary; label-only nodes are safer than guessed CURIEs.

## DOI-first bibliography

1. **Scott KM, Payne RR, Gahramanova A.** “Widespread dissolved inorganic carbon-modifying toolkits…” *Applied and Environmental Microbiology* 90(2), February 2024. DOI: [10.1128/AEM.01557-23](https://doi.org/10.1128/AEM.01557-23). (scott2024widespreaddissolvedinorganic pages 13-15)
2. **Doğan SS, Kocabaş A.** “Seasonal Gene Profiling in Tuz Lake with Regard to Biogeochemical Cycling.” *KSU Journal of Agriculture and Nature* 27:273–284, April 2024. DOI: [10.18016/ksutarimdoga.vi.1212062](https://doi.org/10.18016/ksutarimdoga.vi.1212062). (dogan2024seasonalgeneprofiling pages 5-6)
3. **Tommasi IC.** “The Biochemistry of Artificial CO2-Fixation Pathways.” *Catalysts* 14:679, October 2024. DOI: [10.3390/catal14100679](https://doi.org/10.3390/catal14100679). (tommasi2024thebiochemistryof pages 4-6, tommasi2024thebiochemistryof pages 2-4)
4. **Sokolskyi T, DasSarma S.** “Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle.” bioRxiv, October 2023; **preprint**. DOI: [10.1101/2022.10.25.513756](https://doi.org/10.1101/2022.10.25.513756). (sokolskyi2023roleofhorizontal pages 12-18, sokolskyi2023roleofhorizontal pages 1-6)
5. **Zhang X et al.** “Late acquisition of the rTCA carbon fixation pathway by Chlorobi.” *Nature Ecology & Evolution* 7:1398–1407, August 2023. DOI: [10.1038/s41559-023-02147-0](https://doi.org/10.1038/s41559-023-02147-0).
6. **Garritano AN, Song W, Thomas T.** “Carbon fixation pathways across the bacterial and archaeal tree of life.” *PNAS Nexus* 1(5), October 2022. DOI: [10.1093/pnasnexus/pgac226](https://doi.org/10.1093/pnasnexus/pgac226). (garritano2022carbonfixationpathways pages 2-3)
7. **Berg IA.** “Ecological Aspects of the Distribution of Different Autotrophic CO2 Fixation Pathways.” *Applied and Environmental Microbiology* 77:1925–1936, March 2011; online 7 January 2011. DOI: [10.1128/AEM.02473-10](https://doi.org/10.1128/AEM.02473-10). (berg2011ecologicalaspectsof pages 5-6, berg2011ecologicalaspectsof pages 1-2)
8. **Hügler M, Huber H, Molyneaux SJ, Vetriani C, Sievert SM.** “Autotrophic CO2 fixation via the reductive tricarboxylic acid cycle in different lineages within the phylum Aquificae: evidence for two ways of citrate cleavage.” *Environmental Microbiology* 9:81–92, 2007. DOI: [10.1111/j.1462-2920.2006.01118.x](https://doi.org/10.1111/j.1462-2920.2006.01118.x).
9. **Kim W, Tabita FR.** “Both subunits of ATP-citrate lyase from Chlorobium tepidum contribute to catalytic activity.” *Journal of Bacteriology* 188:6544–6552, September 2006. DOI: [10.1128/JB.00523-06](https://doi.org/10.1128/JB.00523-06).
10. **Wahlund TM, Tabita FR.** “The reductive tricarboxylic acid cycle of carbon dioxide assimilation: initial studies and purification of ATP-citrate lyase from the green sulfur bacterium Chlorobium tepidum.” *Journal of Bacteriology* 179:4859–4867, August 1997. DOI: [10.1128/JB.179.15.4859-4867.1997](https://doi.org/10.1128/JB.179.15.4859-4867.1997).
11. **Rubin-Blum M, Dubilier N, Kleiner M.** “Genetic Evidence for Two Carbon Fixation Pathways…” *mSphere* 4:e00394-18, January 2019. DOI: [10.1128/mSphere.00394-18](https://doi.org/10.1128/mSphere.00394-18). (rubinblum2019geneticevidencefor pages 1-2, rubinblum2019geneticevidencefor pages 2-3)
12. **Peng J-H et al.** “Carbon fluxes rewiring in engineered E. coli via reverse tricarboxylic acid cycle pathway under chemolithotrophic condition.” *Journal of Biological Engineering* 19, February 2025. DOI: [10.1186/s13036-025-00489-w](https://doi.org/10.1186/s13036-025-00489-w). Included as the clearest current implementation beyond the requested 2023–2024 priority window. (peng2025carbonfluxesrewiring pages 1-2)

References

1. (berg2011ecologicalaspectsof pages 5-6): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

2. (berg2011ecologicalaspectsof media 8a2cffc6): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

3. (rubinblum2019geneticevidencefor pages 1-2): Maxim Rubin-Blum, Nicole Dubilier, and Manuel Kleiner. Genetic evidence for two carbon fixation pathways (the calvin-benson-bassham cycle and the reverse tricarboxylic acid cycle) in symbiotic and free-living bacteria. mSphere, Feb 2019. URL: https://doi.org/10.1128/msphere.00394-18, doi:10.1128/msphere.00394-18. This article has 69 citations and is from a peer-reviewed journal.

4. (garritano2022carbonfixationpathways pages 2-3): Alessandro N Garritano, Weizhi Song, and Torsten Thomas. Carbon fixation pathways across the bacterial and archaeal tree of life. PNAS Nexus, Oct 2022. URL: https://doi.org/10.1093/pnasnexus/pgac226, doi:10.1093/pnasnexus/pgac226. This article has 130 citations and is from a peer-reviewed journal.

5. (sokolskyi2023roleofhorizontal pages 1-6): Tymofii Sokolskyi and Shiladitya DasSarma. Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.513756, doi:10.1101/2022.10.25.513756. This article has 6 citations.

6. (berg2011ecologicalaspectsof pages 4-5): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

7. (scott2024widespreaddissolvedinorganic pages 13-15): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 8 citations and is from a peer-reviewed journal.

8. (berg2011ecologicalaspectsof pages 1-2): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

9. (rubinblum2019geneticevidencefor pages 2-3): Maxim Rubin-Blum, Nicole Dubilier, and Manuel Kleiner. Genetic evidence for two carbon fixation pathways (the calvin-benson-bassham cycle and the reverse tricarboxylic acid cycle) in symbiotic and free-living bacteria. mSphere, Feb 2019. URL: https://doi.org/10.1128/msphere.00394-18, doi:10.1128/msphere.00394-18. This article has 69 citations and is from a peer-reviewed journal.

10. (peng2025carbonfluxesrewiring pages 1-2): Jian-Hau Peng, Shou-Chen Lo, Yu-Ning Yu, Ya-Tang Yang, Yu-Chieh Chen, An-I Tsai, Dong-Yan Wu, Chu-Han Huang, Tien-Tsai Su, Chieh-Chen Huang, and En-Pei Isabel Chiang. Carbon fluxes rewiring in engineered e. coli via reverse tricarboxylic acid cycle pathway under chemolithotrophic condition. Journal of Biological Engineering, Feb 2025. URL: https://doi.org/10.1186/s13036-025-00489-w, doi:10.1186/s13036-025-00489-w. This article has 15 citations and is from a peer-reviewed journal.

11. (sokolskyi2023roleofhorizontal pages 12-18): Tymofii Sokolskyi and Shiladitya DasSarma. Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.513756, doi:10.1101/2022.10.25.513756. This article has 6 citations.

12. (sokolskyi2023roleofhorizontal pages 6-12): Tymofii Sokolskyi and Shiladitya DasSarma. Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.513756, doi:10.1101/2022.10.25.513756. This article has 6 citations.

13. (dogan2024seasonalgeneprofiling pages 5-6): Suzan Sahin Dogan and Aytaç Kocabaş. Seasonal gene profiling in tuz lake with regard to biogeochemical cycling. Kahramanmaraş Sütçü İmam Üniversitesi Tarım ve Doğa Dergisi, 27(2):273-284, Apr 2024. URL: https://doi.org/10.18016/ksutarimdoga.vi.1212062, doi:10.18016/ksutarimdoga.vi.1212062. This article has 3 citations.

14. (tommasi2024thebiochemistryof pages 4-6): Immacolata C. Tommasi. The biochemistry of artificial co2-fixation pathways: the exploitation of carboxylase enzymes alternative to rubisco. Catalysts, 14:679, Oct 2024. URL: https://doi.org/10.3390/catal14100679, doi:10.3390/catal14100679. This article has 8 citations.

15. (tommasi2024thebiochemistryof pages 2-4): Immacolata C. Tommasi. The biochemistry of artificial co2-fixation pathways: the exploitation of carboxylase enzymes alternative to rubisco. Catalysts, 14:679, Oct 2024. URL: https://doi.org/10.3390/catal14100679, doi:10.3390/catal14100679. This article has 8 citations.

16. (sokolskyi2023roleofhorizontal pages 18-23): Tymofii Sokolskyi and Shiladitya DasSarma. Role of horizontal gene transfers and microbial ecology in the evolution of fluxes through the tricarboxylic acid cycle. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2022.10.25.513756, doi:10.1101/2022.10.25.513756. This article has 6 citations.