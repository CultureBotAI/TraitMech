---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:14:56.200251'
end_time: '2026-08-04T03:25:44.541120'
duration_seconds: 648.34
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: psychrotolerant
  trait_identifier: METPO:1000618
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: psychrotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature preference in which growth can occur at low temperatures
    without an obligate low-temperature preference.
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel
    psychrotolerant bacterium (Organism example: Pseudomonas guineae is described
    as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity
    (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant
    facultative adaptation overcomes without full psychrophile dedication.)'
  causal_graph_summary: 'psychrotolerant_facultative_cold_adaptation: 12 nodes, 9
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** psychrotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000618
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel psychrotolerant bacterium (Organism example: Pseudomonas guineae is described as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant facultative adaptation overcomes without full psychrophile dedication.)
- **Existing causal graph summary:** psychrotolerant_facultative_cold_adaptation: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **psychrotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrotolerant.yaml`.

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
- **Trait label:** psychrotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000618
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/ijs.0.65141-0: Pseudomonas guineae sp. nov., a novel psychrotolerant bacterium (Organism example: Pseudomonas guineae is described as psychrotolerant.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as the challenge that psychrotolerant facultative adaptation overcomes without full psychrophile dedication.)
- **Existing causal graph summary:** psychrotolerant_facultative_cold_adaptation: 12 nodes, 9 edges

## Research Objective

Research the microbial trait **psychrotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/psychrotolerant.yaml`.

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


# Curation-focused research report: psychrotolerant

## 1. Trait scope

**Trait:** **psychrotolerant**  
**Identifier:** **METPO:1000618**  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** METPO:1000613  
**Reviewed definition:** “A temperature preference in which growth can occur at low temperatures without an obligate low-temperature preference.”

### Operational interpretation

For TraitMech, psychrotolerance should mean **demonstrated multiplication at low temperature combined with an optimum or substantial growth capacity at warmer temperature**. A useful contemporary operational definition is growth at approximately **4°C with an optimum above 20°C**. Examples include *Pseudomonas* spp., *Listeria monocytogenes*, *Yersinia enterocolitica*, and *Aeromonas hydrophila* (ramon2023ageneraloverview pages 1-2).

This is a facultative thermal phenotype, not merely residence in a cold habitat. The phenotype should normally be supported by growth curves, colony formation, biomass increase, or another multiplication assay at both low and non-low temperatures.

### Boundaries

- **Psychrophile:** low-temperature growth is optimal or effectively obligate; obligate psychrophiles commonly have upper growth limits around 10–20°C. By contrast, psychrotolerant organisms retain a broader, warmer growth range (moyer2017psychrophilesandpsychrotrophs pages 2-3).
- **Cold-shock tolerant:** survival after an abrupt downshift does not establish sustained low-temperature growth.
- **Freeze–thaw resistant:** viability after freezing and thawing is not equivalent to multiplication at low temperature.
- **Cryotolerant/dormant:** persistence or metabolic signatures below 0°C do not by themselves demonstrate growth.
- **Cold-adapted enzyme:** activity of an isolated enzyme at low temperature does not establish organism-level psychrotolerance.
- **Genomic prediction:** possession or induction of desaturases, cold-shock proteins, helicases, compatible-solute systems, or antifreeze proteins is mechanistic support, not sufficient phenotype evidence.

The distinction is assay-sensitive. Medium, salinity, oxygenation, inoculum history, duration, and the selected “low” temperature can change the classification. The literature also uses *psychrotroph*, *psychrotolerant*, and *facultative psychrophile* inconsistently; therefore, measured cardinal growth temperatures should be retained whenever available.

## 2. Current mechanistic model

The most defensible causal architecture is modular rather than a single universal pathway:

1. **Low temperature reduces molecular motion** and pushes membrane phospholipids from a liquid-crystalline state toward a gel state.
2. **Membrane rigidification is sensed**, in some taxa through membrane-associated two-component systems.
3. **Lipid remodeling** increases low-melting-point acyl chains—cis-unsaturated, polyunsaturated, short-chain, or appropriate branched-chain fatty acids—restoring membrane fluidity and transport/respiratory function.
4. Cold stabilizes RNA secondary structures and impairs transcription, translation, ribosome maturation, and protein folding.
5. **Cold-shock RNA chaperones, DEAD-box helicases, RNases, ribosome-biogenesis factors, and molecular chaperones** preserve gene expression.
6. Compatible solutes, extracellular polymers, and ice-binding proteins can stabilize proteins and membranes or alter extracellular freezing behavior.
7. Catalase, superoxide dismutase, and related systems mitigate cold-associated oxidative stress.
8. The combined effects enable sustained low-temperature metabolism and growth while preserving growth at warmer temperatures.

A 2023 authoritative review emphasizes that cooling changes membranes from liquid-crystalline to gel phase and identifies the response as homeoviscous adaptation. It lists increased unsaturation, shorter chains, branched chains, hopanoid remodeling, glycolipids, and pigments as alternative solutions rather than a universal signature (ramon2023ageneraloverview pages 2-4).

## 3. Candidate nodes grouped by type

### Trait and environmental nodes

- psychrotolerant — **METPO:1000618**
- low-temperature growth — label-only phenotype node
- low temperature / temperature downshift — label-only experimental factor
- refrigeration temperature — label-only application-specific condition
- extracellular water — **CHEBI:15377**
- freeze–thaw exposure — label-only; should not be conflated with the target

### Cellular structures and physical states

- cytoplasmic membrane — use a taxon-appropriate GO cellular-component term after organismal context is fixed
- liquid-crystalline membrane state — label-only
- gel-state/rigidified membrane — label-only
- membrane fluidity — label-only quantitative property
- cell wall — **GO:0005618**, where taxonomically applicable
- extracellular polymeric matrix — label-only
- ribosome — ground to the appropriate bacterial/archaeal/eukaryotic GO term during taxon-specific curation

### Pathways and biological processes

- homeoviscous adaptation — label-only
- lipid metabolic process — **GO:0006629**
- fatty-acid biosynthetic process — **GO:0006633**
- unsaturated-fatty-acid synthesis/desaturation — label-only pending exact GO selection
- RNA binding — **GO:0003723**
- helicase activity — **GO:0004386**
- translation — **GO:0006412**
- protein folding — **GO:0006457**
- response to oxidative stress — **GO:0006979**
- compatible-solute transport/accumulation — label-only until a specific transport system is selected
- exopolysaccharide biosynthesis — label-only
- DNA repair and replication-fork recovery — label-only in the general graph; taxon-specific in *Pseudomonas syringae*

### Genes, proteins, enzymes, and complexes

**Strong taxon-specific candidates**

- **DesK–DesR two-component system**, *Bacillus subtilis* — membrane-state sensor and transcriptional regulator
- **Des acyl-lipid desaturase**, *B. subtilis*
- **CspA, CspB, CspD**, *L. monocytogenes* — cold-shock proteins; CspA has the strongest cold-growth phenotype
- **Aat/aspartate aminotransferase**, *P. syringae* Lz4W
- **RNA polymerase**, *P. syringae* Lz4W
- **TrmE tRNA-modification GTPase**, *P. syringae* Lz4W

**Provisional candidates**

- DEAD-box RNA helicases
- RNase R/degradosome components
- GroEL and other molecular chaperones
- catalase and superoxide dismutase; oxidoreductase activity **GO:0016491**
- FabA/FabB/FabR system in Gram-negative bacteria
- branched-chain fatty-acid synthesis enzymes, including FabH/KAS-related enzymes
- trehalose/maltose transporter components ThuF/SugA and ThuG/SugB in *P. fragi* D12
- pili/fimbrial proteins D12GL002239–D12GL002241 in *P. fragi* D12

Exact UniProt, EC, KEGG, or Rhea identifiers should only be added after strain-specific sequence verification.

### Chemicals and metabolites

- glycine betaine — **CHEBI:30746**
- trehalose — **CHEBI:17750**
- glycerol — **CHEBI:17754**
- sucrose — **CHEBI:17992**
- mannitol and sorbitol — retain label-only until identifier verification
- saturated fatty acids, cis-monounsaturated fatty acids, polyunsaturated fatty acids, iso- and anteiso-branched fatty acids — ground individual molecular species only when the experiment identifies them
- reactive oxygen species — label-only collective node; use specific CHEBI entities when measured

Recent reviews describe glycine betaine, trehalose, glycerol, sucrose, mannitol, and sorbitol as cryoprotective compatible solutes that lower freezing point, stabilize macromolecules, or scavenge radicals, but these are mostly general/review-level claims rather than universal causal determinants of psychrotolerance (purwar2024adaptationsofpsychrophilic pages 10-11).

## 4. Candidate causal edges

The table below gives the compact curation triage. High-priority edges have intervention, regulatory, or strong biophysical support; medium-priority edges are association-based or require taxonomic qualification.

| Priority | candidate causal triple | evidence class | taxon/assay | DOI | curation decision |
|---|---|---|---|---|---|
| High | low temperature -> membrane gel/rigidification | review-level biophysical mechanism | general microbial membranes; phase-transition/homeoviscous-adaptation framework | 10.1007/s42770-023-01057-4 | Curate as broad environmental-to-process edge only; not specific to psychrotolerant taxa without additional direct assay support (ramon2023ageneraloverview pages 2-4) |
| High | reduced membrane fluidity -> DesK/DesR activates des | direct regulatory genetics | *Bacillus subtilis*; des-lacZ reporter at 37 C with branched-chain precursor manipulation | 10.1046/j.1365-2958.2002.03103.x | Curate as taxon-specific mechanistic subgraph, not as universal psychrotolerant mechanism (cybulski2002mechanismofmembrane pages 4-6, cybulski2002mechanismofmembrane pages 1-2) |
| High | des expression -> unsaturated fatty acid synthesis | direct mechanistic genetics/biochemistry | *Bacillus subtilis*; Des acyl-lipid desaturase pathway | 10.1046/j.1365-2958.2002.03103.x | Curate as taxon-specific edge; strong support in *Bacillus* only (cybulski2002mechanismofmembrane pages 1-2) |
| High | unsaturated fatty acids -> increased membrane fluidity | direct mechanistic interpretation plus lipid data | *Bacillus subtilis* and broader cold-adapted bacteria | 10.1046/j.1365-2958.2002.03103.x | Curate with taxon-specific note; broadly plausible but strongest causal chain is in *Bacillus* (cybulski2002mechanismofmembrane pages 1-2, ramon2023ageneraloverview pages 2-4) |
| Medium | branched/unsaturated low-melting fatty acids -> membrane fluidity | quantitative lipid association | psychrotolerant glacier isolates grown at 5, 15, 25, 35 C | 10.3389/fmicb.2020.00824 | Curate cautiously as physiology-level edge; supports membrane-fluidity role but not single-gene causation (hassan2020temperaturedrivenmembrane pages 6-7, hassan2020temperaturedrivenmembrane pages 2-3) |
| High | CspA -> growth at 4 C | direct deletion phenotype | *Listeria monocytogenes* EGDe; single/double/triple csp deletions | 10.3390/microorganisms9051061 | Curate as taxon-specific direct edge; strong mutant evidence (muchaamba2021listeriamonocytogenescold pages 4-5) |
| High | CspA -> growth at 10 C | direct deletion phenotype | *Listeria monocytogenes* EGDe; single/double/triple csp deletions | 10.3390/microorganisms9051061 | Curate as taxon-specific direct edge; strong mutant evidence (muchaamba2021listeriamonocytogenescold pages 4-5) |
| Medium | low temperature -> fatty acid metabolism / compatible-solute / catalase transcription | expression-associated | *Pseudomonas fragi* D12; RNA-seq after 30->15 C shift | 10.3389/fmicb.2023.1215837 | Do not curate as causal core yet; keep as associative candidate pending perturbation evidence (bao2023miningofkey pages 9-11, bao2023miningofkey pages 1-2) |
| Medium | low temperature -> cold shock protein / helicase transcription | expression-associated | *Pseudomonas fragi* D12; RNA-seq after 15->4 C shift | 10.3389/fmicb.2023.1215837 | Do not curate as direct edge yet; transcriptomic association only (bao2023miningofkey pages 9-11, bao2023miningofkey pages 1-2) |
| Medium | aat -> low-temperature growth | direct gene inactivation phenotype | psychrotolerant *Pseudomonas syringae* Lz4W; low-temperature growth retardation after aat inactivation | 10.1111/1462-2920.15304 | Curate as taxon-specific direct edge with uncertainty on mechanism breadth (pavankumar2021molecularinsightsinto pages 7-10) |


*Table: This table prioritizes the strongest candidate causal edges for curating psychrotolerance (METPO:1000618), separating direct mutant-based evidence from broader physiological associations. It is useful for deciding which claims are ready for TraitMech curation and which should remain provisional.*

### Expanded edge evidence with supporting snippets

| Proposed subject–predicate–object | Reference and supporting snippet | Evidence assessment and curation note |
|---|---|---|
| **low temperature — decreases — membrane fluidity** | Ramón et al. (2023): “When the temperature drops, the liquid-crystalline phase changes to the gel phase,” with molecules “tightly packed” and showing reduced motion (ramon2023ageneraloverview pages 2-4). | **Curatable general biophysical edge.** It is not specific to psychrotolerant organisms but is the initiating stressor in the graph. |
| **decreased membrane fluidity — activates through — DesK–DesR signaling** | Cybulski et al. (2002) state that low-temperature activation is controlled by membrane-associated DesK and soluble DesR and propose that “both a decrease in membrane fluidity at constant temperature and a temperature downshift induce des by the same mechanism” (cybulski2002mechanismofmembrane pages 1-2). | **Strong but taxon-specific.** Curate under a *B. subtilis* mechanism module, not as universal. |
| **DesK–DesR — activates transcription of — des** | In desR-null and desK/desR-null backgrounds, des-reporter activity remained approximately 3.3–4.3 units; expression of desKR increased activity to 34.8–51.0 units without isoleucine. The authors conclude that both partners mediate signaling (cybulski2002mechanismofmembrane pages 4-6). | **Direct regulatory evidence.** Assay was at 37°C with lipid-precursor manipulation, demonstrating membrane-state sensing rather than low-temperature growth itself. |
| **des expression/Des enzyme — increases — unsaturated-fatty-acid synthesis** | The Des pathway “regulates the expression of the acyl-lipid desaturase, Des, thereby controlling the synthesis of unsaturated fatty acids from saturated phospholipid precursors” (cybulski2002mechanismofmembrane pages 1-2). | **Curatable, *Bacillus*-specific biochemical edge.** |
| **unsaturated and low-melting fatty acids — increase/maintain — membrane fluidity** | Homeoviscous adaptation uses increased monounsaturated, polyunsaturated, and branched-chain fatty acids relative to straight saturated analogues to provide adequate fluidity (hassan2020temperaturedrivenmembrane pages 2-3). | **Curatable process-level edge**, but represent lipid classes rather than asserting that every taxon uses all classes. |
| **low temperature — increases — branched and unsaturated membrane-lipid remodeling** | In glacier isolates, branched saturated/monounsaturated lipids in several Gram-positive strains fell from about **90% at 5–15°C to <1% at 35°C**; straight saturated fatty acids rose from **0.4–2% to 1.8–51%**. In Gram-negative strains, cis-16:1 generally decreased as temperature increased (hassan2020temperaturedrivenmembrane pages 6-7). | **Quantitative physiological association.** Strong support for remodeling, but no single-gene perturbation; species-specific patterns vary. |
| **CspA — enables — growth at 4°C and 10°C** | *L. monocytogenes* EGDe ∆cspA, ∆cspAB, ∆cspAD, and ∆cspABD mutants “are all not capable of growth at both 10°C and 4°C”; all mutants could reach stationary phase at 15°C within 72 h (muchaamba2021listeriamonocytogenescold pages 4-5). | **High-confidence direct edge.** Curate as *L. monocytogenes*-specific. The temperature threshold and strain should be retained. |
| **low temperature — induces — cspA expression** | At 4°C, cspA was upregulated relative to 37°C and was **5.1-fold and 3.1-fold** higher than cspB and cspD, respectively (muchaamba2021listeriamonocytogenescold pages 4-5). | **Expression-supported edge.** Curatable as regulation, but not itself proof that induction causes the phenotype; the deletion result supplies causality. |
| **cold-shock proteins — reduce — inhibitory mRNA secondary structure** | The review describes Csps as chaperones that “adjust or melt mRNA secondary structure, allowing translation to continue” under cold stress (muchaamba2021listeriamonocytogenescold pages 4-5). | **Mechanistically plausible, review-supported.** Curate with “supports/enables translation” rather than a direct organism-level phenotype unless primary biochemical evidence is attached. |
| **aat/aspartate aminotransferase — promotes — low-temperature growth** | In psychrotolerant *P. syringae* Lz4W, “aat gene inactivation retards growth at low temperature,” implicating aspartate metabolism (pavankumar2021molecularinsightsinto pages 7-10). | **Direct but taxon-specific.** Curate with uncertainty because the retrieved source is a review of the primary experiment and the exact effect size was unavailable. |
| ***P. syringae* Lz4W RNA polymerase — enables — transcription at 0°C** | Its RNA polymerase retained transcriptional ability at 0°C, unlike the compared *Pseudomonas* and *E. coli* enzymes (pavankumar2021molecularinsightsinto pages 7-10). | **Biochemical comparative evidence.** Curate as a taxon-specific molecular-function edge, not as proof of whole-cell psychrotolerance by itself. |
| **low temperature — increases — trmE expression and cold-active TrmE function** | *P. syringae* TrmE was upregulated at low temperature; its GTPase optimum was **12–18°C**, versus approximately **30°C** for mesophilic homologues (pavankumar2021molecularinsightsinto pages 7-10). | **Expression plus biochemical adaptation.** Useful supporting node; causal requirement for growth was not shown in the retrieved evidence. |
| **30→15°C shift — is associated with — fatty-acid degradation, polysaccharide, compatible-solute, and catalase transcription** | In *P. fragi* D12, those gene groups were upregulated after a 2-h shift. The authors infer shorter average fatty-acid chains and increased compatible solutes/catalase (bao2023miningofkey pages 9-11). | **Uncertain/association only.** Do not encode “causes psychrotolerance” without perturbation and metabolite/ROS measurements. |
| **15→4°C shift — is associated with — unsaturated-fatty-acid, CSP, helicase, and transcription-factor expression** | Crucial unsaturated-fatty-acid genes and “the majority of genes associated with cold shock proteins, helicases, and transcription molecules were up-regulated” (bao2023miningofkey pages 9-11). | **Uncertain/association only.** Appropriate as `associated_with` or provenance for candidate nodes, not a direct causal edge. |
| **low temperature — changes — global transcriptional program in *P. fragi* D12** | At a >2-fold, q≤0.05 threshold, the 30-versus-15°C comparison included **750 upregulated and 542 downregulated genes**; the 15-versus-4°C comparison included **1,003 upregulated and 1,088 downregulated genes** (bao2023miningofkey pages 9-11). | **Recent quantitative systems evidence.** It establishes a large, temperature-dependent response but not individual causal determinants. |
| **compatible solutes/EPS/ice-binding proteins — protect — membranes, proteins, or extracellular water state** | Reviews report glycine betaine, trehalose, glycerol and related solutes as stabilizers/free-radical scavengers, and antifreeze proteins or EPS as freezing modifiers (moyer2017psychrophilesandpsychrotrophs pages 2-3, purwar2024adaptationsofpsychrophilic pages 10-11). | **Review-level and context-dependent.** Split into compound-specific edges only where uptake/knockout or supplementation evidence exists. |

## 5. Recommended graph architecture

A robust TraitMech representation should use a **small conserved core** with taxon-specific branches:

**Core physiology**

`low temperature → reduced membrane molecular motion → membrane rigidification → lipid remodeling → restored membrane fluidity → membrane transport/respiration → low-temperature growth → METPO:1000618`

**RNA/protein-homeostasis branch**

`low temperature → stabilized RNA secondary structure / impaired ribosome function → CSPs and RNA helicases → restored transcription/translation → low-temperature growth`

**Protection branch**

`low temperature → osmotic/freezing/oxidative stress → compatible-solute accumulation + extracellular polymers + ROS detoxification → macromolecular and membrane stability → low-temperature growth`

**Taxon-specific examples**

- *B. subtilis*: `membrane rigidification → DesK/DesR → des → unsaturated fatty acids → membrane fluidity`.
- *L. monocytogenes*: `CspA → translation/stress fitness → growth at 4–10°C`.
- *P. syringae* Lz4W: `aat/aspartate metabolism → low-temperature growth`; cold-active RNA polymerase and TrmE provide supporting molecular adaptations.
- *P. fragi* D12: retain RNA-seq modules as provisional until genetic or biochemical perturbation tests are available.

This avoids incorrectly presenting a mechanism from one bacterium as a defining mechanism of every psychrotolerant microbe.

## 6. Recent developments, applications, and expert analysis

### 2023–2024 research

The strongest recent advance is a shift from lists of “cold genes” toward temperature-resolved, multi-module responses. The 2023 *P. fragi* D12 study identified **124 potential cold-adaptation genes**, including **19 unique candidate genes**, and found distinct programs for 30→15°C versus 15→4°C shifts. Nevertheless, the study is primarily comparative-genomic and transcriptomic; its pili, compatible-solute, catalase, helicase, and lipid claims remain hypotheses until perturbation experiments are performed (bao2023miningofkey pages 1-2, bao2023miningofkey pages 6-7, bao2023miningofkey pages 9-11).

A 2024 review consolidates membrane remodeling, cold-shock/ice-binding proteins, compatible solutes, and oxidative defenses but provides limited new mutant evidence. It is useful for node discovery, not for assigning organism-independent causal edges (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 3-4).

Expert synthesis in 2023 describes cold adaptation as **multifactorial**, with membrane state, protein flexibility, RNA metabolism, cryoprotection, and metabolic regulation interacting. This supports a modular causal graph rather than a single linear gene pathway (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 8-9, ramon2023ageneraloverview pages 2-4).

### Real-world relevance

- **Food safety:** psychrotolerant pathogens can multiply near refrigeration temperatures. *L. monocytogenes*, *Y. enterocolitica*, and *A. hydrophila* are highlighted as prominent cold-growing foodborne pathogens; mechanistic knowledge can support cold-chain control and intervention design (ramon2023ageneraloverview pages 2-4).
- **Food spoilage:** *Pseudomonas fragi* and related psychrotrophs remain metabolically active during chilled storage. Candidate targets include membrane adaptation, RNA chaperones, and compatible-solute transport.
- **Cold-region bioremediation:** *P. fragi* D12 contained extensive carbohydrate and xenobiotic-metabolism annotations, suggesting potential low-temperature remediation, but application performance was not established by the retrieved study (bao2023miningofkey pages 6-7).
- **Industrial biotechnology:** cold-active enzymes permit reactions at low temperature, potentially reducing energy input and heat damage. This application derives more directly from enzyme-level cold activity than from organism-level psychrotolerance (moyer2017psychrophilesandpsychrotrophs pages 2-3, ramon2023ageneraloverview pages 8-9).
- **Agriculture and cryosphere ecology:** psychrotolerant plant-growth-promoting strains may remain functional in cold soils; however, plant-benefit traits and psychrotolerance should be represented separately.
- **Astrobiology:** subzero metabolism, cold-active transcription, and broad thermal ranges inform habitability models, but survival or inferred metabolism below −15°C must not be labeled growth without direct evidence (moyer2017psychrophilesandpsychrotrophs pages 2-3).

## 7. Curation warnings

1. **Do not equate isolation source with phenotype.** Antarctic, glacier, permafrost, refrigerated-food, or deep-sea origin is insufficient.
2. **Require organism-level multiplication.** Survival, respiration, enzyme activity, RNA induction, or membrane remodeling alone does not prove psychrotolerance.
3. **Store cardinal temperatures.** Minimum, optimum, and maximum growth temperatures are more reproducible than categorical labels.
4. **Avoid universal gene requirements.** Csp redundancy differs markedly among *Listeria*, *Bacillus*, and *E. coli*; DesK–DesR is not a universal bacterial cold sensor (muchaamba2021listeriamonocytogenescold pages 4-5).
5. **Do not convert RNA-seq correlation into causality.** The 2023 *P. fragi* D12 results are short-term, 2-h expression responses and lack knockouts or complementation (bao2023miningofkey pages 9-11).
6. **Separate membrane composition from fluidity measurement.** Lipid abundance is often a proxy; direct anisotropy or phase-state measurements are stronger.
7. **Do not assume all unsaturation patterns are identical.** Gram-positive and Gram-negative taxa use different combinations of cis-unsaturated, branched, short-chain, or polyunsaturated lipids (hassan2020temperaturedrivenmembrane pages 6-7).
8. **Compatible solutes need compound-specific evidence.** Gene annotation does not establish transport, intracellular accumulation, or a contribution to cold growth.
9. **Antifreeze and ice-nucleation proteins have different effects.** They should not be merged into a generic “antifreeze” node.
10. **Psychrophile data are supporting, not automatically transferable.** Obligate psychrophiles may possess constitutive adaptations or warm sensitivity absent from psychrotolerant organisms.
11. **Ground strain-specific proteins only after sequence verification.** Gene symbols such as `cspA`, `des`, `aat`, or `trmE` are not globally unique identifiers.
12. **Do not curate pili as causal yet.** Upregulation of three *P. fragi* D12 pilus-associated genes is intriguing but the proposed EPS/freezing-point mechanism is explicitly speculative (bao2023miningofkey pages 9-11).

## 8. DOI-first bibliography

1. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology* 54, 2259–2287. Published July 2023. DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4). (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4)
2. Bao C et al. **Mining of key genes for cold adaptation from *Pseudomonas fragi* D12 and analysis of its cold-adaptation mechanism.** *Frontiers in Microbiology* 14. Published July 2023. DOI: [10.3389/fmicb.2023.1215837](https://doi.org/10.3389/fmicb.2023.1215837). (bao2023miningofkey pages 1-2, bao2023miningofkey pages 9-11)
3. Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory & Technology*, 168–188. Published October 2024. DOI: [10.37256/amtt.5220244537](https://doi.org/10.37256/amtt.5220244537). (purwar2024adaptationsofpsychrophilic pages 10-11)
4. Muchaamba F, Stephan R, Tasara T. ***Listeria monocytogenes* Cold Shock Proteins: Small Proteins with a Huge Impact.** *Microorganisms* 9, 1061. Published May 2021. DOI: [10.3390/microorganisms9051061](https://doi.org/10.3390/microorganisms9051061). (muchaamba2021listeriamonocytogenescold pages 4-5)
5. Pavankumar TL, Mittal P, Hallsworth JE. **Molecular insights into the ecology of a psychrotolerant *Pseudomonas syringae*.** *Environmental Microbiology* 23, 3665–3681. Published November 2021. DOI: [10.1111/1462-2920.15304](https://doi.org/10.1111/1462-2920.15304). (pavankumar2021molecularinsightsinto pages 7-10)
6. Hassan N et al. **Temperature Driven Membrane Lipid Adaptation in Glacial Psychrophilic Bacteria.** *Frontiers in Microbiology* 11, 824. Published May 2020. DOI: [10.3389/fmicb.2020.00824](https://doi.org/10.3389/fmicb.2020.00824). (hassan2020temperaturedrivenmembrane pages 6-7, hassan2020temperaturedrivenmembrane pages 2-3)
7. Cybulski LE et al. **Mechanism of membrane fluidity optimization: isothermal control of the *Bacillus subtilis* acyl-lipid desaturase.** *Molecular Microbiology* 45, 1379–1388. Published September 2002. DOI: [10.1046/j.1365-2958.2002.03103.x](https://doi.org/10.1046/j.1365-2958.2002.03103.x). (cybulski2002mechanismofmembrane pages 4-6, cybulski2002mechanismofmembrane pages 1-2)
8. Moyer CL, Collins RE, Morita RY. **Psychrophiles and Psychrotrophs.** *Reference Module in Life Sciences*. Published January 2017. DOI: [10.1016/B978-0-12-809633-8.02282-2](https://doi.org/10.1016/B978-0-12-809633-8.02282-2). (moyer2017psychrophilesandpsychrotrophs pages 2-3, moyer2017psychrophilesandpsychrotrophs pages 3-5)
9. D’Amico S et al. **Psychrophilic microorganisms: challenges for life.** *EMBO Reports* 7, 385–389. Published April 2006. DOI: [10.1038/sj.embor.7400662](https://doi.org/10.1038/sj.embor.7400662). This is foundational support for the membrane-fluidity challenge in the existing graph.
10. Ryu SH et al. ***Pseudomonas guineae* sp. nov., a novel psychrotolerant bacterium.** *International Journal of Systematic and Evolutionary Microbiology*. DOI: [10.1099/ijs.0.65141-0](https://doi.org/10.1099/ijs.0.65141-0). This remains an organism-example source rather than mechanistic evidence.

References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

2. (moyer2017psychrophilesandpsychrotrophs pages 2-3): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.

3. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

4. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

5. (cybulski2002mechanismofmembrane pages 4-6): L. Cybulski, D. Albanesi, M. C. Mansilla, S. Altabe, P. Aguilar, and D. de Mendoza. Mechanism of membrane fluidity optimization: isothermal control of the bacillus subtilis acyl‐lipid desaturase. Molecular Microbiology, Sep 2002. URL: https://doi.org/10.1046/j.1365-2958.2002.03103.x, doi:10.1046/j.1365-2958.2002.03103.x. This article has 185 citations and is from a domain leading peer-reviewed journal.

6. (cybulski2002mechanismofmembrane pages 1-2): L. Cybulski, D. Albanesi, M. C. Mansilla, S. Altabe, P. Aguilar, and D. de Mendoza. Mechanism of membrane fluidity optimization: isothermal control of the bacillus subtilis acyl‐lipid desaturase. Molecular Microbiology, Sep 2002. URL: https://doi.org/10.1046/j.1365-2958.2002.03103.x, doi:10.1046/j.1365-2958.2002.03103.x. This article has 185 citations and is from a domain leading peer-reviewed journal.

7. (hassan2020temperaturedrivenmembrane pages 6-7): Noor Hassan, Alexandre M. Anesio, Muhammad Rafiq, Jens Holtvoeth, Ian Bull, Abdul Haleem, Aamer Ali Shah, and Fariha Hasan. Temperature driven membrane lipid adaptation in glacial psychrophilic bacteria. Frontiers in Microbiology, May 2020. URL: https://doi.org/10.3389/fmicb.2020.00824, doi:10.3389/fmicb.2020.00824. This article has 129 citations and is from a peer-reviewed journal.

8. (hassan2020temperaturedrivenmembrane pages 2-3): Noor Hassan, Alexandre M. Anesio, Muhammad Rafiq, Jens Holtvoeth, Ian Bull, Abdul Haleem, Aamer Ali Shah, and Fariha Hasan. Temperature driven membrane lipid adaptation in glacial psychrophilic bacteria. Frontiers in Microbiology, May 2020. URL: https://doi.org/10.3389/fmicb.2020.00824, doi:10.3389/fmicb.2020.00824. This article has 129 citations and is from a peer-reviewed journal.

9. (muchaamba2021listeriamonocytogenescold pages 4-5): Francis Muchaamba, Roger Stephan, and Taurai Tasara. Listeria monocytogenes cold shock proteins: small proteins with a huge impact. Microorganisms, 9:1061, May 2021. URL: https://doi.org/10.3390/microorganisms9051061, doi:10.3390/microorganisms9051061. This article has 56 citations.

10. (bao2023miningofkey pages 9-11): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

11. (bao2023miningofkey pages 1-2): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

12. (pavankumar2021molecularinsightsinto pages 7-10): Theetha L. Pavankumar, Pragya Mittal, and John E. Hallsworth. Molecular insights into the ecology of a psychrotolerant <i>pseudomonas syringae</i>. Environmental Microbiology, 23:3665-3681, Nov 2021. URL: https://doi.org/10.1111/1462-2920.15304, doi:10.1111/1462-2920.15304. This article has 35 citations and is from a domain leading peer-reviewed journal.

13. (bao2023miningofkey pages 6-7): Changjie Bao, Muzi Li, Xuhui Zhao, Jia Shi, Yehui Liu, Na Zhang, Yuqi Zhou, Jie Ma, Guang Chen, Sitong Zhang, and Huan Chen. Mining of key genes for cold adaptation from pseudomonas fragi d12 and analysis of its cold-adaptation mechanism. Frontiers in Microbiology, Jul 2023. URL: https://doi.org/10.3389/fmicb.2023.1215837, doi:10.3389/fmicb.2023.1215837. This article has 22 citations and is from a peer-reviewed journal.

14. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

15. (ramon2023ageneraloverview pages 8-9): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.

16. (moyer2017psychrophilesandpsychrotrophs pages 3-5): Craig L. Moyer, R. Eric Collins, and Richard Y. Morita. Psychrophiles and Psychrotrophs. Elsevier, Jan 2017. URL: https://doi.org/10.1016/b978-0-12-809633-8.02282-2, doi:10.1016/b978-0-12-809633-8.02282-2. This article has 187 citations.