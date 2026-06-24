---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:28:46.094163'
end_time: '2026-06-18T01:46:01.672700'
duration_seconds: 1035.58
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature delta
  trait_identifier: METPO:1000303
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_delta
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature phenotype with numerical limits expressing the breadth\
    \ (maximum minus minimum, in \xB0C) of ambient temperatures supporting growth\
    \ of an organism."
  parent_traits: METPO:1000533, METPO:1000534
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance
    span as a derived descriptor reflecting overall thermal-adaptation flexibility.)
    | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation
    review supports homoviscous remodeling capacity as the basis of broad versus narrow
    temperature tolerance.)'
  causal_graph_summary: 'temperature_delta_thermal_flexibility: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature delta
- **METPO identifier:** METPO:1000303
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits expressing the breadth (maximum minus minimum, in °C) of ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance span as a derived descriptor reflecting overall thermal-adaptation flexibility.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous remodeling capacity as the basis of broad versus narrow temperature tolerance.)
- **Existing causal graph summary:** temperature_delta_thermal_flexibility: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta.yaml`.

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
- **Trait label:** temperature delta
- **METPO identifier:** METPO:1000303
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits expressing the breadth (maximum minus minimum, in °C) of ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the breadth of the temperature-tolerance span as a derived descriptor reflecting overall thermal-adaptation flexibility.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous remodeling capacity as the basis of broad versus narrow temperature tolerance.)
- **Existing causal graph summary:** temperature_delta_thermal_flexibility: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_delta.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **temperature delta** (METPO:1000303)

**Trait label:** temperature delta  
**METPO identifier:** METPO:1000303  
**Category:** ENVIRONMENT  
**Definition (given):** breadth (maximum − minimum, °C) of ambient temperatures supporting organismal growth.

## 1) Scope summary (what this trait is and is not)

### 1.1 What “temperature delta” represents
**Temperature delta** is a *growth-permissive temperature range width*: 
\[\Delta T = T_{max, growth} - T_{min, growth}\]
where *Tmin* and *Tmax* are defined operationally by the presence/absence of growth under specified assay conditions. This differs from “optimal growth temperature” (Topt) and from thermal performance curve (TPC) *shape* parameters, which require measuring a quantitative performance trait across a temperature gradient and fitting a model. In TPC literature, **Tmin** and **Tmax** are model parameters for the temperatures below/above which trait values are positive, and **Tpk** is the temperature of maximum performance; these are not equivalent to a simple growth/no-growth “growth limit” assay unless the trait is itself growth rate and sampled densely. (kontopoulos2024nouniversalmathematical pages 1-2)

### 1.2 Distinguishing from nearby traits (boundary cases)
* **Not the same as thermophile/psychrophile classification:** those categories are typically anchored to Tmin/Topt/Tmax and ecological definitions. For example, psychrophiles can grow at 0 °C, have optima near 15 °C, and do not grow at 20 °C; psychrotolerants can grow at 4 °C and have optimal growth above 20 °C; thermophiles have optima 50–80 °C; hyperthermophiles have growth ranges 80–110 °C. These are *category labels* rather than a numeric ∆T trait (ramon2023ageneraloverview pages 1-2).
* **Not the same as “thermal performance breadth” (e.g., full width at half maximum):** TPC breadth depends on curve shape and measurement density; identifiability issues mean different parameter sets can produce similar fitted curves, so breadth estimates can be model- and data-dependent (kontopoulos2024nouniversalmathematical pages 1-2).

### 1.3 Assay/measurement considerations relevant for curation
Growth temperature bounds depend strongly on protocol choices (medium, inoculum, aeration, time-to-score growth, acclimation). A concrete example of a discrete growth-temperature panel is thermophile screening with temperatures 37–80 °C in 10 steps (37, 40, 45, …, 80 °C), with triplicate cultures and defined inoculum counting procedures, illustrating how Tmin/Tmax (and thus ∆T) are inferred from a finite set of temperatures (valenzuela2024isolationofthermophilic pages 2-4).

## 2) Key concepts and current mechanistic understanding (nodes for a TraitMech graph)

Mechanistically, **temperature delta** is best treated as an *emergent descriptor* of the organism’s ability to maintain core cellular functions across both cold- and heat-side constraints. The most consistently supported mechanisms in the evidence corpus are:

### 2.1 Membrane homeoviscous adaptation and membrane-based temperature sensing
A central, broadly conserved concept is **homeoviscous adaptation**: at lower growth temperatures, bacteria incorporate proportionally more **cis-unsaturated fatty acids (UFAs)** (and/or **anteiso-branched-chain fatty acids**) to lower membrane transition temperature and maintain fluidity. This is presented as a strategy that “minimize[s] energy expenditure and optimize[s] growth” by preserving membrane-dependent processes (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 1-2).

A well-characterized bacterial module is the *Bacillus subtilis* membrane thermosensor two-component system:
* **DesK** (membrane histidine kinase) senses membrane lipid order and switches kinase/phosphatase activities depending on temperature.
* **DesR** (response regulator) activates transcription of **des** (fatty-acid desaturase), increasing unsaturation and restoring membrane disorder (negative feedback). (mendoza2014temperaturesensingby pages 6-8, mendoza2014temperaturesensingby pages 5-6)

Complementary lipid regulation occurs via fatty-acid biosynthesis/desaturation pathways:
* In *E. coli*, **FabA** introduces cis double bonds and **FabB** elongates the unsaturated intermediate, while **FabR** represses fabA/fabB in response to fatty-acyl species (ramon2023ageneraloverview pages 2-4).

### 2.2 Proteostasis modules (heat shock and cold shock)
Temperature extremes destabilize proteins and nucleic acids, requiring coordinated proteostasis responses.

**Heat shock (bacteria):** 
* The sigma factor **RpoH/σ32** promotes transcription of heat-shock genes encoding chaperones (e.g., **DnaK**, **GroEL**) and proteases (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 3-5).
* **DnaK/DnaJ** interact with **ClpB** to resolve protein aggregates (moon2023temperaturemattersbacterial pages 6-7).
* Proteases (e.g., **FtsH**, **ClpXP**) regulate heat shock circuitry, including RpoH turnover (moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 3-5).

**Cold shock (bacteria):**
* Cold increases RNA secondary structure and impairs translation; **CspA** acts as an RNA chaperone that destabilizes secondary structures to facilitate transcription/translation at low temperature (grunberger2023uncoveringthetemporal pages 2-4).
* A quantitative datapoint: **CspA can constitute ~15% of protein synthesis after cold shock** in bacteria (moon2023temperaturemattersbacterial pages 3-5).

**Archaea:** thermal-stress regulation differs from bacteria; in *Pyrococcus furiosus*, the transcription factor **Phr** is described as a negative regulator of many heat-inducible genes (grunberger2023uncoveringthetemporal pages 2-4). 

### 2.3 Genome stability mechanisms at high temperature (candidate/uncertain)
For hyperthermophiles, adaptations discussed include **positive DNA supercoiling by reverse gyrase** (grunberger2023uncoveringthetemporal pages 1-2). In this evidence set, this is presented as background synthesis rather than direct causal measurement of ∆T, so it should be treated as a *candidate but uncertain* causal node/edge for temperature_delta curation.

## 3) Candidate nodes grouped by type (ontology grounding suggestions)

### 3.1 Environmental and experimental factors
* **Ambient growth temperature** (label; ENVO term possible but not assigned here)
* **Temperature shift (heat shock / cold shock)** (label)
* **Medium composition / branched-chain AA availability (e.g., isoleucine)** influencing membrane branching (label; mentioned as mechanistic context) (mendoza2014temperaturesensingby pages 5-6)
* **Assay design:** discrete temperature panels, incubation time, aeration/shaking vs static, inoculum size (label) (valenzuela2024isolationofthermophilic pages 2-4)

### 3.2 Pathways/modules
* **Homeoviscous adaptation / membrane lipid remodeling** (label) (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 1-2)
* **Fatty-acid desaturation pathway** (label)
* **Heat shock response / proteostasis network** (label) (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 3-5)
* **Cold shock response / RNA chaperone network** (label) (grunberger2023uncoveringthetemporal pages 2-4)

### 3.3 Genes/proteins/regulators (label nodes; CURIEs not asserted without UniProt/GO mapping in excerpts)
* **DesK** (sensor histidine kinase), **DesR** (response regulator), **des** (fatty-acid desaturase) (mendoza2014temperaturesensingby pages 6-8, mendoza2014temperaturesensingby pages 5-6)
* **Hik33/Rer1** (cyanobacterial cold sensor/regulator), **desB/desD** (desaturases) (mendoza2014temperaturesensingby pages 6-8)
* **FabA**, **FabB**, **FabR** (fatty acid biosynthesis/desaturation regulation) (ramon2023ageneraloverview pages 2-4)
* **RpoH/σ32**, **DnaK**, **DnaJ**, **GroEL**, **GroES**, **ClpB**, **FtsH**, **ClpXP** (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 3-5)
* **CspA** (cold shock protein) (grunberger2023uncoveringthetemporal pages 2-4, moon2023temperaturemattersbacterial pages 3-5)
* **Phr** (archaeal heat shock regulator) (grunberger2023uncoveringthetemporal pages 2-4)
* **Reverse gyrase** (candidate) (grunberger2023uncoveringthetemporal pages 1-2)

### 3.4 Chemicals/metabolites (CHEBI candidates; keep as label if unsure)
* **Unsaturated fatty acids (UFAs)** (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 1-2)
* **Anteiso-branched-chain fatty acids** (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 6-8)
* **Compatible solutes** (e.g., glycine betaine, trehalose, glycerol; presented as cold-adaptation strategy) (purwar2024adaptationsofpsychrophilic pages 10-11)

## 4) Evidence-backed candidate causal edges (curation table)

| Subject node | Predicate | Object node | Evidence snippet | Source | Curation notes |
|---|---|---|---|---|---|
| decreased growth temperature / increased membrane order | activates | DesK histidine kinase (label; Bacillus subtilis thermosensor) | “decreased temperature → increased lipid order → DesK activation” (mendoza2014temperaturesensingby pages 6-8) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Strong mechanistic evidence; Bacillus-specific sensor architecture; environmental input node rather than gene product. |
| DesK histidine kinase (label) | phosphorylates / activates | DesR response regulator (label) | “DesK has… a cytosolic kinase domain… transfers phosphate to DesR (Asp-54). Phosphorylated DesR activates des expression” (mendoza2014temperaturesensingby pages 5-6) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Strong for *B. subtilis* two-component system; curate as taxon-specific unless generalized carefully. |
| DesR response regulator (label) | positively regulates expression of | des fatty-acid desaturase gene (label) | “Phosphorylated DesR activates des expression” (mendoza2014temperaturesensingby pages 5-6) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Strong direct regulatory edge; taxon-specific. |
| des fatty-acid desaturase / 5-Des (label) | increases abundance of | unsaturated fatty acids (CHEBI candidate: unsaturated fatty acid) | “des gene encodes… desaturase (5-Des) that introduces a cis double bond at the Δ5 position of saturated fatty acids” (mendoza2014temperaturesensingby pages 5-6) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Strong biochemical function; product class broad rather than a single CHEBI term. |
| unsaturated fatty acids (CHEBI candidate) | decreases | membrane transition temperature / increases membrane fluidity (GO/label candidate) | “cis-unsaturated fatty acids… disrupt packing, lower Tm, and increase fluidity” (mendoza2014temperaturesensingby pages 2-4) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Foundational, broadly applicable; object best kept as label if no exact ontology term chosen. |
| unsaturated fatty acids (CHEBI candidate) | supports | low-temperature growth / broader temperature delta (METPO:1000303 candidate linkage) | “bacteria respond to decreasing growth temperature by incorporating proportionally more unsaturated fatty acids… [which] optimizes many cellular processes at the new temperature” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Trait edge is inferred from membrane-function optimization rather than direct Tmax−Tmin measurement; curate as indirect/mechanistic. |
| anteiso-branched-chain fatty acids (label) | increases | membrane fluidity / lowers lipid order (label) | “anteiso-branched-chain fatty acids (a-BCFAs) disrupt packing, lower Tm” (mendoza2014temperaturesensingby pages 2-4) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Strong physical-mechanistic support; generalized across bacteria using branched lipids. |
| anteiso-branched-chain fatty acids (label) | required for | membrane function/growth at low temperature (label) | “Membrane function/growth at low temperature requires both anteiso-branched-chain fatty acids (a-BCFAs) and unsaturated fatty acids (UFAs)” (mendoza2014temperaturesensingby pages 6-8) | de Mendoza, 2014, *Annual Review of Microbiology*, doi:10.1146/annurev-micro-091313-103612, https://doi.org/10.1146/annurev-micro-091313-103612 | Useful direct edge to growth-supporting capacity; wording is review-level synthesis, not one assay. |
| FabA (label) | contributes to biosynthesis of | unsaturated fatty acids / cis double bonds (label) | “Key biosynthetic enzymes in *E. coli* include FabA (introduces cis double bonds)” (ramon2023ageneraloverview pages 2-4) | Ramón, 2023, *Brazilian Journal of Microbiology*, doi:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4 | Good mechanistic support; based on *E. coli* pathway. |
| FabB (label) | elongates / contributes to biosynthesis of | unsaturated fatty acid intermediate (label) | “FabB (elongates the unsaturated intermediate)” (ramon2023ageneraloverview pages 2-4) | Ramón, 2023, *Brazilian Journal of Microbiology*, doi:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4 | Good pathway edge; *E. coli*-centered. |
| FabR repressor (label) | negatively regulates | fabA/fabB expression (label) | “FabR is a transcriptional repressor… when UFAs accumulate, FabR bound to UFAs increases repression of fabA/fabB” (ramon2023ageneraloverview pages 2-4) | Ramón, 2023, *Brazilian Journal of Microbiology*, doi:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4 | Strong regulatory edge, but specific to organisms with FabR-controlled UFA biosynthesis. |
| cold shock | induces | CspA cold-shock protein (GO/label candidate) | “cold-induced proteins such as CspA in *Escherichia coli*” and “CspA… act as RNA chaperones” (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 2-4) | Grünberger, 2023, *mBio*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 | Strong for bacteria; archaeal thermophiles may lack canonical CspA family. |
| CspA cold-shock protein (label) | destabilizes | RNA secondary structure (GO/label candidate) | “Csps are small, conserved nucleic-acid binding proteins that act as RNA chaperones, destabilizing secondary structures at low temperature” (grunberger2023uncoveringthetemporal pages 2-4) | Grünberger, 2023, *mBio*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 | Strong mechanism for cold-side breadth; effect on temperature_delta is indirect. |
| CspA cold-shock protein (label) | facilitates | transcription and translation at low temperature (GO:0006412 candidate for translation) | “destabilizing secondary structures at low temperature to facilitate transcription and translation” (grunberger2023uncoveringthetemporal pages 2-4) | Grünberger, 2023, *mBio*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 | Broadly useful edge for low-T growth support; mostly bacterial evidence. |
| RpoH / sigma-32 (label) | positively regulates expression of | DnaK chaperone system (label) | “σ32 promotes transcription of heat shock genes encoding chaperones such as DnaK and GroEL” (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 3-5) | Grünberger, 2023, *mBio*; Moon, 2023, *Journal of Microbiology*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 ; doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong bacterial heat-response edge; not universal in archaea. |
| RpoH / sigma-32 (label) | positively regulates expression of | GroEL/GroES chaperonin system (label) | “σ32 promotes transcription of heat shock genes encoding chaperones such as DnaK and GroEL” (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 3-5) | Grünberger, 2023, *mBio*; Moon, 2023, *Journal of Microbiology*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 ; doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong bacterial heat-response edge; supports high-T side of growth breadth indirectly. |
| DnaK/DnaJ chaperone system (label) | recruits / activates | ClpB disaggregase (label; Hsp100 family) | “DnaK (with DnaJ)… recruits/activates the disaggregase ClpB” (moon2023temperaturemattersbacterial pages 6-7) | Moon, 2023, *Journal of Microbiology*, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Strong bacterial proteostasis edge; heat survival focused, not breadth directly measured. |
| ClpB disaggregase (label) | promotes | protein disaggregation during heat stress (GO/label candidate) | “ClpB is an ATP-dependent Hsp100 disaggregating chaperone” (moon2023temperaturemattersbacterial pages 6-7) | Moon, 2023, *Journal of Microbiology*, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Good mechanistic edge; indirect relation to temperature_delta. |
| FtsH protease / ClpXP protease (label) | degrades / regulates | RpoH / sigma-32 (label) | “FtsH is required for regulation of the heat shock-responsive sigma factor RpoH via degradation” and “ClpXP” participates in control (moon2023temperaturemattersbacterial pages 6-7, moon2023temperaturemattersbacterial pages 3-5) | Moon, 2023, *Journal of Microbiology*, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | Useful regulatory feedback edge; specific mechanistic details vary by species and condition. |
| Phr transcription factor (label; archaeal) | negatively regulates | heat-inducible genes in *Pyrococcus furiosus* (label) | “the transcription factor Phr… act[s] as a negative regulator of many heat-inducible genes” (grunberger2023uncoveringthetemporal pages 2-4) | Grünberger, 2023, *mBio*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 | Strong archaeal heat-shock regulation edge; relevance to broader temperature delta is plausible but organism-specific. |
| reverse gyrase (label) | increases | positive DNA supercoiling (GO/label candidate) | “Adaptations cited include… positive DNA supercoiling by reverse gyrase” (grunberger2023uncoveringthetemporal pages 1-2) | Grünberger, 2023, *mBio*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 | Important hyperthermophile adaptation, but evidence here is review-style summary within article intro. |
| positive DNA supercoiling (label) | supports | growth at high temperature / high-T side of temperature delta (label) | “high temperature causes protein denaturation/aggregation… adaptations cited include… positive DNA supercoiling by reverse gyrase” (grunberger2023uncoveringthetemporal pages 1-2) | Grünberger, 2023, *mBio*, doi:10.1128/mbio.02174-23, https://doi.org/10.1128/mbio.02174-23 | Indirect edge inferred from known hyperthermophile adaptation; should be marked uncertain for direct curation to temperature_delta. |


*Table: This table compiles curation-ready candidate causal edges for microbial growth temperature range breadth, with evidence snippets and limitations. It emphasizes membrane homeoviscous adaptation, cold-shock/heat-shock proteostasis, and high-temperature genome stability mechanisms relevant to curating a TraitMech graph.*

## 5) Recent developments and latest research (prioritize 2023–2024)

### 5.1 Multi-omics characterization of thermal stress networks (2023)
A 2023 mBio study in the hyperthermophilic archaeon *Pyrococcus furiosus* emphasizes rapid and dynamic transcriptomic and proteomic remodeling under heat and cold shock, identifying regulator-level control (Phr) and distinct cold-response signatures that implicate translational regulation (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 2-4). This type of time-resolved systems study is especially relevant to temperature_delta curation because it supports mechanistic nodes describing **regulatory capacity** and **response dynamics**, not just static traits.

### 5.2 Renewed focus on model/measurement uncertainty in thermal performance (2024)
A 2024 Nature Communications synthesis demonstrates that there is no universal mathematical model for TPCs and highlights practical limitations (small datasets, identifiability) in estimating Tmin/Tmax/Tpk from performance curves (kontopoulos2024nouniversalmathematical pages 1-2). For curation, this motivates treating temperature_delta (growth/no-growth range) as a distinct, assay-dependent trait from TPC-derived widths.

### 5.3 Psychrophile-focused mechanistic and applied synthesis (2024)
A 2024 review emphasizes cold-side determinants such as membrane remodeling, compatible solutes, antifreeze/ice-binding proteins, and metabolic rewiring, and connects these to applied contexts including food spoilage in refrigerated environments and biotechnology in low-temperature conditions (purwar2024adaptationsofpsychrophilic pages 1-3, purwar2024adaptationsofpsychrophilic pages 10-11).

## 6) Current applications and real-world implementations

### 6.1 Industrial biocatalysis: thermozymes and psychrozymes
Thermophilic enzymes are described as thermostable and often show optimal activity between **55–110 °C**, with applications spanning food-industry intermediates, detergents, and DNA-modifying tools for molecular biology (Valenzuela et al., 2024) (valenzuela2024isolationofthermophilic pages 2-4). Cold-adapted enzymes from psychrophiles are highlighted for low-temperature processing (e.g., cold-processed foods, cold-water detergents, textiles), with reported benefits such as energy savings and easier deactivation (Gupta et al., 2023) (gupta2023psychrophilesasa pages 1-2).

### 6.2 Food safety and cold-chain contexts
Psychrotrophic bacteria can persist after pasteurization and continue growing in refrigerated milk; psychrotrophs are described as thriving at **7 °C or lower**, linking cold-side growth capacity (low Tmin) to real food-chain risk (purwar2024adaptationsofpsychrophilic pages 1-3).

### 6.3 Environmental biotechnology and bioremediation
Cold-adapted microbes/enzymes are linked to bioremediation and biological control in cold regions (including Antarctic-sourced genes/enzymes) (purwar2024adaptationsofpsychrophilic pages 1-3, ramon2023ageneraloverview pages 1-2).

## 7) Relevant quantitative statistics (from included sources)

* **Environmental context:** most terrestrial biosphere **85%** and **90%** of oceans are below **5 °C** (Ramón et al., 2023) (ramon2023ageneraloverview pages 1-2).
* **Category ranges (contextual, not ∆T itself):** thermophiles optimum 50–80 °C; hyperthermophiles growth range 80–110 °C; psychrophiles grow at 0 °C, optimum ~15 °C (ramon2023ageneraloverview pages 1-2).
* **Cold tolerance example:** *Psychrobacter cryopegella* can thrive at **−10 °C** and remain metabolically active at **−20 °C** (purwar2024adaptationsofpsychrophilic pages 1-3).
* **Assay implementation example:** thermophile growth tests run **37–80 °C** in discrete steps; incubation commonly at **60 °C** (valenzuela2024isolationofthermophilic pages 2-4).
* **Cold shock quantitative response:** **CspA ≈15% of protein synthesis after cold shock** (moon2023temperaturemattersbacterial pages 3-5).
* **Psychrophile genomics statistic (resource-level):** GOLD database numbers for psychrophile genomes (83 complete/permanent draft; 102 targeted/incomplete) and **43.4%** marine origin (purwar2024adaptationsofpsychrophilic pages 3-4).
* **Psychrophile biotech activity (review-level):** “43 businesses” and “31 patents or filings” in an Arctic product context (gupta2023psychrophilesasa pages 9-10).

## 8) Expert interpretation (authoritative-source synthesis)

Across authoritative reviews and mechanistic studies, **temperature delta** can be interpreted as reflecting *the integration of at least two major constraint classes*: 
1) **membrane physical-state control** (via lipid composition and membrane sensing), and 
2) **macromolecular stability/proteostasis and RNA homeostasis** (via heat/cold shock regulons and chaperone networks). 

The strongest “core module” repeatedly supported in the provided evidence is the **membrane-thermosensing → desaturase induction → restored fluidity** feedback loop (DesK/DesR/des) and the more general principle that increased unsaturated/branched lipids preserve function at low temperatures (mendoza2014temperaturesensingby pages 6-8, mendoza2014temperaturesensingby pages 2-4). Proteostasis modules (RpoH→DnaK/GroEL; DnaK/DnaJ→ClpB; cold→CspA) represent complementary mechanisms that support function at extremes and thus plausibly widen growth-permissive boundaries (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 6-7, grunberger2023uncoveringthetemporal pages 2-4).

## 9) Warnings / claims not yet ready for direct TraitMech curation

1) **Avoid curating TPC-model parameters as temperature_delta** without explicit mapping: TPC-derived Tmin/Tmax depend on model fit, sampling resolution, and identifiability; temperature_delta is specifically growth-supporting breadth and may be derived from binary growth assays rather than TPCs (kontopoulos2024nouniversalmathematical pages 1-2).
2) **Reverse gyrase → high-temperature growth breadth** is plausible but is only supported here as background synthesis rather than explicit causal evidence tied to growth range measurements; curate as uncertain unless supported by a primary experimental source directly linking reverse gyrase perturbation to Tmax shifts (grunberger2023uncoveringthetemporal pages 1-2).
3) Many regulatory modules (DesK/DesR, FabR; RpoH circuits) are **taxon-specific in implementation**; edges should be tagged with organismal scope and not assumed universal.

---

# DOI-first bibliography (with URLs and publication dates where available)

1. Kontopoulos D-G, Sentis A, Daufresne M, et al. **No universal mathematical model for thermal performance curves across traits and taxonomic groups.** *Nature Communications*. 2024-10. doi:10.1038/s41467-024-53046-2. https://doi.org/10.1038/s41467-024-53046-2 (kontopoulos2024nouniversalmathematical pages 1-2)
2. Valenzuela B, Solís-Cornejo F, Araya R, Zamorano P. **Isolation of Thermophilic Bacteria from Extreme Environments in Northern Chile.** *Microorganisms*. 2024-02. doi:10.3390/microorganisms12030473. https://doi.org/10.3390/microorganisms12030473 (valenzuela2024isolationofthermophilic pages 2-4, valenzuela2024isolationofthermophilic pages 1-2)
3. Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory ＆ Technology*. 2024-10. doi:10.37256/amtt.5220244537. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 1-3, purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 3-4)
4. Grünberger F, Schmid G, Ahmad ZE, et al. **Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.** *mBio*. 2023-12. doi:10.1128/mbio.02174-23. https://doi.org/10.1128/mbio.02174-23 (grunberger2023uncoveringthetemporal pages 1-2, grunberger2023uncoveringthetemporal pages 2-4)
5. Moon S, Ham S, Jeong J, et al. **Temperature Matters: Bacterial Response to Temperature Change.** *Journal of Microbiology*. 2023-03. doi:10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 6-7)
6. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology*. 2023-07. doi:10.1007/s42770-023-01057-4. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4)
7. Gupta V, Bhaskar P, Thoudam J, et al. **Psychrophiles as a novel and promising source of cold-adapted industrial enzymes.** *The Applied Biology & Chemistry Journal*. 2023-06. doi:10.52679/tabcj.2023.0006. https://doi.org/10.52679/tabcj.2023.0006 (gupta2023psychrophilesasa pages 1-2, gupta2023psychrophilesasa pages 9-10)
8. de Mendoza D. **Temperature sensing by membranes.** *Annual Review of Microbiology*. 2014-09. doi:10.1146/annurev-micro-091313-103612. https://doi.org/10.1146/annurev-micro-091313-103612 (mendoza2014temperaturesensingby pages 2-4, mendoza2014temperaturesensingby pages 6-8, mendoza2014temperaturesensingby pages 5-6, mendoza2014temperaturesensingby pages 4-5, mendoza2014temperaturesensingby pages 1-2, mendoza2014temperaturesensingby pages 15-16)


References

1. (kontopoulos2024nouniversalmathematical pages 1-2): Dimitrios - Georgios Kontopoulos, Arnaud Sentis, Martin Daufresne, Natalia Glazman, Anthony I. Dell, and Samraat Pawar. No universal mathematical model for thermal performance curves across traits and taxonomic groups. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53046-2, doi:10.1038/s41467-024-53046-2. This article has 31 citations and is from a highest quality peer-reviewed journal.

2. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

3. (valenzuela2024isolationofthermophilic pages 2-4): Bernardita Valenzuela, Francisco Solís-Cornejo, Rubén Araya, and Pedro Zamorano. Isolation of thermophilic bacteria from extreme environments in northern chile. Microorganisms, 12:473, Feb 2024. URL: https://doi.org/10.3390/microorganisms12030473, doi:10.3390/microorganisms12030473. This article has 17 citations.

4. (mendoza2014temperaturesensingby pages 2-4): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

5. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

6. (mendoza2014temperaturesensingby pages 6-8): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

7. (mendoza2014temperaturesensingby pages 5-6): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

8. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

9. (grunberger2023uncoveringthetemporal pages 1-2): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

10. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

11. (moon2023temperaturemattersbacterial pages 6-7): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

12. (grunberger2023uncoveringthetemporal pages 2-4): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

13. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

14. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

15. (gupta2023psychrophilesasa pages 1-2): Varsha Gupta, Pranav Bhaskar, Jeancolar Thoudam, Shiwali Bisht, Anita Sharma, and Rashmi Tripathi. Psychrophiles as a novel and promising source of cold-adapted industrial enzymes. The Applied Biology &amp; Chemistry Journal, pages 54-68, Jun 2023. URL: https://doi.org/10.52679/tabcj.2023.0006, doi:10.52679/tabcj.2023.0006. This article has 10 citations.

16. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

17. (gupta2023psychrophilesasa pages 9-10): Varsha Gupta, Pranav Bhaskar, Jeancolar Thoudam, Shiwali Bisht, Anita Sharma, and Rashmi Tripathi. Psychrophiles as a novel and promising source of cold-adapted industrial enzymes. The Applied Biology &amp; Chemistry Journal, pages 54-68, Jun 2023. URL: https://doi.org/10.52679/tabcj.2023.0006, doi:10.52679/tabcj.2023.0006. This article has 10 citations.

18. (valenzuela2024isolationofthermophilic pages 1-2): Bernardita Valenzuela, Francisco Solís-Cornejo, Rubén Araya, and Pedro Zamorano. Isolation of thermophilic bacteria from extreme environments in northern chile. Microorganisms, 12:473, Feb 2024. URL: https://doi.org/10.3390/microorganisms12030473, doi:10.3390/microorganisms12030473. This article has 17 citations.

19. (mendoza2014temperaturesensingby pages 4-5): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

20. (mendoza2014temperaturesensingby pages 15-16): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.