---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:14:25.900046'
end_time: '2026-08-04T00:39:31.808199'
duration_seconds: 1505.91
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: copper tolerant
  trait_identifier: traitmech:000018
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: copper_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems
    and ATPase-driven cytoplasmic copper efflux.
  parent_traits: traitmech:000012
  synonyms: copper resistant
  evidence_summary: 'DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems
    to be the main mechanism responsible for cytoplasmic copper detoxification in
    until now studied bacteria (Review supports active efflux via the cue, cus, pco,
    and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper
    (Cu2+) to a MIC of 5 mM.)'
  causal_graph_summary: 'copper_tolerance_cop_efflux: 7 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 79
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** copper tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000018
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems and ATPase-driven cytoplasmic copper efflux.
- **Parent traits:** traitmech:000012
- **Synonyms:** copper resistant
- **Existing evidence:** DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems to be the main mechanism responsible for cytoplasmic copper detoxification in until now studied bacteria (Review supports active efflux via the cue, cus, pco, and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper (Cu2+) to a MIC of 5 mM.)
- **Existing causal graph summary:** copper_tolerance_cop_efflux: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **copper tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/copper_tolerant.yaml`.

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
- **Trait label:** copper tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000018
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems and ATPase-driven cytoplasmic copper efflux.
- **Parent traits:** traitmech:000012
- **Synonyms:** copper resistant
- **Existing evidence:** DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems to be the main mechanism responsible for cytoplasmic copper detoxification in until now studied bacteria (Review supports active efflux via the cue, cus, pco, and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper (Cu2+) to a MIC of 5 mM.)
- **Existing causal graph summary:** copper_tolerance_cop_efflux: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **copper tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/copper_tolerant.yaml`.

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


# TraitMech curation report: microbial copper tolerance

## Curation target

- **Trait label:** copper tolerant
- **Trait identifier:** `traitmech:000018`
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Parent:** `traitmech:000012`
- **Synonym:** copper resistant

## 1. Scope summary

### Operational definition

For TraitMech, **copper tolerant** should denote the experimentally observed capacity of a microorganism to grow, remain viable, or maintain fitness at an elevated, bioavailable concentration of Cu(I) and/or Cu(II), relative to an appropriate susceptible strain or copper-free control. The central mechanism is not simply “having copper genes,” but reducing toxic copper in vulnerable cellular pools through regulated trafficking, ATP-driven cytoplasmic export, periplasmic oxidation or trans-envelope export, sequestration, and repair of copper-induced damage. Recent deletion analysis supports the expert view that high-level tolerance is often an **emergent network phenotype**, rather than the product of one determinant (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 7-9).

Copper is also an essential micronutrient. Therefore, basal copper uptake, delivery to cuproenzymes, and homeostasis should not by themselves entail `traitmech:000018`. CopA2-like ATPases, for example, can supply periplasmic cuproenzymes rather than detoxify excess copper, whereas low-affinity/high-turnover CopA1-like ATPases preferentially export excess cytoplasmic Cu(I) (andrei2020cuhomeostasisin pages 16-19).

### Recommended inclusion criteria

Curate the trait when evidence includes at least one of the following:

1. Growth, MIC, MBC, IC50, survival, or competitive-fitness measurements under elevated copper.
2. A loss-of-function mutation that decreases copper tolerance, preferably restored by complementation.
3. Direct evidence that a mechanism lowers cytoplasmic or periplasmic copper, or prevents copper-mediated killing.
4. For environmental isolates, a stated maximum tolerated concentration together with growth or viability evidence.

### Boundary cases

- **Tolerance versus resistance:** the literature uses these terms inconsistently. Do not impose a universal MIC threshold. In *Pseudomonas aeruginosa*, the GI-7 island operationally distinguished high survival from ordinary homeostatic tolerance: a GI-7-bearing ST308 strain retained about `10^-1` survival after 24 h at 150 mg/L CuSO4, versus `10^-5–10^-6` for comparison strains, and GI-7 deletion abolished this advantage (virieuxpetit2022fromcoppertolerance pages 8-9).
- **Homeostasis:** maintenance of a normal intracellular copper quota is broader than growth under elevated copper. It is a contributing process, not an equivalent phenotype.
- **Biosorption or bioaccumulation:** copper binding by EPS, biomass, or metalloproteins is not sufficient unless connected to improved growth or survival. Accumulation can even indicate defective export.
- **Copper reduction/removal from medium:** this is an application phenotype and should not automatically be interpreted as cellular tolerance.
- **Cross-metal resistance:** Cu systems may also transport Ag(I), and isolates may tolerate Zn, Co, or Hg. Those are separate traits unless copper-specific evidence is present (rismondo2023thesensoryhistidine pages 1-2, yu2024isolationofhighly pages 4-6).
- **Condition dependence:** oxidation state, oxygen availability, medium composition, pH, chloride, sulfide, organic ligands, inoculum and assay duration alter bioavailable copper. Cus is especially important anaerobically because CueO-like oxidation requires oxygen (rismondo2023thesensoryhistidine pages 8-10, andrei2020cuhomeostasisin pages 19-21).

## 2. Current mechanistic model

Elevated copper enters or accumulates in the cell envelope and cytoplasm. Cytoplasmic Cu(I) is sensed by CueR-like regulators and scavenged by CopZ-like chaperones. CopA/CupA P1B-type ATPases use ATP to move Cu(I) from the cytoplasm to the periplasm. There, oxygen-dependent CueO/PcoA/CopA multicopper oxidases convert Cu(I) to less-toxic Cu(II), while CusCFBA/CusCBA exports periplasmic Cu(I) across the outer membrane. CusS–CusR senses periplasmic copper and induces the Cus pump. Glutathione and envelope-repair pathways support these dedicated systems; extracellular polymers can reduce exposure by copper biosorption (rebelo2023unravelingtherole pages 6-8, andrei2020cuhomeostasisin pages 16-19, hirth2023fullcopperresistance pages 16-18, rismondo2023thesensoryhistidine pages 1-2).

The strongest curation-ready relationships are summarized below.

| subject | predicate | object | taxon/condition | confidence | DOI |
|---|---|---|---|---|---|
| Cu(I)-bound CueR | activates transcription of | copA | *Escherichia coli*; cytoplasmic copper stress; Cue regulon (hyre2021copperhomeostaticmechanisms pages 2-4, bittner2017thecopperefflux pages 1-2, gautam2023linkingcopperassociatedsignal pages 3-5) | high | 10.1128/ecosalplus.esp-0014-2020 |
| Cu(I)-bound CueR | activates transcription of | cueO | *Escherichia coli*; cytoplasmic copper stress; Cue regulon (hyre2021copperhomeostaticmechanisms pages 2-4, bittner2017thecopperefflux pages 1-2, gautam2023linkingcopperassociatedsignal pages 3-5) | high | 10.1128/ecosalplus.esp-0014-2020 |
| CopZ copper chaperone | delivers cytoplasmic Cu(I) to | CopA Cu(+)-ATPase | *Pseudomonas aeruginosa*; cytoplasmic copper trafficking (virieuxpetit2022fromcoppertolerance pages 5-7, andrei2020cuhomeostasisin pages 10-12, giachino2020coppertolerancein pages 3-5) | medium | 10.3390/genes13020301 |
| CopA/CupA P1B-type ATPase | exports | cytoplasmic Cu(I) to the periplasm | Gram-negative bacteria; strongest primary evidence in *Cupriavidus metallidurans* and reviewed broadly (hirth2023fullcopperresistance pages 16-18, andrei2020cuhomeostasisin pages 16-19, hyre2021copperhomeostaticmechanisms pages 2-4) | high | 10.1128/aem.00567-23 |
| CueO/PcoA/CopA multicopper oxidase | oxidizes | periplasmic Cu(I) to Cu(II) | Enterobacteria and *C. metallidurans*; oxygen-dependent periplasmic detoxification (hirth2023fullcopperresistance pages 16-18, chaturvedi2014pathogenicadaptationsto pages 6-7, giachino2020coppertolerancein pages 3-5, andrei2020cuhomeostasisin pages 21-23) | high | 10.1128/aem.00567-23 |
| CusS/CusR two-component system | activates transcription of | cusCFBA | *Escherichia coli*; periplasmic copper sensing, strongest under anaerobic conditions (rismondo2023thesensoryhistidine pages 8-10, rismondo2023thesensoryhistidine pages 2-5) | high | 10.1128/spectrum.00291-23 |
| CusCFBA/CusCBA efflux complex | exports | periplasmic Cu(I) to the extracellular space | *E. coli* and *C. metallidurans*; especially important when oxygen is limiting (rismondo2023thesensoryhistidine pages 1-2, andrei2020cuhomeostasisin pages 19-21, hirth2023fullcopperresistance pages 16-18) | high | 10.1128/spectrum.00291-23 |
| Glutathione (via GshA) | cooperates with | Cop/Cus/Cup copper-defense systems | *C. metallidurans*; deletion analysis showed GSH amplifies resistance but is insufficient alone (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 7-9, hirth2023fullcopperresistance pages 11-12) | high | 10.1128/aem.00567-23 |
| Extracellular polymeric substances (EPS) | sequester/adsorb | copper | Deep-sea vent isolates; Cu induced EPS and adsorption of ~40–50 mg·g−1 Cu (yu2024isolationofhighly pages 4-6, yu2024isolationofhighly pages 1-2, yu2024isolationofhighly pages 2-3) | medium | 10.3389/fmicb.2024.1390451 |
| CopA/CupA-mediated copper export | decreases | intracellular copper accumulation | *Haemophilus influenzae* and *C. metallidurans*; ΔcopZA accumulated 97% more Cu, Cup reduced accumulation at high Cu (hirth2023fullcopperresistance pages 16-18, hirth2023fullcopperresistance pages 11-12, wong2023coppereffluxsystem pages 10-12) | high | 10.1128/iai.00091-23 |
| Reduced intracellular/periplasmic copper burden | enables | growth/survival at elevated copper | Broad bacterial trait; strongest mutant IC50/survival evidence in *C. metallidurans* and hospital-adapted *P. aeruginosa* (hirth2023fullcopperresistance pages 16-18, hirth2023fullcopperresistance pages 4-6, virieuxpetit2022fromcoppertolerance pages 8-9) | high | 10.1128/aem.00567-23 |
| copZA copper efflux locus | promotes | lung infection fitness under host copper stress | Nontypeable *Haemophilus influenzae*; copA mutant ~4-fold and copZA mutant ~20-fold underrepresented in murine lung infection (wong2023coppereffluxsystem pages 10-12) | high | 10.1128/iai.00091-23 |


*Table: This table lists the strongest candidate causal triples for TraitMech curation of microbial copper tolerance, prioritizing experimentally supported sensing, efflux, oxidation, sequestration, and fitness relationships. It is useful as a compact starting set for graph curation while preserving evidence strength and assay context.*

## 3. Candidate nodes, grouped by type

### Environmental and assay nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Elevated bioavailable copper | Label-only composite | Represent concentration and copper salt in evidence metadata rather than treating nominal concentration as universally comparable. |
| Copper(I), Cu(I) | `CHEBI:49552` | Predominant transported/sensed toxic species in many characterized systems. |
| Copper(II), Cu(II) | `CHEBI:29036` | Commonly supplied as CuSO4; may be reduced to Cu(I) intracellularly or under anoxia. |
| Molecular oxygen | `CHEBI:15379` | Required electron acceptor for CueO/PcoA/CopA multicopper-oxidase activity. |
| Anaerobic condition | `ENVO:00002040` is a possible environmental grounding; otherwise label-only | Strong modifier of Cus dependence; verify ontology fit before committing. |
| Copper sulfate exposure | Copper sulfate label plus concentration | Assay factor, not equivalent to free Cu2+ activity. |
| Growth/survival at elevated copper | `traitmech:000018` | Final trait node. Record MIC, IC50, survival fraction, time and medium. |

### Genes, proteins, transporters and regulators

| Node | Function and scope | Grounding recommendation |
|---|---|---|
| CueR | Cytoplasmic Cu(I)-responsive MerR-family transcription factor; activates `copA` and `cueO` in *E. coli* and `cueP` additionally in *Salmonella* (hyre2021copperhomeostaticmechanisms pages 2-4, bittner2017thecopperefflux pages 1-2) | Label plus taxon-specific gene/UniProt identifier. Do not use one universal protein CURIE. |
| CopA/CupA P1B1-type ATPase | ATP-driven Cu(I) export from cytoplasm to periplasm; usually the central cytoplasmic detoxification step (hirth2023fullcopperresistance pages 16-18, andrei2020cuhomeostasisin pages 16-19) | Label plus organism-specific identifier; molecular function may be associated with `GO:0005375` copper-ion transmembrane transporter activity and process `GO:0006825` copper-ion transport. |
| CopZ | Small cytoplasmic Cu(I) chaperone; scavenges Cu(I) and transfers it to efflux ATPases. *P. aeruginosa* CopZ1 interacts with the CopA1 amino-terminal domain, while CopZ2 may serve storage functions (virieuxpetit2022fromcoppertolerance pages 5-7, andrei2020cuhomeostasisin pages 10-12) | Taxon-specific identifier. Keep CopZ1 and CopZ2 separate where paralog functions differ. |
| CueO | Periplasmic multicopper oxidase that converts Cu(I) to Cu(II) (chaturvedi2014pathogenicadaptationsto pages 6-7, giachino2020coppertolerancein pages 3-5) | Taxon-specific identifier; do not merge automatically with all CopA proteins. |
| PcoA | Plasmid-associated periplasmic multicopper oxidase; can substitute for CueO in *E. coli* (chaturvedi2014pathogenicadaptationsto pages 6-7, andrei2020cuhomeostasisin pages 21-23) | Taxon/plasmid-specific identifier. |
| CopA multicopper oxidase | Periplasmic oxidase in the `cop` system of *Cupriavidus* and some other taxa (hirth2023fullcopperresistance pages 16-18) | Explicitly label **CopA oxidase**, not CopA ATPase. |
| CusS–CusR | Two-component sensor/regulator of `cusCFBA`; CusS senses periplasmic copper (rismondo2023thesensoryhistidine pages 8-10, rismondo2023thesensoryhistidine pages 2-5) | Separate taxon-specific kinase and response-regulator nodes. |
| CusCFBA/CusCBA | Cu(I)/Ag(I) trans-envelope efflux system; CusA is a proton-driven RND transporter, CusB a membrane-fusion protein, CusC an outer-membrane channel, and CusF a periplasmic chaperone (rismondo2023thesensoryhistidine pages 1-2, andrei2020cuhomeostasisin pages 19-21) | Complex and subunit nodes, with taxon-specific identifiers. |
| PcoB/PcoD/PcoE | Components of plasmid `pco` systems; reported roles include outer-membrane handling, uptake/incorporation and periplasmic sequestration (rebelo2023unravelingtherole pages 6-8) | **Uncertain for a generic graph.** Functions and directionality remain context dependent. |
| GshA / glutathione | Supports copper defense in *C. metallidurans* but does not independently substitute for primary exporters (hirth2023fullcopperresistance pages 7-9, hirth2023fullcopperresistance pages 9-11) | Glutathione: `CHEBI:16856`; GshA should be taxon-specific. |
| Gig system | Copper-resistance accessory determinant of incompletely resolved function in *C. metallidurans* (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 9-11) | Label-only; mark mechanism uncertain. |
| ScsABCD / Dsb pathways | Envelope thiol-disulfide and damage-response systems that can contribute to copper tolerance in Enterobacteria (giachino2020coppertolerancein pages 3-5) | Accessory, taxon-specific nodes; do not place in a universal minimal graph. |

### Chemicals, compartments and processes

| Node | Suggested grounding / role |
|---|---|
| ATP | `CHEBI:15422`; energy source for CopA/CupA transport. |
| ADP | `CHEBI:16761`; product of ATP-dependent transport cycle. |
| Glutathione | `CHEBI:16856`; redox/accessory defense. |
| Cytoplasm | `GO:0005737`; location of CueR, CopZ and the toxic pool handled by P1B ATPases. |
| Plasma membrane | `GO:0005886`; location of CopA/CupA and CusA. |
| Periplasmic space | `GO:0042597`; location of CueO/PcoA/CopA oxidases, CusF and the pool sensed by CusS. |
| Bacterial outer membrane | `GO:0019867`; traversed by CusC and affected by Pco proteins. |
| Extracellular region | `GO:0005576`; destination of Cus-mediated export and location of EPS. |
| Copper-ion transport | `GO:0006825`; broad process node. |
| EPS-mediated copper sequestration | Label-only process | Mechanistically plausible and quantitatively supported in selected isolates, but not universal. |
| Copper-induced envelope/Fe–S/protein damage | Label-only or separately grounded GO processes | Accessory damage branch; specific molecular target evidence should be supplied before adding each edge. |

## 4. Candidate causal edges with auditable evidence

| Subject–predicate–object | Reference and publication date | Supporting snippet | Interpretation and confidence |
|---|---|---|---|
| Elevated cytoplasmic Cu(I) **activates** CueR | DOI [10.3389/fmolb.2017.00009](https://doi.org/10.3389/fmolb.2017.00009), Feb 2017 | “CueR forms homodimers” and its C112/C120 cysteines bind Cu+ with high affinity. | Strong for *E. coli*; CueR ortholog regulons differ by taxon (bittner2017thecopperefflux pages 1-2). |
| Cu(I)-CueR **activates transcription of** `copA` | DOI [10.1128/ecosalplus.esp-0014-2020](https://doi.org/10.1128/ecosalplus.esp-0014-2020), Dec 2021 | Holo-CueR “activates transcription by unwinding DNA”; CueR boxes occur upstream of `copA`. | High confidence in *E. coli* and *Salmonella* (hyre2021copperhomeostaticmechanisms pages 2-4). |
| Cu(I)-CueR **activates transcription of** `cueO` | Same reference | CueR recognizes promoter sequences of `copA` and `cueO`. | High confidence in Enterobacteria; do not assume `cueO` exists universally (hyre2021copperhomeostaticmechanisms pages 2-4). |
| CopZ1 **delivers Cu(I) to** CopA1 | DOI [10.3390/genes13020301](https://doi.org/10.3390/genes13020301), Feb 2022 | CopZ1 “interacts with the cytoplasmic amino-terminal domain of CopA1” and facilitates copper delivery. | Medium-high, *P. aeruginosa*-specific paralog evidence (virieuxpetit2022fromcoppertolerance pages 5-7). |
| CopA/CupA ATPase **exports** cytoplasmic Cu(I) to periplasm | DOI [10.3390/membranes10090242](https://doi.org/10.3390/membranes10090242), Sep 2020 | CopA is a P1B-1 ATPase that “exports Cu(I) from bacterial cytoplasm to the periplasm using ATP hydrolysis.” | High confidence; central generic edge (andrei2020cuhomeostasisin pages 16-19). |
| CupA activity **increases** copper tolerance | DOI [10.1128/aem.00567-23](https://doi.org/10.1128/aem.00567-23), Jun 2023 | CupA was “by far the most important” system; deletion reduced resistance approximately 46-fold in the parent background. | High-confidence primary mutant evidence in *C. metallidurans* (hirth2023fullcopperresistance pages 9-11, hirth2023fullcopperresistance pages 4-6). |
| CueO/PcoA/CopA oxidase **oxidizes** periplasmic Cu(I) to Cu(II) | DOI [10.1128/aem.00567-23](https://doi.org/10.1128/aem.00567-23), Jun 2023 | CopA is a periplasmic “Cu(I) and Au(I) oxidase” that converts Cu(I) to Cu(II). | High confidence but oxygen-dependent and protein-name-specific (hirth2023fullcopperresistance pages 16-18). |
| Cu(I) oxidation **decreases** copper toxicity/accumulation | Same reference | Oxidation prevents Cu(I)-linked membrane/ROS damage and decreases accumulation because Cu(I) is a better uptake substrate. | High in *C. metallidurans*; biochemical generalization should retain oxygen and taxon qualifiers (hirth2023fullcopperresistance pages 16-18). |
| Periplasmic Cu(I) **activates** CusS–CusR | DOI [10.1128/spectrum.00291-23](https://doi.org/10.1128/spectrum.00291-23), Apr 2023 | Evidence showed CusS “senses periplasmic copper ions.” | High-confidence localization and sensor edge in *E. coli* (rismondo2023thesensoryhistidine pages 8-10, rismondo2023thesensoryhistidine pages 2-5). |
| CusS–CusR **activates transcription of** `cusCFBA` | Same reference | Simultaneous deletion of critical CusS periplasmic regions “ablated cusCFBA upregulation.” | High confidence; the histidine-rich and methionine-rich regions contribute jointly (rismondo2023thesensoryhistidine pages 8-10). |
| CusCFBA **exports** periplasmic Cu(I) extracellularly | Same reference | CusCBA exports Cu(I)/Ag(I) “from periplasm to extracellular space”; CusA couples proton import to export. | High confidence, especially anaerobically (rismondo2023thesensoryhistidine pages 1-2). |
| CusS/Cus system **increases** anaerobic copper tolerance | Same reference | Anaerobic IC50 fell from `>100 µM` in wild type to about `25 µM` in Δ`cusS`, and complementation restored resistance. | Strong primary evidence in *E. coli* W3110; assay-specific (rismondo2023thesensoryhistidine pages 5-8). |
| GSH **cooperates with** Cop/Cus/Cup systems | DOI [10.1128/aem.00567-23](https://doi.org/10.1128/aem.00567-23), Jun 2023 | “GSH amplifies individual system contributions” but cannot function independently. | High-confidence network edge in *C. metallidurans*; do not curate GSH as an independent Cu exporter (hirth2023fullcopperresistance pages 7-9, hirth2023fullcopperresistance pages 9-11). |
| Copper exposure **induces** EPS production | DOI [10.3389/fmicb.2024.1390451](https://doi.org/10.3389/fmicb.2024.1390451), Aug 2024 | At 1 mM Cu(II), *Halomonas* EPS rose from `379.65` to `1013.00 mg/L`; polysaccharide and protein increased 3.64-fold. | Strong for the tested deep-sea isolates; not generic across bacteria (yu2024isolationofhighly pages 4-6). |
| EPS **sequesters** extracellular copper | Same reference | Purified EPS adsorbed approximately `40–50 mg Cu g−1`. | Direct adsorption evidence, but contribution to growth is partly inferred; mark medium-confidence (yu2024isolationofhighly pages 1-2). |
| CopA plus CopZ **decreases** intracellular copper accumulation | DOI [10.1128/iai.00091-23](https://doi.org/10.1128/iai.00091-23), May 2023 | Δ`copZA` accumulated `97% more copper` than wild type during growth with 0.5 mM CuSO4. | High-confidence primary evidence in nontypeable *H. influenzae* (wong2023coppereffluxsystem pages 10-12). |
| CopA/CopZ-mediated detoxification **promotes** infection fitness | Same reference | Δ`copA` and Δ`copZA` were approximately 4-fold and 20-fold underrepresented in mixed murine lung infection. | High confidence for this host/model; host copper is a contextual stressor, not the trait itself (wong2023coppereffluxsystem pages 10-12). |
| Coordinated Cup–Cop–Cus–GSH–Gig activity **increases** copper tolerance | DOI [10.1128/aem.00567-23](https://doi.org/10.1128/aem.00567-23), Jun 2023 | All five systems contributed in the order Cup, Cop, Cus, GSH and Gig; Cup–Cop cooperation accounted for about 77% of parent resistance. | Strong network-level primary evidence, but specific to *C. metallidurans* AE104 (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 7-9). |

## 5. Recent developments and quantitative findings, 2023–2024

1. **Network-emergent tolerance.** Systematic single-through-quintuple deletion analysis in *C. metallidurans* showed that Cup, Cop, Cus, GSH and Gig are not interchangeable modules. CupA was indispensable as the primary cytoplasmic exporter, while the remaining systems restored high resistance only through cooperation. Reported strain IC50 values spanned approximately 0.4–743 µM under the study conditions, illustrating how strongly genotype changes phenotype (hirth2023fullcopperresistance pages 1-3, hirth2023fullcopperresistance pages 3-4).

2. **Direct evidence for periplasmic copper sensing.** A 2023 study localized the relevant CusS sensor region to the periplasm and showed that combined disruption of candidate copper-binding regions eliminated `cusCFBA` induction. Under anaerobic conditions, Δ`cusS` reduced IC50 from greater than 100 µM to approximately 25 µM (rismondo2023thesensoryhistidine pages 8-10, rismondo2023thesensoryhistidine pages 5-8).

3. **Copper defense contributes to infection fitness.** In 2023, tandem `copZ` copies and `copA` in *H. influenzae* were linked to both Cu-specific tolerance and murine lung fitness. The Δ`copZA` strain accumulated 97% more copper and was about 20-fold underrepresented in lung competition, compared with approximately fourfold for Δ`copA` alone (wong2023coppereffluxsystem pages 10-12).

4. **Environmental isolates reveal an EPS branch.** Twelve 2024 deep-sea vent isolates tolerated 6–10 mM Cu(II); EPS from selected strains adsorbed 40–50 mg Cu per gram, while *Marinobacter metalliresistant* CuT 6 tolerated up to 8 mM copper. These are valuable application and environmental-context nodes, but they should not replace the core efflux graph (yu2024isolationofhighly pages 4-6, yu2024isolationofhighly pages 1-2, yu2024isolationofhighly pages 2-3).

5. **One Health and antimicrobial-resistance implications.** A 2024 FEMS review concluded that metal-resistance genes are frequently linked to antibiotic-resistance genes on conjugative plasmids and other mobile elements. Across analyzed complete bacterial genomes, those containing metal-resistance genes were reported to be approximately 10-fold more likely to contain antibiotic-resistance genes, and about 50% carried both classes. Nevertheless, the authors warn that co-resistance is often inferred from correlation without demonstrating functional expression in a defined host (gillieatt2024unravellingthemechanisms pages 10-11). Specific mechanistic examples include Cu-induced MdtABC, which can handle copper/zinc and β-lactams or novobiocin, and `cusCFBA` overexpression producing a reported threefold increase in fosfomycin resistance (gillieatt2024unravellingthemechanisms pages 11-13).

## 6. Current applications and real-world relevance

- **Bioremediation and metal recovery:** tolerant strains and EPS can immobilize or concentrate copper from mine drainage, industrial wastewater and marine contamination. The 2024 vent isolates provide quantitative biosorption candidates, but performance in purified EPS or marine broth does not establish field-scale removal (yu2024isolationofhighly pages 4-6, yu2024isolationofhighly pages 1-2).
- **Pathogen control:** copper surfaces, host copper intoxication and copper-based antimicrobials target the same networks. CopA/CopZ and CueO/Cus defenses can therefore affect pathogen persistence and virulence, as demonstrated by the *H. influenzae* lung model and oxic CueO phenotypes (chaturvedi2014pathogenicadaptationsto pages 6-7, wong2023coppereffluxsystem pages 10-12).
- **Hospital water systems:** copper-handling genomic islands can support persistence of particular *P. aeruginosa* lineages in copper plumbing. GI-7 deletion evidence supports causation in selected strains, but not a universal hospital-persistence edge (virieuxpetit2022fromcoppertolerance pages 8-9).
- **Agriculture and food production:** copper feed supplements and copper biocides may retain mobile elements that also encode antibiotic resistance. In a 2023 poultry-chain study, 81% of *Klebsiella pneumoniae* isolates were copper-tolerant (`silA`/`pcoD` positive; CuSO4 MIC ≥16 mM), 90% were multidrug resistant, and related IncF plasmids carried antibiotic and metal-tolerance genes. This is epidemiologically important but should be modeled as a separate co-selection graph, not as an intrinsic mechanism of `traitmech:000018`.
- **Synthetic biology:** copper-responsive CueR/Cop systems can serve as inducible expression circuits or biosensors. Such uses depend on regulatory sensitivity and host background and should not be interpreted as evidence that the engineered host has high copper tolerance.

## 7. Expert synthesis for the TraitMech graph

The most defensible generic backbone is:

`elevated copper → increased intracellular/periplasmic Cu(I) → copper sensing → induction of copper-defense genes → Cu(I) trafficking/export or oxidation → reduced toxic copper burden → growth/survival at elevated copper`.

Three context-dependent branches should be attached rather than collapsed:

1. **Aerobic envelope branch:** CopA/CupA ATPase → periplasmic Cu(I) → CueO/PcoA/CopA oxidase → Cu(II).
2. **Anaerobic envelope branch:** periplasmic Cu(I) → CusS/CusR → CusCFBA → extracellular Cu(I).
3. **Accessory branch:** GSH, thiol-disulfide repair and EPS sequestration → reduced copper damage/exposure.

This architecture captures the current expert understanding that copper tolerance requires both direct homeostatic export and pathways that prevent or repair copper-induced damage (giachino2020coppertolerancein pages 3-5). It also avoids treating the `cue`, `cus`, `pco` and `cop` labels as interchangeable operons.

## 8. Warnings: claims not yet ready for generic TraitMech curation

1. **Do not create one generic “CopA protein” node.** `CopA` can name a P1B ATPase or a periplasmic multicopper oxidase. These have different localization, chemistry and causal roles (virieuxpetit2022fromcoppertolerance pages 4-5, hirth2023fullcopperresistance pages 16-18).
2. **Do not assert that Cus exports cytoplasmic copper directly.** The strongest evidence supports periplasm-to-exterior export; in *C. metallidurans*, Cus cannot substitute for CupA-mediated cytoplasmic export (hirth2023fullcopperresistance pages 9-11, rismondo2023thesensoryhistidine pages 1-2).
3. **Do not make CueO oxidation oxygen-independent.** CueO-like oxidases require O2; Cus assumes greater importance under anoxia (chaturvedi2014pathogenicadaptationsto pages 6-7, rismondo2023thesensoryhistidine pages 8-10).
4. **Do not curate EPS production as universal.** The 2024 evidence is strain- and assay-specific, and adsorption was measured separately from the complete growth mechanism (yu2024isolationofhighly pages 4-6, yu2024isolationofhighly pages 1-2).
5. **Do not infer phenotype from gene presence alone.** Expression, allelic integrity, copy number, regulation, mobile-element context and assay conditions matter.
6. **Do not use a universal MIC cutoff.** Nominal CuSO4 concentrations are not directly comparable across media because copper speciation and availability differ. Hirth et al. explicitly cautioned that IC50 values can differ with medium composition (hirth2023fullcopperresistance pages 14-16).
7. **Treat `pcoB`, `pcoD`, `pcoE`, Gig and broad “biofilm” edges as provisional.** Their directionality or contribution can be system- and taxon-specific; add only with direct evidence for the selected organism (rebelo2023unravelingtherole pages 6-8, hirth2023fullcopperresistance pages 9-11).
8. **Keep antibiotic co-selection outside the core trait mechanism.** Genetic linkage and shared efflux can explain co-selection, but many environmental studies are correlational and do not establish that copper caused antibiotic resistance in a particular host (gillieatt2024unravellingthemechanisms pages 11-13, gillieatt2024unravellingthemechanisms pages 10-11, gillieatt2024unravellingthemechanisms pages 9-10).

## 9. DOI-first bibliography

1. Hirth N. et al. **Full Copper Resistance in *Cupriavidus metallidurans* Requires the Interplay of Many Resistance Systems.** *Applied and Environmental Microbiology*. Published June 2023. [https://doi.org/10.1128/aem.00567-23](https://doi.org/10.1128/aem.00567-23) (hirth2023fullcopperresistance pages 1-3).
2. Rismondo J., Große C., Nies D.H. **The Sensory Histidine Kinase CusS of *Escherichia coli* Senses Periplasmic Copper Ions.** *Microbiology Spectrum*. Published April 2023. [https://doi.org/10.1128/spectrum.00291-23](https://doi.org/10.1128/spectrum.00291-23) (rismondo2023thesensoryhistidine pages 8-10).
3. Wong S.M., Gawronski J., Akerley B.J. **Copper Efflux System Required in Murine Lung Infection by *Haemophilus influenzae*.** *Infection and Immunity*. Published May 2023. [https://doi.org/10.1128/iai.00091-23](https://doi.org/10.1128/iai.00091-23) (wong2023coppereffluxsystem pages 10-12).
4. Yu T. et al. **Isolation of Highly Copper-Resistant Bacteria from Deep-Sea Hydrothermal Fields and Description of *Marinobacter metalliresistant* sp. nov.** *Frontiers in Microbiology*. Published August 2024. [https://doi.org/10.3389/fmicb.2024.1390451](https://doi.org/10.3389/fmicb.2024.1390451) (yu2024isolationofhighly pages 4-6).
5. Gillieatt B.F., Coleman N.V. **Unravelling the Mechanisms of Antibiotic and Heavy Metal Resistance Co-selection in Environmental Bacteria.** *FEMS Microbiology Reviews*. Published June 2024. [https://doi.org/10.1093/femsre/fuae017](https://doi.org/10.1093/femsre/fuae017) (gillieatt2024unravellingthemechanisms pages 11-13).
6. Rebelo A. et al. **Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain.** *Antibiotics*. Published September 2023. [https://doi.org/10.3390/antibiotics12091474](https://doi.org/10.3390/antibiotics12091474) (rebelo2023unravelingtherole pages 6-8).
7. Giachino A., Waldron K.J. **Copper Tolerance in Bacteria Requires the Activation of Multiple Accessory Pathways.** *Molecular Microbiology*. Published May 2020. [https://doi.org/10.1111/mmi.14522](https://doi.org/10.1111/mmi.14522) (giachino2020coppertolerancein pages 3-5).
8. Andrei A. et al. **Cu Homeostasis in Bacteria: The Ins and Outs.** *Membranes*. Published September 2020. [https://doi.org/10.3390/membranes10090242](https://doi.org/10.3390/membranes10090242) (andrei2020cuhomeostasisin pages 16-19).
9. Hyre A. et al. **Copper Homeostatic Mechanisms and Their Role in the Virulence of *Escherichia coli* and *Salmonella enterica*.** *EcoSal Plus*. Published December 2021. [https://doi.org/10.1128/ecosalplus.esp-0014-2020](https://doi.org/10.1128/ecosalplus.esp-0014-2020) (hyre2021copperhomeostaticmechanisms pages 2-4).
10. Argüello J.M., Raimunda D., Padilla-Benavides T. **Mechanisms of Copper Homeostasis in Bacteria.** *Frontiers in Cellular and Infection Microbiology*. Published November 2013. [https://doi.org/10.3389/fcimb.2013.00073](https://doi.org/10.3389/fcimb.2013.00073) (arguello2013mechanismsofcopper pages 3-4).
11. Virieux-Petit M. et al. **From Copper Tolerance to Resistance in *Pseudomonas aeruginosa* towards Patho-Adaptation and Hospital Success.** *Genes*. Published February 2022. [https://doi.org/10.3390/genes13020301](https://doi.org/10.3390/genes13020301) (virieuxpetit2022fromcoppertolerance pages 8-9).
12. Bittner L.-M. et al. **The Copper Efflux Regulator CueR Is Subject to ATP-Dependent Proteolysis in *Escherichia coli*.** *Frontiers in Molecular Biosciences*. Published February 2017. [https://doi.org/10.3389/fmolb.2017.00009](https://doi.org/10.3389/fmolb.2017.00009) (bittner2017thecopperefflux pages 1-2).

References

1. (hirth2023fullcopperresistance pages 1-3): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

2. (hirth2023fullcopperresistance pages 7-9): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

3. (andrei2020cuhomeostasisin pages 16-19): Andreea Andrei, Yavuz Öztürk, Bahia Khalfaoui-Hassani, Juna Rauch, Dorian Marckmann, Petru-Iulian Trasnea, Fevzi Daldal, and Hans-Georg Koch. Cu homeostasis in bacteria: the ins and outs. Membranes, 10:242, Sep 2020. URL: https://doi.org/10.3390/membranes10090242, doi:10.3390/membranes10090242. This article has 169 citations.

4. (virieuxpetit2022fromcoppertolerance pages 8-9): Maxine Virieux-Petit, Florence Hammer-Dedet, Fabien Aujoulat, Estelle Jumas-Bilak, and Sara Romano-Bertrand. From copper tolerance to resistance in pseudomonas aeruginosa towards patho-adaptation and hospital success. Genes, 13:301, Feb 2022. URL: https://doi.org/10.3390/genes13020301, doi:10.3390/genes13020301. This article has 53 citations.

5. (rismondo2023thesensoryhistidine pages 1-2): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

6. (yu2024isolationofhighly pages 4-6): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 14 citations and is from a peer-reviewed journal.

7. (rismondo2023thesensoryhistidine pages 8-10): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

8. (andrei2020cuhomeostasisin pages 19-21): Andreea Andrei, Yavuz Öztürk, Bahia Khalfaoui-Hassani, Juna Rauch, Dorian Marckmann, Petru-Iulian Trasnea, Fevzi Daldal, and Hans-Georg Koch. Cu homeostasis in bacteria: the ins and outs. Membranes, 10:242, Sep 2020. URL: https://doi.org/10.3390/membranes10090242, doi:10.3390/membranes10090242. This article has 169 citations.

9. (rebelo2023unravelingtherole pages 6-8): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 35 citations.

10. (hirth2023fullcopperresistance pages 16-18): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

11. (hyre2021copperhomeostaticmechanisms pages 2-4): Amanda Hyre, Kaitlin Casanova-Hampton, and Sargurunathan Subashchandrabose. Copper homeostatic mechanisms and their role in the virulence of escherichia coli and salmonella enterica. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0014-2020, doi:10.1128/ecosalplus.esp-0014-2020. This article has 70 citations.

12. (bittner2017thecopperefflux pages 1-2): Lisa-Marie Bittner, Alexander Kraus, Sina Schäkermann, and Franz Narberhaus. The copper efflux regulator cuer is subject to atp-dependent proteolysis in escherichia coli. Frontiers in Molecular Biosciences, Feb 2017. URL: https://doi.org/10.3389/fmolb.2017.00009, doi:10.3389/fmolb.2017.00009. This article has 23 citations.

13. (gautam2023linkingcopperassociatedsignal pages 3-5): Pratima Gautam, Ivan Erill, and Kathleen Cusick. Linking copper-associated signal transduction systems with their environment in marine bacteria. Apr 2023. URL: https://doi.org/10.13016/m2gdm3-y5hr, doi:10.13016/m2gdm3-y5hr. This article has 13 citations.

14. (virieuxpetit2022fromcoppertolerance pages 5-7): Maxine Virieux-Petit, Florence Hammer-Dedet, Fabien Aujoulat, Estelle Jumas-Bilak, and Sara Romano-Bertrand. From copper tolerance to resistance in pseudomonas aeruginosa towards patho-adaptation and hospital success. Genes, 13:301, Feb 2022. URL: https://doi.org/10.3390/genes13020301, doi:10.3390/genes13020301. This article has 53 citations.

15. (andrei2020cuhomeostasisin pages 10-12): Andreea Andrei, Yavuz Öztürk, Bahia Khalfaoui-Hassani, Juna Rauch, Dorian Marckmann, Petru-Iulian Trasnea, Fevzi Daldal, and Hans-Georg Koch. Cu homeostasis in bacteria: the ins and outs. Membranes, 10:242, Sep 2020. URL: https://doi.org/10.3390/membranes10090242, doi:10.3390/membranes10090242. This article has 169 citations.

16. (giachino2020coppertolerancein pages 3-5): Andrea Giachino and Kevin J. Waldron. Copper tolerance in bacteria requires the activation of multiple accessory pathways. Molecular Microbiology, 114:377-390, May 2020. URL: https://doi.org/10.1111/mmi.14522, doi:10.1111/mmi.14522. This article has 244 citations and is from a domain leading peer-reviewed journal.

17. (chaturvedi2014pathogenicadaptationsto pages 6-7): Kaveri S. Chaturvedi and Jeffrey P. Henderson. Pathogenic adaptations to host-derived antibacterial copper. Frontiers in Cellular and Infection Microbiology, Feb 2014. URL: https://doi.org/10.3389/fcimb.2014.00003, doi:10.3389/fcimb.2014.00003. This article has 185 citations.

18. (andrei2020cuhomeostasisin pages 21-23): Andreea Andrei, Yavuz Öztürk, Bahia Khalfaoui-Hassani, Juna Rauch, Dorian Marckmann, Petru-Iulian Trasnea, Fevzi Daldal, and Hans-Georg Koch. Cu homeostasis in bacteria: the ins and outs. Membranes, 10:242, Sep 2020. URL: https://doi.org/10.3390/membranes10090242, doi:10.3390/membranes10090242. This article has 169 citations.

19. (rismondo2023thesensoryhistidine pages 2-5): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

20. (hirth2023fullcopperresistance pages 11-12): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

21. (yu2024isolationofhighly pages 1-2): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 14 citations and is from a peer-reviewed journal.

22. (yu2024isolationofhighly pages 2-3): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 14 citations and is from a peer-reviewed journal.

23. (wong2023coppereffluxsystem pages 10-12): Sandy M. Wong, Jeffrey Gawronski, and Brian J. Akerley. Copper efflux system required in murine lung infection by haemophilus influenzae composed of a canonical atpase gene and tandem chaperone gene copies. Infection and Immunity, May 2023. URL: https://doi.org/10.1128/iai.00091-23, doi:10.1128/iai.00091-23. This article has 7 citations and is from a peer-reviewed journal.

24. (hirth2023fullcopperresistance pages 4-6): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

25. (hirth2023fullcopperresistance pages 9-11): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

26. (rismondo2023thesensoryhistidine pages 5-8): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

27. (hirth2023fullcopperresistance pages 3-4): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

28. (gillieatt2024unravellingthemechanisms pages 10-11): Brodie F Gillieatt and Nicholas V. Coleman. Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria. FEMS Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1093/femsre/fuae017, doi:10.1093/femsre/fuae017. This article has 264 citations and is from a domain leading peer-reviewed journal.

29. (gillieatt2024unravellingthemechanisms pages 11-13): Brodie F Gillieatt and Nicholas V. Coleman. Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria. FEMS Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1093/femsre/fuae017, doi:10.1093/femsre/fuae017. This article has 264 citations and is from a domain leading peer-reviewed journal.

30. (virieuxpetit2022fromcoppertolerance pages 4-5): Maxine Virieux-Petit, Florence Hammer-Dedet, Fabien Aujoulat, Estelle Jumas-Bilak, and Sara Romano-Bertrand. From copper tolerance to resistance in pseudomonas aeruginosa towards patho-adaptation and hospital success. Genes, 13:301, Feb 2022. URL: https://doi.org/10.3390/genes13020301, doi:10.3390/genes13020301. This article has 53 citations.

31. (hirth2023fullcopperresistance pages 14-16): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 19 citations and is from a peer-reviewed journal.

32. (gillieatt2024unravellingthemechanisms pages 9-10): Brodie F Gillieatt and Nicholas V. Coleman. Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria. FEMS Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1093/femsre/fuae017, doi:10.1093/femsre/fuae017. This article has 264 citations and is from a domain leading peer-reviewed journal.

33. (arguello2013mechanismsofcopper pages 3-4): José M. Argüello, Daniel Raimunda, and Teresita Padilla-Benavides. Mechanisms of copper homeostasis in bacteria. Frontiers in Cellular and Infection Microbiology, Nov 2013. URL: https://doi.org/10.3389/fcimb.2013.00073, doi:10.3389/fcimb.2013.00073. This article has 415 citations.