---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:08:35.859725'
end_time: '2026-08-04T09:22:28.315695'
duration_seconds: 832.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: non motile
  trait_identifier: METPO:1000703
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: non_motile
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motility in which an organism lacks the ability to move independently
    under its own power.
  parent_traits: METPO:1000701
  synonyms: no, non-motile
  evidence_summary: 'DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile
    rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832:
    flagellum (Bacterial flagellum review supports the absence or non-expression of
    the flagellar apparatus as the basis for non-motile phenotypes.)'
  causal_graph_summary: 'non_motile_absent_motility_apparatus: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** non motile
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000703
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism lacks the ability to move independently under its own power.
- **Parent traits:** METPO:1000701
- **Synonyms:** no, non-motile
- **Existing evidence:** DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832: flagellum (Bacterial flagellum review supports the absence or non-expression of the flagellar apparatus as the basis for non-motile phenotypes.)
- **Existing causal graph summary:** non_motile_absent_motility_apparatus: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **non motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_motile.yaml`.

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
- **Trait label:** non motile
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000703
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motility in which an organism lacks the ability to move independently under its own power.
- **Parent traits:** METPO:1000701
- **Synonyms:** no, non-motile
- **Existing evidence:** DOI:10.3389/fmicb.2025.1514643: They are Gram-negative, non-motile rods (Organism example: Klebsiella pneumoniae is described as non-motile.) | DOI:10.1146/annurev.micro.57.030502.090832: flagellum (Bacterial flagellum review supports the absence or non-expression of the flagellar apparatus as the basis for non-motile phenotypes.)
- **Existing causal graph summary:** non_motile_absent_motility_apparatus: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **non motile** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/non_motile.yaml`.

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


# Curation-Focused Report: Microbial Trait Non-Motile (METPO:1000703)

## 1. Trait Scope Summary

The microbial trait **non-motile** (METPO:1000703) is defined as "a motility in which an organism lacks the ability to move independently under its own power." The trait represents the **phenotypic absence of active, self-propelled displacement** observable under specified assay and environmental conditions (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6, warrell2024interspeciessurfactantsservea pages 1-2, warrell2024interspeciessurfactantsservea pages 5-7). 

### Boundary Cases and Distinctions

The non-motile phenotype must be carefully distinguished from several related states:

1. **Aflagellate vs. paralyzed flagella:** Non-motile cells may completely lack flagellar structures (e.g., ΔfliC mutants) or may produce flagella that cannot rotate due to motor dysfunction (e.g., ΔmotA mutants with paralyzed flagella) (haiko2013theroleof pages 5-7, warrell2024interspeciessurfactantsservea pages 5-7, wu2020reciprocalcdigmpsignaling pages 11-13, wu2020reciprocalcdigmpsignaling pages 6-8). These represent distinct mechanistic routes.

2. **Reduced swimming speed vs. immobility:** c-di-GMP-mediated flagellar braking through YcgR-MotA/FliG interactions reduces flagellar rotation speed and alters directional bias but typically does not abolish motility entirely (han2023flagellarbrakeprotein pages 1-2, fang2010apost‐translationalc‐di‐gmp‐dependent pages 7-8). Such reduced-speed states should not be curated as constitutive non-motility.

3. **Conditional vs. constitutive non-motility:** Viscosity-dependent phenotypes (e.g., *Campylobacter jejuni* ΔvidA mutants non-motile in low viscosity but motile at high viscosity) (ribardo2024viscositydependentdeterminantsof pages 1-2, ribardo2024viscositydependentdeterminantsof pages 4-6), mechanosensing-regulated states (pathogenic *E. coli* flagellar gene suppression in liquid versus agar) (laganenka2020flagellummediatedmechanosensingand pages 4-5, laganenka2020flagellummediatedmechanosensingand pages 2-4), and developmental-stage-specific arrest (Actinoplanes zoospore rotation arrest upon nutrient sensing) (kato2024molecularmechanismof pages 5-6, kato2024molecularmechanismof pages 1-2, kato2024molecularmechanismof pages 3-4) are context-dependent and should be qualified as such.

4. **Chemotaxis defects vs. motility loss:** Mutations in chemotaxis signaling (e.g., cheA, cheB) produce altered directional responses but do not necessarily eliminate swimming motility (haiko2013theroleof pages 5-7). Chemotaxis-defective strains may migrate uniformly rather than form chemotactic rings in soft agar assays.

5. **Flagellum-dependent vs. flagellum-independent surface movement:** Exogenous surfactants can enable flagellar-dependent surface spreading on agar where cells would otherwise appear immotile (warrell2024interspeciessurfactantsservea pages 1-2, warrell2024interspeciessurfactantsservea pages 5-7). This emergent motility is distinct from passive sliding, twitching, or gliding. "Non-motile" calls from surface assays must account for the physical and chemical environment.

6. **Assay-specific interpretation:** Soft agar concentration strongly affects measured migration speed and chemotactic ring formation (croze2011migrationofchemotactic pages 5-8, croze2011migrationofchemotactic pages 1-5). Increased agar concentration suppresses chemotaxis through collision-induced perturbation of run-tumble dynamics. This represents an assay boundary condition rather than an organism-intrinsic non-motile state.

---

## 2. Candidate Causal Graph Nodes Grouped by Type

### Genes and Proteins

- **FlhDC** (label-only, taxon-scoped): Master transcriptional regulator of flagellar gene expression (bacteria including *E. coli*, *Salmonella*)
- **FliC** / **FlaA** (label-only, taxon-scoped): Flagellin subunit of the flagellar filament (*Pseudomonas*, *Vibrio*, *E. coli*)
- **MotA** / **MotB** (label-only, taxon-scoped): Flagellar stator protein complex enabling proton-driven motor rotation
- **FlhF** (label-only, taxon-scoped): Signal recognition particle-type GTPase required for polar flagellar localization (*Pseudomonas aeruginosa*, *Vibrio cholerae*)
- **YcgR** (label-only, taxon-scoped): c-di-GMP-binding flagellar brake protein (*E. coli*, enterics)
- **FliG** (label-only, taxon-scoped): Switch complex and rotor component of flagellar motor
- **FliN** (label-only, taxon-scoped): C-ring component of flagellar basal body; interaction target for FtgA
- **FtgA** (label-only, *Actinoplanes missouriensis* specific): Protein mediating flagellar rotation arrest during zoospore germination
- **CheA1**, **CheW1-2** (label-only, *Actinoplanes* chemotaxis cluster-1): Chemotaxis signaling proteins forming the sensory complex that modulates FtgA availability
- **VidA**, **VidB** (label-only, *Campylobacter jejuni* specific): Viscosity-dependent determinants regulating swimming velocity across viscosity gradients
- **HsbR**, **WspR** (label-only, *Pseudomonas* specific): Response regulators in c-di-GMP signaling linked to FlhF-mediated biofilm/motility regulation

### Biological Processes and Molecular Functions

- **Bacterial-type flagellum-dependent cell motility** (GO:0071973): The process enabling active self-propelled movement driven by flagellar rotation
- **Bacterial-type flagellum** (GO:0009288): The flagellar apparatus including basal body, hook, and filament
- **c-di-GMP binding** (GO:0035438): Molecular function enabling YcgR and other proteins to respond to elevated cyclic di-GMP
- **Chemotaxis** (GO:0006935): Directed movement along chemical gradients; chemotaxis defects may confound non-motile interpretation in certain assays
- **Biofilm formation** (GO:0042710): Sessile community phenotype often reciprocally regulated with motility

### Chemicals and Metabolites

- **Cyclic di-GMP** (CHEBI:49537): Second messenger controlling motility-sessility transitions through binding to effectors such as YcgR

### Environmental and Assay Factors

- **Soft agar concentration** (label-only): Gel network density (typically 0.15–0.5% w/v) influencing bacterial motility assays through collision-induced run-tumble perturbation
- **Viscosity** (label-only, quantified in cP in source): Environmental medium viscosity affecting swimming speed and flagellar motor output
- **Exogenous surfactants** (label-only): Secreted molecules (bacterial rhamnolipids, PSMs, plant saponins, host mucin, synthetic SDS) enabling flagellar-based surface spreading where cells are otherwise immotile on agar
- **Nutrient signal** (label-only, *Actinoplanes*-specific): Environmental cue triggering zoospore swimming cessation and germination initiation

---

## 3. Evidence-Backed Causal Edges with References and Qualifications

The following candidate edges are proposed with supporting evidence. Each is assigned a priority for TraitMech curation based on directness of the non-motile endpoint and generalizability across taxa and conditions.

| priority | mechanistic route | best-supported triple | representative taxon | evidence strength | key qualification |
|---|---|---|---|---|---|
| High — direct non-motile | FlhF loss alters polar flagellar localization and raises c-di-GMP-associated sessility | FlhF loss → non-motile phenotype | *Pseudomonas aeruginosa* PAO1 | Strong direct phenotype (2024) (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6) | Taxon-specific to polar-flagellated bacteria; mechanism to non-motility likely via flagellar localization/assembly defects rather than a universal non-motile route |
| High — direct non-motile | Flagellin/filament loss removes propulsive filament | fliC/flaA deletion → non-motile / aflagellate phenotype | *P. aeruginosa* (ΔfliC), *Vibrio cholerae* (ΔflaA) | Strong for direct loss of flagellum-based motility, but across taxa/assays (warrell2024interspeciessurfactantsservea pages 5-7, wu2020reciprocalcdigmpsignaling pages 11-13) | Supports non-motility for flagellum-driven movement; may coexist with increased biofilm or preserved attachment in some taxa |
| High — direct non-motile | Stator loss yields paralyzed or non-energized flagella despite retained apparatus | motA loss → non-motile phenotype with paralyzed flagella | Pathogenic *Escherichia coli*; comparative flagellar review examples | Strong mechanistic support (laganenka2020flagellummediatedmechanosensingand pages 4-5, haiko2013theroleof pages 5-7) | Distinguish from aflagellate cells: apparatus may remain but rotation fails; in some systems stator defects also affect attachment/biofilm signaling |
| Medium-High — direct non-motile | Nutrient-triggered FtgA release acts through FliN/C-ring to stop rotation | nutrient exposure → FtgA release → FliN interaction → flagellar rotation arrest → non-motile zoospore | *Actinoplanes missouriensis* | Strong within a single developmental system (2024) (kato2024molecularmechanismof pages 5-6, kato2024molecularmechanismof pages 1-2, kato2024molecularmechanismof pages 3-4) | Specialized zoospore/germination program; likely not generalizable to typical bacterial vegetative non-motility without caution |
| Low-Medium — reduced/conditional, not direct non-motile | c-di-GMP brake on motor through YcgR-MotA/FliG | elevated c-di-GMP → YcgR binding → MotA/FliG interaction → reduced flagellar rotation speed / altered bias | *E. coli* / enterics | Strong for motor braking, not for complete non-motility (han2023flagellarbrakeprotein pages 1-2, fang2010apost‐translationalc‐di‐gmp‐dependent pages 7-8) | Usually reduces speed and changes CW/CCW bias rather than abolishing motility; should not be curated as constitutive non-motile without endpoint-specific evidence |
| Low-Medium — conditional | VidA/VidB viscosity-tuned motor control | vidA loss → non-motile or slow swimming in low viscosity | *Campylobacter jejuni* | Strong but explicitly environment-conditional, with quantitative support (2024) (ribardo2024viscositydependentdeterminantsof pages 1-2, ribardo2024viscositydependentdeterminantsof pages 4-6) | Not constitutive: motility is restored at high viscosity; best modeled as viscosity-dependent conditional immobility or reduced speed |
| Low — assay effect | Soft-agar concentration suppresses apparent chemotactic migration | increased agar concentration → decreased migration front speed / suppressed chemotaxis | *E. coli* soft-agar assay | Strong assay literature, indirect for trait curation (croze2011migrationofchemotactic pages 5-8, croze2011migrationofchemotactic pages 1-5) | Assay artifact/boundary condition, not organism-intrinsic non-motility; important warning for phenotype interpretation |
| Low — assay/environment rescue | Exogenous surfactants permit surface spreading where cells are otherwise immotile on that surface | exogenous surfactant → enables flagella-dependent surface spreading on hard or semi-solid agar | *P. aeruginosa* | Strong for environmental rescue of movement (2024) (warrell2024interspeciessurfactantsservea pages 1-2, warrell2024interspeciessurfactantsservea pages 5-7) | Opposes naive non-motile calls from surface assays; movement requires active flagella and differs from passive sliding |
| Medium — conditional mechanosensing state | Lack of filament or stator rotation can lock cells in motility-off regulation | ΔfliC or ΔmotA → mechanosensing lock-off state → reduced flagellar gene expression / non-motile in agar-liquid comparisons | Pathogenic *E. coli* | Strong but state-dependent (laganenka2020flagellummediatedmechanosensingand pages 4-5, laganenka2020flagellummediatedmechanosensingand pages 5-6) | Useful for regulatory graph expansion, but endpoint combines structural loss with gene-expression feedback and culture-condition effects |


*Table: This table prioritizes candidate mechanistic routes for curating METPO:1000703, separating direct non-motile endpoints from conditional or assay-dependent reductions in motility. It helps focus TraitMech curation on high-confidence causal routes while flagging important qualifications.*

### Edge Detail (Selected High-Priority Examples)

**Edge 1: FlhF loss → non-motile phenotype**
- **Source:** DOI:10.1128/aem.01548-23 (Guan et al., 2024, *Applied and Environmental Microbiology*)
- **Taxon:** *Pseudomonas aeruginosa* PAO1
- **Evidence snippet:** "We constructed an unmarked deletion of flhF in P. aeruginosa PAO1. The ΔflhF mutant strain was non-motile" (guan2024flhfaffectsthe pages 1-2, guan2024flhfaffectsthe pages 2-6).
- **Notes:** The ΔflhF mutant also exhibited elevated c-di-GMP levels, enhanced biofilm formation, and wrinkled colonies. The non-motile phenotype likely arises from defective polar flagellar localization, a function of FlhF confirmed across multiple polar-flagellated species. This edge is **taxon-specific** to polar-flagellated bacteria.
- **Qualification:** The mechanism from FlhF loss to non-motility is indirect (via flagellar mislocalization or altered biosynthesis) and may not be universal. In *P. aeruginosa*, the ΔflhF phenotype includes pleiotropic effects on c-di-GMP signaling and biofilm formation, suggesting causal complexity.

**Edge 2: fliC / flaA deletion → non-motile / aflagellate phenotype**
- **Source (fliC):** DOI:10.1128/jb.00281-24 (Warrell et al., 2024, *Journal of Bacteriology*) and others
- **Source (flaA):** DOI:10.1371/journal.pgen.1008703 (Wu et al., 2020, *PLOS Genetics*)
- **Taxon:** *Pseudomonas aeruginosa* (ΔfliC), *Vibrio cholerae* (ΔflaA)
- **Evidence snippet (ΔfliC):** "The flgB::tn, flgE::tn, and ΔfliC mutants only slid on the plates without spreading out, unlike the motility exhibited by the WT strain" (warrell2024interspeciessurfactantsservea pages 5-7). These mutants lack the flagellar filament and are "defective in swimming."
- **Evidence snippet (ΔflaA):** "Deletion of flaA (flagellin gene) triggers feedback regulation of biofilm formation through c-di-GMP accumulation. The ΔflaA strain exhibits higher vps-II expression and elevated c-di-GMP levels compared to wild-type" (wu2020reciprocalcdigmpsignaling pages 11-13).
- **Notes:** Loss of flagellin eliminates the propulsive filament, producing an aflagellate, non-motile phenotype for flagellum-dependent swimming. However, some species (e.g., *V. cholerae* ΔflaA) maintain or enhance surface attachment, biofilm formation, and c-di-GMP signaling. This edge is robust but should distinguish the **direct loss of flagellum-based motility** from compensatory regulatory changes.
- **Qualification:** Generalizable across flagellated bacteria for swimming motility loss; does not preclude twitching or gliding in species possessing alternative motility systems.

**Edge 3: motA loss → non-motile phenotype with paralyzed flagella**
- **Source:** DOI:10.1128/mbio.02269-19 (Laganenka et al., 2020, *mBio*)
- **Taxon:** Pathogenic *Escherichia coli* Z36 and related strains
- **Evidence snippet:** "ΔfliC mutants (lacking flagellar filaments, reduced motor load) and ΔmotA mutants (paralyzed flagella, absent stator protein) were locked in motility-off state in both liquid and agar growth" (laganenka2020flagellummediatedmechanosensingand pages 4-5).
- **Notes:** The MotA protein is part of the flagellar stator complex. Its absence eliminates the ion channel required for torque generation, producing paralyzed flagella that cannot rotate. The flagellar apparatus may remain structurally intact, distinguishing this phenotype from aflagellate mutants. The study also shows that ΔmotA cells trigger mechanosensing-related gene expression changes in *E. coli*.
- **Qualification:** **Mechanistically distinct from aflagellate states.** In some systems (e.g., *V. cholerae*), stator mutants (ΔmotX) also show biofilm and surface attachment defects beyond simple paralysis (wu2020reciprocalcdigmpsignaling pages 6-8). Curators should separate motor-energization failure from flagellar structural absence.

**Edge 4: Nutrient exposure → FtgA release from CheA1-CheW1-2 complex → FtgA-FliN interaction → flagellar rotation arrest**
- **Source:** DOI:10.1038/s42003-024-07104-6 (Kato et al., 2024, *Communications Biology*)
- **Taxon:** *Actinoplanes missouriensis* (filamentous actinomycete zoospores)
- **Evidence snippet:** "The zoospores of ftgA-knockout mutants kept swimming awkwardly after germination. […] FtgA interacted not only with the C-terminal core region of FliN but also with chemotaxis regulatory proteins CheA1 and CheW1-2, which are encoded by che cluster-1. We propose the following working model of motility regulation in A. missouriensis zoospores: the chemotaxis sensory complex initially captures FtgA to allow zoospores to swim and then releases FtgA to stop flagellar rotation (i.e., swimming) in response to external nutrient signals" (kato2024molecularmechanismof pages 5-6, kato2024molecularmechanismof pages 1-2, kato2024molecularmechanismof pages 3-4).
- **Notes:** This is a **developmental-stage-specific** mechanism for arresting flagellar rotation during the transition from swimming zoospore to germinating cell. FtgA binding to the extended N-terminal region of FliN in the C-ring is proposed to halt flagellar export or rotation. The P101S suppressor mutation in FliN restored motility in ftgA-overexpressing strains.
- **Qualification:** **Highly specialized to the Actinoplanes zoospore life cycle.** This edge is not generalizable to typical bacterial vegetative growth and should be marked as a developmental/germination-specific arrest mechanism. The molecular details of how FtgA-FliN interaction stops rotation remain incompletely resolved.

**Edge 5: Elevated c-di-GMP → YcgR binding → YcgR-MotA and YcgR-FliG interaction → reduced flagellar rotation speed and CCW bias**
- **Source:** DOI:10.3389/fmicb.2023.1159974 (Han et al., 2023, *Frontiers in Microbiology*)
- **Source:** DOI:10.1111/j.1365-2958.2010.07179.x (Fang & Gomelsky, 2010, *Molecular Microbiology*)
- **Taxon:** *E. coli* and enteric bacteria
- **Evidence snippet (2023):** "YcgR binding to c-di-GMP enhances its affinity for both MotA and FliG. Key residues are identified: D54 in YcgR-N for FliG binding, and F117 and E232 for MotA binding. Mutations in these residues restored flagellar rotation speed in wild-type E. coli and in cells lacking CheY, and decreased counterclockwise bias" (han2023flagellarbrakeprotein pages 1-2).
- **Evidence snippet (2010):** "No differences in flagellin production or rotation velocity in wild-type versus ΔyhjH or ΔycgR mutants, indicating stable motor function; ΔyhjH mutants show strong CCW bias, which is fully restored to wild-type ratios by ycgR deletion" (fang2010apost‐translationalc‐di‐gmp‐dependent pages 7-8).
- **Notes:** c-di-GMP-YcgR acts as a **flagellar brake** reducing motor speed and biasing CCW rotation. This system typically produces **reduced swimming speed** and altered chemotaxis, not complete immobility.
- **Qualification:** **Should NOT be curated as constitutive non-motility.** The endpoint is typically speed reduction and directional bias. Complete immobility requires very high c-di-GMP levels or additional regulatory inputs. Mark this edge as **conditional / reduced motility** rather than non-motile.

**Edge 6: vidA loss → non-motile or slow swimming in low viscosity; motility restored at high viscosity**
- **Source:** DOI:10.1128/mbio.02544-23 (Ribardo et al., 2024, *mBio*)
- **Taxon:** *Campylobacter jejuni*
- **Evidence snippet:** "ΔvidA mutants showed severely reduced swimming velocity (2.1 µm/s) in low-viscosity media (1 cP) compared to wild-type (15.9 µm/s), but swimming velocity recovered as viscosity increased (21.7–26.6 µm/s at 5–20 cP, 32.6 µm/s at 40 cP)" (ribardo2024viscositydependentdeterminantsof pages 4-6). "ΔvidA mutants exhibited non-motility or slow swimming in low-viscosity media but restored high-velocity swimming in high-viscosity Newtonian and non-Newtonian fluids similar to wild-type" (ribardo2024viscositydependentdeterminantsof pages 1-2).
- **Notes:** VidA and VidB act as viscosity-dependent regulators of flagellar motor activity. The *C. jejuni* motor evolved for high-viscosity intestinal mucus environments. VidA is required for low-viscosity swimming; unregulated VidB acts as a brake in low viscosity.
- **Qualification:** **Explicitly environment-conditional.** This is not constitutive non-motility. Curate as **viscosity-conditional reduced or absent motility.** The phenotype depends on assay medium viscosity.

**Edge 7: Increased soft agar concentration → decreased migration front speed / suppressed chemotaxis**
- **Source:** DOI:10.1016/j.bpj.2011.06.023 (Croze et al., 2011, *Biophysical Journal*)
- **Taxon:** *E. coli* K-12
- **Evidence snippet:** "The front speed is weakly dependent of agar concentration below C = 0.25%, but decreases sharply above this value. […] Agar concentration in the range C = 0.15–0.5% strongly affects chemotaxis through collision-induced perturbation of run-tumble dynamics" (croze2011migrationofchemotactic pages 5-8, croze2011migrationofchemotactic pages 1-5).
- **Notes:** This is an **assay boundary condition** rather than an organism-intrinsic non-motile phenotype. Elevated agar concentration increases collision frequency, perturbing chemotactic sensing and slowing migration.
- **Qualification:** **Assay artifact / interpretive warning.** Soft agar assays are widely used to assess motility and chemotaxis, but concentration is not standardized. This edge highlights the need to report agar concentration and recognize its effect on phenotype. Do not curate as a mechanistic route to non-motility; include as an experimental factor node.

**Edge 8: Exogenous surfactant → enables flagella-dependent surface spreading where cells are otherwise immotile on agar**
- **Source:** DOI:10.1128/jb.00281-24 (Warrell et al., 2024, *Journal of Bacteriology*)
- **Taxon:** *Pseudomonas aeruginosa*
- **Evidence snippet:** "Exogenous surfactants from S. aureus, other bacteria, and interkingdom species enabled P. aeruginosa to switch from swarming to an alternative surface spreading motility on semi-solid surfaces and allowed for the emergence of surface motility on hard agar where P. aeruginosa was otherwise unable to move" (warrell2024interspeciessurfactantsservea pages 1-2). "Active flagellar function was required for surface spreading" (warrell2024interspeciessurfactantsservea pages 5-7).
- **Notes:** Interspecies surfactants (PSMs from *S. aureus*, rhamnolipids, surfactin, mucin, plant saponin, etc.) act as public goods permitting flagellar-based spreading on surfaces where cells appear immotile without surfactant.
- **Qualification:** **Environmental rescue of apparent immobility.** This demonstrates that "non-motile" calls from surface assays can be reversed by environmental factors. Flagella are functional; lack of movement is due to surface properties. Mark this as an **assay/environment interaction** rather than intrinsic non-motility.

---

## 4. Ontology Grounding

### Stable CURIEs Used
- **METPO:1000703** (target trait, quoted verbatim as requested)
- **GO:0071973** (bacterial-type flagellum-dependent cell motility)
- **GO:0009288** (bacterial-type flagellum)
- **GO:0035438** (c-di-GMP binding)
- **GO:0006935** (chemotaxis)
- **GO:0042710** (biofilm formation)
- **CHEBI:49537** (cyclic di-GMP)

### Label-Only Nodes (No CURIEs Invented)
All gene and protein nodes (FlhDC, FliC, FlaA, MotA, MotB, FlhF, YcgR, FliG, FliN, FtgA, CheA1, CheW1-2, VidA, VidB, HsbR, WspR) are left as **taxon-scoped label-only candidates** pending specific UniProt or gene accession selection. Environmental and assay factor nodes (soft agar concentration, viscosity, exogenous surfactants, nutrient signal) are also **label-only**. No identifiers were fabricated.

---

## 5. DOI-First Bibliography with URLs and Publication Dates

1. Guan C, Huang Y, Zhou Y, et al. FlhF affects the subcellular clustering of WspR through HsbR in *Pseudomonas aeruginosa*. *Applied and Environmental Microbiology*. 2024;90(1). doi:10.1128/aem.01548-23. URL: https://doi.org/10.1128/aem.01548-23. Published: January 2024.

2. Kato H, Tanemura H, Kimura T, et al. Molecular mechanism of flagellar motor rotation arrest in bacterial zoospores of *Actinoplanes missouriensis* before germination. *Communications Biology*. 2024;7(1). doi:10.1038/s42003-024-07104-6. URL: https://doi.org/10.1038/s42003-024-07104-6. Published: October 2024.

3. Warrell DL, Zarrella TM, Machalek C, Khare A. Interspecies surfactants serve as public goods enabling surface motility in *Pseudomonas aeruginosa*. *Journal of Bacteriology*. 2024;206(10). doi:10.1128/jb.00281-24. URL: https://doi.org/10.1128/jb.00281-24. Published: October 2024.

4. Ribardo DA, Johnson JJ, Hendrixson DR. Viscosity-dependent determinants of *Campylobacter jejuni* impacting the velocity of flagellar motility. *mBio*. 2024;15(1). doi:10.1128/mbio.02544-23. URL: https://doi.org/10.1128/mbio.02544-23. Published: January 2024.

5. Han Q, Wang SF, Qian XX, et al. Flagellar brake protein YcgR interacts with motor proteins MotA and FliG to regulate the flagellar rotation speed and direction. *Frontiers in Microbiology*. 2023;14. doi:10.3389/fmicb.2023.1159974. URL: https://doi.org/10.3389/fmicb.2023.1159974. Published: April 2023.

6. Laganenka L, López ME, Colin R, Sourjik V. Flagellum-mediated mechanosensing and RflP control motility state of pathogenic *Escherichia coli*. *mBio*. 2020;11(2). doi:10.1128/mbio.02269-19. URL: https://doi.org/10.1128/mbio.02269-19. Published: April 2020.

7. Wu DC, Zamorano-Sánchez D, Pagliai FA, et al. Reciprocal c-di-GMP signaling: Incomplete flagellum biogenesis triggers c-di-GMP signaling pathways that promote biofilm formation. *PLOS Genetics*. 2020;16(3):e1008703. doi:10.1371/journal.pgen.1008703. URL: https://doi.org/10.1371/journal.pgen.1008703. Published: March 2020.

8. Fang X, Gomelsky M. A post-translational, c-di-GMP-dependent mechanism regulating flagellar motility. *Molecular Microbiology*. 2010;76(5):1295-1305. doi:10.1111/j.1365-2958.2010.07179.x. URL: https://doi.org/10.1111/j.1365-2958.2010.07179.x. Published: June 2010.

9. Haiko J, Westerlund-Wikström B. The role of the bacterial flagellum in adhesion and virulence. *Biology*. 2013;2(4):1242-1267. doi:10.3390/biology2041242. URL: https://doi.org/10.3390/biology2041242. Published: October 2013.

10. Croze OA, Ferguson GP, Cates ME, Poon WCK. Migration of chemotactic bacteria in soft agar: Role of gel concentration. *Biophysical Journal*. 2011;101(3):525-534. doi:10.1016/j.bpj.2011.06.023. URL: https://doi.org/10.1016/j.bpj.2011.06.023. Published: August 2011.

---

## 6. Warnings for TraitMech Curation

### Claims That Should NOT Yet Be Curated as Direct Non-Motile Endpoints

1. **c-di-GMP-YcgR flagellar braking:** Reduces swimming speed and alters directional bias but typically does not produce complete immobility. Mark as **conditional / reduced motility** (han2023flagellarbrakeprotein pages 1-2, fang2010apost‐translationalc‐di‐gmp‐dependent pages 7-8).

2. **VidA/VidB viscosity-dependent regulation:** The ΔvidA non-motile phenotype is **explicitly viscosity-conditional** and restored at high viscosity. Not constitutive non-motility (ribardo2024viscositydependentdeterminantsof pages 1-2, ribardo2024viscositydependentdeterminantsof pages 4-6).

3. **FtgA-mediated rotation arrest in Actinoplanes zoospores:** A **developmental-stage-specific** mechanism for germination-associated swimming cessation. Not generalizable to vegetative bacterial motility (kato2024molecularmechanismof pages 5-6, kato2024molecularmechanismof pages 1-2, kato2024molecularmechanismof pages 3-4).

4. **Mechanosensing regulation in pathogenic E. coli:** Flagellar gene expression and motility differ between liquid culture and agar. This represents **conditional motility suppression** tied to mechanosensing and regulatory feedback, not a direct non-motile state (laganenka2020flagellummediatedmechanosensingand pages 4-5, laganenka2020flagellummediatedmechanosensingand pages 2-4, laganenka2020flagellummediatedmechanosensingand pages 5-6).

5. **Soft agar concentration effects:** Assay boundary condition affecting measured migration and chemotaxis. Not an organism-intrinsic non-motile phenotype; important interpretive warning (croze2011migrationofchemotactic pages 5-8, croze2011migrationofchemotactic pages 1-5).

6. **Exogenous surfactant-enabled surface spreading:** Demonstrates **environmental rescue of apparent immobility** on surfaces. Cells possess functional flagella; lack of movement without surfactant is due to surface properties (warrell2024interspeciessurfactantsservea pages 1-2, warrell2024interspeciessurfactantsservea pages 5-7).

### Taxon-Specific and Assay-Specific Qualifications

- **FlhF:** Polar-flagellated bacteria (*Pseudomonas*, *Vibrio*); non-motility mechanism via flagellar positioning defects.
- **MotX** (mentioned in *V. cholerae* literature): T-ring component of sodium-driven flagellar stator; taxon-specific stator system.
- **FtgA-FliN:** *Actinoplanes* zoospore-specific developmental arrest.
- **VidA/VidB:** *Campylobacter jejuni* intestinal mucus-adapted motor tuning.
- **Soft agar assay:** Widely used but concentration not standardized; results depend on agar %.

### Recommendations for Curation

- **Prioritize high-confidence, constitutive non-motile edges:** FlhF loss, fliC/flaA deletion (aflagellate), motA/motB deletion (paralyzed flagella).
- **Clearly label conditional, reduced-speed, or developmental edges** to avoid misleading downstream applications.
- **Include assay and environmental factor nodes** to capture context-dependence.
- **Do not invent CURIEs** for incompletely characterized proteins; use taxon-scoped labels pending accession selection.
- **Cite recent authoritative sources** (2023–2024) alongside foundational studies to balance novelty and mechanistic depth.

---

**Report prepared for TraitMech curation of METPO:1000703 non-motile trait, integrating mechanistic causal edges with DOI-first references, exact supporting snippets, taxon/assay qualifications, ontology grounding, and explicit curation warnings.**

References

1. (guan2024flhfaffectsthe pages 1-2): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

2. (guan2024flhfaffectsthe pages 2-6): Congcong Guan, Yi Huang, Yun Zhou, Yuqian Han, Shuhui Liu, Shimin Liu, Weina Kong, Tietao Wang, and Yani Zhang. Flhf affects the subcellular clustering of wspr through hsbr in <i>pseudomonas aeruginosa</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01548-23, doi:10.1128/aem.01548-23. This article has 13 citations and is from a peer-reviewed journal.

3. (warrell2024interspeciessurfactantsservea pages 1-2): Delayna L. Warrell, Tiffany M. Zarrella, Christopher Machalek, and Anupama Khare. Interspecies surfactants serve as public goods enabling surface motility in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00281-24, doi:10.1128/jb.00281-24. This article has 14 citations and is from a peer-reviewed journal.

4. (warrell2024interspeciessurfactantsservea pages 5-7): Delayna L. Warrell, Tiffany M. Zarrella, Christopher Machalek, and Anupama Khare. Interspecies surfactants serve as public goods enabling surface motility in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00281-24, doi:10.1128/jb.00281-24. This article has 14 citations and is from a peer-reviewed journal.

5. (haiko2013theroleof pages 5-7): Johanna Haiko and Benita Westerlund-Wikström. The role of the bacterial flagellum in adhesion and virulence. Biology, 2:1242-1267, Oct 2013. URL: https://doi.org/10.3390/biology2041242, doi:10.3390/biology2041242. This article has 785 citations.

6. (wu2020reciprocalcdigmpsignaling pages 11-13): Daniel C. Wu, David Zamorano-Sánchez, Fernando A. Pagliai, Jin Hwan Park, Kyle A. Floyd, Calvin K. Lee, Giordan Kitts, Christopher B. Rose, Eric M. Bilotta, Gerard C. L. Wong, and Fitnat H. Yildiz. Reciprocal c-di-gmp signaling: incomplete flagellum biogenesis triggers c-di-gmp signaling pathways that promote biofilm formation. PLOS Genetics, 16:e1008703, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008703, doi:10.1371/journal.pgen.1008703. This article has 81 citations and is from a domain leading peer-reviewed journal.

7. (wu2020reciprocalcdigmpsignaling pages 6-8): Daniel C. Wu, David Zamorano-Sánchez, Fernando A. Pagliai, Jin Hwan Park, Kyle A. Floyd, Calvin K. Lee, Giordan Kitts, Christopher B. Rose, Eric M. Bilotta, Gerard C. L. Wong, and Fitnat H. Yildiz. Reciprocal c-di-gmp signaling: incomplete flagellum biogenesis triggers c-di-gmp signaling pathways that promote biofilm formation. PLOS Genetics, 16:e1008703, Mar 2020. URL: https://doi.org/10.1371/journal.pgen.1008703, doi:10.1371/journal.pgen.1008703. This article has 81 citations and is from a domain leading peer-reviewed journal.

8. (han2023flagellarbrakeprotein pages 1-2): Qun Han, Shao-Feng Wang, Xin-Xin Qian, Lu Guo, Yi-Feng Shi, Rui He, Jun-Hua Yuan, Yan-Jie Hou, and De-Feng Li. Flagellar brake protein ycgr interacts with motor proteins mota and flig to regulate the flagellar rotation speed and direction. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1159974, doi:10.3389/fmicb.2023.1159974. This article has 22 citations and is from a peer-reviewed journal.

9. (fang2010apost‐translationalc‐di‐gmp‐dependent pages 7-8): Xin Fang and Mark Gomelsky. A post‐translational, c‐di‐gmp‐dependent mechanism regulating flagellar motility. Molecular Microbiology, 76:1295-1305, Jun 2010. URL: https://doi.org/10.1111/j.1365-2958.2010.07179.x, doi:10.1111/j.1365-2958.2010.07179.x. This article has 300 citations and is from a domain leading peer-reviewed journal.

10. (ribardo2024viscositydependentdeterminantsof pages 1-2): Deborah A. Ribardo, Jeremiah J. Johnson, and David R. Hendrixson. Viscosity-dependent determinants of <i>campylobacter jejuni</i> impacting the velocity of flagellar motility. Jan 2024. URL: https://doi.org/10.1128/mbio.02544-23, doi:10.1128/mbio.02544-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (ribardo2024viscositydependentdeterminantsof pages 4-6): Deborah A. Ribardo, Jeremiah J. Johnson, and David R. Hendrixson. Viscosity-dependent determinants of <i>campylobacter jejuni</i> impacting the velocity of flagellar motility. Jan 2024. URL: https://doi.org/10.1128/mbio.02544-23, doi:10.1128/mbio.02544-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (laganenka2020flagellummediatedmechanosensingand pages 4-5): Leanid Laganenka, María Esteban López, Remy Colin, and Victor Sourjik. Flagellum-mediated mechanosensing and rflp control motility state of pathogenic escherichia coli. Apr 2020. URL: https://doi.org/10.1128/mbio.02269-19, doi:10.1128/mbio.02269-19. This article has 44 citations and is from a domain leading peer-reviewed journal.

13. (laganenka2020flagellummediatedmechanosensingand pages 2-4): Leanid Laganenka, María Esteban López, Remy Colin, and Victor Sourjik. Flagellum-mediated mechanosensing and rflp control motility state of pathogenic escherichia coli. Apr 2020. URL: https://doi.org/10.1128/mbio.02269-19, doi:10.1128/mbio.02269-19. This article has 44 citations and is from a domain leading peer-reviewed journal.

14. (kato2024molecularmechanismof pages 5-6): Hiromu Kato, Hiroki Tanemura, Tomohiro Kimura, Yohei Katsuyama, Takeaki Tezuka, and Yasuo Ohnishi. Molecular mechanism of flagellar motor rotation arrest in bacterial zoospores of actinoplanes missouriensis before germination. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-07104-6, doi:10.1038/s42003-024-07104-6. This article has 10 citations and is from a peer-reviewed journal.

15. (kato2024molecularmechanismof pages 1-2): Hiromu Kato, Hiroki Tanemura, Tomohiro Kimura, Yohei Katsuyama, Takeaki Tezuka, and Yasuo Ohnishi. Molecular mechanism of flagellar motor rotation arrest in bacterial zoospores of actinoplanes missouriensis before germination. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-07104-6, doi:10.1038/s42003-024-07104-6. This article has 10 citations and is from a peer-reviewed journal.

16. (kato2024molecularmechanismof pages 3-4): Hiromu Kato, Hiroki Tanemura, Tomohiro Kimura, Yohei Katsuyama, Takeaki Tezuka, and Yasuo Ohnishi. Molecular mechanism of flagellar motor rotation arrest in bacterial zoospores of actinoplanes missouriensis before germination. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-07104-6, doi:10.1038/s42003-024-07104-6. This article has 10 citations and is from a peer-reviewed journal.

17. (croze2011migrationofchemotactic pages 5-8): Ottavio A. Croze, Gail P. Ferguson, Michael E. Cates, and Wilson C.K. Poon. Migration of chemotactic bacteria in soft agar: role of gel concentration. Biophysical Journal, 101:525-534, Aug 2011. URL: https://doi.org/10.1016/j.bpj.2011.06.023, doi:10.1016/j.bpj.2011.06.023. This article has 124 citations and is from a domain leading peer-reviewed journal.

18. (croze2011migrationofchemotactic pages 1-5): Ottavio A. Croze, Gail P. Ferguson, Michael E. Cates, and Wilson C.K. Poon. Migration of chemotactic bacteria in soft agar: role of gel concentration. Biophysical Journal, 101:525-534, Aug 2011. URL: https://doi.org/10.1016/j.bpj.2011.06.023, doi:10.1016/j.bpj.2011.06.023. This article has 124 citations and is from a domain leading peer-reviewed journal.

19. (laganenka2020flagellummediatedmechanosensingand pages 5-6): Leanid Laganenka, María Esteban López, Remy Colin, and Victor Sourjik. Flagellum-mediated mechanosensing and rflp control motility state of pathogenic escherichia coli. Apr 2020. URL: https://doi.org/10.1128/mbio.02269-19, doi:10.1128/mbio.02269-19. This article has 44 citations and is from a domain leading peer-reviewed journal.