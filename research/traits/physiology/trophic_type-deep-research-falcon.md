---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:34:18.519663'
end_time: '2026-06-18T12:55:12.026997'
duration_seconds: 1253.51
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: trophic type
  trait_identifier: METPO:1000631
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: trophic_type
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that is describing how an organism obtains carbon, energy,
    and electron donors for growth and metabolism.
  parent_traits: METPO:1000059
  synonyms: Physiology and metabolism.nutrition type.type, nutritional type, pathways
  evidence_summary: 'DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy
    source, and electron donor (Microbial physiology review frames trophic type as
    the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106:
    molecular mechanisms of adaptation (Comparative genomics supports the classification
    of bacteria by trophic strategy from genome-encoded pathways.)'
  causal_graph_summary: 'trophic_type_classification_axes: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** trophic type
- **METPO identifier:** METPO:1000631
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is describing how an organism obtains carbon, energy, and electron donors for growth and metabolism.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.nutrition type.type, nutritional type, pathways
- **Existing evidence:** DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy source, and electron donor (Microbial physiology review frames trophic type as the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106: molecular mechanisms of adaptation (Comparative genomics supports the classification of bacteria by trophic strategy from genome-encoded pathways.)
- **Existing causal graph summary:** trophic_type_classification_axes: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **trophic type** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/trophic_type.yaml`.

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
- **Trait label:** trophic type
- **METPO identifier:** METPO:1000631
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is describing how an organism obtains carbon, energy, and electron donors for growth and metabolism.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.nutrition type.type, nutritional type, pathways
- **Existing evidence:** DOI:10.1146/annurev.micro.61.080706.093130: carbon source, energy source, and electron donor (Microbial physiology review frames trophic type as the joint classification by carbon, energy, and electron-donor source.) | DOI:10.1073/pnas.0903507106: molecular mechanisms of adaptation (Comparative genomics supports the classification of bacteria by trophic strategy from genome-encoded pathways.)
- **Existing causal graph summary:** trophic_type_classification_axes: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **trophic type** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/trophic_type.yaml`.

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


## Microbial trait causal graph report: **trophic type** (METPO:1000631)

### 0. Scope summary (curation-ready)
**Trophic type** is a *composite physiological phenotype* describing how a microorganism obtains **(i) carbon for biomass, (ii) energy, and (iii) electrons/electron donors** for growth and metabolism. In practice, contemporary microbial physiology operationalizes trophic type via three orthogonal “axes” that can be recorded as trait modalities (e.g., in trait databases) and/or inferred from physiology and genomes: **energy source** (phototroph vs chemotroph), **electron donor type** (lithotroph vs organotroph), and **carbon source** (autotroph vs heterotroph; with **mixotrophy** as a boundary case when organisms can combine inorganic/organic carbon and/or litho/organo energy strategies). (laderriere2026bactotraitsatrait pages 5-6, tothero2024leptothrixochraceagenomes pages 1-2)

**Boundary cases / distinctions for curation**:
- **Mixotrophy**: organisms may encode and/or express both CO2-fixation capacity (e.g., CBB) and organic-carbon uptake/catabolism, and may couple an inorganic electron donor (e.g., Fe(II)) with organic carbon use; this should be treated as a valid trophic type rather than forced into auto vs hetero. (tothero2024leptothrixochraceagenomes pages 13-15, tothero2024leptothrixochraceagenomes pages 9-13, tothero2024leptothrixochraceagenomes pages 15-16)
- **Facultative vs obligate**: genomic potential does not guarantee expression; context (substrate availability, oxygen regime) can switch trophic mode, so edges linking environment→pathway usage are often conditional. (jahn2024theenergymetabolism pages 1-2, ramoneda2024leveraginggenomicinformation pages 1-2)
- **Not the same as “copiotroph vs oligotroph”**: that is a resource-use/ecological strategy; it can correlate with trophic type but is not the same phenotype definition. (lauro2009thegenomicbasis pages 1-2)
- **Respiration/fermentation and electron acceptors**: these are mechanistic sub-traits that condition trophic type (especially for chemotrophs) but should generally be modeled as *supporting nodes/edges* rather than the trophic type itself. (tothero2024leptothrixochraceagenomes pages 9-13, jahn2024theenergymetabolism pages 1-2)

### 1. Key concepts & current understanding (definitions)
Trait modality axes are explicitly represented in contemporary bacterial trait schemas as:
- **Source of energy**: phototroph vs chemotroph
- **Electron donor**: organotroph vs lithotroph
- **Carbon source**: autotroph vs heterotroph
These axes map directly onto the METPO definition of trophic type (carbon, energy, and electron donors). (laderriere2026bactotraitsatrait pages 5-6)

Mechanistically, genome-informed trophic typing is widely practiced: the presence (and ideally expression) of pathway-marker genes provides evidence for trophic capabilities. For example, in *Leptothrix ochracea*, iron oxidation markers (**cyc2**, **mtoA**) indicate potential to conserve energy from Fe(II) oxidation (lithotrophy), sulfur oxidation genes (**sox**) indicate additional lithotrophic potential, and **RuBisCO (rbcL/cbbM) with the full Calvin-Benson-Bassham cycle** indicates CO2 fixation capacity (autotrophy). In the same genomes, numerous sugar/organic acid uptake and catabolism genes indicate heterotrophy; together these support **mixotrophy**. (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 13-15)

### 2. Recent developments & latest research (prioritizing 2023–2024)
#### 2.1 Genome-based trophic inference validated with expression + metabolic modeling (2024)
A 2024 study reconstructed nine near-complete *L. ochracea* genomes from metagenomes and integrated **metatranscriptomics + stoichiometric metabolic models** to support a **mixotrophic iron-oxidizing** lifestyle. Marker genes for Fe(II) oxidation and aerobic respiration were highly expressed in situ, alongside organic uptake/catabolism genes and measurable CO2 fixation capacity, illustrating a modern end-to-end workflow for trophic-type inference (genes → pathways → expressed function → inferred trophic type). (tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 9-13)

#### 2.2 Experimental gene-fitness across trophic conditions in a versatile chemolithoautotroph (2024)
A 2024 barcoded transposon fitness study in *Cupriavidus necator* (a model “knallgas” bacterium) quantified how gene contributions change across **succinate, fructose, H2/CO2, and formate** growth regimes. It reports that only subsets of terminal oxidases are utilized and that **utilization depends on energy source**, highlighting that trophic mode is not just gene presence, but regulated usage under specific substrates. (jahn2024theenergymetabolism pages 1-2)

#### 2.3 Trait inference from incomplete genomes: ML prediction of KEGG metabolic modules (MetaPathPredict, 2024)
Incomplete genomes (MAGs/SAGs) are routine in environmental microbiology, creating uncertainty when building trophic-type graphs. **MetaPathPredict** (eLife, May 2024) uses deep learning to predict **KEGG module presence/absence** from incomplete annotations. Quantitatively, across **190 KEGG modules** it achieved **mean F1 ≈ 0.96** for genomes with **≥30%** estimated completeness, with degraded performance below ~30%. This is directly applicable as an “assay/computation” node that can support more robust pathway nodes for trophic-type curation from MAGs. (gellermcgrath2024predictingmetabolicmodules pages 4-6, gellermcgrath2024predictingmetabolicmodules pages 2-4)

#### 2.4 Genome-scale community metabolic modeling clarifies trophic dependencies (2024)
A Nature Communications 2024 study assembled a marine prokaryotic genome catalogue of **7,658 species-level genomes** (filtered to **5,678** meeting quality thresholds) and applied genome-scale community modeling to infer metabolic cross-feeding. It reports predicted vitamin dependencies at scale (e.g., **86%** of bacterioplankton predicted to require **cobalamin (B12)** while only **37%** encode complete biosynthesis), and finds co-active communities have significantly higher modeled interaction potential than random communities (SMETANA; p = **1.09×10⁻³**). While this is community-level, it supports adding optional context nodes/edges (auxotrophy, cross-feeding) that can modulate realized trophic roles. (giordano2024genomescalecommunitymodelling pages 1-2, giordano2024genomescalecommunitymodelling pages 7-9, giordano2024genomescalecommunitymodelling pages 9-9)

#### 2.5 Authoritative methodological cautions (2024)
A 2024 ISME Journal perspective emphasizes that genomic prediction of preferences/traits must be validated and highlights biases (training sets skewed to culturable taxa; standardized lab conditions), confounding environmental covariates, and phylogenetic signal. It recommends explicit validation on independent clades and integration of culture-based and culture-independent evidence—important warnings for curating trophic type from genomes alone. (ramoneda2024leveraginggenomicinformation pages 1-2, ramoneda2024leveraginggenomicinformation pages 4-6, ramoneda2024leveraginggenomicinformation pages 7-7)

### 3. Current applications & real-world implementations
1. **Ecosystem function inference from MAGs**: Genome-encoded marker genes for carbon fixation pathways (CBB, rTCA) and energy metabolisms (Fe/S/H2 oxidation, terminal oxidases, nitrate reduction) are routinely used to infer where photoautotrophs vs chemolithoautotrophs vs heterotrophs dominate along environmental gradients (euphotic vs aphotic; oxic vs microoxic), enabling functional biogeography and biogeochemical modeling. (bergo2026microbialsignaturesdefine pages 32-33, giordano2024genomescalecommunitymodelling pages 1-2)
2. **Bioprocess and strain engineering**: High-throughput genotype–fitness mapping across trophic regimes (e.g., H2/CO2 vs organic substrates) supports rational engineering—e.g., identifying which redundant energy-conservation complexes are actually used and where protein-cost tradeoffs make some pathways disadvantageous under certain trophic conditions. (jahn2024theenergymetabolism pages 1-2)
3. **Environmental microbiology & biogeochemistry**: Genome + expression + metabolic modeling can identify *in situ* mixotrophy and connect it to geochemical niches (e.g., Fe(II)-rich waters, microaerobic conditions), supporting mechanistic interpretation of mat formation and mineral cycling. (tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 9-13)

### 4. Candidate nodes for `trophic_type.yaml` (grouped)

#### 4.1 Trait-level nodes (phenotypes)
- trophic type (METPO:1000631)
- energy source: phototrophy vs chemotrophy (label; aligns with BactoTraits modalities) (laderriere2026bactotraitsatrait pages 5-6)
- carbon source: autotrophy vs heterotrophy vs mixotrophy (mixotrophy as boundary-case class) (tothero2024leptothrixochraceagenomes pages 13-15)
- electron donor class: lithotrophy vs organotrophy (label; aligns with BactoTraits modalities) (laderriere2026bactotraitsatrait pages 5-6)
- respiratory strategy (aerobic respiration; microaerobic respiration; nitrate respiration) (tothero2024leptothrixochraceagenomes pages 9-13, jahn2024theenergymetabolism pages 1-2)

#### 4.2 Pathways / modules
- Calvin–Benson–Bassham (CBB) cycle (KEGG module candidate) (tothero2024leptothrixochraceagenomes pages 9-13, jahn2024theenergymetabolism pages 1-2)
- reductive TCA (rTCA) cycle (KEGG module candidate) (wang2024novelisolatesof pages 12-15)
- Fe(II) oxidation module (marker-gene-based) (tothero2024leptothrixochraceagenomes pages 9-13)
- sulfur/thiosulfate oxidation via SOX (tothero2024leptothrixochraceagenomes pages 13-15)
- hydrogen oxidation (hydrogenases) (wang2024novelisolatesof pages 12-15)
- formate oxidation (formate dehydrogenase) (tothero2024leptothrixochraceagenomes pages 13-15, jahn2024theenergymetabolism pages 1-2)
- aerobic electron transport chain; terminal oxidase diversity (tothero2024leptothrixochraceagenomes pages 9-13, jahn2024theenergymetabolism pages 1-2)

#### 4.3 Genes / proteins / complexes (examples supported by evidence)
- carbon fixation: **rbcL/cbbM** (RuBisCO), CBB cycle genes; **aclAB**, **oorABCD** (rTCA) (tothero2024leptothrixochraceagenomes pages 9-13, wang2024novelisolatesof pages 12-15)
- iron oxidation: **cyc2**, **mtoA**, **cyc1**, **mofA** (tothero2024leptothrixochraceagenomes pages 9-13)
- sulfur oxidation: **soxABXYZ**, **soxCD** (tothero2024leptothrixochraceagenomes pages 13-15)
- respiration: **ccoNOPQ** (cbb3-type oxidase), **cydABX** (bd oxidase) (tothero2024leptothrixochraceagenomes pages 9-13)
- heterotrophic uptake/catabolism: **gtsABC**, **frcABC**, CAZymes (e.g., GH13/PL9), **lctP**, **ykgEFG**, **actP**, **ackA** (tothero2024leptothrixochraceagenomes pages 13-15)
- hydrogenases ([NiFe]-hydrogenase groups; label) (wang2024novelisolatesof pages 12-15)

#### 4.4 Chemicals (electron donors/acceptors; nutrients)
- carbon dioxide (CO2)
- Fe(II) (Fe2+)
- thiosulfate (S2O3^2−)
- hydrogen (H2)
- formate
- glucose, lactate, acetate (examples of organic carbon/energy sources) (tothero2024leptothrixochraceagenomes pages 13-15, jahn2024theenergymetabolism pages 1-2)
- oxygen (O2; including microaerobic regimes) (tothero2024leptothrixochraceagenomes pages 9-13)

#### 4.5 Environmental & assay factors
- genome completeness/incompleteness (MAG/SAG context)
- substrate regime (e.g., H2/CO2 vs succinate/fructose/formate) (jahn2024theenergymetabolism pages 1-2)
- oxygen availability (oxic vs microoxic) (tothero2024leptothrixochraceagenomes pages 9-13)

#### 4.6 Computational/experimental inference nodes
- KEGG module reconstruction / KEGG Ortholog presence
- MetaPathPredict (ML-based module presence inference) (gellermcgrath2024predictingmetabolicmodules pages 4-6)
- genome-scale metabolic modeling (CarveMe/SMETANA; community cross-feeding inference) (giordano2024genomescalecommunitymodelling pages 7-9)

### 5. Evidence-backed causal edges (triples)
The following table is a curation-oriented set of mechanistic edges that can be translated into YAML edges (subject–predicate–object), with grounding suggestions, supporting snippets, and uncertainty notes.

| Edge (subject–predicate–object) | Entity type(s) | Ontology grounding suggestions | Evidence snippet | Source (DOI + URL + publication month/year) | Notes/uncertainty |
|---|---|---|---|---|---|
| Form II RuBisCO (rbcL/cbbM) + Calvin-Benson-Bassham cycle → enables → CO2 fixation / autotrophic carbon assimilation | gene, pathway, chemical, trait | GO:0015977 carbon fixation; EC:4.1.1.39 RuBisCO; KEGG:M00165 Calvin cycle; CHEBI:16526 carbon dioxide | “all MAGs encode Form II RuBisCO (rbcL/cbbM) and a full CBB cycle, indicating CO2 fixation potential” | 10.1128/AEM.00599-24; https://doi.org/10.1128/AEM.00599-24; Sep 2024 | Strong mechanistic marker for autotrophic potential; in *L. ochracea* authors interpret overall lifestyle as mixotrophic because organic uptake pathways are also present (tothero2024leptothrixochraceagenomes pages 9-13, tothero2024leptothrixochraceagenomes pages 1-2) |
| cyc2 / mtoA iron oxidase genes → enable → Fe(II) oxidation for energy conservation | gene, pathway, chemical, trait | Label: cyc2; Label: mtoA; CHEBI:29033 Fe2+; GO:0015976 carbon utilization?; label-only “iron oxidation” if no stable term chosen | “iron oxidase genes cyc2 and mtoA indicate potential to conserve energy from Fe(II) oxidation” | 10.1128/AEM.00599-24; https://doi.org/10.1128/AEM.00599-24; Sep 2024 | Strong for taxon-specific inference in iron oxidizers; supports chemolithotrophic electron-donor axis rather than carbon-source axis (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 9-13) |
| cbb3-type cytochrome c oxidase (ccoNOPQ) → supports → microaerobic aerobic respiration | gene complex, process, environment | GO:0004129 cytochrome-c oxidase activity; GO:0019646 aerobic electron transport chain; ENVO:01001305 microaerobic environment (candidate) | “Terminal oxidases (cbb3-type ccoNOPQ and cytochrome bd cydABX) are high-affinity oxygen consumers associated with microaerobic respiration” | 10.1128/AEM.00599-24; https://doi.org/10.1128/AEM.00599-24; Sep 2024 | Good edge for environment-linked respiratory mode; oxygen niche inference remains context-dependent (tothero2024leptothrixochraceagenomes pages 9-13) |
| soxABXYZ / soxCD sulfur oxidation genes → enable → thiosulfate/sulfur oxidation as electron-donor use | gene cluster, pathway, chemical, trait | KEGG sulfur oxidation pathway; CHEBI:9567 thiosulfate(2-); GO:0009377? sulfur compound metabolic process (candidate label if needed) | “Presence of soxABXYZ (and soxCD) is tied to thiosulfate oxidation, explicitly described as enabling use of sulfur species as electron donors” | 10.1128/AEM.00599-24; https://doi.org/10.1128/AEM.00599-24; Sep 2024 | Strong for sulfur-based lithotrophic potential; exact sulfur substrate may vary by taxon/system (tothero2024leptothrixochraceagenomes pages 13-15, tothero2024leptothrixochraceagenomes pages 1-2) |
| Sugar transporters (gtsABC, frcABC), maltodextrin import/degradation, CAZymes → enable → heterotrophic utilization of sugars/polysaccharides | genes, transporters, enzymes, chemicals, trait | Label: gtsABC; Label: frcABC; CAZy labels GH13, PL9; CHEBI:17234 glucose; CHEBI:16646 carbohydrates | “Genes for glycolysis, gluconeogenesis, diverse sugar transporters (gtsABC, frcABC), maltodextrin import/degradation and CAZy enzymes … indicate capacity for heterotrophic/organotrophic use of simple sugars and polysaccharides.” | 10.1128/AEM.00599-24; https://doi.org/10.1128/AEM.00599-24; Sep 2024 | Strong evidence for heterotrophic carbon-source use; curate as broad organic-carbon utilization rather than specific substrate unless needed (tothero2024leptothrixochraceagenomes pages 13-15) |
| Absence of [NiFe]-hydrogenases in *L. ochracea* → suggests absence of → H2 lithotrophy | gene family absence, trait | [NiFe]-hydrogenase (label); CHEBI:18276 hydrogen | “Absence of [NiFe]-hydrogenases is noted, indicating lack of hydrogen lithotrophy in L. ochracea.” | 10.1128/AEM.00599-24; https://doi.org/10.1128/AEM.00599-24; Sep 2024 | Negative inference; taxon-specific and absence-based, so curate as uncertain/conditional rather than universal rule (tothero2024leptothrixochraceagenomes pages 13-15) |
| rTCA genes aclAB and oorABCD → enable → CO2 fixation in *Sulfurospirillum* strain 1612 | genes, pathway, chemical, trait | KEGG reductive TCA cycle; EC:2.3.3.8 ATP-citrate lyase; EC:1.2.7.3 2-oxoglutarate:ferredoxin oxidoreductase; CHEBI:16526 carbon dioxide | “The genome of strain 1612 harbored characteristic enzyme genes of rTCA cycle for CO2 fixation (encoded by genes aclAB and oorABCD)...supporting the potential of chemoautotrophy.” | 10.1128/mSystems.00148-24; https://doi.org/10.1128/mSystems.00148-24; Sep 2024 | Strong but taxon-specific example showing a non-CBB autotrophic module for trophic typing (wang2024novelisolatesof pages 12-15) |
| [NiFe]-hydrogenase genes → enable → H2 oxidation / hydrogen lithotrophy | gene family, pathway, chemical, trait | [NiFe]-hydrogenase (label); CHEBI:18276 hydrogen; GO:0008137 NADH dehydrogenase? better label-only if uncertain | “hydrogenase and nitrate reductase genes are noted, linking sulfur- and hydrogen-based lithotrophy and respiratory capabilities to chemoautotrophic metabolism” | 10.1128/mSystems.00148-24; https://doi.org/10.1128/mSystems.00148-24; Sep 2024 | Strong for *Sulfurospirillum* example; subtype-specific roles may differ across hydrogenase groups (wang2024novelisolatesof pages 12-15) |
| Energy substrate identity (succinate, fructose, H2/CO2, formic acid) → determines → terminal oxidase utilization in *Cupriavidus necator* | environmental/experimental factor, genes/complexes, process | Label: bo3/bd/bc1/bb3/cbb3/aa3 oxidases; GO:0019646 aerobic electron transport chain; CHEBI:18276 hydrogen; CHEBI:15740 formate | “Of the six terminal respiratory complexes in C. necator H16, only some are utilized, and utilization depends on the energy source.” | 10.1128/AEM.00748-24; https://doi.org/10.1128/AEM.00748-24; Oct 2024 | Important causal edge linking assay substrate context to respiratory machinery usage; species-specific but conceptually broad (jahn2024theenergymetabolism pages 1-2) |
| MetaPathPredict deep-learning KEGG module inference → improves → metabolic-module prediction from incomplete genomes | computational method, pathway/module inference | KEGG modules (general); label: MetaPathPredict | “Across 190 modules, MetaPathPredict achieved an average F1 of 0.96 on held-out genomes with estimated completeness ≥30%.” | 10.7554/eLife.85749; https://doi.org/10.7554/eLife.85749; May 2024 | Not a biological causal edge; useful as evidence pipeline/assay-method node for TraitMech curation provenance. Performance degrades below ~30–40% completeness (gellermcgrath2024predictingmetabolicmodules pages 6-9, gellermcgrath2024predictingmetabolicmodules pages 4-6) |
| Cobalamin (B12) auxotrophy / incomplete biosynthesis → promotes → community cross-feeding interactions | pathway deficiency, cofactor, community process | CHEBI:176843 cobalamin; label: cobalamin biosynthesis module; GO:0042558 pterin-containing compound metabolic process? label acceptable | “predicted that 86% of them require the cofactor, while only 37% encode a complete biosynthetic potential” | 10.1038/s41467-024-46374-w; https://doi.org/10.1038/s41467-024-46374-w; Mar 2024 | Strong community-scale ecological mechanism, but indirect for single-organism trophic type; better as optional environment/community-context edge (giordano2024genomescalecommunitymodelling pages 7-9, giordano2024genomescalecommunitymodelling pages 9-9) |
| Smaller genomes + metabolic auxotrophies → increase dependence on → metabolic cross-feeding in co-active communities | genome feature, community process | Label-only candidate nodes | “genome streamlining together with metabolic auxotrophies likely act jointly to shape bacterioplankton community assembly” | 10.1038/s41467-024-46374-w; https://doi.org/10.1038/s41467-024-46374-w; Mar 2024 | Broad ecological edge; useful for contextual graph expansion but not a direct trophic-type determinant for an isolate (giordano2024genomescalecommunitymodelling pages 1-2, giordano2024genomescalecommunitymodelling pages 9-9) |


*Table: This table lists curation-ready candidate causal edges for microbial trophic type, linking genes, pathways, substrates, environments, and computational inference methods to trophic strategies. It is useful as a starting point for TraitMech graph construction because each edge includes grounding suggestions, evidence snippets, sources, and uncertainty notes.*

### 6. Visual evidence (figures/tables)
- Tothero et al. 2024 provide (i) a table-style summary of marker genes for trophic capabilities across *Leptothrix–Sphaerotilus* genomes and (ii) a schematic metabolic model for *L. ochracea* supporting mixotrophy (Fe(II) oxidation + organic carbon use + CO2 fixation). These were retrieved as cropped figure/table images. (tothero2024leptothrixochraceagenomes media 598361f9, tothero2024leptothrixochraceagenomes media 733c958a)

### 7. Quantitative statistics & recent data points (from retrieved sources)
- **MetaPathPredict (eLife 2024)**: across **190** KEGG modules, **mean F1 ≈ 0.96** for held-out genomes with estimated completeness **≥30%**; performance degrades strongly below ~30%. (gellermcgrath2024predictingmetabolicmodules pages 4-6)
- **Marine community modeling (Nat Commun 2024)**: genome catalogue size **7,658** species-level genomes (filtered to **5,678** high-quality); SMETANA shows co-active communities have higher interaction potential than random (p = **1.09×10⁻³**). (giordano2024genomescalecommunitymodelling pages 1-2, giordano2024genomescalecommunitymodelling pages 7-9)
- **Vitamin dependency statistic (Nat Commun 2024)**: **86%** predicted to require cobalamin while only **37%** encode complete biosynthesis potential (supports community-level auxotrophy/cross-feeding nodes). (giordano2024genomescalecommunitymodelling pages 7-9, giordano2024genomescalecommunitymodelling pages 9-9)

### 8. Expert opinion / authoritative analysis (limitations & curation cautions)
- Genome-based inference is powerful but must be validated; biases in reference genomes and standardized culture conditions can distort trait prediction, and confounding environmental factors and biotic interactions can break the assumption that abundance reflects growth. Recommended safeguards include testing phylogenetic signal, using out-of-clade validation, and integrating culture-based and culture-independent evidence. (ramoneda2024leveraginggenomicinformation pages 1-2, ramoneda2024leveraginggenomicinformation pages 4-6, ramoneda2024leveraginggenomicinformation pages 7-7)
- For trophic type specifically, **gene presence does not equal realized trophic mode**: substrate identity can change which respiratory complexes are used (and which genes are fitness-critical) even within one organism, motivating explicit “assay condition” nodes in TraitMech graphs. (jahn2024theenergymetabolism pages 1-2)

### 9. Warnings (do-not-curate / curate-as-uncertain)
1. **Absence-based inference** (e.g., “no hydrogenases → cannot use H2”) should generally be tagged **uncertain**, especially for incomplete genomes and annotation gaps; curate only if genome quality is high and the claim is taxon-specific. (tothero2024leptothrixochraceagenomes pages 13-15, gellermcgrath2024predictingmetabolicmodules pages 4-6)
2. **Pathway presence without expression/physiology**: CBB/rTCA genes indicate potential CO2 fixation, but realized autotrophy depends on energy/redox context; where possible, require transcriptomics/fitness/uptake evidence or model constraints. (tothero2024leptothrixochraceagenomes pages 9-13, jahn2024theenergymetabolism pages 1-2)
3. **Community-level dependencies** (vitamin auxotrophy/cross-feeding) modulate realized ecological roles but are not equivalent to single-organism trophic type; curate as optional context layers. (giordano2024genomescalecommunitymodelling pages 7-9, giordano2024genomescalecommunitymodelling pages 9-9)
4. **Predictive tools and model outputs** (MetaPathPredict, SMETANA) are best represented as inference/provenance nodes rather than biological causality, unless explicitly validated experimentally. (gellermcgrath2024predictingmetabolicmodules pages 4-6, giordano2024genomescalecommunitymodelling pages 7-9)

---

## DOI-first bibliography (with URLs; publication dates)

1. **Tothero GK, et al.** *Leptothrix ochracea genomes reveal potential for mixotrophic growth on Fe(II) and organic carbon.* **Applied and Environmental Microbiology** (Sep 2024). DOI: **10.1128/aem.00599-24**. URL: https://doi.org/10.1128/aem.00599-24 (tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 9-13)
2. **Jahn M, et al.** *The energy metabolism of Cupriavidus necator in different trophic conditions.* **Applied and Environmental Microbiology** (Oct 2024). DOI: **10.1128/aem.00748-24**. URL: https://doi.org/10.1128/aem.00748-24 (jahn2024theenergymetabolism pages 1-2)
3. **Wang L, et al.** *Novel isolates of hydrogen-oxidizing chemolithoautotrophic Sulfurospirillum…* **mSystems** (Sep 2024). DOI: **10.1128/msystems.00148-24**. URL: https://doi.org/10.1128/msystems.00148-24 (wang2024novelisolatesof pages 12-15)
4. **Geller‑McGrath D, et al.** *Predicting metabolic modules in incomplete bacterial genomes with MetaPathPredict.* **eLife** (May 2024). DOI: **10.7554/eLife.85749**. URL: https://doi.org/10.7554/eLife.85749 (gellermcgrath2024predictingmetabolicmodules pages 4-6)
5. **Giordano N, et al.** *Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities.* **Nature Communications** (Mar 2024). DOI: **10.1038/s41467-024-46374-w**. URL: https://doi.org/10.1038/s41467-024-46374-w (giordano2024genomescalecommunitymodelling pages 1-2, giordano2024genomescalecommunitymodelling pages 7-9)
6. **Ramoneda J, et al.** *Leveraging genomic information to predict environmental preferences of bacteria.* **The ISME Journal** (Jan 2024). DOI: **10.1093/ismejo/wrae195**. URL: https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 1-2, ramoneda2024leveraginggenomicinformation pages 4-6)

Additional context sources retrieved (not central to mechanistic edge curation):
- **Laderriere V, et al.** *BactoTraits: a trait database…* **Scientific Data** (Feb 2026). DOI: 10.1038/s41597-026-06652-2. URL: https://doi.org/10.1038/s41597-026-06652-2 (trait-axis modalities used) (laderriere2026bactotraitsatrait pages 5-6)
- **Lauro FM, et al.** *The genomic basis of trophic strategy in marine bacteria.* **PNAS** (Sep 2009). DOI: 10.1073/pnas.0903507106. URL: https://doi.org/10.1073/pnas.0903507106 (copiotroph vs oligotroph distinction) (lauro2009thegenomicbasis pages 1-2)


References

1. (laderriere2026bactotraitsatrait pages 5-6): Vincent Laderriere, Philippe Usseglio-Polatera, Florence Maunoury‐Danger, and Aurélie Cébron. Bactotraits: a trait database for exploring functional diversity of bacterial communities. Scientific Data, Feb 2026. URL: https://doi.org/10.1038/s41597-026-06652-2, doi:10.1038/s41597-026-06652-2. This article has 0 citations and is from a peer-reviewed journal.

2. (tothero2024leptothrixochraceagenomes pages 1-2): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

3. (tothero2024leptothrixochraceagenomes pages 13-15): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

4. (tothero2024leptothrixochraceagenomes pages 9-13): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

5. (tothero2024leptothrixochraceagenomes pages 15-16): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

6. (jahn2024theenergymetabolism pages 1-2): Michael Jahn, Nick Crang, Arvid H. Gynnå, Deria Kabova, Stefan Frielingsdorf, Oliver Lenz, Emmanuelle Charpentier, and Elton P. Hudson. The energy metabolism of <i>cupriavidus necator</i> in different trophic conditions. Oct 2024. URL: https://doi.org/10.1128/aem.00748-24, doi:10.1128/aem.00748-24. This article has 39 citations and is from a peer-reviewed journal.

7. (ramoneda2024leveraginggenomicinformation pages 1-2): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

8. (lauro2009thegenomicbasis pages 1-2): Federico M. Lauro, Diane McDougald, Torsten Thomas, Timothy J. Williams, Suhelen Egan, Scott Rice, Matthew Z. DeMaere, Lily Ting, Haluk Ertan, Justin Johnson, Steven Ferriera, Alla Lapidus, Iain Anderson, Nikos Kyrpides, A. Christine Munk, Chris Detter, Cliff S. Han, Mark V. Brown, Frank T. Robb, Staffan Kjelleberg, and Ricardo Cavicchioli. The genomic basis of trophic strategy in marine bacteria. Proceedings of the National Academy of Sciences, 106:15527-15533, Sep 2009. URL: https://doi.org/10.1073/pnas.0903507106, doi:10.1073/pnas.0903507106. This article has 859 citations and is from a highest quality peer-reviewed journal.

9. (gellermcgrath2024predictingmetabolicmodules pages 4-6): David Geller-McGrath, Kishori M Konwar, Virginia P Edgcomb, Maria Pachiadaki, Jack W Roddy, Travis J Wheeler, and Jason E McDermott. Predicting metabolic modules in incomplete bacterial genomes with metapathpredict. eLife, May 2024. URL: https://doi.org/10.7554/elife.85749, doi:10.7554/elife.85749. This article has 13 citations and is from a domain leading peer-reviewed journal.

10. (gellermcgrath2024predictingmetabolicmodules pages 2-4): David Geller-McGrath, Kishori M Konwar, Virginia P Edgcomb, Maria Pachiadaki, Jack W Roddy, Travis J Wheeler, and Jason E McDermott. Predicting metabolic modules in incomplete bacterial genomes with metapathpredict. eLife, May 2024. URL: https://doi.org/10.7554/elife.85749, doi:10.7554/elife.85749. This article has 13 citations and is from a domain leading peer-reviewed journal.

11. (giordano2024genomescalecommunitymodelling pages 1-2): Nils Giordano, Marinna Gaudin, Camille Trottier, Erwan Delage, Charlotte Nef, Chris Bowler, and Samuel Chaffron. Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46374-w, doi:10.1038/s41467-024-46374-w. This article has 76 citations and is from a highest quality peer-reviewed journal.

12. (giordano2024genomescalecommunitymodelling pages 7-9): Nils Giordano, Marinna Gaudin, Camille Trottier, Erwan Delage, Charlotte Nef, Chris Bowler, and Samuel Chaffron. Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46374-w, doi:10.1038/s41467-024-46374-w. This article has 76 citations and is from a highest quality peer-reviewed journal.

13. (giordano2024genomescalecommunitymodelling pages 9-9): Nils Giordano, Marinna Gaudin, Camille Trottier, Erwan Delage, Charlotte Nef, Chris Bowler, and Samuel Chaffron. Genome-scale community modelling reveals conserved metabolic cross-feedings in epipelagic bacterioplankton communities. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46374-w, doi:10.1038/s41467-024-46374-w. This article has 76 citations and is from a highest quality peer-reviewed journal.

14. (ramoneda2024leveraginggenomicinformation pages 4-6): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

15. (ramoneda2024leveraginggenomicinformation pages 7-7): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

16. (bergo2026microbialsignaturesdefine pages 32-33): Natascha M. Bergo, Francielli Vilela Peres, Danilo Candido Vieira, Flúvio Mondolon, Julio Cezar Fornazier Moreira, Rebeca Graciela Matheus Lizárraga, Amanda Goncalves Bendia, Leandro Nascimento Lemos, Alice de Moura Emilio, Augusto Miliorini Amendola, Diana Carolina Duque Castano, Mateus Gustavo Chuqui, Fabiana da Silva Paula, Renato Gamba Romano, William Soares Gattaz Brandão, Gustavo Fonseca, Daniel Moreira, Célio Roberto Jonck, Ana Tereza R Vasconcelos, Frederico P. Brandini, and Vivian H. Pellizari. Microbial signatures define the ecosystem functions of the pelagic microbiome in a basin-scale, southwest atlantic ocean. bioRxiv, Mar 2026. URL: https://doi.org/10.1101/2025.03.17.643744, doi:10.1101/2025.03.17.643744. This article has 1 citations.

17. (wang2024novelisolatesof pages 12-15): Li Wang, Xinyi Cheng, Yi-Yang Guo, Junwei Cao, Mingye Sun, Jiang-Shiou Hwang, Rulong Liu, and Jiasong Fang. Novel isolates of hydrogen-oxidizing chemolithoautotrophic <i>sulfurospirillum</i> provide insight to the functions and adaptation mechanisms of campylobacteria in shallow-water hydrothermal vents. Sep 2024. URL: https://doi.org/10.1128/msystems.00148-24, doi:10.1128/msystems.00148-24. This article has 7 citations and is from a peer-reviewed journal.

18. (gellermcgrath2024predictingmetabolicmodules pages 6-9): David Geller-McGrath, Kishori M Konwar, Virginia P Edgcomb, Maria Pachiadaki, Jack W Roddy, Travis J Wheeler, and Jason E McDermott. Predicting metabolic modules in incomplete bacterial genomes with metapathpredict. eLife, May 2024. URL: https://doi.org/10.7554/elife.85749, doi:10.7554/elife.85749. This article has 13 citations and is from a domain leading peer-reviewed journal.

19. (tothero2024leptothrixochraceagenomes media 598361f9): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

20. (tothero2024leptothrixochraceagenomes media 733c958a): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.