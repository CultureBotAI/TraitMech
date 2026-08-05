---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:59:58.748207'
end_time: '2026-08-04T11:10:35.854481'
duration_seconds: 637.11
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemotaxis
  trait_identifier: traitmech:000086
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemotaxis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A behavioral physiology in which cells bias their movement toward attractants
    or away from repellents by modulating flagellar motor switching in response to
    chemical gradients.
  parent_traits: METPO:1000059
  synonyms: chemotactic
  evidence_summary: 'DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis
    as gradient-guided movement controlled by a histidine-aspartate phosphorelay.)
    | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing
    in complex chemotaxis pathways.)'
  causal_graph_summary: 'chemotaxis_gradient_response: 12 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemotaxis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000086
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A behavioral physiology in which cells bias their movement toward attractants or away from repellents by modulating flagellar motor switching in response to chemical gradients.
- **Parent traits:** METPO:1000059
- **Synonyms:** chemotactic
- **Existing evidence:** DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis as gradient-guided movement controlled by a histidine-aspartate phosphorelay.) | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing in complex chemotaxis pathways.)
- **Existing causal graph summary:** chemotaxis_gradient_response: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **chemotaxis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotaxis.yaml`.

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
- **Trait label:** chemotaxis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000086
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A behavioral physiology in which cells bias their movement toward attractants or away from repellents by modulating flagellar motor switching in response to chemical gradients.
- **Parent traits:** METPO:1000059
- **Synonyms:** chemotactic
- **Existing evidence:** DOI:10.1038/nrm1524:  (Wadhams & Armitage review bacterial chemotaxis as gradient-guided movement controlled by a histidine-aspartate phosphorelay.) | DOI:10.1038/nrmicro2505:  (Porter, Wadhams & Armitage review signal processing in complex chemotaxis pathways.)
- **Existing causal graph summary:** chemotaxis_gradient_response: 12 nodes, 10 edges

## Research Objective

Research the microbial trait **chemotaxis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemotaxis.yaml`.

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


# Curation-focused research report: microbial chemotaxis

## Trait record and scope

- **Trait label:** chemotaxis
- **Trait identifier:** **traitmech:000086**
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000059
- **Recommended scope:** a microbial behavioral physiology in which a cell senses a spatial chemical gradient and biases locomotion toward an attractant or away from a repellent. In the canonical flagellar system, temporal comparisons of chemoeffector concentration alter CheA–CheY phosphosignaling and thereby the probability of flagellar motor switching. The phenotype is therefore **directed bias**, not movement per se. Recent reviews emphasize that *Escherichia coli* supplies the best-resolved paradigm but is among the simplest systems and should not be treated as universal. Chemotaxis-like networks can also control type-IV-pilus motility and non-motility outputs. (muok2024unpackingalternativefeatures pages 4-6, muok2024unpackingalternativefeatures pages 1-2, vass2023analysisofchew‐like pages 1-3, xu2023systematicmappingof pages 1-2)

### Boundary cases

1. **Motility versus chemotaxis.** Swimming, twitching, or gliding in a uniform environment demonstrates locomotor capacity, not chemotaxis. A gradient-dependent directional bias or validated pathway response is required.
2. **Chemokinesis.** A chemical-induced change in speed or turning frequency without directional bias is not sufficient.
3. **Aerotaxis, energy taxis, thermotaxis, pH taxis, and magnetotaxis.** These can use homologous chemosensory machinery, but should be separate traits unless the graph is explicitly intended to cover all taxis controlled by chemotaxis-family systems. The 2024 Annual Review notes this expanded stimulus repertoire while focusing its canonical discussion on flagellar chemotaxis. (muok2024unpackingalternativefeatures pages 1-2)
4. **Surface/mechanosensing.** In *Pseudomonas aeruginosa*, WspA- and PilJ-associated pathways mediate surface or mechanical sensing rather than genuine chemical-gradient sensing; they should not automatically be included under this trait. (xu2023systematicmappingof pages 2-4)
5. **Growth toward a nutrient.** Metabolic utilization and chemotactic attraction must be separated experimentally. The 2024 root-exudate study measured attraction and feeding independently, illustrating this distinction. (fourneau2024a“lovematch” pages 1-2)
6. **Colonization, biofilm formation, collective behavior, and virulence.** These are downstream ecological outcomes to which chemotaxis may contribute, not definitions of chemotaxis itself.

## Current mechanistic understanding

The canonical core is a modified two-component system. Chemoreceptor arrays detect chemoeffectors and, through CheW, control the histidine kinase CheA. CheA autophosphorylates and transfers phosphate to CheY. CheY-P binds the flagellar switch protein FliM; in the *E. coli* paradigm this promotes clockwise rotation and tumbling, whereas low CheY-P favors counterclockwise rotation and smooth swimming. CheZ terminates output by dephosphorylating CheY-P. CheR-mediated methylation and CheB-mediated demethylation provide delayed negative feedback and sensory adaptation, retaining responsiveness across changing background concentrations. (uchida2022thechemoreceptorsensory pages 1-3, muok2024unpackingalternativefeatures pages 4-6, muok2024unpackingalternativefeatures pages 2-4, xu2023systematicmappingof pages 1-2)

The physical signaling unit is an array containing chemoreceptors, CheA, and CheW. A 2023 native-state cryo-electron-tomography study resolved the complete *E. coli* core signaling unit at **12 Å** and described six receptor dimers arranged as two trimers of dimers, one CheA dimer, and two essential CheW adaptors. CheA P4 binds ATP and phosphorylates the P1 histidine; P5 and CheW connect the kinase to receptor tips. (cassidy2023structureofthe pages 1-2)

## Candidate nodes grouped by type

Ontology assignments below are deliberately conservative. Identifiers are suggested only where they are stable and well established; strain-specific proteins and poorly standardized complexes can remain label-only nodes pending ontology validation.

### Trait and biological-process nodes

| Candidate node | Suggested grounding | Curation comment |
|---|---|---|
| chemotaxis | **traitmech:000086**; candidate GO:0006935 | Use the supplied TraitMech CURIE verbatim; validate GO import policy locally. |
| flagellum-dependent cell motility | candidate GO:0071973 | Parent/required locomotor capacity, not equivalent to chemotaxis. |
| bacterial-type flagellum-dependent cell motility | candidate GO:0071973 | Use only if the graph is restricted to flagellar systems. |
| signal transduction by protein phosphorylation | label or validated GO term | Generic process supporting CheA→CheY phosphate flow. |
| chemotactic sensory adaptation | label-only candidate | CheR/CheB feedback restoring kinase output under persistent stimulation. |
| clockwise flagellar rotation; counterclockwise flagellar rotation; tumbling; smooth swimming | label-only candidates | Direction-to-behavior relation is strongly established for peritrichous *E. coli* but not universal across flagellar architectures. |

### Genes, proteins, functions, and complexes

| Node | Type / function | Grounding recommendation |
|---|---|---|
| methyl-accepting chemotaxis protein / chemoreceptor | receptor family | GO:0004884 is a candidate molecular-function grounding; retain protein-family label where appropriate. |
| Tar, Tsr, Trg, Tap, Aer | *E. coli* receptors | Use organism-specific UniProt accessions only after strain selection. |
| CheA | histidine autokinase | Protein-family label; candidate EC 2.7.13.3 for protein histidine kinase activity, subject to local validation. |
| CheW | receptor–CheA coupling/scaffold protein | Protein-family label. |
| CheY / CheY-P | response regulator / phosphorylated state | Separate stateful nodes if the YAML model supports modified forms. |
| CheZ | CheY-P phosphatase | Protein-family label; do not assume universal presence. |
| CheR | receptor methyltransferase | Protein-family label; enzymatic substrate is receptor glutamyl residues. |
| CheB / CheB-P | methylesterase response regulator | Separate phosphorylation state if needed. |
| FliM | flagellar motor-switch component | Protein-family label; UniProt should be strain-specific. |
| chemosensory array | supramolecular complex | Label-only candidate. |
| core signaling unit | complex | Composition in *E. coli*: six receptor dimers, one CheA dimer, and two essential CheW proteins. (cassidy2023structureofthe pages 1-2) |
| flagellar motor switch complex | complex | Label-only or validated GO cellular-component term after ontology lookup. |
| PctA, PctB, PctC, PctP, TlpQ | *P. aeruginosa* chemoreceptors | Use PAO1 locus-specific UniProt accessions only after direct database validation. |

### Chemicals and molecular states

| Node | Suggested grounding / status | Role |
|---|---|---|
| ATP | CHEBI:15422 | CheA P4 substrate for autophosphorylation. |
| ADP | CHEBI:16761 | Product of kinase reaction; optional node. |
| phosphate / phosphoryl group | CHEBI grounding should be selected according to represented chemical form | Transferred CheA→CheY. |
| L-serine | CHEBI:17115 | Canonical attractant in *E. coli*. |
| L-aspartate | CHEBI:17053 | Canonical attractant in *E. coli*. |
| attractant; repellent; extracellular chemoeffector | label-level classes | Use as generic environmental-input nodes. |
| receptor methylated glutamate; receptor unmethylated glutamate | stateful label nodes | Adaptation states controlled by CheR and CheB. |
| methyl 4-aminobutyrate, 5-aminovalerate, L-ornithine, 2-phenylethylamine, tyramine | CHEBI lookup required | Recently mapped *P. aeruginosa* attractants; do not guess CURIEs. |
| guanine, inosine, adenosine, hypoxanthine, adenine, guanosine | individually groundable in CHEBI; validate exact forms | PctP-associated purine chemoeffectors. |
| root exudates | mixture; label-only or ENVO-contextualized | Environmental chemoeffector mixture, not a single chemical node. |

### Cellular locations and environmental/experimental factors

- **Periplasmic ligand-binding domain**, transmembrane helices, HAMP domain, receptor protein-interaction region, cytoplasm, cell pole, cytoplasmic membrane, and flagellar basal body/motor.
- **Chemical concentration gradient**, gradient steepness, background ligand concentration, nutrient gradient, pH, temperature, oxygen/redox state, flow velocity, viscosity, and surface confinement.
- **Assays:** capillary chemotaxis assay, soft-agar migration assay, single-cell tracking, microfluidic gradient assay, receptor-output FRET, thermal-shift assay, isothermal titration calorimetry, genetic deletion/complementation, and motor-rotation measurement. Microfluidics is particularly useful because it imposes controlled gradients, pH, flow, and confinement at microbial length scales. (xu2023systematicmappingof pages 2-4, ugolini2024microfluidicapproachesin pages 1-2)

## Candidate evidence-backed causal edges

The following curation table gives canonical and taxon-specific triples, supporting text, evidence status, and cautions.

| subject | predicate | object | taxon/scope | strength/status | DOI source | short supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| extracellular chemoeffector | binds/sensed by | chemoreceptor ligand-binding domain (LBD) | canonical transmembrane bacterial chemotaxis; E. coli model | strong, canonical | 10.1146/annurev-micro-032421-110850 | “The canonical chemotaxis signaling cascade… is initiated by the sensing of an extracellular chemoeffector by the LBD. Upon ligand binding, the signal is transmitted…” (muok2024unpackingalternativefeatures pages 4-6, muok2024unpackingalternativefeatures pages 2-4) | Trait-defining input step; curate at generic receptor level unless receptor-specific ligand evidence is available. |
| chemoreceptor protein interaction region (PIR) + CheW | regulates/couples to | CheA kinase activity | canonical; E. coli model | strong, canonical | 10.1146/annurev-micro-032421-110850 | “CheA activity is regulated by subsequent receptor packing alterations at the PIR” and “The coupling protein CheW secures the connection between CheA P5 and the receptor tip.” (muok2024unpackingalternativefeatures pages 4-6) | Supports a receptor/CheW→CheA regulatory edge; mechanism is conformational coupling within arrays. |
| chemosensory array / receptors | cooperatively regulate | CheA autophosphorylation activity | E. coli structural CSU | strong, canonical | 10.1128/mbio.00793-23 | “chemosensory arrays… cooperatively integrate the sensory inputs of multiple receptors to regulate the autophosphorylation activity of CheA.” (cassidy2023structureofthe pages 1-2) | Good evidence for array-level regulation node in addition to single receptor nodes. |
| CheA P4 domain + ATP | catalyzes autophosphorylation of | CheA P1 histidine residue | E. coli; canonical kinase architecture | strong, canonical | 10.1128/mbio.00793-23 | “The P4 domain binds ATP and catalyzes autophosphorylation at a histidine residue in the P1 domain.” (cassidy2023structureofthe pages 1-2) | Use if graph includes domain-resolved mechanism; otherwise simplify to CheA autophosphorylates. |
| CheA-P | transfers phosphoryl group to | CheY | canonical bacteria; E. coli and P. aeruginosa descriptions | strong, canonical | 10.1146/annurev-micro-032421-110850; 10.1128/mbio.02099-23 | “Phosphorylated CheA can transfer its phosphoryl group to the response regulator protein CheY” and “subsequently altering the transphosphorylation of CheY.” (muok2024unpackingalternativefeatures pages 4-6, xu2023systematicmappingof pages 1-2) | Core excitation branch; broadly curatable. |
| CheY-P | binds | FliM | canonical flagellar chemotaxis | strong, canonical | 10.1146/annurev-micro-032421-110850 | “CheY-P binds FliM, which is a component of the flagellar motor switch complex.” (muok2024unpackingalternativefeatures pages 4-6) | Prefer explicit FliM node if motor-switch subunits are represented. |
| FliM bound by CheY-P | induces | clockwise flagellar rotation / tumbling | canonical flagellar chemotaxis | strong, canonical | 10.1146/annurev-micro-032421-110850 | “When bound to CheY, FliM induces clockwise flagellar rotation, resulting in tumbling.” (muok2024unpackingalternativefeatures pages 4-6) | Directly matches trait definition’s motor switching component. |
| chemoattractant sensing | inhibits | CheA kinase activity | E. coli canonical model | strong, canonical | 10.1146/annurev-micro-032421-110850; 10.1099/mic.0.001432 | “Sensing of a chemoattractant turns off CheA kinase activity” and attractant binding “propagates a signal… to inhibit CheA phosphorylation.” (muok2024unpackingalternativefeatures pages 4-6, armitage2024twistsandturns pages 6-8) | Directionality may differ for some alternative systems; canonical edge is safe with note. |
| decreased CheA activity | reduces | phosphorylated CheY concentration | E. coli canonical model | strong, canonical | 10.1146/annurev-micro-032421-110850 | “thereby reducing the concentration of phosphorylated CheY” (muok2024unpackingalternativefeatures pages 4-6) | Can be modeled as CheA activity positively regulates CheY-P abundance. |
| lower CheY-P | switches flagella to | counterclockwise rotation / smooth swimming | E. coli canonical model | strong, canonical | 10.1146/annurev-micro-032421-110850 | “switches the flagella to a counterclockwise rotation, resulting in smooth swimming.” (muok2024unpackingalternativefeatures pages 4-6) | Completes attractant-response branch in causal graph. |
| CheZ | dephosphorylates | CheY | canonical bacteria; E. coli and P. aeruginosa descriptions | strong, canonical | 10.1146/annurev-micro-032421-110850; 10.1128/mbio.02099-23 | “The phosphatase CheZ dephosphorylates some CheY” and “CheZ is responsible for the dephosphorylation of CheY.” (muok2024unpackingalternativefeatures pages 4-6, xu2023systematicmappingof pages 1-2) | Curate as signal termination / CheY-P turnover. |
| CheR | methylates | chemoreceptors | canonical adaptation system | strong, canonical | 10.1146/annurev-micro-032421-110850; 10.1128/mbio.02099-23 | “Receptors undergo methylation… by the methyltransferase CheR” and “CheR and CheB adjusts the level of receptor methylation…” (muok2024unpackingalternativefeatures pages 4-6, xu2023systematicmappingof pages 1-2) | Generic receptor methylation edge is well supported. |
| CheB | demethylates / methylesterase acts on | chemoreceptors | canonical adaptation system | strong, canonical | 10.1146/annurev-micro-032421-110850; 10.1128/mbio.02099-23 | “demethylation by… CheB” and “CheB adjusts the level of receptor methylation on several specific glutamyl residues.” (muok2024unpackingalternativefeatures pages 4-6, xu2023systematicmappingof pages 1-2) | Curate as receptor demethylation; phosphorylation dependence of CheB can be added only if needed. |
| receptor methylation feedback (CheR/CheB adaptation system) | maintains responsiveness / enables | adaptation to persistent stimulation | canonical adaptation system | strong, canonical | 10.1146/annurev-micro-032421-110850; 10.1128/mbio.02099-23 | “This dynamic modification system allows the cell to maintain responsiveness… under saturating conditions” and “providing negative feedback… ensures the adaptation of cells to persisting stimulation.” (muok2024unpackingalternativefeatures pages 4-6, xu2023systematicmappingof pages 1-2) | Good process-level edge for “sensory adaptation” subgraph. |
| methyl 4-aminobutyrate | chemoattractant for receptor | PctC | Pseudomonas aeruginosa PAO1 | taxon-specific, strong within study | 10.1128/mbio.02099-23 | Table lists for PctC: “Newly characterized chemoeffectors… methyl 4-aminobutyrate” (xu2023systematicmappingof pages 2-4) | Curate only with explicit taxon/receptor scope; not a general chemotaxis edge. |
| 5-aminovalerate | chemoattractant for receptor | PctC | Pseudomonas aeruginosa PAO1 | taxon-specific, strong within study | 10.1128/mbio.02099-23 | Table lists for PctC: “5-Aminovalerate” (xu2023systematicmappingof pages 2-4) | Same caution as above. |
| 2-phenylethylamine | chemoattractant for receptor | TlpQ | Pseudomonas aeruginosa PAO1 | taxon-specific, strong within study | 10.1128/mbio.02099-23 | Table lists for TlpQ: “2-Phenylethylamine, tyramine” (xu2023systematicmappingof pages 2-4) | Taxon-specific receptor mapping. |
| tyramine | chemoattractant for receptor | TlpQ | Pseudomonas aeruginosa PAO1 | taxon-specific, strong within study | 10.1128/mbio.02099-23 | Table lists for TlpQ: “2-Phenylethylamine, tyramine” (xu2023systematicmappingof pages 2-4) | Taxon-specific receptor mapping. |
| purines (guanine/inosine/adenosine/hypoxanthine/adenine/guanosine) | bind / act as chemoeffectors for | PctP | Pseudomonas aeruginosa PAO1 | taxon-specific, strong within study | 10.1128/mbio.02099-23 | “annotate a novel purine-specific receptor PctP” and table lists “Guanine, inosine, adenosine, hypoxanthine, adenine, and guanosine” (xu2023systematicmappingof pages 1-2, xu2023systematicmappingof pages 2-4) | Consider collapsing to “purines → PctP” node if graph granularity is limited. |
| root exudates | attract | Bacillus subtilis / Pseudomonas fluorescens / Azospirillum brasilense | rhizosphere application | uncertain, assay-/community-specific | 10.3389/fmicb.2024.1473099 | “root exudates… to attract and feed three PGPR” and “rapeseed exudates were the most attractive” (fourneau2024a“lovematch” pages 1-2) | Useful ecological/application note, but too assay- and taxon-specific for core canonical graph unless environmental chemoeffector node is desired. |


*Table: This table summarizes candidate causal edges for microbial chemotaxis curation, combining canonical signal-transduction steps with taxon-specific receptor-ligand mappings and ecological attraction evidence. It is designed to support TraitMech edge selection while flagging which claims are broad, canonical, or context-limited.*

### Recommended minimal canonical subgraph

For a compact extension of the existing 12-node/10-edge graph, the highest-confidence chain is:

1. extracellular chemoeffector **binds/sensed_by** chemoreceptor LBD;
2. ligand-bound receptor state **regulates** CheA through CheW;
3. CheA **autophosphorylates** CheA-P using ATP;
4. CheA-P **phosphorylates** CheY;
5. CheY-P **binds** FliM;
6. FliM-bound CheY-P **increases** clockwise rotation/tumbling in *E. coli*;
7. lower CheY-P **favors** counterclockwise rotation/smooth swimming in *E. coli*;
8. CheZ **dephosphorylates** CheY-P;
9. CheR **methylates** chemoreceptors;
10. CheB **demethylates** chemoreceptors;
11. receptor methylation state **provides negative feedback to** CheA;
12. temporal modulation of motor switching **causes** biased movement along a chemical gradient.

Edges 6–7 should carry an *E. coli*/peritrichous-flagellar scope rather than being asserted as universal. The upstream phosphorelay is more broadly conserved, but CheZ and the exact adaptation architecture are not universal. (muok2024unpackingalternativefeatures pages 4-6, vass2023analysisofchew‐like pages 1-3, xu2023systematicmappingof pages 1-2)

## Recent developments and quantitative evidence, 2023–2024

### Structural mechanism

Cassidy et al. reconstructed a native *E. coli* core signaling unit at **12-Å resolution** using cryo-electron tomography and subtomogram averaging, supplemented with AlphaFold2 and molecular dynamics. This provided a complete structural framework for receptor–CheW–CheA coupling and identified previously unresolved CheA-domain arrangements. Published **29 September 2023**; DOI: [10.1128/mbio.00793-23](https://doi.org/10.1128/mbio.00793-23). (cassidy2023structureofthe pages 1-2)

### System diversity and expert interpretation

A 2024 Annual Review argues that the canonical *E. coli* scheme is a powerful but non-universal paradigm: bacteria differ in array architecture, sensory mechanism, receptor localization, and chemotaxis-protein composition. The review reports an average of approximately **14 chemoreceptor genes per bacterial genome**, with organisms occupying variable habitats having roughly **fivefold more** receptors than organisms in stable habitats. Published online **10 July 2024**; DOI: [10.1146/annurev-micro-032421-110850](https://doi.org/10.1146/annurev-micro-032421-110850). (muok2024unpackingalternativefeatures pages 4-6, muok2024unpackingalternativefeatures pages 1-2)

Vass et al. surveyed approximately **1,900 prokaryotic species** and described **19 known chemotaxis-system categories**. Sixteen CheA/CheW/CheV architectures contained about **94%** of CheW-like domains and were grouped into six likely functional classes. These results support representing “chemotaxis system” as a family of related architectures rather than one invariant module. Published in final form **March 2023**; DOI: [10.1002/prot.26430](https://doi.org/10.1002/prot.26430). Co-occurrence-based assignments remain hypotheses: phyletic coupling need not imply direct physical interaction, and binary presence/absence analysis loses paralog information. (vass2023analysisofchew‐like pages 1-3, vass2023analysisofchew‐like pages 13-14)

### Receptor deorphanization

Xu et al. showed that *P. aeruginosa* PAO1 has **26 chemoreceptors**, **12 LBD types**, and **four chemosensory pathways**. Twenty-three receptors were predicted to feed the swimming-controlling F6 pathway. The team tested **16 hybrid receptors** using capillary assays, FRET, microfluidics, thermal shifts, and calorimetry. Newly assigned attractants included methyl 4-aminobutyrate, 5-aminovalerate, L-ornithine, 2-phenylethylamine, and tyramine; PctP was annotated as purine-specific. At least four receptors contributed to bidirectional pH responses. Published **4 October 2023**; DOI: [10.1128/mbio.02099-23](https://doi.org/10.1128/mbio.02099-23). The authors stress that signal specificity remains unknown for the absolute majority of bacterial chemoreceptors. (xu2023systematicmappingof pages 1-2, xu2023systematicmappingof pages 2-4)

## Applications and real-world relevance

- **Rhizosphere recruitment and bioinoculants.** A September 2024 experiment compared root exudates from rapeseed, pea, and ryegrass against *Bacillus subtilis*, *Pseudomonas fluorescens*, and *Azospirillum brasilense*. Rapeseed exudates were most attractive and supported the fastest growth, whereas pea exudates supported the greatest biomass. The proposed “love match” score could help select plant–PGPR combinations, but it combines distinct attraction and feeding measurements and is not yet a general mechanistic predictor. DOI: [10.3389/fmicb.2024.1473099](https://doi.org/10.3389/fmicb.2024.1473099), published **23 September 2024**. (fourneau2024a“lovematch” pages 1-2)
- **Pathogenesis and colonization.** Authoritative reviews conclude that pathogens can navigate toward host metabolites, stress products, or root exudates, making chemotaxis a contributor to infection-site localization and plant colonization. Chemotaxis inhibition is therefore a proposed anti-virulence strategy, but the gathered evidence does not establish a clinically deployed chemotaxis inhibitor. (muok2024unpackingalternativefeatures pages 4-6)
- **Environmental microbiology.** Controlled microfluidic gradients now permit single-cell and community-level measurements under realistic nutrient, pH, flow, and confinement conditions. These platforms are research implementations rather than evidence that every measured accumulation is receptor-mediated chemotaxis. DOI: [10.1039/D3LC00784G](https://doi.org/10.1039/D3LC00784G), accepted **23 January 2024**. (ugolini2024microfluidicapproachesin pages 1-2)
- **Receptor discovery and biosensing.** Hybrid-receptor FRET and microfluidic workflows provide a practical route to deorphanize sensory domains and may support engineered biosensors, but chimeric signaling must be confirmed by direct ligand binding and native-strain chemotaxis. (xu2023systematicmappingof pages 2-4, xu2023systematicmappingof pages 1-2)

## Curation warnings

1. **Do not universalize *E. coli* motor logic.** “CheY-P→FliM→clockwise→tumble” is robust for the canonical peritrichous system but other taxa reverse, stop, or otherwise reconfigure flagella.
2. **Do not require CheZ universally.** Signal termination can use alternative phosphatases or intrinsic dephosphorylation.
3. **Do not infer chemotaxis from `che` genes alone.** Chemotaxis-family pathways can regulate type-IV pili, cyclic-di-GMP, development, surface sensing, or other outputs. (vass2023analysisofchew‐like pages 1-3, xu2023systematicmappingof pages 2-4)
4. **Do not infer a causal ligand–receptor edge from capillary accumulation alone.** Metabolism, growth, motility differences, and receptor redundancy can confound accumulation. Direct binding, receptor deletion/complementation, signaling readout, or convergent assays are preferable. Thermal-shift assays can yield false positives; ITC is accurate but lower throughput. (xu2023systematicmappingof pages 2-4)
5. **Treat hybrid-receptor results as supported but engineered-system evidence.** Native receptor-context validation remains desirable.
6. **Separate environmental mixtures from molecular ligands.** “Root exudates” should not be modeled as one chemical entity.
7. **Do not curate co-occurrence as physical interaction.** Comparative CheW-class associations are valuable hypotheses but phyletic coupling is not direct biochemical evidence. (vass2023analysisofchew‐like pages 13-14)
8. **Keep pH, temperature, oxygen, redox, and magnetic sensing outside the core graph unless TraitMech explicitly broadens the scope.** Homologous machinery does not make every taxis phenotype chemotaxis in the strict chemical-gradient sense.
9. **Avoid unverified ontology identifiers.** Add strain-specific UniProt accessions and exact CHEBI CURIEs only after database validation; label-only nodes are preferable to invented mappings.
10. **Colonization and virulence edges require taxon-specific experiments.** Reviews support broad relevance but not a universal direct edge from chemotaxis to pathogenicity.

## DOI-first bibliography

1. Muok AR, Olsthoorn FA, Briegel A. **Unpacking Alternative Features of the Bacterial Chemotaxis System.** *Annual Review of Microbiology* 78:169–189. First published online **10 July 2024**. DOI: [10.1146/annurev-micro-032421-110850](https://doi.org/10.1146/annurev-micro-032421-110850). (muok2024unpackingalternativefeatures pages 1-2)
2. Armitage JP. **Twists and turns: 40 years of investigating how and why bacteria swim.** *Microbiology* 170. **February 2024**. DOI: [10.1099/mic.0.001432](https://doi.org/10.1099/mic.0.001432). (armitage2024twistsandturns pages 6-8)
3. Xu W et al. **Systematic mapping of chemoreceptor specificities for Pseudomonas aeruginosa.** *mBio* 14(5). Published **4 October 2023**. DOI: [10.1128/mbio.02099-23](https://doi.org/10.1128/mbio.02099-23). (xu2023systematicmappingof pages 1-2)
4. Cassidy CK et al. **Structure of the native chemotaxis core signaling unit from phage E-protein lysed E. coli cells.** *mBio* 14(5). Published **29 September 2023**. DOI: [10.1128/mbio.00793-23](https://doi.org/10.1128/mbio.00793-23). (cassidy2023structureofthe pages 1-2)
5. Vass LR, Bourret RB, Foster CA. **Analysis of CheW-like domains provides insights into organization of prokaryotic chemotaxis systems.** *Proteins* 91:315–329. Final issue **March 2023**. DOI: [10.1002/prot.26430](https://doi.org/10.1002/prot.26430). (vass2023analysisofchew‐like pages 1-3)
6. Fourneau E et al. **A “love match” score to compare root exudate attraction and feeding of the plant growth-promoting rhizobacteria Bacillus subtilis, Pseudomonas fluorescens, and Azospirillum brasilense.** *Frontiers in Microbiology* 15. Published **23 September 2024**. DOI: [10.3389/fmicb.2024.1473099](https://doi.org/10.3389/fmicb.2024.1473099). (fourneau2024a“lovematch” pages 1-2)
7. Ugolini GS et al. **Microfluidic approaches in microbial ecology.** *Lab on a Chip* 24:1394–1418. Accepted **23 January 2024**. DOI: [10.1039/D3LC00784G](https://doi.org/10.1039/D3LC00784G). (ugolini2024microfluidicapproachesin pages 1-2)
8. Uchida Y et al. **The Chemoreceptor Sensory Adaptation System Produces Coordinated Reversals of the Flagellar Motors on an Escherichia coli Cell.** *Journal of Bacteriology* 204(12). **December 2022**. DOI: [10.1128/jb.00278-22](https://doi.org/10.1128/jb.00278-22). (uchida2022thechemoreceptorsensory pages 1-3)
9. Wadhams GH, Armitage JP. **Making sense of it all: bacterial chemotaxis.** *Nature Reviews Molecular Cell Biology* 5:1024–1037. **December 2004**. DOI: [10.1038/nrm1524](https://doi.org/10.1038/nrm1524). Foundational source supplied in the trait record.
10. Porter SL, Wadhams GH, Armitage JP. **Signal processing in complex chemotaxis pathways.** *Nature Reviews Microbiology*. DOI: [10.1038/nrmicro2505](https://doi.org/10.1038/nrmicro2505). Foundational source supplied in the trait record.

References

1. (muok2024unpackingalternativefeatures pages 4-6): A.R. Muok, F.A. Olsthoorn, and A. Briegel. Unpacking alternative features of the bacterial chemotaxis system. Nov 2024. URL: https://doi.org/10.1146/annurev-micro-032421-110850, doi:10.1146/annurev-micro-032421-110850. This article has 8 citations and is from a peer-reviewed journal.

2. (muok2024unpackingalternativefeatures pages 1-2): A.R. Muok, F.A. Olsthoorn, and A. Briegel. Unpacking alternative features of the bacterial chemotaxis system. Nov 2024. URL: https://doi.org/10.1146/annurev-micro-032421-110850, doi:10.1146/annurev-micro-032421-110850. This article has 8 citations and is from a peer-reviewed journal.

3. (vass2023analysisofchew‐like pages 1-3): Luke R. Vass, Robert B. Bourret, and Clay A. Foster. Analysis of <scp>chew</scp>‐like domains provides insights into organization of prokaryotic chemotaxis systems. Oct 2023. URL: https://doi.org/10.1002/prot.26430, doi:10.1002/prot.26430. This article has 11 citations.

4. (xu2023systematicmappingof pages 1-2): Wenhao Xu, Jean Paul Cerna-Vargas, Ana Tajuelo, Andrea Lozano-Montoya, Melissa Kivoloka, Nicolas Krink, Elizabet Monteagudo-Cascales, Miguel A. Matilla, Tino Krell, and Victor Sourjik. Systematic mapping of chemoreceptor specificities for <i>pseudomonas aeruginosa</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.02099-23, doi:10.1128/mbio.02099-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

5. (xu2023systematicmappingof pages 2-4): Wenhao Xu, Jean Paul Cerna-Vargas, Ana Tajuelo, Andrea Lozano-Montoya, Melissa Kivoloka, Nicolas Krink, Elizabet Monteagudo-Cascales, Miguel A. Matilla, Tino Krell, and Victor Sourjik. Systematic mapping of chemoreceptor specificities for <i>pseudomonas aeruginosa</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.02099-23, doi:10.1128/mbio.02099-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

6. (fourneau2024a“lovematch” pages 1-2): Eulalie Fourneau, Mélissa Pannier, Wassila Riah, Emmanuelle Personeni, Annette Morvan-Bertrand, Josselin Bodilis, and Barbara Pawlak. A “love match” score to compare root exudate attraction and feeding of the plant growth-promoting rhizobacteria bacillus subtilis, pseudomonas fluorescens, and azospirillum brasilense. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1473099, doi:10.3389/fmicb.2024.1473099. This article has 21 citations and is from a peer-reviewed journal.

7. (uchida2022thechemoreceptorsensory pages 1-3): Yumiko Uchida, Tatsuki Hamamoto, Yong-Suk Che, Hiroto Takahashi, John S. Parkinson, Akihiko Ishijima, and Hajime Fukuoka. The chemoreceptor sensory adaptation system produces coordinated reversals of the flagellar motors on an escherichia coli cell. Dec 2022. URL: https://doi.org/10.1128/jb.00278-22, doi:10.1128/jb.00278-22. This article has 10 citations and is from a peer-reviewed journal.

8. (muok2024unpackingalternativefeatures pages 2-4): A.R. Muok, F.A. Olsthoorn, and A. Briegel. Unpacking alternative features of the bacterial chemotaxis system. Nov 2024. URL: https://doi.org/10.1146/annurev-micro-032421-110850, doi:10.1146/annurev-micro-032421-110850. This article has 8 citations and is from a peer-reviewed journal.

9. (cassidy2023structureofthe pages 1-2): C. Keith Cassidy, Zhuan Qin, Thomas Frosio, Khoosheh Gosink, Zhengyi Yang, Mark S. P. Sansom, Phillip J. Stansfeld, John S. Parkinson, and Peijun Zhang. Structure of the native chemotaxis core signaling unit from phage e-protein lysed <i>e. coli</i> cells. Oct 2023. URL: https://doi.org/10.1128/mbio.00793-23, doi:10.1128/mbio.00793-23. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (ugolini2024microfluidicapproachesin pages 1-2): Giovanni Stefano Ugolini, Miaoxiao Wang, Eleonora Secchi, Roberto Pioli, Martin Ackermann, and Roman Stocker. Microfluidic approaches in microbial ecology. Lab on a Chip, 24:1394-1418, Feb 2024. URL: https://doi.org/10.1039/d3lc00784g, doi:10.1039/d3lc00784g. This article has 56 citations and is from a domain leading peer-reviewed journal.

11. (armitage2024twistsandturns pages 6-8): Judith P. Armitage. Twists and turns: 40 years of investigating how and why bacteria swim. Feb 2024. URL: https://doi.org/10.1099/mic.0.001432, doi:10.1099/mic.0.001432. This article has 5 citations and is from a peer-reviewed journal.

12. (vass2023analysisofchew‐like pages 13-14): Luke R. Vass, Robert B. Bourret, and Clay A. Foster. Analysis of <scp>chew</scp>‐like domains provides insights into organization of prokaryotic chemotaxis systems. Oct 2023. URL: https://doi.org/10.1002/prot.26430, doi:10.1002/prot.26430. This article has 11 citations.