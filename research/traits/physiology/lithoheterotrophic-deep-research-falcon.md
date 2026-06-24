---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:31:16.846791'
end_time: '2026-06-18T11:47:41.296437'
duration_seconds: 984.45
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: lithoheterotrophic
  trait_identifier: METPO:1000648
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: lithoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from the oxidation
    of inorganic compounds while using organic compounds as the primary carbon source
    for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: lithoheterotroph
  evidence_summary: 'DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic
    strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth
    with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize
    inorganic atoms or molecules (Review supports inorganic compound oxidation as
    lithotrophic energy metabolism.)'
  causal_graph_summary: 'lithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes,
    9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoheterotrophic
- **METPO identifier:** METPO:1000648
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of inorganic compounds while using organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.)
- **Existing causal graph summary:** lithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **lithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoheterotrophic.yaml`.

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
- **Trait label:** lithoheterotrophic
- **METPO identifier:** METPO:1000648
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of inorganic compounds while using organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.)
- **Existing causal graph summary:** lithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **lithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoheterotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **lithoheterotrophic** (METPO:1000648)

### Scope summary (trait meaning, boundaries, and current understanding)
**Lithoheterotrophic (aka chemolithoheterotrophic)** metabolism denotes organisms that obtain **energy** (electron flow for respiration/PMF/ATP) from oxidation of **inorganic electron donors** while using **organic carbon** as the primary carbon source for biosynthesis (METPO:1000648). A recent synthesis of sulfur-oxidizing bacteria (SOB) states that *chemolithoheterotrophic* SOB “require a source of organic carbon for biosynthesis” while using reduced sulfur compounds for energy, explicitly separating energy source from carbon source. (quinn2025characterizingstratifiedmicrobiala pages 20-23)

**Key boundary distinctions for curation**:
- **Chemolithoautotrophy**: inorganic electron donor-derived energy plus **CO2/HCO3− fixation** as carbon source (e.g., Fe(II) oxidation coupled to O2 reduction “while fixing carbon dioxide”). (jain2021engineeringlithoheterotrophyin pages 1-2)
- **Chemoorganoheterotrophy**: both energy and carbon from organic substrates (e.g., growth using “pyruvate, or glycerol as carbon and energy sources”). (quinn2025characterizingstratifiedmicrobiala pages 20-23)
- **Mixotrophy/facultative chemolithotrophy** (boundary case): organisms can switch or combine organic and inorganic energy/carbon strategies; SOB can be “obligate chemolithotrophs, facultative chemolithotrophs, and chemolithoheterotrophs.” (zhuang2024electrontransferin pages 5-6)

**Operational phenotype definition for TraitMech** (recommended):
- Positive: growth requires an inorganic electron donor (e.g., Fe(II), sulfide, thiosulfate) **and** organic carbon supply for biomass.
- Negative controls: no growth in organic carbon alone (i.e., cannot fully shift to chemoorganoheterotrophy under assay conditions), and/or no growth in inorganic donor + CO2 alone (i.e., not chemolithoautotrophic under the tested conditions).

### Recent developments and latest research (prioritize 2023–2024)
1. **Electron-transfer mechanisms in sulfur cycling (review, 2024)**: A 2024 review highlights extracellular electron transfer (EET) modalities relevant to lithotrophy/chemolithoheterotrophy in sulfidic systems, emphasizing mediated interspecies electron transfer (MIET) and direct interspecies electron transfer (DIET) via “conductive pili… and outer-surface c-type cytochromes,” as well as long-distance electron transfer (LDET) (e.g., cable bacteria). These mechanisms are important for causal graphs that include community-level or mineral/electrode electron exchange. (zhuang2024electrontransferin pages 1-3)
2. **Taxonomic standards document (2024)** provides recent authoritative examples distinguishing **electron donors** from **carbon source** in anaerobic Halobacteria, describing chemolithoheterotrophic members “using formate or hydrogen as electron donors and elemental sulfur, thiosulfate, or dimethyl sulfoxide as electron acceptors,” reinforcing that lithoheterotrophy is grounded in electron donor identity rather than carbon source alone. (cui2024proposedminimalstandards pages 2-3)
3. **Environmental community studies (2023)** increasingly report chemolithotrophic and chemolithoheterotrophic functional guilds based on geochemistry and enrichment responses (e.g., serpentinizing springs; geothermal biofilms), indicating that lithoheterotrophy is often inferred from combined geochemical context and functional annotations rather than single-organism physiology in modern field studies. (jain2021engineeringlithoheterotrophyin pages 1-2)

**Note on evidence availability**: Within the retrieved 2023–2024 set, explicit uses of the term *“lithoheterotrophy”* are less common than *“chemolithoheterotrophy,”* particularly in sulfur cycling and EET contexts; thus, curations should accept the chemolithoheterotrophy label as equivalent when carbon-vs-energy sources are clearly separated. (zhuang2024electrontransferin pages 5-6, quinn2025characterizingstratifiedmicrobiala pages 20-23)

### Current applications and real-world implementations (evidence-backed in current corpus)
1. **Bioelectrochemical systems / electro-fermentation**: Electrodes can serve as inorganic electron donors supporting microbial respiration. A 2023 bioprocess-focused source summarizes evidence that *Geobacter sulfurreducens* can grow and reduce fumarate to succinate with a **cathode as the sole electron donor**, illustrating an applied setting where lithotrophic electron uptake can support metabolism (and potentially lithoheterotrophic production if organic carbon is used for biomass). (bartholet2023rationaldesignand pages 54-58)
2. **Sulfide detoxification coupled to denitrification (environmental application concept)**: Chemolithoheterotrophic coupling of sulfide oxidation with nitrate respiration is positioned as a mechanism allowing heterotrophic denitrifiers to thrive in sulfidic settings and potentially modulate greenhouse gas outcomes by enabling complete denitrification under sulfide stress (mechanistic basis: sulfide inhibition of key denitrification enzymes). (shao2025versatilenitraterespiringheterotrophs pages 1-2)

### Mechanistic entities (candidate nodes for `lithoheterotrophic.yaml`)
The following artifact compiles **candidate nodes**, grouped by type, with suggested ontology groundings where clear.

| Node type | Candidate node label | Short description | Suggested grounding CURIE(s) | Evidence citation |
|---|---|---|---|---|
| Trait/phenotype | lithoheterotrophy | Energy from oxidation of inorganic electron donors while biomass carbon is taken primarily from organic compounds | METPO:1000648 | (quinn2025characterizingstratifiedmicrobiala pages 20-23, jain2021engineeringlithoheterotrophyin pages 2-4) |
| Trait/phenotype | chemolithoheterotrophy | Synonymous/near-synonymous framing of lithoheterotrophy used in sulfur- and Fe-based systems | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, becker2025evaluationofthiobacillus pages 17-18, zhuang2024electrontransferin pages 5-6) |
| Trait/phenotype | chemolithoautotrophy | Inorganic electron donor oxidation coupled to CO2/HCO3- fixation; key contrasting parent/boundary phenotype | GO:0015976 | (jain2021engineeringlithoheterotrophyin pages 1-2, becker2025evaluationofthiobacillus pages 17-18) |
| Trait/phenotype | chemoorganoheterotrophy | Organic compounds serve as both energy/electron source and carbon source; useful exclusion boundary | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, cui2024proposedminimalstandards pages 2-3) |
| Trait/phenotype | facultative chemolithotrophy / mixotrophy | Boundary case where organisms can switch between or combine lithotrophic and heterotrophic modes | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, becker2025evaluationofthiobacillus pages 17-18, zhuang2024electrontransferin pages 5-6) |
| Electron donors | Fe(II) | Inorganic electron donor supporting Fe-oxidizing lithotrophy/lithoheterotrophy | CHEBI:29033 | (jain2021engineeringlithoheterotrophyin pages 1-2, jain2021engineeringlithoheterotrophyin pages 2-4) |
| Electron donors | sulfide | Reduced sulfur electron donor used in chemolithoheterotrophic denitrification and sulfur oxidation | CHEBI:16199 | (shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2, zhuang2024electrontransferin pages 5-6) |
| Electron donors | thiosulfate | Reduced sulfur electron donor used by sulfur oxidizers; central substrate for Sox-linked oxidation | CHEBI:30087 | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23, dukat2024thiobacteraerophilumsp. pages 1-2) |
| Electron donors | elemental sulfur | Reduced inorganic sulfur electron donor in sulfur oxidizers; intermediate/product in incomplete Sox pathways | CHEBI:26806 | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23, dukat2024thiobacteraerophilumsp. pages 1-2) |
| Electron donors | hydrogen | Inorganic electron donor used by some chemolithotrophs/chemolithoheterotrophs | CHEBI:18276 | (dukat2024thiobacteraerophilumsp. pages 2-4, cui2024proposedminimalstandards pages 2-3) |
| Electron donors | cathode-derived electrons | Electrode can act as inorganic electron donor in electro-fermentation/bioelectrochemical growth contexts | label only | (bartholet2023rationaldesignand pages 54-58, zhuang2024electrontransferin pages 1-3) |
| Electron acceptors | oxygen | Terminal electron acceptor in aerobic or microaerobic Fe(II)/sulfur oxidation | CHEBI:15379 | (jain2021engineeringlithoheterotrophyin pages 1-2, dukat2024thiobacteraerophilumsp. pages 1-2, dukat2024thiobacteraerophilumsp. pages 2-4) |
| Electron acceptors | nitrate | Electron acceptor for denitrifying sulfur oxidation and some Fe(II)-oxidizing systems | CHEBI:17632 | (shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2, becker2025evaluationofthiobacillus pages 1-2) |
| Electron acceptors | nitrite | Alternative oxidized nitrogen acceptor in sulfur-oxidizing systems; intermediate in denitrification | CHEBI:16301 | (shao2025versatilenitraterespiringheterotrophs pages 1-2, zhuang2024electrontransferin pages 5-6) |
| Electron acceptors | fumarate | Electron acceptor in cathode-supported growth example relevant to lithotrophic electron uptake | CHEBI:18012 | (bartholet2023rationaldesignand pages 54-58) |
| Electron acceptors | ferric iron [Fe(III)] | Reported acceptor in some sulfur-cycle and Desulfuromusa-related contexts | CHEBI:29034 | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 20-23) |
| Carbon sources | glucose | Organic carbon source enabling engineered Fe-based lithoheterotrophic growth | CHEBI:17234 | (jain2021engineeringlithoheterotrophyin pages 2-4, jain2021engineeringlithoheterotrophyin pages 4-5) |
| Carbon sources | organic carbon | Generic biomass carbon source required for lithoheterotrophy | CHEBI:63353 | (quinn2025characterizingstratifiedmicrobiala pages 20-23, becker2025evaluationofthiobacillus pages 17-18) |
| Carbon sources | bicarbonate | Inorganic carbon source supporting chemolithoautotrophy; absent in glucose-only lithoheterotrophic assay | CHEBI:17544 | (jain2021engineeringlithoheterotrophyin pages 4-5, dukat2024thiobacteraerophilumsp. pages 1-2) |
| Carbon sources | carbon dioxide | Inorganic carbon source fixed during chemolithoautotrophic growth | CHEBI:16526 | (jain2021engineeringlithoheterotrophyin pages 1-2, dukat2024thiobacteraerophilumsp. pages 1-2) |
| Pathways/modules | Fe(II) oxidation | Core lithotrophic energy-conserving process in Fe-based systems | GO:0019419 | (jain2021engineeringlithoheterotrophyin pages 1-2, jain2021engineeringlithoheterotrophyin pages 2-4) |
| Pathways/modules | sulfide oxidation | Core lithotrophic energy process in sulfur-based chemolithoheterotrophy | GO:0009448 | (shao2025versatilenitraterespiringheterotrophs pages 4-4, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Pathways/modules | thiosulfate oxidation | Sulfur-oxidation module frequently linked to Sox proteins | GO:0009449 | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Pathways/modules | reverse Dsr pathway (rDsr) | Oxidation of sulfur/polysulfide to sulfite in sulfur oxidizers | label only | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Pathways/modules | Sox multienzyme system | Periplasmic sulfur oxidation module for thiosulfate/sulfur compound oxidation | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Pathways/modules | denitrification | Respiratory module coupling nitrate/nitrite reduction to sulfur oxidation in chemolithoheterotrophs | GO:0019362 | (shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2) |
| Pathways/modules | DNRA | Dissimilatory nitrate reduction to ammonium in some associated sulfur/Fe metabolisms | GO:0042128 | (quinn2025characterizingstratifiedmicrobial pages 59-62, shao2025versatilenitraterespiringheterotrophs pages 1-2) |
| Pathways/modules | Calvin cycle / CO2 fixation | Carbon fixation pathway diagnostic for chemolithoautotrophy rather than lithoheterotrophy | GO:0019253 | (dukat2024thiobacteraerophilumsp. pages 1-2, jain2021engineeringlithoheterotrophyin pages 1-2) |
| Pathways/modules | extracellular electron transfer (EET) | Electron transfer to/from extracellular solids or electrodes; relevant possible module in bioelectrochemical lithotrophy | GO:0140935 | (bartholet2023rationaldesignand pages 54-58, zhuang2024electrontransferin pages 1-3) |
| Genes/proteins/complexes | Sqr (sulfide:quinone oxidoreductase) | Key sulfide oxidation enzyme; detoxifies/oxidizes sulfide to elemental sulfur/polysulfide | EC:1.8.5.4 | (shao2025versatilenitraterespiringheterotrophs pages 4-4, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | FccAB (flavocytochrome c sulfide dehydrogenase) | Sulfide oxidation enzyme complex linked to sulfur oxidation | label only | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | SoxB | Sulfur oxidation hydrolase marker within Sox pathway | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | SoxABXYZ | Partial Sox module observed in sulfur oxidizers lacking SoxCD | label only | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) |
| Genes/proteins/complexes | SoxCD | Sox sulfur dehydrogenase components; absence predicts incomplete oxidation and S0 accumulation | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | DsrAB | Core reverse Dsr sulfur oxidation proteins converting S0 toward sulfite | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | DsrJKMOP | Accessory reverse Dsr complex components in oxidative sulfur metabolism | label only | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) |
| Genes/proteins/complexes | DsrL | Oxidative rDsr-associated protein supporting sulfur oxidation directionality | label only | (quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | AprAB/Sat | Sulfite oxidation-associated sulfate activation/APS reductase route in sulfur oxidizers | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | SoeABC | Alternative sulfite oxidation complex to sulfate in oxidative sulfur metabolism | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobiala pages 59-62, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | TsdA / DoxDA | Thiosulfate dehydrogenase components in tetrathionate intermediate pathway | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | TetH | Tetrathionate hydrolase in tetrathionate intermediate sulfur oxidation pathway | label only | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) |
| Genes/proteins/complexes | ETHE1 sulfur dioxygenase | Oxidizes sulfur/polysulfide-derived intermediates to sulfite | label only | (shao2025versatilenitraterespiringheterotrophs pages 4-4) |
| Genes/proteins/complexes | TST (thiosulfate:cyanide sulfurtransferase) | Thiosulfate-related sulfurtransferase reported in sulfur-oxidizing denitrifier MAGs | EC:2.8.1.1 | (shao2025versatilenitraterespiringheterotrophs pages 4-4) |
| Genes/proteins/complexes | NapAB | Periplasmic nitrate reductase module in denitrifying sulfur oxidizers | EC:1.7.99.4 | (quinn2025characterizingstratifiedmicrobiala pages 59-62) |
| Genes/proteins/complexes | NarGHI | Membrane nitrate reductase complex in DNRA/denitrifying contexts | EC:1.7.5.1 | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) |
| Genes/proteins/complexes | NirS / NirK | Nitrite reductases in denitrification; sulfide-sensitive in some systems | EC:1.7.2.1, EC:1.7.2.2 | (quinn2025characterizingstratifiedmicrobiala pages 59-62, shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2) |
| Genes/proteins/complexes | NorBC | Nitric oxide reductase complex in denitrification | EC:1.7.2.5 | (quinn2025characterizingstratifiedmicrobiala pages 59-62, shao2025versatilenitraterespiringheterotrophs pages 4-4) |
| Genes/proteins/complexes | NosZ | Nitrous oxide reductase enabling complete denitrification | EC:1.7.2.4 | (quinn2025characterizingstratifiedmicrobiala pages 59-62, shao2025versatilenitraterespiringheterotrophs pages 4-4, shao2025versatilenitraterespiringheterotrophs pages 1-2) |
| Genes/proteins/complexes | NosR | Accessory/regulatory protein associated with nitrous oxide reductase | label only | (shao2025versatilenitraterespiringheterotrophs pages 4-4) |
| Genes/proteins/complexes | NrfAH | DNRA nitrite reductase module reducing nitrite to ammonium | EC:1.7.2.2 | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) |
| Genes/proteins/complexes | GalP | Glucose symporter introduced to enable glucose uptake in engineered lithoheterotroph | UniProt:P0AEP1 | (jain2021engineeringlithoheterotrophyin pages 2-4) |
| Genes/proteins/complexes | Glk | Glucokinase introduced to phosphorylate imported glucose | EC:2.7.1.2 | (jain2021engineeringlithoheterotrophyin pages 2-4) |
| Genes/proteins/complexes | Mtr pathway / MtrABC | Candidate reversed extracellular electron transfer conduit in cathode-supported metabolism; uncertain for lithoheterotrophy curation | label only | (bartholet2023rationaldesignand pages 54-58) |
| Genes/proteins/complexes | conductive pili / c-type cytochromes | Structures implicated in direct interspecies or extracellular electron transfer | GO:0046930 | (zhuang2024electrontransferin pages 1-3) |
| Environmental/experimental factors | microaerobic conditions | Low-O2 regime required for many Fe(II)-oxidizers because high O2 abiotically oxidizes Fe(II) | ENVO:01000750 | (jain2021engineeringlithoheterotrophyin pages 1-2) |
| Environmental/experimental factors | low oxygen / anoxia | Favors rDsr-linked sulfur oxidation and denitrification in some systems | ENVO:01000331, ENVO:01000254 | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) |
| Environmental/experimental factors | acidic hot spring | Example source environment for sulfur-oxidizing chemolithotrophs; contextual habitat | ENVO:00000051 | (dukat2024thiobacteraerophilumsp. pages 1-2) |
| Environmental/experimental factors | serpentinizing spring | Geochemical environment associated with sulfur oxidizers and lithotrophic community members | ENVO:01000222 | (jain2021engineeringlithoheterotrophyin pages 1-2) |
| Environmental/experimental factors | geothermal biofilm | Community context containing chemolithotrophic/chemolithoheterotrophic responders to thiosulfate | ENVO:01000139 | (dukat2024thiobacteraerophilumsp. pages 1-2) |
| Environmental/experimental factors | glucose-supplemented bicarbonate-free medium | Assay condition selecting for lithoheterotrophic growth in engineered Fe oxidizer | label only | (jain2021engineeringlithoheterotrophyin pages 4-5) |
| Environmental/experimental factors | nitrate-replete conditions | Required for denitrifying chemolithoheterotrophic sulfur oxidation | label only | (shao2025versatilenitraterespiringheterotrophs pages 1-2, becker2025evaluationofthiobacillus pages 1-2) |
| Environmental/experimental factors | cathode poised as electron donor | Bioelectrochemical condition enabling electrode-driven electron uptake | label only | (bartholet2023rationaldesignand pages 54-58) |
| Assays/measurements | ferrozine Fe(II) assay | Colorimetric assay used to quantify Fe(II) oxidation over time | label only | (jain2021engineeringlithoheterotrophyin pages 4-5) |
| Assays/measurements | cell counts by microscopy | Direct counting of stained cells to measure growth/yield in Fe-based assays | label only | (jain2021engineeringlithoheterotrophyin pages 4-5) |
| Assays/measurements | flow cytometry | Used for growth quantification in Fe(II)-oxidizer isolation experiments | label only | (becker2025isolationof‘candidatus pages 4-5) |
| Assays/measurements | sulfur species depletion measurements | Analytical monitoring of sulfide/thiosulfate/sulfur consumption during growth | label only | (dukat2024thiobacteraerophilumsp. pages 2-4) |
| Assays/measurements | nitrate/nitrite measurements | Tracks denitrification or DNRA coupled to lithotrophic metabolism | label only | (becker2025evaluationofthiobacillus pages 1-2, becker2025evaluationofthiobacillus pages 2-4) |
| Assays/measurements | DNA-SIP with 13C-organic vs 13C-inorganic labels | Distinguishes heterotrophic organic-C assimilation from inorganic-C fixation in chemolithoheterotrophs | label only | (shao2025versatilenitraterespiringheterotrophs pages 1-2) |


*Table: This table lists evidence-supported candidate nodes for curating a TraitMech causal graph of the lithoheterotrophic trait. It groups phenotype, substrates, pathways, genes, conditions, and assay nodes, with suggested ontology groundings where possible.*

### Evidence-backed causal edges (candidate triples)
The following artifact provides **candidate edges** with supporting snippets, DOI/URL when available, and uncertainty flags.

| Subject node | Predicate | Object node | Mechanistic rationale/notes | Evidence snippet (short quote) | Source (DOI, year, URL if available) | Citation context id | Uncertainty |
|---|---|---|---|---|---|---|---|
| GalP | enables import of | glucose | Engineered expression of the E. coli glucose symporter supplies uptake capacity needed for glucose use in the Fe(II)-oxidizer. | "introducing E. coli galP and glk on plasmid pGlu to enable glucose uptake and phosphorylation" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 2-4) | low |
| Glk | phosphorylates | glucose | Introduced glucokinase provides the first intracellular step of glucose utilization after import. | "introducing E. coli galP and glk on plasmid pGlu to enable glucose uptake and phosphorylation" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 2-4) | low |
| Fe(II) oxidation | provides energy for | lithoheterotrophic growth | In the engineered strain, inorganic Fe(II) oxidation remained the energy metabolism while glucose supplied carbon. | "Fe(II) oxidation) provides energy while organic carbon serves primarily as the carbon source" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 2-4) | low |
| glucose | serves as carbon source for | engineered lithoheterotrophic growth | The transformed strain used glucose instead of CO2 for biomass production under Fe-oxidizing conditions. | "grew lithoheterotrophically: i.e., under Fe(II)-oxidizing conditions with glucose as the sole carbon source and no added CO2" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 2-4) | low |
| empty vector control | fails to enable | growth on glucose | Negative control shows glucose use depends on the engineered functions rather than native metabolism. | "Controls with empty vector could not grow on glucose" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 2-4) | low |
| absence of bicarbonate in medium | forces reliance on | organic carbon assimilation | Bicarbonate-free, glucose-amended medium operationally excludes inorganic carbon supply in the assay. | "for glucose-dependent growth ASW lacking bicarbonate with 500 µM glucose" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 4-5) | medium |
| microaerobic conditions | support | Fe(II)-oxidizing growth | Low O2 is required because high atmospheric O2 oxidizes Fe(II) abiotically and prevents the biological niche. | "requiring microaerobic conditions because atmospheric O2 abiotically oxidizes Fe(II)" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 1-2) | low |
| Fe(II) oxidation | is coupled to reduction of | oxygen | The defining Fe-based chemolithotrophic metabolism uses Fe(II) as donor and O2 as acceptor. | "the oxidation of Fe(II) coupled to the reduction of oxygen while fixing carbon dioxide" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 1-2) | low |
| glucose availability | increases cell yield per unit of | Fe(II) oxidized | Similar final cell densities with less total Fe(II) oxidized imply more biomass formed per Fe oxidized. | "oxidized less total Fe(II) on glucose despite reaching similar final cell densities, implying higher cell yield per Fe(II) oxidized" | 10.1038/s41598-021-81412-3, 2021, https://doi.org/10.1038/s41598-021-81412-3 | (jain2021engineeringlithoheterotrophyin pages 2-4) | medium |
| sulfide:quinone oxidoreductase (SQR) | catalyzes oxidation/detoxification of | sulfide | SQR is explicitly identified as a key sulfide oxidation enzyme in nitrate-reducing chemolithotrophs/heterotrophs. | "a key enzyme that can catalyze sulfide detoxification in nitrate-reducing chemolithoautotrophs" | 10.1038/s41467-025-56588-1, 2025, https://doi.org/10.1038/s41467-025-56588-1 | (shao2025versatilenitraterespiringheterotrophs pages 4-4) | low |
| periplasmic sox genes | encode oxidation of | thiosulfate | The sox cluster is directly described as encoding thiosulfate oxidation. | "periplasmic sox gene clusters encoding for thiosulfate oxidation" | 10.1038/s41467-025-56588-1, 2025, https://doi.org/10.1038/s41467-025-56588-1 | (shao2025versatilenitraterespiringheterotrophs pages 4-4) | low |
| SoxXYZABCD complex | enables complete oxidation of | thiosulfate | Full Sox complement is required for complete thiosulfate oxidation in sulfur oxidizers. | "Complete thiosulfate oxidation requires the full SoxXYZABCD complex" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) | medium |
| absence of SoxCD | causes accumulation of | S0 | Incomplete Sox systems lacking SoxCD are linked to sulfur intermediate accumulation. | "absence of SoxCD or low pH leads to S0 accumulation" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) | medium |
| reverse Dsr pathway (DsrAB) | oxidizes | S0 to sulfite | DsrAB is described as the core oxidative step in rDsr sulfur oxidation. | "The first step of this pathway involves the oxidation of S0 to sulfite by DsrAB" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) | low |
| SoeABC | oxidizes | sulfite to sulfate | Evidence indicates SoeABC can perform the sulfite-to-sulfate step in oxidative sulfur metabolism. | "the oxidation of sulfite to sulphate which can be carried out by AprAB-Sat proteins or the SoeABC complex" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23) | low |
| fccAB | oxidizes | sulfide to S0 | Flavocytochrome c sulfide dehydrogenase is listed among the enzymes for sulfide oxidation to elemental sulfur. | "sqr and fccAB (oxidation of sulfide to S0)" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) | low |
| napAB + nirS + norB + nosZ | enable coupling of | sulfur oxidation to denitrification | Near-complete denitrification modules co-occur with sulfur oxidation pathways in sulfur oxidizers. | "a near-complete denitrification module (napAB, nirS, norB, nosZ) are present... enabling coupling of sulfur oxidation (rDsr) to both aerobic respiration and denitrification" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) | low |
| nrfAH | enables | DNRA | nrfAH is directly identified as part of the DNRA module. | "narGHI and nrfAH for DNRA" | 2025 thesis/book context, URL unavailable | (quinn2025characterizingstratifiedmicrobial pages 59-62, quinn2025characterizingstratifiedmicrobiala pages 59-62) | low |
| sulfide | inhibits | NirK | This explains why sulfide can suppress denitrification performance and promote greenhouse gas release. | "sulfide strongly inhibits the copper-dependent metalloenzymes nitrite reductase (NirK)" | 10.1038/s41467-025-56588-1, 2025, https://doi.org/10.1038/s41467-025-56588-1 | (shao2025versatilenitraterespiringheterotrophs pages 1-2) | low |
| sulfide | inhibits | NosZ | Inhibition of NosZ mechanistically links sulfidic conditions to incomplete denitrification and N2O accumulation. | "sulfide strongly inhibits the copper-dependent metalloenzymes... N2O reductase (NosZ)" | 10.1038/s41467-025-56588-1, 2025, https://doi.org/10.1038/s41467-025-56588-1 | (shao2025versatilenitraterespiringheterotrophs pages 1-2) | low |
| conductive pili and outer-surface c-type cytochromes | enable | direct interspecies electron transfer (DIET) | The sulfur-cycle EET review explicitly attributes DIET to pili/cytochrome-mediated cell-cell conduction. | "direct interspecies electron transfer (DIET) via conductive pili... and outer-surface c-type cytochromes" | 10.3390/life14050591, 2024, https://doi.org/10.3390/life14050591 | (zhuang2024electrontransferin pages 1-3) | low |
| cathode-derived electrons | enable | fumarate reduction to succinate in Geobacter sulfurreducens | Demonstrates that an inorganic electron source can drive respiratory metabolism in electrode-linked systems. | "G. sulfurreducens grew and reduced fumarate to succinate with a cathode as the sole electron donor" | 2023 dissertation/review context, URL unavailable | (bartholet2023rationaldesignand pages 54-58) | low |
| Mtr pathway (reverse operation) | may mediate | cathodic electron transfer in Shewanella | The source presents this as a proposed mechanism and notes that reversibility is contested. | "Ross et al. showed cathodic electron transfer in Shewanella potentially via the Mtr pathway in reverse" | 2023 dissertation/review context, URL unavailable | (bartholet2023rationaldesignand pages 54-58) | high |
| nitrate availability | supports | chemolithoheterotrophic denitrifier growth on sulfide | DNA-SIP/microcosm evidence shows nitrate starvation suppresses the sulfur-linked heterotrophic denitrifier response. | "nitrate starvation suppressed these increases" | 10.1038/s41467-025-56588-1, 2025, https://doi.org/10.1038/s41467-025-56588-1 | (shao2025versatilenitraterespiringheterotrophs pages 1-2) | medium |
| organic 13C substrates | are assimilated by | facultative sulfur-oxidizing heterotrophic denitrifiers | Organic-label enrichment, together with weak inorganic-label incorporation, supports heterotrophic carbon assimilation in these chemolithoheterotrophs. | "13Co labeling increased relative abundances... whereas 13Ci decreased them" | 10.1038/s41467-025-56588-1, 2025, https://doi.org/10.1038/s41467-025-56588-1 | (shao2025versatilenitraterespiringheterotrophs pages 1-2) | medium |


*Table: This table lists candidate subject-predicate-object edges for a lithoheterotrophic TraitMech graph, each tied to a short supporting snippet and source. It is useful for selecting high-confidence curatable mechanisms while flagging inferred or taxon-specific links as uncertain.*

### Relevant quantitative statistics and data (recent studies in retrieved corpus)
- **Nitrate-reducing Fe(II) oxidation (NRFeOx) assay metrics**: In Fe(II)/nitrate medium, *Thiobacillus denitrificans* oxidized **42% of 10 mM Fe(II)** and reduced **54% of 3.5 mM nitrate**, accumulating **1.6 mM nitrite**, yet showed **no cell growth** (indicating Fe(II) oxidation can occur without supporting autotrophic growth under those conditions). A kinetic model estimated ~**70% enzymatic** vs ~**30% abiotic** Fe(II) oxidation within 22 days. (becker2025evaluationofthiobacillus pages 1-2)
- **Fe(II) oxidation rate comparison**: The overall Fe(II) oxidation rate for *T. denitrificans* was reported at ~**0.5 mM day−1**, ~4× slower than referenced mixotrophic NRFeOx cultures (~2 mM day−1). (becker2025evaluationofthiobacillus pages 8-9)
- **Microaerophilic Fe(II)-oxidizer doubling time**: ‘*Candidatus Ferrigenium straubiae*’ strain KS shows a doubling time of **16 h** at 20 °C and pH 6.5 in Fe(II)-O2 gradient culture conditions (autotrophic microaerophilic Fe oxidation). (becker2025isolationof‘candidatus pages 1-2)

### Expert opinions / authoritative analysis in sources
- **SOB metabolic categories**: The 2024 review frames SOB into obligate chemolithotrophs, facultative chemolithotrophs, and chemolithoheterotrophs, and explicitly separates electron donors (sulfide, thiosulfate, elemental sulfur) from electron acceptors (including nitrate/nitrite), reinforcing that trophic type is not determined by electron acceptor choice. (zhuang2024electrontransferin pages 5-6)
- **Mechanistic emphasis on electron transfer**: The sulfur-cycle electron transfer review emphasizes DIET mechanisms via pili/cytochromes and recognizes long-distance electron transfer in filamentous/cable bacteria, supporting inclusion of EET modules as optional subgraphs when lithoheterotrophy is community- or electrode-associated. (zhuang2024electrontransferin pages 1-3)

### Visual evidence
Figures extracted from Jain & Gralnick (2021) show **growth** and **Fe(II) oxidation kinetics** under glucose (bicarbonate-free) vs CO2 conditions, supporting the operational definition of an engineered lithoheterotrophic phenotype (growth with inorganic electron donor dependence plus organic carbon assimilation). (jain2021engineeringlithoheterotrophyin media 6418b038, jain2021engineeringlithoheterotrophyin media 51228eff)

---

## DOI-first bibliography (with dates/URLs when available)
1. Zhuang X, Wang S, Wu S. **Electron Transfer in the Biogeochemical Sulfur Cycle**. *Life*. **2024-05**. DOI: **10.3390/life14050591**. URL: https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 1-3, zhuang2024electrontransferin pages 5-6)
2. Dukat AM, Elcheninov AG, Klyukina AA, Novikov AA, Frolov EN. **Thiobacter aerophilum sp. nov., a Thermophilic, Obligately Chemolithoautotrophic, Sulfur-Oxidizing Bacterium…** *Microorganisms*. **2024-11**. DOI: **10.3390/microorganisms12112252**. URL: https://doi.org/10.3390/microorganisms12112252 (dukat2024thiobacteraerophilumsp. pages 1-2)
3. Cui H-L, Hou J, Amoozegar MA, et al. **Proposed minimal standards for description of new taxa of the class Halobacteria**. *IJSEM*. **2024-03**. DOI: **10.1099/ijsem.0.006290**. URL: https://doi.org/10.1099/ijsem.0.006290 (cui2024proposedminimalstandards pages 2-3)
4. Trutschel LR, Kruger BR, Sackett JD, Chadwick GL, Rowe AR. **Determining resident microbial community members and their correlations with geochemistry in a serpentinizing spring**. *Frontiers in Microbiology*. **2023-06**. DOI: **10.3389/fmicb.2023.1182497**. URL: https://doi.org/10.3389/fmicb.2023.1182497 (jain2021engineeringlithoheterotrophyin pages 1-2)
5. Kostešić E, Mitrović M, Kajan K, et al. **Microbial Diversity and Activity of Biofilms from Geothermal Springs in Croatia**. *Microbial Ecology*. **2023-05**. DOI: **10.1007/s00248-023-02239-1**. URL: https://doi.org/10.1007/s00248-023-02239-1 (shao2025versatilenitraterespiringheterotrophs pages 1-2)
6. Jain A, Gralnick JA. **Engineering lithoheterotrophy in an obligate chemolithoautotrophic Fe(II) oxidizing bacterium**. *Scientific Reports*. **2021**. DOI: **10.1038/s41598-021-81412-3**. URL: https://doi.org/10.1038/s41598-021-81412-3 (jain2021engineeringlithoheterotrophyin pages 2-4, jain2021engineeringlithoheterotrophyin pages 4-5, jain2021engineeringlithoheterotrophyin pages 1-2, jain2021engineeringlithoheterotrophyin media 6418b038, jain2021engineeringlithoheterotrophyin media 51228eff)

Additional quantitative/physiology references (outside 2023–2024 window but used for data points in this retrieval set):
- Becker S, Dang TT, Wei R, Kappler A. *FEMS Microbiology Ecology*. **2025-03**. DOI: **10.1093/femsec/fiaf024**. URL: https://doi.org/10.1093/femsec/fiaf024 (becker2025evaluationofthiobacillus pages 8-9, becker2025evaluationofthiobacillus pages 1-2)
- Becker S, Kappler A. *IJSEM*. **2025-11**. DOI: **10.1099/ijsem.0.006949**. URL: https://doi.org/10.1099/ijsem.0.006949 (becker2025isolationof‘candidatus pages 1-2)

---

## Curation warnings (claims not yet safe to curate)
1. **Electrode/cathode → lithoheterotrophy linkage is indirect in current evidence**: The retrieved source demonstrates cathode-driven electron donation and respiration (Geobacter, Shewanella), but does not directly demonstrate organic-carbon-dependent biomass synthesis under those conditions; curate EET edges as optional/conditional subgraph. (bartholet2023rationaldesignand pages 54-58, zhuang2024electrontransferin pages 1-3)
2. **Reverse Mtr in Shewanella is contested**: Treat Mtr-reversal as **high-uncertainty** until confirmed by primary mechanistic studies in the target taxon/assay. (bartholet2023rationaldesignand pages 54-58)
3. **Sox completeness → S0 accumulation** is supported in a synthesis-style source in this retrieval set; consider confirming with a primary enzymology/genetics paper before encoding as a hard mechanistic rule in TraitMech. (quinn2025characterizingstratifiedmicrobiala pages 20-23, quinn2025characterizingstratifiedmicrobial pages 20-23)
4. **Field/metagenomic inference of lithoheterotrophy**: Many 2023–2024 environmental studies infer trophic modes from annotations/geochemistry; curate only when carbon source evidence (e.g., SIP or controlled substrate tests) is present. (jain2021engineeringlithoheterotrophyin pages 1-2, shao2025versatilenitraterespiringheterotrophs pages 1-2)


References

1. (quinn2025characterizingstratifiedmicrobiala pages 20-23): MW Quinn. Characterizing stratified microbial communities and a novel polyextremophilic chemolithoautotroph from hypersaline cold sulfur springs in the canadian high arctic. Unknown journal, 2025.

2. (jain2021engineeringlithoheterotrophyin pages 1-2): A Jain and JA Gralnick. Engineering lithoheterotrophy in an obligate chemolithoautotrophic fe (ii) oxidizing bacterium. Unknown journal, 2021.

3. (zhuang2024electrontransferin pages 5-6): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

4. (zhuang2024electrontransferin pages 1-3): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

5. (cui2024proposedminimalstandards pages 2-3): Heng-Lin Cui, Jing Hou, Mohammad Ali Amoozegar, Mike L. Dyall-Smith, Rafael R. de la Haba, Hiroaki Minegishi, Rafael Montalvo-Rodriguez, Aharon Oren, Cristina Sanchez-Porro, Antonio Ventosa, and Russell H. Vreeland. Proposed minimal standards for description of new taxa of the class halobacteria. Mar 2024. URL: https://doi.org/10.1099/ijsem.0.006290, doi:10.1099/ijsem.0.006290. This article has 44 citations and is from a peer-reviewed journal.

6. (bartholet2023rationaldesignand pages 54-58): D Bartholet. Rational design and novel bioprocesses for low-carbon biofuels and bioproducts. Unknown journal, 2023.

7. (shao2025versatilenitraterespiringheterotrophs pages 1-2): Bo Shao, Yuan-Guo Xie, Long Zhang, Yang Ruan, Bin Liang, Ruochen Zhang, Xijun Xu, Wei Wang, Zhengda Lin, Xuanyuan Pei, Xueting Wang, Lei Zhao, Xu Zhou, Xiaohui Wu, Defeng Xing, Aijie Wang, Duu-Jong Lee, Nanqi Ren, Donald E. Canfield, Brian P. Hedlund, Zheng-Shuang Hua, and Chuan Chen. Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56588-1, doi:10.1038/s41467-025-56588-1. This article has 30 citations and is from a highest quality peer-reviewed journal.

8. (jain2021engineeringlithoheterotrophyin pages 2-4): A Jain and JA Gralnick. Engineering lithoheterotrophy in an obligate chemolithoautotrophic fe (ii) oxidizing bacterium. Unknown journal, 2021.

9. (becker2025evaluationofthiobacillus pages 17-18): Stefanie Becker, Thu Trang Dang, Ran Wei, and Andreas Kappler. Evaluation of <i>thiobacillus denitrificans</i>’ sustainability in nitrate-reducing fe(ii) oxidation and the potential significance of fe(ii) as a growth-supporting reductant. FEMS Microbiology Ecology, Mar 2025. URL: https://doi.org/10.1093/femsec/fiaf024, doi:10.1093/femsec/fiaf024. This article has 6 citations and is from a peer-reviewed journal.

10. (shao2025versatilenitraterespiringheterotrophs pages 4-4): Bo Shao, Yuan-Guo Xie, Long Zhang, Yang Ruan, Bin Liang, Ruochen Zhang, Xijun Xu, Wei Wang, Zhengda Lin, Xuanyuan Pei, Xueting Wang, Lei Zhao, Xu Zhou, Xiaohui Wu, Defeng Xing, Aijie Wang, Duu-Jong Lee, Nanqi Ren, Donald E. Canfield, Brian P. Hedlund, Zheng-Shuang Hua, and Chuan Chen. Versatile nitrate-respiring heterotrophs are previously concealed contributors to sulfur cycle. Nature Communications, Jan 2025. URL: https://doi.org/10.1038/s41467-025-56588-1, doi:10.1038/s41467-025-56588-1. This article has 30 citations and is from a highest quality peer-reviewed journal.

11. (quinn2025characterizingstratifiedmicrobial pages 20-23): MW Quinn. Characterizing stratified microbial communities and a novel polyextremophilic chemolithoautotroph from hypersaline cold sulfur springs in the canadian high arctic. Unknown journal, 2025.

12. (dukat2024thiobacteraerophilumsp. pages 1-2): Anna M. Dukat, Alexander G. Elcheninov, Alexandra A. Klyukina, Andrei A. Novikov, and Evgenii N. Frolov. Thiobacter aerophilum sp. nov., a thermophilic, obligately chemolithoautotrophic, sulfur-oxidizing bacterium from a hot spring and proposal of thiobacteraceae fam. nov. Microorganisms, 12:2252, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112252, doi:10.3390/microorganisms12112252. This article has 4 citations.

13. (dukat2024thiobacteraerophilumsp. pages 2-4): Anna M. Dukat, Alexander G. Elcheninov, Alexandra A. Klyukina, Andrei A. Novikov, and Evgenii N. Frolov. Thiobacter aerophilum sp. nov., a thermophilic, obligately chemolithoautotrophic, sulfur-oxidizing bacterium from a hot spring and proposal of thiobacteraceae fam. nov. Microorganisms, 12:2252, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112252, doi:10.3390/microorganisms12112252. This article has 4 citations.

14. (becker2025evaluationofthiobacillus pages 1-2): Stefanie Becker, Thu Trang Dang, Ran Wei, and Andreas Kappler. Evaluation of <i>thiobacillus denitrificans</i>’ sustainability in nitrate-reducing fe(ii) oxidation and the potential significance of fe(ii) as a growth-supporting reductant. FEMS Microbiology Ecology, Mar 2025. URL: https://doi.org/10.1093/femsec/fiaf024, doi:10.1093/femsec/fiaf024. This article has 6 citations and is from a peer-reviewed journal.

15. (quinn2025characterizingstratifiedmicrobial pages 59-62): MW Quinn. Characterizing stratified microbial communities and a novel polyextremophilic chemolithoautotroph from hypersaline cold sulfur springs in the canadian high arctic. Unknown journal, 2025.

16. (jain2021engineeringlithoheterotrophyin pages 4-5): A Jain and JA Gralnick. Engineering lithoheterotrophy in an obligate chemolithoautotrophic fe (ii) oxidizing bacterium. Unknown journal, 2021.

17. (quinn2025characterizingstratifiedmicrobiala pages 59-62): MW Quinn. Characterizing stratified microbial communities and a novel polyextremophilic chemolithoautotroph from hypersaline cold sulfur springs in the canadian high arctic. Unknown journal, 2025.

18. (becker2025isolationof‘candidatus pages 4-5): Stefanie Becker and Andreas Kappler. Isolation of ‘candidatus ferrigenium straubiae’ – a microaerophilic fe(ii)-oxidizing bacterium and nitrate-reducing fe(ii)-oxidizer within the community of culture ks. International Journal of Systematic and Evolutionary Microbiology, Nov 2025. URL: https://doi.org/10.1099/ijsem.0.006949, doi:10.1099/ijsem.0.006949. This article has 1 citations and is from a peer-reviewed journal.

19. (becker2025evaluationofthiobacillus pages 2-4): Stefanie Becker, Thu Trang Dang, Ran Wei, and Andreas Kappler. Evaluation of <i>thiobacillus denitrificans</i>’ sustainability in nitrate-reducing fe(ii) oxidation and the potential significance of fe(ii) as a growth-supporting reductant. FEMS Microbiology Ecology, Mar 2025. URL: https://doi.org/10.1093/femsec/fiaf024, doi:10.1093/femsec/fiaf024. This article has 6 citations and is from a peer-reviewed journal.

20. (becker2025evaluationofthiobacillus pages 8-9): Stefanie Becker, Thu Trang Dang, Ran Wei, and Andreas Kappler. Evaluation of <i>thiobacillus denitrificans</i>’ sustainability in nitrate-reducing fe(ii) oxidation and the potential significance of fe(ii) as a growth-supporting reductant. FEMS Microbiology Ecology, Mar 2025. URL: https://doi.org/10.1093/femsec/fiaf024, doi:10.1093/femsec/fiaf024. This article has 6 citations and is from a peer-reviewed journal.

21. (becker2025isolationof‘candidatus pages 1-2): Stefanie Becker and Andreas Kappler. Isolation of ‘candidatus ferrigenium straubiae’ – a microaerophilic fe(ii)-oxidizing bacterium and nitrate-reducing fe(ii)-oxidizer within the community of culture ks. International Journal of Systematic and Evolutionary Microbiology, Nov 2025. URL: https://doi.org/10.1099/ijsem.0.006949, doi:10.1099/ijsem.0.006949. This article has 1 citations and is from a peer-reviewed journal.

22. (jain2021engineeringlithoheterotrophyin media 6418b038): A Jain and JA Gralnick. Engineering lithoheterotrophy in an obligate chemolithoautotrophic fe (ii) oxidizing bacterium. Unknown journal, 2021.

23. (jain2021engineeringlithoheterotrophyin media 51228eff): A Jain and JA Gralnick. Engineering lithoheterotrophy in an obligate chemolithoautotrophic fe (ii) oxidizing bacterium. Unknown journal, 2021.