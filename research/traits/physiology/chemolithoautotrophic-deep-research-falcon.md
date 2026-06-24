---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:53:01.945898'
end_time: '2026-06-18T11:10:28.049943'
duration_seconds: 1046.1
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemolithoautotrophic
  trait_identifier: METPO:1000637
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemolithoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from oxidation of
    inorganic compounds (lithotrophy) and carbon from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: chemolithoautotroph
  evidence_summary: 'DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic
    bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X:
    growth-supporting reductant and energy source (Review supports inorganic reductants
    as energy sources for chemolithotrophic growth.)'
  causal_graph_summary: 'chemolithoautotrophic_energy_and_fixation: 9 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemolithoautotrophic
- **METPO identifier:** METPO:1000637
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds (lithotrophy) and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X: growth-supporting reductant and energy source (Review supports inorganic reductants as energy sources for chemolithotrophic growth.)
- **Existing causal graph summary:** chemolithoautotrophic_energy_and_fixation: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **chemolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoautotrophic.yaml`.

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
- **Trait label:** chemolithoautotrophic
- **METPO identifier:** METPO:1000637
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds (lithotrophy) and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemolithoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: physiology ... of chemoautotrophic bacteria (Review supports chemoautotrophic bacterial CO2 fixation.) | DOI:10.1016/B978-0-12-378630-2.00219-X: growth-supporting reductant and energy source (Review supports inorganic reductants as energy sources for chemolithotrophic growth.)
- **Existing causal graph summary:** chemolithoautotrophic_energy_and_fixation: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **chemolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemolithoautotrophic.yaml`.

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


# Research Report: Chemolithoautotrophic (METPO:1000637) — TraitMech Causal Graph Curation

## 1) Scope summary (trait meaning and boundaries)

**Definition (current understanding).** Chemolithoautotrophy denotes organisms that **fix CO2 (or DIC) into biomass** while obtaining **energy and/or reducing power from oxidation of reduced inorganic compounds** (e.g., H2, reduced sulfur, Fe(II), ammonia). Recent work on vent fluids explicitly frames chemolithoautotrophs as microbes that “convert CO2 to organic carbon using energy from oxidizing reduced inorganic compounds” (10.1186/s40168-023-01712-w; published 2023-12; https://doi.org/10.1186/s40168-023-01712-w) (deng2023strategiesofchemolithoautotrophs pages 1-2). Studies of vent **Hydrogenovibrio** similarly operationalize the trait as **oxidation of inorganic electron donors coupled to autotrophic CO2 fixation** (10.1093/ismejo/wrae173; published 2024-01; https://doi.org/10.1093/ismejo/wrae173) (laufermeiser2024oxidationofsulfur pages 1-2).

**Distinguishing from nearby traits.**
- **Chemolithotrophic vs chemolithoautotrophic:** chemolithotrophy concerns energy from inorganic electron donors; chemolithoautotrophy adds **CO2 fixation as the major carbon source**. Engineering/biomanufacturing reviews emphasize that chemolithotrophs extract “high-energy electrons from inorganic compounds to regenerate reducing powers (NAD(P)H… ferredoxin…)” that can support CO2 fixation (10.3390/bioengineering10121357; published 2023-11; https://doi.org/10.3390/bioengineering10121357) (kurt2023perspectivesforusing pages 9-11).
- **Chemoautotrophic vs phototrophic autotrophy:** photoautotrophs use light-driven photosystems, while chemoautotrophs use chemical redox reactions; this contrast is explicit in engineering context (10.3390/bioengineering10121357; published 2023-11; https://doi.org/10.3390/bioengineering10121357) (kurt2023perspectivesforusing pages 9-11).

**Boundary cases to curate carefully.**
- **Facultative chemolithoautotrophy:** some organisms switch between heterotrophy and chemolithoautotrophy depending on substrates. Ralstonia eutropha (Cupriavidus necator) is described as a **“facultatively chemolithoautotrophic”** chassis used for engineered electrode/light-driven CO2 fixation (10.1038/s41467-023-43524-4; published 2023-12; https://doi.org/10.1038/s41467-023-43524-4) (tu2023engineeringartificialphotosynthesis pages 1-2).
- **Mixotrophy (autotrophy + organic uptake):** marine Arcobacteraceae are described as “mixotrophic” with genes for both inorganic-energy metabolisms and organic matter use; the CO2 fixation module in some is rTCA, but many show substantial heterotrophic capacity (10.1128/msystems.00513-24; published 2024-07; https://doi.org/10.1128/msystems.00513-24) (li2024arcobacteraceaeareubiquitous pages 10-12). In a blue-hole system, many WL-pathway taxa are described as **mixotrophic**, and some genomes encode **two CO2 fixation pathways (WL + CBB)**, implying conditional pathway use rather than obligate chemolithoautotrophy (10.1038/s43705-023-00327-4; published 2023-11; https://doi.org/10.1038/s43705-023-00327-4) (chen2023phylogeneticallyandmetabolically pages 10-11).

**Practical trait interpretation for TraitMech.** For curation, METPO:1000637 should be treated as a **physiological capacity**: growth/biomass synthesis from CO2 when supplied with inorganic electron donor(s) and appropriate terminal acceptor(s) (or engineered electron supply), with the understanding that many taxa are **facultative or mixotrophic** and trait expression is environment-dependent (chen2023phylogeneticallyandmetabolically pages 10-11, tu2023engineeringartificialphotosynthesis pages 1-2).

## 2) Key mechanistic entities (candidate nodes)

Two curation-focused node inventories are provided below.

| Group | Candidate node | Type | Role in chemolithoautotrophy | Suggested grounding | Example gene symbols / markers | Evidence source(s) |
|---|---|---|---|---|---|---|
| A. CO2 fixation pathways/modules | Calvin–Benson–Bassham cycle | pathway | CO2 fixation module used by many bacterial chemolithoautotrophs | GO:0015977 | rbcL, rbcS, prkA | (laufermeiser2024oxidationofsulfur pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8) |
| A. CO2 fixation pathways/modules | reverse tricarboxylic acid cycle | pathway | Reduced-carbon assimilation pathway in vent and nitrifying taxa | GO:0019624 | aclAB, oorABCD, PFOR, OGOR | (wang2024novelisolatesof pages 12-15, prioretti2023carbonfixationin pages 1-2, li2024arcobacteraceaeareubiquitous pages 10-12) |
| A. CO2 fixation pathways/modules | Wood–Ljungdahl pathway | pathway | Low-energy CO2 fixation / acetyl-CoA pathway, especially in anoxic settings | label-only | codh, acs, fdh | (atencio2024metabolicadaptationsunderpin pages 1-2, wang2023microbialconversionand pages 3-5) |
| A. CO2 fixation pathways/modules | 3-hydroxypropionate/4-hydroxybutyrate cycle | pathway | Archaeal CO2 fixation pathway in ammonia oxidizers | label-only | pathway-level markers only in evidence | (deng2023strategiesofchemolithoautotrophs pages 1-2, cornell2024genomeencodedmetabolicpotential pages 15-18) |
| A. CO2 fixation pathways/modules | dicarboxylate/4-hydroxybutyrate cycle | pathway | Alternative archaeal autotrophic carbon fixation pathway; boundary/nearby trait context | label-only | pathway-level markers only in evidence | (scott2024widespreaddissolvedinorganic pages 1-2, kurt2023perspectivesforusing pages 6-8) |
| A. CO2 fixation pathways/modules | partial Wood–Ljungdahl pathway for serine/glycine synthesis | pathway/module | Possible auxiliary CO2 assimilation module rather than core trait-defining pathway | label-only | glycine cleavage system-associated enzymes | (prioretti2023carbonfixationin pages 1-2) |
| B. Inorganic electron donors | molecular hydrogen | chemical | Major inorganic electron donor for hydrogenotrophic chemolithoautotrophy | CHEBI:18276 | hydrogenases | (laufermeiser2024oxidationofsulfur pages 1-2, deng2023strategiesofchemolithoautotrophs pages 1-2, wang2024novelisolatesof pages 12-15) |
| B. Inorganic electron donors | thiosulfate | chemical | Sulfur electron donor coupled to autotrophic growth and CO2 fixation | CHEBI:30087 | sox genes | (laufermeiser2024oxidationofsulfur pages 1-2, wang2024novelisolatesof pages 12-15, alvarez‐guzman2023effectofelectron pages 1-2) |
| B. Inorganic electron donors | sulfide | chemical | Reduced sulfur donor supporting sulfur-based chemolithoautotrophy | CHEBI:16134 | sulfur oxidation genes | (deng2023strategiesofchemolithoautotrophs pages 1-2, li2024arcobacteraceaeareubiquitous pages 10-12, alvarez‐guzman2023effectofelectron pages 1-2) |
| B. Inorganic electron donors | elemental sulfur | chemical | Reduced sulfur donor in sulfur-oxidizing chemolithoautotrophs | CHEBI:26833 | sulfur oxidation genes | (laufermeiser2024oxidationofsulfur pages 1-2) |
| B. Inorganic electron donors | polysulfide | chemical | Sulfur donor used by some sulfur oxidizers | label-only | sulfur oxidation genes | (laufermeiser2024oxidationofsulfur pages 1-2) |
| B. Inorganic electron donors | ferrous iron [Fe(II)] | chemical | Inorganic donor supporting iron-oxidizing autotrophy | CHEBI:29033 | unknown iron oxidation genes; iron acquisition transcripts | (laufermeiser2024oxidationofsulfur pages 1-2) |
| B. Inorganic electron donors | ammonia / ammonium | chemical | Electron donor for nitrifying chemolithoautotrophs | CHEBI:16134 / CHEBI:28938 | amo genes | (cornell2024genomeencodedmetabolicpotential pages 15-18, bayer2024contributionofammonia pages 1-4) |
| B. Inorganic electron donors | nitrite | chemical | Donor in nitrite oxidation coupled to dark carbon fixation estimates | CHEBI:16301 | nitrite oxidizer markers not detailed here | (bayer2024contributionofammonia pages 9-11) |
| B. Inorganic electron donors | phosphite | chemical | Specialized inorganic donor in some chemolithotrophic systems | CHEBI:19042 | phosphite dehydrogenase | (kurt2023perspectivesforusing pages 9-11) |
| B. Inorganic electron donors | electrode-derived electrons | experimental input | Engineered/assay donor enabling facultative chemolithoautotrophic CO2 fixation | label-only | MtrCAB-dependent uptake | (tu2023engineeringartificialphotosynthesis pages 1-2) |
| C. Electron acceptors/terminal processes | oxygen | chemical | Common terminal electron acceptor in aerobic and microaerophilic chemolithoautotrophy | CHEBI:15379 | cytochrome bd ubiquinol oxidase | (deng2023strategiesofchemolithoautotrophs pages 1-2, laufermeiser2024oxidationofsulfur pages 1-2) |
| C. Electron acceptors/terminal processes | nitrate | chemical | Alternative terminal electron acceptor; supports denitrification-linked autotrophy | CHEBI:17632 | napC, nitrate reductase | (wang2024novelisolatesof pages 12-15, li2024arcobacteraceaeareubiquitous pages 10-12) |
| C. Electron acceptors/terminal processes | nitrite reduction | biological process | Terminal process linked to nitrogen-coupled chemolithoautotrophy | GO:0019330 | cytochrome c nitrite reductase | (wang2024novelisolatesof pages 12-15, li2024arcobacteraceaeareubiquitous pages 10-12) |
| C. Electron acceptors/terminal processes | denitrification | biological process | Terminal respiratory process coupled to sulfur oxidation in some taxa | GO:0019646 | nos and related markers in cited taxa | (li2024arcobacteraceaeareubiquitous pages 10-12, wang2024novelisolatesof pages 12-15) |
| C. Electron acceptors/terminal processes | DNRA / dissimilatory nitrate reduction to ammonium | biological process | Nitrogen-coupled terminal process found with sulfur/hydrogen oxidation | GO:0042128 | DNRA markers not fully enumerated | (li2024arcobacteraceaeareubiquitous pages 10-12) |
| D. Energy conservation complexes/electron carriers | Sox sulfur oxidation system | complex/module | Oxidizes reduced sulfur compounds to conserve energy for autotrophy | label-only | soxABCDYZ | (wang2024novelisolatesof pages 12-15) |
| D. Energy conservation complexes/electron carriers | [NiFe]-hydrogenases | enzyme family | Catalyze H2 oxidation for energy/reductant generation | label-only | subgroup 1a, 1b, 2d, 4a, 4c, 4e, 4f | (wang2024novelisolatesof pages 12-15) |
| D. Energy conservation complexes/electron carriers | subgroup 2d cytosolic H2-uptake hydrogenase | enzyme/complex | Supplies reductant directly to support rTCA carbon fixation | label-only | subgroup 2d hydrogenase | (wang2024novelisolatesof pages 12-15) |
| D. Energy conservation complexes/electron carriers | proton-pumping NADH:ubiquinone oxidoreductase | complex | Supports proton export / respiratory energy conservation under acidic conditions | GO:0008137 | nuo-like membrane arm subunits | (deng2023strategiesofchemolithoautotrophs pages 1-2, tu2023engineeringartificialphotosynthesis pages 1-2) |
| D. Energy conservation complexes/electron carriers | cytochrome bd ubiquinol oxidase | complex | Oxygen respiration under vent conditions; supports chemolithoautotrophic energy metabolism | label-only | cydAB-like | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| D. Energy conservation complexes/electron carriers | ATP synthase | complex | Uses proton motive force to produce ATP for CO2 fixation | GO:0015986 | atp operon | (tu2023engineeringartificialphotosynthesis pages 1-2) |
| D. Energy conservation complexes/electron carriers | proton motive force | physiological process | Couples electron transfer or rhodopsin activity to ATP generation | GO:0015992 | n/a | (tu2023engineeringartificialphotosynthesis pages 1-2) |
| D. Energy conservation complexes/electron carriers | quinone pool / menaquinol | electron carrier | Electron carrier regenerated by sulfur oxidation and related processes | CHEBI:58046 | n/a | (kurt2023perspectivesforusing pages 9-11) |
| D. Energy conservation complexes/electron carriers | NADH / NADPH | electron carrier | Reducing equivalents required for CO2 fixation | CHEBI:57945 / CHEBI:57783 | n/a | (tu2023engineeringartificialphotosynthesis pages 1-2, kurt2023perspectivesforusing pages 9-11) |
| D. Energy conservation complexes/electron carriers | reduced ferredoxin | electron carrier | Low-potential reductant for rTCA enzymes and other carboxylation reactions | CHEBI:60524 | Fd6, Fd7 | (prioretti2023carbonfixationin pages 1-2) |
| D. Energy conservation complexes/electron carriers | MtrCAB outer-membrane conduit | complex | Enables extracellular electron uptake in engineered facultative chemolithoautotrophy | label-only | mtrCAB | (tu2023engineeringartificialphotosynthesis pages 1-2) |
| D. Energy conservation complexes/electron carriers | Gloeobacter rhodopsin | protein | Light-driven proton pump used experimentally to augment ATP supply for CO2 fixation | label-only | GR | (tu2023engineeringartificialphotosynthesis pages 1-2) |
| E. DIC acquisition/processing toolkit | dissolved inorganic carbon (DIC) | substrate pool | Carbon source pool supplying CO2/HCO3− to fixation pathways | CHEBI:16526 | n/a | (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10) |
| E. DIC acquisition/processing toolkit | carbon dioxide | chemical | Direct carbon source for chemolithoautotrophic biomass synthesis | CHEBI:16526 | carbon fixation pathway genes | (deng2023strategiesofchemolithoautotrophs pages 1-2, alvarez‐guzman2023effectofelectron pages 1-2) |
| E. DIC acquisition/processing toolkit | bicarbonate | chemical | DIC species assimilated or converted to CO2 for fixation | CHEBI:17544 | transporters/CA | (cornell2024genomeencodedmetabolicpotential pages 15-18, tu2023engineeringartificialphotosynthesis pages 1-2, atencio2024metabolicadaptationsunderpin pages 3-4) |
| E. DIC acquisition/processing toolkit | carbonic anhydrase | enzyme | Interconverts CO2 and HCO3− to match pathway demand | GO:0004089 | can, βCA, αCA, ιCA, CsoSCA | (tu2023engineeringartificialphotosynthesis pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10) |
| E. DIC acquisition/processing toolkit | DIC transporters | transporter class | Import inorganic carbon species for autotrophic metabolism | label-only | DAC, SulP, SbtA | (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10) |
| E. DIC acquisition/processing toolkit | DAC transporter | transporter | DIC uptake under defined pH/DIC regimes | label-only | dac | (scott2024widespreaddissolvedinorganic pages 7-10) |
| E. DIC acquisition/processing toolkit | SulP transporter | transporter | Candidate bicarbonate/DIC transport function in autotrophs | label-only | sulP | (scott2024widespreaddissolvedinorganic pages 7-10) |
| E. DIC acquisition/processing toolkit | SbtA transporter | transporter | High-affinity bicarbonate transport in some autotrophic genomes | label-only | sbtA | (scott2024widespreaddissolvedinorganic pages 7-10) |
| F. Key genes/enzymes/complexes | RuBisCO | enzyme | Carboxylase central to CBB-based chemolithoautotrophy | GO:0016984 | rbcL, rbcS | (laufermeiser2024oxidationofsulfur pages 1-2, scott2024widespreaddissolvedinorganic pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8) |
| F. Key genes/enzymes/complexes | phosphoribulokinase | enzyme | Regenerates RuBP in CBB cycle | label-only | prkA | (kurt2023perspectivesforusing pages 12-14) |
| F. Key genes/enzymes/complexes | ATP-citrate lyase | enzyme | Signature rTCA enzyme for citrate cleavage / carbon fixation direction | label-only | aclAB | (wang2024novelisolatesof pages 12-15) |
| F. Key genes/enzymes/complexes | 2-oxoglutarate:ferredoxin oxidoreductase | enzyme complex | Reductive carboxylation step in rTCA | label-only | oorABCD, OGOR | (wang2024novelisolatesof pages 12-15, prioretti2023carbonfixationin pages 1-2) |
| F. Key genes/enzymes/complexes | pyruvate:ferredoxin oxidoreductase | enzyme complex | Reductive carboxylation of acetyl-CoA to pyruvate in rTCA | label-only | PFOR | (prioretti2023carbonfixationin pages 1-2) |
| F. Key genes/enzymes/complexes | Fd6 ferredoxin | protein | Low-potential electron donor to PFOR/OGOR | label-only | fd6 | (prioretti2023carbonfixationin pages 1-2) |
| F. Key genes/enzymes/complexes | Fd7 ferredoxin | protein | Low-potential electron donor to PFOR/OGOR | label-only | fd7 | (prioretti2023carbonfixationin pages 1-2) |
| F. Key genes/enzymes/complexes | carbon monoxide dehydrogenase/acetyl-CoA synthase | enzyme complex | Core catalytic module of Wood–Ljungdahl pathway | label-only | codh, acs | (wang2023microbialconversionand pages 3-5, kurt2023perspectivesforusing pages 12-14) |
| F. Key genes/enzymes/complexes | formate dehydrogenase | enzyme | Supplies formate / reducing equivalents in WL and related pathways | GO:0050420 | fdh | (wang2023microbialconversionand pages 3-5, kurt2023perspectivesforusing pages 12-14) |
| F. Key genes/enzymes/complexes | formylmethanofuran dehydrogenase | enzyme | CO2 reduction step in WL-associated metabolism | label-only | fwd/fmd-like | (wang2023microbialconversionand pages 3-5, scott2024widespreaddissolvedinorganic pages 1-2) |
| F. Key genes/enzymes/complexes | ammonia monooxygenase | enzyme complex | Entry point for ammonia oxidation in nitrifying chemolithoautotrophy | GO:0003941 | amoA, amoB, amoC | (cornell2024genomeencodedmetabolicpotential pages 15-18, bayer2024contributionofammonia pages 1-4) |
| F. Key genes/enzymes/complexes | nitrate reductase | enzyme complex | Couples inorganic electron donor oxidation to nitrate respiration | GO:0008940 | napC-associated module | (wang2024novelisolatesof pages 12-15) |
| F. Key genes/enzymes/complexes | cytochrome c nitrite reductase | enzyme | Supports nitrite reduction during nitrogen-coupled chemolithotrophy | GO:0050421 | nrfA-like / COG3303 | (wang2024novelisolatesof pages 12-15) |
| F. Key genes/enzymes/complexes | rgy gene product | stress/adaptation factor | Supports DNA stability at high temperature in active vent chemolithoautotrophs | label-only | rgy | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| G. Environmental/experimental factors | hydrothermal vent fluids | environment | Canonical habitat rich in reduced inorganic substrates for chemolithoautotrophy | ENVO:01000030 | n/a | (deng2023strategiesofchemolithoautotrophs pages 1-2, laufermeiser2024oxidationofsulfur pages 1-2) |
| G. Environmental/experimental factors | deep subsurface aquifer | environment | Dark oligotrophic habitat supporting chemosynthetic productivity | ENVO:00000056 | n/a | (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8) |
| G. Environmental/experimental factors | dark ocean / below euphotic zone | environment | Major marine setting for nitrifier-associated dark carbon fixation | ENVO:01000044 | n/a | (bayer2024contributionofammonia pages 1-4, bayer2024contributionofammonia pages 9-11) |
| G. Environmental/experimental factors | low oxygen / microoxic conditions | environmental factor | Often favors sulfur, hydrogen, and iron oxidation coupled to autotrophy | label-only | n/a | (laufermeiser2024oxidationofsulfur pages 1-2, deng2023strategiesofchemolithoautotrophs pages 1-2) |
| G. Environmental/experimental factors | anoxic conditions | environmental factor | Select for WL and other low-energy autotrophic pathways | label-only | n/a | (atencio2024metabolicadaptationsunderpin pages 1-2, chen2023phylogeneticallyandmetabolically pages 10-11) |
| G. Environmental/experimental factors | extremely acidic conditions | environmental factor | Selective pressure shaping proton export and respiratory adaptation | label-only | n/a | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| G. Environmental/experimental factors | high temperature | environmental factor | Affects taxon-specific carbon fixation activity and stress adaptation | label-only | n/a | (deng2023strategiesofchemolithoautotrophs pages 1-2, atencio2024metabolicadaptationsunderpin pages 3-4) |
| G. Environmental/experimental factors | pH gradient | experimental factor | Modulates DIC speciation, transporter use, and niche partitioning | label-only | n/a | (deng2023strategiesofchemolithoautotrophs pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10) |
| G. Environmental/experimental factors | CO2/O2/N2 model flue gas | experimental factor | Assay condition for non-photosynthetic chemolithoautotrophic CO2 fixation | label-only | n/a | (alvarez‐guzman2023effectofelectron pages 1-2) |
| G. Environmental/experimental factors | phenylacetylene | inhibitor | Specific AMO inhibitor used to estimate ammonia-oxidizer contribution to DIC fixation | CHEBI:76217 | n/a | (bayer2024contributionofammonia pages 1-4) |
| G. Environmental/experimental factors | 13C-DNA SIP incubation | assay | Detects active carbon-fixing chemolithoautotrophs under defined conditions | label-only | n/a | (deng2023strategiesofchemolithoautotrophs pages 1-2) |
| G. Environmental/experimental factors | 14C-bicarbonate tracer assay | assay | Quantifies dark chemosynthetic CO2 fixation rates | label-only | n/a | (atencio2024metabolicadaptationsunderpin pages 3-4, atencio2024metabolicadaptationsunderpin pages 1-2) |


*Table: This table compiles candidate nodes for a chemolithoautotrophy causal graph, organized by pathway, substrates, electron-accepting processes, molecular machinery, DIC-handling toolkit, marker genes, and environmental factors. It is designed to support TraitMech-style curation with provisional ontology grounding and direct links to supporting evidence contexts.*

### Notes on ontology grounding
- **Chemicals:** many donors/acceptors map cleanly to CHEBI (e.g., H2 CHEBI:18276; thiosulfate CHEBI:30087; bicarbonate CHEBI:17544; O2 CHEBI:15379) (laufermeiser2024oxidationofsulfur pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10).
- **Processes:** carbon fixation pathways can often be grounded at GO pathway level (e.g., CBB cycle GO:0015977; rTCA GO:0019624) (scott2024widespreaddissolvedinorganic pages 1-2).
- **Gene markers:** gene symbols such as **aclAB, oorABCD, soxABCDYZ** are directly stated in recent genomic/physiology work on Sulfurospirillum (10.1128/msystems.00148-24; 2024-09; https://doi.org/10.1128/msystems.00148-24) (wang2024novelisolatesof pages 12-15). Others (e.g., “cytochrome bd ubiquinol oxidase”, “proton-pumping NADH:ubiquinone oxidoreductase”) are described at functional level and may need mapping to specific gene families (e.g., cydAB, nuo/ndh) during curation (deng2023strategiesofchemolithoautotrophs pages 1-2).

## 3) Evidence-backed candidate causal edges (triples)

The table below provides curation-ready edge candidates with quoted snippets, DOI-first references, and notes.

| Subject node | Predicate | Object node | Edge type (mechanistic/assay/environmental regulation) | Evidence snippet (short quote) | Reference (DOI + URL + pub year) | Citation ID(s) | Notes/uncertainty + suggested ontology grounding (CURIEs when clear) |
|---|---|---|---|---|---|---|---|
| molecular hydrogen | is oxidized by | [NiFe]-hydrogenases | mechanistic | “detected phylotypes of [NiFe]-hydrogenase belong to subgroups 1b, 2d, 4a, 4c, 4e, 1a, and 4f” | 10.1128/msystems.00148-24; https://doi.org/10.1128/msystems.00148-24; 2024 | (wang2024novelisolatesof pages 12-15) | Supports H2 oxidation module in vent Campylobacteria. Grounding: CHEBI:18276 hydrogen; label-only [NiFe]-hydrogenase complex. |
| subgroup 2d hydrogenase | supplies reductant for | reverse TCA cycle | mechanistic | “hydrogen oxidation is widespread… and can directly generate reductant for rTCA (subgroup 2d hydrogenase)” | 10.1128/msystems.00148-24; https://doi.org/10.1128/msystems.00148-24; 2024 | (wang2024novelisolatesof pages 12-15) | Strong but taxon-specific to Sulfurospirillum/Campylobacteria. Grounding: reverse TCA cycle GO:0019624; hydrogenase label-only. |
| sulfur oxidation (Sox system) | supports | chemoautotrophy potential | mechanistic | “oxidation system SOX, hydrogenase, and nitrate reductase, supporting the potential of chemoautotrophy” | 10.1128/msystems.00148-24; https://doi.org/10.1128/msystems.00148-24; 2024 | (wang2024novelisolatesof pages 12-15) | Gene-to-trait inference; curate as probable unless direct knockout data become available. Grounding: soxABCDYZ label-only. |
| soxABCDYZ | enables oxidation of | thiosulfate / reduced sulfur compounds | mechanistic | “the sulfur oxidation SOX system (soxABCDYZ)” | 10.1128/msystems.00148-24; https://doi.org/10.1128/msystems.00148-24; 2024 | (wang2024novelisolatesof pages 12-15) | Conservative gene→process edge. Grounding: CHEBI:30087 thiosulfate; sox genes label-only. |
| Fe(II) oxidation | drives | autotrophic CO2 fixation | mechanistic | “grow on Fe(II), H2, and thiosulfate… measured oxidation and autotrophic CO2 fixation rates” | 10.1093/ismejo/wrae173; https://doi.org/10.1093/ismejo/wrae173; 2024 | (laufermeiser2024oxidationofsulfur pages 1-2) | Direct physiological evidence. Grounding: CHEBI:29033 ferrous iron; CHEBI:16526 carbon dioxide. |
| H2 oxidation | drives | autotrophic CO2 fixation | mechanistic | “oxidation potential were 10, 24, and 952 mmol for iron, hydrogen, and thiosulfate oxidation and 0.3, 1, and 84 mmol CO2 fixation” | 10.1093/ismejo/wrae173; https://doi.org/10.1093/ismejo/wrae173; 2024 | (laufermeiser2024oxidationofsulfur pages 1-2) | Direct donor→fixation coupling in Hydrogenovibrio. Grounding: CHEBI:18276 H2; CHEBI:16526 CO2. |
| thiosulfate oxidation | drives | autotrophic CO2 fixation | mechanistic | “952 mmol for thiosulfate oxidation and 84 mmol CO2 fixation… per vent per hour” | 10.1093/ismejo/wrae173; https://doi.org/10.1093/ismejo/wrae173; 2024 | (laufermeiser2024oxidationofsulfur pages 1-2) | Strong quantitative support. Grounding: CHEBI:30087 thiosulfate; CHEBI:16526 CO2. |
| inorganic electron donor provided | alters expression of | donor-specific genes | environmental regulation | “Several genes were up- or downregulated depending on the inorganic electron donor provided.” | 10.1093/ismejo/wrae173; https://doi.org/10.1093/ismejo/wrae173; 2024 | (laufermeiser2024oxidationofsulfur pages 1-2) | Broad regulation edge; object can be refined later with transcript IDs. |
| RuBisCO | catalyzes | Calvin–Benson–Bassham cycle CO2 fixation | mechanistic | “Ribulose 1,5-bisphosphate carboxylase/oxygenase (RuBisCO)” | 10.1128/aem.01557-23; https://doi.org/10.1128/aem.01557-23; 2024 | (scott2024widespreaddissolvedinorganic pages 1-2) | Canonical carbon-fixation edge. Grounding: GO:0016984 RuBisCO; GO:0015977 CBB cycle. |
| aclAB | encodes module for | reverse TCA cycle CO2 fixation | mechanistic | “rTCA cycle for CO2 fixation (encoded by genes aclAB and oorABCD)” | 10.1128/msystems.00148-24; https://doi.org/10.1128/msystems.00148-24; 2024 | (wang2024novelisolatesof pages 12-15) | Strong gene→pathway assignment. Grounding: label-only aclAB; GO:0019624 reverse TCA. |
| oorABCD | encodes module for | reverse TCA cycle CO2 fixation | mechanistic | “rTCA cycle for CO2 fixation (encoded by genes aclAB and oorABCD)” | 10.1128/msystems.00148-24; https://doi.org/10.1128/msystems.00148-24; 2024 | (wang2024novelisolatesof pages 12-15) | Strong gene→pathway assignment. Grounding: label-only oorABCD; GO:0019624 reverse TCA. |
| PFOR | catalyzes | reductive carboxylation of acetyl-CoA to pyruvate | mechanistic | “PFOR… responsible… for the reductive carboxylation of acetyl-CoA to pyruvate” | 10.3390/life13030627; https://doi.org/10.3390/life13030627; 2023 | (prioretti2023carbonfixationin pages 1-2) | Key mechanistic edge for rTCA. Grounding: label-only PFOR. |
| OGOR | catalyzes | reductive carboxylation of succinyl-CoA to 2-oxoglutarate | mechanistic | “OGOR… responsible… for… succinyl-CoA to 2-oxoglutarate” | 10.3390/life13030627; https://doi.org/10.3390/life13030627; 2023 | (prioretti2023carbonfixationin pages 1-2) | Key mechanistic edge for rTCA. Grounding: label-only OGOR. |
| Fd6 ferredoxin | donates electrons to | PFOR and OGOR | mechanistic | “Fd6 and Fd7… can physically interact and exchange electrons with both PFOR and OGOR” | 10.3390/life13030627; https://doi.org/10.3390/life13030627; 2023 | (prioretti2023carbonfixationin pages 1-2) | Strong biochemical support. Grounding: reduced ferredoxin CHEBI:60524; Fd6 label-only. |
| Fd7 ferredoxin | donates electrons to | PFOR and OGOR | mechanistic | “Fd6 and Fd7… can physically interact and exchange electrons with both PFOR and OGOR” | 10.3390/life13030627; https://doi.org/10.3390/life13030627; 2023 | (prioretti2023carbonfixationin pages 1-2) | Strong biochemical support. Grounding: reduced ferredoxin CHEBI:60524; Fd7 label-only. |
| carbonic anhydrase | facilitates supply of | CO2/HCO3− to autotrophic pathways | mechanistic | “carbonic anhydrase enzymes (CA) to facilitate DIC fixation” | 10.1128/aem.01557-23; https://doi.org/10.1128/aem.01557-23; 2024 | (scott2024widespreaddissolvedinorganic pages 1-2) | General DIC-toolkit edge. Grounding: GO:0004089 carbonic anhydrase; CHEBI:17544 bicarbonate; CHEBI:16526 CO2. |
| DIC transporters | increase availability of | dissolved inorganic carbon for fixation pathways | mechanistic | “DIC transporters… bridge supply from the environment to demand by the autotrophic pathway” | 10.1128/aem.01557-23; https://doi.org/10.1128/aem.01557-23; 2024 | (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10) | General but well-supported review edge; could split into DAC/SulP/SbtA-specific nodes later. |
| β-carbonic anhydrase overexpression | enhances | CO2 fixation | assay | “Overexpression of a carbonic anhydrase further enhances CO2 fixation.” | 10.1038/s41467-023-43524-4; https://doi.org/10.1038/s41467-023-43524-4; 2023 | (tu2023engineeringartificialphotosynthesis pages 1-2) | Engineered system in R. eutropha; assay-specific. Grounding: can / βCA label-only. |
| MtrCAB outer-membrane conduit | enables | extracellular electron uptake into quinone pool | mechanistic | “extracellular electron uptake via the outer-membrane MtrCAB conduit… into the quinone pool” | 10.1038/s41467-023-43524-4; https://doi.org/10.1038/s41467-023-43524-4; 2023 | (tu2023engineeringartificialphotosynthesis pages 1-2) | Strong mechanistic evidence in engineered facultative chemolithoautotroph. Grounding: mtrCAB label-only. |
| Gloeobacter rhodopsin | generates | proton motive force | mechanistic | “light-driven proton pumping by a microbial rhodopsin… to generate proton motive force” | 10.1038/s41467-023-43524-4; https://doi.org/10.1038/s41467-023-43524-4; 2023 | (tu2023engineeringartificialphotosynthesis pages 1-2) | Assay-specific augmentation, not native to most chemolithoautotrophs. Grounding: GO:0015992 proton motive force. |
| proton motive force | drives | ATP synthesis and reversed ETC for NADH/NADPH regeneration | mechanistic | “The proton motive force drives ATP synthesis and can reverse the electron transport chain… to regenerate NADH/NADPH” | 10.1038/s41467-023-43524-4; https://doi.org/10.1038/s41467-023-43524-4; 2023 | (tu2023engineeringartificialphotosynthesis pages 1-2) | Links energy conservation to reductant generation for fixation. Grounding: ATP synthase GO:0015986; NADH CHEBI:57945; NADPH CHEBI:57783. |
| extracellular electrons from electrode | support | CO2 assimilation | assay | “bacteria to use inorganic chemicals—or an electrode—as electron donors to assimilate CO2” | 10.1038/s41467-023-43524-4; https://doi.org/10.1038/s41467-023-43524-4; 2023 | (tu2023engineeringartificialphotosynthesis pages 1-2) | Useful boundary/assay edge; not a natural trait-defining donor in most taxa. |
| phenylacetylene | inhibits | ammonia monooxygenase / ammonia oxidizers | assay | “phenylacetylene - a specific inhibitor of the ammonia monooxygenase enzyme - to selectively inhibit ammonia oxidizers” | 10.1101/2024.11.16.623942; https://doi.org/10.1101/2024.11.16.623942; 2024 | (bayer2024contributionofammonia pages 1-4) | Preprint; inhibitor edge is strong but should be marked assay-specific. Grounding: CHEBI:76217 phenylacetylene; amoA complex label-only. |
| ammonia oxidizer inhibition by phenylacetylene | reduces estimated contribution to | dark-ocean DIC fixation | assay | “ammonia oxidizers contribute only a small fraction… accounting for 2 to 22% of the depth-integrated rates” | 10.1101/2024.11.16.623942; https://doi.org/10.1101/2024.11.16.623942; 2024 | (bayer2024contributionofammonia pages 1-4) | Assay-derived contribution estimate; preprint and ecosystem-specific. |
| high temperature (45→65 °C, moderate acidity) | increases carbon fixation activity of | Nautiliales | environmental regulation | “carbon fixation activities of Nautiliales… significantly increased from 45 to 65 °C under moderately acidic condition” | 10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w; 2023 | (deng2023strategiesofchemolithoautotrophs pages 1-2) | Taxon- and habitat-specific regulation. Grounding: NCBITaxon:Nautiliales label-only. |
| extremely acidic conditions | reduce heat tolerance of | Nautiliales | environmental regulation | “their heat tolerance was reduced under extremely acidic conditions” | 10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w; 2023 | (deng2023strategiesofchemolithoautotrophs pages 1-2) | Environmental modulation, not direct trait definition. |
| low pH / extreme acidity | selects for | proton export and NADH:ubiquinone oxidoreductase genes in Campylobacterales | environmental regulation | “Genes encoding proteins involved in proton export, including the membrane arm subunits of proton-pumping NADH: ubiquinone oxidoreductase… enable Campylobacterales to adapt to extremely acidic conditions.” | 10.1186/s40168-023-01712-w; https://doi.org/10.1186/s40168-023-01712-w; 2023 | (deng2023strategiesofchemolithoautotrophs pages 1-2) | Strong adaptation edge; may belong in environmental subgraph. |
| mixed organic-substrate capacity / dual pathways | enables | mixotrophic or conditional trait expression | environmental regulation | “most of the WL-pathway containing taxa displayed a mixotrophic lifestyle” | 10.1038/s43705-023-00327-4; https://doi.org/10.1038/s43705-023-00327-4; 2023 | (chen2023phylogeneticallyandmetabolically pages 10-11) | Boundary case: not all CO2-fixing taxa are obligate chemolithoautotrophs. Grounding: mixotrophy label-only. |
| dual autotrophic pathways (WL + CBB in same genome) | permits | conditional pathway use by energy context | environmental regulation | “organisms encoding two CO2-fixation pathways (Wood–Ljungdahl (WL) and Calvin–Benson–Bassham (CBB) cycles) in the same genome” | 10.1038/s43705-023-00327-4; https://doi.org/10.1038/s43705-023-00327-4; 2023 | (chen2023phylogeneticallyandmetabolically pages 10-11) | Useful warning edge for curation: presence of fixation genes does not imply obligate chemolithoautotrophy. |


*Table: This table lists candidate causal edges for the chemolithoautotrophic trait using only the provided evidence contexts. It covers core donor-to-energy-to-fixation links, gene/pathway mechanisms, environmental regulation, assay-specific inhibitors, and important boundary cases for curation.*

## 4) Recent developments (2023–2024 highlights)

### 4.1 Donor-flexible chemolithoautotrophy at hydrothermal vents
A 2024 ISME Journal study isolated vent Hydrogenovibrio strains that can grow on **Fe(II), H2, and thiosulfate**, with **measured oxidation and CO2 fixation rates** and donor-dependent transcriptional shifts (10.1093/ismejo/wrae173; 2024-01; https://doi.org/10.1093/ismejo/wrae173) (laufermeiser2024oxidationofsulfur pages 1-2). Importantly, the work provides quantitative “per vent per hour” oxidation/fixation potential estimates, supporting graph edges linking **electron donor availability → oxidation flux → CO2 fixation** (laufermeiser2024oxidationofsulfur pages 1-2).

### 4.2 Mechanistic detail for rTCA: low-potential ferredoxins as electron donors
A 2023 biochemical study in Aquifex aeolicus identified **two oxygen-stable low-potential [4Fe-4S] ferredoxins (Fd6, Fd7)** that physically interact and exchange electrons with **PFOR and OGOR**, key rTCA enzymes catalyzing energetically uphill reductive carboxylations (10.3390/life13030627; 2023-02; https://doi.org/10.3390/life13030627) (prioretti2023carbonfixationin pages 1-2). This provides unusually direct molecular evidence for an edge **ferredoxin → PFOR/OGOR → rTCA carbon fixation**.

### 4.3 DIC toolkits beyond cyanobacteria: transport + carbonic anhydrase as bridging mechanisms
A 2024 minireview synthesizes how DIC transporters and carbonic anhydrase “facilitate DIC fixation” and surveys their distribution across organisms using CBB, rTCA, WL, and hydroxypropionate-based pathways (10.1128/aem.01557-23; 2024-02; https://doi.org/10.1128/aem.01557-23) (scott2024widespreaddissolvedinorganic pages 1-2). It also enumerates specific transporter families (DAC, SulP, SbtA) and CA classes across taxa, enabling environment-to-mechanism edges (e.g., pH/DIC speciation → transporter usage) (scott2024widespreaddissolvedinorganic pages 7-10).

### 4.4 Re-assessing the role of nitrifiers in dark-ocean carbon fixation (preprint)
A 2024 bioRxiv preprint used a specific AMO inhibitor (phenylacetylene) to estimate how much **ammonia oxidizers** contribute to **dark-ocean DIC fixation**, concluding they account for only **2–22% of depth-integrated rates**, with maxima up to 50% at nitrification maxima (10.1101/2024.11.16.623942; 2024-11; https://doi.org/10.1101/2024.11.16.623942) (bayer2024contributionofammonia pages 1-4). This challenges a common assumption that nitrification dominates dark DIC fixation and motivates additional causal nodes for alternative energy sources supporting dark CO2 fixation (bayer2024contributionofammonia pages 1-4).

## 5) Current applications and real-world implementations

### 5.1 Flue-gas CO2 capture by non-photosynthetic (chemolithoautotrophic) communities
A 2023 Microbial Biotechnology study tested inorganic electron donors for CO2 capture from model cement flue gas and reported strong dependence on donor identity: **Na2S enabled 100% CO2 consumption**, FeCl2 only 28%, and a continuous biotrickling filter achieved up to 77% CO2 consumption using Na2S (10.1111/1751-7915.14353; 2023-10; https://doi.org/10.1111/1751-7915.14353) (alvarez‐guzman2023effectofelectron pages 1-2). This supports application edges **electron donor choice → CO2 removal performance**.

### 5.2 Low-carbon wastewater treatment using chemolithotroph-supported processes
A 2024 Scientific Reports bubble-column bioreactor study reports simultaneous flue-gas and wastewater treatment with **89.80% CO2 removal**, **77.30% SO2 removal**, **80.77% NO removal**, and **3.66 g/L biomass yield** (10.1038/s41598-024-67053-2; 2024-07; https://doi.org/10.1038/s41598-024-67053-2) (barla2024sustainablesynergisticapproach pages 1-2). While mechanistic genes are not enumerated in the excerpt, the performance metrics are useful for application-oriented curation.

### 5.3 Engineered electron supply for CO2 fixation (electrode + rhodopsin)
A 2023 Nature Communications paper engineered R. eutropha for photoelectrosynthetic CO2 fixation by integrating extracellular electron uptake via **MtrCAB** and light-driven proton pumping via **Gloeobacter rhodopsin**; it explicitly states the PMF supports ATP synthesis and can reverse ETC to regenerate NAD(P)H, and that carbonic anhydrase overexpression “enhances CO2 fixation” (10.1038/s41467-023-43524-4; 2023-12; https://doi.org/10.1038/s41467-023-43524-4) (tu2023engineeringartificialphotosynthesis pages 1-2). These are curated as **assay/engineering edges**, not necessarily universally biological.

## 6) Relevant statistics and quantitative evidence (recent)

### 6.1 Hydrothermal vents: donor-specific oxidation and CO2 fixation potentials
Hydrogenovibrio strain-level estimates suggest oxidation potentials of **10 mmol Fe(II) h−1**, **24 mmol H2 h−1**, and **952 mmol thiosulfate h−1 per vent**, corresponding to **0.3, 1, and 84 mmol CO2 fixed h−1 per vent**, respectively (10.1093/ismejo/wrae173; 2024-01; https://doi.org/10.1093/ismejo/wrae173) (laufermeiser2024oxidationofsulfur pages 1-2). The corresponding figure/table were extracted:

(see figure/table image) (laufermeiser2024oxidationofsulfur media e0fa8caa)

### 6.2 Deep subsurface aquifers: chemosynthetic productivity and prevalence of fixation pathways
In deep Negev aquifers (to 1.5 km; up to ~60°C), chemosynthetic productivity was estimated at **0.55 ± 0.06 to 0.82 ± 0.07 µg C L−1 d−1**, and **60% of MAGs** carried genes for autotrophic pathways, mainly CBB and WL (10.1038/s41598-024-68868-9; 2024-08; https://doi.org/10.1038/s41598-024-68868-9) (atencio2024metabolicadaptationsunderpin pages 1-2). The same study reported RuBisCO in **32 MAGs** with forms I/II distributions (10.1038/s41598-024-68868-9; 2024-08; https://doi.org/10.1038/s41598-024-68868-9) (atencio2024metabolicadaptationsunderpin pages 6-8).

### 6.3 Dark ocean: ammonia oxidizers may contribute a minority of DIC fixation (preprint)
Ammonia oxidizers comprise up to **40% of deep-water microbial cells** yet account for only **2–22% of depth-integrated dark DIC fixation** in the eastern tropical/subtropical Pacific in inhibitor experiments; up to 50% at nitrification maxima (10.1101/2024.11.16.623942; 2024-11; https://doi.org/10.1101/2024.11.16.623942) (bayer2024contributionofammonia pages 1-4).

### 6.4 Industrial gas contexts: cement flue gas and bioreactor performance
Cement emissions are cited as **~8% of global CO2 (~1.4 Gt/yr)**; donor choice gave 100% CO2 consumption with sulfide and 28% with FeCl2 in acclimated non-photosynthetic communities (10.1111/1751-7915.14353; 2023-10; https://doi.org/10.1111/1751-7915.14353) (alvarez‐guzman2023effectofelectron pages 1-2).

## 7) Expert opinions / synthesis from authoritative sources

**DIC supply–demand is a mechanistic bottleneck.** Scott et al. (2024) argue that DIC uptake and conversion toolkits (transporters + carbonic anhydrase) are likely to “bridge supply from the environment to demand by the autotrophic pathway,” and are not exclusive to CBB organisms, implying a broadly conserved mechanistic layer that can be curated upstream of specific fixation pathways (10.1128/aem.01557-23; 2024-02; https://doi.org/10.1128/aem.01557-23) (scott2024widespreaddissolvedinorganic pages 1-2).

**Dark-ocean chemolithoautotrophy is likely more diverse than nitrification alone.** Bayer et al. (2024 preprint) provide inhibitor-based evidence that ammonia oxidation may not fuel most dark DIC fixation, implying additional inorganic energy sources (e.g., sulfur, hydrogen, iron) or non-nitrifier processes should be emphasized as candidate upstream nodes in marine causal graphs (10.1101/2024.11.16.623942; 2024-11; https://doi.org/10.1101/2024.11.16.623942) (bayer2024contributionofammonia pages 1-4).

## 8) Warnings / curation guardrails (do-not-curate-yet or curate-as-uncertain)

1. **Mixotrophy is common:** presence of CO2 fixation genes does not imply obligate chemolithoautotrophy. Blue-hole MAGs with both WL and CBB and reported mixotrophy indicate conditional use and organic uptake (10.1038/s43705-023-00327-4; 2023-11; https://doi.org/10.1038/s43705-023-00327-4) (chen2023phylogeneticallyandmetabolically pages 10-11).
2. **Engineered edges are assay-specific:** MtrCAB-mediated electron uptake and rhodopsin-driven PMF are powerful but should be curated as engineered/experimental mechanisms, not canonical chemolithoautotrophic machinery (10.1038/s41467-023-43524-4; 2023-12; https://doi.org/10.1038/s41467-023-43524-4) (tu2023engineeringartificialphotosynthesis pages 1-2).
3. **Iron oxidation genetics may be unknown:** Hydrogenovibrio iron oxidation lacked known canonical genes; transcriptomic signatures suggested “unknown iron-oxidation pathways,” so gene-level edges for Fe(II) oxidation should be curated cautiously unless additional sources provide specific gene assignments (10.1093/ismejo/wrae173; 2024-01; https://doi.org/10.1093/ismejo/wrae173) (laufermeiser2024oxidationofsulfur pages 1-2).
4. **Preprints should be flagged:** the nitrifier contribution estimates are based on a 2024 bioRxiv manuscript and should be curated as provisional until peer reviewed (10.1101/2024.11.16.623942; 2024-11; https://doi.org/10.1101/2024.11.16.623942) (bayer2024contributionofammonia pages 1-4).

## 9) DOI-first bibliography (with URLs and publication dates)

- **Laufer-Meiser K, et al.** “Oxidation of sulfur, hydrogen, and iron by metabolically versatile Hydrogenovibrio from deep sea hydrothermal vents.” *The ISME Journal* (2024-01). DOI: **10.1093/ismejo/wrae173**. URL: https://doi.org/10.1093/ismejo/wrae173 (laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur media e0fa8caa)
- **Deng W, et al.** “Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem.” *Microbiome* (2023-12). DOI: **10.1186/s40168-023-01712-w**. URL: https://doi.org/10.1186/s40168-023-01712-w (deng2023strategiesofchemolithoautotrophs pages 1-2)
- **Scott KM, Payne RR, Gahramanova A.** “Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea…” *Applied and Environmental Microbiology* (2024-02). DOI: **10.1128/aem.01557-23**. URL: https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 7-10)
- **Prioretti L, et al.** “Carbon Fixation in the Chemolithoautotrophic Bacterium Aquifex aeolicus Involves Two Low-Potential Ferredoxins…” *Life* (2023-02). DOI: **10.3390/life13030627**. URL: https://doi.org/10.3390/life13030627 (prioretti2023carbonfixationin pages 1-2)
- **Tu W, et al.** “Engineering artificial photosynthesis based on rhodopsin for CO2 fixation.” *Nature Communications* (2023-12). DOI: **10.1038/s41467-023-43524-4**. URL: https://doi.org/10.1038/s41467-023-43524-4 (tu2023engineeringartificialphotosynthesis pages 1-2)
- **Atencio B, et al.** “Metabolic adaptations underpin high productivity rates in relict subsurface water.” *Scientific Reports* (2024-08). DOI: **10.1038/s41598-024-68868-9**. URL: https://doi.org/10.1038/s41598-024-68868-9 (atencio2024metabolicadaptationsunderpin pages 1-2, atencio2024metabolicadaptationsunderpin pages 6-8, atencio2024metabolicadaptationsunderpin pages 3-4)
- **Alvarez-Guzmán CL, et al.** “Effect of electron donors on CO2 fixation… by non-photosynthetic microbial communities…” *Microbial Biotechnology* (2023-10). DOI: **10.1111/1751-7915.14353**. URL: https://doi.org/10.1111/1751-7915.14353 (alvarez‐guzman2023effectofelectron pages 1-2)
- **Barla RJ, Gupta S, Raghuvanshi S.** “Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas.” *Scientific Reports* (2024-07). DOI: **10.1038/s41598-024-67053-2**. URL: https://doi.org/10.1038/s41598-024-67053-2 (barla2024sustainablesynergisticapproach pages 1-2)
- **Li J, et al.** “Arcobacteraceae are ubiquitous mixotrophic bacteria…” *mSystems* (2024-07). DOI: **10.1128/msystems.00513-24**. URL: https://doi.org/10.1128/msystems.00513-24 (li2024arcobacteraceaeareubiquitous pages 10-12)
- **Chen X, et al.** “Phylogenetically and metabolically diverse autotrophs in the world’s deepest blue hole.” *ISME Communications* (2023-11). DOI: **10.1038/s43705-023-00327-4**. URL: https://doi.org/10.1038/s43705-023-00327-4 (chen2023phylogeneticallyandmetabolically pages 10-11)
- **Wang L, et al.** “Novel isolates of hydrogen-oxidizing chemolithoautotrophic Sulfurospirillum…” *mSystems* (2024-09). DOI: **10.1128/msystems.00148-24**. URL: https://doi.org/10.1128/msystems.00148-24 (wang2024novelisolatesof pages 12-15)
- **Bayer B, et al.** “Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean.” *bioRxiv* (2024-11). DOI: **10.1101/2024.11.16.623942**. URL: https://doi.org/10.1101/2024.11.16.623942 (bayer2024contributionofammonia pages 1-4, bayer2024contributionofammonia pages 9-11)
- **Kurt E, et al.** “Perspectives for Using CO2 as a Feedstock for Biomanufacturing of Fuels and Chemicals.” *Bioengineering* (2023-11). DOI: **10.3390/bioengineering10121357**. URL: https://doi.org/10.3390/bioengineering10121357 (kurt2023perspectivesforusing pages 9-11, kurt2023perspectivesforusing pages 8-9, kurt2023perspectivesforusing pages 12-14, kurt2023perspectivesforusing pages 6-8)



References

1. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 14 citations and is from a highest quality peer-reviewed journal.

2. (laufermeiser2024oxidationofsulfur pages 1-2): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 8 citations.

3. (kurt2023perspectivesforusing pages 9-11): Elif Kurt, Jiansong Qin, Alexandria Williams, Youbo Zhao, and Dongming Xie. Perspectives for using co2 as a feedstock for biomanufacturing of fuels and chemicals. Bioengineering, 10:1357, Nov 2023. URL: https://doi.org/10.3390/bioengineering10121357, doi:10.3390/bioengineering10121357. This article has 38 citations.

4. (tu2023engineeringartificialphotosynthesis pages 1-2): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 68 citations and is from a highest quality peer-reviewed journal.

5. (li2024arcobacteraceaeareubiquitous pages 10-12): Jianyang Li, Shizheng Xiang, Yufei Li, Ruolin Cheng, Qiliang Lai, Liping Wang, Guizhen Li, Chunming Dong, and Zongze Shao. <i>arcobacteraceae</i> are ubiquitous mixotrophic bacteria playing important roles in carbon, nitrogen, and sulfur cycling in global oceans. Jul 2024. URL: https://doi.org/10.1128/msystems.00513-24, doi:10.1128/msystems.00513-24. This article has 31 citations and is from a peer-reviewed journal.

6. (chen2023phylogeneticallyandmetabolically pages 10-11): Xing Chen, Jiwen Liu, Xiao-Yu Zhu, Chun-Xu Xue, Peng Yao, Liang Fu, Zuosheng Yang, Kai Sun, Mingchao Yu, Xiaolei Wang, and Xiaohua Zhang. Phylogenetically and metabolically diverse autotrophs in the world’s deepest blue hole. ISME Communications, Nov 2023. URL: https://doi.org/10.1038/s43705-023-00327-4, doi:10.1038/s43705-023-00327-4. This article has 20 citations and is from a peer-reviewed journal.

7. (scott2024widespreaddissolvedinorganic pages 1-2): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

8. (atencio2024metabolicadaptationsunderpin pages 6-8): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

9. (wang2024novelisolatesof pages 12-15): Li Wang, Xinyi Cheng, Yi-Yang Guo, Junwei Cao, Mingye Sun, Jiang-Shiou Hwang, Rulong Liu, and Jiasong Fang. Novel isolates of hydrogen-oxidizing chemolithoautotrophic <i>sulfurospirillum</i> provide insight to the functions and adaptation mechanisms of campylobacteria in shallow-water hydrothermal vents. Sep 2024. URL: https://doi.org/10.1128/msystems.00148-24, doi:10.1128/msystems.00148-24. This article has 7 citations and is from a peer-reviewed journal.

10. (prioretti2023carbonfixationin pages 1-2): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 7 citations.

11. (atencio2024metabolicadaptationsunderpin pages 1-2): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

12. (wang2023microbialconversionand pages 3-5): Ge-Ge Wang, Zhang Yuan, Xiao-Yan Wang, and Gen-Lin Zhang. Microbial conversion and utilization of co2. Annals of Civil and Environmental Engineering, 7:045-060, Sep 2023. URL: https://doi.org/10.29328/journal.acee.1001055, doi:10.29328/journal.acee.1001055. This article has 3 citations.

13. (cornell2024genomeencodedmetabolicpotential pages 15-18): C Cornell. Genome-encoded metabolic potential of the nitrosocosmicus genus and related ammonia-oxidizing archaea. Unknown journal, 2024.

14. (kurt2023perspectivesforusing pages 6-8): Elif Kurt, Jiansong Qin, Alexandria Williams, Youbo Zhao, and Dongming Xie. Perspectives for using co2 as a feedstock for biomanufacturing of fuels and chemicals. Bioengineering, 10:1357, Nov 2023. URL: https://doi.org/10.3390/bioengineering10121357, doi:10.3390/bioengineering10121357. This article has 38 citations.

15. (alvarez‐guzman2023effectofelectron pages 1-2): Cecilia Lizeth Alvarez‐Guzmán, Karla María Muñoz‐Páez, and Idania Valdez‐Vazquez. Effect of electron donors on co2 fixation from a model cement industry flue gas by non‐photosynthetic microbial communities in batch and continuous reactors. Microbial Biotechnology, 16:2387-2400, Oct 2023. URL: https://doi.org/10.1111/1751-7915.14353, doi:10.1111/1751-7915.14353. This article has 7 citations and is from a peer-reviewed journal.

16. (bayer2024contributionofammonia pages 1-4): Barbara Bayer, Katharina Kitzinger, Nicola L. Paul, Justine B. Albers, Mak A. Saito, Michael Wagner, Craig A. Carlson, and Alyson E. Santoro. Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.16.623942, doi:10.1101/2024.11.16.623942. This article has 1 citations.

17. (bayer2024contributionofammonia pages 9-11): Barbara Bayer, Katharina Kitzinger, Nicola L. Paul, Justine B. Albers, Mak A. Saito, Michael Wagner, Craig A. Carlson, and Alyson E. Santoro. Contribution of ammonia oxidizers to inorganic carbon fixation in the dark ocean. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.16.623942, doi:10.1101/2024.11.16.623942. This article has 1 citations.

18. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

19. (atencio2024metabolicadaptationsunderpin pages 3-4): Betzabe Atencio, Eyal Geisler, Maxim Rubin-Blum, Edo Bar-Zeev, Eilon M. Adar, Roi Ram, and Zeev Ronen. Metabolic adaptations underpin high productivity rates in relict subsurface water. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-68868-9, doi:10.1038/s41598-024-68868-9. This article has 3 citations and is from a peer-reviewed journal.

20. (kurt2023perspectivesforusing pages 12-14): Elif Kurt, Jiansong Qin, Alexandria Williams, Youbo Zhao, and Dongming Xie. Perspectives for using co2 as a feedstock for biomanufacturing of fuels and chemicals. Bioengineering, 10:1357, Nov 2023. URL: https://doi.org/10.3390/bioengineering10121357, doi:10.3390/bioengineering10121357. This article has 38 citations.

21. (barla2024sustainablesynergisticapproach pages 1-2): Rachael J. Barla, Suresh Gupta, and Smita Raghuvanshi. Sustainable synergistic approach to chemolithotrophs—supported bioremediation of wastewater and flue gas. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-67053-2, doi:10.1038/s41598-024-67053-2. This article has 9 citations and is from a peer-reviewed journal.

22. (laufermeiser2024oxidationofsulfur media e0fa8caa): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 8 citations.

23. (kurt2023perspectivesforusing pages 8-9): Elif Kurt, Jiansong Qin, Alexandria Williams, Youbo Zhao, and Dongming Xie. Perspectives for using co2 as a feedstock for biomanufacturing of fuels and chemicals. Bioengineering, 10:1357, Nov 2023. URL: https://doi.org/10.3390/bioengineering10121357, doi:10.3390/bioengineering10121357. This article has 38 citations.