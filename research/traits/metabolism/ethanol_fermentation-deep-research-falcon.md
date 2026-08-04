---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:08:33.389777'
end_time: '2026-08-04T06:15:54.339789'
duration_seconds: 440.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ethanol fermentation
  trait_identifier: traitmech:000028
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: ethanol_fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing
    CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic
    of yeasts and the bacterium Zymomonas mobilis.
  parent_traits: METPO:1002005
  synonyms: alcoholic fermentation
  evidence_summary: 'DOI:10.3390/molecules31020333:  (Review of classical fermentations
    describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated
    and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative
    energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)'
  causal_graph_summary: 'ethanol_fermentation_pyruvate_to_ethanol: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ethanol fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000028
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic of yeasts and the bacterium Zymomonas mobilis.
- **Parent traits:** METPO:1002005
- **Synonyms:** alcoholic fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)
- **Existing causal graph summary:** ethanol_fermentation_pyruvate_to_ethanol: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **ethanol fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/ethanol_fermentation.yaml`.

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
- **Trait label:** ethanol fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000028
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation in which pyruvate is decarboxylated to acetaldehyde (releasing CO2) and then reduced by NADH to ethanol, regenerating NAD+ for glycolysis. Characteristic of yeasts and the bacterium Zymomonas mobilis.
- **Parent traits:** METPO:1002005
- **Synonyms:** alcoholic fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes the alcoholic (ethanol) pathway in which pyruvate is decarboxylated and reduced to ethanol.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports ethanol as an NADH-reoxidizing fermentation end product.)
- **Existing causal graph summary:** ethanol_fermentation_pyruvate_to_ethanol: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **ethanol fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/ethanol_fermentation.yaml`.

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


# Curation report: microbial ethanol fermentation

## Trait record and scope

- **Trait label:** ethanol fermentation
- **Trait identifier:** `traitmech:000028`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1002005`
- **Synonym:** alcoholic fermentation

### Recommended operational definition

This trait denotes the **physiological capacity for net fermentative formation of ethanol**, with the canonical graph centered on two cytosolic reactions: (1) thiamine-pyrophosphate-dependent pyruvate decarboxylase (PDC) converts pyruvate to acetaldehyde and CO₂; (2) NADH-dependent alcohol dehydrogenase (ADH) reduces acetaldehyde to ethanol and regenerates NAD⁺. NAD⁺ regeneration permits glycolysis—and therefore substrate-level ATP formation—to continue when respiratory NADH oxidation is unavailable or insufficient. Glycolysis yields pyruvate, ATP, and NADH; fermentation itself adds no ATP beyond glycolysis. (pronk1996pyruvatemetabolismin pages 5-6, eram2013decarboxylationofpyruvate pages 3-6, pfeiffer2014anevolutionaryperspective pages 1-2)

The trait should be recognized by **net ethanol production under a defined fermentative or respiro-fermentative assay**, not merely by the presence of an `adh` homolog. ADHs are often reversible and may instead mediate ethanol oxidation; fungal ADH paralogs differ in physiological direction, regulation, substrate specificity, and localization. (gutierrezcorona2023fungalalcoholdehydrogenases pages 8-10, gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5)

### Important boundary cases

1. **Crabtree-positive aerobic fermentation belongs within scope.** Fermentation need not imply strict anoxia: *Saccharomyces cerevisiae* and other Crabtree-positive yeasts produce ethanol at high glucose even when oxygen is present. The Crabtree effect is a regulatory/ecophysiological route to the same ethanol-forming chemistry, not a separate terminal pathway. (pfeiffer2014anevolutionaryperspective pages 1-2, jouhten2008oxygendependenceof pages 1-2)
2. **Respiration is a competing nearby state, not part of the trait.** Respiratory pyruvate oxidation through acetyl-CoA/TCA/OXPHOS should be represented as a competing branch when relevant. In *S. cerevisiae*, the cited estimate is approximately 18 ATP per glucose through respiration versus 2 ATP per glucose through fermentation. (pfeiffer2014anevolutionaryperspective pages 1-2)
3. **Ethanol utilization is not ethanol fermentation.** Oxidative ADH activity converting ethanol toward acetaldehyde/acetate is an adjacent but inverse phenotype. An ADH annotation alone is therefore insufficient evidence. (gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5)
4. **Alternative bacterial routes require a separate module.** Some organisms form acetaldehyde through pyruvate→acetyl-CoA followed by CoA-acetylating acetaldehyde dehydrogenase, including `adhE`-associated chemistry, rather than direct PDC. This may support a broader ethanol-fermentation class but should not be silently merged into a graph specifically named “pyruvate-to-ethanol via PDC.” (eram2013decarboxylationofpyruvate pages 1-3)
5. **Mixed fermentation is in scope only for its ethanol branch.** Lactate, acetate, acetoin, glycerol, 2,3-butanediol, and alanine routes compete for carbon or redox equivalents; production of these metabolites does not itself establish ethanol fermentation.
6. **Assay detection alone is weaker than mechanism.** Ethanol in a culture can reflect cross-feeding, abiotic carry-over, or another community member. Pure-culture production, isotope tracing, enzyme/genetic perturbation, or stoichiometric product measurements are stronger evidence.

## Candidate nodes and ontology grounding

Identifiers below are limited to mappings that can be stated conservatively without inventing accessions. Exact ChEBI, Rhea, KEGG, MetaCyc, UniProt, and strain-specific gene accessions should be validated against the project’s approved ontology release before YAML insertion.

### Pathways and biological processes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| ethanol fermentation | `traitmech:000028`; parent `METPO:1002005` | Trait root; quote identifier verbatim in YAML. |
| glycolysis | `GO:0006096` | Upstream module in yeast; produces pyruvate, NADH, and ATP. |
| Entner–Doudoroff pathway | label-only pending ontology validation | Principal high-flux sugar-catabolic route in *Zymomonas mobilis*. |
| NAD⁺ regeneration / NADH reoxidation | label-only candidate | Functional purpose of the terminal ADH reaction. |
| substrate-level phosphorylation | `GO:0042777` | ATP is generated in glycolysis, not by the two terminal ethanol reactions. |
| cellular respiration | `GO:0045333` | Competing process; oxygen availability and glucose repression affect partitioning. |
| TCA cycle | `GO:0006099` | Competing respiratory carbon route. |
| Crabtree effect / aerobic alcoholic fermentation | label-only candidate | Ecophysiological state, taxon-specific rather than universal. |
| acetyl-CoA-dependent ethanol pathway | label-only candidate | Alternative bacterial module involving PFL/POR and acetaldehyde dehydrogenase/AdhE. |

### Genes, proteins, enzymes, and molecular functions

| Candidate node | Suggested grounding | Scope |
|---|---|---|
| pyruvate decarboxylase | `EC:4.1.1.1`; molecular-function CURIE should be release-checked | Canonical direct pyruvate→acetaldehyde enzyme; TPP-dependent. |
| *S. cerevisiae* `PDC1`, `PDC5`, `PDC6` | gene labels; use SGD accessions after validation | Three structural genes reported for yeast PDC; do not collapse gene-specific regulation without additional evidence. (pronk1996pyruvatemetabolismin pages 6-8) |
| alcohol dehydrogenase | `EC:1.1.1.1` for NAD⁺-dependent alcohol dehydrogenase, subject to isoenzyme validation | Reaction direction must be specified. |
| *S. cerevisiae* `ADH1` | gene label; use SGD/UniProt identifier after validation | Strong candidate for fermentative acetaldehyde reduction, but exact accession and paralog relationships should be independently checked. |
| *Z. mobilis* `pdc` / ZMO1360 | gene label; protein GenBank AAV89984.1 reported | Strong taxon-specific node. (frohwitter2024anewzymomonas pages 1-2) |
| *Z. mobilis* `adhB` / ADH II | label-only pending accession validation | Candidate terminal reductase; avoid making it the sole universal ADH node. |
| CoA-acetylating acetaldehyde dehydrogenase | enzyme label; EC/Rhea to validate | Alternative route; associated with `mhpF` and `adhE` in some bacteria. (eram2013decarboxylationofpyruvate pages 1-3) |
| pyruvate formate-lyase | enzyme label; EC to validate | Alternative pyruvate→acetyl-CoA/formate branch. |
| pyruvate:ferredoxin oxidoreductase | enzyme label; EC to validate | Alternative route and reported bifunctional POR/PDC activity in *Pyrococcus furiosus*. (eram2013decarboxylationofpyruvate pages 1-3) |
| lactate dehydrogenase | `EC:1.1.1.27` if L-lactate-specific; validate stereochemistry | Competing engineered pyruvate sink in *Z. mobilis*. |

### Chemicals, cofactors, products, and inhibitors

Candidate chemical nodes are **glucose, fructose, sucrose, pyruvate, acetaldehyde, ethanol, carbon dioxide, NADH, NAD⁺, ADP, ATP, thiamine diphosphate/TPP, acetyl-CoA, lactate, acetate, acetoin, glycerol, alanine, oxygen, benzoic acid, and sodium gluconate**. ChEBI identifiers should be batch-validated rather than entered from memory. The chemically essential graph core is:

`pyruvate → acetaldehyde + CO₂ → ethanol`, coupled to `NADH → NAD⁺` in the second reaction. (eram2013decarboxylationofpyruvate pages 3-6, pfeiffer2014anevolutionaryperspective pages 1-2)

### Taxa, localization, and environment

- *Saccharomyces cerevisiae*: `NCBITaxon:4932`.
- *Zymomonas mobilis*: `NCBITaxon:542`.
- Canonical yeast PDC and fermentative ADH chemistry is cytosolic; a fungal review’s enzyme table also identifies acetaldehyde/NADH-dependent fermentative ADH activity in the cytoplasm. Localization should remain attached to the specific protein/taxon rather than asserted universally. (gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5)
- Environmental/experimental nodes: anoxic or oxygen-limited culture; high-glucose conditions; glucose-limited chemostat; aerobic culture; molasses/sucrose medium; benzoic-acid stress; ethanol concentration; pH; temperature; batch, continuous, and cell-free formats.

## Candidate causal edges

“Strong” indicates direct reaction chemistry, a controlled perturbation, or quantitative physiology. “Conditional” indicates a taxon-, strain-, phase-, or assay-specific relationship.

| # | Subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---:|---|---|---|
| 1 | glycolysis — **produces** → pyruvate | DOI [10.3389/fmolb.2014.00017](https://doi.org/10.3389/fmolb.2014.00017), published 21 Oct 2014: “Sugars such as glucose are converted into pyruvate through glycolysis.” (pfeiffer2014anevolutionaryperspective pages 1-2) | **Strong.** Upstream module; yeast framing. |
| 2 | lower glycolysis — **produces** → NADH | Same source: downstream three-carbon sugars are degraded to pyruvate, “each yielding 2 ATP and 1 NADH.” (pfeiffer2014anevolutionaryperspective pages 1-2) | **Strong.** The per-triose statement implies two NADH per glucose. |
| 3 | pyruvate decarboxylase — **converts** → pyruvate to acetaldehyde + CO₂ | DOI [10.3390/biom3030578](https://doi.org/10.3390/biom3030578), published 21 Aug 2013: PDC is TPP-dependent and catalyzes “non-oxidative decarboxylation of pyruvate to acetaldehyde and carbon dioxide.” (eram2013decarboxylationofpyruvate pages 3-6) | **Strong canonical edge.** |
| 4 | thiamine diphosphate — **is cofactor for** → pyruvate decarboxylase | Same review calls PDC “a thiamine pyrophosphate (TPP)-containing enzyme.” (eram2013decarboxylationofpyruvate pages 1-3) | **Strong.** Use preferred ontology label consistently. |
| 5 | acetaldehyde — **accepts reducing equivalents from** → NADH through ADH | The canonical yeast pathway identifies acetaldehyde as “the electron acceptor for NADH reoxidation during fermentative growth.” (pronk1996pyruvatemetabolismin pages 5-6) | **Strong biochemical interpretation.** |
| 6 | alcohol dehydrogenase — **reduces** → acetaldehyde to ethanol | DOI [10.3390/biom3030578](https://doi.org/10.3390/biom3030578): acetaldehyde is converted to ethanol by ADH; ADHs catalyze reversible alcohol/aldehyde interconversion. (eram2013decarboxylationofpyruvate pages 3-6) | **Strong**, but encode direction for fermentation. |
| 7 | ADH-mediated acetaldehyde reduction — **oxidizes** → NADH to NAD⁺ | DOI [10.3389/fmolb.2014.00017](https://doi.org/10.3389/fmolb.2014.00017): “Adh recycles the NADH that is formed in lower glycolysis back into NAD+.” (pfeiffer2014anevolutionaryperspective pages 1-2) | **Strong core redox edge.** |
| 8 | NAD⁺ regeneration — **enables continuation of** → glycolysis without oxygen | Same source states that recycling NADH to NAD⁺ allows alcoholic fermentation to operate without oxygen. (pfeiffer2014anevolutionaryperspective pages 1-2) | **Strong functional edge.** |
| 9 | glycolysis coupled to ethanol fermentation — **yields net** → 2 ATP per glucose | Same source reports fermentation’s net gain as 2 ATP per glucose and clarifies that conversion of pyruvate to ethanol produces no additional ATP. (pfeiffer2014anevolutionaryperspective pages 1-2) | **Strong stoichiometric annotation.** Avoid saying PDC/ADH generate ATP. |
| 10 | *S. cerevisiae* `PDC1`, `PDC5`, `PDC6` — **encode** → pyruvate decarboxylase isoenzymes | DOI [10.1002/(SICI)1097-0061(199612)12:16%3C1607::AID-YEA70%3E3.0.CO;2-4](https://doi.org/10.1002/(SICI)1097-0061(199612)12:16%3C1607::AID-YEA70%3E3.0.CO;2-4), Dec 1996: PDC is encoded by three structural genes, `PDC1`, `PDC5`, and `PDC6`. (pronk1996pyruvatemetabolismin pages 6-8) | **Strong, taxon-specific.** |
| 11 | high glucose in Crabtree-positive yeasts — **induces/favors** → aerobic ethanol fermentation | DOI [10.3389/fmolb.2014.00017](https://doi.org/10.3389/fmolb.2014.00017): *S. cerevisiae* uses fermentation “even in the presence of oxygen, when glucose concentrations are sufficiently high.” (pfeiffer2014anevolutionaryperspective pages 1-2) | **Strong ecological edge**, but not universal across yeasts. |
| 12 | restricted oxygen/respiration — **redirects carbon flux toward** → fermentation | DOI [10.1186/1752-0509-2-60](https://doi.org/10.1186/1752-0509-2-60), published 9 Jul 2008: at 1.0% and 0.5% inlet O₂, respiratory rate was severely restricted and major fluxes progressively shifted to fermentation. (jouhten2008oxygendependenceof pages 1-2) | **Strong, strain/chemostat-specific quantitative edge.** |
| 13 | 0.5% inlet O₂ — **causes yields of** → ethanol + CO₂ to exceed biomass yield | Same study: only at 0.5% O₂ did ethanol and CO₂ yields exceed biomass yield; respiration still supplied 25% of ATP demand, versus 59% under fully aerobic conditions. (jouhten2008oxygendependenceof pages 1-2) | **Conditional quantitative edge.** Do not generalize threshold across strains/processes. |
| 14 | *Z. mobilis* Entner–Doudoroff pathway — **supports high flux toward** → ethanol | DOI [10.1186/s12934-024-02419-9](https://doi.org/10.1186/s12934-024-02419-9), published May 2024: ED metabolism permits glucose uptake approximately 3–4 times higher than in yeast or *E. coli*, and high glycolytic flux is strongly linked to ethanol production. (frohwitter2024anewzymomonas pages 1-2) | **Strong, taxon-specific.** |
| 15 | *Z. mobilis* `pdc` (ZMO1360) — **enables** → pyruvate-to-acetaldehyde flux | Same 2024 study: PDC is the key enzyme “converting pyruvate to acetaldehyde”; complete deletion in wild type proved difficult. (frohwitter2024anewzymomonas pages 1-2) | **Strong.** Essentiality is still better encoded as “widely considered/experimentally difficult to delete,” not absolute. |
| 16 | reduced *Z. mobilis* PDC expression — **decreases ethanol branch and permits redirection toward** → lactate or alanine | In the inducible platform, reducing PDC and expressing heterologous LDH or alanine dehydrogenase redirected pyruvate; a prior inducible construction reduced PDC activity 15-fold, and LDH expression produced lactate at about 70% of theoretical maximum. (frohwitter2024anewzymomonas pages 1-2) | **Strong engineering perturbation**, not a native trait edge. |
| 17 | anaerobiosis in stationary-phase *Z. mobilis* ZM4 — **increases transcripts of** → ED genes and `pdc` | DOI [10.1186/1471-2164-10-34](https://doi.org/10.1186/1471-2164-10-34), published 20 Jan 2009: `glk`, `zwf`, `pgl`, `pgk`, `eno`, and `pdc` transcripts were at least 30-fold more abundant anaerobically by qPCR. (yang2009transcriptomicandmetabolomic pages 1-2) | **Conditional:** stationary phase and strain ZM4. Transcript abundance is not itself flux. |
| 18 | oxygen in *Z. mobilis* fermentation — **reduces** → ethanol accumulation | At 26 h, aerobic ethanol was only 1.7% of the anaerobic amount. (yang2009transcriptomicandmetabolomic pages 1-2) | **Strong assay-specific quantitative edge.** |
| 19 | oxygen in *Z. mobilis* fermentation — **increases accumulation of** → acetate, lactate, acetoin, and acetaldehyde | Aerobic cultures accumulated greater amounts of acetate, lactate, and acetoin; background text also reports acetaldehyde accumulation under oxygen. (yang2009transcriptomicandmetabolomic pages 1-2) | **Strong but condition-specific.** |
| 20 | benzoic acid at 1.2 g/L — **inhibits** → glycolysis and sugar utilization | DOI [10.1038/s41598-024-80484-1](https://doi.org/10.1038/s41598-024-80484-1), published Nov 2024: glycolysis and sugar-metabolism genes were downregulated, and the authors concluded that benzoic acid inhibited glycolysis, sugar uptake/utilization, and ATP supply. (xiufeng2024responsemechanismof pages 1-2) | **Conditional:** *S. cerevisiae* GJ2008, 250 g/L sucrose assay. |
| 21 | benzoic acid at 1.2 g/L — **reduces** → ethanol concentration and fermentation efficiency | Same study reports high residual sugar, low ethanol concentration, and low fermentation efficiency, alongside increased membrane permeability and macromolecule leakage. (xiufeng2024responsemechanismof pages 1-2) | **Strong assay-specific inhibitor edge.** |
| 22 | benzoic acid stress — **increases** → intracellular glycerol | Same study: cells “significantly increasing the intracellular glycerol content.” (xiufeng2024responsemechanismof pages 1-2) | **Conditional adaptive response**, potentially a competing redox/osmoprotection node. |
| 23 | alternative PFL/POR route — **produces** → acetyl-CoA from pyruvate | DOI [10.3390/biom3030578](https://doi.org/10.3390/biom3030578): pyruvate is oxidized to acetyl-CoA by POR or PFL in alternative ethanol pathways. (eram2013decarboxylationofpyruvate pages 1-3) | **Strong pathway-boundary edge.** Keep in a separate module. |
| 24 | CoA-acetylating acetaldehyde dehydrogenase (`mhpF`/`adhE`-associated) — **reduces** → acetyl-CoA to acetaldehyde | Same source explicitly states that AcDH catalyzes acetyl-CoA reduction to acetaldehyde in mesophilic organisms. (eram2013decarboxylationofpyruvate pages 1-3) | **Strong alternative-route edge**, taxon dependent. |
| 25 | ethanol as sole carbon source — **induces/selects** → oxidative ADH function | The 2023 fungal review distinguishes fermentative ADH produced on sugar from oxidative ADH produced on ethanol and repressed by glucose/sucrose in *Neurospora crassa*. (gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5) | **Boundary warning:** do not curate as an ethanol-production edge. |

The compact graph-ready subset is summarized here:

| subject | predicate | object | scope/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| Glycolysis | produces | pyruvate + NADH | yeasts, especially *Saccharomyces cerevisiae* | strong | 10.3389/fmolb.2014.00017 (pfeiffer2014anevolutionaryperspective pages 1-2) |
| Pyruvate decarboxylase (PDC; EC 4.1.1.1) | converts | pyruvate → acetaldehyde + CO2 | canonical ethanologenic route; strong in *S. cerevisiae* and *Zymomonas mobilis* | strong | 10.1002/(sici)1097-0061(199612)12:16<1607::aid-yea70>3.0.co;2-4 (pronk1996pyruvatemetabolismin pages 6-8), 10.1186/s12934-024-02419-9 (frohwitter2024anewzymomonas pages 1-2) |
| Alcohol dehydrogenase (ADH) | converts | acetaldehyde + NADH → ethanol + NAD+ | canonical ethanologenic route; fungal fermentative ADHs | strong | 10.3389/fmolb.2014.00017 (pfeiffer2014anevolutionaryperspective pages 1-2), 10.3390/cells12182239 (gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5) |
| ADH-mediated ethanol formation | regenerates | NAD+ | yeasts; supports anaerobic alcoholic fermentation | strong | 10.3389/fmolb.2014.00017 (pfeiffer2014anevolutionaryperspective pages 1-2), 10.3390/cells12182239 (gutierrezcorona2023fungalalcoholdehydrogenases pages 8-10) |
| NAD+ regeneration by alcoholic fermentation | enables continuation of | glycolysis in absence of oxygen | yeasts | strong | 10.3389/fmolb.2014.00017 (pfeiffer2014anevolutionaryperspective pages 1-2) |
| Low oxygen / restricted respiration | shifts flux toward | fermentative pathway and ethanol production | *Saccharomyces cerevisiae* | strong | 10.1186/1752-0509-2-60 (jouhten2008oxygendependenceof pages 1-2) |
| Excess glucose / Crabtree effect | favors | fermentation even in presence of oxygen | Crabtree-positive yeasts, especially *S. cerevisiae* | strong | 10.3389/fmolb.2014.00017 (pfeiffer2014anevolutionaryperspective pages 1-2), 10.1186/1752-0509-2-60 (jouhten2008oxygendependenceof pages 1-2) |
| Entner-Doudoroff pathway | feeds high flux of | pyruvate/ethanol production | *Zymomonas mobilis* | strong | 10.1186/s12934-024-02419-9 (frohwitter2024anewzymomonas pages 1-2), 10.1186/1471-2164-10-34 (yang2009transcriptomicandmetabolomic pages 1-2) |
| High glycolytic flux via Entner-Doudoroff pathway | is strongly linked to | high ethanol yield and productivity | *Zymomonas mobilis* | strong | 10.1186/s12934-024-02419-9 (frohwitter2024anewzymomonas pages 1-2) |
| *Zymomonas mobilis* pdc (ZMO1360) | enables | pyruvate decarboxylation toward acetaldehyde/ethanol pathway | *Zymomonas mobilis* | strong | 10.1186/s12934-024-02419-9 (frohwitter2024anewzymomonas pages 1-2) |
| Anaerobiosis | increases expression of | ED pathway genes and pdc | *Zymomonas mobilis* | moderate | 10.1186/1471-2164-10-34 (yang2009transcriptomicandmetabolomic pages 1-2) |
| Oxygen | inhibits | ethanol fermentation performance | *Zymomonas mobilis* | strong | 10.1186/1471-2164-10-34 (yang2009transcriptomicandmetabolomic pages 1-2) |
| Oxygen | increases production of | acetate + lactate + acetoin (and lowers ethanol) | *Zymomonas mobilis* | strong | 10.1186/1471-2164-10-34 (yang2009transcriptomicandmetabolomic pages 1-2) |
| Benzoic acid stress (1.2 g/L) | inhibits | glycolysis | *Saccharomyces cerevisiae* in molasses/sucrose fermentation assay | strong, assay-specific | 10.1038/s41598-024-80484-1 (xiufeng2024responsemechanismof pages 1-2) |
| Benzoic acid stress (1.2 g/L) | reduces | ethanol concentration / fermentation efficiency | *Saccharomyces cerevisiae* in molasses/sucrose fermentation assay | strong, assay-specific | 10.1038/s41598-024-80484-1 (xiufeng2024responsemechanismof pages 1-2) |
| Reduced PDC expression (inducible promoter replacement) | redirects pyruvate toward | lactate or alanine production | engineered *Zymomonas mobilis* platform strain; not native trait edge | strong, engineering-specific | 10.1186/s12934-024-02419-9 (frohwitter2024anewzymomonas pages 1-2) |


*Table: This table summarizes the strongest literature-backed causal edges for microbial ethanol fermentation, emphasizing canonical biochemical steps and major environmental or engineering perturbations. It is useful as a compact starting set for TraitMech graph curation, with taxon-specific and assay-specific edges clearly labeled.*

## Recommended minimal TraitMech graph

For a conservative first revision of `ethanol_fermentation.yaml`, retain a taxon-neutral biochemical core and attach organism-specific modules separately:

1. glucose/sugar — **catabolized by** → glycolysis or ED pathway;
2. glycolysis/ED pathway — **produces** → pyruvate;
3. glycolysis/ED pathway — **reduces** → NAD⁺ to NADH;
4. PDC — **decarboxylates** → pyruvate to acetaldehyde + CO₂;
5. TPP — **is cofactor for** → PDC;
6. ADH — **reduces** → acetaldehyde to ethanol;
7. ADH reaction — **oxidizes** → NADH to NAD⁺;
8. NAD⁺ regeneration — **supports** → continued glycolytic flux;
9. glycolysis — **generates** → ATP by substrate-level phosphorylation;
10. ethanol — **is terminal fermentation product of** → the pathway.

Attach two optional modules:

- **Yeast module:** `PDC1/PDC5/PDC6`, fermentative ADH, cytosol, low oxygen, high-glucose/Crabtree effect, glycerol competition.
- ***Z. mobilis* module:** ED pathway, `pdc`/ZMO1360, `adhB` after accession validation, high glucose flux, anaerobic preference, oxygen-associated acetate/lactate/acetoin formation.

## Recent developments and applications

### 2023–2024 research

- A 2024 *Z. mobilis* platform study replaced the native `pdc` promoter with an IPTG-inducible promoter, making pyruvate decarboxylase flux controllable. The study demonstrates causality particularly well: suppressing the ethanol gateway allowed heterologous lactate- and alanine-forming pathways to capture pyruvate. Wild-type *Z. mobilis* reached up to 98% of maximum glucose-to-ethanol yield, while its ED pathway supported glucose uptake about 3–4 times higher than yeast or *E. coli*. (frohwitter2024anewzymomonas pages 1-2)
- A 2023 cell-free *Z. mobilis* study found that adding NAD⁺ at 1 M glucose did not improve ethanol-production efficiency; an ADP/ATP imbalance, rather than NAD⁺ availability, emerged as the controlling factor. The extract reached 100% of theoretical yield from 0.01 M sodium gluconate, a substrate intact *Z. mobilis* cannot consume. This cautions against representing all process limitations as cofactor shortage. (aminian2023investigatingethanolproduction pages 1-2)
- A 2024 *S. cerevisiae* molasses study identified benzoic acid as a process-relevant inhibitor. At 1.2 g/L benzoic acid and 250 g/L sucrose, cells showed depressed ethanol performance, glycolytic downregulation, membrane damage, and increased glycerol. This provides a strong assay-specific environmental branch for industrial molasses fermentation. (xiufeng2024responsemechanismof pages 1-2)
- A 2023 fungal ADH review emphasizes that ADH gene number, directionality, regulation, and physiological role vary substantially among fungi. For example, deleting *Mucor lusitanicus* `adh1` reduced ethanol production by 85–90%, but the same protein can act fermentatively or oxidatively depending on nutritional conditions. The expert implication is that genotype-to-trait inference must include reaction direction and assay context. (gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5)

### Current implementations

Ethanol fermentation is implemented at scale in brewing, winemaking, distilled beverages, bread leavening, first-generation bioethanol from sucrose- or starch-rich feedstocks, and increasingly in lignocellulosic or waste-feedstock processes. *S. cerevisiae* remains the principal industrial catalyst; *Z. mobilis* is attractive because of its high ED flux, high yield, ethanol tolerance, and productivity. Reported *Z. mobilis* benchmarks include tolerance up to 85 g/L ethanol in continuous culture and 127 g/L in batch culture, with 120–200 g/L/h productivity reported in cell-recycle continuous processes. These are literature benchmarks, not universal strain specifications. (yang2009transcriptomicandmetabolomic pages 1-2)

The same graph is also relevant to human-associated microbial ethanol production, food spoilage, and disease-mechanism research, but such applications require organism-resolved evidence because many gut microbes use mixed or alternative pathways.

## Expert synthesis

The most defensible causal backbone is **reaction-level rather than gene-presence-level**. PDC establishes the direct pyruvate-to-acetaldehyde gateway, while fermentative ADH closes redox balance by regenerating NAD⁺. Environment controls pathway flux differently across taxa: low oxygen and high glucose favor fermentation in *S. cerevisiae*, whereas substantial oxygen strongly depresses ethanol accumulation and increases byproducts in *Z. mobilis*. (pfeiffer2014anevolutionaryperspective pages 1-2, jouhten2008oxygendependenceof pages 1-2, yang2009transcriptomicandmetabolomic pages 1-2)

The graph should therefore separate:

- **necessary chemistry**: pyruvate, PDC, acetaldehyde, ADH, NADH/NAD⁺, ethanol, CO₂;
- **upstream energy module**: glycolysis or ED pathway and substrate-level phosphorylation;
- **conditional regulators**: oxygen, glucose excess, inhibitors, growth phase, and strain background;
- **competing sinks**: respiration, glycerol, lactate, acetate, acetoin, alanine, and biosynthesis;
- **alternative architectures**: acetyl-CoA/AcDH/AdhE routes.

## Warnings: claims not yet ready for curation

1. **Do not assert that all ethanol-producing microbes use PDC.** `adhE`/AcDH and POR/PFL-dependent architectures are genuine alternatives. (eram2013decarboxylationofpyruvate pages 1-3)
2. **Do not infer the trait from an `adh` homolog alone.** ADH may oxidize ethanol, serve other alcohol substrates, or function in morphology/pathogenesis. (gutierrezcorona2023fungalalcoholdehydrogenases pages 8-10, gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5)
3. **Do not make `ADH1` or `adhB` universal.** Preserve taxon-specific gene nodes beneath a generic reaction node.
4. **Do not encode oxygen as an absolute inhibitor.** *S. cerevisiae* can ferment aerobically under glucose excess, whereas oxygen markedly suppresses ethanol in *Z. mobilis*. (pfeiffer2014anevolutionaryperspective pages 1-2, yang2009transcriptomicandmetabolomic pages 1-2)
5. **Do not encode anoxia as necessary.** It favors or necessitates fermentation in many contexts but is not part of the trait’s logical definition.
6. **Do not claim that ethanol-branch reactions directly generate ATP.** The net two ATP per glucose arise from glycolysis. (pfeiffer2014anevolutionaryperspective pages 1-2)
7. **Do not generalize numerical thresholds.** The 0.5–2.8% O₂ findings, 1.2 g/L benzoic acid, 250 g/L sucrose, and 26-hour aerobic/anaerobic comparison are assay-specific. (xiufeng2024responsemechanismof pages 1-2, jouhten2008oxygendependenceof pages 1-2, yang2009transcriptomicandmetabolomic pages 1-2)
8. **Treat `pdc` essentiality in *Z. mobilis* cautiously.** Complete deletion was historically difficult and the gene is “widely considered” essential, but inducible/complemented designs permit strong reduction. Encode dependency with provenance rather than an unqualified universal essentiality edge. (frohwitter2024anewzymomonas pages 1-2)
9. **Validate all ontology accessions before committing YAML.** In particular, exact ChEBI, Rhea, UniProt, SGD, KEGG, MetaCyc, and GO molecular-function identifiers should be checked against the repository’s pinned releases.
10. **Do not curate the 2023 cell-free bottleneck ZMO1696 as a general cellular regulator yet.** Its effect was derived in crude extract, and intact-cell physiology differs because transport, growth, and regulation are absent. (aminian2023investigatingethanolproduction pages 1-2)

## DOI-first bibliography

1. Frohwitter J, Behrendt G, Klamt S, Bettenbrock K. “A new *Zymomonas mobilis* platform strain for the efficient production of chemicals.” *Microbial Cell Factories* 23:143. Published May 2024. DOI: [10.1186/s12934-024-02419-9](https://doi.org/10.1186/s12934-024-02419-9). (frohwitter2024anewzymomonas pages 1-2)
2. Long X-F, Xu Y-L, Zhao X-M. “Response mechanism of *Saccharomyces cerevisiae* under benzoic acid stress in ethanol fermentation.” *Scientific Reports* 14:28757. Published November 2024. DOI: [10.1038/s41598-024-80484-1](https://doi.org/10.1038/s41598-024-80484-1). (xiufeng2024responsemechanismof pages 1-2)
3. Aminian A, Motamedian E. “Investigating ethanol production using the *Zymomonas mobilis* crude extract.” *Scientific Reports* 13:1165. Published January 2023. DOI: [10.1038/s41598-023-28396-4](https://doi.org/10.1038/s41598-023-28396-4). (aminian2023investigatingethanolproduction pages 1-2)
4. Gutiérrez-Corona JF et al. “Fungal Alcohol Dehydrogenases: Physiological Function, Molecular Properties, Regulation of Their Production, and Biotechnological Potential.” *Cells* 12:2239. Published September 2023. DOI: [10.3390/cells12182239](https://doi.org/10.3390/cells12182239). (gutierrezcorona2023fungalalcoholdehydrogenases pages 8-10, gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5)
5. Pfeiffer T, Morley A. “An evolutionary perspective on the Crabtree effect.” *Frontiers in Molecular Biosciences* 1:17. Published 21 October 2014. DOI: [10.3389/fmolb.2014.00017](https://doi.org/10.3389/fmolb.2014.00017). (pfeiffer2014anevolutionaryperspective pages 1-2)
6. Eram MS, Ma K. “Decarboxylation of Pyruvate to Acetaldehyde for Ethanol Production by Hyperthermophiles.” *Biomolecules* 3:578–596. Published 21 August 2013. DOI: [10.3390/biom3030578](https://doi.org/10.3390/biom3030578). (eram2013decarboxylationofpyruvate pages 3-6, eram2013decarboxylationofpyruvate pages 1-3)
7. Yang S et al. “Transcriptomic and metabolomic profiling of *Zymomonas mobilis* during aerobic and anaerobic fermentations.” *BMC Genomics* 10:34. Published 20 January 2009. DOI: [10.1186/1471-2164-10-34](https://doi.org/10.1186/1471-2164-10-34). (yang2009transcriptomicandmetabolomic pages 1-2)
8. Jouhten P et al. “Oxygen dependence of metabolic fluxes and energy generation of *Saccharomyces cerevisiae* CEN.PK113-1A.” *BMC Systems Biology* 2:60. Published 9 July 2008. DOI: [10.1186/1752-0509-2-60](https://doi.org/10.1186/1752-0509-2-60). (jouhten2008oxygendependenceof pages 1-2)
9. Pronk JT, Steensma HY, van Dijken JP. “Pyruvate Metabolism in *Saccharomyces cerevisiae*.” *Yeast* 12:1607–1633. Published December 1996. DOI: [10.1002/(SICI)1097-0061(199612)12:16%3C1607::AID-YEA70%3E3.0.CO;2-4](https://doi.org/10.1002/(SICI)1097-0061(199612)12:16%3C1607::AID-YEA70%3E3.0.CO;2-4). (pronk1996pyruvatemetabolismin pages 5-6, pronk1996pyruvatemetabolismin pages 6-8)

References

1. (pronk1996pyruvatemetabolismin pages 5-6): JACK T. PRONK, H. YDE STEENSMA, and JOHANNES P. VAN DIJKEN. Pyruvate metabolism in saccharomyces cerevisiae. Yeast, 12:1607-1633, Dec 1996. URL: https://doi.org/10.1002/(sici)1097-0061(199612)12:16<1607::aid-yea70>3.0.co;2-4, doi:10.1002/(sici)1097-0061(199612)12:16<1607::aid-yea70>3.0.co;2-4. This article has 1086 citations and is from a peer-reviewed journal.

2. (eram2013decarboxylationofpyruvate pages 3-6): Mohammad Eram and Kesen Ma. Decarboxylation of pyruvate to acetaldehyde for ethanol production by hyperthermophiles. Biomolecules, 3:578-596, Aug 2013. URL: https://doi.org/10.3390/biom3030578, doi:10.3390/biom3030578. This article has 93 citations.

3. (pfeiffer2014anevolutionaryperspective pages 1-2): Thomas Pfeiffer and Annabel Morley. An evolutionary perspective on the crabtree effect. Frontiers in Molecular Biosciences, Oct 2014. URL: https://doi.org/10.3389/fmolb.2014.00017, doi:10.3389/fmolb.2014.00017. This article has 489 citations.

4. (gutierrezcorona2023fungalalcoholdehydrogenases pages 8-10): J. Félix Gutiérrez-Corona, Gloria Angélica González-Hernández, Israel Enrique Padilla-Guerrero, Vianey Olmedo-Monfil, Ana Lilia Martínez-Rocha, J. Alberto Patiño-Medina, Víctor Meza-Carmen, and Juan Carlos Torres-Guzmán. Fungal alcohol dehydrogenases: physiological function, molecular properties, regulation of their production, and biotechnological potential. Cells, 12:2239, Sep 2023. URL: https://doi.org/10.3390/cells12182239, doi:10.3390/cells12182239. This article has 34 citations.

5. (gutierrezcorona2023fungalalcoholdehydrogenases pages 3-5): J. Félix Gutiérrez-Corona, Gloria Angélica González-Hernández, Israel Enrique Padilla-Guerrero, Vianey Olmedo-Monfil, Ana Lilia Martínez-Rocha, J. Alberto Patiño-Medina, Víctor Meza-Carmen, and Juan Carlos Torres-Guzmán. Fungal alcohol dehydrogenases: physiological function, molecular properties, regulation of their production, and biotechnological potential. Cells, 12:2239, Sep 2023. URL: https://doi.org/10.3390/cells12182239, doi:10.3390/cells12182239. This article has 34 citations.

6. (jouhten2008oxygendependenceof pages 1-2): Paula Jouhten, Eija Rintala, Anne Huuskonen, Anu Tamminen, Mervi Toivari, Marilyn Wiebe, Laura Ruohonen, Merja Penttilä, and Hannu Maaheimo. Oxygen dependence of metabolic fluxes and energy generation of saccharomyces cerevisiae cen.pk113-1a. BMC Systems Biology, 2:60-60, Jul 2008. URL: https://doi.org/10.1186/1752-0509-2-60, doi:10.1186/1752-0509-2-60. This article has 161 citations and is from a peer-reviewed journal.

7. (eram2013decarboxylationofpyruvate pages 1-3): Mohammad Eram and Kesen Ma. Decarboxylation of pyruvate to acetaldehyde for ethanol production by hyperthermophiles. Biomolecules, 3:578-596, Aug 2013. URL: https://doi.org/10.3390/biom3030578, doi:10.3390/biom3030578. This article has 93 citations.

8. (pronk1996pyruvatemetabolismin pages 6-8): JACK T. PRONK, H. YDE STEENSMA, and JOHANNES P. VAN DIJKEN. Pyruvate metabolism in saccharomyces cerevisiae. Yeast, 12:1607-1633, Dec 1996. URL: https://doi.org/10.1002/(sici)1097-0061(199612)12:16<1607::aid-yea70>3.0.co;2-4, doi:10.1002/(sici)1097-0061(199612)12:16<1607::aid-yea70>3.0.co;2-4. This article has 1086 citations and is from a peer-reviewed journal.

9. (frohwitter2024anewzymomonas pages 1-2): Jonas Frohwitter, Gerrich Behrendt, Steffen Klamt, and Katja Bettenbrock. A new zymomonas mobilis platform strain for the efficient production of chemicals. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02419-9, doi:10.1186/s12934-024-02419-9. This article has 11 citations and is from a peer-reviewed journal.

10. (yang2009transcriptomicandmetabolomic pages 1-2): Shihui Yang, Timothy J Tschaplinski, Nancy L Engle, Sue L Carroll, Stanton L Martin, Brian H Davison, Anthony V Palumbo, Miguel Rodriguez, and Steven D Brown. Transcriptomic and metabolomic profiling of zymomonas mobilis during aerobic and anaerobic fermentations. BMC Genomics, 10:34-34, Jan 2009. URL: https://doi.org/10.1186/1471-2164-10-34, doi:10.1186/1471-2164-10-34. This article has 162 citations and is from a peer-reviewed journal.

11. (xiufeng2024responsemechanismof pages 1-2): Long Xiu-Feng, Xu Yu-Lei, and Zhao Xue-Mei. Response mechanism of saccharomyces cerevisiae under benzoic acid stress in ethanol fermentation. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80484-1, doi:10.1038/s41598-024-80484-1. This article has 7 citations and is from a peer-reviewed journal.

12. (aminian2023investigatingethanolproduction pages 1-2): Amirhossein Aminian and Ehsan Motamedian. Investigating ethanol production using the zymomonas mobilis crude extract. Scientific Reports, Jan 2023. URL: https://doi.org/10.1038/s41598-023-28396-4, doi:10.1038/s41598-023-28396-4. This article has 7 citations and is from a peer-reviewed journal.