---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:31:34.891754'
end_time: '2026-08-04T00:42:41.224134'
duration_seconds: 666.33
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultative oxygen preference
  trait_identifier: METPO:1000612
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultative_oxygen_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An oxygen preference that describes a microorganism that can grow with
    or without molecular oxygen.
  parent_traits: METPO:1000601
  synonyms: Ox_facultative_aerobe_anaerobe
  evidence_summary: 'DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports
    facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051:
    adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive
    metabolic switching.)'
  causal_graph_summary: 'facultative_oxygen_preference_switching: 9 nodes, 8 edges'
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
- **Trait label:** facultative oxygen preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000612
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that describes a microorganism that can grow with or without molecular oxygen.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_facultative_aerobe_anaerobe
- **Existing evidence:** DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051: adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive metabolic switching.)
- **Existing causal graph summary:** facultative_oxygen_preference_switching: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **facultative oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_oxygen_preference.yaml`.

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
- **Trait label:** facultative oxygen preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000612
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that describes a microorganism that can grow with or without molecular oxygen.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_facultative_aerobe_anaerobe
- **Existing evidence:** DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051: adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive metabolic switching.)
- **Existing causal graph summary:** facultative_oxygen_preference_switching: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **facultative oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_oxygen_preference.yaml`.

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


# Curation report: facultative oxygen preference

## Trait record and scope

- **Trait label:** facultative oxygen preference
- **Trait identifier:** **METPO:1000612**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** METPO:1000601
- **Synonym:** `Ox_facultative_aerobe_anaerobe`
- **Operational definition:** capacity of a microorganism to **grow both in the presence and in the absence of molecular oxygen**, usually by switching among aerobic respiration, anaerobic respiration using alternative terminal electron acceptors, and fermentation.

The trait is a growth phenotype, not merely oxygen survival or detoxification. A defensible assay should demonstrate positive growth under an oxic condition and under a rigorously anoxic condition, with medium, electron acceptors, carbon source, inoculum history, and growth endpoint recorded. Facultative organisms need not grow equally well in both regimes; aerobic respiration commonly gives a greater energetic and biomass yield. In *E. coli*, standard free-energy estimates cited for glucose oxidation are approximately −2,830 kJ mol⁻¹ with O₂ versus −806 kJ mol⁻¹ with nitrate, explaining preference for oxygen when it is available. (unden2021sensingofo2 pages 1-7)

### Boundary cases

1. **Aerotolerant anaerobes:** tolerate oxygen but do not use it for respiration; oxygen tolerance alone does not establish METPO:1000612.
2. **Obligate aerobes:** require O₂ for growth and therefore fail the anoxic-growth criterion.
3. **Obligate anaerobes:** do not grow in O₂, even if they possess O₂-detoxifying enzymes.
4. **Microaerophiles:** require or prefer low O₂ and may fail at atmospheric O₂ or under complete anoxia; this is not automatically facultative behavior.
5. **Facultatively fermentative yeasts:** potentially in scope if both oxic and anoxic growth are demonstrated, but their mitochondrial and transcriptional mechanisms should not be merged with the bacterial FNR–ArcAB graph.
6. **Dormancy or survival:** viability without cell multiplication is insufficient.
7. **Nitrate-dependent anoxic growth:** qualifies when the organism also grows oxically, but nitrate respiration is one implementation rather than part of the definition.

The clinical review underlying the supplied evidence makes the same central distinction: facultative anaerobes grow with or without oxygen, whereas strict aerobes, strict anaerobes, and aerotolerant organisms occupy different phenotype classes. It reported that 8 of 12 WHO antimicrobial-resistance priority pathogens—66.7%—were facultative anaerobes, illustrating the ecological and clinical importance of oxygen-regime flexibility. (andre2021theselectiveadvantage pages 1-2)

## Recommended graph architecture

The existing nine-node graph is directionally appropriate, but the trait is better represented as a **conditional capability graph** rather than one universal linear pathway:

1. environmental O₂ availability is sensed directly by FNR-like Fe–S regulators and indirectly through respiratory-chain redox state;
2. FNR and ArcAB reprogram central metabolism and respiratory-chain composition;
3. nitrate and other acceptor-specific systems activate alternative respiratory modules;
4. terminal oxidase switching supports respiration across high-to-low O₂ concentrations;
5. fermentation supplies ATP and redox balancing when usable terminal acceptors are unavailable;
6. the combined alternatives permit growth across oxic and anoxic regimes.

FNR, ArcAB, NarXL, and particular oxidases are **exemplar mechanisms in Enterobacterales**, not universal necessary components of the trait. Recent work reinforces this diversity: the PAS-less ArcB of *Haemophilus influenzae* appears to respond to metabolic signals by a cysteine-independent mechanism rather than duplicating the canonical *E. coli* ArcB redox switch. (alvarez2024diversificationofsignal pages 14-15)

## Candidate nodes grouped by type

### Trait and taxon nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| facultative oxygen preference | **METPO:1000612** | Root phenotype node; quote identifier verbatim in YAML. |
| *Escherichia coli* | NCBITaxon:562 | Use strain-level taxon IDs when an edge derives from K-12 MG1655 or another defined strain. |
| *Bacillus subtilis* | NCBITaxon:1423 | Mechanistically distinct from *E. coli*; nitrate/fermentation and electro-fermentation evidence is taxon-specific. |
| facultative anaerobic bacterium | label-only candidate | Avoid treating this grouping as a molecular mechanism. |

### Environmental and experimental factors

| Node | Suggested grounding | Role |
|---|---|---|
| molecular oxygen | CHEBI:15379 | Terminal electron acceptor and regulatory signal. |
| anoxic condition | ENVO term candidate; verify exact release | Experimental state with O₂ excluded below assay detection. |
| microoxic condition | ENVO term candidate; verify exact release | Intermediate O₂ regime that favors high-affinity oxidases and ArcA activity. |
| oxygen oscillation | label-only experimental factor | Dynamic industrial bioreactor exposure; duration and dissolved-O₂ profile must be qualifiers. |
| nitrate | CHEBI:17632 | Alternative terminal electron acceptor and NarX signal. |
| poised anode | label-only experimental factor | Artificial terminal electron sink in electro-fermentation. |
| glucose availability | glucose: CHEBI:17234 | Carbon/electron-donor context; interacts strongly with oxygen response. |

### Chemicals, cofactors, and metabolites

| Node | Suggested grounding | Role |
|---|---|---|
| [4Fe–4S] cluster | CHEBI class candidate; verify exact identifier | Active anaerobic FNR cofactor. |
| [2Fe–2S] cluster | CHEBI class candidate; verify exact identifier | O₂-converted, inactive FNR state in the *E. coli* mechanism. |
| ubiquinone / ubiquinol | CHEBI identifiers should be selected for the exact isoprenologue | Oxidized/reduced quinone-pool signal affecting ArcB. |
| menaquinone / menaquinol | CHEBI identifiers should be selected for the exact isoprenologue | Additional quinone couple involved in ArcAB control. |
| NADH / NAD⁺ | CHEBI:16908 / CHEBI:15846 | Redox-balancing pair linking respiration and fermentation. |
| pyruvate | CHEBI:15361 | Branch point into respiration or mixed-acid fermentation. |
| acetate | CHEBI:30089 | Overflow/fermentation product and industrial process marker. |
| lactate | CHEBI term should specify stereochemistry | Fermentative redox sink. |
| acetoin | CHEBI term candidate; verify | Industrial fermentation product. |
| 2,3-butanediol | stereospecific CHEBI term required | NADH-coupled product; do not collapse stereoisomers without assay information. |
| reactive oxygen species | GO/process or CHEBI member nodes | Oxygen-associated stress; supportive rather than sufficient for the trait. |

### Genes, proteins, complexes, and transport modules

| Candidate | Grounding strategy | Function and scope |
|---|---|---|
| **FNR** | UniProt/NCBI Gene identifier for the exact taxon and strain | Direct O₂-responsive Fe–S transcription factor in *E. coli* and related Proteobacteria. |
| **ArcB–ArcA** | Taxon-specific UniProt entries | Quinone/redox-responsive sensor kinase and response regulator. |
| **NarX–NarL** | Taxon-specific UniProt entries | Nitrate-responsive two-component system. |
| **narGHJI nitrate reductase** | Taxon-specific complex/gene products; EC/Rhea grounding per reaction | Membrane nitrate-respiratory module. |
| cytochrome **bo₃** ubiquinol oxidase, `cyoABCD` | GO complex plus strain-specific proteins | Lower-affinity, high-throughput aerobic terminal oxidase. |
| cytochrome **bd-I** oxidase, `cydABX` | GO complex plus strain-specific proteins | High-affinity terminal oxidase supporting microoxic respiration and stress resistance. |
| cytochrome **bd-II**, `appBC` | Taxon-specific proteins | Distinct from bd-I; do not merge their stress phenotypes. |
| succinate dehydrogenase, `sdhCDAB` | GO:0045281 is a possible complex grounding; verify annotation context | TCA/respiratory module repressed in oxygen limitation. |
| pyruvate dehydrogenase complex | GO:0045254 candidate | Aerobic carbon oxidation module affected by ArcA. |
| ATP synthase | GO complex term, taxon-specific subunits | Uses proton motive force for ATP production. |
| superoxide dismutase/catalase systems | EC and UniProt entries by taxon | Confer oxygen/ROS tolerance but do not alone prove facultative growth. |

### Pathways, biological processes, molecular functions, and localization

| Node | Suggested grounding |
|---|---|
| aerobic respiration | GO:0009060 |
| anaerobic respiration | GO:0009061 |
| cellular respiration | GO:0045333 |
| fermentation | GO:0006113 |
| tricarboxylic acid cycle | GO:0006099 |
| electron transport chain | GO:0022900 |
| oxidative phosphorylation | GO:0006119 |
| nitrate respiration | GO term candidate; verify the current GO release and taxon usage |
| proton-motive force generation | GO term candidate; verify exact current identifier |
| transcriptional regulation in response to oxygen | label-only unless an exact GO term is verified |
| plasma/inner membrane | GO:0005886 or the taxon-appropriate bacterial inner-membrane term |
| cytoplasm | GO:0005737 |
| DNA-binding transcription-factor activity | GO:0003700 |
| protein histidine kinase activity | GO:0004673 |

## Evidence-backed candidate causal edges

Quoted snippets below are short curation paraphrases or source excerpts and should be retained with taxon and condition qualifiers.

| # | Subject–predicate–object | Reference and publication date | Supporting snippet | Curation assessment |
|---:|---|---|---|---|
| 1 | molecular O₂ **converts/inactivates** FNR-[4Fe–4S] **to** FNR-[2Fe–2S] | 10.1073/pnas.94.12.6087; June 1997; synthesized in 10.1111/1462-2920.15293, Nov. 2021 | “When O₂ is present, the cluster decomposes to form [2Fe–2S]²⁺, causing FNR to become monomeric and unable to bind DNA.” | **High confidence; curate for *E. coli*.** This is the best direct molecular sensing edge. (unden2021sensingofo2 pages 1-7)
| 2 | anoxia **stabilizes/activates** FNR-[4Fe–4S] homodimer **which enables** promoter binding | 10.1111/1462-2920.15293; November 2021 | “In anaerobic conditions, FNR exists as a homodimer with [4Fe–4S]²⁺ clusters that binds to promoters and activates transcription.” | **High confidence; *E. coli*-specific implementation.** (unden2021sensingofo2 pages 1-7)
| 3 | FNR oxygen sensing **regulates** a broad anaerobic transcriptional program | 10.3390/inorganics11120450; November 2023 | FNR is the “master switch” between anaerobic and aerobic respiration and controls expression of “>300 genes.” | **High confidence for *E. coli*;** the exact regulon is condition-dependent. Do not make FNR universal. (unden2021sensingofo2 pages 1-7)
| 4 | respiratory quinone-pool redox state **modulates** ArcB **and thereby** ArcA phosphorylation | 10.1128/mmbr.00110-21; June 2022; 10.3389/fmicb.2016.01339; September 2016 | “The bacterial quinone pool is the primary modulator of ArcAB activity”; all three endogenous *E. coli* quinones contribute to ArcA control. | **High-level edge is strong; molecular polarity needs qualifiers.** Competing details remain about individual quinone species and direct mechanism. (lamoureux2023amultiscaleexpression pages 17-17)
| 5 | phosphorylated ArcA **represses** aerobic carbon-oxidation/TCA modules | 10.1002/bit.20381; March 2005; 10.1371/journal.pgen.1003839; October 2013 | ArcA-P represses “citric acid cycle, succinate dehydrogenase, pyruvate dehydrogenase, [and] cytochrome o oxidase.” | **High confidence in *E. coli*.** Prefer separate gene/complex edges if YAML permits. (levanon2005effectofoxygen pages 1-2)
| 6 | ArcA activity **promotes a shift toward** microaerobic/fermentative metabolism | 10.1002/bit.20381; March 2005 | ArcA is most important under microaerobic conditions and activates fermentative pathways and cytochrome d oxidase. | **Moderate–high confidence; condition-specific.** “Promotes” is safer than asserting direct activation for every fermentation gene. (levanon2005effectofoxygen pages 1-2)
| 7 | low O₂ **activates** ArcA and FNR programs **which repress** `sucABCD` and `sdhCDA` | 10.1111/1751-7915.70051; November 2024 | Oxygen limitation caused “ArcA- and Fnr-dependent repression of TCA-cycle genes (`sucABCD`, `sdhCDA`).” | **Strong recent process evidence; *E. coli* scale-down bioreactor assay.** (bafna‐ruhrer2024combinedoxygenand pages 7-9)
| 8 | nitrate **activates** NarX kinase/NarL phosphorylation | 10.1111/1462-2920.15293; November 2021 | “NarX phosphorylates NarL in the presence of nitrate and dephosphorylates it when nitrate is absent.” | **High confidence for *E. coli*.** (unden2021sensingofo2 pages 1-7)
| 9 | active FNR plus NarL **activates** `narGHJI` expression | 10.1111/1462-2920.15293; November 2021 | Expression of `narGHJI` is regulated by binding of FNR and NarL to its promoter. | **High confidence;** encode nitrate and anoxia as joint context rather than independent sufficient causes. (unden2021sensingofo2 pages 1-7)
| 10 | nitrate respiration **suppresses preference for** lower-energy anaerobic acceptors/fermentation | 10.1111/1462-2920.15293; November 2021 | Under anaerobiosis, nitrate respiration is induced and represses fumarate, tetrathionate, DMSO, and TMAO respiratory programs. | **Moderate confidence as a hierarchy edge;** regulation varies among taxa. (unden2021sensingofo2 pages 1-7)
| 11 | declining O₂ **downregulates** cytochrome bo₃ and **upregulates** cytochrome bd | 10.1111/1751-7915.70051; November 2024 | Under microaerobic conditions, `cyoABCE` was downregulated and `cydAB` upregulated. | **Strong assay-specific edge in *E. coli*.** (bafna‐ruhrer2024combinedoxygenand pages 7-9)
| 12 | cytochrome bd-I high O₂ affinity **enables** microoxic respiration | 10.1128/ecosalplus.esp-0012-2015; October 2015 | Cytochrome bd has O₂ Kᴅ ≈0.28 μM versus >300 μM for bo₃—about a 1,000-fold affinity difference. | **High confidence; *E. coli*.** Affinity is not synonymous with growth rate or energetic efficiency. (borisov2015oxygenasacceptor pages 2-4, borisov2015oxygenasacceptor pages 11-13)
| 13 | cytochrome bd-I **increases resistance to** respiratory inhibitors/host stresses | 10.3390/ijms25021277; January 2024 | At 96.3 μM CO and 100 μM O₂, respiration was inhibited 11.6±1.1% in bd-I-only cells versus 43.3±7.6% and 44.3±1.5% in bd-II- and bo₃-only cells. | **High confidence but accessory to the trait.** Curate as a robustness branch, not the defining oxygen-switch edge. (nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 4-7)
| 14 | absence of O₂ plus nitrate **enables** nitrate respiration and anoxic energy conservation | 10.1111/1462-2920.15293; November 2021 | Numerous bacteria replace O₂ with nitrate under O₂ limitation; in *E. coli*, FNR and NarXL coordinate the switch. | **High confidence for organisms possessing this module; not universal.** (unden2021sensingofo2 pages 1-7)
| 15 | absence of a usable terminal acceptor **favors** fermentation-mediated redox balancing | 10.1371/journal.pgen.1004264; April 2014 | ArcA/FNR regulation coordinates the change between fermentative and nitrate-respiratory conditions. | **Moderate confidence as a generic edge.** Specify substrate and taxon; fermentation pathways vary widely. (federowicz2014determiningthecontrol pages 7-10)
| 16 | coordinated ArcA/FNR regulation **controls** metabolic flux switching | 10.1371/journal.pgen.1004264; April 2014 | Of 91 redox reactions, 89 were regulated directly or indirectly by ArcA or FNR; regulatory and flux changes correlated at r²=0.71, p<10⁻⁶. | **Strong genome-scale support in *E. coli*.** Direct versus indirect edges must remain distinguishable. (federowicz2014determiningthecontrol pages 7-10)
| 17 | O₂ oscillations **cause** persistent transcriptional remodeling and acetate overflow | 10.1111/1751-7915.70051; November 2024 | Ten-minute O₂ oscillations reduced biomass and accumulated 45.4 g L⁻¹ acetate; O₂-driven transcriptional effects persisted after limitation ended. | **Strong assay-specific application edge, not a universal trait mechanism.** (bafna‐ruhrer2024combinedoxygenand pages 7-9, bafna‐ruhrer2024combinedoxygenand pages 10-11, bafna‐ruhrer2024combinedoxygenand pages 1-2)
| 18 | limited aeration plus a poised anode **redirects** *B. subtilis* fermentation toward acetoin | 10.1186/s13068-022-02253-4; January 2023 | A 0.7-V-versus-SHE anode produced an acetoin yield of 0.78±0.04 mol mol⁻¹ glucose, about twice the open/no-poised-potential result of 0.39±0.08. | **Strong application evidence but artificial-system specific.** Do not place the anode in the core natural trait graph. (sun2023anodeassistedelectrofermentationwith pages 1-2)
| 19 | oxygen availability **increases** *B. subtilis* biomass and substrate-use rate relative to anoxic alternatives | 10.1186/s13068-022-02253-4; January 2023 | Aerobic cultures reached OD₆₀₀=5.1, doubled in 1.6 h, and consumed glucose at 2.3 mM h⁻¹; anode systems remained below OD₆₀₀ 2 and 0.7 mM h⁻¹. | **Strong quantitative phenotype edge for strain 168.** The study also observed lysis/limited consumption under fully anaerobic nitrate/anode conditions, so avoid overgeneralizing robust anaerobic growth. (sun2023anodeassistedelectrofermentationwith pages 7-9)

The strongest seed graph is summarized below.

| subject | predicate | object | model taxon | confidence | key DOI |
|---|---|---|---|---|---|
| O2 | inactivates | FNR [4Fe-4S] cluster via [4Fe-4S]→[2Fe-2S] conversion with loss of DNA-binding activity | *Escherichia coli* | high; taxon-specific (unden2021sensingofo2 pages 1-7) | 10.1073/pnas.94.12.6087 |
| anoxia / low O2 | activates | FNR DNA-binding dimer state | *Escherichia coli* | high; taxon-specific (unden2021sensingofo2 pages 1-7) | 10.1111/1462-2920.15293 |
| oxidized quinone pool | inhibits | ArcB kinase activity, lowering ArcA phosphorylation | *Escherichia coli* | moderate-high; taxon-specific (levanon2005effectofoxygen pages 1-2) | 10.1128/jb.00406-13 |
| ArcA-P | represses | aerobic carbon oxidation and TCA / respiratory modules | *Escherichia coli* | high; taxon-specific (levanon2005effectofoxygen pages 1-2, federowicz2014determiningthecontrol pages 7-10) | 10.1002/bit.20381 |
| ArcA-P | promotes / shifts toward | microaerobic-fermentative program | *Escherichia coli* | moderate-high; taxon-specific (levanon2005effectofoxygen pages 1-2, bafna‐ruhrer2024combinedoxygenand pages 7-9) | 10.1002/bit.20381 |
| nitrate | activates | NarX/NarL two-component signaling | *Escherichia coli* | high; taxon-specific (unden2021sensingofo2 pages 1-7) | 10.1111/1462-2920.15293 |
| FNR + NarL + nitrate | activates expression of | narGHJI nitrate reductase operon | *Escherichia coli* | high; taxon-specific (unden2021sensingofo2 pages 1-7) | 10.1111/1462-2920.15293 |
| cytochrome bd oxidase | enables | low-O2 / microaerobic respiration via high O2 affinity | *Escherichia coli* | high; taxon-specific though broad family relevance (borisov2015oxygenasacceptor pages 2-4, borisov2015oxygenasacceptor pages 11-13) | 10.1128/ecosalplus.esp-0012-2015 |
| O2 | enables | aerobic respiration | bacteria, including facultative anaerobes | high; broad but not universal module composition (unden2021sensingofo2 pages 1-7, bueno2012bacterialadaptationof pages 1-2) | 10.1089/ars.2011.4051 |
| absence of O2 + nitrate | enables | nitrate respiration | bacteria; directly evidenced in *E. coli* | high for *E. coli*, broader claim should be curated cautiously (unden2021sensingofo2 pages 1-7) | 10.1111/1462-2920.15293 |
| absence of terminal electron acceptor | favors | fermentation | bacteria; directly evidenced in facultative models | moderate; generalized from facultative model systems (unden2021sensingofo2 pages 1-7, federowicz2014determiningthecontrol pages 7-10) | 10.1371/journal.pgen.1004264 |


*Table: This table compiles the strongest evidence-supported causal triples for a TraitMech graph of facultative oxygen preference, emphasizing well-established regulatory switches and respiratory options. It is useful as a compact seed set for curation because it marks taxon scope and confidence while tying each claim to a key DOI and supporting context IDs.*

## Recent developments and current applications

### Dynamic industrial bioreactors

The 2024 *E. coli* scale-down study is especially relevant because facultative behavior in production vessels is not a static comparison between two bottles. Large reactors contain moving glucose and oxygen gradients. Ten-minute oxygen oscillations changed TCA-cycle and terminal-oxidase expression, reduced biomass, drove acetate accumulation, activated stress programs, and left persistent transcriptional effects after oxygen limitation stopped. Combined glucose-plus-oxygen oscillations differed from either perturbation alone, showing that oxygen preference must be curated with nutrient context and exposure history. (bafna‐ruhrer2024combinedoxygenand pages 7-9, bafna‐ruhrer2024combinedoxygenand pages 10-11, bafna‐ruhrer2024combinedoxygenand pages 1-2)

### Metabolic engineering and electro-fermentation

Facultative switching is exploited through aerobic biomass-building phases followed by oxygen-limited production phases. In *B. subtilis*, limited aeration enabled electron disposal to nitrate or a poised anode and shifted product distributions. Charge transfer reached 926.2±22.7 C under limited aeration, and acetoin reached 17.8±0.6 mM with a poised anode versus 9.7±2.0 mM at open circuit. These results support process-control edges from oxygen/electron-acceptor availability to redox balance and product spectrum, but not a natural ecological edge from “anode” to METPO:1000612. (sun2023anodeassistedelectrofermentationwith pages 5-7, sun2023anodeassistedelectrofermentationwith pages 10-11)

A 2024 synthetic-biology study additionally combined fermentative metabolism with selected respiratory modules in *E. coli*, illustrating that controlled oxygen use can rebalance otherwise redox-infeasible fermentations. This is an engineering implementation of the same organizing principle—respiration supplies an adjustable electron sink while fermentation preserves high product yield—but engineered strains should not be used to infer necessity in wild-type facultative organisms.

### Infection and antimicrobial targeting

Facultative pathogens can move between oxygenated host surfaces, hypoxic inflamed tissue, intracellular niches, and anoxic gut environments. Their aerobic chains can themselves consume O₂ and intensify “infectious hypoxia.” The overrepresentation of facultative organisms among WHO priority pathogens supports clinical relevance but is associative, not proof that facultative metabolism alone causes virulence. (andre2021theselectiveadvantage pages 1-2)

Cytochrome bd is a promising antibacterial target because it is bacterial, supports low-O₂ respiration, and increases resistance to NO, peroxide, sulfide, and CO. Nevertheless, bd oxidase is neither exclusive to facultative organisms nor universally required by them. The 2024 CO study also demonstrates paralogue- and taxon-specific behavior: *E. coli* bd-I was substantially more CO-resistant than bd-II or bo₃, so “cytochrome bd” should not be represented as one functionally uniform node. (nastasi2024membraneboundredoxenzyme pages 2-4, nastasi2024membraneboundredoxenzyme pages 11-13)

### Current expert interpretation

Authoritative reviews converge on a layered model rather than a binary oxygen switch. FNR directly senses O₂ through cluster chemistry; ArcAB senses respiratory-chain/redox consequences; acceptor-specific systems such as NarXL sense nitrate; and terminal-oxidase repertoires tune respiration across oxygen concentrations. The 2024 evolutionary analysis further emphasizes that respiration is only one aspect of adaptation to O₂: oxygen-sensitive biosynthesis and oxygen-detoxification pathways also shaped microbial physiology. Therefore, oxygen tolerance, oxygen-dependent biosynthesis, and facultative energy metabolism should be represented as connected but distinct graph branches. (bueno2012bacterialadaptationof pages 1-2, mrnjavac2024theradicalimpact pages 7-9)

## Recommended minimal YAML-ready core

A conservative first revision of `facultative_oxygen_preference.yaml` should contain the following *E. coli*-anchored mechanism and explicit context qualifiers:

1. `molecular oxygen -> inactivates -> FNR-[4Fe-4S] DNA-binding dimer`
2. `anoxia -> stabilizes -> active FNR-[4Fe-4S] dimer`
3. `quinone-pool redox state -> regulates -> ArcB kinase`
4. `ArcB kinase -> phosphorylates -> ArcA`
5. `ArcA-P -> represses -> aerobic carbon-oxidation/TCA modules`
6. `low oxygen -> promotes -> cytochrome bd-I expression`
7. `cytochrome bd-I -> enables -> microoxic aerobic respiration`
8. `nitrate -> activates -> NarX/NarL`
9. `active FNR AND NarL-P -> activates -> narGHJI nitrate reductase expression`
10. `narGHJI nitrate reductase -> enables -> nitrate respiration`
11. `absence of usable terminal electron acceptor -> favors -> fermentation`
12. `aerobic respiration OR anaerobic respiration OR fermentation -> enables conditionally -> growth across oxygen regimes`
13. `growth across oxic and anoxic regimes -> realizes -> METPO:1000612`

The final OR/AND logic is essential. Neither nitrate respiration nor fermentation is universally required: some facultative organisms use one, some the other, and many use both depending on substrate and acceptor availability.

## Claims not yet suitable for TraitMech curation

1. **“FNR causes facultative oxygen preference in all microbes.”** False as a universal statement; FNR families are phylogenetically restricted and nonhomologous O₂ sensors evolved independently.
2. **“ArcB directly senses oxygen.”** Over-simplified. In canonical *E. coli*, ArcB principally responds to quinone/redox state, and exact signal chemistry remains debated; *H. influenzae* PAS-less ArcB may sense different metabolic signals. (alvarez2024diversificationofsignal pages 14-15)
3. **A single polarity for every quinone→ArcB edge.** Ubiquinone, menaquinone, demethylmenaquinone, their reduction states, growth phase, and medium can alter the observed relationship. Curate the general modulation edge first.
4. **“Cytochrome bd is required for facultative growth.”** It supports microoxia and stress resistance in many taxa but is not universal and also occurs in organisms labeled anaerobic.
5. **ROS-detoxification enzyme→facultative trait as a sufficient edge.** Catalase, superoxide dismutase, NADH oxidases, and rubredoxin oxidoreductases support oxygen tolerance, not necessarily oxic growth.
6. **Anoxic nitrate growth inferred from genes alone.** Presence of `nar` genes or a genome-scale reconstruction does not establish expressed, energy-conserving growth; require phenotype or flux evidence.
7. **Survival, CFU persistence, or inhibitor resistance equated with growth.** CO/NO/peroxide resistance should remain an accessory branch.
8. **Anode-assisted respiration as a natural mechanism.** It is an engineered application and experimental factor.
9. **Generalizing *B. subtilis* strain 168 as robustly growing anaerobically with nitrate or an anode.** The 2023 experiment observed immediate lysis and very limited glucose consumption under fully anaerobic sole-acceptor conditions; only limited aeration supported useful electro-fermentation. (sun2023anodeassistedelectrofermentationwith pages 5-7, sun2023anodeassistedelectrofermentationwith pages 7-9)
10. **Using oxygen oscillation results without temporal qualifiers.** The 2024 data derive from 10-minute scale-down cycles and high-density fed-batch conditions, not steady-state natural environments. (bafna‐ruhrer2024combinedoxygenand pages 10-11)
11. **Merging bacterial and yeast mechanisms.** The phenotype can be shared, but mitochondrial respiration, sterol/unsaturated-fatty-acid oxygen requirements, Crabtree effects, and yeast redox shuttles require a separate taxon-specific graph.
12. **Unverified CURIEs.** Exact ENVO terms, Fe–S CHEBI classes, quinone isoprenologues, stereospecific fermentation products, strain-level UniProt entries, EC numbers, Rhea reactions, and GO nitrate-respiration terms should be validated against current ontology releases before commit.

## DOI-first bibliography

1. **10.1111/1751-7915.70051** — Bafna-Rührer J, Orth JV, Sudarsan S. “Combined oxygen and glucose oscillations distinctly change the transcriptional and physiological state of *Escherichia coli*.” *Microbial Biotechnology*. **November 2024**. https://doi.org/10.1111/1751-7915.70051 (bafna‐ruhrer2024combinedoxygenand pages 7-9)
2. **10.1371/journal.pone.0315238** — Alvarez AF et al. “Diversification of signal identity and modus operandi of the *Haemophilus influenzae* PAS-less ArcB sensor kinase.” *PLOS ONE*. **December 2024**. https://doi.org/10.1371/journal.pone.0315238 (alvarez2024diversificationofsignal pages 14-15)
3. **10.1002/1873-3468.14906** — Mrnjavac N et al. “The radical impact of oxygen on prokaryotic evolution.” *FEBS Letters*. **May 2024**. https://doi.org/10.1002/1873-3468.14906 (mrnjavac2024theradicalimpact pages 7-9)
4. **10.3390/ijms25021277** — Nastasi MR, Borisov VB, Forte E. “Membrane-Bound Redox Enzyme Cytochrome bd-I Promotes Carbon Monoxide-Resistant *Escherichia coli* Growth and Respiration.” *International Journal of Molecular Sciences*. **January 2024**. https://doi.org/10.3390/ijms25021277 (nastasi2024membraneboundredoxenzyme pages 2-4)
5. **10.3390/inorganics11120450** — Crack JC et al. “Probing the Reactivity of [4Fe–4S] FNR with O₂ and NO.” *Inorganics*. **November 2023**. https://doi.org/10.3390/inorganics11120450
6. **10.1186/s13068-022-02253-4** — Sun Y, Kokko M, Vassilev I. “Anode-assisted electro-fermentation with *Bacillus subtilis* under oxygen-limited conditions.” *Biotechnology for Biofuels and Bioproducts*. **January 2023**. https://doi.org/10.1186/s13068-022-02253-4 (sun2023anodeassistedelectrofermentationwith pages 5-7)
7. **10.1093/nar/gkad750** — Lamoureux CR et al. “A multi-scale expression and regulation knowledge base for *Escherichia coli*.” *Nucleic Acids Research*. **September 2023**. https://doi.org/10.1093/nar/gkad750 (lamoureux2023amultiscaleexpression pages 17-17)
8. **10.1128/mmbr.00110-21** — Brown AN et al. “The ArcAB Two-Component System: Function in Metabolism, Redox Control, and Infection.” *Microbiology and Molecular Biology Reviews*. **June 2022**. https://doi.org/10.1128/mmbr.00110-21
9. **10.1111/1462-2920.15293** — Unden G, Klein R. “Sensing of O₂ and nitrate by bacteria.” *Environmental Microbiology*. **November 2021**. https://doi.org/10.1111/1462-2920.15293 (unden2021sensingofo2 pages 1-7)
10. **10.1111/cmi.13338** — André AC, Debande L, Marteyn BS. “The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection.” *Cellular Microbiology*. **April 2021**. https://doi.org/10.1111/cmi.13338 (andre2021theselectiveadvantage pages 1-2)
11. **10.1089/ars.2020.8039** — Borisov VB et al. “Bacterial Oxidases of the Cytochrome bd Family.” *Antioxidants & Redox Signaling*. **June 2021**. https://doi.org/10.1089/ars.2020.8039 (borisov2021bacterialoxidasesof pages 18-19)
12. **10.1089/ars.2011.4051** — Bueno E et al. “Bacterial adaptation of respiration from oxic to microoxic and anoxic conditions: redox control.” *Antioxidants & Redox Signaling*. **April 2012**. https://doi.org/10.1089/ars.2011.4051 (bueno2012bacterialadaptationof pages 1-2)
13. **10.1371/journal.pgen.1004264** — Federowicz S et al. “Determining the Control Circuitry of Redox Metabolism at the Genome-Scale.” *PLOS Genetics*. **April 2014**. https://doi.org/10.1371/journal.pgen.1004264 (federowicz2014determiningthecontrol pages 7-10)
14. **10.1128/ecosalplus.esp-0012-2015** — Borisov VB, Verkhovsky MI. “Oxygen as Acceptor.” *EcoSal Plus*. **October 2015**. https://doi.org/10.1128/ecosalplus.esp-0012-2015 (borisov2015oxygenasacceptor pages 2-4)
15. **10.1002/bit.20381** — Levanon SS, San KY, Bennett GN. “Effect of oxygen on the *Escherichia coli* ArcA and FNR regulation systems and metabolic responses.” *Biotechnology and Bioengineering*. **March 2005**. https://doi.org/10.1002/bit.20381 (levanon2005effectofoxygen pages 1-2)
16. **10.1073/pnas.94.12.6087** — Khoroshilova N et al. “Iron-sulfur cluster disassembly in the FNR protein of *Escherichia coli* by O₂.” *PNAS*. **June 1997**. https://doi.org/10.1073/pnas.94.12.6087

References

1. (unden2021sensingofo2 pages 1-7): Gottfried Unden and Robin Klein. Sensing of <scp>o<sub>2</sub></scp> and nitrate by bacteria: alternative strategies for transcriptional regulation of nitrate respiration by <scp>o<sub>2</sub></scp> and nitrate. Environmental Microbiology, 23:5-14, Nov 2021. URL: https://doi.org/10.1111/1462-2920.15293, doi:10.1111/1462-2920.15293. This article has 27 citations and is from a domain leading peer-reviewed journal.

2. (andre2021theselectiveadvantage pages 1-2): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 110 citations and is from a peer-reviewed journal.

3. (alvarez2024diversificationofsignal pages 14-15): Adrián F. Alvarez, Antonio de Jesús Santillán-Jiménez, Eder Flores-Tamayo, Juan L. Teran-Melo, Oscar J. Vázquez-Ciros, and Dimitris Georgellis. Diversification of signal identity and modus operandi of the haemophilus influenzae pas-less arcb sensor kinase. PLOS ONE, 19:e0315238, Dec 2024. URL: https://doi.org/10.1371/journal.pone.0315238, doi:10.1371/journal.pone.0315238. This article has 0 citations and is from a peer-reviewed journal.

4. (lamoureux2023amultiscaleexpression pages 17-17): Cameron R Lamoureux, Katherine T Decker, Anand V Sastry, Kevin Rychel, Ye Gao, John Luke McConn, Daniel C Zielinski, and Bernhard O Palsson. A multi-scale expression and regulation knowledge base for escherichia coli. Nucleic Acids Research, 51:10176-10193, Sep 2023. URL: https://doi.org/10.1093/nar/gkad750, doi:10.1093/nar/gkad750. This article has 62 citations and is from a highest quality peer-reviewed journal.

5. (levanon2005effectofoxygen pages 1-2): Sagit Shalel Levanon, Ka‐Yiu San, and George N. Bennett. Effect of oxygen on the escherichia coli arca and fnr regulation systems and metabolic responses. Biotechnology and bioengineering, 89 5:556-64, Mar 2005. URL: https://doi.org/10.1002/bit.20381, doi:10.1002/bit.20381. This article has 175 citations and is from a domain leading peer-reviewed journal.

6. (bafna‐ruhrer2024combinedoxygenand pages 7-9): Jonas Bafna‐Rührer, Jean V. Orth, and Suresh Sudarsan. Combined oxygen and glucose oscillations distinctly change the transcriptional and physiological state of escherichia coli. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70051, doi:10.1111/1751-7915.70051. This article has 7 citations and is from a peer-reviewed journal.

7. (borisov2015oxygenasacceptor pages 2-4): Vitaliy B. Borisov and Michael I. Verkhovsky. Oxygen as acceptor. Oct 2015. URL: https://doi.org/10.1128/ecosalplus.esp-0012-2015, doi:10.1128/ecosalplus.esp-0012-2015. This article has 121 citations.

8. (borisov2015oxygenasacceptor pages 11-13): Vitaliy B. Borisov and Michael I. Verkhovsky. Oxygen as acceptor. Oct 2015. URL: https://doi.org/10.1128/ecosalplus.esp-0012-2015, doi:10.1128/ecosalplus.esp-0012-2015. This article has 121 citations.

9. (nastasi2024membraneboundredoxenzyme pages 2-4): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 14 citations.

10. (nastasi2024membraneboundredoxenzyme pages 4-7): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 14 citations.

11. (federowicz2014determiningthecontrol pages 7-10): Stephen Federowicz, Donghyuk Kim, Ali Ebrahim, Joshua Lerman, Harish Nagarajan, Byung-kwan Cho, Karsten Zengler, and Bernhard Palsson. Determining the control circuitry of redox metabolism at the genome-scale. PLoS Genetics, 10:e1004264, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004264, doi:10.1371/journal.pgen.1004264. This article has 91 citations and is from a domain leading peer-reviewed journal.

12. (bafna‐ruhrer2024combinedoxygenand pages 10-11): Jonas Bafna‐Rührer, Jean V. Orth, and Suresh Sudarsan. Combined oxygen and glucose oscillations distinctly change the transcriptional and physiological state of escherichia coli. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70051, doi:10.1111/1751-7915.70051. This article has 7 citations and is from a peer-reviewed journal.

13. (bafna‐ruhrer2024combinedoxygenand pages 1-2): Jonas Bafna‐Rührer, Jean V. Orth, and Suresh Sudarsan. Combined oxygen and glucose oscillations distinctly change the transcriptional and physiological state of escherichia coli. Microbial Biotechnology, Nov 2024. URL: https://doi.org/10.1111/1751-7915.70051, doi:10.1111/1751-7915.70051. This article has 7 citations and is from a peer-reviewed journal.

14. (sun2023anodeassistedelectrofermentationwith pages 1-2): Yu Sun, Marika Kokko, and Igor Vassilev. Anode-assisted electro-fermentation with bacillus subtilis under oxygen-limited conditions. Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02253-4, doi:10.1186/s13068-022-02253-4. This article has 29 citations and is from a domain leading peer-reviewed journal.

15. (sun2023anodeassistedelectrofermentationwith pages 7-9): Yu Sun, Marika Kokko, and Igor Vassilev. Anode-assisted electro-fermentation with bacillus subtilis under oxygen-limited conditions. Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02253-4, doi:10.1186/s13068-022-02253-4. This article has 29 citations and is from a domain leading peer-reviewed journal.

16. (bueno2012bacterialadaptationof pages 1-2): Emilio Bueno, Socorro Mesa, Eulogio J. Bedmar, David J. Richardson, and Maria J. Delgado. Bacterial adaptation of respiration from oxic to microoxic and anoxic conditions: redox control. Antioxidants & redox signaling, 16 8:819-52, Apr 2012. URL: https://doi.org/10.1089/ars.2011.4051, doi:10.1089/ars.2011.4051. This article has 252 citations and is from a domain leading peer-reviewed journal.

17. (sun2023anodeassistedelectrofermentationwith pages 5-7): Yu Sun, Marika Kokko, and Igor Vassilev. Anode-assisted electro-fermentation with bacillus subtilis under oxygen-limited conditions. Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02253-4, doi:10.1186/s13068-022-02253-4. This article has 29 citations and is from a domain leading peer-reviewed journal.

18. (sun2023anodeassistedelectrofermentationwith pages 10-11): Yu Sun, Marika Kokko, and Igor Vassilev. Anode-assisted electro-fermentation with bacillus subtilis under oxygen-limited conditions. Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-022-02253-4, doi:10.1186/s13068-022-02253-4. This article has 29 citations and is from a domain leading peer-reviewed journal.

19. (nastasi2024membraneboundredoxenzyme pages 11-13): Martina R. Nastasi, Vitaliy B. Borisov, and Elena Forte. Membrane-bound redox enzyme cytochrome bd-i promotes carbon monoxide-resistant escherichia coli growth and respiration. International Journal of Molecular Sciences, 25:1277, Jan 2024. URL: https://doi.org/10.3390/ijms25021277, doi:10.3390/ijms25021277. This article has 14 citations.

20. (mrnjavac2024theradicalimpact pages 7-9): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 16 citations and is from a peer-reviewed journal.

21. (borisov2021bacterialoxidasesof pages 18-19): Vitaliy B. Borisov, Sergey A. Siletsky, Alessandro Paiardini, David Hoogewijs, Elena Forte, Alessandro Giuffrè, and Robert K. Poole. Bacterial oxidases of the cytochrome<i>bd</i>family: redox enzymes of unique structure, function, and utility as drug targets. Jun 2021. URL: https://doi.org/10.1089/ars.2020.8039, doi:10.1089/ars.2020.8039. This article has 149 citations and is from a domain leading peer-reviewed journal.