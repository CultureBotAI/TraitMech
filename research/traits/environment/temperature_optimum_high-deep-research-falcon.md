---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T03:45:16.335964'
end_time: '2026-08-04T03:55:43.483338'
duration_seconds: 627.15
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature optimum high
  trait_identifier: METPO:1000447
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_optimum_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature optimum phenotype with the best-growth ambient temperature\
    \ above approximately 40 \xB0C, characteristic of thermophilic physiology."
  parent_traits: METPO:1000304
  synonyms: Thermophile, TO_>40
  evidence_summary: "DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of\
    \ high temperature (Thermophile-adaptation review supports the >40 \xB0C optimum\
    \ as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to\
    \ irreversible inactivation at high temperatures (Thermostable-protein review\
    \ supports thermostable proteins as the mechanism enabling thermophile optima.)"
  causal_graph_summary: 'temperature_optimum_high_thermophile_setpoint: 16 nodes,
    10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Thermophile, TO_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the >40 °C optimum as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostable proteins as the mechanism enabling thermophile optima.)
- **Existing causal graph summary:** temperature_optimum_high_thermophile_setpoint: 16 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_high.yaml`.

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
- **Trait label:** temperature optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Thermophile, TO_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the >40 °C optimum as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostable proteins as the mechanism enabling thermophile optima.)
- **Existing causal graph summary:** temperature_optimum_high_thermophile_setpoint: 16 nodes, 10 edges

## Research Objective

Research the microbial trait **temperature optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_high.yaml`.

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


# Curation report: microbial **temperature optimum high**

**Trait:** “temperature optimum high”  
**Identifier:** **METPO:1000447**  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** METPO:1000304  
**Operational definition:** best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.

## 1. Scope and boundaries

This trait should represent an **organism-level growth optimum**, determined from a growth-rate or biomass-yield curve across temperatures. It is not equivalent to: (i) survival after acute heat shock, (ii) maximum permissive growth temperature, (iii) heat resistance of spores or resting cells, or (iv) thermostability of an isolated protein. Those properties can be mechanistic contributors or associated phenotypes, but do not establish **METPO:1000447** by themselves.

The approximately 40 °C threshold includes moderately thermophilic organisms and creates boundary cases near 40–45 °C. Classification schemes vary: one recent synthesis subdivides thermophiles into moderate thermophiles at roughly 50–60 °C, extreme thermophiles at 60–80 °C, and hyperthermophiles at 80–110 °C. These narrower labels should not replace the supplied METPO cutoff (pandey2026extremethermalenvironments pages 5-6).

A robust annotation should therefore record: medium composition, pH, oxygen/electron donor and acceptor, pressure, salinity, temperature spacing, growth metric, replicate number, and fitted optimum. This matters because temperature optimum is conditional: changing salinity, pressure, pH, or substrate can shift apparent growth performance.

### Closely related but distinct traits

- **Thermotolerance/heat resistance:** survival or retained growth after supra-optimal heat exposure. For example, an *E. coli* screen at 47 °C identified high-temperature survival genes, but *E. coli* remains mesophilic; those results support generic heat-damage mechanisms, not a thermophilic optimum (murata2011molecularstrategyfor pages 1-2).
- **Protein thermostability:** resistance of a protein to irreversible inactivation. It is a molecular property and plausible enabling mechanism, not an organismal optimum.
- **Hyperthermophily:** a narrower high-temperature class, commonly associated with optima ≥80 °C. Reverse gyrase evidence below is strongest in this range and should not be generalized automatically to organisms with optima of 41–60 °C.
- **High maximum growth temperature:** an organism may grow weakly at a high temperature while having a lower optimum.
- **Acclimation:** reversible lipid, solute, or expression changes after a temperature shift; distinct from the evolved trait setpoint.

## 2. Mechanistic model and candidate nodes

The current understanding is **multifactorial**. High-temperature growth requires maintenance of macromolecular structure, DNA topology and repair, membrane permeability, translation/protein quality control, and energy balance. No single mechanism is universal across Bacteria and Archaea.

### Environmental and assay nodes

- high ambient temperature / cultivation temperature
- temperature gradient assay
- optimal growth temperature
- supra-optimal heat stress
- pH, salinity, hydrostatic pressure, oxygen concentration
- electron-donor and electron-acceptor availability
- specific growth rate and maximum cell density
- target trait: **METPO:1000447**

### Organisms and taxonomic contexts

- *Pyrococcus furiosus* — hyperthermophilic archaeon; direct reverse-gyrase and compatible-solute experiments
- *Thermococcus kodakarensis* — hyperthermophilic archaeal genetic model
- *Saccharolobus islandicus* and *Sulfolobus acidocaldarius* — thermoacidophilic archaeal membrane models
- *Thermus thermophilus* — extreme-thermophile bacterial model
- *Escherichia coli* — mesophilic heat-stress comparator, **not** direct evidence for thermophile optimum
- *Kluyveromyces marxianus* — thermotolerant yeast engineering context

Use NCBITaxon identifiers only after strain/species verification in the source. A broad node such as **NCBITaxon:2157** (Archaea) is safe but less informative than source-specific organism nodes.

### Genes, proteins, and complexes

- **reverse gyrase / rgy** — ATP-dependent topoisomerase and DNA-binding heat-protective factor; exact UniProt accession is strain-specific
- **GrsA and GrsB** — radical-SAM GDGT ring synthases; label-only until organism-specific protein accessions are verified
- **DnaK/DnaJ/GrpE**, **GroEL/GroES**, archaeal thermosome/chaperonin
- **ClpB/ClpG**, Lon, HslUV, FtsH, DegP — disaggregation/proteolysis modules
- **Phr** — archaeal heat-response transcriptional regulator implicated in DIP-pathway regulation
- **MPGS** — mannosyl-3-phosphoglycerate synthase
- **IPCT/DIPPS** — enzymes used in di-myo-inositol-phosphate biosynthesis
- DNA repair, tRNA modification, translation-control, and cell-division systems identified in high-temperature screens

Conservative GO candidates include **GO:0006457** (protein folding), **GO:0051082** (unfolded-protein binding), **GO:0006281** (DNA repair), and **GO:0003677** (DNA binding). More specific GO molecular-function terms should be checked against the exact protein and assay before YAML insertion.

### Chemicals and molecular structures

- glycerol dibiphytanyl glycerol tetraethers (**GDGTs**)
- cyclopentane-containing GDGTs
- archaeal tetraether versus diether lipids
- **di-myo-inositol phosphate (DIP)**
- **mannosylglycerate (MG)**
- ATP, reactive oxygen species, unfolded/aggregated proteins

MG, DIP, and complex GDGT species should remain label-only until their exact ChEBI records and stereochemistry are curator-verified.

### Processes and cellular functions

- homeoviscous membrane adaptation
- GDGT cyclization and tetraether-lipid biosynthesis
- maintenance of membrane packing and permeability
- protein folding, disaggregation, and proteolysis
- DNA topology control and protection from thermal strand breakage
- compatible-solute biosynthesis/accumulation
- oxidative-stress defense
- translation and tRNA modification

## 3. Candidate causal edges

The following table summarizes the most useful edges before source-level detail.

| priority | subject | predicate | object | evidence strength | key experiment/statistic | scope limitation |
|---|---|---|---|---|---|---|
| High | reverse gyrase | enables growth at | very high temperature / temperature optimum high | Strong direct genetic | In *Pyrococcus furiosus*, Δrgy grew comparably at 75–85 °C, showed ~50% growth-rate reduction at 90 °C, and no significant growth at 95–100 °C | Strongest for hyperthermophiles; threshold appears taxon-specific and may not generalize to all >40 °C organisms |
| High | reverse gyrase | protects | DNA from heat-induced breakage | Strong direct biochemical | In vitro, reverse gyrase reduced double-stranded DNA breakage ~8-fold at 90 °C | Biochemical protection assay, not by itself a growth-optimum phenotype |
| Medium | elevated temperature | increases accumulation of | di-myo-inositol phosphate (DIP) | Strong direct physiological | In *P. furiosus* at 98 °C versus 90 °C, DIP increased ~7-fold and reached ~20% of total solutes | Demonstrated in a hyperthermophilic archaeon; solute response may differ across taxa |
| Medium | mannosylglycerate (MG) and DIP | redundantly support | thermoprotection / adaptation to supra-optimal temperature | Moderate direct genetic | MG-deficient mutant compensated with ~3-fold more DIP; under 98 °C heat stress, parent, MG-deficient, and DIP-deficient strains had broadly similar growth profiles | Supports heat adaptation more than baseline thermophile setpoint; redundancy complicates single-edge curation |
| Medium | GDGT ring synthases GrsA/GrsB | catalyze | GDGT cyclization | Strong direct enzymology / genetics | GrsA and GrsB identified as enzymes introducing cyclopentane rings at distinct positions in archaeal tetraether lipids | Mechanistically solid, but linkage to the trait is indirect unless paired with growth/fitness evidence |
| Medium | increased GDGT cyclization | increases | membrane packing / transition temperature | Moderate direct biophysical | Liposome and calorimetry studies showed more cyclopentane rings associated with higher transition temperatures and tighter packing; high-tetraether liposomes tolerated sterilization conditions | Mostly model-membrane evidence; cellular growth-optimum consequences not directly quantified |
| Low-Medium | grs copy number / grs expression | associates with | hotter growth environments and stress response | Correlative / uncertain | Hot-spring comparative genomics found only weak positive correlation with temperature, while stress-expression work showed condition-dependent grs regulation | Not yet sufficient alone for TraitMech causal curation of high temperature optimum |
| Medium | protein quality control systems (e.g., DnaK/DnaJ, GroEL, proteases) | support | survival/growth at critical high temperature | Moderate direct genetic | In *E. coli* at 47 °C, genome-wide knockout screening identified 51 thermotolerant genes, with chaperone and proteostasis functions among required systems | Mesophilic heat-survival model, not a native thermophile optimum phenotype |
| Low-Medium | chaperone upregulation | responds to | high-temperature adaptation | Direct but context-specific | 2024 high-temperature adaptation work and thermotolerance engineering studies reported chaperone upregulation during adaptation or screening at elevated temperature | Often reflects acclimation or engineering in specific systems rather than a universally curatable cause of thermophile optimum |


*Table: This table ranks candidate causal edges for curation of the high-temperature optimum trait by directness and evidential strength. It is useful for separating strong mechanistic edges from correlative or heat-shock-specific findings that may require caution.*

### Edge-level evidence table

| Candidate subject–predicate–object triple | Reference | Supporting snippet or quantitative result | Curation assessment |
|---|---|---|---|
| **reverse gyrase — enables — growth above 90 °C** | Lipscomb et al., 2017, DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z) | In *P. furiosus*, Δrgy and controls grew comparably at 75–85 °C; at 90 °C the mutant had about half the growth rate and less than half the maximum density; at 95 and 100 °C it showed no significant growth (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 4-5). | **Strong, direct genetic evidence; curate with taxon and temperature qualifier.** It supports hyperthermophilic growth, not every >40 °C optimum. |
| **reverse gyrase — increases — high-temperature growth rate** | Atomi et al., 2004, DOI: [10.1128/JB.186.14.4829-4833.2004](https://doi.org/10.1128/JB.186.14.4829-4833.2004) | In *T. kodakarensis*, wild type reached μ=0.69 h⁻¹ at 85 °C, whereas Δrgy reached a maximum of 0.40 h⁻¹ at 75 °C. The mutant/control growth-rate ratio fell to 0.49 at 85 °C and 0.46 at 90 °C; no mutant growth occurred at 93 °C over 49 h (atomi2004reversegyraseis pages 3-5). | **Strong and highly informative.** Prefer “contributes to” rather than universally “required for,” because growth remained possible at 90 °C. |
| **reverse gyrase — protects — DNA from heat-induced breakage** | Kampmann & Stock, 2004, DOI: [10.1093/nar/gkh683](https://doi.org/10.1093/nar/gkh683) | Reverse gyrase reduced double-stranded DNA breakage approximately eightfold at 90 °C; protection was described as DNA-chaperone activity independent of supercoiling (kampmann2004reversegyrasehas pages 1-2). | **Strong biochemical edge.** Link onward to growth only through the organismal knockout studies. |
| **reverse gyrase — positively supercoils/removes negative supercoils from — DNA** | Villain et al., 2021, DOI: [10.1093/nar/gkab869](https://doi.org/10.1093/nar/gkab869) | The study describes reverse gyrase as a topoisomerase able to positively supercoil DNA and remove negative supercoils; deletion is lethal at 93 °C in *T. kodakarensis* and 95 °C in *P. furiosus* (villain2021thehyperthermophilicarchaeon pages 11-12). | **Mechanistically credible**, but do not assert that positive supercoiling alone explains thermoprotection; the mechanism remains more complex. |
| **high temperature — increases — DIP accumulation** | Esteves et al., 2014, DOI: [10.1128/AEM.00559-14](https://doi.org/10.1128/AEM.00559-14) | At 98 versus 90 °C in *P. furiosus*, DIP increased sevenfold and represented 20% of the solute pool; final OD600 fell from 0.88 to 0.32 under heat stress (esteves2014mannosylglycerateanddi pages 9-12). | **Direct physiological response.** It is evidence for acclimation at a supra-optimal temperature, not by itself for the evolved optimum. |
| **Phr-mediated heat response — permits — DIP-biosynthesis-gene transcription** | Esteves et al., 2014, same DOI | The source reports that Phr blocks DIP-pathway transcription at optimal temperature but permits it at higher temperature (esteves2014mannosylglycerateanddi pages 16-20). | **Candidate regulatory edge.** Verify exact target genes and promoter evidence before final curation. |
| **MG and DIP — redundantly support — thermoprotection** | Esteves et al., 2014, same DOI | The MG-deficient mutant increased DIP about threefold, making it 55% of the solute pool. Parent, MG-deficient, and DIP-deficient strains had similar growth at 98 °C, supporting “interchangeable roles in thermoprotection” (esteves2014mannosylglycerateanddi pages 16-20, esteves2014mannosylglycerateanddi pages 9-12). | **Moderate direct genetic evidence for redundancy.** Do not encode either solute as individually necessary. A redundant/compensatory relation is essential. |
| **MG synthesis — supports — growth under combined heat and salt stress** | Cario et al., 2016, DOI: [10.1038/srep29483](https://doi.org/10.1038/srep29483) | Two MG-deficient *T. barophilus* mutants had lower growth rates at 90 °C plus 4% NaCl; MG was not detected under heat stress at optimal salinity (cario2016molecularchaperoneaccumulation pages 3-4). | **Conditional and taxon-specific.** Curate only with combined-stress qualifiers; not a general high-temperature edge. |
| **GrsA/GrsB — catalyze — GDGT cyclopentane-ring formation** | Chiu et al., 2023, DOI: [10.3389/fmicb.2023.1219779](https://doi.org/10.3389/fmicb.2023.1219779); Rastädter et al., 2020, DOI: [10.3390/ijms21113935](https://doi.org/10.3390/ijms21113935) | GrsA and GrsB introduce rings at distinct positions; the 2023 experiment compared optimal 76 °C with cold stress at 66 °C and detected condition-dependent lipid and expression responses (chiu2023membranelipidand pages 2-3, rastadter2020thecellmembrane pages 5-7). | **Strong enzyme-to-product edge.** The downstream edge to high-temperature optimum remains indirect. |
| **increased GDGT cyclization — increases — membrane packing/transition temperature** | Rastädter et al., 2020, same DOI | Calorimetry and liposome studies associated more rings with higher transition temperature and packing; tetraether-rich liposomes had lower compressibility and withstood 121 °C sterilization (rastadter2020thecellmembrane pages 5-7). | **Biophysical, mostly cell-free evidence.** Curate as a membrane-property edge, not direct proof of growth optimum. |
| **higher temperature — increases — GDGT cyclization** | Blum et al., 2023, DOI: [10.1111/1462-2920.16375](https://doi.org/10.1111/1462-2920.16375) | Prior cultures systematically increased cyclization with increased temperature, but the hot-spring survey found only a weak positive association between grs distribution and temperature (blum2023distributionandabundance pages 2-2). | **Uncertain/correlational at graph-trait level.** pH and energy limitation are major confounders. |
| **grs copy number — associates with — thermal-environment distribution** | Blum et al., 2023, same DOI | Analysis included 30 isolates and 474 grs-bearing MAGs; temperature distributions differed between one- and two-copy isolates (Kruskal–Wallis p=3.6×10⁻³), but pH was the stronger ecological correlate (blum2023distributionandabundance pages 6-7). | **Do not curate as causal.** Suitable as supporting association metadata only. |
| **DnaK/DnaJ and protein-quality-control systems — support — growth/survival at 47 °C** | Murata et al., 2011, DOI: [10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063) | A genome-wide *E. coli* knockout screen identified 51 thermotolerant genes, 43 newly implicated; functions included protein quality control, outer-membrane organization, DNA repair, translation, and cell division. More than half of mutants were also H₂O₂-sensitive (murata2011molecularstrategyfor pages 1-2). | **Useful damage-response module, but indirect for METPO:1000447.** Mark mesophile/critical-temperature assay. |
| **CYR1 N1546K mutation — reduces cAMP and increases — thermotolerance/recombinant-protein output** | Ren et al., 2024, DOI: [10.1038/s42003-024-06341-z](https://doi.org/10.1038/s42003-024-06341-z) | Screening at 46 °C identified a *K. marxianus* variant; CRISPR validation connected reduced adenylate-cyclase activity/cAMP with altered energy supply, biosynthesis, and stress resistance (ren2024couplingthermotoleranceand pages 1-2). | **Recent direct engineering evidence**, but mutation-specific and eukaryotic; curate in a strain-engineering graph, not as a universal thermophile mechanism. |

## 4. Recommended initial TraitMech graph

A conservative first-pass graph should emphasize direct causality and retain taxon-specific branches:

1. **high ambient temperature** → *causes* → protein unfolding/aggregation  
2. **protein unfolding/aggregation** → *activates* → chaperone/disaggregase/protease systems  
3. **protein-quality-control systems** → *maintain* → functional proteome  
4. **functional proteome** → *supports* → **METPO:1000447**

5. **high ambient temperature** → *increases* → DNA strand-break/topology stress  
6. **reverse gyrase** → *protects* → DNA from heat-induced breakage  
7. **reverse gyrase** → *supports* → growth above 90 °C  
8. **growth above 90 °C** → *is_a/narrower manifestation of* → **METPO:1000447**

9. **GrsA/GrsB** → *catalyze* → GDGT cyclization  
10. **GDGT cyclization** → *increases* → membrane packing/transition temperature  
11. **membrane physical homeostasis** → *supports* → high-temperature growth **[indirect/uncertain]**

12. **supra-optimal temperature** → *increases* → DIP accumulation  
13. **DIP** ↔ *functionally compensates for* ↔ **MG**  
14. **DIP/MG pool** → *supports* → thermoprotection **[redundant, taxon-specific]**

Edges 6–8 have the strongest organismal causal evidence. Edges 9–10 are mechanistically strong but lack a decisive growth-optimum perturbation in the retrieved evidence. Edges 12–14 concern acute/supra-optimal adaptation and should sit in a stress-response branch rather than define the core trait.

## 5. Recent developments, applications, and expert assessment

### 2023–2024 research

Recent archaeal membrane work has shifted from treating GDGT cyclization as a simple temperature proxy toward a multivariable model. The 2023 global hot-spring analysis found grs homologs in 12 archaeal classes and analyzed 474 high-quality grs-bearing MAGs; pH was a stronger correlate than temperature, warning against a universal “more grs means more thermophilic” edge (blum2023distributionandabundance pages 6-7, blum2023distributionandabundance pages 2-2). A separate 2023 multi-omics study of *S. islandicus* compared its 76 °C optimum with 66 °C cold stress and showed that transcript abundance alone did not reliably predict the final GDGT composition, reinforcing the need to curate enzyme activity and lipid phenotype separately (chiu2023membranelipidand pages 2-3).

A 2024 *K. marxianus* study demonstrated that thermotolerance can be engineered through signaling rather than by transferring a single thermostable enzyme: CYR1 N1546K reduced cAMP and improved both heat resistance and recombinant-protein production (ren2024couplingthermotoleranceand pages 1-2). This is valuable applied evidence, but it concerns an engineered thermotolerance phenotype rather than proof that CYR1 establishes a natural >40 °C optimum.

### Real-world implementations

Thermophiles and their enzymes are established or emerging platforms for:

- **Thermostable DNA-processing enzymes** and molecular biology workflows.
- **High-temperature whole-cell biocatalysis**, where elevated temperature can improve substrate solubility, reduce cooling demand, and lower contamination risk.
- **Lignocellulose conversion and fermentation**, using thermostable hydrolases and thermophilic production hosts.
- **Archaeosomes**, liposomes made partly or wholly from archaeal ether lipids, investigated for delivery of vaccines, proteins, peptides, and nucleic acids; their attraction follows the low compressibility and high thermal robustness of tetraether-rich membranes (rastadter2020thecellmembrane pages 5-7).
- **Thermophile genome engineering.** Genetic systems in archaeal and bacterial thermophiles increasingly permit causal testing rather than comparative inference.
- **Thermotolerant recombinant-protein production**, exemplified by the 2024 CYR1 engineering study (ren2024couplingthermotoleranceand pages 1-2).

The expert consensus emerging from these studies is that thermophily is a systems phenotype. Protein thermostability is important, but membrane remodeling, DNA maintenance, proteostasis, compatible-solute redundancy, and energy/redox constraints all contribute. The balance differs by lineage and temperature range.

## 6. Ontology-grounding recommendations

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| temperature optimum high | **METPO:1000447** | Use verbatim as requested. |
| protein folding | **GO:0006457** | Appropriate process node. |
| unfolded-protein binding | **GO:0051082** | Suitable for molecular chaperones when experimentally supported. |
| DNA repair | **GO:0006281** | Broad node; use specific repair term if known. |
| DNA binding | **GO:0003677** | Broad; reverse-gyrase-specific activity should be refined after GO lookup. |
| reverse gyrase | label plus organism-specific UniProt accession | Do not use one accession across taxa. |
| GrsA / GrsB | label plus organism-specific gene/protein accession | Verify strain and locus before insertion. |
| GDGT cyclization | label-only candidate | Seek GO/Rhea term; do not invent one. |
| GDGT species | label-only candidate | Exact structure and ring number determine chemical identity. |
| DIP / MG | label-only pending ChEBI verification | Verify stereochemistry and protonation state. |
| *P. furiosus*, *T. kodakarensis*, *S. islandicus* | NCBITaxon species/strain CURIE after source verification | Prefer strain-level grounding where perturbations are strain-specific. |

## 7. Claims not yet suitable for curation

1. **“Reverse gyrase causes thermophily in all thermophiles.”** Evidence supports a strong requirement above roughly 90–95 °C in tested archaea, not across the full >40 °C class. At 90 °C, a reverse-gyrase-null *T. kodakarensis* strain still grew, albeit slowly (atomi2004reversegyraseis pages 3-5).
2. **“More genomic GC content causes a high temperature optimum.”** This remains confounded by phylogeny and genomic context and lacks a clean causal perturbation here.
3. **“grs copy number causes thermophily.”** The 2023 survey is correlational, and pH was the stronger association (blum2023distributionandabundance pages 6-7, blum2023distributionandabundance pages 2-2).
4. **“Greater GDGT cyclization always increases cellular heat fitness.”** Liposome biophysics supports packing effects, but cell-level knockout-to-growth evidence is incomplete; maximum rigidity did not simply track maximum ring number (rastadter2020thecellmembrane pages 5-7).
5. **“DIP or MG is individually essential for heat growth.”** Single mutants were compensated by the other solute and had broadly similar growth at 98 °C (esteves2014mannosylglycerateanddi pages 16-20, esteves2014mannosylglycerateanddi pages 9-12).
6. **“Trehalose is a universal archaeal thermoprotectant.”** Retrieved deletion evidence in *S. acidocaldarius* showed a salt-stress requirement but no heat-stress phenotype; it should not enter this graph without additional direct evidence.
7. **“Heat-shock induction establishes the temperature optimum.”** Expression changes can be consequences of stress; they need perturbation and growth-curve validation.
8. **Generic industrial thermostability claims.** A heat-stable enzyme from a thermophile is an application of the trait, not necessarily a causal node for organismal growth optimum.

## 8. DOI-first bibliography

- Lipscomb GL, Hahn EM, Crowley AT, Adams MWW. **Reverse gyrase is essential for microbial growth at 95 °C.** *Extremophiles*. Published March 2017. DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z). (lipscomb2017reversegyraseis pages 1-2)
- Atomi H, Matsumi R, Imanaka T. **Reverse gyrase is not a prerequisite for hyperthermophilic life.** *Journal of Bacteriology*. Published July 2004. DOI: [10.1128/JB.186.14.4829-4833.2004](https://doi.org/10.1128/JB.186.14.4829-4833.2004). (atomi2004reversegyraseis pages 3-5)
- Kampmann M, Stock D. **Reverse gyrase has heat-protective DNA chaperone activity independent of supercoiling.** *Nucleic Acids Research*. Published July 2004. DOI: [10.1093/nar/gkh683](https://doi.org/10.1093/nar/gkh683). (kampmann2004reversegyrasehas pages 1-2)
- Villain P et al. **The hyperthermophilic archaeon Thermococcus kodakarensis is resistant to pervasive negative supercoiling activity of DNA gyrase.** *Nucleic Acids Research*. Published November 2021. DOI: [10.1093/nar/gkab869](https://doi.org/10.1093/nar/gkab869). (villain2021thehyperthermophilicarchaeon pages 11-12)
- Esteves AM et al. **Mannosylglycerate and di-myo-inositol phosphate have interchangeable roles during adaptation of Pyrococcus furiosus to heat stress.** *Applied and Environmental Microbiology*. Published July 2014. DOI: [10.1128/AEM.00559-14](https://doi.org/10.1128/AEM.00559-14). (esteves2014mannosylglycerateanddi pages 20-28, esteves2014mannosylglycerateanddi pages 9-12)
- Cario A et al. **Molecular chaperone accumulation as a function of stress evidences adaptation to high hydrostatic pressure in Thermococcus barophilus.** *Scientific Reports*. Published July 2016. DOI: [10.1038/srep29483](https://doi.org/10.1038/srep29483). (cario2016molecularchaperoneaccumulation pages 3-4)
- Blum LN et al. **Distribution and abundance of tetraether lipid cyclization genes in terrestrial hot springs reflect pH.** *Environmental Microbiology*. Published April 2023. DOI: [10.1111/1462-2920.16375](https://doi.org/10.1111/1462-2920.16375). (blum2023distributionandabundance pages 6-7, blum2023distributionandabundance pages 2-2)
- Chiu BK et al. **Membrane lipid and expression responses of Saccharolobus islandicus REY15A to acid and cold stress.** *Frontiers in Microbiology*. Published August 2023. DOI: [10.3389/fmicb.2023.1219779](https://doi.org/10.3389/fmicb.2023.1219779). (chiu2023membranelipidand pages 2-3)
- Rastädter K et al. **The cell membrane of Sulfolobus spp.—homeoviscous adaption and biotechnological applications.** *International Journal of Molecular Sciences*. Published May 2020. DOI: [10.3390/ijms21113935](https://doi.org/10.3390/ijms21113935). (rastadter2020thecellmembrane pages 5-7)
- Murata M et al. **Molecular strategy for survival at a critical high temperature in Escherichia coli.** *PLoS ONE*. Published June 2011. DOI: [10.1371/journal.pone.0020063](https://doi.org/10.1371/journal.pone.0020063). (murata2011molecularstrategyfor pages 1-2)
- Ren H et al. **Coupling thermotolerance and high production of recombinant protein by CYR1N1546K mutation via cAMP signaling cascades.** *Communications Biology*. Published May 2024. DOI: [10.1038/s42003-024-06341-z](https://doi.org/10.1038/s42003-024-06341-z). (ren2024couplingthermotoleranceand pages 1-2)

## Curation conclusion

The best-supported addition to the existing TraitMech graph is a **hyperthermophile-specific reverse-gyrase branch** connecting DNA heat protection to high-temperature growth, supported by quantitative deletion phenotypes. A second, lower-confidence membrane branch should connect GrsA/GrsB to GDGT cyclization and membrane packing, while explicitly marking the final connection to **METPO:1000447** as indirect. DIP/MG should be represented as a **redundant heat-acclimation module**, not as individually necessary determinants. Chaperone/proteostasis edges are biologically compelling but should remain broad or uncertain until direct perturbation data from naturally thermophilic organisms tie them to changes in the measured optimal-growth temperature.

References

1. (pandey2026extremethermalenvironments pages 5-6): Anita Pandey and Kusum Dhakar. Extreme thermal environments: reservoirs of industrially important thermozymes. Frontiers in Microbiology, Jan 2026. URL: https://doi.org/10.3389/fmicb.2025.1739143, doi:10.3389/fmicb.2025.1739143. This article has 6 citations and is from a peer-reviewed journal.

2. (murata2011molecularstrategyfor pages 1-2): Masayuki Murata, Hiroko Fujimoto, Kaori Nishimura, Kannikar Charoensuk, Hiroshi Nagamitsu, Satish Raina, Tomoyuki Kosaka, Taku Oshima, Naotake Ogasawara, and Mamoru Yamada. Molecular strategy for survival at a critical high temperature in eschierichia coli. PLoS ONE, 6:e20063, Jun 2011. URL: https://doi.org/10.1371/journal.pone.0020063, doi:10.1371/journal.pone.0020063. This article has 119 citations and is from a peer-reviewed journal.

3. (lipscomb2017reversegyraseis pages 2-4): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

4. (lipscomb2017reversegyraseis pages 4-5): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

5. (atomi2004reversegyraseis pages 3-5): Haruyuki Atomi, Rie Matsumi, and Tadayuki Imanaka. Reverse gyrase is not a prerequisite for hyperthermophilic life. Journal of Bacteriology, 186:4829-4833, Jul 2004. URL: https://doi.org/10.1128/jb.186.14.4829-4833.2004, doi:10.1128/jb.186.14.4829-4833.2004. This article has 165 citations and is from a peer-reviewed journal.

6. (kampmann2004reversegyrasehas pages 1-2): M. Kampmann and D. Stock. Reverse gyrase has heat-protective dna chaperone activity independent of supercoiling. Nucleic acids research, 32 12:3537-45, Jul 2004. URL: https://doi.org/10.1093/nar/gkh683, doi:10.1093/nar/gkh683. This article has 108 citations and is from a highest quality peer-reviewed journal.

7. (villain2021thehyperthermophilicarchaeon pages 11-12): Paul Villain, Violette da Cunha, Etienne Villain, Patrick Forterre, Jacques Oberto, Ryan Catchpole, and Tamara Basta. The hyperthermophilic archaeon thermococcus kodakarensis is resistant to pervasive negative supercoiling activity of dna gyrase. Nucleic Acids Research, 49:12332-12347, Nov 2021. URL: https://doi.org/10.1093/nar/gkab869, doi:10.1093/nar/gkab869. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (esteves2014mannosylglycerateanddi pages 9-12): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

9. (esteves2014mannosylglycerateanddi pages 16-20): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

10. (cario2016molecularchaperoneaccumulation pages 3-4): Anaïs Cario, Mohamed Jebbar, Axel Thiel, Nelly Kervarec, and Phil M. Oger. Molecular chaperone accumulation as a function of stress evidences adaptation to high hydrostatic pressure in the piezophilic archaeon thermococcus barophilus. Scientific Reports, Jul 2016. URL: https://doi.org/10.1038/srep29483, doi:10.1038/srep29483. This article has 42 citations and is from a peer-reviewed journal.

11. (chiu2023membranelipidand pages 2-3): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

12. (rastadter2020thecellmembrane pages 5-7): Kerstin Rastädter, David J. Wurm, Oliver Spadiut, and Julian Quehenberger. The cell membrane of sulfolobus spp.—homeoviscous adaption and biotechnological applications. International Journal of Molecular Sciences, 21:3935, May 2020. URL: https://doi.org/10.3390/ijms21113935, doi:10.3390/ijms21113935. This article has 49 citations.

13. (blum2023distributionandabundance pages 2-2): Laura N. Blum, Daniel R. Colman, Emiley A. Eloe‐Fadrosh, Matthew Kellom, Eric S. Boyd, Olga Zhaxybayeva, and William D. Leavitt. Distribution and abundance of tetraether lipid cyclization genes in terrestrial hot springs reflect ph. Environmental microbiology, 25:1644-1658, Apr 2023. URL: https://doi.org/10.1111/1462-2920.16375, doi:10.1111/1462-2920.16375. This article has 9 citations and is from a domain leading peer-reviewed journal.

14. (blum2023distributionandabundance pages 6-7): Laura N. Blum, Daniel R. Colman, Emiley A. Eloe‐Fadrosh, Matthew Kellom, Eric S. Boyd, Olga Zhaxybayeva, and William D. Leavitt. Distribution and abundance of tetraether lipid cyclization genes in terrestrial hot springs reflect ph. Environmental microbiology, 25:1644-1658, Apr 2023. URL: https://doi.org/10.1111/1462-2920.16375, doi:10.1111/1462-2920.16375. This article has 9 citations and is from a domain leading peer-reviewed journal.

15. (ren2024couplingthermotoleranceand pages 1-2): Haiyan Ren, Qing Lan, Shihao Zhou, Yilin Lyu, Yao Yu, Jungang Zhou, Wenjuan Mo, and Hong Lu. Coupling thermotolerance and high production of recombinant protein by cyr1n1546k mutation via camp signaling cascades. Communications Biology, May 2024. URL: https://doi.org/10.1038/s42003-024-06341-z, doi:10.1038/s42003-024-06341-z. This article has 8 citations and is from a peer-reviewed journal.

16. (lipscomb2017reversegyraseis pages 1-2): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

17. (esteves2014mannosylglycerateanddi pages 20-28): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.