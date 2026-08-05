---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:51:18.601449'
end_time: '2026-08-04T09:58:41.576604'
duration_seconds: 442.98
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: sphere shaped
  trait_identifier: METPO:1000683
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: sphere_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a spherical or nearly spherical
    morphology with roughly equal dimensions in all directions.
  parent_traits: METPO:1000666
  synonyms: S_sphere, sphere-shaped
  evidence_summary: 'DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan
    only at the division septum (Supports spherical bacterial morphology as associated
    with septal peptidoglycan synthesis.)'
  causal_graph_summary: 'sphere_shaped_septal_peptidoglycan: 11 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sphere shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000683
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_sphere, sphere-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports spherical bacterial morphology as associated with septal peptidoglycan synthesis.)
- **Existing causal graph summary:** sphere_shaped_septal_peptidoglycan: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **sphere shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sphere_shaped.yaml`.

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
- **Trait label:** sphere shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000683
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_sphere, sphere-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports spherical bacterial morphology as associated with septal peptidoglycan synthesis.)
- **Existing causal graph summary:** sphere_shaped_septal_peptidoglycan: 11 nodes, 11 edges

## Research Objective

Research the microbial trait **sphere shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sphere_shaped.yaml`.

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


# Curation report: sphere-shaped microbial morphology

## Target and scope

- **Trait:** sphere shaped
- **Identifier:** **METPO:1000683**
- **Category/kind:** MORPHOLOGY / CLASS
- **Parent:** METPO:1000666
- **Operational meaning:** a cell whose three principal dimensions are approximately equal. For curation, this should mean a stable single-cell geometry under specified growth conditions, not merely the taxonomic descriptor “coccus.”

The strongest general mechanism is spatially restricted cell-wall growth. Peptidoglycan (PG) forms a closed sacculus that preserves cell geometry; its enlargement is governed by localized synthesis and hydrolysis rather than by the sacculus encoding shape autonomously. Elongasomes mediate peripheral growth, whereas divisomes mediate septal growth. Suppressing lateral elongation while retaining division-centered PG synthesis is therefore a recurrent route toward coccal geometry. However, this is a mechanistic pattern, not a universal rule: spherical taxa can use distinct division systems, and ovococci retain appreciable peripheral synthesis. (caccamo2018themolecularbasis pages 1-2, egan2020regulationofpeptidoglycan pages 1-2, teeseling2017determinantsofbacterial pages 3-4)

### Boundary cases

1. **Ovoid/ovococcal cells are not spherical.** *Streptococcus pneumoniae* and *S. suis* undergo both peripheral and septal PG synthesis near midcell; their long and short axes remain distinguishable. Nanoscale imaging showed that pneumococcal septal and peripheral syntheses begin in one annular region, later separate into concentric regions, and that peripheral synthesis persists after septation. (jiang2023divivainteractswith pages 1-2, trouve2021nanoscaledynamicsof pages 1-3)
2. **“Coccoid” is broader than “sphere-shaped.”** It can include nearly spherical, ovoid, irregular, or conditionally rounded cells. A curation assertion should preferably include quantitative length, width, aspect ratio, circularity, or three-dimensional reconstruction.
3. **Wall-deficient forms are a separate mechanism.** L-forms and dormant wall-deficient cells round because membrane mechanics dominate after PG loss; they should not establish a constitutive sphere-shaped trait. (caccamo2018themolecularbasis pages 1-2, carvalho2024aquaticenvironmentdrives pages 1-2)
4. **Transient mutant rounding is evidence about a mechanism, not necessarily trait possession.** For example, reduced peripheral PG synthesis makes *S. suis* shorter and wider, but this demonstrates movement toward roundness rather than conversion to a validated sphere. (jiang2023divivainteractswith pages 7-9)
5. **Cell clusters must be separated from cell shape.** The grape-like appearance of *S. aureus* results from perpendicular division planes and delayed daughter separation; the individual cells, not the cluster, are spherical. (bartlett2023identificationoffacz pages 1-5)

## Current mechanistic model

The most defensible graph backbone is:

**lipid II production → PG polymerization/cross-linking → PG sacculus → maintenance of cell geometry**

with two spatial branches:

- **MreB/elongasome → peripheral PG synthesis → anisotropic elongation → opposes spherical geometry**;
- **FtsZ/divisome → septal PG synthesis → division-centered envelope growth → supports coccal geometry when lateral elongation is absent or small.**

This formulation is preferable to the absolute statement that all cocci synthesize PG only at the septum. Modern imaging shows that some cocci and especially ovococci have peripheral or periseptal synthesis. In spherical *S. aureus*, envelope biogenesis is principally focused at the division site, but “principally” should not be converted into “exclusively” without species- and assay-specific primary evidence. (bartlett2023identificationoffacz pages 1-5, gaifas2024combininglivecell pages 1-4, trouve2021nanoscaledynamicsof pages 1-3)

## Candidate nodes grouped by type

### Trait and taxon/context nodes

- **sphere shaped — METPO:1000683**
- sphere-shaped cell; coccal morphology; rod-to-coccus transition; increased roundness; cell aspect ratio
- *Staphylococcus aureus* — **NCBITaxon:1280**
- *Streptococcus pneumoniae* — **NCBITaxon:1313**; boundary case: ovococcus
- *Streptococcus suis* — **NCBITaxon:1307**; boundary case: ovococcus
- *Listeria monocytogenes* — **NCBITaxon:1639**; conditional CWD/VBNC boundary case
- *Escherichia coli* — **NCBITaxon:562**; surrogate/perturbation context
- *Chlamydia trachomatis* — **NCBITaxon:813**; noncanonical FtsZ-independent system
- *Deinococcus radiodurans* — **NCBITaxon:1299**; taxon-specific septation geometry

### Structures and cellular locations

- peptidoglycan sacculus
- cytoplasmic membrane
- cell wall; septum/cross-wall; division site; midcell; cell periphery/periseptum
- Z-ring; divisome; elongasome
- opposing septa in *D. radiodurans*

Suggested GO grounding, subject to ontology-version verification before YAML insertion:

- **GO:0007049** — cell cycle
- **GO:0051301** — cell division
- **GO:0000917** — barrier septum assembly
- **GO:0071555** — cell wall organization
- **GO:0009274** — peptidoglycan-based cell wall
- **GO:0030288** — outer membrane-bounded periplasmic space, where taxonomically applicable

### Processes and modules

- peptidoglycan biosynthesis and remodeling
- lipid II biosynthesis and membrane translocation
- glycan polymerization and peptide cross-linking
- peripheral/lateral PG synthesis
- septal PG synthesis
- septation, constriction, septum cleavage, daughter-cell separation
- division-site selection and successive perpendicular division-plane placement
- rod-to-coccus differentiation
- cell-wall shedding; viable-but-nonculturable transition

### Genes, proteins, and complexes

**Core divisome:** FtsZ, FtsA, EzrA, SepF, DivIC, DivIB, FtsL, FtsW, PBP2x/FtsI, MapZ/LocZ, GpsB, FacZ, ZapA, ZapJ.

**Elongation/peripheral synthesis:** MreB, MreC, MreD, RodZ, RodA, PBP2/PBP2b, DivIVA, MltG/MpgA.

**Precursor synthesis:** MurG, MraY and MurJ. MurG catalyzes formation of lipid II from lipid I and UDP-GlcNAc; the 2024 Gp11 study experimentally linked MurG inhibition to reduced lipid II and defective *S. aureus* division. (xu2024phageproteingp11 pages 5-8, xu2024phageproteingp11 pages 1-2, egan2020regulationofpeptidoglycan pages 1-2)

**Hydrolases/regulators:** NamA, LytA, Atl and other septal hydrolases; SigB as an environmental-stress regulator.

**Noncanonical/experimental factors:** chlamydial MreB–RodZ, chlamydial BacA, phage ΦNM1 Gp11, SulA-mediated FtsZ inhibition.

Do not assign species-specific UniProt CURIEs until the exact strain and accession have been checked. Gene symbols alone are safer than an unverified accession.

### Chemicals and environmental/experimental factors

- lipid II; lipid I; UDP-N-acetylglucosamine; N-acetylglucosamine; N-acetylmuramic acid
- fluorescent D-amino acids HADA and related probes
- β-lactams and other wall-active agents; PC190723 as an FtsZ perturbant in the FacZ screen
- mineral-water starvation, oligotrophy and hypoosmotic stress
- mutanolysin and other PG-cleaving enzymes
- IPTG/inducible overexpression and CRISPRi as experimental contexts

Conservative chemical grounding includes **CHEBI:506227** for lipid II only after checking that the intended stereochemical form matches the experiment; broad “lipid II” can vary by peptide composition. Avoid inventing identifiers for HADA or strain-specific PG chemotypes.

## Candidate causal edges

The following table separates core mechanisms from taxon-specific, perturbational, surrogate, and boundary-case evidence.

| subject | predicate | object | taxon/context | evidence strength | DOI/date | short exact supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| Peptidoglycan sacculus | maintains | cell shape | Broad bacteria | Strong review consensus | 10.1038/s41579-020-0366-3 (2020-05); 10.1016/j.tim.2017.09.012 (2018-03) | “The shape of a bacterial cell is maintained by the peptidoglycan layer, also called the ‘sacculus’” (egan2020regulationofpeptidoglycan pages 1-2) | Core generic morphology edge; good high-level parent mechanism for sphere-shaped trait. |
| MreB / elongasome | directs | lateral/peripheral peptidoglycan synthesis and elongation | Rod-shaped bacteria | Strong review consensus | 10.1128/spectrum.04750-22 (2023-05); 10.1128/jb.00092-23 (2023-05) | “The elongasome organized by MreB… is responsible for the PG synthesis along the lateral part of the cell, facilitating the elongation of bacterial cells” (jiang2023divivainteractswith pages 1-2) | Supports contrast with sphere-shaped taxa that lack or minimize lateral elongation programs. |
| Stepwise loss of yacF, mreBCD, pbpC, rodA, rodZ | drives | rod-to-coccus transition | Neisseriaceae evolutionary transition | Moderate, taxon-specific review synthesis | 10.1016/j.tim.2017.09.012 (2018-03) | “The transition from rods to cocci in Neisseriaceae correlates with enriched septal and polar peptidoglycan… This transition can be experimentally recapitulated through stepwise deletion of yacF and elongation machinery genes (mreBCD, pbpC, rodA, rodZ)” (caccamo2018themolecularbasis pages 7-9) | Useful mechanistic analogy for sphere acquisition; curate as taxon-specific/inferred unless primary source is added. |
| FtsZ ring | recruits/organizes | divisome and septal PG synthesis | Broad bacteria; especially cocci/ovococci | Strong | 10.3389/fmicb.2021.780864 (2021-12); 10.1101/2024.11.18.624142 (2024-11 preprint) | “The dynamic Z-ring recruits a large number of proteins into the divisome needed for septal peptidoglycan (PG) synthesis” (perez2021ftszringregulationand pages 1-2) | Strong core edge for septum-centered growth underlying spherical morphogenesis. |
| Sphere-shaped S. aureus envelope biogenesis | is focused at | division site throughout cell cycle | Staphylococcus aureus | Moderate, preprint but direct statement | 10.1101/2023.04.24.538170 (2023-04 preprint) | “Spherical S. aureus cells do not have as distinct an elongation phase… Instead, envelope biogenesis is principally focused at the division site throughout the cell cycle” (bartlett2023identificationoffacz pages 1-5) | Strongly relevant to scope; preprint status should be flagged. |
| FacZ | antagonizes | GpsB | Staphylococcus aureus | Moderate, preprint | 10.1101/2023.04.24.538170 (2023-04 preprint) | “FacZ and GpsB were found to interact directly in a purified system. Thus, FacZ is a novel antagonist of GpsB function” (bartlett2023identificationoffacz pages 1-5) | Division-plane control factor; relevant to maintaining proper spherical division pattern, but not yet peer-reviewed. |
| FacZ | controls | division site placement | Staphylococcus aureus and other Firmicutes | Moderate, preprint | 10.1101/2023.04.24.538170 (2023-04 preprint) | “displayed aberrant membrane invaginations and multiple FtsZ cytokinetic ring structures” and “controlling division site placement in S. aureus and other Firmicutes” (bartlett2023identificationoffacz pages 1-5) | Candidate regulatory edge for graph; use uncertainty tag for preprint and placement-specific phenotype. |
| Gp11 | binds/inhibits | MurG | Staphylococcus aureus phage-host interaction | Strong for interaction/perturbation, but non-native phage factor | 10.1128/mbio.00679-24 (2024-05-16) | “Gp11 interacts with MurG… by inhibiting the production of lipid II to regulate peptidoglycan (PG) biosynthesis” (xu2024phageproteingp11 pages 1-2) | Valuable perturbation evidence linking MurG/lipid II to spherical-cell division; not a constitutive endogenous trait mechanism. |
| Gp11 | lowers | lipid II production | Staphylococcus aureus phage-host interaction | Strong perturbation evidence | 10.1128/mbio.00679-24 (2024-05-16) | “a reduction in lipid II was observed in the presence of Gp11” (xu2024phageproteingp11 pages 5-8) | Connects MurG activity to septal PG defects; keep as perturbational edge. |
| Gp11 | binds DivIC and disrupts recruitment of | FtsW | Staphylococcus aureus phage-host interaction | Strong perturbation evidence | 10.1128/mbio.00679-24 (2024-05-16) | “Gp11 also interacts with cell division protein DivIC… to disrupt the recruitment of division protein FtsW” (xu2024phageproteingp11 pages 1-2) | Relevant for divisome assembly branch; exogenous phage protein means caution for TraitMech core graph. |
| DivIVA phosphorylation state | affects | MltG localization | Streptococcus suis (ovococcus, not sphere) | Strong, species-specific | 10.1128/spectrum.04750-22 (2023-05-22) | “DivIVA phosphorylation affects MltG localization and inhibits peripheral PG synthesis” (jiang2023divivainteractswith pages 7-9) | Excellent edge for boundary with ovoid shape; not direct evidence for constitutive sphere trait. |
| Abnormal DivIVA/MltG function | impairs | peripheral PG synthesis | Streptococcus suis | Strong, species-specific | 10.1128/spectrum.04750-22 (2023-05-22) | “DmltG and DivIVA3E cells undertook impaired peripheral PG synthesis” (jiang2023divivainteractswith pages 7-9) | Supports principle that reduced peripheral PG makes cells rounder. |
| DivIVA3E or ΔmltG | produces | significantly rounder cells | Streptococcus suis | Strong, species-specific | 10.1128/spectrum.04750-22 (2023-05-22) | “both DmltG and DivIVA3E cells were significantly shorter and wider” (jiang2023divivainteractswith pages 7-9) | Boundary-case evidence: rounder ovococci ≠ true sphere trait, but mechanistically informative. |
| Chlamydial RodZ | directs | chlamydial MreB to division septum | Chlamydia system tested in E. coli surrogate | Moderate, surrogate experimental system | 10.1128/mBio.03222-19 (2020-02-18) | “chlamydial RodZ directs chlamydial MreB to the E. coli division septum” (ranjit2020chlamydialmrebdirects pages 1-2) | Relevant for septum-centered growth without FtsZ; surrogate assay, not direct native sphere-trait proof. |
| Chlamydial mreB-rodZ | supports | spherical cell growth/division without FtsZ | E. coli surrogate complemented with chlamydial genes | Moderate, surrogate | 10.1128/mBio.03222-19 (2020-02-18) | “When FtsZ activity was inhibited… spherical E. coli grew and divided” (ranjit2020chlamydialmrebdirects pages 1-2) | Mechanistically interesting alternative route; curate only with strong uncertainty tags. |
| Mineral-water starvation | causes | rod-to-coccus / CWD VBNC transition | Listeria monocytogenes in aquatic starvation | Strong for boundary-case physiology | 10.1038/s41467-024-52633-7 (2024-10) | “bacteria starved in mineral water become VBNC by converting into osmotically stable cell wall-deficient coccoid forms” (carvalho2024aquaticenvironmentdrives pages 1-2) | Important exclusion: dormant wall-deficient coccoid state is not constitutive sphere-shaped trait. |
| SigB and NamA | modulate | CWD coccoid VBNC formation | Listeria monocytogenes in mineral water | Strong, condition-specific | 10.1038/s41467-024-52633-7 (2024-10) | “SigB and the autolysin NamA as major actors of VBNC state transition” (carvalho2024aquaticenvironmentdrives pages 1-2) | Good environmental/response branch; should be marked boundary-case, not core morphology graph unless context-specific. |
| Deinococcus opposing septa | progress by | “sliding doors” septation mechanism | Deinococcus radiodurans spherical bacterium | Moderate, 2024 preprint | 10.1101/2024.11.18.624142 (2024-11 preprint) | “two septa originating from opposite sides of the cell progress with a flat leading edge until meeting and fusing at mid-cell” (gaifas2024combininglivecell pages 1-4) | Useful species-specific septation geometry for spherical cells; preprint and taxon-specific. |


*Table: Compact curation table of evidence-backed mechanistic edges relevant to the sphere-shaped microbial trait. It highlights core cell-wall and division mechanisms, while explicitly flagging taxon-specific, perturbational, surrogate, and boundary-case evidence.*

## Recommended graph organization

### Core branch suitable for curation

1. **lipid II —is precursor for→ peptidoglycan**
2. **peptidoglycan biosynthesis/remodeling —builds→ peptidoglycan sacculus**
3. **peptidoglycan sacculus —maintains→ cell shape**
4. **FtsZ Z-ring —recruits/organizes→ divisome**
5. **divisome —directs→ septal peptidoglycan synthesis**
6. **septal peptidoglycan synthesis —builds→ division septum**
7. **division-centered envelope biogenesis —supports→ sphere shaped**
8. **MreB-organized elongasome —directs→ peripheral peptidoglycan synthesis**
9. **peripheral peptidoglycan synthesis —promotes→ anisotropic cell elongation**
10. **reduced/absent elongasome activity —reduces→ anisotropic elongation**
11. **reduced anisotropic elongation with retained septation —promotes→ rod-to-coccus transition**

Edges 7, 10 and 11 should carry mechanistic or taxon-context qualifiers rather than being asserted universally. Evolutionary work summarized for Neisseriaceae links stepwise loss of *yacF*, *mreBCD*, *pbpC*, *rodA* and *rodZ* to rod-to-coccus change and corresponding shifts from lateral toward septal/polar PG signatures. (caccamo2018themolecularbasis pages 7-9, caccamo2018themolecularbasis pages 6-7)

### *S. aureus* regulatory branch

- **FacZ —antagonizes→ GpsB**
- **FacZ/GpsB balance —controls→ FtsZ-ring number and division-site placement**
- **correct division-site placement —supports→ single septum in a selected midcell plane**
- **successive perpendicular division planes —produces→ characteristic staphylococcal cluster organization**

The direct FacZ–GpsB interaction and suppression genetics are promising, but the retrieved source is a 24 April 2023 bioRxiv preprint and should remain provisional pending verification of a peer-reviewed version. (bartlett2023identificationoffacz pages 1-5)

### PG-precursor/divisome perturbation branch

The peer-reviewed 2024 ΦNM1 study screened **345 essential *S. aureus* genes** and found that the 53-aa membrane protein Gp11 interacts with MurG and DivIC. Gp11 mislocalized MurG, reduced lipid II, depleted nascent PG at the septum relative to the periphery, and disrupted DivIC-dependent recruitment of FtsW. HADA septum/periphery measurements used at least 30 cells, while deletion of phage *gp11* increased lipid II two hours after infection. These data establish causal dependencies in the host PG/division machinery, but Gp11 is an exogenous phage inhibitor rather than a normal determinant of spherical morphology. (xu2024phageproteingp11 pages 5-8, xu2024phageproteingp11 pages 1-2)

### Ovococcal boundary branch

In *S. suis*, DivIVA phosphorylation altered its interaction with MltG and MltG localization. Δ*mltG* and phosphomimetic DivIVA3E cells were significantly shorter and wider, with impaired peripheral PG synthesis; morphometry included **at least 100 cells from two independent experiments** and reported **P < 0.001**. Catalytic-site or domain-disrupting MltG variants were also significantly rounder. This is strong evidence that reduced peripheral growth increases roundness, but it is evidence from an ovococcus and should not by itself support the terminal trait METPO:1000683. (jiang2023divivainteractswith pages 1-2, jiang2023divivainteractswith pages 7-9)

### FtsZ-independent alternative

Pathogenic *Chlamydia* lacks FtsZ and instead directs septal PG synthesis through MreB. In an *E. coli* surrogate, chlamydial RodZ directed chlamydial MreB to the septum, and chlamydial *mreB–rodZ* supported growth and division of spherical Δ*mreB* cells even when FtsZ was inhibited by SulA. This is an important exception to an FtsZ-required graph, but the spherical-division result is a heterologous surrogate assay and should be marked uncertain for native chlamydial morphology. (lee2023theuniquenterminal pages 1-2, ranjit2020chlamydialmrebdirects pages 1-2)

### Environmental wall-loss boundary branch

In 2024, mineral-water starvation was shown to drive *L. monocytogenes* from rods to osmotically stable, wall-deficient coccoid VBNC forms. Coccoid forms appeared from day 7 and increased through day 28. After seven days, Δ*sigB* cultures showed a two-log CFU decline and more than 90% of viable cells were nonculturable and had converted to CWD coccoid forms. Conversely, after 14 days, more than 90% of Δ*namA* cells retained their wall versus 44% of wild type, implicating NamA-mediated wall shedding and SigB-dependent modulation. These nodes are valuable for an environmental-state graph but should not enter the constitutive sphere-shaped core. (carvalho2024aquaticenvironmentdrives pages 6-8, carvalho2024aquaticenvironmentdrives pages 1-2)

## Recent developments and practical relevance

- **2023 — DivIVA–MltG regulation:** Established a phosphorylation-sensitive link between a morphogenetic scaffold, hydrolase localization, peripheral PG synthesis and increased roundness in *S. suis*. This supplies a causal bridge from molecular regulation to measured aspect ratio. (jiang2023divivainteractswith pages 1-2, jiang2023divivainteractswith pages 7-9)
- **2023 — BacA and noncanonical chlamydial morphogenesis:** BacA N-terminal residues 51–81 were sufficient to confer membrane association, while N-terminal truncations disrupted rings and altered cell size. This is more directly a size/polarity mechanism than evidence for sphere shape and should remain peripheral to the graph. (lee2023theuniquenterminal pages 1-2)
- **2023 — FacZ discovery:** Suggested a new Firmicute division-site regulator that directly interacts with and antagonizes GpsB; potentially relevant to antimicrobial targeting of staphylococcal envelope biogenesis, but currently preprint evidence in the retrieved corpus. (bartlett2023identificationoffacz pages 1-5)
- **2024 — phage-derived division inhibitor:** Gp11 identifies MurG–lipid II production and DivIC–FtsW recruitment as experimentally vulnerable points in *S. aureus*. The authors explicitly frame phage proteins as templates for antibacterial compounds or peptides, providing a real-world drug-discovery application rather than a deployed therapy. (xu2024phageproteingp11 pages 5-8, xu2024phageproteingp11 pages 1-2)
- **2024 — environmental persistence:** Wall-deficient coccoid VBNC *Listeria* escaped growth-based detection and reverted to a walled, virulent state after passage through chicken embryos. This has implications for food/water surveillance because morphology and viability assays may reveal cells missed by routine culture. (carvalho2024aquaticenvironmentdrives pages 1-2)
- **2024 — *D. radiodurans* septation:** Correlative fluorescence microscopy and cryo-electron tomography support a taxon-specific “sliding doors” mechanism in which two opposing septa meet and fuse. This is mechanistically informative but remains a November 2024 preprint. (gaifas2024combininglivecell pages 1-4)

## Expert interpretation

Authoritative reviews converge on PG as the material determinant that retains shape, while emphasizing that the topology and dynamics of synthetic/hydrolytic complexes generate that shape. Uniform surface expansion tends toward a sphere; non-spherical forms require spatially unequal insertion or remodeling. Consequently, the best TraitMech representation is not “sphere gene → sphere,” but a balance model linking precursor supply, septal synthesis, peripheral synthesis, hydrolase activity and division-plane control. (egan2020regulationofpeptidoglycan pages 1-2, teeseling2017determinantsofbacterial pages 3-4)

The existing statement that spherical cocci synthesize PG only at the division septum is useful as a historical abstraction but too broad for unqualified curation. *S. aureus* is strongly division-centered, whereas modern studies distinguish septal, peripheral and periseptal synthesis even when the relevant machines occupy nearby midcell zones. The graph should therefore use **division-site-focused PG synthesis** as the broadly defensible node and reserve **septum-only PG synthesis** for a named taxon, growth condition and assay. (bartlett2023identificationoffacz pages 1-5, gaifas2024combininglivecell pages 1-4, trouve2021nanoscaledynamicsof pages 1-3)

## Claims not yet ready for TraitMech curation

1. **“All spherical bacteria lack MreB.”** False as a universal claim; *Chlamydia* uses MreB for division, and evolutionary routes vary.
2. **“All cocci synthesize PG exclusively at the septum.”** Overgeneralized; retain only with taxon- and assay-specific evidence.
3. **FacZ as an established universal sphere determinant.** It controls division placement in Firmicutes, but the retrieved study is a preprint and does not show that FacZ creates spherical shape across taxa.
4. **Gp11 as an endogenous cause of the trait.** It is a phage perturbant useful for exposing host dependencies.
5. **DivIVA3E or Δ*mltG* → METPO:1000683.** The data show significantly rounder *S. suis*, not validated isotropic spheres.
6. **Mineral-water starvation → constitutive sphere trait.** This produces dormant, wall-deficient coccoid forms and belongs in a conditional phenotype graph.
7. **Chlamydial MreB–RodZ universally replaces FtsZ.** The spherical division result was obtained in engineered *E. coli*; native and broader taxonomic generalization remains uncertain.
8. **The *D. radiodurans* sliding-doors model as a general coccal mechanism.** It is species-specific and currently supported here by a preprint.
9. **Unverified protein CURIEs.** Do not infer UniProt accessions across strains or treat gene symbols as globally unique.
10. **“Coccus” based solely on two-dimensional microscopy.** Cell orientation and clustering can obscure anisotropy; prefer multi-axis morphometry or 3D imaging.

## DOI-first bibliography

1. Xu Q. et al. **Phage protein Gp11 blocks *Staphylococcus aureus* cell division by inhibiting peptidoglycan biosynthesis.** *mBio* 15(6). Published **16 May 2024**. DOI: [10.1128/mbio.00679-24](https://doi.org/10.1128/mbio.00679-24). (xu2024phageproteingp11 pages 1-2)
2. Carvalho F. et al. **Aquatic environment drives the emergence of cell wall-deficient dormant forms in *Listeria*.** *Nature Communications* 15:8499. Accepted **16 September 2024**; published 2024. DOI: [10.1038/s41467-024-52633-7](https://doi.org/10.1038/s41467-024-52633-7). (carvalho2024aquaticenvironmentdrives pages 6-8, carvalho2024aquaticenvironmentdrives pages 1-2)
3. Jiang Q. et al. **DivIVA interacts with the cell wall hydrolase MltG to regulate *Streptococcus suis* peptidoglycan synthesis.** *Microbiology Spectrum* 11(3). Published **22 May 2023**. DOI: [10.1128/spectrum.04750-22](https://doi.org/10.1128/spectrum.04750-22). (jiang2023divivainteractswith pages 1-2)
4. Lee J., Cox J.V., Ouellette S.P. **The unique N-terminal domain of chlamydial bactofilin mediates its membrane localization and ring-forming properties.** *Journal of Bacteriology* 205(6). Published **16 May 2023**. DOI: [10.1128/jb.00092-23](https://doi.org/10.1128/jb.00092-23). (lee2023theuniquenterminal pages 1-2)
5. Bartlett T.M. et al. **Identification of FacZ as a division site placement factor in *Staphylococcus aureus*.** bioRxiv, posted **24 April 2023**; preprint. DOI: [10.1101/2023.04.24.538170](https://doi.org/10.1101/2023.04.24.538170). (bartlett2023identificationoffacz pages 1-5)
6. Gaifas L. et al. **Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in *Deinococcus radiodurans*.** bioRxiv, **November 2024**; preprint. DOI: [10.1101/2024.11.18.624142](https://doi.org/10.1101/2024.11.18.624142). (gaifas2024combininglivecell pages 1-4)
7. Trouve J. et al. **Nanoscale dynamics of peptidoglycan assembly during the cell cycle of *Streptococcus pneumoniae*.** *Current Biology* 31:2844–2856.e6. Published **12 July 2021**. DOI: [10.1016/j.cub.2021.04.041](https://doi.org/10.1016/j.cub.2021.04.041). (trouve2021nanoscaledynamicsof pages 1-3)
8. Perez A.J. et al. **FtsZ-ring regulation and cell division are mediated by essential EzrA and accessory proteins ZapA and ZapJ in *Streptococcus pneumoniae*.** *Frontiers in Microbiology* 12:780864. Published **2 December 2021**. DOI: [10.3389/fmicb.2021.780864](https://doi.org/10.3389/fmicb.2021.780864). (perez2021ftszringregulationand pages 1-2)
9. Egan A.J.F., Errington J., Vollmer W. **Regulation of peptidoglycan synthesis and remodelling.** *Nature Reviews Microbiology* 18:446–460. Published **May 2020**. DOI: [10.1038/s41579-020-0366-3](https://doi.org/10.1038/s41579-020-0366-3). (egan2020regulationofpeptidoglycan pages 1-2)
10. Ranjit D.K., Liechti G.W., Maurelli A.T. **Chlamydial MreB directs cell division and peptidoglycan synthesis in *Escherichia coli* in the absence of FtsZ activity.** *mBio* 11:e03222-19. Published **18 February 2020**. DOI: [10.1128/mBio.03222-19](https://doi.org/10.1128/mBio.03222-19). (ranjit2020chlamydialmrebdirects pages 1-2)
11. Caccamo P.D., Brun Y.V. **The molecular basis of noncanonical bacterial morphology.** *Trends in Microbiology* 26:191–208. Published **March 2018**. DOI: [10.1016/j.tim.2017.09.012](https://doi.org/10.1016/j.tim.2017.09.012). (caccamo2018themolecularbasis pages 7-9, caccamo2018themolecularbasis pages 1-2)
12. van Teeseling M.C.F., de Pedro M.A., Cava F. **Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting.** *Frontiers in Microbiology* 8:1264. Published **July 2017**. DOI: [10.3389/fmicb.2017.01264](https://doi.org/10.3389/fmicb.2017.01264). (teeseling2017determinantsofbacterial pages 3-4, teeseling2017determinantsofbacterial pages 6-7)

**Curation priority:** retain the existing septal-PG graph but revise its root assertion to a qualified, taxon-aware model: **reduced lateral elongation plus division-site-focused PG synthesis promotes or maintains spherical morphology**. Add separate optional branches for division-plane regulation in *S. aureus*, noncanonical MreB–RodZ division, and environmentally induced wall-deficient rounding rather than merging all three into one universal pathway.

References

1. (caccamo2018themolecularbasis pages 1-2): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.

2. (egan2020regulationofpeptidoglycan pages 1-2): Alexander J. F. Egan, Jeff Errington, and Waldemar Vollmer. Regulation of peptidoglycan synthesis and remodelling. Nature Reviews Microbiology, 18:446-460, May 2020. URL: https://doi.org/10.1038/s41579-020-0366-3, doi:10.1038/s41579-020-0366-3. This article has 693 citations and is from a highest quality peer-reviewed journal.

3. (teeseling2017determinantsofbacterial pages 3-4): Muriel C. F. van Teeseling, Miguel A. de Pedro, and Felipe Cava. Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01264, doi:10.3389/fmicb.2017.01264. This article has 225 citations and is from a peer-reviewed journal.

4. (jiang2023divivainteractswith pages 1-2): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 14 citations and is from a domain leading peer-reviewed journal.

5. (trouve2021nanoscaledynamicsof pages 1-3): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

6. (carvalho2024aquaticenvironmentdrives pages 1-2): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 28 citations and is from a highest quality peer-reviewed journal.

7. (jiang2023divivainteractswith pages 7-9): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 14 citations and is from a domain leading peer-reviewed journal.

8. (bartlett2023identificationoffacz pages 1-5): Thomas M. Bartlett, Tyler A. Sisley, Aaron Mychack, Suzanne Walker, Richard W. Baker, David Z. Rudner, and Thomas G. Bernhardt. Identification of facz as a division site placement factor in staphylococcus aureus. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2023.04.24.538170, doi:10.1101/2023.04.24.538170. This article has 6 citations.

9. (gaifas2024combininglivecell pages 1-4): L. Gaifas, J.P. Kleman, F. Lacroix, E. Schexnaydre, J. Trouve, C. Morlot, L. Sandblad, I. Gutsche, and J. Timmins. Combining live cell fluorescence imaging with in situ cryo electron tomography sheds light on the septation process in deinococcus radiodurans. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.18.624142, doi:10.1101/2024.11.18.624142. This article has 0 citations.

10. (xu2024phageproteingp11 pages 5-8): Qi Xu, Li Tang, Weilin Liu, Neng Xu, Yangbo Hu, Yong Zhang, and Shiyun Chen. Phage protein gp11 blocks <i>staphylococcus aureus</i> cell division by inhibiting peptidoglycan biosynthesis. Jun 2024. URL: https://doi.org/10.1128/mbio.00679-24, doi:10.1128/mbio.00679-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

11. (xu2024phageproteingp11 pages 1-2): Qi Xu, Li Tang, Weilin Liu, Neng Xu, Yangbo Hu, Yong Zhang, and Shiyun Chen. Phage protein gp11 blocks <i>staphylococcus aureus</i> cell division by inhibiting peptidoglycan biosynthesis. Jun 2024. URL: https://doi.org/10.1128/mbio.00679-24, doi:10.1128/mbio.00679-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

12. (caccamo2018themolecularbasis pages 7-9): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.

13. (perez2021ftszringregulationand pages 1-2): Amilcar J. Perez, Jesus Bazan Villicana, Ho-Ching T. Tsui, Madeline L. Danforth, Mattia Benedet, Orietta Massidda, and Malcolm E. Winkler. Ftsz-ring regulation and cell division are mediated by essential ezra and accessory proteins zapa and zapj in streptococcus pneumoniae. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.780864, doi:10.3389/fmicb.2021.780864. This article has 34 citations and is from a peer-reviewed journal.

14. (ranjit2020chlamydialmrebdirects pages 1-2): Dev K. Ranjit, George W. Liechti, and Anthony T. Maurelli. Chlamydial mreb directs cell division and peptidoglycan synthesis in escherichia coli in the absence of ftsz activity. mBio, Feb 2020. URL: https://doi.org/10.1128/mbio.03222-19, doi:10.1128/mbio.03222-19. This article has 22 citations and is from a domain leading peer-reviewed journal.

15. (caccamo2018themolecularbasis pages 6-7): Paul D. Caccamo and Yves V. Brun. The molecular basis of noncanonical bacterial morphology. Mar 2018. URL: https://doi.org/10.1016/j.tim.2017.09.012, doi:10.1016/j.tim.2017.09.012. This article has 80 citations and is from a domain leading peer-reviewed journal.

16. (lee2023theuniquenterminal pages 1-2): Junghoon Lee, John V. Cox, and Scot P. Ouellette. The unique n-terminal domain of chlamydial bactofilin mediates its membrane localization and ring-forming properties. Journal of Bacteriology, Jun 2023. URL: https://doi.org/10.1128/jb.00092-23, doi:10.1128/jb.00092-23. This article has 4 citations and is from a peer-reviewed journal.

17. (carvalho2024aquaticenvironmentdrives pages 6-8): Filipe Carvalho, Alexis Carreaux, Anna Sartori-Rupp, Stéphane Tachon, Anastasia D. Gazi, Pascal Courtin, Pierre Nicolas, Florence Dubois-Brissonnet, Aurélien Barbotin, Emma Desgranges, Matthieu Bertrand, Karine Gloux, Catherine Schouler, Rut Carballido-López, Marie-Pierre Chapot-Chartier, Eliane Milohanic, Hélène Bierne, and Alessandro Pagliuso. Aquatic environment drives the emergence of cell wall-deficient dormant forms in listeria. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52633-7, doi:10.1038/s41467-024-52633-7. This article has 28 citations and is from a highest quality peer-reviewed journal.

18. (teeseling2017determinantsofbacterial pages 6-7): Muriel C. F. van Teeseling, Miguel A. de Pedro, and Felipe Cava. Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01264, doi:10.3389/fmicb.2017.01264. This article has 225 citations and is from a peer-reviewed journal.