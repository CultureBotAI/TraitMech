---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T11:12:00.696075'
end_time: '2026-08-04T11:22:06.139541'
duration_seconds: 605.44
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: lithoautotrophic
  trait_identifier: METPO:1000647
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: lithoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from inorganic electron
    donors and carbon from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: lithoautotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules
    (Review supports inorganic compounds as reductants for lithotrophic growth.) |
    DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation
    as the autotrophic carbon-assimilation process.)'
  causal_graph_summary: 'lithoautotrophic_inorganic_donor_co2_fixation: 15 nodes,
    12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000647
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from inorganic electron donors and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoautotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules (Review supports inorganic compounds as reductants for lithotrophic growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** lithoautotrophic_inorganic_donor_co2_fixation: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **lithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoautotrophic.yaml`.

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
- **Trait label:** lithoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000647
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from inorganic electron donors and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoautotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-378630-2.00219-X: inorganic atoms or molecules (Review supports inorganic compounds as reductants for lithotrophic growth.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** lithoautotrophic_inorganic_donor_co2_fixation: 15 nodes, 12 edges

## Research Objective

Research the microbial trait **lithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoautotrophic.yaml`.

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


# Curation report: lithoautotrophic

## 1. Trait record and scope

- **Trait label:** lithoautotrophic
- **Trait identifier:** `METPO:1000647`
- **Category / kind / status:** PHYSIOLOGY / CLASS / REVIEWED
- **Parent:** `METPO:1000631`
- **Synonym:** lithoautotroph
- **Operational definition:** a trophic state in which inorganic electron donors supply electrons for energy conservation and reducing power, while CO2/HCO3− supplies the carbon incorporated into biomass.

The decisive phenotype is therefore a **conjunction**: demonstrated inorganic-donor utilization **and** net autotrophic assimilation of inorganic carbon under the same compatible growth condition. Donor oxidation alone is lithotrophy, not necessarily lithoautotrophy; conversely, anaplerotic CO2 incorporation by a heterotroph is not autotrophy. A sulfur oxidizer lacking canonical carbon-fixation pathways and relying on organic-carbon uptake illustrates the chemolithoheterotrophic boundary case. Accordingly, sulfur-, H2-, Fe(II)-, ammonia-, or electrode-oxidation genes alone must not trigger this trait annotation.

“Chemolithoautotrophic” is the dominant microbial implementation, in which chemical oxidation drives energy conservation. Photolithoautotrophy is also within the lexical scope when an inorganic electron donor and light jointly support CO2 fixation, but it should be represented as a qualified branch rather than conflated with dark chemolithoautotrophy. Facultative autotrophs and mixotrophs qualify only in the conditions where inorganic donors and inorganic carbon demonstrably support growth. Extracellular-electron uptake is a specialized lithotrophic branch, not a universal requirement. In *Rhodopseudomonas palustris* TIE-1, cathodic electrons enter the photosynthetic electron-transport chain and CO2 fixation is the principal sink; deleting Rubisco genes reduced extracellular-electron uptake by approximately 90%, providing unusually direct causal evidence. (guzman2019phototrophicextracellularelectron pages 12-12)

## 2. Recommended graph architecture

The existing 15-node/12-edge graph should retain a small **universal core** and add alternative, taxon-qualified branches:

1. **Inorganic electron donor** → donor-specific oxidation/electron-uptake module.
2. Oxidation module → electron-transport chain.
3. Electron transport → ion-motive force and ATP generation.
4. Electron transport/reverse electron flow → reduced ferredoxin or NAD(P)H.
5. ATP + reductant + CO2/HCO3− → one of several autotrophic carbon-fixation pathways.
6. Fixed-carbon intermediates → biomass formation.
7. Terminal electron acceptor and physicochemical conditions → enable or constrain the foregoing processes.

No single donor, acceptor, enzyme, or carbon-fixation pathway is necessary across all lithoautotrophs. In particular, Rubisco must not be made obligatory because rTCA-, Wood–Ljungdahl-, and hydroxypropionate-cycle lithoautotrophs exist. The Wood–Ljungdahl pathway uses CODH/acetyl-CoA synthase and reduced ferredoxin and is exceptionally energy-efficient, requiring approximately one ATP per CO2 in the reviewed accounting. (pillot2023sparkoflife pages 9-11)

## 3. Candidate nodes

The following matrix separates broadly reusable nodes from lineage-specific candidates.

| Module/node group | Representative entities | Mechanistic role | Evidence strength or curation caveat |
|---|---|---|---|
| Inorganic electron donors | H2; reduced sulfur compounds (H2S, HS−, S0, S2O3^2−); Fe(II); NH3/NH4+; extracellular electrons; CO | Define the lithotrophic side of the trait by supplying electrons for energy conservation and reducing power generation; donor use is taxon- and condition-specific (gupta2020extracellularelectronuptake pages 8-9, laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 1-2, jahn2024theenergymetabolism pages 1-2, wang2024novelisolatesof pages 12-15) | Strong for H2, sulfur, Fe(II), and extracellular electrons in specific taxa; ammonia is well established for nitrifiers but not directly extracted here as a curation-ready mechanistic edge; CO appears in broader literature but is weaker in the gathered evidence for this trait report |
| Electron acceptors | O2; NO3−; S0/electrode in specialized electrotrophic contexts | Accept terminal electrons during respiration or linked redox metabolism; acceptor availability shapes whether inorganic donor oxidation supports growth and CO2 fixation (gupta2020extracellularelectronuptake pages 8-9, laufermeiser2024oxidationofsulfur pages 1-2, jahn2024theenergymetabolism pages 1-2, wang2024novelisolatesof pages 7-9) | Strong that O2 and nitrate commonly gate lithoautotrophic growth; exact acceptor pairing is lineage-specific and should be curated with condition qualifiers |
| Electron transport / energy conservation | Reverse electron transport; proton motive force; ATP synthesis; NAD(H)/NADPH regeneration; respiratory complexes I–IV; terminal oxidases; outer-membrane electron conduits | Couples donor oxidation or extracellular electron uptake to ATP production and reducing-equivalent generation required for autotrophic growth (gupta2020extracellularelectronuptake pages 9-10, gupta2020extracellularelectronuptake pages 8-9, jahn2024theenergymetabolism pages 1-2, wang2024novelisolatesof pages 7-9) | Strong at pathway/process level; specific conduits differ across taxa and should not be over-generalized to all lithoautotrophs |
| Hydrogen oxidation machinery | [NiFe]-hydrogenases; soluble and membrane-bound hydrogenases; multiple hydrogenase subgroups | Oxidize H2 and feed electrons into respiratory metabolism; in some taxa both soluble and membrane-bound enzymes contribute to lithoautotrophic growth (laufermeiser2024oxidationofsulfur pages 4-6, jahn2024theenergymetabolism pages 1-2, wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15) | Strong for hydrogenotrophic lithoautotrophs; exact subtype usage is species-specific |
| Sulfur oxidation machinery | Sox system; incomplete Sox variants; sulfide:quinone oxidoreductase (Sqr); tetrathionate-related sulfur oxidation modules | Oxidize reduced sulfur compounds to conserve energy for autotrophic carbon fixation (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 6-8, wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15) | Strong that sulfur oxidation supports lithoautotrophy; exact gene complements vary, and incomplete Sox pathways may yield intermediate sulfur storage rather than complete oxidation |
| Iron oxidation machinery | Fe(II) oxidation modules; candidate unknown Fe-oxidation factors | Enable ferrous iron as electron donor for autotrophic growth in some lineages (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur pages 9-10) | Moderate: physiology supports Fe(II)-linked growth/CO2 fixation, but known canonical Fe-oxidation genes were not detected in Hydrogenovibrio, so mechanistic nodes remain partly unresolved |
| Extracellular electron uptake | Electrode/solid-phase conductive substances; cathodic electron flow; phototrophic/electroautotrophic uptake systems | Allows electrons from insoluble or electrical sources to enter metabolism and support CO2 fixation in specialized autotrophs (gupta2020extracellularelectronuptake pages 9-10, guzman2019phototrophicextracellularelectron pages 12-12) | Strong for specialized electroautotrophs, but should be marked as a subtype/special case rather than universal lithoautotrophy |
| Carbon-fixation pathways | Calvin-Benson-Bassham cycle; reverse TCA cycle; Wood-Ljungdahl pathway; 3-hydroxypropionate/4-hydroxybutyrate pathway | Define the autotrophic side of the trait by converting CO2/HCO3− into biomass precursors; alternative pathways occur across bacterial and archaeal lithoautotrophs (pillot2023sparkoflife pages 9-11, laufermeiser2024oxidationofsulfur pages 4-6, jahn2024theenergymetabolism pages 1-2, wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15) | Strong at pathway-class level; no single CO2-fixation pathway should be made obligatory for the trait |
| Carbon-fixation enzymes | RubisCO forms IA/IAq/II; cbbLS; ATP-citrate lyase (aclAB); 2-oxoglutarate:ferredoxin oxidoreductase (oorABCD); pyruvate:ferredoxin oxidoreductase (porABCD); CODH/ACS | Catalyze pathway-specific CO2 assimilation steps and provide stronger causal anchors than pathway labels alone (pillot2023sparkoflife pages 9-11, laufermeiser2024oxidationofsulfur pages 6-8, wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15) | Strong when tied to a specific pathway/taxon; CODH/ACS mainly anchors Wood-Ljungdahl and should not be generalized beyond acetogens/methanogens and related autotrophs |
| Core physiological process node | CO2/HCO3− fixation into biomass | Operational hallmark distinguishing lithoautotrophy from chemolithoheterotrophy or sulfur/hydrogen oxidation without net autotrophic growth (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2) | Very strong trait-defining node; absence of canonical fixation genes can indicate a boundary case rather than lithoautotrophy |
| Boundary/counterexample module | Sulfur oxidation plus organic carbon uptake without canonical autotrophic pathway | Demonstrates that inorganic donor oxidation alone does not suffice for lithoautotrophic annotation (gupta2020extracellularelectronuptake pages 8-9) | Strong warning: chemolithoheterotrophs and mixotrophs should not be auto-curated as lithoautotrophs without net autotrophic evidence |
| Assays and phenotype readouts | Growth on inorganic donor + CO2/HCO3− medium; 14C-bicarbonate incorporation; RubisCO activity assays; donor oxidation rates; transcriptomics under donor shifts | Provide curation-grade phenotype evidence linking inorganic donor use to autotrophic biomass production (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2) | Strong when multiple assays agree; transcriptomics alone is supportive, not sufficient for phenotype assignment |
| Quantitative donor/CO2 fixation data | H2 oxidation 75.4–145.2 nmol ml−1 h−1; thiosulfate oxidation 1.05–2.06 μmol ml−1 h−1; Fe(II) oxidation 0.008–0.016 μmol ml−1 h−1; vent-scale estimates up to 84 mmol CO2 fixation h−1 on thiosulfate for one strain | Quantifies donor-specific support for autotrophy and supports prioritizing donor-specific edges in curation (laufermeiser2024oxidationofsulfur pages 8-9, laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur pages 9-10) | Strong but taxon-specific; do not generalize magnitudes beyond the studied Hydrogenovibrio strains |
| Environmental controls | Microoxic vs oxic conditions; nitrate availability; donor identity; hydrothermal vent geochemistry; low-ammonium oligotrophic niches | Environmental context constrains whether lithoautotrophic modules are active and which donor/acceptor/pathway combinations dominate (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur pages 6-8, jahn2024theenergymetabolism pages 1-2) | Strong that the trait is condition-dependent; many edges should carry environmental qualifiers rather than be asserted as unconditional |
| Real-world/application context | Hydrothermal vent primary production; electroautotrophic growth using hydrovoltaic or electrode-derived electrons; biotechnological CO2 conversion chassis such as Cupriavidus | Shows the trait’s ecological and applied relevance, including chemosynthetic production and engineered CO2 utilization systems (gupta2020extracellularelectronuptake pages 9-10, jahn2024theenergymetabolism pages 1-2) | Useful context, but application-specific engineering components should be curated separately from the core natural trait unless directly intrinsic to lithoautotrophy |


*Table: This table summarizes candidate node groups for curating the lithoautotrophic trait, emphasizing what is broadly supported versus what is taxon- or condition-specific. It is useful for deciding which entities belong in a core TraitMech graph and which should be marked as qualified or uncertain.*

### 3.1 Conservative ontology grounding

Use identifiers only after checking the target ontology release. Safe or high-confidence candidates include:

| Node | Suggested grounding | Curation note |
|---|---|---|
| lithoautotrophic | `METPO:1000647` | Quote verbatim as supplied. |
| carbon dioxide | `CHEBI:16526` | Carbon substrate; bicarbonate may be the supplied assay species. |
| hydrogencarbonate/bicarbonate | `CHEBI:17544` | Common ^14C/^13C tracer substrate. |
| dihydrogen | `CHEBI:18276` | Inorganic electron donor. |
| dioxygen | `CHEBI:15379` | Common terminal acceptor; also competes with CO2 at Rubisco. |
| nitrate | `CHEBI:17632` | Alternative acceptor in several sulfur/hydrogen oxidizers. |
| nitrite | `CHEBI:16301` | Product of ammonia oxidation and donor for nitrite oxidizers. |
| ammonium | `CHEBI:28938` | Environmentally prevalent ammonia/ammonium substrate pool. |
| carbon fixation | `GO:0015977` | Broad process node; verify preferred GO label in release. |
| chemolithotrophy | `GO:0015975` | Broad energy-metabolism process; verify ontology release. |
| Rubisco | `EC:4.1.1.39` | Reaction-level grounding; retain gene labels `cbbL/rbcL`, `cbbS/rbcS` separately. |
| Calvin–Benson–Bassham cycle | label-only candidate | Add MetaCyc/KEGG mapping only after database verification. |
| reverse TCA cycle | label-only candidate | Do not substitute the oxidative TCA-cycle identifier. |
| Wood–Ljungdahl pathway | label-only candidate | Alternative name: reductive acetyl-CoA pathway. |
| 3-hydroxypropionate/4-hydroxybutyrate cycle | label-only candidate | Archaeal branch; avoid an unverified pathway CURIE. |
| Sox complex, Sqr, PioAB, hydrogenases, respiratory complexes | gene/protein labels initially | Ground to UniProt only for a named strain/protein; family-wide UniProt IDs would be inappropriate. |

Additional candidate chemicals should initially be label-only unless independently validated against ChEBI: Fe(II), FeS, elemental sulfur, sulfide/HS−, thiosulfate, tetrathionate, reduced ferredoxin, NADH, NADPH, ATP, proton motive force, and fixed-carbon intermediates.

### 3.2 Genes, enzymes, and complexes

- **Hydrogen oxidation:** membrane-bound and soluble [NiFe]-hydrogenases; `hyaAB`, `hupUV`, and lineage-specific hydrogenase clusters. A 2024 transposon-fitness study demonstrated that both soluble and membrane-bound hydrogenases contribute to H2-supported lithoautotrophic growth in *Cupriavidus necator* H16. (jahn2024theenergymetabolism pages 1-2)
- **Sulfur oxidation:** complete or incomplete Sox systems (`soxXYZABCD` or subsets), sulfide:quinone oxidoreductase (`sqr`), reverse Dsr where supported, and tetrathionate modules. In *Hydrogenovibrio* strain 104, `soxZC YX` were induced on thiosulfate, but `soxB`, `soxD`, and `sqr` were absent and zero-valent sulfur accumulated; this is a strain-specific incomplete-Sox branch. (laufermeiser2024oxidationofsulfur pages 6-8)
- **Iron oxidation/electron uptake:** PioAB and periplasmic c-type cytochromes are candidates in phototrophic Fe(II) oxidizers, but should not be generalized to all Fe(II)-oxidizing lithoautotrophs. (gupta2020extracellularelectronuptake pages 8-9)
- **CBB cycle:** Rubisco forms IA, IAq, and II; `cbbLS`; phosphoribulokinase; optional carboxysome and inorganic-carbon uptake modules. *Hydrogenovibrio* IAq `cbbLS` expression was strongly elevated during thiosulfate growth. (laufermeiser2024oxidationofsulfur pages 6-8)
- **rTCA cycle:** `aclAB`, `oorABCD`, `porABCD`, and conditionally `frdAB`. These genes were identified in the 2024 shallow-vent *Sulfurospirillum* isolate, alongside multiple hydrogenase clusters. (wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15)
- **Wood–Ljungdahl:** CODH/ACS, reduced-ferredoxin supply, and pathway-specific one-carbon carriers. (pillot2023sparkoflife pages 9-11)
- **Respiration/energy conservation:** Complex I, quinone/cytochrome carriers, terminal oxidases, ATP synthase, reverse electron transport, and ferredoxin/NAD(P)H generation. In *C. necator*, only substrate-dependent subsets of nine terminal complexes contributed measurably to fitness, cautioning against equating gene presence with utilization. (jahn2024theenergymetabolism pages 1-2)

## 4. Candidate causal edges

“Strong” indicates experimental physiology, perturbation, activity measurement, or isotope incorporation. “Moderate” indicates convergent physiological and expression evidence. “Uncertain” denotes genomic inference, unresolved molecular identity, or narrow taxonomic scope.

| Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---|---|---|---|---|
| inorganic electron donor oxidation | supplies electrons to | electron-transport chain | Gupta et al. 2020: Fe(II) electrons cross the outer membrane through PioAB, with cytochrome-mediated transfer. DOI [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0), Oct 2020. (gupta2020extracellularelectronuptake pages 8-9) | **Core, strong at process level**; donor-specific complex is not universal. |
| electron transport | generates | proton motive force | Review evidence links reverse electron transfer and proton motive force to biosynthetic reducing power. (gupta2020extracellularelectronuptake pages 8-9) | **Core, moderate**; direction and coupling depend on redox potential. |
| reverse electron transport | produces | NAD(H)/biosynthetic reductant | “reverse electron transfer processes generating NAD(H) for biosynthesis via proton motive force.” (gupta2020extracellularelectronuptake pages 8-9) | **Moderate**; use a broad reducing-equivalent node because taxa may use NADPH or ferredoxin. |
| ATP plus reducing equivalents | enables | autotrophic CO2 fixation | Wood–Ljungdahl evidence identifies reduced ferredoxin and an ATP requirement; CBB/rTCA branches likewise require energy and reductant. (pillot2023sparkoflife pages 9-11) | **Core abstraction**; do not encode identical stoichiometry across pathways. |
| CO2 fixation pathway | produces precursors for | cellular biomass | Wood–Ljungdahl-derived pyruvate links CO2 fixation to amino acids, carbohydrates, and lipids. (pillot2023sparkoflife pages 9-11) | **Core, strong pathway logic**. |
| H2 | is oxidized by | soluble and membrane-bound hydrogenases | 2024 fitness screen: “both soluble and membrane-bound [NiFe]-hydrogenases … contribute to lithoautotrophic growth.” DOI [10.1128/aem.00748-24](https://doi.org/10.1128/aem.00748-24), Oct 2024. (jahn2024theenergymetabolism pages 1-2) | **Strong, *C. necator*-specific**. |
| hydrogenases | support | H2-dependent lithoautotrophic growth | Same transposon evidence; *Sulfurospirillum* additionally contains several uptake/evolutionary hydrogenase groups. (jahn2024theenergymetabolism pages 1-2, wang2024novelisolatesof pages 12-15) | Curate the causal edge strongly for *C. necator*; other taxa require separate evidence. |
| reduced sulfur compounds | donate electrons to | sulfur-oxidation pathways | Sulfur oxidizers use H2S/HS− and S0; sulfur oxidation can couple to O2 or nitrate reduction. DOI [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0). (gupta2020extracellularelectronuptake pages 8-9) | **Strong class-level branch**. |
| thiosulfate | activates/supports | Sox-dependent oxidation | In strain 104, `soxZ`, `soxC`, `soxY`, and `soxX` were upregulated during thiosulfate oxidation. DOI [10.1093/ismejo/wrae173](https://doi.org/10.1093/ismejo/wrae173), Jan 2024. (laufermeiser2024oxidationofsulfur pages 6-8) | **Moderate, taxon-specific expression edge**. |
| incomplete Sox system | causes/promotes | zero-valent sulfur accumulation | Missing `soxB`, `soxD`, and `sqr` coincided with intracellular/extracellular zero-valent sulfur accumulation. (laufermeiser2024oxidationofsulfur pages 6-8) | **Uncertain causal wording**; curate as “associated with” unless a complementation experiment exists. |
| thiosulfate oxidation | supports | CBB-cycle CO2 fixation | Thiosulfate produced the highest measured CO2-fixation rate and Rubisco was strongly upregulated. (laufermeiser2024oxidationofsulfur pages 8-9, laufermeiser2024oxidationofsulfur pages 4-6) | **Strong for studied *Hydrogenovibrio***. |
| thiosulfate availability | increases relative to H2/Fe(II) | donor-supported CO2 fixation | Oxidation energetics were −762, −237, and −90 kJ mol−1 for thiosulfate, H2, and Fe(II), respectively; fixation was highest on thiosulfate. (laufermeiser2024oxidationofsulfur pages 8-9) | **Strong comparison within assay**, not a universal donor ranking. |
| Fe(II) | supports | autotrophic CO2 fixation | Three strains grew on FeCl2/FeS; ^14C-bicarbonate incorporation was measured, though rates were low. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 9-10) | **Strong phenotype, unresolved mechanism**. |
| unknown Fe(II)-oxidation machinery | mediates | Fe(II) oxidation in *Hydrogenovibrio* | No `cyc2` or other known Fe-oxidation genes were found despite growth and oxidation. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 1-2) | **Uncertain placeholder only**; do not nominate individual genes. |
| Rubisco/CBB cycle | fixes | CO2 into organic carbon | *Hydrogenovibrio* displayed Rubisco activity and ^14C-bicarbonate incorporation; IAq `cbbLS` was donor-regulated. (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 6-8) | **Strong, taxon-specific implementation**. |
| `aclAB`/`oorABCD`/`porABCD` | enable | rTCA-cycle carbon fixation | The 2024 *Sulfurospirillum* study identified these characteristic rTCA genes in a validated chemolithoautotrophic isolate. DOI [10.1128/msystems.00148-24](https://doi.org/10.1128/msystems.00148-24), Sep 2024. (wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15) | **Moderate**: pathway assignment is genomic plus physiological, but individual-gene causality was not perturbed. |
| CODH/ACS | catalyzes | Wood–Ljungdahl CO2 fixation | Review identifies CO dehydrogenase and acetyl-CoA synthase as key WL enzymes. DOI [10.3390/life13020356](https://doi.org/10.3390/life13020356), Jan 2023. (pillot2023sparkoflife pages 9-11) | **Strong biochemical knowledge**, pathway-specific. |
| cathodic/extracellular electrons | enter | photosynthetic electron-transport chain | *R. palustris* TIE-1 work found cathodic flow into the photosynthetic chain. DOI [10.1038/s41467-019-09377-6](https://doi.org/10.1038/s41467-019-09377-6), Mar 2019. (guzman2019phototrophicextracellularelectron pages 12-12) | **Strong, photolitho/electroautotrophic subtype**. |
| Rubisco-dependent CO2 fixation | acts as principal sink for | extracellular electrons | Rubisco deletion reduced extracellular-electron uptake by about 90%. (guzman2019phototrophicextracellularelectron pages 12-12) | **Strong perturbational edge**; excellent graph anchor, but not universal. |
| O2 or nitrate availability | enables | respiration coupled to sulfur/iron oxidation | Review reports coupling of sulfur/iron-derived electrons to oxygen or nitrate reduction. (gupta2020extracellularelectronuptake pages 8-9) | **Moderate class-level edge**; encode alternative acceptors, not simultaneous necessity. |
| donor identity | regulates | respiratory and carbon-fixation gene usage | More than 500 genes differed among *Hydrogenovibrio* donor conditions; Rubisco, Sox, and hydrogenase expression changed with substrate. (laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 6-8) | **Strong regulatory observation**, but each edge is strain-specific. |
| inorganic donor oxidation plus inorganic-carbon assimilation | realizes | `METPO:1000647` | Across the experimental studies, growth or fixation required a donor-specific energy module and CO2/HCO3− assimilation. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 4-6, jahn2024theenergymetabolism pages 1-2) | **Recommended phenotype-defining edge**. |

## 5. Assays and minimum evidence standard

A high-confidence lithoautotrophic phenotype should include at least two complementary observations:

1. growth or biomass formation in mineral medium with a defined inorganic donor and CO2/HCO3− as the principal carbon source;
2. donor disappearance/product formation, electrode current uptake, or enzyme activity;
3. ^13C/^14C-bicarbonate incorporation into biomass or a validated autotrophic product;
4. dependence on a fixation or donor-oxidation gene, preferably by knockout/complementation;
5. exclusion of organic-carbon carryover and abiotic donor oxidation.

The 2024 *Hydrogenovibrio* study is a useful assay model: FeS gradient tubes or microoxic FeCl2, H2, and thiosulfate cultures were coupled to oxidation measurements, ^14C-NaHCO3 incorporation, Rubisco activity, microscopy/EDX, and transcriptomics. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 1-2)

Genes alone indicate **potential**, not phenotype. Transcript induction strengthens but does not replace physiological evidence. Stable-isotope incorporation should be normalized against killed/abiotic controls and interpreted carefully because heterotrophs can incorporate inorganic carbon anaplerotically.

## 6. Recent quantitative findings and applications

### 6.1 Donor flexibility at hydrothermal vents

Three 2024 *Hydrogenovibrio* isolates used Fe(II), H2, and thiosulfate. H2 oxidation was 75.4–145.2 nmol mL−1 h−1; thiosulfate oxidation was 1.05–2.06 μmol mL−1 h−1; and Fe(II) oxidation was 0.008–0.016 μmol mL−1 h−1. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 4-6) Vent-scale maxima estimated for one strain were 10 mmol Fe, 24 mmol H2, and 952 mmol thiosulfate oxidized per vent per hour, corresponding to 0.3, 1, and 84 mmol CO2 fixed per hour. (laufermeiser2024oxidationofsulfur pages 1-2) Only approximately 7–11% of electrons were assigned to carbon fixation in the authors’ accounting, illustrating that donor oxidation also funds maintenance, biosynthesis, and other energetic demands. (laufermeiser2024oxidationofsulfur pages 8-9)

These values demonstrate real ecological capacity but are not universal kinetic constants. They depend on strain, donor concentration, oxygen regime, biomass, and the vent-scaling assumptions.

### 6.2 Engineering and biomanufacturing

*C. necator* is a major H2/CO2/O2 gas-fermentation chassis. The 2024 genome-wide fitness study showed that soluble and membrane-bound hydrogenases both matter during H2 lithoautotrophy, whereas terminal-respiratory-complex use is substrate dependent. This provides experimentally grounded targets for reducing unnecessary protein burden and engineering CO2-to-bioproduct platforms. (jahn2024theenergymetabolism pages 1-2)

Electroautotrophy and photoelectroautotrophy can replace diffusible H2 with cathodic or solid-phase electrons. However, extracellular-electron conduits, electrode potentials, mediator dependence, and light input are system-specific engineering nodes, not defining components of all lithoautotrophy. The strongest causal demonstration remains the approximately 90% loss of electron uptake after Rubisco deletion in *R. palustris* TIE-1. (guzman2019phototrophicextracellularelectron pages 12-12)

### 6.3 Environmental implementations

Lithoautotrophs underpin primary production where organic carbon or light is scarce: hydrothermal vents, oxygen-minimum zones, marine sediments, acidic mining systems, and deep subsurface habitats. They also drive nitrification, sulfur oxidation, Fe cycling, hydrogen consumption, and biologically mediated corrosion. The environmental role is conditional on juxtaposition of donor and acceptor; redox interfaces are therefore better graph modifiers than a generic “preferred habitat.” Sulfur and Fe oxidizers, for example, often occupy microoxic or nitrate-bearing interfaces rather than uniformly oxic or anoxic environments. (gupta2020extracellularelectronuptake pages 8-9, laufermeiser2024oxidationofsulfur pages 1-2)

## 7. Expert interpretation for TraitMech

The most defensible graph is **modular rather than enumerative**. Its universal causal claim should be:

> inorganic electron donor availability → donor oxidation/electron uptake → conserved electrochemical energy and reducing power → autotrophic inorganic-carbon fixation → biomass formation → lithoautotrophic phenotype.

Donor-specific enzymes, terminal acceptors, and carbon-fixation pathways should be modeled as alternative subgraphs with taxon and condition qualifiers. This avoids falsely requiring Rubisco, oxygen, or a particular donor. It also accommodates unresolved mechanisms—for example, experimentally supported Fe(II)-dependent autotrophy in *Hydrogenovibrio* despite the absence of recognized Fe-oxidation genes. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 1-2)

For YAML curation, predicates such as `enables`, `supplies_electrons_to`, `generates`, `requires`, `catalyzes`, `increases_activity_of`, and `produces` are preferable to vague associations. Use `associated_with` where evidence is only transcriptomic or genomic. Taxon-specific edges should carry organism/strain and growth-condition qualifiers.

## 8. Warnings: claims not yet ready for unqualified curation

1. **Do not infer lithoautotrophy from donor-oxidation genes alone.** Sulfur oxidizers can be chemolithoheterotrophic.
2. **Do not require Rubisco/CBB universally.** rTCA, Wood–Ljungdahl, and hydroxypropionate pathways are valid alternatives. (pillot2023sparkoflife pages 9-11, wang2024novelisolatesof pages 7-9)
3. **Do not assign `cyc2` or another known iron oxidase to the studied *Hydrogenovibrio*.** Its Fe(II)-oxidation mechanism remains unresolved. (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 9-10)
4. **Do not generalize incomplete Sox composition or sulfur accumulation beyond strain 104.** (laufermeiser2024oxidationofsulfur pages 6-8)
5. **Do not treat gene expression as proof of catalytic necessity.** Knockout, enzyme, flux, or isotope evidence is stronger.
6. **Do not encode O2 as universally required.** Nitrate and other acceptors support anaerobic lithoautotrophic branches. (gupta2020extracellularelectronuptake pages 8-9, wang2024novelisolatesof pages 12-15)
7. **Do not classify formate uncritically as an inorganic donor.** Carbon-source use and nomenclature vary; model formate-supported growth separately unless the curation policy explicitly includes it.
8. **Do not use CO2 incorporation alone.** Heterotrophic anaplerosis can yield measurable inorganic-carbon incorporation.
9. **Do not generalize published rates.** The reported oxidation and fixation rates are strain- and assay-specific.
10. **Do not ground families or complexes to strain-specific UniProt accessions without sequence context.** Label-only nodes are preferable to false precision.

## 9. DOI-first bibliography

1. Laufer-Meiser K. et al. “Oxidation of sulfur, hydrogen, and iron by metabolically versatile *Hydrogenovibrio* from deep sea hydrothermal vents.” *ISME Journal* 18 (January 2024). DOI: [10.1093/ismejo/wrae173](https://doi.org/10.1093/ismejo/wrae173). (laufermeiser2024oxidationofsulfur pages 3-4, laufermeiser2024oxidationofsulfur pages 8-9, laufermeiser2024oxidationofsulfur pages 4-6, laufermeiser2024oxidationofsulfur pages 1-2, laufermeiser2024oxidationofsulfur pages 6-8)
2. Jahn M. et al. “The energy metabolism of *Cupriavidus necator* in different trophic conditions.” *Applied and Environmental Microbiology* 90 (October 2024). DOI: [10.1128/aem.00748-24](https://doi.org/10.1128/aem.00748-24). (jahn2024theenergymetabolism pages 1-2)
3. Wang L. et al. “Novel isolates of hydrogen-oxidizing chemolithoautotrophic *Sulfurospirillum*…” *mSystems* 9 (September 2024). DOI: [10.1128/msystems.00148-24](https://doi.org/10.1128/msystems.00148-24). (wang2024novelisolatesof pages 7-9, wang2024novelisolatesof pages 12-15)
4. Pillot G. et al. “Spark of Life: Role of Electrotrophy in the Emergence of Life.” *Life* 13, 356 (January 2023). DOI: [10.3390/life13020356](https://doi.org/10.3390/life13020356). (pillot2023sparkoflife pages 9-11)
5. Gupta D., Guzman M.S., Bose A. “Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications.” *Journal of Industrial Microbiology and Biotechnology* 47, 863–876 (October 2020). DOI: [10.1007/s10295-020-02309-0](https://doi.org/10.1007/s10295-020-02309-0). (gupta2020extracellularelectronuptake pages 9-10, gupta2020extracellularelectronuptake pages 8-9)
6. Guzman M.S. et al. “Phototrophic extracellular electron uptake is linked to carbon dioxide fixation in the bacterium *Rhodopseudomonas palustris*.” *Nature Communications* 10 (March 2019). DOI: [10.1038/s41467-019-09377-6](https://doi.org/10.1038/s41467-019-09377-6). (guzman2019phototrophicextracellularelectron pages 12-12)

### Recommended curation disposition

Retain `METPO:1000647` as a broad physiological class. Curate the six-step universal core, then add donor-, acceptor-, and fixation-pathway branches with explicit taxon/condition qualifiers. The strongest new additions are H2–hydrogenase edges in *C. necator*, thiosulfate–Sox–Rubisco coupling and quantitative donor comparisons in *Hydrogenovibrio*, rTCA/hydrogenase modules in vent *Sulfurospirillum*, and the perturbational Rubisco-to-electron-uptake edge in *R. palustris*.

References

1. (guzman2019phototrophicextracellularelectron pages 12-12): Michael S. Guzman, Karthikeyan Rengasamy, Michael M. Binkley, Clive Jones, Tahina Onina Ranaivoarisoa, Rajesh Singh, David A. Fike, J. Mark Meacham, and Arpita Bose. Phototrophic extracellular electron uptake is linked to carbon dioxide fixation in the bacterium rhodopseudomonas palustris. Nature Communications, Mar 2019. URL: https://doi.org/10.1038/s41467-019-09377-6, doi:10.1038/s41467-019-09377-6. This article has 204 citations and is from a highest quality peer-reviewed journal.

2. (pillot2023sparkoflife pages 9-11): Guillaume Pillot, Óscar Santiago, Sven Kerzenmacher, and Pierre-Pol Liebgott. Spark of life: role of electrotrophy in the emergence of life. Life, 13:356, Jan 2023. URL: https://doi.org/10.3390/life13020356, doi:10.3390/life13020356. This article has 4 citations.

3. (gupta2020extracellularelectronuptake pages 8-9): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

4. (laufermeiser2024oxidationofsulfur pages 3-4): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

5. (laufermeiser2024oxidationofsulfur pages 1-2): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

6. (jahn2024theenergymetabolism pages 1-2): Michael Jahn, Nick Crang, Arvid H. Gynnå, Deria Kabova, Stefan Frielingsdorf, Oliver Lenz, Emmanuelle Charpentier, and Elton P. Hudson. The energy metabolism of <i>cupriavidus necator</i> in different trophic conditions. Oct 2024. URL: https://doi.org/10.1128/aem.00748-24, doi:10.1128/aem.00748-24. This article has 41 citations and is from a peer-reviewed journal.

7. (wang2024novelisolatesof pages 12-15): Li Wang, Xinyi Cheng, Yi-Yang Guo, Junwei Cao, Mingye Sun, Jiang-Shiou Hwang, Rulong Liu, and Jiasong Fang. Novel isolates of hydrogen-oxidizing chemolithoautotrophic <i>sulfurospirillum</i> provide insight to the functions and adaptation mechanisms of campylobacteria in shallow-water hydrothermal vents. mSystems, Sep 2024. URL: https://doi.org/10.1128/msystems.00148-24, doi:10.1128/msystems.00148-24. This article has 7 citations and is from a peer-reviewed journal.

8. (wang2024novelisolatesof pages 7-9): Li Wang, Xinyi Cheng, Yi-Yang Guo, Junwei Cao, Mingye Sun, Jiang-Shiou Hwang, Rulong Liu, and Jiasong Fang. Novel isolates of hydrogen-oxidizing chemolithoautotrophic <i>sulfurospirillum</i> provide insight to the functions and adaptation mechanisms of campylobacteria in shallow-water hydrothermal vents. mSystems, Sep 2024. URL: https://doi.org/10.1128/msystems.00148-24, doi:10.1128/msystems.00148-24. This article has 7 citations and is from a peer-reviewed journal.

9. (gupta2020extracellularelectronuptake pages 9-10): Dinesh Gupta, Michael S Guzman, and Arpita Bose. Extracellular electron uptake by autotrophic microbes: physiological, ecological, and evolutionary implications. Journal of Industrial Microbiology and Biotechnology, 47:863-876, Oct 2020. URL: https://doi.org/10.1007/s10295-020-02309-0, doi:10.1007/s10295-020-02309-0. This article has 82 citations and is from a peer-reviewed journal.

10. (laufermeiser2024oxidationofsulfur pages 4-6): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

11. (laufermeiser2024oxidationofsulfur pages 6-8): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

12. (laufermeiser2024oxidationofsulfur pages 9-10): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.

13. (laufermeiser2024oxidationofsulfur pages 8-9): Katja Laufer-Meiser, Malik Alawi, Stefanie Böhnke, Claus-Henning Solterbeck, Jana Schloesser, Axel Schippers, Philipp Dirksen, Thomas Brüser, Susann Henkel, Janina Fuss, and Mirjam Perner. Oxidation of sulfur, hydrogen, and iron by metabolically versatile hydrogenovibrio from deep sea hydrothermal vents. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae173, doi:10.1093/ismejo/wrae173. This article has 9 citations.