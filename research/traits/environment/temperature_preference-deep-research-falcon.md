---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:17:17.955457'
end_time: '2026-06-18T02:31:14.271733'
duration_seconds: 836.32
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature preference
  trait_identifier: METPO:1000613
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that describes characteristic growth with respect to environmental
    temperature.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.culture temp.temperature, range_tmp
  evidence_summary: 'DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports
    temperature-dependent microbial growth-rate phenotypes.)'
  causal_graph_summary: 'temperature_preference_growth_physiology: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature preference
- **METPO identifier:** METPO:1000613
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes characteristic growth with respect to environmental temperature.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.culture temp.temperature, range_tmp
- **Existing evidence:** DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports temperature-dependent microbial growth-rate phenotypes.)
- **Existing causal graph summary:** temperature_preference_growth_physiology: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **temperature preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_preference.yaml`.

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
- **Trait label:** temperature preference
- **METPO identifier:** METPO:1000613
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes characteristic growth with respect to environmental temperature.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.culture temp.temperature, range_tmp
- **Existing evidence:** DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports temperature-dependent microbial growth-rate phenotypes.)
- **Existing causal graph summary:** temperature_preference_growth_physiology: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **temperature preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_preference.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Temperature Preference (METPO:1000613)

## 1) Scope summary (trait definition and boundaries)

**Trait label:** temperature preference (METPO:1000613) — “a phenotype that describes characteristic growth with respect to environmental temperature.”

**Operational definition for curation:** temperature preference is best treated as a **growth phenotype** captured by a growth–temperature relationship (e.g., minimum growth temperature, maximum growth temperature, and optimal growth temperature *Topt*). A recent cold-adaptation review provides commonly used category boundaries: **psychrophiles** grow at ~0 °C with optima around ~15 °C (and do not grow at ~20 °C), **psychrotolerants** grow at ~4 °C with optima >20 °C, while **mesophiles** have optima around ~20–45 °C. (ramon2023ageneraloverview pages 1-2)

**Boundary cases / what not to conflate with temperature preference:**
- **Acute heat/cold shock responses** (stress regulons, transient survival programs) occur when temperature shifts away from the growth optimum; these are mechanistically relevant but not equivalent to “temperature preference.” (moon2023temperaturemattersbacterial pages 3-5)
- **Thermal tolerance/survival** (viability after exposure without growth) differs from preference (ability to *grow*) and should be curated separately if represented in METPO. (ramon2023ageneraloverview pages 1-2)

## 2) Key concepts and current understanding (mechanistic framing)

### 2.1 Temperature preference as an emergent property of coupled biophysical constraints
Across microbes, temperature preference is not a single pathway; it emerges from whether core cellular systems remain functional across temperatures, especially:
- **Membrane physical state (fluidity/viscosity)** and its regulation (“homeoviscous adaptation”). (ramon2023ageneraloverview pages 5-7, ramon2023ageneraloverview pages 2-4)
- **Protein folding/proteostasis capacity** (chaperones, heat-shock proteins, proteases). (moon2023temperaturemattersbacterial pages 3-5, li2024mechanismsunderlyingthe pages 10-12)
- **Nucleic-acid topology and stability** (DNA supercoiling; archaeal positive supercoiling via reverse gyrase in thermophiles). (villain2025regulationofdna pages 9-10, takemata2024howdothermophiles pages 1-2)
- **RNA structure and translation control** (RNA thermometers; cold-shock RNA chaperones). (moon2023temperaturemattersbacterial pages 3-5)
- **Compatible solutes/osmoprotection** (e.g., trehalose) that protect macromolecules and membranes at suboptimal temperatures. (moon2023temperaturemattersbacterial pages 3-5)

### 2.2 Temperature sensing and regulation: from physical signal to gene expression
Authoritative bacterial temperature-response synthesis emphasizes that temperature signals are transduced via **biophysical changes** (DNA supercoiling state, RNA secondary structure, membrane viscosity) into regulatory changes (sigma factors, sRNAs, two-component systems) that determine whether growth can proceed at a given temperature. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)

## 3) Candidate causal-graph nodes (curation-oriented)

Below are candidate nodes grouped by type; grounding is suggested where stable identifiers are standard. Label-only nodes are included where exact grounding is uncertain.

### 3.1 Environmental / experimental factors
- **Environmental temperature** (°C) (label-only; could map to an ENVO temperature condition if used)
- **Temperature downshift** / **temperature upshift** (label-only)
- **Growth medium** (e.g., LB-Lennox) (assay factor) (dessenne2024lipidomicanalysesreveal pages 12-13)
- **Aeration/agitation** (e.g., 180 rpm) (assay factor) (dessenne2024lipidomicanalysesreveal pages 12-13)
- **Co-stresses** (ethanol, acid stress in wine; oxidative stress at low temperature) (bellanger2024theroleof pages 1-2, li2024mechanismsunderlyingthe pages 7-9)

### 3.2 Membrane composition / lipid entities
- **Membrane fluidity** (label-only biophysical node)
- **Unsaturated fatty acids (UFA)** (CHEBI label-only; specific examples below)
- **Palmitoleic acid (C16:1)** (CHEBI candidate)
- **Oleic acid (C18:1)** (CHEBI candidate)
- **cis-vaccenic acid (18:1 Δ11)** (CHEBI candidate) (ramon2023ageneraloverview pages 4-5)
- **Phosphatidylethanolamine (PE)** (CHEBI candidate)
- **Phosphatidylglycerol (PG)** (CHEBI candidate)
- **Hopanoids / unsaturated hopanoids** (CHEBI/label-only) (ramon2023ageneraloverview pages 4-5)

### 3.3 Genes/proteins/complexes: membrane remodeling and sensing
- **DesK/DesR two-component system** (Bacillus model cold-sensing module) (UniProt/GO annotation candidates; gene labels acceptable) (ramon2023ageneraloverview pages 5-7)
- **des (fatty-acid desaturase)** (EC/UniProt candidate depending on organism) (ramon2023ageneraloverview pages 5-7)
- **FabF (β-ketoacyl-ACP synthase II)** (EC 2.3.1.179 candidate) (ramon2023ageneraloverview pages 4-5)
- **fabA / fabB / fabH** (fatty-acid synthesis/unsaturation pathway enzymes) (ramon2023ageneraloverview pages 2-4)
- **Desaturases (e.g., DesA/DesB in A. baumannii)** (label-only or UniProt by strain) (dessenne2024lipidomicanalysesreveal pages 8-12)

### 3.4 Genes/proteins: RNA thermosensing and cold-shock translation control
- **RNA thermometer (ROSE, FourU)** (label-only; maps to regulatory RNA element concept) (moon2023temperaturemattersbacterial pages 3-5)
- **CspA (cold-shock protein)** (UniProt candidate) (moon2023temperaturemattersbacterial pages 3-5)
- **CsdA (RNA helicase)** (UniProt candidate) (moon2023temperaturemattersbacterial pages 1-3)
- **RNase R** (UniProt candidate) (moon2023temperaturemattersbacterial pages 1-3)

### 3.5 Genes/proteins: global regulators and compatible-solute synthesis
- **RpoS (σS)** (UniProt candidate) (moon2023temperaturemattersbacterial pages 3-5)
- **ostAB operon** (label-only operon node) (moon2023temperaturemattersbacterial pages 3-5)
- **Trehalose** (CHEBI candidate) (moon2023temperaturemattersbacterial pages 3-5)

### 3.6 Genes/proteins: proteostasis and membrane-associated chaperones
- **DnaK/DnaJ/GrpE (Hsp70 system)** (GO: protein folding; UniProt candidates) (li2024mechanismsunderlyingthe pages 9-10)
- **GroEL/GroES (chaperonin system)** (UniProt candidates) (li2024mechanismsunderlyingthe pages 10-12)
- **ClpP (protease)** and **ClpXP** (complex) (li2024mechanismsunderlyingthe pages 10-12, moon2023temperaturemattersbacterial pages 3-5)
- **Lo18 (small heat shock protein; lipochaperone)** (Oenococcus-specific; UniProt candidate) (bellanger2024theroleof pages 1-2)

### 3.7 Genes/proteins: DNA topology / thermophile genome integrity
- **DNA gyrase** (EC 5.6.2.2) and **Topoisomerase I** (EC 5.6.2.1) (bacteria) (moon2023temperaturemattersbacterial pages 1-3)
- **Reverse gyrase / TopR1** (thermophiles; introduces positive supercoils) (label-only with TopR1 where known) (villain2025regulationofdna pages 9-10, takemata2024howdothermophiles pages 1-2)
- **Topo VI** (archaea) (label-only) (villain2025regulationofdna pages 10-12)
- **Histones / NAPs (e.g., Sso7)** (archaea) (villain2025regulationofdna pages 9-10)

### 3.8 Genes/proteins/metabolites: oxidative stress and DNA repair (cold-associated)
- **SOD (superoxide dismutase)** (EC 1.15.1.1)
- **DPS (DNA-binding ferritin-like protein)** (UniProt candidate)
- **RecA, LexA (SOS response)** and BER/MMR glycosylases (mutY, UDG, mug) (li2024mechanismsunderlyingthe pages 7-9)
- **Compatible solutes: betaine biosynthesis (betB)**; osmosensing channels **mscL** (li2024mechanismsunderlyingthe pages 10-12)

## 4) Recent developments and latest research emphasis (2023–2024)

### 4.1 2024 lipidomics: strain-specific homeoviscous adaptation in a clinically important pathogen
A 2024 *Microbiology Spectrum* study quantified temperature-dependent remodeling of *Acinetobacter baumannii* clinical strains at **18 °C vs 37 °C**, showing systematic increases in monounsaturated fatty acids in most strains at 18 °C (notably **C16:1 palmitoleic acid**; ABVal2 instead strongly increased **C18:1 oleic acid**). (dessenne2024lipidomicanalysesreveal pages 1-2)

It further reports that the **total unsaturated fatty-acid fraction at 18 °C was 60–80%** across strains, and that remodeling is concentrated in **PE and PG** pools. (dessenne2024lipidomicanalysesreveal pages 8-12)

Genomic context suggests a mechanistic basis: although *A. baumannii* often lacks **FabA**, FabA was found in some strains (ABVal2/ABVal3), and ABVal2 carried multiple candidate desaturases, providing candidate causal nodes for low-temperature membrane remodeling (not yet definitive without perturbations). (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)

### 4.2 2024 mechanistic cell biology: membrane-protective “lipochaperone” activity of a bacterial sHSP
A 2024 *Scientific Reports* paper provides quantitative evidence that Lo18 (from *Oenococcus oeni*) preferentially binds membranes containing **phosphatidylglycerol** and/or **oleic acid**, enabling its “lipochaperone” activity (membrane protection). (bellanger2024theroleof pages 1-2, bellanger2024theroleof pages 2-3)

In a biophysical assay, Lo18 improved membrane fluidity retention (anisotropy retention **52% → 68%** at **45 °C** in exponential-phase liposomes), linking a specific stress protein to membrane physical state at elevated temperature. (bellanger2024theroleof pages 3-4)

### 4.3 2024 transcriptomics + functional validation: multi-system low-temperature adaptation in *Rhodococcus*
A 2024 *Frontiers in Microbiology* study of *Rhodococcus* sp. RCBS9 compared growth at **10 °C vs 25 °C**, finding upregulation of heat-shock/proteostasis systems (GroEL/GroES, ClpP; HSPs/USPs), oxidative-stress defenses, and extensive DNA repair/SOS pathway genes at 10 °C. (li2024mechanismsunderlyingthe pages 10-12, li2024mechanismsunderlyingthe pages 7-9)

Notably, heterologous expression of selected RCBS9 proteins in *E. coli* BL21 improved growth at **10 °C** (e.g., BL21 expressing **DPS**, **GroEL**, or **USP-2** reached OD600 ~**1.4** vs ~**1.0–1.1** control at 4 h), supporting these proteins as transferable cold-adaptation effectors. (li2024mechanismsunderlyingthe pages 12-13)

### 4.4 2023 synthesis: integrated bacterial temperature-response logic (RNA, DNA topology, solutes)
A 2023 review provides key mechanistic “expert opinion” synthesis on how RNA thermometers, DNA supercoiling, sigma factors, and compatible solutes coordinate bacterial temperature responses. It also provides practical quantitative benchmarks (e.g., *E. coli* grows optimally at **37 °C**, poorly at **44 °C**, frail near **50 °C**, and shows minimal growth around **8 °C**). (moon2023temperaturemattersbacterial pages 1-3)

It reports quantitative RNA thermometer behavior: FourU melting at ~**42 °C** (without Mg2+) and ~**58 °C** (with Mg2+), supporting explicit temperature thresholds for translation control. (moon2023temperaturemattersbacterial pages 3-5)

## 5) Applications and real-world implementations

1. **Pathogen persistence and environmental fitness:** Temperature-dependent membrane remodeling in *A. baumannii* at 18 °C (environmental temperature) vs 37 °C (host temperature) provides actionable molecular targets (membrane lipid biosynthesis) for understanding environmental survival and transmission risk. (dessenne2024lipidomicanalysesreveal pages 12-13, dessenne2024lipidomicanalysesreveal pages 1-2)

2. **Industrial fermentation robustness (wine):** Lo18-mediated membrane protection is directly relevant to *O. oeni* performance in wine, where membrane fluidity is stressed by ethanol/acid and temperature; lipid composition dependence suggests controllable levers (process temperature, lipid availability) to stabilize fermentation. (bellanger2024theroleof pages 1-2, bellanger2024theroleof pages 3-4)

3. **Synthetic biology/biocatalysis at low temperature:** Transferable cold-adaptation effectors (DPS, GroEL, USP-2) that improve *E. coli* growth at 10 °C suggest engineering strategies for low-temperature bioprocessing/bioremediation (e.g., reducing energy cost, limiting contamination). (li2024mechanismsunderlyingthe pages 12-13)

## 6) Candidate causal edges (evidence-backed)

The following table is designed for direct translation into `data/traits/environment/temperature_preference.yaml` as candidate edges.

| Edge (subject–predicate–object) | Evidence snippet/quote | Notes | Source |
|---|---|---|---|
| temperature downshift → activates → DesK kinase state | “A decrease in temperature increases membrane thickness, which is sensed directly by membrane-bound DesK… helix rotations and 2-HCC rearrangement shift DesK between phosphatase (high-T/thin membrane) and kinase (low-T/thick membrane) states.” (ramon2023ageneraloverview pages 5-7) | Strong mechanistic edge for **Bacillus subtilis** cold sensing; assay/review synthesis, not universal across all bacteria. Candidate node: DesK histidine kinase. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| DesK kinase state → phosphorylates → DesR | “In its kinase state DesK phosphorylates a conserved aspartate in DesR.” (ramon2023ageneraloverview pages 5-7) | Strong, direct two-component signaling edge; taxon-specific exemplar from **B. subtilis**. Candidate nodes: DesK, DesR. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| DesR-P → activates expression of → des fatty-acid desaturase gene | “Phosphorylated DesR activates transcription of des (desaturase), increasing double bonds in membrane fatty acids…” (ramon2023ageneraloverview pages 5-7) | Strong gene-regulatory edge; supports inclusion of des/desaturase module in cold-adaptation graph. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| des desaturase expression → increases → unsaturated membrane fatty acids | “activates transcription of des (desaturase), increasing double bonds in membrane fatty acids” (ramon2023ageneraloverview pages 5-7) | Strong mechanistic edge linking desaturase to UFA content; appropriate generic node: unsaturated fatty acid biosynthesis/homeoviscous adaptation. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| increased unsaturated membrane fatty acids → increases → membrane fluidity | “increasing double bonds in membrane fatty acids and restoring membrane fluidity” (ramon2023ageneraloverview pages 5-7) | Core homeoviscous-adaptation edge; broadly curatable across microbes, though exact lipids differ by clade. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| low temperature → increases → cis-vaccenic acid | “on temperature downshift ‘only cis-vaccenic acid content increases ... and it does it quickly.’” (ramon2023ageneraloverview pages 2-4) | Strong for **E. coli**-like anaerobic UFA route; may not generalize to all taxa. Candidate metabolite: cis-vaccenic acid. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| FabF (β-ketoacyl-ACP synthase II) → increases → cis-vaccenic acid synthesis | “FabF … is ‘the key enzyme in the increase of cis-vaccenic acid,’ catalyzing the elongation of palmitoleoyl-ACP… to precursors of cis-vaccenoyl-ACP (18:1 Δ11-ACP).” (ramon2023ageneraloverview pages 4-5) | Strong enzyme-to-metabolite edge; specifically supports low-temperature membrane remodeling in bacteria using this pathway. | Ramón 2023. DOI: 10.1007/s42770-023-01057-4. URL: https://doi.org/10.1007/s42770-023-01057-4. Jul 2023. |
| low temperature (18°C vs 37°C) → increases → C16:1/C18:1 membrane fatty acids in *A. baumannii* | “At 18°C five strains showed a consistent increase in palmitoleic acid (C16:1), while one strain (ABVal2) uniquely increased oleic acid (C18:1).” (dessenne2024lipidomicanalysesreveal pages 1-2) | Strong primary-study edge; strain-specific variation is important. Assay: clinical strains grown at 18°C vs 37°C. | Dessenne 2024. DOI: 10.1128/spectrum.00757-24. URL: https://doi.org/10.1128/spectrum.00757-24. Oct 2024. |
| low temperature (18°C vs 37°C) → remodels → PE/PG lipid species with C16:1/C18:1 | “In most strains PE and PG species containing C16:1 and C18:1 rose at 18°C…” (dessenne2024lipidomicanalysesreveal pages 12-13) | Strong lipid-class-specific edge for *A. baumannii*; use with PE/PG nodes if graph supports lipid subclasses. | Dessenne 2024. DOI: 10.1128/spectrum.00757-24. URL: https://doi.org/10.1128/spectrum.00757-24. Oct 2024. |
| fabA / desaturase gene content → contributes to → low-temperature UFA remodeling in *A. baumannii* | “FabA was identified in ABVal2 and ABVal3; ABVal2 also encodes five candidate desaturases that may underlie its distinct unsaturated fatty acid profile.” (dessenne2024lipidomicanalysesreveal pages 1-2) | Useful but partly inferential/genomic association rather than direct knockout proof; curate as **uncertain/taxon-specific**. | Dessenne 2024. DOI: 10.1128/spectrum.00757-24. URL: https://doi.org/10.1128/spectrum.00757-24. Oct 2024. |
| temperature upshift → melts → RNA thermometers (ROSE/FourU) | “RNA thermometers (ROSE: 60–100 nt hairpins; FourU: four uracils) control translation by occluding Shine–Dalgarno/start codons; FourU melting points are quantified (≈42 °C without Mg2+ to ≈58 °C with Mg2+).” (moon2023temperaturemattersbacterial pages 3-5) | Strong mechanistic edge for bacterial heat sensing at RNA level; temperature thresholds depend on Mg2+ and construct context. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| RNA thermometer melting → permits translation of → heat-shock genes | “Post-transcriptional RNA thermometers in 5'-UTRs also mediate rapid temperature-dependent control of translation.” (moon2023temperaturemattersbacterial pages 1-3) | Strong generic edge; appropriate for heat-shock response nodes rather than temperature preference alone, but mechanistically relevant at trait boundary. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| cold shock → induces → CspA-mediated RNA remodeling | “Cold shock leads RNAs to form stable secondary/tertiary structures and induces cold-shock proteins (CspA can be ~15% of protein synthesis) that help maintain single-stranded RNA for translation.” (moon2023temperaturemattersbacterial pages 3-5) | Strong for bacterial cold-shock adaptation; likely best represented as RNA chaperone activity supporting translation at low temperature. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| cold shock → recruits → CsdA and RNase R for mRNA hairpin remodeling/degradation | “Cold-shock components include CspA and helicase CsdA collaborating with RNase R to selectively degrade mRNA hairpins at low temperature.” (moon2023temperaturemattersbacterial pages 1-3) | Strong mechanistic RNA-quality-control edge; mostly from model bacteria such as **E. coli**. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| cold shock → upregulates → RpoS | “RpoS is upregulated at low temperature via small RNAs (DsrA, RprA) that increase rpoS mRNA stability/translation” (moon2023temperaturemattersbacterial pages 3-5) | Strong regulatory edge in Gram-negative model bacteria; likely not universal. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| RpoS → upregulates → ostAB operon | “RpoS upregulates ostAB…” (moon2023temperaturemattersbacterial pages 3-5) | Strong within cited model system; can be represented as sigma factor → operon expression. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| ostAB operon → increases → trehalose accumulation | “RpoS upregulates ostAB and trehalose accumulation, a compatible-solute mechanism for cold tolerance.” (moon2023temperaturemattersbacterial pages 3-5) | Strong edge to compatible-solute node; supports inclusion of trehalose as low-temperature protective metabolite. | Moon 2023. DOI: 10.1007/s12275-023-00031-x. URL: https://doi.org/10.1007/s12275-023-00031-x. Mar 2023. |
| supraoptimal temperature → increases activity of → reverse gyrase / TopR1 | “Heat shock increases positive supercoils in plasmid DNA coincident with augmented TopR1 activity” and reverse gyrase is “suggested to maintain the genome integrity of thermophiles by limiting DNA melting and mediating DNA repair.” (takemata2024howdothermophiles pages 1-2) | Strong for archaeal thermophiles; TopR1 naming is taxon-specific. Suitable high-temperature adaptation node. | Takemata 2024. DOI: 10.1264/jsme2.me23087. URL: https://doi.org/10.1264/jsme2.me23087. Jun 2024. |
| reverse gyrase / TopR1 → increases → positive DNA supercoils | “Heat shock (e.g., 80°C→85°C) rapidly increases plasmid linking number within 15–30 min… consistent with reverse gyrase (mainly TopR1) introducing positive supercoils.” (villain2025regulationofdna pages 9-10) | Strong quantitative archaeal evidence; trait-relevant for thermophile growth at supraoptimal temperatures. | Villain 2025. DOI: 10.1111/mmi.15328. URL: https://doi.org/10.1111/mmi.15328. Dec 2025. |
| Lo18 binds phosphatidylglycerol / oleic-acid-rich membranes → enables → lipochaperone activity | “Lo18 showed increased affinity for oleic acid … and/or with the phosphatidylglycerol head group …” and these lipids “favor Lo18–membrane interaction and enable its lipochaperone activity.” (bellanger2024theroleof pages 2-3, bellanger2024theroleof pages 1-2) | Strong primary-study edge in **Oenococcus oeni**; stress context includes wine-associated acid/ethanol/temperature stress, so direct mapping to temperature preference is somewhat context-specific. | Bellanger 2024. DOI: 10.1038/s41598-024-67362-6. URL: https://doi.org/10.1038/s41598-024-67362-6. Jul 2024. |
| Lo18 lipochaperone activity → retains → membrane fluidity under heat stress | “Lo18 maintained membrane fluidity in exponential-phase liposomes (notably improving anisotropy retention from 52% to 68% in O. oeni at 45 °C)” (bellanger2024theroleof pages 3-4) | Strong quantitative edge but in liposome/biophysical assay; curate with assay note. | Bellanger 2024. DOI: 10.1038/s41598-024-67362-6. URL: https://doi.org/10.1038/s41598-024-67362-6. Jul 2024. |
| 10°C stress in *Rhodococcus* RCBS9 → upregulates → GroEL/GroES/ClpP/HSPs/USPs | “Hsps were upregulated, chaperonins GroES/GroEL and protease ClpP were increased, while canonical cold-shock proteins were not induced.” (li2024mechanismsunderlyingthe pages 10-12) | Strong transcriptomic edge at 10°C; low-temperature adaptation in one actinobacterial strain. | Li 2024. DOI: 10.3389/fmicb.2024.1465627. URL: https://doi.org/10.3389/fmicb.2024.1465627. Nov 2024. |
| 10°C stress in *Rhodococcus* RCBS9 → upregulates → DPS / SOD / peroxide-defense systems | “DPS was upregulated” and “all SOD genes plus PX, GPX and Prx were upregulated while catalase (CAT) was downregulated” at 10°C. (li2024mechanismsunderlyingthe pages 7-9) | Strong antioxidant/DNA-protection edge; useful as supporting low-temperature stress nodes. | Li 2024. DOI: 10.3389/fmicb.2024.1465627. URL: https://doi.org/10.3389/fmicb.2024.1465627. Nov 2024. |
| heterologous expression of RCBS9 GroEL / DPS / USP-2 in *E. coli* → improves growth at → 10°C | “Growth assays at 10°C showed that recombinant strains expressing some targets (notably BL21-DPS, BL21-GroEL, and BL21-USP-2) reached higher OD600 (peaking ~1.4 at 4 h) than vector control (~1.0–1.1), indicating improved cold adaptation” (li2024mechanismsunderlyingthe pages 12-13) | Strong functional support, but heterologous-expression assay in **E. coli BL21**; curate as validation of candidate cold-adaptation effectors, not direct native causal proof for RCBS9 temperature preference. | Li 2024. DOI: 10.3389/fmicb.2024.1465627. URL: https://doi.org/10.3389/fmicb.2024.1465627. Nov 2024. |


*Table: This table compiles evidence-backed candidate causal edges for microbial temperature preference, emphasizing mechanistic links from temperature shifts to membrane, RNA, DNA-topology, proteostasis, and compatible-solute systems. It is designed for TraitMech-style curation with assay and taxon-specific caveats noted.*

## 7) Ontology grounding suggestions (non-exhaustive)

- **METPO:** temperature preference = METPO:1000613 (given).
- **GO terms (candidate):**
  - membrane lipid metabolic process; fatty acid biosynthetic process; protein folding; response to temperature stimulus; DNA topological change; transcription regulation.
- **EC numbers (candidate):** FabF (EC 2.3.1.179), DNA gyrase (EC 5.6.2.2), Topoisomerase I (EC 5.6.2.1), SOD (EC 1.15.1.1).
- **CHEBI (candidate):** trehalose; oleic acid; palmitoleic acid; cis-vaccenic acid; phosphatidylethanolamine; phosphatidylglycerol.
- **NCBITaxon:**
  - *Acinetobacter baumannii*; *Bacillus subtilis*; *Escherichia coli*; *Oenococcus oeni*; *Rhodococcus* sp.; hyperthermophilic archaea (e.g., *Thermococcus*, *Pyrococcus*).

## 8) Warnings / curation caveats (important)

1. **Preference vs stress response:** Many edges here are derived from heat/cold-shock response literature (RNA thermometers, sigma factors). These are mechanistically relevant but may reflect **acute stress survival** rather than steady-state temperature preference; tag accordingly if your graph is strictly “growth preference.” (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)

2. **Taxon specificity:**
- DesK/DesR/des is a strong exemplar in *B. subtilis* and should be curated as a **bacterial cold-sensing module**, not assumed universal. (ramon2023ageneraloverview pages 5-7)
- Lo18 is specific to *O. oeni* and wine-associated stress; direct mapping to temperature preference may require additional growth-rate evidence in that organism. (bellanger2024theroleof pages 1-2)

3. **Associative vs causal genetic evidence:** The *A. baumannii* FabA/desaturase findings include genomic associations and plausible mechanism; without knockouts/perturbations they should be curated as **uncertain/inferred** edges. (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)

4. **Thermophile DNA topology evidence:** Reverse gyrase mechanistic linkage to positive supercoiling and thermophile genome integrity is strong, but some of the most quantitative linking-number evidence in this run is from a 2025 review; curate but note that it is beyond the 2024 prioritization window. (villain2025regulationofdna pages 9-10, takemata2024howdothermophiles pages 1-2)

## 9) DOI-first bibliography (with URLs and publication dates)

- Moon S, Ham S, Jeong J, et al. **Temperature Matters: Bacterial Response to Temperature Change.** *Journal of Microbiology* (Mar 2023). DOI: **10.1007/s12275-023-00031-x**. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)

- Ramón A, Esteves A, Villadóniga C, et al. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology* (Jul 2023). DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 5-7, ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4)

- Takemata N. **How Do Thermophiles Organize Their Genomes?** *Microbes and Environments* (Jun 2024). DOI: **10.1264/jsme2.me23087**. https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2)

- Bellanger T, Wien F, Combet S, et al. **The role of membrane physiology in sHSP Lo18-lipid interaction and lipochaperone activity.** *Scientific Reports* (Jul 2024). DOI: **10.1038/s41598-024-67362-6**. https://doi.org/10.1038/s41598-024-67362-6 (bellanger2024theroleof pages 1-2, bellanger2024theroleof pages 3-4)

- Dessenne C, Ménart B, Acket S, et al. **Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.** *Microbiology Spectrum* (Oct 2024). DOI: **10.1128/spectrum.00757-24**. https://doi.org/10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12)

- Li Q, Pan H, Hao P, et al. **Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain Rhodococcus sp. RCBS9.** *Frontiers in Microbiology* (Nov 2024). DOI: **10.3389/fmicb.2024.1465627**. https://doi.org/10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 10-12, li2024mechanismsunderlyingthe pages 7-9, li2024mechanismsunderlyingthe pages 12-13)

- Villain P, Basta T. **Regulation of DNA Topology in Archaea: State of the Art and Perspectives.** *Molecular Microbiology* (Dec 2025). DOI: **10.1111/mmi.15328**. https://doi.org/10.1111/mmi.15328 (villain2025regulationofdna pages 9-10)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

3. (ramon2023ageneraloverview pages 5-7): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

4. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

5. (li2024mechanismsunderlyingthe pages 10-12): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

6. (villain2025regulationofdna pages 9-10): Paul Villain and Tamara Basta. Regulation of dna topology in archaea: state of the art and perspectives. Molecular Microbiology, 123:245-264, Dec 2025. URL: https://doi.org/10.1111/mmi.15328, doi:10.1111/mmi.15328. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

8. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

9. (dessenne2024lipidomicanalysesreveal pages 12-13): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

10. (bellanger2024theroleof pages 1-2): Tiffany Bellanger, Frank Wien, Sophie Combet, Paloma Fernández Varela, and Stéphanie Weidmann. The role of membrane physiology in shsp lo18-lipid interaction and lipochaperone activity. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67362-6, doi:10.1038/s41598-024-67362-6. This article has 3 citations and is from a peer-reviewed journal.

11. (li2024mechanismsunderlyingthe pages 7-9): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

12. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

13. (dessenne2024lipidomicanalysesreveal pages 8-12): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

14. (li2024mechanismsunderlyingthe pages 9-10): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

15. (villain2025regulationofdna pages 10-12): Paul Villain and Tamara Basta. Regulation of dna topology in archaea: state of the art and perspectives. Molecular Microbiology, 123:245-264, Dec 2025. URL: https://doi.org/10.1111/mmi.15328, doi:10.1111/mmi.15328. This article has 7 citations and is from a domain leading peer-reviewed journal.

16. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (bellanger2024theroleof pages 2-3): Tiffany Bellanger, Frank Wien, Sophie Combet, Paloma Fernández Varela, and Stéphanie Weidmann. The role of membrane physiology in shsp lo18-lipid interaction and lipochaperone activity. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67362-6, doi:10.1038/s41598-024-67362-6. This article has 3 citations and is from a peer-reviewed journal.

18. (bellanger2024theroleof pages 3-4): Tiffany Bellanger, Frank Wien, Sophie Combet, Paloma Fernández Varela, and Stéphanie Weidmann. The role of membrane physiology in shsp lo18-lipid interaction and lipochaperone activity. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67362-6, doi:10.1038/s41598-024-67362-6. This article has 3 citations and is from a peer-reviewed journal.

19. (li2024mechanismsunderlyingthe pages 12-13): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.