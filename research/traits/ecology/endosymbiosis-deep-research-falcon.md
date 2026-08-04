---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:46:58.091221'
end_time: '2026-08-04T14:55:38.832362'
duration_seconds: 520.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: endosymbiosis
  trait_identifier: traitmech:000045
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: endosymbiosis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which the microorganism lives inside the cells or tissues
    of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently
    undergo extreme genome reduction.
  parent_traits: traitmech:000040
  synonyms: endosymbiont
  evidence_summary: 'DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome
    reduction in symbiotic bacteria", characterize intracellular endosymbionts and
    their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe
    rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic
    lifestyle.)'
  causal_graph_summary: 'endosymbiosis_intracellular_genome_reduction: 10 nodes, 7
    edges'
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
- **Trait label:** endosymbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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
- **Trait label:** endosymbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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


# Curation report: microbial endosymbiosis

## Trait record and scope

- **Trait label:** endosymbiosis
- **Trait identifier:** `traitmech:000045`
- **Category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Parent:** `traitmech:000040`
- **Operational definition:** a microbial lifestyle/localization trait in which a microorganism resides within the cells or tissues of a host.

For causal-graph curation, the defining phenotype should be **host-internal residence**, preferably demonstrated at cellular resolution. Residence may be directly in host cytoplasm, in bacteriocytes, or inside a host-derived membrane compartment such as a symbiosome. The trait does **not** imply mutualism, obligacy, vertical transmission, nutritional provisioning, or genome reduction; these are frequent but separable properties. For example, *Symbiodolus* occurs intracellularly throughout host development and is concentrated in ovaries, but its secretion systems, nutritional benefits, and entry mechanisms remain largely inferred rather than causally demonstrated (wierz2024intracellularsymbiontsymbiodolus pages 1-2).

### Boundary cases

1. **Ectosymbiosis is excluded**, even when host and microbe exhibit strong genomic or metabolic coupling. Surface attachment to gill epithelial cells is not intracellular residence.
2. **Tissue-associated microbiota are not automatically endosymbionts.** Localization inside host tissue but outside host cells should be represented separately if the ontology distinguishes tissue-level endosymbiosis from intracellular endosymbiosis.
3. **Intracellular pathogens are a semantic boundary.** The supplied definition does not require mutual benefit, so persistent intracellular parasitic associations may satisfy the localization phenotype. Curators should avoid silently restricting the trait to mutualists.
4. **Organelles are evolutionary products of ancient endosymbiosis**, but mitochondria and plastids should not normally be annotated as extant microbial endosymbionts.
5. **Genome reduction is neither necessary nor sufficient.** It commonly follows obligate intracellular association, but reduced genomes can also occur in tightly coupled ectosymbionts.
6. **Rhizobia are stage-dependent.** Free-living rhizobia are not endosymbiotic; bacteroids enclosed within plant-derived symbiosomes are.

## Current mechanistic model

The most defensible general model is not a single universal pathway. Endosymbiosis is an emergent state produced by several modules:

1. **Entry and intracellular accommodation:** host-cell invasion or uptake, followed by residence in cytoplasm or a host-derived compartment.
2. **Immune modulation and population control:** localized immune tolerance, antimicrobial peptides, pattern-recognition proteins, metal limitation, autophagy, apoptosis, or lysosomal digestion.
3. **Bidirectional exchange:** hosts provide carbon, nitrogen precursors, iron, oxygen, or other substrates; symbionts provide amino acids, vitamins, fixed nitrogen, or chemosynthetic carbon.
4. **Transmission and persistence:** vertical, horizontal, or mixed transmission maintains the association.
5. **Evolutionary dependency:** isolation, bottlenecks, relaxed selection, and loss of repair/recombination functions promote genome degeneration and metabolic complementation.

Comparative analysis of 34 independently degenerating *Sodalis* lineages illustrates that this evolutionary module is partly deterministic and partly contingent: amino-acid-biosynthesis genes were preferentially lost, host-beneficial B-vitamin pathways retained, and redundant respiratory-chain and DNA-repair functions lost stochastically (boyd2024stochasticitydeterminismand pages 1-2). The authors identify host-cell isolation, transovarial bottlenecks, and repair/recombination loss as processes expected to reduce effective selection and increase mutational load; these are mechanistic explanations, not individually proven universal causes (boyd2024stochasticitydeterminismand pages 1-2).

## Candidate graph nodes

Identifiers below are conservative suggestions. Taxon-specific proteins are left label-only when a stable accession was not verified.

### Trait, localization, and host structures

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| endosymbiosis | `traitmech:000045` | Target trait; quote verbatim in YAML. |
| host cell | `GO:0005623` | General intracellular context. |
| cytoplasm | `GO:0005737` | Appropriate for cytoplasmic bacteriocytes such as cockroach–*Blattabacterium*. |
| membrane | `GO:0016020` | Generic only; prefer “symbiosome membrane” label where the specialized structure is intended. |
| symbiosome | label-only candidate | Host-derived membrane plus symbiosome space and bacteroid; ontology mapping should be verified locally. |
| symbiosome membrane | label-only candidate | Interface for host–rhizobium nutrient exchange. |
| bacteriocyte | label-only candidate | Specialized symbiont-bearing host cell. |
| bacteriome | label-only candidate | Organ composed of bacteriocytes in many insects. |
| root nodule | `GO:0042129` | Verify local ontology treatment before use. |
| intracellular anatomical structure | `GO:0005622` | Broad fallback; less informative than bacteriocyte/symbiosome. |

### Biological processes and modules

| Candidate node | Suggested grounding | Evidence relevance |
|---|---|---|
| nitrogen fixation | `GO:0009399` | Bacteroid conversion of N₂ to ammonia. |
| transmembrane transport | `GO:0055085` | Nutrient movement across host or symbiosome membranes. |
| amino-acid biosynthetic process | `GO:0008652` | Symbiont provisioning and metabolic complementation. |
| vitamin biosynthetic process | `GO:0009110` | Retained host-beneficial function in reduced genomes. |
| DNA repair | `GO:0006281` | Frequently lost or partitioned between co-symbionts. |
| mismatch repair | `GO:0006298` | Buchnera–Serratia complementation. |
| autophagy | `GO:0006914` | Host-mediated bacteriocyte/endosymbiont recycling. |
| apoptotic process | `GO:0006915` | Developmental elimination of insect symbionts. |
| response to oxidative stress | `GO:0006979` | Relevant to oxygen control, iron, and intracellular stress. |
| vertical transmission | label-only candidate | Do not substitute a reproductive-process GO term without verification. |
| genome reduction/genome degeneration | label-only candidate | Evolutionary process, not the defining trait. |
| metabolic complementation | label-only candidate | Important graph-level concept but not necessarily a standardized ontology class. |
| chemosynthesis | label-only candidate | Use a more specific methane- or sulfur-oxidation process when demonstrated. |

### Genes, proteins, transporters, and complexes

| Node | Grounding recommendation | Role |
|---|---|---|
| ApGLNT1 | label-only; verify aphid gene/protein accession | Host glutamine transporter regulating substrate supply to *Buchnera*. |
| MtVTL8 | label-only; verify *Medicago truncatula* accession | Host VTL-family iron transporter required for bacteroid survival and symbiotic nitrogen fixation. |
| MtVTL4 | label-only | Related iron transporter that did not functionally replace MtVTL8 in the tested context. |
| nitrogenase NifH/NifDK | `GO:0016163` for nitrogenase activity; protein accessions taxon-specific | Oxygen-labile Fe–S/FeMo enzyme system reducing N₂. |
| FixABCX | label-only complex; ground components per organism | Transfers reducing equivalents to nitrogenase. |
| leghemoglobin | label-only protein; accession host-specific | Buffers and delivers oxygen in nodules. |
| thrABC | gene labels; ground per symbiont genome | Threonine-biosynthesis operon in *Sodalis pierantonius*. |
| aspC1, tyrA | gene labels; ground per symbiont genome | Tyrosine-biosynthesis functions associated with host cuticle development. |
| MutH/MutL/MutS | protein labels; ground per symbiont | Partitioned mismatch-repair system in aphid co-symbionts. |
| transferrin, ferritin, bacterioferritin | GO molecular-function terms or verified accessions | Candidate host/symbiont iron-control module. |
| PGRP-LB proteins | verified protein accession needed | Pattern recognition and immune modulation; system-dependent. |
| cathepsins | EC/protein-specific grounding needed | Candidate lysosomal digestion/control of marine chemosymbionts. |
| defensin_g9, defensin_g10, termicin_g4 | label-only | Expression-associated candidates, not yet proven endosymbiont-control factors. |

### Chemicals and environmental factors

| Node | Suggested CURIE | Role |
|---|---|---|
| dinitrogen | `CHEBI:17997` | Nitrogenase substrate. |
| ammonia | `CHEBI:16134` | Product of nitrogen fixation and nitrogen recycling. |
| dioxygen | `CHEBI:15379` | Needed for respiration but inhibitory to nitrogenase at high concentration. |
| iron(2+) | `CHEBI:29033` | Cofactor supply to bacteroids and nitrogenase-associated systems. |
| glutamine | `CHEBI:18050` | Host-delivered nitrogen substrate in aphid–*Buchnera* integration. |
| arginine | `CHEBI:29016` | Symbiont-produced essential amino acid in aphids. |
| tyrosine | `CHEBI:18186` | Symbiont-linked precursor for DOPA and cuticle formation. |
| phenylalanine | `CHEBI:17295` | Nutritional/cuticle-related amino acid. |
| urea | `CHEBI:16199` | Nitrogen-recycling intermediate in cockroach symbiosis. |
| urate/uric acid | `CHEBI:17775` / verify protonation-specific term | Host nitrogen-storage metabolite. |
| methane | `CHEBI:16183` | Electron donor/carbon substrate for methanotrophic mussel endosymbionts. |
| hydrogen sulfide | `CHEBI:16136` | Reduced sulfur substrate for sulfur-oxidizing symbionts. |
| organic acids/dicarboxylates | label or specific CHEBI compounds | Plant carbon/reductant supplied to bacteroids. |
| rifampicin | `CHEBI:28077` | Experimental depletion factor; not an endogenous mechanism. |
| hypoxia | `ENVO:01001026` if compatible with local ontology | Protects oxygen-labile nitrogenase while permitting controlled respiration. |

## Candidate causal edges

“High” denotes direct perturbation or strong functional evidence; “moderate” denotes combined functional and expression/localization evidence; “uncertain” denotes inference, correlation, or a review-level proposal.

| Subject–predicate–object | Reference | Supporting snippet | Strength and curation note |
|---|---|---|---|
| **ApGLNT1 — transports/regulates supply of → glutamine to aphid bacteriocytes** | DOI: [10.1073/pnas.2308448120](https://doi.org/10.1073/pnas.2308448120), October 2023 | “host glutamine transporter GLNT1 is co-opted to regulate amino acid metabolism in aphid bacteriocytes” | **High, taxon-specific.** Functional characterization in *Xenopus* oocytes supports transporter activity (duncan2023cooptionofa pages 8-9). |
| **glutamine supply to bacteriocytes — supports → Buchnera arginine biosynthesis** | Same | Glutamine supply “is linked to Buchnera arginine synthesis.” | **Moderate–high.** Curate as aphid–*Buchnera* metabolic integration, not a universal endosymbiosis mechanism (duncan2023cooptionofa pages 8-9). |
| **MtVTL8 — enables transport of → Fe²⁺ across the symbiosome membrane** | DOI: [10.3389/fpls.2023.1306491](https://doi.org/10.3389/fpls.2023.1306491), published 4 January 2024 | “Mutants were tested in planta… and in an iron sensitive mutant yeast strain”; critical mutations failed to restore nitrogen fixation or yeast iron tolerance. | **High for iron-transport requirement; taxon-specific.** Exact Fe²⁺/H⁺ antiport versus uniport mechanism remains uncertain (cai2024expressionandmutagenesis pages 13-15, cai2024expressionandmutagenesis pages 8-10, cai2024expressionandmutagenesis pages 1-2). |
| **MtVTL8-dependent iron transport — enables → bacteroid survival and symbiotic nitrogen fixation** | Same | MtVTL8 “has been identified as essential for bacteria survival and therefore SNF.” | **High.** Suitable as a direct causal edge in a *Medicago* subgraph (cai2024expressionandmutagenesis pages 1-2). |
| **hypoxic nodule interior — protects → oxygen-labile nitrogenase** | Same | The outer nodule cells form “a gas diffusion barrier resulting in a hypoxic nodule interior… protecting the… oxygen-labile nitrogenase.” | **Moderate, review-supported within an original paper.** Rhizobial/nodule-specific (cai2024expressionandmutagenesis pages 1-2). |
| **leghemoglobin — buffers/delivers → oxygen to respiring bacteroids** | Same | Leghemoglobin supports “rapid binding and delivery of oxygen,” while maintaining low internal oxygen. | **Moderate, established consensus.** Do not generalize beyond legume nodules (cai2024expressionandmutagenesis pages 1-2). |
| **host-derived organic acids — fuel → bacteroid nitrogen fixation** | DOI: [10.1038/s41564-024-01762-2](https://doi.org/10.1038/s41564-024-01762-2), August 2024 | Organic acids are “transferred from plant cells to intracellular rhizobia to fuel N₂ fixation.” | **Moderate–high consensus edge.** The energetic cost reported is 16 ATP per N₂ fixed (porter2024hostimposedcontrolmechanisms pages 1-3, porter2024hostimposedcontrolmechanisms pages 3-4). |
| **rhizobial nitrogen fixation — increases → host nitrogen/fitness** | Same | Bacteroids “fix nitrogen and greatly enhance plant fitness in return for host-derived carbon.” | **High conceptual evidence; broad but rhizobium-specific** (porter2024hostimposedcontrolmechanisms pages 3-4). |
| **host antimicrobial/NCR peptides — cause → terminal bacteroid differentiation** | Same | “Some legumes secrete antimicrobial peptides that trigger the terminal differentiation of rhizobia into bacteroids.” | **Moderate–high, taxon-limited.** Some differentiated bacteroids become non-reproductive and may show increased N-per-C efficiency; not universal among legumes (porter2024hostimposedcontrolmechanisms pages 7-8). |
| **host autophagy and apoptosis — promote → developmental clearance of S. pierantonius** | DOI: [10.1186/s40168-023-01714-8](https://doi.org/10.1186/s40168-023-01714-8), December 2023 | “Endosymbiont clearance and recycling involve bacteriocyte autophagy and apoptosis”; autophagy/endosomal transport rises before clearance. | **Moderate–high, weevil-specific.** The 2023 study is time-resolved transcriptomic evidence integrated with prior functional work, not a single-gene knockout (ferrarini2023coordinationofhost pages 13-14). |
| **S. pierantonius thrABC — increases → threonine provisioning to host** | Same | The `thrABC` operon is induced after metamorphosis, and threonine is described as an essential amino acid provided by the endosymbiont. | **Moderate.** Expression timing supports provisioning but is not direct flux measurement (ferrarini2023coordinationofhost pages 8-10). |
| **S. pierantonius aspC1/tyrA — increases → tyrosine provisioning** | Same | `aspC1` and `tyrA` peak at D2/D3; tyrosine is a precursor of DOPA required for cuticle synthesis. | **Moderate, taxon-specific.** Prefer two edges: genes→tyrosine biosynthesis and tyrosine→DOPA/cuticle formation (ferrarini2023coordinationofhost pages 8-10). |
| **host transferrin/ferritin balance — modulates → iron availability and symbiont load** | Same | Transferrin may “sequester iron… to control bacterial growth or… directly deliver iron”; ferritin and transferrin show opposing expression. | **Uncertain. Do not curate as a directional causal edge yet.** Competing hypotheses remain (ferrarini2023coordinationofhost pages 13-14). |
| **Serratia-derived MutH/proteins — complement → Buchnera mismatch-repair deficiency** | DOI: [10.1073/pnas.2415651121](https://doi.org/10.1073/pnas.2415651121), December 2024 | Serratia MutH complemented deficient Buchnera repair components; 22 Serratia-derived proteins were detected in isolated Buchnera cells. | **High, aphid co-symbiont-specific.** Supported by protein identification and in-vitro functional assays (ling2024acompletedna pages 9-10). |
| **inter-symbiont mismatch-repair complementation — maintains → Buchnera genome integrity** | Same | A complete repair system assembled from two endosymbionts “ensure[d] the genome integrity of Buchnera.” | **High, taxon-specific** (ling2024acompletedna pages 9-10). |
| **Buchnera genome integrity — increases → aphid bacteriocyte heat tolerance** | Same | The assembled DNA-repair system enhanced “thermostability of aphid bacteriocytes.” | **High in the tested system; not a general genome-reduction edge** (ling2024acompletedna pages 9-10). |
| **obligate intracellular association — promotes → genome degeneration** | DOI: [10.1038/s41467-024-48784-2](https://doi.org/10.1038/s41467-024-48784-2), accepted 10 May 2024 | Isolation, vertical-transmission bottlenecks, and repair loss are described as exacerbating degenerative evolution. | **Moderate as a composite evolutionary edge.** Better represented through intermediate nodes rather than as a universal direct implication (boyd2024stochasticitydeterminismand pages 1-2). |
| **host nutritional demand — selects for retention of → symbiont B-vitamin pathways** | Same | Across 34 *Sodalis* lineages, B-vitamin-provisioning genes were retained while amino-acid-biosynthesis genes were lost. | **Moderate–high comparative evidence.** Direction is evolutionary selection/inference rather than experimental causation (boyd2024stochasticitydeterminismand pages 1-2). |
| **maternal/transovarial transmission — maintains → persistent host-associated endosymbiosis** | DOI: [10.1093/ismejo/wrae099](https://doi.org/10.1093/ismejo/wrae099), 2024 | FISH showed intracellular *Symbiodolus* in all life stages and high ovarian abundance indicating transovarial transmission. | **High for localization/transmission; moderate for maintenance causality.** Lack of cospeciation indicates occasional horizontal transmission (wierz2024intracellularsymbiontsymbiodolus pages 1-2). |
| **symbiont secretion systems/effectors — facilitate → host-cell entry** | Same | Multiple secretion systems and effectors “likely facilitate host-cell entry.” | **Uncertain.** Genomic potential only; retain as a hypothesis, not a curated causal edge (wierz2024intracellularsymbiontsymbiodolus pages 1-2). |
| **methane oxidation by intracellular symbionts — supplies → fixed carbon to mussel host** | DOI: [10.7554/eLife.88294](https://doi.org/10.7554/eLife.88294), version of record 5 August 2024 | Methane-oxidizing symbionts use reduced compounds to fix carbon and “turn into carbon source for the host mussel.” | **Moderate–high system-level evidence.** Specific transfer chemistry remains incompletely resolved (wang2024decipheringdeepseachemosynthetic pages 1-2). |
| **bacteriocyte lysosomal proteins/cathepsins — digest/control → mussel endosymbionts** | Same | Cathepsins were proposed as conserved tools hosts use to control resident symbionts. | **Uncertain.** Cell-type-specific expression is convincing, but causal digestion was not directly perturbed here (wang2024decipheringdeepseachemosynthetic pages 10-12). |
| **bacteriocyte solute carriers — transport → substrates and symbiont-derived nutrients** | Same | Solute carriers may shuttle nutrients “in and out of bacteriocytes”; several metal and ion transporters are expressed. | **Uncertain–moderate.** Expression/localization supports candidacy, not substrate-specific causal transport in this mussel (wang2024decipheringdeepseachemosynthetic pages 10-12). |
| **rifampicin depletion of Blattabacterium — changes → host amino-acid and nitrogen-recycling expression** | DOI: [10.3390/ijms25084228](https://doi.org/10.3390/ijms25084228), published 11 April 2024 | Quasi-aposymbionts strongly increased phenylalanine/tyrosine metabolism and decreased uricolysis/uric-acid synthesis. | **Moderate experimental perturbation, but confounding is possible.** Rifampicin and incomplete symbiont removal make the downstream biochemical interpretation less certain (silva2024comparativetranscriptomicsof pages 1-2, silva2024comparativetranscriptomicsof pages 21-22). |

The highest-priority edges are summarized below.

| subject | predicate | object | system/taxon | evidence strength | DOI |
|---|---|---|---|---|---|
| ApGLNT1 (host glutamine transporter) | facilitates glutamine supply to bacteriocytes, supporting | Buchnera arginine synthesis / host-symbiont metabolic integration | aphid–Buchnera endosymbiosis (*Acyrthosiphon pisum*; taxon-specific) (duncan2023cooptionofa pages 8-9) | strong experimental (functional characterization in *Xenopus* oocytes; transporter role demonstrated) | 10.1073/pnas.2308448120 |
| MtVTL8 (host iron transporter) | delivers Fe2+ across the symbiosome membrane, enabling | bacteroid survival and symbiotic nitrogen fixation | legume–rhizobium symbiosis (*Medicago truncatula* nodules; taxon-specific) (cai2024expressionandmutagenesis pages 1-2, cai2024expressionandmutagenesis pages 13-15, cai2024expressionandmutagenesis pages 8-10) | strong experimental (plant mutant complementation and yeast iron-tolerance assays) | 10.3389/fpls.2023.1306491 |
| Serratia-derived proteins / mismatch-repair complementation | restores Buchnera DNA mismatch repair, maintaining | Buchnera genome integrity and aphid heat tolerance | aphid co-obligate symbiosis (Buchnera + *Serratia*; taxon-specific) (ling2024acompletedna pages 9-10) | strong experimental (in vitro complementation assays; protein identification from isolated cells) | 10.1073/pnas.2415651121 |
| Host autophagy and apoptosis programs | promote | endosymbiont clearance / recycling of *Sodalis pierantonius* | cereal weevil bacteriome (*Sitophilus oryzae*; taxon-specific) (ferrarini2023coordinationofhost pages 13-14) | moderate-to-strong experimental (time-resolved transcriptomics integrated with prior functional interpretation; causal direction supported but not single-gene knockout here) | 10.1186/s40168-023-01714-8 |
| *Sodalis pierantonius* thrABC, aspC1, tyrA expression | increases production of threonine and tyrosine, supplying | host essential amino acids / cuticle precursor supply (via DOPA from tyrosine) | cereal weevil endosymbiosis (*Sitophilus oryzae*; taxon-specific) (ferrarini2023coordinationofhost pages 8-10) | moderate experimental (dual RNA-seq shows coordinated induction and timing before cuticle completion) | 10.1186/s40168-023-01714-8 |
| Host-derived organic acids | fuel | rhizobial nitrogen fixation | legume symbiosomes / bacteroids (broad rhizobial endosymbiosis; not universal to all endosymbioses) (porter2024hostimposedcontrolmechanisms pages 1-3, porter2024hostimposedcontrolmechanisms pages 3-4) | strong review-supported consensus, weaker as direct single-study causal assay in cited context | 10.1038/s41564-024-01762-2 |


*Table: This table summarizes the strongest, most curation-ready causal edges for the endosymbiosis trait, emphasizing experimentally supported mechanisms and clearly noting taxon specificity. It is useful as a compact starting point for selecting high-confidence nodes and edges for TraitMech graph curation.*

## Recommended YAML graph architecture

A robust graph should separate **core definitional**, **frequent consequence**, and **taxon-specific mechanism** layers.

### Core layer

- microorganism **located_in** host cell/tissue
- microorganism **located_in** bacteriocyte or symbiosome
- intracellular localization **realizes** `traitmech:000045`

These edges require localization evidence such as microscopy, FISH, TEM, or well-established cell biology. Genomic signatures alone are inadequate.

### Conserved mechanistic layer

- intracellular compartmentation **enables** metabolite exchange
- host transporter **transports** nutrient across host/symbiosome membrane
- symbiont biosynthetic pathway **produces** host-limiting nutrient
- host immune/population-control process **regulates** endosymbiont abundance
- vertical transmission **maintains** association across generations
- host-cell isolation + transmission bottlenecks + repair loss **promote** genome degeneration
- genome degeneration **increases dependence_on** host or co-symbiont metabolic functions

These relationships recur across systems, but graph instances should preserve the taxon and experimental context.

### Taxon-specific branches

1. **Aphid–Buchnera:** ApGLNT1 → glutamine delivery → *Buchnera* arginine synthesis.
2. **Aphid–Buchnera–Serratia:** inter-symbiont protein transfer/MMR complementation → genome integrity → heat tolerance.
3. **Weevil–Sodalis:** `thrABC`/`aspC1`/`tyrA` → amino-acid provisioning; host autophagy/apoptosis → developmental clearance.
4. **Legume–rhizobium:** organic acids + controlled oxygen + Fe²⁺ transport → nitrogenase activity → ammonia/host nitrogen; NCR peptides → terminal bacteroid differentiation.
5. **Mussel–methanotroph:** methane oxidation/carbon fixation → host nutrition, with transport and lysosomal “milking/farming” mechanisms retained as provisional.
6. **Cockroach–Blattabacterium:** urea/ammonia recycling and aromatic-amino-acid complementation, currently supported mainly by depletion/transcriptomic evidence.

## Recent developments and quantitative evidence

- The 2024 *Sodalis* study analyzed **34 independently degenerating lineages**, allowing repeated evolutionary outcomes to be distinguished from contingency. It retained **297 single-copy orthologs** for comparative phylogenomics; amino-acid pathways were preferentially lost and B-vitamin pathways retained (boyd2024stochasticitydeterminismand pages 1-2, boyd2024stochasticitydeterminismand pages 9-10).
- Legume infected cells may contain **10³–10⁴ symbiosomes**, with approximately **1–50 bacteroids per symbiosome**. Nitrogen fixation requires approximately **16 ATP per N₂ molecule fixed**, illustrating the large carbon and respiratory demand imposed on the host (porter2024hostimposedcontrolmechanisms pages 1-3).
- The 2023 weevil dual-transcriptomic study detected **4,078 host genes** differentially expressed in at least one young-adult stage between symbiotic and aposymbiotic insects; 1,917 were stage-specific, 1,747 changed in multiple conditions, and 414 showed mixed profiles (ferrarini2023coordinationofhost pages 8-10).
- The 2024 aphid co-symbiont study detected **22 Serratia-derived proteins** within isolated *Buchnera*, spanning six biological processes, and functionally linked inter-symbiont repair complementation to heat tolerance (ling2024acompletedna pages 9-10).
- The 2024 deep-sea mussel study built a gill atlas with **13 cell types**, including three previously unknown types, from mussels at a methane seep **1,100 m** deep. Bacteriocyte expression implicated lysosomes, vesicle transport, amino-acid transport, and several metal-ion solute carriers (wang2024decipheringdeepseachemosynthetic pages 10-12, wang2024decipheringdeepseachemosynthetic pages 1-2).
- *Symbiodolus* genomes were sampled across **16 host taxa**, while FISH and screening indicated occurrence in at least **six insect orders**; high ovarian abundance supports vertical transmission, but absence of strict cospeciation supports a mixed transmission mode (wierz2024intracellularsymbiontsymbiodolus pages 1-2).
- In quasi-aposymbiotic cockroaches, defensin candidates showed approximately **7- and 8.5-fold** expression differences, while a termicin candidate changed approximately **7.9-fold**. Their much higher hemolymph expression argues against immediate curation as bacteriocyte-control factors (silva2024comparativetranscriptomicsof pages 14-15, silva2024comparativetranscriptomicsof pages 21-22).

## Applications and real-world relevance

1. **Sustainable agriculture.** Rhizobial inoculants and legume breeding aim to increase nitrogen fixation while limiting occupancy by ineffective strains. Current expert analysis emphasizes partner choice, compartmentalization, carbon/oxygen allocation, and post-infection sanctions as potential breeding or microbiome-engineering targets; however, host control is imperfect and strongly genotype- and environment-dependent (porter2024hostimposedcontrolmechanisms pages 5-6, porter2024hostimposedcontrolmechanisms pages 3-4, porter2024hostimposedcontrolmechanisms pages 7-8).
2. **Crop iron and nitrogen management.** MtVTL8 demonstrates that host control of iron delivery across the symbiosome membrane is indispensable for bacteroid survival and nitrogen fixation. VIT/VTL transporter knowledge may also inform agronomic biofortification, although a biofortification role should not be conflated with the endosymbiotic mechanism (cai2024expressionandmutagenesis pages 13-15, cai2024expressionandmutagenesis pages 1-2).
3. **Insect pest biology.** Nutrient-provisioning endosymbionts support insects on deficient diets and can affect cuticle formation, development, heat tolerance, and invasion. These dependencies provide possible control targets, but broad-spectrum antibiotics such as rifampicin have substantial off-target and ecological limitations (silva2024comparativetranscriptomicsof pages 1-2, ferrarini2023coordinationofhost pages 8-10).
4. **Climate resilience.** The aphid work shows that complementary functions distributed across obligate and facultative symbionts can stabilize bacteriocytes under heat stress, suggesting that holobiont thermal tolerance cannot always be predicted from a single symbiont genome (ling2024acompletedna pages 9-10).
5. **Deep-sea ecosystem function.** Methane- and sulfur-oxidizing intracellular symbionts convert reduced geochemical compounds into host biomass, supporting dominant animal populations at vents and seeps and coupling methane/sulfur cycling to animal production (wang2024decipheringdeepseachemosynthetic pages 1-2).

## Expert interpretation

Three principles are especially important for TraitMech curation.

First, **endosymbiosis should be represented as a host–microbe relational phenotype, not as a microbial gene-defined capability**. No single gene or pathway is sufficient. Localization evidence establishes the trait; genes describe how a particular association is established or maintained.

Second, **metabolic incompleteness can be adaptive or tolerated only at the holobiont level**. The 34-lineage *Sodalis* comparison shows convergent retention of host-beneficial vitamins alongside variable loss of redundant cellular functions, whereas the aphid study shows repair functions assembled across two bacterial partners. Consequently, absence of a complete pathway from one symbiont genome should not be interpreted as absence of function in the endosymbiotic consortium (ling2024acompletedna pages 9-10, boyd2024stochasticitydeterminismand pages 1-2).

Third, **host control is conditional rather than absolute**. In legumes, partner choice, resource allocation, terminal differentiation, sanctions, immunity, and autophagy act as partially effective “sieves.” In insects, the same molecule class can support tolerance in one system and bacterial clearance in another. Edges involving AMPs, PGRPs, lectins, autophagy, or metal sequestration therefore require organism- and stage-specific qualifiers (silva2024comparativetranscriptomicsof pages 21-22, porter2024hostimposedcontrolmechanisms pages 5-6, porter2024hostimposedcontrolmechanisms pages 7-8, ferrarini2023coordinationofhost pages 13-14).

## Claims that should not yet be curated

- Do not assert that **all endosymbionts have reduced genomes**, are vertically transmitted, are obligate, or are mutualists.
- Do not curate *Symbiodolus* secretion systems as proven causes of host-cell entry; the authors use “likely” (wierz2024intracellularsymbiontsymbiodolus pages 1-2).
- Do not curate *Symbiodolus* amino-acid/cofactor pathways as demonstrated host provisioning without metabolite-transfer or host-fitness assays (wierz2024intracellularsymbiontsymbiodolus pages 1-2).
- Do not choose between **transferrin-mediated iron sequestration** and **iron delivery** in weevil bacteriocytes; both remain viable explanations (ferrarini2023coordinationofhost pages 13-14).
- Do not curate mussel cathepsins, vesicle transport, or solute carriers as confirmed nutrient-transfer mechanisms solely from cell-specific expression (wang2024decipheringdeepseachemosynthetic pages 10-12).
- Do not encode MtVTL8 specifically as an Fe²⁺/H⁺ antiporter. Iron-transport function is supported, but antiport versus uniport and transport stoichiometry remain unresolved (cai2024expressionandmutagenesis pages 13-15).
- Do not curate cockroach defensin_g9, defensin_g10, termicin_g4, or orphan cysteine-rich proteins as endosymbiont-control effectors. Their expression patterns identify candidates only, and several are predominantly expressed in hemolymph (silva2024comparativetranscriptomicsof pages 14-15, silva2024comparativetranscriptomicsof pages 21-22).
- Treat rifampicin-based quasi-aposymbiotic comparisons cautiously because antibiotic exposure and incomplete depletion can confound direct attribution to symbiont absence (silva2024comparativetranscriptomicsof pages 1-2, silva2024comparativetranscriptomicsof pages 21-22).
- Do not generalize rhizobial NCR-mediated terminal differentiation, host sanctions, or symbiosome organization to non-rhizobial endosymbioses.
- Avoid a direct universal edge `endosymbiosis causes genome reduction`; use intermediate evolutionary factors and qualify the association as frequent rather than necessary.

## DOI-first bibliography

1. Boyd BM et al. **Stochasticity, determinism, and contingency shape genome evolution of endosymbiotic bacteria.** *Nature Communications* 15:4571. Accepted 10 May 2024. DOI: [10.1038/s41467-024-48784-2](https://doi.org/10.1038/s41467-024-48784-2) (boyd2024stochasticitydeterminismand pages 1-2).
2. Porter SS et al. **Host-imposed control mechanisms in legume-rhizobia symbiosis.** *Nature Microbiology* 9:1929–1939. August 2024. DOI: [10.1038/s41564-024-01762-2](https://doi.org/10.1038/s41564-024-01762-2) (porter2024hostimposedcontrolmechanisms pages 1-3).
3. Ling X et al. **A complete DNA repair system assembled by two endosymbionts restores heat tolerance of the insect host.** *PNAS* 121. December 2024. DOI: [10.1073/pnas.2415651121](https://doi.org/10.1073/pnas.2415651121) (ling2024acompletedna pages 9-10).
4. Wang H et al. **Deciphering deep-sea chemosynthetic symbiosis by single-nucleus RNA-sequencing.** *eLife* 12:RP88294. Version of record 5 August 2024. DOI: [10.7554/eLife.88294](https://doi.org/10.7554/eLife.88294) (wang2024decipheringdeepseachemosynthetic pages 1-2).
5. Wierz JC et al. **Intracellular symbiont Symbiodolus is vertically transmitted and widespread across insect orders.** *ISME Journal* 18. 2024. DOI: [10.1093/ismejo/wrae099](https://doi.org/10.1093/ismejo/wrae099) (wierz2024intracellularsymbiontsymbiodolus pages 1-2).
6. Silva FJ et al. **Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of Blattella germanica…** *International Journal of Molecular Sciences* 25:4228. Published 11 April 2024. DOI: [10.3390/ijms25084228](https://doi.org/10.3390/ijms25084228) (silva2024comparativetranscriptomicsof pages 1-2).
7. Cai J, Longo A, Dickstein R. **Expression and mutagenesis studies in the Medicago truncatula iron transporter MtVTL8 confirm its role in symbiotic nitrogen fixation…** *Frontiers in Plant Science* 14:1306491. Published 4 January 2024. DOI: [10.3389/fpls.2023.1306491](https://doi.org/10.3389/fpls.2023.1306491) (cai2024expressionandmutagenesis pages 1-2).
8. Ferrarini MG et al. **Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil Sitophilus spp.** *Microbiome* 11:274. December 2023. DOI: [10.1186/s40168-023-01714-8](https://doi.org/10.1186/s40168-023-01714-8) (ferrarini2023coordinationofhost pages 1-3).
9. Duncan RP et al. **Co-option of a conserved host glutamine transporter facilitates aphid/Buchnera metabolic integration.** *PNAS* 120:e2308448120. October 2023. DOI: [10.1073/pnas.2308448120](https://doi.org/10.1073/pnas.2308448120) (duncan2023cooptionofa pages 8-9).
10. McCutcheon JP, Moran NA. **Extreme genome reduction in symbiotic bacteria.** *Nature Reviews Microbiology* 10:13–26. Published November 2011/issue 2012. DOI: [10.1038/nrmicro2670](https://doi.org/10.1038/nrmicro2670). Seminal background source supplied in the trait record.
11. Poole P, Ramachandran V, Terpolilli J. **Rhizobia: from saprophytes to endosymbionts.** *Nature Reviews Microbiology* 16:291–303. Published 2018. DOI: [10.1038/nrmicro.2017.171](https://doi.org/10.1038/nrmicro.2017.171). Seminal rhizobial scope source supplied in the trait record.

## Curation priority

The safest initial expansion of the existing 10-node/7-edge graph is to add experimentally supported, explicitly taxon-qualified branches for **ApGLNT1-mediated glutamine transport**, **MtVTL8-mediated iron delivery**, **organic-acid-supported nitrogen fixation**, **weevil autophagy/apoptosis-mediated clearance**, and **inter-symbiont DNA-repair complementation**. Genome reduction, secretion systems, immune effectors, and marine “milking” mechanisms should be represented as qualified secondary or provisional modules rather than universal determinants of `traitmech:000045`.

References

1. (wierz2024intracellularsymbiontsymbiodolus pages 1-2): Jürgen C Wierz, Philipp Dirksen, Roy Kirsch, Ronja Krüsemer, Benjamin Weiss, Yannick Pauchet, Tobias Engl, and Martin Kaltenpoth. Intracellular symbiont symbiodolus is vertically transmitted and widespread across insect orders. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae099, doi:10.1093/ismejo/wrae099. This article has 20 citations.

2. (boyd2024stochasticitydeterminismand pages 1-2): Bret M. Boyd, Ian James, Kevin P. Johnson, Robert B. Weiss, Sarah E. Bush, Dale H. Clayton, and Colin Dale. Stochasticity, determinism, and contingency shape genome evolution of endosymbiotic bacteria. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48784-2, doi:10.1038/s41467-024-48784-2. This article has 19 citations and is from a highest quality peer-reviewed journal.

3. (duncan2023cooptionofa pages 8-9): Rebecca P. Duncan, Catriona M. H. Anderson, David T. Thwaites, Charles W. Luetje, and Alex C. C. Wilson. Co-option of a conserved host glutamine transporter facilitates aphid/buchnera metabolic integration. Proceedings of the National Academy of Sciences of the United States of America, Oct 2023. URL: https://doi.org/10.1073/pnas.2308448120, doi:10.1073/pnas.2308448120. This article has 13 citations and is from a highest quality peer-reviewed journal.

4. (cai2024expressionandmutagenesis pages 13-15): Jingya Cai, Antonella Longo, and Rebecca Dickstein. Expression and mutagenesis studies in the medicago truncatula iron transporter mtvtl8 confirm its role in symbiotic nitrogen fixation and reveal amino acids essential for transport. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1306491, doi:10.3389/fpls.2023.1306491. This article has 5 citations.

5. (cai2024expressionandmutagenesis pages 8-10): Jingya Cai, Antonella Longo, and Rebecca Dickstein. Expression and mutagenesis studies in the medicago truncatula iron transporter mtvtl8 confirm its role in symbiotic nitrogen fixation and reveal amino acids essential for transport. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1306491, doi:10.3389/fpls.2023.1306491. This article has 5 citations.

6. (cai2024expressionandmutagenesis pages 1-2): Jingya Cai, Antonella Longo, and Rebecca Dickstein. Expression and mutagenesis studies in the medicago truncatula iron transporter mtvtl8 confirm its role in symbiotic nitrogen fixation and reveal amino acids essential for transport. Frontiers in Plant Science, Jan 2024. URL: https://doi.org/10.3389/fpls.2023.1306491, doi:10.3389/fpls.2023.1306491. This article has 5 citations.

7. (porter2024hostimposedcontrolmechanisms pages 1-3): Stephanie S. Porter, Simon E. Dupin, R. Ford Denison, E. Toby Kiers, and Joel L. Sachs. Host-imposed control mechanisms in legume-rhizobia symbiosis. Nature microbiology, 9:1929-1939, Aug 2024. URL: https://doi.org/10.1038/s41564-024-01762-2, doi:10.1038/s41564-024-01762-2. This article has 64 citations and is from a highest quality peer-reviewed journal.

8. (porter2024hostimposedcontrolmechanisms pages 3-4): Stephanie S. Porter, Simon E. Dupin, R. Ford Denison, E. Toby Kiers, and Joel L. Sachs. Host-imposed control mechanisms in legume-rhizobia symbiosis. Nature microbiology, 9:1929-1939, Aug 2024. URL: https://doi.org/10.1038/s41564-024-01762-2, doi:10.1038/s41564-024-01762-2. This article has 64 citations and is from a highest quality peer-reviewed journal.

9. (porter2024hostimposedcontrolmechanisms pages 7-8): Stephanie S. Porter, Simon E. Dupin, R. Ford Denison, E. Toby Kiers, and Joel L. Sachs. Host-imposed control mechanisms in legume-rhizobia symbiosis. Nature microbiology, 9:1929-1939, Aug 2024. URL: https://doi.org/10.1038/s41564-024-01762-2, doi:10.1038/s41564-024-01762-2. This article has 64 citations and is from a highest quality peer-reviewed journal.

10. (ferrarini2023coordinationofhost pages 13-14): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 19 citations and is from a highest quality peer-reviewed journal.

11. (ferrarini2023coordinationofhost pages 8-10): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 19 citations and is from a highest quality peer-reviewed journal.

12. (ling2024acompletedna pages 9-10): Xiaoyu Ling, Huijuan Guo, Jian Di, Liqiang Xie, Keyan Zhu-Salzman, Feng Ge, Zihua Zhao, and Yucheng Sun. A complete dna repair system assembled by two endosymbionts restores heat tolerance of the insect host. Proceedings of the National Academy of Sciences of the United States of America, Dec 2024. URL: https://doi.org/10.1073/pnas.2415651121, doi:10.1073/pnas.2415651121. This article has 14 citations and is from a highest quality peer-reviewed journal.

13. (wang2024decipheringdeepseachemosynthetic pages 1-2): Hao Wang, Kai He, Huan Zhang, Quanyong Zhang, Lei Cao, Jing Li, Zhaoshan Zhong, Hao Chen, Li Zhou, Chao Lian, Minxiao Wang, Kai Chen, Pei-Yuan Qian, and Chaolun Li. Deciphering deep-sea chemosynthetic symbiosis by single-nucleus rna-sequencing. eLife, Aug 2024. URL: https://doi.org/10.7554/elife.88294, doi:10.7554/elife.88294. This article has 18 citations and is from a domain leading peer-reviewed journal.

14. (wang2024decipheringdeepseachemosynthetic pages 10-12): Hao Wang, Kai He, Huan Zhang, Quanyong Zhang, Lei Cao, Jing Li, Zhaoshan Zhong, Hao Chen, Li Zhou, Chao Lian, Minxiao Wang, Kai Chen, Pei-Yuan Qian, and Chaolun Li. Deciphering deep-sea chemosynthetic symbiosis by single-nucleus rna-sequencing. eLife, Aug 2024. URL: https://doi.org/10.7554/elife.88294, doi:10.7554/elife.88294. This article has 18 citations and is from a domain leading peer-reviewed journal.

15. (silva2024comparativetranscriptomicsof pages 1-2): Francisco J. Silva, Rebeca Domínguez-Santos, Amparo Latorre, and Carlos García-Ferris. Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of blattella germanica with emphasis on the metabolic integration with its endosymbiont blattabacterium and its immune system. International Journal of Molecular Sciences, 25:4228, Apr 2024. URL: https://doi.org/10.3390/ijms25084228, doi:10.3390/ijms25084228. This article has 7 citations.

16. (silva2024comparativetranscriptomicsof pages 21-22): Francisco J. Silva, Rebeca Domínguez-Santos, Amparo Latorre, and Carlos García-Ferris. Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of blattella germanica with emphasis on the metabolic integration with its endosymbiont blattabacterium and its immune system. International Journal of Molecular Sciences, 25:4228, Apr 2024. URL: https://doi.org/10.3390/ijms25084228, doi:10.3390/ijms25084228. This article has 7 citations.

17. (boyd2024stochasticitydeterminismand pages 9-10): Bret M. Boyd, Ian James, Kevin P. Johnson, Robert B. Weiss, Sarah E. Bush, Dale H. Clayton, and Colin Dale. Stochasticity, determinism, and contingency shape genome evolution of endosymbiotic bacteria. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48784-2, doi:10.1038/s41467-024-48784-2. This article has 19 citations and is from a highest quality peer-reviewed journal.

18. (silva2024comparativetranscriptomicsof pages 14-15): Francisco J. Silva, Rebeca Domínguez-Santos, Amparo Latorre, and Carlos García-Ferris. Comparative transcriptomics of fat bodies between symbiotic and quasi-aposymbiotic adult females of blattella germanica with emphasis on the metabolic integration with its endosymbiont blattabacterium and its immune system. International Journal of Molecular Sciences, 25:4228, Apr 2024. URL: https://doi.org/10.3390/ijms25084228, doi:10.3390/ijms25084228. This article has 7 citations.

19. (porter2024hostimposedcontrolmechanisms pages 5-6): Stephanie S. Porter, Simon E. Dupin, R. Ford Denison, E. Toby Kiers, and Joel L. Sachs. Host-imposed control mechanisms in legume-rhizobia symbiosis. Nature microbiology, 9:1929-1939, Aug 2024. URL: https://doi.org/10.1038/s41564-024-01762-2, doi:10.1038/s41564-024-01762-2. This article has 64 citations and is from a highest quality peer-reviewed journal.

20. (ferrarini2023coordinationofhost pages 1-3): Mariana Galvão Ferrarini, Agnès Vallier, Carole Vincent-Monégat, Elisa Dell’Aglio, Benjamin Gillet, Sandrine Hughes, Ophélie Hurtado, Guy Condemine, Anna Zaidman-Rémy, Rita Rebollo, Nicolas Parisot, and Abdelaziz Heddi. Coordination of host and endosymbiont gene expression governs endosymbiont growth and elimination in the cereal weevil sitophilus spp. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01714-8, doi:10.1186/s40168-023-01714-8. This article has 19 citations and is from a highest quality peer-reviewed journal.