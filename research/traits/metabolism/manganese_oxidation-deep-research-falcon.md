---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:25:50.964554'
end_time: '2026-08-04T06:33:28.519475'
duration_seconds: 457.55
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: manganese oxidation
  trait_identifier: traitmech:000032
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: manganese_oxidation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV)
    oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms
    such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
  parent_traits: METPO:1000060
  synonyms: Mn(II) oxidation
  evidence_summary: 'DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology
    of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides
    via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo
    et al., "Biogenic manganese oxides", supports the formation and properties of
    bacterially produced Mn(III/IV) oxides.)'
  causal_graph_summary: 'manganese_oxidation_multicopper_oxidase: 7 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** manganese oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000032
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV) oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
- **Parent traits:** METPO:1000060
- **Synonyms:** Mn(II) oxidation
- **Existing evidence:** DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo et al., "Biogenic manganese oxides", supports the formation and properties of bacterially produced Mn(III/IV) oxides.)
- **Existing causal graph summary:** manganese_oxidation_multicopper_oxidase: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **manganese oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/manganese_oxidation.yaml`.

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
- **Trait label:** manganese oxidation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000032
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which bacteria oxidize soluble Mn(II) to insoluble Mn(III/IV) oxides, typically catalyzed by multicopper oxidases. Characteristic of organisms such as Bacillus sp. SG-1, Leptothrix, and Pseudomonas putida.
- **Parent traits:** METPO:1000060
- **Synonyms:** Mn(II) oxidation
- **Existing evidence:** DOI:10.1016/j.tim.2005.07.009:  (Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase mechanism.) | DOI:10.1146/annurev.earth.32.101802.120213:  (Tebo et al., "Biogenic manganese oxides", supports the formation and properties of bacterially produced Mn(III/IV) oxides.)
- **Existing causal graph summary:** manganese_oxidation_multicopper_oxidase: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **manganese oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/manganese_oxidation.yaml`.

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


# Curation report: microbial manganese oxidation

## Record under review

- **Trait label:** manganese oxidation
- **Trait identifier:** `traitmech:000032`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1000060`
- **Synonym:** Mn(II) oxidation

## Executive recommendation

Retain the supplied definition, but broaden “typically catalyzed by multicopper oxidases” to explicitly permit experimentally demonstrated peroxidase- and reactive-oxygen-species-mediated routes. The highest-confidence core graph is:

**soluble Mn(II) + O₂ → enzyme-bound/soluble Mn(III) → insoluble Mn(III/IV) oxide**, catalyzed in the best-resolved *Bacillus* model by the copper-containing MnxE₃F₃G complex. Spectroscopic trapping, inhibition, purified-enzyme experiments, and structural work jointly support this pathway. However, the exact tunnel-mediated binuclear-intermediate model remains structurally motivated rather than fully demonstrated (soldatova2012multicopperoxidaseinvolvement pages 1-2, butterfield2013mn(iiiii)oxidationand pages 1-1, soldatova2012multicopperoxidaseinvolvement pages 12-16, novikova2024cryoemstructureof pages 1-2).

| Candidate causal module / edge set | Strongest model taxon | Evidence type | Curation confidence | Principal DOI |
|---|---|---|---|---|
| **MnxE3F3G direct oxidation complex**: MnxG multicopper oxidase + MnxE/MnxF accessory ring; complex directly oxidizes Mn and supports biomineralization; **structure-based tunnel/intermediate details are inferential** | *Bacillus* sp. PL-12 / SG-1 lineage | Direct biochemistry + 2024 cryo-EM structure; structural mechanism partly inferred (butterfield2013mn(iiiii)oxidationand pages 1-1, novikova2024cryoemstructureof pages 1-2) | **High** for `Mnx complex enables Mn oxidation`; **Medium** for `tunnel guides binuclear intermediates` | 10.1021/jacs.3c06537 |
| **Stepwise Mn(II)→Mn(III)→Mn(IV)**: multicopper oxidase participates in both oxidation steps during MnO2 formation | *Bacillus* sp. SG-1 / PL-12 | Direct spectroscopy/biochemical evidence with trapped Mn(III) intermediate (soldatova2012multicopperoxidaseinvolvement pages 1-2, soldatova2012multicopperoxidaseinvolvement pages 12-16, butterfield2013mn(iiiii)oxidationand pages 1-1) | **High** | 10.1007/s00775-012-0928-6 |
| **c-di-GMP / PilZ / mop regulatory branch**: elevated c-di-GMP promotes mop expression and patterned biofilm Mn oxidation; PilZ-linked cascade supported, but some steps remain pathway-level | *Pseudomonas resinovorans* MOB-513 | Direct genetics, reporters, proteomics, phenotype correlation; **taxon-specific regulatory branch** (piazza2022cyclicdigmpsignaling pages 1-2, piazza2022cyclicdigmpsignaling pages 14-15) | **Medium-High** for `c-di-GMP positively regulates Mn oxidation via mop`; **Medium** for exact cascade topology | 10.1128/mbio.02734-22 |
| **RpoN / cold-tolerant Pseudomonas branch**: rpoN required for Mn oxidation in psychrotolerant isolates; oxidation retained at 4°C; broader regulatory mechanism still unresolved | *Pseudomonas* spp. DSV-1 / MS-1 | Direct transposon mutagenesis + complementation + growth/oxidation phenotypes; **taxon-specific** (jones2024isolationcharacterizationand pages 7-11, jones2024isolationcharacterizationand pages 13-15, jones2024isolationcharacterizationand pages 11-13, jones2024isolationcharacterizationand pages 2-5) | **Medium** | 10.1128/aem.00510-24 |
| **ROS indirect branch**: superoxide/peroxide chemistry can mediate Mn oxidation outside the canonical MCO route; mechanism supported mainly by review synthesis here | Diverse MnOB; no single strongest model in retrieved direct evidence | **Review-only / indirect evidence in current set**; should be curated cautiously until primary paper is added (wu2022manganesepollutionand pages 8-10) | **Low-Medium** | 10.3390/microorganisms10122411 |
| **Biogenic oxide downstream remediation effects**: Mn biooxides sorb metals and act as strong oxidants, enabling contaminant removal; this is mainly a downstream consequence of the trait, not the core oxidation mechanism | Environmental mixed systems; exemplar MnOB include *Bacillus*, *Leptothrix*, *Pseudomonas* | Authoritative review-level environmental evidence; some application framing, but mostly **downstream phenotype/effect** rather than direct causal core (tebo2004biogenicmanganeseoxides pages 19-23, tebo2004biogenicmanganeseoxides pages 8-10, tebo2004biogenicmanganeseoxides pages 1-3, tebo2004biogenicmanganeseoxides pages 31-33, wu2022manganesepollutionand pages 7-8) | **Medium** for downstream effect node; **do not overstate as universal engineered outcome** | 10.1146/annurev.earth.32.101802.120213 |


*Table: This table prioritizes major candidate causal modules for curating microbial manganese oxidation, distinguishing direct mechanistic evidence from structural inference, taxon-specific regulation, and review-only claims. It helps decide which edges are ready for TraitMech curation versus which need stronger primary support.*

## 1. Trait scope and boundaries

### 1.1 Positive scope

`traitmech:000032` should represent an **assay-observed physiological capacity of a microbe or microbial preparation to cause net oxidation of Mn(II)**. Acceptable endpoints are:

1. detectable Mn(III), including a trapped soluble or enzyme-bound intermediate;
2. formation of insoluble mixed-valence Mn(III/IV) oxides; or
3. formation of predominantly Mn(IV) oxide/mineral products.

In the canonical route, oxidation occurs as sequential one-electron steps, Mn(II)→Mn(III)→Mn(IV). Mn(III)-pyrophosphate trapping and time-resolved spectroscopy directly established the intermediate in the *Bacillus* SG-1 system; anaerobiosis and azide inhibited both oxidation stages (soldatova2012multicopperoxidaseinvolvement pages 1-2, soldatova2012multicopperoxidaseinvolvement pages 12-16). Purified recombinant MnxE/F/G material subsequently reproduced Mn(II), Mn(III), and MnO₂-forming activities (butterfield2013mn(iiiii)oxidationand pages 1-1).

The trait is not restricted to one taxon or enzyme family. Established model organisms include *Bacillus* spp. SG-1/PL-12, *Pseudomonas putida* GB-1, *Pseudomonas resinovorans* MOB-513, and *Leptothrix discophora* SS-1. A remediation review reports that microbial oxidation is several orders of magnitude faster than corresponding abiotic oxidation and identifies *Bacillus*, *Leptothrix*, and *Pseudomonas* as prominent models (wu2022manganesepollutionand pages 7-8).

### 1.2 Boundary cases

**Include, with mechanism qualifiers:**

- extracellular, cell-surface, spore-associated, or secreted enzymatic Mn oxidation;
- MCO-catalyzed oxidation using O₂;
- peroxidase-dependent oxidation where genetics or biochemistry supports the claim;
- indirect ROS-mediated oxidation when microbial production/consumption of superoxide or peroxide is causally demonstrated;
- Mn(II)→Mn(III) only, provided the endpoint is explicitly represented as partial oxidation rather than complete MnO₂ formation.

**Do not equate with the trait:**

- passive Mn adsorption or biosorption;
- intracellular Mn uptake, accumulation, tolerance, or efflux;
- microbially induced Mn carbonate precipitation;
- Mn(III/IV) reduction or Mn respiration;
- abiotic oxidation caused solely by high pH, aeration, pre-existing oxide surfaces, or chemical oxidants;
- visual brown/black precipitate without controls confirming oxidized Mn;
- contaminant adsorption or oxidation by already formed Mn biooxide—this is a downstream consequence, not manganese oxidation itself.

Indirect pathways require special care. Reviews describe superoxide oxidizing Mn(II) to Mn(III), whereas H₂O₂ can reverse net oxidation; catalase-mediated H₂O₂ removal may therefore favor accumulation of oxidized Mn. This branch is plausible but should not be merged into the Mnx mechanism (wu2022manganesepollutionand pages 8-10).

### 1.3 Assay interpretation

Suitable evidence includes leucoberbelin-blue quantification, oxidation-state spectroscopy, Mn(III)-ligand trapping, XANES/XAS, mineral characterization, and purified-enzyme kinetics. Piazza et al. used leucoberbelin blue together with genetics, reporters, proteomics, and c-di-GMP measurements (piazza2022cyclicdigmpsignaling pages 14-15). Colony darkening alone is screening evidence; pH-matched sterile controls, Mn-free controls, and oxidation-state confirmation are needed for a high-confidence trait assertion.

## 2. Candidate graph nodes

Ontology assignments below are deliberately conservative. Organism-specific proteins and complexes should remain label-only until UniProt accessions are verified against the exact strain.

### 2.1 Trait and processes

| Node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| manganese oxidation | trait/process | `traitmech:000032`; parent `METPO:1000060` | Preserve identifier verbatim. |
| oxidation–reduction process | biological process | `GO:0055114` | Broad grounding only. |
| manganese biomineralization | process | Label-only | Do not equate all biomineralization with enzymatic Mn oxidation. |
| biofilm formation | process | `GO:0042710` | Regulatory/application context, not universally required. |

### 2.2 Chemicals and mineral products

| Node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| manganese(2+) / Mn(II) | substrate | `CHEBI:29035` | Verify release/version before YAML commit. |
| manganese(3+) / Mn(III) | intermediate | Label-only pending CHEBI verification | Can be soluble, ligand-bound, or enzyme-bound. |
| manganese(IV) oxide / MnO₂ | product | Label-only pending exact CHEBI mineral mapping | Product is often poorly crystalline/mixed-valence, not ideal stoichiometric MnO₂. |
| molecular oxygen | terminal oxidant | `CHEBI:15379` | Direct MCO branch. |
| water | product | `CHEBI:15377` | Expected from MCO reduction of O₂; reaction stoichiometry should be separately curated. |
| copper ion | cofactor/nutrient | Label-only pending oxidation-state-specific mapping | Copper loading is required for MCO activity. |
| superoxide | ROS/oxidant | `CHEBI:18421` | Alternative indirect branch. |
| hydrogen peroxide | ROS/modulator | `CHEBI:16240` | Can oppose net Mn oxidation; catalase changes outcome. |
| cyclic di-GMP | second messenger | Label-only pending CHEBI verification | Taxon-specific regulatory node. |
| azide | inhibitor | Label-only pending CHEBI verification | Supports MCO/O₂ dependence but is not completely mechanism-specific. |
| pyrophosphate | trapping ligand | Label-only pending CHEBI verification | Experimental node used to stabilize Mn(III). |
| δ-MnO₂/acid birnessite-like biooxide | mineral product | Label-only | Best treated as a material class. |
| buserite; feitknechtite; todorokite | secondary minerals | Label-only | Products depend on conditions and aging; not universal endpoints. |

The primary biooxide is commonly a poorly crystalline phyllomanganate resembling δ-MnO₂ or acid birnessite. Secondary products vary with Mn(II) concentration and alteration history; therefore “birnessite-like biogenic Mn oxide” is safer than a universal, exact mineral assignment (tebo2004biogenicmanganeseoxides pages 19-23, tebo2004biogenicmanganeseoxides pages 1-3, tebo2004biogenicmanganeseoxides pages 31-33).

### 2.3 Genes, proteins, and complexes

| Candidate | Type | Taxonomic context | Status |
|---|---|---|---|
| **MnxG** | multicopper oxidase | *Bacillus* PL-12/SG-1; homologs in *Pseudomonas* | Core high-confidence enzyme; strain-specific accession needed. |
| **MnxE, MnxF** | accessory proteins | *Bacillus* PL-12 | Form alternating E₃F₃ cap on MnxG. |
| **MnxE₃F₃G (Mnx complex)** | protein complex | *Bacillus* PL-12 | Preferred core causal node. |
| **mnxDEFG operon** | gene module | *Bacillus* | Do not assume identical organization in all Mn oxidizers. |
| **McoA** | putative MCO Mn oxidase | *Pseudomonas putida* GB-1 and homologs | Taxon-specific; distinguish from MnxG. |
| **MopA / mop genes** | Mn-oxidizing heme-peroxidase family | *Pseudomonas* | Direct regulatory evidence in MOB-513; biochemical endpoint can be context dependent. |
| **MofA** | putative MCO | *Leptothrix discophora* SS-1 | Keep uncertain until direct genetic/biochemical evidence is attached. |
| **MnxS1, MnxS2, MnxR** | two-component regulatory system | *Pseudomonas* | Candidate regulatory nodes; mere homology is insufficient for edges. |
| **RpoN (σ⁵⁴)** | transcriptional sigma factor | cold-tolerant *Pseudomonas* DSV-1/MS-1 | Necessity supported by transposon disruption and complementation. |
| **PilZ-domain protein** | c-di-GMP receptor/regulator | *P. resinovorans* MOB-513 | Regulatory cascade component; exact topology requires restraint. |
| catalase | ROS-processing enzyme | ROS-mediated branch | Review-supported candidate; add primary evidence before curation. |
| thiol-disulfide isomerase/thioredoxin | accessory candidate | DSV-1/MS-1 | Mutant phenotype only; mechanism unresolved. |
| fumarate hydratase | accessory candidate | DSV-1/MS-1 | Moderate mutant effect; likely indirect physiology. |

The 2024 cryo-EM structure resolved a 138-kDa MnxG capped by three MnxE and three MnxF subunits at 3.4 Å. A tunnel passes through the MnxG–MnxE₃F₃ assembly, and its electrostatics and dimensions can accommodate proposed binuclear Mn intermediates (novikova2024cryoemstructureof pages 1-2).

### 2.4 Cellular and environmental context

- **Bacillus spore exosporium/spore surface:** high-confidence localization context for SG-1-like oxidation (butterfield2013mn(iiiii)oxidationand pages 1-1).
- **Extracellular biofilm matrix and macrocolony layers:** relevant to *P. resinovorans* MOB-513; oxide accumulation is spatially stratified (piazza2022cyclicdigmpsignaling pages 1-2).
- **Oxic or microaerobic conditions:** required in the direct O₂-dependent route; a review reports activity at ≥14% dissolved-oxygen saturation and an approximate optimum pH range of 6.5–8.5, but these should be contextual nodes, not universal thresholds (wu2022manganesepollutionand pages 8-10).
- **Cold environment/4°C:** supported for *Pseudomonas* DSV-1 and MS-1, not a defining property of manganese oxidation generally (jones2024isolationcharacterizationand pages 7-11, jones2024isolationcharacterizationand pages 13-15).
- **Groundwater filter, acid-mine drainage reactor, sediment, soil, marine water, compost:** application or habitat nodes; none is essential to the trait.

## 3. Candidate causal edges

“Snippet” below is a short evidence extract or close source-backed rendering from the retrieved full text. Confidence applies to the proposed graph edge, not the overall paper.

| # | Subject — predicate → object | Reference | Supporting snippet | Evidence note / confidence |
|---:|---|---|---|---|
| 1 | MnxE₃F₃G complex — catalyzes → Mn(II) oxidation | Butterfield et al. 2013, DOI [10.1073/pnas.1303677110](https://doi.org/10.1073/pnas.1303677110), July 2013 | “MnxE, MnxF, and MnxG proteins catalyze two-electron oxidation of Mn(II) to Mn(IV) oxides.” | Purified recombinant complex; **high**, *Bacillus*-specific (butterfield2013mn(iiiii)oxidationand pages 1-1). |
| 2 | Mn(II) — oxidized to → Mn(III) | Soldatova et al. 2012, DOI [10.1007/s00775-012-0928-6](https://doi.org/10.1007/s00775-012-0928-6), August 2012 | “Mn(III)-pyrophosphate formation” precedes MnO₂ accumulation. | Direct time-resolved trapping/spectroscopy; **high** (soldatova2012multicopperoxidaseinvolvement pages 1-2, soldatova2012multicopperoxidaseinvolvement pages 12-16). |
| 3 | Mn(III) — oxidized to → Mn(IV) oxide | Same as #2 | MCO involvement was observed “in both Mn(II) and Mn(III) oxidation during bacterial formation of MnO₂.” | Direct inhibition/kinetic evidence; **high**, although disproportionation may contribute in some conditions (soldatova2012multicopperoxidaseinvolvement pages 1-2, soldatova2012multicopperoxidaseinvolvement pages 12-16). |
| 4 | molecular oxygen — enables → MCO-mediated Mn oxidation | Soldatova et al. 2012 | “Both oxidation steps are O₂-dependent”; anaerobic conditions inhibited the process. | Direct perturbation; **high** for SG-1 assay (soldatova2012multicopperoxidaseinvolvement pages 1-2, soldatova2012multicopperoxidaseinvolvement pages 12-16). |
| 5 | azide — inhibits → MCO-mediated Mn oxidation | Soldatova et al. 2012 | Both steps were “inhibited by azide, a known MCO inhibitor.” | Pharmacological evidence; **medium-high**, because azide is not perfectly specific (soldatova2012multicopperoxidaseinvolvement pages 1-2). |
| 6 | copper loading — enables → active Mnx complex | Butterfield et al. 2013 | Active blue complex required “CuSO₄ supplementation and microaerobic conditions.” | Direct expression/purification condition; **high** in this system (butterfield2013mn(iiiii)oxidationand pages 1-1). |
| 7 | MnxE + MnxF — assemble into → MnxE₃F₃ cap on MnxG | Novikova et al. 2024, DOI [10.1021/jacs.3c06537](https://doi.org/10.1021/jacs.3c06537), July 2024 | “MnxG…capped by a heterohexameric ring of alternating MnxE and MnxF subunits.” | 3.4-Å cryo-EM/native-MS-supported structure; **high** (novikova2024cryoemstructureof pages 1-2). |
| 8 | Mnx tunnel — accommodates/guides → binuclear Mn intermediates | Novikova et al. 2024 | “Tunnel dimensions and charges can accommodate the mechanistically inferred binuclear manganese intermediates.” | **Medium/uncertain**: structural compatibility, not direct observation of substrate transit (novikova2024cryoemstructureof pages 1-2). |
| 9 | elevated c-di-GMP — increases → mop expression | Piazza et al. 2022, DOI [10.1128/mbio.02734-22](https://doi.org/10.1128/mbio.02734-22), December 2022 | Elevated c-di-GMP “upregulate[s] expression of manganese-oxidizing peroxidase (mop) genes.” | Reporter/proteomic/genetic support; **high within MOB-513**, not universal (piazza2022cyclicdigmpsignaling pages 1-2, piazza2022cyclicdigmpsignaling pages 14-15). |
| 10 | elevated c-di-GMP — increases → biogenic Mn oxide accumulation | Piazza et al. 2022 | Higher c-di-GMP correlated with increased top-layer oxide and appearance of a second bottom stratum. | Strong phenotype correlation/perturbation; **medium-high**, spatially and taxonomically specific (piazza2022cyclicdigmpsignaling pages 1-2). |
| 11 | PilZ-domain regulator — controls → mop induction/Mn oxidation | Piazza et al. 2022 | Transposon insertions upstream caused “complete loss of Mn(II) oxidation” and prevented mop7013/mop7014 induction. | Genetics and reporters; **high** for involvement, **medium** for the exact cascade topology (piazza2022cyclicdigmpsignaling pages 14-15). |
| 12 | rpoN — enables → Mn oxidation | Jones et al. 2024, DOI [10.1128/aem.00510-24](https://doi.org/10.1128/aem.00510-24), September 2024 | `rpoN::Tn5` abolished oxidation; plasmid-borne GB-1 `rpoN` restored it. | Disruption plus complementation; **high**, DSV-1/MS-1 branch only (jones2024isolationcharacterizationand pages 13-15, jones2024isolationcharacterizationand pages 11-13). |
| 13 | growth/assay at 4°C — permits → Mn oxidation by MS-1 and DSV-1 | Jones et al. 2024 | Both produced brown Mn-oxide colonies after 5 days and accumulated oxide for 10 months at 4°C. | Direct phenotype; **high**, strain-specific (jones2024isolationcharacterizationand pages 7-11). |
| 14 | cold-adapted strain background — decreases → doubling time at 4°C relative to GB-1 | Jones et al. 2024 | Doubling times: MS-1 7.5 h, DSV-1 8.1 h, GB-1 24.5 h. | Quantitative growth data; relevant environmental modifier, not core chemistry (jones2024isolationcharacterizationand pages 7-11). |
| 15 | superoxide — oxidizes → Mn(II) to Mn(III) | Wu et al. 2022, DOI [10.3390/microorganisms10122411](https://doi.org/10.3390/microorganisms10122411), December 2022 | “Superoxide…oxidizes Mn²⁺ to Mn³⁺.” | **Low-medium for immediate curation** because current retrieved support is review-level; add primary study (wu2022manganesepollutionand pages 8-10). |
| 16 | hydrogen peroxide — reduces/opposes accumulation of → Mn(III) | Wu et al. 2022 | H₂O₂ “can reduce it back”; catalase decomposition supports net oxidation. | Mechanistically important but **review-level** in this evidence set (wu2022manganesepollutionand pages 8-10). |
| 17 | Mn oxidation — produces → δ-MnO₂/acid-birnessite-like biooxide | Tebo et al. 2004, DOI [10.1146/annurev.earth.32.101802.120213](https://doi.org/10.1146/annurev.earth.32.101802.120213), May 2004 | “The primary Mn(IV) biooxide formed is a phyllomanganate most similar to δ-MnO₂ or acid birnessite.” | Authoritative synthesis; **medium-high**, product heterogeneity must be retained (tebo2004biogenicmanganeseoxides pages 1-3). |
| 18 | biogenic Mn oxide — adsorbs/sequesters → trace metals | Tebo et al. 2004 | Biooxides reduce dissolved trace metals and radionuclides “by orders of magnitude” through adsorption, ion exchange, and precipitation. | Downstream environmental effect; **high as general property**, not a core trait edge (tebo2004biogenicmanganeseoxides pages 8-10, tebo2004biogenicmanganeseoxides pages 3-6). |
| 19 | biogenic Mn oxide — oxidizes/transforms → organic and inorganic contaminants | Tebo et al. 2004 | Biooxides mediate redox reactions and can transform phenols, atrazine, PCBs, and reduced metals. | Downstream effect; direction and toxicity outcome are contaminant-specific (tebo2004biogenicmanganeseoxides pages 8-10, tebo2004biogenicmanganeseoxides pages 1-3). |
| 20 | *Leptothrix*-inoculated filtration column — increases → Mn removal | Wu et al. 2022 | “Removal efficiency reached 90% in filtration columns inoculated with *Leptothrix*.” | Application statistic from review; **medium**, retain configuration-specific provenance (wu2022manganesepollutionand pages 7-8). |

## 4. Recent developments, 2023–2024

### 4.1 First high-resolution architecture of the Mnx complex

Novikova et al. resolved the Mnx complex at 3.4 Å using cryo-EM of an H340A point mutant, supported by cross-linking MS, native MS, and AlphaFold-Multimer modeling. The structure consists of 138-kDa MnxG and an alternating MnxE₃F₃ cap; likely substrate-coordinating residues occur near the tunnel entrance. This provides the strongest current structural framework for bacterial MCO-dependent manganese biomineralization, but the proposed passage of binuclear Mn species through the tunnel awaits direct kinetic or substrate-bound structural validation (novikova2024cryoemstructureof pages 1-2).

### 4.2 Cold-active Mn-oxidizing *Pseudomonas*

Jones et al. isolated strains DSV-1 and MS-1 from Minnesota compost. Their 16S sequences were 100% identical to each other and 99.66% identical to a *P. psychrophila* type strain, but ANI was <93%, supporting an undescribed species rather than assignment to *P. psychrophila* (jones2024isolationcharacterizationand pages 1-2, jones2024isolationcharacterizationand pages 2-5). At 4°C their doubling times were 8.1 and 7.5 h, versus 24.5 h for *P. putida* GB-1; both oxidized Mn at 4°C, whereas GB-1 produced no detectable oxide under the reported comparison (jones2024isolationcharacterizationand pages 7-11).

The study recovered 13 transposon mutants with altered Mn oxidation—11 from DSV-1 and two from MS-1—including increased, decreased, and null phenotypes. The strongest new causal result is RpoN necessity, demonstrated by loss and complementation. Fumarate hydratase and thiol-disulfide-isomerase hits are useful candidates but probably represent indirect physiological support rather than Mn-specific catalysis (jones2024isolationcharacterizationand pages 13-15, jones2024isolationcharacterizationand pages 11-13).

### 4.3 Distribution of known oxidases

A 2023 in-silico study found most homologs of MnxG, McoA, MopA, and MofA in Proteobacteria, Actinobacteria, and Firmicutes. It also found many genomes containing only one candidate oxidase, arguing against a universal requirement for multiple enzymes to complete the two-electron conversion. This is hypothesis-generating genomic evidence, not proof that every homolog catalyzes manganese oxidation (kurdi2023aninsilicostudy pages 9-12).

## 5. Applications and environmental significance

Biogenic Mn oxides possess open structures, large surface areas, negative charge, exchangeable cations, and high redox activity. They can adsorb or incorporate Cu, Co, Cd, Zn, Ni, Pb, Hg, U, Pu, As, Se, and other elements; dissolved trace-metal and radionuclide concentrations may fall by orders of magnitude under favorable conditions (tebo2004biogenicmanganeseoxides pages 8-10, tebo2004biogenicmanganeseoxides pages 3-6). These properties underpin biological sand filters, groundwater treatment, acid-mine-drainage treatment, contaminant immobilization, and oxidative transformation of organic pollutants.

A review reports up to **90% Mn removal** in *Leptothrix*-inoculated filtration columns (wu2022manganesepollutionand pages 7-8). Piazza et al. further showed that manipulating c-di-GMP improved Mn-oxidizing capacity and lyophilization performance of freeze-dried MOB-513 cells, suggesting deployable bioaugmentation formulations (piazza2022cyclicdigmpsignaling pages 1-2, piazza2022cyclicdigmpsignaling pages 14-15). Cold-active MS-1 and DSV-1 potentially extend such treatment to low-temperature systems, although their performance has not yet been demonstrated in a full-scale reactor or field filter (jones2024isolationcharacterizationand pages 7-11, jones2024isolationcharacterizationand pages 1-2).

Environmental outcomes are not uniformly beneficial. Mn oxides may immobilize many metals, but oxidation can mobilize chromium or uranium, and product reactivity depends on mineral structure, Mn(III)/Mn(IV) ratio, pH, redox potential, competing ligands, and aging (tebo2004biogenicmanganeseoxides pages 8-10, tebo2004biogenicmanganeseoxides pages 3-6). These should be represented as conditional downstream effects rather than universal trait consequences.

## 6. Recommended minimal YAML graph

The first implementation should remain small and mechanistically coherent:

1. `Mn(II)` — **substrate_of** → `MnxE3F3G complex`
2. `MnxE3F3G complex` — **catalyzes** → `Mn(II) oxidation`
3. `Mn(II) oxidation` — **produces** → `Mn(III) intermediate`
4. `Mn(III) intermediate` — **oxidized_to** → `Mn(IV)-rich biogenic manganese oxide`
5. `molecular oxygen` — **required_for** → `Mnx-mediated manganese oxidation`
6. `copper cofactor` — **required_for_activity_of** → `MnxG`
7. `MnxE` + `MnxF` + `MnxG` — **forms** → `MnxE3F3G complex`
8. `MnxE3F3G complex` — **localized_to** → `Bacillus spore exosporium` [taxon-specific]

Add separate optional subgraphs for:

- `c-di-GMP → PilZ-linked regulation → mop expression → Mn oxidation` in *P. resinovorans* MOB-513;
- `RpoN → Mn oxidation` in cold-tolerant *Pseudomonas* DSV-1/MS-1;
- ROS-mediated oxidation only after primary evidence is attached.

Do not collapse MnxG, McoA, MopA, and MofA into one universal “manganese oxidase” node. Their cofactor chemistry, products, environmental optima, and genetic redundancy differ among organisms (kurdi2023aninsilicostudy pages 9-12).

## 7. Claims not yet ready for TraitMech curation

1. **Universal MCO requirement.** Some Mn oxidation appears ROS- or peroxidase-mediated, and reviews note strains without recognizable canonical MCOs (wu2022manganesepollutionand pages 8-10).
2. **Direct Mn transit through the cryo-EM tunnel.** The geometry is compatible with proposed intermediates, but substrate transit was not visualized (novikova2024cryoemstructureof pages 1-2).
3. **Universal MnxE/F necessity.** Their importance is well supported in the *Bacillus* Mnx complex but should not be projected onto unrelated taxa.
4. **MofA as definitively catalytic.** Current retrieved evidence describes it as putative; attach direct mutation or purified-protein evidence first.
5. **Homolog presence implies phenotype.** The 2023 distribution study is in silico and cannot establish enzyme activity (kurdi2023aninsilicostudy pages 9-12).
6. **MnxS1/S2/MnxR causal edges in DSV-1/MS-1.** Homologs are present, but presence alone does not establish regulation (jones2024isolationcharacterizationand pages 13-15, jones2024isolationcharacterizationand pages 1-2).
7. **Fumarate hydratase or thioredoxin as direct oxidases.** Mutant phenotypes may reflect respiration, protein maturation, or general physiology.
8. **A universal pH optimum of 6.5–8.5 or O₂ threshold of 14%.** These are review-level ranges across heterogeneous organisms, not defining thresholds (wu2022manganesepollutionand pages 8-10).
9. **Brown precipitate equals MnO₂.** Mixed-valence and secondary minerals are common; oxidation-state/mineral assays are required.
10. **Metal removal is always detoxifying.** Chromium and uranium may be mobilized by oxidation (tebo2004biogenicmanganeseoxides pages 8-10).
11. **Cold tolerance is intrinsic to the trait.** It is a strain-specific environmental modifier, not part of the class definition.
12. **Full-scale implementation for DSV-1/MS-1.** Their application is prospective; current evidence is laboratory-based.

## 8. DOI-first bibliography

1. **Novikova IV et al.** “Cryo-EM Structure of the Mnx Protein Complex Reveals a Tunnel Framework for the Mechanism of Manganese Biomineralization.” *Journal of the American Chemical Society* 146, 22950–22958. **July 2024.** DOI: [10.1021/jacs.3c06537](https://doi.org/10.1021/jacs.3c06537) (novikova2024cryoemstructureof pages 1-2).
2. **Jones I et al.** “Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing *Pseudomonas* sp. strains.” *Applied and Environmental Microbiology* 90. **September 2024.** DOI: [10.1128/aem.00510-24](https://doi.org/10.1128/aem.00510-24) (jones2024isolationcharacterizationand pages 7-11, jones2024isolationcharacterizationand pages 1-2, jones2024isolationcharacterizationand pages 11-13).
3. **Kurdi MZ, Olichney J, Geszvain K.** “An in-Silico Study of the Distribution of Mn Oxidation Proteins in Sequenced Bacterial Genomes.” Research Square preprint. **January 2023.** DOI: [10.21203/rs.3.rs-2451893/v1](https://doi.org/10.21203/rs.3.rs-2451893/v1) (kurdi2023aninsilicostudy pages 9-12).
4. **Piazza A et al.** “Cyclic di-GMP Signaling Links Biofilm Formation and Mn(II) Oxidation in *Pseudomonas resinovorans*.” *mBio* 13. **December 2022.** DOI: [10.1128/mbio.02734-22](https://doi.org/10.1128/mbio.02734-22) (piazza2022cyclicdigmpsignaling pages 1-2, piazza2022cyclicdigmpsignaling pages 14-15).
5. **Wu R et al.** “Manganese Pollution and Its Remediation: A Review of Biological Removal and Promising Combination Strategies.” *Microorganisms* 10:2411. **December 2022.** DOI: [10.3390/microorganisms10122411](https://doi.org/10.3390/microorganisms10122411) (wu2022manganesepollutionand pages 8-10, wu2022manganesepollutionand pages 7-8).
6. **Butterfield CN et al.** “Mn(II,III) oxidation and MnO₂ mineralization by an expressed bacterial multicopper oxidase.” *PNAS* 110:11731–11735. **July 2013.** DOI: [10.1073/pnas.1303677110](https://doi.org/10.1073/pnas.1303677110) (butterfield2013mn(iiiii)oxidationand pages 1-1).
7. **Soldatova AV et al.** “Multicopper oxidase involvement in both Mn(II) and Mn(III) oxidation during bacterial formation of MnO₂.” *Journal of Biological Inorganic Chemistry* 17:1151–1158. **August 2012.** DOI: [10.1007/s00775-012-0928-6](https://doi.org/10.1007/s00775-012-0928-6) (soldatova2012multicopperoxidaseinvolvement pages 1-2, soldatova2012multicopperoxidaseinvolvement pages 12-16).
8. **Tebo BM et al.** “Biogenic Manganese Oxides: Properties and Mechanisms of Formation.” *Annual Review of Earth and Planetary Sciences* 32:287–328. **May 2004.** DOI: [10.1146/annurev.earth.32.101802.120213](https://doi.org/10.1146/annurev.earth.32.101802.120213) (tebo2004biogenicmanganeseoxides pages 19-23, tebo2004biogenicmanganeseoxides pages 1-3, tebo2004biogenicmanganeseoxides pages 3-6).

## Curation conclusion

The most defensible initial TraitMech graph is the *Bacillus* Mnx-dependent, O₂- and copper-requiring, stepwise Mn(II)→Mn(III)→Mn(IV)-rich oxide mechanism. Regulatory branches involving c-di-GMP/PilZ/Mop and RpoN should be represented as explicitly taxon-specific extensions. ROS chemistry, exact tunnel transit, MofA catalysis, environmental thresholds, and application outcomes require either additional primary evidence or uncertainty annotations before inclusion in `data/traits/metabolism/manganese_oxidation.yaml`.

References

1. (soldatova2012multicopperoxidaseinvolvement pages 1-2): Alexandra V. Soldatova, Cristina Butterfield, Oyeyemi F. Oyerinde, Bradley M. Tebo, and Thomas G. Spiro. Multicopper oxidase involvement in both mn(ii) and mn(iii) oxidation during bacterial formation of mno2. JBIC Journal of Biological Inorganic Chemistry, 17:1151-1158, Aug 2012. URL: https://doi.org/10.1007/s00775-012-0928-6, doi:10.1007/s00775-012-0928-6. This article has 93 citations.

2. (butterfield2013mn(iiiii)oxidationand pages 1-1): Cristina N. Butterfield, Alexandra V. Soldatova, Sung-Woo Lee, Thomas G. Spiro, and Bradley M. Tebo. Mn(ii,iii) oxidation and mno2 mineralization by an expressed bacterial multicopper oxidase. Proceedings of the National Academy of Sciences, 110:11731-11735, Jul 2013. URL: https://doi.org/10.1073/pnas.1303677110, doi:10.1073/pnas.1303677110. This article has 223 citations and is from a highest quality peer-reviewed journal.

3. (soldatova2012multicopperoxidaseinvolvement pages 12-16): Alexandra V. Soldatova, Cristina Butterfield, Oyeyemi F. Oyerinde, Bradley M. Tebo, and Thomas G. Spiro. Multicopper oxidase involvement in both mn(ii) and mn(iii) oxidation during bacterial formation of mno2. JBIC Journal of Biological Inorganic Chemistry, 17:1151-1158, Aug 2012. URL: https://doi.org/10.1007/s00775-012-0928-6, doi:10.1007/s00775-012-0928-6. This article has 93 citations.

4. (novikova2024cryoemstructureof pages 1-2): Irina V. Novikova, Alexandra V. Soldatova, Trevor H. Moser, Stephanie M. Thibert, Christine A. Romano, Mowei Zhou, Bradley M. Tebo, James E. Evans, and Thomas G. Spiro. Cryo-em structure of the mnx protein complex reveals a tunnel framework for the mechanism of manganese biomineralization. Journal of the American Chemical Society, 146:22950-22958, Jul 2024. URL: https://doi.org/10.1021/jacs.3c06537, doi:10.1021/jacs.3c06537. This article has 8 citations and is from a highest quality peer-reviewed journal.

5. (piazza2022cyclicdigmpsignaling pages 1-2): Ainelén Piazza, Lucia Parra, Lucila Ciancio Casalini, Federico Sisti, Julieta Fernández, Jacob G. Malone, Jorgelina Ottado, Diego O. Serra, and Natalia Gottig. Cyclic di-gmp signaling links biofilm formation and mn(ii) oxidation in pseudomonas resinovorans. Dec 2022. URL: https://doi.org/10.1128/mbio.02734-22, doi:10.1128/mbio.02734-22. This article has 15 citations and is from a domain leading peer-reviewed journal.

6. (piazza2022cyclicdigmpsignaling pages 14-15): Ainelén Piazza, Lucia Parra, Lucila Ciancio Casalini, Federico Sisti, Julieta Fernández, Jacob G. Malone, Jorgelina Ottado, Diego O. Serra, and Natalia Gottig. Cyclic di-gmp signaling links biofilm formation and mn(ii) oxidation in pseudomonas resinovorans. Dec 2022. URL: https://doi.org/10.1128/mbio.02734-22, doi:10.1128/mbio.02734-22. This article has 15 citations and is from a domain leading peer-reviewed journal.

7. (jones2024isolationcharacterizationand pages 7-11): Ian Jones, Duncan Vermillion, Chase Tracy, Robert Denton, Rick Davis, and Kati Geszvain. Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing <i>pseudomonas</i> sp. strains. Sep 2024. URL: https://doi.org/10.1128/aem.00510-24, doi:10.1128/aem.00510-24. This article has 4 citations and is from a peer-reviewed journal.

8. (jones2024isolationcharacterizationand pages 13-15): Ian Jones, Duncan Vermillion, Chase Tracy, Robert Denton, Rick Davis, and Kati Geszvain. Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing <i>pseudomonas</i> sp. strains. Sep 2024. URL: https://doi.org/10.1128/aem.00510-24, doi:10.1128/aem.00510-24. This article has 4 citations and is from a peer-reviewed journal.

9. (jones2024isolationcharacterizationand pages 11-13): Ian Jones, Duncan Vermillion, Chase Tracy, Robert Denton, Rick Davis, and Kati Geszvain. Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing <i>pseudomonas</i> sp. strains. Sep 2024. URL: https://doi.org/10.1128/aem.00510-24, doi:10.1128/aem.00510-24. This article has 4 citations and is from a peer-reviewed journal.

10. (jones2024isolationcharacterizationand pages 2-5): Ian Jones, Duncan Vermillion, Chase Tracy, Robert Denton, Rick Davis, and Kati Geszvain. Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing <i>pseudomonas</i> sp. strains. Sep 2024. URL: https://doi.org/10.1128/aem.00510-24, doi:10.1128/aem.00510-24. This article has 4 citations and is from a peer-reviewed journal.

11. (wu2022manganesepollutionand pages 8-10): Rongrong Wu, Fangting Yao, Xiaoya Li, Chongjing Shi, Xue Zang, Xiao Shu, Hengwei Liu, and Wenchao Zhang. Manganese pollution and its remediation: a review of biological removal and promising combination strategies. Microorganisms, 10:2411, Dec 2022. URL: https://doi.org/10.3390/microorganisms10122411, doi:10.3390/microorganisms10122411. This article has 108 citations.

12. (tebo2004biogenicmanganeseoxides pages 19-23): Bradley M. Tebo, John R. Bargar, Brian G. Clement, Gregory J. Dick, Karen J. Murray, Dorothy Parker, Rebecca Verity, and Samuel M. Webb. Biogenic manganese oxides: properties and mechanisms of formation. May 2004. URL: https://doi.org/10.1146/annurev.earth.32.101802.120213, doi:10.1146/annurev.earth.32.101802.120213. This article has 1724 citations and is from a highest quality peer-reviewed journal.

13. (tebo2004biogenicmanganeseoxides pages 8-10): Bradley M. Tebo, John R. Bargar, Brian G. Clement, Gregory J. Dick, Karen J. Murray, Dorothy Parker, Rebecca Verity, and Samuel M. Webb. Biogenic manganese oxides: properties and mechanisms of formation. May 2004. URL: https://doi.org/10.1146/annurev.earth.32.101802.120213, doi:10.1146/annurev.earth.32.101802.120213. This article has 1724 citations and is from a highest quality peer-reviewed journal.

14. (tebo2004biogenicmanganeseoxides pages 1-3): Bradley M. Tebo, John R. Bargar, Brian G. Clement, Gregory J. Dick, Karen J. Murray, Dorothy Parker, Rebecca Verity, and Samuel M. Webb. Biogenic manganese oxides: properties and mechanisms of formation. May 2004. URL: https://doi.org/10.1146/annurev.earth.32.101802.120213, doi:10.1146/annurev.earth.32.101802.120213. This article has 1724 citations and is from a highest quality peer-reviewed journal.

15. (tebo2004biogenicmanganeseoxides pages 31-33): Bradley M. Tebo, John R. Bargar, Brian G. Clement, Gregory J. Dick, Karen J. Murray, Dorothy Parker, Rebecca Verity, and Samuel M. Webb. Biogenic manganese oxides: properties and mechanisms of formation. May 2004. URL: https://doi.org/10.1146/annurev.earth.32.101802.120213, doi:10.1146/annurev.earth.32.101802.120213. This article has 1724 citations and is from a highest quality peer-reviewed journal.

16. (wu2022manganesepollutionand pages 7-8): Rongrong Wu, Fangting Yao, Xiaoya Li, Chongjing Shi, Xue Zang, Xiao Shu, Hengwei Liu, and Wenchao Zhang. Manganese pollution and its remediation: a review of biological removal and promising combination strategies. Microorganisms, 10:2411, Dec 2022. URL: https://doi.org/10.3390/microorganisms10122411, doi:10.3390/microorganisms10122411. This article has 108 citations.

17. (tebo2004biogenicmanganeseoxides pages 3-6): Bradley M. Tebo, John R. Bargar, Brian G. Clement, Gregory J. Dick, Karen J. Murray, Dorothy Parker, Rebecca Verity, and Samuel M. Webb. Biogenic manganese oxides: properties and mechanisms of formation. May 2004. URL: https://doi.org/10.1146/annurev.earth.32.101802.120213, doi:10.1146/annurev.earth.32.101802.120213. This article has 1724 citations and is from a highest quality peer-reviewed journal.

18. (jones2024isolationcharacterizationand pages 1-2): Ian Jones, Duncan Vermillion, Chase Tracy, Robert Denton, Rick Davis, and Kati Geszvain. Isolation, characterization, and genetic manipulation of cold-tolerant, manganese-oxidizing <i>pseudomonas</i> sp. strains. Sep 2024. URL: https://doi.org/10.1128/aem.00510-24, doi:10.1128/aem.00510-24. This article has 4 citations and is from a peer-reviewed journal.

19. (kurdi2023aninsilicostudy pages 9-12): M. Zakaria Kurdi, Jacob Olichney, and Kati Geszvain. An in-silico study of the distribution of mn oxidation proteins in sequenced bacterial genomes. Unknown journal, Jan 2023. URL: https://doi.org/10.21203/rs.3.rs-2451893/v1, doi:10.21203/rs.3.rs-2451893/v1.