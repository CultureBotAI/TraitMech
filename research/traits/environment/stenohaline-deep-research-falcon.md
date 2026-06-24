---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:28:56.413660'
end_time: '2026-06-18T01:59:34.479223'
duration_seconds: 1838.07
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: stenohaline
  trait_identifier: METPO:1000626
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: stenohaline
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism can only tolerate a narrow
    range of salinity concentrations and cannot survive significant changes in environmental
    salt levels.
  parent_traits: METPO:1000629
  synonyms: ''
  evidence_summary: 'DOI:10.1186/s40168-024-01817-w: narrow range of salinity (Supports
    stenohaline microorganisms as organisms thriving within a narrow salinity range.)'
  causal_graph_summary: 'stenohaline_narrow_salinity_tolerance: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** stenohaline
- **METPO identifier:** METPO:1000626
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can only tolerate a narrow range of salinity concentrations and cannot survive significant changes in environmental salt levels.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/s40168-024-01817-w: narrow range of salinity (Supports stenohaline microorganisms as organisms thriving within a narrow salinity range.)
- **Existing causal graph summary:** stenohaline_narrow_salinity_tolerance: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **stenohaline** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/stenohaline.yaml`.

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
- **Trait label:** stenohaline
- **METPO identifier:** METPO:1000626
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can only tolerate a narrow range of salinity concentrations and cannot survive significant changes in environmental salt levels.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1186/s40168-024-01817-w: narrow range of salinity (Supports stenohaline microorganisms as organisms thriving within a narrow salinity range.)
- **Existing causal graph summary:** stenohaline_narrow_salinity_tolerance: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **stenohaline** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/stenohaline.yaml`.

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


## Microbial trait causal-graph curation report: **stenohaline** (METPO:1000626)

### 0) Scope summary (curation-ready)
**Stenohaline** (METPO:1000626) is best treated as an **environmental-niche breadth trait** describing microorganisms whose growth, survival, or ecological dominance is restricted to a **narrow salinity window**, in contrast to **euryhaline** organisms that tolerate or adapt to **wide and/or rapid salinity fluctuations**. In microbial ecology, this may be measured (i) by **growth/viability assays across salinity gradients** (e.g., culture-based growth curves, spore germination) or (ii) operationally by **abundance restriction to one salinity regime** in field gradients, especially where genome-resolved metagenomics can connect abundance patterns to genomic features. (wu2024metagenomicinsightsinto pages 1-2, velez2019impactofsalinity pages 1-3)

A recent, explicit microbial operationalization defines **stenohaline MAGs** as those whose **average relative abundance in one salinity category exceeds the other two by ~10×**, with remaining MAGs labeled **euryhaline**. This definition is useful for TraitMech curation because it encodes an assay/decision rule, but it should be represented as an **operational classification node** rather than as a universal biological definition. (wu2024metagenomicinsightsinto pages 1-2)

**Boundary cases:** estuaries create continuous gradients where “intermediate” communities can overlap with high-salinity profiles more than low-salinity profiles, and multiple ecotypes can co-occur; thus, stenohaly can be context- and sampling-dependent (season/residence time/gradient resolution). (wu2024metagenomicinsightsinto pages 7-9, wu2024metagenomicinsightsinto pages 2-4)

**Related terms (with evidence limits):**
- **Halophile / hypersaline context:** hypersaline environments are defined by Oren (2024) as **>100–150 g/L salts**, and “halophiles” are organisms capable of growing at **>100–150 g/L dissolved salts**. (oren2024novelinsightsinto pages 1-2)
- A consistent definition for **halotolerant** vs **halophilic** is not fully established in the 2023–2024 corpus retrieved here; however, a 2025 preprint proposes NaCl-optimum thresholds (halotolerant optimum <0.6 M NaCl; slight 0.6–1.2 M; moderate 1.2–2.2 M; extreme >2.2 M). Because this source is a preprint, it should be used cautiously in ontology-level curation. (schiavo2025proposalfornew pages 4-7)

---

### 1) Recent developments & latest research (priority 2023–2024)
#### 1.1 Genome-resolved metagenomics links stenohaline categories to osmoregulation features (Microbiome 2024)
Wu et al. (2024) analyzed a Pearl River Estuary salinity gradient (0.12‰–34‰) and reconstructed **127 MAGs**; they categorized MAGs into stenohaline (low/intermediate/high) versus euryhaline using a **10× relative-abundance rule** across salinity bins. (wu2024metagenomicinsightsinto pages 2-4, wu2024metagenomicinsightsinto pages 1-2)

Key quantitative outputs (curation-friendly):
- MAG totals and quality: **127 MAGs** (116 Bacteria, 11 Archaea); 25 high-quality (≥90% completeness, ≤5% contamination) and 102 medium-quality (≥50% completeness, ≤10% contamination). (wu2024metagenomicinsightsinto pages 7-9)
- Stenohaline counts: **33 low-salinity**, **36 intermediate-salinity**, **44 high-salinity** stenohaline MAGs; **14 euryhaline** MAGs. (wu2024metagenomicinsightsinto pages 7-9)
- Feature selection: from **~12,162 COGs**, **40** were identified as important (Boruta), with “inorganic ion transport and metabolism” prominent; **8 COGs** were implicated in osmoregulation (4 “salt-in”, 3 “salt-out”, 1 water-channel regulation). (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 7-9)
- The **top-ranked** osmoregulation feature was **COG0168 (Trk-type K+ transporter)** whose relative abundance increased with salinity. (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 11-13)

Mechanistic interpretation: the work supports two broad strategies—**salt-in** (inorganic ion transport, especially K+ uptake systems) and **salt-out** (compatible-solute uptake/transport signatures)—as differentiators among stenohaline categories. (wu2024metagenomicinsightsinto pages 13-14, wu2024metagenomicinsightsinto pages 11-13)

Figures supporting the salinity-trend claims were retrieved for curation review (Boruta ranking and COG-abundance vs salinity plots). (wu2024metagenomicinsightsinto media 3c6a53f2)

#### 1.2 Master regulation of osmolyte flux by cyclic di-AMP (MMBR 2024)
Foster et al. (2024) synthesize evidence that **cyclic di-AMP (c-di-AMP)** is a “master regulator” of cell volume and osmoadaptation, primarily by **inhibiting K+ import and compatible-solute uptake** and coordinating these fluxes with envelope remodeling and survival under osmotic transitions. (foster2024bacterialcellvolume pages 31-33, foster2024bacterialcellvolume pages 13-16)

Specific, curation-usable targets include:
- K+ transport regulation via binding to gating/transport components of **Trk/Ktr** systems and transcriptional repression of **Kdp**; inhibition of KUP family importers such as **KimA**; and effects on exporters. (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)
- Compatible solute import regulation: c-di-AMP binds CBS-domain compatible-solute importers (e.g., **OpuA/OpuC/OpuD**) and also acts through regulators such as **BusR** to reduce opuA transcription and glycine betaine uptake. (foster2024bacterialcellvolume pages 10-12)
- Rapid downshock protection: mechanosensitive channels provide a fast release route for osmolytes and water, complementing slower regulatory control of uptake/efflux. (foster2024bacterialcellvolume pages 13-16)

This review provides authoritative “expert opinion” suitable for defining mechanistic nodes and regulatory edges that could underlie narrow versus broad salinity tolerance phenotypes (while not claiming stenohaly per se). (foster2024bacterialcellvolume pages 31-33)

#### 1.3 Quantitative metabolite evidence for compatible-solute accumulation under high salinity (AEM 2024)
Xing et al. (2024) used proteomics/transcript validation and direct metabolite measurements to show that the polyextremophile *Natranaerobius thermophilus* uses a **hybrid strategy** combining ion homeostasis and compatible-solute accumulation at long-term high salinity (2.5–4.3 M Na+). (xing2024thepolyextremophilenatranaerobius pages 1-2)

Quantitative compatible solute data (2.5 → 4.3 M Na+):
- Glycine betaine: **52.7 mM → 893.1 mM**
- L-glutamate: **11.0 mM → 221.3 mM**
- Proline: minimum **67.0 mM** at 3.1 M; peak **130 mM** at 4.3 M
(xing2024thepolyextremophilenatranaerobius pages 17-19)

Transporter/antiporter signals include upregulation of **trkH** and a **nhaC** Na+/H+ antiporter at higher salinities, supporting ion-homeostasis as part of salt tolerance. (xing2024thepolyextremophilenatranaerobius pages 6-7)

#### 1.4 Osmotic stress effectors in Actinobacteria models (microLife 2023)
Bhowmick et al. (2023) review osmotic stress responses in *Streptomyces* and provide concrete examples of:
- Encoded **mechanosensitive channels** (MscL/MscS families) and **aquaporins/aquaporin-like proteins** (gene IDs in *S. venezuelae*) (bhowmick2023osmoticstressresponses pages 3-4)
- Physiological responses including **rapid K+ changes** (emergency response) followed by **compatible-solute (salt-out) accumulation**, with a quantitative example: proline rising to ~50% of the free amino acid pool at 1 M salt in *S. griseus*. (bhowmick2023osmoticstressresponses pages 3-4)
- A regulatory module connecting c-di-AMP to a putative K+/H+ antiporter system (CpeAB homologous to KhtTUS). (bhowmick2023osmoticstressresponses pages 7-8)

---

### 2) Current applications & real-world implementations (salinity-tolerance context)
Although stenohaline itself is primarily an ecological/physiological descriptor, it is relevant in practice wherever salinity varies:
- **Estuary monitoring and prediction:** genome-resolved models can classify microbes as stenohaline vs euryhaline and identify salinity-linked genomic markers (e.g., Trk-type K+ transport) that may improve forecasting of community shifts along salinity gradients. (wu2024metagenomicinsightsinto pages 7-9, wu2024metagenomicinsightsinto pages 1-2)
- **Industrial/high-salt biotechnology context:** Oren (2024) defines hypersaline systems (>100–150 g/L salts) and surveys expanding diversity/metabolism in such ecosystems, which underpins bioprospecting for salt-adapted pathways and enzymes. (oren2024novelinsightsinto pages 1-2)
- **Stress management for engineered cultures:** the c-di-AMP framework highlights a mechanistic axis—tight control of K+ and compatible solute influx—to prevent lysis or growth defects, a principle relevant to stabilizing production strains across osmotic fluctuations. (foster2024bacterialcellvolume pages 13-16, foster2024bacterialcellvolume pages 31-33)

---

### 3) Candidate nodes for `stenohaline.yaml` (grouped by type)

#### 3.1 Trait / operational nodes
- **stenohaline** (METPO:1000626)
- **euryhaline** (label-only; not provided as CURIE in evidence)
- **Operational classification rule:** “MAG is stenohaline if mean relative abundance in one salinity bin is >10× the other bins” (label-only) (wu2024metagenomicinsightsinto pages 1-2)
- **Salinity bins / regimes:** low salinity; intermediate salinity; high salinity (label-only) (wu2024metagenomicinsightsinto pages 7-9)

#### 3.2 Environmental / experimental factor nodes
- **salinity gradient** (ENVO salinity term not retrieved as CURIE; use label or ENVO:00002009 salinity as candidate)
- **estuary** (ENVO candidate label; Pearl River Estuary context) (wu2024metagenomicinsightsinto pages 2-4)
- **hypersaline environment** (defined as >100–150 g/L salts) (oren2024novelinsightsinto pages 1-2)

#### 3.3 Genes/proteins/complexes (candidate mechanistic nodes)
**From Wu 2024 COGs (genome-resolved markers):**
- **COG0168** Trk-type K+ transporter (salt-in) (wu2024metagenomicinsightsinto pages 1-2)
- **COG3158** Kup-type K+ transporter (salt-in; low-salinity-associated) (wu2024metagenomicinsightsinto pages 11-13)
- **COG0530** Ca2+:K+/Na+ antiporter (salt-in) (wu2024metagenomicinsightsinto pages 11-13)
- **COG0038** Cl− channel (salt-in associated) (wu2024metagenomicinsightsinto pages 11-13)
- **COG0477** ProP-family MFS transporter (compatible-solute uptake; salt-out associated) (wu2024metagenomicinsightsinto pages 14-16)
- **COG0591** “symporter activity” (salt-out associated; substrate unspecified) (wu2024metagenomicinsightsinto pages 11-13)
- **COG1115** amino acid carrier (salt-out associated; substrate unspecified) (wu2024metagenomicinsightsinto pages 11-13)
- **COG0580** water channel / aquaporin activity (GO:0015250) (wu2024metagenomicinsightsinto pages 13-14)

**From Foster 2024 c-di-AMP network:**
- **c-di-AMP** (CHEBI:16761)
- **KtrAB/KtrCD / Trk systems**, **Kdp** system, **KimA/Kup** family (label-level nodes unless curated by specific gene IDs) (foster2024bacterialcellvolume pages 6-8, foster2024bacterialcellvolume pages 8-10)
- **OpuA/OpuC/OpuD** compatible-solute importers; **BusR** transcriptional regulator (foster2024bacterialcellvolume pages 10-12)
- **Mechanosensitive channels** (GO:0015288 mechanosensitive ion channel activity) (foster2024bacterialcellvolume pages 13-16)

**From Bhowmick 2023 (taxon-specific exemplars):**
- **MscL/MscS** mechanosensitive channels (bhowmick2023osmoticstressresponses pages 3-4)
- **Aquaporins** (GO:0015250) (bhowmick2023osmoticstressresponses pages 3-4)
- **CpeAB** (putative K+/H+ antiporter system regulated by c-di-AMP; label-only) (bhowmick2023osmoticstressresponses pages 7-8)

**From Xing 2024 (quantitative, taxon-specific exemplars):**
- **trkH** (K+ uptake component) (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **nhaC** Na+/H+ antiporter (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **Opu/ProU** families (glycine betaine ABC transporters; label-level) (xing2024thepolyextremophilenatranaerobius pages 1-2)

#### 3.4 Chemicals/metabolites (compatible solutes and ions)
- **K+** (CHEBI:29103 potassium(1+)) (bhowmick2023osmoticstressresponses pages 3-4)
- **Na+** (CHEBI:29101 sodium(1+)) (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **Glycine betaine** (CHEBI:17750) (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **L-glutamate** (CHEBI:29985) (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **L-proline** (CHEBI:17203) (xing2024thepolyextremophilenatranaerobius pages 17-19)
- **Trehalose** (CHEBI:16551) (foster2024bacterialcellvolume pages 6-8)
- **Ectoine** (CHEBI:30913) (wu2024metagenomicinsightsinto pages 14-16)

#### 3.5 Biological processes / molecular functions
- **osmoadaptation / osmoregulation** (label-only)
- **water channel activity** (GO:0015250) (wu2024metagenomicinsightsinto pages 13-14)
- **mechanosensitive channel activity** (GO:0015288) (foster2024bacterialcellvolume pages 13-16)

---

### 4) Evidence-backed candidate causal edges (table)
The table below enumerates candidate subject–predicate–object edges with supporting snippets, notes, and grounding suggestions.

| Edge (subject–predicate–object) | Edge type (mechanistic/operational) | Suggested ontology grounding (CURIEs for subject/object when available) | Evidence source (first author year, DOI) | Publication date (month year) | Supporting snippet (short quote) | Notes/limitations/uncertainty |
|---|---|---|---|---|---|---|
| stenohaline microorganism → has_salinity_preference → narrow salinity range | operational | subject: METPO:1000626; object: label-only candidate “narrow salinity range” | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “'stenohaline' organisms… thrive within a narrow salinity range” (wu2024metagenomicinsightsinto pages 1-2) | Core trait definition; ecological/operational rather than molecular. |
| MAG with average relative abundance in one salinity category >10× the other two → operationally_classified_as → stenohaline | operational | subject: label-only candidate “MAG abundance rule”; object: METPO:1000626 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “classified as stenohaline when their average relative abundance in one salinity category exceeded the others by an order of magnitude” (wu2024metagenomicinsightsinto pages 1-2) | Useful for curation notes and assay logic; not a universal biological definition. |
| higher environmental salinity → positively_associated_with_abundance_of → COG0168 / Trk-type K+ transporter | mechanistic | subject: ENVO:00002009 salinity; object: COG:COG0168 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0168… was ranked the single most important feature and its relative abundance increased with salinity” (wu2024metagenomicinsightsinto pages 1-2) | Strongest salinity-linked genomic feature in Wu; association across metagenomes and stenohaline MAGs, not direct perturbation. |
| COG0168 / Trk-type K+ transporter → mediates → salt-in osmoadaptation strategy | mechanistic | subject: COG:COG0168; object: label-only candidate “salt-in osmoadaptation” | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0168, annotated as a Trk-type K+ transporter (salt-in)” (wu2024metagenomicinsightsinto pages 1-2) | Good candidate node-edge for salinity adaptation graph. |
| higher environmental salinity → negatively_associated_with_abundance_of → COG3158 / Kup-type K+ transporter | mechanistic | subject: ENVO:00002009; object: COG:COG3158 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG3158 shows a linear decline” with increasing salinity (wu2024metagenomicinsightsinto pages 11-13) | Association from metagenomic trend; may indicate preference for lower-salinity conditions rather than direct causation. |
| COG3158 / Kup-type K+ transporter → associated_with → low-salinity stenohaline state | mechanistic | subject: COG:COG3158; object: label-only candidate “low-salinity stenohaline state” | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG3158 is most abundant in low-salinity samples” (wu2024metagenomicinsightsinto pages 11-13) | Useful contrasting marker versus COG0168; uncertain outside Pearl River estuary dataset. |
| higher environmental salinity → positively_associated_with_abundance_of → COG0530 / Ca2+:K+/Na+ antiporter | mechanistic | subject: ENVO:00002009; object: COG:COG0530 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0168, COG0530, and COG0038 increase with salinity” (wu2024metagenomicinsightsinto pages 11-13) | Antiporter role is inferred from annotation/enrichment, not direct transporter biochemistry in this study. uncertain |
| COG0530 / Ca2+:K+/Na+ antiporter → contributes_to → salt-in osmoadaptation strategy | mechanistic | subject: COG:COG0530; object: label-only candidate “salt-in osmoadaptation” | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0530… implicated in a ‘salt-in’ strategy” (wu2024metagenomicinsightsinto pages 11-13) | Annotation-backed functional grouping; direct causal contribution not experimentally tested here. uncertain |
| intermediate/high salinity → positively_associated_with_abundance_of → COG0038 / Cl− channel | mechanistic | subject: ENVO:00002009; object: COG:COG0038 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0038 peaks at intermediate salinity” and “increase[s] with salinity” (wu2024metagenomicinsightsinto pages 11-13) | Pattern is not monotonic in all summaries; curate cautiously as salinity-associated ion homeostasis feature. |
| COG0477 / ProP-family MFS transporter → transports → compatible solutes (glycine betaine / proline betaine / ectoine) | mechanistic | subject: COG:COG0477; object: CHEBI:17750 glycine betaine; CHEBI:30913 ectoine; label-only candidate proline betaine | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0477 (ProP transporter) imports compatible solutes (proline betaine, glycine betaine, ectoine)” (wu2024metagenomicinsightsinto pages 14-16) | Transported substrates are summarized from annotation/discussion; likely strong but still partly inferred in Wu. uncertain |
| higher environmental salinity → negatively_associated_with_abundance_of → COG0477 / ProP-family MFS transporter | mechanistic | subject: ENVO:00002009; object: COG:COG0477 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0477… declines with salinity (R2 = 0.6608, p = 0.002599)” (wu2024metagenomicinsightsinto pages 11-13) | Suggests compatible-solute transport repertoire differs by salinity niche; trend may be phylum-specific. |
| COG0591 / symporter activity → positively_associated_with → high-salinity stenohaline MAGs | mechanistic | subject: COG:COG0591; object: label-only candidate “high-salinity stenohaline MAG” | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0591 increases with salinity… and is enriched in high-salinity stenohaline MAGs” (wu2024metagenomicinsightsinto pages 11-13) | Annotation broad (“symporter activity”); substrate specificity unclear, so graph node may remain label-only. uncertain |
| COG1115 / amino acid carrier → positively_associated_with_abundance_of → higher environmental salinity | mechanistic | subject: COG:COG1115; object: ENVO:00002009 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG1115… increases (R2=0.8093, p=0.0002428)” (wu2024metagenomicinsightsinto pages 11-13) | Evidence is statistical association; transported amino acid(s) not resolved. uncertain |
| COG0580 / aquaporin-water channel activity → enables → facilitated water diffusion | mechanistic | subject: COG:COG0580; object: GO:0015250 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0580… linked to GO:0015250 and described as enabling facilitated diffusion of water” (wu2024metagenomicinsightsinto pages 13-14) | Good functional edge; specific channel proteins not identified in Wu. |
| higher environmental salinity → negatively_associated_with_abundance_of → COG0580 / aquaporin-water channel activity | mechanistic | subject: ENVO:00002009; object: COG:COG0580 | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “COG0580 R2 = 0.4783, p = 0.01603 (decrease)” (wu2024metagenomicinsightsinto pages 11-13) | Trend varies by phylum in Wu; curate as salinity-associated, not universal. uncertain |
| c-di-AMP → inhibits → K+ import systems (Trk/Ktr/Kup/Kdp-linked targets) | mechanistic | subject: CHEBI:16761 cyclic di-AMP; object: label-only candidate “K+ import systems” | Foster 2024, 10.1128/mmbr.00181-23 | Jun 2024 | “c-di-AMP binds RCK-type gating subunits… inhibiting potassium influx” (foster2024bacterialcellvolume pages 8-10) | Broad regulatory principle across c-di-AMP bacteria; not specific to stenohaline taxa. |
| c-di-AMP → inhibits → compatible-solute importer OpuA | mechanistic | subject: CHEBI:16761; object: label-only candidate “OpuA transporter” | Foster 2024, 10.1128/mmbr.00181-23 | Jun 2024 | “It binds CBS-containing compatible-solute importers (examples: OpuA, OpuC, OpuD) and negatively regulates their transport activity” (foster2024bacterialcellvolume pages 10-12) | Strong mechanistic regulation edge; relevant for osmoadaptation generally, not yet stenohaline-specific. |
| c-di-AMP-bound BusR → represses_transcription_of → opuA | mechanistic | subject: label-only candidate “BusR”; object: label-only candidate “opuA” | Foster 2024, 10.1128/mmbr.00181-23 | Jun 2024 | “BusR binds c-di-AMP… causing inhibition of opuA transcription” (foster2024bacterialcellvolume pages 10-12) | Useful regulatory subgraph for compatible-solute import control. |
| low c-di-AMP state → increases → K+ and compatible solute uptake | mechanistic | subject: label-only candidate “low c-di-AMP state”; object: label-only candidate “K+ and compatible-solute uptake” | Foster 2024, 10.1128/mmbr.00181-23 | Jun 2024 | “low c-di-AMP mutants show increased uptake of K+ and compatible solutes” (foster2024bacterialcellvolume pages 13-16) | Physiological consequence edge; broad bacterial principle. |
| mechanosensitive channels → release → osmolytes during hypoosmotic downshift | mechanistic | subject: GO:0015288 mechanosensitive ion channel activity; object: label-only candidate “osmolytes” | Foster 2024, 10.1128/mmbr.00181-23 | Jun 2024 | “Mechanosensitive (non-selective) channels provide a rapid, sub-second release route for osmolytes and water” (foster2024bacterialcellvolume pages 13-16) | Directly relevant to salinity fluctuation tolerance; may help explain why poor shock-response capacity contributes to stenohaly. inferential for trait-level edge. uncertain |
| Streptomyces genome → encodes → MscL/MscS mechanosensitive channels | mechanistic | subject: NCBITaxon:1883 Streptomyces; object: GO:0015288 | Bhowmick 2023, 10.1093/femsml/uqad020 | Apr 2023 | “Mechanosensitive channels (MscL/MscS types) are present in S. venezuelae as two large… and two small… conductance channels” (bhowmick2023osmoticstressresponses pages 3-4) | Taxon-specific encoding edge; useful exemplar, not general stenohaline marker. |
| Streptomyces genome → encodes → aquaporins / aquaporin-like proteins | mechanistic | subject: NCBITaxon:1883; object: GO:0015250 | Bhowmick 2023, 10.1093/femsml/uqad020 | Apr 2023 | “Aquaporins are encoded… and an aquaporin-like protein… is noted” (bhowmick2023osmoticstressresponses pages 3-4) | Taxon-specific gene inventory edge; relevance to stenohaly is indirect. uncertain |
| osmotic upshift → triggers → rapid K+ import | mechanistic | subject: label-only candidate “osmotic upshift”; object: CHEBI:29103 potassium(1+) | Bhowmick 2023, 10.1093/femsml/uqad020 | Apr 2023 | “many bacteria mount a rapid K+ import upon osmotic upshift” (bhowmick2023osmoticstressresponses pages 3-4) | Canonical osmoadaptation edge; not specific to stenohaline microbes. |
| osmotic upshift → increases → intracellular proline accumulation | mechanistic | subject: label-only candidate “osmotic upshift”; object: CHEBI:17203 L-proline | Bhowmick 2023, 10.1093/femsml/uqad020 | Apr 2023 | “proline… rose from <6% to ~50% of the free amino acid pool at 1 M salt” (bhowmick2023osmoticstressresponses pages 3-4) | Strong example of compatible-solute accumulation in Streptomyces. |
| compatible-solute accumulation (proline / ectoine / trehalose) → supports → salt-out osmoadaptation | mechanistic | subject: CHEBI:17203 L-proline; CHEBI:30913 ectoine; CHEBI:16551 trehalose; object: label-only candidate “salt-out osmoadaptation” | Bhowmick 2023, 10.1093/femsml/uqad020 | Apr 2023 | “The longer-term strategy is 'salt-out' via synthesis/import of compatible solutes” (bhowmick2023osmoticstressresponses pages 3-4) | General mechanistic edge; substrate set partly review-based. |
| increased external Na+ (2.5→4.3 M) → increases → intracellular glycine betaine concentration | mechanistic | subject: CHEBI:29101 sodium(1+); object: CHEBI:17750 glycine betaine | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “glycine betaine rose from 52.7 mM (2.5 M) to 893.1 mM (4.3 M)” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Strong quantitative mechanistic evidence from one extremophile bacterium. |
| increased external Na+ (2.5→4.3 M) → increases → intracellular L-glutamate concentration | mechanistic | subject: CHEBI:29101; object: CHEBI:29985 L-glutamate | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “L-glutamate increased from 11.0 mM to 221.3 mM” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Strong quantitative evidence for compatible-solute/amino-acid accumulation. |
| high salinity → increases → intracellular proline concentration | mechanistic | subject: ENVO:00002009; object: CHEBI:17203 L-proline | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “proline… peaked at 130 mM at 4.3 M” (xing2024thepolyextremophilenatranaerobius pages 17-19) | Quantitative but non-monotonic at lower salinity; still supports high-salt accumulation. |
| Opu/ProU glycine betaine transporters → contribute_to → long-term high-salinity adaptation | mechanistic | subject: label-only candidate “Opu/ProU transporters”; object: label-only candidate “long-term salinity adaptation” | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “employs the glycine betaine ABC transporters (Opu and ProU families)… to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Good edge for compatible-solute uptake; transporter paralogs have mixed regulation in paper. |
| Na+/K+/H+ transporters / antiporters → maintain → intracellular K+ homeostasis under high salinity | mechanistic | subject: label-only candidate “Na+/K+/H+ transporters”; object: label-only candidate “intracellular K+ homeostasis” | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “upregulation of Na+/ K+/ H+ transporters facilitates the maintenance of intracellular K+ concentration” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Directly relevant to salt-in component of adaptation. |
| trkH → positively_responds_to → increased salinity | mechanistic | subject: label-only candidate “trkH”; object: ENVO:00002009 | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “TrkH… was upregulated especially at 3.1 M (1.81-fold)” (xing2024thepolyextremophilenatranaerobius pages 6-7) | Taxon-specific regulation in Natranaerobius thermophilus; supports K+ uptake role. |
| nhaC / Na+/H+ antiporter → positively_responds_to → increased salinity | mechanistic | subject: label-only candidate “nhaC”; object: ENVO:00002009 | Xing 2024, 10.1128/aem.00145-24 | May 2024 | “nhaC… showed strong upregulation at higher salinities (1.04→3.27→3.22)” (xing2024thepolyextremophilenatranaerobius pages 6-7) | Strong within-taxon evidence for antiporter response to salt stress. |
| stenohaline trait → may_reflect_limited_capacity_for → broad salinity-shock acclimation | operational | subject: METPO:1000626; object: label-only candidate “broad salinity-shock acclimation” | Foster 2024, 10.1128/mmbr.00181-23; Bhowmick 2023, 10.1093/femsml/uqad020 | Jun 2024; Apr 2023 | “Mechanosensitive… channels provide a rapid… release route” and osmoadaptation depends on K+ and compatible-solute regulation (foster2024bacterialcellvolume pages 13-16, bhowmick2023osmoticstressresponses pages 3-4) | Integrative trait-level hypothesis, not directly demonstrated for stenohaline organisms in cited papers. uncertain |
| salinity gradient → structures → microbial taxonomic and functional profiles | operational | subject: ENVO:00002009; object: label-only candidate “microbial community taxonomic/functional profile” | Wu 2024, 10.1186/s40168-024-01817-w | Jun 2024 | “salinity exerts influences on both the taxonomic and functional profiles” (wu2024metagenomicinsightsinto pages 1-2) | Useful contextual edge explaining why stenohaline states are observable in community-resolved data. |


*Table: This table compiles evidence-backed candidate causal edges for curating the microbial trait stenohaline, combining operational classification rules with mechanistic salinity-response features from recent literature. It highlights which edges are strong candidates for TraitMech and which remain uncertain or taxon-specific.*

---

### 5) Key statistics & data points to support curation
- **Operational stenohaline definition in a microbial dataset:** 10× abundance rule across salinity bins. (wu2024metagenomicinsightsinto pages 1-2)
- **MAG counts (Pearl River Estuary study):** 127 total MAGs; 33 low-, 36 intermediate-, 44 high-salinity stenohaline; 14 euryhaline. (wu2024metagenomicinsightsinto pages 7-9)
- **Feature selection:** ~12,162 COGs observed; 40 Boruta-selected; 8 osmoregulation-linked COGs; **COG0168** top-ranked feature. (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 11-13)
- **Quantitative metabolite response to high salinity:** glycine betaine 52.7→893.1 mM and glutamate 11.0→221.3 mM between 2.5 and 4.3 M Na+ in *N. thermophilus*. (xing2024thepolyextremophilenatranaerobius pages 17-19)

---

### 6) Curation warnings (do-not-curate-yet / uncertain edges)
1. **Operational vs physiological stenohaly:** Wu et al. classify stenohaline MAGs by abundance restriction across salinity bins, not by direct growth-rate or survival assays; avoid curating “cannot survive outside range” unless supported by direct physiology. (wu2024metagenomicinsightsinto pages 1-2)
2. **Association vs causation:** Most Wu et al. edges (COG abundance vs salinity; MAG category enrichment) are **correlational**. For TraitMech, treat as “associated_with/indicator_of” unless there is perturbation evidence. (wu2024metagenomicinsightsinto pages 11-13)
3. **COG functional ambiguity:** COG0591 and COG1115 are functionally broad (“symporter activity”, “amino acid carrier”); curate as label-level nodes or require additional annotation to identify substrates. (wu2024metagenomicinsightsinto pages 11-13)
4. **Taxon-specific exemplars:** *Streptomyces* (Bhowmick 2023) and *Natranaerobius thermophilus* (Xing 2024) provide strong mechanistic exemplars but should be marked **taxon-specific** unless cross-validated. (bhowmick2023osmoticstressresponses pages 3-4, xing2024thepolyextremophilenatranaerobius pages 17-19)
5. **Halotolerant/halophilic thresholds:** Oren (2024) provides a clear threshold for hypersaline/halophile (>100–150 g/L), but explicit 2023–2024 definitions for halotolerance were not available in the retrieved authoritative sources; avoid hard-threshold curation for halotolerant vs halophilic without additional peer-reviewed support. (oren2024novelinsightsinto pages 1-2)

---

## DOI-first bibliography (URLs + publication dates)
1. **Wu Z, Li M, Qu L, Zhang C, Xie W.** *Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.* **Microbiome**. **Jun 2024**. DOI: **10.1186/s40168-024-01817-w**. URL: https://doi.org/10.1186/s40168-024-01817-w (wu2024metagenomicinsightsinto pages 1-2)
2. **Foster AJ, van den Noort M, Poolman B.** *Bacterial cell volume regulation and the importance of cyclic di-AMP.* **Microbiology and Molecular Biology Reviews**. **Jun 2024**. DOI: **10.1128/mmbr.00181-23**. URL: https://doi.org/10.1128/mmbr.00181-23 (foster2024bacterialcellvolume pages 31-33)
3. **Oren A.** *Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems.* **npj Biodiversity**. **Aug 2024**. DOI: **10.1038/s44185-024-00050-w**. URL: https://doi.org/10.1038/s44185-024-00050-w (oren2024novelinsightsinto pages 1-2)
4. **Xing Q, Zhang S, Tao X, Mesbah NM, Mao X, Wang H, Wiegel J, Zhao B.** *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology**. **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
5. **Bhowmick S, Shenouda ML, Tschowri N.** *Osmotic stress responses and the biology of the second messenger c-di-AMP in Streptomyces.* **microLife**. **Apr 2023**. DOI: **10.1093/femsml/uqad020**. URL: https://doi.org/10.1093/femsml/uqad020 (bhowmick2023osmoticstressresponses pages 3-4)
6. **Matarredona L, Zafrilla B, Camacho M, Bonete M-J, Esclapez J.** *Understanding the tolerance of halophilic archaea to stress landscapes.* **Environmental Microbiology Reports**. **Nov 2024**. DOI: **10.1111/1758-2229.70039**. URL: https://doi.org/10.1111/1758-2229.70039 (matarredona2024understandingthetolerance pages 2-4)

(Non-priority, preprint; use cautiously for thresholds)
- **Schiavo APM et al.** *Proposal for new halophile classification system…* **Nov 2025**. DOI: **10.21203/rs.3.rs-8012852/v1**. URL: https://doi.org/10.21203/rs.3.rs-8012852/v1 (schiavo2025proposalfornew pages 4-7)

---

### 7) Suggested next curation steps (TraitMech-specific)
- Treat **stenohaline** as a trait whose mechanistic underpinnings can be modeled via **(i) ion transport capacity/regulation (K+ uptake/antiporters), (ii) compatible-solute uptake/synthesis, (iii) water flux control (aquaporins), (iv) downshock protection (mechanosensitive channels), (v) global regulation (c-di-AMP)**, while keeping **stenohaline classification** itself explicitly tied to an assay/operational rule when using community data. (wu2024metagenomicinsightsinto pages 11-13, foster2024bacterialcellvolume pages 10-12, foster2024bacterialcellvolume pages 13-16)
- Prioritize edges in the artifact table that are (a) mechanistically direct and (b) not purely correlational (e.g., c-di-AMP → inhibits OpuA; increased salinity → increases glycine betaine in *N. thermophilus*). (foster2024bacterialcellvolume pages 10-12, xing2024thepolyextremophilenatranaerobius pages 17-19)


References

1. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

2. (velez2019impactofsalinity pages 1-3): Patricia Velez. Impact of salinity stress on growth and development of aquatic fungi. Soil Biology, pages 155-168, Jan 2019. URL: https://doi.org/10.1007/978-3-030-18975-4\_7, doi:10.1007/978-3-030-18975-4\_7. This article has 5 citations and is from a peer-reviewed journal.

3. (wu2024metagenomicinsightsinto pages 7-9): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

4. (wu2024metagenomicinsightsinto pages 2-4): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

5. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

6. (schiavo2025proposalfornew pages 4-7): Ana Paula Muche Schiavo, Roberta Almeida Vincenzi, and Fabio Rodrigues. Proposal for new halophile classification system based on statistical rarity definition of extremophiles. Unknown journal, Nov 2025. URL: https://doi.org/10.21203/rs.3.rs-8012852/v1, doi:10.21203/rs.3.rs-8012852/v1.

7. (wu2024metagenomicinsightsinto pages 11-13): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

8. (wu2024metagenomicinsightsinto pages 13-14): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

9. (wu2024metagenomicinsightsinto media 3c6a53f2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

10. (foster2024bacterialcellvolume pages 31-33): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

11. (foster2024bacterialcellvolume pages 13-16): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

12. (foster2024bacterialcellvolume pages 6-8): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

13. (foster2024bacterialcellvolume pages 8-10): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

14. (foster2024bacterialcellvolume pages 10-12): Alexander J. Foster, Marco van den Noort, and Bert Poolman. Bacterial cell volume regulation and the importance of cyclic di-amp. Jun 2024. URL: https://doi.org/10.1128/mmbr.00181-23, doi:10.1128/mmbr.00181-23. This article has 27 citations and is from a domain leading peer-reviewed journal.

15. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

16. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

17. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

18. (bhowmick2023osmoticstressresponses pages 3-4): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

19. (bhowmick2023osmoticstressresponses pages 7-8): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

20. (wu2024metagenomicinsightsinto pages 14-16): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 62 citations and is from a highest quality peer-reviewed journal.

21. (matarredona2024understandingthetolerance pages 2-4): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.