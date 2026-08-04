---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:22:44.020882'
end_time: '2026-08-04T09:31:47.024315'
duration_seconds: 543.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ovoid shaped
  trait_identifier: METPO:1000677
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: ovoid_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has an oval morphology, rounded at
    both ends with one end often slightly broader than the other.
  parent_traits: METPO:1000666
  synonyms: S_ovoid, ovoid-shaped
  evidence_summary: 'DOI:10.1016/j.cub.2021.04.041: ovoid bacterium Streptococcus
    pneumoniae (Supports ovoid bacterial morphology as a recognized ovococcal shape.)'
  causal_graph_summary: 'ovoid_shaped_midcell_pg_assembly: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ovoid shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000677
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval morphology, rounded at both ends with one end often slightly broader than the other.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_ovoid, ovoid-shaped
- **Existing evidence:** DOI:10.1016/j.cub.2021.04.041: ovoid bacterium Streptococcus pneumoniae (Supports ovoid bacterial morphology as a recognized ovococcal shape.)
- **Existing causal graph summary:** ovoid_shaped_midcell_pg_assembly: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **ovoid shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ovoid_shaped.yaml`.

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
- **Trait label:** ovoid shaped
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000677
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval morphology, rounded at both ends with one end often slightly broader than the other.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_ovoid, ovoid-shaped
- **Existing evidence:** DOI:10.1016/j.cub.2021.04.041: ovoid bacterium Streptococcus pneumoniae (Supports ovoid bacterial morphology as a recognized ovococcal shape.)
- **Existing causal graph summary:** ovoid_shaped_midcell_pg_assembly: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **ovoid shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ovoid_shaped.yaml`.

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


# Curation report: ovoid-shaped microbial cells

## Trait record and scope

- **Trait:** ovoid shaped
- **Identifier:** **METPO:1000677**
- **Category / kind:** MORPHOLOGY / CLASS
- **Reviewed definition:** an oval cell morphology rounded at both ends, often with one end slightly broader.
- **Parent:** METPO:1000666
- **Synonyms:** *S_ovoid*, *ovoid-shaped*
- **Best-supported mechanistic model:** *Streptococcus pneumoniae* (pneumococcus; an “ovococcus”).

For causal-graph purposes, the trait should represent an **individual-cell shape**, not cell chaining, colony morphology, capsule appearance, or an environmental preference. In pneumococcus, the mature cell is described as a **prolate ellipsoid/rugby-ball shape**, conveniently expressible by an elliptic ratio, length/diameter (E = L/D). The morphology is generated by balanced **septal** and **peripheral** peptidoglycan (PG) synthesis at midcell. It is therefore a continuously produced morphogenetic state rather than a static structural attribute. (trouve2021nanoscaledynamicsof pages 7-9, stamsas2020acozehomolog pages 1-2)

### Boundaries

1. **Versus spherical cocci:** near-spherical cells have little or insufficient longitudinal extension. In pneumococcus, depletion of the peripheral-growth factors PBP2b, MreC, or MreD produces rounded/spherical cells, providing an operational boundary between ovoid and spherical morphologies. (xiang2019regulationofcell pages 24-30)
2. **Versus rods:** rods generally use MreB-guided, dispersed lateral-wall insertion. Pneumococcus lacks MreB and instead performs zonal elongation in a restricted annulus around midcell. Thus, an elongated cell caused by blocked septation is not necessarily a normal rod-shaped phenotype. (trouve2021nanoscaledynamicsof pages 1-3, fenton2016cozeisa pages 2-4)
3. **Versus diplococcal/chained arrangements:** diplococci and chains describe cell arrangement, not the shape of each cell. Chaining frequently accompanies morphogenesis defects but should be represented separately.
4. **Versus “lentil,” pointed, or minicell phenotypes:** these are abnormal shape outcomes caused by perturbing PG assembly or division-site placement and should not be treated as synonyms of ovoid.
5. **Taxonomic boundary:** the detailed graph below is principally a pneumococcal mechanism. “Ovoid shaped” occurs in other microbes, but homology of shape does not establish homology of mechanism.

## Current mechanistic understanding

Pneumococcus coordinates two PG-synthesis systems in the same nanoscale midcell zone. The **elongasome** supports peripheral PG synthesis and longitudinal extension; the **divisome** synthesizes septal PG and drives constriction. Both initially occupy one annular region and subsequently resolve into concentric zones. Elongation can continue after septation is complete. (trouve2021nanoscaledynamicsof pages 1-3)

The central current model adds PG hydrolysis to this synthesis-only description. Septal PG is produced from early in the cycle but is promptly cleaved; peripheral machinery inserts material into or around the remodeled layers. A visible septum develops when centripetal septal synthesis outpaces cleavage. Ovoid morphology therefore emerges from the relative rates and spatial displacement of septal synthesis, peripheral synthesis, and PG cleavage—not from two cleanly separated, sequential growth phases. (trouve2021nanoscaledynamicsof pages 10-11)

FtsZ supplies the common spatial organizer in this MreB-lacking bacterium. PBP2x–FtsW is associated with septal synthesis, whereas PBP2b–RodA and associated MreC/MreD/RodZ proteins support peripheral synthesis. PBP1a provides additional glycosyltransferase/transpeptidase activity whose localization and activation are controlled by proteins including CozE and, according to recent work, GarP and the pneumococcal S protein. (trouve2021nanoscaledynamicsof pages 1-3, stamsas2020acozehomolog pages 1-2, briggs2021thepneumococcaldivisome pages 6-7, millat2024characterizationofa pages 9-12, burnier2024abacterialcell pages 1-4)

## Candidate nodes grouped by type

### Phenotypes and processes

- **ovoid shaped — METPO:1000677**
- prolate-ellipsoid cell morphology — label-only candidate
- cell elongation — **GO:0051301** may be inappropriate because that term is cell division; retain label-only pending ontology review
- cell division — **GO:0051301**
- peptidoglycan biosynthetic process — **GO:0009252**
- septal peptidoglycan synthesis — label-only candidate
- peripheral peptidoglycan synthesis — label-only candidate
- septum formation/constriction — label-only candidate
- septum splitting — label-only candidate
- PG cleavage/remodeling — label-only candidate
- division-site/Z-ring positioning — label-only candidate
- cell-size homeostasis — label-only candidate
- protein phosphorylation — **GO:0006468**

### Cellular structures and locations

- midcell
- equatorial ring / PG assembly annulus
- FtsZ ring (Z-ring)
- division septum
- leading edge of invaginating septum
- peripheral/outer PG synthesis ring
- divisome complex
- elongasome complex
- cytoplasmic membrane
- peptidoglycan-containing cell wall

These should remain label-only unless the curation pipeline has validated GO cellular-component mappings appropriate to bacteria.

### Genes/proteins and complexes

**High-priority core nodes:** FtsZ, MapZ, StkP, PBP2x, FtsW, PBP2b, RodA, MreC, MreD, RodZ, PBP1a, CozE, CozEb, DivIVA, GpsB, PG hydrolase activity, and the PBP2x–FtsW and PBP2b–RodA pairs.

**Secondary/context nodes:** PBP2a, MacP, FtsA, ZapA, FtsK, FtsL, PcsB, FtsEX, PgdA, MpgA, GarP, and pneumococcal S protein. UniProt accessions should be assigned only after fixing the exact strain, because pneumococcal protein accessions are strain-specific.

### Chemicals and enzyme substrates

- peptidoglycan — **CHEBI:8005**
- lipid II — label-only pending ChEBI verification
- glycan strands and peptide crosslinks — label-only
- β-lactam antibiotics / methicillin — experimental inhibitors and clinically relevant perturbations
- fluorescent D-amino-acid or click-compatible PG probes — assay factors, not endogenous causal nodes
- zinc induction — experimental factor in conditional-expression studies, not a natural shape determinant

No electron donor, electron acceptor, metabolic pathway, or environmental preference is intrinsic to this morphology trait. Adding such nodes without shape-specific evidence would conflate morphology with growth physiology.

## Candidate causal edges

The following table is the recommended starting set for `ovoid_shaped.yaml`.

| subject | predicate | object | evidence tier | DOI | short supporting snippet | curation note |
|---|---|---|---|---|---|---|
| FtsZ ring | organizes_at | midcell PG assembly zone | strong | 10.1016/j.cub.2021.04.041 | "the FtsZ-formed Z-ring at midcell drives localization of elongation and division proteins at the cell cycle's beginning" (trouve2021nanoscaledynamicsof pages 1-3) | Supports FtsZ as proximal organizer for GO:0007049 cell division in ovococci; object kept label-only because no confident ontology ID was provided. |
| PBP2b-RodA peripheral PG synthase pair | enables | peripheral peptidoglycan synthesis → cell elongation | strong | 10.3389/fmicb.2021.737396 | "The RodA-PBP2b complex includes MreC, MreD, and RodZ and performs sidewall synthesis at the midcell for cell elongation" (briggs2021thepneumococcaldivisome pages 6-7) | Use as core elongasome edge feeding GO:0009252 peptidoglycan biosynthetic process and ultimately METPO:1000677; taxon focused on S. pneumoniae. |
| peripheral peptidoglycan synthesis | contributes_to | METPO:1000677 | strong | 10.21775/cimb.032.259 | "blocking peripheral PG synthesis (via PBP2b or MreCD depletion) produces spherical cells in chains" (xiang2019regulationofcell pages 24-30) | Good phenotype edge: loss of peripheral synthesis disrupts ovoid morphology; object may be modeled as maintenance of ovoid shape. |
| PBP2x-FtsW septal PG synthase pair | enables | septal peptidoglycan synthesis → constriction/septum formation | moderate | 10.1128/mbio.02461-20 | "PBP2b and PBP2x work together with RodA and FtsW in peripheral and septal peptidoglycan assembly respectively" (stamsas2020acozehomolog pages 1-2) | Direct pairing evidence here is summarized in review-like text within primary paper; curate as somewhat uncertain unless backed by dedicated primary FtsW/PBP2x study. |
| PBP2x activity | required_for | septum formation | strong | 10.21775/cimb.032.259 | "PBP2x inhibition causes cell elongation, indicating its role in septal PG synthesis" (xiang2019regulationofcell pages 19-24) | Strong phenotype support for septal role; can be separated from the FtsW pairing if conservative curation is preferred. |
| septal peptidoglycan synthesis + peripheral peptidoglycan synthesis | jointly_generate | METPO:1000677 | strong | 10.1016/j.cub.2021.04.041 | "septal and peripheral peptidoglycan syntheses first occur within a single annular region that later separates in two concentric regions" and "ovoid-cell morphogenesis would thus rely on the relative dynamics between peptidoglycan synthesis and cleavage" (trouve2021nanoscaledynamicsof pages 1-3, trouve2021nanoscaledynamicsof pages 10-11) | Central graph edge for trait definition; maps trait emergence to coordinated GO:0009252 sub-processes. |
| MreC/MreD/CozE complex | restricts_localization_of | PBP1a to midcell | strong | 10.1038/nmicrobiol.2016.237 | "CozE forms a complex with MreCD and PBP1a but not PBP2a" and "restricts PBP1a to midcell" (fenton2016cozeisa pages 2-4) | High-value mechanistic edge directly tied to zonal elongation and normal morphology. |
| CozE-dependent midcell PBP1a localization | promotes | zonal cell elongation / normal morphology | strong | 10.1038/nmicrobiol.2016.237 | "CozE is identified as a novel member of the MreCD complex that directs PBP1a activity to the midcell plane to promote zonal cell elongation and normal morphology" (fenton2016cozeisa pages 1-2) | Useful downstream edge from localization to morphology; taxon-specific but direct. |
| CozEb | contributes_to | cell size homeostasis | strong | 10.1128/mbio.02461-20 | "cozEb deletion results in cells that are smaller than their wild-type counterparts" and "the interplay between PBP1a and the cell size regulators CozE and CozEb is required for the maintenance of pneumococcal cell size and shape" (stamsas2020acozehomolog pages 1-2) | More directly about size than shape; keep as auxiliary morphology regulator node linked to ovoid maintenance with caution. |
| MapZ | positions | Z-ring correctly | strong | 10.21775/cimb.032.259 | "MapZ mutants are viable but severely deformed, indicating it is essential for correct Z-ring placement though not required for Z-ring formation itself" (xiang2019regulationofcell pages 19-24) | Strong spatial-organization edge upstream of FtsZ-mediated division patterning. |
| StkP phosphorylation of MapZ | stabilizes | Z-ring placement machinery | moderate | 10.21775/cimb.032.259 | "StkP phosphorylates MapZ for Z-ring stabilization without affecting FtsZ polymerization or GTPase activity" (xiang2019regulationofcell pages 19-24) | Good regulatory edge, but phosphorylation target details come via review synthesis; treat as moderate unless traced to original primary study. |
| peptidoglycan hydrolase cleavage balance | modulates | septum splitting vs elongation balance supporting METPO:1000677 | strong | 10.1016/j.cub.2021.04.041 | "Septal PG is synthesized continuously... but is promptly cleaved by PG hydrolases" and "Septum formation only occurs when the cleavage speed of septal PG is lower than its centripetal growth rate" (trouve2021nanoscaledynamicsof pages 10-11) | Strong process-level edge; specific hydrolase identities are not pinned down here, so keep node generic. |
| GarP | activates | PBP1a glycosyltransferase activity | uncertain-preprint | 10.1101/2024.11.09.622756 | "GarP stimulates PBP1a activity in vitro, particularly enhancing its glycosyltransferase (GT) activity" (millat2024characterizationofa pages 9-12) | Promising 2024 addition to PBP1a regulation graph, but preprint and not yet ideal for stable TraitMech curation without peer review. |
| GarP | associates_with | GpsB-linked cell wall remodeling complex | uncertain-preprint | 10.1101/2024.11.09.622756 | "The study suggests a cell wall remodeling complex composed of GarP/PBP1a/MacP/PBP2a/MpgA/PgdA coordinated by GpsB" (millat2024characterizationofa pages 5-9) | Complex architecture is partly speculative; do not over-curate beyond direct GarP-PBP1a/GpsB interactions. |
| S protein | interacts_with | PBP1a-PgdA repair/modification complex | uncertain-preprint | 10.1101/2024.11.08.622053 | "Direct protein-protein interactions occur between S protein, PBP1a, and the deacetylase PgdA" (burnier2024abacterialcell pages 1-4) | Relevant to morphology and cell-wall homeostasis, but preprint and oriented to stress repair rather than baseline ovoid-shape determination. |
| S protein absence | reduces | circumferential movement of PBP1a molecules | uncertain-preprint | 10.1101/2024.11.08.622053 | "Single-molecule studies show reduced circumferential movement of PBP1a molecules when S protein is absent" (burnier2024abacterialcell pages 1-4) | Interesting movement/mechanism edge for future expansion; preprint and may reflect repair-state regulation more than constitutive shape control. |


*Table: This table compiles the strongest candidate causal triples for curating the ovoid-shaped Streptococcus pneumoniae trait, emphasizing direct mechanistic evidence and clearly flagging preprint-only or less-certain claims. It is useful as a compact starting point for building a TraitMech graph around midcell peptidoglycan synthesis, division-site control, and morphology maintenance.*

### Additional conservative triples

- **PBP2b depletion — causes → lentil-shaped/rounded chained cells.** Supporting evidence: “PBP2b depletion causes lentil-shaped cells in chains.” This is strong loss-of-function evidence that peripheral synthesis is required for normal shape, but the abnormal phenotype should be a separate node. (xiang2019regulationofcell pages 24-30)
- **MreC or MreD depletion — causes → spherical cell chains.** This supports `MreC/MreD enables peripheral PG synthesis` and `peripheral PG synthesis contributes to METPO:1000677`. (xiang2019regulationofcell pages 24-30)
- **PBP2x inhibition — causes → cell elongation.** This supports `PBP2x enables septal PG synthesis`; it should not be encoded as PBP2x inhibiting elongation directly because the phenotype is secondary to defective septation. (xiang2019regulationofcell pages 19-24)
- **MapZ loss — disrupts → correct Z-ring placement — contributes to → severe deformation.** MapZ is required for correct placement, but not for Z-ring formation itself. (xiang2019regulationofcell pages 19-24)
- **CozE/MreCD — forms complex with → PBP1a.** Two-hybrid and co-immunoprecipitation evidence support a physical complex; PBP1a was delocalized when CozE or MreC was deficient. More than 700 cell units were evaluated in the cited localization analysis. (fenton2016cozeisa pages 14-17, fenton2016cozeisa pages 2-4)
- **CozEb deletion — causes → reduced cell size.** Double loss of CozE and CozEb produces poor viability and stronger shape defects; CozEb overexpression can compensate for CozE loss. This is best curated as size/homeostasis regulation rather than as an indispensable core ovoid-shape determinant. (stamsas2020acozehomolog pages 1-2)
- **DivIVA deletion — causes → shorter, rounder chained cells.** DivIVA has interactions with several division proteins, but its exact molecular action remains incompletely defined; curate the phenotype, not a detailed enzymatic mechanism. (xiang2019regulationofcell pages 24-30)

## Recent developments, 2023–2024

### 1. PBP1a regulation by GarP — promising but preprint-only

A November 2024 preprint identified **GarP**, a GpsB-associated regulator, as a direct activator of PBP1a. Co-immunoprecipitation and bacterial two-hybrid experiments support physical interaction, while in-vitro assays indicate enhanced PBP1a glycosyltransferase activity. Deleting `garP` reduced PG-label incorporation, reduced cell width, produced dispersed length distributions, and generated spherical minicells at ectopic septa. (millat2024characterizationofa pages 9-12, millat2024characterizationofa pages 15-19)

The proposed PαH helix and residues L68/F71 are candidates for the activation interface. However, the detailed structural mechanism is based partly on AlphaFold prediction, and the larger GarP/PBP1a/MacP/PBP2a/MpgA/PgdA complex remains partly hypothetical. These edges should be staged as **uncertain/preprint**. (millat2024characterizationofa pages 5-9, millat2024characterizationofa pages 1-5)

### 2. S-protein/PBP1a/PgdA cell-wall repair complex — contextual, preprint-only

A separate November 2024 preprint reports that pneumococcal S protein localizes septally, binds PG through a LysM domain, and interacts with PBP1a and the PG deacetylase PgdA. Loss of S protein reduced the fraction of circumferentially moving PBP1a, changed morphology, reduced glycan N-deacetylation, and increased susceptibility to cell-wall antibiotics, LL-37, and lysozyme. (burnier2024abacterialcell pages 1-4, burnier2024abacterialcell pages 4-7)

This advances understanding of how morphogenesis machinery is repurposed for wall repair under host stress. It does **not yet establish S protein as a constitutive determinant of ovoid shape**, and the claim that S protein activates PBP1a analogously to MacP remains a hypothesis. (burnier2024abacterialcell pages 21-25)

### 3. Contemporary expert synthesis

A 2023 review emphasizes that PG provides osmotic resistance, shape maintenance, and environmental protection and remains a major antibiotic target. For this TraitMech record, the important expert consensus is that morphology should be modeled as a regulated balance of PG polymerization, crosslinking, localization, and hydrolysis—not as the output of one “shape gene.”

## Quantitative and assay evidence

- The 2021 nanoscale study used metabolic PG labeling, click chemistry, and single-molecule localization microscopy to resolve synthesis within nanometer-scale midcell annuli. It formalized shape as a prolate ellipsoid and used the elliptic ratio **E = length/diameter** in its geometric model. (trouve2021nanoscaledynamicsof pages 7-9, trouve2021nanoscaledynamicsof pages 1-3)
- The CozE study quantified localization across **more than 700 cell units** and coupled imaging to genetics, catalytic-dead PBP1a variants, two-hybrid assays, and co-immunoprecipitation. Catalytically inactive PBP1a suppressed the lethality caused by delocalized active PBP1a, strongly linking spatially misregulated synthesis to lysis and deformation. (fenton2016cozeisa pages 14-17)
- Perturbation signatures are directionally informative: peripheral-system defects produce rounding/spheres, septal-system inhibition produces elongation or gross division defects, and division-site defects produce deformation or ectopic minicells. (xiang2019regulationofcell pages 24-30, millat2024characterizationofa pages 15-19)
- Exact speeds, absolute cell dimensions, and effect sizes should not be entered from the retrieved summaries because they were not available with sufficient source-level precision.

## Applications and real-world relevance

1. **Antibiotic mechanism and target discovery.** PBPs catalyze the final steps of PG assembly and are major β-lactam targets. Shape phenotyping can distinguish predominant impairment of peripheral versus septal synthesis. PBP mutations also contribute to pneumococcal β-lactam resistance. (stamsas2020acozehomolog pages 1-2)
2. **Combination or resensitization strategies.** Regulators such as CozE/CozEb, MacP, GarP, GpsB, or wall-repair factors may provide routes to perturb PBP function indirectly and potentially resensitize resistant organisms. This remains a research strategy rather than an established clinical implementation. (stamsas2020acozehomolog pages 1-2, millat2024characterizationofa pages 9-12)
3. **High-content antimicrobial screening.** Automated microscopy can use transitions from ovoid to spherical, elongated, pointed, or minicell phenotypes as mechanistic signatures. Such use requires growth-rate and chaining controls because terminal stress can create nonspecific shape defects.
4. **Host-defense biology.** The proposed S-protein complex connects PBP1a dynamics and PG modification to resistance against lysozyme and antimicrobial peptides, illustrating that wall architecture affects both shape and host survival. This application is recent and preprint-based. (burnier2024abacterialcell pages 1-4, burnier2024abacterialcell pages 4-7)
5. **Model bacterial cell biology.** Pneumococcus is particularly valuable for studying how elongation occurs without MreB and how elongasome and divisome activities are coordinated in the same midcell region. (trouve2021nanoscaledynamicsof pages 1-3, fenton2016cozeisa pages 2-4)

## Recommended first-pass TraitMech graph

A conservative stable graph could contain approximately these core nodes:

`FtsZ ring → midcell organization → {elongasome, divisome}`

`MapZ → correct Z-ring placement → midcell organization`

`PBP2b–RodA + MreC/MreD/RodZ → peripheral PG synthesis → longitudinal extension`

`PBP2x–FtsW → septal PG synthesis → constriction/septum formation`

`CozE–MreCD → PBP1a midcell localization → zonal PG synthesis`

`septal PG synthesis ↔ PG cleavage/remodeling`

`peripheral extension + septal constriction + controlled cleavage → METPO:1000677`

This retains the existing graph’s midcell-PG-assembly theme while making explicit that ovoid shape is the **joint outcome of competing/coordinated rates**, not merely the presence of an elongasome.

## Warnings: claims not ready for stable curation

- **Do not generalize the pneumococcal graph to all ovoid microorganisms.** The evidence is overwhelmingly taxon-specific.
- **Do not equate morphology with arrangement.** Chaining/diplococci require separate phenotype nodes.
- **Do not encode MreB as a positive determinant.** Pneumococcus lacks MreB; its absence is a mechanistic distinction from rods, not necessarily a direct cause of ovoid shape.
- **Do not treat PBP inhibition phenotypes as simple direct shape edges.** Elongation after PBP2x inhibition is mediated through failed septation.
- **Do not curate the proposed full GarP/GpsB remodeling supercomplex as established.** Direct pairwise data exist, but the complete architecture and structural activation model remain partly inferred and preprint-only. (millat2024characterizationofa pages 5-9)
- **Do not yet curate S protein as required for baseline ovoid morphology.** Current evidence better supports stress-responsive repair/modification. (burnier2024abacterialcell pages 21-25, burnier2024abacterialcell pages 1-4)
- **Do not assign strain-specific UniProt identifiers without recording the experimental strain.** Protein names are safer until strain normalization is completed.
- **Do not add unverified GO/ChEBI/EC identifiers.** Label-only nodes are preferable to incorrect grounding.
- **Do not infer exact quantitative thresholds for classifying ovoid cells.** The literature supports E = L/D as a descriptor, but the retrieved evidence does not establish a universal cutoff.

## DOI-first bibliography

1. Trouvé J, et al. **Nanoscale dynamics of peptidoglycan assembly during the cell cycle of *Streptococcus pneumoniae*.** *Current Biology*. Published July 2021. DOI: [10.1016/j.cub.2021.04.041](https://doi.org/10.1016/j.cub.2021.04.041). (trouve2021nanoscaledynamicsof pages 1-3, trouve2021nanoscaledynamicsof pages 10-11)
2. Fenton AK, et al. **CozE is a member of the MreCD complex that directs cell elongation in *Streptococcus pneumoniae*.** *Nature Microbiology*. Published December 2016. DOI: [10.1038/nmicrobiol.2016.237](https://doi.org/10.1038/nmicrobiol.2016.237). (fenton2016cozeisa pages 14-17, fenton2016cozeisa pages 2-4)
3. Stamsås GA, et al. **A CozE homolog contributes to cell size homeostasis of *Streptococcus pneumoniae*.** *mBio*. Published October 2020. DOI: [10.1128/mBio.02461-20](https://doi.org/10.1128/mbio.02461-20). (stamsas2020acozehomolog pages 1-2)
4. Briggs NS, et al. **The pneumococcal divisome: dynamic control of *Streptococcus pneumoniae* cell division.** *Frontiers in Microbiology*. Published October 2021. DOI: [10.3389/fmicb.2021.737396](https://doi.org/10.3389/fmicb.2021.737396). (briggs2021thepneumococcaldivisome pages 1-2, briggs2021thepneumococcaldivisome pages 6-7)
5. Xiang Z, et al. **Regulation of cell division in streptococci: comparing with the model rods.** *Current Issues in Molecular Biology*. Published June 2019. DOI: [10.21775/cimb.032.259](https://doi.org/10.21775/cimb.032.259). (xiang2019regulationofcell pages 19-24, xiang2019regulationofcell pages 24-30)
6. Galinier A, et al. **Recent advances in peptidoglycan synthesis and regulation in bacteria.** *Biomolecules*. Published April 2023. DOI: [10.3390/biom13050720](https://doi.org/10.3390/biom13050720).
7. Millat H, et al. **Characterization of a GpsB-associated regulator of PBP1a reveals the organization of the cell wall remodeling complex of *Streptococcus pneumoniae*.** bioRxiv preprint. Published November 2024. DOI: [10.1101/2024.11.09.622756](https://doi.org/10.1101/2024.11.09.622756). (millat2024characterizationofa pages 9-12, millat2024characterizationofa pages 5-9)
8. Burnier J, et al. **A bacterial cell wall repair and modification system to resist host antibacterial factors.** bioRxiv preprint. Published November 2024. DOI: [10.1101/2024.11.08.622053](https://doi.org/10.1101/2024.11.08.622053). (burnier2024abacterialcell pages 1-4, burnier2024abacterialcell pages 4-7)

**Curation conclusion:** The strongest defensible causal explanation for **METPO:1000677** is the spatially coordinated, midcell-restricted balance of PBP2b–RodA-dependent peripheral synthesis, PBP2x–FtsW-dependent septal synthesis, PBP1a-associated wall assembly, and PG cleavage/remodeling under FtsZ/MapZ-centered spatial control. GarP and S protein are valuable 2024 candidate extensions but should remain explicitly provisional until peer-reviewed replication and clearer linkage to baseline ovoid morphology.

References

1. (trouve2021nanoscaledynamicsof pages 7-9): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

2. (stamsas2020acozehomolog pages 1-2): Gro Anita Stamsås, Marine Restelli, Adrien Ducret, Céline Freton, Pierre Simon Garcia, Leiv Sigve Håvarstein, Daniel Straume, Christophe Grangeasse, and Morten Kjos. A coze homolog contributes to cell size homeostasis of streptococcus pneumoniae. mBio, Oct 2020. URL: https://doi.org/10.1128/mbio.02461-20, doi:10.1128/mbio.02461-20. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (xiang2019regulationofcell pages 24-30): Zhenting Xiang, Zongbo Li, Jumei Zeng, Yuqing Li, and Jiyao Li. Regulation of cell division in streptococci: comparing with the model rods. Current issues in molecular biology, 32:259-326, Jun 2019. URL: https://doi.org/10.21775/cimb.032.259, doi:10.21775/cimb.032.259. This article has 3 citations.

4. (trouve2021nanoscaledynamicsof pages 1-3): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

5. (fenton2016cozeisa pages 2-4): Andrew K. Fenton, Lamya El Mortaji, Derek T. C. Lau, David Z. Rudner, and Thomas G. Bernhardt. Coze is a member of the mrecd complex that directs cell elongation in streptococcus pneumoniae. Nature Microbiology, Dec 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.237, doi:10.1038/nmicrobiol.2016.237. This article has 91 citations and is from a highest quality peer-reviewed journal.

6. (trouve2021nanoscaledynamicsof pages 10-11): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

7. (briggs2021thepneumococcaldivisome pages 6-7): Nicholas S. Briggs, Kevin E. Bruce, Souvik Naskar, Malcolm E. Winkler, and David I. Roper. The pneumococcal divisome: dynamic control of streptococcus pneumoniae cell division. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.737396, doi:10.3389/fmicb.2021.737396. This article has 42 citations and is from a peer-reviewed journal.

8. (millat2024characterizationofa pages 9-12): Hugo Millat, Cassandra Lenoir, Cassandra Falcou, Caroline Cluzel, André Zapun, David I Roper, Cécile Morlot, Adrien Ducret, and Christophe Grangeasse. Characterization of a gpsb-associated regulator of pbp1a reveals the organization of the cell wall remodeling complex of streptococcus pneumoniae. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.09.622756, doi:10.1101/2024.11.09.622756. This article has 1 citations.

9. (burnier2024abacterialcell pages 1-4): Jessica Burnier, Clement Gallay, Kevin Bruce, Elisabet Bjånes, Louise Martin, Kinki Jim, Ho-Ching Tiffany Tsui, Amelieke Cremers, Johann Mignolet, Daniela Vollmer, Jacob Biboy, Victor Nizet, Waldemar Vollmer, Malcolm E. Winkler, and Jan-Willem Veening. A bacterial cell wall repair and modification system to resist host antibacterial factors. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.08.622053, doi:10.1101/2024.11.08.622053. This article has 1 citations.

10. (xiang2019regulationofcell pages 19-24): Zhenting Xiang, Zongbo Li, Jumei Zeng, Yuqing Li, and Jiyao Li. Regulation of cell division in streptococci: comparing with the model rods. Current issues in molecular biology, 32:259-326, Jun 2019. URL: https://doi.org/10.21775/cimb.032.259, doi:10.21775/cimb.032.259. This article has 3 citations.

11. (fenton2016cozeisa pages 1-2): Andrew K. Fenton, Lamya El Mortaji, Derek T. C. Lau, David Z. Rudner, and Thomas G. Bernhardt. Coze is a member of the mrecd complex that directs cell elongation in streptococcus pneumoniae. Nature Microbiology, Dec 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.237, doi:10.1038/nmicrobiol.2016.237. This article has 91 citations and is from a highest quality peer-reviewed journal.

12. (millat2024characterizationofa pages 5-9): Hugo Millat, Cassandra Lenoir, Cassandra Falcou, Caroline Cluzel, André Zapun, David I Roper, Cécile Morlot, Adrien Ducret, and Christophe Grangeasse. Characterization of a gpsb-associated regulator of pbp1a reveals the organization of the cell wall remodeling complex of streptococcus pneumoniae. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.09.622756, doi:10.1101/2024.11.09.622756. This article has 1 citations.

13. (fenton2016cozeisa pages 14-17): Andrew K. Fenton, Lamya El Mortaji, Derek T. C. Lau, David Z. Rudner, and Thomas G. Bernhardt. Coze is a member of the mrecd complex that directs cell elongation in streptococcus pneumoniae. Nature Microbiology, Dec 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.237, doi:10.1038/nmicrobiol.2016.237. This article has 91 citations and is from a highest quality peer-reviewed journal.

14. (millat2024characterizationofa pages 15-19): Hugo Millat, Cassandra Lenoir, Cassandra Falcou, Caroline Cluzel, André Zapun, David I Roper, Cécile Morlot, Adrien Ducret, and Christophe Grangeasse. Characterization of a gpsb-associated regulator of pbp1a reveals the organization of the cell wall remodeling complex of streptococcus pneumoniae. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.09.622756, doi:10.1101/2024.11.09.622756. This article has 1 citations.

15. (millat2024characterizationofa pages 1-5): Hugo Millat, Cassandra Lenoir, Cassandra Falcou, Caroline Cluzel, André Zapun, David I Roper, Cécile Morlot, Adrien Ducret, and Christophe Grangeasse. Characterization of a gpsb-associated regulator of pbp1a reveals the organization of the cell wall remodeling complex of streptococcus pneumoniae. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.09.622756, doi:10.1101/2024.11.09.622756. This article has 1 citations.

16. (burnier2024abacterialcell pages 4-7): Jessica Burnier, Clement Gallay, Kevin Bruce, Elisabet Bjånes, Louise Martin, Kinki Jim, Ho-Ching Tiffany Tsui, Amelieke Cremers, Johann Mignolet, Daniela Vollmer, Jacob Biboy, Victor Nizet, Waldemar Vollmer, Malcolm E. Winkler, and Jan-Willem Veening. A bacterial cell wall repair and modification system to resist host antibacterial factors. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.08.622053, doi:10.1101/2024.11.08.622053. This article has 1 citations.

17. (burnier2024abacterialcell pages 21-25): Jessica Burnier, Clement Gallay, Kevin Bruce, Elisabet Bjånes, Louise Martin, Kinki Jim, Ho-Ching Tiffany Tsui, Amelieke Cremers, Johann Mignolet, Daniela Vollmer, Jacob Biboy, Victor Nizet, Waldemar Vollmer, Malcolm E. Winkler, and Jan-Willem Veening. A bacterial cell wall repair and modification system to resist host antibacterial factors. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.08.622053, doi:10.1101/2024.11.08.622053. This article has 1 citations.

18. (briggs2021thepneumococcaldivisome pages 1-2): Nicholas S. Briggs, Kevin E. Bruce, Souvik Naskar, Malcolm E. Winkler, and David I. Roper. The pneumococcal divisome: dynamic control of streptococcus pneumoniae cell division. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.737396, doi:10.3389/fmicb.2021.737396. This article has 42 citations and is from a peer-reviewed journal.