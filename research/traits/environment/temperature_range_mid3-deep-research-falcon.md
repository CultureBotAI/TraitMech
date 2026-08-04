---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:24:28.943038'
end_time: '2026-08-04T04:31:57.069327'
duration_seconds: 448.13
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid3
  trait_identifier: METPO:1000452
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid3
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 30\u201334 \xB0C, characteristic of mesophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_30_to_34
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 30\u201334 \xB0C range as the\
    \ upper-mesophile growth range.)"
  causal_graph_summary: 'temperature_range_mid3_upper_mesophile: 14 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000452
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 30–34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C range as the upper-mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid3_upper_mesophile: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid3.yaml`.

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
- **Trait label:** temperature range mid3
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000452
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 30–34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C range as the upper-mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid3_upper_mesophile: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **temperature range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid3.yaml`.

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


# Curation report: microbial **temperature range mid3**

## Executive conclusion

**Target trait:** **temperature range mid3**  
**Identifier:** **METPO:1000452**  
**Category/kind:** ENVIRONMENT / CLASS  
**Definition supplied for curation:** a growth-supporting ambient-temperature range spanning approximately **30–34 °C**, characteristic of mesophilic physiology.  
**Parent:** **METPO:1000306**  
**Synonyms:** *Mesophilie*; *TR_30_to_34*.

The most defensible causal backbone is **ambient temperature → membrane physical state → membrane-fluidity sensing → fatty-acid remodeling → membrane fluidity compatible with growth**. In *Bacillus subtilis*, the DesK–DesR–des pathway supplies unusually strong molecular evidence for this chain. Recent 2024 lipidomics confirms extensive, but strain-dependent, remodeling of unsaturated fatty acids in *Acinetobacter baumannii*. Chaperone and proteostasis mechanisms are biologically relevant to thermal tolerance, but the retrieved 2024 intervention studies measured survival after severe heat shock rather than sustained growth across a 30–34 °C interval; these edges should therefore remain provisional for this trait. No retrieved study directly demonstrates that a particular molecular perturbation creates the **exact 30–34 °C growth-range breadth**.

## 1. Trait scope and boundary conditions

### 1.1 What the phenotype represents

For TraitMech, **METPO:1000452 should be modeled as an assay-observed thermal niche breadth**, not as a molecular stress response. A positive assignment requires net population growth over a temperature interval whose span falls approximately in the 30–34 °C bin. Suitable endpoints include repeated cell division, increase in viable biomass, specific growth rate, or another validated measure of sustained reproduction.

The phenotype should ideally be represented using cardinal-temperature observations:

- **TMIN:** lowest temperature permitting detectable sustained growth;
- **TOPT:** temperature giving the maximum growth rate under the assay conditions;
- **TMAX:** highest temperature permitting sustained growth;
- **growth-range breadth:** approximately `TMAX − TMIN`, subject to the temperatures actually tested.

A recent adaptive-evolution study explicitly uses TMIN, TMAX, and TOPT to characterize microbial growth profiles and defines mesophiles broadly by **TOPT 20–45 °C**. This broad mesophile definition is not equivalent to a 30–34 °C-wide growth range (lehmann2023adaptivelaboratoryevolution pages 1-2).

### 1.2 Distinctions from neighboring phenotypes

1. **Not temperature optimum.** A microorganism may have TOPT near 30–34 °C but possess a much narrower or wider growth range. Conversely, a 30–34 °C-wide range does not determine where TOPT lies.
2. **Not growth at 30–34 °C.** The supplied definition concerns the *span* of temperatures supporting growth, not merely growth at temperatures numerically between 30 and 34 °C.
3. **Not heat- or cold-shock survival.** Retention of viability after 30 minutes at 55 °C or five days at 52 °C does not establish reproduction at those temperatures or a 30–34 °C growth breadth (liang2024interactionsbetweenchaperone pages 8-10, sato2024effectsofsmall pages 10-11).
4. **Not generic mesophily.** Mesophily is commonly classified by TOPT, whereas this METPO class is a quantitative range bin (lehmann2023adaptivelaboratoryevolution pages 1-2).
5. **Assay dependence is intrinsic.** Medium, pH, oxygen, inoculum history, acclimation, incubation time, and temperature sampling density can alter observed TMIN and TMAX. A coarse temperature grid can over- or underestimate range breadth.

**Recommended graph interpretation:** mechanisms below should be treated as contributors that preserve growth across moderately changing temperatures, not as sufficient determinants of the exact bin.

## 2. Candidate nodes grouped by type

### Trait and experimental nodes

- **temperature range mid3 — METPO:1000452**
- Ambient growth temperature
- Decreased ambient temperature
- Increased ambient temperature
- Temperature shift / cold shock / heat shock
- Sustained growth rate
- TMIN, TOPT, TMAX
- Growth-supporting temperature-range breadth
- Culture medium, oxygen status, pH, acclimation time, and assay duration

### Cellular structures, physical states, and processes

- Cytoplasmic membrane — candidate **GO:0005886**
- Membrane lipid bilayer
- Membrane fluidity
- Membrane lipid order
- Liquid-crystalline membrane state
- Gel-state membrane
- Homeoviscous adaptation
- Fatty-acid biosynthetic process — candidate **GO:0006633**
- Unsaturated-fatty-acid biosynthetic process — candidate **GO:0006636**
- Protein folding — candidate **GO:0006457**
- Response to heat — candidate **GO:0009408**
- Protein disaggregation and proteolysis — label-only pending exact graph context

Lower temperature can drive a reversible liquid-crystalline-to-gel transition. Unsaturated and anteiso-branched fatty acids lower membrane transition temperature and counteract this loss of fluidity (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 1-2).

### Regulatory systems, genes, and proteins

**High-priority, mechanistically connected module**

- **DesK**, membrane-associated histidine kinase/thermosensor — *B. subtilis* label; species-specific database grounding required
- **DesR**, response regulator — *B. subtilis* label
- **des**, Δ9 fatty-acid desaturase gene — *B. subtilis* label
- Δ9 fatty-acid desaturase
- DesK–DesR two-component regulatory system
- **FabA**, 3-hydroxydecanoyl-ACP dehydratase/isomerase — label; ground by taxon before YAML insertion
- **FabB**, 3-oxoacyl-ACP synthase I — label; ground by taxon before insertion
- **FabH**, 3-oxoacyl-ACP synthase III — label; taxon-specific candidate

**Provisional proteostasis module**

- **DnaK/Hsp70**, **DnaJ/Hsp40**, **HtpG/Hsp90**
- **ClpX**, ATP-dependent protease/chaperone component
- **ClpB**, disaggregase
- **HSP20/small heat-shock proteins**, including native IbpA/IbpB and heterologous thermotolerant homologs
- Polyhydroxybutyrate storage pathway and PhaP — provisional, owing to reported epistasis with chaperone evolution in *Legionella pneumophila* (liang2024interactionsbetweenchaperone pages 1-2).

### Chemicals and lipid classes

- Saturated fatty acids
- Unsaturated fatty acids
- Anteiso-branched-chain fatty acids
- Iso-branched-chain fatty acids
- Short-chain fatty acids
- **Palmitoleic acid (C16:1)** — candidate **CHEBI:32372**, to be database-validated
- **Oleic acid (C18:1)** — candidate **CHEBI:16196**, to be database-validated
- Palmitate
- cis-3-decenoyl-ACP
- Phosphatidylethanolamine
- Phosphatidylglycerol
- Plasmalogens
- Isoleucine, as a substrate-level experimental determinant of branched-chain fatty-acid composition

Only identifiers confirmed against the project’s ontology release should enter the YAML. The species-specific DesK, DesR, des, fabA/fabB, dnaK/dnaJ, htpG, and clpX nodes should remain label-only until mapped to the exact organism and protein record.

## 3. Candidate causal edges

The following table separates immediately curatable generic or direct edges from strain-specific, survival-only, and inferred relationships.

| subject | predicate | object | evidence type/strength | taxon/assay | DOI | short supporting snippet | curation decision |
|---|---|---|---|---|---|---|---|
| decreased ambient temperature | increases | membrane lipid order / decreases membrane fluidity | review-level mechanistic synthesis; strong but generic | bacteria; general physiology | 10.1146/annurev-micro-091313-103612 | “low temperatures cause reversible state transitions from fluid (liquid crystalline) to nonfluid (gel) configurations” (mendoza2014temperaturesensingby pages 1-2) | Curate as generic environmental input edge; not specific to 30–34 °C |
| increased unsaturated fatty acids or anteiso-branched fatty acids | decreases | membrane transition temperature / increases fluidity | review-level mechanistic synthesis; strong | bacteria; general physiology | 10.1146/annurev-micro-091313-103612 | “Unsaturated fatty acids (UFAs) and anteiso-branched-chain fatty acids… decrease Tm and increase fluidity” (mendoza2014temperaturesensingby pages 2-4) | Curate as core homeoviscous mechanism |
| decreased temperature | induces | homeoviscous adaptation | review-level mechanistic synthesis; strong | bacteria; general physiology | 10.1146/annurev-micro-091313-103612 | bacteria incorporate “proportionally more UFAs or a-BCFAs to maintain optimal membrane fluidity” (mendoza2014temperaturesensingby pages 2-4) | Curate as central process node |
| homeoviscous adaptation | maintains | membrane fluidity compatible with growth | review-level mechanistic synthesis; strong | bacteria; general physiology | 10.1146/annurev-micro-091313-103612 | the process “optimizes the performance of a large array of cellular physiological processes at the new temperature” (mendoza2014temperaturesensingby pages 1-2) | Curate; generic growth-support mechanism |
| membrane lipid order increase | activates | DesK thermosensor signaling | direct perturbation plus review summary; strong | *Bacillus subtilis*; membrane-order manipulation at constant 37 °C | 10.1146/annurev-micro-091313-103612 | des activation occurred at constant 37 °C when membrane lipid order increased, showing DesK senses “membrane fluidity rather than temperature directly” (mendoza2014temperaturesensingby pages 5-6) | Curate as one of the strongest direct edges |
| DesK | phosphorylates/activates | DesR | direct molecular mechanism summarized in review; strong | *Bacillus subtilis* | 10.1146/annurev-micro-091313-103612 | “DesK autophosphorylation at His-188 transfers phosphate to DesR-Asp-54” (mendoza2014temperaturesensingby pages 5-6) | Curate |
| phosphorylated DesR | activates transcription of | des | direct molecular mechanism summarized in review; strong | *Bacillus subtilis* cold-shock response | 10.1146/annurev-micro-091313-103612 | “phosphorylated DesR-P activates des transcription” (mendoza2014temperaturesensingby pages 5-6) | Curate |
| des (Δ9-desaturase gene) expression | increases | unsaturated fatty-acid synthesis | direct molecular mechanism; strong | *Bacillus subtilis* cold shock | 10.1146/annurev-micro-091313-103612 | “the des gene encodes a Δ9-desaturase catalyzing cis double bonds in saturated fatty acids” (mendoza2014temperaturesensingby pages 5-6) | Curate |
| shift from 37 °C to 20 °C | induces | unsaturated fatty-acid synthesis | direct experimental evidence summarized in review; strong | *Bacillus subtilis* temperature-shift assay | 10.1146/annurev-micro-091313-103612 | “transfer to 20°C induces UFA synthesis” while at 37 °C saturated fatty acids dominate (mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 5-6) | Curate; nearest direct temperature-shift edge |
| lower temperature (18 °C vs 37 °C) | increases | palmitoleic acid (C16:1) abundance | direct lipidomics; strain-specific, correlational to phenotype; moderate | *Acinetobacter baumannii* clinical strains; 18 °C vs 37 °C culture | 10.1128/spectrum.00757-24 | “Five strains… increased palmitoleic acid (C16:1) at 18°C” (dessenne2024lipidomicanalysesreveal pages 8-12) | Provisional: curate only as strain-supported lipid remodeling edge |
| lower temperature (18 °C vs 37 °C) | increases | oleic acid (C18:1) abundance | direct lipidomics; strain-specific, correlational; moderate | *A. baumannii* ABVal2; 18 °C vs 37 °C culture | 10.1128/spectrum.00757-24 | “ABVal2 uniquely elevated oleic acid (C18:1) at 18°C” (dessenne2024lipidomicanalysesreveal pages 8-12) | Provisional: taxon/strain-specific |
| fabA/fabB presence (plus candidate desaturases) | enables/increases capacity for | unsaturated fatty-acid biosynthesis | genomic inference linked to lipidomics; moderate | *A. baumannii* ABVal2/ABVal3 | 10.1128/spectrum.00757-24 | insertion including “fabA and fabB genes… FabA catalyzes… a precursor of unsaturated C16:1 and C18:1 fatty acids” (dessenne2024lipidomicanalysesreveal pages 8-12) | Provisional: mechanistically plausible but not directly perturbed |
| heterologous HSP20 expression | increases survival under | prolonged high-temperature stress | direct intervention; strong for survival, not growth range | *Escherichia coli* expressing thermotolerant HSP20s; survival at 52 °C | 10.1007/s00792-023-01326-y | HSP20s “improved E. coli survival under prolonged high-temperature stress (>100 hours at 52°C)” (sato2024effectsofsmall pages 10-11) | Provisional: survival-only, outside target range |
| dnaJ / htpG mutations | increase | heat-shock survival time | reverse genetics in ALE background; strong for survival | *Legionella pneumophila*; 30-min heat challenge, 55–59 °C selection | 10.7717/peerj.17197 | “mutations in dnaJ and htpG were significantly beneficial for survival time” (liang2024interactionsbetweenchaperone pages 16-17) | Provisional: survival-only, high-temperature adaptation |
| clpX and dnaK pathway mutations | alter | heat-shock survival (epistatic, temperature-dependent) | reverse genetics/ALE; moderate to strong but complex | *L. pneumophila*; 55 °C kill-rate assay after heat-shock evolution | 10.7717/peerj.17197 | “ClpX mutations… potentially reflect altered substrate targeting” and dnaK effects showed “epistatic deterioration” with rescue by dnaJF95Y (liang2024interactionsbetweenchaperone pages 13-16, liang2024interactionsbetweenchaperone pages 8-10) | Provisional: complex, non-linear survival phenotype |
| adaptive laboratory evolution at suboptimal low temperature | shifts | growth temperature optimum (TOPT) downward | direct evolution experiment; strong for TOPT shift, not exact trait bin | *Thermoanaerobacter kivui*; serial transfer at 45 °C | 10.3389/fmicb.2023.1265216 | after 67 transfers, “a shift in the TOPT to 60°C was observed”; TMIN under conditions was 39 °C (lehmann2023adaptivelaboratoryevolution pages 1-2) | Provisional/background only: demonstrates evolvability of thermal niche, not METPO:1000452 |
| no cited source | directly proves | exact growth-supporting range of 30–34 °C | negative curation finding; strong | target trait synthesis | NA | available sources support general mesophilic/homeoviscous mechanisms, but “no source directly proves the exact 30–34 °C range” (lehmann2023adaptivelaboratoryevolution pages 1-2, mendoza2014temperaturesensingby pages 2-4) | Keep explicit warning in YAML; do not overstate exact-range causality |


*Table: This table compiles compact, curation-ready candidate edges for METPO:1000452, emphasizing direct mechanistic temperature–membrane links and clearly flagging survival-only, strain-specific, or correlational evidence. It is useful for deciding which edges are safe to curate now versus which should remain provisional.*

### Recommended core subgraph

The most conservative initial graph is:

1. `decreased ambient temperature — increases — membrane lipid order`
2. `membrane lipid order — activates — DesK signaling`
3. `DesK — phosphorylates — DesR`
4. `phosphorylated DesR — activates transcription of — des`
5. `des/Δ9-desaturase — increases — cis-unsaturated fatty acids`
6. `cis-unsaturated fatty acids — increase — membrane fluidity`
7. `homeoviscous adaptation — maintains — membrane fluidity compatible with growth`
8. `membrane fluidity compatible with growth — contributes_to — METPO:1000452`

Edges 1–7 have direct or strong mechanistic support. Edge 8 is necessarily an **inferred trait-linking edge** because the retrieved experiments did not measure the exact 30–34 °C range.

### Evidence details for the strongest edges

In *B. subtilis*, transfer from **37 °C to 20 °C** induces unsaturated-fatty-acid synthesis. DesK autophosphorylates at His-188, transfers phosphate to DesR Asp-54, and DesR-P activates transcription of **des**, whose product introduces cis double bonds into saturated fatty acids (mendoza2014temperaturesensingby pages 5-6). Crucially, manipulating isoleucine availability increased membrane lipid order and activated des at a constant 37 °C; in a branched-chain-fatty-acid-deficient background, des transcription reached approximately **fourfold above wild type**. This supports membrane physical state, rather than temperature itself, as the proximal DesK input (mendoza2014temperaturesensingby pages 5-6).

In *Bacillus megaterium*, palmitate desaturation was nearly complete at **23 °C** but negligible at **30 °C**. Transfer from 35 °C to 20 °C produced stronger desaturation than steady-state culture at 20 °C, indicating that both temperature-shift signaling and acclimated steady-state regulation matter (mendoza2014temperaturesensingby pages 4-5).

Comparative evidence also supports lipid composition as a thermal-adaptation variable: mesophilic *Mesotoga prima* at 35 °C contains branched and monounsaturated fatty acids, whereas thermophilic *Kosmotoga olearia* at 55 °C contains only saturated fatty acids. In Bacillus, desaturase regulation responds to membrane fluidity, while temperature-dependent FabH substrate selectivity can alter the initiation of branched-chain lipid synthesis in *Listeria monocytogenes* (pollo2015insightsintothermoadaptation pages 7-11). These are taxon-specific examples, not universal requirements.

## 4. Recent developments, 2023–2024

### 4.1 Strain-resolved lipidomics

Dessenne and colleagues cultured six clinical *A. baumannii* strains at **18 versus 37 °C**. Five strains increased palmitoleic acid (C16:1) at 18 °C, whereas ABVal2 preferentially increased oleic acid (C18:1). Across strains, total unsaturated fatty acids constituted approximately **60–80% at 18 °C**. ABVal2 and ABVal3 contained an approximately 20-gene insertion including **fabA** and **fabB**, while ABVal2 also carried five candidate desaturases (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12). Published October 2024; DOI: [10.1128/spectrum.00757-24](https://doi.org/10.1128/spectrum.00757-24).

This is valuable current evidence that homeoviscous adaptation varies substantially among strains. However, fabA/fabB presence was not independently perturbed, and the study does not establish that these genes determine thermal-range breadth. The corresponding gene-to-lipid edges should be annotated **genomically inferred / lipidomics-associated** rather than fully causal.

### 4.2 Adaptive evolution of cardinal temperature

Serial transfer of the thermophilic acetogen *Thermoanaerobacter kivui* at 45 °C for **67 transfers, approximately 180 generations**, shifted TOPT from **66 to 60 °C**. TMIN under the tested conditions remained 39 °C. The evolved strain had 67 SNPs, altered morphology, increased short-chain fatty acids at 50 versus 66 °C, and significantly more plasmalogens (lehmann2023adaptivelaboratoryevolution pages 1-2). Published October 2023; DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216).

This experiment demonstrates that cardinal growth temperatures and membrane composition are evolvable. It does not resolve which mutation caused the TOPT shift and does not model a 30–34 °C range; it should be background evidence rather than a direct trait edge.

### 4.3 Chaperones and engineered thermal survival

Heterologous expression of HSP20 proteins from thermotolerant bacteria enhanced *E. coli* stress resistance. Fifteen of 18 tested HSP20s improved resistance, and an HSP20 from *Tepidimonas sediminis* supported detectable viability after **52 °C treatment for five days (>100 hours)**, followed by proliferation when returned to 37 °C (sato2024effectsofsmall pages 10-11). Published January 2024; DOI: [10.1007/s00792-023-01326-y](https://doi.org/10.1007/s00792-023-01326-y).

This is a direct intervention and a plausible biotechnology module, but its endpoint is survival followed by recovery, not growth at 52 °C or expansion of the target growth range.

Adaptive evolution of *L. pneumophila* under progressively stronger heat shock produced parallel mutations in **dnaK, dnaJ, htpG, clpB, and clpX**. Reverse-genetic assays showed beneficial dnaJ and htpG mutations, but also strong epistasis: some dnaK combinations reduced tolerance and were rescued by dnaJ variation. The principal assay was survival after a **30-minute, 55 °C** challenge, with selection temperatures progressing to 59 °C over approximately 70 passages (liang2024interactionsbetweenchaperone pages 16-17, liang2024interactionsbetweenchaperone pages 8-10, liang2024interactionsbetweenchaperone pages 13-16). Published April 2024; DOI: [10.7717/peerj.17197](https://doi.org/10.7717/peerj.17197).

The authoritative interpretation is therefore not “more chaperone activity always broadens the growth range,” but that proteostasis-network variants can alter acute thermal survival in genotype- and epistasis-dependent ways.

## 5. Current applications and real-world relevance

1. **Industrial strain engineering.** Thermotolerant HSP20 proteins can be deployed as molecular tools to improve survival of production strains during thermal, pH, or osmotic stress. The demonstrated five-day 52 °C survival phenotype is compelling, although growth productivity under operating conditions still requires validation (sato2024effectsofsmall pages 10-11).
2. **Building-water pathogen control.** Heat-selection experiments in *L. pneumophila* are relevant to hot-water systems subjected to repeated, incomplete pasteurization. Chaperone and storage-network evolution may alter the effectiveness of thermal disinfection, but laboratory survival mutations were not established as common in environmental or clinical isolates (liang2024interactionsbetweenchaperone pages 16-17, liang2024interactionsbetweenchaperone pages 1-2).
3. **Pathogen persistence across environments.** The 2024 *A. baumannii* study links strain-specific lipid remodeling to survival outside healthcare environments and reports accompanying temperature-dependent differences in motility and biofilm formation. These observations may help explain environmental persistence, but they are associations rather than proven causal effects of individual lipids (dessenne2024lipidomicanalysesreveal pages 1-2).
4. **Evolutionary engineering.** The *T. kivui* experiment shows that selection can shift microbial TOPT by 6 °C within roughly 180 generations, providing a framework for adapting biocatalysts to lower process temperatures (lehmann2023adaptivelaboratoryevolution pages 1-2).

## 6. Curation recommendations

### Curate now

- The supplied trait node **METPO:1000452**, with parent **METPO:1000306**.
- Temperature-dependent membrane-order and homeoviscous-adaptation edges.
- The *B. subtilis* DesK → DesR → des → unsaturated-fatty-acid module, explicitly scoped to *B. subtilis*.
- UFA/anteiso-fatty-acid → lower transition temperature / increased fluidity edges.
- An inferred terminal edge from maintained membrane fluidity to support of growth across changing temperatures, carrying an evidence note that exact 30–34 °C breadth was not tested.

### Curate only as taxon-specific or provisional

- *A. baumannii* 18 °C → C16:1/C18:1 remodeling.
- fabA/fabB or candidate-desaturase presence → UFA profile.
- DnaK/DnaJ/HtpG/ClpX → acute heat survival.
- HSP20 overexpression → prolonged heat survival.
- Plasmalogens or short-chain fatty acids → reduced TOPT in evolved *T. kivui*.

### Suggested evidence qualifiers

- `direct_perturbation`
- `molecular_mechanism`
- `review_supported`
- `lipidomics_association`
- `genomic_inference`
- `adaptive_evolution_association`
- `survival_endpoint_not_growth`
- `taxon_specific`
- `strain_specific`
- `exact_trait_range_not_tested`

## 7. Warnings: claims not ready for TraitMech

1. **Do not state that more unsaturated fatty acids specifically cause a 30–34 °C growth breadth.** They support membrane function across temperature changes, but the exact trait bin was not experimentally attributed to them.
2. **Do not equate survival and growth.** HSP20 and *Legionella* studies demonstrate recovery or reduced killing after severe heat exposure, not reproduction at the challenge temperature (liang2024interactionsbetweenchaperone pages 16-17, sato2024effectsofsmall pages 10-11).
3. **Do not universalize DesK–DesR.** It is a strong *Bacillus* model; other taxa use different sensors, constitutive lipid profiles, substrate selection, or exogenous-fatty-acid uptake.
4. **Do not curate fabA/fabB as causal in *A. baumannii* without qualification.** Their presence coincides with distinctive lipid profiles, but knockout/complementation evidence was not retrieved (dessenne2024lipidomicanalysesreveal pages 8-12).
5. **Do not make oleic acid uniformly beneficial.** ABVal2’s C18:1-dominant response differed from the C16:1 response of five other strains, emphasizing strain-specific membrane solutions (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12).
6. **Do not infer causal genes from ALE recurrence alone.** The *T. kivui* study retained 67 SNPs, and the *Legionella* study found substantial epistasis and lineage complexity (lehmann2023adaptivelaboratoryevolution pages 1-2, liang2024interactionsbetweenchaperone pages 13-16).
7. **Do not assign a range from an incompletely sampled temperature series.** TMIN and TMAX are censored by the lowest and highest temperatures tested and by assay duration.

## 8. DOI-first bibliography

1. **de Mendoza D.** “Temperature sensing by membranes.” *Annual Review of Microbiology* 68:101–116. **September 2014.** DOI: [10.1146/annurev-micro-091313-103612](https://doi.org/10.1146/annurev-micro-091313-103612). Foundational source for membrane-state sensing, DesK–DesR regulation, and homeoviscous adaptation (mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 1-2).
2. **Dessenne C, et al.** “Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of *Acinetobacter baumannii*.” *Microbiology Spectrum* 12(10). **October 2024.** DOI: [10.1128/spectrum.00757-24](https://doi.org/10.1128/spectrum.00757-24) (dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal pages 8-12).
3. **Liang J, Faucher S.** “Interactions between chaperone and energy storage networks during the evolution of *Legionella pneumophila* under heat shock.” *PeerJ* 12. **April 2024.** DOI: [10.7717/peerj.17197](https://doi.org/10.7717/peerj.17197) (liang2024interactionsbetweenchaperone pages 16-17, liang2024interactionsbetweenchaperone pages 8-10, liang2024interactionsbetweenchaperone pages 13-16, liang2024interactionsbetweenchaperone pages 1-2).
4. **Sato Y, Okano K, Honda K.** “Effects of small heat shock proteins from thermotolerant bacteria on the stress resistance of *Escherichia coli* to temperature, pH, and hyperosmolarity.” *Extremophiles* 28(1). **January 2024.** DOI: [10.1007/s00792-023-01326-y](https://doi.org/10.1007/s00792-023-01326-y) (sato2024effectsofsmall pages 10-11).
5. **Lehmann M, et al.** “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14. **October 2023.** DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216) (lehmann2023adaptivelaboratoryevolution pages 1-2).
6. **Pollo SMJ, Zhaxybayeva O, Nesbø CL.** “Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum Thermotogae.” *Canadian Journal of Microbiology* 61:655–670. **September 2015.** DOI: [10.1139/cjm-2015-0073](https://doi.org/10.1139/cjm-2015-0073) (pollo2015insightsintothermoadaptation pages 7-11).

**Overall curation judgment:** the membrane-fluidity module is ready for a conservative, taxon-aware graph expansion. Proteostasis, ALE, and strain-resolved lipid nodes are valuable supporting hypotheses but should not yet be used as direct determinants of **METPO:1000452** without growth-range intervention data.

References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (liang2024interactionsbetweenchaperone pages 8-10): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

3. (sato2024effectsofsmall pages 10-11): Yu Sato, Kenji Okano, and Kohsuke Honda. Effects of small heat shock proteins from thermotolerant bacteria on the stress resistance of escherichia coli to temperature, ph, and hyperosmolarity. Extremophiles, Jan 2024. URL: https://doi.org/10.1007/s00792-023-01326-y, doi:10.1007/s00792-023-01326-y. This article has 21 citations and is from a peer-reviewed journal.

4. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

6. (liang2024interactionsbetweenchaperone pages 1-2): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

7. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

8. (mendoza2014temperaturesensingby pages 4-5): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 210 citations and is from a peer-reviewed journal.

9. (dessenne2024lipidomicanalysesreveal pages 8-12): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Microbiology Spectrum, Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

10. (liang2024interactionsbetweenchaperone pages 16-17): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

11. (liang2024interactionsbetweenchaperone pages 13-16): Jeffrey Liang and Sebastien Faucher. Interactions between chaperone and energy storage networks during the evolution of legionella pneumophila under heat shock. PeerJ, Apr 2024. URL: https://doi.org/10.7717/peerj.17197, doi:10.7717/peerj.17197. This article has 2 citations and is from a peer-reviewed journal.

12. (pollo2015insightsintothermoadaptation pages 7-11): Stephen M.J. Pollo, Olga Zhaxybayeva, and Camilla L. Nesbø. Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum <i>thermotogae</i>. Sep 2015. URL: https://doi.org/10.1139/cjm-2015-0073, doi:10.1139/cjm-2015-0073. This article has 63 citations and is from a peer-reviewed journal.

13. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Microbiology Spectrum, Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.