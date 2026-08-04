---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:37:25.183070'
end_time: '2026-08-04T09:47:47.705591'
duration_seconds: 622.52
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: polyphosphate granule
  trait_identifier: traitmech:000068
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: polyphosphate_granule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular storage inclusion of inorganic polyphosphate (a polymer
    of many phosphate residues), historically called a volutin or metachromatic granule,
    serving as a phosphate and energy reserve.
  parent_traits: traitmech:000066
  synonyms: volutin granule, metachromatic granule
  evidence_summary: "DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, G\xF3mez-Garc\xED\
    a & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy\
    \ reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:\
    \  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular\
    \ inclusions.)"
  causal_graph_summary: 'polyphosphate_granule_storage: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** polyphosphate granule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000068
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion of inorganic polyphosphate (a polymer of many phosphate residues), historically called a volutin or metachromatic granule, serving as a phosphate and energy reserve.
- **Parent traits:** traitmech:000066
- **Synonyms:** volutin granule, metachromatic granule
- **Existing evidence:** DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, Gómez-García & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular inclusions.)
- **Existing causal graph summary:** polyphosphate_granule_storage: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **polyphosphate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyphosphate_granule.yaml`.

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
- **Trait label:** polyphosphate granule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000068
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular storage inclusion of inorganic polyphosphate (a polymer of many phosphate residues), historically called a volutin or metachromatic granule, serving as a phosphate and energy reserve.
- **Parent traits:** traitmech:000066
- **Synonyms:** volutin granule, metachromatic granule
- **Existing evidence:** DOI:10.1146/annurev.biochem.77.083007.093039:  (Rao, Gómez-García & Kornberg review inorganic polyphosphate, accumulated as granules, as a phosphate/energy reserve essential for growth and survival.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include polyphosphate bodies among bacterial intracellular inclusions.)
- **Existing causal graph summary:** polyphosphate_granule_storage: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **polyphosphate granule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/polyphosphate_granule.yaml`.

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


# TraitMech curation report: polyphosphate granule

**Trait label:** polyphosphate granule  
**Trait identifier:** `traitmech:000068`  
**Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED  
**Parent:** `traitmech:000066`  
**Synonyms:** volutin granule; metachromatic granule

## 1. Scope summary

`traitmech:000068` should denote the **capacity or observed state of forming a discrete intracellular inclusion enriched in inorganic polyphosphate (polyP)**. PolyP is a linear polymer of roughly 3–1,000 orthophosphate residues joined by phosphoanhydride bonds; its strongly anionic backbone associates with Ca²⁺, Mg²⁺ and other cations. The granular phenotype is morphological and particulate, not merely the presence of soluble or diffuse cellular polyP (moreno2013polyphosphateandits pages 1-2, schoeppe2024anupdateon pages 2-4).

Reported bacterial granules are electron-dense intracellular particles approximately 15–500 nm across. In nitrogen-starved *Pseudomonas aeruginosa*, mature granules reached about 200 nm and occupied about 2% of cell volume at peak accumulation (omelon2013areviewof pages 6-8, racki2017polyphosphategranulebiogenesis pages 1-1). Historically, granules were recognized by the purple or pink metachromatic response produced when basic blue dyes bind polyP; the dye absorption maximum can shift from approximately 630 to 530 nm (kornberg2003inorganicpolyphosphatea pages 2-4, rao2009inorganicpolyphosphateessential pages 4-5).

### Inclusion criteria

A positive trait assertion should ideally require at least one of:

1. Electron-dense, spatially discrete intracellular bodies verified as polyP by elemental/spectroscopic analysis.
2. Granular DAPI, JC-D7, toluidine-blue, or polyP-binding-domain signal supported by a genetic control such as loss after deletion of a required `ppk` gene.
3. Biochemical polyP measurement combined with microscopy establishing particulate localization.
4. A well-supported historical description of intracellular volutin/metachromatic granules.

Suitable orthogonal methods include TEM or cryo-electron microscopy, DAPI or polyP-selective dyes, ^31P-NMR, urea-PAGE, X-ray microanalysis/fluorescence, Raman microscopy, and genetically validated polyP-binding domains (omelon2013areviewof pages 6-8, moreno2013polyphosphateandits pages 1-2, schoeppe2024anupdateon pages 15-16).

### Boundary cases and exclusions

- **Diffuse intracellular polyP:** polyP abundance alone does not establish granules. In yeast, granular material may represent only about 15% of total cellular polyP, illustrating why polymer abundance and granule morphology should remain separate traits (rao2009inorganicpolyphosphateessential pages 5-6).
- **Acidocalcisome:** do not treat every bacterial polyP granule as an acidocalcisome. Reserve that label for an acidic, membrane-delimited compartment supported by membrane, proton-pump, transporter, or pH evidence. “PolyP granule” is the safer generic class.
- **PHA/PHB granules:** these are carbon-storage inclusions, chemically distinct from polyP. In starvation experiments, PHA may appear later and must be distinguished by chemical or genetic evidence (racki2017polyphosphategranulebiogenesis pages 1-3).
- **Apatite, struvite, or other phosphate minerals:** phosphorus-rich particles are not necessarily polyP. X-ray methods found that only about half of phosphorus-rich regions in one marine-sediment context were polyP rather than apatite (omelon2013areviewof pages 6-8).
- **Extracellular or secreted polyP:** exclude unless intracellular granules are independently demonstrated.
- **Metachromatic staining alone:** supportive but not definitive because fixation, dye behavior, other polyanions, and mineral inclusions may confound interpretation.

## 2. Candidate nodes

### Chemicals and metabolites

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| inorganic polyphosphate | **CHEBI:16838** | Polymer stored in the inclusion; confirm identifier during repository validation. |
| phosphate / orthophosphate | **CHEBI:18367** | Imported substrate and PPX product. |
| ATP | **CHEBI:15422** | Principal phosphate donor for bacterial PPK1. |
| ADP | **CHEBI:16761** | Product of ATP-dependent polymerization; also regenerated from polyP by some PPK2 enzymes. |
| GTP/GDP and other nucleoside phosphates | CHEBI identifiers should be resolved individually | Relevant mainly to taxon- and class-specific PPK2 reactions. |
| calcium ion | **CHEBI:29108** | Common polyP-associated counterion. |
| magnesium ion | **CHEBI:18420** | Common counterion and enzymatic cofactor. |
| zinc, iron, sodium, potassium ions; polyamines | Resolve individually if used | Associated with granules in some taxa; not universal defining components. |
| poly(3-hydroxybutyrate), PHA | label or verified CHEBI entry | Nearby carbon-storage inclusion; useful as an explicit contrast node. |

PolyP may associate with Ca²⁺, Mg²⁺, Zn²⁺, Fe²⁺, Na⁺, K⁺, basic amino acids, and polyamines. This supports a generic “cation complexation” node but not a universal fixed granule stoichiometry (rao2009inorganicpolyphosphateessential pages 5-6, moreno2013polyphosphateandits pages 1-2).

### Genes, proteins, and complexes

| Candidate node | Suggested grounding | Role and qualification |
|---|---|---|
| polyphosphate kinase 1, PPK1 | **EC:2.7.4.1**; taxon-specific gene/UniProt entry | ATP-dependent polyP synthesis; principal curation-ready causal enzyme. |
| polyphosphate kinase 2, PPK2 | Resolve by class and taxon; do not collapse to PPK1 | Reversible polyP/nucleoside-phosphate metabolism; many PPK2s preferentially consume polyP. |
| exopolyphosphatase, PPX | **EC:3.6.1.11** | Progressive terminal hydrolysis of polyP to Pi. |
| Pst high-affinity phosphate transporter | GO/KEGG/UniProt entries after taxon resolution | Supplies phosphate under Pho-regulated conditions. |
| Pit low-affinity phosphate transporter | taxon-specific grounding | Perturbation affects polyP accumulation in *Ralstonia*. |
| PhoB response regulator / Pho regulon | taxon-specific grounding | Controls phosphate-acquisition response; evidence for granule effects is context-specific. |
| PhaX phosphate-transport regulator | label plus *Ralstonia* locus | Deletion derepresses phosphate acquisition and increases granules in *R. eutropha*. |
| CHAD-domain phosin | Pfam/InterPro or taxon-specific protein | PolyP-granule-associated protein; association is stronger than evidence for granule nucleation. |
| (p)ppGpp stringent-response machinery | gene-specific RelA/SpoT homologs | Interacts with polyP physiology, but pathway relationship differs among bacteria. |

PPK1 transfers terminal phosphate from ATP to polyP. By contrast, PPK2 enzymes frequently use polyP to phosphorylate nucleoside mono- or diphosphates; reported classes differ in substrate preference. PPX releases Pi progressively from chains with at least three phosphoanhydride bonds (corrales2025polyphosphatefromlactic pages 6-9).

### Processes, environmental factors, and locations

- Polyphosphate biosynthetic process — candidate **GO:0006797** (“polyphosphate metabolic process”; verify exact GO label/version).
- Polyphosphate catabolic process / PPX-mediated hydrolysis.
- Phosphate uptake and phosphate-starvation response.
- Phosphate refeeding or “polyP overplus” response.
- Nitrogen, carbon, amino-acid, or general nutrient starvation; encode the exact tested condition rather than a universal “starvation” node.
- Intracellular cation complexation and polymer condensation.
- Cytoplasm and nucleoid region; granules in *P. aeruginosa* form and organize within the nucleoid region (racki2017polyphosphategranulebiogenesis pages 1-3, racki2017polyphosphategranulebiogenesis pages 6-7).
- Acidocalcisome, only where organelle criteria are demonstrated.
- Cell-cycle exit, DNA-replication completion, stress survival, energy buffering.
- EBPR anaerobic phosphate release and aerobic/anoxic phosphate uptake.

### Taxa and ecological systems

- *Pseudomonas aeruginosa*: strongest time-resolved granule-biogenesis and cell-cycle evidence.
- *Ralstonia eutropha*/*Cupriavidus necator* H16: strong PPK knockout, phosphate-transport, and complementation evidence.
- *Synechocystis* sp. PCC 6803: recent metabolic-engineering and stress-trade-off evidence.
- “Candidatus *Accumulibacter phosphatis*”: major polyphosphate-accumulating organism in EBPR.
- *Tetrasphaera*: important alternative PAO in some wastewater systems.
- *Corynebacterium*, *Mycobacterium*, *Vibrio*, algae, yeasts, and protists: useful scope exemplars, but mechanisms should not automatically be transferred across lineages.

## 3. Candidate causal edges

The following table is the most concise shortlist of curation-ready relationships.

| subject | predicate | object | evidence strength/taxon | DOI |
|---|---|---|---|---|
| ATP + PPK1 | drives synthesis of | intracellular polyphosphate | Strong, enzyme-level; broad bacteria; “PPK1… ATP-dependent” (corrales2025polyphosphatefromlactic pages 6-9, tumlirsch2015formationofpolyphosphate pages 1-4) | https://doi.org/10.3390/foods14132211; https://doi.org/10.1128/AEM.02279-15 |
| Loss of key PPKs | abolishes formation of | polyphosphate granules | Strong, mutant evidence; *Ralstonia eutropha*; triple deletion eliminated granules (tumlirsch2015formationofpolyphosphate pages 12-15, tumlirsch2015formationofpolyphosphate pages 1-4) | https://doi.org/10.1128/AEM.02279-15 |
| Pho derepression / increased phosphate uptake | increases | polyphosphate granule accumulation | Strong, mutant + complementation; *Ralstonia eutropha* ΔphaX / pitA-linked effect (tumlirsch2015formationofpolyphosphate pages 12-15, tumlirsch2015formationofpolyphosphate pages 7-10) | https://doi.org/10.1128/AEM.02279-15 |
| Nitrogen starvation | induces | polyphosphate granule biogenesis | Strong, time-resolved imaging; *Pseudomonas aeruginosa*; granules appear by 1 h, consolidate by 3 h (racki2017polyphosphategranulebiogenesis pages 1-3, racki2017polyphosphategranulebiogenesis pages 3-4, racki2017polyphosphategranulebiogenesis pages 4-4) | https://doi.org/10.1073/pnas.1615575114 |
| Net polyphosphate granule synthesis | enables | cell-cycle exit during starvation | Strong, functional linkage; *Pseudomonas aeruginosa*; polyP mutants elongate and exit poorly (racki2017polyphosphategranulebiogenesis pages 6-7, racki2017polyphosphategranulebiogenesis pages 1-1, racki2017polyphosphategranulebiogenesis pages 7-8) | https://doi.org/10.1073/pnas.1615575114 |
| PPX exopolyphosphatase | hydrolyzes / releases Pi from | polyphosphate | Strong, canonical enzyme function; broad bacteria; progressive Pi release (corrales2025polyphosphatefromlactic pages 6-9) | https://doi.org/10.3390/foods14132211 |
| Divalent cations (e.g., Ca2+, Mg2+, Zn2+) | complex / condense | polyphosphate into granules | Moderate-strong, physicochemical + localization; broad taxa (rao2009inorganicpolyphosphateessential pages 5-6, moreno2013polyphosphateandits pages 1-2, schoeppe2024anupdateon pages 2-4) | https://doi.org/10.1146/annurev.biochem.77.083007.093039; https://doi.org/10.1371/journal.ppat.1003230; https://doi.org/10.3390/biom14080937 |
| Anaerobic EBPR phase | promotes breakdown of | polyP with phosphate release | Strong, process physiology; *Candidatus Accumulibacter* community context (camejo2016candidatusaccumulibacterphosphatis pages 6-6, camejo2016candidatusaccumulibacterphosphatis pages 6-8, camejo2016candidatusaccumulibacterphosphatis pages 1-2) | https://doi.org/10.1016/j.watres.2016.06.033 |
| Oxygen / nitrate / nitrite | support phosphate uptake and | polyP re-accumulation | Strong, rate data; *Candidatus Accumulibacter* EBPR; O2 6.6±1.8, NO3− 4.9±2.6, NO2− 1.5±0.6 mg P h−1 gVSS−1 (camejo2016candidatusaccumulibacterphosphatis pages 12-12, camejo2016candidatusaccumulibacterphosphatis pages 6-8, camejo2016candidatusaccumulibacterphosphatis pages 1-2) | https://doi.org/10.1016/j.watres.2016.06.033 |
| ppk deletion | increases lab productivity but causes | stress defects / loss of polyP accumulation | Strong, 2024 experimental; *Synechocystis* sp. PCC 6803; abolished polyP, faster growth, impaired stress survival, higher ethylene productivity (sebesta2024polyphosphatekinasedeletion pages 4-6, sebesta2024polyphosphatekinasedeletion pages 6-8, sebesta2024polyphosphatekinasedeletion pages 1-2) | https://doi.org/10.3389/fpls.2024.1342496 |


*Table: This table summarizes the strongest, most curation-ready causal edges for the polyphosphate granule trait, emphasizing direct mechanistic, mutant, and process-level evidence. It is useful as a compact shortlist of candidate TraitMech edges with taxon qualifiers and DOI-first sourcing.*

A more explicit triple set follows. Quoted text is intentionally short; notes state whether the edge can be generalized.

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| PPK1 + ATP | **catalyzes formation of** | intracellular polyP | DOI: [10.3390/foods14132211](https://doi.org/10.3390/foods14132211), June 2025: “Ppk1 catalyzes ATP-dependent polyP synthesis” (corrales2025polyphosphatefromlactic pages 6-9) | **Strong core edge.** The source is 2025 but synthesizes established enzymology. Granule formation additionally requires polymer condensation/localization. |
| *R. eutropha* PPK1a + PPK2c | **required for** | polyP-granule formation | DOI: [10.1128/AEM.02279-15](https://doi.org/10.1128/AEM.02279-15), December 2015: double/triple PPK deletion “completely eliminated polyP granule formation” (tumlirsch2015formationofpolyphosphate pages 12-15, tumlirsch2015formationofpolyphosphate pages 1-4) | **Strong mutant edge; taxon-specific paralog structure.** Do not infer that every organism requires both families. |
| deletion of `ppk` | **abolishes** | phosphate-refeeding-induced polyP accumulation | DOI: [10.3389/fpls.2024.1342496](https://doi.org/10.3389/fpls.2024.1342496), February 2024: accumulation was “completely abolished” in Δ`ppk`, whereas wild type accumulated polyP within 1 h (sebesta2024polyphosphatekinasedeletion pages 4-6) | **Strong, recent, taxon-specific** to *Synechocystis* PCC 6803; DAPI-based biochemical assay rather than ultrastructural granule quantification. |
| PPX | **hydrolyzes** | polyP to orthophosphate | DOI: [10.3390/foods14132211](https://doi.org/10.3390/foods14132211), June 2025: PPX “progressively releas[es] inorganic phosphate” (corrales2025polyphosphatefromlactic pages 6-9) | **Strong enzyme edge.** Use “decreases polyP/granule material” only when an in-vivo perturbation establishes that morphological outcome. |
| loss of PhaX / Pho-pathway derepression | **increases** | phosphate acquisition and polyP granules | DOI: [10.1128/AEM.02279-15](https://doi.org/10.1128/AEM.02279-15), December 2015: phosphatase, PhoB and PstS rose 53-, 48- and 33-fold; complementation restored normal polyP (tumlirsch2015formationofpolyphosphate pages 12-15, tumlirsch2015formationofpolyphosphate pages 7-10) | **Strong mutant plus complementation evidence**, but PhaX is *Ralstonia*-specific and the direction of Pho effects should not be generalized unqualified. |
| nitrogen starvation | **induces** | nascent polyP granules | DOI: [10.1073/pnas.1615575114](https://doi.org/10.1073/pnas.1615575114), March 2017: microgranules appeared by 1 h and consolidated by 3 h (racki2017polyphosphategranulebiogenesis pages 1-3, racki2017polyphosphategranulebiogenesis pages 3-4) | **Strong time-resolved edge in *P. aeruginosa*.** Encode nitrogen starvation specifically. Other nutrient limitations require separate evidence. |
| granule consolidation | **decreases number while increasing size of** | polyP granules | Same DOI: granule number fell from 13 to 5 while total volume rose more than tenfold; large granules were 200±50 nm and satellites 59±20 nm (racki2017polyphosphategranulebiogenesis pages 4-4) | **Strong morphology edge.** Represents maturation rather than degradation. |
| polyP synthesis / granule biogenesis | **promotes** | completion of cell-cycle exit during starvation | Same DOI: ΔpolyP cells elongated and completed fewer divisions; either PPK1 or PPK2A could support exit (racki2017polyphosphategranulebiogenesis pages 6-7, racki2017polyphosphategranulebiogenesis pages 1-1) | **Strong functional edge in *P. aeruginosa*.** The immediate molecular mediator remains unresolved, so do not assert a direct physical mechanism. |
| polyP and (p)ppGpp | **act additively to promote** | starvation cell-cycle exit | Same DOI: the double mutant showed greater impairment, while (p)ppGpp was not required for polyP synthesis in this species (racki2017polyphosphategranulebiogenesis pages 7-8) | **Taxon-specific.** This explicitly conflicts with simple universal models derived from *E. coli*. |
| Ca²⁺/Mg²⁺ and other counterions | **complex with / promote condensation of** | polyP | DOI: [10.1146/annurev.biochem.77.083007.093039](https://doi.org/10.1146/annurev.biochem.77.083007.093039), June 2009; DOI: [10.3390/biom14080937](https://doi.org/10.3390/biom14080937), August 2024: polyP complexes divalent cations and Ca-polyP nanoparticles aggregate (rao2009inorganicpolyphosphateessential pages 5-6, schoeppe2024anupdateon pages 2-4) | **Moderate mechanistic edge.** “Required for granule formation” is stronger than the available organism-level causal evidence. |
| CHAD-domain phosins | **associate with** | polyP granules | DOI: [10.3390/biom14080937](https://doi.org/10.3390/biom14080937), August 2024: CHAD proteins are “attached to polyphosphate granules in vivo” (schoeppe2024anupdateon pages 15-16) | **Curate association/localization**, not “nucleates granule formation,” absent a loss-of-function phenotype. |
| anaerobic EBPR phase | **promotes consumption of** | intracellular polyP with Pi release | DOI: [10.1016/j.watres.2016.06.033](https://doi.org/10.1016/j.watres.2016.06.033), October 2016: reactor profiles showed anaerobic phosphate release followed by microaerobic uptake (camejo2016candidatusaccumulibacterphosphatis pages 6-6, camejo2016candidatusaccumulibacterphosphatis pages 6-8) | **Strong process-level edge** for PAO communities; molecular enzyme attribution was not isolated in this experiment. |
| O₂, nitrate, or nitrite | **supports** | phosphate uptake/polyP re-accumulation | Same DOI: uptake rates were 6.6±1.8, 4.9±2.6, and 1.5±0.6 mg P h⁻¹ gVSS⁻¹, respectively; none occurred without an electron acceptor (camejo2016candidatusaccumulibacterphosphatis pages 6-8) | **Strong reactor evidence** for enriched *Accumulibacter* communities. Keep electron acceptors and measured rates separate. |
| loss of polyP synthesis | **increases under controlled conditions** | ATP/energy charge and early growth | DOI: [10.3389/fpls.2024.1342496](https://doi.org/10.3389/fpls.2024.1342496), February 2024: Δ`ppk` growth rose 166% mixotrophically, 32% at low light, and 26% at high light (5.26 versus 4.18 d⁻¹) (sebesta2024polyphosphatekinasedeletion pages 4-6) | **Strong but conditional.** At 24 h, energy charge was lower despite faster growth, so a sustained ATP-mediated mechanism is not established. |
| loss of polyP synthesis | **reduces** | environmental stress tolerance | Same DOI: Δ`ppk` stopped growing by day 4 at pH 6.5 and failed to grow in natural creek water or low inorganic carbon (sebesta2024polyphosphatekinasedeletion pages 6-8) | **Strong for *Synechocystis***; not a universal quantitative stress-survival edge. |

## 4. Current understanding and recent developments

### Granule biogenesis is an organized cellular process

The strongest direct morphology study shows that granules do not simply precipitate randomly. In nitrogen-starved *P. aeruginosa*, small granules first appear throughout the nucleoid, then consolidate into regularly spaced bodies. The first two granules occurred at normalized cell-axis positions 0.32±0.06 and 0.68±0.08, at least 0.3 μm from poles and 0.2 μm apart (racki2017polyphosphategranulebiogenesis pages 6-7). This supports graph nodes for **nucleoid-region localization**, **microgranule nucleation**, and **granule consolidation**, although the molecular machinery that determines spacing remains unresolved.

### PPK family names do not imply identical causal direction

PPK1 is generally the principal ATP-driven polymerizing enzyme. PPK2 is more heterogeneous and often preferentially consumes polyP to regenerate nucleoside triphosphates; one synthesis reports an approximately 75-fold preference for degradation over synthesis for a characterized PPK2 context (corrales2025polyphosphatefromlactic pages 6-9). Consequently, a graph edge `PPK2 -> polyP granule formation` must carry the exact paralog, organism, and experimental direction. The *P. aeruginosa* and *Ralstonia* results establish that particular PPK2 paralogs can support granule formation, not that all PPK2 proteins are biosynthetic.

### PolyP is both a reserve and a conditional energy-management system

The 2024 *Synechocystis* work provides a useful causal trade-off: eliminating `ppk` prevented polyP accumulation and diverted resources toward faster laboratory growth and 40–46% greater culture-level ethylene productivity, but impaired growth under acidic, natural-water, and low-carbon conditions. Increased ethylene output reflected faster biomass accumulation rather than greater per-cell productivity (sebesta2024polyphosphatekinasedeletion pages 4-6, sebesta2024polyphosphatekinasedeletion pages 6-8). This supports a reserve/buffering interpretation while warning against a simplistic edge such as `polyP granule -> always increases growth`.

### Expert interpretation

Authoritative reviews describe polyP as a phosphate and energy reservoir with roles in stress physiology, metal binding, regulation, and chaperoning. Nevertheless, the strongest curation strategy is to separate **well-established polymer chemistry and storage** from pleiotropic organism-level outcomes (rao2009inorganicpolyphosphateessential pages 5-6, schoeppe2024anupdateon pages 2-4). Stress survival, virulence, biofilm formation, motility, and cell-cycle control should each be represented only with taxon- and condition-specific perturbation evidence.

## 5. Applications and real-world implementation

### Enhanced biological phosphorus removal

EBPR intentionally enriches polyphosphate-accumulating organisms by alternating redox and substrate conditions. In a representative *Accumulibacter*-enriched system, anaerobic phosphate release was followed by oxygen-, nitrate-, or nitrite-dependent phosphate uptake. Full-scale PAOs were reported as approximately 5–25% of the microbial community, while enriched laboratory reactors contained >70% PAOs in some regimes; *Tetrasphaera* can dominate certain plants (camejo2016candidatusaccumulibacterphosphatis pages 6-8). A pilot process achieved 91±15% phosphorus removal and 42±15% nitrogen removal (camejo2016candidatusaccumulibacterphosphatis pages 6-8). These results make EBPR the clearest mature implementation of microbial polyP-granule cycling.

### Phosphorus recovery and environmental biotechnology

PolyP-rich biomass concentrates dissolved phosphorus and can be separated or processed for recovery. However, recovery as struvite, apatite, or another mineral occurs downstream of or alongside biological accumulation; those minerals must not be modeled as identical to intracellular polyP granules. Recent phosphorus-removal reviews continue to position biological accumulation as one component of integrated recovery systems, while chemical precipitation remains a distinct mechanism.

### Metabolic engineering and biocontainment

The 2024 *Synechocystis* study suggests `ppk` deletion as a laboratory-productivity and potential biocontainment strategy: engineered cells can grow faster under controlled, carbon-rich cultivation yet perform poorly under environmental stress. The result is promising but currently organism- and process-specific, not a broadly validated industrial rule (sebesta2024polyphosphatekinasedeletion pages 6-8, sebesta2024polyphosphatekinasedeletion pages 1-2).

### Imaging and community phenotyping

DAPI/tetracycline labeling, Raman microscopy, flow cytometry, TEM, and polyP-binding domains are used to identify PAOs and monitor intracellular storage in mixed wastewater communities. Because many probes are not perfectly specific, reliable implementation increasingly combines imaging with Raman spectra, elemental analysis, biochemical extraction, or genetic validation (omelon2013areviewof pages 6-8, schoeppe2024anupdateon pages 15-16, schoeppe2024anupdateon pages 16-17).

## 6. Recommended minimal graph extension

For a conservative first revision of `polyphosphate_granule_storage`, the existing seven-node graph could be expanded around this core:

1. `extracellular_phosphate` — **transported_into_cell_by** → `Pst/Pit phosphate transport system`
2. `Pst/Pit phosphate transport system` — **increases_availability_of** → `intracellular_orthophosphate`
3. `ATP` — **phosphate_donor_for** → `PPK1`
4. `PPK1` — **catalyzes_synthesis_of** → `inorganic_polyphosphate`
5. `divalent_cations` — **complex_with** → `inorganic_polyphosphate`
6. `inorganic_polyphosphate` — **assembles_into** → `polyphosphate_granule`
7. `PPX` — **degrades** → `inorganic_polyphosphate`
8. `PPX-mediated_polyP_hydrolysis` — **releases** → `orthophosphate`
9. `nitrogen_starvation` — **induces_in_P._aeruginosa** → `polyphosphate_granule_biogenesis`
10. `polyphosphate_granule_biogenesis` — **promotes_in_P._aeruginosa** → `starvation_cell-cycle_exit`
11. `anaerobic_EBPR_phase` — **promotes** → `polyP_consumption_and_phosphate_release`
12. `aerobic_or_anoxic_EBPR_phase` — **promotes** → `phosphate_uptake_and_polyP_reaccumulation`

Edges 1–8 capture the generic storage mechanism. Edges 9–12 should carry taxon or process qualifiers and should not be inherited automatically by every organism annotated with the trait.

## 7. Warnings: claims not ready for unqualified TraitMech curation

1. **All polyP granules are acidocalcisomes.** Membrane delimitation and acidification are not universal; curate only with direct organelle evidence.
2. **All PPK2 proteins synthesize polyP.** Reaction bias and nucleoside specificity vary by PPK2 class and paralog.
3. **The Pho response universally increases granules.** The strong transport-regulatory result is from *R. eutropha*; other taxa and phosphate states may differ.
4. **(p)ppGpp is universally upstream of polyP accumulation.** It was dispensable for starvation-induced synthesis in *P. aeruginosa*, despite different relationships reported in *E. coli* (racki2017polyphosphategranulebiogenesis pages 7-8).
5. **DAPI-positive puncta prove polyP granules.** Use orthogonal chemical or genetic controls.
6. **Every phosphorus-rich inclusion is polyP.** Apatite, struvite, and other minerals are major confounders.
7. **Granules necessarily improve growth.** They support stress resilience in some contexts but can reduce controlled-laboratory productivity through resource or energy allocation.
8. **PolyP directly causes cell-cycle exit through a known molecular target.** The phenotype is causal at the pathway level, but the immediate target remains unresolved.
9. **Phosins nucleate granules.** Current evidence robustly supports granule association; nucleation or structural necessity needs knockout/complementation evidence.
10. **Granule presence is diagnostic of pathogenicity.** Volutin granules occur in pathogens and nonpathogens, including *Corynebacterium glutamicum* and *Vibrio cholerae* (rao2009inorganicpolyphosphateessential pages 4-5).

## 8. DOI-first bibliography

- **Schoeppe R, Waldmann M, Jessen HJ, Renné T.** “An Update on Polyphosphate In Vivo Activities.” *Biomolecules* 14:937. **August 2024.** DOI: [10.3390/biom14080937](https://doi.org/10.3390/biom14080937). Recent authoritative review of polyP chemistry, physiology, granule-associated proteins, and analytical methods (schoeppe2024anupdateon pages 2-4, schoeppe2024anupdateon pages 15-16).
- **Sebesta J et al.** “Polyphosphate kinase deletion increases laboratory productivity in cyanobacteria.” *Frontiers in Plant Science* 15. **February 2024.** DOI: [10.3389/fpls.2024.1342496](https://doi.org/10.3389/fpls.2024.1342496). Recent knockout study linking polyP synthesis to energy allocation, stress tolerance, productivity, and biocontainment (sebesta2024polyphosphatekinasedeletion pages 4-6, sebesta2024polyphosphatekinasedeletion pages 6-8).
- **Racki LR et al.** “Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in *Pseudomonas aeruginosa*.” *PNAS* 114:E2440–E2449. **March 2017.** DOI: [10.1073/pnas.1615575114](https://doi.org/10.1073/pnas.1615575114). Best direct time-resolved study of bacterial granule biogenesis and spatial organization (racki2017polyphosphategranulebiogenesis pages 1-1, racki2017polyphosphategranulebiogenesis pages 4-4).
- **Camejo PY et al.** “*Candidatus Accumulibacter phosphatis* clades enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors.” *Water Research* 102:125–137. **October 2016.** DOI: [10.1016/j.watres.2016.06.033](https://doi.org/10.1016/j.watres.2016.06.033). Reactor-scale evidence for EBPR redox cycling and electron-acceptor-dependent phosphate uptake (camejo2016candidatusaccumulibacterphosphatis pages 6-6, camejo2016candidatusaccumulibacterphosphatis pages 6-8).
- **Tumlirsch T, Sznajder A, Jendrossek D.** “Formation of Polyphosphate by Polyphosphate Kinases and Its Relationship to Poly(3-Hydroxybutyrate) Accumulation in *Ralstonia eutropha* H16.” *Applied and Environmental Microbiology* 81:8277–8293. **December 2015.** DOI: [10.1128/AEM.02279-15](https://doi.org/10.1128/AEM.02279-15). Strong deletion/complementation evidence for PPKs and phosphate-transport regulation (tumlirsch2015formationofpolyphosphate pages 12-15, tumlirsch2015formationofpolyphosphate pages 7-10).
- **Moreno SNJ, Docampo R.** “Polyphosphate and Its Diverse Functions in Host Cells and Pathogens.” *PLoS Pathogens* 9:e1003230. **May 2013.** DOI: [10.1371/journal.ppat.1003230](https://doi.org/10.1371/journal.ppat.1003230). Useful source for polymer chemistry, associated cations, chain-length conventions, and compartmentalization (moreno2013polyphosphateandits pages 1-2).
- **Omelon S et al.** “A Review of Phosphate Mineral Nucleation in Biology and Geobiology.” *Calcified Tissue International* 93:382–396. **September 2013.** DOI: [10.1007/s00223-013-9784-9](https://doi.org/10.1007/s00223-013-9784-9). Supports granule dimensions, elemental analysis, and distinction from apatite (omelon2013areviewof pages 6-8).
- **Rao NN, Gómez-García MR, Kornberg A.** “Inorganic polyphosphate: essential for growth and survival.” *Annual Review of Biochemistry* 78:605–647. **June 2009.** DOI: [10.1146/annurev.biochem.77.083007.093039](https://doi.org/10.1146/annurev.biochem.77.083007.093039). Foundational authoritative review of polyP granules, enzymes, storage, and survival (rao2009inorganicpolyphosphateessential pages 5-6, rao2009inorganicpolyphosphateessential pages 4-5).
- **Kornberg A, Rao NN, Ault-Riché D.** “Inorganic polyphosphate: a molecule of many functions.” *Annual Review of Biochemistry* 68:89–125. **November 1999 online record / volume 1999**. DOI: [10.1146/annurev.biochem.68.1.89](https://doi.org/10.1146/annurev.biochem.68.1.89). Foundational source for metachromasy and classical granule terminology (kornberg2003inorganicpolyphosphatea pages 2-4).

**Overall curation judgment:** the generic causal core—phosphate acquisition, ATP-dependent PPK1 synthesis, cation-associated condensation into an intracellular inclusion, and PPX-mediated mobilization—is ready for TraitMech. Starvation signaling, spatial organization, cell-cycle effects, PPK2 contributions, stress survival, and EBPR cycling are valuable extensions but require explicit taxon, environmental, or process qualifiers.

References

1. (moreno2013polyphosphateandits pages 1-2): Silvia N. J. Moreno and Roberto Docampo. Polyphosphate and its diverse functions in host cells and pathogens. PLoS Pathogens, 9:e1003230, May 2013. URL: https://doi.org/10.1371/journal.ppat.1003230, doi:10.1371/journal.ppat.1003230. This article has 121 citations and is from a highest quality peer-reviewed journal.

2. (schoeppe2024anupdateon pages 2-4): Robert Schoeppe, Moritz Waldmann, Henning J. Jessen, and Thomas Renné. An update on polyphosphate in vivo activities. Biomolecules, 14:937, Aug 2024. URL: https://doi.org/10.3390/biom14080937, doi:10.3390/biom14080937. This article has 18 citations.

3. (omelon2013areviewof pages 6-8): Sidney Omelon, Marianne Ariganello, Ermanno Bonucci, Marc Grynpas, and Antonio Nanci. A review of phosphate mineral nucleation in biology and geobiology. Calcified Tissue International, 93:382-396, Sep 2013. URL: https://doi.org/10.1007/s00223-013-9784-9, doi:10.1007/s00223-013-9784-9. This article has 110 citations and is from a peer-reviewed journal.

4. (racki2017polyphosphategranulebiogenesis pages 1-1): Lisa R. Racki, Elitza I. Tocheva, Michael G. Dieterle, Meaghan C. Sullivan, Grant J. Jensen, and Dianne K. Newman. Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences, 114:E2440-E2449, Mar 2017. URL: https://doi.org/10.1073/pnas.1615575114, doi:10.1073/pnas.1615575114. This article has 152 citations and is from a highest quality peer-reviewed journal.

5. (kornberg2003inorganicpolyphosphatea pages 2-4): Arthur Kornberg, Narayana N. Rao, and Dana Ault-Riché. Inorganic polyphosphate: a molecule of many functions. Annual review of biochemistry, 68:89-125, Nov 2003. URL: https://doi.org/10.1146/annurev.biochem.68.1.89, doi:10.1146/annurev.biochem.68.1.89. This article has 1550 citations and is from a domain leading peer-reviewed journal.

6. (rao2009inorganicpolyphosphateessential pages 4-5): Narayana N. Rao, María R. Gómez-García, and Arthur Kornberg. Inorganic polyphosphate: essential for growth and survival. Annual review of biochemistry, 78:605-47, Jun 2009. URL: https://doi.org/10.1146/annurev.biochem.77.083007.093039, doi:10.1146/annurev.biochem.77.083007.093039. This article has 986 citations and is from a domain leading peer-reviewed journal.

7. (schoeppe2024anupdateon pages 15-16): Robert Schoeppe, Moritz Waldmann, Henning J. Jessen, and Thomas Renné. An update on polyphosphate in vivo activities. Biomolecules, 14:937, Aug 2024. URL: https://doi.org/10.3390/biom14080937, doi:10.3390/biom14080937. This article has 18 citations.

8. (rao2009inorganicpolyphosphateessential pages 5-6): Narayana N. Rao, María R. Gómez-García, and Arthur Kornberg. Inorganic polyphosphate: essential for growth and survival. Annual review of biochemistry, 78:605-47, Jun 2009. URL: https://doi.org/10.1146/annurev.biochem.77.083007.093039, doi:10.1146/annurev.biochem.77.083007.093039. This article has 986 citations and is from a domain leading peer-reviewed journal.

9. (racki2017polyphosphategranulebiogenesis pages 1-3): Lisa R. Racki, Elitza I. Tocheva, Michael G. Dieterle, Meaghan C. Sullivan, Grant J. Jensen, and Dianne K. Newman. Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences, 114:E2440-E2449, Mar 2017. URL: https://doi.org/10.1073/pnas.1615575114, doi:10.1073/pnas.1615575114. This article has 152 citations and is from a highest quality peer-reviewed journal.

10. (corrales2025polyphosphatefromlactic pages 6-9): Daniela Corrales, Cristina Alcántara, Vicente Monedero, and Manuel Zúñiga. Polyphosphate from lactic acid bacteria: a functional molecule for food and health applications. Foods, 14:2211, Jun 2025. URL: https://doi.org/10.3390/foods14132211, doi:10.3390/foods14132211. This article has 3 citations.

11. (racki2017polyphosphategranulebiogenesis pages 6-7): Lisa R. Racki, Elitza I. Tocheva, Michael G. Dieterle, Meaghan C. Sullivan, Grant J. Jensen, and Dianne K. Newman. Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences, 114:E2440-E2449, Mar 2017. URL: https://doi.org/10.1073/pnas.1615575114, doi:10.1073/pnas.1615575114. This article has 152 citations and is from a highest quality peer-reviewed journal.

12. (tumlirsch2015formationofpolyphosphate pages 1-4): Tony Tumlirsch, Anna Sznajder, and Dieter Jendrossek. Formation of polyphosphate by polyphosphate kinases and its relationship to poly(3-hydroxybutyrate) accumulation in ralstonia eutropha strain h16. Applied and Environmental Microbiology, 81:8277-8293, Dec 2015. URL: https://doi.org/10.1128/aem.02279-15, doi:10.1128/aem.02279-15. This article has 41 citations and is from a peer-reviewed journal.

13. (tumlirsch2015formationofpolyphosphate pages 12-15): Tony Tumlirsch, Anna Sznajder, and Dieter Jendrossek. Formation of polyphosphate by polyphosphate kinases and its relationship to poly(3-hydroxybutyrate) accumulation in ralstonia eutropha strain h16. Applied and Environmental Microbiology, 81:8277-8293, Dec 2015. URL: https://doi.org/10.1128/aem.02279-15, doi:10.1128/aem.02279-15. This article has 41 citations and is from a peer-reviewed journal.

14. (tumlirsch2015formationofpolyphosphate pages 7-10): Tony Tumlirsch, Anna Sznajder, and Dieter Jendrossek. Formation of polyphosphate by polyphosphate kinases and its relationship to poly(3-hydroxybutyrate) accumulation in ralstonia eutropha strain h16. Applied and Environmental Microbiology, 81:8277-8293, Dec 2015. URL: https://doi.org/10.1128/aem.02279-15, doi:10.1128/aem.02279-15. This article has 41 citations and is from a peer-reviewed journal.

15. (racki2017polyphosphategranulebiogenesis pages 3-4): Lisa R. Racki, Elitza I. Tocheva, Michael G. Dieterle, Meaghan C. Sullivan, Grant J. Jensen, and Dianne K. Newman. Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences, 114:E2440-E2449, Mar 2017. URL: https://doi.org/10.1073/pnas.1615575114, doi:10.1073/pnas.1615575114. This article has 152 citations and is from a highest quality peer-reviewed journal.

16. (racki2017polyphosphategranulebiogenesis pages 4-4): Lisa R. Racki, Elitza I. Tocheva, Michael G. Dieterle, Meaghan C. Sullivan, Grant J. Jensen, and Dianne K. Newman. Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences, 114:E2440-E2449, Mar 2017. URL: https://doi.org/10.1073/pnas.1615575114, doi:10.1073/pnas.1615575114. This article has 152 citations and is from a highest quality peer-reviewed journal.

17. (racki2017polyphosphategranulebiogenesis pages 7-8): Lisa R. Racki, Elitza I. Tocheva, Michael G. Dieterle, Meaghan C. Sullivan, Grant J. Jensen, and Dianne K. Newman. Polyphosphate granule biogenesis is temporally and functionally tied to cell cycle exit during starvation in pseudomonas aeruginosa. Proceedings of the National Academy of Sciences, 114:E2440-E2449, Mar 2017. URL: https://doi.org/10.1073/pnas.1615575114, doi:10.1073/pnas.1615575114. This article has 152 citations and is from a highest quality peer-reviewed journal.

18. (camejo2016candidatusaccumulibacterphosphatis pages 6-6): Pamela Y. Camejo, Brian R. Owen, Joseph Martirano, Juan Ma, Vikram Kapoor, Jorge Santo Domingo, Katherine D. McMahon, and Daniel R. Noguera. Candidatus accumulibacter phosphatis clades enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors. Water research, 102:125-137, Oct 2016. URL: https://doi.org/10.1016/j.watres.2016.06.033, doi:10.1016/j.watres.2016.06.033. This article has 138 citations and is from a highest quality peer-reviewed journal.

19. (camejo2016candidatusaccumulibacterphosphatis pages 6-8): Pamela Y. Camejo, Brian R. Owen, Joseph Martirano, Juan Ma, Vikram Kapoor, Jorge Santo Domingo, Katherine D. McMahon, and Daniel R. Noguera. Candidatus accumulibacter phosphatis clades enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors. Water research, 102:125-137, Oct 2016. URL: https://doi.org/10.1016/j.watres.2016.06.033, doi:10.1016/j.watres.2016.06.033. This article has 138 citations and is from a highest quality peer-reviewed journal.

20. (camejo2016candidatusaccumulibacterphosphatis pages 1-2): Pamela Y. Camejo, Brian R. Owen, Joseph Martirano, Juan Ma, Vikram Kapoor, Jorge Santo Domingo, Katherine D. McMahon, and Daniel R. Noguera. Candidatus accumulibacter phosphatis clades enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors. Water research, 102:125-137, Oct 2016. URL: https://doi.org/10.1016/j.watres.2016.06.033, doi:10.1016/j.watres.2016.06.033. This article has 138 citations and is from a highest quality peer-reviewed journal.

21. (camejo2016candidatusaccumulibacterphosphatis pages 12-12): Pamela Y. Camejo, Brian R. Owen, Joseph Martirano, Juan Ma, Vikram Kapoor, Jorge Santo Domingo, Katherine D. McMahon, and Daniel R. Noguera. Candidatus accumulibacter phosphatis clades enriched under cyclic anaerobic and microaerobic conditions simultaneously use different electron acceptors. Water research, 102:125-137, Oct 2016. URL: https://doi.org/10.1016/j.watres.2016.06.033, doi:10.1016/j.watres.2016.06.033. This article has 138 citations and is from a highest quality peer-reviewed journal.

22. (sebesta2024polyphosphatekinasedeletion pages 4-6): Jacob Sebesta, Michael Cantrell, Eric Schaedig, Harvey J. M. Hou, Colleen Pastore, Katherine J. Chou, Wei Xiong, Michael T. Guarnieri, and Jianping Yu. Polyphosphate kinase deletion increases laboratory productivity in cyanobacteria. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1342496, doi:10.3389/fpls.2024.1342496. This article has 11 citations.

23. (sebesta2024polyphosphatekinasedeletion pages 6-8): Jacob Sebesta, Michael Cantrell, Eric Schaedig, Harvey J. M. Hou, Colleen Pastore, Katherine J. Chou, Wei Xiong, Michael T. Guarnieri, and Jianping Yu. Polyphosphate kinase deletion increases laboratory productivity in cyanobacteria. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1342496, doi:10.3389/fpls.2024.1342496. This article has 11 citations.

24. (sebesta2024polyphosphatekinasedeletion pages 1-2): Jacob Sebesta, Michael Cantrell, Eric Schaedig, Harvey J. M. Hou, Colleen Pastore, Katherine J. Chou, Wei Xiong, Michael T. Guarnieri, and Jianping Yu. Polyphosphate kinase deletion increases laboratory productivity in cyanobacteria. Frontiers in Plant Science, Feb 2024. URL: https://doi.org/10.3389/fpls.2024.1342496, doi:10.3389/fpls.2024.1342496. This article has 11 citations.

25. (schoeppe2024anupdateon pages 16-17): Robert Schoeppe, Moritz Waldmann, Henning J. Jessen, and Thomas Renné. An update on polyphosphate in vivo activities. Biomolecules, 14:937, Aug 2024. URL: https://doi.org/10.3390/biom14080937, doi:10.3390/biom14080937. This article has 18 citations.