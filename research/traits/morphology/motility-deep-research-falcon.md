---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:38:18.582187'
end_time: '2026-06-18T08:57:25.665713'
duration_seconds: 1147.08
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: motility
  trait_identifier: METPO:1000701
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: motility
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype in which an organism has the capability to move independently
    through its environment, typically by means of flagella, pili, gliding mechanisms,
    or other locomotory structures.
  parent_traits: METPO:1000059
  synonyms: Morphology.cell morphology.motility
  evidence_summary: 'DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria
    to move around (Supports bacterial motility as a phenotype mediated by multiple
    molecular machines and physical mechanisms.)'
  causal_graph_summary: 'motility_locomotion_machinery: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** motility
- **METPO identifier:** METPO:1000701
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype in which an organism has the capability to move independently through its environment, typically by means of flagella, pili, gliding mechanisms, or other locomotory structures.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.motility
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria to move around (Supports bacterial motility as a phenotype mediated by multiple molecular machines and physical mechanisms.)
- **Existing causal graph summary:** motility_locomotion_machinery: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motility.yaml`.

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
- **Trait label:** motility
- **METPO identifier:** METPO:1000701
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype in which an organism has the capability to move independently through its environment, typically by means of flagella, pili, gliding mechanisms, or other locomotory structures.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.motility
- **Existing evidence:** DOI:10.1038/s41579-021-00626-4: mechanisms that allow bacteria to move around (Supports bacterial motility as a phenotype mediated by multiple molecular machines and physical mechanisms.)
- **Existing causal graph summary:** motility_locomotion_machinery: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/motility.yaml`.

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


## Microbial trait causal-graph report: **Motility** (METPO:1000701)

### Executive scope summary
**Motility** (METPO:1000701) is best curated as an **active, self-propelled locomotion phenotype** produced by dedicated microbial nanomachines (e.g., bacterial flagella, archaeal archaella, type IV pili, and gliding motility machineries) that generate force and yield measurable cell displacement in liquid or on surfaces. Recent work emphasizes that “motility” is a **family of mechanistically distinct modes** whose expression depends strongly on physical context (liquid vs semi-solid vs hard surface; viscosity; surface chemistry), and thus phenotype terms like **swimming, swarming, twitching, gliding, surfing/surface spreading** should be treated as assay- and environment-qualified children/contexts rather than synonyms. (warrell2024interspeciessurfactantsserve pages 1-2, warrell2024interspeciessurfactantsserve pages 15-17, ohara2024surfacehydrophilicitypromotes pages 1-2)

**Boundary cases that require careful curation**:
- **Chemotaxis vs motility**: chemotaxis biases movement trajectories but is not itself the propulsion machinery; it should be modeled as a regulator of motility trajectories rather than the motility phenotype itself. (jin2024microbesinporous pages 9-14)
- **Active vs passive colony expansion**: sliding and some “surface spreading” phenomena can be passive or propulsion-independent; these should be flagged as *uncertain/assay-specific* when used as evidence for the general “motility” trait. (warrell2024interspeciessurfactantsserve pages 15-17)
- **Surface-associated modes are not interchangeable**: e.g., in *Pseudomonas aeruginosa*, swarming depends on flagella plus endogenous rhamnolipid production, while a distinct surfactant-enabled surface spreading requires functional flagella but not type IV pili or rhamnolipids. (warrell2024interspeciessurfactantsserve pages 15-17)

---

## 1) Key concepts and definitions (current understanding)

### Core motility modes and their canonical machinery
- **Swimming (liquid)**: typically driven by a **polar flagellum** in liquid environments. (warrell2024interspeciessurfactantsserve pages 1-2)
- **Swarming (semi-solid surfaces)**: a **flagella-mediated social surface migration** that often requires biosurfactants (e.g., rhamnolipids in *P. aeruginosa*) and shows distinct colony morphologies (tendrils/rafts). (warrell2024interspeciessurfactantsserve pages 1-2)
- **Twitching (hard surfaces/interstitial)**: **type IV pili (T4P)**-driven surface translocation via extension–attachment–retraction cycles. (ohara2024surfacehydrophilicitypromotes pages 1-2)
- **Gliding (solid surfaces, flagella/pili independent)**: diverse mechanisms; two well-supported examples include:
  - **Bacteroidetes/Flavobacterium-like gliding**, where the proton-driven **GldLM** motor drives surface adhesin (e.g., **SprB**) motion along tracks. (shibata2023filamentousstructuresin pages 1-2)
  - **Myxococcus xanthus gliding**, where bacterial focal adhesion complexes (bFACs) transmit force across the envelope and require peptidoglycan coupling factors such as **AgmT**. (carbo2024alytictransglycosylase pages 1-2)
- **Archaeal swimming**: driven by the **archaellum**, a rotary filament system functionally analogous (but evolutionarily distinct) from bacterial flagella. (gaines2024towardsamolecular pages 1-2)
- **Archaeal twitching**: now directly demonstrated in *Sulfolobus acidocaldarius* via retractable **Aap (archaeal T4P-like) pili** despite lacking bacterial PilT homologs. (charlesorszag2024adhesionpilusretraction pages 1-2)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 Surface motility is strongly shaped by community and physicochemical context
A 2024 *Journal of Bacteriology* study showed that **exogenous surfactants** from other species can act as “public goods,” enabling *P. aeruginosa* to adopt a **flagella-dependent surface spreading** motility even on hard agar, distinct from classical swarming and distinct from passive sliding. (warrell2024interspeciessurfactantsserve pages 15-17)

A 2024 *mSphere* paper demonstrated that **surface hydrophilicity** is a strong determinant of T4P-driven twitching: bile salts and detergents increase twitching not by a stress response but by altering the surface physicochemistry/hydrophilicity, and hydrophilic substrates (glass/plasma-treated plastics) can bypass the need for detergents. (ohara2024surfacehydrophilicitypromotes pages 1-2)

### 2.2 Mechanistic integration of motility with second-messenger signaling (c-di-GMP, cAMP)
A 2024 *Nature Communications* paper identified a direct environmental-sensing module in *P. aeruginosa* where iron binding to the CHASE4 domain of **IsmP** disrupts IsmP–**ImcA** interaction, increasing ImcA diguanylate cyclase activity and **raising c-di-GMP**, which “promot[es] bioﬁlm formation and reduc[es] bacterial motility.” (zhan2024acdigmpsignaling pages 1-2)

Separately, 2024 work in *Vibrio parahaemolyticus* shows **environmental Ca2+** can significantly increase **c-di-GMP production** and **swimming motility**, and causes broad transcriptome remodeling (459 differentially expressed genes), including upregulation of polar-flagellum genes. (li2024theeffectof pages 1-2)

For T4P and twitching, 2024 reviews in *Journal of Bacteriology* synthesize that surface engagement triggers the **Pil-Chp → CyaB → cAMP → Vfr** pathway, which upregulates T4P genes and supports surface adaptation/virulence; PilT is proposed as a key sensor linking retraction to signaling. (geiger2024abacterialsense pages 1-3, roberge2024buildingpermits—controlof pages 3-5)

### 2.3 Archaeal motility: structural and post-translational control
Two 2024 *Nature Communications* studies provide particularly curatable mechanistic advances:
- **Aap pili-driven twitching without PilT**: *S. acidocaldarius* moves by retracting surface-adhered Aap pili; reported retraction speeds are **0.3–2 μm·s−1**, and ΔaapF abolishes twitching (quantified by displacement/persistence). (charlesorszag2024adhesionpilusretraction pages 4-6, charlesorszag2024adhesionpilusretraction pages 1-2)
- **Archaellum N-glycosylation controls filament interactions and motility**: truncating N-linked glycans leads to filament bundling and compromised motility; tetrasaccharides are proposed to act as “physical spacers” limiting aggregation. (sofer2024perturbednglycosylationof pages 1-2)

---

## 3) Current applications and real-world implementations

### 3.1 Infection, virulence, and biofilms
Motility traits are routinely treated as **fitness/virulence determinants** because they influence colonization and biofilm formation. For example, T4P-dependent twitching is characterized as a key virulence-associated behavior in *P. aeruginosa* and is coupled to surface sensing and cAMP/Vfr-controlled virulence programs. (geiger2024abacterialsense pages 1-3)

### 3.2 Materials and device contexts (surface chemistry)
The finding that **hydrophilicity modulates twitching** suggests real-world relevance to **implant/tissue surface properties**, because hydrophilic materials promote T4P function and interstitial surface translocation in multiple pathogens examined. (ohara2024surfacehydrophilicitypromotes pages 1-2)

### 3.3 Microbial communities and “public goods” control of motility
In polymicrobial settings, secreted surfactants can enable or reshape motility modes, expanding niche access (e.g., surfactant-enabled surface spreading on otherwise non-permissive surfaces). This has implications for wounds/respiratory co-infections and soil communities. (warrell2024interspeciessurfactantsserve pages 15-17)

---

## 4) Expert opinions and authoritative synthesis

### 4.1 “Motility” as a context-dependent phenotype class
Across the 2024 mechanistic and review literature, a consistent expert framing is that “motility” should be decomposed into **mode-specific phenotypes** tied to distinct machines and to **environmental/assay parameters** such as surface hardness and viscosity, which strongly influence which motility program manifests. (warrell2024interspeciessurfactantsserve pages 1-2, warrell2024interspeciessurfactantsserve pages 15-17)

### 4.2 Surface sensing as a mechanochemical signaling process
The 2024 *Journal of Bacteriology* synthesis proposes that T4P motors are not merely actuators but also participate in **mechanosensing**, with PilT proposed to relay surface engagement signals via PilJ to the Pil-Chp system, elevating cAMP across generations. (geiger2024abacterialsense pages 1-3)

A complementary 2024 review emphasizes PilB as a checkpoint integrating second messengers and protein effectors to control T4P assembly and thereby twitching behavior. (roberge2024buildingpermits—controlof pages 1-3)

(See Figure evidence: schematic of PilB/PilT competition and Pil-Chp→cAMP/Vfr in (roberge2024buildingpermits—controlof media 4513e20a).)

---

## 5) Recent quantitative/statistical data points usable in curation

- **Aap pilus retraction speed** (archaea): **0.3–2 μm·s−1** in *S. acidocaldarius*. (charlesorszag2024adhesionpilusretraction pages 4-6)
- **Motility displacement metrics** (archaea): WT-like strains show average displacements **4.6–6.6 μm** and persistence ratios **0.11–0.12**; ΔaapF average displacement **1.49 μm** and persistence **0.02**; **46.2%** of ΔaapF cells have total displacement <2 μm. (charlesorszag2024adhesionpilusretraction pages 1-2)
- **Environmental iron sensing affinity**: IsmP CHASE4 domain iron binding reported around **Kd ~7 μM** (ITC; CHASE4-containing proteins; values cited in text). (zhan2024acdigmpsignaling pages 9-10)
- **Transcriptome-scale calcium response**: **459** differentially expressed genes in *V. parahaemolyticus* upon Ca2+ exposure (RNA-seq). (li2024theeffectof pages 1-2)

---

## TraitMech curation content

### A) Candidate nodes grouped by type (with grounding suggestions)

**Phenotypes / processes (GO / label):**
- swimming motility (GO:0060284) (warrell2024interspeciessurfactantsserve pages 1-2)
- swarming motility (GO:0009405) (warrell2024interspeciessurfactantsserve pages 1-2)
- twitching motility (GO:0001539) (ohara2024surfacehydrophilicitypromotes pages 1-2)
- gliding motility (label; bacterial gliding varies; Myxococcus and Bacteroidetes have distinct systems) (shibata2023filamentousstructuresin pages 1-2, carbo2024alytictransglycosylase pages 1-2)
- surface spreading / surfing-like motility (label; mode definition is species- and context-specific) (warrell2024interspeciessurfactantsserve pages 15-17)

**Locomotory structures / complexes:**
- bacterial flagellum (GO:0009288) (warrell2024interspeciessurfactantsserve pages 1-2)
- archaeal archaellum (label; sometimes “archaeal flagellum”) (gaines2024towardsamolecular pages 1-2, sofer2024perturbednglycosylationof pages 1-2)
- type IV pilus (GO:0009289) (ohara2024surfacehydrophilicitypromotes pages 1-2)
- Pil-Chp chemosensory/surface sensing system (label) (roberge2024buildingpermits—controlof pages 3-5, geiger2024abacterialsense pages 1-3)
- Bacteroidetes gliding machinery: GldLM motor, multirail/track, SprB adhesin (label; map proteins where possible) (shibata2023filamentousstructuresin pages 1-2, shibata2023filamentousstructuresin pages 5-6)
- Myxococcus gliding: bFACs, AglR/Q/S channel, peptidoglycan coupling (label) (carbo2024alytictransglycosylase pages 1-2)

**Genes/proteins (UniProt label nodes; taxon-specific grounding may be added during curation):**
- PilB (T4P extension ATPase), PilT (retraction ATPase), PilU (accessory retraction) (roberge2024buildingpermits—controlof pages 1-3, geiger2024abacterialsense pages 1-3)
- PilJ (methyl-accepting chemoreceptor), ChpA, PilG/PilH, CyaB, Vfr (roberge2024buildingpermits—controlof pages 3-5, geiger2024abacterialsense pages 1-3)
- IsmP (CHASE4 sensor), ImcA (diguanylate cyclase) (zhan2024acdigmpsignaling pages 1-2)
- GldL, GldM, GldJ, SprB (shibata2023filamentousstructuresin pages 1-2, shibata2023filamentousstructuresin pages 5-6)
- AgmT (lytic transglycosylase), MltG (heterologous rescue) (carbo2024alytictransglycosylase pages 1-2)
- Aap pili system components: AapF (assembly), AapA/AapB/AapX (components affecting twitching) (charlesorszag2024adhesionpilusretraction pages 1-2, charlesorszag2024adhesionpilusretraction pages 3-4)
- MinD2 (ParA/MinD ATPase; positions chemotaxis arrays/archaellum motors) (patro2024mind2modulatescell pages 1-2)

**Chemicals / environmental factors (CHEBI / ENVO / label):**
- c-di-GMP (CHEBI:23411) (zhan2024acdigmpsignaling pages 1-2)
- cAMP (CHEBI:17489) (roberge2024buildingpermits—controlof pages 3-5)
- iron (label; Fe3+/heme as signal) (zhan2024acdigmpsignaling pages 1-2)
- Ca2+ (CHEBI:29108) (li2024theeffectof pages 1-2)
- surfactants / rhamnolipids (label/CHEBI where possible) (warrell2024interspeciessurfactantsserve pages 15-17)
- mucin (label/CHEBI:53448 candidate) (warrell2024interspeciessurfactantsserve pages 22-22)
- bile salts (CHEBI:3098) and detergents (ohara2024surfacehydrophilicitypromotes pages 1-2)
- surface hydrophilicity (PATO:0002208 candidate) (ohara2024surfacehydrophilicitypromotes pages 1-2)

---

### B) Candidate causal edges (evidence-backed)
The table below provides a starting set of subject–predicate–object triples with snippets and notes suitable for curation into `motility.yaml`.

| Subject (node) | Predicate | Object (node) | Grounding suggestions (CURIEs) | Evidence snippet (verbatim short quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|---|
| Flagellum | enables | swimming motility | GO:0009288; GO:0060284 | “Swimming is driven by a single polar flagellum in liquid” (warrell2024interspeciessurfactantsserve pages 1-2) | DOI:10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | General bacterial edge; broadly curatable. |
| Flagella | contributes_to | swarming motility | GO:0009288; GO:0009405 | “Swarming is a social tendril-forming behavior on semi-solid surfaces that requires flagella” (warrell2024interspeciessurfactantsserve pages 1-2) | DOI:10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Surface-specific phenotype; distinguish from swimming. |
| Rhamnolipid production | required_for | swarming motility | CHEBI:63506; label:swarming motility | “Swarming … requires flagella and rhamnolipid surfactant production” (warrell2024interspeciessurfactantsserve pages 1-2) | DOI:10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Strong for P. aeruginosa; taxon bias. |
| Functional flagella | required_for | surface spreading motility | GO:0009288; label:surface spreading motility | “surface spreading is an active, surfactant-enabled motility that requires functional flagella” (warrell2024interspeciessurfactantsserve pages 15-17) | DOI:10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Distinct from sliding; likely assay/species specific. |
| Mucin | promotes | surfing / rapid surface motility | CHEBI:53448; label:surfing motility | “Mucin promotes rapid surface motility” (warrell2024interspeciessurfactantsserve pages 22-22) | DOI:10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Boundary case: subtype of surface motility, not universal “motility.” |
| Exogenous surfactants | enable | surface spreading motility | label:surfactant; label:surface spreading motility | “Exogenous surfactants … enable surface spreading even on hard agar” (warrell2024interspeciessurfactantsserve pages 15-17) | DOI:10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Environmental factor; useful assay/context node. |
| Type IV pilus | drives | twitching motility | GO:0009289; GO:0001539 | “Twitching motility is a form of bacterial surface translocation powered by the type IV pilus (T4P)” (ohara2024surfacehydrophilicitypromotes pages 1-2) | DOI:10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Strong, broad bacterial statement. |
| PilB | drives_extension_of | type IV pilus | UniProt:label-only PilB; GO:0043540 | “PilB is the homohexameric extension ATPase” (roberge2024buildingpermits—controlof pages 1-3) | DOI:10.1128/jb.00359-24, 2024, https://doi.org/10.1128/jb.00359-24 | Conserved T4P extension ATPase; grounding may be taxon-specific. |
| PilT | drives_retraction_of | type IV pilus | UniProt:label-only PilT; GO:0043540 | “Retraction is carried out by the antagonistic ATPase PilT” (roberge2024buildingpermits—controlof pages 1-3) | DOI:10.1128/jb.00359-24, 2024, https://doi.org/10.1128/jb.00359-24 | Strong mechanistic edge. |
| PilU | supports | type IV pilus retraction | UniProt:label-only PilU | “PilT (primary) and PilU (accessory)” (geiger2024abacterialsense pages 1-3) | DOI:10.1128/jb.00442-23, 2024, https://doi.org/10.1128/jb.00442-23 | Accessory role; species/system dependent. |
| Type IV pilus retraction | generates | twitching motility | GO:0001539; label:T4P retraction | “T4P retraction generates the pulling forces underlying twitching motility” (geiger2024abacterialsense pages 1-3) | DOI:10.1128/jb.00442-23, 2024, https://doi.org/10.1128/jb.00442-23 | Core causal edge for twitching. |
| PilJ | signals_via | Pil-Chp system | UniProt:label-only PilJ; label:Pil-Chp system | “signals are sensed by the methyl-accepting chemotactic receptor PilJ and transduced via the Pil-Chp system” (roberge2024buildingpermits—controlof pages 3-5) | DOI:10.1128/jb.00359-24, 2024, https://doi.org/10.1128/jb.00359-24 | Chemosensory/surface sensing edge; may be Pseudomonas-focused. |
| Pil-Chp system | increases | cAMP | label:Pil-Chp system; CHEBI:17489 | “PilG activates adenylate cyclase CyaB, increasing intracellular cAMP” (roberge2024buildingpermits—controlof pages 3-5) | DOI:10.1128/jb.00359-24, 2024, https://doi.org/10.1128/jb.00359-24 | Can optionally decompose to PilG→CyaB→cAMP. |
| cAMP | activates | Vfr | CHEBI:17489; UniProt:label-only Vfr | “cAMP … with the transcription factor Vfr” (roberge2024buildingpermits—controlof pages 3-5) | DOI:10.1128/jb.00359-24, 2024, https://doi.org/10.1128/jb.00359-24 | In source as cAMP/Vfr complex; predicate simplified. |
| Vfr | upregulates | T4P-associated gene expression | UniProt:label-only Vfr; GO:0045893; label:T4P-associated genes | “cAMP, which with the transcription factor Vfr upregulates T4P-associated genes” (roberge2024buildingpermits—controlof pages 3-5) | DOI:10.1128/jb.00359-24, 2024, https://doi.org/10.1128/jb.00359-24 | Regulatory edge; transcriptional effect. |
| Surface hydrophilicity | promotes | twitching motility | PATO:0002208; GO:0001539 | “altering the surface hydrophilicity of a twitching surface significantly impacts T4P functionality” (ohara2024surfacehydrophilicitypromotes pages 1-2) | DOI:10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Physical environmental factor; assay-context important. |
| Bile salts | enhance | twitching motility | CHEBI:3098; GO:0001539 | “bile salts and other detergents augment the twitching” (ohara2024surfacehydrophilicitypromotes pages 1-2) | DOI:10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Likely mediated by surface physicochemistry, not direct signaling. |
| Detergents | promote | twitching motility | CHEBI:27780; GO:0001539 | “other detergents promoted twitching like bile salts” (ohara2024surfacehydrophilicitypromotes pages 1-2) | DOI:10.1128/msphere.00390-24, 2024, https://doi.org/10.1128/msphere.00390-24 | Context/assay specific. |
| Iron-bound IsmP | inhibits_interaction_with | ImcA | UniProt:label-only IsmP; UniProt:label-only ImcA | “Binding of iron to the CHASE4 domain of IsmP inhibits the IsmP-ImcA interaction” (zhan2024acdigmpsignaling pages 1-2) | DOI:10.1038/s41467-024-46149-3, 2024, https://doi.org/10.1038/s41467-024-46149-3 | Upstream environmental sensing edge. |
| IsmP–ImcA dissociation | increases | c-di-GMP synthesis | label:IsmP-ImcA interaction; CHEBI:23411 | “leads to increased c-di-GMP synthesis by ImcA” (zhan2024acdigmpsignaling pages 1-2) | DOI:10.1038/s41467-024-46149-3, 2024, https://doi.org/10.1038/s41467-024-46149-3 | Mechanistic intermediary; may also represent as ImcA activity edge. |
| Elevated c-di-GMP | reduces | bacterial motility | CHEBI:23411; label:motility | “promoting bioﬁlm formation and reducing bacterial motility” (zhan2024acdigmpsignaling pages 1-2) | DOI:10.1038/s41467-024-46149-3, 2024, https://doi.org/10.1038/s41467-024-46149-3 | Strong but phenotype-generic; species context P. aeruginosa. |
| ArgR | represses | diguanylate cyclase expression | UniProt:label-only ArgR; EC:2.7.7.65 | “ArgR represses diguanylate cyclase expression” (wang2024argrregulatesmotility pages 1-2) | DOI:10.1038/s42003-024-07392-y, 2024, https://doi.org/10.1038/s42003-024-07392-y | Upstream regulatory edge in Aeromonas veronii. |
| Reduced diguanylate cyclase expression | lowers | c-di-GMP level | EC:2.7.7.65; CHEBI:23411 | “lowering c-di-GMP” (wang2024argrregulatesmotility pages 1-2) | DOI:10.1038/s42003-024-07392-y, 2024, https://doi.org/10.1038/s42003-024-07392-y | Straightforward biochemical consequence. |
| Lower c-di-GMP | relieves_inhibition_of | motility | CHEBI:23411; label:motility | “relieving its inhibition on motility” (wang2024argrregulatesmotility pages 1-2) | DOI:10.1038/s42003-024-07392-y, 2024, https://doi.org/10.1038/s42003-024-07392-y | Good generic c-di-GMP→motility edge. |
| Ca2+ | enhances | swimming motility | CHEBI:29108; GO:0060284 | “Ca2+ ‘significantly enhanced’ … swimming motility” (li2024theeffectof pages 1-2) | DOI:10.3389/fmicb.2024.1340429, 2024, https://doi.org/10.3389/fmicb.2024.1340429 | Species-specific (Vibrio parahaemolyticus RIMD2210633). |
| Ca2+ | increases | c-di-GMP production | CHEBI:29108; CHEBI:23411 | “Ca2+ ‘significantly enhanced’ c-di-GMP production” (li2024theeffectof pages 1-2) | DOI:10.3389/fmicb.2024.1340429, 2024, https://doi.org/10.3389/fmicb.2024.1340429 | Not universal directionality across taxa; curate as context-specific. |
| GldLM proton motor | drives | SprB helical motion | UniProt:label-only GldL; UniProt:label-only GldM; UniProt:Q5NIF3? candidate SprB | “the GldLM complex is fueled by the proton gradient to drive SprB helical motion” (shibata2023filamentousstructuresin pages 1-2) | DOI:10.1038/s42003-023-04472-3, 2023, https://doi.org/10.1038/s42003-023-04472-3 | Strong Bacteroidetes gliding edge. |
| SprB movement along helical track | enables | gliding motility | label:SprB helical-loop track; GO:0097588 | “SprB molecules that engage the substratum convert that motion into cell rotation and translocation” (shibata2023filamentousstructuresin pages 5-6) | DOI:10.1038/s42003-023-04472-3, 2023, https://doi.org/10.1038/s42003-023-04472-3 | Good mechanistic edge for Flavobacterium-like gliding. |
| Gld proteins | required_for | multirail structure formation | label:Gld proteins; label:multirail structure | “multiple Gld proteins are required for formation of the multirail” (shibata2023filamentousstructuresin pages 5-6) | DOI:10.1038/s42003-023-04472-3, 2023, https://doi.org/10.1038/s42003-023-04472-3 | Structural intermediate in gliding mechanism. |
| AgmT lytic transglycosylase activity | enables | bFAC–peptidoglycan coupling | UniProt:label-only AgmT; EC:4.2.2.-; GO:0009274 | “AgmT … couples bFACs to PG” (carbo2024alytictransglycosylase pages 1-2) | DOI:10.7554/elife.99273.1, 2024, https://doi.org/10.7554/elife.99273.1 | Myxococcus-specific; strong mechanistic support. |
| bFAC–peptidoglycan coupling | required_for | gliding motility | label:bacterial focal adhesion complex; GO:0097588 | “gliding motors fail to connect to PG and cannot assemble into bFACs” (carbo2024alytictransglycosylase pages 1-2) | DOI:10.7554/elife.99273.1, 2024, https://doi.org/10.7554/elife.99273.1 | Curate as Myxococcus xanthus-specific. |
| N-linked tetrasaccharides on archaellins | prevent | archaellum filament bundling | label:N-linked tetrasaccharides; label:archaellum filament bundling | “act as physical spacers that minimize the archaellum filament aggregation” (sofer2024perturbednglycosylationof pages 1-2) | DOI:10.1038/s41467-024-50277-1, 2024, https://doi.org/10.1038/s41467-024-50277-1 | Archaeal post-translational modification edge. |
| Reduced archaellum bundling | improves | cell motility | label:archaellum filament bundling; label:motility | “loss/truncation of these glycans compromises motility” (sofer2024perturbednglycosylationof pages 1-2) | DOI:10.1038/s41467-024-50277-1, 2024, https://doi.org/10.1038/s41467-024-50277-1 | Inferred converse from mutant phenotype; note inference. |
| MinD2 | positions | chemotaxis arrays and archaellum motors | UniProt:label-only MinD2; GO:0007165; label:archaellum motor | “impacts cell shape and motility by mispositioning the chemotaxis arrays and archaellum motors” (patro2024mind2modulatescell pages 1-2) | DOI:10.3389/fmicb.2024.1474570, 2024, https://doi.org/10.3389/fmicb.2024.1474570 | Spatial organization edge in Haloferax volcanii. |
| Proper positioning of chemotaxis arrays/archaellum motors | supports | archaeal swimming motility | label:chemotaxis array positioning; label:archaellum motor positioning; GO:0060284 | “deletion of minD4 reduces archaeal swimming motility due to mispositioning of chemotaxis arrays and archaellum motors” (patro2024mind2modulatescell pages 1-2) | DOI:10.3389/fmicb.2024.1474570, 2024, https://doi.org/10.3389/fmicb.2024.1474570 | Uses supporting statement from related MinD homolog; moderate inference for generic positioning node. |
| Aap pili retraction | powers | twitching motility | label:Aap pilus; GO:0001539 | “move around by retracting surface-adhered pili” (charlesorszag2024adhesionpilusretraction pages 4-6) | DOI:10.1038/s41467-024-49101-7, 2024, https://doi.org/10.1038/s41467-024-49101-7 | Strong archaeal twitching edge. |
| AapF | required_for | archaeal twitching motility | UniProt:label-only AapF; GO:0001539 | “deleting the adhesion pilus assembly protein AapF (ΔaapF) abolishes twitching” (charlesorszag2024adhesionpilusretraction pages 1-2) | DOI:10.1038/s41467-024-49101-7, 2024, https://doi.org/10.1038/s41467-024-49101-7 | Strong but specific to Sulfolobus acidocaldarius. |
| Archaellum | enables | archaeal swimming motility | GO:0060284; label:archaellum | “The archaellum … enables cell motility in archaea” (sofer2024perturbednglycosylationof pages 1-2) | DOI:10.1038/s41467-024-50277-1, 2024, https://doi.org/10.1038/s41467-024-50277-1 | Broad archaeal analogue of flagellum; curatable. |


*Table: This table compiles candidate subject-predicate-object edges for microbial motility curation, spanning flagellar, pili-based, gliding, archaeal, and environmentally regulated mechanisms. It is useful as a starting set of evidence-backed, ontology-aware causal statements for TraitMech graph assembly.*

Key mechanistic schematic supporting the PilB/PilT + Pil-Chp→cAMP/Vfr model is available as a figure crop. (roberge2024buildingpermits—controlof media 4513e20a)

---

## Warnings / claims not ready to curate (or curate as uncertain)
1. **Surface spreading vs sliding vs swarming**: Some surface migration modes can occur without canonical appendages or may be strongly condition-dependent; treat “surface spreading” labels as **context-qualified** and avoid promoting them to the general motility class without mechanistic confirmation per taxon/assay. (warrell2024interspeciessurfactantsserve pages 15-17)
2. **Surfactant effects**: Exogenous surfactants enabling motility are compelling but can be **species-specific** and depend on surfactant properties (charge; inhibitors such as CTAB). Curate with explicit environmental context. (warrell2024interspeciessurfactantsserve pages 15-17)
3. **c-di-GMP → motility directionality is not universal**: While high c-di-GMP often correlates with sessility and reduced motility, some systems show more complex or even opposite relationships (e.g., Ca2+ in *V. parahaemolyticus* increases c-di-GMP and swimming). Curate these as **taxon- and condition-specific** edges. (zhan2024acdigmpsignaling pages 1-2, li2024theeffectof pages 1-2)
4. **Archaeal PilT-independent retraction mechanism**: The phenotype is strongly supported, but the molecular motor mechanism remains unresolved; model the retraction event and the absence of PilT as an open mechanistic gap. (charlesorszag2024adhesionpilusretraction pages 4-6, charlesorszag2024adhesionpilusretraction pages 1-2)

---

## DOI-first bibliography (with dates and URLs)

- Warrell DL, Zarrella TM, Machalek C, Khare A. **Interspecies surfactants serve as public goods enabling surface motility in *Pseudomonas aeruginosa*.** *Journal of Bacteriology* (Oct 2024). DOI:10.1128/jb.00281-24. https://doi.org/10.1128/jb.00281-24 (warrell2024interspeciessurfactantsserve pages 15-17)
- O’Hara MT, Shimozono TM, Dye KJ, Harris D, Yang Z. **Surface hydrophilicity promotes bacterial twitching motility.** *mSphere* (Sep 2024). DOI:10.1128/msphere.00390-24. https://doi.org/10.1128/msphere.00390-24 (ohara2024surfacehydrophilicitypromotes pages 1-2)
- Roberge NA, Burrows LL. **Building permits—control of type IV pilus assembly by PilB and its cofactors.** *Journal of Bacteriology* (Dec 2024). DOI:10.1128/jb.00359-24. https://doi.org/10.1128/jb.00359-24 (roberge2024buildingpermits—controlof pages 1-3, roberge2024buildingpermits—controlof pages 3-5, roberge2024buildingpermits—controlof media 4513e20a)
- Geiger CJ, Wong GCL, O’Toole GA. **A bacterial sense of touch: T4P retraction motor as a means of surface sensing by *Pseudomonas aeruginosa* PA14.** *Journal of Bacteriology* (Jul 2024). DOI:10.1128/jb.00442-23. https://doi.org/10.1128/jb.00442-23 (geiger2024abacterialsense pages 1-3)
- Zhan X, Zhang K, Wang C, et al. **A c-di-GMP signaling module controls responses to iron in *Pseudomonas aeruginosa*.** *Nature Communications* (Feb 2024). DOI:10.1038/s41467-024-46149-3. https://doi.org/10.1038/s41467-024-46149-3 (zhan2024acdigmpsignaling pages 1-2, zhan2024acdigmpsignaling pages 9-10)
- Li X, Chang J, Zhang M, et al. **The effect of environmental calcium on gene expression, biofilm formation and virulence of *Vibrio parahaemolyticus*.** *Frontiers in Microbiology* (May 2024). DOI:10.3389/fmicb.2024.1340429. https://doi.org/10.3389/fmicb.2024.1340429 (li2024theeffectof pages 1-2, li2024theeffectof pages 2-3)
- Wang Z, Tang Y, Li H, et al. **ArgR regulates motility and virulence through positive control of flagellar genes and inhibition of diguanylate cyclase expression in *Aeromonas veronii*.** *Communications Biology* (Dec 2024). DOI:10.1038/s42003-024-07392-y. https://doi.org/10.1038/s42003-024-07392-y (wang2024argrregulatesmotility pages 1-2)
- Shibata S, Tahara YO, Katayama E, et al. **Filamentous structures in the cell envelope are associated with Bacteroidetes gliding machinery.** *Communications Biology* (Jan 2023). DOI:10.1038/s42003-023-04472-3. https://doi.org/10.1038/s42003-023-04472-3 (shibata2023filamentousstructuresin pages 1-2, shibata2023filamentousstructuresin pages 5-6)
- Ramirez Carbo C, Faromiki OG, Nan B. **A lytic transglycosylase connects bacterial focal adhesion complexes to the peptidoglycan cell wall.** *eLife* (Jul 2024). DOI:10.7554/elife.99273.1. https://doi.org/10.7554/elife.99273.1 (carbo2024alytictransglycosylase pages 1-2)
- Charles-Orszag A, van Wolferen M, Lord SJ, Albers S-V, Mullins RD. **Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon *Sulfolobus acidocaldarius*.** *Nature Communications* (Jun 2024). DOI:10.1038/s41467-024-49101-7. https://doi.org/10.1038/s41467-024-49101-7 (charlesorszag2024adhesionpilusretraction pages 1-2, charlesorszag2024adhesionpilusretraction pages 4-6)
- Sofer S, Vershinin Z, Mashni L, et al. **Perturbed N-glycosylation of *Halobacterium salinarum* archaellum filaments leads to filament bundling and compromised cell motility.** *Nature Communications* (Jul 2024). DOI:10.1038/s41467-024-50277-1. https://doi.org/10.1038/s41467-024-50277-1 (sofer2024perturbednglycosylationof pages 1-2)
- Patro M, Grünberger F, Sivabalasarma S, et al. **MinD2 modulates cell shape and motility in the archaeon *Haloferax volcanii*.** *Frontiers in Microbiology* (Nov 2024). DOI:10.3389/fmicb.2024.1474570. https://doi.org/10.3389/fmicb.2024.1474570 (patro2024mind2modulatescell pages 1-2)
- Gaines MC, Isupov MN, McLaren M, et al. **Towards a molecular picture of the archaeal cell surface.** *Nature Communications* (Nov 2024). DOI:10.1038/s41467-024-53986-9. https://doi.org/10.1038/s41467-024-53986-9 (gaines2024towardsamolecular pages 1-2)



References

1. (warrell2024interspeciessurfactantsserve pages 1-2): Delayna L. Warrell, Tiffany M. Zarrella, Christopher Machalek, and Anupama Khare. Interspecies surfactants serve as public goods enabling surface motility in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00281-24, doi:10.1128/jb.00281-24. This article has 13 citations and is from a peer-reviewed journal.

2. (warrell2024interspeciessurfactantsserve pages 15-17): Delayna L. Warrell, Tiffany M. Zarrella, Christopher Machalek, and Anupama Khare. Interspecies surfactants serve as public goods enabling surface motility in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00281-24, doi:10.1128/jb.00281-24. This article has 13 citations and is from a peer-reviewed journal.

3. (ohara2024surfacehydrophilicitypromotes pages 1-2): Megan T. O'Hara, Tori M. Shimozono, Keane J. Dye, David Harris, and Zhaomin Yang. Surface hydrophilicity promotes bacterial twitching motility. Sep 2024. URL: https://doi.org/10.1128/msphere.00390-24, doi:10.1128/msphere.00390-24. This article has 10 citations and is from a peer-reviewed journal.

4. (jin2024microbesinporous pages 9-14): Chenyu Jin and Anupam Sengupta. Microbes in porous environments: from active interactions to emergent feedback. Biophysical Reviews, 16:173-188, Apr 2024. URL: https://doi.org/10.1007/s12551-024-01185-7, doi:10.1007/s12551-024-01185-7. This article has 42 citations and is from a peer-reviewed journal.

5. (shibata2023filamentousstructuresin pages 1-2): Satoshi Shibata, Yuhei O. Tahara, Eisaku Katayama, Akihiro Kawamoto, Takayuki Kato, Yongtao Zhu, Daisuke Nakane, Keiichi Namba, Makoto Miyata, Mark J. McBride, and Koji Nakayama. Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery. Communications Biology, Jan 2023. URL: https://doi.org/10.1038/s42003-023-04472-3, doi:10.1038/s42003-023-04472-3. This article has 20 citations and is from a peer-reviewed journal.

6. (carbo2024alytictransglycosylase pages 1-2): Carlos Ramirez Carbo, Olalekan G Faromiki, and Beiyan Nan. A lytic transglycosylase connects bacterial focal adhesion complexes to the peptidoglycan cell wall. Jul 2024. URL: https://doi.org/10.7554/elife.99273.1, doi:10.7554/elife.99273.1.

7. (gaines2024towardsamolecular pages 1-2): Matthew C. Gaines, Michail N. Isupov, Mathew McLaren, Clara L. Mollat, Risat Ul Haque, Jake K. Stephenson, Shamphavi Sivabalasarma, Cyril Hanus, Daniel Kattnig, Vicki A. M. Gold, Sonja Albers, and Bertram Daum. Towards a molecular picture of the archaeal cell surface. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53986-9, doi:10.1038/s41467-024-53986-9. This article has 10 citations and is from a highest quality peer-reviewed journal.

8. (charlesorszag2024adhesionpilusretraction pages 1-2): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and R. Dyche Mullins. Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon sulfolobus acidocaldarius. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49101-7, doi:10.1038/s41467-024-49101-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

9. (zhan2024acdigmpsignaling pages 1-2): Xueliang Zhan, Kuo Zhang, Chenchen Wang, Qiao Fan, Xiu-Shan Tang, Xi Zhang, Ke Wang, Yang Fu, and Haihua Liang. A c-di-gmp signaling module controls responses to iron in pseudomonas aeruginosa. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46149-3, doi:10.1038/s41467-024-46149-3. This article has 53 citations and is from a highest quality peer-reviewed journal.

10. (li2024theeffectof pages 1-2): Xue Li, Jingyang Chang, Miaomiao Zhang, Yining Zhou, Tingting Zhang, Yiquan Zhang, and Renfei Lu. The effect of environmental calcium on gene expression, biofilm formation and virulence of vibrio parahaemolyticus. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1340429, doi:10.3389/fmicb.2024.1340429. This article has 10 citations and is from a peer-reviewed journal.

11. (geiger2024abacterialsense pages 1-3): C. J. Geiger, G. C. L. Wong, and G. A. O'Toole. A bacterial sense of touch: t4p retraction motor as a means of surface sensing by <i>pseudomonas aeruginosa</i> pa14. Journal of Bacteriology, Jul 2024. URL: https://doi.org/10.1128/jb.00442-23, doi:10.1128/jb.00442-23. This article has 21 citations and is from a peer-reviewed journal.

12. (roberge2024buildingpermits—controlof pages 3-5): Nathan A. Roberge and Lori L. Burrows. Building permits—control of type iv pilus assembly by pilb and its cofactors. Dec 2024. URL: https://doi.org/10.1128/jb.00359-24, doi:10.1128/jb.00359-24. This article has 16 citations and is from a peer-reviewed journal.

13. (charlesorszag2024adhesionpilusretraction pages 4-6): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and R. Dyche Mullins. Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon sulfolobus acidocaldarius. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49101-7, doi:10.1038/s41467-024-49101-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

14. (sofer2024perturbednglycosylationof pages 1-2): Shahar Sofer, Zlata Vershinin, Leen Mashni, Ran Zalk, Anat Shahar, Jerry Eichler, and Iris Grossman-Haham. Perturbed n-glycosylation of halobacterium salinarum archaellum filaments leads to filament bundling and compromised cell motility. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50277-1, doi:10.1038/s41467-024-50277-1. This article has 15 citations and is from a highest quality peer-reviewed journal.

15. (roberge2024buildingpermits—controlof pages 1-3): Nathan A. Roberge and Lori L. Burrows. Building permits—control of type iv pilus assembly by pilb and its cofactors. Dec 2024. URL: https://doi.org/10.1128/jb.00359-24, doi:10.1128/jb.00359-24. This article has 16 citations and is from a peer-reviewed journal.

16. (roberge2024buildingpermits—controlof media 4513e20a): Nathan A. Roberge and Lori L. Burrows. Building permits—control of type iv pilus assembly by pilb and its cofactors. Dec 2024. URL: https://doi.org/10.1128/jb.00359-24, doi:10.1128/jb.00359-24. This article has 16 citations and is from a peer-reviewed journal.

17. (zhan2024acdigmpsignaling pages 9-10): Xueliang Zhan, Kuo Zhang, Chenchen Wang, Qiao Fan, Xiu-Shan Tang, Xi Zhang, Ke Wang, Yang Fu, and Haihua Liang. A c-di-gmp signaling module controls responses to iron in pseudomonas aeruginosa. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-46149-3, doi:10.1038/s41467-024-46149-3. This article has 53 citations and is from a highest quality peer-reviewed journal.

18. (shibata2023filamentousstructuresin pages 5-6): Satoshi Shibata, Yuhei O. Tahara, Eisaku Katayama, Akihiro Kawamoto, Takayuki Kato, Yongtao Zhu, Daisuke Nakane, Keiichi Namba, Makoto Miyata, Mark J. McBride, and Koji Nakayama. Filamentous structures in the cell envelope are associated with bacteroidetes gliding machinery. Communications Biology, Jan 2023. URL: https://doi.org/10.1038/s42003-023-04472-3, doi:10.1038/s42003-023-04472-3. This article has 20 citations and is from a peer-reviewed journal.

19. (charlesorszag2024adhesionpilusretraction pages 3-4): Arthur Charles-Orszag, Marleen van Wolferen, Samuel J. Lord, Sonja-Verena Albers, and R. Dyche Mullins. Adhesion pilus retraction powers twitching motility in the thermoacidophilic crenarchaeon sulfolobus acidocaldarius. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49101-7, doi:10.1038/s41467-024-49101-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

20. (patro2024mind2modulatescell pages 1-2): Megha Patro, Felix Grünberger, Shamphavi Sivabalasarma, Sabrina Gfrerer, Marta Rodriguez-Franco, Phillip Nußbaum, Dina Grohmann, Solenne Ithurbide, and Sonja-Verena Albers. Mind2 modulates cell shape and motility in the archaeon haloferax volcanii. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1474570, doi:10.3389/fmicb.2024.1474570. This article has 7 citations and is from a peer-reviewed journal.

21. (warrell2024interspeciessurfactantsserve pages 22-22): Delayna L. Warrell, Tiffany M. Zarrella, Christopher Machalek, and Anupama Khare. Interspecies surfactants serve as public goods enabling surface motility in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00281-24, doi:10.1128/jb.00281-24. This article has 13 citations and is from a peer-reviewed journal.

22. (wang2024argrregulatesmotility pages 1-2): Zucheng Wang, Yanqiong Tang, Hong Li, Juanjuan Li, Xue Chi, Xiang Ma, and Zhu Liu. Argr regulates motility and virulence through positive control of flagellar genes and inhibition of diguanylate cyclase expression in aeromonas veronii. Communications Biology, Dec 2024. URL: https://doi.org/10.1038/s42003-024-07392-y, doi:10.1038/s42003-024-07392-y. This article has 7 citations and is from a peer-reviewed journal.

23. (li2024theeffectof pages 2-3): Xue Li, Jingyang Chang, Miaomiao Zhang, Yining Zhou, Tingting Zhang, Yiquan Zhang, and Renfei Lu. The effect of environmental calcium on gene expression, biofilm formation and virulence of vibrio parahaemolyticus. Frontiers in Microbiology, May 2024. URL: https://doi.org/10.3389/fmicb.2024.1340429, doi:10.3389/fmicb.2024.1340429. This article has 10 citations and is from a peer-reviewed journal.