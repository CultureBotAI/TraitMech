---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:33:38.920787'
end_time: '2026-08-04T04:41:17.795510'
duration_seconds: 458.87
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: xerophilic
  trait_identifier: traitmech:000011
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: xerophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental growth preference in which an organism grows at low
    water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
  parent_traits: METPO:1000059
  synonyms: xerotolerant
  evidence_summary: 'DOI:10.1098/rstb.2004.1502: some of which are capable of growth
    at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date
    (Low-water-activity review supports growth at very low aw as the defining feature
    of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life
    without water) is predominantly described as the ability of some organisms to
    lose all or almost all water and enter a state of suspension where the metabolism
    comes to a reversible standstill (Anhydrobiosis review supports low-water-activity
    adaptation as the physiological context distinguishing xerophilic growth from
    desiccation survival.)'
  causal_graph_summary: 'xerophilic_low_water_activity_growth: 8 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** xerophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000011
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows at low water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
- **Parent traits:** METPO:1000059
- **Synonyms:** xerotolerant
- **Existing evidence:** DOI:10.1098/rstb.2004.1502: some of which are capable of growth at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date (Low-water-activity review supports growth at very low aw as the defining feature of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Anhydrobiosis review supports low-water-activity adaptation as the physiological context distinguishing xerophilic growth from desiccation survival.)
- **Existing causal graph summary:** xerophilic_low_water_activity_growth: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **xerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/xerophilic.yaml`.

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
- **Trait label:** xerophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000011
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows at low water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
- **Parent traits:** METPO:1000059
- **Synonyms:** xerotolerant
- **Existing evidence:** DOI:10.1098/rstb.2004.1502: some of which are capable of growth at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date (Low-water-activity review supports growth at very low aw as the defining feature of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Anhydrobiosis review supports low-water-activity adaptation as the physiological context distinguishing xerophilic growth from desiccation survival.)
- **Existing causal graph summary:** xerophilic_low_water_activity_growth: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **xerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/xerophilic.yaml`.

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


# TraitMech curation report: xerophilic

**Trait:** `traitmech:000011`  
**Category:** ENVIRONMENT · **Kind:** CLASS · **Mapping:** REVIEWED  
**Parent:** `METPO:1000059`  
**Preferred label:** xerophilic  
**Synonym supplied:** xerotolerant

## 1. Scope and current understanding

### Recommended scope

For TraitMech, **xerophilic** should mean the demonstrated capacity or preference for **active microbial growth at reduced water activity (aw)**, including germination, cell division, biomass increase, or colony extension in low-aw media or substrates. Reduced aw may be produced by desiccation, concentrated sugars/polyols, salts, or other solutes, but aw—not solute concentration alone—is the defining environmental variable.

A recent authoritative review uses **≤0.80 aw** as an operational threshold for xerophilic fungi, refining an older ≤0.85 criterion. This is a useful annotation convention, not a universal biological discontinuity. The same review reports *Aspergillus penicillioides* cell division at **0.585 aw**, a theoretical germination minimum near **0.565 aw**, and theoretical growth limits of approximately **0.632–0.636 aw** for *A. penicillioides* and *Xeromyces bisporus*. All 32 examined species in *Aspergillus* section *Aspergillus* and 22 in section *Restricti* reportedly grew on 60% sucrose medium (1.75 M), illustrating the trait's strong enrichment in these lineages. (pocsi2024biotechnologicalpotentialof pages 2-5, pocsi2024biotechnologicalpotentialof pages 1-2)

### Boundaries

- **Xerophily versus xerotolerance:** Strict usage reserves *xerophile* for organisms that prefer or require low aw and *xerotolerant* for organisms that merely tolerate it. Because the supplied synonym collapses these concepts, the graph should encode the assay-observed endpoint and aw rather than infer preference from survival alone.
- **Growth versus desiccation survival/anhydrobiosis:** Viability after drying, metabolic arrest, or recovery after rehydration is insufficient. Curate only evidence of growth, germination, or division under low aw. Lag phase alone is unreliable: it can vary independently of exponential growth rate under low-aw and other stresses. (hamill2020microbiallagphase pages 3-4)
- **Xerophily versus osmophily:** Osmophily is preference or requirement for high osmotic pressure, often generated by sugars. It overlaps mechanistically with xerophily but is defined by the osmotic environment rather than aw itself.
- **Xerophily versus halophily:** Halophily requires or prefers salt; salt also lowers aw but adds ion-specific toxicity and ion-homeostasis requirements. For example, *Wallemia ichthyophaga* is an obligate halophile growing at 10–32% NaCl and aw 0.959–0.771, whereas low aw can also be generated by nonionic glycerol or sucrose. Therefore, salt-response edges should be annotated as supporting mechanisms under a particular low-aw regime, not universal xerophily mechanisms. (zajc2014osmoadaptationstrategyof pages 1-2, pocsi2024biotechnologicalpotentialof pages 2-5)
- **Germination versus sustained growth:** Germ-tube emergence or cell division at 0.585 aw is compelling phenotypic evidence, but should not automatically be represented as sustained population growth unless the assay measured it.
- **Solute-specific effects:** Below approximately 5 M, glycerol stress is dominated by aw reduction; above 5 M, glycerol chaotropicity can become limiting. Thus, equal aw values produced by different solutes need not be physiologically equivalent. (hamill2020microbiallagphase pages 3-4)

## 2. Candidate graph nodes

### Trait and environmental/experimental nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| xerophilic | `traitmech:000011` | Target trait; quote identifier verbatim in YAML. |
| reduced water activity / low aw | Label only | Record numerical aw and method/solute whenever possible. |
| high osmolarity / hyperosmotic stress | `GO:0006970` (response to osmotic stress), where used as a process | Not identical to low aw; retain environmental context separately. |
| high salinity / NaCl stress | Label only | Taxon- and ion-specific low-aw condition. |
| sugar-rich substrate | Label only | Examples include 60% sucrose media and dried/sugared foods. |
| glycerol-supplemented medium | Label only | Both lowers aw and becomes chaotropic at very high concentration. |
| desiccated substrate | Label only | Do not equate desiccation survival with xerophilic growth. |
| temperature | Label only | Important covariate in growth and mycotoxin assays. |
| active growth | `GO:0040007` (growth) | Prefer direct biomass/colony-extension evidence. |
| cell division | `GO:0051301` | Strong low-aw phenotype endpoint. |
| conidial germination | `GO:0009847` may apply in appropriate fungal annotation | Verify applicability to the specific organism and assay. |

### Chemicals and metabolites

| Candidate node | Suggested grounding | Role |
|---|---|---|
| glycerol | `CHEBI:17754` | Principal compatible solute in several low-aw/salt-adapted fungi. |
| trehalose | `CHEBI:27082` | Compatible solute or stress protectant; response is condition- and taxon-dependent. |
| D-mannitol | `CHEBI:16899` | Secondary/stage-dependent polyol. |
| erythritol | `CHEBI:17113` | Compatible polyol in some fungi. |
| arabitol | Label only unless stereochemistry is established | Secondary compatible solute; avoid an unjustified stereospecific CURIE. |
| sodium ion | `CHEBI:29101` | Ion-homeostasis substrate in saline low-aw conditions. |
| potassium ion | `CHEBI:29103` | Cytosolic ion balance. |
| sodium chloride | `CHEBI:26710` | Lowers aw but also produces ionic stress. |
| sucrose | `CHEBI:17992` | Common nonionic aw depressor and xerophile-selection substrate. |
| chitin | `CHEBI:17029` | Cell-wall polymer altered under salt/osmotic stress. |
| β-glucan | Label only | Cell-wall cross-linking and architecture; exact polymer should be specified if known. |
| sterols and sphingolipids | Label only | Membrane-remodeling module; molecular species generally unresolved in current evidence. |

### Genes, proteins, pathways, and cellular processes

| Candidate node | Grounding | Evidence status |
|---|---|---|
| HOG high-osmolarity glycerol pathway | `GO:0000165` (MAPK cascade) plus label | Central fungal osmotic-signaling candidate, but xerophile-specific causality is incompletely tested. |
| Hog1/HogA MAP kinase | Label or taxon-specific UniProt after strain verification | Includes WiHog1A/WiHog1B and *Aspergillus* HogA-related proteins. |
| glycerol-3-phosphate dehydrogenase | `EC:1.1.1.8` for NAD-dependent enzyme, only after enzyme identity verification | Links central metabolism to glycerol synthesis. |
| *gfdB* | Label only pending organism-specific database verification | Reported osmoadaptation-associated gene in aspergilli. |
| AgGlpF aquaglyceroporin | Label only pending verified accession | Heterologous crop/yeast tolerance evidence; not yet direct xerophilic-growth causality. |
| ENA P-type Na⁺-exporting ATPase/*ena2* | Label only pending exact sequence | Ion-homeostasis module in *A. sydowii*. |
| K⁺/H⁺ antiporter/*kha1* | Label only pending exact sequence | Stress-responsive ion transport. |
| fatty-acid desaturase | `GO:0045300` may describe activity only if experimentally assigned | Supports membrane-fluidity remodeling. |
| sterol monooxygenase | Label/EC after enzyme-specific verification | Differentially expressed during saline stress. |
| ECM33, CRH, and GEL-family proteins | Label only | Candidate cell-wall integrity/cross-linking module. |
| compatible-solute accumulation | `GO:0071470` may be considered for cellular response to osmotic stress | Prefer a process label if GO semantics do not exactly match accumulation. |
| ion homeostasis | `GO:0050801` | Especially relevant to saline low-aw growth. |
| cell-wall organization/remodeling | `GO:0071555` | Strong *A. sydowii* stress-response evidence. |
| membrane lipid remodeling | Label only | Current evidence is mainly expression/composition association. |

### Taxon/context nodes

Retain taxa as label-only until exact NCBITaxon records are verified: *Aspergillus penicillioides*, *Xeromyces bisporus*, *Wallemia ichthyophaga*, *Aspergillus sydowii*, *A. ruber*, *A. cristatus*, *A. glaucus*, *A. wentii*, and *A. flavus*. The strongest extreme-low-aw phenotype concerns *A. penicillioides*; the strongest mechanistic evidence retrieved concerns halophilic *W. ichthyophaga* and *A. sydowii*, so taxon qualifiers are essential.

## 3. Candidate causal edges

The following compact view highlights the most defensible graph backbone.

| subject | predicate | object | taxon/condition | evidence strength |
|---|---|---|---|---|
| low water activity | causes | osmotic stress | generalized fungal low-aw growth context | strong |
| osmotic/salt stress | induces | glycerol accumulation | *Wallemia ichthyophaga*, *Aspergillus sydowii* under elevated salinity / reduced aw | strong |
| glycerol accumulation | supports | osmotic balance | halophilic/xerophilic fungal osmoadaptation | moderate-strong |
| hyperosmotic stress | induces | cell-wall remodeling | *Aspergillus sydowii* at high salinity; thicker wall, altered chitin/β-glucan architecture | strong |
| hyperosmotic stress | induces | membrane remodeling | *Aspergillus sydowii* at high salinity; altered fatty-acid/sterol-related response | moderate |
| cation transport | maintains | ion homeostasis | halophilic fungi including *Aspergillus sydowii*; ENA/KHA-associated transport responses | moderate |
| reduced water activity | permits active growth | cell division/germination | *Aspergillus penicillioides* at extremely low aw, reported down to 0.585 in assay conditions | strong |


*Table: This table summarizes the strongest candidate causal edges for xerophilic growth curation, emphasizing experimentally supported low-water-activity responses and the main mechanistic modules likely suitable for a TraitMech graph.*

### Evidence table

| # | Subject–predicate–object | Reference | Supporting snippet | Curation assessment |
|---:|---|---|---|---|
| 1 | **reduced water activity —permits→ active cell division/germination by *A. penicillioides*** | DOI: [10.1007/s00253-024-13338-5](https://doi.org/10.1007/s00253-024-13338-5), published Nov 2024 | “*A. penicillioides* … cell division detected at 0.585 aw” and “germination minimum at 0.565 aw.” | **Strong phenotype edge**, but distinguish measured 0.585 cell division from the modeled/theoretical 0.565 minimum. Review synthesis; ideally attach the cited primary study in YAML. (pocsi2024biotechnologicalpotentialof pages 1-2, pocsi2024biotechnologicalpotentialof pages 2-5) |
| 2 | **low aw (operationally ≤0.80) —defines/characterizes→ xerophilic fungal growth** | DOI: [10.1007/s00253-024-13338-5](https://doi.org/10.1007/s00253-024-13338-5), Nov 2024 | “definition threshold for xerophilic fungi at ≤0.80 aw.” | **Curatable scope relation**, but treat 0.80 as an operational convention rather than a universal mechanistic threshold. (pocsi2024biotechnologicalpotentialof pages 2-5) |
| 3 | **increased salinity/reduced aw —induces→ glycerol accumulation in *W. ichthyophaga*** | DOI: [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13), Jan 2014 | “glycerol is the major osmotically regulated solute that increases with salinity and decreases with hypo-osmotic shock.” | **Strong, taxon-specific primary evidence.** This is saline low-aw adaptation and should not be generalized to every xerophile. (zajc2014osmoadaptationstrategyof pages 1-2) |
| 4 | **glycerol accumulation —supports→ osmotic balance under saline low aw** | DOI: [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13), Jan 2014 | “primary osmoadaptation mechanism involves compatible solute accumulation.” | **Strong in *W. ichthyophaga*.** Compatible-solute strategy is supported over a salt-in strategy. (zajc2014osmoadaptationstrategyof pages 1-2) |
| 5 | **salinity stress —induces→ glycerol production in *A. sydowii*** | DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525), Feb 2020 | “osmotic stress from increased salinity triggers glycerol production.” | **Strong, condition-specific primary evidence.** At optimal 0.5 M NaCl, other polyols contributed, whereas glycerol dominated nonoptimal stress responses. (perezllano2020stressreshapesthe pages 15-17) |
| 6 | **hyperosmotic stress —induces→ thicker, remodeled fungal cell wall** | DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525), Feb 2020 | At 2.0 M NaCl, “chitin content decreases while β-glucan cross-linking increases, generating thicker cell walls with distinctive lamellar structure.” | **Strong for *A. sydowii* at 2.0 M NaCl.** Do not encode “more chitin”: evidence indicates decreased chitin in this assay. (perezllano2020stressreshapesthe pages 8-11, perezllano2020stressreshapesthe pages 11-13) |
| 7 | **ECM33/CRH/GEL-family expression —supports→ cell-wall integrity during osmotic stress** | DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525), Feb 2020 | “Cross-linkage proteins (ECM33, CRH, GEL families) show enhanced expression at high salinity (2.0 M NaCl).” | **Moderate/uncertain causal edge.** Differential expression is associative without knockout or perturbation evidence. (perezllano2020stressreshapesthe pages 8-11) |
| 8 | **salinity stress —induces→ membrane remodeling** | DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525), Feb 2020 | “upregulation of fatty acid desaturase and sterol monooxygenase, increasing membrane fluidity.” | **Moderate.** Expression supports a membrane-remodeling module, but direct necessity for xerophilic growth was not demonstrated. (perezllano2020stressreshapesthe pages 8-11) |
| 9 | **ENA2 P-type ATPase —contributes to→ Na⁺/K⁺ homeostasis under stress** | DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525), Feb 2020 | “ena2 (sodium pump) expression responds to stress signals”; ENA pumps help maintain “Na⁺/K⁺ balance.” | **Moderate, taxon-specific.** Expression and known transporter function support the edge, but necessity was not established. (perezllano2020stressreshapesthe pages 15-17) |
| 10 | **KHA1 K⁺/H⁺ antiporter —contributes to→ ion homeostasis under hypo-osmotic stress** | DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525), Feb 2020 | “kha1 (K⁺/H⁺ antiporter) is overexpressed under hypoosmotic conditions.” | **Weak-to-moderate** and not specifically a hyperosmotic/xerophilic-growth edge. Keep outside the minimal graph unless the graph includes recovery from osmotic shifts. (perezllano2020stressreshapesthe pages 15-17) |
| 11 | **HOG MAPK signaling —promotes→ compatible-solute/glycerol response** | DOI: [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13), Jan 2014; DOI: [10.1007/s00253-024-13338-5](https://doi.org/10.1007/s00253-024-13338-5), Nov 2024 | Sources identify WiHog1A/WiHog1B and HogA-dependent pathways; the 2024 review notes that functional characterization remains limited. | **Uncertain for TraitMech causality.** Biologically plausible and established broadly in fungi, but retrieved xerophile-specific material does not establish a clean perturbation chain to low-aw growth. (zajc2014osmoadaptationstrategyof pages 9-9, pocsi2024biotechnologicalpotentialof pages 7-8) |
| 12 | **glycerol-3-phosphate dehydrogenase upregulation/activity —increases→ glycerol-based osmoadaptation** | DOI: [10.1007/s00253-024-13338-5](https://doi.org/10.1007/s00253-024-13338-5), Nov 2024 | “*A. ruber* shows upregulation of glycerol-3-phosphate dehydrogenase under salt stress.” | **Moderate/uncertain.** Strong biochemical rationale, but review-level expression evidence is not proof that the enzyme is necessary or sufficient for xerophilic growth. (pocsi2024biotechnologicalpotentialof pages 5-7) |
| 13 | **very high glycerol (>5 M) —adds→ chaotropic stress** | DOI: [10.1038/s41598-020-62552-4](https://doi.org/10.1038/s41598-020-62552-4), Apr 2020 | “water-activity reduction is the primary mechanism … below 5 M, while chaotropicity becomes limiting … >5 M.” | **Strong assay interpretation edge.** Useful for preventing erroneous attribution of all glycerol effects solely to aw. (hamill2020microbiallagphase pages 3-4) |
| 14 | **reduced aw/sugar-rich food —selects for/enables→ xerophilic Aspergillus spoilage** | DOI: [10.1007/s00253-024-13338-5](https://doi.org/10.1007/s00253-024-13338-5), Nov 2024 | Xerophilic aspergilli spoil products at aw “as low as 0.68–0.75”; *A. candidus* contaminates stored cereals and processed meat. | **Strong ecological/application association**, but “selects for” is safer than a direct intracellular causal predicate. (pocsi2024biotechnologicalpotentialof pages 5-7, pocsi2024biotechnologicalpotentialof pages 2-5) |

## 4. Proposed minimal causal graph

A conservative initial graph for `xerophilic_low_water_activity_growth` should emphasize generic processes and leave taxon-specific subgraphs explicit:

1. **low water activity → osmotic/water stress**
2. **osmotic stress → HOG/MAPK signaling** *(provisional)*
3. **osmotic stress/HOG signaling → glycerol and compatible-solute accumulation** *(HOG link provisional; accumulation itself strong)*
4. **compatible-solute accumulation → cytoplasmic osmotic balance**
5. **cytoplasmic osmotic balance → active growth at low aw**
6. **hyperosmotic stress → cell-wall remodeling**
7. **hyperosmotic stress → membrane-lipid remodeling** *(moderate)*
8. **saline low-aw conditions → cation-transport response → ion homeostasis** *(salinity-specific branch)*
9. **osmotic balance + envelope remodeling + ion homeostasis → xerophilic growth** *(integrative inferred edge)*

For a first YAML revision, edges 1, 3 (without overcommitting to HOG), 4, 6, and the phenotype endpoint are the safest. The final integrative edge should be marked inferred unless a genetic perturbation directly links each module to growth at measured low aw.

## 5. Recent developments, applications, and statistics

The principal 2024 synthesis identifies xerophilic and salt-tolerant aspergilli as sources of salt-tolerant proteases, peptidases, glycosidases, lipases, and oxidoreductases. Reported examples include *A. oryzae* proteases tolerating **18% NaCl (~3 M)**, an *A. glaucus* GH5 cellulase tolerating **4.0 M NaCl**, and *A. sydowii* γ-glutamyl transpeptidase functioning at **aw 0.85** in solid-state fermentation. These are real-world enzyme-platform applications but are consequences of extremotolerance, not causal mechanisms of xerophilic growth. (pocsi2024biotechnologicalpotentialof pages 7-8)

Current implementations and opportunities include low-aw fermentation of tea by *A. cristatus*, cured-meat fermentation involving *A. chevalieri/A. proliferans*, and traditional daqu and meju production. Environmental applications include dye decolorization, xenobiotic degradation, ion removal, and high-salinity wastewater treatment; one reviewed implementation used *A. tubingensis*-based aerobic granular sludge at **50 g/L (~0.9 M) NaCl** to improve chemical-oxygen-demand and nitrogen removal. Agricultural work includes phosphate biosolubilization and heterologous expression of fungal stress genes such as **AgGlpF** and **AgRPS3aE** to enhance drought/salt tolerance in crops. These applications are promising but should remain outside the core causal graph unless the graph explicitly represents trait consequences. (pocsi2024biotechnologicalpotentialof pages 12-13, pocsi2024biotechnologicalpotentialof pages 11-12, pocsi2024biotechnologicalpotentialof pages 10-11)

Food safety remains the dominant real-world concern. Xerophilic fungi colonize dried, sugared, salted, and stored foods that exclude most bacteria; low-aw and temperature jointly alter growth and mycotoxin production. The 2024 review reports food-spoilage growth at aw approximately **0.68–0.75**, while control studies operate across broader aw ranges. These figures are species-, substrate-, and temperature-dependent and should not be treated as universal safe limits. (pocsi2024biotechnologicalpotentialof pages 12-13, pocsi2024biotechnologicalpotentialof pages 5-7)

The current expert view is therefore **modular rather than single-gene**: fungal growth at low aw combines compatible-solute management, signaling, envelope remodeling, membrane adaptation, and—when salts produce the low aw—ion transport. Importantly, the *A. sydowii* study found that responses at optimal salinity differed qualitatively from those under hypo- or hyperosmotic stress. Mechanisms measured during acute 2.0 M NaCl stress should not automatically be labeled constitutive adaptations of xerophiles. (perezllano2020stressreshapesthe pages 15-17, perezllano2020stressreshapesthe pages 4-8)

## 6. Warnings: claims not yet ready for unqualified curation

1. **Do not use desiccation survival as evidence of xerophilic growth.** Require growth, division, germination, or metabolism while aw remains low.
2. **Do not make `xerotolerant` universally equivalent to `xerophilic`.** Preserve the supplied synonym for search, but retain preference/requirement versus tolerance in evidence annotations.
3. **Do not generalize halophile mechanisms to all xerophiles.** ENA transport, K⁺/H⁺ antiport, and Na⁺ homeostasis belong to a saline-low-aw branch.
4. **Do not curate HOG→xerophilic growth as established from expression alone.** Seek knockout, complementation, phospho-Hog1, or growth-rescue experiments at measured aw.
5. **Do not curate gene-expression changes as necessity.** ECM33/CRH/GEL proteins, desaturases, sterol monooxygenases, and GPD genes are candidates until perturbation data are linked to low-aw growth.
6. **Do not treat 0.565 aw as an observed sustained-growth limit.** It is described as theoretical; 0.585 aw is the reported cell-division/germination benchmark in the retrieved synthesis.
7. **Do not infer low aw from solute concentration alone.** Record measured aw, solute identity, concentration, temperature, medium, strain, and endpoint.
8. **Do not collapse osmotic and chaotropic effects.** At very high glycerol concentrations, chaotropicity can dominate toxicity. (hamill2020microbiallagphase pages 3-4)
9. **Do not curate application phenotypes as mechanisms.** Enzyme production, fermentation, spoilage, bioremediation, and crop engineering are downstream uses or consequences.
10. **Ontology caution:** organism-specific genes and proteins should remain label-only until strain-specific UniProt/NCBI identifiers are verified; arabitol should not receive a stereospecific CHEBI identifier without chemical resolution.

## 7. DOI-first bibliography

1. Pócsi I, Dijksterhuis J, Houbraken J, de Vries RP. **Biotechnological potential of salt tolerant and xerophilic species of Aspergillus.** *Applied Microbiology and Biotechnology* 108 (published November 2024). DOI: [10.1007/s00253-024-13338-5](https://doi.org/10.1007/s00253-024-13338-5). Recent authoritative synthesis of definitions, taxa, mechanisms, applications, and quantitative limits. (pocsi2024biotechnologicalpotentialof pages 2-5, pocsi2024biotechnologicalpotentialof pages 1-2)
2. Pérez-Llano Y, et al. **Stress Reshapes the Physiological Response of Halophile Fungi to Salinity.** *Cells* 9:525 (published February 2020). DOI: [10.3390/cells9030525](https://doi.org/10.3390/cells9030525). Primary transcriptomic, biochemical, and ultrastructural study of *A. sydowii*. (perezllano2020stressreshapesthe pages 15-17, perezllano2020stressreshapesthe pages 8-11)
3. Hamill PG, et al. **Microbial lag phase can be indicative of, or independent from, cellular stress.** *Scientific Reports* 10 (published April 2020). DOI: [10.1038/s41598-020-62552-4](https://doi.org/10.1038/s41598-020-62552-4). Demonstrates assay interpretation issues and separates low-aw from high-glycerol chaotropic effects. (hamill2020microbiallagphase pages 3-4)
4. Zajc J, Kogej T, Galinski EA, Ramos J, Gunde-Cimerman N. **Osmoadaptation Strategy of the Most Halophilic Fungus, Wallemia ichthyophaga, Growing Optimally at Salinities above 15% NaCl.** *Applied and Environmental Microbiology* 80:247–256 (published January 2014). DOI: [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13). Primary quantitative evidence for glycerol-centered compatible-solute adaptation and ion/cell-wall physiology. (zajc2014osmoadaptationstrategyof pages 1-2)

### Bottom-line curation recommendation

Retain `traitmech:000011` as **active growth at low water activity**, with measured aw as a required evidence qualifier. Build the first causal graph around **low aw → osmotic stress → compatible-solute accumulation → osmotic balance → growth**, supplemented by strongly supported **cell-wall remodeling** and a separate **salinity-specific ion-homeostasis branch**. Mark HOG, individual GPD genes, aquaglyceroporins, and membrane-remodeling genes as provisional until direct perturbation evidence demonstrates altered growth at controlled aw.

References

1. (pocsi2024biotechnologicalpotentialof pages 2-5): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

2. (pocsi2024biotechnologicalpotentialof pages 1-2): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (hamill2020microbiallagphase pages 3-4): Philip G. Hamill, Andrew Stevenson, Phillip E. McMullan, James P. Williams, Abiann D. R. Lewis, Sudharsan S, Kath E. Stevenson, Keith D. Farnsworth, Galina Khroustalyova, Jon Y. Takemoto, John P. Quinn, Alexander Rapoport, and John E. Hallsworth. Microbial lag phase can be indicative of, or independent from, cellular stress. Scientific Reports, Apr 2020. URL: https://doi.org/10.1038/s41598-020-62552-4, doi:10.1038/s41598-020-62552-4. This article has 164 citations and is from a peer-reviewed journal.

4. (zajc2014osmoadaptationstrategyof pages 1-2): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

5. (perezllano2020stressreshapesthe pages 15-17): Yordanis Pérez-Llano, Eya Caridad Rodríguez-Pupo, Irina S. Druzhinina, Komal Chenthamara, Feng Cai, Nina Gunde-Cimerman, Polona Zalar, Cene Gostinčar, Rok Kostanjšek, Jorge Luis Folch-Mallol, Ramón Alberto Batista-García, and María del Rayo Sánchez-Carbente. Stress reshapes the physiological response of halophile fungi to salinity. Cells, 9:525, Feb 2020. URL: https://doi.org/10.3390/cells9030525, doi:10.3390/cells9030525. This article has 77 citations.

6. (perezllano2020stressreshapesthe pages 8-11): Yordanis Pérez-Llano, Eya Caridad Rodríguez-Pupo, Irina S. Druzhinina, Komal Chenthamara, Feng Cai, Nina Gunde-Cimerman, Polona Zalar, Cene Gostinčar, Rok Kostanjšek, Jorge Luis Folch-Mallol, Ramón Alberto Batista-García, and María del Rayo Sánchez-Carbente. Stress reshapes the physiological response of halophile fungi to salinity. Cells, 9:525, Feb 2020. URL: https://doi.org/10.3390/cells9030525, doi:10.3390/cells9030525. This article has 77 citations.

7. (perezllano2020stressreshapesthe pages 11-13): Yordanis Pérez-Llano, Eya Caridad Rodríguez-Pupo, Irina S. Druzhinina, Komal Chenthamara, Feng Cai, Nina Gunde-Cimerman, Polona Zalar, Cene Gostinčar, Rok Kostanjšek, Jorge Luis Folch-Mallol, Ramón Alberto Batista-García, and María del Rayo Sánchez-Carbente. Stress reshapes the physiological response of halophile fungi to salinity. Cells, 9:525, Feb 2020. URL: https://doi.org/10.3390/cells9030525, doi:10.3390/cells9030525. This article has 77 citations.

8. (zajc2014osmoadaptationstrategyof pages 9-9): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

9. (pocsi2024biotechnologicalpotentialof pages 7-8): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (pocsi2024biotechnologicalpotentialof pages 5-7): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (pocsi2024biotechnologicalpotentialof pages 12-13): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

12. (pocsi2024biotechnologicalpotentialof pages 11-12): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

13. (pocsi2024biotechnologicalpotentialof pages 10-11): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

14. (perezllano2020stressreshapesthe pages 4-8): Yordanis Pérez-Llano, Eya Caridad Rodríguez-Pupo, Irina S. Druzhinina, Komal Chenthamara, Feng Cai, Nina Gunde-Cimerman, Polona Zalar, Cene Gostinčar, Rok Kostanjšek, Jorge Luis Folch-Mallol, Ramón Alberto Batista-García, and María del Rayo Sánchez-Carbente. Stress reshapes the physiological response of halophile fungi to salinity. Cells, 9:525, Feb 2020. URL: https://doi.org/10.3390/cells9030525, doi:10.3390/cells9030525. This article has 77 citations.