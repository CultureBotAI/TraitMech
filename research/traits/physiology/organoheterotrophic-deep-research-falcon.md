---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:33:59.415404'
end_time: '2026-08-04T11:44:10.374019'
duration_seconds: 610.96
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: organoheterotrophic
  trait_identifier: METPO:1000664
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: organoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of organic compounds as both
    electron donors and primary carbon sources for energy generation and biosynthesis.
  parent_traits: METPO:1000631
  synonyms: organoheterotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the
    primary sources of carbon and energy (Encyclopedia chapter supports organic compounds
    as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008:
    free energy of a redox reaction (Review supports energy conservation from electron
    donor oxidation through respiratory chains.)'
  causal_graph_summary: 'organoheterotrophic_organic_donor_carbon: 12 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000664
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of organic compounds as both electron donors and primary carbon sources for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** organoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon and energy (Encyclopedia chapter supports organic compounds as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports energy conservation from electron donor oxidation through respiratory chains.)
- **Existing causal graph summary:** organoheterotrophic_organic_donor_carbon: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **organoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organoheterotrophic.yaml`.

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
- **Trait label:** organoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000664
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of organic compounds as both electron donors and primary carbon sources for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** organoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon and energy (Encyclopedia chapter supports organic compounds as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports energy conservation from electron donor oxidation through respiratory chains.)
- **Existing causal graph summary:** organoheterotrophic_organic_donor_carbon: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **organoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organoheterotrophic.yaml`.

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


# Curation report: organoheterotrophic microbial trait

## 1. Scope summary

**Trait:** organoheterotrophic  
**Identifier:** `METPO:1000664`  
**Category/kind/status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** `METPO:1000631`

Organoheterotrophy is a trophic strategy in which **organic compounds provide both the principal carbon source and the reducing equivalents/electrons used for energy conservation**. A concise operational formulation is: uptake or extracellular depolymerization of organic matter, intracellular catabolism through one or more central-carbon routes, allocation of carbon skeletons to biomass, and conservation of energy by respiration or fermentation. A major review defines heterotrophs as organisms that “respire organic compounds to gain energy and build up biomass”; oxidation may use oxygen or alternative electron acceptors such as nitrate, ferric iron, or sulfate (braun2021reviewsandsyntheses pages 1-2).

The trait is broader than aerobic growth. It includes aerobic and anaerobic respiration and fermentative growth, provided organic compounds remain the primary carbon source and electron donors. Conversely, presence of glycolysis, a TCA cycle, transporters, or respiratory genes alone is insufficient to establish the phenotype.

### Boundary cases

- **Autotrophy:** inorganic carbon is the principal carbon source. Mere anaplerotic incorporation of CO2 does not make an organism autotrophic: heterotrophic anaplerosis commonly contributes approximately 1–8% of microbial biomass carbon (braun2021reviewsandsyntheses pages 2-4, braun2021reviewsandsyntheses pages 1-2).
- **Mixotrophy:** simultaneous or condition-dependent combination of heterotrophic machinery with phototrophy or chemolithotrophy. Therefore, demonstrated organoheterotrophic growth may be one mode of a mixotroph rather than an organism-wide obligate phenotype (eiler2006evidenceforthe pages 1-2, burgsdorf2021rethinkingsymbioticmetabolism pages 1-4).
- **Lithoheterotrophy:** organic carbon remains the biomass source, but inorganic compounds provide some or all reducing power. It should not be asserted as organoheterotrophy unless organic compounds are also shown to act as electron donors (burgsdorf2021rethinkingsymbioticmetabolism pages 1-4).
- **Photoheterotrophy:** organic carbon is assimilated, but light supplies energy. This is heterotrophic with respect to carbon but is not necessarily organoheterotrophic under the supplied definition because organic compounds need not be the primary energy/electron source.
- **Methylotrophy and methanotrophy:** organic C1 compounds can satisfy the literal organic-donor/organic-carbon criterion, but many databases treat these as separate specialist trophic classes. Methanotrophs may derive up to 50% of biomass carbon from CO2 while still depending on methane-derived energy; any mapping should follow METPO’s explicit modeling policy (braun2021reviewsandsyntheses pages 1-2, braun2021reviewsandsyntheses pages 4-5).
- **Assay interpretation:** growth on an organic substrate is strong phenotype evidence; disappearance of substrate plus biomass labeling is stronger. Genome or transcript detection only establishes potential or activity of modules, not necessarily organic carbon as both primary carbon and energy source (burgsdorf2021rethinkingsymbioticmetabolism pages 1-4, campana2021dna‐stableisotopeprobing pages 1-2).

## 2. Candidate nodes grouped by type

### Trait and process nodes

- organoheterotrophic — `METPO:1000664`
- organic-compound uptake — label-only candidate
- extracellular organic-matter depolymerization — label-only candidate
- heterotrophic carbon metabolism — label-only candidate
- glycolysis / Embden–Meyerhof–Parnas pathway — `KEGG:map00010`
- Entner–Doudoroff pathway — label-only pending ontology validation
- pentose-phosphate pathway — `KEGG:map00030`
- tricarboxylic-acid cycle — `KEGG:map00020`
- respiratory electron transport — `GO:0022900`
- ATP synthesis coupled to proton transport — `GO:0015986`
- fermentation — `GO:0006113`
- biosynthesis/anabolism — `GO:0009058`
- anaplerotic CO2 fixation — label-only candidate
- microbial carbon-use efficiency — label-only experimental-factor node

### Chemicals and nutrients

- organic compound — `CHEBI:33229`
- dissolved organic matter and particulate organic matter — label-only; these are mixtures rather than single ChEBI entities
- glucose — use a verified ChEBI mapping during implementation
- pyruvate — `CHEBI:15361`
- acetyl-CoA — `CHEBI:15351`
- NADH — `CHEBI:16908`
- NADPH — `CHEBI:16474`
- oxygen — `CHEBI:15379`
- carbon dioxide — `CHEBI:16526`
- acetate — `CHEBI:30089`
- ethanol — `CHEBI:16236`
- nitrate, ferric iron, and sulfate — verify ChEBI CURIEs before YAML insertion
- ATP, ADP, proton, quinone/quinol, lactate, and TCA intermediates — retain as label-only until identifier validation

### Proteins, enzymes, transporters, and complexes

These should be modeled as **representative or optional modules**, not universally required markers:

- substrate-specific organic-compound transporter
- carbohydrate-active enzymes and extracellular hydrolases
- phosphotransferase system or ABC-type sugar transporter
- glycolytic, ED, and PPP enzymes
- pyruvate dehydrogenase complex
- TCA-cycle enzymes
- NADH dehydrogenase, quinone pool, terminal oxidase, or anaerobic terminal reductase
- F-type or A/V-type ATP synthase
- fermentative dehydrogenases
- pyruvate carboxylase and phosphoenolpyruvate carboxylase for anaplerosis

No single transporter, glycolytic route, respiratory complex, or terminal reductase is universal across bacterial, archaeal, fungal, and protistan organoheterotrophs. Protein-specific UniProt identifiers would therefore be inappropriate without a taxon and sequence.

### Cellular locations

- extracellular space or cell surface: polymer depolymerization
- plasma/cytoplasmic membrane: substrate transport, respiratory chain, ATP synthase
- cytosol: central carbon metabolism and fermentation
- mitochondrion/inner mitochondrial membrane: eukaryotic microbial TCA cycle, respiration, and ATP synthesis

Localization is domain-specific and should be represented as conditional branches rather than a single universal chain.

### Environmental and experimental factors

- availability, composition, and molecular accessibility of organic carbon
- oxygen concentration and alternative terminal-electron-acceptor availability
- carbon-to-nutrient stoichiometry; nitrogen, phosphorus, and trace-metal limitation
- temperature, pH, salinity, light, and redox potential
- growth versus starvation or maintenance state
- substrate-amended growth assay
- substrate disappearance measured by chromatography or mass spectrometry
- respirometry and fermentation-product assays
- `13C`-substrate stable-isotope probing and biomass incorporation
- transcriptomics, proteomics, or metagenomics—supportive but not independently diagnostic

## 3. Recommended core causal chain

The following compact artifact summarizes a defensible generic model. It should be treated as a scaffold with respiration and fermentation represented as alternatives, rather than as one obligatory linear pathway.

| Subject node | Predicate | Object node | Suggested stable CURIE where confidently known | Evidence strength / qualification |
|---|---|---|---|---|
| organic compound | is imported for | organoheterotrophic metabolism | CHEBI:33229; METPO:1000664 | Core trait-defining step; direct support that heterotrophs respire organic compounds to gain energy and build biomass; substrate specificity varies by taxon and transporter repertoire (braun2021reviewsandsyntheses pages 1-2, halloran2024molecularcharacterizationof pages 32-36) |
| organic matter / DOM | provides carbon and energy to | heterotrophic carbon metabolism | label only | Experimental ecosystem support from sponge DOM uptake and marine DOM-consumer studies; broad but not universal for all organoheterotrophs (campana2021dna‐stableisotopeprobing pages 1-2, halloran2024molecularcharacterizationof pages 32-36) |
| glucose / sugars / organic acids | feeds into | glycolysis / EMPP / EDP / PPP | KEGG:map00010; KEGG:map00030; label only for EDP | Strong review-level central-metabolism support in heterotrophs; exact route differs among taxa and niches (theodosiou2022exploitationofhetero pages 1-2) |
| glycolysis / EMPP / EDP / PPP | generates | pyruvate and reducing equivalents | CHEBI:15361; label only for reducing equivalents | Strong review-level support; pathway-level statement appropriate, but specific cofactors and yields are taxon/condition dependent (theodosiou2022exploitationofhetero pages 1-2) |
| pyruvate | is converted to | acetyl-CoA | CHEBI:15361; CHEBI:15351 | Canonical central-metabolism step implied in TCA-linked heterotrophic growth; curate as general mechanism without taxon-specific enzyme unless source added (theodosiou2022exploitationofhetero pages 1-2) |
| acetyl-CoA | enters | tricarboxylic acid cycle | CHEBI:15351; KEGG:map00020 | Strong review-level support for aerobic heterotrophic central metabolism; extent of complete versus branched TCA varies by lineage (theodosiou2022exploitationofhetero pages 1-2) |
| tricarboxylic acid cycle | supplies | biosynthetic precursors and additional reducing equivalents | KEGG:map00020; label only | Strong mechanistic support; useful for linking catabolism to biomass synthesis, but exact precursor set is broad (theodosiou2022exploitationofhetero pages 1-2, braun2021reviewsandsyntheses pages 1-2) |
| NADH / FADH2 / NADPH | donates electrons to | respiratory electron transport chain | CHEBI:16908; CHEBI:37554; CHEBI:16474; GO:0022900 | Strong review-level support; source states reducing equivalents are transferred to O2 via respiratory chain during aerobic growth (theodosiou2022exploitationofhetero pages 1-2) |
| respiratory electron transport chain | transfers electrons to | oxygen | GO:0022900; CHEBI:15379 | Strong for aerobic organoheterotrophy; not universal because some organoheterotrophs use alternative acceptors or ferment (theodosiou2022exploitationofhetero pages 1-2, braun2021reviewsandsyntheses pages 1-2) |
| respiratory electron transport chain | can transfer electrons to | alternative terminal electron acceptors | GO:0022900; label only | Broad review support for nitrate, ferric iron, sulfate as heterotrophic electron acceptors; curate acceptor-specific edges only when separately sourced (braun2021reviewsandsyntheses pages 1-2) |
| electron transport chain | generates | proton motive force | GO:0015986 | Mechanistically standard and supported in respiration-focused literature background, but not explicitly quantified in the retrieved 2023-2024 sources; suitable as medium-confidence general edge (theodosiou2022exploitationofhetero pages 1-2) |
| proton motive force | drives | ATP synthase | GO:0015986; GO:0015986? | Mechanistically canonical for respiration; ontology grounding for ATP synthase complex not established here, so curate cautiously unless additional explicit source is added (theodosiou2022exploitationofhetero pages 1-2) |
| ATP synthesis | supports | biomass production | GO:0006754; GO:0009058 | Strong general physiological inference linking energy generation to growth; supported by CUE literature showing allocation to biomass vs respiration (xu2024activemicrobialpopulation pages 1-2, clara2022phylogeneticallyandfunctionally pages 7-8) |
| imported organic carbon | is incorporated into | biomass | label only; GO:0009058 | Strong experimental support from DNA-SIP and quantitative heterotrophic studies; incorporation fractions vary by substrate and habitat (campana2021dna‐stableisotopeprobing pages 1-2, braun2021reviewsandsyntheses pages 1-2) |
| organoheterotrophic metabolism | can proceed by | fermentation | GO:0006113 | Strong but not universal alternative branch; taxon-specific fermentation products documented in recent marine study, indicating anaerobic or microoxic alternative to respiration (li2024arcobacteraceaeareubiquitous pages 10-12) |
| fermentation | produces | acetate / lactate / ethanol | CHEBI:30089; CHEBI:24996; CHEBI:16236 | Recent metatranscriptomic support exists, but this is taxon-specific to marine Arcobacteraceae/mixotroph context and should be marked uncertain for generic TraitMech use (li2024arcobacteraceaeareubiquitous pages 10-12) |
| heterotrophic central metabolism | includes | anaplerotic CO2 fixation | label only | Important boundary case: heterotrophs can fix CO2 via carboxylases while remaining heterotrophs; contributes ~1–8% of biomass in many microbes and higher in some cases (braun2021reviewsandsyntheses pages 1-2) |
| anaplerotic CO2 fixation | replenishes | TCA cycle intermediates | CHEBI:16526; KEGG:map00020 | Strong review support via pyruvate carboxylase / PEP carboxylase replenishing oxaloacetate and related intermediates; boundary edge, not evidence of autotrophy (braun2021reviewsandsyntheses pages 2-4, braun2021reviewsandsyntheses pages 1-2) |
| organoheterotrophic trait | is distinct from | mixotrophy / lithoautotrophy / photoautotrophy | METPO:1000664; label only | Strong scope/boundary support: organoheterotrophs rely on organic compounds for energy and carbon, whereas other trophic modes add inorganic electron donors, light, or CO2 fixation as primary strategies (eiler2006evidenceforthe pages 1-2, clara2022phylogeneticallyandfunctionally pages 1-2) |


*Table: This table summarizes a concise, curation-oriented causal chain for organoheterotrophy, from organic substrate uptake through central metabolism, respiration or fermentation, and biomass production. It also marks the important boundary case of anaplerotic CO2 fixation, which can occur in heterotrophs without changing the trait to autotrophy.*

## 4. Candidate evidence-backed edges

| Subject | Predicate | Object | Reference and supporting snippet | Curation note |
|---|---|---|---|---|
| organoheterotroph | uses as primary carbon and energy/electron source | organic compounds | Braun et al.: heterotrophs “respire organic compounds to gain energy and build up biomass” (braun2021reviewsandsyntheses pages 1-2) | **Core, strong.** Closest source-backed expression of the defining edge. |
| organic compound | is taken up and supports | growth/biomass | Halloran 2024: branched-chain amino acids and 3-methyl-2-oxobutanoate supported *Alteromonas* growth; cells increased 94-fold while the latter metabolite declined eightfold in 60 h (halloran2024molecularcharacterizationof pages 32-36) | **Experimental but taxon/substrate-specific.** Supports a generic uptake→growth relationship, not a universal transporter. |
| transporter specificity | determines | utilizable organic-substrate range | Halloran 2024 found utilization of the valine precursor but not structurally similar leucine/isoleucine precursors, consistent with selective uptake (halloran2024molecularcharacterizationof pages 32-36, halloran2024molecularcharacterizationof pages 40-43) | **Recent, experimental, taxon-specific.** Prefer an optional substrate-range branch. |
| dissolved organic matter | is incorporated into | microbial DNA/biomass | DNA-SIP identified seven bacterial ASVs as active DOM consumers after `13C`-DOM amendment (campana2021dna‐stableisotopeprobing pages 1-2) | **Strong assay evidence**, but sponge-holobiont and community-specific. |
| complex organic carbon | is degraded by | aerobic organoheterotrophic bacteria | Ross Ice Shelf study: “enriched were aerobic organoheterotrophic bacteria capable of degrading complex organic carbon substrates” (clara2022phylogeneticallyandfunctionally pages 1-2) | **Strong ecological multi-omics inference.** Exact enzymes/substrates require taxon-level evidence. |
| polysaccharides | are degraded by | carbohydrate-active enzymes | Ross Ice Shelf organisms transcribed enzymes targeting alginate, rhamnose, and xylan (clara2022phylogeneticallyandfunctionally pages 7-8) | **Habitat-specific.** Suitable examples, not universal core substrates. |
| sugars/organic acids | feed | central carbon metabolism | Review: heterotrophic central metabolism uses simple organic molecules and includes EMP, ED, PPP, and TCA pathways (theodosiou2022exploitationofhetero pages 1-2) | **Strong module-level edge.** Encode pathways as alternatives because not every lineage has all routes. |
| central carbon metabolism | generates | carbon building blocks, reducing power, and energy | Review explicitly states that heterotrophic central metabolism provides “carbon building blocks as well as redox power and energy” (theodosiou2022exploitationofhetero pages 1-2) | **Core, strong.** Appropriate abstraction above individual reactions. |
| glucose oxidation | generates | NADH/NADPH/FADH2 reducing equivalents | Under aerobic growth, complete glucose oxidation theoretically yields up to 24 reducing equivalents in 12 reduced cofactors (theodosiou2022exploitationofhetero pages 1-2) | **Mechanistically strong but conditional.** The maximum assumes complete aerobic oxidation and should not be encoded as a universal numeric edge. |
| reduced cofactors | donate electrons through | respiratory electron-transport chain | Review: reducing equivalents are transferred to O2 through the respiratory chain, generating most metabolic energy (theodosiou2022exploitationofhetero pages 1-2) | **Core for aerobic respiratory branch only.** |
| oxygen | serves as | terminal electron acceptor | Same aerobic heterotrophic mechanism (theodosiou2022exploitationofhetero pages 1-2) | **Conditional.** Do not make oxygen obligatory for `METPO:1000664`. |
| nitrate/ferric iron/sulfate | can serve as | alternative electron acceptor | Braun et al. describe organic-substrate oxidation using oxygen or “alternative electron acceptors (e.g. nitrate, ferric iron, sulfate)” (braun2021reviewsandsyntheses pages 1-2) | **Broad review support.** Curate each acceptor-specific branch only with organism/pathway evidence. |
| electron transport | supports | ATP synthesis/energy conservation | Aerobic respiratory transfer generates the majority of metabolic energy (theodosiou2022exploitationofhetero pages 1-2) | **Strong at process level.** Add explicit proton-motive-force and ATP-synthase edges only with a dedicated bioenergetics citation or retain as inferred. |
| organic carbon uptake | partitions into | biomass production and respiration | CUE is defined as growth relative to uptake, where uptake equals growth plus respiration (xu2024activemicrobialpopulation pages 1-2) | **Core ecological allocation concept.** CUE itself is assay- and condition-dependent. |
| organic fertilization/high organic matter | increases | biomass-directed carbon allocation | A 35-year fertilization study found organic-rich soils had higher CUE, faster net growth, and anabolic-biased carbon cycling, allocating more carbon to biomass rather than respiration (xu2024activemicrobialpopulation pages 1-2) | **2024 field-derived community evidence.** Do not generalize direction to every ecosystem. |
| organoheterotrophic metabolism | can proceed through | fermentation | Global metatranscriptomes detected Arcobacteraceae ethanol-, acetate-, and lactate-production pathways at >98% of 187 Tara Ocean sites (li2024arcobacteraceaeareubiquitous pages 10-12) | **Recent but taxon-specific and mixotrophic.** Valid optional branch; not a generic universal product edge. |
| heterotrophic carboxylases | fix | inorganic carbon | More than 20 carboxylases participate in heterotrophic central/peripheral metabolism (braun2021reviewsandsyntheses pages 1-2) | **Boundary edge.** This does not imply autotrophy. |
| PEP/pyruvate carboxylation | replenishes | TCA intermediates | Review identifies pyruvate/PEP carboxylation and anaplerosis; *B. subtilis* biomass contained 6%, 5%, and 3% external inorganic carbon when growing on glucose, lactate, and malate, respectively (braun2021reviewsandsyntheses pages 1-2) | **Strong but auxiliary.** Include as optional co-substrate/anaplerotic branch. |
| organic-carbon limitation | constrains | organoheterotrophic production | Under the Ross Ice Shelf, growth efficiency was approximately 5% and estimated organic-C demand was 6–12 µmol C m⁻³ d⁻¹ in an oligotrophic system (clara2022phylogeneticallyandfunctionally pages 7-8) | **Quantitative ecosystem-specific edge.** Useful environmental modifier, not universal parameter. |
| heterotrophic metabolism | regenerates | redox cofactors for biocatalysis | Whole-cell review emphasizes engineering NAD(P)H supply, blocking competing fluxes, and increasing biosynthetic co-substrates (theodosiou2022exploitationofhetero pages 1-2) | **Application-level edge**, not a natural-trait requirement. |
| heterotrophic cultivation | produces | ectoine/PHB/propane | *Halomonas rowanensis* produced ectoine, poly-3-hydroxybutyrate, and recombinant bio-propane under heterotrophic conditions (faulkner2023chemoautotrophicproductionof pages 1-2) | **2023 proof of concept, strain-specific.** Keep outside the core trait graph or as an application extension. |

## 5. Recent developments and applications

### 2023–2024 research

1. **Compound-resolved DOM utilization.** Halloran’s 2024 experimental work shows that structurally similar metabolites can have sharply different biological fates. In *Alteromonas macleodii*, a valine intermediate supported a 94-fold cell increase and fell eightfold over 60 h, whereas cognate branched-chain precursors were not consumed. This argues against representing “DOM uptake” as nonspecific and supports transporter- or substrate-class branches in organism-specific graphs (halloran2024molecularcharacterizationof pages 32-36, halloran2024molecularcharacterizationof pages 40-43).

2. **Carbon-use efficiency and soil sequestration.** Xu et al., published 20 February 2024, used H2¹⁸O quantitative SIP and metagenomics in soils under 35 years of fertilization. Organic-rich treatments selected more diverse, faster-growing, anabolic-biased active communities and shifted carbon toward biomass rather than respiration. The authors note that microbial necromass may constitute up to 80% of soil organic carbon, although that percentage derives from prior model literature rather than the experiment itself (xu2024activemicrobialpopulation pages 1-2).

3. **Global evidence for flexible trophic modes.** A July 2024 Arcobacteraceae study analyzed metatranscriptomes from 187 Tara Oceans sites and detected expression of fermentation pathways at more than 98% of sites. Because these organisms are mixotrophs, the result supports a widespread optional organoheterotrophic branch but not a universal definition of the family or trait (li2024arcobacteraceaeareubiquitous pages 10-12).

4. **Industrial chassis development.** In October 2023, *Halomonas rowanensis* was demonstrated as a facultative trophic chassis producing ectoine, PHB, and engineered propane under heterotrophic conditions and fixing CO2 with thiosulfate under chemoautotrophic conditions. Related *Halomonas* production systems had reportedly operated at >1,000-tonne scale for over three years and achieved an approximately 65% pilot-process cost saving relative to an *E. coli* host; these scale/cost data concern the related *H. bluephagenesis*, not the newly isolated strain (faulkner2023chemoautotrophicproductionof pages 1-2).

### Current real-world implementations

- **Wastewater treatment:** heterotrophic denitrification uses organic carbon as electron donor and biomass carbon, but it is an application-specific respiratory branch rather than a defining universal pathway.
- **Biomanufacturing:** sugars, organic acids, glycerol, and waste-derived feedstocks fuel biomass, cofactor regeneration, and synthesis of fuels, bioplastics, osmolytes, and fine chemicals. Heterotrophic hosts remain attractive because of high growth rates, well-developed engineering tools, active metabolism, and high-cell-density cultivation (theodosiou2022exploitationofhetero pages 1-2, faulkner2023chemoautotrophicproductionof pages 1-2).
- **Bioremediation:** organoheterotrophic respiration can couple oxidation of hydrocarbons or other organic contaminants to oxygen, nitrate, iron(III), sulfate, or other acceptors. Such substrate/acceptor edges must be curated from organism-specific physiological studies.
- **Carbon-cycle assessment:** isotope probing, CUE measurements, and compound-specific metabolomics now resolve whether organic carbon is incorporated into biomass or respired. DNA-SIP directly linked DOM-derived carbon to seven sponge-associated bacterial ASVs (campana2021dna‐stableisotopeprobing pages 1-2).

## 6. Expert interpretation for TraitMech

The most defensible graph is a **small phenotype-level spine plus alternative mechanistic branches**:

1. organic compound availability → uptake/depolymerization;
2. uptake → intracellular organic carbon;
3. intracellular organic carbon → central carbon metabolism;
4. central metabolism → carbon skeletons → biomass;
5. central metabolism → reduced cofactors;
6. reduced cofactors → either respiratory electron transport → energy conservation, or fermentation → substrate-level energy/redox balancing;
7. respiration → oxygen **or** alternative electron acceptor;
8. optional anaplerotic CO2 fixation → replenished biosynthetic intermediates.

This structure captures the trait without falsely requiring glucose, one transporter, a complete oxidative TCA cycle, oxygen, or a particular respiratory complex. The literature also supports modeling **substrate availability, electron-acceptor availability, nutrient limitation, and carbon-use efficiency as contextual modifiers**, not definitional nodes (clara2022phylogeneticallyandfunctionally pages 7-8, xu2024activemicrobialpopulation pages 1-2, theodosiou2022exploitationofhetero pages 1-2).

## 7. Warnings: claims not yet ready for curation

1. **Do not infer the trait from pathway annotations alone.** Glycolysis, TCA, transporter, or respiratory genes can occur in autotrophs and mixotrophs; expression is stronger than presence but still may not establish the primary carbon/energy source (burgsdorf2021rethinkingsymbioticmetabolism pages 1-4).
2. **Do not make oxygen obligatory.** Anaerobic respiration and fermentation are legitimate organoheterotrophic modes (braun2021reviewsandsyntheses pages 1-2).
3. **Do not require all central-carbon pathways.** EMP, ED, PPP, complete/branched TCA cycles, and glyoxylate shunts vary by lineage and condition (theodosiou2022exploitationofhetero pages 1-2).
4. **Do not treat all DOM as bioavailable.** Approximately 75–90% of marine DOM may be refractory, and compound-specific transporter/metabolic compatibility strongly controls uptake (campana2021dna‐stableisotopeprobing pages 1-2, halloran2024molecularcharacterizationof pages 32-36).
5. **Do not interpret anaplerotic CO2 fixation as autotrophy.** It commonly contributes 1–8% of heterotrophic biomass and can be higher in specialist metabolisms (braun2021reviewsandsyntheses pages 2-4, braun2021reviewsandsyntheses pages 1-2).
6. **Do not generalize taxon-specific products.** Acetate, lactate, ethanol, PHB, ectoine, and propane are optional products or engineered outputs, not components of the generic trait (li2024arcobacteraceaeareubiquitous pages 10-12, faulkner2023chemoautotrophicproductionof pages 1-2).
7. **Do not use UniProt or EC identifiers without specifying the actual protein/reaction.** Orthologous alternatives and non-homologous replacements are common.
8. **Validate ontology mappings before commit.** In particular, DOM, carbon-use efficiency, proton motive force, ATP synthase complexes, Entner–Doudoroff metabolism, and generic transport/depolymerization may need label-only nodes or more precise ontology review.
9. **Treat the 2021 sponge-metabolism preprint cautiously.** Its quantitative and transcript-correlation claims are useful hypothesis support, but should not outrank peer-reviewed physiological evidence (burgsdorf2021rethinkingsymbioticmetabolism pages 13-16).
10. **The existing 12-node/12-edge graph should not be expanded merely to enumerate every possible substrate or acceptor.** Add branches only when they improve the generic mechanism or are explicitly labeled taxon/assay-specific.

## 8. DOI-first bibliography

- Xu Q. et al. **Active microbial population dynamics and life strategies drive the enhanced carbon use efficiency in high-organic matter soils.** *mBio* 15, 2024. Published 20 February 2024. DOI: [10.1128/mbio.00177-24](https://doi.org/10.1128/mbio.00177-24) (xu2024activemicrobialpopulation pages 1-2).
- Li J. et al. **Arcobacteraceae are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans.** *mSystems* 9, July 2024. DOI: [10.1128/msystems.00513-24](https://doi.org/10.1128/msystems.00513-24) (li2024arcobacteraceaeareubiquitous pages 10-12).
- Halloran K.H. **Molecular characterization of microbial interactions with labile dissolved organic matter.** WHOI dissertation, 2024. DOI: [10.1575/1912/69776](https://doi.org/10.1575/1912/69776) (halloran2024molecularcharacterizationof pages 32-36).
- Faulkner M. et al. **Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel Halomonas species.** *Biotechnology for Biofuels and Bioproducts* 16:152, October 2023. DOI: [10.1186/s13068-023-02404-1](https://doi.org/10.1186/s13068-023-02404-1) (faulkner2023chemoautotrophicproductionof pages 1-2).
- Martínez-Pérez C. et al. **Phylogenetically and functionally diverse microorganisms reside under the Ross Ice Shelf.** *Nature Communications* 13:117, January 2022. DOI: [10.1038/s41467-021-27769-5](https://doi.org/10.1038/s41467-021-27769-5) (clara2022phylogeneticallyandfunctionally pages 7-8, clara2022phylogeneticallyandfunctionally pages 1-2).
- Theodosiou E. et al. **Exploitation of hetero- and phototrophic metabolic modules for redox-intensive whole-cell biocatalysis.** *Frontiers in Bioengineering and Biotechnology* 10, published 13 April 2022. DOI: [10.3389/fbioe.2022.855715](https://doi.org/10.3389/fbioe.2022.855715) (theodosiou2022exploitationofhetero pages 1-2).
- Campana S. et al. **DNA-stable isotope probing identifies marine sponge-associated bacteria actively utilizing dissolved organic matter.** *Environmental Microbiology* 23:4489–4504, 2021. DOI: [10.1111/1462-2920.15642](https://doi.org/10.1111/1462-2920.15642) (campana2021dna‐stableisotopeprobing pages 1-2).
- Braun A. et al. **Heterotrophic fixation of inorganic carbon—significant but invisible flux in environmental carbon cycling.** *Biogeosciences* 18:3689–3700, published 21 June 2021. DOI: [10.5194/bg-18-3689-2021](https://doi.org/10.5194/bg-18-3689-2021) (braun2021reviewsandsyntheses pages 2-4, braun2021reviewsandsyntheses pages 1-2).
- Marella T.K. et al. **Impact of organic carbon acquisition on growth and functional biomolecule production in diatoms.** *Microbial Cell Factories* 20, July 2021. DOI: [10.1186/s12934-021-01627-x](https://doi.org/10.1186/s12934-021-01627-x) (marella2021impactoforganic pages 6-8, marella2021impactoforganic pages 1-2).
- Eiler A. **Evidence for the ubiquity of mixotrophic bacteria in the upper ocean: implications and consequences.** *Applied and Environmental Microbiology* 72:7431–7437, December 2006. DOI: [10.1128/AEM.01559-06](https://doi.org/10.1128/AEM.01559-06) (eiler2006evidenceforthe pages 1-2).
- Burgsdorf I. et al. **Rethinking symbiotic metabolism: trophic strategies in the microbiomes of different sponge species.** bioRxiv preprint, August 2021. DOI: [10.1101/2021.08.28.458021](https://doi.org/10.1101/2021.08.28.458021) (burgsdorf2021rethinkingsymbioticmetabolism pages 1-4, burgsdorf2021rethinkingsymbioticmetabolism pages 13-16).

References

1. (braun2021reviewsandsyntheses pages 1-2): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.

2. (braun2021reviewsandsyntheses pages 2-4): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.

3. (eiler2006evidenceforthe pages 1-2): Alexander Eiler. Evidence for the ubiquity of mixotrophic bacteria in the upper ocean: implications and consequences. Dec 2006. URL: https://doi.org/10.1128/aem.01559-06, doi:10.1128/aem.01559-06. This article has 196 citations and is from a peer-reviewed journal.

4. (burgsdorf2021rethinkingsymbioticmetabolism pages 1-4): I. Burgsdorf, S. Sizikov, V. Squatrito, M. Britstein, BM Slaby, C. Cerrano, K. Handley, and L. Steindler. Rethinking symbiotic metabolism: trophic strategies in the microbiomes of different sponge species. bioRxiv, Aug 2021. URL: https://doi.org/10.1101/2021.08.28.458021, doi:10.1101/2021.08.28.458021. This article has 2 citations.

5. (braun2021reviewsandsyntheses pages 4-5): Alexander Braun, Marina Spona-Friedl, Maria Avramov, Martin Elsner, Federico Baltar, Thomas Reinthaler, Gerhard J. Herndl, and Christian Griebler. Reviews and syntheses: heterotrophic fixation of inorganic carbon – significant but invisible flux in environmental carbon cycling. Biogeosciences, 18:3689-3700, Jun 2021. URL: https://doi.org/10.5194/bg-18-3689-2021, doi:10.5194/bg-18-3689-2021. This article has 104 citations and is from a domain leading peer-reviewed journal.

6. (campana2021dna‐stableisotopeprobing pages 1-2): Sara Campana, Kathrin Busch, Ute Hentschel, Gerard Muyzer, and Jasper M. de Goeij. Dna‐stable isotope probing (dna‐sip) identifies marine sponge‐associated bacteria actively utilizing dissolved organic matter (dom). Environmental Microbiology, 23:4489-4504, Jun 2021. URL: https://doi.org/10.1111/1462-2920.15642, doi:10.1111/1462-2920.15642. This article has 45 citations and is from a domain leading peer-reviewed journal.

7. (halloran2024molecularcharacterizationof pages 32-36): Kathryn H. Halloran. Molecular characterization of microbial interactions with labile dissolved organic matter. ArXiv, 2024. URL: https://doi.org/10.1575/1912/69776, doi:10.1575/1912/69776. This article has 0 citations.

8. (theodosiou2022exploitationofhetero pages 1-2): Eleni Theodosiou, Adrian Tüllinghoff, Jörg Toepel, and Bruno Bühler. Exploitation of hetero- and phototrophic metabolic modules for redox-intensive whole-cell biocatalysis. Frontiers in Bioengineering and Biotechnology, Apr 2022. URL: https://doi.org/10.3389/fbioe.2022.855715, doi:10.3389/fbioe.2022.855715. This article has 16 citations.

9. (xu2024activemicrobialpopulation pages 1-2): Qicheng Xu, Ling Li, Junjie Guo, Hanyue Guo, Manqiang Liu, Shiwei Guo, Yakov Kuzyakov, Ning Ling, and Qirong Shen. Active microbial population dynamics and life strategies drive the enhanced carbon use efficiency in high-organic matter soils. Mar 2024. URL: https://doi.org/10.1128/mbio.00177-24, doi:10.1128/mbio.00177-24. This article has 54 citations and is from a domain leading peer-reviewed journal.

10. (clara2022phylogeneticallyandfunctionally pages 7-8): Clara Martínez-Pérez, Chris Greening, Sean K. Bay, Rachael J. Lappan, Zhiao Zhao, Daniele De Corte, Christina Hulbe, Christian Ohneiser, Craig Stevens, Blair Thomson, Ramunas Stepanauskas, José M. González, Ramiro Logares, Sergio E. Morales, and Federico Baltar. Phylogenetically and functionally diverse microorganisms reside under the ross ice shelf. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-021-27769-5, doi:10.1038/s41467-021-27769-5. This article has 61 citations and is from a highest quality peer-reviewed journal.

11. (li2024arcobacteraceaeareubiquitous pages 10-12): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 39 citations and is from a peer-reviewed journal.

12. (clara2022phylogeneticallyandfunctionally pages 1-2): Clara Martínez-Pérez, Chris Greening, Sean K. Bay, Rachael J. Lappan, Zhiao Zhao, Daniele De Corte, Christina Hulbe, Christian Ohneiser, Craig Stevens, Blair Thomson, Ramunas Stepanauskas, José M. González, Ramiro Logares, Sergio E. Morales, and Federico Baltar. Phylogenetically and functionally diverse microorganisms reside under the ross ice shelf. Nature Communications, Jan 2022. URL: https://doi.org/10.1038/s41467-021-27769-5, doi:10.1038/s41467-021-27769-5. This article has 61 citations and is from a highest quality peer-reviewed journal.

13. (halloran2024molecularcharacterizationof pages 40-43): Kathryn H. Halloran. Molecular characterization of microbial interactions with labile dissolved organic matter. ArXiv, 2024. URL: https://doi.org/10.1575/1912/69776, doi:10.1575/1912/69776. This article has 0 citations.

14. (faulkner2023chemoautotrophicproductionof pages 1-2): Matthew Faulkner, Robin Hoeven, Paul P. Kelly, Yaqi Sun, Helen Park, Lu-Ning Liu, Helen S. Toogood, and Nigel S. Scrutton. Chemoautotrophic production of gaseous hydrocarbons, bioplastics and osmolytes by a novel halomonas species. Biotechnology for Biofuels and Bioproducts, Oct 2023. URL: https://doi.org/10.1186/s13068-023-02404-1, doi:10.1186/s13068-023-02404-1. This article has 8 citations and is from a domain leading peer-reviewed journal.

15. (burgsdorf2021rethinkingsymbioticmetabolism pages 13-16): I. Burgsdorf, S. Sizikov, V. Squatrito, M. Britstein, BM Slaby, C. Cerrano, K. Handley, and L. Steindler. Rethinking symbiotic metabolism: trophic strategies in the microbiomes of different sponge species. bioRxiv, Aug 2021. URL: https://doi.org/10.1101/2021.08.28.458021, doi:10.1101/2021.08.28.458021. This article has 2 citations.

16. (marella2021impactoforganic pages 6-8): Thomas Kiran Marella, Raya Bhattacharjya, and Archana Tiwari. Impact of organic carbon acquisition on growth and functional biomolecule production in diatoms. Microbial Cell Factories, Jul 2021. URL: https://doi.org/10.1186/s12934-021-01627-x, doi:10.1186/s12934-021-01627-x. This article has 84 citations and is from a peer-reviewed journal.

17. (marella2021impactoforganic pages 1-2): Thomas Kiran Marella, Raya Bhattacharjya, and Archana Tiwari. Impact of organic carbon acquisition on growth and functional biomolecule production in diatoms. Microbial Cell Factories, Jul 2021. URL: https://doi.org/10.1186/s12934-021-01627-x, doi:10.1186/s12934-021-01627-x. This article has 84 citations and is from a peer-reviewed journal.