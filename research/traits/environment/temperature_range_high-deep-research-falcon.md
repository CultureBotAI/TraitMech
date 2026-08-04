---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T04:14:00.360282'
end_time: '2026-08-04T04:24:22.828778'
duration_seconds: 622.47
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range high
  trait_identifier: METPO:1000454
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range extends above approximately 40 \xB0C, characteristic of thermophilic\
    \ physiology."
  parent_traits: METPO:1000306
  synonyms: Thermophile, TR_>40
  evidence_summary: "DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of\
    \ high temperature (Thermophile-adaptation review supports growth ranges extending\
    \ above 40 \xB0C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001:\
    \ resistant to irreversible inactivation at high temperatures (Thermostable-protein\
    \ review supports thermostability as the mechanism extending growth into thermophilic\
    \ temperatures.)"
  causal_graph_summary: 'temperature_range_high_thermophile: 10 nodes, 9 edges'
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
- **Trait label:** temperature range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000454
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range extends above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Thermophile, TR_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports growth ranges extending above 40 °C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostability as the mechanism extending growth into thermophilic temperatures.)
- **Existing causal graph summary:** temperature_range_high_thermophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_high.yaml`.

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
- **Trait label:** temperature range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000454
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range extends above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Thermophile, TR_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports growth ranges extending above 40 °C as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostability as the mechanism extending growth into thermophilic temperatures.)
- **Existing causal graph summary:** temperature_range_high_thermophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **temperature range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_high.yaml`.

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


# Curation report: microbial **temperature range high**

## 1. Scope and interpretation

**Target trait:** **“temperature range high”**  
**Identifier:** **`METPO:1000454`**  
**Parent:** `METPO:1000306`  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED.

The trait should denote a **growth-supporting temperature range whose upper portion extends above approximately 40 °C**, not merely survival after a heat pulse. A practical annotation should record the complete tested growth range, medium, pressure, pH, salinity, atmosphere, and growth criterion. Recent literature often defines a thermophile by an optimum growth temperature above 45 °C, extreme thermophiles above approximately 65–70 °C, and hyperthermophiles above 80 °C. These conventions are useful qualifiers but are not identical to the supplied METPO definition: an organism can have a range extending above 40 °C without having an optimum above 45 °C. For example, cultured *Thermoanaerobacter kivui* has an optimum of 66 °C; under the reported experimental conditions its lowest observed growth temperature was 39 °C. *Pyrococcus furiosus* has an optimum near 100 °C, maximum of about 103 °C, and minimum near 65 °C. (lehmann2023adaptivelaboratoryevolution pages 1-2)

### Boundaries

Do **not** treat the following as sufficient evidence for `METPO:1000454`:

* **Heat-shock survival or acquired thermotolerance:** viability after exposure does not establish sustained growth.
* **High-temperature optimum or maximum alone:** these are related quantitative phenotypes, but the target is a range class.
* **Protein/enzyme thermostability:** it is a candidate mechanism, not organismal growth evidence.
* **Transient heat-shock expression:** induction at a supraoptimal temperature may protect an already thermophilic organism but does not by itself establish its basal thermophilic range.
* **Environmental sequence detection:** DNA from a taxon in hot water can reflect immigration, dormant/dead cells, or taxonomic misassignment. In an 85 °C spring, only 15 of 66 consistently detected genera had cultured strains documented to grow above 45 °C. (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 23-24)
* **Thermotolerance engineered into a mesophile:** useful causal evidence for a mechanism, but it should be marked heterologous and assay-specific unless sustained growth across a range is measured.

The phenotype is best modeled as an emergent outcome of **proteostasis, RNA stability, genome maintenance, membrane homeostasis, compatible-solute chemistry, and temperature-compatible metabolism**, rather than a single universal pathway.

## 2. Candidate nodes

### Trait and environmental nodes

| Candidate node | Type | Suggested grounding | Curation comment |
|---|---|---|---|
| temperature range high | phenotype | `METPO:1000454` | Exact target node. |
| ambient high temperature | environmental factor | Label only unless the project has an approved ENVO/PATO temperature node | Store actual °C values and assay duration as evidence metadata. |
| sustained microbial growth | biological process/assay outcome | `GO:0016049` (cell growth), if consistent with project practice | Prefer growth rate, biomass increase, CFU increase, or serial propagation over survival. |
| heat shock | experimental factor/process | `GO:0009408` (response to heat) for the response, not the exposure itself | Nearby but distinct from the target trait. |
| volcanic hot spring / hydrothermal habitat | environment | ENVO term should be selected against the exact sampled habitat | Habitat association is contextual evidence, not direct trait proof. |

### Genes, proteins, and complexes

| Candidate node | Type | Suggested grounding | Evidence status |
|---|---|---|---|
| reverse gyrase (`rgy`; PF0495 in *P. furiosus*) | enzyme/topoisomerase | `GO:0003918` DNA topoisomerase type II activity is **not sufficiently specific**; retain gene/protein label or use verified UniProt per strain | Strong, direct, but most relevant above ~90 °C and taxon-specific. |
| CspL | RNA chaperone/cold-shock-domain protein | Use the verified *Bacillus coagulans* protein accession; otherwise label only | Strong heterologous intervention evidence. |
| HSP20/small heat-shock proteins | molecular chaperone family | `GO:0051082` unfolded protein binding may describe function; verify protein accessions individually | Direct effects differ greatly among family members. |
| CeHSP17 | small heat-shock protein | Species-specific accession recommended | Strong heterologous evidence, but derived from *C. elegans*, not a microbe. |
| GroEL–GroES | group I chaperonin complex | `GO:1990220` GroEL–GroES complex | Supportive intervention evidence; smaller shift than CeHSP17. |
| thermosome α/β subunits | archaeal group II chaperonin | `GO:0005832` chaperonin-containing T-complex may be considered only after checking ontology scope | Heat-induced in *Sulfolobus*; causal trait evidence remains incomplete. |
| Phr | archaeal heat-shock transcriptional regulator | Label or verified UniProt | Regulates heat-inducible genes in *P. furiosus*; taxon-specific. |
| IPCT/DIPPS | di-myo-inositol-phosphate biosynthetic enzyme | Label plus verified UniProt/EC after sequence-level confirmation | Deletion reveals compensatory solutes rather than an essential phenotype. |
| GDGT ring synthase GrsB | lipid-modifying enzyme | Verified UniProt only | Expression/composition evidence is mainly associative and stress-specific. |
| DNA-repair proteins | module | `GO:0006281` DNA repair | Biologically plausible module; individual causal genes need direct evidence. |
| methionine-sulfoxide reductases/ROS-defense enzymes | redox-repair module | Ground individual proteins/functions after verification | Hot-spring metagenomic enrichment is associative, not causal. |

### Chemicals and membrane structures

| Candidate node | Type | Suggested grounding | Comment |
|---|---|---|---|
| di-myo-inositol phosphate (DIP) | compatible solute | ChEBI identifier should be verified before YAML insertion; label-only is safer here | Heat-induced, but functionally replaceable by MG or aspartate. |
| mannosylglycerate (MG) | compatible solute | Verify exact stereochemical CHEBI record | Interchangeable with DIP in *P. furiosus*. |
| L-aspartate | compatible solute/metabolite | `CHEBI:29991` | Compensates for DIP loss in *T. kodakarensis*. |
| glycerol dialkyl glycerol tetraether (GDGT) | archaeal membrane lipid class | Use verified LIPID MAPS/ChEBI class identifier | Class composition and cyclization matter; do not treat all GDGTs as equivalent. |
| cyclopentane rings in GDGT | structural feature | Label only | Increasing ring number tightens packing in models; growth causality is incomplete. |
| archaeal tetraether-rich monolayer membrane | cellular structure | Label only | Mechanistically linked to low permeability and temperature-insensitive behavior. |
| proton | chemical | `CHEBI:15378` | Relevant to passive proton permeability and pH homeostasis. |

### Processes/modules

* Protein folding and proteostasis—`GO:0006457` protein folding.
* RNA binding/stabilization—ground individual RNA-binding activities after protein-specific validation.
* DNA topology and positive supercoiling—label-specific process unless an exact GO term is verified.
* Membrane homeoviscous adaptation—label-only candidate module.
* Passive proton transport/permeability—model as a measured membrane property rather than an active transporter process.
* Compatible-solute biosynthesis and accumulation—ground reactions only after confirming strain-specific enzymes and Rhea/EC records.
* DNA repair and oxidative-damage repair—use broad GO modules only as intermediate nodes until causal genes are demonstrated.

## 3. Candidate causal edges

The strongest proposed edges are summarized first.

| subject | predicate | object | evidence tier | organism/condition | DOI |
|---|---|---|---|---|---|
| reverse gyrase | enables growth at | >90–95 °C temperature range high | strong intervention; taxon-specific | *Pyrococcus furiosus* Δrgy shows no significant growth at 95–100 °C, while lower temperatures remain permissive (lipscomb2017reversegyraseis pages 1-2, lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 4-5) | 10.1007/s00792-017-0929-z |
| CspL RNA-binding activity | increases | high-temperature growth | strong intervention; heterologous, taxon-transferable | *Escherichia coli* expressing thermophile-derived **cspL** shows ~2.4-fold biomass increase at 45 °C; RNA-binding-dead variant loses benefit (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2, zhou2021acoldshock pages 2-5) | 10.1038/s41421-021-00246-5 |
| CeHSP17 | maintains envelope integrity and permits growth at | 50 °C growth | strong intervention; heterologous | *E. coli* expressing **CeHSP17** grows at 50 °C and resists 58 °C heat shock; effect linked to envelope/cytoplasm integrity (ezemaduka2014asmallheat pages 1-2, ezemaduka2014asmallheat pages 5-6, ezemaduka2014asmallheat pages 3-4, ezemaduka2014asmallheat pages 6-7) | 10.1128/JB.01473-14 |
| di-myo-inositol phosphate | compensates for loss of | mannosylglycerate during heat stress | strong intervention; taxon-specific | *P. furiosus* MG-deficient mutant increases DIP under 98 °C heat stress and maintains near-parent growth (esteves2014mannosylglycerateanddi pages 20-28, esteves2014mannosylglycerateanddi pages 9-12, esteves2014mannosylglycerateanddi pages 16-20, esteves2014mannosylglycerateanddi pages 12-16) | 10.1128/AEM.00559-14 |
| mannosylglycerate | compensates for loss of | di-myo-inositol phosphate during heat stress | strong intervention; taxon-specific | *P. furiosus* DIP-deficient mutant shows growth comparable to or better than parent under heat stress, indicating interchangeable thermoprotective roles (esteves2014mannosylglycerateanddi pages 1-5, esteves2014mannosylglycerateanddi pages 9-12, esteves2014mannosylglycerateanddi pages 12-16) | 10.1128/AEM.00559-14 |
| archaeal tetraether/GDGT-rich membrane | lowers | proton permeability | mechanistic indirect-to-trait; biophysical intervention/measurement | *Sulfolobus acidocaldarius* PLFE liposomes show very low proton permeability across 65–82 °C, supporting membrane stability in hot conditions but not direct growth intervention (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 3-4, chong2024archaeamembranesin pages 1-2) | 10.3389/frbis.2023.1338019 |


*Table: This table compacts the strongest intervention-backed candidate causal edges for the high-temperature growth trait. It separates direct growth evidence from indirect but mechanistically informative membrane biophysics, while flagging taxon-specific or heterologous claims.*

### Expanded edge table

| Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---|---|---|---|---|
| high ambient temperature above ~40 °C | selects/permits classification by | `METPO:1000454` | Recent work operationally describes thermophiles as having optimum growth above 45 °C, while the supplied METPO definition uses a range extending above ~40 °C. (lehmann2023adaptivelaboratoryevolution pages 1-2) | **Definition edge**, not a molecular mechanism. Preserve the METPO threshold wording and record measured values. |
| reverse gyrase | enables | growth above 90–95 °C | In *P. furiosus*, Δ`rgy` grew comparably at 75–85 °C, had about half the control growth rate at 90 °C, and showed no significant growth at 95 or 100 °C. At 90 °C, maximum OD680 was 0.093 ± 0.003 versus 0.214 ± 0.001 for control. DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z), March 2017. (lipscomb2017reversegyraseis pages 2-4, lipscomb2017reversegyraseis pages 4-5) | **Curate, strong direct intervention; taxon- and temperature-specific.** Do not generalize to all growth above 40 °C. |
| reverse gyrase | promotes | high-temperature growth rate | In *T. kodakarensis*, Δ`rgy` shifted its maximum growth rate from 0.69 h⁻¹ at 85 °C in the host to 0.40 h⁻¹ at 75 °C; mutant/control rate ratios fell to 0.49 at 85 °C and 0.46 at 90 °C. DOI: [10.1128/JB.186.14.4829-4833.2004](https://doi.org/10.1128/JB.186.14.4829-4833.2004), July 2004. (atomi2004reversegyraseis pages 3-5, atomi2004reversegyraseis pages 1-2) | **Curate with qualifier:** promotes rather than universally required; viable growth persisted at 90 °C. |
| CspL RNA-binding activity | increases | growth at elevated temperature | Thermophile-derived CspL yielded a 2.4–2.5-fold biomass increase in *E. coli* at 45 °C; an RNA-binding-defective variant lost the benefit. CspL bound transcripts from 662 genes at 45 °C. DOI: [10.1038/s41421-021-00246-5](https://doi.org/10.1038/s41421-021-00246-5), March 2021. (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2, zhou2021acoldshock pages 2-5) | **Curate as heterologous and assay-specific.** Strong causal link from RNA binding to improved high-temperature growth, but not evidence of natural thermophily in *E. coli*. |
| CspL | increases | RNA accumulation/stability at high temperature | CspL expression increased mRNA accumulation for 1,160 genes, about 27% of the *E. coli* genome, at 45 °C; direct RNA targets expanded from 206 genes at 37 °C to 662 at 45 °C. (zhou2021acoldshock pages 5-6) | **Curate as mechanistic intermediate**, phrased “increases accumulation of diverse RNAs”; direct stabilization of every transcript is not established. |
| CeHSP17 | maintains | cell-envelope and cytoplasmic integrity under heat | CeHSP17-expressing *E. coli* retained normal morphology and grew at 50 °C, while controls showed collapsed periplasm, membrane vesiculation, and cytoplasmic aggregates. DOI: [10.1128/JB.01473-14](https://doi.org/10.1128/JB.01473-14), March 2014. (ezemaduka2014asmallheat pages 1-2, ezemaduka2014asmallheat pages 5-6) | **Curate as heterologous.** “Maintains” is supported; the proposed “thermal insulation” interpretation should remain uncertain. |
| CeHSP17 | enables | *E. coli* growth at 50 °C | Expression raised sustained growth beyond the ordinary maximum and protected against a 58 °C, 30-min lethal challenge. (ezemaduka2014asmallheat pages 3-4) | **Growth edge is strong; survival edge is separate.** Protein is nonmicrobial, so it is an engineering mechanism rather than a natural thermophile node. |
| GroEL–GroES overexpression | modestly increases | maximum *E. coli* growth temperature | Overexpression raised the maximum from 46.5 to 47.5 °C. (ezemaduka2014asmallheat pages 6-7) | **Curate only if engineering evidence is in scope.** Family-level “all chaperones cause thermophily” would be overgeneralized. |
| thermotolerant-bacterial HSP20 | increases | prolonged high-temperature viability | Fifteen of 17 soluble HSP20s improved stress resistance; *Tepidimonas sediminis* HSP20 allowed detectable *E. coli* viability after 52 °C for five days. DOI: [10.1007/s00792-023-01326-y](https://doi.org/10.1007/s00792-023-01326-y), January 2024. (sato2024effectsofsmall pages 1-2) | **Do not map directly to the target trait yet:** the endpoint is prolonged viability, not demonstrated growth at 52 °C. Useful supporting edge to thermotolerance. |
| heat shock | induces | thermosome/HSP20 heat-response program | In *S. acidocaldarius*, heat shock caused rapid transcript changes, followed by slower protein changes; thermosome α/β, HSP20, and TFS2 were among proteins increased after 30 min. DOI: [10.1128/mbio.03593-22](https://doi.org/10.1128/mbio.03593-22), October 2023. (baes2023transcriptionalandtranslational pages 15-17) | **Uncertain for trait graph:** observational time-series response at supraoptimal heat, not proof that these proteins establish the baseline growth range. |
| Phr regulator | regulates/represses | heat-inducible gene program | In *P. furiosus*, Phr is described as a negative regulator of heat-inducible genes; the 2023 study compared 105 °C shock with a 95 °C baseline. DOI: [10.1128/mbio.02174-23](https://doi.org/10.1128/mbio.02174-23), December 2023. (grunberger2023uncoveringthetemporal pages 2-4) | **Taxon-specific regulatory edge.** Connect to heat-shock response, not directly to `METPO:1000454`, unless perturbation changes growth range. |
| increasing GDGT cyclopentane-ring number | increases | membrane packing/rigidity | A 2024 synthesis reports that cyclopentane rings tighten packing and hinder chain rotation; simulations show increased packing density and interaction energy. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019), January 2024. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 3-4) | **Mechanistic but indirect.** Simulation/biophysics supports membrane-property edges, not an organismal growth-range edge. |
| tetraether/GDGT-rich archaeal membrane | decreases | passive proton permeability at high temperature | *S. acidocaldarius* polar-lipid liposomes had proton permeability of 0.3–0.5 × 10⁻⁸ cm/s at 65–82 °C versus 3–9 × 10⁻⁸ cm/s for egg phosphatidylcholine. (chong2024archaeamembranesin pages 2-3) | **Curate as a measured biophysical edge.** It supports, but does not prove, high-temperature growth. |
| increased growth temperature | increases | average GDGT cyclization | In *S. acidocaldarius*, mean cyclopentane-ring number reportedly rose from 3.4 to 4.8 as temperature increased from 65 to 82 °C. (chong2024archaeamembranesin pages 1-2) | **Correlative/reversible environmental-response edge.** Do not invert it into “rings cause thermophily” without genetic growth phenotypes. |
| heat stress | increases | DIP accumulation | In *T. kodakarensis*, DIP increased 20-fold from 85 to 93.7 °C; `IPCT/DIPPS` expression increased 1.6-fold. DOI: [10.1128/JB.01115-09](https://doi.org/10.1128/JB.01115-09), January 2010. (borges2010thermococcuskodakarensis pages 1-2, borges2010thermococcuskodakarensis pages 3-4) | **Curate as a response edge**, not as proof that DIP is essential. |
| aspartate accumulation | compensates for | loss of DIP biosynthesis | A DIP-deficient *T. kodakarensis* mutant accumulated 0.265 μmol aspartate per mg protein and grew at 0.42 ± 0.02 h⁻¹ under heat stress versus 0.41 ± 0.06 h⁻¹ for the parent. (borges2010thermococcuskodakarensis pages 5-6) | **Curate, strong compensation edge.** This argues against an indispensable DIP→trait edge. |
| DIP | compensates for | loss of MG under heat stress | At 98 °C, MG-deficient *P. furiosus* increased DIP to 55% of its solute pool and maintained near-parent growth. DOI: [10.1128/AEM.00559-14](https://doi.org/10.1128/AEM.00559-14), July 2014. (esteves2014mannosylglycerateanddi pages 20-28, esteves2014mannosylglycerateanddi pages 9-12) | **Curate, strong and taxon-specific.** |
| MG | compensates for | loss of DIP under heat stress | DIP-deficient *P. furiosus* had growth nearly superimposable on, or better than, the parent at heat stress because MG substituted effectively. (esteves2014mannosylglycerateanddi pages 1-5, esteves2014mannosylglycerateanddi pages 12-16) | **Curate, strong and taxon-specific.** Model redundancy rather than two independent essential edges. |
| compatible-solute redundancy | supports | growth during supraoptimal heat | Parent, MG-deficient, and DIP-deficient strains had similar growth at 98 °C; the total solute pool remained approximately 0.65–0.68 μmol/mg protein. (esteves2014mannosylglycerateanddi pages 9-12) | **Recommended aggregate edge.** The robust mechanism is maintenance of a protective solute pool, not dependence on one named solute. |
| adaptive evolution at 45 °C | shifts downward | optimum growth temperature | After 67 transfers, approximately 180 generations, *T. kivui* shifted its optimum from 66 to 60 °C but did not improve growth at 45 °C. DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216), October 2023. (lehmann2023adaptivelaboratoryevolution pages 1-2) | **Do not curate a specific causal gene edge:** 67 SNPs were present and the molecular basis remained unresolved. This is useful evidence that optimum and range are separable phenotypes. |

## 4. Current understanding and expert analysis

The intervention literature supports a **layered, partially redundant causal architecture**:

1. **Proteome/RNA maintenance can extend growth limits.** CspL provides unusually strong evidence because the phenotype depends on its nucleotide-binding function, while CeHSP17 and GroEL–GroES demonstrate that increasing folding or envelope-protection capacity can move the upper growth boundary. These are powerful engineering demonstrations, although they do not establish that the same proteins naturally determine thermophile ranges. (zhou2021acoldshock pages 1-2, ezemaduka2014asmallheat pages 5-6, ezemaduka2014asmallheat pages 6-7)
2. **Genome topology becomes especially consequential near the upper limit of hyperthermophily.** Reverse gyrase is beneficial below 90 °C in tested Thermococcales but becomes essential around 95–100 °C in *P. furiosus*. It is therefore a threshold- and lineage-dependent mechanism, not a universal cause of all growth above 40 °C. (lipscomb2017reversegyraseis pages 1-2, atomi2004reversegyraseis pages 3-5)
3. **Membrane chemistry supplies a plausible enabling layer.** Tetraether-rich archaeal membranes display exceptionally low proton permeability that is relatively insensitive to temperature. Yet much of the evidence connecting GDGT cyclization to growth temperature remains compositional, model-based, or biophysical rather than genetic. (chong2024archaeamembranesin pages 2-3, chiu2023membranelipidand pages 1-2, siliakus2017adaptationsofarchaeal pages 8-10)
4. **Compatible solutes exhibit functional degeneracy.** DIP is a conspicuous marker of many hyperthermophiles and strongly heat-induced, but deletion studies show that MG or aspartate can replace it. A graph asserting that DIP alone causes the trait would therefore be misleading. (esteves2014mannosylglycerateanddi pages 9-12, borges2010thermococcuskodakarensis pages 1-2)
5. **Heat-shock programs are not equivalent to constitutive thermophilic physiology.** In 2023, multi-omics studies showed rapid, broad, and temporally structured responses in *S. acidocaldarius* and *P. furiosus*. These identify candidate regulators and effectors, but perturbation experiments are still required before most can be linked directly to the organism’s growth range. (grunberger2023uncoveringthetemporal pages 2-4, baes2023transcriptionalandtranslational pages 15-17)

## 5. Recent developments, applications, and quantitative context

### 2023–2024 research

* **Temporal multi-omics:** *P. furiosus* exposed to 105 °C from a 95 °C baseline showed a rapid Phr-centered heat-response program, while *S. acidocaldarius* shifted from its 75 °C optimum to 86 °C and displayed rapid transcriptional but slower proteomic remodeling. These studies sharpen the distinction between immediate stress regulation and stable thermophile physiology. (grunberger2023uncoveringthetemporal pages 2-4, baes2023transcriptionalandtranslational pages 15-17)
* **Membrane lipid caution:** The 2023 *Saccharolobus islandicus* study found lower GDGT cyclization under acid and cold stress and warned that transcription of `grsB` does not reliably predict lipid composition. This argues against transcript-only causal annotation. (chiu2023membranelipidand pages 1-2)
* **Small-HSP engineering:** In 2024, 15 of 17 expressed bacterial HSP20 proteins improved one or more stress-resistance endpoints in *E. coli*; one construct preserved viability for more than 100 hours at 52 °C. This is a practical stress-engineering result, although not sustained-growth evidence at that temperature. (sato2024effectsofsmall pages 1-2)
* **Evolution of thermal niche:** ALE shifted *T. kivui* optimum by 6 °C after ~180 generations without improving growth at the selection temperature, illustrating that optimum, minimum, maximum, and range width must be modeled separately. (lehmann2023adaptivelaboratoryevolution pages 1-2)
* **Environmental implementation/context:** In an 85 °C Trans-Himalayan spring, cell density was approximately 8.5 × 10⁴ mL⁻¹, live:dead ratio 1.7, Aquificae comprised 80% of 16S reads, and a Hydrogenobacter-related MAG comprised about 56% of the metagenome. However, Aquificae represented only about 25% of protein-coding genes, and most detected genera lacked cultured growth above 45 °C. (mondal2024aquificaeovercomescompetition pages 24-26, mondal2024aquificaeovercomescompetition pages 1-2)

### Real-world applications

* **High-temperature fermentation:** CspL is a demonstrated transferable tool: it increased *E. coli* biomass 2.4-fold at 45 °C, *Saccharomyces cerevisiae* biomass about 2.6–2.7-fold at 36 °C, and *Pseudomonas putida* biomass 1.4-fold at elevated temperature. Higher-temperature operation can potentially reduce cooling requirements and contamination risk, although process-scale validation is separate from laboratory growth assays. (zhou2021acoldshock pages 5-6, zhou2021acoldshock pages 1-2)
* **Robust production hosts:** HSP20, CeHSP17, and GroEL–GroES interventions offer modules for protecting proteins and envelopes during thermal excursions. HSP20 results also suggest cross-protection against pH and osmotic stress, but such pleiotropy requires construct-specific testing. (sato2024effectsofsmall pages 1-2, ezemaduka2014asmallheat pages 6-7)
* **Thermostable biocatalysis and biomaterials:** Thermophile-derived chaperones and low-permeability tetraether membranes motivate enzyme-production platforms and durable lipid vesicles. The membrane evidence is strongest at the liposome-property level, not yet at direct engineering of a broader microbial growth range. (chong2024archaeamembranesin pages 2-3)
* **Hot-process biogeochemistry:** Aquificae dominance and sulfur-oxidation capacity in high-temperature springs support applications in thermophilic sulfur cycling and high-temperature bioprocess prospecting, but MAG abundance is insufficient to assign `METPO:1000454` to every detected lineage. (mondal2024aquificaeovercomescompetition pages 26-28, mondal2024aquificaeovercomescompetition pages 1-2)

## 6. Recommended initial TraitMech graph

A conservative first graph should emphasize experimentally supported intermediate mechanisms:

1. `high ambient temperature` → **causes** → `protein unfolding / RNA instability / membrane leak / DNA-topology stress` — conceptual aggregate; retain as a mechanism scaffold, not a single-source assertion.
2. `CspL RNA-binding activity` → **increases** → `RNA accumulation at elevated temperature` → **increases** → `high-temperature growth` — heterologous, strong.
3. `small heat-shock protein activity` → **maintains** → `protein and cell-envelope integrity` → **permits** → `growth at elevated temperature` — protein-specific; do not universalize.
4. `reverse gyrase` → **maintains** → `high-temperature-compatible DNA topology/genome function` → **enables** → `growth above 90–95 °C` — strong for tested hyperthermophilic archaea; threshold-specific.
5. `tetraether/GDGT-rich membrane` → **decreases** → `passive proton permeability` → **supports** → `ion/pH homeostasis at high temperature` → **supports** → `temperature range high` — final edge indirect/uncertain.
6. `heat stress` → **increases** → `DIP accumulation`; `DIP`, `MG`, or `aspartate` → **maintains** → `compatible-solute thermoprotection` → **supports** → `growth during supraoptimal heat` — redundant and taxon-specific.
7. `heat shock` → **activates** → `Phr/thermosome/HSP20 response module` → **supports** → `recovery from thermal stress` — keep separate from the basal range trait until growth-range perturbations are available.

## 7. Warnings: claims not yet ready for TraitMech

1. **Do not curate “reverse gyrase causes thermophily” without a temperature/taxon qualifier.** It is dispensable for growth at 90 °C in one tested strain but essential at 95–100 °C in *P. furiosus*. (lipscomb2017reversegyraseis pages 2-4, atomi2004reversegyraseis pages 1-2)
2. **Do not curate DIP as universally required.** DIP-null strains can retain high-temperature growth through MG or aspartate compensation. (borges2010thermococcuskodakarensis pages 5-6, esteves2014mannosylglycerateanddi pages 12-16)
3. **Do not infer growth from HSP expression, metagenomic occurrence, or post-heat viability.** These endpoints support mechanism discovery but are not the target phenotype.
4. **Do not infer membrane causality solely from lipid-temperature correlations.** The low-permeability edge is strong; the final lipid→growth-range edge remains indirect. (chong2024archaeamembranesin pages 2-3, chong2024archaeamembranesin pages 1-2)
5. **Do not use genus-level environmental detections as strain-level thermal traits.** The 2024 hot-spring study explicitly demonstrates the mismatch between environmental detection and cultured thermal capacity. (mondal2024aquificaeovercomescompetition pages 1-2, mondal2024aquificaeovercomescompetition pages 23-24)
6. **Do not assign unverified CURIEs.** DIP, MG, GDGT subclasses, strain proteins, and specific enzymes should remain label-only until exact stereochemistry, sequence, and database records are checked.
7. **Do not merge high temperature range, high optimum, high maximum, and heat-shock resistance.** They can covary but are experimentally and causally distinct.

## 8. DOI-first bibliography

1. **Lipscomb GL et al.** “Reverse gyrase is essential for microbial growth at 95 °C.” *Extremophiles* 21, 603–608. Published March 2017. DOI: [10.1007/s00792-017-0929-z](https://doi.org/10.1007/s00792-017-0929-z). (lipscomb2017reversegyraseis pages 1-2)
2. **Atomi H, Matsumi R, Imanaka T.** “Reverse Gyrase Is Not a Prerequisite for Hyperthermophilic Life.” *Journal of Bacteriology* 186, 4829–4833. Published July 2004. DOI: [10.1128/JB.186.14.4829-4833.2004](https://doi.org/10.1128/JB.186.14.4829-4833.2004). (atomi2004reversegyraseis pages 3-5)
3. **Zhou Z et al.** “A cold shock protein promotes high-temperature microbial growth through binding to diverse RNA species.” *Cell Discovery* 7. Published March 2021. DOI: [10.1038/s41421-021-00246-5](https://doi.org/10.1038/s41421-021-00246-5). (zhou2021acoldshock pages 1-2)
4. **Sato Y, Okano K, Honda K.** “Effects of small heat shock proteins from thermotolerant bacteria on the stress resistance of *Escherichia coli* to temperature, pH, and hyperosmolarity.” *Extremophiles* 28. Published January 2024. DOI: [10.1007/s00792-023-01326-y](https://doi.org/10.1007/s00792-023-01326-y). (sato2024effectsofsmall pages 1-2)
5. **Ezemaduka AN et al.** “A Small Heat Shock Protein Enables *Escherichia coli* To Grow at a Lethal Temperature of 50°C Conceivably by Maintaining Cell Envelope Integrity.” *Journal of Bacteriology* 196, 2004–2011. Published March 2014. DOI: [10.1128/JB.01473-14](https://doi.org/10.1128/JB.01473-14). (ezemaduka2014asmallheat pages 1-2)
6. **Borges N et al.** “*Thermococcus kodakarensis* Mutants Deficient in Di-myo-Inositol Phosphate Use Aspartate To Cope with Heat Stress.” *Journal of Bacteriology* 192, 191–197. Published January 2010. DOI: [10.1128/JB.01115-09](https://doi.org/10.1128/JB.01115-09). (borges2010thermococcuskodakarensis pages 1-2)
7. **Esteves AM et al.** “Mannosylglycerate and Di-myo-Inositol Phosphate Have Interchangeable Roles during Adaptation of *Pyrococcus furiosus* to Heat Stress.” *Applied and Environmental Microbiology* 80, 4226–4233. Published July 2014. DOI: [10.1128/AEM.00559-14](https://doi.org/10.1128/AEM.00559-14). (esteves2014mannosylglycerateanddi pages 1-5)
8. **Baes R et al.** “Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon *Sulfolobus acidocaldarius*.” *mBio* 14. Published October 2023. DOI: [10.1128/mbio.03593-22](https://doi.org/10.1128/mbio.03593-22). (baes2023transcriptionalandtranslational pages 15-17)
9. **Grünberger F et al.** “Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.” *mBio* 14. Published December 2023. DOI: [10.1128/mbio.02174-23](https://doi.org/10.1128/mbio.02174-23). (grunberger2023uncoveringthetemporal pages 2-4)
10. **Chiu BK et al.** “Membrane lipid and expression responses of *Saccharolobus islandicus* REY15A to acid and cold stress.” *Frontiers in Microbiology* 14. Published August 2023. DOI: [10.3389/fmicb.2023.1219779](https://doi.org/10.3389/fmicb.2023.1219779). (chiu2023membranelipidand pages 1-2)
11. **Chong PL-G.** “Archaea membranes in response to extreme acidic environments.” *Frontiers in Biophysics* 1. Published January 2024. DOI: [10.3389/frbis.2023.1338019](https://doi.org/10.3389/frbis.2023.1338019). (chong2024archaeamembranesin pages 2-3)
12. **Siliakus MF, van der Oost J, Kengen SWM.** “Adaptations of archaeal and bacterial membranes to variations in temperature, pH and pressure.” *Extremophiles* 21, 651–670. Published May 2017. DOI: [10.1007/s00792-017-0939-x](https://doi.org/10.1007/s00792-017-0939-x). (siliakus2017adaptationsofarchaeal pages 8-10)
13. **Lehmann M et al.** “Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.” *Frontiers in Microbiology* 14. Published October 2023. DOI: [10.3389/fmicb.2023.1265216](https://doi.org/10.3389/fmicb.2023.1265216). (lehmann2023adaptivelaboratoryevolution pages 1-2)
14. **Mondal N et al.** “Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a Trans-Himalayan sulfur-borax spring.” *PLOS ONE* 19:e0310595. Published April 2024. DOI: [10.1371/journal.pone.0310595](https://doi.org/10.1371/journal.pone.0310595). (mondal2024aquificaeovercomescompetition pages 1-2)

**Curation priority:** The most defensible additions are the reverse-gyrase threshold mechanism, CspL→RNA accumulation→high-temperature growth, protein-specific small-HSP/chaperone effects, and compatible-solute compensation. Membrane cyclization, broad DNA-repair modules, oxidative-stress defenses, and 2023 heat-shock regulons should remain intermediate or uncertain until perturbations demonstrate a changed growth-supporting temperature range.

References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (mondal2024aquificaeovercomescompetition pages 1-2): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19:e0310595-e0310595, Apr 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 10 citations and is from a peer-reviewed journal.

3. (mondal2024aquificaeovercomescompetition pages 23-24): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19:e0310595-e0310595, Apr 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 10 citations and is from a peer-reviewed journal.

4. (lipscomb2017reversegyraseis pages 1-2): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

5. (lipscomb2017reversegyraseis pages 2-4): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

6. (lipscomb2017reversegyraseis pages 4-5): Gina L. Lipscomb, Elin M. Hahn, Alexander T. Crowley, and Michael W. W. Adams. Reverse gyrase is essential for microbial growth at 95 °c. Extremophiles, 21:603-608, Mar 2017. URL: https://doi.org/10.1007/s00792-017-0929-z, doi:10.1007/s00792-017-0929-z. This article has 44 citations and is from a peer-reviewed journal.

7. (zhou2021acoldshock pages 5-6): Zikang Zhou, Hongzhi Tang, Weiwei Wang, Lige Zhang, Fei Su, Yuanting Wu, Linquan Bai, Sicong Li, Yuhui Sun, Fei Tao, and Ping Xu. A cold shock protein promotes high-temperature microbial growth through binding to diverse rna species. Cell Discovery, Mar 2021. URL: https://doi.org/10.1038/s41421-021-00246-5, doi:10.1038/s41421-021-00246-5. This article has 45 citations and is from a peer-reviewed journal.

8. (zhou2021acoldshock pages 1-2): Zikang Zhou, Hongzhi Tang, Weiwei Wang, Lige Zhang, Fei Su, Yuanting Wu, Linquan Bai, Sicong Li, Yuhui Sun, Fei Tao, and Ping Xu. A cold shock protein promotes high-temperature microbial growth through binding to diverse rna species. Cell Discovery, Mar 2021. URL: https://doi.org/10.1038/s41421-021-00246-5, doi:10.1038/s41421-021-00246-5. This article has 45 citations and is from a peer-reviewed journal.

9. (zhou2021acoldshock pages 2-5): Zikang Zhou, Hongzhi Tang, Weiwei Wang, Lige Zhang, Fei Su, Yuanting Wu, Linquan Bai, Sicong Li, Yuhui Sun, Fei Tao, and Ping Xu. A cold shock protein promotes high-temperature microbial growth through binding to diverse rna species. Cell Discovery, Mar 2021. URL: https://doi.org/10.1038/s41421-021-00246-5, doi:10.1038/s41421-021-00246-5. This article has 45 citations and is from a peer-reviewed journal.

10. (ezemaduka2014asmallheat pages 1-2): Anastasia N Ezemaduka, Jiayu Yu, Xiaodong Shi, Kaiming Zhang, Chang-Cheng Yin, Xinmiao Fu, and Z. Chang. A small heat shock protein enables escherichia coli to grow at a lethal temperature of 50°c conceivably by maintaining cell envelope integrity. Journal of Bacteriology, 196:2004-2011, Mar 2014. URL: https://doi.org/10.1128/jb.01473-14, doi:10.1128/jb.01473-14. This article has 69 citations and is from a peer-reviewed journal.

11. (ezemaduka2014asmallheat pages 5-6): Anastasia N Ezemaduka, Jiayu Yu, Xiaodong Shi, Kaiming Zhang, Chang-Cheng Yin, Xinmiao Fu, and Z. Chang. A small heat shock protein enables escherichia coli to grow at a lethal temperature of 50°c conceivably by maintaining cell envelope integrity. Journal of Bacteriology, 196:2004-2011, Mar 2014. URL: https://doi.org/10.1128/jb.01473-14, doi:10.1128/jb.01473-14. This article has 69 citations and is from a peer-reviewed journal.

12. (ezemaduka2014asmallheat pages 3-4): Anastasia N Ezemaduka, Jiayu Yu, Xiaodong Shi, Kaiming Zhang, Chang-Cheng Yin, Xinmiao Fu, and Z. Chang. A small heat shock protein enables escherichia coli to grow at a lethal temperature of 50°c conceivably by maintaining cell envelope integrity. Journal of Bacteriology, 196:2004-2011, Mar 2014. URL: https://doi.org/10.1128/jb.01473-14, doi:10.1128/jb.01473-14. This article has 69 citations and is from a peer-reviewed journal.

13. (ezemaduka2014asmallheat pages 6-7): Anastasia N Ezemaduka, Jiayu Yu, Xiaodong Shi, Kaiming Zhang, Chang-Cheng Yin, Xinmiao Fu, and Z. Chang. A small heat shock protein enables escherichia coli to grow at a lethal temperature of 50°c conceivably by maintaining cell envelope integrity. Journal of Bacteriology, 196:2004-2011, Mar 2014. URL: https://doi.org/10.1128/jb.01473-14, doi:10.1128/jb.01473-14. This article has 69 citations and is from a peer-reviewed journal.

14. (esteves2014mannosylglycerateanddi pages 20-28): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

15. (esteves2014mannosylglycerateanddi pages 9-12): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

16. (esteves2014mannosylglycerateanddi pages 16-20): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

17. (esteves2014mannosylglycerateanddi pages 12-16): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

18. (esteves2014mannosylglycerateanddi pages 1-5): Ana M. Esteves, Sanjeev K. Chandrayan, Patrick M. McTernan, Nuno Borges, Michael W. W. Adams, and Helena Santos. Mannosylglycerate and di- <i>myo</i> -inositol phosphate have interchangeable roles during adaptation of pyrococcus furiosus to heat stress. Applied and Environmental Microbiology, 80:4226-4233, Jul 2014. URL: https://doi.org/10.1128/aem.00559-14, doi:10.1128/aem.00559-14. This article has 37 citations and is from a peer-reviewed journal.

19. (chong2024archaeamembranesin pages 2-3): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

20. (chong2024archaeamembranesin pages 3-4): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

21. (chong2024archaeamembranesin pages 1-2): Parkson Lee-Gau Chong. Archaea membranes in response to extreme acidic environments. Frontiers in Biophysics, Jan 2024. URL: https://doi.org/10.3389/frbis.2023.1338019, doi:10.3389/frbis.2023.1338019. This article has 10 citations.

22. (atomi2004reversegyraseis pages 3-5): Haruyuki Atomi, Rie Matsumi, and Tadayuki Imanaka. Reverse gyrase is not a prerequisite for hyperthermophilic life. Journal of Bacteriology, 186:4829-4833, Jul 2004. URL: https://doi.org/10.1128/jb.186.14.4829-4833.2004, doi:10.1128/jb.186.14.4829-4833.2004. This article has 165 citations and is from a peer-reviewed journal.

23. (atomi2004reversegyraseis pages 1-2): Haruyuki Atomi, Rie Matsumi, and Tadayuki Imanaka. Reverse gyrase is not a prerequisite for hyperthermophilic life. Journal of Bacteriology, 186:4829-4833, Jul 2004. URL: https://doi.org/10.1128/jb.186.14.4829-4833.2004, doi:10.1128/jb.186.14.4829-4833.2004. This article has 165 citations and is from a peer-reviewed journal.

24. (sato2024effectsofsmall pages 1-2): Yu Sato, Kenji Okano, and Kohsuke Honda. Effects of small heat shock proteins from thermotolerant bacteria on the stress resistance of escherichia coli to temperature, ph, and hyperosmolarity. Extremophiles, Jan 2024. URL: https://doi.org/10.1007/s00792-023-01326-y, doi:10.1007/s00792-023-01326-y. This article has 21 citations and is from a peer-reviewed journal.

25. (baes2023transcriptionalandtranslational pages 15-17): Rani Baes, Felix Grünberger, Sébastien Pyr dit Ruys, Mohea Couturier, Sarah De Keulenaer, Sonja Skevin, Filip Van Nieuwerburgh, Didier Vertommen, Dina Grohmann, Sébastien Ferreira-Cerca, and Eveline Peeters. Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon <i>sulfolobus acidocaldarius</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.03593-22, doi:10.1128/mbio.03593-22. This article has 17 citations and is from a domain leading peer-reviewed journal.

26. (grunberger2023uncoveringthetemporal pages 2-4): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 23 citations and is from a domain leading peer-reviewed journal.

27. (borges2010thermococcuskodakarensis pages 1-2): Nuno Borges, Rie Matsumi, Tadayuki Imanaka, Haruyuki Atomi, and Helena Santos. <i>thermococcus kodakar</i> <i>ensis</i> mutants deficient in di- <i>myo</i> -inositol phosphate use aspartate to cope with heat stress. Journal of Bacteriology, 192:191-197, Jan 2010. URL: https://doi.org/10.1128/jb.01115-09, doi:10.1128/jb.01115-09. This article has 47 citations and is from a peer-reviewed journal.

28. (borges2010thermococcuskodakarensis pages 3-4): Nuno Borges, Rie Matsumi, Tadayuki Imanaka, Haruyuki Atomi, and Helena Santos. <i>thermococcus kodakar</i> <i>ensis</i> mutants deficient in di- <i>myo</i> -inositol phosphate use aspartate to cope with heat stress. Journal of Bacteriology, 192:191-197, Jan 2010. URL: https://doi.org/10.1128/jb.01115-09, doi:10.1128/jb.01115-09. This article has 47 citations and is from a peer-reviewed journal.

29. (borges2010thermococcuskodakarensis pages 5-6): Nuno Borges, Rie Matsumi, Tadayuki Imanaka, Haruyuki Atomi, and Helena Santos. <i>thermococcus kodakar</i> <i>ensis</i> mutants deficient in di- <i>myo</i> -inositol phosphate use aspartate to cope with heat stress. Journal of Bacteriology, 192:191-197, Jan 2010. URL: https://doi.org/10.1128/jb.01115-09, doi:10.1128/jb.01115-09. This article has 47 citations and is from a peer-reviewed journal.

30. (chiu2023membranelipidand pages 1-2): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

31. (siliakus2017adaptationsofarchaeal pages 8-10): Melvin F. Siliakus, John van der Oost, and Servé W. M. Kengen. Adaptations of archaeal and bacterial membranes to variations in temperature, ph and pressure. Extremophiles, 21:651-670, May 2017. URL: https://doi.org/10.1007/s00792-017-0939-x, doi:10.1007/s00792-017-0939-x. This article has 551 citations and is from a peer-reviewed journal.

32. (mondal2024aquificaeovercomescompetition pages 24-26): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19:e0310595-e0310595, Apr 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 10 citations and is from a peer-reviewed journal.

33. (mondal2024aquificaeovercomescompetition pages 26-28): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. BioRxiv, Jul 2023. URL: https://doi.org/10.1101/2023.07.10.548480, doi:10.1101/2023.07.10.548480. This article has 0 citations.