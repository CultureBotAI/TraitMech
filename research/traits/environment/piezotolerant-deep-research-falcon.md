---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:56:14.456629'
end_time: '2026-06-18T01:05:44.656310'
duration_seconds: 570.2
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: piezotolerant
  trait_identifier: traitmech:000003
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: piezotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure growth preference in which an organism can grow under elevated
    hydrostatic pressure but grows at similar or faster rates at atmospheric pressure
    (0.1 MPa).
  parent_traits: METPO:1000059
  synonyms: barotolerant
  evidence_summary: 'DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP
    are usually known as piezophiles, referring to their preference for high pressure
    (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand
    high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure,
    from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140
    MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile
    reference point against which piezotolerant (atmospheric-capable) growth is defined.)'
  causal_graph_summary: 'piezotolerance_pressure_range: 3 nodes, 2 edges'
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
- **Trait label:** piezotolerant
- **METPO identifier:** traitmech:000003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism can grow under elevated hydrostatic pressure but grows at similar or faster rates at atmospheric pressure (0.1 MPa).
- **Parent traits:** METPO:1000059
- **Synonyms:** barotolerant
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure, from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile reference point against which piezotolerant (atmospheric-capable) growth is defined.)
- **Existing causal graph summary:** piezotolerance_pressure_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **piezotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezotolerant.yaml`.

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
- **Trait label:** piezotolerant
- **METPO identifier:** traitmech:000003
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism can grow under elevated hydrostatic pressure but grows at similar or faster rates at atmospheric pressure (0.1 MPa).
- **Parent traits:** METPO:1000059
- **Synonyms:** barotolerant
- **Existing evidence:** DOI:10.3389/fmolb.2022.1058381: Microorganisms adapted to HHP are usually known as piezophiles, referring to their preference for high pressure (Pressure-adaptation review distinguishes piezotolerant organisms, which withstand high hydrostatic pressure but grow at similar or faster rates at atmospheric pressure, from obligate piezophiles.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Provides the contrasting obligate-piezophile reference point against which piezotolerant (atmospheric-capable) growth is defined.)
- **Existing causal graph summary:** piezotolerance_pressure_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **piezotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/piezotolerant.yaml`.

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


## Research report: Microbial trait **piezotolerant** (barotolerant) — TraitMech candidate (traitmech:000003)

### 1) Scope summary (trait definition, boundaries, assays)

**Trait meaning (growth phenotype, not mere survival):** In current usage, *piezotolerant* (syn. **barotolerant**) refers to organisms that can **withstand and grow under elevated hydrostatic pressure** but have **similar or faster growth rates at atmospheric pressure**, in contrast to **obligate piezophiles**, which can **only grow under high hydrostatic pressure (HHP)**. (tamby2023microbialmembranelipid pages 1-2)

**Nearby/contrast traits:**
- **Piezophile / piezophilic:** organisms that **grow optimally at pressures above atmospheric (0.1 MPa)**. (malas2024biologicalfunctionsat pages 1-2)
- **Piezotolerant vs piezophilic terminology:** one operational definition contrasts **piezotolerant vs piezophilic growth** as “the ability to grow or preferentially grow, respectively, at high hydrostatic or lithostatic pressures.” (coffin2024responseandadaptation pages 1-2)
- **Baroresistance/pressure resistance (food microbiology):** HHP/HPP in food contexts is typically an **inactivation** treatment; “survivors” and “recovery” are discussed, but these do **not** necessarily imply a growth preference phenotype (piezotolerance) and are strongly assay/matrix dependent. (wisniewski2023impactofhighpressure pages 1-2, shymialevich2024thenovelconcept pages 4-5)

**Boundary cases (important for curation):**
- **Short exposure survival at very high pressure** (e.g., minutes at ≥150 MPa or far higher) is distinct from *growth under pressure*. Non-piezophilic taxa can survive brief exposures, whereas sustained growth/adaptation is a different phenotype and mechanism set. (malas2024biologicalfunctionsat pages 1-2)
- **Confounding with temperature (psychrophily):** deep-sea pressure and low temperature co-occur; multiple sources caution that lipid and other “pressure” signatures can be hard to disentangle from cold adaptation. (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 9-10)

**Assay readouts commonly used:** growth rate/biomass under defined pressure series (0.1 MPa baseline vs elevated MPa), plus omics and physiological measurements (membrane composition, transcriptomics, compatible-solute profiling). (tamby2023microbialmembranelipid pages 1-2, malas2024biologicalfunctionsat pages 1-2)

---

### 2) Key concepts and definitions (current understanding)

#### 2.1 Hydrostatic pressure context
- Deep sea becomes >10 MPa at depths >1,000 m and increases about **~1 MPa per 100 m**. (tamby2023microbialmembranelipid pages 1-2)
- Highest explored deep-sea habitat pressures are **~110 MPa** (Challenger Deep). (malas2024biologicalfunctionsat pages 1-2)

#### 2.2 Demonstrated biological pressure limits and illustrative phenotypes
- One review notes a “currently demonstrated microbial growth limit” of **140 MPa**. (malas2024biologicalfunctionsat pages 1-2)
- A non-piezophilic bacterium (*Shewanella oneidensis* MR‑1) was reported metabolically active and capable of viable growth following **2 h exposure at 158 MPa**. (malas2024biologicalfunctionsat pages 1-2)
- A laboratory-evolved *E. coli* strain (AN62) is described as **piezotolerant (not piezophilic)** and “capable of growth up to **62 MPa**.” (coffin2024responseandadaptation pages 1-2)

#### 2.3 Canonical mechanistic theme: maintaining function under pressure
Across bacteria/archaea discussed in recent reviews, pressure perturbs (i) membrane packing/fluidity, (ii) protein folding/complex stability, (iii) respiratory chain performance, and (iv) macromolecular processes such as translation and DNA transactions; adaptation often involves coordinated changes in lipids, stress regulons/chaperones, solute composition (piezolytes), and energy metabolism. (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10, coffin2024responseandadaptation pages 1-2)

---

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 Membrane lipid adaptation as a curated mechanism hub (2023)
A 2023 Frontiers review emphasizes that increasing HHP is often associated with increased abundance of membrane lipids containing **unsaturated and branched-chain fatty acids**, consistent with maintaining membrane properties under pressure. (tamby2023microbialmembranelipid pages 1-2)

It also formalizes mechanistic concepts of **homeoviscous adaptation** (adjusting lipid composition to maintain fluidity) and **homeophasic adaptation** (adjusting proportions in crystalline states) (tamby2023microbialmembranelipid pages 2-4), and summarizes organism-level examples and optima (e.g., Photobacterium profundum SS9 listed with optimal growth pressure **28 MPa at 15°C** in the paper’s Table 1). (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid media 3c77da24)

#### 3.2 Heat-shock response as a measurable pressure response (2024)
A 2024 study quantified single-cell and population-level transcriptional responses of key heat shock genes to pressure shock in *E. coli* and showed **rpoH, rpoE, dnaK, groEL** are transcriptionally upregulated after pressure shock. (coffin2024responseandadaptation pages 1-2)

The same work reports distinct regulation patterns in the pressure-adapted strain (AN62) and suggests **RpoE** could act as a **pressure sensor** (uncertain mechanistic status; transcriptional stochasticity interpreted as feedback/sensing). (coffin2024responseandadaptation pages 1-2)

#### 3.3 Non-piezophiles showing robust high-pressure responses (2024; astrobiology-relevant)
A 2024 transcriptomics study of *S. oneidensis* MR‑1 at **158 MPa** reports regulation of **arginine biosynthesis genes (argA/argB/argC/argF)**, “genes involved in membrane reconfiguration,” and stress responses including **cold-shock protein CspG** and antioxidant defense genes—supporting the view that pressure tolerance can involve generalized stress modules plus membrane remodeling. (malas2024biologicalfunctionsat pages 1-2)

---

### 4) Candidate causal-graph entities (nodes) for `piezotolerant.yaml`

Below are curation-ready candidate nodes, grouped by type, with suggested ontology grounding where possible (label-only where unclear).

#### A. Environmental / experimental factors
- **High hydrostatic pressure (HHP)** (ENVO label; pressure values in MPa are assay parameters) (tamby2023microbialmembranelipid pages 1-2)
- **Temperature** (confounder with HHP in deep sea) (tamby2023microbialmembranelipid pages 1-2)
- **Nutrient/carbon conditions** (e.g., glucose dependence of certain piezolytes) (scheffer2023themysteryof pages 9-10)
- **Food-matrix variables** (pH, water activity, fat/oil content) affecting pressure outcomes in applied HPP (shymialevich2024thenovelconcept pages 5-7)

#### B. Cellular structures & processes
- **Membrane fluidity / membrane stability** (label-only process node) (scheffer2023themysteryof pages 6-7)
- **Homeoviscous adaptation** (label-only process node) (tamby2023microbialmembranelipid pages 2-4)
- **Protein folding/proteome stability / heat-shock response** (GO:0006457 protein folding as an anchor) (coffin2024responseandadaptation pages 1-2)
- **Respiratory electron transport chain remodeling** (GO label) (scheffer2023themysteryof pages 7-9)
- **Motility / flagellar assembly** (GO:0009288 bacterial-type flagellum assembly as anchor) (scheffer2023themysteryof pages 6-7)

#### C. Genes / proteins (examples explicitly named in evidence)
- **rpoH (σ32), rpoE (σE), dnaK, groEL** (heat-shock/stress response) (coffin2024responseandadaptation pages 1-2)
- **argA, argB, argC, argF** (arginine biosynthesis; pressure-regulated in MR‑1 study) (malas2024biologicalfunctionsat pages 1-2)
- **ompH** (outer-membrane porin upregulated under pressure) (scheffer2023themysteryof pages 7-9)
- **pfa operon** (ω-3 PUFA synthase operon; pressure vs cold confounding noted) (scheffer2023themysteryof pages 6-7)
- **δ‑9‑acyl‑phospholipid‑desaturase** (reported only in piezophilic *Colwellia* in cited review) (scheffer2023themysteryof pages 6-7)
- **Flagellar genes (examples cited: flaB3, fliD, fliA)** (taxon-specific growth effect under pressure) (scheffer2023themysteryof pages 6-7)
- **Respiration components** (label-only unless mapped in a given taxon): cytochrome c‑551; terminal quinol oxidase (pressure-conditional expression in *Shewanella*) (scheffer2023themysteryof pages 7-9)

#### D. Metabolites / chemicals (CHEBI candidates)
- **Unsaturated fatty acids; branched-chain fatty acids; ω‑3 polyunsaturated fatty acids (PUFAs)** (membrane remodeling) (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 6-7)
- **Eicosapentaenoic acid (EPA; C20:5)** (PUFA associated with HHP adaptation in some bacteria) (tamby2023microbialmembranelipid pages 2-4)
- **“Piezolytes” / compatible solutes:** glutamate, betaine, β‑hydroxybutyrate (3‑hydroxybutyrate) (scheffer2023themysteryof pages 9-10)
- **TMAO (trimethylamine N‑oxide)** (energy substrate and/or piezolyte in some taxa) (scheffer2023themysteryof pages 9-10)

#### E. Applied HPP nodes (food processing; separate but adjacent causal subgraph)
- **High-pressure processing (HPP/HHP) parameters:** pressure (100–600 MPa typical), time (minutes), temperature (ambient or lower), adiabatic heating (~3–6°C per 100 MPa) (wisniewski2023impactofhighpressure pages 1-2, shymialevich2024thenovelconcept pages 2-4)
- **Sublethal injury / VBNC states / recovery during storage** (label-only) (wisniewski2023impactofhighpressure pages 6-7, shymialevich2024thenovelconcept pages 4-5)
- **Spore germination machinery:** gerA-type germination receptors; SpoVA channels; CaDPA (calcium dipicolinate) release (shymialevich2024thenovelconcept pages 7-8)

---

### 5) Candidate causal edges (evidence-backed triples)

The following table is designed for direct curation into a TraitMech-style causal graph. Uncertainty flags indicate potential temperature confounding, taxon specificity, or inference beyond direct causality.

| Edge (subject–predicate–object) | Entity type(s) | Ontology grounding suggestions | Evidence snippet | Source |
|---|---|---|---|---|
| Elevated hydrostatic pressure (HHP) → decreases → membrane fluidity | environment → cellular process | ENVO:high hydrostatic pressure (label); GO:0016042 lipid catabolic process? / label-only “membrane fluidity” | “high hydrostatic pressure reduces membrane fluidity by compacting fatty acids” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| Reduced membrane fluidity → causes increase in → unsaturated fatty acids | cellular process → metabolite class | CHEBI:unsaturated fatty acid | organisms counter HHP by “increasing the proportions of unsaturated fatty acids” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| HHP → increases abundance of → branched-chain and unsaturated membrane fatty acids | environment → metabolite class | CHEBI:branched-chain fatty acid; CHEBI:unsaturated fatty acid | “abundance of membrane lipids containing unsaturated and branched-chain fatty acids increases with increasing HHP” (tamby2023microbialmembranelipid pages 1-2) | 10.3389/fmolb.2022.1058381, 2023, https://doi.org/10.3389/fmolb.2022.1058381 |
| pfa operon → enables increase in → ω-3 polyunsaturated fatty acids [uncertain: pressure vs temperature confounded] | gene cluster/pathway → metabolite class | label-only pfa operon; CHEBI:omega-3 fatty acid | “increase of ω-3 polyunsaturated fatty acids was found in response to high hydrostatic pressure… the pfa operon is identified as encoding an ‘ω-3 polyunsaturated fatty acid synthase’… unclear if the pfa operon responds to… high pressure or low temperature” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| δ-9-acyl-phospholipid-desaturase → contributes to synthesis of → unsaturated membrane fatty acids [taxon-specific] | enzyme → metabolite class | EC/UniProt unclear; label-only δ-9-acyl-phospholipid-desaturase; CHEBI:unsaturated fatty acid | “A specific desaturase, ‘δ-9-acyl-phospholipid-desaturase,’ is noted only in piezophilic Colwellia” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| HHP → induces transcription of → rpoH/rpoE/dnaK/groEL | environment → genes/proteins | GO:0006457 protein folding; UniProt/NCBI Gene label-only: rpoH, rpoE, dnaK, groEL | “key heat shock genes-rpoH, rpoE, dnaK, and groEL- are transcriptionally upregulated following pressure shock” (coffin2024responseandadaptation pages 1-2) | 10.3389/fmicb.2024.1470617, 2024, https://doi.org/10.3389/fmicb.2024.1470617 |
| RpoE signaling → may act as → pressure sensor [uncertain] | sigma factor/protein → function | label-only RpoE; GO:0001076? / label-only “pressure sensor” | “suggesting that RpoE could act as a pressure sensor” (coffin2024responseandadaptation pages 1-2) | 10.3389/fmicb.2024.1470617, 2024, https://doi.org/10.3389/fmicb.2024.1470617 |
| HHP → induces accumulation of → piezolytes (glutamate, betaine, β-hydroxybutyrate) | environment → metabolites | CHEBI:glutamate; CHEBI:betaine; CHEBI:3-hydroxybutyrate | “‘piezolytes’… molecules that accumulate in cells in response to high pressure… Examples include glutamate, betaine, and β-hydroxybutyrate” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| Piezolyte accumulation → protects → proteins under pressure | metabolites → biological process | GO:0042594 response to starvation? / label-only “preferential hydration”; CHEBI terms as above | compatible solutes “act via preferential hydration to protect proteins” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| HHP → increases → glutamate accumulation | environment → metabolite | CHEBI:glutamate | “2.25-fold increase in glutamate accumulation under high pressure compared to atmospheric pressure” (scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| TMAO reduction / TMAO reductase activity → supports growth at → elevated pressure [taxon-specific] | enzyme/pathway → phenotype/environment | CHEBI:trimethylamine N-oxide; EC/GO label-only TMAO reductase | “increased TMAO reductase activity linked to growth at 30 MPa” and TMAO used for “pressure tolerance” (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| High pressure (~60 MPa) → remodels respiratory chain to → cytochrome c-551 + terminal quinol oxidase [taxon-specific] | environment → proteins/pathway | label-only cytochrome c-551; GO:respiratory electron transport chain | “at 60 MPa the bc-1/terminal oxidase are replaced by cytochrome c-551 and a quinol oxidase; quinol oxidase expressed only at high pressure” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| Low temperature/high pressure → induces expression of → type I DMSO reduction system [uncertain, cross-adaptation] | environment → pathway | CHEBI:dimethyl sulfoxide; label-only DMSO reductase system | “DMSO reduction systems with type I expressed under low temperature/high pressure, and type II at higher temp/lower pressure” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| Elevated pressure → upregulates → OmpH | environment → outer membrane protein | label-only OmpH; GO:0016020 membrane | “increased OmpH abundance with pressure (0.1 -> 28 MPa; ~10–100× increase)” (scheffer2023themysteryof pages 7-9) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| OmpH upregulation → may maintain → membrane transport under pressure [inferred] | protein → process | label-only OmpH; GO:0055085 transmembrane transport | porins/OMPs “adapt… to maintain transport under pressure” with OmpH upregulation noted (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 2-4) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629; 10.3389/fmolb.2022.1058381, 2023, https://doi.org/10.3389/fmolb.2022.1058381 |
| Flagellar biosynthesis genes (flaB3/fliD/fliA) → enable growth at → high pressure [taxon-specific] | genes/proteins → phenotype | GO:0009288 bacterial-type flagellum assembly | “mutants ∆flaB3, ∆fliD, ∆fliA non-motile and slower under high hydrostatic pressure” (scheffer2023themysteryof pages 6-7) | 10.3390/microorganisms11071629, 2023, https://doi.org/10.3390/microorganisms11071629 |
| HPP/HHP (100–600 MPa) → inactivates → Listeria monocytogenes | environment/process → organism | NCBITaxon:Listeria monocytogenes; ENVO:high-pressure processing (label) | “Typical pressure ranges cited are 100–600 MPa” and HPP “can reduce L. monocytogenes to below detection limits” (wisniewski2023impactofhighpressure pages 1-2) | 10.3390/foods13010014, 2023, https://doi.org/10.3390/foods13010014 |
| HPP/HHP → causes → sublethal injury and recovery of survivors | process/environment → phenotype/process | label-only sublethal injury; VBNC state label-only | “sublethally injured cells can regenerate” and survivors “may recover during storage” (shymialevich2024thenovelconcept pages 4-5, wisniewski2023impactofhighpressure pages 1-2) | 10.3390/foods13162519, 2024, https://doi.org/10.3390/foods13162519; 10.3390/foods13010014, 2023, https://doi.org/10.3390/foods13010014 |
| Moderate-high pressure (50–300 MPa) → activates → gerA-type spore germination receptors | environment/process → receptor/process | label-only gerA-type germination receptor | “moderate–high-pressure (MHP) treatments (50–300 MPa) activate gerA-type germination receptors” (shymialevich2024thenovelconcept pages 5-7, shymialevich2024thenovelconcept pages 7-8) | 10.3390/foods13162519, 2024, https://doi.org/10.3390/foods13162519 |
| Very high pressure (400–600 MPa) → opens → SpoVA channels causing CaDPA release | environment/process → channel/metabolite | label-only SpoVA; CHEBI:calcium dipicolinate / CaDPA label-only | “VHP (400–600 MPa) … opens SpoVA channels causing release of CaDPA” (shymialevich2024thenovelconcept pages 7-8) | 10.3390/foods13162519, 2024, https://doi.org/10.3390/foods13162519 |


*Table: This table compiles candidate causal edges for the microbial trait piezotolerant/barotolerant from the gathered evidence, including mechanistic nodes, pressure-response pathways, and food-HPP context. It is designed to support TraitMech curation by highlighting ontology grounding options, direct evidence snippets, and uncertainty flags.*

**Visual corroboration from a recent synthesis:** Tamby et al. summarize piezophile/piezotolerant strains and optima in a consolidated Table 1 and illustrate membrane-adaptation concepts (e.g., increased unsaturation changing membrane packing/fluidity) in a figure; these are useful as high-level evidence of the “membrane lipid remodeling ↔ pressure” concept cluster. (tamby2023microbialmembranelipid media 3c77da24, tamby2023microbialmembranelipid media 7b9a160e)

---

### 6) Current applications and real-world implementations

#### 6.1 Food high-pressure processing (HPP/HHP)
High-pressure processing is widely deployed as a **non-thermal** preservation step and is typically described with **pressure ranges of 100–600 MPa** with operation times of **minutes** and temperatures “room temperature or lower.” (wisniewski2023impactofhighpressure pages 1-2)

A 2024 Foods review frames “ultra-high pressures” for food products as **200–800 MPa**, and cites an early example of **650 MPa for 10 min at room temperature**; it also notes **adiabatic heating** of approximately **3–6 °C per 100 MPa**, which is relevant when mapping treatment conditions to biological responses. (shymialevich2024thenovelconcept pages 2-4, shymialevich2024thenovelconcept pages 1-2)

**Survivors and recovery (barotolerance-like behavior):** For *Listeria monocytogenes*, HPP can reduce cells to below detection, but survivors may recover during storage; survivors may also show altered expression of virulence- and antibiotic-resistance-related genes (mechanisms remain incompletely explained in available literature). (wisniewski2023impactofhighpressure pages 1-2)

A specific example of post-HPP recovery dependence on storage temperature is provided in the 2024 review: after treatment at **500 MPa, 25°C, 10 min**, no colonies were observed after storage at **4°C for 120 h**, but regrowth was observed at warmer storage temperatures (25°C; variable regrowth at 0°C and 15°C with reported values). (shymialevich2024thenovelconcept pages 5-7)

#### 6.2 Spore control and pressure-triggered germination strategies
For spore-formers, moderate–high pressure (**50–300 MPa**) can activate **gerA-type germination receptors**, whereas very high pressure (**400–600 MPa**) can open **SpoVA channels** and drive **CaDPA release**, which is associated with increased spore susceptibility. (shymialevich2024thenovelconcept pages 7-8)

For *Clostridium botulinum* spores, a 2023 Foods review highlights that spores can be extremely pressure resistant at ambient temperature (e.g., **1500 MPa at 20°C for 5 min** did not significantly inactivate spores), emphasizing why combined pressure–temperature strategies are often needed for spore hazards. (munir2023physicaltreatmentsto pages 12-14)

---

### 7) Expert synthesis / analysis (authoritative interpretations)

**Consensus mechanism hubs appropriate for TraitMech nodes/edges:**
1. **Membrane lipid remodeling** (unsaturation/branching; homeoviscous adaptation) as a core mechanistic axis linking HHP to growth capability and cellular integrity. (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 2-4)
2. **Stress-proteostasis circuitry** (heat shock regulon; chaperones and sigma factors) as an inducible response to pressure shocks and potentially a target of adaptation. (coffin2024responseandadaptation pages 1-2)
3. **Energy metabolism / respiration remodeling** (pressure-conditional respiratory components; alternative electron acceptors) as a second mechanistic axis enabling growth under pressure. (scheffer2023themysteryof pages 7-9)
4. **Compatible-solute (“piezolyte”) accumulation** as a chemical mechanism supporting macromolecular stability via preferential hydration. (scheffer2023themysteryof pages 9-10)

**Interpretation for curation:** The above hubs form a plausible multi-branch causal graph where HHP perturbs membrane/protein systems, triggering lipid remodeling + stress regulons + solute shifts, while respiration remodeling maintains bioenergetics—together enabling growth under elevated pressure. However, directionality and universality vary by lineage and co-stress (temperature), so edges should often be annotated as taxon-conditional or “uncertain.” (tamby2023microbialmembranelipid pages 1-2, scheffer2023themysteryof pages 9-10)

---

### 8) Curation warnings (claims not yet safe for TraitMech without qualifiers)

1. **Pressure vs temperature confounding:** The pfa operon is linked to ω‑3 PUFA increases under HHP, but the source explicitly notes uncertainty whether it responds to high pressure or low temperature; curate with an uncertainty tag or include temperature as a parent causal node. (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 1-2)

2. **Taxon-specific edges:** Respiratory chain remodeling (e.g., cytochrome c‑551/quinol oxidase) and specific desaturases are demonstrated/mentioned in particular genera; curate as lineage-specific unless validated across taxa. (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7)

3. **Food HPP “barotolerance” ≠ piezotolerance:** HPP literature often addresses survival/inactivation and post-treatment recovery, not growth preference. These edges are useful as an adjacent “pressure injury/repair” subgraph, but should not be conflated with the METPO definition of piezotolerant growth. (wisniewski2023impactofhighpressure pages 1-2, shymialevich2024thenovelconcept pages 4-5)

4. **Inferred causality:** Some mechanistic statements (e.g., OmpH upregulation maintaining transport under pressure) are plausible but partly interpretive; treat as inferred unless a source directly links the protein to a functional outcome. (scheffer2023themysteryof pages 7-9)

---

## DOI-first bibliography (2023–2024 prioritized; publication dates and URLs)

1. **Coffin CH, Fisher LA, Crippen S, et al.** (Nov **2024**). *Response and adaptation of the transcriptional heat shock response to pressure.* **Frontiers in Microbiology**. DOI: **10.3389/fmicb.2024.1470617**. URL: https://doi.org/10.3389/fmicb.2024.1470617 (coffin2024responseandadaptation pages 1-2)

2. **Malas J, Russo DC, Bollengier O, et al.** (Feb **2024**). *Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds.* **Frontiers in Microbiology**. DOI: **10.3389/fmicb.2024.1293928**. URL: https://doi.org/10.3389/fmicb.2024.1293928 (malas2024biologicalfunctionsat pages 1-2)

3. **Shymialevich D, Wójcicki M, Sokołowska B.** (Aug **2024**). *The Novel Concept of Synergically Combining: High Hydrostatic Pressure and Lytic Bacteriophages to Eliminate Vegetative and Spore-Forming Bacteria in Food Products.* **Foods**. DOI: **10.3390/foods13162519**. URL: https://doi.org/10.3390/foods13162519 (shymialevich2024thenovelconcept pages 2-4, shymialevich2024thenovelconcept pages 5-7, shymialevich2024thenovelconcept pages 7-8, shymialevich2024thenovelconcept pages 1-2)

4. **Wiśniewski P, Chajęcka-Wierzchowska W, Zadernowska A.** (Dec **2023**). *Impact of High-Pressure Processing (HPP) on Listeria monocytogenes—An Overview of Challenges and Responses.* **Foods**. DOI: **10.3390/foods13010014**. URL: https://doi.org/10.3390/foods13010014 (wisniewski2023impactofhighpressure pages 1-2, wisniewski2023impactofhighpressure pages 6-7)

5. **Scheffer G, Gieg LM.** (Jun **2023**). *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface.* **Microorganisms**. DOI: **10.3390/microorganisms11071629**. URL: https://doi.org/10.3390/microorganisms11071629 (scheffer2023themysteryof pages 6-7, scheffer2023themysteryof pages 9-10, scheffer2023themysteryof pages 7-9)

6. **Munir MT, Mtimet N, Guillier L, et al.** (Apr **2023**). *Physical Treatments to Control Clostridium botulinum Hazards in Food.* **Foods**. DOI: **10.3390/foods12081580**. URL: https://doi.org/10.3390/foods12081580 (munir2023physicaltreatmentsto pages 12-14)

7. **Tamby A, Sinninghe Damsté JS, Villanueva L.** (Jan **2023**; Frontiers article DOI year lists 2022). *Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment.* **Frontiers in Molecular Biosciences**. DOI: **10.3389/fmolb.2022.1058381**. URL: https://doi.org/10.3389/fmolb.2022.1058381 (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid media 3c77da24)

---

### Notes on deliverables for TraitMech curation
The artifact table provides a ready set of candidate edges (with uncertainty annotations) suitable for initial population of `data/traits/environment/piezotolerant.yaml`, with recommended separation of a *growth-preference* subgraph from a *food-HPP injury/recovery* subgraph to maintain phenotype clarity. (tamby2023microbialmembranelipid pages 1-2, wisniewski2023impactofhighpressure pages 1-2)

References

1. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

2. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

3. (coffin2024responseandadaptation pages 1-2): Carleton H. Coffin, Luke A. Fisher, Sara Crippen, Phoebe Demers, Douglas H. Bartlett, and Catherine A. Royer. Response and adaptation of the transcriptional heat shock response to pressure. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1470617, doi:10.3389/fmicb.2024.1470617. This article has 1 citations and is from a peer-reviewed journal.

4. (wisniewski2023impactofhighpressure pages 1-2): Patryk Wiśniewski, Wioleta Chajęcka-Wierzchowska, and Anna Zadernowska. Impact of high-pressure processing (hpp) on listeria monocytogenes—an overview of challenges and responses. Foods, 13:14, Dec 2023. URL: https://doi.org/10.3390/foods13010014, doi:10.3390/foods13010014. This article has 29 citations.

5. (shymialevich2024thenovelconcept pages 4-5): Dziyana Shymialevich, Michał Wójcicki, and Barbara Sokołowska. The novel concept of synergically combining: high hydrostatic pressure and lytic bacteriophages to eliminate vegetative and spore-forming bacteria in food products. Foods, 13:2519, Aug 2024. URL: https://doi.org/10.3390/foods13162519, doi:10.3390/foods13162519. This article has 18 citations.

6. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

7. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

8. (tamby2023microbialmembranelipid pages 2-4): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

9. (tamby2023microbialmembranelipid media 3c77da24): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

10. (shymialevich2024thenovelconcept pages 5-7): Dziyana Shymialevich, Michał Wójcicki, and Barbara Sokołowska. The novel concept of synergically combining: high hydrostatic pressure and lytic bacteriophages to eliminate vegetative and spore-forming bacteria in food products. Foods, 13:2519, Aug 2024. URL: https://doi.org/10.3390/foods13162519, doi:10.3390/foods13162519. This article has 18 citations.

11. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

12. (shymialevich2024thenovelconcept pages 2-4): Dziyana Shymialevich, Michał Wójcicki, and Barbara Sokołowska. The novel concept of synergically combining: high hydrostatic pressure and lytic bacteriophages to eliminate vegetative and spore-forming bacteria in food products. Foods, 13:2519, Aug 2024. URL: https://doi.org/10.3390/foods13162519, doi:10.3390/foods13162519. This article has 18 citations.

13. (wisniewski2023impactofhighpressure pages 6-7): Patryk Wiśniewski, Wioleta Chajęcka-Wierzchowska, and Anna Zadernowska. Impact of high-pressure processing (hpp) on listeria monocytogenes—an overview of challenges and responses. Foods, 13:14, Dec 2023. URL: https://doi.org/10.3390/foods13010014, doi:10.3390/foods13010014. This article has 29 citations.

14. (shymialevich2024thenovelconcept pages 7-8): Dziyana Shymialevich, Michał Wójcicki, and Barbara Sokołowska. The novel concept of synergically combining: high hydrostatic pressure and lytic bacteriophages to eliminate vegetative and spore-forming bacteria in food products. Foods, 13:2519, Aug 2024. URL: https://doi.org/10.3390/foods13162519, doi:10.3390/foods13162519. This article has 18 citations.

15. (tamby2023microbialmembranelipid media 7b9a160e): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

16. (shymialevich2024thenovelconcept pages 1-2): Dziyana Shymialevich, Michał Wójcicki, and Barbara Sokołowska. The novel concept of synergically combining: high hydrostatic pressure and lytic bacteriophages to eliminate vegetative and spore-forming bacteria in food products. Foods, 13:2519, Aug 2024. URL: https://doi.org/10.3390/foods13162519, doi:10.3390/foods13162519. This article has 18 citations.

17. (munir2023physicaltreatmentsto pages 12-14): Muhammad Tanveer Munir, Narjes Mtimet, Laurent Guillier, François Meurens, Phillipe Fravalo, Michel Federighi, and Pauline Kooh. Physical treatments to control clostridium botulinum hazards in food. Foods, 12:1580, Apr 2023. URL: https://doi.org/10.3390/foods12081580, doi:10.3390/foods12081580. This article has 56 citations.