---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:34:42.522856'
end_time: '2026-08-04T08:41:52.945772'
duration_seconds: 430.42
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: gliding
  trait_identifier: METPO:1000706
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: gliding
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A motile in which an organism moves smoothly along solid surfaces without
    flagella or pili.
  parent_traits: METPO:1000702
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces
    (Supports gliding as active surface movement without flagella.)'
  causal_graph_summary: 'gliding_surface_motility: 10 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** gliding
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000706
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism moves smoothly along solid surfaces without flagella or pili.
- **Parent traits:** METPO:1000702
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces (Supports gliding as active surface movement without flagella.)
- **Existing causal graph summary:** gliding_surface_motility: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **gliding** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gliding.yaml`.

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
- **Trait label:** gliding
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000706
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A motile in which an organism moves smoothly along solid surfaces without flagella or pili.
- **Parent traits:** METPO:1000702
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev.micro.55.1.49: move actively over surfaces (Supports gliding as active surface movement without flagella.)
- **Existing causal graph summary:** gliding_surface_motility: 10 nodes, 10 edges

## Research Objective

Research the microbial trait **gliding** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/gliding.yaml`.

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


# Curation report: microbial gliding

## 1. Scope and recommended interpretation

**Target:** `METPO:1000706`  
**Category:** MORPHOLOGY; **term kind:** CLASS; **parent:** `METPO:1000702`; **mapping:** REVIEWED.

For TraitMech, gliding should denote **active, energy-dependent translocation of a microbial cell along a solid or semisolid interface without flagellar propulsion**. Canonical *Flavobacterium* gliding uses moving cell-surface adhesins, whereas *Myxococcus xanthus* adventurous/A-motility uses a trans-envelope Agl–Glt focal-adhesion system. These systems are mechanistically nonhomologous and should be represented as separate branches converging on `METPO:1000706`. *F. columnare* glides on fish tissue, glass, agar, and other surfaces and forms spreading colonies on agar, illustrating both the biological phenotype and common assays. (vincent2022dynamicprotondependentmotors pages 1-2, thunes2024glidingmotilityproteins pages 1-2, jolivet2023integrinlikeadhesincgld pages 1-3)

The supplied wording—“moves smoothly along solid surfaces without flagella or pili”—is appropriate for canonical *Flavobacterium* motility and *M. xanthus* A-motility. It should **not** be applied indiscriminately to every historical use of “gliding,” because some cyanobacterial literature uses that label for type-IV-pilus-related movement.

### Boundary cases

- **Exclude swimming:** movement through liquid driven by flagella or other swimming machinery.
- **Exclude twitching/social motility:** type IV pilus extension–retraction. In *M. xanthus*, S-motility is twitching, whereas A-motility is the gliding branch. (chen2022flagellarmotortransformed pages 1-2)
- **Exclude passive sliding:** colony expansion driven chiefly by growth, surfactants, or reduced friction without an active cell-autonomous motor.
- **Do not equate colony spreading with gliding automatically:** spreading can combine growth, environmental conditions, collective organization, and several adhesins. Agar and glucose strongly alter *F. johnsoniae* colony morphology, and glucose can permit SprB-independent spreading on soft agar. (sato2021colonyspreadingof pages 1-3)
- **Swarming is separate:** normally a coordinated, flagellum-dependent surface behavior.
- **Mycoplasma gliding:** a genuine but mechanistically distinct ATP-driven branch. Because adequate full-text evidence was not recovered here, its machinery should not be added to this graph from this report alone.

## 2. Current mechanistic understanding

### Bacteroidota/*Flavobacterium* branch

The best-supported causal chain is:

**transmembrane proton gradient → GldL/GldM motor → T9SS-dependent SprB export and surface motion → transient SprB–substratum adhesion → cell-body displacement → gliding.**

Vincent et al. directly showed that the pH-gradient component of proton motive force powers *F. johnsoniae* gliding. GldL and GldM form dynamic membrane channels; conserved glutamates in GldL TMH2 are required; and PMF-dissipating inhibitors prevent secretion and halt cell displacement. SprB follows a closed helical path, and its substrate binding converts relative adhesin motion into screw-like forward displacement. The paper was published **25 March 2022**. (vincent2022dynamicprotondependentmotors pages 1-2)

The apparatus is intertwined with the type IX secretion system (T9SS). GldK, GldL, GldM, and GldN are shared core components, while some factors are branch-specific. PorV can be required for secretion of many type-A CTD substrates without eliminating SprB-dependent movement, whereas SprB is principally a motility adhesin. Thus, “T9SS activity” and “gliding” should be separate nodes rather than treated as equivalent phenotypes. (thunes2024glidingmotilityproteins pages 2-5, thunes2024glidingmotilityproteins pages 1-2)

### *Myxococcus xanthus* A-motility branch

The approximately 20-component Agl–Glt apparatus spans the cell envelope. Its AglR/Q/S energy-harvesting unit is homologous to MotA/B-family flagellar stators and operates as a proton-channel motor. Motors move helically in an MreB-dependent manner and become stationary relative to the substratum at force-generating bacterial focal adhesions. MreB disruption abolishes helical motor motion and blocks gliding, although whether MreB is a direct track remains unresolved. Motor aggregation also increases on harder substrates, supporting a mechanosensing model. These conclusions were synthesized in a peer-reviewed perspective published **6 May 2022**. (chen2022flagellarmotortransformed pages 1-2)

A **19 October 2023 bioRxiv preprint** proposed that CglB engagement immobilizes the Agl–Glt complex at focal-adhesion sites, enabling force transmission. It further identified CglD as a calcium-dependent, integrin-like outer-membrane lipoprotein that anchors and stabilizes the Glt–CglB assembly. The work used traction-force, bead-force, TIRF microscopy, and biochemical methods, but its preprint status requires an uncertainty flag. (jolivet2023integrinlikeadhesincgld pages 1-3)

## 3. Candidate nodes

### Trait and processes

- gliding — `METPO:1000706`
- cell motility — `GO:0048870`
- surface-associated locomotion — label-only
- bacterial focal-adhesion assembly — label-only
- trans-envelope force transduction — label-only
- mechanosensing — label-only
- type IX secretion — label-only pending curator verification of an exact ontology term
- colony spreading — label-only; assay readout, not synonymous with gliding
- virulence in fish — label-only; downstream application phenotype

### Energy, chemicals, and experimental factors

- proton — `CHEBI:15378`
- transmembrane proton gradient / proton motive force — label-only
- calcium(2+) — `CHEBI:33070`
- glucose — `CHEBI:17234` should be curator-verified before use; retain label-only if not verified locally
- carbonyl cyanide *m*-chlorophenyl hydrazone (CCCP) — label-only pending identifier verification
- solid substratum, glass, agar, fish tissue — label-only or ENVO-grounded after exact-term verification
- substrate stiffness, agar concentration, glucose concentration — experimental-factor nodes

### *Flavobacterium* proteins and complexes

- GldL–GldM proton-driven motor complex
- GldKLMN trans-envelope/T9SS complex
- GldL; GldM; GldK; GldN; GldJ
- SprB motility adhesin
- SprF, supporting SprB function
- RemA, semiredundant motility adhesin
- PorV, secretion-biased T9SS component
- SprA outer-membrane translocon
- T9SS

These should remain **label-only** until species-specific UniProt accessions are verified; the same gene symbol can refer to nonidentical proteins across species.

### *Myxococcus* proteins, structures, and localizations

- AglR/Q/S proton-channel motor
- Agl–Glt trans-envelope gliding apparatus
- GltA/B/H/K/C outer-membrane module
- CglB surface adhesin
- CglD outer-membrane lipoprotein
- MreB cytoskeleton
- bacterial focal adhesion
- leading pole, lagging pole, ventral cell surface
- plasma membrane — `GO:0005886`
- extracellular region — `GO:0005576`

### Taxon constraints

Use explicit taxon qualifiers for at least:

- *Flavobacterium johnsoniae*
- *Flavobacterium columnare*
- *Myxococcus xanthus*
- Bacteroidota when describing T9SS-associated gliding

Exact NCBITaxon identifiers should be retrieved from a taxonomy authority during YAML implementation rather than inferred here.

## 4. Candidate causal edges

The table below distinguishes strong experimental edges from taxon-specific, assay-specific, perspective-derived, preprint-derived, and speculative claims.

| subject | predicate | object | taxon/mechanistic branch | evidence snippet | DOI/reference | confidence/curation note |
|---|---|---|---|---|---|---|
| proton gradient component of PMF | powers | gliding motility | *Flavobacterium johnsoniae* / Bacteroidota gliding | “F. johnsoniae gliding motility is powered by the pH gradient component of the PMF” (vincent2022dynamicprotondependentmotors pages 1-2) | Vincent et al., 2022, PLoS Biol. doi:10.1371/journal.pbio.3001443 | High; direct experiment; taxon-specific but central curatable edge |
| GldL/GldM dynamic membrane channels | power | T9SS-dependent secretion of SprB | *F. johnsoniae* / GldLM-T9SS motor | “GldL and GldM assemble dynamic membrane channels that use the proton gradient to power both T9SS-dependent secretion of SprB” (vincent2022dynamicprotondependentmotors pages 1-2) | doi:10.1371/journal.pbio.3001443 | High; direct experiment |
| GldL/GldM dynamic membrane channels | power | SprB motion at the cell surface | *F. johnsoniae* / GldLM-T9SS motor | “use the proton gradient to power both T9SS-dependent secretion of SprB and its motion at the cell surface” (vincent2022dynamicprotondependentmotors pages 1-2) | doi:10.1371/journal.pbio.3001443 | High; direct experiment |
| type IX secretion system (T9SS) | transports to cell surface | SprB adhesin | *F. johnsoniae* / secretion-linked gliding | “SprB and other adhesins involved in gliding motility are transported to the cell surface by a multiprotein secretion apparatus, named type IX secretion system (T9SS)” (vincent2022dynamicprotondependentmotors pages 1-2) | doi:10.1371/journal.pbio.3001443 | High; direct background in primary paper |
| SprB motion relative to cell + SprB attachment to substratum | displaces cell / enables | gliding motility | *F. johnsoniae* / adhesin-driven gliding | “binding of SprB to the substratum generates adhesion points and hence that SprB motion relative to the cell displaces the cell body in a forward screw-like motion” (vincent2022dynamicprotondependentmotors pages 1-2) | doi:10.1371/journal.pbio.3001443 | High; mechanism stated in primary paper, widely accepted for this branch |
| conserved glutamate residues in GldL TMH2 | are essential for | gliding motility | *F. johnsoniae* / GldLM motor chemistry | “conserved glutamate residues in GldL TMH2 are essential for gliding motility” (vincent2022dynamicprotondependentmotors pages 1-2) | doi:10.1371/journal.pbio.3001443 | High; direct mutational evidence |
| CCCP / PMF dissipation | halts | cell displacement / SprB dynamics | *F. johnsoniae* / energetic inhibition assay | “inhibitors that dissipate the PMF prevent substrate secretion and halt cell displacement” (vincent2022dynamicprotondependentmotors pages 1-2) | doi:10.1371/journal.pbio.3001443 | High; assay-specific inhibitor edge; curate as experimental factor |
| ΔsprB deletion | causes reduced gliding and | nonspreading colonies | *Flavobacterium columnare* / virulence-linked gliding | “sprB and sprF deletion mutants were partially defective in gliding and formed nonspreading colonies” (thunes2024glidingmotilityproteins pages 1-2) | Thunes et al., 2024, J Bacteriol. doi:10.1128/jb.00068-24 | High; direct mutant phenotype; taxon-specific |
| ΔsprF deletion | causes reduced gliding and | nonspreading colonies | *F. columnare* / virulence-linked gliding | “sprB and sprF deletion mutants were partially defective in gliding and formed nonspreading colonies” (thunes2024glidingmotilityproteins pages 1-2) | doi:10.1128/jb.00068-24 | High; direct mutant phenotype; taxon-specific |
| ΔsprB or ΔsprF | retains | extracellular proteolytic activity / secretion competence | *F. columnare* / separating motility from secretion | “Wild-type cells and cells of the ΔsprB and ΔsprF mutants produced similar levels of secreted proteolytic activity” (thunes2024glidingmotilityproteins pages 2-5) | doi:10.1128/jb.00068-24 | High; useful negative/control edge to separate mechanisms |
| gldJ563 truncation | causes loss of | gliding motility while secretion is retained | *F. columnare* / track-associated factor | “gldJ563, which produces GldJ truncated at amino acid 563, was defective for gliding but was competent for secretion” (thunes2024glidingmotilityproteins pages 1-2) | doi:10.1128/jb.00068-24 | High; direct separation-of-function evidence |
| gliding motility | contributes to | virulence in rainbow trout fry | *F. columnare* / real-world host interaction | “This mutant displayed reduced virulence in rainbow trout fry, suggesting that motility contributes to virulence” (thunes2024glidingmotilityproteins pages 1-2) | doi:10.1128/jb.00068-24 | High for *F. columnare* virulence context; not core mechanism of motility itself |
| GldL/GldM motor | is thought to function directly in | protein secretion and cell movement | *F. columnare* (inferred from *F. johnsoniae* framework) | “The GldLM motor is thought to function directly in both protein secretion and in cell movement” (thunes2024glidingmotilityproteins pages 1-2) | doi:10.1128/jb.00068-24 | Medium; review/background statement in species-focused paper; use cautiously |
| agar and glucose concentrations | drastically affect | colony spreading behavior | *F. johnsoniae* / assay-environment effect | “Colony spreading… is drastically affected by agar and glucose concentrations” (sato2021colonyspreadingof pages 1-3) | Sato et al., 2021, Sci Rep. doi:10.1038/s41598-020-79762-5 | Medium; assay-specific environmental modulation, not universal gliding mechanism |
| glucose presence on soft agar | permits | spreading dendritic colonies in ΔsprB background | *F. johnsoniae* / assay-specific SprB-independent spreading | “Wild-type (WT) and ΔsprB mutant cells formed nonspreading colonies on soft agar, but spreading dendritic colonies on soft agar containing glucose” (sato2021colonyspreadingof pages 1-3) | doi:10.1038/s41598-020-79762-5 | Medium; assay-specific and partly SprB-independent branch; do not overgeneralize |
| AglR/AglQ/AglS proton channel | powers | Myxococcus gliding machinery | *Myxococcus xanthus* / A-motility | “Gliding of Myxococcus xanthus is powered by a proton channel homologous to the stators in the bacterial flagellar motor” (chen2022flagellarmotortransformed pages 1-2) | Chen & Nan, 2022, Front Microbiol. doi:10.3389/fmicb.2022.891694 | Medium; perspective-derived synthesis, but grounded in prior experiments |
| MreB | is required for | helical motor motion and gliding motility | *M. xanthus* / intracellular organization | “Disruption of MreB abolishes the helical motion of the motors and blocks gliding motility” (chen2022flagellarmotortransformed pages 1-2) | doi:10.3389/fmicb.2022.891694 | Medium; perspective citing prior work; curate as supported but indirect in this source |
| Agl–Glt complex trafficking to ventral side + CglB engagement | causes | immobilization at bFA sites | *M. xanthus* / focal adhesion mechanism | “Upon reaching the ventral side… the motorized Agl–Glt apparatus becomes coupled to the substratum via… adhesin CglB… Engagement of CglB results in Agl–Glt complex immobilization at bFA sites” (jolivet2023integrinlikeadhesincgld pages 1-3) | Jolivet et al., 2023, bioRxiv. doi:10.1101/2023.10.19.562135 | Medium; preprint-derived but mechanistically detailed |
| immobilized Agl–Glt/CglB focal adhesions | allow | force transduction and gliding locomotion | *M. xanthus* / focal adhesion mechanism | “allowing for force transduction across the cell envelope and gliding locomotion relative to the fixed bFA” (jolivet2023integrinlikeadhesincgld pages 1-3) | doi:10.1101/2023.10.19.562135 | Medium; preprint-derived |
| CglD | anchors and stabilizes | Glt–CglB gliding apparatus at bacterial focal adhesions | *M. xanthus* / focal adhesion stabilization | “CglD to be a β-integrin-like outer-membrane lipoprotein that functionally associates with and anchors the trans-envelope Glt–CglB gliding apparatus, stabilizing… this assembly at bFAs” (jolivet2023integrinlikeadhesincgld pages 1-3) | doi:10.1101/2023.10.19.562135 | Medium; preprint-derived; strong candidate but await peer review |
| calcium dependence | governs importance of | CglD in focal adhesion function | *M. xanthus* / focal adhesion stabilization | “Calcium dependence governs CglD importance” (jolivet2023integrinlikeadhesincgld pages 1-3) | doi:10.1101/2023.10.19.562135 | Medium-low; preprint-derived and specific; curate with explicit condition note |
| CglD | confers | mechanosensory and mechanotransductory capabilities | *M. xanthus* / focal adhesion stabilization | “CglD thus confers mechanosensory and mechanotransductory capabilities to the gliding apparatus” (jolivet2023integrinlikeadhesincgld pages 1-3) | doi:10.1101/2023.10.19.562135 | Medium-low; preprint-derived functional interpretation |
| stationary motor aggregation on harder substrates | increases with | substrate stiffness | *M. xanthus* / mechanosensing | “aggregation of stationary motors and motor-associated proteins intensifies on harder substrates” (chen2022flagellarmotortransformed pages 1-2) | doi:10.3389/fmicb.2022.891694 | Low-medium; perspective-derived mechanosensing claim, useful as environment edge if flagged |
| T9SS and gliding machineries | share components | GldK/GldL/GldM/GldN | Bacteroidota gliding framework | “The T9SS and gliding motility machineries share some, but not all, components” (thunes2024glidingmotilityproteins pages 1-2) | doi:10.1128/jb.00068-24 | High as architectural background; broad but phylum-specific |
| GldJ | may form | track along which SprB and other adhesins are propelled | *F. columnare*/*F. johnsoniae* framework | “GldJ, may form the track along which SprB and the other motility adhesins are propelled” (thunes2024glidingmotilityproteins pages 1-2) | doi:10.1128/jb.00068-24 | Low; explicitly speculative (“may form”); warning-level only |


*Table: This table compiles candidate causal edges for the microbial gliding trait METPO:1000706, emphasizing experimentally supported mechanisms in Flavobacterium and Myxococcus. It also flags assay-specific, taxon-specific, perspective-derived, and preprint-derived claims so curators can prioritize high-confidence edges.*

### Recommended minimal high-confidence graph

For an initial conservative graph, prioritize these edges:

1. `transmembrane proton gradient` **powers** `GldL–GldM motor`.
2. `GldL–GldM motor` **powers** `SprB secretion`.
3. `GldL–GldM motor` **powers** `SprB surface motion`.
4. `T9SS` **localizes** `SprB` **to** `cell surface`.
5. `SprB surface motion` **enables** `substratum-coupled traction`.
6. `substratum-coupled traction` **causes** `METPO:1000706`.
7. `GldL TMH2 conserved glutamates` **are required for** `GldL–GldM motor function`.
8. `CCCP/PMF dissipation` **inhibits** `SprB motion and gliding`.
9. `AglR/Q/S proton channel` **powers** `Agl–Glt motor activity`—taxon-restricted to *M. xanthus*.
10. `CglB engagement with substratum` **stabilizes** `bacterial focal adhesion`—taxon-restricted; source status should be checked.
11. `bacterial focal adhesion` **enables** `trans-envelope force transduction`.
12. `trans-envelope force transduction` **causes** `METPO:1000706`.

Do **not** merge GldLM and AglR/Q/S into one protein complex. They represent separate mechanistic solutions connected only through higher-level nodes such as proton-gradient utilization, adhesion, force transmission, and gliding.

## 5. Recent developments and applications

The strongest 2024 application evidence concerns columnaris disease. Thunes et al., published **22 March 2024**, constructed *F. columnare* mutants that separated gliding from bulk T9SS secretion. ΔsprB and ΔsprF cells moved less than one cell length before reversing, formed nonspreading colonies, but retained wild-type-like extracellular proteolytic activity. The gldJ563 truncation was also defective in gliding while retaining secretion competence. These mutants showed reduced virulence in rainbow trout fry, supporting gliding as a virulence contributor independent of generalized secretion failure. (thunes2024glidingmotilityproteins pages 2-5, thunes2024glidingmotilityproteins pages 1-2)

This finding has practical relevance for freshwater aquaculture: *F. columnare* infects skin, fins, and gills, and the authors report that fish surviving exposure to ΔsprB or gldJ563 mutants gained partial resistance to subsequent wild-type challenge. This suggests possible attenuated-strain or motility-targeted control strategies, although it is not yet evidence of a deployable vaccine. (thunes2024glidingmotilityproteins pages 1-2, thunes2024glidingmotilityproteins pages 16-18)

The study also exposes host-stage dependence. Motility-deficient mutants remained capable of killing immature fish in some models, whereas T9SS-deficient mutants were much more strongly attenuated. Therefore, gliding is a **context-dependent virulence contributor**, not a universal or sufficient cause of disease. (thunes2024glidingmotilityproteins pages 9-12, thunes2024glidingmotilityproteins pages 16-18)

## 6. Warnings: claims not yet ready for TraitMech curation

1. **Do not encode one universal gliding mechanism.** *Flavobacterium*, *Myxococcus*, mycoplasmas, and cyanobacteria use distinct systems.
2. **Do not define all gliding as pilus-independent without qualification.** This is safe for the two principal branches curated here, but historical cyanobacterial usage creates boundary ambiguity.
3. **CglD edges require an evidence-status flag.** The retrieved 2023 source is a bioRxiv preprint, not a peer-reviewed article. (jolivet2023integrinlikeadhesincgld pages 1-3)
4. **“GldJ forms the adhesin track” is speculative.** The 2024 paper says it “may form” the track; curate GldJ’s necessity/separation-of-function phenotype, not the track architecture, unless stronger structural evidence is added. (thunes2024glidingmotilityproteins pages 1-2)
5. **The precise SprB screw model contains an interpretive step.** SprB motion, substrate adhesion, and gliding are well supported, but the exact mechanical conversion is described partly as a proposal. (vincent2022dynamicprotondependentmotors pages 1-2)
6. **Colony spreading is not a clean proxy for gliding.** Agar concentration, glucose, growth, lipoproteins, and SprB-independent collective dynamics alter the assay. Store medium composition and surface as experimental context. (sato2021colonyspreadingof pages 1-3)
7. **Virulence should be downstream, not part of the trait definition.** The *F. columnare* edge is species-, host-, and developmental-stage-specific. (thunes2024glidingmotilityproteins pages 9-12, thunes2024glidingmotilityproteins pages 16-18)
8. **MreB’s exact role remains unresolved.** “Required for helical motion” is supportable; “is the direct motor track” is not. (chen2022flagellarmotortransformed pages 1-2)
9. **Substrate stiffness/mechanosensing is not yet a universal environmental rule.** Retain it as a *Myxococcus*-specific, perspective-supported condition.
10. **Do not curate Mycoplasma ATPase, cyanobacterial Pil/T2SS, or slime-nozzle edges from this evidence set.** Relevant publications were located, but sufficient full-text causal evidence was not recovered.
11. **Verify all external CURIEs before committing YAML.** Specialized proteins and complexes should remain label-only until species-specific UniProt/GO identifiers are checked.

## 7. DOI-first bibliography

1. **Thunes NC et al.** “Gliding motility proteins GldJ and SprB contribute to *Flavobacterium columnare* virulence.” *Journal of Bacteriology* 206(4). Published 22 March 2024. DOI: [10.1128/jb.00068-24](https://doi.org/10.1128/jb.00068-24). (thunes2024glidingmotilityproteins pages 1-2)
2. **Jolivet NY et al.** “Integrin-like adhesin CglD confers traction and stabilizes bacterial focal adhesions involved in myxobacterial gliding motility.” bioRxiv preprint, posted 19 October 2023. DOI: [10.1101/2023.10.19.562135](https://doi.org/10.1101/2023.10.19.562135). (jolivet2023integrinlikeadhesincgld pages 1-3)
3. **Vincent MS et al.** “Dynamic proton-dependent motors power type IX secretion and gliding motility in *Flavobacterium*.” *PLOS Biology* 20:e3001443. Published 25 March 2022. DOI: [10.1371/journal.pbio.3001443](https://doi.org/10.1371/journal.pbio.3001443). (vincent2022dynamicprotondependentmotors pages 1-2)
4. **Chen J, Nan B.** “Flagellar Motor Transformed: Biophysical Perspectives of the *Myxococcus xanthus* Gliding Mechanism.” *Frontiers in Microbiology* 13:891694. Published 6 May 2022. DOI: [10.3389/fmicb.2022.891694](https://doi.org/10.3389/fmicb.2022.891694). (chen2022flagellarmotortransformed pages 1-2)
5. **Sato K et al.** “Colony spreading of the gliding bacterium *Flavobacterium johnsoniae* in the absence of the motility adhesin SprB.” *Scientific Reports* 11:967. Published January 2021. DOI: [10.1038/s41598-020-79762-5](https://doi.org/10.1038/s41598-020-79762-5). (sato2021colonyspreadingof pages 1-3)
6. **Zhu Y, McBride MJ.** “Comparative Analysis of *Cellulophaga algicola* and *Flavobacterium johnsoniae* Gliding Motility.” *Journal of Bacteriology* 198:1743–1754. Published June 2016. DOI: [10.1128/JB.01020-15](https://doi.org/10.1128/JB.01020-15). This comparative study supports the absence of reciprocal orthology between Bacteroidota and myxobacterial motility components. (zhu2016comparativeanalysisof pages 21-26)
7. **McBride MJ.** “Bacterial gliding motility: multiple mechanisms for cell movement over surfaces.” *Annual Review of Microbiology* 55:49–75. Published 2001. DOI: [10.1146/annurev.micro.55.1.49](https://doi.org/10.1146/annurev.micro.55.1.49). This is the supplied foundational evidence and remains useful for the broad phenotype, but newer primary studies should support molecular edges.

References

1. (vincent2022dynamicprotondependentmotors pages 1-2): Maxence S. Vincent, Caterina Comas Hervada, Corinne Sebban-Kreuzer, Hugo Le Guenno, Maïalène Chabalier, Artemis Kosta, Françoise Guerlesquin, Tâm Mignot, Mark J. McBride, Eric Cascales, and Thierry Doan. Dynamic proton-dependent motors power type ix secretion and gliding motility in flavobacterium. Mar 2022. URL: https://doi.org/10.1371/journal.pbio.3001443, doi:10.1371/journal.pbio.3001443. This article has 34 citations and is from a highest quality peer-reviewed journal.

2. (thunes2024glidingmotilityproteins pages 1-2): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 7 citations and is from a peer-reviewed journal.

3. (jolivet2023integrinlikeadhesincgld pages 1-3): Nicolas Y. Jolivet, Endao Han, Akeisha M. Belgrave, Fares Saïdi, Newsha Koushki, David J. Lemon, Laura M. Faure, Betty Fleuchot, Utkarsha Mahanta, Heng Jiang, Gaurav Sharma, Jean-Bernard Fiche, Benjamin P. Bratton, Mamoudou Diallo, Beiyan Nan, David R. Zusman, Guillaume Sudre, Anthony Garza, Marcelo Nollmann, Allen J. Ehrlicher, Olivier Théodoly, Joshua W. Shaevitz, Tâm Mignot, and Salim T. Islam. Integrin-like adhesin cgld confers traction and stabilizes bacterial focal adhesions involved in myxobacterial gliding motility. bioRxiv, Oct 2023. URL: https://doi.org/10.1101/2023.10.19.562135, doi:10.1101/2023.10.19.562135. This article has 7 citations.

4. (chen2022flagellarmotortransformed pages 1-2): Jing Chen and Beiyan Nan. Flagellar motor transformed: biophysical perspectives of the myxococcus xanthus gliding mechanism. Frontiers in Microbiology, May 2022. URL: https://doi.org/10.3389/fmicb.2022.891694, doi:10.3389/fmicb.2022.891694. This article has 14 citations and is from a peer-reviewed journal.

5. (sato2021colonyspreadingof pages 1-3): Keiko Sato, Masami Naya, Yuri Hatano, Yoshio Kondo, Mari Sato, Yuka Narita, Keiji Nagano, Mariko Naito, Koji Nakayama, and Chikara Sato. Colony spreading of the gliding bacterium flavobacterium johnsoniae in the absence of the motility adhesin sprb. Scientific Reports, Jan 2021. URL: https://doi.org/10.1038/s41598-020-79762-5, doi:10.1038/s41598-020-79762-5. This article has 20 citations and is from a peer-reviewed journal.

6. (thunes2024glidingmotilityproteins pages 2-5): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 7 citations and is from a peer-reviewed journal.

7. (thunes2024glidingmotilityproteins pages 16-18): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 7 citations and is from a peer-reviewed journal.

8. (thunes2024glidingmotilityproteins pages 9-12): Nicole C. Thunes, Jason P. Evenhuis, Ryan S. Lipscomb, David Pérez-Pascual, Rebecca J. Stevick, Clayton Birkett, Jean-Marc Ghigo, and Mark J. McBride. Gliding motility proteins gldj and sprb contribute to <i>flavobacterium columnare</i> virulence. Journal of Bacteriology, Apr 2024. URL: https://doi.org/10.1128/jb.00068-24, doi:10.1128/jb.00068-24. This article has 7 citations and is from a peer-reviewed journal.

9. (zhu2016comparativeanalysisof pages 21-26): Yongtao Zhu and Mark J. McBride. Comparative analysis of cellulophaga algicola and flavobacterium johnsoniae gliding motility. Journal of Bacteriology, 198:1743-1754, Jun 2016. URL: https://doi.org/10.1128/jb.01020-15, doi:10.1128/jb.01020-15. This article has 28 citations and is from a peer-reviewed journal.