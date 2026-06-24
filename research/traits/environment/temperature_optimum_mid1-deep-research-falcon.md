---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:03:44.963769'
end_time: '2026-06-18T02:21:30.503426'
duration_seconds: 1065.54
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum mid1
  trait_identifier: METPO:1000443
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ between approximately 22 and 27 \xB0C, characteristic of mesophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Mesophilie, TO_22_to_27
  evidence_summary: 'DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty
    acids (Membrane-adaptation review supports moderate-temperature optima matched
    by homoviscous lipid composition as the mesophile setpoint.)'
  causal_graph_summary: 'temperature_optimum_mid1_lower_mesophile: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid1
- **METPO identifier:** METPO:1000443
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 22 and 27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate-temperature optima matched by homoviscous lipid composition as the mesophile setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid1_lower_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid1.yaml`.

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
- **Trait label:** temperature optimum mid1
- **METPO identifier:** METPO:1000443
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 22 and 27 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_22_to_27
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports moderate-temperature optima matched by homoviscous lipid composition as the mesophile setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid1_lower_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid1.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **temperature optimum mid1** (METPO:1000443)

### Scope summary (trait meaning and boundaries)
**Trait definition (curation target).** *temperature optimum mid1* denotes a microbial phenotype in which the **optimal growth temperature (OGT)**—the temperature yielding the **maximal growth rate**—falls in the approximate range **22–27 °C**, consistent with a *mesophilic* setpoint near room temperature. Operationally, OGT is defined as the temperature at which an organism attains its maximal growth rate, which requires measuring growth across multiple incubation temperatures (colette2025machinelearningfor pages 1-4).

**Relationship to adjacent traits and boundary cases.** Common classification schemes distinguish cold-adapted organisms using cardinal growth temperatures. In one operational scheme: (i) **psychrophiles** can grow at 0 °C, have an optimum near 15 °C, and do not grow at 20 °C; (ii) **psychrotolerant/psychrotrophs** can grow at 4 °C but have optima **above 20 °C**; and (iii) **mesophiles** grow roughly from ~20 °C to ~45 °C (ramon2023ageneraloverview pages 1-2). A complementary “cardinal temperature” scheme (Morita-style) reports typical psychrophile minimum/optimum/maximum of ≤0/≤15/≤20 °C and psychrotroph values of ≥0/≥20/≥30 °C, with the note that mesophiles can still show cold resistance and may grow (slowly) at 4–12 °C (flegler2022complementaryadaptationsof pages 13-15). Thus, **22–27 °C** OGT organisms are generally **mesophiles**, but some may also meet **psychrotolerant** criteria if they can grow at ~4 °C (ramon2023ageneraloverview pages 1-2, flegler2022complementaryadaptationsof pages 13-15).

**Assay/curation notes.** OGT values in databases may reflect differing record types (optimum vs “growth” temperatures), and ranges may be averaged during curation; these choices can blur boundaries near ~20–30 °C (colette2025machinelearningfor pages 4-7). For TraitMech, treat **temperature optimum** as a phenotype derived from a growth-rate-vs-temperature curve (or equivalent) rather than a single cultivation temperature (colette2025machinelearningfor pages 1-4, colette2025machinelearningfor pages 4-7).

---

## 1) Key concepts and definitions (current understanding)

### 1.1 Homeoviscous adaptation (HVA) as a central concept
A major mechanistic framework connecting temperature to growth performance is **homeoviscous adaptation (HVA)**: regulation of membrane lipid composition to maintain a functional membrane physical state under temperature shifts. Recent synthesis emphasizes that HVA begins with **membrane stress sensing** (candidate sensed parameters include **membrane fluidity** vs **lipid-packing density**) followed by remodeling toward **low-melting lipids** (e.g., mono- and polyunsaturated fatty acids, branched fatty acids, short-chain and hydroxylated fatty acids, plus headgroup remodeling) (maiti2024extrememakeoverthe pages 3-4). 

In bacterial cold adaptation contexts, membrane biophysics is often described using a **thermotropic phase transition temperature (Tm)** separating gel (ordered) from liquid-crystalline (functional) states; at Tm, “50% of membrane acyl chains melt,” motivating lipid remodeling below Tm (ramon2023ageneraloverview pages 2-4).

### 1.2 Lipid remodeling mechanisms relevant to mesophilic setpoints
Cold-side responses that can support an organism whose optimum is near 22–27 °C include: increasing **cis-unsaturated fatty acids**; shifting to **branched-chain fatty acids** with lower melting temperatures (notably *anteiso* forms); and changing other membrane modifiers such as **hopanoids/hopanols** and pigments (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23, ramon2023ageneraloverview pages 2-4). A quantitative example cited in a recent review: in one methanotroph, the fraction of **unsaturated hopanoids** increased from **27% to 49%** when temperature decreased from **20 °C to 4 °C** (ramon2023ageneraloverview pages 4-5).

### 1.3 Regulatory systems connecting temperature to lipid remodeling
A mechanistically detailed example of temperature sensing is the **Bacillus subtilis DesKR two-component system**, in which the membrane-bound histidine kinase **DesK** senses **membrane thickening/rigidification** upon temperature downshift and switches from phosphatase (high temperature) to kinase mode (low temperature). The mechanism includes a short N-terminal “buoy” motif (Lys10-Leu11-Asn12) that becomes buried in a thicker membrane at low temperature, triggering conformational changes that promote kinase activity; kinase-active DesK phosphorylates **DesR**, which induces **des** transcription (ramon2023ageneraloverview pages 5-7). The Des desaturase inserts double bonds into membrane fatty acids, fluidizing the membrane and reversing the signal (ramon2023ageneraloverview pages 5-7).

### 1.4 Protein stability and folding as a complementary determinant of temperature optima
Temperature also constrains growth through **protein folding/stability** and stress responses. A 2024 anammox adaptation study highlights **upregulation of chaperones** as a notable mechanism during thermal adaptation, consistent with a general role for chaperones in maintaining correct folding and protein conformational stability under temperature stress (christina2024mechanismsofanammox pages 1-5).

---

## 2) Candidate causal graph entities (nodes) with ontology grounding suggestions

### 2.1 Environmental and experimental factors
- **Ambient temperature** (ENVO:00002230 “temperature” may be suitable; otherwise label-only)
- **Temperature downshift / cold shock** (label-only)
- **Temperature upshift / heat stress** (label-only)
- **Growth medium / nutrient status** (label-only; influences fatty acid pools)
- **Bioreactor loading rate** (label-only; relevant in anammox adaptation where loading must be reduced during temperature increase) (christina2024mechanismsofanammox pages 1-5)

### 2.2 Phenotypes and biophysical states
- **Optimal growth temperature (OGT)** (label-only; operational definition supported) (colette2025machinelearningfor pages 1-4)
- **Membrane fluidity** (candidate: GO:0061024 “membrane organization” is too broad; keep label-only unless a precise GO term is chosen)
- **Membrane thickness/rigidification** (label-only)
- **Homeoviscous adaptation** (label-only process node) (maiti2024extrememakeoverthe pages 3-4)

### 2.3 Genes/proteins/regulators (examples with strong evidence)
- **DesK** (B. subtilis sensor histidine kinase; two-component sensor HK; consider GO:0000155 “two-component sensor activity” as function) (ramon2023ageneraloverview pages 5-7)
- **DesR** (response regulator) (ramon2023ageneraloverview pages 5-7)
- **des** (fatty acid desaturase gene; B. subtilis) (ramon2023ageneraloverview pages 5-7, ramon2023ageneraloverview pages 4-5)
- **fabA / fabB** (E. coli unsaturated fatty acid biosynthesis enzymes) (ramon2023ageneraloverview pages 2-4)
- **fabR** (transcriptional repressor of fabA/fabB) (ramon2023ageneraloverview pages 2-4)
- **fabF, fabZ** and related fatty-acid synthesis enzymes referenced as contributing to UFA control in cold adaptation contexts (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23)

### 2.4 Chemicals/metabolites/lipid classes
- **Unsaturated fatty acids (UFAs)** (CHEBI class; keep as label + CHEBI if matched) (ramon2023ageneraloverview pages 5-7)
- **cis-vaccenic acid** (CHEBI term exists but not resolved in current evidence; label-only acceptable) (ramon2023ageneraloverview pages 2-4)
- **Branched-chain fatty acids (iso/anteiso)** (label-only or CHEBI class) (ramon2023ageneraloverview pages 4-5)
- **Branched-chain amino acids**: valine, leucine, isoleucine (CHEBI terms available; used as precursors) (ramon2023ageneraloverview pages 4-5)
- **Hopanoids/hopanols** (CHEBI terms likely; label-only acceptable) (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23)
- **Carotenoids/pigments** (CHEBI classes; label-only acceptable) (ramon2023ageneraloverview pages 22-23)

### 2.5 Pathways/modules
- **Unsaturated fatty acid biosynthesis (E. coli pathway)** (MetaCyc/KEGG grounding possible but not asserted here) (ramon2023ageneraloverview pages 2-4)
- **Two-component signal transduction (DesKR)** (GO:0000160 “two-component signal transduction system” is a candidate) (ramon2023ageneraloverview pages 5-7)

---

## 3) Recent developments and latest research (prioritizing 2023–2024)

### 3.1 2023–2024 synthesis of membrane-centric mechanisms
A 2023 review emphasizes that membrane physical state and lipid composition are central determinants of temperature performance, highlighting specific lipid-modifying routes (e.g., desaturase-mediated insertion of double bonds; branching shifts such as iso→anteiso patterns) and additional lipid modifiers including hopanoids and pigments (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 22-23, ramon2023ageneraloverview pages 2-4). A 2024 Chemical Communications feature article generalizes this into a modern HVA framing in which membrane stress sensing (fluidity vs packing) triggers increases in low-melting lipid species (maiti2024extrememakeoverthe pages 3-4).

### 3.2 2024 computational advances: protein optimal temperature prediction at scale
A notable 2024 advance is GeoPoc, a structure- and language-model–informed predictor for protein optimal conditions. GeoPoc assembled a dataset of **175,905 non-redundant proteins** linked to organismal condition data and reported strong performance for optimal temperature prediction (internal validation **PCC ≈ 0.78**) and improvement over prior methods in **AUC** (reported as +2.3% in an independent test) (zhu2024accuratelypredictingoptimal pages 1-2). The study describes deriving **species-level optimal temperature** by aggregating predicted protein optima (mean across proteins for a species) (zhu2024accuratelypredictingoptimal pages 8-9). Interpretability analyses highlight physicochemical determinants; for example, importance aligns with conserved regions and implicates **hydrophobic cores** (aromatic rings, isoleucine) in preventing disintegration at high temperatures (zhu2024accuratelypredictingoptimal pages 6-7).

### 3.3 2024 applied physiology: anammox temperature adaptation
A 2024 bioRxiv preprint on anammox adaptation explicitly frames the field’s operational focus: anammox processes are widely implemented under **mesophilic conditions (30–35 °C)** and in mainstream wastewater under **10–25 °C**; performance can deteriorate above ~40 °C unless adaptation is gradual, and adaptation may require substantial reduction of loading rate (≤~50% of specific anammox activity) (christina2024mechanismsofanammox pages 1-5). Mechanistically, the study highlights **chaperone upregulation** and membrane lipid modifications, including a reported increase in ladderane lipid cyclization (p = 0.005) (christina2024mechanismsofanammox pages 1-5).

---

## 4) Current applications and real-world implementations (mesophilic temperature regime)

### 4.1 Wastewater nitrogen removal (anammox)
Operationally, anammox systems commonly run at **30–35 °C** (mesophilic) and have been applied at full scale under **10–25 °C** mainstream conditions, making temperature control and acclimation strategies directly relevant for any organism or community with a mid-mesophilic optimum (christina2024mechanismsofanammox pages 1-5).

### 4.2 Anaerobic digestion and sludge treatment
Most anaerobic digesters operate under **mesophilic conditions ~25–40 °C**, described as robust and stable due to diverse microbial communities; two-stage digestion (mesophilic then thermophilic) can increase solids reduction (e.g., reported TS reduction 45.6% for one operating schedule) (grubel2015hybridalkalihydrodynamicdisintegration pages 1-2). This underscores why temperature-optimum traits near room temperature are important for engineered consortia stability and conversion efficiency.

### 4.3 Biodegradation and bioremediation processes at ~20–30 °C
A 2024 applied study compiling biodegradation contexts lists multiple microbial processes with operational temperature ranges overlapping the mid-mesophilic band (e.g., 20–28 °C; 20–35 °C) and provides Arrhenius/Q10-style temperature-dependence metrics for microbial growth on pollutants (abubakar2024activationenergytemperature pages 3-4, abubakar2024activationenergytemperature pages 5-5). While not specific to a single gene mechanism, this supports the relevance of curated temperature optima for environmental process performance predictions.

---

## 5) Evidence-backed candidate causal edges (triples)
The following curation-ready edge table is provided as an artifact for YAML drafting.

| Subject node (label + CURIE) | Predicate | Object node (label + CURIE) | Evidence snippet/quote | Reference (DOI + URL + year) | Notes on strength/uncertainty |
|---|---|---|---|---|---|
| temperature downshift (label-only candidate; environmental factor) | causes | membrane thickening / rigidification (label-only candidate; biological process) | “At low temperature membrane thickening drives DesK into its kinase state” and “This change in the thickness of the membrane is the signal that sets in motion...” (ramon2023ageneraloverview pages 5-7, ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong mechanistic support in *Bacillus subtilis*; taxon-specific sensor details but broadly relevant to homeoviscous adaptation. |
| membrane thickening / rigidification (label-only candidate) | activates kinase activity of | DesK sensor histidine kinase (GO:0000155 candidate; label-only gene/protein node) | “At high temperature DesK is in a phosphatase state; at low temperature membrane thickening drives DesK into its kinase state” (ramon2023ageneraloverview pages 5-7) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong, but specific to the DesKR system of *B. subtilis* and close homologs. |
| DesK sensor histidine kinase (label-only candidate) | phosphorylates | DesR response regulator (label-only candidate) | “Kinase-active DesK phosphorylates DesR” (ramon2023ageneraloverview pages 5-7) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong within the DesKR two-component pathway. |
| phosphorylated DesR (label-only candidate) | induces transcription of | des fatty acid desaturase gene (label-only candidate) | “DesR, whose phosphorylated form induces des transcription” (ramon2023ageneraloverview pages 5-7) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong for *B. subtilis* cold-shock response. |
| des fatty acid desaturase gene / Des desaturase (label-only candidate) | increases abundance of | unsaturated fatty acids (CHEBI:59554 candidate class) | “The Des desaturase inserts double bonds in membrane fatty acids” (ramon2023ageneraloverview pages 5-7); “the des gene encodes the only fatty acid desaturase in this organism” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong for the stated organism; useful as a canonical mesophile membrane-adaptation edge. |
| unsaturated fatty acids (CHEBI:59554 candidate class) | increases | membrane fluidity (GO:0061024 candidate; label-only candidate) | “The Des desaturase inserts double bonds in membrane fatty acids, fluidizing the membrane and reversing the signal” (ramon2023ageneraloverview pages 5-7) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong causal link for homeoviscous adaptation. |
| temperature drop (label-only candidate; environmental factor) | increases abundance of | cis-vaccenic acid (CHEBI candidate unavailable) | “When the temperature drops, only cis-vaccenic acid content increases.” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong as a compositional response, but the statement is drawn from cited bacterial examples rather than a universal rule. |
| FabR transcriptional repressor (label-only candidate) | represses transcription of | fabA / fabB unsaturated FA biosynthesis genes (label-only candidates) | “FabR acting as a transcriptional repressor that senses UFA/SFA... and regulates fabA/fabB expression.” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong for enteric UFA regulation; useful but taxon-limited. |
| FabA β-hydroxydecanoyl-ACP dehydratase/isomerase (EC candidate) | introduces cis double bond into precursor for | unsaturated fatty acid biosynthesis (label-only pathway candidate) | “FabA introduces cis double-bonds into a 10-carbon chain; FabB elongates those intermediates” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong enzyme-function edge; pathway grounding may require external curation. |
| FabB β-ketoacyl-ACP synthase I (EC candidate) | elongates intermediates in | unsaturated fatty acid biosynthesis (label-only pathway candidate) | “FabA introduces cis double-bonds into a 10-carbon chain; FabB elongates those intermediates” (ramon2023ageneraloverview pages 2-4) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong enzyme-function edge. |
| branched-chain amino acids: valine / leucine / isoleucine (CHEBI candidates) | serve as precursors for | branched-chain fatty acids including anteiso fatty acids (CHEBI candidate class) | “Branched (iso/anteiso) FAs derive from branched-chain amino acid precursors (valine, leucine, isoleucine)” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong biochemical precursor relationship. |
| increased isoleucine-dependent branching / anteiso fatty acids (label-only candidate) | fluidizes | membrane (GO:0016020 candidate) | “B. subtilis modulates the ratio of lower-melting anteiso versus higher-melting iso branched FAs with temperature” and “the predominant, longer-term cold adaptation... relies on membrane fluidization via chain branching” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong in *Bacillus*; broader extrapolation to all mesophiles should be marked uncertain. |
| membrane physical state / fluidity (label-only candidate) | is sensed as input to | homeoviscous adaptation (GO:0008150-related label-only process candidate) | “HVA was first observed in E. coli and is described as a universal paradigm for membrane adaptation. The initial HVA step involves membrane stress sensing by sensor proteins; proposed sensed parameters include membrane fluidity... or alternatively lipid-packing density.” (maiti2024extrememakeoverthe pages 3-4) | Maiti et al. 2024, DOI:10.1039/d4cc03114h, https://doi.org/10.1039/d4cc03114h, 2024 | Good high-level mechanistic edge; sensor molecular identities remain incompletely resolved. |
| homeoviscous adaptation (label-only candidate) | remodels toward increased | low-melting lipids: MUFAs / PUFAs / branched FAs / short-chain FAs (CHEBI class candidates) | “Adaptive changes include increasing lipids with low melting temperatures: MUFAs, PUFAs, branched fatty acids, short-chain... hydroxylated fatty acids” (maiti2024extrememakeoverthe pages 3-4) | Maiti et al. 2024, DOI:10.1039/d4cc03114h, https://doi.org/10.1039/d4cc03114h, 2024 | Strong review-level support, but general rather than specific to 22–27 °C organisms. |
| hopanoids / hopanols (CHEBI candidates) | modulate ordering and phase behavior of | membrane lipids (label-only candidate) | “hopanoids/hopanols... order lipid chains and modulate phase transitions” (ramon2023ageneraloverview pages 4-5); “hopanoids/sterols and carotenoids... modulate membrane ordering, phase behavior and permeability” (ramon2023ageneraloverview pages 22-23) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Strong for membrane biophysics; direct causal link to the specific 22–27 °C optimum band is indirect. |
| lower temperature from 20 °C to 4 °C (label-only candidate) | increases fraction of | unsaturated hopanoids (label-only candidate) | “in one methanotroph the fraction of unsaturated hopanoids rose from 27% to 49% when temperature fell from 20 to 4 °C.” (ramon2023ageneraloverview pages 4-5) | Ramón et al. 2023, DOI:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4, 2023 | Quantitative and useful, but taxon-specific and not necessarily representative of mesophiles generally. |
| elevated temperature stress (label-only candidate) | induces upregulation of | chaperones (GO:0051082-related candidate) | “The most notable adaptation mechanisms included: (1) upregulation of chaperones” (christina2024mechanismsofanammox pages 1-5) | Karmann et al. 2024, DOI:10.1101/2024.07.23.604647, https://doi.org/10.1101/2024.07.23.604647, 2024 | Moderate evidence from a preprint and high-temperature adaptation experiment; still valuable as a general protein-stress mechanism. |
| chaperone upregulation (GO:0051082-related candidate) | promotes | correct protein folding / protein conformational stability (GO:0006457 candidate) | “stabilization of protein conformation via thermoprotectant enzymes and facilitation of correct protein folding (i.e., upregulation of chaperones)” (christina2024mechanismsofanammox pages 1-5) | Karmann et al. 2024, DOI:10.1101/2024.07.23.604647, https://doi.org/10.1101/2024.07.23.604647, 2024 | Moderate evidence; mechanistically plausible and widely accepted, but source is a preprint and not specific to mid1 mesophily. |
| gradual temperature increase with reduced loading rate (label-only experimental factor) | enables adaptation of | anammox biomass above mesophilic baseline (label-only candidate) | “successful adaptation when increasing temperature required reducing the original loading rate by at least half” (christina2024mechanismsofanammox pages 1-5) | Karmann et al. 2024, DOI:10.1101/2024.07.23.604647, https://doi.org/10.1101/2024.07.23.604647, 2024 | Useful assay/process edge; operational rather than intrinsic trait mechanism. |
| protein sequence/structure physicochemical properties (label-only candidate) | contribute to | predicted protein optimal temperature (label-only candidate) | “GeoPoc elucidates the critical physicochemical properties that contribute to enhancing protein thermostability” (zhu2024accuratelypredictingoptimal pages 1-2); “hydrophobic cores (e.g., aromatic rings and isoleucine) compact the interior and prevent structural disintegration at high temperatures” (zhu2024accuratelypredictingoptimal pages 6-7) | Zhu et al. 2024, DOI:10.1038/s42003-024-07436-3, https://doi.org/10.1038/s42003-024-07436-3, 2024 | Strong computational/statistical evidence; mechanistic but inferential rather than direct experimental causation. |
| mean predicted protein optimal temperatures across proteins (label-only candidate) | is used to infer | species-level optimal temperature / OGT (label-only candidate) | “species-level optimal temperature was computed as the mean predicted temperature across proteins” (zhu2024accuratelypredictingoptimal pages 8-9) | Zhu et al. 2024, DOI:10.1038/s42003-024-07436-3, https://doi.org/10.1038/s42003-024-07436-3, 2024 | Strong method edge for computational inference; not a biological causal relation in vivo. |
| optimal growth temperature (OGT; label-only candidate) | is defined as | temperature giving maximal growth rate (label-only candidate) | “OGT is defined as the temperature at which an organism achieves its maximal growth rate.” (colette2025machinelearningfor pages 1-4) | Colette et al. 2025, DOI:10.1101/2025.03.03.640802, https://doi.org/10.1101/2025.03.03.640802, 2025 | Strong operational definition; curation-relevant for trait scope rather than mechanism. |
| structural RNA / genome GC content (label-only candidate) | positively correlates with | optimal growth temperature (OGT; label-only candidate) | “positive correlations between Topt and GC content both in bacterial and archaeal structural RNA genes and in bacterial whole genome sequences...” (colette2025machinelearningfor pages 7-12) | Hu et al. 2022, DOI:10.1186/s12864-022-08353-7, https://doi.org/10.1186/s12864-022-08353-7, 2022 | Correlative, not mechanistic; should be marked weak for TraitMech causal curation unless linked to an explicit molecular mechanism. |


*Table: This table lists curation-ready candidate causal edges for the microbial trait temperature optimum mid1 (22–27 °C), emphasizing membrane homeoviscous adaptation, fatty-acid regulation, stress-response proteins, and computational OGT inference. It is useful as a starting artifact for YAML graph curation because each edge includes a quote, reference, and uncertainty note.*

**Visual evidence.** The Ramón et al. 2023 paper includes figures/tables summarizing lipid structures, UFA biosynthesis regulation (FabA/FabB/FabR), and the DesKR membrane-thickness sensing model (ramon2023ageneraloverview media 5b0dc536, ramon2023ageneraloverview media 07cb98ee, ramon2023ageneraloverview media 4206d483, ramon2023ageneraloverview media 48c181b5).

---

## 6) Expert opinions and analysis (authoritative synthesis)
- **Membrane state as a proximate “setpoint” determinant.** Recent reviews converge on the view that maintaining an appropriate membrane physical state across temperatures is a primary determinant of growth performance; temperature shifts drive lipid remodeling toward low-melting components (UFAs, branching, chain length changes, headgroup remodeling) (ramon2023ageneraloverview pages 2-4, maiti2024extrememakeoverthe pages 3-4).
- **Temperature sensing can be direct and biophysical.** The DesKR “buoy” model offers a concrete example of a temperature-responsive system that senses membrane thickness/rigidity rather than extracellular ligands, providing a mechanistic blueprint for how a cell can translate temperature into lipid remodeling gene expression (ramon2023ageneraloverview pages 5-7).
- **Protein stability signatures are increasingly quantifiable.** The 2024 GeoPoc work demonstrates that large-scale protein sequence/structure features can predict temperature optima and identify interpretable physicochemical correlates (e.g., hydrophobic-core features), linking molecular stability principles to organism-level thermal niches via aggregation (zhu2024accuratelypredictingoptimal pages 1-2, zhu2024accuratelypredictingoptimal pages 8-9, zhu2024accuratelypredictingoptimal pages 6-7).

---

## 7) Relevant statistics and quantitative data points (from recent studies)
- **Hopanoid response (quantitative example):** unsaturated hopanoids increased from **27% to 49%** when temperature decreased from **20 °C to 4 °C** in one methanotroph example compiled in a 2023 review (ramon2023ageneraloverview pages 4-5).
- **GeoPoc dataset and performance (2024):** **175,905** non-redundant proteins; optimal temperature prediction **PCC ≈ 0.78**; independent-test improvement over prior state-of-the-art by **2.3% in AUC** (zhu2024accuratelypredictingoptimal pages 1-2).
- **Anammox implementation temperatures (2024 preprint):** common mesophilic operation **30–35 °C**; mainstream full-scale conditions **10–25 °C**; deterioration reported above ~40 °C in rapid shifts; adaptation strategy includes reducing loading rate to ≤~50% of specific activity during temperature increase (christina2024mechanismsofanammox pages 1-5).

---

## 8) DOI-first bibliography (with URLs and publication dates)
1. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology* (Jul 2023). DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 5-7)
2. Maiti A, Erimban S, Daschakraborty S. **Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.** *Chemical Communications* (Aug 2024). DOI: **10.1039/d4cc03114h**. https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 3-4)
3. Karmann C, Navrátilová K, et al. **Mechanisms of anammox adaptation to high temperatures: increased cyclization of ladderane lipids and proteomic insights.** *bioRxiv* (Jul 2024). DOI: **10.1101/2024.07.23.604647**. https://doi.org/10.1101/2024.07.23.604647 (christina2024mechanismsofanammox pages 1-5)
4. Zhu M, Song Y, Yuan Q, Yang Y. **Accurately predicting optimal conditions for microorganism proteins through geometric graph learning and language model.** *Communications Biology* (Dec 2024). DOI: **10.1038/s42003-024-07436-3**. https://doi.org/10.1038/s42003-024-07436-3 (zhu2024accuratelypredictingoptimal pages 1-2, zhu2024accuratelypredictingoptimal pages 8-9, zhu2024accuratelypredictingoptimal pages 6-7)
5. Hu E-Z, Lan X-R, Liu Z-L, Gao J, Niu D-K. **A positive correlation between GC content and growth temperature in prokaryotes.** *BMC Genomics* (Feb 2022). DOI: **10.1186/s12864-022-08353-7**. https://doi.org/10.1186/s12864-022-08353-7 (colette2025machinelearningfor pages 7-12)
6. Colette S, François J, De Moor B, van Noort V. **Machine learning for optimal growth temperature prediction of prokaryotes using amino acid descriptors.** *bioRxiv* (May 2025). DOI: **10.1101/2025.03.03.640802**. https://doi.org/10.1101/2025.03.03.640802 (colette2025machinelearningfor pages 1-4, colette2025machinelearningfor pages 4-7)
7. Grübel K, Suschka J. **Hybrid alkali-hydrodynamic disintegration of waste-activated sludge before two-stage anaerobic digestion process.** *Environmental Science and Pollution Research* (Oct 2015). DOI: **10.1007/s11356-014-3705-y**. https://doi.org/10.1007/s11356-014-3705-y (grubel2015hybridalkalihydrodynamicdisintegration pages 1-2)
8. Abubakar A, Rahim MBHA, Khayat ME. **Activation energy, temperature coefficient and Q10 value estimations of the growth of Rhodotorula sp. strain MBH23 on acrylamide.** *Journal of Environmental Microbiology and Toxicology* (Jul 2024). DOI: **10.54987/jemat.v12i1.998**. https://doi.org/10.54987/jemat.v12i1.998 (abubakar2024activationenergytemperature pages 3-4, abubakar2024activationenergytemperature pages 5-5)

---

## 9) Warnings (claims not ready for TraitMech curation)
1. **Correlation-only edges (e.g., GC content ↔ OGT)** should be treated as *weak* for mechanistic curation unless connected to explicit molecular mechanisms; the Hu et al. 2022 study is explicitly correlational (colette2025machinelearningfor pages 7-12).
2. **Taxon-specific mechanisms** (e.g., DesKR in *B. subtilis*, FabR/fabA/fabB in *E. coli*) are excellent mechanistic templates but should be marked as **context-dependent** rather than universal for all microbes with 22–27 °C optima (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 5-7).
3. **Preprint-only findings** (e.g., some anammox lipid cyclization/proteomic details) should be curated with an **uncertainty flag** until peer-reviewed confirmation (christina2024mechanismsofanammox pages 1-5).
4. The node **temperature optimum mid1 (22–27 °C)** is an organism-level phenotype; many mechanistic statements in reviews are derived from cold adaptation experiments (often 20 °C→4 °C or broader), so mapping to a strict 22–27 °C optimum band may require organism-specific evidence (ramon2023ageneraloverview pages 4-5, ramon2023ageneraloverview pages 2-4).


References

1. (colette2025machinelearningfor pages 1-4): Sophie Colette, Jaldert François, Bart De Moor, and Vera van Noort. Machine learning for optimal growth temperature prediction of prokaryotes using amino acid descriptors. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.03.03.640802, doi:10.1101/2025.03.03.640802. This article has 4 citations.

2. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

3. (flegler2022complementaryadaptationsof pages 13-15): A Flegler. Complementary adaptations of bacterial membranes to low temperatures. Unknown journal, 2022.

4. (colette2025machinelearningfor pages 4-7): Sophie Colette, Jaldert François, Bart De Moor, and Vera van Noort. Machine learning for optimal growth temperature prediction of prokaryotes using amino acid descriptors. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.03.03.640802, doi:10.1101/2025.03.03.640802. This article has 4 citations.

5. (maiti2024extrememakeoverthe pages 3-4): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

7. (ramon2023ageneraloverview pages 4-5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

8. (ramon2023ageneraloverview pages 22-23): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

9. (ramon2023ageneraloverview pages 5-7): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

10. (christina2024mechanismsofanammox pages 1-5): Karmann Christina, Navrátilová Klára, Behner Adam, Noor Tayyaba, Danner Stella, Majchrzak Anastasia, Šantrůček Jiří, Podzimek Tomáš, Marin Lopez Marco A., Hajšlová Jana, Lipovová Petra, Bartáček Jan, and Kouba Vojtěch. Mechanisms of anammox adaptation to high temperatures: increased cyclization of ladderane lipids and proteomic insights. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.23.604647, doi:10.1101/2024.07.23.604647. This article has 1 citations.

11. (zhu2024accuratelypredictingoptimal pages 1-2): Mingming Zhu, Yidong Song, Qianmu Yuan, and Yuedong Yang. Accurately predicting optimal conditions for microorganism proteins through geometric graph learning and language model. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07436-3, doi:10.1038/s42003-024-07436-3. This article has 12 citations and is from a peer-reviewed journal.

12. (zhu2024accuratelypredictingoptimal pages 8-9): Mingming Zhu, Yidong Song, Qianmu Yuan, and Yuedong Yang. Accurately predicting optimal conditions for microorganism proteins through geometric graph learning and language model. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07436-3, doi:10.1038/s42003-024-07436-3. This article has 12 citations and is from a peer-reviewed journal.

13. (zhu2024accuratelypredictingoptimal pages 6-7): Mingming Zhu, Yidong Song, Qianmu Yuan, and Yuedong Yang. Accurately predicting optimal conditions for microorganism proteins through geometric graph learning and language model. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07436-3, doi:10.1038/s42003-024-07436-3. This article has 12 citations and is from a peer-reviewed journal.

14. (grubel2015hybridalkalihydrodynamicdisintegration pages 1-2): Klaudiusz Grübel and Jan Suschka. Hybrid alkali-hydrodynamic disintegration of waste-activated sludge before two-stage anaerobic digestion process. Environmental Science and Pollution Research International, 22:7258-7270, Oct 2015. URL: https://doi.org/10.1007/s11356-014-3705-y, doi:10.1007/s11356-014-3705-y. This article has 71 citations.

15. (abubakar2024activationenergytemperature pages 3-4): Aisami Abubakar, Mohd Badrin Hanizam Abdul Rahim, and Mohd Ezuan Khayat. Activation energy, temperature coefficient and q10 value estimations of the growth of rhodotorula sp. strain mbh23 on acrylamide. Journal of Environmental Microbiology and Toxicology, 12:1-6, Jul 2024. URL: https://doi.org/10.54987/jemat.v12i1.998, doi:10.54987/jemat.v12i1.998. This article has 0 citations.

16. (abubakar2024activationenergytemperature pages 5-5): Aisami Abubakar, Mohd Badrin Hanizam Abdul Rahim, and Mohd Ezuan Khayat. Activation energy, temperature coefficient and q10 value estimations of the growth of rhodotorula sp. strain mbh23 on acrylamide. Journal of Environmental Microbiology and Toxicology, 12:1-6, Jul 2024. URL: https://doi.org/10.54987/jemat.v12i1.998, doi:10.54987/jemat.v12i1.998. This article has 0 citations.

17. (colette2025machinelearningfor pages 7-12): Sophie Colette, Jaldert François, Bart De Moor, and Vera van Noort. Machine learning for optimal growth temperature prediction of prokaryotes using amino acid descriptors. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.03.03.640802, doi:10.1101/2025.03.03.640802. This article has 4 citations.

18. (ramon2023ageneraloverview media 5b0dc536): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

19. (ramon2023ageneraloverview media 07cb98ee): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

20. (ramon2023ageneraloverview media 4206d483): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

21. (ramon2023ageneraloverview media 48c181b5): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.