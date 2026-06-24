---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:10:13.235640'
end_time: '2026-06-18T02:38:28.445319'
duration_seconds: 1695.21
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid4
  trait_identifier: METPO:1000446
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid4
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 34 and 40 \xB0C, characteristic of warm-mesophilic physiology\
    \ (including many mammalian host-associated bacteria)."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_34_to_40
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports a 34\u201340 \xB0C optimum as the\
    \ warm-mesophile (mammalian-host) setpoint.)"
  causal_graph_summary: 'temperature_optimum_mid4_warm_mesophile: 4 nodes, 3 edges'
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
- **Trait label:** temperature optimum mid4
- **METPO identifier:** METPO:1000446
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 34 and 40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 34–40 °C optimum as the warm-mesophile (mammalian-host) setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid4_warm_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid4.yaml`.

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
- **Trait label:** temperature optimum mid4
- **METPO identifier:** METPO:1000446
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 34 and 40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 34–40 °C optimum as the warm-mesophile (mammalian-host) setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid4_warm_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid4.yaml`.

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


## Curation-focused research report: METPO:1000446 temperature optimum mid4 (warm mesophile; 34–40 °C)

### 1) Scope summary (trait meaning, boundaries, and distinctions)

**Trait definition (curation target).** *temperature optimum mid4* (METPO:1000446) represents a **temperature optimum phenotype** where an organism’s **best-growth ambient temperature** lies **approximately 34–40 °C**, i.e., a warm-mesophilic setpoint that overlaps mammalian host temperature (~37 °C). This is consistent with the common use of **E. coli as a canonical mesophile with optimal growth at 37 °C**. (moon2023temperaturemattersbacterial pages 1-3)

**How it differs from nearby temperature categories.** A useful categorical boundary appears in an experimental thermophile adaptation study that defines **mesophiles as TOPT ~20–45 °C**, and **thermophiles as TOPT >45 °C** (with more extreme tiers above that). (lehmann2023adaptivelaboratoryevolution pages 1-2)

**Boundary cases.** (i) Organisms with TOPT near **40–45 °C** may be better treated as **upper-mesophiles/thermotolerant** depending on the ontology’s adjacent classes; this trait (mid4) should be curated only when the optimum lies within **34–40 °C**. (ii) Mechanisms such as **reverse gyrase** are strongly associated with **high-temperature thermophily** (especially >65 °C) and should generally be treated as a **contrast/boundary-case mechanism**, not a core warm-mesophile mechanism. (takemata2024howdothermophiles pages 1-2)

### 2) Key concepts and mechanistic definitions (current understanding)

**Temperature optimum (TOPT).** TOPT is a cardinal temperature descriptor of growth, used for grouping taxa into psychrophiles/mesophiles/thermophiles. (lehmann2023adaptivelaboratoryevolution pages 1-2)

**Homeoviscous adaptation (membrane fluidity homeostasis).** A central concept in temperature adaptation is that bacteria adjust membrane lipid composition to maintain membrane physical properties. A foundational review describes that bacteria incorporate **“proportionally more unsaturated fatty acids as growth temperature decreases,”** and that microbes **sense decreased membrane fluidity** and induce responses to increase unsaturated fatty-acid biosynthesis. (mendoza2014temperaturesensingby pages 1-2)

**RNA thermometers (RNATs).** RNATs are temperature-sensitive RNA structures in 5′ UTRs that regulate translation by controlling accessibility of the **Shine–Dalgarno (SD)** sequence. A 2023 bacterial temperature-response review summarizes that canonical RNAT families (e.g., **ROSE, FourU**) form inhibitory structures covering SD/AUG at low temperature and **melt upon warming**, relieving translational repression. (moon2023temperaturemattersbacterial pages 3-5)

**Heat-shock sigma factor and proteostasis control.** In many bacteria, the **RpoH (σ32)** regulon coordinates chaperone/protease expression during heat stress. The review evidence emphasizes that **DnaK binds/retains RpoH** under non-stress conditions, heat-denatured proteins titrate DnaK away, and ATP-dependent proteases (e.g., **FtsH, ClpXP**) control RpoH levels. (moon2023temperaturemattersbacterial pages 3-5)

**DNA topology and supercoiling as a temperature-sensitive regulator.** DNA supercoiling changes with temperature and can affect promoter accessibility and transcription. The 2023 review notes cold shock increases negative supercoiling and that the state of supercoiling is tied to **ATP-dependent DNA gyrase** whose efficiency depends on temperature and cellular ATP. (moon2023temperaturemattersbacterial pages 3-5)

### 3) Recent developments and latest research (prioritizing 2023–2024)

#### 3.1 Warm-mesophile–relevant lipid remodeling datasets (2024)

A 2024 **Microbiology Spectrum** paper profiled six clinical **Acinetobacter baumannii** strains under **37 °C vs 18 °C** to quantify lipidomic responses framed explicitly as **homeoviscous adaptation**. The figures show that at 18 °C most strains increase **palmitoleic acid (C16:1)**, while one strain (ABVal2) shows a distinct increase in **oleic acid (C18:1)**. (dessenne2024lipidomicanalysesreveal media c3a19ac9)

The same work reports temperature-dependent remodeling of **glycerophospholipid classes** (e.g., PE, PG) and PE/PG species containing C16:1 or C18:1. (dessenne2024lipidomicanalysesreveal media c3a19ac9)

*Why it matters for METPO:1000446:* While the experiment is a downshift (18 °C) rather than the 34–40 °C optimum band itself, it provides **direct, quantitative, modern evidence** that **host-temperature (37 °C) warm-mesophile physiology** is underpinned by membrane-lipid composition and that temperature shifts elicit predictable FA remodeling. (dessenne2024lipidomicanalysesreveal media c3a19ac9)

#### 3.2 Heat-shock transcriptional network mapping at 42 °C (2024)

A 2024 **PLOS Genetics** systems biology study profiled *Salmonella Typhimurium* under **control 37 °C vs sublethal heat shock 42 °C** and mapped genome-wide binding for three sigma factors at near–1 bp resolution. Under heat shock, the authors report **2,319 RpoD**, **2,226 RpoS**, and **213 RpoH** binding sites. (park2024unveilingthenovel pages 1-2)

They further report **1,353 differentially expressed genes** after heat shock (**713 up**, **640 down**) and show that the **RpoS sigmulon expands from 97 to 301 genes** in response to heat shock, along with sigma-factor competition dynamics between RpoS and RpoD. (park2024unveilingthenovel pages 1-2, park2024unveilingthenovel pages 2-4)

*Relevance to METPO:1000446:* This dataset supports the view that warm-mesophile growth near 37 °C sits adjacent to (and is constrained by) a rapidly engaged stress-response regime at slightly higher temperatures (e.g., 42 °C), implicating sigma-factor network activity as a proximate causal mediator when conditions exceed the optimum. (park2024unveilingthenovel pages 1-2, park2024unveilingthenovel pages 2-4)

#### 3.3 Thermophile boundary-case: reverse gyrase and positive supercoiling (2024)

A 2024 review on thermophile genome organization highlights that **reverse gyrase introduces positive supercoils** and that **“reverse gyrase prevents the thermal denaturation of DNA by introducing positive DNA supercoiling.”** Importantly for scoping, the review states reverse gyrase **“is limited to prokaryotes with an optimal growth temperature higher than 65 °C,”** making it a strong discriminator away from warm-mesophily. (takemata2024howdothermophiles pages 1-2)

### 4) Current applications and real-world implementations

**Clinical microbiology and host-associated pathogens.** The warm-mesophile band (34–40 °C) is directly relevant to pathogens and commensals adapted to mammalian hosts, where **37 °C** is a dominant niche temperature. Modern lipidomics in *A. baumannii* is explicitly motivated by its survival across environmental vs physiological temperatures, demonstrating concrete lipid remodeling associated with 37 °C physiology. (dessenne2024lipidomicanalysesreveal pages 2-4, dessenne2024lipidomicanalysesreveal media c3a19ac9)

**Food safety and heat-shock resilience.** Sublethal heat shock conditions close to (but above) warm-mesophile optima occur in food processing and environmental exposures. The 2024 *Salmonella* systems-biology work demonstrates that repeated or acute exposure near **42 °C** engages global sigma-factor programs (including RpoH and expanded RpoS control) and reshapes gene regulation affecting metabolism and stress resistance—mechanistically relevant to survival during thermal perturbations. (park2024unveilingthenovel pages 1-2, park2024unveilingthenovel pages 2-4)

**Bioprocess control (temperature as a control variable).** A general modeling review in bioprocess contexts emphasizes that temperature is typically controlled at an optimum value and that shifting temperature alters metabolic processes in complex ways, motivating mechanistic graph modeling. (moon2023temperaturemattersbacterial pages 1-3)

### 5) Relevant quantitative statistics and data points (recent studies)

- **Mesophile vs thermophile TOPT ranges:** mesophiles TOPT ~20–45 °C; thermophiles >45 °C. (lehmann2023adaptivelaboratoryevolution pages 1-2)
- **Canonical mesophile example:** *E. coli* optimum at **37 °C**, with poor growth at **44 °C** and fragility near **50 °C** (contextualizing why mid4 ends at 40 °C). (moon2023temperaturemattersbacterial pages 1-3)
- **Lipidomics (A. baumannii) 18 °C vs 37 °C:** multiple strains show increased **C16:1** at 18 °C and one strain increased **C18:1**, with PE/PG species-level quantification shown in figures. (dessenne2024lipidomicanalysesreveal media c3a19ac9)
- **Heat shock network mapping (Salmonella) at 42 °C:** 2,319 (RpoD), 2,226 (RpoS), 213 (RpoH) binding sites under 42 °C; 1,353 DEGs (713 up/640 down); RpoS sigmulon expansion 97→301. (park2024unveilingthenovel pages 1-2, park2024unveilingthenovel pages 2-4)

## Candidate causal-graph content for `data/traits/environment/temperature_optimum_mid4.yaml`

### Candidate nodes (grouped by type; with suggested grounding)

| Node type | Label | Suggested grounding | Brief rationale |
|---|---|---|---|
| Phenotype/assay variables | temperature optimum mid4 (34–40 °C) | METPO:1000446 | Warm-mesophile growth optimum centered near host temperature 37 °C; subset of mesophily (moon2023temperaturemattersbacterial pages 1-3, lehmann2023adaptivelaboratoryevolution pages 1-2) |
| Phenotype/assay variables | optimal growth temperature (TOPT) |  | Cardinal temperature trait used to distinguish mesophiles from thermophiles and quantify shifts (lehmann2023adaptivelaboratoryevolution pages 1-2) |
| Phenotype/assay variables | doubling time at 37 °C |  | Common assay output for host-temperature growth fitness in warm mesophiles (dessenne2024lipidomicanalysesreveal pages 2-4) |
| Phenotype/assay variables | growth under sublethal heat shock (42 °C) |  | Heat-shock condition reveals regulatory systems acting above warm-mesophile optimum (moon2023temperaturemattersbacterial pages 3-5) |
| Environmental variables | 37 °C ambient temperature | ENVO:09200013 | Canonical mammalian-host temperature and reference point for warm-mesophile physiology (moon2023temperaturemattersbacterial pages 1-3, dessenne2024lipidomicanalysesreveal pages 2-4) |
| Environmental variables | temperature downshift |  | Triggers membrane remodeling and increased negative supercoiling responses (moon2023temperaturemattersbacterial pages 3-5, mendoza2014temperaturesensingby pages 1-2) |
| Environmental variables | temperature upshift / heat shock |  | Triggers RNA thermometer melting, RpoH activation, and proteostasis programs (moon2023temperaturemattersbacterial pages 3-5, viuda2025physicalcommunicationpathways pages 5-7) |
| Environmental variables | mammalian host-associated environment | ENVO:01001436 | Explains why many pathogens/commensals center growth near 37 °C (moon2023temperaturemattersbacterial pages 1-3, dessenne2024lipidomicanalysesreveal pages 2-4) |
| Membrane/lipid nodes | membrane fluidity homeostasis / homeoviscous adaptation | GO:0016042 | Core mechanism coupling temperature change to membrane lipid remodeling (mendoza2014temperaturesensingby pages 1-2, moon2023temperaturemattersbacterial pages 3-5) |
| Membrane/lipid nodes | unsaturated fatty acids | CHEBI:27208 | Increased at lower temperature to preserve bilayer fluidity (mendoza2014temperaturesensingby pages 1-2, arsh2025effectsofcooling pages 28-32) |
| Membrane/lipid nodes | saturated fatty acids | CHEBI:26607 | Relative decrease accompanies cold adaptation; ratio versus unsaturated FA is temperature sensitive (moon2023temperaturemattersbacterial pages 3-5, mendoza2014temperaturesensingby pages 1-2) |
| Membrane/lipid nodes | palmitoleic acid (C16:1) | CHEBI:28837 | Increased in most A. baumannii strains at 18 °C versus 37 °C (dessenne2024lipidomicanalysesreveal pages 2-4, dessenne2024lipidomicanalysesreveal media c3a19ac9) |
| Membrane/lipid nodes | oleic acid (C18:1) | CHEBI:16196 | Alternative unsaturated FA increased in one strain during cold adaptation (dessenne2024lipidomicanalysesreveal pages 2-4, dessenne2024lipidomicanalysesreveal media c3a19ac9) |
| Membrane/lipid nodes | phosphatidylethanolamine (PE) | CHEBI:16038 | Major GPL class remodeled across temperatures in clinical warm-mesophile strains (dessenne2024lipidomicanalysesreveal pages 2-4, dessenne2024lipidomicanalysesreveal media c3a19ac9) |
| Membrane/lipid nodes | phosphatidylglycerol (PG) | CHEBI:17517 | Temperature-responsive GPL class contributing to homeoviscous adaptation (dessenne2024lipidomicanalysesreveal pages 2-4, dessenne2024lipidomicanalysesreveal media c3a19ac9) |
| Membrane/lipid nodes | plasmalogens | CHEBI:35715 | Increased in evolved lower-TOPT thermophile, suggesting lipid-class contribution to optimum shifts (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7) |
| Membrane/lipid nodes | FabG (3-oxoacyl-ACP reductase) | EC:1.1.1.100 | Fatty-acid biosynthesis enzyme mutated in temperature-adapted lineage (lehmann2023adaptivelaboratoryevolution pages 6-7) |
| RNA thermoregulation nodes | RNA thermometer (RNAT) | GO:0030371 | Temperature-sensitive 5′-UTR structure controlling translation initiation (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 1-3) |
| RNA thermoregulation nodes | ROSE RNA thermometer |  | Canonical inhibitory hairpin class for heat-responsive translation control (moon2023temperaturemattersbacterial pages 3-5) |
| RNA thermoregulation nodes | FourU RNA thermometer |  | Heat-labile 5′-UTR motif that exposes the ribosome binding site on warming (moon2023temperaturemattersbacterial pages 3-5) |
| RNA thermoregulation nodes | Shine–Dalgarno sequence accessibility | GO:0006413 | Direct translational output altered by RNA thermometer melting (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 1-3) |
| Proteostasis/heat shock nodes | heat shock response | GO:0009408 | Protects proteins from denaturation as cells exceed warm-mesophile optimum (moon2023temperaturemattersbacterial pages 3-5, viuda2025physicalcommunicationpathways pages 5-7) |
| Proteostasis/heat shock nodes | RpoH (sigma-32) |  | Major bacterial heat-shock sigma factor controlling chaperone/protease regulons (moon2023temperaturemattersbacterial pages 3-5, viuda2025physicalcommunicationpathways pages 5-7) |
| Proteostasis/heat shock nodes | DnaK |  | Binds and restrains RpoH under non-stress conditions; central chaperone in heat response (moon2023temperaturemattersbacterial pages 3-5) |
| Proteostasis/heat shock nodes | DnaJ |  | Canonical cochaperone in the DnaK system and heat-response regulon member (moon2023temperaturemattersbacterial pages 14-15) |
| Proteostasis/heat shock nodes | GrpE |  | Nucleotide-exchange factor in DnaK chaperone system; heat-shock machinery component (moon2023temperaturemattersbacterial pages 14-15) |
| Proteostasis/heat shock nodes | GroEL/GroES |  | Major folding chaperone system induced during heat stress (moon2023temperaturemattersbacterial pages 14-15) |
| Proteostasis/heat shock nodes | FtsH protease |  | ATP-dependent protease controlling RpoH abundance (moon2023temperaturemattersbacterial pages 3-5) |
| Proteostasis/heat shock nodes | ClpXP protease |  | ATP-dependent protease contributing to sigma-factor/protein quality control (moon2023temperaturemattersbacterial pages 3-5) |
| Proteostasis/heat shock nodes | denatured proteins | GO:0042597 | Heat-generated substrate load that titrates DnaK and activates stress response (moon2023temperaturemattersbacterial pages 3-5) |
| DNA topology nodes | DNA supercoiling | GO:0065004 | Temperature-sensitive genome property coupling thermal change to transcription (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5) |
| DNA topology nodes | negative DNA supercoiling |  | Enhanced during cold stress; influences promoter accessibility and transcription (moon2023temperaturemattersbacterial pages 3-5) |
| DNA topology nodes | DNA gyrase |  | ATP-dependent enzyme modulating supercoiling during thermal transitions (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5) |
| DNA topology nodes | topoisomerase I |  | Works with gyrase to relax supercoils after heat shock (moon2023temperaturemattersbacterial pages 1-3) |
| DNA topology nodes | reverse gyrase |  | Positive-supercoiling topoisomerase associated with thermophily, not typical warm-mesophile state (lehmann2023adaptivelaboratoryevolution pages 6-7, lehmann2023adaptivelaboratoryevolution pages 1-2) |
| DNA topology nodes | positive DNA supercoiling |  | High-temperature DNA-protective state emphasized in thermophiles (moon2023temperaturemattersbacterial pages 14-15, lehmann2023adaptivelaboratoryevolution pages 6-7) |
| Regulatory/signaling nodes | membrane thermosensing |  | Membrane physical state acts as primary temperature sensor upstream of lipid adaptation (mendoza2014temperaturesensingby pages 1-2) |
| Regulatory/signaling nodes | ATP/ADP ratio | CHEBI:15422 / CHEBI:16761 | Energy charge modulates gyrase activity and thus temperature-linked supercoiling (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5) |
| Regulatory/signaling nodes | SigH (alternative sigma factor H) |  | Mutated in adapted lineage; possible taxon-specific contributor to temperature adaptation (lehmann2023adaptivelaboratoryevolution pages 6-7) |
| Regulatory/signaling nodes | transcriptional regulatory network under heat shock | GO:0006355 | Multi-sigma coordination at 42 °C expands stress-responsive gene control (moon2023temperaturemattersbacterial pages 14-15) |
| Regulatory/signaling nodes | membrane phospholipid composition | GO:0006644 | Integrative state variable connecting lipid metabolism to thermal fitness near 37 °C (mendoza2014temperaturesensingby pages 1-2, dessenne2024lipidomicanalysesreveal pages 2-4) |


*Table: This table lists candidate nodes for a causal graph of temperature optimum mid4 (34–40 °C), grouped by biological type and annotated with suggested ontology grounding where possible. It is useful as a starting curation inventory linking warm-mesophile growth to membrane adaptation, RNA thermoregulation, proteostasis, and DNA topology.*

### Candidate evidence-backed edges (triples with snippets and curation notes)

| Edge (S–P–O) | Evidence snippet | Source (DOI, year, URL) | Evidence strength | Curation notes |
|---|---|---|---|---|
| Temperature downshift → increases → unsaturated fatty acid proportion | “bacteria perform homoviscous adaptation by incorporating proportionally more unsaturated fatty acids as growth temperature decreases” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza 2014. DOI: 10.1146/annurev-micro-091313-103612. https://doi.org/10.1146/annurev-micro-091313-103612 | strong | Broad review; direct mechanistic claim; general bacteria, not specific to mid4 alone. |
| Increased unsaturated fatty acids → maintains/enhances → membrane fluidity homeostasis | “thereby disrupting bilayer order and optimizing cellular processes at the new temperature” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza 2014. DOI: 10.1146/annurev-micro-091313-103612. https://doi.org/10.1146/annurev-micro-091313-103612 | strong | Direct mechanistic membrane-adaptation edge; foundational evidence. |
| Decreased membrane fluidity → induces → unsaturated fatty acid biosynthesis response | “Microbes sense decreases in membrane fluidity and initiate responses that upregulate biosynthesis of unsaturated fatty acids” (mendoza2014temperaturesensingby pages 1-2) | de Mendoza 2014. DOI: 10.1146/annurev-micro-091313-103612. https://doi.org/10.1146/annurev-micro-091313-103612 | strong | Direct causal thermosensing edge; useful upstream of FA nodes. |
| Temperature change → alters → saturated/unsaturated fatty-acid ratio | “temperature shifts modulate membrane stability by altering the ratio of saturated versus unsaturated fatty acids” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | General bacterial response; direct mechanistic summary. |
| Growth at 18°C vs 37°C in A. baumannii → increases → palmitoleic acid (C16:1) in most strains | “at 18°C, most strains (ABVal1, ABVal3, ABVal4, ABVal5, and AB5075) exhibit a significant increase in palmitoleic acid (C16:1)” (dessenne2024lipidomicanalysesreveal media c3a19ac9) | Dessenne et al. 2024. DOI: 10.1128/spectrum.00757-24. https://doi.org/10.1128/spectrum.00757-24 | strong | Figure-based primary evidence; taxon- and assay-specific (18 vs 37°C lipidomics), but highly concrete. |
| Growth at 18°C vs 37°C in ABVal2 → increases → oleic acid (C18:1) | “ABVal2 shows a distinctive increase in oleic acid (C18:1)” (dessenne2024lipidomicanalysesreveal media c3a19ac9) | Dessenne et al. 2024. DOI: 10.1128/spectrum.00757-24. https://doi.org/10.1128/spectrum.00757-24 | moderate | Primary evidence; strain-specific boundary case showing alternative unsaturated FA strategy. |
| Growth at 18°C vs 37°C → remodels → PE and PG lipid species | “Figure 4… quantifies the percentages of PE and PG lipid species containing at least one C16:1 or C18:1 fatty acid” (dessenne2024lipidomicanalysesreveal media c3a19ac9) | Dessenne et al. 2024. DOI: 10.1128/spectrum.00757-24. https://doi.org/10.1128/spectrum.00757-24 | moderate | Figure-derived lipid-class remodeling edge; taxon-specific but mechanistically relevant. |
| RNA thermometer hairpin → occludes → Shine–Dalgarno/AUG sequence | “ROSE and FourU RNA thermometers form inhibitory hairpins that cover Shine–Dalgarno/AUG” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Direct mechanistic translational-control edge; general bacterial. |
| Heat shock / temperature upshift → melts → RNA thermometer structure | “are stable at low temperatures but undergo conformational change (melting) at heat shock” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Direct mechanistic edge linking temperature to post-transcriptional control. |
| RNA thermometer melting → exposes/enables → ribosome binding and translation initiation | “releasing translation inhibition” (moon2023temperaturemattersbacterial pages 3-5); “melting at 37°C allows ribosome binding and translation initiation” paraphrased from host-temperature RNAT summary (viuda2025physicalcommunicationpathways pages 5-7) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x; de la Viuda et al. 2025 summary context (viuda2025physicalcommunicationpathways pages 5-7) | strong | Direct mechanism; use Moon as primary curation source, extra support from cross-review context. |
| Heat-denatured proteins → displace/titrate → DnaK from RpoH | “DnaK binds and retains RpoH until heat-denatured proteins displace it” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Core heat-shock regulatory mechanism; direct causal edge. |
| DnaK → negatively regulates/retains → RpoH | “DnaK binds and retains RpoH” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Canonical chaperone–sigma interaction; direct mechanistic edge. |
| FtsH protease → controls abundance of → RpoH | “ATP-dependent proteases FtsH and ClpXP control RpoH protein levels” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Direct regulatory edge; proteostasis node useful for graph. |
| ClpXP protease → controls abundance of → RpoH | “ATP-dependent proteases FtsH and ClpXP control RpoH protein levels” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Direct regulatory edge; broad bacterial mechanism. |
| Sublethal heat shock at 42°C → increases activity/binding of → RpoS and RpoH regulons | “RpoS and RpoH iModulon activities increase under heat shock” and experiments “performed at 42°C” (park2024unveilingthenovel pages 4-5) | Park et al. 2024. DOI: 10.1371/journal.pgen.1011464. https://doi.org/10.1371/journal.pgen.1011464 | strong | Primary systems-biology evidence; assay-specific to Salmonella at 42°C, informative as above-optimum perturbation. |
| Heat shock at 42°C → expands → RpoS sigmulon | “a notable expansion of the RpoS regulon (sigmulon) from 97 to 301 genes in response to heat shock” (park2024unveilingthenovel pages 1-2) | Park et al. 2024. DOI: 10.1371/journal.pgen.1011464. https://doi.org/10.1371/journal.pgen.1011464 | strong | Primary genome-wide evidence; taxon-specific but direct. |
| Temperature downshift in evolved thermophile lineage → increases → plasmalogens | “Adpt45_67 shows increased plasmalogen levels” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Lehmann et al. 2023. DOI: 10.3389/fmicb.2023.1265216. https://doi.org/10.3389/fmicb.2023.1265216 | moderate | Primary evidence for lipid-class contribution to TOPT shift; taxon-specific thermophile-to-lower-T adaptation, not warm-mesophile native state. |
| Decreasing temperature → reduces → fatty-acyl chain length | “reduction in chain length with decreasing temperature” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Lehmann et al. 2023. DOI: 10.3389/fmicb.2023.1265216. https://doi.org/10.3389/fmicb.2023.1265216 | moderate | Direct membrane-remodeling edge; thermophile ALE context, uncertain generalizability. |
| Cold shock / temperature downshift → enhances → negative DNA supercoiling | “cold shock enhances negative supercoiling and DNA condensation” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Direct topology response to low temperature; more relevant to lower-than-mid4 perturbation. |
| ATP-dependent DNA gyrase → mediates → temperature-sensitive DNA supercoiling changes | “negative supercoiling depends on ATP-dependent DNA gyrase whose efficiency is temperature- and ATP-sensitive” (moon2023temperaturemattersbacterial pages 3-5) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | strong | Direct mechanistic edge linking energy state, temperature, and topology. |
| Heat shock → increases ATP/ADP ratio → activates DNA gyrase | “Changes in cellular [ATP]/[ADP] during heat shock activate ATP-dependent DNA gyrase” (moon2023temperaturemattersbacterial pages 1-3) | Moon et al. 2023. DOI: 10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x | moderate | Mechanistically useful but phrased as review synthesis; indirect for mid4 optimum itself. |
| Reverse gyrase → introduces → positive DNA supercoils | “a unique topoisomerase that introduces positive supercoils into DNA” (takemata2024howdothermophiles pages 1-2) | Takemata 2024. DOI: 10.1264/jsme2.me23087. https://doi.org/10.1264/jsme2.me23087 | strong | Thermophile boundary-case; important negative/discriminating node for separating warm mesophiles from >65°C thermophiles. |
| Reverse gyrase-mediated positive supercoiling → prevents → thermal DNA denaturation | “reverse gyrase prevents the thermal denaturation of DNA by introducing positive DNA supercoiling” (takemata2024howdothermophiles pages 1-2) | Takemata 2024. DOI: 10.1264/jsme2.me23087. https://doi.org/10.1264/jsme2.me23087 | strong | Direct thermophile mechanism; likely should be curated as boundary-case/contrast, not core warm-mesophile mechanism. |
| Optimal growth temperature >65°C → associates with → reverse gyrase presence | “is limited to prokaryotes with an optimal growth temperature higher than 65°C” (takemata2024howdothermophiles pages 1-2) | Takemata 2024. DOI: 10.1264/jsme2.me23087. https://doi.org/10.1264/jsme2.me23087 | strong | Discriminative edge against warm-mesophile trait; helpful warning for graph scope. |


*Table: This table lists evidence-backed candidate causal edges for a warm-mesophile temperature-optimum graph, spanning membrane remodeling, RNA thermometers, heat-shock regulation, DNA topology, and thermophile boundary-case mechanisms. It is useful as a curation-ready starting set for selecting edges to include or exclude in temperature_optimum_mid4.yaml.*

### Expert synthesis: mechanistic interpretation for mid4 (34–40 °C)

A defensible “core mechanism set” for warm-mesophile optimal growth is that the mid4 optimum emerges when **(i) membrane physical state and permeability** are tuned for efficient transport and enzyme function (via homeoviscous adaptation and lipid remodeling), **(ii) translation and proteostasis** remain below a threshold where denaturation-driven demand overwhelms folding systems, and **(iii) DNA topology/transcriptional programs** remain in a supercoiling regime that supports the organism’s promoter architecture and regulatory network. The cited sources collectively support each axis as temperature-causal, and show that mild excursions above the optimum (e.g., 42 °C) activate alternative sigma-factor programs that can impose growth trade-offs. (mendoza2014temperaturesensingby pages 1-2, moon2023temperaturemattersbacterial pages 3-5, park2024unveilingthenovel pages 1-2)

## Warnings / not-yet-curatable claims

1. **Reverse gyrase edges should generally not be curated as mid4 causal mechanisms** because reverse gyrase is strongly associated with **optimal growth temperature >65 °C** thermophiles, i.e., outside warm-mesophile scope; it is best curated as a **boundary-case discriminator**. (takemata2024howdothermophiles pages 1-2)
2. **Strain- and taxon-specific lipid details** (e.g., which unsaturated FA increases) should be tagged as **context-specific**, since *A. baumannii* shows both shared and strain-specific remodeling strategies (C16:1 vs C18:1). (dessenne2024lipidomicanalysesreveal media c3a19ac9)
3. **42 °C heat-shock sigma-factor rewiring** is a powerful mechanistic dataset, but it reflects **above-optimum perturbation** rather than the optimum itself; edges derived from it should be curated as **“temperature upshift/heat shock response”** edges rather than “determinants of optimum” unless coupled to growth-rate data in the same experimental context. (park2024unveilingthenovel pages 1-2)

## DOI-first bibliography (with URLs and dates)

> DOI: https://doi.org/10.1007/s12275-023-00031-x — Mar 2023 — Moon S, Ham S, Jeong J, Ku H, Kim H, Lee C. *Temperature Matters: Bacterial Response to Temperature Change*. *Journal of Microbiology* — review covering membrane fatty-acid remodeling, RNA thermometers, RpoH/DnaK regulation, and DNA supercoiling responses to temperature shifts. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)
>
> DOI: https://doi.org/10.1128/spectrum.00757-24 — Oct 2024 — Dessenne C, Ménart B, Acket S, Dewulf G, Guerardel Y, Vidal O, Rossez Y. *Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii, providing insights from an environmental adaptation perspective*. *Microbiology Spectrum* — primary 18°C vs 37°C lipidomics evidence for C16:1/C18:1 and PE/PG remodeling in a warm-mesophile-associated pathogen. (dessenne2024lipidomicanalysesreveal pages 2-4, dessenne2024lipidomicanalysesreveal pages 1-2, dessenne2024lipidomicanalysesreveal media c3a19ac9)
>
> DOI: https://doi.org/10.1371/journal.pgen.1011464 — Oct 2024 — Park JY, Jang M, Lee S-M, Woo J, Lee E-J, Kim D. *Unveiling the novel regulatory roles of RpoD-family sigma factors in Salmonella Typhimurium heat shock response through systems biology approaches*. *PLOS Genetics* — primary systems-biology study mapping sigma-factor binding and regulon changes under sublethal heat shock at 42°C. (park2024unveilingthenovel pages 1-2, park2024unveilingthenovel pages 4-5, park2024unveilingthenovel pages 2-4)
>
> DOI: https://doi.org/10.1264/jsme2.me23087 — Jun 2024 — Takemata N. *How Do Thermophiles Organize Their Genomes?* *Microbes and Environments* — review establishing reverse gyrase and positive supercoiling as hallmark high-temperature DNA-protection mechanisms, useful as a thermophile boundary case against warm mesophily. (takemata2024howdothermophiles pages 2-3, takemata2024howdothermophiles pages 1-2)
>
> DOI: https://doi.org/10.3389/fmicb.2023.1265216 — Oct 2023 — Lehmann M, Prohaska C, Zeldes B, Poehlein A, Daniel R, Basen M. *Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum*. *Frontiers in Microbiology* — experimental evidence that temperature-optimum shifts can involve plasmalogens, shorter fatty-acyl chains, and mutations including fabG and regulatory loci. (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7)
>
> DOI: https://doi.org/10.1146/annurev-micro-091313-103612 — Sep 2014 — de Mendoza D. *Temperature sensing by membranes*. *Annual Review of Microbiology* — foundational review of membrane thermosensing and homeoviscous adaptation via increased unsaturated fatty acids at lower growth temperatures. (mendoza2014temperaturesensingby pages 1-2)


*Blockquote: This blockquote lists the core sources used to support the temperature_optimum_mid4 curation, with DOI URLs, dates, and one-line relevance notes. It is useful as a compact, curation-ready bibliography focused on the main mechanistic evidence.*


References

1. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

2. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

3. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

4. (mendoza2014temperaturesensingby pages 1-2): Diego de Mendoza. Temperature sensing by membranes. Annual review of microbiology, 68:101-16, Sep 2014. URL: https://doi.org/10.1146/annurev-micro-091313-103612, doi:10.1146/annurev-micro-091313-103612. This article has 209 citations and is from a peer-reviewed journal.

5. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

6. (dessenne2024lipidomicanalysesreveal media c3a19ac9): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

7. (park2024unveilingthenovel pages 1-2): Joon Young Park, Minchang Jang, Sang-Mok Lee, Jihoon Woo, Eun-Jin Lee, and Donghyuk Kim. Unveiling the novel regulatory roles of rpod-family sigma factors in salmonella typhimurium heat shock response through systems biology approaches. Oct 2024. URL: https://doi.org/10.1371/journal.pgen.1011464, doi:10.1371/journal.pgen.1011464. This article has 12 citations and is from a domain leading peer-reviewed journal.

8. (park2024unveilingthenovel pages 2-4): Joon Young Park, Minchang Jang, Sang-Mok Lee, Jihoon Woo, Eun-Jin Lee, and Donghyuk Kim. Unveiling the novel regulatory roles of rpod-family sigma factors in salmonella typhimurium heat shock response through systems biology approaches. Oct 2024. URL: https://doi.org/10.1371/journal.pgen.1011464, doi:10.1371/journal.pgen.1011464. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (dessenne2024lipidomicanalysesreveal pages 2-4): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

10. (viuda2025physicalcommunicationpathways pages 5-7): Virgilio de la Viuda, Javier Buceta, and Iago Grobas. Physical communication pathways in bacteria: an extra layer to quorum sensing. Biophysical Reviews, 17:667-685, Mar 2025. URL: https://doi.org/10.1007/s12551-025-01290-1, doi:10.1007/s12551-025-01290-1. This article has 9 citations and is from a peer-reviewed journal.

11. (arsh2025effectsofcooling pages 28-32): Amir M. Arsh, Miguel M. Azevedo, and Andre S. Ribeiro. Effects of cooling on <i>e. coli</i> ’s dna organization, structure, and gene expression. Microbiology and Molecular Biology Reviews, Dec 2025. URL: https://doi.org/10.1128/mmbr.00153-25, doi:10.1128/mmbr.00153-25. This article has 0 citations and is from a domain leading peer-reviewed journal.

12. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

13. (moon2023temperaturemattersbacterial pages 14-15): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

14. (park2024unveilingthenovel pages 4-5): Joon Young Park, Minchang Jang, Sang-Mok Lee, Jihoon Woo, Eun-Jin Lee, and Donghyuk Kim. Unveiling the novel regulatory roles of rpod-family sigma factors in salmonella typhimurium heat shock response through systems biology approaches. Oct 2024. URL: https://doi.org/10.1371/journal.pgen.1011464, doi:10.1371/journal.pgen.1011464. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

16. (takemata2024howdothermophiles pages 2-3): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.