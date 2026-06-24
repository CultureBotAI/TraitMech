---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:31:52.445445'
end_time: '2026-06-18T02:41:09.867673'
duration_seconds: 557.42
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid2
  trait_identifier: METPO:1000451
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 27\u201330 \xB0C, characteristic of mesophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_27_to_30
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 27\u201330 \xB0C range as a typical\
    \ mesophile growth range.)"
  causal_graph_summary: 'temperature_range_mid2_baseline_mesophile: 3 nodes, 2 edges'
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
- **Trait label:** temperature range mid2
- **METPO identifier:** METPO:1000451
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 27–30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 27–30 °C range as a typical mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid2_baseline_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid2.yaml`.

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
- **Trait label:** temperature range mid2
- **METPO identifier:** METPO:1000451
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 27–30 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_27_to_30
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 27–30 °C range as a typical mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid2_baseline_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid2.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **temperature range mid2** (METPO:1000451)

### Scope summary (TraitMech curation perspective)
**temperature range mid2** represents a *growth-supporting ambient temperature range* spanning approximately **27–30 °C**, described as characteristic of **mesophilic physiology**. This class is best interpreted as a **narrow mesophilic subrange** (often used as a laboratory cultivation or process temperature window), not as the full mesophilic envelope. Recent reviews define **mesophiles** broadly as organisms that “**grow between room temperature (around 20 °C) and about 45 °C**,” placing 27–30 °C unambiguously inside mesophily and suggesting that “mid2” should be distinguished from nearby classes by *cardinal growth boundaries* and *assay/culture conditions* rather than by unique molecular machinery (which is largely shared across mesophiles). (ramon2023ageneraloverview pages 1-2)

**Boundary cases / distinctions**
- Distinguish from **psychrophiles** (can grow at 0 °C; optimum ≈15 °C; may not grow at 20 °C) and **psychrotolerants** (can grow at 4 °C; optimum >20 °C). (ramon2023ageneraloverview pages 1-2)
- Distinguish from **thermophiles** by the lack of growth at high temperatures (e.g., for *E. coli*, optimal growth is ~37 °C with poor growth at 44 °C and fragility near ~50 °C, illustrating a mesophile’s upper constraint). (moon2023temperaturemattersbacterial pages 1-3)

Because the trait is centered at 27–30 °C, many mechanistic edges relevant to **temperature-dependent growth limits** come from studies of **temperature shifts** (cold-shock and heat-shock) rather than from experiments explicitly at 27–30 °C. These edges remain curation-relevant because they describe *shared temperature-sensing, membrane homeostasis, and proteostasis mechanisms* that shape the viable growth range that includes 27–30 °C. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, ramon2023ageneraloverview pages 22-23)

---

## 1) Key concepts and definitions (current understanding)

### Mesophily and temperature range phenotypes
- **Mesophiles**: broad growth range around **~20–45 °C**. (ramon2023ageneraloverview pages 1-2)
- The **mid2** label (27–30 °C) is consistent with real-world mesophilic practice: e.g., “**mesophilic (28–33 °C) sludge**” in anaerobic digestion contexts overlaps the mid2 window. (wu2024effectoftemperature pages 2-3)

### Homeoviscous adaptation (membrane fluidity homeostasis)
A central concept linking temperature to growth capacity is **homeoviscous adaptation**, i.e., temperature-driven remodeling of membrane lipid composition to maintain membrane physical properties. Ramón et al. explicitly define it as regulation of **membrane lipid viscosity** (in *E. coli*). (ramon2023ageneraloverview pages 22-23)

### Nucleic-acid thermosensing and post-transcriptional control
- **DNA supercoiling as thermosensor**: Temperature shifts alter DNA topology, affecting promoter accessibility and transcription of thermal tolerance genes. (moon2023temperaturemattersbacterial pages 1-3)
- **RNA thermometers (RNATs)**: 5′-UTR secondary structures can occlude the Shine–Dalgarno site at lower temperature and melt at higher temperature to permit translation—an efficient coupling of temperature to expression of stress proteins. (moon2023temperaturemattersbacterial pages 1-3, viuda2025physicalcommunicationpathways pages 5-7)

---

## 2) Candidate causal graph entities (nodes)

### A. Environmental & experimental factors
- Ambient temperature (27–30 °C; broader mesophile 20–45 °C) (ramon2023ageneraloverview pages 1-2)
- Temperature shift (e.g., 37→20 °C cold shift for DesK/DesR sensing) (moon2023temperaturemattersbacterial pages 7-9)
- Culture medium amino acid availability (e.g., **isoleucine** impacting branched-chain fatty acids in *B. subtilis*) (ramon2023ageneraloverview pages 4-5)
- Process temperatures (examples): mesophilic sludge 28–33 °C; mesophilic AD operation 35–37 °C; high-temperature initiation 55 °C; storage 15 °C vs 35 °C (wu2024effectoftemperature pages 2-3, wu2024effectoftemperature pages 1-2)

### B. Membrane/lipid composition nodes
- Membrane fluidity / viscosity (homeoviscous adaptation) (ramon2023ageneraloverview pages 22-23)
- Saturated fatty acids (SFA), unsaturated fatty acids (UFA) (moon2023temperaturemattersbacterial pages 7-9)
- Branched-chain fatty acids (iso-/anteiso-) (ramon2023ageneraloverview pages 4-5)
- Hopanoids / sterol-like membrane lipids (ramon2023ageneraloverview pages 22-23)
- Pigments (carotenoids, etc.; temperature-dependent synthesis) (ramon2023ageneraloverview pages 4-5)
- Cyclopropanation of unsaturated FAs (as membrane-stabilizing strategy; review evidence) (maiti2024extrememakeoverthe pages 4-5)

### C. Genes/proteins and regulatory modules
- Two-component thermosensing: **DesK (sensor kinase) / DesR (response regulator)** (cold-responsive lipid remodeling) (moon2023temperaturemattersbacterial pages 7-9)
- Fatty-acid remodeling enzymes: **FabF** (cis-vaccenic acid increase on cooling) (ramon2023ageneraloverview pages 4-5)
- DNA topology and enzymes: **DNA gyrase**; ATP/ADP ratio as regulator (moon2023temperaturemattersbacterial pages 1-3)
- RNA thermometers (5′-UTR structural elements; label-only node) (moon2023temperaturemattersbacterial pages 1-3, viuda2025physicalcommunicationpathways pages 5-7)
- Proteostasis: chaperones and shock proteins (heat- and cold-shock proteins broadly; chaperones) (moon2023temperaturemattersbacterial pages 1-3)
- Protein folding accelerators at low temperature: **PPIases**, **trigger factor** (strong induction reported) (moon2023temperaturemattersbacterial pages 7-9)
- Cold-shock translation/RNA factors: **CspA**, **CsdA** (moon2023temperaturemattersbacterial pages 7-9)

### D. Cellular processes
- Cellular response to temperature change (heat shock / cold shock programs) (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9)
- Transcriptional regulation via DNA topology (moon2023temperaturemattersbacterial pages 1-3)
- Translational regulation via RNATs (moon2023temperaturemattersbacterial pages 1-3, viuda2025physicalcommunicationpathways pages 5-7)

---

## 3) Evidence-backed causal edges (triples)
The following table is designed for direct curation into a TraitMech-style causal graph.

| Subject node | Predicate | Object node | Edge type | Evidence snippet (short quote) | Source (authors, year) | DOI | URL | Publication month/year | Curation notes |
|---|---|---|---|---|---|---|---|---|---|
| Decreased ambient temperature | decreases | membrane fluidity / increases membrane rigidification | direct | "Temperature drop -> membrane rigidification and increased thickness" (ramon2023ageneraloverview pages 4-5) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Broad bacterial cold-adaptation mechanism; relevant as lower-boundary pressure for mesophiles, not specific to 27–30 °C. |
| Homeoviscous adaptation | maintains | membrane lipid viscosity / fluidity | direct | "Homeoviscous adaptation ... regulation of membrane lipid viscosity in E. coli" (ramon2023ageneraloverview pages 22-23) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Strong background mechanism; good generic node for mesophilic temperature tolerance graph. |
| FabF | increases | cis-vaccenic acid | direct | "The key enzyme in the increase of cis-vaccenic acid is FabF" (ramon2023ageneraloverview pages 4-5) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Primarily evidenced in cold shift responses; supports unsaturated FA remodeling node. |
| Increased unsaturated fatty acid fraction | increases | membrane fluidity | direct | "higher unsaturated content increases fluidity" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Canonical mechanism; suitable for curation as general bacterial thermoadaptation edge. |
| Fatty acid desaturase Des | increases | unsaturated fatty acids | direct | "FA desaturase Des ... produces unsaturated fatty acids after cold exposure" (barbotin2026twotemperaturedependentmembrane pages 1-2) | Barbotin et al., 2026 | 10.1128/msphere.00095-26 | https://doi.org/10.1128/msphere.00095-26 | Jun 2026 | Strong mechanistic chain but source is 2026; include with date caution if prioritizing 2023–2024. |
| Unsaturated fatty acid fraction | supports | functional membrane at lower temperature | indirect | "UFA fraction ↑ -> membrane fluidity ↑ -> survival/functional membrane at lower T" (maiti2024extrememakeoverthe pages 4-5) | Maiti et al., 2024 | 10.1039/d4cc03114h | https://doi.org/10.1039/d4cc03114h | Aug 2024 | Review-level synthesis; good for generalized edge, but mostly from cold-adaptation examples. |
| Isoleucine in culture medium | enables | branched-chain fatty acid synthesis | direct | "the occurrence of the branching of FAs in B. subtilis depends on the presence of isoleucine in the culture medium" (ramon2023ageneraloverview pages 4-5) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Medium-dependent and taxon-specific (B. subtilis); curate as assay- and taxon-specific. |
| Branched-chain fatty acids | fluidize | membrane | direct | "fluidization of the membrane by the introduction of chain branching" (ramon2023ageneraloverview pages 4-5) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Strong mechanism for Gram-positives; useful near lower mesophilic boundary. |
| Hopanoids / sterol-like molecules | regulate | membrane fluidity | direct | "hopanoids, sterol-like molecules, and carotenoids ... act as regulators for membrane fluidity" (ramon2023ageneraloverview pages 22-23) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Good generic membrane-modulator edge; broad, not 27–30 °C-specific. |
| Cholesterol / hopanoid increase | inhibits | fluid-to-gel phase transition | direct | "an increase in cholesterol can hinder the fluid-to-gel phase transition" (maiti2024extrememakeoverthe pages 4-5) | Maiti et al., 2024 | 10.1039/d4cc03114h | https://doi.org/10.1039/d4cc03114h | Aug 2024 | Mechanistically strong for membrane-state node; cholesterol wording may not generalize across bacteria, so prefer hopanoid/sterol-like abstraction. |
| Low temperature of growth | induces | carotenoid and other pigment synthesis | direct | "The dependence between low temperature of growth and the synthesis of carotenoids and other pigments was observed" (ramon2023ageneraloverview pages 4-5) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Likely taxon-specific and mostly lower-temperature response; uncertain for broad mesophile graph. |
| Carotenoids / pigments | modulate | membrane fluidity | indirect | "these pigments ... can modulate fluidity" (ramon2023ageneraloverview pages 4-5) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Mechanism plausible but weaker, with limited breadth; flag uncertain. |
| Temperature drop from 37 °C to 20 °C | activates | DesK sensor kinase | direct | "DesK responds when temperature falls from 37 to 20 °C" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong, classic Bacillus mechanism; taxon-specific but highly curation-worthy. |
| DesK | phosphorylates / activates | DesR | direct | "DesK ... phosphorylates DesR" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong two-component signaling edge; Bacillus-focused. |
| DesR | induces transcription of | D5-desaturase / Des | direct | "DesR to induce D5-desaturase transcription" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong mechanistic regulator edge; taxon-specific but standard. |
| Low temperatures below 26 °C | trigger | membrane fluidity homeostasis | direct | "fluidity is maintained only at low temperatures (<26°C)" (barbotin2026twotemperaturedependentmembrane pages 1-2) | Barbotin et al., 2026 | 10.1128/msphere.00095-26 | https://doi.org/10.1128/msphere.00095-26 | Jun 2026 | Quantitative threshold is useful because trait mid2 begins just above this zone; source is 2026 and Gram-positive-focused. |
| Temperature change | alters | DNA supercoiling | direct | "DNA can function as a thermosensor by shifting the degree of supercoiling" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Broad thermosensing mechanism; suitable as high-level regulatory edge. |
| Increased ATP/ADP ratio during heat shock | activates | gyrase | direct | "the increase of [ATP]/[ADP] ratio activates the function of gyrase" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong mechanistic edge for heat response; not specific to 27–30 °C but relevant near upper mesophilic shifts. |
| Gyrase activation | relaxes | DNA supercoils | direct | "activates the function of gyrase, resulting in relaxation of the DNA supercoil" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Good direct regulatory edge. |
| DNA topology change | alters | transcription of thermal tolerance genes | indirect | "the change of DNA topology is an important factor" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Broad and useful, but gene targets often context-specific. |
| Low temperature | closes | Shine-Dalgarno sequence within RNA thermometer | direct | "At a low temperature, Shine-Dalgarno sequences are closed" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong RNAT mechanism; generic across bacterial thermometers. |
| Elevated temperature | melts / opens | RNA thermometer 5′-UTR structure | direct | "5′-UTR secondary structures melt upon heat exposure, exposing ribosome binding sites" (viuda2025physicalcommunicationpathways pages 5-7) | de la Viuda et al., 2025 | 10.1007/s12551-025-01290-1 | https://doi.org/10.1007/s12551-025-01290-1 | Mar 2025 | Good concise mechanistic edge; broad review-level support. |
| Open RNA thermometer | permits translation of | heat-responsive proteins / chaperones | direct | "initiating translation of heat-responsive proteins (notably chaperones)" (viuda2025physicalcommunicationpathways pages 5-7) | de la Viuda et al., 2025 | 10.1007/s12551-025-01290-1 | https://doi.org/10.1007/s12551-025-01290-1 | Mar 2025 | Strong regulatory edge; ideal for causal graph. |
| Temperature shift / heat shock | induces | heat-shock proteins and chaperones | direct | "temperature shifts induce heat- and cold-shock proteins" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | High-confidence general edge for stress response layer. |
| Heat-shock proteins / chaperones | counteract | protein denaturation / aggregation | direct | "counteract denaturation and aid tolerance" (moon2023temperaturemattersbacterial pages 1-3) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong, general proteostasis edge. |
| RpoH (σ32) | coordinates expression of | chaperones and proteases | direct | "RpoH (σ32) ... coordinate expression of chaperones and proteases" (viuda2025physicalcommunicationpathways pages 5-7) | de la Viuda et al., 2025 | 10.1007/s12551-025-01290-1 | https://doi.org/10.1007/s12551-025-01290-1 | Mar 2025 | Good canonical heat-shock regulatory edge. |
| Low temperature | slows | prolyl isomerization | direct | "At low temperature, intrinsic prolyl isomerization slows" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Mechanistically relevant to folding constraints at lower mesophilic boundary. |
| PPIases and trigger factor overexpression | accelerates / supports | protein folding at low temperature | direct | "overexpress PPIases and the trigger factor (~40-fold) to accelerate folding and prevent aggregation" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Quantified response; useful but mainly low-temperature adaptation literature. |
| CsdA helicase | maintains | translation under cold shock | direct | "CsdA ... maintain translation by resolving RNA structures" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Strong cold-shock edge; probably outside narrow mid2 core but relevant boundary mechanism. |
| CspA RNA chaperone | maintains | translation under cold shock | direct | "CspA (RNA chaperone) maintain translation" (moon2023temperaturemattersbacterial pages 7-9) | Moon et al., 2023 | 10.1007/s12275-023-00031-x | https://doi.org/10.1007/s12275-023-00031-x | Mar 2023 | Good edge for low-temperature boundary adaptation. |
| Mesophilic organisms | grow between | around 20 °C and about 45 °C | direct | "mesophiles ... grow between room temperature (around 20 °C) and about 45 °C" (ramon2023ageneraloverview pages 1-2) | Ramón et al., 2023 | 10.1007/s42770-023-01057-4 | https://doi.org/10.1007/s42770-023-01057-4 | Jul 2023 | Key scope-defining edge; directly supports placing 27–30 °C within mesophily. |
| Mesophile growth curve | peaks at | 35 °C | direct | "The mesophile curve peaks at 35°C and drops to zero at 15°C and 45°C" (alghazali2025theroleof pages 3-9) | AlGhazali and Eljamay, 2025 | not available in context | not available in context | 2025 | Secondary or unclear-source support only; do not curate alone without stronger primary source. |
| Mesophilic sludge | has operating temperature | 28–33 °C | direct | "mesophilic (28–33 °C) sludge" (wu2024effectoftemperature pages 2-3) | Wu et al., 2024 | 10.3390/agronomy14122991 | https://doi.org/10.3390/agronomy14122991 | Dec 2024 | Real-world process evidence for mid2-adjacent mesophilic operation; engineering context rather than intrinsic mechanism. |
| Mesophilic anaerobic digestion | operates at | 35–37 °C | direct | "mesophilic AD operation at 35–37 °C" (wu2024effectoftemperature pages 2-3) | Wu et al., 2024 | 10.3390/agronomy14122991 | https://doi.org/10.3390/agronomy14122991 | Dec 2024 | Useful application/process node; slightly above mid2 range but within mesophile practice. |
| Mesophilic Bacillus cereus isolates | are pre-cultured at | 30 °C | direct | "mesophilic isolates were routinely pre-cultured at 30°C" (maktabdar2025developmentofextensive pages 2-3) | Maktabdar et al., 2025 | 10.3389/fmicb.2025.1553885 | https://doi.org/10.3389/fmicb.2025.1553885 | Mar 2025 | Assay-specific evidence that 30 °C is a standard mesophilic cultivation temperature; useful experimental-factor node. |
| Mix-Bcmes mesophilic model | tested temperature range | 13–45 °C | direct | "Cardinal temperature testing for the mesophilic mix covered 13–45°C" (maktabdar2025developmentofextensive pages 2-3) | Maktabdar et al., 2025 | 10.3389/fmicb.2025.1553885 | https://doi.org/10.3389/fmicb.2025.1553885 | Mar 2025 | Helpful boundary evidence for mesophilic strains in predictive food microbiology; taxon- and assay-specific. |


*Table: This table compiles evidence-backed candidate causal edges for the microbial trait temperature range mid2, centered on mesophilic growth around 27–30 °C. It emphasizes membrane adaptation, thermosensing, nucleic-acid-based regulation, chaperone responses, and process temperatures relevant to mesophilic cultivation and operation.*

---

## 4) Current applications and real-world implementations (temperature windows near mid2)

### A. Mesophilic anaerobic digestion (AD) and wastewater/waste-to-energy systems
A 2024 engineering-focused study describes seed sludge as “**mesophilic (28–33 °C) sludge**,” overlapping the 27–30 °C mid2 class, and cites typical **mesophilic AD operation at 35–37 °C**. (wu2024effectoftemperature pages 2-3)

Quantitative operational context reported includes preservation temperatures (**15 ± 1 °C** vs **35 ± 1 °C** for 60 days), comparisons to 4 °C/room temperature/−20 °C storage effects, and a high-to-mesophilic initiation strategy (**55 °C → 35 °C**). This positions mid2-like temperatures as practically relevant (especially for inoculum handling and start-up) even when the main operating setpoint is slightly higher (35 °C). (wu2024effectoftemperature pages 2-3, wu2024effectoftemperature pages 1-2, wu2024effectoftemperature pages 3-5)

### B. Food safety and predictive microbiology (mesophilic pathogens/spoilage)
A 2025 study on **mesophilic *Bacillus cereus*** modeling in dairy reports routine **pre-culturing at 30 °C**, directly aligned with the mid2 range, and uses a temperature domain of **13–45 °C** for cardinal growth modeling (large dataset of **344 μmax** values for a mesophilic strain cocktail). (maktabdar2025developmentofextensive pages 2-3)

This supports adding experimental-factor nodes such as “standard pre-culture temperature 30 °C” and provides a data-backed argument that 30 °C is a common mesophilic cultivation temperature used in practice for growth characterization and safety modeling. (maktabdar2025developmentofextensive pages 2-3)

---

## 5) Expert synthesis / analysis (authoritative interpretations)

### Mechanistic “backbone” likely common across mid2 mesophiles
Recent reviews converge on a shared mechanistic backbone that determines whether growth is possible across the mesophile range that includes 27–30 °C:
1. **Membrane fluidity homeostasis (homeoviscous adaptation)** via lipid remodeling (UFA/SFA ratios; branching; hopanoids/pigments) to preserve membrane-associated processes required for growth. (moon2023temperaturemattersbacterial pages 7-9, ramon2023ageneraloverview pages 22-23)
2. **Thermosensing and regulation** through (i) membrane-embedded systems such as **DesK/DesR** (Gram-positive example) and (ii) nucleic acid-based thermosensing (DNA supercoiling; RNATs). (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9, viuda2025physicalcommunicationpathways pages 5-7)
3. **Proteostasis capacity** (heat/cold shock proteins; chaperones; folding catalysts) to prevent temperature-dependent protein misfolding that would limit growth. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9)

### Practical implication for curation
Because mid2 (27–30 °C) is a **narrow band inside mesophily**, *the trait itself is unlikely to map to a single unique gene or pathway*. Instead, curatable causal structure should emphasize:
- Edges that connect **temperature** to **membrane state** and **global regulation**, and from there to **growth capacity**.
- Explicit **assay/process context nodes** (e.g., pre-culture at 30 °C; sludge category 28–33 °C), because these often operationalize what “mid2” means in real datasets. (wu2024effectoftemperature pages 2-3, maktabdar2025developmentofextensive pages 2-3)

---

## 6) Ontology grounding suggestions (CURIEs; conservative)

### Trait
- METPO:1000451 (temperature range mid2) (provided by user)

### Environmental factor
- Temperature: consider ENVO temperature terms (label-only if exact ENVO term not selected)

### Biological processes (GO)
- Response to heat: **GO:0009408** (candidate)
- Response to cold: **GO:0009409** (candidate)
- Peptidyl-prolyl cis-trans isomerase activity (PPIase): **GO:0003755** (candidate)
- Two-component sensor kinase activity: **GO:0000155** (candidate)
- Two-component response regulator activity: **GO:0000156** (candidate)

### Enzymes/proteins (IDs depend on organism)
- DNA gyrase: **EC 5.6.2.2** (enzyme class; gene-level UniProt is organism-specific) (moon2023temperaturemattersbacterial pages 1-3)
- DesK/DesR/Des: keep as label-only or map to organism-specific UniProt when the taxon is specified (moon2023temperaturemattersbacterial pages 7-9)

### Chemicals (CHEBI)
- Fatty acid (generic): **CHEBI:35366** (fatty acid; if used) / **CHEBI:27208** (as suggested concept)
- Palmitic acid: **CHEBI:15756** (moon2023temperaturemattersbacterial pages 7-9)
- Oleic acid: **CHEBI:30879** (mentioned in membrane-remodeling review context) (maiti2024extrememakeoverthe pages 4-5)
- Hopanoid: **CHEBI:26125** (candidate) (ramon2023ageneraloverview pages 22-23)
- Carotenoid: **CHEBI:23044** (candidate) (ramon2023ageneraloverview pages 22-23)

### Concepts lacking stable identifiers in evidence
- RNA thermometer: keep **label-only** unless adopting a specific SO/NCRNA ontology term consistently across the project. (moon2023temperaturemattersbacterial pages 1-3, viuda2025physicalcommunicationpathways pages 5-7)
- Branched-chain fatty acids (iso-/anteiso-): keep **label-only** unless selecting specific CHEBI entries for the dominant species. (ramon2023ageneraloverview pages 4-5)

---

## 7) Warnings / claims that should not yet be curated
1. **Mid2-specific unique mechanisms are not established**: evidence supports general mesophilic thermoadaptation mechanisms, but not a distinct mechanistic signature exclusive to 27–30 °C.
2. **Taxon-specific edges** should be flagged as such in YAML (e.g., DesK/DesR/Des from *Bacillus*; isoleucine-dependent branching in *B. subtilis*). (ramon2023ageneraloverview pages 4-5, moon2023temperaturemattersbacterial pages 7-9)
3. **Edges supported only by unclear/low-trust sources** should not be curated alone. For example, the 2025 “meta-analysis” excerpt stating a mesophile curve peaking at 35 °C lacks clear bibliographic/DOI context in the retrieved text and should be treated as secondary until confirmed. (alghazali2025theroleof pages 3-9)
4. **Non-2023/2024 evidence**: one mechanistic membrane-fluidity-threshold paper is from 2026 and should be optional if your curation policy restricts recency; keep but mark provenance clearly. (barbotin2026twotemperaturedependentmembrane pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)

1. Moon S, Ham S, Jeong J, et al. **Temperature matters: bacterial response to temperature change.** *Journal of Microbiology.* **Mar 2023.** DOI: **10.1007/s12275-023-00031-x**. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 7-9)
2. Ramón A, Esteves A, Villadóniga C, et al. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology.* **Jul 2023.** DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23)
3. Maiti A, Erimban S, Daschakraborty S. **Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.** *Chemical Communications.* **Aug 2024.** DOI: **10.1039/d4cc03114h**. https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 4-5)
4. Wu J, Zhang H, Zhao Y, Yuan X, Cui Z. **Effect of Temperature on the Inocula Preservation, Mesophilic Anaerobic Digestion Start-Up, and Microbial Community Dynamics.** *Agronomy.* **Dec 2024.** DOI: **10.3390/agronomy14122991**. https://doi.org/10.3390/agronomy14122991 (wu2024effectoftemperature pages 2-3, wu2024effectoftemperature pages 1-2, wu2024effectoftemperature pages 3-5)
5. Maktabdar M, Wemmenhove E, Gkogka E, Dalgaard P. **Development of extensive growth and growth boundary models for mesophilic and psychrotolerant Bacillus cereus in dairy products (Part 1).** *Frontiers in Microbiology.* **Mar 2025.** DOI: **10.3389/fmicb.2025.1553885**. https://doi.org/10.3389/fmicb.2025.1553885 (maktabdar2025developmentofextensive pages 2-3)
6. de la Viuda V, Buceta J, Grobas I. **Physical communication pathways in bacteria: an extra layer to quorum sensing.** *Biophysical Reviews.* **Mar 2025.** DOI: **10.1007/s12551-025-01290-1**. https://doi.org/10.1007/s12551-025-01290-1 (viuda2025physicalcommunicationpathways pages 5-7)
7. Barbotin A, Juillot D, Wongdontree P, Carballido-López R. **Two temperature-dependent membrane fluidity regimes in gram-positive bacteria.** *mSphere.* **Jun 2026.** DOI: **10.1128/msphere.00095-26**. https://doi.org/10.1128/msphere.00095-26 (barbotin2026twotemperaturedependentmembrane pages 1-2)

Non-DOI / unclear bibliographic reliability in retrieved context:
- AlGhazali MA, Eljamay SM. *The role of temperature in microbial growth: a discussion and meta-analysis* (2025; journal/DOI not verified in retrieved context). (alghazali2025theroleof pages 3-9)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

3. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

4. (ramon2023ageneraloverview pages 22-23): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

5. (wu2024effectoftemperature pages 2-3): Jingwei Wu, Huan Zhang, Ye Zhao, Xufeng Yuan, and Zongjun Cui. Effect of temperature on the inocula preservation, mesophilic anaerobic digestion start-up, and microbial community dynamics. Agronomy, 14:2991, Dec 2024. URL: https://doi.org/10.3390/agronomy14122991, doi:10.3390/agronomy14122991. This article has 11 citations and is from a peer-reviewed journal.

6. (viuda2025physicalcommunicationpathways pages 5-7): Virgilio de la Viuda, Javier Buceta, and Iago Grobas. Physical communication pathways in bacteria: an extra layer to quorum sensing. Biophysical Reviews, 17:667-685, Mar 2025. URL: https://doi.org/10.1007/s12551-025-01290-1, doi:10.1007/s12551-025-01290-1. This article has 9 citations and is from a peer-reviewed journal.

7. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

8. (wu2024effectoftemperature pages 1-2): Jingwei Wu, Huan Zhang, Ye Zhao, Xufeng Yuan, and Zongjun Cui. Effect of temperature on the inocula preservation, mesophilic anaerobic digestion start-up, and microbial community dynamics. Agronomy, 14:2991, Dec 2024. URL: https://doi.org/10.3390/agronomy14122991, doi:10.3390/agronomy14122991. This article has 11 citations and is from a peer-reviewed journal.

9. (maiti2024extrememakeoverthe pages 4-5): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

10. (barbotin2026twotemperaturedependentmembrane pages 1-2): Aurélien Barbotin, Dimitri Juillot, Paprapach Wongdontree, and Rut Carballido-López. Two temperature-dependent membrane fluidity regimes in gram-positive bacteria. mSphere, Jun 2026. URL: https://doi.org/10.1128/msphere.00095-26, doi:10.1128/msphere.00095-26. This article has 0 citations and is from a peer-reviewed journal.

11. (alghazali2025theroleof pages 3-9): MA AlGhazali and SM Eljamay. The role of temperature in microbial growth: a discussion and meta-analysis. Unknown journal, 2025.

12. (maktabdar2025developmentofextensive pages 2-3): Maryam Maktabdar, Ellen Wemmenhove, Elissavet Gkogka, and Paw Dalgaard. Development of extensive growth and growth boundary models for mesophilic and psychrotolerant bacillus cereus in dairy products (part 1). Frontiers in Microbiology, Mar 2025. URL: https://doi.org/10.3389/fmicb.2025.1553885, doi:10.3389/fmicb.2025.1553885. This article has 9 citations and is from a peer-reviewed journal.

13. (wu2024effectoftemperature pages 3-5): Jingwei Wu, Huan Zhang, Ye Zhao, Xufeng Yuan, and Zongjun Cui. Effect of temperature on the inocula preservation, mesophilic anaerobic digestion start-up, and microbial community dynamics. Agronomy, 14:2991, Dec 2024. URL: https://doi.org/10.3390/agronomy14122991, doi:10.3390/agronomy14122991. This article has 11 citations and is from a peer-reviewed journal.