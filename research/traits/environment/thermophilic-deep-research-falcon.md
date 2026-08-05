---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:30:41.665074'
end_time: '2026-08-04T04:40:52.754577'
duration_seconds: 611.09
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: thermophilic
  trait_identifier: METPO:1000616
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: thermophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at elevated temperatures,\
    \ typically \u226545 \xB0C."
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Supports thermophilic growth as adaptation to elevated temperature.)
    | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic
    bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)'
  causal_graph_summary: 'thermophilic_heat_adaptation: 14 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** thermophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000616
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at elevated temperatures, typically ≥45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Supports thermophilic growth as adaptation to elevated temperature.) | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)
- **Existing causal graph summary:** thermophilic_heat_adaptation: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **thermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermophilic.yaml`.

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
- **Trait label:** thermophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000616
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at elevated temperatures, typically ≥45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Supports thermophilic growth as adaptation to elevated temperature.) | PMID:24058645: Geobacillus stearothermophilus is a gram-positive, thermophilic bacterium (Organism example: Geobacillus stearothermophilus is described as thermophilic.)
- **Existing causal graph summary:** thermophilic_heat_adaptation: 14 nodes, 10 edges

## Research Objective

Research the microbial trait **thermophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermophilic.yaml`.

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


# Curation report: thermophilic microbial trait

## 1. Scope summary

**Trait:** `METPO:1000616` (“thermophilic”); category **ENVIRONMENT**; parent `METPO:1000613`.

For TraitMech, this trait should denote a **reproducible growth preference or optimum at elevated temperature, operationally about ≥45 °C**, rather than mere survival after heating. Hyperthermophiles are conventionally distinguished by optimal growth at **≥80 °C**; some microorganisms tolerate temperatures above 100 °C. The temperature threshold is operational rather than a universal mechanistic boundary. Thermophily should therefore be asserted from growth-rate/yield curves across temperatures, ideally with biological replication, not solely from isolation in a hot habitat or thermostability of one enzyme. (takemata2024howdothermophiles pages 1-2, lipscomb2017reversegyraseis pages 1-2)

### Boundary cases

- **Thermophilic versus hyperthermophilic:** hyperthermophily is the ≥80 °C-optimum subset. Reverse gyrase is especially characteristic of organisms with optima above approximately 65 °C and is experimentally essential at 95–100 °C in *Pyrococcus furiosus*, but this does not make it a universal cause of moderate thermophily. (takemata2024howdothermophiles pages 1-2, lipscomb2017reversegyraseis pages 2-4)
- **Thermophily versus thermotolerance:** survival, viability, or enzyme activity after a heat pulse is not equivalent to growth being favored at high temperature.
- **Stable adaptation versus heat-shock response:** constitutive membrane/protein/genome features may define the trait, whereas transient chaperone induction is an acute response that may occur in mesophiles too.
- **Thermophily versus thermoacidophily:** low proton permeability of bipolar tetraether membranes is strongly documented in thermoacidophilic *Sulfolobus* systems, where heat and pH selection are confounded. These edges should be taxon- and environment-qualified. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2)
- **Habitat temperature versus phenotype:** a hot-spring isolate is not necessarily thermophilic unless cultivated growth supports the designation.

## 2. Current mechanistic model

Elevated temperature destabilizes several cellular systems simultaneously: it increases membrane permeability and fluidity, melts DNA duplex regions, accelerates chemical DNA damage, perturbs chromosome motion, and promotes protein unfolding/aggregation. Thermophilic growth is therefore a **systems phenotype**, not a single pathway. The best-supported modules are:

1. **Membrane homeoviscous adaptation:** remodeling bacterial fatty-acid chain length, branching, and unsaturation, or archaeal ether/tetraether composition and cyclization, preserves membrane packing and permeability.
2. **Genome protection:** reverse gyrase, nucleoid-associated proteins (NAPs), archaeal histones, polyamines, DNA repair, and chromosome-organization proteins limit heat-induced genome dysfunction.
3. **Proteostasis:** intrinsically stable proteins, oligomeric interfaces, chaperones, and proteases preserve the folded proteome.
4. **Chemical thermoprotection:** compatible solutes such as mannosylglycerate, di-myo-inositol phosphate, and cyclic 2,3-diphosphoglycerate stabilize macromolecules.

The evidence-ranked overview is:

| module | strongest proposed triple | evidence class | taxon/assay scope | curation decision |
|---|---|---|---|---|
| Reverse gyrase | reverse gyrase **enables** growth at >90–95 °C | **Direct perturbation**: deletion of *rgy* in *Pyrococcus furiosus* abolishes growth at 95–100 °C; review consensus links reverse gyrase to positive supercoiling/genome integrity (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2, takemata2024howdothermophiles pages 2-3, takemata2024howdothermophiles pages 1-2) | Hyperthermophilic archaea; strongest evidence in *P. furiosus* growth assays | **High priority curate**; mark as strongest direct edge, but note best supported for hyperthermophily rather than all thermophily |
| Archaeal tetraether cyclization | increased tetraether cyclization **decreases** membrane proton permeability / **stabilizes** membrane packing at high temperature | **Review + quantitative biophysical evidence**: higher cyclopentane ring number with higher growth temperature; very low, temperature-insensitive proton permeability in tetraether liposomes (chong2024archaeamembranesin pages 1-2, chong2024archaeamembranesin pages 2-3, siliakus2017adaptationsofarchaeal pages 1-3) | Thermoacidophilic archaea, especially *Sulfolobus* lipid systems and liposome assays | **Medium-high curate** as archaeal/thermoacidophile-specific mechanism; not universal across all thermophiles |
| Bacterial fatty-acid remodeling | bacterial membrane fatty-acid remodeling **maintains** membrane fluidity under temperature change | **Original experimental + review**: homeoviscous adaptation; anteiso and unsaturated FAs increase at lower temperature; thermophile/mesophile comparisons support temperature-linked remodeling (hellequin2023membranelipidadaptation pages 1-2, hellequin2023membranelipidadaptation pages 13-14, pollo2015insightsintothermoadaptation pages 7-11, siliakus2017adaptationsofarchaeal pages 3-5) | Bacteria; strongest direct data from soil Bacteroidetes and broader comparative bacterial literature | **Medium curate** as bacterial, taxon-specific homeoviscous module; avoid overgeneralizing exact lipid species to all thermophiles |
| NAPs / archaeal histones | NAPs or archaeal histones **increase** DNA melting temperature / **protect** genomes from heat denaturation | **Mostly in vitro + correlative review evidence**: NAPs increase DNA melting temperature by up to 40 °C; abundance correlates with growth temperature (takemata2024howdothermophiles pages 3-4, takemata2024howdothermophiles pages 2-3, takemata2024howdothermophiles pages 1-2, pollo2015insightsintothermoadaptation pages 11-14) | Mainly thermophilic archaea; mixed biochemical and comparative evidence | **Medium curate with caution**; acceptable as protective genome-stability edge, but mechanistic universality remains uncertain |
| Compatible solute: mannosylglycerate | mannosylglycerate **stabilizes** proteins against thermal stress | **Direct in vitro biochemical evidence**: improved residual activity of multiple enzymes after heat stress; often better thermoprotectant than trehalose (ramos1997stabilizationofenzymes pages 1-2, ramos1997stabilizationofenzymes pages 3-5) | In vitro enzyme assays using thermophilic, hyperthermophilic, and mesophilic enzymes; solute occurs in some thermophiles | **Medium curate** as compatible-solute thermoprotection, explicitly labeled in-vitro / not direct growth-phenotype proof |
| Chaperone / proteostasis | constitutive chaperone and protease systems **support** protein folding at high temperature | **Review / proteomic inference**: high constitutive expression and increased abundance at supraoptimal temperatures, but limited perturbation evidence in retrieved set (pollo2015insightsintothermoadaptation pages 14-17) | Thermotogae-focused and comparative thermophile literature | **Provisional**; useful candidate node set, but defer strong causal edges until direct knockout/fitness evidence is assembled |
| GGR paralogs | geranylgeranyl reductase paralogs **regulate** archaeal thermophilic membrane adaptation | **Speculative/review-level**: paralog multiplicity correlated with saturation of polyterpenes, but exact functions unresolved (rao2024unravelingthemultiplicity pages 1-2, rao2024unravelingthemultiplicity pages 19-20) | Archaea; genomic, structural, and bioinformatic inference | **Do not curate yet** as mechanistic edge for thermophily pending direct functional validation |


*Table: This table prioritizes candidate mechanistic modules for a thermophilic TraitMech graph by evidence strength and scope. It helps distinguish broadly curatable edges from taxon-specific, provisional, or not-yet-curatable claims.*

## 3. Candidate nodes grouped by type

Identifiers below are included only where confidence is high. Specialized molecules and taxon-specific proteins should remain label-only until checked against the target ontology release and organism-specific UniProt records.

### Trait and environment

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| thermophilic | `METPO:1000616` | Target phenotype; quote verbatim in YAML. |
| elevated environmental temperature | `ENVO:01000207` | Confirm label/version locally; represent measured °C as assay metadata. |
| supraoptimal heat stress | Label only | Distinguish stress above the organism’s optimum from its preferred growth temperature. |
| thermoacidic environment | Label only | Needed for *Sulfolobus* membrane evidence; do not merge with thermophily. |
| high-temperature growth | Label only | Assay outcome connecting maintenance modules to the trait. |

### Cellular structures and processes

| Candidate node | Suggested grounding | Role |
|---|---|---|
| plasma membrane | `GO:0005886` | Heat-sensitive permeability/fluidity barrier. |
| homeoviscous adaptation | Label only | Lipid remodeling that preserves membrane functional state. |
| protein folding | `GO:0006457` | Chaperone-supported proteostasis. |
| DNA repair | `GO:0006281` | Counteracts heat-associated chemical damage and breaks. |
| DNA topological change | `GO:0006265` | Parent process for reverse-gyrase action. |
| positive DNA supercoiling | Label only | Direct biochemical product of reverse gyrase; physiological necessity is context-dependent. |
| genome integrity | Label only | Intermediate phenotype rather than a molecule. |
| membrane proton permeability | Label only | Particularly relevant to thermoacidophilic archaea. |
| protein thermostability | Label only | Intermediate phenotype; do not equate automatically with organismal thermophily. |

### Genes, proteins, enzymes, and complexes

- **Reverse gyrase / `rgy` / TopR1–TopR2:** ATP-dependent helicase–type-IA-topoisomerase fusion introducing positive supercoils. Use taxon-specific UniProt identifiers only after sequence verification.
- **Archaeal histones and other NAPs:** HtkA/HtkB, Alba-family proteins, bacterial HU-like proteins; grounding must be organism-specific.
- **SMC-family proteins and coalescin (ClsN):** chromosome architecture candidates. Evidence for a direct thermophily edge remains incomplete.
- **Chaperonins and heat-shock proteins:** GroEL/GroES, DnaK/DnaJ/GrpE, archaeal thermosome, small HSPs, trigger factor; represent separately by taxon rather than as one universal node.
- **Proteases:** Lon and related quality-control proteases; candidate proteostasis nodes needing direct temperature-fitness evidence.
- **Archaeal lipid enzymes:** tetraether lipid synthase (Tes), GDGT ring synthases GrsA/GrsB, geranylgeranyl reductase (GGR), GGGP synthase, and DGGGP synthase. The 2024 review states that GrsA/GrsB introduce GDGT rings, but GGR-paralog functions remain unresolved. (rao2024unravelingthemultiplicity pages 1-2, rao2024unravelingthemultiplicity pages 19-20)
- **Compatible-solute enzymes:** 2-phosphoglycerate kinase and cyclic diphosphoglycerate synthetase for cDPG biosynthesis; pathway-specific identifiers should be verified before use. (rose2021productionofthe pages 1-2)

### Chemicals and membrane components

| Node | Suggested grounding/status | Note |
|---|---|---|
| ATP | `CHEBI:15422` | Energy donor for reverse gyrase and many chaperones. |
| trehalose | `CHEBI:27082` | Compatible solute; not thermophile-specific. |
| spermidine | `CHEBI:16610` | Polyamine implicated in nucleic-acid stabilization. |
| putrescine | `CHEBI:17148` | Polyamine; broad cellular functions. |
| mannosylglycerate | Label only pending ChEBI verification | Strong in-vitro thermoprotection evidence, but organismal causation is weaker. |
| di-myo-inositol phosphate | Label only | Heat-responsive solute in multiple thermophiles; pathway redundancy is important. |
| cyclic 2,3-diphosphoglycerate (cDPG) | Label only | Hyperthermophilic methanogen extremolyte and engineering product. |
| archaeal ether lipids | Label only | Ether linkages are chemically and thermally more stable than ester linkages. (chong2024archaeamembranesin pages 1-2) |
| GDGT / bipolar tetraether lipids | Label only | Membrane-spanning lipids forming monolayer-like structures. |
| cyclized GDGT | Label only | Cyclopentane rings increase packing/stability; strongly archaeal-specific. (rao2024unravelingthemultiplicity pages 1-2) |
| saturated, unsaturated, iso-, and anteiso-fatty acids | Label only or verified ChEBI species | Exact direction depends on taxon and temperature range. |
| diabolic fatty acids | Label only | Thermotogae-associated candidate; comparative rather than perturbational evidence. |

### Taxa useful as evidence contexts

- *Pyrococcus furiosus*: decisive reverse-gyrase deletion phenotype.
- *Thermococcus kodakarensis*: reverse-gyrase and compatible-solute perturbation evidence, with redundancy.
- *Sulfolobus acidocaldarius*, *S. islandicus*: tetraether/cyclization and genome-organization models.
- *Thermotoga maritima*: membrane, compatible-solute, chaperone, and thermostable-enzyme model.
- *Thermus thermophilus*: genetically tractable thermophilic cell factory.
- *Geobacillus stearothermophilus*: established thermophilic bacterial example from the supplied evidence.

## 4. Candidate causal edges

**Evidence classes:** **Direct** = perturbation or controlled biochemical/biophysical experiment; **Correlative** = measured covariation; **Review-supported** = synthesis of primary studies; **Inferred** = plausible graph connection not directly demonstrated.

| # | Subject–predicate–object triple | Evidence and supporting snippet | Scope, strength, and curation note |
|---:|---|---|---|
| 1 | elevated temperature → **increases** → DNA melting/chemical damage/chromosome thermal motion | “High temperatures… denaturing the DNA double helix, causing chemical damage to DNA, and increasing the random thermal motion of chromosomes.” DOI: [10.1264/jsme2.ME23087](https://doi.org/10.1264/jsme2.ME23087), published 6 June 2024. (takemata2024howdothermophiles pages 1-2) | **Review-supported.** Curate as an environmental challenge, not as a thermophile-specific adaptation. |
| 2 | elevated temperature → **increases** → membrane permeability | The Thermotogae review states that temperature-driven permeability increases can compromise function and cause death. DOI: [10.1139/cjm-2015-0073](https://doi.org/10.1139/cjm-2015-0073), September 2015. (pollo2015insightsintothermoadaptation pages 7-11) | **Review-supported.** Direction depends on starting membrane composition; use as a challenge edge. |
| 3 | membrane lipid remodeling → **maintains** → membrane fluidity/permeability | “Microorganisms… adjust their membrane lipid composition… maintaining the appropriate fluidity,” termed homeoviscous adaptation. DOI: [10.3389/fmicb.2023.1032032](https://doi.org/10.3389/fmicb.2023.1032032), 6 March 2023. (hellequin2023membranelipidadaptation pages 1-2) | **Original study plus established framework.** Strong module-level edge, but exact lipid changes are taxon-specific. |
| 4 | decreasing growth temperature → **increases** → anteiso fatty-acid proportion | Three Bacteroidetes strains showed “an increase… [in] total anteiso 3-OH FAs… with decreasing growth temperature”; anteiso/iso-or-normal ratios changed significantly. (hellequin2023membranelipidadaptation pages 13-14, hellequin2023membranelipidadaptation pages 1-2) | **Direct controlled cultivation, but mesophilic soil Bacteroidetes.** Useful for homeoviscous directionality, not direct evidence of thermophilic causation. Consequently, increasing temperature can be represented as favoring relatively more iso/normal species only within this assay context. |
| 5 | archaeal tetraether cyclization → **increases** → membrane packing/stability | The 2024 archaeal-lipid review states: “Cyclized GDGTs increase the membrane packing and stability”; GrsA/GrsB introduce rings at defined core-lipid positions. DOI: [10.1007/s00792-023-01330-2](https://doi.org/10.1007/s00792-023-01330-2), 27 January 2024. (rao2024unravelingthemultiplicity pages 1-2) | **Review-supported biochemical mechanism.** Curate only in archaeal lipid modules. |
| 6 | increasing growth temperature → **increases** → GDGT cyclopentane-ring number | In *S. acidocaldarius*, average rings per tetraether rose **3.4→4.8** as growth temperature rose **65→82 °C**. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019), 4 January 2024. (chong2024archaeamembranesin pages 1-2) | **Correlative controlled-growth observation**, confounded by growth rate and pH in related datasets. Curate as taxon-specific regulation, not universal law. |
| 7 | bipolar tetraether membrane → **decreases** → passive proton permeability | *S. acidocaldarius* PLFE liposomes had proton permeability **0.3–0.5×10⁻⁸ cm s⁻¹ at 65–82 °C**, versus **3–9×10⁻⁸ cm s⁻¹** for egg-yolk phosphatidylcholine liposomes. (chong2024archaeamembranesin pages 2-3) | **Direct liposome biophysics.** Strong molecular edge; it does not itself prove enhanced cellular growth. |
| 8 | low membrane proton permeability → **supports** → intracellular pH homeostasis at elevated temperature | The 2024 review links low permeability to maintenance of near-neutral cytosolic pH and protein activity under acidic, hot conditions. Thermoacidophile intracellular pH is generally **5.4–6.5**, or about **4.6** in *Picrophilus*. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2) | **Review-level physiological inference.** Curate only in a thermoacidophile subgraph. |
| 9 | reverse gyrase + ATP → **introduces** → positive DNA supercoils | Reverse gyrase “uses energy from ATP to introduce positive DNA supercoiling.” DOI: [10.1264/jsme2.ME23087](https://doi.org/10.1264/jsme2.ME23087), 2024. (takemata2024howdothermophiles pages 2-3) | **Established biochemical function.** High-confidence molecular edge; ATP consumption may be modeled separately. |
| 10 | reverse gyrase → **promotes** → growth above 90 °C | In *P. furiosus*, Δ*rgy* grew comparably at **75–85 °C**, had about **half the control growth rate at 90 °C**, and showed no significant growth at **95 or 100 °C**. At 90 °C, maximal OD₆₈₀ was **0.093±0.003 versus 0.214±0.001**. DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z), accepted 10 March 2017. (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2) | **Direct genetic perturbation; strongest phenotype edge.** Curate as *P. furiosus*/extreme-temperature-specific. It supports hyperthermophily, not every ≥45 °C thermophile. |
| 11 | reverse gyrase → **protects/repairs** → heat-damaged DNA | In vitro reverse gyrase promotes DNA renaturation, protects nicked DNA from heat-induced breakage, and can destabilize Holliday junctions; depletion of *S. islandicus* TopR1 accelerates alkylation-induced DNA degradation. (takemata2024howdothermophiles pages 2-3) | **Mixed direct biochemical and in-vivo damage evidence.** Use separate edges for renaturation, nick protection, and repair; avoid collapsing them into an unqualified universal function. |
| 12 | positive DNA supercoiling → **reduces** → heat-induced DNA melting | This is the prevailing hypothesis, but some thermophile plasmids are negatively supercoiled, and heterologous strong negative supercoiling in *T. kodakarensis* did not produce a clear growth defect. (takemata2024howdothermophiles pages 2-3, lipscomb2017reversegyraseis pages 1-2) | **Uncertain/inferred.** Do not curate as the sole explanation for the Δ*rgy* phenotype. Reverse gyrase may act through repair or DNA-twist control. |
| 13 | NAP/histone binding → **increases** → DNA melting temperature | In-vitro studies found that several prokaryotic NAPs increase DNA melting temperature by **up to 40 °C**. (takemata2024howdothermophiles pages 3-4) | **Direct in vitro, protein- and taxon-dependent.** Curate with specific NAP/taxon where the primary study is available. |
| 14 | increased archaeal NAP abundance → **supports** → thermal genome protection | NAPs range from **<0.03% to >5% of total protein**, and overall abundance correlates with archaeal growth temperature; histone abundance similarly correlates with temperature. (takemata2024howdothermophiles pages 2-3) | **Correlative.** Suitable as a provisional edge, not proof that NAP abundance causes thermophilic growth. |
| 15 | thermophile-specific polyamines → **stabilize** → DNA/ribosomal complexes | Thermotogae literature reports putrescine, spermidine, spermine, caldopentamine, and caldohexamine as nucleic-acid stabilizers, with longer polyamines increasing with temperature in some *Thermotoga* species. (pollo2015insightsintothermoadaptation pages 11-14, pollo2015insightsintothermoadaptation pages 14-17) | **Biochemical/comparative evidence.** Exact solute and organism must be represented; do not assert every thermophile uses polyamines identically. |
| 16 | mannosylglycerate → **increases** → enzyme residual activity after heat stress | At 100 °C for 15 min, *P. furiosus* ADH retained **75%** activity with mannosylglycerate versus **53%** with trehalose; at 90 °C, *T. maritima* GDH retained **40%** with mannosylglycerate while activity without solute or with trehalose/KCl was negligible. DOI: [10.1128/AEM.63.10.4020-4025.1997](https://doi.org/10.1128/AEM.63.10.4020-4025.1997), October 1997. (ramos1997stabilizationofenzymes pages 3-5, ramos1997stabilizationofenzymes pages 1-2) | **Direct in-vitro thermoprotection.** Curate as protein stabilization, not direct organismal growth causation. One *P. furiosus* GDH showed no benefit, demonstrating protein specificity. |
| 17 | heat stress → **increases** → selected compatible-solute pools | In *P. furiosus*, total solute increased with temperature or salinity; mannosylglycerate mainly tracked salinity, whereas di-myo-inositol phosphate increased under temperature stress. (ramos1997stabilizationofenzymes pages 1-2) | **Measured physiological response.** Do not use mannosylglycerate as a universal heat-specific solute; its induction can be osmotic. |
| 18 | compatible-solute pathway redundancy → **buffers** → loss of one thermoprotectant | Deleting di-myo-inositol-phosphate synthesis in *T. kodakarensis* did not impair growth because aspartate accumulated instead. (pollo2015insightsintothermoadaptation pages 14-17) | **Direct perturbation with compensatory response.** Important warning against simple “gene required for thermophily” edges. |
| 19 | chaperones/trigger factor → **support** → protein folding at high temperature | *T. maritima* chaperones are constitutively abundant, and chaperone abundance increases at supraoptimal temperatures. (pollo2015insightsintothermoadaptation pages 14-17) | **Proteomic/review evidence.** Retain as provisional until direct knockout or rescue data are attached to each protein. |
| 20 | stronger oligomer interfaces/disulfides → **increase** → protein melting temperature | Engineering *Chloroflexus aurantiacus* malate dehydrogenase interfaces increased melting temperature by **15 °C** with a disulfide bridge and approximately **24 °C** with selected interface substitutions. (pollo2015insightsintothermoadaptation pages 20-23) | **Direct protein engineering.** Demonstrates a mechanism of thermostability, but engineered single-enzyme stability is not sufficient evidence for organismal thermophily. |
| 21 | 2-phosphoglycerate kinase + cDPG synthetase → **produces** → cDPG | Introducing the two-enzyme pathway into *T. thermophilus* produced cDPG up to **650 µM**, confirmed by mass spectrometry. DOI: [10.3389/fctls.2021.803416](https://doi.org/10.3389/fctls.2021.803416), 20 December 2021. (rose2021productionofthe pages 1-2) | **Direct synthetic-biology implementation.** Curate as a pathway/application edge, not as evidence that cDPG naturally causes *T. thermophilus* thermophily. |
| 22 | thermophilic growth → **enables** → high-temperature whole-cell biomanufacturing | The *T. thermophilus* platform supports high-temperature pathway expression; reported advantages include lower contamination risk, higher mass transfer, volatile-product recovery, and compatibility with thermophilic enzymes. (rose2021productionofthe pages 1-2) | **Demonstrated platform plus application rationale.** Keep outside the core adaptation graph unless applications are in scope. |

## 5. Recent developments and expert assessment (2023–2024)

### Genome organization

Takemata’s 2024 synthesis shifts the field away from the simplistic equation “reverse gyrase = positive supercoiling = thermophily.” Reverse gyrase is clearly important for high-temperature fitness, but thermophile DNA topology ranges from positive to negative; its DNA-renaturation, nick-protection, repair, and recombination activities may be equally important. NAP abundance, archaeal histone arrays, SMC-related architecture, and polyamines are now viewed as interacting genome-protection layers. However, the author explicitly notes that the mechanisms connecting three-dimensional genome organization to high-temperature survival remain incompletely resolved. (takemata2024howdothermophiles pages 2-3, takemata2024howdothermophiles pages 1-2)

### Membrane mechanisms

The 2023 Bacteroidetes cultivation study provides microbial-level validation that 3-hydroxy-fatty-acid distributions respond to temperature, strengthening lipid-proxy interpretation while also showing substantial strain specificity. Its strongest common signal was increased anteiso relative to iso/normal 3-OH fatty acids at lower temperature; it is evidence for homeoviscous remodeling, not direct evidence that one lipid causes thermophily. (hellequin2023membranelipidadaptation pages 13-14, hellequin2023membranelipidadaptation pages 1-2)

The 2024 archaeal-membrane review supplies quantitative biophysical support for bipolar tetraether membranes as low-permeability barriers. In *S. acidocaldarius*-derived liposomes, proton permeability is roughly an order of magnitude below phosphatidylcholine controls at 65–82 °C and changes very little over 25–82 °C. This is compelling for thermoacidophile energetics, although most evidence is from isolated lipids/liposomes rather than lipid-enzyme knockouts. (chong2024archaeamembranesin pages 2-3)

Rao and Driessen’s 2024 review identifies recently elucidated enzymes such as tetraether lipid synthase and GDGT ring synthases, making the membrane module increasingly gene-addressable. Conversely, the authors stress that GGR paralog functions and substrates remain uncertain and call for genetic studies; those paralogs should not yet receive thermophily-causal edges. (rao2024unravelingthemultiplicity pages 1-2, rao2024unravelingthemultiplicity pages 19-20)

## 6. Applications and recent quantitative data

- **Thermophilic cell factories:** engineered *T. thermophilus* produced cDPG to **650 µM**. Natural cDPG concentrations reported for hyperthermophilic methanogens are **0.3–1.1 M**, illustrating both its physiological abundance and the remaining engineering yield gap. (rose2021productionofthe pages 1-2)
- **Extremolyte markets and stabilization:** the 2021 report notes commercial ectoine/hydroxyectoine production around **5 tonnes/year** and proposes cDPG for cosmetics and healthcare. These are application statistics, not thermophily-mechanism evidence. (rose2021productionofthe pages 1-2)
- **Biocatalyst stabilization:** mannosylglycerate preserved 40% activity of *T. maritima* GDH after 15 min at 90 °C when controls were negligible, and preserved 75% of *P. furiosus* ADH activity at 100 °C. (ramos1997stabilizationofenzymes pages 3-5)
- **Paleotemperature reconstruction:** temperature-sensitive bacterial 3-OH fatty-acid and archaeal GDGT distributions are used as environmental proxies, but 2023 findings emphasize strain, pH, growth-rate, and community-composition confounding. (hellequin2023membranelipidadaptation pages 13-14, hellequin2023membranelipidadaptation pages 1-2)
- **Robust high-temperature fermentation:** thermophilic hosts can reduce contamination risk and improve substrate solubility/mass transfer, although process-specific technoeconomic validation is still required. (rose2021productionofthe pages 1-2)

## 7. Recommended TraitMech graph architecture

Rather than one universal linear graph, use a conserved challenge layer plus taxon-specific adaptation branches:

1. `elevated temperature` → increases → `membrane permeability / DNA damage / protein unfolding`
2. **Bacterial branch:** `fatty-acid remodeling` → maintains → `membrane fluidity` → supports → `high-temperature growth`
3. **Archaeal branch:** `Tes/Grs-dependent tetraether architecture` → increases → `membrane packing` → decreases → `ion/proton permeability` → supports → `high-temperature growth`
4. **Hyperthermophile genome branch:** `reverse gyrase` → DNA topological change and damage mitigation → maintains → `genome integrity` → enables → `growth above 90–95 °C`
5. **Chromatin branch:** `NAPs/histones/polyamines` → stabilize/organize → `DNA` → supports → `genome integrity`
6. **Proteostasis branch:** `chaperones + proteases + intrinsically stable protein interactions` → maintain → `functional proteome`
7. **Solute branch:** `compatible-solute accumulation` → stabilizes → `proteins/nucleic acids/membranes`
8. Convergence: `membrane homeostasis + genome integrity + proteostasis` → enables → `METPO:1000616`

Only the reverse-gyrase knockout edge currently gives a particularly clean gene-to-growth causal link. Most other mechanisms support intermediate molecular phenotypes and should reach `METPO:1000616` through an explicitly **inferred** convergence edge.

## 8. Warnings: claims not yet ready for curation

1. **Do not assert reverse gyrase as necessary for all thermophiles.** The strongest necessity evidence applies above 90 °C in *P. furiosus*; moderate thermophiles may lack it. (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2)
2. **Do not assert that positive supercoiling alone explains reverse-gyrase benefit.** Some hyperthermophile DNA is relaxed or negatively supercoiled, and forced negative supercoiling did not clearly inhibit *T. kodakarensis*. (takemata2024howdothermophiles pages 2-3)
3. **Do not generalize *Sulfolobus* lipid rules to Bacteria or all Archaea.** Tetraether abundance, cyclization, headgroups, pH, growth phase, and growth rate interact. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2)
4. **Do not encode “more saturated fatty acids causes thermophily” as universal.** Chain length, iso/anteiso branching, unsaturation, pressure, and taxon all alter the optimum.
5. **Do not infer causation from genomic GC content.** The 2024 review states that high genomic GC is not obligatory for thermophiles. (takemata2024howdothermophiles pages 1-2)
6. **Do not equate thermostable enzymes with thermophilic organisms.** A protein can be thermostable in a mesophile, and protein-engineering assays do not establish a growth-temperature preference.
7. **Do not curate GGR paralogs as thermophily regulators yet.** Their exact substrates/functions and essentiality require genetic validation. (rao2024unravelingthemultiplicity pages 1-2, rao2024unravelingthemultiplicity pages 19-20)
8. **Treat chaperone edges as provisional** unless a specific knockout, depletion, complementation, or temperature-dependent fitness assay is attached.
9. **Model compatible-solute redundancy.** Loss of one solute may trigger another, masking phenotype; mannosylglycerate can respond more strongly to salinity than heat. (pollo2015insightsintothermoadaptation pages 14-17, ramos1997stabilizationofenzymes pages 1-2)
10. **Verify specialized CURIEs before YAML insertion.** Label-only nodes are safer than invented ChEBI, EC, Rhea, KEGG, or UniProt identifiers.

## 9. DOI-first bibliography

1. Takemata N. **How Do Thermophiles Organize Their Genomes?** *Microbes and Environments* 39, 2024. Published **6 June 2024**. DOI: [10.1264/jsme2.ME23087](https://doi.org/10.1264/jsme2.ME23087). (takemata2024howdothermophiles pages 1-2)
2. Chong PL-G. **Archaea membranes in response to extreme acidic environments.** *Frontiers in Biophysics* 1, 2024. Published **4 January 2024**. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019). (chong2024archaeamembranesin pages 1-2)
3. Rao A, Driessen AJM. **Unraveling the multiplicity of geranylgeranyl reductases in Archaea: potential roles in saturation of terpenoids.** *Extremophiles* 28:14, 2024. Published **27 January 2024**. DOI: [10.1007/s00792-023-01330-2](https://doi.org/10.1007/s00792-023-01330-2). (rao2024unravelingthemultiplicity pages 1-2)
4. Hellequin E et al. **Membrane lipid adaptation of soil Bacteroidetes isolates to temperature and pH.** *Frontiers in Microbiology* 14:1032032, 2023. Published **6 March 2023**. DOI: [10.3389/fmicb.2023.1032032](https://doi.org/10.3389/fmicb.2023.1032032). (hellequin2023membranelipidadaptation pages 1-2)
5. Lipscomb GL et al. **Reverse gyrase is essential for microbial growth at 95 °C.** *Extremophiles* 21:603–608, 2017. DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z). (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 1-2)
6. Siliakus MF, van der Oost J, Kengen SWM. **Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure.** *Extremophiles* 21:651–670, 2017. DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x). (siliakus2017adaptationsofarchaeal pages 1-3)
7. Pollo SMJ, Zhaxybayeva O, Nesbø CL. **Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum Thermotogae.** *Canadian Journal of Microbiology* 61:655–670, September 2015. DOI: [10.1139/cjm-2015-0073](https://doi.org/10.1139/cjm-2015-0073). (pollo2015insightsintothermoadaptation pages 11-14, pollo2015insightsintothermoadaptation pages 7-11, pollo2015insightsintothermoadaptation pages 14-17, pollo2015insightsintothermoadaptation pages 20-23)
8. De Rose SA et al. **Production of the Extremolyte Cyclic 2,3-Diphosphoglycerate Using Thermus thermophilus as a Whole-Cell Factory.** *Frontiers in Catalysis* 1:803416, 2021. Published **20 December 2021**. DOI: [10.3389/fctls.2021.803416](https://doi.org/10.3389/fctls.2021.803416). (rose2021productionofthe pages 1-2)
9. Ramos A et al. **Stabilization of Enzymes against Thermal Stress and Freeze-Drying by Mannosylglycerate.** *Applied and Environmental Microbiology* 63:4020–4025, October 1997. DOI: [10.1128/AEM.63.10.4020-4025.1997](https://doi.org/10.1128/AEM.63.10.4020-4025.1997). (ramos1997stabilizationofenzymes pages 3-5, ramos1997stabilizationofenzymes pages 1-2)

**Curation conclusion:** the most defensible expansion of the existing 14-node/10-edge summary is a modular graph centered on membrane homeostasis, genome integrity, proteostasis, and compatible-solute protection. The first high-confidence gene-to-trait edge should be the *P. furiosus* reverse-gyrase requirement at ≥95 °C, explicitly tagged as **hyperthermophile- and assay-specific**. Archaeal tetraether and compatible-solute edges are strong at the molecular level but should connect to organismal thermophily through qualified or inferred intermediate edges.

References

1. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 7 citations and is from a peer-reviewed journal.

2. (lipscomb2017reversegyraseis pages 1-2): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

3. (lipscomb2017reversegyraseis pages 2-4): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

4. (chong2024archaeamembranesin pages 2-3): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

5. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

6. (takemata2024howdothermophiles pages 2-3): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 7 citations and is from a peer-reviewed journal.

7. (siliakus2017adaptationsofarchaeal pages 1-3): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

8. (hellequin2023membranelipidadaptation pages 1-2): Eve Hellequin, Sylvie Collin, Marina Seder-Colomina, Pierre Véquaud, Christelle Anquetil, Adrienne Kish, and Arnaud Huguet. Membrane lipid adaptation of soil bacteroidetes isolates to temperature and ph. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1032032, doi:10.3389/fmicb.2023.1032032. This article has 14 citations and is from a peer-reviewed journal.

9. (hellequin2023membranelipidadaptation pages 13-14): Eve Hellequin, Sylvie Collin, Marina Seder-Colomina, Pierre Véquaud, Christelle Anquetil, Adrienne Kish, and Arnaud Huguet. Membrane lipid adaptation of soil bacteroidetes isolates to temperature and ph. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1032032, doi:10.3389/fmicb.2023.1032032. This article has 14 citations and is from a peer-reviewed journal.

10. (pollo2015insightsintothermoadaptation pages 7-11): Stephen M.J. Pollo, Olga Zhaxybayeva, and Camilla L. Nesbø. Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum <i>thermotogae</i>. Sep 2015. URL: https://doi.org/10.1139/cjm-2015-0073, doi:10.1139/cjm-2015-0073. This article has 63 citations and is from a peer-reviewed journal.

11. (siliakus2017adaptationsofarchaeal pages 3-5): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

12. (takemata2024howdothermophiles pages 3-4): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 7 citations and is from a peer-reviewed journal.

13. (pollo2015insightsintothermoadaptation pages 11-14): Stephen M.J. Pollo, Olga Zhaxybayeva, and Camilla L. Nesbø. Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum <i>thermotogae</i>. Sep 2015. URL: https://doi.org/10.1139/cjm-2015-0073, doi:10.1139/cjm-2015-0073. This article has 63 citations and is from a peer-reviewed journal.

14. (ramos1997stabilizationofenzymes pages 1-2): A. Ramos, Neil D.H. Raven, Richard J. Sharp, S. Bartolucci, Mosé Rossi, R. Cannio, J. Lebbink, J. Oost, W. M. D. Vos, and Helena Santos. Stabilization of enzymes against thermal stress and freeze-drying by mannosylglycerate. Applied and Environmental Microbiology, 63:4020-4025, Oct 1997. URL: https://doi.org/10.1128/aem.63.10.4020-4025.1997, doi:10.1128/aem.63.10.4020-4025.1997. This article has 155 citations and is from a peer-reviewed journal.

15. (ramos1997stabilizationofenzymes pages 3-5): A. Ramos, Neil D.H. Raven, Richard J. Sharp, S. Bartolucci, Mosé Rossi, R. Cannio, J. Lebbink, J. Oost, W. M. D. Vos, and Helena Santos. Stabilization of enzymes against thermal stress and freeze-drying by mannosylglycerate. Applied and Environmental Microbiology, 63:4020-4025, Oct 1997. URL: https://doi.org/10.1128/aem.63.10.4020-4025.1997, doi:10.1128/aem.63.10.4020-4025.1997. This article has 155 citations and is from a peer-reviewed journal.

16. (pollo2015insightsintothermoadaptation pages 14-17): Stephen M.J. Pollo, Olga Zhaxybayeva, and Camilla L. Nesbø. Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum <i>thermotogae</i>. Sep 2015. URL: https://doi.org/10.1139/cjm-2015-0073, doi:10.1139/cjm-2015-0073. This article has 63 citations and is from a peer-reviewed journal.

17. (rao2024unravelingthemultiplicity pages 1-2): Alka Rao and Arnold J. M. Driessen. Unraveling the multiplicity of geranylgeranyl reductases in archaea: potential roles in saturation of terpenoids. Extremophiles, Jan 2024. URL: https://doi.org/10.1007/s00792-023-01330-2, doi:10.1007/s00792-023-01330-2. This article has 3 citations and is from a peer-reviewed journal.

18. (rao2024unravelingthemultiplicity pages 19-20): Alka Rao and Arnold J. M. Driessen. Unraveling the multiplicity of geranylgeranyl reductases in archaea: potential roles in saturation of terpenoids. Extremophiles, Jan 2024. URL: https://doi.org/10.1007/s00792-023-01330-2, doi:10.1007/s00792-023-01330-2. This article has 3 citations and is from a peer-reviewed journal.

19. (rose2021productionofthe pages 1-2): Simone A. De Rose, William Finnigan, Nicholas J. Harmer, Jennifer A. Littlechild, and The HotSolute consortium. Production of the extremolyte cyclic 2,3-diphosphoglycerate using thermus thermophilus as a whole-cell factory. Frontiers in Catalysis, Dec 2021. URL: https://doi.org/10.3389/fctls.2021.803416, doi:10.3389/fctls.2021.803416. This article has 10 citations.

20. (pollo2015insightsintothermoadaptation pages 20-23): Stephen M.J. Pollo, Olga Zhaxybayeva, and Camilla L. Nesbø. Insights into thermoadaptation and the evolution of mesophily from the bacterial phylum <i>thermotogae</i>. Sep 2015. URL: https://doi.org/10.1139/cjm-2015-0073, doi:10.1139/cjm-2015-0073. This article has 63 citations and is from a peer-reviewed journal.