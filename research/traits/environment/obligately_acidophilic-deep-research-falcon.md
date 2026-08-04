---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:03:25.853067'
end_time: '2026-08-04T02:10:00.441464'
duration_seconds: 394.59
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately acidophilic
  trait_identifier: METPO:1003006
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_acidophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by the requirement for acidic environments
    (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
  parent_traits: METPO:1003000
  synonyms: obligate acidophile
  evidence_summary: 'DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports
    acidophilic growth as a phenotype defined by acidic optimal pH.)'
  causal_graph_summary: 'obligately_acidophilic_ph_homeostasis: 14 nodes, 13 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the requirement for acidic environments (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate acidophile
- **Existing evidence:** DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports acidophilic growth as a phenotype defined by acidic optimal pH.)
- **Existing causal graph summary:** obligately_acidophilic_ph_homeostasis: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **obligately acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_acidophilic.yaml`.

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
- **Trait label:** obligately acidophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the requirement for acidic environments (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate acidophile
- **Existing evidence:** DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports acidophilic growth as a phenotype defined by acidic optimal pH.)
- **Existing causal graph summary:** obligately_acidophilic_ph_homeostasis: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **obligately acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_acidophilic.yaml`.

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


# Curation report: obligately acidophilic

**Trait:** obligately acidophilic  
**Identifier:** **METPO:1003006**  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** METPO:1003000  
**Synonym:** obligate acidophile

## 1. Scope summary

This trait should represent a **growth requirement**, not merely survival under acid stress: the organism grows only in acidic medium—under the supplied definition, below pH 5.5—and cannot grow at neutral or alkaline pH. The causal endpoint should therefore be **growth under an obligately acidic pH range**, supported by a measured growth curve or explicit minimum/maximum-growth-pH assay.

Important distinctions are:

- **Acid-tolerant / acid-resistant:** survives transient low-pH challenge but may grow optimally near neutrality; insufficient for this trait.
- **Acidophilic:** prefers acidic conditions, but published usage does not always establish failure to grow at neutral pH.
- **Moderate acidophile:** commonly reported growth range pH 3–7.5 and optimum pH 4–5; this category can include organisms that grow near neutrality and therefore is not automatically obligate acidophily. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4)
- **Extreme acidophile:** usually defined by optimum pH ≤3 (some literature uses growth at ≤3.5). This describes degree of acid preference, not logically the same property as obligacy. (vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2)
- **Polyextremophile:** acidophily combined with temperature, salinity, metal, or other adaptations; these additional traits should remain separate graph branches.

The mechanistic core is maintenance of a cytoplasm near pH 6–7 despite a strongly proton-rich exterior. Extreme acidophiles may face proton gradients of 10⁴–10⁵ fold. Direct measurements in *Methylacidiphilum* sp. RTK17.1 found intracellular pH 6.55 ± 0.05 over extracellular pH 1.5–3.0, illustrating the physiological endpoint but not proving that every obligate acidophile uses every proposed mechanism. (vergara2020evolutionofpredicted pages 1-3, gonzalezrosales2022integrativegenomicssheds pages 1-2, carere2021growthonformic pages 3-4)

**Curation recommendation:** retain the supplied pH <5.5 definition for METPO consistency, but require evidence of **absence of growth at neutral/alkaline pH**. Do not infer “obligately acidophilic” solely from an acidic optimum, habitat metadata, genome content, or the label “extreme acidophile.”

## 2. Current mechanistic model

Authoritative recent reviews divide acid homeostasis into two interacting defenses. A first line limits proton entry through low-permeability membranes, envelope proteins, and an inside-positive electrical potential. A second line removes or consumes protons that enter, through respiratory pumping, antiport, decarboxylation, and buffering. Comparative genomics indicates that acidophilic Acidithiobacillia gained hopanoid synthesis and redundant systems for generating positive membrane potential relative to inferred neutrophilic ancestors, but much of that evidence remains predictive because these organisms are difficult to manipulate genetically. (gonzalezrosales2022integrativegenomicssheds pages 1-2)

Direct perturbation evidence is strongest in *Methylacidiphilum* sp. RTK17.1. At external pH 2.5 it maintained intracellular pH 6.52 ± 0.04; growth occurred over pH 1–6 with optimum pH 2.5 and μmax 0.015 h⁻¹. Nigericin/valinomycin treatment acidified the cytoplasm, while formic acid lowered intracellular pH from 6.52 to 6.05 at 1 mM and inhibited batch growth. These observations causally connect intact ion gradients and cytoplasmic pH homeostasis to growth in acid. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 3-4)

## 3. Candidate nodes grouped by type

Identifiers below are supplied only where they are well-established and unambiguous. Gene-family labels are preferable to invented or strain-unspecified UniProt accessions.

### Trait and environmental nodes

- **obligately acidophilic** — METPO:1003006.
- **acidic environment / acidic growth medium** — candidate ENVO grounding should be selected according to the assayed habitat; retain label-only for generic culture pH.
- **extracellular pH below 5.5** — experimental-factor node; represent the numeric condition in evidence metadata.
- **high extracellular proton activity / proton gradient** — chemical/process node; proton: CHEBI:15378.
- **neutral or alkaline growth condition** — negative assay condition needed to establish obligacy.
- **growth**, **no growth**, **specific growth rate**, and **intracellular pH** — assay/output nodes.

### Cellular structures and locations

- cytoplasm — GO:0005737.
- plasma membrane — GO:0005886.
- outer membrane — GO:0019867, applicable to Gram-negative taxa only.
- cell envelope — GO:0030313.
- respiratory chain / membrane respiratory complexes — label or appropriate taxon-specific GO terms.

### Ions, chemicals, and metabolites

- proton — CHEBI:15378.
- potassium cation — CHEBI:29103.
- sodium cation — CHEBI:29101.
- spermidine — CHEBI:16610.
- glutamate — use the charge-state-specific CHEBI entity matching the reaction.
- γ-aminobutyrate/GABA — CHEBI:16865.
- arginine — use the charge-state-specific CHEBI entity matching the reaction.
- hopanoids — class-level CHEBI grounding should be verified per compound; do not assign one generic molecule without source specificity.
- formic acid — CHEBI:30751; a conditional inhibitor/uncoupling substrate in the cited assay.
- poly-γ-glutamate and alkaline amino-acid pool — candidate buffering nodes; grounding requires reaction/context review.

### Genes, proteins, and complexes

- **KdpABCDE/KdpABC**, K⁺-transporting ATPase; **Kch** potassium channel; **Trk** potassium uptake system; **Kef-type** potassium transporter.
- **NhaA/NhaP**, sodium/proton antiporters; **ClcA**, chloride/proton exchanger candidate.
- Respiratory **Complexes I, III, and IV**, proposed primary proton exporters in acidophilic methanotrophs. (yao2023howmethanotrophsrespond pages 5-7)
- **gadABC / Gad**, glutamate decarboxylase module; **adi / speA**, arginine decarboxylases.
- **hpnAIJKNHM**, predicted hopanoid-biosynthesis genes; **cfa**, cyclopropane-fatty-acyl-phospholipid synthase.
- **Omp40**, acidophile outer-membrane porin; **Slp**, starvation-inducible outer-membrane protein; **PspA**, membrane-stress protein.
- **ClpXP**, protease/chaperone-associated damage-control module.
- **Fur**, ferric uptake regulator implicated in regulation of acid-resistance, iron-transport, biofilm, and ISC-metabolism genes in *Fervidacidithiobacillus caldus*. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

### Processes and pathway modules

- membrane proton exclusion / low proton permeability.
- potassium uptake and generation of an inside-positive (“reversed”) membrane potential.
- proton export by respiration.
- cation/proton antiport.
- proton-consuming amino-acid decarboxylation.
- cytoplasmic buffering.
- membrane lipid remodeling and stabilization.
- macromolecular damage control/DNA repair.
- intracellular pH homeostasis — GO:0030003 is a candidate general grounding (“cellular cation homeostasis”), but a more precise GO term should be verified before release.

## 4. Candidate causal edges

The following compact graph distinguishes high-confidence physiological relations from genomic predictions.

| # | subject | predicate | object | best evidence type | confidence/curation status |
|---|---|---|---|---|---|
| 1 | Extracellular acidic pH (<5.5; often ≤3 in extreme acidophiles) | increases | transmembrane proton gradient | comparative physiology/review | High; broad trait-context edge suitable for curation (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) |
| 2 | Hopanoid-rich, saturated, or ether-/tetraether-enriched membrane | decreases | membrane proton permeability | comparative-genomic + taxon-specific physiological support | Medium; curate as generalized membrane adaptation with note on taxon-specific chemistry (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| 3 | Omp40 / Slp-like outer-membrane barrier | decreases | proton influx into cell envelope/cell | taxon-specific evidence + comparative prediction | Medium; curate cautiously as Gram-negative/taxon-limited first-line defense (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) |
| 4 | Kdp/Kch/Trk potassium uptake systems | increases | inside-positive (reversed) membrane potential | comparative-genomic prediction + indirect physiological support | Medium-High; strong recurrent mechanism, but often inferred outside direct knockout tests (vergara2020evolutionofpredicted pages 1-3, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, carere2021growthonformic pages 9-10) |
| 5 | Inside-positive membrane potential | decreases | inward proton influx | comparative physiology/review | High; central acidophile homeostasis edge (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2, yao2023howmethanotrophsrespond pages 5-7) |
| 6 | Respiratory complexes I/III/IV | exports | protons to outside of membrane | direct physiology in acidophilic methanotrophs + comparative review | Medium-High; mechanistically solid but enzyme-specific demonstration is taxon-dependent (yao2023howmethanotrophsrespond pages 5-7, carere2021growthonformic pages 4-5) |
| 7 | NhaA/NhaP and related cation/proton antiporters | removes | cytoplasmic protons | comparative-genomic prediction | Medium; curate as predicted second-line defense, annotate as inferred in many taxa (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| 8 | Glutamate decarboxylase / arginine decarboxylase systems | consumes | cytoplasmic protons | comparative-genomic prediction + broader acid-resistance literature | Medium; curate as proton-consuming buffering module with uncertainty for obligate acidophiles specifically (gonzalezrosales2022integrativegenomicssheds pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) |
| 9 | Cytoplasmic buffering (alkaline amino acids, poly-γ-glutamate, polyamines) | stabilizes | intracellular pH | comparative physiology/review | Medium; broad support but molecular contributors vary by taxon (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2) |
| 10 | Combined first- and second-line acid defenses | maintains | near-neutral cytoplasmic pH | direct physiology + comparative synthesis | High; core trait-mechanism edge (gonzalezrosales2022integrativegenomicssheds pages 1-2, carere2021growthonformic pages 4-5, carere2021growthonformic pages 3-4) |
| 11 | Maintained near-neutral cytoplasmic pH | enables | growth in acidic environments below pH 5.5 | direct physiology | High; directly supported by Methylacidiphilum growth/homeostasis measurements (carere2021growthonformic pages 4-5, carere2021growthonformic pages 1-2, carere2021growthonformic pages 3-4) |
| 12 | Formic acid influx (protonated weak acid) | acidifies | cytoplasm | direct Methylacidiphilum physiology | High; direct experimental edge suitable for conditional/assay-specific curation note (carere2021growthonformic pages 4-5, carere2021growthonformic pages 5-7) |
| 13 | Cytoplasmic acidification by formic acid | inhibits | growth under acidic conditions | direct Methylacidiphilum physiology | High; strong but substrate-specific negative edge (carere2021growthonformic pages 5-7, carere2021growthonformic pages 1-2) |
| 14 | Protonophore/ionophore collapse of PMF (e.g., nigericin/valinomycin) | disrupts | pH homeostasis / intracellular pH maintenance | direct Methylacidiphilum physiology | High; direct perturbation evidence, but assay-specific (carere2021growthonformic pages 4-5, carere2021growthonformic pages 2-3) |


*Table: This table summarizes candidate causal edges for curating obligately acidophilic mechanisms, distinguishing direct physiological evidence from comparative-genomic predictions and taxon-limited claims. It is useful as a compact draft edge list for TraitMech review and prioritization.*

### Evidence snippets and edge notes

1. **Acidic exterior → increased transmembrane proton gradient.** Supporting snippet: extreme acidophiles maintain near-neutral cytoplasm against gradients “up to 10⁵-fold.” This is a high-confidence physical/physiological edge. (gonzalezrosales2022integrativegenomicssheds pages 1-2)

2. **Hopanoid-, saturated-, or ether-rich membrane → reduced proton permeability.** Supporting snippets include “hopanoid lipids in cytoplasmic membranes” and increased saturated ether-containing AEG lipids in *Acididesulfobacillus acetoxydans* at pH 3.9–5.0. The broad membrane-barrier concept is strong, but the exact lipid solution is taxon-specific. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

3. **Omp40/Slp envelope proteins → reduced proton influx.** Supporting snippet: Omp40 occurs in the rigid, proton-resistant membrane of *Acidithiobacillus ferrooxidans*; Slps are classified as first-line defenses in *Leptospirillum*. This should be restricted to organisms with the relevant envelope architecture. (vergara2020evolutionofpredicted pages 1-3, dopson2023eurypsychrophilicacidophilesfrom pages 2-4)

4. **Kdp/Kch/Trk-mediated K⁺ uptake → inside-positive potential.** Supporting snippet: first-line defenses include an “inside-positive membrane potential … generated by potassium uptake via Kch, Kdp, and Trk transporters.” Potassium removal reduces acid resistance in *Sulfolobus* spp. and *Acidithiobacillus thiooxidans*, but individual transporter-to-trait links frequently remain genomic predictions. (vergara2020evolutionofpredicted pages 1-3)

5. **Inside-positive potential → electrostatic limitation of proton influx.** Recent reviews describe K⁺/Na⁺ accumulation generating an electrochemical barrier that repels protons. This is a central model across acidophiles, although the magnitude varies by taxon. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 2-4, yao2023howmethanotrophsrespond pages 5-7)

6. **Respiratory Complexes I/III/IV → proton export.** Supporting snippet: primary respiratory proton pumps and secondary transporters remove excess intracellular protons in acidophilic methanotrophs. Curate at pathway level unless taxon-specific biochemical evidence identifies the responsible complex. (yao2023howmethanotrophsrespond pages 5-7)

7. **NhaA/NhaP antiport → cytoplasmic proton removal.** These systems are repeatedly predicted in acidophile genomes, including *Leptospirillum* and cold-adapted acidophiles. Evidence is primarily comparative-genomic, so mark `uncertain: true` absent knockout, transport, or expression-plus-physiology evidence. (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

8. **Gad/Adi/SpeA decarboxylation → proton consumption.** Supporting snippets identify gadABC, adi, and speA as predicted proton-consuming modules. This is mechanistically plausible and established in broader bacterial acid resistance, but its necessity for obligate acidophily is not demonstrated across taxa. (gonzalezrosales2022integrativegenomicssheds pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

9. **Buffering molecules → stabilized intracellular pH.** Overproduced alkaline amino acids, spermidine, and poly-γ-glutamate are proposed contributors. Composition and direction can vary; avoid collapsing all buffers into one universal node. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalezrosales2022integrativegenomicssheds pages 1-2)

10. **Combined defenses → near-neutral cytoplasmic pH → acidic growth.** Direct evidence in *Methylacidiphilum* sp. RTK17.1 measured intracellular pH 6.55 ± 0.05 across external pH 1.5–3.0. This supports the endpoint but not every upstream mechanism in every lineage. (carere2021growthonformic pages 1-2, carere2021growthonformic pages 3-4)

11. **Weak organic acid influx → cytoplasmic acidification → growth inhibition.** At 1 mM formic acid, intracellular pH fell from 6.52 to 6.05; the reported IC50 was 0.58 mM. Batch growth failed, whereas substrate-limited chemostats supported growth at D = 0.0052 h⁻¹ (doubling time 133 h). This is strong direct but substrate- and assay-specific evidence. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 5-7, carere2021growthonformic pages 1-2)

12. **Ionophore/protonophore treatment → disruption of pH homeostasis.** Nigericin plus valinomycin at 10 μM acidified *Methylacidiphilum* cells, giving perturbational evidence that intact electrochemical gradients are causal. Curate these chemicals as experimental inhibitors, not natural causes of obligate acidophily. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 2-3)

## 5. Recent developments and applications

### Genomic and systems-level developments

Recent work increasingly treats acidophily as a **redundant systems phenotype**, not a single-gene trait. Comparative genomes of low-temperature acidophiles encode kdpABCDE/Kef potassium systems, nhaA, hpn hopanoid genes, gadABC/adi/speA, cfa, and clpXP. However, these are mostly presence/absence predictions from genomes or MAGs; they identify candidate modules rather than proving causal sufficiency. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

The 2024 aSRB review extends the model to anaerobic sulfate reducers, reporting internal pH around 6 while growth occurs below pH 3 and discussing proton exclusion, pumping, consumption, and buffering. Its authors explicitly caution that many mechanisms were inferred from other acidophiles and require confirmation in pure aSRB cultures. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### Biomining and bioleaching

A 2024 review identifies commercial-scale copper-tailings bioleaching in China at Dexing, Zijinshan, and Jinchuan. Reported examples include a 1,000-ton Dexing operation recovering 16.59–30% Cu from tailings above 0.12% Cu, and a 10,000-ton Zijinshan bioheap using *Acidithiobacillus*, *Leptospirillum*, and *Sulfobacillus*. Globally, bioleaching was estimated to account for approximately 1.2% of copper production in 2020. (zhang2024accumulatedcoppertailing pages 5-8, zhang2024accumulatedcoppertailing pages 1-2)

Operating windows span mesophiles at 20–40°C, moderate thermophiles at 40–60°C, and extreme thermophiles above 65°C; typical acidophile systems use pH 1–3. Reported examples include >40% copper recovery by *A. caldus* at 45°C and >97% by *Sulfolobus acidocaldarius* at 70°C. These values are process- and mineral-specific and should not be interpreted as intrinsic trait parameters. (zhang2024accumulatedcoppertailing pages 5-8)

*A. ferrooxidans* oxidizes Fe²⁺, H₂S, elemental sulfur, and H₂ and generates Fe(III), which attacks metal sulfides. A 2024 synthesis reports mobilization of Li, P, V, Cr, Fe, Ni, Cu, Zn, Ga, As, Mo, W, Pb, and U. The same activity can contribute to acid mine drainage, requiring containment and monitoring. (tonietti2024unveilingthebioleaching pages 1-2)

Consortia can outperform isolates: one cited copper study achieved 70% extraction in 35 days with *A. ferrooxidans* plus *A. thiooxidans*, versus 35% with *Leptospirillum ferrooxidans* plus *A. thiooxidans*. A consortium treating electroplating sludge was reported to be 21.1% more efficient than sulfuric-acid chemical leaching. Experts caution that mineralogy prevents generalization from one deposit to another. (cozma2024biorecoveryofmetals pages 10-11)

### Remediation, fermentation, and electrochemical systems

Acidophilic sulfate reducers are being developed for acid-mine-drainage treatment because biogenic sulfide precipitates dissolved metals; recovered metal sulfides may support circular-economy uses. Recent work also reports *Alicyclobacillus tolerans*–*Acidiphilium cryptum* cultures producing schwertmannite for arsenic removal from acidic effluents. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalez2024acidophilicheterotrophsbasic pages 3-4)

More than 80 cultured acidophilic heterotrophs can use organic substrates, creating opportunities for low-contamination acidic fermentation, biopolymers, extremozymes, and metal reduction. *A. cryptum* Lhet2 has been used in microbial fuel cells at pH ≤4, but its reported maximum power density of 12.6 mW m⁻² remains far below neutral-pH systems at 5.61–7.72 W m⁻². This gap illustrates that acid robustness does not automatically imply competitive process productivity. (gonzalez2024acidophilicheterotrophsbasic pages 3-4)

## 6. Claims not ready for TraitMech curation

1. **A universal obligate-acidophile mechanism.** Acidophily evolved repeatedly in Bacteria and Archaea; individual taxa combine different membrane chemistries and transport systems.
2. **Gene presence → obligate phenotype.** kdp, nha, gad, hopanoid, or repair genes are neither demonstrated necessary nor sufficient for METPO:1003006 in most taxa.
3. **Acidic optimum → obligacy.** An optimum ≤3 or ≤5 does not prove inability to grow at pH 7.
4. **Habitat pH → organismal growth boundary.** Recovery from AMD or hot springs is ecological association, not a growth-range assay.
5. **All hopanoids/tetraether lipids as one node.** Hopanoids, saturated bacterial lipids, archaeal ether/tetraether lipids, and AEG lipids are chemically distinct and taxonomically distributed.
6. **Omp40 or Slp as universal.** These are envelope- and lineage-specific.
7. **Donnan potential equals all reversed membrane potential.** The terms overlap in some reviews but should not be treated as universally identical without source-specific electrophysiology.
8. **DNA repair/chaperones directly cause obligate acidophily.** These are plausible damage-control systems; current retrieved evidence is broad or predictive, and *Leptospirillum* protein folding and chaperone roles remain explicitly underinvestigated. (vergara2020evolutionofpredicted pages 16-17)
9. **Formic acid sensitivity as a defining edge.** It is a conditional weak-acid assay result, not part of the trait definition.
10. **Application performance as phenotype evidence.** Metal recovery depends on mineralogy, temperature, oxygen, pulp density, community composition, and reactor design.

## 7. Suggested minimal YAML graph

A conservative first curation should prioritize broadly supported nodes and reserve gene-level branches for taxon-specific extensions:

1. acidic extracellular environment → increases → transmembrane proton gradient;
2. low-proton-permeability membrane → decreases → proton influx;
3. K⁺ uptake → increases → inside-positive membrane potential;
4. inside-positive membrane potential → decreases → proton influx;
5. proton export/antiport → decreases → cytoplasmic proton concentration;
6. proton-consuming reactions/buffering → stabilizes → intracellular pH;
7. stable near-neutral intracellular pH → enables → growth in acidic environment;
8. growth in acid plus no growth at neutral/alkaline pH → realizes → **METPO:1003006**.

Edges 1, 5, and 6 should initially use process-level nodes. Attach Kdp/Kch/Trk, NhaA/NhaP, Gad/Adi, Omp40, and lipid modules only in evidence blocks scoped to the experimentally or genomically studied taxon.

## 8. DOI-first bibliography

- Valdez-Nuñez LF et al. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports*. Published October 2024. https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- Zhang J et al. **Accumulated Copper Tailing Solid Wastes with Specific Compositions Encourage Advances in Microbial Leaching.** *Minerals* 14:1051. Published October 2024. https://doi.org/10.3390/min14101051 (zhang2024accumulatedcoppertailing pages 5-8, zhang2024accumulatedcoppertailing pages 1-2)
- Tonietti L et al. **Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.** *Microorganisms* 12:2407. Published November 2024. https://doi.org/10.3390/microorganisms12122407 (tonietti2024unveilingthebioleaching pages 1-2)
- Cozma P et al. **Bio-Recovery of Metals through Biomining within Circularity-Based Solutions.** *Processes* 12:1793. Published August 2024. https://doi.org/10.3390/pr12091793 (cozma2024biorecoveryofmetals pages 10-11)
- González E et al. **Acidophilic heterotrophs: basic aspects and technological applications.** *Frontiers in Microbiology* 15. Published May 2024. https://doi.org/10.3389/fmicb.2024.1374800 (gonzalez2024acidophilicheterotrophsbasic pages 3-4, gonzalez2024acidophilicheterotrophsbasic pages 2-3)
- Dopson M et al. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology* 14. Published March 2023. https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology* 13. Published January 2023. https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)
- González-Rosales C et al. **Integrative Genomics Sheds Light on Evolutionary Forces Shaping the Acidithiobacillia Class Acidophilic Lifestyle.** *Frontiers in Microbiology* 12. Published February 2022. https://doi.org/10.3389/fmicb.2021.822229 (gonzalezrosales2022integrativegenomicssheds pages 1-2)
- Carere CR et al. **Growth on Formic Acid Is Dependent on Intracellular pH Homeostasis for the Thermoacidophilic Methanotroph Methylacidiphilum sp. RTK17.1.** *Frontiers in Microbiology* 12. Published March 2021. https://doi.org/10.3389/fmicb.2021.651744 (carere2021growthonformic pages 4-5, carere2021growthonformic pages 5-7, carere2021growthonformic pages 1-2, carere2021growthonformic pages 3-4)
- Vergara E et al. **Evolution of Predicted Acid Resistance Mechanisms in the Extremely Acidophilic Leptospirillum Genus.** *Genes* 11:389. Published April 2020. https://doi.org/10.3390/genes11040389 (vergara2020evolutionofpredicted pages 1-3, vergara2020evolutionofpredicted pages 16-17)

References

1. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

2. (vergara2020evolutionofpredicted pages 1-3): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.

3. (gonzalezrosales2022integrativegenomicssheds pages 1-2): Carolina González-Rosales, Eva Vergara, Mark Dopson, Jorge H. Valdés, and David S. Holmes. Integrative genomics sheds light on evolutionary forces shaping the acidithiobacillia class acidophilic lifestyle. Frontiers in Microbiology, Feb 2022. URL: https://doi.org/10.3389/fmicb.2021.822229, doi:10.3389/fmicb.2021.822229. This article has 31 citations and is from a peer-reviewed journal.

4. (carere2021growthonformic pages 3-4): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

5. (carere2021growthonformic pages 4-5): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

6. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 79 citations and is from a peer-reviewed journal.

7. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

8. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 18 citations and is from a peer-reviewed journal.

9. (carere2021growthonformic pages 9-10): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

10. (vergara2020evolutionofpredicted pages 16-17): Eva Vergara, Gonzalo Neira, Carolina González, Diego Cortez, Mark Dopson, and David S. Holmes. Evolution of predicted acid resistance mechanisms in the extremely acidophilic leptospirillum genus. Genes, 11:389, Apr 2020. URL: https://doi.org/10.3390/genes11040389, doi:10.3390/genes11040389. This article has 40 citations.

11. (carere2021growthonformic pages 1-2): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

12. (carere2021growthonformic pages 5-7): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

13. (carere2021growthonformic pages 2-3): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

14. (zhang2024accumulatedcoppertailing pages 5-8): Juan Zhang, Xiaojun Liu, Xinyue Du, Xin Wang, Yifan Zeng, and Shu-kai Fan. Accumulated copper tailing solid wastes with specific compositions encourage advances in microbial leaching. Minerals, 14:1051, Oct 2024. URL: https://doi.org/10.3390/min14101051, doi:10.3390/min14101051. This article has 5 citations.

15. (zhang2024accumulatedcoppertailing pages 1-2): Juan Zhang, Xiaojun Liu, Xinyue Du, Xin Wang, Yifan Zeng, and Shu-kai Fan. Accumulated copper tailing solid wastes with specific compositions encourage advances in microbial leaching. Minerals, 14:1051, Oct 2024. URL: https://doi.org/10.3390/min14101051, doi:10.3390/min14101051. This article has 5 citations.

16. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

17. (cozma2024biorecoveryofmetals pages 10-11): Petronela Cozma, Camelia Bețianu, Raluca-Maria Hlihor, Isabela Maria Simion, and Maria Gavrilescu. Bio-recovery of metals through biomining within circularity-based solutions. Processes, 12:1793, Aug 2024. URL: https://doi.org/10.3390/pr12091793, doi:10.3390/pr12091793. This article has 37 citations.

18. (gonzalez2024acidophilicheterotrophsbasic pages 3-4): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.

19. (gonzalez2024acidophilicheterotrophsbasic pages 2-3): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 10 citations and is from a peer-reviewed journal.