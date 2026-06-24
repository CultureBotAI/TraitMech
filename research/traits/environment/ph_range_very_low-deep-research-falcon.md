---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:50:06.908220'
end_time: '2026-06-18T01:02:19.172786'
duration_seconds: 732.26
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range very low
  trait_identifier: METPO:1000459
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH range phenotype in which growth extends to external pH at or below
    approximately 4, characteristic of extreme-acidophile physiology.
  parent_traits: METPO:1000332
  synonyms: Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile,
    Obligative acidophile, pHR_0_to_4
  evidence_summary: "DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis\
    \ review supports growth in the pH 1\u20134 range as the extreme-acidophile growth\
    \ range.)"
  causal_graph_summary: 'ph_range_very_low_extreme_acidophile: 3 nodes, 2 edges'
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
- **Trait label:** pH range very low
- **METPO identifier:** METPO:1000459
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which growth extends to external pH at or below approximately 4, characteristic of extreme-acidophile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHR_0_to_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth in the pH 1–4 range as the extreme-acidophile growth range.)
- **Existing causal graph summary:** ph_range_very_low_extreme_acidophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_very_low.yaml`.

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
- **Trait label:** pH range very low
- **METPO identifier:** METPO:1000459
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which growth extends to external pH at or below approximately 4, characteristic of extreme-acidophile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHR_0_to_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth in the pH 1–4 range as the extreme-acidophile growth range.)
- **Existing causal graph summary:** ph_range_very_low_extreme_acidophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_very_low.yaml`.

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


# Research report: Microbial trait “pH range very low” (METPO:1000459)

## 0) Scope summary (what the trait represents)

**Trait definition (curation-ready interpretation).** METPO:1000459 (“pH range very low”) corresponds to a **growth phenotype** in which an organism’s **growth range extends to external pH ≤ ~4**, consistent with **extreme-acidophile physiology** rather than mere survival under transient acid shock. The mechanistic hallmark is the ability to **maintain cytoplasmic pH near neutral (≈6–7)** despite very acidic extracellular conditions, using a combination of **low proton permeability** and **active pH homeostasis** processes. (krulwich2011molecularaspectsof pages 11-12, johnson2016themicrobiologyof pages 3-4)

**Common operational boundaries.**
- A widely used microbiological delineation is that **“extreme acidophiles” grow at pH < 3** and maintain a cytoplasmic pH around ~6.0 (example taxa include *Acidithiobacillus* and *Alicyclobacillus*). (krulwich2011molecularaspectsof pages 11-12)
- A complementary, application-facing classification notes **moderate acidophiles** with growth optima **pH 3–5**, while **extreme acidophiles** have optima at **pH ≤ 3** (with reported organisms capable of growth near pH 0, e.g., *Picrophilus* spp.). (gonzalez2024acidophilicheterotrophsbasic pages 1-2)

**Boundary cases (do not over-curate).**
- **Acid tolerance / acid resistance** in neutrophiles (e.g., *E. coli* survival at pH ~2) uses some overlapping mechanisms (decarboxylases, proton pumps), but may not imply sustained growth at pH ≤4. These should be curated as **contextual/orthologous mechanisms** unless a source ties them to obligate acidophilic growth. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17)
- **Organic-acid stress** differs from mineral-acid stress: protonated weak acids can diffuse across membranes and acidify the cytoplasm, creating a major constraint even for acidophiles. This is an important negative-edge/boundary condition for the trait. (johnson2016themicrobiologyof pages 3-4, lund2020understandinghowmicroorganisms pages 1-2)

## 1) Key concepts and current understanding (mechanistic overview)

### 1.1 Core physiological problem
At external pH ≤4, the **proton gradient** favors proton influx; without defenses, intracellular acidification would disrupt enzymes. Extreme acidophiles therefore couple **(i) reduced proton entry** with **(ii) active removal/consumption of protons** and **(iii) electrical strategies** that oppose proton influx.

### 1.2 Canonical mechanistic themes (high-confidence)

1) **Inside-positive membrane potential (reversed Δψ) + large ΔpH**
- Extreme acidophiles are described as maintaining a large **ΔpH (inside alkaline)** supported by a **reversed membrane potential (inside positive)**, which electrostatically disfavors proton entry. (krulwich2011molecularaspectsof pages 11-12)
- Visual summary: Krulwich et al. schematize the “extreme acidophile” PMF pattern with **inside-positive Δψ** and large ΔpH in **Box 1**. (krulwich2011molecularaspectsof media 6346d681)

2) **Active cation uptake (e.g., K+) to generate inside-positive potential**
- Acidophiles can “generate positive (inside) membrane potentials… via the active influx of cations, such as K+.” (johnson2016themicrobiologyof pages 3-4)

3) **Low passive proton permeability of membranes/envelopes**
- Some acidophilic archaea synthesize **tetraether lipids (GDGT/GDNT)** that have “extremely low proton permeabilities,” supporting low proton leak. (johnson2016themicrobiologyof pages 3-4)

4) **Active proton export / proton handling (ATPases, respiratory coupling)**
- Bacterial acid stress responses include **up-regulated hydrolytic activity of the F1Fo-ATPase** to drive **ATP-dependent H+ extrusion**. (krulwich2011molecularaspectsof pages 5-6)

5) **Metabolic proton consumption and buffering reactions**
- Amino-acid decarboxylase systems (e.g., glutamate decarboxylase **GadB** with its antiporter cycle) consume cytoplasmic protons and are well established in acid resistance. (krulwich2011molecularaspectsof pages 5-6)

### 1.3 2023–2024 mechanistic emphases (what is being highlighted recently)

**Cell-envelope remodeling and protective molecules in low-pH anaerobes.** A 2024 review of **acidophilic sulfate-reducing bacteria (aSRB)** emphasizes multiple routes to maintain homeostasis at pH <5 (and down to ~2.9 in reported isolates): “proton exclusion, exchange, pumping and consumption, and cytoplasmic buffering,” plus **reduced proton permeability** via envelope modifications (hopanoids, specific membrane proteins such as Omp40/PspA, and altered lipid composition such as AEG lipids). Protective polymers and polyamines (poly-γ-glutamate, spermidine) are also reported. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

## 2) Candidate causal-graph nodes (grouped by type; with grounding suggestions)

### 2.1 Trait/phenotype nodes
- **Growth at very low pH** (METPO:1000459; target)
- **Extreme acidophily** (label-only; maps to METPO:1000459 conceptually)
- **Cytoplasmic pH homeostasis / near-neutral intracellular pH** (label-only physiological state; commonly ~pH 6–7) (krulwich2011molecularaspectsof pages 11-12, johnson2016themicrobiologyof pages 3-4)

### 2.2 Environmental & experimental factor nodes
- **Low external pH (≤4)** (ENVO:00001998 “acidic environment” is a candidate, but not confirmed here)
- **Mineral acids / high hydronium activity** (process-level)
- **Weak organic acids (e.g., acetic acid)**: CHEBI:15366 (acetic acid) as a representative inhibitory stressor (johnson2016themicrobiologyof pages 3-4)
- **Acid mine drainage (AMD)**: extremely acidic, metal-rich waters (label-only environment; ENVO grounding not confirmed here) with reported pH <3 and high dissolved metals (johnson2016themicrobiologyof pages 3-4)

### 2.3 Molecular function / process nodes
- **Proton transmembrane transport** (GO:1902600 candidate)
- **Proton extrusion / H+ efflux** (process label-only)
- **Generation of membrane potential** (process label-only)
- **Passive proton permeability of membranes** (biophysical property label-only)

### 2.4 Genes/proteins/complexes (examples)
High-confidence nodes with direct mention in evidence:
- **F1Fo-ATPase / ATP synthase** (GO:0046933) (krulwich2011molecularaspectsof pages 5-6)
- **Glutamate decarboxylase GadB** (EC:4.1.1.15) and associated antiporter cycle (gad system) (krulwich2011molecularaspectsof pages 5-6)
- **Urease (UreA/UreB) and UreI channel** (acid acclimation system in *Helicobacter*) (krulwich2011molecularaspectsof pages 11-12)
- **Envelope stress / membrane proteins (Omp40, PspA)** (label-only proteins; mentioned in aSRB review) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

Transport/ion-homeostasis nodes (partly lineage-specific; best grounded when organism-specific evidence exists):
- **K+ transport / potassium influx** (CHEBI:29103 for K+; transporter label-only; KdpABC is a common candidate) (johnson2016themicrobiologyof pages 3-4)
- **Na+ transport** (CHEBI:29101) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 2.5 Lipids and envelope chemistry
- **Archaeal tetraether lipids (GDGT/GDNT)** (label-only lipid class; used to reduce proton permeability) (johnson2016themicrobiologyof pages 3-4)
- **Hopanoids** (CHEBI:51963) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Acyl/ether glycerol (AEG) lipids** (label-only) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 2.6 Small molecules and protective metabolites
- **Spermidine** (CHEBI:15729) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Poly-γ-glutamate** (label-only polymer) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Hydron/proton** (CHEBI:15378) (krulwich2011molecularaspectsof pages 5-6)

## 3) Evidence-backed candidate causal edges (triples)

The following table is formatted for direct triage into a TraitMech-style causal graph; uncertain edges are flagged.

| Subject (node; suggested CURIE) | Predicate | Object (node; suggested CURIE) | Evidence snippet | Reference (authors, year, DOI, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Potassium influx / K+ transport (CHEBI:29103; candidate transporter node e.g., KdpABC) | causes | Inside-positive membrane potential / reversed Δψ (label-only candidate) | “generate positive (inside) membrane potentials (Δω’s) via the active influx of cations, such as K+” | Johnson & Aguilera, 2016, DOI:10.1128/9781555818821.ch4.3.1, https://doi.org/10.1128/9781555818821.ch4.3.1 (johnson2016themicrobiologyof pages 3-4) | Strong review support for acidophiles broadly; mechanism is general and not restricted to one lineage. |
| Inside-positive membrane potential / reversed Δψ (label-only candidate) | reduces | Proton influx / passive H3O+ entry (CHEBI:15378 for hydron; process label-only) | “maintain a large transmembrane ΔpH… supported by a reversed membrane potential (inside-positive)” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof media 6346d681) | Strong conceptual support; figure/Box 1 explicitly links reversed Δψ to extreme acidophile PMF. |
| Glycerol dialkyl glycerol tetraether lipids / GDGT-GDNT (CHEBI not confidently assigned; label-only candidate) | decreases | Passive proton permeability (label-only candidate) | “These have extremely low proton permeabilities” | Johnson & Aguilera, 2016, DOI:10.1128/9781555818821.ch4.3.1, https://doi.org/10.1128/9781555818821.ch4.3.1 (johnson2016themicrobiologyof pages 3-4) | Strong for some acidophilic archaea, especially Thermoplasmales/thermoacidophiles; taxon-specific. |
| Low passive proton permeability (label-only candidate) | enables maintenance of | Near-neutral cytoplasmic pH (GO:0006885 not appropriate; label-only physiological state) | “As such, a low passive proton permeability and a near neutral intracellular pH can be maintained” | Chong, 2024, DOI:10.3389/frbis.2023.1338019, https://doi.org/10.3389/frbis.2023.1338019 | Strong for archaeal membrane review; most directly applicable to thermoacidophilic archaea. |
| F1Fo-ATPase / ATP synthase (GO:0046933) | exports protons by hydrolysis, increasing | Intracellular pH / cytoplasmic pH homeostasis (label-only candidate) | “up-regulation of the hydrolytic activity of the F1Fo-ATPase to drive ATP-dependent H+ extrusion” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | Strong for bacterial acid stress and acid tolerance; curation into extreme-acidophile graph should be marked broader-than-trait unless direct acidophile evidence is added. |
| Glutamate decarboxylase GadB (EC:4.1.1.15; gene gadB) | consumes | Cytoplasmic protons (CHEBI:15378) | “amino-acid decarboxylases (e.g., glutamate decarboxylase GadB) consume cytoplasmic protons” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | Strong for enteric/neutralophilic acid resistance systems; not specific evidence for obligate extreme acidophiles. |
| GadC glutamate/GABA antiporter (gene gadC; label-only candidate transporter) | coupled with | Glutamate decarboxylase system / continued proton-consuming cycle (label-only candidate) | “GadB is coupled to an antiporter that exports the decarboxylation product (GABA) in exchange for glutamate” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof media 6346d681) | Strong mechanistic support, but mostly acid-resistance literature rather than extreme acidophile growth trait. |
| Glutamate decarboxylase system (gadB/gadC) | contributes to | Acid resistance / survival at low pH (label-only candidate) | “enabling continued decarboxylation-based acid resistance” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | Useful comparator mechanism; likely too generic for direct TraitMech curation without trait-specific evidence. |
| Urease complex (EC:3.5.1.5; ureA/ureB) | causes | Periplasmic buffering (label-only candidate) | “acid acclimation relies on urease-mediated periplasmic buffering” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof media 6346d681) | Strong but specifically Helicobacter acid acclimation; acid tolerance, not extreme acidophily. |
| UreI urea channel (gene ureI; label-only candidate) | enables | Urease-mediated periplasmic buffering (label-only candidate) | “urease (UreA/UreB) is recruited to the inner membrane via UreI… permitting rapid access of incoming urea” | Krulwich et al., 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof media 6346d681) | Strong but taxon-specific to gastric Helicobacter; should be flagged as non-trait-general. |
| Hopanoid lipids (CHEBI:51963) | decrease | Proton permeability of cell envelope (label-only candidate) | “Structural adaptations that reduce proton permeability include hopanoid lipids” | Valdez-Nuñez et al., 2024, DOI:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Review evidence for acidophilic sulfate-reducing bacteria and acidophiles more broadly; moderate strength. |
| Acyl/ether glycerol lipids with saturated ether moieties (label-only candidate) | associated with reduced | Low-pH sensitivity / proton permeability (label-only candidate) | “A. acetoxydans shows increased acyl/ether glycerol (AEG) lipids with saturated ether moieties… linked to low-pH resistance” | Valdez-Nuñez et al., 2024, DOI:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Moderate; somewhat taxon-specific and phrased as linked/associated rather than directly causal. |
| Omp40 / PspA envelope proteins (label-only candidate proteins) | decrease | Proton permeability (label-only candidate) | “Structural adaptations that reduce proton permeability include… specific membrane proteins (Omp40, PspA)” | Valdez-Nuñez et al., 2024, DOI:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Moderate review support; direct mechanistic experiments may be limited and lineage-dependent. |
| Poly-gamma-glutamate polymer (label-only candidate) | contributes to | Acid stress protection (label-only candidate) | “Protective molecules detected include poly-gamma-glutamate polymer” | Valdez-Nuñez et al., 2024, DOI:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Weak-to-moderate; detection/protective role summarized in review, but direct causal evidence likely taxon-specific. |
| Spermidine (CHEBI:15729) | contributes to | Acid stress protection (label-only candidate) | “Protective molecules detected include… spermidine” | Valdez-Nuñez et al., 2024, DOI:10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Weak-to-moderate; likely protective but needs direct experimental support before strong curation. |
| Protonated weak organic acids (e.g., acetic acid, CHEBI:15366) | diffuse into | Cell / cytoplasm (GO:0005737 for cytoplasm) | “lipophilic weak organic acids… can diffuse in and acidify the cytoplasm” | Johnson & Aguilera, 2016, DOI:10.1128/9781555818821.ch4.3.1, https://doi.org/10.1128/9781555818821.ch4.3.1; Lund et al., 2020, DOI:10.3389/fmicb.2020.556140, https://doi.org/10.3389/fmicb.2020.556140 (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, lund2020understandinghowmicroorganisms pages 1-2, johnson2016themicrobiologyof pages 3-4) | Strong general principle; relevant as inhibitory environmental factor rather than positive trait mechanism. |
| Protonated weak organic acids (e.g., acetic acid, CHEBI:15366) | cause | Cytoplasmic acidification (label-only candidate) | “small organic acids can act as uncouplers”; “can diffuse in and acidify the cytoplasm” | Lehtovirta-Morley et al., 2016, DOI:10.1128/AEM.04031-15, https://doi.org/10.1128/AEM.04031-15; Johnson & Aguilera, 2016, DOI:10.1128/9781555818821.ch4.3.1, https://doi.org/10.1128/9781555818821.ch4.3.1 (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, johnson2016themicrobiologyof pages 3-4) | Strong inhibitor edge; especially important boundary condition distinguishing mineral acids from permeant organic acids. |


*Table: This table summarizes evidence-backed candidate causal edges relevant to the microbial trait of growth at very low external pH, including membrane, transport, enzymatic, and inhibitory mechanisms. It is designed to support TraitMech curation while flagging taxon-specific or acid-tolerance-only mechanisms that may not generalize to extreme acidophily.*

### Visual evidence note
Krulwich et al. provide a schematic of the **distinctive proton motive force architecture** of extreme acidophiles (large ΔpH with inside-positive Δψ) in Box 1, which is useful for curating a high-level physiological edge connecting **cation influx → reversed Δψ → reduced proton influx → near-neutral cytoplasmic pH**. (krulwich2011molecularaspectsof media 6346d681)

## 4) Recent developments (2023–2024 prioritized)

### 4.1 Expanding mechanistic emphasis on envelope composition and polymers
The 2024 aSRB review consolidates multiple envelope-centered mechanisms (hopanoids, specific membrane proteins, and lipid remodeling including AEG lipids) together with protective solutes/polymers (poly-γ-glutamate, spermidine) as contributors to low-pH homeostasis in anaerobic acidophiles. This emphasizes that acidophily is frequently a **multistressor adaptation** (pH + metals) and not solely a single transporter or pump. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 4.2 Archaeal membrane biophysics as a mechanistic lever
A 2024 focused review highlights how archaea living at **pH ≤ 4** can maintain near-neutral intracellular pH via compositional tuning of tetraether membranes (e.g., cyclization, glycosylation, tetraether:diether ratios), which is interpreted to support **low passive proton permeability** and robust function under acidic/high-temperature conditions. (Chong 2024 is retrieved but only indirectly quoted in artifact; the explicit “low passive proton permeability… near neutral intracellular pH” wording is represented there.)

### 4.3 Low-pH biotechnology framing
A 2024 review on acidophilic heterotrophs updates the diversity/applications landscape, noting **>80 heterotrophic acidophiles isolated** and highlighting operational advantages of low pH (e.g., reduced contamination) for fermentation and bioprocessing, along with biomining/bioremediation roles. (gonzalez2024acidophilicheterotrophsbasic pages 1-2)

## 5) Current applications and real-world implementations

### 5.1 Acid mine drainage (AMD) treatment and metal recovery
- Acidophilic sulfate-reducing bacteria are discussed as relevant for **AMD treatment (often pH <3)** via biogenic sulfide production and metal precipitation, with quantitative enrichment data reported for passive bioreactor treatment (see statistics below). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- Acidophilic heterotrophs (notably iron reducers) are positioned as enabling biomining/bioremediation operations at low pH, including iron mineral dissolution and removal of impurities. (gonzalez2024acidophilicheterotrophsbasic pages 2-3)

### 5.2 Low-pH fermentation and biopolymer production
Low pH can improve robustness and simplify downstream processing for organic acids; acid stress knowledge is explicitly framed as “central to… successful exploitation.” (lund2020understandinghowmicroorganisms pages 3-5)

Quantitative example (biopolymer production at low pH): In one reported optimization for **P3HB** production, optimal conditions included **pH 3.0** and yielded **19.75 g/L** (with additional extraction/purity metrics reported). (gonzalez2024acidophilicheterotrophsbasic pages 3-4)

## 6) Statistics and recent quantitative data

### 6.1 Environmental/bioreactor pH ranges relevant to low-pH growth
- aSRB review summarizes acidic habitats and microcosms with pH ranges including **pH 2.3–5.4** (waters), pore waters **pH 2.6–3.0**, and microcosms **pH 3.4–4.8**. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 6.2 Reported isolate growth ranges and community shifts (aSRB)
- aSRB isolate growth ranges summarized in Table 1 span minima around **pH ~2.9** (species-specific ranges reported such as 2.9–6.5, 3.6–6.5, 4.0–6.5, etc.). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- During passive bioreactor AMD treatment, Desulfosporosinus-like organisms reportedly increased from **0.0025%–0.0093%** to **27.3%–87.0%** (relative abundance) under acidic conditions (around pH ~3.4–3.7). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

### 6.3 Extremely acidic environment chemistry (context for selection)
Extremely acidic waters can include **pond pH 0.2–2.5** and extremely high dissolved metals (e.g., dissolved iron **2–38 g/L**, and some waters up to **200 g/L dissolved metals**). (johnson2016themicrobiologyof pages 3-4)

## 7) Expert opinions / synthesis from authoritative sources

- A central expert synthesis from a Nature Reviews Microbiology article is that extreme acidophiles **grow at pH < 3** while maintaining cytoplasmic pH around **~6**, requiring integrated control of membrane potential, proton flux, and envelope properties. (krulwich2011molecularaspectsof pages 11-12)
- Johnson & Aguilera emphasize that in extremely acidic systems, acidophiles generally maintain **intracellular pH close to neutral** and can employ **K+ influx** and **low-proton-permeability membranes (tetraether lipids in some archaea)** as key components, but remain vulnerable to **lipophilic weak acids** that bypass the membrane barrier. (johnson2016themicrobiologyof pages 3-4)

## 8) Warnings: claims that may be premature for TraitMech curation

1) **Do not equate acid resistance with extreme-acidophile growth.** Gad decarboxylase systems and many other acid-resistance mechanisms are strongly evidenced in neutrophilic bacteria (e.g., *E. coli*) but are not necessarily the defining mechanisms of obligate acidophiles; curate them as **contextual/putative** unless species-specific evidence links them to growth at pH ≤4. (krulwich2011molecularaspectsof pages 5-6)

2) **Helicobacter urease/UreI is an acid-acclimation niche adaptation**, not a generalizable mechanism for extreme-acidophile physiology; include only if the causal graph is intended to encompass host-associated acid tolerance rather than environmental extreme acidophily. (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof media 6346d681)

3) **Membrane tetraether lipid edges are taxon-specific.** The “extremely low proton permeability” claim is strong for certain archaeal lineages, but should not be generalized to bacteria without supporting sources. (johnson2016themicrobiologyof pages 3-4)

4) **Envelope proteins, polymers, and polyamines** in the aSRB review (Omp40/PspA, poly-γ-glutamate, spermidine) are plausible protective factors but may be **association-level** summaries; curate with **uncertainty flags** unless primary studies demonstrate causality in growth at pH ≤4. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

## 9) DOI-first bibliography (with URLs and publication dates)

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology* (May 2011). DOI: **10.1038/nrmicro2549**. https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 5-6)

2. Valdez‑Nuñez LF, Kappler A, Ayala‑Muñoz D, Chávez IJ, Mansor M. **Acidophilic sulphate‑reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports* (Oct 2024). DOI: **10.1111/1758-2229.70019**. https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

3. González E, Vera F, Scott F, et al. **Acidophilic heterotrophs: basic aspects and technological applications.** *Frontiers in Microbiology* (May 2024). DOI: **10.3389/fmicb.2024.1374800**. https://doi.org/10.3389/fmicb.2024.1374800 (gonzalez2024acidophilicheterotrophsbasic pages 1-2, gonzalez2024acidophilicheterotrophsbasic pages 3-4)

4. Johnson DB, Aguilera A. **The Microbiology of Extremely Acidic Environments.** ASM Press chapter / hosted as ArXiv record (Sep 2016). DOI: **10.1128/9781555818821.ch4.3.1**. https://doi.org/10.1128/9781555818821.ch4.3.1 (johnson2016themicrobiologyof pages 3-4)

5. Lund PA, De Biase D, Liran O, et al. **Understanding How Microorganisms Respond to Acid pH Is Central to Their Control and Successful Exploitation.** *Frontiers in Microbiology* (Sep 2020). DOI: **10.3389/fmicb.2020.556140**. https://doi.org/10.3389/fmicb.2020.556140 (lund2020understandinghowmicroorganisms pages 3-5)

6. Lehtovirta‑Morley LE, Sayavedra‑Soto LA, Gallois N, et al. **Identifying Potential Mechanisms Enabling Acidophily in the Ammonia‑Oxidizing Archaeon “Candidatus Nitrosotalea devanaterra”.** *Applied and Environmental Microbiology* (May 2016). DOI: **10.1128/AEM.04031-15**. https://doi.org/10.1128/AEM.04031-15 (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5, lehtovirtamorley2016identifyingpotentialmechanisms pages 28-33)

## 10) Suggested minimal TraitMech graph skeleton (starting point)

A curation-safe initial graph for METPO:1000459 can be seeded with high-level nodes/edges that are broadly supported across acidophiles:
- **Low external pH (≤4)** → increases proton gradient → **requires pH homeostasis** (krulwich2011molecularaspectsof pages 11-12)
- **K+ influx / cation uptake** → **inside-positive Δψ** → **reduced proton influx** → **near-neutral cytoplasmic pH** → **growth at low pH** (johnson2016themicrobiologyof pages 3-4, krulwich2011molecularaspectsof media 6346d681)
- **Low proton permeability membrane (tetraether lipids in archaea; other envelope adaptations in bacteria)** → reduced passive H+ entry → cytoplasmic pH homeostasis → growth at low pH (johnson2016themicrobiologyof pages 3-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **F1Fo-ATPase (proton extrusion by hydrolysis under acid stress)** → increased intracellular pH → acid survival/growth (flag broader-than-trait unless acidophile-specific) (krulwich2011molecularaspectsof pages 5-6)
- **Weak organic acids** → membrane diffusion → cytoplasmic acidification → inhibits growth at low pH (boundary condition) (johnson2016themicrobiologyof pages 3-4)


References

1. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (johnson2016themicrobiologyof pages 3-4): D. Barrie Johnson and Angeles Aguilera. The microbiology of extremely acidic environments. ArXiv, pages 4.3.1-1-4.3.1-24, Sep 2016. URL: https://doi.org/10.1128/9781555818821.ch4.3.1, doi:10.1128/9781555818821.ch4.3.1. This article has 38 citations.

3. (gonzalez2024acidophilicheterotrophsbasic pages 1-2): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

6. (lund2020understandinghowmicroorganisms pages 1-2): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 359 citations and is from a peer-reviewed journal.

7. (krulwich2011molecularaspectsof media 6346d681): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

8. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

9. (lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5): Laura E. Lehtovirta-Morley, Luis A. Sayavedra-Soto, Nicolas Gallois, Stefan Schouten, Lisa Y. Stein, James I. Prosser, and Graeme W. Nicol. Identifying potential mechanisms enabling acidophily in the ammonia-oxidizing archaeon “candidatus nitrosotalea devanaterra”. Applied and Environmental Microbiology, 82:2608-2619, May 2016. URL: https://doi.org/10.1128/aem.04031-15, doi:10.1128/aem.04031-15. This article has 180 citations and is from a peer-reviewed journal.

10. (gonzalez2024acidophilicheterotrophsbasic pages 2-3): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

11. (lund2020understandinghowmicroorganisms pages 3-5): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 359 citations and is from a peer-reviewed journal.

12. (gonzalez2024acidophilicheterotrophsbasic pages 3-4): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

13. (lehtovirtamorley2016identifyingpotentialmechanisms pages 28-33): Laura E. Lehtovirta-Morley, Luis A. Sayavedra-Soto, Nicolas Gallois, Stefan Schouten, Lisa Y. Stein, James I. Prosser, and Graeme W. Nicol. Identifying potential mechanisms enabling acidophily in the ammonia-oxidizing archaeon “candidatus nitrosotalea devanaterra”. Applied and Environmental Microbiology, 82:2608-2619, May 2016. URL: https://doi.org/10.1128/aem.04031-15, doi:10.1128/aem.04031-15. This article has 180 citations and is from a peer-reviewed journal.