---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:59:59.455386'
end_time: '2026-06-17T22:33:28.701682'
duration_seconds: 2009.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultative psychrophilic
  trait_identifier: METPO:1000720
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultative_psychrophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature preference characterized by the ability to grow at low
    temperatures (typically below 20 degrees C) while maintaining optimal growth at
    moderate temperatures.
  parent_traits: METPO:1000613
  synonyms: facultative psychrophile
  evidence_summary: "DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20\
    \ \xB0C and are capable of growth around 0 \xB0C (Supports facultative psychrophiles\
    \ as cold-growing organisms with higher temperature optima.)"
  causal_graph_summary: 'facultative_psychrophilic_cold_tolerance: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative psychrophilic
- **METPO identifier:** METPO:1000720
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference characterized by the ability to grow at low temperatures (typically below 20 degrees C) while maintaining optimal growth at moderate temperatures.
- **Parent traits:** METPO:1000613
- **Synonyms:** facultative psychrophile
- **Existing evidence:** DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20 °C and are capable of growth around 0 °C (Supports facultative psychrophiles as cold-growing organisms with higher temperature optima.)
- **Existing causal graph summary:** facultative_psychrophilic_cold_tolerance: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **facultative psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_psychrophilic.yaml`.

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
- **Trait label:** facultative psychrophilic
- **METPO identifier:** METPO:1000720
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference characterized by the ability to grow at low temperatures (typically below 20 degrees C) while maintaining optimal growth at moderate temperatures.
- **Parent traits:** METPO:1000613
- **Synonyms:** facultative psychrophile
- **Existing evidence:** DOI:10.1111/j.1574-6941.2009.00727.x: optimum temperatures >20 °C and are capable of growth around 0 °C (Supports facultative psychrophiles as cold-growing organisms with higher temperature optima.)
- **Existing causal graph summary:** facultative_psychrophilic_cold_tolerance: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **facultative psychrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_psychrophilic.yaml`.

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


# Research report: Facultative psychrophilic (METPO:1000720) — curation-focused causal graph evidence

## 1) Scope summary (trait meaning, boundaries, and assay context)

**Trait definition (operational):** *Facultative psychrophilic* organisms (often called **psychrotolerant** or **psychrotrophs**) are microbes that **can grow at low temperature (typically 0–4 °C)** yet maintain **optimal growth above ~20 °C** (or at least above the psychrophile range), distinguishing them from obligate psychrophiles whose optima are near 15 °C and which fail to grow at ~20 °C. (ramon2023ageneraloverview pages 1-2)

**Canonical temperature classes used in microbiology (Morita-derived):**
- **Psychrophiles:** optimum growth about **≤15 °C**, maximal growth about **≤20 °C**, minimal growth **≤0 °C**. (moyer2017psychrophilesandpsychrotrophs pages 1-2)
- **Psychrotrophs / psychrotolerant / facultative psychrophiles:** can grow at low temperature but have **optimal and maximal growth temperatures above 15 °C and 20 °C**, respectively. (moyer2017psychrophilesandpsychrotrophs pages 1-2)
- **Mesophiles:** for practical classification, grow **~20–45 °C**. (ramon2023ageneraloverview pages 1-2)

**Boundary cases & distinctions important for curation:**
- The term “facultative psychrophile” historically overlaps with “psychrotroph/psychrotolerant,” with terminology varying by subfield (food/dairy vs environmental microbiology). (moyer2017psychrophilesandpsychrotrophs pages 1-2)
- Evidence suggests a **continuum** of cardinal temperatures; thus, curating this trait should explicitly encode the assay context (growth curve at defined temperatures) and the criterion (e.g., growth at 0–4 °C plus optimum >20 °C). (moyer2017psychrophilesandpsychrotrophs pages 1-2, ramon2023ageneraloverview pages 1-2)
- A useful *phenomenological* distinction: in **Arrhenius plots**, psychrophiles maintain linear growth-rate behavior down to **0 °C**, psychrotolerants deviate/maintain linearity around **5–10 °C**, and mesophiles around **~20 °C**. (purwar2024adaptationsofpsychrophilic pages 8-10)

**Example of temperature-growth measurement:** *Pseudomonas sivasensis* W-6 grew from **4 to 30 °C** (optimum 15 °C), illustrating that some cold-adapted strains may not be facultative psychrophiles by the strict “optimum >20 °C” criterion even if they are cold-tolerant; this is a common boundary issue in practice. (xiong2023wholegenomeanalysis pages 2-3)

## 2) Current understanding: key concepts and mechanistic themes (2023–2024 emphasis)

Cold adaptation relevant to facultative psychrophily is **multifactorial** and typically includes: (i) cold sensing and regulatory rewiring, (ii) membrane remodeling, (iii) protein/RNA homeostasis mechanisms, (iv) cryoprotectants/ice-interacting molecules, and (v) metabolic reprogramming and energy-storage strategies. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)

### 2.1 Cold sensing and regulation
A current synthesis emphasizes that microbes sense cold largely via **changes in membrane physical state**, which can activate **two-component regulatory systems** that transduce the signal. (ramon2023ageneraloverview pages 1-2)

### 2.2 Membrane lipid remodeling (homeoviscous adaptation)
Membranes are repeatedly identified as a primary locus of temperature stress and a key determinant of low-temperature growth. (moyer2017psychrophilesandpsychrotrophs pages 3-5)

Mechanisms supported in the evidence base include:
- Increasing **lipid unsaturation** (double bonds) and related structural changes (chain length, branching/cyclization), with **desaturase activity** described as a rapid early response increasing unsaturated lipids. (moyer2017psychrophilesandpsychrotrophs pages 3-5, ramon2023ageneraloverview pages 1-2)
- In Gram-negative bacteria, cold adaptation may include increasing **short-chain and/or unsaturated fatty acids** in **lipid A** of LPS, supporting membrane fluidity in cold environments. (purwar2024adaptationsofpsychrophilic pages 8-10)

### 2.3 Cold shock proteins, RNA helicases, and chaperones
Low temperature stabilizes RNA secondary structure; **cold shock proteins (CSPs)** act as nucleic-acid chaperones that destabilize such structures, supporting transcription/translation and RNA turnover pathways. (ramon2023ageneraloverview pages 10-12)

Additionally, cold-adapted microbes frequently deploy **protein and nucleic-acid chaperones**, described as upregulated at low temperature (e.g., GroEL/DnaK/GroES; Hsc66 noted as a folding/stabilization factor). (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10)

### 2.4 Cryoprotection: EPS and ice-binding proteins
Evidence supports multiple extracellular and proteinaceous cryoprotective strategies:
- **Exopolysaccharides (EPS)** can protect against freeze–thaw cycles and function as cryoprotectants; EPS is also linked to biofilm formation and survivability. (purwar2024adaptationsofpsychrophilic pages 8-10, yasser2024psychrotrophicbacteriain pages 34-40)
- **Antifreeze/ice-binding proteins (AFPs/IBPs)** bind ice to inhibit growth and recrystallization; **ice-nucleating proteins (INPs)** can nucleate ice at high subzero temperatures (e.g., as high as −2 °C in the cited description). (yasser2024psychrotrophicbacteriain pages 34-40)

### 2.5 Osmoprotection and compatible solutes
In sea-ice/brine contexts, cells can import compatible solutes (e.g., **glycine betaine, choline, proline**) via transporters to counteract freezing-linked osmotic stress, and export ions via mechanosensitive channels during salinity decreases. (yasser2024psychrotrophicbacteriain pages 34-40)

Antarctic-focused synthesis further highlights compatible osmolyte accumulation (e.g., **glycine betaine, trehalose, glycerol, sucrose, mannitol**) as a strategy to reduce freezing point and stabilize membranes/proteins. (ramasamy2023comprehensiveinsightson pages 3-4)

### 2.6 Metabolic reprogramming and energy reserves
A 2024 synthesis summarizes cold-associated metabolic reprogramming (e.g., glycolysis ↑, TCA ↓, electron chain ↓, beta-oxidation ↑; ROS ↑). (purwar2024adaptationsofpsychrophilic pages 8-10)

A 2023 genome study emphasizes that **glycogen and trehalose metabolism** can be central to cold-environment survival, with specific pathways and enzymes described (Glg enzymes; multiple trehalose biosynthesis routes). (xiong2023wholegenomeanalysis pages 1-2, xiong2023wholegenomeanalysis pages 6-9)

## 3) Recent developments and primary-study evidence (prioritizing 2023–2024)

### 3.1 Genomic and pathway evidence in a cold-adapted Pseudomonas (2023)
*Pseudomonas sivasensis* W-6:
- Growth observed **4–30 °C** (optimum 15 °C). (xiong2023wholegenomeanalysis pages 2-3)
- Proposed cold adaptation mechanisms include: using **glycogen and trehalose** as resources; **membrane fluidity** via unsaturated fatty acid profile changes; **two-component systems**; antisense transcription; and involvement of **rpsU** in translation. (xiong2023wholegenomeanalysis pages 1-2)
- The study enumerates key glycogen enzymes (GlgC/GlgA/GlgB/GlgP/GlgX) and trehalose pathways (OtsBA/TreYZ/TreS/TreP/TreT) and notes the treS-pep2-glgE-glgB link between trehalose and glycogen metabolism. (xiong2023wholegenomeanalysis pages 1-2)

**Visual evidence:** Figure 6 provides a schematic of glycogen and trehalose metabolic pathways in W-6 (xiong2023wholegenomeanalysis media 49cca2c2), which can be used directly to curate pathway-level nodes/edges for carbohydrate-mediated cold adaptation.

### 3.2 Gene expression evidence for cold shock proteins in an Antarctic psychrotroph (2024)
*Pseudomonas migulae* CAS19 (Antarctic isolate):
- Reported as psychrotrophic and alkalitolerant, with growth temperatures **15–33 °C**. (otur2024comprehensivecharacterizationand pages 1-3)
- **Cold-related genes cspA_2 and cspD were overexpressed at 4 and 15 °C**, and the study interprets this as consistent with cold adaptation. (otur2024comprehensivecharacterizationand pages 1-3)
- Quantitative statistics provided for antibiotic-exposure induction (not cold-specific): **dfr 63-fold**, **bla 461-fold**, **vanW 31.7-fold**, **macA 24.7-fold** upon antibiotic exposure (useful as a general example of stress-induced transcriptional responses in a cold-region isolate). (otur2024comprehensivecharacterizationand pages 1-3)

### 3.3 Updated reviews (2023–2024) synthesizing mechanistic categories
- **Multifactorial cold adaptation overview** emphasizing membrane-state sensing → two-component activation, membrane double-bond production, cold-adapted proteins, and protective molecules (EPS/compatible solutes/IBPs), plus CSP-mediated regulation and metabolic reprogramming. (ramon2023ageneraloverview pages 1-2)
- **Antarctic adaptation and biotechnological applications** emphasizing compatible osmolytes, ice-binding proteins, and CSP/cspA evidence in Antarctic psychrotrophs; includes claims of constitutive cspA homolog expression at **4 °C and 22 °C** in specific isolates in the cited synthesis. (ramasamy2023comprehensiveinsightson pages 3-4)
- **Physiology-focused cold adaptation review** describing membrane lipid remodeling, EPS cryoprotection, and Arrhenius distinctions among psychrophiles/psychrotolerants/mesophiles, and noting ROS as elevated in cold-adapted metabolic states. (purwar2024adaptationsofpsychrophilic pages 8-10)

## 4) Candidate nodes grouped by type (for `facultative_psychrophilic.yaml`)

| Node label | Node type (environmental factor / process / pathway / gene/protein / metabolite / cellular component) | Brief role in cold growth | Example evidence source (DOI, year) | Suggested ontology grounding (CURIEs where possible) |
|---|---|---|---|---|
| low temperature / cold stress | environmental factor | Primary environmental trigger defining the trait and inducing cold-response systems (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10) | 10.1007/s42770-023-01057-4, 2023 | ENVO:cold environment [label-only]; GO:0009409 |
| cold environment (<5 °C habitats) | environmental factor | Ecological setting where psychrophiles dominate and psychrotolerants persist (moyer2017psychrophilesandpsychrotrophs pages 1-2, ramasamy2023comprehensiveinsightson pages 1-2) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | ENVO:00000446 polar environment [candidate]; ENVO:cold environment [label-only] |
| membrane fluidity | process | Central homeoviscous target that must be maintained for transport, respiration, and growth at low temperature (moyer2017psychrophilesandpsychrotrophs pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 3-5) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | GO:0006869 lipid transport [broad]; GO:0009409 |
| homeophasic adaptation | process | Adjusts membrane viscosity across temperatures to preserve function (moyer2017psychrophilesandpsychrotrophs pages 1-2) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | GO:0009409 |
| fatty acid desaturase | gene/protein | Introduces double bonds into membrane lipids, increasing unsaturation during cold adaptation (moyer2017psychrophilesandpsychrotrophs pages 3-5, purwar2024adaptationsofpsychrophilic pages 8-10) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | GO:0016213 |
| unsaturated fatty acids | metabolite | Increase membrane flexibility at low temperature (moyer2017psychrophilesandpsychrotrophs pages 3-5, purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | CHEBI:35748 |
| polyunsaturated fatty acids (PUFAs) | metabolite | Extreme membrane-fluidizing lipids enriched in some cold-adapted microbes (moyer2017psychrophilesandpsychrotrophs pages 3-5) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | CHEBI:26214 polyunsaturated fatty acid |
| eicosapentaenoic acid (EPA, 20:5) | metabolite | Example PUFA reported in psychrophiles, linked to low-temperature membrane adaptation (moyer2017psychrophilesandpsychrotrophs pages 3-5) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | CHEBI:28364 |
| docosahexaenoic acid (DHA, 22:6) | metabolite | Example PUFA that can increase at 0 °C in some strains (moyer2017psychrophilesandpsychrotrophs pages 3-5) | 10.1016/B978-0-12-809633-8.02282-2, 2017 | CHEBI:28125 |
| branched-chain fatty acids | metabolite | Support membrane remodeling and fluidity in cold-adapted envelopes (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | CHEBI:61912 branched-chain fatty acid |
| lipid A of LPS | cellular component | Outer-membrane lipid moiety remodeled toward short-chain/unsaturated fatty acids in cold (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | CHEBI:16412 lipid A |
| outer membrane / cell envelope | cellular component | Structural barrier that is remodeled to resist freezing, osmotic stress, and membrane rigidification (purwar2024adaptationsofpsychrophilic pages 8-10, ramasamy2023comprehensiveinsightson pages 1-2) | 10.37256/amtt.5220244537, 2024 | GO:0019867; GO:0009274 |
| two-component system | process | Signal transduction module activated by membrane-state changes during cold sensing (ramon2023ageneraloverview pages 1-2, xiong2023wholegenomeanalysis pages 2-3) | 10.1007/s42770-023-01057-4, 2023 | GO:0000160 |
| cold shock protein (CSP) | gene/protein | RNA-binding chaperone family induced or constitutively expressed in cold adaptation (ramon2023ageneraloverview pages 10-12, ramasamy2023comprehensiveinsightson pages 3-4) | 10.1007/s42770-023-01057-4, 2023 | GO:0003723 |
| CspA | gene/protein | Canonical CSP homolog reported in Antarctic psychrotrophs and linked to cold adaptation (ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1197797, 2023 | UniProt:CspA [label-only] |
| CspD | gene/protein | Cold-related gene overexpressed in Antarctic Pseudomonas migulae CAS19 at 4 and 15 °C (otur2024comprehensivecharacterizationand pages 1-3) | 10.1007/s11274-024-04153-1, 2024 | UniProt:CspD [label-only] |
| Hsc66 | gene/protein | Molecular chaperone assisting folding/stabilization under cold stress (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | UniProt:Hsc66 [label-only] |
| GroEL | gene/protein | Chaperonin upregulated during cold shock to support protein folding (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024 | UniProt:GroEL [label-only] |
| DnaK | gene/protein | Hsp70-family chaperone helping prevent misfolding at low temperature (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024 | UniProt:DnaK [label-only] |
| GroES | gene/protein | Co-chaperonin supporting GroEL-mediated folding during cold stress (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024 | UniProt:GroES [label-only] |
| RNA helicase | gene/protein | Remodels stabilized RNA secondary structures that accumulate at low temperature (shaffer2023genomicandphenotypic pages 1-2, ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1156033, 2023 | GO:0003724 |
| mechanosensitive ion channel | gene/protein | Exports ions during salinity shifts associated with freezing/thawing in sea ice and cold brines (yasser2024psychrotrophicbacteriain pages 34-40) | no DOI, 2024 | GO:0006811 [broad]; GO:0015288 [candidate] |
| compatible solute transport | process | Imports osmoprotectants such as betaine/choline/proline to counter freezing-associated osmotic stress (yasser2024psychrotrophicbacteriain pages 34-40) | no DOI, 2024 | GO:0006857 |
| ABC transporter | gene/protein | Broad transport capacity for nutrients and stress-related solutes in cold-adapted strains (xiong2023wholegenomeanalysis pages 2-3) | 10.1038/s41598-023-41323-x, 2023 | GO:0043190 |
| trehalose | metabolite | Major compatible solute and stress protectant in cold adaptation (xiong2023wholegenomeanalysis pages 1-2, ramasamy2023comprehensiveinsightson pages 3-4) | 10.1038/s41598-023-41323-x, 2023 | CHEBI:18154 |
| trehalose metabolism / biosynthesis | pathway | Multiple bacterial trehalose pathways support survival in low-temperature environments (xiong2023wholegenomeanalysis pages 6-9, licciardello2025twoantarcticendophytic pages 1-2) | 10.1038/s41598-023-41323-x, 2023 | GO:0005992 |
| glycogen | metabolite | Energy reserve and cold-survival resource in bacteria adapting to low temperature (xiong2023wholegenomeanalysis pages 1-2) | 10.1038/s41598-023-41323-x, 2023 | CHEBI:28087 |
| glycogen metabolism | pathway | Energy-storage system supporting adaptation and survival during cold stress (xiong2023wholegenomeanalysis pages 1-2, xiong2023wholegenomeanalysis pages 6-9) | 10.1038/s41598-023-41323-x, 2023 | GO:0005978 |
| OtsA/OtsB (TPS/TPP pathway) | gene/protein | Core trehalose biosynthesis enzymes/pathway components discussed for bacterial cold tolerance (xiong2023wholegenomeanalysis pages 1-2, xiong2023wholegenomeanalysis pages 6-9) | 10.1038/s41598-023-41323-x, 2023 | UniProt:OtsA [label-only]; UniProt:OtsB [label-only] |
| TreY/TreZ/TreS/TreP/TreT | gene/protein | Alternative trehalose pathway enzymes supporting cold-associated trehalose production/use (xiong2023wholegenomeanalysis pages 1-2, xiong2023wholegenomeanalysis pages 6-9) | 10.1038/s41598-023-41323-x, 2023 | UniProt:TreY [label-only]; UniProt:TreZ [label-only]; UniProt:TreS [label-only]; UniProt:TreP [label-only]; UniProt:TreT [label-only] |
| glycine betaine | metabolite | Compatible osmolyte imported/accumulated to stabilize cells in freezing conditions (yasser2024psychrotrophicbacteriain pages 34-40, ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1197797, 2023 | CHEBI:17750 |
| choline | metabolite | Imported compatible solute precursor/solute in cold-salinity adaptation models (yasser2024psychrotrophicbacteriain pages 34-40) | no DOI, 2024 | CHEBI:15354 |
| proline | metabolite | Compatible solute associated with osmoprotection in cold-adapted bacteria (yasser2024psychrotrophicbacteriain pages 34-40, licciardello2025twoantarcticendophytic pages 1-2) | 10.1007/s00300-025-03367-9, 2025 | CHEBI:17203 |
| exopolysaccharide (EPS) | metabolite | Cryoprotective matrix component protecting against freeze-thaw cycles and aiding biofilm formation (purwar2024adaptationsofpsychrophilic pages 8-10, yasser2024psychrotrophicbacteriain pages 34-40) | 10.37256/amtt.5220244537, 2024 | GO:0005618 [extracellular space, broad]; CHEBI:16646 polysaccharide |
| biofilm formation | process | Enhances survivability and nutrient access; linked with EPS in cold adaptation (ramasamy2023comprehensiveinsightson pages 3-4, yasser2024psychrotrophicbacteriain pages 34-40) | 10.3389/fmicb.2023.1197797, 2023 | GO:0042710 |
| antifreeze protein (AFP) | gene/protein | Binds ice and inhibits ice growth/recrystallization to prevent freezing damage (yasser2024psychrotrophicbacteriain pages 34-40, ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1197797, 2023 | GO:0050821 [candidate ice binding label-only] |
| ice-binding protein (IBP) | gene/protein | General class of microbial proteins mediating thermal hysteresis and ice-recrystallization inhibition (purwar2024adaptationsofpsychrophilic pages 6-7, ramasamy2023comprehensiveinsightson pages 3-4) | 10.37256/amtt.5220244537, 2024 | GO:0050821 [candidate ice binding label-only] |
| ice nucleating protein (INP) | gene/protein | Promotes controlled ice formation at high sub-zero temperatures (yasser2024psychrotrophicbacteriain pages 34-40, purwar2024adaptationsofpsychrophilic pages 6-7) | no DOI, 2024 | UniProt:ice nucleation protein [label-only] |
| reactive oxygen species (ROS) | metabolite | Cold increases oxidative burden, necessitating detox defenses (purwar2024adaptationsofpsychrophilic pages 8-10, licciardello2025twoantarcticendophytic pages 1-2) | 10.37256/amtt.5220244537, 2024 | CHEBI:26523 |
| superoxide dismutase (SOD) | gene/protein | Antioxidant enzyme reported in Antarctic/cold-adapted systems to mitigate oxidative stress (ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1197797, 2023 | EC:1.15.1.1 |
| glutathione reductase | gene/protein | Antioxidant enzyme supporting redox homeostasis in cold-adapted bacteria (ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1197797, 2023 | EC:1.8.1.7 |
| glutathione | metabolite | Cellular antioxidant substance increased/used in cold and other Antarctic stresses (ramasamy2023comprehensiveinsightson pages 3-4) | 10.3389/fmicb.2023.1197797, 2023 | CHEBI:16856 |
| carotenoids / pigments | metabolite | Stabilize membranes and provide antioxidant, photoprotective, and cryoprotective functions (ramasamy2023comprehensiveinsightson pages 3-4, shaffer2023genomicandphenotypic pages 1-2) | 10.3389/fmicb.2023.1197797, 2023 | CHEBI:23044 carotenoid |
| CAZymes | gene/protein | Carbohydrate-active enzymes linked to glycogen/trehalose use and energy acquisition in cold-adapted Pseudomonas (xiong2023wholegenomeanalysis pages 6-9) | 10.1038/s41598-023-41323-x, 2023 | dbCAN:CAZy [label-only] |
| rpsU | gene/protein | Translation-associated ribosomal protein gene implicated in low-temperature adaptation in W-6 (xiong2023wholegenomeanalysis pages 1-2) | 10.1038/s41598-023-41323-x, 2023 | UniProt:RpsU [label-only] |
| glycolysis | pathway | Reported as upregulated in cold-adapted metabolic reprogramming (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | GO:0006096 |
| tricarboxylic acid (TCA) cycle | pathway | Reported as downregulated in cold-adapted metabolic reprogramming (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | GO:0006099 |
| beta-oxidation of fatty acids | pathway | Reported as increased in cold-adapted metabolism, supporting acetyl-CoA supply (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | GO:0006635 |
| acetyl-CoA metabolism | pathway | Upregulated metabolic hub in cold-adapted organisms (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024 | CHEBI:15351; GO:0006084 [broad] |


*Table: This table lists candidate graph nodes for facultative psychrophily, covering environmental triggers, membrane adaptations, cryoprotectants, transport systems, cold-shock proteins, and metabolic pathways. It is useful as a curation-ready inventory of entities that can be grounded and linked in a TraitMech causal graph.*

## 5) Candidate causal edges (triples) with evidence snippets and grounding

| Edge (subject–predicate–object) | Mechanistic rationale (1 phrase) | Evidence snippet (verbatim or near-verbatim quote) | Source (DOI, year, URL) | Certainty (high/medium/uncertain) | Suggested ontology grounding (CURIEs where available) |
|---|---|---|---|---|---|
| low temperature – induces – two-component system signaling | membrane-based cold sensing | “sensing the cold, mainly through the modification of the liquid-crystalline membrane state, leading to the activation of a two-component system that transduce the signal” (ramon2023ageneraloverview pages 1-2) | Ramón 2023; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | high | GO:0009409; GO:0007165; ENVO:cold environment [label] |
| low temperature – increases – lipid double bonds in membrane lipids | preserves membrane fluidity | “adapting the composition of membranes for proper functions mainly due to the production of double bonds in lipids” (ramon2023ageneraloverview pages 1-2) | Ramón 2023; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | high | GO:0006636; GO:0016213; GO:0009409 |
| fatty acid desaturase activity – increases – unsaturated membrane lipids | rapid homeoviscous response | “the desaturase acting on the acyl chyl chains of the membrane lipids comes into play, thereby increasing the amount of unsaturated lipid” (moyer2017psychrophilesandpsychrotrophs pages 3-5) | Moyer 2017; DOI:10.1016/B978-0-12-809633-8.02282-2; 2017; https://doi.org/10.1016/B978-0-12-809633-8.02282-2 | high | GO:0016213; GO:0006636; CHEBI:35748 unsaturated fatty acid |
| low temperature – upregulates – genes for fatty acid desaturation and branched-chain fatty-acid production | membrane remodeling for cold | “Genes involved in membrane biogenesis, fatty acid synthesis, fatty acid desaturation, and production of branched-chain fatty acids are upregulated” (purwar2024adaptationsofpsychrophilic pages 8-10) | Purwar 2024; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | high | GO:0016213; GO:0006633; GO:0006636; GO:0009409 |
| unsaturated/short-chain lipid A fatty acids – improve – membrane fluidity in cold environments | outer membrane adaptation | “The lipid A component of LPS... often comprises higher proportions of short-chain and/or unsaturated fatty acids, which contribute to improved membrane fluidity in cold environments” (purwar2024adaptationsofpsychrophilic pages 8-10) | Purwar 2024; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | high | CHEBI:35748; GO:0005886; GO:0009409 |
| extracellular polymeric substances (EPS) – protect against – freeze-thaw cycles | cryoprotective matrix | “exopolysaccharides (EPS) surrounding bacterial cells also play a critical role in cold adaptation by providing protection against freeze-thaw cycles and acting as cryoprotectants” (purwar2024adaptationsofpsychrophilic pages 8-10) | Purwar 2024; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | high | GO:0009273; GO:0005975; GO:0009409 |
| antifreeze proteins / ice-binding proteins – inhibit – ice growth and recrystallization | prevents ice damage | “Antifreeze proteins (AFPs)... can bind to ice and inhibit ice growth and recrystallisation” (yasser2024psychrotrophicbacteriain pages 34-40) | Yasser 2024; no DOI; 2024; URL not available | high | GO:0009273 [ice binding label-only if needed]; GO:0009409 |
| compatible solute transport proteins – import – glycine betaine/choline/proline during increased salinity at low temperature | osmoprotection in cold brine | “cells use transport proteins... to import compatible solutes (e.g., betaine, choline, proline)” (yasser2024psychrotrophicbacteriain pages 34-40) | Yasser 2024; no DOI; 2024; URL not available | high | CHEBI:17750 glycine betaine; CHEBI:26271 choline; CHEBI:17203 proline; GO:1901653 response to salt stress; GO:0009409 |
| compatible solute accumulation – restores – osmotic balance and counters freezing injury | protects cytoplasm | “Accumulation of these organic osmolytes contributes to restoring osmotic balance... depress the freezing point of solution” (yasser2024psychrotrophicbacteriain pages 34-40) | Yasser 2024; no DOI; 2024; URL not available | high | CHEBI:17750; CHEBI:17203; CHEBI:18154 trehalose; GO:0006970 response to osmotic stress; GO:0009409 |
| trehalose – protects – bacteria against abiotic stress including low temperature | compatible solute/cryoprotectant | “Trehalose... plays an important role in protecting bacteria against a range of stresses” (xiong2023wholegenomeanalysis pages 1-2) | Xiong 2023; DOI:10.1038/s41598-023-41323-x; 2023; https://doi.org/10.1038/s41598-023-41323-x | high | CHEBI:18154 trehalose; GO:0005992 trehalose biosynthetic process; GO:0009409 |
| low temperature adaptation – involves – glycogen synthesis/metabolism | energy storage for survival | “under different abiotic stresses, such as low temperature... glycogen synthesis is one of the well-developed energy storage systems for bacteria to adapt and survive” (xiong2023wholegenomeanalysis pages 1-2) | Xiong 2023; DOI:10.1038/s41598-023-41323-x; 2023; https://doi.org/10.1038/s41598-023-41323-x | high | GO:0005978 glycogen biosynthetic process; CHEBI:glycogen [label]; GO:0009409 |
| trehalose and glycogen metabolic pathways – contribute to – survival in cold environments | linked reserve/protectant system | “Five trehalose metabolic pathways... facilitating survival in cold environments” and “Trehalose and glycogen were highly accumulated... under cold conditions” (xiong2023wholegenomeanalysis pages 6-9) | Xiong 2023; DOI:10.1038/s41598-023-41323-x; 2023; https://doi.org/10.1038/s41598-023-41323-x | high | GO:0005992; GO:0005978; CHEBI:18154; GO:0009409 |
| rpsU ribosomal genes – contribute to – low-temperature adaptation in translation | translation support in cold | “the cold-adapted mechanisms of the W-6 included... the role played by rpsU genes in the translation process” (xiong2023wholegenomeanalysis pages 1-2) | Xiong 2023; DOI:10.1038/s41598-023-41323-x; 2023; https://doi.org/10.1038/s41598-023-41323-x | medium | GO:0006412 translation; UniProt:rpsU [label-only]; GO:0009409 |
| cspA_2 / cspD overexpression – associated with – cold adaptation | cold-shock RNA chaperones | “Cold-related genes cspA_2 and cspD were overexpressed at 4 and 15 °C, consistent with the cold adaptation mechanism” (otur2024comprehensivecharacterizationand pages 1-3) | Otur 2024; DOI:10.1007/s11274-024-04153-1; 2024; https://doi.org/10.1007/s11274-024-04153-1 | high | GO:0009409; UniProt:CspA [label-only]; UniProt:CspD [label-only] |
| cold shock proteins (CSPs) – destabilize – RNA secondary structures | maintains transcription/translation | “CSPs function as chaperones that destabilize those secondary structures and maintain a single-stranded molecule” (ramon2023ageneraloverview pages 10-12) | Ramón 2023; DOI:10.1007/s42770-023-01057-4; 2023; https://doi.org/10.1007/s42770-023-01057-4 | high | GO:0003723 RNA binding; GO:0006457 protein folding [broad]; GO:0009409 |
| RNA helicases – are associated with – cold and salt tolerance | nucleic-acid remodeling | “The genome contains several genes associated with cold and salt tolerance, including multiple RNA helicases, protein chaperones, and cation/proton antiporters” (shaffer2023genomicandphenotypic pages 1-2) | Shaffer/Massilia 2023 evidence was retrieved but not requested source list; therefore do not curate from this source | uncertain | GO:0003724 RNA helicase activity; GO:0009409 |
| reactive oxygen species detoxification systems – contribute to – cold tolerance | mitigates cold-associated oxidative stress | “genomes encompassed genes possibly associated with bacterial cold tolerance... reactive oxygen species detoxification” (licciardello2025twoantarcticendophytic pages 1-2) | Licciardello 2025 evidence was retrieved but not requested source list; therefore do not curate from this source | uncertain | GO:0000302 response to reactive oxygen species; GO:0009409 |
| low temperature – increases – reactive oxygen species (ROS) burden | oxidative stress consequence of cold | “increased gas solubility, including oxygen molecules and reactive oxygen species (ROS)... These factors negatively impact solute transport and diffusion” and Table 3 lists “Reactive oxygen species (ROS) ↑” (purwar2024adaptationsofpsychrophilic pages 8-10) | Purwar 2024; DOI:10.37256/amtt.5220244537; 2024; https://doi.org/10.37256/amtt.5220244537 | medium | CHEBI:26523 reactive oxygen species; GO:0000302; GO:0009409 |
| Antarctic bacteria – accumulate – glycine betaine/trehalose/glycerol/sucrose/mannitol | compatible osmolyte strategy | “Accumulation of compatible osmolytes (glycine betaine, trehalose, glycerol, sucrose, mannitol etc.) is the other way of Antarctic bacteria to prevent cell shrinkage and water loss during sub-zero temperature” (ramasamy2023comprehensiveinsightson pages 3-4) | Ramasamy 2023; DOI:10.3389/fmicb.2023.1197797; 2023; https://doi.org/10.3389/fmicb.2023.1197797 | high | CHEBI:17750; CHEBI:18154; CHEBI:17522 glycerol; CHEBI:17992 sucrose; CHEBI:29864 mannitol; GO:0009409 |


*Table: This table lists evidence-backed candidate causal edges for a TraitMech graph of facultative psychrophily/cold tolerance. It emphasizes membrane remodeling, osmolytes, cold-shock systems, cryoprotectants, and glycogen/trehalose metabolism, with ontology grounding suggestions for curation.*

## 6) Current applications and real-world implementations

### 6.1 Food cold chain and dairy spoilage
Psychrotrophic bacteria are a well-recognized problem in refrigerated foods, including milk, because they remain active at low temperature. The 2024 dairy-focused review emphasizes cold adaptation strategies (compatible solute import; EPS; ice-binding proteins; cold-active enzymes) that are directly relevant to psychrotrophic persistence in refrigerated environments. (yasser2024psychrotrophicbacteriain pages 34-40)

### 6.2 Bioremediation and environmental biotechnology
Antarctic/cold-adapted microbes are repeatedly framed as sources of **cold-adapted enzymes and molecules** with “many more industrial applications than mesophilic ones,” including for industrial processes and bioremediation strategies in cold conditions. (ramasamy2023comprehensiveinsightson pages 1-2, ramon2023ageneraloverview pages 1-2)

A concrete example is the Antarctic *Pseudomonas migulae* CAS19 isolate, which is reported to have **diesel fuel (5%) degradation capacity**, illustrating real-world applicability of cold-region strains for pollutant transformation. (otur2024comprehensivecharacterizationand pages 1-3)

## 7) Relevant statistics and quantitative data points (from cited evidence)

- Earth cold environment prevalence: by volume, **>90% of the ocean is 5 °C or colder** (contextualizing why psychrotolerance/facultative cold growth is ecologically common). (moyer2017psychrophilesandpsychrotrophs pages 1-2)
- *Pseudomonas sivasensis* W-6 growth temperature range: **4–30 °C**; optimum **15 °C** (important as a comparison/boundary case vs facultative psychrophily criterion “optimum >20 °C”). (xiong2023wholegenomeanalysis pages 2-3)
- *Pseudomonas migulae* CAS19 antibiotic-stress RT-qPCR induction (example stress quantification): **dfr 63-fold**, **bla 461-fold**, **vanW 31.7-fold**, **macA 24.7-fold** upon antibiotic exposure. (otur2024comprehensivecharacterizationand pages 1-3)
- Mechanistic statistic example from membrane adaptation literature: in Moritella ANT-300 starvation, palmitoleate (16:1) increased from **46% to 62.5%**, while myristate (14:0) decreased from **26% to 13%** (illustrative of lipid remodeling magnitudes; though not specific to facultative psychrophiles, it supports membrane-fluidity mechanisms in cold-adapted lineages). (moyer2017psychrophilesandpsychrotrophs pages 3-5)

## 8) Expert opinions/authoritative analysis (from reviews)

- A 2023 synthesis frames cold adaptation as beginning with **membrane physical-state sensing** that activates a **two-component system**, followed by membrane composition changes (double bonds; hopanoids; pigments), protein adaptation for catalytic efficiency, and protective EPS/compatible solutes/IBPs; it also highlights CSP action on mRNAs and global metabolic reprogramming. (ramon2023ageneraloverview pages 1-2)
- A 2017 authoritative reference module emphasizes that **membranes may be the primary site of thermal damage** in psychrophiles compared with enzymes, which helps justify prioritizing membrane-focused nodes/edges in TraitMech curation. (moyer2017psychrophilesandpsychrotrophs pages 3-5)

## 9) Ontology grounding notes (curation guidance)

- **Trait term:** METPO:1000720 (provided).
- **Cold response:** GO:0009409 (response to cold) is a common anchoring GO term for edges triggered by cold.
- **Membrane lipid remodeling:** use GO:0016213 (fatty acid desaturase activity) where desaturase is specified; consider CHEBI unsaturated fatty acid classes where lipid products are nodes.
- **Compatible solutes:** CHEBI identifiers are available for trehalose, glycine betaine, choline, proline (listed in artifact-01).
- **Ice-binding proteins / antifreeze proteins:** may require label-only nodes unless a stable GO/MF term is selected in your ontology stack.

## 10) Warnings / claims not yet ready for TraitMech curation

1. **Trait boundary mismatch in available primary study:** *Pseudomonas sivasensis* W-6 is cold-adapted but has optimum **15 °C**, so it does not satisfy the strict facultative psychrophile criterion “optimal growth at moderate temperatures (>20 °C)” in your template definition; it is best used to curate *cold tolerance mechanisms* rather than the trait label itself unless the curation model allows broader cold-growth phenotypes. (xiong2023wholegenomeanalysis pages 2-3, xiong2023wholegenomeanalysis pages 1-2)
2. **Non-peer-reviewed/uncertain bibliographic metadata:** The “Psychrotrophic bacteria in milk” 2024 source provides useful mechanistic descriptions but lacks clear journal/DOI metadata in the retrieved text; its mechanistic edges should be flagged as **medium/high uncertainty** until a citable DOI source corroborates specific statements. (yasser2024psychrotrophicbacteriain pages 34-40)
3. **General mechanisms vs facultative specificity:** Several cited mechanistic themes (e.g., membrane unsaturation; AFP/IBP; osmolytes) are broadly “cold-adaptation” mechanisms and may not discriminate obligate psychrophiles from facultative psychrophiles on their own. Curating them as edges into a *cold growth/cold tolerance* subgraph is appropriate, but the mapping to “facultative psychrophilic” should be explicitly stated as inferred unless the source studied a strain meeting the facultative definition. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10, moyer2017psychrophilesandpsychrotrophs pages 3-5)

---

## DOI-first bibliography (with dates and URLs where available)

1. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro‑Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology.* Published online **2023-07-21**. DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 10-12)
2. Ramasamy KP, Mahawar L, Rajasabapathy R, et al. **Comprehensive insights on environmental adaptation strategies in Antarctic bacteria and biotechnological applications of cold adapted molecules.** *Frontiers in Microbiology.* Published **2023-06-16**. DOI: **10.3389/fmicb.2023.1197797**. https://doi.org/10.3389/fmicb.2023.1197797 (ramasamy2023comprehensiveinsightson pages 1-2, ramasamy2023comprehensiveinsightson pages 3-4)
3. Xiong L, Li Y, Yu H, et al. **Whole genome analysis and cold adaptation strategies of Pseudomonas sivasensis W‑6 isolated from the Napahai plateau wetland.** *Scientific Reports.* Accepted **2023-08-24** (Received 2023-01-02). DOI: **10.1038/s41598-023-41323-x**. https://doi.org/10.1038/s41598-023-41323-x (xiong2023wholegenomeanalysis pages 1-2, xiong2023wholegenomeanalysis pages 2-3, xiong2023wholegenomeanalysis pages 6-9, xiong2023wholegenomeanalysis media 49cca2c2)
4. Otur Ç, Okay S, Konuksever Ö, et al. **Comprehensive characterization and resistome analysis of Antarctic Pseudomonas migulae strain CAS19.** *World Journal of Microbiology and Biotechnology.* **2024** (received 2024-03-01; accepted 2024-09-30). DOI: **10.1007/s11274-024-04153-1**. https://doi.org/10.1007/s11274-024-04153-1 (otur2024comprehensivecharacterizationand pages 1-3)
5. Purwar S, Srivastava S. **Adaptations of psychrophilic microorganism to low-temperature environments.** *Applied Microbiology: Theory & Technology.* **2024-10**. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7)
6. Moyer CL, Collins RE, Morita RY. **Psychrophiles and Psychrotrophs.** *Reference Module in Life Sciences (Elsevier).* **2017-01**. DOI: **10.1016/B978-0-12-809633-8.02282-2**. https://doi.org/10.1016/B978-0-12-809633-8.02282-2 (moyer2017psychrophilesandpsychrotrophs pages 1-2, moyer2017psychrophilesandpsychrotrophs pages 3-5)

Non-DOI source used cautiously:
- Yasser B. **Psychrotrophic bacteria in milk and their negative effects on dairy products quality: A review.** 2024. (DOI/journal metadata not available in retrieved text.) (yasser2024psychrotrophicbacteriain pages 34-40)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (moyer2017psychrophilesandpsychrotrophs pages 1-2): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

3. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

4. (xiong2023wholegenomeanalysis pages 2-3): Lingling Xiong, Yanmei Li, Hang Yu, Yunlin Wei, Haiyan Li, and Xiuling Ji. Whole genome analysis and cold adaptation strategies of pseudomonas sivasensis w-6 isolated from the napahai plateau wetland. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41323-x, doi:10.1038/s41598-023-41323-x. This article has 12 citations and is from a peer-reviewed journal.

5. (moyer2017psychrophilesandpsychrotrophs pages 3-5): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 185 citations.

6. (ramon2023ageneraloverview pages 10-12): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

7. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

8. (yasser2024psychrotrophicbacteriain pages 34-40): B Yasser. Psychrotrophic bacteria in milk and their negative effects on dairy products quality: a review. Unknown journal, 2024.

9. (ramasamy2023comprehensiveinsightson pages 3-4): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 69 citations and is from a peer-reviewed journal.

10. (xiong2023wholegenomeanalysis pages 1-2): Lingling Xiong, Yanmei Li, Hang Yu, Yunlin Wei, Haiyan Li, and Xiuling Ji. Whole genome analysis and cold adaptation strategies of pseudomonas sivasensis w-6 isolated from the napahai plateau wetland. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41323-x, doi:10.1038/s41598-023-41323-x. This article has 12 citations and is from a peer-reviewed journal.

11. (xiong2023wholegenomeanalysis pages 6-9): Lingling Xiong, Yanmei Li, Hang Yu, Yunlin Wei, Haiyan Li, and Xiuling Ji. Whole genome analysis and cold adaptation strategies of pseudomonas sivasensis w-6 isolated from the napahai plateau wetland. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41323-x, doi:10.1038/s41598-023-41323-x. This article has 12 citations and is from a peer-reviewed journal.

12. (xiong2023wholegenomeanalysis media 49cca2c2): Lingling Xiong, Yanmei Li, Hang Yu, Yunlin Wei, Haiyan Li, and Xiuling Ji. Whole genome analysis and cold adaptation strategies of pseudomonas sivasensis w-6 isolated from the napahai plateau wetland. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-41323-x, doi:10.1038/s41598-023-41323-x. This article has 12 citations and is from a peer-reviewed journal.

13. (otur2024comprehensivecharacterizationand pages 1-3): Çiğdem Otur, Sezer Okay, Ömer Konuksever, Oğuzhan Duyar, Yılmaz Kaya, and Aslıhan Kurt-Kızıldoğan. Comprehensive characterization and resistome analysis of antarctic pseudomonas migulae strain cas19. World journal of microbiology & biotechnology, 40 11:347, Oct 2024. URL: https://doi.org/10.1007/s11274-024-04153-1, doi:10.1007/s11274-024-04153-1. This article has 2 citations and is from a peer-reviewed journal.

14. (ramasamy2023comprehensiveinsightson pages 1-2): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 69 citations and is from a peer-reviewed journal.

15. (shaffer2023genomicandphenotypic pages 1-2): Jacob M. C. Shaffer, Lesley-Ann Giddings, Robert M. Samples, and Jill A. Mikucki. Genomic and phenotypic characterization of a red-pigmented strain of massilia frigida isolated from an antarctic microbial mat. Frontiers in Microbiology, May 2023. URL: https://doi.org/10.3389/fmicb.2023.1156033, doi:10.3389/fmicb.2023.1156033. This article has 16 citations and is from a peer-reviewed journal.

16. (licciardello2025twoantarcticendophytic pages 1-2): Giorgio Licciardello, Livio Antonielli, Carmela Sicher, Ilaria Larini, and Michele Perazzolli. Two antarctic endophytic bacteria of colobanthus quitensis show functional and genomic characteristics potentially responsible for plant growth promotion and cold tolerance. Polar Biology, Feb 2025. URL: https://doi.org/10.1007/s00300-025-03367-9, doi:10.1007/s00300-025-03367-9. This article has 6 citations and is from a peer-reviewed journal.