---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:33:32.043520'
end_time: '2026-06-17T22:48:03.600242'
duration_seconds: 871.56
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: halotolerant
  trait_identifier: METPO:1000622
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: halotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism can tolerate high salt concentrations
    but does not require them for growth.
  parent_traits: METPO:1000629
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: highly halotolerant representatives
    (Supports halotolerant microorganisms as high-salt tolerant without strict salt
    requirement.) | PMID:27621824: Halomonas massiliensis sp. nov., a new halotolerant
    bacterium (Organism example: Halomonas massiliensis is described as halotolerant.)'
  causal_graph_summary: 'halotolerant_salt_stress_response: 6 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** halotolerant
- **METPO identifier:** METPO:1000622
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate high salt concentrations but does not require them for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: highly halotolerant representatives (Supports halotolerant microorganisms as high-salt tolerant without strict salt requirement.) | PMID:27621824: Halomonas massiliensis sp. nov., a new halotolerant bacterium (Organism example: Halomonas massiliensis is described as halotolerant.)
- **Existing causal graph summary:** halotolerant_salt_stress_response: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **halotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halotolerant.yaml`.

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
- **Trait label:** halotolerant
- **METPO identifier:** METPO:1000622
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate high salt concentrations but does not require them for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: highly halotolerant representatives (Supports halotolerant microorganisms as high-salt tolerant without strict salt requirement.) | PMID:27621824: Halomonas massiliensis sp. nov., a new halotolerant bacterium (Organism example: Halomonas massiliensis is described as halotolerant.)
- **Existing causal graph summary:** halotolerant_salt_stress_response: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **halotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halotolerant.yaml`.

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


# Research Report: Microbial Trait “Halotolerant” (METPO:1000622)

## 1) Scope summary (trait meaning, boundaries, and assay representations)

**Trait definition (curation target):** *Halotolerant* denotes microorganisms that **tolerate high salt concentrations but do not require salt for growth** (i.e., can grow in low/no added salt as well as elevated NaCl). This distinguishes halotolerant organisms from **halophiles**, which require salt for growth. A recent rhizosphere study explicitly states that halotolerant bacteria “can tolerate relatively high NaCl concentrations and grow regardless of salt’s presence or absence,” contrasting them with halophiles that flourish at very high salt. (reang2024extremozymesandcompatible pages 1-2)

**Boundary cases / nearby traits:**
- **Halotolerant vs (slight/moderate/extreme) halophiles:** A recent review summarizing salinity categories (non-halophiles ≤1% NaCl; slight 1–3%; moderate 3–15%; extreme ≥15–25%) reinforces that **halophiles require salt**, while **halotolerants can persist without it**. (santoyo2024trichodermaandbacillus pages 3-4)
- **Mechanistic boundary (salt-out vs salt-in):** Halotolerance is most commonly associated with the **“salt-out” strategy** (exclude excess inorganic ions and balance osmotic pressure using organic compatible solutes). Extreme halophily often relies on **“salt-in”** (intracellular inorganic ion accumulation such as KCl), which has downstream consequences for proteome composition and enzyme salt-dependence. (fan2024improvementinsalt pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4)
- **Environmental boundary:** In soil ecology, “saline” is commonly operationalized by electrical conductivity (ECe > 4 dS/m), and hypersaline soils may exceed crop tolerance ranges; a hypersaline soil study used ECe = 97.02 dS/m and observed active communities dominated by extreme halophiles, with moderately halophilic/halotolerant taxa also growing but less actively. (veragargallo2023thriveorsurvive pages 1-2)
- **Habitat definition boundary:** Hypersaline environments are defined in a 2024 synthesis as >100–150 g/L salts, where growth can reach “up to saturation” and specialized strategies dominate. (oren2024novelinsightsinto pages 1-2)

**Assay/phenotype representations appropriate for curation:**
- **Growth across a NaCl gradient** (e.g., presence/absence of salt; growth at multiple NaCl % w/v or molarities). (reang2024extremozymesandcompatible pages 1-2, fan2024improvementinsalt pages 10-12)
- **Physiological readouts**: intracellular compatible-solute pools; ion homeostasis markers; expression of salt-response transporters/synthesis genes. (fan2024improvementinsalt pages 12-14, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media f888d5a9)
- **Functional readouts** relevant to applications: pollutant degradation under saline conditions; plant growth promotion under saline irrigation; enzyme activity under salt. (fan2024improvementinsalt pages 12-14, reang2024extremozymesandcompatible pages 1-2)

## 2) Current mechanistic understanding (concepts → entities)

### 2.1 Core concept: salt stress has osmotic + ionic components
High salinity imposes **osmotic stress** (water efflux, turgor loss) and **ionic stress** (Na+ toxicity; disruption of enzyme function and electrochemical gradients), necessitating coordinated osmoadaptation and ion homeostasis. (fan2024improvementinsalt pages 1-2, lichty2024compatiblesolutesare pages 19-23)

### 2.2 Two major osmoadaptation strategies

**Salt-out (typical for halotolerants; also used by many halophiles):** Export/exclude salts via membrane systems and accumulate **compatible solutes** (osmolytes that do not strongly interfere with metabolism). Compatible solutes cited across recent sources include **glycine betaine, proline, trehalose, mannitol, ectoine**. (fan2024improvementinsalt pages 1-2, reang2024extremozymesandcompatible pages 1-2)

**Salt-in (more typical of extreme halophiles; boundary for halotolerant trait):** Accumulate inorganic ions (notably **K+** and often Cl−) to balance external osmolarity, coupled to protein/proteome adaptations (acidic proteomes) that maintain function at high ionic strength. (bonnaud2024haloarchaeaaspromising pages 2-4)

### 2.3 Compatible solutes: biosynthesis and uptake modules
A recent synthesis of compatible solutes summarizes that they are accumulated **via biosynthesis or uptake** and details major transporter classes. (lichty2024compatiblesolutesare pages 19-23)

**Biosynthesis (examples that are highly “TraitMech-curatable”):**
- **Glycine betaine biosynthesis from choline via betA/betB.** (lichty2024compatiblesolutesare pages 19-23)
- **Ectoine biosynthesis via ectABC operon; ectD converts ectoine to 5-hydroxyectoine.** (lichty2024compatiblesolutesare pages 19-23)
- Isolate-level confirmation: halophilic/halotolerant rhizosphere strains produced ectoine and had PCR evidence for an “ectoine synthase gene” and for “betaine aldehyde dehydrogenase” (betB) in those isolates. (reang2024extremozymesandcompatible pages 1-2)

**Uptake (transport modules):**
- **BCCT-family carriers** using proton- or sodium-motive force; **ABC systems** such as **ProU** (E. coli ProV/ProW/ProX); **MFS** (e.g., ProP transporting proline/GB/ectoine); and **TRAP** (TeaABC, UehABC for ectoine/hydroxyectoine). (lichty2024compatiblesolutesare pages 19-23)
- In an extremely halophilic bacterium, proteome/transcript/metabolite data indicate that **Opu and ProU-family ABC transporters** are used for glycine betaine import during long-term salinity adaptation. (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19)

### 2.4 Ion homeostasis modules (Na+ export; K+ uptake)

**Na+ export:** Na+/H+ antiporters (families including NhaA, NhaB, NhaC, NhaD) are discussed as key components of the salt-out strategy for salt export and Na+ detoxification. (fan2024improvementinsalt pages 1-2)

**K+ uptake:** In bacterial systems, K+ uptake is often mediated by Kdp/Trk-class systems and can be transcriptionally induced under hypertonic conditions (though its contribution to growth may be taxon-specific). In Pseudomonas putida KT2440, kdpA/kdpB/kdpD were upregulated under hypertonic conditions; however, the authors report that overexpressing kdp did not improve growth and infer that K+ accumulation is not a primary salt-tolerance strategy for this strain. (fan2024improvementinsalt pages 12-14)

## 3) Recent developments & latest research (prioritizing 2023–2024)

### 3.1 Quantitative metabolite/ion evidence for hybrid adaptation strategies (2024)
A 2024 multi-omics study of *Natranaerobius thermophilus* reports a hybrid long-term adaptation strategy combining compatible solutes and ion homeostasis. Intracellular compatible solutes **increase with salinity**, with glycine betaine and glutamate reported to rise across 2.5–4.3 M Na+ conditions (e.g., glycine betaine 52.7 → 893.1 mM; glutamate 11.0 → 221.3 mM), and K+ is tracked alongside these pools. (xing2024thepolyextremophilenatranaerobius pages 17-19)

**Visual evidence:** Figure 8 from this study summarizes intracellular compatible solutes and K+ across the salinity series, supporting a causal edge “increased salinity → increased compatible solutes/K+.” (xing2024thepolyextremophilenatranaerobius media f888d5a9)

### 3.2 Engineering halotolerance for applications (2024)
A 2024 engineering study in *Pseudomonas putida* KT2440 provides a mechanistically interpretable example of improving halotolerance via combined ion homeostasis and compatible-solute pathways:
- Baseline tolerance in minimal medium: **4% w/v NaCl**.
- Engineering: overexpression of **betB** (betaine aldehyde dehydrogenase) and heterologous **E. coli nhaA** (EcnhaA) increased maximum tolerance to **5% w/v NaCl**.
- Supplementation with compatible solutes (betaine and proline) increased tolerance to **6% w/v NaCl**.
- The engineered strain degraded aromatic pollutants under 4% w/v NaCl, demonstrating a real-world bioremediation-relevant phenotype under salinity. (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12)

### 3.3 Saline soil microbiology and halotolerant relevance (2023–2024)
- **Scale of the problem:** Salt-affected soils cover **>900 million hectares globally**, and projections suggest up to **50% of arable land** could be drought- and salt-affected by 2050. (veragargallo2023thriveorsurvive pages 1-2)
- DNA-stable isotope probing in hypersaline soil (ECe = 97.02 dS/m) showed that extreme halophiles dominated the active community, but moderately halophilic/halotolerant taxa also grew, implying that halotolerance mechanisms remain ecologically relevant even when salt-in specialists dominate. (veragargallo2023thriveorsurvive pages 1-2)
- In agricultural biotechnology reviews focused on halotolerant plant-growth-promoting bacteria (PGPB), reported halotolerant PGPB are dominated by **Firmicutes (~50%), Proteobacteria (~40%), Actinobacteria (~10%)**, and common functional capacities in evaluated halotolerant PGPB genomes include osmoprotectants (~80%) and ion homeostasis (~80%). (zamanzadehnasrabadi2023salinitystressendurance pages 1-2)

### 3.4 Expanding knowledge of halophiles and boundaries with halotolerants (2024)
A 2024 synthesis emphasizes that halophile diversity and metabolic potential have expanded substantially with cultivation and metagenomics; it operationalizes hypersaline as >100–150 g/L salts and documents increased taxonomic breadth (as of Dec 2023: nine families, 82 genera, 357 species vs. 2017: six families, 57 genera, 233 species). These sources are useful to define what *halotolerant* is **not** (i.e., obligate high-salt specialists). (oren2024novelinsightsinto pages 1-2)

## 4) Current applications and real-world implementations

### 4.1 Bioremediation in saline environments
Engineering salt tolerance in chassis organisms can enable pollutant degradation in saline wastewater/brines. The engineered *P. putida* KT2440-EcnhaA-betB strain degraded aromatic pollutants under 4% w/v NaCl in 48 h (benzoic acid and protocatechuic acid), while the wild-type did not in the same conditions, demonstrating direct applicability to high-salinity bioremediation. (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14)

### 4.2 Agricultural bioinoculants / saline soil remediation (halotolerant PGPB)
Salinity-affected agriculture motivates use of halotolerant microbes that promote growth and stress resilience. A 2023 review reports taxonomic composition and functional-gene prevalence (e.g., osmoprotectants and ion homeostasis each ~80% among evaluated halotolerant PGPB genomes), supporting a practical screening focus for marker development and inoculant design. (zamanzadehnasrabadi2023salinitystressendurance pages 1-2)

### 4.3 Industrial and biotechnological products linked to halotolerance mechanisms
A rhizosphere isolate study shows halophilic/halotolerant bacteria can produce enzymes (“extremozymes/halozymes”) and compatible solutes (ectoine), and explicitly ties compatible-solute production to enzyme stability under saline conditions (though it notes that the correlation warrants further work). (reang2024extremozymesandcompatible pages 1-2)

## 5) Candidate nodes for a TraitMech causal graph (with ontology grounding)

| Group | Node label | Brief definition / role in halotolerance | Suggested grounding | Evidence |
|---|---|---|---|---|
| Environmental factors / assays | high salinity | Elevated external salt concentration that imposes osmotic and ionic stress; core environmental condition used to assay halotolerance | label only | High salinity is the defining stressor across recent halotolerance studies; e.g., growth at 4–6% NaCl in engineered *Pseudomonas putida*, and broad discussion of saline/hypersaline habitats (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 10-12, veragargallo2023thriveorsurvive pages 1-2, oren2024novelinsightsinto pages 1-2) |
| Environmental factors / assays | salt stress | Stress condition caused by excess salt, typically including osmotic and ionic components | GO:0009651 | Explicitly discussed as the condition mitigated by compatible solutes, ion homeostasis, and transporter systems (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, zamanzadehnasrabadi2023salinitystressendurance pages 1-2) |
| Environmental factors / assays | osmotic stress | Water-activity / osmolarity stress induced by high external solute concentration; immediate driver of osmoadaptation | GO:0006970 | Compatible solutes are described as accumulated in response to osmotic stress (lichty2024compatiblesolutesare pages 19-23) |
| Environmental factors / assays | saline soil | Salt-affected soil habitat where halotolerant microbes are ecologically relevant and often assayed | ENVO:00002010 | Saline soils are defined operationally by ECe and are a major application context for halotolerant microbes (zamanzadehnasrabadi2023salinitystressendurance pages 1-2, veragargallo2023thriveorsurvive pages 1-2) |
| Environmental factors / assays | hypersaline environment | Environment with very high dissolved salt, often >100–150 g/L salts; boundary habitat where obligate/extreme halophiles dominate | ENVO:01000026 | Recent review defines hypersaline environments and notes growth “up to saturation” for true halophiles (oren2024novelinsightsinto pages 1-2) |
| Processes / strategies | salt-out strategy | Osmoadaptation strategy based on excluding excess inorganic ions and accumulating organic compatible solutes | label only | Presented as the typical strategy for halotolerant organisms and many moderate halophiles (fan2024improvementinsalt pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4, reang2024extremozymesandcompatible pages 1-2) |
| Processes / strategies | compatible solute accumulation | Intracellular buildup of organic osmolytes that balance osmotic pressure while preserving macromolecular function | label only | Central mechanistic process in bacterial halotolerance (lichty2024compatiblesolutesare pages 19-23, reang2024extremozymesandcompatible pages 1-2) |
| Processes / strategies | de novo compatible solute biosynthesis | Synthesis of osmoprotectants such as ectoine or glycine betaine from metabolic precursors | label only | Supported by ectABC and betA/betB pathway evidence (lichty2024compatiblesolutesare pages 19-23, reang2024extremozymesandcompatible pages 1-2) |
| Processes / strategies | ion homeostasis | Regulation of intracellular Na+ and K+ levels during salt stress | GO:0050801 | Broadly highlighted in halotolerant genomes and engineering studies as a core trait component (fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12, zamanzadehnasrabadi2023salinitystressendurance pages 1-2) |
| Processes / strategies | K+ accumulation | Rapid or sustained intracellular potassium accumulation used for osmotic adjustment and charge balance | label only | Seen as part of osmoregulation; major in some taxa and hybrid strategies (xing2024thepolyextremophilenatranaerobius pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4, fan2024improvementinsalt pages 10-12, xing2024thepolyextremophilenatranaerobius media f888d5a9) |
| Processes / strategies | Na+ extrusion | Export of cytoplasmic sodium to reduce ionic stress, commonly via Na+/H+ antiporters | label only | Antiporter-mediated Na+ export is a recurring salt-tolerance mechanism (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, bonnaud2024haloarchaeaaspromising pages 2-4) |
| Processes / strategies | salt-in strategy | Boundary-case osmoadaptation strategy based on intracellular accumulation of KCl or other inorganic ions; more typical of extreme halophiles than generic halotolerant microbes | label only | Important for distinguishing halotolerant from obligate/extreme halophilic states (bonnaud2024haloarchaeaaspromising pages 2-4, xing2024thepolyextremophilenatranaerobius pages 1-2, oren2024novelinsightsinto pages 1-2) |
| Processes / strategies | exopolysaccharide production (EPS) | Possible support trait that may buffer cells or microenvironments in saline soils; should be treated as supportive rather than core without direct mechanistic proof | label only | Mentioned as a trait that may support growth in hypersaline soils and common in salinity-mitigating PGPB literature (zamanzadehnasrabadi2023salinitystressendurance pages 1-2, veragargallo2023thriveorsurvive pages 1-2) |
| Genes / proteins / complexes | ectABC operon | Canonical ectoine biosynthesis genes enabling de novo ectoine production from aspartate-derived precursors | label only | Explicitly identified as the ectoine biosynthetic operon/pathway (lichty2024compatiblesolutesare pages 19-23) |
| Genes / proteins / complexes | ectoine synthase gene | Gene evidence used in isolates to support ectoine biosynthesis capability | label only | PCR detection used as evidence in halophilic/halotolerant isolates (reang2024extremozymesandcompatible pages 1-2) |
| Genes / proteins / complexes | betA | Choline dehydrogenase; first step in glycine betaine synthesis from choline | label only | Part of the betA/betB route from choline to glycine betaine (lichty2024compatiblesolutesare pages 19-23) |
| Genes / proteins / complexes | betB | Betaine aldehyde dehydrogenase; converts betaine aldehyde to glycine betaine and can improve salt tolerance when overexpressed | label only | Directly implicated in glycine betaine biosynthesis and salt-tolerance engineering (fan2024improvementinsalt pages 12-14, lichty2024compatiblesolutesare pages 19-23, reang2024extremozymesandcompatible pages 1-2, fan2024improvementinsalt pages 10-12) |
| Genes / proteins / complexes | Kdp system | High-affinity potassium uptake system associated with osmotic adaptation in many bacteria | label only | Kdp genes were induced under hypertonic conditions; role may be taxon-dependent (fan2024improvementinsalt pages 10-12) |
| Genes / proteins / complexes | Trk system | Potassium uptake system involved in osmoregulation in many bacteria | label only | Discussed alongside Kdp as a K+ uptake/osmoregulatory system (fan2024improvementinsalt pages 10-12) |
| Genes / proteins / complexes | Na+/H+ antiporter (NhaA family) | Sodium/proton antiporter family that helps export Na+ and support salt tolerance | label only | Na+/H+ antiporters are repeatedly identified as core salt-out effectors (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, bonnaud2024haloarchaeaaspromising pages 2-4) |
| Genes / proteins / complexes | EcnhaA | Heterologous *E. coli* Na+/H+ antiporter used to improve salt tolerance in *P. putida* | label only | Strong engineering evidence but assay-specific and not a universal native node (fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12) |
| Transporters | ProU-family ABC transporter | High-affinity ABC transporter family for compatible-solute import, especially glycine betaine | label only | Specifically named in a salinity-adaptation study as a glycine betaine transporter family (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Transporters | Opu-family ABC transporter | ABC transporter family involved in compatible-solute uptake, including glycine betaine | label only | Specifically named with ProU in salt adaptation (xing2024thepolyextremophilenatranaerobius pages 1-2) |
| Transporters | BCCT transporter | Betaine/carnitine/choline transporter family that imports compatible solutes using ion motive force | label only | Described as a major compatible-solute uptake class; widespread in halophiles/halotolerant microbes (lichty2024compatiblesolutesare pages 19-23, bonnaud2024haloarchaeaaspromising pages 2-4) |
| Transporters | PutP | Na+/proline symporter mediating sodium-dependent proline uptake | label only | Directly identified as a proline uptake transporter under salinity adaptation (xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Transporters | ProP | MFS-compatible-solute transporter that can transport proline, glycine betaine, and ectoine | label only | Named as an MFS transporter for multiple osmolytes (lichty2024compatiblesolutesare pages 19-23) |
| Metabolites / chemicals | ectoine | Major compatible solute / osmoprotectant widely used in microbial salt tolerance and biotechnology | CHEBI:27689 | A central osmolyte in halotolerant and halophilic bacteria, with pathway and production evidence (lichty2024compatiblesolutesare pages 19-23, reang2024extremozymesandcompatible pages 1-2) |
| Metabolites / chemicals | 5-hydroxyectoine / hydroxyectoine | Hydroxylated derivative of ectoine; compatible solute and stress protectant | label only | Mentioned as an ectoine derivative taken up by transporters and associated with osmoprotection (lichty2024compatiblesolutesare pages 19-23) |
| Metabolites / chemicals | glycine betaine | Canonical compatible solute accumulated or imported during salt stress | CHEBI:17750 | Strongly supported across recent studies as a major osmoprotectant (fan2024improvementinsalt pages 1-2, lichty2024compatiblesolutesare pages 19-23, xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Metabolites / chemicals | L-proline | Compatible solute and osmoprotective amino acid | CHEBI:26271 | Explicitly listed as a compatible solute and transported by PutP/ProP (fan2024improvementinsalt pages 1-2, lichty2024compatiblesolutesare pages 19-23, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| Metabolites / chemicals | L-glutamate | Amino-acid osmolyte/compatible solute that can increase with salinity in some taxa | CHEBI:29991 | Reported as an intracellular compatible solute increasing under salt stress (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media f888d5a9) |
| Metabolites / chemicals | trehalose | Non-reducing sugar compatible solute used in salt-out adaptation | CHEBI:16551 | Cited as a common compatible solute in reviews of salt adaptation (fan2024improvementinsalt pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4) |
| Metabolites / chemicals | choline | Environmental precursor for glycine betaine biosynthesis via betA/betB | CHEBI:15354 | Explicit precursor in the betA/betB pathway (lichty2024compatiblesolutesare pages 19-23) |
| Metabolites / chemicals | potassium ion (K+) | Inorganic osmolyte central to K+ uptake and salt-in/hybrid osmoadaptation strategies | CHEBI:29103 | Measured as part of salinity adaptation and boundary-case salt-in responses (xing2024thepolyextremophilenatranaerobius pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4, xing2024thepolyextremophilenatranaerobius media f888d5a9) |
| Metabolites / chemicals | sodium ion (Na+) | Principal toxic/external ion whose high concentration drives salt stress and antiporter responses | CHEBI:29101 | Central ionic stressor in saline environments and antiporter-mediated homeostasis (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, bonnaud2024haloarchaeaaspromising pages 2-4) |


*Table: This table lists candidate node types and labels for a TraitMech-style causal graph of microbial halotolerance, with concise functional roles and ontology grounding where supported. It separates broadly curatable core nodes from boundary-case nodes such as the salt-in strategy.*

## 6) Evidence-backed candidate causal edges (triples) for curation

| Subject | Predicate | Object | Evidence source | Supporting snippet | Notes | Suggested grounding |
|---|---|---|---|---|---|---|
| osmotic stress / high salinity | increases | compatible solute accumulation | Lichty 2024, doi:10.58088/07hg-r941 | “Compatible solutes are accumulated in response to osmotic stress” (lichty2024compatiblesolutesare pages 19-23) | Broad mechanistic claim across marine bacteria; suitable as a general edge for halotolerance. | Subject: label `osmotic stress`; Object: GO:0006970 osmotic stress response / label `compatible solute accumulation` |
| halotolerant strategy (“salt-out”) | relies on | compatible solute accumulation or de novo synthesis | Reang 2024, doi:10.1038/s41598-024-63581-z | “ ‘salt-out’ or ‘low-salt-high-compatible-solute-in-cytoplasm’ strategy… relies on accumulation or de-novo synthesis of organic compatible solutes” (reang2024extremozymesandcompatible pages 1-2) | Directly supports halotolerant scope; distinguishes from obligate/extreme halophile salt-in strategy. | Subject: label `salt-out strategy`; Object: label `compatible solute accumulation` |
| ectABC operon | enables | ectoine biosynthesis | Lichty 2024, doi:10.58088/07hg-r941 | “ectoine is synthesized de novo from aspartic acid via the ectABC operon” (lichty2024compatiblesolutesare pages 19-23) | Strong pathway edge; general bacterial mechanism, not specific to all halotolerant taxa. | Subject: KEGG/MetaCyc label `ectABC`; Object: CHEBI:27689 ectoine |
| ectoine synthase gene | supports | ectoine production | Reang 2024, doi:10.1038/s41598-024-63581-z | “PCR showed the presence of the ectoine synthase gene responsible for its biosynthesis” (reang2024extremozymesandcompatible pages 1-2) | Isolate-specific evidence from halophilic/halotolerant rhizosphere bacteria; useful corroboration for ectoine node. | Subject: label `ectoine synthase gene`; Object: CHEBI:27689 ectoine |
| betA + betB | enables | glycine betaine biosynthesis from choline | Lichty 2024, doi:10.58088/07hg-r941 | “GB is produced from environmental choline via betA and betB” (lichty2024compatiblesolutesare pages 19-23) | Canonical pathway edge; broadly applicable where choline oxidation route is present. | Subject: label `betA/betB`; Object: CHEBI:17750 glycine betaine; input: CHEBI:15354 choline |
| betaine aldehyde dehydrogenase (betB) | contributes to | salt tolerance via betaine accumulation | Fan 2024, doi:10.3390/biology13060404 | “overexpression of betB… improved growth under 4% NaCl” and authors “speculate betaine is the major compatible solute” (fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12) | Functional evidence from engineered *Pseudomonas putida* KT2440; curate as taxon-specific unless generalized by additional sources. | Subject: EC 1.2.1.8 betaine-aldehyde dehydrogenase / label `betB`; Object: label `salt tolerance` |
| ProU-family ABC transporter | imports | glycine betaine | Xing 2024, doi:10.1128/aem.00145-24 | “employs the glycine betaine ABC transporters (Opu and ProU families)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Strong transporter edge, but demonstrated in *Natranaerobius thermophilus* (extreme halophile); mechanism likely transferable. | Subject: label `ProU family ABC transporter`; Object: CHEBI:17750 glycine betaine |
| Opu-family ABC transporter | imports | glycine betaine | Xing 2024, doi:10.1128/aem.00145-24 | “employs the glycine betaine ABC transporters (Opu and ProU families)” (xing2024thepolyextremophilenatranaerobius pages 1-2) | As above; taxon-specific to *N. thermophilus* in excerpt. | Subject: label `Opu family ABC transporter`; Object: CHEBI:17750 glycine betaine |
| glycine betaine ABC transporters | increase intracellular | glycine betaine under high salinity | Xing 2024, doi:10.1128/aem.00145-24 | “glycine betaine, imported through ABC transporters, acts as the main osmoprotectant” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Good causal edge linking transporter activity to osmoprotection; species-specific. | Subject: label `glycine betaine ABC transporter activity`; Object: CHEBI:17750 glycine betaine |
| PutP (Na+/proline symporter) | mediates uptake of | proline | Xing 2024, doi:10.1128/aem.00145-24 | “The Na+/proline symporter PutP mediates sodium-dependent proline uptake” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Direct transporter edge from excerpt; evidence in *N. thermophilus*. | Subject: label `PutP`; Object: CHEBI:26271 L-proline |
| increased salinity | increases intracellular | glycine betaine | Xing 2024, doi:10.1128/aem.00145-24 | “intracellular glycine betaine rises markedly with external Na+ (52.7 to 893.1 mM across 2.5–4.3 M Na+)” (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media f888d5a9) | Quantitative evidence; strong but species-specific. | Subject: label `high salinity`; Object: CHEBI:17750 glycine betaine |
| increased salinity | increases intracellular | glutamate | Xing 2024, doi:10.1128/aem.00145-24 | “intracellular L-glutamate increases (11.0 to 221.3 mM across 2.5–4.3 M Na+)” (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media f888d5a9) | Quantitative evidence; compatible-solute role in one extreme halophile. | Subject: label `high salinity`; Object: CHEBI:29991 L-glutamate |
| Na+/H+ antiporter (NhaA family) | extrudes | Na+ | Fan 2024, doi:10.3390/biology13060404 | “Na+/H+ antiporters (families NhaA, NhaB, NhaC, NhaD)” support a salt-out mechanism with salt export (fan2024improvementinsalt pages 1-2) | General mechanistic support from review/discussion; exact edge should be marked inferred from family function in excerpt. | Subject: label `NhaA Na+/H+ antiporter`; Object: CHEBI:29101 sodium(1+) |
| nhaA-II overexpression | improves | growth under salt stress | Fan 2024, doi:10.3390/biology13060404 | “nhaA-II was upregulated ~7.4-fold and its overexpression slightly improved growth” (fan2024improvementinsalt pages 12-14) | Functional but modest effect in *P. putida* KT2440; taxon- and assay-specific. | Subject: label `nhaA-II`; Object: label `salt tolerance/growth under NaCl` |
| heterologous EcnhaA expression | increases | salt tolerance | Fan 2024, doi:10.3390/biology13060404 | “heterologous EcnhaA overexpression could significantly improve the growth” and co-expression raised tolerance to 5% NaCl (fan2024improvementinsalt pages 12-14) | Engineering evidence; good application edge, but not native-mechanism proof for all taxa. | Subject: label `EcnhaA`; Object: label `salt tolerance` |
| Kdp/Trk systems | mediate | K+ uptake | Fan 2024, doi:10.3390/biology13060404 | “the Kdp and Trk systems are involved in K+ uptake/osmoregulation” (fan2024improvementinsalt pages 10-12) | General transporter-function edge supported in excerpt; direct contribution to halotolerance may vary by taxon. | Subject: label `Kdp/Trk potassium transport systems`; Object: CHEBI:29103 potassium(1+) |
| hypertonic conditions | upregulate | kdpA/kdpB/kdpD | Fan 2024, doi:10.3390/biology13060404 | “Transcriptomics showed upregulation of… K+ transporter genes (kdpA, kdpB, kdpD)” (fan2024improvementinsalt pages 10-12) | Strong expression edge in *P. putida* KT2440; does not by itself prove improved tolerance. | Subject: label `hypertonic conditions`; Object: label `kdpA/kdpB/kdpD expression` |
| K+ accumulation (“salt-in” strategy) | supports | osmotic adjustment at high salinity | Bonnaud 2024, doi:10.3390/microorganisms12081738 | “salt-in… sequestration of inorganic ions… Potassium… enters the cell through a uniport system” (bonnaud2024haloarchaeaaspromising pages 2-4) | Important contrast trait boundary: typical of extreme halophiles more than halotolerant organisms. | Subject: label `salt-in strategy`; Object: CHEBI:29103 potassium(1+) |
| salt-in strategy | selects for / is associated with | acidic proteome adaptation | Bonnaud 2024, doi:10.3390/microorganisms12081738 | “Adaptations include acidified proteomes, high GC content, increased surface acidic residues” (bonnaud2024haloarchaeaaspromising pages 2-4) | Strong general edge for extreme halophiles; may be inappropriate as a core edge for generic halotolerance unless marked boundary-case. | Subject: label `salt-in strategy`; Object: label `acidic proteome` |
| high salinity / salt-in adaptation | is associated with | very acidic proteomes | Gutiérrez-Preciado 2024, doi:10.1038/s41559-024-02505-6 | “halophilic archaea accumulate up to 4 M K+ in their cytoplasm… ‘salt-in’ strategy” and MAGs encoded “the most acidic proteomes ever observed” (bonnaud2024haloarchaeaaspromising pages 2-4) | Supports stronger version of salt-in→acidic proteome, but this evidence is about archaeal extreme halophily rather than halotolerance. | Subject: label `salt-in adaptation`; Object: label `acidic proteome` |


*Table: This table lists candidate subject-predicate-object edges for a halotolerant TraitMech graph, with supporting excerpts, cautions about taxon specificity, and suggested ontology grounding. It is useful as a curation-ready starting point for selecting which mechanisms are broadly supported versus boundary-case or organism-specific.*

## 7) Expert synthesis / analysis (curation guidance)

1. **Core halotolerance graph should emphasize “salt-out” + compatible solutes + Na+ homeostasis** because these mechanisms are repeatedly described as central for halotolerant microbes and moderate halophiles. (fan2024improvementinsalt pages 1-2, reang2024extremozymesandcompatible pages 1-2)
2. **Transport and biosynthesis are both first-class entities**: sources explicitly describe uptake systems (BCCT, ABC ProU, MFS ProP, TRAP Tea/Ueh) and biosynthetic routes (betA/betB; ectABC/ectD), enabling mechanistic edges that are portable across taxa when gene evidence exists. (lichty2024compatiblesolutesare pages 19-23)
3. **K+ accumulation is context-dependent**: Kdp/Trk are often induced by hypertonic stress, but functional contribution can be strain-specific; therefore, edges “Kdp → halotolerance” should be marked uncertain unless supported by direct phenotyping in the target taxon. (fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12)
4. **Salt-in / acidic proteome adaptation is an important boundary mechanism**: it is highly relevant for extreme halophiles and for understanding why some taxa become salt-dependent, but it should be curated as a *boundary-case/nearby-trait* module rather than as a default halotolerant mechanism. (bonnaud2024haloarchaeaaspromising pages 2-4, oren2024novelinsightsinto pages 1-2)

## 8) Statistics and data highlights (recent)

- **Global extent:** salt-affected soils >900 million hectares; projection up to 50% arable land drought- and salt-affected by 2050. (Vera-Gargallo et al., 2023; DOI:10.1186/s40793-023-00475-z; published Mar 2023) (veragargallo2023thriveorsurvive pages 1-2)
- **Agricultural-microbe composition (reported halotolerant PGPB):** Firmicutes ~50%, Proteobacteria ~40%, Actinobacteria ~10%; functional traits among evaluated genomes include osmoprotectants ~80% and ion homeostasis ~80%. (Zamanzadeh-Nasrabadi et al., 2023; DOI:10.3389/fgene.2023.1049608; published Apr 2023) (zamanzadehnasrabadi2023salinitystressendurance pages 1-2)
- **Quantitative solute response to salinity:** in a 2024 extreme-halophile study, intracellular glycine betaine increases from 52.7 to 893.1 mM across 2.5–4.3 M Na+, and intracellular glutamate increases from 11.0 to 221.3 mM across the same range. (Xing et al., 2024; DOI:10.1128/aem.00145-24; published May 2024) (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media f888d5a9)
- **Engineering thresholds (bioremediation chassis):** engineered *P. putida* KT2440 tolerance increased from 4% w/v NaCl to 5% (gene co-expression) and to 6% with compatible-solute supplementation; degradation of aromatic pollutants under 4% w/v NaCl demonstrated. (Fan et al., 2024; DOI:10.3390/biology13060404; published Jun 2024) (fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12)

## 9) Warnings / “do not curate yet” items

- **Do not treat salt-in and acidic proteome adaptation as core halotolerance edges** unless the trait scope is expanded to halophily/extreme halophily; these are best curated as boundary/neighbor modules. (bonnaud2024haloarchaeaaspromising pages 2-4)
- **Treat engineered gene effects as assay- and chassis-specific**: e.g., heterologous EcnhaA and betB overexpression improves salt tolerance in *P. putida* KT2440, but may not generalize without additional evidence. (fan2024improvementinsalt pages 12-14)
- **Ectoine/enzyme stability linkage** in rhizosphere isolates is suggestive but explicitly described as needing further investigation; curate cautiously as a hypothesis edge. (reang2024extremozymesandcompatible pages 1-2)

---

# DOI-first bibliography (URLs + publication dates)

1. Reang L, et al. *Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria…* **Scientific Reports** (Jul 2024). DOI: **10.1038/s41598-024-63581-z**. URL: https://doi.org/10.1038/s41598-024-63581-z (reang2024extremozymesandcompatible pages 1-2)
2. Fan M, et al. *Improvement in Salt Tolerance Ability of Pseudomonas putida KT2440.* **Biology** (Jun 2024). DOI: **10.3390/biology13060404**. URL: https://doi.org/10.3390/biology13060404 (fan2024improvementinsalt pages 1-2, fan2024improvementinsalt pages 12-14, fan2024improvementinsalt pages 10-12)
3. Xing Q, et al. *Natranaerobius thermophilus adopts a dual adaptive strategy…* **Applied and Environmental Microbiology** (May 2024). DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius media f888d5a9)
4. Bonnaud E, et al. *Haloarchaea as Promising Chassis to Green Chemistry.* **Microorganisms** (Aug 2024). DOI: **10.3390/microorganisms12081738**. URL: https://doi.org/10.3390/microorganisms12081738 (bonnaud2024haloarchaeaaspromising pages 2-4)
5. Santoyo G, et al. *Trichoderma and Bacillus multifunctional allies… in saline soils.* **Frontiers in Microbiology** (Aug 2024). DOI: **10.3389/fmicb.2024.1423980**. URL: https://doi.org/10.3389/fmicb.2024.1423980 (santoyo2024trichodermaandbacillus pages 3-4)
6. Oren A. *Novel insights into the diversity of halophilic microorganisms…* **npj Biodiversity** (Aug 2024). DOI: **10.1038/s44185-024-00050-w**. URL: https://doi.org/10.1038/s44185-024-00050-w (oren2024novelinsightsinto pages 1-2)
7. Vera-Gargallo B, et al. *Thrive or survive: prokaryotic life in hypersaline soils.* **Environmental Microbiome** (Mar 2023). DOI: **10.1186/s40793-023-00475-z**. URL: https://doi.org/10.1186/s40793-023-00475-z (veragargallo2023thriveorsurvive pages 1-2)
8. Zamanzadeh-Nasrabadi SM, et al. *Salinity stress endurance of the plants with the aid of bacterial genes.* **Frontiers in Genetics** (Apr 2023). DOI: **10.3389/fgene.2023.1049608**. URL: https://doi.org/10.3389/fgene.2023.1049608 (zamanzadehnasrabadi2023salinitystressendurance pages 1-2)
9. Lichty KB. *Compatible Solutes Are Accumulated in Response to Osmotic Stress…* Dissertation (2024). DOI: **10.58088/07hg-r941**. URL: https://doi.org/10.58088/07hg-r941 (lichty2024compatiblesolutesare pages 19-23)


References

1. (reang2024extremozymesandcompatible pages 1-2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 16 citations and is from a peer-reviewed journal.

2. (santoyo2024trichodermaandbacillus pages 3-4): Gustavo Santoyo, Ma. del Carmen Orozco-Mosqueda, Muhammad Siddique Afridi, Debasis Mitra, Eduardo Valencia-Cantero, and Lourdes Macías-Rodríguez. Trichoderma and bacillus multifunctional allies for plant growth and health in saline soils: recent advances and future challenges. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1423980, doi:10.3389/fmicb.2024.1423980. This article has 75 citations and is from a peer-reviewed journal.

3. (fan2024improvementinsalt pages 1-2): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

4. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 7 citations.

5. (veragargallo2023thriveorsurvive pages 1-2): Blanca Vera-Gargallo, Marcela Hernández, Marc G. Dumont, and Antonio Ventosa. Thrive or survive: prokaryotic life in hypersaline soils. Environmental Microbiome, Mar 2023. URL: https://doi.org/10.1186/s40793-023-00475-z, doi:10.1186/s40793-023-00475-z. This article has 23 citations and is from a peer-reviewed journal.

6. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

7. (fan2024improvementinsalt pages 10-12): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

8. (fan2024improvementinsalt pages 12-14): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 25 citations.

9. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius media f888d5a9): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (lichty2024compatiblesolutesare pages 19-23): Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria This article has 0 citations.

12. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

13. (zamanzadehnasrabadi2023salinitystressendurance pages 1-2): Seyyedeh Maryam Zamanzadeh-Nasrabadi, Fatemeh Mohammadiapanah, Mehdi Hosseini-Mazinani, and Sajjad Sarikhan. Salinity stress endurance of the plants with the aid of bacterial genes. Frontiers in Genetics, Apr 2023. URL: https://doi.org/10.3389/fgene.2023.1049608, doi:10.3389/fgene.2023.1049608. This article has 41 citations and is from a peer-reviewed journal.