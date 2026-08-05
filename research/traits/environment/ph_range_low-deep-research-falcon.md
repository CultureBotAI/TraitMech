---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:53:08.192544'
end_time: '2026-08-04T03:01:36.402669'
duration_seconds: 508.21
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range low
  trait_identifier: METPO:1000460
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 4\u20136, characteristic of acidophilic physiology."
  parent_traits: METPO:1000332
  synonyms: Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile,
    pHR_4_to_6
  evidence_summary: "DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review\
    \ supports moderately acidic pH-homeostasis as the basis of growth in the pH 4\u2013\
    6 range.)"
  causal_graph_summary: 'ph_range_low_acidophile_range: 13 nodes, 8 edges'
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
- **Trait label:** pH range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000460
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 4–6, characteristic of acidophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile, pHR_4_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4–6 range.)
- **Existing causal graph summary:** ph_range_low_acidophile_range: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **pH range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_low.yaml`.

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
- **Trait label:** pH range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000460
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 4–6, characteristic of acidophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Facultative acidophile, Obligative acidophile, pHR_4_to_6
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4–6 range.)
- **Existing causal graph summary:** ph_range_low_acidophile_range: 13 nodes, 8 edges

## Research Objective

Research the microbial trait **pH range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_low.yaml`.

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


# Curation report: microbial **pH range low**

## Executive curation recommendation

**Trait:** `METPO:1000460`  
**Parent:** `METPO:1000332`  
**Category:** ENVIRONMENT  
**Recommended interpretation:** an **assay-observed capacity for net microbial growth across an external pH interval centered approximately on pH 4–6**. The range should be represented separately from optimum pH, minimum pH, transient survival, acid production, and inducible acid resistance.

The most defensible causal backbone is:

> external pH 4–6 → increased proton challenge → membrane/transport/metabolic pH-homeostasis mechanisms → maintenance of a growth-compatible cytoplasmic pH → growth across pH 4–6 → `METPO:1000460`.

No single gene is sufficient across microbial diversity. The trait is mechanistically convergent: bacteria, archaea, and fungi use partly different combinations of proton exclusion, membrane potential, active transport, proton-consuming reactions, buffering, membrane remodeling, and macromolecular protection.

## 1. Trait scope and boundaries

### 1.1 What the trait represents

The trait records a **growth-supporting external pH range**, not merely exposure or survival. Foundational work emphasizes that pH homeostasis permits growth at external pH values outside the narrower intracellular range compatible with metabolism. Neutralophilic bacteria commonly grow over approximately pH 5.5–9 while maintaining cytoplasmic pH around 7.5–7.7; *Streptococcus mutans* growing near pH 4.8 illustrates an acid-tolerant phenotype relevant to the lower part of this trait. Proton motive force, comprising ΔpH and electrical potential Δψ, links external pH to transport and energy conservation. (krulwich2011molecularaspectsof pages 1-3)

A useful expert classification is based on **pH optimum**, not the full range: extreme acidophiles have optima at or below pH 3, moderate acidophiles have optima around pH 3–5, and acid-tolerant organisms have optima above pH 5 but can grow at lower pH. Thus, `METPO:1000460` can include moderate acidophiles and acid-tolerant organisms, depending on the measured range. (johnson2020acidophilemicrobiologyin pages 1-2)

### 1.2 Boundary cases

1. **Extreme acidophily is adjacent but not synonymous.** Organisms optimized below pH 3 may grow through pH 4, but their defining phenotype is not necessarily a 4–6 range. Extreme acidophiles can maintain cytoplasmic pH near 6 while growing below pH 3. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, krulwich2011molecularaspectsof pages 11-12)
2. **Optimum is not range.** *Phlebiopsis gigantea* had an optimum at pH 4 but sharply reduced growth at pH 2.6 and 5.0, whereas *Mollisia* sp. had a broad optimum of pH 3–5. These are distinct phenotype shapes even though both are “acidophilic.” (ianutsevich2023theroleof pages 1-2)
3. **Survival is not growth.** Viability after an acid challenge, recovery after return to permissive medium, or a short-term acid-resistance assay should not alone establish this trait. (krulwich2011molecularaspectsof pages 1-3)
4. **Acid production is not acid tolerance.** Acidogenic organisms may acidify their environment without continuing to grow throughout pH 4–6.
5. **Organic-acid resistance is not equivalent to mineral-acid resistance.** Undissociated weak acids can cross membranes and dissociate internally; medium composition, acid identity, buffering, temperature, oxygen, and growth phase must therefore accompany pH-range evidence.
6. **Strain specificity matters.** Lactobacilli are reported to tolerate approximately pH 3.7–4.3 and often grow optimally around pH 5.5–6.0, whereas bifidobacteria may fail to survive below pH 4.0. Acid-tolerance responses vary among strains. (sionek2024theimpactof pages 5-6)

## 2. Candidate nodes grouped by type

### Trait and process nodes

- **pH range low:** `METPO:1000460`
- **Parent trait:** `METPO:1000332`
- **pH homeostasis:** `GO:0006885`
- Growth at external pH 4–6 — label-only assay/phenotype node
- Cytoplasmic pH maintenance — label-only process node
- Proton exclusion, proton extrusion, cytoplasmic buffering, acid-stress response — label-only candidate processes
- Reversed/inside-positive membrane potential — label-only biophysical state
- Proton motive force — label-only unless a locally validated ontology term is selected

### Environmental and experimental nodes

- External pH 4–6
- Acidic growth medium
- Organic acid challenge versus strong-acid challenge
- Buffer composition and capacity
- Temperature, oxygen availability, salinity, growth phase, and electron donor/acceptor
- Acid mine drainage, acidic sulfate soil, gastric/periplasmic acid exposure, and acidic food fermentation

These covariates should be retained as evidence metadata because low-pH growth is strongly conditional.

### Chemicals and ions

- Proton: `CHEBI:15378`
- Potassium ion: `CHEBI:29103`
- Sodium ion: `CHEBI:29101`
- L-glutamate: `CHEBI:29985`
- 4-aminobutanoate/GABA: `CHEBI:16865`
- Urea: `CHEBI:16199`
- Ammonia: `CHEBI:16134`
- Arginine, trehalose, polyols, spermidine, carbon dioxide, ammonium, hopanoids, saturated fatty acids, cyclopropane fatty acids, and poly-γ-glutamate — retain as labels until identifiers are verified locally

### Genes, proteins, transporters, and complexes

- `kdpDEABC`/Kdp potassium-uptake system
- Kef-type K⁺ transport system
- `nhaA`; NhaA/NhaB-like Na⁺/H⁺ antiporters
- ClcA-like H⁺/anion antiporter
- Respiratory-chain proton pumps
- F₁F₀ ATPase/ATP synthase
- `gadB` or `gadABC`, glutamate decarboxylase system
- `speA`/`adi`, arginine decarboxylase systems
- `ureABCDEFGHJ`, urease system; UreI urea channel
- `cfa`, cyclopropane-fatty-acyl-phospholipid synthase
- `hpnAIJKNHM` and `shc`, candidate hopanoid/squalene synthesis machinery
- GroEL, GroES, DnaK; ClpXP/related Clp proteases
- Fungal V-ATPase and plasma-membrane Pma1
- Omp40 and PspA, proposed acid-stress membrane proteins in acidophilic sulfate reducers

These symbols should remain **label-only or taxon-qualified** until mapped to an organism-specific UniProt, KEGG Orthology, EC, Rhea, or GO record. The same gene symbol can denote different orthologous scopes across taxa.

### Cellular structures and localizations

- Cytoplasmic membrane/plasma membrane
- Cytoplasm
- Periplasm in diderm bacteria
- Cell surface and cell envelope
- Fungal vacuole for V-ATPase-associated claims

## 3. Candidate causal edges

The following table is intended as the primary curation worksheet. “Promotes” and “reduces” are safer than claiming universal necessity unless the supporting study includes direct perturbation.

| subject | predicate | object | proposed grounding | evidence/source DOI | quote-ready snippet | confidence/caveat |
|---|---|---|---|---|---|---|
| external pH 4–6 | causes | proton stress | ENVO low-pH condition candidate; CHEBI:15378 proton | 10.1038/nrmicro2549 | “maintain more alkaline internal pH at acidic external pH” and pH homeostasis is required when growth occurs at acidic pH (krulwich2011molecularaspectsof pages 1-3) | Medium; foundational review, not specific to one pH-4–6 assay |
| Kdp/Kef potassium uptake systems | promotes | inside-positive membrane potential | CHEBI:29103 potassium ion; kdpDEABC label-only; Kef-type K+ transport label-only | 10.3389/fmicb.2023.1149903; 10.1111/1758-2229.70019 | “candidate genes include kdpDEABC (potassium uptake)” and “aSRB maintain a positive internal membrane potential and accumulate K+ and Na+ to reduce proton influx” (dopson2023eurypsychrophilicacidophilesfrom pages 9-11, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Medium; mixed evidence, partly genomic prediction and partly review synthesis |
| inside-positive membrane potential | reduces | proton influx | membrane potential label-only; CHEBI:15378 proton | 10.1038/nrmicro2549; 10.1111/1758-2229.70019 | acidophiles show “reversed (inside-positive) membrane potential to offset extreme pH gradients” and accumulated cations “reduce proton influx via electrostatic repulsion” (krulwich2011molecularaspectsof pages 1-3, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Medium-high; mechanism well established for acidophiles, not measured specifically for all pH-4–6 taxa |
| NhaA/NhaB/ClcA-like antiporters | promotes | pH homeostasis | CHEBI:29101 sodium ion; nhaA label-only; NhaB-like label-only; ClcA-like antiporter label-only; GO:0006885 pH homeostasis | 10.1103/prxlife.2.043015; 10.3389/fmicb.2023.1149903 | “for acidic external pH (pHe 2-5), ClcA-like antiporters dominate; for neutral pH (5-9), NhaB-like antiporters are optimal” and “nhaA (sodium/proton antiporter)” is a candidate acid-adaptation gene (terradot2024escherichiacolimaintains pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 9-11) | Medium; strong experimental support in E. coli, genomic-prediction support in acidophiles |
| respiratory proton pumps / ATPase activity | promotes | proton extrusion | proton pump label-only; F1Fo ATPase label-only; CHEBI:15378 proton | 10.1038/nrmicro2549; 10.3390/fermentation10060298 | “E. coli up-regulates respiratory chain proton pumps” under acid challenge; LAB use “ATPase-mediated proton extrusion to maintain intracellular pH around 6.0” (krulwich2011molecularaspectsof pages 5-6, sionek2024theimpactof pages 5-6) | Medium-high; broadly supported but taxon-specific implementations differ |
| GadB/GadABC glutamate decarboxylation | causes | proton consumption | gadB/gadABC label-only; CHEBI:29985 L-glutamate; CHEBI:16865 GABA | 10.1038/nrmicro2549; 10.3389/fmicb.2023.1149903 | “Amino acid decarboxylases (particularly GadB) consume cytoplasmic protons” and At. ferrivorans carries “gadABC (glutamate decarboxylase)” (krulwich2011molecularaspectsof pages 5-6, dopson2023eurypsychrophilicacidophilesfrom pages 9-11) | Medium; direct mechanism established in model bacteria, acidophile evidence includes genomic prediction |
| urease/UreI system | causes | ammonia/periplasm buffering | urease label-only; UreI label-only; CHEBI:16199 urea; CHEBI:16134 ammonia | 10.1038/nrmicro2549 | “Urease products (CO2, NH3, NH4+) buffer the periplasm” and UreI recruits urease to the inner membrane for rapid urea access (krulwich2011molecularaspectsof pages 11-12) | Medium-high for Helicobacter; taxon-specific and should be marked uncertain outside urease-positive taxa |
| saturated / cyclopropane / hopanoid lipids | reduces | proton permeability | cyclopropane-fatty-acyl-phospholipid synthase (cfa) label-only; hopanoid synthesis genes hpnAIJKNHM label-only | 10.3389/fmicb.2023.1149903; 10.1111/1758-2229.70019 | “decreased proton permeability through increased saturated fatty acid composition specifically at pH 1.5” and acidophiles use hopanoid and related lipid adaptations for membrane stability (dopson2023eurypsychrophilicacidophilesfrom pages 9-11, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Medium; direct measurement in some taxa, broader lipid classes inferred across acidophiles |
| trehalose / polyols | promotes | acid adaptation in fungi | trehalose label-only; polyols label-only | 10.3390/microorganisms11071733 | “Trehalose and polyols were among the main osmolytes during growth under optimal conditions (pH 4.0)” and broader-range fungus maintained/increased osmolytes across pH shifts (ianutsevich2023theroleof pages 1-2, ianutsevich2023theroleof pages 2-4) | Medium; fungal evidence only, likely not portable to all microbes |
| GroEL/GroES/DnaK or Clp proteases | promotes | macromolecular protection under acid stress | GroEL label-only; GroES label-only; DnaK label-only; ClpXP label-only | 10.3390/fermentation10060298; 10.3389/fmicb.2023.1149903 | LAB acid responses include “stress protein induction (GroEL, GroES, DnaK)” and acidophiles encode “acid resistance proteases (clpXP, clpXPB)” (sionek2024theimpactof pages 5-6, dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Medium; stress-protection role is strong, but direct edge to pH-range phenotype is indirect |
| pH homeostasis | enables | growth at pH 4–6 | GO:0006885 pH homeostasis | 10.1038/nrmicro2549; 10.3390/fermentation10060298; 10.3390/microorganisms11071733 | “cytoplasmic pH homeostasis enable[s] most bacteria to tolerate or grow at external pH values” and LAB maintain intracellular pH ~6.0 while fungal growth range tracks pH-adaptation capacity (krulwich2011molecularaspectsof pages 11-12, sionek2024theimpactof pages 5-6, ianutsevich2023theroleof pages 1-2) | High at process level; exact cutoffs vary by taxon and assay |
| growth-supporting external pH range approximately 4–6 | instance_of | METPO:1000460 | METPO:1000460 | trait definition in prompt; supported conceptually by moderate acidophile / acid-tolerant boundaries in 10.21775/cimb.039.063 and pH-growth examples in 10.1038/nrmicro2549 | moderate acidophiles have “pH optima of 3–5” while acid-tolerant species have “pH optima above 5”; examples include organisms growing around pH 4.8–6.0 (johnson2020acidophilemicrobiologyin pages 1-2, krulwich2011molecularaspectsof pages 1-3, sionek2024theimpactof pages 5-6) | High for ontology mapping; boundary with neighboring traits should remain explicit (range vs optimum vs survival) |


*Table: This table lists 12 compact, evidence-backed candidate causal edges for curating microbial growth at low pH as METPO:1000460. It highlights mechanisms, proposed grounding, supporting snippets, and caveats so curators can separate broadly supported processes from taxon-specific or inference-based claims.*

## 4. Interpretation of the strongest mechanistic modules

### 4.1 Membrane potential and ion transport

Acidophiles can establish an inside-positive electrical potential that opposes proton entry. Acidophilic sulfate-reducing bacteria are reported to accumulate K⁺ and Na⁺, thereby supporting a positive internal potential and electrostatic suppression of proton influx. However, much of the aSRB literature remains comparative or inferential rather than based on clean transporter knockouts. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

A 2024 *E. coli* study provides stronger experimental support that proton-ion antiport and membrane potential are coupled to pH maintenance. Its model and single-cell measurements indicate that collapsing proton motive force depolarizes cells and impairs pH control. The inferred operating domains were approximately pHe 2–5 for ClcA-like transport, pHe 5–9 for NhaB-like transport, and pHe 9–12 for NhaA-like transport. These are model-organism and model-dependent domains, not universal transporter thresholds. (terradot2024escherichiacolimaintains pages 8-9)

### 4.2 Proton extrusion and consumption

Respiratory proton pumps and ATPase-mediated proton export are recurrent mechanisms. Acid-challenged *E. coli* increases respiratory-chain proton-pump expression while reducing ATP-synthase expression; lactic-acid bacteria use ATPase-mediated extrusion to maintain intracellular pH near 6, at an energetic cost. (krulwich2011molecularaspectsof pages 5-6, sionek2024theimpactof pages 5-6)

Glutamate decarboxylation converts glutamate to GABA while consuming a cytoplasmic proton. In model bacteria this directly supports acid resistance; the presence of `gadABC` in *Acidithiobacillus ferrivorans* is mechanistically plausible but remains genomic-prediction evidence unless validated by perturbation. Arginine-dependent systems are analogous candidates. (krulwich2011molecularaspectsof pages 5-6, dopson2023eurypsychrophilicacidophilesfrom pages 9-11)

### 4.3 Urease buffering

In *Helicobacter pylori*, urease activity is central to acid acclimation. Membrane-associated activity approximately doubles at pH 4.5; UreI facilitates rapid urea access, and the resulting NH₃/NH₄⁺ and CO₂ buffer the periplasm while regulatory systems coordinate acid-acclimation genes. This is strong evidence for a **taxon-specific module**, not a universal low-pH-growth mechanism. (krulwich2011molecularaspectsof pages 11-12)

### 4.4 Membrane composition and stress protection

Increased saturated fatty acids can reduce proton permeability; *A. ferrivorans* showed this response at pH 1.5. Candidate acidophile modules also include hopanoid and cyclopropane-lipid synthesis. Because much of the evidence concerns pH below the target range, these edges support general acid adaptation but should not automatically be asserted as necessary for growth specifically at pH 4–6. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 9-11)

Lactic-acid bacteria can lower the unsaturated/saturated fatty-acid ratio and increase cyclic fatty acids, while inducing GroEL, GroES, and DnaK. These responses plausibly reduce membrane proton leakage and protect proteins, but are strain- and condition-dependent. (sionek2024theimpactof pages 5-6)

Fungi provide a distinct implementation. At pH 4, *P. gigantea* and *Mollisia* sp. accumulated trehalose and polyols; V-ATPase and Pma1 were implicated in near-neutral intracellular pH maintenance. *P. gigantea* showed growth decline and lipid/osmolyte changes away from pH 4, whereas *Mollisia* maintained a broader pH 3–5 optimum and more stable membrane composition. The experiment used cultivation periods of 5–14 days and 12–35 days, respectively, emphasizing that assay duration affects range calls. (ianutsevich2023theroleof pages 1-2, ianutsevich2023theroleof pages 2-4)

## 5. Recent applications and implementation data

- **Low-pH organic-acid production:** a 2024 authoritative review reports engineered yeast CB1 producing more than 135 g/L lactic acid at pH 3, with 90% present as free acid; *Rhizopus oryzae* can produce up to 230 g/L but requires pH above 4.5; *Lactobacillus pentosus* achieved 95% yield at pH 3.6. These examples illustrate why low-pH growth/tolerance can reduce neutralization demand and downstream salt waste. (atasoy2024exploitationofmicrobial pages 10-11)
- **Food fermentation and probiotic viability:** selecting strain-specific acid responses is important for fermented-food production and storage. Reported Lactobacillus tolerance at pH 3.7–4.3 and optima around 5.5–6.0 place many strains directly within this trait’s intended scope. (sionek2024theimpactof pages 5-6)
- **Acid-mine-drainage treatment:** a system inoculated with acidic Tinto River sediments achieved more than 99% removal of dissolved metals except Mn, more than 75% sulfate removal, and over 85% iron removal. These are process-level community outcomes and should not be translated directly into single-organism causal edges. (atasoy2024exploitationofmicrobial pages 10-11)
- **Bioleaching and biomining:** *Acidithiobacillus ferrooxidans* generates Fe(III) under oxic conditions, facilitating attack on metal sulfides and mobilization of Li, P, V, Cr, Fe, Ni, Cu, Zn, Ga, As, Mo, W, Pb, and U. The organism generally thrives below pH 2.5, so this is an adjacent extreme-acidophile application rather than direct evidence for a 4–6 range. The same activity can contribute to environmentally harmful acid mine drainage. (tonietti2024unveilingthebioleaching pages 1-2)
- **Acidic sulfate reduction:** acidophilic sulfate reducers can produce sulfide that precipitates metals from acidic drainage. One directly relevant isolate, *Acididesulfobacillus acetoxydans*, grows at pH 3.9–5.0, but the 2024 review stresses that pure-culture mechanistic validation remains limited. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

## 6. Recommended minimal graph for `ph_range_low.yaml`

A conservative cross-taxon graph should prioritize process-level nodes:

1. `external pH 4–6` → **increases** → `inward proton pressure/proton stress`
2. `low proton permeability of cytoplasmic membrane` → **reduces** → `passive proton influx`
3. `cation accumulation/inside-positive membrane potential` → **reduces** → `proton influx`
4. `proton-ion antiport and active proton extrusion` → **promotes** → `cytoplasmic pH homeostasis`
5. `proton-consuming metabolism and chemical buffering` → **promotes** → `cytoplasmic/periplasmic pH homeostasis`
6. `membrane remodeling and macromolecular protection` → **promotes** → `cellular function under acid stress`
7. `cytoplasmic pH homeostasis` → **enables** → `growth at external pH 4–6`
8. `growth at external pH 4–6` → **realizes** → `METPO:1000460`

Gene-level branches should be taxon-qualified and optional—for example, Gad in enteric bacteria, UreI/urease in *Helicobacter*, Kdp/Kef/NhaA candidates in *Acidithiobacillus* and *Ferrovum*, and Pma1/V-ATPase plus osmolytes in fungi.

## 7. Claims not yet safe to curate

- Do **not** encode `kdp`, `nhaA`, `gadABC`, `speA`, `hpn`, or `cfa` as universally necessary or sufficient for `METPO:1000460`; much acidophile evidence is based on gene presence, comparative genomics, or expression. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 9-11)
- Do not generalize *E. coli* antiporter pH domains to all bacteria or archaea. (terradot2024escherichiacolimaintains pages 8-9)
- Do not generalize the *H. pylori* UreI–urease mechanism beyond urease-positive organisms with appropriate localization. (krulwich2011molecularaspectsof pages 11-12)
- Do not use mechanisms measured only near pH 1–3 as direct evidence of growth spanning pH 4–6 without an explicit assay connecting them to that range.
- Do not merge fungal V-ATPase/Pma1 and osmolyte mechanisms into a bacterial graph without taxonomic qualifiers. (ianutsevich2023theroleof pages 1-2, ianutsevich2023theroleof pages 2-4)
- Do not infer phenotype from genome sequence alone. A 2024 model trained on 15,596 bacterial and archaeal genomes obtained only moderate pH prediction performance (reported R² 0.48), reinforcing the need for measured growth curves rather than gene-content inference.
- Do not curate “acidophile,” “acid tolerant,” “facultative acidophile,” and “obligate acidophile” as exact synonyms without preserving the distinction between optimum, range, and requirement.

## DOI-first bibliography

1. **Krulwich TA, Sachs G, Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9, 330–343. Published May 2011. https://doi.org/10.1038/nrmicro2549. Foundational synthesis of pH homeostasis, PMF, antiport, decarboxylation, urease, and acidophile membrane potential. (krulwich2011molecularaspectsof pages 11-12, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3)
2. **Dopson M, González-Rosales C, Holmes DS, Mykytczuk N.** “Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.” *Frontiers in Microbiology* 14. Published March 2023. https://doi.org/10.3389/fmicb.2023.1149903. Recent synthesis of Kdp/Kef, NhaA, decarboxylases, urease, lipids, and stress proteases in acidophilic taxa. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 9-11, dopson2023eurypsychrophilicacidophilesfrom pages 7-8)
3. **Ianutsevich EA et al.** “The Role of Osmolytes and Membrane Lipids in the Adaptation of Acidophilic Fungi.” *Microorganisms* 11, 1733. Published July 2023. https://doi.org/10.3390/microorganisms11071733. Comparative pH-growth, osmolyte, and lipid data for acidophilic fungi. (ianutsevich2023theroleof pages 1-2, ianutsevich2023theroleof pages 2-4)
4. **Terradot G et al.** “Escherichia coli Maintains pH via the Membrane Potential.” *PRX Life* 2, 043015. Published November 2024. https://doi.org/10.1103/prxlife.2.043015. Experimental and modeling analysis of PMF, antiporters, and pH maintenance. (terradot2024escherichiacolimaintains pages 8-9)
5. **Valdez-Nuñez LF et al.** “Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.” *Environmental Microbiology Reports* 16. Published October 2024. https://doi.org/10.1111/1758-2229.70019. Acidophile physiology, pH ranges, membrane adaptations, and AMD applications. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
6. **Atasoy M et al.** “Exploitation of microbial activities at low pH to enhance planetary health.” *FEMS Microbiology Reviews* 48. Published November 2024. https://doi.org/10.1093/femsre/fuad062. Authoritative application review with fermentation and remediation metrics. (atasoy2024exploitationofmicrobial pages 10-11)
7. **Sionek B et al.** “The Impact of Physicochemical Conditions on Lactic Acid Bacteria Survival in Food Products.” *Fermentation* 10, 298. Published June 2024. https://doi.org/10.3390/fermentation10060298. Food-relevant pH ranges and acid-response mechanisms. (sionek2024theimpactof pages 5-6)
8. **Tonietti L et al.** “Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.” *Microorganisms* 12, 2407. Published November 2024. https://doi.org/10.3390/microorganisms12122407. Bioleaching applications and environmental trade-offs. (tonietti2024unveilingthebioleaching pages 1-2)
9. **Johnson DB, Quatrini R.** “Acidophile Microbiology in Space and Time.” *Current Issues in Molecular Biology* 39, 63–76. Published February 2020. https://doi.org/10.21775/cimb.039.063. Authoritative terminology for extreme, moderate, and acid-tolerant phenotypes. (johnson2020acidophilemicrobiologyin pages 1-2)

**Bottom line:** curate `METPO:1000460` primarily through a process-level pH-homeostasis graph. Add gene-specific mechanisms only as taxon-scoped branches with evidence codes distinguishing direct perturbation, physiological observation, transcriptomics, comparative genomics, and review inference.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (johnson2020acidophilemicrobiologyin pages 1-2): D. Barrie Johnson and Raquel Quatrini. Acidophile microbiology in space and time. Current issues in molecular biology, 39:63-76, Feb 2020. URL: https://doi.org/10.21775/cimb.039.063, doi:10.21775/cimb.039.063. This article has 102 citations.

3. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 18 citations and is from a peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 11-12): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (ianutsevich2023theroleof pages 1-2): Elena A. Ianutsevich, Olga A. Danilova, Olga A. Grum-Grzhimaylo, and Vera M. Tereshina. The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi. Microorganisms, 11:1733, Jul 2023. URL: https://doi.org/10.3390/microorganisms11071733, doi:10.3390/microorganisms11071733. This article has 23 citations.

6. (sionek2024theimpactof pages 5-6): Barbara Sionek, Aleksandra Szydłowska, Monika Trząskowska, and Danuta Kołożyn-Krajewska. The impact of physicochemical conditions on lactic acid bacteria survival in food products. Fermentation, 10:298, Jun 2024. URL: https://doi.org/10.3390/fermentation10060298, doi:10.3390/fermentation10060298. This article has 139 citations.

7. (dopson2023eurypsychrophilicacidophilesfrom pages 9-11): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

8. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 10 citations.

9. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (ianutsevich2023theroleof pages 2-4): Elena A. Ianutsevich, Olga A. Danilova, Olga A. Grum-Grzhimaylo, and Vera M. Tereshina. The role of osmolytes and membrane lipids in the adaptation of acidophilic fungi. Microorganisms, 11:1733, Jul 2023. URL: https://doi.org/10.3390/microorganisms11071733, doi:10.3390/microorganisms11071733. This article has 23 citations.

11. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.

12. (atasoy2024exploitationofmicrobial pages 10-11): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 104 citations and is from a domain leading peer-reviewed journal.

13. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 57 citations.

14. (dopson2023eurypsychrophilicacidophilesfrom pages 7-8): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 22 citations and is from a peer-reviewed journal.