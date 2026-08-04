---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:10:38.594029'
end_time: '2026-08-04T11:17:50.568286'
duration_seconds: 431.97
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: heterotrophic
  trait_identifier: METPO:1000644
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: heterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains carbon from organic compounds
    rather than from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: TT_heterotroph, aerobic_heterotrophy, heterotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the
    primary sources of carbon (Encyclopedia chapter supports organic compounds as
    heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules
    ... carbon source (Review table supports organic molecules as carbon sources in
    heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example:
    Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model
    bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science,
    complete genome).)'
  causal_graph_summary: 'heterotrophic_organic_carbon_assimilation: 12 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** heterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000644
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_heterotroph, aerobic_heterotrophy, heterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon (Encyclopedia chapter supports organic compounds as heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules ... carbon source (Review table supports organic molecules as carbon sources in heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example: Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science, complete genome).)
- **Existing causal graph summary:** heterotrophic_organic_carbon_assimilation: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **heterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/heterotrophic.yaml`.

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
- **Trait label:** heterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000644
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_heterotroph, aerobic_heterotrophy, heterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon (Encyclopedia chapter supports organic compounds as heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules ... carbon source (Review table supports organic molecules as carbon sources in heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example: Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science, complete genome).)
- **Existing causal graph summary:** heterotrophic_organic_carbon_assimilation: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **heterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/heterotrophic.yaml`.

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


# Curation-focused research report: microbial heterotrophy

## Executive recommendation

The reviewed class should remain **`METPO:1000644`** exactly as supplied. Its defensible scope is: **a microbial trophic phenotype in which organic compounds provide the principal carbon incorporated into cellular material**. The trait does **not** specify the energy source, electron donor, terminal electron acceptor, oxygen requirement, or a single conserved pathway.

For `heterotrophic.yaml`, the safest graph backbone is therefore:

**environmental organic compound → transport/uptake → central carbon catabolism → precursor metabolites → biomass**, with a conditional branch from catabolism through **respiration or fermentation → ATP/redox regeneration/by-products**. Specific transporters, substrates, pathways, and respiratory machinery should be modeled as taxon- or assay-conditioned alternatives, not universal requirements.

## 1. Trait scope and boundaries

### 1.1 Positive definition

The supplied definition—“A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide”—captures the principal-carbon-source distinction. Current literature describes heterotrophs as using organic compounds for energy and biomass production, while also showing that heterotrophic cells can incorporate small amounts of inorganic carbon through ordinary carboxylation reactions. Reported inorganic-carbon contributions are commonly about **1–8% of microbial biomass carbon**, with *Bacillus subtilis* measurements of **3–6%** on several organic substrates. Consequently, “rather than carbon dioxide” should mean **not relying primarily on autotrophic CO₂ fixation**, not zero CO₂ incorporation (braun2021reviewsandsyntheses pages 1-2).

### 1.2 Important distinctions

- **Heterotrophy versus autotrophy:** autotrophs obtain their principal biomass carbon through inorganic-carbon fixation. The presence of anaplerotic CO₂ fixation does not make an organic-carbon-grown organism autotrophic (braun2021reviewsandsyntheses pages 1-2).
- **Heterotrophy versus mixotrophy:** simultaneous meaningful use of organic carbon and autotrophic carbon fixation is mixotrophy. In 2024, *Leptothrix ochracea* MAGs encoded sugar/organic-acid utilization together with RuBisCO and the Calvin–Benson–Bassham cycle; transcriptomic and modeling evidence therefore supports mixotrophy, not strict heterotrophy (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 9-13).
- **Heterotrophy versus organotrophy:** “heterotroph” identifies the **carbon source**; “organotroph” identifies an organic **electron donor**. These frequently coincide as chemoorganoheterotrophy but are not logically identical.
- **Heterotrophy versus aerobic heterotrophy:** oxygen is not part of the defining phenotype. Heterotrophic carbon metabolism can be coupled to aerobic respiration, anaerobic respiration, or fermentation. *Cupriavidus necator*, for example, can use organic substrates aerobically or respire anaerobically with nitrate/nitrite (alagesan201813cassistedmetabolicflux pages 1-2).
- **Dark growth:** growth in darkness on an organic substrate is a strong operational assay for heterotrophy in otherwise photosynthetic microorganisms, but darkness is not required when assaying nonphototrophic bacteria or archaea. *Chlorella sorokiniana* AARL G015 grew and was genetically transformed under complete darkness (jareonsin2023unlockingmicroalgalhost—exploring pages 1-2).
- **Genomic potential versus phenotype:** transporter and catabolic genes establish metabolic potential, not demonstrated growth. The 2024 Group-3.unk Thaumarchaeota assignment rests on MAG reconstruction—ABC transporters, carbohydrate/amino-acid catabolism, glycolysis and a glyoxylate cycle—not an isolate growth experiment (zhang2024metagenomiccharacterizationof pages 8-11, zhang2024metagenomiccharacterizationof pages 1-2).

## 2. Candidate graph nodes

Identifiers below are limited to high-confidence, stable mappings. Label-only nodes are preferable wherever substrate charge state, pathway variant, or taxonomic implementation remains unresolved.

### Trait and environmental nodes

- **heterotrophic** — `METPO:1000644`
- organic compound available as carbon source — label-only umbrella node
- dissolved organic matter — label-only unless a project-approved ENVO term is selected
- darkness / absence of photosynthetically active light — label-only experimental condition
- oxygen availability — environmental factor; do not make it required
- carbon limitation, substrate concentration, temperature, nitrogen and phosphorus availability — modulators

Organic-substrate availability is the main bottom-up control on marine heterotrophic bacteria; temperature directly alters metabolic rates, while nutrient limitation and grazing/viral mortality provide additional controls (kim2023projected21stcenturychanges pages 1-2).

### Chemicals and metabolites

- D-glucose — `CHEBI:17634`
- acetate — `CHEBI:30089`
- L-lactate — `CHEBI:422`
- pyruvate — `CHEBI:15361`
- acetyl-CoA — `CHEBI:15351`
- carbon dioxide — `CHEBI:16526`
- ATP — `CHEBI:15422`
- phosphoenolpyruvate — `CHEBI:18021`
- glucose 6-phosphate — `CHEBI:4170`
- amino acids, peptides, carbohydrates, fatty acids, hydrocarbons, dissolved organic matter — class-level or label-only nodes
- oxygen — `CHEBI:15379`; conditional terminal electron acceptor
- nitrate/nitrite — conditional anaerobic acceptors; ground only after selecting the intended ionic forms

### Processes and pathways

- transmembrane transport — `GO:0055085`
- carbohydrate transport — `GO:0008643`
- glycolytic process — `GO:0006096`
- tricarboxylic acid cycle — `GO:0006099`
- glyoxylate cycle — `GO:0006097`
- cellular respiration — `GO:0045333`
- aerobic respiration — `GO:0009060`
- fermentation — `GO:0006113`
- oxidative phosphorylation — `GO:0006119`
- ATP synthesis coupled proton transport — `GO:0015986`
- Entner–Doudoroff pathway — label-only pending the project’s approved pathway database mapping
- pentose-phosphate pathway — label-only unless GO/pathway-version conventions are fixed
- organic-carbon assimilation into biomass — label-only biological-process node
- anaplerotic CO₂ fixation — label-only; optional boundary node

### Genes, proteins and complexes

**Taxon-specific *E. coli* exemplars:**

- `ptsG` — glucose-specific PTS EIICB component
- `ptsH`, `ptsI`, `crr` — HPr, enzyme I and EIIA^Glc, respectively
- `ompF`, `ompC` — outer-membrane porins used under relatively glucose-rich conditions
- `lamB` — preferentially induced under glucose limitation
- ABC-family glucose/sugar transporters
- major facilitator superfamily proton symporters

The *E. coli* PTS transfers phosphate from PEP through EI, HPr and EIIA/EIIB to incoming glucose, producing glucose 6-phosphate. The reviewed PtsG system has a reported **Kₘ of 10–20 μM**, and one estimate gives **37 glucose molecules imported and phosphorylated per IICB^Glc molecule per second** (carreonrodriguez2023glucosetransportin pages 5-7).

**Taxon-specific *L. ochracea* candidates:**

- `gtsABC`, glucose/mannose transporter
- `frcABC`, fructose transporter
- `lctP`, L-lactate permease
- `ykgEFG`, L-lactate dehydrogenase system
- `actP`, acetate permease
- `ackA`, acetate kinase
- respiratory complexes I–IV, cbb3-type oxidase and cytochrome-bd oxidase
- RuBisCO/CBB components as mixotrophy boundary markers

These are supported by MAGs and environmental expression, not knockout or isolate-complementation experiments (tothero2024leptothrixochraceagenomes pages 13-15, tothero2024leptothrixochraceagenomes pages 9-13).

**Hadal Group-3.unk candidates:**

- amino-acid and carbohydrate ABC transporters
- V-type ATP synthase
- partial cytochrome-c oxidase system
- `OforAB`, putative substitute for pyruvate dehydrogenase-related 2-oxoacid conversion
- `CoxLMS`, putative aerobic CO dehydrogenase
- `EcfT`, vitamin/micronutrient transporter

The authors explicitly caution that Form II CoxL does not invariably confer CO oxidation; this node should not be curated as functional without direct validation (zhang2024metagenomiccharacterizationof pages 8-11).

### Cellular locations

- extracellular environment
- Gram-negative outer membrane
- periplasm
- cytoplasmic/inner membrane
- cytoplasm
- mitochondrion in heterotrophic eukaryotic microalgae

In *E. coli*, glucose first diffuses through outer-membrane porins into the periplasm, then crosses the inner membrane through PTS, ABC, or MFS systems (carreonrodriguez2023glucosetransportin pages 1-2, carreonrodriguez2023glucosetransportin pages 3-4).

## 3. Candidate causal edges

The following triples separate a compact core from organism-specific expansions.

| Priority | Subject — predicate — object | Reference | Supporting source snippet | Curation note |
|---|---|---|---|---|
| Core | organic carbon availability — **enables** — heterotrophic carbon uptake | DOI: [10.1186/s40168-023-01728-2](https://doi.org/10.1186/s40168-023-01728-2), published Jan 2024 | “ABC transporters for the uptake of amino acids and carbohydrates and catabolic utilization of these substrates” | Generic at the class level; individual substrate/transporter edges remain conditional (zhang2024metagenomiccharacterizationof pages 1-2). |
| Core, sugar-utilizing taxa | glucose — **is transported by** — PTS/ABC/MFS systems | DOI: [10.3390/microorganisms11061588](https://doi.org/10.3390/microorganisms11061588), published 15 Jun 2023 | “including the…PTS, the…ABC transporters, and…the MFS…proton symporters” | Mechanistically strong for *E. coli*; do not require all three families in every heterotroph (carreonrodriguez2023glucosetransportin pages 1-2). |
| *E. coli* exemplar | OmpF/OmpC or LamB — **facilitates** — glucose entry into periplasm | same DOI | “under glucose limiting conditions, LamB is induced and diffuses glucose preferentially into the periplasm” | Environment-conditioned outer-membrane edge (carreonrodriguez2023glucosetransportin pages 5-7). |
| *E. coli* exemplar | PEP-dependent PTS — **couples** — glucose import to glucose-6-phosphate formation | same DOI | “concomitant uptake and phosphorylation” | Strong molecular edge; PTS is not universal (carreonrodriguez2023glucosetransportin pages 5-7). |
| Core, sugar-utilizing taxa | imported glucose — **feeds** — glycolysis | same DOI | “transport and breakdown of imported glucose through the glycolytic pathway” | Safe conditional module, not a universal substrate requirement (carreonrodriguez2023glucosetransportin pages 3-4). |
| Core | central organic-carbon catabolism — **supplies** — biosynthetic precursors | same DOI | glucose catabolism “supplies at least 12 biosynthetic precursors” | The number 12 is *E. coli*-specific; the precursor relationship is broadly curatable (carreonrodriguez2023glucosetransportin pages 3-4). |
| Conditional | LctP — **imports** — L-lactate | DOI: [10.1128/aem.00599-24](https://doi.org/10.1128/aem.00599-24), published Sep 2024 | MAGs contain “L-lactate permease (lctP)” | *L. ochracea* MAG inference; uncertain until culture validation (tothero2024leptothrixochraceagenomes pages 13-15). |
| Conditional | YkgEFG — **converts** — L-lactate to pyruvate | same DOI | “L-lactate dehydrogenase (ykgEFG) converting lactate to pyruvate” | Taxon-specific genomic inference (tothero2024leptothrixochraceagenomes pages 13-15). |
| Conditional | acetate or lactate — **feeds** — TCA-cycle intermediates | same DOI | “Both lactate and acetate can feed into TCA cycle intermediates” | Useful substrate expansion; not universal and partly model-based (tothero2024leptothrixochraceagenomes pages 13-15). |
| Core, respiring taxa | oxidation of organic compounds — **generates** — reducing equivalents/electron flow | same DOI | organic carbon can be oxidized “to generate NADH for energy” | Keep generic; exact dehydrogenases and carriers vary (tothero2024leptothrixochraceagenomes pages 9-13). |
| Conditional aerobic branch | oxygen + electron-transport chain — **enables** — aerobic respiration | same DOI | “complete electron transport chains (Complexes I–IV)” and terminal oxidases | Do not make oxygen a defining parent of heterotrophy (tothero2024leptothrixochraceagenomes pages 9-13). |
| Core, respiring taxa | heterotrophic respiration — **converts part of** — organic carbon to CO₂ | DOI: [10.3389/fmicb.2023.1049579](https://doi.org/10.3389/fmicb.2023.1049579), published 16 Feb 2023 | bacteria act by “utilizing, respiring, and remineralizing organic matter” | Distinguish respired carbon from assimilated biomass carbon (kim2023projected21stcenturychanges pages 1-2). |
| Conditional anaerobic branch | organic-substrate catabolism — **supports** — fermentation products | DOI: [10.1038/s41467-019-09747-0](https://doi.org/10.1038/s41467-019-09747-0), published Apr 2019 | pathways produce “acetate, lactate, and ethanol” | Environmental MAG/metabolomics evidence; product differs by organism and condition (dong2019metabolicpotentialof pages 4-5). |
| Conditional | glyoxylate cycle — **supplies** — anabolic intermediates | DOI: [10.1186/s40168-023-01728-2](https://doi.org/10.1186/s40168-023-01728-2), Jan 2024 | “Complete glyoxylate cycle…supplying intermediates of anabolic pathways” | Group-3.unk-specific genomic inference (zhang2024metagenomiccharacterizationof pages 1-2). |
| Boundary | heterotrophic carboxylation — **incorporates a minority of** — inorganic carbon into biomass | DOI: [10.5194/bg-18-3689-2021](https://doi.org/10.5194/bg-18-3689-2021), published Jun 2021 | heterotrophic fixation contributes “1–8% to microbial carbon biomass” | Optional explanatory edge; prevents the erroneous rule that heterotrophs never fix CO₂ (braun2021reviewsandsyntheses pages 1-2). |
| Boundary | substantial organic-carbon utilization + CBB/RuBisCO activity — **supports classification as** — mixotrophic | DOI: [10.1128/aem.00599-24](https://doi.org/10.1128/aem.00599-24), Sep 2024 | genes and expression support use of “both inorganic and organic carbon sources” | Do not curate *L. ochracea* as a strict heterotroph from transporter genes alone (tothero2024leptothrixochraceagenomes pages 1-2). |
| Assay | growth in darkness + organic carbon consumption — **supports** — heterotrophic phenotype | DOI: [10.3389/fbioe.2023.1296216](https://doi.org/10.3389/fbioe.2023.1296216), published 9 Nov 2023 | “rapid growth in complete darkness” and use of “diverse carbon sources” | Strong for photosynthetic microbes when paired with no-carbon controls (jareonsin2023unlockingmicroalgalhost—exploring pages 1-2). |

A compact prioritization of these claims is provided below.

| tier | subject | predicate | object | evidence type | scope/caveat |
|---|---|---|---|---|---|
| core | organic carbon availability | enables | uptake and catabolic use as cellular carbon source | definition/review + environmental genomics (braun2021reviewsandsyntheses pages 1-2, zhang2024metagenomiccharacterizationof pages 1-2) | Generic heterotrophy scope; carbon source, not specific energy metabolism |
| core | glucose transport systems (PTS/ABC/MFS) | transport | glucose into the cytoplasm | mechanistic review (carreonrodriguez2023glucosetransportin pages 1-2, carreonrodriguez2023glucosetransportin pages 3-4) | Strong for *E. coli* and broadly plausible in bacteria, but named systems are not universal |
| conditional | ptsG / ptsHIcrr (PTS), ABC transporters, MFS symporters | mediate | glucose uptake and phosphorylation/import | gene-level mechanism (carreonrodriguez2023glucosetransportin pages 3-4, carreonrodriguez2023glucosetransportin pages 5-7) | Taxon-specific exemplar from *E. coli*; do not require these exact genes for all heterotrophs |
| core | imported glucose | feeds | glycolysis and formation of biosynthetic precursors | mechanistic review (carreonrodriguez2023glucosetransportin pages 3-4) | Good generic central-carbon edge for sugar-using heterotrophs |
| conditional | L-lactate permease (lctP) + L-lactate dehydrogenase (ykgEFG) | converts | lactate to pyruvate | comparative genomics (tothero2024leptothrixochraceagenomes pages 13-15) | Explicitly *Leptothrix ochracea* MAG inference; not yet isolate-validated |
| conditional | acetate and lactate | feed into | TCA cycle intermediates | comparative genomics/metabolic interpretation (tothero2024leptothrixochraceagenomes pages 13-15) | *Leptothrix ochracea* specific inference from genomes/transcript context |
| core | central carbon catabolism | supports | ATP generation and biomass precursor supply | review/synthesis + physiology review (braun2021reviewsandsyntheses pages 1-2, stegemuller2024synergisticeffectsof pages 1-2) | Broad mechanism across heterotrophs; exact pathway usage varies |
| core | heterotrophic respiration of organic carbon | produces | CO2 | review/synthesis + ecosystem analysis (braun2021reviewsandsyntheses pages 1-2, kim2023projected21stcenturychanges pages 1-2) | Applies to respiring heterotrophs; fermentation-only cases differ in end products |
| conditional | glyoxylate cycle | supplies | intermediates for anabolic pathways | metagenomic pathway reconstruction (zhang2024metagenomiccharacterizationof pages 1-2, zhang2024metagenomiccharacterizationof pages 8-11) | Group-3.unk non-AOA Thaumarchaeota-specific genomic inference |
| conditional | oxygen availability | enables | electron transport chain use / aerobic respiration | genomic + physiology evidence (zhang2024metagenomiccharacterizationof pages 8-11, tothero2024leptothrixochraceagenomes pages 9-13) | Only for aerobic taxa with ETC genes; not a defining requirement of heterotrophy |
| conditional | dark conditions + organic carbon | support | heterotrophic microalgal growth | cultivation/application studies (jareonsin2023unlockingmicroalgalhost—exploring pages 1-2, tocca2024mixotrophicandheterotrophic pages 1-2) | Eukaryotic microalgae implementation; not a universal microbial assay |
| do-not-generalize | CBB cycle / RuBisCO + organic-carbon utilization | indicates | mixotrophy rather than strict heterotrophy | genomics/transcriptomics (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 9-13) | Important boundary case; should exclude strict heterotroph curation if carbon fixation is substantial |
| do-not-generalize | heterotrophs | may fix | a minority of inorganic carbon into biomass | review/synthesis (braun2021reviewsandsyntheses pages 1-2) | Usually minor (often ~1–8%); does not negate heterotrophic status |


*Table: This table prioritizes candidate causal edges for curating METPO:1000644 into core, conditional, and non-generalizable claims. It emphasizes which mechanisms are broadly safe to curate versus those that are taxon-specific genomic inferences or boundary-case interpretations.*

## 4. Recommended assay model

A defensible trait assertion should ideally combine:

1. **Defined medium** with a specified organic carbon compound.
2. **No-organic-carbon control**; for phototrophs, a dark condition or photosynthesis-inhibited control.
3. **Net growth measurement**, such as optical density, cell counts, dry mass, protein, or DNA.
4. **Substrate depletion** and preferably carbon mass balance.
5. **Isotope tracing**—for example, incorporation from ^13C-labeled substrate—to demonstrate that organic carbon enters biomass rather than merely stimulating another process.
6. **Respiration/product measurements**, such as O₂ uptake, CO₂ evolution, nitrate reduction, or fermentation products, to identify the energy branch without conflating it with heterotrophy.
7. **Genetic evidence** where feasible: loss of uptake/growth after transporter or catabolic-gene disruption and restoration by complementation.

Growth on glucose as the sole carbon source is well established in *E. coli*: reported specific growth rates include **0.57 h⁻¹ for K-12, 0.92 h⁻¹ for MG1655, and 0.7 h⁻¹ for JM101**. Those values demonstrate that growth kinetics are strain- and condition-dependent rather than intrinsic to the ontology class (carreonrodriguez2023glucosetransportin pages 3-4).

## 5. Recent developments and quantitative evidence

### 5.1 Expanded environmental diversity

The 2024 Challenger Deep study recovered a novel non-ammonia-oxidizing Thaumarchaeota group with ABC transporters for amino acids and carbohydrates, central carbon pathways, a glyoxylate cycle, and no complete recognized autotrophic fixation pathway. The samples came from **10,853 m** depth. This expands candidate heterotrophy into hadal archaea but remains a culture-independent prediction (zhang2024metagenomiccharacterizationof pages 8-11, zhang2024metagenomiccharacterizationof pages 1-2).

The 2024 *L. ochracea* work illustrates why multi-omics changes classification: sugar and organic-acid transport/catabolism alone suggested heterotrophy, but RuBisCO/CBB genes, iron oxidation genes, expression profiles and metabolic modeling collectively favored mixotrophy. This is an authoritative warning against assigning trophic traits from a single marker gene or module (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 9-13).

### 5.2 Heterotrophic and mixotrophic microalgal production

A 2024 *Haematococcus lacustris* experiment measured maximum mixotrophic growth rates of **0.91 ± 0.13 d⁻¹ on acetate, 0.19 ± 0.05 d⁻¹ on methanol, 0.36 ± 0.05 d⁻¹ on glucose, and 0.23 ± 0.05 d⁻¹ on glycerol**. Optimal acetate-supported mixotrophic growth was **1.8-fold higher than the sum** of separately measured heterotrophic and photoautotrophic growth, illustrating nonadditive interaction between trophic modules (stegemuller2024synergisticeffectsof pages 1-2).

In *Chlorella vulgaris*, sodium acetate increased TCA-cycle activity and mitochondrial ATP/CO₂ generation; heterotrophic energy production was reported to derive almost entirely from mitochondria. Because the study’s main emphasis was mixotrophy, these edges should be maintained as algal/taxon-specific rather than a universal microbial graph (yan2024carbonandenergy pages 8-9).

### 5.3 Global carbon-cycle implications

A 2023 Earth-system-model analysis projected marine heterotrophic bacterial biomass to decline **5–10% globally by 2076–2099**, while increasing **3–5% in the Southern Ocean**. Semi-labile dissolved organic carbon drove Southern Ocean uptake changes, whereas temperature drove changes in northern high and low latitudes. These are model projections—not direct physiological effect sizes—but they demonstrate the relevance of substrate availability and temperature as graph modifiers (kim2023projected21stcenturychanges pages 1-2).

## 6. Applications and implementations

- **Industrial *E. coli* cell factories:** glucose transport and central-carbon flux underpin production of recombinant proteins, metabolites, biofuels and nanomaterials. EcoCyc data summarized in the 2023 review list **532 transport reactions, 480 transporters and 97 proteins involved in sugar transport** for MG1655, illustrating extensive redundancy and why no single transporter is a universal heterotrophy marker (carreonrodriguez2023glucosetransportin pages 1-2).
- **Transport engineering:** replacing or modifying PTS/ABC/MFS uptake can redirect carbon toward products and reduce carbon-catabolite repression. This is an implementation of heterotrophic uptake engineering, not a change to the trait definition (carreonrodriguez2023glucosetransportin pages 1-2, carreonrodriguez2023glucosetransportin pages 5-7).
- **Dark microalgal cell factories:** *C. sorokiniana* was transformed under complete darkness for prospective production of nutrients, nutraceuticals, proteins and pharmaceuticals. G418, hygromycin and streptomycin inhibited growth by **98%, 93% and 92%**, respectively, providing selectable-marker performance data for a heterotrophic host platform (jareonsin2023unlockingmicroalgalhost—exploring pages 1-2).
- **Circular acetate biorefineries:** a 2024 review argues that waste- or C1-derived acetate can connect waste conversion with algal biomass production. It reported indicative acetate and glucose prices of **€0.44–0.46 kg⁻¹** and **€0.55–0.78 kg⁻¹**, respectively, while emphasizing that purification, inhibition, scale-up and economics remain unresolved (tocca2024mixotrophicandheterotrophic pages 1-2).
- **Wastewater and anaerobic-processing integration:** thermochemical process waters can contain **0.7–33 g L⁻¹ acetate**, while acidogenic effluents commonly contain **0.3–29 g L⁻¹**. These streams are potential heterotrophic substrates but may also contain antimicrobial contaminants and therefore require growth and toxicity validation (tocca2024mixotrophicandheterotrophic pages 7-9).

## 7. Expert synthesis for `heterotrophic.yaml`

### Minimum core graph

1. `organic carbon compound` — **available_in_environment** → `cell exterior`
2. `organic carbon compound` — **transported_by** → `organic-compound transport system`
3. `organic-compound transport` — **increases** → `intracellular organic substrate`
4. `intracellular organic substrate` — **catabolized_by** → `central carbon metabolism`
5. `central carbon metabolism` — **produces** → `precursor metabolites`
6. `precursor metabolites` — **incorporated_into** → `cellular biomass`
7. `central carbon metabolism` — **produces** → `reducing equivalents`
8. `reducing equivalents` — **support** → `energy conservation`
9. `energy conservation` — **supports** → `growth`
10. `organic-carbon assimilation and growth` — **manifests_as** → `METPO:1000644`

### Conditional branches

- sugar → PTS/ABC/MFS → glycolysis/ED/PPP
- lactate → permease/dehydrogenase → pyruvate
- acetate → acetyl-CoA-generating reactions → TCA/glyoxylate cycle
- oxygen present + respiratory machinery → aerobic respiration → ATP + CO₂
- alternative acceptor present → anaerobic respiration
- acceptor-limited/fermentative physiology → fermentation products + redox regeneration
- photosynthetic machinery active together with organic-carbon assimilation → mixotrophy boundary

This structure preserves the trait’s causal meaning without asserting that glucose, glycolysis, oxygen, the TCA cycle, PTS, or mitochondria are necessary in every heterotroph.

## 8. Warnings: claims not ready for TraitMech curation

1. **Do not equate “aerobic heterotrophy” with all heterotrophy.** It excludes anaerobic respirers and fermenters.
2. **Do not make glucose the defining substrate.** Heterotrophs use diverse sugars, organic acids, amino acids, fatty acids, hydrocarbons and complex organic matter.
3. **Do not require PTS, `ptsG`, glycolysis, or a complete TCA cycle.** These are common exemplars, not universal necessities.
4. **Do not infer demonstrated heterotrophy from MAG annotation alone.** Group-3.unk and *L. ochracea* edges should carry `uncertain`, `predicted_from_genome`, or equivalent evidence qualifiers (tothero2024leptothrixochraceagenomes pages 1-2, zhang2024metagenomiccharacterizationof pages 1-2).
5. **Do not infer CO oxidation from Form II `coxL` alone.** The 2024 hadal study notes that some organisms possessing it cannot oxidize CO (zhang2024metagenomiccharacterizationof pages 8-11).
6. **Do not classify RuBisCO-containing, organic-carbon-using organisms automatically as strict heterotrophs.** Evaluate flux and growth evidence for mixotrophy (tothero2024leptothrixochraceagenomes pages 1-2).
7. **Do not require zero inorganic-carbon incorporation.** Anaplerotic fixation can supply a measurable minority of heterotrophic biomass carbon (braun2021reviewsandsyntheses pages 1-2).
8. **Do not treat substrate disappearance alone as assimilation.** It may reflect oxidation, adsorption or cometabolism; pair it with growth and preferably isotope incorporation.
9. **Do not generalize eukaryotic mitochondrial mechanisms to bacteria or archaea.** Keep cellular localization taxon-specific.
10. **Do not curate modeled climate projections as organism-level causal constants.** They support environmental modifiers, not universal effect sizes (kim2023projected21stcenturychanges pages 1-2).

## DOI-first bibliography

1. Carreón-Rodríguez OE, Gosset G, Escalante A, Bolívar F. “Glucose Transport in *Escherichia coli*: From Basics to Transport Engineering.” *Microorganisms*. Published **15 June 2023**. DOI: [10.3390/microorganisms11061588](https://doi.org/10.3390/microorganisms11061588) (carreonrodriguez2023glucosetransportin pages 1-2).
2. Tothero GK et al. “*Leptothrix ochracea* genomes reveal potential for mixotrophic growth on Fe(II) and organic carbon.” *Applied and Environmental Microbiology*. Published **September 2024**. DOI: [10.1128/aem.00599-24](https://doi.org/10.1128/aem.00599-24) (tothero2024leptothrixochraceagenomes pages 1-2).
3. Zhang R-Y et al. “Metagenomic characterization of a novel non-ammonia-oxidizing Thaumarchaeota from hadal sediment.” *Microbiome*. Published **January 2024**. DOI: [10.1186/s40168-023-01728-2](https://doi.org/10.1186/s40168-023-01728-2) (zhang2024metagenomiccharacterizationof pages 1-2).
4. Proietti Tocca G et al. “Mixotrophic and heterotrophic growth of microalgae using acetate from different production processes.” *Reviews in Environmental Science and Bio/Technology*. Published **20 February 2024**. DOI: [10.1007/s11157-024-09682-7](https://doi.org/10.1007/s11157-024-09682-7) (tocca2024mixotrophicandheterotrophic pages 1-2).
5. Stegemüller L et al. “Synergistic effects of heterotrophic and phototrophic metabolism for *Haematococcus lacustris* grown under mixotrophic conditions.” *Journal of Applied Phycology*. Published **30 July 2024**. DOI: [10.1007/s10811-024-03322-x](https://doi.org/10.1007/s10811-024-03322-x) (stegemuller2024synergisticeffectsof pages 1-2).
6. Yan X et al. “Carbon and energy metabolism for the mixotrophic culture of *Chlorella vulgaris* using sodium acetate as a carbon source.” *Frontiers in Microbiology*. Published **October 2024**. DOI: [10.3389/fmicb.2024.1436264](https://doi.org/10.3389/fmicb.2024.1436264) (yan2024carbonandenergy pages 8-9).
7. Jareonsin S et al. “Unlocking microalgal host—exploring dark-growing microalgae transformation for sustainable high-value phytochemical production.” *Frontiers in Bioengineering and Biotechnology*. Published **9 November 2023**. DOI: [10.3389/fbioe.2023.1296216](https://doi.org/10.3389/fbioe.2023.1296216) (jareonsin2023unlockingmicroalgalhost—exploring pages 1-2).
8. Kim HH et al. “Projected 21st-century changes in marine heterotrophic bacteria under climate change.” *Frontiers in Microbiology*. Published **16 February 2023**. DOI: [10.3389/fmicb.2023.1049579](https://doi.org/10.3389/fmicb.2023.1049579) (kim2023projected21stcenturychanges pages 1-2).
9. Braun A et al. “Heterotrophic fixation of inorganic carbon—significant but invisible flux in environmental carbon cycling.” *Biogeosciences*. Published **June 2021**. DOI: [10.5194/bg-18-3689-2021](https://doi.org/10.5194/bg-18-3689-2021) (braun2021reviewsandsyntheses pages 1-2).
10. Dong X et al. “Metabolic potential of uncultured bacteria and archaea associated with petroleum seepage in deep-sea sediments.” *Nature Communications*. Published **April 2019**. DOI: [10.1038/s41467-019-09747-0](https://doi.org/10.1038/s41467-019-09747-0) (dong2019metabolicpotentialof pages 4-5).
11. Alagesan S, Minton NP, Malys N. “13C-assisted metabolic flux analysis to investigate heterotrophic and mixotrophic metabolism in *Cupriavidus necator* H16.” *Metabolomics*. Published **2018**. DOI: [10.1007/s11306-017-1302-z](https://doi.org/10.1007/s11306-017-1302-z) (alagesan201813cassistedmetabolicflux pages 1-2).

References

1. (braun2021reviewsandsyntheses pages 1-2): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.

2. (tothero2024leptothrixochraceagenomes pages 1-2): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 24 citations and is from a peer-reviewed journal.

3. (tothero2024leptothrixochraceagenomes pages 9-13): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 24 citations and is from a peer-reviewed journal.

4. (alagesan201813cassistedmetabolicflux pages 1-2): Swathi Alagesan, Nigel P. Minton, and Naglis Malys. 13c-assisted metabolic flux analysis to investigate heterotrophic and mixotrophic metabolism in cupriavidus necator h16. Metabolomics, Dec 2018. URL: https://doi.org/10.1007/s11306-017-1302-z, doi:10.1007/s11306-017-1302-z. This article has 79 citations and is from a peer-reviewed journal.

5. (jareonsin2023unlockingmicroalgalhost—exploring pages 1-2): Surumpa Jareonsin, Kanjana Mahanil, Kittiya Phinyo, Sirasit Srinuanpan, Jeeraporn Pekkoh, Masafumi Kameya, Hiroyuki Arai, Masaharu Ishii, Ruttaporn Chundet, Pachara Sattayawat, and Chayakorn Pumas. Unlocking microalgal host—exploring dark-growing microalgae transformation for sustainable high-value phytochemical production. Frontiers in Bioengineering and Biotechnology, Nov 2023. URL: https://doi.org/10.3389/fbioe.2023.1296216, doi:10.3389/fbioe.2023.1296216. This article has 6 citations.

6. (zhang2024metagenomiccharacterizationof pages 8-11): Ru-Yi Zhang, Yan-Ren Wang, Ru-Long Liu, Sung-Keun Rhee, Guo-Ping Zhao, and Zhe-Xue Quan. Metagenomic characterization of a novel non-ammonia-oxidizing thaumarchaeota from hadal sediment. Microbiome, Jan 2024. URL: https://doi.org/10.1186/s40168-023-01728-2, doi:10.1186/s40168-023-01728-2. This article has 25 citations and is from a highest quality peer-reviewed journal.

7. (zhang2024metagenomiccharacterizationof pages 1-2): Ru-Yi Zhang, Yan-Ren Wang, Ru-Long Liu, Sung-Keun Rhee, Guo-Ping Zhao, and Zhe-Xue Quan. Metagenomic characterization of a novel non-ammonia-oxidizing thaumarchaeota from hadal sediment. Microbiome, Jan 2024. URL: https://doi.org/10.1186/s40168-023-01728-2, doi:10.1186/s40168-023-01728-2. This article has 25 citations and is from a highest quality peer-reviewed journal.

8. (kim2023projected21stcenturychanges pages 1-2): Heather H. Kim, Charlotte Laufkötter, Tomas Lovato, Scott C. Doney, and Hugh W. Ducklow. Projected 21st-century changes in marine heterotrophic bacteria under climate change. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1049579, doi:10.3389/fmicb.2023.1049579. This article has 34 citations and is from a peer-reviewed journal.

9. (carreonrodriguez2023glucosetransportin pages 5-7): Ofelia E. Carreón-Rodríguez, Guillermo Gosset, Adelfo Escalante, and Francisco Bolívar. Glucose transport in escherichia coli: from basics to transport engineering. Microorganisms, 11:1588, Jun 2023. URL: https://doi.org/10.3390/microorganisms11061588, doi:10.3390/microorganisms11061588. This article has 83 citations.

10. (tothero2024leptothrixochraceagenomes pages 13-15): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 24 citations and is from a peer-reviewed journal.

11. (carreonrodriguez2023glucosetransportin pages 1-2): Ofelia E. Carreón-Rodríguez, Guillermo Gosset, Adelfo Escalante, and Francisco Bolívar. Glucose transport in escherichia coli: from basics to transport engineering. Microorganisms, 11:1588, Jun 2023. URL: https://doi.org/10.3390/microorganisms11061588, doi:10.3390/microorganisms11061588. This article has 83 citations.

12. (carreonrodriguez2023glucosetransportin pages 3-4): Ofelia E. Carreón-Rodríguez, Guillermo Gosset, Adelfo Escalante, and Francisco Bolívar. Glucose transport in escherichia coli: from basics to transport engineering. Microorganisms, 11:1588, Jun 2023. URL: https://doi.org/10.3390/microorganisms11061588, doi:10.3390/microorganisms11061588. This article has 83 citations.

13. (dong2019metabolicpotentialof pages 4-5): Xiyang Dong, Chris Greening, Jayne E. Rattray, Anirban Chakraborty, Maria Chuvochina, Daisuke Mayumi, Jan Dolfing, Carmen Li, James M. Brooks, Bernie B. Bernard, Ryan A. Groves, Ian A. Lewis, and Casey R. J. Hubert. Metabolic potential of uncultured bacteria and archaea associated with petroleum seepage in deep-sea sediments. Nature Communications, Apr 2019. URL: https://doi.org/10.1038/s41467-019-09747-0, doi:10.1038/s41467-019-09747-0. This article has 252 citations and is from a highest quality peer-reviewed journal.

14. (stegemuller2024synergisticeffectsof pages 1-2): Lars Stegemüller, Borja Valverde-Pérez, Anders Thygesen, and Irini Angelidaki. Synergistic effects of heterotrophic and phototrophic metabolism for haematococcus lacustris grown under mixotrophic conditions. Journal of Applied Phycology, 36:3175-3186, Jul 2024. URL: https://doi.org/10.1007/s10811-024-03322-x, doi:10.1007/s10811-024-03322-x. This article has 11 citations and is from a peer-reviewed journal.

15. (tocca2024mixotrophicandheterotrophic pages 1-2): Giacomo Proietti Tocca, Valeria Agostino, Barbara Menin, Tonia Tommasi, Debora Fino, and Fabrizio Di Caprio. Mixotrophic and heterotrophic growth of microalgae using acetate from different production processes. Reviews in Environmental Science and Bio/Technology, 23:93-132, Feb 2024. URL: https://doi.org/10.1007/s11157-024-09682-7, doi:10.1007/s11157-024-09682-7. This article has 82 citations.

16. (yan2024carbonandenergy pages 8-9): Xi Yan, Shengzhou Shan, Xiaohui Li, Qingshan Xu, Xiaojun Yan, Roger Ruan, and Pengfei Cheng. Carbon and energy metabolism for the mixotrophic culture of chlorella vulgaris using sodium acetate as a carbon source. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1436264, doi:10.3389/fmicb.2024.1436264. This article has 26 citations and is from a peer-reviewed journal.

17. (tocca2024mixotrophicandheterotrophic pages 7-9): Giacomo Proietti Tocca, Valeria Agostino, Barbara Menin, Tonia Tommasi, Debora Fino, and Fabrizio Di Caprio. Mixotrophic and heterotrophic growth of microalgae using acetate from different production processes. Reviews in Environmental Science and Bio/Technology, 23:93-132, Feb 2024. URL: https://doi.org/10.1007/s11157-024-09682-7, doi:10.1007/s11157-024-09682-7. This article has 82 citations.