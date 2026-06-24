---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:58:27.441526'
end_time: '2026-06-18T10:10:05.680761'
duration_seconds: 698.24
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: sulfur globule
  trait_identifier: traitmech:000069
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: sulfur_globule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An intracellular (or periplasmic) inclusion of elemental sulfur formed
    as an intermediate during the oxidation of reduced sulfur compounds, characteristic
    of many sulfur-oxidizing and phototrophic sulfur bacteria.
  parent_traits: traitmech:000066
  synonyms: sulfur inclusion
  evidence_summary: 'DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe
    sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism
    in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening
    & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)'
  causal_graph_summary: 'sulfur_globule_sulfur_oxidation_intermediate: 3 nodes, 2
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur globule
- **METPO identifier:** traitmech:000069
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular (or periplasmic) inclusion of elemental sulfur formed as an intermediate during the oxidation of reduced sulfur compounds, characteristic of many sulfur-oxidizing and phototrophic sulfur bacteria.
- **Parent traits:** traitmech:000066
- **Synonyms:** sulfur inclusion
- **Existing evidence:** DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)
- **Existing causal graph summary:** sulfur_globule_sulfur_oxidation_intermediate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **sulfur globule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sulfur_globule.yaml`.

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
- **Trait label:** sulfur globule
- **METPO identifier:** traitmech:000069
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular (or periplasmic) inclusion of elemental sulfur formed as an intermediate during the oxidation of reduced sulfur compounds, characteristic of many sulfur-oxidizing and phototrophic sulfur bacteria.
- **Parent traits:** traitmech:000066
- **Synonyms:** sulfur inclusion
- **Existing evidence:** DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)
- **Existing causal graph summary:** sulfur_globule_sulfur_oxidation_intermediate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **sulfur globule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sulfur_globule.yaml`.

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


# Sulfur Globule (METPO traitmech:000069) — Curation-Focused Research Report

## 0) Trait scope summary (what the trait represents)

**Trait definition (operationalized):** A *sulfur globule* is a discrete, microscopically visible inclusion/body composed primarily of elemental sulfur (S(0)), formed as an intermediate during microbial oxidation of reduced sulfur compounds and often serving as a transient storage pool that can be further oxidized. In purple sulfur bacteria (Chromatiaceae), sulfur globules are **intracellular but extracytoplasmic**, typically **in the periplasmic space**, and are surrounded by a proteinaceous envelope (kumpel2023cellbiologyof pages 1-3, petushkova2024thecompletegenome pages 20-22). 

**Key boundary conditions:**
- **Localization boundary:** A major boundary is whether sulfur intermediates are deposited **outside the cytoplasm**. A phototrophic-sulfur-bacteria synthesis states that in anoxygenic phototrophs sulfur intermediates “are never deposited in the cytoplasm” (dahl2017sulfurmetabolismin pages 14-17), consistent with periplasmic/extracytoplasmic globules in Chromatiaceae (petushkova2024thecompletegenome pages 20-22).
- **Taxonomic boundary:** Chromatiaceae periplasmic globules vs taxa that form extracellular globules (reviewed synthesis) (dahl2017sulfurmetabolismin pages 14-17).
- **Mechanistic boundary cases (do not conflate with sulfur globules):**
  1) **Cytoplasmic S8 “sulfur globules” in aerobic/heterotrophic contexts** (e.g., engineered/recombinant contexts) are mechanistically relevant but may not match the phototroph-focused trait scope (rudenko2024mechanismofintracellular pages 1-2).
  2) **Encapsulin-based protein compartments storing crystalline elemental sulfur** are a distinct bacterial storage morphology. They provide valuable mechanistic analogies but should be curated as a separate structure/trait unless TraitMech explicitly includes protein compartments under “sulfur globule” (benisch2024awidespreadbacterial media 1a2af37b, benisch2024awidespreadbacterial media e49c5f77).

**Assay/observation modes:** 
- Light-refractive intracellular deposits observed by microscopy in sulfide-fed *Allochromatium vinosum* (kumpel2023cellbiologyof pages 1-3).
- Quantification by biomass fraction (e.g., % dry weight) or by transcriptomic/proteomic changes during formation/consumption (kumpel2023cellbiologyof pages 1-3, rudenko2024mechanismofintracellular pages 10-12).

## 1) Key concepts and definitions (current understanding)

### 1.1 Sulfur globules as intermediate and storage pools
In purple sulfur bacteria, sulfur globules are formed during oxidation of reduced sulfur compounds and function as **obligatory intermediates** during oxidative sulfur metabolism (kumpel2023cellbiologyof pages 1-3). In *A. vinosum*, globules can be large (up to ~1 µm) and represent a substantial fraction of biomass, consistent with a major storage/intermediate role (kumpel2023cellbiologyof pages 1-3).

### 1.2 Subcellular localization and architecture
In Chromatiaceae, sulfur globules are located in the **periplasmic space** (intracellular but extracytoplasmic) and surrounded by a **protein coat** (petushkova2024thecompletegenome pages 20-22). This proteinaceous interface is a key morphological feature that distinguishes periplasmic sulfur globules from other intracellular sulfur particles (petushkova2024thecompletegenome pages 20-22).

### 1.3 Envelope proteins (Sgp) and “globule organelle-like” properties
A key mechanistic concept is that sulfur globules are not just passive precipitates; in Chromatiaceae they have an envelope composed of multiple hydrophobic proteins. *A. vinosum* globules have a monolayer coat of **SgpA/B/C/D** (petushkova2024thecompletegenome pages 20-22), with functional differentiation such as SgpC involvement in expansion (kumpel2023cellbiologyof pages 1-3).

### 1.4 Sulfur relay into cytoplasmic oxidation systems
Because periplasmic S(0) is insoluble and not directly accessible to cytosolic enzymes, models emphasize **activation/translocation** of sulfur as persulfide carriers and relay proteins. A Chromatiaceae model describes mobilization via low-molecular-weight persulfide “vehicles” (e.g., glutathione persulfide) and transfer through relay proteins (rhodanese-like proteins, TusA, DsrE/E2, DsrEFH) to **DsrC**, with persulfated DsrC feeding the reverse Dsr pathway (petushkova2024thecompletegenome pages 20-22).

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 2023: In vivo localization and non-essentiality of SgpD for globule formation
A fluorescence-microscopy study in *Allochromatium vinosum* localized a candidate envelope protein **SgpD** to sulfur deposits, reporting that it “co-localized…with the highly light-refractive sulfur deposits” in sulfide-fed cells (kumpel2023cellbiologyof pages 1-3). The same work concludes that SgpD is a component of the globule envelope yet is “neither essential…nor for sulfur globule formation” (kumpel2023cellbiologyof pages 10-11). This supports a curation stance where SgpD is an **envelope component** but not necessarily an **essential causal determinant** of the trait in all conditions.

**Quantitative statistics (2023):** 
- Globules up to **~1 µm** and up to **34% of cell dry weight** in *A. vinosum* (kumpel2023cellbiologyof pages 1-3).
- sgpD transcription induction reported as **28-fold (sulfide) and 6-fold (thiosulfate)** vs malate (kumpel2023cellbiologyof pages 1-3).

### 2.2 2024: Genome-based reinforcement of Sgp coat and sulfur-relay model in purple sulfur bacteria
A 2024 genome/physiology analysis reiterates that Chromatiaceae “accumulate molecular sulfur in the periplasmic space in the form of globules surrounded by the protein coat” and specifies the four coat proteins **SgpA/B/C/D** in *A. vinosum* (petushkova2024thecompletegenome pages 20-22). It further provides a detailed relay model for moving sulfur equivalents from globules into cytoplasmic oxidation (rhodanese/TusA/DsrE(E2)/DsrEFH → DsrC → DsrAB) (petushkova2024thecompletegenome pages 20-22). This is useful for TraitMech causal-graph entities even when some steps are framed as model/“likely” rather than directly proven for all taxa.

### 2.3 2024: Alternative intracellular sulfur oxidation mechanism involving SQR–PDO–Sox in Beggiatoa
A 2024 mechanistic study in *Beggiatoa leptomitoformis* provides evidence for intracellular elemental sulfur storage and a linked oxidation route that does **not** require canonical rDsr/sHdr genes. It reports that “The initial oxidation of sulfide occurs in the cytoplasm under the action of SQR” and highlights PDO acting on glutathione persulfide with the reaction “GSSH + O2 + H2O →GSH + SO3(2−)+ 2H+” (rudenko2024mechanismofintracellular pages 10-12, rudenko2024mechanismofintracellular pages 1-2). The study links these intracellular steps to periplasmic branched Sox oxidation, noting that in the periplasm “oxidation by the branched Sox-system” produces “elemental sulfur and sulfate” (rudenko2024mechanismofintracellular pages 10-12).

**Quantitative statistics (2024):**
- Elemental sulfur up to **~70% of cell dry weight** under sulfide-fed chemolithoautotrophy (rudenko2024mechanismofintracellular pages 10-12).
- Differential expression during endogenous sulfur utilization: **soxAX/soxB ~15-fold**, **soxY ~8.6-fold** upregulated vs sulfide-grown condition (rudenko2024mechanismofintracellular pages 10-12).

### 2.4 2024: Mineral-linked sulfur metabolism and globule-associated gene signatures (pyrite)
A 2024 study shows *A. vinosum* can grow autotrophically with pyrite as electron and sulfur source and reports differential expression patterns consistent with a shift toward periplasmic/membrane sulfur handling (e.g., upregulation of FccAB and SoxYZ; downregulation of cytoplasmic Dsr/Apr groups) (alarcon2024evidenceforautotrophic pages 1-2). It also reports that a type IV **SqrD** gene (Alvin_2145) is upregulated (~4.5-fold) in pyrite-grown cells, and discusses a link between SqrD presence and intracellular vs extracellular globule phenotypes (alarcon2024evidenceforautotrophic pages 18-20).

### 2.5 2024: Protein compartments that store crystalline elemental sulfur (boundary case)
A 2024 Science Advances study demonstrates a “widespread bacterial protein compartment” (encapsulin) that can store crystalline elemental sulfur. Visual evidence includes electron-dense sulfur puncta in cryo-EM and HR-TEM lattice fringes with **d-spacing 3.4 Å**, supporting crystalline sulfur inside the compartment (benisch2024awidespreadbacterial media 1a2af37b, benisch2024awidespreadbacterial media e49c5f77). This is a critical conceptual expansion of “sulfur storage” but is likely distinct from periplasmic sulfur globules as defined in Chromatiaceae.

## 3) Current applications and real-world implementations

### 3.1 Biotechnology and environmental sulfur management (H2S detoxification / sulfur recovery)
Mechanistic understanding of sulfur globule formation supports strategies to convert toxic sulfide into less reactive elemental sulfur for removal/recovery, including proposals to use bacteria with sulfide oxidation capacity to generate recoverable sulfur globules (rudenko2024mechanismofintracellular pages 1-2). While the cited example focuses on cytoplasmic globule formation in an aerobic/heterotrophic system, the conceptual application—biological conversion of H2S to S(0) solids—translates to broader sulfur-oxidation engineering.

### 3.2 Mineral–microbe interactions and biogeochemical cycling
Pyrite-supported growth of purple sulfur bacteria emphasizes that insoluble mineral substrates can drive distinct sulfur metabolic states and potentially yield polymeric sulfur products on mineral surfaces, relevant to natural settings and engineered “artificial photosynthesis” concepts discussed in that work (alarcon2024evidenceforautotrophic pages 1-2).

## 4) Expert opinions and authoritative analysis

### 4.1 Envelope indispensability and unresolved formation chemistry
A synthesis on sulfur metabolism in phototrophic bacteria emphasizes that sulfur globules arise from oxidation intermediates, but that key steps remain unresolved: polysulfides are primary oxidation products and it remains “unclear how polysulfides are converted into sulfur globules” (dahl2017sulfurmetabolismin pages 14-17). This supports curating some formation steps (e.g., “polysulfide → globule”) as **uncertain** unless supported by taxon-specific primary evidence.

### 4.2 Modular and lineage-specific sulfur metabolism
The same synthesis characterizes dissimilatory sulfur metabolism as modular across organisms (dahl2017sulfurmetabolismin pages 1-4). Practically, this means the causal graph should support multiple alternative subgraphs (e.g., Chromatiaceae Sgp + Dsr relay; Beggiatoa SQR/PDO/Sox) rather than enforcing a single universal pathway.

## 5) Candidate causal graph entities (nodes), grouped by type

### 5.1 Trait node
- **sulfur globule** (METPO:traitmech:000069)

### 5.2 Chemicals / metabolites (suggested CURIEs)
- **hydrogen sulfide** (CHEBI:18421)
- **thiosulfate(2−)** (CHEBI:30087)
- **elemental sulfur** (CHEBI:24866)
- **sulfane sulfur / polysulfide pool** (CHEBI:61702; polysulfide CHEBI:29256) 
- **sulfite(2−)** (CHEBI:16551)
- **sulfate(2−)** (CHEBI:16189)
- **glutathione persulfide (GSSH)** (label-only; mentioned as glutathione persulfide) (petushkova2024thecompletegenome pages 20-22, rudenko2024mechanismofintracellular pages 1-2)

### 5.3 Cellular structures / localizations
- **periplasmic space** (GO:0042597)
- **cytoplasm** (GO:0005737)
- **sulfur globule envelope / protein coat** (label-only structural entity) (petushkova2024thecompletegenome pages 20-22, kumpel2023cellbiologyof pages 10-11)

### 5.4 Genes / proteins / complexes (label-only unless specific UniProt IDs are curated later)
- **SgpA, SgpB, SgpC, SgpD** (sulfur globule envelope proteins) (petushkova2024thecompletegenome pages 20-22, kumpel2023cellbiologyof pages 1-3)
- **SQR (sulfide:quinone oxidoreductase; EC:1.8.5.4)** (rudenko2024mechanismofintracellular pages 10-12, rudenko2024mechanismofintracellular pages 1-2)
- **PDO (persulfide dioxygenase)** (rudenko2024mechanismofintracellular pages 1-2)
- **Sox system (branched Sox; soxAXBYZ genes)** (rudenko2024mechanismofintracellular pages 10-12)
- **Dsr relay components:** rhodanese-like proteins, TusA, DsrE/DsrE2, DsrEFH, **DsrC** (petushkova2024thecompletegenome pages 20-22)
- **rDsrAB (reverse dissimilatory sulfite reductase)** (kumpel2023cellbiologyof pages 1-3)
- **FccAB (flavocytochrome c sulfide dehydrogenase; periplasmic/membrane-associated)** (alarcon2024evidenceforautotrophic pages 1-2)

### 5.5 Environmental / experimental factors
- **sulfide availability** (CHEBI:18421) (kumpel2023cellbiologyof pages 1-3)
- **thiosulfate availability** (CHEBI:30087) (kumpel2023cellbiologyof pages 1-3)
- **pyrite (FeS2) as substrate** (ENVO:00001995; label if ENVO mismatch) (alarcon2024evidenceforautotrophic pages 1-2)
- **oxygen exposure (assay factor for fluorescence maturation)** (CHEBI:15379 dioxygen) (kumpel2023cellbiologyof pages 1-3)

## 6) Evidence-backed candidate causal edges (triples)

The following table is intended to be directly convertible into `data/traits/morphology/sulfur_globule.yaml` edges, with uncertainty notes.

| Edge (S–P–O) | Evidence organism/context | Reference (DOI + URL + year) | Supporting snippet | Notes/uncertainty for curation | Suggested ontology grounding (subject; object) |
|---|---|---|---|---|---|
| sulfide availability — positively_regulates — sulfur globule formation | *Allochromatium vinosum*; sulfide-fed purple sulfur bacterium | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “co-localized it exactly with the highly light-refractive sulfur deposits seen in sulfide-fed *A. vinosum* cells” (kumpel2023cellbiologyof pages 1-3) | Supports sulfide-dependent appearance of sulfur deposits/globules in *A. vinosum*; phenotype-specific and taxon-specific. | CHEBI:18421 hydrogen sulfide; METPO:traitmech:000069 sulfur globule |
| thiosulfate availability — positively_regulates — sgpD transcription | *Allochromatium vinosum*; sulfur globule protein candidate | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “sgpD transcription increases strongly on sulfide/thiosulfate” and “28-fold and 6-fold increases” (kumpel2023cellbiologyof pages 1-3) | Strong evidence for regulation of a globule-envelope-associated gene by sulfur substrates; indirect edge to globule phenotype. | CHEBI:30087 thiosulfate(2-); label:SgpD |
| sulfide or thiosulfate addition — positively_regulates — sgp genes | Phototrophic sulfur bacteria review, mainly Chromatiaceae/*A. vinosum* | 10.1007/978-3-319-51365-2_2; https://doi.org/10.1007/978-3-319-51365-2_2; 2017 | “sgp gene expression increases strongly upon sulfide or thiosulfate addition” (dahl2017sulfurmetabolismin pages 14-17) | Foundational review support; useful but older and partly synthesis rather than single experiment. | CHEBI:18421 hydrogen sulfide / CHEBI:30087 thiosulfate(2-); label:sgp genes |
| sulfur globule — located_in — periplasmic space | Chromatiaceae / purple sulfur bacteria | 10.3390/microorganisms12020391; https://doi.org/10.3390/microorganisms12020391; 2024 | “accumulate molecular sulfur in the periplasmic space in the form of globules” (petushkova2024thecompletegenome pages 20-22) | Good definition edge for trait scope in Chromatiaceae; not universal across all sulfur bacteria. | METPO:traitmech:000069 sulfur globule; GO:0042597 periplasmic space |
| sulfur globule — has_participant_location — extracytoplasmic compartment | *Allochromatium vinosum* | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “obligatory intracellular – but extracytoplasmic – intermediates” (kumpel2023cellbiologyof pages 1-3) | Important boundary statement: intracellular but not cytoplasmic in *A. vinosum*. | METPO:traitmech:000069 sulfur globule; GO:0042597 periplasmic space |
| SgpA/SgpB/SgpC/SgpD protein coat — surrounds — sulfur globule | Chromatiaceae / *Allochromatium vinosum* DSM 180T | 10.3390/microorganisms12020391; https://doi.org/10.3390/microorganisms12020391; 2024 | “a monolayer of four sulfur globule proteins SgpA/B/C/D” (petushkova2024thecompletegenome pages 20-22) | Strong structural edge for envelope composition in *A. vinosum*; likely curate as taxon-grounded. | label:SgpABCD sulfur globule proteins; METPO:traitmech:000069 sulfur globule |
| SgpC — positively_regulates — sulfur globule expansion | *Allochromatium vinosum* / Chromatiaceae | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “SgpC is involved in the expansion of the sulfur globules” (kumpel2023cellbiologyof pages 1-3) | Direct mechanistic role; likely strong candidate node/edge. | label:SgpC; METPO:traitmech:000069 sulfur globule |
| SgpD — component_of — sulfur globule envelope | *Allochromatium vinosum* fluorescence localization | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “SgpD is tightly bound to sulfur globules and represents a novel component of their proteinaceous envelope” (kumpel2023cellbiologyof pages 10-11) | Good localization evidence; authors also report non-essentiality for formation, so structural component but not required. | label:SgpD; label:sulfur globule envelope |
| loss_of_sgpD — does_not_prevent — sulfur globule formation | *Allochromatium vinosum* insertional inactivation | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “is neither essential for growth on sulfide nor for sulfur globule formation during its oxidation” (kumpel2023cellbiologyof pages 10-11) | Negative edge; useful warning against over-curating SgpD as essential. | label:sgpD loss-of-function; METPO:traitmech:000069 sulfur globule |
| sulfur globule envelope — required_for — intracellular sulfur formation/deposition | *Allochromatium vinosum* / Chromatiaceae review synthesis | 10.1007/978-3-319-51365-2_2; https://doi.org/10.1007/978-3-319-51365-2_2; 2017 | “The envelope is indispensable for formation and deposition of intracellular sulfur in *A. vinosum*.” (dahl2017sulfurmetabolismin pages 14-17) | Strong but older review statement; may need primary mutational source before final curation. | label:sulfur globule envelope; METPO:traitmech:000069 sulfur globule |
| SQR — produces — sulfane sulfur | *Beggiatoa leptomitoformis* model for intracellular sulfur oxidation | 10.3390/ijms252010962; https://doi.org/10.3390/ijms252010962; 2024 | “The initial oxidation of sulfide occurs in the cytoplasm under the action of SQR,” producing sulfane sulfur (rudenko2024mechanismofintracellular pages 10-12, rudenko2024mechanismofintracellular pages 1-2) | Strong mechanistic edge in Beggiatoa; may generalize broadly to sulfur-oxidizers with caution. | EC:1.8.5.4 sulfide:quinone oxidoreductase; CHEBI:61702 sulfane sulfur |
| SQR-mediated sulfide oxidation — produces — polysulfide / H2Sn intermediates | Recombinant *E. coli* and *Corynebacterium vitaeruminis* with SQR | 10.1128/aem.01941-21; https://doi.org/10.1128/aem.01941-21; 2022 | “SQR oxidized H2S into short-chain inorganic polysulfide (H2Sn, n ≥ 2)” (rudenko2024mechanismofintracellular pages 1-2) | Relevant biochemical mechanism, but non-classical sulfur-globule system and not 2023–2024; curate as broader sulfur-chemistry support. | EC:1.8.5.4; CHEBI:29256 polysulfide |
| polysulfide / sulfane sulfur — precursor_of — elemental sulfur globule | Cytoplasmic sulfur globule pathway in aerobic bacteria; broader sulfur oxidation review | 10.1128/aem.01941-21; https://doi.org/10.1128/aem.01941-21; 2022 | “After GSH was depleted, SQR simply oxidized H2S to H2Sn, which spontaneously generated S8. S8 aggregated into sulfur globules” (rudenko2024mechanismofintracellular pages 1-2) | Strong chemical-pathway edge, but from cytoplasmic globules in aerobic bacteria rather than periplasmic Chromatiaceae. | CHEBI:29256 polysulfide / CHEBI:61702 sulfane sulfur; METPO:traitmech:000069 sulfur globule |
| PDO — oxidizes — glutathione persulfide to sulfite | *Beggiatoa leptomitoformis*; endogenous sulfur oxidation | 10.3390/ijms252010962; https://doi.org/10.3390/ijms252010962; 2024 | “PDO therefore does not oxidize elemental sulfur directly but acts on GSSH” and “GSSH + O2 + H2O → GSH + SO3^2− + 2H+” (rudenko2024mechanismofintracellular pages 1-2) | Strong enzymatic edge; subject/object are well defined. | label:persulfide dioxygenase (PDO); CHEBI:16551 sulfite |
| sulfite — reacts_with — sulfane sulfur to form thiosulfate | *Beggiatoa leptomitoformis* proposed intracellular sulfur oxidation route | 10.3390/ijms252010962; https://doi.org/10.3390/ijms252010962; 2024 | “sulfite can react with sulfane sulfur to form thiosulfate” (rudenko2024mechanismofintracellular pages 1-2, rudenko2024mechanismofintracellular pages 10-12) | Chemical step, partly inferred in pathway model; curate with uncertainty tag. | CHEBI:16551 sulfite / CHEBI:61702 sulfane sulfur; CHEBI:30087 thiosulfate(2-) |
| thiosulfate — transported_to — periplasm | *Beggiatoa leptomitoformis* sulfur oxidation model | 10.3390/ijms252010962; https://doi.org/10.3390/ijms252010962; 2024 | “thiosulfate, which is then probably transported into the periplasm” (rudenko2024mechanismofintracellular pages 10-12) | Explicitly probable/inferred, not directly demonstrated. Mark uncertain. | CHEBI:30087 thiosulfate(2-); GO:0042597 periplasmic space |
| branched Sox system — oxidizes — thiosulfate to sulfate | *Beggiatoa leptomitoformis* | 10.3390/ijms252010962; https://doi.org/10.3390/ijms252010962; 2024 | “In the periplasm, there occurs its oxidation by the branched Sox-system with the formation of elemental sulfur and sulfate.” (rudenko2024mechanismofintracellular pages 10-12) | Strong pathway edge for Beggiatoa; produces both sulfur and sulfate, reflecting branching. | label:branched Sox system; CHEBI:16189 sulfate |
| soxAX / soxB / soxY upregulation — associated_with — endogenous sulfur globule consumption | *Beggiatoa leptomitoformis* starvation on endogenous sulfur | 10.3390/ijms252010962; https://doi.org/10.3390/ijms252010962; 2024 | “soxAX and soxB were ~15-fold upregulated and soxY ~8.6-fold upregulated” (rudenko2024mechanismofintracellular pages 10-12) | Expression association rather than direct causation; still valuable supporting evidence for sulfur oxidation during globule utilization. | label:soxAX/soxB/soxY; METPO:traitmech:000069 sulfur globule |
| rhodanese/TusA/DsrE(DsrE2)/DsrEFH — transfers persulfide sulfur to — DsrC | Chromatiaceae / *Thiocapsa bogorovii* comparative genomics and model from *A. vinosum* | 10.3390/microorganisms12020391; https://doi.org/10.3390/microorganisms12020391; 2024 | “A cascade of rhodanese, TusA, DsrE2/DsrE, and DsrC transfers persulfides” (petushkova2024thecompletegenome pages 20-22) | Useful relay edge, but some steps are model-based and may vary across taxa. | label:rhodanese/TusA/DsrE/DsrEFH; label:DsrC |
| DsrC-persulfide — substrate_for — reverse DsrAB | Chromatiaceae / sulfur globule oxidation model | 10.3390/microorganisms12020391; https://doi.org/10.3390/microorganisms12020391; 2024 | “culminating in persulfated DsrC which is a likely substrate for reverse (dissimilatory) sulfite reductase DsrAB” (petushkova2024thecompletegenome pages 20-22) | Important mechanistic edge, but phrased as “likely”; curate as uncertain/model-supported. | label:DsrC-persulfide; EC:1.8.99.5 DsrAB |
| rDsrAB system — required_for — further oxidation of stored sulfur | *Allochromatium vinosum* | 10.20944/preprints202306.1429.v1; https://doi.org/10.20944/preprints202306.1429.v1; 2023 | “A. vinosum requires the rDsr system (rDsrAB) for further oxidation of sulfur in the cytoplasm” (kumpel2023cellbiologyof pages 1-3) | Strong pathway edge for sulfur globule consumption after storage. | label:rDsrAB; METPO:traitmech:000069 sulfur globule |
| periplasmic or membrane-bound sulfur proteins (e.g., FccAB, SoxYZ) — upregulated_in — pyrite-grown cells | *Allochromatium vinosum* grown on pyrite | 10.1128/aem.00863-24; https://doi.org/10.1128/aem.00863-24; 2024 | “genes encoding periplasmic or membrane-bound proteins (e.g., FccAB and SoxYZ) were largely upregulated” (alarcon2024evidenceforautotrophic pages 1-2) | Expression/context edge linking external sulfur mineral use to periplasmic sulfur handling; not direct proof of globule biogenesis. | label:FccAB/SoxYZ; ENVO:00001995 pyrite |
| pyrite as electron/sulfur source — associated_with — polymeric sulfur formation | *Allochromatium vinosum* pyrite-supported autotrophic growth | 10.1128/aem.00863-24; https://doi.org/10.1128/aem.00863-24; 2024 | “Characterization of the biologically reacted pyrite indicates the presence of polymeric sulfur.” (alarcon2024evidenceforautotrophic pages 1-2) | Good environmental/material context; sulfur product may be globular or other polymeric sulfur, so phenotype connection is indirect. | ENVO:00001995 pyrite; CHEBI:24866 elemental sulfur |
| sulfur source concentration/type — influences — elemental sulfur accumulation in encapsulin | Desulfurase encapsulin compartment | 10.1126/sciadv.adk9345; https://doi.org/10.1126/sciadv.adk9345; 2024 | “Sulfur accumulation can be influenced by the concentration and type of sulfur source in growth medium.” (from paper abstract summarized in search results) | Distinct sulfur-storage compartment, not classical sulfur globule/inclusion; curate only as boundary case. | label:environmental sulfur source; label:encapsulin sulfur compartment |
| desulfurase-loaded encapsulin — sequesters_and_stores — elemental sulfur | Widespread bacterial protein compartment | 10.1126/sciadv.adk9345; https://doi.org/10.1126/sciadv.adk9345; 2024 | “desulfurase encapsulins can sequester and store large amounts of crystalline elemental sulfur” (benisch2024awidespreadbacterial media 1a2af37b, benisch2024awidespreadbacterial media e49c5f77) | Important related storage morphology but likely outside TraitMech sulfur globule scope; boundary case only. | label:desulfurase encapsulin; CHEBI:24866 elemental sulfur |
| encapsulated desulfurase activity — positively_regulates — elemental sulfur crystal formation inside encapsulin | Desulfurase encapsulin with L-cysteine donor | 10.1126/sciadv.adk9345; https://doi.org/10.1126/sciadv.adk9345; 2024 | “Elemental sulfur crystals can be formed inside the encapsulin shell in a desulfurase-dependent manner with l-cysteine as the sulfur donor.” (benisch2024awidespreadbacterial media 1a2af37b, benisch2024awidespreadbacterial media e49c5f77) | Strong for encapsulin system; not evidence for canonical periplasmic sulfur globules. | label:encapsulated desulfurase; CHEBI:24866 elemental sulfur |
| sulfur globule — distinct_from — cytoplasmic sulfur deposition in anoxygenic phototrophs | Phototrophic sulfur bacteria review | 10.1007/978-3-319-51365-2_2; https://doi.org/10.1007/978-3-319-51365-2_2; 2017 | “in all anoxygenic phototrophs sulfur intermediates ‘are never deposited in the cytoplasm’” (dahl2017sulfurmetabolismin pages 14-17) | Important boundary edge for scope; excludes cytoplasmic sulfur particles in some other bacteria from this trait instance. | METPO:traitmech:000069 sulfur globule; GO:0005737 cytoplasm |


*Table: This table lists evidence-backed candidate subject–predicate–object edges for curation of the sulfur globule trait, emphasizing 2023–2024 sources and noting uncertainty where claims are model-based, taxon-specific, or boundary cases such as encapsulin sulfur storage.*

## 7) Warnings / claims that should not yet be curated (or should be curated as uncertain)

1. **“Polysulfides → sulfur globules”** is explicitly described as mechanistically unresolved in authoritative synthesis for phototrophic sulfur bacteria; treat as uncertain unless backed by direct taxon-specific mechanistic evidence (dahl2017sulfurmetabolismin pages 14-17).
2. **SgpD essentiality:** SgpD is a globule-envelope component but **not essential** for globule formation in *A. vinosum* under tested conditions; avoid curating “sgpD required_for globule formation” as a strong edge (kumpel2023cellbiologyof pages 10-11).
3. **Thiosulfate transport to periplasm** in *Beggiatoa leptomitoformis* is framed as “probably transported”; curate as uncertain/inferred (rudenko2024mechanismofintracellular pages 10-12).
4. **Encapsulin sulfur storage** is well supported (including visual crystallinity evidence) but is likely a different morphological class than periplasmic sulfur globules in phototrophs; curate only as boundary/related trait unless METPO scope is expanded (benisch2024awidespreadbacterial media 1a2af37b, benisch2024awidespreadbacterial media e49c5f77).

## 8) DOI-first bibliography (with URLs and publication dates where available)

- **Rudenko TS, et al.** *Mechanism of Intracellular Elemental Sulfur Oxidation in Beggiatoa leptomitoformis, Where Persulfide Dioxygenase Plays a Key Role.* **Int J Mol Sci** (Oct **2024**). DOI: **10.3390/ijms252010962**. URL: https://doi.org/10.3390/ijms252010962 (rudenko2024mechanismofintracellular pages 1-2, rudenko2024mechanismofintracellular pages 10-12)
- **Petushkova E, et al.** *The Complete Genome of a Novel Typical Species Thiocapsa bogorovii and Analysis of Its Central Metabolic Pathways.* **Microorganisms** (Feb **2024**). DOI: **10.3390/microorganisms12020391**. URL: https://doi.org/10.3390/microorganisms12020391 (petushkova2024thecompletegenome pages 20-22)
- **Alarcon HV, et al.** *Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source.* **Applied and Environmental Microbiology** (Jul **2024**). DOI: **10.1128/aem.00863-24**. URL: https://doi.org/10.1128/aem.00863-24 (alarcon2024evidenceforautotrophic pages 1-2, alarcon2024evidenceforautotrophic pages 18-20)
- **Benisch R, Andreas MP, Giessen TW.** *A widespread bacterial protein compartment sequesters and stores elemental sulfur.* **Science Advances** (Feb **2024**). DOI: **10.1126/sciadv.adk9345**. URL: https://doi.org/10.1126/sciadv.adk9345 (benisch2024awidespreadbacterial media 1a2af37b, benisch2024awidespreadbacterial media e49c5f77)
- **Kümpel C, Grein F, Dahl C.** *Cell Biology of a Purple Sulfur Bacterium: Fluorescence Microscopy of Intracellular Sulfur Globules in Allochromatium vinosum.* **Preprint** (Jun **2023**). DOI: **10.20944/preprints202306.1429.v1**. URL: https://doi.org/10.20944/preprints202306.1429.v1 (kumpel2023cellbiologyof pages 1-3, kumpel2023cellbiologyof pages 10-11)
- **Dahl C.** *Sulfur Metabolism in Phototrophic Bacteria.* (Book chapter; Jan **2017**). DOI: **10.1007/978-3-319-51365-2_2**. URL: https://doi.org/10.1007/978-3-319-51365-2_2 (dahl2017sulfurmetabolismin pages 14-17, dahl2017sulfurmetabolismin pages 1-4)
- **Wang T, et al.** *The Pathway of Sulfide Oxidation to Octasulfur Globules in the Cytoplasm of Aerobic Bacteria.* **Applied and Environmental Microbiology** (Feb **2022**). DOI: **10.1128/aem.01941-21**. URL: https://doi.org/10.1128/aem.01941-21 (rudenko2024mechanismofintracellular pages 1-2)



References

1. (kumpel2023cellbiologyof pages 1-3): Carolin Kümpel, Fabian Grein, and Christiane Dahl. Cell biology of a purple sulfur bacterium: fluorescence micros-copy of intracellular sulfur globules in allochromatium vinosum. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.1429.v1, doi:10.20944/preprints202306.1429.v1.

2. (petushkova2024thecompletegenome pages 20-22): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

3. (dahl2017sulfurmetabolismin pages 14-17): Christiane Dahl. Sulfur metabolism in phototrophic bacteria. ArXiv, pages 27-66, Jan 2017. URL: https://doi.org/10.1007/978-3-319-51365-2\_2, doi:10.1007/978-3-319-51365-2\_2. This article has 98 citations.

4. (rudenko2024mechanismofintracellular pages 1-2): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

5. (benisch2024awidespreadbacterial media 1a2af37b): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 22 citations and is from a highest quality peer-reviewed journal.

6. (benisch2024awidespreadbacterial media e49c5f77): Robert Benisch, Michael P. Andreas, and Tobias W. Giessen. A widespread bacterial protein compartment sequesters and stores elemental sulfur. Science Advances, Feb 2024. URL: https://doi.org/10.1126/sciadv.adk9345, doi:10.1126/sciadv.adk9345. This article has 22 citations and is from a highest quality peer-reviewed journal.

7. (rudenko2024mechanismofintracellular pages 10-12): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

8. (kumpel2023cellbiologyof pages 10-11): Carolin Kümpel, Fabian Grein, and Christiane Dahl. Cell biology of a purple sulfur bacterium: fluorescence micros-copy of intracellular sulfur globules in allochromatium vinosum. Unknown journal, Jun 2023. URL: https://doi.org/10.20944/preprints202306.1429.v1, doi:10.20944/preprints202306.1429.v1.

9. (alarcon2024evidenceforautotrophic pages 1-2): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 5 citations and is from a peer-reviewed journal.

10. (alarcon2024evidenceforautotrophic pages 18-20): Hugo V. Alarcon, Jonathon E. Mohl, Grace W. Chong, Ana Betancourt, Yi Wang, Weinan Leng, Jason C. White, and Jie Xu. Evidence for autotrophic growth of purple sulfur bacteria using pyrite as electron and sulfur source. Jul 2024. URL: https://doi.org/10.1128/aem.00863-24, doi:10.1128/aem.00863-24. This article has 5 citations and is from a peer-reviewed journal.

11. (dahl2017sulfurmetabolismin pages 1-4): Christiane Dahl. Sulfur metabolism in phototrophic bacteria. ArXiv, pages 27-66, Jan 2017. URL: https://doi.org/10.1007/978-3-319-51365-2\_2, doi:10.1007/978-3-319-51365-2\_2. This article has 98 citations.