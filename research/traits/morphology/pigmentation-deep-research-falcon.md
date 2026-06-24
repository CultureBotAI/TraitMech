---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:57:42.397209'
end_time: '2026-06-18T09:22:25.961459'
duration_seconds: 1483.56
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pigmentation
  trait_identifier: METPO:1003021
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: pigmentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by the color of pigments produced by a microorganism.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.procbio.2013.06.006: bacterial pigments in food,
    pharmaceuticals, dyeing and other aspects (Supports bacterial pigments as chemically
    produced microbial color phenotypes.)'
  causal_graph_summary: 'pigmentation_biosynthetic_colorants: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pigmentation
- **METPO identifier:** METPO:1003021
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the color of pigments produced by a microorganism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.procbio.2013.06.006: bacterial pigments in food, pharmaceuticals, dyeing and other aspects (Supports bacterial pigments as chemically produced microbial color phenotypes.)
- **Existing causal graph summary:** pigmentation_biosynthetic_colorants: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pigmentation.yaml`.

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
- **Trait label:** pigmentation
- **METPO identifier:** METPO:1003021
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by the color of pigments produced by a microorganism.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.procbio.2013.06.006: bacterial pigments in food, pharmaceuticals, dyeing and other aspects (Supports bacterial pigments as chemically produced microbial color phenotypes.)
- **Existing causal graph summary:** pigmentation_biosynthetic_colorants: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pigmentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pigmentation.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Pigmentation (METPO:1003021)

### 0) Scope summary (TraitMech curation intent)
**Pigmentation (METPO:1003021)** is a microbial morphology phenotype characterized by visible coloration attributable to **pigments produced (biosynthesized) and/or accumulated by microorganisms**, rather than light-scattering effects. A key boundary case is that **pigment-derived color is distinct from structural coloration** (color arising from physical structure rather than pigment chemistry), which should be excluded from this trait definition (agarwal2023bacterialpigmentsand pages 2-4). 

Operationally, pigmentation is commonly observed as:
- **Cell-/colony-associated color** from **intracellular/insoluble pigments** (requires cell disruption for extraction) (agarwal2023bacterialpigmentsand pages 4-6).
- **Diffusible color** in medium/supernatant from **extracellular/soluble pigments** (pigment diffuses into medium; often simpler chromatographic access) (agarwal2023bacterialpigmentsand pages 4-6).

**Distinguish from nearby traits** (recommended exclusions/flags):
- **Structural coloration** (non-pigment optical effect) (agarwal2023bacterialpigmentsand pages 2-4).
- Traits that measure **pigment bioactivity** (antioxidant/antimicrobial) rather than **color phenotype** per se—these can be downstream nodes/edges but should not redefine the trait.

### 1) Current understanding: key concepts & definitions
Microbial pigments are widely described as (often) **secondary metabolites**, with production dependent on physiological state and environment; pigmentation is observed across bacteria, archaea, microalgae and fungi and can be intracellular or extracellular (agarwal2023bacterialpigmentsand pages 4-6, barreto2023microbialpigmentsmajor pages 1-2). Microbial pigmentation is increasingly discussed as an adaptive phenotype linked to stress survival and ecological interactions (e.g., UV/ROS protection; competitive interference), but the **TraitMech curation target is the color phenotype**, with mechanistic determinants represented as causal nodes upstream of visible pigment accumulation.

### 2) Candidate graph nodes (grouped)
A candidate node inventory suitable to seed `data/traits/morphology/pigmentation.yaml` is provided here:

| Group | Candidate node | Suggested grounding | Notes | Key supporting sources |
|---|---|---|---|---|
| Phenotype/Assay | pigmentation | METPO:1003021 | Visible microbial color phenotype attributable to pigments rather than structural coloration | (agarwal2023bacterialpigmentsand pages 4-6, agarwal2023bacterialpigmentsand pages 2-4) |
| Phenotype/Assay | pigment-based coloration | label only | Boundary node distinguishing pigment-derived color from structural color | (agarwal2023bacterialpigmentsand pages 2-4) |
| Phenotype/Assay | structural coloration | label only | Exclusion/boundary case; not the same as pigment production | (agarwal2023bacterialpigmentsand pages 2-4) |
| Phenotype/Assay | intracellular pigment phenotype | GO:0005622 | Cell-confined, often insoluble pigmentation detectable in cells/colonies | (agarwal2023bacterialpigmentsand pages 4-6) |
| Phenotype/Assay | extracellular/diffusible pigment phenotype | GO:0005576 | Soluble pigment released into medium/supernatant | (agarwal2023bacterialpigmentsand pages 4-6) |
| Pigment classes | carotenoids | KEGG:map00906 | Major microbial pigment class derived from isoprenoid pathways | (barreto2023microbialpigmentsmajor pages 4-6, agarwal2023bacterialpigmentsand pages 6-7) |
| Pigment classes | beta-carotene | CHEBI:17579 | Representative orange carotenoid | (agarwal2023bacterialpigmentsand pages 6-7) |
| Pigment classes | zeaxanthin | CHEBI:27306 | Xanthophyll carotenoid product of crtY/crtZ-dependent steps | (agarwal2023bacterialpigmentsand pages 6-7) |
| Pigment classes | astaxanthin | CHEBI:26947 | Ketocarotenoid relevant to industrial pigmentation | (agarwal2023bacterialpigmentsand pages 6-7, huang2024bacterialpigmentsas pages 1-2) |
| Pigment classes | canthaxanthin | CHEBI:28137 | Carotenoid pigment associated with crtW-containing modules | (agarwal2023bacterialpigmentsand pages 6-7) |
| Pigment classes | staphyloxanthin | CHEBI:20158 | Golden carotenoid of Staphylococcus aureus | (agarwal2023bacterialpigmentsand pages 6-7) |
| Pigment classes | nostoxanthin | label only | Yellow carotenoid/xanthophyll produced by Sphingomonas sp. COS14-R2 | (raman2024nostoxanthinbiosynthesisby pages 1-2) |
| Pigment classes | violacein | CHEBI:38557 | Purple bisindole pigment | (venkatramanan2024regulationofvirulence pages 5-7, agarwal2023bacterialpigmentsand pages 6-7) |
| Pigment classes | prodigiosin | CHEBI:50926 | Red tripyrrole pigment | (lu2024prodigiosinunveilingthe pages 9-10, agarwal2023bacterialpigmentsand pages 6-7, barreto2023microbialpigmentsmajor pages 10-12) |
| Pigment classes | phenazines | CHEBI:26188 | Colored heterocyclic pigment family derived from shikimate pathway | (barreto2023microbialpigmentsmajor pages 12-15) |
| Pigment classes | pyocyanin | CHEBI:58410 | Blue-green phenazine pigment of Pseudomonas aeruginosa | (xia2024quorumsensingregulationof pages 1-2, mendoza2024thehistidinekinase pages 2-5) |
| Pigment classes | melanin | CHEBI:60027 | Broad dark polymeric pigment class in fungi and bacteria | (moustafa2024mutationofhmga pages 1-2, huang2024bacterialpigmentsas pages 3-4) |
| Pigment classes | pyomelanin | label only | Brown melanin-like pigment formed from homogentisate | (moustafa2024mutationofhmga pages 1-2) |
| Pathways/modules | carotenoid biosynthesis | KEGG:map00906 | Central pathway for many yellow/orange/red pigments | (barreto2023microbialpigmentsmajor pages 4-6, agarwal2023bacterialpigmentsand pages 6-7) |
| Pathways/modules | mevalonate pathway | label only | Supplies IPP/DMAPP precursors for carotenoids in some taxa | (barreto2023microbialpigmentsmajor pages 4-6) |
| Pathways/modules | MEP pathway | label only | Alternative IPP/DMAPP precursor pathway for carotenoids | (barreto2023microbialpigmentsmajor pages 4-6, huang2024bacterialpigmentsas pages 3-4) |
| Pathways/modules | GGPP supply module | label only | Immediate precursor branch feeding phytoene synthesis | (barreto2023microbialpigmentsmajor pages 4-6) |
| Pathways/modules | violacein biosynthesis pathway | label only | vioABCDE-governed tryptophan-derived pathway | (venkatramanan2024regulationofvirulence pages 5-7) |
| Pathways/modules | prodigiosin biosynthesis pathway | label only | Pig/Red cluster-governed pathway joining MBC and monopyrrole branches | (barreto2023microbialpigmentsmajor pages 10-12) |
| Pathways/modules | MBC branch | label only | 4-methoxy-2,2′-bipyrrole-5-carbaldehyde branch of prodigiosin synthesis | (barreto2023microbialpigmentsmajor pages 10-12) |
| Pathways/modules | MAP/2-undecylpyrrole branch | label only | Monopyrrole branch condensed with MBC in prodigiosin synthesis | (barreto2023microbialpigmentsmajor pages 10-12) |
| Pathways/modules | phenazine biosynthesis pathway | label only | Core phz-dependent pathway to phenazines/pyocyanin | (agarwal2023bacterialpigmentsand pages 6-7, barreto2023microbialpigmentsmajor pages 12-15) |
| Pathways/modules | shikimate pathway | label only | Precursor pathway for phenazines and tyrosine-derived pigments | (barreto2023microbialpigmentsmajor pages 12-15) |
| Pathways/modules | pyomelanin biosynthesis pathway | label only | Tyrosine/4-hydroxyphenylpyruvate/homogentisate route | (moustafa2024mutationofhmga pages 1-2) |
| Pathways/modules | DOPA-melanin pathway | label only | Tyrosine-derived melanin route | (huang2024bacterialpigmentsas pages 3-4) |
| Pathways/modules | DHN-melanin pathway | label only | Malonyl-CoA/polyketide-derived melanin route | (huang2024bacterialpigmentsas pages 3-4) |
| Genes/enzymes/regulators | crtE | label only | Carotenoid pathway gene associated with beta-carotene and other carotenoids | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | crtB | label only | Phytoene synthase-associated carotenoid gene | (agarwal2023bacterialpigmentsand pages 6-7, barreto2023microbialpigmentsmajor pages 4-6) |
| Genes/enzymes/regulators | crtI | label only | Phytoene desaturase-associated carotenoid gene | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | crtY | label only | Lycopene beta-cyclase | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | crtZ | label only | Beta-carotene hydroxylase | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | crtW | label only | Ketolase module for astaxanthin/canthaxanthin synthesis | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | crtO/crtP/crtQ/crtM/crtN | label only | Staphyloxanthin biosynthetic module | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | vioABCDE | label only | Violacein biosynthetic operon | (venkatramanan2024regulationofvirulence pages 5-7) |
| Genes/enzymes/regulators | vioA | label only | Violacein pathway gene directly QS-responsive in reviewed model | (venkatramanan2024regulationofvirulence pages 3-5) |
| Genes/enzymes/regulators | CviI | label only | AHL synthase in Chromobacterium violaceum QS regulation | (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence pages 3-5, venkatramanan2024regulationofvirulence media e0035403) |
| Genes/enzymes/regulators | CviR | label only | AHL-responsive transcriptional regulator of violacein/OMV system | (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence pages 3-5, venkatramanan2024regulationofvirulence media e0035403) |
| Genes/enzymes/regulators | pigB/pigC/pigD/pigE/pigF/pigM/pigH/pigJ | label only | Prodigiosin-associated genes from Pig cluster | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | Pig cluster | label only | Serratia prodigiosin biosynthetic gene cluster | (barreto2023microbialpigmentsmajor pages 10-12) |
| Genes/enzymes/regulators | Red cluster | label only | Streptomyces prodigiosin-related gene cluster | (barreto2023microbialpigmentsmajor pages 10-12) |
| Genes/enzymes/regulators | CpxA | label only | Temperature-responsive regulator repressing prodigiosin cluster transcription | (lu2024prodigiosinunveilingthe pages 9-10) |
| Genes/enzymes/regulators | phzE/phzD/phzF/phzB/phzG | label only | Core phenazine biosynthesis genes | (agarwal2023bacterialpigmentsand pages 6-7) |
| Genes/enzymes/regulators | phzM | label only | Pyocyanin-modifying/biosynthetic gene linked to regulation | (mendoza2024thehistidinekinase pages 2-5, humme2024optimisedstress– pages 10-13) |
| Genes/enzymes/regulators | phzS | label only | Pyocyanin-modifying/biosynthetic gene linked to regulation | (mendoza2024thehistidinekinase pages 2-5, humme2024optimisedstress– pages 10-13) |
| Genes/enzymes/regulators | Las system | label only | QS layer contributing to phenazine/pyocyanin regulation | (xia2024quorumsensingregulationof pages 1-2, mendoza2024thehistidinekinase pages 2-5) |
| Genes/enzymes/regulators | Rhl system | label only | QS layer contributing to phenazine/pyocyanin regulation | (xia2024quorumsensingregulationof pages 1-2, mendoza2024thehistidinekinase pages 2-5) |
| Genes/enzymes/regulators | PQS system | label only | Quinolone QS system strongly tied to pyocyanin regulation | (mendoza2024thehistidinekinase pages 14-16, xia2024quorumsensingregulationof pages 1-2, mendoza2024thehistidinekinase pages 2-5) |
| Genes/enzymes/regulators | NahK | label only | Histidine kinase regulating pyocyanin through PQS | (mendoza2024thehistidinekinase pages 14-16, mendoza2024thehistidinekinase pages 2-5) |
| Genes/enzymes/regulators | hppD | label only | 4-hydroxyphenylpyruvate dioxygenase generating homogentisate | (moustafa2024mutationofhmga pages 1-2) |
| Genes/enzymes/regulators | hmgA | label only | Homogentisate 1,2-dioxygenase preventing pyomelanin accumulation | (moustafa2024mutationofhmga pages 1-2) |
| Genes/enzymes/regulators | hmgA Gly378Arg variant | label only | Variant associated with pigmented vs non-pigmented Burkholderia strains | (moustafa2024mutationofhmga pages 1-2) |
| Metabolites/signals | IPP | CHEBI:17361 | Isoprenoid precursor feeding carotenoid biosynthesis | (barreto2023microbialpigmentsmajor pages 4-6) |
| Metabolites/signals | DMAPP | CHEBI:17211 | Isoprenoid precursor feeding carotenoid biosynthesis | (barreto2023microbialpigmentsmajor pages 4-6) |
| Metabolites/signals | GGPP | CHEBI:18026 | Direct precursor to phytoene/carotenoids | (barreto2023microbialpigmentsmajor pages 4-6) |
| Metabolites/signals | phytoene | CHEBI:26126 | Early carotenoid intermediate | (barreto2023microbialpigmentsmajor pages 4-6) |
| Metabolites/signals | lycopene | CHEBI:17579 | Carotenoid intermediate/product upstream of beta-carotene | (barreto2023microbialpigmentsmajor pages 4-6, agarwal2023bacterialpigmentsand pages 6-7) |
| Metabolites/signals | tryptophan | CHEBI:16828 | Violacein precursor | (barreto2023microbialpigmentsmajor pages 12-15) |
| Metabolites/signals | homogentisate (HGA) | CHEBI:44747 | Key pyomelanin precursor | (moustafa2024mutationofhmga pages 1-2) |
| Metabolites/signals | 4-hydroxyphenylpyruvate | CHEBI:13731 | Substrate for HppD in pyomelanin branch | (moustafa2024mutationofhmga pages 1-2) |
| Metabolites/signals | maleylacetoacetate | CHEBI:16378 | Product of HmgA activity diverting HGA away from pyomelanin | (moustafa2024mutationofhmga pages 1-2) |
| Metabolites/signals | MBC | label only | Bipyrrole aldehyde branch metabolite in prodigiosin synthesis | (barreto2023microbialpigmentsmajor pages 10-12) |
| Metabolites/signals | MAP | label only | Monopyrrole branch metabolite in prodigiosin synthesis | (barreto2023microbialpigmentsmajor pages 10-12) |
| Metabolites/signals | 2-undecylpyrrole | label only | Alternative monopyrrole branch metabolite in prodigiosin synthesis | (barreto2023microbialpigmentsmajor pages 10-12) |
| Metabolites/signals | C4-C8 AHLs | label only | QS signals stimulating vioA/violacein expression | (venkatramanan2024regulationofvirulence pages 3-5) |
| Metabolites/signals | C10-C14 AHLs | label only | QS antagonistic signals in violacein regulation | (venkatramanan2024regulationofvirulence pages 3-5) |
| Metabolites/signals | C10-HSL | label only | Principal Chromobacterium QS autoinducer made by CviI | (venkatramanan2024regulationofvirulence pages 3-5, venkatramanan2024regulationofvirulence media e0035403) |
| Metabolites/signals | pyruvate | CHEBI:15361 | Counteracts pyocyanin-linked metabolic effect in culture | (xia2024quorumsensingregulationof pages 1-2) |
| Environmental/process factors | temperature | ENVO:01000206 | Major determinant across carotenoid, prodigiosin, pyocyanin, melanin systems | (lu2024prodigiosinunveilingthe pages 9-10, raman2024nostoxanthinbiosynthesisby pages 1-2, humme2024optimisedstress– pages 1-2, elzawawy2024bioproductionandoptimization pages 2-4) |
| Environmental/process factors | pH | label only | Common culture determinant of pigment output | (lu2024prodigiosinunveilingthe pages 9-10, raman2024nostoxanthinbiosynthesisby pages 1-2, elzawawy2024bioproductionandoptimization pages 2-4) |
| Environmental/process factors | oxygen transfer rate | label only | Process control affecting prodigiosin production | (lu2024prodigiosinunveilingthe pages 9-10) |
| Environmental/process factors | dissolved oxygen | label only | Bioreactor control variable for prodigiosin | (lu2024prodigiosinunveilingthe pages 9-10) |
| Environmental/process factors | dark incubation | label only | Condition associated with optimized nostoxanthin production | (raman2024nostoxanthinbiosynthesisby pages 1-2) |
| Environmental/process factors | glucose concentration | CHEBI:17234 | Carbon-source variable affecting nostoxanthin and other pigments | (raman2024nostoxanthinbiosynthesisby pages 1-2, huang2024bacterialpigmentsas pages 9-10) |
| Environmental/process factors | yeast extract concentration | label only | Nitrogen-rich medium component affecting nostoxanthin output | (raman2024nostoxanthinbiosynthesisby pages 1-2) |
| Environmental/process factors | L-tyrosine supplementation | CHEBI:17895 | Precursor supplementation used for melanin production | (elzawawy2024bioproductionandoptimization pages 2-4) |
| Environmental/process factors | ZnO nanoparticles | CHEBI:36533 | Sublethal stressor that can stimulate or abolish pyocyanin depending on dose | (humme2024optimisedstress– pages 1-2, humme2024optimisedstress– pages 10-13) |
| Environmental/process factors | low ZnO NP concentration (6.06 ug/mL) | label only | Pyocyanin-enhancing regime at 32 C | (humme2024optimisedstress– pages 1-2) |
| Environmental/process factors | high ZnO NP concentration (275.75 ug/mL) | label only | Pyocyanin-abolishing regime with higher temperature | (humme2024optimisedstress– pages 1-2) |
| Environmental/process factors | fed-batch fermentation | label only | Implementation node for high nostoxanthin titers | (raman2024nostoxanthinbiosynthesisby pages 1-2) |
| Environmental/process factors | agitation/aeration | label only | Process variables influencing prodigiosin and pyocyanin | (lu2024prodigiosinunveilingthe pages 9-10, jabłonska2023thetwofaces pages 6-7, elzawawy2024bioproductionandoptimization pages 2-4) |
| Environmental/process factors | oxidative stress | label only | Pigment-inducing/protective condition in several systems | (moustafa2024mutationofhmga pages 1-2, humme2024optimisedstress– pages 1-2, humme2024optimisedstress– pages 10-13) |
| Environmental/process factors | UV/light exposure | ENVO:01001448 | Environmental driver/protective context for pigmentation | (agarwal2023bacterialpigmentsand pages 4-6, barreto2023microbialpigmentsmajor pages 4-6, kiki2023biopigmentsofmicrobial pages 2-4) |
| Cellular structures/localization | outer membrane vesicle | GO:1990410 | Vehicle for violacein packaging and delivery; QS-linked | (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence media e0035403) |
| Cellular structures/localization | extracellular region | GO:0005576 | Localization for secreted/diffusible pigments | (agarwal2023bacterialpigmentsand pages 4-6) |
| Cellular structures/localization | intracellular region | GO:0005622 | Localization for cell-associated pigments | (agarwal2023bacterialpigmentsand pages 4-6) |
| Cellular structures/localization | colony pigmentation | label only | Assay-observed morphology endpoint on solid media | (raman2024nostoxanthinbiosynthesisby pages 1-2, agarwal2023bacterialpigmentsand pages 4-6) |
| Cellular structures/localization | culture supernatant pigmentation | label only | Assay-observed extracellular pigment endpoint | (agarwal2023bacterialpigmentsand pages 4-6, mendoza2024thehistidinekinase pages 14-16) |


*Table: This table lists candidate nodes for a microbial pigmentation causal graph, organized by entity type and annotated with suggested ontology grounding where possible. It is intended to support curation of pigmentation.yaml by highlighting phenotype boundaries, core pigment classes, mechanisms, and experimental/environmental determinants.*

### 3) Evidence-backed candidate causal edges (triples)
A curated set of edges supported by the retrieved literature is provided here:

| Edge (subject–predicate–object) | Node types | Suggested ontology grounding | Evidence snippet (short quote) | Reference (DOI + URL + year) | Uncertainty/notes |
|---|---|---|---|---|---|
| pigment-based coloration — distinct_from — structural coloration | phenotype–predicate–phenotype | METPO:1003021; label: structural coloration | “distinguishes pigment-based color from structural color” (agarwal2023bacterialpigmentsand pages 2-4) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Good scope edge for trait boundary; not a mechanistic edge. |
| intracellular pigment localization — contributes_to — pigmentation phenotype | process/localization–predicate–phenotype | GO:0005622 intracellular; METPO:1003021 | “intracellular (insoluble, cell-confined; require cell disruption/sonication)” (agarwal2023bacterialpigmentsand pages 4-6) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Useful assay/localization node; broad across taxa. |
| extracellular pigment localization — contributes_to — pigmentation phenotype | process/localization–predicate–phenotype | GO:0005576 extracellular region; METPO:1003021 | “extracellular (soluble, diffuse into medium; amenable to direct chromatography)” (agarwal2023bacterialpigmentsand pages 4-6) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Useful to distinguish colony or cell color from diffusible medium color. |
| MVA pathway — provides_precursor_for — carotenoid biosynthesis | pathway–predicate–pathway | KEGG:map00900 carotenoid biosynthesis; label: mevalonate pathway | “GGPP originates from C5 precursors (IPP and DMAPP) via either the MVA or MEP pathways” (barreto2023microbialpigmentsmajor pages 4-6) | Barreto et al. 2023. DOI:10.3390/microorganisms11122920 https://doi.org/10.3390/microorganisms11122920 | Broad review evidence; precursor relation rather than direct phenotype edge. |
| MEP pathway — provides_precursor_for — carotenoid biosynthesis | pathway–predicate–pathway | KEGG:map00900 carotenoid biosynthesis; label: 2-C-methyl-D-erythritol 4-phosphate pathway | “GGPP originates from C5 precursors (IPP and DMAPP) via either the MVA or MEP pathways” (barreto2023microbialpigmentsmajor pages 4-6) | Barreto et al. 2023. DOI:10.3390/microorganisms11122920 https://doi.org/10.3390/microorganisms11122920 | Broad review evidence. |
| crtE/crtB/crtI/crtY gene set — enables — beta-carotene biosynthesis | gene set–predicate–pathway | label: crtE/crtB/crtI/crtY; CHEBI:17579 beta-carotene | “beta-carotene: crtE, crtY, crtI, crtB” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Gene list table evidence from review; curate as generic carotenoid module. |
| crtY — catalyzes_step_in — zeaxanthin biosynthesis | gene/enzyme–predicate–pathway | label: crtY lycopene beta-cyclase; CHEBI:27306 zeaxanthin | “crtY = lycopene beta-cyclase” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Strong enzyme-function edge; product phenotype indirect. |
| crtZ — catalyzes_step_in — zeaxanthin biosynthesis | gene/enzyme–predicate–pathway | label: crtZ beta-carotene hydroxylase; CHEBI:27306 zeaxanthin | “crtZ = beta-carotene hydroxylase” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Strong enzyme-function edge. |
| crtW — enables — astaxanthin or canthaxanthin biosynthesis | gene–predicate–pathway | label: crtW; CHEBI:26947 astaxanthin; CHEBI:28137 canthaxanthin | “astaxanthin: crtW, crtZ; canthaxanthin: crtE, crtY, crtI, crtB, crtW” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Taxon or product specific but well supported at pathway level. |
| crtO/crtP/crtQ/crtM/crtN module — enables — staphyloxanthin biosynthesis | gene set–predicate–pathway | label: crtO/crtP/crtQ/crtM/crtN; CHEBI:20158 staphyloxanthin | “staphyloxanthin: crtO, crtP, crtQ, crtM, crtN” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Useful taxon-specific carotenoid subgraph, mainly Staphylococcus. |
| vioABCDE operon — enables — violacein biosynthesis | gene cluster–predicate–pathway | label: vioABCDE; CHEBI:38557 violacein | “Violacein synthesis is ‘constrained by the quorum-sensing machinery’ and is governed by the vioABCDE operon” (venkatramanan2024regulationofvirulence pages 5-7) | Venkatramanan and Nalini 2024. DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 | Strong direct edge. |
| CviI/CviR quorum-sensing system — positively_regulates — vioABCDE operon | regulatory system–predicate–gene cluster | label: CviI/CviR QS system; label: vioABCDE | “The CviI synthase makes AHLs that complex with CviR to stimulate the vioABCDE operon” (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence media e0035403) | Venkatramanan and Nalini 2024. DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 | Strong direct regulatory edge. |
| C4 to C8 AHLs — stimulate — vioA transcription | metabolite/signal–predicate–gene | label: N-acyl-L-homoserine lactones; label: vioA | “C4–C8 AHLs stimulate vioA transcription” (venkatramanan2024regulationofvirulence pages 3-5) | Venkatramanan and Nalini 2024. DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 | Chain length specificity is important; likely taxon-specific. |
| C10 to C14 AHLs — inhibits — violacein biosynthesis | metabolite/signal–predicate–pathway | label: N-acyl-L-homoserine lactones; CHEBI:38557 violacein | “longer AHLs (C10–C14) act as antagonists” (venkatramanan2024regulationofvirulence pages 3-5) | Venkatramanan and Nalini 2024. DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 | Useful negative-regulation edge; chain-length dependent. |
| violacein biosynthesis — promotes — OMV vesiculation | pathway/metabolite–predicate–process | CHEBI:38557 violacein; GO:1990410 extracellular vesicle | “Deletion of vioABCDE causes a twofold reduction in vesiculation” (venkatramanan2024regulationofvirulence pages 5-7) | Venkatramanan and Nalini 2024. DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 | Strong in Chromobacterium; may not generalize beyond taxon. |
| outer membrane vesicles — transports_or_delivers — violacein | cellular structure/process–predicate–metabolite | GO:1990410 extracellular vesicle; CHEBI:38557 violacein | “C. violaceum packages violacein in OMVs to deliver it to competitors” (venkatramanan2024regulationofvirulence pages 5-7) | Venkatramanan and Nalini 2024. DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 | Transport edge, not core biosynthetic edge. |
| Pig or Red gene cluster — enables — prodigiosin biosynthesis | gene cluster–predicate–pathway | label: Pig or Red cluster; CHEBI:50926 prodigiosin | “Pig (Serratia) and Red (Streptomyces) gene clusters regulate prodigiosin biosynthesis” (barreto2023microbialpigmentsmajor pages 10-12) | Barreto et al. 2023. DOI:10.3390/microorganisms11122920 https://doi.org/10.3390/microorganisms11122920 | Broad cluster-level edge; suitable generic prodigiosin subgraph. |
| pigB/pigC/pigD/pigE/pigF/pigM/pigH/pigJ — enables — prodigiosin biosynthesis | gene set–predicate–pathway | label: pig cluster genes; CHEBI:50926 prodigiosin | “prodigiosin (pigB, pigC, pigD, pigE, pigF, pigM, pigH, pigJ)” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Gene list only; individual step assignments not given in gathered evidence. |
| temperature above 30 C — decreases — prodigiosin biosynthesis | environment–predicate–pathway | ENVO:01000206 temperature; CHEBI:50926 prodigiosin | “enzymes become inactive above ~30°C” (lu2024prodigiosinunveilingthe pages 9-10) | Lu et al. 2024. DOI:10.3389/fmicb.2024.1412776 https://doi.org/10.3389/fmicb.2024.1412776 | Condition-specific; mechanism via enzyme activity and CpxA noted below. |
| elevated temperature — activates — CpxA sensor/regulator | environment–predicate–regulator | ENVO:01000206 temperature; label: CpxA | “Elevated temperatures also activate the CpxA two-component sensor” (lu2024prodigiosinunveilingthe pages 9-10) | Lu et al. 2024. DOI:10.3389/fmicb.2024.1412776 https://doi.org/10.3389/fmicb.2024.1412776 | Taxon-specific to Serratia context. |
| CpxA activation — represses — pig cluster transcription | regulator–predicate–gene cluster | label: CpxA; label: pig cluster | “repressing pig cluster transcription” (lu2024prodigiosinunveilingthe pages 9-10) | Lu et al. 2024. DOI:10.3389/fmicb.2024.1412776 https://doi.org/10.3389/fmicb.2024.1412776 | Strong mechanistic edge in prodigiosin producers. |
| pH 7 to 9 — increases — prodigiosin production | environment–predicate–phenotype/pathway | label: pH 7 to 9; CHEBI:50926 prodigiosin | “pH 7–9 optimal and extremes (<3.0 or >10.0) unfavorable” (lu2024prodigiosinunveilingthe pages 9-10) | Lu et al. 2024. DOI:10.3389/fmicb.2024.1412776 https://doi.org/10.3389/fmicb.2024.1412776 | Broad process edge; exact optimum can vary by strain. |
| lower oxygen transfer rate — increases — prodigiosin biosynthesis | process/environment–predicate–pathway | label: oxygen transfer rate; CHEBI:50926 prodigiosin | “lower OTRs (oxygen limitation) can actually increase PG” (lu2024prodigiosinunveilingthe pages 9-10) | Lu et al. 2024. DOI:10.3389/fmicb.2024.1412776 https://doi.org/10.3389/fmicb.2024.1412776 | Conflicts with some older high-aeration reports; curate with note that effect is process-specific. |
| low-oxygen bioreactor strategy — results_in — prodigiosin productivity 36.1 mg/L/h | process–predicate–quantitative phenotype | label: low dissolved oxygen strategy; CHEBI:50926 prodigiosin | “production of 1066.2 mg of prodigiosin in 24 h and a productivity of 36.1 mgproduct/(L.h)” (lu2024prodigiosinunveilingthe pages 9-10) | Pereira and de Carvalho 2024. DOI:10.3390/pr12091794 https://doi.org/10.3390/pr12091794 | Implementation and statistics edge; useful quantitative process node. |
| phzE/phzD/phzF/phzB/phzG — enables — phenazine biosynthesis | gene set–predicate–pathway | label: phz core genes; CHEBI:26188 phenazine | “phenazines/pyocyanin (phzE, phzD, phzF, phzB, phzG)” (agarwal2023bacterialpigmentsand pages 6-7) | Agarwal et al. 2023. DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 | Core phenazine pathway edge; pyocyanin is a downstream decorated phenazine. |
| shikimate pathway — precursor_of — phenazine biosynthesis | pathway–predicate–pathway | label: shikimate pathway; CHEBI:26188 phenazine | “Phenazine pigments (including pyocyanin) are stated to ‘derive from the shikimate pathway’” (barreto2023microbialpigmentsmajor pages 12-15) | Barreto et al. 2023. DOI:10.3390/microorganisms11122920 https://doi.org/10.3390/microorganisms11122920 | Broad precursor relation. |
| Las/Rhl/PQS quorum-sensing systems — positively_regulates — phenazine or pyocyanin biosynthesis | regulatory system–predicate–pathway | label: Las/Rhl/PQS QS systems; CHEBI:58410 pyocyanin | “the three interconnected QS systems (Las, Rhl, PQS)” and “QS-regulated pyocyanin” (xia2024quorumsensingregulationof pages 1-2, mendoza2024thehistidinekinase pages 2-5) | Xia et al. 2024. DOI:10.1128/aac.00118-24 https://doi.org/10.1128/aac.00118-24; Mendoza et al. 2024. DOI:10.1128/jb.00276-23 https://doi.org/10.1128/jb.00276-23 | Strong direct regulatory edge in Pseudomonas aeruginosa. |
| NahK histidine kinase — negatively_regulates — pyocyanin production | regulator–predicate–phenotype/pathway | label: NahK; CHEBI:58410 pyocyanin | “Deletion of nahK leads to a fourfold increase in PYO production” (mendoza2024thehistidinekinase pages 14-16, mendoza2024thehistidinekinase pages 2-5) | Mendoza et al. 2024. DOI:10.1128/jb.00276-23 https://doi.org/10.1128/jb.00276-23 | Direction inferred from knockout phenotype; curate as negative regulator. |
| NahK — regulates_through — PQS system | regulator–predicate–regulatory system | label: NahK; label: PQS system | “NahK regulates pyocyanin production through the PQS system” (mendoza2024thehistidinekinase pages 14-16) | Mendoza et al. 2024. DOI:10.1128/jb.00276-23 https://doi.org/10.1128/jb.00276-23 | Strong paper-title-supported edge. |
| pyocyanin production — alters — carbon flux and decreases PDH activity | metabolite/pathway–predicate–process | CHEBI:58410 pyocyanin; label: pyruvate dehydrogenase activity | “pyocyanin alters cellular carbon flux and ‘decreased the activity of pyruvate dehydrogenase (PDH)’” (xia2024quorumsensingregulationof pages 1-2) | Xia et al. 2024. DOI:10.1128/aac.00118-24 https://doi.org/10.1128/aac.00118-24 | Mechanistic downstream edge; relevant if connecting pigment to physiology. |
| exogenous pyruvate — partially_inhibits — pyocyanin-mediated effect | metabolite–predicate–process | CHEBI:15361 pyruvate; CHEBI:58410 pyocyanin | “the pyocyanin effect can be ‘partially inhibited by the addition of pyruvate to cultures’” (xia2024quorumsensingregulationof pages 1-2) | Xia et al. 2024. DOI:10.1128/aac.00118-24 https://doi.org/10.1128/aac.00118-24 | In study, pyruvate counteracts a pyocyanin-linked resistance phenotype; indirect inhibitor of pigment consequence rather than synthesis itself. |
| hppD — produces — homogentisate | gene/enzyme–predicate–metabolite | label: hppD 4-hydroxyphenylpyruvate dioxygenase; CHEBI:44747 homogentisate | “conversion of 4-hydroxyphenylpyruvate to HGA by HppD” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al. 2024. DOI:10.1128/spectrum.00410-24 https://doi.org/10.1128/spectrum.00410-24 | Strong enzymatic edge in pyomelanin pathway. |
| homogentisate — polymerizes_to_form — pyomelanin | metabolite–predicate–pigment | CHEBI:44747 homogentisate; label: pyomelanin | “HGA, excretion of HGA, spontaneous auto-oxidation… and polymerization to pyomelanin” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al. 2024. DOI:10.1128/spectrum.00410-24 https://doi.org/10.1128/spectrum.00410-24 | Good metabolite-to-pigment edge. |
| hmgA — prevents_accumulation_of — pyomelanin | gene/enzyme–predicate–pigment | label: hmgA homogentisate 1,2-dioxygenase; label: pyomelanin | “HmgA… normally converts HGA to maleylacetoacetate, preventing pigment accumulation” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al. 2024. DOI:10.1128/spectrum.00410-24 https://doi.org/10.1128/spectrum.00410-24 | Strong negative-control edge. |
| hmgA mutation Gly378Arg — causes — pyomelanin production phenotype | variant/gene–predicate–phenotype | label: hmgA Gly378Arg; label: pyomelanin production | “A point mutation in hmgA (Gly378→Arg) correlates with pigment production differences” (moustafa2024mutationofhmga pages 1-2) | Moustafa et al. 2024. DOI:10.1128/spectrum.00410-24 https://doi.org/10.1128/spectrum.00410-24 | Strain-specific causal claim from allelic comparison; curate with taxon note. |
| temperature 35 C — increases — nostoxanthin production | environment–predicate–phenotype/pathway | ENVO:01000206 temperature; label: nostoxanthin | “highest nostoxanthin concentration observed at 35 °C” (raman2024nostoxanthinbiosynthesisby pages 1-2) | Raman et al. 2024. DOI:10.1007/s00284-024-03956-7 https://doi.org/10.1007/s00284-024-03956-7 | Strong process edge; strain-specific. |
| pH 7.5 — increases — nostoxanthin production | environment–predicate–phenotype/pathway | label: pH 7.5; label: nostoxanthin | “produced most pigment at pH 7.5” (raman2024nostoxanthinbiosynthesisby pages 1-2) | Raman et al. 2024. DOI:10.1007/s00284-024-03956-7 https://doi.org/10.1007/s00284-024-03956-7 | Strong process edge; strain-specific. |
| dark incubation with glucose 40 g/L and yeast extract 5 g/L — results_in — nostoxanthin 217.22 plus or minus 9.60 mg/L | process/media–predicate–quantitative phenotype | label: dark incubation; label: glucose 40 g/L; label: yeast extract 5 g/L; label: nostoxanthin | “fed-batch fermentation yielded 217.22 ± 9.60 mg L−1 nostoxanthin” (raman2024nostoxanthinbiosynthesisby pages 1-2) | Raman et al. 2024. DOI:10.1007/s00284-024-03956-7 https://doi.org/10.1007/s00284-024-03956-7 | Very useful quantitative implementation edge. |
| low ZnO nanoparticle concentration 6.06 ug/mL at 32 C — increases — pyocyanin production | process/environment–predicate–phenotype | label: zinc oxide nanoparticle; CHEBI:58410 pyocyanin | “low ZnO NP concentration (6.06 µg/mL) combined with a temperature of 32°C enhanced pyocyanin production” (humme2024optimisedstress– pages 1-2) | Humme et al. 2024. DOI:10.1186/s12934-024-02486-y https://doi.org/10.1186/s12934-024-02486-y | Strong process-stimulation edge. |
| high ZnO nanoparticle concentration 275.75 ug/mL with higher temperature — abolishes — pyocyanin production | process/environment–predicate–phenotype | label: zinc oxide nanoparticle; CHEBI:58410 pyocyanin | “275.75 µg/mL and higher temperature increased biomass and abolished pyocyanin” (humme2024optimisedstress– pages 1-2) | Humme et al. 2024. DOI:10.1186/s12934-024-02486-y https://doi.org/10.1186/s12934-024-02486-y | Useful negative process edge; quantitative concentrations available. |


*Table: This table compiles evidence-backed candidate causal edges for curating the microbial trait pigmentation, covering scope boundaries, core biosynthetic pathways, regulatory systems, localization, and environmental/process determinants. It is useful as a starting point for building a TraitMech-style pigmentation causal graph with citations, grounding suggestions, and curation notes.*

### 4) Recent developments (prioritizing 2023–2024)
#### 4.1 Quorum sensing (QS) and pigment regulation; pigment delivery/transport
- **Violacein regulation + OMV delivery (Chromobacterium violaceum)**: 2024 evidence describes violacein synthesis as governed by the **vioABCDE operon** under control of the **CviI/CviR LuxI/LuxR-type QS circuit**, and links QS to **outer membrane vesicle (OMV)** secretion that can carry hydrophobic violacein (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence pages 3-5). Figure-level evidence explicitly depicts QS regulation of violacein production and OMV secretion (venkatramanan2024regulationofvirulence media e0035403). 
- **Phenazine/pyocyanin regulation (Pseudomonas aeruginosa)**: 2024 studies provide mechanistic regulatory structure: QS (Las/Rhl/PQS) regulates phenazine biosynthesis, and a specific histidine kinase **NahK** modulates pyocyanin production through PQS; deletion of nahK increases pyocyanin and alters QS system outputs (mendoza2024thehistidinekinase pages 14-16, xia2024quorumsensingregulationof pages 1-2, mendoza2024thehistidinekinase pages 2-5).

#### 4.2 Process intensification and engineered yield improvements
- **Nostoxanthin bioprocess optimization (2024)**: A Sphingomonas strain was optimized for nostoxanthin with explicit temperature/pH/media controls; fed-batch reached **217.22 ± 9.60 mg/L** nostoxanthin with reported selectivity and productivity, providing concrete quantitative process nodes/edges for pigmentation graphs when the pigment class is carotenoid/xanthophyll (raman2024nostoxanthinbiosynthesisby pages 1-2).
- **Prodigiosin process control (2024)**: A 2024 review synthesizes evidence that **temperature, pH, and oxygen transfer/OTR** strongly alter prodigiosin production; it also compiles strategies including oxygen limitation vs high-aeration regimes depending on system, and links high temperature to repression of pig cluster transcription via the sensor **CpxA** (lu2024prodigiosinunveilingthe pages 9-10).
- **Nanoparticle-triggered pigment modulation (2024)**: Sublethal ZnO nanoparticles can **increase pyocyanin** at a specific dose/temperature but **abolish** it at higher concentrations, illustrating an emerging class of “engineered stress” variables that can be modeled as environment/process nodes influencing pigmentation output (humme2024optimisedstress– pages 1-2, humme2024optimisedstress– pages 10-13).

### 5) Applications and real-world implementations
#### 5.1 Industrial sectors
Recent reviews consistently position microbial pigments as safer/greener alternatives to synthetic dyes for **food, pharmaceuticals/biomedicine, textiles, cosmetics**, and additional areas (agarwal2023bacterialpigmentsand pages 1-2, huang2024bacterialpigmentsas pages 1-2, agarwal2023bacterialpigmentsand pages 13-14). A 2024 review notes a broad pigment market projection (US$33.2–49.1B by 2027) and highlights fermentation-based manufacturing advantages and regulatory approvals for some microbially produced pigments (huang2024bacterialpigmentsas pages 1-2).

#### 5.2 Regulatory and commercialization signals
A 2024 review summarizes that only a limited set of microbial pigments have reached broad regulatory acceptance and notes examples of FDA-approved microbial pigments (e.g., riboflavin and certain carotenoids) in the broader “natural pigment” landscape (anshi2024unveilingtheintricacies pages 2-4, huang2024bacterialpigmentsas pages 1-2). 

#### 5.3 Biosensors and indicator applications
Microbial pigments are also used as **visible reporters** in whole-cell biosensors; pigments (including violacein/pyocyanin-derived readouts) can be quantified by spectrophotometry and used to report on signals or contaminants (e.g., AHL quorum signals; metal detection), supporting a practical “assay factor → pigment readout” linkage relevant to trait observation contexts (nemer2024seeingcolorsa pages 20-21).

### 6) Relevant recent statistics and quantitative data (examples)
- **Carotenoid market/production**: Carotenoids are widely used in foods/medications/cosmetics/feed, but a 2024 review reports that **~80–90%** of carotenoid synthesis remains chemical; it provides sector share estimates and multiple market projections for natural pigments (anshi2024unveilingtheintricacies pages 2-4). A 2023 review similarly estimates carotenoid market size and reports chemical vs plant vs microbial cost/price comparisons (agarwal2023bacterialpigmentsand pages 1-2).
- **Textile dye waste**: A 2024 review reports **1.3 million metric tons** of dyes produced annually with only **~15% used**, motivating interest in biodegradable microbial pigments as alternatives (anshi2024unveilingtheintricacies pages 2-4).
- **Quantitative pigment bioprocess outputs**: 
  - Nostoxanthin: **217.22 ± 9.60 mg/L** under optimized fed-batch conditions (raman2024nostoxanthinbiosynthesisby pages 1-2).
  - Prodigiosin: a bioreactor strategy yields **1066.2 mg in 24 h** and **36.1 mg/(L·h)** productivity (lu2024prodigiosinunveilingthe pages 9-10).

### 7) Warnings / claims not yet ready for general TraitMech curation
- **Taxon-specific regulatory edges**: QS→violacein→OMV edges are strongly supported in *Chromobacterium violaceum* but should be flagged as **taxon-specific** until validated in other violacein producers (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence media e0035403).
- **Conflicting oxygen effects in prodigiosin**: Evidence indicates oxygen transfer can either enhance or reduce prodigiosin depending on process context; this should be curated as **context-conditional** rather than a single universal edge (lu2024prodigiosinunveilingthe pages 9-10).
- **Nanoparticle effects**: NP→pigment edges (e.g., ZnO→pyocyanin changes) represent engineered stress responses and should be labeled **assay-/process-specific** (humme2024optimisedstress– pages 1-2).
- **Virulence assumptions**: Pyomelanin is often discussed as protective/virulence-associated, but a 2024 study indicates the pigment phenotype did not necessarily alter virulence in a specific Burkholderia model, cautioning against curating “pigment → virulence” as universal (moustafa2024mutationofhmga pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates where available)

1. Agarwal H, et al. **Bacterial Pigments and Their Multifaceted Roles in Contemporary Biotechnology and Pharmacological Applications.** *Microorganisms* (Feb 2023). DOI:10.3390/microorganisms11030614 https://doi.org/10.3390/microorganisms11030614 (agarwal2023bacterialpigmentsand pages 4-6, agarwal2023bacterialpigmentsand pages 2-4, agarwal2023bacterialpigmentsand pages 6-7, agarwal2023bacterialpigmentsand pages 1-2, agarwal2023bacterialpigmentsand pages 13-14)
2. de Oliveira Barreto JV, et al. **Microbial Pigments: Major Groups and Industrial Applications.** *Microorganisms* (Dec 2023). DOI:10.3390/microorganisms11122920 https://doi.org/10.3390/microorganisms11122920 (barreto2023microbialpigmentsmajor pages 4-6, barreto2023microbialpigmentsmajor pages 18-19, barreto2023microbialpigmentsmajor pages 12-15, barreto2023microbialpigmentsmajor pages 10-12, barreto2023microbialpigmentsmajor pages 1-2)
3. Huang X, et al. **Bacterial Pigments as a Promising Alternative to Synthetic Colorants: From Fundamentals to Applications.** *Journal of Microbiology and Biotechnology* (Sep 2024). DOI:10.4014/jmb.2404.04018 https://doi.org/10.4014/jmb.2404.04018 (huang2024bacterialpigmentsas pages 13-13, huang2024bacterialpigmentsas pages 9-10, huang2024bacterialpigmentsas pages 3-4, huang2024bacterialpigmentsas pages 1-2)
4. Venkatramanan M, Nalini E. **Regulation of virulence in Chromobacterium violaceum and strategies to combat it.** *Frontiers in Microbiology* (Jan 2024). DOI:10.3389/fmicb.2024.1303595 https://doi.org/10.3389/fmicb.2024.1303595 (venkatramanan2024regulationofvirulence pages 5-7, venkatramanan2024regulationofvirulence pages 3-5, venkatramanan2024regulationofvirulence pages 2-3, venkatramanan2024regulationofvirulence media e0035403)
5. Mendoza AG, et al. **The histidine kinase NahK regulates pyocyanin production through the PQS system.** *Journal of Bacteriology* (Jan 2024). DOI:10.1128/jb.00276-23 https://doi.org/10.1128/jb.00276-23 (mendoza2024thehistidinekinase pages 14-16, mendoza2024thehistidinekinase pages 2-5)
6. Xia L, et al. **Quorum-sensing regulation of phenazine production heightens Pseudomonas aeruginosa resistance to ciprofloxacin.** *Antimicrobial Agents and Chemotherapy* (May 2024). DOI:10.1128/aac.00118-24 https://doi.org/10.1128/aac.00118-24 (xia2024quorumsensingregulationof pages 1-2)
7. Lu Y, et al. **Prodigiosin: unveiling the crimson wonder – a comprehensive journey from diverse bioactivity to synthesis and yield enhancement.** *Frontiers in Microbiology* (Jun 2024). DOI:10.3389/fmicb.2024.1412776 https://doi.org/10.3389/fmicb.2024.1412776 (lu2024prodigiosinunveilingthe pages 9-10)
8. Pereira RFS, de Carvalho CCCR. **Mimicking Marine Conditions to Improve Prodigiosin Yields in Bioreactor.** *Processes* (Aug 2024). DOI:10.3390/pr12091794 https://doi.org/10.3390/pr12091794 (lu2024prodigiosinunveilingthe pages 9-10)
9. Raman J, et al. **Nostoxanthin Biosynthesis by Sphingomonas Species (COS14-R2): Isolation, Identification, and Optimization of Culture Conditions.** *Current Microbiology* (Nov 2024). DOI:10.1007/s00284-024-03956-7 https://doi.org/10.1007/s00284-024-03956-7 (raman2024nostoxanthinbiosynthesisby pages 1-2)
10. Humme JH, et al. **Optimised stress – intensification of pyocyanin production with zinc oxide nanoparticles.** *Microbial Cell Factories* (Jul 2024). DOI:10.1186/s12934-024-02486-y https://doi.org/10.1186/s12934-024-02486-y (humme2024optimisedstress– pages 1-2, humme2024optimisedstress– pages 10-13)
11. Moustafa DA, et al. **Mutation of hmgA… is responsible for pyomelanin production…** *Microbiology Spectrum* (Jul 2024). DOI:10.1128/spectrum.00410-24 https://doi.org/10.1128/spectrum.00410-24 (moustafa2024mutationofhmga pages 1-2)
12. Nemer G, et al. **Seeing Colors: A Literature Review on Colorimetric Whole-Cell Biosensors.** *Fermentation* (Jan 2024). DOI:10.3390/fermentation10020079 https://doi.org/10.3390/fermentation10020079 (nemer2024seeingcolorsa pages 20-21)
13. Anshi, et al. **Unveiling the Intricacies of Microbial Pigments as Sustainable Alternatives to Synthetic Colorants: Recent Trends and Advancements.** *Micro* (Oct 2024). DOI:10.3390/micro4040038 https://doi.org/10.3390/micro4040038 (anshi2024unveilingtheintricacies pages 4-5, anshi2024unveilingtheintricacies pages 2-4, anshi2024unveilingtheintricacies pages 13-14, anshi2024unveilingtheintricacies pages 7-8)
14. Kiki MJ. **Biopigments of Microbial Origin and Their Application in the Cosmetic Industry.** *Cosmetics* (Mar 2023). DOI:10.3390/cosmetics10020047 https://doi.org/10.3390/cosmetics10020047 (kiki2023biopigmentsofmicrobial pages 2-4)

---

## Figure evidence used
- Figure 2 schematic of **CviI/CviR quorum sensing regulating violacein and OMV secretion** (venkatramanan2024regulationofvirulence media e0035403).


References

1. (agarwal2023bacterialpigmentsand pages 2-4): Himani Agarwal, Sneh Bajpai, Arti Mishra, Isha Kohli, Ajit Varma, Mireille Fouillaud, Laurent Dufossé, and Naveen Chandra Joshi. Bacterial pigments and their multifaceted roles in contemporary biotechnology and pharmacological applications. Microorganisms, 11:614, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030614, doi:10.3390/microorganisms11030614. This article has 118 citations.

2. (agarwal2023bacterialpigmentsand pages 4-6): Himani Agarwal, Sneh Bajpai, Arti Mishra, Isha Kohli, Ajit Varma, Mireille Fouillaud, Laurent Dufossé, and Naveen Chandra Joshi. Bacterial pigments and their multifaceted roles in contemporary biotechnology and pharmacological applications. Microorganisms, 11:614, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030614, doi:10.3390/microorganisms11030614. This article has 118 citations.

3. (barreto2023microbialpigmentsmajor pages 1-2): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

4. (barreto2023microbialpigmentsmajor pages 4-6): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

5. (agarwal2023bacterialpigmentsand pages 6-7): Himani Agarwal, Sneh Bajpai, Arti Mishra, Isha Kohli, Ajit Varma, Mireille Fouillaud, Laurent Dufossé, and Naveen Chandra Joshi. Bacterial pigments and their multifaceted roles in contemporary biotechnology and pharmacological applications. Microorganisms, 11:614, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030614, doi:10.3390/microorganisms11030614. This article has 118 citations.

6. (huang2024bacterialpigmentsas pages 1-2): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 31 citations and is from a peer-reviewed journal.

7. (raman2024nostoxanthinbiosynthesisby pages 1-2): Jegadeesh Raman, Jeong-Seon Kim, Young-Joon Ko, and Soo-Jin Kim. Nostoxanthin biosynthesis by sphingomonas species (cos14-r2): isolation, identification, and optimization of culture conditions. Current Microbiology, Nov 2024. URL: https://doi.org/10.1007/s00284-024-03956-7, doi:10.1007/s00284-024-03956-7. This article has 4 citations and is from a peer-reviewed journal.

8. (venkatramanan2024regulationofvirulence pages 5-7): Mahendrarajan Venkatramanan and Easwaran Nalini. Regulation of virulence in chromobacterium violaceum and strategies to combat it. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1303595, doi:10.3389/fmicb.2024.1303595. This article has 40 citations and is from a peer-reviewed journal.

9. (lu2024prodigiosinunveilingthe pages 9-10): Yonglin Lu, Derun Liu, Renhui Jiang, Ziyun Li, and Xueyan Gao. Prodigiosin: unveiling the crimson wonder – a comprehensive journey from diverse bioactivity to synthesis and yield enhancement. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1412776, doi:10.3389/fmicb.2024.1412776. This article has 28 citations and is from a peer-reviewed journal.

10. (barreto2023microbialpigmentsmajor pages 10-12): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

11. (barreto2023microbialpigmentsmajor pages 12-15): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

12. (xia2024quorumsensingregulationof pages 1-2): Lexin Xia, Yue Li, Yufan Wang, Hui Zhou, Ajai A. Dandekar, Meizhen Wang, and Feng Xu. Quorum-sensing regulation of phenazine production heightens <i>pseudomonas aeruginosa</i> resistance to ciprofloxacin. Antimicrobial Agents and Chemotherapy, May 2024. URL: https://doi.org/10.1128/aac.00118-24, doi:10.1128/aac.00118-24. This article has 16 citations and is from a highest quality peer-reviewed journal.

13. (mendoza2024thehistidinekinase pages 2-5): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

14. (moustafa2024mutationofhmga pages 1-2): Dina A. Moustafa, Linda Wu, Melissa Ivey, Sarah C. Fankhauser, and Joanna B. Goldberg. Mutation of <i>hmga</i> , encoding homogentisate 1,2-dioxygenase, is responsible for pyomelanin production but does not impact the virulence of <i>burkholderia cenocepacia</i> in a chronic granulomatous disease mouse lung infection. Jul 2024. URL: https://doi.org/10.1128/spectrum.00410-24, doi:10.1128/spectrum.00410-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

15. (huang2024bacterialpigmentsas pages 3-4): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 31 citations and is from a peer-reviewed journal.

16. (venkatramanan2024regulationofvirulence pages 3-5): Mahendrarajan Venkatramanan and Easwaran Nalini. Regulation of virulence in chromobacterium violaceum and strategies to combat it. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1303595, doi:10.3389/fmicb.2024.1303595. This article has 40 citations and is from a peer-reviewed journal.

17. (venkatramanan2024regulationofvirulence media e0035403): Mahendrarajan Venkatramanan and Easwaran Nalini. Regulation of virulence in chromobacterium violaceum and strategies to combat it. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1303595, doi:10.3389/fmicb.2024.1303595. This article has 40 citations and is from a peer-reviewed journal.

18. (humme2024optimisedstress– pages 10-13): Joanna Honselmann genannt Humme, Kamila Dubrowska, Bartłomiej Grygorcewicz, Marta Gliźniewicz, Oliwia Paszkiewicz, Anna Głowacka, Daniel Musik, Grzegorz Story, Rafał Rakoczy, and Adrian Augustyniak. Optimised stress – intensification of pyocyanin production with zinc oxide nanoparticles. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02486-y, doi:10.1186/s12934-024-02486-y. This article has 10 citations and is from a peer-reviewed journal.

19. (mendoza2024thehistidinekinase pages 14-16): Alicia G. Mendoza, Danielle Guercio, Marina K. Smiley, Gaurav K. Sharma, Jason M. Withorn, Natalie V. Hudson-Smith, Chika Ndukwe, Lars E. P. Dietrich, and Elizabeth M. Boon. The histidine kinase nahk regulates pyocyanin production through the pqs system. Journal of Bacteriology, Jan 2024. URL: https://doi.org/10.1128/jb.00276-23, doi:10.1128/jb.00276-23. This article has 12 citations and is from a peer-reviewed journal.

20. (humme2024optimisedstress– pages 1-2): Joanna Honselmann genannt Humme, Kamila Dubrowska, Bartłomiej Grygorcewicz, Marta Gliźniewicz, Oliwia Paszkiewicz, Anna Głowacka, Daniel Musik, Grzegorz Story, Rafał Rakoczy, and Adrian Augustyniak. Optimised stress – intensification of pyocyanin production with zinc oxide nanoparticles. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02486-y, doi:10.1186/s12934-024-02486-y. This article has 10 citations and is from a peer-reviewed journal.

21. (elzawawy2024bioproductionandoptimization pages 2-4): Nessma A. El-Zawawy, El-Refaie Kenawy, Sara Ahmed, and Shimaa El-Sapagh. Bioproduction and optimization of newly characterized melanin pigment from streptomyces djakartensis nss-3 with its anticancer, antimicrobial, and radioprotective properties. Microbial Cell Factories, Jan 2024. URL: https://doi.org/10.1186/s12934-023-02276-y, doi:10.1186/s12934-023-02276-y. This article has 47 citations and is from a peer-reviewed journal.

22. (huang2024bacterialpigmentsas pages 9-10): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 31 citations and is from a peer-reviewed journal.

23. (jabłonska2023thetwofaces pages 6-7): Joanna Jabłońska, Adrian Augustyniak, Kamila Dubrowska, and Rafał Rakoczy. The two faces of pyocyanin - why and how to steer its production? World Journal of Microbiology & Biotechnology, Feb 2023. URL: https://doi.org/10.1007/s11274-023-03548-w, doi:10.1007/s11274-023-03548-w. This article has 48 citations and is from a peer-reviewed journal.

24. (kiki2023biopigmentsofmicrobial pages 2-4): Manal Jameel Kiki. Biopigments of microbial origin and their application in the cosmetic industry. Cosmetics, 10:47, Mar 2023. URL: https://doi.org/10.3390/cosmetics10020047, doi:10.3390/cosmetics10020047. This article has 85 citations.

25. (agarwal2023bacterialpigmentsand pages 1-2): Himani Agarwal, Sneh Bajpai, Arti Mishra, Isha Kohli, Ajit Varma, Mireille Fouillaud, Laurent Dufossé, and Naveen Chandra Joshi. Bacterial pigments and their multifaceted roles in contemporary biotechnology and pharmacological applications. Microorganisms, 11:614, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030614, doi:10.3390/microorganisms11030614. This article has 118 citations.

26. (agarwal2023bacterialpigmentsand pages 13-14): Himani Agarwal, Sneh Bajpai, Arti Mishra, Isha Kohli, Ajit Varma, Mireille Fouillaud, Laurent Dufossé, and Naveen Chandra Joshi. Bacterial pigments and their multifaceted roles in contemporary biotechnology and pharmacological applications. Microorganisms, 11:614, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030614, doi:10.3390/microorganisms11030614. This article has 118 citations.

27. (anshi2024unveilingtheintricacies pages 2-4): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 17 citations.

28. (nemer2024seeingcolorsa pages 20-21): Georgio Nemer, Mohamed Koubaa, Laure El Chamy, Richard G. Maroun, and Nicolas Louka. Seeing colors: a literature review on colorimetric whole-cell biosensors. Fermentation, 10:79, Jan 2024. URL: https://doi.org/10.3390/fermentation10020079, doi:10.3390/fermentation10020079. This article has 13 citations.

29. (barreto2023microbialpigmentsmajor pages 18-19): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

30. (huang2024bacterialpigmentsas pages 13-13): Xin Huang, Longzhan Gan, Zhicheng He, Guangyang Jiang, and Tengxia He. Bacterial pigments as a promising alternative to synthetic colorants: from fundamentals to applications. Journal of Microbiology and Biotechnology, 34:2153-2165, Sep 2024. URL: https://doi.org/10.4014/jmb.2404.04018, doi:10.4014/jmb.2404.04018. This article has 31 citations and is from a peer-reviewed journal.

31. (venkatramanan2024regulationofvirulence pages 2-3): Mahendrarajan Venkatramanan and Easwaran Nalini. Regulation of virulence in chromobacterium violaceum and strategies to combat it. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1303595, doi:10.3389/fmicb.2024.1303595. This article has 40 citations and is from a peer-reviewed journal.

32. (anshi2024unveilingtheintricacies pages 4-5): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 17 citations.

33. (anshi2024unveilingtheintricacies pages 13-14): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 17 citations.

34. (anshi2024unveilingtheintricacies pages 7-8): Anshi, Shikha Kapil, Lalit Goswami, and Vipasha Sharma. Unveiling the intricacies of microbial pigments as sustainable alternatives to synthetic colorants: recent trends and advancements. Micro, 4:621-640, Oct 2024. URL: https://doi.org/10.3390/micro4040038, doi:10.3390/micro4040038. This article has 17 citations.