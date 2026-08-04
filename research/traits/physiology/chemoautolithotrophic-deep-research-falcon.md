---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:45:09.692771'
end_time: '2026-08-04T10:51:16.452711'
duration_seconds: 366.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoautolithotrophic
  trait_identifier: METPO:1000634
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoautolithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses chemical oxidation of inorganic
    compounds as the energy source and carbon dioxide as the primary carbon source
    for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: chemoautolithotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms
    or molecules (Review supports inorganic compound oxidation as lithotrophic energy
    metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview
    supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485:
    Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation
    as a chemolithoautotrophic example.)'
  causal_graph_summary: 'chemoautolithotrophic_inorganic_energy_co2_fixation: 11 nodes,
    12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000634
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses chemical oxidation of inorganic compounds as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as a chemolithoautotrophic example.)
- **Existing causal graph summary:** chemoautolithotrophic_inorganic_energy_co2_fixation: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **chemoautolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautolithotrophic.yaml`.

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
- **Trait label:** chemoautolithotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000634
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses chemical oxidation of inorganic compounds as the energy source and carbon dioxide as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautolithotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Minireview supports microbial carbon dioxide fixation pathways.) | DOI:10.1146/annurev.micro.55.1.485: Chemolitho-autotrophic ammonia-oxidizing bacteria (Review supports ammonia oxidation as a chemolithoautotrophic example.)
- **Existing causal graph summary:** chemoautolithotrophic_inorganic_energy_co2_fixation: 11 nodes, 12 edges

## Research Objective

Research the microbial trait **chemoautolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautolithotrophic.yaml`.

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


# Curation report: chemoautolithotrophic

**Trait:** chemoautolithotrophic  
**Identifier:** `METPO:1000634`  
**Category/kind/status:** PHYSIOLOGY / CLASS / REVIEWED

## 1. Scope and current interpretation

`METPO:1000634` denotes a trophic phenotype in which chemical oxidation of an inorganic electron donor supplies energy and reductant, while CO2 or HCO3− supplies the principal carbon incorporated into biomass. “Chemolithoautotrophic” is the more common literature spelling; “chemoautolithotrophic” and “chemoautolithotroph” are defensible ontology labels/synonyms. Recent authors operationalize the phenotype through growth with an inorganic donor plus inorganic carbon, donor consumption/product formation, and preferably ^13CO2/^13C-bicarbonate incorporation—not merely by finding marker genes. For example, a 2023 hydrothermal study measured active fixation using ^13C-NaHCO3 across 30–65°C incubations, while a 2024 Sulfurospirillum study combined culture phenotype with hydrogenase, Sox, and rTCA genes. (wang2024novelisolatesof pages 12-15, deng2023strategiesofchemolithoautotrophs pages 1-2)

A minimal causal abstraction is:

**inorganic electron donor oxidation → electron transfer/energy conservation → ATP and reducing equivalents → inorganic-carbon fixation → biomass synthesis.**

This abstraction should be the graph’s conserved core. Donor-specific oxidation systems, terminal acceptors, electron-transfer chains, and carbon-fixation pathways should be represented as alternative, taxon-qualified modules rather than asserted as universal.

### Boundary cases

- **Photolithoautotrophy:** also uses inorganic donors and inorganic carbon, but light—not chemical oxidation—is the primary energy source. Exclude from this trait.
- **Chemoorganoheterotrophy:** both electrons/energy and carbon are obtained mainly from organic compounds. Exclude.
- **Chemolithoheterotrophy:** inorganic oxidation supplies energy, but organic carbon is required or predominant. Do not infer `METPO:1000634` from lithotrophy alone.
- **Chemoorganoautotrophy:** inorganic carbon is fixed, but an organic compound supplies the relevant electrons/energy. It satisfies autotrophy but not lithotrophy.
- **Mixotrophy:** simultaneous or conditional use of inorganic and organic carbon. It may coexist with a chemolithoautotrophic capacity, but environmental activity should not automatically be annotated as strict chemolithoautotrophy. In sulfur-stimulated groundwater, active mixotrophs—not strict autotrophs—were most abundant and replaced 43% and 80% of microbial carbon with ^13C after 21 and 70 days, respectively. (taubert2022bolsteringfitnessvia pages 6-7)
- **Electroautotrophy:** electrode electrons plus CO2 fixation are mechanistically adjacent but the electrode is not conventionally an inorganic chemical compound. A 2024 comparison found distinct extracellular-electron-uptake phenotypes and 493 differentially expressed genes relative to Fe2+-based chemoautotrophy. Treat electroautotrophy as a sibling or experimental variant, not an unqualified instance of `METPO:1000634`. (wang2024characterizethegrowth pages 22-23, wang2024characterizethegrowth pages 1-2)
- **Methanotrophy:** CH4 is commonly classified as an organic one-carbon compound; therefore methane oxidation plus CO2 assimilation should not be used as a clean lithotrophy example despite occasional broad “reduced compound” terminology.
- **Genomic potential:** genes such as `rbcL`, `aclAB`, `sox`, or hydrogenases establish potential, not the complete phenotype. Curate the trait most strongly when growth, donor oxidation, and inorganic-carbon assimilation are jointly demonstrated.

## 2. Candidate causal-graph nodes

### Trait and phenotype nodes

- `METPO:1000634` — chemoautolithotrophic.
- Chemoautolithotrophic growth; autotrophic biomass production; dark CO2 fixation.
- Growth with inorganic donor and CO2/HCO3− as principal or sole carbon source.
- Experimental readouts: growth yield/doubling, donor depletion, oxidized product accumulation, O2 or nitrate consumption, Rubisco activity, and ^13CO2/^13C-HCO3− incorporation.

### Environmental and experimental factors

- Availability and concentration of H2, NH3/NH4+, NO2−, H2S/HS−, elemental sulfur, thiosulfate, Fe2+, CO, or phosphite.
- CO2/HCO3− concentration; organic-carbon exclusion or limitation.
- O2, nitrate/nitrite, sulfate, CO2, or other taxon-specific terminal electron acceptors.
- Redox potential, pH, temperature, salinity, donor/acceptor gradients, and trace metals.
- Microoxic conditions and oxic–anoxic interfaces, hydrothermal vents, serpentinizing systems, groundwater, mine drainage, sediments, biofilms, and engineered reactors.
- Acid stress and temperature are modifiers, not defining conditions. Campylobacterales fixed carbon at pH 5.6 and 2.2 at 30–45°C, whereas Nautiliales fixation increased from 45 to 65°C under moderately acidic conditions. (deng2023strategiesofchemolithoautotrophs pages 1-2)

### Chemicals and metabolites

Confidently groundable examples include carbon dioxide (`CHEBI:16526`) and molecular hydrogen (`CHEBI:18276`). Other candidate chemicals should be mapped by an ontology lookup during YAML preparation rather than assigning identifiers from memory: bicarbonate, ammonia/ammonium, nitrite, nitrate, sulfide/hydrogen sulfide, elemental sulfur, thiosulfate, sulfate, Fe2+/Fe3+, phosphite/phosphate, O2, NADH/NADPH, quinones, reduced/oxidized ferredoxin, ATP/ADP, acetyl-CoA, pyruvate, and 2-oxoglutarate.

### Donor-oxidation proteins and modules

- Uptake [NiFe]-hydrogenases and associated electron-transfer proteins.
- Ammonia monooxygenase (AMO), hydroxylamine oxidation machinery, and nitrite oxidoreductase (NXR)—important nitrifier modules, but not evidenced sufficiently in the retrieved excerpts for edge-level curation here.
- Sox multienzyme system (`soxABCDYZ`), sulfide:quinone oxidoreductase (SQR), flavocytochrome c sulfide dehydrogenase, and reverse dissimilatory sulfite oxidation modules.
- Cyc2, rusticyanin (Rus), Cyc1, quinones, and terminal oxidases in *Acidithiobacillus ferrooxidans* iron oxidation.
- Carbon monoxide dehydrogenase for CO oxidation; phosphite dehydrogenase for phosphite oxidation.
- Rnf complex, NADH:quinone oxidoreductase, cytochromes, quinones, ferredoxins, proton-translocating complexes, and F-type or A/V-type ATP synthases.

### Carbon acquisition and fixation modules

- CO2/HCO3− transporters, carbonic anhydrase, and carbon-concentrating mechanisms.
- Calvin–Benson–Bassham cycle and Rubisco.
- Reverse/reductive TCA cycle, ATP citrate lyase (`aclAB`), PFOR, OGOR, and low-potential ferredoxins.
- Wood–Ljungdahl/acetyl-CoA pathway, CODH–ACS complex, formate dehydrogenase, and methyl/carbonyl branches.
- 3-hydroxypropionate bicycle and 3-hydroxypropionate/4-hydroxybutyrate cycle.
- Dicarboxylate/4-hydroxybutyrate and other lineage-specific fixation pathways should be added only with direct evidence.

## 3. Evidence-backed candidate edges

The following artifact is a curation-oriented edge inventory. Labels are retained where exact ontology grounding was not verified; identifiers should not be inferred from gene names alone.

| subject | predicate | object | suggested grounding | evidence tier | taxon/context | DOI | short supporting snippet | curation note/uncertainty |
|---|---|---|---|---|---|---|---|---|
| chemoautolithotrophic growth | has_energy_source | inorganic compound oxidation | METPO:1000634; CHEBI label-only: inorganic electron donor | Review + recent study | general definition; hydrothermal vent chemolithotrophs | 10.1186/s40168-023-01712-w | “convert CO2 to organic carbon using energy from oxidizing reduced compounds (H2S, CH4, H2)” (deng2023strategiesofchemolithoautotrophs pages 1-2) | Core definitional edge; CH4-containing wording is broader than strict lithotrophy, so curate as “reduced inorganic compounds” with caution. |
| chemoautolithotrophic growth | has_carbon_source | CO2/HCO3- | METPO:1000634; CHEBI:16526 carbon dioxide; CHEBI:17544 bicarbonate | Review + culture | general; multiple taxa | 10.3390/microorganisms12112252 | “grew by aerobic respiration with sulfide, sulfur, or thiosulfate as the electron donor and HCO3−/CO2 as the carbon source” | Strong phenotype-level edge from obligate sulfur oxidizer; broadly consistent across trait definition. |
| inorganic electron donor oxidation | drives | electron transport chain | GO label-only: electron transport chain | Mechanistic inference from culture/transcriptomics | Acidithiobacillus ferrooxidans Fe2+ oxidation | 10.3390/microorganisms12030590 | “Fe2+ oxidation by outer-membrane cytochrome c (Cyc2) initiates electron flow toward rusticyanin (Rus), then through cytoplasm cytochrome c (Cyc1)” (wang2024characterizethegrowth pages 1-2) | Core causal chain is strong, but the exact ETC architecture is taxon-specific. |
| electron transport chain | generates | ATP / proton motive force | GO label-only: ATP biosynthetic process; proton motive force | Mechanistic inference | Acidithiobacillus ferrooxidans | 10.3390/microorganisms12030590 | “via downhill pathways to generate ATP” (wang2024characterizethegrowth pages 1-2) | Use as a generic energy-conservation edge; proton motive force is implied rather than directly measured here. |
| ATP / reducing power | enables | CO2 fixation | GO label-only: carbon fixation | Mechanistic synthesis | general | 10.3390/life13030627 | “energetically unfavorable reactions that require a strong reduction potential” (PFOR/OGOR-driven carboxylations) (prioretti2023carbonfixationin pages 16-17) | Strong for reductant requirement; ATP requirement depends on pathway and is generalized here. |
| CO2 fixation pathway | contributes_to | biomass synthesis | GO label-only: autotrophic growth / biomass synthesis | Culture + reactor + SIP | general | 10.1111/1462-2920.16470 | “allowing for nearly complete assimilation of the substrate electrons into bacterial biomass” (mao2023anaerobicdissimilatoryphosphite pages 5-5) | Broad endpoint edge; exact biomass yield is pathway- and taxon-dependent. |
| H2 | is_electron_donor_for | hydrogen-oxidizing chemolithoautotrophy | CHEBI:18276 molecular hydrogen | Culture + genomics | Sulfurospirillum sp. strain 1612 | 10.1128/msystems.00148-24 | “strain 1612… as chemolithoautotrophic using H2 and sulfur compounds” (wang2024novelisolatesof pages 12-15) | Strong strain-specific phenotype edge. |
| [NiFe]-hydrogenase | oxidizes | H2 | EC/UniProt not assigned; label-only [NiFe]-hydrogenase | Genomics + physiological context | Sulfurospirillum sp. strain 1612; Aquifex aeolicus | 10.1128/msystems.00148-24 | “possesses diverse [NiFe]-hydrogenase subgroups… for H2 oxidation and uptake” (wang2024novelisolatesof pages 12-15) | Strong but gene-to-reaction evidence is genomic/physiological, not purified biochemistry in this strain. |
| hydrogen oxidation | supplies electrons for | rTCA carbon fixation | GO label-only: reverse tricarboxylic acid cycle | Culture + comparative physiology | Campylobacteria / Sulfurospirillum | 10.1128/msystems.00148-24 | “H2 oxidation provides favorable energy yields for carbon fixation… avoiding reverse electron transport requirements” (wang2024novelisolatesof pages 12-15) | Useful donor-specific edge; may not generalize to all hydrogen oxidizers. |
| Sox system (soxABCDYZ) | enables | sulfur oxidation | KEGG/MetaCyc label-only: Sox system | Culture/genome/transcriptome | Sulfurospirillum; vent biofilms | 10.1128/msystems.00148-24 | “The SOX system (soxABCDYZ) enables sulfur oxidation” (wang2024novelisolatesof pages 12-15) | Strong for sulfur-oxidizing taxa carrying sox; absent in some chemolithoautotrophs (e.g., Nautiliales). |
| sulfur oxidation | fuels | CO2 fixation | GO label-only: sulfur compound oxidation; carbon fixation | SIP + metaproteogenomics | vent biofilms; groundwater sulfur oxidizers | 10.3389/fmicb.2021.638300 | “inorganic reduced sulfur species are the main electron donors and CO2 the main carbon source” | Strong ecological edge, but context-specific to sulfur-rich systems; cited from retrieved paper without context ID not used here, so keep wording general in later curation. |
| Cyc2 | oxidizes | Fe2+ | label-only Cyc2; CHEBI:29033 Fe2+ | Mechanistic model + transcriptomics | Acidithiobacillus ferrooxidans | 10.3390/microorganisms12030590 | “Fe2+ oxidation by outer-membrane cytochrome c (Cyc2)” (wang2024characterizethegrowth pages 1-2) | Strong candidate edge for acidophilic iron oxidizers; not universal for all iron oxidizers. |
| rusticyanin / Cyc1 | transfers_electrons_from | Fe2+ oxidation pathway | label-only rusticyanin; Cyc1 | Mechanistic model + transcriptomics | Acidithiobacillus ferrooxidans | 10.3390/microorganisms12030590 | “electron flow toward rusticyanin (Rus), then through cytoplasm cytochrome c (Cyc1)” (wang2024characterizethegrowth pages 1-2) | Good pathway edge; exact subcellular routing should remain taxon-specific. |
| phosphite | is_electron_donor_for | anaerobic chemolithoautotrophy | CHEBI label-only: phosphite | Culture + biochemical/genomic evidence | Desulfotignum phosphitoxidans; Phosphitispora fastidiosa | 10.1111/1462-2920.16470 | “phosphite as an efficient inorganic electron donor supporting lithoautotrophic growth” (mao2023anaerobicdissimilatoryphosphite pages 5-5) | Strong but restricted to specialized anaerobes. |
| phosphite dehydrogenase | oxidizes | phosphite | label-only phosphite dehydrogenase | Biochemical review of pathway | anaerobic phosphite oxidizers | 10.1111/1462-2920.16470 | “The key enzyme of this metabolism is an NAD+-dependent phosphite dehydrogenase” (mao2023anaerobicdissimilatoryphosphite pages 4-5) | Strong edge; specific enzyme family details vary across taxa. |
| Rnf complex | transfers_electrons_to | ferredoxin | label-only Rnf complex; ferredoxin | Genomic/mechanistic evidence | Desulfotignum phosphitoxidans | 10.1111/1462-2920.16470 | “A membrane-bound Rnf complex facilitates electron shifting from NADH to ferredoxin levels” (mao2023anaerobicdissimilatoryphosphite pages 5-5) | Important energy-coupling edge; may be absent or partial in related taxa. |
| Calvin-Benson-Bassham cycle | fixes | CO2 | GO/KEGG label-only CBB cycle; Rubisco not directly evidenced in cited context IDs | Culture/transcriptome | Acidithiobacillus ferrooxidans | 10.3390/microorganisms12030590 | “exclusive energy source for O2 reduction and CO2 fixation” and A. ferrooxidans “fixing CO2 via the Calvin-Benson-Bassham (CBB) cycle” (wang2024characterizethegrowth pages 1-2) | Strong pathway-level edge for this taxon; avoid adding Rubisco-specific edge without direct snippet from source. |
| rTCA cycle | fixes | CO2 | GO/KEGG label-only reverse TCA cycle | Culture + genomics + proteomics | Sulfurospirillum strain 1612; Aquifex aeolicus | 10.1128/msystems.00148-24 | “uses rTCA cycle (genes aclAB, oorABCD) for CO2 fixation” (wang2024novelisolatesof pages 12-15) | Strong pathway-level edge. |
| PFOR / OGOR with low-potential ferredoxins | drives | reductive carboxylation in rTCA cycle | label-only PFOR; OGOR; ferredoxin | Biochemical + proteomic | Aquifex aeolicus | 10.3390/life13030627 | “Fd6 and Fd7… can physically interact and exchange electrons with both PFOR and OGOR” (prioretti2023carbonfixationin pages 16-17) | High-value mechanistic edge, but currently evidenced in Aquifex-specific biochemistry. |
| Wood-Ljungdahl pathway (acetyl-CoA pathway) | fixes | CO2 | GO/KEGG label-only Wood-Ljungdahl pathway; CODH-ACS label-only | Review + pathway biochemistry context | acetogens/methanogens; phosphite oxidizers | 10.3389/fmicb.2023.1257597 | “strictly anaerobic chemolithoautotrophs that use the acetyl-CoA pathway of CO2 fixation” (schwander2023serpentinizationasthe pages 8-9) | Strong pathway-level edge for anaerobic chemolithoautotrophs; do not overgeneralize to aerobic taxa. |


*Table: This table compiles strong candidate causal edges for curating METPO:1000634, emphasizing core trait logic and representative donor- and pathway-specific mechanisms. It highlights which edges are broadly curatable versus those that should remain taxon- or context-qualified.*

### Recommended compact core for the YAML

The most defensible universal graph is deliberately small:

1. `inorganic electron donor` **is oxidized during** `chemoautolithotrophic growth`.
2. `inorganic electron donor oxidation` **supplies electrons to** `electron-transfer/energy-conservation process`.
3. `electron-transfer/energy-conservation process` **generates** `ATP and reducing equivalents`.
4. `ATP and reducing equivalents` **enable** `autotrophic inorganic-carbon fixation`.
5. `CO2/HCO3−` **is carbon source for** `autotrophic inorganic-carbon fixation`.
6. `autotrophic inorganic-carbon fixation` **contributes carbon to** `biomass synthesis`.

Edges 2–4 are biologically sound but should be worded at process level: substrate-level phosphorylation occurs in some anaerobic pathways, and neither a respiratory chain nor reverse electron transport is universal. The phosphite system illustrates this diversity: phosphite dehydrogenase supplies NADH, while an Rnf complex can shift electrons to low-potential ferredoxin for the Wood–Ljungdahl pathway. (mao2023anaerobicdissimilatoryphosphite pages 5-5, mao2023anaerobicdissimilatoryphosphite pages 4-5)

### Strong modular subgraphs

**Hydrogen oxidation–rTCA.** A 2024 Sulfurospirillum isolate grew chemolithoautotrophically with H2, encoded diverse [NiFe]-hydrogenases, and carried `aclAB` and `oorABCD` for the rTCA cycle. This supports `H2 → hydrogenase → electron supply → rTCA fixation`, but only with a strain/taxon qualifier. (wang2024novelisolatesof pages 12-15)

**Sulfur oxidation.** `soxABCDYZ → sulfur oxidation` is supported in the same Sulfurospirillum system, but Sox is not universal: 2023 hydrothermal evidence found that Nautiliales lacked Sox while retaining chemolithoautotrophic activity. Therefore, absence of Sox cannot negate the trait. (wang2024novelisolatesof pages 12-15, deng2023strategiesofchemolithoautotrophs pages 1-2)

**Fe2+ oxidation–CBB.** In *A. ferrooxidans*, the supported sequence is `Fe2+ → Cyc2 → rusticyanin → Cyc1/downhill electron transfer → ATP`, coupled to CBB-cycle CO2 fixation with O2 as terminal acceptor. This is a valuable, well-resolved taxon-specific module, not a generic iron-oxidizer pathway. (wang2024characterizethegrowth pages 1-2)

**rTCA ferredoxin chemistry.** In *Aquifex aeolicus*, purified low-potential Fd6 and Fd7 physically interacted and exchanged electrons with PFOR and OGOR, supporting direct edges from reduced ferredoxin to the two reductive carboxylation complexes. This is among the strongest enzyme-level evidence retrieved. (prioretti2023carbonfixationin pages 16-17)

**Anaerobic phosphite oxidation–Wood–Ljungdahl.** Phosphite is a specialized inorganic donor. The reviewed pathway supports phosphite dehydrogenase-mediated oxidation, NADH production, Rnf-mediated ferredoxin reduction in *Desulfotignum phosphitoxidans*, and delivery of reducing power to CODH-dependent CO2 fixation. The review estimates approximately one ATP per electron pair and emphasizes exceptionally efficient routing of substrate electrons into biomass. (mao2023anaerobicdissimilatoryphosphite pages 5-5, mao2023anaerobicdissimilatoryphosphite pages 4-5)

## 4. Recent developments, applications, and quantitative evidence

- **Hydrothermal ecology (2023–2024):** ^13C-bicarbonate SIP resolved active carbon fixation across pH 2.2–5.6 and 30–65°C, revealing distinct Campylobacterales and Nautiliales strategies rather than one universal chemolithoautotrophic mechanism. (deng2023strategiesofchemolithoautotrophs pages 1-2)
- **New cultured phenotype (2024):** strain 1612 was reported as the first Sulfurospirillum supported as chemolithoautotrophic by combined genomic and phenotype evidence, expanding the known metabolic range of shallow-water vent Campylobacteria. (wang2024novelisolatesof pages 12-15)
- **Electrode-driven carbon fixation (2024):** *A. ferrooxidans* displayed 493 DEGs—297 downregulated and 196 upregulated—during electroautotrophy versus Fe2+-based chemoautotrophy. Pilin, porin, and ATP-associated transcripts included reported log2 fold changes of 2.24, 1.72, and 2.59. This supports engineering relevance but also confirms electroautotrophy is physiologically distinct. (wang2024characterizethegrowth pages 22-23)
- **Flue-gas capture (2023):** a non-photosynthetic community acclimated to a model cement flue gas achieved 100% CO2 removal after 45 days. Na2S gave 100% batch CO2 consumption, FeCl2 28%, and a continuous sulfide-fed biotrickling filter reached up to 77%. These are community/reactor outcomes and cannot be assigned to a single organism or mechanism without further validation. DOI: [10.1111/1751-7915.14353](https://doi.org/10.1111/1751-7915.14353), published October 2023.
- **Environmental primary production:** serpentinizing systems continuously generate H2; hydrogenases connect this reductant to acetogen and methanogen Wood–Ljungdahl metabolism. Such chemolithoautotrophs can form the primary-production base of sunlight-free crustal ecosystems. (schwander2023serpentinizationasthe pages 8-9)
- **Biotechnology:** current implementations include nitrifying biofilms in wastewater treatment, sulfur oxidation and sulfide detoxification, bioleaching/biomining by acidophilic iron/sulfur oxidizers, H2/CO2 gas fermentation, microbial electrosynthesis, and CO2-to-biomass/chemicals platforms. For TraitMech, these applications are contextual annotations; they should not be represented as mechanistic causes of the trait.

## 5. Expert synthesis for curation

The strongest expert-level conclusion is that chemolithoautotrophy is a **compound physiological capability**, not a single pathway. It requires evidence for both axes: inorganic chemical energy/electrons and inorganic-carbon assimilation. Carbon-fixation genes alone establish autotrophic potential; donor-oxidation genes alone establish lithotrophic potential. Their co-occurrence is suggestive, but the reviewed groundwater work shows why phenotype and isotope evidence matter: organisms can combine CO2 fixation with substantial organic-carbon uptake. (taubert2022bolsteringfitnessvia pages 6-7)

Accordingly, the TraitMech graph should use a small universal causal spine and attach donor-, acceptor-, pathway-, taxon-, and condition-specific branches. It should not encode Rubisco, Sox, oxygen respiration, reverse electron transport, or any particular donor as necessary for every bearer of `METPO:1000634`.

## 6. Warnings: claims not ready for unconditional curation

1. **Do not make methane a canonical inorganic donor.** Its classification conflicts with strict lithotrophy.
2. **Do not infer the trait from marker genes alone.** MAGs and metagenomes show potential, not growth or flux.
3. **Do not assert Sox as necessary for sulfur chemolithoautotrophy.** Nautiliales can lack Sox. (deng2023strategiesofchemolithoautotrophs pages 1-2)
4. **Do not assert Rubisco/CBB as universal.** rTCA and Wood–Ljungdahl pathways are directly supported alternatives. (schwander2023serpentinizationasthe pages 8-9, prioretti2023carbonfixationin pages 16-17)
5. **Do not make O2 a universal terminal acceptor.** Nitrate and CO2-supported anaerobic systems exist; acceptor use is modular.
6. **Do not make reverse electron transport universal.** Its need depends on donor redox potential and fixation pathway; the Sulfurospirillum interpretation is taxon-specific. (wang2024novelisolatesof pages 12-15)
7. **Keep Cyc2–Rus–Cyc1 taxon-qualified.** It should not be generalized to all Fe2+ oxidizers. (wang2024characterizethegrowth pages 1-2)
8. **Keep PFOR/OGOR–Fd6/Fd7 Aquifex-qualified.** The biochemical edge is strong, but the precise ferredoxins are lineage-specific. (prioretti2023carbonfixationin pages 16-17)
9. **Treat electroautotrophy separately.** Electrode electrons, extracellular pili/EPS, and porins define an engineered or environmental electron-uptake mode distinct from oxidation of a dissolved inorganic donor. (wang2024characterizethegrowth pages 22-23)
10. **Do not curate the 2024 Halomonas “new pathway” preprint as established chemolithoautotrophy.** CO2-dependent nucleotide synthesis is not equivalent to CO2 as the primary biomass carbon source, and the report was a preprint.
11. **Verify all ontology identifiers before YAML insertion.** Label-only nodes are preferable to an incorrect CHEBI, GO, EC, Rhea, KEGG, or UniProt CURIE.

## 7. DOI-first bibliography

1. Wang Q. et al. “Characterize the Growth and Metabolism of *Acidithiobacillus ferrooxidans* under Electroautotrophic and Chemoautotrophic Conditions.” *Microorganisms* 12, 590. **March 2024.** [https://doi.org/10.3390/microorganisms12030590](https://doi.org/10.3390/microorganisms12030590). (wang2024characterizethegrowth pages 1-2, wang2024characterizethegrowth pages 22-23)
2. Wang L. et al. “Novel isolates of hydrogen-oxidizing chemolithoautotrophic *Sulfurospirillum*…” *mSystems* 9. **September 2024.** [https://doi.org/10.1128/msystems.00148-24](https://doi.org/10.1128/msystems.00148-24). (wang2024novelisolatesof pages 12-15)
3. Deng W. et al. “Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions…” *Microbiome* 11. **December 2023.** [https://doi.org/10.1186/s40168-023-01712-w](https://doi.org/10.1186/s40168-023-01712-w). (deng2023strategiesofchemolithoautotrophs pages 1-2)
4. Prioretti L. et al. “Carbon Fixation in the Chemolithoautotrophic Bacterium *Aquifex aeolicus* Involves Two Low-Potential Ferredoxins…” *Life* 13, 627. **February 2023.** [https://doi.org/10.3390/life13030627](https://doi.org/10.3390/life13030627). (prioretti2023carbonfixationin pages 16-17)
5. Mao Z. et al. “Anaerobic dissimilatory phosphite oxidation, an extremely efficient concept of microbial electron economy.” *Environmental Microbiology* 25:2068–2074. **August 2023.** [https://doi.org/10.1111/1462-2920.16470](https://doi.org/10.1111/1462-2920.16470). (mao2023anaerobicdissimilatoryphosphite pages 5-5, mao2023anaerobicdissimilatoryphosphite pages 4-5)
6. Schwander L. et al. “Serpentinization as the source of energy, electrons, organics, catalysts, nutrients and pH gradients…” *Frontiers in Microbiology* 14. **October 2023.** [https://doi.org/10.3389/fmicb.2023.1257597](https://doi.org/10.3389/fmicb.2023.1257597). (schwander2023serpentinizationasthe pages 8-9, schwander2023serpentinizationasthe pages 10-11)
7. Alvarez-Guzmán C.L. et al. “Effect of electron donors on CO2 fixation from a model cement industry flue gas…” *Microbial Biotechnology* 16:2387–2400. **October 2023.** [https://doi.org/10.1111/1751-7915.14353](https://doi.org/10.1111/1751-7915.14353).
8. Taubert M. et al. “Bolstering fitness via CO2 fixation and organic carbon uptake: mixotrophs in modern groundwater.” *ISME Journal* 16:1153–1162. **Published online December 2021; volume 2022.** [https://doi.org/10.1038/s41396-021-01163-x](https://doi.org/10.1038/s41396-021-01163-x). (taubert2022bolsteringfitnessvia pages 6-7)
9. Wright C.L., Lehtovirta-Morley L.E. “Nitrification and beyond: metabolic versatility of ammonia oxidising archaea.” *ISME Journal* 17:1358–1368. **July 2023.** [https://doi.org/10.1038/s41396-023-01467-0](https://doi.org/10.1038/s41396-023-01467-0).
10. Laufer-Meiser K. et al. “Oxidation of sulfur, hydrogen, and iron by metabolically versatile *Hydrogenovibrio*…” *ISME Journal* 18. **2024.** [https://doi.org/10.1093/ismejo/wrae173](https://doi.org/10.1093/ismejo/wrae173).

References

1. (wang2024novelisolatesof pages 12-15): Li Wang, Xinyi Cheng, Yi-Yang Guo, Junwei Cao, Mingye Sun, Jiang-Shiou Hwang, Rulong Liu, and Jiasong Fang. Novel isolates of hydrogen-oxidizing chemolithoautotrophic <i>sulfurospirillum</i> provide insight to the functions and adaptation mechanisms of campylobacteria in shallow-water hydrothermal vents. Sep 2024. URL: https://doi.org/10.1128/msystems.00148-24, doi:10.1128/msystems.00148-24. This article has 7 citations and is from a peer-reviewed journal.

2. (deng2023strategiesofchemolithoautotrophs pages 1-2): Wenchao Deng, Zihao Zhao, Yufang Li, Rongguang Cao, Mingming Chen, Kai Tang, Deli Wang, Wei Fan, Anyi Hu, Guangcheng Chen, Chen-Tung Arthur Chen, and Yao Zhang. Strategies of chemolithoautotrophs adapting to high temperature and extremely acidic conditions in a shallow hydrothermal ecosystem. Microbiome, Dec 2023. URL: https://doi.org/10.1186/s40168-023-01712-w, doi:10.1186/s40168-023-01712-w. This article has 17 citations and is from a highest quality peer-reviewed journal.

3. (taubert2022bolsteringfitnessvia pages 6-7): Martin Taubert, Will A Overholt, Beatrix M Heinze, Georgette Azemtsop Matanfack, Rola Houhou, Nico Jehmlich, Martin von Bergen, Petra Rösch, Jürgen Popp, and Kirsten Küsel. Bolstering fitness via co2 fixation and organic carbon uptake: mixotrophs in modern groundwater. The ISME Journal, 16:1153-1162, Dec 2022. URL: https://doi.org/10.1038/s41396-021-01163-x, doi:10.1038/s41396-021-01163-x. This article has 69 citations.

4. (wang2024characterizethegrowth pages 22-23): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

5. (wang2024characterizethegrowth pages 1-2): Quansheng Wang, Haijun Long, Huiqi Wang, and Maggie C. Y. Lau Vetter. Characterize the growth and metabolism of acidithiobacillus ferrooxidans under electroautotrophic and chemoautotrophic conditions. Microorganisms, 12:590, Mar 2024. URL: https://doi.org/10.3390/microorganisms12030590, doi:10.3390/microorganisms12030590. This article has 11 citations.

6. (prioretti2023carbonfixationin pages 16-17): Laura Prioretti, Giulia D'Ermo, Pascale Infossi, Arlette Kpebe, Régine Lebrun, Marielle Bauzan, Elisabeth Lojou, Bruno Guigliarelli, Marie-Thérèse Giudici-Orticoni, and Marianne Guiral. Carbon fixation in the chemolithoautotrophic bacterium aquifex aeolicus involves two low-potential ferredoxins as partners of the pfor and ogor enzymes. Life, 13:627, Feb 2023. URL: https://doi.org/10.3390/life13030627, doi:10.3390/life13030627. This article has 8 citations.

7. (mao2023anaerobicdissimilatoryphosphite pages 5-5): Zhuqing Mao, Nicolai Müller, Sabrina Borusak, David Schleheck, and Bernhard Schink. Anaerobic dissimilatory phosphite oxidation, an extremely efficient concept of microbial electron economy. Environmental microbiology, 25:2068-2074, Aug 2023. URL: https://doi.org/10.1111/1462-2920.16470, doi:10.1111/1462-2920.16470. This article has 5 citations and is from a domain leading peer-reviewed journal.

8. (mao2023anaerobicdissimilatoryphosphite pages 4-5): Zhuqing Mao, Nicolai Müller, Sabrina Borusak, David Schleheck, and Bernhard Schink. Anaerobic dissimilatory phosphite oxidation, an extremely efficient concept of microbial electron economy. Environmental microbiology, 25:2068-2074, Aug 2023. URL: https://doi.org/10.1111/1462-2920.16470, doi:10.1111/1462-2920.16470. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (schwander2023serpentinizationasthe pages 8-9): Loraine Schwander, Max Brabender, Natalia Mrnjavac, Jessica L. E. Wimmer, Martina Preiner, and William F. Martin. Serpentinization as the source of energy, electrons, organics, catalysts, nutrients and ph gradients for the origin of luca and life. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1257597, doi:10.3389/fmicb.2023.1257597. This article has 71 citations and is from a peer-reviewed journal.

10. (schwander2023serpentinizationasthe pages 10-11): Loraine Schwander, Max Brabender, Natalia Mrnjavac, Jessica L. E. Wimmer, Martina Preiner, and William F. Martin. Serpentinization as the source of energy, electrons, organics, catalysts, nutrients and ph gradients for the origin of luca and life. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1257597, doi:10.3389/fmicb.2023.1257597. This article has 71 citations and is from a peer-reviewed journal.