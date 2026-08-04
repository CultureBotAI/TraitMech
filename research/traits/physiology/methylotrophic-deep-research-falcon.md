---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:22:34.214035'
end_time: '2026-08-04T11:32:33.284258'
duration_seconds: 599.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: methylotrophic
  trait_identifier: METPO:1000651
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: methylotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy and carbon from reduced
    one-carbon compounds.
  parent_traits: METPO:1000631
  synonyms: TT_methylotroph, methylotroph, methylotrophy
  evidence_summary: 'DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy
    (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy
    mechanisms.)'
  causal_graph_summary: 'methylotrophic_methanol_assimilation: 19 nodes, 15 edges'
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
- **Trait label:** methylotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000651
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy and carbon from reduced one-carbon compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_methylotroph, methylotroph, methylotrophy
- **Existing evidence:** DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy mechanisms.)
- **Existing causal graph summary:** methylotrophic_methanol_assimilation: 19 nodes, 15 edges

## Research Objective

Research the microbial trait **methylotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methylotrophic.yaml`.

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
- **Trait label:** methylotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000651
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy and carbon from reduced one-carbon compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_methylotroph, methylotroph, methylotrophy
- **Existing evidence:** DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy mechanisms.)
- **Existing causal graph summary:** methylotrophic_methanol_assimilation: 19 nodes, 15 edges

## Research Objective

Research the microbial trait **methylotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methylotrophic.yaml`.

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


# Curation-focused research report: methylotrophic

## Executive curation recommendation

**Trait:** methylotrophic  
**Trait identifier:** `METPO:1000651`  
**Category:** PHYSIOLOGY; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** `METPO:1000631`

The trait should represent the demonstrated capacity to obtain **both cellular carbon and energy from reduced one-carbon compounds**, generally compounds lacking carbon–carbon bonds. The most defensible generic causal architecture is:

**reduced C1 substrate → substrate-specific oxidation/transfer module → assimilatory C1 flux + energy-conserving oxidation → biomass formation and growth on the C1 substrate.**

Methylotrophy is mechanistically diverse rather than a single pathway. Therefore, the graph should use alternative modules for methanol, methylamine, and other reduced C1 substrates, converging on formaldehyde/formate-level metabolism, assimilation, energy conservation, and growth. Methanol oxidation followed by formaldehyde assimilation is a strong core example, but it must not define the entire trait. The authoritative modern definition distinguishes methylotrophy from **methylovory**, in which a C1 compound supplements energy without supplying the organism’s carbon requirement. Methanotrophs are methylotrophs that can use methane, but non-methanotrophic methylotrophs use substrates such as methanol or methylamine without oxidizing methane (chistoserdova2018currenttrendsin pages 3-4, chistoserdova2018currenttrendsin pages 2-3).

## 1. Scope and boundaries

### Included phenotype

A positive phenotype requires evidence of growth, biomass carbon incorporation, or a comparably strong physiological demonstration that a reduced C1 compound serves as both carbon and energy source. Suitable assays include growth with methanol or methylamine as the sole carbon and energy source, isotope incorporation into biomass coupled to oxidation, or genetic loss-and-rescue experiments that connect a C1 pathway to growth.

### Important boundary cases

1. **Methanotrophy:** methane-utilizing organisms are a substrate-defined subset of methylotrophs. Methane monooxygenase belongs in a methane-specific upstream extension, not in the universal methylotrophy core.
2. **Methylovory:** supplemental oxidation of a C1 compound for energy, without C1-derived biomass carbon, is insufficient. This is explicitly distinguished from methylotrophy in current expert reviews (chistoserdova2018currenttrendsin pages 2-3, wegner2019lanthanidedependentmethylotrophsof pages 2-3).
3. **Formaldehyde detoxification:** glutathione-dependent or other formaldehyde-removal systems occur in many non-methylotrophs. Detoxification alone does not establish methylotrophy.
4. **Methylamine as nitrogen only:** methylamine utilization for nitrogen, with succinate or another multicarbon carbon source, is not a methylotrophic growth phenotype. In *Methylobacterium extorquens* AM1, MaDH and N-methylglutamate pathways can be differentially favored for methylamine as carbon/energy versus nitrogen (nayak2016selectionmaintainsapparently pages 8-9).
5. **Genomic potential:** an isolated `xoxF`, `mxaF`, formaldehyde-dehydrogenase gene, or incomplete pathway is not proof of growth. Some XoxF-containing organisms lack recognizable assimilation modules, and environmental studies commonly infer rather than demonstrate activity (chistoserdova2018currenttrendsin pages 2-3, voutsinos2024weatheredgranitesand pages 2-4).
6. **Synthetic methylotrophy:** engineered methanol incorporation should be described as synthetic or partial unless methanol supports net growth as the carbon and energy source.
7. **Methyl-based methanogenesis:** archaeal conversion of methyl compounds to methane is often called “methylotrophic methanogenesis,” but it is not automatically equivalent to the aerobic bacterial trophic phenotype modeled here. It should be represented only if TraitMech explicitly intends a cross-domain, process-neutral scope.

## 2. Candidate causal-graph nodes

Identifiers below are limited to source-reported or readily verifiable stable classes. Where exact ontology mapping has not been checked against the project’s preferred release, a label-only node is safer than an invented CURIE.

### Trait and phenotype nodes

- `METPO:1000651` — methylotrophic
- growth on reduced one-carbon compound
- C1-derived biomass formation
- C1-dependent energy conservation
- methylovory — boundary/negative comparator
- formaldehyde tolerance — accessory phenotype, not equivalent to methylotrophy

### Substrates, products, and intermediates

- methanol
- methylamine
- methane — substrate-specific upstream extension
- formaldehyde
- formate/formic acid
- carbon dioxide
- ammonium
- glycine; L-serine; hydroxypyruvate; D-glycerate
- ribulose 5-phosphate; hexulose 6-phosphate; fructose 6-phosphate
- 5,10-methylene-tetrahydrofolate; tetrahydrofolate
- acetyl-CoA; glyoxylate; malyl-CoA; ethylmalonyl-CoA
- NAD+/NADH; PQQ/PQQH2
- molecular oxygen; hydrogen peroxide

### Environmental and experimental factors

- methanol or methylamine as sole carbon and energy source
- oxygen availability
- calcium availability
- bioavailable lanthanides, especially La, Ce, and Nd
- phosphate limitation and lanthanide-phosphate minerals
- formaldehyde concentration/stress
- alternative electron acceptors such as N2O — taxon-specific extension
- pH and temperature — assay/context attributes rather than universal causes

### Genes, proteins, enzymes, and complexes

**Methanol oxidation**
- `mxaF`, `mxaI`; MxaFI PQQ-dependent methanol dehydrogenase, `EC:1.1.2.7`
- `xoxF`; XoxF-type lanthanide-dependent PQQ methanol dehydrogenase
- NAD-dependent methanol dehydrogenase, `EC:1.1.1.244`
- alcohol oxidase/AOX — methylotrophic yeasts only
- PQQ biosynthesis proteins
- XoxG/cytochrome cL-type electron acceptor

**Formaldehyde oxidation and regulation**
- formaldehyde-activating enzyme, Fae
- H4MPT-dependent formaldehyde oxidation module
- formate dehydrogenase
- glutathione-dependent formaldehyde-activating/dehydrogenase module, including Gfa/FrmAB-like proteins
- EfgA formaldehyde sensor/binder — taxon-specific regulatory node

**Assimilation**
- hexulose-6-phosphate synthase/HPS
- 6-phospho-3-hexulose isomerase/PHI
- serine hydroxymethyltransferase/SHMT, `EC:2.1.2.1`
- serine–glyoxylate transaminase, `EC:2.6.1.45`
- hydroxypyruvate reductase, `EC:1.1.1.81`
- glycerate 2-kinase, `EC:2.7.1.165`
- phosphoenolpyruvate carboxylase, `EC:4.1.1.31`
- malate dehydrogenase, `EC:1.1.1.37`
- malate-CoA ligase, `EC:6.2.1.9`
- malyl-CoA lyase, `EC:4.1.3.24`
- isocitrate lyase, `EC:4.1.3.1`; malate synthase
- crotonyl-CoA carboxylase/reductase and ethylmalonyl-CoA pathway proteins
- dihydroxyacetone synthase/DAS — yeast XuMP/DHA pathway

**Methylamine entry**
- `mau` cluster; methylamine dehydrogenase/MaDH
- N-methylglutamate/NMG pathway
- `mgdABCD`; NMG dehydrogenase
- `nmgR`; NMG-pathway regulator

**Lanthanide acquisition**
- LutH-like TonB-dependent receptor
- LutAEF-like ABC transporter
- lanmodulin/LanM
- candidate metallophore or lanthanophore biosynthesis system

### Pathway and process nodes

- methanol oxidation
- methylamine oxidation
- H4MPT-dependent formaldehyde oxidation
- formate oxidation
- ribulose-monophosphate/RuMP assimilation cycle
- serine assimilation cycle
- glyoxylate regeneration
- ethylmalonyl-CoA/EMC pathway
- yeast xylulose-monophosphate/DHA pathway
- electron transfer to respiratory chain
- biomass synthesis

### Cellular localizations

- bacterial periplasm — PQQ-dependent MxaFI/XoxF oxidation in characterized Gram-negative methylotrophs
- cytoplasm — H4MPT/formate and assimilation reactions
- yeast peroxisome — AOX-dependent methanol oxidation
- outer membrane/periplasm/cytoplasmic membrane — staged lanthanide uptake machinery

## 3. Candidate evidence-backed causal edges

| Subject–predicate–object triple | Reference and supporting snippet | Curation note |
|---|---|---|
| reduced C1 compound — **serves as carbon-and-energy source for** → methylotrophic growth | “Methylotrophy [uses] C1 compounds as energy and carbon sources,” whereas methylovory is supplemental energy use (DOI 10.1016/j.tim.2018.01.011; August 2018) (chistoserdova2018currenttrendsin pages 3-4, chistoserdova2018currenttrendsin pages 2-3) | **Core, high confidence.** Use as the trait-defining endpoint. |
| MxaFI — **oxidizes** → methanol to formaldehyde | MxaFI is the Ca-dependent, PQQ-linked MDH; the 2024 pangenomic study states that MDH converts methanol to formaldehyde and identifies `mxaF/mxaI` as its subunits (DOIs 10.3389/fbioe.2021.787791; December 2021, and 10.1128/msystems.00248-24; June 2024) (le2021methanoldehydrogenasesas pages 2-3, samanta2024fromgenometo pages 18-20) | **Core alternative module.** Most applicable to Gram-negative methylotrophs. |
| PQQ + Ca2+ — **enable catalytic activity of** → MxaF | Structures contain one PQQ and one Ca2+ in each MxaF-encoded large subunit (DOI 10.3389/fbioe.2021.787791; December 2021) (le2021methanoldehydrogenasesas pages 4-6) | **High confidence.** Cofactor relation, not a sufficient phenotype marker. |
| MxaFI — **transfers methanol-derived electrons to** → cytochrome c | PQQ captures electrons from methanol and passes them to cytochrome; Mxa MDH is activated by a cytochrome-c electron acceptor (le2021methanoldehydrogenasesas pages 2-3, samanta2024fromgenometo pages 18-20) | **High confidence**, although exact cytochrome partners vary. |
| XoxF + lanthanide + PQQ — **oxidizes** → methanol to formaldehyde | XoxF enzymes require a lanthanide in the active site and catalyze methanol-to-formaldehyde oxidation in the periplasm (DOI 10.1186/s12915-024-01841-0; February 2024) (voutsinos2024weatheredgranitesand pages 2-4) | **Core alternative module.** Some reports assign formate as the apparent XoxF product; do not curate a universal product without enzyme- and taxon-specific evidence. |
| low-mass lanthanides — **enable** → XoxF-dependent methylotrophic growth | Beijerinckiaceae growth on 1% methanol was supported by La, Ce, and Nd; heavier lanthanides supported poor growth (DOI 10.1128/AEM.01830-19; published online December 2019, issue January 2020) (wegner2019lanthanidedependentmethylotrophsof pages 8-9) | **Strong but taxon-specific environmental edge.** |
| lanthanide addition — **restores** → methylotrophy in an `mxaF` mutant through XoxF | Lanthanides restored methylotrophy in an *M. extorquens* AM1 `mxaF` mutant by stimulating Xox-type MDH activity (wegner2019lanthanidedependentmethylotrophsof pages 2-3) | **Strong genetic evidence**, but model-organism-specific. |
| LutH/TonB receptor + LutAEF ABC transporter + LanM — **promote acquisition/delivery of** → lanthanides to XoxF | Current model assigns TonB-dependent uptake to the periplasm, ABC transport to the cytoplasm, and lanmodulin-mediated handling/delivery (DOI 10.1128/AEM.01830-19) (wegner2019lanthanidedependentmethylotrophsof pages 2-3, wegner2019lanthanidedependentmethylotrophsof pages 12-13) | **Provisional modular edge.** Components and compartmental routes differ among taxa. |
| methanol-derived formaldehyde — **enters** → H4MPT-dependent oxidation to formate | In AM1, formaldehyde flows through the H4MPT pathway to formate; Fae accelerates formaldehyde–H4MPT condensation (DOI 10.1016/j.cub.2016.04.029; June 2016) (nayak2016selectionmaintainsapparently pages 3-4) | **High confidence** in alphaproteobacterial models. |
| formate dehydrogenase — **oxidizes** → formate to CO2 | AM1 partially oxidizes formate to CO2 through four formate dehydrogenases (nayak2016selectionmaintainsapparently pages 3-4) | **Strong**, but copy number is strain-specific. This branch supplies dissimilatory reducing power rather than biomass carbon. |
| formaldehyde oxidation — **supports** → energy generation for methylotrophic growth | The 2024 synthesis states that methylotrophs derive growth energy by oxidizing C1 substrates through specific dehydrogenases (DOI 10.1128/msystems.00248-24) (samanta2024fromgenometo pages 18-20) | **Core process-level edge.** Avoid claiming a single universal respiratory chain. |
| HPS — **condenses** → formaldehyde with ribulose-5-phosphate | The RuMP module is defined by HPS and PHI and is a principal prokaryotic methanol-assimilation route (DOI 10.3389/fbioe.2021.787791) (le2021methanoldehydrogenasesas pages 2-3) | **Review-supported candidate.** Add a primary biochemical source before assigning exact reaction CURIEs. |
| PHI — **converts** → hexulose-6-phosphate to fructose-6-phosphate | HPS/PHI are identified as the key RuMP combination, with high theoretical growth performance (le2021methanoldehydrogenasesas pages 2-3) | **Moderate confidence** for pathway architecture; theoretical advantage is not universal physiological superiority. |
| SHMT — **incorporates a C1 unit into glycine to form** → L-serine | The serine pathway begins through SHMT (`EC:2.1.2.1`), with 5,10-methylene-THF donating the formaldehyde-derived unit to glycine (DOI 10.1128/msystems.00248-24) (samanta2024fromgenometo pages 18-20) | **High-confidence serine-cycle edge.** |
| serine–glyoxylate transaminase — **converts** → serine + glyoxylate to hydroxypyruvate + glycine | The reaction and `EC:2.6.1.45` are explicitly described in the 2024 pathway reconstruction (samanta2024fromgenometo pages 18-20) | **High confidence**, although the study also reports taxon-specific isozymes. |
| hydroxypyruvate reductase — **reduces** → hydroxypyruvate to D-glycerate | Explicitly assigned `EC:1.1.1.81` in the serine pathway (samanta2024fromgenometo pages 18-20) | **High confidence.** |
| glycerate 2-kinase — **phosphorylates** → D-glycerate to 2-phosphoglycerate | Explicitly assigned `EC:2.7.1.165` (samanta2024fromgenometo pages 18-20) | **High confidence.** |
| PEP carboxylase — **fixes CO2 into** → oxaloacetate | PEP carboxylase (`EC:4.1.1.31`) converts PEP to oxaloacetate in the reconstructed serine cycle (samanta2024fromgenometo pages 18-20) | **High confidence** for the pathway module. |
| malate-CoA ligase + malyl-CoA lyase — **regenerate** → glyoxylate and produce acetyl-CoA | Malate-CoA ligase (`EC:6.2.1.9`) forms malyl-CoA, cleaved by malyl-CoA lyase (`EC:4.1.3.24`) into acetyl-CoA and glyoxylate (samanta2024fromgenometo pages 18-20) | **High-confidence cycle-closing edge.** |
| isocitrate lyase + malate synthase — **support** → glyoxylate regeneration | The `icl+` serine-cycle variant uses the glyoxylate cycle; many methylotrophs instead lack isocitrate lyase (samanta2024fromgenometo pages 18-20) | **Optional, taxon-specific branch.** |
| absence of isocitrate lyase — **favors use of** → EMC pathway for glyoxylate regeneration | In many type II methylotrophs, acetyl-CoA is processed through EMC when isocitrate lyase is absent (samanta2024fromgenometo pages 18-20) | **Moderate confidence.** Encode as an alternative pathway, not as a strict logical rule for every taxon. |
| MaDH/`mau` — **oxidizes** → methylamine to formaldehyde + ammonium | AM1 MaDH produces formaldehyde; deletion of the `mau` cluster removes this route (DOI 10.1016/j.cub.2016.04.029) (nayak2016selectionmaintainsapparently pages 3-4, nayak2016selectionmaintainsapparently pages 8-9) | **High-confidence methylamine entry route**, but not universal. |
| Fae/H4MPT oxidation — **prevents accumulation of** → toxic formaldehyde during MaDH-dependent growth | `fae` deletion prevented methylamine growth because toxic formaldehyde accumulated; Fae is essential for rapid MaDH-mediated growth (nayak2016selectionmaintainsapparently pages 3-4) | **Strong causal genetic edge.** |
| `mgdABCD`/NMG dehydrogenase — **is required for** → NMG-dependent growth on methylamine | Deleting `mgdABCD` abolished methylamine growth in evolved NMG-dependent strains; deleting H4MPT biosynthesis gene `mptG` also abolished growth (nayak2016selectionmaintainsapparently pages 3-4) | **Strong, strain- and regulatory-context-specific.** |
| increased NMG pathway expression — **increases** → NMG-dependent methylamine growth | Evolved strains had 5.2- and 9.3-fold higher NMGDH activity; their growth rates were 0.04 and 0.09 h−1 on 20 mM methylamine (nayak2016selectionmaintainsapparently pages 4-6, nayak2016selectionmaintainsapparently pages 3-4) | **Quantitative experimental edge.** Do not infer constitutive NMG-dependent methylotrophy from gene presence. |
| excessive formaldehyde — **downregulates** → core methylotrophy and serine/EMC pathways | In *Methylobacterium* sp. XJLW, formaldehyde exposure predominantly downregulated methanol/formaldehyde oxidation, TCA, serine-cycle, and EMC genes (DOI 10.1186/s12864-024-10923-w; October 2024) (shao2024transcriptomicdatareveals pages 2-4) | **Taxon- and stress-specific regulatory edge.** |
| `RS27765` + `glyA` redundancy — **supports** → XJLW growth on methanol | The double knockout lost methanol growth, whereas either single mutant retained growth (shao2024transcriptomicdatareveals pages 7-9) | **Uncertain mechanism.** Genetic phenotype is real, but the proposed direct methanol-assimilation bypass lacks purified-enzyme activity. Do not curate the claimed reaction yet. |
| N2O respiration — **can enhance** → C1 oxidation and biomass under O2 limitation | In *Methylocella tundrae* T4, adding N2O increased CH4 oxidation from 9.74 to 12.19 mmol L−1 and OD600 increase from 0.114 to 0.143; cells achieved about 37% more CH4 oxidized per O2 reduced (DOI 10.1038/s41467-024-48161-z; May 2024) (awala2024nitrousoxiderespiration pages 8-9) | **Ecological extension, not core methylotrophy.** Relevant only to specific methanotrophs with functional `nosZ` systems. |

The following compact artifact summarizes recommended module-level curation decisions.

| module | core causal chain | confidence | scope/taxon caveat | recommended curation action |
|---|---|---|---|---|
| Phenotype endpoint | reduced C1 compound availability → methanol/formaldehyde/methylamine utilization pathways + assimilation + energy conservation → growth with reduced one-carbon compounds as carbon and energy source | High | Trait requires growth use of reduced C1 compounds, not just energy supplementation or detoxification; distinguish from methylovory and methanotrophy as a subset (chistoserdova2018currenttrendsin pages 3-4, chistoserdova2018currenttrendsin pages 2-3) | Curate as top-level trait definition and endpoint node for growth on reduced C1 compounds |
| Methanol oxidation: MxaFI | methanol → formaldehyde via PQQ-dependent methanol dehydrogenase MxaFI (EC 1.1.2.7); MxaF large subunit binds PQQ + Ca2+; electrons passed to cytochrome | High | Strong for Gram-negative methylotrophs; periplasmic localization emphasized in these taxa; not universal because some methylotrophs lack MxaFI and rely on XoxF or NAD-MDH (le2021methanoldehydrogenasesas pages 2-3, le2021methanoldehydrogenasesas pages 4-6, samanta2024fromgenometo pages 18-20) | Curate core edge set: methanol enables methylotrophy via MxaFI-dependent oxidation to formaldehyde; annotate Ca2+/PQQ requirement and periplasmic location |
| Methanol oxidation: XoxF | methanol → formaldehyde via XoxF-type PQQ methanol dehydrogenase (EC 1.1.2.7 class context); XoxF requires lanthanide in active site; often replaces/suppresses MxaFI under lanthanide-replete conditions | High | Strong but not universal across all methylotrophs; clade composition and exact product can vary by taxon/report; regulatory relationship to mxaF especially characterized in specific alphaproteobacterial models (le2021methanoldehydrogenasesas pages 2-3, wegner2019lanthanidedependentmethylotrophsof pages 2-3, rocha2024rareearthelements pages 2-5) | Curate as major alternative methanol oxidation module with lanthanide dependence; mark mxaF suppression/regulation as taxon-specific unless generalized evidence is added |
| Methanol oxidation: NAD-dependent MDH | methanol → formaldehyde via NAD-dependent methanol dehydrogenase (EC 1.1.1.244) with NAD+ reduction | Medium | Strong for Gram-positive methylotrophs and specific exceptions such as Methylovirgula sp. 4M-Z18; not a universal methylotroph module (le2021methanoldehydrogenasesas pages 2-3, samanta2024fromgenometo pages 18-20, samanta2024fromgenometo pages 12-14) | Curate as alternative, taxon-restricted methanol oxidation route; mark uncertain for broad trait graph |
| Methanol oxidation: AOX in yeasts | methanol → formaldehyde + H2O2 via O2-dependent alcohol oxidase (AOX); catalase and dihydroxyacetone synthase mitigate toxicity/enable assimilation | Medium | Eukaryotic methylotroph-specific, peroxisomal, aerobic only; unsuitable for bacterial trait graph unless cross-kingdom scope is intended (le2021methanoldehydrogenasesas pages 2-3) | Do not place in bacterial core graph; keep as optional non-bacterial extension/warning row |
| Formaldehyde oxidation / H4MPT-formate-CO2 energy branch | formaldehyde + H4MPT (spontaneous or FAE-assisted) → H4MPT-dependent oxidation pathway → formate → CO2 via formate dehydrogenases; oxidation provides energy | High | Strong in alphaproteobacterial methylotroph models and methylamine-growth experiments; some taxa also have glutathione-dependent formaldehyde oxidation; exact enzyme inventory varies (nayak2016selectionmaintainsapparently pages 3-4, alessa2021comprehensivecomparativegenomics pages 10-11) | Curate as central dissimilatory energy-conserving branch linked to methanol and methylamine growth; include FAE/H4MPT/formate dehydrogenase nodes and mark glutathione branch as optional/taxon-dependent |
| Formaldehyde oxidation: glutathione-dependent branch | formaldehyde → glutathione-dependent formaldehyde oxidation (gfa/frmAB-like or equivalent) → formate | Medium | Present in many but not all methylotrophs; can also serve detoxification outside true methylotrophy, so presence alone is insufficient for trait assertion (alessa2021comprehensivecomparativegenomics pages 10-11) | Curate only as accessory/module node with caution note that it is not by itself diagnostic of methylotrophy |
| RuMP assimilation | formaldehyde + ribulose-5-phosphate → hexulose-6-phosphate via HPS → fructose-6-phosphate via PHI → biomass precursors | Medium | Canonical bacterial assimilation route, especially in RuMP methylotrophs; direct evidence in retrieved texts is review-level rather than organism-specific experimental here (le2021methanoldehydrogenasesas pages 2-3) | Curate pathway-level module nodes HPS and PHI as candidate assimilation route; mark as review-supported and seek primary experimental citation before strong edge curation |
| Serine cycle assimilation | formaldehyde + tetrahydrofolate → 5,10-methylene-THF; glycine + 5,10-methylene-THF → L-serine via SHMT (EC 2.1.2.1) → 3-hydroxypyruvate via serine-glyoxylate transaminase (EC 2.6.1.45) → D-glycerate via hydroxypyruvate reductase (EC 1.1.1.81) → 2-phospho-D-glycerate via glycerate 2-kinase (EC 2.7.1.165) → phosphoenolpyruvate/oxaloacetate/malyl-CoA cycle regeneration | High | Strongly supported as primary assimilation route in type II methylotrophs and many facultative methylotrophs; enzyme complements and isozymes vary by taxon (samanta2024fromgenometo pages 18-20, shao2024transcriptomicdatareveals pages 2-4) | Curate as core assimilation module with SHMT, SGT, HPR, glycerate kinase, PEP carboxylase, malate dehydrogenase, malate-CoA ligase, malyl-CoA lyase |
| Glyoxylate regeneration / icl+ serine cycle | acetyl-CoA → glyoxylate regeneration through glyoxylate cycle requiring isocitrate lyase (EC 4.1.3.1) + malate synthase | Medium | Only some methylotrophs possess isocitrate lyase during methylotrophic growth; not a universal regeneration strategy (samanta2024fromgenometo pages 18-20) | Curate as optional branch for serine-cycle methylotrophs with explicit taxon caveat |
| EMC regeneration | acetyl-CoA → ethylmalonyl-CoA pathway → glyoxylate + propionyl-CoA/succinate regeneration; crotonyl-CoA carboxylase/reductase central | Medium | Common when isocitrate lyase absent, especially in many type II methylotrophs, but direct evidence here is partly genomic/review synthesis (samanta2024fromgenometo pages 18-20) | Curate as alternative regeneration branch linked to serine cycle; mark as pathway-level with moderate confidence |
| Methylamine oxidation: Mau pathway | methylamine → formaldehyde + NH4+ via methylamine dehydrogenase (MaDH; mau cluster) → formaldehyde enters H4MPT oxidation and/or serine assimilation | High | Strong in Methylobacterium extorquens AM1 background and many methylotrophs, but some methylotrophs lack mau entirely (nayak2016selectionmaintainsapparently pages 3-4, nayak2016selectionmaintainsapparently pages 8-9) | Curate as major methylamine-to-formaldehyde entry route with explicit note that it is absent in some methylotrophs |
| Methylamine oxidation: NMG pathway | methylamine → N-methylglutamate pathway → formaldehyde-equivalent flux / NH4+ release → H4MPT oxidation and/or serine cycle; mgdABCD required for evolved methylamine growth in mau-deficient AM1 derivatives | High | Strong but context-sensitive: in WT AM1 the pathway is repressed during methylamine growth and can support nitrogen use differently from carbon use; role varies among taxa (nayak2016selectionmaintainsapparently pages 4-6, nayak2016selectionmaintainsapparently pages 3-4, nayak2016selectionmaintainsapparently pages 8-9) | Curate as distinct methylamine module, but annotate regulatory and physiological caveat: carbon-source methylotrophy versus nitrogen assimilation are separable outcomes |
| Lanthanide uptake / REE utilization | environmental lanthanides → TonB-dependent receptor (lutH-like) to periplasm + ABC transporter (LutAEF-like) to cytoplasm + lanmodulin/LanM binding → activation/use of XoxF/ExaF-like REE enzymes → methanol oxidation | Medium | Strong in specific alphaproteobacterial and environmental genomic studies; transporter inventory differs across taxa and some proposed transporters are still inferred (wegner2019lanthanidedependentmethylotrophsof pages 2-3, wegner2019lanthanidedependentmethylotrophsof pages 12-13, rocha2024rareearthelements pages 2-5, voutsinos2024weatheredgranitesand pages 10-12) | Curate lanthanide dependence of XoxF as core; keep detailed uptake machinery as taxon-specific or provisional until broader direct experimental support is assembled |
| Environmental dependency: low-mass lanthanides | La3+/Ce3+/Nd3+ availability → supports XoxF-based methylotrophic growth on methanol | High | Demonstrated in isolated Beijerinckiaceae; growth on heavier lanthanides poor; effect size and preferred lanthanides vary with XoxF active-site chemistry (wegner2019lanthanidedependentmethylotrophsof pages 8-9) | Curate as strong environmental factor edge for XoxF-based methylotrophy, with low-mass lanthanides prioritized |
| Genomic prediction caution | presence of xoxF, formaldehyde oxidation genes, or secondary lanthanide clusters alone ↛ proven methylotrophic phenotype | High | Environmental MAGs and comparative genomics show broad distribution without phenotype confirmation; detoxification genes can exist outside methylotrophy (chistoserdova2018currenttrendsin pages 2-3, voutsinos2024weatheredgranitesand pages 2-4, voutsinos2024weatheredgranitesand pages 10-12, alessa2021comprehensivecomparativegenomics pages 10-11) | Add explicit curation warning: require growth or mechanistic phenotype evidence before asserting trait from genomes alone |


*Table: This table summarizes which methylotrophy modules are strongest for immediate TraitMech curation versus which remain taxon-specific or review-level. It highlights core causal chains, confidence, and cautions needed to avoid overgeneralizing from genomic prediction or non-bacterial systems.*

## 4. Recent developments and quantitative evidence, 2023–2024

### Environmental prevalence of lanthanide-dependent systems

A 2024 weathered-granite metagenomic study recovered **411 distinct XoxF-like sequences**: 340 XoxF3, 63 XoxF5, and eight unclassified XoxF sequences. No calcium-dependent MxaF representative was detected. This indicates unexpectedly broad genomic potential for lanthanide-dependent methanol oxidation in moderately weathered rock, but it remains environmental genomic evidence rather than direct demonstration that every carrier grows methylotrophically (voutsinos2024weatheredgranitesand pages 2-4). The authors also found XoxF-associated candidate transporters and metallophore clusters, while explicitly treating several proposed transport functions as hypotheses (voutsinos2024weatheredgranitesand pages 10-12).

### Diversity of type II methylotroph modules

A 2024 pangenomic study examined **75 organisms**. Methanol-dehydrogenase subunit I occurred in 73 genomes at an average of 3.16 copies, SHMT in 74 at 1.31 copies on average, serine–glyoxylate transaminase in all 75, and hydroxypyruvate reductase in all 75 with 22 isoforms. Only 10 genomes carried the formaldehyde-dehydrogenase class counted by that analysis. These values demonstrate pathway diversity and copy-number variation, not uniform biochemical activity (samanta2024fromgenometo pages 12-14). Only 15 of the 75 organisms carried the methane-monooxygenase inventory used by the authors to classify methane oxidation potential, reinforcing that methylotrophy is broader than methanotrophy (samanta2024fromgenometo pages 12-14).

### Formaldehyde stress and pathway plasticity

In *Methylobacterium* sp. XJLW exposed to formaldehyde, 2,888 genes differed significantly relative to methanol growth—1,423 upregulated and 1,465 downregulated. Resting cells were tested with 15 g L−1 formaldehyde, while methanol growth assays used 10 g L−1 methanol. The study suggests auxiliary stress metabolism, but its proposed RS27765-mediated direct assimilation route is not biochemically established: purified RS27765 did not reduce formaldehyde or methanol in vitro (shao2024transcriptomicdatareveals pages 7-9, shao2024transcriptomicdatareveals pages 2-4).

### Alternative respiratory ecology

The 2024 N2O-respiration study expands the known environmental conditions compatible with C1 oxidation. *M. tundrae* T4 encoded one MxaF and four XoxF-type MDHs, and functional N2O respiration allowed greater carbon oxidation and biomass under oxygen limitation. This is a valuable taxon-specific environmental modifier, not a defining methylotrophy mechanism (awala2024nitrousoxiderespiration pages 8-9, awala2024nitrousoxiderespiration pages 2-3).

## 5. Applications and real-world implementations

1. **C1 biomanufacturing:** methanol is an attractive renewable feedstock for fuels and chemicals. Natural or engineered methylotrophs combine MDH with RuMP, serine, or XuMP/DHA assimilation. PQQ-dependent systems can be difficult to transplant because functional MxaFI assembly requires numerous gene products and common hosts such as *E. coli* do not synthesize PQQ; NAD-dependent MDHs are therefore frequently favored in synthetic systems (le2021methanoldehydrogenasesas pages 4-6).
2. **Plant-associated agriculture:** pink-pigmented facultative methylotrophs use plant-emitted methanol in the phyllosphere and are associated with phytohormone production, stress tolerance, and plant growth. These applications are strain-level properties and should not be inferred from methylotrophy alone (alessa2021comprehensivecomparativegenomics pages 2-3).
3. **Rare-earth biotechnology:** XoxF biology has motivated REE biosensors, recovery, and separation strategies. Lanmodulin binds REEs with low-picomolar dissociation constants—about eight orders of magnitude more tightly than calcium in the reviewed measurements—making it relevant to biomining and recycling (DOI 10.1111/1751-7915.14503; June 2024) (rocha2024rareearthelements pages 2-5).
4. **Rock weathering and nutrient acquisition:** co-occurrence of XoxF systems, lanthanide-phosphate dissolution, and candidate metallophores suggests coupling between methylotrophy, REE acquisition, and phosphate availability in weathered granite. This is ecologically plausible but remains partly inferential (voutsinos2024weatheredgranitesand pages 2-4, voutsinos2024weatheredgranitesand pages 10-12).
5. **Greenhouse-gas management:** methanotrophic members of the broader methylotroph guild can convert methane, and selected strains can combine methane/C1 oxidation with N2O reduction. Such functions are promising for engineered emission mitigation but are not general properties of `METPO:1000651` (awala2024nitrousoxiderespiration pages 8-9).

## 6. Recommended graph architecture

For `methylotrophic_methanol_assimilation`, retain a compact high-confidence core:

1. methanol availability → methanol oxidation;
2. alternative enzyme branches: MxaFI + PQQ + Ca2+, XoxF + PQQ + lanthanide, or taxon-specific NAD-MDH;
3. methanol oxidation → formaldehyde/C1 intermediate;
4. formaldehyde partition → assimilatory branch and dissimilatory H4MPT/formate branch;
5. assimilation alternatives → RuMP or serine cycle, with EMC/glyoxylate regeneration as appropriate;
6. dissimilation → formate oxidation → reducing equivalents/respiratory energy;
7. assimilated carbon + conserved energy → biomass and growth on methanol;
8. formaldehyde stress/detoxification → modifier nodes rather than trait-defining endpoints.

A second substrate module should represent methylamine:

**methylamine → MaDH or NMG pathway → formaldehyde/C1 transfer + ammonium → H4MPT oxidation and serine-cycle assimilation → growth**, with an explicit distinction between methylamine as carbon/energy and as nitrogen only.

## 7. Claims not yet ready for TraitMech curation

- **Do not equate `xoxF` presence with methylotrophy.** XoxF-like enzymes occur in non-methylotrophs and may oxidize multicarbon alcohols.
- **Do not assert that all XoxF enzymes produce the same immediate product.** Formaldehyde and formate assignments vary across enzyme clades and assay conditions.
- **Do not curate candidate NRAMP or MscS proteins as lanthanide transporters.** Their roles in the 2024 environmental study were inferred from conserved co-occurrence, not experimentally established (voutsinos2024weatheredgranitesand pages 10-12).
- **Do not curate RS27765 as a methanol-assimilation enzyme or direct bypass.** The double-mutant phenotype warrants investigation, but docking is not reaction evidence and purified protein lacked the proposed activity (shao2024transcriptomicdatareveals pages 7-9).
- **Do not treat glutathione-dependent formaldehyde oxidation as diagnostic.** It can be a general detoxification mechanism.
- **Do not generalize N2O respiration, lanthanide-switch regulation, EMC dependence, or NMG regulation across methylotrophs.** Each is strongly taxon- and condition-dependent.
- **Do not include AOX/peroxisomal XuMP edges in a bacteria-only graph.** They are appropriate only if the trait graph intentionally spans methylotrophic yeasts.
- **Do not convert pangenomic presence/absence counts into proven physiological edges.** Gene inventories require expression, biochemical, isotope, or growth validation.

## DOI-first bibliography

1. Chistoserdova L, Kalyuzhnaya MG. **Current Trends in Methylotrophy.** *Trends in Microbiology*. Published August 2018. DOI: [10.1016/j.tim.2018.01.011](https://doi.org/10.1016/j.tim.2018.01.011). (chistoserdova2018currenttrendsin pages 3-4, chistoserdova2018currenttrendsin pages 2-3)
2. Samanta D, et al. **From genome to evolution: investigating type II methylotrophs using a pangenomic analysis.** *mSystems*. Published June 2024. DOI: [10.1128/msystems.00248-24](https://doi.org/10.1128/msystems.00248-24). (samanta2024fromgenometo pages 18-20, samanta2024fromgenometo pages 12-14)
3. Voutsinos MY, et al. **Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes.** *BMC Biology*. Published February 2024. DOI: [10.1186/s12915-024-01841-0](https://doi.org/10.1186/s12915-024-01841-0). (voutsinos2024weatheredgranitesand pages 2-4, voutsinos2024weatheredgranitesand pages 10-12)
4. Shao Y, et al. **Transcriptomic data reveals an auxiliary detoxification mechanism that alleviates formaldehyde stress in Methylobacterium sp. XJLW.** *BMC Genomics*. Published October 2024. DOI: [10.1186/s12864-024-10923-w](https://doi.org/10.1186/s12864-024-10923-w). (shao2024transcriptomicdatareveals pages 7-9, shao2024transcriptomicdatareveals pages 2-4)
5. Awala SI, et al. **Nitrous oxide respiration in acidophilic methanotrophs.** *Nature Communications*. Published May 2024. DOI: [10.1038/s41467-024-48161-z](https://doi.org/10.1038/s41467-024-48161-z). (awala2024nitrousoxiderespiration pages 8-9, awala2024nitrousoxiderespiration pages 2-3)
6. Rocha RA, Alexandrov K, Scott C. **Rare earth elements in biology: From biochemical curiosity to solutions for extractive industries.** *Microbial Biotechnology*. Published June 2024. DOI: [10.1111/1751-7915.14503](https://doi.org/10.1111/1751-7915.14503). (rocha2024rareearthelements pages 2-5)
7. Le T-K, et al. **Methanol Dehydrogenases as Key Biocatalysts for Synthetic Methylotrophy.** *Frontiers in Bioengineering and Biotechnology*. Published December 2021. DOI: [10.3389/fbioe.2021.787791](https://doi.org/10.3389/fbioe.2021.787791). (le2021methanoldehydrogenasesas pages 4-6, le2021methanoldehydrogenasesas pages 2-3)
8. Alessa O, et al. **Comprehensive Comparative Genomics and Phenotyping of Methylobacterium Species.** *Frontiers in Microbiology*. Published October 2021. DOI: [10.3389/fmicb.2021.740610](https://doi.org/10.3389/fmicb.2021.740610). (alessa2021comprehensivecomparativegenomics pages 2-3, alessa2021comprehensivecomparativegenomics pages 10-11)
9. Wegner C-E, et al. **Lanthanide-Dependent Methylotrophs of the Family Beijerinckiaceae: Physiological and Genomic Insights.** *Applied and Environmental Microbiology*. Published online December 2019; January 2020 issue. DOI: [10.1128/AEM.01830-19](https://doi.org/10.1128/AEM.01830-19). (wegner2019lanthanidedependentmethylotrophsof pages 8-9, wegner2019lanthanidedependentmethylotrophsof pages 2-3, wegner2019lanthanidedependentmethylotrophsof pages 12-13)
10. Nayak DD, et al. **Selection Maintains Apparently Degenerate Metabolic Pathways due to Tradeoffs in Using Methylamine for Carbon versus Nitrogen.** *Current Biology*. Published June 2016. DOI: [10.1016/j.cub.2016.04.029](https://doi.org/10.1016/j.cub.2016.04.029). (nayak2016selectionmaintainsapparently pages 4-6, nayak2016selectionmaintainsapparently pages 3-4, nayak2016selectionmaintainsapparently pages 8-9)

References

1. (chistoserdova2018currenttrendsin pages 3-4): Ludmila Chistoserdova and Marina G. Kalyuzhnaya. Current trends in methylotrophy. Trends in microbiology, 26 8:703-714, Aug 2018. URL: https://doi.org/10.1016/j.tim.2018.01.011, doi:10.1016/j.tim.2018.01.011. This article has 202 citations and is from a domain leading peer-reviewed journal.

2. (chistoserdova2018currenttrendsin pages 2-3): Ludmila Chistoserdova and Marina G. Kalyuzhnaya. Current trends in methylotrophy. Trends in microbiology, 26 8:703-714, Aug 2018. URL: https://doi.org/10.1016/j.tim.2018.01.011, doi:10.1016/j.tim.2018.01.011. This article has 202 citations and is from a domain leading peer-reviewed journal.

3. (wegner2019lanthanidedependentmethylotrophsof pages 2-3): Carl-Eric Wegner, Linda Gorniak, Stefan Riedel, Martin Westermann, and Kirsten Küsel. Lanthanide-dependent methylotrophs of the family <i>beijerinckiaceae</i> : physiological and genomic insights. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01830-19, doi:10.1128/aem.01830-19. This article has 50 citations and is from a peer-reviewed journal.

4. (nayak2016selectionmaintainsapparently pages 8-9): Dipti D. Nayak, Deepa Agashe, Ming-Chun Lee, and Christopher J. Marx. Selection maintains apparently degenerate metabolic pathways due to tradeoffs in using methylamine for carbon versus nitrogen. Current Biology, 26:1416-1426, Jun 2016. URL: https://doi.org/10.1016/j.cub.2016.04.029, doi:10.1016/j.cub.2016.04.029. This article has 25 citations and is from a highest quality peer-reviewed journal.

5. (voutsinos2024weatheredgranitesand pages 2-4): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 15 citations and is from a domain leading peer-reviewed journal.

6. (le2021methanoldehydrogenasesas pages 2-3): Thien-Kim Le, Yu-Jin Lee, Gui Hwan Han, and Soo-Jin Yeom. Methanol dehydrogenases as a key biocatalysts for synthetic methylotrophy. Frontiers in Bioengineering and Biotechnology, Dec 2021. URL: https://doi.org/10.3389/fbioe.2021.787791, doi:10.3389/fbioe.2021.787791. This article has 60 citations.

7. (samanta2024fromgenometo pages 18-20): Dipayan Samanta, Shailabh Rauniyar, Priya Saxena, and Rajesh K. Sani. From genome to evolution: investigating type ii methylotrophs using a pangenomic analysis. Jun 2024. URL: https://doi.org/10.1128/msystems.00248-24, doi:10.1128/msystems.00248-24. This article has 11 citations and is from a peer-reviewed journal.

8. (le2021methanoldehydrogenasesas pages 4-6): Thien-Kim Le, Yu-Jin Lee, Gui Hwan Han, and Soo-Jin Yeom. Methanol dehydrogenases as a key biocatalysts for synthetic methylotrophy. Frontiers in Bioengineering and Biotechnology, Dec 2021. URL: https://doi.org/10.3389/fbioe.2021.787791, doi:10.3389/fbioe.2021.787791. This article has 60 citations.

9. (wegner2019lanthanidedependentmethylotrophsof pages 8-9): Carl-Eric Wegner, Linda Gorniak, Stefan Riedel, Martin Westermann, and Kirsten Küsel. Lanthanide-dependent methylotrophs of the family <i>beijerinckiaceae</i> : physiological and genomic insights. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01830-19, doi:10.1128/aem.01830-19. This article has 50 citations and is from a peer-reviewed journal.

10. (wegner2019lanthanidedependentmethylotrophsof pages 12-13): Carl-Eric Wegner, Linda Gorniak, Stefan Riedel, Martin Westermann, and Kirsten Küsel. Lanthanide-dependent methylotrophs of the family <i>beijerinckiaceae</i> : physiological and genomic insights. Applied and Environmental Microbiology, Dec 2019. URL: https://doi.org/10.1128/aem.01830-19, doi:10.1128/aem.01830-19. This article has 50 citations and is from a peer-reviewed journal.

11. (nayak2016selectionmaintainsapparently pages 3-4): Dipti D. Nayak, Deepa Agashe, Ming-Chun Lee, and Christopher J. Marx. Selection maintains apparently degenerate metabolic pathways due to tradeoffs in using methylamine for carbon versus nitrogen. Current Biology, 26:1416-1426, Jun 2016. URL: https://doi.org/10.1016/j.cub.2016.04.029, doi:10.1016/j.cub.2016.04.029. This article has 25 citations and is from a highest quality peer-reviewed journal.

12. (nayak2016selectionmaintainsapparently pages 4-6): Dipti D. Nayak, Deepa Agashe, Ming-Chun Lee, and Christopher J. Marx. Selection maintains apparently degenerate metabolic pathways due to tradeoffs in using methylamine for carbon versus nitrogen. Current Biology, 26:1416-1426, Jun 2016. URL: https://doi.org/10.1016/j.cub.2016.04.029, doi:10.1016/j.cub.2016.04.029. This article has 25 citations and is from a highest quality peer-reviewed journal.

13. (shao2024transcriptomicdatareveals pages 2-4): Yunhai Shao, Shuang Li, Yanxin Wang, Pei Qiao, and Weihong Zhong. Transcriptomic data reveals an auxiliary detoxification mechanism that alleviates formaldehyde stress in methylobacterium sp. xjlw. BMC Genomics, Oct 2024. URL: https://doi.org/10.1186/s12864-024-10923-w, doi:10.1186/s12864-024-10923-w. This article has 7 citations and is from a peer-reviewed journal.

14. (shao2024transcriptomicdatareveals pages 7-9): Yunhai Shao, Shuang Li, Yanxin Wang, Pei Qiao, and Weihong Zhong. Transcriptomic data reveals an auxiliary detoxification mechanism that alleviates formaldehyde stress in methylobacterium sp. xjlw. BMC Genomics, Oct 2024. URL: https://doi.org/10.1186/s12864-024-10923-w, doi:10.1186/s12864-024-10923-w. This article has 7 citations and is from a peer-reviewed journal.

15. (awala2024nitrousoxiderespiration pages 8-9): Samuel Imisi Awala, Joo-Han Gwak, Yongman Kim, Man-Young Jung, Peter. F. Dunfield, Michael Wagner, and Sung-Keun Rhee. Nitrous oxide respiration in acidophilic methanotrophs. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-48161-z, doi:10.1038/s41467-024-48161-z. This article has 33 citations and is from a highest quality peer-reviewed journal.

16. (rocha2024rareearthelements pages 2-5): Raquel A. Rocha, Kirill Alexandrov, and Colin Scott. Rare earth elements in biology: from biochemical curiosity to solutions for extractive industries. Microbial Biotechnology, Jun 2024. URL: https://doi.org/10.1111/1751-7915.14503, doi:10.1111/1751-7915.14503. This article has 27 citations and is from a peer-reviewed journal.

17. (samanta2024fromgenometo pages 12-14): Dipayan Samanta, Shailabh Rauniyar, Priya Saxena, and Rajesh K. Sani. From genome to evolution: investigating type ii methylotrophs using a pangenomic analysis. Jun 2024. URL: https://doi.org/10.1128/msystems.00248-24, doi:10.1128/msystems.00248-24. This article has 11 citations and is from a peer-reviewed journal.

18. (alessa2021comprehensivecomparativegenomics pages 10-11): Ola Alessa, Yoshitoshi Ogura, Yoshiko Fujitani, Hideto Takami, Tetsuya Hayashi, Nurettin Sahin, and Akio Tani. Comprehensive comparative genomics and phenotyping of methylobacterium species. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.740610, doi:10.3389/fmicb.2021.740610. This article has 61 citations and is from a peer-reviewed journal.

19. (voutsinos2024weatheredgranitesand pages 10-12): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 15 citations and is from a domain leading peer-reviewed journal.

20. (awala2024nitrousoxiderespiration pages 2-3): Samuel Imisi Awala, Joo-Han Gwak, Yongman Kim, Man-Young Jung, Peter. F. Dunfield, Michael Wagner, and Sung-Keun Rhee. Nitrous oxide respiration in acidophilic methanotrophs. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-48161-z, doi:10.1038/s41467-024-48161-z. This article has 33 citations and is from a highest quality peer-reviewed journal.

21. (alessa2021comprehensivecomparativegenomics pages 2-3): Ola Alessa, Yoshitoshi Ogura, Yoshiko Fujitani, Hideto Takami, Tetsuya Hayashi, Nurettin Sahin, and Akio Tani. Comprehensive comparative genomics and phenotyping of methylobacterium species. Frontiers in Microbiology, Oct 2021. URL: https://doi.org/10.3389/fmicb.2021.740610, doi:10.3389/fmicb.2021.740610. This article has 61 citations and is from a peer-reviewed journal.