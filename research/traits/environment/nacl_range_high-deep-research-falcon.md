---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:50:08.234342'
end_time: '2026-08-04T01:54:59.292022'
duration_seconds: 291.06
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range high
  trait_identifier: METPO:1000472
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl range phenotype in which the growth-supporting NaCl range extends
    above approximately 8% (w/v), characteristic of extreme-halophile organisms.
  parent_traits: METPO:1000334
  synonyms: Extreme halophile, NaR_>8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation
    review supports growth ranges extending above 8% NaCl as the extreme-halophile
    category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum
    (Saline-Systems review supports salt-in physiology underlying extended high-salt
    growth.)'
  causal_graph_summary: 'nacl_range_high_extreme_halophile: 10 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000472
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range extends above approximately 8% (w/v), characteristic of extreme-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Extreme halophile, NaR_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports growth ranges extending above 8% NaCl as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports salt-in physiology underlying extended high-salt growth.)
- **Existing causal graph summary:** nacl_range_high_extreme_halophile: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **NaCl range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_high.yaml`.

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
- **Trait label:** NaCl range high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000472
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range extends above approximately 8% (w/v), characteristic of extreme-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Extreme halophile, NaR_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports growth ranges extending above 8% NaCl as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports salt-in physiology underlying extended high-salt growth.)
- **Existing causal graph summary:** nacl_range_high_extreme_halophile: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **NaCl range high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_high.yaml`.

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


# Curation report: NaCl range high

**Trait:** “NaCl range high”  
**Identifier:** `METPO:1000472`  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** `METPO:1000334`  
**Working definition:** a growth-supporting NaCl range whose upper boundary extends above approximately 8% (w/v), corresponding to >80 g/L NaCl and characteristic of extreme halophily.

## 1. Scope and boundaries

This trait should encode an **assay-observed growth-range capacity**, not merely exposure to a hypersaline habitat or possession of an osmoadaptation gene. The decisive observation is reproducible growth at one or more NaCl concentrations above approximately 8% (w/v). For example, *Halorubrum kocurii* 2020YC7 has reported optimal growth at 150–250 g/L NaCl—15–25% (w/v)—and therefore clearly falls within the trait scope. Its physiological experiments covered 50–250 g/L NaCl. (ding2022theosmoprotectantswitch pages 4-6, ding2022theosmoprotectantswitch pages 2-4)

Important distinctions are:

- **Range versus optimum:** an optimum above 8% strongly supports the class, but an organism can qualify when only the upper growth limit exceeds 8%. Conversely, an optimum below 8% does not exclude qualification if growth continues above the threshold.
- **Growth versus survival/tolerance:** viability after acute salt shock, transient biomass persistence, or stress-gene induction is insufficient without evidence of growth.
- **NaCl versus total salinity:** environmental total dissolved salts, mixed-brine salinity, and chaotropicity are not numerically interchangeable with NaCl (w/v). Danakil organisms thriving above 30% total salinity are highly relevant mechanistically, but these environmental observations should not automatically be converted into an exact NaCl growth range. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **Extreme versus moderate halophily:** the supplied operational threshold is approximately 8% NaCl. Traditional labels vary among sources, so measured concentration should take precedence over the words “moderate,” “extreme,” or “halo-tolerant.”
- **Obligate halophile versus high upper range:** a high minimum NaCl requirement is a separate property. `METPO:1000472` should not imply obligate halophily unless minimum-growth data also establish it.
- **Stable versus fluctuating salinity:** capacity to withstand rapid changes may depend on hybrid regulation and should be modeled as an environmental modifier, not as synonymous with high NaCl range. The 2024 Dead Sea study inferred that frequent, abrupt salinity changes select for scalable salt-in/salt-out systems. (ionescu2024extremefluctuationsin pages 1-2)

## 2. Mechanistic model and current understanding

The strongest general model is that high external NaCl lowers water activity and imposes osmotic stress. Extreme halophiles compensate through one or both of two modules:

1. **Salt-in:** accumulation of intracellular K+, with accompanying anions, offsets external osmotic pressure. This requires ion uptake/efflux control and a proteome adapted to function at molar ionic strength.
2. **Salt-out:** synthesis or uptake of compatible organic solutes—such as glycine betaine, ectoine, proline betaine, or trehalose—raises cytoplasmic osmolarity without requiring the entire proteome to operate in concentrated salt.

These are not mutually exclusive categories. Quantitative work in *H. kocurii* showed K+ dominance at 100–200 g/L NaCl but a switch toward exogenous glycine betaine at 200–250 g/L. Recent environmental genomics likewise reports hybrid systems in Dead Sea bacteria and *Halogeometricum*. (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 8-13, strakova2024unveilingthegenomic pages 16-17, ionescu2024extremefluctuationsin pages 1-2)

A major 2024 result strengthens the salt-in/proteome link: organisms from Danakil brines had median predicted protein isoelectric points ≤4.4, while extreme halophiles can accumulate intracellular K+ up to approximately 4 M. Enrichment in glutamate and aspartate is interpreted as maintaining protein solubility and function under high intracellular salt. Haloarchaea and Nanohaloarchaeota represented 99% of communities under the most extreme Western-Canyon Lake conditions. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

## 3. Candidate nodes

### Trait and environmental nodes

- `METPO:1000472` — NaCl range high, quoted verbatim.
- `METPO:1000334` — supplied parent trait.
- High external NaCl concentration — retain as a concentration-qualified environmental node.
- Hyperosmotic stress / reduced water activity — candidate process/environmental state.
- Fluctuating salinity regime — candidate modifier; not equivalent to the target trait.
- Growth above approximately 8% (w/v) NaCl — assay endpoint.

### Chemicals and metabolites

High-confidence ontology candidates, subject to identifier validation against the project’s ontology release:

- Sodium chloride — **CHEBI:26710**.
- Potassium ion — **CHEBI:29103**.
- Sodium ion — **CHEBI:29101**.
- Chloride — **CHEBI:17996**.
- Glycine betaine — **CHEBI:17750**.
- Trehalose — **CHEBI:27082**.
- L-glutamate — **CHEBI:29985**.
- L-aspartate — **CHEBI:29991**.
- Ectoine, proline betaine, choline, glutamine, and KCl — useful candidates, but their exact CURIEs should be resolved programmatically rather than entered from memory.

### Genes, proteins, and transport systems

Use label-only or database-resolved protein-family nodes until organism-specific accessions are obtained:

- **TrkA/TrkH potassium-uptake system**.
- **Kch potassium channel**.
- **KefB potassium-efflux system**.
- **BCCT-family betaine/carnitine/choline transporter**.
- **TreS trehalose synthase** and **SugA-associated transport**.
- **YrbG Na+/Ca²+ antiporter**.
- **NhaC and Mrp sodium-homeostasis systems**.
- **Opu-family ABC compatible-solute transporter**.
- **MscS/MscL mechanosensitive channels**.
- KdpFABC and KtrAB/KtrCD are biologically plausible candidates but are not directly established as trait-causing components by the strongest evidence retrieved here.

### Cellular and process nodes

- Cytoplasmic K+ accumulation / salt-in osmoadaptation.
- Compatible-solute uptake and accumulation / salt-out osmoadaptation.
- Sodium extrusion.
- Intracellular osmotic balance and turgor maintenance.
- Acidic-proteome adaptation.
- Protein stabilization at high ionic strength.
- Mechanosensitive pressure release.
- NaCl-supported cellular growth.

### Taxon/context nodes

- *Halorubrum kocurii* 2020YC7 — strongest quantitative transporter/metabolite case.
- *Halogeometricum* spp. — recent comparative-genomic hybrid-strategy case.
- Danakil haloarchaea and Nanohaloarchaeota — recent community/proteome evidence.
- Dead Sea spring bacteria, including *Prosthecochloris*, *Flexistipes*, *Izemoplasma*, *Halomonas*, and *Halanaerobium* MAGs — environmental hybrid-strategy hypothesis.
- *Halobacillus halophilus* — chloride-regulation boundary case; moderate-halophile evidence should not be generalized automatically.

## 4. Candidate causal edges

The compact table below separates measured evidence from genomic inference and environmental hypothesis.

| subject | predicate | object | evidence mode (measured/genomic inference/hypothesis) | taxon/context | quantitative support | DOI |
|---|---|---|---|---|---|---|
| High external NaCl | increases | intracellular K+ accumulation | measured | *Halorubrum kocurii* 2020YC7 grown at 50–250 g/L NaCl | intracellular K+ rose to 28.67 µmol/mg protein at 200 g/L NaCl; 7.5× higher than at 50 g/L NaCl (ding2022theosmoprotectantswitch pages 6-8) | 10.3390/genes13060939 |
| trkA/trkH/kch K+ uptake system | contributes to | salt-in osmoadaptation at high NaCl | measured + genomic inference | *H. kocurii* 2020YC7 | trkH transcript abundance was ~500× higher at 250 vs 50 g/L NaCl; genome encodes trkA, trkH, kch (ding2022theosmoprotectantswitch pages 6-8, ding2022theosmoprotectantswitch pages 1-2) | 10.3390/genes13060939 |
| kefB K+ exporter | enables | K+ discharge during osmoadaptation | genomic inference | *H. kocurii* 2020YC7 genome | kefB identified in osmoadaptation gene set; supports regulated K+ efflux rather than constitutive retention (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8) | 10.3390/genes13060939 |
| Salt-in strategy | requires/adapts with | acidic proteome | measured | archaea from Danakil Western-Canyon Lakes | median predicted protein pI ≤4.4; extreme halophiles reported to accumulate up to 4 M K+ with excess acidic amino acids (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | 10.1038/s41559-024-02505-6 |
| Elevated acidic amino acid content | may facilitate | cation binding under hypersalinity | genomic inference | *H. kocurii* 2020YC7 | acidic amino acids 17.14% vs 8.93–13.97% in comparator species (ding2022theosmoprotectantswitch pages 4-6) | 10.3390/genes13060939 |
| Exogenous glycine betaine uptake | replaces part of | K+-based osmoprotection at very high NaCl | measured | *H. kocurii* 2020YC7 with added glycine betaine | glycine betaine became primary osmotic solute at 200–250 g/L NaCl; accumulated up to 15.27 mg/mg protein; intracellular K+ decreased after glycine betaine addition (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 8-13, ding2022theosmoprotectantswitch pages 13-14) | 10.3390/genes13060939 |
| bcct-family compatible-solute transporters | mediates uptake of | glycine betaine | genomic inference with physiological support | *H. kocurii* 2020YC7 | no glycine betaine synthesis genes detected, but BCCT transporters present; phenotype shows glycine betaine accumulation at high NaCl (ding2022theosmoprotectantswitch pages 6-8, ding2022theosmoprotectantswitch pages 8-13) | 10.3390/genes13060939 |
| treS-dependent trehalose production | contributes to | osmoadaptation at relatively lower salt | measured + genomic inference | *H. kocurii* 2020YC7 at 50–100 g/L NaCl | trehalose decreased from ~5.00 to 2.67 mg/mg protein as NaCl rose from 50 to 250 g/L; treS expression highest at lower salinity (ding2022theosmoprotectantswitch pages 6-8, ding2022theosmoprotectantswitch pages 1-2) | 10.3390/genes13060939 |
| YrbG Na+/Ca2+ antiport system | contributes to | Na+ extrusion under hypersalinity | genomic inference | *Halogeometricum* spp. comparative genomics | identified across six species as part of dual osmoregulatory adaptation; not directly assayed here (strakova2024unveilingthegenomic pages 16-17) | 10.3389/fmars.2024.1421769 |
| Compatible-solute transport systems | broadens capacity for | salt-out osmoadaptation | genomic inference | *Halogeometricum* spp. | all six species encoded transport for trehalose, glycine betaine, proline betaine, ectoine, and choline; two strains additionally encoded Opu-family ABC transporters (strakova2024unveilingthegenomic pages 16-17) | 10.3389/fmars.2024.1421769 |
| Fluctuating salinity regime | selects for | hybrid salt-in/salt-out osmoregulation | hypothesis supported by genomic inference | Dead Sea spring biofilm MAGs | MAGs from five bacterial taxa contained genes for both strategies; system experiences drastic salinity fluctuations and bacterial concentrations of 10^4–10^5 cells/mL under normal Dead Sea conditions (ionescu2024extremefluctuationsin pages 1-2) | 10.3389/frmbi.2023.1329925 |
| Chloride | signals/regulates | growth-linked osmoadaptation processes | measured | *Halobacillus halophilus* chloride-dependent moderate halophile | chloride-dependent regulation reported for growth and glycine betaine transport, but species is a moderate halophile and evidence is not specific to >8% NaCl extreme-halophile phenotype (saum2008regulationofosmoadaptation pages 13-14) | 10.1186/1746-1448-4-4 |


*Table: This table compacts the strongest source-backed candidate edges relevant to METPO:1000472, separating measured physiology from genomic inference and hypothesis. It is useful for deciding which mechanisms are ready for TraitMech curation versus those needing caution.*

### Recommended high-confidence core for an initial graph

The following reduced chain is the most defensible starting point:

1. **high external NaCl → induces/increases → K+ uptake and intracellular K+ accumulation**;
2. **TrkA/TrkH/Kch system → contributes to → intracellular K+ accumulation**;
3. **intracellular K+ accumulation → contributes to → osmotic balance at high NaCl**;
4. **salt-in osmoadaptation → is associated with/requires → acidic-proteome adaptation**;
5. **acidic-proteome adaptation → supports → protein function at high intracellular ionic strength**;
6. **osmotic balance plus salt-adapted protein function → enables → growth above approximately 8% NaCl**.

The first two links have organism-specific expression and physiological support in *H. kocurii*: intracellular K+ reached 28.67 µmol/mg protein at 200 g/L NaCl, and *trkH* expression was approximately 500-fold higher at 250 than at 50 g/L. The fourth and fifth links are supported strongly at comparative/proteome level, but “requires” should be represented cautiously because direct perturbation was not reported in the retrieved 2024 study. (ding2022theosmoprotectantswitch pages 6-8, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

### Optional taxon-specific branch

For *H. kocurii* under supplied-glycine-betaine conditions:

- **external glycine betaine → BCCT-dependent uptake → intracellular glycine betaine**;
- **intracellular glycine betaine at 200–250 g/L NaCl → partially replaces → K+-based osmoprotection**;
- **osmoprotectant switching → supports → growth under very high NaCl**.

Glycine betaine reached 15.27 mg/mg protein, while intracellular K+ and trehalose declined after supplementation. Because the phenotype depends on exogenous betaine, this branch must carry an experimental-condition qualifier. (ding2022theosmoprotectantswitch pages 8-13, ding2022theosmoprotectantswitch pages 13-14)

Trehalose should not be modeled as the principal extreme-salt solute in this organism: its concentration fell from approximately 5.00 to 2.67 mg/mg protein between 50 and 250 g/L NaCl, and *treS* expression was greatest at relatively low salinity. (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8)

## 5. Recent developments, applications, and statistics

### 2024 research developments

- **Proteome extremity near life limits:** Danakil WCL archaea encoded the most acidic proteomes reported in the study, with median pI ≤4.4. Haloarchaea and Nanohaloarchaeota comprised 99% of the most extreme communities, and organisms were observed in salt-saturating conditions above 30% total salinity. This is authoritative comparative evidence connecting environmental extremity, salt-in physiology, and proteome acidification. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **Hybrid strategies in fluctuating environments:** five Dead Sea bacterial MAGs contained combinations of salt-in and salt-out genes. The authors explicitly framed environmental selection for a scalable hybrid strategy as a hypothesis, not a directly demonstrated causal evolutionary result. Reported bacterial concentrations under normal Dead Sea conditions were 10⁴–10⁵ cells/mL. (ionescu2024extremefluctuationsin pages 1-2)
- **Hybrid haloarchaeal osmoregulation:** comparative genomics of six *Halogeometricum* species found ion-transport and compatible-solute systems; all six encoded transport potential for trehalose, glycine betaine, proline betaine, ectoine, and choline. Two strains also encoded Opu-family ABC transporters. These are genomic capabilities rather than transporter knockouts or flux measurements. (strakova2024unveilingthegenomic pages 16-17)

### Real-world applications

High-salt growth enables bioprocesses in brines where conventional organisms fail and contamination pressure may be lower. The most direct application evidence retrieved concerns *Halogeometricum* isolates: experimental assays confirmed tolerance to arsenic, cadmium, and lead, prompting proposed use in bioremediation of metal-contaminated hypersaline environments. Salt-range phenotype and metal resistance remain distinct traits, however; neither should be treated as causing the other without additional experiments. (strakova2024unveilingthegenomic pages 16-17)

Other plausible uses—hypersaline wastewater treatment, compatible-solute production, salt-stable enzymes, pigments, and astrobiology—are scientifically credible but were not directly established by the retrieved mechanistic sources and therefore should not be added as causal graph edges.

## 6. Expert interpretation

The current evidence favors a **modular, conditional graph**, rather than a single universal extreme-halophile pathway. Salt-in physiology and acidic proteomes form the most broadly supported core for haloarchaea and some extreme halophilic bacteria. Compatible-solute transport can supplement or replace K+ under particular salinity and nutrient conditions. Recent research further indicates that salinity stability matters: stable saturation may favor a constitutive salt-in/acidic-proteome solution, whereas fluctuating systems may favor hybrid regulation. This latter evolutionary interpretation remains partly inferential. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, ionescu2024extremefluctuationsin pages 1-2)

Gene presence alone should be represented as **enabling potential**, not as causing `METPO:1000472`. The strongest causal evidence would require deletion or repression of a transporter or proteome-adaptation determinant followed by a measured loss or narrowing of the NaCl growth range, ideally with genetic complementation. None of the retrieved recent studies supplies that complete intervention chain.

## 7. Warnings and claims not yet ready for TraitMech

1. **Do not curate “hypersaline habitat → NaCl range high” as a direct causal edge.** Habitat detection or MAG recovery does not demonstrate growth range.
2. **Do not translate total salinity directly into NaCl (w/v).** Danakil and Dead Sea brines contain mixed ions and additional stresses.
3. **Do not treat predicted transporter genes as active mechanisms without qualification.** *Halogeometricum* and Dead Sea MAG findings are primarily genomic inference. (strakova2024unveilingthegenomic pages 16-17, ionescu2024extremefluctuationsin pages 1-2)
4. **Do not universalize the glycine-betaine switch.** It was measured in one *H. kocurii* strain and depended on exogenous glycine betaine. (ding2022theosmoprotectantswitch pages 8-13)
5. **Do not curate trehalose as a high-salt driver in *H. kocurii*.** Its abundance and *treS* expression declined as NaCl increased. (ding2022theosmoprotectantswitch pages 6-8)
6. **Do not use acidic-proteome pI as a phenotype assay.** It is a strong mechanistic signature of salt-in adaptation, not direct evidence of growth above 8% NaCl.
7. **Treat chloride signaling as a boundary-case branch.** Chloride regulates growth and osmolyte transport in moderate-halophilic *H. halophilus*, but taxon transfer to extreme haloarchaea is unsupported. (saum2008regulationofosmoadaptation pages 13-14)
8. **Avoid GC-content → high-salt growth.** The proposed DNA-stabilization interpretation in *H. kocurii* is correlational and unsuitable as a curated causal edge. (ding2022theosmoprotectantswitch pages 4-6)
9. **Do not assign gene-family identifiers as organism-specific genes.** Resolve NCBITaxon, UniProt, KEGG orthology, and protein accessions against the exact strain genome before YAML insertion.
10. **Record assay metadata:** medium composition, NaCl units, temperature, pH, aeration, inoculum, growth metric, duration, and whether compatible solutes were supplied.

## 8. DOI-first bibliography

1. Gutiérrez-Preciado A, et al. “Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines.” *Nature Ecology & Evolution* 8:1856–1869. **Published August 2024.** DOI: [10.1038/s41559-024-02505-6](https://doi.org/10.1038/s41559-024-02505-6). (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
2. Straková D, Sánchez-Porro C, de la Haba RR, Ventosa A. “Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus *Halogeometricum*: spotlight on thiamine biosynthesis.” *Frontiers in Marine Science* 11. **Published October 2024.** DOI: [10.3389/fmars.2024.1421769](https://doi.org/10.3389/fmars.2024.1421769). (strakova2024unveilingthegenomic pages 16-17)
3. Ionescu D, Zoccarato L, Cabello-Yeves PJ, Tikochinski Y. “Extreme fluctuations in ambient salinity select for bacteria with a hybrid ‘salt-in’/‘salt-out’ osmoregulation strategy.” *Frontiers in Microbiomes* 2. **Published January 2024**; DOI registered as 2023. DOI: [10.3389/frmbi.2023.1329925](https://doi.org/10.3389/frmbi.2023.1329925). (ionescu2024extremefluctuationsin pages 1-2, ionescu2024extremefluctuationsin pages 6-7)
4. Ding R, Yang N, Liu J. “The Osmoprotectant Switch of Potassium to Compatible Solutes in an Extremely Halophilic Archaea *Halorubrum kocurii* 2020YC7.” *Genes* 13:939. **Published May 2022.** DOI: [10.3390/genes13060939](https://doi.org/10.3390/genes13060939). (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8)
5. Saum SH, Müller V. “Regulation of osmoadaptation in the moderate halophile *Halobacillus halophilus*: chloride, glutamate and switching osmolyte strategies.” *Saline Systems* 4:4. **Published April 2008.** DOI: [10.1186/1746-1448-4-4](https://doi.org/10.1186/1746-1448-4-4). (saum2008regulationofosmoadaptation pages 13-14)

**Curation recommendation:** begin with the measured *H. kocurii* K+-uptake/accumulation branch and the broadly supported acidic-proteome branch. Add compatible-solute, sodium-extrusion, mechanosensitive-channel, chloride-signaling, and fluctuating-salinity branches only with explicit taxon, assay, and evidence-strength qualifiers.

References

1. (ding2022theosmoprotectantswitch pages 4-6): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

2. (ding2022theosmoprotectantswitch pages 2-4): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

3. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 22 citations and is from a highest quality peer-reviewed journal.

4. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.

5. (ding2022theosmoprotectantswitch pages 1-2): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

6. (ding2022theosmoprotectantswitch pages 8-13): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

7. (strakova2024unveilingthegenomic pages 16-17): Dáša Straková, Cristina Sánchez-Porro, Rafael R. de la Haba, and Antonio Ventosa. Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus halogeometricum: spotlight on thiamine biosynthesis. Frontiers in Marine Science, Oct 2024. URL: https://doi.org/10.3389/fmars.2024.1421769, doi:10.3389/fmars.2024.1421769. This article has 7 citations.

8. (ding2022theosmoprotectantswitch pages 6-8): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

9. (ding2022theosmoprotectantswitch pages 13-14): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

10. (saum2008regulationofosmoadaptation pages 13-14): Stephan H Saum and Volker Müller. Regulation of osmoadaptation in the moderate halophile halobacillus halophilus: chloride, glutamate and switching osmolyte strategies. Saline Systems, 4:4-4, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-4, doi:10.1186/1746-1448-4-4. This article has 162 citations.

11. (ionescu2024extremefluctuationsin pages 6-7): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.