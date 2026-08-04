---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:08:14.226402'
end_time: '2026-08-04T02:14:33.815495'
duration_seconds: 379.59
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately alkaphilic
  trait_identifier: METPO:1003004
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_alkaphilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference in which an organism requires alkaline conditions
    (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
  parent_traits: METPO:1003000
  synonyms: obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
  evidence_summary: 'DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9
    and above (Supports the obligate alkaliphile definition.)'
  causal_graph_summary: 'obligately_alkaphilic_sodium_cycle_homeostasis: 14 nodes,
    13 edges'
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
- **Trait label:** obligately alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism requires alkaline conditions (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9 and above (Supports the obligate alkaliphile definition.)
- **Existing causal graph summary:** obligately_alkaphilic_sodium_cycle_homeostasis: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **obligately alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_alkaphilic.yaml`.

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
- **Trait label:** obligately alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism requires alkaline conditions (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9 and above (Supports the obligate alkaliphile definition.)
- **Existing causal graph summary:** obligately_alkaphilic_sodium_cycle_homeostasis: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **obligately alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_alkaphilic.yaml`.

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


# Curation-focused research report: obligately alkaphilic

## 1. Scope summary

**Trait:** obligately alkaphilic  
**Identifier:** **METPO:1003004**  
**Category:** ENVIRONMENT; **kind:** CLASS; **status:** REVIEWED  
**Parent:** METPO:1003000

This trait denotes a demonstrated **growth requirement for alkaline conditions**, typically with optimal or strong growth at pH ≥9 and no growth at neutral or acidic pH. The mechanistic phenotype is not merely survival in alkali: cells must maintain a cytoplasm substantially less alkaline than the medium while conserving energy despite an outward-to-inward pH gradient that opposes the usual productive proton gradient. In *Bacillus pseudofirmus* OF4, cytoplasmic pH remains ≤8.3 at external pH 10.8, a difference exceeding two pH units; its upper growth limit is about pH 11.4. (preiss2015alkaliphilicbacteriawith pages 4-5)

### Boundary cases

* **Facultative alkaliphile:** grows at both alkaline and neutral pH. The 2022 comparison explicitly defines obligate *Evansella clarkii* as unable to grow at neutral pH, whereas facultative *Sutcliffella cohnii* grows at both neutral and alkaline pH. (goto2022differencesinbioenergetic pages 2-3)
* **Alkalitolerant organism:** tolerates elevated pH but need not prefer or require it. It should not be annotated from an alkaline isolation site or maximum tolerated pH alone.
* **Haloalkaliphile:** combines alkaline adaptation with salinity/Na-carbonate adaptation. Halophily, ectoine production, and sodium requirement should be separate nodes or traits rather than treated as synonyms for obligate alkaliphily.
* **Assay caution:** growth range, optimum, endpoint pH, buffer, sodium concentration, carbon source, oxygen availability, and inoculum carryover all matter. A 2023 study noted substantial deviation between initial and final pH at range extremes and therefore used measured final pH. (khomyakova2023phenotypicandgenomic pages 2-3)
* **Taxonomic caution:** “obligate” may modify another property, such as obligate anaerobiosis or obligate acetotrophy, and does not imply obligate alkaliphily.

A recent boundary example is *Methanocrinis natronophilus* strain Mx: reported growth range pH 7.7–10.2 and optimum 9.3–9.5. It was called an obligate alkaliphile, but its lower reported limit is below the template’s “cannot grow at neutral pH” criterion. This should be represented with exact assay values and a qualification rather than silently generalized. (khomyakova2023phenotypicandgenomic pages 10-11)

## 2. Current mechanistic model

The best-supported graph is a coordinated **proton–sodium-cycle homeostasis system**:

1. External alkaline pH creates proton scarcity and an inverted ΔpH.
2. The respiratory chain exports protons and establishes a large, inside-negative membrane potential.
3. Electrogenic Mrp-family Na+/H+ antiport exports Na+ while importing more H+, acidifying the cytoplasm and converting proton motive force into sodium motive force.
4. Na+-coupled solute transport, MotPS flagellar stators, and NavBP channels replenish intracellular Na+, allowing antiport to continue.
5. Acidic surface polymers and membrane-associated components delay loss of respiratory protons into alkaline bulk medium.
6. Proton-coupled F1Fo ATP synthase uses the locally retained proton supply and electrical potential to synthesize ATP.

For *B. pseudofirmus* OF4, respiration proceeds through dehydrogenases and menaquinone to proton-pumping complexes III and IV. Although inverted ΔpH subtracts from the electrical component, the substantial ΔΨ leaves a low but productively oriented total proton-motive force. (preiss2015alkaliphilicbacteriawith pages 4-5)

| module/edge | representative taxon | evidence type | confidence | curation recommendation |
|---|---|---|---|---|
| external high pH -> inverted delta pH challenge / need to keep cytoplasm ~2 pH units lower | *Bacillus pseudofirmus* OF4; obligately alkaliphilic Bacillaceae | physiology + review synthesis with quantitative values (cytoplasmic pH <=8.3 at external pH 10.8; growth limit ~11.4) (preiss2015alkaliphilicbacteriawith pages 4-5, goto2022differencesinbioenergetic pages 1-2) | High | Curate as core trait-defining challenge/mechanism context |
| respiratory chain proton export -> membrane potential contributes to productive PMF at high pH | *Evansella clarkii*; alkaliphilic Bacillaceae | bioenergetic physiology/review; quantitative DeltaPsi ~-170 mV high aeration, ~-140 mV low aeration (goto2022differencesinbioenergetic pages 1-2, goto2022differencesinbioenergetic pages 2-3) | High | Curate as core edge, noting evidence strongest in Bacillaceae |
| Mrp Na+/H+ antiporter -> Na+ efflux coupled to H+ influx -> cytoplasmic pH homeostasis | *Alkalihalobacillus halodurans* C-125; *B. pseudofirmus* OF4 | genetic/physiology synthesis; repeatedly described as important/indispensable for Na cycle and pH homeostasis (goto2022differencesinbioenergetic pages 2-3, preiss2015alkaliphilicbacteriawith pages 4-5) | High | Curate as central core module |
| MotPS / NavBP / Na+-solute uptake -> replenished intracellular Na+ for antiport cycle | *B. pseudofirmus* OF4; *A. halodurans* C-125 | mechanistic physiology/review (motility channel, voltage-gated Na+ channel, Na+-coupled uptake routes) (preiss2015alkaliphilicbacteriawith pages 4-5) | Moderate-High | Curate as supportive sodium-cycle inputs; mark channel-specific edges as Bacillaceae-centered |
| proton-coupled F1Fo-ATP synthase -> ATP production under alkaline conditions | obligately alkaliphilic Bacillaceae; *Caldalkalibacillus thermarum* | biochemical/physiological synthesis; direct ATP synthase role established but exact high-pH microdomain mechanism partly unresolved (goto2022differencesinbioenergetic pages 1-2, jong2024quantitativeproteomicsreveals pages 1-2) | High | Curate as core energy-conservation edge; keep proton-retention submechanism separate |
| acidic secondary cell wall / S-layer components -> surface proton retention / delayed proton loss | *A. halodurans* C-125; *B. pseudofirmus* OF4 | mutant + physiological synthesis; acidic teichuronic/teichuronopeptide or SlpA-linked surface effects (goto2022differencesinbioenergetic pages 1-2, preiss2015alkaliphilicbacteriawith pages 12-13, horikoshi1999alkaliphilessomeapplications pages 4-5) | Moderate-High | Curate as core but note much evidence is from reviews summarizing older experiments |
| oxygen limitation -> increased membrane-bound cytochrome c / H+ capacitor | *Evansella clarkii* | aeration-dependent physiology/review; 2.5-6.3-fold increase under low aeration (goto2022differencesinbioenergetic pages 1-2) | Moderate | Curate only as conditional, taxon-specific branch |
| oxygen limitation -> Mrp downregulation, possibly lowered need for Mrp due to sodium:acetate export | *Caldalkalibacillus thermarum* TA2.A1 | 2024 chemostat proteomics; mechanistic interpretation partly hypothetical (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8) | Moderate | Curate cautiously as condition-dependent regulation, not universal trait logic |
| BpOF4_01690 -> supports respiratory chain / ATP synthase function and growth at high pH, low Na+ | *B. pseudofirmus* OF4 | direct deletion/complementation and enzyme activity assays (takahashi2018ahydrophobicsmall pages 2-4, takahashi2018ahydrophobicsmall pages 9-12, takahashi2018ahydrophobicsmall pages 1-2) | Moderate | Curate only as taxon-specific candidate, not generic obligate alkaliphily node yet |
| ectoine biosynthesis / single-subunit cation:proton antiporters -> alkaline adaptation | *Methanocrinis natronophilus* strain Mx and related methanogens | 2023 genomic inference + direct ectoine detection (~1.5 mg g-1 dry weight) (khomyakova2023phenotypicandgenomic pages 10-11) | Low-Moderate | Do not curate as general obligate alkaliphily edge yet; retain as uncertain archaeal branch |
| absence of Mrp/Mnh with alternative antiport strategy | *Methanocrinis* spp. | comparative genomics/inference only (khomyakova2023phenotypicandgenomic pages 10-11) | Low | Warning: not ready for TraitMech core graph without direct functional validation |


*Table: This table prioritizes candidate mechanistic modules for curating obligate alkaliphily (METPO:1003004), distinguishing core broadly supported edges from conditional or taxon-specific branches. It is useful for deciding what belongs in the initial TraitMech graph versus what should remain provisional.*

## 3. Candidate nodes grouped by type

### Trait and environmental/experimental nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| obligately alkaphilic | **METPO:1003004** | Use verbatim CURIE supplied by the template. |
| alkaline growth condition | ENVO label-level candidate; pH represented as assay datum | Do not collapse pH 9, 10.5, and 12 into one unqualified exposure. |
| external pH | label-only measurement node | Store initial and preferably final measured pH. |
| low Na+ / high Na+ | CHEBI:29101 for sodium(1+) | Concentration is an experimental modifier, not intrinsically beneficial. |
| oxygen availability / aeration | CHEBI:15379 for dioxygen plus assay-condition node | Strongly modifies respiratory mechanisms. |
| cytoplasmic pH | label-only quantitative state | Distinguish measurement from “pH homeostasis” process. |
| inverted transmembrane ΔpH | label-only biophysical state | More acidic inside than outside. |
| membrane potential, inside negative | GO:0051881, regulation of mitochondrial membrane potential, is inappropriate for bacteria; retain label-only pending ontology review | Record measured millivolts when available. |
| proton-motive force | label-only or verified GO term during curation | Sum of electrical and chemical components. |
| sodium-motive force | label-only | Generated partly through antiport. |

### Chemicals, ions, metabolites, and electron acceptors

| Node | Grounding | Role |
|---|---|---|
| proton | CHEBI:15378 | Imported by antiport; retained near surface; drives ATP synthase. |
| sodium(1+) | CHEBI:29101 | Antiporter substrate and coupling ion for transport/motility. |
| potassium(1+) | CHEBI:29103 | Alternative cation-cycle contributor in some strains. |
| hydroxide | CHEBI:16234 | High external activity; negatively charged surfaces are proposed to exclude it. |
| dioxygen | CHEBI:15379 | Terminal electron acceptor in the aerobic Bacillaceae model. |
| menaquinone | CHEBI:16374 | Respiratory electron carrier; exact menaquinone species may vary. |
| ATP | CHEBI:15422 | Product of F1Fo ATP synthase. |
| ADP | CHEBI:16761 | ATP-synthesis substrate. |
| ectoine | CHEBI:39084 | Osmoprotection branch in haloalkaliphilic archaea; not a universal alkaliphily mechanism. |
| acetate | CHEBI:30089 | Methanogenic substrate and proposed Na+-coupled export partner under oxygen limitation; latter remains hypothetical. |

### Genes, proteins, complexes, and cellular structures

| Candidate | Suggested grounding | Evidence scope |
|---|---|---|
| Mrp/Mnh multisubunit Na+/H+ antiporter | GO:0015385, sodium:proton antiporter activity, for activity; complex itself should remain label-only unless a verified complex term is selected | Central in *A. halodurans* C-125 and *B. pseudofirmus* OF4, but absent in examined *Methanocrinis* genomes. |
| single-subunit cation:H+ antiporters | GO activity-level candidate; exact families unresolved | Genomic alternative in *Methanocrinis*; uncertain function. |
| MotPS Na+-driven flagellar stator | label-only until taxon-specific protein IDs are verified | Supplies Na+ influx while powering motility. |
| NavBP voltage-gated Na+ channel | label-only; use verified UniProt only during YAML curation | Sodium-cycle input in *B. pseudofirmus* OF4. |
| Ktr K+ importer | label-only complex | Potassium-cycle input. |
| F-type H+-transporting ATP synthase | GO:0045259 for proton-transporting ATP synthase complex; verify ontology version | ATP production and proton return. |
| complex III, menaquinol:cytochrome-c oxidoreductase | label-only complex or appropriate GO complex after verification | Proton-pumping respiratory module. |
| cytochrome-c oxidase / complex IV | GO:0005751 is mitochondrial and unsuitable; use bacterial molecular-function/complex term after verification | Pumps protons and reduces O2. |
| cytochrome aa3 and ba3 oxidases | label-only pending exact complex grounding | Oxygen-dependent respiratory alternatives. |
| membrane-bound cytochrome c with Asn-rich segment | label-only | Proposed surface H+ capacitor in *E. clarkii*. |
| acidic secondary cell-wall polymers | label-only | Includes teichuronic acid and teichuronopeptide. |
| SlpA/SlaA acidic S-layer protein | label-only; locus/protein IDs require strain verification | Surface proton-retention candidate. |
| BpOF4_01690 | label-only locus-specific node | 59-aa hydrophobic membrane protein; direct deletion phenotype but narrow taxonomic scope. |
| cardiolipin-rich membrane | CHEBI:28494 for cardiolipin | Proposed delay of proton equilibration; mechanism not directly established. |
| flotillin-T/A and NfeD proteins | label-only | Proposed microdomain/proton-compartmentalization branch; insufficient mutant validation. |
| EctA, EctB, EctC | EC or UniProt IDs only after strain-specific verification | Ectoine synthesis in *Methanocrinis*; primarily osmoprotection. |

### Processes and pathways

Candidate process nodes include cytoplasmic pH homeostasis; electrogenic Na+/H+ antiport; sodium-ion cycling; respiratory electron transport; proton translocation; oxidative phosphorylation; ATP synthesis; sodium-coupled solute uptake; sodium-driven flagellar rotation; surface proton retention; acid production; membrane microdomain organization; and ectoine biosynthesis/osmoprotection. Use GO:0006814 for sodium-ion transport and GO:0006091 for generation of precursor metabolites and energy only where their breadth is acceptable; narrower verified terms are preferable.

## 4. Candidate evidence-backed causal edges

Predicates are intentionally simple and YAML-friendly. “High” indicates direct physiology or intervention plus coherent mechanism; “moderate” indicates strong association or older experiments summarized by a review; “uncertain” denotes genomic inference or an unresolved molecular interpretation.

| # | Subject — predicate → object | Reference and supporting snippet | Notes/confidence |
|---:|---|---|---|
| 1 | external alkaline pH — **creates** → inverted transmembrane ΔpH | Preiss et al. 2015: “cytoplasmic pH of ≤8.3 at an external pH of 10.8.” DOI: [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075). (preiss2015alkaliphilicbacteriawith pages 4-5) | **High**, quantitative *B. pseudofirmus* OF4 physiology. |
| 2 | inverted ΔpH — **reduces** → bulk proton-motive force available for ATP synthesis | Goto et al. 2022: “the H+ concentration required for driving ATP synthesis…does not occur under the alkaline conditions.” DOI: [10.3389/fmicb.2022.842785](https://doi.org/10.3389/fmicb.2022.842785). (goto2022differencesinbioenergetic pages 1-2) | **High** thermodynamic relationship; bulk PMF does not exclude local surface proton transfer. |
| 3 | proton-pumping respiratory chain — **generates** → membrane potential and PMF | Preiss et al. 2015: complexes III and IV “pump protons out of the cell”; ΔΨ plus inverted ΔpH yields “a low but productively oriented bulk PMF.” (preiss2015alkaliphilicbacteriawith pages 4-5) | **High** in aerobic Bacillaceae; not universal to fermenters or anaerobes. |
| 4 | high aeration — **supports** → approximately −170 mV ΔΨ in *E. clarkii* | Goto et al. 2022: “high ΔΨ (ca. −170 mV)” under high aeration, falling to “∼−140 mV” at low aeration. (goto2022differencesinbioenergetic pages 1-2) | **Moderate–high**, quantitative but taxon- and aeration-specific. |
| 5 | Mrp Na+/H+ antiporter — **exports/imports** → Na+ outward / H+ inward | Goto et al. 2022: Mrp Na+ efflux translates H+-based PMF “to the Na+-based potential,” concomitant with increasing intracellular H+. (goto2022differencesinbioenergetic pages 2-3) | **High** core mechanistic edge for the two Bacillaceae models. |
| 6 | Mrp-mediated H+ influx — **maintains** → lower cytoplasmic pH | Preiss et al. 2015: cation/proton antiporters are “indispensable” for cytoplasmic pH more than two units below medium pH. (preiss2015alkaliphilicbacteriawith pages 4-5) | **High** in extreme alkaliphilic Bacillaceae; avoid universal taxonomic assertion. |
| 7 | Na+-coupled solute uptake — **replenishes** → intracellular Na+ | Preiss et al. 2015: solute pathways take up solutes with Na+, favored by the inward sodium gradient. (preiss2015alkaliphilicbacteriawith pages 4-5) | **Moderate–high** sodium-cycle module. |
| 8 | MotPS Na+ channel — **imports** → Na+ during flagellar rotation | Preiss et al. 2015: MotPS sodium channels power motility; influx “complete[s] a sodium-ion cycle.” (preiss2015alkaliphilicbacteriawith pages 4-5) | **Moderate–high**, Bacillaceae-specific. |
| 9 | NavBP voltage-gated channel — **imports** → Na+ | Preiss et al. 2015: NavBP influx contributes to completion of the sodium cycle. (preiss2015alkaliphilicbacteriawith pages 4-5) | **Moderate–high**, *B. pseudofirmus* OF4-specific. |
| 10 | Na+ influx pathways — **enable continued substrate supply for** → Na+/H+ antiport | Preiss et al. 2015: continuous availability of efflux cation is “crucial” so antiporters can exchange it for external protons. (preiss2015alkaliphilicbacteriawith pages 4-5) | **High** systems-level edge. |
| 11 | acidic secondary cell-wall polymers — **attract/delay loss of** → surface H+ | Goto et al. 2022: acidic components “will attract H+ around the cell surface” and “delay the rapid loss of H+” to alkaline bulk medium. (goto2022differencesinbioenergetic pages 1-2) | **Moderate**; physical interpretation is strong, exact proton microdomain remains difficult to measure. |
| 12 | loss of acidic surface layer/SCWP — **reduces** → alkaline growth capacity | Goto et al. 2022 reports slower growth of an S-layer-deficient mutant, especially at low Na+; Preiss et al. notes reduced alkaliphily after mutational loss of negatively charged SCWPs. (goto2022differencesinbioenergetic pages 1-2, preiss2015alkaliphilicbacteriawith pages 12-13) | **Moderate–high**, intervention evidence summarized in reviews. Verify primary mutant paper before final YAML citation if possible. |
| 13 | locally retained respiratory protons — **supply** → proton-coupled F1Fo ATP synthase | Preiss et al. 2015 describes lateral movement of retained protons to PMF users before bulk equilibration. (preiss2015alkaliphilicbacteriawith pages 4-5) | **Moderate/uncertain mechanism**; retain as a proposed local-coupling edge rather than settled molecular channeling. |
| 14 | proton-coupled F1Fo ATP synthase — **produces** → ATP | Goto et al. 2022: alkaliphilic Bacillaceae use H+ for ATP synthase while Na+ powers many transport and motility functions. (goto2022differencesinbioenergetic pages 2-3) | **High**, core energy-conservation edge. |
| 15 | low aeration — **increases** → membrane-bound cytochrome c abundance | Goto et al. 2022: *E. clarkii* produced “2.5–6.3-fold higher” membrane-bound cytochrome c under low versus high aeration. (goto2022differencesinbioenergetic pages 1-2) | **Moderate–high**, quantitative and conditional. |
| 16 | Asn-rich membrane-bound cytochrome c — **promotes** → surface H+-bond network/H+ capacitance | Goto et al. 2022: the extra Asn-rich segment “may influence” formation of an H+-bond network. (goto2022differencesinbioenergetic pages 1-2) | **Uncertain**, author-proposed mechanism; curate only with uncertainty. |
| 17 | deletion of BpOF4_01690 — **impairs** → growth at pH 10.5 under low Na+ | Takahashi et al. 2018: deletion caused significantly weaker growth in malate- and glucose-based media; complementation restored the locus. DOI: [10.3389/fmicb.2018.01994](https://doi.org/10.3389/fmicb.2018.01994). (takahashi2018ahydrophobicsmall pages 2-4, takahashi2018ahydrophobicsmall pages 1-2) | **High phenotype causality**, but locus is taxon-specific. |
| 18 | deletion of BpOF4_01690 — **decreases** → respiratory-chain and ATPase activities | At pH 10.5/25 mM Na+, Δ01690 had lower NADH oxidase, NADH-ferricyanide reductase, succinate dehydrogenase, TMPD oxidase, and F1Fo-ATPase activities; 400 mM Na+ partially restored some activities. (takahashi2018ahydrophobicsmall pages 9-12) | **High experimental association**, but whether the protein directly transfers protons is unresolved. |
| 19 | BpOF4_01690 — **may facilitate** → coupling between respiration and ATP synthase | High-molecular-weight fractions contained both caa3 oxidase and ATP synthase, but pull-down failed to co-purify them. (takahashi2018ahydrophobicsmall pages 7-9) | **Uncertain**; do not encode direct physical interaction. |
| 20 | decreasing oxygen — **downregulates** → Mrp abundance in *C. thermarum* | de Jong et al. 2024 chemostats spanning 0.25–4.2% O2 found Mrp significantly downregulated at lower O2. DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8) | **Moderate–high regulatory association**; organism is thermoalkaliphilic, and the result is not proof that Mrp is dispensable. |
| 21 | lower O2 — **shifts abundance from** → aa3 toward ba3 oxidase | de Jong et al. 2024: aa3 was highest at 4.2% O2; ba3 dominated at most lower O2 levels and declined below 0.42% O2. (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8) | **Moderate–high**, proteomic remodeling; not a defining obligate-alkaliphily edge. |
| 22 | proposed Na+:acetate exporter — **may reduce requirement for** → Mrp under strong O2 limitation | de Jong et al. 2024 explicitly states no in-vivo or in-vitro acetate-export data and labels the replacement model a hypothesis. (jong2024quantitativeproteomicsreveals pages 6-8) | **Uncertain; do not curate as causal fact.** |
| 23 | ectABC pathway — **produces** → ectoine in strain Mx | Khomyakova et al. 2023 chemically detected ~1.5 mg ectoine g−1 dry weight at 0.6 M total Na+/pH 9.5, called the first direct evidence in archaea. DOI: [10.3389/fmicb.2023.1233691](https://doi.org/10.3389/fmicb.2023.1233691). (khomyakova2023phenotypicandgenomic pages 10-11) | **High for ectoine production; low for causing alkaliphily.** Primarily an osmoprotection edge. |
| 24 | single-subunit cation:H+ antiporters — **may maintain** → pH homeostasis in *Methanocrinis* | The 2023 genomes lacked Mrp/Mnh and authors proposed alternative single-subunit antiporters. (khomyakova2023phenotypicandgenomic pages 10-11) | **Uncertain genomic inference**, no functional perturbation. |
| 25 | acid production — **increases** → local proton availability / lowers ambient pH | Goto et al. 2022 notes acid generation from carbohydrate metabolism or amino-acid deamination and proposes increased H+ near the surface. (goto2022differencesinbioenergetic pages 2-3) | **Moderate/conditional**; likely medium- and metabolism-dependent, not a universal obligate mechanism. |

## 5. Recent developments, applications, and expert analysis

### 2023–2024 findings

The most important 2024 advance is the demonstration that the alkaliphile respiratory/ion-homeostasis network is **dynamically regulated by oxygen**, rather than being a fixed pathway. In *Caldalkalibacillus thermarum* TA2.A1 chemostats, cells grew from 0.25% to 4.2% inlet O2; Ndh-I and Ndh-II remained constitutive, aa3/ba3 oxidase abundance shifted with oxygen, and Mrp declined under oxygen limitation. The suggested substitution of Mrp function by Na+-coupled acetate export is explicitly hypothetical. (jong2024quantitativeproteomicsreveals pages 1-2, jong2024quantitativeproteomicsreveals pages 6-8)

The 2023 *Methanocrinis* study expands the trait beyond aerobic Bacillaceae. Strain Mx grew optimally at pH 9.3–9.5 with optimal total Na+ around 0.2–0.3 M, while direct chemistry detected ectoine at approximately 1.5 mg g−1 dry weight under 0.6 M Na+/pH 9.5. Both genomes lacked multisubunit Mrp/Mnh, showing that the Bacillaceae Mrp-centered graph cannot be asserted as universal. (khomyakova2023phenotypicandgenomic pages 10-11)

### Applications and real-world relevance

Obligate alkaliphily mechanisms inform engineering of high-pH biocatalysis, detergent enzymes, pulp bleaching, cyclodextrin production, alkaline waste treatment, soda-lake methane cycling, and interpretation of serpentinizing ecosystems. Alkaliphile-derived enzymes are valuable because extracellular proteins and cell-envelope systems operate under conditions that destabilize ordinary enzymes; however, enzyme alkali stability is a product property and should not itself be used as evidence that the producing organism is obligately alkaliphilic. The foundational review identifies both industrial applications and the bioenergetic importance of proton-coupled ATP synthesis at high pH. (preiss2015alkaliphilicbacteriawith pages 4-5)

For environmental implementation, the *Methanocrinis* result suggests that low-energy aceticlastic methanogenesis can operate in haloalkaline sediments, while oxygen-responsive respiratory plasticity in *C. thermarum* is relevant to hot-spring gradients and potentially alkaline aerobic bioreactors. These are ecological or engineering implications, not direct evidence that ectoine or a particular terminal oxidase causes the target trait. (khomyakova2023phenotypicandgenomic pages 10-11, jong2024quantitativeproteomicsreveals pages 1-2)

### Expert interpretation

The authoritative consensus is a **multi-adaptation model**, not a single “alkaliphily gene.” Antiport, ion recirculation, membrane potential, respiratory proton pumping, cell-surface charge, ATP synthase adaptation, and local proton retention cooperate. The strongest generic causal module is cytoplasmic pH homeostasis through cation:H+ antiport supplied by cation uptake. The least settled component is how respiratory protons reach ATP synthase before equilibrating with alkaline bulk medium; cell walls, lipids, microdomains, cytochrome c, and small membrane proteins are plausible contributors but should not be merged into one proven proton-channeling mechanism. (preiss2015alkaliphilicbacteriawith pages 12-13, preiss2015alkaliphilicbacteriawith pages 4-5)

## 6. Recommended initial TraitMech graph

For a conservative first revision of `obligately_alkaphilic.yaml`, prioritize this backbone:

1. alkaline external pH → causes → proton scarcity/inverted ΔpH challenge;
2. respiratory electron transport → generates → inside-negative ΔΨ;
3. respiratory electron transport → exports → H+;
4. Mrp Na+/H+ antiport → imports → H+;
5. Mrp Na+/H+ antiport → exports → Na+;
6. H+ import → maintains → lower cytoplasmic pH;
7. Na+-coupled solute uptake → imports → Na+;
8. MotPS/NavBP → imports → Na+;
9. intracellular Na+ replenishment → sustains → Mrp antiport;
10. acidic cell surface → delays loss of → surface H+;
11. ΔΨ plus locally available H+ → drives → F1Fo ATP synthase;
12. F1Fo ATP synthase → produces → ATP;
13. cytoplasmic pH homeostasis plus ATP production → enables → **METPO:1003004**.

Add conditional subgraphs for low-aeration cytochrome-c capacitance and oxygen-dependent terminal-oxidase/Mrp regulation. Keep BpOF4_01690 and archaeal ectoine/alternative antiporters in taxon-specific extensions.

## 7. Warnings: claims not ready for TraitMech curation

* Do **not** infer **METPO:1003004** from isolation at high pH, genome content, enzyme stability, or maximum tolerated pH without a growth-range assay demonstrating failure at neutral/acidic pH.
* Do not make Mrp universal: the 2023 *Methanocrinis* genomes lack Mrp/Mnh. (khomyakova2023phenotypicandgenomic pages 10-11)
* Do not encode a direct BpOF4_01690–ATP synthase or BpOF4_01690–caa3 physical interaction; co-fractionation was suggestive, while pull-down was negative. (takahashi2018ahydrophobicsmall pages 7-9)
* Do not curate the Na+:acetate exporter as replacing Mrp; the 2024 authors report no in-vivo or in-vitro export evidence. (jong2024quantitativeproteomicsreveals pages 6-8)
* Do not encode ectoine as causing obligate alkaliphily. Production is directly demonstrated, but its supported function is osmoprotection under haloalkaline conditions. (khomyakova2023phenotypicandgenomic pages 10-11)
* Do not treat surface proton microdomains as fully resolved. Proton retention is strongly motivated, but the relative contributions of SCWPs, cardiolipin, flotillins, cytochrome c, and respiratory supercomplexes remain incompletely tested. (preiss2015alkaliphilicbacteriawith pages 12-13)
* Do not generalize Bacillaceae respiratory edges to anaerobic archaea, fermenters, Gram-negative alkaliphiles, or fungi without taxon-specific evidence.
* Verify all GO/EC/UniProt identifiers against the current ontology and exact strain before YAML insertion; label-only nodes are preferable to incorrect grounding.

## 8. DOI-first bibliography

1. **de Jong SI et al.** “Quantitative proteomics reveals oxygen-induced adaptations in *Caldalkalibacillus thermarum* TA2.A1 microaerobic chemostat cultures.” *Frontiers in Microbiology* 15 (published **28 October 2024**). DOI: [10.3389/fmicb.2024.1468929](https://doi.org/10.3389/fmicb.2024.1468929). (jong2024quantitativeproteomicsreveals pages 1-2)
2. **Khomyakova MA et al.** “Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens…” *Frontiers in Microbiology* 14 (published **October 2023**). DOI: [10.3389/fmicb.2023.1233691](https://doi.org/10.3389/fmicb.2023.1233691). (khomyakova2023phenotypicandgenomic pages 10-11)
3. **Goto T et al.** “Differences in Bioenergetic Metabolism of Obligately Alkaliphilic Bacillaceae Under High pH Depend on the Aeration Conditions.” *Frontiers in Microbiology* 13 (published **18 March 2022**). DOI: [10.3389/fmicb.2022.842785](https://doi.org/10.3389/fmicb.2022.842785). (goto2022differencesinbioenergetic pages 1-2)
4. **Takahashi T, Krulwich TA, Ito M.** “A Hydrophobic Small Protein, BpOF4_01690, Is Critical for Alkaliphily of Alkaliphilic *Bacillus pseudofirmus* OF4.” *Frontiers in Microbiology* 9 (published **August 2018**). DOI: [10.3389/fmicb.2018.01994](https://doi.org/10.3389/fmicb.2018.01994). (takahashi2018ahydrophobicsmall pages 1-2)
5. **Preiss L et al.** “Alkaliphilic Bacteria with Impact on Industrial Applications, Concepts of Early Life Forms, and Bioenergetics of ATP Synthesis.” *Frontiers in Bioengineering and Biotechnology* 3 (published **June 2015**). DOI: [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075). (preiss2015alkaliphilicbacteriawith pages 4-5)
6. **Horikoshi K.** “Alkaliphiles: Some Applications of Their Products for Biotechnology.” *Microbiology and Molecular Biology Reviews* 63:735–750 (published **December 1999**). DOI: [10.1128/MMBR.63.4.735-750.1999](https://doi.org/10.1128/MMBR.63.4.735-750.1999). Foundational evidence includes cytoplasmic pH homeostasis, acidic cell-wall chemistry, and genetic restoration of alkaline growth by an antiporter-associated DNA fragment. (horikoshi1999alkaliphilessomeapplications pages 4-5)

References

1. (preiss2015alkaliphilicbacteriawith pages 4-5): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

2. (goto2022differencesinbioenergetic pages 2-3): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

3. (khomyakova2023phenotypicandgenomic pages 2-3): Maria A. Khomyakova, Alexander Y. Merkel, Alexander I. Slobodkin, and Dimitry Y. Sorokin. Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus methanocrinis gen.nov. within the family methanotrichaceae. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1233691, doi:10.3389/fmicb.2023.1233691. This article has 13 citations and is from a peer-reviewed journal.

4. (khomyakova2023phenotypicandgenomic pages 10-11): Maria A. Khomyakova, Alexander Y. Merkel, Alexander I. Slobodkin, and Dimitry Y. Sorokin. Phenotypic and genomic characterization of the first alkaliphilic aceticlastic methanogens and proposal of a novel genus methanocrinis gen.nov. within the family methanotrichaceae. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1233691, doi:10.3389/fmicb.2023.1233691. This article has 13 citations and is from a peer-reviewed journal.

5. (goto2022differencesinbioenergetic pages 1-2): Toshitaka Goto, Shinichi Ogami, Kazuaki Yoshimume, and Isao Yumoto. Differences in bioenergetic metabolism of obligately alkaliphilic bacillaceae under high ph depend on the aeration conditions. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.842785, doi:10.3389/fmicb.2022.842785. This article has 6 citations and is from a peer-reviewed journal.

6. (jong2024quantitativeproteomicsreveals pages 1-2): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

7. (preiss2015alkaliphilicbacteriawith pages 12-13): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

8. (horikoshi1999alkaliphilessomeapplications pages 4-5): Koki Horikoshi. Alkaliphiles: some applications of their products for biotechnology. Microbiology and Molecular Biology Reviews, 63:735-750, Dec 1999. URL: https://doi.org/10.1128/mmbr.63.4.735-750.1999, doi:10.1128/mmbr.63.4.735-750.1999. This article has 1281 citations and is from a domain leading peer-reviewed journal.

9. (jong2024quantitativeproteomicsreveals pages 6-8): Samuel I. de Jong, Martijn Wissink, Kadir Yildirim, Martin Pabst, Mark C. M. van Loosdrecht, and Duncan G. G. McMillan. Quantitative proteomics reveals oxygen-induced adaptations in caldalkalibacillus thermarum ta2.a1 microaerobic chemostat cultures. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1468929, doi:10.3389/fmicb.2024.1468929. This article has 4 citations and is from a peer-reviewed journal.

10. (takahashi2018ahydrophobicsmall pages 2-4): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

11. (takahashi2018ahydrophobicsmall pages 9-12): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

12. (takahashi2018ahydrophobicsmall pages 1-2): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

13. (takahashi2018ahydrophobicsmall pages 7-9): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.