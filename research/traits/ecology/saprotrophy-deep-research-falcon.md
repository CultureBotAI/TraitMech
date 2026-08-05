---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:43:57.206831'
end_time: '2026-08-03T23:50:00.978925'
duration_seconds: 363.77
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: saprotrophy
  trait_identifier: traitmech:000055
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: saprotrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic-ecology lifestyle in which an organism feeds on dead or decaying
    organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
  parent_traits: METPO:1000059
  synonyms: decomposer, saprophytic
  evidence_summary: 'DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial
    control over carbon cycling in soil", support microbial decomposition of organic
    matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer
    supports decomposer/saprotrophic activity as a key function of soil microbial
    communities.)'
  causal_graph_summary: 'saprotrophy_decomposition_cycling: 14 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** saprotrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000055
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which an organism feeds on dead or decaying organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
- **Parent traits:** METPO:1000059
- **Synonyms:** decomposer, saprophytic
- **Existing evidence:** DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial control over carbon cycling in soil", support microbial decomposition of organic matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports decomposer/saprotrophic activity as a key function of soil microbial communities.)
- **Existing causal graph summary:** saprotrophy_decomposition_cycling: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **saprotrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/saprotrophy.yaml`.

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
- **Trait label:** saprotrophy
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000055
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic-ecology lifestyle in which an organism feeds on dead or decaying organic matter, mineralizing it and driving carbon and nutrient cycling (decomposition).
- **Parent traits:** METPO:1000059
- **Synonyms:** decomposer, saprophytic
- **Existing evidence:** DOI:10.3389/fmicb.2012.00348:  (Schimel & Schaeffer, "Microbial control over carbon cycling in soil", support microbial decomposition of organic matter as a central ecosystem process.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports decomposer/saprotrophic activity as a key function of soil microbial communities.)
- **Existing causal graph summary:** saprotrophy_decomposition_cycling: 14 nodes, 9 edges

## Research Objective

Research the microbial trait **saprotrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/saprotrophy.yaml`.

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


# Curation report: microbial saprotrophy

## Record and scope

- **Trait:** saprotrophy
- **Identifier:** `traitmech:000055`
- **Category / term kind / status:** ECOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000059`
- **Synonyms:** decomposer; saprophytic

Saprotrophy is best represented as an **ecological nutritional lifestyle**, not as one enzyme, pathway, assay result, or taxonomic attribute. Its defining phenotype is acquisition of carbon, energy, and nutrients from **nonliving organic matter**, usually through extracellular depolymerization followed by uptake and catabolism of soluble products. Relevant substrates include dead wood, litter, soil organic matter, microbial necromass, detritus, and—in context—dead animal material. Saprotrophs consequently mediate decomposition and carbon/nutrient recycling. This formulation closely follows the expert fungal-trait synthesis describing saprotrophs as degraders of dead organic matter and ecosystem “biochemical engineers.” (zanne2020fungalfunctionalecology pages 15-16)

### Boundaries

1. **Necrotroph versus saprotroph:** a necrotroph kills living host tissue and then consumes it; a saprotroph consumes material already dead. Shared plant-cell-wall-degrading enzymes do not prove which process occurred. Some fungi switch between pathogenic and saprotrophic phases, so lifestyle assertions should be qualified by substrate state and experimental context. (zanne2020fungalfunctionalecology pages 15-16)
2. **Biotroph, mutualist, or endophyte:** these interact nutritionally or asymptomatically with living hosts. Endophytes are specifically distinguished from saprotrophs by colonization of living, asymptomatic tissues, although an organism may later become saprotrophic after tissue senescence. (christian2024plantendophytecommunicationscaling pages 12-13)
3. **Fibrolysis versus saprotrophy:** polymer degradation in a herbivore gut is mechanistically relevant, but the substrate is part of an active host digestive system. Such evidence supports enzyme/module edges, not necessarily ecological assignment of the organism as a free-living saprotroph.
4. **Genomic potential versus phenotype:** CAZyme counts predict degradative capacity but do not establish enzyme secretion, substrate loss, assimilation, or mineralization. Expression, secretome, activity, mass-loss, isotope-tracing, or growth evidence is preferable.
5. **Not restricted to fungi:** bacteria and other microorganisms can use dead organic matter. Fungal mechanisms dominate the retrieved evidence and should not be generalized automatically to all microbial taxa.

## Recommended core causal model

A conservative graph should represent this sequence:

**dead organic matter → substrate sensing/induction → extracellular enzyme production and secretion → oxidative and/or hydrolytic depolymerization → soluble monomers/oligomers → transport and assimilation → central metabolism and respiration/biomass → carbon and nutrient cycling.**

Regulatory and environmental branches should modify individual steps rather than define the trait. Carbon catabolite repression regulates lignocellulose-degrading machinery; substrate chemistry, mineral surfaces, and community composition alter the partitioning of processed carbon between respiration, biomass, and stabilized soil organic matter. (gurovic2023regulationoflignocellulose pages 2-3, elias2024microbialandmineral pages 1-2, elias2024microbialandmineral pages 12-13)

## Candidate nodes grouped by type

### Trait, process, and localization nodes

- `traitmech:000055` — saprotrophy.
- `METPO:1000059` — supplied parent trait.
- Decomposition; extracellular digestion; lignocellulose degradation; cellulose catabolism; hemicellulose catabolism; pectin catabolism; lignin oxidation; carbohydrate transport; aerobic respiration; fermentation; carbon mineralization; nutrient mineralization; microbial biomass formation.
- **GO candidates:** `GO:0005576` extracellular region; `GO:0005975` carbohydrate metabolic process; `GO:0030245` cellulose catabolic process; `GO:0046274` lignin catabolic process; `GO:0006096` glycolytic process; `GO:0006119` oxidative phosphorylation. Identifier-to-edge fit should be checked against the current GO release before YAML insertion.

### Environmental and experimental nodes

- Dead organic matter; plant litter; dead wood; cellulose; hemicellulose; xylan; pectin; lignin; chitin; starch; soil organic matter; microbial necromass.
- Soil; forest soil; leaf litter; woody debris; compost; anaerobic gut; sawdust-amended medium.
- Temperature, water availability, oxygen availability, pH, nitrogen availability, litter quality, mineral surface area/charge, substrate accessibility, incubation time.
- Enzyme-activity assay, secretomics, transcriptomics, genomics/CAZyme annotation, substrate mass loss, growth on polymer, metabolomics, and ^13C isotope tracing.

### Enzymes, proteins, and complexes

- Cellobiohydrolase, endoglucanase, β-glucosidase.
- Xylanase/endo-xylanase, hemicellulase, polygalacturonase, pectinase.
- Laccase, lignin peroxidase, manganese peroxidase.
- Lytic polysaccharide monooxygenase (LPMO; fungal AA families in the cited *Crucibulum* experiment).
- GMC oxidoreductases/AA3, AA7 oxidoreductases, carbohydrate-binding modules.
- Carbohydrate esterases CE4/CE16; expansin- or loosenin-like proteins.
- Cellulosome—particularly relevant to anaerobic fungi and bacteria.
- Secretory pathway and sugar/oligosaccharide transporters are important candidate modules, but no transporter-specific edge in the retrieved evidence is sufficiently grounded for direct curation.

### Chemicals and metabolites

- `CHEBI:17234` glucose; cellobiose; xylose; arabinose; galacturonic acid; gluconic acid; short-chain fatty acids; carbon dioxide; water; oxygen.
- LPMO reductants/electron donors: ascorbate, cysteine, glutathione, gallic acid, phenolic mediators, and AA3/AA7 redox partners. The *Crucibulum laeve* study specifically supports electron-donor dependence in an oxidative lignocellulose system. (shabaev2024saprotrophicwooddecay pages 14-16)
- Mineral-associated organic matter and microbial necromass should be ecosystem-output nodes, not intrinsic components of the saprotrophic phenotype.

### Regulatory modules

- Carbon catabolite repression (CCR).
- Substrate induction of lignocellulolytic genes.
- Transcriptional regulation, anti-sigma-factor systems, regulatory RNAs, unfolded-protein response, pH response, and nitrogen-use regulation.
- Only CCR has sufficiently direct support in the retrieved evidence set for a provisional graph edge; other regulatory modules require organism-specific primary evidence. (gurovic2023regulationoflignocellulose pages 2-3)

## Candidate causal edges

The following table is designed for direct review during construction of `data/traits/ecology/saprotrophy.yaml`.

| subject | predicate | object | confidence/scope | DOI evidence | short supporting snippet | curator note |
|---|---|---|---|---|---|---|
| dead organic matter | enables | saprotrophy | High; broad fungal ecology definition | 10.1111/brv.12570; 10.1080/00275514.2023.2299658 | Saprotrophs consume or degrade dead plant material and other dead organic matter rather than living host tissue. (zanne2020fungalfunctionalecology pages 15-16, christian2024plantendophytecommunicationscaling pages 12-13) | Good scope edge for trait definition; keep distinct from necrotrophy, endophytism, and biotrophy. |
| secreted cellulase/xylanase/pectinase activity | depolymerizes | plant cell wall polysaccharides | Moderate; broad but enzyme classes summarized mostly in reviews | 10.1080/00275514.2023.2299658; 10.1186/s42523-022-00224-6 | Reviews summarize cellulases, xylanases, pectinases and related CAZymes acting on cellulose, hemicellulose, and pectin during saprotrophic decomposition. (christian2024plantendophytecommunicationscaling pages 12-13, wunderlich2023understandingthemicrobial pages 4-6) | Curate as enzyme-class level, not universal gene presence in all saprotrophs. |
| cellobiohydrolase + endoglucanase + beta-glucosidase | converts | cellulose to glucose | High; general microbial lignocellulose mechanism | 10.1093/jambio/lxac002 | Cellulose is degraded by the concerted action of cellobiohydrolases, endoglucanases, and beta-glucosidases into glucose. (gurovic2023regulationoflignocellulose pages 2-3) | Strong mechanistic edge; applicable to many lignocellulose degraders, not only fungi. |
| manganese peroxidase / lignin peroxidase / laccase | oxidizes | lignin | High; classic fungal ligninolysis | 10.1093/jambio/lxac002 | Lignin requires fungal ligninolytic enzymes including MnP, LiP, and laccases that catalyze oxidative reactions. (gurovic2023regulationoflignocellulose pages 2-3) | Suitable as pathway edge for lignin-degrading saprotrophs; not all saprotrophs attack lignin. |
| lytic polysaccharide monooxygenase (LPMO) | oxidatively cleaves | polysaccharides in lignocellulose | Moderate; strong but taxon-specific experimental support | 10.3390/jof11010021 | Crucibulum laeve uses LPMOs among its oxidative machinery targeting cellulose and related wall polymers. (shabaev2024saprotrophicwooddecay pages 14-16) | Mark taxon-specific unless broader LPMO saprotrophy evidence is added. |
| electron donors / redox partner CAZymes | enables | LPMO activity | Moderate; biochemical mechanism shown in white-rot system | 10.3390/jof11010021 | Reported electron donors include small organic molecules and enzymatic redox partners such as AA3/AA7 enzymes for LPMO function. (shabaev2024saprotrophicwooddecay pages 14-16) | Keep as biochemical support edge; currently based on fungal experimental system. |
| expansin-like protein | loosens | lignocellulosic substrate | Moderate; taxon-specific | 10.3390/jof11010021 | Expansin-like proteins are described as non-enzymatically loosening lignocellulosic substrates. (shabaev2024saprotrophicwooddecay pages 14-16) | Useful candidate node, but evidence is organism-specific and should be flagged uncertain. |
| cellulosome | promotes | lignocellulose breakdown | Moderate; anaerobic gut fungi/bacteria context | 10.1186/s42523-022-00224-6 | Some anaerobic fungi and bacteria possess cellulosomes, multi-enzyme complexes that enhance plant fiber breakdown. (wunderlich2023understandingthemicrobial pages 11-12, wunderlich2023understandingthemicrobial pages 4-6) | Strong for anaerobic fibrolytic consortia; not a universal saprotroph feature. |
| carbon catabolite repression | inhibits | cellulolytic/lignocellulolytic gene expression | Moderate; broad regulatory review, not trait-specific direct assay here | 10.1093/jambio/lxac002 | The review identifies carbon catabolite repression as a major regulatory pathway controlling lignocellulose degradation. (gurovic2023regulationoflignocellulose pages 2-3) | Curate conservatively as regulation of degradation machinery; direct inhibitory edge may need organism-level follow-up. |
| extracellular depolymerization products (e.g., glucose, other monomers) | enables | uptake and assimilation | Low-Moderate; inferred from degradation-to-growth logic | 10.1093/jambio/lxac002; 10.3390/jof11010021 | Sources link polymer breakdown to glucose production and catabolism of released acids/sugars in saprotrophic growth. (gurovic2023regulationoflignocellulose pages 2-3, shabaev2024saprotrophicwooddecay pages 14-16) | Mechanistically plausible but indirect in retrieved evidence; flag as inferred unless transporter-specific data are added. |
| saprotrophy | recycles | carbon and nutrients | High; ecosystem function definition | 10.1111/brv.12570; 10.1038/nrmicro.2017.87 | Saprotrophs function as decay agents and biochemical engineers that recycle carbon and nutrients through ecosystems. (zanne2020fungalfunctionalecology pages 15-16) | Good high-level ecology edge; broad and appropriate for trait summary rather than molecular subgraph. |
| litter quality | affects | microbial carbon-use efficiency (CUE) | Moderate; soil ecosystem experiment | 10.1038/s41467-024-54446-0 | High-quality litter was associated with lower microbial CUE in the 13C tracing soil study. (elias2024microbialandmineral pages 1-2, elias2024microbialandmineral pages 12-13) | Soil-specific systems edge; not intrinsic to all saprotrophs. Use environmental-context qualifier. |
| soil mineralogy | affects | mineral-associated organic matter (MAOM) formation | Moderate; soil ecosystem experiment | 10.1038/s41467-024-54446-0 | The 2024 study concluded mineralogy was the primary control on mineral-associated SOC/MAOM formation efficiency. (elias2024microbialandmineral pages 1-2, elias2024microbialandmineral pages 12-13) | Valuable ecosystem edge, but it links saprotrophic processing to soil C stabilization rather than defining the trait itself. |


*Table: This table summarizes conservative candidate causal edges for traitmech:000055 saprotrophy, using only evidence already gathered. It is designed to support TraitMech curation by separating broadly supported mechanisms from taxon-specific or ecosystem-inferred edges.*

### Priority edges for immediate curation

The strongest molecular core is: **cellobiohydrolase/endoglucanase/β-glucosidase → cellulose-to-glucose conversion**, and **MnP/LiP/laccase → lignin oxidation**. A 2023 regulatory review explicitly reports concerted cellulose hydrolysis to glucose and oxidative lignin reactions by these enzymes. (gurovic2023regulationoflignocellulose pages 2-3)

A second high-value module is extracellular CAZyme-mediated depolymerization. Recent work identifies cellulases, xylanases, pectinases, laccases, lipolytic enzymes, and proteases in decomposition contexts, while also showing temporal niche differentiation between early users of labile compounds and later decomposers of recalcitrant material. (christian2024plantendophytecommunicationscaling pages 12-13)

For white-rot wood decay, LPMOs, laccases, AA3/AA7 oxidoreductases, esterases, and expansin-like proteins constitute a defensible taxon-specific oxidative module. The cited *C. laeve* experiment also found substrate-dependent secretion and highlighted electron donors and redox partners required for LPMO activity. These edges should carry a white-rot or organism-specific qualifier rather than be treated as universal saprotrophy. (shabaev2024saprotrophicwooddecay pages 14-16)

## Recent research and quantitative findings

### Enzyme-system diversity

A 2023 synthesis of equine hindgut fibrolysis reported **137 distinct CAZymes** in fecal gene catalogues, with **85.4%** assigned to glycoside hydrolases or polysaccharide lyases. Anaerobic fungal genomes were reported to encode approximately **200–300 CAZyme genes**. In ruminant systems, Neocallimastigomycota degraded **18–63% of untreated plant biomass** despite representing about **8% of microbiota biomass**. These figures demonstrate the potency of coordinated extracellular depolymerization, but they are gut- and taxon-specific and should not define saprotrophy globally. (wunderlich2023understandingthemicrobial pages 4-6)

Cellulosomes provide a complementary strategy: multi-enzyme complexes concentrate cellulolytic activities at the substrate surface. Carbohydrate-binding modules improve substrate attachment and enzyme–substrate proximity; methanogens can indirectly facilitate anaerobic fiber degradation by maintaining low hydrogen partial pressure. These are community-context mechanisms rather than universal trait requirements. (wunderlich2023understandingthemicrobial pages 11-12, wunderlich2023understandingthemicrobial pages 4-6)

### Soil-carbon research

A 2024 ^13C-litter tracing study revised a common assumption about decomposition and carbon stabilization. High-quality litter produced **less efficient mineral-associated soil organic-carbon formation**, associated with microbial community shifts and lower carbon-use efficiency; low-quality litter enhanced loss of pre-existing soil carbon; and mineralogy was the primary control of mineral-associated organic-carbon formation. Mineral surface area and charge can regulate microbial access to organic matter and decomposition. (elias2024microbialandmineral pages 1-2)

The study defined microbial carbon-use efficiency as litter carbon recovered in microbial biomass divided by litter carbon in biomass plus respiration. Mineral-associated organic-matter formation efficiency was litter carbon recovered in that pool divided by total processed litter carbon. These operational definitions are useful graph nodes because they distinguish decomposition rate from the eventual fate of carbon. (elias2024microbialandmineral pages 12-13)

### Current expert interpretation

The evidence supports treating saprotrophy as a **system-level strategy assembled from partially substitutable mechanisms**. Some organisms rely heavily on hydrolytic CAZymes; white-rot fungi add oxidative ligninolysis; anaerobic degraders may use cellulosomes and syntrophic hydrogen transfer. Therefore, no single CAZyme, CAZyme count, or lignin-degrading enzyme is necessary and sufficient for the trait. The trait should be inferred most strongly when dead-substrate use, extracellular depolymerization, uptake/assimilation, and growth or mineralization are observed together. This is consistent with trait-based fungal ecology, which also emphasizes polyphyly and substantial gaps between taxonomy, genomic potential, and function. (zanne2020fungalfunctionalecology pages 15-16)

## Current applications and implementations

1. **Composting and residue conversion:** selection or management of cellulolytic, hemicellulolytic, and ligninolytic communities accelerates conversion of crop residues and organic wastes. Graph transfer is strongest at enzyme and substrate edges; field performance also depends on aeration, moisture, temperature, nutrient balance, and community succession.
2. **Biorefining and enzyme discovery:** cellulases, xylanases, pectinases, laccases, peroxidases, LPMOs, and cellulosomes are targets for lignocellulosic biomass pretreatment and saccharification. The *C. laeve* secretome illustrates discovery of oxidative enzyme combinations and accessory substrate-loosening proteins. (shabaev2024saprotrophicwooddecay pages 14-16)
3. **Animal nutrition:** anaerobic fungal and bacterial fibrolysis releases fermentable products and short-chain fatty acids from plant fiber. CAZyme profiling and functional assays are being used to characterize these consortia, although gut fibrolysis should remain a contextual child mechanism rather than the trait definition. (wunderlich2023understandingthemicrobial pages 11-12, wunderlich2023understandingthemicrobial pages 4-6)
4. **Soil-carbon and climate models:** decomposition, microbial CUE, respiration, necromass production, and mineral stabilization determine whether litter carbon is returned as CO₂, retained in biomass, or stabilized as mineral-associated organic matter. The 2024 isotope study shows why litter quality alone is insufficient to predict storage. (elias2024microbialandmineral pages 1-2, elias2024microbialandmineral pages 12-13)
5. **Functional annotation and ecological monitoring:** metagenomes, transcriptomes, secretomes, and enzyme assays can detect decomposer potential and activity. Expert reviews caution that taxonomic or gene-presence inference should be validated with functional measurements. (zanne2020fungalfunctionalecology pages 15-16, wunderlich2023understandingthemicrobial pages 11-12)

## Warnings: claims not yet ready for TraitMech curation

- **Do not curate “CAZyme abundance causes saprotrophy.”** CAZyme repertoires are neither exclusive to saprotrophs nor proof of expressed activity.
- **Do not make lignin degradation universal.** Many saprotrophs consume labile compounds, proteins, lipids, cellulose, or pectin without substantial ligninolysis.
- **Do not equate necrotrophy with saprotrophy.** Killing living tissue is a pathogenic mechanism; consumption of already dead material is the defining saprotrophic condition. (zanne2020fungalfunctionalecology pages 15-16)
- **Do not curate named sugar transporters without direct evidence.** The retrieved studies support monomer production and subsequent metabolism only indirectly; transporter identity and directionality remain unresolved.
- **Treat CCR as provisional at the trait level.** It is widely described in lignocellulose-degrading bacteria, yeasts, and filamentous fungi, but the exact regulator and sign depend on organism and carbon source. (gurovic2023regulationoflignocellulose pages 2-3)
- **Qualify LPMO, expansin-like protein, AA3/AA7, and absent GH-family claims as taxon-specific.** Current direct support here comes primarily from *C. laeve*. (shabaev2024saprotrophicwooddecay pages 14-16)
- **Qualify cellulosomes and methanogen facilitation as anaerobic-community specific.** They should not be attached to all saprotrophs. (wunderlich2023understandingthemicrobial pages 11-12, wunderlich2023understandingthemicrobial pages 4-6)
- **Do not collapse decomposition into carbon sequestration.** Saprotrophic processing can increase respiration, biomass, necromass, or mineral-associated carbon; substrate quality and mineralogy change this partitioning. (elias2024microbialandmineral pages 1-2, elias2024microbialandmineral pages 12-13)
- **Moisture, temperature, oxygen, pH, and nitrogen edges require additional primary experiments.** They are plausible major controls but were not supported with sufficiently direct, extractable causal evidence in the present retrieval set.
- **Verify all ontology identifiers before merge.** CAZy family names such as AA9 or GH5 are database classifications, not GO or EC identifiers; individual proteins require species/strain-specific UniProt accessions.

## DOI-first bibliography

1. Shabaev AV, Savinova OS, Moiseenko KV, Glazunova OA, Fedorova TV. “Saprotrophic Wood Decay Ability and Plant Cell Wall Degrading Enzyme System of the White Rot Fungus *Crucibulum laeve*.” *Journal of Fungi*. Published December 2024 (volume issue dated 2025). DOI: [10.3390/jof11010021](https://doi.org/10.3390/jof11010021). (shabaev2024saprotrophicwooddecay pages 14-16)
2. Elias DMO et al. “Microbial and mineral interactions decouple litter quality from soil organic matter formation.” *Nature Communications*. Published November 2024. DOI: [10.1038/s41467-024-54446-0](https://doi.org/10.1038/s41467-024-54446-0). (elias2024microbialandmineral pages 1-2, elias2024microbialandmineral pages 12-13)
3. Christian N, Perlin MH. “Plant-endophyte communication: Scaling from molecular mechanisms to ecological outcomes.” *Mycologia*. Published February 2024. DOI: [10.1080/00275514.2023.2299658](https://doi.org/10.1080/00275514.2023.2299658). (christian2024plantendophytecommunicationscaling pages 12-13)
4. Gurovic MSV, Viceconte FR, Bidegain MA, Dietrich J. “Regulation of lignocellulose degradation in microorganisms.” *Journal of Applied Microbiology*. Published 2023. DOI: [10.1093/jambio/lxac002](https://doi.org/10.1093/jambio/lxac002). (gurovic2023regulationoflignocellulose pages 2-3)
5. Wunderlich G, Bull M, Ross T, Rose M, Chapman B. “Understanding the microbial fibre degrading communities & processes in the equine gut.” *Animal Microbiome*. Published January 2023. DOI: [10.1186/s42523-022-00224-6](https://doi.org/10.1186/s42523-022-00224-6). (wunderlich2023understandingthemicrobial pages 11-12, wunderlich2023understandingthemicrobial pages 4-6)
6. Zanne AE et al. “Fungal functional ecology: bringing a trait-based approach to plant-associated fungi.” *Biological Reviews*. Published 2020. DOI: [10.1111/brv.12570](https://doi.org/10.1111/brv.12570). (zanne2020fungalfunctionalecology pages 15-16)
7. Fierer N. “Embracing the unknown: disentangling the complexities of the soil microbiome.” *Nature Reviews Microbiology*. Published August 2017. DOI: [10.1038/nrmicro.2017.87](https://doi.org/10.1038/nrmicro.2017.87).

## Curation recommendation

Expand the existing 14-node/9-edge graph first with the high-confidence **extracellular hydrolysis**, **oxidative ligninolysis**, **soluble-product formation**, and **carbon/nutrient recycling** modules. Add LPMO/redox-partner, cellulosome, CCR, and soil-carbon-fate branches only with explicit taxon or environmental-context qualifiers. Transporter-specific, universal environmental-control, and genomic-prediction-to-trait edges should remain pending until supported by direct primary evidence.

References

1. (zanne2020fungalfunctionalecology pages 15-16): Amy E. Zanne, Kessy Abarenkov, Michelle E. Afkhami, Carlos A. Aguilar‐Trigueros, Scott Bates, Jennifer M. Bhatnagar, Posy E. Busby, Natalie Christian, William K. Cornwell, Thomas W. Crowther, Habacuc Flores‐Moreno, Dimitrios Floudas, Romina Gazis, David Hibbett, Peter Kennedy, Daniel L. Lindner, Daniel S. Maynard, Amy M. Milo, Rolf Henrik Nilsson, Jeff Powell, Mark Schildhauer, Jonathan Schilling, and Kathleen K. Treseder. Fungal functional ecology: bringing a trait‐based approach to plant‐associated fungi. Nov 2020. URL: https://doi.org/10.1111/brv.12570, doi:10.1111/brv.12570. This article has 351 citations and is from a domain leading peer-reviewed journal.

2. (christian2024plantendophytecommunicationscaling pages 12-13): Natalie Christian and Michael H. Perlin. Plant-endophyte communication: scaling from molecular mechanisms to ecological outcomes. Mycologia, 116:227-250, Feb 2024. URL: https://doi.org/10.1080/00275514.2023.2299658, doi:10.1080/00275514.2023.2299658. This article has 9 citations and is from a domain leading peer-reviewed journal.

3. (gurovic2023regulationoflignocellulose pages 2-3): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 32 citations and is from a peer-reviewed journal.

4. (elias2024microbialandmineral pages 1-2): Dafydd M. O. Elias, Kelly E. Mason, Tim Goodall, Ashley Taylor, Pengzhi Zhao, Alba Otero-Fariña, Hongmei Chen, Caroline L. Peacock, Nicholas J. Ostle, Robert Griffiths, Pippa J. Chapman, Joseph Holden, Steve Banwart, Niall P. McNamara, and Jeanette Whitaker. Microbial and mineral interactions decouple litter quality from soil organic matter formation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54446-0, doi:10.1038/s41467-024-54446-0. This article has 109 citations and is from a highest quality peer-reviewed journal.

5. (elias2024microbialandmineral pages 12-13): Dafydd M. O. Elias, Kelly E. Mason, Tim Goodall, Ashley Taylor, Pengzhi Zhao, Alba Otero-Fariña, Hongmei Chen, Caroline L. Peacock, Nicholas J. Ostle, Robert Griffiths, Pippa J. Chapman, Joseph Holden, Steve Banwart, Niall P. McNamara, and Jeanette Whitaker. Microbial and mineral interactions decouple litter quality from soil organic matter formation. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54446-0, doi:10.1038/s41467-024-54446-0. This article has 109 citations and is from a highest quality peer-reviewed journal.

6. (shabaev2024saprotrophicwooddecay pages 14-16): Alexander V. Shabaev, Olga S. Savinova, Konstantin V. Moiseenko, Olga A. Glazunova, and Tatyana V. Fedorova. Saprotrophic wood decay ability and plant cell wall degrading enzyme system of the white rot fungus crucibulum laeve: secretome, metabolome and genome investigations. Journal of Fungi, 11:21, Dec 2024. URL: https://doi.org/10.3390/jof11010021, doi:10.3390/jof11010021. This article has 9 citations.

7. (wunderlich2023understandingthemicrobial pages 4-6): Georgia Wunderlich, Michelle Bull, Tom Ross, Michael Rose, and Belinda Chapman. Understanding the microbial fibre degrading communities & processes in the equine gut. Animal Microbiome, Jan 2023. URL: https://doi.org/10.1186/s42523-022-00224-6, doi:10.1186/s42523-022-00224-6. This article has 59 citations and is from a peer-reviewed journal.

8. (wunderlich2023understandingthemicrobial pages 11-12): Georgia Wunderlich, Michelle Bull, Tom Ross, Michael Rose, and Belinda Chapman. Understanding the microbial fibre degrading communities & processes in the equine gut. Animal Microbiome, Jan 2023. URL: https://doi.org/10.1186/s42523-022-00224-6, doi:10.1186/s42523-022-00224-6. This article has 59 citations and is from a peer-reviewed journal.