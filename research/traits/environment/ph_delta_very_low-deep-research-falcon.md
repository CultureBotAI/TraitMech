---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:29:14.008658'
end_time: '2026-08-04T02:38:00.840507'
duration_seconds: 526.83
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta very low
  trait_identifier: METPO:1000473
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH delta phenotype with a very narrow growth-supporting pH breadth
    of at most approximately 1 pH unit, characteristic of stenotopic pH-sensitive
    physiology.
  parent_traits: METPO:1000232
  synonyms: pHd_<=1
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports very narrow pH-tolerance breadths as the stenotopic / pH-sensitive phenotype.)'
  causal_graph_summary: 'ph_delta_very_low_stenotopic: 13 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000473
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a very narrow growth-supporting pH breadth of at most approximately 1 pH unit, characteristic of stenotopic pH-sensitive physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_<=1
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very narrow pH-tolerance breadths as the stenotopic / pH-sensitive phenotype.)
- **Existing causal graph summary:** ph_delta_very_low_stenotopic: 13 nodes, 7 edges

## Research Objective

Research the microbial trait **pH delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_very_low.yaml`.

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
- **Trait label:** pH delta very low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000473
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a very narrow growth-supporting pH breadth of at most approximately 1 pH unit, characteristic of stenotopic pH-sensitive physiology.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_<=1
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports very narrow pH-tolerance breadths as the stenotopic / pH-sensitive phenotype.)
- **Existing causal graph summary:** ph_delta_very_low_stenotopic: 13 nodes, 7 edges

## Research Objective

Research the microbial trait **pH delta very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_very_low.yaml`.

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


# Curation report: microbial trait “pH delta very low”

## Executive curation judgment

**Trait:** “pH delta very low”  
**Identifier:** **`METPO:1000473`**  
**Parent:** `METPO:1000232`  
**Operational meaning:** an organism-level, growth-assay phenotype in which the reproducible interval from minimum to maximum growth-supporting extracellular pH is **≤ approximately 1 pH unit**, under otherwise fixed conditions.

The literature strongly supports a mechanistic network connecting extracellular pH, proton permeability, proton motive force (PMF), intracellular-pH homeostasis, ion transport, cell-envelope synthesis, proton-consuming metabolism, and pH-dependent growth. However, **none of the retrieved perturbation studies directly demonstrates that a named mechanism causes the terminal phenotype of a ≤1-unit growth breadth**. Most evidence concerns broad-range organisms, failure at one end of a pH series, acute survival, or maintenance of intracellular pH. Accordingly, the graph should presently curate mechanistic intermediate edges while leaving any direct edge to `METPO:1000473` marked **inferred/uncertain**.

## 1. Trait scope and boundary conditions

### 1.1 What the trait represents

The recommended assay-level definition is:

> **pH delta = maximum tested extracellular pH supporting reproducible net growth − minimum tested extracellular pH supporting reproducible net growth.**

“Very low” means a breadth of no more than approximately one pH unit. Growth should be defined prospectively—for example, a positive specific growth rate, a specified increase in biomass or cell number, or serially transferable colony formation—and the pH must remain measured or controlled during incubation.

This is a **breadth trait**, not a location trait. An organism growing only from pH 1.5–2.5 and one growing only from pH 7.0–8.0 could both satisfy it despite having different optima and ecological classifications.

### 1.2 Distinctions from nearby traits

* **pH optimum:** the pH giving maximal growth rate or yield; it does not specify breadth.
* **Acidophily/alkaliphily:** location of the optimum or preferred niche, not necessarily narrowness. Classical acidophiles may grow at pH 1–3 and alkaliphiles at pH 10–13, but some have broad ranges. The foundational review distinguishes growth range from maintenance of a different cytoplasmic pH. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 1-3)
* **Acid or alkali resistance:** survival without net growth. The literature explicitly treats survival as the ability to resume growth after return to permissive conditions; gastric survival by *E. coli* or *Salmonella* therefore is not evidence of growth at stomach pH. (krulwich2011molecularaspectsof pages 1-3)
* **Intracellular pH or ΔpH:** a mechanistic state variable, not the extracellular growth interval. Neutralophiles commonly grow over roughly pH 5.5–9 while maintaining pHi around 7.2–7.8; these values must not be interpreted as a narrow pH-delta phenotype. (rebelo2023unravelingtherole pages 18-20, krulwich2011molecularaspectsof pages 1-3)
* **Acute pH-shift response:** transcriptomic or survival responses over minutes do not establish sustained growth. For example, the 2023 *E. coli* study shifted cultures from pH 7.6 to 5.8 or 4.4 for 30 minutes; it identified 702 and 1,030 altered transcripts, respectively, but did not map minimum-to-maximum growth pH. (schumacher2023ribosomeprofilingreveals pages 2-5)
* **Community association or biofilm formation:** environmental occurrence, relative abundance, or biofilm biomass is not equivalent to an isolate’s planktonic growth range.

### 1.3 Essential assay metadata

A defensible annotation should record strain, medium and nutrients, buffer chemistry and concentration, temperature, oxygen/electron acceptor, salinity and major ions, inoculum physiological state, pH spacing, incubation duration, growth threshold, biological replication, and beginning/end pH. Organic acids require special treatment because identical nominal pH values can impose different membrane-permeant weak-acid loads. Protonated weak acids cross membranes and dissociate in the more neutral cytoplasm, causing proton and anion stress. (lund2020understandinghowmicroorganisms pages 1-2, lund2020understandinghowmicroorganisms pages 2-3)

## 2. Current mechanistic understanding

A conservative causal model is:

**external pH and acid/base chemistry → proton influx/efflux and PMF → cytoplasmic pH → macromolecular and metabolic function → pH-dependent growth → observed growth-range breadth.**

PMF comprises ΔpH and electrical potential, Δψ. Primary proton pumps, ATPases, and secondary Na⁺/H⁺ or K⁺/H⁺ antiporters redistribute protons and other ions. Acid conditions additionally recruit proton-consuming decarboxylation, ammonia-generating reactions, membrane remodeling, and weak-organic-acid export. At alkaline pH, electrogenic cation/proton antiporters import protons. (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 5-6, lund2020understandinghowmicroorganisms pages 1-2)

An important expert interpretation is that these mechanisms usually **broaden** the supported pH interval. A very narrow interval could arise from missing, weak, energetically costly, or poorly regulated homeostasis at either boundary; from pH-specialized cell-envelope enzymes; from membrane leakage; or from a pH-sensitive essential metabolic reaction. That terminal inference is biologically plausible but is not yet directly demonstrated for `METPO:1000473`.

## 3. Candidate nodes grouped by type

Only identifiers that can be assigned confidently are given. Label-only nodes are preferable to guessed identifiers.

### Trait and environmental nodes

* `METPO:1000473` — pH delta very low.
* `METPO:1000232` — supplied parent trait.
* Extracellular pH — label-only environmental/experimental variable.
* Growth-supporting pH interval; minimum growth pH; maximum growth pH; pH optimum — label-only assay nodes.
* Buffer capacity; medium composition; incubation temperature; oxygen availability; salinity; Na⁺ and K⁺ availability — experimental-context nodes.

### Chemicals and physicochemical entities

* Proton — **CHEBI:15378**.
* Sodium cation — **CHEBI:29101**.
* Potassium cation — **CHEBI:29103**.
* L-glutamate — **CHEBI:29985**.
* 4-aminobutanoate/GABA — **CHEBI:16865**.
* Putrescine — **CHEBI:17148**.
* Acetate — **CHEBI:30089**.
* Acetoin — **CHEBI:15688**.
* Formic acid — **CHEBI:30751**.
* Formate — **CHEBI:15740**.
* Proton motive force, transmembrane pH gradient, membrane potential, cytoplasmic pH, and passive proton permeability — label-only process/state nodes unless the project’s ontology profile provides approved identifiers.

### Transporters and complexes

* F-type H⁺-transporting ATPase / ATP synthase — **GO:0015986** is a suitable biological-process grounding for ATP synthesis coupled proton transport; retain complex-specific gene nodes where known.
* A/V-type ATPase — label or GO-grounded after checking taxon-specific directionality; ATP synthesis versus ATP-driven proton pumping must not be conflated.
* Na⁺/H⁺ antiporter activity — **GO:0015385**.
* K⁺/H⁺ antiporter activity — candidate label; verify the exact GO term before curation.
* Mrp1 and Mrp2 multisubunit antiporters; Mrp1A Lys299 — taxon-specific label nodes.
* NhaA, NhaP, ChaA — gene/protein-family nodes; use strain-specific UniProt identifiers only after organism-level sequence confirmation.
* KtrAB/KtrAD and regulator KtrA; Kup and KimA; KdpFABC — potassium-transport nodes.

### Enzymes, pathways, and regulatory modules

* Glutamate-, arginine-, lysine-, and ornithine-dependent acid-resistance systems; glutamate decarboxylase GadB; arginine decarboxylase AdiA; amino-acid/amine antiporters. GadB consumes a cytoplasmic proton while producing GABA, supporting extreme-acid survival in *E. coli*. (rebelo2023unravelingtherole pages 18-20, krulwich2011molecularaspectsof pages 5-6)
* PBP1a/*mrcA*, PBP1b/*mrcB*, and lipoprotein activators LpoA/LpoB — pH-specialized peptidoglycan-synthesis machinery.
* Acetate metabolism: AckA and AcsA.
* Acetoin biosynthesis: AlsS and AlsD; acetoin catabolism AcoA.
* Archaeal GDGT/GDNT tetraether-lipid biosynthesis, cyclopentane-ring synthases GrsA/GrsB, glycosylation, and tetraether:diether ratio.
* Intracellular pH homeostasis — **GO:0051453**.
* Peptidoglycan biosynthetic process — **GO:0009252**.
* Biofilm formation — **GO:0042710**, where relevant; this must remain separate from isolate-level growth breadth.

### Cellular locations and structures

* Cytoplasm — **GO:0005737**.
* Plasma membrane — **GO:0005886**.
* Bacterial cell wall/peptidoglycan layer — use project-approved taxon-appropriate GO terms.
* Archaeal tetraether membrane; extracellular biofilm microenvironment; extracellular polymeric substance matrix — label-only candidates.

## 4. Candidate evidence-backed causal edges

The following artifact summarizes the edge set and curation status.

| subject | predicate | object | evidence class | taxon and assay | DOI | curation recommendation |
|---|---|---|---|---|---|---|
| Mrp1 antiporter (mrp1 operon) | maintains | cytoplasmic pH homeostasis under alkaline conditions | direct pH-series perturbation | *Corynebacterium glutamicum*; deletion mutants assayed across alkaline pH and salt conditions; Δmrp1 showed more alkaline pHi and Δmrp1Δmrp2 lost pHi homeostasis at high pH (xu2018thelysine299 pages 8-11) | https://doi.org/10.1128/AEM.00110-18 | Curate as taxon-specific mechanistic edge to pHi homeostasis; do **not** connect directly to METPO:1000473 |
| Mrp1 antiporter (mrp1 operon) | promotes | growth under alkaline pH and NaCl stress | direct pH-series perturbation | *C. glutamicum*; Δmrp1 had growth attenuation above pH 8.0; Δmrp1Δmrp2 nearly lost ability to grow under high alkaline conditions (xu2018thelysine299 pages 8-11) | https://doi.org/10.1128/AEM.00110-18 | Curate as taxon-specific pH-dependent growth edge |
| Mrp2 antiporter (mrp2 operon) | contributes to | K+/H+ balance and growth under KCl/osmotic stress | component mechanism | *C. glutamicum*; deletion had significant defect with 0.6 M KCl, exacerbated by increased pH (xu2018thelysine299 pages 8-11) | https://doi.org/10.1128/AEM.00110-18 | Curate cautiously; role is context-specific and less directly tied to pHi than Mrp1 |
| Mrp1A Lys299 residue | required for | Mrp1-dependent pHi homeostasis and alkaline/NaCl growth | direct pH-series perturbation | *C. glutamicum* point mutant Mrp1A-K299H; elevated pHi at alkaline pH and severe growth defects under high NaCl/alkaline conditions (xu2018thelysine299 pages 13-15) | https://doi.org/10.1128/AEM.00110-18 | Curate as residue-level evidence supporting Mrp1 mechanism; strain-specific |
| PBP1b (mrcB) | required for | growth at acidic pH | direct pH-series perturbation | *Escherichia coli* MG1655; ΔmrcB defects in buffered LB across pH 4.8–8.4; loss of LpoB prevented growth at pH 4.8 (mueller2019plasticityofescherichia pages 3-5, mueller2019plasticityofescherichia pages 5-6) | https://doi.org/10.7554/eLife.40754 | Curate as strong pH-dependent cell-wall growth edge |
| PBP1a (mrcA) | required for | growth at neutral-to-alkaline pH | direct pH-series perturbation | *E. coli* MG1655; ΔmrcA defect across discrete non-overlapping pH range; significant defect between pH 5.9–8.2 and deletion sensitive at neutral/alkaline pH (mueller2019plasticityofescherichia pages 3-5, mueller2019plasticityofescherichia pages 5-6) | https://doi.org/10.7554/eLife.40754 | Curate as strong pH-dependent cell-wall growth edge |
| LpoB cofactor | activates/supports | PBP1b-dependent acidic growth | direct pH-series perturbation | *E. coli*; deletion of *lpoB* prevented growth at pH 4.8, mimicking loss of PBP1b (mueller2019plasticityofescherichia pages 5-6) | https://doi.org/10.7554/eLife.40754 | Curate as cofactor→enzyme→acidic growth edge |
| LpoA cofactor | activates/supports | PBP1a-dependent neutral/alkaline growth | direct pH-series perturbation | *E. coli*; loss of *lpoA* caused significant defect in doublings per hour between pH 5.9–8.2 (mueller2019plasticityofescherichia pages 5-6) | https://doi.org/10.7554/eLife.40754 | Curate as cofactor→enzyme→alkaline growth edge |
| KtrA-dependent Ktr system | promotes | growth at alkaline pH when K+ is limiting | direct pH-series perturbation | *Enterococcus faecalis* JH2-2; ΔktrA mutants in low-K mLBG showed delayed growth at pH 9.0, rescued by 10 mM KCl (acciarri2023redundantpotassiumtransporter pages 6-8, acciarri2023redundantpotassiumtransporter pages 5-6) | https://doi.org/10.3389/fmicb.2023.1117684 | Curate as alkaline/low-K conditional edge; not a general narrow-pH trait determinant |
| Kup transporter | supports | K+ uptake and stress growth with Ktr deficiency | direct pH-series perturbation | *E. faecalis* and heterologous *E. coli* complementation; ΔkupΔktrA showed strongest alkaline low-K defect; Kup restored low-K growth in transporter-deficient *E. coli* (acciarri2023redundantpotassiumtransporter pages 6-8, acciarri2023redundantpotassiumtransporter pages 5-6) | https://doi.org/10.3389/fmicb.2023.1117684 | Curate as K+ uptake edge with alkaline-growth context |
| Formic acid | causes | cytosolic acidification | component mechanism | *Methylacidiphilum* sp. RTK17.1; methane-grown cells, pH series and formic-acid addition; intracellular pH decreased from 6.52 to 6.05 with 1 mM formic acid (carere2021growthonformic pages 4-5, carere2021growthonformic pages 3-4) | https://doi.org/10.3389/fmicb.2021.651744 | Curate as weak-organic-acid stress edge; indirect for METPO:1000473 |
| extracellular acidic pH / proton gradient | constrains | growth unless circumneutral cytosolic pH is maintained | component mechanism | *Methylacidiphilum* sp. RTK17.1 batch cultures from pH 0.5–6.0; optimal growth where external pH 1.5–4.0 maintained internal pH 6.55 ± 0.05 (carere2021growthonformic pages 4-5, carere2021growthonformic pages 3-4) | https://doi.org/10.3389/fmicb.2021.651744 | Curate as foundational pHi-homeostasis edge; note this is a broad-range acidophile, not METPO:1000473 |
| acetate production pathway (AckA/AcsA-associated overflow metabolism) | acidifies | biofilm extracellular environment | component mechanism | *Bacillus subtilis* NCIB 3610 biofilms in minimally buffered MSgg; ΔackAΔacsA reduced acidification rate by ~48% versus WT (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5) | https://doi.org/10.1128/mbio.03387-23 | Curate as extracellular-pH modification edge; biofilm-specific |
| AlsS/AlsD acetoin biosynthesis | alkalinizes | biofilm extracellular environment | direct pH-series perturbation | *B. subtilis* biofilms; ΔalsS and ΔalsD retained acidification but completely lost alkalinization; initial pH 6–9 experiments showed pH conditioning toward neutrophile range (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5) | https://doi.org/10.1128/mbio.03387-23 | Curate as strong biofilm pH-regulation edge |
| AlsS-mediated acetoin biosynthesis | promotes | biofilm fitness in minimally buffered conditions | component mechanism | *B. subtilis*; ΔalsS biofilms failed to maintain local pH in preferred neutrophile range and had significantly lower cell count / altered morphology in minimally buffered medium (tran2024activephregulation pages 5-7) | https://doi.org/10.1128/mbio.03387-23 | Curate as phenotype edge for biofilm development, not planktonic growth breadth |
| archaeal GDGT/tetraether membrane features (cyclopentane rings, GDNT:GDGT ratio, sugar moieties) | decreases | passive proton permeability | component mechanism | thermoacidophilic archaea; review synthesis with comparative lipid, simulation, and prior physiology evidence; explicit uncertainty about direct causal proof (chong2024archaeamembranesin pages 4-6, chong2024archaeamembranesin pages 3-4) | https://doi.org/10.3389/frbis.2023.1338019 | Curate only as uncertain/general edge unless a taxon-specific perturbation paper is added |
| exogenous putrescine | increases | acid-condition biofilm formation and intracellular alkalinizing/GABA-linked responses | community-level | biofilm-based activated sludge communities; acidic pH 3–4 increased biofilm biomass by 102%, intact cells by 125%, ATP up, GABA/glutamate pathway genes up (jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6) | https://doi.org/10.1128/AEM.00569-24 | Curate only if community-level nodes are allowed; otherwise keep as background |
| exogenous putrescine | decreases | alkaline-condition biofilm formation | community-level | activated-sludge biofilms; alkaline pH 8–9 decreased biofilm biomass by 37% and intact cells by 36% with downregulation of proton-transport/ATP-synthesis functions (jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6) | https://doi.org/10.1128/AEM.00569-24 | Community-specific and non-curatable for organism-level TraitMech unless explicitly modeled |
| None of the retrieved mechanisms | directly establishes | growth-supporting pH breadth <= approximately 1 pH unit | curation conclusion | Across retrieved studies, mechanisms affect pHi, proton permeability, extracellular pH regulation, or growth at tested pH values, but no perturbation study directly demonstrates causation of the METPO:1000473 terminal phenotype (carere2021growthonformic pages 4-5, mueller2019plasticityofescherichia pages 3-5, mueller2019plasticityofescherichia pages 5-6, acciarri2023redundantpotassiumtransporter pages 6-8, tran2024activephregulation pages 5-7, chong2024archaeamembranesin pages 4-6, xu2018thelysine299 pages 8-11) | n/a | Add as warning in curation notes; avoid direct mechanism→METPO:1000473 edge without dedicated narrow-range evidence |


*Table: This table summarizes the strongest source-backed candidate causal edges relevant to the pH delta very low trait. It distinguishes direct pH-series perturbation evidence from component and community-level mechanisms, and flags that none directly prove a growth breadth of ≤1 pH unit.*

### Additional foundational edges and supporting snippets

| Subject–predicate–object | Supporting snippet | Interpretation and status |
|---|---|---|
| Low external pH → activates → GadB/proton-consuming decarboxylation | “Glutamate decarboxylase (GadB) is specifically activated during acid stress, consuming cytoplasmic protons during conversion to GABA.” | Strong general mechanism; evidence is principally acid survival, not ≤1-unit growth breadth. (krulwich2011molecularaspectsof pages 5-6) |
| High external pH → activates → Na⁺/H⁺ and K⁺/H⁺ antiport | Antiporters “use transmembrane potential to drive proton uptake”; *E. coli* NhaA has 2H⁺/1Na⁺ stoichiometry. | Strong component edge; transporter and stoichiometry are taxon-specific. (krulwich2011molecularaspectsof pages 5-6) |
| F₁F₀-ATP synthase integrity → supports → alkaline pH homeostasis | Mutations in ATP-synthase motifs reduced activity and homeostatic capacity, especially at pH 10.5. | Perturbational evidence in alkaliphiles; do not generalize directionality to every organism. (krulwich2011molecularaspectsof pages 12-14) |
| Mrp antiporter activity → supports → alkaline growth | Point mutations in *mrpA* abolished the alkaliphile phenotype; Mrp was described as essential for high-pH homeostasis. | Strong but taxon-specific. (krulwich2011molecularaspectsof pages 12-14) |
| Weak organic acid permeation → causes → cytosolic acidification/PMF stress | In *Methylacidiphilum* RTK17.1, 1 mM formic acid decreased pHi from 6.52 to 6.05; protonated acids enter and dissociate in the cytosol. | Strong chemical-to-state edge. It may narrow an observed interval in organic-acid media but does not establish intrinsic stenotopy. (carere2021growthonformic pages 4-5) |
| Failure to maintain circumneutral pHi → associates with → reduced growth outside the preferred pH range | RTK17.1 grew from pH 1.0–6.0, optimally near 2.5; pHi was 6.55 ± 0.05 at external pH 1.5–3.0, while growth-reducing external conditions produced pHi 5.97 ± 0.13. | Quantitative physiology, but the organism is broad-range and therefore a mechanistic comparator rather than an example of `METPO:1000473`. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 3-4) |
| PBP1b/LpoB activity → enables → acidic growth | “Deletion of lpoB prevented growth at pH 4.8”; catalytically inactive PBP1b variants failed to restore growth. | Among the strongest pH-series causal edges; suitable for curation with *E. coli* context. (mueller2019plasticityofescherichia pages 5-6) |
| PBP1a/LpoA activity → promotes → neutral/alkaline growth | Loss of LpoA caused a significant defect from pH 5.9–8.2; PBP1a and PBP1b defects occupied discrete ranges. | Supports pH-specialized essential-envelope functions and a mechanism by which a range boundary may shift. (mueller2019plasticityofescherichia pages 3-5, mueller2019plasticityofescherichia pages 5-6) |
| Acetate production → acidifies → biofilm microenvironment | Δ*ackA*Δ*acsA* reduced the acidification rate by approximately 48%. | Direct environmental-modification edge, but biofilm- and medium-specific. (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5) |
| AlsS/AlsD acetoin biosynthesis → alkalinizes → biofilm microenvironment | Δ*alsS* and Δ*alsD* “completely lost the alkalinization phase”; complementation restored it. | Strong 2024 perturbation evidence. It modifies local exposure rather than intrinsic cellular breadth. (tran2024activephregulation pages 5-7) |
| Loss of AlsS-mediated pH regulation → decreases → minimally buffered biofilm fitness | Δ*alsS* failed to maintain the neutrophile range and had significantly fewer cells only under minimally buffered conditions. | Current real-world-relevant mechanism for natural, weakly buffered biofilms. (tran2024activephregulation pages 5-7) |
| Archaeal tetraether-membrane packing → reduces → proton permeability | Tight PLFE membranes support a pH 2.5 outside/6.5 inside gradient; simulations found eight-ring GDNT reduced membrane volume by 4.9% and increased interaction energy by 35 kcal/mol. | Mechanistically credible, but the 2024 review explicitly says live-cell quantitative proton-permeability and pump-activity measurements are largely missing. Treat as uncertain. (chong2024archaeamembranesin pages 3-4, chong2024archaeamembranesin pages 4-6) |

## 5. Recent developments, 2023–2024

### 5.1 Systems-level acid-response resolution

Ribosome profiling and RNA-seq of *E. coli* in 2023 distinguished mild pH 5.8 from severe, near-lethal pH 4.4 stress. Of 3,654 analyzed genes, 702 transcripts changed significantly at pH 5.8 and 1,030 at pH 4.4; 18 candidate acid-induced small ORFs were reported. This establishes graded and partly distinct responses rather than a single generic acid program. It remains acute-shift evidence, not growth-range causality. (schumacher2023ribosomeprofilingreveals pages 2-5)

### 5.2 Potassium transport as a conditional pH determinant

A 2023 *Enterococcus faecalis* study showed that KtrA-deficient strains had delayed growth at pH 9 in low-K⁺ medium, with the Δ*kup*Δ*ktrA* mutant most affected; 10 mM KCl restored wild-type growth. At pH 5, these mutants did not differ from the parent under the same low-K⁺ condition. Thus, pH-range boundaries can depend jointly on ion availability and transporter redundancy. (acciarri2023redundantpotassiumtransporter pages 6-8)

### 5.3 Active extracellular-pH regulation by biofilms

In 2024, *Bacillus subtilis* biofilms in minimally buffered medium acidified to approximately pH 5.5 at 0.06 ± 0.0008 pH units/hour and then alkalinized to pH 6.9 at 0.03 ± 0.0005 pH units/hour. The alkalinization lasted 31.2 ± 0.5 hours. Initial-pH experiments from pH 6–9 showed regulation toward the preferred neutrophile interval; Δ*alsS* abolished effective regulation, while overexpression accelerated return. This reveals that laboratory buffering can conceal an organism-driven environmental feedback. (tran2024activephregulation pages 2-5, tran2024activephregulation pages 5-7)

### 5.4 Archaeal membrane adaptation is more complex than ring-count models

Recent work cautions against equating increased GDGT cyclization with acid adaptation. In *Saccharolobus islandicus*, mean cyclization decreased from 3.7 at growth pH 3.4 to 1.6 at pH 2.4 despite *grsB* and ATPase expression responses. The current expert view is that cyclization, glycosylation, GDNT:GDGT ratio, tetraether:diether ratio, and proton-pump expression must be considered jointly; transcript abundance alone cannot predict membrane phenotype. (chong2024archaeamembranesin pages 4-6, chiu2023membranelipidand pages 9-10)

### 5.5 Community engineering with putrescine

In a 2024 activated-sludge biofilm study, putrescine increased acidic-condition biofilm production by 102% and intact-cell proportion by 125%, but decreased alkaline-condition biofilm production by 37% and intact cells by 36%. Acidic conditions increased ATP and ADP by 58% and 26%, respectively, and upregulated glutamate–GABA and proton-transport functions. This is a potential engineering lever for biofilm stability, but it is a mixed-community result and must not be assigned to an isolate-level trait graph. (jiang2024exogenousputrescineplays pages 4-6, jiang2024exogenousputrescineplays pages 9-12)

## 6. Applications and real-world relevance

* **Food preservation and pathogen control:** weak organic acids impose both extracellular acidity and membrane-permeant acid stress. GDAR, ADAR, and LDAR systems contribute to survival of foodborne *E. coli* and *Salmonella* in acidic processing environments and the gastrointestinal tract. Mechanistic knowledge can guide preservative combinations designed to overwhelm proton consumption and anion export. (rebelo2023unravelingtherole pages 18-20)
* **Industrial organic-acid production:** acid-tolerant production hosts require controlled proton pumping, membrane permeability, and anion export. The distinction between nominal pH and weak-acid load is critical for strain screening. (lund2020understandinghowmicroorganisms pages 1-2, lund2020understandinghowmicroorganisms pages 2-3)
* **Wastewater and engineered biofilms:** putrescine and extracellular metabolic pH regulation may alter biofilm formation, stability, and community composition across acidic versus alkaline operation. (jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6)
* **Biofilm control:** disrupting acetoin-mediated alkalinization could selectively impair biofilms in minimally buffered environments; in *B. subtilis*, Δ*alsS* reduced cell counts and altered morphology only when external buffering was weak. (tran2024activephregulation pages 5-7)
* **Acid-mine and geothermal ecology:** pH structures community composition and biogeochemical activity. A 2023 acid-mine-lake study found comammox *Nitrospira* and ammonia-oxidizing archaea represented 52% and 41% of total *amoA* genes, respectively, but genomic presence of an acidophile-affiliated ATPase or antiporters remains associative rather than proof of a narrow growth range. (li2023comammoxnitrospiraand pages 9-11)
* **Synthetic cells and extremophile biotechnology:** archaeal tetraether membranes are being considered as models for low-permeability membranes under harsh conditions, although direct quantitative validation remains incomplete. (chong2024archaeamembranesin pages 4-6)

## 7. Recommended TraitMech graph architecture

A defensible first revision of `ph_delta_very_low_stenotopic` should use layered intermediate nodes rather than connect every homeostasis protein directly to the trait:

1. **Exposure layer:** extracellular pH, buffer capacity, weak organic acid, Na⁺, K⁺, temperature, respiratory condition.
2. **Boundary layer:** proton permeability, tetraether or bacterial membrane composition, porins, peptidoglycan synthesis, PBP1a/PBP1b.
3. **Transport/energy layer:** PMF, Δψ, ΔpH, F/A/V ATPase, Nha/Mrp antiporters, Ktr/Kup/Kdp systems.
4. **Chemical buffering layer:** Gad/Adi/Cad systems, GABA, ammonia-generating reactions, polyamines.
5. **Environmental-feedback layer:** acetate production, acetoin biosynthesis, extracellular acidification/alkalinization, biofilm microenvironment.
6. **State layer:** intracellular pH homeostasis, ATP availability, macromolecular function, cell-envelope integrity.
7. **Assay layer:** specific growth rate at each pH, lower and upper growth boundaries, calculated pH delta.
8. **Terminal trait:** `METPO:1000473` only after the measured delta is ≤ approximately 1.

The terminal relation should initially be represented as **“measured growth pH breadth qualifies as `METPO:1000473`”**, not “gene X causes `METPO:1000473`.”

## 8. Claims that should not yet be curated

1. **Do not curate any retrieved gene or pathway as a universal cause of `METPO:1000473`.** No study directly compares a ≤1-unit strain with a broader isogenic counterpart across a sufficiently dense pH series.
2. **Do not infer pH delta from optimum alone.** “Optimum pH 3” supplies no minimum or maximum.
3. **Do not merge survival with growth.** Decarboxylase-mediated survival at pH 2–2.5 does not prove growth there. (krulwich2011molecularaspectsof pages 5-6)
4. **Do not infer isolate physiology from environmental abundance or MAG gene content.** The acid-mine-lake Nitrospira findings are ecological/genomic associations. (li2023comammoxnitrospiraand pages 9-11)
5. **Do not treat transcript induction as causal sufficiency.** *grsB*, ATPase, or acid-response induction may be compensatory; the archaeal lipid literature contains directionally inconsistent results. (chiu2023membranelipidand pages 9-10, chong2024archaeamembranesin pages 4-6)
6. **Do not generalize community-level putrescine effects to a taxon.** Changes in species composition can produce the apparent response. (jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6)
7. **Do not ignore assay chemistry.** Weak organic acids, K⁺ limitation, NaCl, oxygen, temperature, and buffering can move apparent boundaries independently or interactively.
8. **Do not assume narrower growth after a mutation unless both boundaries are measured.** A defect at pH 9 establishes reduced alkaline fitness; it does not by itself establish a final interval ≤1.

## 9. Priority experiments needed to support the terminal causal edge

The most informative design would use a verified narrow-range isolate and an isogenic perturbation of a candidate mechanism. Measure growth at ≤0.25-pH-unit spacing across and beyond both boundaries in strongly controlled medium, with continuous pH logging, pHi and membrane-potential reporters, and complementation. A mechanism should be considered causal for `METPO:1000473` only if perturbation or rescue reproducibly changes the calculated breadth across the threshold while controlling for growth-rate and medium effects. Comparative genomics alone should be used only to nominate candidates.

## DOI-first bibliography

1. Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology*. Published May 2011. https://doi.org/10.1038/nrmicro2549. (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3)
2. Xu N, et al. **The Lysine 299 residue endows the multisubunit Mrp1 antiporter with dominant roles in Na⁺ resistance and pH homeostasis in Corynebacterium glutamicum.** *Applied and Environmental Microbiology*. Published May 2018. https://doi.org/10.1128/AEM.00110-18. (xu2018thelysine299 pages 13-15, xu2018thelysine299 pages 8-11)
3. Mueller EA, et al. **Plasticity of Escherichia coli cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions.** *eLife*. Published April 2019. https://doi.org/10.7554/eLife.40754. (mueller2019plasticityofescherichia pages 3-5, mueller2019plasticityofescherichia pages 5-6)
4. Lund PA, et al. **Understanding how microorganisms respond to acid pH is central to their control and successful exploitation.** *Frontiers in Microbiology*. Published September 2020. https://doi.org/10.3389/fmicb.2020.556140. (lund2020understandinghowmicroorganisms pages 3-5, lund2020understandinghowmicroorganisms pages 1-2, lund2020understandinghowmicroorganisms pages 2-3)
5. Carere CR, et al. **Growth on formic acid is dependent on intracellular pH homeostasis for the thermoacidophilic methanotroph Methylacidiphilum sp. RTK17.1.** *Frontiers in Microbiology*. Published March 2021. https://doi.org/10.3389/fmicb.2021.651744. (carere2021growthonformic pages 4-5, carere2021growthonformic pages 3-4)
6. Acciarri G, et al. **Redundant potassium transporter systems guarantee the survival of Enterococcus faecalis under stress conditions.** *Frontiers in Microbiology*. Published February 2023. https://doi.org/10.3389/fmicb.2023.1117684. (acciarri2023redundantpotassiumtransporter pages 6-8, acciarri2023redundantpotassiumtransporter pages 5-6)
7. Li D, et al. **Comammox Nitrospira and ammonia-oxidizing archaea are dominant ammonia oxidizers in sediments of an acid mine lake containing high ammonium concentrations.** *Applied and Environmental Microbiology*. Published March 2023. https://doi.org/10.1128/AEM.00047-23. (li2023comammoxnitrospiraand pages 9-11)
8. Chiu BK, et al. **Membrane lipid and expression responses of Saccharolobus islandicus REY15A to acid and cold stress.** *Frontiers in Microbiology*. Published August 2023. https://doi.org/10.3389/fmicb.2023.1219779. (chiu2023membranelipidand pages 9-10, chiu2023membranelipidand pages 3-5)
9. Rebelo A, et al. **Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain.** *Antibiotics*. Published September 2023. https://doi.org/10.3390/antibiotics12091474. (rebelo2023unravelingtherole pages 18-20)
10. Schumacher K, et al. **Ribosome profiling reveals the fine-tuned response of Escherichia coli to mild and severe acid stress.** *mSystems*. Published December 2023. https://doi.org/10.1128/msystems.01037-23. (schumacher2023ribosomeprofilingreveals pages 2-5)
11. Chong PL-G. **Archaea membranes in response to extreme acidic environments.** *Frontiers in Biophysics*. Published January 2024. https://doi.org/10.3389/frbis.2023.1338019. (chong2024archaeamembranesin pages 4-6, chong2024archaeamembranesin pages 3-4)
12. Tran P, Lander SM, Prindle A. **Active pH regulation facilitates Bacillus subtilis biofilm development in a minimally buffered environment.** *mBio*. Published March 2024. https://doi.org/10.1128/mbio.03387-23. (tran2024activephregulation pages 5-7, tran2024activephregulation pages 2-5)
13. Jiang G, et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology*. Published July 2024. https://doi.org/10.1128/AEM.00569-24. (jiang2024exogenousputrescineplays pages 9-12, jiang2024exogenousputrescineplays pages 4-6)

**Bottom line:** the strongest immediately curatable mechanisms are Mrp-dependent alkaline pHi homeostasis, pH-specialized PBP/Lpo cell-wall synthesis, conditional Ktr/Kup-supported alkaline growth, weak-acid-driven cytosolic acidification, and acetate/acetoin-mediated biofilm pH modification. Their connection to the exact ≤1-unit trait must remain indirect until a study measures and causally shifts both growth-range boundaries.

References

1. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

3. (rebelo2023unravelingtherole pages 18-20): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 35 citations.

4. (schumacher2023ribosomeprofilingreveals pages 2-5): Kilian Schumacher, Rick Gelhausen, Willow Kion-Crosby, Lars Barquist, Rolf Backofen, and Kirsten Jung. Ribosome profiling reveals the fine-tuned response of <i>escherichia coli</i> to mild and severe acid stress. Dec 2023. URL: https://doi.org/10.1128/msystems.01037-23, doi:10.1128/msystems.01037-23. This article has 24 citations and is from a peer-reviewed journal.

5. (lund2020understandinghowmicroorganisms pages 1-2): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 366 citations and is from a peer-reviewed journal.

6. (lund2020understandinghowmicroorganisms pages 2-3): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 366 citations and is from a peer-reviewed journal.

7. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

8. (xu2018thelysine299 pages 8-11): Ning Xu, Yingying Zheng, Xiaochen Wang, Terry A. Krulwich, Yanhe Ma, and Jun Liu. The lysine 299 residue endows the multisubunit mrp1 antiporter with dominant roles in na <sup>+</sup> resistance and ph homeostasis in corynebacterium glutamicum. Applied and Environmental Microbiology, May 2018. URL: https://doi.org/10.1128/aem.00110-18, doi:10.1128/aem.00110-18. This article has 24 citations and is from a peer-reviewed journal.

9. (xu2018thelysine299 pages 13-15): Ning Xu, Yingying Zheng, Xiaochen Wang, Terry A. Krulwich, Yanhe Ma, and Jun Liu. The lysine 299 residue endows the multisubunit mrp1 antiporter with dominant roles in na <sup>+</sup> resistance and ph homeostasis in corynebacterium glutamicum. Applied and Environmental Microbiology, May 2018. URL: https://doi.org/10.1128/aem.00110-18, doi:10.1128/aem.00110-18. This article has 24 citations and is from a peer-reviewed journal.

10. (mueller2019plasticityofescherichia pages 3-5): Elizabeth A Mueller, Alexander JF Egan, Eefjan Breukink, Waldemar Vollmer, and Petra Anne Levin. Plasticity of escherichia coli cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions. eLife, Apr 2019. URL: https://doi.org/10.7554/elife.40754, doi:10.7554/elife.40754. This article has 126 citations and is from a domain leading peer-reviewed journal.

11. (mueller2019plasticityofescherichia pages 5-6): Elizabeth A Mueller, Alexander JF Egan, Eefjan Breukink, Waldemar Vollmer, and Petra Anne Levin. Plasticity of escherichia coli cell wall metabolism promotes fitness and antibiotic resistance across environmental conditions. eLife, Apr 2019. URL: https://doi.org/10.7554/elife.40754, doi:10.7554/elife.40754. This article has 126 citations and is from a domain leading peer-reviewed journal.

12. (acciarri2023redundantpotassiumtransporter pages 6-8): Giuliana Acciarri, Fernán O. Gizzi, Mariano A. Torres Manno, Jörg Stülke, Martín Espariz, Víctor S. Blancato, and Christian Magni. Redundant potassium transporter systems guarantee the survival of enterococcus faecalis under stress conditions. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1117684, doi:10.3389/fmicb.2023.1117684. This article has 23 citations and is from a peer-reviewed journal.

13. (acciarri2023redundantpotassiumtransporter pages 5-6): Giuliana Acciarri, Fernán O. Gizzi, Mariano A. Torres Manno, Jörg Stülke, Martín Espariz, Víctor S. Blancato, and Christian Magni. Redundant potassium transporter systems guarantee the survival of enterococcus faecalis under stress conditions. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1117684, doi:10.3389/fmicb.2023.1117684. This article has 23 citations and is from a peer-reviewed journal.

14. (carere2021growthonformic pages 4-5): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

15. (carere2021growthonformic pages 3-4): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 21 citations and is from a peer-reviewed journal.

16. (tran2024activephregulation pages 5-7): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

17. (tran2024activephregulation pages 2-5): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 33 citations and is from a domain leading peer-reviewed journal.

18. (chong2024archaeamembranesin pages 4-6): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

19. (chong2024archaeamembranesin pages 3-4): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

20. (jiang2024exogenousputrescineplays pages 9-12): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

21. (jiang2024exogenousputrescineplays pages 4-6): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

22. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

23. (chiu2023membranelipidand pages 9-10): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

24. (li2023comammoxnitrospiraand pages 9-11): Deyong Li, Zhichang Ren, Yangqi Zhou, Lugao Jiang, Min Zheng, and Guoqiang Liu. Comammox <i>nitrospira</i> and ammonia-oxidizing archaea are dominant ammonia oxidizers in sediments of an acid mine lake containing high ammonium concentrations. Applied and Environmental Microbiology, Mar 2023. URL: https://doi.org/10.1128/aem.00047-23, doi:10.1128/aem.00047-23. This article has 34 citations and is from a peer-reviewed journal.

25. (lund2020understandinghowmicroorganisms pages 3-5): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 366 citations and is from a peer-reviewed journal.

26. (chiu2023membranelipidand pages 3-5): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.