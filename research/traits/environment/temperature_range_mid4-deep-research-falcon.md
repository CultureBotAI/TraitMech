---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:38:26.890711'
end_time: '2026-06-18T03:00:41.808279'
duration_seconds: 1334.92
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid4
  trait_identifier: METPO:1000453
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid4
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 34\u201340 \xB0C, characteristic of warm-mesophilic\
    \ physiology (including many mammalian host-associated bacteria)."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_34_to_40
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 34\u201340 \xB0C range as the\
    \ warm-mesophile (mammalian-host) growth range.)"
  causal_graph_summary: 'temperature_range_mid4_warm_mesophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid4
- **METPO identifier:** METPO:1000453
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 34–40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 34–40 °C range as the warm-mesophile (mammalian-host) growth range.)
- **Existing causal graph summary:** temperature_range_mid4_warm_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid4.yaml`.

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
- **Trait label:** temperature range mid4
- **METPO identifier:** METPO:1000453
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 34–40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 34–40 °C range as the warm-mesophile (mammalian-host) growth range.)
- **Existing causal graph summary:** temperature_range_mid4_warm_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid4.yaml`.

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


# Research report: Microbial trait “temperature range mid4” (METPO:1000453)

## 1) Scope summary (trait concept, definition, boundary cases)

**Trait concept.** METPO:1000453 (“temperature range mid4”) is a *class-level* growth temperature-range phenotype describing microbes whose growth-supporting ambient temperature range spans approximately **34–40 °C**, consistent with **warm-mesophilic physiology** and common **mammalian host–associated** growth conditions (e.g., 37 °C). This trait is a *growth range* (ability to grow across a temperature interval), not strictly an optimum-growth-temperature (Topt) phenotype.

**Distinguishing from nearby traits.** A broader definition of *mesophile* frequently spans from around **~20 °C to ~45 °C**, which is wider than the warm-mesophilic “mid4” window and overlaps both cooler mesophily and thermotolerance boundaries. (ramon2023ageneraloverview pages 1-2)

**Boundary cases and operational thresholds.** In acetic acid bacteria (AAB) used for vinegar production, temperatures above **34 °C** can severely impact growth/fermentation; nevertheless, “thermotolerant” AAB strains can grow at **37 °C** and some up to **42 °C**, which straddles the mid4 window and extends toward thermotolerance. (hua2024regulatorymechanismsof pages 1-3)

## 2) Current mechanistic understanding (key concepts/definitions)

### 2.1 Membrane homeoviscous adaptation (HVA) as a central mechanism
A dominant mechanistic theme for growth across changing temperatures is **homeoviscous adaptation**: maintaining membrane physical properties (commonly described as membrane “fluidity”) by changing lipid composition. A recent 2024 *Nature Communications* study in *E. coli* quantified enzymes and intermediates in fatty-acid/phospholipid pathways and concluded that **temperature is “measured” through fatty-acyl precursor pools**, enabling restoration of optimal membrane fluidity **within a single generation** after temperature shock. (hoogerland2024atemperaturesensitivemetabolic pages 1-2)

Mechanistically, Hoogerland et al. propose a **two-component control system**:
1) a rapid **temperature-sensitive metabolic valve** at branchpoint enzymes **FabI** and **FabB** that allocates flux between saturated vs unsaturated fatty-acid synthesis; and
2) a slower **transcriptional negative feedback loop** (notably involving **FabR** and **FadR**-linked regulation) that counteracts/adjusts the initial metabolic shift. (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 2-3)

The hallmark kinetics includes **transient overshoot** in saturated/unsaturated production after shocks, which accelerates return toward a fluidity-maintaining composition. (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 7-8)

**Figure evidence (time-resolved overshoot).** Hoogerland et al. provide time-course data for cold-shock **37 → 13 °C** and heat-shock **13 → 37 °C**, showing rapid, transient changes in the **acyl-ACP substrate pool** and **phosphatidic acid** composition consistent with overshoot-based homeoviscous adaptation. (hoogerland2024atemperaturesensitivemetabolic media 276b58f7, hoogerland2024atemperaturesensitivemetabolic media f97c365c)

### 2.2 Proteostasis and heat-shock response as determinants near the upper warm-growth limit
At warm-mesophilic upper temperatures, heat stress can destabilize proteins and other macromolecules. In heat-adapted *E. coli*, high temperature is described as causing “**protein unfolding and aggregation**,” as well as “**increased membrane fluidity**” and changes in nucleic-acid processes (DNA supercoiling/RNA stability/transcription/translation). (mcguire2023wholegenomesequencinganalysis pages 1-2)

A canonical bacterial heat-shock control module is **σ32 (RpoH)**, which activates chaperone systems including **DnaK/DnaJ/GrpE** and **GroES/GroEL**. (berdejo2024evolutionarytradeoffbetween pages 1-2)

### 2.3 DNA topology / global regulation (transcription machinery) as a repeated evolutionary target
For thermal adaptation, studies repeatedly observe mutations in **global transcription regulators** rather than single “temperature genes.” In heat-evolved *E. coli*, McGuire & Nano highlight changes in “master regulators such as the RNA polymerase” (e.g., **rpoB**) and “the transcriptional termination factor **Rho**.” (mcguire2023wholegenomesequencinganalysis pages 1-2)

### 2.4 Osmoadaptation / ionic homeostasis as cross-protection for thermotolerance (taxon-specific)
In *Bacillus* lineages, recent experimental evolution implicates the second messenger **c-di-AMP** and its synthesis genes (DACs such as **DisA/CdaA/CdaS**, modulated by **CdaR**) in temperature tolerance via **potassium homeostasis** and osmoadaptation. The authors note that under high osmolarity cells gain increased resistance to high temperature, including an “**elevated upper limit of growth temperature**,” and compatible solutes (e.g., **glycine betaine**, **proline**) act as heat protectants. (hurtadobautista2024thermalplasticityand pages 16-17)

## 3) Recent developments and latest research (prioritizing 2023–2024)

### 3.1 2024: Quantitative metabolic control model for membrane adaptation (E. coli)
Hoogerland et al. (2024) propose that temperature control is implemented through an asymmetric temperature dependence at the fatty-acid branchpoint: FabI vs FabB/FabA competition for shared intermediates creates a **metabolic valve** controlling saturated vs unsaturated output, while transcriptional control (notably via **FabR** and **FadR** links) tunes steady state and dynamics. (hoogerland2024atemperaturesensitivemetabolic pages 2-3, hoogerland2024atemperaturesensitivemetabolic pages 10-11, hoogerland2024atemperaturesensitivemetabolic pages 6-7)

### 3.2 2023: Whole-genome analysis of heat-evolved E. coli emphasizes diverse genetic routes
McGuire & Nano (2023) highlight that enhanced thermotolerance can evolve by many genetic mechanisms; notably, their resequencing clarifies that a heat-evolved strain carried a **groESL-bearing plasmid (pOF39)** maintained by high-temperature selection, and identifies numerous changes including in transcription machinery (RNA polymerase; Rho). (mcguire2023wholegenomesequencinganalysis pages 1-2)

### 3.3 2024: Trade-off between heat-shock resistance and warm-range growth in Salmonella
Berdejo et al. (2024) report that repeated heat shocks selected **dnaJ loss-of-function** in *Salmonella Typhimurium*, producing **>1,000-fold increased survival** after **55 °C/20 min** heat shock, but also **attenuated growth at 37 °C and higher temperatures**, linking stress adaptation to fitness trade-offs within the warm-mesophilic window and above. (berdejo2024evolutionarytradeoffbetween pages 1-2)

### 3.4 2024: Bacillus thermal niche constraints and c-di-AMP/K+ as a candidate mechanistic axis
Hurtado-Bautista et al. (2024) situate mesophilic *Bacillus* as typically thriving between **27–40 °C**, and report convergent evolution signals involving c-di-AMP synthesis genes; they interpret c-di-AMP as “crucial for potassium transport,” supporting a mechanistic hypothesis that ionic/osmotic regulation contributes to thermal tolerance constraints. (hurtadobautista2024thermalplasticityand pages 1-2, hurtadobautista2024thermalplasticityand pages 16-17)

### 3.5 2024: AAB vinegar-production stresses and thermal tolerance above 34°C
Hua et al. (2024) provide a domain-specific synthesis for vinegar AAB: most grow best near **~30 °C** and are “severely affected” above **34 °C**, but thermotolerant strains can grow at **37–42 °C**; exothermic fermentation can push temperatures above **40 °C** and traditional solid-state processes can exceed **45 °C**, motivating thermotolerant strains and engineering strategies. (hua2024regulatorymechanismsof pages 1-3, hua2024regulatorymechanismsof pages 9-11)

## 4) Current applications and real-world implementations

### 4.1 High-temperature bioprocessing: SSF (simultaneous saccharification and fermentation)
A practical driver for pushing mesophilic hosts upward in temperature is integration with enzymes (e.g., cellulases) that work best near ~50 °C.

Pérez-Morales et al. (2024) report **adaptive laboratory evolution (ALE)** to generate a thermotolerant *E. coli* strain **GT48**, evolved to tolerate ~48 °C, which can **grow and ferment glucose at 47 °C**. They demonstrate **SSF** of diluted acid–pretreated corn stover at **47 °C**, **pH 6.3**, **15% (w/w) solids**, and **15 FPU/g** enzyme loading, achieving **59 g/L d-lactic acid** and **71% yield from the glucan fraction**. (perezmorales2024simultaneoussaccharificationand pages 2-4)

This represents a concrete implementation pathway where shifting growth temperature upward (beyond mid4) enables process integration, while illustrating constraints (e.g., viability drop with increments >0.2 °C above 43 °C during chemostat adaptation). (perezmorales2024simultaneoussaccharificationand pages 2-4)

### 4.2 Food fermentation: vinegar production with thermotolerant acetic acid bacteria
Hua et al. (2024) describe vinegar production as a high-stress, high-heat context: acetic acid fermentation is exothermic; temperatures can frequently exceed **40 °C**, and traditional solid-state methods can exceed **45 °C**. They connect thermotolerance to actionable mechanisms: protective extracellular polysaccharides (EPS/PPS) enabling **surface flotation and reduced exposure to heat**, and increased **thermal stability/optimal temperature of ADH** in thermotolerant strains. (hua2024regulatorymechanismsof pages 9-11)

## 5) Expert opinions / analysis (authoritative interpretations)

**Thermal adaptation is multi-constraint.** McGuire & Nano (2023) emphasize that high-temperature stress simultaneously perturbs proteins, membranes, and nucleic acid processes, implying that growth in the upper warm-mesophilic range is inherently multi-factorial. (mcguire2023wholegenomesequencinganalysis pages 1-2)

**Thermal adaptation can create trade-offs inside the warm-mesophilic window.** Berdejo et al. (2024) interpret the dnaJ evolution result as evidence for a “delicate balance” between stress resistance and virulence/fitness, with direct relevance to growth and regulation at 37 °C and above. (berdejo2024evolutionarytradeoffbetween pages 1-2)

**Membrane adaptation can be rapid and modelable.** Hoogerland et al. (2024) explicitly frame their metabolic valve + feedback architecture as potentially “ubiquitous” core features of homeoviscous adaptation, implying that lipid precursor-control motifs may generalize beyond *E. coli* as a mechanistic module supporting stable growth across temperature ranges. (hoogerland2024atemperaturesensitivemetabolic pages 1-2)

## 6) Candidate nodes and candidate causal edges for TraitMech curation

### 6.1 Candidate node inventory (grouped by type)
| Node label | Type | Role in trait | Suggested identifier(s) | Key supporting source(s) |
|---|---|---|---|---|
| Temperature upshift | environmental factor | tests upper warm-growth tolerance | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| Temperature downshift | environmental factor | reveals reciprocal membrane adaptation | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic media 276b58f7) |
| Growth temperature range 34–40 °C | process | focal warm-mesophile phenotype | METPO:1000453 | Hua 2024, DOI:10.1186/s12934-024-02602-y; Ramón 2023, DOI:10.1007/s42770-023-01057-4 (hua2024regulatorymechanismsof pages 1-3, ramon2023ageneraloverview pages 1-2) |
| Upper growth temperature limit | process | boundary of warm-range growth | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088; Hua 2024, DOI:10.1186/s12934-024-02602-y (hurtadobautista2024thermalplasticityand pages 16-17, hua2024regulatorymechanismsof pages 9-11) |
| Membrane fluidity | process | physical property that must be maintained | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (hoogerland2024atemperaturesensitivemetabolic pages 1-2, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| Homeoviscous adaptation | process | compensates temperature-driven membrane changes | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 1-2) |
| Heat shock response | process | protects cells near/above warm-growth ceiling | GO:0009408 | Berdejo 2024, DOI:10.1128/mbio.03105-23; Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (berdejo2024evolutionarytradeoffbetween pages 1-2, hurtadobautista2024thermalplasticityand pages 1-2) |
| Osmoadaptation | process | links ionic/solute balance to thermotolerance | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| Acetic acid fermentation efficiency | process | warm-range industrial performance output | label-only | Hua 2024, DOI:10.1186/s12934-024-02602-y (hua2024regulatorymechanismsof pages 9-11, hua2024regulatorymechanismsof pages 1-3) |
| Temperature shock assay (37→13 °C; 13→37 °C) | assay factor | measures rapid adaptation kinetics | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic media 276b58f7) |
| High-temperature growth assay (37–42 °C) | assay factor | quantifies warm/thermotolerant growth | label-only | Hua 2024, DOI:10.1186/s12934-024-02602-y; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (hua2024regulatorymechanismsof pages 1-3, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| High-osmolarity assay | assay factor | tests osmotic cross-protection to heat | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| fabA | gene | routes flux into UFA branch | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3) |
| fabB | gene | key UFA branchpoint synthase | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3, hoogerland2024atemperaturesensitivemetabolic pages 6-7) |
| fabI | gene | key SFA branchpoint reductase | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3, hoogerland2024atemperaturesensitivemetabolic pages 10-11) |
| fabF | gene | elongates C16:1 toward C18:1 | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 9-10) |
| plsB | gene | loads sn-1 acyl chains into phospholipid synthesis | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| plsC | gene | loads sn-2 acyl chains into phospholipid synthesis | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| fabR | gene | transcriptional feedback on UFA pathway | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 6-7, hoogerland2024atemperaturesensitivemetabolic pages 7-8) |
| fadR | gene | regulates fabA in response to acyl-CoA | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3) |
| rpoH | gene | encodes heat-shock sigma factor σ32 | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2) |
| dnaK | gene | chaperone for protein quality control | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2) |
| dnaJ | gene | co-chaperone affecting heat resistance-growth tradeoff | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2) |
| grpE | gene | co-chaperone in heat protection | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2) |
| groES | gene | chaperonin subunit supporting thermotolerance | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (berdejo2024evolutionarytradeoffbetween pages 1-2, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| groEL | gene | chaperonin subunit supporting thermotolerance | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (berdejo2024evolutionarytradeoffbetween pages 1-2, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| rpoB | gene | recurrent adaptive transcription target in heat | label-only | McGuire 2023, DOI:10.1186/s12864-023-09266-9 (mcguire2023wholegenomesequencinganalysis pages 1-2) |
| rho | gene | recurrent adaptive transcription termination target | label-only | McGuire 2023, DOI:10.1186/s12864-023-09266-9 (mcguire2023wholegenomesequencinganalysis pages 1-2) |
| disA | gene | diadenylate cyclase for c-di-AMP synthesis | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| cdaA | gene | major diadenylate cyclase in Bacillus | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| cdaS | gene | diadenylate cyclase linked to heat tolerance | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| cdaR | gene | modulates CdaA activity | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| adh | gene | thermally stable enzyme supporting AAB productivity | label-only | Hua 2024, DOI:10.1186/s12934-024-02602-y (hua2024regulatorymechanismsof pages 9-11) |
| FabA | protein complex | branchpoint isomerase/dehydratase activity | UniProtKB:P0A6B7 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3) |
| FabB | protein complex | UFA-branch ketoacyl-ACP synthase | UniProtKB:P0A6R3 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 6-7) |
| FabI | protein complex | enoyl-ACP reductase favoring SFA branch | UniProtKB:P0A9P0 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 10-11) |
| FabF | protein complex | elongates unsaturated acyl-ACP species | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 9-10) |
| PlsB | protein complex | acyltransferase using acyl-ACP substrate pools | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| PlsC | protein complex | acyltransferase shaping PA composition | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4) |
| FabR | protein complex | repressor tuning fabB with unsaturated precursor | UniProtKB:P0A9D8 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 6-7, hoogerland2024atemperaturesensitivemetabolic pages 10-11) |
| FadR | protein complex | regulator linking acyl-CoA to fatty acid genes | UniProtKB:P0A6A3 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3) |
| σ32 (RpoH) | protein complex | activates heat-shock regulon | label-only | Berdejo 2024, DOI:10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2) |
| DnaK/DnaJ/GrpE system | protein complex | refolds stress-damaged proteins | GO:0031072 | Berdejo 2024, DOI:10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2) |
| GroES/GroEL chaperonin | protein complex | protects folding at elevated temperature | GO:0005832 | Berdejo 2024, DOI:10.1128/mbio.03105-23; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (berdejo2024evolutionarytradeoffbetween pages 1-2, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| Alcohol dehydrogenase (ADH) | protein complex | thermal stability supports AAB productivity | EC:1.1.1.1 | Hua 2024, DOI:10.1186/s12934-024-02602-y (hua2024regulatorymechanismsof pages 9-11) |
| Saturated fatty acids | metabolite | stiffen membrane at higher temperature | CHEBI:26607 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5; McGuire 2023, DOI:10.1186/s12864-023-09266-9 (hoogerland2024atemperaturesensitivemetabolic pages 1-2, mcguire2023wholegenomesequencinganalysis pages 1-2) |
| Unsaturated fatty acids | metabolite | fluidize membrane at lower temperature | CHEBI:27208 | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 1-2, hoogerland2024atemperaturesensitivemetabolic pages 2-3) |
| C16:0-ACP | metabolite | saturated acyl-ACP indicator of warm adaptation | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 10-11) |
| C18:1-ACP | metabolite | unsaturated acyl-ACP indicator of cold adaptation | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 7-8) |
| C10:1 acyl-ACP pool | metabolite | shared branchpoint substrate pool | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 2-3) |
| C16:1 acyl-ACP | metabolite | intermediate in unsaturated branch | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 6-7, hoogerland2024atemperaturesensitivemetabolic pages 9-10) |
| C18:1-OH ACP | metabolite | reporter of altered branchpoint flux | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 6-7) |
| Acyl-ACP substrate pool | metabolite | immediate readout of temperature response | label-only | Hoogerland 2024, DOI:10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic media 276b58f7) |
| c-di-AMP | metabolite | second messenger coupling K+ homeostasis to heat tolerance | CHEBI:140259 | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17, hurtadobautista2024thermalplasticityand pages 1-2) |
| Potassium ion | metabolite | osmotic counterion aiding thermotolerance | CHEBI:29103 | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| Glycine betaine | metabolite | compatible solute heat protectant | CHEBI:17750 | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| L-proline | metabolite | compatible solute heat protectant | CHEBI:17203 | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |
| Extracellular polysaccharides (EPS/PPS) | metabolite | floating/biofilm protection from heat | CHEBI:18154 | Hua 2024, DOI:10.1186/s12934-024-02602-y (hua2024regulatorymechanismsof pages 9-11) |
| High osmolarity | environmental factor | induces cross-protection to heat | label-only | Hurtado-Bautista 2024, DOI:10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 16-17) |


*Table: This table lists candidate causal-graph nodes for METPO:1000453, grouped by type and mapped to suggested identifiers where possible. It is useful as a curation-ready inventory of environmental factors, assay factors, genes, protein systems, metabolites, and processes implicated in growth across the warm-mesophilic 34–40 °C range.*

### 6.2 Evidence-backed candidate edges (triples with snippets and curation notes)
| Edge (subject–predicate–object) | Entity types (gene/protein/metabolite/process/environment) | Source (first author year) | DOI | URL | Publication date (month/year) | Evidence snippet (verbatim short quote) | Notes/curation confidence | Suggested CURIEs |
|---|---|---|---|---|---|---|---|---|
| temperature downshift (37→13 °C) → decreases FabI-dominated saturated-branch flux → increases unsaturated phospholipid synthesis | environment / enzyme / lipid metabolic process | Hoogerland 2024 | 10.1038/s41467-024-53677-5 | https://doi.org/10.1038/s41467-024-53677-5 | 10/2024 | “Upon cold shock, flux through the saturated branch is immediately reduced via FabI, producing a rapid increase in unsaturated phospholipid production” (hoogerland2024atemperaturesensitivemetabolic pages 10-11) | High; direct mechanistic statement from primary study | FabI: UniProtKB:P0A9P0; unsaturated fatty acid biosynthetic process: GO:0006636; phospholipid biosynthetic process: GO:0008654 |
| FabI/FabB branchpoint metabolic valve → reallocates flux between saturated and unsaturated fatty acid synthesis → homeoviscous adaptation | enzyme / metabolic process / physiological process | Hoogerland 2024 | 10.1038/s41467-024-53677-5 | https://doi.org/10.1038/s41467-024-53677-5 | 10/2024 | “a ‘temperature-sensitive metabolic valve’ at the fatty-acid branchpoint reallocates flux between saturated and unsaturated fatty acid synthesis via the branchpoint enzymes FabI and FabB” (hoogerland2024atemperaturesensitivemetabolic pages 1-2) | High; central proposed edge | FabI: UniProtKB:P0A9P0; FabB: UniProtKB:P0A6R3; homeoviscous adaptation: label-only |
| FabA/FabI/FabB competition for C10:1 pool → shifts flux between saturated and unsaturated fatty acids → changes membrane lipid composition | enzyme / metabolite / lipid composition process | Hoogerland 2024 | 10.1038/s41467-024-53677-5 | https://doi.org/10.1038/s41467-024-53677-5 | 10/2024 | “FabA, FabI and FabB compete for a common C10:1 pool — forming a metabolic valve that shifts flux between saturated and unsaturated fatty acids” (hoogerland2024atemperaturesensitivemetabolic pages 2-3) | High; direct branchpoint mechanism | FabA: UniProtKB:P0A6B7; FabI: UniProtKB:P0A9P0; FabB: UniProtKB:P0A6R3; unsaturated fatty acid: CHEBI:27208; saturated fatty acid: CHEBI:26607 |
| FabR-mediated transcriptional feedback → modulates fabB repression/expression → tunes steady-state membrane composition | transcription factor / gene regulation / membrane composition | Hoogerland 2024 | 10.1038/s41467-024-53677-5 | https://doi.org/10.1038/s41467-024-53677-5 | 10/2024 | “Transcriptional feedback via FabR tunes steady-state membrane composition” and “disrupting FabR-precursor interaction (ΔfabR) abolishes temperature sensitivity of FabB expression” (hoogerland2024atemperaturesensitivemetabolic pages 6-7) | High; direct regulatory evidence | FabR: UniProtKB:P0A9D8; fabB: label-only gene; regulation of transcription, DNA-templated: GO:0006355 |
| FadR → controls FabA expression in response to fatty acyl-CoA → contributes to unsaturated-fatty-acid branch regulation | transcription factor / gene / metabolite / process | Hoogerland 2024 | 10.1038/s41467-024-53677-5 | https://doi.org/10.1038/s41467-024-53677-5 | 10/2024 | “FadR controls FabA expression in response to fatty acyl-CoA” (hoogerland2024atemperaturesensitivemetabolic pages 2-3) | Medium; supportive but not directly tied to 34–40 °C phenotype in this excerpt | FadR: UniProtKB:P0A6A3; FabA: UniProtKB:P0A6B7; acyl-CoA: CHEBI:17984 |
| valve + transcriptional feedback → restores optimal membrane fluidity within a single generation → supports growth after temperature shock | process / membrane property / growth process | Hoogerland 2024 | 10.1038/s41467-024-53677-5 | https://doi.org/10.1038/s41467-024-53677-5 | 10/2024 | “restores optimal membrane fluidity within a single generation after a temperature shock” (hoogerland2024atemperaturesensitivemetabolic pages 1-2) | High; strong phenotype-level link | membrane fluidity: label-only; cellular response to heat/cold: GO:1900034 / GO:0070417 |
| heat stress → protein unfolding and aggregation → impairs mesophile growth unless compensated | environment / protein quality control / growth | McGuire 2023 | 10.1186/s12864-023-09266-9 | https://doi.org/10.1186/s12864-023-09266-9 | 03/2023 | “High temperatures cause a suite of problems for cells, including protein unfolding and aggregation” (mcguire2023wholegenomesequencinganalysis pages 1-2) | High; general mechanistic background applicable to warm-mesophile upper range | response to heat: GO:0009408; protein folding: GO:0006457 |
| heat stress → increased membrane fluidity → requires compensatory adaptation | environment / membrane property / adaptation process | McGuire 2023 | 10.1186/s12864-023-09266-9 | https://doi.org/10.1186/s12864-023-09266-9 | 03/2023 | “High temperatures cause a suite of problems for cells, including … increased membrane fluidity” (mcguire2023wholegenomesequencinganalysis pages 1-2) | High; broad but directly relevant to trait mechanism | membrane fluidity: label-only |
| groESL-bearing plasmid pOF39 → high GroESL expression under high-temperature selection → enhanced thermotolerance | plasmid / chaperonin complex / growth at high temperature | McGuire 2023 | 10.1186/s12864-023-09266-9 | https://doi.org/10.1186/s12864-023-09266-9 | 03/2023 | “BM28 inexplicitly carries the groESL bearing plasmid pOF39 that was maintained simply by high-temperature selection pressure” (mcguire2023wholegenomesequencinganalysis pages 1-2) | Medium; strain-specific evolutionary mechanism | GroEL: UniProtKB:P0A6F5; GroES: UniProtKB:P0A6F9; chaperonin complex: GO:0005832; plasmid pOF39: label-only |
| mutations in rpoB or rho → adaptive transcriptional reprogramming → higher-temperature growth in E. coli | gene / transcription machinery / adaptation process | McGuire 2023 | 10.1186/s12864-023-09266-9 | https://doi.org/10.1186/s12864-023-09266-9 | 03/2023 | “changes in master regulators such as the RNA polymerase and the transcriptional termination factor Rho” and recurrent mutations in “rpoB … or rho” (mcguire2023wholegenomesequencinganalysis pages 1-2) | Medium; strong for heat adaptation, but not sufficient alone to define warm-mesophile trait | rpoB: UniProtKB:P0A8T7; rho: UniProtKB:P0AG30; transcription termination factor activity: GO:0003714 |
| σ32/RpoH regulon → induces DnaK/DnaJ/GrpE and GroES/GroEL systems → protects against heat stress | sigma factor / chaperone systems / heat response | Berdejo 2024 | 10.1128/mbio.03105-23 | https://doi.org/10.1128/mbio.03105-23 | 03/2024 | “The alternative sigma factor σ32 (RpoH) drives protective heat shock proteins including the DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems” (berdejo2024evolutionarytradeoffbetween pages 1-2) | High; canonical heat-response edge in warm-mesophilic pathogen | RpoH: UniProtKB:P0ACQ0; DnaK: UniProtKB:P0A6Y8; DnaJ: UniProtKB:P08622; GrpE: UniProtKB:P09372; GroEL: UniProtKB:P0A6F5; GroES: UniProtKB:P0A6F9; response to heat: GO:0009408 |
| dnaJ loss-of-function → >1,000-fold increased survival after 55 °C/20 min heat shock → attenuated growth at 37 °C and higher temperatures | gene / co-chaperone / survival / growth | Berdejo 2024 | 10.1128/mbio.03105-23 | https://doi.org/10.1128/mbio.03105-23 | 03/2024 | “loss-of-function mutations in dnaJ … produced >1,000-fold increased survival after 55°C/20 min heat shocks but also ‘led to attenuated growth at 37°C and higher temperatures’” (berdejo2024evolutionarytradeoffbetween pages 1-2) | High; direct trade-off, but reflects heat-shock resistance more than routine warm growth | dnaJ: UniProtKB:P08622; protein folding chaperone binding: GO:0051087 |
| c-di-AMP synthesis genes (DisA/CdaA/CdaS; CdaR-modulated) → regulate potassium transport/osmotic balance → contribute to thermotolerance and elevated upper growth-temperature limit | gene / second messenger / ion homeostasis / growth range | Hurtado-Bautista 2024 | 10.3390/biology13121088 | https://doi.org/10.3390/biology13121088 | 12/2024 | “c-di-AMP is essential in B. subtilis and regulates potassium transport and osmotic balance” and high-osmolarity thermotolerance includes “an elevated upper limit of growth temperature” (hurtadobautista2024thermalplasticityand pages 16-17) | Medium; promising, but Bacillus-specific and indirect for general warm-mesophile trait | c-di-AMP: CHEBI:140259; potassium ion transport: GO:0006813; DisA/CdaA/CdaS/CdaR: label-only |
| high osmolarity / potassium homeostasis → increased resistance to high temperature → improved survival at lethal temperatures | environment / ion homeostasis / survival | Hurtado-Bautista 2024 | 10.3390/biology13121088 | https://doi.org/10.3390/biology13121088 | 12/2024 | “When cells face high osmolarity they acquire increased resistance to high temperature” and this includes “improved survival at otherwise lethal temperatures” (hurtadobautista2024thermalplasticityand pages 16-17) | Medium; physiological but not trait-defining alone | osmotic stress: GO:0006970; potassium ion: CHEBI:29103 |
| glycine betaine and proline → act as heat protectants → support Bacillus heat tolerance | metabolite / compatible solute / stress protection | Hurtado-Bautista 2024 | 10.3390/biology13121088 | https://doi.org/10.3390/biology13121088 | 12/2024 | “Compatible solutes (glycine–betaine, proline) are noted as heat protectants for B. subtilis” (hurtadobautista2024thermalplasticityand pages 16-17) | Medium; taxon-specific but mechanistically plausible | glycine betaine: CHEBI:17750; L-proline: CHEBI:17203 |
| temperature >34 °C → significantly reduces AAB activity → lowers acetic acid synthesis efficiency | environment / microbial activity / fermentation process | Hua 2024 | 10.1186/s12934-024-02602-y | https://doi.org/10.1186/s12934-024-02602-y | 11/2024 | “the optimal growth temperature for most AAB is below 34 °C” and “High temperatures can significantly reduce the activity of AAB, thus reducing the efficiency of acetic acid synthesis” (hua2024regulatorymechanismsof pages 9-11) | High; directly supports upper-bound boundary case near trait range | acetic acid biosynthetic/production process: label-only; acetic acid: CHEBI:15366 |
| thermotolerant AAB strains → can grow at 37–42 °C → extend growth into warm-mesophile/thermotolerant boundary | organismal phenotype / growth temperature range | Hua 2024 | 10.1186/s12934-024-02602-y | https://doi.org/10.1186/s12934-024-02602-y | 11/2024 | “thermotolerant strains can grow at 37 °C and some up to 42 °C” (hua2024regulatorymechanismsof pages 1-3) | High; directly relevant to trait scope and boundary cases | growth temperature phenotype: label-only |
| extracellular polysaccharides (PPS/EPS) → enable floating away from heat source → reduce thermal damage | polymer / biofilm-associated process / thermal protection | Hua 2024 | 10.1186/s12934-024-02602-y | https://doi.org/10.1186/s12934-024-02602-y | 11/2024 | “These polysaccharides enable the strain to float ... thereby minimizing its exposure to the heat source and reducing thermal damage to the strain” (hua2024regulatorymechanismsof pages 9-11) | Medium; niche-specific implementation in vinegar fermentation | extracellular polymeric substance: GO:0045226; polysaccharide: CHEBI:18154 |
| increased ADH thermal stability → contributes to thermotolerance → sustains acetic acid production at elevated temperature | enzyme / catalytic stability / fermentation phenotype | Hua 2024 | 10.1186/s12934-024-02602-y | https://doi.org/10.1186/s12934-024-02602-y | 11/2024 | “the ADH of thermotolerant strains had higher optimal temperatures and superior thermal stability” (hua2024regulatorymechanismsof pages 9-11) | Medium; enzyme-specific, likely taxon-specific | alcohol dehydrogenase: EC:1.1.1.1; catalytic activity: GO:0003824 |


*Table: This table compiles curation-ready candidate causal edges for METPO:1000453, emphasizing recent mechanistic evidence on membrane homeoviscous adaptation, chaperone-mediated heat response, osmoadaptation, and warm-range growth constraints. It is useful as a starting point for selecting high-confidence nodes and edges for TraitMech YAML curation.*

## 7) Curation warnings (do-not-curate-yet / uncertain claims)

1) **Avoid over-generalizing heat-adaptation results >40–45 °C into “mid4” causal edges** without explicit evidence that the same mechanisms determine routine growth across 34–40 °C. Many cited experiments probe 42 °C+ adaptation (e.g., *E. coli* heat evolution; SSF strains at 47 °C). These are valuable for identifying constraints and modules, but may represent **thermotolerance** rather than warm-mesophily per se. (mcguire2023wholegenomesequencinganalysis pages 1-2, perezmorales2024simultaneoussaccharificationand pages 2-4)

2) **Taxon specificity:** c-di-AMP/K+ osmoadaptation evidence is strong in *Bacillus* but may not generalize to Gram-negatives lacking the same c-di-AMP network; curate as **Bacillus-/Firmicutes-biased** unless broader evidence is added. (hurtadobautista2024thermalplasticityand pages 16-17)

3) **Assay dependence:** rapid temperature-shock responses (e.g., 37→13 °C) reveal regulatory architecture but are not identical to defining a growth-supporting warm range (34–40 °C). Curate “temperature shock” as an assay factor distinct from “steady-state growth range.” (hoogerland2024atemperaturesensitivemetabolic media 276b58f7, hoogerland2024atemperaturesensitivemetabolic media f97c365c)

4) **Label-only grounding gaps:** specific acyl-ACP chemical entities (e.g., C16:0-ACP, C18:1-ACP) and many AAB-specific genetic factors were not fully grounded to stable identifiers in the extracted evidence and should remain **label-only nodes** pending further targeted sourcing (e.g., UniProt entries for specific strains). (hua2024regulatorymechanismsof pages 9-11, hoogerland2024atemperaturesensitivemetabolic pages 3-4)

## 8) DOI-first bibliography (with URLs and publication dates)

1) Hoogerland L, van den Berg SPH, Suo Y, et al. **A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in *Escherichia coli*.** *Nature Communications.* **Oct 2024**. DOI: **10.1038/s41467-024-53677-5**. URL: https://doi.org/10.1038/s41467-024-53677-5 (hoogerland2024atemperaturesensitivemetabolic pages 1-2)

2) McGuire BE, Nano FE. **Whole-genome sequencing analysis of two heat-evolved *Escherichia coli* strains.** *BMC Genomics.* **Mar 2023**. DOI: **10.1186/s12864-023-09266-9**. URL: https://doi.org/10.1186/s12864-023-09266-9 (mcguire2023wholegenomesequencinganalysis pages 1-2)

3) Berdejo D, Mortier J, Cambré A, et al. **Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in *Salmonella* Typhimurium.** *mBio.* **Mar 2024**. DOI: **10.1128/mbio.03105-23**. URL: https://doi.org/10.1128/mbio.03105-23 (berdejo2024evolutionarytradeoffbetween pages 1-2)

4) Hurtado-Bautista E, Islas-Robles A, Moreno-Hagelsieb G, Olmedo-Alvarez G. **Thermal Plasticity and Evolutionary Constraints in *Bacillus*: Implications for Climate Change Adaptation.** *Biology.* **Dec 2024**. DOI: **10.3390/biology13121088**. URL: https://doi.org/10.3390/biology13121088 (hurtadobautista2024thermalplasticityand pages 1-2)

5) Hua S, Wang Y, Wang L, et al. **Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production.** *Microbial Cell Factories.* **Nov 2024**. DOI: **10.1186/s12934-024-02602-y**. URL: https://doi.org/10.1186/s12934-024-02602-y (hua2024regulatorymechanismsof pages 1-3)

6) Pérez-Morales G, Caspeta L, Merino E, et al. **Simultaneous saccharification and fermentation for d-lactic acid production using a metabolically engineered *Escherichia coli* adapted to high temperature.** *Biotechnology for Biofuels and Bioproducts.* **Nov 2024**. DOI: **10.1186/s13068-024-02579-1**. URL: https://doi.org/10.1186/s13068-024-02579-1 (perezmorales2024simultaneoussaccharificationand pages 2-4)

7) Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology.* **Jul 2023**. DOI: **10.1007/s42770-023-01057-4**. URL: https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (hua2024regulatorymechanismsof pages 1-3): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

3. (hoogerland2024atemperaturesensitivemetabolic pages 1-2): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

4. (hoogerland2024atemperaturesensitivemetabolic pages 2-3): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

5. (hoogerland2024atemperaturesensitivemetabolic pages 7-8): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

6. (hoogerland2024atemperaturesensitivemetabolic media 276b58f7): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

7. (hoogerland2024atemperaturesensitivemetabolic media f97c365c): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

8. (mcguire2023wholegenomesequencinganalysis pages 1-2): Bailey E. McGuire and Francis E. Nano. Whole-genome sequencing analysis of two heat-evolved escherichia coli strains. BMC Genomics, Mar 2023. URL: https://doi.org/10.1186/s12864-023-09266-9, doi:10.1186/s12864-023-09266-9. This article has 9 citations and is from a peer-reviewed journal.

9. (berdejo2024evolutionarytradeoffbetween pages 1-2): Daniel Berdejo, Julien Mortier, Alexander Cambré, Malgorzata Sobota, Ronald Van Eyken, Tom Dongmin Kim, Kristof Vanoirbeek, Diego García Gonzalo, Rafael Pagán, Médéric Diard, and Abram Aertsen. Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in <i>salmonella</i> typhimurium. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03105-23, doi:10.1128/mbio.03105-23. This article has 9 citations and is from a domain leading peer-reviewed journal.

10. (hurtadobautista2024thermalplasticityand pages 16-17): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 5 citations.

11. (hoogerland2024atemperaturesensitivemetabolic pages 10-11): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

12. (hoogerland2024atemperaturesensitivemetabolic pages 6-7): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

13. (hurtadobautista2024thermalplasticityand pages 1-2): Enrique Hurtado-Bautista, Africa Islas-Robles, Gabriel Moreno-Hagelsieb, and Gabriela Olmedo-Alvarez. Thermal plasticity and evolutionary constraints in bacillus: implications for climate change adaptation. Biology, 13:1088, Dec 2024. URL: https://doi.org/10.3390/biology13121088, doi:10.3390/biology13121088. This article has 5 citations.

14. (hua2024regulatorymechanismsof pages 9-11): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

15. (perezmorales2024simultaneoussaccharificationand pages 2-4): Gilberto Pérez-Morales, Luis Caspeta, Enrique Merino, Miguel A. Cevallos, Guillermo Gosset, and Alfredo Martinez. Simultaneous saccharification and fermentation for d-lactic acid production using a metabolically engineered escherichia coli adapted to high temperature. Biotechnology for Biofuels and Bioproducts, Nov 2024. URL: https://doi.org/10.1186/s13068-024-02579-1, doi:10.1186/s13068-024-02579-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (hoogerland2024atemperaturesensitivemetabolic pages 3-4): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

17. (hoogerland2024atemperaturesensitivemetabolic pages 9-10): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.