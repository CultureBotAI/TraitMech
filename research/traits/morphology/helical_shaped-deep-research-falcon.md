---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:45:51.937557'
end_time: '2026-08-04T09:00:10.146343'
duration_seconds: 858.21
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: helical shaped
  trait_identifier: METPO:1000676
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: helical_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a corkscrew-like helical cell
    body with curvature and twist along its long axis.
  parent_traits: METPO:1000666
  synonyms: helical-shaped
  evidence_summary: 'DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple
    proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for
    helical bacterial cell curvature and twist in Helicobacter pylori.)'
  causal_graph_summary: 'helical_shaped_pg_relaxation: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 69
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** helical shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000676
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a corkscrew-like helical cell body with curvature and twist along its long axis.
- **Parent traits:** METPO:1000666
- **Synonyms:** helical-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for helical bacterial cell curvature and twist in Helicobacter pylori.)
- **Existing causal graph summary:** helical_shaped_pg_relaxation: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **helical shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/helical_shaped.yaml`.

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
- **Trait label:** helical shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000676
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a corkscrew-like helical cell body with curvature and twist along its long axis.
- **Parent traits:** METPO:1000666
- **Synonyms:** helical-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2010.03.046: coordinated action of multiple proteins relaxes peptidoglycan crosslinking (Supports a mechanistic basis for helical bacterial cell curvature and twist in Helicobacter pylori.)
- **Existing causal graph summary:** helical_shaped_pg_relaxation: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **helical shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/helical_shaped.yaml`.

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


# Curation report: microbial “helical shaped”

## Executive summary

**Target:** “METPO:1000676” (`helical shaped`), morphology class, reviewed. The trait should denote a **cell-body** geometry having longitudinal curvature plus twist, yielding a corkscrew or true helical centerline. It should not be assigned merely because an organism has a helical flagellar filament, follows a helical swimming trajectory, is a single-plane curved rod, or transiently becomes coccoid or filamentous.

Two mechanistically distinct graph branches are warranted:

1. **Peptidoglycan (PG)-sculpted helicity** in *Helicobacter pylori* and *Campylobacter jejuni*: regulated PG endopeptidase/carboxypeptidase activity and cytoskeletal/scaffolding proteins alter peptide stems and crosslinks, producing anisotropic wall mechanics and stable curvature/twist.
2. **Periplasmic-flagella-imposed morphology** in spirochetes: elastic forces between internal flagella and the cell cylinder impose species-specific waves or helices. This branch needs tighter phenotype qualification because *Borrelia burgdorferi* is usually described as **flat-wave**, not a true three-dimensional helical cell body. (charon2012theuniqueparadigm pages 2-4, charon2012theuniqueparadigm pages 4-5, nakamura2020spirocheteflagellaand pages 1-3)

The strongest immediately curatable backbone is therefore:

**shape proteins/PG hydrolases → altered PG peptide stems and crosslinks → asymmetric sacculus mechanics → cell curvature plus twist → helical cell body → enhanced movement or colonization in host-associated environments.**

---

## 1. Trait scope and boundaries

### 1.1 Positive operational definition

Curate “METPO:1000676” when microscopy or isolated-sacculus analysis demonstrates a stable corkscrew-like cell body with curvature and axial twist. Useful measurements include centerline torsion, helical pitch, radius, handedness, and three-dimensional reconstruction. In *H. pylori*, mutant sacculi reproduce the morphology of intact cells, directly identifying the PG sacculus as the shape-bearing structure. (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, sycuro2010peptidoglycancrosslinkingrelaxation pages 6-7, sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6)

### 1.2 Boundary cases

- **Curved rod:** curvature without clear axial twist is a nearby but distinct phenotype. Deletion of *H. pylori csd1/csd2/ccmA* or *C. jejuni pgp3* produces curved rods rather than wild-type helices. These mutant phenotypes are useful negative or intermediate states, not instances of full helicity. (frirdich2023multiplecampylobacterjejuni pages 2-3, sycuro2010peptidoglycancrosslinkingrelaxation pages 2-4)
- **Flat-wave spirochete:** *B. burgdorferi* has a planar waveform—reported amplitude 0.78 µm and wavelength 2.83 µm—rather than an unambiguous three-dimensional helix. It should be included only if TraitMech intentionally treats “spiral/wavy” as within scope; otherwise map it to a separate waveform trait. (charon2012theuniqueparadigm pages 2-4)
- **Helical flagellum:** the flagellar filament is an appendage, not the cell body. In *B. burgdorferi*, purified periplasmic flagella are left-handed helices with approximately 0.28-µm diameter and 1.48-µm pitch, whereas the cell body is a flat wave. (charon2012theuniqueparadigm pages 2-4)
- **Helical swimming trajectory:** circular or corkscrew movement is an assay outcome and cannot alone establish cell-body helicity.
- **Coccoid transition:** aged or stressed *Helicobacter/Campylobacter* cells may become spherical; this is a morphological transition away from the target trait, not another expression of helicity.
- **External flagella on helical rods:** *H. pylori* and *C. jejuni* body shape is principally encoded by PG architecture; their external flagella primarily generate propulsion. In spirochetes, internal flagella can additionally determine body shape.

### 1.3 Recommended trait-assignment rule

Require evidence for the **cell body**, preferably from three-dimensional imaging or a combination of phase/DIC microscopy and isolated sacculi. Record `curved rod`, `flat wave`, and `helical` separately whenever the source does so. Do not infer the target from a genus name such as *Spirillum* or from “spiral-shaped” wording without inspection of the authors’ morphology definition.

---

## 2. Candidate nodes grouped by type

### 2.1 Trait and taxon nodes

- **helical shaped:** “METPO:1000676”
- **parent morphology:** “METPO:1000666”
- *Helicobacter pylori* — taxon label; verify the current NCBITaxon CURIE during ingestion.
- *Campylobacter jejuni* — taxon label; verify NCBITaxon CURIE during ingestion.
- *Borrelia burgdorferi*, *Leptospira interrogans*, *Treponema pallidum* — label-only here pending accession validation.
- Boundary phenotypes: `curved rod`, `straight rod`, `flat-wave cell body`, `coccoid cell`.

### 2.2 Cellular structures and localizations

- Peptidoglycan sacculus / cell wall — **GO:0009274** is a suitable general bacterial PG-based cell-wall term, subject to ontology-version confirmation.
- Periplasmic space — **GO:0042597**.
- Cytoplasmic membrane / inner membrane.
- Cytoskeleton and bactofilin polymers.
- Periplasmic flagellum/endoflagellum; flagellar ribbon; motor, hook and filament.
- Membrane-associated *H. pylori* “shapeosome/shapesome” complex—candidate label-only complex.

### 2.3 *H. pylori* genes and proteins

- **Csd1:** M23-family D,D-endopeptidase; cleaves PG crosslinks.
- **Csd2:** M23-family homolog and stabilizing partner of Csd1.
- **Csd3/HdpA:** D,D-endopeptidase with weak D,D-carboxypeptidase activity.
- **Csd4:** M14 D,L-carboxypeptidase, trimming monomeric tripeptides to dipeptides.
- **Csd6:** L,D-carboxypeptidase, converting tetrapeptides to tripeptides.
- **Csd5:** inner-membrane scaffold whose SH3 domain binds PG; interacts with CcmA, MurF and ATP synthase.
- **Csd7:** candidate adaptor linking the Csd1–Csd2 module to CcmA polymers; currently supported here through review synthesis rather than a directly extracted primary experiment.
- **CcmA:** polymerizing bactofilin/cytoskeletal protein.
- **MurF:** cytosolic PG-precursor ligase/synthase interacting with Csd5.
- **Slt:** lytic transglycosylase included in the proposed shape network.

Csd1 is reported to cleave tetra–pentapeptide crosslinks; Csd2 stabilizes Csd1; Csd3 has D,D-endopeptidase and weak D,D-carboxypeptidase activities; and Csd4/Csd6 successively alter uncrosslinked peptide stems. (salama2020cellmorphologyas pages 1-2, salama2020cellmorphologyas pages 2-4)

### 2.4 *C. jejuni* genes and proteins

- **Pgp2:** L,D-carboxypeptidase converting tetrapeptides to tripeptides.
- **Pgp1:** D,L-carboxypeptidase converting the resulting tripeptides to dipeptides.
- **Pgp3:** D,D-carboxypeptidase and D,D-endopeptidase; catalytic access involves substrate-dependent conformational change.
- **CJJ81176_1104:** putative bactofilin.
- **CJJ81176_1105, CJJ81176_1228, CJJ81176_0166:** M23-domain candidates in the 2023 study; their precise biochemical assignments should remain provisional in a graph restricted to evidence available through 2024.
- **Ape1:** PG O-acetyl esterase; deletion increased O-acetylated peptides from approximately 2% to 10% and produced highly curved cells, but its relationship to full helicity is indirect. (lin2021peptidoglycanbindingby pages 46-51)

Pgp2 generates the tripeptide substrate consumed by Pgp1, while loss of either enzyme makes normally helical cells rod-like. Pgp3 provides another, nonidentical PG-remodeling route. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2023multiplecampylobacterjejuni pages 2-3)

### 2.5 Spirochete machinery

- Periplasmic flagellar filament/ribbon.
- **FlaB:** major flagellin/core filament protein.
- **FlaA:** sheath/minor flagellin affecting filament mechanics.
- **FlgE:** hook protein.
- **FliF/FliG2/MotB:** motor or switch components.
- **FlhF:** SRP-like GTPase controlling periplasmic-flagella number and configuration.
- Elastic protoplasmic cell cylinder and PG wall.

In *B. burgdorferi*, loss of *flaB*, *flgE*, *fliF*, or *fliG2* eliminates the normal flat wave and yields straight rods. The accepted physical interpretation is reciprocal force balance between a comparatively straight cell cylinder and constrained helical periplasmic flagella. (charon2012theuniqueparadigm pages 2-4, charon2012theuniqueparadigm pages 4-5)

### 2.6 Chemicals and molecular states

- PG glycan strands and peptide stems.
- Tetrapeptide, tripeptide, dipeptide and pentapeptide stems.
- mDAP–D-Ala crosslinks; tetra–pentapeptide, tetra–tetrapeptide and tetra–tripeptide dimers.
- PG O-acetylation.
- Zn²⁺: required in the reported purified Pgp1 assay; Pgp1 was tested at 5 μM with 1 mg/mL PG and 0.005 M ZnCl₂, pH 4.8, 37°C for 4 h. This is assay-specific and should not become a physiological causal requirement without in-vivo evidence. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 11-12)
- EDTA: assay inhibitor/metal chelator, not established as a specific cellular helicity regulator.

### 2.7 Processes and functions

- PG crosslink hydrolysis/relaxation.
- PG peptide-stem trimming.
- Localized or anisotropic PG remodeling.
- Bactofilin polymerization and shape-complex organization.
- Flagellar assembly and elastic coupling to the cell cylinder.
- Cell curvature, axial twist, helical pitch and handedness.
- Motility in mucus or viscous media; gastric/intestinal colonization.

---

## 3. Candidate causal edges

The table below summarizes the graph backbone. “Strong” denotes direct genetics, biochemistry, structural analysis or a closely linked combination; “moderate” denotes mechanistic inference from muropeptides/interactions; “uncertain” denotes review-supported, taxon-restricted or unresolved claims.

| Proposed subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---|---|---|
| *H. pylori* Csd1 — **promotes hydrolysis of** → PG crosslinks | Sycuro et al., May 2010, DOI [10.1016/j.cell.2010.03.046](https://doi.org/10.1016/j.cell.2010.03.046): mutants showed “26–49% increased tetrapentapeptide crosslinked dimers” and the catalytic H250A allele phenocopied deletion. (sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6) | **Moderate/strong.** Catalytic requirement and muropeptides support the edge, but the 2010 enzyme assignment was partly inferred rather than directly assayed. |
| *H. pylori* Csd2 — **stabilizes/interacts with** → Csd1 | Salama, April 2020, DOI [10.1016/j.mib.2019.12.002](https://doi.org/10.1016/j.mib.2019.12.002): “Csd2 stabilizes Csd1 through heterodimer formation.” (salama2020cellmorphologyas pages 1-2) | **Moderate.** Review-supported; link the primary interaction paper before final YAML acceptance. |
| *H. pylori* Csd3 — **modifies** → PG crosslink species | Sycuro et al.: Δ*csd3* decreased tetra–tetra and tetra–tri crosslinks by >30% and increased tetra–penta species by 20–50%. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10, sycuro2010peptidoglycancrosslinkingrelaxation pages 6-7) | **Strong association; uncertain exact 2010 reaction.** Later work supports D,D-endopeptidase/weak carboxypeptidase activity. |
| Loss of *H. pylori csd1/csd2/ccmA* — **causes** → curved-rod rather than helical morphology | “Single deletions of csd1, csd2, or ccmA each produce curved-rod morphology.” (sycuro2010peptidoglycancrosslinkingrelaxation pages 2-4) | **Strong, taxon-specific.** Useful negative/intermediate edges. |
| Loss of *H. pylori csd3* — **causes** → heterogeneous excessive curvature | Among 100 cells: 17% straight/bent, 53% C-shaped, 25% coiled/figure-eight, and 5% coccoid. (sycuro2010peptidoglycancrosslinkingrelaxation pages 2-4) | **Strong.** Do not simplify to “loss causes straight cells.” |
| Increased tetra–pentapeptide crosslinks — **reduces** → normal helical curvature/twist | All four shape mutants had 26–49% more tetra–pentapeptide dimers and 8–33% fewer tetrapeptide monomers; intact cells and sacculi lost wild-type shape. (sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6) | **Strong correlation; causal direction mechanistically plausible.** Prefer `negatively_regulates` or `associated_with_loss_of` unless direct reconstitution is required. |
| Coordinated PG crosslink relaxation — **enables** → *H. pylori* helical curvature and twist | The foundational conclusion is that coordinated protein action “relaxes peptidoglycan crosslinking, enabling helical cell curvature and twist.” (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8) | **Strong high-level edge** and best match to the existing graph summary. |
| Csd4 — **converts** → monomeric tripeptides to dipeptides | Review: “Csd4 is an M14 D,L-carboxypeptidase trimming tripeptides to dipeptides.” (salama2020cellmorphologyas pages 1-2, salama2020cellmorphologyas pages 2-4) | **Biochemically supported but primary-source link needed** before strict curation. |
| Csd6 — **converts** → tetrapeptides to tripeptides | Review: “Csd6 is an L,D-carboxypeptidase cleaving tetrapeptides to tripeptides.” (salama2020cellmorphologyas pages 2-4) | **Moderate here.** Primary DOI is 10.1074/jbc.M115.658781, but full text was not retrieved; verify there. |
| Csd5 SH3 domain — **binds** → PG | Blair et al., September 2018, DOI [10.1111/mmi.14087](https://doi.org/10.1111/mmi.14087): “Csd5 interacts directly with peptidoglycan via its C-terminal SH3” domain. (blair2018thehelicobacterpylori pages 1-3) | **Strong direct interaction.** |
| Csd5 — **interacts with** → CcmA and MurF | Immunoprecipitation/mass spectrometry identified MurF, CcmA and ATP-synthase proteins; the N-terminal transmembrane domain promoted these interactions. (blair2018thehelicobacterpylori pages 1-3, blair2018thehelicobacterpylori pages 23-27) | **Strong physical-interaction edges.** Interaction does not alone establish activation or localization direction. |
| Csd5-centered membrane complex — **promotes** → helical shape | Authors conclude that Csd5 promotes helical shape in a membrane-associated multiprotein complex linking wall, PG precursor synthesis and cytoskeleton. (blair2018thehelicobacterpylori pages 1-3) | **Strong composite model.** Keep “shapeosome” as a candidate complex, not a universally conserved pathway. |
| Csd7 — **links** → Csd1–Csd2 to CcmA polymers | 2020 synthesis describes Csd1/Csd2 as linked “via Csd7 to CcmA polymers.” (salama2020cellmorphologyas pages 2-4) | **Uncertain/review-supported.** Retrieve and cite the direct Csd7 study before curation. |
| *H. pylori* helical shape — **promotes** → efficient gastric colonization | Shape mutants were attenuated despite retained flagellation; Δ*csd6* straight cells were modestly attenuated after one week. (salama2020cellmorphologyas pages 4-5, sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8) | **Strong phenotype association, partly confounded by each protein’s other functions.** |
| *H. pylori* helical shape — **increases** → movement through gastric mucin | Helical cells swam 7–21% faster in gastric mucin; loss of helicity increased immobilization by 30–40%. (salama2020cellmorphologyas pages 4-5) | **Assay-specific.** Curate with `gastric mucin` and experimental context, not as universal motility enhancement. |
| *C. jejuni* Pgp2 — **converts** → tetrapeptide to tripeptide | Frirdich et al., April 2023, DOI [10.3389/fmicb.2023.1162806](https://doi.org/10.3389/fmicb.2023.1162806): Pgp2 is an L,D-carboxypeptidase converting tetrapeptides to tripeptides. (frirdich2023multiplecampylobacterjejuni pages 2-3) | **Strong enzyme edge.** |
| Pgp2 product — **is substrate for** → Pgp1 | The 2023 synthesis describes Pgp2-generated tripeptide as Pgp1 substrate. (frirdich2023multiplecampylobacterjejuni pages 2-3) | **Strong pathway ordering.** |
| *C. jejuni* Pgp1 — **converts** → tripeptide to dipeptide | Frirdich et al., March 2012, DOI [10.1371/journal.ppat.1002602](https://doi.org/10.1371/journal.ppat.1002602): Pgp1 is a D,L-carboxypeptidase “cleaving monomeric tripeptides to dipeptides.” (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | **Strong direct biochemical edge.** |
| Loss of Pgp1 or Pgp2 — **causes** → rod-shaped *C. jejuni* | Both deletion strains became rods and had altered PG muropeptide profiles. (frirdich2023multiplecampylobacterjejuni pages 2-3) | **Strong direct genetic edge.** |
| *C. jejuni* Pgp3 — **hydrolyzes** → D,D crosslinks and pentapeptide termini | Pgp3 has D,D-endopeptidase and D,D-carboxypeptidase activity; prior cleavage on one side is required for substrate recognition. DOI [10.1038/s41467-019-13934-4](https://doi.org/10.1038/s41467-019-13934-4), January 2020. (frirdich2023multiplecampylobacterjejuni pages 2-3) | **Strong biochemical edge.** |
| Loss of Pgp3 — **causes** → curved-rod morphology | The 2023 study reports Δ*pgp3* curved rods rather than the Δ*pgp1/2* straight-rod state. (frirdich2023multiplecampylobacterjejuni pages 2-3) | **Strong and taxon-specific.** |
| CJJ81176_1104/1105/1228/0166 dosage — **modulates** → *C. jejuni* curvature and PG composition | Deletions produced varying curved rods; overexpressed 1104 reduced curvature, while overexpressed 1105 increased it, with muropeptide changes. (frirdich2023multiplecampylobacterjejuni pages 2-3) | **Strong phenotype edges; biochemical predicates uncertain through 2024.** |
| *C. jejuni* helical-shape pathway — **promotes** → chick colonization | Δ*pgp1* had a >10³-fold colonization defect and motility/biofilm defects. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | **Strong but pleiotropic.** Prefer `Pgp1-dependent morphology/pathway promotes colonization`; avoid attributing the entire effect solely to geometry. |
| Spirochete periplasmic flagella — **exert reciprocal elastic force on** → cell cylinder | The straight cylinder deforms helical flagella in the confined periplasm, while the flagella bend the cylinder into the observed waveform. (charon2012theuniqueparadigm pages 4-5) | **Strong biophysical model supported by genetics and measured geometry.** |
| Loss of *B. burgdorferi flaB/flgE/fliF/fliG2* — **causes** → straight-rod cell body | Flagellar-filament, hook, motor and switch mutants form straight rods rather than flat waves. (charon2012theuniqueparadigm pages 2-4, charon2012theuniqueparadigm pages 4-5) | **Strong, but object should be `flat-wave morphology`, not automatically “helical shaped.”** |
| FlhF — **controls** → periplasmic-flagella number/configuration | Wild type has 7–11 PFs per pole; Δ*flhF* averaged 4 ± 2 and failed to make the normal flat ribbon. DOI [10.1111/mmi.14482](https://doi.org/10.1111/mmi.14482), February 2020. | **Strong direct genetics/cryo-ET; morphology is flat-wave-specific.** |
| Periplasmic-flagellar organization — **promotes** → spirochete motility and infection | Motility mutants involving FlaB, MotB or CheA2 failed to infect mice or migrate from ticks in summarized studies. (wolgemuth2015flagellarmotilityof pages 4-6) | **Strong functional association but not a shape-only edge.** |

A compact cross-taxon graph view is provided here:

| Taxon/module | subject | predicate | object | evidence strength | DOI |
|---|---|---|---|---|---|
| *Helicobacter pylori* PG remodeling | Csd1 | promotes | peptidoglycan crosslink relaxation | genetic + muropeptide inference (no direct biochemistry in 2010 Cell) (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6) | 10.1016/j.cell.2010.03.046 |
| *H. pylori* PG remodeling | Csd2 | promotes | peptidoglycan crosslink relaxation | genetic + muropeptide inference; likely partner/stabilizer of Csd1 from review (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10, salama2020cellmorphologyas pages 1-2) | 10.1016/j.cell.2010.03.046; 10.1016/j.mib.2019.12.002 |
| *H. pylori* PG remodeling | Csd3 | promotes | peptidoglycan crosslink relaxation | genetic + muropeptide inference; direct enzymatic activity supported by review, not primary source here (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10, salama2020cellmorphologyas pages 1-2) | 10.1016/j.cell.2010.03.046; 10.1016/j.mib.2019.12.002 |
| *H. pylori* shape scaffold | CcmA | promotes | helical cell shape | strong genetic evidence; biochemical mechanism still partly inferred (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, salama2020cellmorphologyas pages 1-2) | 10.1016/j.cell.2010.03.046; 10.1016/j.mib.2019.12.002 |
| *H. pylori* cell wall | peptidoglycan crosslink relaxation | enables | helical cell curvature and twist | strong primary evidence (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6) | 10.1016/j.cell.2010.03.046 |
| *H. pylori* cell wall | increased tetrapentapeptide crosslinks | associated_with_loss_of | helical shape | strong muropeptide-phenotype association (sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6) | 10.1016/j.cell.2010.03.046 |
| *H. pylori* shape complex | Csd5 | binds | peptidoglycan | direct interaction evidence (blair2018thehelicobacterpylori pages 1-3, blair2018thehelicobacterpylori pages 23-27) | 10.1111/mmi.14087 |
| *H. pylori* shape complex | Csd5 | interacts_with | MurF | direct interaction evidence (blair2018thehelicobacterpylori pages 1-3, blair2018thehelicobacterpylori pages 23-27) | 10.1111/mmi.14087 |
| *H. pylori* shape complex | Csd5 | interacts_with | CcmA | direct interaction evidence (blair2018thehelicobacterpylori pages 1-3, blair2018thehelicobacterpylori pages 23-27) | 10.1111/mmi.14087 |
| *H. pylori* shape complex | Csd5 | promotes | helical cell shape | strong genetic + interaction evidence (blair2018thehelicobacterpylori pages 1-3) | 10.1111/mmi.14087 |
| *H. pylori* PG trimming | Csd4 | trims | monomeric tripeptides to dipeptides | review-supported biochemical summary; not directly extracted from primary article here (salama2020cellmorphologyas pages 1-2, salama2020cellmorphologyas pages 2-4) | 10.1016/j.mib.2019.12.002 |
| *H. pylori* PG trimming | Csd6 | trims | tetrapeptides to tripeptides | review-supported biochemical summary (salama2020cellmorphologyas pages 2-4, salama2020cellmorphologyas pages 4-5) | 10.1016/j.mib.2019.12.002 |
| *H. pylori* pathway organization | Csd7 | links | Csd1/Csd2 complex to CcmA polymers | review-supported/inferred network edge (salama2020cellmorphologyas pages 2-4) | 10.1016/j.mib.2019.12.002 |
| *H. pylori* virulence phenotype | helical cell shape | promotes | stomach colonization | strong genetic/pathogenesis evidence (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, salama2020cellmorphologyas pages 4-5) | 10.1016/j.cell.2010.03.046; 10.1016/j.mib.2019.12.002 |
| *Campylobacter jejuni* PG pathway | Pgp2 | converts | tetrapeptides to tripeptides | direct biochemical evidence summarized in primary/recent review-style source (frirdich2023multiplecampylobacterjejuni pages 2-3, lin2021peptidoglycanbindingby pages 46-51) | 10.3389/fmicb.2023.1162806; 10.14288/1.0401780 |
| *C. jejuni* PG pathway | Pgp1 | converts | tripeptides to dipeptides | strong direct biochemical/genetic evidence (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2023multiplecampylobacterjejuni pages 2-3) | 10.1371/journal.ppat.1002602; 10.3389/fmicb.2023.1162806 |
| *C. jejuni* PG pathway | Pgp2 | supplies substrate_for | Pgp1 | strong pathway inference supported by enzyme activities (frirdich2023multiplecampylobacterjejuni pages 2-3) | 10.3389/fmicb.2023.1162806 |
| *C. jejuni* PG remodeling | Pgp3 | cleaves | PG crosslinks and pentapeptide termini | direct biochemical evidence (DD-carboxypeptidase/DD-endopeptidase) (frirdich2023multiplecampylobacterjejuni pages 2-3, salama2020cellmorphologyas pages 2-4) | 10.3389/fmicb.2023.1162806; 10.1038/s41467-019-13934-4 |
| *C. jejuni* morphology | loss of Pgp1 | causes | rod-shaped cells | strong direct genetic evidence (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602 |
| *C. jejuni* morphology | loss of Pgp2 | causes | rod/football-shaped cells | strong direct genetic evidence (lin2021peptidoglycanbindingby pages 46-51, frirdich2023multiplecampylobacterjejuni pages 2-3) | 10.14288/1.0401780; 10.3389/fmicb.2023.1162806 |
| *C. jejuni* morphology | loss of Pgp3 | causes | curved-rod morphology | strong direct genetic evidence (frirdich2023multiplecampylobacterjejuni pages 2-3) | 10.3389/fmicb.2023.1162806 |
| *C. jejuni* pathogenesis | helical cell shape | promotes | chick colonization | strong direct phenotype evidence (>10^3-fold defect for Δpgp1) (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602 |
| *C. jejuni* pathogenesis | loss of Pgp1 | reduces | motility/biofilm fitness | strong direct phenotype evidence (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2) | 10.1371/journal.ppat.1002602 |
| *C. jejuni* candidate 1104 | CJJ81176_1104 (bactofilin-like) | modulates | degree of helical curvature | direct genetic evidence, mechanism partly inferred (frirdich2023multiplecampylobacterjejuni pages 2-3) | 10.3389/fmicb.2023.1162806 |
| *C. jejuni* candidate 1105 | CJJ81176_1105 | modulates | degree of helical curvature | direct genetic evidence; predicted M23 peptidase mechanism (frirdich2023multiplecampylobacterjejuni pages 2-3, lin2021peptidoglycanbindingby pages 46-51) | 10.3389/fmicb.2023.1162806; 10.14288/1.0401780 |
| *C. jejuni* candidate 1228 | CJJ81176_1228 | modulates | degree of helical curvature | direct genetic evidence; predicted M23 peptidase mechanism (frirdich2023multiplecampylobacterjejuni pages 2-3, lin2021peptidoglycanbindingby pages 46-51) | 10.3389/fmicb.2023.1162806; 10.14288/1.0401780 |
| *C. jejuni* candidate 0166 | CJJ81176_0166 | modulates | degree of helical curvature | direct genetic evidence; precise activity unresolved in 2023 paper (frirdich2023multiplecampylobacterjejuni pages 2-3) | 10.3389/fmicb.2023.1162806 |
| *Borrelia burgdorferi* morphomechanics | periplasmic flagella | impose_force_balance_on | cell body | strong review-supported synthesis from mutant/biophysical evidence (charon2012theuniqueparadigm pages 4-5, nakamura2020spirocheteflagellaand pages 1-3) | 10.1146/annurev-micro-092611-150145; 10.3390/biom10040550 |
| *B. burgdorferi* morphology | FlaB | required_for | flat-wave/helical cell-body morphology | strong genetic evidence (charon2012theuniqueparadigm pages 2-4, charon2012theuniqueparadigm pages 4-5) | 10.1146/annurev-micro-092611-150145 |
| *B. burgdorferi* morphology | FlgE | required_for | flat-wave/helical cell-body morphology | strong genetic evidence from review synthesis (charon2012theuniqueparadigm pages 2-4, charon2012theuniqueparadigm pages 4-5) | 10.1146/annurev-micro-092611-150145 |
| *B. burgdorferi* morphology | loss of periplasmic flagella | causes | straight rod morphology | strong genetic/structural evidence (charon2012theuniqueparadigm pages 4-5, wolgemuth2015flagellarmotilityof pages 6-7) | 10.1146/annurev-micro-092611-150145; 10.1016/j.semcdb.2015.10.015 |
| *B. burgdorferi* recent assembly control | FlhF | controls | number and configuration of periplasmic flagella | strong direct genetic + cryo-ET evidence (nakamura2020spirocheteflagellaand pages 1-3) | 10.1111/mmi.14482 |
| *B. burgdorferi* recent assembly control | altered periplasmic flagella number/configuration | alters | morphology and motility | strong direct evidence (nakamura2020spirocheteflagellaand pages 1-3) | 10.1111/mmi.14482 |
| Spirochete boundary case | helical periplasmic flagellar filament | distinct_from | helical/flat-wave cell body | strong structural evidence; important exclusion edge for trait scope (charon2012theuniqueparadigm pages 2-4, liu2010cellulararchitectureof pages 8-9) | 10.1146/annurev-micro-092611-150145; 10.1016/j.jmb.2010.09.020 |


*Table: This table compiles the strongest candidate causal edges for curating the microbial helical-shaped trait, spanning peptidoglycan-remodeling mechanisms in Helicobacter and Campylobacter and periplasmic-flagella-driven morphogenesis in Borrelia. It distinguishes direct biochemical or genetic evidence from inferred or review-supported edges to guide cautious TraitMech curation.*

---

## 4. Current understanding and recent developments

### 4.1 2023: homologous proteins do not imply homologous morphogenesis

The principal 2023 advance was systematic analysis of four additional *C. jejuni* morphogenesis candidates: CJJ81176_1104, 1105, 1228 and 0166. Deletions generated distinct curved-rod phenotypes and altered PG profiles; dosage of 1104 and 1105 also changed both curvature and muropeptides. Critically, homologous proteins in *H. pylori* produced different PG or morphology effects. The authors therefore concluded that even related helical organisms can use divergent PG biosynthetic programs. (frirdich2023multiplecampylobacterjejuni pages 2-3)

**Expert interpretation:** a single pan-bacterial “helical-shape pathway” would be biologically misleading. TraitMech should use a conserved high-level node—`spatially regulated PG remodeling`—with taxon-specific child modules and reactions.

### 4.2 2024: dynamic cytoskeleton–hydrolase modules

Pöhl et al. reported that a bactofilin and an M23 endopeptidase colocalize at the inner curve of spiral-shaped *Rhodospirillum rubrum* and modulate curvature, extending the cytoskeleton–PG-hydrolase module beyond *Helicobacter/Campylobacter*. DOI [10.7554/eLife.86577.2](https://doi.org/10.7554/eLife.86577.2), January 2024. Because the retrieved evidence is abstract-level and describes curvature rather than quantified twist, this is a promising expansion node but not yet a core “helical shaped” edge.

### 4.3 2024: spirochete flagellar assembly and pathogenesis

Recent *B. burgdorferi* work identified FlgV as a motor-associated flagellar component. Loss of *flgV* produced fewer and shorter filaments, defective division and motility, and impaired dissemination/infection in mice. DOI [10.1038/s41467-024-54806-w](https://doi.org/10.1038/s41467-024-54806-w), November 2024. The evidence supports `FlgV → flagellar assembly → motility/dissemination`; it does **not yet support a clean FlgV → helical cell body edge** without directly extracted morphology measurements.

A 2024 *B. burgdorferi* DnaA preprint found that DnaA depletion impaired helical morphology and altered transcripts involved in flagella, elongation and division. DOI [10.1101/2024.06.08.598065](https://doi.org/10.1101/2024.06.08.598065), June 2024. This is broad, pleiotropic regulation and a preprint; it should not be curated as a direct morphogenesis edge.

### 4.4 Mechanistic consensus

Authoritative syntheses converge on a modular view: shape emerges from the mechanics of the load-bearing cell envelope, with enzymes changing local PG connectivity and cytoskeletal/scaffold systems controlling where and how strongly those enzymes act. For spirochetes, periplasmic flagella provide an additional internal mechanical scaffold. (salama2020cellmorphologyas pages 1-2, charon2012theuniqueparadigm pages 4-5, wolgemuth2015flagellarmotilityof pages 6-7)

---

## 5. Applications and real-world relevance

### 5.1 Anti-virulence targets

PG hydrolases and their scaffolds are candidate anti-virulence targets because disrupting the shape pathway can reduce host colonization without necessarily inhibiting growth. *H. pylori* shape mutants retained growth and flagellation yet colonized less efficiently; *C. jejuni* Δ*pgp1* was deficient in chick colonization by more than three orders of magnitude. (salama2020cellmorphologyas pages 4-5, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8)

This approach remains preclinical. A morphology inhibitor may also alter PG fragment release, innate immune recognition, wall integrity or division, so “shape-specific” pharmacology must be established experimentally. Δ*pgp1* PG, for example, activated Nod1 more strongly and elicited more epithelial IL-8 than wild-type material. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2)

### 5.2 Diagnostics and phenotypic assays

High-content microscopy, DIC imaging, automated centerline analysis, CellTool/MicrobeJ, purified sacculus imaging, HPLC–MS muropeptide profiling and cryo-electron tomography provide practical readouts for shape-pathway screens. The 2018 Csd5 work quantified side curvature across 188–382 cells per strain, illustrating the replication needed to distinguish partial curvature from full helicity. (blair2018thehelicobacterpylori pages 23-27)

### 5.3 Host-environment navigation

Shape can improve transport in structured, viscous host environments. In gastric mucin, helical *H. pylori* reportedly swam 7–21% faster and nonhelical cells were immobilized 30–40% more often. *C. jejuni* motor mechanics are adapted to high-viscosity intestinal milieus, although that 2024 evidence concerns flagellar motor output rather than generation of body helicity. (salama2020cellmorphologyas pages 4-5)

### 5.4 Biomimetics

Spirochete propulsion—rotation of internal flagella in a narrow periplasm—has been proposed as a design basis for autonomous, efficient microrobots. This is an engineering inspiration rather than an implemented TraitMech phenotype application. DOI [10.3390/biom10040550](https://doi.org/10.3390/biom10040550), April 2020. (nakamura2020spirocheteflagellaand pages 1-3)

---

## 6. Recommended graph organization

Rather than enlarging the existing ten-node `helical_shaped_pg_relaxation` graph indiscriminately, use three linked subgraphs:

### A. *H. pylori* shapeosome/PG-relaxation module

`CcmA polymers` → organize → `Csd1–Csd2–Csd7 module`

`Csd5` → binds → `PG`

`Csd5` → interacts_with → `MurF`

`Csd1/Csd3` → hydrolyze → `PG crosslinks`

`Csd6` → tetrapeptide-to-tripeptide trimming → `Csd4` → tripeptide-to-dipeptide trimming

`coordinated localized PG remodeling` → relaxes/redistributes → `PG crosslink architecture`

`anisotropic sacculus mechanics` → produces → `curvature + twist`

`curvature + twist` → realizes → “METPO:1000676”

### B. *C. jejuni* sequential peptide-stem-remodeling module

`Pgp2` → tetrapeptide-to-tripeptide → `Pgp1 substrate`

`Pgp1` → tripeptide-to-dipeptide → `remodeled PG`

`Pgp3` → D,D-endopeptidase/carboxypeptidase activity → `remodeled PG`

`CJJ81176_1104/1105/1228/0166` → modulate → `PG composition/curvature` **[activity unresolved through 2024]**

`remodeled PG` → supports → “METPO:1000676”

### C. Spirochete morphomechanical module

`flagellar motor/hook/filament assembly` → produces → `periplasmic flagellar ribbon`

`FlhF` → controls → `PF number/configuration`

`helical PF ribbon ↔ elastic force balance ↔ cell cylinder`

`force balance` → produces → `species-specific flat wave or helical body`

The final object must be phenotype-qualified: *Leptospira* may support true helical-body assignment, while *B. burgdorferi* usually supports `flat wave`, not “METPO:1000676.”

---

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not merge all spiral-like morphologies.** Curved rods, planar waves and true helices need distinct nodes.
2. **Do not equate helical flagellar filaments with helical cells.** This is especially important for spirochetes and externally flagellated curved rods. (charon2012theuniqueparadigm pages 2-4, liu2010cellulararchitectureof pages 8-9)
3. **Do not generalize homolog function across *H. pylori* and *C. jejuni*.** The 2023 comparative results explicitly show divergent outcomes. (frirdich2023multiplecampylobacterjejuni pages 2-3)
4. **Treat the 2010 Csd enzyme assignments carefully.** The original study inferred specific activities from LytM homology, catalytic mutants and muropeptide changes; later biochemical studies refine these reactions. (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10)
5. **Csd7 needs a direct primary citation.** The retrieved support is a 2020 review synthesis. (salama2020cellmorphologyas pages 2-4)
6. **Do not curate CJJ81176_1105/1228/0166 catalytic reactions from prediction alone.** Their effects on shape and PG were demonstrated in 2023, but precise activities were unresolved in the requested 2023–2024 window. (frirdich2023multiplecampylobacterjejuni pages 2-3)
7. **Do not assign causality from pleiotropic virulence phenotypes solely to shape.** PG composition, immune recognition, motility, division and envelope stress can change together. Δ*pgp1* is a clear example. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2)
8. **Mucin results are environmental and assay-specific.** Do not encode `helical shape universally increases motility`.
9. **DnaA and FlgV are not yet direct helicity determinants.** DnaA is pleiotropic and the 2024 result is a preprint; FlgV directly supports flagellar assembly/motility but requires morphology-resolved evidence for a body-shape edge.
10. **Avoid unverified database accessions.** Protein and taxon labels above should be reconciled against the exact strain used in each paper before assigning UniProt, NCBITaxon, KEGG or Rhea CURIEs.

---

## DOI-first bibliography

1. Sycuro LK et al. **Peptidoglycan Crosslinking Relaxation Promotes *Helicobacter pylori*’s Helical Shape and Stomach Colonization.** *Cell*. Published May 2010. [https://doi.org/10.1016/j.cell.2010.03.046](https://doi.org/10.1016/j.cell.2010.03.046). (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8, sycuro2010peptidoglycancrosslinkingrelaxation pages 2-4, sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6)
2. Frirdich E et al. **Multiple *Campylobacter jejuni* proteins affecting the peptidoglycan structure and the degree of helical cell curvature.** *Frontiers in Microbiology*. Published April 2023. [https://doi.org/10.3389/fmicb.2023.1162806](https://doi.org/10.3389/fmicb.2023.1162806). (frirdich2023multiplecampylobacterjejuni pages 2-3)
3. Blair KM et al. **The *Helicobacter pylori* cell shape promoting protein Csd5 interacts with the cell wall, MurF, and the bacterial cytoskeleton.** *Molecular Microbiology*. Published September 2018. [https://doi.org/10.1111/mmi.14087](https://doi.org/10.1111/mmi.14087). (blair2018thehelicobacterpylori pages 1-3, blair2018thehelicobacterpylori pages 23-27)
4. Salama NR. **Cell morphology as a virulence determinant: lessons from *Helicobacter pylori*.** *Current Opinion in Microbiology*. Published April 2020. [https://doi.org/10.1016/j.mib.2019.12.002](https://doi.org/10.1016/j.mib.2019.12.002). (salama2020cellmorphologyas pages 1-2, salama2020cellmorphologyas pages 2-4, salama2020cellmorphologyas pages 4-5)
5. Frirdich E et al. **Peptidoglycan-Modifying Enzyme Pgp1 Is Required for Helical Cell Shape and Pathogenicity Traits in *Campylobacter jejuni*.** *PLoS Pathogens*. Published March 2012. [https://doi.org/10.1371/journal.ppat.1002602](https://doi.org/10.1371/journal.ppat.1002602). (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2, frirdich2012peptidoglycanmodifyingenzymepgp1 pages 11-12)
6. Min K et al. **Peptidoglycan reshaping by a noncanonical peptidase for helical cell shape in *Campylobacter jejuni*.** *Nature Communications*. Published January 2020. [https://doi.org/10.1038/s41467-019-13934-4](https://doi.org/10.1038/s41467-019-13934-4). (frirdich2023multiplecampylobacterjejuni pages 2-3)
7. Charon NW et al. **The Unique Paradigm of Spirochete Motility and Chemotaxis.** *Annual Review of Microbiology*. Published October 2012. [https://doi.org/10.1146/annurev-micro-092611-150145](https://doi.org/10.1146/annurev-micro-092611-150145). (charon2012theuniqueparadigm pages 2-4, charon2012theuniqueparadigm pages 4-5)
8. Liu J et al. **Cellular architecture of *Treponema pallidum*: novel flagellum, periplasmic cone, and cell envelope as revealed by cryo-electron tomography.** *Journal of Molecular Biology*. Published November 2010. [https://doi.org/10.1016/j.jmb.2010.09.020](https://doi.org/10.1016/j.jmb.2010.09.020). (liu2010cellulararchitectureof pages 8-9, liu2010cellulararchitectureof pages 7-8)
9. Wolgemuth CW. **Flagellar motility of the pathogenic spirochetes.** *Seminars in Cell & Developmental Biology*. Published October 2015. [https://doi.org/10.1016/j.semcdb.2015.10.015](https://doi.org/10.1016/j.semcdb.2015.10.015). (wolgemuth2015flagellarmotilityof pages 6-7, wolgemuth2015flagellarmotilityof pages 4-6)
10. Nakamura S. **Spirochete Flagella and Motility.** *Biomolecules*. Published April 2020. [https://doi.org/10.3390/biom10040550](https://doi.org/10.3390/biom10040550). (nakamura2020spirocheteflagellaand pages 1-3)
11. Zhang K et al. **FlhF regulates the number and configuration of periplasmic flagella in *Borrelia burgdorferi*.** *Molecular Microbiology*. Published February 2020. [https://doi.org/10.1111/mmi.14482](https://doi.org/10.1111/mmi.14482).
12. Pöhl S et al. **A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.** *eLife*. Version published January 2024. [https://doi.org/10.7554/eLife.86577.2](https://doi.org/10.7554/eLife.86577.2).
13. Zamba-Campero M et al. **Broadly conserved FlgV controls flagellar assembly and *Borrelia burgdorferi* dissemination in mice.** *Nature Communications*. Published November 2024. [https://doi.org/10.1038/s41467-024-54806-w](https://doi.org/10.1038/s41467-024-54806-w).
14. Krusenstjerna AC et al. **DnaA modulates the gene expression and morphology of the Lyme disease spirochete.** *bioRxiv*. Posted June 2024. [https://doi.org/10.1101/2024.06.08.598065](https://doi.org/10.1101/2024.06.08.598065). **Preprint; not recommended for direct graph curation.**

References

1. (charon2012theuniqueparadigm pages 2-4): Nyles W. Charon, Andrew Cockburn, Chunhao Li, Jun Liu, Kelly A. Miller, Michael R. Miller, Md. A. Motaleb, and Charles W. Wolgemuth. The unique paradigm of spirochete motility and chemotaxis. Annual Review of Microbiology, 66:349-370, Oct 2012. URL: https://doi.org/10.1146/annurev-micro-092611-150145, doi:10.1146/annurev-micro-092611-150145. This article has 243 citations and is from a peer-reviewed journal.

2. (charon2012theuniqueparadigm pages 4-5): Nyles W. Charon, Andrew Cockburn, Chunhao Li, Jun Liu, Kelly A. Miller, Michael R. Miller, Md. A. Motaleb, and Charles W. Wolgemuth. The unique paradigm of spirochete motility and chemotaxis. Annual Review of Microbiology, 66:349-370, Oct 2012. URL: https://doi.org/10.1146/annurev-micro-092611-150145, doi:10.1146/annurev-micro-092611-150145. This article has 243 citations and is from a peer-reviewed journal.

3. (nakamura2020spirocheteflagellaand pages 1-3): Shuichi Nakamura. Spirochete flagella and motility. Biomolecules, 10:550, Apr 2020. URL: https://doi.org/10.3390/biom10040550, doi:10.3390/biom10040550. This article has 70 citations.

4. (sycuro2010peptidoglycancrosslinkingrelaxation pages 7-8): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

5. (sycuro2010peptidoglycancrosslinkingrelaxation pages 6-7): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

6. (sycuro2010peptidoglycancrosslinkingrelaxation pages 5-6): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

7. (frirdich2023multiplecampylobacterjejuni pages 2-3): Emilisa Frirdich, Jenny Vermeulen, Jacob Biboy, Waldemar Vollmer, and Erin C. Gaynor. Multiple campylobacter jejuni proteins affecting the peptidoglycan structure and the degree of helical cell curvature. Frontiers in Microbiology, Apr 2023. URL: https://doi.org/10.3389/fmicb.2023.1162806, doi:10.3389/fmicb.2023.1162806. This article has 11 citations and is from a peer-reviewed journal.

8. (sycuro2010peptidoglycancrosslinkingrelaxation pages 2-4): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

9. (salama2020cellmorphologyas pages 1-2): Nina R Salama. Cell morphology as a virulence determinant: lessons from helicobacter pylori. Apr 2020. URL: https://doi.org/10.1016/j.mib.2019.12.002, doi:10.1016/j.mib.2019.12.002. This article has 44 citations and is from a peer-reviewed journal.

10. (salama2020cellmorphologyas pages 2-4): Nina R Salama. Cell morphology as a virulence determinant: lessons from helicobacter pylori. Apr 2020. URL: https://doi.org/10.1016/j.mib.2019.12.002, doi:10.1016/j.mib.2019.12.002. This article has 44 citations and is from a peer-reviewed journal.

11. (lin2021peptidoglycanbindingby pages 46-51): Chang Sheng-Huei Lin. Peptidoglycan binding by pgp2 and ape1 determines campylobacter jejuni helical cell shape. ArXiv, Jan 2021. URL: https://doi.org/10.14288/1.0401780, doi:10.14288/1.0401780. This article has 0 citations.

12. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 1-2): Emilisa Frirdich, Jacob Biboy, Calvin Adams, Jooeun Lee, Jeremy Ellermeier, Lindsay Davis Gielda, Victor J. DiRita, Stephen E. Girardin, Waldemar Vollmer, and Erin C. Gaynor. Peptidoglycan-modifying enzyme pgp1 is required for helical cell shape and pathogenicity traits in campylobacter jejuni. PLoS Pathogens, 8:e1002602, Mar 2012. URL: https://doi.org/10.1371/journal.ppat.1002602, doi:10.1371/journal.ppat.1002602. This article has 139 citations and is from a highest quality peer-reviewed journal.

13. (frirdich2012peptidoglycanmodifyingenzymepgp1 pages 11-12): Emilisa Frirdich, Jacob Biboy, Calvin Adams, Jooeun Lee, Jeremy Ellermeier, Lindsay Davis Gielda, Victor J. DiRita, Stephen E. Girardin, Waldemar Vollmer, and Erin C. Gaynor. Peptidoglycan-modifying enzyme pgp1 is required for helical cell shape and pathogenicity traits in campylobacter jejuni. PLoS Pathogens, 8:e1002602, Mar 2012. URL: https://doi.org/10.1371/journal.ppat.1002602, doi:10.1371/journal.ppat.1002602. This article has 139 citations and is from a highest quality peer-reviewed journal.

14. (sycuro2010peptidoglycancrosslinkingrelaxation pages 8-10): Laura K. Sycuro, Zachary Pincus, Kimberley D. Gutierrez, Jacob Biboy, Chelsea A. Stern, Waldemar Vollmer, and Nina R. Salama. Peptidoglycan crosslinking relaxation promotes helicobacter pylori's helical shape and stomach colonization. Cell, 141:822-833, May 2010. URL: https://doi.org/10.1016/j.cell.2010.03.046, doi:10.1016/j.cell.2010.03.046. This article has 356 citations and is from a highest quality peer-reviewed journal.

15. (blair2018thehelicobacterpylori pages 1-3): Kris M. Blair, Kevin S. Mears, Jennifer A. Taylor, Jutta Fero, Lisa A. Jones, Philip R. Gafken, John C. Whitney, and Nina R. Salama. The helicobacter pylori cell shape promoting protein csd5 interacts with the cell wall, murf, and the bacterial cytoskeleton. Molecular Microbiology, 110:114-127, Sep 2018. URL: https://doi.org/10.1111/mmi.14087, doi:10.1111/mmi.14087. This article has 37 citations and is from a domain leading peer-reviewed journal.

16. (blair2018thehelicobacterpylori pages 23-27): Kris M. Blair, Kevin S. Mears, Jennifer A. Taylor, Jutta Fero, Lisa A. Jones, Philip R. Gafken, John C. Whitney, and Nina R. Salama. The helicobacter pylori cell shape promoting protein csd5 interacts with the cell wall, murf, and the bacterial cytoskeleton. Molecular Microbiology, 110:114-127, Sep 2018. URL: https://doi.org/10.1111/mmi.14087, doi:10.1111/mmi.14087. This article has 37 citations and is from a domain leading peer-reviewed journal.

17. (salama2020cellmorphologyas pages 4-5): Nina R Salama. Cell morphology as a virulence determinant: lessons from helicobacter pylori. Apr 2020. URL: https://doi.org/10.1016/j.mib.2019.12.002, doi:10.1016/j.mib.2019.12.002. This article has 44 citations and is from a peer-reviewed journal.

18. (wolgemuth2015flagellarmotilityof pages 4-6): Charles W. Wolgemuth. Flagellar motility of the pathogenic spirochetes. Seminars in cell & developmental biology, 46:104-12, Oct 2015. URL: https://doi.org/10.1016/j.semcdb.2015.10.015, doi:10.1016/j.semcdb.2015.10.015. This article has 112 citations and is from a peer-reviewed journal.

19. (wolgemuth2015flagellarmotilityof pages 6-7): Charles W. Wolgemuth. Flagellar motility of the pathogenic spirochetes. Seminars in cell & developmental biology, 46:104-12, Oct 2015. URL: https://doi.org/10.1016/j.semcdb.2015.10.015, doi:10.1016/j.semcdb.2015.10.015. This article has 112 citations and is from a peer-reviewed journal.

20. (liu2010cellulararchitectureof pages 8-9): Jun Liu, Jerrilyn K. Howell, Sherille D. Bradley, Yesha Zheng, Z. Hong Zhou, and Steven J. Norris. Cellular architecture of treponema pallidum: novel flagellum, periplasmic cone, and cell envelope as revealed by cryo electron tomography. Journal of molecular biology, 403 4:546-61, Nov 2010. URL: https://doi.org/10.1016/j.jmb.2010.09.020, doi:10.1016/j.jmb.2010.09.020. This article has 166 citations and is from a domain leading peer-reviewed journal.

21. (liu2010cellulararchitectureof pages 7-8): Jun Liu, Jerrilyn K. Howell, Sherille D. Bradley, Yesha Zheng, Z. Hong Zhou, and Steven J. Norris. Cellular architecture of treponema pallidum: novel flagellum, periplasmic cone, and cell envelope as revealed by cryo electron tomography. Journal of molecular biology, 403 4:546-61, Nov 2010. URL: https://doi.org/10.1016/j.jmb.2010.09.020, doi:10.1016/j.jmb.2010.09.020. This article has 166 citations and is from a domain leading peer-reviewed journal.