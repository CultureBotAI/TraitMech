---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:45:22.896395'
end_time: '2026-06-17T21:11:36.353480'
duration_seconds: 1573.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: predatory bacterium
  trait_identifier: traitmech:000054
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: predatory_bacterium
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic-ecology lifestyle in which a bacterium actively kills and
    consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio
    bacteriovorus.
  parent_traits: METPO:1000059
  synonyms: bacterial predator
  evidence_summary: "DOI:10.1146/annurev.micro.091208.073346:  (Sockett, \"Predatory\
    \ lifestyle of Bdellovibrio bacteriovorus\", describes invasion, killing, and\
    \ digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:\
    \  (P\xE9rez et al. survey predatory bacteria, their hunting strategies, prey\
    \ ranges, and genome characteristics.)"
  causal_graph_summary: 'predatory_bacterium_prey_killing: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** predatory bacterium
- **METPO identifier:** traitmech:000054
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus.
- **Parent traits:** METPO:1000059
- **Synonyms:** bacterial predator
- **Existing evidence:** DOI:10.1146/annurev.micro.091208.073346:  (Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", describes invasion, killing, and digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:  (Pérez et al. survey predatory bacteria, their hunting strategies, prey ranges, and genome characteristics.)
- **Existing causal graph summary:** predatory_bacterium_prey_killing: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **predatory bacterium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/predatory_bacterium.yaml`.

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
- **Trait label:** predatory bacterium
- **METPO identifier:** traitmech:000054
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus.
- **Parent traits:** METPO:1000059
- **Synonyms:** bacterial predator
- **Existing evidence:** DOI:10.1146/annurev.micro.091208.073346:  (Sockett, "Predatory lifestyle of Bdellovibrio bacteriovorus", describes invasion, killing, and digestion of prey bacteria as a predatory lifestyle.) | DOI:10.1111/1462-2920.13171:  (Pérez et al. survey predatory bacteria, their hunting strategies, prey ranges, and genome characteristics.)
- **Existing causal graph summary:** predatory_bacterium_prey_killing: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **predatory bacterium** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/predatory_bacterium.yaml`.

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


## Microbial Trait Causal Graph Research Report: **Predatory bacterium** (TraitMech: traitmech:000054)

**Target trait definition (provided):** A trophic-ecology lifestyle in which a bacterium actively kills and consumes other bacteria for nutrients (e.g., *Bdellovibrio bacteriovorus*). This report focuses on mechanistic entities and evidence-backed causal edges suitable for curation into `data/traits/ecology/predatory_bacterium.yaml`.

### Executive scope summary (TraitMech curation view)
Predatory bacteria are best treated as an **interaction-defined trophic lifestyle**: bacteria that *actively hunt/attack, kill living bacterial cells, and consume their macromolecules for energy and biosynthesis*—distinguishing them from non-lethal host associations such as commensalism and many forms of parasitism. (perez2016bacterialpredation75 pages 1-2)

A practical curation scope is to represent **multiple predation modes** that share the core “kills-and-consumes bacteria” outcome but differ in mechanism and required structures:

1. **Endobiotic/periplasmic predators** (canonical BALOs such as *Bdellovibrio bacteriovorus*): predator **attaches**, **invades prey periplasm**, converts prey into a **bdelloplast**, grows/replicates inside, and **exits by lysing prey**. (kaplan2023bdellovibriopredationcycle pages 1-3)
2. **Epibiotic predators** (e.g., *Bdellovibrio exovorus*, *Micavibrio*): predator **remains external**, attaches to prey surface, forms feeding structures/pores/junctions, and **consumes prey from outside**. (perez2016bacterialpredation75 pages 2-4, santin2024lifecycleofa pages 1-4)
3. **Social/group-attack extracellular predators** (e.g., many myxobacteria): predation is often **density-dependent** and uses **secreted enzymes/secondary metabolites** and contact-dependent systems; predators remain outside prey while killing and digesting externally. (perez2016bacterialpredation75 pages 2-4, alexakis2024predatorybacteriain pages 1-2)

**Boundary cases important for TraitMech:**
- **Not absolute categories:** the same taxon may display mixed strategies depending on prey, environment, or predator:prey ratio; thus “predatory bacterium” should not be restricted to one mechanistic archetype. (perez2016bacterialpredation75 pages 1-2)
- **Obligate vs facultative predation:** some predators can grow axenically (opportunistic/social predators; some facultative predators), while others are classically prey-dependent; however, recent work shows genetic routes can relax prey dependence in BALOs (see flagellar stator / host-independent variants). (wang2024thepredatoryproperties pages 1-2, mookherjee2024flagellarstatorgenes pages 13-15)

---

## 1) Key concepts & definitions (current understanding)

### 1.1 What the trait represents
For TraitMech purposes, **predatory bacterium** can be operationalized as:
- A **physiological and behavioral capacity** enabling detection/attachment to bacterial prey, delivery of lethal damage (invasion-based or external), and assimilation of prey-derived nutrients supporting growth/energy. (perez2016bacterialpredation75 pages 1-2, kaplan2023bdellovibriopredationcycle pages 1-3)

### 1.2 Minimal trait criteria (curation guideline)
Evidence suggests the trait should require **at least two components**:
1) **Prey killing/damage** (demonstrable reduction in prey viability or lysis) and
2) **Nutrient acquisition** (growth/energy generation from prey or prey-derived substrates).

Periplasmic predators meet both via bdelloplast growth and prey consumption. (kaplan2023bdellovibriopredationcycle pages 1-3)

### 1.3 Distinguishing from nearby traits
- **Antagonism/competition without consumption** (e.g., antibiotic production to inhibit neighbors) is not necessarily predation unless tied to killing followed by consumption. (perez2016bacterialpredation75 pages 1-2)
- **Parasites/epibionts** that depend on a host but do not kill are outside scope, though the boundary can be nuanced across taxa and assays. (perez2016bacterialpredation75 pages 1-2)

---

## 2) Recent developments (prioritize 2023–2024)

### 2.1 Nanometer-scale structural biology of periplasmic predation (2023)
Cryo-electron tomography has resolved key physical structures of the *Bdellovibrio* invasion cycle, including:
- **Type IVa pili (T4aP)** contacting prey outer membrane, and basal bodies aligned at contact sites. (kaplan2023bdellovibriopredationcycle pages 3-4)
- A **flexible “portal”** that lines the prey peptidoglycan opening during entry and is associated with the entry process. (kaplan2023bdellovibriopredationcycle pages 3-4)
- **Bdelloplast anatomy**: a sealed entry scar and predator morphological transitions inside prey. (kaplan2023bdellovibriopredationcycle pages 6-7)

Key supporting figure panels are available from this work (T4P attachment; portal; bdelloplast seal/division). (kaplan2023bdellovibriopredationcycle media 473bcfba, kaplan2023bdellovibriopredationcycle media 732758e8, kaplan2023bdellovibriopredationcycle media 544a69cf)

### 2.2 Expanded molecular basis of prey recognition: MAT adhesins and invasion organelle (2024)
A 2024 *Nature Microbiology* study identified a prey-invasion system centered on:
- **CpoB (Bd0635)** concentrating into a **vesicular invasion compartment deposited into prey periplasm** during invasion. (caulton2024bdellovibriobacteriovorususes pages 1-2)
- A **MAT (mosaic adhesive trimer) superfamily** of fiber-like adhesins that localize on the predator surface pre-contact and provide a diversified repertoire for recognizing prey epitopes (including glycan binding specificity in at least one MAT). (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 8-9)

### 2.3 Prey killing without successful invasion: MIDAS-family adhesin Bd0875 (2024)
A 2024 *Nature Communications* paper provides a mechanistically important boundary case:
- **Bd0875 (MIDAS-family adhesin)** is important for successful invasion; deletion yields ~10% bdelloplasts lacking an internalized predator. (tyson2024preykillingwithout pages 1-2)
- Nonetheless, prey can be killed even when invasion is abortive, consistent with **predator protein secretion into prey being sufficient for killing** in some contexts. (tyson2024preykillingwithout pages 1-2)

### 2.4 Epibiotic predation lifecycle and S-layer non-protection (2024)
Live imaging/cryo-EM of epibiotic predator *Bdellovibrio exovorus* showed:
- A **non-binary division pattern** producing mainly **three progeny**.
- Predation **occurs regardless of prey S-layer presence**, challenging the idea that S-layers provide generalized protection.
- Epibiotic feeding depends on a **secured predator–prey outer-membrane junction** that must be resolved to maintain predator integrity at departure.
(santin2024lifecycleofa pages 1-4)

### 2.5 Prey escape/anti-predation factors emphasized by 2024 synthesis
A 2024 review highlights chemical/ecological prey defenses modulating predation efficacy, including:
- Quorum/diffusible factors such as **DSF (50 μM)** reducing predator motility and slowing predation.
- **Indole** delaying intraperiplasmic growth and bdelloplast lysis/release.
- Pseudomonad quinolone signals (**HHQ/PQS/HQNO**) reducing predation, with HQNO potentially strongly lowering predator viability.
- **Increased viscosity** (e.g., Ficoll/methylcellulose) reducing invasion/attachment by increasing drag.
- Prey motility determinants (e.g., **motY** in *V. cholerae*) affecting susceptibility.
(das2024howdogramnegative pages 3-4, das2024howdogramnegative pages 4-6)

---

## 3) Candidate causal-graph nodes (grouped by type)

### 3.1 Processes / lifecycle stages (GO candidates)
- Attack-phase swimming (flagellum-driven motility) (kaplan2023bdellovibriopredationcycle pages 1-3)
- Prey attachment (T4P-mediated) (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 3-4)
- Prey envelope penetration / invasion
- Portal formation and entry pore sealing (bdelloplast formation) (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 3-4)
- Intraperiplasmic growth / synchronous septation (periplasmic predators) (kaplan2023bdellovibriopredationcycle pages 1-3)
- Prey lysis and predator exit (kaplan2023bdellovibriopredationcycle pages 1-3)
- Epibiotic junction formation and external feeding (santin2024lifecycleofa pages 1-4)

### 3.2 Cellular structures / localizations
- Sheathed unipolar flagellum (predator) (kaplan2023bdellovibriopredationcycle pages 1-3)
- Type IVa pili apparatus (T4aP) (kaplan2023bdellovibriopredationcycle pages 3-4)
- Invasion “portal” / attachment plaque (structural entity, label-only) (kaplan2023bdellovibriopredationcycle pages 3-4)
- Bdelloplast (modified prey envelope compartment) (kaplan2023bdellovibriopredationcycle pages 1-3)
- Outer membrane (predator and prey), prey peptidoglycan (kaplan2023bdellovibriopredationcycle pages 3-4)

### 3.3 Genes / proteins (examples with strongest evidence in retrieved sources)
**Prey recognition / adhesion:**
- CpoB / Bd0635 (invasion vesicle organelle) (caulton2024bdellovibriobacteriovorususes pages 1-2)
- MAT superfamily adhesins (mosaic adhesive trimer proteins) (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 8-9)
- Bd0875 MIDAS-family adhesin (invasion success; killing without invasion context) (tyson2024preykillingwithout pages 1-2)

**Prey escape (prey-side factors):**
- motY (prey motility determinant; *V. cholerae*) (das2024howdogramnegative pages 3-4)
- Serratia secreted proteases/serralysins (attachment interference; review synthesis) (das2024howdogramnegative pages 4-6)

**Engineering tools (application nodes; not native mechanisms):**
- Tn7 integration at attTn7, Golden Standard (GS) toolkit (salgado2024controllingtheexpression pages 1-2, salgado2024controllingtheexpression pages 12-14)
- Promoters PJExD/EliR, PBG37 (salgado2024controllingtheexpression pages 1-2, salgado2024controllingtheexpression pages 12-14)

### 3.4 Chemicals / environmental & experimental factors
- Diffusible signaling factor (DSF) 50 μM (das2024howdogramnegative pages 3-4, das2024howdogramnegative pages 3-3)
- Indole (das2024howdogramnegative pages 3-4)
- HHQ/PQS/HQNO quinolone signals (das2024howdogramnegative pages 3-4)
- Increased viscosity (Ficoll/methylcellulose; concept) (das2024howdogramnegative pages 3-4)
- pH and temperature ranges affecting predator viability (pH 5–9 tolerated; 4°C and 29°C best survival; 60°C lethal for isolates studied) (mohsenipour2024predationonbacterial pages 1-2, mohsenipour2024predationonbacterial pages 6-8)

### 3.5 Nutrients / metabolites (host-independent growth boundary)
- Amino-acid-rich media (PYE10) (herencias2024bdellovibrio’spreyindependentlifestyle pages 4-5)
- Defined amino-acid medium (CAV) (herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7)
- Preferred amino acids (glutamate, serine, aspartate, isoleucine, threonine) (herencias2024bdellovibrio’spreyindependentlifestyle pages 1-2, herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7)

---

## 4) Candidate causal edges (evidence-backed)
The following table is designed for direct curation into a TraitMech causal graph as subject–predicate–object triples, with uncertainty notes.

| Subject node (label + CURIE) | Predicate (causal) | Object node (label + CURIE) | Evidence snippet | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Sheathed unipolar flagellum (GO:0009288 candidate) | enables | high-velocity attack-phase swimming / prey collisions (label-only) | “attack-phase” *Bdellovibrio* bears a sheathed unipolar flagellum used for high-velocity collisions before attachment (kaplan2023bdellovibriopredationcycle pages 1-3) | 10.1038/s41564-023-01401-2, 2023, https://doi.org/10.1038/s41564-023-01401-2 | Strong for *B. bacteriovorus*; taxon-specific to periplasmic BALOs |
| Type IV pili / T4aP (GO:0009289 candidate) | mediates attachment to | prey outer membrane (GO:0019867 candidate) | Cryo-ET shows T4P tips contacting prey OM; attachment is described as mediated by type IV pili (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 3-4) | 10.1038/s41564-023-01401-2, 2023, https://doi.org/10.1038/s41564-023-01401-2 | Strong for *B. bacteriovorus*; likely not universal across all predators |
| Prey attachment / invasion complex (“portal”, label-only) | seals | prey peptidoglycan entry hole / bdelloplast pore (GO:0009274 candidate) | A “flexible portal” lines the hole during entry and the “entry pore is sealed” to form a bdelloplast (kaplan2023bdellovibriopredationcycle pages 1-3, kaplan2023bdellovibriopredationcycle pages 3-4) | 10.1038/s41564-023-01401-2, 2023, https://doi.org/10.1038/s41564-023-01401-2 | Structural feature well supported; molecular composition still incomplete |
| Prey-cell-wall modification enzymes (label-only) | causes | bdelloplast formation (label-only) | During invasion, the predator “modifies the prey cell wall,” rounding the killed prey into a bdelloplast (tyson2024preykillingwithout pages 1-2) | 10.1038/s41467-024-47412-3, 2024, https://doi.org/10.1038/s41467-024-47412-3 | Mechanism supported; exact enzyme set broader than one curated edge |
| Bdelloplast (label-only) | provides environment for | intraperiplasmic growth / predator replication (GO:0044409 candidate) | The sealed bdelloplast contains a live predator that grows and replicates inside the prey periplasm (kaplan2023bdellovibriopredationcycle pages 1-3, tyson2024preykillingwithout pages 1-2) | 10.1038/s41564-023-01401-2, 2023, https://doi.org/10.1038/s41564-023-01401-2 | Canonical for periplasmic/endobiotic predation only |
| Exit-associated lytic activity (label-only) | causes | prey cell wall lysis and progeny release (GO:0044409 candidate) | After synchronous septation, progeny “lyse the prey cell wall and exit” (kaplan2023bdellovibriopredationcycle pages 1-3) | 10.1038/s41564-023-01401-2, 2023, https://doi.org/10.1038/s41564-023-01401-2 | Generic edge; specific exit proteins not fully pinned down here |
| CpoB / Bd0635 (label-only) | localizes to / forms | invasion vesicular compartment in prey periplasm (label-only) | CpoB “concentrates into a vesicular compartment that is deposited into the prey periplasm during invasion” (caulton2024bdellovibriobacteriovorususes pages 1-2) | 10.1038/s41564-023-01552-2, 2024, https://doi.org/10.1038/s41564-023-01552-2 | Strong, but deletion evidence suggests possible essentiality rather than direct sufficiency |
| MAT adhesin repertoire (mosaic adhesive trimer proteins; label-only) | enables recognition of | diverse prey surface epitopes / glycans (CHEBI:16670 candidate for glycans) | MAT proteins form a “broad means for the recognition and handling of diverse prey epitopes”; one member binds specific prey glycans (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 8-9) | 10.1038/s41564-023-01552-2, 2024, https://doi.org/10.1038/s41564-023-01552-2 | Strong for prey recognition; breadth likely strain-specific |
| MAT proteins (label-only) | localize before contact to | predator surface / poles (GO:0009276 candidate) | MATs are present on the attack-phase predator surface and dynamically localize to poles or midcell before invasion (caulton2024bdellovibriobacteriovorususes pages 1-2, caulton2024bdellovibriobacteriovorususes pages 8-9) | 10.1038/s41564-023-01552-2, 2024, https://doi.org/10.1038/s41564-023-01552-2 | Localization strong; exact anchoring partners still inferred |
| Bd0875 MIDAS-family adhesin (label-only) | promotes | successful prey invasion (GO:0044409 candidate) | Bd0875 is “important for successful invasion”; Δbd0875 yields ~10% round dead bdelloplasts lacking an internalized predator (tyson2024preykillingwithout pages 1-2) | 10.1038/s41467-024-47412-3, 2024, https://doi.org/10.1038/s41467-024-47412-3 | Strong but not absolutely required because of adhesin redundancy |
| Conserved MIDAS motif in Bd0875 (label-only) | is required for | Bd0875 adhesin activity (GO:0005515 candidate) | The paper states Bd0875 activity requires the conserved MIDAS motif, linked to catch-bond-like adhesive behavior (tyson2024preykillingwithout pages 1-2) | 10.1038/s41467-024-47412-3, 2024, https://doi.org/10.1038/s41467-024-47412-3 | Specific to Bd0875 and mechanistically inferred from motif-function studies |
| Abortive invasion protein secretion (label-only) | is sufficient for | prey killing without invasion (label-only) | Uninvaded bdelloplasts still contain predator proteins, indicating secreted proteins can kill prey even without a live intraperiplasmic predator (tyson2024preykillingwithout pages 1-2) | 10.1038/s41467-024-47412-3, 2024, https://doi.org/10.1038/s41467-024-47412-3 | Strong but specific to Δbd0875 context; should be marked conditional |
| Secured predator–prey OM junction (label-only) | enables | epibiotic feeding by *Bdellovibrio exovorus* (label-only) | Epibiotic predation “relies on the establishment of a secured junction between the prey and predator outer membranes” (santin2024lifecycleofa pages 1-4) | 10.1101/2023.10.25.563945, 2024, https://doi.org/10.1101/2023.10.25.563945 | Strong for *B. exovorus*; preprint DOI/versioning noted |
| Prey S-layer / RsaA (label-only) | does not prevent | *Bdellovibrio exovorus* predation (label-only) | Predation occurred “regardless of the presence of an S-layer,” challenging its proposed protective role (santin2024lifecycleofa pages 1-4) | 10.1101/2023.10.25.563945, 2024, https://doi.org/10.1101/2023.10.25.563945 | Negative causal edge; specific to *Caulobacter crescentus* prey and *B. exovorus* |
| DSF quorum-sensing molecule (CHEBI candidate; label-only) | reduces | predator motility / predation efficiency (GO:0040011 candidate) | Exogenous DSF at 50 μM slowed predation and reduced predatory-cell motility by about 50% (das2024howdogramnegative pages 3-4, das2024howdogramnegative pages 3-3) | 10.1038/s44259-024-00048-1, 2024, https://doi.org/10.1038/s44259-024-00048-1 | Review-level synthesis; underlying primary data should be checked before high-confidence curation |
| Indole (CHEBI:16881) | delays | intraperiplasmic growth and bdelloplast lysis / predator release (label-only) | Indole is described as delaying intraperiplasmic growth, bdelloplast lysis and predator release (das2024howdogramnegative pages 3-4) | 10.1038/s44259-024-00048-1, 2024, https://doi.org/10.1038/s44259-024-00048-1 | Review synthesis; likely prey/context dependent |
| HHQ / PQS / HQNO quinolone signals (CHEBI candidates; label-only) | reduce | *Bdellovibrio* viability and predation (label-only) | Pseudomonad quinolone signals reduce predation; HQNO can be directly bactericidal and lower predator viability by orders of magnitude (das2024howdogramnegative pages 3-4) | 10.1038/s44259-024-00048-1, 2024, https://doi.org/10.1038/s44259-024-00048-1 | Strong conceptually, but pooled from review and multiple prey systems |
| Increased medium viscosity / Ficoll or methylcellulose (ENVO:01000324 candidate for viscous medium) | reduces | predator attachment/invasion success (label-only) | Higher viscosity increases drag on attached predators, improving survival of motile prey and reducing predator invasions (das2024howdogramnegative pages 3-4) | 10.1038/s44259-024-00048-1, 2024, https://doi.org/10.1038/s44259-024-00048-1 | Assay-specific environmental factor; likely important for liquid systems |
| Prey motility determinant MotY (label-only) | increases resistance to | *Bdellovibrio* predation (label-only) | In *Vibrio cholerae*, non-motile motY mutants were more susceptible, linking prey motility to escape (das2024howdogramnegative pages 3-4) | 10.1038/s44259-024-00048-1, 2024, https://doi.org/10.1038/s44259-024-00048-1 | Review summary; gene-level edge is prey-taxon specific |
| Serratia secreted proteases / serralysins (label-only) | reduce | predator attachment to prey (label-only) | *Serratia marcescens* proteases reduce attachment; deletion mutants become more susceptible and purified metalloprotease can block predation (das2024howdogramnegative pages 4-6) | 10.1038/s44259-024-00048-1, 2024, https://doi.org/10.1038/s44259-024-00048-1 | Review summary; exact protease identities vary across studies |
| Amino-acid-rich medium PYE10 (label-only) | supports | host-independent biomass increase and ATP generation (GO:0006091 candidate) | In prey-free PYE10, biomass rose and intracellular ATP increased up to ~5-fold while genome copy number also increased (herencias2024bdellovibrio’spreyindependentlifestyle pages 7-10, herencias2024bdellovibrio’spreyindependentlifestyle pages 4-5) | 10.1007/s00253-024-13250-y, 2024, https://doi.org/10.1007/s00253-024-13250-y | Strong for host-independent strains/conditions tested; not equivalent to full natural predation |
| Defined amino acid medium CAV (label-only) | supports | active host-independent metabolism (label-only) | A defined amino-acid-only CAV medium sustained active metabolism and significant biomass increase by 48 h (herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7, herencias2024bdellovibrio’spreyindependentlifestyle pages 10-10) | 10.1007/s00253-024-13250-y, 2024, https://doi.org/10.1007/s00253-024-13250-y | Strong for axenic physiology; replication remained limited in some assays |
| Preferred amino acids: glutamate, serine, aspartate, isoleucine, threonine (CHEBI candidates) | fuel | prey-independent carbon metabolism (GO:0015976 candidate) | These amino acids were significantly depleted and identified as the main carbon sources during axenic growth (herencias2024bdellovibrio’spreyindependentlifestyle pages 1-2, herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7) | 10.1007/s00253-024-13250-y, 2024, https://doi.org/10.1007/s00253-024-13250-y | Strong but based partly on modeling + depletion data |
| Host-independent amino-acid growth state (label-only) | preserves | predatory killing capacity (label-only) | After axenic growth in amino-acid media, *Bdellovibrio* retained effective prey killing against *Pseudomonas putida* (herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7, herencias2024bdellovibrio’spreyindependentlifestyle pages 7-10) | 10.1007/s00253-024-13250-y, 2024, https://doi.org/10.1007/s00253-024-13250-y | Useful boundary case: prey-independent growth does not abolish predation |
| Bdellovibrio sp. YBD-1 (NCBITaxon candidate) | reduces | *E. coli* biofilm formation and virulence/biofilm gene expression (label-only) | YBD-1 significantly reduced planktonic cells and biofilms; SEM and qRT-PCR showed lower *fim*, *iroN* and *pgaABC* expression after 48 h (xi2024evaluationofthe pages 10-11) | 10.1038/s41598-024-63418-9, 2024, https://doi.org/10.1038/s41598-024-63418-9 | Application-oriented, strain-specific; mechanism of transcriptional reduction indirect |
| Sewage-derived *Bdellovibrio* isolates A/C/G (NCBITaxon candidate) | inhibit | Gram-negative pathogens (label-only) | Reported 3 h CFU reductions include 70.48% for *Salmonella enterica*, 60.42% for *E. coli*, and lower activity on some Gram-positives (mohsenipour2024predationonbacterial pages 1-2, mohsenipour2024predationonbacterial pages 6-8, mohsenipour2024predationonbacterial pages 8-10) | 10.1186/s12866-024-03672-z, 2024, https://doi.org/10.1186/s12866-024-03672-z | Applied phenotype under assay conditions; broad but isolate-specific |
| Bdellovibrio abundance in amended soil (label-only) | correlates with | ARG profile shifts: tetA(+), vanA(+), tetM(−) (label-only) | Soil ddPCR showed Bdellovibrio abundance positively associated with tetA and vanA, negatively with tetM; Bdellovibrio was 1–2 orders more abundant than Bacteriovorax (rosberg2024regulationofantibiotic pages 7-9, rosberg2024regulationofantibiotic pages 3-7) | 10.3390/antibiotics13080750, 2024, https://doi.org/10.3390/antibiotics13080750 | Correlative only; not yet suitable as a direct mechanistic causal edge without caution |
| Tn7 chromosomal integration + GS toolkit (label-only) | enables | stable heterologous gene expression in *Bdellovibrio bacteriovorus* (label-only) | Tn7 insertion at attTn7 was stable for ≥10 generations and did not impair predation; Golden Standard enabled rapid construct assembly (salgado2024controllingtheexpression pages 1-2, salgado2024controllingtheexpression pages 12-14, salgado2024controllingtheexpression pages 7-8) | 10.1111/1751-7915.14517, 2024, https://doi.org/10.1111/1751-7915.14517 | Engineering-enabler edge rather than natural trait mechanism |
| PJExD/EliR inducible system / PBG37 constitutive promoter (label-only) | enables | precise or high constitutive expression in engineered *Bdellovibrio* (label-only) | PJExD/EliR showed tight control with low background; PBG37 yielded high constitutive expression in *Bdellovibrio* (salgado2024controllingtheexpression pages 1-2, salgado2024controllingtheexpression pages 12-14, salgado2024controllingtheexpression pages 14-15) | 10.1111/1751-7915.14517, 2024, https://doi.org/10.1111/1751-7915.14517 | Application/synthetic biology only; not a native predation edge |
| Predatory bacterium lifestyle (METPO:traitmech:000054) | includes mode | epibiotic, endobiotic/periplasmic, and social/group-attack predation (label-only) | Reviews classify predators into epibiotic, endobiotic/periplasmic, and social/extracellular modes, with obligate vs facultative/opportunistic boundary cases (perez2016bacterialpredation75 pages 1-2, perez2016bacterialpredation75 pages 2-4, alexakis2024predatorybacteriain pages 1-2, santin2024lifecycleofa pages 1-4) | 10.1111/1462-2920.13171, 2016, https://doi.org/10.1111/1462-2920.13171 | Scope edge for ontology framing; not a mechanistic molecular edge |


*Table: This table lists candidate causal edges for the TraitMech trait 'predatory bacterium', spanning core Bdellovibrio invasion stages, adhesins, epibiotic predation, prey escape mechanisms, prey-independent metabolism, and applied/engineering contexts. It is designed to help prioritize which relationships are strong enough for curation versus which remain taxon-specific, correlative, or assay-dependent.*

**Visual support for core invasion-stage nodes:** cryo-ET figure panels showing T4P-mediated attachment, portal/entry, and bdelloplast seal/division are available for citation. (kaplan2023bdellovibriopredationcycle media 473bcfba, kaplan2023bdellovibriopredationcycle media 732758e8, kaplan2023bdellovibriopredationcycle media 544a69cf)

---

## 5) Current applications & real-world implementations (with recent data)

### 5.1 Pathogen inhibition and host-range performance (environmental isolates)
A 2024 study isolating sewage-derived predators reported **3-hour prey CFU reduction percentages** (predatory efficiency) against pathogens including:
- *Salmonella enterica*: up to **70.48%** reduction (isolate C).
- *E. coli*: up to **60.42%** reduction (isolate G).
- *P. aeruginosa*: as low as **3.84%** reduction (isolate C; isolate A higher).
- Gram-positive effects were limited or variable (e.g., *S. aureus* up to **29.83%** with isolate G).
(mohsenipour2024predationonbacterial pages 8-10)

This same study provides deployability-relevant stability data: isolates tolerated **pH 5–9**, were killed at **pH 2 and 12**, survived best at **4°C (92–95% survival by 24 h)** and **29°C (81–86% survival by 24 h)**, and were rapidly killed at **60°C**. (mohsenipour2024predationonbacterial pages 6-8)

### 5.2 Biofilm control and virulence-associated gene expression impacts
A 2024 *Scientific Reports* evaluation of a yak-feces isolate (*Bdellovibrio* sp. YBD-1) reported reduction of **planktonic cells and biofilms** of *E. coli*, accompanied by decreased expression of virulence genes (*fim*, *iroN*) and biofilm genes (*pgaABC*) after **48 h** exposure. (xi2024evaluationofthe pages 10-11)

### 5.3 Environmental microbiome roles: antibiotic resistome correlations (soil)
A 2024 soil incubation study using ddPCR quantified three ARGs (**tetA, tetM, vanA**) and predator taxa (**Bdellovibrio** and **Bacteriovorax**). It reported that Bdellovibrio abundance was **positively correlated with tetA and vanA and negatively correlated with tetM**, while Bacteriovorax showed no significant correlations in that dataset. (rosberg2024regulationofantibiotic pages 3-7, rosberg2024regulationofantibiotic pages 7-9)

**Curation caution:** these are correlations; mechanistic causality (e.g., predation reducing hosts that carry specific ARGs) is plausible but not directly demonstrated in the cited work. (rosberg2024regulationofantibiotic pages 3-7)

### 5.4 Engineering/implementation readiness: synthetic biology toolchains
For real-world deployment (biocontrol/therapeutic chassis concepts), 2024 work provides enabling infrastructure:
- **Tn7 chromosomal integration** at attTn7 is stable for at least **10 generations without selection** and does not impair predation.
- A modular cloning pipeline (Golden Standard/GS) and promoter panels allow constitutive and inducible heterologous expression (including **PJExD/EliR** and **PBG37**).
(salgado2024controllingtheexpression pages 12-14, salgado2024controllingtheexpression pages 1-2)

---

## 6) Expert opinions & analysis (authoritative sources)

### 6.1 Why predation is a useful trait abstraction (but must be mode-aware)
An authoritative synthesis emphasizes that “predatory bacteria” are broadly distributed, affect population structure and mortality, and display multiple strategies; classification is interaction-based and **not absolute**, so causal graphs should avoid over-committing to a single mechanism as the definition of the trait. (perez2016bacterialpredation75 pages 1-2)

### 6.2 Mechanistic convergences and divergences relevant to causal graphs
- **Convergence:** Many predator modes require (i) a prey-contact step and (ii) delivery of lethal envelope/cell-wall damage (via invasion complexes, junctions, secreted hydrolases, or contact-dependent systems). (kaplan2023bdellovibriopredationcycle pages 1-3, santin2024lifecycleofa pages 1-4)
- **Divergence:** Periplasmic predation depends on bdelloplast formation and internal growth; epibiotic predation relies on stable inter-membrane junctions and external consumption; social predators often require group density and extracellular enzyme pools. (perez2016bacterialpredation75 pages 2-4, santin2024lifecycleofa pages 1-4)

### 6.3 Boundary case insight (obligate vs facultative)
Host-independent growth supported by amino-acid media (PYE10/CAV) can preserve predatory killing capacity, indicating that “obligate” predation may be less absolute than traditionally framed and that **nutrient availability** can modulate trophic dependence. (herencias2024bdellovibrio’spreyindependentlifestyle pages 7-10, herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7)

---

## 7) Relevant statistics and quantitative data (recent studies)

### 7.1 Structural counts / quantitative morphology (cryo-ET)
Attack-phase *Bdellovibrio* frequently shows **~3–6 non-piliated T4aP basal bodies** per cell (n=171), and these structures are reduced/degraded in bdelloplast stages (n=72). (kaplan2023bdellovibriopredationcycle pages 6-7)

### 7.2 Predation efficacy / inhibition percentages (pathogens)
Prey CFU reduction (%) at 3 h by sewage-derived predators (examples):
- *S. enterica*: 61.53–70.48% (isolate A vs C)
- *E. coli*: 45.36–60.42%
- *P. aeruginosa*: 3.84–59.83% (strong isolate dependence)
(mohsenipour2024predationonbacterial pages 8-10)

### 7.3 Host-independent metabolism metrics (prey-free media)
In prey-free PYE10, *Bdellovibrio* showed:
- Viable counts decreasing by **1.32 log10** over 96 h (median log10 viable 9.28 → 7.97), while genome copy number rose by **0.5 log10**.
- Intracellular ATP increases reported up to **~5-fold** (2.5-fold normalized by biomass).
(herencias2024bdellovibrio’spreyindependentlifestyle pages 4-5, herencias2024bdellovibrio’spreyindependentlifestyle pages 7-10)

---

## 8) Ontology grounding suggestions (non-exhaustive)

**Trait:**
- Predatory bacterium — METPO: traitmech:000054 (given)

**Potential GO candidates (confirm exact GO IDs during curation):**
- Type IV pilus-dependent motility/assembly (GO candidates)
- Flagellum-dependent cell motility (GO:0001539 candidate)
- Peptidoglycan catabolic process (GO:0009253 candidate)
- Biofilm formation (GO:0042710 candidate)

**CHEBI candidates:**
- Indole — CHEBI:16881 (das2024howdogramnegative pages 3-4)
- DSF, HHQ/PQS/HQNO — label-only CHEBI candidates (confirm exact CHEBI mappings before curation) (das2024howdogramnegative pages 3-4)

**ENVO candidates:**
- Viscous medium / increased viscosity (label-only; confirm best ENVO match) (das2024howdogramnegative pages 3-4)

**NCBITaxon (examples):**
- *Bdellovibrio bacteriovorus* (NCBITaxon:959)
- *Bdellovibrio exovorus* (NCBITaxon; verify)

---

## 9) Warnings / “do not curate yet” items

1. **Review-synthesized prey-escape edges** (DSF/indole/HQNO/viscosity, Serratia proteases, motY) are mechanistically plausible but should be curated with **uncertainty tags** unless the primary experimental papers are also captured and quoted directly. (das2024howdogramnegative pages 3-4, das2024howdogramnegative pages 4-6)
2. **ARG shaping by predatory bacteria** is **correlative** in the retrieved soil study; causal edges “predation → ARG decrease” should be marked *uncertain* or deferred until direct predation/host linkage is experimentally shown. (rosberg2024regulationofantibiotic pages 3-7)
3. **Portal composition and many invasion effectors** are structurally evident but incompletely molecularly resolved in the evidence here; avoid over-specific protein assignments without direct support. (kaplan2023bdellovibriopredationcycle pages 3-4)

---

## DOI-first bibliography (with publication dates and URLs where available)

**Core mechanistic (recent):**
- Kaplan M. et al. *Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography.* **Nature Microbiology**. 2023-06. DOI: **10.1038/s41564-023-01401-2**. https://doi.org/10.1038/s41564-023-01401-2 (kaplan2023bdellovibriopredationcycle pages 1-3)
- Caulton S.G. et al. *Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts.* **Nature Microbiology**. 2024-01. DOI: **10.1038/s41564-023-01552-2**. https://doi.org/10.1038/s41564-023-01552-2 (caulton2024bdellovibriobacteriovorususes pages 1-2)
- Tyson J. et al. *Prey killing without invasion by Bdellovibrio bacteriovorus defective for a MIDAS-family adhesin.* **Nature Communications**. 2024-04. DOI: **10.1038/s41467-024-47412-3**. https://doi.org/10.1038/s41467-024-47412-3 (tyson2024preykillingwithout pages 1-2)
- Santin Y.G. et al. *Lifecycle of a predatory bacterium vampirizing its prey through the cell envelope and S-layer.* **Nature Communications** (posted as preprint DOI). 2024-10 (preprint posted 2023-10-25). DOI: **10.1101/2023.10.25.563945**. https://doi.org/10.1101/2023.10.25.563945 (santin2024lifecycleofa pages 1-4)

**Prey escape / ecology (recent):**
- Das S.K., Negus D. *How do Gram-negative bacteria escape predation by Bdellovibrio bacteriovorus?* **npj Antimicrobials and Resistance**. 2024-10. DOI: **10.1038/s44259-024-00048-1**. https://doi.org/10.1038/s44259-024-00048-1 (das2024howdogramnegative pages 3-4)

**Metabolism / boundary cases (recent):**
- Herencias C. et al. *Bdellovibrio’s prey-independent lifestyle is fueled by amino acids as a carbon source.* **Applied Microbiology and Biotechnology**. 2024-07. DOI: **10.1007/s00253-024-13250-y**. https://doi.org/10.1007/s00253-024-13250-y (herencias2024bdellovibrio’spreyindependentlifestyle pages 4-5)

**Applications / real-world performance (recent):**
- Mohsenipour Z. et al. *Predation on bacterial pathogens by predatory bacteria of sewage origin: three days prey-predator interactions.* **BMC Microbiology**. 2024-12. DOI: **10.1186/s12866-024-03672-z**. https://doi.org/10.1186/s12866-024-03672-z (mohsenipour2024predationonbacterial pages 8-10)
- Xi Y. et al. *Evaluation of the application potential of Bdellovibrio sp. YBD-1 isolated from Yak faeces.* **Scientific Reports**. 2024-06. DOI: **10.1038/s41598-024-63418-9**. https://doi.org/10.1038/s41598-024-63418-9 (xi2024evaluationofthe pages 10-11)
- Rosberg A.K. et al. *Regulation of Antibiotic Resistance Genes on Agricultural Land Is Dependent on Both Choice of Organic Amendment and Prevalence of Predatory Bacteria.* **Antibiotics**. 2024-08. DOI: **10.3390/antibiotics13080750**. https://doi.org/10.3390/antibiotics13080750 (rosberg2024regulationofantibiotic pages 3-7)

**Engineering enablers (recent):**
- Salgado S. et al. *Controlling the expression of heterologous genes in Bdellovibrio bacteriovorus using synthetic biology strategies.* **Microbial Biotechnology**. 2024-06. DOI: **10.1111/1751-7915.14517**. https://doi.org/10.1111/1751-7915.14517 (salgado2024controllingtheexpression pages 12-14)

**Foundational scope / classification (authoritative):**
- Pérez J. et al. *Bacterial predation: 75 years and counting!* **Environmental Microbiology**. 2016-03. DOI: **10.1111/1462-2920.13171**. https://doi.org/10.1111/1462-2920.13171 (perez2016bacterialpredation75 pages 2-4)

---

### Suggested next curation step (internal)
Start a `predatory_bacterium.yaml` with a small, high-confidence core module for **periplasmic predation** (T4P attachment → portal/entry pore sealing → bdelloplast growth → exit) and a separate module for **epibiotic predation** (secured OM junction; S-layer non-protection), then attach prey-escape and environmental modulation edges with explicit uncertainty flags until primary studies are added. (kaplan2023bdellovibriopredationcycle pages 3-4, santin2024lifecycleofa pages 1-4, das2024howdogramnegative pages 3-4)

References

1. (perez2016bacterialpredation75 pages 1-2): Juana Pérez, Aurelio Moraleda‐Muñoz, Francisco Javier Marcos‐Torres, and José Muñoz‐Dorado. Bacterial predation: 75 years and counting! Environmental microbiology, 18 3:766-79, Mar 2016. URL: https://doi.org/10.1111/1462-2920.13171, doi:10.1111/1462-2920.13171. This article has 316 citations and is from a domain leading peer-reviewed journal.

2. (kaplan2023bdellovibriopredationcycle pages 1-3): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

3. (perez2016bacterialpredation75 pages 2-4): Juana Pérez, Aurelio Moraleda‐Muñoz, Francisco Javier Marcos‐Torres, and José Muñoz‐Dorado. Bacterial predation: 75 years and counting! Environmental microbiology, 18 3:766-79, Mar 2016. URL: https://doi.org/10.1111/1462-2920.13171, doi:10.1111/1462-2920.13171. This article has 316 citations and is from a domain leading peer-reviewed journal.

4. (santin2024lifecycleofa pages 1-4): Yoann G. Santin, Adrià Sogues, Yvann Bourigault, Han K. Remaut, and Géraldine Laloux. Lifecycle of a predatory bacterium vampirizing its prey through the cell envelope and s-layer. Nature Communications, Oct 2024. URL: https://doi.org/10.1101/2023.10.25.563945, doi:10.1101/2023.10.25.563945. This article has 16 citations and is from a highest quality peer-reviewed journal.

5. (alexakis2024predatorybacteriain pages 1-2): Konstantinos Alexakis, Stella Baliou, and Petros Ioannou. Predatory bacteria in the treatment of infectious diseases and beyond. Infectious Disease Reports, 16:684-698, Jul 2024. URL: https://doi.org/10.3390/idr16040052, doi:10.3390/idr16040052. This article has 8 citations.

6. (wang2024thepredatoryproperties pages 1-2): Shuo Wang, Ya Gong, Guan-Jun Chen, and Zong-Jun Du. The predatory properties of bradymonabacteria, the representative of facultative prey-dependent predators. Microorganisms, 12:2008, Oct 2024. URL: https://doi.org/10.3390/microorganisms12102008, doi:10.3390/microorganisms12102008. This article has 3 citations.

7. (mookherjee2024flagellarstatorgenes pages 13-15): Abhirup Mookherjee, Mohor Mitra, Gal Sason, Polpass Arul Jose, Maria Martinenko, Shmuel Pietrokovski, and Edouard Jurkevitch. Flagellar stator genes control a trophic shift from obligate to facultative predation and biofilm formation in a bacterial predator. Aug 2024. URL: https://doi.org/10.1128/mbio.00715-24, doi:10.1128/mbio.00715-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

8. (kaplan2023bdellovibriopredationcycle pages 3-4): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

9. (kaplan2023bdellovibriopredationcycle pages 6-7): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

10. (kaplan2023bdellovibriopredationcycle media 473bcfba): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

11. (kaplan2023bdellovibriopredationcycle media 732758e8): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

12. (kaplan2023bdellovibriopredationcycle media 544a69cf): Mohammed Kaplan, Yi-Wei Chang, Catherine M. Oikonomou, William J. Nicolas, Andrew I. Jewett, Stefan Kreida, Przemysław Dutka, Lee A. Rettberg, Stefano Maggi, and Grant J. Jensen. Bdellovibrio predation cycle characterized at nanometre-scale resolution with cryo-electron tomography. Nature Microbiology, 8:1267-1279, Jun 2023. URL: https://doi.org/10.1038/s41564-023-01401-2, doi:10.1038/s41564-023-01401-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

13. (caulton2024bdellovibriobacteriovorususes pages 1-2): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 33 citations and is from a highest quality peer-reviewed journal.

14. (caulton2024bdellovibriobacteriovorususes pages 8-9): Simon G. Caulton, Carey Lambert, Jess Tyson, Paul Radford, Asmaa Al-Bayati, Samuel Greenwood, Emma J. Banks, Callum Clark, Rob Till, Elisabete Pires, R. Elizabeth Sockett, and Andrew L. Lovering. Bdellovibrio bacteriovorus uses chimeric fibre proteins to recognize and invade a broad range of bacterial hosts. Nature Microbiology, 9:214-227, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01552-2, doi:10.1038/s41564-023-01552-2. This article has 33 citations and is from a highest quality peer-reviewed journal.

15. (tyson2024preykillingwithout pages 1-2): Jess Tyson, Paul Radford, Carey Lambert, Rob Till, Simona G. Huwiler, Andrew L. Lovering, and R. Elizabeth Sockett. Prey killing without invasion by bdellovibrio bacteriovorus defective for a midas-family adhesin. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47412-3, doi:10.1038/s41467-024-47412-3. This article has 19 citations and is from a highest quality peer-reviewed journal.

16. (das2024howdogramnegative pages 3-4): Sourav Kumar Das and David Negus. How do gram-negative bacteria escape predation by bdellovibrio bacteriovorus? npj Antimicrobials and Resistance, Oct 2024. URL: https://doi.org/10.1038/s44259-024-00048-1, doi:10.1038/s44259-024-00048-1. This article has 8 citations and is from a peer-reviewed journal.

17. (das2024howdogramnegative pages 4-6): Sourav Kumar Das and David Negus. How do gram-negative bacteria escape predation by bdellovibrio bacteriovorus? npj Antimicrobials and Resistance, Oct 2024. URL: https://doi.org/10.1038/s44259-024-00048-1, doi:10.1038/s44259-024-00048-1. This article has 8 citations and is from a peer-reviewed journal.

18. (salgado2024controllingtheexpression pages 1-2): Sergio Salgado, Natalia Hernández‐Herreros, and M. Auxiliadora Prieto. Controlling the expression of heterologous genes in bdellovibrio bacteriovorus using synthetic biology strategies. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14517, doi:10.1111/1751-7915.14517. This article has 6 citations and is from a peer-reviewed journal.

19. (salgado2024controllingtheexpression pages 12-14): Sergio Salgado, Natalia Hernández‐Herreros, and M. Auxiliadora Prieto. Controlling the expression of heterologous genes in bdellovibrio bacteriovorus using synthetic biology strategies. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14517, doi:10.1111/1751-7915.14517. This article has 6 citations and is from a peer-reviewed journal.

20. (das2024howdogramnegative pages 3-3): Sourav Kumar Das and David Negus. How do gram-negative bacteria escape predation by bdellovibrio bacteriovorus? npj Antimicrobials and Resistance, Oct 2024. URL: https://doi.org/10.1038/s44259-024-00048-1, doi:10.1038/s44259-024-00048-1. This article has 8 citations and is from a peer-reviewed journal.

21. (mohsenipour2024predationonbacterial pages 1-2): Zeinab Mohsenipour, Parya Arazi, Mikael Skurnik, Behnaz Jahanbin, Hamid Reza Abtahi, Maryam Edalatifard, and Mohamad Mehdi Feizabadi. Predation on bacterial pathogens by predatory bacteria of sewage origin: three days prey-predator interactions. BMC Microbiology, Dec 2024. URL: https://doi.org/10.1186/s12866-024-03672-z, doi:10.1186/s12866-024-03672-z. This article has 7 citations and is from a peer-reviewed journal.

22. (mohsenipour2024predationonbacterial pages 6-8): Zeinab Mohsenipour, Parya Arazi, Mikael Skurnik, Behnaz Jahanbin, Hamid Reza Abtahi, Maryam Edalatifard, and Mohamad Mehdi Feizabadi. Predation on bacterial pathogens by predatory bacteria of sewage origin: three days prey-predator interactions. BMC Microbiology, Dec 2024. URL: https://doi.org/10.1186/s12866-024-03672-z, doi:10.1186/s12866-024-03672-z. This article has 7 citations and is from a peer-reviewed journal.

23. (herencias2024bdellovibrio’spreyindependentlifestyle pages 4-5): Cristina Herencias, Virginia Rivero-Buceta, Sergio Salgado, Natalia Hernández-Herreros, Fernando Baquero, Rosa del Campo, Juan Nogales, and M. Auxiliadora Prieto. Bdellovibrio’s prey-independent lifestyle is fueled by amino acids as a carbon source. Applied Microbiology and Biotechnology, Jul 2024. URL: https://doi.org/10.1007/s00253-024-13250-y, doi:10.1007/s00253-024-13250-y. This article has 9 citations and is from a domain leading peer-reviewed journal.

24. (herencias2024bdellovibrio’spreyindependentlifestyle pages 5-7): Cristina Herencias, Virginia Rivero-Buceta, Sergio Salgado, Natalia Hernández-Herreros, Fernando Baquero, Rosa del Campo, Juan Nogales, and M. Auxiliadora Prieto. Bdellovibrio’s prey-independent lifestyle is fueled by amino acids as a carbon source. Applied Microbiology and Biotechnology, Jul 2024. URL: https://doi.org/10.1007/s00253-024-13250-y, doi:10.1007/s00253-024-13250-y. This article has 9 citations and is from a domain leading peer-reviewed journal.

25. (herencias2024bdellovibrio’spreyindependentlifestyle pages 1-2): Cristina Herencias, Virginia Rivero-Buceta, Sergio Salgado, Natalia Hernández-Herreros, Fernando Baquero, Rosa del Campo, Juan Nogales, and M. Auxiliadora Prieto. Bdellovibrio’s prey-independent lifestyle is fueled by amino acids as a carbon source. Applied Microbiology and Biotechnology, Jul 2024. URL: https://doi.org/10.1007/s00253-024-13250-y, doi:10.1007/s00253-024-13250-y. This article has 9 citations and is from a domain leading peer-reviewed journal.

26. (herencias2024bdellovibrio’spreyindependentlifestyle pages 7-10): Cristina Herencias, Virginia Rivero-Buceta, Sergio Salgado, Natalia Hernández-Herreros, Fernando Baquero, Rosa del Campo, Juan Nogales, and M. Auxiliadora Prieto. Bdellovibrio’s prey-independent lifestyle is fueled by amino acids as a carbon source. Applied Microbiology and Biotechnology, Jul 2024. URL: https://doi.org/10.1007/s00253-024-13250-y, doi:10.1007/s00253-024-13250-y. This article has 9 citations and is from a domain leading peer-reviewed journal.

27. (herencias2024bdellovibrio’spreyindependentlifestyle pages 10-10): Cristina Herencias, Virginia Rivero-Buceta, Sergio Salgado, Natalia Hernández-Herreros, Fernando Baquero, Rosa del Campo, Juan Nogales, and M. Auxiliadora Prieto. Bdellovibrio’s prey-independent lifestyle is fueled by amino acids as a carbon source. Applied Microbiology and Biotechnology, Jul 2024. URL: https://doi.org/10.1007/s00253-024-13250-y, doi:10.1007/s00253-024-13250-y. This article has 9 citations and is from a domain leading peer-reviewed journal.

28. (xi2024evaluationofthe pages 10-11): Yao Xi, Yangyang Pan, Mei Li, Qiaoying Zeng, and Meng Wang. Evaluation of the application potential of bdellovibrio sp. ybd-1 isolated from yak faeces. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-63418-9, doi:10.1038/s41598-024-63418-9. This article has 5 citations and is from a peer-reviewed journal.

29. (mohsenipour2024predationonbacterial pages 8-10): Zeinab Mohsenipour, Parya Arazi, Mikael Skurnik, Behnaz Jahanbin, Hamid Reza Abtahi, Maryam Edalatifard, and Mohamad Mehdi Feizabadi. Predation on bacterial pathogens by predatory bacteria of sewage origin: three days prey-predator interactions. BMC Microbiology, Dec 2024. URL: https://doi.org/10.1186/s12866-024-03672-z, doi:10.1186/s12866-024-03672-z. This article has 7 citations and is from a peer-reviewed journal.

30. (rosberg2024regulationofantibiotic pages 7-9): Anna Karin Rosberg, Maria João Silva, Cecilie Skøtt Feidenhans’l, Eddie Cytryn, Edouard Jurkevitch, and Rolf Lood. Regulation of antibiotic resistance genes on agricultural land is dependent on both choice of organic amendment and prevalence of predatory bacteria. Antibiotics, 13:750, Aug 2024. URL: https://doi.org/10.3390/antibiotics13080750, doi:10.3390/antibiotics13080750. This article has 2 citations.

31. (rosberg2024regulationofantibiotic pages 3-7): Anna Karin Rosberg, Maria João Silva, Cecilie Skøtt Feidenhans’l, Eddie Cytryn, Edouard Jurkevitch, and Rolf Lood. Regulation of antibiotic resistance genes on agricultural land is dependent on both choice of organic amendment and prevalence of predatory bacteria. Antibiotics, 13:750, Aug 2024. URL: https://doi.org/10.3390/antibiotics13080750, doi:10.3390/antibiotics13080750. This article has 2 citations.

32. (salgado2024controllingtheexpression pages 7-8): Sergio Salgado, Natalia Hernández‐Herreros, and M. Auxiliadora Prieto. Controlling the expression of heterologous genes in bdellovibrio bacteriovorus using synthetic biology strategies. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14517, doi:10.1111/1751-7915.14517. This article has 6 citations and is from a peer-reviewed journal.

33. (salgado2024controllingtheexpression pages 14-15): Sergio Salgado, Natalia Hernández‐Herreros, and M. Auxiliadora Prieto. Controlling the expression of heterologous genes in bdellovibrio bacteriovorus using synthetic biology strategies. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14517, doi:10.1111/1751-7915.14517. This article has 6 citations and is from a peer-reviewed journal.