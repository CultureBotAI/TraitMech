---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:11:30.078868'
end_time: '2026-08-04T11:22:27.398011'
duration_seconds: 657.32
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: hydrogenotrophic
  trait_identifier: METPO:1000646
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: hydrogenotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses molecular hydrogen as an electron
    donor for energy generation and carbon dioxide as the primary carbon source.
  parent_traits: METPO:1000631
  synonyms: ''
  evidence_summary: 'DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas
    (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.)
    | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation
    into cellular carbon in autotrophic metabolism.)'
  causal_graph_summary: 'hydrogenotrophic_hydrogen_oxidation_fixation: 14 nodes, 14
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** hydrogenotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000646
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses molecular hydrogen as an electron donor for energy generation and carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.) | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation into cellular carbon in autotrophic metabolism.)
- **Existing causal graph summary:** hydrogenotrophic_hydrogen_oxidation_fixation: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **hydrogenotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/hydrogenotrophic.yaml`.

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
- **Trait label:** hydrogenotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000646
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses molecular hydrogen as an electron donor for energy generation and carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.21775/cimb.006.159: reversible oxidation of hydrogen gas (Review supports hydrogenase-catalyzed H2 oxidation and microbial energy metabolism.) | DOI:10.1128/AEM.02473-10: assimilation of CO2 (Review supports CO2 assimilation into cellular carbon in autotrophic metabolism.)
- **Existing causal graph summary:** hydrogenotrophic_hydrogen_oxidation_fixation: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **hydrogenotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/hydrogenotrophic.yaml`.

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


# Curation report: hydrogenotrophic microbial physiology

## Executive scope

**Target:** `METPO:1000646` (“hydrogenotrophic”), category **PHYSIOLOGY**, term kind **CLASS**, mapping **REVIEWED**. The supplied definition—use of molecular hydrogen as electron donor for energy generation and CO2 as the primary carbon source—is appropriately **stricter than “H2 oxidizing.”** A defensible TraitMech graph should therefore require two linked capacities:

1. **H2 oxidation/electron transfer**, and
2. **predominantly inorganic-carbon assimilation**, usually through the Calvin–Benson–Bassham (CBB) cycle or reductive Wood–Ljungdahl pathway (WLP).

Hydrogenotrophy is not one pathway. It is a trophic architecture realized in aerobic Knallgas bacteria, anaerobic acetogens, hydrogenotrophic methanogens, and some nitrate- or sulfate-reducing autotrophs. Uptake hydrogenases oxidize H2 and route electrons to respiratory chains or soluble carriers; the resulting reducing power and chemiosmotic energy support CO2 fixation and growth. Hydrogenotrophic methanogens and acetogens additionally use CO2 as a catabolic electron acceptor, producing methane or acetate, respectively (culp2023crossfeedinginthe pages 7-9, pichechoquette2019molecularhydrogena pages 8-9, pichechoquette2019molecularhydrogena pages 6-8).

## 1. Trait boundaries

### Include

* Demonstrated growth with **H2 as principal electron donor** and **CO2/bicarbonate as principal carbon source**.
* Facultative organisms, such as *Cupriavidus necator*, when assayed specifically under H2–CO2 autotrophic conditions. *C. necator* uses H2 and CO2 as sole energy and carbon sources and encodes soluble and membrane-bound uptake hydrogenases plus a branched respiratory chain (cramm2009genomicviewof pages 1-2).
* Obligately or facultatively autotrophic acetogens growing by H2-dependent WLP activity. The 2023 description of *Aceticella autotrophica* reports obligate autotrophic acetogenic growth and the reaction `4 H2 + 2 CO2 → acetate + H+ + 2 H2O`, with ΔG°′ approximately −104 kJ per reaction as represented by the authors (frolov2023obligateautotrophyat pages 1-2).
* Methanogens performing `4 H2 + CO2 → CH4 + 2 H2O` while assimilating inorganic carbon (culp2023crossfeedinginthe pages 7-9, pichechoquette2019molecularhydrogena pages 8-9).

### Exclude or annotate as boundary cases

* **Hydrogen oxidation without autotrophy.** H2-supported fumarate, nitrate, or sulfate respiration is not by itself sufficient if biomass carbon comes predominantly from organics.
* **Atmospheric-H2 scavenging for persistence or mixotrophy.** High-affinity H2 oxidizers account for about 70% of atmospheric H2 uptake in soils, but atmospheric H2 is generally insufficient to sustain growth; many use it as ancillary maintenance energy. This is “H2 scavenging/mixotrophy,” not strict hydrogenotrophy unless CO2-primary growth is shown (pichechoquette2019molecularhydrogena pages 11-13).
* **Hydrogenogenic organisms.** Microbes producing H2 through fermentation, nitrogenase, or reversible hydrogenases have the opposite net flux and should not inherit the trait on that basis.
* **Hydrogen-dependent methylotrophic methanogenesis.** H2 reduces a methyl compound, but CO2 is not necessarily the primary carbon substrate or catabolic acceptor; curate separately unless autotrophic CO2 assimilation is demonstrated.
* **CO or formate utilization.** Acetogens and methanogens may use these substrates, but that does not establish H2 dependence. Syngas cultures containing CO/H2/CO2 are especially ambiguous because CO can supply both carbon and electrons (neto2024exploringthepotential pages 1-2).
* **Genomic potential alone.** A hydrogenase plus a carbon-fixation pathway supports a prediction, not an observed phenotype. Form-IV Rubisco-like proteins are not evidence of a functional CBB cycle; absence of phosphoribulokinase and the Rubisco small subunit can argue against CBB function (jiao2021insightintothe pages 6-7).

## 2. Candidate graph nodes

Identifiers below are restricted to high-confidence CURIEs. Labels are deliberately retained where an exact database identifier was not verified.

### Trait and processes

| Candidate node | Grounding | Curation note |
|---|---|---|
| hydrogenotrophic | `METPO:1000646` | Target trait; quote CURIE verbatim in YAML |
| parent trait | `METPO:1000631` | Supplied parent |
| molecular-hydrogen oxidation | Label only | Net H2-consuming process |
| chemolithoautotrophic growth | Label only | Assay-level phenotype |
| CBB-cycle CO2 fixation | Label only | Principal aerobic/Knallgas branch |
| reductive Wood–Ljungdahl pathway | Label only | Acetogenic and methanogenic carbon branch |
| hydrogenotrophic methanogenesis | Label only | H2-dependent CO2 reduction to methane |
| homoacetogenesis | Label only | H2-dependent CO2 reduction to acetate |
| hydrogenotrophic respiration | Label only | Must be paired with autotrophic carbon assimilation |
| oxidative phosphorylation | Label only | Respiratory energy-conservation module |
| flavin-based electron bifurcation | Label only | Important in HydABC and methanogenic systems |

### Chemicals and physicochemical entities

| Node | Suggested grounding |
|---|---|
| molecular hydrogen | `CHEBI:18276` |
| carbon dioxide | `CHEBI:16526` |
| water | `CHEBI:15377` |
| dioxygen | `CHEBI:15379` |
| methane | `CHEBI:16183` |
| acetate | `CHEBI:30089` |
| nitrate | `CHEBI:17632` |
| sulfate | `CHEBI:16189` |
| proton | `CHEBI:15378` |
| ATP | `CHEBI:15422` |
| NAD+ / NADH | `CHEBI:15846` / `CHEBI:16908` |
| ferredoxin, reduced ferredoxin | Label only pending exact protein/context grounding |
| sodium ion, proton-motive force, sodium-motive force | Label only pending validation |
| bicarbonate, formate, sulfide, fumarate, succinate | Candidate chemicals; verify exact CURIEs during implementation |

### Enzymes, genes, and complexes

* **Uptake [NiFe]-hydrogenase**, including membrane-bound hydrogenase (MBH): core H2-oxidation entry module.
* **Soluble [NiFe]-hydrogenase (SH):** couples H2 oxidation to NAD reduction in *C. necator* and related organisms (pichechoquette2019molecularhydrogena pages 9-11).
* **Group 2b regulatory/sensor hydrogenase:** regulates hydrogenase transcription in some bacteria; not a catalytic core requirement (pichechoquette2019molecularhydrogena pages 6-8, pichechoquette2019molecularhydrogena pages 9-11).
* **High-affinity group 1h/5 [NiFe]-hydrogenase:** atmospheric-H2 scavenging branch; usually a boundary rather than trait-defining node (pichechoquette2019molecularhydrogena pages 6-8).
* **HydABC electron-bifurcating [FeFe]-hydrogenase:** transfers H2-derived electrons to NAD+ and ferredoxin in acetogens (frolov2023obligateautotrophyat pages 8-9).
* **Ech/Eha/Ehb-type energy-converting hydrogenases:** membrane complexes coupling H2/ferredoxin chemistry to ion translocation (pichechoquette2019molecularhydrogena pages 6-8, frolov2023obligateautotrophyat pages 1-2).
* **Rnf complex:** ferredoxin:NAD+ oxidoreductase and ion-translocation module in Rnf-type acetogens (frolov2023obligateautotrophyat pages 1-2).
* **Hydrogen-dependent CO2 reductase (HDCR):** candidate CO2-to-formate entry module in acetogens; the *A. autotrophica* assignment is genomic/predicted and should be marked uncertain (frolov2023obligateautotrophyat pages 8-9).
* **CODH/ACS complex (AcsABC)** and acetate-formation genes `pta/eutD/acyP/ackA/acdAB/acs`: WLP and acetogenic-output candidates (jiao2021insightintothe pages 6-7).
* **Rubisco and phosphoribulokinase:** CBB-cycle markers. Require a complete, functional module rather than Rubisco-like sequence alone.
* **Respiratory chain:** NADH dehydrogenase, quinone pool, quinol/cytochrome oxidases, and ATP synthase. *C. necator* H16 encodes two uptake hydrogenases, two NADH dehydrogenases, five quinol oxidases, and three cytochrome oxidases (cramm2009genomicviewof pages 1-2).
* **Methanogenesis modules:** methyl-H4MPT:CoM methyltransferase (Mtr), heterodisulfide reductase/hydrogenase electron-bifurcation machinery, and methyl-CoM reductase. These should be introduced only on the methanogenic branch.

### Environmental and assay nodes

* H2 concentration or partial pressure; gas–liquid H2 mass transfer.
* CO2/bicarbonate availability and isotopic-carbon incorporation.
* O2 availability/redox state; hydrogenase O2 tolerance.
* Terminal acceptor availability: O2, nitrate, sulfate, fumarate, or CO2.
* pH, temperature, salinity, pressure, and trace metals needed for hydrogenase maturation, especially Ni and Fe.
* Organic-carbon exclusion or limitation in growth assays.
* H2-consumption rate, CO2-fixation rate, growth yield, product formation, and inhibitor controls.

## 3. Candidate causal edges

The compact priority map below separates core edges from pathway-specific extensions.

| priority | subject | predicate | object | biological context | evidence strength/curation status |
|---|---|---|---|---|---|
| P1 | molecular hydrogen (H2) | is oxidized by | uptake hydrogenase | Core hydrogenotrophic entry step; broad across aerobic hydrogen oxidizers and many anaerobes | strong; generic core edge; curate first (pichechoquette2019molecularhydrogena pages 6-8) |
| P1 | uptake hydrogenase | transfers electrons to | electron transport chain | Best supported for aerobic/respiratory hydrogenotrophy; membrane-bound [NiFe] systems | strong; generic for respiratory branch, not universal to all hydrogenotrophs (pichechoquette2019molecularhydrogena pages 6-8, cramm2009genomicviewof pages 1-2) |
| P1 | electron transport chain | generates | ion motive force | Respiratory H2 oxidation coupled to terminal acceptor reduction | strong; generic for respiratory branch (culp2023crossfeedinginthe pages 7-9, cramm2009genomicviewof pages 1-2) |
| P1 | ion motive force | drives | ATP synthase / ATP production | Chemiosmotic energy conservation in aerobic and many anaerobic H2 users | strong; generic bioenergetic edge (culp2023crossfeedinginthe pages 7-9, frolov2023obligateautotrophyat pages 1-2) |
| P1 | H2 | donates electrons via HydABC | NADH and reduced ferredoxin | Electron-bifurcating [FeFe]-hydrogenase in acetogenic branch | strong; taxon-specific branch, curate with scope note (frolov2023obligateautotrophyat pages 8-9) |
| P1 | reduced ferredoxin and NADH | power | Wood-Ljungdahl pathway CO2 fixation | Acetogenic hydrogenotrophy; reductive acetyl-CoA pathway | strong; taxon-specific branch (frolov2023obligateautotrophyat pages 8-9, frolov2023obligateautotrophyat pages 1-2) |
| P1 | CO2 + H2 | are converted to | acetate | Acetogens / homoacetogens | strong; taxon-specific product edge (pichechoquette2019molecularhydrogena pages 8-9, frolov2023obligateautotrophyat pages 1-2) |
| P1 | CO2 + H2 | are converted to | methane | Hydrogenotrophic methanogens | strong; taxon-specific product edge (culp2023crossfeedinginthe pages 7-9, pichechoquette2019molecularhydrogena pages 8-9) |
| P2 | Calvin-Benson-Bassham cycle | fixes carbon into | biomass carbon | Aerobic Knallgas bacteria and other CBB-using autotrophs | moderate; trait-relevant but source support here is indirect relative to other core edges (cramm2009genomicviewof pages 1-2, pichechoquette2019molecularhydrogena pages 9-11) |
| P2 | O2 | serves as terminal electron acceptor for | respiratory hydrogenotrophy | Knallgas/aerobic hydrogen-oxidizing bacteria | strong; conditional branch, not universal (pichechoquette2019molecularhydrogena pages 6-8, cramm2009genomicviewof pages 1-2) |
| P2 | nitrate | serves as terminal electron acceptor for | hydrogenotrophic respiration | Anaerobic respiratory hydrogenotrophs | moderate; conditional branch, broad review support (culp2023crossfeedinginthe pages 7-9, pichechoquette2019molecularhydrogena pages 11-13) |
| P2 | sulfate | serves as terminal electron acceptor for | hydrogenotrophic respiration | Sulfate-reducing hydrogenotrophs | strong; conditional branch, broad review support (culp2023crossfeedinginthe pages 7-9, thaysen2020¬estimatingmicrobialhydrogen pages 6-8) |
| P2 | H2 concentration | modulates | hydrogenotroph growth and pathway competitiveness | Elevated H2 favors low-affinity H2 oxidizers / alters community function | strong; environmental modifier (pichechoquette2019molecularhydrogena pages 11-13, thaysen2020¬estimatingmicrobialhydrogen pages 6-8) |
| P2 | O2 availability | modulates | hydrogenase activity and hydrogenotrophic niche | Distinguishes aerobic Knallgas, O2-tolerant scavengers, and anoxic acetogenic/methanogenic branches | strong; environmental modifier (pichechoquette2019molecularhydrogena pages 6-8) |
| P3 | membrane-bound energy-converting hydrogenase (Ech/Eha/Ehb-like) | generates | ion motive force | Acetogens and methanogens using ion-coupled H2 metabolism | moderate; mechanistically important but often genomic/organism-specific in available evidence (pichechoquette2019molecularhydrogena pages 6-8, frolov2023obligateautotrophyat pages 8-9, frolov2023obligateautotrophyat pages 1-2) |
| P3 | hydrogen sensor hydrogenase | regulates expression of | uptake hydrogenase systems | Regulatory layer in some bacteria such as Cupriavidus | moderate; useful extension, not core trait-defining edge (pichechoquette2019molecularhydrogena pages 6-8, pichechoquette2019molecularhydrogena pages 9-11) |
| P3 | genome-encoded WLP or hydrogenase modules | implies capacity for | hydrogenotrophy | MAG/genome-based prediction without direct physiology | uncertain; genomic inference only, curate cautiously (jiao2021insightintothe pages 6-7) |


*Table: This table prioritizes candidate causal edges for curating the hydrogenotrophic trait, separating universal core edges from taxon-specific branches and uncertain genomic inferences. It is useful as a compact checklist for deciding what to curate first into a TraitMech graph.*

The supporting snippets and curation interpretation for the recommended edges are as follows.

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| H2 | is oxidized by | uptake hydrogenase | Piché-Choquette & Constant: uptake hydrogenases “channel electrons to the respiratory electron transport chain and supply energy to the cell” (2019; DOI below) (pichechoquette2019molecularhydrogena pages 6-8) | **Strong core edge**, but specify uptake rather than bidirectional H2-producing hydrogenase. |
| Uptake hydrogenase | transfers electrons to | respiratory electron-transport chain | Same review; *C. necator* additionally encodes MBH/SH, NADH dehydrogenases, and multiple terminal oxidases (pichechoquette2019molecularhydrogena pages 6-8, cramm2009genomicviewof pages 1-2) | Strong for respiratory hydrogenotrophs; not universal to soluble acetogenic branches. |
| H2 oxidation | reduces | NAD+ | In Knallgas bacteria, group-3 hydrogenase “couples H2 oxidation to NAD reduction” (pichechoquette2019molecularhydrogena pages 9-11) | Strong but taxon-specific; represent NADH as product. |
| H2 | donates electrons through | HydABC | *A. autotrophica*: “Electrons coming from molecular hydrogen are transferred by the electron-bifurcating hydrogenase to … NAD+ and ferredoxin” (frolov2023obligateautotrophyat pages 8-9) | Strong 2023 primary evidence for an acetogenic branch. |
| Reduced ferredoxin/NADH | supplies reducing power to | WLP | “A portion of the reduced ferredoxin is used in the reductive reactions of Wood-Ljungdahl pathway” (frolov2023obligateautotrophyat pages 8-9) | Strong in *A. autotrophica*; broader generalization should retain acetogen scope. |
| Ech or Rnf | generates | ion-motive force | Acetogenic energy conservation uses either Rnf or Ech; *A. autotrophica* encodes a membrane-bound energy-converting hydrogenase “which generates ion-motive force” (frolov2023obligateautotrophyat pages 8-9, frolov2023obligateautotrophyat pages 1-2) | Strong module-level relationship; exact ion may be organism-specific. |
| Ion-motive force | drives | ATP synthase | Rnf/Ech-linked energy conservation is coupled to ATP synthase; respiratory H2 cleavage and carrier oxidation generate PMF/SMF that drives ATP synthesis (culp2023crossfeedinginthe pages 7-9, frolov2023obligateautotrophyat pages 1-2) | Strong bioenergetic edge. Do not force proton rather than sodium coupling globally. |
| H2 + CO2 | are converted by WLP to | acetate | `4H2 + 2CO2 → CH3COOH + 2H2O`; ΔG°′ ≈ −104 kJ as stated in the 2023 acetogen study (frolov2023obligateautotrophyat pages 1-2) | Strong acetogenic branch. Balance protonation consistently in YAML. |
| H2 + CO2 | are converted by methanogenesis to | methane | `4H2 + CO2 → CH4 + 2H2O` (culp2023crossfeedinginthe pages 7-9, pichechoquette2019molecularhydrogena pages 8-9) | Strong methanogenic branch; methane is chiefly catabolic product, while cellular carbon assimilation is a distinct edge. |
| Mtr methyl transfer | translocates | Na+ | Methanogenic Mtr translocates Na+ during methyl transfer, contributing to energy conservation (culp2023crossfeedinginthe pages 7-9) | Strong mechanistic branch, but not shared with bacterial hydrogenotrophs. |
| O2 | serves as terminal acceptor for | Knallgas H2 oxidation | Knallgas bacteria oxidize H2 with O2; *C. necator* has multiple quinol and cytochrome oxidases (cramm2009genomicviewof pages 1-2, pichechoquette2019molecularhydrogena pages 9-11) | Strong aerobic branch. Avoid the imprecise unbalanced shorthand `H2 + O2 → H2O`; use `2H2 + O2 → 2H2O`. |
| Nitrate or sulfate | accepts H2-derived electrons in | anaerobic respiration | Hydrogenotrophic respiration uses H2 to reduce nitrate or sulfate; sulfate stoichiometry reported as `4H2 + SO4²− + H+ → HS− + 4H2O` (culp2023crossfeedinginthe pages 7-9, thaysen2020¬estimatingmicrobialhydrogen pages 6-8) | Strong for H2 respiration, but **insufficient alone** for `METPO:1000646`; require CO2-primary biomass evidence. |
| Elevated H2 | selects/stimulates | low-affinity H2 oxidizers and carbon turnover | H2 up to approximately 10,000 ppmv shifted communities toward low-affinity oxidation and sometimes shifted soil from net CO2 release to fixation (pichechoquette2019molecularhydrogena pages 11-13) | Environmental modifier; ecosystem-level and not a constitutive molecular edge. |
| Low H2 partial pressure | enables | syntrophic H2-consuming reactions | H2 buildup inhibits NADH oxidation, whereas low H2 can make syntrophic reactions favorable (culp2023crossfeedinginthe pages 7-9) | Context-dependent thermodynamic edge. H2 thresholds differ among pathways and taxa. |
| O2 availability | modulates | hydrogenase activity/niche | Hydrogenases differ markedly in O2 sensitivity; group-5 systems can be O2 tolerant and high affinity (pichechoquette2019molecularhydrogena pages 6-8) | Strong environmental regulator, but hydrogenase-group annotations must be checked carefully. |
| Complete CBB cycle | fixes | CO2 into biomass precursors | *C. necator* oxidizes H2 and fixes CO2 under H2-rich conditions (cramm2009genomicviewof pages 1-2, pichechoquette2019molecularhydrogena pages 9-11) | **Moderate in retrieved evidence** because the excerpts do not directly demonstrate Rubisco flux. Curate with a CBB-specific biochemical/genetic source before asserting individual enzyme edges. |

## 4. Recent developments, applications, and statistics

### Mechanistic and ecological advances

* **New obligate hydrogenotrophic acetogen (2023).** *Aceticella autotrophica* strain 3443-3AcT was described as the first obligately autotrophic acetogenic bacterium in its reported context. Its 2.27-Mbp genome contains 2,234 genes, HydABC, WLP machinery, and a membrane-bound energy-converting hydrogenase. This provides an unusually coherent genotype-to-physiology case for the acetogenic subgraph (frolov2023obligateautotrophyat pages 8-9, frolov2023obligateautotrophyat pages 1-2).
* **Methanogen hydrogenase evolution (2023).** Hydrogenotrophic methanogens commonly possess group 3a/3c and group-4 [NiFe]-hydrogenase homologues; phylogenetic analysis supports duplication and subunit recruitment as routes to diversified redox coupling. H2-driven ferredoxin reduction is thermodynamically favorable in H2-rich hyperalkaline serpentinizing settings but not under many other conditions, underscoring the need for environmental qualifiers (boyd2023anaturalistperspective pages 8-9).
* **Rumen systems (2024).** A recent review identified 6,152 hydrogenase-bearing MAGs: 3,003 encoded fermentative H2-production systems, whereas 95 encoded H2-uptake hydrogenases together with methyl-CoM reductase, principally in *Methanobrevibacter*. These numbers illustrate why hydrogenase presence alone cannot diagnose hydrogenotrophy (mackie2024—invitedreview pages 6-7).

### Real-world implementation

* **Biological methanation and carbon capture/utilization.** Hydrogenotrophic methanogens are deployed or developed for power-to-gas and biogas upgrading, reducing captured CO2 with renewable H2 to methane. Bio-integrated CCU seeks to avoid energy-intensive CO2 desorption by coupling capture-agent release directly to archaeal CO2 reduction. This is a strong application of the methanogenic branch, although reactor mass transfer, gas safety, capture-agent compatibility, and methane leakage remain important system-level constraints.
* **Gas fermentation and chemical production.** Acetogens convert H2/CO2-containing gas streams through WLP chemistry. In 2024, a lactate-mediated coculture of engineered *Acetobacterium woodii* and *Clostridium drakei* produced **4 ± 1.7 mM hexanoate** and **18.5 ± 5.8 mM butyrate**, respectively fourfold and twofold higher than a non-lactate-mediated coculture. The experiment used H2:CO2 of 67:33; the authors caution that some inferred pathways remain speculative (mook2024lactatemediatedmixotrophiccocultivation pages 1-2).
* **Syngas valorization.** Acetogens can convert industrial CO/CO2-containing gases into fuels, chemicals, and feed. The 2024 assessment identifies low gas-to-liquid mass transfer, slow growth/productivity, and scale-up costs as leading constraints; microbial catalysts can, however, tolerate or adapt to some impurities better than chemical catalysts (neto2024exploringthepotential pages 1-2).
* **Enteric-methane mitigation.** Rumen methanogens consume fermentation-derived H2 to reduce CO2. Redirecting H2 toward alternative sinks is an active mitigation strategy. Methane has an atmospheric lifetime of about **12.5 years** and is commonly assigned **28×** the warming potential of CO2; the cited review attributes about **80% of agricultural methane** to livestock systems, approximately 90% of that to enteric fermentation (mackie2024—invitedreview pages 1-2).
* **Underground H2 storage risk.** Methanogenesis, sulfate reduction, and homoacetogenesis can consume stored H2. Reported threshold ranges are approximately **0.4–95 nM H2** for methanogenesis and **1–15 nM** for sulfate reduction, but extrapolation from optimized batch cultures to reservoirs remains uncertain (thaysen2020¬estimatingmicrobialhydrogen pages 6-8).

## 5. Recommended minimal TraitMech architecture

A robust YAML should use a **shared core plus mutually qualified branches**, rather than treating all edges as universal:

1. `molecular hydrogen → oxidized by → uptake hydrogenase`
2. `uptake hydrogenase → transfers electrons to → electron carrier or respiratory chain`
3. `electron transfer → generates → reducing equivalents and/or ion-motive force`
4. `ion-motive force → drives → ATP synthase`
5. `ATP + reducing equivalents → support → CO2 fixation`
6. Branch A: `CBB cycle → produces → biomass precursors`
7. Branch B: `WLP → produces → acetyl-CoA/acetate and biomass precursors`
8. Branch C: `hydrogenotrophic methanogenesis → produces → methane`, with separate cellular-carbon assimilation
9. Environmental qualifiers: H2 partial pressure, O2/redox state, terminal acceptor, pH, temperature, and gas-transfer regime.

The graph should not imply that O2, sulfate, nitrate, acetate, and methane all belong to one organism or one simultaneous physiological state.

## 6. Claims not yet ready for curation

1. **Universal CBB assignment.** Hydrogenotrophs use multiple carbon-fixation pathways; CBB is not universal. Add Rubisco/phosphoribulokinase edges only with pathway-specific evidence.
2. **Hydrogenase group as phenotype proxy.** Hydrogenases can produce H2, recycle endogenous H2, sense H2, or support persistence. Direction, localization, electron partner, and physiological assay are required.
3. **MAG-only hydrogenotrophy.** Co-occurrence of hydrogenase and WLP/CBB genes is a prediction. Mark as “putative” until H2 uptake and inorganic-carbon incorporation or growth are measured.
4. **Atmospheric H2 equals autotrophic growth.** Atmospheric scavenging commonly supports maintenance or mixotrophy rather than CO2-primary biomass formation (pichechoquette2019molecularhydrogena pages 11-13).
5. **Terminal-acceptor respiration equals the target trait.** H2-dependent nitrate, sulfate, fumarate, or O2 reduction establishes hydrogen oxidation, not necessarily autotrophy.
6. **Generic ion coupling.** Rnf, Ech, Mtr, and related complexes may translocate H+ or Na+ depending on organism and complex; do not globally assert one ion.
7. **Unqualified HDCR edge in *A. autotrophica*.** The available evidence is genomic prediction, not direct enzyme measurement (frolov2023obligateautotrophyat pages 8-9).
8. **Syngas growth as H2/CO2 growth.** CO can dominate both carbon and electron flux; isotope tracing or controlled gas comparisons are needed.
9. **Existing 14-node/14-edge graph completeness.** The supplied summary cannot be audited without the YAML. Merge only after checking whether its nodes distinguish respiratory, acetogenic, and methanogenic branches.

## DOI-first bibliography

1. Frolov EN et al. “Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium.” *Frontiers in Microbiology*. **12 May 2023**. https://doi.org/10.3389/fmicb.2023.1185739 (frolov2023obligateautotrophyat pages 8-9, frolov2023obligateautotrophyat pages 1-2)
2. Boyd ES et al. “A naturalist perspective of microbiology: Examples from methanogenic archaea.” *Environmental Microbiology* 25:184–198. **2023**. https://doi.org/10.1111/1462-2920.16285 (boyd2023anaturalistperspective pages 8-9)
3. Culp EJ, Goodman AL. “Cross-feeding in the gut microbiome: Ecology and mechanisms.” *Cell Host & Microbe* 31:485–499. **April 2023**. https://doi.org/10.1016/j.chom.2023.03.016 (culp2023crossfeedinginthe pages 7-9)
4. Mook A et al. “Lactate-mediated mixotrophic co-cultivation … for autotrophic production of volatile fatty acids.” *Microbial Cell Factories* 23. **July 2024**. https://doi.org/10.1186/s12934-024-02481-3 (mook2024lactatemediatedmixotrophiccocultivation pages 1-2)
5. Mackie RI et al. “Hydrogen production and hydrogen utilization in the rumen.” *Animal Bioscience* 37:323–336. **February 2024**. https://doi.org/10.5713/ab.23.0294 (mackie2024—invitedreview pages 6-7, mackie2024—invitedreview pages 1-2)
6. Neto AS et al. “Exploring the potential of syngas fermentation for recovery of high-value resources.” *Current Pollution Reports*. **Accepted 12 November 2024**. https://doi.org/10.1007/s40726-024-00337-3 (neto2024exploringthepotential pages 1-2)
7. Piché-Choquette S, Constant P. “Molecular hydrogen, a neglected key driver of soil biogeochemical processes.” *Applied and Environmental Microbiology* 85:e02418-18. **March 2019**. https://doi.org/10.1128/AEM.02418-18 (pichechoquette2019molecularhydrogena pages 6-8, pichechoquette2019molecularhydrogena pages 11-13, pichechoquette2019molecularhydrogena pages 8-9, pichechoquette2019molecularhydrogena pages 9-11)
8. Jiao J-Y et al. “Insight into the function and evolution of the Wood–Ljungdahl pathway in Actinobacteria.” *ISME Journal* 15:3005–3018. **May 2021**. https://doi.org/10.1038/s41396-021-00935-9 (jiao2021insightintothe pages 6-7)
9. Cramm R. “Genomic view of energy metabolism in *Ralstonia eutropha* H16.” *Microbial Physiology* 16:38–52. **Published online 29 October 2008; issue 2009**. https://doi.org/10.1159/000142893 (cramm2009genomicviewof pages 1-2)
10. Thaysen E et al. “Estimating microbial hydrogen consumption in hydrogen storage in porous media as a basis for site selection.” **November 2020 preprint**. https://doi.org/10.31223/X5HC7H (thaysen2020¬estimatingmicrobialhydrogen pages 6-8)

**Curation conclusion:** retain `METPO:1000646` as a composite trophic phenotype whose minimal evidence is H2-supported energy conservation plus CO2-primary carbon assimilation. The best-supported first expansion of the existing graph is a shared hydrogenase–electron-transfer–ion-gradient–ATP core, followed by explicitly scoped CBB, acetogenic-WLP, and methanogenic branches.

References

1. (culp2023crossfeedinginthe pages 7-9): Elizabeth J. Culp and Andrew L. Goodman. Cross-feeding in the gut microbiome: ecology and mechanisms. Cell host & microbe, 31 4:485-499, Apr 2023. URL: https://doi.org/10.1016/j.chom.2023.03.016, doi:10.1016/j.chom.2023.03.016. This article has 566 citations and is from a highest quality peer-reviewed journal.

2. (pichechoquette2019molecularhydrogena pages 8-9): Sarah Piché-Choquette and Philippe Constant. Molecular hydrogen, a neglected key driver of soil biogeochemical processes. Applied and Environmental Microbiology, Mar 2019. URL: https://doi.org/10.1128/aem.02418-18, doi:10.1128/aem.02418-18. This article has 130 citations and is from a peer-reviewed journal.

3. (pichechoquette2019molecularhydrogena pages 6-8): Sarah Piché-Choquette and Philippe Constant. Molecular hydrogen, a neglected key driver of soil biogeochemical processes. Applied and Environmental Microbiology, Mar 2019. URL: https://doi.org/10.1128/aem.02418-18, doi:10.1128/aem.02418-18. This article has 130 citations and is from a peer-reviewed journal.

4. (cramm2009genomicviewof pages 1-2): Rainer Cramm. Genomic view of energy metabolism in &lt;i&gt;ralstonia eutropha&lt;/i&gt; h16. Microbial Physiology, 16:38-52, Oct 2009. URL: https://doi.org/10.1159/000142893, doi:10.1159/000142893. This article has 268 citations.

5. (frolov2023obligateautotrophyat pages 1-2): Evgenii N. Frolov, Alexander G. Elcheninov, Alexandra V. Gololobova, Stepan V. Toshchakov, Andrei A. Novikov, Alexander V. Lebedinsky, and Ilya V. Kublanov. Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1185739, doi:10.3389/fmicb.2023.1185739. This article has 29 citations and is from a peer-reviewed journal.

6. (pichechoquette2019molecularhydrogena pages 11-13): Sarah Piché-Choquette and Philippe Constant. Molecular hydrogen, a neglected key driver of soil biogeochemical processes. Applied and Environmental Microbiology, Mar 2019. URL: https://doi.org/10.1128/aem.02418-18, doi:10.1128/aem.02418-18. This article has 130 citations and is from a peer-reviewed journal.

7. (neto2024exploringthepotential pages 1-2): Alvaro S. Neto, Steven Wainaina, Konstantinos Chandolias, Pawel Piatek, and Mohammad J. Taherzadeh. Exploring the potential of syngas fermentation for recovery of high-value resources: a comprehensive review. Current Pollution Reports, Nov 2024. URL: https://doi.org/10.1007/s40726-024-00337-3, doi:10.1007/s40726-024-00337-3. This article has 48 citations and is from a peer-reviewed journal.

8. (jiao2021insightintothe pages 6-7): Jian-Yu Jiao, Li Fu, Zheng-Shuang Hua, Lan Liu, Nimaichand Salam, Peng-Fei Liu, Ai-Ping Lv, Geng Wu, Wen-Dong Xian, Qiyun Zhu, En-Min Zhou, Bao-Zhu Fang, Aharon Oren, Brian P Hedlund, Hong-Chen Jiang, Rob Knight, Lei Cheng, and Wen-Jun Li. Insight into the function and evolution of the wood–ljungdahl pathway in actinobacteria. The ISME Journal, 15:3005-3018, May 2021. URL: https://doi.org/10.1038/s41396-021-00935-9, doi:10.1038/s41396-021-00935-9. This article has 149 citations.

9. (pichechoquette2019molecularhydrogena pages 9-11): Sarah Piché-Choquette and Philippe Constant. Molecular hydrogen, a neglected key driver of soil biogeochemical processes. Applied and Environmental Microbiology, Mar 2019. URL: https://doi.org/10.1128/aem.02418-18, doi:10.1128/aem.02418-18. This article has 130 citations and is from a peer-reviewed journal.

10. (frolov2023obligateautotrophyat pages 8-9): Evgenii N. Frolov, Alexander G. Elcheninov, Alexandra V. Gololobova, Stepan V. Toshchakov, Andrei A. Novikov, Alexander V. Lebedinsky, and Ilya V. Kublanov. Obligate autotrophy at the thermodynamic limit of life in a new acetogenic bacterium. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1185739, doi:10.3389/fmicb.2023.1185739. This article has 29 citations and is from a peer-reviewed journal.

11. (thaysen2020¬estimatingmicrobialhydrogen pages 6-8): Eike Thaysen, Sean McMahon, Gion Strobel, Ian Butler, Bryne Ngwenya, Niklas Heinemann, Mark Wilkinson, Aliakbar Hassanpouryouzband, Christopher McDermott, and Katriona Edlmann. ¬estimating microbial hydrogen consumption in hydrogen storage in porous media as a basis for site selection. Unknown journal, Nov 2020. URL: https://doi.org/10.31223/x5hc7h, doi:10.31223/x5hc7h. This article has 17 citations.

12. (boyd2023anaturalistperspective pages 8-9): Eric S. Boyd, Rachel L. Spietz, Manjinder Kour, and Daniel R. Colman. A naturalist perspective of microbiology: examples from methanogenic archaea. Environmental Microbiology, 25:184-198, Nov 2023. URL: https://doi.org/10.1111/1462-2920.16285, doi:10.1111/1462-2920.16285. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (mackie2024—invitedreview pages 6-7): Roderick I. Mackie, Hyewon Kim, Na Kyung Kim, and Isaac Cann. — invited review — hydrogen production and hydrogen utilization in the rumen: key to mitigating enteric methane production. Animal Bioscience, 37:323-336, Feb 2024. URL: https://doi.org/10.5713/ab.23.0294, doi:10.5713/ab.23.0294. This article has 45 citations and is from a peer-reviewed journal.

14. (mook2024lactatemediatedmixotrophiccocultivation pages 1-2): Alexander Mook, Jan Herzog, Paul Walther, Peter Dürre, and Frank R. Bengelsdorf. Lactate-mediated mixotrophic co-cultivation of clostridium drakei and recombinant acetobacterium woodii for autotrophic production of volatile fatty acids. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02481-3, doi:10.1186/s12934-024-02481-3. This article has 13 citations and is from a peer-reviewed journal.

15. (mackie2024—invitedreview pages 1-2): Roderick I. Mackie, Hyewon Kim, Na Kyung Kim, and Isaac Cann. — invited review — hydrogen production and hydrogen utilization in the rumen: key to mitigating enteric methane production. Animal Bioscience, 37:323-336, Feb 2024. URL: https://doi.org/10.5713/ab.23.0294, doi:10.5713/ab.23.0294. This article has 45 citations and is from a peer-reviewed journal.