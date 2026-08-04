---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:24:07.341335'
end_time: '2026-08-04T02:33:52.274491'
duration_seconds: 584.93
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta mid2
  trait_identifier: METPO:1000476
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 3\u20134 pH units, characteristic of organisms with broad pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_3_4
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports broad pH-homeostasis flexibility as the basis of generalist pH-tolerance
    physiology.)'
  causal_graph_summary: 'ph_delta_mid2_broad_breadth: 15 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000476
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 3–4 pH units, characteristic of organisms with broad pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_3_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports broad pH-homeostasis flexibility as the basis of generalist pH-tolerance physiology.)
- **Existing causal graph summary:** ph_delta_mid2_broad_breadth: 15 nodes, 8 edges

## Research Objective

Research the microbial trait **pH delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid2.yaml`.

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
- **Trait label:** pH delta mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000476
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 3–4 pH units, characteristic of organisms with broad pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_3_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports broad pH-homeostasis flexibility as the basis of generalist pH-tolerance physiology.)
- **Existing causal graph summary:** ph_delta_mid2_broad_breadth: 15 nodes, 8 edges

## Research Objective

Research the microbial trait **pH delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_mid2.yaml`.

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


# Curation report: pH delta mid2

## 1. Scope and recommended interpretation

**Target:** **pH delta mid2**  
**Identifier:** **METPO:1000476**  
**Parent:** METPO:1000232  
**Synonym:** `pHd_3_4`  
**Recommended operational meaning:** an organism-level, assay-observed phenotype in which reproducible growth is supported across an approximately **3–4 pH-unit interval** under otherwise defined conditions.

The trait should encode **breadth**, not the location of the interval. Thus, organisms growing over pH 4–7 and pH 7–10 could both satisfy the breadth class despite different optima and acid/alkaline physiology. The endpoints should ideally be calculated from growth rate, biomass yield, or another prespecified growth threshold relative to the organism’s maximum, using the same medium, temperature, atmosphere, incubation time, and inoculum across the pH series.

The mechanistic center of the graph should be **cytoplasmic pH homeostasis**: bacteria generally preserve a much narrower intracellular pH than the external range supporting growth. In neutralophiles, cytoplasmic pH is commonly maintained near 7.5–7.7; respiratory proton extrusion and proton-consuming metabolism dominate on the acidic side, whereas proton uptake through cation/H+ antiport, ATP synthase, and associated ion cycles becomes important on the alkaline side. These mechanisms vary substantially among taxa and physiological conditions. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 1-3)

### Boundary cases

1. **Not pH optimum or environmental preference.** A pH optimum is a location parameter; pH delta is a range width. Ramoneda et al. inferred ecological pH preferences from distributions across 795 soil and 675 freshwater samples spanning pH 3–10, rather than directly measuring each organism’s growth breadth. Such preference estimates should not be asserted as METPO:1000476 observations. (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 5-6)
2. **Not acute survival or recovery.** Survival after exposure to pH 2, or regrowth after a short pH 4/11 pulse, is an acid/alkali-resistance endpoint, not evidence that sustained growth occurs at those pH values.
3. **Not acid tolerance alone.** Gad, Hde, urease, or other acid-resistance mechanisms may establish the acidic endpoint but do not by themselves demonstrate a 3–4-unit total growth range.
4. **Not alkaliphily alone.** NhaA/Mrp-dependent growth at high pH establishes an alkaline mechanism, not breadth across both sides of an optimum.
5. **Not community abundance.** Ecological interactions can reverse monoculture expectations. For example, many tested *Bacteroides* were sensitive at pH 5.5 or below in isolation but expanded in acidified mouse intestinal communities. (ng2023singlestrainbehaviorpredicts pages 10-11)
6. **Not unbuffered endpoint pH.** Metabolic acidification or alkalinization can change exposure during growth; initial and final pH, buffer identity/capacity, and organic-acid concentrations should be reported.

## 2. Candidate graph architecture

A defensible graph should use a **two-arm model**:

- **Acid-side arm:** low external pH → proton influx/macromolecular damage → proton extrusion or consumption, reduced membrane permeability, protein/DNA/envelope protection → maintenance of intracellular pH and growth.
- **Alkaline-side arm:** high external pH → proton scarcity and cation stress → electrogenic Na+(K+)/H+ antiport, respiratory-chain energization, proton capture by ATP synthase, envelope-associated proton retention → maintenance of intracellular pH and growth.
- **Convergence:** successful function of both arms across the assay interval → sustained metabolic activity and cell-envelope integrity → observed growth over a 3–4-unit pH interval.

The final convergence into **METPO:1000476** remains a mechanistic synthesis, because the retrieved intervention studies generally test one pH extreme rather than directly showing that perturbing one node changes the measured breadth by 3–4 units.

## 3. Candidate nodes grouped by type

### A. Trait, environment, and assay nodes

| Candidate node | Type | Grounding/comment |
|---|---|---|
| pH delta mid2 | Trait class | **METPO:1000476** |
| parent pH-delta phenotype | Trait class | METPO:1000232 |
| external/environmental pH | Environmental factor | Prefer a verified ENVO/PATO/OBA term during implementation; do not invent a CURIE |
| acidic external pH | Experimental/environmental state | Label-only pending ontology verification |
| alkaline external pH | Experimental/environmental state | Label-only pending ontology verification |
| growth-supporting pH interval | Assay-derived property | Label-only; explicitly store approximately 3–4 pH units |
| growth rate; biomass yield; lag time | Assay outputs | Label-only unless project conventions specify ontology terms |
| buffer capacity, medium composition, oxygen availability, temperature, salinity/osmolality | Experimental modifiers | Essential qualifiers: oxygen and cation availability can change transporter and respiratory mechanisms (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 3-5) |

### B. Core processes and energetic entities

| Candidate node | Type | Grounding/comment |
|---|---|---|
| cellular/cytoplasmic pH homeostasis | Biological process | **GO:0006885** (regulation of pH); verify whether a more specific child is preferred |
| proton transmembrane transport | Biological process | **GO:1902600** |
| proton motive force | Energetic state/process | Label-only recommended; comprises ΔpH and membrane potential Δψ |
| respiratory-chain proton extrusion | Process/module | Label-only or ground to taxon-specific respiratory modules |
| oxidative phosphorylation | Biological process | **GO:0006119** |
| ATP synthesis coupled proton transport | Biological process | **GO:0015986** |
| intracellular proton consumption | Process | Label-only |
| membrane permeability remodeling | Process | Label-only pending exact GO selection |
| cell-wall/peptidoglycan integrity | Process/structure | Peptidoglycan: **CHEBI:8005**; process term should be verified |
| protein-folding/protein-aggregation protection | Process | Select exact GO child only after deciding whether aggregation prevention or chaperone-mediated folding is represented |
| DNA repair | Biological process | **GO:0006281** |

### C. Transporters, complexes, proteins, and regulators

| Candidate node | Class | Curation status |
|---|---|---|
| NhaA Na+/H+ antiporter | Transporter | Strong alkaline-side exemplar in *E. coli*; label/gene symbol is safer than a species-specific UniProt CURIE until the graph’s taxon is known |
| MrpA–G cation/proton antiporter complex | Complex | Strong alkaline-side candidate; subunit requirements and transported cation vary by taxon |
| NhaD/NhaP and K+/H+ antiporters | Transporters | Useful secondary candidates; retain taxon-specific evidence |
| F0F1 ATP synthase | Complex/enzyme | Direction is conditional: ATP hydrolysis can expel/consume cytoplasmic H+ in acid stress, whereas ATP synthesis can capture H+ at high external pH |
| respiratory-chain complexes/cytochrome bd | Module | Process-level node preferred unless taxon and oxygen regime are specified |
| GadA/GadB | Glutamate decarboxylases | Strong *E. coli* acid-side candidates; EC grounding should be verified before YAML entry |
| GadC | Glutamate/GABA antiporter | Strong *E. coli* acid-side candidate |
| YbaS | Glutaminase | Acid-activated ammonia-generating candidate in *E. coli* |
| AdiA/AdiC | Arginine decarboxylase/antiporter | Taxon-specific acid-resistance module |
| CadA/CadB | Lysine decarboxylase/antiporter | Taxon-specific; reported optimum near pH 5.8 in the reviewed system (li2024responseofescherichia pages 4-5) |
| SpeF/PotE | Ornithine decarboxylase/antiporter | Taxon-specific candidate |
| HdeA/HdeB | Periplasmic acid chaperones | *E. coli* candidates acting at different acid ranges |
| PBP1a/PBP1b | Peptidoglycan synthases | Direct but opposing pH-specialist effects in *E. coli* |
| RecA and base-excision/nucleotide-excision/mismatch-repair modules | Repair proteins/pathways | Downstream damage protection, not primary pH control |
| OmpC/OmpF, cyclopropane fatty-acid synthase | Envelope components/enzymes | Acid-side membrane/porin remodeling; taxon-specific |
| two-component systems and pH-responsive regulators | Signaling/regulation | Candidate process-level node; exact systems differ among taxa (krulwich2011molecularaspectsof pages 14-15) |
| Stb5, Mac1, Rtg1/Rtg3 | Transcription factors | *Issatchenkia orientalis*-specific, primarily transcriptomic/functional-genomics candidates (dubinkina2024atranscriptomicatlas pages 1-2) |

### D. Chemicals and metabolites

| Candidate node | CURIE where confidently available | Role |
|---|---|---|
| proton | **CHEBI:24636** | Central transported/consumed species |
| sodium cation | **CHEBI:29101** | Antiporter counter-ion; salinity confounder |
| potassium cation | **CHEBI:29103** | Alternative antiporter counter-ion |
| L-glutamate | **CHEBI:29985** | Gad substrate |
| 4-aminobutanoate/GABA | **CHEBI:16865** | Gad product exported by GadC |
| L-glutamine | **CHEBI:18050** | YbaS substrate |
| ammonia | **CHEBI:16134** | Basic product that neutralizes protons |
| carbon dioxide | **CHEBI:16526** | Decarboxylation product |
| putrescine | **CHEBI:17148** | Community-level, pH-dependent modifier; not a universal breadth determinant |
| ATP | **CHEBI:15422** | Energy substrate/product whose role depends on ATPase direction |
| ADP | **CHEBI:16761** | ATPase product/substrate |
| arginine, lysine, ornithine, serine | Chemicals | Ground exact protonation-state CURIEs according to project conventions |

## 4. Candidate causal edges

The compact table below gives the strongest proposed triples and their curation disposition.

| candidate triple (subject — predicate — object) | evidence tier | organism/context | DOI | curation decision |
|---|---|---|---|---|
| external pH variation — causally challenges/elicits — cytoplasmic pH homeostasis | High | broad bacterial scope; neutralophiles and extremophiles in review synthesis | 10.1038/nrmicro2549 | Curate as core environmental-input edge (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) |
| NhaA Na+/H+ antiporter — enables — alkaline pH homeostasis / proton uptake via electrogenic antiport | High | *Escherichia coli*; alkaline adaptation in sodium-containing environments | 10.1038/nrmicro2549 | Curate, but annotate as taxon-tested exemplar rather than universal single-gene mechanism (krulwich2011molecularaspectsof pages 6-8) |
| Mrp antiporter complex — enables — alkaline pH homeostasis | High | alkaliphilic/halotolerant bacteria including *Bacillus* spp. and *Halomonas* sp. Y2; deletion/complementation evidence | 10.1038/nrmicro2549; 10.1074/jbc.M116.751016; 10.3389/fmicb.2017.02325 | Curate with note that specific subunits/ion specificities are taxon-dependent (krulwich2011molecularaspectsof pages 12-14, cheng(程彬)2016alkalineresponseof pages 8-9, cheng(程彬)2016alkalineresponseof pages 5-6, ito2017mrpantiportershave pages 1-2) |
| GadA/GadB glutamate decarboxylases + GadC antiporter — causes — proton consumption / glutamate-to-GABA acid resistance cycle | High | *E. coli* acid stress; survival impairment when system components are deleted | 10.3390/microorganisms12091774 | Curate as strong acid-side mechanism; taxon-specific to organisms encoding this system (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 4-5) |
| glutamate-to-GABA acid resistance cycle — promotes — acid survival | High | *E. coli* extreme acid resistance (pH 2–3 in cited review synthesis) | 10.3390/microorganisms12091774 | Curate as process-level edge if gene-level cycle node is present (li2024responseofescherichia pages 2-4) |
| F0F1-ATPase hydrolysis — consumes — intracellular H+ | High | *E. coli* under acid stress | 10.3390/microorganisms12091774 | Curate with explicit acid-stress context; do not overgeneralize directionality to all taxa/conditions (li2024responseofescherichia pages 2-4) |
| respiratory chain proton extrusion — contributes to — acid-side cytoplasmic pH homeostasis | Medium-High | neutralophilic bacteria; emphasized in broad review, exemplified by *E. coli* | 10.1038/nrmicro2549 | Curate as process-level mechanism, with broad-review support and organismal caveat (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 3-5) |
| PBP1a cell-wall synthase activity — promotes fitness at — alkaline pH | High | *E. coli* environmental pH-dependent cell-wall specialization | 10.7554/eLife.40754 | Curate as taxon-specific envelope mechanism (mueller2019plasticityofescherichia pages 1-2) |
| PBP1b cell-wall synthase activity — promotes fitness at — acidic pH | High | *E. coli* environmental pH-dependent cell-wall specialization | 10.7554/eLife.40754 | Curate as taxon-specific envelope mechanism (mueller2019plasticityofescherichia pages 1-2) |
| HdeA/HdeB chaperones — prevent — acid-induced protein aggregation | High | *E. coli*; HdeA at pH 1–3 and HdeB at pH 3–5 per review synthesis | 10.3390/microorganisms12091774 | Curate as acid-protective protein-homeostasis mechanism, taxon-specific (li2024responseofescherichia pages 5-7) |
| exogenous putrescine — enhances — glutamate/GABA pathway and ATPase-linked acidic biofilm response | Medium | biofilm-based activated sludge community; acidic pH 3–4; assay/community specific | 10.1128/AEM.00569-24 | Curate only if graph allows community-level assay-specific modifiers; otherwise hold for warning section (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6) |
| cytoplasmic pH homeostasis — increases likelihood of — broad pH growth-supporting breadth phenotype (METPO:1000476) | Inferred | cross-taxon mechanistic synthesis; not directly demonstrated as sole determinant of 3–4 unit breadth | 10.1038/nrmicro2549 | Do not yet curate as a direct phenotype edge without more direct breadth-specific evidence (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6) |


*Table: This compact table prioritizes the best-supported candidate causal edges for a TraitMech graph of pH delta mid2. It distinguishes strong mechanistic edges suitable for curation from assay-specific or still-inferred links that should be annotated cautiously.*

### Additional edge-level evidence and snippets

| Proposed triple | Supporting snippet or close source-backed wording | Interpretation and uncertainty |
|---|---|---|
| low external pH → increases → intracellular proton stress | Acid stress exposes cells to high H+; persistent intracellular acidification triggers membrane, protein, and DNA protection. (li2024responseofescherichia pages 5-7, dubinkina2024atranscriptomicatlas pages 1-2) | Mechanistically broad, but magnitude depends on membrane permeability, weak acids, and buffer composition. |
| respiratory-chain proton extrusion → promotes → acid-side pH homeostasis | Neutralophilic bacteria increase respiratory-chain complexes for proton extrusion under acid stress. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 3-5) | Curate at process level; oxygen availability can reverse expression of individual electron-transport components. |
| GadA/GadB-mediated glutamate decarboxylation → consumes → intracellular H+ | GadA/GadB convert glutamate to GABA and CO2 while consuming H+; GadC exports GABA in exchange for glutamate. (li2024responseofescherichia pages 2-4) | High confidence in *E. coli*. |
| deletion of gadA/gadB/gadC → decreases → extreme-acid survival | Deleting the components “significantly impairs survival at pH 2–3”; both GadA and GadB were required for pH-2 survival in the reviewed evidence. (li2024responseofescherichia pages 2-4) | Direct intervention evidence for survival, but survival at pH 2 is not equivalent to growth breadth. |
| YbaS glutaminase activity → produces → ammonia | YbaS converts glutamine to glutamate plus ammonia and is activated below pH 6; ammonia neutralizes intracellular protons. (li2024responseofescherichia pages 2-4) | Strong biochemical logic; retain *E. coli*/acid-side context. |
| F0F1-ATPase ATP hydrolysis → consumes/exports → cytoplasmic H+ | Under acid stress, ATP synthase operating through ATP hydrolysis consumes intracellular H+ and supports pH homeostasis. (li2024responseofescherichia pages 2-4) | Directionality is crucial; do not encode ATP synthase as having one universal effect. |
| NhaA Na+/H+ antiport → increases → proton uptake at alkaline pH | NhaA performs electrogenic 2H+/1Na+ exchange, is activated from pH 6.5–8.5, and is essential for alkaline adaptation when Na+ is present. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 6-8) | High confidence for *E. coli*; sodium dependence must be represented. |
| Mrp complex → promotes → alkaline growth/pH homeostasis | In *Halomonas* Y2, ΔHa-mrp was inhibited at pH 8 and completely inhibited at pH 10 in 15% NaCl; expression complemented Na+-sensitive *E. coli* growth at 500 mM NaCl. (cheng(程彬)2016alkalineresponseof pages 5-6) | Strong intervention evidence but extreme-salinity and taxon-specific. |
| respiratory PMF → drives → cation/H+ antiport | Cation/H+ antiporters use PMF to import protons in exchange for cytoplasmic Na+ or K+. (krulwich2011molecularaspectsof pages 3-5, cheng(程彬)2016alkalineresponseof pages 2-4) | Suitable core energetic edge. |
| PBP1a synthase activity → promotes → alkaline-pH fitness | PBP1a is required for maximal *E. coli* growth under alkaline conditions. (mueller2019plasticityofescherichia pages 1-2) | Direct and useful, but a pH-specialist envelope edge rather than a universal mechanism. |
| PBP1b synthase activity → promotes → acidic-pH fitness | PBP1b is required for maximal *E. coli* growth under acidic conditions. (mueller2019plasticityofescherichia pages 1-2) | The complementary PBP1a/PBP1b pair is a plausible breadth mechanism only in relevant taxa. |
| HdeA/HdeB → prevents → acid-induced protein aggregation | HdeA operates at approximately pH 1–3 and HdeB at pH 3–5, preventing aggregation without ATP. (li2024responseofescherichia pages 5-7) | Strong acid-protection edge; not evidence of sustained growth at pH 1–3. |
| membrane lipid remodeling → decreases → acid-associated proton influx/damage | Altering saturated/unsaturated and cyclopropane-fatty-acid composition enhances acid resistance. (li2024responseofescherichia pages 5-7, li2024responseofescherichia pages 4-5) | Exact direction and lipid species are strain- and condition-dependent; curate conservatively. |
| exogenous putrescine at pH 3–4 → promotes → biofilm viability/energy metabolism | Putrescine increased intact cells by 125%, living cells by 105%, ATP by 58%, and ADP by 26% under acidic conditions. (jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6) | Community/activated-sludge assay only; not a generic organismal graph edge. |
| exogenous putrescine at pH 8–9 → inhibits → biofilm development | Intact and living cells decreased 36% and 48%, respectively, under alkaline conditions. (jiang2024exogenousputrescineplays pages 4-6) | Demonstrates a sign reversal: putrescine cannot be modeled as a monotonic tolerance enhancer. |
| cytoplasmic pH homeostasis → enables → METPO:1000476 | Broad review evidence establishes homeostasis as the basis for growth outside the cytoplasmic pH range. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3) | **Inferred final edge.** No retrieved perturbation directly demonstrates a change into/out of the defined 3–4-unit breadth bin. |

## 5. Recent developments, applications, and statistics

### Genome-to-pH preference prediction (2023)

Ramoneda et al. analyzed **1,470 environmental samples**—795 soil and 675 freshwater—spanning pH 3–10 and representing **250,275 ASVs across 38 phyla**. They found **332 gene types** associated with pH preferences, of which **56** were consistent across soil and freshwater; **30 of those 56** already had prior links to pH adaptation. Associated functions included ATPases, ion antiporters, phosphatases, decarboxylases, and urea transporters. Taxonomy and phylogeny were comparatively poor predictors. This work supports candidate discovery and cultivation design, but its edges are associative because environmental abundance-derived preference is not growth breadth. (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-1)

### Gut isolate-to-community prediction (2023)

Ng et al. assayed **92 gut bacterial strains from 28 families** across pH and osmolality conditions. Growth was represented by normalized growth rate and OD600. Known stress-response genes explained tolerance in many but not all cases, and machine learning identified additional predictive genes/subsystems. Monoculture performance often predicted survival in mixed communities and an acidified mouse gut, supporting practical use of standardized pH-growth screens. The *Bacteroides* discrepancy nevertheless shows that strain sampling and ecological context can override a simple phenotype-to-abundance mapping. (ng2023singlestrainbehaviorpredicts pages 10-11, ng2023singlestrainbehaviorpredicts pages 1-2, ng2023singlestrainbehaviorpredicts pages 6-6)

### Multi-strain yeast transcriptomics (2024)

Dubinkina et al. compared **12 *I. orientalis* strains—six tolerant and six susceptible**—and identified hundreds of differential or reversed low-pH transcriptional responses. Candidate regulators included Stb5, Mac1, and Rtg1/Rtg3; implicated pathways included energy metabolism, translation, cell-wall integrity, RTG-dependent retrograde signaling, glycolysis, and trehalose biosynthesis. The authors explicitly call for perturbation and long-term low-pH experiments; motif analysis can yield false positives, and acute transcriptional response should not be curated as causal breadth evidence. *I. orientalis* is being developed as an acid-tolerant chassis for organic-acid and bio-based production. (dubinkina2024atranscriptomicatlas pages 1-2, dubinkina2024atranscriptomicatlas pages 18-20)

### Biofilm and wastewater engineering (2024)

In activated-sludge biofilms, putrescine had a switch-like effect: it promoted acidic-pH biofilm formation and glutamate/GABA/ATPase-associated metabolism but inhibited development at alkaline pH. At pH 3–4, polysaccharide and polysaccharide/protein measures increased **54% and 99%**; at pH 5–6, effects were not significant; at pH 8–9, viability decreased. This provides a real-world process-control lead but is unsuitable as a universal cell-autonomous edge. (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6)

### Current implementation areas

- **Industrial fermentation:** acid-tolerant *E. coli* and *I. orientalis* can reduce neutralization demand and contamination risk in organic-acid production; Gad/ATPase/envelope pathways are engineering targets. (li2024responseofescherichia pages 2-4, dubinkina2024atranscriptomicatlas pages 1-2)
- **Microbial-inoculant selection and cultivation:** genome-based pH preference models can prioritize strains and media, although they require phenotypic validation. (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 1-1)
- **Microbiome prediction:** monoculture pH-response matrices can help predict community shifts caused by intestinal acidification, drugs, or disease, but strain variation and interactions remain important. (ng2023singlestrainbehaviorpredicts pages 10-11, ng2023singlestrainbehaviorpredicts pages 1-2)
- **Wastewater biofilms:** pH-dependent polyamine supplementation may alter biofilm formation and community composition; use is conditional rather than generally beneficial. (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 4-6)
- **Antimicrobial development:** pH-homeostasis pathways are potential condition-dependent vulnerabilities, but disrupting an acid-adaptation pathway may alter persistence or virulence without changing sustained growth breadth.

## 6. Recommended initial YAML-level curation

### High-priority core nodes

1. `METPO:1000476` pH delta mid2.
2. External pH variation.
3. Acidic external pH and alkaline external pH.
4. Cytoplasmic pH homeostasis (`GO:0006885`, subject to project convention).
5. Proton transmembrane transport (`GO:1902600`).
6. Proton motive force.
7. Respiratory-chain proton extrusion.
8. Cation/H+ antiport.
9. NhaA and Mrp antiporters as taxon-qualified exemplars.
10. ATP synthase, with direction-specific activities.
11. Intracellular proton consumption.
12. GadA/GadB–GadC acid-resistance cycle as a taxon-specific module.
13. Membrane/cell-wall integrity and protein homeostasis.
14. Sustained growth across an approximately 3–4-unit pH interval.

### Suggested graph pattern

`external pH variation → challenges → cytoplasmic pH homeostasis`

Acid branch:

`low external pH → increases → proton influx/stress`  
`respiratory proton extrusion + amino-acid decarboxylation + ATPase hydrolysis → reduce → intracellular proton burden`  
`envelope remodeling + Hde chaperones + DNA repair → preserve → cellular integrity`

Alkaline branch:

`high external pH → causes → proton scarcity`  
`respiratory PMF → drives → NhaA/Mrp-mediated proton uptake`  
`ATP synthesis-coupled proton transport + cell-surface proton retention → support → cytoplasmic pH homeostasis`

Convergence:

`cytoplasmic pH homeostasis + envelope/macromolecular integrity → supports → sustained growth across tested pH values → defines → METPO:1000476`

The final convergence edges should initially carry an **inferred/mechanistic-model** qualifier rather than direct experimental evidence.

## 7. Warnings: claims not ready for TraitMech curation

1. **Do not curate all 56 Ramoneda genes as causal.** They are cross-environment associations; multifunctionality, habitat specificity, and incomplete taxonomic conservation are acknowledged limitations. (ramoneda2023buildingagenomebased pages 3-5)
2. **Do not equate pH preference with pH breadth.** Environmental abundance optima and laboratory growth-range endpoints are different phenotypes.
3. **Do not use extreme-acid survival as a growth edge.** Gad deletion effects at pH 2–3 and Hde activity at pH 1–5 support resistance mechanisms, not sustained growth at those values. (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 5-7)
4. **Do not universalize NhaA, Mrp, or Gad.** Transport stoichiometry, cation specificity, subunit requirements, expression, and physiological roles vary by species and medium. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14, patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5)
5. **Do not encode ATP synthase with an unconditional direction.** ATP hydrolysis and ATP synthesis have different proton-flow consequences, and taxa may use H+- or Na+-coupled enzymes. (li2024responseofescherichia pages 2-4, krulwich2011molecularaspectsof pages 12-14)
6. **Do not curate transcript abundance as causation.** The *I. orientalis* regulators and pathways require knockout, overexpression, rescue, or direct biochemical validation, especially under long-term growth conditions. (dubinkina2024atranscriptomicatlas pages 1-2, dubinkina2024atranscriptomicatlas pages 18-20)
7. **Do not generalize putrescine.** Its effect reverses between acidic and alkaline conditions and was measured in a mixed activated-sludge biofilm. (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 4-6)
8. **Do not assign unverified ontology identifiers.** Gene symbols and label-only nodes are preferable to an incorrect taxon-specific UniProt, EC, Rhea, KEGG, or MetaCyc identifier.
9. **Control correlated stresses.** Na+/H+ antiporter studies often combine alkalinity with high NaCl, while organic-acid experiments combine proton stress with membrane-permeant weak-acid toxicity. These require explicit experimental qualifiers.
10. **Direct breadth evidence is still missing.** The strongest future experiment would measure full pH growth curves for isogenic deletions and complemented strains, then test whether the calculated growth-supporting width moves into or out of the 3–4-unit METPO bin.

## 8. DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9, 330–343. **May 2011.** DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). Foundational synthesis of pH sensing, PMF, antiport, respiration, ATP synthase, and taxon-specific homeostasis strategies. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 6-8, krulwich2011molecularaspectsof pages 1-3)
2. Li Z, Huang Z, Gu P. “Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review.” *Microorganisms* 12:1774. **August 2024.** DOI: [10.3390/microorganisms12091774](https://doi.org/10.3390/microorganisms12091774). (li2024responseofescherichia pages 2-4, li2024responseofescherichia pages 5-7, li2024responseofescherichia pages 4-5)
3. Jiang G et al. “Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.” *Applied and Environmental Microbiology* 90. **July 2024.** DOI: [10.1128/AEM.00569-24](https://doi.org/10.1128/AEM.00569-24). (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6)
4. Dubinkina V et al. “A transcriptomic atlas of acute stress response to low pH in multiple *Issatchenkia orientalis* strains.” *Microbiology Spectrum* 12. **Published online November 2023; January 2024 issue.** DOI: [10.1128/spectrum.02536-23](https://doi.org/10.1128/spectrum.02536-23). (dubinkina2024atranscriptomicatlas pages 1-2, dubinkina2024atranscriptomicatlas pages 18-20)
5. Ramoneda J et al. “Building a genome-based understanding of bacterial pH preferences.” *Science Advances* 9. **28 April 2023.** DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 13-13)
6. Ng KM et al. “Single-strain behavior predicts responses to environmental pH and osmolality in the gut microbiota.” *mBio*. **July 2023.** DOI: [10.1128/mbio.00753-23](https://doi.org/10.1128/mbio.00753-23). (ng2023singlestrainbehaviorpredicts pages 10-11, ng2023singlestrainbehaviorpredicts pages 1-2)
7. Patiño-Ruiz M, Ganea C, Călinescu O. “Prokaryotic Na+/H+ Exchangers—Transport Mechanism and Essential Residues.” *International Journal of Molecular Sciences* 23:9156. **August 2022.** DOI: [10.3390/ijms23169156](https://doi.org/10.3390/ijms23169156). (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5)
8. Mueller EA et al. “Plasticity of *Escherichia coli* cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions.” *eLife* 8:e40754. **April 2019.** DOI: [10.7554/eLife.40754](https://doi.org/10.7554/eLife.40754). (mueller2019plasticityofescherichia pages 1-2)
9. Ito M, Morino M, Krulwich TA. “Mrp Antiporters Have Important Roles in Diverse Bacteria and Archaea.” *Frontiers in Microbiology* 8:2325. **November 2017.** DOI: [10.3389/fmicb.2017.02325](https://doi.org/10.3389/fmicb.2017.02325). (ito2017mrpantiportershave pages 1-2)
10. Cheng B et al. “Alkaline Response of a Halotolerant Alkaliphilic *Halomonas* Strain and Functional Diversity of Its Na+(K+)/H+ Antiporters.” *Journal of Biological Chemistry* 291:26056–26065. **December 2016.** DOI: [10.1074/jbc.M116.751016](https://doi.org/10.1074/jbc.M116.751016). (cheng(程彬)2016alkalineresponseof pages 8-9, cheng(程彬)2016alkalineresponseof pages 5-6, cheng(程彬)2016alkalineresponseof pages 1-2)

References

1. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

4. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

5. (ramoneda2023buildingagenomebased pages 5-6): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

6. (ng2023singlestrainbehaviorpredicts pages 10-11): Katharine M. Ng, Sagar Pannu, Sijie Liu, Juan C. Burckhardt, Thad Hughes, Will Van Treuren, Jen Nguyen, Kisa Naqvi, Bachviet Nguyen, Charlotte A. Clayton, Deanna M. Pepin, Samuel R. Collins, and Carolina Tropini. Single-strain behavior predicts responses to environmental ph and osmolality in the gut microbiota. Jul 2023. URL: https://doi.org/10.1128/mbio.00753-23, doi:10.1128/mbio.00753-23. This article has 42 citations and is from a domain leading peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (li2024responseofescherichia pages 4-5): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

9. (krulwich2011molecularaspectsof pages 14-15): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

10. (dubinkina2024atranscriptomicatlas pages 1-2): Veronika Dubinkina, Shounak Bhogale, Ping-Hung Hsieh, Payam Dibaeinia, Ananthan Nambiar, Sergei Maslov, Yasuo Yoshikuni, and Saurabh Sinha. A transcriptomic atlas of acute stress response to low ph in multiple <i>issatchenkia orientalis</i> strains. Jan 2024. URL: https://doi.org/10.1128/spectrum.02536-23, doi:10.1128/spectrum.02536-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

11. (krulwich2011molecularaspectsof pages 6-8): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

12. (cheng(程彬)2016alkalineresponseof pages 8-9): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

13. (cheng(程彬)2016alkalineresponseof pages 5-6): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

14. (ito2017mrpantiportershave pages 1-2): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 145 citations and is from a peer-reviewed journal.

15. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

16. (mueller2019plasticityofescherichia pages 1-2): Elizabeth A Mueller, Alexander JF Egan, Eefjan Breukink, Waldemar Vollmer, and Petra Anne Levin. Plasticity of escherichia coli cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions. eLife, Apr 2019. URL: https://doi.org/10.7554/elife.40754, doi:10.7554/elife.40754. This article has 126 citations and is from a domain leading peer-reviewed journal.

17. (li2024responseofescherichia pages 5-7): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

18. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

19. (jiang2024exogenousputrescineplays pages 9-12): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

20. (jiang2024exogenousputrescineplays pages 4-6): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

21. (cheng(程彬)2016alkalineresponseof pages 2-4): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

22. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

23. (ramoneda2023buildingagenomebased pages 1-1): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

24. (ng2023singlestrainbehaviorpredicts pages 1-2): Katharine M. Ng, Sagar Pannu, Sijie Liu, Juan C. Burckhardt, Thad Hughes, Will Van Treuren, Jen Nguyen, Kisa Naqvi, Bachviet Nguyen, Charlotte A. Clayton, Deanna M. Pepin, Samuel R. Collins, and Carolina Tropini. Single-strain behavior predicts responses to environmental ph and osmolality in the gut microbiota. Jul 2023. URL: https://doi.org/10.1128/mbio.00753-23, doi:10.1128/mbio.00753-23. This article has 42 citations and is from a domain leading peer-reviewed journal.

25. (ng2023singlestrainbehaviorpredicts pages 6-6): Katharine M. Ng, Sagar Pannu, Sijie Liu, Juan C. Burckhardt, Thad Hughes, Will Van Treuren, Jen Nguyen, Kisa Naqvi, Bachviet Nguyen, Charlotte A. Clayton, Deanna M. Pepin, Samuel R. Collins, and Carolina Tropini. Single-strain behavior predicts responses to environmental ph and osmolality in the gut microbiota. Jul 2023. URL: https://doi.org/10.1128/mbio.00753-23, doi:10.1128/mbio.00753-23. This article has 42 citations and is from a domain leading peer-reviewed journal.

26. (dubinkina2024atranscriptomicatlas pages 18-20): Veronika Dubinkina, Shounak Bhogale, Ping-Hung Hsieh, Payam Dibaeinia, Ananthan Nambiar, Sergei Maslov, Yasuo Yoshikuni, and Saurabh Sinha. A transcriptomic atlas of acute stress response to low ph in multiple <i>issatchenkia orientalis</i> strains. Jan 2024. URL: https://doi.org/10.1128/spectrum.02536-23, doi:10.1128/spectrum.02536-23. This article has 12 citations and is from a domain leading peer-reviewed journal.

27. (patinoruiz2022prokaryoticna+h+exchangers—transport pages 4-5): Miyer Patiño-Ruiz, Constanța Ganea, and Octavian Călinescu. Prokaryotic na+/h+ exchangers—transport mechanism and essential residues. International Journal of Molecular Sciences, 23:9156, Aug 2022. URL: https://doi.org/10.3390/ijms23169156, doi:10.3390/ijms23169156. This article has 28 citations.

28. (ramoneda2023buildingagenomebased pages 13-13): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

29. (cheng(程彬)2016alkalineresponseof pages 1-2): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.