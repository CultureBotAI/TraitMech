---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:18:19.334919'
end_time: '2026-06-18T06:31:07.872653'
duration_seconds: 768.54
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: bacillus shaped
  trait_identifier: METPO:1000667
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: bacillus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape characterized by an elongated, rod cylindrical morphology
    with relatively parallel sides and rounded ends.
  parent_traits: METPO:1000666
  synonyms: bacillus
  evidence_summary: 'DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape
    formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)'
  causal_graph_summary: 'bacillus_shaped_rod_elongation: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** bacillus shaped
- **METPO identifier:** METPO:1000667
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an elongated, rod cylindrical morphology with relatively parallel sides and rounded ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** bacillus
- **Existing evidence:** DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)
- **Existing causal graph summary:** bacillus_shaped_rod_elongation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **bacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/bacillus_shaped.yaml`.

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
- **Trait label:** bacillus shaped
- **METPO identifier:** METPO:1000667
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by an elongated, rod cylindrical morphology with relatively parallel sides and rounded ends.
- **Parent traits:** METPO:1000666
- **Synonyms:** bacillus
- **Existing evidence:** DOI:10.1146/annurev-cellbio-010521-010834: bacterial rod shape formation (Supports bacillus shape as a rod-like bacterial morphogenesis phenotype.)
- **Existing causal graph summary:** bacillus_shaped_rod_elongation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **bacillus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/bacillus_shaped.yaml`.

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


## Research Report: Microbial Trait Causal Graph — **bacillus shaped** (METPO:1000667)

### Scope summary (TraitMech curation focus)
**Trait label:** bacillus shaped (syn. *bacillus*) — a **rod-shaped cell morphology** characterized by an elongated, cylindrical form with relatively parallel sides and rounded ends (METPO:1000667). This trait operationally corresponds to maintenance of a rod-like aspect ratio through **lateral/circumferential peptidoglycan (PG) insertion** during elongation coupled to septal PG synthesis during division. A key modern consensus is that the **peptidoglycan cell wall is a primary determinant of bacterial cell shape** (“PG… determines cell shape”). (shlosman2023allostericactivationof pages 1-2)

**Boundary/nearby traits:**
- **Coccus/ovoid**: cells become spherical when lateral elongation machinery is impaired or when PG insertion becomes more isotropic (e.g., Rod system defects; altered PBP localization). (castanheira2023evidenceoftwo pages 1-2, costa2024theroleof pages 1-2)
- **Coccobacilli/short rods**: intermediate aspect ratios; may reflect reduced elongation processivity or environmental constraints.
- **Curved rods (vibrioid)**: require additional curvature-generating determinants not necessary for basic rod/bacillus trait.
- **Filamentous**: elongated without septation; not equivalent to stable bacillus morphology.
- **Pleomorphic / L-forms**: loss of PG-controlled shape; outside this trait’s main mechanistic scope.

---

## 1) Key concepts and current mechanistic understanding (definitions)

### 1.1 Peptidoglycan as the load-bearing shape determinant
Recent mechanistic work reiterates that PG is the **major load-bearing structure** that both protects from osmotic lysis and **determines cell shape**. (shlosman2023allostericactivationof pages 1-2)

### 1.2 The elongasome / Rod complex and rod-shape generation
Rod-shaped bacteria elongate by inserting new cell wall material into the **sidewall** using the conserved **elongasome (Rod complex)**. In *Bacillus subtilis*, elongasome activity inserts long glycan strands that function as **“barrel-hoop-like reinforcing structures”**, “thereby giving rise to a rod-shaped cell.” (middlemiss2024molecularmotortugofwar pages 1-2)

Core, widely conserved modules highlighted in 2023–2024 literature:
- **SEDS-family PG polymerase RodA** (glycosyltransferase activity)
- **Class B penicillin-binding protein (bPBP) partner** (e.g., PBP2/MrdA in many Gram-negatives; PBP2A/PBPH in *B. subtilis*)
- **MreB cytoskeletal scaffold** and accessory factors (MreC/MreD, RodZ) coordinating spatial patterning of synthesis. (shlosman2023allostericactivationof pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2, castanheira2023evidenceoftwo pages 1-2)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 Allosteric activation of the essential elongation synthase (2023)
Shlosman et al. (Nature Communications, Jun 2023) provide a structural/regulatory mechanism for elongation: the essential elongation synthase **RodA–PBP2** dynamically exchanges between **closed and open states**, where “structural opening couples the activation of polymerization and crosslinking and is essential in vivo.” This supports a causal regulatory node for **conformational activation → PG synthesis → elongation/rod shape**. (shlosman2023allostericactivationof pages 1-2)

**Publication/URL:** https://doi.org/10.1038/s41467-023-39037-9 (Jun 2023). (shlosman2023allostericactivationof pages 1-2)

### 2.2 Elongasome dynamics controlled by RodA levels and a “tug-of-war” model (2024)
Middlemiss et al. (Nature Communications, Jun 2024) link **processive motion** of elongasome complexes to rod-shape maintenance and show that “cellular levels of RodA regulate elongasome processivity, reversal and pausing,” proposing a **molecular motor tug-of-war** between oppositely oriented synthesis complexes associated with MreB as a regulator of elongation dynamics and therefore shape. (middlemiss2024molecularmotortugofwar pages 1-2)

**Visual evidence:** their figures schematize the tug-of-war model and show RodA-level dependence of processivity. (middlemiss2024molecularmotortugofwar media febec7a3, middlemiss2024molecularmotortugofwar media 8d75e962, middlemiss2024molecularmotortugofwar media 6e27f329)

**Publication/URL:** https://doi.org/10.1038/s41467-024-49785-x (Jun 2024). (middlemiss2024molecularmotortugofwar pages 1-2)

### 2.3 Environment-dependent alternative elongasomes in *Salmonella* (2023)
Castanheira & García-del Portillo (Communications Biology, Sep 2023) provide evidence for **two differentially regulated elongasomes** in *Salmonella*, directed by distinct morphogenetic PBPs:
- A **PBP2-directed elongasome** responsive to **neutral pH**
- A pathogen-specific **PBP2SAL-directed elongasome** that assembles and functions in **acidic conditions**, “moves at a lower speed,” and can “generate rod shape independently of PBP2.” (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 3-5)

**Quantitative/conditional statistics:** ΔmrdA (PBP2) mutants at neutral pH become “giant spherical cells” and exhibit large viability losses (~5-log in LB; ~2–3 log in PCN), while growth in acidified PCN (pH 4.6) restores “genuine rod morphology.” (castanheira2023evidenceoftwo pages 1-2)

**Publication/URL:** https://doi.org/10.1038/s42003-023-05308-w (Sep 2023). (castanheira2023evidenceoftwo pages 1-2)

### 2.4 Drug-like perturbation reveals synthase–hydrolase coordination underlying rod stability (2023)
Zhang et al. (Nature Communications, Sep 2023) show that **pharmacological inhibition of class A PBPs (aPBPs) by moenomycin** can collapse rod shape even when aPBPs are genetically non-essential in their system, by perturbing coordination with hydrolases. Specifically, moenomycin “promotes the binding between DacB and PG,” and inhibited PBP1a2 accelerates pole degradation by **DacB**, resulting in rod-shape collapse. (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

**Publication/URL:** https://doi.org/10.1038/s41467-023-41082-3 (Sep 2023). (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

### 2.5 Rod-complex accessory factor RodZ: shape loss and envelope fragility with measurable output (2024)
Ojima et al. (Frontiers in Microbiology, Jun 2024) use *E. coli* ΔrodZ to connect Rod-complex integrity to cell envelope failure:
- “ΔrodZ cells were spherical (WT cells are rod-shaped).” (ojima2024buddingandexplosive pages 1-2)
- ΔrodZ produced **>50×** more outer-membrane vesicles than WT; CRISPRi repression of mreB (~20% expression) produced **8×** higher vesicles than WT. (ojima2024buddingandexplosive pages 1-2)
- **~7%** of ΔrodZ cells showed aberrant surface structures; holes in PG were observed; osmotic support with **sucrose** increased OD660 and decreased vesicle production drastically. (ojima2024buddingandexplosive pages 1-2)

**Publication/URL:** https://doi.org/10.3389/fmicb.2024.1400434 (Jun 2024). (ojima2024buddingandexplosive pages 1-2)

### 2.6 Spatial regulation of PG synthesis proteins modulates elongation vs spherical morphology (2024)
Costa et al. (mBio, Mar 2024) identify **GpsB** as a determinant of proper morphogenesis in *Staphylococcus aureus* elongation (a taxon where elongation is subtler). Loss of GpsB causes “partial delocalization… of PBP2 and PBP4” from septum to periphery, increasing peripheral PG insertion/crosslinking and making cells more spherical. Reported quantitative effect includes ~**10% reduction in eccentricity** in the gpsB mutant. (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13)

**Publication/URL:** https://doi.org/10.1128/mbio.03235-23 (Mar 2024). (costa2024theroleof pages 1-2)

---

## 3) Current applications and real-world implementations

### 3.1 Antibiotic discovery and envelope-targeting strategies
Because PG synthesis determines shape and is essential for osmotic stability, elongasome/divisome enzymes are longstanding antibiotic targets; recent mechanistic detail (e.g., RodA–PBP2 allosteric activation) provides more specific opportunities for **mechanism-based inhibitor design** against conserved activation motions or protein–protein interfaces. (shlosman2023allostericactivationof pages 1-2)

### 3.2 Bioprocess and phenotype engineering
Morphology engineering is used in industrial microbiology to tune downstream processing and performance traits. For instance, ΔrodZ and MreB repression alter envelope integrity and vesiculation, which can be harnessed (in principle) for production of membrane vesicles or as readouts of envelope stress during strain optimization. (ojima2024buddingandexplosive pages 1-2)

---

## 4) Expert opinions / authoritative synthesis (as stated in sources)

Across these recent high-authority studies, a consistent mechanistic framing emerges:
- **“PG… determines cell shape”** and is the key load-bearing structure. (shlosman2023allostericactivationof pages 1-2)
- Rod shape is generated by the **elongasome/Rod complex** executing sidewall PG insertion (with MreB scaffold and RodA–bPBP synthase pairing) and coordinated with division machinery. (castanheira2023evidenceoftwo pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2)
- Regulation occurs at multiple levels: enzyme conformational activation (open/closed), complex processivity dynamics, and environmental switching between alternative morphogenetic modules in pathogens. (shlosman2023allostericactivationof pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2, castanheira2023evidenceoftwo pages 1-2)

---

## 5) Candidate causal-graph nodes (grouped by type; with ontology grounding suggestions)

### A. Trait node
- **bacillus shaped** — METPO:1000667 (given)

### B. Core molecular machinery (conserved candidates)
- **Peptidoglycan (PG) cell wall** — GO:0009273 (cell wall); PG biosynthesis process candidate GO:0009252
- **RodA (SEDS family PG polymerase)** — UniProtKB (taxon-specific)
- **PBP2 / MrdA (class B transpeptidase)** — UniProtKB (taxon-specific)
- **MreB (actin homolog cytoskeleton)** — UniProtKB (taxon-specific)
- **MreC/MreD, RodZ** (elongasome accessory components) — UniProtKB candidates (taxon-specific) (shlosman2023allostericactivationof pages 1-2, ojima2024buddingandexplosive pages 1-2)

### C. Alternative / taxon-specific morphogenetic enzymes
- **PBP2SAL** (Salmonella-specific morphogenetic bPBP) — label-only unless UniProt provided in curated organism set (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 3-5)
- **PBP2A/PBPH** (*Bacillus subtilis* bPBPs mentioned as RodA partners) — label-only unless mapped to UniProt (middlemiss2024molecularmotortugofwar pages 1-2)

### D. Remodeling/coordination enzymes
- **Class A PBPs (aPBPs; e.g., PBP1a2)** — enzyme family label-only unless taxon specified (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
- **DacB (PG hydrolase/peptidase; PBP4 family)** — UniProtKB candidate; process node: polar PG degradation (zhang2023coordinatedpeptidoglycansynthases pages 1-2)

### E. Regulators of spatial organization
- **GpsB** (morphogenesis regulator affecting PBP localization) — UniProtKB candidate (taxon-specific; *S. aureus*) (costa2024theroleof pages 1-2)

### F. Environmental/experimental factors
- **Neutral pH vs acidic pH** — ENVO candidates (acidic/neutral environment); influences which elongasome is active in *Salmonella* (castanheira2023evidenceoftwo pages 1-2)
- **Osmotic support (sucrose)** — CHEBI:17992; modulates osmotic sensitivity/vesiculation in ΔrodZ (ojima2024buddingandexplosive pages 1-2)
- **Growth media condition nodes** (LB, PCN; acidified PCN pH 4.6) — label-only (castanheira2023evidenceoftwo pages 1-2)

### G. Chemicals / inhibitors / assays
- **Moenomycin** — CHEBI:68868; inhibits aPBPs (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
- **Fluorescent D-amino acids (e.g., HADA)** — label-only; assay readout of PG insertion patterning (costa2024theroleof pages 11-13)

---

## 6) Evidence-backed candidate causal edges (triples)
The following table is formatted for direct TraitMech curation and includes edge candidates with grounding suggestions, evidence snippets, and uncertainty notes.

| Edge (Subject —predicate→ Object) | Node types (S/O) | Suggested ontology grounding (CURIEs when clear) | Evidence snippet (short quote) | Source (authors, year, title) | DOI URL | Publication date/month | Notes/uncertainty |
|---|---|---|---|---|---|---|---|
| Peptidoglycan cell wall —determines→ bacillus shaped | cellular structure / morphology trait | GO:0009273 / METPO:1000667 | “PG… protects bacteria against osmotic lysis and determines cell shape.” (shlosman2023allostericactivationof pages 1-2) | Shlosman et al., 2023, *Allosteric activation of cell wall synthesis during bacterial growth* | https://doi.org/10.1038/s41467-023-39037-9 | 2023-06 | Broad, strong mechanistic edge across bacteria. |
| RodA-PBP2 (Rod complex synthase) —required_for→ bacterial elongation | protein complex / biological process | RodA: UniProtKB candidate; PBP2/MrdA: UniProtKB candidate; GO:0009252 | “RodA-PBP2… [is] an essential synthase ‘responsible for bacterial elongation.’” (shlosman2023allostericactivationof pages 1-2) | Shlosman et al., 2023, *Allosteric activation of cell wall synthesis during bacterial growth* | https://doi.org/10.1038/s41467-023-39037-9 | 2023-06 | Core elongasome edge; exact UniProt depends on taxon. |
| RodA-PBP2 open state —activates→ peptidoglycan polymerization/crosslinking | conformational state / biological process | label-only / GO:0009252 | “structural opening couples the activation of polymerization and crosslinking and is essential in vivo” (shlosman2023allostericactivationof pages 1-2) | Shlosman et al., 2023, *Allosteric activation of cell wall synthesis during bacterial growth* | https://doi.org/10.1038/s41467-023-39037-9 | 2023-06 | Useful regulatory edge; conformational-state node may remain label-only. |
| Elongasome-mediated circumferential glycan insertion —gives_rise_to→ bacillus shaped | biological process / morphology trait | GO:0009252 / METPO:1000667 | “inserts long glycan strands that act as barrel-hoop-like reinforcing structures, thereby giving rise to a rod-shaped cell” (middlemiss2024molecularmotortugofwar pages 1-2) | Middlemiss et al., 2024, *Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in Bacillus subtilis* | https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Strong, directly trait-linked edge. |
| RodA abundance —regulates→ elongasome processivity | protein / process quality | RodA: UniProtKB candidate / label-only | “cellular levels of RodA regulate elongasome processivity, reversal and pausing” (middlemiss2024molecularmotortugofwar pages 1-2) | Middlemiss et al., 2024, *Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in Bacillus subtilis* | https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Quantitative/regulatory edge; processivity node may remain label-only. |
| MreB-associated opposing synthesis complexes —regulate→ elongasome processivity | protein/cytoskeletal system / process quality | MreB: UniProtKB candidate / label-only | “regulated by molecular motor tug-of-war competition between… oppositely oriented peptidoglycan synthesis complexes associated with the MreB filament” (middlemiss2024molecularmotortugofwar pages 1-2) | Middlemiss et al., 2024, *Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in Bacillus subtilis* | https://doi.org/10.1038/s41467-024-49785-x | 2024-06 | Mechanistic model edge; moderate abstraction. |
| Neutral pH —favors activity/assembly_of→ PBP2-directed elongasome | environmental factor / protein complex | ENVO:09200004 (neutral pH, candidate) / PBP2(MrdA): UniProtKB candidate | “The PBP2-elongasome responds to neutral pH” (castanheira2023evidenceoftwo pages 1-2) | Castanheira & García-del Portillo, 2023, *Evidence of two differentially regulated elongasomes in Salmonella* | https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Taxon-specific to *Salmonella*; mark uncertain for broad curation. |
| Acidic pH —induces assembly_of→ PBP2SAL-directed elongasome | environmental factor / protein complex | ENVO:09200003 (acidic environment, candidate) / label-only PBP2SAL elongasome | “PBP2SAL… assembles in acidic conditions” (castanheira2023evidenceoftwo pages 1-2) | Castanheira & García-del Portillo, 2023, *Evidence of two differentially regulated elongasomes in Salmonella* | https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Strong within *Salmonella*; uncertain outside taxa carrying PBP2SAL. |
| PBP2SAL —can_generate→ bacillus shaped | protein / morphology trait | label-only PBP2SAL / METPO:1000667 | “PBP2SAL acting as morphogenetic protein that can generate rod shape independently of PBP2” (castanheira2023evidenceoftwo pages 3-5) | Castanheira & García-del Portillo, 2023, *Evidence of two differentially regulated elongasomes in Salmonella* | https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Taxon-specific alternative elongasome; curate cautiously. |
| mrdA/PBP2 loss at neutral pH —causes→ spherical/giant spherical morphology | gene/protein / morphology trait | PBP2/MrdA: UniProtKB candidate / coccus-like morphology label | “ΔmrdA mutants grown at neutral pH… become giant spherical cells” (castanheira2023evidenceoftwo pages 1-2) | Castanheira & García-del Portillo, 2023, *Evidence of two differentially regulated elongasomes in Salmonella* | https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Conditional phenotype; environment-dependent and taxon-specific. |
| Acidified PCN medium (pH 4.6) —restores→ rod morphology in ΔmrdA cells | experimental condition / morphology trait | label-only / METPO:1000667 | “growth in acidified PCN (pH 4.6) restores genuine rod morphology” (castanheira2023evidenceoftwo pages 1-2) | Castanheira & García-del Portillo, 2023, *Evidence of two differentially regulated elongasomes in Salmonella* | https://doi.org/10.1038/s42003-023-05308-w | 2023-09 | Assay-specific rescue edge in *Salmonella*. |
| Moenomycin —inhibits→ class A PBPs | chemical / enzyme family | CHEBI:68868 / aPBPs label-only | “moenomycin… inhibits a family of PG synthases known as Class-A penicillin-binding proteins” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | Zhang et al., 2023, *Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall* | https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | Strong inhibitor edge. |
| aPBP inhibition by moenomycin —promotes→ DacB binding to peptidoglycan | inhibited enzyme activity / molecular interaction | aPBPs label-only / DacB: UniProtKB candidate + GO:0009273 | “Moenomycin promotes the binding between DacB and PG” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | Zhang et al., 2023, *Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall* | https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | Mechanistic intermediate linking inhibitor to shape collapse. |
| DacB enrichment/binding at poles —accelerates→ polar peptidoglycan degradation | enzyme / biological process | DacB: UniProtKB candidate / GO:0009253 candidate | “DacB… degrades polar PG and collapses rod morphology when enriched at poles” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | Zhang et al., 2023, *Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall* | https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | Strong in *Myxococcus xanthus*; hydrolase-coordination lesson may generalize. |
| Polar peptidoglycan degradation —causes→ rod-shape collapse | biological process / morphology trait | GO candidate / METPO:1000667 | “polar PG degradation… collapses rod morphology” (zhang2023coordinatedpeptidoglycansynthases pages 1-2) | Zhang et al., 2023, *Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall* | https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | Downstream phenotype edge; organism-specific evidence. |
| RodZ loss (ΔrodZ) —causes→ spherical cells | protein / morphology trait | RodZ: UniProtKB candidate / coccus-like morphology label | “ΔrodZ cells were spherical (WT cells are rod-shaped)” (ojima2024buddingandexplosive pages 1-2) | Ojima et al., 2024, *Budding and explosive membrane vesicle production by hypervesiculating Escherichia coli strain ΔrodZ* | https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | Strong for *E. coli*; RodZ broadly implicated in rod maintenance. |
| MreB repression —causes→ increased vesicle production and shape defects | protein / phenotype | MreB: UniProtKB candidate / outer membrane vesiculation label | “mreB-repressed strain mreBR3 showed eightfold higher vesicle production than the WT” (ojima2024buddingandexplosive pages 1-2) | Ojima et al., 2024, *Budding and explosive membrane vesicle production by hypervesiculating Escherichia coli strain ΔrodZ* | https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | Indirect trait edge via PG integrity and osmotic sensitivity. |
| Sucrose osmotic support —reduces→ vesiculation/osmotic sensitivity of ΔrodZ cells | chemical/environmental factor / phenotype | CHEBI:17992 / label-only | “using sucrose, the OD660… increased significantly, and vesicle production decreased drastically” (ojima2024buddingandexplosive pages 1-2) | Ojima et al., 2024, *Budding and explosive membrane vesicle production by hypervesiculating Escherichia coli strain ΔrodZ* | https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | Supportive edge showing envelope mechanics contribute to rod-shape maintenance. |
| GpsB loss —delocalizes→ PBP2/PBP4 from septum to periphery | protein / protein localization state | GpsB: UniProtKB candidate / PBP2,PBP4: UniProtKB candidates | “The gpsB mutant showed the strongest phenotype, mediated by the partial delocalization from the division septum of PBP2 and PBP4” (costa2024theroleof pages 1-2) | Costa et al., 2024, *The role of GpsB in Staphylococcus aureus cell morphogenesis* | https://doi.org/10.1128/mbio.03235-23 | 2024-03 | Taxon-specific to *S. aureus*; still valuable for morphology-regulation node set. |
| Increased peripheral PBP2/PBP4 peptidoglycan insertion/crosslinking —causes→ more spherical cells | biological process / morphology trait | GO:0009252 candidate / coccus-like morphology label | “higher levels of peptidoglycan insertion/crosslinking throughout the entire cell… [cells] become more spherical” (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13) | Costa et al., 2024, *The role of GpsB in Staphylococcus aureus cell morphogenesis* | https://doi.org/10.1128/mbio.03235-23 | 2024-03 | Strong within ovococcal *S. aureus*; uncertain for canonical bacilli. |
| RodA/PBP2 activity —supports→ expression of cell wall-spanning supramolecular organelles and virulence | proteins / phenotype | RodA: UniProtKB candidate; PBP2: UniProtKB candidate / virulence label | “Essential roles of RodA peptidoglycan polymerase and PBP2 transpeptidase in expression of cell wall-spanning supramolecular organelles and modulating Salmonella virulence” (doble2024essentialrolesof pages 35-37) | Doble et al., 2024, *Essential Roles of RodA Peptidoglycan Polymerase and PBP2 Transpeptidase in Expression of Cell Wall-Spanning Supramolecular Organelles and Modulating Salmonella Virulence* | https://doi.org/10.1101/2024.07.01.601524 | 2024-07 | Preprint; not primary evidence for rod-shape mechanism alone, but supports broader consequences of Rod machinery. |


*Table: This table compiles candidate causal edges for curating a TraitMech graph of bacillus-shaped morphology. It prioritizes recent mechanistic evidence on peptidoglycan synthesis, elongasome regulation, environmental modulation, and perturbations that convert rods toward spherical states.*

---

## 7) Curation warnings (do-not-curate-yet / caution flags)
1. **Taxon-specific modules:** PBP2SAL-directed elongasome and its pH regulation are strongly supported in *Salmonella* but should be curated as **uncertain / taxon-specific** nodes unless the trait graph is intended to capture pathogen niche adaptation modules. (castanheira2023evidenceoftwo pages 1-2, castanheira2023evidenceoftwo pages 3-5)
2. **Ovococcal elongation regulators:** GpsB → PBP2/PBP4 localization → spherical morphology is strong in *S. aureus* but may not generalize to canonical bacilli/Gram-negatives; curate as **taxon-specific**. (costa2024theroleof pages 1-2, costa2024theroleof pages 11-13)
3. **Preprints:** Doble et al. 2024 is a preprint; treat as supporting context for RodA/PBP2 consequences (virulence/organelles) rather than definitive new mechanistic edges unless corroborated by peer-reviewed sources. (doble2024essentialrolesof pages 35-37)
4. **Abstracted process nodes:** “elongasome processivity,” “tug-of-war competition,” and “open vs closed state” are mechanistically meaningful but may require consistent ontology strategy (label-only nodes or mapping to GO process qualities) before inclusion. (shlosman2023allostericactivationof pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2, middlemiss2024molecularmotortugofwar media febec7a3)

---

## DOI-first bibliography (with URLs and dates)
- Shlosman I. et al. **Allosteric activation of cell wall synthesis during bacterial growth.** *Nature Communications* (Jun 2023). https://doi.org/10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 1-2)
- Zhang H. et al. **Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall.** *Nature Communications* (Sep 2023). https://doi.org/10.1038/s41467-023-41082-3 (zhang2023coordinatedpeptidoglycansynthases pages 1-2)
- Castanheira S., García-del Portillo F. **Evidence of two differentially regulated elongasomes in Salmonella.** *Communications Biology* (Sep 2023). https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2)
- Costa S.F. et al. **The role of GpsB in Staphylococcus aureus cell morphogenesis.** *mBio* (Mar 2024). https://doi.org/10.1128/mbio.03235-23 (costa2024theroleof pages 1-2)
- Middlemiss S. et al. **Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in Bacillus subtilis.** *Nature Communications* (Jun 2024). https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2)
- Ojima Y. et al. **Budding and explosive membrane vesicle production by hypervesiculating Escherichia coli strain ΔrodZ.** *Frontiers in Microbiology* (Jun 2024). https://doi.org/10.3389/fmicb.2024.1400434 (ojima2024buddingandexplosive pages 1-2)
- Doble A.C. et al. **Essential Roles of RodA Peptidoglycan Polymerase and PBP2 Transpeptidase…** *bioRxiv* (Jul 2024). https://doi.org/10.1101/2024.07.01.601524 (doble2024essentialrolesof pages 35-37)

---

### Included figure evidence (for curators)
- Middlemiss et al. 2024 figures supporting the elongasome tug-of-war/processivity model and RodA-level dependence. (middlemiss2024molecularmotortugofwar media febec7a3, middlemiss2024molecularmotortugofwar media 8d75e962, middlemiss2024molecularmotortugofwar media 6e27f329)


References

1. (shlosman2023allostericactivationof pages 1-2): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 44 citations and is from a highest quality peer-reviewed journal.

2. (castanheira2023evidenceoftwo pages 1-2): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

3. (costa2024theroleof pages 1-2): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

4. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (middlemiss2024molecularmotortugofwar media febec7a3): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

6. (middlemiss2024molecularmotortugofwar media 8d75e962): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

7. (middlemiss2024molecularmotortugofwar media 6e27f329): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (castanheira2023evidenceoftwo pages 3-5): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.

9. (zhang2023coordinatedpeptidoglycansynthases pages 1-2): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

10. (ojima2024buddingandexplosive pages 1-2): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.

11. (costa2024theroleof pages 11-13): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 17 citations and is from a domain leading peer-reviewed journal.

12. (doble2024essentialrolesof pages 35-37): Anne C. Doble, Bethany C Gollan, John Clark-Corrigall, David M. Bulmer, Richard A Daniel, Pietro Mastroeni, and C. M. Anjam Khan. Essential roles of roda peptidoglycan polymerase and pbp2 transpeptidase in expression of cell wall-spanning supramolecular organelles and modulating salmonella virulence. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.01.601524, doi:10.1101/2024.07.01.601524. This article has 1 citations.