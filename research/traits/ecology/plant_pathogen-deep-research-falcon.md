---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:44:24.107353'
end_time: '2026-06-17T20:59:40.204280'
duration_seconds: 916.1
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: plant pathogen
  trait_identifier: METPO:1004003
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: plant_pathogen
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pathogen that infects organisms in the kingdom Viridiplantae.
  parent_traits: METPO:1004000
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion
    (Plant-pathology review supports type III secretion of effectors as the central
    mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535:
    cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading
    enzymes as essential virulence factors of bacterial phytopathogens.)'
  causal_graph_summary: 'plant_pathogen_t3ss_effector_program: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** plant pathogen
- **METPO identifier:** METPO:1004003
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Viridiplantae.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion (Plant-pathology review supports type III secretion of effectors as the central mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535: cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading enzymes as essential virulence factors of bacterial phytopathogens.)
- **Existing causal graph summary:** plant_pathogen_t3ss_effector_program: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **plant pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/plant_pathogen.yaml`.

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
- **Trait label:** plant pathogen
- **METPO identifier:** METPO:1004003
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pathogen that infects organisms in the kingdom Viridiplantae.
- **Parent traits:** METPO:1004000
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.phyto.43.040204.135923: type III secretion (Plant-pathology review supports type III secretion of effectors as the central mechanism by which bacterial plant pathogens manipulate plant cells.) | DOI:10.1146/annurev.micro.55.1.535: cell-wall-degrading enzymes (Plant-pathogen review supports secreted plant-cell-wall-degrading enzymes as essential virulence factors of bacterial phytopathogens.)
- **Existing causal graph summary:** plant_pathogen_t3ss_effector_program: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **plant pathogen** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/plant_pathogen.yaml`.

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


## Microbial Trait Causal Graph Research Report: **Plant pathogen** (METPO:1004003)

### 1) Scope summary (Trait scope and boundary cases)

**Trait definition (curation-ready):** The METPO trait **plant pathogen (METPO:1004003)** represents a microbial ecological phenotype/class describing organisms that **infect, multiply on/in, and cause disease in hosts from the kingdom Viridiplantae** (plants). Operationally, the trait is often evidenced by **successful host colonization, symptom development (e.g., wilting, necrosis, rot), and/or transmissibility**, which are typically underpinned by conserved virulence strategies such as secretion/delivery of effectors, enzymatic degradation of plant barriers, and suppression/manipulation of plant immunity (hajjihedfi2024plantdiseasespathogenicity pages 2-4, kvitko2023discoveryofthe pages 1-2).

**Boundary cases / nearby traits:**
- **Nonpathogenic endophytes vs. pathogens (same species complex):** Nonpathogenic endophytic strains of *Fusarium oxysporum* can elicit plant defense responses similar to pathogenic infections (e.g., increased PR gene transcripts), yet show **restricted colonization and lower biomass** relative to pathogenic strains; one cited comparison reports a pathogen producing **~10× more biomass** at 2 weeks post-inoculation (wojtasik2024endophyticnonpathogenicfusarium pages 1-2, wojtasik2024endophyticnonpathogenicfusarium pages 2-3). This supports a boundary distinction based on **vascular invasion and in planta proliferation**, not merely immune activation.
- **Assay-based boundary (HR infiltration assay):** A classic operational distinction for bacterial plant pathogens is induction of the **hypersensitive reaction (HR)** in nonhost tobacco after high-density syringe infiltration. Klement’s assay used ≥ **5 × 10^6 cells/mL**, distinguishing pathogens (e.g., *Pseudomonas syringae*) from nonpathogens (e.g., *P. fluorescens*) (kvitko2023discoveryofthe pages 1-2). Importantly, boundary/conditional behavior exists: **co-inoculation with a compatible pathogen can enable growth of co-inoculated nonpathogens** by altering the leaf environment (kvitko2023discoveryofthe pages 1-2), cautioning that “nonpathogen” may be context-dependent.

**Distinguish from nearby ecological traits** (curation guidance):
- **Plant-associated commensal/epiphyte:** colonizes surfaces without causing disease.
- **Endophyte:** colonizes internal tissues without disease; may still induce defense priming.
- **Opportunistic/conditional pathogen:** disease depends strongly on host genotype, stress, or co-infection; may share partial virulence modules.

### 2) Key concepts and current mechanistic understanding (2023–2024 emphasis)

#### 2.1 Bacterial plant pathogenicity: T3SS effectors as central virulence determinants
Gram-negative bacterial phytopathogens commonly rely on the **Hrp (hrp/hrc) type III secretion system (T3SS)** to inject effectors into plant cells. The *hrp* gene clusters encode a T3SS that “injects Avr (now ‘effector’) proteins into plant cells,” and these systems are broadly distributed and often acquired on pathogenicity islands via horizontal gene transfer (kvitko2023discoveryofthe pages 1-2). A key conceptual point is that T3SS effectors collectively contribute to pathogenicity by **subverting plant defenses**; Kvitko & Collmer emphasize that a primary function of phytopathogen effectors is to **subvert defenses induced by recognition of conserved microbial features outside plant cells** (i.e., PTI) (kvitko2023discoveryofthe pages 1-2).

A schematic of the Hrp T3SS gene cluster and injection apparatus is available in the retrieved figure (kvitko2023discoveryofthe media 08856614).

#### 2.2 Biofilms, quorum sensing (QS), and EPS-driven xylem occlusion in vascular pathogens
Biofilm formation is a widely used persistence/colonization strategy in phytopathogenic bacteria. In a 2023 review, biofilms are described as structured communities with an EPS-rich matrix, and QS is noted as required for cooperative biofilm formation; QS regulates production of toxins, enzymes, EPS, and other virulence factors (carezzano2023biofilmformingabilityof pages 5-6). The same review ties biofilm and EPS production to colonization of plant tissues including xylem and apoplast; for example, *Ralstonia solanacearum* “travels to the xylem where it multiplies [and] obstructs the vessels with large amounts of EPS” (carezzano2023biofilmformingabilityof pages 9-11). Vascular biofilms by *Ralstonia*, *Xylella*, and *Pantoea* are linked to wilting disease phenotypes (carezzano2023biofilmformingabilityof pages 6-8).

A 2024 primary study on *Ralstonia pseudosolanacearum* provides mechanistic detail: carbohydrate-binding lectins (LecF, LecX) and exopolysaccharide EPS I have **flow-dependent roles**—they are essential for biofilm development under shear stress similar to xylem flow and contribute to xylem blockage/disrupted sap flow (carter2024lectinsandpolysaccharide pages 1-2).

#### 2.3 Cell-wall-degrading enzymes (CWDEs) and barrier breach
Across bacteria and filamentous pathogens, secretion of **plant cell-wall-degrading enzymes** (CWDEs; e.g., pectinases, cellulases, xylanases, proteases) is repeatedly highlighted as enabling invasion and colonization (hajjihedfi2024plantdiseasespathogenicity pages 2-4). Enzymatic degradation of plant cell walls contributes to penetration, tissue maceration, and necrosis; specific CWDE genes can be virulence determinants in specific taxa (e.g., fungal xylanases affecting virulence and necrosis) (cui2024xylanasevmxyl2is pages 13-13).

#### 2.4 Filamentous pathogens (fungi/oomycetes): effector secretion routes as emerging mechanistic determinants
A 2024 review synthesizes advances in **effector secretion** in fungi and oomycetes: apoplastic effectors often use the conventional **ER–Golgi secretion**, whereas cytoplasmic effectors can be packaged into vesicles that bypass Golgi via **unconventional protein secretion (UPS)** (dulal2024pathsofleast pages 1-2). The same review links regulation of cytoplasmic effector translation/secretion rates to maintenance of the biotrophic interface and successful infection (dulal2024pathsofleast pages 1-2). These are recent, mechanistically specific candidates for inclusion as upstream nodes/edges for filamentous plant-pathogen causal graphs.

#### 2.5 Expert, authoritative mechanistic exemplars: effector–host target immune suppression
A high-confidence, molecularly explicit example is provided by a 2024 *Nature Communications* study on the necrotroph *Sclerotinia sclerotiorum*: the secreted effector **SsPEIE1** is required for full virulence and suppresses plant immunity by interacting with host hypersensitive-induced reaction protein **AtHIR4**, inhibiting AtHIR4 oligomerization and reducing PTI outputs such as ROS bursts and SA-associated immune gene induction (liu2024aneffectoressential pages 1-2). This kind of effector–host-target edge is ideal for TraitMech graphs when taxonomy/host context is represented.

### 3) Recent developments and latest research (prioritizing 2023–2024)

**(i) Mechanistic understanding of secretion and delivery has expanded beyond “effectors exist” to “how they are secreted”:** UPS-mediated cytoplasmic effector secretion in fungi/oomycetes and its translational constraints (codon usage/tRNA modification) are highlighted as mechanistic constraints on pathogenicity (dulal2024pathsofleast pages 1-2).

**(ii) Physical-environment dependence of virulence traits:** Flow/shear effects on *Ralstonia* lectin/EPS-mediated biofilm mechanics show virulence traits can invert between static (root surface) and flowing (xylem) environments, reinforcing the need for ENVO-like environmental nodes (e.g., xylem flow) in causal graphs (carter2024lectinsandpolysaccharide pages 1-2).

**(iii) Increased granularity in effector–host target mechanisms:** The SsPEIE1–AtHIR4 mechanism provides explicit host-pathway readouts (ROS, SA-associated gene induction) linked to effector action and virulence (liu2024aneffectoressential pages 1-2).

### 4) Current applications and real-world implementations

**Biocontrol via quorum quenching / anti-biofilm strategies (evidence of implementability):** Because QS can regulate virulence factors and biofilms in plant pathogens, quorum quenching and biofilm inhibition are active translational areas. The biofilm review emphasizes management challenges posed by biofilm-forming phytopathogens and the role of QS/EPS pathways as intervention points (carezzano2023biofilmformingabilityof pages 6-8, carezzano2023biofilmformingabilityof pages 5-6). Similarly, the *Xanthomonas campestris* black-rot study frames biofilm disruption as practically relevant, linking biofilm control to xylem “unblocking” in planta (fontana2023effectsofflavonoids pages 1-2).

**Effector-informed crop protection (conceptual application):** Effector discovery/prediction and effector biology are increasingly used to inform resistance breeding and targeted interventions, with reviews emphasizing effectors as primary pathogenic “weapons” and key to immune manipulation (liu2023crucialrolesof pages 15-17, santosbriones2024algorithmsforeffector pages 18-19).

### 5) Relevant statistics and data (recent studies/reviews)

A 2024 narrative review synthesizing phytopathogenic bacterial impacts reports:
- **Yield loss up to 100%** in severe scenarios and **economic losses up to $1 billion annually** (context-dependent across crops, regions, and pathogens) (mulungu2024unmaskingthehidden pages 1-2).
- It also summarizes numerous pathogen/crop-specific yield-loss ranges and economic burdens (including multi-hundred-million to multi-billion USD estimates in some cases) (mulungu2024unmaskingthehidden pages 7-9).

These data motivate the trait’s real-world importance and support prioritizing causal mechanisms for intervention.

---

## Candidate causal-graph nodes (grouped by type)

### A) Pathways / modules / processes
- **Type III secretion system (T3SS), Hrp/Hrc** (GO:0030257; GO:0052049) (kvitko2023discoveryofthe pages 1-2, kvitko2023discoveryofthe media 08856614)
- **Biofilm formation** (GO:0042710) (carezzano2023biofilmformingabilityof pages 5-6)
- **Quorum sensing** (label node; varies by taxon: AHL, DSF) (carezzano2023biofilmformingabilityof pages 5-6)
- **c-di-GMP signaling** (label node) controlling EPS/biofilm transitions (carezzano2023biofilmformingabilityof pages 8-9, carezzano2023biofilmformingabilityof pages 5-6)
- **Plant cell wall degradation** (label node; tied to CWDE activity) (hajjihedfi2024plantdiseasespathogenicity pages 2-4)
- **Effector secretion (ER–Golgi vs UPS)** (GO:0006888 for ER→Golgi transport; label node for UPS) (dulal2024pathsofleast pages 1-2)
- **Immune suppression of PTI outputs** (ROS burst, SA-associated gene induction) (liu2024aneffectoressential pages 1-2)

### B) Genes / proteins / complexes (example nodes)
- **hrp/hrc gene cluster** (label node; bacterial pathogenicity island) (kvitko2023discoveryofthe pages 1-2, kvitko2023discoveryofthe media 08856614)
- **Type III effectors (T3Es/T3SEs)** (label node) (kvitko2023discoveryofthe pages 1-2)
- **Lectins LecF/LecX (Ralstonia)** (label node; UniProt grounding needed) (carter2024lectinsandpolysaccharide pages 1-2)
- **EPS I (Ralstonia)** (label node) (carter2024lectinsandpolysaccharide pages 1-2)
- **SsPEIE1 effector** (label node; UniProt grounding needed) (liu2024aneffectoressential pages 1-2)
- **AtHIR4 (plant host target)** (label node) (liu2024aneffectoressential pages 1-2)
- **CWDEs:** pectinase, cellulase, xylanase (enzyme-class nodes; EC grounding often possible but varies) (hajjihedfi2024plantdiseasespathogenicity pages 2-4, cui2024xylanasevmxyl2is pages 13-13)

### C) Chemicals / metabolites / signals
- **N-acyl homoserine lactones (AHLs)** (CHEBI:16698) (carezzano2023biofilmformingabilityof pages 5-6)
- **Oxalic acid** (CHEBI:16995) (liu2024aneffectoressential pages 1-2)
- **Exopolysaccharides (EPS)** (label node; polymer-specific where possible) (carezzano2023biofilmformingabilityof pages 9-11, carezzano2023biofilmformingabilityof pages 5-6)

### D) Environmental / host anatomical context (ENVO-like)
- **Plant xylem (water-transporting vessels)** (label node; ENVO:01000617 suggested) (carezzano2023biofilmformingabilityof pages 9-11, carter2024lectinsandpolysaccharide pages 1-2)
- **Apoplast / intercellular spaces** (label node) (carezzano2023biofilmformingabilityof pages 9-11)
- **Flow/shear stress in xylem** (label node; experimental factor) (carter2024lectinsandpolysaccharide pages 1-2)

---

## Evidence-backed candidate causal edges (curation table)

| Edge (subject–predicate–object) | Node grounding suggestions (CURIEs where available) | Evidence snippet (short quote) | Reference (DOI + URL + year) | Notes/uncertainty |
|---|---|---|---|---|
| hrp/hrc type III secretion system → injects → type III effectors into plant cells | subject: GO:0030257 (protein secretion by the type III secretion system); object: GO:0052049 (interaction with host via protein secreted by type III secretion system); label nodes: hrp/hrc gene cluster, T3Es | “hrp gene clusters encode a type III secretion system (T3SS), which injects Avr (now ‘effector’) proteins into plant cells” (kvitko2023discoveryofthe pages 1-2) | DOI:10.1094/PHYTO-08-22-0292-KD · https://doi.org/10.1094/phyto-08-22-0292-kd · 2023 | Strong, broad bacterial phytopathogen mechanism; especially Gram-negative taxa with Hrp T3SS. |
| type III effector injection → suppresses → PTI / non-HR defenses | subject: GO:0052049; object: GO:0009627 (systemic acquired resistance, imperfect), label node: PTI suppression | “a primary function of phytopathogen effectors is to subvert non-HR defenses resulting from recognition of conserved microbial features outside of plant cells” (kvitko2023discoveryofthe pages 1-2) | DOI:10.1094/PHYTO-08-22-0292-KD · https://doi.org/10.1094/phyto-08-22-0292-kd · 2023 | Strong review support; curate as defense suppression rather than a single host pathway unless host target is known. |
| quorum sensing (AHL/DSF) → positively regulates → biofilm formation | subject: CHEBI:16698 (N-acyl-L-homoserine lactone); label node: DSF family signal; object: GO:0042710 (biofilm formation) | “QS is required for cooperative biofilm formation” and regulates “toxins, enzymes, EPS, virulence factors” (carezzano2023biofilmformingabilityof pages 5-6) | DOI:10.3390/plants12112207 · https://doi.org/10.3390/plants12112207 · 2023 | Broad bacterial trend; signal chemistry varies by taxon (AHL in many Proteobacteria; DSF in Xanthomonas/Ralstonia). |
| quorum sensing / c-di-GMP → positively regulates → EPS production | label nodes: QS, cyclic di-GMP; object: exopolysaccharide biosynthesis | “EPS such as amylovoran, levan, xanthan, stewartan, and cellulose are often regulated by intracellular c-di-GMP and QS” (carezzano2023biofilmformingabilityof pages 8-9) | DOI:10.3390/plants12112207 · https://doi.org/10.3390/plants12112207 · 2023 | Good systems-level edge; specific EPS polymers are taxon-specific. |
| EPS-rich biofilm in xylem → causes → vessel obstruction / reduced water flow | subject: biofilm/EPS matrix; object: ENVO:01000617 (xylem) + label node: xylem occlusion | “travels to the xylem where it multiplies, obstructs the vessels with large amounts of EPS” (carezzano2023biofilmformingabilityof pages 9-11) | DOI:10.3390/plants12112207 · https://doi.org/10.3390/plants12112207 · 2023 | Strong for vascular bacterial pathogens such as Ralstonia; not universal across all plant pathogens. |
| xylem vessel obstruction → causes → wilting disease phenotype | subject: xylem occlusion; object: label node: wilting | vascular biofilms “cause wilting” and “interfere with plant tissue and organ function” (carezzano2023biofilmformingabilityof pages 6-8) | DOI:10.3390/plants12112207 · https://doi.org/10.3390/plants12112207 · 2023 | Strong phenotype-level edge for xylem-colonizing pathogens. |
| plant cell-wall-degrading enzymes (CWDEs) → degrades → plant cell wall | subject: GO:0004553 (hydrolase activity, hydrolyzing O-glycosyl compounds; broad), label nodes: CWDEs/PCWDEs; object: GO:0009505 (plant-type cell wall) | “secretion of cell-wall-degrading enzymes (e.g., pectinase, chitinase, cellulase, protease) that enable invasion and colonization” (hajjihedfi2024plantdiseasespathogenicity pages 2-4) | DOI:10.21608/mb.2024.307263.1134 · https://doi.org/10.21608/mb.2024.307263.1134 · 2024 | Broad, cross-kingdom pathogen mechanism; enzyme class should be refined per taxon. |
| pectinase / cellulase / xylanase / cellobiohydrolase → promotes → invasion and colonization | label nodes: pectinase, cellulase, xylanase, β-1,4-cellobiohydrolase; object: host invasion/colonization | “CWDEs… enable invasion and colonization” (hajjihedfi2024plantdiseasespathogenicity pages 2-4) | DOI:10.21608/mb.2024.307263.1134 · https://doi.org/10.21608/mb.2024.307263.1134 · 2024 | Good generic edge; if curated, consider separate enzyme-specific child edges. |
| β-1,4-cellobiohydrolase CbhA → required for → xylem infection and virulence | subject: label node: CbhA; object: xylem vessel infection / virulence | “The cbhA-deletion mutant (ΔcbhA) lacked the ability to infect xylem vessels and displayed loss of virulence” (carezzano2023biofilmformingabilityof pages 5-6) | DOI:10.1111/mpp.13322 · https://doi.org/10.1111/mpp.13322 · 2023 | Strong but taxon-specific to Ralstonia pseudosolanacearum OE1-1. Mark taxon-specific. |
| xylanase VmXyl2 → contributes to → pathogenicity and cell necrosis | subject: label node: VmXyl2; object: pathogenicity / necrosis | “VmXyl2… considerably reduced the virulence of V. mali… VmXyl2 induces plant cell necrosis” (cui2024xylanasevmxyl2is pages 13-13) | DOI:10.3389/fpls.2024.1342714 · https://doi.org/10.3389/fpls.2024.1342714 · 2024 | Strong for fungal necrotroph Valsa mali; enzyme moonlighting beyond catalytic xylanase activity noted. |
| oxalic acid and CWDEs → facilitate → invasion / host cell death | subject: CHEBI:16995 (oxalic acid) + CWDEs; object: invasion / host cell death | “oxalic acid (OA) and cell-wall-degrading enzymes (CWDEs) … facilitate invasion by lowering pH, sequestering Ca2+, impairing oxidative burst, inducing host cell death” (liu2024aneffectoressential pages 1-2) | DOI:10.1038/s41467-024-53725-0 · https://doi.org/10.1038/s41467-024-53725-0 · 2024 | Strong for Sclerotinia sclerotiorum and related necrotrophs; not universal. |
| apoplastic effector secretion via ER–Golgi → delivers → apoplastic effectors | subject: GO:0006888 (ER to Golgi vesicle-mediated transport); object: apoplastic effector delivery | “apoplastic effectors are secreted via the conventional endoplasmic reticulum (ER)-Golgi pathway” (dulal2024pathsofleast pages 1-2) | DOI:10.1094/MPMI-12-23-0212-CR · https://doi.org/10.1094/mpmi-12-23-0212-cr · 2024 | Strong for fungi/oomycetes; secretion-route edge, not sufficient alone for pathogenicity. |
| unconventional protein secretion (UPS) → delivers → cytoplasmic effectors | subject: label node: unconventional protein secretion; object: cytoplasmic effector delivery | “cytoplasmic effectors are packaged into vesicles that bypass Golgi in an unconventional protein secretion (UPS) pathway” (dulal2024pathsofleast pages 1-2) | DOI:10.1094/MPMI-12-23-0212-CR · https://doi.org/10.1094/mpmi-12-23-0212-cr · 2024 | Strong but currently best established in Magnaporthe and some oomycete models; taxon/lifestyle-specific. |
| cytoplasmic effector delivery → enables → host infection | subject: cytoplasmic effector delivery; object: infection success | effector translation/secretion “fine-tunes cytoplasmic effector translation and secretion rates to maintain biotrophic interfacial complex integrity and permit host infection” (dulal2024pathsofleast pages 1-2) | DOI:10.1094/MPMI-12-23-0212-CR · https://doi.org/10.1094/mpmi-12-23-0212-cr · 2024 | Strong mechanistic statement, especially for Magnaporthe oryzae. |
| SsPEIE1 → inhibits → AtHIR4 oligomerization | subject: label node: SsPEIE1; object: label node: AtHIR4 oligomerization | “SsPEIE1 inhibits AtHIR4 oligomerization-mediated immune responses by interacting with the key immune factor AtHIR4” (liu2024aneffectoressential pages 1-2) | DOI:10.1038/s41467-024-53725-0 · https://doi.org/10.1038/s41467-024-53725-0 · 2024 | Strong direct host-target edge; species-specific but high-value mechanistic exemplar. |
| AtHIR4 oligomerization inhibition → reduces → ROS burst | subject: AtHIR4 oligomerization inhibition; object: GO:0012501 (programmed cell death? not exact), label node: ROS burst | “hir2 and hir4 mutants exhibit suppressed pathogen-associated molecular pattern-triggered reactive oxygen species (ROS) bursts” and this is “phenocopied by the SsPEIE1 transgenic plants” (liu2024aneffectoressential pages 1-2) | DOI:10.1038/s41467-024-53725-0 · https://doi.org/10.1038/s41467-024-53725-0 · 2024 | Strong causal support through mutant/transgenic phenocopy; host-specific. |
| AtHIR4 oligomerization inhibition → reduces → SA-associated immune gene induction | subject: AtHIR4 oligomerization inhibition; object: salicylic-acid-associated immune gene induction | “hir2 and hir4 mutants exhibit suppressed… salicylic acid (SA)-associated immune gene induction, all of which are phenocopied by the SsPEIE1 transgenic plants” (liu2024aneffectoressential pages 1-2) | DOI:10.1038/s41467-024-53725-0 · https://doi.org/10.1038/s41467-024-53725-0 · 2024 | Strong host-specific immune suppression edge. |
| endophytic non-pathogenic Fo47 → induces → PR gene transcripts | subject: label node: Fusarium oxysporum Fo47; object: PR gene induction | “non-pathogenic strains can nonetheless trigger defense responses ‘similar to those seen during pathogenic infections,’ evidenced by increased Pathogenesis-Related (PR) gene transcripts” (wojtasik2024endophyticnonpathogenicfusarium pages 1-2) | DOI:10.3389/fpls.2024.1352105 · https://doi.org/10.3389/fpls.2024.1352105 · 2024 | Boundary-case edge: indicates immune activation without full pathogenicity; should not be used as a positive pathogen determinant. |
| endophytic non-pathogenic Fo47 → remodels → host cell wall | subject: Fo47; object: host cell wall remodeling | “Fo47 induced measurable cell-wall changes (reduced cellulose, altered pectin methylesterification, delayed lignin increase)” (wojtasik2024endophyticnonpathogenicfusarium pages 1-2) | DOI:10.3389/fpls.2024.1352105 · https://doi.org/10.3389/fpls.2024.1352105 · 2024 | Boundary-case: host remodeling can occur in nonpathogenic interactions; curate cautiously as discriminating-negative context. |
| restricted colonization / lower biomass of Fo47 → distinguishes from → pathogenic Fusarium lifestyle | subject: Fo47 restricted colonization; object: pathogenic Fusarium colonization | “endophytic strains are ‘less efficient colonizers than pathogens,’… the pathogenic strain produced ‘10 times’ more biomass” (wojtasik2024endophyticnonpathogenicfusarium pages 1-2, wojtasik2024endophyticnonpathogenicfusarium pages 2-3) | DOI:10.3389/fpls.2024.1352105 · https://doi.org/10.3389/fpls.2024.1352105 · 2024 | Useful warning/boundary edge rather than TraitMech core causal edge; likely annotation/supporting note only. |


*Table: This table lists evidence-backed candidate causal edges for curating the microbial trait 'plant pathogen' into a TraitMech-style graph. It emphasizes central mechanisms and also includes a boundary-case row showing why some host-response features should not be treated as sufficient for pathogenicity.*

Supporting schematic for T3SS structure/gene cluster and effector injection is available as a figure crop (kvitko2023discoveryofthe media 08856614).

---

## Warnings / claims not yet ready for TraitMech curation

1. **Do not treat host immune activation as sufficient for “plant pathogen”:** Nonpathogenic endophytes can induce PR genes and cell-wall remodeling similar to pathogenic infections (wojtasik2024endophyticnonpathogenicfusarium pages 1-2). Such nodes should be used as boundary/negative context rather than positive determinants.
2. **Taxon specificity:** Some strong edges are highly specific (e.g., SsPEIE1→AtHIR4; *Ralstonia* LecF/LecX/EPS I; Valsa VmXyl2). These are valuable mechanistic exemplars but may not generalize across all plant pathogens (liu2024aneffectoressential pages 1-2, carter2024lectinsandpolysaccharide pages 1-2, cui2024xylanasevmxyl2is pages 13-13).
3. **Assay dependence and conditionality:** HR infiltration is a useful operational discriminator, but co-inoculation can allow nonpathogen proliferation; interpret HR and “nonpathogen” labels with ecological context (kvitko2023discoveryofthe pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Kvitko BH, Collmer A. **Discovery of the Hrp Type III Secretion System in Phytopathogenic Bacteria**. *Phytopathology* (Apr 2023). DOI: **10.1094/phyto-08-22-0292-kd**. https://doi.org/10.1094/phyto-08-22-0292-kd (kvitko2023discoveryofthe pages 1-2, kvitko2023discoveryofthe media 08856614)
2. Carezzano ME, et al. **Biofilm-Forming Ability of Phytopathogenic Bacteria: A Review**. *Plants* (Jun 2023). DOI: **10.3390/plants12112207**. https://doi.org/10.3390/plants12112207 (carezzano2023biofilmformingabilityof pages 6-8, carezzano2023biofilmformingabilityof pages 9-11, carezzano2023biofilmformingabilityof pages 5-6)
3. Carter MD, et al. **Lectins and polysaccharide EPS I have flow-responsive roles in the attachment and biofilm mechanics of plant pathogenic Ralstonia**. *PLOS Pathogens* (Sep 2024). DOI: **10.1371/journal.ppat.1012358**. https://doi.org/10.1371/journal.ppat.1012358 (carter2024lectinsandpolysaccharide pages 1-2)
4. Dulal N, Wilson RA. **Paths of Least Resistance: Unconventional Effector Secretion by Fungal and Oomycete Plant Pathogens**. *Molecular Plant-Microbe Interactions* (Sep 2024). DOI: **10.1094/mpmi-12-23-0212-cr**. https://doi.org/10.1094/mpmi-12-23-0212-cr (dulal2024pathsofleast pages 1-2)
5. Liu X, et al. **An effector essential for virulence of necrotrophic fungi targets plant HIRs to inhibit host immunity**. *Nature Communications* (Oct 2024). DOI: **10.1038/s41467-024-53725-0**. https://doi.org/10.1038/s41467-024-53725-0 (liu2024aneffectoressential pages 1-2)
6. Wojtasik W, et al. **Endophytic non-pathogenic Fusarium oxysporum reorganizes the cell wall in flax seedlings**. *Frontiers in Plant Science* (Mar 2024). DOI: **10.3389/fpls.2024.1352105**. https://doi.org/10.3389/fpls.2024.1352105 (wojtasik2024endophyticnonpathogenicfusarium pages 1-2, wojtasik2024endophyticnonpathogenicfusarium pages 2-3)
7. Hajji-Hedfi L, et al. **Plant Diseases: Pathogenicity and integrated management overview**. *Microbial Biosystems* (Dec 2024). DOI: **10.21608/mb.2024.307263.1134**. https://doi.org/10.21608/mb.2024.307263.1134 (hajjihedfi2024plantdiseasespathogenicity pages 2-4)
8. Cui X, et al. **Xylanase VmXyl2 is involved in the pathogenicity of Valsa mali**. *Frontiers in Plant Science* (Apr 2024). DOI: **10.3389/fpls.2024.1342714**. https://doi.org/10.3389/fpls.2024.1342714 (cui2024xylanasevmxyl2is pages 13-13)
9. Fontana R, et al. **Effects of Flavonoids and Phenols from Moringa oleifera Leaf Extracts on Biofilm Processes in Xanthomonas campestris pv. campestris**. *Plants* (Mar 2023). DOI: **10.3390/plants12071508**. https://doi.org/10.3390/plants12071508 (fontana2023effectsofflavonoids pages 1-2)
10. Mulungu EL. **Unmasking the hidden threat: a review of damage and losses due to phytopathogenic bacteria**. *Journal of Current Opinion in Crop Science* (Dec 2024). DOI: **10.62773/jcocs.v5i4.277**. https://doi.org/10.62773/jcocs.v5i4.277 (mulungu2024unmaskingthehidden pages 1-2, mulungu2024unmaskingthehidden pages 7-9)

---

## Figure citation (visual evidence)

- Hrp T3SS schematic (gene cluster + apparatus + effector injection model): (kvitko2023discoveryofthe media 08856614)


References

1. (hajjihedfi2024plantdiseasespathogenicity pages 2-4): Lobna Hajji-Hedfi, Amira Khlif, Wassila Hlaoua, Abdelhak Rhouma, Samar Dali, Omaima Bargougui, and Hemraj Chhipa. Plant diseases: pathogenicity and integrated management overview. Microbial Biosystems, 9:41-57, Dec 2024. URL: https://doi.org/10.21608/mb.2024.307263.1134, doi:10.21608/mb.2024.307263.1134. This article has 8 citations.

2. (kvitko2023discoveryofthe pages 1-2): Brian H. Kvitko and Alan Collmer. Discovery of the hrp type iii secretion system in phytopathogenic bacteria: how investigation of hypersensitive cell death in plants led to a novel protein injector system and a world of inter-organismal molecular interactions within plant cells. Phytopathology, 113:PHYTO08220292KD, Apr 2023. URL: https://doi.org/10.1094/phyto-08-22-0292-kd, doi:10.1094/phyto-08-22-0292-kd. This article has 31 citations and is from a peer-reviewed journal.

3. (wojtasik2024endophyticnonpathogenicfusarium pages 1-2): Wioleta Wojtasik, Lucyna Dymińska, Jerzy Hanuza, Marta Burgberger, Aleksandra Boba, Jan Szopa, Anna Kulma, and Justyna Mierziak. Endophytic non-pathogenic fusarium oxysporum reorganizes the cell wall in flax seedlings. Frontiers in Plant Science, Mar 2024. URL: https://doi.org/10.3389/fpls.2024.1352105, doi:10.3389/fpls.2024.1352105. This article has 12 citations.

4. (wojtasik2024endophyticnonpathogenicfusarium pages 2-3): Wioleta Wojtasik, Lucyna Dymińska, Jerzy Hanuza, Marta Burgberger, Aleksandra Boba, Jan Szopa, Anna Kulma, and Justyna Mierziak. Endophytic non-pathogenic fusarium oxysporum reorganizes the cell wall in flax seedlings. Frontiers in Plant Science, Mar 2024. URL: https://doi.org/10.3389/fpls.2024.1352105, doi:10.3389/fpls.2024.1352105. This article has 12 citations.

5. (kvitko2023discoveryofthe media 08856614): Brian H. Kvitko and Alan Collmer. Discovery of the hrp type iii secretion system in phytopathogenic bacteria: how investigation of hypersensitive cell death in plants led to a novel protein injector system and a world of inter-organismal molecular interactions within plant cells. Phytopathology, 113:PHYTO08220292KD, Apr 2023. URL: https://doi.org/10.1094/phyto-08-22-0292-kd, doi:10.1094/phyto-08-22-0292-kd. This article has 31 citations and is from a peer-reviewed journal.

6. (carezzano2023biofilmformingabilityof pages 5-6): María Evangelina Carezzano, María Fernanda Paletti Rovey, Lorena del Rosario Cappellari, Lucas Antonio Gallarato, Pablo Bogino, María de las Mercedes Oliva, and Walter Giordano. Biofilm-forming ability of phytopathogenic bacteria: a review of its involvement in plant stress. Plants, 12:2207, Jun 2023. URL: https://doi.org/10.3390/plants12112207, doi:10.3390/plants12112207. This article has 53 citations.

7. (carezzano2023biofilmformingabilityof pages 9-11): María Evangelina Carezzano, María Fernanda Paletti Rovey, Lorena del Rosario Cappellari, Lucas Antonio Gallarato, Pablo Bogino, María de las Mercedes Oliva, and Walter Giordano. Biofilm-forming ability of phytopathogenic bacteria: a review of its involvement in plant stress. Plants, 12:2207, Jun 2023. URL: https://doi.org/10.3390/plants12112207, doi:10.3390/plants12112207. This article has 53 citations.

8. (carezzano2023biofilmformingabilityof pages 6-8): María Evangelina Carezzano, María Fernanda Paletti Rovey, Lorena del Rosario Cappellari, Lucas Antonio Gallarato, Pablo Bogino, María de las Mercedes Oliva, and Walter Giordano. Biofilm-forming ability of phytopathogenic bacteria: a review of its involvement in plant stress. Plants, 12:2207, Jun 2023. URL: https://doi.org/10.3390/plants12112207, doi:10.3390/plants12112207. This article has 53 citations.

9. (carter2024lectinsandpolysaccharide pages 1-2): Mariama D. Carter, Tuan M. Tran, Matthew L. Cope-Arguello, Sofia Weinstein, Hanlei Li, Connor G. Hendrich, Jessica L. Prom, Jiayu Li, Lan Thanh Chu, Loan Bui, Harishankar Manikantan, Tiffany M. Lowe-Power, and Caitilyn Allen. Lectins and polysaccharide eps i have flow-responsive roles in the attachment and biofilm mechanics of plant pathogenic ralstonia. Sep 2024. URL: https://doi.org/10.1371/journal.ppat.1012358, doi:10.1371/journal.ppat.1012358. This article has 10 citations and is from a highest quality peer-reviewed journal.

10. (cui2024xylanasevmxyl2is pages 13-13): Xinyue Cui, Xinke Li, Shen Li, Yan Huang, Naixu Liu, Sen Lian, Baohua Li, and Caixia Wang. Xylanase vmxyl2 is involved in the pathogenicity of valsa mali by regulating xylanase activity and inducing cell necrosis. Frontiers in Plant Science, Apr 2024. URL: https://doi.org/10.3389/fpls.2024.1342714, doi:10.3389/fpls.2024.1342714. This article has 10 citations.

11. (dulal2024pathsofleast pages 1-2): Nawaraj Dulal and Richard A. Wilson. Paths of least resistance: unconventional effector secretion by fungal and oomycete plant pathogens. Molecular Plant-Microbe Interactions®, 37:653-661, Sep 2024. URL: https://doi.org/10.1094/mpmi-12-23-0212-cr, doi:10.1094/mpmi-12-23-0212-cr. This article has 12 citations.

12. (liu2024aneffectoressential pages 1-2): Xiaofan Liu, Huihui Zhao, Mingyun Yuan, Pengyue Li, Jiatao Xie, Yanping Fu, Bo Li, Xiao Yu, Tao Chen, Yang Lin, Weidong Chen, Daohong Jiang, and Jiasen Cheng. An effector essential for virulence of necrotrophic fungi targets plant hirs to inhibit host immunity. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53725-0, doi:10.1038/s41467-024-53725-0. This article has 34 citations and is from a highest quality peer-reviewed journal.

13. (fontana2023effectsofflavonoids pages 1-2): Riccardo Fontana, Anna Caproni, Mariaconcetta Sicurella, Stefano Manfredini, Anna Baldisserotto, and Peggy Marconi. Effects of flavonoids and phenols from moringa oleifera leaf extracts on biofilm processes in xanthomonas campestris pv. campestris. Plants, 12:1508, Mar 2023. URL: https://doi.org/10.3390/plants12071508, doi:10.3390/plants12071508. This article has 16 citations.

14. (liu2023crucialrolesof pages 15-17): Ting Liu, Yong Chen, Shiping Tian, and Boqiang Li. Crucial roles of effectors in interactions between horticultural crops and pathogens. Horticulturae, 9:250, Feb 2023. URL: https://doi.org/10.3390/horticulturae9020250, doi:10.3390/horticulturae9020250. This article has 8 citations.

15. (santosbriones2024algorithmsforeffector pages 18-19): César De los Santos-Briones, Karla Gisel Carreón-Anguiano, Sara E. Vila-Luna, Jewel Nicole Anna Todd, Ignacio Islas-Flores, Luis Sáenz-Carbonell, Pablo Alejandro Gamas-Trujillo, and Blondy Canto-Canché. Algorithms for effector prediction in plant pathogens and pests: achievements and current challenges. Microbiology Research, 15:2162-2183, Oct 2024. URL: https://doi.org/10.3390/microbiolres15040145, doi:10.3390/microbiolres15040145. This article has 3 citations.

16. (mulungu2024unmaskingthehidden pages 1-2): Emanuel L Mulungu. Unmasking the hidden threat: a review of damage and losses due to phytopathogenic bacteria. Journal of Current Opinion in Crop Science, 5:250-263, Dec 2024. URL: https://doi.org/10.62773/jcocs.v5i4.277, doi:10.62773/jcocs.v5i4.277. This article has 8 citations.

17. (mulungu2024unmaskingthehidden pages 7-9): Emanuel L Mulungu. Unmasking the hidden threat: a review of damage and losses due to phytopathogenic bacteria. Journal of Current Opinion in Crop Science, 5:250-263, Dec 2024. URL: https://doi.org/10.62773/jcocs.v5i4.277, doi:10.62773/jcocs.v5i4.277. This article has 8 citations.

18. (carezzano2023biofilmformingabilityof pages 8-9): María Evangelina Carezzano, María Fernanda Paletti Rovey, Lorena del Rosario Cappellari, Lucas Antonio Gallarato, Pablo Bogino, María de las Mercedes Oliva, and Walter Giordano. Biofilm-forming ability of phytopathogenic bacteria: a review of its involvement in plant stress. Plants, 12:2207, Jun 2023. URL: https://doi.org/10.3390/plants12112207, doi:10.3390/plants12112207. This article has 53 citations.