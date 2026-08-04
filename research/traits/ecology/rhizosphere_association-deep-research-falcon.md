---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:42:24.179666'
end_time: '2026-08-03T23:50:33.669047'
duration_seconds: 489.49
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: rhizosphere association
  trait_identifier: traitmech:000051
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: rhizosphere_association
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A habitat association in which an organism lives in the rhizosphere\
    \ \u2014 the soil zone influenced by plant roots and root exudates \u2014 a hotspot\
    \ of microbial activity and plant-microbe interaction."
  parent_traits: traitmech:000047
  synonyms: rhizosphere-associated
  evidence_summary: 'DOI:10.1038/nrmicro3109:  (Philippot et al., "Going back to the
    roots", define the rhizosphere as a distinct, root-influenced microbial habitat.)
    | DOI:10.1038/nrmicro.2017.87:  (Fierer supports the rhizosphere as a high-activity
    subset of the broader soil microbiome.)'
  causal_graph_summary: 'rhizosphere_root_exudate: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** rhizosphere association
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000051
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives in the rhizosphere — the soil zone influenced by plant roots and root exudates — a hotspot of microbial activity and plant-microbe interaction.
- **Parent traits:** traitmech:000047
- **Synonyms:** rhizosphere-associated
- **Existing evidence:** DOI:10.1038/nrmicro3109:  (Philippot et al., "Going back to the roots", define the rhizosphere as a distinct, root-influenced microbial habitat.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports the rhizosphere as a high-activity subset of the broader soil microbiome.)
- **Existing causal graph summary:** rhizosphere_root_exudate: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **rhizosphere association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/rhizosphere_association.yaml`.

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
- **Trait label:** rhizosphere association
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000051
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism lives in the rhizosphere — the soil zone influenced by plant roots and root exudates — a hotspot of microbial activity and plant-microbe interaction.
- **Parent traits:** traitmech:000047
- **Synonyms:** rhizosphere-associated
- **Existing evidence:** DOI:10.1038/nrmicro3109:  (Philippot et al., "Going back to the roots", define the rhizosphere as a distinct, root-influenced microbial habitat.) | DOI:10.1038/nrmicro.2017.87:  (Fierer supports the rhizosphere as a high-activity subset of the broader soil microbiome.)
- **Existing causal graph summary:** rhizosphere_root_exudate: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **rhizosphere association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/rhizosphere_association.yaml`.

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


# TraitMech curation report: rhizosphere association

## Trait record and scope

- **Trait:** rhizosphere association
- **Identifier:** `traitmech:000051`
- **Category / kind / status:** ECOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000047`
- **Synonym:** rhizosphere-associated

### Recommended interpretation

`traitmech:000051` should represent an **organism-level habitat association**: reproducible occurrence, enrichment, persistence, or activity in soil whose physicochemical and biological state is influenced by living roots and their rhizodeposits. It is not itself a single biochemical capacity. Chemotaxis, substrate utilization, attachment, biofilm formation, stress tolerance, and competition are mechanisms that can increase the probability or strength of this association.

A useful operational model is:

**root-derived input → microbial sensing or uptake → directed motility/growth → attachment or persistence → enrichment in root-influenced soil.**

The conventional soluble-exudate zone is often approximately **2–10 mm** from the root, although the boundary is dynamic and depends on plant species, root age, soil structure, water connectivity, and the measured variable. Root volatiles such as methyl jasmonate can act beyond the soluble-exudate zone, so a rigid distance cutoff should not define the ontology class. (kulkarni2024volatilemethyljasmonate pages 1-2, kulkarni2024volatilemethyljasmonate pages 8-9, arredondo2024differentialexudationcreates pages 1-6)

### Boundary cases

1. **Bulk-soil association:** exclude organisms detected only in non-root-influenced soil. Enrichment in rhizosphere relative to matched bulk soil is strong assay evidence, but enrichment is not required if direct spatial or activity measurements establish residence.
2. **Rhizoplane colonization:** attachment to the root surface is a narrower phenotype and should be represented as a downstream or related trait, not treated as synonymous with rhizosphere association. Primary attachment is initially reversible; adhesins, appendages, cellulose, extracellular proteins, and polysaccharides then support stronger attachment and microcolonies. (knights2021decipheringbacterialmechanisms pages 1-2)
3. **Endosphere association:** residence inside root tissues is distinct. A strain may be rhizosphere-associated without being endophytic, and vice versa.
4. **Plant-beneficial phenotype:** plant-growth promotion, pathogen suppression, nitrogen fixation, or salt tolerance must not be required. Pathogens and commensals can also be rhizosphere-associated; nucleosides attracted both beneficial and pathogenic bacteria. (keren2024rootsecretednucleosidessignaling pages 1-2)
5. **Rhizocompetence:** this is a composite capacity to reach, colonize, compete, and persist near roots. It is mechanistically relevant but should not be collapsed into the habitat-association class.
6. **Assay-only chemotaxis:** attraction in capillary, agar, or gradient assays supports a mechanism, but alone does not prove stable rhizosphere residence.
7. **Aerial-root mucilage and mycorrhizosphere:** include only where the sampled microhabitat is demonstrably root-influenced soil or mucilage and the intended parent trait permits it; otherwise model these as adjacent specialized habitats.

## Candidate nodes grouped by type

### Environmental and experimental nodes

- rhizosphere; root-influenced soil
- bulk soil comparator
- rhizoplane; root surface
- root endosphere
- root tip, elongation zone, mature root zone
- root exudate and rhizodeposition
- root volatile organic compounds
- dissolved organic carbon
- soil moisture and water-filled pore connectivity
- oxygen availability, redox potential, and pH
- salinity / NaCl stress
- nitrogen limitation or sufficiency
- phosphorus availability
- plant genotype and developmental stage
- capillary chemotaxis assay, semisolid-agar assay, soil-plate assay
- rhizobox, microdialysis, microsensor, and root-colonization CFU assay

Root-zone biogeochemistry is spatially heterogeneous: in *Avena sativa*, sugars correlated with declining redox potential after root-tip arrival, plausibly through increased microbial oxygen demand, while organic acids correlated with declining pH. These are useful environmental modifiers, but the reported relationships are correlations rather than direct organism-level colonization mechanisms. (arredondo2024differentialexudationcreates pages 1-6)

### Chemicals and nutrients

**High-priority specific nodes**

- xanthine — candidate `CHEBI:15318`
- glucose — candidate `CHEBI:17234`
- sucrose — candidate `CHEBI:15824`
- citric acid — candidate `CHEBI:30769`
- L-malic acid — candidate `CHEBI:30797`
- fumaric acid — candidate `CHEBI:30887`
- methyl jasmonate — retain label-only pending identifier verification
- nucleoside and deoxynucleoside classes; ground individual compounds only when the experiment identifies them
- naringin, naringenin, quercetin, flavone, and flavanone — verify individual ChEBI records before YAML insertion
- myo-inositol
- D-galactose
- amino acids including histidine, arginine, and aspartate
- coumarins including sideretin and fraxetin
- plant polysaccharides and mucilage
- iron, oxygen, and carbon substrates

**Lower-priority, association-only candidates**

- chlorogenic acid, cinnamic acid, glucuronic acid, serotonin, ectoine, and acetylcholine. A 2024 switchgrass study associated stress-responsive metabolites with microbial lineages, including ectoine with drought-tolerant Actinobacteria, but these network relationships are insufficient for causal TraitMech edges without intervention or mutant evidence. (baker2024nutrientandmoisture pages 10-10)

### Genes, proteins, transporters, and regulatory complexes

- methyl-accepting chemotaxis protein / MCP
- CheW coupling protein
- CheA histidine kinase
- CheY response regulator
- chemotaxis adaptation proteins CheB/CheC/CheD/CheX
- flagellin FliC and flagellar assembly genes `fli`, `flg`, `flh`
- MotA/MotB flagellar motor components
- McpA chemoreceptor in *Bacillus velezensis* SQR9
- TlpH chemoreceptor in *Azorhizobium caulinodans* ORS571
- CtaA/CtaB/CtaC amino-acid chemoreceptors in *Pseudomonas fluorescens* Pf0-1
- PtsG glucose transporter
- inositol catabolism/transport module (`iol` genes); plant INT1 and PMT5 are plant-side transport candidates
- LapA/LapF adhesin system in *Pseudomonas putida*
- KinD sensor histidine kinase
- Spo0A, DegU, FleQ, and DksA regulators
- extracellular levan biosynthesis machinery
- surfactin biosynthesis module
- bacillomycin D and FeuABC iron-uptake module
- siderophore biosynthesis and uptake modules
- `bphA` / biphenyl-degradation pathway in *Paraburkholderia xenovorans* LB400

Do not assign strain-specific UniProt accessions until the exact genome and protein records used in each experiment have been checked.

### Processes and pathway modules

- bacterial chemotaxis — `GO:0006935`
- flagellum-dependent cell motility — candidate `GO:0001539`
- root-directed migration
- nutrient uptake and catabolism
- surface attachment and microcolony formation
- biofilm formation — `GO:0042710`
- extracellular polymeric-substance production
- siderophore-mediated iron acquisition
- oxidative-stress tolerance
- antimicrobial production and competitive exclusion
- immune recognition/evasion
- community assembly and rhizosphere enrichment
- root colonization and persistence

The conserved chemotaxis backbone is suitable as a mechanistic subgraph: ligand binding to an MCP–CheW–CheA complex modulates CheA autophosphorylation; phosphate transfer to CheY changes motor behavior and therefore directed movement. This is authoritative pathway evidence, but each ligand–receptor link still requires taxon-specific support. (liu2024rootcolonizationby pages 3-4)

## Candidate causal edges

The following table prioritizes direct 2024 interventions and mutant evidence, followed by carefully labeled omics and review-supported links.

| Subject | Predicate | Object | Evidence strength | Taxon/context | Reference DOI/date | concise verbatim supporting snippet | curation note/uncertainty |
|---|---|---|---|---|---|---|---|
| salt-stressed wild soybean root exudates | secrete/enrich | purines, especially xanthine | strong-direct | *Glycine soja* rhizosphere under salt stress | 10.1038/s41467-024-47773-9 (2024) | “roots of salt stressed plants secreted purines, especially xanthine” (zheng2024purinesenrichrootassociated pages 1-2) | Direct primary evidence; plant-side causal input that can seed recruitment edges. |
| xanthine | induces motility of | root-associated *Pseudomonas* isolates | strong-direct | *Pseudomonas* isolates XN05-1 and YE17 from wild soybean | 10.1038/s41467-024-47773-9 (2024) | “xanthine, which induce motility of the Pseudomonas isolates” (zheng2024purinesenrichrootassociated pages 1-2) | Direct experimental statement; phenotype is motility, not by itself full colonization. |
| cheW | required for chemotaxis toward | xanthine | strong-direct mutant | *Pseudomonas* in wild soybean system | 10.1038/s41467-024-47773-9 (2024) | “the motility related gene cheW is required for chemotaxis toward xanthine” (zheng2024purinesenrichrootassociated pages 1-2) | Strong gene-to-phenotype edge supported by mutant analysis. |
| cheW | required for | enhancement of plant salt tolerance | strong-direct mutant | *Pseudomonas*–wild soybean interaction | 10.1038/s41467-024-47773-9 (2024) | “cheW is required for chemotaxis toward xanthine and for enhancing plant salt tolerance” (zheng2024purinesenrichrootassociated pages 1-2) | Downstream host-benefit edge; relevant but more distal than rhizosphere association itself. |
| exogenous xanthine application | enriches | *Pseudomonas* in root/rhizosphere microbiota | strong-direct | non-stressed wild soybean | 10.1038/s41467-024-47773-9 (2024) | “exogenous application for xanthine to non-stressed plants results in Pseudomonas enrichment” (zheng2024purinesenrichrootassociated pages 1-2) | Strong intervention evidence connecting metabolite to microbial enrichment. |
| salt stress | enriches expression of | methyl-accepting chemotaxis proteins (MCPs) | strong-direct omics | wild soybean rhizosphere microbiota | 10.1038/s41467-024-47773-9 (2024) | “genes expressing methyl-accepting chemotaxis proteins (MCP; fold change = 6.14)” (zheng2024purinesenrichrootassociated pages 6-7) | Community-level omics; supports MCP node relevance but not a single-species edge. |
| salt stress | enriches expression of | purine-binding chemotaxis protein CheW | strong-direct omics | wild soybean rhizosphere microbiota | 10.1038/s41467-024-47773-9 (2024) | “purine-binding chemotaxis protein CheW (fold change = 4.70)” (zheng2024purinesenrichrootassociated pages 6-7) | Strong context-specific support for purine-linked chemotaxis. |
| salt stress | enriches expression of | flagellin FliC / flagellar assembly | strong-direct omics | wild soybean rhizosphere microbiota | 10.1038/s41467-024-47773-9 (2024) | “flagellin FliC… showed a 3.66-fold enrichment” (zheng2024purinesenrichrootassociated pages 6-7) | Supports motility module as rhizosphere-association mechanism. |
| root-secreted nucleosides and deoxynucleosides | induce positive chemotaxis in | rhizosphere bacteria | strong-direct | *Bacillus pumilus*, *B. subtilis*, *Pseudomonas turukhanskensis*, *Serratia marcescens*, *Xanthomonas campestris*, *E. coli* | 10.3389/fpls.2024.1388384 (2024) | “Nucleosides induced positive chemotaxis in plant beneficial bacteria” (keren2024rootsecretednucleosidessignaling pages 1-2) | Direct assay evidence; broad taxonomic scope but specific receptors not identified. |
| root-secreted nucleosides | contribute to assembly of | rhizosphere bacterial community | moderate-direct | soil plate assay / multiple plant exudates | 10.3389/fpls.2024.1388384 (2024) | “root-secreted nucleosides are involved in the assembly of the rhizosphere bacterial community by inducing chemotaxis toward plant roots” (keren2024rootsecretednucleosidessignaling pages 1-2) | Good mechanistic interpretation from primary study; assembly claim is somewhat inferential. |
| methyl jasmonate (MeJA) | rapidly triggers | biofilm formation and microbiome changes | strong-direct | root volatile signaling to complex soil microbiome | 10.1038/s41589-023-01462-8 (2024 issue; published 2023) | “Methyl jasmonate (MeJA) is a bioactive signal of rVOCs that rapidly triggers both biofilm and microbiome changes” (kulkarni2024volatilemethyljasmonate pages 1-2) | Strong primary evidence for volatile-mediated rhizosphere recruitment beyond soluble exudate zone. |
| root volatile organic compounds (rVOCs) | promote | biofilm formation in soil microbiota | strong-direct | complex soil microbiome, multiple plant species | 10.1038/s41589-023-01462-8 (2024 issue; published 2023) | “rVOCs can promote biofilm formation in the soil microbiota” (kulkarni2024volatilemethyljasmonate pages 1-2) | Useful higher-level edge; MeJA is a more specific child edge. |
| naringenin and quercetin | attract | *Paraburkholderia xenovorans* LB400 | strong-direct | in vitro chemotaxis assays relevant to early root colonization | 10.3389/fpls.2024.1325048 (2024) | “strain LB400 was attracted by 50 mM and 100 mM naringenin and by 50 mM quercetin” (ghitti2024flavonoidsinfluencekey pages 8-10) | Direct but assay-specific and taxon-specific; retain uncertainty on generalization. |
| naringin | increases | swimming motility of *P. xenovorans* LB400 | strong-direct | in vitro swimming assay | 10.3389/fpls.2024.1325048 (2024) | “50 µM and 100 µM naringin significantly increased the bacterial swimming halo” (ghitti2024flavonoidsinfluencekey pages 8-10) | Strong direct phenotype edge, concentration dependent. |
| naringin and naringenin | promote | biofilm formation by *P. xenovorans* LB400 | strong-direct | in vitro biofilm assay | 10.3389/fpls.2024.1325048 (2024) | “10 µM and 100 µM naringin and naringenin promoted the ability of the bacterium to adhere and form a biofilm” (ghitti2024flavonoidsinfluencekey pages 8-10) | Direct, useful for early colonization/biofilm nodes; still taxon-specific. |
| flavonoid aglycone-enriched exudation (Arabidopsis tt8) | favors early rhizoplane colonization by | *P. xenovorans* LB400 | moderate-direct | Arabidopsis mutant plantlets | 10.3389/fpls.2024.1325048 (2024) | “early rhizoplane colonization was favored in plantlets of the tt8 Arabidopsis mutant” and “1.09 × 10^4 CFUs/mg” vs “5.57 × 10^3” WT (ghitti2024flavonoidsinfluencekey pages 1-2, ghitti2024flavonoidsinfluencekey pages 8-10) | Strongly suggestive direct colonization phenotype; genotype-specific metabolite background complicates single-metabolite attribution. |
| MCP–CheW receptor complex | modulates autophosphorylation of | CheA histidine kinase | moderate-review-supported | conserved bacterial chemotaxis signaling in rhizobacteria | 10.1093/femsre/fuad066 (2024) | “The MCPs selectively recognize and bind to specific ligands… modulates the autophosphorylation rate of the histidine kinase CheA in a CheW-dependent manner” (liu2024rootcolonizationby pages 3-4) | Mechanistic backbone edge from authoritative review; curate as conserved module, not trait-specific proof alone. |
| phosphorylated CheY | binds to | motor proteins driving motility | moderate-review-supported | conserved bacterial chemotaxis signaling | 10.1093/femsre/fuad066 (2024) | “Phosphorylated CheY binds to motor proteins that are responsible for driving various kinds of motility” (liu2024rootcolonizationby pages 3-4) | Canonical pathway support connecting chemotaxis signaling to motility. |
| glucose transporter PtsG | promotes | root colonization | moderate-direct cited-in-review | *Bacillus cereus* C1L | 10.1093/femsre/fuad066 (2024 review summarizing Lin et al. 2020) | “knockout of the ptsG gene encoding the main glucose transporter… led to a sharp decrease in root colonization” (liu2024rootcolonizationby pages 6-7) | Useful nutrient-uptake edge, but primary source should be checked before final curation. |


*Table: This table summarizes the strongest curation-ready causal edges supporting microbial rhizosphere association, prioritizing direct 2024 experimental evidence and adding a small number of conserved review-supported mechanistic links. It is useful as a first-pass edge set for TraitMech graph construction and for distinguishing strong direct evidence from taxon-specific or review-derived claims.*

### Additional attachment, nutrition, and persistence edges

| Subject | Predicate | Object | Evidence and snippet | Curation assessment |
|---|---|---|---|---|
| root-exudate carbon | supports | microbial growth in the rhizosphere | Plants can direct a substantial fraction of fixed carbon belowground; primary metabolites stimulate growth and shape assembly. “Plants exude up to 20% of photosynthetically fixed carbon” in the cited synthesis. (knights2021decipheringbacterialmechanisms pages 1-2, knights2021decipheringbacterialmechanisms pages 8-9) | Curate only as a broad environmental edge; estimates vary strongly by method and study. |
| LapF | promotes | microcolony formation and root colonization | “*P. putida lapF* mutants show reduced colonization of corn and alfalfa roots with impaired microcolony formation.” (knights2021decipheringbacterialmechanisms pages 8-9) | Strong candidate after checking the primary experiment and strain-specific accession. |
| PtsG glucose transporter | promotes | root colonization by *Bacillus cereus* C1L | `ptsG` knockout caused a “sharp decrease in root colonization.” (liu2024rootcolonizationby pages 6-7) | Primary paper should be retrieved before final curation. |
| plant polysaccharides | activate through Spo0A signaling | *B. subtilis* matrix production and biofilm formation | Polysaccharides act as signals affecting Spo0A phosphorylation and as carbon for matrix exopolysaccharide. (liu2024rootcolonizationby pages 6-7) | Mechanistically useful but taxon-specific. |
| D-galactose | activates through McpA | chemotaxis and biofilm formation in *B. velezensis* SQR9 | Review reports that cucumber-secreted D-galactose enhances both processes “in a McpA-dependent manner.” (liu2024rootcolonizationby pages 6-7) | High-priority edge once the primary source is verified. |
| biofilm matrix | increases | persistence under environmental and biological stress | Biofilms confer antimicrobial tolerance, resistance to environmental stress and protozoan predation, and support consortium metabolism. (liu2024rootcolonizationby pages 6-7) | Broad enabling mechanism; avoid implying that every biofilm-forming organism is rhizosphere-associated. |
| root-secreted sucrose | stimulates | levan/surfactin production and motility in *B. subtilis* | Sucrose activates extracellular levan, which regulates flagellar synthesis; sucrose-deficient *Arabidopsis* supported ineffective colonization. (liu2024rootcolonizationby pages 3-4, liu2024rootcolonizationby pages 6-7) | Promising multi-step module; retrieve primary study before committing exact predicates. |
| fumaric, tartaric, and L-malic acids | regulate | `fla/che` proteins and biofilm formation in *Hansschlegelia zhihuaiae* S113 | The 2024 review identifies these organic acids as nutrients/signals affecting the `fla/che` cluster and biofilm. (chen2024thefunctionof pages 9-10) | Review-derived and strain-specific; primary-source verification required. |

## Strongest proposed graph architecture

A conservative first implementation should center on two experimentally supported routes:

### Route A: soluble-metabolite recruitment

`root stress` → `xanthine secretion` → `CheW-dependent chemotaxis` → `flagellar motility` → `Pseudomonas enrichment near/in roots` → `plant salt-tolerance benefit`.

This route has intervention, mutant, metagenomic, and metatranscriptomic support. Under salt stress, cell-motility transcripts were enriched **2.5-fold**; 395 chemotaxis DEGs included 329 upregulated genes, and 729 flagellar-assembly DEGs included 654 upregulated genes. MCP, CheW, and FliC signals increased **6.14-, 4.70-, and 3.66-fold**, respectively. Exogenous xanthine raised the reported *Pseudomonas* relative abundance to **17.47%**, versus **0.81%** in the control, and plant benefit depended on the presence of *Pseudomonas*. (zheng2024purinesenrichrootassociated pages 6-7, zheng2024purinesenrichrootassociated pages 10-11)

### Route B: volatile signal–biofilm assembly

`root methyl jasmonate emission` → `soil microbiome response` → `biofilm matrix/biovolume increase` → `host-influenced biofilm community` → `plant-growth benefit`.

The response was detectable within approximately **15 h**; root VOCs altered the abundance of **8–10%** of biofilm-community members, and affected taxa represented **19 of 24 phyla** present in host-influenced biofilms. The authors emphasize that low MeJA abundance favors interpretation as a signal rather than a nutrient. (kulkarni2024volatilemethyljasmonate pages 8-9)

These routes should remain connected to the parent ecological phenotype through an edge such as `increases_probability_of` or `contributes_to`, rather than asserting that any single mechanism is necessary and sufficient across all taxa.

## Recent developments and applications

### Precision recruitment under stress

The 2024 wild-soybean work provides one of the strongest current demonstrations of a plant metabolite recruiting a functional microbial group through a defined chemotaxis gene. It suggests possible seed, soil, or root-zone treatments combining a compatible metabolite with chemotaxis-competent inoculants. Translation beyond *Glycine soja* and the two tested *Pseudomonas* isolates remains unproven. (zheng2024purinesenrichrootassociated pages 1-2, zheng2024purinesenrichrootassociated pages 6-7)

### Bioinoculant screening

Effective inoculants require colonization and persistence, not merely nitrogen fixation, phosphate solubilization, or hormone production. Screening should therefore include root-exudate chemotaxis, motility in porous media, carbon-source utilization, attachment, biofilm formation, oxidative-stress tolerance, and competition. Experimental evolution in *Pseudomonas protegens* identified **35 mutations across 28 genes**, repeatedly affecting global regulation, siderophores, surface decoration, attachment, and motility; motility increased in independent lines. (li2021experimentalevolutiondrivenidentificationof pages 1-2)

### Rhizoremediation

Flavonoids changed growth, chemotaxis, motility, biofilm formation, and PCB-catabolic behavior in *P. xenovorans* LB400. Arabidopsis `tt8` plants, enriched in flavonoid aglycones, supported approximately **1.09 × 10⁴ CFU mg⁻¹ root** after 1 h versus **5.57 × 10³ CFU mg⁻¹** for wild type. Quercetin at 50 µM increased stationary-phase biomass by **40.1%**, while individual flavonoids produced concentration-dependent stimulation or inhibition. This supports metabolite-assisted rhizoremediation, but effects cannot be generalized across flavonoids or bacteria. (ghitti2024flavonoidsinfluencekey pages 8-10, ghitti2024flavonoidsinfluencekey pages 1-2)

### Spatially resolved microbiome engineering

Rhizoboxes, microdialysis, high-resolution mass spectrometry, microsensors, microfluidics, transposon screens, and SynComs now allow root-zone mechanisms to be studied at finer spatial and temporal scales. The current expert consensus is that single-strain, sterile systems are valuable for causality but systematically omit microbial competition, cross-feeding, antimicrobial interactions, soil structure, and host immune effects. (knights2021decipheringbacterialmechanisms pages 8-9, arredondo2024differentialexudationcreates pages 1-6)

## Ontology-grounding recommendations

| Node | Suggested grounding | Qualification |
|---|---|---|
| rhizosphere | ENVO term for rhizosphere, exact current CURIE to be registry-verified | Do not infer from “soil” alone. |
| chemotaxis | `GO:0006935` | Suitable process node. |
| flagellum-dependent motility | `GO:0001539` | Verify applicability to the microbial annotation profile in use. |
| biofilm formation | `GO:0042710` | Suitable broad process node. |
| xanthine | `CHEBI:15318` | High-confidence chemical candidate. |
| glucose | `CHEBI:17234` | Specify stereochemistry when the paper does. |
| sucrose | `CHEBI:15824` | High-confidence chemical candidate. |
| citric acid | `CHEBI:30769` | Check whether citrate rather than neutral acid is intended at physiological pH. |
| L-malic acid | `CHEBI:30797` | Preserve stereochemistry. |
| fumaric acid | `CHEBI:30887` | Check protonation state if reaction-level modeling is added. |
| MCP, CheW, CheA, CheY, FliC, PtsG | label plus gene/protein family; strain-specific UniProt later | Do not use one accession across taxa. |
| flagellar assembly / bacterial chemotaxis | KEGG pathway candidates | Verify current KEGG identifiers and licensing context before insertion. |
| *Pseudomonas* XN05-1/YE17 and LB400 | NCBITaxon or strain registry after exact record lookup | Genus-level IDs would lose critical strain specificity. |

## Claims that should not yet be curated

1. **“Nucleoside chemotaxis is universal.”** Responses were broad but not universal, and *E. coli* responsiveness shows that attraction is not specific to rhizosphere-adapted organisms. The community-assembly edge should be marked inferred. (keren2024rootsecretednucleosidessignaling pages 1-2)
2. **All rhizosphere-associated microbes require flagella or chemotaxis.** This excludes nonmotile bacteria, fungi, archaea, passive dispersal, hyphal transport, and growth-driven enrichment.
3. **Any biofilm gene causes rhizosphere association.** Biofilm formation is widespread outside roots and must be tied to a root-context assay.
4. **MeJA defines the rhizosphere boundary.** Volatile effects motivate a process-based boundary but do not establish a universal distance.
5. **Keystone-metabolite correlations are causal recruitment edges.** The switchgrass metabolite–ASV network is hypothesis-generating until perturbation tests establish directionality. (baker2024nutrientandmoisture pages 10-10)
6. **Sugar-driven redox decline is definitively caused by microbial oxygen consumption.** The 2024 spatial study reports a significant correlation and a plausible mechanism, not a completed causal chain. (arredondo2024differentialexudationcreates pages 1-6)
7. **Flavonoids uniformly increase rhizocompetence.** Effects varied by compound and concentration; flavone and quercetin could reduce swimming even where biomass increased. (ghitti2024flavonoidsinfluencekey pages 8-10)
8. **Plant benefit is part of the trait definition.** Beneficial, neutral, and pathogenic organisms may all satisfy `traitmech:000051`.
9. **Review-only gene edges should enter production YAML without primary-paper verification.** This applies especially to PtsG, McpA–D-galactose, sucrose–levan–surfactin, and several organic-acid edges.
10. **Omics enrichment alone demonstrates necessity.** The MCP, CheW, and FliC fold changes support a module; necessity is directly established only where mutants or controlled interventions were tested.

## DOI-first bibliography

1. Zheng Y. et al. “Purines enrich root-associated *Pseudomonas* and improve wild soybean growth under salt stress.” *Nature Communications* 15, 3520. **Accepted 12 April 2024**. DOI: [10.1038/s41467-024-47773-9](https://doi.org/10.1038/s41467-024-47773-9). (zheng2024purinesenrichrootassociated pages 1-2, zheng2024purinesenrichrootassociated pages 6-7)
2. Keren G. et al. “Root-secreted nucleosides: signaling chemoattractants of rhizosphere bacteria.” *Frontiers in Plant Science* 15. **Published 10 May 2024**. DOI: [10.3389/fpls.2024.1388384](https://doi.org/10.3389/fpls.2024.1388384). (keren2024rootsecretednucleosidessignaling pages 1-2)
3. Kulkarni O.S. et al. “Volatile methyl jasmonate from roots triggers host-beneficial soil microbiome biofilms.” *Nature Chemical Biology* 20:473–483. **Published online 13 November 2023; April 2024 issue**. DOI: [10.1038/s41589-023-01462-8](https://doi.org/10.1038/s41589-023-01462-8). (kulkarni2024volatilemethyljasmonate pages 1-2, kulkarni2024volatilemethyljasmonate pages 8-9)
4. Ghitti E. et al. “Flavonoids influence key rhizocompetence traits for early root colonization and PCB degradation potential of *Paraburkholderia xenovorans* LB400.” *Frontiers in Plant Science* 15. **Published 2 February 2024**. DOI: [10.3389/fpls.2024.1325048](https://doi.org/10.3389/fpls.2024.1325048). (ghitti2024flavonoidsinfluencekey pages 8-10, ghitti2024flavonoidsinfluencekey pages 1-2)
5. Chen L., Liu Y. “The Function of Root Exudates in the Root Colonization by Beneficial Soil Rhizobacteria.” *Biology* 13:95. **February 2024**. DOI: [10.3390/biology13020095](https://doi.org/10.3390/biology13020095). (chen2024thefunctionof pages 9-10, chen2024thefunctionof pages 10-12)
6. Liu Y. et al. “Root colonization by beneficial rhizobacteria.” *FEMS Microbiology Reviews* 48(1). **2024**. DOI: [10.1093/femsre/fuad066](https://doi.org/10.1093/femsre/fuad066). (liu2024rootcolonizationby pages 3-4, liu2024rootcolonizationby pages 6-7)
7. Arredondo M.G. et al. “Differential Exudation Creates Biogeochemically Distinct Microenvironments during Rhizosphere Evolution.” *Environmental Science & Technology* 58:18713–18722. **October 2024**. DOI: [10.1021/acs.est.4c04108](https://doi.org/10.1021/acs.est.4c04108). (arredondo2024differentialexudationcreates pages 1-6)
8. Baker N.R. et al. “Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes.” *PNAS* 121. **August 2024**. DOI: [10.1073/pnas.2303439121](https://doi.org/10.1073/pnas.2303439121). (baker2024nutrientandmoisture pages 10-10)
9. Li E. et al. “Experimental-Evolution-Driven Identification of *Arabidopsis* Rhizosphere Competence Genes in *Pseudomonas protegens*.” *mBio* 12. **June 2021**. DOI: [10.1128/mbio.00927-21](https://doi.org/10.1128/mbio.00927-21). (li2021experimentalevolutiondrivenidentificationof pages 1-2)
10. Knights H.E. et al. “Deciphering bacterial mechanisms of root colonization.” *Environmental Microbiology Reports* 13:428–444. **February 2021**. DOI: [10.1111/1758-2229.12934](https://doi.org/10.1111/1758-2229.12934). (knights2021decipheringbacterialmechanisms pages 1-2, knights2021decipheringbacterialmechanisms pages 8-9)

## Curation recommendation

The strongest first expansion of the existing `rhizosphere_root_exudate` graph is a compact causal core containing **root exudate/volatile signal, xanthine, nucleosides, methyl jasmonate, MCP, CheW, CheA, CheY, flagellar motility, attachment, biofilm formation, carbon uptake, and rhizosphere enrichment**. Encode taxon and assay context on each edge. Give highest confidence to the xanthine–CheW–*Pseudomonas* route, moderate-to-high confidence to nucleoside chemotaxis and MeJA-induced biofilms, and provisional status to review-derived nutrient-uptake, adhesin, siderophore, and immune-evasion links pending retrieval of their primary experiments.

References

1. (kulkarni2024volatilemethyljasmonate pages 1-2): Omkar S. Kulkarni, Mrinmoy Mazumder, Shruthi Kini, Eric D. Hill, Johanan Shao Bing Aow, Samantha Mun Lin Phua, Untzizu Elejalde, Staffan Kjelleberg, and Sanjay Swarup. Volatile methyl jasmonate from roots triggers host-beneficial soil microbiome biofilms. Nature Chemical Biology, 20:473-483, Nov 2024. URL: https://doi.org/10.1038/s41589-023-01462-8, doi:10.1038/s41589-023-01462-8. This article has 87 citations and is from a highest quality peer-reviewed journal.

2. (kulkarni2024volatilemethyljasmonate pages 8-9): Omkar S. Kulkarni, Mrinmoy Mazumder, Shruthi Kini, Eric D. Hill, Johanan Shao Bing Aow, Samantha Mun Lin Phua, Untzizu Elejalde, Staffan Kjelleberg, and Sanjay Swarup. Volatile methyl jasmonate from roots triggers host-beneficial soil microbiome biofilms. Nature Chemical Biology, 20:473-483, Nov 2024. URL: https://doi.org/10.1038/s41589-023-01462-8, doi:10.1038/s41589-023-01462-8. This article has 87 citations and is from a highest quality peer-reviewed journal.

3. (arredondo2024differentialexudationcreates pages 1-6): Mariela Garcia Arredondo, William Kew, Rosalie Chu, Morris E. Jones, Rene M. Boiteau, Zoe G. Cardon, and Marco Keiluweit. Differential exudation creates biogeochemically distinct microenvironments during rhizosphere evolution. Oct 2024. URL: https://doi.org/10.1021/acs.est.4c04108, doi:10.1021/acs.est.4c04108. This article has 32 citations and is from a domain leading peer-reviewed journal.

4. (knights2021decipheringbacterialmechanisms pages 1-2): Hayley E. Knights, Beatriz Jorrin, Timothy L. Haskett, and Philip S. Poole. Deciphering bacterial mechanisms of root colonization. Feb 2021. URL: https://doi.org/10.1111/1758-2229.12934, doi:10.1111/1758-2229.12934. This article has 222 citations and is from a peer-reviewed journal.

5. (keren2024rootsecretednucleosidessignaling pages 1-2): Guy Keren, Galit Yehezkel, Lakkakula Satish, Zahar Adamov, Ze’ev Barak, Shimon Ben-Shabat, Varda Kagan-Zur, and Yaron Sitrit. Root-secreted nucleosides: signaling chemoattractants of rhizosphere bacteria. Frontiers in Plant Science, May 2024. URL: https://doi.org/10.3389/fpls.2024.1388384, doi:10.3389/fpls.2024.1388384. This article has 16 citations.

6. (baker2024nutrientandmoisture pages 10-10): Nameer R. Baker, Kateryna Zhalnina, Mengting Yuan, Don Herman, Javier A. Ceja-Navarro, Joelle Sasse, Jacob S. Jordan, Benjamin P. Bowen, Liyou Wu, Christina Fossum, Aaron Chew, Ying Fu, Malay Saha, Jizhong Zhou, Jennifer Pett-Ridge, Trent R. Northen, and Mary K. Firestone. Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2303439121, doi:10.1073/pnas.2303439121. This article has 146 citations and is from a highest quality peer-reviewed journal.

7. (liu2024rootcolonizationby pages 3-4): Yunpeng Liu, Zhihui Xu, Lin Chen, Weibing Xun, Xia Shu, Yu Chen, Xinli Sun, Zhengqi Wang, Yi Ren, Qirong Shen, and Ruifu Zhang. Root colonization by beneficial rhizobacteria. FEMS Microbiology Reviews, Dec 2024. URL: https://doi.org/10.1093/femsre/fuad066, doi:10.1093/femsre/fuad066. This article has 220 citations and is from a domain leading peer-reviewed journal.

8. (zheng2024purinesenrichrootassociated pages 1-2): Yanfen Zheng, Xuwen Cao, Yanan Zhou, Siqi Ma, Youqiang Wang, Zhe Li, Donglin Zhao, Yanzhe Yang, Han Zhang, Chen Meng, Zhihong Xie, Xiaona Sui, Kangwen Xu, Yiqiang Li, and Cheng-Sheng Zhang. Purines enrich root-associated pseudomonas and improve wild soybean growth under salt stress. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47773-9, doi:10.1038/s41467-024-47773-9. This article has 237 citations and is from a highest quality peer-reviewed journal.

9. (zheng2024purinesenrichrootassociated pages 6-7): Yanfen Zheng, Xuwen Cao, Yanan Zhou, Siqi Ma, Youqiang Wang, Zhe Li, Donglin Zhao, Yanzhe Yang, Han Zhang, Chen Meng, Zhihong Xie, Xiaona Sui, Kangwen Xu, Yiqiang Li, and Cheng-Sheng Zhang. Purines enrich root-associated pseudomonas and improve wild soybean growth under salt stress. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47773-9, doi:10.1038/s41467-024-47773-9. This article has 237 citations and is from a highest quality peer-reviewed journal.

10. (ghitti2024flavonoidsinfluencekey pages 8-10): Elisa Ghitti, Eleonora Rolli, Lorenzo Vergani, and Sara Borin. Flavonoids influence key rhizocompetence traits for early root colonization and pcb degradation potential of paraburkholderia xenovorans lb400. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1325048, doi:10.3389/fpls.2024.1325048. This article has 24 citations.

11. (ghitti2024flavonoidsinfluencekey pages 1-2): Elisa Ghitti, Eleonora Rolli, Lorenzo Vergani, and Sara Borin. Flavonoids influence key rhizocompetence traits for early root colonization and pcb degradation potential of paraburkholderia xenovorans lb400. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1325048, doi:10.3389/fpls.2024.1325048. This article has 24 citations.

12. (liu2024rootcolonizationby pages 6-7): Yunpeng Liu, Zhihui Xu, Lin Chen, Weibing Xun, Xia Shu, Yu Chen, Xinli Sun, Zhengqi Wang, Yi Ren, Qirong Shen, and Ruifu Zhang. Root colonization by beneficial rhizobacteria. FEMS Microbiology Reviews, Dec 2024. URL: https://doi.org/10.1093/femsre/fuad066, doi:10.1093/femsre/fuad066. This article has 220 citations and is from a domain leading peer-reviewed journal.

13. (knights2021decipheringbacterialmechanisms pages 8-9): Hayley E. Knights, Beatriz Jorrin, Timothy L. Haskett, and Philip S. Poole. Deciphering bacterial mechanisms of root colonization. Feb 2021. URL: https://doi.org/10.1111/1758-2229.12934, doi:10.1111/1758-2229.12934. This article has 222 citations and is from a peer-reviewed journal.

14. (chen2024thefunctionof pages 9-10): Lin Chen and Yunpeng Liu. The function of root exudates in the root colonization by beneficial soil rhizobacteria. Biology, 13:95, Feb 2024. URL: https://doi.org/10.3390/biology13020095, doi:10.3390/biology13020095. This article has 236 citations.

15. (zheng2024purinesenrichrootassociated pages 10-11): Yanfen Zheng, Xuwen Cao, Yanan Zhou, Siqi Ma, Youqiang Wang, Zhe Li, Donglin Zhao, Yanzhe Yang, Han Zhang, Chen Meng, Zhihong Xie, Xiaona Sui, Kangwen Xu, Yiqiang Li, and Cheng-Sheng Zhang. Purines enrich root-associated pseudomonas and improve wild soybean growth under salt stress. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47773-9, doi:10.1038/s41467-024-47773-9. This article has 237 citations and is from a highest quality peer-reviewed journal.

16. (li2021experimentalevolutiondrivenidentificationof pages 1-2): Erqin Li, Hao Zhang, Henan Jiang, Corné M. J. Pieterse, Alexandre Jousset, Peter A. H. M. Bakker, and Ronnie de Jonge. Experimental-evolution-driven identification of <i>arabidopsis</i> rhizosphere competence genes in pseudomonas protegens. Jun 2021. URL: https://doi.org/10.1128/mbio.00927-21, doi:10.1128/mbio.00927-21. This article has 45 citations and is from a domain leading peer-reviewed journal.

17. (chen2024thefunctionof pages 10-12): Lin Chen and Yunpeng Liu. The function of root exudates in the root colonization by beneficial soil rhizobacteria. Biology, 13:95, Feb 2024. URL: https://doi.org/10.3390/biology13020095, doi:10.3390/biology13020095. This article has 236 citations.