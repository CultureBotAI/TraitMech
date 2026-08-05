---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:53:07.312225'
end_time: '2026-08-04T02:58:18.716582'
duration_seconds: 311.4
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range mid1
  trait_identifier: METPO:1000461
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 6\u20137, characteristic of neutrophilic physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Facultative acidophile, Neutrophile, pHR_6_to_7
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports near-neutral cytoplasmic pH at near-neutral external pH as the neutrophilic
    regime.)'
  causal_graph_summary: 'ph_range_mid1_neutrophile_range: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000461
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 6–7, characteristic of neutrophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Facultative acidophile, Neutrophile, pHR_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports near-neutral cytoplasmic pH at near-neutral external pH as the neutrophilic regime.)
- **Existing causal graph summary:** ph_range_mid1_neutrophile_range: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **pH range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid1.yaml`.

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
- **Trait label:** pH range mid1
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000461
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 6–7, characteristic of neutrophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Facultative acidophile, Neutrophile, pHR_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports near-neutral cytoplasmic pH at near-neutral external pH as the neutrophilic regime.)
- **Existing causal graph summary:** ph_range_mid1_neutrophile_range: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **pH range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid1.yaml`.

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


# Curation report: microbial pH range mid1

## Executive conclusion

**Target trait:** **“METPO:1000461”** (*pH range mid1*; ENVIRONMENT; CLASS; REVIEWED).

The safest interpretation is an **assay-observed capacity for growth across an external-pH interval of approximately 6–7**, characteristic of neutralophilic physiology. It should not be equated with an organism’s pH optimum, its complete growth range, or survival after transient acid/alkaline challenge. Neutralophiles as a broad physiological class may grow over approximately pH 5.5–9.0 while maintaining a much narrower cytoplasmic pH, historically estimated at about 7.5–7.7; a 2023 synthesis gives a more general internal-pH range of 7.0–7.5 for many cell types. At external pH near 7, *Escherichia coli* has a small inwardly alkaline ΔpH together with a substantial negative-inside membrane potential. (krulwich2011molecularaspectsof pages 1-3, poolman2023physicochemicalhomeostasisin pages 1-2)

The graph should therefore center on **near-neutral cytoplasmic pH, cytoplasmic buffering, proton-motive-force homeostasis, respiratory or ATPase-mediated proton transport, and cation/proton exchange**. NhaA, KefC, glutamate decarboxylase, and other named stress systems are valuable mechanistic examples, but most should not be represented as universal causes of the pH 6–7 growth phenotype.

## 1. Trait scope and boundaries

### Positive scope

The trait records growth support over an extracellular pH interval, ideally established from replicated growth curves or endpoint biomass/yield measurements in buffered media. The phenotype is environmentally conditional: temperature, medium composition, buffering species and capacity, ionic strength, oxygen availability, carbon source, inoculum history, and incubation time can all shift the observed limits.

A biologically plausible mechanistic interpretation is:

**external pH 6–7 → manageable proton activity at the cell surface → cytoplasmic buffering plus regulated proton/cation transport → near-neutral cytoplasmic pH and usable PMF → ATP synthesis, transport, enzyme function, and growth.**

PMF comprises ΔpH and electrical potential Δψ. Under standard conventions, bacterial interiors are usually alkaline and electrically negative relative to the exterior. Near external pH 7, ΔpH is small and Δψ supplies a substantial part of PMF. (krulwich2011molecularaspectsof pages 1-3, poolman2023physicochemicalhomeostasisin pages 1-2)

### Boundary cases

1. **pH optimum versus range:** growth optimal near pH 6.5 does not prove that the growth-supporting range spans 6–7.
2. **Growth versus survival:** enteric bacteria can survive nonpermissive gastric acidity and resume growth after return to neutral medium; that is acid resistance, not growth at the challenge pH. (krulwich2011molecularaspectsof pages 1-3)
3. **Broad neutralophile versus this bin:** the literature’s approximate pH 5.5–9.0 neutralophile range is broader than the ontology term’s specific 6–7 interval. (krulwich2011molecularaspectsof pages 1-3)
4. **Facultative acidophile and “alkali tolerant”:** these synonyms should be treated cautiously. Acidophilic growth or alkaline tolerance implies capacities beyond the core 6–7 phenotype and should not be inferred from this trait alone.
5. **Assay drift:** microbial metabolism can acidify or alkalinize weakly buffered media. Initial pH alone is therefore insufficient; final or continuous pH should be reported.
6. **Taxon-specific stress mechanisms:** GadB, NhaA, Ktr, and KefC evidence does not establish that every organism carrying this phenotype uses those systems.

## 2. Candidate nodes grouped by type

### Trait and environmental nodes

- **pH range mid1 — “METPO:1000461”**
- Parent trait — **METPO:1000332**
- External pH 6–7
- Hydrogen-ion activity / proton concentration
- Buffered growth medium
- Buffer capacity, temperature, ionic strength, salinity, oxygen availability, carbon source, and incubation time

### Chemicals and energetic quantities

- Proton — **CHEBI:15378**
- Sodium ion — **CHEBI:29101**
- Potassium ion — **CHEBI:29103**
- ATP — **CHEBI:15422**
- ADP — **CHEBI:16761**
- Proton motive force
- Transmembrane pH gradient, ΔpH
- Membrane potential, Δψ
- Inorganic and organic phosphates
- Glutamate and GABA, if an acid-stress subgraph is retained
- Glutathione and glutathione–electrophile adducts, if a KefC context subgraph is retained

### Cellular locations

- Cytoplasm — **GO:0005737**
- Plasma membrane — **GO:0005886**
- Extracellular region/periplasm as taxonomically appropriate

### Processes and molecular functions

- Cellular pH homeostasis — **GO:0006885**
- Proton transmembrane transport — **GO:1902600**
- ATP synthesis coupled proton transport — **GO:0015986**
- Sodium/proton antiport
- Potassium/proton antiport
- Cytoplasmic buffering
- Cellular respiration and respiratory proton pumping
- Amino-acid decarboxylation, explicitly marked acid-stress-specific

### Proteins, transporters, and complexes

- Respiratory-chain proton-pumping complexes; retain as a family-level node unless taxon-specific evidence identifies a complex
- F-type H+-transporting ATP synthase — preferably GO-grounded at complex/function level
- Na+/H+ antiporter family
- K+/H+ antiporter family
- **NhaA**, *E. coli* Na+/H+ antiporter — use a strain-specific UniProt accession only after the curated taxon/strain is fixed
- **Ktr potassium-uptake system** — taxon-specific evidence from *Staphylococcus aureus*
- **KefC** and **KefB** — *E. coli* electrophile-response K+/H+ exchangers
- **GadB** plus glutamate/GABA antiporter — acid-resistance module, not a core neutral-range module

Do not assign a UniProt, NCBITaxon, EC, Rhea, KEGG, or MetaCyc identifier without fixing the exact organism, reaction direction, and database record. Label-only nodes are preferable to incorrect grounding.

## 3. Evidence-backed candidate edges

The following table is the proposed evidence ledger. “Core” means suitable for a generic neutrophilic pH-range graph; “context-only” means mechanistically valid but stress- or taxon-specific.

| subject | predicate | object | evidence tier | taxon/condition | DOI | short verbatim supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| external pH 6–7 | associated_with | small positive ΔpH and near-neutral cytoplasmic pH | High | neutralophilic bacteria; especially *E. coli* near pH ~7.0 | 10.1038/nrmicro2549 | "E. coli has only a small ΔpH (pHin > pHout) when growing at pH ~7.0" (krulwich2011molecularaspectsof pages 1-3) | Core trait-scope edge for neutrophilic growth regime; maps assay pH range to expected PMF architecture. |
| neutralophilic bacteria | maintain | cytoplasmic pH ~7.5–7.7 | High | neutralophiles across growth pHout ~5.5–9.0 | 10.1038/nrmicro2549 | "neutralophilic bacteria can grow at pHout values from ~5.5–9.0 but generally maintain their cytoplasmic pH in a narrow range ~7.5–7.72,3" (krulwich2011molecularaspectsof pages 1-3) | Core definitional physiology; helps distinguish neutrophilic growth from mere survival outside range. |
| cytoplasmic buffering capacity | resists | internal pH fluctuation | High | *Escherichia coli*, *Lactococcus lactis* cytoplasm | 10.1093/femsre/fuad033 | "The buffering capacity of the cytoplasm is important in absorbing pH fluctuations" (poolman2023physicochemicalhomeostasisin pages 1-2) | Core supportive mechanism; node can be label-only or “cytoplasmic buffering capacity”. |
| proton-pumping respiratory chain components | generates | proton motive force (PMF) via proton efflux | High | respiratory bacteria | 10.1038/nrmicro2549 | "Primary proton pumps generate the PMF... They include respiratory or other redox potential-driven pumps (e.g. respiratory chain pumps)" (krulwich2011molecularaspectsof pages 1-3) | Core generic mechanism, but not uniquely specific to pH 6–7. Curate as broad support node if graph remains generic. |
| PMF | drives | ATP synthesis and solute transport | High | bacteria generally | 10.1093/femsre/fuad033 | "serve as a source of electrochemical energy (proton motive force, PMF... ) to drive the synthesis of ATP and the transport of solutes" (poolman2023physicochemicalhomeostasisin pages 1-2) | Core bioenergetic edge connecting homeostasis to growth support. |
| Na+/H+ antiporters | regulates | internal pH / pH homeostasis | High | bacteria generally | 10.1093/femsre/fuad033 | "Key regulators of bacterial pH homeostasis are Na+/H+ and K+/H+ antiporters" (poolman2023physicochemicalhomeostasisin pages 1-2) | Core causal family-level edge. Ground as transporter class if individual gene unknown. |
| K+/H+ antiporters | regulates | internal pH / pH homeostasis | High | bacteria generally | 10.1093/femsre/fuad033 | "Key regulators of bacterial pH homeostasis are Na+/H+ and K+/H+ antiporters" (poolman2023physicochemicalhomeostasisin pages 1-2) | Core causal family-level edge. Distinct from K+ uptake systems such as Ktr. |
| NhaA (*E. coli* Na+/H+ antiporter) | mediates | 2 H+ influx coupled to 1 Na+ efflux | High | *Escherichia coli*; alkaline activation context | 10.1038/nrmicro2549 | "the stoichiometry for E. coli NhaA is 2H+/1Na+" (krulwich2011molecularaspectsof pages 5-6) | Strong mechanistic edge for transporter function; likely context-supporting rather than central for pH 6–7 specifically. |
| NhaA | inactive_below_pH | 6.5 | High | *Escherichia coli*; transporter assay | 10.1038/s41598-024-56425-3 | "It is inactive below pH 6.5, and its activity increases with pH, peaking at pH 8.5" (rimon2024thecrossingof pages 1-2) | Important boundary note: NhaA is not a strong candidate core cause for growth in the 6–7 regime, especially near pH 6. |
| Ktr-mediated K+ uptake | supports | maintenance of cytoplasmic pH and PMF | Medium | *Staphylococcus aureus*; tested at pH 6.0, 7.3, 8.6 | 10.1128/msphere.00125-16 | "Ktr-mediated K+ uptake is necessary for maintaining cytoplasmic pH and the establishment of a proton motive force" (gries2016potassiumuptakemodulates pages 2-3) | Useful taxon-specific mechanistic support; uncertain for general neutrophiles. Mark as taxon-specific if curated. |
| amino acid decarboxylation pathways | consumes | cytoplasmic protons / contributes to PMF | High | acid stress; lactic acid bacteria and enterics | 10.1093/femsre/fuad033 | "the chemistry of the decarboxylation reaction requires a proton... the equivalent of 1 proton is pumped per molecule decarboxylated" (poolman2023physicochemicalhomeostasisin pages 2-4) | Context-only, not core neutral-range cause; primarily acid-stress adaptation. |
| glutamate decarboxylase system (GadB plus antiporter) | supports | acid pH homeostasis | High | *E. coli* gastric/acid challenge | 10.1038/nrmicro2549 | "GadB... consumes a proton during decarboxylation... The consumption of the proton supports acid pH homeostasis" (krulwich2011molecularaspectsof pages 5-6) | Context-only; do not overgeneralize to routine growth at pH 6–7. |
| KefC activation | causes | K+ efflux coupled to H+ influx | High | *Escherichia coli*; electrophile stress | 10.1038/s41467-024-49082-7 | "exchange intracellular K+ for external H+ in response to electrophilic stress" (gulati2024structureandmechanism pages 1-2) | Context-only stress response, not a core neutral-range homeostasis edge. |
| KefC activation | causes | short-term cytosolic acidification of 1–2 pH units | High | *Escherichia coli*; electrophile stress | 10.1038/s41467-024-49082-7 | "Activation of KefC leads to short-term cytosolic acidification of 1–2 pH units" (gulati2024structureandmechanism pages 1-2) | Strong recent mechanistic result, but explicitly stress-specific and unsuitable as a core cause of neutrophilic phenotype. |


*Table: This table lists candidate causal edges for curating METPO:1000461, with direct snippets, DOI-first sourcing, and notes on whether each edge is core to neutral-range growth or only context-specific stress physiology.*

### Recommended minimal graph

For a compact graph close to the existing nine-node/eight-edge scale, the strongest defensible backbone is:

1. **external pH 6–7 → establishes → small inwardly alkaline ΔpH**;
2. **cytoplasmic buffering → resists → cytoplasmic pH fluctuation**;
3. **respiratory proton pumping or ATPase-mediated proton extrusion → generates/supports → PMF**;
4. **Na+/H+ and K+/H+ antiport → regulates → cytoplasmic pH**;
5. **regulated proton/cation flux → maintains → near-neutral cytoplasmic pH**;
6. **ΔpH + Δψ → constitute → PMF**;
7. **PMF → drives → ATP synthesis and solute transport**;
8. **near-neutral cytoplasmic pH plus PMF → supports → growth at external pH 6–7**.

Edges 1, 2, 6, and 7 have especially direct generic support. Edges linking the homeostatic state to the ontology phenotype are biologically strong but remain integrative rather than gene-knockout demonstrations of this exact METPO class. (krulwich2011molecularaspectsof pages 1-3, poolman2023physicochemicalhomeostasisin pages 1-2)

## 4. Current quantitative understanding

The 2023 review estimates that a roughly 1-fL *E. coli* or *Lactococcus lactis* cytoplasm contains only about **10 free protons at pH 7.2**. It cites approximately **100 mM organic phosphates** in *L. lactis*, illustrating why chemical buffering is indispensable even though buffering alone does not establish the growth phenotype. (poolman2023physicochemicalhomeostasisin pages 1-2)

PMF can be represented as the sum of electrical and chemical terms, with approximately **58–59 mV per pH unit** near room temperature. F-type ATP synthases use approximately **3–5 protons per ATP**, depending on species. Metabolite decarboxylation releases about **20 kJ mol−1**, below the approximately **31 kJ mol−1** standard free-energy requirement quoted for ATP synthesis, but its energy can be conserved indirectly as PMF. (poolman2023physicochemicalhomeostasisin pages 1-2)

For *E. coli* NhaA, transport is electrogenic at **2 H+ entering per 1 Na+ exiting**, with reported turnover of **10³–10⁴ s−1**. The 2024 study reports that NhaA is inactive below pH 6.5 and peaks near pH 8.5; this argues against making NhaA the universal central driver of growth throughout pH 6–7. (krulwich2011molecularaspectsof pages 5-6, rimon2024thecrossingof pages 1-2)

In *S. aureus*, Ktr-mediated K+ uptake was studied at external pH **6.0, 7.3, and 8.6**. K+ deficiency caused cytoplasmic acidification exceeding **one pH unit within three hours** and strongly inhibited growth, supporting a taxon-specific link among K+ uptake, pH homeostasis, PMF, and metabolism. (gries2016potassiumuptakemodulates pages 2-3)

## 5. Recent developments, 2023–2024

### Physicochemical integration, 2023

Poolman’s 2023 review reframed pH regulation as part of integrated physicochemical homeostasis rather than an isolated transporter phenotype. Internal pH, PMF, ionic strength, crowding, volume, and energy status are coupled; bacterial internal pH is commonly maintained around 7.0–7.5. This supports modeling the trait as a systems-level state rather than attributing it to one marker gene. (poolman2023physicochemicalhomeostasisin pages 1-2)

### NhaA conformational mechanism, 2024

Rimon and colleagues showed that cross-linking two residues across the characteristic NhaA transmembrane crossing traps the transporter in an outward-facing conformation, suppresses antiport, and impairs NhaA-dependent high-salt growth. In everted-vesicle assays, reducing conditions restored the double mutant to approximately **80% of wild-type activity at pH 8.5**. This is strong evidence for the alternating-access mechanism, but the experiments concern NhaA activity and salt resistance rather than direct determination of the pH 6–7 growth-range trait. (rimon2024thecrossingof pages 1-2, rimon2024thecrossingof pages 4-5)

### KefC structural mechanism, 2024

Cryo-EM structures at approximately **3.1 Å** resolved the glutathione-gated *E. coli* KefC K+/H+ exchanger and its regulatory RCK domains. KefC exchanges intracellular K+ for external H+ during electrophile stress; activation transiently acidifies the cytosol by **1–2 pH units**, protecting against electrophilic damage. This is an important current example of controlled cytoplasmic acidification, but it is the opposite of a generic “maintain neutral pH at all times” model and must remain a stress-specific branch. (gulati2024structureandmechanism pages 1-2)

## 6. Applications and expert interpretation

The mechanisms have practical relevance to fermentation robustness, food preservation, pathogen survival, antimicrobial development, environmental biotechnology, and engineering strains exposed to fluctuating pH or salt. The 2011 authoritative review explicitly identifies pathogen targeting and environmental-microbe exploitation as translational motivations. (krulwich2011molecularaspectsof pages 1-3)

For TraitMech, the expert-level interpretation is that **the phenotype is emergent and many-to-one**. Different respiratory modes and transporter repertoires can yield the same pH 6–7 growth phenotype. Consequently, family-level process nodes are more portable than named *E. coli* genes. A transporter’s presence is also not evidence that it is active at pH 6–7: NhaA’s strong pH gating is a direct counterexample. (poolman2023physicochemicalhomeostasisin pages 1-2, rimon2024thecrossingof pages 1-2)

## 7. Warnings: claims not yet ready for curation

- Do not curate **NhaA → causes METPO:1000461**. The evidence supports Na+/pH homeostasis and alkaline/salt physiology, while NhaA is inactive below pH 6.5. (rimon2024thecrossingof pages 1-2)
- Do not curate **KefC → maintains neutrophilic cytoplasmic pH**. KefC deliberately acidifies the cytosol during electrophile stress. (gulati2024structureandmechanism pages 1-2)
- Do not curate GadB or other decarboxylases as universal pH 6–7 growth determinants; the retrieved evidence concerns severe acid challenge and gastric survival. (krulwich2011molecularaspectsof pages 5-6)
- Do not equate “alkali tolerant,” “facultative acidophile,” and “neutrophile” without organism-level growth data.
- Do not infer this trait from genome content alone. Growth-range evidence must control medium, buffer, temperature, atmosphere, and time.
- Do not represent buffering capacity as sufficient by itself. A foundational review notes that no strong general correlation had emerged between buffering capacity and bacterial pH-homeostasis capacity. (krulwich2011molecularaspectsof pages 5-6)
- Avoid a universal fixed pHin. Estimates differ by organism and method: approximately 7.5–7.7 in the foundational neutralophile synthesis versus 7.0–7.5 in the broader 2023 physicochemical review. (krulwich2011molecularaspectsof pages 1-3, poolman2023physicochemicalhomeostasisin pages 1-2)

## DOI-first bibliography

1. Poolman B. **Physicochemical homeostasis in bacteria.** *FEMS Microbiology Reviews*. Advance publication **19 June 2023**. DOI: [10.1093/femsre/fuad033](https://doi.org/10.1093/femsre/fuad033). (poolman2023physicochemicalhomeostasisin pages 1-2)
2. Rimon A, Amartely H, Padan E. **The crossing of two unwound transmembrane regions that is the hallmark of the NhaA structural fold is critical for antiporter activity.** *Scientific Reports*. **March 2024**;14:5915. DOI: [10.1038/s41598-024-56425-3](https://doi.org/10.1038/s41598-024-56425-3). (rimon2024thecrossingof pages 1-2)
3. Gulati A, et al. **Structure and mechanism of the K+/H+ exchanger KefC.** *Nature Communications*. Accepted **23 May 2024**; published **June 2024**;15:4751. DOI: [10.1038/s41467-024-49082-7](https://doi.org/10.1038/s41467-024-49082-7). (gulati2024structureandmechanism pages 1-2)
4. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. **May 2011**;9:330–343. DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3)
5. Gries CM, et al. **Potassium Uptake Modulates Staphylococcus aureus Metabolism.** *mSphere*. **June 2016**;1. DOI: [10.1128/mSphere.00125-16](https://doi.org/10.1128/mSphere.00125-16). (gries2016potassiumuptakemodulates pages 2-3)

Overall, the recommended YAML graph should encode a **generic homeostatic and bioenergetic backbone**, while retaining NhaA, Ktr, KefC, and amino-acid decarboxylation only as explicitly taxon- or stress-qualified evidence modules.

References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (poolman2023physicochemicalhomeostasisin pages 1-2): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 46 citations and is from a domain leading peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

4. (rimon2024thecrossingof pages 1-2): Abraham Rimon, Hadar Amartely, and Etana Padan. The crossing of two unwound transmembrane regions that is the hallmark of the nhaa structural fold is critical for antiporter activity. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-56425-3, doi:10.1038/s41598-024-56425-3. This article has 6 citations and is from a peer-reviewed journal.

5. (gries2016potassiumuptakemodulates pages 2-3): Casey M. Gries, Marat R. Sadykov, Logan L. Bulock, Sujata S. Chaudhari, Vinai C. Thomas, Jeffrey L. Bose, and Kenneth W. Bayles. Potassium uptake modulates staphylococcus aureus metabolism. mSphere, Jun 2016. URL: https://doi.org/10.1128/msphere.00125-16, doi:10.1128/msphere.00125-16. This article has 42 citations and is from a peer-reviewed journal.

6. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 46 citations and is from a domain leading peer-reviewed journal.

7. (gulati2024structureandmechanism pages 1-2): Ashutosh Gulati, Surabhi Kokane, Annemarie Perez-Boerema, Claudia Alleva, Pascal F. Meier, Rei Matsuoka, and David Drew. Structure and mechanism of the k+/h+ exchanger kefc. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49082-7, doi:10.1038/s41467-024-49082-7. This article has 12 citations and is from a highest quality peer-reviewed journal.

8. (rimon2024thecrossingof pages 4-5): Abraham Rimon, Hadar Amartely, and Etana Padan. The crossing of two unwound transmembrane regions that is the hallmark of the nhaa structural fold is critical for antiporter activity. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-56425-3, doi:10.1038/s41598-024-56425-3. This article has 6 citations and is from a peer-reviewed journal.