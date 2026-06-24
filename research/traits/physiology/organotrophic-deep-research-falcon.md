---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:00:18.760152'
end_time: '2026-06-18T12:17:02.916316'
duration_seconds: 1004.16
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: organotrophic
  trait_identifier: METPO:1000655
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: organotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from the oxidation
    of organic compounds.
  parent_traits: METPO:1000631
  synonyms: TT_organotroph, organotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound
    into biomass (Microbial metabolism reference supports assimilation and use of
    organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound
    electron transport chain (Review supports respiratory electron transport as an
    energy-conserving route.)'
  causal_graph_summary: 'organotrophic_organic_compound_oxidation: 8 nodes, 7 edges'
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
- **Trait label:** organotrophic
- **METPO identifier:** METPO:1000655
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_organotroph, organotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound into biomass (Microbial metabolism reference supports assimilation and use of organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory electron transport as an energy-conserving route.)
- **Existing causal graph summary:** organotrophic_organic_compound_oxidation: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **organotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organotrophic.yaml`.

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
- **Trait label:** organotrophic
- **METPO identifier:** METPO:1000655
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_organotroph, organotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: incorporation of a compound into biomass (Microbial metabolism reference supports assimilation and use of organic compounds in growth.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory electron transport as an energy-conserving route.)
- **Existing causal graph summary:** organotrophic_organic_compound_oxidation: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **organotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **organotrophic** (METPO:1000655)

### 1) Scope summary (trait meaning, boundaries, nearby traits)

**Trait definition (curation target).** *Organotrophic* organisms obtain energy by **oxidation of organic compounds** (electron donors are organic molecules), consistent with the METPO definition provided by the user. In the retrieved recent literature, organotrophy is operationalized ecologically as a strategy favored by **high organic carbon / dissolved organic carbon (DOC)** availability: enriched organic C/DOC “support[s] the rapid propagation of obligate organotrophic copiotrophs,” and increased organic C availability shifts communities “from oligotrophic trace gas oxidizers to copiotrophic organotroph.” (li2023reducedtracegas pages 7-8)

**Boundary cases and distinctions.**
- **Organotrophy vs lithotrophy (inferred boundary):** Li et al. frame microbial energy strategies as a shift “between organic compounds and inorganic trace gases” (H2, CO). Under carbon limitation, “organoheterotrophic isolates upregulate hydrogenase and CO dehydrogenase expression to obtain alternative energy,” implying facultative use of inorganic electron donors despite an organoheterotrophic baseline. (li2023reducedtracegas pages 1-2)
- **Copiotroph vs oligotroph (ecological correlates):** in the desert-soil study, organic-C enrichment favors “organotrophic copiotrophs,” while low-organic-carbon conditions favor trace-gas oxidizers, highlighting that organotrophy is not a single pathway but a **resource-linked life-history strategy** in situ. (li2023reducedtracegas pages 7-8, li2023reducedtracegas pages 1-2)
- **Trait is not equivalent to carbon-source class (heterotrophy/autotrophy):** the present evidence set is stronger on energy acquisition (electron donor oxidation, respiration) than on carbon assimilation categories; however, it explicitly links organoheterotrophs to shifts in energy acquisition when organic C is depleted. (li2023reducedtracegas pages 1-2)

**What this trait should represent in TraitMech.** For a TraitMech causal graph, *organotrophic* is best treated as a **physiological capacity**: the ability to conserve energy from oxidation of organic compounds via respiratory/fermentative redox metabolism; in curated edges below, the focus is on **organic substrate oxidation → reducing equivalents (NADH/FADH2) → electron transport chain (ETC) / redox systems → proton motive force (PMF) → ATP synthesis**, plus environmental modulators (organic C, oxygen, cofactors, inhibitors). (giordano2024nitricoxideand pages 8-13, yamamoto2024rolesofflavoprotein pages 3-5, garimella2024fromcellsto pages 1-2)


### 2) Candidate mechanistic entities (nodes), grouped by type

The following node candidates are directly supported by the retrieved sources and are intended for curation into `organotrophic.yaml`.

| Node label | Node type | Suggested ontology grounding | Evidence support | Notes |
|---|---|---|---|---|
| organotrophy | process | METPO:1000655 | (li2023reducedtracegas pages 7-8, li2023reducedtracegas pages 1-2) | Trait of obtaining energy from oxidation of organic compounds; community-level support in current corpus. |
| oxidation of organic compounds | process | GO candidate: oxidation-reduction process (GO:0055114) | (li2023reducedtracegas pages 2-3, garimella2024fromcellsto pages 1-2) | Central mechanistic process feeding reducing equivalents into ETC. |
| carbohydrate utilization | process | label only | (li2023reducedtracegas pages 8-9, li2023reducedtracegas pages 2-3) | Used in Li et al. as marker of organotrophic strategy. |
| aerobic respiration | process | GO:0009060 | (yamamoto2024rolesofflavoprotein pages 3-5, giordano2024nitricoxideand pages 8-13) | Canonical organotrophic energy-conserving route with O2 as terminal acceptor. |
| electron transport chain | process | GO:0022900 | (yamamoto2024rolesofflavoprotein pages 3-5, garimella2024fromcellsto pages 1-2) | Conserved respiratory chain linking substrate oxidation to PMF. |
| oxidative phosphorylation | process | GO:0006119 | (garimella2024fromcellsto pages 1-2, giordano2024nitricoxideand pages 8-13) | ATP generation using ETC-derived electrochemical gradient. |
| proton motive force | process | GO candidate: proton motive force-driven ATP synthesis (GO:0015986) | (garimella2024fromcellsto pages 1-2, giordano2024nitricoxideand pages 8-13) | Energetic intermediate generated by some respiratory complexes. |
| proton transmembrane transport | process | GO:1902600 | (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 8-13) | Mechanistic step underlying PMF generation. |
| ATP synthesis by ATP synthase | process | GO:0015986 | (garimella2024fromcellsto pages 1-2, giordano2024nitricoxideand pages 8-13) | Downstream consequence of PMF in organotrophic respiration. |
| carbohydrates | metabolite | CHEBI candidate: carbohydrate (class) | (li2023reducedtracegas pages 8-9, li2023reducedtracegas pages 2-3) | Generic organic substrates associated with organotrophic copiotrophs. |
| lactate | metabolite | CHEBI:24996 | (yamamoto2024rolesofflavoprotein pages 3-5, gonzalezmontalvo2024therespiratorychain pages 1-2) | Fermentation/respiration-linked metabolite; dehydrogenase activity increases in some conditions. |
| pyruvate | metabolite | CHEBI:15361 | (yamamoto2024rolesofflavoprotein pages 3-5) | Central product/intermediate in organotrophic metabolism. |
| acetate | metabolite | CHEBI:30089 | (yamamoto2024rolesofflavoprotein pages 3-5, uriberamirez2024modificationsofthe pages 11-12) | Carbon source affecting terminal oxidase usage in B. licheniformis. |
| succinate | metabolite | CHEBI:30031 | (giordano2024nitricoxideand pages 8-13, uriberamirez2024modificationsofthe pages 1-2) | Organic electron donor feeding Complex II/SDH. |
| NADH | metabolite | CHEBI:57945 | (garimella2024fromcellsto pages 1-2, giordano2024nitricoxideand pages 8-13) | Major reduced electron carrier from organic catabolism. |
| FADH2 | metabolite | CHEBI candidate: FADH2 | (garimella2024fromcellsto pages 1-2, giordano2024nitricoxideand pages 8-13) | Reduced carrier from substrate oxidation; grounding may require verification. |
| quinone pool | metabolite | label only | (garimella2024fromcellsto pages 4-6, giordano2024nitricoxideand pages 8-13) | Mobile membrane electron carrier pool linking dehydrogenases to downstream oxidases. |
| ubiquinone | metabolite/cofactor | CHEBI:16389 | (gonzalezmontalvo2024therespiratorychain pages 13-13, giordano2024nitricoxideand pages 1-8) | Respiratory quinone in some bacteria. |
| ubiquinol | metabolite/cofactor | CHEBI:17976 | (gonzalezmontalvo2024therespiratorychain pages 13-13, garimella2024fromcellsto pages 4-6) | Reduced quinone donating electrons downstream. |
| menaquinone | metabolite/cofactor | CHEBI:18067 | (yamamoto2024rolesofflavoprotein pages 3-5, garimella2024fromcellsto pages 4-6) | Respiratory quinone especially highlighted in LAB. |
| oxygen | metabolite/electron acceptor | CHEBI:15379 | (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 8-13) | Major terminal electron acceptor in aerobic organotrophy. |
| nitrate | metabolite/electron acceptor | CHEBI:17632 | (uriberamirez2024modificationsofthe pages 1-2, gonzalezmontalvo2024therespiratorychain pages 13-14) | Alternative respiratory electron acceptor in some taxa. |
| heme | cofactor | CHEBI:30413 | (yamamoto2024rolesofflavoprotein pages 3-5) | Required exogenously for respiration in many LAB. |
| cyanide | inhibitor/environmental factor | CHEBI:17514 | (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | Inhibits cytochrome oxidases; selects for resistant branches. |
| antimycin A | inhibitor | CHEBI:135783 | (uriberamirez2024modificationsofthe pages 11-12) | Used as inhibitor probe for bc-caa3 activity; condition-specific evidence. |
| NDH-1 (type I NADH dehydrogenase) | protein complex | EC candidate: 7.1.1.2 | (giordano2024nitricoxideand pages 8-13) | Proton-pumping NADH:quinone oxidoreductase. |
| NDH-2 (type II NADH dehydrogenase) | protein complex | EC candidate: 1.6.5.11 | (gonzalezmontalvo2024therespiratorychain pages 1-2, yamamoto2024rolesofflavoprotein pages 3-5, uriberamirez2024modificationsofthe pages 1-2) | Non-proton-pumping NADH dehydrogenase common in many bacteria. |
| succinate dehydrogenase (Complex II) | protein complex | EC:1.3.5.1 | (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 8-13) | Oxidizes succinate and reduces quinone. |
| NQR / nitrate reductase-linked complex | protein complex | label only | (gonzalezmontalvo2024therespiratorychain pages 13-13, uriberamirez2024modificationsofthe pages 11-12) | Evidence mixes Na+-pumping NADH:quinone oxidoreductase and quinone-linked nitrate reductase contexts; curate carefully. |
| Complex III / cytochrome bc1 | protein complex | EC:7.1.1.8 | (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 8-13) | Transfers electrons from quinol to cytochrome c and contributes to PMF. |
| cytochrome c | protein/metabolite carrier | UniProt/GO candidate; label only | (uriberamirez2024modificationsofthe pages 1-2, giordano2024nitricoxideand pages 8-13) | Mobile/peripheral electron carrier between Complex III and some terminal oxidases. |
| ATP synthase (FOF1-ATP synthase) | protein complex | EC:7.1.2.2 | (garimella2024fromcellsto pages 1-2, giordano2024nitricoxideand pages 8-13) | Uses electrochemical gradient to produce ATP. |
| aa3 oxidase | protein complex | label only | (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | Terminal oxidase detected in B. licheniformis; cyanide-sensitive. |
| caa3 oxidase | protein complex | label only | (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | Terminal oxidase linked with bc-caa3 branch in Bacillus. |
| bo3 oxidase | protein complex | label only | (gonzalezmontalvo2024therespiratorychain pages 13-13, gonzalezmontalvo2024therespiratorychain pages 13-14) | Quinol oxidase noted in K. aerogenes respiratory-chain context. |
| bd-type oxidase | protein complex | label only | (gonzalezmontalvo2024therespiratorychain pages 1-2, yamamoto2024rolesofflavoprotein pages 3-5, uriberamirez2024modificationsofthe pages 11-12) | Common terminal oxidase; often stress tolerant and high O2 affinity. |
| heme-copper oxidase | protein complex | GO/EC candidate; label only | (giordano2024nitricoxideand pages 8-13) | Family-level terminal oxidases contributing to proton pumping. |
| cytochrome bc-caa3 supercomplex | protein complex | label only | (uriberamirez2024modificationsofthe pages 11-12) | Taxon-specific Bacillus respiratory supercomplex. |
| high organic carbon / dissolved organic carbon | environmental factor | label only | (li2023reducedtracegas pages 7-8, li2023reducedtracegas pages 1-2) | Enriches organotrophic copiotrophs. |
| low oxygen environment | environmental factor | ENVO candidate: hypoxic environment | (giordano2024nitricoxideand pages 8-13) | Drives oxidase choice and respiratory adaptation. |
| urine-like medium | environmental factor/assay | label only | (gonzalezmontalvo2024therespiratorychain pages 1-2, gonzalezmontalvo2024therespiratorychain pages 13-13) | Condition used to profile K. aerogenes respiratory chain. |
| alkaline medium | environmental factor/assay | ENVO candidate: alkaline environment | (uriberamirez2024modificationsofthe pages 1-2) | Experimental condition affecting B. licheniformis growth and respiration. |
| exogenous heme supplementation | assay/environmental factor | label only | (yamamoto2024rolesofflavoprotein pages 3-5) | Enables respiratory metabolism in LAB lacking heme biosynthesis. |
| oxygen consumption assay | assay | label only | (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | Functional assay for respiratory activity under different conditions. |
| BN-PAGE / proteomic complex profiling | assay | label only | (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | Used to identify respiratory complexes and supercomplexes. |
| soil microbial fuel cell | application | label only | (zhao2023keygenesof pages 1-2, garimella2024fromcellsto pages 1-2) | Real-world/bioengineering system exploiting microbial organotrophic electron flow. |


*Table: This table lists candidate nodes for a causal graph of the organotrophic trait, spanning metabolic processes, metabolites, respiratory complexes, environmental drivers, assays, and applications. It is useful for selecting curation-ready entities and identifying where ontology grounding is clear versus where label-only nodes are safer.*


### 3) Evidence-backed candidate causal edges (triples)

The following edges are proposed as **subject—predicate—object** triples with supporting snippets. They include both **core mechanistic edges** (respiration bioenergetics) and **contextual edges** (environmental drivers, inhibitors, applied systems).

| Edge (subject—predicate—object) | Node type(s) | Suggested grounding | Evidence snippet | Reference (DOI + URL + publication date) | Notes/uncertainty |
|---|---|---|---|---|---|
| organic carbon availability — increases abundance of — organotrophic copiotrophs | environmental factor → phenotype/community state | label only; ENVO candidate for soil organic carbon not asserted | “Enriched organic C and dissolved organic C can support the rapid propagation of obligate organotrophic copiotrophs” (li2023reducedtracegas pages 7-8) | Li et al. 2023, doi:10.1038/s41396-023-01437-6, https://doi.org/10.1038/s41396-023-01437-6, May 2023 | Strong ecological support for organotroph enrichment; community-level rather than single-cell mechanistic edge. |
| organic carbon availability — shifts community toward — copiotrophic organotrophs | environmental factor → phenotype/community state | label only | “shifted the dominant taxa... from oligotrophic trace gas oxidizers to copiotrophic organotroph” (li2023reducedtracegas pages 7-8) | Li et al. 2023, doi:10.1038/s41396-023-01437-6, https://doi.org/10.1038/s41396-023-01437-6, May 2023 | Good for trait scope/boundary; inferred at community level. |
| oxidation of organic substrates — generates — NADH and FADH2 | biological process → chemical | GO candidate: oxidative phosphorylation / electron transport chain; CHEBI:NADH, CHEBI:FADH2 | “Catabolic pathways (Krebs cycle and β-oxidation) generate reduced carriers (NADH and FADH2)” (garimella2024fromcellsto pages 1-2) | Garimella et al. 2024, doi:10.1186/s13213-024-01761-y, https://doi.org/10.1186/s13213-024-01761-y, Jun 2024 | General bioenergetic edge; not bacteria-exclusive in quote, but presented as conserved with bacterial systems. |
| NADH — donates electrons to — NADH dehydrogenase / Complex I | chemical → enzyme complex | CHEBI:NADH; GO:0008137? label: NADH dehydrogenase (Complex I) | “NADH dehydrogenase (Complex I) extracts hydrogen/electrons” (garimella2024fromcellsto pages 2-4) | Garimella et al. 2024, doi:10.1186/s13213-024-01761-y, https://doi.org/10.1186/s13213-024-01761-y, Jun 2024 | Broad canonical edge; grounding for enzyme complex should be refined during curation. |
| NDH-1 — transfers electrons from — NADH to quinone | enzyme complex → chemicals | label: NDH-1; CHEBI:NADH; CHEBI:quinone | “NDH-1 transfers electrons from NADH to quinone” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Mechanistically explicit; source excerpt lacks full bibliographic metadata. |
| NDH-1 — generates — proton motive force | enzyme complex → process | label: NDH-1; GO:0015986 proton motive force-driven ATP synthesis or GO proton transmembrane transport candidate | “NDH-1 transfers electrons from NADH to quinone while ‘pumping four electrons to generate PMF’” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Strong mechanistic edge; verify exact stoichiometric wording in source before formal curation. |
| NDH-2 — transfers electrons from — NADH to quinone | enzyme complex → chemicals | label: NDH-2; CHEBI:NADH; CHEBI:quinone | “NDH-2 transfers electrons to quinone” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Canonical mechanistic edge. |
| NDH-2 — does not generate — proton motive force | enzyme complex → process | label: NDH-2; GO candidate: proton motive force generation | “NDH-2 transfers electrons to quinone ‘without generating PMF’” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Useful negative edge/constraint for graph logic. |
| succinate dehydrogenase — transfers electrons from — succinate to quinone | enzyme complex → chemicals | EC/Complex II candidate; CHEBI:succinate; CHEBI:quinone | “Complex II reduces quinone from succinate oxidation” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Canonical respiratory edge. |
| succinate dehydrogenase — contributes to — proton motive force generation | enzyme complex → process | label: succinate dehydrogenase; GO candidate: electron transport chain | “Succinate dehydrogenase (SDH) is described as ‘electrogenic, proton-motive force generating’” (uriberamirez2024modificationsofthe pages 1-2) | Uribe-Ramírez et al. 2024, doi:10.1007/s10863-024-10041-y, https://doi.org/10.1007/s10863-024-10041-y, Nov 2024 | Taxon-specific wording from B. licheniformis paper; broader applicability should be checked. |
| reduced quinone pool — donates electrons to — Complex III / cytochrome bc1 | chemical pool → enzyme complex | CHEBI:quinol; label: Complex III / cytochrome bc1 | “The reduced quinone pool donates electrons to Complex III” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Strong canonical edge. |
| Complex III / cytochrome bc1 — generates — proton motive force | enzyme complex → process | label: Complex III / cytochrome bc1; GO candidate: proton transmembrane transport | “Complex III... ‘transfers electrons from the quinone pool to cytochrome c, generating PMF’” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Strong mechanistic edge. |
| terminal oxidase / Complex IV — reduces — oxygen to water | enzyme complex → chemicals | GO:0004129 cytochrome-c oxidase activity candidate; CHEBI:oxygen; CHEBI:water | “terminal oxidases... shuttle electrons to O2, ‘which is eventually reduced into water’” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Canonical and central to aerobic organotrophy. |
| terminal oxidase activity — helps generate — electrochemical proton gradient | enzyme complex/process → process | GO candidate: aerobic respiration; proton transmembrane transport | “this terminal reduction ‘helps generate the electrochemical gradient for ATP synthesis’” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Strong mechanistic edge; applicable to aerobic branches. |
| proton gradient / PMF — powers — ATP synthase | process → enzyme complex | GO:0015986; label: FOF1-ATP synthase | “ATP synthase uses this electrochemical gradient” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Core energy-conservation edge. |
| ATP synthase — synthesizes — ATP | enzyme complex → chemical | GO:0016887 ATP hydrolysis activity not exact; label: ATP synthase; CHEBI:ATP | “ATP synthase uses this electrochemical gradient to convert ADP + Pi into ATP” (giordano2024nitricoxideand pages 8-13) | Giordano 2024 excerpt, no DOI available, publication date not available | Strong canonical edge; ATP CHEBI can be added during formal curation. |
| exogenous heme — enables — respiratory metabolism in LAB | nutrient/cofactor → phenotype/process | CHEBI:heme; label: lactic acid bacteria respiration | “LAB lack endogenous heme synthesis and therefore cannot perform respiration unless an exogenous heme source is supplied” (yamamoto2024rolesofflavoprotein pages 3-5) | Yamamoto 2024, doi:10.12938/bmfh.2024-002, https://doi.org/10.12938/bmfh.2024-002, May 2024 | Strong but taxon-specific; applies to heme-auxotrophic LAB, not all bacteria. |
| cyanide — inhibits — cytochrome c oxidase / aa3 oxidase activity | inhibitor → enzyme complex/process | CHEBI:cyanide; label: cytochrome c oxidase / aa3 oxidase | “cyanide normally inhibits cytochrome c oxidase” and “Cyanide exposure... caused a large (≈90%) reduction in respiratory activity by inhibiting the aa3 oxidase” (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12) | Uribe-Ramírez et al. 2024, doi:10.1007/s10863-024-10041-y, https://doi.org/10.1007/s10863-024-10041-y, Nov 2024 | Strong inhibitor edge; aa3-specific effect shown in B. licheniformis. |
| branched respiratory chain / alternative terminal oxidases — enables respiration in presence of — cyanide | pathway architecture → environmental tolerance | label only | “can also carry out aerobic respiration in the presence of this compound, consistent with a ‘branched respiratory chain with various terminal oxidases’” (uriberamirez2024modificationsofthe pages 1-2) | Uribe-Ramírez et al. 2024, doi:10.1007/s10863-024-10041-y, https://doi.org/10.1007/s10863-024-10041-y, Nov 2024 | Taxon-specific tolerance mechanism; curate with uncertainty if generalized. |
| acetate growth conditions — increase usage of — bd and aa3 terminal oxidases | carbon source/environmental factor → enzyme complexes | CHEBI:acetate; label: cytochrome bd oxidase; label: aa3 oxidase | “Growth in the presence of acetate caused bd and aa3 to be the predominant terminal oxidases” (uriberamirez2024modificationsofthe pages 11-12) | Uribe-Ramírez et al. 2024, doi:10.1007/s10863-024-10041-y, https://doi.org/10.1007/s10863-024-10041-y, Nov 2024 | Specific to B. licheniformis and tested media; condition-specific edge. |
| soil microbial fuel cell operation — increases — tetracycline removal | experimental system → outcome | label: soil microbial fuel cell; CHEBI:tetracycline | “soil MFCs removing tetracycline with a removal... 64% higher than control” (zhao2023keygenesof pages 1-2) | Zhao et al. 2023, doi:10.1186/s13068-023-02430-z, https://doi.org/10.1186/s13068-023-02430-z, Nov 2023 | Real-world application edge; useful for application section more than core trait mechanism. |
| soil microbial fuel cell operation — decreases — antibiotic resistance gene abundance | experimental system → outcome | label: soil microbial fuel cell; label: antibiotic resistance gene abundance | “the abundance decreased by 17% in the soil MFC” (zhao2023keygenesof pages 1-2) | Zhao et al. 2023, doi:10.1186/s13068-023-02430-z, https://doi.org/10.1186/s13068-023-02430-z, Nov 2023 | Application-specific systems edge; not intrinsic to organotrophy alone. |


*Table: This table lists candidate causal edges for curating the organotrophic trait graph, spanning ecological drivers, respiratory-chain mechanisms, and application-linked outcomes. It emphasizes evidence-backed triples, suggested ontology grounding, and uncertainty notes for trait-mechanism curation.*


### 4) Key concepts & current understanding (mechanism-focused)

#### 4.1 Canonical bioenergetic mechanism underlying organotrophy (aerobic respiration example)
A recurring mechanistic theme across recent reviews is that oxidation of organic substrates generates reduced electron carriers (e.g., NADH, FADH2), which feed electrons into membrane electron-transport systems. (garimella2024fromcellsto pages 1-2)

A mechanistically explicit description of bacterial ETC coupling in the evidence set includes:
- **Entry:** NADH donates electrons to NADH dehydrogenases; **NDH-1** transfers electrons from NADH to quinone while generating PMF, whereas **NDH-2** transfers electrons to quinone without generating PMF. (giordano2024nitricoxideand pages 8-13)
- **Carrier pool:** the reduced quinone pool donates electrons onward to downstream complexes. (giordano2024nitricoxideand pages 8-13)
- **Middle segment:** Complex III (cytochrome bc1) transfers electrons from the quinone pool to cytochrome c while generating PMF. (giordano2024nitricoxideand pages 8-13)
- **Terminal step:** terminal oxidases reduce O2 to water and contribute to the electrochemical gradient used for ATP synthesis at ATP synthase. (giordano2024nitricoxideand pages 8-13)
- **Energy conservation:** ATP synthase uses the electrochemical gradient (PMF) to convert ADP + Pi into ATP (oxidative phosphorylation). (giordano2024nitricoxideand pages 8-13)

Although some descriptions are presented using mitochondria as the illustrative model, they are explicitly framed as conserved principles relevant to bacterial systems and microbial fuel-cell applications. (garimella2024fromcellsto pages 1-2, garimella2024fromcellsto pages 2-4)

#### 4.2 Minimal respiratory modules and cofactor dependencies (LAB example)
In lactic acid bacteria (LAB), a minimal respiratory chain can comprise **NDH-2 + menaquinone + cytochrome bd oxidase**, and critically, respiration depends on **exogenous heme** because many LAB cannot synthesize heme. (yamamoto2024rolesofflavoprotein pages 3-5)

This is directly relevant to TraitMech because it provides a clean example of an **environmental-factor-to-phenotype** edge: heme availability can switch cells from non-respiring to respiring states, altering energy yield and redox balance. (yamamoto2024rolesofflavoprotein pages 3-5)

#### 4.3 Respiratory chain plasticity and condition-specific oxidase usage (Bacillus example)
Bacillus licheniformis is reported to have a **branched respiratory chain** with multiple terminal oxidases and can continue aerobic respiration even in the presence of cyanide, a classic cytochrome oxidase inhibitor, consistent with alternative terminal oxidases/branches. (uriberamirez2024modificationsofthe pages 1-2)

Moreover, growth conditions shift terminal oxidase usage: growth in the presence of acetate caused bd and aa3 oxidases to predominate, while cyanide strongly inhibited respiration in nutrient-grown cells by inhibiting aa3, but had less effect when bd predominated. (uriberamirez2024modificationsofthe pages 11-12)


### 5) Recent developments (2023–2024 emphasis) and expert-style analysis

**2023 (ecological framing of organotrophy vs alternative energy strategies).** Li et al. (ISME J, 2023) connect organic C gradients to shifts between organotrophic copiotrophs and trace-gas oxidizers, and show that even organoheterotrophs can upregulate hydrogenase/CO dehydrogenase under organic-C depletion—supporting a modern view that trophic “types” can be **facultative and condition-dependent** in complex environments. (li2023reducedtracegas pages 7-8, li2023reducedtracegas pages 1-2)

**2024 (mechanistic and applied focus on modular respiratory chains).** Multiple 2024 sources emphasize that bacterial respiratory chains are modular and adaptable:
- A review of LAB respiration highlights cofactor gating (heme/quinone) and minimal-chain architectures. (yamamoto2024rolesofflavoprotein pages 3-5)
- Respiratory chain plasticity and inhibitor sensitivity (cyanide effects, alternative oxidases) are emphasized for Bacillus. (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12)
- Reviews connecting respiratory electron transport principles to microbial fuel cell design stress electron-carrier generation, quinone pools, terminal oxidases, and PMF-to-ATP coupling as fundamental design constraints. (garimella2024fromcellsto pages 1-2, garimella2024fromcellsto pages 2-4)

**Expert analysis for curation.** Across these sources, organotrophy is best curated not as a single pathway, but as a **graph of mechanistic modules**:
1. Organic substrate uptake/oxidation (varies widely by substrate class).
2. Reducing-equivalent generation (NADH/FADH2/ferredoxin depending on metabolism).
3. Electron transport chain entry (NDH-1 vs NDH-2; substrate dehydrogenases; quinone pool).
4. Terminal electron acceptor usage (O2 vs nitrate; terminal oxidase family selection).
5. Energy conservation efficiency (PMF coupling differences; branch choice changes H+/e− and yield).
This modularization supports a TraitMech causal graph that can be applied across taxa while allowing taxon-specific edges as *uncertain* or *conditional*. (alleman2023mechanismsforgenerating pages 7-9, giordano2024nitricoxideand pages 8-13, yamamoto2024rolesofflavoprotein pages 3-5)


### 6) Applications and real-world implementations (with recent statistics)

Because organotrophy supplies electrons from organic substrates, it underpins **bioelectrochemical systems** where microbial metabolism drives pollutant removal and/or electricity generation.

**Soil microbial fuel cells (MFCs) for antibiotic remediation (statistics).** Zhao et al. (2023) report that soil MFCs achieved tetracycline removal in the cathode–anode overlap area that was **64% higher than control**, and note prior results of **42–50% tetracycline removal within 7 days** versus **6% in control soil**. The same study reports antibiotic resistance gene (ARG) abundance changes: tetracycline increased ARG abundance by **14%**, but ARG abundance **decreased by 17% in the soil MFC**. (zhao2023keygenesof pages 1-2)

**Microbial electrochemical technologies and bionanotechnology outputs.** A 2024 review of Geobacter electron-transfer pathways describes a protein-nanowire thin film device that generates ~**0.5 V** across a 7 μm film with current density ~**17 μA cm−2**, indicating a tangible implementation of microbial-derived conductive materials for low-power applications. (fernandes2024structuralandfunctional pages 38-41)


### 7) Warnings and “do-not-curate-yet” items

1. **Textbook-grade definition gap in retrieved corpus:** No retrieved source provided a single-sentence, formal definition explicitly stating “organotrophs use organic compounds as electron donors” in the classic trophic-classification wording. The ISME J 2023 evidence strongly supports the concept operationally (organotrophs supported by organic C, contrasted with H2/CO oxidation), but curators may still want to add a microbiology textbook or authoritative glossary citation in the YAML (not available in this tool run). (li2023reducedtracegas pages 7-8, li2023reducedtracegas pages 1-2)
2. **Giordano 2024 excerpt lacks full bibliographic metadata:** The mechanistic statements about NDH-1/NDH-2, Complex III/IV, PMF and ATP synthase are explicit and useful, but because DOI/date/journal were not captured in the available text, edges relying solely on this source should be marked **uncertain** until the full citation is verified. (giordano2024nitricoxideand pages 8-13)
3. **Taxon- and condition-specific edges:** edges about acetate-driven oxidase usage and cyanide inhibition patterns are specific to *B. licheniformis* growth conditions and should be curated either with **NCBITaxon constraints** or tagged as conditional. (uriberamirez2024modificationsofthe pages 11-12)
4. **Application edges are not trait mechanisms:** MFC-based tetracycline removal/ARG changes are valuable for “real-world implementation” documentation, but these outcomes are not direct mechanistic definitions of organotrophy and should likely remain in an application/evidence section rather than the core mechanistic subgraph. (zhao2023keygenesof pages 1-2)


## DOI-first bibliography (retrieved in this run)

1. **Li S. et al.** Reduced trace gas oxidizers as a response to organic carbon availability linked to oligotrophs in desert fertile islands. *The ISME Journal*. **May 2023**. DOI: **10.1038/s41396-023-01437-6**. URL: https://doi.org/10.1038/s41396-023-01437-6 (li2023reducedtracegas pages 7-8, li2023reducedtracegas pages 1-2)
2. **Alleman AB, Peters JW.** Mechanisms for Generating Low Potential Electrons across the Metabolic Diversity of Nitrogen-Fixing Bacteria. *Applied and Environmental Microbiology*. **May 2023**. DOI: **10.1128/aem.00378-23**. URL: https://doi.org/10.1128/aem.00378-23 (alleman2023mechanismsforgenerating pages 7-9)
3. **Zhao X. et al.** Key genes of electron transfer, the nitrogen cycle and tetracycline removal in bioelectrochemical systems. *Biotechnology for Biofuels and Bioproducts*. **Nov 2023**. DOI: **10.1186/s13068-023-02430-z**. URL: https://doi.org/10.1186/s13068-023-02430-z (zhao2023keygenesof pages 1-2)
4. **Yamamoto Y.** Roles of flavoprotein oxidase and the exogenous heme- and quinone-dependent respiratory chain in lactic acid bacteria. *Bioscience of Microbiota, Food and Health*. **May 2024**. DOI: **10.12938/bmfh.2024-002**. URL: https://doi.org/10.12938/bmfh.2024-002 (yamamoto2024rolesofflavoprotein pages 3-5)
5. **Garimella SSS. et al.** From cells to power cells: harnessing bacterial electron transport for microbial fuel cells (MFCs). *Annals of Microbiology*. **Jun 2024**. DOI: **10.1186/s13213-024-01761-y**. URL: https://doi.org/10.1186/s13213-024-01761-y (garimella2024fromcellsto pages 1-2, garimella2024fromcellsto pages 2-4)
6. **Uribe-Ramírez D. et al.** Modifications of the respiratory chain of *Bacillus licheniformis* as an alkalophilic and cyanide-degrading microorganism. *Journal of Bioenergetics and Biomembranes*. **Nov 2024**. DOI: **10.1007/s10863-024-10041-y**. URL: https://doi.org/10.1007/s10863-024-10041-y (uriberamirez2024modificationsofthe pages 1-2, uriberamirez2024modificationsofthe pages 11-12)
7. **González-Montalvo MA. et al.** The respiratory chain of *Klebsiella aerogenes* in urine-like conditions: critical roles of NDH-2 and bd-terminal oxidases. *Frontiers in Microbiology*. **Nov 2024**. DOI: **10.3389/fmicb.2024.1479714**. URL: https://doi.org/10.3389/fmicb.2024.1479714 (gonzalezmontalvo2024therespiratorychain pages 1-2)
8. **Fernandes TM.** Structural and functional insights on the electrifying pathways of *Geobacter sulfurreducens*. **2024**. DOI/journal not captured in retrieved excerpt. (fernandes2024structuralandfunctional pages 38-41, fernandes2024structuralandfunctional pages 41-45)
9. **Giordano F.** Nitric Oxide and Hydrogen Sulfide interplay and tolerance in *Pseudomonas aeruginosa*: role of sulfide catabolism and aerobic respiration. **2024**. DOI/journal not captured in retrieved excerpt. (giordano2024nitricoxideand pages 8-13)


References

1. (li2023reducedtracegas pages 7-8): Shuyue Li, Shanshan Yang, Xiaomeng Wei, Shuo Jiao, Wen Luo, Weimin Chen, and Gehong Wei. Reduced trace gas oxidizers as a response to organic carbon availability linked to oligotrophs in desert fertile islands. The ISME journal, 17:1257-1266, May 2023. URL: https://doi.org/10.1038/s41396-023-01437-6, doi:10.1038/s41396-023-01437-6. This article has 31 citations.

2. (li2023reducedtracegas pages 1-2): Shuyue Li, Shanshan Yang, Xiaomeng Wei, Shuo Jiao, Wen Luo, Weimin Chen, and Gehong Wei. Reduced trace gas oxidizers as a response to organic carbon availability linked to oligotrophs in desert fertile islands. The ISME journal, 17:1257-1266, May 2023. URL: https://doi.org/10.1038/s41396-023-01437-6, doi:10.1038/s41396-023-01437-6. This article has 31 citations.

3. (giordano2024nitricoxideand pages 8-13): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

4. (yamamoto2024rolesofflavoprotein pages 3-5): Yuji Yamamoto. Roles of flavoprotein oxidase and the exogenous heme- and quinone-dependent respiratory chain in lactic acid bacteria. Bioscience of Microbiota, Food and Health, 43:183-191, May 2024. URL: https://doi.org/10.12938/bmfh.2024-002, doi:10.12938/bmfh.2024-002. This article has 3 citations.

5. (garimella2024fromcellsto pages 1-2): Sri Sathya Sandilya Garimella, Sai Vennela Rachakonda, Sai Sowmya Pratapa, Gnana Divya Mannem, and Ganesh Mahidhara. From cells to power cells: harnessing bacterial electron transport for microbial fuel cells (mfcs). Annals of Microbiology, 74:1-15, Jun 2024. URL: https://doi.org/10.1186/s13213-024-01761-y, doi:10.1186/s13213-024-01761-y. This article has 25 citations and is from a peer-reviewed journal.

6. (li2023reducedtracegas pages 2-3): Shuyue Li, Shanshan Yang, Xiaomeng Wei, Shuo Jiao, Wen Luo, Weimin Chen, and Gehong Wei. Reduced trace gas oxidizers as a response to organic carbon availability linked to oligotrophs in desert fertile islands. The ISME journal, 17:1257-1266, May 2023. URL: https://doi.org/10.1038/s41396-023-01437-6, doi:10.1038/s41396-023-01437-6. This article has 31 citations.

7. (li2023reducedtracegas pages 8-9): Shuyue Li, Shanshan Yang, Xiaomeng Wei, Shuo Jiao, Wen Luo, Weimin Chen, and Gehong Wei. Reduced trace gas oxidizers as a response to organic carbon availability linked to oligotrophs in desert fertile islands. The ISME journal, 17:1257-1266, May 2023. URL: https://doi.org/10.1038/s41396-023-01437-6, doi:10.1038/s41396-023-01437-6. This article has 31 citations.

8. (uriberamirez2024modificationsofthe pages 1-2): Daniel Uribe-Ramírez, Lucero Romero-Aguilar, Héctor Vázquez-Meza, Eliseo Cristiani-Urbina, and Juan Pablo Pardo. Modifications of the respiratory chain of bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. Journal of Bioenergetics and Biomembranes, 56:591-605, Nov 2024. URL: https://doi.org/10.1007/s10863-024-10041-y, doi:10.1007/s10863-024-10041-y. This article has 1 citations and is from a peer-reviewed journal.

9. (gonzalezmontalvo2024therespiratorychain pages 1-2): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

10. (uriberamirez2024modificationsofthe pages 11-12): Daniel Uribe-Ramírez, Lucero Romero-Aguilar, Héctor Vázquez-Meza, Eliseo Cristiani-Urbina, and Juan Pablo Pardo. Modifications of the respiratory chain of bacillus licheniformis as an alkalophilic and cyanide-degrading microorganism. Journal of Bioenergetics and Biomembranes, 56:591-605, Nov 2024. URL: https://doi.org/10.1007/s10863-024-10041-y, doi:10.1007/s10863-024-10041-y. This article has 1 citations and is from a peer-reviewed journal.

11. (garimella2024fromcellsto pages 4-6): Sri Sathya Sandilya Garimella, Sai Vennela Rachakonda, Sai Sowmya Pratapa, Gnana Divya Mannem, and Ganesh Mahidhara. From cells to power cells: harnessing bacterial electron transport for microbial fuel cells (mfcs). Annals of Microbiology, 74:1-15, Jun 2024. URL: https://doi.org/10.1186/s13213-024-01761-y, doi:10.1186/s13213-024-01761-y. This article has 25 citations and is from a peer-reviewed journal.

12. (gonzalezmontalvo2024therespiratorychain pages 13-13): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

13. (giordano2024nitricoxideand pages 1-8): F Giordano. Nitric oxide and hydrogen sulfide interplay and tolerance in pseudomonas aeruginosa: role of sulfide catabolism and aerobic respiration. Unknown journal, 2024.

14. (gonzalezmontalvo2024therespiratorychain pages 13-14): Martín A. González-Montalvo, Jennifer M. Sorescu, Gabriella Baltes, Oscar Juárez, and Karina Tuz. The respiratory chain of klebsiella aerogenes in urine-like conditions: critical roles of ndh-2 and bd-terminal oxidases. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1479714, doi:10.3389/fmicb.2024.1479714. This article has 10 citations and is from a peer-reviewed journal.

15. (zhao2023keygenesof pages 1-2): Xiaodong Zhao, Xiaorui Qin, Xiuqing Jing, Teng Wang, Qingqing Qiao, Xiaojing Li, Pingmei Yan, and Yongtao Li. Key genes of electron transfer, the nitrogen cycle and tetracycline removal in bioelectrochemical systems. Biotechnology for Biofuels and Bioproducts, Nov 2023. URL: https://doi.org/10.1186/s13068-023-02430-z, doi:10.1186/s13068-023-02430-z. This article has 25 citations and is from a domain leading peer-reviewed journal.

16. (garimella2024fromcellsto pages 2-4): Sri Sathya Sandilya Garimella, Sai Vennela Rachakonda, Sai Sowmya Pratapa, Gnana Divya Mannem, and Ganesh Mahidhara. From cells to power cells: harnessing bacterial electron transport for microbial fuel cells (mfcs). Annals of Microbiology, 74:1-15, Jun 2024. URL: https://doi.org/10.1186/s13213-024-01761-y, doi:10.1186/s13213-024-01761-y. This article has 25 citations and is from a peer-reviewed journal.

17. (alleman2023mechanismsforgenerating pages 7-9): Alexander B. Alleman and John W. Peters. Mechanisms for generating low potential electrons across the metabolic diversity of nitrogen-fixing bacteria. Applied and Environmental Microbiology, May 2023. URL: https://doi.org/10.1128/aem.00378-23, doi:10.1128/aem.00378-23. This article has 54 citations and is from a peer-reviewed journal.

18. (fernandes2024structuralandfunctional pages 38-41): TM Fernandes. Structural and functional insights on the electrifying pathways of geobacter sulfurreducens. Unknown journal, 2024.

19. (fernandes2024structuralandfunctional pages 41-45): TM Fernandes. Structural and functional insights on the electrifying pathways of geobacter sulfurreducens. Unknown journal, 2024.