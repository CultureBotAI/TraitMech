---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:07:48.429603'
end_time: '2026-06-18T05:27:32.138321'
duration_seconds: 1183.71
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: iron oxidation
  trait_identifier: traitmech:000107
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: iron_oxidation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric
    iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic
    or anaerobic conditions.
  parent_traits: METPO:1000060
  synonyms: ferrous iron oxidation
  evidence_summary: 'DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming &
    McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.)
    | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing
    proteobacteria and their energy metabolism.)'
  causal_graph_summary: 'iron_oxidation_ferrous_to_ferric: 3 nodes, 2 edges'
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
- **Trait label:** iron oxidation
- **METPO identifier:** traitmech:000107
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** ferrous iron oxidation
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming & McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.) | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing proteobacteria and their energy metabolism.)
- **Existing causal graph summary:** iron_oxidation_ferrous_to_ferric: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **iron oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/iron_oxidation.yaml`.

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
- **Trait label:** iron oxidation
- **METPO identifier:** traitmech:000107
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes ferrous iron (Fe2+) to ferric iron (Fe3+) to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** ferrous iron oxidation
- **Existing evidence:** DOI:10.1146/annurev.micro.112408.134208:  (Emerson, Fleming & McBeth review iron-oxidizing bacteria from an environmental and genomic perspective.) | DOI:10.1099/mic.0.045344-0:  (Hedrich, Schlomann & Johnson review the iron-oxidizing proteobacteria and their energy metabolism.)
- **Existing causal graph summary:** iron_oxidation_ferrous_to_ferric: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **iron oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/iron_oxidation.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Iron Oxidation (traitmech:000107)

## 0) Executive scope summary

**Trait definition (METPO/Template):** iron oxidation is a metabolism in which an organism oxidizes **ferrous iron (Fe2+) to ferric iron (Fe3+)** to conserve energy, at acidic or circumneutral pH and under aerobic or anaerobic conditions.

**Operational phenotype for curation:** evidence-supported **dissimilatory Fe(II) oxidation coupled to an electron transport chain (ETC)** that supports energy conservation (ATP generation and/or reductant generation for CO2 fixation), typically mediated by **outer-membrane/periplasmic electron-transfer modules** that keep Fe(III) formation outside the cytoplasm (to avoid precipitation/oxidative stress). This “vertical” arrangement is explicitly described as a defining design principle of Fe(II)-oxidation systems. (li2023sequencesimilaritynetwork pages 2-4)

**Boundary cases / exclusions (important for TraitMech):**
1. **Abiotic Fe(II) oxidation** (e.g., by O2 at neutral pH) can mimic the phenotype; curated edges should emphasize enzymatic electron uptake and downstream ETC coupling (li2023sequencesimilaritynetwork pages 2-4).
2. **Nitrate-dependent Fe(II) oxidation (NRFO)** is a boundary case because Fe(II) oxidation can occur via both **biological electron transport** and **chemical oxidation by nitrite/NO (chemodenitrification)**; intermediates can also inhibit cytochromes (hoover2023gallionellaceaepangenomicanalysis pages 10-14, hou2024biologicalandchemical pages 11-13).
3. **Phototrophic Fe(II) oxidation (photoferrotrophy)** is distinct (light-driven electron transfer); it can be ecologically suppressed by nitrate-reducing Fe(II) oxidizers via reactive nitrogen intermediates (NO) (nikeleit2024inhibitionofphototrophic pages 1-2).
4. **Fe(III) reduction** (reverse direction) shares homologous porin–cytochrome conduits (Mtr/Mto), but is a different trait; reversibility of conduits is plausible, so directionality should be curated with caution (hoover2023gallionellaceaepangenomicanalysis pages 4-8).

## 1) Key concepts and definitions (current understanding)

### 1.1 Core mechanistic concept: “vertical” iron respiratory chains
A recurring mechanistic theme is that Fe(II)-oxidation chains are organized as **electron shuttles connecting the external medium to the cytoplasm**, distinct from laterally arranged respiratory chains, with benefits including avoidance of intracellular Fe(III) precipitation and limiting oxidative stress. (li2023sequencesimilaritynetwork pages 2-4)

### 1.2 Canonical gene/protein modules (acidophilic vs neutrophilic)
A recent synthesis enumerates canonical pathways across acidophiles, neutrophiles, and archaea (Table 1), including: **Cyc2/Cyc1/rusticyanin (rus operon), Pio/Mto systems (decaheme cytochromes + outer-membrane porins), Fox systems, sulfocyanin, Mob**, and terminal oxidases. (li2023sequencesimilaritynetwork pages 2-4)

### 1.3 Substrate form matters: aqueous vs mineral/organic-bound Fe(II)
For circumneutral FeOB, different outer-membrane electron-uptake proteins appear adapted to different Fe(II) substrates; e.g., Cyc2 is associated with **aqueous Fe2+**, whereas MtoA/MtoAB are associated with **solid/mineral-bound Fe(II)** (smectite clay), based on expression/functional association. (tothero2024leptothrixochraceagenomes pages 9-13)

### 1.4 Ecophysiology: microaerobic interfaces
Circumneutral FeOB often inhabit **microaerobic redox transition zones** (Fe(II)-rich anoxic waters meeting low O2). Genomic evidence in Fe-mat organisms (e.g., Leptothrix ochracea) shows high-affinity terminal oxidases (cbb3 and bd), consistent with microaerobic lifestyles. (tothero2024leptothrixochraceagenomes pages 9-13)

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 2023: Cross-pathway synthesis + structure prediction for Fe(II) oxidation proteins
A 2023 mSystems study used sequence similarity networks and AI structure prediction to unify diverse Fe(II)-oxidation components, emphasizing (i) broad taxonomic distribution (suggesting HGT), (ii) outer-membrane/periplasmic localization, and (iii) “vertical shuttles” as a functional design. It provides explicit mechanistic statements for the Acidithiobacillus Cyc2→rusticyanin branching model and a canonical pathway table spanning many taxa. (li2023sequencesimilaritynetwork pages 2-4)

### 2.2 2023: Pangenomics of Gallionellaceae reveals multiple EET solutions
A 2023 pangenomic analysis of 103 Gallionellaceae genomes reports that **cyc2** and **mtoA** are prevalent marker genes for FeOB (with specific percentages) and that FeOB genomes are enriched in **multiheme cytochromes (MHCs)** and candidate porin–multiheme complexes, implying multiple extracellular electron-uptake solutions beyond the best-characterized oxidases. (hoover2023gallionellaceaepangenomicanalysis pages 4-8)

**Key statistic:** cyc2 detected in **83%** of FeOB genomes; mtoA in **41%**; and **89%** have at least one of cyc2 or mtoA; **37%** have both. (hoover2023gallionellaceaepangenomicanalysis pages 4-8)

### 2.3 2024: First near-complete genomes of Leptothrix ochracea support mixotrophic iron oxidation
A 2024 Applied and Environmental Microbiology study reconstructed nine high-quality L. ochracea genomes and provides explicit mechanistic framing that **validated iron oxidase genes** (cyc2 cluster 1, mtoA) plus periplasmic carriers (cyc1) can connect Fe(II) oxidation to the ETC, supporting energy conservation and growth. It also distinguishes L. ochracea from a related isolate lacking known iron oxidase genes despite exhibiting iron oxidation activity in culture (cautionary boundary case). (tothero2024leptothrixochraceagenomes pages 9-13)

### 2.4 2024: Reactive nitrogen species reshape Fe(II)-oxidizer competition
A 2024 Nature Geoscience study shows nitrate-reducing Fe(II) oxidizers can outcompete photoferrotrophs for Fe(II) and inhibit photoferrotrophy via toxic intermediates, supporting the concept that nitrogen redox chemistry (NO/NO2−) can control Fe(II)-oxidation ecology. (nikeleit2024inhibitionofphototrophic pages 1-2)

## 3) Current applications and real-world implementations

### 3.1 Biomining / bioleaching (acidophilic Fe(II) oxidation as an oxidant generator)
A 2023 review frames bioleaching as exploiting iron- and sulfur-oxidizing acidophiles to generate oxidants (ferric iron) that attack sulfide minerals. It includes a schematic of iron oxidation operons (rus operon) and models for iron oxidation in key acidophiles. (jones2023mechanismsofbioleaching pages 6-11, jones2023mechanismsofbioleaching media 3808103a, jones2023mechanismsofbioleaching media 7934dd83)

### 3.2 Environmental engineering contexts: Fe mats, groundwater seeps, and treatment interfaces
Circumneutral FeOB (Gallionellaceae, Leptothrix) are prominent in Fe-rich, microaerobic interfaces that generate Fe(III) (oxyhydr)oxide biominerals (mats, sheaths). Genomic signatures (cyc2/mtoA, terminal oxidases) provide a mechanism-based rationale for monitoring and potentially managing iron biomineralization in such settings. (tothero2024leptothrixochraceagenomes pages 9-13, hoover2023gallionellaceaepangenomicanalysis pages 4-8)

### 3.3 Bioelectrochemical systems (conceptual overlap: extracellular electron transfer)
A 2024 study comparing electroautotrophic vs chemoautotrophic growth in Acidithiobacillus ferrooxidans found altered expression consistent with different extracellular electron uptake pathways and increased pili/EPS under electroautotrophy, connecting iron-oxidation electron transfer concepts to electrode-based applications. (wang2024characterizethegrowth pages 1-2)

## 4) Candidate causal graph nodes (grouped by type)

### 4.1 Pathways / modules
- **Ferrous iron oxidation pathway (acidophilic rus pathway):** Fe2+ → Cyc2 → rusticyanin → (branch) downhill O2 reduction via Cyc1 + aa3 oxidase; uphill reverse electron transport to NADH1. (li2023sequencesimilaritynetwork pages 2-4)
- **Neutrophilic Fe(II) oxidation modules:** Cyc2 (cluster 1) for aqueous Fe2+; MtoA/MtoAB for solid Fe(II) (smectite); additional porin–MHC complexes (e.g., Uet, PCC3; as candidate EET systems). (hoover2023gallionellaceaepangenomicanalysis pages 10-14, tothero2024leptothrixochraceagenomes pages 9-13)
- **NRFO (nitrate reduction–ferrous oxidation coupling):** mixed biological and chemical processes; gene cluster dependence (MtrABC) in a model system (Shewanella). (hou2024biologicalandchemical pages 11-13)

### 4.2 Genes / proteins / complexes (candidate nodes)
**Outer membrane / extracellular electron uptake**
- Cyc2 (outer-membrane cytochrome-porin iron oxidase) (li2023sequencesimilaritynetwork pages 2-4, hoover2023gallionellaceaepangenomicanalysis pages 4-8)
- MtoA (decaheme cytochrome), MtoB (outer membrane protein), MtoAB complex (li2023sequencesimilaritynetwork pages 2-4)
- PioA/PioB (photoferrotrophy-associated decaheme/porin analogs) (li2023sequencesimilaritynetwork pages 2-4)
- MtrABC (porin–cytochrome conduit required for NRFO in Shewanella) (hou2024biologicalandchemical pages 11-13)
- Multiheme c-type cytochromes (MHCs; class-level node) (hoover2023gallionellaceaepangenomicanalysis pages 1-2, hoover2023gallionellaceaepangenomicanalysis pages 4-8)

**Periplasmic carriers / branch points**
- Rusticyanin (blue copper protein; branch point in acidophiles) (li2023sequencesimilaritynetwork pages 2-4)
- Cyc1 (cytochrome c4; connects periplasm to inner membrane/ETC) (li2023sequencesimilaritynetwork pages 2-4, tothero2024leptothrixochraceagenomes pages 9-13)

**Respiratory chain / energy conservation**
- Terminal oxidases: aa3-type (coxABCD), cbb3-type (ccoNOPQ), bd-type (cydABX) (tothero2024leptothrixochraceagenomes pages 9-13, hoover2023gallionellaceaepangenomicanalysis pages 10-14)
- Electron routing complexes: bc1 complex; ACIII (Alternative complex III) (hoover2023gallionellaceaepangenomicanalysis pages 10-14)
- NADH dehydrogenase I (Complex I; “NADH1 complex”) in reverse electron transport (li2023sequencesimilaritynetwork pages 2-4)

**Carbon fixation**
- RuBisCO (Form I/II) and Calvin–Benson–Bassham cycle (hoover2023gallionellaceaepangenomicanalysis pages 10-14, tothero2024leptothrixochraceagenomes pages 9-13)

### 4.3 Chemicals / substrates / inhibitors (candidate nodes)
- Fe2+ (electron donor), Fe3+ (product) (CHEBI:29033, CHEBI:29034)
- O2 (terminal electron acceptor) (CHEBI:15379)
- Nitrate (NO3−), nitrite (NO2−), nitric oxide (NO) as ecological/assay modifiers and inhibitors/competitors (CHEBI:17632, CHEBI:16301, CHEBI:16480) (hoover2023gallionellaceaepangenomicanalysis pages 10-14, nikeleit2024inhibitionofphototrophic pages 1-2)

### 4.4 Environmental / experimental factors (candidate nodes)
- **pH** (acid mine drainage vs circumneutral) influences Fe redox potential and solubility (li2023sequencesimilaritynetwork pages 2-4)
- **Oxygen regime / microaerobic interface** (high-affinity oxidases used under microaerobic conditions) (tothero2024leptothrixochraceagenomes pages 9-13)
- **Fe(II) substrate form:** aqueous, mineral-bound (smectite), organic-bound (humics/EPS) (tothero2024leptothrixochraceagenomes pages 9-13)
- **Organic carbon availability:** linked to bd oxidase expression patterns and ecological niche differentiation (hoover2023gallionellaceaepangenomicanalysis pages 10-14)

## 5) Evidence-backed candidate causal edges (curation-ready table)

| Edge (subject–predicate–object) | Node type (S/P/O) | Suggested grounding (CURIEs where possible) | Evidence snippet (verbatim quote) | Source (first author year, journal) | DOI | URL | Notes/uncertainty |
|---|---|---|---|---|---|---|---|
| Cyc2 – oxidizes – Fe(II) | protein–molecular function–chemical | Cyc2 \/ label; GO:0016491; CHEBI:29033 (Fe2+); CHEBI:29034 (Fe3+) | “electrons are initially extracted from extracellular Fe(II) by the outer membrane cytochrome c Cyc2” (li2023sequencesimilaritynetwork pages 2-4) | Li 2023, mSystems | 10.1128/mSystems.00720-23 | https://doi.org/10.1128/msystems.00720-23 | Strong for acidophile model; broader trait-level curation reasonable because Cluster 1 Cyc2 is also validated in neutrophiles, but exact mechanism varies by taxon. |
| Cyc2 – transfers electrons to – rusticyanin | protein–causally upstream of, positive effect on–protein | Cyc2 \/ label; rusticyanin \/ label | “electrons are initially extracted from extracellular Fe(II) by the outer membrane cytochrome c Cyc2 and then transferred to the periplasmic blue copper protein rusticyanin” (li2023sequencesimilaritynetwork pages 2-4) | Li 2023, mSystems | 10.1128/mSystems.00720-23 | https://doi.org/10.1128/msystems.00720-23 | Strong for Acidithiobacillus-like acidophile pathway; taxon-specific, not universal across all FeOB. |
| rusticyanin – routes electrons via Cyc1 and aa3 oxidase to – O2 reduction | protein–causally upstream of, positive effect on–process | rusticyanin \/ label; Cyc1 \/ label; EC:7.1.1.9 or GO:0004129 candidate for aa3 oxidase; CHEBI:15379 (O2) | “From the ‘branch point’ protein rusticyanin, the electrons can then flow either downstream, reducing O2 to water via cytochrome c4 Cyc1 and the aa3-type cytochrome oxidase complex” (li2023sequencesimilaritynetwork pages 2-4) | Li 2023, mSystems | 10.1128/mSystems.00720-23 | https://doi.org/10.1128/msystems.00720-23 | Strong for acidophilic aerobic Fe oxidation; represents canonical downhill branch. |
| rusticyanin – routes electrons to – NADH1 via reverse electron transport | protein–causally upstream of, positive effect on–process | rusticyanin \/ label; NADH dehydrogenase I \/ KEGG:K00330-K00346 candidate; GO:0019646 candidate for reverse electron transport | “or upstream, utilizing the proton motive force across the inner membrane to overcome the unfavorable thermodynamic gradient and transfer electrons to the NADH1 complex” (li2023sequencesimilaritynetwork pages 2-4) | Li 2023, mSystems | 10.1128/mSystems.00720-23 | https://doi.org/10.1128/msystems.00720-23 | Strong in Acidithiobacillus model; should be curated as acidophile-specific rather than universal FeOB feature. |
| MtoA\/MtoAB – associated with oxidation of – solid Fe(II) substrates | complex–associated with activity toward–chemical substrate | MtoA \/ label; MtoAB \/ label; CHEBI:29033 (Fe2+); ENVO:solid substrate label | “mtoA has been shown to be expressed specifically when the Gallionellaceae Sideroxydans lithotrophicus ES-1 oxidizes solid Fe(II) in smectite clay” (tothero2024leptothrixochraceagenomes pages 9-13) | Tothero 2024, Applied and Environmental Microbiology | 10.1128/AEM.00599-24 | https://doi.org/10.1128/aem.00599-24 | Good support for solid/mineral-bound Fe(II) specialization; expression evidence, not purified-enzyme biochemistry. |
| cbb3-type oxidase – supports growth in – microaerobic conditions | terminal oxidase–adapted to–environmental condition | ccoNOPQ; GO:0004129 candidate; ENVO:microaerobic habitat label | “These terminal oxidases have high affinity for oxygen and therefore are widely understood to be used under microaerobic conditions” (tothero2024leptothrixochraceagenomes pages 9-13) | Tothero 2024, Applied and Environmental Microbiology | 10.1128/AEM.00599-24 | https://doi.org/10.1128/aem.00599-24 | Strong; applies to cbb3 and bd in Leptothrix context and broadly consistent with FeOB ecology. |
| bd-type oxidase – supports growth in – low-O2\/organic-rich niches | terminal oxidase–adapted to–environmental condition | cydABX; GO:0004129 candidate; ENVO:microaerobic habitat label | “Like cbb3-type oxidases, cytochrome bd-type oxidases have a high affinity for oxygen, and recent studies show they can be more highly expressed than cbb3-type oxidases under low-oxygen, organic-rich conditions” (hoover2023gallionellaceaepangenomicanalysis pages 10-14) | Hoover 2023, mSystems | 10.1128/mSystems.00038-23 | https://doi.org/10.1128/msystems.00038-23 | Strong genomic/ecophysiological inference; direct expression claim refers to recent studies cited by authors, not this dataset alone. |
| nitrite\/NO – inhibit – cytochromes and compete with enzymatic Fe(II) oxidation | chemicals–negatively regulates–biological process | CHEBI:16301 (nitrite); CHEBI:16480 (nitric oxide); cytochrome c \/ GO:0020037; CHEBI:29033 (Fe2+) | “Both nitrite and NO present major challenges to FeOB metabolism because of their reactivity with iron: they bind to hemes, inhibiting the activity of cytochromes, and also directly oxidize Fe(II), thus competing with enzymatic iron oxidation” (hoover2023gallionellaceaepangenomicanalysis pages 10-14) | Hoover 2023, mSystems | 10.1128/mSystems.00038-23 | https://doi.org/10.1128/msystems.00038-23 | Strong for inhibitory environmental edge; relevant warning for assay interpretation because abiotic oxidation can confound biological Fe oxidation. |
| MtrABC – required for – nitrate-dependent Fe(II) oxidation | gene cluster–required for–process | mtrABC \/ label; nitrate-dependent Fe(II) oxidation \/ label; CHEBI:17632 (nitrate) | “the MtrABC gene cluster knockout strains exhibited substantially reduced iron oxidation compared to the wild type, emphasizing the crucial role of these gene clusters within the electron transport chain” (hou2024biologicalandchemical pages 11-13) | Hou 2024, Microorganisms | 10.3390/microorganisms12122454 | https://doi.org/10.3390/microorganisms12122454 | Useful but uncertain for TraitMech core graph: Shewanella is not a canonical dedicated FeOB, and NRFO includes mixed biological plus chemical oxidation. |
| cyc2 + mtoA – enable use of – varied Fe(II) substrates | gene set–enables utilization of–substrate class | cyc2 \/ label; mtoA \/ label; CHEBI:29033 (Fe2+); varied Fe(II) substrates \/ label | “The presence of multiple iron oxidase genes (cyc2 and mtoA) in L. ochracea genomes may enable the cells to utilize different ferrous iron substrates.” (tothero2024leptothrixochraceagenomes pages 9-13) | Tothero 2024, Applied and Environmental Microbiology | 10.1128/AEM.00599-24 | https://doi.org/10.1128/aem.00599-24 | Strong but still inferential (“may enable”); good candidate edge with uncertainty flag. |
| FeOB-enriched multiheme cytochromes – enable – extracellular electron transfer across minerals\/long distances | protein class–enables–process | multiheme c-type cytochrome \/ label; GO:0009055 or electron transfer label; mineral-bound Fe(II) \/ label | “MHCs efficiently conduct electrons across longer distances and function across a wide range of redox potentials that overlap with mineral redox potentials, which can expand the range of usable iron substrates.” (hoover2023gallionellaceaepangenomicanalysis pages 1-2) | Hoover 2023, mSystems | 10.1128/mSystems.00038-23 | https://doi.org/10.1128/msystems.00038-23 | Good support for EET-capability edge; specific MHC identities and exact partners remain unresolved, so node may need to remain class-level. |


*Table: This table compiles candidate causal edges for the microbial iron oxidation trait, linking genes, proteins, complexes, and environmental factors to mechanistic roles with verbatim evidence and curation notes. It is useful as a starting point for TraitMech graph assembly and for identifying edges that remain taxon-specific or uncertain.*

### Key mechanistic quote digest

> “electrons are initially extracted from extracellular Fe(II) by the outer membrane cytochrome c Cyc2” (li2023sequencesimilaritynetwork pages 2-4)
>
> “and then transferred to the periplasmic blue copper protein rusticyanin” (li2023sequencesimilaritynetwork pages 2-4)
>
> “the electrons can then flow either downstream, reducing O2 to water via cytochrome c4 Cyc1 and the aa3-type cytochrome oxidase complex” (li2023sequencesimilaritynetwork pages 2-4)
>
> “or upstream, utilizing the proton motive force across the inner membrane to overcome the unfavorable thermodynamic gradient and transfer electrons to the NADH1 complex” (li2023sequencesimilaritynetwork pages 2-4)
>
> “mtoA has been shown to be expressed specifically when the Gallionellaceae Sideroxydans lithotrophicus ES-1 oxidizes solid Fe(II) in smectite clay” (tothero2024leptothrixochraceagenomes pages 9-13)
>
> “These terminal oxidases have high affinity for oxygen and therefore are widely understood to be used under microaerobic conditions” (tothero2024leptothrixochraceagenomes pages 9-13)
>
> “they bind to hemes, inhibiting the activity of cytochromes, and also directly oxidize Fe(II), thus competing with enzymatic iron oxidation” (hoover2023gallionellaceaepangenomicanalysis pages 10-14)
>
> “the MtrABC gene cluster knockout strains exhibited substantially reduced iron oxidation compared to the wild type” (hou2024biologicalandchemical pages 11-13)
>
> “MHCs efficiently conduct electrons across longer distances and function across a wide range of redox potentials that overlap with mineral redox potentials” (hoover2023gallionellaceaepangenomicanalysis pages 1-2)


*Blockquote: This artifact compiles short verbatim quotations supporting core mechanistic edges for microbial Fe(II) oxidation. It is useful for curation because each quote directly supports a specific node or causal relationship in the candidate TraitMech graph.*

## 6) Visual evidence (figures useful for curators)

- A schematic of the **Acidithiobacillus ferrooxidans** ferrous iron oxidation ETC (Cyc2→rusticyanin→Cyc1→aa3 oxidase; downhill branch) was retrieved from a 2023 review figure. (jones2023mechanismsofbioleaching media 3808103a)
- A schematic of the **rus operon** (including promoters upstream of cyc2 and coxABCD encoding aa3 subunits) was retrieved from the same review. (jones2023mechanismsofbioleaching media 7934dd83)

## 7) Warnings: claims that should not yet be curated (or should be marked uncertain)

1. **“cyc2 + mtoA enable varied Fe(II) substrates”** is supported as a plausible genomic/physiological inference (“may enable”), but is not direct biochemical proof in every taxon; curate with an uncertainty flag and link to substrate-form context. (tothero2024leptothrixochraceagenomes pages 9-13)
2. **NRFO edges (e.g., MtrABC→Fe(II) oxidation with nitrate)** should be curated as a **separate mechanistic subgraph** or flagged boundary-case because chemical Fe(II) oxidation via nitrite/NO can contribute, and because Shewanella is not a canonical obligate FeOB. (hou2024biologicalandchemical pages 11-13, hoover2023gallionellaceaepangenomicanalysis pages 10-14)
3. **Denitrification as an energy-conserving partner metabolism in Gallionellaceae** appears rare; narGH is uncommon and should not be inferred broadly for the family. (hoover2023gallionellaceaepangenomicanalysis pages 10-14)
4. **MHC/EET complexes (PCC3/Uet etc.)** are strong candidates but largely bioinformatic; curate as “candidate” nodes/edges unless there is direct functional validation in the target taxa. (hoover2023gallionellaceaepangenomicanalysis pages 10-14, hoover2023gallionellaceaepangenomicanalysis pages 4-8)

## 8) DOI-first bibliography (with publication dates and URLs)

1. Li L, et al. **Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation.** *mSystems.* Published: Sep/Oct 2023 (issue 5). DOI: **10.1128/msystems.00720-23**. URL: https://doi.org/10.1128/msystems.00720-23 (li2023sequencesimilaritynetwork pages 2-4)
2. Hoover RL, et al. **Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms.** *mSystems.* Published: Nov/Dec 2023. DOI: **10.1128/msystems.00038-23**. URL: https://doi.org/10.1128/msystems.00038-23 (hoover2023gallionellaceaepangenomicanalysis pages 4-8)
3. Jones S, Santini JM. **Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms.** *Essays in Biochemistry.* Published: Aug 2023. DOI: **10.1042/ebc20220257**. URL: https://doi.org/10.1042/EBC20220257 (jones2023mechanismsofbioleaching pages 6-11)
4. Tothero GK, et al. **Leptothrix ochracea genomes reveal potential for mixotrophic growth on Fe(II) and organic carbon.** *Applied and Environmental Microbiology.* Published: Sep 2024. DOI: **10.1128/aem.00599-24**. URL: https://doi.org/10.1128/aem.00599-24 (tothero2024leptothrixochraceagenomes pages 9-13)
5. Nikeleit V, et al. **Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments.** *Nature Geoscience.* Published online: 4 Oct 2024. DOI: **10.1038/s41561-024-01560-9**. URL: https://doi.org/10.1038/s41561-024-01560-9 (nikeleit2024inhibitionofphototrophic pages 1-2)
6. Hou L, et al. **Biological and Chemical Processes of Nitrate Reduction and Ferrous Oxidation Mediated by Shewanella oneidensis MR-1.** *Microorganisms.* Published: Nov 2024. DOI: **10.3390/microorganisms12122454**. URL: https://doi.org/10.3390/microorganisms12122454 (hou2024biologicalandchemical pages 11-13)
7. Wang Q, et al. **Characterize the Growth and Metabolism of Acidithiobacillus ferrooxidans under Electroautotrophic and Chemoautotrophic Conditions.** *Microorganisms.* Published: 15 Mar 2024. DOI: **10.3390/microorganisms12030590**. URL: https://doi.org/10.3390/microorganisms12030590 (wang2024characterizethegrowth pages 1-2)

## 9) Minimal curation-ready takeaways

- **Core enzymatic entry points:** Cyc2 (widely used), MtoA/MtoAB (solid/mineral Fe(II)), plus diverse porin–cytochrome/MHC systems. (hoover2023gallionellaceaepangenomicanalysis pages 4-8, tothero2024leptothrixochraceagenomes pages 9-13)
- **Core environmental constraints:** pH and O2 regime control feasibility/architecture; microaerobic terminal oxidases are key in Fe mats; reactive nitrogen species can inhibit cytochromes and confound Fe(II) oxidation assays. (tothero2024leptothrixochraceagenomes pages 9-13, hoover2023gallionellaceaepangenomicanalysis pages 10-14, li2023sequencesimilaritynetwork pages 2-4)
- **Graph design guidance:** maintain separate subgraphs for (i) acidophilic rus pathway, (ii) circumneutral Fe-mat FeOB Cyc2/Mto systems, (iii) nitrate-linked/boundary NRFO; connect through shared higher-level nodes (Fe2+ electron donor, outer-membrane electron uptake, ETC coupling, Fe(III) biomineralization). (li2023sequencesimilaritynetwork pages 2-4, hoover2023gallionellaceaepangenomicanalysis pages 4-8, hou2024biologicalandchemical pages 11-13)


References

1. (li2023sequencesimilaritynetwork pages 2-4): Liangzhi Li, Zhenghua Liu, Delong Meng, Yongjun Liu, Tianbo Liu, Chengying Jiang, and Huaqun Yin. Sequence similarity network and protein structure prediction offer insights into the evolution of microbial pathways for ferrous iron oxidation. Oct 2023. URL: https://doi.org/10.1128/msystems.00720-23, doi:10.1128/msystems.00720-23. This article has 5 citations and is from a peer-reviewed journal.

2. (hoover2023gallionellaceaepangenomicanalysis pages 10-14): Rene L. Hoover, Jessica L. Keffer, Shawn W. Polson, and Clara S. Chan. Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms. Dec 2023. URL: https://doi.org/10.1128/msystems.00038-23, doi:10.1128/msystems.00038-23. This article has 24 citations and is from a peer-reviewed journal.

3. (hou2024biologicalandchemical pages 11-13): Lingyu Hou, Xiangyu Bai, Zihe Sima, Jiani Zhang, Luyao Yan, Ding Li, and Yongguang Jiang. Biological and chemical processes of nitrate reduction and ferrous oxidation mediated by shewanella oneidensis mr-1. Microorganisms, 12:2454, Nov 2024. URL: https://doi.org/10.3390/microorganisms12122454, doi:10.3390/microorganisms12122454. This article has 6 citations.

4. (nikeleit2024inhibitionofphototrophic pages 1-2): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

5. (hoover2023gallionellaceaepangenomicanalysis pages 4-8): Rene L. Hoover, Jessica L. Keffer, Shawn W. Polson, and Clara S. Chan. Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms. Dec 2023. URL: https://doi.org/10.1128/msystems.00038-23, doi:10.1128/msystems.00038-23. This article has 24 citations and is from a peer-reviewed journal.

6. (tothero2024leptothrixochraceagenomes pages 9-13): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

7. (jones2023mechanismsofbioleaching pages 6-11): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 83 citations and is from a peer-reviewed journal.

8. (jones2023mechanismsofbioleaching media 3808103a): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 83 citations and is from a peer-reviewed journal.

9. (jones2023mechanismsofbioleaching media 7934dd83): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 83 citations and is from a peer-reviewed journal.

10. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 9 citations.

11. (hoover2023gallionellaceaepangenomicanalysis pages 1-2): Rene L. Hoover, Jessica L. Keffer, Shawn W. Polson, and Clara S. Chan. Gallionellaceae pangenomic analysis reveals insight into phylogeny, metabolic flexibility, and iron oxidation mechanisms. Dec 2023. URL: https://doi.org/10.1128/msystems.00038-23, doi:10.1128/msystems.00038-23. This article has 24 citations and is from a peer-reviewed journal.