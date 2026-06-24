---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:33:27.391554'
end_time: '2026-06-17T23:02:25.164795'
duration_seconds: 1737.77
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: halophily preference
  trait_identifier: METPO:1000629
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: halophily_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that is relating to an organism's salt concentration requirements
    or tolerance for growth.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.halophily.halophily level, range_salinity
  evidence_summary: 'DOI:10.1093/femsre/fuy009: life at high salt concentrations (Supports
    salinity and salt concentration as a growth-relevant microbial trait axis.)'
  causal_graph_summary: 'halophily_preference_osmoadaptation: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** halophily preference
- **METPO identifier:** METPO:1000629
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's salt concentration requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.halophily.halophily level, range_salinity
- **Existing evidence:** DOI:10.1093/femsre/fuy009: life at high salt concentrations (Supports salinity and salt concentration as a growth-relevant microbial trait axis.)
- **Existing causal graph summary:** halophily_preference_osmoadaptation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **halophily preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halophily_preference.yaml`.

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
- **Trait label:** halophily preference
- **METPO identifier:** METPO:1000629
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's salt concentration requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.halophily.halophily level, range_salinity
- **Existing evidence:** DOI:10.1093/femsre/fuy009: life at high salt concentrations (Supports salinity and salt concentration as a growth-relevant microbial trait axis.)
- **Existing causal graph summary:** halophily_preference_osmoadaptation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **halophily preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halophily_preference.yaml`.

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


## Curation-focused research report: Microbial trait “halophily preference” (METPO:1000629)

### 1) Scope summary (TraitMech-ready)
**Trait definition (curation scope):** *Halophily preference* is a microbial phenotype describing an organism’s **salt concentration requirement/tolerance for growth**, commonly operationalized as a **growth response curve vs salinity** (growth/no growth, optimum, tolerance range), and can be expressed in NaCl molarity, % (w/v), or total dissolved salts (g/L). Haloarchaea are described as mostly obligate halophiles with **optimal growth at 10–35% NaCl (1.71–6 M)**, directly tying “preference” to measurable growth optima (10.3390/microorganisms12081738; published 2024-08-22) (bonnaud2024haloarchaeaaspromising pages 1-2). A recent authoritative review defines *hypersaline* as **>100–150 g/L salts** and *halophiles* as organisms **growing at >100–150 g/L dissolved salts**, providing a practical boundary for “halophily” in environmental surveys and cultivation criteria (10.1038/s44185-024-00050-w; published 2024-08) (oren2024novelinsightsinto pages 1-2).

**Boundary cases / nearby traits:**
- *Halotolerance vs halophily:* Halophily preference implies **growth at high salt** and often a measurable optimum; halotolerance may indicate survival or growth across a broad range with lower optima, often leaning on **salt-out (compatible solute)** strategies. Haloarchaea and extreme halophiles frequently rely on **salt-in**; many bacteria rely on **salt-out**, and hybrid strategies occur (bonnaud2024haloarchaeaaspromising pages 2-4, ionescu2024extremefluctuationsin pages 1-2).
- *Osmotic stress response vs halophily preference:* acute shock responses (minutes–hours) (e.g., NaCl shock) characterize **stress physiology**; trait preference is better curated from **steady-state growth ranges/optima**, but shock assays provide mechanistic edges connecting salinity to osmoregulatory modules (yu2024temporaldynamicsof pages 1-2).
- *Ionic composition matters:* “Salinity” is not only NaCl; chaotropic ions (e.g., MgCl2) can set different physiological limits (review context), so the trait node should permit salt identity/composition where known (oren2024novelinsightsinto pages 4-5).

### 2) Key concepts and current mechanistic understanding (salt-in vs salt-out)
Microbial halophily preference is largely determined by **osmoadaptation strategy choice**:
- **Salt-in strategy:** intracellular accumulation of **molar K+ and Cl−** to balance external osmotic potential (bonnaud2024haloarchaeaaspromising pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4). This requires extensive adaptation of cellular components; organisms using salt-in typically exhibit an **acidified proteome**, and acidic residues are described as important for **protein solubility** at high salt (bonnaud2024haloarchaeaaspromising pages 2-4).
- **Salt-out strategy:** **Na+ exclusion** plus accumulation of **organic compatible solutes** (e.g., ectoine, glycine betaine, trehalose, amino acids/derivatives) to raise cytoplasmic osmolarity without high cytoplasmic salinity (bonnaud2024haloarchaeaaspromising pages 2-4).
- **Hybrid strategies:** Some halophiles can deploy both (e.g., concurrent compatible-solute accumulation and ion accumulation), which is important for curation because halophily preference may emerge from a **composite** of modules rather than one canonical mechanism. A 2024 AEM study reports that *Natranaerobius thermophilus* uses a hybrid long-term mechanism combining “compatible solute” and “salt-in” strategies, supported by protein/mRNA changes and measurements of intracellular solutes/ions across salinities (10.1128/aem.00145-24; 2024-05) (xing2024thepolyextremophilenatranaerobius pages 14-17).

### 3) Candidate nodes for a TraitMech causal graph
A curation-ready node inventory with candidate ontology groundings is provided here:

| Node label | Node type | Suggested ontology grounding | Evidence/supporting source(s) (short) | Context IDs |
|---|---|---|---|---|
| salinity / NaCl concentration | environmental factor | CHEBI:26710 | Growth and stress responses measured across NaCl gradients and salt shocks; haloarchaeal optima 10–35% NaCl; halophiles operationally defined by growth at >100–150 g/L salts | (bonnaud2024haloarchaeaaspromising pages 1-2, yu2024temporaldynamicsof pages 1-2, oren2024novelinsightsinto pages 1-2, shu2023metabolicengineeringof pages 3-4) |
| osmotic stress | cellular property | GO:0006970 | NaCl shock induces osmotic stress; central immediate consequence of increased salinity | (yu2024temporaldynamicsof pages 1-2) |
| oxidative stress (ROS) | cellular property | GO:0006979 | NaCl shock also induced oxidative stress; peroxidase/catalase defenses and cysB response reported | (yu2024temporaldynamicsof pages 1-2) |
| compatible solute | cellular property | GO:0010288 | Reviews and experiments describe compatible-solute accumulation as core salt-out response | (bonnaud2024haloarchaeaaspromising pages 2-4, yu2024temporaldynamicsof pages 1-2) |
| salt-in strategy | cellular property |  | Accumulation of molar K+ and Cl− in cytoplasm as major osmoadaptation mode in extreme halophiles | (bonnaud2024haloarchaeaaspromising pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4) |
| salt-out strategy | cellular property |  | Na+ exclusion plus accumulation/synthesis of organic osmolytes; common in halotolerant and some haloarchaea | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| Na+/H+ antiporter | transporter/complex | GO:0015385 | Broad review support for Na+ expulsion via Na+/H+ antiporters under both strategies | (bonnaud2024haloarchaeaaspromising pages 2-4, bonnaud2024haloarchaeaaspromising pages 1-2) |
| K+ uptake / K+ uniport | transporter/complex | GO:0015079 | Immediate K+ import during acute osmotic stress; K+ uptake central to salt-in and early shock responses | (bonnaud2024haloarchaeaaspromising pages 2-4, yu2024temporaldynamicsof pages 1-2) |
| Cl-/Na+ symport | transporter/complex | GO:0015370 | Review support for Cl− uptake through Cl−/Na+ symport in salt-in adaptation | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| halorhodopsin | gene/protein |  | Light-driven primary Cl− pump used for cytoplasmic Cl− uptake in haloarchaea | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| bacteriorhodopsin | gene/protein |  | Light-driven proton pump contributing to proton motive force in salt-in systems | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| ATP synthase | transporter/complex | GO:0015986 | Proton gradient supports ATP synthase; ATP supply implicated in osmoadaptation and energy crisis under shock | (bonnaud2024haloarchaeaaspromising pages 2-4, yu2024temporaldynamicsof pages 1-2) |
| mechanosensitive channels (Msc) | transporter/complex | GO:0015250 | Safety valves enabling rapid release of ions and organic solutes upon osmotic downshock | (bonnaud2024haloarchaeaaspromising pages 2-4, thompson2024themicrobiomeof pages 5-6) |
| ABC transporter OpuA | transporter/complex |  | Glycine betaine uptake transporter induced or detected under salt stress; OpuAC copies upregulated in N. thermophilus | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| ABC transporter OpuB | transporter/complex |  | Choline/glycine-betaine-related uptake system; OpuBA mildly upregulated at high salinity | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| ABC transporter ProU (proVWX/ProX) | transporter/complex |  | Osmoprotectant uptake system detected in N. thermophilus; mixed salinity regulation reported | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| BCCT transporter BetT / OpuD | transporter/complex |  | BCCT family carriers for glycine betaine/related osmolytes; detected in N. thermophilus and broadly in halophiles | (xing2024thepolyextremophilenatranaerobius pages 14-17, bonnaud2024haloarchaeaaspromising pages 2-4) |
| Na+/proline symporter PutP | transporter/complex |  | PutP detected in N. thermophilus and discussed with proline accumulation under salt stress | (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| ectABC operon | pathway | MetaCyc:PWY-7315 | Canonical ectoine biosynthesis module; expression enhanced under salt stress and central to Halomonas production strains | (chen2024elucidatingthesalttolerant pages 1-2, lichty2024compatiblesolutesare pages 19-23, thompson2024themicrobiomeof pages 5-6) |
| ectD | gene/protein | EC:1.14.11.55 | Converts ectoine to 5-hydroxyectoine; included in ectoine/hydroxyectoine node set | (lichty2024compatiblesolutesare pages 19-23, thompson2024themicrobiomeof pages 5-6) |
| gsmt | gene/protein | EC:2.1.1.- | Glycine sarcosine N-methyltransferase gene in glycine methylation pathway; upregulated at higher salinity | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| sdmt | gene/protein | EC:2.1.1.- | Sarcosine dimethylglycine N-methyltransferase gene; upregulated at higher salinity | (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| betA / betB | pathway |  | Choline oxidation pathway genes for glycine betaine synthesis; common bacterial salt-out route | (lichty2024compatiblesolutesare pages 19-23, thompson2024themicrobiomeof pages 5-6) |
| gbsAB | pathway |  | Glycine betaine biosynthesis genes cited in halophile osmoadaptation literature | (xing2024thepolyextremophilenatranaerobius pages 24-25) |
| ectoine | metabolite/ion | CHEBI:27856 | Main compatible solute in Halomonas elongata and many halophilic bacteria; industrial product with salt-responsive accumulation | (yu2024temporaldynamicsof pages 1-2, chen2024elucidatingthesalttolerant pages 1-2, lichty2024compatiblesolutesare pages 19-23) |
| 5-hydroxyectoine | metabolite/ion | CHEBI:60300 | Hydroxylated ectoine derivative produced via EctD; part of compatible-solute repertoire | (lichty2024compatiblesolutesare pages 19-23, thompson2024themicrobiomeof pages 5-6) |
| glycine betaine | metabolite/ion | CHEBI:17750 | Major compatible solute; imported and/or synthesized; intracellular concentration increases with salinity in N. thermophilus | (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| trehalose | metabolite/ion | CHEBI:16551 | Compatible solute found in many halophiles including haloarchaea and bacteria | (bonnaud2024haloarchaeaaspromising pages 2-4, thompson2024themicrobiomeof pages 5-6, xing2024thepolyextremophilenatranaerobius pages 24-25) |
| glutamate | metabolite/ion | CHEBI:29991 | Rapidly increased under salt shock; secondary compatible solute in N. thermophilus and H. elongata | (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| glutamine | metabolite/ion | CHEBI:28300 | Amino-acid pool increased under NaCl shock; compatible-solute-related role in hybrid adaptation | (yu2024temporaldynamicsof pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| proline | metabolite/ion | CHEBI:26271 | Compatible solute/precursor increased under salt stress; linked to PutP transporter | (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| potassium ion (K+) | metabolite/ion | CHEBI:29103 | Principal cation in salt-in strategy and rapid osmotic-shock response | (bonnaud2024haloarchaeaaspromising pages 2-4, yu2024temporaldynamicsof pages 1-2) |
| chloride ion (Cl-) | metabolite/ion | CHEBI:17996 | Principal anion in salt-in strategy; intracellular Cl− tracks external Cl− in hybrid systems | (bonnaud2024haloarchaeaaspromising pages 2-4, xing2024thepolyextremophilenatranaerobius pages 10-14) |
| sodium ion (Na+) | metabolite/ion | CHEBI:29101 | External osmotic driver; taken up transiently in some shock responses but generally expelled from cytoplasm | (bonnaud2024haloarchaeaaspromising pages 2-4, yu2024temporaldynamicsof pages 1-2) |
| acidified proteome / increased surface acidic residues | cellular property |  | Hallmark of salt-in extreme halophiles; associated with acidic amino-acid enrichment on protein surfaces | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| protein solubility in high salt | cellular property | GO:0006457 | Acidic surfaces and hydrated cation network help keep halophilic proteins soluble in hypersaline environments | (bonnaud2024haloarchaeaaspromising pages 2-4) |
| energy metabolism upregulation (TCA, glycolysis, ED) | pathway | KEGG:map00020; KEGG:map00010; KEGG:map00030 | Salt stress enriches carbon metabolism, TCA, glycolysis; H. elongata relies on ED pathway; interpreted as ATP-supporting | (xing2024thepolyextremophilenatranaerobius pages 10-14, yu2024temporaldynamicsof pages 1-2, shu2023metabolicengineeringof pages 6-10) |
| assay: growth at >100–150 g/L dissolved salts | assay factor |  | Oren 2024 operational definition of halophiles for scope and curation boundary | (oren2024novelinsightsinto pages 1-2) |
| assay: NaCl shock (1–13%) | assay factor |  | Recent H. elongata study uses defined shock range to map tolerance and mechanistic phases | (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5) |
| assay: intracellular compatible-solute / ion quantification | assay factor |  | HPLC, metabolomics, proteomics, transcriptomics, ddPCR used to operationalize mechanisms and salinity responses | (xing2024thepolyextremophilenatranaerobius pages 14-17, shu2023metabolicengineeringof pages 3-4) |


*Table: This table lists curation-ready candidate nodes for a microbial halophily preference causal graph, with suggested grounding and concise evidence. It is useful for translating recent halophily and osmoadaptation literature into TraitMech node inventories.*

### 4) Evidence-backed candidate causal edges (triples)
A curation table of candidate causal edges (subject–predicate–object), with verbatim evidence snippets, DOI-first references, and uncertainty notes is provided here:

| Edge (triple) | Edge type | Evidence snippet (verbatim from sources) | Reference (DOI, year, URL) | Context ID | Notes/uncertainty |
|---|---|---|---|---|---|
| high external NaCl/salinity → causes → osmotic stress | environmental | “NaCl shock induced two major stresses, namely osmotic stress and oxidative stress.” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | pqac-00000030 | Experimental; H. elongata NaCl-shock study. |
| osmotic stress → induces → Na+/H+ antiporter-mediated Na+ expulsion | molecular | “Whatever the strategy, sodium ions are expelled from the cytoplasm... and this is usually performed with the help of Na+/H+ antiporters.” (bonnaud2024haloarchaeaaspromising pages 1-2) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000029 | Review-based, broad across haloarchaea; good generic mechanism but not taxon-specific experiment. |
| proton electrochemical gradient → drives → Na+/H+ antiporter activity | molecular | “sodium is excluded from the cytoplasm with the help of an Na+/H+ antiporter that uses the electrochemical proton gradient as a driving force” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; mechanistic but not directly growth assay-linked. |
| acute osmotic stress → induces → K+ uptake | cellular | “It starts with an immediate adjustment response, consisting of the cellular import of K+ (acute osmotic stress).” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; suitable as generic edge for acute response. |
| NaCl shock (1–8%) → increases → intracellular Na+ and K+ uptake | experimental | “within the cell’s tolerable range (1–8% NaCl shock), H. elongata urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | pqac-00000030 | Experimental; species-specific to H. elongata. |
| salt-in strategy → results in → K+ accumulation | cellular | “the accumulation of a molar concentration of K+ and Cl−(salt-in strategy)” (bonnaud2024haloarchaeaaspromising pages 1-2) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000029 | Review-level edge; broadly accepted. |
| salt-in strategy → results in → Cl− accumulation | cellular | “the accumulation of a molar concentration of K+ and Cl−(salt-in strategy)” (bonnaud2024haloarchaeaaspromising pages 1-2) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000029 | Review-level edge; broadly accepted. |
| halorhodopsin / Cl−/Na+ symport → mediates → Cl− uptake into cytoplasm | molecular | “Cl−is transported into the cytoplasm with the help of primary or secondary transporters (halorhodopsin, light-driven chloride pump in purple and symporter in blue)” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; transporter names grounded, but not a single-gene experimental validation here. |
| salt-out strategy → results in → compatible solute accumulation | cellular | “The salt-out strategy consists of the exclusion of sodium from the cytoplasm and the accumulation of a high concentration of organic solutes” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; generic across halophiles. |
| high salinity → upregulates → gsmt | molecular | “the proteins GSMT and SDMT exhibited a significant upregulation of 2.1- and 3.16-fold, respectively. The mRNA levels of genes gsmt and sdmt were also upregulated 1.56- and 3.36-fold” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000027 | Experimental; specific to N. thermophilus and glycine methylation pathway. |
| high salinity → upregulates → sdmt | molecular | “the proteins GSMT and SDMT exhibited a significant upregulation of 2.1- and 3.16-fold, respectively. The mRNA levels of genes gsmt and sdmt were also upregulated 1.56- and 3.36-fold” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000027 | Experimental; specific to N. thermophilus. |
| gsmt/sdmt-mediated glycine methylation pathway → contributes to → de novo glycine betaine biosynthesis | molecular | “This suggests that the de novo biosynthesis of glycine betaine could have a significant impact on the ability of N. thermophilus to adapt to high salinity.” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000027 | Experimental but still somewhat inferential (“could have”); curate as uncertain. |
| high salinity → induces → OpuA/OpuB/ProU glycine betaine transport systems | molecular | “Among these OpuAC proteins, only one OpuAC (Nther_0728) was upregulated at three different concentrations of salt... The OpuBA protein was slightly upregulated (1.36-fold) at 4.3 M Na+” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000027 | Experimental; transporter regulation is mixed by component, so edge should be component-aware. |
| glycine betaine uptake transporters (OpuA/OpuB/OpuC/OpuD/ProU) → mediate → environmental glycine betaine uptake | molecular | “Glycine betaine uptake from the environment occurs via transporters OpuA, OpuC, OpuD, and ProU, and its precursor choline is imported via OpuB and OpuC” (xing2024thepolyextremophilenatranaerobius pages 14-17) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000027 | Literature-backed in discussion; partially review/transfer from other taxa. |
| salinity increase → increases → intracellular glycine betaine concentration | experimental | “glycine betaine is reported as the main imported osmoprotectant with intracellular concentrations rising from ~53 to 893 mM across 2.5–4.3 M Na+.” (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000041 | Experimental summary; strong quantitative support in N. thermophilus. |
| NaCl shock → increases → intracellular glutamate and glutamine pools | experimental | “within the cell’s tolerable range (1–8% NaCl shock), H. elongata urgently balanced the surging osmotic pressure by... augmenting intracellular amino acid pools, particularly glutamate and glutamine.” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | pqac-00000030 | Experimental; directly relevant for compatible-solute precursor response. |
| salinity increase → increases → intracellular glutamate | experimental | “increased glutamate levels (11.0 to 221.3 mM) at higher salinities, indicating glutamate as a secondary compatible solute.” (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000041 | Experimental; taxon-specific to N. thermophilus. |
| salinity increase → increases → intracellular proline | experimental | “The Na+/proline symporter PutP is present and discussed alongside proline accumulation dynamics (67.0–130 mM).” (xing2024thepolyextremophilenatranaerobius pages 17-19) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000041 | Experimental summary; PutP function vs accumulation may need more direct evidence. |
| salt stress → enriches/upregulates → ABC transporter pathway | molecular | “the pathway of ABC transporters (nth02010) was significantly enriched in the 3.7 M Na+ compared to the 2.5 M Na+” (xing2024thepolyextremophilenatranaerobius pages 10-14) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000026 | Experimental proteomics/transcript validation in N. thermophilus. |
| salt stress → upregulates → amino-acid metabolism and energy metabolism pathways | cellular | “These regulatory mechanisms facilitate enhanced ATP production and amino acid metabolism” (xing2024thepolyextremophilenatranaerobius pages 10-14) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000026 | Experimental but pathway-to-ATP wording is interpretive. |
| upregulated carbon/TCA/glycolysis pathways → supports → ATP supply under high salt | cellular | “These regulations may contribute to increased ATP production within the N. thermophilus, providing sufficient energy to sustain normal cellular functions.” (xing2024thepolyextremophilenatranaerobius pages 10-14) | 10.1128/aem.00145-24, 2024, https://doi.org/10.1128/aem.00145-24 | pqac-00000026 | Experimental enrichment with author interpretation. |
| salt stress → enhances → ectoine biosynthesis module expression | molecular | “Transcriptome analysis indicated that expression of ectoine biosynthesis module was enhanced under salt stress.” (chen2024elucidatingthesalttolerant pages 1-2) | 10.1186/s12934-024-02515-w, 2024, https://doi.org/10.1186/s12934-024-02515-w | pqac-00000032 | Experimental; H. cupida J9. |
| NaCl shock → increases → ectoine accumulation | experimental | “ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | pqac-00000030 | Experimental; H. elongata. |
| ectoine accumulation → associated with → high ectoine productivity under salt shock | experimental | “reaching the maximum productivity (1450 ± 99 mg/L/h)” (yu2024temporaldynamicsof pages 1-2) | 10.1186/s12934-024-02358-5, 2024, https://doi.org/10.1186/s12934-024-02358-5 | pqac-00000030 | Experimental; productivity is process phenotype, not direct mechanism. |
| high salinity → favors → acidified proteome / increased acidic residues | molecular | “microorganisms employing this strategy... exhibit an acidified proteome... The acidification of the proteome would be essential for protein solubility under such environmental conditions” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; good generic edge for extreme halophiles. |
| increased surface acidic residues → promotes → protein solubility in hypersaline environments | molecular | “The high number of negative charges on the surface coordinates a network of hydrated cations and keeps the protein in solution.” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; mechanistic explanation rather than direct gene-level evidence. |
| osmotic downshock → activates → mechanosensitive channels (Msc) | cellular | “Msc channels (mechanosensitive channels, which serve as safety valves, allowing the rapid release of ions and organic solutes in the case of sudden downward osmotic shocks)” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; broad applicability across halophiles. |
| mechanosensitive channels → mediate → rapid solute efflux | cellular | “allowing the rapid release of ions and organic solutes in the case of sudden downward osmotic shocks” (bonnaud2024haloarchaeaaspromising pages 2-4) | 10.3390/microorganisms12081738, 2024, https://doi.org/10.3390/microorganisms12081738 | pqac-00000028 | Review; useful but not specific to one transporter family member. |
| hom knockout → decreases → betaine synthesis | experimental | “Betaine fermentation experiments revealed that betaine synthesis by the gene-deficient strain decreased under saline culture conditions” (shu2023metabolicengineeringof pages 6-10) | 10.1038/s41598-023-36975-8, 2023, https://doi.org/10.1038/s41598-023-36975-8 | pqac-00000033 | Experimental; H. campaniensis XH26/Δhom. |
| decreased betaine concentration → associated with → improved ectoine production | experimental | “Therefore, knocking out hom may also improve ectoine production by reducing betaine concentrations.” (shu2023metabolicengineeringof pages 6-10) | 10.1038/s41598-023-36975-8, 2023, https://doi.org/10.1038/s41598-023-36975-8 | pqac-00000033 | Author inference from knockout data; curate as uncertain causal mediation. |
| hom knockout → increases → ectoine yield | experimental | “ectoine yields was 351.13 mg (g CDW)−1 at a salinity of 1.5 mol NaCl L−1, much higher than the 239.18 mg (g CDW)−1 of the wild-type strain.” (shu2023metabolicengineeringof pages 6-10) | 10.1038/s41598-023-36975-8, 2023, https://doi.org/10.1038/s41598-023-36975-8 | pqac-00000033 | Strong experimental edge in engineered Halomonas; engineering-specific, not native trait mechanism. |


*Table: This table lists candidate causal edges for halophily preference and osmoadaptation, with verbatim evidence snippets, DOI-first references, and curation notes. It is designed to help prioritize TraitMech-ready relationships and flag review-based or taxon-specific claims.*

### 5) Recent developments and latest research (2023–2024 prioritized)
**(i) Hybrid osmoadaptation in bacteria:** A 2024 study in *Applied and Environmental Microbiology* finds the polyextremophile *N. thermophilus* uses both compatible-solute accumulation and K+ accumulation under long-term salinity stress, with transporter detection/regulation (OpuA/OpuB/ProU/BetT/PutP) and compatible-solute/ion measurements across 2.5–4.3 M Na+ (10.1128/aem.00145-24; 2024-05) (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19).

**(ii) Quantitative, time-resolved salt shock physiology in a major ectoine producer:** A 2024 *Microbial Cell Factories* paper provides a temporal map for *Halomonas elongata* under NaCl shock, showing an early phase of **Na+ and K+ uptake** and increased amino acid pools (glutamate/glutamine), followed by a delayed rise of ectoine as dominant osmoprotectant, reaching very high short-term productivities (10.1186/s12934-024-02358-5; 2024-03) (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5).

**(iii) Open/unsterile fermentation and lignocellulosic feedstocks:** A 2024 *Microbial Cell Factories* study engineers *Halomonas cupida* for ectoine production, demonstrating **unsterile/open fermentation** and use of corn-straw hydrolysate, with explicit titres/productivities and discussion of halophiles as contamination-resistant chassis (10.1186/s12934-024-02515-w; 2024-08) (chen2024elucidatingthesalttolerant pages 1-2, chen2024elucidatingthesalttolerant pages 10-11).

**(iv) Industrial-chassis perspective for haloenzymes:** A 2024 review argues that halophilic enzymes often cannot be produced in active form in low-salt mesophilic expression systems, motivating development of **haloarchaea-based chassis**; it also provides market context for enzymes (10.3390/microorganisms12081738; 2024-08-22) (bonnaud2024haloarchaeaaspromising pages 1-2).

### 6) Current applications and real-world implementations
**Ectoine production as a halophile-enabled industrial process:**
- Ectoine is presented as a high-value compatible solute with an **annual demand of ~15,000 tons** and a **market price of ~$1,000/kg** (10.1186/s12934-024-02515-w; 2024-08) (chen2024elucidatingthesalttolerant pages 1-2).
- **Unsterile/open fermentation** is explicitly demonstrated for engineered *H. cupida* J9U-P8EC, producing ectoine from a glucose–xylose mix and from corn-straw hydrolysate, highlighting cost reduction via avoidance of sterilization and potential seawater use (chen2024elucidatingthesalttolerant pages 10-11).

**Halophiles as industrial chassis beyond ectoine:** Haloarchaea are positioned as a necessary chassis for production of **halophilic extremozymes** because conventional hosts cannot produce active haloenzymes under low-salt conditions, requiring extensive purification that is described as industrially incompatible (10.3390/microorganisms12081738; 2024-08-22) (bonnaud2024haloarchaeaaspromising pages 1-2).

### 7) Expert opinions / authoritative analysis (curation implications)
- **Operational definition preference (growth-based):** Oren (npj Biodiversity, 2024) emphasizes an operational approach: halophiles are those that **grow at >100–150 g/L salts**, which is directly translatable to a trait definition and assay requirement in TraitMech (10.1038/s44185-024-00050-w; 2024-08) (oren2024novelinsightsinto pages 1-2).
- **Strategy–environment coupling:** The haloarchaea chassis review emphasizes that **salt-out becomes energetically unfavorable at high salinities**, explaining why extreme halophiles often favor **salt-in** at high salt concentrations (10.3390/microorganisms12081738; 2024-08-22) (bonnaud2024haloarchaeaaspromising pages 2-4).

### 8) Relevant recent statistics and quantitative data (2023–2024)
**(A) Halomonas elongata NaCl shock:**
- At 4 h post-shock, ectoine titres reached **4.08 ± 0.28 g/L (5% NaCl)** and **4.58 ± 0.19 g/L (8% NaCl)** (10.1186/s12934-024-02358-5; 2024-03) (yu2024temporaldynamicsof pages 2-5).
- Peak short-term ectoine productivities (maximum during first 4 h) were **1,230 ± 112 mg/L/h (5% NaCl)** and **1,450 ± 99 mg/L/h (8% NaCl)**; specific ectoine production rate qp was **66.54 mg/g DCW/h** at 8% NaCl (yu2024temporaldynamicsof pages 2-5).
- Reported tolerance framing includes **tolerable range (1–8% NaCl shock)** and beyond-threshold shocks up to **13%** associated with respiratory/ATP-synthase inhibition and stagnation (yu2024temporaldynamicsof pages 1-2).

**(B) Halomonas cupida open fermentation:**
- J9U-P8EC achieved **8.55 g/L** ectoine at **142.50 mg/L·h** and **0.32 g/g** conversion (mixed sugars), and **1.30 g/L** at **21.67 mg/L·h** on lignocellulosic hydrolysate in open fermentation (10.1186/s12934-024-02515-w; 2024-08) (chen2024elucidatingthesalttolerant pages 10-11).

**(C) Halomonas campaniensis engineered yield shift:**
- hom knockout increased ectoine yield to **351.13 mg/g CDW** at **1.5 M NaCl**, vs **239.18 mg/g CDW** wild-type; in a 3-L bioreactor, **587.09 mg/g CDW** was reached, with betaine reduced (10.1038/s41598-023-36975-8; 2023-06) (shu2023metabolicengineeringof pages 6-10, shu2023metabolicengineeringof media 6936fa1b).

### 9) Warnings / claims not yet ready for curation
- **Causality vs correlation:** Several sources describe that gene upregulation “could” impact adaptation (e.g., gsmt/sdmt → de novo glycine betaine contribution), but these are partially inferential without direct knockout/causal tests; edges should be marked **uncertain** unless supported by perturbation experiments (xing2024thepolyextremophilenatranaerobius pages 14-17).
- **Review-derived mechanistic edges:** Na+/H+ antiporter-driven Na+ expulsion, halorhodopsin-based Cl− uptake, and proteome acidification are strongly accepted but often review-summarized; curate as high-confidence **background biology** but note **evidence type: review** (bonnaud2024haloarchaeaaspromising pages 2-4, bonnaud2024haloarchaeaaspromising pages 1-2).
- **Transporter component heterogeneity:** In *N. thermophilus*, regulation is component-specific (some Opu/ProU components up/down); avoid over-generalizing “salinity upregulates OpuA/ProU” without component-level mapping (xing2024thepolyextremophilenatranaerobius pages 14-17).

---

## DOI-first bibliography (URLs + publication dates where available)
1. **Bonnaud E, Oger PM, Ohayon A, Louis Y.** *Haloarchaea as Promising Chassis to Green Chemistry.* **Microorganisms**. Published **2024-08-22**. DOI: **10.3390/microorganisms12081738**. URL: https://doi.org/10.3390/microorganisms12081738 (bonnaud2024haloarchaeaaspromising pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4)
2. **Oren A.** *Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems.* **npj Biodiversity**. Published **2024-08**. DOI: **10.1038/s44185-024-00050-w**. URL: https://doi.org/10.1038/s44185-024-00050-w (oren2024novelinsightsinto pages 1-2)
3. **Xing Q, Zhang S, Tao X, Mesbah NM, Mao X, Wang H, Wiegel J, Zhao B.** *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology**. Published **2024-05**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14)
4. **Yu J, Zhang Y, Liu H, et al.** *Temporal dynamics of stress response in Halomonas elongata to NaCl shock: physiological, metabolomic, and transcriptomic insights.* **Microbial Cell Factories**. Published **2024-03**. DOI: **10.1186/s12934-024-02358-5**. URL: https://doi.org/10.1186/s12934-024-02358-5 (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 2-5)
5. **Chen Y, Liu Y, Meng Y, et al.** *Elucidating the salt-tolerant mechanism of Halomonas cupida J9 and unsterile ectoine production from lignocellulosic biomass.* **Microbial Cell Factories**. Published **2024-08** (accepted 2024-08-24). DOI: **10.1186/s12934-024-02515-w**. URL: https://doi.org/10.1186/s12934-024-02515-w (chen2024elucidatingthesalttolerant pages 1-2, chen2024elucidatingthesalttolerant pages 10-11)
6. **Shu Z, Zhang X, Wang R, et al.** *Metabolic engineering of Halomonas campaniensis strain XH26 to remove competing pathways to enhance ectoine production.* **Scientific Reports**. Published **2023-06**. DOI: **10.1038/s41598-023-36975-8**. URL: https://doi.org/10.1038/s41598-023-36975-8 (shu2023metabolicengineeringof pages 6-10, shu2023metabolicengineeringof pages 3-4, shu2023metabolicengineeringof media 6936fa1b)

### Evidence figure/table crop available
Cropped figures showing ectoine yield vs NaCl conditions and bioreactor yield timing in Shu et al. 2023 were retrieved (shu2023metabolicengineeringof media 6936fa1b, shu2023metabolicengineeringof media 8eff8d48).


References

1. (bonnaud2024haloarchaeaaspromising pages 1-2): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

2. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

3. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

4. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 11 citations.

5. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

6. (oren2024novelinsightsinto pages 4-5): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

7. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

8. (shu2023metabolicengineeringof pages 3-4): Zhiwan Shu, Xin Zhang, Rong Wang, Jiangwa Xing, Yongzhen Li, Derui Zhu, and Guoping Shen. Metabolic engineering of halomonas campaniensis strain xh26 to remove competing pathways to enhance ectoine production. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36975-8, doi:10.1038/s41598-023-36975-8. This article has 18 citations and is from a peer-reviewed journal.

9. (thompson2024themicrobiomeof pages 5-6): Michelle E. H. Thompson and Manish N. Raizada. The microbiome of fertilization-stage maize silks (style) encodes genes and expresses traits that potentially promote survival in pollen/style niches and host reproduction. Microorganisms, 12:1473, Jul 2024. URL: https://doi.org/10.3390/microorganisms12071473, doi:10.3390/microorganisms12071473. This article has 6 citations.

10. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (chen2024elucidatingthesalttolerant pages 1-2): Yaping Chen, Yujie Liu, Yan Meng, Yuting Jiang, Weini Xiong, Shufang Wang, Chao Yang, and Ruihua Liu. Elucidating the salt-tolerant mechanism of halomonas cupida j9 and unsterile ectoine production from lignocellulosic biomass. Microbial Cell Factories, Aug 2024. URL: https://doi.org/10.1186/s12934-024-02515-w, doi:10.1186/s12934-024-02515-w. This article has 16 citations and is from a peer-reviewed journal.

12. (lichty2024compatiblesolutesare pages 19-23): Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria This article has 0 citations.

13. (xing2024thepolyextremophilenatranaerobius pages 24-25): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

14. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

15. (shu2023metabolicengineeringof pages 6-10): Zhiwan Shu, Xin Zhang, Rong Wang, Jiangwa Xing, Yongzhen Li, Derui Zhu, and Guoping Shen. Metabolic engineering of halomonas campaniensis strain xh26 to remove competing pathways to enhance ectoine production. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36975-8, doi:10.1038/s41598-023-36975-8. This article has 18 citations and is from a peer-reviewed journal.

16. (yu2024temporaldynamicsof pages 2-5): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 24 citations and is from a peer-reviewed journal.

17. (chen2024elucidatingthesalttolerant pages 10-11): Yaping Chen, Yujie Liu, Yan Meng, Yuting Jiang, Weini Xiong, Shufang Wang, Chao Yang, and Ruihua Liu. Elucidating the salt-tolerant mechanism of halomonas cupida j9 and unsterile ectoine production from lignocellulosic biomass. Microbial Cell Factories, Aug 2024. URL: https://doi.org/10.1186/s12934-024-02515-w, doi:10.1186/s12934-024-02515-w. This article has 16 citations and is from a peer-reviewed journal.

18. (shu2023metabolicengineeringof media 6936fa1b): Zhiwan Shu, Xin Zhang, Rong Wang, Jiangwa Xing, Yongzhen Li, Derui Zhu, and Guoping Shen. Metabolic engineering of halomonas campaniensis strain xh26 to remove competing pathways to enhance ectoine production. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36975-8, doi:10.1038/s41598-023-36975-8. This article has 18 citations and is from a peer-reviewed journal.

19. (shu2023metabolicengineeringof media 8eff8d48): Zhiwan Shu, Xin Zhang, Rong Wang, Jiangwa Xing, Yongzhen Li, Derui Zhu, and Guoping Shen. Metabolic engineering of halomonas campaniensis strain xh26 to remove competing pathways to enhance ectoine production. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36975-8, doi:10.1038/s41598-023-36975-8. This article has 18 citations and is from a peer-reviewed journal.