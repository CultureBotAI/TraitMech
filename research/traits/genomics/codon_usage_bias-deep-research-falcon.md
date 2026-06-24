---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:55:19.805329'
end_time: '2026-06-18T03:19:55.759901'
duration_seconds: 1475.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: codon usage bias
  trait_identifier: traitmech:000096
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: codon_usage_bias
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genome-sequence property describing non-uniform usage of synonymous
    codons across a genome, shaped by mutational bias and translational selection
    and correlated with gene expression level.
  parent_traits: METPO:1000188
  synonyms: codon bias
  evidence_summary: 'DOI:10.1038/nrg2899:  (Plotkin & Kudla review the causes and
    consequences of synonymous codon bias.) | DOI:10.1146/annurev.genet.42.110807.091442:  (Hershberg
    & Petrov review selection on codon bias across genomes.)'
  causal_graph_summary: 'codon_bias_translation_efficiency: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 71
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** codon usage bias
- **METPO identifier:** traitmech:000096
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing non-uniform usage of synonymous codons across a genome, shaped by mutational bias and translational selection and correlated with gene expression level.
- **Parent traits:** METPO:1000188
- **Synonyms:** codon bias
- **Existing evidence:** DOI:10.1038/nrg2899:  (Plotkin & Kudla review the causes and consequences of synonymous codon bias.) | DOI:10.1146/annurev.genet.42.110807.091442:  (Hershberg & Petrov review selection on codon bias across genomes.)
- **Existing causal graph summary:** codon_bias_translation_efficiency: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **codon usage bias** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/codon_usage_bias.yaml`.

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
- **Trait label:** codon usage bias
- **METPO identifier:** traitmech:000096
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing non-uniform usage of synonymous codons across a genome, shaped by mutational bias and translational selection and correlated with gene expression level.
- **Parent traits:** METPO:1000188
- **Synonyms:** codon bias
- **Existing evidence:** DOI:10.1038/nrg2899:  (Plotkin & Kudla review the causes and consequences of synonymous codon bias.) | DOI:10.1146/annurev.genet.42.110807.091442:  (Hershberg & Petrov review selection on codon bias across genomes.)
- **Existing causal graph summary:** codon_bias_translation_efficiency: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **codon usage bias** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/codon_usage_bias.yaml`.

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


## Research report: Microbial codon usage bias (TraitMech candidate; METPO traitmech:000096)

### Scope summary (TraitMech curation)
**Codon usage bias (CUB)** is a *genome-sequence property* describing non-uniform use of synonymous codons across coding sequences. Mechanistically, CUB reflects a balance of (i) **mutational biases** (e.g., genome-wide base composition/GC content and context-dependent mutation/repair) and (ii) **selection on translation** (typically for translational efficiency and/or accuracy), often strongest in genes with high protein-production demand. Standard operationalizations use metrics such as **RSCU**, **CAI**, **FOP**, **tAI**, and **ENC**. Plotkin & Kudla emphasize that codon-usage patterns are produced by both mutational and selective categories of mechanisms, and that within-genome variation is often interpreted through translation dynamics (initiation/elongation) but can also arise from neutral processes such as horizontal gene transfer and replication-strand nucleotide biases. (plotkin2011synonymousbutnot pages 2-3, plotkin2011synonymousbutnot pages 4-5)

**Boundary cases / nearby traits (do not conflate in curation):**
- **Local 5′-CDS effects** (first ~10–50 codons; mRNA folding and RBS accessibility) can strongly influence expression but are not identical to genome-wide CUB (plotkin2011synonymousbutnot pages 6-7, nieuwkoop2023revealingdeterminantsof pages 1-1).
- **Start/stop codon usage** and stop-codon readthrough relate to translation initiation/termination efficiency but are not “synonymous codon bias” strictly (farookhi2024differentialselectionfor pages 1-2).
- **Amino-acid usage bias** can confound codon-bias metrics and should be controlled in inference (cope2024evolutionaryprinciplesunderpinning pages 11-14).
- **HGT or replication-strand base-composition effects** can generate codon frequency skews without translational adaptation (plotkin2011synonymousbutnot pages 4-5).

### Key concepts and definitions (current understanding)
**Core definitions and measures**
- **RSCU (Relative Synonymous Codon Usage):** defined as observed frequency divided by expected under equal usage within a synonymous family; Plotkin & Kudla note interpretive anchors: **0** (codon absent), **1** (no bias), and up to **6** for sixfold-degenerate families. (plotkin2011synonymousbutnot pages 2-3)
- **CAI (Codon Adaptation Index):** similarity of a gene’s codon usage to that of highly expressed genes (proxying “optimal codons”). (plotkin2011synonymousbutnot pages 2-3, fan2024genrcaauserfriendly pages 3-5)
- **tAI (tRNA Adaptation Index):** similarity of codon usage to relative **tRNA gene copy numbers** (a proxy for supply). (plotkin2011synonymousbutnot pages 2-3, johnson2023growthdependentgeneexpression pages 13-15)
- **ENC (Effective Number of Codons):** widely used measure of overall codon-bias strength (lower values = stronger bias; definition not quantified in retrieved excerpts but identified as a standard metric). (farookhi2024differentialselectionfor pages 19-21, fan2024genrcaauserfriendly pages 3-5)

**Mechanistic framing**
- **Mutational-bias mechanisms:** include point-mutation biases and contextual mutation/repair biases that help set genome-wide GC composition, which propagates to synonymous codon frequencies. (plotkin2011synonymousbutnot pages 2-3)
- **Selection on translation:** preferred codons are commonly interpreted as being translated faster and/or more accurately, often by matching abundant tRNAs; this selection is typically **weak** (population-genetics sense) but detectable across genes/genomes. (hershberg2008selectiononcodon pages 2-3)
- **Translation initiation vs elongation as mediators:** Plotkin & Kudla emphasize that initiation and elongation rates jointly determine ribosome density and protein synthesis, which can complicate naive “codon optimality → more protein” narratives. (plotkin2011synonymousbutnot pages 2-3)

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Growth-condition dependence: codon bias is tied to rapid-growth physiology (2023)
Johnson et al. (2023) show that **growth-rate dependent expression variation** constrains codon-bias evolution. They define a **Growth Correlation Index (GCI)** as the Pearson correlation between a gene’s expression and growth rate, ranging from about **−1 to 1**, and find GCI is a positive predictor of codon usage bias independent of mean expression. Genes with positive GCI (upregulated during rapid growth) have stronger codon usage bias than genes with comparable mean expression but negative GCI; results generalize across **E. coli** transcriptome/proteome and **S. cerevisiae** datasets and multiple codon-bias metrics (CAI, tAI, ROC-SEMPPR). (johnson2023growthdependentgeneexpression pages 6-8, johnson2023growthdependentgeneexpression pages 13-15)

#### 2) Quantifying start-region determinants: first ~8 codons and local mRNA structure dominate expression variance in a controlled bacterial library (2023)
Nieuwkoop et al. (2023) built a whole-gene codon-randomized library of **mRFP** in **E. coli**, retaining **1,459** high-quality sequence–expression pairs. A Random Forest model predicted protein production with **Pearson r ≈ 0.762**, and the predictive signal “lies on the sequence information of the first eight codons.” (nieuwkoop2023revealingdeterminantsof pages 1-1)

They validated fluorescence as a protein proxy via LC–MS/MS (Pearson **r = 0.901** between fluorescence and proteomics for 10 variants) and found that the most predictive sequence/structure features are near the start codon and RBS. (nieuwkoop2023revealingdeterminantsof pages 7-8, nieuwkoop2023revealingdeterminantsof pages 8-9)

This supports a mechanistic edge: **synonymous codon choice near the translation start** modulates protein production largely via **local secondary structure/RBS accessibility**, and global CAI can be a weak design heuristic in such settings. (nieuwkoop2023revealingdeterminantsof pages 1-2, nieuwkoop2023revealingdeterminantsof pages 12-13)

#### 3) Stress-responsive “tRNA reprogramming” links environment to codon-biased translation programs (2023–2024)
Mitchener et al. (2023) synthesize evidence that tRNA modifications (notably at anticodon-loop positions 34/37) are **dynamically reprogrammed in response to cellular stresses**, and that this reprogramming drives **codon-biased translation** of “modification tunable transcripts” (MoTTs). They report that each tRNA carries ~**8–10 modifications** that can change under stress, enabling preferential translation of mRNAs enriched for codons decoded more efficiently by the modified tRNAs. (mitchener2023molecularcopingmechanisms pages 1-2)

A key mechanistic example: the tRNA methyltransferase **Trm9** installs wobble-U modifications **mcm5U/mcm5s2U**; loss of Trm9 reduces methylation ~**4-fold** and causes ~**6–7-fold** reduced translation of reporters enriched in **AGA (Arg)** and **GAA (Glu)** codons; codon-optimizing an endogenous target (RNR1) rescues the phenotype, supporting a causal chain stress/cell-cycle state → tRNA modification state → codon-specific translation output. (mitchener2023molecularcopingmechanisms pages 4-5)

Yared et al. (2024) add bacterial examples for stress-responsive tRNA modification effects. In **Pseudomonas aeruginosa**, oxidative stress (H2O2) increases **trmB** transcription and **m7G46** modification; loss of trmB reduces efficient translation of Phe/Asp codons and decreases catalase (KatA/KatB) production, causing H2O2 sensitivity. (yared2024beyondtheanticodon pages 11-12)

#### 4) Comparative genomics: tRNA modification capacity correlates with codon-usage variability across Proteobacteria (2024)
Delgado et al. (2024) analyze ~**1,484** proteobacterial genomes and report that presence/absence of genes encoding **tRNA anticodon-loop modifications** strongly associates with codon-usage frequencies and genomic GC%. Their genome-wide association (Roary/Scoary) found the strongest associations for modification enzymes such as **tilS** (lysidine formation), **tsaB** (t6A formation), and **gluQ**, with very low P-values (**< 1e−10**). (delgado2024impactofthe pages 2-4)

They also report that genomes with GC% below ~**40%** tend to lack some tRNA modification genes (e.g., GluQRS, TsaB), and that presence of tsaB or gluQ associates with higher GC% while genomes lacking both tend to have lower GC%. (delgado2024impactofthe pages 7-8, delgado2024impactofthe pages 6-7)

These findings are highly relevant to a TraitMech graph because they suggest that **modification-dependent decoding constraints** can shape the allowable evolutionary space of codon frequencies, but the conclusions are primarily correlational and should be curated with uncertainty until experimentally validated. (delgado2024impactofthe pages 7-8, delgado2024impactofthe pages 6-7)

#### 5) Temperature-dependent tRNA modifications as a microbial adaptation layer (2024)
Hoffmann et al. (2024) compare Bacillales across temperature niches and show strong temperature dependence in tRNA modification profiles. In the thermophile **Geobacillus stearothermophilus**, the number of modified tRNAs at positions such as D17, D20, and Ψ55 increases with temperature (example counts across 40/55/70°C: **D17 1→12→13; D20 6→18→19; Ψ55 9→21→29**) and **s4U8** occurrences are much higher than in non-thermophiles (**>24 vs ≤4**). (hoffmann2024temperaturedependenttrnamodifications pages 9-10)

Psychrophilic/mesophilic bacteria show higher dihydrouridine abundance, interpreted as increasing local flexibility for cold adaptation. These data support environment → tRNA modification state edges that can plausibly couple to codon-biased translation and, in the long run, to codon usage evolution. (hoffmann2024temperaturedependenttrnamodifications pages 1-2, hoffmann2024temperaturedependenttrnamodifications pages 17-19)

### Current applications and real-world implementations
#### Codon optimization and expression prediction tools (2024)
Fan et al. (2024) released **GenRCA**, a free web tool implementing **31 codon usage bias indices** and supporting **65 expression host species**, enabling comprehensive CUB assessment and codon optimization decisions. Indices are grouped into categories covering uniformity deviations (e.g., RSCU, ENC), reference-based indices (e.g., CAI, FOP), tRNA-adaptation indices (e.g., tAI), and more complex features (e.g., GC content, ENcp). GenRCA supports batch processing, interactive plots, and downloadable reports; the authors highlight that no single index universally works across species. (fan2024genrcaauserfriendly pages 1-3, fan2024genrcaauserfriendly pages 3-5, fan2024genrcaauserfriendly pages 5-8)

#### Synthetic biology design insight: optimize the start region, not only global CAI (2023)
Nieuwkoop et al. provide data-driven engineering guidance: in their E. coli library, expression is largely determined by sequence features within the first ~8 codons and local 5′ structure, implying that “full-CDS CAI optimization” may underperform compared with **reducing inhibitory 5′ structure**. (nieuwkoop2023revealingdeterminantsof pages 1-1, nieuwkoop2023revealingdeterminantsof pages 1-2)

### Expert opinions and analysis from authoritative sources
- Plotkin & Kudla (Nature Reviews Genetics) emphasize that codon bias is central for both molecular evolution and biotechnology, and they highlight that translation initiation/elongation dynamics are essential for interpreting synonymous variation. They also explicitly caution that codon-usage variation can arise from neutral processes (HGT; replication strand biases), which must be separated from selection-based interpretations when curating causal graphs. (plotkin2011synonymousbutnot pages 2-3, plotkin2011synonymousbutnot pages 4-5)
- Hershberg & Petrov (Annual Review of Genetics) synthesize population-genetic evidence that codon bias is maintained by selection–mutation–drift balance and review evidence for selection for translational accuracy/efficiency, including experimental quantification of missense and elongation rate effects. (hershberg2008selectiononcodon pages 2-3)
- Cope et al. (2024) argue for **selection–mutation–drift equilibrium** as a useful default null model and emphasize that analyses must control for gene expression and mechanistic plausibility; they also discuss ROC-SEMPPR/ASUMDE-like frameworks that estimate selection coefficients and mutation biases from sequence. (cope2024evolutionaryprinciplesunderpinning pages 8-11, cope2024evolutionaryprinciplesunderpinning pages 11-14)

### Relevant recent statistics and data points (curation-useful)
- RSCU interpretive scale: **0 absent; 1 unbiased; up to 6** for sixfold families. (plotkin2011synonymousbutnot pages 2-3)
- Translational accuracy/speed effects (reviewed): codon choice changed misincorporation **4–9×**, and frequent codons incorporated amino acids **~6× faster** than rare codons. (hershberg2008selectiononcodon pages 2-3)
- 5′ mRNA structure threshold: in E. coli GFP example, 5′ folding energy below **~−10 kcal/mol** strongly inhibits expression; Figure 3 summarizes initiation occlusion mechanisms. (plotkin2011synonymousbutnot pages 6-7, plotkin2011synonymousbutnot media 4022dfe4)
- Codon-randomization library scale: **1,459** E. coli mRFP variants; RF predictor **r ≈ 0.762**; fluorescence–proteomics **r = 0.901** (10 variants). (nieuwkoop2023revealingdeterminantsof pages 1-1, nieuwkoop2023revealingdeterminantsof pages 7-8)
- Mtb tRNA pool: despite single-copy tRNA genes, relative tRNA levels vary by **~an order of magnitude**; codon usage correlates with tRNA adaptability (TAc), but codon optimality metrics did **not** correlate with translation efficiency in that system. (soman2023codonoptimalityhas pages 1-2)
- Bacillales temperature-linked modifications: example modification count increases with temperature (**D17 1→12→13; D20 6→18→19; Ψ55 9→21→29**) and higher **s4U8** occurrences (**>24 vs ≤4**). (hoffmann2024temperaturedependenttrnamodifications pages 9-10)
- Proteobacteria comparative genomics: ~**1,484** genomes; top tRNA modification genes associated with codon usage/GC% have P-values **< 1e−10**. (delgado2024impactofthe pages 2-4)

### Visual evidence (mechanistic)
Figure evidence for the edge **mRNA secondary structure near the start site → translation initiation inhibition** is provided by Plotkin & Kudla’s Figure 3, which depicts RBS/SD occlusion and a folding-energy threshold for strong inhibition of GFP expression in E. coli. (plotkin2011synonymousbutnot media 4022dfe4)

### Candidate nodes (grouped) with ontology grounding suggestions
| Node label | Node type | Suggested CURIE(s) | Evidence/justification | Notes |
|---|---|---|---|---|
| codon usage bias | trait / genome property | METPO:traitmech:000096 | Trait target; defined as non-uniform synonymous codon usage shaped by mutational bias and translational selection; foundational reviews discuss causes and consequences of codon bias (plotkin2011synonymousbutnot pages 2-3, hershberg2008selectiononcodon pages 2-3) | Core TraitMech node; class-level genome-sequence property |
| synonymous codon usage | genome property / process descriptor | label only | Central concept in codon-bias literature; Plotkin & Kudla explicitly discuss synonymous codons and codon bias (plotkin2011synonymousbutnot pages 2-3) | Near-synonym/related descriptor; may be redundant with codon usage bias depending on graph granularity |
| mutational bias | evolutionary process | label only | Explicitly identified as a main force shaping codon usage; includes context-dependent mutation and base-composition effects (plotkin2011synonymousbutnot pages 2-3, hershberg2008selectiononcodon pages 2-3) | Broad upstream driver; no single GO term exactly captures genome-wide mutational bias |
| GC content | genome property | label only | Plotkin & Kudla note GC content is largely set by mutational processes; multiple recent studies link GC% with codon usage and tRNA-modification gene presence (plotkin2011synonymousbutnot pages 2-3, delgado2024impactofthe pages 1-2, delgado2024impactofthe pages 2-4, delgado2024impactofthe pages 6-7) | Important measurable covariate; not itself codon bias |
| translation initiation | biological process | GO:0006413 | Translation initiation efficiency is a major mechanism linking 5′ sequence features to expression; discussed in foundational review and recent comparative work (farookhi2024differentialselectionfor pages 1-2, plotkin2011synonymousbutnot pages 4-5, plotkin2011synonymousbutnot pages 6-7) | Strong candidate mediator node |
| translation elongation | biological process | GO:0006414 | Codon adaptation, tRNA supply, and local codon choice affect elongation rate and efficiency (farookhi2024differentialselectionfor pages 1-2, plotkin2011synonymousbutnot pages 2-3, hershberg2008selectiononcodon pages 2-3) | Strong candidate mediator node |
| translation termination | biological process | GO:0006415 | Farookhi & Xia discuss stop-codon identity and +4 nucleotide effects on termination/readthrough (farookhi2024differentialselectionfor pages 1-2) | Neighboring translation process; outside strict synonymous-sense-codon scope but relevant boundary node |
| Shine–Dalgarno interaction | molecular interaction / RNA-RNA pairing | label only | Initiation efficiency depends on SD pairing with anti-SD on rRNA in bacteria (farookhi2024differentialselectionfor pages 1-2, plotkin2011synonymousbutnot media 4022dfe4) | Bacterial-specific initiation mechanism; grounding could be added later if a suitable ontology term is chosen |
| mRNA secondary structure | molecular feature | label only | Strong 5′ mRNA structure inhibits initiation; Figure 3 and E. coli GFP threshold around −10 kcal/mol support this (plotkin2011synonymousbutnot pages 4-5, plotkin2011synonymousbutnot pages 6-7, plotkin2011synonymousbutnot media 4022dfe4) | Useful mechanistic node; often localized to 5′ CDS/RBS region |
| tRNA abundance | molecular quantity | label only | Preferred codons often correspond to abundant tRNAs; direct measurements and correlations discussed across reviews and Mtb study (soman2023codonoptimalityhas pages 1-2, hershberg2008selectiononcodon pages 2-3) | Quantity/state node rather than entity |
| tRNA pool | molecular pool / cellular resource | label only | tRNA pool abundance/composition is repeatedly invoked as a determinant of codon adaptation and translation efficiency (farookhi2024differentialselectionfor pages 1-2, soman2023codonoptimalityhas pages 1-2, johnson2023growthdependentgeneexpression pages 8-10) | Good aggregate node for graph simplicity |
| tRNA modification | molecular process / modification state | GO:0006400 | Stress-responsive reprogramming of tRNA modifications drives codon-biased translation; multiple specific modifications discussed (mitchener2023molecularcopingmechanisms pages 4-5, mitchener2023molecularcopingmechanisms pages 2-4, mitchener2023molecularcopingmechanisms pages 1-2, mitchener2023molecularcopingmechanisms pages 5-6) | Use as parent node for specific modified nucleosides |
| 5-methoxycarbonylmethyluridine (mcm5U) | modified nucleoside | CHEBI:19610 | Trm9-mediated wobble modification implicated in codon-biased translation of AGA/GAA-enriched transcripts (mitchener2023molecularcopingmechanisms pages 4-5, mitchener2023molecularcopingmechanisms pages 2-4, mitchener2023molecularcopingmechanisms pages 5-6) | Specific tRNA wobble modification; strong mechanistic evidence, mainly yeast-centric in cited review |
| 5-methoxycarbonylmethyl-2-thiouridine (mcm5s2U) | modified nucleoside | CHEBI:76955 | Listed with mcm5U as Trm9-dependent wobble U modification affecting decoding and stress response translation (mitchener2023molecularcopingmechanisms pages 4-5, mitchener2023molecularcopingmechanisms pages 2-4) | Strong mechanistic candidate; microbial transferability should be checked case-by-case |
| 5-methylcytidine (m5C) | modified nucleoside | CHEBI:27812 | Oxidative stress/H2O2-associated increases in m5C and Trm4-dependent translational effects are described (mitchener2023molecularcopingmechanisms pages 5-6, yared2024beyondtheanticodon pages 8-10) | Modification state can be represented either as molecule or as tRNA methylation event |
| 7-methylguanosine at position 46 (m7G46) | modified nucleoside / tRNA feature | CHEBI:18241 | Hoffmann et al. detect m7G46 across Bacillales; Yared et al. cite trmB/m7G46 effects on oxidative-stress catalase translation (yared2024beyondtheanticodon pages 11-12, hoffmann2024temperaturedependenttrnamodifications pages 6-9, hoffmann2024temperaturedependenttrnamodifications pages 9-10) | Strong bacterial relevance |
| 4-thiouridine at position 8 (s4U8) | modified nucleoside / tRNA feature | CHEBI:17609 | Temperature- and UV/stress-linked tRNA modification in Bacillales; affects stability and UV sensing (yared2024beyondtheanticodon pages 11-12, hoffmann2024temperaturedependenttrnamodifications pages 1-2, hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 6-9) | Strong environmental-response node |
| pseudouridine at position 55 (Ψ55) | modified nucleoside / tRNA feature | CHEBI:17802 | Hoffmann et al. report temperature-linked increases in Ψ55 in thermophilic Bacillales (hoffmann2024temperaturedependenttrnamodifications pages 17-19, hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 9-10) | Good temperature-adaptation node |
| dihydrouridine | modified nucleoside | CHEBI:17508 | Psychrophilic/mesophilic Bacillales show higher D abundance, interpreted as increasing local tRNA flexibility in cold (hoffmann2024temperaturedependenttrnamodifications pages 1-2, hoffmann2024temperaturedependenttrnamodifications pages 17-19, hoffmann2024temperaturedependenttrnamodifications pages 19-20, hoffmann2024temperaturedependenttrnamodifications pages 9-10) | Useful environment-linked tRNA chemistry node |
| stringent response | biological process | GO:0009269 | UV-linked s4U8 crosslinking causes uncharged tRNA accumulation, ribosome stalling, ppGpp production, and stringent response (yared2024beyondtheanticodon pages 11-12) | Strong bacterial stress-response node |
| guanosine tetraphosphate / ppGpp | signaling nucleotide | CHEBI:16696 | Explicit downstream mediator of s4U8-linked UV response and stringent response (yared2024beyondtheanticodon pages 11-12) | Useful chemical mediator node |
| oxidative stress | biological process / environmental condition | GO:0006979 | H2O2 and oxidative stress trigger tRNA modification changes and codon-biased stress-protein translation (mitchener2023molecularcopingmechanisms pages 7-8, mitchener2023molecularcopingmechanisms pages 5-6, yared2024beyondtheanticodon pages 11-12, yared2024beyondtheanticodon pages 8-10) | Strong environmental/process node |
| UV stress | environmental condition / stress process | GO:0009411 | UV induces s4U8:C13 crosslinks and stringent-response signaling (yared2024beyondtheanticodon pages 11-12) | May be represented as UV response or ultraviolet radiation exposure depending ontology choice |
| growth rate | physiological property | label only | Johnson et al. define GCI linking expression to growth rate; growth-dependent expression strongly influences codon bias strength (johnson2023growthdependentgeneexpression pages 8-10, johnson2023growthdependentgeneexpression pages 6-8, johnson2023growthdependentgeneexpression pages 1-3, johnson2023growthdependentgeneexpression pages 10-11, johnson2023growthdependentgeneexpression pages 13-15) | Trait-like quantitative covariate; no simple GO term for generic microbial growth rate |
| horizontal gene transfer | biological process | GO:0019083 | Identified as a non-translational contributor to codon-usage variation within genomes (plotkin2011synonymousbutnot pages 4-5) | Boundary-case node; affects codon composition without necessarily reflecting translational adaptation |
| Escherichia coli | taxon | NCBITaxon:562 | Major model system in growth-condition, codon-randomization, and translation-initiation studies (johnson2023growthdependentgeneexpression pages 8-10, nieuwkoop2023revealingdeterminantsof pages 1-2, nieuwkoop2023revealingdeterminantsof pages 6-7, plotkin2011synonymousbutnot media 4022dfe4) | Key exemplar taxon |
| Mycobacterium tuberculosis | taxon | NCBITaxon:1773 | Mtb study shows strong codon bias/codon–tRNA coadaptation but weak link to translation efficiency (soman2023codonoptimalityhas pages 1-2) | Important counterexample taxon |
| Proteobacteria | taxon | NCBITaxon:1224 | Delgado et al. analyze ~1,484 proteobacterial genomes to link tRNA-modification genes with codon-usage variability (delgado2024impactofthe pages 1-2, delgado2024impactofthe pages 2-4, delgado2024impactofthe pages 4-6, delgado2024impactofthe pages 6-7) | High-level taxon for comparative edges |
| Bacillales | taxon | NCBITaxon:1385 | Hoffmann et al. profile temperature-dependent tRNA modifications across Bacillales (hoffmann2024temperaturedependenttrnamodifications pages 1-2, hoffmann2024temperaturedependenttrnamodifications pages 6-9, hoffmann2024temperaturedependenttrnamodifications pages 9-10, hoffmann2024temperaturedependenttrnamodifications pages 10-11) | High-level taxon for temperature-adaptation edges |


*Table: This table lists curation-ready candidate nodes for a microbial codon-usage-bias causal graph, grouped by biological type and paired with suggested ontology groundings where reasonably standard. It is useful for translating the literature into stable graph entities while flagging nodes that remain label-only or need narrower taxon-specific curation.*

### Candidate causal edges (evidence-backed; curation table)
| Edge (triple) | Mechanistic rationale | Evidence snippet (short quote/paraphrase with key numbers) | Source (DOI + URL) | Publication date (month/year) | Notes/uncertainty for curation |
|---|---|---|---|---|---|
| mutational bias → shapes → codon usage bias | Genome-wide base-composition and context-dependent mutation biases alter synonymous codon frequencies. | Plotkin & Kudla classify explanations as “mutational and selective”; “GC content is largely set by mutational processes,” and context-dependent mutation predicts codon-usage context dependence (e.g., CpG effects). (plotkin2011synonymousbutnot pages 2-3) | 10.1038/nrg2899 https://doi.org/10.1038/nrg2899 | 11/2011 | Strong, broad mechanism; curate as general upstream driver. |
| natural selection for translational efficiency/accuracy → shapes → codon usage bias | Preferred codons can be favored because they improve elongation speed and/or accuracy, especially where translation demand is high. | Hershberg & Petrov: preferred codons often match abundant tRNAs; codon choice changed misincorporation “4–9-fold,” and amino-acid incorporation at frequent codons was “almost six times faster” than at rare codons. (hershberg2008selectiononcodon pages 2-3) | 10.1146/annurev.genet.42.110807.091442 https://doi.org/10.1146/annurev.genet.42.110807.091442 | 12/2008 | Strong foundational evidence; exact balance of speed vs accuracy may vary by taxon/gene. |
| high gene expression level → strengthens selection for → codon usage bias | Selection on synonymous codons scales with protein production; highly expressed genes show stronger codon preferences. | Hershberg & Petrov: codon bias “correlates most strongly with gene expression level.” Cope et al. summarize ASUMDE/ROC-SEMPPR frameworks where codon-specific selection scales with per-gene protein production rate. (hershberg2008selectiononcodon pages 2-3, cope2024evolutionaryprinciplesunderpinning pages 8-11) | 10.1146/annurev.genet.42.110807.091442 https://doi.org/10.1146/annurev.genet.42.110807.091442; 10.32942/x2802v https://doi.org/10.32942/x2802v | 12/2008; 05/2024 | Strong general edge; metric used to estimate expression may affect inference. |
| rapid growth condition → strengthens → expression–codon-bias association | During fast growth, genes induced with growth show stronger codon bias, consistent with stronger translational selection. | Johnson et al.: GCI (range about -1 to 1) positively predicts CUB; in E. coli primary RNA-seq dataset they analyze 250 conditions, and another processed set includes 3,923 genes across 103 conditions. Genes upregulated at high growth have stronger CUB across CAI, tAI, ROC-SEMPPR. (johnson2023growthdependentgeneexpression pages 8-10, johnson2023growthdependentgeneexpression pages 6-8, johnson2023growthdependentgeneexpression pages 1-3, johnson2023growthdependentgeneexpression pages 10-11, johnson2023growthdependentgeneexpression pages 13-15) | 10.1093/molbev/msad189 https://doi.org/10.1093/molbev/msad189 | 03/2023 | Strong but condition-dependent; relates growth physiology to realized selection rather than defining the trait alone. |
| short generation time / rapid growth strategy → selects for → codon–anticodon adaptation | Fast-growing bacteria are predicted to optimize translation machinery and codon usage more strongly than slow growers. | Farookhi & Xia contrast short-generation bacteria (e.g., E. coli ~20–30 min) with long-generation bacteria (e.g., Mycobacterium leprae ~2 weeks) and predict more tRNA genes, better codon/anticodon adaptation, and weaker start-region structure in short-generation bacteria. (farookhi2024differentialselectionfor pages 1-2) | 10.3390/microorganisms12040768 https://doi.org/10.3390/microorganisms12040768 | 04/2024 | Comparative/macroevolutionary edge; useful but somewhat inferential for per-genome curation. |
| tRNA abundance / tRNA pool → influences → codon adaptation | Synonymous codons decoded by more abundant tRNAs tend to be more adapted and often preferred. | Plotkin & Kudla define tAI by similarity to relative tRNA gene copy numbers; Hershberg & Petrov cite direct tRNA-level support. Soman et al.: “The more abundant the tRNAs that decode a codon, the more adapted the codon is.” In Mtb, tRNA levels vary by “an order of magnitude.” (plotkin2011synonymousbutnot pages 2-3, hershberg2008selectiononcodon pages 2-3, soman2023codonoptimalityhas pages 1-2) | 10.1038/nrg2899 https://doi.org/10.1038/nrg2899; 10.1146/annurev.genet.42.110807.091442 https://doi.org/10.1146/annurev.genet.42.110807.091442; 10.1038/s41598-022-27164-0 https://doi.org/10.1038/s41598-022-27164-0 | 11/2011; 12/2008; 01/2023 | Strong general edge, but tRNA gene copy number is only a proxy and can fail in some taxa/conditions. |
| genomic codon usage ↔ coevolves with ↔ tRNA adaptability | Codon frequencies and decoding capacity can co-evolve over evolutionary time. | Soman et al.: Mtb has single-copy tRNA genes yet tRNA levels vary by an order of magnitude; codons decoded by abundant tRNAs show higher adaptability, and there is a “general positive correlation between genomic codon usage and the tRNA adaptability of codons (TAc).” (soman2023codonoptimalityhas pages 1-2) | 10.1038/s41598-022-27164-0 https://doi.org/10.1038/s41598-022-27164-0 | 01/2023 | Strong for coadaptation, but in Mtb this did not translate into mRNA abundance/translation-efficiency correlations. |
| codon optimality measures → may not predict → translation efficiency in all microbes | Some species show weak links between codon optimality and translation output despite clear codon bias. | Soman et al.: TAc and tRNA-demand–based optimality “did not show any correlation with mRNA abundance and translation efficiency”; no correlation with ribosome pausing either. (soman2023codonoptimalityhas pages 1-2) | 10.1038/s41598-022-27164-0 https://doi.org/10.1038/s41598-022-27164-0 | 01/2023 | Important warning edge; taxon-specific (slow-growing, high-GC Mtb). Mark uncertain/generalization-limited. |
| strong 5′ mRNA secondary structure → inhibits → translation initiation | Start-region RNA folding can limit ribosome access and dominate expression effects of synonymous codons. | Plotkin & Kudla: 5′ structure “generally disadvantageous”; GFP expression in E. coli is strongly inhibited when 5′ folding energy is below about -10 kcal/mol. Figure summary shows RBS/SD/start-codon occlusion effect. (plotkin2011synonymousbutnot pages 4-5, plotkin2011synonymousbutnot pages 6-7, plotkin2011synonymousbutnot media 4022dfe4) | 10.1038/nrg2899 https://doi.org/10.1038/nrg2899 | 11/2011 | Strong mechanistic edge; especially relevant for gene-level/local codon patterns rather than whole-genome trait alone. |
| synonymous codons in first ~8 codons / 5′ CDS → strongly influence → protein production | Early coding sequence affects local structure and initiation-proximal translation efficiency. | Nieuwkoop et al.: 1,459 E. coli mRFP variants; Random Forest prediction r = 0.762; codons 2–8 / first eight codons carry most predictive signal; fluorescence-proteomics correlation r = 0.901. (nieuwkoop2023revealingdeterminantsof pages 1-2, nieuwkoop2023revealingdeterminantsof pages 1-1, nieuwkoop2023revealingdeterminantsof pages 7-8, nieuwkoop2023revealingdeterminantsof pages 9-10, nieuwkoop2023revealingdeterminantsof pages 12-13, nieuwkoop2023revealingdeterminantsof pages 6-7) | 10.1093/nar/gkad035 https://doi.org/10.1093/nar/gkad035 | 01/2023 | Strong for expression engineering and local codon effects; not evidence that global CAI is primary driver. |
| reduced 5′ mRNA structure (A/T-rich early codons) → increases → protein production | A/T-rich synonymous choices weaken local pairing and improve initiation-region accessibility. | Nieuwkoop et al.: A/T, especially A, in the 5′ coding region is positively correlated with production, while G/C is negative; sequence/BPP models show strongest features around start codon and RBS. (nieuwkoop2023revealingdeterminantsof pages 8-9, nieuwkoop2023revealingdeterminantsof pages 9-10, nieuwkoop2023revealingdeterminantsof pages 12-13) | 10.1093/nar/gkad035 https://doi.org/10.1093/nar/gkad035 | 01/2023 | Strong for construct-level behavior in E. coli; likely gene-context dependent. |
| tRNA anticodon-loop modifications → alter → codon–anticodon decoding efficiency | Wobble/anticodon chemistry changes pairing, selectivity, and translation speed/fidelity. | Mitchener et al.: ASL positions 34/37 are modification hotspots; modifications stabilize codon–anticodon interactions and “promote translational fidelity.” Delgado et al. cite cmo5U/inosine as altering affinities and selectivity. (mitchener2023molecularcopingmechanisms pages 2-4, delgado2024impactofthe pages 7-8) | 10.1021/acs.accounts.3c00572 https://doi.org/10.1021/acs.accounts.3c00572; 10.3389/fmicb.2024.1412318 https://doi.org/10.3389/fmicb.2024.1412318 | 11/2023; 08/2024 | Strong molecular mechanism; exact codon targets depend on modification and tRNA species. |
| cellular stress → reprograms → tRNA modification landscape | Stress-responsive tRNA chemistry provides a rapid route to change decoding of codon-biased transcripts. | Mitchener et al.: each tRNA carries ~8–10 modifications that “undergo unique reprogramming in response to cellular stresses”; LC-MS/MS and sequencing capture dynamic changes. H2O2 increases m5C; S-phase increases Trm9-mediated mcm5U. (mitchener2023molecularcopingmechanisms pages 1-2, mitchener2023molecularcopingmechanisms pages 5-6) | 10.1021/acs.accounts.3c00572 https://doi.org/10.1021/acs.accounts.3c00572 | 11/2023 | Strong; stress type and organism matter. |
| Trm9-dependent wobble U modifications (mcm5U/mcm5s2U) → promote translation of → AGA/GAA-enriched transcripts | Specific tRNA-modifying enzymes create codon-specific translational programs. | Mitchener et al.: loss of Trm9 lowers methylation ~4-fold and causes ~6–7-fold reduced translation of AGA/GAA-enriched reporters; 425 genes overuse AGA/GAA; codon-optimized RNR1 rescues phenotype. (mitchener2023molecularcopingmechanisms pages 4-5, mitchener2023molecularcopingmechanisms pages 5-6) | 10.1021/acs.accounts.3c00572 https://doi.org/10.1021/acs.accounts.3c00572 | 11/2023 | Strong mechanistic edge, but mostly from yeast/eukaryotic model systems; curate cautiously for microbes unless supported in bacteria. |
| Trm4-dependent m5C wobble modification → promotes translation of → UUG-run stress-response reporter | Modification-dependent decoding can control stress survival through codon-biased translation. | Mitchener et al.: in trm4Δ, UUG-run reporter activity drops ~10-fold under oxidative stress context; trm4 loss causes H2O2 hypersensitivity. (mitchener2023molecularcopingmechanisms pages 5-6) | 10.1021/acs.accounts.3c00572 https://doi.org/10.1021/acs.accounts.3c00572 | 11/2023 | Mechanistically strong but mainly non-bacterial example; mark limited-transferability. |
| H2O2 stress → increases trmB / m7G46 → enhances translation of → Phe/Asp-rich catalases | Bacterial tRNA core modifications can connect oxidative stress to protein output. | Yared et al.: in Pseudomonas aeruginosa, H2O2 increases trmB transcription and m7G46; trmB loss reduces efficient translation of Phe/Asp codons and lowers KatA/KatB catalase production, causing H2O2 sensitivity. (yared2024beyondtheanticodon pages 11-12) | 10.3390/genes15030374 https://doi.org/10.3390/genes15030374 | 03/2024 | Strong bacterial example linking stress, tRNA modification, decoding, and phenotype. |
| UV stress via s4U8 crosslinking → causes → uncharged tRNA accumulation and stringent response | Some tRNA modifications mediate environmental sensing that changes translation state. | Yared et al.: UV-induced s4U8:C13 crosslinks reduce charging, causing ribosome stalling, ppGpp production, and stringent response. (yared2024beyondtheanticodon pages 11-12) | 10.3390/genes15030374 https://doi.org/10.3390/genes15030374 | 03/2024 | Strong for stress-response mechanism; indirect relation to genome-wide codon bias, so curate as peripheral if needed. |
| tRNA anticodon-loop modification genes (tilS, tsaB, gluQ, tgt, tusE/mnmA) → correlate with → proteobacterial codon usage patterns | Comparative genomics suggests modification capacity constrains allowable codon-frequency space. | Delgado et al.: ~1,484 Proteobacteria analyzed; strongest associations with tilS, tsaB, gluQ (P < 1e-10); >25 more modification genes show weaker but significant GC% associations. (delgado2024impactofthe pages 1-2, delgado2024impactofthe pages 2-4, delgado2024impactofthe pages 4-6, delgado2024impactofthe pages 6-7) | 10.3389/fmicb.2024.1412318 https://doi.org/10.3389/fmicb.2024.1412318 | 08/2024 | Valuable broad comparative edge; primarily correlational/bioinformatic and should be marked uncertain until experimental validation. |
| presence of tsaB / gluQ → associates with → higher genomic GC% and codon-frequency shifts | Modification systems may bias which codons change during GC-content evolution. | Delgado et al.: genomes lacking both tsaB and gluQ tend to have lower GC%; presence of tsaB or gluQ associates with higher GC%; low-variability codons include AAC, CGA, AGG, GGA. (delgado2024impactofthe pages 6-7, delgado2024impactofthe pages 1-2) | 10.3389/fmicb.2024.1412318 https://doi.org/10.3389/fmicb.2024.1412318 | 08/2024 | Correlative and potentially confounded by genome reduction; mark uncertain for causal graph. |
| low-GC proteobacterial genomes (<~40% GC) → tend to lack → certain tRNA modification genes | Loss of modification systems covaries with genome composition and may constrain codon repertoire. | Delgado et al.: genomes below ~40% GC “tend to lack” genes such as GluQRS and TsaB; codon variability patterns track presence of modification enzymes. (delgado2024impactofthe pages 7-8) | 10.3389/fmicb.2024.1412318 https://doi.org/10.3389/fmicb.2024.1412318 | 08/2024 | Comparative association only; direction of causality unresolved. |
| thermophilic growth/temperature adaptation → increases → stability-associated tRNA modifications | Thermal niche can tune tRNA chemistry, potentially affecting codon decoding and translation robustness. | Hoffmann et al.: in G. stearothermophilus, modified-tRNA counts rise with temperature; examples D17 1→12→13, D20 6→18→19, Ψ55 9→21→29 across 40/55/70°C; s4U8 occurrences >24 vs ≤4 in non-thermophiles. (hoffmann2024temperaturedependenttrnamodifications pages 17-19, hoffmann2024temperaturedependenttrnamodifications pages 13-14, hoffmann2024temperaturedependenttrnamodifications pages 9-10) | 10.3390/ijms25168823 https://doi.org/10.3390/ijms25168823 | 08/2024 | Strong for temperature→modification edge; direct codon-bias consequences are plausible but not directly tested. |
| psychrophilic/mesophilic thermal niche → increases → dihydrouridine (D) abundance | Dihydrouridine increases local tRNA flexibility, supporting cold adaptation. | Hoffmann et al.: psychrophilic/mesophilic bacteria show higher D levels; interpreted as enhancing local tRNA flexibility in cold environments. (hoffmann2024temperaturedependenttrnamodifications pages 1-2, hoffmann2024temperaturedependenttrnamodifications pages 17-19, hoffmann2024temperaturedependenttrnamodifications pages 19-20) | 10.3390/ijms25168823 https://doi.org/10.3390/ijms25168823 | 08/2024 | Strong for temperature adaptation; indirect for codon-bias trait curation. |
| start codon / stop codon identity and +4 nucleotide → influences → translation efficiency/termination fidelity | Translation machinery optimization includes codon choices beyond synonymous sense codons. | Farookhi & Xia: initiation depends on AUG, SD/aSD, and local structure; termination readthrough frequencies are UGA 10^-3–10^-2 > UAG 1.1×10^-4–7×10^-3 > UAA 9×10^-4 to <1×10^-5. (farookhi2024differentialselectionfor pages 1-2) | 10.3390/microorganisms12040768 https://doi.org/10.3390/microorganisms12040768 | 04/2024 | Useful neighboring mechanism, but stop/start codons are outside strict synonymous-codon-bias scope. |
| horizontal gene transfer / replication-strand nucleotide bias → can contribute to → codon-usage variation | Non-translational processes can create codon-usage structure within genomes. | Plotkin & Kudla note systematic codon-usage variation can also result from “horizontal gene transfer” and “different nucleotide bias in leading and lagging strands of replication in bacteria.” (plotkin2011synonymousbutnot pages 4-5) | 10.1038/nrg2899 https://doi.org/10.1038/nrg2899 | 11/2011 | Important boundary-case warning: these drivers affect codon frequencies but may not reflect translational adaptation. |
| codon-bias metrics (RSCU, ENC, CAI, FOP, tAI, ENcp, etc.) → quantify → codon usage bias for prediction/engineering | Operationalization of the trait requires metrics rather than a single molecular entity. | Plotkin & Kudla define RSCU (0 absent, 1 unbiased, up to 6 in sixfold families) and list CAI/FOP/tAI. GenRCA implements 31 indices + 2 motif metrics across 65 hosts for codon optimization/expression assessment. (plotkin2011synonymousbutnot pages 2-3, fan2024genrcaauserfriendly pages 3-5, fan2024genrcaauserfriendly pages 1-3, fan2024genrcaauserfriendly pages 8-9) | 10.1038/nrg2899 https://doi.org/10.1038/nrg2899; 10.1186/s12859-024-05934-z https://doi.org/10.1186/s12859-024-05934-z | 11/2011; 09/2024 | Curate as assay/measurement support, not as causal biology. |
| multi-index codon-bias analysis → supports → host-specific codon optimization and expression prediction | Real-world implementation uses codon-bias indices to design heterologous genes. | GenRCA: 31 indices, 65 expression hosts, batch processing; intended for evaluating whether codon optimization is needed and for ML/regression prediction of expression. (fan2024genrcaauserfriendly pages 5-8, fan2024genrcaauserfriendly pages 3-5, fan2024genrcaauserfriendly pages 1-3) | 10.1186/s12859-024-05934-z https://doi.org/10.1186/s12859-024-05934-z | 09/2024 | Application edge rather than intrinsic microbial mechanism; keep separate from core causal graph if needed. |


*Table: This table compiles candidate subject-predicate-object edges for curating a microbial codon usage bias causal graph. It emphasizes evidence-backed mechanisms, quantitative findings, and flags edges that are broad, taxon-specific, or mainly correlational.*

### Warnings / claims not yet ready for confident TraitMech curation
1. **Proteobacteria tRNA-modification gene ↔ codon usage/GC% associations** are powerful and genome-wide but largely **correlational** and potentially confounded by genome reduction and phylogeny; curate edges as *uncertain* unless supported by experimental perturbations in representative taxa. (delgado2024impactofthe pages 7-8, delgado2024impactofthe pages 6-7)
2. **Stress → tRNA modification reprogramming → codon-biased translation** is strongly supported mechanistically, but some of the clearest quantitative examples in Mitchener et al. are from **yeast/human** systems; curate bacterial/general microbial edges using bacterial examples (e.g., Pseudomonas trmB/m7G46) as higher-confidence anchors. (mitchener2023molecularcopingmechanisms pages 4-5, yared2024beyondtheanticodon pages 11-12)
3. **Codon optimality → translation efficiency** is not universal: in **M. tuberculosis**, codon optimality measures did not correlate with translation efficiency, implying that “codon bias implies higher translation efficiency” should be curated as context-dependent rather than universal. (soman2023codonoptimalityhas pages 1-2)
4. **Start/stop codon features and readthrough** affect translation efficiency but are adjacent traits rather than synonymous codon-usage bias per se; include as boundary nodes only if the graph explicitly models translation machinery optimization more broadly. (farookhi2024differentialselectionfor pages 1-2)

---

## DOI-first bibliography (with URLs; publication dates)

1. Plotkin JB, Kudla G. *Synonymous but not the same: the causes and consequences of codon bias.* **Nature Reviews Genetics** 12:32–42 (Jan 2011 online; issue Jan 2011; retrieved pages list Nov 2011). DOI: **10.1038/nrg2899**. URL: https://doi.org/10.1038/nrg2899 (plotkin2011synonymousbutnot pages 2-3, plotkin2011synonymousbutnot pages 4-5, plotkin2011synonymousbutnot pages 6-7, plotkin2011synonymousbutnot media 4022dfe4)
2. Hershberg R, Petrov DA. *Selection on Codon Bias.* **Annual Review of Genetics** 42:287–299 (Dec 2008). DOI: **10.1146/annurev.genet.42.110807.091442**. URL: https://doi.org/10.1146/annurev.genet.42.110807.091442 (hershberg2008selectiononcodon pages 2-3)
3. Johnson MM, Hockenberry AJ, McGuffie MJ, Vieira LC, Wilke CO. *Growth-dependent Gene Expression Variation Influences the Strength of Codon Usage Biases.* **Molecular Biology and Evolution** (Mar 2023). DOI: **10.1093/molbev/msad189**. URL: https://doi.org/10.1093/molbev/msad189 (johnson2023growthdependentgeneexpression pages 6-8, johnson2023growthdependentgeneexpression pages 13-15)
4. Nieuwkoop T, Terlouw BR, Stevens KG, et al. *Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning.* **Nucleic Acids Research** 51:2363–2376 (Jan 2023). DOI: **10.1093/nar/gkad035**. URL: https://doi.org/10.1093/nar/gkad035 (nieuwkoop2023revealingdeterminantsof pages 1-1, nieuwkoop2023revealingdeterminantsof pages 7-8, nieuwkoop2023revealingdeterminantsof pages 8-9)
5. Soman S, Chattopadhyay S, Ram S, Nandicoori VK, Arimbasseri GA. *Codon optimality has minimal effect on determining translation efficiency in mycobacterium tuberculosis.* **Scientific Reports** 13 (Jan 2023). DOI: **10.1038/s41598-022-27164-0**. URL: https://doi.org/10.1038/s41598-022-27164-0 (soman2023codonoptimalityhas pages 1-2)
6. Farookhi H, Xia X. *Differential Selection for Translation Efficiency Shapes Translation Machineries in Bacterial Species.* **Microorganisms** 12:768 (Apr 2024). DOI: **10.3390/microorganisms12040768**. URL: https://doi.org/10.3390/microorganisms12040768 (farookhi2024differentialselectionfor pages 1-2)
7. Mitchener MM, Begley TJ, Dedon PC. *Molecular coping mechanisms: reprogramming tRNAs to regulate codon-biased translation of stress response proteins.* **Accounts of Chemical Research** 56:3504–3514 (Nov 2023). DOI: **10.1021/acs.accounts.3c00572**. URL: https://doi.org/10.1021/acs.accounts.3c00572 (mitchener2023molecularcopingmechanisms pages 1-2, mitchener2023molecularcopingmechanisms pages 4-5, mitchener2023molecularcopingmechanisms pages 5-6)
8. Yared M-J, Marcelot A, Barraud P. *Beyond the Anticodon: tRNA Core Modifications and Their Impact on Structure, Translation and Stress Adaptation.* **Genes** 15:374 (Mar 2024). DOI: **10.3390/genes15030374**. URL: https://doi.org/10.3390/genes15030374 (yared2024beyondtheanticodon pages 11-12, yared2024beyondtheanticodon pages 8-10)
9. Delgado S, Armijo Á, Bravo V, et al. *Impact of the chemical modification of tRNAs anticodon loop on the variability and evolution of codon usage in proteobacteria.* **Frontiers in Microbiology** 15 (Aug 2024). DOI: **10.3389/fmicb.2024.1412318**. URL: https://doi.org/10.3389/fmicb.2024.1412318 (delgado2024impactofthe pages 2-4, delgado2024impactofthe pages 7-8, delgado2024impactofthe pages 6-7)
10. Hoffmann A, Lorenz C, Fallmann J, et al. *Temperature-Dependent tRNA Modifications in Bacillales.* **International Journal of Molecular Sciences** 25 (Aug 2024). DOI: **10.3390/ijms25168823**. URL: https://doi.org/10.3390/ijms25168823 (hoffmann2024temperaturedependenttrnamodifications pages 1-2, hoffmann2024temperaturedependenttrnamodifications pages 9-10)
11. Fan K, Li Y, Chen Z, Fan L. *GenRCA: a user-friendly rare codon analysis tool for comprehensive evaluation of codon usage preferences based on coding sequences in genomes.* **BMC Bioinformatics** (Sep 2024). DOI: **10.1186/s12859-024-05934-z**. URL: https://doi.org/10.1186/s12859-024-05934-z (fan2024genrcaauserfriendly pages 1-3, fan2024genrcaauserfriendly pages 3-5, fan2024genrcaauserfriendly pages 5-8)
12. Cope A, Shah P, Wallace E. *Evolutionary principles underpinning codon usage bias: patterns, functions, and mechanisms.* (May 2024; preprint/archival DOI). DOI: **10.32942/x2802v**. URL: https://doi.org/10.32942/x2802v (cope2024evolutionaryprinciplesunderpinning pages 8-11, cope2024evolutionaryprinciplesunderpinning pages 11-14)


References

1. (plotkin2011synonymousbutnot pages 2-3): Joshua B. Plotkin and Grzegorz Kudla. Synonymous but not the same: the causes and consequences of codon bias. Nature Reviews Genetics, 12:32-42, Nov 2011. URL: https://doi.org/10.1038/nrg2899, doi:10.1038/nrg2899. This article has 2075 citations and is from a domain leading peer-reviewed journal.

2. (plotkin2011synonymousbutnot pages 4-5): Joshua B. Plotkin and Grzegorz Kudla. Synonymous but not the same: the causes and consequences of codon bias. Nature Reviews Genetics, 12:32-42, Nov 2011. URL: https://doi.org/10.1038/nrg2899, doi:10.1038/nrg2899. This article has 2075 citations and is from a domain leading peer-reviewed journal.

3. (plotkin2011synonymousbutnot pages 6-7): Joshua B. Plotkin and Grzegorz Kudla. Synonymous but not the same: the causes and consequences of codon bias. Nature Reviews Genetics, 12:32-42, Nov 2011. URL: https://doi.org/10.1038/nrg2899, doi:10.1038/nrg2899. This article has 2075 citations and is from a domain leading peer-reviewed journal.

4. (nieuwkoop2023revealingdeterminantsof pages 1-1): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

5. (farookhi2024differentialselectionfor pages 1-2): Heba Farookhi and Xuhua Xia. Differential selection for translation efficiency shapes translation machineries in bacterial species. Microorganisms, 12:768, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040768, doi:10.3390/microorganisms12040768. This article has 4 citations.

6. (cope2024evolutionaryprinciplesunderpinning pages 11-14): Alexander Cope, Premal Shah, Premal Shah, and Edward Wallace. Evolutionary principles underpinning codon usage bias: patterns, functions, and mechanisms. Unknown journal, May 2024. URL: https://doi.org/10.32942/x2802v, doi:10.32942/x2802v.

7. (fan2024genrcaauserfriendly pages 3-5): Kunjie Fan, Yuanyuan Li, Zhiwei Chen, and Long Fan. Genrca: a user-friendly rare codon analysis tool for comprehensive evaluation of codon usage preferences based on coding sequences in genomes. BMC Bioinformatics, Sep 2024. URL: https://doi.org/10.1186/s12859-024-05934-z, doi:10.1186/s12859-024-05934-z. This article has 20 citations and is from a peer-reviewed journal.

8. (johnson2023growthdependentgeneexpression pages 13-15): Mackenzie M. Johnson, Adam J. Hockenberry, Matthew J. McGuffie, Luiz Carlos Vieira, and Claus O. Wilke. Growth-dependent gene expression variation influences the strength of codon usage biases. Molecular Biology and Evolution, Mar 2023. URL: https://doi.org/10.1093/molbev/msad189, doi:10.1093/molbev/msad189. This article has 4 citations and is from a highest quality peer-reviewed journal.

9. (farookhi2024differentialselectionfor pages 19-21): Heba Farookhi and Xuhua Xia. Differential selection for translation efficiency shapes translation machineries in bacterial species. Microorganisms, 12:768, Apr 2024. URL: https://doi.org/10.3390/microorganisms12040768, doi:10.3390/microorganisms12040768. This article has 4 citations.

10. (hershberg2008selectiononcodon pages 2-3): Ruth Hershberg and Dmitri A. Petrov. Selection on codon bias. Dec 2008. URL: https://doi.org/10.1146/annurev.genet.42.110807.091442, doi:10.1146/annurev.genet.42.110807.091442. This article has 1296 citations and is from a domain leading peer-reviewed journal.

11. (johnson2023growthdependentgeneexpression pages 6-8): Mackenzie M. Johnson, Adam J. Hockenberry, Matthew J. McGuffie, Luiz Carlos Vieira, and Claus O. Wilke. Growth-dependent gene expression variation influences the strength of codon usage biases. Molecular Biology and Evolution, Mar 2023. URL: https://doi.org/10.1093/molbev/msad189, doi:10.1093/molbev/msad189. This article has 4 citations and is from a highest quality peer-reviewed journal.

12. (nieuwkoop2023revealingdeterminantsof pages 7-8): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

13. (nieuwkoop2023revealingdeterminantsof pages 8-9): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

14. (nieuwkoop2023revealingdeterminantsof pages 1-2): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

15. (nieuwkoop2023revealingdeterminantsof pages 12-13): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

16. (mitchener2023molecularcopingmechanisms pages 1-2): Michelle M. Mitchener, Thomas J. Begley, and Peter C. Dedon. Molecular coping mechanisms: reprogramming trnas to regulate codon-biased translation of stress response proteins. Accounts of Chemical Research, 56:3504-3514, Nov 2023. URL: https://doi.org/10.1021/acs.accounts.3c00572, doi:10.1021/acs.accounts.3c00572. This article has 31 citations and is from a domain leading peer-reviewed journal.

17. (mitchener2023molecularcopingmechanisms pages 4-5): Michelle M. Mitchener, Thomas J. Begley, and Peter C. Dedon. Molecular coping mechanisms: reprogramming trnas to regulate codon-biased translation of stress response proteins. Accounts of Chemical Research, 56:3504-3514, Nov 2023. URL: https://doi.org/10.1021/acs.accounts.3c00572, doi:10.1021/acs.accounts.3c00572. This article has 31 citations and is from a domain leading peer-reviewed journal.

18. (yared2024beyondtheanticodon pages 11-12): Marcel-Joseph Yared, Agathe Marcelot, and Pierre Barraud. Beyond the anticodon: trna core modifications and their impact on structure, translation and stress adaptation. Genes, 15:374, Mar 2024. URL: https://doi.org/10.3390/genes15030374, doi:10.3390/genes15030374. This article has 54 citations.

19. (delgado2024impactofthe pages 2-4): Sebastián Delgado, Álvaro Armijo, Verónica Bravo, Omar Orellana, Juan Carlos Salazar, and Assaf Katz. Impact of the chemical modification of trnas anticodon loop on the variability and evolution of codon usage in proteobacteria. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1412318, doi:10.3389/fmicb.2024.1412318. This article has 2 citations and is from a peer-reviewed journal.

20. (delgado2024impactofthe pages 7-8): Sebastián Delgado, Álvaro Armijo, Verónica Bravo, Omar Orellana, Juan Carlos Salazar, and Assaf Katz. Impact of the chemical modification of trnas anticodon loop on the variability and evolution of codon usage in proteobacteria. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1412318, doi:10.3389/fmicb.2024.1412318. This article has 2 citations and is from a peer-reviewed journal.

21. (delgado2024impactofthe pages 6-7): Sebastián Delgado, Álvaro Armijo, Verónica Bravo, Omar Orellana, Juan Carlos Salazar, and Assaf Katz. Impact of the chemical modification of trnas anticodon loop on the variability and evolution of codon usage in proteobacteria. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1412318, doi:10.3389/fmicb.2024.1412318. This article has 2 citations and is from a peer-reviewed journal.

22. (hoffmann2024temperaturedependenttrnamodifications pages 9-10): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

23. (hoffmann2024temperaturedependenttrnamodifications pages 1-2): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

24. (hoffmann2024temperaturedependenttrnamodifications pages 17-19): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

25. (fan2024genrcaauserfriendly pages 1-3): Kunjie Fan, Yuanyuan Li, Zhiwei Chen, and Long Fan. Genrca: a user-friendly rare codon analysis tool for comprehensive evaluation of codon usage preferences based on coding sequences in genomes. BMC Bioinformatics, Sep 2024. URL: https://doi.org/10.1186/s12859-024-05934-z, doi:10.1186/s12859-024-05934-z. This article has 20 citations and is from a peer-reviewed journal.

26. (fan2024genrcaauserfriendly pages 5-8): Kunjie Fan, Yuanyuan Li, Zhiwei Chen, and Long Fan. Genrca: a user-friendly rare codon analysis tool for comprehensive evaluation of codon usage preferences based on coding sequences in genomes. BMC Bioinformatics, Sep 2024. URL: https://doi.org/10.1186/s12859-024-05934-z, doi:10.1186/s12859-024-05934-z. This article has 20 citations and is from a peer-reviewed journal.

27. (cope2024evolutionaryprinciplesunderpinning pages 8-11): Alexander Cope, Premal Shah, Premal Shah, and Edward Wallace. Evolutionary principles underpinning codon usage bias: patterns, functions, and mechanisms. Unknown journal, May 2024. URL: https://doi.org/10.32942/x2802v, doi:10.32942/x2802v.

28. (plotkin2011synonymousbutnot media 4022dfe4): Joshua B. Plotkin and Grzegorz Kudla. Synonymous but not the same: the causes and consequences of codon bias. Nature Reviews Genetics, 12:32-42, Nov 2011. URL: https://doi.org/10.1038/nrg2899, doi:10.1038/nrg2899. This article has 2075 citations and is from a domain leading peer-reviewed journal.

29. (soman2023codonoptimalityhas pages 1-2): Smitha Soman, Somdeb Chattopadhyay, Siya Ram, Vinay Kumar Nandicoori, and G. Aneeshkumar Arimbasseri. Codon optimality has minimal effect on determining translation efficiency in mycobacterium tuberculosis. Scientific Reports, Jan 2023. URL: https://doi.org/10.1038/s41598-022-27164-0, doi:10.1038/s41598-022-27164-0. This article has 4 citations and is from a peer-reviewed journal.

30. (delgado2024impactofthe pages 1-2): Sebastián Delgado, Álvaro Armijo, Verónica Bravo, Omar Orellana, Juan Carlos Salazar, and Assaf Katz. Impact of the chemical modification of trnas anticodon loop on the variability and evolution of codon usage in proteobacteria. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1412318, doi:10.3389/fmicb.2024.1412318. This article has 2 citations and is from a peer-reviewed journal.

31. (johnson2023growthdependentgeneexpression pages 8-10): Mackenzie M. Johnson, Adam J. Hockenberry, Matthew J. McGuffie, Luiz Carlos Vieira, and Claus O. Wilke. Growth-dependent gene expression variation influences the strength of codon usage biases. Molecular Biology and Evolution, Mar 2023. URL: https://doi.org/10.1093/molbev/msad189, doi:10.1093/molbev/msad189. This article has 4 citations and is from a highest quality peer-reviewed journal.

32. (mitchener2023molecularcopingmechanisms pages 2-4): Michelle M. Mitchener, Thomas J. Begley, and Peter C. Dedon. Molecular coping mechanisms: reprogramming trnas to regulate codon-biased translation of stress response proteins. Accounts of Chemical Research, 56:3504-3514, Nov 2023. URL: https://doi.org/10.1021/acs.accounts.3c00572, doi:10.1021/acs.accounts.3c00572. This article has 31 citations and is from a domain leading peer-reviewed journal.

33. (mitchener2023molecularcopingmechanisms pages 5-6): Michelle M. Mitchener, Thomas J. Begley, and Peter C. Dedon. Molecular coping mechanisms: reprogramming trnas to regulate codon-biased translation of stress response proteins. Accounts of Chemical Research, 56:3504-3514, Nov 2023. URL: https://doi.org/10.1021/acs.accounts.3c00572, doi:10.1021/acs.accounts.3c00572. This article has 31 citations and is from a domain leading peer-reviewed journal.

34. (yared2024beyondtheanticodon pages 8-10): Marcel-Joseph Yared, Agathe Marcelot, and Pierre Barraud. Beyond the anticodon: trna core modifications and their impact on structure, translation and stress adaptation. Genes, 15:374, Mar 2024. URL: https://doi.org/10.3390/genes15030374, doi:10.3390/genes15030374. This article has 54 citations.

35. (hoffmann2024temperaturedependenttrnamodifications pages 6-9): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

36. (hoffmann2024temperaturedependenttrnamodifications pages 13-14): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

37. (hoffmann2024temperaturedependenttrnamodifications pages 19-20): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

38. (mitchener2023molecularcopingmechanisms pages 7-8): Michelle M. Mitchener, Thomas J. Begley, and Peter C. Dedon. Molecular coping mechanisms: reprogramming trnas to regulate codon-biased translation of stress response proteins. Accounts of Chemical Research, 56:3504-3514, Nov 2023. URL: https://doi.org/10.1021/acs.accounts.3c00572, doi:10.1021/acs.accounts.3c00572. This article has 31 citations and is from a domain leading peer-reviewed journal.

39. (johnson2023growthdependentgeneexpression pages 1-3): Mackenzie M. Johnson, Adam J. Hockenberry, Matthew J. McGuffie, Luiz Carlos Vieira, and Claus O. Wilke. Growth-dependent gene expression variation influences the strength of codon usage biases. Molecular Biology and Evolution, Mar 2023. URL: https://doi.org/10.1093/molbev/msad189, doi:10.1093/molbev/msad189. This article has 4 citations and is from a highest quality peer-reviewed journal.

40. (johnson2023growthdependentgeneexpression pages 10-11): Mackenzie M. Johnson, Adam J. Hockenberry, Matthew J. McGuffie, Luiz Carlos Vieira, and Claus O. Wilke. Growth-dependent gene expression variation influences the strength of codon usage biases. Molecular Biology and Evolution, Mar 2023. URL: https://doi.org/10.1093/molbev/msad189, doi:10.1093/molbev/msad189. This article has 4 citations and is from a highest quality peer-reviewed journal.

41. (nieuwkoop2023revealingdeterminantsof pages 6-7): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

42. (delgado2024impactofthe pages 4-6): Sebastián Delgado, Álvaro Armijo, Verónica Bravo, Omar Orellana, Juan Carlos Salazar, and Assaf Katz. Impact of the chemical modification of trnas anticodon loop on the variability and evolution of codon usage in proteobacteria. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1412318, doi:10.3389/fmicb.2024.1412318. This article has 2 citations and is from a peer-reviewed journal.

43. (hoffmann2024temperaturedependenttrnamodifications pages 10-11): Anne Hoffmann, Christian Lorenz, Jörg Fallmann, Philippe Wolff, Antony Lechner, Heike Betat, Mario Mörl, and Peter Florian Stadler. Temperature-dependent trna modifications in bacillales. International Journal of Molecular Sciences, Aug 2024. URL: https://doi.org/10.3390/ijms25168823, doi:10.3390/ijms25168823. This article has 6 citations.

44. (nieuwkoop2023revealingdeterminantsof pages 9-10): Thijs Nieuwkoop, Barbara R Terlouw, Katherine G Stevens, Richard A Scheltema, Dick de Ridder, John van der Oost, and Nico J Claassens. Revealing determinants of translation efficiency via whole-gene codon randomization and machine learning. Nucleic Acids Research, 51:2363-2376, Jan 2023. URL: https://doi.org/10.1093/nar/gkad035, doi:10.1093/nar/gkad035. This article has 74 citations and is from a highest quality peer-reviewed journal.

45. (fan2024genrcaauserfriendly pages 8-9): Kunjie Fan, Yuanyuan Li, Zhiwei Chen, and Long Fan. Genrca: a user-friendly rare codon analysis tool for comprehensive evaluation of codon usage preferences based on coding sequences in genomes. BMC Bioinformatics, Sep 2024. URL: https://doi.org/10.1186/s12859-024-05934-z, doi:10.1186/s12859-024-05934-z. This article has 20 citations and is from a peer-reviewed journal.