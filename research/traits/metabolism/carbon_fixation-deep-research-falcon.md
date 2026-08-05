---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:40:42.051779'
end_time: '2026-08-04T05:57:27.183301'
duration_seconds: 1005.13
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: carbon fixation
  trait_identifier: traitmech:000019
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: carbon_fixation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolic process in which an organism assimilates inorganic carbon
    (CO2 or bicarbonate) into organic compounds (autotrophy). Six distinct natural
    autotrophic carbon-fixation pathways are currently recognized.
  parent_traits: METPO:1000060
  synonyms: CO2 fixation, autotrophic carbon assimilation
  evidence_summary: "DOI:10.1128/AEM.02473-10:  (Berg review of the distribution of\
    \ autotrophic CO2-fixation pathways establishes that, besides the Calvin-Benson-Bassham\
    \ cycle, five further autotrophic carbon-fixation pathways are known, parent of\
    \ the six pathway sub-variants proposed here.) | DOI:10.1146/annurev-marine-120709-142712:\
    \  (H\xFCgler & Sievert, \"Beyond the Calvin cycle\", supports multiple autotrophic\
    \ carbon-fixation pathways operating among ocean microorganisms.)"
  causal_graph_summary: 'carbon_fixation_co2_assimilation: 15 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carbon fixation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000019
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolic process in which an organism assimilates inorganic carbon (CO2 or bicarbonate) into organic compounds (autotrophy). Six distinct natural autotrophic carbon-fixation pathways are currently recognized.
- **Parent traits:** METPO:1000060
- **Synonyms:** CO2 fixation, autotrophic carbon assimilation
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review of the distribution of autotrophic CO2-fixation pathways establishes that, besides the Calvin-Benson-Bassham cycle, five further autotrophic carbon-fixation pathways are known, parent of the six pathway sub-variants proposed here.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert, "Beyond the Calvin cycle", supports multiple autotrophic carbon-fixation pathways operating among ocean microorganisms.)
- **Existing causal graph summary:** carbon_fixation_co2_assimilation: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **carbon fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/carbon_fixation.yaml`.

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
- **Trait label:** carbon fixation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000019
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolic process in which an organism assimilates inorganic carbon (CO2 or bicarbonate) into organic compounds (autotrophy). Six distinct natural autotrophic carbon-fixation pathways are currently recognized.
- **Parent traits:** METPO:1000060
- **Synonyms:** CO2 fixation, autotrophic carbon assimilation
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review of the distribution of autotrophic CO2-fixation pathways establishes that, besides the Calvin-Benson-Bassham cycle, five further autotrophic carbon-fixation pathways are known, parent of the six pathway sub-variants proposed here.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert, "Beyond the Calvin cycle", supports multiple autotrophic carbon-fixation pathways operating among ocean microorganisms.)
- **Existing causal graph summary:** carbon_fixation_co2_assimilation: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **carbon fixation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/carbon_fixation.yaml`.

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


# Curation report: microbial carbon fixation

## 1. Trait record and scope

- **Trait:** carbon fixation
- **Identifier:** **traitmech:000019**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** METPO:1000060
- **Synonyms:** CO2 fixation; autotrophic carbon assimilation

### Recommended scope

The trait should represent the **physiological capacity for net assimilation of inorganic carbon—CO2 and/or bicarbonate—into central organic metabolites and biomass through an autotrophic pathway**. Reduction of CO2 to average cellular carbon requires reducing equivalents and energy, usually ATP; a carboxylase links CO2 or HCO3− to an organic acceptor that the pathway regenerates. Carbon-species availability is pH dependent, with bicarbonate favored under mildly alkaline conditions such as seawater. (berg2011ecologicalaspectsof pages 1-2)

For compatibility with the reviewed definition and existing graph, retain the classical six natural autotrophic pathways as child mechanisms:

1. Calvin–Benson–Bassham cycle (CBB)
2. reductive tricarboxylic-acid cycle (rTCA)
3. Wood–Ljungdahl/reductive acetyl-CoA pathway (WL)
4. 3-hydroxypropionate bicycle (3HP bicycle)
5. 3-hydroxypropionate/4-hydroxybutyrate cycle (3HP/4HB)
6. dicarboxylate/4-hydroxybutyrate cycle (DC/4HB)

Berg’s authoritative review states: “Besides the well-known Calvin-Benson cycle, five other totally different autotrophic mechanisms are known today.” A 2024 Great Salt Lake study used the same six-pathway classification when screening metagenome-assembled genomes. (berg2011ecologicalaspectsof pages 1-2, shoemaker2024wood–ljungdahlpathwayencoding pages 2-3)

### Boundary cases

- **Exclude anaplerotic fixation alone.** Carboxylation by phosphoenolpyruvate carboxylase, pyruvate carboxylase, or related enzymes can replenish central-metabolic intermediates in heterotrophs without supporting autotrophic growth.
- **Do not infer the trait from `rbcL` or another marker alone.** A recent genome survey explicitly warns that CBB genes do not necessarily establish autotrophic growth; in some aerobic anoxygenic phototrophs the cycle supplements heterotrophic metabolism. (nishihara2025exploringthediversity pages 5-8)
- **Distinguish fixation from an electron-balancing sink.** In some purple photoheterotrophs the CBB cycle consumes excess reducing power rather than establishing autotrophic carbon assimilation. (berg2011ecologicalaspectsof pages 2-3)
- **Exclude dissimilatory CO2 reduction by itself.** Methanogenesis or other CO2-reducing energy metabolism does not necessarily assimilate carbon into biomass through one of the trait’s pathways.
- **Exclude carbon capture, storage, and sequestration as environmental outcomes** unless organism-level inorganic-carbon assimilation is demonstrated.
- **Partial or engineered pathways** may be represented as experimental mechanisms, but they should not automatically imply the organism-level autotrophic trait.
- **Pathway-count warning:** newer literature sometimes describes seven or eight mechanisms by adding the reductive glycine pathway and/or reverse oxidative TCA variant. These should be modeled as proposed extensions rather than silently changing the reviewed six-pathway definition. (nishihara2025exploringthediversity pages 1-5, li2024productionofsuccinate pages 1-2)

## 2. Current mechanistic understanding

The CBB cycle is quantitatively dominant and unusually tolerant of oxygen, but Rubisco is slow, has limited CO2 affinity, and also catalyzes an oxygenase reaction that generates 2-phosphoglycolate. Berg reported a Rubisco turnover range of approximately 1–12 s−1 and explained why carbon-concentrating mechanisms are advantageous. (berg2011ecologicalaspectsof pages 2-3)

Anaerobic pathways commonly exploit low-potential reduced ferredoxin, whereas aerobic pathways more often use NAD(P)H. Reviews consequently classify CBB, 3HP, and 3HP/4HB as broadly oxygen-compatible and rTCA, WL, and DC/4HB as anaerobic or microaerobic, although this is a pathway-level generalization rather than an absolute taxonomic rule. The WL and DC/4HB mechanisms contain especially oxygen-sensitive chemistry. (liang2020recentadvancesin pages 3-5, liang2020recentadvancesin pages 1-2)

A 2025 computational—not experimental—comparison concluded that anaerobic pathways generally incur lower ATP costs and that rTCA and WL are efficient across broad simulated CO2 and H2 conditions. This is useful expert guidance for graph interpretation and engineering prioritization, but not evidence that a particular organism expresses those pathways in vivo. (taha2025bioenergetictradeoffscan pages 1-2)

## 3. Candidate nodes

### Trait and biological-process nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| carbon fixation | **traitmech:000019**; GO:0015977 | Root trait/process; preserve supplied CURIE verbatim. |
| autotrophic growth | GO label candidate | Phenotypic outcome; require growth or biomass-assimilation evidence. |
| carbon-concentrating mechanism | Label-only candidate | Mechanistic module supporting CBB fixation, especially in cyanobacteria. |
| photorespiration | GO:0009853 | Competing/consequent process caused by Rubisco oxygenation. |
| inorganic-carbon sensing | Label-only candidate | Regulatory module, not fixation itself. |

### Pathway/module nodes

Use label-only nodes unless the project’s selected pathway ontology has been validated:

- Calvin–Benson–Bassham cycle
- reductive TCA cycle
- Wood–Ljungdahl pathway
- 3-hydroxypropionate bicycle
- 3-hydroxypropionate/4-hydroxybutyrate cycle
- dicarboxylate/4-hydroxybutyrate cycle
- reductive glycine pathway — **proposed extension/uncertain relative to current trait definition**
- partial engineered 3HP pathway — **assay-specific module, not equivalent to natural autotrophy**

### Genes, proteins, enzymes, and complexes

| Node | Suggested grounding | Function in graph |
|---|---|---|
| `rbcL`, `rbcS`; Rubisco | EC:4.1.1.39; GO:0016984 | RuBP carboxylation; key CBB enzyme. |
| phosphoribulokinase | EC:2.7.1.19 | Regenerates RuBP in CBB. |
| CO dehydrogenase/acetyl-CoA synthase complex | Label/EC candidates pending reaction-level validation | Key WL carbonyl-branch and acetyl-CoA-forming machinery; oxygen sensitive. |
| ATP-citrate lyase / citryl-CoA module | Label-only pending taxon-specific pathway validation | Diagnostic rTCA machinery in relevant taxa. |
| acetyl-CoA carboxylase (ACC) | EC:6.4.1.2 | Bicarbonate-fixing enzyme in 3HP chemistry. |
| propionyl-CoA carboxylase (PCC) | EC:6.4.1.3 | Second engineered 3HP-bypass carboxylation. |
| SbtA | transporter label/UniProt per strain | Medium-affinity, low-flux Na+/HCO3− symporter. |
| BicA | transporter label/UniProt per strain | Low-affinity, high-flux Na+/HCO3− symporter. |
| BCT1; `cmp` operon | ABC-transporter label | ATP-driven, high-affinity bicarbonate uptake. |
| NDH-1₃/CupA and NDH-1₄/CupB | complex labels | Cyanobacterial CO2 uptake and cytoplasmic conversion to bicarbonate. |
| carbonic anhydrase | GO:0004089; EC:4.2.1.1 | Interconverts CO2 and bicarbonate; carboxysomal forms supply CO2 to Rubisco. |
| CcmR/NdhR | label/strain-specific UniProt | Represses CCM genes under high CO2. |
| CyAbrB2, CmpR, RbcR | label/strain-specific UniProt | CCM transcriptional regulators. |
| SbtB | label/strain-specific UniProt | PII-like signaling protein associated with `sbtA`. |

### Cellular structures/localizations

- **Carboxysome:** protein-shell bacterial microcompartment containing Rubisco, carbonic anhydrase, and auxiliary proteins.
- **Cytoplasmic membrane:** location of SbtA, BicA, BCT1, and specialized NDH-1 uptake systems.
- **Cytoplasm:** location of most CBB reactions and the intracellular bicarbonate pool.
- **Carboxysome lumen:** localized conversion of bicarbonate to CO2 and Rubisco carboxylation.

Alpha-carboxysomes contain form IA Rubisco and CsoSCA; beta-carboxysomes contain form IB Rubisco and either the CcmM carbonic-anhydrase domain or CcaA. These subtype relations are robust but should be curated taxon-specifically. (kurkela2024inorganiccarbonsensing pages 3-4)

### Chemicals and environmental factors

| Node | Grounding/status | Mechanistic relevance |
|---|---|---|
| carbon dioxide | CHEBI:16526 | Inorganic-carbon substrate. |
| bicarbonate | CHEBI:17544 | Transported inorganic-carbon substrate; favored at alkaline pH. |
| oxygen | CHEBI:15379 | Competes at Rubisco and inhibits oxygen-sensitive anaerobic enzymes. |
| ribulose 1,5-bisphosphate | ChEBI identifier should be registry-verified | Rubisco acceptor substrate. |
| 3-phosphoglycerate | ChEBI identifier should be registry-verified | Product of CBB carboxylation. |
| 2-phosphoglycolate | ChEBI identifier should be registry-verified | Rubisco oxygenation product and low-Ci signal. |
| ATP, NADPH, reduced ferredoxin | Registry-verified CHEBI terms | Energy and reducing-power inputs. |
| sodium ion | CHEBI identifier should be registry-verified | Supports SbtA/BicA symport and cyanobacterial bicarbonate influx. |
| low inorganic carbon | Environmental/experimental label | Induces CCM acclimation. |
| high CO2 | Experimental-condition label | Relieves carboxysome/CCM dependence and represses uptake genes. |
| alkaline pH | ENVO/condition label pending validation | Raises bicarbonate relative to dissolved CO2. |
| anoxia / microoxia | ENVO terms pending validation | Permits oxygen-sensitive pathways. |
| hypersaline sediment | ENVO label pending validation | Ecological context associated with WL selection in the Great Salt Lake study. |
| light | Environmental factor | Supplies energy/reducing power in phototrophic fixation; absence defines dark fixation assays. |
| H2, reduced sulfur, Fe(II), NH3 | Chemical/electron-donor labels | Potential energy sources for chemolithoautotrophy; edges must be curated by taxon and pathway. |

## 4. Candidate evidence-backed causal edges

The following table emphasizes edges sufficiently concrete for YAML curation. “Strong” means the mechanism is established, although some cited papers are reviews synthesizing the primary experiments.

| Subject | Predicate | Object | Supporting snippet | Reference and evidence note |
|---|---|---|---|---|
| CBB cycle | `has_key_enzyme` | Rubisco | “The key CB cycle enzyme, RubisCO…” | DOI:10.1128/AEM.02473-10; foundational review. (berg2011ecologicalaspectsof pages 2-3) |
| Rubisco | `catalyzes` | RuBP + CO2 → two 3-phosphoglycerate | “Rubisco catalyses the fixation of CO2 to…RuBP by forming two molecules of 3-phosphoglycerate.” | DOI:10.1111/ppl.14140; 2024 review. (kurkela2024inorganiccarbonsensing pages 3-4) |
| O2 | `competes_with` | CO2 at Rubisco | Rubisco “functions both as a carboxylase and an oxygenase.” | DOI:10.1111/ppl.14140; strong general mechanism. (kurkela2024inorganiccarbonsensing pages 1-2) |
| Rubisco oxygenase activity | `produces` | 2-phosphoglycolate | “If RuBisCo uses O2 as a substrate, the resulting 2-phosphoglycolate…is metabolized via photorespiration.” | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 2-3) |
| SbtA | `transports` | HCO3− into cytoplasm | “BicA and SbtA transporters function as Na+/HCO3 symporters.” | DOI:10.1111/ppl.14140; cyanobacteria-specific. (kurkela2024inorganiccarbonsensing pages 2-3) |
| BicA | `transports` | HCO3− into cytoplasm | Same snippet; BicA is described as “low affinity, high flux.” | DOI:10.1111/ppl.14140; cyanobacteria-specific. (kurkela2024inorganiccarbonsensing pages 2-3) |
| Na+ gradient | `supports` | SbtA/BicA bicarbonate influx | The symporters require “at least 1 mM Na+ concentration to function.” | DOI:10.1111/ppl.14140; condition may vary by system. (kurkela2024inorganiccarbonsensing pages 2-3) |
| BCT1 | `actively_transports` | HCO3− into cytoplasm | “an ABC-type high-affinity HCO3 pump directly fuelled by ATP.” | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 2-3) |
| NDH-1₃/CupA and NDH-1₄/CupB | `converts` | cytoplasmic CO2 to HCO3− | Specialized NDH complexes “convert CO2 to HCO3 in the cytoplasm.” | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 1-2) |
| Carboxysome | `encapsulates` | Rubisco and carbonic anhydrase | “proteinaceous shell encloses RuBisCo, carbonic anhydrase and a few auxiliary proteins.” | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 3-4) |
| Carboxysomal carbonic anhydrase | `converts` | HCO3− to CO2 near Rubisco | HCO3− “diffuses into carboxysomes where it is converted to CO2.” | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 3-4) |
| Carboxysome CCM | `increases` | local CO2 near Rubisco | Carboxysomes “increase CO2 concentration and reduce O2 levels close to RuBisCo.” | DOI:10.1111/ppl.14140; mechanistic review. (kurkela2024inorganiccarbonsensing pages 1-2) |
| CCM uptake systems | `enable` | growth in ambient air | Inactivation of two NDH systems and three bicarbonate transporters yields cells that “cannot grow in ambient air but grow in high CO2.” | DOI:10.1111/ppl.14140; summarized mutant evidence. (kurkela2024inorganiccarbonsensing pages 1-2) |
| `bicA` overexpression | `increases` | photosynthesis, glycogen, biomass | Overexpression “increases photosynthetic activity, glycogen production and biomass accumulation.” | DOI:10.1111/ppl.14140; taxon/construct-specific and should not be universalized. (kurkela2024inorganiccarbonsensing pages 2-3) |
| low Ci / ambient-air transition | `upregulates` | `sbtA` operon | The operon is “rapidly upregulated” after transfer from high CO2 to ambient air. | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 4-5) |
| high CO2 | `downregulates` | `sbtA` operon | Transfer to high CO2 rapidly and persistently downregulates the operon. | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 4-5) |
| CcmR/NdhR | `represses` | `sbtA` operon | CcmR “act[s] as a repressor…in high CO2 conditions.” | DOI:10.1111/ppl.14140. (kurkela2024inorganiccarbonsensing pages 4-5) |
| 2-phosphoglycolate | `signals` | low inorganic-carbon status | Its accumulation “indicates low Ci.” | DOI:10.1111/ppl.14140; regulatory interpretation. (kurkela2024inorganiccarbonsensing pages 1-2) |
| oxygen | `inhibits` | WL pathway | WL is limited to anaerobic settings because CODH/ACS is highly oxygen sensitive. | DOI:10.1186/s12934-024-02470-6; review statement within a research article. (li2024productionofsuccinate pages 1-2) |
| oxygen | `restricts` | DC/4HB and rTCA activity | Oxygen-sensitive enzymes restrict these pathways to anaerobic or microaerobic conditions. | DOI:10.1186/s12934-024-02470-6; broad generalization requiring pathway/taxon qualification. (li2024productionofsuccinate pages 1-2) |
| anoxic hypersaline sediment | `selects_for` | WL-mediated autotrophy | Authors interpret WL prevalence as favored by “anoxic and hypersaline conditions” that increase cellular energy demand. | DOI:10.1093/femsec/fiae105; field activity plus metagenomic inference, not direct pathway knockout. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) |
| sediment depth | `shifts_community_toward` | anaerobic autotrophy | MAG predictions indicated transition “from aerobic and heterotrophic at the surface to anaerobic and autotrophic at depth.” | DOI:10.1093/femsec/fiae105; **inferred** from 36 OTUs/MAGs. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) |
| partial 3HP pathway | `assimilates` | two CO2 per succinate | “a single succinate molecule from one acetyl-CoA molecule and two CO2 molecules.” | DOI:10.1186/s12934-024-02470-6; experimental engineering. (li2024productionofsuccinate pages 1-2) |
| NaH13CO3 labeling | `verifies` | CO2-derived succinate carbon | Isotope labeling showed “50% of the carbon atoms present in succinate are derived from CO2.” | DOI:10.1186/s12934-024-02470-6; strong assay evidence. (li2024productionofsuccinate pages 1-2) |
| ATP/NADPH and burden optimization | `increases` | engineered succinate production | Final strain produced 3.6 g/L, “an increase of 159% from the starting strain.” | DOI:10.1186/s12934-024-02470-6; construct- and medium-specific. (li2024productionofsuccinate pages 1-2) |

A compact representation of the highest-confidence edges is provided below.

| subject | predicate | object | evidence strength | DOI |
|---|---|---|---|---|
| Calvin-Benson-Bassham cycle | has_key_enzyme | ribulose-1,5-bisphosphate carboxylase/oxygenase (Rubisco) (berg2011ecologicalaspectsof pages 1-2, berg2011ecologicalaspectsof pages 2-3) | Strong review | 10.1128/AEM.02473-10 |
| Rubisco | catalyzes | CO2 fixation from RuBP to 3-phosphoglycerate in the first CBB reaction (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3) | Strong review | 10.1111/ppl.14140 |
| SbtA | transports | bicarbonate into the cyanobacterial cytoplasm as a Na+/HCO3- symporter (kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 1-2) | Strong review | 10.1111/ppl.14140 |
| BicA | transports | bicarbonate into the cyanobacterial cytoplasm as a Na+/HCO3- symporter (kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 1-2) | Strong review | 10.1111/ppl.14140 |
| BCT1 (cmp operon ABC transporter) | transports | bicarbonate into the cyanobacterial cytoplasm using ATP (kurkela2024inorganiccarbonsensing pages 2-3, kurkela2024inorganiccarbonsensing pages 1-2) | Strong review | 10.1111/ppl.14140 |
| NDH-13/CupA and NDH-14/CupB | convert | CO2 to HCO3- in the cytoplasm, facilitating CO2 uptake (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 2-3) | Strong review | 10.1111/ppl.14140 |
| carboxysome | encloses | Rubisco and carbonic anhydrase in a protein shell microcompartment (kurkela2024inorganiccarbonsensing pages 1-2, kurkela2024inorganiccarbonsensing pages 3-4) | Strong review | 10.1111/ppl.14140 |
| carbonic anhydrase in carboxysome | converts | HCO3- to CO2 for Rubisco-dependent fixation (kurkela2024inorganiccarbonsensing pages 3-4, kurkela2024inorganiccarbonsensing pages 2-3) | Strong review | 10.1111/ppl.14140 |
| low inorganic carbon | upregulates | sbtA operon expression (kurkela2024inorganiccarbonsensing pages 4-5) | Strong review of experimental literature | 10.1111/ppl.14140 |
| CcmR/NdhR | represses | sbtA operon under high CO2 conditions (kurkela2024inorganiccarbonsensing pages 4-5, kurkela2024inorganiccarbonsensing pages 1-2) | Strong review of experimental literature | 10.1111/ppl.14140 |
| 2-phosphoglycolate | inhibits | CcmR during low-Ci/photorespiratory conditions, contributing to CCM gene induction (kurkela2024inorganiccarbonsensing pages 4-5, kurkela2024inorganiccarbonsensing pages 1-2) | Moderate review of regulatory mechanism | 10.1111/ppl.14140 |
| Wood-Ljungdahl pathway | requires | strictly anaerobic conditions because CO dehydrogenase/acetyl-CoA synthase is oxygen sensitive (li2024productionofsuccinate pages 1-2, liang2020recentadvancesin pages 3-5) | Strong review | 10.1186/s12934-024-02470-6 |
| anoxic hypersaline sediment conditions | select_for | Wood-Ljungdahl pathway-mediated autotrophy (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | Strong field study, metagenomic inference plus dark CO2 fixation assay | 10.1093/femsec/fiae105 |
| dark CO2 fixation in Great Salt Lake sediments | is_predicted_to_be_primarily_via | Wood-Ljungdahl pathway (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2) | Strong field study, metagenomic inference plus activity detection | 10.1093/femsec/fiae105 |
| partial 3-hydroxypropionate pathway engineered in Cupriavidus necator H16 | enables | succinate production with two CO2 fixation reactions (li2024productionofsuccinate pages 1-2, li2024productionofsuccinate pages 2-4) | Strong experimental engineering study | 10.1186/s12934-024-02470-6 |
| NaH13CO3 isotope labeling in engineered Cupriavidus necator H16 | verifies | 50% of succinate carbon derived from CO2 (li2024productionofsuccinate pages 1-2) | Strong experimental validation | 10.1186/s12934-024-02470-6 |


*Table: This table compiles the strongest candidate causal edges for curating microbial autotrophic carbon fixation, emphasizing experimentally grounded cyanobacterial CCM components, Wood-Ljungdahl environmental constraints, and a recent engineered 3HP-derived application. It is useful as a compact starting set for TraitMech graph curation.*

## 5. Recent developments, applications, and quantitative evidence

### Cyanobacterial carbon-concentrating mechanisms—2024 synthesis

Kurkela and Tyystjärvi’s January 2024 review integrates Ci transport, carboxysomal fixation, and metabolic signaling. Its most curation-relevant advance is a connected mechanism from environmental Ci through SbtA/BicA/BCT1 and specialized NDH-1 complexes to carboxysomal CO2 generation, Rubisco activity, and transcriptional acclimation. The authors also identify unresolved areas: regulation of carboxysome dynamics, turnover of photosynthetic complexes, and coordination of cell division with Ci remain incompletely understood. (kurkela2024inorganiccarbonsensing pages 1-2)

### Dark fixation in hypersaline sediments—2024 field implementation

Shoemaker et al. studied a 30-cm Great Salt Lake sediment core under approximately 30% NaCl conditions. Dark CO2 fixation was detected, while pathway assignment was based primarily on MAGs from 36 OTUs. WL was predicted as the dominant autotrophic mechanism, including novel hydrogenotrophic acetogens affiliated with *Candidatus Bipolaricaulia*; CBB and rTCA populations were minor. The result supports a graph edge from anoxic/hypersaline energy limitation to ecological selection for low-energy WL autotrophy, but not a direct molecular claim that salinity activates WL genes. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2, shoemaker2024wood–ljungdahlpathwayencoding pages 2-3)

### Engineered CO2 incorporation into succinate—2024 demonstration

Li et al. installed a partial 3HP module in *Cupriavidus necator* H16, using ACC and PCC carboxylation steps. NaH13CO3 labeling showed that two of succinate’s four carbons originated from inorganic carbon. The optimized strain reached **3.6 g/L succinate**, a **159% increase** over the starting strain. The reported theoretical values were **2.37 g succinate per g fatty-acid feedstock** and **0.8 g net CO2 fixed per g feedstock** under the modeled route. This is a real metabolic-engineering implementation, but it is mixotrophic CO2 incorporation driven by fatty-acid catabolism, not proof of autotrophic growth. (li2024productionofsuccinate pages 2-4, li2024productionofsuccinate pages 1-2)

### Bioenergetic design guidance

The six pathways differ in ATP cost, oxygen tolerance, thermodynamic driving force, and preferred reductant. A 2025 systems analysis predicts that rTCA has the lowest overall energy cost and broad adaptability, with WL also highly efficient; 3HP/4HB and 3HP can provide larger driving forces at moderate yield penalties. Because these conclusions derive from flux and thermodynamic modeling, they are suitable as design hypotheses, not organism-level causal evidence. (taha2025bioenergetictradeoffscan pages 1-2)

## 6. Recommended YAML architecture

A practical graph should separate four layers:

1. **Environmental inputs:** CO2/HCO3− availability, pH, O2, light, electron donors, salinity.
2. **Acquisition and concentration:** SbtA, BicA, BCT1, NDH-1₃/₄, carboxysome, carbonic anhydrase.
3. **Assimilation pathway:** one of the six established pathway child nodes and its diagnostic enzymes.
4. **Phenotypic output:** incorporation into a central metabolite, biomass labeling, and autotrophic growth.

Evidence metadata should include `taxon`, `strain`, `condition`, `assay`, `evidence_type`, and `certainty`. Recommended evidence categories are: biochemical reaction, genetic perturbation, isotope incorporation, growth phenotype, transcript/protein expression, metagenomic potential, and computational prediction.

## 7. Claims that should not yet be curated as general TraitMech edges

1. **`rbcL present → carbon fixation trait`.** Marker presence is insufficient; require pathway completeness plus culture, isotope, or expression evidence. (nishihara2025exploringthediversity pages 5-8)
2. **`bicarbonate incorporation → autotrophy`.** Anaplerotic or engineered partial-pathway fixation may occur during heterotrophic growth.
3. **`high salinity activates WL`.** The 2024 Great Salt Lake result supports ecological selection/association, not direct regulatory activation. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
4. **Universal oxygen categories.** Label pathways as generally oxygen-compatible or oxygen-sensitive, but encode organism- and enzyme-specific exceptions.
5. **Universal `bicA` overexpression benefit.** Increased photosynthesis and biomass were construct-specific findings summarized in a review. (kurkela2024inorganiccarbonsensing pages 2-3)
6. **Reductive glycine as an established seventh child.** It is increasingly treated as an autotrophic route, but adding it changes the reviewed six-pathway scope and needs a versioned ontology decision. (nishihara2025exploringthediversity pages 1-5)
7. **MAG pathway calls as demonstrated physiology.** MAGs establish encoded potential; missing genes, assembly incompleteness, paralogy, and multifunctional enzymes can confound assignments.
8. **Computational energetic rankings as biological causation.** The rTCA/WL rankings are predictions pending matched experimental validation. (taha2025bioenergetictradeoffscan pages 1-2)
9. **Global sequestration outcomes from laboratory fixation rates.** Biomass turnover and downstream carbon persistence must be measured separately.

## 8. DOI-first bibliography

1. **10.1111/ppl.14140** — Kurkela J, Tyystjärvi T. “Inorganic carbon sensing and signalling in cyanobacteria.” *Physiologia Plantarum* 176:e14140. **Published January 2024**; received October 30, 2023. https://doi.org/10.1111/ppl.14140 (kurkela2024inorganiccarbonsensing pages 1-2)
2. **10.1093/femsec/fiae105** — Shoemaker A et al. “Wood–Ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at Great Salt Lake, Utah.” *FEMS Microbiology Ecology* 100. **Published online July 25, 2024.** https://doi.org/10.1093/femsec/fiae105 (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2)
3. **10.1186/s12934-024-02470-6** — Li L et al. “Production of succinate with two CO2 fixation reactions from fatty acids in *Cupriavidus necator* H16.” *Microbial Cell Factories* 23:194. **Published July 2024.** https://doi.org/10.1186/s12934-024-02470-6 (li2024productionofsuccinate pages 1-2)
4. **10.1128/AEM.02473-10** — Berg IA. “Ecological Aspects of the Distribution of Different Autotrophic CO2 Fixation Pathways.” *Applied and Environmental Microbiology* 77:1925–1936. **Published March 2011; online January 7, 2011.** https://doi.org/10.1128/AEM.02473-10 (berg2011ecologicalaspectsof pages 2-3, berg2011ecologicalaspectsof pages 1-2)
5. **10.3389/fmicb.2020.592631** — Liang B, Zhao Y, Yang J. “Recent Advances in Developing Artificial Autotrophic Microorganism for Reinforcing CO2 Fixation.” *Frontiers in Microbiology* 11. **Published November 2020.** https://doi.org/10.3389/fmicb.2020.592631 (liang2020recentadvancesin pages 3-5, liang2020recentadvancesin pages 1-2)
6. **10.1128/msystems.01274-24** — Taha A, Patón M, Rodríguez J. “Bioenergetic trade-offs can reveal the path to superior microbial CO2 fixation pathways.” *mSystems* 10. **Published February 2025.** https://doi.org/10.1128/msystems.01274-24 — computational study. (taha2025bioenergetictradeoffscan pages 1-2)
7. **10.1101/2025.05.01.651632** — Nishihara A, Kato S, Ohkuma M. “Exploring the diversity and physiological characteristics of Rubisco-mediated carbon fixation in culturable prokaryotes.” bioRxiv. **Posted May 2025.** https://doi.org/10.1101/2025.05.01.651632 — non-peer-reviewed genomic survey. (nishihara2025exploringthediversity pages 1-5, nishihara2025exploringthediversity pages 5-8)

References

1. (berg2011ecologicalaspectsof pages 1-2): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

2. (shoemaker2024wood–ljungdahlpathwayencoding pages 2-3): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 15 citations and is from a peer-reviewed journal.

3. (nishihara2025exploringthediversity pages 5-8): Arisa Nishihara, Shingo Kato, and Moriya Ohkuma. Exploring the diversity and physiological characteristics of rubisco-mediated carbon fixation in culturable prokaryotes. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.01.651632, doi:10.1101/2025.05.01.651632. This article has 1 citations.

4. (berg2011ecologicalaspectsof pages 2-3): Ivan A. Berg. Ecological aspects of the distribution of different autotrophic co <sub>2</sub> fixation pathways. Mar 2011. URL: https://doi.org/10.1128/aem.02473-10, doi:10.1128/aem.02473-10. This article has 1025 citations and is from a peer-reviewed journal.

5. (nishihara2025exploringthediversity pages 1-5): Arisa Nishihara, Shingo Kato, and Moriya Ohkuma. Exploring the diversity and physiological characteristics of rubisco-mediated carbon fixation in culturable prokaryotes. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.01.651632, doi:10.1101/2025.05.01.651632. This article has 1 citations.

6. (li2024productionofsuccinate pages 1-2): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 13 citations and is from a peer-reviewed journal.

7. (liang2020recentadvancesin pages 3-5): Bo Liang, Yukun Zhao, and Jianming Yang. Recent advances in developing artificial autotrophic microorganism for reinforcing co2 fixation. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.592631, doi:10.3389/fmicb.2020.592631. This article has 64 citations and is from a peer-reviewed journal.

8. (liang2020recentadvancesin pages 1-2): Bo Liang, Yukun Zhao, and Jianming Yang. Recent advances in developing artificial autotrophic microorganism for reinforcing co2 fixation. Frontiers in Microbiology, Nov 2020. URL: https://doi.org/10.3389/fmicb.2020.592631, doi:10.3389/fmicb.2020.592631. This article has 64 citations and is from a peer-reviewed journal.

9. (taha2025bioenergetictradeoffscan pages 1-2): Ahmed Taha, Mauricio Patón, and Jorge Rodríguez. Bioenergetic trade-offs can reveal the path to superior microbial co <sub>2</sub> fixation pathways. Feb 2025. URL: https://doi.org/10.1128/msystems.01274-24, doi:10.1128/msystems.01274-24. This article has 4 citations and is from a peer-reviewed journal.

10. (kurkela2024inorganiccarbonsensing pages 3-4): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

11. (kurkela2024inorganiccarbonsensing pages 1-2): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

12. (kurkela2024inorganiccarbonsensing pages 2-3): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

13. (kurkela2024inorganiccarbonsensing pages 4-5): Juha Kurkela and Taina Tyystjärvi. Inorganic carbon sensing and signalling in cyanobacteria. Physiologia Plantarum, Jan 2024. URL: https://doi.org/10.1111/ppl.14140, doi:10.1111/ppl.14140. This article has 24 citations and is from a peer-reviewed journal.

14. (shoemaker2024wood–ljungdahlpathwayencoding pages 1-2): Anna Shoemaker, Andrew Maritan, Su Cosar, Sylvia Nupp, Ana Menchaca, Thomas Jackson, Aria Dang, Bonnie K Baxter, Daniel R Colman, Eric C Dunham, and Eric S Boyd. Wood–ljungdahl pathway encoding anaerobes facilitate low-cost primary production in hypersaline sediments at great salt lake, utah. FEMS Microbiology Ecology, Jul 2024. URL: https://doi.org/10.1093/femsec/fiae105, doi:10.1093/femsec/fiae105. This article has 15 citations and is from a peer-reviewed journal.

15. (li2024productionofsuccinate pages 2-4): Linqing Li, Xiuyuan Zhou, Zhuoao Gao, Peng Xiong, and Xiutao Liu. Production of succinate with two co2 fixation reactions from fatty acids in cupriavidus necator h16. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02470-6, doi:10.1186/s12934-024-02470-6. This article has 13 citations and is from a peer-reviewed journal.