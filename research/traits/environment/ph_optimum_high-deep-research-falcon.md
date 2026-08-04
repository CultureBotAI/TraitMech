---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:35:02.607273'
end_time: '2026-08-04T02:44:41.361543'
duration_seconds: 578.75
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH optimum high
  trait_identifier: METPO:1000458
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_optimum_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH optimum phenotype with the best-growth external pH above approximately
    8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
  parent_traits: METPO:1000331
  synonyms: Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
  evidence_summary: 'DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review
    supports alkaliphile and extreme-alkaliphile physiology growing at high external
    pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review
    supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism
    sustaining the proton motive force at high external pH.)'
  causal_graph_summary: 'ph_optimum_high_alkaliphile_setpoint: 15 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000458
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH above approximately 8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile and extreme-alkaliphile physiology growing at high external pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism sustaining the proton motive force at high external pH.)
- **Existing causal graph summary:** ph_optimum_high_alkaliphile_setpoint: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **pH optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_high.yaml`.

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
- **Trait label:** pH optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000458
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH optimum phenotype with the best-growth external pH above approximately 8, corresponding to alkaliphilic or extreme-alkaliphilic physiology.
- **Parent traits:** METPO:1000331
- **Synonyms:** Alkali Tolerant, Alkaliphile, Extreme Alkaliphile, pHO_8_to_14
- **Existing evidence:** DOI:10.1038/nrmicro2549: alkaliphiles (pH-homeostasis review supports alkaliphile and extreme-alkaliphile physiology growing at high external pH.) | DOI:10.1016/j.tim.2007.02.005: proton motive force (pH-homeostasis review supports Na+/H+ antiporters re-importing protons as the alkaliphile mechanism sustaining the proton motive force at high external pH.)
- **Existing causal graph summary:** ph_optimum_high_alkaliphile_setpoint: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **pH optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_optimum_high.yaml`.

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


# Curation-focused research report: microbial **pH optimum high**

## 1. Scope summary

**Target trait:** **“METPO:1000458”** — *pH optimum high*  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Parent:** METPO:1000331

This trait should encode an organism-level **optimal-growth phenotype**: the external pH at which measured growth is maximal lies above approximately pH 8. In the classical alkaliphile literature, the operational threshold is usually stricter: alkaliphiles grow optimally above pH 9, commonly around pH 10–10.5, and extreme strains may grow at pH 12–13. The supplied METPO definition is therefore somewhat broader than conventional “alkaliphile” usage and can include organisms whose optimum is only mildly alkaline. (preiss2015alkaliphilicbacteriawith pages 1-2, maksimova2024metabolicandmorphological pages 1-2)

A useful literature-based subdivision is:

- **Facultative alkaliphile:** optimal growth at approximately pH 10 or higher but also capable of near-neutral growth.
- **Obligate alkaliphile:** requires alkaline conditions; one recent formulation specifies optimal growth above pH 10 and no growth below pH 9.
- **Alkali-tolerant organism:** optimum remains neutral or mildly alkaline—reported as pH 7–9 in the 2024 study—even though the organism can withstand some alkaline exposure.
- **Extreme alkaliphile:** an alkaliphile capable of growth at exceptionally high external pH, sometimes pH 12–13. (preiss2015alkaliphilicbacteriawith pages 1-2, maksimova2024metabolicandmorphological pages 1-2)

Accordingly, **survival, metabolic activity, or growth after transient alkaline shock is not sufficient** to assert “METPO:1000458.” The primary evidence should be a growth-rate, biomass-yield, colony-formation, or comparable growth curve measured across multiple buffered pH conditions, with the maximum above the METPO threshold. Medium composition, buffering, temperature, salinity, carbon source, oxygen status, and inoculum phase should be retained as assay context because they can shift the apparent optimum.

The best-characterized mechanistic exemplar is *Bacillus pseudofirmus* OF4. It grows optimally near external pH 10.5 while maintaining cytoplasmic pH about 8.3; at external pH 7.5–9.5 it maintains cytoplasmic pH near 7.5. This demonstrates that the trait is not equivalent to an alkaline cytoplasm: the defining adaptation is growth in an alkaline **external** environment while keeping the cytoplasm substantially less alkaline. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 1-3)

## 2. Current mechanistic model

High external pH makes protons scarce outside the membrane and reverses the usual transmembrane pH-gradient contribution to the proton-motive force: the cytoplasm is more acidic than the environment. This reversed ΔpH opposes inward proton flow and reduces the bulk PMF available for proton-coupled ATP synthesis. Alkaliphiles compensate through a network rather than a single “alkaliphily gene”: electrogenic cation/proton antiport, a sodium-recycling circuit, high membrane potential, respiratory proton pumping, adapted ATP synthase, and cell-surface features that may retard proton loss. (preiss2015alkaliphilicbacteriawith pages 1-2, krulwich2011molecularaspectsof pages 1-3)

The central, strongly supported module in aerobic alkaliphilic bacilli is the **Mrp-family Na+/H+ antiporter**. It exports Na+ while importing a greater number of H+, thereby acidifying the cytoplasm and using membrane potential to drive pH homeostasis. A point mutation in *mrpA* of *B. halodurans* C-125 eliminated both alkaline pH homeostasis and the alkaliphile phenotype; all seven Mrp components are reported as required for active-complex formation. (krulwich2011molecularaspectsof pages 12-14, preiss2015alkaliphilicbacteriawith pages 3-4)

Continuous antiport requires Na+ to re-enter the cell. In *B. pseudofirmus* OF4, documented routes include Na+/solute symporters, the voltage-gated NaVBP channel, and the Na+-driven MotPS flagellar stator/channel. These form a **sodium cycle** linking nutrient uptake, motility, ion balance, and proton acquisition. These routes should be represented as parallel, taxon-dependent contributors rather than universal requirements of every alkaliphile. (krulwich2011molecularaspectsof pages 27-28, krulwich2011molecularaspectsof pages 22-23, takahashi2018ahydrophobicsmall pages 1-2)

Aerobic alkaliphilic bacilli nevertheless use proton-pumping respiration and proton-coupled F1Fo ATP synthase. Alkaliphile-specific residues in ATP-synthase a- and c-subunits improve high-pH function and limit proton leak. In *B. pseudofirmus* OF4, replacing a-subunit K180 with the neutralophile consensus glycine reduced malate-supported growth at pH 10.5 to 18% of wild type, versus 86% at pH 7.5, and caused a major ATP-synthesis defect. This is unusually strong residue-to-phenotype evidence. (krulwich2011molecularaspectsof pages 22-23, preiss2015alkaliphilicbacteriawith pages 7-8)

Acidic secondary cell-wall polymers, teichuronic acids, and the SlpA S-layer contribute to pH homeostasis. Loss of negatively charged surface polymers reduces alkaliphily, but the frequently proposed explanation—surface proton capture or delayed equilibration with bulk medium—remains partly inferential. Similarly, proximity or direct proton transfer between caa3-type terminal oxidase and ATP synthase is mechanistically attractive but has not been demonstrated as a stable direct complex. (krulwich2011molecularaspectsof pages 5-6, preiss2015alkaliphilicbacteriawith pages 12-13, takahashi2018ahydrophobicsmall pages 1-2)

## 3. Candidate causal-graph nodes

### Trait and environmental nodes

- **pH optimum high:** **METPO:1000458**
- **External alkaline pH / alkaline environment:** label-only unless an approved ENVO term matching the intended granularity is selected during ontology review.
- **Extracellular proton scarcity:** label-only process/state.
- **Soda lake**, **alkaline spring**, **serpentinizing ecosystem:** candidate ENVO-grounded habitat nodes; use only where a graph branch explicitly represents natural selective context.
- **NaCl concentration / salinity:** experimental-factor node; do not merge high pH with haloalkaliphily.
- **Buffered growth medium**, carbon source, oxygen availability, temperature, and growth phase: assay-context nodes.

### Chemical and energetic nodes

- **Proton:** CHEBI:15378.
- **Sodium cation:** CHEBI:29101.
- **Potassium cation:** CHEBI:29103.
- **ATP:** CHEBI:15422.
- **ADP:** CHEBI:16761.
- **Phosphate:** CHEBI:18367.
- **Proton-motive force**, membrane potential (Δψ), transmembrane ΔpH, cytoplasmic pH, and local membrane-surface proton concentration: label-only physical-state nodes unless the project already has approved ontology mappings.

### Transport proteins and complexes

- **MrpA–MrpG Na+/H+ antiporter complex:** label-only complex, with organism-specific gene members. Candidate GO molecular function: **GO:0015385**, sodium:proton antiporter activity.
- **Na+/solute symporters:** family-level label; ground individual transporters only when substrate and locus are known.
- **NaVBP voltage-gated sodium channel:** label-only protein node; use organism-specific accession when curated.
- **MotPS sodium-driven flagellar stator:** label-only complex; associated with bacterial-type flagellum-dependent motility, **GO:0071973**.
- Other Na+/H+ and K+/H+ antiporters: retain as separate family or locus-specific nodes rather than treating all as Mrp equivalents.

### Bioenergetic proteins and modules

- **F-type H+-transporting ATP synthase:** **GO:0045259**; ATP synthesis coupled proton transport: **GO:0015986**.
- ATP-synthase a-subunit and c-ring; alkaliphile-specific K180 and other a/c-subunit motifs: taxon- and sequence-specific nodes.
- **AtpZ:** label-only alkaliphile-associated accessory protein; reported to enhance Mg acquisition at elevated pH.
- **Respiratory electron-transport chain:** **GO:0022904**.
- **caa3-type cytochrome-c oxidase**, including CtaC/CtaD: label-only complex/subunits pending organism-specific grounding.
- **BpOF4_01690:** label-only, 59-aa hydrophobic protein from *B. pseudofirmus* OF4; GenBank ADC48406.1 was reported in the primary study. (takahashi2018ahydrophobicsmall pages 1-2)

### Cell-envelope nodes

- Cytoplasmic membrane: **GO:0005886**.
- Cell wall: **GO:0005618**.
- Peptidoglycan biosynthesis: **GO:0009252**.
- Acidic secondary cell-wall polymers, teichuronic acid, SlpA S-layer, and poly-γ-glutamate: label-only candidates pending chemical/protein-specific grounding.
- Penicillin-binding proteins PBP2a, PBP3, PBP5, PBP1a/PBP1b, PBP4, and PBPH: organism-specific nodes. Current evidence concerns alkaline shock in neutralophilic *B. subtilis*, not an alkaline optimum.

### Organism nodes

- *Bacillus pseudofirmus* OF4, *Bacillus halodurans* C-125, *Bacillus aequororis* 5-DB, and *Bacillus subtilis* strains should receive NCBITaxon identifiers only after strain-level verification. The report does not assign unverified taxon CURIEs.

## 4. Candidate evidence-backed edges

The following table separates graph-ready edges from taxon-specific, assay-specific, and currently non-curatable claims.

| Subject | Predicate | Object | Evidence snippet (short verbatim quote) | DOI/date | Curatorial status/notes |
|---|---|---|---|---|---|
| High external pH | causes | reversed transmembrane ΔpH / reduced bulk PMF | “the pH gradient… with its orientation of more acidic inside than outside, is in the reverse of the productive orientation for bioenergetic work. The reversed gradient reduces the trans-membrane proton-motive force” (preiss2015alkaliphilicbacteriawith pages 1-2) | 10.3389/fbioe.2015.00075 / Jun 2015 | **Curate** as core environmental-pressure edge for alkaliphily. |
| Bacillus pseudofirmus OF4 at external pH ~10.5 | associated with | cytoplasmic pH 8.3 | “grows optimally at pHout ~10.5 with pHin=8.3” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549 / May 2011 | **Curate** as quantitative phenotype support; taxon-specific exemplar for trait scope. |
| Mrp-type Na+/H+ antiporter (MrpA-G) | enables | electrogenic Na+/H+ antiport | “This membrane-embedded antiporter plays an essential role in catalyzing the electrogenic antiport in support of alkaliphily” (preiss2015alkaliphilicbacteriawith pages 3-4) | 10.3389/fbioe.2015.00075 / Jun 2015 | **Curate**; central mechanistic module. |
| mrpA point mutation | causes loss of | alkaliphile phenotype / alkaline pH homeostasis | “A point mutation in mrpA gene of B. halodurans C-125 causes loss of both alkaliphile phenotype and alkaline pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549 / May 2011 | **Curate**; strong causal genetics, but species-specific experiment. |
| Na+/H+ antiporters | catalyze | cytoplasmic proton accumulation / pH homeostasis | “Na+/H+ antiporters catalyze proton accumulation in the cytoplasm” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Curate**; figure-based mechanistic statement in alkaliphilic Bacillus pseudofirmus OF4. |
| Cytoplasmic pH homeostasis | supports | high-pH optimal growth | “Alkaliphiles also have to maintain a cytoplasmic pH that is significantly lower than the highly alkaline external milieu in which they grow” (preiss2015alkaliphilicbacteriawith pages 3-4) | 10.3389/fbioe.2015.00075 / Jun 2015 | **Curate**; general expert synthesis linking mechanism to phenotype. |
| Na+/solute symporters | provide | Na+ re-entry for pH homeostasis | “Na+ re-entry in support of pH homeostasis is achieved by Na+: solute symporters” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Curate**; pathway component of sodium cycle. |
| NaVBP voltage-gated Na+ channel | provides | physiologically important Na+ re-entry route | “the voltage-gated Na channel operates as a physiologically important ensuring a re-entry route for Na+” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Curate with caution**; wording from figure legend, mainly Bacillus pseudofirmus OF4. |
| MotPS Na+-driven flagellar motor | functions as | secondary Na+ re-entry pathway | “The Na+-driven flagellar motor (MotPS channel) functions as a secondary pathway” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Curate with caution**; sodium-cycle support, not universal to all alkaliphiles. |
| Respiratory chain proton efflux | supplies | outer-surface protons / local PMF for ATP synthesis | “the outer surface vicinity of the cytoplasmic membrane is locally acidified, and enough PMF necessary for the synthesis of ATP is provided” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Do not yet curate as firm edge**; mechanistic model is partly hypothetical/localized. |
| Proton-coupled F1Fo-ATP synthase | drives | ATP synthesis in alkaliphilic Bacillus | “ATP synthesis by oxidative phosphorylation (OXPHOS) using F1Fo-ATP synthase is driven by PMF in alkaliphilic Bacillus species” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Curate**; foundational energy-conservation edge. |
| Alkaliphile-specific ATP synthase a-subunit motif K180 | promotes | growth / ATP synthesis at pH 10.5 | “K180G… major loss of growth on malate at pH 10.5 but not 7.5 and major loss of ATP synthesis” (preiss2015alkaliphilicbacteriawith pages 7-8) | 10.3389/fbioe.2015.00075 / Jun 2015 | **Curate**; strong mutational evidence for alkaliphile-specific adaptation. |
| Acidic SCWP / S-layer / teichuronic acids | contributes to | alkaliphily / pH homeostasis | “Acidic secondary cell wall polymers including teichuronic acids and S-layer protein (SlpA) contribute to pH homeostasis” (krulwich2011molecularaspectsof pages 5-6) | 10.1038/nrmicro2549 / May 2011 | **Curate with caution**; contribution supported, but “proton trapping” mechanism remains inferred. |
| BpOF4_01690 | supports | respiratory-chain activity / high-pH growth | “Δ01690 exhibited weaker growth… under low-sodium conditions at pH 10.5. Additionally, the enzymatic activity of the respiratory chain of Δ01690 was much lower than that of the wild type” (takahashi2018ahydrophobicsmall pages 1-2) | 10.3389/fmicb.2018.01994 / 28 Aug 2018 | **Curate as taxon-specific/uncertain**; strong for B. pseudofirmus OF4 only. |
| Alkaline-active PBPs (PBP2a/PBP3/PBP5) | required for | growth in alkaline conditions | “PBP3, PBP2a, and PBP5 maintain activity during alkaline shock, so it is likely that these PBPs are required for growth in an alkaline environment” (mitchell2024penicillinbindingproteinredundancy pages 8-10) | 10.1128/aem.00548-23 / 21 Dec 2023 (Jan 2024 issue) | **Do not curate as trait edge**; neutrophile alkaline-shock/tolerance evidence, not true alkaliphile optimum. |
| High Na+ concentration with high external pH | increases | ΔpH in Bacillus aequororis 5-DB | “High concentration of Na+ in the medium coupled with high pHout course to activating Na+/H+ antiporter… which leads to an increase in the pH gradient” (maksimova2024metabolicandmorphological pages 9-10) | 10.1155/2024/3087296 / 2024 | **Assay-specific / uncertain**; useful contextual edge for facultative alkaliphile physiology, not broad universal curation. |


*Table: This table summarizes candidate mechanistic edges for curation of the microbial trait pH optimum high, with concise verbatim evidence snippets, DOI/date metadata, and curation notes. It distinguishes strong cross-taxon mechanisms from taxon-specific, assay-specific, or non-curatable alkaline-shock findings.*

### Recommended compact core for `ph_optimum_high.yaml`

A defensible minimal causal chain is:

1. **high external pH → decreases → extracellular proton availability**;
2. **high external pH → reverses → transmembrane ΔpH contribution**;
3. **reversed ΔpH → decreases → bulk proton-motive force available for ATP synthesis**;
4. **respiratory proton pumping → increases → membrane potential / external membrane-surface proton supply**;
5. **Mrp Na+/H+ antiporter → imports → H+ into cytoplasm**;
6. **Mrp Na+/H+ antiporter → exports → Na+ from cytoplasm**;
7. **Na+/solute symport, NaVBP, and MotPS → replenish → cytoplasmic Na+**;
8. **cytoplasmic proton import → maintains → cytoplasmic pH below external pH**;
9. **cytoplasmic pH homeostasis → enables → macromolecular function and growth at high external pH**;
10. **alkaliphile-adapted F1Fo ATP synthase → enables → ATP synthesis at high external pH**;
11. **ATP synthesis and pH homeostasis → support → “METPO:1000458.”**

Edges 1–3, 5–9, and 10–11 have the broadest support. Routes involving MotPS, NaVBP, particular ATP-synthase residues, AtpZ, SlpA, Cta proteins, and BpOF4_01690 should carry organism or clade qualifiers.

## 5. Recent developments and quantitative evidence

### 2024 facultative-alkaliphile physiology

Maksimova and colleagues compared facultative alkaliphile *B. aequororis* 5-DB with weakly alkali-resistant *B. subtilis* ATCC 6633 using resazurin reduction, intracellular ATP, AFM, and fluorescent intracellular-pH measurement. *B. aequororis* grew at pH 11 and 50 g/L NaCl and retained broader pH and salinity resistance; *B. subtilis* metabolic activity was practically absent at pH 11 and 13 in the reported assay. The largest measured ΔpH occurred under external pH 11 with elevated NaCl, consistent with sodium-dependent antiport, although activation of a specific antiporter was inferred rather than established by genetic perturbation. (maksimova2024metabolicandmorphological pages 1-2, maksimova2024metabolicandmorphological pages 5-6, maksimova2024metabolicandmorphological pages 9-10)

This study is valuable as recent physiological validation of high-pH homeostasis, but it should not be used to create a direct gene-level edge because no specific transporter was deleted or biochemically isolated. Its salinity result also concerns a polyextreme condition and should not be generalized to nonsaline alkaliphiles.

### 2023–2024 cell-wall enzyme specialization

Mitchell and colleagues reported that *B. subtilis* PBPs respond differentially to alkaline shock: PBPH and PBP4 lost activity, PBP1a shifted to PBP1b, whereas PBP2a, PBP3, and PBP5 remained active. At pH 8.5 cells remained 100% viable after a 30-minute shock, while viability was 40% at pH 10.5. Deletion strains lacking PBP2a, PBP3, or PBP5 were more base-sensitive. However, the strain could not survive chronic exposure above pH 9.5 and could partly neutralize unbuffered medium. Thus, this is important evidence that extracellular enzyme redundancy supports alkaline **stress tolerance**, but not evidence that these PBPs cause a high-pH optimum. (mitchell2024penicillinbindingproteinredundancy pages 8-10, mitchell2024penicillinbindingproteinredundancy pages 1-2)

### Taxon-specific small-protein mechanism

Deletion of *BpOF4_01690* weakened *B. pseudofirmus* OF4 growth in glucose- and malate-defined media at pH 10.5 under low-sodium conditions and substantially reduced respiratory-chain activity. The phenotype resembled *ctaD* and *atpB–F* deletion strains. Because the protein's molecular action was not resolved and homologues were concentrated in alkaliphilic bacilli, the appropriate edge is “BpOF4_01690 supports respiratory-chain activity/high-pH growth,” qualified as taxon-specific and mechanistically uncertain. (takahashi2018ahydrophobicsmall pages 1-2, takahashi2018ahydrophobicsmall pages 5-7)

## 6. Applications and real-world relevance

Alkaliphiles and their extracellular enzymes are useful where conventional organisms or enzymes lose activity at high pH. Established or proposed application classes include alkaline proteases, amylases, lipases, cellulases and xylanases for detergents, textile processing, leather treatment, food processing, biomass conversion, and alkaline-waste treatment. Whole-cell alkaliphiles may also support high-pH biotransformations and decontamination while reducing the need to neutralize process streams. The core value proposition is operational stability and activity in alkaline media, not the pH-optimum trait alone. (preiss2015alkaliphilicbacteriawith pages 1-2, maksimova2024metabolicandmorphological pages 1-2)

Alkaliphiles have also been tested in microbial fuel cells. The reviewed examples include *Pseudomonas alcaliphila* MBR, which releases phenazine-1-carboxylic acid under alkaline conditions, and *Corynebacterium* strain MFC03 generating electricity from organics at pH 9 through secreted redox compounds. These are real-world implementation examples but do not establish that the homeostasis mechanisms are identical to those of alkaliphilic bacilli. (preiss2015alkaliphilicbacteriawith pages 3-4)

Soda lakes and pH 11–12 serpentinizing springs provide natural laboratories for carbon, sulfur, nitrogen, and hydrogen cycling and for hypotheses about early bioenergetic evolution. Habitat association is ecologically relevant but must not be converted automatically into an organism-level optimum annotation without growth assays. (preiss2015alkaliphilicbacteriawith pages 3-4)

## 7. Expert assessment

The strongest expert consensus is that extreme alkaliphily is a **systems-level bioenergetic phenotype**. Mrp-mediated proton uptake is central in well-studied aerobic bacilli, but it operates with sodium re-entry, respiratory generation of Δψ, adapted ATP synthase, and envelope architecture. The fact that alkaliphilic aerobes synthesize ATP using proton-coupled machinery despite a reversed ΔpH is a major reason these organisms remain important models of chemiosmotic energy conservation. (krulwich2011molecularaspectsof pages 12-14, preiss2015alkaliphilicbacteriawith pages 1-2, preiss2015alkaliphilicbacteriawith pages 12-13)

The current causal graph should therefore avoid both extremes: it should not reduce alkaliphily to mere presence of an *mrp* operon, but it also should not encode every associated omics feature as causal. Loss-of-function, complementation, transport measurements, intracellular-pH assays, and pH-dependent growth phenotypes provide the best evidence.

## 8. Warnings—claims not yet ready for TraitMech curation

1. **Do not equate alkali tolerance with high-pH optimum.** Acute viability, stationary-phase persistence, sporulation, or enzyme activity at pH 10 does not establish “METPO:1000458.”
2. **Do not use the PBP study as a direct trait edge.** It examines a neutralophile under shock/chronic stress, with substantial medium neutralization and no chronic survival above pH 9.5. (mitchell2024penicillinbindingproteinredundancy pages 8-10)
3. **Do not curate “cardiolipin enables alkaliphily.”** Although proposed to conduct or retain surface protons, mutational loss did not significantly affect ATP synthesis in *B. pseudofirmus* OF4. (takahashi2018ahydrophobicsmall pages 1-2)
4. **Treat localized proton transfer as hypothetical.** Surface proton retention and direct caa3 oxidase-to-ATP-synthase transfer are plausible, but a direct stable complex has not been demonstrated. (takahashi2018ahydrophobicsmall pages 1-2, preiss2015alkaliphilicbacteriawith pages 12-13)
5. **Do not generalize MotPS, NaVBP, AtpZ, or BpOF4_01690 to all alkaliphiles.** These are clade- or strain-dependent solutions.
6. **Do not merge alkaliphily with haloalkaliphily.** Na+ can be mechanistically important, but high salinity is a separate trait and experimental variable.
7. **Do not infer causality from gene presence or differential expression alone.** Mrp systems also occur in non-alkaliphiles, while distinct bacterial and archaeal lineages use different ion-coupling strategies. (preiss2015alkaliphilicbacteriawith pages 3-4)
8. **Do not apply a single universal numerical boundary without provenance.** The METPO definition uses approximately >8, whereas much of the literature defines alkaliphiles by optima >9 or around 10. Store the measured optimum and assay conditions whenever possible.
9. **Avoid the supplied DOI 10.1016/j.tim.2007.02.005 as direct alkaliphile evidence.** That DOI corresponds to a review of acidophile physiology. Any antiporter claim used here should instead be sourced to alkaliphile-specific literature.
10. **Verify all ontology mappings and strain identifiers before YAML insertion.** Label-only nodes are preferable to invented or overly broad CURIEs.

## 9. DOI-first bibliography

1. **Maksimova YG, Eliseeva A, Maksimov A.** “Metabolic and Morphological Aspects of Adaptation of Alkaliphilic *Bacillus aequororis* 5-DB and Alkali-Tolerant *Bacillus subtilis* ATCC 6633 to Changes in pH and Mineralization.” *International Journal of Microbiology* (2024; received 10 April, accepted 10 July 2024). DOI: [10.1155/2024/3087296](https://doi.org/10.1155/2024/3087296). (maksimova2024metabolicandmorphological pages 1-2)
2. **Mitchell SL, Kearns DB, Carlson EE.** “Penicillin-binding protein redundancy in *Bacillus subtilis* enables growth during alkaline shock.” *Applied and Environmental Microbiology* 90(1) (published online 21 December 2023; January 2024 issue). DOI: [10.1128/aem.00548-23](https://doi.org/10.1128/aem.00548-23). (mitchell2024penicillinbindingproteinredundancy pages 1-2)
3. **Takahashi T, Krulwich TA, Ito M.** “A Hydrophobic Small Protein, BpOF4_01690, Is Critical for Alkaliphily of Alkaliphilic *Bacillus pseudofirmus* OF4.” *Frontiers in Microbiology* 9:1994 (28 August 2018). DOI: [10.3389/fmicb.2018.01994](https://doi.org/10.3389/fmicb.2018.01994). (takahashi2018ahydrophobicsmall pages 1-2)
4. **Preiss L, Hicks DB, Suzuki S, Meier T, Krulwich TA.** “Alkaliphilic Bacteria with Impact on Industrial Applications, Concepts of Early Life Forms, and Bioenergetics of ATP Synthesis.” *Frontiers in Bioengineering and Biotechnology* 3:75 (June 2015). DOI: [10.3389/fbioe.2015.00075](https://doi.org/10.3389/fbioe.2015.00075). (preiss2015alkaliphilicbacteriawith pages 1-2)
5. **Krulwich TA, Sachs G, Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9:330–343 (May 2011). DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 12-14)

**Curation conclusion:** The most defensible expansion of the existing graph is a core branch from high external pH through reversed ΔpH and diminished bulk PMF, followed by respiratory Δψ generation, Mrp-mediated H+ uptake, sodium recycling, cytoplasmic pH homeostasis, and alkaliphile-adapted ATP synthesis. Surface polymers and BpOF4_01690 can be added as qualified taxon-specific contributors; PBP alkaline-shock findings and localized proton-transfer models should remain outside the asserted core graph pending direct evidence.

References

1. (preiss2015alkaliphilicbacteriawith pages 1-2): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

2. (maksimova2024metabolicandmorphological pages 1-2): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

5. (preiss2015alkaliphilicbacteriawith pages 3-4): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

6. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 22-23): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (takahashi2018ahydrophobicsmall pages 1-2): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.

9. (preiss2015alkaliphilicbacteriawith pages 7-8): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

10. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

11. (preiss2015alkaliphilicbacteriawith pages 12-13): Laura Preiss, David B. Hicks, Shino Suzuki, Thomas Meier, and Terry Ann Krulwich. Alkaliphilic bacteria with impact on industrial applications, concepts of early life forms, and bioenergetics of atp synthesis. Frontiers in Bioengineering and Biotechnology, Jun 2015. URL: https://doi.org/10.3389/fbioe.2015.00075, doi:10.3389/fbioe.2015.00075. This article has 194 citations.

12. (mitchell2024penicillinbindingproteinredundancy pages 8-10): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

13. (maksimova2024metabolicandmorphological pages 9-10): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

14. (maksimova2024metabolicandmorphological pages 5-6): Yulia G. Maksimova, A. Eliseeva, and Aleksandr Maksimov. Metabolic and morphological aspects of adaptation of alkaliphilic bacillus aequororis 5-db and alkali-tolerant bacillus subtilis atcc 6633 to changes in ph and mineralization. International Journal of Microbiology, Jan 2024. URL: https://doi.org/10.1155/2024/3087296, doi:10.1155/2024/3087296. This article has 10 citations and is from a peer-reviewed journal.

15. (mitchell2024penicillinbindingproteinredundancy pages 1-2): Stephanie L. Mitchell, Daniel B. Kearns, and Erin E. Carlson. Penicillin-binding protein redundancy in <i>bacillus subtilis</i> enables growth during alkaline shock. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.00548-23, doi:10.1128/aem.00548-23. This article has 18 citations and is from a peer-reviewed journal.

16. (takahashi2018ahydrophobicsmall pages 5-7): Tetsuaki Takahashi, Terry A. Krulwich, and Masahiro Ito. A hydrophobic small protein, bpof4_01690, is critical for alkaliphily of alkaliphilic bacillus pseudofirmus of4. Frontiers in Microbiology, Aug 2018. URL: https://doi.org/10.3389/fmicb.2018.01994, doi:10.3389/fmicb.2018.01994. This article has 4 citations and is from a peer-reviewed journal.