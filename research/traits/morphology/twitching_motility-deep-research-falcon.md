---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:23:32.723683'
end_time: '2026-08-04T10:30:34.535645'
duration_seconds: 421.81
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: twitching motility
  trait_identifier: traitmech:000061
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: twitching_motility
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagella-independent surface motility driven by the extension, attachment,
    and retraction of type IV pili, producing intermittent, jerky translocation of
    cells across moist surfaces.
  parent_traits: METPO:1000702
  synonyms: twitching
  evidence_summary: 'DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type
    IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface
    translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey,
    "Bacterial motility on a surface", places twitching among the distinct surface-translocation
    strategies of bacteria.)'
  causal_graph_summary: 'twitching_type_iv_pilus_retraction: 11 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** twitching motility
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000061
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-independent surface motility driven by the extension, attachment, and retraction of type IV pili, producing intermittent, jerky translocation of cells across moist surfaces.
- **Parent traits:** METPO:1000702
- **Synonyms:** twitching
- **Existing evidence:** DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places twitching among the distinct surface-translocation strategies of bacteria.)
- **Existing causal graph summary:** twitching_type_iv_pilus_retraction: 11 nodes, 7 edges

## Research Objective

Research the microbial trait **twitching motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/twitching_motility.yaml`.

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
- **Trait label:** twitching motility
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000061
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-independent surface motility driven by the extension, attachment, and retraction of type IV pili, producing intermittent, jerky translocation of cells across moist surfaces.
- **Parent traits:** METPO:1000702
- **Synonyms:** twitching
- **Existing evidence:** DOI:10.1146/annurev.micro.56.012302.160938:  (Mattick, "Type IV pili and twitching motility", describes twitching as type-IV-pilus-driven surface translocation operating like a grappling hook.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places twitching among the distinct surface-translocation strategies of bacteria.)
- **Existing causal graph summary:** twitching_type_iv_pilus_retraction: 11 nodes, 7 edges

## Research Objective

Research the microbial trait **twitching motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/twitching_motility.yaml`.

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


# Curation report: twitching motility

## Trait record and scope

- **Trait:** twitching motility
- **Identifier:** `traitmech:000061`
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000702`
- **Synonym:** twitching

Twitching motility is flagellum-independent crawling over a moist solid surface or solid–medium interface. A surface-exposed type IV pilus (T4P) extends, its tip or filament attaches to the substratum, and retraction pulls the cell toward the attachment point. Repetition produces intermittent, jerky translocation. This “extension–attachment–retraction” cycle is the defining mechanism, not merely the presence of pili or surface spreading. Mattick’s foundational review identifies pilus retraction as the motive force and describes the characteristic intermittent jerks and directional changes; a later mechanosensing review states explicitly that repeated extension, attachment, and retraction pull the cell body forward (mattick2002typeivpili pages 5-7, webster2022thepowerof pages 10-12).

### Inclusion criteria

Curate a positive phenotype when there is evidence of:

1. translocation along a solid or interfacial surface;
2. dependence on retractile T4P or homologous type-IV filaments;
3. force-producing pilus attachment and retraction; and
4. an assay measuring interface expansion or individual-cell displacement.

Common assays include a subsurface stab inoculation followed by radial expansion at an agar–plastic interface, colony-edge imaging in glass–agarose sandwiches, and direct single-cell or single-pilus imaging. Surface attachment is a mechanistic prerequisite, so planktonic movement should not be called twitching (tala2022characterizationofpseudomonas pages 58-61, geiger2024abacterialsense pages 3-5, tala2022characterizationofpseudomonas pages 56-58).

### Boundary cases

- **Swimming:** propulsion in liquid by rotating flagella; exclude.
- **Swarming:** coordinated surface migration that is usually flagellum-dependent and often surfactant-assisted; exclude unless T4P-dependent single-cell twitching is measured separately.
- **Sliding:** passive, growth- and surface-force-driven colony spreading without a dedicated motility motor; exclude. A T4P/flagellum-deficient *Pseudomonas aeruginosa* colony can therefore spread without exhibiting twitching.
- **Gliding:** a broad surface-motility label covering several unrelated mechanisms. *Myxococcus xanthus* “social gliding” is T4P-dependent and mechanistically equivalent to twitching, whereas adventurous/non-T4P gliding is outside scope (mattick2002typeivpili pages 5-7).
- **Adhesion, natural transformation, secretion, and biofilm formation:** T4P can mediate all of these without twitching. They are associated functions, not evidence of the motility phenotype by themselves.
- **Pilus extension without productive retraction:** insufficient. Hyperpiliation can coexist with loss of twitching.

## Current mechanistic model

PilA major pilin subunits form the fiber. The PilB ATPase supplies energy for polymerization and extension through the PilC platform; the filament exits the outer membrane through the PilQ secretin. Once attached, PilT-driven depolymerization retracts the fiber. PilU can augment PilT-dependent retraction, especially under high load. Retraction converts ATP-derived mechanical work into cell-body displacement; repeated cycles produce the trait (tala2022characterizationofpseudomonas pages 56-58, tala2022characterizationofpseudomonas pages 21-24, webster2022thepowerof pages 10-12).

This simple “grappling hook” description remains useful, but modern imaging shows coordinated attachment sensing and motor switching rather than indiscriminate extension and retraction. In *P. aeruginosa*, attachment can trigger motor engagement within approximately 130–150 ms. Retraction-associated tension substantially prolongs pilus–surface adhesion: one imaging study reported median/characteristic dwell values of about 75 ms in a non-retracting `pilT` mutant versus 2,315 ms in wild type (tala2022characterizationofpseudomonas pages 58-61).

## Candidate nodes

### Trait and process nodes

- twitching motility — `traitmech:000061`
- type IV pilus-dependent motility — label-only unless the project has a validated GO/METPO mapping
- type IV pilus assembly
- type IV pilus extension
- type IV pilus attachment to surface
- type IV pilus retraction
- pilus depolymerization
- cell-body displacement across surface
- directional twitching / T4P-mediated chemotaxis — regulatory subtype, not synonymous with baseline twitching
- surface sensing and surface adaptation — associated processes, not part of the minimal phenotype

### Structural and localization nodes

- type IV pilus / type IVa pilus complex
- PilA-based pilus filament
- PilC assembly platform
- PilQ outer-membrane secretin
- bacterial cell pole
- cytoplasmic or inner-membrane motor platform
- outer membrane
- extracellular pilus tip
- solid substratum / agar–plastic or agarose–glass interface
- moist surface — retain as label-only unless an exact ENVO term is verified

### Genes and proteins

**Core machinery:** `pilA`, `pilB`, `pilC`, `pilQ`, `pilT`, and, where present, `pilU`.

**Taxon-specific regulatory candidates in *P. aeruginosa*:** `pilJ`, `pilK`, `chpB`, `chpC`, `chpA`, `pilG`, `pilH`, `cyaB`, `cpdA`, and `vfr`.

Gene symbols are not globally unique ontology identifiers. For YAML curation, use label-only nodes or taxon-specific UniProt accessions after strain selection; do not assign a single UniProt CURIE across species.

### Chemicals and molecular functions

- ATP — `CHEBI:15422`
- ADP — `CHEBI:16761`
- cyclic AMP — `CHEBI:17489`
- ATP hydrolysis / ATPase activity
- protein polymerization and depolymerization
- mechanical force / tensile load
- substratum adhesion
- *Staphylococcus aureus* phenol-soluble modulins or PSM-containing supernatant — assay-specific environmental signal

ATP is the relevant energy input to PilB/PilT-family motors, but a graph should preferably represent ATP hydrolysis as a mechanistic activity rather than assert a direct ATP→trait edge.

### Taxa

The most detailed causal evidence concerns *Pseudomonas aeruginosa*. T4P-dependent twitching or equivalent social motility also occurs in organisms including *Acinetobacter* and *Myxococcus*, but component names, pilus systems, regulation, and motor dependence vary. Regulatory branches should therefore carry an explicit taxon or strain qualifier.

## Candidate causal edges

The following table separates the broadly defensible core mechanism from *P. aeruginosa*-specific regulatory extensions.

| subject | predicate | object | taxon/scope | evidence strength | DOI/reference | short supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| PilB | polymerizes / drives extension of | type IV pilus (PilA-based filament) | Type IVa pilus systems; directly described for *Pseudomonas aeruginosa* | strong | Talà 2022, https://doi.org/10.5075/epfl-thesis-8646; Webster et al. 2022, https://doi.org/10.1128/jb.00084-22 | “PilB as the extension motor polymerizing PilA subunits” (tala2022characterizationofpseudomonas pages 56-58, tala2022characterizationofpseudomonas pages 21-24) | Core mechanistic edge; species-general within T4aP is likely, but direct phrasing here is mainly *P. aeruginosa*. |
| PilA | forms | type IV pilus filament | Broad T4P systems; directly described for *P. aeruginosa* | strong | Webster et al. 2022, https://doi.org/10.1128/jb.00084-22; Talà 2022, https://doi.org/10.5075/epfl-thesis-8646 | “PilA major pilin monomers forming the pilus fiber core” (webster2022thepowerof pages 10-12) | Safe structural edge for graph; maps trait to pilus filament rather than motility by itself. |
| PilQ secretin | enables passage of | type IV pilus through outer membrane | Gram-negative T4P systems; described for *P. aeruginosa* and broader T4P | strong | Talà 2022, https://doi.org/10.5075/epfl-thesis-8646; Singh et al. 2022, https://doi.org/10.1128/mmbr.00076-22 | “pilus fiber passes through the OM secretin complex (PilQ)” (tala2022characterizationofpseudomonas pages 21-24, singh2022landmarkdiscoveriesand pages 5-7) | Structural prerequisite edge; not specific to twitching alone, but necessary for surface-exposed pili. |
| surface attachment of T4P tip | enables | force-bearing pilus retraction | Surface-associated twitching, especially *P. aeruginosa* | strong | Talà 2022, https://doi.org/10.5075/epfl-thesis-8646; Geiger et al. 2024, https://doi.org/10.1128/jb.00442-23 | “surface attachment is a prerequisite for T4P-mediated motility”; “attachment to surfaces triggers rapid motor engagement” (geiger2024abacterialsense pages 3-5, tala2022characterizationofpseudomonas pages 58-61) | Important environmental/process edge; scope trait to moist solid/interface conditions, not planktonic growth. |
| PilT ATP hydrolysis | drives | type IV pilus retraction | Broad T4P systems; central evidence from *P. aeruginosa* and *Vibrio cholerae* | strong | Adams et al. 2019, https://doi.org/10.1371/journal.pgen.1008393; Geiger et al. 2024, https://doi.org/10.1128/jb.00442-23 | “PilT powers pilus retraction”; “PilT is essential for retraction” (geiger2024abacterialsense pages 3-5, tala2022characterizationofpseudomonas pages 56-58) | Core causal edge for twitching mechanism. |
| PilU | supports high-load, PilT-dependent | pilus retraction | Taxon-specific but supported in *P. aeruginosa* and *Vibrio cholerae* | moderate | Adams et al. 2019, https://doi.org/10.1371/journal.pgen.1008393; Talà 2022, https://doi.org/10.5075/epfl-thesis-8646 | “PilU functions exclusively in a PilT-dependent manner”; “PilU engages under high friction/load” (singh2022landmarkdiscoveriesand pages 5-7, tala2022characterizationofpseudomonas pages 58-61) | Mark as taxon/mechanism-specific support edge, not universal across all twitching systems. |
| type IV pilus retraction | displaces | cell body across surface | Surface twitching; best quantified in *P. aeruginosa* | strong | Webster et al. 2022, https://doi.org/10.1128/jb.00084-22; Talà et al. 2019, https://doi.org/10.1038/s41564-019-0378-9 | “retraction of bound pili results in cell body displacement” (webster2022thepowerof pages 10-12) | Direct phenotype-producing edge; links machinery to observable movement. |
| repeated T4P extension + attachment + retraction | causes | twitching motility | Broad trait definition; authoritative review consensus | strong | Webster et al. 2022, https://doi.org/10.1128/jb.00084-22; Mattick 2002, https://doi.org/10.1146/annurev.micro.56.012302.160938 | “repeated rounds of extension, attachment, and retraction... pulling the cell body forward in a jerky motion” (webster2022thepowerof pages 10-12, mattick2002typeivpili pages 5-7) | Best top-level phenotype edge for traitmech:000061. |
| PilJ chemoreceptor | regulates directional bias of | twitching motility toward *Staphylococcus aureus* peptide gradients | *P. aeruginosa* interspecies chemotaxis only | strong, taxon-specific | Yarrington et al. 2024, https://doi.org/10.1371/journal.pbio.3002488 | “PilJ controls chemotaxis”; deletion of PilJ ligand-binding domains “eliminates detection... while preserving motility” (yarrington2024thetypeiv pages 1-2, yarrington2024thetypeiv pages 18-20) | Curate only as regulatory branch of directional twitching, not as constitutive requirement for baseline twitching. |
| PilK methylase and ChpB demethylase | modulate | PilJ-dependent directional twitching | *P. aeruginosa* toward *S. aureus* PSM/supernatant gradients | moderate, taxon-specific | Yarrington et al. 2024, https://doi.org/10.1371/journal.pbio.3002488 | “PilK and ChpB are necessary for directional migration control” (yarrington2024thetypeiv pages 1-2, yarrington2024thetypeiv pages 3-5) | Good candidate regulatory edges; mutants retain twitching but lose directionality. |
| Pil-Chp pathway (ChpA/PilG/PilH etc.) | regulates | directional twitching / chemotactic reversals | *P. aeruginosa* interspecies chemotaxis | moderate, partly unresolved | Yarrington et al. 2024, https://doi.org/10.1371/journal.pbio.3002488 | “PilG and PilH... appear essential for generating reversals and biased movement” (yarrington2024thetypeiv pages 17-18) | Useful regulatory edge, but annotate uncertainty on exact signal flow. |
| *S. aureus* PSM-containing supernatant gradient | biases | *P. aeruginosa* twitching directionality | coculture / gradient assay context | moderate, assay-specific | Yarrington et al. 2024, https://doi.org/10.1371/journal.pbio.3002488 | “gradients of *S. aureus* supernatant (containing phenol-soluble modulins/PSMs)” (yarrington2024thetypeiv pages 3-5) | Environmental/input node for directional-twitching subgraph; not a general requirement for twitching trait. |
| CyaB / cAMP / Vfr signaling | promotes | surface adaptation and virulence-associated response downstream of T4P engagement | *P. aeruginosa* surface-sensing branch | moderate, proposed/not constitutive | Geiger et al. 2024, https://doi.org/10.1128/jb.00442-23; Yarrington et al. 2024, https://doi.org/10.1371/journal.pbio.3002488 | “cells that have engaged a surface increase production of... cAMP... via the Pil-Chp system”; “cAMP levels increase in coculture” (geiger2024abacterialsense pages 3-5, yarrington2024thetypeiv pages 16-17) | Keep as side branch only; not constitutive for defining twitching motility, and exact link to directionality remains unresolved. |


*Table: This table summarizes compact, curation-ready candidate causal edges for the twitching motility trait graph, emphasizing core type IV pilus mechanics and clearly separating taxon-specific regulatory branches from constitutive trait-defining edges.*

### Recommended minimal graph

For the existing 11-node graph, the highest-confidence backbone is:

1. `PilA subunit —part_of→ type IV pilus filament`
2. `PilB ATPase activity —positively_regulates→ T4P extension`
3. `PilC platform —enables→ pilus assembly at the inner membrane`
4. `PilQ secretin —enables→ outer-membrane passage of T4P`
5. `T4P extension —precedes→ surface attachment`
6. `surface attachment —enables→ force-bearing T4P retraction`
7. `PilT ATPase activity —positively_regulates→ T4P retraction`
8. `PilU —supports→ PilT-dependent retraction under load` **[taxon-specific]**
9. `T4P retraction —causes→ cell-body displacement toward attachment point`
10. `repeated cell-body displacement —causes→ twitching motility`

PilU should not be represented as a universally independent retraction motor. Evidence supports a PilT-dependent accessory role, and the phenotypic requirement varies with organism and mechanical load (tala2022characterizationofpseudomonas pages 58-61, tala2022characterizationofpseudomonas pages 56-58).

## Recent developments, 2023–2024

### PilJ mediates interspecies-directed twitching

A February 2024 *PLOS Biology* study showed that *P. aeruginosa* uses its Pil-Chp system to bias T4P-mediated movement toward *S. aureus* peptide signals. Removing PilJ ligand-binding domains or modifying predicted methylation sites disrupted gradient sensing while preserving motility, separating **directional sensing** from the core ability to twitch. Wild-type directionality arose from more frequent and/or larger steps toward the signal; signal-blind mutants lost that asymmetry (yarrington2024thetypeiv pages 18-20, yarrington2024thetypeiv pages 1-2).

PilK and ChpB, predicted to methylate and demethylate PilJ, were required for normal directional control. In one condition, approximately half of `ΔpilK` microcolonies dispersed while half were immotile, and motile cells showed step sizes of 1.56 ± 0.06 μm; the marked dish-to-dish heterogeneity cautions against treating this as a constitutive trait parameter (yarrington2024thetypeiv pages 9-11).

This branch has practical relevance to polymicrobial communities and *P. aeruginosa–S. aureus* coinfections, including cystic-fibrosis airway communities. Nevertheless, it should be curated as a taxon- and assay-specific modifier of twitching direction, not as part of the universal trait definition (yarrington2024thetypeiv pages 18-20, yarrington2024thetypeiv pages 3-5).

### Retraction motors as candidate surface sensors

A July 2024 *Journal of Bacteriology* review proposed an integrated *P. aeruginosa* PA14 model in which PilT detects mechanical resistance during T4P engagement and relays it through PilJ/Pil-Chp to elevate cAMP. cAMP-bound Vfr then supports surface adaptation and virulence-associated transcription. The authors characterize this relay as an active model and emphasize that the exact means by which surface engagement becomes an intracellular signal remains unresolved (geiger2024abacterialsense pages 3-5).

Accordingly, the following is suitable only as an uncertain side branch:

`surface-bound T4P retraction ─[proposed]→ PilT/PilJ signaling → CyaB → cAMP → Vfr-dependent surface adaptation`

It should not replace the established mechanical edge from retraction to cell displacement.

## Quantitative findings

Measurements depend strongly on organism, surface, load, imaging method, and whether a single pilus or whole cell is measured:

- *P. aeruginosa* whole-cell twitching is reported near **0.3 μm/s**, with bursts around **1 μm/s** when multiple pili cooperate (geiger2024abacterialsense pages 3-5, tala2022characterizationofpseudomonas pages 21-24).
- Pilus extension and retraction have been measured around **0.5 μm/s** in relevant imaging configurations (tala2022characterizationofpseudomonas pages 21-24).
- A typical retraction force is approximately **30 pN per pilus**; reported single-pilus maxima or ranges differ by system and method, including **80–110 ± 30 pN** in optical-force literature (geiger2024abacterialsense pages 3-5, singh2022landmarkdiscoveriesand pages 5-7).
- Surface adhesion can oppose retraction with substantially larger forces: approximately **150 pN** in one synthesis, while maximal aggregate/adhesive measurements as high as **750 pN** have been reported (geiger2024abacterialsense pages 3-5, webster2022thepowerof pages 10-12).
- Retraction tension increased attachment dwell time from roughly **75 ms** in non-retracting `pilT⁻` cells to **2,315 ms** in wild type under the cited imaging conditions (tala2022characterizationofpseudomonas pages 58-61).

These numbers are informative annotations, not universal thresholds for declaring the trait.

## Applications and implementation relevance

1. **Phenotyping and diagnostics.** Agar-interface twitching assays discriminate motile from nonmotile isolates and can screen mutants, clinical isolates, or anti-pilus compounds. Results require controls for growth, inoculation depth, agar concentration, hydration, and passive sliding.
2. **Biofilm research.** Twitching promotes surface exploration, microcolony organization, and biofilm expansion. Mechanical engagement also intersects with cAMP-dependent surface adaptation, making T4P dynamics potential targets for preventing initial attachment or altering mature biofilm architecture (geiger2024abacterialsense pages 3-5, webster2022thepowerof pages 10-12).
3. **Virulence and colonization.** T4P support adhesion and host interactions in addition to motility. Because these functions share machinery, `pilA`, `pilB`, `pilQ`, or `pilT` perturbations are pleiotropic; a reduced infection phenotype cannot automatically be attributed specifically to loss of twitching.
4. **Polymicrobial ecology.** PilJ-dependent directional twitching provides a mechanism for locating bacterial competitors or their secreted products, with relevance to mixed-species biofilms and chronic airway infection (yarrington2024thetypeiv pages 2-3, yarrington2024thetypeiv pages 1-2).
5. **Antimicrobial development.** PilB/PilT-family ATPases, PilQ, assembly interfaces, and pilus adhesion are candidate antivirulence targets. However, no clinical implementation follows directly from the mechanistic literature reviewed here; most applications remain assay, discovery, or preclinical concepts.

## Curation warnings

- **Do not equate T4P presence with twitching.** T4P can mediate adhesion, DNA uptake, secretion, or aggregation without cell translocation.
- **Do not make PilJ universal.** Its strong recent evidence concerns directional chemotaxis in *P. aeruginosa*, whereas baseline twitching can persist after specific PilJ sensory-domain alterations (yarrington2024thetypeiv pages 18-20, yarrington2024thetypeiv pages 1-2).
- **Do not curate direct PSM–PilJ binding yet.** Direct binding, proteolytic processing, solute-binding intermediates, and membrane-stress sensing remain competing hypotheses (yarrington2024thetypeiv pages 17-18).
- **Treat cAMP as regulatory, not as the motor energy source.** ATP hydrolysis powers extension/retraction; cAMP participates in signaling. cAMP magnitude does not map simply onto motility magnitude (yarrington2024thetypeiv pages 16-17).
- **PilU is not universally required or independent.** Its contribution is load-, system-, and taxon-dependent.
- **Avoid universal numerical thresholds.** Speed, force, and zone diameter are assay-dependent.
- **Separate phenotype from assay artifact.** Colony expansion can reflect growth or passive sliding; include nonpiliated, nonretractile, flagellar, and growth controls.
- **Do not generalize from *P. aeruginosa* to all T4P systems.** MSHA, competence, type IVb, and archaeal systems can use different motors and may perform functions other than twitching.
- **Verify ontology releases before committing CURIEs.** Preserve `traitmech:000061` and `METPO:1000702` verbatim; use label-only entries where an exact GO, ENVO, UniProt, or taxon-specific identifier has not been checked.

## DOI-first bibliography

1. **Yarrington KD, Shendruk TN, Limoli DH.** “The type IV pilus chemoreceptor PilJ controls chemotaxis of one bacterial species towards another.” *PLOS Biology* 22:e3002488. **February 2024.** https://doi.org/10.1371/journal.pbio.3002488 (yarrington2024thetypeiv pages 2-3, yarrington2024thetypeiv pages 1-2)
2. **Geiger CJ, Wong GCL, O’Toole GA.** “A bacterial sense of touch: T4P retraction motor as a means of surface sensing by *Pseudomonas aeruginosa* PA14.” *Journal of Bacteriology* 206. **July 2024.** https://doi.org/10.1128/jb.00442-23 (geiger2024abacterialsense pages 3-5)
3. **Singh PK, Little J, Donnenberg MS.** “Landmark Discoveries and Recent Advances in Type IV Pilus Research.” *Microbiology and Molecular Biology Reviews* 86(3). **September 2022.** https://doi.org/10.1128/mmbr.00076-22 (singh2022landmarkdiscoveriesand pages 5-7)
4. **Webster SS, Wong GCL, O’Toole GA.** “The Power of Touch: Type 4 Pili, the von Willebrand A Domain, and Surface Sensing by *Pseudomonas aeruginosa*.” *Journal of Bacteriology* 204(6). **June 2022.** https://doi.org/10.1128/jb.00084-22 (webster2022thepowerof pages 10-12)
5. **Talà L.** “Characterization of *Pseudomonas aeruginosa* mechanosensing through label-free imaging of type IV pili.” EPFL dissertation. **January 2022.** https://doi.org/10.5075/epfl-thesis-8646 (tala2022characterizationofpseudomonas pages 58-61, tala2022characterizationofpseudomonas pages 56-58, tala2022characterizationofpseudomonas pages 21-24)
6. **Adams DW et al.** “The type IV pilus protein PilU functions as a PilT-dependent retraction ATPase.” *PLOS Genetics* 15:e1008393. **September 2019.** https://doi.org/10.1371/journal.pgen.1008393
7. **Talà L et al.** “*Pseudomonas aeruginosa* orchestrates twitching motility by sequential control of type IV pili movements.” *Nature Microbiology* 4:774–780. **February 2019.** https://doi.org/10.1038/s41564-019-0378-9
8. **Mattick JS.** “Type IV pili and twitching motility.” *Annual Review of Microbiology* 56:289–314. **October 2002.** https://doi.org/10.1146/annurev.micro.56.012302.160938 (mattick2002typeivpili pages 5-7)

References

1. (mattick2002typeivpili pages 5-7): John S. Mattick. Type iv pili and twitching motility. Annual review of microbiology, 56:289-314, Oct 2002. URL: https://doi.org/10.1146/annurev.micro.56.012302.160938, doi:10.1146/annurev.micro.56.012302.160938. This article has 1752 citations and is from a peer-reviewed journal.

2. (webster2022thepowerof pages 10-12): Shanice S. Webster, Gerard C. L. Wong, and George A. O’Toole. The power of touch: type 4 pili, the von willebrand a domain, and surface sensing by pseudomonas aeruginosa. Jun 2022. URL: https://doi.org/10.1128/jb.00084-22, doi:10.1128/jb.00084-22. This article has 47 citations and is from a peer-reviewed journal.

3. (tala2022characterizationofpseudomonas pages 58-61): Lorenzo Anton-Louis Talà. Characterization of pseudomonas aeruginosa mechanosensing through label-free imaging of type iv pili. Dissertation, Jan 2022. URL: https://doi.org/10.5075/epfl-thesis-8646, doi:10.5075/epfl-thesis-8646. This article has 1 citations.

4. (geiger2024abacterialsense pages 3-5): C. J. Geiger, G. C. L. Wong, and G. A. O'Toole. A bacterial sense of touch: t4p retraction motor as a means of surface sensing by <i>pseudomonas aeruginosa</i> pa14. Journal of Bacteriology, Jul 2024. URL: https://doi.org/10.1128/jb.00442-23, doi:10.1128/jb.00442-23. This article has 22 citations and is from a peer-reviewed journal.

5. (tala2022characterizationofpseudomonas pages 56-58): Lorenzo Anton-Louis Talà. Characterization of pseudomonas aeruginosa mechanosensing through label-free imaging of type iv pili. Dissertation, Jan 2022. URL: https://doi.org/10.5075/epfl-thesis-8646, doi:10.5075/epfl-thesis-8646. This article has 1 citations.

6. (tala2022characterizationofpseudomonas pages 21-24): Lorenzo Anton-Louis Talà. Characterization of pseudomonas aeruginosa mechanosensing through label-free imaging of type iv pili. Dissertation, Jan 2022. URL: https://doi.org/10.5075/epfl-thesis-8646, doi:10.5075/epfl-thesis-8646. This article has 1 citations.

7. (singh2022landmarkdiscoveriesand pages 5-7): Pradip Kumar Singh, Janay Little, and Michael S. Donnenberg. Landmark discoveries and recent advances in type iv pilus research. Microbiology and Molecular Biology Reviews, Sep 2022. URL: https://doi.org/10.1128/mmbr.00076-22, doi:10.1128/mmbr.00076-22. This article has 39 citations and is from a domain leading peer-reviewed journal.

8. (yarrington2024thetypeiv pages 1-2): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.

9. (yarrington2024thetypeiv pages 18-20): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.

10. (yarrington2024thetypeiv pages 3-5): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.

11. (yarrington2024thetypeiv pages 17-18): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.

12. (yarrington2024thetypeiv pages 16-17): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.

13. (yarrington2024thetypeiv pages 9-11): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.

14. (yarrington2024thetypeiv pages 2-3): Kaitlin D. Yarrington, Tyler N. Shendruk, and Dominique H. Limoli. The type iv pilus chemoreceptor pilj controls chemotaxis of one bacterial species towards another. PLOS Biology, 22:e3002488, Feb 2024. URL: https://doi.org/10.1371/journal.pbio.3002488, doi:10.1371/journal.pbio.3002488. This article has 27 citations and is from a highest quality peer-reviewed journal.