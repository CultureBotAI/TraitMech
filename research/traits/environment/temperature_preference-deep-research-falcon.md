---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:06:57.649867'
end_time: '2026-08-04T04:18:38.487677'
duration_seconds: 700.84
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature preference
  trait_identifier: METPO:1000613
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that describes characteristic growth with respect to environmental
    temperature.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.culture temp.temperature, range_tmp
  evidence_summary: 'DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports
    temperature-dependent microbial growth-rate phenotypes.)'
  causal_graph_summary: 'temperature_preference_growth_physiology: 13 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 76
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000613
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes characteristic growth with respect to environmental temperature.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.culture temp.temperature, range_tmp
- **Existing evidence:** DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports temperature-dependent microbial growth-rate phenotypes.)
- **Existing causal graph summary:** temperature_preference_growth_physiology: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **temperature preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_preference.yaml`.

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
- **Trait label:** temperature preference
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000613
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes characteristic growth with respect to environmental temperature.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.culture temp.temperature, range_tmp
- **Existing evidence:** DOI:10.1038/sj.jim.2900572: growth rate vs temperature (Supports temperature-dependent microbial growth-rate phenotypes.)
- **Existing causal graph summary:** temperature_preference_growth_physiology: 13 nodes, 12 edges

## Research Objective

Research the microbial trait **temperature preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_preference.yaml`.

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


# Curation report: microbial temperature preference

## Trait record and recommended interpretation

- **Trait label:** temperature preference
- **Trait identifier:** **`METPO:1000613`**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Given definition:** “A phenotype that describes characteristic growth with respect to environmental temperature.”
- **Parent:** `METPO:1000059`
- **Synonyms:** *Physiology and metabolism.culture temp.temperature*; *range_tmp*

### Scope summary

For TraitMech, **temperature preference should be represented as an assay-conditioned microbial growth phenotype**, not as a single intrinsic temperature value. Its core observable is a thermal performance curve relating temperature to a growth endpoint—preferably maximum specific growth rate, μ—and its cardinal parameters:

- **TMIN:** lower boundary permitting detectable growth;
- **TOPT:** temperature giving the maximum specific growth rate, μopt;
- **TMAX:** upper boundary permitting growth.

Thermal growth curves are typically asymmetric or “hump-shaped”; TOPT is therefore not equivalent to the midpoint of TMIN and TMAX. It can also differ from the temperature maximizing biomass yield, product formation, survival, or enzyme activity. Cardinal temperatures are the standard parameters used to delimit the growth niche and its optimum. (noll2020modelingandexploiting pages 6-8, noll2020modelingandexploiting pages 19-20)

The phenotype is **conditional on the assay**. The record should preserve strain, medium and carbon source, pH, oxygen/redox condition, salinity, pressure, inoculum history, acclimation time, temperature-shift versus steady-state design, incubation duration, and measurement endpoint. For example, *Thermoanaerobacter kivui* was assayed in defined or complex medium under strict anoxia, at pH 7.5, with specified carbon sources and growth measured by OD600; its experimentally observed TMIN under those conditions was 39°C. (lehmann2023adaptivelaboratoryevolution pages 2-3, lehmann2023adaptivelaboratoryevolution pages 1-2)

### Boundary cases

1. **Acute thermal survival is not temperature preference.** Heat-shock killing, freeze–thaw survival, or transient stress tolerance measures viability after an insult, whereas temperature preference concerns sustained growth across temperatures. In 2024, *Salmonella* `dnaJ` loss increased acute heat resistance by 10³–10⁵-fold but impaired growth at 37°C and above, directly demonstrating that these phenotypes can oppose one another. (berdejo2024evolutionarytradeoffbetween pages 8-10)
2. **Cold/heat-shock response is not necessarily adaptation of TOPT.** A transient transcriptional or metabolic response may restore homeostasis without shifting the strain’s cardinal temperatures.
3. **Environmental occurrence is not proof of preference.** Detection in ice, hot springs, or hydrothermal sediment does not establish active growth or TOPT.
4. **Enzyme temperature optimum is not organismal TOPT.** Mean enzyme optima correlate with growth temperature, but individual enzymes and genome annotations do not determine organismal preference by themselves. (engqvist2018correlatingenzymeannotations pages 4-6, engqvist2018correlatingenzymeannotations pages 9-10)
5. **Thermotolerance, psychrotolerance, and cardinal-temperature classes should remain separate annotations.** A commonly used scheme defines psychrophiles by TOPT <15°C, mesophiles by approximately 20–45°C, thermophiles by >45°C, extreme thermophiles by >65–70°C, and hyperthermophiles by >80°C. These thresholds are conventions rather than mechanisms. (lehmann2023adaptivelaboratoryevolution pages 1-2)
6. **Growth rate, lag, yield, and product formation are different endpoints.** Evolution at low temperature may shorten lag or improve yield without increasing μ or changing TOPT. (lehmann2023adaptivelaboratoryevolution pages 8-9)

## Current mechanistic model

Temperature simultaneously changes reaction kinetics, protein and nucleic-acid stability, membrane viscosity, diffusion, transport, ribosome function, energy demand, and oxidative damage. Consequently, no universal “temperature-preference gene” is expected. The phenotype emerges from the temperature dependence of multiple cellular subsystems.

The strongest experimentally resolved module is **homeoviscous adaptation**. Cooling packs membrane lipids more tightly and lowers fluidity; cells compensate by increasing unsaturated, branched, or shorter acyl chains. Heating generally favors more saturated or longer chains. In *Escherichia coli*, recent work resolved this response into a temperature-sensitive fatty-acid flux valve plus transcriptional feedback, rather than merely a generic stress response. (hoogerland2024atemperaturesensitivemetabolic pages 1-2)

Other modules include protein folding and degradation, RNA structure and translation, DNA topology and repair, compatible-solute accumulation, ice management, oxidative-stress defense, and central-metabolic buffering. These systems often support growth within a thermal range but do not individually establish TOPT.

## Candidate nodes grouped by type

Identifiers below are supplied only where the grounding is unambiguous. **Label-only nodes are preferable to uncertain or invented CURIEs.** Gene symbols should additionally carry organism-specific locus or UniProt identifiers during implementation.

### Trait and assay nodes

| Candidate node | Suggested grounding or treatment | Curation note |
|---|---|---|
| temperature preference | `METPO:1000613` | Target trait; quote CURIE verbatim |
| minimum growth temperature, TMIN | Label-only or verified METPO term | Assay-derived cardinal parameter |
| optimal growth temperature, TOPT | Label-only or verified METPO term | Temperature maximizing a stated growth endpoint |
| maximum growth temperature, TMAX | Label-only or verified METPO term | Assay-derived upper growth boundary |
| specific growth rate | Label plus verified ontology term if available | Prefer μ from exponential growth |
| growth thermal performance curve | Label-only | Relation among temperature, μ, and cardinal parameters |
| growth medium, pH, oxygen availability, salinity, hydrostatic pressure, substrate, incubation time | ENVO/CHEBI terms after record-level verification | Experimental modifiers, not components of the organism |
| acute heat-shock survival; freeze–thaw survival | Separate phenotype nodes | Must not be merged into `METPO:1000613` |

### Environmental and physical nodes

- Environmental temperature and temperature shift.
- Low temperature; high temperature; freezing; heat shock; cold shock.
- Membrane fluidity/viscosity and lipid phase state.
- Reactive oxygen species and oxidative stress.
- Ice formation and ice recrystallization.
- Pressure, pH, oxygen, salinity, and water activity as interaction terms.

### Pathways and biological processes

- Homeoviscous adaptation.
- Type II fatty-acid biosynthesis and phospholipid biosynthesis.
- Saturated versus unsaturated fatty-acid branchpoint flux.
- Protein folding, refolding, disaggregation, and proteolysis.
- Cold-shock and heat-shock responses.
- RNA folding/chaperoning, RNA turnover, ribosome assembly, and translation.
- DNA supercoiling, DNA repair, and genome maintenance.
- Compatible-solute biosynthesis/transport.
- Exopolysaccharide production and ice-binding/antifreeze activity.
- Oxidative-stress response.
- Central-carbon metabolic and transcriptional buffering.

### Genes, proteins, enzymes, transporters, and complexes

**High-priority, perturbation-supported candidates**

- *E. coli*: FabI, FabA, FabB, FabF, FabR, FadR, PlsB, PlsC, and acyl carrier protein.
- *Bacillus subtilis*: DesK membrane thermosensor, DesR response regulator, and fatty-acid desaturase Des.
- Cyanobacteria: DesB/ω-3 desaturase, but only in a taxon-specific subgraph.
- Hyperthermophilic archaea: reverse gyrase (`rgy`); its molecular function is ATP-dependent introduction of positive DNA supercoils.
- DnaK–DnaJ–GrpE and GroEL–GroES chaperone systems; σ32/RpoH; Lon, Clp, HslUV, FtsH, and DegP proteases.
- Cold-shock proteins and RNA helicases.
- Ice-binding/antifreeze proteins, including DUF3494-containing proteins where sequence evidence is available.

### Chemicals and metabolites

Verified chemistry grounding can use:

- Palmitate / C16:0 — **CHEBI:7896**.
- cis-Vaccenate / C18:1 — use a verified CHEBI record at implementation; do not infer one from chain notation.
- Eicosapentaenoic acid — **CHEBI:28364**.
- Glycerol 3-phosphate — **CHEBI:15978**.
- Phosphatidic acid, phosphatidylethanolamine, and phosphatidylglycerol — use the appropriate class CURIEs after CHEBI verification.
- Glycine betaine — **CHEBI:17750**.
- Trehalose — **CHEBI:27082**.
- Glycerol — **CHEBI:17754**.
- Proline — **CHEBI:17203**.
- Reactive oxygen species — **CHEBI:26523**.
- Acyl-ACP species such as C16:0-ACP and C18:1-ACP — label-only unless a stable chemical/reaction identifier is verified.
- Triclosan and cerulenin — experimental inhibitors of FabI- and FabB-associated flux, respectively; ground only after record-level CHEBI verification.

### Cellular structures and localizations

- Cytoplasmic membrane / plasma membrane — **GO:0005886**.
- Cytoplasm — **GO:0005737**.
- Ribosome — **GO:0005840**.
- Nucleoid — **GO:0009295**.
- Cell envelope, outer membrane, and periplasm for Gram-negative taxa.
- Extracellular matrix/EPS layer.

## Candidate causal edges

The following table emphasizes edges most suitable for curation. “Strong” denotes direct genetic, inhibitor, overexpression, or controlled temperature-shift evidence. “Moderate” denotes a mechanistically coherent but taxon-limited or review-mediated claim.

| subject | predicate | object | taxon/assay scope | evidence level | key quantitative result | DOI |
|---|---|---|---|---|---|---|
| low temperature shift | decreases activity of | FabI enoyl-ACP reductase | *Escherichia coli*; defined minimal medium; temperature shock and in vitro enzyme comparison; growth adaptation, not just survival | strong, taxon-specific | FabI showed ~2-fold less activity at 27°C than 37°C; cold shock 37→13°C caused C16:0-ACP to decrease ~5-fold within 5 min (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4) | 10.1038/s41467-024-53677-5 |
| FabI/FabB branchpoint activity ratio | reallocates flux between | saturated vs unsaturated acyl-ACP pools | *E. coli* fatty-acid synthesis pathway; perturbations with temperature shock, triclosan, cerulenin, modeling | strong, taxon-specific | Triclosan phenocopied cold shock; cerulenin phenocopied heat shock; branchpoint temperature dependence was described as necessary and sufficient for membrane composition changes (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 6-7) | 10.1038/s41467-024-53677-5 |
| PlsB/PlsC acyl-ACP substrate pool composition | determines | phospholipid composition | *E. coli* exponential-phase cultures, 12–42°C LC-MS profiling | strong, taxon-specific | C16:0-ACP and 16:0 sn-1 phospholipids increased with temperature, while C18:1-ACP and 18:1 sn-1 phospholipids decreased; authors state phospholipid composition is determined by PlsB and PlsC substrate pools (hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 2-3) | 10.1038/s41467-024-53677-5 |
| unsaturated membrane phospholipids | increase | membrane fluidity / homeoviscous adaptation | general microbial principle, experimentally instantiated in *E. coli* | moderate; curate as higher-level physiology edge | Low temperatures reduce membrane fluidity; organisms counteract this by varying the proportion of unsaturated or branched-chain fatty acids to maintain a fixed viscosity across growth temperatures (hoogerland2024atemperaturesensitivemetabolic pages 1-2) | 10.1038/s41467-024-53677-5 |
| C18:1-ACP–FabR complex | represses expression of | fabB | *E. coli* transcriptional control of fatty-acid synthesis | strong, taxon-specific | Model and experiments support that decreased unsaturated precursor relieves fabB repression; ΔfabR abolishes temperature sensitivity of FabB expression (hoogerland2024atemperaturesensitivemetabolic pages 7-8, hoogerland2024atemperaturesensitivemetabolic pages 6-7, hoogerland2024atemperaturesensitivemetabolic pages 2-3) | 10.1038/s41467-024-53677-5 |
| FabR-mediated transcriptional feedback | accelerates | homeoviscous adaptation after temperature shock | *E. coli* wild type vs ΔfabR; cold-shock adaptation kinetics | strong, taxon-specific | Wild-type model and data show overshoot kinetics and ~90% adaptation within 1 generation; ΔfabR lacks overshoot and requires >1 generation (hoogerland2024atemperaturesensitivemetabolic pages 7-8) | 10.1038/s41467-024-53677-5 |
| reverse gyrase | enables growth at | >90°C temperature range | *Pyrococcus furiosus* deletion mutant in cellobiose minimal medium; sustained growth phenotype, not acute heat-shock survival | strong, taxon-specific | Δrgy grew comparably at 75–85°C, had ~half the control growth rate at 90°C and <half maximal density (OD680 0.093±0.003 vs 0.214±0.001), and showed no significant growth at 95 or 100°C (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2) | 10.1007/s00792-017-0929-z |
| cold-induced membrane rigidification | activates | DesK/DesR two-component system | *Bacillus subtilis*; cold-sensing/homeoviscous adaptation | moderate, taxon-specific | Review evidence identifies DesK as membrane-fluidity sensor and DesR as response regulator activated at low temperature (pathania2021adaptationtocold pages 220-223, pathania2021adaptationtocold pages 192-195) | 10.1007/978-981-16-2625-8_4 |
| DesK/DesR signaling | increases expression of | fatty-acid desaturase / unsaturation program | *B. subtilis* (general desaturase program) and cyanobacterial analogue in *Synechocystis* | moderate, taxon-specific | DesK/DesR controls desaturase regulation; related low-temperature signaling in *Synechocystis* increased desaturase gene expression including *desB* (ω-3 desaturase) (pathania2021adaptationtocold pages 220-223, pathania2021adaptationtocold pages 192-195) | 10.1007/978-981-16-2625-8_4 |
| eicosapentaenoic acid (EPA) production | supports | low-temperature cell division and growth | *Shewanella livingstonensis* Ac10 at 4°C | moderate, taxon-specific | Strain grows at 4°C and produces EPA; EPA-deficient mutants are cold-sensitive and filamentous with defective cell division at low temperature (pathania2021adaptationtocold pages 220-223) | 10.1007/978-981-16-2625-8_4 |
| dnaJ loss-of-function | increases acute resistance to | lethal heat shock | *Salmonella enterica* serovar Typhimurium; repeated severe heat-shock selection; stress-survival edge, not temperature-preference edge | strong but stress-survival-specific | Heat-shock resistance increased 1,000–100,000-fold in dnaJ mutants (berdejo2024evolutionarytradeoffbetween pages 8-10) | 10.1128/mbio.03105-23 |
| dnaJ loss-of-function | reduces sustained growth at | elevated growth temperatures | *S. Typhimurium* and *E. coli*; growth phenotype distinct from acute survival | strong but stress-survival-derived, taxon-specific | Mutants showed attenuated basal growth at 37°C and higher temperatures; maximum sustained growth temperature fell to 43°C for *S. Typhimurium* and 41°C for *E. coli* (berdejo2024evolutionarytradeoffbetween pages 8-10) | 10.1128/mbio.03105-23 |


*Table: This table summarizes the strongest candidate causal edges for curating microbial temperature preference, emphasizing perturbation-backed mechanisms and clearly flagging taxon-specific or stress-survival-specific claims. It is useful for selecting high-confidence TraitMech edges while separating broader physiological principles from assay-limited observations.*

### Additional moderate-confidence edges

| Subject | Predicate | Object | Supporting snippet | Reference and notes |
|---|---|---|---|---|
| low temperature | reduces | membrane fluidity | “low temperatures reduce membrane fluidity by increasing the packing of membrane lipids” | DOI [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5), published 30 October 2024. General physical edge. (hoogerland2024atemperaturesensitivemetabolic pages 1-2) |
| increased unsaturated/branched lipids | restores | membrane fluidity | organisms vary lipids that “disrupt membrane packing,” including unsaturated and branched-chain fatty acids | Same 2024 study; suitable as a process-level edge, but exact lipid implementation is taxon-specific. (hoogerland2024atemperaturesensitivemetabolic pages 1-2) |
| fatty-acid desaturase activity | increases | membrane-lipid unsaturation | psychrophiles replace saturated fatty acids with unsaturated species; DesK/DesR controls desaturase expression | DOI [10.1007/978-981-16-2625-8_4](https://doi.org/10.1007/978-981-16-2625-8_4), published December 2021. Review-mediated; retain taxon qualifier. (pathania2021adaptationtocold pages 220-223, pathania2021adaptationtocold pages 192-195) |
| compatible-solute accumulation | supports | low-temperature cellular protection | glycine betaine, trehalose, glycerol and related solutes depress freezing, stabilize proteins/membranes, and scavenge radicals | DOI [10.37256/amtt.5220244537](https://doi.org/10.37256/amtt.5220244537), published October 2024. Broad review claim; do not connect directly to TOPT without perturbation. (purwar2024adaptationsofpsychrophilic pages 10-11) |
| ice-binding proteins | inhibit | ice recrystallization | bacterial and algal IBPs mediate thermal hysteresis and ice-recrystallization inhibition | Same 2024 review. Curate under freezing survival or subzero growth rather than generic TOPT. (purwar2024adaptationsofpsychrophilic pages 6-7) |
| chaperones and proteases | maintain | proteostasis at high temperature | *E. coli* screening identified DnaK/DnaJ and ATP-dependent proteases among high-temperature factors | DOI [10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063), published 2 June 2011. The assay was sustained growth at 47°C, but effects remain strain-specific. (murata2011molecularstrategyfor pages 5-6, murata2011molecularstrategyfor pages 1-2) |
| oxidative-stress resistance | supports | growth at critical high temperature | more than half of 51 thermotolerant mutants were also H₂O₂-sensitive at 30°C | Same 2011 study; overlap supports a mechanistic module but not a single direct molecular edge. (murata2011molecularstrategyfor pages 1-2) |
| high temperature | increases need for | DNA repair/genome maintenance | knockout screening identified double-strand-break repair genes among factors required at 47°C | Same study; curate individual gene edges only from primary mutant data. (murata2011molecularstrategyfor pages 5-6, murata2011molecularstrategyfor pages 1-2) |

## Recent developments and quantitative findings

### 1. Rapid homeoviscous adaptation resolved mechanistically in 2024

Hoogerland and colleagues quantified *E. coli* fatty-acid enzymes, acyl-ACP intermediates, and phospholipids across 12–42°C and after temperature shifts. FabI had approximately twofold lower activity at 27°C than at 37°C. After a 37→13°C shift, C16:0-ACP fell about fivefold in five minutes, C18:1-ACP became the dominant PlsB substrate, and membrane phospholipids approached the 12°C state in roughly one generation. Conversely, a 13→37°C shift increased C16:0-ACP more than twofold and decreased C18:1-ACP twofold. (hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 3-4, hoogerland2024atemperaturesensitivemetabolic pages 4-5)

The study’s strongest causal inference comes from convergent perturbations: triclosan inhibition of FabI resembled cold shock; cerulenin inhibition of FabB resembled heat shock; `fabF` overexpression did not reproduce the cold response; and a `ΔfabF` strain retained temperature-dependent membrane composition. FabR deletion removed overshoot kinetics and delayed adaptation beyond one generation. Thus, the preferred graph module is **temperature → FabI/FabB relative flux → acyl-ACP pool → phospholipid composition → homeoviscous adaptation**, with **C18:1-ACP–FabR → repression of `fabB`** as feedback. (hoogerland2024atemperaturesensitivemetabolic pages 6-7, hoogerland2024atemperaturesensitivemetabolic pages 5-6, hoogerland2024atemperaturesensitivemetabolic pages 7-8)

### 2. Evolution can shift TOPT without immediately improving growth at the selection temperature

In 2023, *T. kivui* with ancestral TOPT 66°C was serially transferred at 45°C. After 67 transfers—approximately 180 generations—the evolved strain’s TOPT shifted to 60°C, but growth at 45°C did not improve. The evolved strain contained 67 SNPs and showed increased plasmalogens, while both evolved and ancestral strains increased short-chain fatty acids at 50°C relative to 66°C. The authors explicitly concluded that the causal molecular basis remained unresolved. These observations support **ALE at low temperature → lower TOPT** at phenotype level, but individual SNPs, regulators, cAMP-binding protein, and plasmalogens should not yet be asserted as causal. (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 8-9)

### 3. High-temperature growth can have a sharply defined molecular dependency

Deletion of reverse gyrase in *Pyrococcus furiosus* had little effect at 75–85°C, halved growth rate at 90°C, reduced final OD680 from 0.214±0.001 to 0.093±0.003, and abolished significant growth at 95 and 100°C. This is unusually strong evidence for a gene establishing the upper part of a growth-temperature range. The proposed mechanism—maintenance of DNA twist or genome stability—is plausible but remains less directly proven than the growth requirement itself. (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2)

### 4. Large-scale genomic associations remain hypothesis generators

A dataset of 21,498 cultured microbes linked growth temperatures to enzyme annotations. Among 18,135 experimentally characterized enzymes from 1,811 overlapping organisms, 51% had optima within ±10°C and 67% within ±15°C of organismal growth temperature. Averaging at least five enzymes raised correlation above 0.75; broader analyses reported correlations up to 0.89. The study found 319 temperature-associated EC functions, eight enriched KEGG pathways, and 33 associated DUFs. These are not causal edges because gene presence does not establish expression or function, culture-collection temperatures may not be true optima, and phylogeny can create spurious associations. (engqvist2018correlatingenzymeannotations pages 4-6, engqvist2018correlatingenzymeannotations pages 1-2, engqvist2018correlatingenzymeannotations pages 2-4, engqvist2018correlatingenzymeannotations pages 6-9)

## Applications and real-world implementations

1. **Predictive food microbiology.** Cardinal-temperature models estimate growth rates and boundaries across storage temperatures, supporting shelf-life, cold-chain, and pathogen-risk decisions. Temperature should be modeled jointly with pH, water activity, atmosphere, and food matrix rather than treated as an isolated trait. (noll2020modelingandexploiting pages 6-8, noll2020modelingandexploiting pages 19-20)
2. **Bioprocess control.** Temperature is routinely controlled near a growth or production optimum, while programmed shifts can redirect metabolism or separate biomass accumulation from product formation. The relevant optimum may therefore be μ, yield, or product-specific rather than TOPT. (noll2020modelingandexploiting pages 6-8)
3. **Low-temperature wastewater treatment.** *Bacillus simplex* H-b retained 27.22% nitrogen removal at 5°C; transcriptomic and physiological results implicated greater nitrogen assimilation, ATP/EPS accumulation, unsaturated fatty acids, transport, cofactor synthesis, translation, and stress responses. This is a promising application but the component-level claims are multi-omic associations rather than isolated causal perturbations. DOI [10.1128/aem.01928-22](https://doi.org/10.1128/aem.01928-22), published 31 January 2023.
4. **Cold-active biocatalysts and bioeconomy.** Psychrophilic enzymes can reduce heating requirements and enable food, detergent, environmental, and molecular-biological processes at low temperature. Cold-adapted hydrogen production is also under investigation, although slow metabolism, long lag phases, and low yields remain economic constraints. DOI [10.3389/fmicb.2023.1197797](https://doi.org/10.3389/fmicb.2023.1197797), published 23 June 2023; DOI [10.4314/ajcem.v24i3.1](https://doi.org/10.4314/ajcem.v24i3.1), published July 2023. (mohammed2023potentialsandlimitations pages 5-6)
5. **Climate and ecosystem modeling.** Thermal performance curves and plasticity determine how microbial primary producers and decomposers respond to warming and variability. Experiments with *Thalassiosira pseudonana* showed that fluctuations every 3–4 generations selected enhanced plasticity and thermal tolerance, whereas fluctuations spanning 30–40 generations generated two stable strategies. DOI [10.1098/rspb.2022.0834](https://doi.org/10.1098/rspb.2022.0834), published 17 August 2022. (schaum2022evolutionofthermal pages 5-6)
6. **Astrobiology and origins-of-life research.** Hyperthermophile growth limits, membrane chemistry, and reverse gyrase constrain models of habitability and early evolution. *P. furiosus*, for example, has TOPT 100°C and a reported 65–103°C growth range. (lehmann2023adaptivelaboratoryevolution pages 1-2)

## Expert assessment for TraitMech

The best initial graph is not a universal catalogue of every cold- or heat-induced molecule. It should contain a **small core of perturbation-backed modules**, with taxon qualifiers:

1. An *E. coli* membrane homeostasis module centered on FabI/FabB/FabR and acyl-ACP/phospholipid composition.
2. A *B. subtilis* DesK–DesR–desaturase cold-sensing module, marked taxon-specific and moderate confidence.
3. A *P. furiosus* reverse-gyrase/high-temperature-growth module.
4. Separate stress-response subgraphs for DnaJ/chaperones, compatible solutes, EPS, and ice-binding proteins that connect to survival or maintenance of growth, **not directly to TOPT unless cardinal-temperature effects are measured**.
5. An assay layer linking temperature and covariates to measured growth rate and the inferred TMIN/TOPT/TMAX.

This architecture distinguishes **proximal physical causes** (temperature alters enzyme activity and membrane packing), **homeostatic mechanisms** (lipid remodeling and feedback), and the final **assay phenotype** (temperature-dependent growth). It also prevents evidence for acute stress resistance from being misrepresented as evidence for preference.

## Claims that should not yet be curated as definitive causal edges

- **Any genome-wide correlation → temperature preference.** The 319 EC functions, eight pathways, and DUFs are discovery candidates, not causal mechanisms. (engqvist2018correlatingenzymeannotations pages 1-2, engqvist2018correlatingenzymeannotations pages 10-11)
- **A particular *T. kivui* SNP or plasmalogen increase → reduced TOPT.** The 2023 study did not validate individual mutations, and growth at the selection temperature did not improve. (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 8-9)
- **Heat-shock resistance → higher TOPT/TMAX.** `dnaJ` loss shows the opposite can occur. (berdejo2024evolutionarytradeoffbetween pages 8-10)
- **Chaperone induction → change in temperature preference.** Induction supports proteostasis but does not itself demonstrate a shifted thermal performance curve.
- **Compatible solutes, EPS, pigments, carotenoids, or IBPs → lower TOPT.** Most evidence concerns protection, freezing survival, or expression under cold conditions. (purwar2024adaptationsofpsychrophilic pages 6-7, mohammed2023potentialsandlimitations pages 5-6, purwar2024adaptationsofpsychrophilic pages 10-11)
- **Archaeal tetraether/cyclopentane lipids → thermophily as a universal rule.** Temperature, pH, pressure, oxygen, and taxonomy confound lipid distributions; use only strain-specific perturbation evidence.
- **Reverse gyrase → positive DNA supercoiling → growth above 90°C as a fully demonstrated chain.** The gene-to-growth edge is strong, but the intervening DNA-topology mechanism remains partly inferred. (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2)
- **Membrane adaptation alone → TOPT.** Homeoviscous adaptation is necessary in many microbes but TOPT also reflects proteome, nucleic-acid, translation, energy, and repair constraints.
- **Culture-collection “growth temperature” → true TOPT.** Reported cultivation temperatures may be convenient conditions rather than experimentally fitted optima. (engqvist2018correlatingenzymeannotations pages 2-4)

## DOI-first bibliography

1. **Hoogerland L, et al.** “A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in *Escherichia coli*.” *Nature Communications* 15, 9386. **Published 30 October 2024.** DOI: [10.1038/s41467-024-53677-5](https://doi.org/10.1038/s41467-024-53677-5). (hoogerland2024atemperaturesensitivemetabolic pages 1-2)
2. **Berdejo D, et al.** “Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in *Salmonella* Typhimurium.” *mBio* 15. **Published March 2024.** DOI: [10.1128/mbio.03105-23](https://doi.org/10.1128/mbio.03105-23). (berdejo2024evolutionarytradeoffbetween pages 8-10)
3. **Lehmann M, et al.** “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14:1265216. **Published 12 October 2023.** DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). (lehmann2023adaptivelaboratoryevolution pages 1-2)
4. **Ramón A, et al.** “A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.” *Brazilian Journal of Microbiology* 54:2259–2287. **Published July 2023.** DOI: [10.1007/s42770-023-01057-4](https://doi.org/10.1007/s42770-023-01057-4). (ramon2023ageneraloverview pages 1-2)
5. **Moon S, et al.** “Temperature Matters: Bacterial Response to Temperature Change.” *Journal of Microbiology* 61:343–357. **Published March 2023.** DOI: [10.1007/s12275-023-00031-x](https://doi.org/10.1007/s12275-023-00031-x).
6. **Riccardi C, et al.** “Metabolic Robustness to Growth Temperature of a Cold-Adapted Marine Bacterium.” *mSystems* 8. **Published April 2023.** DOI: [10.1128/msystems.01124-22](https://doi.org/10.1128/msystems.01124-22).
7. **Yang Q, et al.** “Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: *Bacillus simplex* H-b.” *Applied and Environmental Microbiology* 89. **Published 31 January 2023.** DOI: [10.1128/aem.01928-22](https://doi.org/10.1128/aem.01928-22).
8. **Lipscomb GL, et al.** “Reverse gyrase is essential for microbial growth at 95°C.” *Extremophiles* 21:603–608. **Published 20 March 2017.** DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z). (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2)
9. **Engqvist MKM.** “Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures.” *BMC Microbiology* 18. **Published 20 November 2018.** DOI: [10.1186/s12866-018-1320-7](https://doi.org/10.1186/s12866-018-1320-7). (engqvist2018correlatingenzymeannotations pages 4-6, engqvist2018correlatingenzymeannotations pages 1-2)
10. **Noll P, et al.** “Modeling and Exploiting Microbial Temperature Response.” *Processes* 8:121. **Published 21 January 2020.** DOI: [10.3390/pr8010121](https://doi.org/10.3390/pr8010121). (noll2020modelingandexploiting pages 6-8)
11. **Hassan N, et al.** “Temperature Driven Membrane Lipid Adaptation in Glacial Psychrophilic Bacteria.” *Frontiers in Microbiology* 11:824. **Published 15 May 2020.** DOI: [10.3389/fmicb.2020.00824](https://doi.org/10.3389/fmicb.2020.00824).
12. **Murata M, et al.** “Molecular Strategy for Survival at a Critical High Temperature in *Escherichia coli*.” *PLoS ONE* 6:e20063. **Published 2 June 2011.** DOI: [10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063). (murata2011molecularstrategyfor pages 5-6, murata2011molecularstrategyfor pages 1-2)

**Recommended curation priority:** begin with the strong *E. coli* FabI/FabB/FabR module and the *P. furiosus* reverse-gyrase edge; add the DesK/DesR and cold-protection modules only as explicitly taxon-specific, confidence-qualified subgraphs. Every terminal edge to `METPO:1000613` should carry the growth assay, temperature range, endpoint, and strain context.

References

1. (noll2020modelingandexploiting pages 6-8): Philipp Noll, Lars Lilge, Rudolf Hausmann, and Marius Henkel. Modeling and exploiting microbial temperature response. ArXiv, 8:121, Jan 2020. URL: https://doi.org/10.3390/pr8010121, doi:10.3390/pr8010121. This article has 73 citations.

2. (noll2020modelingandexploiting pages 19-20): Philipp Noll, Lars Lilge, Rudolf Hausmann, and Marius Henkel. Modeling and exploiting microbial temperature response. ArXiv, 8:121, Jan 2020. URL: https://doi.org/10.3390/pr8010121, doi:10.3390/pr8010121. This article has 73 citations.

3. (lehmann2023adaptivelaboratoryevolution pages 2-3): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

4. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

5. (berdejo2024evolutionarytradeoffbetween pages 8-10): Daniel Berdejo, Julien Mortier, Alexander Cambré, Malgorzata Sobota, Ronald Van Eyken, Tom Dongmin Kim, Kristof Vanoirbeek, Diego García Gonzalo, Rafael Pagán, Médéric Diard, and Abram Aertsen. Evolutionary trade-off between heat shock resistance, growth at high temperature, and virulence expression in <i>salmonella</i> typhimurium. mBio, Mar 2024. URL: https://doi.org/10.1128/mbio.03105-23, doi:10.1128/mbio.03105-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (engqvist2018correlatingenzymeannotations pages 4-6): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

7. (engqvist2018correlatingenzymeannotations pages 9-10): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

8. (lehmann2023adaptivelaboratoryevolution pages 8-9): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

9. (hoogerland2024atemperaturesensitivemetabolic pages 1-2): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

10. (hoogerland2024atemperaturesensitivemetabolic pages 5-6): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

11. (hoogerland2024atemperaturesensitivemetabolic pages 3-4): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

12. (hoogerland2024atemperaturesensitivemetabolic pages 6-7): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

13. (hoogerland2024atemperaturesensitivemetabolic pages 2-3): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

14. (hoogerland2024atemperaturesensitivemetabolic pages 7-8): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

15. (lipscomb2017reversegyraseis pages 2-4): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

16. (lipscomb2017reversegyraseis pages 1-2): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

17. (pathania2021adaptationtocold pages 220-223): Shruti Pathania, Preeti Solanki, Chayanika Putatunda, Ravi Kant Bhatia, and Abhishek Walia. Adaptation to cold environment: the survival strategy of psychrophiles. Survival Strategies in Cold-adapted Microorganisms, pages 87-111, Dec 2021. URL: https://doi.org/10.1007/978-981-16-2625-8\_4, doi:10.1007/978-981-16-2625-8\_4. This article has 27 citations.

18. (pathania2021adaptationtocold pages 192-195): Shruti Pathania, Preeti Solanki, Chayanika Putatunda, Ravi Kant Bhatia, and Abhishek Walia. Adaptation to cold environment: the survival strategy of psychrophiles. Survival Strategies in Cold-adapted Microorganisms, pages 87-111, Dec 2021. URL: https://doi.org/10.1007/978-981-16-2625-8\_4, doi:10.1007/978-981-16-2625-8\_4. This article has 27 citations.

19. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

20. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

21. (murata2011molecularstrategyfor pages 5-6): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

22. (murata2011molecularstrategyfor pages 1-2): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

23. (hoogerland2024atemperaturesensitivemetabolic pages 4-5): Loles Hoogerland, Stefan Pieter Hendrik van den Berg, Yixing Suo, Yuta W. Moriuchi, Adja Zoumaro-Djayoon, Esther Geurken, Flora Yang, Frank Bruggeman, Michael D. Burkart, and Gregory Bokinsky. A temperature-sensitive metabolic valve and a transcriptional feedback loop drive rapid homeoviscous adaptation in escherichia coli. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-53677-5, doi:10.1038/s41467-024-53677-5. This article has 26 citations and is from a highest quality peer-reviewed journal.

24. (engqvist2018correlatingenzymeannotations pages 1-2): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

25. (engqvist2018correlatingenzymeannotations pages 2-4): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

26. (engqvist2018correlatingenzymeannotations pages 6-9): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

27. (mohammed2023potentialsandlimitations pages 5-6): A. Mohammed, M. F. Abdul-Wahab, J. N. Mohammed, L. Mohammed I, R. A. Sani, and H. Majiya. Potentials and limitations of cold-adapted hydrogen producing bacteria: a mini review. African Journal of Clinical and Experimental Microbiology, 24:222-234, Jul 2023. URL: https://doi.org/10.4314/ajcem.v24i3.1, doi:10.4314/ajcem.v24i3.1. This article has 1 citations.

28. (schaum2022evolutionofthermal pages 5-6): C.-E. Schaum, A. Buckling, N. Smirnoff, and G. Yvon-Durocher. Evolution of thermal tolerance and phenotypic plasticity under rapid and slow temperature fluctuations. Proceedings of the Royal Society B: Biological Sciences, Aug 2022. URL: https://doi.org/10.1098/rspb.2022.0834, doi:10.1098/rspb.2022.0834. This article has 54 citations.

29. (engqvist2018correlatingenzymeannotations pages 10-11): Martin K. M. Engqvist. Correlating enzyme annotations with a large set of microbial growth temperatures reveals metabolic adaptations to growth at diverse temperatures. BMC Microbiology, Nov 2018. URL: https://doi.org/10.1186/s12866-018-1320-7, doi:10.1186/s12866-018-1320-7. This article has 103 citations and is from a peer-reviewed journal.

30. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 20 citations and is from a peer-reviewed journal.