---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:31:05.314451'
end_time: '2026-08-04T03:38:06.833184'
duration_seconds: 421.52
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta high
  trait_identifier: METPO:1000487
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature delta phenotype with a growth-supporting temperature\
    \ breadth above approximately 30 \xB0C, characteristic of extreme-eurythermal\
    \ physiology."
  parent_traits: METPO:1000303
  synonyms: Td_>30
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity
    as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001:
    resistant to irreversible inactivation at high temperatures (Thermostable-protein
    review supports robust thermostability as the basis of extending tolerance beyond
    standard mesophile ranges.)'
  causal_graph_summary: 'temperature_delta_high_eurythermal: 15 nodes, 9 edges'
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
- **Trait label:** temperature delta high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000487
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth above approximately 30 °C, characteristic of extreme-eurythermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_>30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports robust thermostability as the basis of extending tolerance beyond standard mesophile ranges.)
- **Existing causal graph summary:** temperature_delta_high_eurythermal: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_high.yaml`.

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
- **Trait label:** temperature delta high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000487
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature delta phenotype with a growth-supporting temperature breadth above approximately 30 °C, characteristic of extreme-eurythermal physiology.
- **Parent traits:** METPO:1000303
- **Synonyms:** Td_>30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports very broad homoviscous remodeling capacity as the basis of extreme-eurythermal physiology.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports robust thermostability as the basis of extending tolerance beyond standard mesophile ranges.)
- **Existing causal graph summary:** temperature_delta_high_eurythermal: 15 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta_high.yaml`.

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


# Curation report: microbial “temperature delta high”

## Executive assessment

**Trait:** “temperature delta high”  
**Identifier:** `METPO:1000487`  
**Parent:** `METPO:1000303`  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Operational definition:** a microbial phenotype in which reproducible growth is supported across a temperature interval, \(T_{max}-T_{min}\), greater than approximately 30°C.

The strongest exemplar recovered is *Exiguobacterium chiriqhucha* RW2, which grew from **4–50°C**, a 46°C breadth and the broadest reported range among the examined *Exiguobacterium* isolates. Its membrane phospholipid composition was measured at 4, 18, 30, and 50°C; iso-C17:1Δ5 declined from **17.0 ± 0.5 mol% at 4°C to 1.1 ± 0.3 mol% at 50°C**, a reduction exceeding 93%. This directly anchors the phenotype and strongly associates temperature-dependent membrane remodeling with it, although it does not prove that the lipid change is sufficient or necessary for the full breadth. (white2019thecompletegenome pages 17-18, white2019thecompletegenome pages 10-11, white2019thecompletegenome pages 7-9)

The best-supported mechanistic architecture is therefore **modular rather than a single pathway**:

1. low-temperature membrane sensing and homoviscous lipid remodeling;
2. RNA remodeling and maintenance of translation at the cold end;
3. chaperone/protease-mediated proteostasis and protein thermostability at the warm end;
4. possibly compatible-solute and antioxidant systems that protect membranes and macromolecules.

Only the first three have evidence strong enough to contribute selected graph edges, and even these differ substantially in evidential strength. Recent 2023 literature consolidates bacterial temperature-response mechanisms, but the search found little 2023–2024 work that directly perturbs a mechanism and demonstrates a **greater-than-30°C growth breadth**. Most recent studies address one thermal endpoint or acute survival rather than eurythermal growth. (moon2023temperaturemattersbacterial pages 7-9)

## 1. Trait scope and boundaries

### Included phenotype

A positive annotation should require:

- measured microbial growth—not merely viability—at multiple temperatures;
- documented lower and upper growth limits, or sufficient tested points to establish a breadth above approximately 30°C;
- comparable medium, pH, salinity, oxygenation, inoculum, and incubation criteria across temperatures;
- preferably serial propagation or quantitative growth curves near both endpoints.

RW2 is a strong positive example because growth was reported over 4–50°C and lipid analyses used cultures grown at 4, 18, 30, and 50°C. The strain also tolerates pH 5–11 and varying salinity, emphasizing that assay covariates must be represented separately rather than folded into the temperature trait. (white2019thecompletegenome pages 17-18, white2019thecompletegenome pages 7-9, white2019thecompletegenome pages 3-4)

### Excluded or adjacent phenotypes

- **Thermophily/hyperthermophily:** describes a high optimum or high growth range, not necessarily a range wider than 30°C. Hyperthermophilic enzymes can remain active and resist irreversible inactivation at high temperature, but that does not establish low-temperature growth.
- **Psychrophily/psychrotolerance:** establishes low-temperature growth, not a high upper limit.
- **Heat-shock or cold-shock survival:** survival after an acute exposure is not equivalent to sustained growth.
- **Thermotolerance of spores or resting states:** should not be transferred automatically to vegetative growth.
- **Broad enzyme activity range:** an isolated enzyme is not an organism-level growth phenotype.
- **Temperature optimum:** one optimum value cannot determine \(T_{max}-T_{min}\).

For example, recombinant CspL substantially improves growth at elevated temperature, but the tested spans do not establish a >30°C breadth. It is evidence for a component mechanism, not direct evidence of `METPO:1000487`. (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2)

## 2. Candidate nodes and ontology grounding

Identifiers below are included only where grounding is sufficiently clear. Gene symbols, strain-specific lipids, and complexes should remain label-only until reconciled against the exact TraitMech ontology import and taxon-specific database records.

### Trait, taxa, and environmental/experimental nodes

- `METPO:1000487` — temperature delta high.
- `METPO:1000303` — supplied parent trait.
- *Exiguobacterium chiriqhucha* RW2 — exemplar taxon/strain; **label-only pending NCBITaxon verification**.
- *Bacillus subtilis* — DesK/DesR/des model organism; use a verified NCBITaxon CURIE during implementation.
- *Bacillus coagulans* 2-6 — CspL source strain; label-only pending strain-level verification.
- low temperature; high temperature; temperature downshift; heat shock; cold shock — environmental or experimental nodes; map to ENVO or assay ontology terms only after exact term verification.
- growth-supporting temperature minimum, maximum, and breadth — assay-derived quantities; preserve the temperatures, medium, atmosphere, duration, and growth criterion as evidence metadata.

### Genes, proteins, and complexes

- **DesK**, membrane histidine kinase/thermosensor.
- **DesR**, response regulator.
- **des**, Δ5 fatty-acid desaturase gene; corresponding desaturase enzyme.
- **CspL**, RNA chaperone from *B. coagulans*.
- **CspA**, **CsdA**, and trigger factor — cold-response RNA/protein-folding candidates.
- **DnaK–DnaJ–GrpE** chaperone system; **GroEL/GroES**, **HtpG** — proteostasis candidates.
- **FtsH**, **Lon**, **ClpXP**, and **HslVU** — heat-shock proteases; useful candidate nodes, but no recovered evidence directly ties them to >30°C breadth.
- **opu/proU** compatible-solute transport systems — predicted in RW2, not mechanistically validated for thermal breadth.
- C30 carotenoid-biosynthesis enzymes — predicted in RW2; antioxidant relevance is plausible but not directly linked to the trait.

Useful generic GO grounding includes **GO:0006457 protein folding**, **GO:0009408 response to heat**, **GO:0009409 response to cold**, **GO:0006950 response to stress**, and **GO:0006629 lipid metabolic process**. Exact molecular-function terms for each taxon-specific protein should be assigned from its curated database record rather than inferred from a gene name.

### Chemicals and molecular-state nodes

- unsaturated fatty acid — **CHEBI:27208**.
- saturated fatty acid — **CHEBI:26607**.
- cis double bond in membrane acyl chain — label/process state.
- anteiso-branched-chain fatty acid and branched monoenoic PLFA — label-only unless the precise molecule is known.
- iso-C17:1Δ5 — label-only; avoid collapsing it into a generic fatty acid when quantitative RW2 evidence is attached.
- glycine betaine — **CHEBI:17750**.
- choline — **CHEBI:15354**.
- trehalose — **CHEBI:27082**.
- reactive oxygen species — **CHEBI:26523**.
- ATP — **CHEBI:15422**.

### Processes, functions, and localizations

- homoviscous adaptation;
- membrane-fluidity sensing;
- two-component phosphorelay;
- fatty-acid desaturation;
- membrane lipid remodeling;
- RNA binding/RNA chaperone activity;
- protein folding, refolding, anti-aggregation, and proteolysis;
- compatible-solute uptake/biosynthesis;
- oxidative-stress protection;
- cytoplasmic membrane, cytoplasm, and ribosome/translation machinery.

## 3. Evidence-backed candidate edges

The following table is the recommended starting point for YAML curation. “Direct physiology” means the phenotype or molecular state was measured, but not necessarily genetically perturbed. “Predicted” means genome annotation or cross-source inference.

| subject | predicate | object | evidence class | taxon and conditions | DOI with publication date | short supporting snippet | curation decision/uncertainty |
|---|---|---|---|---|---|---|---|
| low temperature | decreases | membrane fluidity | review | Bacteria; cold shift generally | 10.1146/annurev-micro-091313-103612 (2014-09) | "growth temperature decreases... proportionally more unsaturated fatty acids... This process, termed homoviscous adaptation" (mendoza2014temperaturesensingby pages 2-4) | Curate as broad background mechanism only; not specific to breadth >30°C. |
| reduced membrane fluidity | activates | DesK autophosphorylation | review with mechanistic detail | *Bacillus subtilis*; cold shock / low-fluidity membrane states | 10.1146/annurev-micro-091313-103612 (2014-09) | "Upon cold shock or reduced membrane fluidity, DesKC autophosphorylates at His-188" (mendoza2014temperaturesensingby pages 5-6) | Curate with medium confidence; strong mechanistic review, but not a primary perturbation paper here. |
| DesK~P | phosphorylates | DesR | review with mechanistic detail | *B. subtilis* DesK/DesR system | 10.1146/annurev-micro-091313-103612 (2014-09) | "transferring the phosphoryl group to the response regulator DesR at Asp-54" (mendoza2014temperaturesensingby pages 5-6) | Curate with medium confidence; pathway step is explicit. |
| DesR~P | activates transcription of | des (Δ5-desaturase gene) | review with mechanistic detail | *B. subtilis* | 10.1146/annurev-micro-091313-103612 (2014-09) | "Phosphorylated DesR-P acts as a transcriptional activator of the des gene" (mendoza2014temperaturesensingby pages 5-6) | Curate with medium confidence. |
| des (Δ5-desaturase) | increases synthesis of | unsaturated fatty acids | review with mechanistic detail | *B. subtilis*, low temperature 20–23°C | 10.1146/annurev-micro-091313-103612 (2014-09) | "encodes a Δ5-desaturase catalyzing introduction of cis double bonds in saturated fatty acids to increase unsaturated fatty acid (UFA) content" (mendoza2014temperaturesensingby pages 5-6) | Curate with medium confidence; direct enzymatic role is clear. |
| unsaturated fatty acid / branched monoenoic lipid remodeling | maintains | membrane fluidity | direct physiology + review | *Exiguobacterium chiriqhucha* RW2; PLFA at 4, 18, 30, 50°C; plus general bacterial model | 10.3389/fmicb.2018.03189 (2019-01); 10.1146/annurev-micro-091313-103612 (2014-09) | "unsaturated fatty acids increase at low temperature (4°C)... and decrease dramatically at high temperature"; "93% reduction in branched monoenoic PLFAs between 4–50°C" (white2019thecompletegenome pages 17-18, white2019thecompletegenome pages 10-11) | Curate as physiology-supported association; explicit fluidity maintenance is composite across sources. |
| maintained membrane fluidity | supports | broad thermal growth | correlative/composite | General bacteria; exemplar RW2 4–50°C | 10.1146/annurev-micro-091313-103612 (2014-09); 10.3389/fmicb.2018.03189 (2019-01) | "optimizes the performance of a large array of cellular physiological processes at the new temperature"; RW2 has "the most extensive growth range for temperature (4–50°C)" (mendoza2014temperaturesensingby pages 2-4, white2019thecompletegenome pages 1-2) | Uncertain composite edge; do not overstate as single direct mechanism for METPO:1000487. |
| CspL RNA binding | promotes | high-temperature growth | direct perturbation | CspL from *Bacillus coagulans* expressed in *E. coli*, *Pseudomonas putida*, *S. cerevisiae*; up to 45°C | 10.1038/s41421-021-00246-5 (2021-03) | "E. coli showed 2.4-fold biomass increase at 45°C"; "P. putida... 1.4-fold biomass increase"; CspL is "an RNA chaperone" (zhou2021acoldshock pages 1-2, zhou2021acoldshock pages 5-6) | Curate for high-temperature growth support, not for broad thermal breadth per se. |
| nucleotide-binding-dead CspL | abolishes | CspL high-temperature growth benefit | direct perturbation | Heterologous expression at 45°C | 10.1038/s41421-021-00246-5 (2021-03) | "mutation of 11 nucleotide-binding domain amino acids abolished growth promotion at 45°C" (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2) | Strong negative-control evidence; curate as mechanism-validation edge. |
| DnaK/DnaJ/GrpE heat-shock cluster | supports | high-end growth / thermotolerance | predicted + genome annotation | *E. chiriqhucha* RW2; >45°C high-end growth noted | 10.3389/fmicb.2018.03189 (2019-01) | "Genomic analysis reveals a complete heat shock gene cluster (dnaJ, dnaK, GrpE) supporting thermotolerance above 45°C" (white2019thecompletegenome pages 10-11) | Predicted only in RW2 paper; curate cautiously or keep as candidate node/edge pending perturbation data. |
| compatible-solute uptake/biosynthesis systems (opu, proU, choline/betaine) | may support | broad thermal breadth | predicted | *E. chiriqhucha* RW2 genome | 10.3389/fmicb.2018.03189 (2019-01) | "genome predicts pathways for... choline and betaine uptake/biosynthesis (e.g., opu and proU)" (white2019thecompletegenome pages 1-2) | Too indirect for TraitMech edge without direct temperature-breadth experiment; candidate node only. |
| thermostable proteins / enzymes | enable | high-temperature activity and resistance to irreversible inactivation | review | Hyperthermophiles, proteins/enzymes | 10.1128/mmbr.65.1.1-43.2001 (2001-03) | "typically thermostable (i.e., resistant to irreversible inactivation at high temperatures) and are optimally active at high temperatures" | Curate only as high-temperature function mechanism; does not by itself imply broad growth range or cold-end competence. |
| *Exiguobacterium chiriqhucha* RW2 | exhibits | growth at 4–50°C | direct physiology | Growth assays on M-agar/M-medium; broadest reported for genus | 10.3389/fmicb.2018.03189 (2019-01) | "Strain RW2 has the most extensive growth range for temperature (4–50°C)" (white2019thecompletegenome pages 1-2, white2019thecompletegenome pages 7-9) | Strong anchor edge for trait membership; preferred phenotype-support statement for METPO:1000487 exemplars. |


*Table: This table summarizes compact, curation-ready candidate causal edges for the microbial trait METPO:1000487, separating direct perturbation evidence from physiological associations, predictions, and review-based mechanisms. It is useful for deciding which edges are ready for TraitMech curation and which should remain provisional.*

### Recommended minimal graph

The most defensible initial graph is:

1. `low temperature -> decreases -> membrane fluidity`;
2. `reduced membrane fluidity -> activates -> DesK autophosphorylation`;
3. `DesK~P -> phosphorylates -> DesR`;
4. `DesR~P -> activates_transcription_of -> des`;
5. `Δ5-desaturase -> increases -> unsaturated fatty-acid synthesis`;
6. `unsaturated/branched monoenoic lipid remodeling -> contributes_to -> maintenance of membrane fluidity`;
7. `CspL RNA binding -> promotes -> high-temperature microbial growth`;
8. `nucleotide-binding-defective CspL -> abolishes -> CspL growth benefit`;
9. `E. chiriqhucha RW2 -> exhibits -> METPO:1000487`.

Edges 1–6 describe a taxon-tested cold-end module. In *B. subtilis*, reduced membrane fluidity activates DesK, which autophosphorylates at His-188 and transfers phosphate to DesR Asp-54; DesR-P activates `des`, whose Δ5-desaturase introduces cis double bonds. Importantly, altered membrane composition activated the system at a constant 37°C, supporting fluidity—not temperature itself—as the proximal signal. (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 2-4)

RW2 supplies organism-level consistency for the same general model: low-temperature cultures contained more branched monoenoic lipids, while iso-C17:1Δ5 declined by more than 93% from 4 to 50°C. However, the particular RW2 regulator and enzyme responsible were not functionally established, so the *B. subtilis* DesK/DesR/des chain must not be asserted as an RW2-specific pathway. (white2019thecompletegenome pages 17-18, white2019thecompletegenome pages 10-11)

CspL supplies unusually strong perturbational evidence for a warm-end RNA-homeostasis module. Heterologous expression produced a **2.4-fold biomass increase in *E. coli* at 45°C**, approximately **1.4-fold in *Pseudomonas putida*** under elevated temperature, and **2.6–2.7-fold in *Saccharomyces cerevisiae* at 36°C**. Mutation of 11 nucleotide-binding-domain residues abolished the 45°C benefit, establishing that RNA binding is mechanistically required. At 45°C, CspL expression affected 1,160 genes—about 27% of the *E. coli* genome—and induced several chaperone and membrane-associated genes. (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2)

## 4. Interpretation of recent research

### 2023 synthesis

Moon et al. reviewed bacterial responses to temperature change and integrated membrane remodeling, RNA chaperones, helicases, heat-shock proteins, and membrane-stabilizing small HSPs. Examples include increased cis-vaccenic acid with decreased palmitic acid in cold-grown *E. coli*, DesK/DesR-dependent Δ5 desaturation after a 37→20°C shift in *B. subtilis*, and approximately 40-fold induction of trigger factor under low-temperature conditions. The review also notes that chaperone overexpression can become detrimental around 4°C, demonstrating that more stress machinery is not invariably beneficial and that thermal breadth likely requires regulated allocation rather than constitutive maximal expression. (moon2023temperaturemattersbacterial pages 7-9)

Comparative proteomics found *Shewanella frigidimarina* able to acclimatize across **4–30°C**, with chaperones interacting with transmembrane proteins, elongation factors, and oxidative-protection proteins. This 26°C interval falls below the proposed >30°C threshold and the results are predominantly proteomic associations, so this organism should not be used as a positive trait anchor without additional endpoint data. (garciadescalzo2022comparativeproteomicanalysis pages 1-2)

### 2024 context

The 2024 literature located in the search emphasizes extremophile membrane adaptation and industrial robustness, but did not provide a direct genetic perturbation that expands an organism’s confirmed growth interval beyond 30°C. Thus, recent work strengthens the **conceptual modules**—homeoviscous adaptation, osmolyte-mediated membrane protection, and engineered stress-response systems—more than it validates a complete TraitMech graph for this specific phenotype. This is an important negative result: high-temperature growth improvements, acute thermotolerance, or membrane-lipid changes at two temperatures should not be relabeled as extreme eurythermy without both endpoints.

## 5. Applications and real-world relevance

- **Industrial fermentation:** thermal robustness can lower cooling demand, reduce contamination risk, and support high-temperature bioconversion. CspL is a concrete engineering candidate because it improved elevated-temperature biomass across bacterial and yeast hosts, although product titer and full temperature breadth require separate validation. (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2)
- **Enzyme biotechnology:** thermostable enzymes support high-temperature catalysis and are genetically encoded, but enzyme thermostability should be represented as a warm-end mechanism rather than evidence of whole-cell eurythermy.
- **Environmental resilience:** broad-range organisms such as RW2 may remain active during strong diel, seasonal, or process-driven temperature fluctuations. RW2 originated in a permanently cold 4–10°C microbialite yet retained growth to 50°C, suggesting a generalist capacity whose ecological maintenance remains unresolved. (white2019thecompletegenome pages 17-18, white2019thecompletegenome pages 1-2)
- **Synthetic biology:** a rational design would combine regulated lipid remodeling, RNA chaperoning, protein quality control, and oxidative protection. Evidence currently supports engineering the modules separately; it does not establish that simply stacking them will produce `METPO:1000487`.

## 6. Curation warnings

1. **Do not equate tolerance with growth.** Acute survival, colony recovery after heat shock, enzyme activity, and spore resistance are insufficient.
2. **Do not infer breadth from one endpoint.** CspL supports high-temperature growth but does not demonstrate >30°C breadth.
3. **Do not transfer pathways across taxa without qualification.** DesK/DesR/des is well described in *B. subtilis*; RW2’s lipid remodeling does not prove that it uses the identical regulatory chain.
4. **Mark RW2 genomic annotations as predicted.** `dnaJ`, `dnaK`, `grpE`, `opu`, `proU`, carotenoid synthesis, and fatty-acid regulation are candidate explanations, not validated necessities. (white2019thecompletegenome pages 10-11, white2019thecompletegenome pages 1-2)
5. **Do not curate generic thermostability as sufficient.** Stable proteins extend warm-end function but can trade stability against low-temperature catalytic flexibility.
6. **Treat oxidative protection and compatible solutes as provisional.** They are biologically plausible but lack direct evidence for expanding RW2’s temperature breadth.
7. **Preserve assay context.** Medium solidity, composition, pH, NaCl, oxygenation, duration, and detection limit can shift apparent endpoints.
8. **Resolve an apparent reporting discrepancy before importing exact minima.** The RW2 paper discusses broader genus-level or tolerance values down to −12°C, but direct growth supporting the strong phenotype statement is 4–50°C; use **4–50°C** unless primary endpoint data verify growth below 4°C. (white2019thecompletegenome pages 7-9, white2019thecompletegenome pages 3-4)
9. **Avoid unsupported ontology CURIEs.** Keep strain-specific lipids, genes, and assay concepts label-only until exact database records are verified.

## 7. DOI-first bibliography

1. **Moon S, et al.** “Temperature Matters: Bacterial Response to Temperature Change.” *Journal of Microbiology* 61, 343–357. **Published March 2023.** DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x). (moon2023temperaturemattersbacterial pages 7-9)
2. **García-Descalzo L, García-López E, Cid C.** “Comparative Proteomic Analysis of Psychrophilic vs. Mesophilic Bacterial Species Reveals Different Strategies to Achieve Temperature Adaptation.” *Frontiers in Microbiology* 13. **Published May 2022.** DOI: [10.3389/fmicb.2022.841359](https://doi.org/10.3389/fmicb.2022.841359). (garciadescalzo2022comparativeproteomicanalysis pages 1-2)
3. **Zhou Z, et al.** “A cold shock protein promotes high-temperature microbial growth through binding to diverse RNA species.” *Cell Discovery* 7. **Published March 2021.** DOI: [10.1038/s41421-021-00246-5](https://doi.org/10.1038/s41421-021-00246-5). (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2)
4. **White RA III, et al.** “The Complete Genome and Physiological Analysis of the Eurythermal Firmicute *Exiguobacterium chiriqhucha* Strain RW2…” *Frontiers in Microbiology* 9. **Published January 2019.** DOI: [10.3389/fmicb.2018.03189](https://doi.org/10.3389/fmicb.2018.03189). (white2019thecompletegenome pages 17-18, white2019thecompletegenome pages 10-11, white2019thecompletegenome pages 7-9, white2019thecompletegenome pages 1-2)
5. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68, 101–116. **Published September 2014.** DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 2-4)
6. **Vieille C, Zeikus GJ.** “Hyperthermophilic Enzymes: Sources, Uses, and Molecular Mechanisms for Thermostability.” *Microbiology and Molecular Biology Reviews* 65, 1–43. **Published March 2001.** DOI: [10.1128/MMBR.65.1.1-43.2001](https://doi.org/10.1128/MMBR.65.1.1-43.2001).

## Final curation recommendation

Curate RW2’s **4–50°C growth** as the principal taxon-to-trait evidence. Curate the DesK→DesR→des→unsaturated-fatty-acid chain as a taxon-scoped mechanistic subgraph for cold-end membrane adaptation, and CspL RNA binding→high-temperature growth as a separately scoped, direct perturbation edge. Connect either module to `METPO:1000487` only with a qualified predicate such as `contributes_to` or `candidate_mechanism_for`; a direct `causes` edge is not yet justified. Retain DnaK/DnaJ/GrpE, compatible-solute systems, carotenoids, proteases, and generic protein thermostability as candidate nodes or uncertain edges pending knockout, complementation, or controlled temperature-range experiments.

References

1. (white2019thecompletegenome pages 17-18): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

2. (white2019thecompletegenome pages 10-11): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

3. (white2019thecompletegenome pages 7-9): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 104 citations and is from a peer-reviewed journal.

5. (white2019thecompletegenome pages 3-4): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

6. (zhou2021acoldshock pages 5-6): Zikang Zhou, Hongzhi Tang, Weiwei Wang, Lige Zhang, Fei Su, Yuanting Wu, Linquan Bai, Sicong Li, Yuhui Sun, Fei Tao, and Ping Xu. A cold shock protein promotes high-temperature microbial growth through binding to diverse rna species. Cell Discovery, Mar 2021. URL: https://doi.org/10.1038/s41421-021-00246-5, doi:10.1038/s41421-021-00246-5. This article has 45 citations and is from a peer-reviewed journal.

7. (zhou2021acoldshock pages 1-2): Zikang Zhou, Hongzhi Tang, Weiwei Wang, Lige Zhang, Fei Su, Yuanting Wu, Linquan Bai, Sicong Li, Yuhui Sun, Fei Tao, and Ping Xu. A cold shock protein promotes high-temperature microbial growth through binding to diverse rna species. Cell Discovery, Mar 2021. URL: https://doi.org/10.1038/s41421-021-00246-5, doi:10.1038/s41421-021-00246-5. This article has 45 citations and is from a peer-reviewed journal.

8. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

9. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

10. (white2019thecompletegenome pages 1-2): Richard Allen White, Sarah A. Soles, Greg Gavelis, Emma Gosselin, Greg F. Slater, Darlene S. S. Lim, Brian Leander, and Curtis A. Suttle. The complete genome and physiological analysis of the eurythermal firmicute exiguobacterium chiriqhucha strain rw2 isolated from a freshwater microbialite, widely adaptable to broad thermal, ph, and salinity ranges. Frontiers in Microbiology, Jan 2019. URL: https://doi.org/10.3389/fmicb.2018.03189, doi:10.3389/fmicb.2018.03189. This article has 56 citations and is from a peer-reviewed journal.

11. (mendoza2014temperaturesensingby pages 4-5): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

12. (garciadescalzo2022comparativeproteomicanalysis pages 1-2): Laura García-Descalzo, Eva García-López, and Cristina Cid. Comparative proteomic analysis of psychrophilic vs. mesophilic bacterial species reveals different strategies to achieve temperature adaptation. Frontiers in Microbiology, May 2022. URL: https://doi.org/10.3389/fmicb.2022.841359, doi:10.3389/fmicb.2022.841359. This article has 31 citations and is from a peer-reviewed journal.