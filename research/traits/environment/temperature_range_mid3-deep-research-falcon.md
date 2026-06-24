---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:33:56.626987'
end_time: '2026-06-18T02:55:18.094540'
duration_seconds: 1281.47
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
  causal_graph_summary: 'temperature_range_mid3_upper_mesophile: 3 nodes, 2 edges'
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
- **METPO identifier:** METPO:1000452
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 30–34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C range as the upper-mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid3_upper_mesophile: 3 nodes, 2 edges

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
- **METPO identifier:** METPO:1000452
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 30–34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C range as the upper-mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid3_upper_mesophile: 3 nodes, 2 edges

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


## Microbial Trait Causal Graph Curation Report: **temperature range mid3** (METPO:1000452)

### Scope summary (TraitMech curation focus)
**Trait definition (curation target):** *temperature range mid3* represents a temperature-range phenotype in which growth is supported across approximately **30–34 °C**, intended to capture an “upper-mesophile” growth-supporting ambient range (mesophilic physiology). This class should be curated as a **growth-supporting temperature window** (not necessarily the exact optimum), and should be interpreted relative to community standards for temperature categories.

**How it relates to standard temperature categories:** A recent microbiology review defines **mesophiles** as growing “between room temperature (around **20 °C**) and about **45 °C**,” while **psychrotolerants** can grow at **4 °C** (optimum >20 °C), and **thermophiles** have optima **50–80 °C**. Thus, **30–34 °C** lies squarely within mesophily and plausibly near the upper-middle portion of a common mesophile band (ramon2023ageneraloverview pages 1-2). A large-scale growth-temperature dataset study defines mesophiles more broadly as **15–50 °C**, again placing 30–34 °C unambiguously within mesophily (engqvist2018correlatingenzymeannotations pages 1-2).

**Boundary cases and distinctions:**
- Do **not** treat *temperature_range_mid3* as a universal ecological cutoff; “upper mesophile” is not a consistently standardized subcategory across microbiology sources. This trait is therefore best handled as an **ontology-driven subrange** within mesophily rather than a universally defined physiological class (ramon2023ageneraloverview pages 1-2, engqvist2018correlatingenzymeannotations pages 1-2).
- Distinguish from **psychrotolerant** phenotypes (ability to grow at 4 °C) and **thermophilic** phenotypes (optima ≥50 °C), which are defined by different growth boundaries and mechanisms (ramon2023ageneraloverview pages 1-2, rekadwad2023extremophilesthespecies pages 2-4).

---

### Key concepts & definitions (current understanding)
1. **Thermal niche / growth temperature range:** Microbial “temperature traits” can refer to minimum growth temperature (Tmin), optimum (Topt), maximum (Tmax), or *growth-supporting range*. The *temperature_range_mid3* concept corresponds to a **growth-supporting range** centered on **30–34 °C**, consistent with mesophilic physiology (ramon2023ageneraloverview pages 1-2, engqvist2018correlatingenzymeannotations pages 1-2).

2. **Homeoviscous adaptation (HVA):** A broad principle in which cells **remodel membrane lipids** to maintain a functional liquid-crystalline membrane state despite temperature change. Mechanisms include increasing unsaturation (often cis-MUFAs), shifting chain length, and adjusting branched-chain fatty acids and other lipids; membrane rigidification and **increased thickness** can act as a proximal signal for adaptive pathways (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5).

3. **Membrane thickness/fluidity as a signal:** Cooling tends to rigidify membranes and increase thickness; organisms can sense this via membrane-associated sensors, triggering adaptive gene expression and lipid remodeling (ramon2023ageneraloverview pages 4-5, sidarta2024lipidphaseseparation pages 1-2).

---

### Candidate causal-graph nodes (grouped by type)
Below are evidence-backed candidate nodes suitable for `data/traits/environment/temperature_range_mid3.yaml`. CURIEs are suggested where stable identifiers are standard; otherwise, label-only nodes are provided.

#### A) Phenotype / environmental nodes
- **Ambient temperature** (label-only; ENVO term may be possible depending on curation policy)
- **Growth-supporting temperature range 30–34 °C** (this trait instance)
- **Temperature downshift** / **cold shock** (label-only)
- **Membrane rigidification** (label-only)
- **Increased membrane thickness** (label-only)
- **Lipid phase separation** (label-only) (sidarta2024lipidphaseseparation pages 1-2)

#### B) Cellular structures & physical properties
- **Cytoplasmic membrane** (GO:0005886)
- **Membrane fluidity** (label-only; biophysical property) (ramon2023ageneraloverview pages 2-4)
- **Membrane thickness** (label-only; biophysical property) (sidarta2024lipidphaseseparation pages 1-2)

#### C) Genes / proteins / regulators (examples anchored in evidence)
**Bacillus subtilis (Gram-positive model for temperature sensing):**
- **DesK** (sensor histidine kinase/phosphatase; two-component system HK) (sidarta2024lipidphaseseparation pages 1-2)
- **DesR** (response regulator) (sidarta2024lipidphaseseparation pages 1-2)
- **des** (acyl-lipid desaturase; Δ5 desaturase) (sidarta2024lipidphaseseparation pages 1-2, mansilla2025fattyacidsynthesis pages 15-17)

**Escherichia coli (Gram-negative UFA synthesis/regulation):**
- **FabA** (introduces double bond in UFA biosynthesis intermediate) (ramon2023ageneraloverview pages 2-4)
- **FabB** (elongates UFA intermediate) (ramon2023ageneraloverview pages 2-4)
- **FabF** (elongation step toward cis-vaccenoyl-ACP precursors) (ramon2023ageneraloverview pages 4-5)
- **FabR** (transcriptional regulator sensing UFA/SFA acyl species; regulates fabA/fabB) (ramon2023ageneraloverview pages 2-4)

**Proteostasis / stress systems (candidate nodes; broader stress literature):**
- **DnaK (Hsp70)** (UniProt family-level node) (purwar2024adaptationsofpsychrophilic pages 6-7)
- **GroEL / GroES (Hsp60/Hsp10)** (UniProt family-level node) (purwar2024adaptationsofpsychrophilic pages 6-7)
- **Clp proteases / caseinolytic proteases** (PQCS components) (purwar2024adaptationsofpsychrophilic pages 6-7)

#### D) Pathways / processes
- **Two-component signal transduction system** (GO:0000160) (sidarta2024lipidphaseseparation pages 1-2)
- **Fatty acid biosynthetic process** (GO:0006633) (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4)
- **Fatty acid desaturation** (GO:0033539) (sidarta2024lipidphaseseparation pages 1-2, mansilla2025fattyacidsynthesis pages 15-17)
- **Membrane lipid remodeling / homeoviscous adaptation** (label-only; process concept) (ramon2023ageneraloverview pages 2-4)
- **Protein folding / proteostasis** (GO:0006457; PQCS concept) (purwar2024adaptationsofpsychrophilic pages 6-7)

#### E) Chemicals / lipid entities (candidate nodes; ground where possible)
- **Unsaturated fatty acids (UFAs)** (CHEBI family-level; label-only acceptable) (ramon2023ageneraloverview pages 2-4)
- **cis-vaccenic acid (18:1 Δ11)** (CHEBI term likely; label-only if not retrieved) (ramon2023ageneraloverview pages 2-4)
- **Palmitoleoyl-ACP / cis-vaccenoyl-ACP (ACP intermediates)** (Rhea/MetaCyc may exist; label-only acceptable) (ramon2023ageneraloverview pages 4-5)
- **Branched-chain fatty acids (BCFAs)** including **iso-BCFA** and **anteiso-BCFA** (label-only; may map to CHEBI families) (ramon2023ageneraloverview pages 4-5, mansilla2025fattyacidsynthesis pages 15-17)
- **Hopanoids (unsaturated hopanoids)** (CHEBI family-level; label-only acceptable) (ramon2023ageneraloverview pages 4-5)
- **Carotenoids / pigments** (CHEBI family-level; label-only acceptable) (ramon2023ageneraloverview pages 4-5)

---

### Candidate causal edges (evidence-backed triples)
The following table is designed for direct curation into a TraitMech-style causal graph.

| Subject node | Predicate | Object node | Mechanism/interpretation | Evidence snippet (short quote) | Source (DOI URL; year) | Confidence |
|---|---|---|---|---|---|---|
| temperature decrease / membrane rigidification | activates | DesK kinase state | In *Bacillus subtilis*, cooling thickens and rigidifies the membrane; DesK senses bilayer thickness and switches to kinase mode, initiating adaptation relevant to mesophilic temperature shifts around the 30–34 °C band. | “upon temperature decrease the membrane rigidifies and thickens, leading to a kinase-dominant DesK” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | high |
| DesK | phosphorylates | DesR | Core two-component signaling step linking membrane physical state to transcriptional response. | “DesK… autophosphorylates (His188) and phosphorylates DesR” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | high |
| phosphorylated DesR | activates transcription of | des | DesR-P binds the des promoter and induces lipid desaturation, a direct mechanism for restoring membrane fluidity during cooling. | “P-DesR tetramerizes, binds Pdes, and activates des expression” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | high |
| des (Δ5 desaturase) | introduces double bonds into | membrane fatty acyl chains | Des-mediated unsaturation fluidizes membranes and reduces bilayer thickness, supporting growth after downshift from warmer mesophilic conditions. | “Des introduces double bonds into fatty acyl chains, fluidizing the membrane and reducing thickness” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | high |
| increased unsaturated fatty acids | decreases | membrane thickness / order | Negative feedback in the DesK–DesR–Des module: restored fluidity switches DesK away from kinase mode. | “lipid desaturation… causes membrane fluidization and a concomitant decrease in bilayer thickness, which triggers DesK phosphatase activity” (sidarta2024lipidphaseseparation pages 2-5) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | high |
| DesK phosphatase state | represses | des expression | Once membrane order is restored, the response is shut off; this supports homeostasis rather than constitutive desaturation. | “trigger[s] DesK phosphatase activity and negatively regulates des expression” (sidarta2024lipidphaseseparation pages 2-5) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | high |
| mild cold shock (37→25 °C) | induces | Pdes reporter activity | Shows that subtle temperature shifts within or near mesophilic regimes can trigger the Des system. | “a 2-h shift from 37°C to 25°C produced significant Pdes activation” (sidarta2024lipidphaseseparation pages 2-5) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | medium |
| severe cold shock / lipid phase separation | impairs | DesK thickness sensing | Stronger cold or membrane phase separation can mislocalize DesK and uncouple sensing from adaptation; important caution for curation. | “phase separation… can partition DesK into fluid domains, impairing thickness sensing” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta et al. 2024, https://doi.org/10.1128/spectrum.03925-23; 2024 | medium |
| increased membrane order (reduced fluidity) | drives | DesK kinase-dominant state | Independent corroboration from review synthesis; membrane physical state is the proximate signal. | “increased membrane order (reduced fluidity) drives DesK to a kinase-dominant state” (mansilla2025fattyacidsynthesis pages 15-17) | Mansilla & de Mendoza 2025, https://doi.org/10.1128/mmbr.00069-23; 2025 | high |
| DesK/DesR system | controls | des transcription | Review-level consensus on the canonical *B. subtilis* cold-response pathway. | “The two-component system DesK… and DesR… controls des transcription” (mansilla2025fattyacidsynthesis pages 15-17) | Mansilla & de Mendoza 2025, https://doi.org/10.1128/mmbr.00069-23; 2025 | high |
| lower temperature | shifts | iso/anteiso branched-chain fatty acid ratio toward anteiso | In *B. subtilis*, anteiso-BCFAs are more fluidizing than iso-BCFAs; remodeling supports membrane function as temperature falls. | “switching from iso to anteiso SFA” and “anteiso-branched vs higher-melting iso-branched FAs” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| isoleucine-derived anteiso-BCFAs | increases | membrane fluidity | Anteiso-branched chains lower membrane melting behavior and are part of long-term temperature adaptation in Gram-positives. | “a-BCFAs derived from isoleucine promote greater membrane fluidity” (mansilla2025fattyacidsynthesis pages 15-17) | Mansilla & de Mendoza 2025, https://doi.org/10.1128/mmbr.00069-23; 2025 | high |
| low temperature | increases | cis-vaccenic acid (18:1) | In Gram-negative bacteria such as *E. coli*, rapid enrichment of cis-vaccenic acid is a characteristic homeoviscous response. | “cis-vaccenic (18:1) rises quickly when temperature drops” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| FabA | introduces double bonds into | unsaturated fatty acid precursor | FabA is part of the anaerobic UFA synthesis route supporting membrane unsaturation in Gram-negative mesophiles. | “FabA introduces double bonds in a 10-carbon intermediate” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| FabB | elongates | unsaturated fatty acid intermediate | FabB extends the FabA-generated unsaturated intermediate, contributing to UFA production. | “FabB elongates that intermediate” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| FabF | catalyzes elongation of | palmitoleoyl-ACP to cis-vaccenoyl-ACP precursor | Provides a more specific biochemical step linking fatty acid synthesis to cold-associated UFA remodeling. | “FabF… catalyzes the elongation from palmitoleoyl-ACP… to precursors of cis-vaccenoyl-ACP” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| FabR bound to UFA acyl species | represses | fabA/fabB transcription | Regulatory link coupling fatty acid composition to further UFA synthesis in *E. coli*. | “FabR senses fatty-acyl species… and regulates fabA/fabB promoters — binding of UFAs to FabR increases repression-promoter affinity” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| temperature decrease | causes | membrane rigidification and increased thickness | General physical trigger underlying homeoviscous adaptation across microbes. | “membrane rigidification and increased thickness… are proposed as sensing signals that trigger adaptive responses” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| homeoviscous adaptation | maintains | liquid-crystalline membrane state | Broad mechanism relevant to upper-mesophile growth: cells preserve membrane function across temperature fluctuations. | “maintain the liquid‑crystalline phase at low temperature” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |
| low temperature | upregulates | GroEL / DnaK / GroES / Clp proteostasis functions | Chaperones and proteases counter protein misfolding during temperature stress; useful as candidate nodes, but evidence is broader cold-stress rather than specific to 30–34 °C. | “Protein and RNA/DNA chaperones play critical roles…” and “Specific chaperones… include caseinolytic proteases (Clps), GroEL, DnaK, GroES” (purwar2024adaptationsofpsychrophilic pages 6-7) | Purwar & Srivastava 2024, https://doi.org/10.37256/amtt.5220244537; 2024 | medium |
| low temperature stress | increases risk of | protein misfolding / cold denaturation | Mechanistic rationale for including proteostasis nodes in a temperature-trait graph. | “cold denaturation… weakens hydrophobic interactions and increases the risk of protein misfolding” (purwar2024adaptationsofpsychrophilic pages 6-7) | Purwar & Srivastava 2024, https://doi.org/10.37256/amtt.5220244537; 2024 | medium |
| adaptive mutation in fabG | may alter | fatty acid composition at lower temperature | Experimental-evolution evidence that altered fatty acid biosynthesis can shift temperature-growth behavior, but taxon-specific and not directly an upper-mesophile determinant. | “a nonsynonymous mutation in fabG… may have altered fatty acid composition” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Lehmann et al. 2023, https://doi.org/10.3389/fmicb.2023.1265216; 2023 | uncertain |
| increased plasmalogens / shorter-chain fatty acids | associated with | adaptation to reduced growth temperature optimum | Supports membrane-lipid remodeling as a causal lever in temperature adaptation, though from a thermophile evolving downward. | “increased plasmalogens and a reduction in lipid chain length with decreasing temperature” (lehmann2023adaptivelaboratoryevolution pages 6-7) | Lehmann et al. 2023, https://doi.org/10.3389/fmicb.2023.1265216; 2023 | uncertain |
| mesophilic temperature category | includes | 30–34 °C growth optimum/range | Trait-scope anchor: 30–34 °C clearly falls within mesophily, supporting the interpretation of “upper mesophile.” | “mesophiles (15–50 °C)” (engqvist2018correlatingenzymeannotations pages 1-2) | Engqvist 2018, https://doi.org/10.1186/s12866-018-1320-7; 2018 | high |
| mesophiles | grow between | ~20 °C and ~45 °C | Alternative boundary source showing 30–34 °C sits in the upper half of a common mesophile span. | “Mesophiles are described as growing ‘between room temperature (around 20 °C) and about 45 °C.’” (ramon2023ageneraloverview pages 1-2) | Ramón et al. 2023, https://doi.org/10.1007/s42770-023-01057-4; 2023 | high |


*Table: This table summarizes evidence-backed candidate causal edges for the temperature range mid3 trait, emphasizing membrane sensing, fatty-acid remodeling, and proteostasis. It is formatted for direct use in TraitMech-style curation, with snippets, DOI-based sources, and confidence judgments.*

**Visual evidence supporting a key mechanism:** Sidarta et al. provide a schematic of the **DesK/DesR/des** membrane thickness-sensing negative-feedback circuit and the reporter constructs used to test it (sidarta2024lipidphaseseparation media 020e451d, sidarta2024lipidphaseseparation media 07e73b0a).

---

### Recent developments & latest research (prioritize 2023–2024)
1. **In vivo limits on membrane-thickness sensing via DesK:** A 2024 *Microbiology Spectrum* study reports that *B. subtilis* **des expression is only activated by mild temperature shocks** and proposes that **phase separation** can partition DesK into fluid domains, impairing thickness sensing under harsh cold shock or antibiotic stress—highlighting that “textbook” sensor models may behave differently in vivo than in vitro reconstitutions (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14).

2. **Subtle temperature shocks within mesophile regimes can trigger membrane adaptation circuits:** The same study observed **Pdes activation after a 37 → 25 °C shift** even when a standard fluorescent reporter (laurdan GP) did not detect a strong change in fluidity at that shift, suggesting that the Des system may respond to **very small** physical changes (sidarta2024lipidphaseseparation pages 2-5, sidarta2024lipidphaseseparation pages 12-14).

3. **Updated synthesis of multi-factor cold adaptation includes proteostasis modules:** A 2024 review emphasizes that **protein and nucleic-acid chaperones** (e.g., GroEL/DnaK, Clp proteases) can be upregulated under temperature stress to counter protein misfolding, which provides a rationale for including proteostasis nodes as modulators of growth across temperature ranges (purwar2024adaptationsofpsychrophilic pages 6-7).

---

### Current applications & real-world implementations (what maps to this trait)
The *temperature_range_mid3* trait is most directly relevant to applications operating in the **mesophilic band**, especially where **30–37 °C** operation is common:
- **Industrial and lab cultivation of mesophilic bacteria**: Many standard microbial growth protocols and bioprocesses are conducted near 30 °C or 37 °C, making membrane homeostasis mechanisms (fatty-acid remodeling; sensor/regulator circuits) operationally important for robustness to modest temperature deviations.
- **Adaptive laboratory evolution (ALE) for temperature tolerance:** Experimental evolution can shift growth-temperature properties via changes in lipid metabolism and regulatory networks; a 2023 ALE study in a thermophile highlights lipid remodeling (plasmalogens; chain-length) and mutations in fatty-acid biosynthesis genes (fabG) as candidate levers, illustrating a generalizable strategy though not specific to 30–34 °C (lehmann2023adaptivelaboratoryevolution pages 6-7).

(Engineering-scale examples at exactly 30–34 °C are often process-specific; the most directly citable mechanistic literature here focuses on conserved cellular adaptation modules rather than a single temperature setpoint.)

---

### Expert synthesis / interpretation (authoritative-source grounded)
- **Membranes act as “first responders” to temperature change:** Reviews emphasize that temperature shifts perturb membrane phase behavior, fluidity, and thickness, and that cells restore a functional membrane state via lipid remodeling (homeoviscous adaptation) (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5).
- **Two-component systems can directly couple membrane physics to gene regulation:** The DesK/DesR/des pathway is a canonical example in Gram-positive bacteria where a membrane-associated sensor histidine kinase toggles kinase/phosphatase states in response to membrane thickness/order and controls a desaturase gene to restore fluidity (sidarta2024lipidphaseseparation pages 1-2, mansilla2025fattyacidsynthesis pages 15-17).
- **Regulatory feedback tunes adaptation rather than maximizing unsaturation:** The DesK system is explicitly described as a negative-feedback loop in which desaturation reduces thickness and triggers DesK phosphatase activity to shut down des expression, consistent with maintaining homeostasis rather than drifting membrane composition (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 2-5).

---

### Relevant statistics & quantitative data (from recent/authoritative studies)
- **Temperature category boundaries:** Mesophiles grow ~**20–45 °C** (review definition) (ramon2023ageneraloverview pages 1-2) and **15–50 °C** (growth-temperature database definition) (engqvist2018correlatingenzymeannotations pages 1-2).
- **B. subtilis membrane fatty-acid composition context:** In LB-grown *B. subtilis*, membranes are reported as **highly branched (80–96% BCFAs)** and an **unsaturated:saturated ratio ~0.075** (sidarta2024lipidphaseseparation pages 12-14).
- **B. subtilis DesK system induction regime:** A **37 → 25 °C** downshift for **2 h** produced significant **Pdes activation** in the Sidarta et al. assays (sidarta2024lipidphaseseparation pages 2-5).
- **Hopanoid temperature-dependent shift (example from review synthesis):** Unsaturated hopanoids reported to rise from **27% to 49%** as growth temperature fell from **20 to 4 °C** in a cited bacterial example, illustrating a quantitative lipid remodeling response to temperature decrease (ramon2023ageneraloverview pages 4-5).

---

### Ontology grounding suggestions (non-exhaustive)
- **Trait:** METPO:1000452 (given)
- **Membrane:** GO:0005886
- **Two-component system:** GO:0000160
- **Fatty acid biosynthesis:** GO:0006633
- **Protein folding:** GO:0006457
- **DesK/DesR/des, FabA/FabB/FabF/FabR:** recommend grounding to **UniProt** (organism-specific) during curation once target taxa are determined.
- **cis-vaccenic acid; UFAs; hopanoids; carotenoids:** recommend grounding to **ChEBI** terms during curation (label-only acceptable until exact IDs are confirmed).

---

### Warnings / curation caveats (do not over-curate)
1. **“Upper mesophile (30–34 °C)” is an ontology subrange, not a universal physiological boundary.** Many sources define mesophiles broadly; avoid claiming universal taxonomic/ecological meaning for “upper mesophile” without organism-specific Tmin/Topt/Tmax data (ramon2023ageneraloverview pages 1-2, engqvist2018correlatingenzymeannotations pages 1-2).

2. **Mechanisms are often conserved, but gene names are taxon- and lifestyle-dependent.** DesK/DesR/des is a strong mechanistic module for *Bacillus* and related Gram-positives, but should not be assumed present or causal in all organisms expressing this trait (sidarta2024lipidphaseseparation pages 1-2, mansilla2025fattyacidsynthesis pages 15-17).

3. **Assay context matters:** Sidarta et al. highlight that **phase separation** can impair DesK sensing in vivo and that reporter readouts may respond to subtle shifts differently than standard fluidity dyes; edges involving “temperature → des induction” should be annotated with assay conditions (shift magnitude, time) and confidence (sidarta2024lipidphaseseparation pages 2-5, sidarta2024lipidphaseseparation pages 1-2).

4. **Proteostasis edges are broader-stress evidence:** Chaperone/protease nodes (DnaK, GroEL/ES, Clp) are supported as general low-temperature stress adaptors but are not specific to the 30–34 °C band; consider marking as **uncertain** unless organism-specific studies link them to growth limits around this range (purwar2024adaptationsofpsychrophilic pages 6-7).

---

## DOI-first bibliography (with URLs and publication dates where available)
- Sidarta M. et al. **“Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK.”** *Microbiology Spectrum* (2024-06). https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 1-2)
- Ramón A. et al. **“A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.”** *Brazilian Journal of Microbiology* (2023-07). https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)
- Purwar S., Srivastava S. **“Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.”** *Applied Microbiology: Theory & Technology* (2024-10). https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 6-7)
- Lehmann M. et al. **“Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.”** *Frontiers in Microbiology* (2023-10). https://doi.org/10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 6-7)
- Engqvist M.K.M. **“Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures.”** *BMC Microbiology* (2018-11). https://doi.org/10.1186/s12866-018-1320-7 (engqvist2018correlatingenzymeannotations pages 1-2)
- Rekadwad B.N. et al. **“Extremophiles: the species that evolve and survive under hostile conditions.”** *3 Biotech* (2023-08). https://doi.org/10.1007/s13205-023-03733-6 (rekadwad2023extremophilesthespecies pages 2-4)



References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (engqvist2018correlatingenzymeannotations pages 1-2): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 99 citations and is from a peer-reviewed journal.

3. (rekadwad2023extremophilesthespecies pages 2-4): Bhagwan Narayan Rekadwad, Wen-Jun Li, Juan M. Gonzalez, Rekha Punchappady Devasya, Arun Ananthapadmanabha Bhagwath, Ruchi Urana, and Khalid Parwez. Extremophiles: the species that evolve and survive under hostile conditions. 3 Biotech, Aug 2023. URL: https://doi.org/10.1007/s13205-023-03733-6, doi:10.1007/s13205-023-03733-6. This article has 49 citations and is from a peer-reviewed journal.

4. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

5. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

6. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

7. (mansilla2025fattyacidsynthesis pages 15-17): María Cecilia Mansilla and Diego de Mendoza. Fatty acid synthesis and utilization in gram-positive bacteria: insights from <i>bacillus subtilis</i>. Microbiology and Molecular Biology Reviews, Jun 2025. URL: https://doi.org/10.1128/mmbr.00069-23, doi:10.1128/mmbr.00069-23. This article has 7 citations and is from a domain leading peer-reviewed journal.

8. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

9. (sidarta2024lipidphaseseparation pages 2-5): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

10. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

11. (sidarta2024lipidphaseseparation media 020e451d): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

12. (sidarta2024lipidphaseseparation media 07e73b0a): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.