---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:59:42.213955'
end_time: '2026-06-18T02:10:08.474972'
duration_seconds: 626.26
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'temperature_optimum_high_thermophile_setpoint: 4 nodes, 3
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum high
- **METPO identifier:** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Thermophile, TO_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the >40 °C optimum as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostable proteins as the mechanism enabling thermophile optima.)
- **Existing causal graph summary:** temperature_optimum_high_thermophile_setpoint: 4 nodes, 3 edges

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
- **METPO identifier:** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature above approximately 40 °C, characteristic of thermophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Thermophile, TO_>40
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the >40 °C optimum as the thermophile category.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports thermostable proteins as the mechanism enabling thermophile optima.)
- **Existing causal graph summary:** temperature_optimum_high_thermophile_setpoint: 4 nodes, 3 edges

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


## Microbial Trait Causal Graph Research Report: **temperature optimum high** (METPO:1000447)

### Trait metadata (target)
- **Trait label:** temperature optimum high
- **METPO:** METPO:1000447
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Definition (given):** “temperature optimum phenotype with the best-growth ambient temperature above ~40 °C, characteristic of thermophilic physiology.”
- **Synonyms:** Thermophile, TO_>40

---

## 1) Trait scope (phenotype definition, boundaries, assay interpretation)

### 1.1 What the trait represents
“Temperature optimum high” corresponds to a **growth phenotype**: the **optimal growth temperature (TOPT)** is above a threshold (METPO suggests ~40 °C). Contemporary microbiology often operationalizes this using **cardinal temperatures**: **TMIN**, **TOPT**, and **TMAX** (minimum, optimum, maximum temperatures for growth), measured under defined medium/atmosphere conditions. (lehmann2023adaptivelaboratoryevolution pages 1-2)

### 1.2 Common categorical cutoffs (thermophile, extreme thermophile, hyperthermophile)
Recent peer-reviewed sources explicitly define temperature classes (note: these cutoffs vary by community and are not perfectly standardized):
- One 2023 study defines: **thermophiles** as TOPT **>45 °C**, **extreme thermophiles** as TOPT **>65–70 °C**, and **hyperthermophiles** as **>80 °C**; it also gives a hyperthermophile example (*Pyrococcus furiosus* TOPT ~100 °C). (lehmann2023adaptivelaboratoryevolution pages 1-2)
- A 2024 systematic review similarly states thermophile survival spans ~41–122 °C and provides subcategories: **moderate (50–64 °C)**, **extreme (65–79 °C)**, **hyperthermophile (>80 °C)**. (arfah2024systematicreviewon pages 3-5)

**Curation implication:** METPO’s “>~40 °C” will include organisms some papers would call “moderate thermophiles” and could even include borderline strains at 41–45 °C that some frameworks might label **thermotolerant mesophiles**. Because the evidence base often uses **>45 °C** for “thermophile,” the YAML should preserve the METPO definition but include a boundary note.

### 1.3 Boundary cases to distinguish
- **Thermotolerance vs thermophily:** heat-shock survival and transient stress responses (minutes–hours) are not the same as having a **high TOPT**. Many sources discuss heat-shock chaperones/proteases as stress responses; these may contribute to growth at high temperature, but evidence often comes from **temperature shift** experiments rather than TOPT assays. (grunberger2023uncoveringthetemporal pages 1-2, baes2023transcriptionalandtranslational pages 1-2)
- **Acidothermophily/polyextremophily:** some thermophiles (e.g., *Sulfolobus acidocaldarius*) are thermoacidophiles; mechanisms may reflect joint adaptation to temperature and pH. (baes2023transcriptionalandtranslational pages 1-2)

---

## 2) Key concepts and mechanistic definitions (current understanding)

Thermophily is widely understood as a systems-level phenotype requiring coordinated stability of **(i) genome/DNA**, **(ii) proteome/protein homeostasis (proteostasis)**, and **(iii) membranes**, plus repair/regulation layers.

### 2.1 DNA topology & genome integrity under high temperature
- **Reverse gyrase (TopR)** is emphasized as a hallmark of extreme thermophiles/hyperthermophiles. It introduces **positive supercoils** into DNA and is proposed to reduce DNA melting and support genome integrity/repair at high temperature. (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3)

### 2.2 Genome organization/packaging
Thermophiles mitigate heat-driven DNA denaturation and damage using chromatin-like packaging:
- **Nucleoid-associated proteins (NAPs)** and **archaeal histones** are highlighted as contributors to DNA thermostability and 3D genome organization; abundance of NAPs/histones can correlate with growth temperature in archaea. (takemata2024howdothermophiles pages 2-3)
- **SMC-family proteins** are implicated in higher-order chromosome organization/loops in thermophilic archaea, linking genome architecture to stable inheritance and function under extreme conditions. (takemata2024howdothermophiles pages 4-5)

### 2.3 Proteostasis: chaperones, chaperonins, proteases/proteasome
High temperatures increase protein unfolding/aggregation risk; thermophiles rely on:
- **Small heat shock proteins (sHSPs)**, **prefoldin**, and **group II chaperonins (“thermosome”)** in archaea. In *S. acidocaldarius*, prefoldin and sHSPs bind denaturing proteins and shuttle to thermosome, which refolds proteins ATP-dependently. (baes2023transcriptionalandtranslational pages 1-2)
- General heat-shock regulation is described as inducing chaperones (e.g., DnaK, GroEL) and proteases for refolding/degradation pathways. (grunberger2023uncoveringthetemporal pages 1-2)

### 2.4 Membrane composition and remodeling
Membranes must remain functional despite temperature effects on fluidity/permeability.
- Heat shock can change membrane lipid composition (e.g., in *S. acidocaldarius*), and unique membrane composition is repeatedly listed as a thermophile adaptation theme. (baes2023transcriptionalandtranslational pages 1-2, grunberger2023uncoveringthetemporal pages 1-2)
- Experimental evolution in a thermophile (*Thermoanaerobacter kivui*) observed **temperature-associated fatty acid composition shifts** and altered **plasmalogen proportions**, linking lipid remodeling to temperature phenotypes (though directionality was toward a reduced TOPT). (lehmann2023adaptivelaboratoryevolution pages 6-7)

---

## 3) Candidate causal-graph entities (nodes), grouped by type (with ontology grounding suggestions)

### 3.1 Environmental / experimental factors
- **High ambient temperature** (label-only; ENVO term likely exists but not retrieved in provided evidence)
- **Heat shock / temperature upshift** (GO:0009408 response to heat) (baes2023transcriptionalandtranslational pages 1-2)
- **Geothermal/hot spring / hydrothermal vent context** (label-only; e.g., “boiling (85 °C) fluid vented”) (mondal2024aquificaeovercomescompetition pages 1-2)

### 3.2 Phenotypes and intermediate states
- **Cardinal temperatures:** TMIN, TOPT, TMAX (label-only) (lehmann2023adaptivelaboratoryevolution pages 1-2)
- **Positive DNA supercoiling** (GO:0006265 DNA topological change; label-only) (takemata2024howdothermophiles pages 1-2)
- **DNA melting resistance / genome thermostability** (label-only) (takemata2024howdothermophiles pages 1-2)
- **Protein thermostability / reduced aggregation** (label-only) (grunberger2023uncoveringthetemporal pages 1-2, baes2023transcriptionalandtranslational pages 1-2)
- **Membrane stability / permeability control** (label-only) (baes2023transcriptionalandtranslational pages 1-2)

### 3.3 Genes / proteins / complexes
**DNA topology and genome organization**
- Reverse gyrase **TopR/TopR1** (protein label; often “reverse gyrase”) (takemata2024howdothermophiles pages 1-2, baes2023transcriptionalandtranslational pages 1-2)
- Topoisomerases (Topo III, Topo VI; label-only) (takemata2024howdothermophiles pages 4-5)
- NAPs (e.g., **Alba**, **Cren7**) (label-only) (takemata2024howdothermophiles pages 4-5)
- Archaeal **histones** (label-only; GO:0000786 nucleosome suggested for nucleosome-like packaging) (takemata2024howdothermophiles pages 2-3)
- **SMC** proteins / condensin-like organization (label-only; GO:0000796 condensin complex) (takemata2024howdothermophiles pages 4-5)

**Proteostasis**
- **Small heat shock proteins (sHSPs)** (label-only) (baes2023transcriptionalandtranslational pages 1-2)
- **Prefoldin** (label-only) (baes2023transcriptionalandtranslational pages 1-2)
- **Thermosome** (group II chaperonin; subunits Thα/Thβ/Thγ, label-only) (baes2023transcriptionalandtranslational pages 1-2)
- **DnaK** and **GroEL** (bacterial chaperone exemplars; UniProt grounding not provided here) (grunberger2023uncoveringthetemporal pages 1-2)
- Proteases / proteasome-associated pathways (label-only) (grunberger2023uncoveringthetemporal pages 1-2, baes2023transcriptionalandtranslational pages 21-21)

**Membrane/lipid**
- **Fatty acid desaturases** (EC family-level label) (mondal2024aquificaeovercomescompetition pages 1-2)
- **FabG** (3-oxoacyl-[ACP] reductase; suggested EC:1.1.1.100) (lehmann2023adaptivelaboratoryevolution pages 6-7)

**Repair / oxidative stress**
- **Methionine sulfoxide reductase** (EC:1.8.4.11 / EC:1.8.4.12 family-level) (mondal2024aquificaeovercomescompetition pages 1-2)

### 3.4 Chemicals / metabolites
- **Polyamines** (CHEBI:26195) (takemata2024howdothermophiles pages 4-5, lehmann2023adaptivelaboratoryevolution pages 1-2)
- **Plasmalogens** (CHEBI:35910) (lehmann2023adaptivelaboratoryevolution pages 6-7)

---

## 4) Evidence-backed causal edges (triples) suitable for curation

The following table focuses on mechanistic edges that can be curated into a TraitMech-style graph for **METPO:1000447**.

| Edge (S–P–O) | Mechanism class | Ontology grounding suggestions | Evidence snippet | Source (DOI, year, URL) | Curation notes |
|---|---|---|---|---|---|
| reverse gyrase **positively regulates** positive DNA supercoiling | DNA topology | reverse gyrase [label]; GO:0006265 DNA topological change | “reverse gyrase… introduces positive supercoils into DNA” and is a hallmark of many thermophiles (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Strong mechanistic edge; broad but especially supported in archaeal thermophiles. |
| positive DNA supercoiling **reduces** DNA melting at high temperature | DNA topology | GO:0006265 DNA topological change; label: DNA melting resistance | Reverse gyrase is “proposed to limit DNA melting” and prevent thermal denaturation (takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Strong but partly inferential at phenotype level; mechanism-to-biophysical state rather than direct growth assay. |
| reverse gyrase **contributes to** temperature optimum high | DNA topology | reverse gyrase [label]; METPO:1000447 | Presence of reverse gyrase is associated with organisms with optimal growth temperature “higher than 65°C”; loss/depletion causes temperature-correlated growth impairment (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Good candidate but should be marked uncertain for non-hyperthermophiles; association strongest above ~65°C, not all >40°C thermophiles. |
| elevated temperature **increases activity of** reverse gyrase TopR1 | Regulation/repair | reverse gyrase TopR1 [label] | In Sulfolobus, heat shock increases positive plasmid supercoiling “coincident with augmented TopR1 activity” (takemata2024howdothermophiles pages 1-2, baes2023transcriptionalandtranslational pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087; 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22 | Strong, but assay-specific to heat shock in Sulfolobus rather than baseline optimum determination. |
| nucleoid-associated proteins **increase** genome thermostability | Genome organization | GO:0006325 chromatin organization; label: nucleoid-associated protein (NAP) | “NAPs… affect 3D genome organization and enhance DNA thermostability”; abundance correlates with growth temperature (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Good curation candidate at generic NAP level; specific NAP family may vary by lineage. |
| archaeal histones **protect against** heat-induced DNA denaturation | Genome organization | GO:0000786 nucleosome; label: archaeal histone | Thermophilic archaea show elevated histone abundance that may “chromatinize and protect genomes against heat-induced denaturation” (takemata2024howdothermophiles pages 2-3, lehmann2023adaptivelaboratoryevolution pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087; 10.3389/fmicb.2023.1265216, 2023, https://doi.org/10.3389/fmicb.2023.1265216 | Strong for histone-containing archaea; not applicable to histone-lacking groups such as Sulfolobales. |
| histone-lacking Sulfolobales nucleoid-associated proteins **mediate** temperature-responsive DNA compaction | Genome organization | label: Sulfolobales NAPs; GO:0006325 | Sulfolobales “use… temperature-responsive changes in DNA organization and compaction induced by nucleoid-associated proteins” (baes2023transcriptionalandtranslational pages 1-2) | 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22 | Strong but clade-specific; best curated as Sulfolobales-specific or archaeal conditional mechanism. |
| canonical SMC proteins **organize** thermophile chromosome structure | Genome organization | GO:0000796 condensin complex; label: SMC protein | DNA loops in thermophiles can be “dependent on a canonical SMC protein”; SMC proteins contribute to higher-order chromosome organization (takemata2024howdothermophiles pages 4-5, takemata2024howdothermophiles pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087 | Moderate evidence for contribution to genome organization; link to optimum high is indirect. |
| polyamines **enhance** DNA thermostability | Genome organization | CHEBI:26195 polyamine | Polyamines are “ubiquitous and potentially relevant to genome thermostability”; earlier mechanistic framing notes positively charged polyamines protect DNA (takemata2024howdothermophiles pages 4-5, lehmann2023adaptivelaboratoryevolution pages 1-2) | 10.1264/jsme2.me23087, 2024, https://doi.org/10.1264/jsme2.me23087; 10.3389/fmicb.2023.1265216, 2023, https://doi.org/10.3389/fmicb.2023.1265216 | Reasonable candidate; direct causal assays to growth optimum are limited in these excerpts, so mark somewhat uncertain. |
| small heat shock proteins **prevent** heat-induced protein aggregation | Proteostasis | GO:0009408 response to heat; label: small heat shock protein | Small HSPs bind denaturing proteins and “protect them from aggregation” under heat stress (baes2023transcriptionalandtranslational pages 1-2, baes2023transcriptionalandtranslational pages 21-21) | 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22 | Strong mechanistic proteostasis edge; mostly archaeal examples here. |
| prefoldin **shuttles substrates to** thermosome | Proteostasis | label: prefoldin; label: thermosome/group II chaperonin | Prefoldin binds denaturing proteins and shuttles them to the HSP60-type group II chaperonin (thermosome) (baes2023transcriptionalandtranslational pages 1-2) | 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22 | Strong, taxon-rich archaeal evidence; direct cellular mechanism. |
| thermosome (group II chaperonin) **refolds** denatured proteins | Proteostasis | GO:0006457 protein folding; label: thermosome | Thermosome “refolds denatured proteins in an ATP-dependent manner” (baes2023transcriptionalandtranslational pages 1-2) | 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22 | Strong proteostasis edge; especially relevant in archaea. |
| chaperones/chaperonins (e.g., DnaK, GroEL) **support** survival at high temperature | Proteostasis | UniProt labels: DnaK, GroEL; GO:0006457 | Heat shock transcription “promotes… chaperones, such as DnaK and GroEL” and metagenomes from 85°C vent water are enriched in “heat shock proteins, molecular chaperones, and chaperonin complexes” (grunberger2023uncoveringthetemporal pages 1-2, mondal2024aquificaeovercomescompetition pages 1-2) | 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23; 10.1371/journal.pone.0310595, 2024, https://doi.org/10.1371/journal.pone.0310595 | Strong general heat-tolerance edge, but less specific to setting optimum versus coping with transient heat stress. |
| proteases / proteasome-associated quality control **removes** damaged proteins during heat stress | Proteostasis | GO:0006508 proteolysis; label: proteasome/ubiquitin-like modifier pathway | Heat shock systems include “proteases responsible for… degradation,” and archaeal ubiquitin-like modifier/proteasome pathways are implicated in protein quality control (grunberger2023uncoveringthetemporal pages 1-2, baes2023transcriptionalandtranslational pages 21-21) | 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23; 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22 | Moderate-to-strong; wording in one source is reference-list based, so use caution. |
| altered membrane lipid composition **stabilizes** cytoplasmic membrane at high temperature | Membrane | GO:0016042 lipid catabolic process [broad label not exact]; label: membrane lipid composition | Heat shock in S. acidocaldarius “leads to an altered lipid composition of the cytoplasmic membrane”; unique membrane composition is a recognized thermophile adaptation (baes2023transcriptionalandtranslational pages 1-2, grunberger2023uncoveringthetemporal pages 1-2) | 10.1128/mbio.03593-22, 2023, https://doi.org/10.1128/mbio.03593-22; 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23 | Strong general mechanism, but exact lipid species differ across bacteria vs archaea. |
| plasmalogen enrichment **contributes to** adaptation toward different temperature optimum | Membrane | CHEBI:35910 plasmalogen | Adapted T. kivui showed a “significantly increased proportion of plasmalogens” when optimum shifted downward from 66°C to 60°C (lehmann2023adaptivelaboratoryevolution pages 6-7) | 10.3389/fmicb.2023.1265216, 2023, https://doi.org/10.3389/fmicb.2023.1265216 | Important but directionality is tricky: evidence comes from adaptation away from higher optimum; do not curate as generic positive driver of thermophily without caution. |
| fatty acid desaturases **modulate** membrane adaptation under thermal stress | Membrane | EC:1.14.19.- fatty acid desaturase [family-level] | 85°C vent-water metagenome contains “fatty acid desaturases” among genes crucial for thermal adaptation (mondal2024aquificaeovercomescompetition pages 1-2) | 10.1371/journal.pone.0310595, 2024, https://doi.org/10.1371/journal.pone.0310595 | Weak-to-moderate; metagenomic association only, likely taxon- and context-specific. |
| fabG-mediated fatty acid composition change **affects** temperature adaptation | Membrane | gene: fabG; EC:1.1.1.100 3-oxoacyl-[acyl-carrier-protein] reductase | A fixed fabG mutation is highlighted as likely contributing to temperature-linked fatty acid composition changes (lehmann2023adaptivelaboratoryevolution pages 6-7) | 10.3389/fmicb.2023.1265216, 2023, https://doi.org/10.3389/fmicb.2023.1265216 | Useful candidate but strain-specific and inferred from evolution experiment; curate as uncertain. |
| methionine sulfoxide reductase **repairs** oxidatively damaged proteins during high-temperature stress | Regulation/repair | EC:1.8.4.11 methionine-S-sulfoxide reductase / EC:1.8.4.12 methionine-R-sulfoxide reductase | Vent-water metagenome includes “methionine sulfoxide reductases” among genes crucial for thermal adaptation (mondal2024aquificaeovercomescompetition pages 1-2) | 10.1371/journal.pone.0310595, 2024, https://doi.org/10.1371/journal.pone.0310595 | Moderate; metagenomic/ecological association, not direct perturbation evidence. |
| enrichment in hydrophobic and charged amino acids **increases** protein thermostability | Proteostasis | label: hydrophobic amino acid enrichment; label: charged amino acid enrichment; GO:0006457 protein folding | Thermophiles show “enrichment in hydrophobic and charged amino acids” and altered protein structure contributing to intrinsic thermostability (grunberger2023uncoveringthetemporal pages 1-2) | 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23 | Strong as a comparative molecular trend; not a single gene/module, so best curated as a compositional/mechanistic class. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating the microbial trait 'temperature optimum high' into a causal graph. It emphasizes DNA topology, genome organization, proteostasis, membrane remodeling, and repair mechanisms, with citations restricted to available context IDs.*

---

## 5) Recent developments (2023–2024) and expert analysis

### 5.1 Genome organization and reverse gyrase remain central (2024 synthesis)
A 2024 focused review frames thermophile genome stability as challenged by DNA helix denaturation and chemical damage and emphasizes **reverse gyrase** as a “most notable hallmark” of extreme thermophiles/hyperthermophiles, along with NAPs/histones/SMC proteins and polyamines as genome-organization determinants. (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3)

### 5.2 Systems-biology resolution of thermal stress responses in model hyperthermophiles (2023)
Multi-omics work in *Pyrococcus furiosus* describes broad thermal-stress regulatory remodeling and reiterates mechanistic classes (reverse gyrase, nucleoid proteins, membrane composition, proteostasis). (grunberger2023uncoveringthetemporal pages 1-2)

### 5.3 Mechanistic dissection of archaeal heat-shock proteostasis (2023)
In *Sulfolobus acidocaldarius* (TOPT ~75 °C), heat-shock triggers reduced transcription/translation but sustained neosynthesis, with chaperone systems (sHSP/prefoldin/thermosome) and DNA topology changes (TopR1-associated positive supercoiling) as key response elements; authors hypothesize temperature-responsive DNA organization/compaction as an ancient regulatory mechanism in histone-lacking archaea. (baes2023transcriptionalandtranslational pages 1-2)

### 5.4 Evolutionary plasticity of temperature optima (2023 ALE)
Adaptive laboratory evolution of the thermophile *Thermoanaerobacter kivui* under lower temperature selection resulted in a TOPT shift (66 °C → 60 °C) and implicated lipid remodeling (fatty acids, plasmalogens) and regulatory mutations (e.g., sigma factor-related) as candidate determinants. This is useful for causal-graph edges but should be curated with directionality caution (it is adaptation away from higher optimum). (lehmann2023adaptivelaboratoryevolution pages 6-7)

---

## 6) Current applications and real-world implementations (with recent quantitative data)

### 6.1 Thermophilic cyanobacteria as biotechnology chassis (2024)
A 2024 review defines thermophilic cyanobacteria as capable of growth **45–73 °C** and highlights them as hot-spring primary producers and potential “microbial cell factories,” emphasizing stable photosystems/light-harvesting components and bioproduct potential; it also reports strain-level growth temperatures commonly in the **~50–65 °C** range (table evidence). (rasul2024thermophiliccyanobacteria—excitingyet pages 1-3, rasul2024thermophiliccyanobacteria—excitingyet pages 3-4)

### 6.2 Industrial enzymes from thermophiles: α-amylases (2024 systematic review)
Thermophilic microbial α-amylases are positioned as industrially important, with thermophiles described as thriving/surviving **~41–122 °C**, and α-amylase operating optima often **45–90 °C** (with examples in the review’s table, e.g., some Bacillus/Geobacillus and fungal sources). Applications include food processing, textile finishing, paper, and detergents. (arfah2024systematicreviewon pages 1-3, arfah2024systematicreviewon pages 3-5)

### 6.3 Thermophiles in industrial bioprocesses: biohydrogen and biodegradation (2024)
A 2024 review summarizes thermophile-enabled process metrics including: 
- Maximum H2 yield **760 mL/L at 60 °C** from untreated cassava pulp in one cited thermophilic fermentation context, and a reported **~28.3%** H2-yield boost with nickel ferrite nanoparticles. (gallo2024theundeniablepotential pages 4-5)
- *Caldicellulosiruptor saccharolyticus* sugar-to-H2 yields **2.9–3.4 mol H2/mol hexose** (≈74–85% theoretical). (gallo2024theundeniablepotential pages 4-5)
- Thermophilic anaerobic biodegradation showing **53.0–95.7% biodegradability** across plastics, and thermophilic co-digestion reducing methane-production lag by **1–4 days** with **9.11–11.2%** increased conversion. (gallo2024theundeniablepotential pages 4-5)

---

## 7) Warnings / non-curation guidance (claims needing caution)

1. **Heat-shock response ≠ growth optimum:** Many mechanistic claims come from heat-shock/temperature-shift experiments and may represent **stress survival** rather than determinants of TOPT. Consider modelling these edges as contributing to “high-temperature growth tolerance” rather than directly to TOPT unless the study links to growth curves/optima. (grunberger2023uncoveringthetemporal pages 1-2, baes2023transcriptionalandtranslational pages 1-2)
2. **Reverse gyrase is not universal in all thermophiles:** Reverse gyrase is most strongly associated with organisms with **higher optima (e.g., >65 °C)** and is described as a hallmark of extreme thermophiles/hyperthermophiles; it should likely be curated with a conditional scope note. (takemata2024howdothermophiles pages 1-2)
3. **Directionality pitfalls in lipid remodeling:** In the ALE study, increased plasmalogens were associated with adaptation to lower TOPT (66→60 °C). Do not curate “plasmalogens increase → higher TOPT” without additional evidence. (lehmann2023adaptivelaboratoryevolution pages 6-7)
4. **Metagenomic presence is associative:** Genes found in hot-spring metagenomes (e.g., fatty acid desaturases, methionine sulfoxide reductases) support plausibility but are not perturbation evidence; mark such edges as “inferred/uncertain.” (mondal2024aquificaeovercomescompetition pages 1-2)

---

## DOI-first bibliography (with publication dates and URLs)

1. **Takemata N.** (2024-06). *How Do Thermophiles Organize Their Genomes?* Microbes and Environments. DOI: **10.1264/jsme2.me23087**. URL: https://doi.org/10.1264/jsme2.me23087 (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3, takemata2024howdothermophiles pages 4-5)
2. **Grünberger F. et al.** (2023-12). *Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.* mBio. DOI: **10.1128/mbio.02174-23**. URL: https://doi.org/10.1128/mbio.02174-23 (grunberger2023uncoveringthetemporal pages 1-2)
3. **Baes R. et al.** (2023-10). *Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon Sulfolobus acidocaldarius.* mBio. DOI: **10.1128/mbio.03593-22**. URL: https://doi.org/10.1128/mbio.03593-22 (baes2023transcriptionalandtranslational pages 1-2, baes2023transcriptionalandtranslational pages 21-21)
4. **Lehmann M. et al.** (2023-10). *Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum.* Frontiers in Microbiology. DOI: **10.3389/fmicb.2023.1265216**. URL: https://doi.org/10.3389/fmicb.2023.1265216 (lehmann2023adaptivelaboratoryevolution pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7)
5. **Mondal N. et al.** (2024-10). *Aquificae overcomes competition… to dominate the boiling vent-water of a Trans-Himalayan sulfur-borax spring.* PLOS ONE. DOI: **10.1371/journal.pone.0310595**. URL: https://doi.org/10.1371/journal.pone.0310595 (mondal2024aquificaeovercomescompetition pages 1-2)
6. **Rasul F. et al.** (2024-03). *Thermophilic cyanobacteria—exciting, yet challenging biotechnological chassis.* Applied Microbiology and Biotechnology. DOI: **10.1007/s00253-024-13082-w**. URL: https://doi.org/10.1007/s00253-024-13082-w (rasul2024thermophiliccyanobacteria—excitingyet pages 1-3, rasul2024thermophiliccyanobacteria—excitingyet pages 3-4)
7. **Arfah R.A. et al.** (2024-09). *Systematic review on isolation, purification, characterization, and industrial applications of thermophilic microbial α-amylases.* Karbala International Journal of Modern Science. DOI: **10.33640/2405-609x.3367**. URL: https://doi.org/10.33640/2405-609x.3367 (arfah2024systematicreviewon pages 1-3, arfah2024systematicreviewon pages 3-5)
8. **Gallo G. et al.** (2024-07). *The Undeniable Potential of Thermophiles in Industrial Processes.* International Journal of Molecular Sciences. DOI: **10.3390/ijms25147685**. URL: https://doi.org/10.3390/ijms25147685 (gallo2024theundeniablepotential pages 4-5, gallo2024theundeniablepotential pages 8-9, gallo2024theundeniablepotential pages 11-12)

---

## Notes for YAML curation into `data/traits/environment/temperature_optimum_high.yaml`
- Use METPO:1000447 as the trait node; consider adding a **definition note** capturing the common alternative thermophile cutoff (>45 °C) and subcategories (extreme/hyper). (lehmann2023adaptivelaboratoryevolution pages 1-2, arfah2024systematicreviewon pages 3-5)
- Consider organizing mechanistic subgraphs as modules:
  - **DNA topology/genome module:** reverse gyrase → positive supercoiling → reduced DNA melting/repair capacity (takemata2024howdothermophiles pages 1-2, takemata2024howdothermophiles pages 2-3)
  - **Genome organization module:** NAPs/histones/SMC/polyamines → genome compaction/thermostability (takemata2024howdothermophiles pages 2-3, takemata2024howdothermophiles pages 4-5)
  - **Proteostasis module:** sHSP/prefoldin/thermosome/proteases → reduced aggregation/functional proteome (baes2023transcriptionalandtranslational pages 1-2, grunberger2023uncoveringthetemporal pages 1-2)
  - **Membrane module:** lipid composition remodeling / desaturases / fatty acid biosynthesis → membrane functional stability (baes2023transcriptionalandtranslational pages 1-2, mondal2024aquificaeovercomescompetition pages 1-2, lehmann2023adaptivelaboratoryevolution pages 6-7)


References

1. (lehmann2023adaptivelaboratoryevolution pages 1-2): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

2. (arfah2024systematicreviewon pages 3-5): Rugaiyah A. Arfah, Sarlan Sarlan, Abdul Karim, Anita Anita, Ahyar Ahmad, Paulina Taba, Harningsih Karim, Siti Halimah Larekeng, Dorothea Agnes Rampisela, and Rusdina Bte Ladju. Systematic review on isolation, purification, characterization, and industrial applications of thermophilic microbial α- amylases. Sep 2024. URL: https://doi.org/10.33640/2405-609x.3367, doi:10.33640/2405-609x.3367. This article has 5 citations.

3. (grunberger2023uncoveringthetemporal pages 1-2): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

4. (baes2023transcriptionalandtranslational pages 1-2): Rani Baes, Felix Grünberger, Sébastien Pyr dit Ruys, Mohea Couturier, Sarah De Keulenaer, Sonja Skevin, Filip Van Nieuwerburgh, Didier Vertommen, Dina Grohmann, Sébastien Ferreira-Cerca, and Eveline Peeters. Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon <i>sulfolobus acidocaldarius</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.03593-22, doi:10.1128/mbio.03593-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

5. (takemata2024howdothermophiles pages 1-2): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

6. (takemata2024howdothermophiles pages 2-3): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

7. (takemata2024howdothermophiles pages 4-5): Naomichi Takemata. How do thermophiles organize their genomes? Microbes and Environments, 39:n/a, Jun 2024. URL: https://doi.org/10.1264/jsme2.me23087, doi:10.1264/jsme2.me23087. This article has 6 citations and is from a peer-reviewed journal.

8. (lehmann2023adaptivelaboratoryevolution pages 6-7): Maria Lehmann, Christoph Prohaska, Benjamin Zeldes, Anja Poehlein, Rolf Daniel, and Mirko Basen. Adaptive laboratory evolution of a thermophile toward a reduced growth temperature optimum. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1265216, doi:10.3389/fmicb.2023.1265216. This article has 18 citations and is from a peer-reviewed journal.

9. (mondal2024aquificaeovercomescompetition pages 1-2): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

10. (baes2023transcriptionalandtranslational pages 21-21): Rani Baes, Felix Grünberger, Sébastien Pyr dit Ruys, Mohea Couturier, Sarah De Keulenaer, Sonja Skevin, Filip Van Nieuwerburgh, Didier Vertommen, Dina Grohmann, Sébastien Ferreira-Cerca, and Eveline Peeters. Transcriptional and translational dynamics underlying heat shock response in the thermophilic crenarchaeon <i>sulfolobus acidocaldarius</i>. Oct 2023. URL: https://doi.org/10.1128/mbio.03593-22, doi:10.1128/mbio.03593-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (rasul2024thermophiliccyanobacteria—excitingyet pages 1-3): Faiz Rasul, Dawei You, Ying Jiang, Xiangjian Liu, and Maurycy Daroch. Thermophilic cyanobacteria—exciting, yet challenging biotechnological chassis. Applied Microbiology and Biotechnology, Mar 2024. URL: https://doi.org/10.1007/s00253-024-13082-w, doi:10.1007/s00253-024-13082-w. This article has 16 citations and is from a domain leading peer-reviewed journal.

12. (rasul2024thermophiliccyanobacteria—excitingyet pages 3-4): Faiz Rasul, Dawei You, Ying Jiang, Xiangjian Liu, and Maurycy Daroch. Thermophilic cyanobacteria—exciting, yet challenging biotechnological chassis. Applied Microbiology and Biotechnology, Mar 2024. URL: https://doi.org/10.1007/s00253-024-13082-w, doi:10.1007/s00253-024-13082-w. This article has 16 citations and is from a domain leading peer-reviewed journal.

13. (arfah2024systematicreviewon pages 1-3): Rugaiyah A. Arfah, Sarlan Sarlan, Abdul Karim, Anita Anita, Ahyar Ahmad, Paulina Taba, Harningsih Karim, Siti Halimah Larekeng, Dorothea Agnes Rampisela, and Rusdina Bte Ladju. Systematic review on isolation, purification, characterization, and industrial applications of thermophilic microbial α- amylases. Sep 2024. URL: https://doi.org/10.33640/2405-609x.3367, doi:10.33640/2405-609x.3367. This article has 5 citations.

14. (gallo2024theundeniablepotential pages 4-5): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

15. (gallo2024theundeniablepotential pages 8-9): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.

16. (gallo2024theundeniablepotential pages 11-12): Giovanni Gallo, Paola Imbimbo, and Martina Aulitto. The undeniable potential of thermophiles in industrial processes. International Journal of Molecular Sciences, 25:7685, Jul 2024. URL: https://doi.org/10.3390/ijms25147685, doi:10.3390/ijms25147685. This article has 21 citations.