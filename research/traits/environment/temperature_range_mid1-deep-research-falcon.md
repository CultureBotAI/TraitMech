---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:31:22.003475'
end_time: '2026-06-18T02:51:14.488321'
duration_seconds: 1192.48
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range mid1
  trait_identifier: METPO:1000450
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 22\u201327 \xB0C, characteristic of mesophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Mesophilie, TR_22_to_27
  evidence_summary: "DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty\
    \ acids (Membrane-adaptation review supports the 22\u201327 \xB0C range as a lower\
    \ mesophile growth range.)"
  causal_graph_summary: 'temperature_range_mid1_lower_mesophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid1
- **METPO identifier:** METPO:1000450
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 22–27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 22–27 °C range as a lower mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid1_lower_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid1.yaml`.

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
- **Trait label:** temperature range mid1
- **METPO identifier:** METPO:1000450
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 22–27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 22–27 °C range as a lower mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid1_lower_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid1.yaml`.

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


## Microbial Trait Causal Graph Research Report: **temperature range mid1** (METPO:1000450)

### 1) Scope summary (trait meaning, assay context, boundaries)

**Trait definition (curation target).** *temperature range mid1* is a **growth-supporting ambient temperature range** spanning approximately **22–27 °C**, intended to represent a **lower-mesophile** growth window (i.e., below many canonical mesophile optima but still within mesophilic ecology). This trait should be interpreted as a **capability to grow over a specified temperature interval**, not as an organism’s single **optimal growth temperature (OGT)**.

**Relationship to nearby traits.** Many microbiology sources define **mesophiles** broadly (e.g., “thrive between 20 and 45 °C,” with optima often around 30–39 °C) and emphasize that the *optimum* is distinct from the *minimum* and *maximum* temperatures permitting growth. Thus, a microbe can be mesophilic overall while experiencing **mild cold stress** when shifted from its OGT (often 30–37 °C) down into ~25 °C, which overlaps the METPO:1000450 window. (fasesan2023physiologicalcharacteristicsamylase pages 35-38, moon2023temperaturemattersbacterial pages 1-3)

**Boundary cases (important for curation).**
- **Downshift from OGT to 22–27 °C (e.g., 37→25 °C)**: frequently treated as **cold shock** relative to the optimum and can induce rapid membrane- and RNA-level responses. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5, sidarta2024lipidphaseseparation pages 12-14)
- **“Mesophilic temperature range” in environmental standards**: soil mesophilic microbial activity is often operationalized around **~25 °C** (e.g., standard-inspired incubation) and can be used as an experimental proxy for mesophilic community function; this aligns with the trait window. (romano2024changesinsoil pages 1-2)

### 2) Key concepts and definitions (current understanding)

**Growth temperature range vs. optimum (OGT).** Microbial growth is commonly described by **minimum**, **maximum**, and **optimum** temperatures; the optimum is where growth rate is highest, but survival/growth can occur across a broader range. (fasesan2023physiologicalcharacteristicsamylase pages 35-38)

**Mild cold stress / lower-mesophile physiology.** A shift from a mesophile’s OGT (e.g., *E. coli* 37 °C) down to ~23–25 °C can trigger “cold shock” regulatory programs because macromolecular processes (membrane fluidity, RNA folding, enzyme kinetics) become temperature-limited. (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)

**Homeoviscous adaptation (HVA).** A central mechanistic concept is **homeoviscous adaptation**: microbes adjust **membrane lipid composition** to keep the membrane in a functional liquid-crystalline state when temperature changes, including changes in **unsaturation**, **chain length**, **branching**, hopanoids, and pigments. (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5)

### 3) Candidate causal-graph entities (nodes), grouped by type

Below are candidate nodes likely to be reusable in `temperature_range_mid1.yaml`. CURIE suggestions are included where stable identifiers are widely used; for gene/protein nodes, **label-only is acceptable** unless you are curating species-specific instances.

#### A. Environmental / experimental factors
- **Ambient temperature ~22–27 °C** (METPO:1000450; also ENVO term may be used for “temperature”/“ambient temperature” if needed)
- **Temperature downshift** (e.g., 37→25 °C “mild cold shock”) (sidarta2024lipidphaseseparation pages 12-14)

#### B. Cellular structures / physical properties
- **Cell membrane** (GO:0016020 “membrane” as generic grounding)
- **Membrane fluidity / viscosity** (label; often treated as a physical property)
- **Membrane thickness** (label; key for DesK sensing) (sidarta2024lipidphaseseparation pages 1-2)

#### C. Pathways / biological processes (GO-level)
- **Homeoviscous adaptation / membrane lipid remodeling** (label; can be decomposed into GO:0006644 “phospholipid metabolic process”, GO:0008610 “lipid biosynthetic process”, etc.) (ramon2023ageneraloverview pages 2-4)
- **Fatty acid biosynthesis** (GO:0006633)
- **Fatty acid desaturation** (GO:0033522)
- **Cold shock response** (label; includes cold-shock proteins and RNA remodeling)
- **Heat shock response / proteostasis** (label; sigma factors, chaperones, proteases)
- **Transcriptional regulation by sigma factors** (GO:0006355 + sigma-factor specific nodes)

#### D. Genes / proteins / complexes (mechanistic control points)
**Membrane thickness/viscosity sensing and signaling (two-component system, Gram+ exemplar).**
- **DesK** (histidine kinase/phosphatase; label; UniProt depends on strain) (sidarta2024lipidphaseseparation pages 1-2)
- **DesR** (response regulator; label) (sidarta2024lipidphaseseparation pages 1-2)
- **des** (acyl-lipid fatty acid desaturase; label) (sidarta2024lipidphaseseparation pages 1-2)

**Fatty-acid synthesis control (enteric exemplar).**
- **FabF (β-ketoacyl-ACP synthase II)** (EC:2.3.1.179 often used for KASII; label acceptable) (ramon2023ageneraloverview pages 4-5)
- **FabA, FabB, FabH** (fatty-acid synthesis enzymes; label) (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5)
- **FabR** (transcriptional repressor regulating fabA/fabB; label) (ramon2023ageneraloverview pages 2-4)

**Cold-shock and temperature-sensing regulators.**
- **CspA** (cold shock protein; label) (moon2023temperaturemattersbacterial pages 3-5)
- **RNase R** (RNA degradation; label) (moon2023temperaturemattersbacterial pages 1-3)
- **CsdA** (cold-shock DEAD-box helicase; label) (moon2023temperaturemattersbacterial pages 1-3)
- **RpoS (σS)**, **RpoH (σ32)**, **RpoE (σ24)** (sigma factors; label) (moon2023temperaturemattersbacterial pages 3-5)
- **RseA/RseB/RseAB** (anti-sigma regulators for RpoE; label) (moon2023temperaturemattersbacterial pages 1-3)
- **DsrA sRNA** (promotes rpoS translation at low temperature; label) (moon2023temperaturemattersbacterial pages 3-5)

**Alternative/taxon-specific nodes for cyanobacteria (mesophilic optima near 25–26 °C).**
- **LcyB** (lycopene β-cyclase; carotenoid-related, linked to membrane FA unsaturation pathway context) (qian2023genomicinsightson pages 9-11)
- **GlgX / GlgP** (glycogen debranching enzyme / glycogen phosphorylase; carbon storage control) (qian2023genomicinsightson pages 9-11)

#### E. Chemicals / metabolites (CHEBI candidates)
- **cis-vaccenic acid (18:1 Δ11)** (CHEBI identifier exists; curate if needed) (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5)
- **Branched-chain fatty acids (BCFAs)**: **iso-BCFAs**, **anteiso-BCFAs**, e.g., **anteiso-C15:0** (CHEBI exists for many specific FAs; otherwise label nodes) (wu2023molecularmechanismsof pages 3-5)
- **Hopanoids (unsaturated hopanoids)** (CHEBI exists for some hopanoids; label if unspecified) (ramon2023ageneraloverview pages 4-5)
- **ATP/ADP** (CHEBI) (moon2023temperaturemattersbacterial pages 3-5)
- **Compatible solutes / osmoprotectants**: e.g., glycine betaine/proline betaine (CHEBI), if needed for broader environment trait graphs (qian2023genomicinsightson pages 9-11)

### 4) Recent developments (prioritizing 2023–2024)

#### 4.1 Membrane thickness sensing and mild cold shifts (explicit 37→25 °C evidence)
A 2024 *Microbiology Spectrum* study re-examined the **Bacillus subtilis DesK/DesR/des** system in vivo and reported that **des promoter (Pdes) activation occurs after a mild temperature shift 37→25 °C**, consistent with the idea that the system senses subtle membrane changes even when common fluidity reporters do not detect strong rigidification. (sidarta2024lipidphaseseparation pages 12-14, sidarta2024lipidphaseseparation media 27897efc, sidarta2024lipidphaseseparation media 8ac70925)

#### 4.2 Integrative view of temperature response regulatory layers (thermosensors, sigma factors, RNA remodeling)
A highly cited 2023 review in *Journal of Microbiology* synthesized bacterial responses to temperature changes across:
- **DNA topology (supercoiling) as a thermosensor**
- **RNA thermometers** controlling translation by exposing/occluding Shine–Dalgarno sequences
- **Sigma-factor cascades** (RpoH/RpoE for heat stress; RpoS for general/low-temperature stress)
- **Cold shock proteins**, particularly **CspA**, which can represent a large fraction of protein synthesis after cold shock (quantified in the review). (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)

#### 4.3 Quantitative lipid signatures of cold adaptation (hopanoid unsaturation)
A 2023 cold-adaptation review summarized quantitative compositional shifts, including a reported example where **unsaturated hopanoids increased from 27% to 49% when growth temperature decreased from 20 to 4 °C**, supporting hopanoid unsaturation as an adaptation axis that can be represented as candidate nodes/edges (with caution about taxonomic generality). (ramon2023ageneraloverview pages 4-5)

### 5) Current applications and real-world implementations relevant to 22–27 °C

#### 5.1 Soil biodegradation processes operating at 20–25 °C (mesophilic community function)
A 2024 *Microbial Ecology* study on soil mulch degradation used **room temperature (20–25 °C)** as a mesophilic condition and reported substantial degradation of a biodegradable mulch: **up to 69.15% at room temperature** (and **88.90% at 30 °C**), while **45 °C resulted in no degradation** in their setup. This supports the practical relevance of the 22–27 °C window for environmental microbial function/processing. (romano2024changesinsoil pages 1-2)

#### 5.2 Cold/mesophilic-range wastewater or nitrogen cycling: aerobic denitrification under cooler conditions
A 2023 *Applied and Environmental Microbiology* study of *Bacillus simplex* H-b quantified temperature impacts on nitrate removal: **84.71% at 20 °C vs 27.22% at 5 °C**, with transcriptomic evidence that temperature shifts involve changes in respiratory electron transport, fatty-acid metabolism, membrane transport, EPS, and stress response categories—mechanistic handles relevant for engineered systems operating at the cool end of mesophily. (yang2023insightintothe pages 2-4)

### 6) Expert opinions / authoritative synthesis (mechanistic interpretation)

Across recent authoritative reviews, the consensus mechanistic framing is that **temperature affects multiple coupled constraints**—membrane physical state, RNA structure/translation, and protein folding/quality control—so adaptation is typically **multifactorial** rather than single-gene. The membrane is emphasized as a *central integrator* because respiration-associated proteins reside there and temperature-driven rigidification can alter permeability and enzyme function, motivating lipid remodeling (HVA) as a primary causal axis. (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4)

### 7) Candidate causal edges (triples) with evidence

The following table is provided as a curation-ready shortlist of mechanistic edges for inclusion in a TraitMech causal graph for METPO:1000450.

| Edge (subject–predicate–object) | Mechanistic rationale (1 sentence) | Evidence snippet (short quote) | Source (first author year, DOI, URL, publication month/year if present) | Curation notes/uncertainty |
|---|---|---|---|---|
| temperature decrease to ~25 °C → causes → membrane rigidification/thickening | Mild cooling from a warmer mesophilic condition can reduce membrane fluidity and increase bilayer thickness, creating the initiating physical state for adaptation. | “membrane rigidification and increased thickness act as the primary physical signal” and DesK “detects membrane thickness changes when shifted from 37°C to 25°C” (ramon2023ageneraloverview pages 4-5, sidarta2024lipidphaseseparation pages 12-14) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023; Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong for Bacillus-based mechanism; direct 37→25 °C evidence is taxon-specific. |
| membrane thickening/rigidification → activates → DesK kinase-dominant state | The Bacillus DesK sensor is switched by physical membrane changes into a signaling-active kinase state. | “membrane rigidification and thickening upon cooling activates a kinase-dominant state” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong, but specific to DesK-containing taxa. |
| DesK kinase activity → autophosphorylates at → His188 | Autophosphorylation is the immediate biochemical step converting physical sensing into phosphosignaling. | “DesK… autophosphorylates at His188” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong and specific; residue-level detail appropriate for node grounding if desired. |
| phosphorylated DesK → phosphorylates → DesR | Phosphate transfer to the response regulator propagates the cold-sensing signal to transcriptional control. | “phosphorylating DesR” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong, Bacillus-specific two-component edge. |
| phosphorylated DesR → activates transcription of → des | Activated DesR turns on the lipid desaturase gene needed for rapid membrane fluidization. | “P-DesR tetramerizes, binds Pdes and induces expression of the des desaturase” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong, direct transcriptional edge. |
| des (fatty-acid desaturase) expression → increases → fatty-acid desaturation | Des encodes the enzyme that introduces double bonds into existing membrane lipids during cold adaptation. | “Des catalyzes desaturation of fatty acyl chains” and “The des gene is responsible for coding the only FA desaturase” (sidarta2024lipidphaseseparation pages 1-2, ramon2023ageneraloverview pages 4-5) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024; Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Strong for desaturase function; exact substrate scope varies by taxon. |
| fatty-acid desaturation → increases → membrane fluidity | Double bonds disrupt tight acyl-chain packing, reversing cold-induced rigidification. | “fluidizing the membrane and reducing thickness” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong and broadly conserved principle. |
| increased membrane fluidity/thinner membrane → promotes → DesK phosphatase activity | Once fluidity is restored, DesK switches off the response, forming a negative-feedback loop. | “resulting fluidization triggers DesK phosphatase activity to dephosphorylate DesR” (sidarta2024lipidphaseseparation pages 1-2) | Sidarta 2024, DOI:10.1128/spectrum.03925-23, https://doi.org/10.1128/spectrum.03925-23, Jun 2024 | Strong feedback edge; suitable for causal graph. |
| cooling → increases → cis-vaccenic acid | Rapid accumulation of cis-vaccenic acid is a classic membrane adaptation to lower temperature. | “When the temperature drops, only cis-vaccenic acid content increases… quickly” (ramon2023ageneraloverview pages 2-4) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Strong, but described mainly from E. coli-type pathway. |
| FabF activity → promotes synthesis of → cis-vaccenic acid | FabF catalyzes the elongation step that yields the cis-vaccenoyl precursor during cooling. | “FabF… catalyzes the final elongation from palmitoleoyl-ACP to the precursor of cis-vaccenoyl-ACP” (ramon2023ageneraloverview pages 4-5) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Strong enzymatic edge; best curated as pathway-level support in enteric/related bacteria. |
| FabR → regulates expression of → fabA/fabB | FabR couples fatty-acid status to transcription of unsaturated-fatty-acid biosynthesis genes. | “fabA/fabB transcription is regulated by FabR” and FabR “modulates fabA/fabB expression” (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Strong for E. coli-like UFA regulation; not universal across bacteria. |
| branched-chain amino acids (valine/leucine/isoleucine) → serve as precursors for → iso/anteiso-branched fatty acids | BCFA synthesis links amino-acid availability to membrane remodeling under cooler conditions. | “Iso- and anteiso-branched FAs are derived from valine, leucine, and isoleucine precursors” (ramon2023ageneraloverview pages 4-5) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Strong biochemical precursor edge. |
| isoleucine availability → increases → anteiso-BCFA synthesis | In Bacillus subtilis, isoleucine availability specifically biases branching toward the more fluidizing anteiso form. | “B. subtilis branching depends on the presence of isoleucine in the culture medium” (ramon2023ageneraloverview pages 4-5) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Strong but taxon-specific. |
| anteiso-branched fatty acids → increase → membrane fluidity | Anteiso chains disorder lipids more effectively than iso chains, supporting growth at lower temperatures. | “anteiso-BCFAs are more effective at fluidizing membranes than iso-BCFAs” (wu2023molecularmechanismsof pages 3-5) | Wu 2023, DOI:10.3390/cells12101353, https://doi.org/10.3390/cells12101353, May 2023 | Strong, generalizable across many Gram-positives. |
| lower temperature (20→4 °C) → increases → unsaturated hopanoids | Hopanoid unsaturation is another lipid-level route to preserve membrane function during cooling. | “As the growth temperature decreased from 20 to 4 °C, the total percent of unsaturated hopanoids increased from 27 to 49%” (ramon2023ageneraloverview pages 4-5) | Ramón 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, Jul 2023 | Quantitative and useful, but based on a psychrotolerant methanotroph example; extrapolation to all mid1 microbes should be cautious. |
| low temperature / DsrA sRNA → increases translation of → rpoS | Low-temperature induction of DsrA elevates the general stress sigma factor RpoS post-transcriptionally. | “RpoS as a low-temperature/stress sigma factor whose rpoS translation is promoted by the small RNA DsrA” (moon2023temperaturemattersbacterial pages 3-5) | Moon 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x, Mar 2023 | Strong in enteric models; indirect for 22–27 °C trait but mechanistically relevant to lower-mesophile shifts. |
| cold shock → induces → CspA RNA-binding protein | CspA helps maintain RNA functionality when colder temperatures stabilize inhibitory secondary structures. | “Cold-shock proteins (notably CspA) bind RNA and help maintain single-stranded regions; CspA can constitute ~15% of protein synthesis after cold shock” (moon2023temperaturemattersbacterial pages 3-5) | Moon 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x, Mar 2023 | Strong cold-shock edge; response magnitude is organism- and assay-dependent. |
| temperature-dependent RNA thermometer melting → exposes → Shine-Dalgarno sequence | RNA thermometers provide rapid translational control by altering ribosome access as temperature changes. | “5'-UTR cis-elements… occlude or expose Shine-Dalgarno sequences to control translation” (moon2023temperaturemattersbacterial pages 1-3) | Moon 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x, Mar 2023 | Strong general mechanism, but often associated with heat upshifts rather than specifically 22–27 °C cold adaptation. |
| temperature shift → changes → DNA supercoiling | DNA topology functions as a thermosensor that globally reprograms transcription after temperature change. | “DNA topology acts as a thermosensor” and “Cold stress enhances negative DNA supercoiling” (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5) | Moon 2023, DOI:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x, Mar 2023 | Strong systems-level edge, but broad and not uniquely diagnostic for mid1. |
| incubation at 20–25 °C → supports → mesophilic soil microbial activity and biodegradable mulch degradation | The mid1 range overlaps an experimentally useful mesophilic window for real-world soil microbial processing. | “mesophilic temperature range (10 to 45 °C)” and white mulch degradation reached “69.15% at room temperature” (20–25 °C) versus “88.90% at 30 °C” (romano2024changesinsoil pages 1-2) | Romano 2024, DOI:10.1007/s00248-024-02420-0, https://doi.org/10.1007/s00248-024-02420-0, Jul 2024 | Application edge rather than intrinsic mechanism; should be curated separately from cell-level causal edges. |
| low temperature shift → redirects nitrogen use toward → assimilation rather than dissimilatory denitrification | Cooler conditions can reallocate metabolism away from denitrification while still supporting survival/growth. | “At low temperatures, more nitrogen was utilized for assimilation” and nitrate removal was “27.22% at 5°C vs 84.71% at 20°C” (yang2023insightintothe pages 2-4) | Yang 2023, DOI:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22, Feb 2023 | Strong for Bacillus simplex H-b; temperature tested was colder than mid1, so relevance to 22–27 °C is inferred, not direct. |


*Table: This table lists candidate subject–predicate–object edges for the temperature_range_mid1 trait, emphasizing mechanistic support for lower-mesophile growth and highlighting where evidence is taxon-specific or indirect. It is useful as a curation-ready starting point for selecting robust versus uncertain edges for a TraitMech graph.*

### 8) Notes on ontology grounding (CURIE suggestions)

Because TraitMech graphs typically mix organism-agnostic mechanisms with organism-specific implementations, the recommended approach is:
- Represent **physical/phenomenological nodes** as **label nodes** (e.g., “membrane thickness,” “membrane fluidity”) unless a stable ontology term is already in your stack.
- For **genes/proteins**, use **label nodes** unless the trait YAML is intended to be taxon-specific; then map to **UniProt** or locus tags.
- For **processes**, prefer **GO** when straightforward (e.g., fatty acid biosynthesis GO:0006633; membrane GO:0016020).
- For **metabolites**, prefer **CHEBI** when a specific species is used (e.g., cis-vaccenic acid), otherwise use class-level label nodes (“branched-chain fatty acids”).

### 9) Warnings / non-curation-ready claims

1. **Taxon specificity:** DesK/DesR/des is best supported in **Bacillus** and relatives; do not assume all lower-mesophiles use this system, though the *principle* of membrane-thickness/viscosity sensing is broad. (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)
2. **Temperature mismatch:** Some quantitative lipid data (e.g., hopanoid unsaturation 20→4 °C) are colder than mid1 and should be curated as **general cold-adaptation edges** with an “uncertain for 22–27 °C” note. (ramon2023ageneraloverview pages 4-5)
3. **Application vs mechanism separation:** Soil mulch degradation at 20–25 °C supports the *ecological relevance* of mesophilic communities at this range, but it is not a direct cell-level mechanism and should be curated in a separate “environment/application” layer. (romano2024changesinsoil pages 1-2)
4. **Do not conflate OGT with growth range:** Many mesophiles have OGT ~30–39 °C; the 22–27 °C window can represent **sub-optimal but growth-permissive** conditions with mild cold stress responses. (fasesan2023physiologicalcharacteristicsamylase pages 35-38, moon2023temperaturemattersbacterial pages 1-3)

---

## DOI-first bibliography (with URLs and publication dates where available)

1. **Sidarta M**, et al. *Lipid phase separation impairs membrane thickness sensing by the Bacillus subtilis sensor kinase DesK.* **Microbiology Spectrum** (Jun **2024**). DOI: **10.1128/spectrum.03925-23**. URL: https://doi.org/10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparation pages 1-2, sidarta2024lipidphaseseparation pages 12-14)

2. **Román I**, et al. *Changes in Soil Microbial Communities Induced by Biodegradable and Polyethylene Mulch Residues Under Three Different Temperatures.* **Microbial Ecology** (Jul **2024**). DOI: **10.1007/s00248-024-02420-0**. URL: https://doi.org/10.1007/s00248-024-02420-0 (romano2024changesinsoil pages 1-2)

3. **Moon S**, et al. *Temperature Matters: Bacterial Response to Temperature Change.* **Journal of Microbiology** (Mar **2023**). DOI: **10.1007/s12275-023-00031-x**. URL: https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3, moon2023temperaturemattersbacterial pages 3-5)

4. **Ramón A**, et al. *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* **Brazilian Journal of Microbiology** (Jul **2023**). DOI: **10.1007/s42770-023-01057-4**. URL: https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 4-5)

5. **Yang Q**, et al. *Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: Bacillus simplex H-b.* **Applied and Environmental Microbiology** (Feb **2023**). DOI: **10.1128/aem.01928-22**. URL: https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 2-4)

6. **Qian M**, et al. *Genomic Insights on the Carbon-Negative Workhorse: Systematical Comparative Genomic Analysis on 56 Synechococcus Strains.* **Bioengineering** (Nov **2023**). DOI: **10.3390/bioengineering10111329**. URL: https://doi.org/10.3390/bioengineering10111329 (qian2023genomicinsightson pages 9-11)

7. **Wu G**, et al. *Molecular Mechanisms of Lipid-Based Metabolic Adaptation Strategies in Response to Cold.* **Cells** (May **2023**). DOI: **10.3390/cells12101353**. URL: https://doi.org/10.3390/cells12101353 (wu2023molecularmechanismsof pages 3-5)

8. (Background definitional source captured in evidence set; lower authority) **Fasesan DE**. Definitions of temperature minima/maxima/optimum; mesophile range context (2023; venue unclear). (fasesan2023physiologicalcharacteristicsamylase pages 35-38)


References

1. (fasesan2023physiologicalcharacteristicsamylase pages 35-38): DE FASESAN. Physiological characteristics, amylase properties and metagenomic analyses of bacterial and fungal communities from ikogosi …. Unknown journal, 2023.

2. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

3. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

4. (sidarta2024lipidphaseseparation pages 12-14): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (romano2024changesinsoil pages 1-2): Ida Romano, Valeria Ventorino, Mariachiara Schettino, Giuseppina Magaraci, and Olimpia Pepe. Changes in soil microbial communities induced by biodegradable and polyethylene mulch residues under three different temperatures. Microbial Ecology, Jul 2024. URL: https://doi.org/10.1007/s00248-024-02420-0, doi:10.1007/s00248-024-02420-0. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

7. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

8. (sidarta2024lipidphaseseparation pages 1-2): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (qian2023genomicinsightson pages 9-11): Meiwen Qian, Xiao Han, Jiongqin Liu, Ping Xu, and Fei Tao. Genomic insights on the carbon-negative workhorse: systematical comparative genomic analysis on 56 synechococcus strains. Bioengineering, 10:1329, Nov 2023. URL: https://doi.org/10.3390/bioengineering10111329, doi:10.3390/bioengineering10111329. This article has 3 citations.

10. (wu2023molecularmechanismsof pages 3-5): Gang Wu, Ralf Baumeister, and Thomas Heimbucher. Molecular mechanisms of lipid-based metabolic adaptation strategies in response to cold. Cells, 12:1353, May 2023. URL: https://doi.org/10.3390/cells12101353, doi:10.3390/cells12101353. This article has 87 citations.

11. (sidarta2024lipidphaseseparation media 27897efc): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

12. (sidarta2024lipidphaseseparation media 8ac70925): Margareth Sidarta, Ana I. Lorente Martín, Anuntxi Monsalve, Gabriela Marinho Righetto, Ann-Britt Schäfer, and Michaela Wenzel. Lipid phase separation impairs membrane thickness sensing by the <i>bacillus subtilis</i> sensor kinase desk. Jun 2024. URL: https://doi.org/10.1128/spectrum.03925-23, doi:10.1128/spectrum.03925-23. This article has 5 citations and is from a domain leading peer-reviewed journal.

13. (yang2023insightintothe pages 2-4): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

14. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.