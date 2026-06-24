---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:37:49.289689'
end_time: '2026-06-17T23:50:18.761179'
duration_seconds: 749.47
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately acidophilic
  trait_identifier: METPO:1003006
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_acidophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH growth preference characterized by the requirement for acidic environments
    (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
  parent_traits: METPO:1003000
  synonyms: obligate acidophile
  evidence_summary: 'DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports
    acidophilic growth as a phenotype defined by acidic optimal pH.)'
  causal_graph_summary: 'obligately_acidophilic_ph_homeostasis: 7 nodes, 6 edges'
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
- **Trait label:** obligately acidophilic
- **METPO identifier:** METPO:1003006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the requirement for acidic environments (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate acidophile
- **Existing evidence:** DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports acidophilic growth as a phenotype defined by acidic optimal pH.)
- **Existing causal graph summary:** obligately_acidophilic_ph_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_acidophilic.yaml`.

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
- **Trait label:** obligately acidophilic
- **METPO identifier:** METPO:1003006
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by the requirement for acidic environments (pH below 5.5) for growth, with inability to grow at neutral or alkaline pH values.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate acidophile
- **Existing evidence:** DOI:10.3389/fmicb.2021.822229: acidic optimal growth pH (Supports acidophilic growth as a phenotype defined by acidic optimal pH.)
- **Existing causal graph summary:** obligately_acidophilic_ph_homeostasis: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **obligately acidophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_acidophilic.yaml`.

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


## Research report: obligately acidophilic (METPO:1003006)

### 0) Scope summary (curation intent)
The trait **obligately acidophilic** (METPO:1003006) denotes microorganisms that *require* acidic conditions for growth (definition given by user: growth below pH 5.5 with inability to grow at neutral/alkaline pH). Mechanistically, obligate acidophiles must (i) prevent lethal proton influx and maintain a cytoplasmic pH compatible with enzyme function, while (ii) operating in ecosystems and/or engineered processes where acidity is sustained (often by microbial Fe/S cycling). Recent reviews synthesize a common mechanistic picture centered on **pH homeostasis via reversed membrane potential, active proton export, reduced membrane proton permeability, and cytoplasmic proton-consuming reactions**, plus community-level strategies like **biofilm microenvironments**. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, tonietti2024unveilingthebioleaching pages 2-4)

**Boundary cases / nearby traits:**
- Many sources classify **moderate** vs **extreme** acidophiles by optimum pH (moderate optima ~pH 3–5; extreme optima ≤pH 3). (gonzalez2024acidophilicheterotrophsbasic pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 1-2)
- **Obligate** acidophily is stricter than “acid-tolerant/aciduric” (able to survive or grow across a broad pH range). The strongest direct “no growth at higher pH” evidence in this tool run is a **truncated** statement from an acidophilic fungi study indicating fungi classified as obligate acidophiles had a growth optimum at pH 4.0 and “no growth at pH …” (missing the exact endpoint in the extracted snippet). Because this quotation is incomplete, it should be treated as **supportive but not yet curatable** for an explicit numeric “no growth at pH ≥X” boundary until the underlying figure/table text is re-checked. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)

### 1) Key concepts and definitions (current understanding)
**Acidophiles and pH categories (operational definitions in recent reviews):**
- A 2024 review on acidophilic heterotrophs summarizes that **moderate acidophiles** have growth optima from **pH 3 to 5**, while **extreme acidophiles** have optima at **pH 3 or below**; some organisms can proliferate near **pH ~0** (example given: *Picrophilus oshimae*). (gonzalez2024acidophilicheterotrophsbasic pages 1-2)
- A 2023 review provides similar quantitative framing: acidophiles with growth optima <5; **extreme acidophiles** have optima <3; and **moderate acidophiles** can have broader growth ranges (e.g., pH 3–7.5) with optima ~pH 4–5. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 2-4)

**Physiological definition of the trait in practice:**
- For TraitMech curation, “obligately acidophilic” should be interpreted as a **growth phenotype** measurable by growth rate/biomass formation across a pH series, where growth is observed only in the acidic range and absent at neutral/alkaline pH (assay-defined). The mechanistic literature emphasizes that acidophiles may keep **intracellular pH near circumneutral** despite external pH <3, implying the trait is not “acidic cytoplasm” but rather specialized homeostasis. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, gonzalez2024acidophilicheterotrophsbasic pages 1-2)

### 2) Candidate causal-graph entities (nodes) with ontology grounding
Below are candidate node sets suitable for a TraitMech causal graph. Grounding is provided where stable identifiers are clear; otherwise, label-only nodes are recommended.

#### A) Environmental & experimental factors
- **Low external pH / acidic environment** (ENVO label-only; e.g., “acidic environment”) (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 1-2)
- **Acid mine drainage (AMD)** (ENVO label-only; AMD contexts and acid rock drainage) (jones2023mechanismsofbioleaching pages 1-2, tonietti2024unveilingthebioleaching pages 2-4)
- **Bioleaching heap/bioreactor conditions** (label-only; low-pH process environment) (jones2023mechanismsofbioleaching pages 1-2, tonietti2024unveilingthebioleaching pages 2-4)
- **High metal(loid) concentrations** (label-only; frequent in AMD/bioleaching) (tonietti2024unveilingthebioleaching pages 2-4, li2023comammoxnitrospiraand pages 1-2)

#### B) Core physiological processes (GO-oriented)
- **Cellular pH homeostasis / regulation of cellular pH** (GO label-only; often summarized as “pH homeostasis”) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Proton transmembrane transport** (GO:0015991) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- **Biofilm formation** (GO:0042710) (tonietti2024unveilingthebioleaching pages 2-4)

#### C) Ion transporters, ATPases, membrane energetics
- **Kdp K+ transporting ATPase / kdpABCDE** (genes; KEGG/label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)
- **Kef-type K+ transport** (genes; label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- **Na+/H+ antiporter (nhaA, nhaB)** (GO:0015385 sodium:proton antiporter activity) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, liu2023molecularmechanismof pages 9-12)
- **P-type ATPases (proton efflux)** (label-only; tied to GO:0015991) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- **F-type ATPase / F0F1 ATP synthase (acidophile-affiliated variants)** (EC:7.1.2.2 label-only) (li2023comammoxnitrospiraand pages 1-2)

#### D) Membrane/envelope adaptations
- **Hopanoids** (CHEBI:51963) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Saturated fatty acids** (CHEBI:26666; label-only context) (yao2023howmethanotrophsrespond pages 5-7)
- **Cyclopropane-fatty-acyl-phospholipid synthase** (EC:2.1.1.79 label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
- **Porin Omp40** (protein; label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **PspA (phage shock protein A)** (protein; label-only) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

#### E) Cytoplasmic proton consumption / buffering
- **Glutamate decarboxylase (Gad; gadB/gadABC)** (GO:0004351) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)
- **Arginine decarboxylase / arginine-dependent acid resistance (Adi; speA)** (label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)
- **Urease system UreABCDEFGHJ** (GO:0009039; EC:3.5.1.5) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, liu2023molecularmechanismof pages 9-12)
- **Spermidine** (CHEBI:15729) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- **Poly-γ-glutamate** (CHEBI:60971) (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

#### F) Niche-building energy metabolisms (bioleaching/AMD relevance)
- **Iron oxidation machinery** (e.g., *cyc2*, *rus*, *petABC*; label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, tonietti2024unveilingthebioleaching pages 2-4)
- **Sulfur oxidation machinery** (e.g., *sqr*, *sdo*, *sox*, *hdrABC*, *tetH*; label-only) (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, tonietti2024unveilingthebioleaching pages 2-4)
- **Ferric iron (Fe3+)** (CHEBI:29033) and **protons (H+)** (CHEBI:15378) as abiotic leaching agents regenerated by microbes (jones2023mechanismsofbioleaching pages 2-5, jones2023mechanismsofbioleaching pages 6-11)

### 3) Evidence-backed candidate causal edges (triples)
The table below is a curation-ready set of candidate edges with evidence, snippets, and uncertainty notes.

| Subject node (suggested grounding) | Predicate | Object node (suggested grounding) | Evidence source | Supporting snippet | Notes / uncertainty |
|---|---|---|---|---|---|
| acidic environment / low external pH (ENVO: acidic environment, label-only) | selects for | obligately acidophilic growth (METPO:1003006) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Acidophiles are defined by low pH optima; moderate acidophiles have growth ranges pH 3–7.5 with optima pH 4–5, and extreme acidophiles have optima <3. Acidic mine drainage, acid sulfate soils, and other acidic habitats are described as selecting for these taxa. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 1-2) | Broad ecological edge; strongest for acidophiles generally, not uniquely obligate acidophiles. Trait boundary to curate with caution because “obligate” additionally implies inability to grow near neutral pH. |
| K+ uptake system Kdp/Kef (KEGG module/label-only; genes kdpA/kdpB/kdpC/kdpD/kdpE, kef) | increases | inside-positive / reversed membrane potential (label-only) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Review describes “inside-positive (inversed) membrane potential via potassium-transporting ATPases and K+ uptake systems (kdp… kdpDEABC) and Kef-type K+ transport” that form an electrochemical barrier to proton influx. Figure schematic also shows Kdp/Kef maintaining an inside-positive membrane potential. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8) | Strong mechanistic edge for acidophiles; direct experimental support may vary by taxon. Suitable core candidate for graph. |
| inside-positive / reversed membrane potential (label-only) | decreases | proton influx (CHEBI:15378 proton) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | The reversed membrane potential is described as creating an electrochemical barrier that repels protons from entering the cytoplasm; similar wording appears in acidophile and acidophilic methanotroph reviews. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom pages 2-4, yao2023howmethanotrophsrespond pages 5-7) | Core causal abstraction widely accepted; not tied to a single gene product. |
| P-type ATPase / proton-translocating ATPase (GO:0015991 proton transmembrane transport; EC/label-only) | increases | proton efflux from cytoplasm (GO:1902600/label-only) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Dopson review lists “active proton efflux via P-type ATPases” as a pH homeostasis strategy. Acidophile reviews broadly describe proton pumps/ATPases as maintaining near-neutral cytoplasm. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, adetunji2024unravelingthepotentials pages 4-6) | Strong general mechanism; exact ATPase family may differ among taxa. |
| F-type ATPase, acidophile-affiliated (EC:7.1.2.2 / label-only) | contributes to | pH homeostasis under acidic conditions (GO:0030641 regulation of cellular pH, label-only) | Li 2023, Applied and Environmental Microbiology, Mar 2023, DOI: 10.1128/aem.00047-23, https://doi.org/10.1128/aem.00047-23 | Acid mine lake comammox Nitrospira MAG “contained diverse metal resistance genes and an acidophile-affiliated F-type ATPase,” interpreted as adaptation to acidic conditions. (li2023comammoxnitrospiraand pages 1-2) | More taxon-specific and inferential than P-type ATPase edge; useful as supporting, not universal, node. |
| Na+/H+ antiporter NhaA/NhaB (GO:0015385 sodium:proton antiporter activity; genes nhaA, nhaB) | exports | proton (CHEBI:15378) | Dopson 2023 / Liu 2023 preprint, DOI: 10.3389/fmicb.2023.1149903 and 10.1101/2023.07.13.548807 | Dopson lists “Na+/H+ exchange (nhaA sodium/proton antiporter)” among pH-homeostasis systems; Liu reports NhaB increased rapidly under acid stress and NhaA active around intracellular pH 6.5 with complementary lower-pH NhaB function. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, liu2023molecularmechanismof pages 9-12) | Strong mechanistic plausibility; Liu evidence is preprint and from Alicyclobacillus acidoterrestris under sublethal acid stress. |
| hopanoid-containing membrane / membrane lipid remodeling (CHEBI:51963 hopanoid, label-only) | decreases | membrane proton permeability (GO:1902600-related, label-only) | Valdez-Nuñez 2024, Environ Microbiol Rep, Oct 2024, DOI: 10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Acid resistance is linked to “hopanoid membrane lipids” and reduced proton permeability; review summarizes proton exclusion as a core strategy. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Strong for acidophiles broadly; some evidence from acidophilic sulfate reducers and prior acidophile literature. |
| saturated fatty acid-rich membrane (CHEBI:26666 saturated fatty acid, label-only) | decreases | membrane proton permeability (label-only) | Yao 2023, Frontiers in Microbiology, Jan 2023, DOI: 10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | Acidophilic methanotrophs form membranes “rich in saturated fatty acids to minimize proton permeability.” (yao2023howmethanotrophsrespond pages 5-7) | Taxon-specific to methanotrophs in cited source; still useful as candidate generalized membrane-impermeability mechanism. Mark uncertain for universal curation. |
| cyclopropane-fatty-acyl-phospholipid synthase / cyclopropane fatty acid formation (EC:2.1.1.79 / label-only) | decreases | membrane proton permeability (label-only) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Review includes “cyclopropane-fatty-acyl-phospholipid synthase” among membrane adaptations that reduce proton permeability. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Inferred functional edge from review synthesis; gene-specific experimental support may be lineage-dependent. |
| Omp40 porin (protein Omp40, label-only) | contributes to | reduced proton entry / acid resistance (label-only) | Valdez-Nuñez 2024 and Dopson 2023, DOI: 10.1111/1758-2229.70019 and 10.3389/fmicb.2023.1149903 | Omp40 is cited as a membrane protein associated with acid resistance; Dopson notes a “unique Omp40 porin in Acidithiobacillus ferrooxidans” among structural defenses. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, dopson2023eurypsychrophilicacidophilesfrom pages 2-4) | Useful but taxon-linked; exact causal role may be more structural than directly measured in all obligate acidophiles. |
| glutamate decarboxylase system Gad / gadB / gadABC (GO:0004351 glutamate decarboxylase activity; genes gadA/gadB/gadC) | consumes | cytoplasmic proton (CHEBI:15378) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Figure/review lists “decarboxylases (Adi, Gad, etc.)” as cytoplasmic proton-consuming systems used in acidophile pH homeostasis. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8) | Mechanistically strong but often inferred from gene presence in genomes/MAGs rather than direct perturbation in every acidophile. |
| arginine decarboxylase / arginine-dependent acid resistance (genes adi, speA; GO:0004054/label-only) | consumes | cytoplasmic proton (CHEBI:15378) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Review identifies “adi, … speA arginine decarboxylase, arginine-dependent acid resistance” among proton-consuming/buffering systems. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8) | Broadly plausible; direct evidence may be genomic/transcriptomic more than knockout-based. |
| urease system UreABCDEFGHJ (GO:0009039 urease activity; EC:3.5.1.5) | increases | cytoplasmic buffering / proton consumption (label-only) | Dopson 2023, Frontiers in Microbiology, Mar 2023, DOI: 10.3389/fmicb.2023.1149903, https://doi.org/10.3389/fmicb.2023.1149903 | Dopson includes “ureABCDEFGHJ urease system” among cytoplasmic proton-consuming/buffering systems; Liu also notes NH3 production can combine with H+ to form NH4+, raising cytoplasmic pH. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, liu2023molecularmechanismof pages 9-12, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8) | Good candidate; taxon distribution uneven. Use caution if curating as universal obligate-acidophile mechanism. |
| spermidine (CHEBI:15729) | decreases | proton influx via porins / strengthens acid resistance (label-only) | Dopson 2023; Valdez-Nuñez 2024, DOI: 10.3389/fmicb.2023.1149903 and 10.1111/1758-2229.70019 | Dopson notes spermidine synthase and spermidine “to inhibit proton influx via porins”; Valdez-Nuñez links spermidine to acid resistance in aSRB. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | More indirect than Kdp/ATPase edges; may act through envelope stabilization and porin effects. |
| poly-gamma-glutamate (CHEBI:60971 poly(gamma-glutamic acid), label-only) | contributes to | acid resistance / reduced proton permeability (label-only) | Valdez-Nuñez 2024, Environ Microbiol Rep, Oct 2024, DOI: 10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Review links production of poly-gamma-glutamate to acid resistance in acidophilic sulfate reducers. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Promising but less established as a universal acidophile mechanism; likely lineage-specific. |
| biofilm formation (GO:0042710 biofilm formation) | creates | protective low-pH microenvironment / local pH regulation (label-only) | Tonietti 2024, Microorganisms, Nov 2024, DOI: 10.3390/microorganisms12122407, https://doi.org/10.3390/microorganisms12122407 | Review states adaptive mechanisms include “biofilm formation that creates microenvironments for pH regulation.” (tonietti2024unveilingthebioleaching pages 2-4) | Likely important in biomining taxa such as Acidithiobacillus ferrooxidans; may not define obligate acidophily itself. |
| iron oxidation pathway (genes cyc2, rus, petABC; GO:0015979-like iron oxidation label-only) | increases | Fe3+ production (CHEBI:29033 ferric iron) | Jones & Santini 2023 / Tonietti 2024, DOI: 10.1042/ebc20220257 and 10.3390/microorganisms12122407 | Bioleaching depends on microbial ferrous iron oxidation regenerating Fe3+; Tonietti lists Cyc2 and related machinery and notes A. ferrooxidans generates iron(III) ions in oxic conditions. (jones2023mechanismsofbioleaching pages 1-2, jones2023mechanismsofbioleaching pages 2-5, tonietti2024unveilingthebioleaching pages 2-4) | Strong application/environment edge; not a direct pH-homeostasis mechanism but central to acidophile niche construction. |
| sulfur oxidation pathway (genes sqr, sdo, sox, hdrABC, tetH; GO sulfur oxidation label-only) | increases | sulfuric acid / proton production (CHEBI:26836 sulfuric acid; CHEBI:15378 proton) | Jones & Santini 2023 / Tonietti 2024, DOI: 10.1042/ebc20220257 and 10.3390/microorganisms12122407 | Sulfur oxidation is described as producing sulfate and regenerating protons; Tonietti explicitly notes sulfur oxidation generating H2SO4 and reactions yielding H+. (jones2023mechanismsofbioleaching pages 1-2, jones2023mechanismsofbioleaching pages 6-11, tonietti2024unveilingthebioleaching pages 2-4) | Strong, directly relevant to environmental acidification and self-reinforcing acidophile habitats. |
| Fe3+ and protons generated by iron/sulfur oxidation (CHEBI:29033, CHEBI:15378) | increases | sulfide mineral dissolution / metal release (label-only) | Jones & Santini 2023, Essays in Biochemistry, Aug 2023, DOI: 10.1042/ebc20220257, https://doi.org/10.1042/ebc20220257 | Review explains that protons and Fe3+ attack sulfide minerals, releasing metals; microbial activity regenerates these oxidants in bioleaching. (jones2023mechanismsofbioleaching pages 1-2, jones2023mechanismsofbioleaching pages 2-5, jones2023mechanismsofbioleaching pages 6-11) | Application edge for biomining rather than trait-defining physiology, but useful environmental context node. |
| iron/sulfur oxidation by acidophiles (label-only) | acidifies | acid mine drainage / bioleaching environment (ENVO: acid mine drainage, label-only) | Jones & Santini 2023; Tonietti 2024; Wei 2024, DOI: 10.1042/ebc20220257, 10.3390/microorganisms12122407, 10.3389/fmicb.2024.1412599 | Bioleaching mirrors natural AMD because sulfuric acid is generated; Wei notes AMD generation results from sulfide oxidation and dissolution facilitated by microbial catalysis, with strongest acidity associated with acidophilic iron oxidizers. (jones2023mechanismsofbioleaching pages 1-2, tonietti2024unveilingthebioleaching pages 2-4, gonzalez2024acidophilicheterotrophsbasic pages 1-2) | Strong environmental feedback edge; can support graph nodes linking organismal trait to habitat construction. |
| acidophilic community in AMD / biomining systems (ENVO: acid mine drainage, label-only) | enables | metal recovery / biomining process performance (label-only) | González 2024; Tonietti 2024; Jones & Santini 2023 | Acidophilic heterotrophs and autotrophs are applied in biomining and bioremediation; A. ferrooxidans mobilizes many elements and is key in bioleaching technologies; bioleaching is a low-input extraction method exploiting acidophilic sulfur/iron metabolisms. (gonzalez2024acidophilicheterotrophsbasic pages 1-2, jones2023mechanismsofbioleaching pages 1-2, tonietti2024unveilingthebioleaching pages 1-2) | Application-level edge; not appropriate as a mechanistic intracellular edge but useful for broader causal graph context if environmental outputs are modeled. |
| acidophile pH-homeostasis system (aggregate node) | maintains | intracellular pH around 6 despite external pH <3 (label-only) | Valdez-Nuñez 2024, Environ Microbiol Rep, Oct 2024, DOI: 10.1111/1758-2229.70019, https://doi.org/10.1111/1758-2229.70019 | Acidophiles “usually maintain an internal pH of around 6.0 while growing at pH lower than 3.0” through proton exclusion, exchange, pumping, consumption, and buffering. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4) | Very useful integrative phenotype edge; broad/general and not a single molecular entity. |
| obligate acidophilic phenotype (METPO:1003006) | associated with | no growth near neutral/alkaline pH (label-only) | Ianutsevich 2023, Microorganisms, Jul 2023, DOI: 10.3390/microorganisms11071733, https://doi.org/10.3390/microorganisms11071733 | Review snippet reports some fungi “belong to obligate acidophiles since their growth optimum is at pH 4.0, while there is no growth at pH … [higher pH].” (dopson2023eurypsychrophilicacidophilesfrom pages 8-9) | Evidence appears from fungal acidophiles and snippet is truncated in retrieved text; use as trait-boundary support, but avoid over-curation until exact growth table/figure is checked. |


*Table: This table compiles curation-ready candidate causal edges for obligate acidophily, linking pH-homeostasis mechanisms, membrane adaptations, and habitat-forming metabolisms to the phenotype and to biomining/AMD contexts. It prioritizes 2023–2024 review and primary evidence and flags where claims are broad, inferred, or taxon-specific.*

### 4) Recent developments and latest research (2023–2024 emphasis)
**(i) Omics-driven identification of conserved low-pH adaptations**
A 2023 synthesis focusing on eurypsychrophilic acidophiles highlights how metagenomics/transcriptomics accelerated the identification of **K+ uptake systems (kdp/Kef), Na+/H+ exchange, membrane remodeling (hopanoids, cyclopropane fatty acids), proton-consuming decarboxylases/urease, and proteostasis modules** as recurring low-pH adaptations across mine drainage and related ecosystems. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)

**(ii) Quantitative framing of “near-neutral internal pH” under extreme acidity**
A 2024 review on acidophilic sulfate-reducing bacteria states that acidophiles “usually maintain an internal pH of around **6.0** while growing at external pH **<3.0**,” and organizes mechanisms into proton exclusion/exchange/pumping/consumption and buffering, while also emphasizing envelope components (hopanoids; Omp40; PspA; poly-γ-glutamate; spermidine). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

**(iii) New genomic evidence for acid adaptation in acidic mine lakes**
A 2023 study of an **acid mine lake** found pH **<5** with **175 mg-N/L ammonium**, and reported active nitrification in sediments; a recovered comammox *Nitrospira* MAG encoded an “acidophile-affiliated F-type ATPase,” supporting the idea that acid-adapted ATPases are part of the acid-stress toolkit in some lineages. (li2023comammoxnitrospiraand pages 1-2)

### 5) Current applications and real-world implementations (with recent quantitative data)

#### A) Biomining / bioleaching (industrial and pilot relevance)
- A 2024 review on *Acidithiobacillus ferrooxidans* reports it thrives at **pH ~1.5–2.5** and links its iron/sulfur oxidation reactions to generation of **Fe3+** and **H2SO4**, which chemically attack metal sulfides; it also highlights biofilm formation as a process-relevant adaptation for creating microenvironments favorable to pH regulation on mineral surfaces. (tonietti2024unveilingthebioleaching pages 2-4)
- A 2023 mechanistic review emphasizes why acidophilic physiology is functionally required in bioleaching: at **low pH**, abiotic Fe2+ oxidation is very slow so microbial iron oxidation is essential; the review also quantifies redox potentials at pH 2 (Fe2+/Fe3+ couple +0.77 V; O2/H2O +1.12 V), explaining why iron oxidation is aerobic in acidophiles and how Fe3+/H+ are regenerated for continued mineral dissolution. (jones2023mechanismsofbioleaching pages 2-5)

#### B) Acid mine drainage (AMD) treatment / bioremediation concepts
- Acidophilic sulfate-reducing bacteria are highlighted for AMD treatment, with reported engineered system operating ranges including **bioreactors pH ~2.5–3.5** and AMD treatment around **pH ~3.4–3.7** (context-dependent), indicating that some remediation strategies aim to function without fully neutralizing acidity. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)

#### C) Ecosystem function and monitoring: acidic mine lake nitrification as a quantitative example
- In sediments of an acidic mine lake with **pH <5** and **175 mg-N/L ammonium**, maximum nitrate production potential was reported as **70.5 μg-N/(g dw·day)**, and amoA gene abundance fractions were **52% comammox Nitrospira** and **41% ammonia-oxidizing archaea**, demonstrating that key biogeochemical functions can be sustained in acidic systems dominated by acid-adapted guilds. (li2023comammoxnitrospiraand pages 1-2)

### 6) Expert synthesis / authoritative interpretation (for curation)
Across recent reviews, a convergent mechanism emerges for acidophilic growth:
1. **Electrostatic proton exclusion** via an **inside-positive (reversed) membrane potential**, often supported by **K+ uptake (Kdp/Kef)** and other cation transport. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)
2. **Active proton efflux** via ATPases and ion antiporters (including Na+/H+ exchange). (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, liu2023molecularmechanismof pages 9-12)
3. **Reduced membrane proton permeability** through lipid/envelope remodeling (hopanoids, saturated/cyclopropane fatty acids; specialized porins and stress proteins). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4, yao2023howmethanotrophsrespond pages 5-7, dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
4. **Cytoplasmic proton consumption/buffering** (decarboxylases, urease; polyamines and polymers). (dopson2023eurypsychrophilicacidophilesfrom pages 8-9, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
5. **Community and surface-associated strategies** such as **biofilms**, particularly relevant in biomining where mineral surfaces and microenvironments matter. (tonietti2024unveilingthebioleaching pages 2-4)

### 7) Warnings / not-yet-curatable items
1. **Obligate vs non-obligate boundary evidence is incomplete in extracted text:** the fungal paper snippet indicating “no growth at pH …” is truncated in current evidence, so the precise neutral/alkaline cutoff cannot be curated from this run without checking the full table/figure text. Treat “no growth above pH X” as **pending** until verified. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9)
2. **Taxon-specific extrapolation risk:** Some mechanistic evidence comes from acidophilic methanotrophs (membrane saturated fatty acids) or acidophilic sulfate reducers (poly-γ-glutamate), which may not generalize to all obligate acidophiles. Curate such nodes/edges with an “uncertain/taxon-specific” flag. (yao2023howmethanotrophsrespond pages 5-7, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
3. **Preprint caution:** Acid stress response mechanisms in *Alicyclobacillus acidoterrestris* are from a preprint; useful for hypothesis generation but lower authority than peer-reviewed evidence. (liu2023molecularmechanismof pages 9-12)

---

## DOI-first bibliography (URLs + publication dates where available)
- Dopson M, González-Rosales C, Holmes DS, Mykytczuk N. **Eurypsychrophilic acidophiles: From (meta)genomes to low-temperature biotechnologies.** *Frontiers in Microbiology* (Mar 2023). https://doi.org/10.3389/fmicb.2023.1149903 (dopson2023eurypsychrophilicacidophilesfrom pages 1-2, dopson2023eurypsychrophilicacidophilesfrom pages 8-9, dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)
- Valdez-Nuñez LF, Kappler A, Ayala-Muñoz D, et al. **Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.** *Environmental Microbiology Reports* (Oct 2024). https://doi.org/10.1111/1758-2229.70019 (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4)
- Tonietti L, Esposito M, Cascone M, et al. **Unveiling the Bioleaching Versatility of Acidithiobacillus ferrooxidans.** *Microorganisms* (Nov 2024). https://doi.org/10.3390/microorganisms12122407 (tonietti2024unveilingthebioleaching pages 2-4, tonietti2024unveilingthebioleaching pages 1-2)
- González E, Vera F, Scott F, et al. **Acidophilic heterotrophs: basic aspects and technological applications.** *Frontiers in Microbiology* (May 2024). https://doi.org/10.3389/fmicb.2024.1374800 (gonzalez2024acidophilicheterotrophsbasic pages 1-2, gonzalez2024acidophilicheterotrophsbasic pages 3-4)
- Jones S, Santini JM. **Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms.** *Essays in Biochemistry* (Aug 2023). https://doi.org/10.1042/ebc20220257 (jones2023mechanismsofbioleaching pages 1-2, jones2023mechanismsofbioleaching pages 2-5, jones2023mechanismsofbioleaching pages 6-11)
- Li D, Ren Z, Zhou Y, et al. **Comammox Nitrospira and ammonia-oxidizing archaea are dominant ammonia oxidizers in sediments of an acid mine lake containing high ammonium concentrations.** *Applied and Environmental Microbiology* (Mar 2023). https://doi.org/10.1128/aem.00047-23 (li2023comammoxnitrospiraand pages 1-2)
- Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology* (Jan 2023). https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 5-7)

**Additional (lower-authority) mechanistic source used for hypothesis support:**
- Liu X, Wu Y, Jiao L, et al. **Molecular mechanism of acid stress response of A. acidoterrestris DSM 3922T under sublethal pH environment.** *bioRxiv* (Jul 2023). https://doi.org/10.1101/2023.07.13.548807 (liu2023molecularmechanismof pages 9-12)

---

## Figure evidence
A schematic diagram summarizing acidophile pH-homeostasis mechanisms (Kdp/Kef/Nha transporters, membrane impermeability, decarboxylases/urease, and other modules) is available from Dopson et al. 2023 (Figure 4). (dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8)


References

1. (dopson2023eurypsychrophilicacidophilesfrom pages 8-9): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

2. (dopson2023eurypsychrophilicacidophilesfrom media d45c2cd8): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

3. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 2-4): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 19 citations and is from a peer-reviewed journal.

4. (tonietti2024unveilingthebioleaching pages 2-4): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 45 citations.

5. (gonzalez2024acidophilicheterotrophsbasic pages 1-2): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.

6. (dopson2023eurypsychrophilicacidophilesfrom pages 1-2): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

7. (dopson2023eurypsychrophilicacidophilesfrom pages 2-4): Mark Dopson, Carolina González-Rosales, David S. Holmes, and Nadia Mykytczuk. Eurypsychrophilic acidophiles: from (meta)genomes to low-temperature biotechnologies. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1149903, doi:10.3389/fmicb.2023.1149903. This article has 20 citations and is from a peer-reviewed journal.

8. (jones2023mechanismsofbioleaching pages 1-2): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 84 citations and is from a peer-reviewed journal.

9. (li2023comammoxnitrospiraand pages 1-2): Deyong Li, Zhichang Ren, Yangqi Zhou, Lugao Jiang, Min Zheng, and Guoqiang Liu. Comammox <i>nitrospira</i> and ammonia-oxidizing archaea are dominant ammonia oxidizers in sediments of an acid mine lake containing high ammonium concentrations. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.00047-23, doi:10.1128/aem.00047-23. This article has 32 citations and is from a peer-reviewed journal.

10. (liu2023molecularmechanismof pages 9-12): Xiaoxue Liu, Youzhi Wu, Lingxia Jiao, Junjian Ran, Linjun Sun, Fuzhou Ye, Xin-hong Liang, and Ruixiang Zhao. Molecular mechanism of acid stress response of a. acidoterrestris dsm 3922t under sublethal ph environment. bioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.13.548807, doi:10.1101/2023.07.13.548807. This article has 0 citations.

11. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

12. (jones2023mechanismsofbioleaching pages 2-5): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 84 citations and is from a peer-reviewed journal.

13. (jones2023mechanismsofbioleaching pages 6-11): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 84 citations and is from a peer-reviewed journal.

14. (adetunji2024unravelingthepotentials pages 4-6): Adegoke Isiaka Adetunji and Mariana Erasmus. Unraveling the potentials of extremophiles in bioextraction of valuable metals from industrial solid wastes: an overview. Minerals, 14:861, Aug 2024. URL: https://doi.org/10.3390/min14090861, doi:10.3390/min14090861. This article has 7 citations.

15. (tonietti2024unveilingthebioleaching pages 1-2): Luca Tonietti, Mattia Esposito, Martina Cascone, Bernardo Barosa, Stefano Fiscale, Maria Teresa Muscari Tomajoli, Tomasa Sbaffi, Rosa Santomartino, Giovanni Covone, Angelina Cordone, Alessandra Rotundi, and Donato Giovannelli. Unveiling the bioleaching versatility of acidithiobacillus ferrooxidans. Microorganisms, 12:2407, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122407, doi:10.3390/microorganisms12122407. This article has 45 citations.

16. (gonzalez2024acidophilicheterotrophsbasic pages 3-4): Ernesto González, Fernando Vera, Felipe Scott, Cecilia Guerrero, Juan M. Bolívar, Germán Aroca, Jesús Ángel Muñoz, Miguel Ladero, and Victoria E. Santos. Acidophilic heterotrophs: basic aspects and technological applications. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1374800, doi:10.3389/fmicb.2024.1374800. This article has 7 citations and is from a peer-reviewed journal.