---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:59:01.197552'
end_time: '2026-08-04T08:09:14.485697'
duration_seconds: 613.29
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: coccus shaped
  trait_identifier: METPO:1000668
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: coccus_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a spherical or nearly spherical
    morphology, with roughly equal dimensions in all directions.
  parent_traits: METPO:1000666
  synonyms: coccus, coccus-shaped
  evidence_summary: 'DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan
    only at the division septum (Supports coccus shape as a spherical morphology with
    septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus
    aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus
    aureus is described as coccus-shaped.)'
  causal_graph_summary: 'coccus_shaped_septal_growth: 9 nodes, 9 edges'
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
- **Trait label:** coccus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000668
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology, with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccus, coccus-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports coccus shape as a spherical morphology with septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus aureus is described as coccus-shaped.)
- **Existing causal graph summary:** coccus_shaped_septal_growth: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **coccus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccus_shaped.yaml`.

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
- **Trait label:** coccus shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000668
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a spherical or nearly spherical morphology, with roughly equal dimensions in all directions.
- **Parent traits:** METPO:1000666
- **Synonyms:** coccus, coccus-shaped
- **Existing evidence:** DOI:10.1038/nrmicro3088: spherical cocci synthesize peptidoglycan only at the division septum (Supports coccus shape as a spherical morphology with septal wall growth rather than lateral elongation.) | PMID:19747126: Staphylococcus aureus is a facultative, Gram-positive coccus (Organism example: Staphylococcus aureus is described as coccus-shaped.)
- **Existing causal graph summary:** coccus_shaped_septal_growth: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **coccus shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/coccus_shaped.yaml`.

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


# TraitMech curation report: coccus-shaped morphology

## 1. Scope summary

**Target trait:** **coccus shaped**  
**Identifier:** **METPO:1000668**  
**Category:** morphology; class; reviewed  
**Definition used:** a spherical or nearly spherical microbial cell whose dimensions are approximately equal in all directions.

This is an **assay-observed single-cell morphology**, not a metabolic capacity or environmental preference. For curation, the terminal phenotype should be a roughly spherical cell measured by microscopy or equivalent morphological observation. In the best-characterized “true coccus,” *Staphylococcus aureus*, growth is dominated by division-associated peptidoglycan (PG) synthesis at midcell. FtsZ organizes the divisome, but PG polymerization and cross-linking supply the indispensable progression of septum closure. Recent work also shows that *S. aureus* is not a geometrically invariant sphere: it undergoes limited pre-division elongation mediated by RodA–PBP3 and regulated by GpsB. Thus, **coccus-shaped means nearly spherical at the organism/phenotype level, not complete absence of all elongation**. (battaje2023modelsversuspathogens pages 1-3, costa2024theroleof pages 13-14, puls2023inhibitionofpeptidoglycan pages 4-5)

### Boundary cases

1. **Ovococci are not strict synonyms.** *Streptococcus pneumoniae* and *S. suis* combine septal and peripheral PG synthesis and commonly have an ovoid/ellipsoid shape. Their elongasome-like machinery is concentrated near midcell rather than distributed along a long lateral cylinder. They may satisfy a broad “nearly spherical” assay threshold, but their mechanism should be represented in a separate ovococcal graph or explicitly qualified. (battaje2023modelsversuspathogens pages 4-5, battaje2023modelsversuspathogens pages 1-3)
2. **“Rounder” mutants are not automatically cocci.** A statistically lower aspect ratio establishes movement toward sphericity, not necessarily attainment of METPO:1000668.
3. **Cell arrangement is separate from shape.** Diplococci, tetrads, chains, and grape-like clusters describe post-division arrangement, not the shape of each cell.
4. **Transient coccoid states require qualification.** Stationary-phase rounding, stress-induced coccoid conversion, spores, dormant bodies, and pleomorphic forms should not be treated as constitutive coccus shape without condition and life-stage nodes.
5. **Wall-less spheres are mechanistically distinct.** Protoplasts, spheroplasts, and L-forms can become spherical through loss of the load-bearing PG sacculus; they should not be merged with the septal-growth mechanism of walled cocci.
6. **Taxonomic descriptors are observations, not mechanisms.** A statement that *S. aureus* is a Gram-positive coccus supports the phenotype–taxon association but does not by itself support any molecular edge.

## 2. Current mechanistic model

The strongest curation model is:

**midcell selection → FtsZ/Z-ring and divisome assembly → recruitment/organization of septal PG machinery → PBP/SEDS-dependent PG synthesis and cross-linking → centripetal septum constriction → hydrolase-mediated septum splitting → nearly spherical daughter cells.**

True cocci lack the canonical MreB-directed, sidewall-distributed elongation program characteristic of many rods. Nevertheless, the older formulation that cocci synthesize PG **only** at the septum is now too absolute for *S. aureus*: RodA–PBP3 supports limited elongation at the outer septal edge, while GpsB controls the septal-versus-peripheral distribution of PBP2 and PBP4. Loss of GpsB shifts PBP activity toward the periphery, increases peripheral cross-linking/stiffness, impairs mild elongation, and produces smaller, rounder cells. (costa2024theroleof pages 13-14, battaje2023modelsversuspathogens pages 3-4)

A key 2023 result refined the mechanical model of cytokinesis. Vancomycin and telavancin halted constriction while the Z-ring remained present; only 3 of 735 treated cells divided, versus 98% of controls. Active septum progression fell below 3% within 10 minutes, and all tested PG inhibitors increased mean Z-ring diameter by 30–44%. Therefore, FtsZ treadmilling organizes early division but is insufficient to close the septum when PG synthesis is blocked. (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 3-4, puls2023inhibitionofpeptidoglycan pages 2-3)

## 3. Candidate graph nodes

Identifiers below are suggested only where grounding is sufficiently clear. Taxon-specific proteins should be represented with the organism/gene context; label-only nodes are preferable to an unverified UniProt accession.

### Trait and taxa

- **coccus shaped** — **METPO:1000668**
- **parent morphology trait** — **METPO:1000666**
- *Staphylococcus aureus* — **NCBITaxon:1280**; principal true-coccus model
- *Streptococcus pneumoniae* — **NCBITaxon:1313**; ovococcal boundary model
- *Streptococcus suis* — **NCBITaxon:1307**; ovococcal boundary model

### Complexes, structures, and localizations

- FtsZ cytokinetic ring / Z-ring — label-only complex node; taxon-specific FtsZ gene product
- divisome — label-only complex node
- elongasome — label-only complex node; generally absent as a canonical MreB-guided sidewall machine in true cocci
- division septum / midcell — label-only localization
- cell periphery / peripheral wall — label-only localization
- peptidoglycan sacculus — **CHEBI:8005**
- cytoplasmic membrane — **GO:0005886**

### Genes and proteins

- **ftsZ / FtsZ** — tubulin-like GTPase and divisome organizer
- **ftsW / FtsW** — septal SEDS-family PG glycosyltransferase component
- **pbp2 / PBP2** — major bifunctional PG synthase in *S. aureus*; crucial for septum closure
- **pbp1 / PBP1** and **FtsW–PBP1 pair** — candidate septal PG module in *S. aureus*
- **rodA / RodA** and **pbp3 / PBP3** — limited elongation-associated SEDS–PBP pair in *S. aureus*
- **pbp4 / PBP4** — PG cross-linking enzyme whose localization is regulated by GpsB
- **gpsB / GpsB** — morphogenetic regulator of PBP2/PBP4 distribution
- **smdA / SmdA** — septum-enriched staphylococcal morphology determinant
- **ezrA / EzrA** — FtsZ-associated division regulator and reported SmdA interactor
- **atl / Atl** — major staphylococcal autolysin; candidate daughter-cell separation effector
- **mreB / MreB** — canonical rod-shape cytoskeleton component; absence is an association rather than a sufficient cause
- Ovococcal boundary nodes: **DivIVA, MltG, RodA–PBP2b, FtsW–PBP2x, CozE, MreC, MreD, RodZ**. (battaje2023modelsversuspathogens pages 4-5, myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 12-14)

### Processes and molecular functions

- peptidoglycan biosynthetic process — **GO:0009252**
- cell wall organization or biogenesis — **GO:0071554**
- cell division — **GO:0051301**
- cell morphogenesis — **GO:0000902**
- GTPase activity — **GO:0003924**, applicable to FtsZ
- PG glycosyltransferase activity — use an appropriate verified child term during implementation
- transpeptidase/cross-linking activity — use protein-specific verified GO/EC grounding
- PG hydrolysis, septum cleavage, daughter-cell separation — retain as label-only processes unless the exact hydrolase reaction is specified
- FtsZ treadmilling; septal PG synthesis; peripheral PG synthesis; septum constriction; cell splitting — label-only process nodes

### Experimental and chemical nodes

- vancomycin — **CHEBI:28001**
- oxacillin — **CHEBI:7809**
- telavancin — label-only unless its CHEBI record is verified during YAML preparation
- β-lactam antibiotic — class node; use a verified CHEBI class identifier during implementation
- CRISPR interference/CRISPRi knockdown — experimental perturbation
- gene deletion/transposon mutation — experimental perturbation
- fluorescent D-amino-acid labeling/HADA — assay node
- time-lapse and super-resolution fluorescence microscopy — assay nodes

## 4. Candidate causal edges

The compact high-confidence set is summarized below.

| subject | predicate | object | taxon/scope | evidence strength | DOI |
|---|---|---|---|---|---|
| FtsZ/divisome | spatially organizes | septal peptidoglycan synthesis/localization | true cocci, especially *Staphylococcus aureus*; broader coccoid review scope | strong review-supported, not exclusive mechanism statement (battaje2023modelsversuspathogens pages 1-3, battaje2023modelsversuspathogens pages 3-4) | https://doi.org/10.1042/bsr20221664 |
| Peptidoglycan synthesis | drives | septum constriction/cytokinesis | *Staphylococcus aureus* | strong primary experimental (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 1-2) | https://doi.org/10.1126/sciadv.ade9023 |
| PBP2 | is required for | septum closure | *Staphylococcus aureus* | strong primary experimental (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 1-2) | https://doi.org/10.1126/sciadv.ade9023 |
| Vancomycin or telavancin inhibition of peptidoglycan synthesis | arrests | septum constriction/cell division | *Staphylococcus aureus* | strong primary experimental with rapid arrest (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 3-4, puls2023inhibitionofpeptidoglycan pages 2-3) | https://doi.org/10.1126/sciadv.ade9023 |
| Oxacillin | prevents recruitment of | PBP2 to the septum | *Staphylococcus aureus* | strong primary experimental (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 3-4) | https://doi.org/10.1126/sciadv.ade9023 |
| Balanced SmdA levels | enable | proper septum formation and cell splitting | *Staphylococcus aureus* | strong primary experimental (myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 1-2) | https://doi.org/10.1128/mbio.03404-21 |
| SmdA depletion | increases susceptibility to | β-lactam/cell-wall-targeting antibiotics | *Staphylococcus aureus* | strong primary experimental (myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 12-14) | https://doi.org/10.1128/mbio.03404-21 |
| GpsB | promotes septal localization of | PBP2 and PBP4 | *Staphylococcus aureus* | strong primary experimental (costa2024theroleof pages 13-14) | https://doi.org/10.1128/mbio.03235-23 |
| GpsB-dependent septal PBP2/PBP4 positioning | contributes to | mild elongation/correct non-perfectly-spherical morphogenesis | *Staphylococcus aureus* | moderate-to-strong primary experimental; shape nuance important (costa2024theroleof pages 13-14) | https://doi.org/10.1128/mbio.03235-23 |
| gpsB loss | causes | rounder, smaller cells | *Staphylococcus aureus* | strong primary experimental (costa2024theroleof pages 13-14) | https://doi.org/10.1128/mbio.03235-23 |
| Absence of MreB/elongasome | is associated with | true coccus septal-only growth program | true cocci versus rods; evolutionary/mechanistic association | uncertain/generalized review association; curate cautiously (battaje2023modelsversuspathogens pages 1-3, battaje2023modelsversuspathogens pages 3-4, pinho2013howtoget pages 11-11) | https://doi.org/10.1038/nrmicro3088 |
| DivIVA-MltG-dependent peripheral peptidoglycan synthesis | supports | ovococcal elongation/less-round morphology | ovococci such as *Streptococcus suis*; boundary case, not core true-coccus edge | strong for ovococci, boundary-only for METPO:1000668 (battaje2023modelsversuspathogens pages 4-5) | https://doi.org/10.1128/spectrum.04750-22 |


*Table: This table summarizes the highest-confidence causal edges relevant to coccus-shaped morphology (METPO:1000668), emphasizing experimentally supported mechanisms in Staphylococcus aureus and clearly separating uncertain generalizations and ovococcal boundary-case biology.*

The following expanded table supplies curation snippets and interpretation. Snippets are intentionally short; quotation marks indicate wording reported in the retrieved source or its abstract-level evidence.

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| FtsZ/Z-ring | spatially organizes | septal PG synthesis | Battaje et al. 2023: PG synthesis in spherical cocci occurs at the septal region “under FtsZ coordination.” DOI: [10.1042/BSR20221664](https://doi.org/10.1042/BSR20221664). (battaje2023modelsversuspathogens pages 3-4, battaje2023modelsversuspathogens pages 1-3) | **Curate, taxon-qualified.** Strong consensus, but FtsZ is an organizer rather than the sole mechanical driver of constriction. |
| Divisome-only/dominant growth program | produces PG at | division septum | Battaje et al. 2023: *S. aureus* division is coordinated primarily by the divisome; PG synthesis is primarily septal. (battaje2023modelsversuspathogens pages 3-4) | **Curate with updated wording.** Do not say “exclusive” because limited RodA–PBP3 elongation is now established. |
| Peptidoglycan synthesis | drives | septum constriction | Puls et al. 2023: “peptidoglycan synthesis is the essential driving force of septum constriction.” DOI: [10.1126/sciadv.ade9023](https://doi.org/10.1126/sciadv.ade9023). (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 1-2) | **High-confidence direct edge** in *S. aureus*. |
| FtsZ treadmilling alone | is insufficient for | septum constriction | PG inhibitors arrested constriction despite maintained FtsZ/divisome localization and dynamics. (puls2023inhibitionofpeptidoglycan pages 1-2, puls2023inhibitionofpeptidoglycan pages 3-4) | Curate as a negative/insufficiency relation if schema supports it; otherwise place in edge notes. |
| Vancomycin or telavancin | inhibits | septum constriction | Only 3/735 exposed cells divided; progression fell below 3% within 10 min. DOI: [10.1126/sciadv.ade9023](https://doi.org/10.1126/sciadv.ade9023). (puls2023inhibitionofpeptidoglycan pages 3-4, puls2023inhibitionofpeptidoglycan pages 2-3) | **High-confidence perturbational edge.** The proximal mechanism is inhibition of PG synthesis by substrate blocking. |
| Oxacillin | prevents | recruitment of PBP2 to septum | Only one PBP2 recruitment event was observed among 90 analyzed cells after treatment. (puls2023inhibitionofpeptidoglycan pages 4-5) | **High-confidence, assay-specific edge.** Already septal PBP2 can continue functioning. |
| PBP2 septal recruitment/activity | enables | septum closure | Oxacillin prevented recruitment and blocked division progression; PBP2 was identified as crucial for closure. (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 1-2) | **High-confidence *S. aureus* edge.** Avoid generalizing to every coccus. |
| Balanced SmdA abundance | enables | normal septum formation | Myrbråten et al. 2022: “proper levels of SmdA were necessary for cell division, including septum formation and cell splitting.” DOI: [10.1128/mbio.03404-21](https://doi.org/10.1128/mbio.03404-21). (myrbraten2022smdaisa pages 1-2) | **Curate, taxon-specific.** Both depletion and overexpression perturb division, so represent homeostatic abundance rather than simple activation. |
| SmdA depletion | increases | multiple/irregular septa and cell clustering | Depletion produced multiple septa in 20.1% of cells and reduced cross-wall splitting/autolytic activity. (myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 12-14) | Strong phenotype edge; clustering is an arrangement/separation defect, not coccus shape itself. |
| SmdA | interacts with | PBP2/PBP1–3, EzrA, and Atl | Pulldown/two-hybrid evidence identified PBPs and EzrA; GFP trapping recovered PBP2 and Atl. (myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 12-14, myrbraten2022smdaisa pages 1-2) | **Curate interactions separately from causation.** Interaction does not establish direction of regulation. |
| SmdA depletion | sensitizes | β-lactam antibiotics | MICs fell twofold for oxacillin/cefoxitin in MSSA and 2–8-fold across β-lactams in MRSA. (myrbraten2022smdaisa pages 5-7) | Application-relevant, but not a direct coccus-shape edge. |
| GpsB | promotes septal restriction of | PBP2 and PBP4 | Costa et al. 2024 found partial delocalization of PBP2/PBP4 in a *gpsB* mutant. DOI: [10.1128/mbio.03235-23](https://doi.org/10.1128/mbio.03235-23). (costa2024theroleof pages 13-14) | **Curate, taxon-specific.** |
| Loss of GpsB | increases | peripheral PBP2/PBP4 activity and PG cross-linking | Increased peripheral synthesis/cross-linking was linked to stiffer peripheral wall. (costa2024theroleof pages 13-14) | Strong mechanistic model, but “stiffness” is partly interpretive; mark that sub-edge **moderate/inferred** unless direct mechanics were measured. |
| Loss of GpsB | causes | smaller, rounder cells | Costa et al. 2024: absence of GpsB caused cells to “become more spherical.” (costa2024theroleof pages 13-14) | Strong morphology edge. Confirm an explicit aspect-ratio threshold before mapping the mutant directly to METPO:1000668. |
| RodA–PBP3 | supports | limited pre-division elongation | Costa et al. 2024 confirmed RodA/PBP3 participation in *S. aureus* elongation. (costa2024theroleof pages 13-14) | Important **refinement/anti-edge** against “septal synthesis only.” It contributes to correct coccal morphogenesis but does not simply cause sphericity. |
| Absence of canonical MreB elongation system | is associated with | true-coccus morphology | Reviews note absence of MreB homologs/elongation machinery in true cocci and repeated rod-to-coccus transitions after loss of rod-shape functions. (battaje2023modelsversuspathogens pages 3-4, pinho2013howtoget pages 11-11) | **Uncertain generalized edge.** Absence is neither experimentally sufficient nor universal; do not encode as a simple direct cause without taxon-specific genetics. |
| DivIVA phosphorylation/state | regulates through MltG localization | peripheral PG synthesis and ovococcal aspect ratio | Jiang et al. 2023: *divIVA* deletion caused abortive peripheral PG synthesis and lower aspect ratio; *mltG* deletion and phosphomimetic DivIVA produced rounder *S. suis*. DOI: [10.1128/spectrum.04750-22](https://doi.org/10.1128/spectrum.04750-22). (battaje2023modelsversuspathogens pages 4-5) | **Boundary-only.** Strong for ovococcal morphogenesis, but it should not be inserted as a core true-coccus mechanism. |

## 5. Recent developments, applications, and expert analysis

### 2023–2024 advances

- **PG synthesis, not FtsZ motion alone, is the proximate constriction driver.** Puls et al. showed immediate division arrest after PG inhibition while Z-rings remained intact. Oxacillin’s stage-specific outcome was especially informative: approximately 95% of late-stage, 63% of mid-stage, and 15% of early-stage cells completed closure, consistent with inhibition of new PBP2 recruitment while already recruited PBP2 remained functional. (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 5-7)
- **The “perfect sphere with no elongation machinery” model has been revised.** Costa et al. demonstrated a RodA–PBP3-dependent elongation phase and identified GpsB, SsaA, and RodZ as contributors. GpsB regulates where PBP2/PBP4 synthesize or cross-link PG, showing that coccal shape results from quantitative spatial balancing, not merely deletion of a rod program. (costa2024theroleof pages 13-14)
- **Species-specific divisome architectures matter.** A 2023 comparison emphasizes that conserved FtsZ operates with different partners in rods, true cocci, and ovococci. *S. pneumoniae*, despite lacking MreB, retains a midcell elongasome containing RodA–PBP2b, CozE, MreC, MreD, and RodZ. This is strong evidence against inferring cell shape from the presence/absence of one cytoskeletal gene. (battaje2023modelsversuspathogens pages 4-5, battaje2023modelsversuspathogens pages 20-21)
- **Novel regulators expand the graph beyond canonical divisome proteins.** SmdA connects septum formation, splitting, PBP/EzrA interactions, and antibiotic susceptibility, while the DivIVA–MltG axis links phosphorylation-dependent localization to peripheral PG growth in ovococci. (battaje2023modelsversuspathogens pages 4-5, myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 1-2)

### Real-world and experimental applications

1. **Antimicrobial mechanism and target discovery.** Septal PBP2 recruitment, SmdA, GpsB-regulated PBP positioning, FtsZ, and PG hydrolase control are potential intervention points. SmdA depletion reduced β-lactam MICs by 2–8-fold in MRSA and caused a 64-fold tunicamycin MIC reduction in an MSSA background, illustrating possible resistance-resensitization strategies. These remain target-validation findings rather than clinical implementations. (myrbraten2022smdaisa pages 5-7)
2. **Mechanism-of-action imaging.** Fluorescent FtsZ/PBP fusions, time-lapse microscopy, and fluorescent D-amino acids can distinguish inhibitors that collapse Z-ring organization from those that arrest PG-dependent constriction or prevent synthase recruitment. Puls et al. measured effects after minutes and quantified septal localization after 25 minutes across three biological replicates. (puls2023inhibitionofpeptidoglycan pages 5-7, puls2023inhibitionofpeptidoglycan pages 2-3)
3. **Morphology-aware infection biology.** The 2024 GpsB study notes that limited *S. aureus* elongation may matter during osteomyelitis, where elongated cells may access narrow bone channels. This is a biologically plausible application but should be marked **infection-context-specific** rather than a universal function of coccal morphology. (costa2024theroleof pages 13-14)
4. **Phenotype annotation and diagnostics.** Coccus shape remains useful in microscopy and taxonomic identification, but causal annotation should separate cell geometry, Gram status, division-plane pattern, and arrangement.
5. **Synthetic morphology.** Spatial redistribution of PBPs or controlled attenuation of elongation modules could tune cell aspect ratio, surface-area-to-volume ratio, and product/export properties. Current evidence is principally laboratory-scale; no mature industrial implementation was identified in the retrieved 2023–2024 literature.

### Expert synthesis

The most defensible expert interpretation is that **coccal shape is an emergent spatial outcome of wall growth**, not a single-gene trait. The PG sacculus is the physical shape-bearing structure; FtsZ and accessory regulators position the construction machinery; SEDS proteins and PBPs build and cross-link PG; and hydrolases remodel/split the septum. True cocci bias this network strongly toward midcell. Ovococci add a substantial peripheral-growth component, whereas rods deploy a more extensive lateral elongation system. The causal graph should therefore use process and localization nodes between genes and the terminal morphology rather than direct edges such as `ftsZ causes coccus shaped`. (battaje2023modelsversuspathogens pages 1-3, costa2024theroleof pages 13-14, puls2023inhibitionofpeptidoglycan pages 4-5)

## 6. Recommended minimal graph architecture

A conservative first expansion of `coccus_shaped_septal_growth` is:

1. `FtsZ/Z-ring —organizes→ divisome at midcell`
2. `divisome at midcell —recruits/organizes→ septal PG synthesis machinery`
3. `septal PBP2 activity —enables→ septum closure`
4. `septal PG synthesis —drives→ centripetal septum constriction`
5. `centripetal septum constriction —contributes_to→ nearly spherical daughter-cell geometry`
6. `septal hydrolase activity —enables→ daughter-cell separation`
7. `balanced SmdA abundance —enables→ normal septum formation and splitting`
8. `GpsB —promotes→ septal localization of PBP2/PBP4`
9. `RodA–PBP3 activity at outer septal edge —supports→ limited pre-division elongation`
10. `balance of septal and limited peripheral PG synthesis —maintains→ METPO:1000668`

Edges 1–4 and 7–9 have direct source support. Edge 5 is a mechanistic integration and should be labeled **inferred**, because most perturbation studies measure division/morphology rather than proving that septal synthesis alone is sufficient to generate the terminal spherical geometry. Edge 6 is biologically well supported for separation, but an Atl-specific causal chain requires additional primary evidence before committing it to the core graph.

## 7. Claims not yet ready for TraitMech curation

- **Do not curate “all cocci synthesize PG only at the septum.”** It is outdated for *S. aureus* and incorrect for ovococci.
- **Do not curate “absence of MreB causes coccus shape” as a universal direct edge.** It is an evolutionary association with counterexamples and missing sufficiency evidence.
- **Do not treat FtsZ as the mechanical constriction motor.** Its treadmilling organizes early division, but PG synthesis remains essential for closure in *S. aureus*. (puls2023inhibitionofpeptidoglycan pages 1-2, puls2023inhibitionofpeptidoglycan pages 3-4)
- **Do not infer causation from protein interaction alone.** SmdA–PBP/EzrA/Atl interactions require directional functional tests for specific regulatory edges.
- **Do not merge true cocci and ovococci into one mechanism.** DivIVA–MltG and RodA–PBP2b peripheral growth belong in an ovococcal branch.
- **Do not equate smaller/rounder with the METPO class without an operational threshold.** Curators should record aspect ratio, measurement method, growth phase, medium, and taxon.
- **Do not generalize antibiotic perturbations into native morphology causes.** Vancomycin, telavancin, and oxacillin establish dependencies of cytokinesis; they do not demonstrate adaptive causes of coccus evolution.
- **Do not assign protein CURIEs without strain context.** UniProt accessions can vary by strain and annotation; verify them when constructing the YAML.
- **Treat the proposed “cocci are an evolutionary dead end” hypothesis as historical/uncertain.** The review found repeated rod-to-coccus transitions and no documented reversions, but absence of observed reversal is not proof of impossibility. (pinho2013howtoget pages 11-11)

## 8. DOI-first bibliography

1. Costa SF et al. **The role of GpsB in *Staphylococcus aureus* cell morphogenesis.** *mBio*. Published March 2024. DOI: [10.1128/mbio.03235-23](https://doi.org/10.1128/mbio.03235-23). (costa2024theroleof pages 13-14)
2. Puls J-S et al. **Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division.** *Science Advances*. Published March 2023. DOI: [10.1126/sciadv.ade9023](https://doi.org/10.1126/sciadv.ade9023). (puls2023inhibitionofpeptidoglycan pages 4-5, puls2023inhibitionofpeptidoglycan pages 3-4)
3. Battaje RR et al. **Models versus pathogens: how conserved is the FtsZ in bacteria?** *Bioscience Reports*. Published February 2023. DOI: [10.1042/BSR20221664](https://doi.org/10.1042/BSR20221664). (battaje2023modelsversuspathogens pages 4-5, battaje2023modelsversuspathogens pages 1-3)
4. Jiang Q et al. **DivIVA Interacts with the Cell Wall Hydrolase MltG To Regulate Peptidoglycan Synthesis in *Streptococcus suis*.** *Microbiology Spectrum*. Published June 2023. DOI: [10.1128/spectrum.04750-22](https://doi.org/10.1128/spectrum.04750-22). (battaje2023modelsversuspathogens pages 4-5)
5. Myrbråten IS et al. **SmdA is a Novel Cell Morphology Determinant in *Staphylococcus aureus*.** *mBio*. Published April 2022. DOI: [10.1128/mbio.03404-21](https://doi.org/10.1128/mbio.03404-21). (myrbraten2022smdaisa pages 5-7, myrbraten2022smdaisa pages 1-2)
6. Pinho MG, Kjos M, Veening J-W. **How to get (a)round: mechanisms controlling growth and division of coccoid bacteria.** *Nature Reviews Microbiology*. Published August 2013. DOI: [10.1038/nrmicro3088](https://doi.org/10.1038/nrmicro3088). (pinho2013howtoget pages 11-11)

## Curation conclusion

**METPO:1000668 is suitable for a TraitMech graph**, but the graph should be explicitly centered on *S. aureus* or another defined true coccus. The highest-confidence causal backbone is **FtsZ-organized septal machinery → PBP-dependent septal PG synthesis → septum constriction**, supplemented by SmdA-dependent septation/splitting and GpsB-controlled spatial balancing of PBP activity. A universal bacterial “coccus mechanism” is not yet justified because true cocci and ovococci reach similar gross geometries through materially different distributions of PG growth.

References

1. (battaje2023modelsversuspathogens pages 1-3): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 32 citations and is from a peer-reviewed journal.

2. (costa2024theroleof pages 13-14): Sara F. Costa, Bruno M. Saraiva, Helena Veiga, Leonor B. Marques, Simon Schäper, Marta Sporniak, Daniel E. Vega, Ana M. Jorge, Andreia M. Duarte, António D. Brito, Andreia C. Tavares, Patricia Reed, and Mariana G. Pinho. The role of gpsb in <i>staphylococcus aureus</i> cell morphogenesis. Mar 2024. URL: https://doi.org/10.1128/mbio.03235-23, doi:10.1128/mbio.03235-23. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (puls2023inhibitionofpeptidoglycan pages 4-5): Jan-Samuel Puls, Dominik Brajtenbach, Tanja Schneider, Ulrich Kubitscheck, and Fabian Grein. Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade9023, doi:10.1126/sciadv.ade9023. This article has 34 citations and is from a highest quality peer-reviewed journal.

4. (battaje2023modelsversuspathogens pages 4-5): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 32 citations and is from a peer-reviewed journal.

5. (battaje2023modelsversuspathogens pages 3-4): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 32 citations and is from a peer-reviewed journal.

6. (puls2023inhibitionofpeptidoglycan pages 3-4): Jan-Samuel Puls, Dominik Brajtenbach, Tanja Schneider, Ulrich Kubitscheck, and Fabian Grein. Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade9023, doi:10.1126/sciadv.ade9023. This article has 34 citations and is from a highest quality peer-reviewed journal.

7. (puls2023inhibitionofpeptidoglycan pages 2-3): Jan-Samuel Puls, Dominik Brajtenbach, Tanja Schneider, Ulrich Kubitscheck, and Fabian Grein. Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade9023, doi:10.1126/sciadv.ade9023. This article has 34 citations and is from a highest quality peer-reviewed journal.

8. (myrbraten2022smdaisa pages 5-7): Ine Storaker Myrbråten, Gro Anita Stamsås, Helena Chan, Danae Morales Angeles, Tiril Mathiesen Knutsen, Zhian Salehian, Volha Shapaval, Daniel Straume, and Morten Kjos. Smda is a novel cell morphology determinant in staphylococcus aureus. Apr 2022. URL: https://doi.org/10.1128/mbio.03404-21, doi:10.1128/mbio.03404-21. This article has 16 citations and is from a domain leading peer-reviewed journal.

9. (myrbraten2022smdaisa pages 12-14): Ine Storaker Myrbråten, Gro Anita Stamsås, Helena Chan, Danae Morales Angeles, Tiril Mathiesen Knutsen, Zhian Salehian, Volha Shapaval, Daniel Straume, and Morten Kjos. Smda is a novel cell morphology determinant in staphylococcus aureus. Apr 2022. URL: https://doi.org/10.1128/mbio.03404-21, doi:10.1128/mbio.03404-21. This article has 16 citations and is from a domain leading peer-reviewed journal.

10. (puls2023inhibitionofpeptidoglycan pages 1-2): Jan-Samuel Puls, Dominik Brajtenbach, Tanja Schneider, Ulrich Kubitscheck, and Fabian Grein. Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade9023, doi:10.1126/sciadv.ade9023. This article has 34 citations and is from a highest quality peer-reviewed journal.

11. (myrbraten2022smdaisa pages 1-2): Ine Storaker Myrbråten, Gro Anita Stamsås, Helena Chan, Danae Morales Angeles, Tiril Mathiesen Knutsen, Zhian Salehian, Volha Shapaval, Daniel Straume, and Morten Kjos. Smda is a novel cell morphology determinant in staphylococcus aureus. Apr 2022. URL: https://doi.org/10.1128/mbio.03404-21, doi:10.1128/mbio.03404-21. This article has 16 citations and is from a domain leading peer-reviewed journal.

12. (pinho2013howtoget pages 11-11): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 383 citations and is from a highest quality peer-reviewed journal.

13. (puls2023inhibitionofpeptidoglycan pages 5-7): Jan-Samuel Puls, Dominik Brajtenbach, Tanja Schneider, Ulrich Kubitscheck, and Fabian Grein. Inhibition of peptidoglycan synthesis is sufficient for total arrest of staphylococcal cell division. Science Advances, Mar 2023. URL: https://doi.org/10.1126/sciadv.ade9023, doi:10.1126/sciadv.ade9023. This article has 34 citations and is from a highest quality peer-reviewed journal.

14. (battaje2023modelsversuspathogens pages 20-21): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 32 citations and is from a peer-reviewed journal.