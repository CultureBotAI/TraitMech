---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:41:11.597599'
end_time: '2026-08-04T01:59:44.959281'
duration_seconds: 1113.36
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum high
  trait_identifier: METPO:1000468
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum_high
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl optimum phenotype with the best-growth NaCl concentration above
    approximately 8% (w/v), corresponding to extreme-halophile physiology.
  parent_traits: METPO:1000333
  synonyms: Extreme halophile, NaO_>8
  evidence_summary: 'DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation
    review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2:
    KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in
    (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)'
  causal_graph_summary: 'nacl_optimum_high_extreme_halophile: 11 nodes, 9 edges'
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
- **Trait label:** NaCl optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000468
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration above approximately 8% (w/v), corresponding to extreme-halophile physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Extreme halophile, NaO_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)
- **Existing causal graph summary:** nacl_optimum_high_extreme_halophile: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_high.yaml`.

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
- **Trait label:** NaCl optimum high
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000468
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl optimum phenotype with the best-growth NaCl concentration above approximately 8% (w/v), corresponding to extreme-halophile physiology.
- **Parent traits:** METPO:1000333
- **Synonyms:** Extreme halophile, NaO_>8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: extreme halophile (Osmoadaptation review supports >8% NaCl optimum as the extreme-halophile category.) | DOI:10.1186/1746-1448-4-2: KCl accumulating Halobacterium salinarum (Saline-Systems review supports the salt-in (intracellular KCl) strategy as the mechanism for extreme-halophile growth.)
- **Existing causal graph summary:** nacl_optimum_high_extreme_halophile: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl optimum high** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum_high.yaml`.

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


# Curation report: NaCl optimum high

## Executive summary

**Target trait:** **NaCl optimum high**  
**Identifier:** **METPO:1000468**  
**Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED  
**Parent:** METPO:1000333  
**Operational definition:** best growth above approximately **8% (w/v) NaCl**, corresponding to a high-salt-optimum or extreme-halophile-like phenotype.

The trait should be represented primarily as an **experimentally measured growth optimum**, not as a generic salt-tolerance genotype. Its strongest general mechanistic backbone is: high extracellular NaCl imposes osmotic imbalance; cells restore water and turgor balance through either intracellular inorganic-ion accumulation (“salt-in”), organic compatible-solute accumulation (“salt-out”), or a taxon- and condition-dependent hybrid; salt-in organisms additionally require a proteome adapted to high ionic strength. Direct data from an extremely halophilic archaeon support salinity-dependent Trk-mediated K⁺ accumulation, while 2024 work adds evidence for membrane-lipid remodeling and genomically inferred hybrid strategies. Nevertheless, no single mechanism is necessary or sufficient across all taxa with this phenotype. (ding2022theosmoprotectantswitch pages 1-2, oren2008microbiallifeat pages 1-2, ionescu2024extremefluctuationsin pages 1-2, ugwuodo2024changesinenvironmental pages 1-2)

## 1. Trait scope and boundaries

### 1.1 What the trait represents

**METPO:1000468 should mean the NaCl concentration at which a strain’s measured growth rate or yield is maximal exceeds approximately 8% w/v.** Because 8% w/v NaCl is about 80 g/L or 1.37 M, this threshold lies below the conventional lower boundary for “extreme halophiles” in the Kushner classification. Oren’s authoritative review gives conventional ranges of **2.5–5.2 M** for extreme halophiles, **1.5–4.0 M** for borderline extreme halophiles, and **0.5–2.5 M** for moderate halophiles. Thus the METPO label’s synonym “extreme halophile” is useful shorthand but is not taxonomically or physiologically identical to the classical 2.5-M boundary. (oren2008microbiallifeat pages 1-2)

A direct boundary example is *Spiribacter salinus*: it showed no growth below 0.4 M NaCl, optimum growth at 0.8 M, and tolerance to 2.0 M. It is conventionally a moderate halophile, but its 0.8-M optimum—approximately 4.7% w/v—does **not** meet METPO:1000468, even though its upper tolerance exceeds 8%. This illustrates why maximum tolerated NaCl must not be substituted for optimum NaCl. (leon2018compatiblesolutesynthesis pages 4-5)

Conversely, ten *Halomonas* isolates in a 2024 study had optima at **10–15% NaCl** and tolerated 25%; these satisfy the supplied METPO threshold even though the authors classified the isolates as moderate halophiles rather than classical extreme halophiles. (reang2024extremozymesandcompatible pages 4-5, reang2024extremozymesandcompatible pages 2-3)

### 1.2 Recommended assay interpretation

A positive annotation should require:

1. A NaCl gradient containing values below and above 8% w/v.
2. A growth endpoint such as maximum specific growth rate, final biomass, colony expansion, or another explicitly defined growth measure.
3. The best observed value above the threshold, preferably with replication and a sufficiently resolved concentration series.
4. Medium composition, temperature, pH, aeration, carbon source, and growth phase recorded because these can shift the apparent optimum.

The phenotype is condition-dependent. For example, *Halanaerobium congolense* WG10 was studied at 7%, 13%, and 20% NaCl, with **13% designated the optimum** and 20% hypersaline stress. That is a direct, trait-compatible optimum, whereas lipid changes at 20% concern tolerance beyond the optimum. (ugwuodo2024changesinenvironmental pages 1-2)

### 1.3 Nearby traits that must remain distinct

- **High NaCl tolerance:** growth or survival at >8%, even if optimum is lower.
- **Obligate halophily / minimum salt requirement:** inability to grow at low NaCl; related but not equivalent to a high optimum.
- **Maximum NaCl tolerated:** upper growth boundary, not the optimum.
- **Osmotic-stress resistance:** may be caused by sugars or other salts and need not imply a NaCl optimum.
- **Chloride dependence:** specific dependence on Cl⁻ signaling or physiology, separable from total NaCl optimum.
- **Fluctuating-salinity adaptation:** favors rapid or hybrid regulation and is not identical to growth at a stable high-salt optimum. Dead Sea spring MAGs illustrate this distinction. (ionescu2024extremefluctuationsin pages 1-2)
- **Haloalkaliphily, halothermophily, or chaotolerance:** compound environmental traits requiring separate annotations.

## 2. Current mechanistic understanding

### 2.1 Salt-in strategy

Salt-in organisms accumulate molar intracellular KCl to approximate external osmotic pressure. This is widespread in haloarchaea and also occurs in phylogenetically distant bacteria such as Halanaerobiales and *Salinibacter*. The strategy is relatively inexpensive in osmolyte synthesis but forces essentially the entire intracellular molecular system to function at high ionic strength. (oren2008microbiallifeat pages 1-2)

In *Halorubrum kocurii* 2020YC7, genomic, physiological, and RT-qPCR measurements identified *trkA*, *trkH*, and *kch* for K⁺ uptake and *kefB* for K⁺ export. Intracellular K⁺ increased from **8.17 to 28.67 μmol/mg protein** as salinity increased from 100 to 200 g/L; at 200 g/L it was about **7.5-fold** the level measured at 50 g/L. Expression of *trkH* increased approximately **500-fold** between 50 and 250 g/L NaCl. These measurements strongly support a causal chain from high external NaCl through Trk-system induction to intracellular K⁺ accumulation, although individual-gene knockout evidence was not reported. (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8)

### 2.2 Acidic proteome adaptation

KCl accumulation is viable only when proteins remain soluble and functional at high ionic strength. Salt-in organisms typically have proteomes enriched in acidic residues; haloarchaeal proteins also tend to have reduced surface hydrophobicity and abundant negative surface charge, which supports hydrated cation networks. Such proteins may denature or lose stability at low salt, helping explain obligate or strong halophily. (oren2008microbiallifeat pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4)

In *H. kocurii*, acidic amino acids constituted **17.14%** of the proteome, compared with 8.93–13.97% in the comparison species reported by the authors. This is supportive comparative evidence, but it does not establish that proteome acidification alone produces a >8% NaCl optimum. (ding2022theosmoprotectantswitch pages 4-6)

### 2.3 Compatible-solute strategy

Salt-out organisms limit cytoplasmic inorganic ions and synthesize or import organic osmolytes such as ectoine, glycine betaine, trehalose, amino-acid derivatives, sugars, and polyols. These solutes support osmotic balance while interfering relatively little with normal enzyme function; this strategy is common in halophilic bacteria and permits wider salinity ranges, but it is energetically more expensive than ion accumulation. (leon2018compatiblesolutesynthesis pages 1-2, oren2008microbiallifeat pages 1-2)

Mechanisms can switch with salinity and substrate availability. In *H. kocurii*, K⁺ dominated without supplied osmolyte, but exogenous glycine betaine accumulated to **15.27 mg/mg protein at 200–250 g/L NaCl** and became the primary osmotic solute. Two BCCT-family transporter genes were identified, and glycine betaine altered potassium-transporter expression. Trehalose declined from **5.26 to 2.61 mg/mg protein** as NaCl increased from 50 to 250 g/L, indicating that it functioned mainly at 50–100 g/L rather than at the highest salinities. The glycine-betaine uptake phenotype is direct, but assigning it specifically to either BCCT gene remains partly inferential without transporter mutants. (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8, ding2022theosmoprotectantswitch pages 2-4)

In *S. salinus*, ectoine synthesis and salinity-regulated glycine-betaine import were demonstrated experimentally. Radiolabeled glycine betaine was accumulated intact, protected growth, and suppressed ectoine synthesis; ectoine genes occurred in a noncanonical, separated *ectAC*/*ectB* organization. This is strong mechanism evidence for a moderate halophile, but its 0.8-M optimum does not qualify for the target phenotype and should therefore be used only as comparative evidence. (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 4-5)

### 2.4 Hybrid regulation and membrane remodeling

Two 2024 studies broaden the binary salt-in/salt-out model. Dead Sea freshwater-spring biofilm MAGs from *Prosthecochloris*, *Flexistipes*, *Izemoplasma*, *Halomonas*, and *Halanaerobium* contained genes for both strategies. The authors hypothesized that abrupt salinity fluctuations select scalable hybrid regulation; because this was inferred from MAG content, simultaneous or condition-dependent pathway use was not experimentally demonstrated. (ionescu2024extremefluctuationsin pages 1-2)

Comparative genomic analysis likewise inferred dual salt-in/salt-out capacity in *Halogeometricum*. Wet-lab experiments in that study validated heavy-metal resistance, not the proposed osmoregulatory switching; therefore, the latter remains genomic inference. (strakova2024unveilingthegenomic pages 1-2)

Membrane adaptation is independently supported by 2024 lipidomics. Relative to its 13% optimum, planktonic *H. congolense* grown at 20% NaCl was enriched in phosphatidylglycerols, cardiolipins, and phosphatidylethanolamines; biofilm growth also increased several zwitterionic phosphatidylcholines and phosphatidylethanolamines. The authors interpreted these shifts as strategic membrane chemistry adjustments enabling stress adaptation and biofilm formation. This supports “20% NaCl induces membrane-lipid remodeling,” but not “lipid remodeling causes a 13% optimum,” because no lipid-pathway perturbation was performed. (ugwuodo2024changesinenvironmental pages 1-2)

## 3. Candidate graph nodes

### 3.1 Trait and environment

- **NaCl optimum high** — **METPO:1000468**
- Parent high-salinity optimum trait — **METPO:1000333**
- High extracellular NaCl concentration — candidate chemical grounding **CHEBI:26710** (sodium chloride)
- Hypersaline growth medium — label-only environmental/assay node unless a verified ENVO term is selected
- Osmotic upshift / hyperosmotic stress — candidate process **GO:0006970** (response to osmotic stress)
- Growth optimum above 8% w/v NaCl — assay-result node; retain threshold and units in node metadata

### 3.2 Ions, solutes, and metabolites

- Potassium ion — **CHEBI:29103**
- Chloride — **CHEBI:17996**
- Intracellular KCl / high intracellular inorganic-ion concentration — process/state node
- Glycine betaine — **CHEBI:17750**
- Ectoine — **CHEBI:16979**
- Trehalose — **CHEBI:27082**
- Sodium ion — **CHEBI:29101**
- Cytoplasmic water activity / osmotic pressure / turgor — label-only state nodes pending exact ontology review

### 3.3 Genes, proteins, and transport modules

- **Trk K⁺ uptake system:** *trkA*, *trkH*; protein-specific accessions must be assigned per strain
- **Kch voltage-gated K⁺ channel:** *kch*
- **Kef K⁺ efflux/K⁺–H⁺ antiport module:** *kefB*
- **Kdp high-affinity K⁺ transport ATPase:** *kdpFABC*; relevant in some taxa but not established as a universal extreme-halophile determinant
- **BCCT-family betaine/carnitine/choline transporter:** strain-specific candidates OM942798 and OM942799 in *H. kocurii*; verify accession namespace before YAML insertion
- **Ectoine biosynthesis:** *ectA*, *ectB*, *ectC*; **EctC/ectoine synthase EC 4.2.1.108** is a candidate grounding
- **Trehalose synthesis:** *treS*; assign EC/UniProt only after strain-specific verification
- **Betaine aldehyde dehydrogenase:** *BADH1*; candidate enzyme activity **EC 1.2.1.8**, subject to sequence/function verification
- **Na⁺/H⁺ antiporter** and **Mrp sodium-export complex** — taxon-specific salt-out/supporting modules
- **Bacteriorhodopsin/respiratory-chain electrochemical-gradient generation** — plausible upstream support for haloarchaeal ion transport, but not universal

### 3.4 Cellular structures and molecular properties

- Cytoplasm
- Plasma membrane — candidate **GO:0005886**
- Acidic proteome / enrichment of Asp and Glu residues
- Reduced protein-surface hydrophobicity
- Phosphatidylglycerol, cardiolipin, phosphatidylethanolamine, and phosphatidylcholine pools
- Compatible-solute pool
- Intracellular K⁺ pool

### 3.5 Taxon/context nodes

- *Halorubrum kocurii* 2020YC7 — direct high-salinity ion/solute-switch evidence
- *Halanaerobium congolense* WG10 — 13% NaCl optimum and lipidomics
- *Halomonas* spp. — direct 10–15% optima in selected isolates
- *Spiribacter salinus* M19-40 — comparative moderate-halophile evidence
- Haloarchaea / class Halobacteria — review-level salt-in and proteome evidence
- Halanaerobiales and *Salinibacter* — independent bacterial salt-in lineages

Taxon identifiers should be resolved against NCBI Taxonomy during implementation rather than inferred from names here.

## 4. Candidate causal edges

The compact table below identifies the strongest core edges. It deliberately distinguishes direct measurements from review synthesis.

| subject | predicate | object | evidence/taxon | confidence | DOI |
|---|---|---|---|---|---|
| high external NaCl | induces | Trk-mediated K+ uptake | Direct experiment in *Halorubrum kocurii* 2020YC7; salinity-dependent upregulation of potassium-uptake machinery, including strong *trkH* induction across 50–250 g/L NaCl (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8) | High | https://doi.org/10.3390/genes13060939 |
| TrkA/TrkH | increases | intracellular K+ concentration | Direct experiment in *H. kocurii* 2020YC7; intracellular K+ rose with salinity, reaching 28.67 µmol/mg protein at 200 g/L NaCl, alongside increased *trkA/trkH* expression (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8) | High | https://doi.org/10.3390/genes13060939 |
| intracellular K+/Cl- accumulation | balances | cytoplasmic osmotic pressure under hypersalinity | Review synthesis across extreme halophiles; KCl accumulation presented as the canonical “salt-in” strategy for osmotic balance, not a direct single-taxon perturbation test (oren2008microbiallifeat pages 1-2) | High (review-level) | https://doi.org/10.1186/1746-1448-4-2 |
| acidic proteome | enables | protein function at high intracellular salt | Review synthesis across salt-in strategists; highly acidic proteomes are described as required for enzymes/proteins to remain functional in near-saturating intracellular salt, with poor low-salt stability (oren2008microbiallifeat pages 1-2, bonnaud2024haloarchaeaaspromising pages 2-4) | High (review-level) | https://doi.org/10.1186/1746-1448-4-2; https://doi.org/10.3390/microorganisms12081738 |
| exogenous glycine betaine uptake via BCCT transporter | substitutes for / reduces reliance on | K+-based osmoprotection at 200–250 g/L NaCl | Direct experiment in *H. kocurii* 2020YC7; BCCT-family transporters inferred genomically and glycine betaine became the primary osmotic solute when supplied exogenously, indicating an osmoprotectant switch; transporter-specific causality partly inferred (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8) | Medium-High | https://doi.org/10.3390/genes13060939 |
| ectoine synthesis/import | supports | osmoadaptation during growth at elevated salinity | Direct physiology plus genomics in moderate halophile *Spiribacter salinus* M19-40; ectoine levels increase under optimal and salt-challenging conditions, but this is not direct evidence for extreme-halophile >8% optimum and is taxon-specific (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 4-5) | Medium | https://doi.org/10.3389/fmicb.2018.00108 |
| 20% NaCl | enriches | phosphatidylglycerols, cardiolipins, and phosphatidylethanolamines relative to 13% NaCl | Direct lipidomics in *Halanaerobium congolense* WG10; 13% NaCl defined as optimum and 20% as hypersalinity, with authors interpreting lipid shifts as adaptive plasma-membrane remodeling (ugwuodo2024changesinenvironmental pages 1-2) | High | https://doi.org/10.1128/spectrum.02334-23 |


*Table: This table summarizes the highest-confidence causal edges relevant to the NaCl optimum high trait, separating direct experiments from review-level synthesis and flagging taxon-specific or partially inferred claims for curation use.*

Additional curation candidates are listed with source snippets and restrictions below.

| Subject | Predicate | Object | Supporting snippet | Reference | Curation note |
|---|---|---|---|---|---|
| External NaCl increase from 100 to 200 g/L | increases | intracellular K⁺ | “8.17 to 28.67 μmol/mg protein K⁺…increasing along with…salinity” | 10.3390/genes13060939 | **Strong, direct, taxon-specific.** Do not generalize beyond *H. kocurii* without a higher-level review edge. (ding2022theosmoprotectantswitch pages 1-2) |
| High NaCl, 50→250 g/L | induces expression of | *trkH* | “*trkH* expression increased 500-fold” | 10.3390/genes13060939 | **Direct RT-qPCR association.** “Induces” is acceptable; “is required for growth” is not established without knockout evidence. (ding2022theosmoprotectantswitch pages 6-8) |
| TrkA/TrkH/Kch module | transports | K⁺ into cytoplasm | Genes for K⁺ uptake were identified and their expression tracked salinity-dependent K⁺ accumulation | 10.3390/genes13060939 | **Medium–high.** Transport function plus physiological correlation; individual contribution was not genetically dissected. (ding2022theosmoprotectantswitch pages 4-6, ding2022theosmoprotectantswitch pages 6-8) |
| Intracellular KCl accumulation | balances | extracellular osmotic pressure | “accumulation of molar concentrations of KCl” is one of two principal osmotic strategies | 10.1186/1746-1448-4-2 | **Strong review-level mechanism.** Suitable as a generic salt-in edge. (oren2008microbiallifeat pages 1-2) |
| Salt-in strategy | selects for / requires | acidic proteome | Intracellular machinery must remain active at near-saturating salt; proteomes are highly acidic | 10.1186/1746-1448-4-2 | Prefer **requires/adaptively associated with**, not a short-timescale induction predicate. (oren2008microbiallifeat pages 1-2) |
| Acidic protein surfaces | promote | protein solubility/function at high salt | Negative residues form hydrated cation networks that maintain solubility | 10.3390/microorganisms12081738 | **Review-level; haloarchaeal context.** (bonnaud2024haloarchaeaaspromising pages 2-4) |
| Exogenous glycine betaine | increases | intracellular glycine betaine | Accumulated to 15.27 mg/mg protein at 200–250 g/L | 10.3390/genes13060939 | **Strong direct edge** conditional on extracellular betaine. (ding2022theosmoprotectantswitch pages 1-2) |
| Glycine-betaine accumulation | reduces reliance on | K⁺ osmoprotection | Betaine became the primary osmotic solute and altered K⁺ transport-gene expression | 10.3390/genes13060939 | **Direct switch phenotype;** transporter-to-phenotype edge remains partly inferred. (ding2022theosmoprotectantswitch pages 6-8, ding2022theosmoprotectantswitch pages 2-4) |
| BCCT transporter candidates | mediate | glycine-betaine uptake | Two BCCT genes were identified in a strain unable to synthesize betaine | 10.3390/genes13060939 | **Uncertain/partly inferred:** curate only with an evidence qualifier until mutant or heterologous transport evidence is available. (ding2022theosmoprotectantswitch pages 6-8) |
| Increasing NaCl, 50→250 g/L | decreases | intracellular trehalose | Trehalose declined from 5.26 to 2.61 mg/mg protein | 10.3390/genes13060939 | **Direct inverse edge.** Indicates trehalose is not the principal highest-salt osmolyte in this strain. (ding2022theosmoprotectantswitch pages 1-2) |
| Ectoine synthesis/import | supports | osmotic-stress growth | Enhanced ectoine and salinity-regulated betaine uptake were measured in *S. salinus* | 10.3389/fmicb.2018.00108 | **Comparative only:** organism’s optimum is 0.8 M and does not meet the supplied threshold. (leon2018compatiblesolutesynthesis pages 1-2, leon2018compatiblesolutesynthesis pages 4-5) |
| 20% versus 13% NaCl | enriches | phosphatidylglycerol, cardiolipin, and phosphatidylethanolamine pools | These lipids were “predominantly enriched” at hypersalinity | 10.1128/spectrum.02334-23 | **Strong direct lipidomics edge;** adaptation/function is interpretive rather than perturbational. (ugwuodo2024changesinenvironmental pages 1-2) |
| Rapidly fluctuating salinity | selects for | hybrid salt-in/salt-out genomic capacity | MAGs contain genes for both strategies; authors hypothesize scalable adaptation | 10.3389/frmbi.2023.1329925 | **Uncertain:** ecological hypothesis based on MAGs, not pathway activity. (ionescu2024extremefluctuationsin pages 1-2) |
| *ectC* | catalyzes | final ectoine-biosynthesis step | *ectC* encodes a 129-aa ectoine synthase catalyzing the final step | 10.1038/s41598-024-63581-z | Enzyme-function edge is appropriate; gene presence alone is not evidence of a high optimum. (reang2024extremozymesandcompatible pages 8-11) |
| BADH1 | catalyzes | betaine aldehyde→glycine betaine | 1,473-bp gene encodes a 490-aa polypeptide for the conversion | 10.1038/s41598-024-63581-z | Enzyme edge appropriate after sequence/accession verification. (reang2024extremozymesandcompatible pages 8-11) |

### Minimal recommended core graph

For a compact TraitMech graph, the highest-confidence path is:

**high extracellular NaCl → hyperosmotic stress → Trk-mediated K⁺ uptake → elevated intracellular K⁺/KCl → osmotic balance → growth at high NaCl**, with a parallel adaptation branch **salt-in strategy → acidic proteome → macromolecular function at high intracellular salt → high-NaCl growth**. A conditional alternative is **available glycine betaine → BCCT-mediated uptake → compatible-solute accumulation → osmotic balance**, but the BCCT-specific edge should be qualified as inferred. (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8, oren2008microbiallifeat pages 1-2)

## 5. Recent developments and quantitative evidence, 2023–2024

### 5.1 Hybrid osmoadaptation is increasingly recognized

The 2024 Dead Sea study recovered five bacterial MAGs with both salt-in and salt-out genes and proposed that frequent, abrupt salinity changes favor hybrid, scalable regulation. A separate October 2024 *Halogeometricum* analysis also inferred dual osmoregulation. Together these studies challenge a rigid one-strategy-per-lineage model, but both conclusions about osmotic switching remain computational rather than experimentally validated. (ionescu2024extremefluctuationsin pages 1-2, strakova2024unveilingthegenomic pages 1-2)

### 5.2 Membrane lipidomics provides a new mechanistic layer

The January 2024 *H. congolense* study directly compared 7%, 13%, and 20% NaCl. Enrichment of anionic and zwitterionic membrane lipids at 20% or during biofilm growth indicates that high-salt persistence involves membrane-state regulation in addition to cytoplasmic osmolytes. This is especially relevant to fractured-shale systems, where persistent halophiles form biofilms, sour reservoirs through sulfide production, corrode infrastructure, and reduce permeability. (ugwuodo2024changesinenvironmental pages 1-2)

### 5.3 Recent isolate and MAG statistics

A July 2024 survey analyzed **15 strains**: six *Halomonas pacifica*, one *H. stenophila*, two *H. salifodinae*, one *H. binhaiensis*, one *Oceanobacillus oncorhynchi*, and four *Bacillus paralicheniformis*. Ten *Halomonas* isolates had **10–15% NaCl optima** and tolerated 25%. Measured activities were **6.90–35.38 U/mL protease**, **0.004–0.042 U/mL cellulase**, and **0.097–0.550 U/mL chitinase**; ectoine production was **0.01–3.17 mg/L**. PCR detected *ectC* and *BADH1* in all 15 isolates, although five had no detectable ectoine under the assay conditions. (reang2024extremozymesandcompatible pages 1-2, reang2024extremozymesandcompatible pages 4-5, reang2024extremozymesandcompatible pages 3-4, reang2024extremozymesandcompatible pages 2-3)

A March 2024 genome-resolved metagenomic study reconstructed **67 MAGs**: 15 with MEGAHIT, 26 with metaSPAdes, and 26 with IDBA-UD. Among medium/high-quality metaSPAdes MAGs, annotations indicated salt tolerance in **91.3%**, heavy-metal tolerance in **95.6%**, exopolysaccharide biosynthesis in **95.6%**, and antioxidant biosynthesis in **60.86%**; iron acquisition and potassium solubilization occurred in 91.3%. These percentages describe annotated genetic potential, not measured high-NaCl optima or causal mechanisms. (dindhoria2024metagenomicassembledgenomes pages 1-2)

## 6. Applications and real-world implementation

### 6.1 Haloarchaeal production chassis and green chemistry

Haloarchaea are being developed as chassis for producing functional halophilic enzymes and other molecules under hypersaline process conditions. A 2024 review describes haloarchaeal optima broadly in the **10–35% NaCl** range and argues that a salt-in host is advantageous for expressing enzymes that themselves require high salt. Potential benefits include reduced contamination, process robustness, and direct production of correctly folded halophilic proteins. The chief limitation is the still-restricted genetic toolkit and the difficulty of downstream processing in concentrated brines. (bonnaud2024haloarchaeaaspromising pages 2-4)

### 6.2 Compatible solutes and extremozymes

Ectoine and glycine betaine are valuable as protein/cell protectants, while halophilic proteases, cellulases, and chitinases are candidates for saline industrial reactions, biofuel workflows, and biocontrol. The 2024 isolate study supplies quantitative production data, but the authors explicitly cautioned that compatible-solute protection of the measured extremozymes was “purely our assumption” and required further investigation. That claimed causal link should not be curated. (reang2024extremozymesandcompatible pages 1-2, reang2024extremozymesandcompatible pages 15-16, reang2024extremozymesandcompatible pages 16-16)

### 6.3 Agriculture and salinized soils

Hypersaline microbiomes are being investigated as inoculants to alleviate crop salt stress and supply plant-growth-promoting functions. The 67-MAG study found widespread annotated salt tolerance, exopolysaccharide capacity, phosphate solubilization, IAA-production potential, iron acquisition, and potassium solubilization. These findings motivate biofertilizer development but remain largely genomic predictions rather than field-demonstrated implementation. (dindhoria2024metagenomicassembledgenomes pages 1-2)

### 6.4 Engineered subsurface systems

In fractured shale, *Halanaerobium* can persist at brine salinities, produce sulfide, corrode infrastructure, and form permeability-reducing biofilms. The 2024 lipidomic data provide potential biomarkers or intervention targets for salinity-dependent activity, although no lipid-directed biocontrol treatment was demonstrated. (ugwuodo2024changesinenvironmental pages 1-2)

## 7. Expert analysis and curation interpretation

The literature supports a **modular rather than single-gene** interpretation. A high NaCl optimum emerges from coordinated ion or osmolyte homeostasis, proteome compatibility, membrane function, energy metabolism, and cell-envelope stability. Oren’s synthesis remains authoritative because it connects intracellular KCl to proteome-wide acidification and explains why salt-in organisms often lose function at low salinity. Recent studies refine this model by showing osmoprotectant switching, mixed genomic repertoires, and membrane remodeling. (ding2022theosmoprotectantswitch pages 6-8, oren2008microbiallifeat pages 1-2, ionescu2024extremefluctuationsin pages 1-2, ugwuodo2024changesinenvironmental pages 1-2)

For TraitMech, evidence should be represented at three levels:

1. **Generic mechanism edges** supported by broad reviews, such as intracellular KCl producing osmotic balance.
2. **Taxon-specific experimental edges**, such as NaCl increasing *trkH* expression and intracellular K⁺ in *H. kocurii*.
3. **Hypothesis/inference edges**, such as a MAG encoding both strategies or a transporter being assigned from sequence alone.

This separation prevents a genomic feature such as *ectC*, *trkH*, or a BCCT transporter from being treated as sufficient evidence that a strain has a >8% NaCl optimum.

## 8. Warnings: claims not ready for TraitMech curation

1. **Do not equate “extreme halophile” with the supplied >8% threshold.** The classical extreme category begins around 2.5 M NaCl, whereas the METPO threshold is approximately 1.37 M. (oren2008microbiallifeat pages 1-2)
2. **Do not infer the trait from maximum tolerance.** *S. salinus* tolerates ~2 M but has a 0.8-M optimum. (leon2018compatiblesolutesynthesis pages 4-5)
3. **Do not infer phenotype from gene presence alone.** MAG annotations for salt tolerance, *ectABC*, Trk, Kdp, BCCT, or Mrp require phenotype confirmation. (dindhoria2024metagenomicassembledgenomes pages 1-2, ionescu2024extremefluctuationsin pages 1-2)
4. **Do not curate hybrid strategy deployment as demonstrated** for Dead Sea MAGs or *Halogeometricum*; pathway co-occurrence was inferred in silico. (ionescu2024extremefluctuationsin pages 1-2, strakova2024unveilingthegenomic pages 1-2)
5. **Do not assert BCCT-specific causality without perturbation.** Betaine uptake was measured in *H. kocurii*, but assignment to either candidate transporter is not genetically resolved. (ding2022theosmoprotectantswitch pages 6-8)
6. **Do not claim trehalose supports the highest tested salinities in *H. kocurii*.** Its concentration and *treS* expression decreased as NaCl rose, supporting a lower-salinity role. (ding2022theosmoprotectantswitch pages 1-2, ding2022theosmoprotectantswitch pages 6-8)
7. **Do not claim lipid remodeling causes the high optimum.** The 20%-versus-13% lipid changes are direct associations and adaptive interpretations, not knockout-validated causes. (ugwuodo2024changesinenvironmental pages 1-2)
8. **Do not curate compatible-solute protection of extremozymes from Reang et al. as causal.** The authors called it an assumption requiring validation. (reang2024extremozymesandcompatible pages 16-16)
9. **Do not make Kdp, bacteriorhodopsin, halorhodopsin, EPS, or biofilm formation universal nodes.** Each is lineage- or condition-specific and requires direct evidence tied to the target strain and phenotype.
10. **Do not assign UniProt, NCBITaxon, Rhea, or strain-specific identifiers by name matching alone.** Resolve sequences and taxonomic records before inserting CURIEs.

## 9. DOI-first bibliography

1. **Ding R, Yang N, Liu J.** “The Osmoprotectant Switch of Potassium to Compatible Solutes in an Extremely Halophilic Archaea *Halorubrum kocurii* 2020YC7.” *Genes* 13, 939. **May 2022.** DOI: **10.3390/genes13060939**. https://doi.org/10.3390/genes13060939 (ding2022theosmoprotectantswitch pages 1-2)
2. **Ugwuodo CJ et al.** “Changes in environmental and engineered conditions alter the plasma membrane lipidome of fractured shale bacteria.” *Microbiology Spectrum* 12. **January 2024.** DOI: **10.1128/spectrum.02334-23**. https://doi.org/10.1128/spectrum.02334-23 (ugwuodo2024changesinenvironmental pages 1-2)
3. **Ionescu D et al.** “Extreme fluctuations in ambient salinity select for bacteria with a hybrid ‘salt-in’/‘salt-out’ osmoregulation strategy.” *Frontiers in Microbiomes* 2. **January 2024.** DOI: **10.3389/frmbi.2023.1329925**. https://doi.org/10.3389/frmbi.2023.1329925 (ionescu2024extremefluctuationsin pages 1-2)
4. **Straková D et al.** “Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus *Halogeometricum*.” *Frontiers in Marine Science* 11. **October 2024.** DOI: **10.3389/fmars.2024.1421769**. https://doi.org/10.3389/fmars.2024.1421769 (strakova2024unveilingthegenomic pages 1-2)
5. **Reang L et al.** “Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria…” *Scientific Reports* 14. **July 2024.** DOI: **10.1038/s41598-024-63581-z**. https://doi.org/10.1038/s41598-024-63581-z (reang2024extremozymesandcompatible pages 1-2)
6. **Dindhoria K et al.** “Metagenomic assembled genomes indicated the potential application of hypersaline microbiome…” *mSystems* 9. **March 2024.** DOI: **10.1128/msystems.01050-23**. https://doi.org/10.1128/msystems.01050-23 (dindhoria2024metagenomicassembledgenomes pages 1-2)
7. **Bonnaud E et al.** “Haloarchaea as Promising Chassis to Green Chemistry.” *Microorganisms* 12, 1738. **August 2024.** DOI: **10.3390/microorganisms12081738**. https://doi.org/10.3390/microorganisms12081738 (bonnaud2024haloarchaeaaspromising pages 2-4)
8. **León MJ et al.** “Compatible Solute Synthesis and Import by the Moderate Halophile *Spiribacter salinus*.” *Frontiers in Microbiology* 9. **February 2018.** DOI: **10.3389/fmicb.2018.00108**. https://doi.org/10.3389/fmicb.2018.00108 (leon2018compatiblesolutesynthesis pages 1-2)
9. **Oren A.** “Microbial life at high salt concentrations: phylogenetic and metabolic diversity.” *Saline Systems* 4:2. **April 2008.** DOI: **10.1186/1746-1448-4-2**. https://doi.org/10.1186/1746-1448-4-2 (oren2008microbiallifeat pages 1-2)

**Recommended curation decision:** retain the existing salt-in/KCl and acidic-proteome backbone; add taxon-qualified Trk→K⁺ and glycine-betaine-switch edges from *H. kocurii*; add membrane-lipid remodeling only as a stress-response branch; and place hybrid-strategy, MAG-based, and extremozyme-protection claims in an uncertain or non-curated evidence layer.

References

1. (ding2022theosmoprotectantswitch pages 1-2): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

2. (oren2008microbiallifeat pages 1-2): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

3. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 15 citations.

4. (ugwuodo2024changesinenvironmental pages 1-2): Chika Jude Ugwuodo, Fabrizio Colosimo, Jishnu Adhikari, Kent Bloodsworth, Stephanie A. Wright, Josie Eder, and Paula J. Mouser. Changes in environmental and engineered conditions alter the plasma membrane lipidome of fractured shale bacteria. Jan 2024. URL: https://doi.org/10.1128/spectrum.02334-23, doi:10.1128/spectrum.02334-23. This article has 3 citations and is from a domain leading peer-reviewed journal.

5. (leon2018compatiblesolutesynthesis pages 4-5): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

6. (reang2024extremozymesandcompatible pages 4-5): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.

7. (reang2024extremozymesandcompatible pages 2-3): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.

8. (ding2022theosmoprotectantswitch pages 6-8): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

9. (bonnaud2024haloarchaeaaspromising pages 2-4): Emma Bonnaud, Philippe M. Oger, Avigaël Ohayon, and Yoann Louis. Haloarchaea as promising chassis to green chemistry. Microorganisms, 12:1738, Aug 2024. URL: https://doi.org/10.3390/microorganisms12081738, doi:10.3390/microorganisms12081738. This article has 8 citations.

10. (ding2022theosmoprotectantswitch pages 4-6): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

11. (leon2018compatiblesolutesynthesis pages 1-2): María J. León, Tamara Hoffmann, Cristina Sánchez-Porro, Johann Heider, Antonio Ventosa, and Erhard Bremer. Compatible solute synthesis and import by the moderate halophile spiribacter salinus: physiology and genomics. Frontiers in Microbiology, Feb 2018. URL: https://doi.org/10.3389/fmicb.2018.00108, doi:10.3389/fmicb.2018.00108. This article has 77 citations and is from a peer-reviewed journal.

12. (ding2022theosmoprotectantswitch pages 2-4): Runting Ding, Na Yang, and Jianguo Liu. The osmoprotectant switch of potassium to compatible solutes in an extremely halophilic archaea halorubrum kocurii 2020yc7. Genes, 13:939, May 2022. URL: https://doi.org/10.3390/genes13060939, doi:10.3390/genes13060939. This article has 25 citations.

13. (strakova2024unveilingthegenomic pages 1-2): Dáša Straková, Cristina Sánchez-Porro, Rafael R. de la Haba, and Antonio Ventosa. Unveiling the genomic landscape and adaptive mechanisms of the haloarchaeal genus halogeometricum: spotlight on thiamine biosynthesis. Frontiers in Marine Science, Oct 2024. URL: https://doi.org/10.3389/fmars.2024.1421769, doi:10.3389/fmars.2024.1421769. This article has 7 citations.

14. (reang2024extremozymesandcompatible pages 8-11): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.

15. (reang2024extremozymesandcompatible pages 1-2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.

16. (reang2024extremozymesandcompatible pages 3-4): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.

17. (dindhoria2024metagenomicassembledgenomes pages 1-2): Kiran Dindhoria, Raghawendra Kumar, Bhavya Bhargava, and Rakshak Kumar. Metagenomic assembled genomes indicated the potential application of hypersaline microbiome for plant growth promotion and stress alleviation in salinized soils. Mar 2024. URL: https://doi.org/10.1128/msystems.01050-23, doi:10.1128/msystems.01050-23. This article has 27 citations and is from a peer-reviewed journal.

18. (reang2024extremozymesandcompatible pages 15-16): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.

19. (reang2024extremozymesandcompatible pages 16-16): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 18 citations and is from a peer-reviewed journal.