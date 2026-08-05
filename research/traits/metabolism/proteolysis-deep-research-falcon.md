---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:47:49.958119'
end_time: '2026-08-04T06:59:27.402878'
duration_seconds: 697.44
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: proteolysis
  trait_identifier: traitmech:000116
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: proteolysis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism secretes proteases
    to hydrolyze extracellular proteins and peptides into amino acids and short peptides
    for nutrition.
  parent_traits: traitmech:000110
  synonyms: proteolytic, protein degradation
  evidence_summary: 'DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial
    proteases, noting that secreted (extracellular) proteases play a major nutritional
    role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review
    of Bacillus proteases covers extracellular protease activities and their functions.)'
  causal_graph_summary: 'proteolysis_extracellular_protease: 8 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** proteolysis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000116
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism secretes proteases to hydrolyze extracellular proteins and peptides into amino acids and short peptides for nutrition.
- **Parent traits:** traitmech:000110
- **Synonyms:** proteolytic, protein degradation
- **Existing evidence:** DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial proteases, noting that secreted (extracellular) proteases play a major nutritional role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review of Bacillus proteases covers extracellular protease activities and their functions.)
- **Existing causal graph summary:** proteolysis_extracellular_protease: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **proteolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteolysis.yaml`.

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
- **Trait label:** proteolysis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000116
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism secretes proteases to hydrolyze extracellular proteins and peptides into amino acids and short peptides for nutrition.
- **Parent traits:** traitmech:000110
- **Synonyms:** proteolytic, protein degradation
- **Existing evidence:** DOI:10.1128/mmbr.62.3.597-635.1998:  (Rao et al. review microbial proteases, noting that secreted (extracellular) proteases play a major nutritional role through their depolymerizing activity.) | DOI:10.1093/femsre/fuab046:  (Review of Bacillus proteases covers extracellular protease activities and their functions.)
- **Existing causal graph summary:** proteolysis_extracellular_protease: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **proteolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/proteolysis.yaml`.

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


# Curation report: microbial proteolysis

**Target:** `traitmech:000116`  
**Label:** proteolysis  
**Category:** METABOLISM | **Kind:** CLASS | **Status:** REVIEWED  
**Parent:** `traitmech:000110`

## 1. Scope recommendation

`traitmech:000116` should represent the organism-level capacity to deploy **secreted or cell-envelope-associated proteases that depolymerize extracellular proteins into peptides and amino acids used for nutrition**. The defining causal chain is:

**environmental protein → extracellular/cell-envelope protease activity → shorter peptides and amino acids → uptake → cellular carbon/nitrogen metabolism and growth.**

This interpretation follows the supplied definition and the foundational distinction that extracellular proteases have a major nutritional role, while intracellular proteases principally perform protein processing, regulation, and quality control. In *Bacillus subtilis*, extracellular proteases explicitly degrade environmental proteins as carbon and nitrogen sources, but individual enzymes can additionally process signals or remove misfolded proteins; those latter activities are not independently sufficient for this trait (harwood2022theinsand pages 14-15, harwood2022theinsand pages 15-16, rao1998molecularandbiotechnological pages 1-2).

### Boundary cases

| Case | Include? | Curation rule |
|---|---:|---|
| Secreted enzyme hydrolyzes extracellular protein and products support nutrition | Yes | Trait-defining case. |
| Cell-wall/cell-envelope proteinase cleaves external protein before uptake | Yes | Functionally extracellular; typical of lactic acid bacteria (LAB). |
| Uptake of pre-existing peptides without evidence that the organism hydrolyzes protein externally | No, not by itself | Peptide utilization is downstream/supporting, not sufficient evidence of extracellular proteolysis. |
| Intracellular degradation of damaged, regulatory, or short-lived proteins | No | Protein quality control or regulation, not extracellular biopolymer-degradation metabolism. |
| Proteolytic maturation of a secreted enzyme or signaling peptide | Usually no | Include only as an enabling/contextual edge when it activates a nutritional protease. |
| Host-protein cleavage used solely for virulence or immune evasion | No | Nearby virulence phenotype; include only if nutritional assimilation is independently demonstrated. |
| Biofilm-matrix proteolysis, sporulation signaling, or bacteriocin activation | No, unless nutritional use is shown | These are alternative functions of extracellular proteases. |
| Clearing on skim-milk/casein/gelatin agar | Assay evidence | Supports extracellular endoprotease activity, but does not alone prove that released products support growth. |
| Extracellular protease detected after cell lysis | Uncertain | Exoproteomic localization requires a signal peptide or other secretion evidence because lysis can release cytoplasmic enzymes (tinta2023jellyfishdetritussupports pages 7-10, harwood2022theinsand pages 15-16).

## 2. Current mechanistic model

Extracellular endopeptidases cleave internal peptide bonds, converting macromolecular protein into shorter peptides; exopeptidases remove terminal residues and can release free amino acids. In LAB, extracellular or cell-envelope proteinases provide amino acids because milk contains insufficient freely assimilable nitrogen to meet growth requirements. The first stage is explicitly described as extracellular CEP-mediated degradation of casein into smaller products (kieliszek2021characteristicsofthe pages 2-4, song2023microbialproteasesand pages 2-3).

Products can then enter the cell through peptide or amino-acid transporters. In *B. subtilis*, the high-affinity ABC systems Opp, App, and Dpp comprise extracellular, lipid-anchored binding proteins; membrane channels; and cytoplasmic ATPases. OppA and DppE bind extracellular substrates and deliver them for uptake. OppA showed highest affinity for tetra- and pentapeptides, with measured dissociation constants of **0.4 µM** and **2 µM** for two tested peptides (hughes2022peptidetransportin pages 1-3). The transport architecture is directly depicted in Hughes et al. Figure 1 (hughes2022peptidetransportin media 8f9fa6d3).

A compact graph-ready summary is provided below.

| subject | predicate | object | confidence/qualifier |
|---|---|---|---|
| extracellular environmental protein | enables | extracellular proteolysis | high; trait-defining nutritional context (kieliszek2021characteristicsofthe pages 2-4, rao1998molecularandbiotechnological pages 1-2) |
| secreted or cell-envelope endoprotease | hydrolyzes | extracellular protein to oligopeptides | high; broad microbial mechanism, including LAB/Bacillus examples (kieliszek2021characteristicsofthe pages 2-4, song2023microbialproteasesand pages 2-3) |
| extracellular exopeptidase | releases | terminal amino acids from peptides | moderate; well-supported enzyme class, often downstream of endoproteolysis (kieliszek2021characteristicsofthe pages 2-4, song2023microbialproteasesand pages 2-3) |
| Opp/App/Dpp peptide transporters | transports | extracellular peptides into Bacillus subtilis cells | high; taxon-specific to Bacillus subtilis (hughes2022peptidetransportin pages 1-3, hughes2022peptidetransportin media 8f9fa6d3) |
| imported peptides | supports | nitrogen nutrition and growth | moderate; direct for nutritional role, growth link partly contextual/taxon-specific (hughes2022peptidetransportin pages 1-3, kieliszek2021characteristicsofthe pages 2-4) |
| imported amino acids | supports | nitrogen nutrition and growth | moderate; strong in LAB nutritional framing, broader generalization inferred (kieliszek2021characteristicsofthe pages 2-4) |
| CodY | represses | vpr expression in Bacillus subtilis | high; Bacillus subtilis-specific regulatory edge (harwood2022theinsand pages 14-15) |
| CodY | represses | nprE expression in Bacillus subtilis | high; Bacillus subtilis-specific regulatory edge (harwood2022theinsand pages 13-14) |
| phosphate starvation | induces | vpr expression in Bacillus subtilis | high; specific environmental condition (harwood2022theinsand pages 14-15) |
| protein-rich jellyfish detritus | enriches | secretory extracellular proteases in marine bacteria | high; community-level ecological evidence (tinta2023jellyfishdetritussupports pages 1-2, tinta2023jellyfishdetritussupports pages 7-10) |
| secretory S8 subtilisin-family proteases | enriched_in | jellyfish-OM exoproteome | high; marine microcosm/metaproteomics context (tinta2023jellyfishdetritussupports pages 7-10) |
| metalloproteases (including M9 family) | enriched_in | jellyfish-OM degrading community | moderate; marine microcosm/metaproteomics context (tinta2023jellyfishdetritussupports pages 7-10) |
| I39 protease inhibitor | inhibits_or_regulates | extracellular protease activity | low; contextual/uncertain, association stronger than direct causal proof in this trait scope (tinta2023jellyfishdetritussupports pages 7-10) |


*Table: This table summarizes a compact set of graph-ready causal edges for traitmech:000116 extracellular nutritional proteolysis. It emphasizes strongly supported mechanistic and regulatory relations, while clearly marking taxon-specific and uncertain contextual claims.*

## 3. Candidate nodes grouped by type

### A. Processes and pathway modules

| Candidate node | Suggested grounding | Comment |
|---|---|---|
| extracellular nutritional proteolysis | `traitmech:000116` | Trait root; quote identifier verbatim. |
| proteolysis / protein catabolic process | `GO:0030163` | Broader process; localization and nutritional context must be added. |
| peptidase activity | `GO:0008233` | Generic molecular function. |
| extracellular protein hydrolysis | Label only | Prefer a relation/reaction node if TraitMech models transformations. |
| oligopeptide transport | `GO:0006857` | Downstream assimilation module; verify applicability to each transporter. |
| amino-acid transport | Label only or a more specific GO term | Select substrate-specific terms only when evidence identifies the amino acid. |
| nitrogen assimilation from protein | Label only | Do not equate automatically with inorganic-nitrogen assimilation. |
| carbon acquisition from protein | Label only | Supported for Bacillus extracellular proteases but should remain conditional on taxon/source. |

### B. Substrates and products

| Candidate node | Suggested grounding | Comment |
|---|---|---|
| extracellular environmental protein | Label only | A pool/class rather than a single chemical. |
| casein | Label only; curator should select a stable protein/chemical class identifier | Common physiological substrate and assay substrate. |
| gelatin | Label only | Common assay substrate; denatured collagen. |
| collagen | Label only | Relevant to jellyfish detritus and collagenolytic proteases. |
| oligopeptide | Label only or verified ChEBI class | Avoid assigning an unverified ChEBI CURIE. |
| dipeptide | Label only or verified ChEBI class | Dpp substrate class. |
| amino acid | `CHEBI:33709` candidate | Verify against the current ChEBI release before committing. |
| dissolved organic nitrogen | Label only | Environmental pool, not a single molecule. |
| jellyfish-derived organic matter | Label only; environmental material | Protein-rich ecological substrate. |

### C. Enzymes and catalytic classes

| Candidate node | Grounding | Role/qualification |
|---|---|---|
| endopeptidase | `EC:3.4.21–3.4.25` family ranges | Internal cleavage; use a specific EC only when catalytic class is known. |
| serine endopeptidase | `EC:3.4.21.-` | Includes subtilisin-family enzymes. |
| cysteine endopeptidase | `EC:3.4.22.-` | Candidate class. |
| aspartic endopeptidase | `EC:3.4.23.-` | Candidate class. |
| metalloprotease | `EC:3.4.24.-` | Includes marine M9-family observations. |
| aminopeptidase | `EC:3.4.11.-` | Removes N-terminal residues. |
| carboxypeptidase | `EC:3.4.16–3.4.18` | Removes C-terminal residues, catalytic class dependent. |
| dipeptidase | `EC:3.4.13.-` | Hydrolyzes dipeptides. |
| subtilisin/S8-family protease | MEROPS S8; specific EC/UniProt by protein | Dominant exoproteomic class in the 2023 jellyfish-OM study. |
| AprE, NprE, Vpr, Epr, Bpr, Mpr, NprB | Gene/protein labels; ground to taxon-specific UniProt records during implementation | *B. subtilis*-specific candidates; functions are not all exclusively nutritional. |
| PrtP/cell-envelope proteinase | Gene/protein label; taxon-specific UniProt record | Strong LAB candidate for casein hydrolysis. |
| WprA, HtrA, HtrB | Gene/protein labels | Mainly quality-control/context nodes; do not treat automatically as nutritional proteases. |

### D. Transporters and complexes

| Candidate node | Grounding | Components/role |
|---|---|---|
| Opp oligopeptide ABC transporter | Taxon-specific protein complex; label or verified GO/UniProt components | In *B. subtilis*: OppA, OppBC, OppDF. |
| App peptide ABC transporter | Taxon-specific label/UniProt components | AppA, AppBC, AppDF. |
| Dpp dipeptide ABC transporter | Taxon-specific label/UniProt components | DppE, DppBC, DppD2; DppE also bound a murein tripeptide. |
| amino-acid transporter | Label or substrate-specific transporter record | Community-level evidence in jellyfish-OM experiments; exact systems require MAG/protein-level curation. |
| Sec secretion system | `GO:0043952` candidate for protein transport by the Sec complex | Use only where the source establishes Sec-dependent export. |
| signal peptide | `SO:0000418` candidate | Enabling feature rather than an enzyme. |

The Opp/App/Dpp component organization and extracellularly facing substrate-binding proteins are directly supported by structural and biochemical evidence (hughes2022peptidetransportin pages 1-3, hughes2022peptidetransportin media 8f9fa6d3).

### E. Regulators and environmental factors

| Node | Type | Qualification |
|---|---|---|
| CodY | transcriptional regulator | Represses *vpr* and is among the regulators repressing *nprE* in *B. subtilis*. |
| DegU | response regulator | Several extracellular protease genes belong to the DegU regulon; gene-specific edges require exact evidence. |
| AbrB, ScoC/ScoB, PhoP, SigH, Spo0A | regulators | Taxon- and gene-specific contextual nodes; do not generalize across microbes. |
| phosphate starvation | experimental/environmental condition | Induces *vpr* in *B. subtilis*. |
| transition/stationary phase | physiological condition | NprE and AprE dominate stationary-phase culture protease activity. |
| extracellular protein abundance | nutrient condition | Trait-proximal environmental driver. |
| pH, temperature, salinity, metal availability | environmental/assay factors | Protease- and taxon-specific; avoid universal directional edges. |
| I39-family protease inhibitor | inhibitor family | Enriched in jellyfish-OM metaproteomes, but direct inhibition of a particular nutritional protease was not established in the retrieved study. |

## 4. Candidate evidence-backed edges

The table distinguishes **core graph edges** from taxon-specific extensions. Quotes are short excerpts from the retrieved full text.

| # | Subject | Predicate | Object | Reference | Supporting snippet | Curation notes |
|---:|---|---|---|---|---|---|
| 1 | secreted/cell-envelope endopeptidase | hydrolyzes | extracellular protein into shorter peptides | Song et al. 2023, DOI [10.3389/fmicb.2023.1236368](https://doi.org/10.3389/fmicb.2023.1236368) | “Endopeptidases… cleave internally in peptides or proteins.” | **High confidence; core.** Add extracellular localization from gene/protein or assay evidence (song2023microbialproteasesand pages 2-3). |
| 2 | LAB cell-envelope protease | degrades | casein into smaller products | Kieliszek et al. 2021, DOI [10.3390/molecules26071858](https://doi.org/10.3390/molecules26071858) | “In the first stage of proteolysis, extracellular proteolytic enzymes (CEPs) degrade casein milk protein to smaller sizes.” | **High confidence; LAB-specific.** Strong template for a PrtP/CEP branch (kieliszek2021characteristicsofthe pages 2-4). |
| 3 | exopeptidase | removes | terminal amino-acid residue(s) from peptide | Kieliszek et al. 2021; Song et al. 2023 | “cleave the peptide bond proximal to the amino or carboxy termini”; carboxypeptidases “remove a single amino acid from the C-terminus.” | **High confidence enzymology.** Extracellular localization must be separately demonstrated for a trait-defining edge (kieliszek2021characteristicsofthe pages 2-4, song2023microbialproteasesand pages 2-3). |
| 4 | casein proteolysis | produces | amino acids used as nitrogen source by LAB | Kieliszek et al. 2021 | “The final products… are most often the amino acids used by LAB as a source of nitrogen.” | **High confidence; LAB-specific nutritional edge** (kieliszek2021characteristicsofthe pages 2-4). |
| 5 | insufficient free amino acids/nitrogen in milk | necessitates | decomposition of casein by LAB | Kieliszek et al. 2021 | Milk nitrogen “is insufficient to meet all needs; hence, these bacterial species must obtain these ingredients by decomposing milk proteins.” | **High confidence physiological driver; LAB/dairy context** (kieliszek2021characteristicsofthe pages 2-4). |
| 6 | extracellular peptides | bind | OppA/AppA/DppE substrate-binding proteins | Hughes et al. 2022, DOI [10.1099/mic.0.001274](https://doi.org/10.1099/mic.0.001274) | The receptor captures “extracellular solutes and deliver[s] them to the membrane components for uptake.” | **High confidence; *B. subtilis*-specific** (hughes2022peptidetransportin pages 1-3). |
| 7 | Opp/App/Dpp ABC systems | transport | peptides into *B. subtilis* | Hughes et al. 2022 | “Three high-affinity… transporters are involved in peptide uptake—the… Opp… App… and… Dpp.” | **High confidence; downstream module.** Uptake alone is not proof of extracellular protein hydrolysis (hughes2022peptidetransportin pages 1-3). |
| 8 | OppA | preferentially binds | tetra- and pentapeptides | Hughes et al. 2022 | “OppA has highest affinity for tetra- and penta-peptides.” | **High confidence; biochemical/assay-specific.** Reported peptide Kd values were 0.4 and 2 µM (hughes2022peptidetransportin pages 1-3). |
| 9 | extracellular proteases of *B. subtilis* | degrade | environmental proteins as carbon and nitrogen sources | Harwood & Kikuchi 2022, DOI [10.1093/femsre/fuab046](https://doi.org/10.1093/femsre/fuab046) | “roles in degrading environmental proteins as a source of carbon and nitrogen.” | **High confidence; trait-defining but taxon-specific** (harwood2022theinsand pages 14-15). |
| 10 | CodY | represses | *vpr* expression | Harwood & Kikuchi 2022 | “The vpr gene… [is] repressed by CodY.” | **High confidence; *B. subtilis*.** A CodY mutant increased Vpr expression **30–50-fold** (harwood2022theinsand pages 14-15). |
| 11 | phosphate starvation | induces | *vpr* expression | Harwood & Kikuchi 2022 | Vpr is induced under conditions “such as phosphate starvation.” | **High confidence; *B. subtilis*-specific environmental regulation** (harwood2022theinsand pages 14-15). |
| 12 | CodY/AbrB/ScoC-associated regulation | represses | *nprE* | Harwood & Kikuchi 2022 | NprE is “repressed as a member of the ScoB, AbrB and CodY regulons.” | **Moderate-to-high; nomenclature should be checked against the primary regulatory paper** (harwood2022theinsand pages 13-14). |
| 13 | *aprE* + *nprE* deletion | decreases | culture-medium protease activity | Harwood & Kikuchi 2022 | Deletions “reduce the protease activity of the culture medium by 95%.” | **High confidence, genetic intervention; *B. subtilis*.** Supports AprE/NprE as major extracellular contributors, not necessarily the complete nutritional pathway (harwood2022theinsand pages 14-15, harwood2022theinsand pages 13-14). |
| 14 | Vpr signal peptide/preproprotein | enables | secretion and extracellular maturation of Vpr | Harwood & Kikuchi 2022 | PreproVpr has a “28-residue signal sequence and a 132-residue propeptide”; mature protein was isolated from culture medium. | **High confidence; *B. subtilis*.** Prefer `has_signal_peptide` and `localized_to` rather than asserting a secretion system not established in this excerpt (harwood2022theinsand pages 14-15). |
| 15 | WprA precursor processing during secretion | produces/localizes | cell-wall-associated protease | Harwood & Kikuchi 2022 | “processing of the WprA precursor during secretion” accompanies formation of cell-wall proteins. | **High confidence localization, but primarily quality control.** Keep outside the minimal nutritional graph unless substrate-to-nutrition evidence is added (harwood2022theinsand pages 14-15, harwood2022theinsand pages 13-14). |
| 16 | extracellular endopeptidase production | causes | clearing halo on protein agar | Song et al. 2023 | “Protease production is indicated by the formation of clear halos… This occurs when extracellular endopeptidases are produced.” | **High confidence assay edge.** Applicable to skim milk, casein, BSA, gelatin, keratin, fibrin, or elastin agar, but halos miss weak enzymes and many exopeptidases (song2023microbialproteasesand pages 2-3). |
| 17 | protease | hydrolyzes | casein to acid-soluble peptides/amino acids | Song et al. 2023 | “Protease hydrolyzes casein… to produce peptides or amino acids that are soluble in an acidic solution.” | **High confidence assay chemistry.** Temperature and pH are explicit assay conditions, not universal biological optima (song2023microbialproteasesand pages 2-3). |
| 18 | protein-rich jellyfish detritus | enriches | protein/amino-acid catabolic enzymes in marine bacteria | Tinta et al. 2023, DOI [10.1186/s40168-023-01598-8](https://doi.org/10.1186/s40168-023-01598-8) | Jelly-OM caused “significant enrichment of protein/amino acid catabolism-related enzymes.” | **High confidence at community level; microcosm/metaproteomics evidence** (tinta2023jellyfishdetritussupports pages 1-2). |
| 19 | Pseudoalteromonadaceae | synthesize and excrete | proteolysis-associated enzymes | Tinta et al. 2023 | “Pseudoalteromonadaceae synthesized and excreted enzymes associated with proteolysis.” | **High confidence community/taxon-family association**, not a universal property of every member (tinta2023jellyfishdetritussupports pages 1-2). |
| 20 | Vibrionaceae | synthesize | peptide and amino-acid transporters | Tinta et al. 2023 | “Vibrionaceae synthesized transporter proteins for peptides [and] amino acids… exhibiting a cheater-type lifestyle.” | **High confidence community observation.** Demonstrates cross-feeding; do not assign the proteolysis trait to these organisms from transporters alone (tinta2023jellyfishdetritussupports pages 1-2). |
| 21 | jellyfish-OM amendment | enriches | secretory S8/subtilisin-family proteases | Tinta et al. 2023 | “>70% of all proteases” in two exoproteome fractions were considered secretory; S8 proteases represented about **66%** and **54%** of all proteases in those fractions. | **High confidence for the experiment**, but secretion assignment included signal-peptide/exoproteome criteria and could not fully exclude proteins released by dead cells (tinta2023jellyfishdetritussupports pages 7-10). |
| 22 | I39-family inhibitor abundance | associates with | jellyfish-OM proteolytic response | Tinta et al. 2023 | Inhibitors represented **14.9 ± 0.06%** of proteins in late-exponential endometaproteomes and **6.3 ± 0.7%** in an exoproteome fraction during decay. | **Uncertain causal edge.** Association does not identify the inhibited protease or direction of pathway flux; retain as contextual only (tinta2023jellyfishdetritussupports pages 7-10). |

## 5. Minimal YAML-oriented graph recommendation

The most defensible **generic core** is:

1. `extracellular_protein` — **substrate_of** → `secreted_or_cell_envelope_endopeptidase`
2. `secreted_or_cell_envelope_endopeptidase` — **catalyzes** → `extracellular_protein_hydrolysis`
3. `extracellular_protein_hydrolysis` — **produces** → `oligopeptide`
4. `extracellular_exopeptidase` — **catalyzes_terminal_cleavage_of** → `oligopeptide`
5. `terminal_peptide_cleavage` — **produces** → `amino_acid`
6. `peptide_ABC_transporter` — **imports** → `oligopeptide`
7. `amino_acid_transporter` — **imports** → `amino_acid`
8. `imported_peptide_or_amino_acid` — **supports** → `cellular_nitrogen_nutrition`
9. `cellular_nitrogen_nutrition` — **supports** → `microbial_growth`

Edges 1–3 and 8 are trait-defining. Edges 4–7 are common but not universal: some organisms import peptides and finish hydrolysis intracellularly, whereas others release more amino acids outside the cell. Accordingly, localization should be attached to each enzyme rather than assumed from the enzyme class (hughes2022peptidetransportin pages 1-3, kieliszek2021characteristicsofthe pages 2-4, song2023microbialproteasesand pages 2-3).

A **B. subtilis extension** may add AprE/NprE/Vpr, CodY, phosphate starvation, and Opp/App/Dpp. A **LAB extension** may add PrtP/CEP, casein, dairy environment, and amino-acid auxotrophy. These should not be merged into one universal mechanistic path without taxon qualifiers.

## 6. Recent developments, applications, and statistics

### Marine ecology and cross-feeding—2023

Tinta et al. provided a recent multi-omics implementation of the causal model in a coastal marine microcosm. Jellyfish organic matter is approximately **72 ± 14% protein** in its organic fraction, has a biomass C:N ratio of about **4.6 ± 0.1:1**, and can support bacterial specific growth rates of **0.2–7 d⁻¹**, versus commonly reported ocean microbiota rates of **0.1–1 d⁻¹**. The experiment resolved a division of labor: Pseudoalteromonadaceae secreted proteases, while Vibrionaceae emphasized uptake of the released peptides and amino acids (tinta2023jellyfishdetritussupports pages 1-2).

The same study found that secretory S8-family proteases dominated exoproteome proteases, while Pseudoalteromonadaceae contributed approximately **48%** and **94%** of S8 proteases in two extracellular fractions. M9 metalloproteases were less abundant, at roughly **1–2%** of detected proteases in relevant fractions (tinta2023jellyfishdetritussupports pages 7-10). This is strong evidence that extracellular proteolysis can act as a community “public-good” process; it also warns that transporter-rich beneficiaries should not automatically receive the trait annotation.

### Assay modernization and interpretation—2023

Song et al. reviewed halo assays, natural-substrate assays, chromogenic methods, and fluorescence/FRET substrates. Skim milk, casein, BSA, gelatin, keratin, fibrin, and elastin agar remain practical real-world screens. However, clearing halos preferentially detect extracellular endopeptidases with sufficient activity, so a negative plate does not exclude exopeptidases, low-activity enzymes, or proteases requiring different pH/substrate conditions (song2023microbialproteasesand pages 2-3).

### Food fermentation—2024

Proteolytic LAB fermentation is currently applied in dairy, meat, bakery, brewing, vegetable, fish, and sourdough systems. The 2024 review associates *Lactobacillus delbrueckii* subsp. *bulgaricus* and *Lactiplantibacillus plantarum* with production of antioxidant, antihypertensive, antimicrobial, and other peptides in fermented foods. Reported strain optima in the review include pH ranges of approximately **5.5–6.8** and temperatures of **37–46 °C**, but these are strain/application data rather than generic optima for the trait (ter2024areviewon pages 3-4).

### Industrial strain engineering

Extracellular proteolysis is beneficial for detergent, food, leather, waste-treatment, and peptide-production processes, but detrimental when *Bacillus* is used to secrete a heterologous protein. In *B. subtilis*, deleting *aprE* and *nprE* removes about **95%** of culture-medium protease activity. Conversely, the organism’s secretion capacity can permit target-protein accumulation above **20 g L⁻¹**, motivating industrial protease-deficient production strains (harwood2022theinsand pages 14-15, harwood2022theinsand pages 13-14). This application illustrates an important causal validation strategy: loss-of-function of extracellular protease genes should reduce substrate hydrolysis and, under protein-dependent growth conditions, reduce nutritional access.

## 7. Expert interpretation

The authoritative Bacillus review emphasizes that extracellular proteases are multifunctional: feeding, quality control, signaling, and protein processing coexist. Therefore, **gene presence is weaker evidence than a complete functional chain** consisting of extracellular localization, protein hydrolysis, product uptake, and a nutritional/growth consequence. Even deletion of all major extracellular proteases may have little effect in nutrient-rich laboratory medium, although it can impair environmental competitiveness; assays should therefore use protein as the relevant limiting carbon or nitrogen source (harwood2022theinsand pages 14-15, harwood2022theinsand pages 15-16).

For community studies, extracellular proteolysis should be attributed to the enzyme producer when signal-peptide, exoproteomic, transcriptomic, or genetic evidence supports secretion. Organisms expressing only peptide transporters should be represented as cross-feeders, not proteolytic organisms. Tinta et al.’s producer–beneficiary partition provides a particularly clear recent example (tinta2023jellyfishdetritussupports pages 1-2, tinta2023jellyfishdetritussupports pages 7-10).

## 8. Claims not yet ready for TraitMech curation

1. **A universal Sec edge for every extracellular protease.** Signal peptides support export, but Sec, Tat, type I/II secretion, autotransport, vesicles, or nonclassical release must be established protein by protein.
2. **Universal induction by protein or nitrogen starvation.** Regulation differs substantially among taxa and proteases; retain CodY, phosphate-starvation, DegU, AbrB, and stationary-phase edges as taxon/gene-specific.
3. **Universal extracellular exopeptidase completion to free amino acids.** Some systems import oligopeptides and hydrolyze them intracellularly.
4. **Trait assignment from a protease-domain gene alone.** Many proteases are intracellular quality-control, regulatory, signaling, sporulation, or virulence proteins.
5. **Trait assignment from peptide/amino-acid transporters alone.** These can identify cross-feeders that consume public goods made by other organisms.
6. **Trait assignment from a clearing halo alone.** The assay supports secreted endoprotease activity but not necessarily nutritional use or the identity of the enzyme.
7. **Direct I39-inhibitor causal edges.** The 2023 marine study established enrichment, not the specific inhibited enzyme or physiological outcome.
8. **Generic pH, temperature, salt, or metal-direction edges.** Optima and inhibition are protease- and strain-specific; add only with enzyme-resolved evidence.
9. **Collagenase equals nutritional proteolysis.** Collagen cleavage may support nutrition, tissue invasion, or both; nutritional assimilation must be demonstrated.
10. **All AprE/NprE/Vpr/Epr/WprA functions are nutritional.** Their processing, biofilm, signaling, and quality-control roles must be separated from feeding edges.

## 9. DOI-first bibliography

1. **Tinta T, Zhao Z, Bayer B, Herndl GJ.** “Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria.” *Microbiome* 11, 156. **Published July 2023.** DOI: [10.1186/s40168-023-01598-8](https://doi.org/10.1186/s40168-023-01598-8) (tinta2023jellyfishdetritussupports pages 1-2, tinta2023jellyfishdetritussupports pages 7-10).
2. **Song P et al.** “Microbial proteases and their applications.” *Frontiers in Microbiology* 14. **Published September 2023.** DOI: [10.3389/fmicb.2023.1236368](https://doi.org/10.3389/fmicb.2023.1236368) (song2023microbialproteasesand pages 2-3).
3. **Ter ZY et al.** “A review on proteolytic fermentation of dietary protein using lactic acid bacteria for the development of novel proteolytically fermented foods.” *International Journal of Food Science & Technology* 59:1213–1236. **Published January 2024.** DOI: [10.1111/ijfs.16888](https://doi.org/10.1111/ijfs.16888) (ter2024areviewon pages 3-4).
4. **Harwood CR, Kikuchi Y.** “The ins and outs of Bacillus proteases: activities, functions and commercial significance.” *FEMS Microbiology Reviews* 46. **Published August 2022.** DOI: [10.1093/femsre/fuab046](https://doi.org/10.1093/femsre/fuab046) (harwood2022theinsand pages 14-15, harwood2022theinsand pages 13-14, harwood2022theinsand pages 15-16).
5. **Hughes AM et al.** “Peptide transport in *Bacillus subtilis*—structure and specificity in the extracellular solute binding proteins OppA and DppE.” *Microbiology* 168:001274. **Published December 1, 2022.** DOI: [10.1099/mic.0.001274](https://doi.org/10.1099/mic.0.001274) (hughes2022peptidetransportin pages 1-3, hughes2022peptidetransportin media 8f9fa6d3).
6. **Kieliszek M et al.** “Characteristics of the Proteolytic Enzymes Produced by Lactic Acid Bacteria.” *Molecules* 26:1858. **Published March 2021.** DOI: [10.3390/molecules26071858](https://doi.org/10.3390/molecules26071858) (kieliszek2021characteristicsofthe pages 11-13, kieliszek2021characteristicsofthe pages 2-4).
7. **Rao MB, Tanksale AM, Ghatge MS, Deshpande VV.** “Molecular and Biotechnological Aspects of Microbial Proteases.” *Microbiology and Molecular Biology Reviews* 62:597–635. **Published September 1998.** DOI: [10.1128/MMBR.62.3.597-635.1998](https://doi.org/10.1128/MMBR.62.3.597-635.1998) (rao1998molecularandbiotechnological pages 1-2).

References

1. (harwood2022theinsand pages 14-15): Colin R Harwood and Yoshimi Kikuchi. The ins and outs of bacillus proteases: activities, functions and commercial significance. FEMS Microbiology Reviews, Aug 2022. URL: https://doi.org/10.1093/femsre/fuab046, doi:10.1093/femsre/fuab046. This article has 131 citations and is from a domain leading peer-reviewed journal.

2. (harwood2022theinsand pages 15-16): Colin R Harwood and Yoshimi Kikuchi. The ins and outs of bacillus proteases: activities, functions and commercial significance. FEMS Microbiology Reviews, Aug 2022. URL: https://doi.org/10.1093/femsre/fuab046, doi:10.1093/femsre/fuab046. This article has 131 citations and is from a domain leading peer-reviewed journal.

3. (rao1998molecularandbiotechnological pages 1-2): Mala B. Rao, Aparna M. Tanksale, Mohini S. Ghatge, and Vasanti V. Deshpande. Molecular and biotechnological aspects of microbial proteases. Microbiology and Molecular Biology Reviews, 62:597-635, Sep 1998. URL: https://doi.org/10.1128/mmbr.62.3.597-635.1998, doi:10.1128/mmbr.62.3.597-635.1998. This article has 3597 citations and is from a domain leading peer-reviewed journal.

4. (tinta2023jellyfishdetritussupports pages 7-10): Tinkara Tinta, Zihao Zhao, Barbara Bayer, and Gerhard J. Herndl. Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01598-8, doi:10.1186/s40168-023-01598-8. This article has 25 citations and is from a highest quality peer-reviewed journal.

5. (kieliszek2021characteristicsofthe pages 2-4): Marek Kieliszek, Katarzyna Pobiega, Kamil Piwowarek, and Anna M. Kot. Characteristics of the proteolytic enzymes produced by lactic acid bacteria. Molecules, 26:1858, Mar 2021. URL: https://doi.org/10.3390/molecules26071858, doi:10.3390/molecules26071858. This article has 534 citations.

6. (song2023microbialproteasesand pages 2-3): Peng Song, Xue Zhang, Shuhua Wang, Wei Xu, Fei Wang, Rongzhao Fu, and Feng Wei. Microbial proteases and their applications. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1236368, doi:10.3389/fmicb.2023.1236368. This article has 264 citations and is from a peer-reviewed journal.

7. (hughes2022peptidetransportin pages 1-3): Adam M. Hughes, John F. Darby, Eleanor J. Dodson, Samuel J. Wilson, Johan P. Turkenburg, Gavin H. Thomas, and Anthony J. Wilkinson. Peptide transport in bacillus subtilis – structure and specificity in the extracellular solute binding proteins oppa and dppe. Dec 2022. URL: https://doi.org/10.1099/mic.0.001274, doi:10.1099/mic.0.001274. This article has 27 citations and is from a peer-reviewed journal.

8. (hughes2022peptidetransportin media 8f9fa6d3): Adam M. Hughes, John F. Darby, Eleanor J. Dodson, Samuel J. Wilson, Johan P. Turkenburg, Gavin H. Thomas, and Anthony J. Wilkinson. Peptide transport in bacillus subtilis – structure and specificity in the extracellular solute binding proteins oppa and dppe. Dec 2022. URL: https://doi.org/10.1099/mic.0.001274, doi:10.1099/mic.0.001274. This article has 27 citations and is from a peer-reviewed journal.

9. (harwood2022theinsand pages 13-14): Colin R Harwood and Yoshimi Kikuchi. The ins and outs of bacillus proteases: activities, functions and commercial significance. FEMS Microbiology Reviews, Aug 2022. URL: https://doi.org/10.1093/femsre/fuab046, doi:10.1093/femsre/fuab046. This article has 131 citations and is from a domain leading peer-reviewed journal.

10. (tinta2023jellyfishdetritussupports pages 1-2): Tinkara Tinta, Zihao Zhao, Barbara Bayer, and Gerhard J. Herndl. Jellyfish detritus supports niche partitioning and metabolic interactions among pelagic marine bacteria. Microbiome, Jul 2023. URL: https://doi.org/10.1186/s40168-023-01598-8, doi:10.1186/s40168-023-01598-8. This article has 25 citations and is from a highest quality peer-reviewed journal.

11. (ter2024areviewon pages 3-4): Zhi Yin Ter, Lee Sin Chang, Abdul Salam Babji, Nurul Aqilah Mohd Zaini, Shazrul Fazry, Shahrul Razid Sarbini, Clemens Karl Peterbauer, and Seng Joe Lim. A review on proteolytic fermentation of dietary protein using lactic acid bacteria for the development of novel proteolytically fermented foods. International Journal of Food Science &amp; Technology, 59:1213-1236, Jan 2024. URL: https://doi.org/10.1111/ijfs.16888, doi:10.1111/ijfs.16888. This article has 54 citations and is from a peer-reviewed journal.

12. (kieliszek2021characteristicsofthe pages 11-13): Marek Kieliszek, Katarzyna Pobiega, Kamil Piwowarek, and Anna M. Kot. Characteristics of the proteolytic enzymes produced by lactic acid bacteria. Molecules, 26:1858, Mar 2021. URL: https://doi.org/10.3390/molecules26071858, doi:10.3390/molecules26071858. This article has 534 citations.