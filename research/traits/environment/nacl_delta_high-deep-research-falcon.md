---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:17:21.755999'
end_time: '2026-08-04T01:34:03.385367'
duration_seconds: 1001.63
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl delta high
  trait_identifier: METPO:1000482
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_delta_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately
    8% (w/v), characteristic of extreme-euryhaline organisms.
  parent_traits: METPO:1000335
  synonyms: Nad_>8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.)
    | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems
    review supports combined osmolyte / salt-in flexibility as the basis of very wide
    salinity tolerance.)'
  causal_graph_summary: 'nacl_delta_high_extreme_euryhaline: 14 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000482
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately 8% (w/v), characteristic of extreme-euryhaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports combined osmolyte / salt-in flexibility as the basis of very wide salinity tolerance.)
- **Existing causal graph summary:** nacl_delta_high_extreme_euryhaline: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_high.yaml`.

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
- **Trait label:** NaCl delta high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000482
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth above approximately 8% (w/v), characteristic of extreme-euryhaline organisms.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports very wide salinity-tolerance breadths as the extreme-euryhaline phenotype.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports combined osmolyte / salt-in flexibility as the basis of very wide salinity tolerance.)
- **Existing causal graph summary:** nacl_delta_high_extreme_euryhaline: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **NaCl delta high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_high.yaml`.

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


# Curation report: NaCl delta high

**Trait:** “NaCl delta high”  
**Identifier:** **METPO:1000482**  
**Parent:** METPO:1000335  
**Category:** ENVIRONMENT; **term kind:** CLASS; **mapping:** REVIEWED  
**Operational definition:** growth-supporting NaCl breadth greater than approximately 8% (w/v), corresponding to an extreme-euryhaline phenotype.

## 1. Scope and interpretation

METPO:1000482 should represent the **width of the experimentally demonstrated NaCl growth interval**, not merely a high optimum, high maximum, survival after salt exposure, or occurrence in a hypersaline habitat. The minimum and maximum growth-supporting NaCl concentrations should ideally be measured in the same medium, temperature, pH, incubation time, and growth-detection assay. Because molarity, percent w/v NaCl, total Na+, practical salinity units (PSU), and water activity are not interchangeable, the graph should preserve the original assay units and medium composition.

The strongest illustrative phenotype is *Aspergillus sydowii*, which grows from no added NaCl to 5.13 M NaCl, although growth at saturation is weak. This is an extreme breadth rather than obligate halophily. By contrast, *Wallemia ichthyophaga* grows only from 10% to saturated NaCl (~32%); it has a large breadth but also a high lower bound and is therefore obligately halophilic. The same paper reports *Hortaea werneckii* growing from 0% to 32% NaCl, *Aureobasidium pullulans* from 0% to 17%, and *Debaryomyces hansenii* tolerating up to 24%. These examples show why breadth, minimum, maximum, and optimum should be represented separately (zajc2014osmoadaptationstrategyof pages 1-2, jimenezgomez2022survivinginthe pages 1-2).

Oren’s authoritative framework classifies extreme halophiles by salt optimum—approximately 2.5–5.2 M—rather than breadth. It also notes that organisms using organic compatible solutes often accommodate broader salt ranges than organisms whose proteins require a high-salt cytoplasm. Thus, “extreme halophile” and “extreme-euryhaline” overlap but are not equivalent (oren2008microbiallifeat pages 1-2, oren2008microbiallifeat pages 10-11).

### Boundary cases

- **Include:** reproducible vegetative growth across a NaCl interval exceeding ~8 percentage points w/v.
- **Do not infer from:** a single high-NaCl growth point, viability without growth, spore survival, environmental detection, gene presence, or predicted salt tolerance.
- **High maximum but unknown breadth:** insufficient for METPO:1000482.
- **Wide MgCl₂ range:** relevant to general osmoadaptation but not direct evidence for a specifically NaCl-defined trait.
- **PSU or total Na+ assays:** potentially supportive, but only after preserving ionic composition and avoiding unjustified conversion to NaCl w/v.
- **Obligate halophile:** may possess the trait if the measured interval is wide enough, but should additionally carry a high-minimum/NaCl-requirement phenotype.

## 2. Current mechanistic model

No single mechanism is sufficient across all taxa. The most defensible model is a coordinated system with four possible layers:

1. **Rapid ionic adjustment:** K⁺ uptake and Na⁺/H⁺, K⁺/H⁺, or multispecific antiport maintain turgor, pH, and ion homeostasis.
2. **Compatible-solute adjustment:** synthesis or uptake of ectoine, glycine betaine, proline, glutamate, glycerol, or related compounds balances osmotic pressure without imposing high ionic strength on most enzymes.
3. **Macromolecular adaptation:** acidic proteins, membrane and cell-wall remodeling, and stress-signaling networks preserve function at high salt.
4. **Energetic reconfiguration:** transport, compatible-solute synthesis, respiratory-chain alternatives, and carbon/amino-acid metabolism are reorganized to pay the energetic cost of adaptation.

The latest strong mechanistic study is Xing et al. (published 5 April 2024). *Natranaerobius thermophilus* grows at 3.1–4.9 M Na⁺ and optimally at 3.3–3.9 M; iTRAQ proteomics at 2.5, 3.1, 3.7, and 4.3 M Na⁺, ddPCR, intracellular metabolites, and K⁺ measurements supported simultaneous compatible-solute and salt-in strategies. Glycine betaine, glutamate, and proline increased with salinity, while Opu/ProU-family transporters, Na⁺/solute symporters, and Na⁺/K⁺/H⁺ transporters participated in adaptation. The median pI of upregulated proteins declined with salinity, consistent with cytoplasmic acidification (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17).

## 3. Candidate nodes grouped by type

### Trait and assay nodes

- **NaCl delta high:** METPO:1000482.
- **NaCl delta phenotype parent:** METPO:1000335.
- Growth-supporting NaCl minimum; growth-supporting NaCl maximum; NaCl growth optimum; growth rate; biomass yield; water activity; incubation time; medium composition — retain as label-only assay nodes unless established TraitMech identifiers exist.

### Environmental and experimental factors

- Sodium chloride — **CHEBI:26710**.
- High-salinity environment; hypersaline water; brine; solar saltern — use ENVO terms only after identifier verification against the project’s ontology release.
- Water activity, temperature, pH, oxygen availability, carbon source, extracellular K⁺ availability, hypo-osmotic shock — label-only candidates are safer than unverified CURIEs.

### Chemicals and metabolites

- Sodium ion — **CHEBI:29101**.
- Potassium ion — **CHEBI:29103**.
- Chloride — **CHEBI:17996**.
- L-proline — **CHEBI:17203**.
- L-glutamate — **CHEBI:29985**.
- Glycerol — **CHEBI:17754**.
- Ectoine, hydroxyectoine, glycine betaine, trehalose, arabitol, and mannitol are strong candidate nodes, but their exact CURIEs should be resolved programmatically before YAML insertion rather than copied from memory.

### Genes, proteins, and transport systems

- **ectA–ectB–ectC:** ectoine biosynthesis from L-aspartate semialdehyde.
- **gsmt, sdmt:** glycine methylation route to glycine betaine; evidence in *N. thermophilus* remains partly unpublished/undetected in the principal salinity series.
- **OpuA/OpuB/OpuC/OpuD and ProU/ProVWX:** compatible-solute ABC or secondary transport systems.
- **PutP / SSS-family transporter:** Na⁺/proline symport.
- **TeaABC:** ectoine/hydroxyectoine TRAP transporter in *H. elongata*.
- **Na⁺/K⁺/H⁺ antiporters; Mrp-family antiporter; Na⁺-translocating F-type ATPase:** ion and pH homeostasis.
- **Sho1, Sln1, Ssk1, Ssk2, Hog1, Ste20, Cla4:** fungal osmosensing/HOG-network components.
- **β-1,3-glucan biosynthesis machinery; chitin, mannose, and cell-wall-protein synthesis modules.**
- **Cytochrome bo′ and cytochrome bd quinol oxidases:** alternative respiratory endpoints associated with salt stress.

Gene symbols should be qualified by taxon/strain. Do not assign UniProt accessions without sequence-level resolution.

### Pathways, functions, and cellular processes

- Compatible-solute biosynthesis and uptake.
- Ectoine biosynthetic process.
- Glycine-betaine transport and biosynthesis.
- Potassium-ion accumulation and homeostasis.
- Sodium/proton and potassium/proton antiport.
- Cellular response to osmotic stress — **GO:0071470**.
- Osmoregulation — **GO:0006970**.
- HOG MAPK signaling; cell-wall remodeling; maintenance of cytoplasmic ionic strength; protein adaptation to high ionic strength; oxidative phosphorylation; chemotaxis and motility; amino-acid and carbohydrate metabolism.

### Organisms and cellular locations

Priority taxon-qualified models are *Natranaerobius thermophilus* DSM 18059T, *Halomonas elongata* DSM 2581T, *Aspergillus sydowii* EXF-12860, *Wallemia ichthyophaga*, *Virgibacillus dokdonensis* 21D, and *Euplaesiobystra salpumilio*. Exact NCBITaxon identifiers should be imported from a current taxonomy service before curation. Relevant compartments include cytoplasm, plasma membrane, cell wall, extracellular medium, and—where applicable—fungal vacuole.

## 4. Candidate causal edges

The following table is the prioritized edge set. “High” means direct biochemical, quantitative multi-level, or perturbational support; it does not imply universality across taxa.

| subject | predicate | object | evidence/taxon | confidence |
|---|---|---|---|---|
| Increased external NaCl / salinity | increases accumulation of | compatible solutes (glycine betaine, glutamate, proline) | *Natranaerobius thermophilus*; intracellular compatible-solute content increased with salinity in 2.5–4.3 M Na+ experiments (xing2024thepolyextremophilenatranaerobius pages 1-2) | High |
| OpuA/OpuB/ProU ABC transporters | mediates uptake of | glycine betaine / osmoprotectants | *N. thermophilus* proteomics/transcript context; ABC-type glycine betaine transporters implicated as major salt-adaptation route (xing2024thepolyextremophilenatranaerobius pages 14-17) | High, taxon-specific |
| Na+/solute symporters (SSS family, including PutP) | mediates uptake of | proline / solutes used in osmoadaptation | *N. thermophilus* used Na+/solute symporters and proline pathway under high salinity (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17) | Medium-High, taxon-specific |
| Na+/K+/H+ transporters | maintains | intracellular K+ homeostasis | *N. thermophilus*; transporter upregulation linked to maintenance of intracellular K+ under varying salinities (xing2024thepolyextremophilenatranaerobius pages 1-2) | High |
| KCl accumulation | contributes to | osmotic balance in high salt | General halophile mechanism; foundational review of salt-in strategy (oren2008microbiallifeat pages 1-2, oren2008microbiallifeat pages 10-11) | High, broad but not trait-specific |
| Acidic proteome / decreased median pI | supports | protein function in high ionic strength cytoplasm | General salt-in halophiles require adapted acidic proteomes; in *N. thermophilus* median pI of upregulated proteins decreased with salinity (oren2008microbiallifeat pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) | High for association, Medium for direct causal edge |
| ectABC | enables biosynthesis of | ectoine | *Halomonas elongata* introduction summarizes ectoine biosynthesis from aspartate semialdehyde via ectABC (hobmeier2022adaptationtovarying pages 1-2) | High, pathway-level |
| Glycerol accumulation | contributes to | osmotic balance | *Wallemia ichthyophaga*; glycerol was the major osmotically regulated solute and increased with salinity (zajc2014osmoadaptationstrategyof pages 1-2) | High, taxon-specific |
| Saturated NaCl (5.13 M) | induces | HOG-pathway transcriptional remodeling | *Aspergillus sydowii*; sho1/cla4/ssk1 up, hog1/ste20/ssk2 down at saturated NaCl vs 1 M (jimenezgomez2022survivinginthe pages 1-2, jimenezgomez2022survivinginthe pages 8-9) | High, taxon-specific |
| Saturated NaCl (5.13 M) | induces | cell-wall transcriptional remodeling (β-1,3-glucan up; chitin/mannose/cell-wall proteins down) | *A. sydowii* transcriptomics under saturated NaCl (jimenezgomez2022survivinginthe pages 1-2, jimenezgomez2022survivinginthe pages 8-9) | High, taxon-specific |
| teaABC deletion | causes | ectoine excretion phenotype | *H. elongata* mutant KB2.13; loss of ectoine Na+ uptake defines ectoine-excreting phenotype (hobmeier2022adaptationtovarying pages 14-16) | High, perturbational |
| teaABC deletion | shifts transcription toward | low-salt-like transcriptional state | *H. elongata* mutant KB2.13 transcriptome resembles low-salt profile (hobmeier2022adaptationtovarying pages 14-16) | High, perturbational |
| High salinity / salt stress | upregulates | cytochrome bo′ and cytochrome bd quinol oxidases | *H. elongata* transcriptome; alternative terminal oxidase routes seem upregulated in salt-stressed cells (hobmeier2022adaptationtovarying pages 1-2) | Medium, associational |
| Compatible-solute-based osmoadaptation traits (glycine-betaine/carnitine/choline ABC transporters, ectoine synthase enzymes) | associated with | adaptation to hypersaline interface conditions | *Virgibacillus dokdonensis* 21D genomics + phenomics (zeaiter2019phenomicsandgenomics pages 1-2) | Medium, associational |
| High salinity (100–150 PSU) | associates with / may require | intracellular Na+ accumulation, with salt-out at higher salinity | *Euplaesiobystra salpumilio* shows salt-in at 100 PSU and salt-out at 150 PSU (lee2022accumulationpatternsof pages 1-2) | Medium, taxon-specific and unusual |
| Potassium-accumulation genes | associated with | osmoregulation in hypersaline community | Tuz Lake seasonal PICRUSt2 inference; community-level archaeal dominance (dogan2023profilingthegenes pages 1-3) | Low-Medium, predictive/community-level |
| Hypersaline microbiome salt-tolerance genes | associated with | plant-growth-promotion potential in salinized soils | MAG-based functional annotation from Sambhar Lake and Drang Mine (dindhoria2024metagenomicassembledgenomes pages 1-2) | Low-Medium, application-level and genomic inference |


*Table: This table summarizes strong and curation-relevant candidate causal edges for the NaCl delta high trait, emphasizing direct mechanistic and perturbational evidence where available. It also flags taxon-specific or associational claims to help prioritize what is most suitable for TraitMech curation.*

### Edge-specific supporting snippets and curation notes

| Candidate triple | Supporting snippet | DOI and date | Curation note |
|---|---|---|---|
| Increased salinity **increases** intracellular glycine betaine, glutamate, and proline | “The intracellular content of compatible solutes…increases with rising salinity levels” | [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), published 5 Apr 2024 | Strong multi-level evidence in *N. thermophilus*; curate as taxon-specific, not universal (xing2024thepolyextremophilenatranaerobius pages 1-2). |
| Na⁺/K⁺/H⁺ transporter upregulation **supports** intracellular K⁺ homeostasis | “upregulation…facilitates the maintenance of intracellular K⁺ concentration” | [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), 2024 | Strong association plus physiological K⁺ measurement; individual transporter necessity was not tested (xing2024thepolyextremophilenatranaerobius pages 1-2). |
| Opu/ProU-family transport **promotes** glycine-betaine/osmoprotectant uptake | “Glycine betaine uptake is the main mechanism for salt adaptation” | [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24), 2024 | Strong for the transporter class in *N. thermophilus*; individual paralogs responded differently, so avoid collapsing every Opu copy into a positive edge (xing2024thepolyextremophilenatranaerobius pages 14-17). |
| KCl accumulation **enables** osmotic balance at high salinity | “accumulation of molar concentrations of KCl” | [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2), Apr 2008 | Foundational, broad mechanism. Link to METPO:1000482 only through a taxon-specific measured breadth; salt-in organisms can be poor low-salt growers (oren2008microbiallifeat pages 1-2). |
| Acidic proteome **supports** protein function in a high-salt cytoplasm | proteins “should maintain their proper conformation and activity at near-saturating salt concentrations” and the proteome is “highly acidic” | [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2), 2008 | Mechanistically credible but often constitutive/evolutionary rather than an acute response. The 2024 decline in median pI is supporting association, not a knockout test (oren2008microbiallifeat pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2). |
| **ectABC enables ectoine biosynthesis**; ectoine accumulation **supports** osmotic balance | “corresponding synthesis enzymes are encoded by the gene cluster ectABC” | [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677), published 30 Mar 2022 | Curate pathway-level biochemistry confidently; the final edge to breadth remains mechanistic inference unless a breadth assay compares ectABC mutants (hobmeier2022adaptationtovarying pages 1-2). |
| teaABC deletion **causes** ectoine excretion and a low-salt-like transcriptional state | “removal of the teaABC cluster” produced loss of ectoine Na⁺ uptake; mutant response correlated with low salt | [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677), 2022 | Best perturbational edge in the retrieved set. It establishes recycling/uptake function, but not by itself a change in the >8% growth breadth (hobmeier2022adaptationtovarying pages 14-16). |
| Glycerol accumulation **supports** fungal osmoadaptation | “glycerol was the major osmotically regulated solute, since its accumulation increased with salinity and was diminished by hypo-osmotic shock” | [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13), published online 25 Oct 2013; issue Jan 2014 | Strong physiological directionality in *W. ichthyophaga*. This fungus grows only at 10–32% NaCl, so separately encode obligate halophily (zajc2014osmoadaptationstrategyof pages 1-2). |
| Saturated NaCl **remodels** fungal HOG signaling | at 5.13 M, “sho1…cla4…and ssk1 were upregulated,” whereas “hog1…ste20…and ssk2 were downregulated” | [10.3389/fmicb.2022.840408](https://doi.org/10.3389/fmicb.2022.840408), published 2 May 2022 | Do not simplify to “NaCl activates Hog1.” The observed network response is mixed and transcript abundance is not kinase activity (jimenezgomez2022survivinginthe pages 8-9). |
| Saturated NaCl **induces** cell-wall remodeling | upregulated genes included “biosynthesis of β-1,3-glucans”; downregulated genes involved chitin, mannose, and cell-wall proteins | [10.3389/fmicb.2022.840408](https://doi.org/10.3389/fmicb.2022.840408), 2022 | Strong transcriptomic association in *A. sydowii*; causal contribution to growth breadth awaits perturbation (jimenezgomez2022survivinginthe pages 1-2). |
| Salt stress **upregulates** alternative terminal oxidases | pathways via cytochrome bo′ and bd quinol oxidases “seem to be upregulated in salt stressed cells” | [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677), 2022 | Mark uncertain/associational; wording in the source is cautious and respiratory necessity was not tested (hobmeier2022adaptationtovarying pages 1-2). |
| Compatible-solute transporter and ectoine-synthase genes **associate with** hypersaline adaptation | genome contained “glycine-betaine/carnitine/choline ABC transporters” and “ectoine synthase enzymes”; phenomics confirmed osmoadaptation | [10.3389/fmicb.2019.01304](https://doi.org/10.3389/fmicb.2019.01304), published 12 Jun 2019 | Useful corroboration in *V. dokdonensis* 21D, but its highlighted assay concerns MgCl₂ and cannot directly establish NaCl-delta-high (zeaiter2019phenomicsandgenomics pages 1-2). |
| Salinity-dependent strategy switching **modulates** intracellular Na⁺ | *E. salpumilio* showed “salt-in…at…100 PSU” and “salt-out…at…150 PSU” | [10.3389/fmicb.2022.960621](https://doi.org/10.3389/fmicb.2022.960621), published 5 Aug 2022 | Interesting eukaryotic evidence, but PSU is not equivalent to NaCl w/v and the transporter mechanism is unresolved (lee2022accumulationpatternsof pages 1-2). |

## 5. Quantitative evidence and recent developments

- *N. thermophilus* grows over 3.1–4.9 M Na⁺, with an optimum at 3.3–3.9 M. Its 2024 study compared 2.5, 3.1, 3.7, and 4.3 M Na⁺ and validated mRNA levels for 109 upregulated proteins by ddPCR. This is the best recent evidence that compatible-solute and salt-in mechanisms can operate simultaneously rather than as mutually exclusive alternatives (xing2024thepolyextremophilenatranaerobius pages 1-2).
- *A. sydowii* was compared at 1 M versus saturated 5.13 M NaCl. There were 1,842 differentially expressed genes, including 704 overexpressed genes; 42% of lncRNAs and 69% of transcription-factor RNAs were differentially expressed. This demonstrates system-wide regulatory remodeling, although it does not identify which changes are necessary for breadth (jimenezgomez2022survivinginthe pages 1-2).
- *W. ichthyophaga* has a measured 10–32% NaCl growth range and a 15–20% optimum. Glycerol increased with salinity, whereas intracellular Na⁺ and K⁺ remained relatively low under steady conditions and rose after hyperosmotic shock (zajc2014osmoadaptationstrategyof pages 1-2).
- In *H. elongata*, RNA-seq compared 0.17, 1, and 2 M NaCl on glucose or acetate. The study argues that tolerance involves ectoine, ion accumulation, sodium-efflux capacity, central metabolism, respiration, motility, and chemotaxis rather than one osmolyte pathway (hobmeier2022adaptationtovarying pages 1-2, hobmeier2022adaptationtovarying pages 14-16).
- A 2024 hypersaline-community study reconstructed 67 MAGs. Among medium/high-quality MetaSPAdes MAGs, predicted traits included salt tolerance in 91.3%, heavy-metal tolerance and exopolysaccharide synthesis in 95.6%, antioxidant synthesis in 60.86%, and iron acquisition in 91.3%. These are genomic predictions, not growth-breadth measurements or validated causal mechanisms (dindhoria2024metagenomicassembledgenomes pages 1-2).
- The 2023 Tuz Lake study analyzed 13 monthly samples from a lake reported at 32% w/v salt. PICRUSt2 predicted an important role for potassium-accumulation genes and seasonal changes in bacteriorhodopsin and halorhodopsin abundance. Because these functions were inferred from 16S profiles, they should not be curated as organism-level causal edges (dogan2023profilingthegenes pages 1-3).

## 6. Applications and real-world relevance

Extreme-euryhaline organisms are attractive chassis for high-salt or nonsterile fermentation because salt can suppress contaminants and compatible solutes such as ectoine and hydroxyectoine are valuable products. The *H. elongata* TeaABC mutant provides a concrete engineering principle: disrupting ectoine reuptake creates an ectoine-excreting phenotype, although productivity and robustness must be assessed independently (hobmeier2022adaptationtovarying pages 14-16).

Hypersaline organisms and enzymes are also candidates for saline-waste treatment, brine bioremediation, food processes, and biocatalysis where conventional proteins lose activity. Compatible solutes stabilize proteins and nucleic acids, but applications should not be represented as mechanisms of METPO:1000482 unless linked by organism-level growth assays (dindhoria2024metagenomicassembledgenomes pages 1-2, dogan2023profilingthegenes pages 1-3).

For agriculture, the 2024 MAG study proposes hypersaline microbiomes as sources of salt-tolerant plant-growth-promoting inoculants. However, its percentages describe annotated genomic potential, not demonstrated field efficacy. Such nodes belong in an application layer rather than the core trait-mechanism graph (dindhoria2024metagenomicassembledgenomes pages 1-2).

## 7. Recommended minimal graph expansion

A conservative next YAML revision could add the following modules while keeping taxon qualifiers in evidence annotations:

1. `high_external_NaCl -> induces -> compatible_solute_accumulation`
2. `Opu_ProU_transport -> increases -> intracellular_glycine_betaine`
3. `ectABC -> enables -> ectoine_biosynthesis`
4. `TeaABC -> enables -> ectoine_reuptake`
5. `compatible_solute_accumulation -> contributes_to -> osmotic_balance`
6. `Na_K_H_transport -> maintains -> intracellular_K_homeostasis`
7. `intracellular_K_accumulation -> contributes_to -> osmotic_balance`
8. `acidic_proteome -> supports -> protein_function_at_high_ionic_strength`
9. `high_external_NaCl -> induces -> HOG_network_remodeling`
10. `high_external_NaCl -> induces -> cell_wall_remodeling`
11. `osmotic_balance -> enables -> growth_across_wide_NaCl_range`

Edges 1–10 have source support at the indicated taxon or pathway level. Edge 11 is the integrating biological interpretation and should be marked **inferred** until a perturbation study directly shows contraction or expansion of the measured NaCl growth interval.

## 8. Warnings: claims not yet ready for TraitMech

1. **Do not curate gene presence → METPO:1000482.** MAG annotation, PICRUSt2 prediction, or an ectoine gene cluster cannot establish a measured NaCl breadth.
2. **Do not treat expression as necessity.** Most recent evidence is transcriptomic/proteomic; only TeaABC has a clear perturbational result in the retrieved literature.
3. **Do not assert that HOG is simply activated.** In *A. sydowii*, upstream components increased while `hog1`, `ssk2`, and `ste20` transcripts decreased; phosphorylation/activity was not measured (jimenezgomez2022survivinginthe pages 8-9).
4. **Do not generalize the hybrid strategy to all extreme-euryhaline organisms.** The 2024 result is strong but specific to *N. thermophilus* and unusual among characterized bacteria (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17).
5. **Do not equate Na⁺, NaCl, MgCl₂, PSU, and water activity.** Each captures a different physicochemical quantity.
6. **Do not infer growth from viability.** The no-growth-but-viable state at 50 PSU in *E. salpumilio* illustrates this distinction (lee2022accumulationpatternsof pages 1-2).
7. **Do not assign uncertain CURIEs.** Resolve ectoine, glycine betaine, transporter family, ENVO habitat, and strain-level NCBITaxon/UniProt identifiers against current ontology releases before committing YAML.
8. **Avoid universal directionality for individual paralogs.** In *N. thermophilus*, some Opu and ProU components were upregulated, unchanged, or downregulated depending on salinity (xing2024thepolyextremophilenatranaerobius pages 14-17).
9. **Separate acute acclimation from evolved adaptation.** Ion flux and transcription can change rapidly; acidic proteomes generally reflect longer-term evolutionary accommodation.

## 9. DOI-first bibliography

1. Xing Q. et al. “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress.” *Applied and Environmental Microbiology* 90(5). Published 5 April 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17)
2. Dindhoria K. et al. “Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils.” *mSystems* 9(3). Published 20 February 2024. DOI: [10.1128/msystems.01050-23](https://doi.org/10.1128/msystems.01050-23). (dindhoria2024metagenomicassembledgenomes pages 1-2)
3. Şahin Doğan S., Kocabaş A. “Profiling the genes associated with osmoadaptation and their variation seasonally in Tuz Lake.” Published September 2023. DOI: [10.53447/communc.1206230](https://doi.org/10.53447/communc.1206230). (dogan2023profilingthegenes pages 1-3)
4. Hobmeier K. et al. “Adaptation to Varying Salinity in *Halomonas elongata*: Much More Than Ectoine Accumulation.” *Frontiers in Microbiology* 13. Published 30 March 2022. DOI: [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677). (hobmeier2022adaptationtovarying pages 1-2, hobmeier2022adaptationtovarying pages 14-16)
5. Jiménez-Gómez I. et al. “Surviving in the Brine: A Multi-Omics Approach…” *Frontiers in Microbiology* 13. Published 2 May 2022. DOI: [10.3389/fmicb.2022.840408](https://doi.org/10.3389/fmicb.2022.840408). (jimenezgomez2022survivinginthe pages 1-2, jimenezgomez2022survivinginthe pages 8-9)
6. Lee H.B. et al. “Accumulation patterns of intracellular salts in…*Euplaesiobystra salpumilio*.” *Frontiers in Microbiology* 13. Published 5 August 2022. DOI: [10.3389/fmicb.2022.960621](https://doi.org/10.3389/fmicb.2022.960621). (lee2022accumulationpatternsof pages 1-2)
7. Zeaiter Z. et al. “Phenomics and Genomics Reveal Adaptation of *Virgibacillus dokdonensis* Strain 21D…” *Frontiers in Microbiology* 10. Published 12 June 2019. DOI: [10.3389/fmicb.2019.01304](https://doi.org/10.3389/fmicb.2019.01304). (zeaiter2019phenomicsandgenomics pages 1-2)
8. Zajc J. et al. “Osmoadaptation Strategy of the Most Halophilic Fungus, *Wallemia ichthyophaga*…” *Applied and Environmental Microbiology* 80:247–256. Published online 25 October 2013; issue January 2014. DOI: [10.1128/AEM.02702-13](https://doi.org/10.1128/AEM.02702-13). (zajc2014osmoadaptationstrategyof pages 1-2)
9. Oren A. “Microbial life at high salt concentrations: phylogenetic and metabolic diversity.” *Saline Systems* 4:2. Published April 2008. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2). (oren2008microbiallifeat pages 1-2, oren2008microbiallifeat pages 10-11)

**Overall curation assessment:** the evidence strongly supports adding modular osmolyte transport/synthesis, ion-homeostasis, proteome adaptation, fungal signaling/cell-wall remodeling, and energetic-response nodes. Nevertheless, most edges currently explain **high-salt acclimation**, not the complete causal basis of **growth breadth**. The final links from these modules to METPO:1000482 should therefore be taxon-qualified and marked inferred unless direct gene perturbation demonstrably changes both the lower and upper NaCl growth limits.

References

1. (zajc2014osmoadaptationstrategyof pages 1-2): Janja Zajc, Tina Kogej, Erwin A. Galinski, José Ramos, and Nina Gunde-Cimerman. Osmoadaptation strategy of the most halophilic fungus, wallemia ichthyophaga, growing optimally at salinities above 15% nacl. Applied and Environmental Microbiology, 80:247-256, Jan 2014. URL: https://doi.org/10.1128/aem.02702-13, doi:10.1128/aem.02702-13. This article has 131 citations and is from a peer-reviewed journal.

2. (jimenezgomez2022survivinginthe pages 1-2): Irina Jiménez-Gómez, Gisell Valdés-Muñoz, Aldo Moreno-Ulloa, Yordanis Pérez-Llano, Tonatiuh Moreno-Perlín, Hortencia Silva-Jiménez, Fernando Barreto-Curiel, María del Rayo Sánchez-Carbente, Jorge Luis Folch-Mallol, Nina Gunde-Cimerman, Asunción Lago-Lestón, and Ramón Alberto Batista-García. Surviving in the brine: a multi-omics approach for understanding the physiology of the halophile fungus aspergillus sydowii at saturated nacl concentration. Frontiers in Microbiology, May 2022. URL: https://doi.org/10.3389/fmicb.2022.840408, doi:10.3389/fmicb.2022.840408. This article has 33 citations and is from a peer-reviewed journal.

3. (oren2008microbiallifeat pages 1-2): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

4. (oren2008microbiallifeat pages 10-11): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

5. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

6. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

7. (hobmeier2022adaptationtovarying pages 1-2): Karina Hobmeier, Martina Cantone, Quynh Anh Nguyen, Katharina Pflüger-Grau, Andreas Kremling, Hans Jörg Kunte, Friedhelm Pfeiffer, and Alberto Marin-Sanguino. Adaptation to varying salinity in halomonas elongata: much more than ectoine accumulation. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.846677, doi:10.3389/fmicb.2022.846677. This article has 53 citations and is from a peer-reviewed journal.

8. (jimenezgomez2022survivinginthe pages 8-9): Irina Jiménez-Gómez, Gisell Valdés-Muñoz, Aldo Moreno-Ulloa, Yordanis Pérez-Llano, Tonatiuh Moreno-Perlín, Hortencia Silva-Jiménez, Fernando Barreto-Curiel, María del Rayo Sánchez-Carbente, Jorge Luis Folch-Mallol, Nina Gunde-Cimerman, Asunción Lago-Lestón, and Ramón Alberto Batista-García. Surviving in the brine: a multi-omics approach for understanding the physiology of the halophile fungus aspergillus sydowii at saturated nacl concentration. Frontiers in Microbiology, May 2022. URL: https://doi.org/10.3389/fmicb.2022.840408, doi:10.3389/fmicb.2022.840408. This article has 33 citations and is from a peer-reviewed journal.

9. (hobmeier2022adaptationtovarying pages 14-16): Karina Hobmeier, Martina Cantone, Quynh Anh Nguyen, Katharina Pflüger-Grau, Andreas Kremling, Hans Jörg Kunte, Friedhelm Pfeiffer, and Alberto Marin-Sanguino. Adaptation to varying salinity in halomonas elongata: much more than ectoine accumulation. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.846677, doi:10.3389/fmicb.2022.846677. This article has 53 citations and is from a peer-reviewed journal.

10. (zeaiter2019phenomicsandgenomics pages 1-2): Zahraa Zeaiter, Ramona Marasco, Jenny M. Booth, Erica M. Prosdocimi, Francesca Mapelli, Matteo Callegari, Marco Fusi, Grégoire Michoud, Francesco Molinari, Daniele Daffonchio, Sara Borin, and Elena Crotti. Phenomics and genomics reveal adaptation of virgibacillus dokdonensis strain 21d to its origin of isolation, the seawater-brine interface of the mediterranean sea deep hypersaline anoxic basin discovery. Frontiers in Microbiology, Jun 2019. URL: https://doi.org/10.3389/fmicb.2019.01304, doi:10.3389/fmicb.2019.01304. This article has 13 citations and is from a peer-reviewed journal.

11. (lee2022accumulationpatternsof pages 1-2): Hyeon Been Lee, Dong Hyuk Jeong, and Jong Soo Park. Accumulation patterns of intracellular salts in a new halophilic amoeboflagellate, euplaesiobystra salpumilio sp. nov., (heterolobosea; discoba) under hypersaline conditions. Frontiers in Microbiology, Aug 2022. URL: https://doi.org/10.3389/fmicb.2022.960621, doi:10.3389/fmicb.2022.960621. This article has 7 citations and is from a peer-reviewed journal.

12. (dogan2023profilingthegenes pages 1-3): Suzan SAHİN DOGAN and Aytaç KOCABAŞ. Profiling the genes associated with osmoadaptation and their variation by seasonally in tuz lake. Communications Faculty of Science University of Ankara Series C Biology Geological Engineering and Geophysical Engineering, 32:174-191, Sep 2023. URL: https://doi.org/10.53447/communc.1206230, doi:10.53447/communc.1206230. This article has 4 citations.

13. (dindhoria2024metagenomicassembledgenomes pages 1-2): Kiran Dindhoria, Raghawendra Kumar, Bhavya Bhargava, and Rakshak Kumar. Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils. Mar 2024. URL: https://doi.org/10.1128/msystems.01050-23, doi:10.1128/msystems.01050-23. This article has 27 citations and is from a peer-reviewed journal.